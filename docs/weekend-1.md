# Weekend 1: extend Pan and Trimble to P5 2014

**Goal.** Every P5 2014 bet in `data/bets.csv`, with whether it was built in
`data/outcomes.csv`, extracted by two models and hand checked. Astro2010 rows seeded from
Pan and Trimble alongside, so both reports sit in one table.

**Good enough.** All P5 2014 large and medium projects, promise side hand checked, built
status sourced. Cost variance and schedule are Weekend 2.

## Status

| Step | State |
|---|---|
| Schema, extraction prompt, compare script | Done |
| Sources (P5 2014, Pan and Trimble preprint) | Done, in `sources/`. See `sources/README.md` for what Pan and Trimble do and do not cover |
| Two-model extraction of P5 2014 | Done, v2 prompt. Sonnet 23 bets (12 guess), Haiku 20 (0 guess). v1 kept in `research-log/extractions/p5-2014/v1/` |
| Hand check | **David.** `research-log/hand-check/README.md`: 34 cells for this weekend, 50 more for Weekend 3 |
| Merge into `data/`, built status, score | After hand check |

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
5. **Hand check every row** (David). Fill `verdict` (`a`, `b`, `both`, `neither`) and
   `correct_value`. This is the resolution event for the model trust data.
6. **Merge** checked rows into `data/bets.csv`. Add a `built` outcome per bet with a
   `source_url`.
7. **Score the models.** `python3 scripts/compare_extractions.py --score research-log/hand-check/p5-2014.csv`
   gives accuracy per model per field: the first jagged profile.
