#!/usr/bin/env python3
"""Kelompokkan query dari CSV berdasarkan modifier intent sederhana.

Pemakaian:
    python scripts/cluster_queries.py queries.csv --column query

Output: cluster, jumlah query, daftar query (CSV ke stdout).
Hasil adalah titik awal. Cek SERP manual sebelum memutuskan gabung atau pisah.
"""
import argparse
import csv
import sys
from collections import defaultdict

INTENT_MODIFIERS = {
    "transaksional": ["jasa", "harga", "biaya", "beli", "pesan", "sewa", "murah", "terdekat", "dekat saya", "order"],
    "komersial": ["terbaik", "vs", "review", "alternatif", "rekomendasi", "perbandingan", "bandingkan"],
    "informasional": ["cara", "apa itu", "pengertian", "tutorial", "panduan", "tips", "contoh", "kenapa", "mengapa", "adalah"],
}


def classify(query: str) -> str:
    q = query.lower()
    for intent, words in INTENT_MODIFIERS.items():
        for w in words:
            if w in q:
                return intent
    return "tidak-terklasifikasi"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_file")
    ap.add_argument("--column", default="query")
    args = ap.parse_args()

    groups = defaultdict(list)
    with open(args.csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if args.column not in (reader.fieldnames or []):
            print(f"Kolom '{args.column}' tidak ada. Kolom tersedia: {reader.fieldnames}", file=sys.stderr)
            return 1
        for row in reader:
            q = (row.get(args.column) or "").strip()
            if q:
                groups[classify(q)].append(q)

    out = csv.writer(sys.stdout)
    out.writerow(["intent", "jumlah_query", "query"])
    for intent, qs in sorted(groups.items()):
        out.writerow([intent, len(qs), " | ".join(sorted(set(qs)))])
    return 0


if __name__ == "__main__":
    sys.exit(main())
