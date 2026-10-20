"""Search visual-support catalog entries using Python 3."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--age", type=int)
parser.add_argument("--category")
parser.add_argument("--query", default="")
parser.add_argument("--status", choices=["planned", "ready"])
args = parser.parse_args()
if args.age is not None and not 0 <= args.age <= 18:
    parser.error("age must be between 0 and 18")
root = Path(__file__).resolve().parent
categories = json.loads((root / "catalog/categories.json").read_text())
if args.category and args.category not in {c["id"] for c in categories}:
    parser.error("unknown category; see catalog/categories.json")
entries = json.loads((root / "catalog/visuals.json").read_text())
results = [v for v in entries
           if (args.age is None or v["min_age"] <= args.age <= v["max_age"])
           and (not args.category or v["category"] == args.category)
           and (not args.status or v["status"] == args.status)
           and all(word in " ".join([v["title"], v["category"], *v["keywords"]]).casefold()
                   for word in args.query.casefold().split())]
for v in results:
    print(f'{v["title"]} | ages {v["age_strand"]} | {v["category"]} | {v["status"]}')
    for asset in v["assets"]:
        print(f'  {asset}')
if not results:
    print("No matching visuals.")
