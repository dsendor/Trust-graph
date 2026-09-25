# Extraction prompt: bets from a prioritization report

Give this prompt, unchanged, to each model. Same text, same source file, no other
context. The only variable is `{REPORT}` and `{SOURCE_FILE}`.

---

You are extracting the ranked bets from `{REPORT}`. The full text is in `{SOURCE_FILE}`.
Read all of it before writing anything.

A **bet** is a specific project, facility, or experiment the report recommends building,
funding, or continuing, and places in its priority tables or numbered recommendations.
Programs (R&D lines, "support theory") are not bets. Projects the report considered and
declined to recommend are bets with `rank_or_scenario` set to `not-recommended`.

Output a JSON array. One object per bet, with exactly these keys:

```
project, agency, size_class, rank_or_scenario, science_driver, promise_quote,
science_question, cost_at_ranking, cost_basis, target_date, source_locator,
confidence, rationale
```

Rules:

1. `promise_quote` is verbatim from the report. If you cannot quote it, the row is a `guess`.
2. `cost_at_ranking` and `target_date` come only from the report. If it gives no figure,
   write `null`. Do not use what you know happened later.
3. `size_class` and `rank_or_scenario` use the report's own tiers and scenario labels.
4. `science_question` is the specific question in one sentence, e.g. "Measure the dark
   energy equation of state w(z) to percent precision," not "study dark energy."
5. `source_locator` is a page number, table number, or recommendation number.
6. `confidence` is `confident` or `guess`. A run with no guesses is not a confident run.
7. Output the JSON array only. No commentary.
