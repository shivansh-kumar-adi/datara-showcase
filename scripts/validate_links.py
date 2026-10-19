from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def main() -> int:
    missing: list[str] = []
    for document in ROOT.rglob("*.md"):
        text = document.read_text(encoding="utf-8")
        for target in LINK.findall(text):
            clean = target.strip().split("#", 1)[0]
            if not clean or clean.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (document.parent / clean).resolve()
            if not resolved.exists():
                missing.append(f"{document.relative_to(ROOT)} -> {target}")
    if missing:
        print("Broken relative links:")
        print("\n".join(missing))
        return 1
    print("PASS: all Markdown relative links resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

