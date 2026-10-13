# Alavi, S., & Nozari, S. (2026). When agents shop for you: Role coherence in AI-mediated markets. arXiv:2604.26220.

**Identifier:** arXiv:2604.26220 · **Read depth:** full_text (arXiv v1, 29 Apr 2026, "A Preprint", 19 pages; pagination is that PDF's; I read the whole text and tables, and skimmed only the reference list) · **Source-tier:** preprint (the bib entry is typed `@misc`) · **Evidence basis:** direct_read · **Design and sample:** simulation experiment, no human subjects. A buyer agent, a seller agent and a separate "inference agent" are all Claude Haiku 4.5. Main design: 2 conditions × 6 target willingness-to-pay (WTP) levels ($50 to $500) × 60 trials = 720 shopping dialogues of up to four turns, each read twice (full and price-redacted), 1,440 inferences; a factorial extension adds 450 dialogues (pp. 2, 9–10) · **Parties modeled:** two parties + third party (a consumer, the consumer's delegated agent, and a seller agent) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Alavi and Nozari claim that describing yourself to a shopping agent leaks what you will pay. They call the channel "role coherence": an agent told to act for "a mid-career consultant who travels frequently" behaves like one, and the way it shops reveals the budget tier. In the main condition the buyer agent gets a verbal profile and no dollar figure. In the contrast condition it gets a literal budget and a strict confidentiality instruction.

A separate inference agent reads each transcript and estimates the buyer's maximum WTP. For verbal profiles the slope of mean estimate on target WTP is 1.00 (bootstrap 95% CI [0.96, 1.05]; mean absolute error $48; 210 of 360 estimates within ±25%), with mean estimates running from $88 (target $50) to $510 (target $500; Table 5, p. 11). For numeric budgets the slope is 0.21 [0.17, 0.26], error $92, 36% within ±25%, and the estimates run only from $111 to $222 (Table 12, p. 16; Table 14, p. 17). Three robustness runs hold the verbal effect: profiles rewritten without financial vocabulary (slope 0.85 [0.79, 0.91]; p. 12), transcripts stripped of persona content by a second agent (slope 0.93 [0.89, 0.97]; p. 14), and three profile variants crossed with two prompt wordings (slope 0.999; design-aware CI [0.926, 1.086]; p. 11). With dollar amounts removed from the transcript, level calibration collapses (slope 2.90; 2% within ±25%; p. 11) while rank order survives.

The authors draw three conclusions. The leakage "arises from delegation itself, it cannot be mitigated at the prompt level" (abstract, p. 1). Role-coherent leakage "is not a privacy failure": no instruction is broken (p. 3). And "the inference agent recovers willingness to pay from how the buyer shops, not from who the buyer is" (p. 14). They propose three architectural defences, none tested: an anonymizing intermediary, profile rotation, and federated buyer-side aggregation (p. 18).

## Relation to the argument

**Premise P7 and rulings D3 and D4.** The source offers a worked case of a third-party agent that carries information to a counterpart that the person never chose to send. The person would have to infer what the delegate reveals, which is the same inference work P7 places on each party, now pointed at one's own agent. The authors' contrast, a prompt-level fix against an architecture-level fix, maps onto the author's D3/D4 distinction between a literacy-based and an algorithmacy-based intervention. Use it as an illustration of that distinction, not as evidence for D3: the paper tests no instruction aimed at the verbal condition, so the claim that prompts cannot close the channel follows from the persona-redaction result and the numeric contrast, not from a direct trial of a prompt-level mitigation (I found none in the text).

**Premise P10.** The agent here serves the buyer. The leak happens with the agent doing what it was asked, so it shows that an aligned mediator can still expose the principal. That does not support P10's step about an owner's divergent interest, and the seller's interest is not what produces the leak.

**What it cuts.** The "WTP" is the authors' own mapping from each written profile to a tier, hidden from the buyer agent and used only for scoring (Table 1 and its note, p. 7). A slope of 1.00 shows that a model can recover the tier the authors encoded. It does not measure any real consumer's willingness to pay, and the seller never acts on the estimate, so no price or welfare effect is measured. Cell-level Spearman ρ = 1.00 is computed on six cell means; the authors themselves note that the numeric condition also scores 1.00 (pp. 17–18).

**Facet check:** the facet's quotations are accurate. The facet's closing line, "Counter-delegation creates a privacy channel", does not appear in the text: I searched for "counter-delegation" and found nothing. The defences are named as the three above (p. 18). The facet's "lets a seller infer" also compresses the design: a separate inference agent, not the seller, produces the estimates.

## In conversation with

- `allouah2026what` — cited for systematic biases in agent purchasing (pp. 2–3).
- `zhu2025automated` — cited as Zhu et al. (2025), arXiv:2506.00073, whose numeric-budget paradigm the contrast condition copies (p. 6). The bib entry carries the same arXiv number under a later title.
- Not in the bib, as leads: Bansal et al. (2025), "Magentic Marketplace" (arXiv:2510.25779); Cherep et al. (2025) on agent consumer choice (arXiv:2509.25609); Shanahan, McDonell & Reynolds (2023), "Role play with large language models" (*Nature*); Andreas (2022), "Language models as agent models"; Shiller (2020) on reservation prices from browsing data.

## Caution

One model family fills every role, and the authors decline cross-model replication (p. 10). No human subjects, no seller behaviour. Six target tiers and written profiles; the slope of 1.00 is partly an artefact of the profiles being written to evoke tiers. A preprint by two assistant professors of marketing.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened arXiv v1 PDF (title, authors, 29 Apr 2026, 19 pp.); layout and reading-order extraction. Checked 8 quotations and about 30 numbers (slopes 1.00/0.21/0.85/0.93/0.999/2.90, CIs, MAE $48/$92, 210/360, 36%, $88-$510, $111-$222, 450 factorial dialogues, Spearman 1.00) with page locators by page-wise extraction; the three defences; the 'counter-delegation' absence; Zhu arXiv number.

**Findings:** No issues found. The card's own remark that 'Counter-delegation creates a privacy channel' is absent from the text is correct (searched; no hit). Not independently checked: the 1,440 inference count (arithmetic 720 x 2, not printed) and the claim that the reference list was only skimmed (card says so).
