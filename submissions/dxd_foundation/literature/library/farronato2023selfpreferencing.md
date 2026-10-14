# Farronato, C., Fradkin, A., & MacKay, A. (2023). Self-preferencing at Amazon: Evidence from search rankings. *AEA Papers and Proceedings, 113*, 239–243. https://doi.org/10.1257/pandp.20231068

**Identifier:** doi:10.1257/pandp.20231068; read as NBER Working Paper 30894 (January 2023), https://www.nber.org/papers/w30894 · **Read depth:** full_text of the NBER working paper, not the journal version (9-page PDF; I read the whole text, Tables 1–2 and the references; page numbers below are the working paper's; the five-page AEA P&P version I did not see) · **Source-tier:** peer-reviewed article (read as working paper; AEA Papers and Proceedings are editor-selected session papers) · **Evidence basis:** direct_read · **Design and sample:** observational; a browser extension (Webmunk) installed by 184 US frequent Amazon shoppers in two 2022 pilots recorded 228,281 search results from 3,019 searches; OLS of rank on an Amazon-brand dummy, a sponsored dummy, search-spell fixed effects and product controls · **Parties modeled:** two parties + third party (shoppers and third-party sellers, with the platform ranking both its own and others' products) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

Farronato, Fradkin and MacKay ask whether Amazon ranks its own brands higher in search than comparable products. Search matters: 46.5% of product pages in their data are reached from a search page, in 72.1% of searches users do not go past the first page, and only about half of a full page is ever seen (p. 3). Amazon brands make up 1.3% of results and appear in 19.7% of searches (p. 4).

Within a search, Amazon-branded products rank higher. Without controls, the brand effect (−6.16 positions) is about as large as the effect of paid sponsorship (−7.09); with controls for price, ratings, delivery, availability and relevance it falls to −3.84 against −6.55 for sponsorship, "roughly 60% as large" (Table 2, p. 6). Recognisable third-party "major brands" get no comparable boost (column 3). Across specifications, "The effect of Amazon brands tends to be 30% to 60% as large as the effect of sponsoring" (p. 7).

The authors limit their claim: unobserved factors "such as click and purchase rates" might justify the ranking, and "our findings do not necessarily imply that consumers are hurt by Amazon brands' position in search results" (p. 7). Self-preferencing "can be good or bad for consumers" (p. 2).

## Relation to the argument

**Agency costs and custody (§7.1).** The draft grounds the custody test in agency theory: an intermediary with its own financial stake "faces continuing incentives to alter the representation to capture surplus" (line 408). This paper is direct evidence of an intermediary with a stake in the outcome adjusting the representation (the ranking) in favour of its own products, measured on real users' screens. It supports the premise with a measured magnitude. It does not show the move captured surplus from users, which the authors decline to claim (p. 7).

**Why it matters for a convention.** The ranking is exactly the kind of "interface convention" the draft says the owner "sets and changes" (line 418). The finding was obtainable only by an outside panel instrumenting users' browsers, which bears on who could audit a DXD convention in practice.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Farronato" finds no line, 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 408** ("When an intermediary has an independent financial interest in the transaction, its operator faces continuing incentives to alter the representation to capture surplus"). Supports the first half: the operator does tilt the representation toward its own products (Table 2, p. 6; p. 7). Narrows the second half: the paper does not show surplus capture or consumer harm (p. 7).
- **Line 418** (platforms: "the owner sets and changes rankings, algorithms, and interface conventions"). Supports with a measured case of owner-set ranking favouring the owner (pp. 5–7).
- **Line 426** ("Digital platforms fare worst on the custody test"). Consistent; adds an empirical instance outside terms of service.

## In conversation with

- `jensen1976theory` — the draft's theoretical anchor for line 408; this paper is an empirical instance in a platform.
- `suzor2018digital`, `klonick2018new` — the draft's custody sources on governance by terms and moderation; this paper adds ranking.
- `chen2015peeking` — in the bib; another outside-measurement study of a platform's hidden rule (Uber surge).
- Leads not in the bib: Raval (2022), "Steering in one click" on the Amazon Buy Box; Lee & Musolff (2022) on platform-guided search; Dubé (2022) on Amazon private brands; Farronato, Fradkin & Karr (2023) on the Webmunk tool.

## Caution

Two pilot samples of 184 frequent Amazon shoppers using desktop Chrome in the US (p. 3); not representative of all users or devices. Observational: the authors cannot rule out that unobserved demand signals justify the ranking (p. 7). The search-ad flag is measured with some noise (p. 5). I read the NBER working paper; check numbers against the AEA P&P version before quoting. A web-search summary I saw mentions a later preliminary draft by the same authors ("Vertical integration and consumer choice") that reportedly does not find discrimination in search; I did not open it, cannot confirm it, and it is marked not for distribution.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** Downloaded NBER WP 30894 myself (byte-identical to the writer's farronato.pdf; 9 pp.; printed page = PDF page − 1). The AEA P&P version is closed (OpenAlex is_oa false), so I could not compare it. Checked Crossref (AEA P&P 113, 239–243, 2023). Checked every quotation and number and Table 2 column by column. Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. All quotations are verbatim (pp. 2, 7). 46.5%, 72.1% and "only half of the products on a full page" (p. 3); 1.3% and 19.7% (p. 4); 228,281 results, 3,019 searches, 184 US-resident users in two 2022 pilots (pp. 2–3); Table 2 (p. 6): −6.16 vs −7.09 (col. 1), −3.84 vs −6.55 (col. 2), major brand −0.662 n.s. (col. 3). The controls include relevance, availability, quality, price and delivery (p. 5).
2. No change to the body except the not-cited note in "Use in DRAFT_v2". The card's unverified mention of a later draft by the same authors is already flagged as unconfirmed; it should not be used.
