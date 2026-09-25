# Hand check: P5 2014

`p5-2014.csv` lines up Claude Sonnet (`value_a`) and Claude Haiku (`value_b`) field by
field, one row per bet and field, with the source text for that bet in `source_excerpt`.
Rows are grouped by field, so you read down one column of Table 1 (report p. 17) at a time.

## What to fill

For every row where `agree` is `no` or `check`, set `verdict`:

| `verdict` | Meaning |
|---|---|
| `a` | Sonnet is right |
| `b` | Haiku is right |
| `both` | Both acceptable (e.g. same meaning, different words) |
| `neither` | Both wrong; put the right value in `correct_value` |

For `_row` rows (a bet only one model found): `a` or `b` is the model that was right to
include or leave it out.

Rows where `agree` is `yes` count as right for both unless you mark them `neither`.

## Order

1. **Weekend 1 fields, 34 cells:** `_row` (7), `size_class` (4), `rank_or_scenario` (4),
   `agency` (7), `science_driver` (5), `target_date` (7). Table 1 answers most of them.
2. **Weekend 3 fields, 50 cells:** `promise_quote`, `science_question`, `source_locator`.
   Leave for later. Quotes are already checked mechanically, below.

Then: `python3 scripts/compare_extractions.py --score research-log/hand-check/p5-2014.csv`

## Already checked mechanically

`research-log/extractions/p5-2014/quote-check.csv`: is each "verbatim" quote in the report?
41 of 43 yes. Both misses are Haiku:

- **LSST:** silently corrected the report's typo "stucture" to "structure."
- **RADAR:** stitched two different passages (p. 13 and a later section) into one quote.

## Known ambiguity in the source

The PDF text loses Table 1's cell layout. Four notes ("LBNF components delayed relative
to Scenario B," "possibly small hardware contributions," "some reductions with redirection
to PIP-II development," "Mu2e small reprofile needed") float free of their cells. That is
why LBNF, PIP-II, and ILC scenario cells disagree. Check them against the PDF (link in `sources/README.md`), not the text.
