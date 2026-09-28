"""Merge an adjudicated comparison sheet into data/bets.csv.

    python3 scripts/build_bets.py <report> <adjudicated.csv> <a.json> <b.json> --map <map>.csv

For each bet: agreed cells take the shared value; disagreements take the adjudicator's
verdict (a, b, both -> a, neither -> correct_value). A bet only one model found is kept
if the adjudicator ruled for the model that found it; its fields then come from that
model alone, and the rationale says so. Rows for <report> already in data/bets.csv are
replaced; other reports' rows are kept.

Standard library only.
"""
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

COLUMNS = [
    "bet_id", "source_report", "source_locator", "project", "agency", "size_class",
    "rank_or_scenario", "science_driver", "promise_quote", "science_question",
    "cost_at_ranking", "cost_basis", "target_date", "field_arxiv", "confidence", "rationale",
]
OUT = Path(__file__).resolve().parent.parent / "data" / "bets.csv"


def main(report, sheet_path, a_path, b_path, map_path):
    name_map = {(r["model"], r["project"]): r["bet_id"] for r in csv.DictReader(open(map_path))}
    models = {}
    for path in (a_path, b_path):
        model = Path(path).stem
        models[model] = {name_map[(model, r["project"])]: r for r in json.loads(Path(path).read_text())}
    model_a, model_b = Path(a_path).stem, Path(b_path).stem

    cells = defaultdict(dict)
    for r in csv.DictReader(open(sheet_path)):
        cells[r["project"]][r["field"]] = r

    rows = []
    for bet_id, fields in sorted(cells.items()):
        if "_row" in fields:
            r = fields["_row"]
            v = r["verdict"].strip().lower()
            found_by = model_a if r["value_a"] == "present" else model_b
            if (v == "a" and found_by != model_a) or (v == "b" and found_by != model_b) or v not in ("a", "b", "both"):
                continue  # adjudicator ruled it is not a bet
            src = models[found_by][bet_id]
            row = {k: src.get(k) for k in COLUMNS if k in src}
            row["rationale"] = f"Found by {found_by} only; fields not cross-checked. {src.get('rationale') or ''}".strip()
        else:
            base = models[model_a][bet_id]
            row = {k: base.get(k) for k in COLUMNS if k in base}
            for field, r in fields.items():
                v = r["verdict"].strip().lower()
                if r["agree"] == "yes" and v != "neither":
                    continue
                if v in ("a", "both"):
                    row[field] = r["value_a"]
                elif v == "b":
                    row[field] = r["value_b"]
                elif v == "neither":
                    row[field] = r["correct_value"]
                else:
                    sys.exit(f"{bet_id}.{field} has no verdict; adjudicate before merging")
        row["bet_id"] = bet_id
        row["source_report"] = report
        rows.append({k: ("" if row.get(k) is None else row.get(k)) for k in COLUMNS})

    kept = [r for r in csv.DictReader(open(OUT)) if r["source_report"] != report] if OUT.exists() else []
    with open(OUT, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS)
        w.writeheader()
        w.writerows(kept + rows)
    print(f"{len(rows)} {report} bets -> {OUT} ({len(kept)} rows from other reports kept)")


if __name__ == "__main__":
    args = sys.argv[1:]
    main(*args[:4], map_path=args[args.index("--map") + 1])
