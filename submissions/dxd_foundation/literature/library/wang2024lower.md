# Wang, S., Huang, S., Zhou, A., & Metaxa, D. (2024). Lower quantity, higher quality: Auditing news content and user perceptions on Twitter/X algorithmic versus chronological timelines. *Proceedings of the ACM on Human-Computer Interaction, 8*(CSCW2).

**Identifier:** doi:10.1145/3687046 (arXiv:2406.17097) · **Read depth:** full_text (arXiv v1 preprint of 24 Jun 2024, 24 pp. in the CSCW '24 template; page numbers below are that template's. I read the body, sections 1 to 7, and checked the reference list for the works named below; appendices A.1 to A.3, the full survey and the demographic charts, were not read) · **Source-tier:** peer-reviewed article (preprint read) · **Evidence basis:** direct_read · **Design and sample:** preregistered "sociotechnical audit", a three-week field experiment on real Twitter/X users: one week of observation, then one week forced onto the algorithmic "For You" timeline and one week onto the chronological "Following" timeline, order randomised per user; N = 243 Prolific users (68% male, 62.5% lean Democrat) from 822 onboarded; 846,494 tweets analysed; run November and December 2023 · **Parties modeled:** person–system (user and platform feed), with the researchers as the intervening party · **Facets:** H · **Read:** 2026-10-13

## What it argues

Wang and colleagues ask two questions at once. The algorithm audit asks what news each timeline shows. The user audit asks how users behave and what they think when forced onto one. A Chrome extension logged every tweet that reached the browser viewport and enforced the timeline on the home page (p. 6–7).

Algorithm-audit results (pp. 10–11):
- News density: 3.26% of tweets in the chronological condition against 0.94% in the algorithmic (H1 confirmed). In the observation week 1.6% of tweets in the algorithmic timeline held a news link against 7.5% in the chronological one (p. 10).
- Ideological congruence: more congruent news in the chronological condition (β = 2.82, SE = 1.11, p = .031); this reverses the hypothesis that the algorithm would amplify like-minded news.
- Extremity: more extreme sources in the chronological condition (β = 1.219, SE = 0.364, p = .003).
- Reliability: no significant difference between conditions (p. 10).

User-audit results (pp. 11–13):
- Users saw more news-link tweets in the chronological condition (β = 30.3, SE = 8.72, p = .002) and loaded more tweets overall in the algorithmic condition (β = 709, SE = 157, p < .001) (p. 11). They engaged with more tweets there (β = 19.75, SE = 5.32, p < .001) but not with more news tweets (β = −0.31, n.s.).
- Perceptions: satisfaction with the Twitter/X experience was higher in the unforced observation week (M = 3.38 on a 5-point scale) than in the chronological (3.23) or algorithmic (3.21) week, F(2, 432) = 4.54, p = .011 (p. 12). Perceived bias of one's own timeline tracked actual bias (β = 0.85, p < .001), but exposure did not move beliefs about whether the platform favours liberals or conservatives (β = −0.01, n.s.) or credibility and trust (F(2, 388) = 0.67 and 1.37, n.s.) (pp. 12–13).

The authors' headline is "lower quantity but higher quality" of news in the algorithmic timeline, and a gap between behaviour and perception: the authors saw "swift and sizable changes in user behavior" alongside "tremendous stability of user perceptions" (p. 14). In the observation week 43% of participants used both timelines (p. 10), and the authors read the satisfaction drop as the loss of that choice: users "became disappointed when losing that agency" (p. 15).

## Relation to the argument

**P9 and the behaviour/perception split.** This is a good case for the point behind P9 that what people report differs from what they do. The intervention changed exposure and engagement measurably; it changed little in stated attitudes. A caution runs the other way for the argument map: the study intervenes by forcing a feed on users, not by giving them a control, so it tests the effect of the algorithm and not the effect of a control surface.

**P10 and D8 (who holds the convention; exit and voice).** The observation week shows ordinary users switching between a default algorithmic feed and a chronological one, and the satisfaction drop when the researchers removed the choice. That is evidence for the value of a user-held switch. It also shows the limit: the choice exists at the platform's pleasure, and the authors note the algorithm itself may have changed after the platform's takeover, so "it is unclear to what extent these findings are due to intentional platform-level algorithm adjustment" and whether the algorithms "remain stable in the coming months and years" (p. 14). The owner can alter the thing the users choose between.

**Third party.** The platform feed is a third party in the sense of the argument, but the paper audits the feed as an object and models no joint task between two people.

Facet check: the facet says "243 users, randomised algorithmic versus chronological timelines, crossover; behaviour changed, perceptions of the platform barely." This matches. The full text adds a point the facet's phrasing could hide: the abstract says "slightly more reliable" news in the algorithmic timeline, but the results report no significant difference in reliability (p. 10), so the headline "higher quality" rests on lower congruence and extremity only.

## In conversation with

From the source's text and reference list:
- `guess2023how` — the Meta-collaboration experiment with randomised feeds (ref. 21); Wang et al. report a different result for Twitter/X, a moderating algorithm, from Facebook, where Guess et al. found none (p. 14).
- Lam et al. 2023, "Sociotechnical audits" (ref. 28), the method they extend. Not in `../references.bib`.
- Huszár et al. 2022, algorithmic amplification of politics on Twitter (ref. 26), the other randomised-exclusion study. Not in the bib.
- Eslami et al. 2015, "I always assumed that I wasn't really that close to [her]" (ref. 12), cited for lay awareness of curation. The bib's `eslami2016first` is a different paper by the same lead author, so this one is a lead, not a bib match.
- Bandy and Diakopoulos 2021 (ref. 4), Bakshy, Messing and Adamic 2015 (ref. 2) and Milli et al. on Twitter's algorithm and anger (ref. 39) are the main priors.

## Caution

A three-week, desktop-only study of US Prolific users with a left-leaning, male sample; the forced condition is a research intervention and not ordinary use. The authors list possible carry-over between weeks and awareness effects (p. 15). The platform's algorithm was in flux after the 2022 takeover. News quality is scored at the source level by Ad Fontes ratings, and tweets without news links, the large majority, are outside the outcome. Preprint v1; the published version may differ in wording and pagination.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the arXiv v1 preprint PDF (24 pp.; printed page numbers equal PDF pages). Checked 9 quotations (all exact), about 30 numbers (percentages, betas, SEs, p-values, F statistics, N = 243 of 822, 846,494 tweets, 68%/62.5%), and the Guess, Lam, Huszar, Eslami, Bandy, Bakshy and Milli references.

**Findings:** Locators were wrong by one page throughout the results and discussion sections, though every quotation and number was right. Fixed: news density, congruence, extremity now pp. 10-11 / 11; 1.6% vs 7.5% news-link share and the 43% both-timelines figure are p. 10, not 9; user-audit results pp. 11-13; satisfaction p. 12; credibility and trust pp. 12-13; 'swift and sizable' / 'tremendous stability' p. 14, not 13; 'unclear to what extent' / 'remain stable' and the Facebook divergence from Guess et al. p. 14, not 13; 'became disappointed when losing that agency' p. 15, not 14; carry-over and awareness limitation p. 15. Not checked: the appendix survey items beyond the 5-point scale wording, as the card states. The 'five-point scale' for satisfaction is confirmed in Appendix A.1. Milli et al. is in the reference list; 'anger' appears only in its title.
