# Promise ledger scorecard

Thirty-three ranked bets from two reports, checked against what happened, as of
October 2026. Twelve are the ranked items of Astro2010 (*New Worlds, New Horizons*, the
2010 astronomy decadal survey); twenty-one are the projects in P5 2014 (*Building for
Discovery*, the particle physics plan). Each bet is logged as the report wrote it: the
promise, the science question it was sold on, the cost and date given, the funder. Four
questions are then scored per bet, each with a source link, a one-line rationale, and a
confidence (`confident` or `guess`) in `data/outcomes.csv`. Numbers below come from
`scripts/scorecard_stats.py`.

Built and cost for astronomy are already covered by Pan and Trimble (2024, BAAS 56(1),
arXiv:2311.02950) and by the Academies' 2016 midterm assessment. The ledger cites them
and spends its effort on what nobody covers: P5, the science question, and attribution.

## 1. Was it built?

| | Built | Partly | Being built | Never | Cancelled |
|---|---|---|---|---|---|
| Astro2010 (12) | 4 | 2 | 4 | 1 | 1 |
| P5 2014 (21) | 6 | 4 | 4 | 6 | 1 |
| Both (33) | 10 | 6 | 8 | 7 | 2 |

In Pan and Trimble's five categories (ours for Astro2010, since they do not code those
rows): Astro2010 has 5 items operating within 15 years on mostly federal money, 1 built
later with federal money (Roman), 5 built or building with mostly other money (LISA, IXO
as Athena, GSMT, CTA, CCAT), 1 never (SPICA). P5 2014 has 7 operating within the window on
federal money, 2 on mostly other money (LHC Phase-1, MICE), 7 never, and 5 still inside
their 15-year window. Pan and Trimble's rule of thumb across seven surveys, about a third
operating on time, a third late or on other money, a third never, holds for both reports.

**The pattern that matters:** half of Astro2010's large and medium items ended up built by
someone else. The US withdrew from LISA and IXO in 2011, never joined CTA construction,
and has yet to fund a giant telescope. P5's never-built list is different in kind: six of
its seven are projects the panel itself ranked N in every budget scenario.

## 2. What did it cost, and when did it arrive?

Twelve bets have a cost at ranking and a later cost on the same basis. The answer depends
on what the first number was.

| First estimate | Bets | Median latest/first | Over by more than 15% |
|---|---|---|---|
| Astro2010 survey appraisal (FY2010 $) | 3 | 2.3x | 3 of 3: WFIRST/Roman 2.7x, GMT 2.3x, LSST/Rubin 1.7x |
| DOE baseline after P5 ranking (CD-2 total project cost) | 9 | 1.0x | 2 of 9: LBNF/DUNE 2.2x, PIP-II 1.4x, both still building |

Every DOE project that reached its CD-2 baseline and finished came in at 0.97x to 1.00x
(Muon g-2, DESI, LSST camera, LZ, the LHC Phase-1 upgrades). The overruns sit in the
estimates made before a baseline: the decadal appraisals, and the CD-1 ranges that LBNF
(1.26 to 1.86 billion in 2015, 3.28 billion now) and PIP-II outgrew. DESI's own 2012
CD-0 range was 1.3 to 2.2x below its final cost. So the variation is by estimate stage
more than by agency: DOE's baselines hold; the numbers committees rank on do not. (Bases
differ and are labelled in each row: appraisals are FY2010 dollars and total cost, DOE
figures are then-year dollars and the DOE share.) NASA appears in one comparable row
(Roman, 2.7x); NSF never funded construction of GMT or CTA, so there is no NSF number to
compare.

**Time to first data.** Ten bets have taken first data (the four program lines are
scored on funding, not data). Median wait from ranking: 7.5 years (range 1 to 16). The two Astro2010 flagships took 15 and 16 years (Rubin First Look
June 2025, Roman launch August 2026); the P5 projects that finished took 1 to 12. Against
the date the report itself gave, 5 of 8 arrived on time or early and 3 arrived late:
Rubin and Roman by about 6 years, the LHC Phase-1 upgrades by 4. Eight more bets are still
to come, projected 12 to 25 years after ranking (LISA and GMT both mid-2030s).

## 3. Did it answer the question it was sold on?

Five bets on three named questions, scored against the promise as written.

| Bet | Question sold on | Result | What happened |
|---|---|---|---|
| DESI (P5 2014) | Dark energy parameters to 5% by 2020, 1% by 2025 | **surprise** | With 3 of 5 survey years, a constant equation of state is pinned to 2 to 3.5% (5% met, 1% not). The unpromised result: every data combination prefers dark energy that weakens over time, at 2.8 to 4.2 sigma, below the 5 sigma discovery bar. Full results 2027 |
| WFIRST/Roman (Astro2010) | Why is the expansion accelerating | **not yet** | Launched 2026-08-30, in commissioning. First dark energy result expected about 2029 to 2030 |
| LSST/Rubin (Astro2010) | Why is the expansion accelerating | **not yet** | Survey began 2026-06-30. One year of data should match DESI plus CMB precision; first result plausibly 2028 |
| LBNF/DUNE (P5 2014) | Neutrino mass ordering, CP violation | **not yet** | No beam before 2031; a 3 sigma ordering answer about 2034. JUNO and NOvA are projected to get there first, around 2030 to 2032 |
| CMB-S4 (P5 2014) | Amplitude of inflationary gravitational waves to percent level by 2025 | **no** | Best bound r < 0.034, 10 to 20 times above the design threshold. Half the goal (refuting BICEP2) was done in 2015 by existing instruments. DOE and NSF dropped the project in July 2025 |

One of five answered, and it answered a question the report did not ask. Three cannot be
scored before 2028 to 2034: time to an answer runs longer than time to build. One was
cancelled before it could try. Both reports sold the dark energy bets on "why is the
expansion accelerating"; the first data on that question came from the smallest of the
three (DESI, under 60 million dollars), and the two flagships are now cast as its check.

## 4. Whose call was it?

Attribution is recorded per bet and per question in `data/actors.csv` (committee, chair,
champions, agencies, with roles at the time). Named people stay internal; this page
scores at committee and agency level.

- **What kills a bet the whole community agreed on:** CMB-S4 was endorsed by P5 2014,
  Astro2020 and P5 2023. NSF ruled out the South Pole site in May 2024 and both agencies
  withdrew in July 2025. The cancellation scores the agencies; the committee's forecast,
  that the question was reachable by 2025, scores the committee and was already unmet.
- **Partnerships dissolve:** the two Astro2010 space bets that depended on ESA (LISA, IXO)
  both lost NASA as an equal partner within a year of the report. NSF's inability to
  fund its share took CTA and the giant telescopes off the federal books.
- **Where the P5 forecast held:** the five finished DOE projects came in on budget and
  five of six finished P5 bets inside the report's own window. The misses are the two
  largest, LBNF and PIP-II, whose first baselines came three to four years after ranking.

## What the ledger does not yet say

Five P5 projects are still inside their 15-year window, so their category is blank.
Astro2010 program lines (Explorer, MSIP, the two technology programs) are scored on
funding delivered, from the 2016 midterm and Astro2020. A dozen facts rest on search
snippets where the primary host was unreachable; each is marked `guess` with the reason.
Cost bases are labelled, not inflation-adjusted. The science-question verdicts are one
reader's call on the published results and are meant to be argued with; the evidence
file (`research-log/outcomes/science-question-evidence.md`) holds every source read.
