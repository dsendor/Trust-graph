"""Line up two model extractions field by field into a hand-check sheet.

    python3 scripts/compare_extractions.py <a.json> <b.json> <out.csv> [--map name-map.csv] [--evidence rows.csv]
        Writes one row per (bet, field) with both values and whether they agree.
        --map joins rows the models named differently (columns model, project, bet_id).
        --evidence adds the source text for each bet (columns bet_id, source_excerpt).
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

# Weekend 1 fields first; the free-text fields matter from Weekend 3.
FIELDS = [
    "size_class", "rank_or_scenario", "agency", "science_driver", "target_date",
    "cost_at_ranking", "cost_basis", "promise_quote", "science_question", "source_locator",
]
# Free-text fields: disagreement in wording is expected, so the check is "do they say the same thing".
FUZZY = {"promise_quote", "science_question", "source_locator", "rationale"}


def norm(v, field=None):
    if v is None:
        return ""
    v = str(v).lower()
    if field == "size_class":  # "Large (>$200M) per Table 1" and "Large" are the same answer
        m = re.search(r"\b(large|medium|small)\b", v)
        return m.group(1) if m else v
    if field == "science_driver":  # a set: order does not matter
        return ";".join(sorted(t.strip() for t in v.split(";")))
    if field == "rank_or_scenario":
        return re.sub(r"\s+", "", v)
    return re.sub(r"[^a-z0-9$.,]+", " ", v).strip()


def key(project):
    return re.sub(r"[^a-z0-9]+", "", project.lower())


def load(path, name_map):
    model = Path(path).stem
    rows = json.loads(Path(path).read_text())
    return {name_map.get((model, r["project"]), key(r["project"])): r for r in rows}


def compare(a_path, b_path, out_path, map_path=None, evidence_path=None):
    name_map = {(r["model"], r["project"]): r["bet_id"] for r in csv.DictReader(open(map_path))} if map_path else {}
    evidence = {r["bet_id"]: r["source_excerpt"] for r in csv.DictReader(open(evidence_path))} if evidence_path else {}
    a, b = load(a_path, name_map), load(b_path, name_map)
    model_a, model_b = Path(a_path).stem, Path(b_path).stem
    out = []
    for k in sorted(set(a) | set(b)):
        ra, rb = a.get(k), b.get(k)
        project = k
        ev = evidence.get(k, "")
        if ra is None or rb is None:
            out.append({"project": project, "source_excerpt": ev, "field": "_row", "model_a": model_a, "model_b": model_b,
                        "value_a": "present" if ra else "MISSING", "value_b": "present" if rb else "MISSING",
                        "agree": "no", "verdict": "", "correct_value": ""})
            continue
        for f in FIELDS:
            va, vb = ra.get(f), rb.get(f)
            agree = norm(va, f) == norm(vb, f)
            out.append({"project": project, "source_excerpt": ev, "field": f, "model_a": model_a, "model_b": model_b,
                        "value_a": va if va is not None else "", "value_b": vb if vb is not None else "",
                        "agree": "yes" if agree else ("check" if f in FUZZY else "no"),
                        "verdict": "", "correct_value": ""})
    # Group by field, in FIELDS order, so a checker reads down one column of the source at a time.
    order = {f: i for i, f in enumerate(["_row"] + FIELDS)}
    out.sort(key=lambda r: (order[r["field"]], r["project"]))
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
    args = sys.argv[1:]
    if args[0] == "--score":
        score(args[1])
    else:
        opt = lambda name: args[args.index(name) + 1] if name in args else None
        compare(*args[:3], map_path=opt("--map"), evidence_path=opt("--evidence"))
