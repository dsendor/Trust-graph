# Weekend 3 attribution: actors draft

Companion to `actors-draft.csv` (107 rows: 5 committee, 90 person, 12 agency; 99 confident,
8 guess). Written 2026-10-01. Named people stay in these two draft files only (CLAUDE.md
rule 7). Columns are the `data/actors.csv` six plus `confidence` and `rationale`.

How the file is organised:

- Committee rows: one per bet (`committee-p5-2014` x3, `committee-astro2010` x2).
- Chair rows: one per bet (`steve-ritz` x3, `roger-blandford` x2).
- Astro2010 panel chairs linked to the bet their panel ranked (Dressler for WFIRST, Osmer
  for LSST).
- Full membership: one row per member with `bet_id` blank (24 P5 rows including Lankford
  ex officio; 22 Astro2010 rows including three vice chairs and the executive officer).
  Ritz appears on both committees under one `actor_id`.
- Champions: roles as of ranking (2013-2014 for P5, 2009-2010 for Astro2010), and "later
  project leader" rows labelled with the year the source shows.
- Agencies: one row per agency per bet with role `funder`, plus the CMB-S4 withdrawal rows.

## Cross-links worth knowing before the trust graph

- John Carlstrom sat on the Astro2010 survey committee, convened the Snowmass 2013 CMB
  document P5 read, and was CMB-S4 co-spokesperson by 2019.
- Steve Ritz chaired P5 2014 and was a member of the Astro2010 committee.
- Scott Dodelson (P5 member) is an author of the CMB-S4 champion document arXiv:1309.5383.
- Saul Perlmutter (P5 member, LBNL) sat on the 2015 WFIRST-AFTA SDT.
- Kate Scholberg (P5 member) is an LBNE author and chapter editor in arXiv:1307.7335.
- Jim Strait: LBNE project director at P5 time (snippet only), CMB-S4 project director
  from July 2022 (confirmed in role May 2024 by AIP FYI).
- Lia Merminga (P5 member) is Fermilab director as of 2024.

## Per bet

### p5-2014-desi

Committee P5 2014, chair Steve Ritz (Appendix B). Champions at ranking: the DESI Snowmass
2013 white paper arXiv:1308.0847 (submitted 2013-08-04), authors Michael Levi, Chris
Bebek, Timothy Beers, Robert Blum, Robert Cahn, Daniel Eisenstein, Brenna Flaugher, Klaus
Honscheid, Richard Kron, Ofer Lahav, Patrick McDonald, Natalie Roe, David Schlegel. Later
titles from Fermilab news: Levi "DESI Director" (2018-02-12) and "project director"
(2021-05-17); Schlegel "DESI Project Scientist" (2018, 2021); Eisenstein "DESI Collaboration
Co-spokesperson" (2018-02-12); Risa Wechsler co-spokesperson (2018); Nathalie
Palanque-Delabrouille and Kyle Dawson co-spokespersons (2019-2021). Not verified on an
allowed host: Levi leading DESI since 2012 and Eisenstein co-spokesperson 2014-2020 (both
search snippets, wikipedia and cfa.harvard.edu). The DESI Final Design Report
arXiv:1611.00036 has a 292-name author list and no leadership statement.

### p5-2014-lbnf

Committee P5 2014, chair Steve Ritz. Host lab director Nigel Lockyer from 2013-09-03
(Fermilab news 2013-06-20), confident. LBNE collaboration leads at P5 time: Milind Diwan
(BNL) and Bob Wilson (Colorado State) as co-spokespersons, and Jim Strait (Fermilab) as
project director, all three `guess`: arXiv:1307.7335 (v3 2014-04-22) lists them under
"General Guidance" and names Wilson "Editor of the 2010 Interim Physics Report" but gives
no spokesperson or director title; the titles come from BNL newsroom, symmetry (2010-01-06,
"LBNE elects spokespersons"), colostate.edu and LBL news snippets, all blocked hosts.
Later leaders, confident from Fermilab news: Bertolucci interim chair of the DUNE
institutional board in January 2015 and co-spokesperson from 2022 (2023-03-20 article);
Mark Thomson co-spokesperson in role 2016-02-16, succeeded 2018-03-13; Andre Rubbia
co-spokesperson succeeded 2017-03-13; Elaine McCluskey LBNF Project Manager (2019-11-14;
the brief said project director, the article says project manager); Jim Kerby LBNF/DUNE-US
project director from 2024-06-04. Not found on an allowed host: the 2015 election of
Thomson and Rubbia (DUNE CDR arXiv:1512.06148 has them only in the author list) and the
"co-chair of the interim international executive board" wording for Bertolucci.

### p5-2014-cmb-s4

Committee P5 2014, chair Steve Ritz. Champion statement at ranking: arXiv:1309.5383
"Neutrino Physics from the CMB and Large Scale Structure" (Snowmass 2013, v3 2014-05-30),
topical conveners K.N. Abazajian, J.E. Carlstrom, A.T. Lee, 77 authors including Borrill
and P5 member Dodelson. Later leadership, confident: arXiv:1907.04473 (2019) org chart
names spokespeople Julian Borrill and John Carlstrom, interim project director Jim Yeck,
technical coordinators Jeff McMahon and Abby Vieregg, project managers Brenna Flaugher
and Mark Reichanadter; AIP FYI 2024-05-15 quotes Jim Strait (CMB-S4 Project Director,
LBNL) and Kevin Huffenberger (co-spokesperson). The brief's "Jim Strait, project director
2020" is wrong: LBL news snippet says effective 2022-07-11. The CMB-S4 Science Book
arXiv:1610.02743 (2016) has 86 authors, first author Abazajian, submitted by Carlstrom,
no editor statement. Agency: AIP FYI 2024-05-15 (NSF, May 7 2024, not "in its current
form", South Pole infrastructure) and AIP FYI week of 2025-07-14 (DOE and NSF will no
longer pursue CMB-S4).

### astro2010-wfirst

Committee Astro2010, chair Roger Blandford, vice chairs Martha Haynes, John Huchra,
Marcia Rieke, executive officer Lynne Hillenbrand (front matter, confirmed). EOS panel
chair Alan Dressler. Champions at ranking: Neil Gehrels, sole author of the JDEM-Omega RFI
response to the EOS panel (arXiv:1008.4936, posted 2010-08-29); David Bennett, lead
author of the MPF white paper to the PSF panel (arXiv:0902.3000, 2009-02-17); Daniel
Stern, lead author of the NIRSS RFI response to the EOS panel (arXiv:1008.3563,
2010-08-20). The brief's suggestion that NIRSS was a Perlmutter/JDEM team is wrong; NIRSS
was a JPL-led all-sky NIR survey (Stern, Bartlett, Brodwin, Cooray, Cutri, Dey, Eisenhardt,
Gonzalez, Kalirai, Mainzer, Moustakas, Rhodes, Stanford, Wright). Later: WFIRST-AFTA 2015
report arXiv:1503.03757 signed by SDT co-chairs David Spergel and Neil Gehrels, SDT
including Bennett, Dressler, Perlmutter, ex officio D. Benford (NASA Headquarters).
Guesses: Benford's "program scientist" title and McEnery's "senior project scientist"
title appear only in snippets (science.nasa.gov, wikipedia); arXiv:1902.05569 (2019)
lists both without titles. The AIP launch page (2026-08-30) is a Sky and Telescope
excerpt and names nobody.

### astro2010-lsst

Committee Astro2010, chair Roger Blandford. OIR ground panel chair Patrick Osmer.
Champions at ranking, confident from the LSST Science Book v2.0 arXiv:0912.0201 (November
2009) front matter: "J. Anthony Tyson, Director", "Donald W. Sweeney, Project Manager",
"Michael A. Strauss, Chair of Science Collaborations"; chapter 1 by Tyson, Strauss,
Ivezic. The reference design paper arXiv:0805.2366 (2008) is by Ivezic, Kahn, Tyson and
313 others including Wolff and Axelrod. Guesses (snippets only, lsst.org, SLAC and NOAO
blocked): Ivezic LSST Project Scientist; Kahn deputy director in 2010 and LSST Director
from 2013-07-01 succeeding Sidney Wolff; Wolff President of the LSST Corporation in 2010.

## URLs read

Fetched and read (allowed hosts):

- https://nap.nationalacademies.org/read/12951/chapter/1 (301 to
  https://www.nationalacademies.org/read/12951/chapter/1, read there): Astro2010
  committee, panel chairs, study director Michael Moloney
- https://www.usparticlephysics.org/wp-content/uploads/2018/03/FINAL_P5_Report_053014.pdf
  (local copy sources/p5-2014.txt lines 3310-3365, Appendix B)
- https://arxiv.org/abs/1308.0847 DESI Snowmass 2013 white paper
- https://arxiv.org/abs/1611.00036 and PDF: DESI Experiment Part I (author list only)
- https://arxiv.org/abs/1307.7335 and PDF: LBNE science document, contributor table
- https://arxiv.org/pdf/1110.6249 LBNE Science Collaboration 2011 (no leadership names)
- https://arxiv.org/pdf/1512.06148 DUNE CDR vol 1 (author list only)
- https://arxiv.org/pdf/1807.10334 DUNE Far Detector IDR (management structure, no names)
- https://arxiv.org/abs/1309.5383 and PDF: Snowmass CMB neutrino document, conveners
- https://arxiv.org/abs/1610.02743 CMB-S4 Science Book
- https://arxiv.org/abs/1907.04473 and PDF: CMB-S4 reference design, org chart
- https://arxiv.org/pdf/2203.08024 Snowmass 2021 CMB-S4 white paper (author list only)
- https://arxiv.org/abs/1008.4936 JDEM-Omega RFI response
- https://arxiv.org/abs/0902.3000 MPF white paper
- https://arxiv.org/abs/1008.3563 NIRSS RFI response
- https://arxiv.org/pdf/1503.03757 WFIRST-AFTA 2015 report, SDT list
- https://arxiv.org/pdf/1902.05569 WFIRST Astro2020 APC white paper, author list
- https://arxiv.org/abs/2505.10574 Roman ROTAC report (abstract names nobody)
- https://arxiv.org/abs/0912.0201 and PDF: LSST Science Book front matter
- https://arxiv.org/abs/0805.2366 and PDF: LSST reference design paper
- https://news.fnal.gov/2013/06/nigel-lockyer-canadas-triumf-lab-named-fermilab-director/
- https://news.fnal.gov/2016/02/test-of-dune-tech-begins/
- https://news.fnal.gov/2017/03/dune-collaboration-elects-university-chicagos-edward-blucher-new-co-spokesperson/
- https://news.fnal.gov/2018/03/dune-collaboration-elects-university-of-manchesters-stefan-soldner-rembold-as-new-co-spokesperson/
- https://news.fnal.gov/2019/11/fermilab-international-partners-break-ground-on-new-beamline-for-the-worlds-most-advanced-neutrino-experiment/
- https://news.fnal.gov/2023/03/mary-bishai-joins-sergio-bertolucci-as-co-spokesperson-of-dune/
- https://news.fnal.gov/2024/06/fermilab-names-jim-kerby-as-lbnf-dune-u-s-project-director/
- https://news.fnal.gov/tag/dune/page/46/ (2016-2017 index, nothing from 2015)
- https://news.fnal.gov/2018/02/installation-next-generation-dark-energy-experiment/
- https://news.fnal.gov/2019/10/desi-opens-its-5000-eyes-to-capture-the-colors-of-the-cosmos/
- https://news.fnal.gov/2021/05/dark-energy-spectroscopic-instrument-starts-5-year-survey/
- https://www.aip.org/fyi/the-week-of-july-14-2025
- https://www.aip.org/fyi/week-of-may-13-2024
- https://www.aip.org/fyi/nsf-delays-cosmic-microwave-background-experiment
- https://www.aip.org/news-and-analysis/aas/nasa-launches-nancy-grace-roman-space-telescope

Search snippets only (host blocked or not opened), used for `guess` rows:

- https://www.bnl.gov/newsroom/news.php?a=21561 (LBNE first spokespeople, Diwan, 2010)
- https://www.physics.colostate.edu/?p=2342 (Wilson co-leads LBNE with Diwan)
- https://newscenter.lbl.gov/2022/06/02/james-strait-named-project-director-of-next-generation-cosmic-microwave-background-project/
- https://www.lsst.org/about/team/lsst-project-scientist (Ivezic)
- https://www.lsst.org/sites/default/files/enews/kahn-201304.html (Kahn director 2013)
- https://www.lsst.org/sites/default/files/enews/kt-lim-1004.html (Wolff president 2010)
- https://science.nasa.gov/people/dr-dominic-benford/ (Benford program scientist)
- https://en.wikipedia.org/wiki/Julie_McEnery (McEnery project scientist)
- https://nsf-gov-resources.nsf.gov/attachments/114268/public/Gehreis_JDEM_update.pdf
  (Gehrels "JDEM Project Scientist", 2009)
- https://www.cfa.harvard.edu/people/daniel-eisenstein (co-spokesperson 2014-2020)

## Open gaps

1. LBNE co-spokesperson and project director titles at P5 time (Diwan, Wilson, Strait):
   need an open copy; the DOE FY2015 or FY2016 HEP budget justification may name the LBNE
   project director, not checked.
2. DUNE's first co-spokesperson election (Thomson, Rubbia, 2015): no Fermilab news page
   found; a CERN or symmetry page would have it.
3. Roman project scientist (McEnery) and program scientist (Benford) titles: NASA hosts
   blocked.
4. LSST 2010 titles for Ivezic, Kahn, Wolff: lsst.org blocked.
5. DESI 2014 titles for Levi and Eisenstein: only 2018 and later pages reachable.
