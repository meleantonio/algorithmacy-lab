# Matsuo, R., Liu, H., Hiraoka, T., & Wada, T. (2026). An educational human machine interface providing request-to-intervene trigger and reason explanation for enhancing the driver's comprehension of ADS's system limitations. *IEEE Transactions on Human-Machine Systems, 56*(3), 650–661.

**Identifier:** doi:10.1109/THMS.2026.3679748; arXiv:2602.11507 · **Read depth:** full_text (arXiv v2, 21 Apr 2026, 12 pp., IEEE two-column layout; the page numbers I cite are the manuscript's own and do not match the journal's 650–661; the figures on pp. 9–10 viewed as rendered images) · **Source-tier:** peer-reviewed article (author preprint) · **Evidence basis:** direct_read · **Design and sample:** between-group driving-simulator experiment; 45 licensed Japanese drivers aged 22–28 (mean 23.36, SD 1.42; 31 men, 14 women) with no experience of automated driving, 15 per group; 14 trials per participant, 13 learning trials and one test trial · **Parties modeled:** person–system (driver and a level 3 automated driving system) · **Facets:** H · **Read:** 2026-10-13

## What it argues
A level 3 system hands control back with a request to intervene (RtI) when it nears the limits of its operating design domain, and a driver who cannot tell which condition triggered it may hesitate (p. 1). The authors test a voice interface that adds to the RtI (a) a trigger cue ("Thick fog, take over!") and (b) a spoken reason, delivered after the driver re-engages the system ("The reason for RtI is that it is difficult to recognize lanes and vehicles ahead in thick fog..."), 5 seconds after reactivation (§II, p. 3). The comparison groups hear "Take over!" only, or the cue without the reason. All groups read the same manual first. The system limits were a curve radius under 230 m and visibility under 40 m; fog and curve conditions were crossed so that a driver could see two plausible triggers (Table I, p. 6).

The final trial is the test: on a sharp curve (R = 150 m) the RtI fails, and a driver who has not taken over about 1.5 seconds after the system switches off hits the guardrail (§IV-D, p. 7).

Results (45 participants):
- **Workload.** NASA-TLX showed no difference between groups (Kruskal–Wallis H = 1.702, p = 0.427; Fig. 8, p. 9).
- **Comprehension.** On a 13-item test, medians were 13 (cue and reason), 12 (cue only) and 9 (neither). Cue and reason beat neither at U = 192.5, adjusted p = 0.001 (Hedges' g = 1.534), and beat cue only at p = 0.017; cue only beat neither at p = 0.047 (Table III, p. 9).
- **Collisions in the failure trial.** Per Fig. 10 (p. 9), 7 of 15 collided with no cue, 6 of 15 with the cue only, and 1 of 15 with cue and reason (Fisher 2×3, p = 0.044).
- **Timing.** Take-over time differed (ANOVA F = 5.715, p = 0.006); only cue and reason against neither was significant (Tukey p = 0.005, g = 1.381). Per Fig. 12 (p. 10), 12, 5 and 4 of 15 took over before the system switched off in the cue-and-reason, cue-only and neither groups.
- Comprehension and take-over time correlate at Spearman r = 0.350, 95% CI [0.06, 0.58], p = 0.018 (Table V, p. 10).

The authors write that the correlation "does not support causal interpretation" and that unmeasured factors such as driving skill and trust cannot be excluded (p. 11).

## Relation to the argument
**P9, complicated.** The argument map says interventions that give the person something to read show weaker, less consistent effects on what people do (P9). Matsuo et al. report a reading intervention with a behavioural outcome (collisions 1 of 15 against 7 of 15). Three conditions limit how far this goes. The effect needs the reason, not the cue (cue only gave 6 against 7 collisions, no significant timing gain; pp. 9–10). The measure of comprehension was written by the authors from the training scenarios. And the drivers were trained for 13 trials in the same two limits before the test, so this is a learning design, not a one-shot display.

**D7 (understanding through deciding).** The design fits the author's idea partly: the reason is delivered after the driver acts and re-engages, so understanding is built from repeated decide-and-see trials, not from reading ahead. That is a better match than most reading interventions, but it is a dyad, a person and one fixed system with stated limits.

**P7 and P10.** The system's limits are fixed numeric thresholds (230 m, 40 m) stated in a manual. A coordination mediated by an adaptive, interested system (P7, P10) offers no such stable threshold to learn, and the paper does not test one or ask what happens when a threshold changes.

Facet check: facet H lists "n not in abstract". The full text gives N = 45 (15 per group) and the collision counts above. The facet's reading "trigger cues and reasons improved comprehension of limits and cut collisions" overstates the cue: the cue alone gave a small, non-significant timing change and 6 against 7 collisions. The reason carried the result.

## In conversation with
- `boelhouwer2019should`: the authors cite it (ref. [28]) as finding that user manuals did not help participants decide whether to take over; this study adds an education step after each event.
- Leads, not in the bib: Zhou, Itoh & Kitazaki (2021), "How does explanation-based knowledge influence driver take-over in conditional driving automation?" (ref. [12]); Wright et al. (2018), cues that name the hazard (ref. [25]); Körber et al. (2018) on post hoc explanation of take-over requests (ref. [30]); Merriman et al. (2023), video training and mental models (ref. [40]).

## Caution
Small groups of young Japanese drivers in a simulator, with a fixed scenario order and no non-driving task. The authors flag all of these and the 10-second time budget (p. 11). The test trial's failure case was one scenario. Statistics are across three groups of 15, with multiple outcomes and non-normal data. I read the arXiv v2 manuscript, so the journal's edits are not seen. The Fig. 12 counts are read from the rendered figure.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened arXiv:2602.11507v2 PDF (title, authors, 21 Apr 2026 match) and viewed pp. 9-10 as images. Checked 5 quotations and about 40 numbers: sample, groups, thresholds, Kruskal-Wallis, Mann-Whitney U and adjusted p values, Hedges' g, Fisher, ANOVA, Tukey, Spearman, Fig. 10 collision counts (7, 6, 1 of 15), Fig. 12 counts (4, 5, 12), and the cited references (Boelhouwer, Zhou, Wright, Koerber, Merriman 2023).

**Findings:** No issues found. The 'n not in abstract' and 'trigger cues and reasons improved comprehension...' phrases are the facet's wording, quoted as such.
