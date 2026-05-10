from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def _text_files() -> list[Path]:
    suffixes = {".md", ".py", ".yaml", ".yml", ".json", ".html", ".css", ".ps1", ".txt"}
    ignored_parts = {".git", ".pytest_cache", "__pycache__"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in suffixes:
            continue
        if ignored_parts.intersection(path.parts):
            continue
        files.append(path)
    return files


def test_public_demo_runs() -> None:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "public_smoke_test.py"), "--rounds", "1", "--seed", "42"],
        text=True,
        capture_output=True,
        check=True,
    )
    payload = json.loads(result.stdout)
    assert payload["ok"] is True
    assert payload["summary"]["agents"] == 6
    assert payload["summary"]["properties"] == 4


def test_license_and_package_metadata_are_noncommercial() -> None:
    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    package_json = json.loads((ROOT / "package.json").read_text(encoding="utf-8"))
    package_lock = json.loads((ROOT / "package-lock.json").read_text(encoding="utf-8"))

    assert "PolyForm Noncommercial License 1.0.0" in license_text
    assert package_json["name"] == "atlas-market-engine-public"
    assert package_json["license"] == "SEE LICENSE IN LICENSE"
    assert package_lock["packages"][""]["license"] == "SEE LICENSE IN LICENSE"


def test_public_tree_excludes_private_material() -> None:
    forbidden_paths = [
        ROOT / ("pro" + "mpts"),
        ROOT / "services",
        ROOT / "utils",
        ROOT / "docs" / "发布素材包_20260501",
        ROOT / "SNAPSHOT_MANIFEST.json",
    ]
    assert [str(path.relative_to(ROOT)) for path in forbidden_paths if path.exists()] == []


def test_markdown_links_resolve() -> None:
    broken: list[str] = []
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            resolved = (path.parent / target.split("#", 1)[0]).resolve()
            if not resolved.exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")
    assert sorted(broken) == []


def test_no_credential_like_or_reserved_terms() -> None:
    credential_pattern = re.compile(
        "|".join(
            [
                "s" + "k-[A-Za-z0-9_-]{10,}",
                "g" + "hp_[A-Za-z0-9_]{10,}",
                "github" + "_pat_",
                "AK" + "IA[0-9A-Z]{16}",
                "xo" + "x[baprs]-",
                "h" + "f_[A-Za-z0-9]{10,}",
                "Bear" + r"er\s+[A-Za-z0-9._-]{10,}",
            ]
        ),
        re.IGNORECASE,
    )
    forbidden_terms = [
        "S" + "606",
        "S" + "707",
        "S" + "808",
        "night" + "_run",
        "night" + "-run",
        "formal" + " matrix",
        "完整" + " pro" + "mpt",
        "commercial" + " pro" + "mpt",
        "软" + "著",
        "签" + "章",
        "登记" + "材料",
        "results" + "/runs",
        "reports" + "/phase",
        "D:" + "\\GitProj",
        "C:" + "\\Users",
    ]
    hits: list[str] = []
    for path in _text_files():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if credential_pattern.search(text):
            hits.append(f"{path.relative_to(ROOT)}: credential-like pattern")
        for term in forbidden_terms:
            if term.lower() in text.lower():
                hits.append(f"{path.relative_to(ROOT)}: {term}")
    assert hits == []
