from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(sys.argv[1]).resolve()
OUTPUT_DIR = ROOT / "tmp"


def normalize_path(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def extract_questions(body: str) -> list[dict[str, object]]:
    old_match = re.search(r"(?ms)^\*\*原题\*\*\s*(.*?)^\*\*参考解答\*\*", body)
    question_area = old_match.group(1) if old_match else body.split("> [!note]- 分析与解答", 1)[0]
    records: list[dict[str, object]] = []
    for line in question_area.splitlines():
        if not line.startswith("+ "):
            continue
        sources = [
            {"year": match.group(1), "path": match.group(2)}
            for match in re.finditer(r"\[(\d{4})\]\((test/[^)]+)\)", line)
        ]
        if not sources:
            continue
        text = re.sub(r"\s*\(?(?:\[\d{4}\]\(test/[^)]+\)\s*,?\s*)+\)?", " ", line[2:])
        text = re.sub(r"〔[^〕]+〕", "", text).strip()
        text = text.removeprefix("「").removesuffix("」").strip()
        records.append({"text": text, "sources": sources, "raw": line})
    return records


entries: list[dict[str, object]] = []
for path in sorted(ROOT.rglob("QUESTIONS*.md")):
    if "tmp" in path.parts or ".agents" in path.parts:
        continue
    raw = path.read_text(encoding="utf-8")
    section_pattern = re.compile(
        r"(?ms)^### Q(?P<number>\d{2}) (?P<title>.+?)\s*$\n(?P<body>.*?)(?=^### Q\d{2} |^## |\Z)"
    )
    for section in section_pattern.finditer(raw):
        body = section.group("body")
        entries.append(
            {
                "file": normalize_path(path),
                "course_dir": normalize_path(path.parent),
                "number": int(section.group("number")),
                "title": section.group("title").strip(),
                "questions": extract_questions(body),
                "body": body.rstrip(),
            }
        )

catalog_path = OUTPUT_DIR / "question_catalog.json"
catalog_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")

summary_lines = ["# 现有题库抽取索引", ""]
current_course = None
for entry in entries:
    course = str(entry["course_dir"])
    if course != current_course:
        summary_lines.extend([f"## {course}", ""])
        current_course = course
    summary_lines.append(f"### {entry['file']} · Q{entry['number']:02d} {entry['title']}")
    summary_lines.append("")
    for question in entry["questions"]:
        source_text = "，".join(
            f"{source['year']}:{source['path']}" for source in question["sources"]
        )
        summary_lines.append(f"+ {question['text']} 〔{source_text}〕")
    summary_lines.append("")

(OUTPUT_DIR / "question_catalog.md").write_text("\n".join(summary_lines), encoding="utf-8")
print(f"Cataloged {len(entries)} question clusters")
