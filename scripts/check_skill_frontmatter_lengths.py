#!/usr/bin/env python3
"""Check skill frontmatter description lengths without third-party packages."""

from __future__ import annotations

import argparse
from pathlib import Path


DEFAULT_LIMIT = 1024


def frontmatter(text: str) -> str | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return "\n".join(lines[1:index])
    return None


def description_from_frontmatter(block: str) -> str:
    lines = block.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("description:"):
            _, value = line.split(":", 1)
            value = value.strip()
            if value in {">-", ">", "|-", "|"}:
                collected: list[str] = []
                for follow in lines[index + 1 :]:
                    if follow.startswith((" ", "\t")):
                        collected.append(follow.strip())
                    elif not follow.strip():
                        collected.append("")
                    else:
                        break
                return " ".join(part for part in collected if part)
            return value.strip("\"'")
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check SKILL.md frontmatter description lengths."
    )
    parser.add_argument("roots", nargs="+", help="Skill roots or SKILL.md files to scan.")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    args = parser.parse_args()

    failures = []
    checked = 0
    for root in args.roots:
        path = Path(root).expanduser()
        skill_files = [path] if path.name == "SKILL.md" else sorted(path.glob("*/SKILL.md"))
        for skill_file in skill_files:
            block = frontmatter(skill_file.read_text(encoding="utf-8"))
            if block is None:
                continue
            description = description_from_frontmatter(block)
            checked += 1
            length = len(description)
            print(f"{length:4d}  {skill_file}")
            if length > args.limit:
                failures.append((length, skill_file))

    if failures:
        print(f"\nDescriptions over {args.limit} characters:")
        for length, skill_file in failures:
            print(f"{length:4d}  {skill_file}")
        return 1

    print(f"\nOK: {checked} skill description(s) at or below {args.limit} characters.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
