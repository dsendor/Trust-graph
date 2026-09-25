# Extraction prompt: bets from a prioritization report

Give this prompt, unchanged, to each model. Same text, same source file, no other
context. The variables are `{REPORT}`, `{SOURCE_FILE}`, and the report's section under
"Report-specific values" below.

**v2, 2026-09-25.** v1 left agency, driver, scenario, and size as free text, so the two
models disagreed mostly on wording and the comparison measured formatting, not accuracy.
v1 output is kept in `research-log/extractions/p5-2014/v1/`.

---

You are extracting the ranked bets from `{REPORT}`. The full text is in `{SOURCE_FILE}`.
Read all of it before writing anything.

A **bet** is a specific, named project, facility, or experiment the report recommends
building, funding, or continuing, or considered and declined. Programs, portfolios, and
R&D lines are not bets. Mentions too early for any recommendation either way are not bets.

Output a JSON array. One object per bet, with exactly these keys:

```
project, agency, size_class, rank_or_scenario, science_driver, promise_quote,
science_question, cost_at_ranking, cost_basis, target_date, source_locator,
confidence, rationale
```

Rules:

1. **Named values only** for `agency`, `size_class`, `rank_or_scenario`,
   `science_driver`, and `cost_basis`. Use exactly the values listed for this report
   below. Nothing else, no added notes; put notes in `rationale`.
2. `project` is the report's own short name for it, e.g. `Mu2e`, not `Mu2e experiment`.
3. `promise_quote` is verbatim from the report. If you cannot quote it, the row is a `guess`.
4. `cost_at_ranking` is a number in millions of dollars, or `null`. `target_date` is a
   year or `YYYY-YYYY`, or `null`. Both come only from the report. Do not use what you
   know happened later.
5. `science_question` is the specific question in one sentence, e.g. "Measure the dark
   energy equation of state w(z) to percent precision," not "study dark energy."
6. `source_locator` is the report's printed page number and a table or recommendation
   number, e.g. `p. 17, Table 1; Recommendation 16`.
7. `confidence` is `confident` or `guess`. A run with no guesses is not a confident run.
8. Output the JSON array only. No commentary.

## Report-specific values

### P5 2014

- `agency`: `DOE`, `NSF`, `DOE+NSF`, or `not-stated`. The US funders only; partners go in `rationale`.
- `size_class`: `large`, `medium`, `small`, or `not-stated`. Use the Table 1 section the
  project sits under ("Additional Small Projects" is `small`). If it is not in Table 1,
  use a size the text states, else `not-stated`.
- `rank_or_scenario`: for Table 1 rows, `A:<cell>|B:<cell>|C:<cell>`, each cell as
  written in Table 1 (`Y`, `N`, `Y, reduced`, `R&D only`, ...). For projects not in
  Table 1: `not-in-table-1:recommended` or `not-in-table-1:not-recommended`.
- `science_driver`: one or more of `higgs`, `neutrino-mass`, `dark-matter`,
  `cosmic-acceleration`, `unknown`, joined with `;`, from the Table 1 driver columns
  where the project has a row, else from the text.
- `cost_basis`: `size-class-only` when the report gives only the Table 1 band, else
  `stated` when `cost_at_ranking` has a number.
