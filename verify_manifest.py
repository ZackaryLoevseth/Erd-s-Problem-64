#!/usr/bin/env python3
"""Verify the SHA-256 integrity manifest for the public release packet."""

from __future__ import annotations

import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "SHA256SUMS"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    checked = 0
    for raw_line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue

        expected, rel = line.split(maxsplit=1)
        rel = rel.strip()
        if rel.startswith("./"):
            rel = rel[2:]

        path = ROOT / rel
        if not path.is_file():
            raise SystemExit(f"MISSING: {rel}")

        actual = sha256(path)
        if actual != expected:
            raise SystemExit(
                f"HASH MISMATCH: {rel}\nexpected {expected}\nactual   {actual}"
            )
        checked += 1

    print(f"VERIFIED SHA256SUMS: {checked} files")


if __name__ == "__main__":
    main()
