# Astro2010 ground bets: cost-schedule notes

Written 2026-10-01 for the rows in `astro2010-cost-schedule-ground.csv`. Bases: Astro2010
(NWNH) costs are the survey's CATE appraisals in FY2010 dollars, total not US share (US
share in parentheses in Table ES.3). Later figures are agency totals in then-year dollars
unless marked. No inflation-adjusted comparison was found for any of these five bets, so
ratios are then-year over FY2010 and labelled as such. Hosts tried and blocked: nsf.gov,
gao.gov, lsst.org, rubinobservatory.org, giantmagellan.org, cornell.edu,
cta-observatory.org, ar5iv.labs.arxiv.org, spiedigitallibrary.org.

Scoring rule used (from the task brief): `yes` if cost ratio <= 1.15 and first data inside
the target window; `partial` if over by up to 2x or late by up to 5 years; `no` if more than
2x over or more than 5 years late; `building` if no final cost or first data yet.

## astro2010-lsst (Rubin Observatory): no, borderline

- https://www.nationalacademies.org/read/23560/chapter/5 (2016 midterm, chapter 3, read
  from the saved copy mid-ch5.txt): Table 3.1 reproduces NWNH: LSST $465M ($421M federal),
  FY2010 dollars; "NSF ... Major Research Equipment and Facilities Construction (MREFC)
  award in August 2014"; "Authority to begin camera fabrication was granted by DOE in
  August 2015"; "Engineering First Light is planned in 2020, with the 10-year science survey
  commencing in late 2022"; Finding 3-1: "on schedule and within budget".
- DOE Science FY2016 Congressional Budget Justification, Vol. 4 (saved as
  cbj-FY2016-SC-Vol4.txt from energy.gov): "CD-2 for the LSSTcam project was approved on
  January 7, 2015, with a TPC of $168,000,000 and completion date of FY 2022." FY2020 HEP
  justification: CD-3 August 27, 2015, TPC $168,000,000, components complete FY2020.
  FY2023 HEP justification: LSSTCam "completed its MIE funded construction phase in 2021",
  survey "expected to start in 2024".
- https://www.aip.org/fyi/slac-completes-largest-digital-camera-ever-built-for-astronomy
  (Apr 10 2024): "The camera cost roughly $168 million to build, funded by the Department
  of Energy"; NSF "has so far authorized $551 million" (link to the project's Jan 2024 EVMS
  cost report).
- NSF budget request documents (nsf-gov-resources.nsf.gov, blocked; search snippet only):
  original NSF TPC $473.0M; "In December 2021, NSB authorized a new Total Project Cost of
  $571.0 million" after the COVID rebaseline. Not verified on a reachable host, so the row
  carries both 551 (sourced) and 571 (snippet).
- https://www.energy.gov/science/articles/ever-changing-universe-revealed-first-imagery-nsf-doe-vera-c-rubin-observatory
  (Jun 23 2025): First Look imagery released that day; survey to begin "later in 2025".
- https://news.fnal.gov/2026/06/action-nsf-doe-vera-c-rubin-observatory-begins-capturing-the-greatest-cosmic-movie-ever-made/
  (Jun 30 2026): LSST formally began; follows the June 2025 First Look.
- https://arxiv.org/abs/2603.23786 (Rubin Data Preview 1; via search summary of the paper):
  first on-sky commissioning campaign with ComCam 2024-10-24 to 2024-12-11.
- Arithmetic: federal 551 + 168 = 719 then-year vs 421 FY2010 federal appraisal, ratio
  1.71 (739 and 1.76 with the $571M TPC). Window end 2019-12-31 to First Look 2025-06-23
  is 5.5 years; to survey start 2026-06-30 is 6.5 years; to ComCam first photons
  2024-10-24 is 4.8 years. Verdict `no` by the rule, but it flips to `partial` if ComCam
  counts as first data. Flagged in the rationale for David.
- Not verified: the private share of the actual total (early mirror and site work), so no
  total-to-total ratio is given.

## astro2010-gsmt (GMT, with TMT dropped): building

- Midterm chapter 3 (same URL as above): appraisals $1.1B (GMT), $1.4B (TMT), federal
  $257M-$350M; GMT ground breaking November 2015 with 70 percent pledged; TMT 80 percent
  pledged, construction interrupted; Finding 3-5: "NSF budget constraints have prevented
  NSF's implementation of the NWNH recommendation".
- https://www.nationalacademies.org/read/26141/chapter/9 (Astro2020, chapter 7): "Federal
  investment in the U.S. ELT program for the U.S. community. $1.7 billion NSF share of
  $5.1 billion project"; "expected to commence operations in the mid-2030s, contingent on
  a U.S. funding commitment."
- https://www.aip.org/fyi/nsf-likely-to-drop-one-of-two-giant-telescopes-from-consideration-for-construction-funds
  (Mar 1 2024): NSB "$1.6 billion ceiling" on NSF's contribution to TMT and/or GMT; GMT
  "total project cost of $2.54 billion" with "more than $850 million" committed by
  partners; TMT partners "$2.0 billion"; board anticipates a down-selection.
- https://www.aip.org/fyi/external-panel-to-advise-nsf-on-extremely-large-telescope-plans
  (May 2 2024) and https://www.aip.org/fyi/gmt-and-tmt-still-in-limbo-after-external-review
  (Dec 16 2024): external panel; "Entering FDP is not a commitment by NSF to fund
  construction". No dollar figures.
- https://www.aip.org/fyi/the-week-of-june-2-2025: FY2026 request: NSF "will not advance
  the Thirty Meter Telescope project to the final design phase or supply any further
  funding"; GMT advanced "to the final design phase but does not commit to seek
  construction funding". (NSF's own June 12 2025 announcement is on giantmagellan.org and
  nsf.gov, both blocked.)
- https://www.aip.org/fyi/nsf-construction-budget-defunded-as-trump-challenges-emergency-spending
  (Apr 1 2025): GMT and TMT "have been waiting in the wings for MREFC funding", either
  "would require a significant and sustained MREFC budget increase".
- https://www.aip.org/fyi/trump-proposes-deep-research-cuts-new-icebreaker-for-nsf
  (Apr 9 2026): FY2027 request: "The GMT will be completed without further funds from NSF";
  Congress had directed NSF to also advance TMT in the FY2026 explanatory report.
- https://arxiv.org/abs/2608.10212 (GMagAO-X final design, Aug 2026, read via pdftotext):
  instrument "on track to be ready at first-light of the GMT in the mid 2030s".
- Arithmetic: 2540 / 1100 = 2.31 (then-year vs FY2010). NSF construction share so far 0.
- Not found: the dollar amount of NSF design-phase awards to GMT and TMT (AIP says NSF
  "has funded design and technology development work for each" without a figure).

## astro2010-ccat (now the 6 m Fred Young Submillimeter Telescope): building

- Midterm chapter 3: "NWNH recommended an NSF-AST investment of $37 million in the $140
  million cost of construction ... annual contribution to operations of $7.5 million";
  "The NSF contribution so far this decade to CCAT has been support for the design at
  $4.75 million from 2011 to 2015"; MSIP proposal not funded; project "now being
  rebaselined".
- Pan and Trimble 2024 (sources/pan-trimble-2024.txt): CCAT "Descoped to 6m Fred Young
  Submm ... US-Germany-Canada for 2024".
- https://arxiv.org/abs/2107.10364 (CCAT-prime science paper, Jul 2021): "first light in
  mid-2024", 6 m aperture, Cornell-led consortium. No cost.
- https://arxiv.org/abs/2511.01707 (Nov 2025): "scheduled for first light in 2026". No cost.
- https://arxiv.org/abs/2608.25111 (Aug 25 2026, read via pdftotext): Prime-Cam shipped
  June 2026, arrived on site 2026-07-31, "scheduled for integration in FYST in late 2026,
  followed by a year of early science observations" with the 280 and 350 GHz modules;
  EoR-Spec and 850 GHz modules 2027. No cost.
- https://arxiv.org/abs/1807.06675 (2018 SPIE): telescope built by "CCAT Observatory, Inc.";
  no cost.
- Search snippets only (hosts blocked): Vertex Antennentechnik contract signed
  2017-03-31 "with first light expected in 2025"; Fred Young gave "over US$16 million";
  Canada CFI plus provinces C$9.4M; NSF $1.3M award in 2021 (news.cornell.edu).
- Not found anywhere reachable: a total FYST construction cost. The ratio is left
  uncomputed rather than compare a 25 m appraisal with a 6 m telescope.

## astro2010-acta (CTAO, US did not join): building

- Midterm chapter 2 and 3: "NSF-AST participation in the Cherenkov Telescope Array (CTA)
  has not occurred because of budgetary constraints"; NSF MRI "funded a prototype SCT
  ... in 2012"; NWNH recommended "a U.S. budget for construction and operations of
  approximately $100 million over the decade be shared between DOE, NSF-Physics, and
  NSF-Astronomy"; CTA construction "expected to start in 2017 with completion in 2024".
- https://arxiv.org/abs/1709.05434 (CTA Consortium, 2017, read via pdftotext): "The
  estimated cost for the baseline implementation of CTA, consisting of 99 telescopes ...
  in the southern array and 19 telescopes ... in the northern array is 400 MEuro
  (including FTE's)"; 2016 threshold implementation "250 MEuro"; construction to start
  2018.
- https://arxiv.org/abs/2305.12888 (Hofmann and Zanin, May 2023, read via pdftotext): 2016
  staged plan "with a cost of the first stage of about 60% of the full cost"; 2021 "CTAO
  Cost Book" set the alpha configuration "4 LSTs and 9 MSTs in the north, and 14 MSTs and
  37 SSTs in the south"; ERIC application submitted mid-2022. The Cost Book total is not
  given.
- https://arxiv.org/abs/2512.03798 (Hinton, Dec 2025): CTAO-South "observations with the
  first telescopes are expected to begin in 2026"; LST-1 in the north completed 2018.
- https://arxiv.org/abs/2509.05527 (Sep 2025): SCT "is a candidate MST for CTAO-South";
  "The initial CTAO configuration will include 14 MSTs of the DC design and no SCTs";
  pSCT inaugurated January 2019, first gamma ray 2020-01-17.
- https://arxiv.org/abs/2010.13027 (Oct 2020, read via pdftotext): "The pSCT has been
  designed, procured and constructed at the Fred Lawrence Whipple Observatory (FLWO) at the
  cost of US$ 5.2M funded by NSF (US$ 3.9M) and participating institutions (US$ 1.3M)."
- https://arxiv.org/abs/2605.18596 (NectarCAM, May 18 2026): first production NectarCAM
  ready summer 2026; no cost or US content.
- Search snippet only (cta-observatory.org blocked): "$3.9 million grant from the National
  Science Foundation" to US teams for ten SST cameras. Not verified.
- Not found: the alpha-configuration cost in euros; the pSCT camera-upgrade MRI amount; any
  DOE spend on CTA.

## astro2010-msip (Mid-Scale Innovations Program): partial

- Midterm chapter 3: NWNH asked for "$40 million per year"; "NSF-AST funded midscale
  activities at a level of $31 million in FY2010"; "Overall, NSF-AST mid-scale funding
  dropped from $31 million in FY2010 to a nadir of $15.5 million in FY2015, recovering to
  $21 million in FY2016"; first MSIP call 2013, second 2015; "Six awards were made with a
  total from NSF-AST FY2014/FY2015 of $27.1 million and other NSF support of $20 million".
- https://www.nationalacademies.org/read/26141/chapter/8 (Astro2020, chapter 6): "Astro2010
  recommended MSIP as its second highest priority for large programs on the ground" at
  "~$40 million a year (FY 2010)"; "In its first three cycles, MSIP has competitively
  awarded a total of $114 million to 18 distinct projects" (2014-2021), awards "between $2
  million and $12 million per project"; most recent cycle "$21 million in funding, well
  below the $40 million a year target".
- https://www.aip.org/fyi/2021/astro2020-decadal-survey-priorities-small-and-mid-scale-projects
  (Dec 22 2021): MSIP "has been funded at a lower overall level than was recommended in the
  last decadal survey"; Astro2020 recommends ramping MSIP plus MSRI astronomy funding to
  "$50 million in total" per year.
- Pan and Trimble 2024: MSIP "Many funded, often technical development for bigger things,
  like ngVLA, BICEP, and IceCube-Gen2".
- Arithmetic: $114M over 2014-2021 is 1.2x the $93M floor and 0.57 of the $200M ceiling in
  nominal dollars, but the recommendation was an augmentation to $40M/yr and the actual
  annual level was about half that, so the row reports the ratio as about 0.5 of target.
- Not found: a year-by-year MSIP obligation table after FY2016 on a reachable host.
