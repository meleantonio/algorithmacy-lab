# Choi, Y., Kang, E. J., Lee, M. K., & Kim, J. (2023). Creator-friendly algorithms: Behaviors, challenges, and design opportunities in algorithmic platforms. In *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems (CHI '23)* (Article, 22 pp.). ACM.

**Identifier:** doi:10.1145/3544548.3581386 · **Read depth:** partial (published ACM PDF as saved locally; the PDF carries no printed page numbers in the text layer, so locators are sections; main text read in full; appendices A.1–A.2 and the reference list skimmed only, not read) · **Source-tier:** proceedings · **Evidence basis:** direct_read · **Design and sample:** Study 1, semi-structured interviews, N = 14 Korean YouTube creators (5 female, 9 male, 20s–30s; 7 full-time, 7 part-time; interviews up to 2 hours); Study 2, four participatory design workshops with 12 creators (4 female; mean age 27.33, SD 4.05; mean session 112.25 min) and two UX-of-AI facilitators; thematic analysis by two researchers · **Parties modeled:** person–platform algorithm (creator and recommender), with viewers and advertisers named but not studied · **Facets:** I · **Read:** 2026-10-13

## What it argues

The authors ask how a platform could be "creator-friendly." From the interviews they model a cycle of expectation, behaviour and perception (Fig. 1, Section 5). Creators who expect the algorithm to help "work with" it: they chase trendy topics, exploit a "halo effect" after a hit (retitling, re-thumbnailing, making a series), tune to advertisers, and "running real-world experiments" on their channels (5.2.1). Creators who stop expecting help "work against" it, protecting creativity and channel identity or seeking income outside YouTube (5.2.2). Every participant reported a "blessing" (sudden view or subscriber surge) at least once, and several could not reproduce it (5.1.1). One participant "would prefer not to be blessed" after it distracted her (5.1.2). Three challenges follow: choosing a strategy under uncertainty, reading performance without explanation ("it is not transparent whether the return is due to their effort or due to the algorithmic impact," 5.3.2), and burnout and discouragement from repeating the cycle (5.3.3). A participant who took a three-month break felt the channel was "abandoned by the algorithm."

The workshops produce design wishes in three groups: foster diverse expression (declare channel identity to the algorithm; a "Discover New" slot for experiments), achieve success (an "algorithm test board" to simulate a video before upload; personalised "quest"-style suggestions), and sustain motivation (creator solidarity, strategy sharing, qualitative evaluation) (Section 7). In 8.4.3 the authors warn that "transparent and interpretable algorithms may sound like a panacea" but could push creators toward similar, algorithm-optimised content and fiercer competition. They also note that serving creators can reduce recommendation quality for consumers.

## Relation to the argument

This card bears on ruling D7 (understanding through acting) and premise P7. The creators act constantly and try experiments (5.2.1: a creator tests an eating-show topic, an entertaining title and her face on the thumbnail, and "did not see the desired results"), but the results are confounded with audience and algorithm effects they cannot separate (5.3.2). Acting did not by itself yield understanding; the participants themselves ask for tools that make the algorithm testable and explained. That fits Part 1's point that a mediator disrupts the rapid, unequivocal feedback learning needs. It also bears on P9 and ruling D3: the transparency the participants request is exactly the disclosure the author ranks as a literacy intervention, and the authors' own caution in 8.4.3 is a reason it may not change behaviour in the wanted direction.

On P10 (the owner's interests): the platform is a party with its own objective, advertisers and consumers, and the authors say creator goals "may not always be possible" to prioritise (8.4.3). The workshop wishes are proposals made to the platform, not constraints on it.

Facet check: the facet entry (read in part: abstract and 5.2.1) matches. The full text adds that the work-against turn is also driven by values, not only failed blessings (8.1), which the facet does not mention.

## In conversation with

- `devito2021adaptive` — NOT cited. The paper cites DeVito et al. 2018 (refs 27, 28, "How people form folk theories of social media feeds") and DeVito, Gergle and Birnholtz 2017 (ref 29, "Algorithms ruin everything") for folk theorization; the authors say little research covers folk theorization in the creator context and aim to fill it (2.2). The 2021 single-author DeVito paper in the bib is not in the reference list.
- `eslami2016first` — cited as Eslami et al. (ref 34) among folk-theory work (2.2, the folk-theory background).
- `cameron2024making` — not cited. The only Cameron item (ref 16) is Cameron, Christin, DeVito and others, 2021, "This Seems to Work", a CHI extended abstract, not the 2024 Administrative Science Quarterly article.
- Leads not in the bib: Wu et al. on creators' algorithmic personas (gatekeeper, drug dealer, agent); Ma et al. on demonetisation; Karizat et al. 2021 on TikTok identity; Zhang et al. on participatory redesign with drivers; Bishop 2018 on YouTube anxiety.

## Caution

Qualitative, self-report data; all participants are Korean-language creators recruited through a Korean creator forum, flyers, university boards and cold email, so selection is heavy (the authors say so in Section 9). Two workshop participants also took part in the interviews. Facilitators contributed ideas in the workshops. The creator proposals are wishes, not tested designs, and no outcome is measured. The authors write "four sessions"; there is no measure of whether any suggestion improves outcomes. The creative economy setting (self-chosen content, no fixed task) differs from a coordination mediated between two counterparts.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** published ACM PDF (choi2023creator.pdf, 22 pp., text layer, no printed page numbers so sections only); 16 quoted strings and the participant numbers (N = 14, 5F/9M, 7/7 full/part-time, N = 12 workshop, mean age 27.33, SD 4.05, 112.25 min, four sessions, two overlapping participants), reference-list entries 16, 27-29, 34.

**Findings:** (1) The In-conversation entry for `devito2021adaptive` was wrong: the paper does not cite that 2021 paper; refs 27-29 are DeVito 2018 (twice) and 2017. Rewritten. (2) The `cameron2024making` entry implied a possible match; ref 16 is a 2021 CHI EA item by Cameron et al., not the ASQ article. Rewritten. (3) "run real-world experiments" is not verbatim; source reads "running real-world experiments". Fixed. (4) Read depth changed from full_text to partial because the card says appendices and references were only skimmed. Other quotes match (ligature breaks only). `eslami2016first` (ref 34) confirmed.
