# Kuhl, U., Artelt, A., & Hammer, B. (2023). Let's go to the Alien Zoo: Introducing an experimental framework to study usability of counterfactual explanations for machine learning. *Frontiers in Computer Science, 5*, Article 1087929.

**Identifier:** doi:10.3389/fcomp.2023.1087929 · **Read depth:** full_text (published open-access PDF, 17 pp.; page numbers below are the journal's printed "01"–"16" footers; I read the whole article; the supplementary tables and figures are not in the PDF) · **Source-tier:** peer-reviewed article, framework plus proof-of-concept study · **Evidence basis:** direct_read · **Design and sample:** two online experiments on Amazon Mechanical Turk (Masters workers), 45 recruited each, randomised to counterfactual-explanation (CFE) or no-explanation control; 39 analysed in Experiment 1 (19 control, 20 CFE) and 43 in Experiment 2 (21 control, 22 CFE); 12 feeding decisions per person · **Parties modeled:** person–system (a novice and a decision-tree model) · **Facets:** I · **Read:** 2026-10-13

## What it argues

Kuhl and colleagues build a web game, the Alien Zoo, to test whether counterfactual explanations help novices learn a hidden relationship. Players feed an alien pack by choosing leaves of five plants per turn; a decision tree, trained on synthetic data, sets the pack's growth (§2.1, §2.2.6). After every second feeding, the control group sees a summary of its last two choices and the resulting pack size. The CFE group sees that summary plus, for each choice, a counterfactual: an alternative choice that would have grown the pack more (§2.2.3). In Experiment 1 growth depends on three plants jointly; in Experiment 2, on two.

The authors give their design rationale: study designs in explainable AI usually let people "passively study pre-selected examples", but "interactive activities grant deeper understanding", so they build an iterative act-and-feedback task (p. 3, citing Chi & Wylie 2014).

Experiment 1: the control group never improved. "No user in the control condition managed to increase their pack size from the minimal attainable number of two by trial 12" (p. 10). The trial-by-group interaction is F(11, 407) = 6.649, p < .001, ηp² = .153; groups differ from trial 9 on (p. 10). When asked which plants mattered, CFE players matched the truth more often (relevant plants: 3.000 against 1.895, U = 281.5, p = .001) (p. 10). Experiment 2, with the easier structure: CFE players still outperform from trial 5 (interaction F(11, 451) = 32.748, p < .001), but some controls improve, and the knowledge-question difference disappears (p = .554) (p. 12). All of the CFE players in Experiment 2 but only 57% of controls identified the key plant (p. 15). Decision times fall in both groups and do not differ. Subjective helpfulness and usability are higher with CFEs in both experiments (pp. 11, 13).

The authors state a limit that matters here: "it is very unlikely that users are able to form an accurate mental model of the entire underlying system solely based on a sparse set of these specific explanations" (p. 16).

## Relation to the argument

D7 and facet I's "understanding through action". The control condition is the cleanest available test of acting and ingesting results with no contrast supplied. Players chose twelve times and saw the outcome each time. In the three-factor task they learned nothing. So the paper cuts against the plain form of D7 ("we understand THROUGH deciding and quickly ingesting the results") and supports a narrower claim: acting plus feedback that shows the better alternative. That narrower claim still rests on a feedback device (the CFE) that the person reads, which makes P9's pessimism about reading aids look weaker than the argument map allows. It also rests on a fixed, non-interested model.

P7. The Alien Zoo is the nearest thing in facet I to a convention-building aid: an artefact that carries the work of working out what to change. The design is a model for the paper's proposed experiment (D9 open question) but not evidence about a triad.

D3. Disclosure of the model's rule is not what is tested; the explanation is a derived display of one decision at a time.

Facet check: the facet's reading from the abstract is right. Added: the knowledge result does not replicate in Experiment 2, and the authors' account that interactivity explains a result that Lim et al. (2009) did not find is untested; they did not compare interactive with passive versions of the same task (p. 14).

## In conversation with

In `../references.bib`, cited by Kuhl:
- `poursabzi2021manipulating`: simulating a clear model does not make users follow it or spot its errors (p. 2).
- `warren2024categorical`: probably the journal successor of the Warren, Keane & Byrne (2022) preprint that Kuhl cites for a CFE-versus-causal comparison; I did not check the identity.

Leads not in the bib: Lim, Dey & Avrahami 2009 (what-if explanations gave no advantage in an earlier test); van der Waa et al. 2021; Chi & Wylie 2014; Keane et al. 2021 (review: one in three counterfactual-XAI papers has a user test); Lage et al. 2019.

## Caution

Small samples (39 and 43 analysed, after excluding 6 and 2 for quality flags), twelve trials, an abstract task for novices on a crowdwork platform, no transfer test and no long-run retention. The authors call it "a proof of concept" and warn that results may not generalise beyond "an abstract domain for novice users" (§2.1.5, p. 5). The model is stationary and benign; it does not adapt and has no interest of its own.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The published open-access PDF (Frontiers in Computer Science 2023, 5:1087929), extracted with pdftotext. I checked 9 verbatim quotations with their page numbers, and the statistics F(11,407)=6.649 with partial eta squared .153, F(11,451)=32.748, U=281.5 with p=.001 and the 3.000 against 1.895 means, p=.554, the 'from trial 9' and 'from trial 5' onsets, 45 recruited per experiment with 6 and 2 excluded (39 and 43 analysed), the 100% against 57% key-plant figure on p. 15, and the Lim et al. 2009 and Keane et al. 2021 passages.

**Findings:** No issues found. The two short quoted phrases tagged to facet I ('understanding through action' and the D7 wording) are the author's, not the paper's, and were not checked against the paper.
