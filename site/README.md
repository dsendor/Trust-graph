# Website

A single static page that reads the ledger and explains it to someone new to physics.

```bash
python3 scripts/build_site.py                 # writes site/index.html from data/*.csv
python3 scripts/build_site.py --fragment x.html   # also writes the page without the document wrapper
```

| File | What it is |
|---|---|
| `template.html` | The page: styles, layout, and the script that draws the charts from the data |
| `copy.json` | Plain-English name, one-line description, and the science question in lay terms, per bet |
| `findings.json` | The narrative: lede, primer cards, the text under each of the four questions, the five case stories, method, glossary |
| `index.html` | Built output. Regenerate after any change to the CSVs or the files above; do not edit by hand |

Rules the build enforces: every bet needs copy; only `committee` and `agency` rows from
`data/actors.csv` reach the page (CLAUDE.md rule 7). The charts parse the `value` string
of each `cost-schedule` outcome (`ratio=`, `first_data=`, `target=`), so keep those keys.
Program lines (rows with `delivered=` or `recommended=`) are left out of the cost and
timeline charts. Open `index.html` in a browser; it needs no server.
