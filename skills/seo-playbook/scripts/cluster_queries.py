#!/usr/bin/env python3
"""Group queries from a CSV by simple intent modifiers (Indonesian and English).

Usage:
    python scripts/cluster_queries.py queries.csv --column query --lang both

--lang: id, en, or both (default both).
Output: intent, query count, query list (CSV to stdout).
The result is a starting point. Check the SERP manually before merging or splitting pages.
"""
import argparse
import csv
import re
import sys
from collections import defaultdict

MODIFIERS = {
    "id": {
        "transaksional": ["jasa", "harga", "biaya", "beli", "pesan", "sewa", "murah", "terdekat", "dekat saya", "order"],
        "komersial": ["terbaik", "vs", "review", "alternatif", "rekomendasi", "perbandingan", "bandingkan"],
        "informasional": ["cara", "apa itu", "pengertian", "tutorial", "panduan", "tips", "contoh", "kenapa", "mengapa", "adalah"],
    },
    "en": {
        "transaksional": ["hire", "price", "cost", "buy", "order", "near me", "cheap", "service"],
        "komersial": ["best", "vs", "review", "alternative", "comparison", "compare"],
        "informasional": ["how to", "what is", "guide", "tutorial", "tips", "example", "why"],
    },
}
ORDER = ["transaksional", "komersial", "informasional"]


def build_patterns(lang: str):
    langs = ["id", "en"] if lang == "both" else [lang]
    patterns = {}
    for intent in ORDER:
        words = [w for l in langs for w in MODIFIERS[l][intent]]
        patterns[intent] = re.compile(r"(?<!\w)(?:" + "|".join(re.escape(w) for w in words) + ")", re.I)
    return patterns


def classify(query: str, patterns) -> str:
    for intent in ORDER:
        if patterns[intent].search(query):
            return intent
    return "tidak-terklasifikasi"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv_file")
    ap.add_argument("--column", default="query")
    ap.add_argument("--lang", choices=["id", "en", "both"], default="both")
    args = ap.parse_args()
    patterns = build_patterns(args.lang)

    groups = defaultdict(list)
    with open(args.csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if args.column not in (reader.fieldnames or []):
            print(f"Column '{args.column}' not found. Available: {reader.fieldnames}", file=sys.stderr)
            return 1
        for row in reader:
            q = (row.get(args.column) or "").strip()
            if q:
                groups[classify(q, patterns)].append(q)

    out = csv.writer(sys.stdout)
    out.writerow(["intent", "query_count", "queries"])
    for intent, qs in sorted(groups.items()):
        out.writerow([intent, len(qs), " | ".join(sorted(set(qs)))])
    return 0


if __name__ == "__main__":
    sys.exit(main())
