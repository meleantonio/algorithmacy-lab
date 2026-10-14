# Li, L., Chu, W., Langford, J., & Schapire, R. E. (2010). A contextual-bandit approach to personalized news article recommendation. In *Proceedings of the 19th International Conference on World Wide Web* (pp. 661–670). ACM. https://doi.org/10.1145/1772690.1772758

**Identifier:** doi:10.1145/1772690.1772758; arXiv:1003.0146 · **Read depth:** full_text (arXiv v2 of 1 March 2012, 10 pp., which states "A version of this paper appears at WWW 2010"; read whole, including algorithms, Table 1, figure captions and references; pagination is the arXiv PDF's, so I give section locators; the WWW page range above is from the DOI record and was not checked against the proceedings PDF) · **Source-tier:** proceedings (peer-reviewed conference) · **Evidence basis:** direct_read · **Design and sample:** an algorithm (LinUCB) with an offline evaluation on logged traffic from the Yahoo! Front Page Today Module: about 4.7 million random-bucket events on 1 May 2009 for tuning and about 36 million from 3–9 May 2009 for evaluation · **Parties modeled:** person–system (a platform choosing which article to show each visitor; editors and article publishers in the background) · **Facets:** R4 · **Read:** 2026-10-14

## What it argues

Li and colleagues treat news recommendation as a contextual bandit: the system chooses an article, sees whether the user clicks, and must trade off exploiting what it knows against exploring what it does not. Their introduction describes what web services already did: "a small amount of traffic can be designated for such exploration. Based on the users' response (such as clicks) to randomly selected content on this small slice of traffic, the most popular content can be identified and exploited on the remaining traffic" (§1). Exploration has a cost to the people served: "Exploration can increase short-term regret since some suboptimal arms may be chosen" (§2.2).

The data themselves come from deliberate randomisation on a live platform. "We collected events from a random bucket in May 2009. Users were randomly selected to the bucket with a certain probability per visiting view. In this bucket, articles were randomly selected from the article pool to serve users" (§5.2.1). For evaluation it adopts a deployment design in which "one reasonable way is to randomly split all traffic to this page into two buckets": a small "learning bucket" where bandit algorithms explore and a "deployment bucket" served greedily from the learning bucket's estimates (§5.4). The paper offers this as a reasonable design and does not say it was Yahoo!'s production configuration. On the logged data, LinUCB raised click-through rate by about 12.5% over a context-free bandit (abstract; Table 1; the abstract describes the dataset as "over 33 million events", §5.2.1 as about 36 million), and UCB methods beat ε-greedy, which explores "uniformly at random" (§5.5.2). CTRs are reported only relative to a random policy "To protect business-sensitive information" (§5.4).

## Relation to the argument

**Premise P10 and the draft's account of mediated distortion.** The draft's line 279 says "No source I have found shows that a platform introduces noise or delay on purpose." This paper is a primary source, written by the platform's own researchers, showing a platform that randomises what it serves on purpose, as standard practice, to learn. Randomised exploration is stochastic allocation by design. It is not concealment and its aim is not to confuse anyone, but from the side of the person or the content owner on the receiving end, the platform's response to their behaviour contains deliberate random variation. The draft's statement should be revised or narrowed (for example, to "no source shows a platform adding noise in order to obscure its rules").

The paper also complicates the two-driver split at lines 278–279. Exploration noise is neither "strategic rule secrecy" nor "technical noise and latency" as the draft defines them: it is designed, and it serves the mediator's own objective J_M (clicks). That is a third driver the draft's taxonomy lacks.

**Use in DRAFT_v2:** This paper is not cited in DRAFT_v2.md. The draft's "Li (2017)" (lines 321, 498) is Shengwu Li's work on obviously strategy-proof mechanisms, a different work. The lines below are where the draft makes claims this source bears on.
- Line 279 ("No source I have found shows that a platform introduces noise or delay on purpose"): contradicts, for noise in allocation. Yahoo! served randomly selected articles to a randomly selected bucket of visitors in order to learn (§1, §5.2.1, §5.4). It does not speak to delay.
- Line 279 ("Algorithmic mediators introduce jitter, batching delays, and stochastic allocations. Not all distortion is intended"): supports the first sentence for stochastic allocation, and shows that this part of the distortion is intended.
- Line 281 ("Regardless of whether distortion originates in corporate strategy or system architecture, its cognitive result is the same"): complicates. Exploration is an architectural choice serving the mediator's objective, so the strategy/architecture line the draft draws does not hold for it.

## In conversation with

- `chen2015peeking` — the draft's other evidence on line 279 (Uber's surge jitter, by Uber's account a bug); this paper supplies the intended counterpart for recommendation.
- `rogers2021linkedins` — a second platform source on deliberate noise, there added to analytics returned to business users.
- `rich2018limits` — the human analogue: learners with choice-contingent feedback that do not explore fall into stable false beliefs; this paper is a platform paying a short-term cost to avoid the same trap in its own learning.
- Not in the bib, as leads: Agarwal et al. (2009), "Online models for content optimization"; Agarwal, Chen and Elango (2009), "Explore/exploit schemes for web content optimization"; Langford and Zhang (2008), epoch-greedy; Auer, Cesa-Bianchi and Fischer (2002) on UCB1.

## Caution

The parties here are a portal and its readers. The randomised party is the reader, and the paper does not discuss how readers or article providers perceive the variation. It is a 2009–2010 system; it shows that deliberate randomisation exists in deployed platforms, not that any gig or marketplace platform randomises allocation today. The offline evaluation assumes i.i.d. events and a uniform random logging policy (§4).

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the writer's saved copy (dxd_foundation_local/pdfs/r4c/li2010.pdf, arXiv:1003.0146v2, 1 March 2012, 10 pp., with the WWW 2010 notice) and searched the full extracted text. I matched the five quotations word for word with their sections (§1, §2.2, §5.2.1, §5.4, §5.5.2), and I checked the 4.7 million (1 May) and 36 million (3–9 May) event counts, the 12.5% lift and the relative-CTR reporting. I checked the reference record against Crossref (four authors, WWW '10, pp. 661–670, DOI) and re-read DRAFT_v2.md lines 278–281. I grepped the draft for "Li", "Langford" and "bandit".

**Findings:**
1. The card called the learning-bucket/deployment-bucket split Yahoo!'s "deployment practice". In §5.4 the paper presents it only as "one reasonable way" to deploy the methods, a motivation for its two evaluation metrics. Corrected. The random bucket used to collect the data (§5.2.1) is a deployed practice. That bucket and the §1 statement "In practice, we usually explore..." still support the card's claim that this platform randomised what it served on purpose.
2. The abstract gives the dataset as "over 33 million events", while §5.2.1 gives about 36 million. The card now records the discrepancy.
3. "Use in DRAFT_v2" did not say the source is uncited. The draft's Li (2017) is a different author and work, and I added that statement. On re-reading line 279, I agree with the verdicts: the source contradicts "no source ... shows that a platform introduces noise ... on purpose" for allocation noise, it does not speak to delay, and it complicates the two-driver split.
4. The quotations, the event counts, the reference record and the full-read claim (arXiv version, section locators) all check out.
