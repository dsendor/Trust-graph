# Notes: P5 2014 cost-schedule outcomes, neutrino bets

Companion to `p5-2014-cost-schedule-neutrino.csv`. Written 2026-10-01. One section per
bet: every URL read, what it said, and what could not be verified.

Method: for DOE projects, cost at ranking is the earliest agency baseline after the May
2014 P5 report (CD-1 cost range, or CD-2 TPC if that came first), cost latest is the TPC
in the newest budget justification. All DOE figures are the DOE share in then-year
dollars and exclude international in-kind contributions. The DOE Office of Science HEP
congressional budget justifications FY2016 to FY2027 were downloaded once and
text-extracted with pdftotext into the session scratchpad as `cbj-FY20xx-HEP.txt` (or
`cbj-FY20xx-SC-Vol4.txt` for years where only the full Science volume was found). pypdf
could not be installed (no PyPI route), so pdftotext was used instead.

Budget justification URLs read (all www.energy.gov, all opened and grepped):

| FY | URL |
|---|---|
| 2016 | https://www.energy.gov/sites/default/files/2015/02/f19/FY2016BudgetVolume4_5.pdf |
| 2017 | https://www.energy.gov/sites/prod/files/2016/02/f29/FY2017BudgetVolume%204.pdf |
| 2018 | https://www.energy.gov/sites/prod/files/2017/05/f34/FY2018BudgetVolume4_1.pdf |
| 2020 | https://www.energy.gov/sites/prod/files/2019/05/f62/fy-2020-doe-sc-hep-congressional-budget-request.pdf |
| 2021 | https://www.energy.gov/sites/default/files/2020/06/f75/fy-2021-doe-congressional-budget-justification.pdf |
| 2022 | https://www.energy.gov/sites/default/files/2021-06/05%20HEP%20Program%20Narrative%206_16_21.pdf |
| 2023 | https://www.energy.gov/sites/default/files/2022-04/FY2023-PresidentsRequest-HEP-Final-2.pdf |
| 2024 | https://www.energy.gov/sites/default/files/2023-03/FY2024-PresidentsRequest-HEP.pdf |
| 2025 | https://www.energy.gov/documents/fy-2025-high-energy-physics-budget-request |
| 2026 | https://www.energy.gov/sites/default/files/2025-07/FY2026-PresidentsRequest-HEP.pdf |
| 2027 | https://www.energy.gov/documents/fy-2027-high-energy-physics-budget-request |

FY2019 was not fetched (the FY2020 CBJ reprints the FY2019 milestone row).

## p5-2014-lbnf (LBNF/DUNE-US, DOE line item 11-SC-40)

Cost history, DOE share, then-year dollars, foreign contributions excluded:

| Date | Event | Range ($M) | Point ($M) | CD-4 | Source |
|---|---|---|---|---|---|
| 2012-12-10 | CD-1 (pre-P5 LBNE) | 805 to 1,110 | 873 | FY2025, then FY2027 | FY2016 CBJ |
| 2015-11-05 | CD-1R refresh (post-P5, international, underground) | 1,260 to 1,860 | 1,500 | FY2030 | FY2017 CBJ |
| 2016-09-01 | CD-3A | same | 1,536 (FY2018 CBJ) | 4Q FY2030 | FY2018 CBJ |
| 2019-01 | IPR | same | 1,850 | 4Q FY2030 | FY2020 CBJ |
| FY2019 analysis | 40 percent above range top | same | 2,600 | 4Q FY2033 | FY2021 CBJ |
| FY2020 analysis | | same | 2,600 | early FY2034 | FY2022 CBJ |
| 2022 | over 50 percent above range top | same | about 3,000 | | FY2023 CBJ |
| 2023-02-16 | CD-1RR | 3,160 to 3,677 | 3,277 | 4Q FY2035 (FY2025 CBJ) | FY2024 CBJ |
| 2025, 2026 | unchanged | 3,160 to 3,677 | 3,277 | 1Q FY2035 | FY2026, FY2027 CBJ |

FY2027 CBJ "Project Cost History": TEC 3,169,955 plus OPC 107,045 equals TPC 3,277,000
(thousands), for both FY2026 and FY2027 columns. Subproject CD-4s in the FY2027 CBJ:
FSCF-EXC 1Q FY2027, FSCF-BSI 4Q FY2028, FDC 2Q FY2034, NSCF+B 2Q FY2034, ND 1Q FY2035.

FY2023 CBJ: in-kind contributions from international partners to the facility valued at
about $260M and to the experiment about $400M, "the cost if DOE would supply the
components". FY2017 CBJ: DOE contributes less than a third of the DUNE detectors; CERN
cryostat worth $90M. FY2024 CBJ: Inflation Reduction Act gave $125M, TPC unchanged.

- https://www.aip.org/fyi/2020/flagship-neutrino-project-working-keep-costs-within-cap
  (2020-06-19): CD-1 range $1.26B to $1.86B; cost "had risen 40% over the previous year to
  $2.6 billion"; cap of 50 percent over the top of the range; "apt to rise by an
  additional $300 million" without more partner commitments; LBNF goal of 25 percent
  partner contribution. No first-beam date.
- https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment/
  (2026-05-07): "Fermilab's priority is to deliver the first neutrino beam to DUNE by
  2031." CERN in-kind 10 million pounds of steel. No cost.
- https://news.fnal.gov/2026/07/fermilab-marks-70-years-of-neutrino-science-and-leads-next-generation-experiment/
  (2026-07-07): "Fermilab's top institutional priority is delivering a neutrino beam to
  DUNE at LBNF by 2031." No cost.

Handoff check: the $2.6B (2020) figure is confirmed by both the FY2021 CBJ and AIP FYI.
The "$3.1 to 3.3B 2021 to 2024" figure resolves to: about $3.0B in the FY2023 CBJ
(March 2022), then the CD-1RR point of $3.277B in a $3.16B to $3.677B range from February
2023, carried unchanged into the FY2026 and FY2027 CBJs. Nothing reachable gives an
aggregate of the baselined subproject TPCs.

Not verified: a far-detector first-data date. A search snippet said "DUNE is expected to
begin collecting data in 2029" but no opened page stated it, so the row uses 2031 first
beam only.

## p5-2014-pip-ii (PIP-II, DOE line item 18-SC-42)

| Date | Event | Range ($M) | Point or TPC ($M) | CD-4 | Source |
|---|---|---|---|---|---|
| 2015-11-12 | CD-0 | none stated | | | FY2020 CBJ |
| 2018-07-23 | CD-1 | 653 to 928 | 721 | 1Q FY2030 | FY2020 CBJ |
| FY2019 design | | same | 888 | | FY2021 CBJ |
| 2020-07-17 | ECF subproject CD-2/3 | | 36 (within PIP-II) | | FY2022 CBJ |
| 2020-12-14 | CD-2 | | 978 | FY2033 | FY2022 CBJ |
| 2021-03-16 | CD-3A | | 978 | | FY2022 CBJ |
| 2022-04-18 | CD-3 | | 978 | 1Q FY2033 | FY2024 CBJ |
| 2025, 2026 | unchanged | | 978 | 1Q FY2033 | FY2026, FY2027 CBJ |

FY2022 CBJ: CD-4 "delayed by three years to FY 2033" due to in-kind delivery schedules.
FY2024 to FY2027 CBJs: international in-kind $330M at DOE-equivalent cost, not in the
TPC. FY2025 CBJ: May 2023 construction accident stopped civil work until December 2023,
consumed contingency (the CBJ text says "$2,000,000,000 of cost contingency", an evident
typo for $2M). FY2026 CBJ: significant contingency use through 3Q FY2024 for civil
costs, the accident, overhead rates, in-kind delays and arc-flash redesign. FY2027 CBJ:
cost history TEC 891,200 plus OPC 86,800 equals 978,000 (thousands).

- https://news.fnal.gov/2026/07/fermilab-installs-first-beamline-component-for-new-state-of-the-art-accelerator/
  (2026-07-09): RFQ installed; interfacing through 2026; "In 2027, they will start to
  apply power to the RFQ to prepare for the first parts of beam commissioning." No cost.
- https://arxiv.org/pdf/2311.05456 (Nov 2023): "The scheduled completion date for the
  early finish of the PIP-II Project is April 2029."
- https://arxiv.org/pdf/2606.25159 (2026): PIP-II began construction of Linac2 in 2023;
  "In 2028, the user program will turn off for two years to connect the Linac2 to the
  Booster"; the LBNF beamline connection to the Main Injector is planned in the same
  window.
- https://arxiv.org/pdf/2609.17155 (Sept 2026): Booster tunnel work scheduled to start
  fall 2026; operational readiness and completion of (front-end) commissioning planned
  spring 2027.
- https://news.fnal.gov/2023/01/construction-contract-awarded-for-particle-accelerator-complex-at-fermilab/
  (2023-01-10): 39-month civil construction from January 2023. No cost.

bets.csv has no target date for PIP-II. The P5 promise was ">1 MW by the time of first
operation of the new long-baseline neutrino facility", so the comparison is against LBNF
first beam, 2031.

## p5-2014-sbn (Short-Baseline Neutrino program)

No DOE total project cost exists. Grep of every CBJ FY2016 to FY2027 for SBN, SBND,
ICARUS and MicroBooNE finds only narrative text and two GPP items: FY2017 CBJ GPP table,
"Short Baseline Neutrino Far Hall" TEC 9,800 and "Short Baseline Neutrino Near Hall" TEC
5,350 (thousands; the FY2018 CBJ revises them to 8,700 and 5,250). Funding statements:
"Funding for the SBN program supports subsystems integration and infrastructure needed
for the program" (FY2017 CBJ).

- https://arxiv.org/pdf/1503.01520 (SBN proposal, March 2015): high-level milestones put
  installation of both near and far detectors in 2017 and the three-detector configuration
  "ready for beam data-taking in the spring of 2018"; funding "expected from a combination
  of US DOE, US NSF, and international in-kind contributions"; ICARUS overhaul and
  transport "a major contribution of INFN and of CERN"; commitments from CERN, INFN and
  UK-STFC; CH-NSF sought. States that LAr1 "was not encouraged by P5, however, due to the
  high cost of a new detector of this scale." No dollar totals.
- https://news.fnal.gov/2015/10/microboone-sees-first-accelerator-born-neutrinos-2/
  (2015-10-30): beam delivered from 2015-10-15, first neutrinos seen. No cost.
- https://news.fnal.gov/2018/06/big-boost-for-fermilabs-short-baseline-neutrino-experiments/
  (2018-06-05): ICARUS "should start taking data in about a year", SBND "operational in
  2020"; DOE and NSF funded. No cost.
- https://www.energy.gov/node/3564761 (2018-06-29): US-Italy SBN agreement; SBN "started
  in 2015". No cost.
- https://news.fnal.gov/2021/05/icarus-gets-ready-to-fly/ (2021-05-20): filled early 2020,
  activated August 2020, "official first data collection run in fall 2021"; DOE, INFN,
  CERN support. No cost.
- https://news.fnal.gov/2021/09/scientists-assemble-final-detector-of-fermilabs-short-baseline-neutrino-program/
  (2021-09): SBND "data debut in early 2023"; ICARUS physics run fall 2021. No cost.
- https://news.fnal.gov/2024/09/first-neutrinos-detected-at-fermilab-short-baseline-detector/
  (2024-09-10): first neutrinos; 250 people, 38 institutions. No cost.
- https://arxiv.org/abs/2504.00245 (2025-03-31): "SBND began operation in July 2024" and
  "started collecting stable neutrino beam data in December 2024". No cost.

Not verified: any dollar cost for SBND, ICARUS relocation, or the program. Hosts that
might hold it (sbn.fnal.gov, lss.fnal.gov, osti.gov) are blocked.

## p5-2014-lar1

LAr1 was never built. The SBN proposal (above) records that P5 did not encourage it on
cost. Scored on SBND, which grew out of LAr1-ND.

- https://arxiv.org/pdf/1309.7987 (LAr1-ND white paper, September 2013): "relatively
  modest cost", "built quickly", "definitive result within one year", data run
  "concurrent with the final year of MicroBooNE data taking". No dollar figure.
- SBND dates and the spring 2018 plan: same sources as the SBN section.

The 2012 LAr1 letter of intent (cited as ref. 8 in the SBN proposal) was not found on a
reachable host, so the LAr1 cost at ranking is blank. Result "no" uses the spring 2018
proposal plan as the earliest post-ranking schedule; against the P5 SBN window (2015 to
2020) it would read partial. Flag for David if he prefers the window.

## p5-2014-chips

- https://arxiv.org/pdf/1307.5918 (CHIPS LoI, July 2013): 100 kt fiducial goal in the
  Wentworth pit; fast track "building a 10 kton detector two years after NOvA starts
  data taking and increasing this to 20, 50 and 100 kton every subsequent two years";
  slow track 10 kt four years after NOvA turn-on. Component costs per PMT channel are
  tabulated (12 inch HQE PMT $1,800 etc.) but no project total; the stated aim is to cut
  the cost per kt of water Cherenkov detectors.
- https://arxiv.org/abs/2401.11728 and the PDF (January 2024): "the total cost of the
  hardware components for the prototype was estimated to be 1.7m euro which could have
  equipped 15 kt if the detector had been expanded fully"; Hyper-K comparison $2.3M per
  kt; "assembled and deployed from April to October 2019"; liner damaged during towing
  before water ingress; Covid halted site access March 2020; "did not observe Numi
  neutrinos"; "decommissioned in July 2020". Acknowledgements: Fermilab, Leverhulme
  Trust, US DOE, Royal Society, ERC CHROMIUM.

A search snippet gave a CHIPS cost target of "$200k per kt" and NSF support; neither
appears in the two opened papers, so they are not in the row.

## p5-2014-pingu (scored on the IceCube Upgrade)

- https://arxiv.org/pdf/1401.2046v1 (PINGU LoI v1, 2014-01-09, 40 strings by 96 DOMs):
  "estimated total US cost for PINGU, including contingency, ranges from $55M to $80M for
  the experiment as part of a larger MREFC project or as a standalone project,
  respectively. The assumed foreign contribution is $25M in both cases." Table 8: US cost
  without contingency $59.9M standalone, $39.8M within a larger upgrade; Table 9 grand
  total $104.3M with contingency before foreign contributions. "We anticipate a potential
  completion date for the PINGU detector in the 2019/20 austral summer season."
- https://arxiv.org/pdf/1401.2046 (v2, 2017-09-05, 26 strings by 192 modules): Section 9
  cost table, $39M (20 strings) to $47M (26 strings) without contingency; about five
  project years, two deployment seasons.
- https://arxiv.org/pdf/1310.1287 (October 2013): "relatively modest cost", no number
  (the search snippet's "below US$100M" was not found in this text).
- https://arxiv.org/pdf/1908.09441 (August 2019, Upgrade design): "The IceCube Upgrade,
  which will be constructed in the 2022/23 Antarctic Summer season"; seven strings.
- https://www.aip.org/fyi/2022/nsf-budget-fy22-outcomes-and-fy23-request: "Crew size
  limitations have resulted in a delay of at least three years to a planned upgrade to the
  IceCube neutrino observatory at the South Pole."
- https://arxiv.org/pdf/2509.13066 (September 2025): seven strings to be deployed in the
  2025 to 2026 austral summer; "This fully funded IceCube Upgrade extension is distinct
  from the previously proposed PINGU extension."
- https://arxiv.org/abs/2609.24387 and PDF (2026-09-21): "In the austral summer of
  2025/2026, five new strings have been added"; "The 5 commissioned strings work well and
  are expected to start taking science data with the rest of the detector in fall 2026."
- https://arxiv.org/pdf/2608.28395 (2026-08-28): full integration of new modules "by the
  end of 2026".

Not verified (search snippets only, hosts blocked): 2019 NSF mid-scale award of $23M
toward a $37M Upgrade with more than $3M each from Germany, Japan and MSU
(wipac.wisc.edu, eurekalert.org, nbi.ku.dk all refused); "$55 million IceCube Upgrade
... NSF contributing about 70% of the funds" (physicstoday.aip.org, refused); NSF
FY2025 budget facility page (nsf-gov-resources.nsf.gov, refused). The handoff's "NSF
share about 70 percent" therefore still rests on a snippet; the 2019 figures imply 62
percent, the 2026 Physics Today snippet says about 70 percent of a larger total. No
arXiv paper found via the arXiv API states the Upgrade cost.

## p5-2014-mice

- https://arxiv.org/pdf/1312.1626 (December 2013): Step IV "results expected starting in
  2015"; the full Step VI sustainable-cooling demonstration to complete "about 2020".
- https://arxiv.org/pdf/1805.07128 (May 2018): "Data were taken in 2016 and 2017 in the
  Step IV configuration"; "MICE data taking was concluded in December 2017"; funding
  acknowledgement names DOE, NSF and others (STFC in the full list).
- https://arxiv.org/abs/1907.08562 (2019-07-19, Nature 2020 preprint, RAL-P-2019-003):
  first demonstration of ionization cooling. No cost.
- https://news.fnal.gov/2020/02/mice-experiment-demonstrates-key-technique-for-future-muon-colliders/
  (2020-02-05): Nature publication 2020-02-05; "support of the UK Science and Technology
  Facilities Council, Fermilab, the U.S. Department of Energy's Office of Science and
  the National Science Foundation". No cost, no mention of descoping.

Not verified: any cost figure. The November 2014 rebaseline to Step IV appears only in a
search snippet (lss.fnal.gov conference paper, host blocked) and is consistent with the
2018 paper's statement that data taking ended in the Step IV configuration. STFC pages
(ppd.stfc.ac.uk) and iit.edu were refused.

## Gaps across all seven

1. No DOE TPC exists for SBN, SBND or ICARUS in any CBJ; the cost half of those rows is
   blank.
2. IceCube Upgrade cost and NSF share rest on snippets of blocked hosts.
3. MICE has no cost figure on any reachable host.
4. LAr1's 2012 LoI (with whatever cost it stated) was not found.
5. A DUNE far-detector first-data date (2029 in a snippet) was not confirmed on an opened
   page; 2031 first beam is the sourced date.
