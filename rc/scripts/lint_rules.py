#!/usr/bin/env python3
"""Minimalist rule & skill linter for /rc standards (<=10 content words, <=100 chars, no **, no inline headers)."""
import glob
import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

STOP_WORDS = {
    # RU prepositions, conjunctions, particles, pronouns, numbers/symbols
    "в", "во", "на", "с", "со", "к", "ко", "по", "из", "от", "до", "для", "при", "про", "без", "через", "над", "под",
    "за", "между", "перед", "о", "об", "обо", "у", "и", "а", "но", "или", "либо", "да", "не", "ни", "же", "бы", "ли",
    "что", "чтобы", "как", "если", "то", "так", "также", "только", "все", "всё", "это", "этот", "эта", "эти", "этого",
    "том", "же", "их", "его", "ее", "её", "свой", "свои", "своих", "один", "одной", "одним", "два", "двух", "три",
    # EN prepositions, conjunctions, articles, particles
    "a", "an", "the", "in", "on", "at", "to", "for", "of", "with", "by", "from", "up", "about", "into", "over",
    "after", "under", "between", "out", "against", "during", "without", "before", "around", "among", "and", "or",
    "but", "nor", "so", "yet", "if", "then", "else", "when", "where", "while", "as", "than", "that", "this", "these",
    "those", "it", "its", "their", "your", "all", "any", "each", "every", "no", "not", "only", "own", "same", "such",
    "too", "very", "can", "will", "just", "should", "now", "is", "are", "was", "were", "be", "been", "being", "per",
}

TOKEN_RE = re.compile(r"[A-Za-zА-Яа-яЁё]{2,}")
INLINE_HEADER_RE = re.compile(r"^-\s+(?:‼\s+|!+\s+)?[A-ZА-ЯЁ][^:.\n]{1,30}:\s+")


def count_content_words(line: str) -> list[str]:
    # Strip leading bullet and markers
    body = re.sub(r"^-\s*(?:‼|!+|✅|❌|💬|\s)+", "", line)
    # Strip markdown link targets [text](target) -> text
    body = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", body)
    words = TOKEN_RE.findall(body.lower())
    return [w for w in words if w not in STOP_WORDS]


def lint_file(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    in_code_block = False
    in_frontmatter = False

    if path.name in ("SKILL.md", "SKILL_RU.md"):
        desc_match = re.search(r'^description:\s*"([^"]*)"', text, re.MULTILINE)
        if not desc_match:
            errors.append(f"{path}:1: missing valid description in YAML frontmatter")
        else:
            desc = desc_match.group(1)
            if desc.endswith("."):
                errors.append(f"{path}:1: trailing period in description is prohibited: {desc}")
            if path.name == "SKILL.md" and not desc.startswith("Use when"):
                errors.append(f"{path}:1: EN description must start with 'Use when': {desc}")
            if path.name == "SKILL_RU.md" and not desc.startswith("Применяй когда"):
                errors.append(f"{path}:1: RU description must start with 'Применяй когда': {desc}")

        required_headers = (
            ("## Goal", "## Role", "## Thinking", "## Steps")
            if path.name == "SKILL.md"
            else ("## Цель", "## Роль", "## Мышление", "## Шаги")
        )
        for hdr in required_headers:
            if hdr not in text:
                errors.append(f"{path}:1: missing mandatory skill section '{hdr}'")

    for idx, raw_line in enumerate(text.splitlines(), start=1):
        stripped = raw_line.strip()
        if idx == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block or not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("<!--") or stripped.endswith("-->"):
            continue
        if stripped.startswith("|") and stripped.endswith("|"):
            continue

        char_len = len(stripped)
        if char_len > 100:
            errors.append(f"{path}:{idx}: length {char_len} > 100 chars: {stripped}")

        if not stripped.startswith("- "):
            continue

        if re.search(r"!{3,}", stripped):
            errors.append(f"{path}:{idx}: prohibited exclamation marker (!{{3,}}): {stripped}")

        if "**" in stripped and "`" not in stripped:
            errors.append(f"{path}:{idx}: prohibited bold (**): {stripped}")

        # Skip example lines (✅ / ❌ / 💬) and Thinking template bullets from strict word/header checks
        if any(m in stripped for m in ("✅", "❌", "💬")):
            continue
        if re.match(r"^-\s+(Целевой адресат|Суть|Ограничения|Target Audience|Essence|Constraints):", stripped):
            continue

        if INLINE_HEADER_RE.match(stripped):
            errors.append(f"{path}:{idx}: prohibited inline pre-header with colon: {stripped}")

        cwords = count_content_words(stripped)
        if len(cwords) > 10:
            errors.append(
                f"{path}:{idx}: {len(cwords)} content words > 10 ({', '.join(cwords)}): {stripped}"
            )

    return errors


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python lint_rules.py <file.md> [...]")
        return 2
    all_errors: list[str] = []
    for arg in sys.argv[1:]:
        if any(c in arg for c in "*?"):
            matched = list(Path(".").glob(arg)) if not Path(arg).is_absolute() else [Path(p) for p in glob.glob(arg)]
            for p in matched:
                all_errors.extend(lint_file(p))
        else:
            all_errors.extend(lint_file(Path(arg)))
    if all_errors:
        for err in all_errors:
            print(err)
        print(f"\nFAILED: {len(all_errors)} violation(s) found.")
        return 1
    print("OK: 0 violations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
