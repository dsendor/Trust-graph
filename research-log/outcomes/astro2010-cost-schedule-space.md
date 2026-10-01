# Astro2010 cost-schedule outcomes, space bets (Weekend 2)

Notes for `astro2010-cost-schedule-space.csv`. Written 2026-10-01. Per bet: every URL read,
what it said (numbers and dates with their basis), and what could not be verified.

Scoring rule used (from the task brief): `yes` if cost ratio <= 1.15 and first data within
the target window; `partial` if over by up to 2x or late by up to 5 years; `no` if more than
2x over or more than 5 years late; `building` if no final cost or first data yet. Program
lines (Explorer, the two technology programs) are scored on funding delivered versus the
recommended augmentation, and on timing.

Bases, stated once: Astro2010 (NWNH) costs are the survey's appraisals in FY2010 dollars,
total mission cost (US share in `data/bets.csv` rationale). For WFIRST, LISA and IXO these
are CATE appraisals "for phase A costs onward"; for the Explorer augmentation and the medium
space elements they are committee-generated. Later NASA figures are then-year dollars.

Hosts blocked this session: nasa.gov, gao.gov, esa.int, ww2.aip.org (the www.aip.org copies
of the same FYI pages work).

## astro2010-wfirst (Roman): no

Sources read:

- https://www.nationalacademies.org/read/23560/chapter/6 (2016 midterm, chapter 4 of the
  report, served as chapter 6). NWNH adopted $1.6 billion (FY2010) from the CATE of the
  JDEM-Omega design, launch 2020. NASA's 2015 CATE-informed projection of the 2015 DRM with
  coronagraph: $2.0 billion to $2.3 billion in FY2015 dollars, of which $0.35 billion was
  the coronagraph (including an extra year of operations) and $0.1 billion the expanded GO
  program. "The estimated cost of the 'original' WFIRST scope envisioned by NWNH was $1.8
  billion, very close to the NWNH value of $1.6 billion after adjustment from FY2010 to
  FY2015 dollars." Changes between the 2015 DRM and KDP-A added about 25 percent ($550
  million). "NASA's current cost projection for WFIRST is $2.6 billion to $2.8 billion in
  FY2015 dollars for a 2025 launch." Phase A start February 2016. Finding 4-2 on cost-growth
  risk. Footnote 17: NWNH's WFIRST estimate did not include the guest investigator program.
- https://www.aip.org/fyi/2017/final-fy17-appropriations-nasa: $105 million for WFIRST in
  FY2017, Congress applied a $3.5 billion life-cycle cost cap.
- https://www.aip.org/fyi/2020/final-fy20-appropriations-nasa: FY2020 funding no less than
  $511 million, up to $65 million for the coronagraph; Congress said "the mission should
  adhere to a $3.2 billion cost cap, which is at the bottom end of NASA's current cost
  estimates"; administration had proposed cancellation; baseline expected at confirmation
  review early 2020.
- https://www.aip.org/fyi/fyi-this-week/week-march-9-2020: NASA announced March 2, 2020
  that WFIRST passed its confirmation review (KDP-C), "committed to a development cost of
  $3.2 billion and a launch readiness date of October 2026", aiming a year earlier; the
  coronagraph "has a cost cap of $334 million that is not included in the $3.2 billion".
- https://www.aip.org/fyi/2021/final-fy21-appropriations-nasa: $505 million in FY2021,
  "on pace to launch in the mid-2020s", administration had again proposed cancellation.
- https://www.aip.org/fyi/2021/fy22-budget-request-nasa: "NASA set the mission's baseline
  development cost at $3.2 billion in February 2020, with an additional $334 million
  allocated for a coronagraph demonstration project"; Inspector General expected about $400
  million pandemic cost impact and a six-month delay; updated baseline due at CDR fall 2021.
- https://www.aip.org/fyi/2021/fy22-budget-outlook-nasa (the `source_url`): NASA "added
  $382 million to the telescope's total price tag and pushed the launch target from October
  2026 to May 2027"; "development of the telescope and coronagraph and the first five years
  of mission operations will together cost $4.3 billion"; Senate appropriators still cited a
  $3.2 billion development cap that excludes pandemic costs and the coronagraph.
- https://www.aip.org/fyi/2022/nasa-budget-fy22-outcomes-and-fy23-request: "the overall
  cost of the mission has increased by $400 million due to the pandemic and that its launch
  will be pushed from 2026 to 2027"; Congress directs a "firm" $3.5 billion cap on
  development costs; FY2022 about $500 million, FY2023 request $482 million.
- https://www.aip.org/fyi/2023/fy23-budget-outcomes-nasa: budget "decreasing as planned
  from $502 million to $482 million, with Congress continuing to cap the flagship mission's
  development cost at $3.5 billion"; 2027 target launch.
- https://www.aip.org/fyi/fy24-budget-outlook-nasa: FY2024 ramp-down $447 million to $407
  million, "target launch date in 2027".
- https://www.nationalacademies.org/read/26141/chapter/9 (Astro2020, chapter 7, section
  7.7.1): Astro2010 envisioned "a $1.6 billion, 1.5 m near-IR telescope"; "NASA has adopted
  a $3.5 billion cost ceiling for Roman"; CGI "significantly de-scoped"; KDP-C in 2020;
  "currently scheduled for a 2026 launch". Chapter 3 says launch expected 2026; chapter 4
  (as served) says 2025.
- https://arxiv.org/abs/2309.08672 (Roman CGI overview, Sept 2023; text from the PDF):
  "The launch date commitment is May 2027, with a current planned date of October 2026";
  commissioning phase launch + 3 months.
- https://arxiv.org/html/2608.17152 (Roman Coronagraph CPP target database, Aug 2026):
  "current launch readiness date of August 30th, 2026"; first coronagraph observations "as
  early as December 2026".
- https://arxiv.org/html/2602.21280 (all-sky survey with Roman, Feb 2026): "launch scheduled
  for Fall 2026"; Cycle 1 is 2027 to 2029 with commissioning, coronagraph demonstrations and
  the Core Community Surveys; nominal five-year mission.
- https://www.aip.org/news-and-analysis/aas/nasa-launches-nancy-grace-roman-space-telescope
  (dated 2026-08-30, a Sunday): Falcon Heavy from LC-39A "shortly after sunrise early
  Sunday". Short item; no cost or schedule history.
- /home/user/Trust-graph/sources/pan-trimble-2024.txt: Roman "Planned launch in 2027",
  Table 2.3 "Nancy Grace Roman Space Telescope (2027?)". Status text only.

Judgment: target 2020, launched 2026-08-30 (6.7 years late, which alone is `no`). Cost
2.7x nominal ($4.3B then-year life-cycle including coronagraph and five years of operations,
over $1.6B FY2010 appraisal). The bases differ in year-dollars and scope. The most
favorable like-for-like is the midterm's own: $2.6B to $2.8B FY2015 (2016 projection,
including coronagraph and GO) over $1.8B FY2015 (NWNH scope inflated) is 1.4x to 1.6x; the
development-only $3.5B cap over $1.6B is 2.2x. No source gives $4.3B in FY2010 dollars; I
did not compute one.

Not verified: whether the NWNH $1.6B included prime-mission operations (CATE was "phase A
costs onward"; footnote 17 says GO costs were excluded). The GAO cost history (gao.gov) and
NASA's own baseline documents (nasa.gov) were unreachable; the $3.934B figure sometimes
quoted for the 2020 life-cycle baseline was not found on a reachable host, so the row uses
the AIP-reported $3.2B development plus $334M coronagraph for 2020 and $4.3B for 2021.

## astro2010-lisa: building

Sources read:

- https://www.nationalacademies.org/read/23560/chapter/6 (2016 midterm): NWNH total $2.4B
  FY2010 with US share $1.5B at 50 percent. In 2011 the ESA/NASA co-equal partnership was
  dissolved; US re-costed concepts never came in under $1.2 billion; ESA selected the
  "Gravitational Universe" theme for L3 with launch in the 2030s, mission call late 2016,
  selection 2017, international contributions up to 20 percent. US LISA funding about $3
  million per year in FY2010 and FY2011, then about $300,000 per year, $1.3 million total
  FY2012 to FY2015. "NASA is currently authorized to plan for U.S. participation in an eLISA
  mission at the reduced cost of $150 million, which equates to a 10 percent stake." LISA
  Pathfinder launched November 2015, "3 years later than the launch date assumed by NWNH",
  science mode end of February 2016. Finding 4-9 and Recommendation 4-4.
- https://www.nationalacademies.org/read/26141/chapter/9 (Astro2020, section 7.7.3): "In
  2017, ESA accepted a proposal to develop a version of LISA with launch expected in 2034 or
  after"; "NASA currently plans to contribute an equivalent of $400 million in mission
  hardware by supplying the telescope, laser, and charge management systems as well as
  phasemeters and micro-thrusters."
- https://www.nationalacademies.org/read/26141/chapter/22 (Astro2020, Appendix L): "NASA is
  currently supporting a range of potential contributions to LISA, including instruments,
  spacecraft elements, and science analysis, in the medium-scale range of $400 million to
  $600 million"; planned launch 2034; recommended $100 million more over the decade for US
  science and a US LISA Science Facility.
- https://arxiv.org/abs/2402.07571 and the PDF (LISA Definition Study Report,
  ESA-SCI-DIR-RP-002, Feb 2024): Phase A 2018 to 2021, Phase B1 2021 to 2023, Mission
  Adoption Review end of 2023; launch-date trade figures span 2035; NASA Contributions and a
  NASA LISA Project Office appear in the organisation chart. No cost figures.
- https://arxiv.org/abs/2507.05130 (LISA summary for the European Strategy, July 2025):
  "adopted in January 2024", "scheduled for launch in the mid-2030's", collaboration of ESA,
  member states and NASA.
- https://arxiv.org/html/2608.31160v1 (Ad Astra white paper, 2026-08-31, the `source_url`):
  "ESA formally adopted the mission in January 2024 for a 2035 launch, and NASA's hardware
  contribution is now a formal project."
- /home/user/Trust-graph/sources/pan-trimble-2024.txt: "LISA Pathfinder in operation
  2015-17", "US Involvement in LISA ... Pathfinder successful, ESA and others".

Judgment: `building`. Target 2025 (NWNH assumed a 2016 new start for a mid-2020s launch);
current plan 2035, ten years late, so on schedule the bet will land at `no`. Cost is not
comparable: NWNH priced a 50 percent NASA share of a $2.4B mission; what exists is a junior
NASA contribution of $400M to $600M (then-year, Astro2020) to an ESA-led mission. US-share
ratio 0.27 to 0.4, but that is buying less, not spending less.

Not verified: the ESA cost at completion for LISA (esa.int blocked, no open copy found);
NASA's current (2024 to 2026) contribution figure, which AIP budget pages do not break out.

## astro2010-explorer: partial

Sources read:

- https://www.nationalacademies.org/read/23560/chapter/6 (2016 midterm): NWNH asked for 2
  MIDEX, 2 SMEX and 4 MoOs over 2012 to 2021 ($463M, FY2010, committee-generated); the
  midterm reads the intent as four augmentation missions on top of two baseline ones, six in
  total. First astrophysics AO September 2014 (one SMEX capped at $175M FY2015 plus one MoO
  capped at $65M); planned MIDEX AO FY2016, SMEX 2019, MIDEX 2021, each with a MoO. "NASA's
  implementation of the augmented Explorer program did not begin as early in the decade as
  originally planned." "Even if fully executed, however, the plan does not result in the
  full augmentation recommended by NWNH." Recommendation 4-3: at least four AOs. Chapter
  text also says Explorer support in the first half of the decade "has been minimal".
- https://www.nationalacademies.org/read/26141/chapter/8 (Astro2020, chapter 6, the
  `source_url`): "Astro2010 recommended increasing NASA's investment in Explorers from $40
  million to $100 million (FY 2010) annually ... NASA has largely achieved the recommended
  target"; conclusion that the augmentation "has resulted in an increased rate and a
  tremendous science output". SMEX cap $145M (FY2020), MIDEX $290M (FY2022).
- https://www.nationalacademies.org/read/26141/chapter/18 (Astro2020, Appendix H, Table
  H.1): AO (launch) years: NuSTAR 2003 (2012) SMEX; NICER 2011 (2017) MO; TESS 2011 (2018)
  MIDEX; IXPE 2014 (2021 plan) SMEX; GUSTO 2014 (2021 plan) MO; SPHEREx 2016 (2023) MIDEX;
  ARIEL/CASE 2016 (2028) MO; ESCAPE or COSI 2019 (2025) SMEX; Dorado or LEAP 2019 (TBD) MO;
  MIDEX and MO to be selected from the 2021 AO (2028). NASA plans a cadence of two MIDEX,
  two SMEX and four MOs per decade.
- https://www.aip.org/fyi/2021/fy22-budget-outlook-nasa: FY2022 request $300 million for
  the Explorer program, House $278 million, "a $73 million increase over the current
  budget".
- https://www.aip.org/fyi/2016/decadal-survey-midterm-assessment-highlights-dilemmas-game-changing-astronomy:
  "NASA, it notes, has implemented fewer Explorers projects than recommended".
- /home/user/Trust-graph/sources/pan-trimble-2024.txt: "Imaging X-ray Polarimetry Explorer
  (SMEX-14) 2021, others planned".

Judgment: `partial`. By 2021 the annual funding target was reached and four AOs produced the
2+2+4 count, but the first AO came in 2014 instead of 2012, half the selections launch after
the decade (2023 to 2028), and the midterm judged the plan short of the full augmentation.

Not verified: a delivered-dollar total for astrophysics Explorers over 2012 to 2021 (the
NASA budget pages are blocked); whether the $300M FY2022 line is astrophysics-only (AIP
describes it as the Explorer program within NASA astrophysics).

## astro2010-new-worlds-tech: yes (guess)

Sources read:

- https://www.nationalacademies.org/read/23560/chapter/6 (2016 midterm, the `source_url`):
  NWNH $100M to $200M (FY2010). "The total cost of exoplanet-related precursor science and
  technology development, including technology development for the WFIRST coronagraph,
  significantly exceeds the $100 million to $200 million envisioned by NWNH." Finding 4-11:
  planned decadal investment "exceeds the level envisioned in NWNH". Finding 4-4: coronagraph
  "currently estimated $350 million" (FY2015, inside the WFIRST cost) is justifiable, but
  much beyond that "would significantly distort the science priorities". SAT program
  funding "over the first half of the decade has exceeded $64 million" across all areas, with
  coronagraph technology funded within the WFIRST commitment.
- https://www.aip.org/fyi/fyi-this-week/week-march-9-2020: coronagraph cost cap $334
  million, outside the $3.2 billion development commitment; "drop dead" completion mid-2023.
- https://www.nationalacademies.org/read/26141/chapter/9 (Astro2020, 7.7.1): CGI added as a
  technology demonstration and "significantly de-scoped" to hold the $3.5 billion ceiling.
- https://www.nationalacademies.org/read/26141/chapter/19 (Astro2020, Appendix I): neither
  JWST, Roman nor the ELTs will have coronagraphs with adequate contrast for exo-Earths;
  coronagraphic missions "require a significant technology investment, probably as large as
  $600 million ($FY 2020) by the start of phase A"; Roman coronagraph demonstrations at
  about 1e-9 contrast; some subsystems still at TRL 3.
- https://www.nationalacademies.org/read/26141/chapter/8 (Astro2020, chapter 6): SAT was
  "initiated in response to a recommendation from" Astro2010, first selections 2012.
- https://arxiv.org/html/2608.17152: first Roman coronagraph observations as early as
  December 2026 after the 2026-08-30 launch readiness date.

Judgment: `yes` on the program line: delivered funding exceeded the recommended range (the
coronagraph alone is 1.7x to 3.3x the range, before SAT and starshade work) and the program
ran on NWNH's timeline with the technology demonstration now in orbit. Confidence `guess`
because no source sums the decade's exoplanet technology spending and the stated goal (a
direct-imaging mission ready for a 2020-decade start) was not met; Astro2020 moved that
mission to the 2040s via GOMAP.

Not verified: total NASA exoplanet technology and starshade spending 2010 to 2020; final
Roman CGI cost against its $334M cap (nasa.gov and gao.gov blocked).

## astro2010-inflation-probe-tech: yes (guess)

Sources read:

- https://www.nationalacademies.org/read/23560/chapter/6 (2016 midterm, the `source_url`):
  NWNH asked for a modest APRA augmentation for CMB technology and a technology program
  "contingent on having made a positive B-mode detection", $60M (range $60M to $200M,
  FY2010). "While this has not occurred", Planck, ACTpol, SPTpol, BICEP2/Keck and POLARBEAR
  results are consistent; ground efforts target r about 0.01; NASA supports long-duration
  balloon flights; LiteBIRD selected as an Explorer MoO Phase A study from the 2014 AO with
  downselect summer 2016; CMB-S4 highly ranked by P5. Finding 4-12: program "well aligned
  with the recommendations of NWNH, with NASA, NSF, and DOE supporting technology
  development and precursor science". Suborbital program "boosted by $7 million per year
  over FY2011-2012 to a total of $32 million per year in FY2013-2015, broadly in line with
  the $15 million per year augmentation recommended in NWNH". SAT total over the first half
  of the decade exceeded $64 million (all areas, CMB among them).
- https://www.nationalacademies.org/read/26141/chapter/18 (Astro2020, Table H.1): the 2014
  MoO selection was GUSTO, so the US LiteBIRD MoO was not selected.
- https://www.nationalacademies.org/read/26141/chapter/9 (Astro2020, chapter 7): "With
  investment in technologies this decade, combined with ground measurements, a CMB probe
  mission could potentially be a compelling candidate for the future probe call in the
  2030s, complementing the survey's ground-based CMB-S4 recommendation." Appendix J lists
  PICO among probe concepts.

Judgment: `yes` on the program line: the conditional $60M to $200M was never due because the
trigger (a mid-decade B-mode detection) never happened, and the unconditional part (modest
CMB technology and balloon support) was delivered on schedule per the midterm. Confidence
`guess` because no source states the dollars spent on CMB technology under this line; the
suborbital and SAT figures are proxies.

Not verified: NASA's CMB technology spending by year; whether NASA later joined LiteBIRD in
any form (nasa.gov blocked, and neither Academies report says so).

## Open gaps across the five rows

1. LISA total mission cost (ESA cost at completion) and NASA's current contribution figure.
2. Roman: an inflation-adjusted comparison of the $4.3B life-cycle figure to the NWNH
   $1.6B FY2010 appraisal; whether NWNH's figure included prime operations.
3. Explorer: a delivered-dollar total for 2012 to 2021.
4. Both technology lines: actual NASA spending totals; the rows rest on the midterm's
   qualitative findings and the coronagraph cap.
