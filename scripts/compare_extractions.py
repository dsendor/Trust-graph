"""Line up two model extractions field by field into a hand-check sheet.

    python3 scripts/compare_extractions.py <a.json> <b.json> <out.csv>
        Writes one row per (bet, field) with both values and whether they agree.
        David fills `verdict` (a, b, both, neither) and `correct_value` if neither.

    python3 scripts/compare_extractions.py --score <out.csv>
        After hand check: accuracy per model per field. The jagged profile.

Standard library only.
"""
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

FIELDS = [
    "agency", "size_class", "rank_or_scenario", "science_driver", "promise_quote",
    "science_question", "cost_at_ranking", "cost_basis", "target_date", "source_locator",
]
# Free-text fields: disagreement is expected, so the check is "does each say the same thing".
FUZZY = {"promise_quote", "science_question"}


def norm(v):
    if v is None:
        return ""
    return re.sub(r"[^a-z0-9$.,]+", " ", str(v).lower()).strip()


def key(project):
    return re.sub(r"[^a-z0-9]+", "", project.lower())


def load(path):
    rows = json.loads(Path(path).read_text())
    return {key(r["project"]): r for r in rows}


def compare(a_path, b_path, out_path):
    a, b = load(a_path), load(b_path)
    model_a, model_b = Path(a_path).stem, Path(b_path).stem
    out = []
    for k in sorted(set(a) | set(b)):
        ra, rb = a.get(k), b.get(k)
        project = (ra or rb)["project"]
        if ra is None or rb is None:
            out.append({"project": project, "field": "_row", "model_a": model_a, "model_b": model_b,
                        "value_a": "present" if ra else "MISSING", "value_b": "present" if rb else "MISSING",
                        "agree": "no", "verdict": "", "correct_value": ""})
            continue
        for f in FIELDS:
            va, vb = ra.get(f), rb.get(f)
            agree = norm(va) == norm(vb)
            out.append({"project": project, "field": f, "model_a": model_a, "model_b": model_b,
                        "value_a": va if va is not None else "", "value_b": vb if vb is not None else "",
                        "agree": "yes" if agree else ("check" if f in FUZZY else "no"),
                        "verdict": "", "correct_value": ""})
    with open(out_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(out[0]))
        w.writeheader()
        w.writerows(out)
    n = len(out)
    agreed = sum(r["agree"] == "yes" for r in out)
    print(f"{len(set(a) | set(b))} bets, {n} cells, {agreed} agree, {n - agreed} to hand check -> {out_path}")


def score(sheet):
    """Agreed cells count as right for both unless a verdict says otherwise."""
    right = defaultdict(lambda: [0, 0])  # (model, field) -> [right, total]
    unchecked = 0
    for r in csv.DictReader(open(sheet)):
        v = r["verdict"].strip().lower()
        if r["agree"] != "yes" and not v:
            unchecked += 1
            continue
        for side, model in (("a", r["model_a"]), ("b", r["model_b"])):
            ok = v in (side, "both") or (r["agree"] == "yes" and v in ("", "both"))
            cell = right[(model, r["field"])]
            cell[0] += ok
            cell[1] += 1
    print("model,field,right,total,accuracy")
    for (model, field), (ok, total) in sorted(right.items()):
        print(f"{model},{field},{ok},{total},{ok / total:.2f}")
    if unchecked:
        print(f"# {unchecked} disagreements not yet hand checked", file=sys.stderr)


if __name__ == "__main__":
    if sys.argv[1] == "--score":
        score(sys.argv[2])
    else:
        compare(*sys.argv[1:4])
