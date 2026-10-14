# Liu, D. Z. (2026). SovereignNegotiation-Bench: Evaluating user-owned personal agents in delegated bargaining under privacy, consent, evidence, and institutional pressure [v2 title: "Faithful delegates? Benchmarking the fiduciary duties of LLM negotiating agents"]. *arXiv preprint* arXiv:2607.02814.

**Identifier:** arXiv:2607.02814 · **Read depth:** full_text (arXiv v2, 1 Oct 2026, 17 pp., cs.MA; cited by PDF page; main text pp. 1–9 and the appendix tables read, prompt appendix F skimmed). **Version note:** the bib title is the v1 title. The PDF I read carries the new title "Faithful Delegates?" and the benchmark keeps the name SovereignNegotiation-Bench. · **Source-tier:** preprint · **Evidence basis:** direct_read · **Design and sample:** benchmark; 1,764 paired scenarios (252 situations × 7 counterparty tactics, 18 domains); test split 1,435 scenarios from 205 situations; 17 open-weight models, one run per scenario; no human subjects · **Parties modeled:** two parties + third party (a simulated principal, the model-under-test as the principal's agent, and a scripted counterparty) · **Facets:** H · **Read:** 2026-10-13

## What it argues
Liu holds that a delegate negotiating for a person should be scored on the duties agency law places on an agent, not on whether a deal closed. He turns five duties (loyalty, obedience to actual authority, confidentiality, candor, diligence) into deterministic checks on episode logs. Three of them (loyalty, authority, confidentiality) enter one headline metric, "faithful success" (pp. 1, 3, 5).

The counterparty is a fixed policy, so language has a price. Disclosing the principal's reservation value makes it "offers exactly that value and holds it"; disclosing a weakness caps the concession at half the surplus (§3.3, p. 4). The model-under-test sees only the observable state. Results (Table 3, p. 7):

- Faithful success runs from 6% to 75% across 17 models; the best is Gemma-4-26B-A4B at 75%. A rule-based "careful" agent that reads only the observable state reaches 92% (pp. 1, 6).
- A single sentence stating the limit takes the careful agent's surplus from 0.70 to 0.00. Forcing one disclosing sentence in two LLMs lowers surplus by 0.30 and 0.32 on clean pairs (n = 609 and 344; Table 6, p. 9).
- Limit disclosure runs from 2% to 80% of episodes, authority breaches from 2% to 23%, and compliance with an instruction injected into the counterparty's message from 5% to 57%.
- Agreement does not certify faithfulness. Liu writes that "pooled over models, 48% of the 13,755 agreements involve at least one breach of loyalty, authority or confidentiality" (§4.1, pp. 6–7).
- Of the pressure tactics, injection costs most: faithful success falls 12 points (p = 8.2×10⁻²⁸), lower in 17 of 17 models (Table 5, p. 8).
- Mitigations were tried on one model (Qwen3.5-9B): a fiduciary checklist moved faithful success by 0 points; a PrincipalBench scaffold lowered it by 7 points and cut the deal rate from 59% to 26%; a code guard on binding steps raised it by 3 points (p = 0.095, not significant) and left disclosure untouched (§4.4, p. 9; Table 8, p. 13). Within families, no size trend reaches exact p < 0.05 (App. D).

## Relation to the argument
**P7 and the delegate.** The paper shows a person who hands a coordination to an agent loses three things the person cannot easily check: what was said, what was shared and what was bound. Reading logs is a machine task here, not a human one. This supports the paper's view that no convention yet carries the work of inferring what a mediator will do, and it supplies a measured case where that work falls on the delegate's own principal.

**P8 and D3.** The only control that removed unauthorised agreements was a rule outside the model (the code guard), and it did not touch what the model said. This lines up with P8's contrast between rules in the mediator and aids that add to what a person reads, and with the Nadella post's external controls (P11 of the argument map). The check on disclosure was automatic string matching, not a human reader.

**Cuts the other way.** A disclosed limit has a price only because the counterparty is built to exploit it. Liu says the counterparty is "deliberately harsher than today's LLM counterparties" (p. 4), so the price is a worst case, not an estimate of platform behaviour.

Facet check: facet H quotes "high privacy/consent risk" from an abstract. That phrase is not in the v2 abstract I read, which instead gives faithful success of 6% to 75%, and 48% of agreements breaching a duty. The facet's description ("preprint, benchmark, no human subjects") holds.

## In conversation with
- `chan2024visibility`: Liu cites Chan et al. (2024) for the claim that agents' actions should be visible to oversight (p. 3) and says his benchmark supplies the measurement that argument calls for.
- Leads, not in the bib: Li & Shi (2026), PrincipalBench (arXiv:2606.30383); Zhang et al. (2026), TERMS-Bench (arXiv:2605.13909), whose "environment as verifier" design Liu adopts; Payne et al. (2026), SocialReasoning-Bench; Anthropic (2026), Project Deal and Project Swap field pilots, which Liu reports find "users do not notice the difference" in model quality (p. 2); Benthall & Shekman (2023) and Kolt (2025) on fiduciary agents.

## Caution
A synthetic benchmark with English-only, templated scenarios and a scripted rational-adversary counterparty. Open-weight models only, up to 120B parameters; no frontier API models and no human counterparties. Each scenario ran once per model with a fixed seed schedule; run-to-run spread reaches 11 points on injection compliance for one model (App. B). Liu tightened two metric definitions after looking at early test episodes of one model; he says this can only lower breach rates and the ranking is unchanged (Spearman 0.995; p. 6). Mitigations rest on one model. Liu discloses that AI tools were used "to polish the writing" (p. 9). A preprint that has changed title and abstract between versions: cite the version number.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** arXiv v2 PDF (2607.02814v2, 1 Oct 2026, 17 pp.; title 'Faithful Delegates?', as the card's version note says), extracted with pdftotext. I checked 6 verbatim quotations, the figures 1,764 scenarios / 252 situations, 1,435 test scenarios from 205 situations, 6% to 75% faithful success, 92% for the rule-based agent, 0.70 to 0.00 surplus, -0.30 and -0.32 with n = 609 and 344, 2-80%, 2-23% and 5-57% ranges, 48% of 13,755 agreements, injection -12 points (p = 8.2e-28, 17 of 17 models), the three mitigations on Qwen3.5-9B (0, -7, +3 points; deal rate 59% to 26%; p = 0.095), the 11-point seed spread, Spearman 0.995, and the Chan, TERMS-Bench, Project Deal, Benthall and Kolt citations.

**Findings:** No issues found. Small locator note: the injection result is in the text on p. 7 and in Table 5 on p. 8, which the card's 'Table 5, p. 8' covers. The card's quoted facet phrases ('high privacy/consent risk', 'preprint, benchmark, no human subjects') are the facet's, not the paper's; I confirmed only that 'high privacy' does not appear in this version. I did not check the v1 title or the bib entry.
