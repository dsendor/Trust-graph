# Sources

Primary documents the ledger is built from. The `.txt` files are what the models read;
the PDFs are not committed (size), so the hash lets anyone confirm they have the same file.

| File | Source | Fetched | sha256 of PDF |
|---|---|---|---|
| `p5-2014.txt` | P5, *Building for Discovery*, May 2014. [usparticlephysics.org](https://www.usparticlephysics.org/wp-content/uploads/2018/03/FINAL_P5_Report_053014.pdf) | 2026-09-25 | `d61a1c23...e104` |
| `pan-trimble-2024.txt` | Pan and Trimble, *An Overview of Seven Astronomical Decadal Surveys*, BAAS 56(1), 2024. Read from the open preprint, [arXiv:2311.02950](https://arxiv.org/abs/2311.02950); baas.aas.org refuses automated fetches | 2026-09-25 | `496aa390...55b4` |
| `astro2010.txt` | NRC, *New Worlds, New Horizons in Astronomy and Astrophysics*, 2010: Executive Summary and Chapter 7, from the [National Academies Press reader](https://nap.nationalacademies.org/read/12951/chapter/2). `=== PAGE n ===` are printed pages. Raw HTML (not committed) in `nwnh-html/` | 2026-09-28 | |
| `p5-2014-pdfpage27.png`, `...28.png` | Page images of P5 Table 1 and Figure 1, rendered with pypdfium2 so the adjudicator sees the real table layout | 2026-09-28 | |
| `pan-trimble-2024-astro2010.csv` | Hand transcription of their Table 2.3 (Astro2010 / Blandford items). `pt_category` is blank because they do not code Astro2010 rows individually | 2026-09-25 | |

Text extracted with `pypdf`, one `=== PAGE n ===` marker per PDF page.

## What Pan and Trimble give us, and what they do not

- **Five outcome categories** (their Section 2.3), carried into `outcomes.csv` as `pt_category`.
- **Per-row categories only through the 2001 report** (their Table 2.2). For Astro2010
  (Table 2.3) they list status text with no category, so coding Astro2010 is our work,
  not a citation.
- **Their Astro2010 count is inconsistent:** Table 2.3 totals 15 requests, the scorecard
  (Table 2.5) says 23 with categories 10 / 1.5 / 4 / 3.5 / 4. Cite the scorecard with that caveat.
- **Some statuses are stale** (Roman "2027?", Rubin "first light 2024"). Ours supersede them, with sources.
