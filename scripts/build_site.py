#!/usr/bin/env python3
"""Build site/index.html from the ledger CSVs.

    python3 scripts/build_site.py            # writes site/index.html

Reads data/bets.csv, data/outcomes.csv, data/actors.csv, site/copy.json and
site/template.html. Named people are stripped from actors (CLAUDE.md rule 7):
only committee and agency rows reach the page. The template holds the literal
token __LEDGER_JSON__ inside a <script> tag; it is replaced with the data.
"""
import csv
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = ROOT / "site"


def read(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main():
    bets = read(DATA / "bets.csv")
    outcomes = read(DATA / "outcomes.csv")
    actors = [a for a in read(DATA / "actors.csv") if a.get("type") in ("committee", "agency")]
    copy = json.loads((SITE / "copy.json").read_text(encoding="utf-8"))
    template = (SITE / "template.html").read_text(encoding="utf-8")

    missing = [b["bet_id"] for b in bets if b["bet_id"] not in copy["bets"]]
    if missing:
        sys.exit(f"copy.json lacks plain-English copy for: {missing}")

    findings = json.loads((SITE / "findings.json").read_text(encoding="utf-8"))
    payload = {
        "bets": bets,
        "outcomes": outcomes,
        "actors": actors,
        "copy": copy["bets"],
        "findings": findings,
    }
    # </script> inside a JSON string would end the tag early; escape the slash.
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    if "__LEDGER_JSON__" not in template:
        sys.exit("template.html lacks the __LEDGER_JSON__ token")
    body = template.replace("__LEDGER_JSON__", blob)
    # site/index.html is a complete document (for GitHub Pages or a local open).
    html = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            "<meta name=\"description\" content=\"33 ranked bets from Astro2010 and P5 2014, checked against what happened.\">\n"
            "</head>\n<body>\n" + body + "\n</body>\n</html>\n")
    (SITE / "index.html").write_text(html, encoding="utf-8")
    # --fragment <path>: the same page without the document wrapper, for hosts that add their own.
    if "--fragment" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1]).write_text(body, encoding="utf-8")
    print(f"site/index.html: {len(bets)} bets, {len(outcomes)} outcomes, "
          f"{len(actors)} committee/agency actors, {len(html)//1024} KB")


if __name__ == "__main__":
    main()
