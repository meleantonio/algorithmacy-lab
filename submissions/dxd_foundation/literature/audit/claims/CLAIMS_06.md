# Claims audit — §6 Decision Experience Design (DRAFT_v2.md lines 285–397)

*Agent-written, 2026-10-14, research round 4. Checked against the card library and, where a card did not
settle wording or page, against the saved full texts in `dxd_foundation_local/pdfs/` (Li 2017 MPRA working
paper `H/li2017.txt`; Shneiderman 1983 `F/shneiderman1983.txt`; Gonczarowski et al. 2024 NBER w33020
`R4S2/w33020.txt`). No edits were made to the draft. Wrong facts are flagged with the correct value and
source for the author to decide; no replacement prose is proposed.*

**Section:** §6, "Decision Experience Design (DXD): Two Candidate Conventions" · **Lines:** 285–397 ·
**Date:** 2026-10-14 · **Round:** 4

**Counts (29 checkable claims):** supported 11 · supported_narrower 7 · overstated 3 · contradicted 1 ·
not_in_source 0 · miscited 0 · unverifiable 4 · needs_citation 3.
A further 15 entries are the author's stipulations, design openings or mock-ups (recorded, not checked;
marked "stipulation" or "illustration").

**Main points for the author.**
1. Line 327, "better understanding moved play only a little", runs against Gonczarowski et al.'s fourth
   main result: participants with high strategyproofness understanding played straightforwardly far more
   (83% against 46% pooled, p. 30). What was small was the *treatment* effect on play (p. 28).
2. Line 325 credits menu framing as such with the 71% understanding score. The menu description of the
   algorithm (Menu-DA) scored 58%, which the draft counts among "the other descriptions"; only the
   property-only menu (Menu-SP) reached 71% (pp. 4, 6, 24).
3. Line 319, "rarely translates into sincere human behavior", holds for the Vickrey auction (Masuda) but
   not across the library's evidence, where majorities often play straightforwardly.
4. Line 366's second sentence and line 362's "informational vacuum" claim have no citation, and the
   sources nearby do not carry them.
5. Norman (1988) is a ⚠ card: the attribution and the two gulf definitions remain unchecked against the book.
6. The library holds one close test of a what-if sandbox (Liu, Lai & Tan 2021), and it cuts against
   Convention B's sandbox (line 368).

| ID | Line | Claim (short quote) | Cited | Verdict | Evidence (locator + short quote) | Also supports | Cuts against | Correct value and source (only for errors) |
|---|---|---|---|---|---|---|---|---|
| C06-01 | 289 | "DXD shifts the design agenda from writing textual explanations to restructuring the decision interface" | — | stipulation | Author's framing; not checked. | — | — | — |
| C06-02 | 289 | "DXD grounds its interventions in Norman's (1988) framework of action" | Norman 1988 | unverifiable | `norman1988psychology` is ⚠: no text of the book seen; secondary sources (Wikipedia, citing ch. 2, p. 51; Open Library ToC, ch. 2 pp. 34–53) attribute the gulfs to it. The terms appear earlier in Hutchins, Hollan & Norman (1985) and Norman (1986). | `hutchins1985direct` (abstract only), `vermeulen2013crossing` (abstract only), `margono1987study` (§1.1 uses "Norman's two aspects of directness") | — | — |
| C06-03 | 291–312 | Diagram of the two gulfs bridged by Conventions A and B | — | illustration | Not checked. | — | — | — |
| C06-04 | 314 | Gulf of Execution = "cognitive distance between a user's goal and the actions permitted by the interface" | Norman 1988 (implied) | unverifiable | Consistent with the secondary paraphrase recorded in `norman1988psychology`; the book's wording and page not seen. Card adds: Norman's gulfs are person–device, the draft's mediator is a third party (D9). | `norman1988psychology` (secondary) | — | — |
| C06-05 | 314 | Convention A "narrows the Gulf of Execution by eliminating tactical gaming calculations … and showing on the display that they have been eliminated" | — | stipulation | Author's design claim. | `masuda2022net` (being told the task is gone moves behaviour, p. 908, Table 2) | `bjorkegren2020manipulation` (displaying a manipulable rule increases gaming, pp. 2, 29: holds only where the rule is truly strategy-proof) | — |
| C06-06 | 315 | Gulf of Evaluation = "cognitive distance between the system's state and the user's ability to assess that state" | Norman 1988 (implied) | unverifiable | As C06-04. Wikipedia's second-hand p. 51 quotation ("information about its state in a form that is easy to get, is easy to interpret…") is consistent but unchecked. | `norman1988psychology` (secondary) | — | — |
| C06-07 | 315 | Convention B narrows the Gulf of Evaluation by "valid, noise-filtered, low-latency feedback" | — | stipulation | Author's design claim. | — | — | — |
| C06-08 | 319 | "a mechanism is strategy-proof if reporting one's true valuation or preference is a dominant strategy: no participant can gain by lying…" | none | needs_citation | Standard definition, stated correctly; no source given. Li (2017) §1–2 and Pycia & Troyan (2023, p. 1502) state it. | `li2017obviously`, `pycia2023theory`, `ashlagi2018stable` | — | — |
| C06-09 | 319 | "Yet theoretical strategy-proofness rarely translates into sincere human behavior." | none (Masuda follows as one example) | overstated | True of the lab Vickrey auction (20.6% sincere, `masuda2022net` Table 2, p. 914). Elsewhere majorities play straightforwardly: Rees-Jones & Skowronek, 23.3% suboptimal lists (76.7% optimal), p. 12; Li SP-RSD, 36% of games off the dominant outcome (64% on), p. 29; Gonczarowski et al., 48–59% straightforward, p. 28; Artemov et al., 17–35% identifiable mistakes, Table 1, p. 273. | `masuda2022net`, `blume2023mediated` (≈20% act as if mediator absent, p. 17), `ashlagi2018stable` (misreporting under DA, p. 1), `cerrone2024school` (DA truth-telling 43.88%) | `reesjones2018experimental` (p. 12), `li2017obviously` (p. 29), `gonczarowski2024describing` (p. 28), `artemov2023stable` (only 1–20% of mistakes change the assignment, p. 272) | Non-sincere play is frequent (roughly a fifth to a half of participants or bids, depending on mechanism and setting), not near-universal: sources and pages in Evidence. |
| C06-10 | 319 | "In a laboratory Vickrey auction, only about a fifth of bids were sincere without advice" | Masuda et al. 2022 | supported | 20.6% sincere bids in VN (Table 2, p. 914); abstract "stays at 20%". | — | — | — |
| C06-11 | 321 | "To address this, Li (2017) formalized obviously strategy-proof (OSP) mechanisms." | Li 2017 | supported | Li motivates OSP by agents failing to see dominance in strategy-proof mechanisms, §1 (WP pp. 1–4); "policymakers could announce that a mechanism is strategy-proof, but that may not be enough" (§1). Read in the April 2017 MPRA version, not AER. | `pycia2023theory`, `ashlagi2018stable` | — | — |
| C06-12 | 321 | OSP if "for any deviating strategy, the best possible outcome under the deviation is no better than the worst possible outcome under the truth" | Li 2017 | supported_narrower | Li's definition carries a qualifier the draft drops: "for any deviation, at any information set where both strategies first diverge, the best outcome under the deviation is no better than the worst outcome under the dominant strategy" (abstract; WP p. 1). The comparison is made at the earliest point of divergence, not over whole strategies. | `pycia2023theory` (p. 1502), `ashlagi2018stable` ("at a decision node", pp. 5–6) | — | Li (2017), abstract: "at any information set where both strategies first diverge". |
| C06-13 | 321 | "OSP mechanisms can be recognized as safe by agents who lack contingent reasoning capabilities" | Li 2017 | supported | "Obviously dominant strategies are those that can be recognized as dominant by a cognitively limited agent"; the agent "is unable to reason contingently about hypothetical scenarios" (§1, WP pp. 3–4). Li's statement concerns strategies, and "recognize as weakly dominant". | `ashlagi2018stable` (pp. 5–6) | `pycia2023theory` (OSP may still require long-range planning, pp. 1497, 1511–1512: holds for clock auctions and serial dictatorships, not every OSP game) | — |
| C06-14 | 321 | "in Li's experiments far fewer games ended off the dominant-strategy outcome under the obviously strategy-proof version of the same rule" | Li 2017 | supported | "Under SP-RSD, 36% of games do not end in the dominant strategy outcome. Under OSP-RSD, 7%" (§5.3, WP p. 29); one-shot 40% vs 8% (§5.4, p. 30). This measure applies to the serial-dictatorship pair; the auction pairs use a different measure (31 and 28 points closer to equilibrium price, p. 28). | `pycia2023theory` | Li calls it "only preliminary evidence" (§5.5); arms differ in presentation as well as OSP status (§5.1). | — |
| C06-15 | 323 | Convention A "embeds this property in the visual interface" and "uses the interface to make that removal obvious" | — | stipulation | Author's design claim. | `gonczarowski2023strategyproofness` (description as a design object, pp. 1–2) | `pycia2023theory` (the property worth showing is the stronger SOSP/menu standard; OSP alone does not give an obvious display, pp. 1503–1504, 1515) | — |
| C06-16 | 325 | "Recent experimental economics calibrates the convention and its limit." | — | stipulation | Signposting. | — | — | — |
| C06-17 | 325 | "Gonczarowski, Heffetz, Ishai, and Thomas (2024; N = 542)" | Gonczarowski et al. 2024 | supported | N = 542 (p. 5; 255 Prolific + 287 Cornell, p. 20). NBER WP 33020, not peer reviewed. | — | — | — |
| C06-18 | 325 | "tested whether describing a matching mechanism as a personalized menu, in place of the traditional description of its algorithm, increased understanding and straightforward play" | Gonczarowski et al. 2024 | supported_narrower (revised by skeptic) | Five treatments, two of them menus (pp. 3–5). The menu description of the algorithm (Menu-DA) did not raise understanding (58% vs 56% Trad-DA, "statistically indistinguishable", p. 6). Only Menu-SP, which states the property "without specifying how one could calculate the mechanism's outcome" (p. 4), did. The sentence credits menu framing as such. | `gonczarowski2023strategyproofness` (p. 23 summary of the companion) | `gonczarowski2024describing` ("Menu-DA is less effective at teaching SP relative to Menu-SP—despite merely providing more information", p. 36) | The gain belongs to the property-only menu (Menu-SP, 71%), not to a menu description of the algorithm (Menu-DA, 58%): Gonczarowski et al. 2024, pp. 4, 6, 24. |
| C06-19 | 325 | "Understanding of strategy-proofness rose to 71%, against 58% and 56% under the other descriptions." | Gonczarowski et al. 2024 | supported_narrower | Numbers correct (p. 6). There were four other descriptions, not two: Textbook-SP 62% and Null 54% omitted (pp. 6, 24); and the 58% is Menu-DA, itself a menu description. Menu-SP beats every other arm after Bonferroni (p < 0.01 vs Textbook-SP; p < 0.001 others; fn. 14, p. 24). | — | — | Full set: Menu-SP 71%, Textbook-SP 62%, Menu-DA 58%, Trad-DA 56%, Null 54% (pp. 6, 24). |
| C06-20 | 325 | "Straightforward play reached 59% under the menu description, against 56% under the traditional description, … not significant, and 48% under a control" | Gonczarowski et al. 2024 | supported_narrower | 59/56/48% and p = 0.47 correct (p. 28; Fig. 10, p. 29). But "the menu description" is Menu-SP; the other menu arm, Menu-DA, was 50%, and Textbook-SP 53% (p. 28). Under the same uncorrected tests Menu-SP vs Null is p = 0.01 and vs Menu-DA p = 0.04 (Fig. 10). | — | — | Menu-DA 50%, Textbook-SP 53% (p. 28); Menu-SP vs Null p = 0.01 (Fig. 10, p. 29). |
| C06-21 | 327 | "under the best description tested, about four in ten participants still did not play straightforwardly" | Gonczarowski et al. 2024 (implied) | supported_narrower (revised by skeptic) | Menu-SP 59% straightforward, the highest (p. 28), so 41% not. | `blume2023mediated` (p. 17) | `artemov2023stable` (much non-straightforward play is payoff-irrelevant, pp. 272, 274) | — |
| C06-22 | 327 | "and better understanding moved play only a little" | Gonczarowski et al. 2024 (implied) | contradicted | The paper's fourth main result is the reverse at the participant level: "Participants with high-enough SP-understanding play SF at very high rates" (§3.4, p. 28); pooled, 83% straightforward above 75% understanding vs 46% below (p. 30); a "jump" at "roughly 75–80%" (p. 29). What was small was the treatments' effect on play: "our treatments' effects on % SF are overall small" (p. 28). The understanding–play relation was not pre-registered (p. 29). | treatment-level reading: `gonczarowski2024describing` (p. 28) | `gonczarowski2024describing` (pp. 29–30) | Gonczarowski et al. 2024, p. 30: mean straightforward play 83% (understanding > 75%) vs 46% (< 75%), a 36-point difference; the small effect is of the treatments, p. 28. |
| C06-23 | 329 | "a plain statement that sincere bidding is a dominant strategy" | Masuda et al. 2022 | supported (revised by skeptic) | The advice read: "You can maximize your earnings by bidding your valuations as they are, regardless of what others bid" (p. 908): a plain-language statement of (weak) dominance, not the words "dominant strategy"; printed on paper and read aloud by the experimenter, not an interface. | `guillen2018effectiveness` (via Masuda p. 905; no card), `reesjones2018experimental` (NRMP advice raised truthful reporting, AME 0.10, pp. 17–18) | — | Wording per Masuda et al. 2022, p. 908. |
| C06-24 | 329 | "raised sincere bids from 20.6% to 46.9%" | Masuda et al. 2022 | supported | Table 2, p. 914; net of demand effect 23.8 points (Result 3, p. 916). | — | — | — |
| C06-25 | 329 | "while efficiency rose by about one percentage point" | Masuda et al. 2022 | supported | 0.967 → 0.977, p = 0.020 (Table 6, p. 920); net of pay-your-bid only 0.009, p = 0.051. | — | — | — |
| C06-26 | 329 | "Convention A must therefore pair the structural elimination … with an interface that visibly confirms the task is gone" | — | stipulation | Author's inference. Note that Masuda et al. present advice as an *alternative* to structural redesign such as OSP, which "severely restricts the admissible class of mechanisms" (p. 905). | `ashlagi2018stable` (trust and witnessing the mechanism run, pp. 14–15) | `masuda2022net` (p. 905) | — |
| C06-27 | 329 | "its designers should expect behavior to change more than outcomes" | Masuda et al. 2022 (implied) | overstated | Masuda's authors tie the small efficiency change to their design: symmetric valuations left both auctions nearly efficient, so "the effects of advice on efficiency are limited" (p. 938). A study-specific result, not a general expectation. | `artemov2023stable` (behaviour and outcomes come apart, Corollary 2, p. 284) | `masuda2022net` (p. 938) | Masuda et al. 2022, p. 938: limited efficiency effect attributed to near-ceiling efficiency in a symmetric environment. |
| C06-28 | 331–355 | Mock-up: bid box with "platform commission (20%)"; "Guaranteed Clearing Menu"; "Ascending Clock Active. Sincere preference revelation is dominant." | — | illustration | Not checked. Note for the author: Pycia & Troyan separate the ascending clock (OSP, not SOSP) from the menu (SOSP), and a guaranteed-tier menu is a posted-price mechanism (pp. 1503–1504, 1515–1516, n. 35). | — | `pycia2023theory` | — |
| C06-29 | 357–358 | Design opening: ascending-clock menus "where compensation is guaranteed and tactical undercutting is made impossible by design" | — | stipulation | A "What if". | `li2017obviously` (ascending clock is OSP, §1) | `pycia2023theory` (n. 35, efficiency cost); `ashlagi2018stable` (no OSP implementation of stable matching in general, Theorem 3, p. 10) | — |
| C06-30 | 362 | Convention B shortens "the temporal and causal distance between an actor's exploratory probe and the mediator's response" | — | stipulation | Author's design claim. | — | — | — |
| C06-31 | 362 | "direct manipulation relies on immediate visual feedback" | Shneiderman 1983 | supported | "rapid, reversible, incremental actions" (p. 57); principle of operations whose "impact on the object of interest is immediately visible" (p. 64); "Users can immediately see if their actions are furthering their goals" (p. 65). | `margono1987study` (§1.1), `hutchins1985direct` (abstract only) | `shneiderman1983direct` itself: visual form does not help by being visual; "content … is a critical determinant" (p. 64) | — |
| C06-32 | 362 | "when a user drags a file, the icon tracks the cursor in real time (Shneiderman, 1983)" | Shneiderman 1983 | supported_narrower | The article's drag example is the Xerox Star: "Users can drag a document icon and drop it into a printer icon to generate a hardcopy printout" (p. 62, page by scan count, not image-checked). It does not describe the icon tracking the cursor in real time; that detail is the draft's. | — | — | Shneiderman 1983, p. 62: drag-and-drop of a document icon to a printer icon (Xerox Star). |
| C06-33 | 362 | "In algorithmic mediation, that immediate coupling is routinely broken … waits in an informational vacuum while backend algorithms batch, calculate, and commit" | none | needs_citation | A factual claim about platform practice with no source. Partial support in the library: Uber recomputes surge "independently on a 5-minute clock" by area (`chen2015peeking`, §8, p. 507); FX Last Look holds a filled trade for a rejection window (`cartea2019foreign`, pp. 3, 13–14). Neither shows "routinely". | `chen2015peeking`, `cartea2019foreign` | — | — |
| C06-34 | 364 | "ecological validity strictly precedes speed" | — | stipulation | Author's ordering. | `wisniewski2020power` (information content matters most, p. 12) | — | — |
| C06-35 | 364 | "Exposing high-frequency feedback on noisy or volatile data can damage human decision-making." | none directly (Larson follows) | supported (revised by skeptic) | Larson et al. show harm from frequent price feedback (pp. 8–9), but the mechanism is seeing losses often on a positively drifting asset, not noisy or unreliable data (p. 6). Beshears et al. find frequency effects vanish with real funds over a year and realistic return distributions (pp. 15, 27). | `larson2016can`, `rahmandad2023delays` (noise cut profit in study 1, p. 13) | `beshears2017does` (pp. 15, 27) | — |
| C06-36 | 364 | Second-by-second traders "invested about 25% less in the risky asset and earned about 35% less than traders shown prices every four hours" | Larson, List & Metcalfe 2016 | supported | 27.4% vs 36.4% risky share over the last 20% (p. 8) = 24.7% less; profits 401,634 vs 615,715 units (p. 9) = 34.8% less. The paper states them the other way (33% more, 53% higher, abstract). Profits are platform units. | — | `beshears2017does` | — |
| C06-37 | 364 | "a pattern they attribute to myopic loss aversion" | Larson et al. 2016 | supported | Abstract: "data patterns consonant with MLA"; title. | `beshears2017does` (MLA framing) | — | — |
| C06-38 | 366 | "Kluger and DeNisi (1996, 1998) showed in a meta-analysis that more than one-third of feedback interventions reduce performance" | Kluger & DeNisi 1996, 1998 | supported (revised by skeptic) | Both cards are ⚠ (abstract / first paragraph only), but the fraction is visible: "over 1/3 of the FIs decreased performance" (1996 abstract; d = .41 on average; 607 effect sizes); "they reduce performance in more than one third of the cases" (1998, p. 67). Only the 1996 article is the meta-analysis; the 1998 piece reports it. Whether the unit is interventions or effect sizes is unsettled from the abstract. | `wisniewski2020power` ("about a third", p. 1) | `wisniewski2020power` (in education 17% of effects negative, p. 7) | The meta-analysis is Kluger & DeNisi (1996); the 1998 article is a summary (p. 67). |
| C06-39 | 366 | "Providing uncurated, rapid feedback on a volatile algorithm hands the user a stream of noise." | none (follows Kluger & DeNisi) | needs_citation | Kluger & DeNisi's abstract attributes harm to attention moving toward the self, and says nothing about speed, curation or volatility (1996 abstract). Wisniewski et al. locate harm in low-information feedback, not rapidity (pp. 11–12). | `chen2015peeking` (surge is "extremely noisy", most surges < 5 min; jitter from a bug, pp. 495, 503) | `kluger1996effects`, `wisniewski2020power` | — |
| C06-40 | 368 | Convention B: feedback "valid and noise-filtered first, plain second, and low-latency third"; "pre-commit sandboxes and boundary contours" | — | stipulation | Author's design specification. | `wisniewski2020power` (p. 12), `rich2018limits` (full foregone-outcome feedback, pp. 1561, 1565), `lee2023learning` (p. 2321), `rahmandad2023delays` (delay impairs learning, Table 2, p. 13) | `dietvorst2015algorithm` (valid feedback on an imperfect algorithm lowers reliance, pp. 6–9); `logg2019algorithm` (pp. 2, 31–34); `rogers2021linkedins` (some noise protects third parties, §8.3); `liu2021understanding` (free counterfactual probing did not improve decisions and raised over-reliance, 408:23–24) | — |
| C06-41 | 368 | "No experiment has yet tested this convention in a mediated triad" | none | unverifiable | A negative existence claim; no systematic search for it is recorded. In the library, the closest test is dyadic: Liu, Lai & Tan (2021) tested interactive what-if explanations with a classifier and found they did not help (408:23–24). No triadic test found in the library. | — | `liu2021understanding` (a dyadic test exists, and it cuts against the sandbox) | — |
| C06-42 | 368 | "it follows from the conditions in §5.3 and is offered as a hypothesis" | — | stipulation | Internal cross-reference. | — | — | — |
| C06-43 | 370–393 | Mock-up: sandbox with "P(Match) = 88%", "± 3%" | — | illustration | Not checked. | — | `logg2019algorithm` (mediator-labelled estimates weighted differently by lay users and experts, pp. 2, 31–34) | — |
| C06-44 | 395–396 | Design opening: drivers and sellers dragging a slider to see allocation before committing | — | stipulation | A "What if". | `chen2015peeking` (riders wait out short surges, p. 506) | `liu2021understanding` (users without guidance did not know what to probe, 408:14, 408:27) | — |

## Sources opened this pass (beyond the cards)

- Li (2017), MPRA WP 78930, April 2017 version, `dxd_foundation_local/pdfs/H/li2017.txt`: abstract definition, §1 pp. 3–4, Table 4 and §5.3 p. 29.
- Shneiderman (1983), `dxd_foundation_local/pdfs/F/shneiderman1983.txt`: searched for the drag/cursor passage; p. 62 by page count in the OCR text (not checked against the page image).
- Gonczarowski et al. (2024), NBER w33020, `dxd_foundation_local/pdfs/R4S2/w33020.txt`: §3.4 and Figure 11 text, printed pp. 28–30.

## Notes

- Norman (1988) and Kluger & DeNisi (1996, 1998) remain ⚠ cards. Library copies would settle C06-02,
  C06-04, C06-06 and the unit question in C06-38.
- Li (2017) was read in the April 2017 working paper, not the AER version of record; locators are the WP's.

## Skeptic pass (2026-10-14)

*Agent-written. I re-opened the saved full texts myself: Gonczarowski et al. 2024 (`R4S2/w33020.txt`, with
pp. 29 rendered from the PDF to read the Figure 10 p-values and bars), Masuda et al. 2022
(`P/masuda2022.txt`), Li 2017 MPRA WP (`H/li2017.txt`), Shneiderman 1983 (`F/shneiderman1983.txt`; page of
the new passage fixed with pdftotext page by page), Larson et al. 2016 NBER (`R4b/larson2016_nber.txt`), and
the Kluger & DeNisi 1996 abstract (`R4b/kluger/kd_abstract.doc`) plus the `kluger1998feedback` card. For
Norman (1988) I found one Internet Archive item (xerox-parc collection, "The Psychology of Everyday Things",
1987-04-20), but it is a talk record with no text files, not the book. OpenAlex was rate-limited, so I made no
fresh search for Norman or Hutchins texts.*

### Overturned (verdict cells revised in place)

- **C06-18 → supported_narrower** (was overstated). The sentence describes the study's question, and the
  paper frames its design the same way: "We compare a traditional DA description, and a description of the
  definition of strategyproofness itself, with new menu versions of both" (§1, p. 1). Menu-DA against Trad-DA
  is exactly "a personalized menu in place of the traditional description of its algorithm". The sentence
  claims no result, so it cannot overstate one. It is narrower than the design because it omits the two
  property arms and the Null arm. The defect the ledger found (crediting the 71% to menu framing as such)
  sits in C06-19, which stays flagged.
- **C06-21 → supported_narrower** (was supported; unit error). "About four in ten participants still did
  not play straightforwardly" turns a mean share of *rounds* into a share of *participants*. % SF is each
  participant's share of the 10 rounds played straightforwardly; Menu-SP's mean is 59% (p. 28), and "most
  participants play SF in some rounds and NSF in others" (p. 28). Figure 10(b) (p. 29, read from the page
  image) shows 19% of Menu-SP participants played SF in all ten rounds, so about 81% of participants
  deviated at least once. Correct value: Menu-SP participants ranked straightforwardly in 59% of rounds on
  average; 19% did so in every round (Gonczarowski et al. 2024, p. 28; Fig. 10(b), p. 29).
- **C06-23 → supported** (was supported_narrower). The advice read: "You can maximize your earnings by
  bidding your valuations as they are, regardless of what others bid" (p. 908). That is a plain-language
  statement that sincere bidding is (weakly) dominant, which is what the draft says. The draft does not claim
  the words "dominant strategy" were used, and this clause says nothing about an interface (the interface
  inference is C06-26). One detail the author may want: the advice also told subjects to "consider carefully
  whether this advice is true or false" (p. 908).
- **C06-35 → supported** (was supported_narrower). The sentence is hedged ("can damage") and names "noisy
  or volatile" data. Larson et al. put the mechanism in volatility itself: under MLA investors "pay too much
  attention to the short-term volatility of their asset portfolios … In this way, frequent feedback on asset
  returns is detrimental" (NBER WP p. 1). The frequent group saw price ticks arriving "1-3 times a second"
  (p. 5). `beshears2017does` (pp. 15, 27) still cuts against any general reading, and the author should know
  that; it does not defeat a "can".
- **C06-38 → supported** (was supported_narrower). The draft's wording matches the 1996 abstract
  word for word in substance: "over 1/3 of the FIs decreased performance" (abstract; 607 effect sizes). The
  draft's unit, "feedback interventions", is the authors' own unit in that sentence, so the
  interventions-or-effect-sizes question does not make the draft wrong. Citing the 1998 summary alongside the
  meta-analysis is ordinary practice; the 1998 text says "more than one third of the cases (Kluger & DeNisi,
  1996…)" (p. 67). Both cards remain ⚠ (abstract / first paragraph only).

### Upheld

- **C06-22 (contradicted).** I looked for a reading that saves the clause. One exists: at the treatment
  level, the description that raised understanding most moved mean play little (59% vs 56%, p = 0.47,
  Fig. 10, p. 29), and the authors explain why (only 5–43% of participants per arm crossed the 75%
  understanding threshold, so a gap of at most about 14 points was expected, p. 30). But the clause makes
  *understanding* the subject, and on that the paper's fourth main result is the reverse: "Participants with
  high-enough SP-understanding play SF at very high rates" (p. 28); pooled, 83% vs 46% (p. 30). The abstract
  says the same: "While behavioral effects are small on average, participants with levels of
  strategyproofness understanding above a certain threshold play the classical dominant strategy at very
  high rates." Upheld, with the note that the relation was not pre-registered (p. 29).
- **C06-09 (overstated).** Masuda et al., the draft's own example, frame the general literature more weakly
  than the draft: "telling the truth is far from universal" (p. 903). "Most subjects do not reveal their true
  type" is said of the Vickrey auction only (p. 903, fn. 2). Gonczarowski et al. say DA participants
  "frequently do not play straightforwardly" (p. 1). "Frequently" and "far from universal" are what the
  sources carry; "rarely" is not.
- **C06-19 (supported_narrower).** Numbers confirmed (pp. 6, 24: Menu-SP 71%, Textbook-SP 62%, Menu-DA 58%,
  Trad-DA 56%, Null 54%). The omission stands.
- **C06-20 (supported_narrower).** Confirmed from the rendered Figure 10(a), p. 29: Trad-DA 56, Menu-DA 50,
  Menu-SP 59, Textbook-SP 53, Null 48; Trad-DA vs Menu-SP p = 0.47; Menu-DA vs Menu-SP p = 0.04; Menu-SP vs
  Null p = 0.01 (two-sample t-tests, uncorrected). So the 11-point gain over the control is significant in
  the authors' own test, which the draft's sentence does not say.
- **C06-27 (overstated).** Masuda p. 938: both auctions were "almost perfectly efficient" in the symmetric
  design, so "efficiency in both auctions has little room for improvement"; they "conjecture that experiments
  in an 'asymmetric' environment would clarify the advice effect on efficiency." They also call their advice
  deliberately simple, which "makes the effect of advice limited" (p. 937). The small outcome effect is a
  ceiling effect of the design, not a lesson for designers.
- **C06-12 (supported_narrower).** The WP's own prose statement (§1, p. 2) carries the qualifier too: "starting
  from any earliest information set where Si and Si′ diverge". A second narrowing the ledger missed: Li
  defines *obviously dominant* for a strategy; a mechanism is OSP "if it has an equilibrium in obviously
  dominant strategies" (abstract). The draft applies the strategy condition straight to the mechanism.
- **C06-32 (supported_narrower), evidence corrected.** The ledger said the Xerox Star passage (p. 62) is
  the article's only drag example. It is not. Shneiderman also sketches a job-control interface where
  "Copies are made by locking a cursor onto a file name and dragging it to a picture of a tape drive or a
  printer" (p. 67, PDF page 11). That is closer to the draft's "drags a file", but it is a proposed design
  ("Imagine a job control language…"), and neither passage says the icon tracks the cursor in real time.
  The general principle the draft needs is on p. 64 ("impact on the object of interest is immediately
  visible"). The article's examples are display editors, VisiCalc, video games and CAD, not "classical
  graphical user interfaces" as a class.
- **C06-08 (needs_citation).** Low stakes: the definition is standard and Li (2017) follows in the next
  paragraph, but a definition in an HCI paper still wants a source.
- **C06-33, C06-39 (needs_citation).** Nothing new found. For C06-39 the 1996 abstract locates harm in
  attention moving "up the hierarchy closer to the self and away from the task", not in speed or noise.
- **C06-02, C06-04, C06-06 (unverifiable).** No text of Norman (1988) could be opened (see header note).
- **C06-41 (unverifiable).** A negative existence claim; no systematic search recorded, and I ran none.

### Supported rows sampled (11) — attempted to break

| ID | Result | What I checked |
|---|---|---|
| C06-10 | holds | 20.6% without advice (p. 904; Table 2, p. 914). The auction is a two-unit Vickrey auction. |
| C06-11 | holds | Li §1 motivation (WP pp. 1–4). |
| C06-13 | holds | "can be recognized as dominant by a cognitively limited agent" (WP p. 3); "unable to reason contingently" (p. 4). Li's statement is about strategies, not mechanisms (see C06-12). |
| C06-14 | holds | "Under SP-RSD, 36% of games do not end in the dominant strategy outcome. Under OSP-RSD, 7%" (WP p. 29). Same choice rule, two implementations. |
| C06-17 | holds | "combined N = 542; pre-registered" (p. 5); 255 Prolific + 287 Cornell. |
| C06-21 | **broken** | Unit error: rounds, not participants. See Overturned. |
| C06-24 | holds | "20.6% without advice, it increases to 46.9%" (p. 904). |
| C06-25 | holds | Table 6, p. 920: VA 0.977 vs VN 0.967, difference 0.010 (p = 0.020, p. 920); net of pay-your-bid 0.009 (p = 0.051). |
| C06-31 | holds | "Rapid, incremental, reversible operations whose impact on the object of interest is immediately visible" (p. 64). |
| C06-36 | holds | 36.4% vs 27.4% risky share; 615,715 vs 401,634 profit units (NBER WP pp. 8–9); abstract "33% more … 53% higher". Frequent = "every second", Infrequent = "every four hours" (p. 6). |
| C06-37 | holds | Abstract: "data patterns consonant with MLA". |

### Missed claims

- **Line 327 (C06-21's sentence), unit.** See Overturned. Listed here too because the ledger marked it
  supported.
- **Line 366, "Similarly".** The connective presents Kluger & DeNisi's finding as the same kind of evidence as
  Larson et al.'s frequency result. As far as the 1996 abstract shows, the meta-analysis is not about
  feedback frequency or noisy data; it locates the harm in attention moving toward the self (abstract).
  Verdict: overstated (the analogy is the draft's, not the source's). Source: Kluger & DeNisi 1996, abstract
  (⚠ card).
- **Line 325, significance of the gain over control.** The draft reports 59% vs 48% "under a control" without
  saying the difference is significant (p = 0.01, Fig. 10(a), p. 29), while it does report the
  non-significant comparison. Verdict: supported_narrower; this selective reporting understates the
  evidence for Convention A. Source: Gonczarowski et al. 2024, Fig. 10(a), p. 29.
- **Line 321, mechanism vs strategy.** See C06-12 above (Li abstract: a mechanism is OSP "if it has an
  equilibrium in obviously dominant strategies").
- **Line 362, "In classical graphical user interfaces … (Shneiderman, 1983)".** Shneiderman's 1983 examples
  predate and are wider than "classical GUIs" (display editors, VisiCalc, Pong and arcade games, CAD, the
  Xerox Star). Verdict: supported_narrower. Source: Shneiderman 1983, pp. 57–62.
