#!/usr/bin/env python3
"""Regenerasi summary/INDEX.md dari seluruh digest mingguan yang tersimpan.

Pakai:
    python3 scripts/build_index.py
"""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUMMARY = ROOT / "summary"
INDEX = SUMMARY / "INDEX.md"
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
BULAN = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember",
]


def extract(path: Path) -> tuple[str, str]:
    """Kembalikan (periode, ringkasan singkat) dari sebuah digest."""
    lines = path.read_text(encoding="utf-8").splitlines()
    periode, ringkas = "—", ""
    for i, line in enumerate(lines):
        low = line.strip().lower()
        if low.startswith("**periode liputan:**") and periode == "—":
            match = re.search(r"\*\*Periode liputan:\*\*\s*(.+?)(?:\s*·|$)", line)
            if match:
                periode = match.group(1).strip()
        elif low.startswith("## ") and "ringkasan eksekutif" in low and not ringkas:
            body = [
                l.strip().lstrip("-").strip()
                for l in lines[i + 1 : i + 8]
                if l.strip() and not l.startswith("#")
            ]
            ringkas = " ".join(body)
            ringkas = re.sub(r"\[\d+\](\[\d+\])*", "", ringkas)
            ringkas = re.sub(r"\s+", " ", ringkas).strip()[:200]
    return periode, ringkas


def main() -> int:
    digests = sorted(SUMMARY.rglob("*.md"), reverse=True)
    digests = [p for p in digests if DATE_RE.search(p.stem)]

    rows: dict[tuple[int, int], list[str]] = {}
    for path in digests:
        y, m, d = (int(x) for x in DATE_RE.search(path.stem).groups())
        periode, ringkas = extract(path)
        rel = path.relative_to(SUMMARY).as_posix()
        rows.setdefault((y, m), []).append(
            f"| [{y}-{m:02d}-{d:02d}]({rel}) | {periode} | {ringkas or '—'} |"
        )

    out = [
        "# 📚 Arsip Weekly News Digest — Tim Audit",
        "",
        f"Total **{len(digests)}** digest · diperbarui {date.today().isoformat()}",
        "",
    ]
    if not digests:
        out += ["_Belum ada digest tersimpan._", ""]
    for (y, m), lines in sorted(rows.items(), reverse=True):
        out += [
            f"## {BULAN[m - 1]} {y}",
            "",
            "| Tanggal | Periode liputan | Ringkasan |",
            "|---|---|---|",
            *lines,
            "",
        ]

    SUMMARY.mkdir(parents=True, exist_ok=True)
    INDEX.write_text("\n".join(out), encoding="utf-8")
    print(f"INDEX.md diperbarui: {len(digests)} digest")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
