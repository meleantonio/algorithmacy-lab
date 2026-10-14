# Engel, D., & Malone, T. W. (2018). Integrated information as a metric for group interaction. *PLOS ONE, 13*(10), Article e0205335. https://doi.org/10.1371/journal.pone.0205335

**Identifier:** doi:10.1371/journal.pone.0205335 · **Read depth:** full_text (published open-access PLOS ONE PDF, 19 pp., article-page numbering "n / 19"; local copy `dxd_foundation_local/pdfs/P/engel2018.pdf`. I read the whole text, Table 1, the supporting-information captions and the reference list; the S-tables and S-figures themselves (DOCX files) were not opened, and Figures 1–5 I read through captions and the text that reports them) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** three observational studies with an estimated Φ. Study 1: 68 four-person groups from an earlier collective-intelligence study (Boston, 2012), half face-to-face and half text-chat only, state = who was speaking (200 ms bins) or who posted each chat line; Study 2: edit histories of 999 Wikipedia Vital Articles, state = who edited at each edit step; Study 3: one minute per sampled month of CAIDA backbone traffic (San Jose, 2008–2014), 100-node subsamples · **Parties modeled:** other (groups of peers; in Study 3 machines; no mediator with its own objective) · **Facets:** P, T (§8) · **Read:** 2026-10-14

## What it argues

Engel and Malone propose integrated information, "phi", as a metric for group interaction because it captures "in a single mathematical quantity, two properties … differentiated information and integration" (abstract, p. 1). They do not compute Tononi's theoretical Φ. Because for that "a complete model of the rules governing state transitions in the system is needed", which observational data rarely supply, they use "two alternative versions of phi suggested by Barrett and Seth", which "estimate conditional probabilities for state transitions from the actual observed data" (p. 3). They name later work pointing out "limitations of (and possible corrections for) these versions" (p. 3).

- **Study 1.** Φ_E ("empirical phi") with the minimum information bipartition, computed on a binary who-is-active state vector (pp. 10–11). The lag for face-to-face groups was the one that maximised average Φ, "a clear peak at around 2 seconds" (p. 5; Fig 1); chat groups used a one-line lag (p. 11). Φ was normalised by condition and pooled: "an overall correlation of r = 0.370 (p = .003) between collective intelligence and phi" (p. 11; also p. 5). Dropping one borderline outlier leaves r = .290, p = .025 (p. 11). The methods describe "68 groups of four people" (p. 10), but the hierarchical regression in S4 Table is captioned "n = 61 groups" (p. 16); the paper does not state the n for the pooled r.
- **Study 2.** Φ_AR with "atomic" partitions (each editor its own part), validated against the bipartition version on articles with ≤14 editors (r = 0.83, p. 12). Quality predicts Φ controlling for editors and edits per editor (F = 3.6847, p = 0.0053, p. 6). When Φ_AR was unstable or out of range (19.5% of cases), they dropped the 5% lowest-variance nodes and reran (p. 13).
- **Study 3.** Φ over Internet traffic rose over six years (β = 1.779, p < 0.0001 for one setting, Fig 5, p. 7; Table 1 shows similar coefficients for three of four sampling methods, not for random-node sampling, p. 15). Invalid values occurred in 67.14% of cases before the node-dropping correction (p. 15).

Limits they state: "we assume, but do not test for, stationarity" (p. 11); "other metrics would have predictive power similar to that of phi and be simpler to compute" may exist, and comparing them is "an important task for future research" (p. 9). They read Φ as "a potential metric of effective group collaboration" (abstract, p. 1) and say it "at least sometimes, predicts group performance" (p. 1).

## Relation to the argument

**Ruling D9 and premise P11.** This is the one application of an integrated-information measure to human groups that the facets found. It supports the claim that Φ-family measures can be computed on coded human interaction and can track an outcome. It does not support Φ as a gauge of irreducibility in the IIT sense: the measures are Barrett and Seth's observational estimates, the lag was tuned to maximise Φ, and the authors use the number as a predictor of performance, not as a test of whether the group is reducible. Nothing in it involves a mediator, so it says nothing about a triad with an interested third party. It is the precedent and the cautionary example for the pre-specification that DRAFT_v2 line 450 promises.

**Use in DRAFT_v2:**

- **Line 450** ("Engel and Malone (2018) computed a proxy on who was active when in 68 groups and found it correlated with collective intelligence (r = .37), in groups with no mediator"). **Supported, with two qualifications.** "Proxy" and "who was active when" match pp. 3 and 10–11; r = .370 matches p. 11. (a) "68 groups" is the study's sample (p. 10); the analysed n may be 61 (S4 Table caption, p. 16), and the paper does not give the n beside r. Safer: "in four-person groups from a 68-group study". (b) "No mediator" is right in the sense that matters to the paper: no third party with its own objective. Half the groups did communicate only through a text-chat system (p. 10), which a reader might call a mediating channel. The draft's next clause, that "Barrett et al. (2026) note that Φ itself has not been computed on a real physical system", is not from this source.
- The draft's plan to "fix the measure, the coding … the time lag, and the partition in advance" answers exactly the choices Engel and Malone made after looking at the data (lag by maximum Φ, p. 5 and p. 14; low-variance nodes dropped until a valid value appeared, p. 13).

## In conversation with

- `barrett2011practical` — the source of Φ_E and Φ_AR, cited as [23] (p. 3, p. 10, p. 12); Barrett also supplied the MATLAB toolbox (Acknowledgments, p. 17).
- `mediano2019measuring` — not cited (later); belongs to the line on correcting empirical Φ measures that Engel and Malone point to through Oizumi et al. 2016 and Tegmark 2016 ([24, 25], p. 3).
- `albantakis2023integrated` — not cited (later); IIT 4.0, whose interventional Φ these observational estimates do not compute.
- `barrett2026integrated` — not cited (later); the draft pairs it with this source at line 450.
- Not in the bib, as leads: Woolley et al. (2010), *Science*, the collective-intelligence factor ([36]); Engel, Woolley, Jing, Chabris & Malone (2014), *PLOS ONE*, the source of the Study 1 data ([35]); Oizumi et al. (2016) and Tegmark (2016) on limits of these Φ estimates ([24, 25]); Balduzzi & Tononi (2008) ([13]).

## Caution

Correlational; one lab sample of 68 (or 61) groups, Wikipedia histories and backbone traces. The measures are Barrett and Seth's 2011 empirical estimates, not IIT 3.0 or 4.0 Φ, and Φ_AR can return negative or impossible values, handled here by dropping nodes. Lags and time-step sizes were chosen to maximise Φ. Stationarity untested. No comparison with simpler metrics (participation equality, turn-taking counts), which the authors flag. Do not cite it as showing that Φ measures irreducibility, collaboration quality or anything about mediated triads.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's local copy (`dxd_foundation_local/pdfs/P/engel2018.pdf` / `.txt`, PLOS ONE open-access PDF, pages "n / 19") and located every quotation and number by page: abstract (p. 1); Barrett and Seth versions and the later corrections [24, 25] (p. 3); 2-second peak (p. 5, Fig 1); quality F = 3.6847, p = 0.0053 (p. 6); β = 1.779 (p. 7); "other metrics … an important task for future research" (p. 9); 68 groups of four and the text-chat condition (p. 10); r = 0.370 (p = .003), r = .290 (p = .025), the stationarity assumption and the one-line chat encoding (p. 11); r = 0.83 and atomic partitions (p. 12); 19.5% and the 5% node-dropping (p. 13); time step chosen to maximise phi (p. 14); 67.14% (p. 15); S4 Table caption "n = 61 groups" (p. 16). Checked the record against Crossref (David Engel, Thomas W. Malone; PLOS ONE 13(10), e0205335, 2018). Re-read DRAFT_v2.md line 450 and the reference at line 555.

**Findings:**

1. Misquotation: the paper does not say phi "requires a complete model of the rules governing state transitions"; it says "a complete model of the rules governing state transitions in the system is needed" (p. 3). Fixed; meaning unchanged.
2. Page error: β = 1.779 (Fig 5) is reported on p. 7, not p. 6. Fixed.
3. Page error: the "other metrics … simpler to compute" and "an important task for future research" sentences are on p. 9, not p. 8. Fixed.
4. All other numbers and quotations verified, including the n = 61 caption against the 68-group sample, which the card correctly flags.
5. Use-in-DRAFT_v2 verdict on line 450 confirmed: "proxy" (Barrett and Seth's observational estimates, p. 3), "who was active when" (binary speaking or chat state, p. 11) and r = .37 (p. 11) are supported; "68 groups" is the study sample while S4 Table reports n = 61 for the regression; half the groups communicated only by text chat (p. 10). The paired Barrett et al. (2026) clause is not from this source. Read depth (full text, figures via captions) is consistent with the copy.
