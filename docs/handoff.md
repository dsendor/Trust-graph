# Handoff: finishing the ledger

What a new session needs that the other docs do not say. Written 2026-10-01, after
Weekend 1 merged.

## The goal

**Ship the scorecard.** Done means all four of these:

1. **Cost and schedule (Weekend 2).** A `cost-schedule` outcome in `data/outcomes.csv`
   for every bet whose `built` result is `yes`, `partial`, or `building`: cost estimate
   near ranking, latest or final cost, ratio, target date vs first-data date, each with a
   `source_url`.
2. **Science question (Weekend 3).** A `science` outcome for five bets on three named
   questions: dark energy's equation of state (DESI, Roman/WFIRST, LSST), neutrino mass
   ordering (LBNF/DUNE), primordial gravitational waves (CMB-S4). Result is `yes`, `no`,
   `partial`, or `surprise`, with sources and a `confidence`.
3. **Attribution (Weekend 3).** `data/actors.csv` filled for those five bets: the
   committee (P5 2014, Astro2010), its chair, and the project's named champions, with
   roles at the time. Named people stay internal (CLAUDE.md rule 7).
4. **Scorecard.** `docs/scorecard.md`, one page: the four questions the ledger answers
   (`docs/promise-ledger.md`, "What the finished ledger answers"), each answered from the
   data with numbers, plus the five science-question cases. Cite Pan and Trimble for what
   they cover. It is the attachment for the Paul email, so it must read cold.

**Not in scope until David says so:** the trust graph build (schema, code, trust math),
publishing anything, emailing anyone, making the repo public.

## Status, 2026-10-02 (round 2)

David's rulings: he does not have the knowledge to settle the five borderline calls, so
they stay as scored, marked `guess`, with both readings in the rationale and a
"Borderline calls" section in the scorecard. CLAUDE.md now points at the scorecard and the
site. The `science` and attribution questions were then extended to every built or
building bet: 25 `science` rows (5 answered, 2 of them surprises; 4 partly; 3 no; 13 too
early) and 292 actor rows covering all 24 of those bets. Round-2 research notes:
`research-log/outcomes/science-round2-*.md` and `actors-round2-*.md`. Rescore when SBND
publishes its joint sterile-neutrino result, when DESI's five-year result lands (2027),
and when JUNO reports on the mass ordering.

## Status, 2026-10-01 (after the scorecard session)

All four "done" items above are in: 24 `cost-schedule` outcomes, 5 `science` outcomes,
107 actor rows for the five bets, and `docs/scorecard.md`. `scripts/scorecard_stats.py`
prints the scorecard's numbers from `data/`. A website (`site/`, built by
`scripts/build_site.py`) explains the results for a non-physicist at committee and agency
level only. Research notes per bet are in `research-log/outcomes/*-cost-schedule-*.md`,
`science-question-evidence.md` and `actors-draft.md`.

Calls made this session that David may want to revisit: Rubin's `cost-schedule` is `no`
by the letter of the rule (First Look 5.5 years past the window; `partial` if ComCam first
photons count); ACTA's is `no` on US terms (the US share never arrived) while its `built`
row stays `building` for CTAO; LAr1 is scored on SBND against the SBN proposal's 2018
plan; Mu2e sits exactly on the yes/partial cost line and the partial/no schedule line;
CMB-S4's science row is `no` with `partial` noted as defensible. Of the five snippet-based
facts flagged below, the LBNF cost figures are now confirmed from the budget
justifications and SuperCDMS's mid-2026 start from Fermilab news; NSF's share of the
IceCube Upgrade, the exact CMB-S4 statement date, and the Roman commissioning dates still
rest on snippets and are marked `guess`.

Not done, by rule: CLAUDE.md "Where to look" does not yet point at `docs/scorecard.md`,
`scripts/scorecard_stats.py` or `site/` (rule 1: ask David before editing that file).

## Decisions David has made

- **Opus settles every conflict** between extraction models. David does not hand check.
  Label these resolutions Opus-adjudicated in the model trust data.
- **SBN is a bet** even though it is a portfolio (his override, 2026-09-28).
- **Agency:** the report's statement wins; where the report is silent, fill from funding
  records (`scripts/fill_agency.py`). CTA and DESI records disagree with the report;
  the report's version is kept.
- **Keep the same two extractors** (Sonnet as model a, Haiku as model b) for any new
  extraction, so the model trust data stays comparable. Opus adjudicates. If you use a
  different model anywhere, say so in the file name.
- **TL;DR goes at the end of chat replies only**, never at the start, never in documents.
- **Good Enough Protocol.** Don't polish what already works; ship the scorecard.

## Environment gotchas

- **Network is allow-listed.** Hosts that work: `news.fnal.gov`, `energy.gov`,
  `aip.org` (with `www`), `arxiv.org`, `www.nationalacademies.org`,
  `nap.nationalacademies.org`, `usparticlephysics.org`. Blocked: `nasa.gov`,
  `science.nasa.gov`, `nsf.gov`, `esa.int`, `rubinobservatory.org`, `osti.gov`,
  `cern.ch`, `gao.gov` (403), `baas.aas.org` (403), Wikipedia, most journals. When a
  primary host is blocked, find the open copy (arXiv preprint, Fermilab news, AIP FYI,
  DOE budget justification) and say which copy you read. Ask David to open a host only if
  no alternative exists.
- **Academies reports** read as HTML at `nap.nationalacademies.org/read/<id>/chapter/<n>`.
  The 2016 Astro2010 midterm assessment is `read/23560`.
- **PDF tooling:** `pypdf` needs `pip install cffi` first. `pypdfium2` renders a page to
  PNG, which is how the adjudicator reads tables whose layout the text loses.
- **Brave search** (from science-gap-map-analysis, `engine/search.mjs`) is not ported.
  It needs `BRAVE_API_KEY` in the environment's secrets and `api.search.brave.com`
  allowed. Weekend 2 is about 30 lookups; port it only if logged, cached searches turn
  out to matter. WebSearch plus WebFetch worked for Weekend 1.
- **GitHub:** the repo is `dsendor/Trust-graph`. Claude cannot create repos. Push
  branches with git; open PRs with the GitHub tools. Never commit to `main`.

## Data caveats to carry or fix

- **P5 costs:** the report gives only size bands. Use the earliest agency baseline after
  ranking (for DOE projects, the CD-2 total project cost) as `cost_at_ranking` in the
  `cost-schedule` outcome, and say so in `rationale`. Do not overwrite `bets.csv`.
- **Astro2010 costs** are survey appraisals in FY2010 dollars (total, not US share; US
  share is in `rationale`). Compare like with like, or label the basis of each number.
- **Five P5 facts rest on search snippets** (hosts unreachable): SuperCDMS SNOLAB start
  date, DOE pausing XLZD, NSF's share of the IceCube Upgrade, the exact CMB-S4 statement
  date, US non-membership of CTAO. Verify if a Weekend 2 or 3 source reaches them.
- **Astro2010 program rows** (Explorer, MSIP, the two technology programs) are sourced to
  the 2016 midterm, so their status is only as of 2016.
- **P5 `pt_category` is blank for five bets** still under construction (Mu2e, PIP-II,
  HL-LHC, LBNF, DM G3) because the 15-year window runs to 2029.
- **Muon g-2's scenario cell** carries Table 1's "Mu2e small reprofile needed" note,
  because the table shares one row for both. Leave it; it is literal.
- **One verbatim quote contains an em dash** (from the report). Quotes stay verbatim.

## Recipe for a new report or a new extraction

`docs/weekend-1.md` Steps 1 to 7 and the CLAUDE.md commands. Save the source text in
`sources/`, add the report's allowed values to `prompts/extract-bets.md`, run both
extractors as sub-agents on the same text, compare, have Opus adjudicate, build, fill
agency, research outcomes with sources.

## Open questions for David (ask only if a weekend is blocked on one)

From `docs/trust-graph-or-ledger.md`: is this artifact for conversations or for a
company; how many weekend blocks exist before year end; ledger only, or the trust graph
after it. The scorecard goal above holds whichever way he answers.
