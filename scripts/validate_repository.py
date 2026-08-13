#!/usr/bin/env python3
"""Validate the public skills repository without third-party packages."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


DESCRIPTION_LIMIT = 1024
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
README_SKILL_PATTERN = re.compile(r"^\| \[`([^`]+)`\]\(([^)]+)\) \|$", re.MULTILINE)
REQUIRED_INTERFACE_FIELDS = {
    "display_name",
    "short_description",
    "icon_small",
    "icon_large",
    "default_prompt",
}


def read_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening frontmatter delimiter")

    try:
        end = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing frontmatter delimiter") from exc

    block = lines[1:end]
    values: dict[str, str] = {}
    index = 0
    while index < len(block):
        line = block[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, raw_value = line.split(":", 1)
        key = key.strip()
        raw_value = raw_value.strip()
        if key in values:
            raise ValueError(f"duplicate frontmatter field: {key}")
        if raw_value in {">-", ">", "|-", "|"}:
            parts: list[str] = []
            index += 1
            while index < len(block) and (block[index].startswith((" ", "\t")) or not block[index].strip()):
                if block[index].strip():
                    parts.append(block[index].strip())
                index += 1
            values[key] = " ".join(parts)
            continue
        values[key] = raw_value.strip("\"'")
        index += 1

    if set(values) != {"name", "description"}:
        raise ValueError("frontmatter must contain only name and description")
    return values


def read_interface(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "interface:":
        raise ValueError("the first line must be 'interface:'")

    values: dict[str, str] = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        match = re.fullmatch(r"  ([a-z_]+):\s*(.+)", line)
        if not match:
            raise ValueError(f"invalid interface line: {line!r}")
        key, raw_value = match.groups()
        if key in values:
            raise ValueError(f"duplicate interface field: {key}")
        if raw_value.startswith(('"', "'")) and raw_value[-1:] == raw_value[0]:
            try:
                values[key] = json.loads(raw_value) if raw_value[0] == '"' else raw_value[1:-1]
            except json.JSONDecodeError as exc:
                raise ValueError(f"invalid quoted value for {key}") from exc
        else:
            values[key] = raw_value
    return values


def validate_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
        target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        local_path = unquote(target.split("#", 1)[0])
        if local_path and not (path.parent / local_path).exists():
            errors.append(f"{path}: local link does not exist: {target}")


def validate_eval(path: Path, skill_name: str, errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return

    if not isinstance(data, dict) or data.get("skill") != skill_name:
        errors.append(f"{path}: 'skill' must equal {skill_name!r}")
    evals = data.get("evals") if isinstance(data, dict) else None
    if not isinstance(evals, list) or not evals:
        errors.append(f"{path}: 'evals' must be a non-empty list")
        return

    names: set[str] = set()
    for index, case in enumerate(evals, start=1):
        location = f"{path}: eval {index}"
        if not isinstance(case, dict):
            errors.append(f"{location} must be an object")
            continue
        name = case.get("name")
        prompt = case.get("prompt")
        expect = case.get("expect")
        if not isinstance(name, str) or not name:
            errors.append(f"{location} needs a non-empty name")
        elif name in names:
            errors.append(f"{location} has a duplicate name: {name}")
        else:
            names.add(name)
        if not isinstance(prompt, str) or not prompt:
            errors.append(f"{location} needs a non-empty prompt")
        if not isinstance(expect, list) or not expect or not all(isinstance(item, str) and item for item in expect):
            errors.append(f"{location} needs a non-empty list of expected behaviors")


def main() -> int:
    repository = Path(__file__).resolve().parent.parent
    skills_root = repository / "skills"
    errors: list[str] = []

    if not skills_root.is_dir():
        errors.append(f"{skills_root}: skill root does not exist")
        skill_directories: list[Path] = []
    else:
        skill_directories = sorted(path for path in skills_root.iterdir() if path.is_dir())
    if not skill_directories:
        errors.append(f"{skills_root}: no skill directories found")

    skill_names: set[str] = set()
    for skill_directory in skill_directories:
        skill_name = skill_directory.name
        skill_names.add(skill_name)
        skill_file = skill_directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_file}: required file does not exist")
            continue

        try:
            metadata = read_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_file}: {exc}")
            metadata = {}

        if not NAME_PATTERN.fullmatch(skill_name):
            errors.append(f"{skill_directory}: directory name is invalid")
        if metadata.get("name") != skill_name:
            errors.append(f"{skill_file}: name must equal the directory name {skill_name!r}")
        description = metadata.get("description", "")
        if not description:
            errors.append(f"{skill_file}: description must not be empty")
        elif len(description) > DESCRIPTION_LIMIT:
            errors.append(f"{skill_file}: description has {len(description)} characters; limit is {DESCRIPTION_LIMIT}")

        license_file = skill_directory / "LICENSE.txt"
        if not license_file.is_file():
            errors.append(f"{license_file}: required file does not exist")

        interface_file = skill_directory / "agents" / "openai.yaml"
        if not interface_file.is_file():
            errors.append(f"{interface_file}: required file does not exist")
        else:
            try:
                interface = read_interface(interface_file)
            except ValueError as exc:
                errors.append(f"{interface_file}: {exc}")
                interface = {}
            missing = REQUIRED_INTERFACE_FIELDS - interface.keys()
            if missing:
                errors.append(f"{interface_file}: missing fields: {', '.join(sorted(missing))}")
            for field in ("icon_small", "icon_large"):
                value = interface.get(field)
                if value:
                    icon_path = skill_directory / value.removeprefix("./")
                    if not icon_path.is_file():
                        errors.append(f"{interface_file}: {field} does not exist: {value}")

        eval_file = skill_directory / "evals" / "evals.json"
        if eval_file.exists():
            validate_eval(eval_file, skill_name, errors)

        for markdown_file in skill_directory.rglob("*.md"):
            validate_markdown_links(markdown_file, errors)

    readme = repository / "README.md"
    if not readme.is_file():
        errors.append(f"{readme}: required file does not exist")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        catalog_entries = README_SKILL_PATTERN.findall(readme_text)
        catalog = dict(catalog_entries)
        catalog_names = set(catalog)
        if len(catalog_entries) != len(catalog):
            errors.append(f"{readme}: catalog contains a duplicate skill")
        if catalog_names != skill_names:
            missing = sorted(skill_names - catalog_names)
            extra = sorted(catalog_names - skill_names)
            if missing:
                errors.append(f"{readme}: catalog is missing: {', '.join(missing)}")
            if extra:
                errors.append(f"{readme}: catalog has unknown skills: {', '.join(extra)}")
        for name, target in catalog.items():
            expected = f"skills/{name}/SKILL.md"
            if target != expected:
                errors.append(f"{readme}: catalog link for {name} must be {expected}")
        validate_markdown_links(readme, errors)

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"OK: validated {len(skill_directories)} skills and the repository catalog.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
