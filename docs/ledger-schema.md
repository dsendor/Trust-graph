# Ledger schema

Three CSV files in `data/`, one row per bet, outcome, or actor. Plain CSV so it opens in
anything and loads into SQLite or Notion later without a decision today.

## `data/bets.csv`: the promise, as written at ranking

| Column | Meaning |
|---|---|
| `bet_id` | `<report>-<slug>`, e.g. `p5-2014-mu2e`. Stable, never reused |
| `source_report` | `astro2010`, `p5-2014` |
| `source_locator` | Page, section, or recommendation number in the report |
| `project` | Name as the report writes it |
| `agency` | US funders only: `DOE`, `NSF`, `NASA`, `DOE+NSF`, `not-stated`, ... |
| `size_class` | The report's own tier. P5 2014: `large` (>$200M), `medium` ($50M to $200M), `small` (<$50M) |
| `rank_or_scenario` | Astro2010: rank within its category. P5 2014: which of scenarios `A`, `B`, `C` include it, e.g. `A,B,C` or `B,C` |
| `science_driver` | P5 2014 names five: `higgs`, `neutrino-mass`, `dark-matter`, `cosmic-acceleration`, `unknown` |
| `promise_quote` | Verbatim sentence(s) from the report stating what the bet is for |
| `science_question` | The specific question it was sold on, in our words, traceable to `promise_quote` |
| `cost_at_ranking` | The report's figure, or blank if the report gives none. Never inferred |
| `cost_basis` | What the figure is: `size-class-only`, `TPC then-year $`, `US share`, ... |
| `target_date` | The report's stated date or window, or blank |
| `field_arxiv` | arXiv category the science question lives in, e.g. `hep-ex`, `astro-ph.CO` |
| `confidence` | `confident` or `guess` |
| `rationale` | Why this row reads the way it does, one line |

## `data/outcomes.csv`: what happened, one row per question answered

| Column | Meaning |
|---|---|
| `bet_id` | Joins to `bets.csv` |
| `question` | `built`, `cost-schedule`, `science`, `attribution` (the four ledger questions) |
| `result` | `yes`, `no`, `partial`, `surprise`, `building`, `cancelled` |
| `pt_category` | Pan and Trimble's five outcome categories (their Section 2.3), for comparability: `1` in operation within 15 years, mostly federal; `2` within 15 years, mostly other funding; `3` eventually built, mostly federal; `4` eventually built, mostly other funding; `5` never or very unlikely. Their "about a third each" groups 1, 2 to 4, and 5 |
| `as_of` | Date the result was true |
| `value` | The number or date, when there is one (final cost, first-data date) |
| `source_url` | Required. A search snippet is not a source |
| `confidence` | `confident` or `guess` |
| `rationale` | One line |

## `data/actors.csv`: whose call it was (Weekend 3)

`actor_id`, `name`, `type` (`person`, `committee`, `agency`), `bet_id`, `role_at_bet`,
`source_url`. Named people stay internal (CLAUDE.md rule 7).

## Model extractions

Each model's raw output lives in `research-log/extractions/<report>/<model>.json`, same
fields as `bets.csv`. `scripts/compare_extractions.py` lines two of them up field by
field into a hand-check sheet. David's verdict on each disagreement is the resolution
event for the model trust dataset.
