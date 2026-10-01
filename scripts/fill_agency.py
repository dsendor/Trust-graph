"""Fill `agency` in data/bets.csv from funding records where the report does not state it.

    python3 scripts/fill_agency.py <agency_records.csv>

The records file has columns bet_id, agency_record, source_url, confidence, rationale.
A bet whose `agency` is `not-stated` takes the record's value, `agency_basis` becomes
`record`, and `agency_source_url` gets the record's source. Where the report states an
agency it stays, with `agency_basis` = `report`; a record that disagrees is printed, not
applied. Run it after scripts/build_bets.py, which rewrites data/bets.csv.
"""
import csv
import sys
from pathlib import Path

BETS = Path(__file__).resolve().parent.parent / "data" / "bets.csv"
EXTRA = ["agency_basis", "agency_source_url"]


def main(records_path):
    records = {r["bet_id"]: r for r in csv.DictReader(open(records_path))}
    rows = list(csv.DictReader(open(BETS)))
    cols = list(rows[0].keys())
    for c in EXTRA:
        if c not in cols:
            cols.insert(cols.index("agency") + 1 + EXTRA.index(c), c)
    filled = 0
    for r in rows:
        rec = records.get(r["bet_id"])
        if r["agency"] and r["agency"] != "not-stated":
            r["agency_basis"] = "report"
            r.setdefault("agency_source_url", "")
            if rec and rec["agency_record"] not in (r["agency"], "not-found"):
                print(f"{r['bet_id']}: report says {r['agency']}, record says {rec['agency_record']} (kept report)")
        elif rec and rec["agency_record"] != "not-found":
            r["agency"], r["agency_basis"], r["agency_source_url"] = rec["agency_record"], "record", rec["source_url"]
            filled += 1
        else:
            r.setdefault("agency_basis", "")
            r.setdefault("agency_source_url", "")
    with open(BETS, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows({c: r.get(c, "") for c in cols} for r in rows)
    print(f"{filled} agencies filled from records -> {BETS}")


if __name__ == "__main__":
    main(sys.argv[1])
