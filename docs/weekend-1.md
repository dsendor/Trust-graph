# Weekend 1: extend Pan and Trimble to P5 2014

**Goal.** Every P5 2014 bet in `data/bets.csv`, with whether it was built in
`data/outcomes.csv`, extracted by two models, conflicts settled by Opus. Astro2010 rows seeded from
Pan and Trimble alongside, so both reports sit in one table.

**Good enough.** All P5 2014 large and medium projects, promise side adjudicated, built
status sourced. Cost variance and schedule are Weekend 2.

## Status

**Done.** 33 bets in `data/bets.csv` (21 P5 2014, 12 Astro2010), each with a sourced
`built` outcome in `data/outcomes.csv`.

| Step | State |
|---|---|
| Sources | P5 2014 report, Pan and Trimble preprint, Astro2010 Executive Summary and Chapter 7 (`sources/README.md`) |
| Two-model extraction | Both reports, v2 prompt, Sonnet and Haiku |
| Adjudication | Opus: 93 P5 cells, 43 Astro2010 cells. One override by David: SBN included |
| Agency | P5 agencies the report does not name are filled from funding records (13 bets, `agency_basis` = `record`) |
| Built status | Opus, sourced, 33 bets. `research-log/outcomes/` |
| Model scores | `research-log/model-trust/`. Graded by Opus, not by a person |

## Findings

- **Astro2010 by Pan and Trimble's categories (our coding, 12 ranked items):** 5 in
  operation by 2025 with federal money (1), 1 built later (3, Roman), 5 built later or
  building with mostly other money (4), 1 never (5, SPICA). Their scorecard for the same
  report counts 23 items including unranked small ones: 10 / 1.5 / 4 / 3.5 / 4.
- **P5 2014 gives no project costs**, only size bands. Astro2010 gives appraised costs
  in FY2010 dollars. Cost variance is Weekend 2.
- **Extraction:** on P5 (messy table), Sonnet beat Haiku clearly; on Astro2010 (clean
  ranked tables), both were near perfect. Haiku never marks its own uncertainty.

## Search tooling

No Brave search this weekend. Weekend 1 reads two known documents, so there is nothing to
search, and both models getting the same saved text in `sources/` already gives the
"same evidence" property that Brave's cache gave the gap map project. Port
`engine/search.mjs` from science-gap-map-analysis at the start of Weekend 2, when cost and
schedule lookups across ~30 bets need logged searches and provable nulls. That needs
`BRAVE_API_KEY` in the environment's secrets and `api.search.brave.com` allowed.

## Steps

1. **Sources.** P5 2014 report PDF to text in `sources/p5-2014.txt`
   ([usparticlephysics.org](https://www.usparticlephysics.org/wp-content/uploads/2018/03/FINAL_P5_Report_053014.pdf),
   mirror at [OSTI](https://www.osti.gov/servlets/purl/1320608)). Pan and Trimble 2024
   Astro2010 table transcribed to `sources/pan-trimble-2024-astro2010.csv`, with citation.
2. **Seed Astro2010** from Pan and Trimble: `bets.csv` rows plus `built` outcomes with
   `pt_category`. They do not code Astro2010 rows, so this coding is ours; cite their status text.
3. **Extract P5 2014 twice.** Same prompt (`prompts/extract-bets.md`), same text, two
   models, run as sub-agents: Claude Sonnet and Claude Haiku. Raw output to
   `research-log/extractions/p5-2014/<model>.json`. Cross-vendor models (GPT, Gemini)
   need API keys and wait for v1.
4. **Line them up.**
   `python3 scripts/compare_extractions.py <a>.json <b>.json research-log/hand-check/p5-2014.csv`
5. **Adjudicate conflicts with Opus.** Opus fills `verdict` (`a`, `b`, `both`, `neither`),
   `correct_value`, and `adjudication_note` into `p5-2014-adjudicated.csv`. This is the
   resolution event for the model trust data, labelled Opus-adjudicated.
6. **Merge** with `python3 scripts/build_bets.py <report> <adjudicated>.csv <a>.json <b>.json --map <map>.csv`,
   then `python3 scripts/fill_agency.py <agency-records>.csv` for agencies the report does not name. Add a `built` outcome per bet with a
   `source_url`.
7. **Score the models.** `python3 scripts/compare_extractions.py --score research-log/hand-check/p5-2014.csv`
   gives accuracy per model per field: the first jagged profile.
