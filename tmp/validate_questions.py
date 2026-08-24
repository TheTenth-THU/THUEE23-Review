from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


REQUIRED_SECTIONS = ("分析", "解答", "拓展", "关联")
Q_HEADING_RE = re.compile(r"^### Q(\d{2})\s+(.+)$", re.MULTILINE)
SOURCE_RE = re.compile(r"\[(20\d{2})\]\((test/[^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
UNESCAPED_PIPE_RE = re.compile(r"(?<!\\)\|")


def split_wikilink(raw: str) -> tuple[str, str | None]:
    parts = UNESCAPED_PIPE_RE.split(raw, maxsplit=1)
    target = parts[0].replace(r"\|", "|")
    if "#" in target:
        file_target, fragment = target.split("#", 1)
        return file_target, fragment
    return target, None


def resolve_note(vault: Path, question_file: Path, target: str) -> Path | None:
    target = unquote(target).replace("/", str(Path("/"))).replace("\\", str(Path("/")))
    candidate = Path(target)
    if candidate.suffix.lower() != ".md":
        candidate = candidate.with_suffix(".md")

    direct_candidates = []
    if "/" in target or "\\" in target:
        direct_candidates.append(vault / candidate)
    else:
        direct_candidates.append(question_file.parent / candidate)

    for direct in direct_candidates:
        if direct.exists():
            return direct

    matches = [path for path in vault.rglob(candidate.name) if "raw" not in path.parts]
    if len(matches) == 1:
        return matches[0]
    return None


def audit_file(vault: Path, question_file: Path) -> list[tuple[str, str]]:
    text = question_file.read_text(encoding="utf-8")
    issues: list[tuple[str, str]] = []
    relative = question_file.relative_to(vault).as_posix()
    questions = list(Q_HEADING_RE.finditer(text))

    expected = list(range(1, len(questions) + 1))
    actual = [int(match.group(1)) for match in questions]
    if actual != expected:
        issues.append(("numbering", f"{actual} != {expected}"))

    if re.search(r"^##\s+(原题|原题与参考解答|面试题)", text, re.MULTILINE):
        issues.append(("empty_category", "存在无信息量二级标题"))

    blocks = re.split(r"(?=^### Q\d{2}\s+)", text, flags=re.MULTILINE)[1:]
    for block in blocks:
        header = block.splitlines()[0]
        source_lines = [
            line for line in block.splitlines()
            if line.startswith("+ (") and SOURCE_RE.search(line)
        ]
        if not source_lines:
            issues.append(("missing_original", header))
        if block.count("> [!note]- 分析与解答") != 1:
            issues.append(("callout_count", header))
        for section in REQUIRED_SECTIONS:
            if block.count(f"> **{section}**") != 1:
                issues.append(("section_count", f"{header}: {section}"))

    for _, source in SOURCE_RE.findall(text):
        source_path = vault / unquote(source)
        if not source_path.exists():
            issues.append(("missing_source", source))

    for raw_link in WIKILINK_RE.findall(text):
        target, fragment = split_wikilink(raw_link)
        note = resolve_note(vault, question_file, target)
        if note is None:
            issues.append(("missing_note", raw_link))
            continue
        if fragment:
            headings = set(HEADING_RE.findall(note.read_text(encoding="utf-8")))
            if fragment not in headings:
                issues.append(("missing_heading", raw_link))

    if not issues:
        issues.append(("ok", f"{len(questions)} questions"))
    return [(relative, f"{kind}\t{detail}") for kind, detail in issues]


def main() -> int:
    vault = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    report_path = vault / "tmp" / "questions_validation.tsv"
    rows: list[tuple[str, str]] = []
    question_files = sorted({
        *vault.glob("*/*/QUESTIONS.md"),
        *vault.glob("*/QUESTIONS.md"),
    })
    for question_file in question_files:
        rows.extend(audit_file(vault, question_file))

    lines = ["file\tstatus\tdetail"]
    for relative, result in rows:
        status, detail = result.split("\t", 1)
        lines.append(f"{relative}\t{status}\t{detail}")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    problems = [row for row in rows if not row[1].startswith("ok\t")]
    print(f"Validated {len(question_files)} files; "
          f"issues: {len(problems)}; report: {report_path.relative_to(vault)}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
