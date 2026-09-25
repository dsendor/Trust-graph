# 📒 Promise ledger: scoring the decadal and P5 bets

> **Unverified.** Bill's research and design, 2026-09-24. Extends proposal A in
> [Applying Paul's approach to physics and astronomy](https://app.notion.com/p/8a68006af42e44bbb9a0778c8014f711).
> First dataset for the [trust graph POC](https://app.notion.com/p/c231e4e6dec04385acb0b6e8adef649b).
>
> Imported from Notion on 2026-09-25:
> [original page](https://app.notion.com/p/55db65007f7e4876900d939fae3928c9).

**What it is.** Every ranked bet in Astro2010 and P5 2014, logged as a promise with a
cost, a date, and the people who made the call, then checked against what happened.

Four questions per bet:

1. **Was it built?**
2. **What did it cost, and when did it arrive?** Measured against the estimate at the time of ranking.
3. **Did it answer the question it was sold on?** Each report names a specific science
   question for each bet. This asks what became of that question.
4. **Whose call was it?** Which committee members and champions backed it.

## What already exists

Questions 1 and 2 have answers in the literature. Start from those rather than redoing them.

| Source | What it covers |
|---|---|
| [Pan and Trimble 2024](https://baas.aas.org/pub/2024i006/release/1), BAAS 56(1), extending [Trimble 2011](https://arxiv.org/pdf/2311.02950) | Every prioritized facility from seven decadal surveys, sorted under "what they asked for" and "what we got." Across 106 requests in the first five reports: roughly a third operating within 15 years on mostly federal money, a third later or with other funding, a third never happened |
| [CATE](https://www.nationalacademies.org/read/24857/chapter/5), required since the 2008 NASA Authorization Act | An independent cost estimate for every candidate mission, built to be compared against what advocates claimed. Run by Aerospace Corporation |
| Midterm assessments: [Astro2010](https://www.nationalacademies.org/projects/DEPS-SSB-14-05/publication/23560), [planetary](https://www.nationalacademies.org/read/25186/chapter/8), [Earth science](https://www.nationalacademies.org/read/27743/chapter/12) | Progress against recommendations, with cost and schedule sections |
| [Powering Science: NASA's Large Strategic Science Missions](https://www.nationalacademies.org/read/24857/chapter/5), NASEM 2017 | Cost overruns in large NASA missions |

Questions 3 and 4 have no equivalent. All of the above is astronomy and space science,
so P5 has no version of it either.

## Why it works as the test case

- **Outcomes have arrived.** Astro2010 is sixteen years old, P5 2014 is twelve. Most bets have resolved on something.
- **All three entity types appear.** Claims (the bets and their science questions),
  people (committee members, project leads), and models (the extraction step, hand-checked).
- **The community reports on progress, not on judgment.** The Academies ran a
  [midterm assessment of Astro2010](https://www.nationalacademies.org/projects/DEPS-SSB-14-05/publication/23560)
  in 2016, and the P5 2023 report declared the 2014 plan successful.[^1] Both track
  whether things got built and funded. Neither asks whether the science question got
  answered or whose forecast held up.

## Seed rows

| Bet | Source | Promise | What happened | Where it stands |
|---|---|---|---|---|
| WFIRST | Astro2010, top large space priority | Wide-field infrared survey for dark energy and exoplanets | Launched as Roman on 2026-08-30[^2] | Built. Science question open |
| LSST | Astro2010, top large ground priority | Ten-year time-domain survey of the southern sky | Rubin began the LSST in June 2026[^3] | Built. Science question open |
| DESI | P5 2014 | Precision measurement of dark energy | 2025 results strengthened hints that dark energy evolves[^4] | Built. Answered, with a surprise |
| Muon g-2 | P5 2014 | Precision measurement of the muon magnetic anomaly | Final result June 2025, the most precise to date[^5] | Built. Answered |
| LBNF/DUNE | P5 2014 | Long-baseline neutrino program | US cost estimate $2.6B in 2020,[^6] range $3.16B to $3.68B by 2024[^7] | Building. Over estimate |
| CMB-S4 | Astro2020, P5 2023[^8] | Search for the signal of cosmic inflation | DOE and NSF withdrew support 2025-07-09[^9] | Cancelled after two endorsements |

**Three patterns already visible in six rows:**

1. **Time to data runs in decades.** Both Astro2010 top priorities reached first science in 2026.
2. **Delivered bets can surprise.** DESI was built to measure dark energy and found hints
   that it changes over time. The ledger needs an outcome type for "answered, differently
   than expected."
3. **Consensus did not save CMB-S4.** Two community endorsements, then a budget
   cancellation. Outcomes get attributed separately: a cancellation scores agency
   follow-through and leaves the scientists' judgment untouched.

## What to record

- **Bet:** source report, rank, the promise as written, the science question, cost
  estimate at ranking, target date, field (arXiv category), champions.
- **Outcome:** which of the four questions it answers, date, result (yes, no, partial, surprise), source link.
- **Actor:** person, committee, or agency, with their role at the time of the bet.

## What the finished ledger answers

1. How far off were the cost estimates, and does that vary by agency?
2. How long from ranking to first data?
3. What share of built facilities answered the question they were built for?
4. What kills a bet the whole community agreed on?

## Build plan

1. **Weekend 1.** Take the Pan and Trimble table as the starting point for built and
   cost, then extend it to P5 2014, which nobody covers. Extract with two models and hand
   check every row, which doubles as the model trust data for the POC.
2. **Weekend 2.** Fill cost and schedule gaps from agency project pages and GAO major-projects reports.
3. **Weekend 3.** The science question, on three named cases: dark energy's equation of
   state (DESI, Roman), neutrino mass ordering (DUNE), primordial gravitational waves
   (CMB-S4). Record who championed each.

**Deliverable:** the database plus a one-page scorecard. Good enough is five bets scored
on the science question with attribution. It is the artifact for the Paul email.

[^1]: [P5 report, Hitoshi Murayama](https://nsf-gov-resources.nsf.gov/attachments/308681/public/2_P5_Report_Hitoshi_Murayama.pdf)
[^2]: [SpaceX: Roman](https://www.spacex.com/launches/roman)
[^3]: [Rubin: LSST](https://rubinobservatory.org/explore/how-rubin-works/lsst)
[^4]: [Fermilab: new DESI results strengthen hints that dark energy may evolve](https://news.fnal.gov/2025/03/new-desi-results-strengthen-hints-that-dark-energy-may-evolve/)
[^5]: [Fermilab: Muon g-2 most precise measurement](https://news.fnal.gov/2025/06/muon-g-2-most-precise-measurement-of-muon-magnetic-anomaly)
[^6]: [AIP FYI: flagship neutrino project working to keep costs within cap](https://www.aip.org/fyi/2020/flagship-neutrino-project-working-keep-costs-within-cap)
[^7]: [DOE PM Workshop 2024: LBNF/DUNE](https://www.energy.gov/sites/default/files/2024-04/Day2%201100%202024%20DOE%20PM%20Workshop%20LBNFDUNE%20-%20New%20Video%20Encoding.pdf)
[^8]: [2023 P5 report: the recommended program](https://www.usparticlephysics.org/2023-p5-report/the-recommended-particle-physics-program.html)
[^9]: [CMB-S4](https://cmb-s4.org/)
