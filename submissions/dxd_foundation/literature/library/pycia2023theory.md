# Pycia, M., & Troyan, P. (2023). A theory of simplicity in games and mechanism design. *Econometrica, 91*(4), 1495–1526. https://doi.org/10.3982/ECTA16310

**Identifier:** doi:10.3982/ECTA16310 · **Read depth:** full_text (published open-access PDF, CC BY, 32 pages, journal pagination 1495–1526; I read the whole main text, Appendix A (proof sketches) and the reference list; the Supplemental Material, which proves all lemmas used in Appendix A as well as Theorem 6 and Lemma 1 (Appendix A, p. 1517, gives only "the central elements of the proofs"), I did not open; Figures 1–5 I read through captions and the text that describes them) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** formal theory; no data. Extensive-form games in which agents plan only k moves ahead (k = ∞, 1, 0) · **Parties modeled:** other (many agents and a designer who chooses the game; no mediator with its own objective) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

Pycia and Troyan ask which mechanisms are simple to play. They start from the same evidence the draft cites: "there is accumulating empirical evidence of agents not reporting the truth in such mechanisms" (p. 1496, citing Kagel et al. 1987, Li 2017, Hassidim et al. 2016, Rees-Jones 2017/2018, Shorrer and Sóvágó 2018, Artemov et al. 2017). Their move is to let agents plan only part of the future, a "planning horizon", and to call a plan simply dominant when the worst outcome of following it beats the best outcome of any deviation, whatever happens outside the horizon (§3.2, p. 1502).

Varying the horizon gives three nested standards (pp. 1497, 1503):

- k = ∞ reproduces Li's obvious strategy-proofness (OSP);
- k = 1, one-step simplicity (OSS): the agent plans only her next move;
- k = 0, strong obvious strategy-proofness (SOSP): the agent plans no future move.

Three results matter here. First, OSP is weaker than it looks: "any winning strategy of White is obviously dominant; yet, the strategic choices in chess are far from obvious" (p. 1497). Without transfers, every OSP mechanism is a "millipede" clinch-or-pass game, and some millipedes require "lengthy backward induction" (Theorem 5, p. 1510; Figure 2, p. 1512). Second, in Li's binary settings with transfers, ascending (personal clock) auctions are OSS but in general not SOSP (Theorem 6, p. 1512; example, pp. 1503–1504: "In general, however, the ascending auction is not SOSP"). Third, SOSP mechanisms are exactly sequential choice from a menu: "each agent moves at most once, and, at this move, is offered a choice from a menu of options" (p. 1498; Theorem 8, p. 1515); with prices, these are posted-price menus. The paper ranks the two directly: "choosing from a menu of outcomes … entails simpler strategic considerations than those faced by a bidder in an ascending clock auction" (p. 1501), and "Random Priority is SOSP, but ascending auctions are not" (p. 1514).

Simplicity has a price. Theorem 2 shows that stronger standards shrink the set of rules a designer can implement (p. 1505). With transfers, "SOSP generally precludes efficiency and revenue maximization" (p. 1516); footnote 35 gives an impossibility: with two or more agents and values drawn from at least three levels, no SOSP mechanism allocates an object efficiently (p. 1516).

On behaviour, the paper reports, citing others, that experiments "confirm[] that obviously strategy-proof mechanisms are indeed simpler to play than merely strategy-proof mechanisms, while strongly obviously strategy-proof mechanisms are easier still and nearly all participants play them as expected (see Bo and Hakimov (2020) and Chakraborty and Kendall (2022))" (p. 1517). That is the authors' summary of other work, not their own data.

## Relation to the argument

**Convention A (§6.2).** The paper gives Convention A a sharper standard than the draft uses. The draft rests Convention A on OSP (line 321). Pycia and Troyan show OSP admits games that are hard to see through, and they rank a menu (SOSP) above an ascending clock (OSS). That supports the draft's instinct that a menu is the right display. It also exposes a mismatch: the draft's mock-up and design opening fuse "Guaranteed Clearing Menu" with "Ascending Clock Active" (lines 345–350, 358) and Arm 3 is labelled "Ascending Clock / Strategic Offloading Menus" (line 470). In this paper's terms those are two different mechanisms with two different simplicity levels.

**It cuts against the draft on cost.** The SOSP menu cannot do price discovery: with transfers it generally cannot allocate efficiently (p. 1516). A clearing-tier menu with "guaranteed" compensation (line 347) is a posted-price menu; the platform has to set the tiers. A menu that removes tactical calculation for the worker thus hands the price-setting to the mediator, which is the party §7 says cannot be trusted with the convention. The paper does not say this; the inference is mine from Theorem 8 and footnote 35.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Pycia" finds no line, 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 321** (OSP definition; OSP "can be recognized as safe by agents who lack contingent reasoning capabilities"). Supported as a statement of Li's standard: p. 1502 restates the worst-versus-best comparison and Theorem 3 (p. 1506) gives the behavioural microfoundation. Narrowed: the paper shows OSP still demands planning far ahead (pp. 1497, 1511–1512), so "recognized as safe" holds for clock auctions and serial dictatorships, not for every OSP game.
- **Line 323** ("Convention A embeds this property in the visual interface"). Narrows: the property worth embedding is the stronger SOSP (menu) standard where possible; OSP alone does not guarantee an obvious display.
- **Lines 350 and 358, line 470** ("Ascending Clock Active"; "ascending-clock menus that display clearing tiers where compensation is guaranteed"). Complicates: the paper separates the ascending clock (OSS, not SOSP; pp. 1503–1504, 1514) from the menu (SOSP; Theorem 8, p. 1515). A guaranteed-tier menu is a posted-price mechanism and gives up efficient price discovery (p. 1516, n. 35).
- **Line 498** ("Convention A rests on experiments in mechanism design that show a real but partial effect (Li, 2017; Gonczarowski et al., 2024)"). Consistent; the paper's own reading of the experimental record (p. 1517) is that SOSP mechanisms are played almost as intended, which suggests the draft could test a pure menu arm against a clock arm.

## In conversation with

- `li2017obviously` — the base definition; this paper generalises it, strengthens Li's clock-auction result to one-step simplicity (Theorem 6, p. 1512) and adapts Li's microfoundation (Theorem 3, p. 1506).
- `ashlagi2018stable` — cited for the result that deferred acceptance is not OSP except in restricted environments (p. 1499).
- `breitmoser2022obviousness` — cited (as the 2019 WZB version) as a test of whether OSP mechanisms are simpler to play (n. 37, p. 1517).
- `reesjones2018suboptimal` — cited directly among the evidence of untruthful play (n. 1, p. 1496). The same footnote cites Hassidim, Romm & Shorrer (2016, EC '16), "Strategic behavior in a strategy-proof environment", which is not the same work as `hassidim2017mechanism`.
- `artemov2023stable` — cited (as the 2017 working paper "Strategic 'Mistakes'") in the same footnote (n. 1, p. 1496).
- Leads not in the bib: Bó & Hakimov (2020), "Pick-an-object mechanisms"; Chakraborty & Kendall (2022), "Future self-proof elicitation mechanisms"; Kagel, Harstad & Levin (1987), *Econometrica*; Einav, Farronato, Levin & Sundaresan (2018), "Auctions versus posted prices in online markets", *JPE*; Li & Dworczak (2020) on designers who can confuse participants.

## Caution

Pure theory. It proves which games meet which standard; it does not measure how people play them. The claim that SOSP mechanisms are "nearly" always played as expected is the authors' summary of two other papers (p. 1517), which I did not read. The models have no mediator with its own objective and no repeated interaction, so nothing here speaks to custody or drift. Appendix A gives only the central elements of the proofs; the proofs of the lemmas, of Theorem 6 and of Lemma 1 sit in the Supplemental Material, which I did not open. I rely on the main-text statements of the theorems.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Opened the published CC BY Econometrica PDF the writer saved (dxd_foundation_local/pdfs/r5/pycia_ecta.pdf, 32 pp., journal pages 1495–1526) and extracted its text myself. Checked the Crossref record (Econometrica 91(4), 1495–1526, 2023; authors and DOI match). Searched every quotation in the text and mapped each to its journal page; checked Theorems 2, 3, 5, 6, 8, Figure 2, footnotes 1, 35 and 37, the Appendix A preface and the reference list. Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. Every quotation is verbatim and on the page given (pp. 1496, 1497, 1498, 1501, 1504, 1514, 1516, 1517). "Random Priority is SOSP, but ascending auctions are not" carries a footnote marker (31) after "SOSP" in the original; "confirm[]" correctly marks the original "confirms". Theorem pages (2: 1505; 3: 1506; 5: 1510; 6: 1512; 8: 1515), footnote 35's impossibility result and footnote 1's list of evidence all check.
2. Corrected the read-depth note and Caution: the card said the Supplemental Material holds the full proofs of Theorems 6–8 and Lemmas A.1–A.9. Appendix A (p. 1517) says it gives "the central elements of the proofs" and that all lemmas, Theorem 6 and Lemma 1 are proven in the Supplemental Material; Theorems 7 and 8 have their central proofs in Appendix A.
3. Added the not-cited note to "Use in DRAFT_v2". The verdicts themselves hold: the draft's OSP definition (line 321) matches p. 1502; the separation of the ascending clock (OSS, not SOSP) from the menu (SOSP) is on pp. 1503–1504, 1512, 1514–1515; the efficiency cost is p. 1516 and n. 35. The posted-price/mediator inference is correctly flagged as the writer's own.
