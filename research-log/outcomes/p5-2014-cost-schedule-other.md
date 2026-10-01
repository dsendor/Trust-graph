# Notes: P5 2014 cost-schedule outcomes (Mu2e, Muon g-2, HL-LHC, LHC Phase-1, DESI, LSST, DM G2)

Written 2026-10-01. Companion to `p5-2014-cost-schedule-other.csv`. P5 2014 gives only size
bands, so "cost at ranking" is the earliest DOE baseline after May 2014 (CD-2 TPC where it
exists, else the CD-1 or CD-0 cost range), per `docs/handoff.md`. All costs are then-year
dollars, DOE share only (TPC = TEC plus OPC). CERN, NSF and foreign in-kind are excluded.

## Sources read (all on allowed hosts unless noted)

DOE Office of Science budget justifications (HEP chapter), extracted with pdftotext. The
other agent's copies are in the scratchpad as `cbj-FY20xx-*.txt`; pypdf would not install
(no package index) so `pdftotext -layout` was used instead.

| FY | URL | Used for |
|---|---|---|
| 2016 | https://www.energy.gov/sites/prod/files/2015/02/f19/FY2016BudgetVolume4_5.pdf | Mu2e CPDS (CD-1 range $200M to $310M of 2012-07-11, TPC growth $233.577M to $273.677M, CD-4 1Q FY2023); MIE footnotes: Phase-1 ATLAS CD-2/3 2014-11-12 TPC $33.25M, CMS $33.217M; g-2 CD-1 2013-12-19 range $43.0M to $50.1M; LSSTcam CD-2 2015-01-07 TPC $168M, completion FY2022; DESI CD-0 2012-09-12 range $25M to $42M; ADMX-G2 "small-scale" |
| 2017 | https://www.energy.gov/sites/prod/files/2016/02/f29/FY2017BudgetVolume%204.pdf | Mu2e CD-2 and CD-3B approved 2015-03-04, TPC $273.677M, CD-4 1Q FY2023; g-2 CD-2/3 2015-08-20 TPC $46.4M, CD-4 FY2019; DESI CD-2 2015-09-17 TPC $56.328M, completion FY2021; LZ CD-1/3A 2015-04-24 range $46M to $59M; SuperCDMS CD-1 2015-12-21 range $16M to $21.5M; ADMX-G2 fabrication completed FY2016 |
| 2018 | https://www.energy.gov/sites/prod/files/2017/05/f34/FY2018BudgetVolume4_1.pdf | HL-LHC AUP CD-0 2016-04-13 range $180M to $250M; LZ CD-2/3B 2016-08-08 TPC $55.5M, completion FY2022, CD-3 2017-02; DESI CD-3 2016-06-22; Phase-1 ATLAS CD-4 FY2019 |
| 2019 | https://www.energy.gov/sites/prod/files/2018/03/f49/DOE-FY2019-Budget-Volume-4_0.pdf | g-2 CD-4 approved 2018-01-16, TPC $46.4M; AUP CD-1/3A 2017-10-13 range $208.6M to $252.4M; HL-LHC ATLAS and CMS CD-0 2016-04-13 range $125M to $155M each; Phase-1 ATLAS CD-4 FY2019, CMS CD-4 FY2020, CMS pixel already installed |
| 2020 | https://www.energy.gov/sites/prod/files/2019/05/f62/fy-2020-doe-sc-hep-congressional-budget-request.pdf | AUP CD-2/3B 2019-02-11 TPC $242.72M; HL-LHC ATLAS CD-1 2018-09-21 range $149M to $181M; SuperCDMS CD-2/3 2018-05-02 TPC $18.6M; LSSTcam, DESI, LZ unchanged |
| 2021 | https://www.energy.gov/sites/default/files/2020/06/f75/fy-2021-doe-congressional-budget-justification.pdf | HL-LHC CMS CD-1 2019-12-19 range $144.1M to $183M; DESI and LZ "CD-4 expected FY2020"; SuperCDMS CD-4 end FY2021 |
| 2022 | https://www.energy.gov/sites/default/files/2021-06/05%20HEP%20Program%20Narrative%206_16_21.pdf | DESI commissioning complete 2020-03, project completion approved 2020-05, survey start 2021-05; Mu2e BCP in process, $2M FY2021 and $13M FY2022 held; AUP CD-3 2020-12-21 |
| 2023 | https://www.energy.gov/sites/default/files/2022-04/FY2023-PresidentsRequest-HEP.pdf | DESI survey started 2021-05; LSSTcam MIE construction phase completed 2021; LZ science ops 2021-12; SuperCDMS "full science operations late 2023" (slipped) |
| 2024 | https://www.energy.gov/sites/default/files/2023-03/FY2024-PresidentsRequest-HEP.pdf | Mu2e BCP approved 2022-12-21, +$42.023M, TPC $315.7M, CD-4 2028-01; AUP rebaseline review 2022-12, new TEC $259.952M, $38.355M IRA; HL-LHC ATLAS CD-2/3 2023-01-31 TPC $200M; CMS $200M proposed; LZ science ops 2021-12; SuperCDMS "starts science operations with full detector suite FY2024" (slipped again) |
| 2025 | https://www.energy.gov/sites/default/files/2024-03/FY2025-PresidentsRequest-HEP-1.pdf | AUP new TEC approved 2023-03-20; HL-LHC CMS CD-2/3C 2023-04-04 TPC $200M; AUP final funding FY2023 |
| 2026 | https://www.energy.gov/sites/default/files/2025-07/FY2026-PresidentsRequest-HEP.pdf | HL-LHC ATLAS and CMS unchanged at $200M; AUP no longer described |
| 2027 | https://www.energy.gov/documents/fy-2027-high-energy-physics-budget-request | Rubin LSST survey began FY2026, first images 2025-06; HL-LHC ATLAS ($5.0M) and CMS ($6.812M) final year of TEC funding |

DOE Project Management Performance Metrics reports (quarterly, energy.gov; list CD-2 TPC,
latest TPC, status, FY completed for projects over $50M and some smaller legacy ones):

| Report | URL | Rows |
|---|---|---|
| FY2020 Q2 | https://www.energy.gov/sites/default/files/2020/05/f74/FY%202020%20Q2%20Project%20Management%20Performance%20Metrics%20Report.pdf | Muon g-2: CD-2 TPC $46.4M, latest $46.205M, completed and closed FY2018; LZ active, FY2020 planned |
| FY2021 Q1 | https://www.energy.gov/sites/default/files/2022-02/FY2021%20Q1%20Project%20Management%20Performance%20Metrics%20Report.pdf | LZ completed FY2020, latest TPC $53.59M; DESI closed; LSST Camera active, FY2021 planned |
| FY2021 Q3 | https://www.energy.gov/sites/default/files/2022-02/FY2021%20Q3%20Project%20Management%20Performance%20Metrics%20Report.pdf | DESI: CD-2 TPC $56.328M, latest $54.418M, completed and closed FY2020; LZ $53.59M completed FY2020; HL-LHC AUP CD-3 $242.72M |
| FY2021 Q4 | https://www.energy.gov/sites/default/files/2022-02/FY2021%20Q4%20Project%20Management%20Performance%20Metrics%20Report.pdf | Same; LSST Camera still active |
| FY2022 Q1 | https://www.energy.gov/sites/default/files/2022-02/FY2022%20Q1%20Project%20Management%20Performance%20Metrics%20Report.pdf | LSST Camera: CD-2 TPC $168M, latest $165.28M, completed and closed FY2021; LZ latest TPC shown as $55.5M again (the $53.59M in FY2021 reports is the earlier figure; both are at or under baseline) |
| FY2022 Q2 to FY2026 Q2 | https://www.energy.gov/documents/fy20xx-qN-project-management-performance-metrics-report | LSST Camera $165.28M through FY2023 Q4, then drops off; no SuperCDMS, Phase-1 or AUP CD-4 rows (under the $50M listing threshold or not yet complete) |

Other allowed-host sources:

- https://news.fnal.gov/2017/05/muon-magnets-moment-arrived/ : first muon beam into the g-2 ring 2017-05-31.
- https://news.fnal.gov/2018/02/fermilabs-muon-g-2-experiment-officially-starts-up/ : CD-4 granted Jan 16 (2018); "on schedule and under budget" (Polly); physics data from March 2018.
- https://arxiv.org/abs/2506.03069 : g-2 final result, data 2020 to 2023 combined with earlier runs, 127 ppb, submitted 2025-06-03.
- https://arxiv.org/html/2609.25943 : Mu2e "in detector installation and commissioning, with Run I expected to begin in the second half of 2027"; slow-extraction commissioning runs 2025 and early 2026.
- https://arxiv.org/abs/2606.25140 : first full-scale slow-extraction commissioning run during the 2025 run, second in early 2026.
- https://news.fnal.gov/2026/02/mu2e-reaches-major-milestone-with-tracker-move/ : tracker moved into Mu2e hall 2025-11; no dates for beam.
- https://news.fnal.gov/2021/02/hl-lhc-accelerator-upgrade-project-receives-approval-to-move-full-speed-ahead-from-department-of-energy/ : CD-3 Feb 2021 (CBJ: 2020-12-21); US delivers 16 magnets and 8 cavities, installation 2025 to early 2027, HL-LHC start 2027 (as of 2021).
- https://news.fnal.gov/2026/02/hilumi-lhc-full-scale-tests-start/ : LS3 starts summer 2026, HL-LHC "set to enter operation in 2030", Fermilab delivers five more cryoassemblies by mid-2027.
- https://news.fnal.gov/2019/02/large-hadron-collider-upgrade-project-leaps-forward/ : AUP CD-2/3b 2019-02-11; no cost.
- https://www.aip.org/fyi/2022/doe-projects-putting-inflation-reduction-act-funds-work : IRA $35M to Mu2e, $106M to LHC upgrades.
- https://news.fnal.gov/2022/07/berkeley-lab-researchers-record-successful-startup-of-lux-zeplin-dark-matter-detector-at-sanford-underground-research-facility/ : LZ first results 2022-07-07 from 60 live days starting end of December (2021).
- https://news.fnal.gov/tag/lux-zeplin/ : lists the 2020-10-27 Symmetry piece "DOE officials have formally signed off on project completion for LUX-ZEPLIN" (Symmetry itself is blocked).
- https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway/ : SuperCDMS installation (bar shielding) completed 2025, cooldown fall 2025, "Science-quality data taking is on schedule to start in mid-2026"; funders DOE, NSF, CFI, NSERC.
- https://arxiv.org/html/2507.11368v3 : SuperCDMS "first full science run expected to begin in early 2026", operate through at least 2028, initial payload about 30 kg in 4 towers.
- https://arxiv.org/abs/2312.16668 : ADMX Run 1A data January to June 2017.
- https://news.fnal.gov/2026/04/desi-completes-planned-3d-map-of-the-universe-and-continues-exploring/ : DESI data from May 2021, planned five-year survey finished ahead of schedule, release 2026-04-17.
- https://news.fnal.gov/2026/06/action-nsf-doe-vera-c-rubin-observatory-begins-capturing-the-greatest-cosmic-movie-ever-made/ : LSST survey officially started 2026-06-30, First Look June 2025.

## Per bet

### p5-2014-mu2e (building)
- CD-1 2012-07-11, range $200M to $310M (predates ranking). TPC grew to $273.677M during
  preliminary design (FY2016 CBJ). CD-2 and CD-3B 2015-03-04, TPC $273.677M, CD-4 1Q FY2023
  (FY2017 CBJ). CD-3 2016-07-14.
- BCP approved 2022-12-21: +$42.023M, TPC $315.7M, CD-4 January 2028 (FY2024 CBJ). Ratio
  315.7/273.677 = 1.154. IRA provided $35M (AIP) and FY2023 enacted finished the funding.
- First beam: slow-extraction commissioning runs in 2025 and early 2026 (arXiv:2606.25140).
  Run I physics expected 2H 2027 (arXiv:2609.25943). Not final, so `building`.
- Not verified: actual final cost at CD-4 (not before 2028).

### p5-2014-muon-g-2 (yes)
- CD-1 2013-12-19, range $43.0M to $50.1M (predates ranking). CD-2/3 2015-08-20, TPC $46.4M,
  CD-4 FY2019 (FY2017 CBJ). Earliest post-ranking baseline is the CD-2/3 TPC.
- CD-4 2018-01-16 (FY2019 CBJ footnote; Fermilab news). Final cost $46.205M (PM metrics
  FY2020 Q2). Ratio 0.996.
- First beam 2017-05-31 (Fermilab news). Run-1 physics March to July 2018. Data ended 2023;
  final result 2025-06-03 (arXiv:2506.03069). P5 target_date blank, so the FY2019 baseline
  CD-4 is the comparator: a year early.

### p5-2014-hl-lhc (building)
- Scored on the DOE projects only. AUP: CD-0 2016-04-13 range $180M to $250M (FY2018 CBJ);
  CD-1/3A 2017-10-13 range $208.6M to $252.4M (FY2019 CBJ); CD-2/3B 2019-02-11 TPC $242.72M
  (FY2020 CBJ); CD-3 2020-12-21; rebaseline review 2022-12, new TEC $259.952M approved
  2023-03-20 (FY2024, FY2025 CBJs). The CBJ gives the new TEC, not the new TPC, so the ratio
  259.952/242.72 = 1.071 is a floor (TPC is TEC plus OPC).
- HL-LHC ATLAS: CD-0 2016-04-13 $125M to $155M; CD-1 2018-09-21 $149M to $181M; CD-3A
  2019-10-16; CD-2/3 2023-01-31 TPC $200M. HL-LHC CMS: CD-0 2016-04-13 $125M to $155M; CD-1
  2019-12-19 $144.1M to $183M; CD-3A 2020-06-08; CD-2/3C 2023-04-04 TPC $200M. Both "stalled by
  COVID shutdowns and increased costs" (FY2023 CBJ). FY2027 is the final year of TEC funding
  for both.
- Schedule: HL-LHC start was 2027 as of Feb 2021 (Fermilab news), now 2030 (Fermilab news
  2026-02), one year outside the P5 "2020s" window; LS3 began summer 2026.
- Not verified: AUP CD-4 date (an LBL ATAP page in search results says 2016 CD-0 to 2028 CD-4;
  lbl.gov is blocked) and AUP post-rebaseline TPC.

### p5-2014-lhc-phase-1 (partial, guess)
- ATLAS Phase-1 MIE: CD-2/3 2014-11-12, TPC $33.25M, CD-4 FY2019. CMS Phase-1 MIE: CD-2/3
  2014-11-12, TPC $33.217M, CD-4 FY2020 (FY2019 CBJ; FY2018 CBJ said CMS would complete the
  bulk of deliverables in FY2017). No cost change reported through FY2019. Both absent from
  the FY2020 CBJ MIE table.
- CMS pixel detector and parts of the trigger and HCAL installed before FY2018 and ran in
  Run 2 (FY2019 CBJ). ATLAS Phase-1 components installed from 2018 and during LS2. Run 3
  (first full Phase-1 data) began 2022-07-05 (news.fnal.gov/tag/lhc-run-3, used in the built
  row). P5 said "completed by 2018"; the LHC's own LS2 slipped with COVID.
- Not verified: actual CD-4 dates and closeout costs for either MIE (not in any CBJ or PM
  report read; the PM reports list projects over $50M). Hence `guess`.

### p5-2014-desi (yes)
- CD-0 2012-09-12 range $25M to $42M (predates ranking). CD-2 2015-09-17 TPC $56.328M,
  completion FY2021 (FY2017 CBJ). CD-3 2016-06-22. FY2018 CBJ flagged a rebaseline for
  FY2017 funding, but every later CBJ keeps $56.328M.
- Commissioning complete 2020-03; project completion (CD-4) approved 2020-05 (FY2022 CBJ).
  Final cost $54.418M, completed and closed FY2020 (PM metrics FY2021 Q3). Ratio 0.966.
- Five-year survey started 2021-05 (FY2022, FY2023 CBJs; Fermilab news 2026-04), finished
  2026-04. Target 2020 to 2025: inside.

### p5-2014-lsst (yes)
- DOE LSSTcam only. CD-1 2012-04 (range $120M to $175M per a search snippet from lsst.org,
  blocked; predates ranking anyway). CD-3A 2014-06 (long-lead sensors, predates ranking).
  CD-2 2015-01-07, DOE TPC $168M, completion FY2022 (FY2016 CBJ). CD-3 2015-08-27.
- Completed and closed FY2021, latest TPC $165.28M (PM metrics FY2022 Q1); FY2023 CBJ: "MIE
  funded construction phase completed in 2021". Ratio 0.984. The camera was finished at SLAC
  2024-04 and mounted 2025-03 (search snippets; the DOE project had closed earlier).
- First Look 2025-06-23; LSST survey start 2026-06-30 (Fermilab news; FY2027 CBJ). Target
  2020 to 2030: inside. Cross-reference the Astro2010 LSST row for NSF totals and the
  facility-level schedule slip.

### p5-2014-dm-g2 (yes, from LZ)
- LZ: CD-1/3A 2015-04-24 range $46M to $59M (FY2017 CBJ); CD-2/3B 2016-08-08 TPC $55.5M,
  completion FY2022 (FY2018 CBJ); CD-3 2017-02-09. Completed FY2020, latest TPC $53.59M (PM
  metrics FY2021 Q1 to Q4; FY2022 Q1 and Q2 show $55.5M). CD-4 signed 2020-09-21 per LBL and
  Sanford Lab releases (blocked) and the Symmetry piece listed on news.fnal.gov/tag/lux-zeplin
  (2020-10-27); the PM reports confirm FY2020. Science operations 2021-12 (FY2024 CBJ), first
  results 2022-07-07 from 60 live days starting end of December 2021 (Fermilab news).
- SuperCDMS SNOLAB: CD-1 2015-12-21 range $16M to $21.5M (FY2017 CBJ); CD-2/3 2018-05-02 TPC
  $18.6M, CD-4 end FY2021 (FY2020, FY2021 CBJs). Rebaseline review passed 2021-09 with a $6.4M
  TPC increase, DOE $5.3M and NSF $1.1M (HEPAP Procario slides Nov 2021, science.osti.gov
  blocked, search snippet only) which gives about $25.0M, ratio about 1.34. CBJs then slipped
  science operations from late 2023 (FY2023) to FY2024 (FY2024). Installation and cooldown done
  by 2026-03 with science-quality data "on schedule to start in mid-2026" (Fermilab news
  2026-03, verified on an allowed host); early-science data taking began 2026-08 and a
  full-sensitivity year follows in 2027 (SLAC release 2026-08-26, host unreachable, snippet
  only). The handoff's flagged snippet is therefore partly verified: mid-2026 is confirmed by
  Fermilab, the exact August date is not.
- ADMX-G2: "series of small experiments" below the MIE threshold, fabrication completed
  FY2016 (FY2017 CBJ). Run 1A data January to June 2017 (arXiv:2312.16668). Cost: not stated
  in any CBJ; a search snippet attributes "$16M to $21M for DOE (FY15 to 19)" to a 2016 AAAC
  report on nsf.gov (blocked) but that figure matches the SuperCDMS CD-1 range and is not
  trusted. Gap.
- Target 2015 to 2024: LZ inside, SuperCDMS outside, ADMX-G2 inside.

## Gaps
1. AUP CD-4 date and post-rebaseline TPC (only TEC $259.952M is published).
2. Phase-1 ATLAS and CMS actual CD-4 dates and closeout costs.
3. SuperCDMS SNOLAB post-rebaseline TPC (snippet only) and exact first-data date (Fermilab
   confirms mid-2026; the August 2026 date is from an unreachable SLAC release).
4. ADMX-G2 cost (not in CBJs).
5. Mu2e final cost (CD-4 not before January 2028).
