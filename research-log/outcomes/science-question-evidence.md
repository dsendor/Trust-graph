# Science question evidence, Weekend 3

Evidence for the `science` outcome on five bets. Written 2026-10-01 by a research
sub-agent (Claude). The lead makes the final call; this file holds the promise as written,
every source read, the numbers, and a proposed result with a confidence. Quotes are
verbatim and marked with quotation marks. Hosts outside the allow list could not be opened;
where a fact rests only on a search snippet it is marked "search snippet only".

Draft rows: `science-question-draft.csv` next to this file.

## Summary table

| bet_id | question sold on | proposed result | headline | confidence |
|---|---|---|---|---|
| p5-2014-desi | dark energy equation of state to 5% (2020) and 1% (2025) | `surprise` | DESI DR2 BAO + CMB + DESY5: w0 = -0.752 +/- 0.057, wa = -0.86 +0.23 -0.20, 4.2 sigma from LCDM (2.8 to 4.2 depending on SN sample); constant w = -0.971 +/- 0.021 | confident |
| astro2010-wfirst (Roman) | why is the expansion accelerating | `building` | launched 2026-08-30; commissioning; first science images expected early 2027; no dark energy result yet | confident |
| astro2010-lsst (Rubin) | why is the expansion accelerating | `building` | LSST began 2026-06-30; DP1 (ComCam) 2025, DP2 (LSSTCam) mid-2026; year-1 cosmic shear forecast comparable to DESI+CMB, so earliest dark energy result about 2028 | confident |
| p5-2014-lbnf (DUNE) | mass ordering and CP violation | `building` | no beam data; first beam 2031; 3 sigma ordering needs 66 kt-MW-yr (about 3 beam-years); meanwhile NOvA+T2K show no strong ordering preference, NOvA alone Bayes factor 6.6 for normal with Daya Bay, JUNO running since Aug 2025 with 3 sigma expected after about 6.5 years | confident |
| p5-2014-cmb-s4 | amplitude of primordial gravitational waves (r) to percent level by 2025 | `no` (alternative: `partial`) | CMB-S4 cancelled July 2025; r < 0.036 (BICEP/Keck 2021), r < 0.034 (all CMB + BAO, end 2025); target was r < 0.001; BICEP2 claim was refuted in 2015 by other experiments | confident |

---

## 1. p5-2014-desi: dark energy equation of state

### (a) The promise as written

P5 2014 (`sources/p5-2014.txt`, p. 39 to 40, lines 2585 to 2596 and 2604 to 2608):

- "Measure the parameters that characterize dark energy to 5% precision (2020) and then improve to 1% (2025) over the entire history from the decelerating epoch to accelerating epoch."
- "Distinguish dark energy from modified gravity as an explanation of the current epoch of acceleration by measuring structure to 10% (2020), ultimately reaching percent precision over a wide range of distance scales and times (2030)."
- "The expansion history constraints from DESI BAO can be measured at the percent level, looking back over ten billion years. DESI can also measure RSD, providing a unique view of structure growth over time."
- bets.csv `promise_quote`: "Build DESI as a major step forward in dark energy science, if funding permits (see Scenarios discussion below)."

Note on the target: the 5%/1% goal is on "the parameters that characterize dark energy", with no stated parametrization. The natural readings are the constant equation of state w, or (w0, wa). Both are reported below.

### (b) Sources read

**https://arxiv.org/abs/2404.03002** DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations. DESI Collaboration, submitted 2024-04-03. DR1, first year, "over 6 million extragalactic objects in the redshift range 0.1<z<4.2".
- "Extending the baseline model with a constant dark energy equation of state parameter w, DESI BAO alone require w=-0.99+0.15-0.13."
- "In models with a time-varying dark energy equation of state parametrized by w0 and wa, combinations of DESI with CMB or with SN Ia individually prefer w0>-1 and wa<0. This preference is 2.6σ for the DESI+CMB combination, and persists or grows when SN Ia are added in, giving results discrepant with the ΛCDM model at the 2.5σ, 3.5σ or 3.9σ levels for the addition of Pantheon+, Union3, or DES-SN5YR datasets respectively."
- "combining the DESI and CMB data yields an upper limit Σmν < 0.072 (0.113) eV at 95% confidence for a Σmν>0 (Σmν>0.059) eV prior."

**https://arxiv.org/abs/2503.14738** (abstract) and **https://arxiv.org/pdf/2503.14738** (PDF, Tables V and VI, read with pdftotext). DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints. DESI Collaboration, submitted 2025-03-18, Phys. Rev. D 112, 083515 (2025). "more than 14 million galaxies and quasars", "three years of operation".
- Abstract: "The results are well described by a flat ΛCDM model, but the parameters preferred by BAO are in mild, 2.3σ tension with those determined from the cosmic microwave background (CMB)". "This solution is preferred over ΛCDM at 3.1σ for the combination of DESI BAO and CMB data. When also including SNe, the preference for a dynamical dark energy model over ΛCDM ranges from 2.8−4.2σ depending on which SNe sample is used." "From the combination of DESI and CMB we derive 95% upper limits on the sum of neutrino masses, finding ∑mν<0.064 eV assuming ΛCDM and ∑mν<0.16 eV in the w0wa model. Unless there is an unknown systematic error associated with one or more datasets, it is clear that ΛCDM is being challenged by the combination of DESI BAO with other measurements and that dynamical dark energy offers a possible solution."
- Table V, wCDM (constant w), 68% intervals: DESI+CMB w = -1.055 +/- 0.036 (3.4%); DESI+CMB+Pantheon+ w = -0.995 +/- 0.023 (2.3%); DESI+CMB+Union3 w = -0.997 +/- 0.027 (2.7%); DESI+CMB+DESY5 w = -0.971 +/- 0.021 (2.2%); DESI+DESY5 alone w = -0.872 +/- 0.039.
- Table V, w0waCDM: DESI+CMB w0 = -0.42 +/- 0.21, wa = -1.75 +/- 0.58; DESI+CMB+Pantheon+ w0 = -0.838 +/- 0.055, wa = -0.62 +0.22 -0.19; DESI+CMB+Union3 w0 = -0.667 +/- 0.088, wa = -1.09 +0.31 -0.27; DESI+CMB+DESY5 w0 = -0.752 +/- 0.057, wa = -0.86 +0.23 -0.20.
- Table VI, significance of w0waCDM over LCDM: DESI alone 1.7σ; DESI+CMB 3.1σ; DESI+CMB+Pantheon+ 2.8σ; DESI+CMB+Union3 3.8σ; DESI+CMB+DESY5 4.2σ.
- Text: "Assuming a ΛCDM background, the combination of DESI and CMB data give the tightest upper bound on the neutrino mass sum to date, Σmν < 0.064 eV (95% limit) in our baseline analysis." "both results are approaching the lower bound set by terrestrial neutrino oscillation experiments, Σmν ≥ 0.059 eV."
- BAO precision: Lyman-alpha BAO "precision of 0.64% at an effective redshift of zeff = 2.33"; galaxy isotropic BAO per tracer "between 0.1% (QSO) and 2% (LRG3+ELG1)" (statistical, per bin).
- Note: the DR1 figure for Union3 was 3.5σ; DR2 raises it to 3.8σ. The brief's "2.8 to 4.2 sigma" matches DR2.

**https://arxiv.org/abs/2411.12022** DESI 2024 VII: Cosmological Constraints from the Full-Shape Modeling of Clustering Measurements. DESI Collaboration, submitted 2024-11-18. On the second P5 goal (structure growth, modified gravity): "DESI (FS+BAO), combined with a baryon density prior from Big Bang Nucleosynthesis and a weak prior on the scalar spectral index, determines matter density to Ωm=0.2962±0.0095, and the amplitude of mass fluctuations to σ8=0.842±0.034." "DESI data alone measure the modified-gravity parameter that controls the clustering of massive particles, μ0=0.11+0.45−0.54, while the combination of DESI with the CMB and the clustering and lensing analysis from DESY3 constrains both modified-gravity parameters, giving μ0 = 0.04±0.22 and Σ0 = 0.044±0.047, in agreement with general relativity." The 4% on σ8 from DESI alone meets the "structure to 10% (2020)" goal.

**https://arxiv.org/abs/2607.27410** DESI DR2 Results IV: Alcock-Paczyński Measurements from the Lyman Alpha Forest and Cosmological Constraints. DESI Collaboration, submitted 2026-07-29. One percent AP measurement at z = 2.33; evolving dark energy "preferred over ΛCDM at 2.7σ for DESI and CMB data combined, and at 3.2σ when additionally including supernovae." (These are the Lyman-alpha-only DR2 numbers, not a new headline.)

**https://arxiv.org/abs/2602.05368** Dark Energy After DESI DR2: Observational Status, Reconstructions, and Physical Models. S. G. Turyshev, submitted 2026-02-05. Review: "DESI DR2 delivers percent-level BAO distance ratios over 0≲z≲2.5"; the evolving-dark-energy preference "depends on the specific dataset employed" and is sensitive to supernova calibration at the few percent magnitude level. Useful as the independent caveat.

**https://news.fnal.gov/2026/04/desi-completes-planned-3d-map-of-the-universe-and-continues-exploring/** Fermilab news, 2026-04-17. "Surprising results using DESI's first three years of data hinted that dark energy, once thought to be a 'cosmological constant,' might be evolving over time." "Researchers expected to gather data on 34 million galaxies and quasars during the five-year survey, but the instrument performed so efficiently that it captured more than 47 million galaxies and quasars, plus more than 20 million nearby stars." "the collaboration will immediately begin processing the completed dataset, with the first dark energy results from DESI's full five-year survey expected in 2027." DESI continues to 2028, expanding the footprint "from 14,000 square degrees to 17,000 square degrees".

**No DESI DR2 full-shape cosmology paper found.** An arXiv title search for "DESI DR2 Results" (2026-10-01) lists Results I, II (both March 2025) and IV (July 2026); the Lyman-alpha full-shape validation paper is arXiv:2607.27411. The DR2 full-shape cosmology paper has not appeared as of this date.

### (c) Proposed result: `surprise`, confident

The P5 2014 target was 5% (2020) then 1% (2025). By March 2025, with three of five survey years, DESI DR2 BAO combined with CMB and supernovae pins a constant w to 2.1 to 3.6% (w = -0.971 +/- 0.021 with DESY5) and w0 to about 7.5% (w0 = -0.752 +/- 0.057), so the 5% goal is met for constant w and the 1% goal is not met on any reading; the 10% structure-growth goal was met by DR1 full shape (σ8 to 4%). The headline, though, is not the precision but the sign: every combination prefers w0 > -1, wa < 0, with evolving dark energy favored over LCDM at 2.8 to 4.2 sigma depending on the supernova sample (3.1 sigma from DESI+CMB alone), and the DESI+CMB neutrino mass bound (< 0.064 eV) now presses against the oscillation floor (0.059 eV). That is the thing P5 2014 did not promise and the field did not expect, so `surprise` fits better than `partial`. The full five-year result is due 2027; if it recedes, this row should revert to `partial` (precision between 5% and 1%).

Neutrino mass sum (asked for in the brief): DESI+CMB Σmν < 0.064 eV (LCDM) or < 0.16 eV (w0wa), 95%, from arXiv:2503.14738.

---

## 2. astro2010-wfirst (Roman) and astro2010-lsst (Rubin): why is the expansion accelerating

### (a) The promise as written

Astro2010 (`sources/astro2010.txt`):
- WFIRST, line 449: "WFIRST is a wide-field-of-view near-infrared imaging and low-resolution spectroscopy observatory that will tackle two of the most fundamental questions in astrophysics: Why is the expansion rate of the universe accelerating? And are there other solar systems like ours, with worlds like Earth?"
- LSST, line 577: "It would address the pressing and fundamental question of why the expansion rate of the universe is accelerating".
- Both, line 378: "The properties of dark energy would be inferred from the measurement of both its effects on the expansion rate and its effects on the growth of structure (the pattern of galaxies and galaxy clusters in the universe). In doing so it should be possible to measure deviations from a cosmological constant larger than about a percent."
- Target dates in bets.csv: WFIRST 2020, LSST 2016 to 2019.

### (b) Sources read

**Roman**

**https://www.aip.org/news-and-analysis/aas/nasa-launches-nancy-grace-roman-space-telescope** AIP (AAS feed of Sky and Telescope), dated AUG 30, 2026: "NASA has a new telescope headed into space. A SpaceX Falcon Heavy rocket roared to life at launch pad LC-39A at the Kennedy Space Center shortly after sunrise early Sunday". The page is a truncated syndication; the rest of the article is not on the AIP host.

**https://www.aip.org/fyi/the-week-of-august-31-2026** AIP FYI: "NASA's Nancy Grace Roman Space Telescope launched successfully on Sunday and is now headed to its observation orbit."

**https://www.aip.org/fyi/the-week-of-april-27-2026** AIP FYI: "NASA sets early September launch date for Roman Space Telescope" (headline only).

**Commissioning timeline: search snippet only, hosts unreachable** (nasa.gov, space.com, spacepolicyonline.com, scientificamerican.com blocked). Snippets agree on: a roughly 90-day commissioning period during the cruise to L2, Coronagraph Instrument powered on 2026-09-01, Wide Field Instrument activated 2026-09-11, first science images expected early 2027, science operations expected by early 2027. Best URL: https://science.nasa.gov/missions/roman-space-telescope/roman-commissioning/ (not opened). Confidence on these dates: guess.

**https://www.nationalacademies.org/read/26141/chapter/19** Astro2020, Appendix I (Panel on Electromagnetic Observations from Space 1): "The anticipated launch date is in late 2025." "The Nancy Grace Roman Space Telescope (formerly the Wide-Field Infrared Survey Telescope [WFIRST]) is a NASA mission to survey wide swaths of the sky at near-IR wavelengths to address fundamental questions about the nature of dark energy".

**https://www.nationalacademies.org/read/26141/chapter/9** Astro2020, Chapter 7: Roman "will begin its cosmology and exoplanet microlensing surveys" in the middle part of the decade; "Vera Rubin Observatory, with science commencing in late 2023 or early 2024, will conduct a deep survey over an enormous area of sky."

**https://www.nationalacademies.org/read/26141/chapter/4** Astro2020, Chapter 2: "Observations in the coming decade using Rubin Observatory, Roman, Euclid, and higher-resolution, higher-sensitivity CMB facilities will test whether observations are, or are not, consistent with a cosmological constant."

**https://arxiv.org/abs/2506.04402** Kessler et al., submitted 2025-06-04: simulations of the Roman High Latitude Time Domain Survey, "10,000 Roman SNe Ia that we combine with 4,400 events from LSST"; "The resulting dark energy figure of merit is well above the NASA mission requirement of 326". (Forecast; sets what Roman is required to deliver on w0, wa.)

**https://arxiv.org/abs/2601.00438** Cao et al., submitted 2026-01-01: Fisher forecasts for the Roman High Latitude Imaging Survey 3x2pt; abstract gives no w0, wa number.

**https://arxiv.org/search/?query=%22Roman+Space+Telescope%22+commissioning** (arXiv title/abstract search, 2026-10-01): September 2026 papers still say "set to launch in Fall 2026"; none report commissioning results.

**Rubin**

**https://news.fnal.gov/2026/06/action-nsf-doe-vera-c-rubin-observatory-begins-capturing-the-greatest-cosmic-movie-ever-made/** Fermilab news, 2026-06-30: the Legacy Survey of Space and Time officially began June 30, 2026, ten years, each point about 800 times; "Today, we begin filming the greatest cosmic movie ever made" (Brian Stone, NSF). No dark energy result timeline.

**https://arxiv.org/abs/2603.23786** The Vera C. Rubin Observatory Data Preview 1, Rubin team, submitted 2026-03-24: DP1 is "based on 1792 optical near infrared exposures acquired over 48 distinct nights by the Rubin Commissioning Camera" in late 2024, about 15 square degrees, about 2.3 million objects, "approximately 3.5 TB in size", for "early science investigations ahead of full operations in 2026". Not a cosmology dataset.

**https://arxiv.org/abs/2606.09938** and **https://arxiv.org/html/2606.09938v2** Commissioning of the Vera C. Rubin Observatory, P.-F. Léget, submitted 2026-06-07: "The Vera C. Rubin Observatory began commissioning its camera, LSSTCam, in April 2025, with the Legacy Survey of Space and Time (LSST) scheduled to start in 2026. A primary science goal is constraining Dark Energy through weak gravitational lensing of the large-scale structure (cosmic shear). After a full year of data from LSST, these measurements are expected to reach precision comparable to recent Dark Energy Spectroscopic Instrument (DESI), providing an independent test of hints that Dark Energy may evolve over time. However, cosmic shear requires exquisite control of instrumental systematics." Body: DP1 "released as Data Preview 1 (DP1) in mid-2025"; "real-time alerts having begun in February 2026"; "first batch of LSSTCam data is expected to be published as Data Preview 2 (DP2)...in mid-2026"; the 3x2pt analysis "should reach a precision comparable to the current combination of DESI and CMB results after just one year of the LSST survey"; "early LSSTCam data show this is more challenging than anticipated" (PSF modelling, chromatic effects, astrometric residuals).

**Early DP2 release 2026-07-27: search snippet only** (community.lsst.org blocked). Snippet: DP2 holds LSSTCam data from April 2025 to January 2026; images to follow October to December 2026.

### (c) Proposed results

**astro2010-wfirst: `building`, confident.** Roman launched 2026-08-30 (AIP), six years after Astro2010's 2020 target, and is in commissioning; its dark energy surveys have not started. No measurement of w0, wa from Roman exists. Earliest science images early 2027 (snippet only); a dark energy result needs the multi-year High Latitude surveys, so not before about 2029 to 2030. The science question is open; the facility exists.

**astro2010-lsst: `building`, confident.** LSST began 2026-06-30 (Fermilab), seven to ten years after the 2016 to 2019 target. DP1 and DP2 are commissioning data, not cosmology. Rubin's own commissioning paper says one year of LSST should match DESI+CMB precision on the evolving dark energy question but that early data are harder than expected, so the first competitive Rubin dark energy result is plausibly 2028, not earlier. The question Astro2010 sold both on has meanwhile been moved by DESI (see bet 1): the live question is now whether Rubin and Roman confirm or refute the DESI preference for w0 > -1, wa < 0.

---

## 3. p5-2014-lbnf (DUNE): neutrino mass ordering and CP violation

### (a) The promise as written

P5 2014 (`sources/p5-2014.txt`):
- Line 2153: "With these ingredients, combined with a baseline greater than 1000 km, LBNF can, with a single experiment, measure evidence for CP-violation in the lepton sector and provide a definite determination of the mass hierarchy, independent of the value of δCP."
- Lines 1050 to 1058 (goal): "we set as the goal a mean sensitivity to CP violation of better than 3σ (corresponding to 99.8% confidence level for a detected signal) over more than 75% of the range of possible values of the unknown CP-violating phase δCP. By current estimates, this goal corresponds to an exposure of 600 kt*MW*yr".
- bets.csv `promise_quote`: "Form a new international collaboration to design and execute a highly capable Long-Baseline Neutrino Facility (LBNF) hosted by the U.S. ... LBNF is the highest-priority large project in its timeframe." Target window 2018 to 2035.

### (b) Sources read

**https://news.fnal.gov/2026/05/fermilab-marks-major-milestone-for-world-leading-dune-experiment/** Fermilab news, May 2026: "Fermilab's priority is to deliver the first neutrino beam to DUNE by 2031." Steel for the far detector structures is moving underground ("10 million pounds of steel beams being moved a mile underground"); CERN cryostat steel "scheduled to be moved underground and prepared for installation this summer." No sensitivity or cost figures.

**https://arxiv.org/abs/2109.01304** Low exposure long-baseline neutrino oscillation sensitivity of the DUNE experiment, DUNE Collaboration, submitted 2021-09-03 (PDF read with pdftotext): DUNE "will be able to unambiguously resolve the neutrino mass ordering at a 3σ (5σ) level, with a 66 (100) kt-MW-yr far detector exposure", and can make "a robust measurement of CP violation at a 3σ level with a 100 kt-MW-yr exposure for the maximally CP-violating values δCP = ±π/2". Rate: "with two FD modules, assuming a fiducial mass of 10 kt and a beam intensity of 1.2 MW, exposure would accumulate at a rate of 24 kt-MW-yr per calendar year, although a ramp up in beam power is expected before reaching the design intensity in early running." Uptime of 57% is already folded into that rate. So Phase I reaches 3 sigma on the ordering after about 2.75 beam-years and 5 sigma after about 4.2, i.e. roughly 2034 and 2035 if beam starts 2031 at full power; later with the ramp.

**https://arxiv.org/abs/2502.08493** DUNE: science and status, F. Martínez López, submitted 2025-02-12: "Its primary goal is the determination of the neutrino mass hierarchy and the CP-violating phase." Phase I: "17-kton Liquid Argon Time Projection Chamber (LArTPC) far detector modules", "1.2 MW proton beam, with a planned upgrade to 2.4 MW".

**https://arxiv.org/html/2504.01804** US National Input to the European Strategy Update (2025): "The first phase of DUNE and PIP-II to open an era of precision neutrino measurements that include the determination of the mass ordering among neutrinos." Phase II: a 2.1 MW beam (ACE-MIRT), a third far detector, upgraded near detector.

**https://www.usparticlephysics.org/2023-p5-report/the-recommended-particle-physics-program.html** P5 2023: same Phase I sentence; "early implementation of the accelerator upgrade ACE-MIRT advances the DUNE program significantly, hastening the definite discovery" (of the ordering and CP violation).

**https://www.usparticlephysics.org/2023-p5-report/illuminate-the-invisible-universe.html** P5 2023: cosmic surveys "will provide complementary information with the measurements of the mass ordering by DUNE".

The state of the question without DUNE:

**https://arxiv.org/abs/2510.19888** Joint neutrino oscillation analysis from the T2K and NOvA experiments, NOvA and T2K Collaborations, submitted 2025-10-22, Nature 646, 818 (2025): Δm²₃₂ = 2.43 +0.04 -0.03 x 10⁻³ eV² (normal) or -2.48 +0.03 -0.04 x 10⁻³ eV² (inverted); 3σ δCP interval [-1.38π, 0.30π] (normal) and [-0.92π, -0.04π] (inverted). The data show no strong preference for either mass ordering; if the inverted ordering is assumed, the result would be evidence of CP violation in the lepton sector.

**https://arxiv.org/abs/2509.04361** Precision measurement of neutrino oscillation parameters with 10 years of data from the NOvA experiment, NOvA Collaboration, submitted 2025-09-04, PRL 136, 011802 (2026): "The NOvA data show a mild preference for the normal mass ordering with a Bayes factor of 2.4" (70%), rising to 6.6 (87%) with the Daya Bay Δm²₃₂ constraint; Δm²₃₂ = 2.431 +0.036 -0.034 x 10⁻³ eV² (normal).

**https://arxiv.org/abs/2606.14121** Determining Neutrino Mass Ordering with NOvA and Upcoming JUNO Measurements, NOvA Collaboration, submitted 2026-06-12: "We find that 3σ evidence of the normal ordering is achievable over a range of plausible JUNO measurements within the next five years."

**https://arxiv.org/abs/2511.14593** First measurement of reactor neutrino oscillations at JUNO, JUNO Collaboration, submitted 2025-11-18 (PDF read): "using the first 59.1 days of data collected since detector completion in August 2025", sin²θ₁₂ = 0.3092 +/- 0.0087 and Δm²₂₁ = (7.50 +/- 0.12) x 10⁻⁵ eV², improving "precision by a factor of 1.6 relative to the combination of all previous measurements"; results "confirm JUNO's readiness for its primary goal of resolving the neutrino mass ordering with a larger dataset". No ordering result yet.

**https://arxiv.org/abs/2405.18008** Potential to identify neutrino mass ordering with reactor antineutrinos at JUNO, JUNO Collaboration, submitted 2024-05-28, Chin. Phys. C 49, 033104: "3σ median sensitivity to reject the wrong mass ordering hypothesis" after about 6.5 years at 26.6 GW thermal power (JUNO plus TAO, reactor data alone). From an August 2025 start that is about 2032.

**https://arxiv.org/abs/2406.13516** Direct neutrino-mass measurement based on 259 days of KATRIN data, KATRIN Collaboration, submitted 2024-06-19, Science 388, 180 (2025): m_ν² = -0.14 +0.13 -0.15 eV², "an upper limit of m_ν < 0.45 eV at 90 % confidence level". KATRIN bounds the absolute scale, not the ordering.

**https://arxiv.org/abs/2503.14738** (see bet 1): DESI+CMB Σmν < 0.064 eV at 95% in LCDM, "approaching the lower bound set by terrestrial neutrino oscillation experiments, Σmν ≥ 0.059 eV" (the inverted ordering floor is about 0.10 eV, so the cosmological bound nominally disfavors inverted ordering, but relaxes to < 0.16 eV in the w0wa model).

### (c) Proposed result: `building`, confident

DUNE has no beam data and will not before 2031 (Fermilab, May 2026), so it has answered nothing; its Phase I sensitivity (3 sigma on the ordering at 66 kt-MW-yr, about three beam-years) puts a DUNE answer around 2034 to 2035, the end of the P5 2014 window. The question has moved without it: NOvA+T2K (Nature 2025) find no strong preference for either ordering, NOvA alone reaches a Bayes factor of 6.6 for normal only with Daya Bay, JUNO (running since August 2025) projects 3 sigma after about 6.5 years, and NOvA+JUNO project 3 sigma for normal "within the next five years". KATRIN caps the absolute mass at 0.45 eV and DESI's cosmological bound (0.064 eV) sits just above the normal-ordering floor. The honest state on 2026-10-01: the ordering is not determined at 3 sigma by anyone; the first 3-sigma answer is likely to come from JUNO or JUNO+NOvA around 2030 to 2032, before DUNE. If that happens, the lead may prefer `surprise` (answered by a different facility) at that time; today it is `building`.

---

## 4. p5-2014-cmb-s4: primordial gravitational waves (r)

### (a) The promise as written

P5 2014 (`sources/p5-2014.txt`):
- Line 2593 (goal): "Confirm or refute the BICEP2 detection of primordial gravitational waves from inflation (2015–17). Depending on the outcome, either measure the amplitude of this signal to the percent level or constrain the spectrum to sub-percent accuracy to distinguish between models of inflation (2025)."
- Line 604: "Current CMB probes will lead to a Stage 4 Cosmic Microwave Background (CMB-S4) experiment, with the potential for important insights into the ultra-high energy physics that drove inflation."
- Line 2040: next-generation surveys including CMB-S4 "are expected to improve on these by a factor of ten" (neutrino mass sum).
- bets.csv `promise_quote` (Recommendation 18): "Support CMB experiments as part of the core particle physics program. The multidisciplinary nature of the science warrants continued multiagency support." Target 2025.

### (b) Sources read

Goal and design target:

**https://arxiv.org/abs/2203.08024** and **https://arxiv.org/pdf/2203.08024** (PDF read) Snowmass 2021 CMB-S4 White Paper, CMB-S4 Collaboration, submitted 2022-03-15: "All inflation models that naturally explain the observed deviation from scale invariance and that also have a characteristic scale equal to or larger than the Planck scale predict r ≳ 0.001. A well-motivated sub-class within this set of models is detectable by CMB-S4 at 5σ. The observed departure from scale invariance is a potentially important clue that strongly motivates exploring down to r = 10−3. With an order of magnitude more detectors than precursor observations, and exquisite control of systematic errors, CMB-S4 will improve upon limits from pre-CMB-S4 observations by a factor of five to reach this target". "CMB-S4 will constrain ∆Neff < 0.06 at 95% C.L." (The brief's sigma(r) ~ 5e-4 is the CMB-S4 Science Book figure; the white paper states the target as r = 0.001.)

**https://www.nationalacademies.org/read/26141/chapter/23** Astro2020, Appendix M (Radio, Millimeter, Submillimeter panel): current constraints "r <0.06", models predict "r >0.001", CMB-S4 is to detect r or constrain it to "less than 0.001 at 95 percent confidence"; the panel also asks that third-generation CMB experiments aligned with CMB-S4 (the South Pole Observatory and the nominal Simons Observatory) "be high priorities for federal support"; construction about $500 million (2020 dollars), first light proposed 2026, construction complete 2028, operations to 2035.

**https://www.nationalacademies.org/read/26141/chapter/13** Astro2020, Appendix C (Cosmology panel): "A measurement of r >0.01 would imply that the inflationary field moved over very large distances... models... predict r >0.001." "A concerted effort over the next decade to improve the sensitivity to gravitational waves by a factor of 10–100 would cross important theoretical thresholds."

**https://www.nationalacademies.org/read/26141/chapter/9** and **chapter/2** Astro2020: "Cosmic Microwave Background Stage 4 Observatory (CMB-S4; joint NSF/DOE)", capital cost $660 million ("NSF share, $273 million; DOE share, $387 million"), operations $17 million/yr.

**https://www.usparticlephysics.org/2023-p5-report/illuminate-the-invisible-universe.html** P5 2023: "CMB-S4 is the transformative next-generation CMB experiment, with the ambitious primary science goals of constraining the energy scale of inflation and determining the abundance of light relic particles in the early universe." "CMB-S4 construction is planned to begin in Chile and at the South Pole late in this decade (Recommendation 2a)."

What happened to the facility:

**https://www.aip.org/fyi/nsf-delays-cosmic-microwave-background-experiment** AIP FYI, 2024-05-15: NSF will not advance CMB-S4 to the design phase "in its current form"; cost about $800 million jointly NSF and DOE, operations targeted for the early 2030s; NSF's Chris Smith: the agency "must prioritize the recapitalization of critical infrastructure at the South Pole so that the groundbreaking research it enables can continue to thrive."

**https://www.aip.org/fyi/the-week-of-july-14-2025** AIP FYI: "DOE and NSF announced they will no longer pursue the proposed Cosmic Microwave Background Stage Four (CMB-S4) project, despite it being identified as a top priority by U.S. particle physicists and astronomers." The exact statement date, 2025-07-09, and the quote "DOE and NSF have jointly decided that they can no longer support the CMB-S4 Project" come from search snippets of science.org and cmb-s4.org (both blocked): search snippet only, confidence guess on the date.

State of the question:

**https://arxiv.org/abs/1502.00612** A Joint Analysis of BICEP2/Keck Array and Planck Data, BICEP2/Keck and Planck Collaborations, submitted 2015-02-02, PRL 114, 101301: "strong evidence for dust and no statistically significant evidence for tensor modes"; "an upper limit r₀.₀₅<0.12 at 95% confidence". This settled the first half of the P5 2014 goal (refute BICEP2) in 2015, on schedule, with no US Stage 4 instrument.

**https://arxiv.org/abs/2110.00483** BICEP/Keck XIII, submitted 2021-10-01, PRL 127, 151301: "The likelihood analysis yields the constraint r₀.₀₅<0.036 at 95% confidence. Running maximum likelihood search on simulations we obtain unbiased results and find that σ(r)=0.009. These are the strongest constraints to date on primordial gravitational waves."

**https://arxiv.org/abs/2505.02827** Constraints on Inflationary Gravitational Waves with Two Years of SPT-3G Data, SPT-3G Collaboration, submitted 2025-05-05: "95% upper limit on the tensor-to-scalar ratio of r < 0.25", "σ(r) = 0.067", on about 1500 square degrees that "covers part of the proposed Simons Observatory and CMB-S4 deep fields".

**https://arxiv.org/abs/2512.10613** Inflation at the End of 2025: Constraints on r and n_s Using the Latest CMB and BAO Data, Balkenhol et al., submitted 2025-12-11 (revised 2026-06-29): with Planck, SPT, ACT and BICEP/Keck, "r<0.034" at 95%; n_s = 0.9682 +/- 0.0032 (CMB) or 0.9728 +/- 0.0029 with DESI BAO.

**https://arxiv.org/abs/2512.15833** The Simons Observatory: forecasted constraints on primordial gravitational waves with the expanded array of Small Aperture Telescopes, SO Collaboration, submitted 2025-12-17, JCAP 04 (2026) 051: SAT array grows from three to six by 2027, survey through 2035; forecast "a 1σ constraint on the tensor-to-scalar ratio r of σ_r = 1.2×10⁻³", improving to "σ_r = 7×10⁻⁴" under optimistic assumptions. This is the de facto replacement path: σ(r) about 1e-3 by 2035, versus the CMB-S4 goal of r < 0.001 at 95% (σ(r) about 5e-4).

Not found on allowed hosts: a 2025 or 2026 BICEP/Keck update to r < 0.036 (search snippet mentions a BICEP Array projection of σ(r) ≲ 0.003 using data to 2027, from arXiv:2203.16556, not opened).

### (c) Proposed result: `no`, confident (alternative `partial`)

The P5 2014 goal had two halves. The first, confirm or refute BICEP2 by 2015 to 2017, was done in 2015 (dust, r < 0.12) by BICEP2/Keck with Planck, before any Stage 4 program. The second, measure the amplitude to the percent level or constrain the spectrum to sub-percent accuracy by 2025, is unmet: the best bound is r < 0.034 to 0.036 (σ(r) = 0.009), a factor of ten to twenty above the r = 0.001 threshold CMB-S4 was designed to reach, and the US facility sold on that goal was cancelled by DOE and NSF in July 2025 after NSF ruled out the South Pole site in May 2024. What is left is Simons Observatory (σ(r) about 1e-3 forecast by 2035, with no US Stage 4 contribution) and BICEP Array. The neutrino mass sum half of the bets.csv question has been advanced by DESI (< 0.064 eV), not by a CMB-S4. On the bet's own question, the answer is `no`: the amplitude was not measured, the threshold was not reached, and the facility will not exist. `partial` is defensible if the lead counts the 2015 BICEP2 refutation as the first half of the goal delivered; attribution for the cancellation goes to the agencies (CLAUDE.md rule 6).

---

## Open gaps

1. Roman commissioning dates (90 days, first images early 2027) rest on search snippets; nasa.gov is blocked. The launch date is on AIP.
2. Rubin Early DP2 release date (2026-07-27) rests on a snippet; the mid-2026 expectation is on arXiv.
3. CMB-S4 statement date (2025-07-09) rests on snippets; the fact of cancellation is on AIP FYI.
4. No 2025 or 2026 BICEP/Keck r update was found on arXiv by title search; the end-2025 combined bound (r < 0.034) is from Balkenhol et al.
5. No DESI DR2 full-shape cosmology paper exists yet; the full five-year DESI result is promised for 2027.
6. The sigma(r) ~ 5e-4 CMB-S4 figure was not confirmed on an allowed host; the white paper states the goal as r = 0.001 and Astro2020 as r < 0.001 at 95%.
