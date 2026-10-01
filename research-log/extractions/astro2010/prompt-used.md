You are extracting the ranked bets from the Astro2010 decadal survey, "New Worlds, New Horizons in Astronomy and Astrophysics" (National Research Council, 2010). The full text is in `/home/user/trust-graph/sources/astro2010.txt` (the Executive Summary and Chapter 7; `=== PAGE n ===` markers are the printed page numbers).
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

Report-specific values (Astro2010). Where these conflict with the general definition of a bet above, these win:

- Scope: every item in Tables ES.2 to ES.5 is a bet, programs included, because those
  tables are the ranked priorities. In Table ES.1 (small scale, unranked) only named
  facilities or missions are bets; augmentations and grant programs are not.
- `agency`: US funders only, joined with `+` in the order `DOE`, `NASA`, `NSF`
  (e.g. `DOE+NSF`), or `not-stated`.
- `size_class`: `large`, `medium`, or `small`, from the table's scale.
- `rank_or_scenario`: `<ground|space>-<large|medium>-<rank>` for Tables ES.2 to ES.5
  (e.g. `space-large-1`), or `small-unranked` for Table ES.1.
- `science_driver`: one or more of `cosmic-dawn` (first stars, galaxies, black holes),
  `new-worlds` (nearby habitable planets), `physics-of-the-universe` (fundamental physics),
  or `broad`, joined with `;`.
- `cost_at_ranking`: the survey's appraisal of total cost through construction in
  millions of FY2010 dollars, as a number or a `low-high` range (e.g. `1100-1400`). Put
  the US federal share in `rationale`. `cost_basis`: `appraisal-total-FY2010`, or
  `not-stated`.
- `target_date`: from the table's science or launch timing, as a year range: early =
  first four years of the decade, mid = middle four, late = last four (e.g. "late 2010s"
  -> `2016-2019`, "mid-2020s" -> `2023-2026`, "mid-to-late 2010s" -> `2013-2019`).
