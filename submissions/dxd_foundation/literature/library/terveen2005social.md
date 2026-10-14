# Terveen, L., & McDonald, D. W. (2005). Social matching: A framework and research agenda. *ACM Transactions on Computer-Human Interaction, 12*(3), 401–434. https://doi.org/10.1145/1096737.1096740

**Identifier:** doi:10.1145/1096737.1096740 · **Read depth:** full_text (the published article as a 34-page PDF with the journal's running heads and pagination, pp. 401–434, posted by the GroupLens lab at files.grouplens.org/papers/Terveen-SocialMatching.pdf; ACM lists the article as closed. I read the whole text and searched the reference list; Fig. 1 seen through its caption) · **Source-tier:** peer-reviewed article (framework and research agenda) · **Evidence basis:** direct_read · **Design and sample:** none (conceptual framework, survey of systems, social-science review, eight claims with research questions) · **Parties modeled:** two parties + third party (a system that matches people to each other and introduces them) · **Facets:** H · **Read:** 2026-10-14

## What it argues

Terveen and McDonald argue that "social matching systems", which recommend people to each other, are a class of their own and not just recommenders for a different item. "Recommending people fundamentally changes the game" (pp. 403–404): personal information is revealed, so privacy, trust, reputation and attraction matter more. Their process model has "four main steps": modeling the users who can be matched, matching them on request or opportunity, introducing matched users, and their interaction, with feedback to the system (Fig. 1, p. 404). They survey expertise recommenders, information systems with implicit matching, and opportunistic matching (pp. 405–409), and review social-science work on attraction, settings, networks, participation and cooperation (pp. 410–414).

The bulk of the article is a research agenda "organized around a set of claims [Erickson 2003]" (p. 414). The authors say what the claims are: "We expect some of the claims to be controversial, and we cannot prove that any of them are true" (p. 414). They were written "to capture our intuitions about what is most likely to be true, and to articulate interesting questions" (p. 414). There are eight, each followed by numbered research questions. Two bear on this project. Claim 2: "Social matching algorithms necessarily embody a model of what makes a good match; making that model explicit leads to better matches" (p. 414); explicit models "will make systems less opaque to users" (p. 416). Claim 3 itself is positive ("Social networks are a useful tool for social matching", p. 414, with egocentric networks preferred to whole ones), but its discussion is "cautious about approaches where large networks or long referral chains are visually presented to users as decision aids": "it has not been established that social network diagrams help users select others with whom to interact" (p. 418). A footnote on public reputation adds: "Making social behavior visible is not the solution to every socio-technical dilemma or trade-off" (p. 427).

They distinguish matching from social visualization: visualizations "leave interpretation and decision-making up to the users", while matching systems "attempt to ease decision-making by identifying specific people" (p. 409). eBay's reputation system appears as the case of cooperation through a third party: such systems "seek to establish the shadow of the future" (p. 414, quoting Resnick et al. 2000).

## Relation to the argument

**The form the draft borrows.** The draft takes Terveen and McDonald's agenda-by-claims as its model. Their claims are stated beliefs with research questions attached; the authors concede none can be proved (p. 414), and several are design imperatives ("Designers must consider ..."), not testable predictions. The draft's own addition, claims "stated so that data could count against it", is stricter than the model it cites. That is a defensible choice, but it is the draft's standard, not Terveen and McDonald's.

**Content that bears on the argument.** This is an early HCI account of a system that mediates between two parties: matching people, introducing them and taking feedback on the match. It supports the draft's premise that HCI has studied third-party mediation of two people (P11) at least as a design space. Claim 2 cuts in two directions for D3: it recommends making the matching model explicit, a disclosure, and expects better matches from that, but the reason given is that designers should build on explicit social-science models, with user-facing transparency as a side benefit (p. 416). The caution under Claim 3 about whole-network diagrams (p. 418) and the footnote on p. 427 side with the draft: showing people the network or making behaviour visible does not by itself help them act.

**P12.** The matching system here has no objective of its own beyond good matches; commercial dating sites are described, not analysed as interested parties. The paper does not anticipate the interested mediator of P12.

**Use in DRAFT_v2:**
- **Line 447** ("In the manner of a framework and research agenda (Terveen & McDonald, 2005), I set out four claims, each stated so that data could count against it"). Supported as a model of form: the article is a framework plus an agenda "organized around a set of claims" (p. 414). The clause "each stated so that data could count against it" describes the draft's claims, not Terveen and McDonald's, whose claims are intuitions they "cannot prove" (p. 414). Read that way, the line is accurate.

## In conversation with

- `herlocker2000explaining`: cited for enumerating and evaluating explanations for a recommender (p. 421), as a technique for computing introductions.
- `erickson2000social`: Erickson & Kellogg (2000) is in Terveen and McDonald's reference list (p. 431), but I found no in-text citation of it in the extracted text; the claims format is credited to a different work, Erickson 2003 (p. 414), which is not in the bib.
- Leads not in the bib: Erickson 2003 on claims as a research form (p. 414); Kautz, Selman & Shah 1997, ReferralWeb (p. 405); McDonald & Ackerman 2000, Expertise Recommender (p. 405); Kollock 1996 on conditions for cooperation (p. 413); Resnick et al. 2000, "Reputation systems" (p. 414).

## Caution

A 2005 agenda written before most platform research; its systems are prototypes, dating sites and early social networks. It reports no new data, and its claims are explicitly unproven. The copy read is a lab-hosted PDF of the published article with journal pagination; I did not compare it with the ACM PDF.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's saved copy of the GroupLens-hosted PDF (34 pages, journal running heads, pp. 401–434), extracted it with page breaks and located every quotation by journal page; read the eight claim statements and the passages around each quotation. Checked the record against Crossref (Terveen & McDonald, "Social matching: A framework and research agenda", *ACM TOCHI* 12(3), 401–434, September 2005). Checked the reference list for the "In conversation with" links. Re-read DRAFT_v2.md line 447 and the reference at line 693.

**Findings:**
1. The four-step process model was given in words the paper does not use ("profiling users, computing matches"); the Fig. 1 caption says "modeling the set of users who can be matched" and "matching users". Rewritten to the caption's terms.
2. "Claim 3 doubts visual decision aids" misstated the claim. Claim 3 asserts that "Social networks are a useful tool for social matching" (p. 414); the doubt about network diagrams as decision aids is a caution inside its discussion (p. 418) and concerns whole networks, not egocentric ones. Rewritten in both "What it argues" and "Relation to the argument".
3. `erickson2000social`: the card called it "a different Erickson work" as though unconnected; Erickson & Kellogg (2000) is in the article's reference list (p. 431), though I found no in-text citation. Corrected.
4. Verified verbatim with correct pages: "Recommending people fundamentally changes the game" (pp. 403–404, across the page break); "organized around a set of claims [Erickson 2003]", "we cannot prove that any of them are true", "to capture our intuitions ..." (p. 414); Claim 2 (p. 414) and "less opaque to users" (p. 416); the diagrams sentence (p. 418); the p. 427 footnote; "leave interpretation and decision-making up to the users" and "attempt to ease decision-making by identifying specific people" (p. 409); the Resnick et al. "shadow of the future" quotation (p. 414); "Designers must consider ..." (Claim 6); Herlocker et al. [2000] at p. 421.
5. Read depth (full text) is consistent with the saved PDF.
6. Use in DRAFT_v2 (line 447): verdict stands. The article is a framework and agenda organised around claims; the draft's falsifiability standard is its own, since Terveen and McDonald say they "cannot prove" their claims (p. 414).
