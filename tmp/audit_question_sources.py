from __future__ import annotations

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path(sys.argv[1]).resolve()
TMP = ROOT / "tmp"
SOURCE_TEXT = TMP / "source_text"


def normalized(text: str) -> str:
    text = re.sub(r"\$.*?\$", " ", text)
    text = re.sub(r"[`*_\\{}\[\]()]", " ", text)
    return re.sub(r"[^0-9A-Za-z\u3400-\u9fff]+", "", text).lower()


def grams(text: str) -> set[str]:
    value = normalized(text)
    chinese = "".join(re.findall(r"[\u3400-\u9fff]", value))
    tokens = set(re.findall(r"[a-z0-9]+", value))
    tokens.update(chinese[index : index + 2] for index in range(max(0, len(chinese) - 1)))
    return {token for token in tokens if token}


def prepare_source(source: str) -> tuple[set[str], list[tuple[str, set[str]]]]:
    all_grams = grams(source)
    raw_lines = [line.strip() for line in source.splitlines() if line.strip()]
    windows = []
    for index, line in enumerate(raw_lines):
        window = " ".join(raw_lines[index : index + 3])
        windows.append((window[:240], grams(window)))
    return all_grams, windows


def best_line(question: str, prepared: tuple[set[str], list[tuple[str, set[str]]]]) -> tuple[float, str]:
    question_grams = grams(question)
    if not question_grams:
        return 0.0, ""
    all_grams, windows = prepared
    global_score = len(question_grams & all_grams) / len(question_grams)
    best_excerpt = ""
    best_overlap = -1
    for excerpt, line_grams in windows:
        overlap = len(question_grams & line_grams)
        if overlap > best_overlap:
            best_overlap = overlap
            best_excerpt = excerpt
    return global_score, best_excerpt


def object_kind(logical_name: str) -> str:
    if "::" not in logical_name:
        return "regular"
    if logical_name.endswith("推研面经2024.md"):
        return "zip-interview"
    if any(name in logical_name for name in ("问题answer", "核心课复习")):
        return "zip-preparation"
    return "zip-other"


def select_best_candidate(
    question: str,
    candidates: list[tuple[str, tuple[set[str], list[tuple[str, set[str]]]]]],
) -> tuple[float, str, str]:
    scored: list[tuple[float, str, str]] = []
    for logical_name, prepared in candidates:
        score, excerpt = best_line(question, prepared)
        scored.append((score, logical_name, excerpt))
    if not scored:
        return 0.0, "", ""

    # 同一 ZIP 中的实际面经与备考答案不是同等证据。只要实际面经对题目
    # 有可识别覆盖，就优先在实际面经中取最佳匹配；备考答案只用于暴露
    # 「题目可能仅来自复习材料」的异常，不得以更长、更像的答案文本覆盖现场记录。
    interview = [item for item in scored if object_kind(item[1]) == "zip-interview"]
    best_interview = max(interview, default=(0.0, "", ""), key=lambda item: item[0])
    if best_interview[0] >= 0.15:
        return best_interview
    return max(scored, key=lambda item: item[0])


objects: dict[str, list[tuple[str, tuple[set[str], list[tuple[str, set[str]]]]]]] = defaultdict(list)
for row in csv.reader((SOURCE_TEXT / "INDEX.tsv").read_text(encoding="utf-8").splitlines(), delimiter="\t"):
    if len(row) < 2:
        continue
    logical_name, output_name = row[0], row[1]
    top_name = logical_name.split("::", 1)[0]
    source_text = (SOURCE_TEXT / output_name).read_text(encoding="utf-8")
    objects[top_name].append((logical_name, prepare_source(source_text)))

catalog = json.loads((TMP / "question_catalog.json").read_text(encoding="utf-8"))
rows: list[dict[str, object]] = []
for entry in catalog:
    for question in entry["questions"]:
        for source in question["sources"]:
            source_name = Path(source["path"]).name
            candidates = objects.get(source_name, [])
            best = select_best_candidate(question["text"], candidates)
            evidence_kind = object_kind(best[1])
            rows.append(
                {
                    "course": entry["course_dir"],
                    "file": entry["file"],
                    "number": f"Q{entry['number']:02d}",
                    "title": entry["title"],
                    "question": question["text"],
                    "source": source["path"],
                    "score": round(best[0], 3),
                    "evidence_kind": evidence_kind,
                    "best_object": best[1],
                    "excerpt": best[2],
                }
            )

fieldnames = list(rows[0]) if rows else []
with (TMP / "question_source_audit.tsv").open("w", encoding="utf-8", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=fieldnames, delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)

review = sorted(rows, key=lambda row: (str(row["evidence_kind"]), float(row["score"])))
lines = ["# 题目来源自动核对", "", "低相似度只表示需要人工复核，不自动判定题目错误。", ""]
for row in review:
    if float(row["score"]) >= 0.58 and row["evidence_kind"] != "zip-preparation":
        continue
    lines.extend(
        [
            f"## {row['course']} · {row['number']} {row['title']}",
            "",
            f"+ 题目：{row['question']}",
            f"+ 来源：{row['source']}",
            f"+ 最佳对象：{row['best_object']}",
            f"+ 类型：{row['evidence_kind']}；覆盖分数：{row['score']}",
            f"+ 邻近文本：{row['excerpt']}",
            "",
        ]
    )
(TMP / "question_source_review.md").write_text("\n".join(lines), encoding="utf-8")
print(f"Audited {len(rows)} question-source pairs; review items: {(len(lines) - 4) // 8}")
