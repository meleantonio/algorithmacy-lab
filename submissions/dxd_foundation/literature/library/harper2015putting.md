# Harper, F. M., Xu, F., Kaur, H., Condiff, K., Chang, S., & Terveen, L. (2015). Putting users in control of their recommendations. *Proceedings of the 9th ACM Conference on Recommender Systems (RecSys '15)*, 3–10.

**Identifier:** doi:10.1145/2792838.2800179 · **Read depth:** full_text (GroupLens author copy of the published 8-page paper; page numbers below are PDF pages 1–8, which I did not check against the ACM pagination) · **Source-tier:** proceedings · **Evidence basis:** direct_read · **Design and sample:** offline simulation on 4,976 MovieLens users, then an online user study of 168 tuner users (148 survey completers) · **Parties modeled:** person–system (user and recommender; no third party) · **Facets:** H · **Read:** 2026-10-13

## What it argues
Harper and colleagues give MovieLens users a single control over an item-item collaborative-filtering recommender. The final score is a weighted sum of the predicted rating and one non-personalised variable, popularity or item age (Eq. 2, §3), and the user moves the weight with left and right buttons (§5.1, Fig. 2). They ask whether users like control (RQ1), how far tuned lists differ from the originals (RQ2), and whether users converge on one best setting (RQ3) (§1).

The offline study (§4) uses a 5-fold holdout on users who joined in the preceding six months. It shows that a small weight on popularity or age moves the list a long way: blending in 5% popularity cuts the number of unique movies recommended across all users from 14.5k to 6.8k (§4.2).

The user study invites 2,023 existing MovieLens users; 381 click through and are assigned to a condition. Of these, 168 (8.3% of those emailed) meet the usage criteria and 148 (7.3%) finish the survey. The survey completers are heavy users: a median of 186 logins and 626 ratings, against 48 logins and 254 ratings for all those emailed (§5.2). Each click swaps four of the 24 movies shown, and the labels are deliberately neutral ("left", "right") so that users do not bring a prior about "newer" or "older" (§5.1).

Results. 85% of the 168 chose a setting at least one step from the origin and 15% kept the original (§5.2). The median user made 10 actions; in the popularity condition the median user replaced 12 of 24 movies, in the age condition 7 (§6). Tuned lists beat original lists on every survey item, all Wilcoxon p<0.001: more movies heard of (median 13 against 7) and more wanted (median 9 against 5) (Table 3). In the popularity condition the share rating the list "just right" on obscurity rose from 31% to 49% (Fig. 5, read from the plotted percentages). Users did not converge: 15% in the popularity condition and 17% in the age condition chose negative weights, which the authors call "surprising" (§6, RQ3). Users rated the interface hard to use (median "disagree" to "easy to use"), and the authors attribute much of that to their own obfuscated labels (§6).

## Relation to the argument
Candidate evidence for premise P9 (aids that hand the person something to tune show weaker, more mixed effects on what people do). The study supports part of that and cuts against another part. The outcome measures are perceptions of the list, not choices or welfare, so the paper shows satisfaction with a tuned list and nothing about decision quality; the author's "willingness is not performance" caution applies. Against P9's "weaker": the effect on perception is large, and the authors say the divergence in preferred settings (RQ3) shows why one fixed mediator rule cannot suit everyone. That divergence is the most useful finding for a mediated-triad argument: a control moves work to the person, and different people use it differently.

The setting is a dyad (user and platform operating on the user's own recommendations). The platform here is MovieLens, a research site with no commercial interest in the ranking, so the paper cannot speak to ruling D8 or P10 (an owner whose interests differ from the user's).

Facet check: facet H records 381 assigned, 168 used the tuner and 148 surveyed, and the 8% self-selection; my reading agrees. It also notes the heavy-user skew (median 186 logins); confirmed in §5.2.

## In conversation with
Its own text cites, among works outside this bib: Tasteweights (Bostandjiev et al., reference [2]) as prior evidence that control raises satisfaction, critiquing recommenders (§2), and the Netflix linear-ensemble description. Within `references.bib`, I found no entry the paper cites by name. Related bib entries, not cited by this paper: `knijnenburg2012inspectability` (control in social recommenders), `jannach2017user` and `he2016interactive` (surveys of user control), `vaccaro2018illusion` (placebo controls). Leads not in the bib: Bostandjiev, O'Donovan & Höllerer 2012 (TasteWeights); Ekstrand et al. 2014 on algorithm differences.

## Caution
Self-selected power users (8% of invitees); one site, one domain (movies), two attributes; the authors call their own interface poorly rated for usability (§6.1). No behavioural outcome. The paper's "N=168" and "N=148" are the analysed groups, not the 381 who started.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened cards/harper2015putting.pdf (GroupLens author copy, 8 pp.), extracted text and rendered page 6 to read Figure 5. Checked the card's in-source quotations (all matched) and about 35 numbers: 4,976 offline users, 14.5k to 6.8k at 5% popularity, 2,023 invited / 381 assigned / 168 / 148 and the 8.3% / 7.3%, medians 186 / 626 vs 48 / 254, four of 24 movies per click, 85% / 15%, median actions 10 (12 pop, 10 age), movies changed 12 and 7, Table 3 medians (13 vs 7; 9 vs 5), 15% / 17% negative weights, the usability median and the obfuscated-label explanation. Not checked: the Netflix description and the bib entries the card says are not cited by the paper (absence only spot-checked by name).

**Findings:** One fix: the card said the share rating the popularity list 'just right' rose from 26% to 49%. Figure 5 shows 31% for the original list and 49% for the tuned list (26% is the tuned list's share on the too-obscure side). Corrected to 31% to 49%. Everything else matches.
