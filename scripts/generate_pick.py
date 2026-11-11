#!/usr/bin/env python3
"""Turn an "Adding a Pick" issue form submission into a Hugo data file under data/picks/.

Reads ISSUE_BODY and ISSUE_NUMBER from the environment. The body is untrusted user input,
so it must only ever reach this script through env vars, never be interpolated into a shell command.
"""
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml

SHOWS = {
    "LINUX Unplugged": "linux-unplugged",
    "This Week in Bitcoin": "this-week-in-bitcoin",
    "The Launch": "the-launch",
    "Jupiter Extras": "jupiter-extras",
    "Coder Radio": "coder-radio",
    "Linux Action News": "linux-action-news",
    "Office Hours": "office-hours",
    "Self-Hosted": "self-hosted",
}

# GitHub renders optional fields left empty as this literal
NO_RESPONSE = "_No response_"


def parse_form(body: str) -> dict:
    parts = re.split(r"^### (.+?)\s*$", body.replace("\r\n", "\n"), flags=re.M)
    fields = {}
    for label, value in zip(parts[1::2], parts[2::2]):
        value = value.strip()
        fields[label.strip()] = "" if value == NO_RESPONSE else value
    return fields


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9.]+", "-", title.lower())
    # the slug is also used in a git branch name, which can't contain ".." or end in ".lock"
    slug = re.sub(r"\.{2,}", ".", slug)
    slug = re.sub(r"\.lock$", "", slug).strip("-.")
    if not slug:
        raise ValueError(f"Pick name {title!r} has no usable characters for a file name")
    return slug


def build_pick(fields: dict) -> dict:
    title = " ".join(fields.get("Name", "").split())
    if not title:
        raise ValueError("Name is required")

    url = fields.get("Pick URL", "").strip()
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https") or not parsed.netloc or any(c.isspace() for c in url):
        raise ValueError(f"Pick URL must be a single http(s) link, got {url!r}")

    description = " ".join(fields.get("Description", "").split())
    if not description:
        raise ValueError("Description is required")

    episode = fields.get("Episode Number", "").strip()
    if not re.fullmatch(r"\d+", episode) or int(episode) < 1:
        raise ValueError(f"Episode Number must be a positive whole number, got {episode!r}")

    names = [s.strip() for s in fields.get("Show", "").split(",") if s.strip()]
    if not names:
        raise ValueError("Show is required")
    unknown = [n for n in names if n not in SHOWS]
    if unknown:
        raise ValueError(f"Unknown show(s): {', '.join(unknown)}")

    return {
        "title": title,
        "url": url,
        "description": description,
        "license": " ".join(fields.get("License", "").split()) or None,
        "shows": [{"episode": int(episode), "show": n, "slug": SHOWS[n]} for n in names],
    }


def write_pick(pick: dict, picks_dir: Path) -> Path:
    path = picks_dir / f"{slugify(pick['title'])}.yaml"
    if path.exists():
        # same pick featured on another episode: keep the existing entry and add the new appearance
        existing = yaml.safe_load(path.read_text(encoding="utf-8"))
        seen = {(str(s["slug"]), str(s["episode"])) for s in existing["shows"]}
        for s in pick["shows"]:
            if (s["slug"], str(s["episode"])) not in seen:
                existing["shows"].append(s)
        pick = existing
    text = yaml.safe_dump(pick, sort_keys=True, allow_unicode=True)
    path.write_text("---\n" + text, encoding="utf-8")
    return path


def generate(body: str, issue_number: int, picks_dir: Path) -> dict:
    pick = build_pick(parse_form(body))
    path = write_pick(pick, picks_dir)
    return {"file": str(path), "title": pick["title"], "branch": f"{issue_number}-{path.stem}"}


def main() -> int:
    try:
        number = int(os.environ["ISSUE_NUMBER"])
        result = generate(os.environ["ISSUE_BODY"], number, Path(os.environ.get("PICKS_DIR", "data/picks")))
    except ValueError as e:
        print(f"::error::{e}")
        return 1
    with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as out:
        for key, value in result.items():
            out.write(f"{key}={value}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
