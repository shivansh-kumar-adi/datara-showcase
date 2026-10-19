from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_PARTS = {".git", "node_modules", ".venv", "__pycache__", ".next", ".next-build"}
SECRET_PATTERNS = {
    "Clerk secret": re.compile(r"sk_(?:test|live)_[A-Za-z0-9]+"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC )?PRIVATE KEY-----"),
    "database password URL": re.compile(r"postgres(?:ql)?[^\s]*://[^\s:@]+:[^\s@]+@", re.I),
}


def main() -> int:
    errors: list[str] = []
    files = [path for path in ROOT.rglob("*") if path.is_file()]
    for path in files:
        relative = path.relative_to(ROOT)
        if FORBIDDEN_PARTS.intersection(relative.parts):
            errors.append(f"forbidden path: {relative}")
        if path.name in {".env", ".env.local"}:
            errors.append(f"environment file: {relative}")
        if path.suffix.lower() in {".md", ".py", ".yaml", ".yml", ".svg", ".cff"}:
            text = path.read_text(encoding="utf-8")
            for label, pattern in SECRET_PATTERNS.items():
                if pattern.search(text):
                    errors.append(f"possible {label}: {relative}")
    required = [
        "README.md", "BUILD_REPORT.md", "docs/04-system-architecture.md",
        "docs/architecture/system-context.mmd", "assets/brand/datara-logo.svg",
    ]
    for item in required:
        if not (ROOT / item).exists():
            errors.append(f"missing required file: {item}")
    if errors:
        print("FAIL")
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(files)} files checked; no forbidden paths or obvious credentials found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

