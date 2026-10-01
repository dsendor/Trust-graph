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
