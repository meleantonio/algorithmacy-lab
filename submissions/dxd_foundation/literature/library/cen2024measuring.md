# Cen, S. H., Ilyas, A., Allen, J., Li, H., & Mądry, A. (2024). Measuring strategization in recommendation: Users adapt their behavior to shape future content. *Proceedings of the 25th ACM Conference on Economics and Computation (EC '24)*, 203–204 (extended abstract). Full paper: arXiv:2405.05596v1.

**Identifier:** doi:10.1145/3670865.3673634; arXiv:2405.05596 · **Read depth:** partial (arXiv preprint v1, 9 May 2024, 51 pp., the full paper behind the two-page EC '24 abstract; the arXiv page numbers are used below; I read pp. 1–34; the appendices, pp. 36–51, were skimmed and not read: balance checks, model specifications, regression tables, outcome distributions, survey wording) · **Source-tier:** preprint (the full paper); the published EC '24 item is a two-page extended abstract · **Evidence basis:** direct_read · **Design and sample:** online randomised experiment with a custom music player, 750 recruited from CloudResearch Connect, 657 analysed; 3 × 2 between-subjects design; post-study survey; analyses stated as pre-registered on AsPredicted · **Parties modeled:** person–system (one listener, one assumed recommender) · **Facets:** I · **Read:** 2026-10-13

## What it argues

Cen and colleagues test whether people shape what they do to what they believe an algorithm learns. They model a "strategic" user as one who picks behaviours to optimise utility over a horizon T > 1, so that behaviour depends on the believed algorithm and on the horizon (pp. 7–9). That gives two hypotheses: a different belief about the algorithm (Information condition) or a different horizon (Incentive condition) should change behaviour (p. 9).

The design is clean about one thing. Every participant hears two five-minute listening sessions with songs drawn at random from the same pool; the music never responds to behaviour (pp. 11–13). Only the instructions change. Half are told they will get personalised recommendations at the end (Incentive treatment). In the second session each hears one of three descriptions: no information, "the algorithm will pay more attention to likes and dislikes", or "more attention to dwell time" (§3.3, p. 13).

The headline: the abstract reports that those told the algorithm watches likes use likes and dislikes "1.9x more" than those told it watches dwell time (p. 1). In the body the Likes group makes 2.9 more likes-plus-dislikes than control (SE .7, p < .001) and the Dwell group 3.0 fewer (SE .7, p < .001); means are 11.7 and 6.4 (pp. 17–18). The Incentive treatment raises likes-plus-dislikes by 3.6 (SE .7), fast skips by 3.0 (SE .97, p = .009) and dashboard clicks by 6.9 (SE 2.6, p = .04), and shortens dwell time (p. 20–21). No Information × Incentive interaction appears (p. 21). The log-dwell-time variance effects are "suggestive" and do not survive multiple-comparison correction (p. 19).

Self-report adds colour: 53% say they "probably" or "definitely" changed behaviour between sessions (p. 25), and a ChatGPT coding of an open question puts about 47% as definitely strategizing on their own platforms, 28% not, 25% unclear (Table 6, p. 29). Reported tactics include liking songs they dislike to steer the feed, incognito browsing and separate accounts (pp. 28–29).

## Relation to the argument

D7 and P9. The paper measures how people act on a belief about the algorithm, and it shows that a one-sentence disclosure moves what they do. It does not show that acting teaches anyone how the algorithm works. The algorithm never responds, so participants had no feedback to learn from, and the authors set that question aside: "In most real-world platforms, users are not given explicit information about their algorithm's inner workings; instead, users learn how their algorithm works through repeated interaction" (p. 32). They call the accuracy of those inferences "out-of-scope" (p. 32).

D3 (disclosure). One sentence about the algorithm changed behaviour by large amounts. That cuts against the strong form of D3 ("disclosure of the algorithm doesnt affect our ability to navigate it"), at least if "navigate" includes acting on a belief about the algorithm. The study cannot say whether the beliefs were correct or the acts effective. The authors list as future work whether strategizing "actually improves users' utilities" (p. 33). It also shows the activity the paper wants conventions for: the survey tactics are the folk practice of people with no convention.

P7. The pairing of the two parties is person and platform; no counterpart in the triad appears.

Facet check: facet I read the two-page abstract and reported "1.9 more"; the full paper says "1.9x" and the body counts above. Its bearing line holds.

## In conversation with

In `../references.bib`, cited by Cen:
- `eslami2016first`, `devito2021adaptive`: evidence that users hold beliefs about recommenders, "a precursor to the phenomenon that we study" (p. 4).
- `rahman2021invisible`: freelancer strategization under opaque evaluation (p. 5).

Leads not in the bib: Cen, Ilyas & Mądry 2023 (the theory paper the experiment tests); Haupt, Hadfield-Menell & Podimata 2023; Kleinberg, Mullainathan & Raghavan 2022 (inconsistent preferences); DeVito et al. 2017, 2018.

## Caution

Music is a low-stakes domain; participants were told what the algorithm "pays attention to" and nothing in the study learns from them. The effect sizes mix true strategizing with demand effects, which the authors argue against but cannot remove (pp. 31–32). The 47% figure rests on ChatGPT classification of free text and a non-representative online sample (p. 26). The published EC '24 item is the abstract, not this text; cite the arXiv full paper for numbers, and check them against any later version.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** the arXiv v1 PDF (2405.05596v1, 51 pages) from the cards folder; title, authors, version match. About 30 numbers and quotations: 1.9x (abstract), 750 recruited and 657 analysed, AsPredicted registration statement, 2.9 and 3.0 effects with SE and p, means 11.7 and 6.4, incentive effects 3.6, 3.0 (SE .97, p = .009), 6.9 (SE 2.6, p = .04), dwell time effects, the no-interaction statement, the "suggestive" statement, 53% (p. 25), Table 6 (0.471, 0.283, 0.247; p. 29), and the quotations at pp. 4, 32 and 33 and the non-representativeness note at p. 26.

**Findings:** Read depth changed from full_text to partial: the card itself says the appendices (pp. 36-51, about a third of the document) were skimmed, so they are listed as not read. All numbers and quotations are exact. Minor: the body says 11.7 against 6.4 is "80 percent more" while the abstract says 1.9x; the card reports both correctly. I did not check the model section (pp. 7-9) line by line.
