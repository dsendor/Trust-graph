# Science question evidence, round 2: twelve P5 2014 bets

Evidence for the `science` outcome on twelve P5 2014 bets. Written 2026-10-02 by a research
sub-agent (Claude). Draft rows are in `science-round2-p5.csv` next to this file. Quotes are
verbatim and in quotation marks. Hosts outside the allow list were not opened; where a fact
rests only on a search snippet or on an earlier ledger row it is marked as such.

## Summary table

| bet_id | question sold on | result | headline | confidence |
|---|---|---|---|---|
| p5-2014-muon-g-2 | sharpen a 3.5 sigma discrepancy with the SM | `surprise` | 127 ppb delivered; WP25 lattice prediction moved onto the measurement, exp minus SM = 38(63) x 10^-11, no tension | confident |
| p5-2014-dm-g2 | order-of-magnitude sensitivity gain and discovery reach, 1 GeV to 100 TeV | `partial` | LZ 2.2 x 10^-48 cm2 at 40 GeV, no WIMP; ADMX excludes DFSZ 3.27 to 3.34 ueV; SuperCDMS no data yet | confident |
| p5-2014-sbn | conclusively address the sterile neutrino hints, 2015 to 2020 | `partial` | MicroBooNE: no nue excess, electron interpretation out at >99% CL; ICARUS: no numu disappearance, systematics limited; joint SBN analysis pending | confident |
| p5-2014-lar1 (SBND) | address the SBL anomalies with a mid-scale LAr detector | `building` | SBND running since 2024-12, no oscillation result yet | confident |
| p5-2014-lhc-phase-1 | keep ATLAS and CMS performing for Run 3 physics | `yes` | Run 3 Higgs results at 13.6 TeV consistent with SM, mu = 0.99 +/- 0.13 (ATLAS 4l) | confident |
| p5-2014-mice | demonstrate ionization cooling | `yes` | Nature 578, 53 (2020); emittance reduction confirmed 2023 | confident |
| p5-2014-lsst | percent-level dark energy and structure growth by 2030 | `building` | survey began 2026-06-30, no result; earliest about 2028 | confident |
| p5-2014-mu2e | muon to electron conversion, four orders of magnitude | `building` | Run I second half 2027, goal R < 8 x 10^-17 | confident |
| p5-2014-hl-lhc | Higgs couplings to few percent, new particle reach, 2020s | `building` | operation 2030 | confident |
| p5-2014-pip-ii | >1 MW beam by first LBNF operation | `building` | RFQ installed 2026-07, power-up 2027, CD-4 1Q FY2033, 1.2 MW KPP | confident |
| p5-2014-pingu (IceCube Upgrade) | mass hierarchy sooner than competitors, low-mass WIMPs | `building` | five strings deployed 2025/26, no data; projected up to 3 sigma in 5 years | confident |
| p5-2014-chips | incremental hierarchy and CP sensitivity on NuMI off-axis | `no` | never took data | confident |

---

## 1. p5-2014-muon-g-2

### The promise as written

P5 2014, p. 44 (`sources/p5-2014.txt` lines 2819 to 2826): "The prediction for the anomalous magnetic moment, g-2, of the muon differs from its measured value by three-and-a-half standard deviations. A new experiment, Muon g-2 at Fermilab, will significantly improve the accuracy of the measurement, and combining this with further improvements in the theoretical prediction for it may sharpen this discrepancy and point the way to new physics."

### Sources read

**https://news.fnal.gov/2025/06/muon-g-2-most-precise-measurement-of-muon-magnetic-anomaly/** Fermilab news, 2025-06-03. Final precision 127 ppb, better than the 140 ppb design goal. a_mu = 0.001 165 920 705 +/- 0.000 000 000 114 (stat) +/- 0.000 000 000 091 (syst). On theory: "recent challenges with the theoretical predictions reduce evidence of new physics from muon g-2"; the May 2025 Theory Initiative prediction using lattice QCD "remains closer to the experimental measurement, dampening the possibility of new physics"; "the theoretical effort will continue to work to understand the discrepancy between the data-driven and computational approaches."

**https://arxiv.org/abs/2506.03069** Measurement of the Positive Muon Anomalous Magnetic Moment to 127 ppb, Muon g-2 Collaboration, submitted 2025-06-03. Data 2020 to 2023, more than 2.5 times the previous statistics. "a_mu = 116 592 070 5(148) x 10^-12 (127 ppb)" combined with previous results; experimental world average "116 592 071 5(145) x 10^-12 (124 ppb)", a fourfold improvement over prior work.

**https://arxiv.org/abs/2606.17323** Final Report on the Measurement of the Positive Muon Anomalous Magnetic Moment at Fermilab to 127 ppb, Muon g-2 Collaboration, submitted 2026-06-15. Same numbers; abstract does not compare to theory.

**https://arxiv.org/abs/2505.21476** The anomalous magnetic moment of the muon in the Standard Model: an update, Aliberti et al. (Muon g-2 Theory Initiative, 235 authors), submitted 2025-05-27, final version 2025-09-11. "a_mu^SM = 116 592 033(62) x 10^-11" (530 ppb); "a_mu^exp - a_mu^SM = 38(63) x 10^-11"; "there is no tension between the SM and experiment at the current level of precision." Reason for the change: "A new measurement ... by CMD-3 has increased the tensions among data-driven dispersive evaluations ... to a level that makes it impossible to combine the results in a meaningful way", so the lattice QCD HVP is used, "a precision of about 0.9%".

Search snippets only (not opened, hosts blocked): CERN Courier 2025-07-08 "Fermilab's final word on muon g-2": "The new measurement agrees closely with a significantly revised Standard Model prediction." Listed on https://news.fnal.gov/tag/theory/.

### Judgment

`surprise`, confident. The experiment did exactly what it promised (127 ppb vs 140 ppb goal). The question it was sold on, a 3.5 sigma discrepancy that might point to new physics, dissolved on the theory side when WP25 switched the hadronic vacuum polarization to lattice QCD. The answer is "no discrepancy", reached by the prediction moving, not the measurement. The data-driven vs lattice tension in the theory remains open, so a future revision cannot be excluded.

---

## 2. p5-2014-dm-g2

### The promise as written

P5 2014, pp. 35 to 36 (lines 2339 to 2358): "any new experiment should either provide at least an order of magnitude improvement in cross section sensitivity for some range of DM masses and interaction types, or demonstrate the capability to confirm or deny an indication of a DM signal from another experiment. ... These experiments should span a broad mass range (1 GeV to 100 TeV) and use multiple target materials ... with an emphasis on cross-section reach and discovery potential, as well as the ability to confirm or refute the current anomalous results." Goal and timeframe (p. 37): "Probe dark matter interactions with ordinary matter over a range of dark matter masses and interaction types, with large and important discovery reach (2015-2024)."

### Sources read

**https://arxiv.org/abs/2410.17036** Dark Matter Search Results from 4.2 Tonne-Years of Exposure of the LUX-ZEPLIN (LZ) Experiment, LZ Collaboration, submitted 2024-10-22, PRL 135, 011802 (2025). "4.2 +/- 0.1 tonne-years from 280 live days"; new technique tagging 214Pb beta decays; 124Xe double electron capture identified as a new background. No WIMP signal; "the strongest SI exclusion set is 2.2 x 10^-48 cm2" at 90% CL at 40 GeV/c2; "best SI median sensitivity achieved is 5.1 x 10^-48 cm2"; world-leading for masses 9 GeV/c2 and above.

**https://arxiv.org/abs/2609.02823** Search for dark matter particle interactions in an extended nuclear recoil energy window with the LZ experiment, submitted 2026-09-02. 2.84 tonne-years, window to about 270 keV; one event at "248 +/- 23 (stat) +/- 23 (sys) keV"; "tension with the background-only hypothesis at a global significance of 2.6 sigma", local up to "3.4 sigma across the models tested". Not a discovery.

**https://arxiv.org/abs/2408.15227** Axion Dark Matter eXperiment around 3.3 ueV with DFSZ Discovery Ability, ADMX, submitted 2024-08-27, PRL 134, 111002 (2025). "excludes (with a 90% confidence level) DFSZ axions with masses between 3.27 to 3.34 ueV, assuming a standard halo model with a local energy density of 0.45 GeV/cm3 made up 100% of axions."

**https://arxiv.org/abs/2504.07279** Search for Axion Dark Matter from 1.1 to 1.3 GHz with ADMX, submitted 2025-04-09, PRL 135, 191001 (2025). "searched for axions between 1.10-1.31 GHz to extended Kim-Shifman-Vainshtein-Zakharov (KSVZ) sensitivity." Search snippet adds that DFSZ sensitivity was not reached in that run while keeping the scan rate, and that the G2 ADMX goal was 0.6 to 2 GHz at DFSZ sensitivity by 2025 (snippet only).

**https://news.fnal.gov/2026/03/a-chilling-new-search-for-dark-matter-will-soon-be-underway/** Fermilab news, 2026-03-17, SuperCDMS SNOLAB: "Installation was completed late last year, except for the shielding." "Science-quality data taking is on schedule to start in mid-2026." Target is light dark matter near the proton mass; "we don't expect to see more than a few events per year for our entire experiment."

Not verified: the size of the gain over 2014-era limits (LUX 2013 was of order 10^-45 to 10^-46 cm2 from memory; no allowed-host source read for this). The row says "roughly two orders" and flags it.

### Judgment

`partial`, confident. The sensitivity promise was met and exceeded by LZ; ADMX reached DFSZ sensitivity over a narrow mass band rather than the full G2 band; SuperCDMS, the low-mass leg, has no data two years past the 2024 window. No dark matter was found, so the discovery reach produced only limits. `yes` is defensible if the promise is read purely as reach.

---

## 3. p5-2014-sbn

### The promise as written

P5 2014, p. 12 (lines 1125 to 1145): "Hints from short-baseline experiments suggest possible new non-interacting neutrino types or non-standard interactions of ordinary neutrinos. ... A judiciously selected subset of experiments can definitively address the sterile-neutrino interpretation of the anomalies". Recommendation 15: "Select and perform in the short term a set of small-scale short-baseline experiments that can conclusively address experimental hints of physics beyond the three-neutrino paradigm." Target 2015 to 2020 in bets.csv.

### Sources read

**https://arxiv.org/abs/2110.14054** Search for an Excess of Electron Neutrino Interactions in MicroBooNE Using Multiple Final State Topologies, MicroBooNE, submitted 2021-10-26 (PRL 2022). Three independent single-electron searches; results "consistent with the nominal electron neutrino rate expectations from the Booster Neutrino Beam and no excess of electron neutrino events is observed."

**https://news.fnal.gov/2021/10/microboone-experiments-first-results-show-no-hint-of-a-sterile-neutrino/** Fermilab news, 2021-10-27. MicroBooNE "ruled out electrons as the sole source with greater than 99% confidence, and ruled out the most likely source of photons as the cause of MiniBooNE's excess events with 95% confidence." Open: "there's a chance it could still be a sterile neutrino, hiding in even more unexpected ways"; only half the dataset analyzed. "in one month, SBND will record more data than MicroBooNE collected in two years".

**https://arxiv.org/abs/2210.10216** First constraints on light sterile neutrino oscillations from combined appearance and disappearance searches with the MicroBooNE detector, submitted 2022-10-18, PRL 130, 011801 (2023). 6.37 x 10^20 POT; "observe no evidence of light sterile neutrino oscillations"; 95% CL exclusions that exclude part of the anomaly-allowed space; "Cancellation of nu_e appearance and nu_e disappearance effects due to the full 3+1 treatment of the analysis leads to a degeneracy when determining the oscillation parameters."

**https://arxiv.org/abs/2603.22557** First search for sterile neutrino oscillation leading to numu disappearance in the Booster Neutrino Beam at ICARUS, ICARUS Collaboration, submitted 2026-03-23. Run 2 (2022 to 2023), 1muNp selection: "we find no statistically significant muon neutrino disappearance at the ICARUS baseline of 600 meters"; 90% CL exclusion contours; "the analysis is systematics limited due to large unconstrained uncertainties from the flux and interaction models. In future joint analyses, data from ICARUS and the SBND detector ... will be combined ... enabling a robust, world-leading two-detector analysis."

**https://news.fnal.gov/2026/04/icarus-experiment-marks-major-milestone-in-first-neutrino-science-results/** Fermilab news, 2026-04-15. Same result; "it will be essential to work with SBND to reduce uncertainties and conduct a robust two-detector analysis." No date for the joint analysis.

**https://arxiv.org/abs/2504.00245** (PDF read with pdftotext) The Short-Baseline Near Detector at Fermilab, input to the European Strategy 2026 update, submitted 2025-03-31. "The SBN Program is fully online now with both the near (SBND) and far (ICARUS) detectors operating and is poised to test the eV-scale sterile neutrino hypothesis by covering the parameter regions allowed by past anomalies at ~5 sigma significance." SBND began operation in July 2024, "started collecting stable BNB data in December 2024 with an unprecedented rate of ~7,000 neutrino events per day", and will run "until the planned long accelerator shutdown at Fermilab (scheduled for late 2027/early 2028), accruing a total exposure of 10 x 10^20 protons on target."

No SBND oscillation or cross-section paper was found on arXiv as of 2026-10-02 (searches for "SBND first" 2026 returned only status and technique papers).

### Judgment

`partial`, confident. The electron-neutrino interpretation of the MiniBooNE excess is excluded and part of the 3+1 space is gone, but the conclusive two-detector test that the program was built for has not been published and the P5 window (2020) is six years past.

---

## 4. p5-2014-lar1 (scored on SBND)

Promise (p. 13, line 1183): "LAr1 is a mid-scale short-baseline accelerator-based experiment to address both the neutrino and antineutrino SBL anomalies." P5 did not recommend it; the ledger scores LAr1 on SBND, its realized near detector (see the `built` and `cost-schedule` rows).

Sources: the SBND white paper (arXiv:2504.00245) and ICARUS (arXiv:2603.22557) above. SBND has no published oscillation result; the ICARUS paper says its own result cannot be made robust without SBND.

### Judgment

`building`, confident. The detector is running with the world's largest neutrino-argon dataset; the question it inherited from LAr1 will be answered by the joint SBN analysis after the 2027 exposure. MicroBooNE's partial progress is credited on the SBN row, not here.

---

## 5. p5-2014-lhc-phase-1

Promise (p. 10, lines 920 to 927): "The nearest-term high-energy collider, the LHC and its upgrades, is a core part of the U.S. particle physics program, with unique physics opportunities addressing three of the main science Drivers (Higgs, New Particles, Dark Matter). The ongoing Phase-1 upgrade should be completed by 2018."

Sources:

**https://arxiv.org/abs/2605.19016** Measurements of the Higgs boson production, fiducial and differential cross-sections in the four lepton decay channel using 164 fb-1 of data collected at sqrt(s) = 13.6 TeV with the ATLAS detector, submitted 2026-05-18. "sigma_fid = 3.65 +0.35 -0.33 fb" vs SM "3.68 +/- 0.17 fb"; signal strength "mu = 0.99 +/- 0.13"; "All the results are consistent with Standard Model expectations."

**https://arxiv.org/abs/2602.18611** Combined measurements and interpretations of Higgs boson production and decay in proton-proton collisions at sqrt(s) = 13 TeV, CMS, submitted 2026-02-20. Run 2 (138 fb-1), seven decay channels; inclusive signal strength "1.014 +0.055/-0.053"; "good compatibility with the standard model predictions for the majority of the measured parameters."

Search snippets only: ATLAS Run 3 CP studies of the Higgs-vector coupling "in good agreement with the SM"; ATLAS+CMS HH combination March 2026. Run 3 start date 2022-07-05 is from the ledger's `built` row (news.fnal.gov/tag/lhc-run-3, which on reading lists only two 2022 Symmetry articles).

### Judgment

`yes`, confident. The Phase-1 detectors delivered Run 3 and its Higgs program; the physics answer so far is the Standard Model. New-particle and dark matter search papers were not surveyed (brief: keep brief).

---

## 6. p5-2014-mice

Promise: Recommendation 25 (p. 20): "consult with international partners on the early termination of MICE." The science question in bets.csv: demonstrate ionization cooling of a muon beam.

Sources:

**https://arxiv.org/abs/1907.08562** First demonstration of ionization cooling by the Muon Ionization Cooling Experiment, MICE Collaboration, submitted 2019-07-19; published as Nature 578, 53 to 59 (2020) (journal reference from a search snippet; arXiv page gives RAL-P-2019-003). Abstract: "The Muon Ionization Cooling Experiment collaboration has constructed a section of an ionization cooling cell and used it to provide the first demonstration of ionization cooling."

**https://arxiv.org/abs/2310.05669** Transverse Emittance Reduction in Muon Beams by Ionization Cooling, MICE Collaboration, submitted 2023-10-09 (STFC-P-2023-004). "Here we demonstrate a clear signal of ionization cooling through the observation of transverse emittance reduction in beams that traverse lithium hydride or liquid hydrogen absorbers ... The measurement is well reproduced by the simulation of the experiment and the theoretical model."

Context from the ledger's cost-schedule row (arXiv:1805.07128, 1312.1626): rebaselined to Step IV in November 2014; Step VI (sustainable cooling with re-acceleration) never built; data 2016 to 2017.

### Judgment

`yes`, confident. Ionization cooling was demonstrated, at reduced scope. Attribution note: the result came from the UK-led collaboration after P5 recommended early termination of US participation.

---

## 7. p5-2014-lsst

Promise: "Complete LSST as planned" (Recommendation 17); cosmic acceleration goals p. 39: structure to 10% by 2020 and percent precision by 2030.

Sources:

**https://arxiv.org/abs/2606.09938** Commissioning of the Vera C. Rubin Observatory, submitted 2026-06-07. "The Vera C. Rubin Observatory began commissioning its camera, LSSTCam, in April 2025, with the Legacy Survey of Space and Time (LSST) scheduled to start in 2026. ... After a full year of data from LSST, these measurements are expected to reach precision comparable to recent Dark Energy Spectroscopic Instrument (DESI), providing an independent test of hints that Dark Energy may evolve over time. However, cosmic shear requires exquisite control of instrumental systematics."

**https://news.fnal.gov/2026/06/action-nsf-doe-vera-c-rubin-observatory-begins-capturing-the-greatest-cosmic-movie-ever-made/** Fermilab news, June 2026: the ten-year LSST officially started 2026-06-30.

### Judgment

`building`, confident; same logic as astro2010-lsst in `science-question-draft.csv`.

---

## 8. p5-2014-mu2e

Promise (p. 44, lines 2808 to 2818): "Very ambitious next-generation experiments aim to be sensitive to conversion rates four orders of magnitude beyond the existing bounds ... Phase II of COMET, not yet approved, and Mu2e plan to improve this sensitivity by two more orders of magnitude [beyond COMET Phase I's 3 x 10^-15] in a similar time frame."

Source: **https://arxiv.org/html/2609.25943** Future Muon Physics Experiments: Muon Beams and Experimental Apparatus, submitted 2026-09-22. "The experiment is currently in detector installation and commissioning, with Run I expected to begin in the second half of 2027"; "Mu2e aims for a 90% CL upper limit of R_mue < 8 x 10^-17"; "The current best limit is R_mue < 7 x 10^-13 at 90% CL, set by SINDRUM II on a gold target". Search snippet only: Run I collects about 10% of full statistics before the 2028 Fermilab shutdown and reaches up to 1000 times better than current limits.

### Judgment

`building`, confident.

---

## 9. p5-2014-hl-lhc

Promise (p. 10): HL-LHC "is required to fully exploit the physics opportunities offered by the ultimate energy and luminosity performance of the LHC"; operate in the 2020s; Higgs couplings to a few percent per bets.csv.

Sources:

**https://news.fnal.gov/2026/02/hilumi-lhc-full-scale-tests-start/** Fermilab news, 2026-02-24: HL-LHC will "increase by a factor of ten the number of particle collisions (called 'luminosity')", let physicists "understand for the first time how the Higgs boson interacts with itself", and is "set to enter operation in 2030" after Long Shutdown 3 starting summer 2026. Five US cryoassemblies shipped, five more by mid-2027.

**https://arxiv.org/abs/2504.00672** Highlights of the HL-LHC physics projections by ATLAS and CMS, submitted 2025-04-01 (ESPP input): the projections for Higgs couplings, self-coupling and searches.

### Judgment

`building`, confident. Interim Run 3 results (bet 5) show no deviation from the SM.

---

## 10. p5-2014-pip-ii

Promise (Recommendation 14, p. 12): "provide proton beams of >1 MW by the time of first operation of the new long-baseline neutrino facility."

Sources:

**https://news.fnal.gov/2026/07/fermilab-installs-first-beamline-component-for-new-state-of-the-art-accelerator/** Fermilab news, 2026-07-09: 800 MeV, 215 m linac for DUNE; RFQ installed; power application for first beam commissioning begins 2027. "What we're building now will set Fermilab up for the next 50 to 60 years."

**https://www.energy.gov/documents/fy-2027-high-energy-physics-budget-request** FY2027 HEP budget justification (scratchpad text cbj-FY2027-HEP.txt): "PIP-II received Critical Decision (CD)-3 approval on April 18, 2022, with a Total Project Cost (TPC) of $978,000,000. The CD-4 milestone date is 1Q FY 2033." KPP threshold: "Upgrades of the Booster, Recycler and Main Injector Synchrotrons, required to support delivery of 1.2 MW onto the LBNF target, will be installed and tested without beam."

Search snippets only (arXiv:2606.25159, 2503.23744): linac construction complete about 2028, two-year user shutdown from 2028 to connect Linac2 to the Booster, DUNE first beam physics 2031 at 1.2 MW.

### Judgment

`building`, confident.

---

## 11. p5-2014-pingu (scored on the IceCube Upgrade)

Promise (p. 13, lines 1188 to 1196): "PINGU, an infill array concept at the IceCube facility, may also have the interesting potential to determine the neutrino mass hierarchy using atmospheric neutrinos sooner than other competing methods, as well as have sensitivity to low-mass WIMP dark matter."

Sources:

**https://arxiv.org/abs/1401.2046** (PDF read with pdftotext) Letter of Intent: The Precision IceCube Next Generation Upgrade (PINGU), submitted 2014-01-09, revised 2017-09-05: PINGU "will be able to distinguish the neutrino mass ordering at 3 sigma significance with less than 4 years of data"; "PINGU will determine the ordering with a significance of 3 sigma in roughly 4 years. This significance depends quite strongly on the actual value of theta23".

**https://arxiv.org/abs/2509.13066** (PDF read with pdftotext) Physics potential of the IceCube Upgrade for atmospheric neutrino oscillations, submitted 2025-09-16: seven new strings in the 2025-2026 austral summer; "For a true normal ordering a detection significance of up to 3 sigma is possible within 5 years, while for a true inverted ordering up to 2 sigma is possible"; "a factor of 2 - 3x boost in the median NMO sensitivity" over IceCube without the strings.

**https://arxiv.org/abs/2609.24387** IceCube Upgrade status and perspectives, submitted 2026-09-21: five new strings installed in the 2025/26 austral summer as a dense infill. The abstract page read here does not give the science-data start; the "fall 2026" date is carried from the ledger's `cost-schedule` row, which cites the same paper's body.

Mass ordering status from `science-question-evidence.md` (LBNF row): not determined at 3 sigma by anyone as of 2026-10; NOvA+T2K no strong preference (arXiv:2510.19888); JUNO running since August 2025 with 3 sigma expected after about 6.5 years (arXiv:2405.18008); NOvA+JUNO project 3 sigma within five years (arXiv:2606.14121).

### Judgment

`building`, confident. Nothing answered; the realized instrument is smaller and slower than the promise, and other experiments are now expected to answer first.

---

## 12. p5-2014-chips

Promise (p. 13): "CHIPS proposes a large water Cherenkov detector in a water-filled mine pit, first at a NuMI off-axis location, and possibly later as an off-axis LBNF detector." P5: N/N/N.

Source: **https://arxiv.org/abs/2401.11728** The Design and Construction of the CHIPS Water Cherenkov Neutrino Detector, submitted 2024-01-22: "While issues during and after the deployment of the detector prevented data taking, a number of key concepts and designs were successfully demonstrated." Deployment October 2019, removal 2020 per the ledger's `built` row (same paper).

### Judgment

`no`, confident.

---

## Open gaps

- dm-g2: the size of LZ's gain over the 2014 limits (LUX 2013) was not verified from an allowed host; the row flags it.
- dm-g2: ADMX G2's stated goal (0.6 to 2 GHz at DFSZ sensitivity by 2025) rests on a search snippet; the two ADMX papers read show DFSZ reached only in the 3.27 to 3.34 ueV band.
- pingu: the fall 2026 science-data date is carried from the earlier cost-schedule row, not re-read.
- mu2e: the 2028 shutdown and Run I statistics fraction are snippet only.
- mice: the Nature 578, 53 (2020) journal reference is from a search snippet; the arXiv page lists only the RAL report number.
- lhc-phase-1: no survey of Run 3 new-particle or dark matter search papers; the `yes` rests on the detectors performing and the Higgs results read.
- sbn and lar1: no SBND physics paper found as of 2026-10-02; if the joint SBND plus ICARUS result appears, both rows should be rescored.
