# Science question evidence, round 2: eight Astro2010 bets

Written 2026-10-02 by a research sub-agent (Claude). Draft rows are in
`science-round2-astro.csv` next to this file. The lead makes the final call. Quotes are
verbatim and in quotation marks. Hosts outside the allow list were not opened; the
cost-schedule research notes (`astro2010-cost-schedule-space.md`, `-ground.md`) and
`science-question-evidence.md` section 4 were reused where they already held the fact.

## Summary table

| bet_id | question sold on | proposed result | headline | confidence |
|---|---|---|---|---|
| astro2010-new-worlds-tech | eta-Earth, exozodi level, technology for a direct-imaging mission | `partial` | eta-Earth 0.37 to 0.60 per Sun-like star (Kepler); median HZ dust 3 zodis, 95% < 27 zodis (HOSTS); Roman coronagraph launched 2026-08-30; imaging mission moved to the 2040s | confident |
| astro2010-inflation-probe-tech | detect primordial B-modes as evidence for inflation | `no` | r < 0.036 (BICEP/Keck 2021), r < 0.034 (all CMB + BAO, end 2025); no probe started; technology delivered | confident |
| astro2010-explorer | steady cadence of small missions responsive to discoveries | `yes` | 2 SMEX, 2 MIDEX, 4 MoOs from four AOs; IXPE first X-ray polarization of a point source; GUSTO 57-day record flight; SPHEREx first all-sky NIR spectral survey | confident |
| astro2010-msip | keep mid-scale ground innovation flowing | `partial` | $114M to 18 projects (HERA, ZTF, DSA, KPF, ngVLA and BICEP development) at half the target rate | confident |
| astro2010-lisa | waveforms of 1e4 to 1e7 Msun mergers, Galactic binaries | `building` | 2035 launch; meanwhile NANOGrav 2023 nanohertz background consistent with SMBH binaries | confident |
| astro2010-gsmt | spectra of JWST's earliest galaxies, exoplanet imaging | `building` | GMT first light mid-2030s; JWST confirmed z = 14.32 and 13.90 galaxies in 2024 | confident |
| astro2010-acta | dark matter via gamma-ray annihilation | `building` (alt `no` on US terms) | US never joined; CTAO-South from 2026; combined five-instrument dwarf limits, no detection | guess |
| astro2010-ccat | wide-field submm surveys for dusty high-z galaxies | `building` | 6 m FYST first light 2026, early science 2027 | confident |

---

## 1. astro2010-new-worlds-tech: eta-Earth, exozodi, imaging technology

### The promise as written

`sources/astro2010.txt`:
- line 313: "The optimum strategy depends strongly on the fraction of stars with Earth-like planets orbiting them. If the fraction is close to 100 percent, then astronomers will not need to look far to find an Earth-like planet, but if Earth-like planets are rare, then a much larger search extending to more distant stars will be necessary."
- line 513 to 516: "The first is to understand the demographics of other planetary systems, in particular to determine over a wide range of orbital distances what fraction of systems contain Earth-like planets ... The second need is to characterize the level of zodiacal light present so as to determine, in a statistical sense if not for individual prime targets, at what level starlight scattered from dust will hamper planet detection. Nulling interferometers on NASA-supported ground-based telescopes (for example, Keck, and the Large Binocular Telescope) ... could be used to constrain zodiacal light levels."
- bets.csv `promise_quote`: "The ultimate goal is to image rocky planets that lie in the habitable zone of nearby stars ... and to characterize their atmospheres."

### Sources read

- https://arxiv.org/abs/2010.14812 Bryson et al., "The Occurrence of Rocky Habitable Zone Planets Around Solar-Like Stars from Kepler Data", submitted 2020-10-28 (AJ 2021). eta-Earth defined as "the HZ occurrence of planets with radius between 0.5 and 1.5 R⊕ orbiting stars with effective temperatures between 4800 K and 6300 K". Conservative HZ: "0.37+0.48−0.21 ... and 0.60+0.90−0.36 planets per star" (two extrapolation models); optimistic HZ "0.58+0.73−0.33 and 0.88+1.28−0.51 planets per star". With 95% confidence "the nearest HZ planet around G and K dwarfs is about 6 pc away" and there are "~4 HZ rocky planets around G and K dwarfs within 10 pc of the Sun".
- https://arxiv.org/abs/2003.03499 Ertel et al., "The HOSTS survey for exozodiacal dust: Observational results from the complete survey", submitted 2020-03-07 (AJ). LBTI nulling, N band 8 to 13 micron. 38 stars observed, 10 significant excesses (about 26%). "the majority of Sun-like stars have relatively low HZ dust levels (best-fit median: 3 zodis, 1 sigma upper limit: 9 zodis, 95% confidence: 27 zodis)"; the "median HZ dust level would not be a major limitation to the direct imaging search for Earth-like exoplanets", though tighter constraints are still needed for spectroscopic characterization. (The brief's arXiv:1910.04143 is a different paper, Tokovinin on spectroscopic binaries; the HOSTS final paper is 2003.03499.)
- https://www.nationalacademies.org/read/23560/chapter/6 2016 midterm: zodiacal light "will be investigated by NASA's investment in the Long Baseline Telescope Interferometer"; Finding 4-11: "The current planned decadal investment in NWNH-recommended technology development and precursor science exceeds the level envisioned in NWNH." No eta-Earth number.
- https://www.nationalacademies.org/read/26141/chapter/9 Astro2020 section 7.5.2: recommends "a high-contrast direct imaging mission with a target off-axis aperture of approximately 6 m" to yield "a robust sample of ~25 atmospheric spectra of potentially habitable exoplanets"; "Total implementation and operations cost (5 years) estimated at $11 billion" (FY2020), "target launch in the first half of the 2040s"; enters the Great Observatories Mission and Technology Maturation Program first; "uncertainty in the number of Earth-sized potentially habitable planets has been reduced by Kepler"; Roman will test "key capabilities" for starlight suppression.
- https://www.nationalacademies.org/read/26141/chapter/19 (from the cost-schedule notes) Astro2020 Appendix I: coronagraphic missions "require a significant technology investment, probably as large as $600 million ($FY 2020) by the start of phase A"; Roman coronagraph demonstrations at about 1e-9 contrast.
- https://www.aip.org/news-and-analysis/aas/nasa-launches-nancy-grace-roman-space-telescope AIP, 2026-08-30: Falcon Heavy launch from LC-39A (the article is a truncated Sky and Telescope repost; it does not mention the coronagraph).
- https://arxiv.org/abs/2608.17152 Savransky et al., 2026-08-17: Roman "will carry the Coronagraph Instrument, which will, for the first time, demonstrate high-contrast imaging with active wavefront control in visible wavelengths from space." First observations as early as December 2026 (from the cost-schedule notes on the same paper).

### Proposed result: `partial`, confident

The two precursor questions NWNH set for this line were answered: Kepler gave eta-Earth at roughly 0.4 to 0.6 per Sun-like star (with a factor of 2 to 3 spread between extrapolation models) and HOSTS showed the typical HZ dust level is low enough not to block exo-Earth imaging. The technology piece reached orbit only in August 2026 with first light pending, and the ultimate goal, a direct-imaging mission starting early in the 2020s, slipped to a 2040s launch under Astro2020's GOMAP. `yes` is defensible if the row is read as the precursor program alone; `partial` is the reading against the promise quote.

Not verified: any Roman coronagraph on-sky result (none exists yet); nasa.gov blocked for commissioning dates.

---

## 2. astro2010-inflation-probe-tech: primordial B-modes

### The promise as written

bets.csv `promise_quote`: "Detecting the B-mode polarization pattern on the cosmic microwave background impressed by gravitational waves produced during the first few moments of the universe both would provide strong evidence for the theory of inflation ... and would open a new window on exotic physics in the early universe". Table ES.4: mission-specific technology triggered only if B-modes were detected mid-decade.

### Sources read

Reused from `science-question-evidence.md` section 4 (all opened there):
- https://arxiv.org/abs/2110.00483 BICEP/Keck XIII (PRL 127, 151301, 2021): "r₀.₀₅<0.036 at 95% confidence", "σ(r)=0.009", "the strongest constraints to date on primordial gravitational waves".
- https://arxiv.org/abs/2512.10613 Balkenhol et al., "Inflation at the End of 2025": with Planck, SPT, ACT and BICEP/Keck, "r<0.034" at 95%.
- https://arxiv.org/abs/2505.02827 SPT-3G two-year B-mode result (2025): "r < 0.25", "σ(r) = 0.067", on 1500 deg².
- https://arxiv.org/abs/1502.00612 BICEP2/Keck and Planck joint analysis (2015): "strong evidence for dust and no statistically significant evidence for tensor modes", r < 0.12.
- https://arxiv.org/abs/2512.15833 Simons Observatory forecast (JCAP 2026): "σ_r = 1.2×10⁻³" by 2035 with six SATs.

Opened this round:
- https://arxiv.org/abs/2103.13334 SPIDER Collaboration, "A Constraint on Primordial B-Modes from the First Flight of the SPIDER Balloon-Borne Telescope", submitted 2021-03-24: NASA long-duration balloon, 2015 flight, 4.8% of sky at 95 and 150 GHz; "r<0.11 and r<0.19, respectively" (Feldman-Cousins and Bayesian); "roughly half the uncertainty in r derives from noise associated with the template subtraction". This is the NASA suborbital leg of the program NWNH funded.
- https://www.nationalacademies.org/read/23560/chapter/6 2016 midterm: a "convincing detection" of primordial B-modes "would represent a watershed discovery"; "While this has not occurred, significant new results have come from the Planck mission"; ground experiments target r ~ 0.01; Finding 4-12: the program is "well aligned with the recommendations of NWNH".
- https://www.nationalacademies.org/read/26141/chapter/9 (from the cost-schedule notes) Astro2020: a CMB probe "could potentially be a compelling candidate for the future probe call in the 2030s".

### Proposed result: `no`, confident

No primordial B-mode detection exists; the best bound (r < 0.034 to 0.036) is a factor of 3 below the 2010-era ground target of r ~ 0.01 but a detection it is not, the 2014 BICEP2 claim was dust, and the probe the technology was meant to enable was never triggered or started. The technology half was delivered (midterm Finding 4-12, SPIDER flights, the detector lineage behind BICEP Array, SPT-3G and Simons Observatory), so the row records a program that did its part on a question nature has not yet answered. Attribution of the `no` is to the universe, not to NASA or the committee.

Not verified: a 2025 or 2026 BICEP/Keck update (none found by arXiv title search in the earlier round).

---

## 3. astro2010-explorer: cadence and science of the augmented Explorer line

### The promise as written

bets.csv: "The Explorer program's Small Explorer (SMEX) and Medium-scale Explorer (MIDEX) missions, developed and launched on few-year timescales, enable rapid response to new discoveries and provide platforms for targeted investigations essential to the breadth of NASA's astrophysics program." Science question: 2 MIDEX, 2 SMEX, 4 MoOs over the decade.

### Sources read

- https://www.nationalacademies.org/read/26141/chapter/8 Astro2020 chapter 6: "NASA has largely achieved the recommended target" ($40M to $100M FY2010 per year); the augmentation "has resulted in an increased rate and a tremendous science output"; "TESS has already identified more than 4,000 planet candidates".
- https://www.nationalacademies.org/read/26141/chapter/9 Astro2020 section 7.1: "the Explorers Program has recently reached the enhanced selection rates envisioned by Astro2010, and is providing high-value scientific returns".
- https://www.nationalacademies.org/read/26141/chapter/18 Astro2020 Appendix H: Explorers "provide consistently excellent scientific returns for a relatively moderate investment" and "the ability of rapid response to new scientific and technical breakthroughs"; "NASA Astrophysics plans an Explorers program cadence of two MIDEXs, two SMEXs, and four MOs per decade"; Table H.1: IXPE (2014 AO, SMEX), GUSTO (2014 AO, MO), SPHEREx (2016 AO, MIDEX), TESS (2011 AO, MIDEX, 2018).
- https://arxiv.org/abs/2205.08898 Taverna et al., "Polarized x-rays from a magnetar", submitted 2022-05-18, Science (doi 10.1126/science.add0080): IXPE observation of 4U 0142+61, polarization degree "(12±1)%" over 2 to 8 keV, "(14±1)%" at 2 to 4 keV and "(41±7)%" at 5.5 to 8 keV, angle "swings by ~90°" around 4 to 5 keV; results "lend further support to the presence of the quantum mechanical effect of vacuum birefringence". Search snippet (arXiv 2402.05622): "the first time that polarized X-rays have been detected from any astrophysical point sources"; IXPE launched 2021-12-09.
- https://arxiv.org/abs/2511.02985 Bock et al., "The SPHEREx Satellite Mission", submitted 2025-11-04: "a NASA explorer satellite launched on 11 March 2025" conducting "the first all-sky near-infrared spectral survey", 102 bands over 0.75 to 5.0 micron, 6.2 arcsec pixels, four full-sky maps in two years; goals: "constrain the amplitude of inflationary non-Gaussianity", intensity mapping of the extragalactic background, and "the abundance and composition of water and other biogenic ice species in the interstellar medium". Search snippets (arXiv 2603.25790 and others): in-orbit checkout complete and survey start 2025-05-01; first public quick-release spectral images July 2025, QR2 October 2025.
- https://arxiv.org/pdf/2507.07289 (read with pdftotext) "Great Observatories Maturation: a Review of NASA Astrophysics Development Through Suborbital Rocket and Balloon Programs", 2025: "In 2024, the long-duration balloon mission GUSTO set the new record for an astrophysics stratospheric balloon mission duration with >57 days at a float altitude of ≈36 km. GUSTO carried a 0.9-m telescope and heterodyne arrays to spectroscopically map the interstellar medium throughout the Milky Way and the Large Magellanic Cloud at terahertz frequencies." (Launch was from McMurdo in December 2023 per search snippets; no GUSTO science paper found on arXiv by search.)
- `sources/pan-trimble-2024.txt`: "Imaging X-ray Polarimetry Explorer (SMEX-14) 2021, others planned".
- 2016 midterm (from the cost-schedule notes): first AO 2014 not 2012; "Even if fully executed, however, the plan does not result in the full augmentation recommended by NWNH."

### Proposed result: `yes`, confident

The question was whether the augmented line would sustain a cadence of quickly built missions that respond to discoveries. By 2021 the funding target and the 2+2+4 count were met, and the missions chosen have produced new capabilities (first X-ray polarimetry of point sources, the first all-sky NIR spectral survey, a record balloon flight). Astro2020's verdict, "tremendous science output", is the independent judgment. The late start is already scored `partial` on cost-schedule and is not double-counted here.

Not verified: a GUSTO science results paper (none on arXiv found); nasa.gov blocked.

---

## 4. astro2010-msip: mid-scale ground innovation

### The promise as written

bets.csv: "a competed program, based on NASA's highly successful Explorer model, that would enable moderate-scale projects to be frequently selected through peer review", at least seven projects over the decade, about $40M per year.

### Sources read

- https://www.nationalacademies.org/read/26141/chapter/8 Astro2020 chapter 6: "MSIP has competitively awarded a total of $114 million to 18 distinct projects spanning a diverse range of science and wavelength" (2014 to 2021), including HERA, the Deep Synoptic Array and the Keck Planet Finder; the projects are "high-impact projects with broad science reach and relevance to Astro2020 science goals"; "The last biannual solicitation provided a total of ~$21 million in funding, well below the $40 million a year target"; awards "between $2 million and $12 million per project, significantly below the ~$100 million level envisioned by Astro2010".
- https://arxiv.org/abs/2108.02263 HERA Collaboration, "First Results from HERA Phase I", submitted 2021-08-04 (ApJ 2022): "a 95% confidence upper limit on the 21 cm power spectrum of Δ²₂₁ ≤ (30.76)² mK² at k=0.192 h Mpc⁻¹ at z=7.9, and also Δ²₂₁ ≤ (95.74)² mK² at k=0.256 h Mpc⁻¹ at z=10.4"; search snippet: at z=7.9 "the most sensitive to-date by over an order of magnitude". The abstract page does not show the funding acknowledgment; HERA's MSIP funding rests on Astro2020 naming it as an MSIP project.
- https://arxiv.org/abs/1902.01932 Bellm et al., "The Zwicky Transient Facility: System Overview, Performance, and First Results", 2019, PASP 131, 995: "A custom-built wide-field camera provides a 47 deg² field of view and 8 second readout time, yielding more than an order of magnitude improvement in survey speed relative to its predecessor survey". The abstract page does not show the MSIP grant; ZTF's MSIP funding is from the brief and Pan and Trimble, not verified on an opened page.
- `sources/pan-trimble-2024.txt`: MSIP "Many funded, often technical development for bigger things, like ngVLA, BICEP, and IceCube-Gen2".
- 2016 midterm (from the cost-schedule notes): NSF-AST mid-scale funding fell from $31M (FY2010) to $15.5M (FY2015), $21M (FY2016).

### Proposed result: `partial`, confident

The line exists, has run continuously since 2013, and its awards produced the outcomes the recommendation was for (HERA's first reionization limits, ZTF's survey, design work for ngVLA, BICEP and IceCube-Gen2), but the annual rate is about half the target and the award ceiling an order of magnitude below the intended range, so the "frequently selected, moderate-scale" promise was met in kind and not in scale.

Not verified: MSIP grant numbers for HERA and ZTF (nsf.gov blocked; arXiv abstract pages omit acknowledgments).

---

## 5. astro2010-lisa: building

- https://arxiv.org/html/2608.31160v1 (from the cost-schedule notes): "ESA formally adopted the mission in January 2024 for a 2035 launch, and NASA's hardware contribution is now a formal project."
- https://arxiv.org/abs/2306.16213 NANOGrav Collaboration, "The NANOGrav 15-year Data Set: Evidence for a Gravitational-Wave Background", submitted 2023-06-28: correlated signal across 67 pulsars, Hellings-Downs correlations with "a Bayes factor in excess of 10^14" versus uncorrelated noise; strain amplitude "2.4^+0.7_-0.6 × 10^-15" at 1/yr; properties "consistent with astrophysical expectations for a signal from a population of supermassive black-hole binaries", with cosmological sources not excluded.
- Judgment: `building`, confident. The nanohertz background touches the supermassive black hole part of LISA's question (that SMBH binaries exist and merge in numbers), but LISA was sold on individual waveforms from 1e4 to 1e7 solar mass mergers and Galactic compact binaries in the millihertz band, which nobody has measured.

## 6. astro2010-gsmt: building

- https://arxiv.org/abs/2608.10212 (from the cost-schedule notes): GMagAO-X "on track to be ready at first-light of the GMT in the mid 2030s".
- https://arxiv.org/abs/2405.18485 Carniani et al., "Spectroscopic confirmation of two luminous galaxies at z~14", submitted 2024-05-28, Nature 633, 318: redshifts "z = 14.32 (+0.08/-0.20) and z = 13.90 ± 0.17"; "luminous galaxies were already in place 300 million years after the Big Bang and are more common than expected"; the z = 14.32 galaxy has a 260 pc radius and is "dominated by stellar continuum emission", so "the excess of luminous galaxies in the early Universe cannot be entirely explained by accretion onto black holes".
- Judgment: `building`, confident. JWST has done the discovery half of the NWNH story; the GSMT's job (resolved spectra, masses, chemistry of those galaxies, and direct exoplanet imaging) waits for a telescope a decade late.

## 7. astro2010-acta: building (alternative `no` on US terms)

- https://arxiv.org/abs/2508.20229 Fermi-LAT, HAWC, H.E.S.S., MAGIC and VERITAS Collaborations, "Combined dark matter search towards dwarf spheroidal galaxies", submitted 2025-08-27: "This five-instrument combination allows the derivation of up to 2-3 times more constraining upper limits on ⟨σv⟩ than the individual results over a wide mass range spanning from 5 GeV to 100 TeV"; limits of 1.5×10⁻²⁴ and 3.2×10⁻²⁵ cm³ s⁻¹ in the τ⁺τ⁻ channel at 2 TeV depending on the dark matter content model. No detection.
- https://arxiv.org/abs/2007.16129 CTA Consortium, "Sensitivity of the Cherenkov Telescope Array to a dark matter signal from the Galactic centre", 2020 (JCAP 2021): "CTA will open a new window of discovery potential, significantly extending the range of robustly testable models given a standard cuspy profile"; "even for a cored profile, the projected sensitivity of CTA will be sufficient to probe various well-motivated models of thermally produced dark matter at the TeV scale."
- https://arxiv.org/abs/2512.03798 Hinton, "Gamma-ray astronomy from the ground: future perspectives", 2025-12-03; the cost-schedule notes record from this paper that CTAO-South "observations with the first telescopes are expected to begin in 2026".
- https://arxiv.org/abs/2509.05527 (from the cost-schedule notes): "The initial CTAO configuration will include 14 MSTs of the DC design and no SCTs."
- Judgment: `building`, guess. The dark matter question is open for everyone; CTAO will start on it in 2026 without a US share. Because the US never delivered its $100M and has no stake in the data, the lead may prefer `no` for consistency with the cost-schedule row's "no on US terms" ruling.

## 8. astro2010-ccat: building

- https://arxiv.org/abs/2608.25111 (from the cost-schedule notes): Prime-Cam arrived on site 2026-07-31, "scheduled for integration in FYST in late 2026, followed by a year of early science observations" with the 280 and 350 GHz modules; EoR-Spec and 850 GHz modules 2027.
- https://arxiv.org/abs/2511.01707 Vavagiakis for the CCAT Collaboration, 2025-11-03: "The CCAT Observatory's Fred Young Submillimeter Telescope, a novel, high-throughput, 6-meter aperture telescope, is scheduled for first light in 2026"; Prime-Cam with over 100,000 KIDs over 220 to 850 GHz, "over ten times faster mapping speed than previous submillimeter observatories"; science: reionization line-intensity mapping, star formation, galaxy evolution, Galactic magnetic fields, transients, overlap with Simons Observatory.
- Judgment: `building`, confident. No data yet; the 6 m descope means the eventual row should weigh what a 6 m survey delivers against the 25 m promise.

---

## Open gaps

1. HOSTS: the brief's arXiv ID (1910.04143) is wrong; the complete-survey paper is 2003.03499 and that is what the row cites.
2. No GUSTO science paper on arXiv; the flight record rests on the 2025 suborbital review (arXiv:2507.07289), which cites a nasa.gov page (blocked).
3. MSIP grant numbers for HERA and ZTF not verified on an opened page.
4. Roman coronagraph: no on-sky result yet; commissioning schedule from nasa.gov is blocked.
5. ACTA: the row's `building` versus `no` depends on whether the bet is CTAO as a whole or the US share; flagged for the lead.
6. Astro2020 chapter 7 (read/26141/chapter/9) does not name CTA or US participation in the extracted text.
