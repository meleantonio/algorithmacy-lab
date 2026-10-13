# Zhu, L., Lu, Q., Ding, M., Lee, S. U., & Wang, C. (2026). Designing meaningful human oversight in AI. *AI and Ethics, 6*, Article 286.

**Identifier:** doi:10.1007/s43681-026-01147-7 · **Read depth:** full_text (publisher PDF, open access, 21 pages; page numbers are the PDF's "Page N of 21", which is the article's own pagination; received 5 Nov 2025, accepted 15 Apr 2026, published 4 May 2026). I read all of it, including the reference list; I skimmed the four worked patterns in Section 7 and Tables 3 to 5 for structure and did not check their cited vendor pages · **Source-tier:** peer-reviewed journal article · **Evidence basis:** direct_read · **Design and sample:** conceptual framework built from a "known uses" document analysis of 12 publicly documented AI systems (54 candidates screened, June to September 2025) and a targeted literature review. No users, interviews or experiments (pp. 6-8) · **Parties modeled:** person–system (a human evaluator and an AI system), inside an organisation; affected parties appear only as people who can appeal · **Facets:** Z · **Read:** 2026-10-13

## What it argues

The authors say current oversight fails in two ways: "humans act as rubber stamps" or the system is "constrained so tightly" that it becomes rule-following automation (p. 2). Their remedy splits agency in two. The AI keeps *operative* agency, "the AI's capacity to generate solutions"; the human keeps *evaluative* agency, "the human's capacity to understand, judge, verify the AI's solution" and to steer or substitute it (p. 2). Accountability attaches to the evaluation, not to re-doing the work. They borrow four agency conditions from Barandiaran and colleagues (individuality, source of action, goal-directedness, adaptivity) and turn each into a design lever (pp. 3-4, 9).

Two further moves carry the paper. First, they separate *internal* reasoning faithfulness (what the model computes) from *external* reasoning faithfulness (agreement with outside criteria and expert judgement), and argue that "understanding and effective oversight therefore tends to rely more on external reasoning faithfulness" (p. 5), because mechanistic insight is not yet feasible. Second, they use the solve-verify asymmetry: some tasks are hard to solve and easy to check. Verification should be built into the system, and "effective design should therefore reduce or even eliminate the need for costly runtime verification" (p. 5), by doing as much checking as possible at design time (pp. 5-6).

Section 6 (Table 5, p. 11) lists 19 oversight mechanisms by layer and agency dimension: provenance capture, structured rationales, explanation packs, calibrated confidence with abstention, divergence detection against an independent checker, confidence-and-impact routing, veto and substitution, circuit breakers, goals ledgers, drift monitors, shadow mode, counterfactual probes, appeal bundles and sampling for post-hoc review. Section 7 composes them into four patterns for document evaluation: criteria-aligned assessment, conformance checking, evidence-grounded synthesis, and signal detection and prioritisation (pp. 12-17). Section 8 lists limits: the evaluator becomes "a distinct class of labour" whose work is "a redistribution rather than a net creation of effort" (p. 18); "well-structured explanation packs may themselves become a new locus of undue trust" (p. 18); the model fails in real-time safety-critical settings where run-time intervention "may be impracticable or unsafe" (p. 18); and the cases come from vendor and conference documents that "are often marketing-oriented" (p. 19). The authors call the framework "conceptual and design-oriented" (p. 19) and propose controlled studies, field deployments and longitudinal work as future steps.

## Relation to the argument

Facet check: facet Z (entry 16) quoted the abstract line about designing outputs so humans can check and contest them "without having to resolve the task," and concluded that "none of these sources replaces the human check with structure." The abstract quote is accurate. The conclusion needs a qualifier for this paper: Zhu keeps the human as evaluator at run time, but pushes much of the checking to design time and to sampling (pp. 5-6), so structure does replace some run-time checks. The paper does not ask what task the person keeps once the structure is in place; it asks how to make the person's check cheaper.

- **P12 (people monitor badly).** Supported from inside the oversight literature. Zhu cites decades of work that "humans are poor at sustained monitoring of highly reliable systems" (p. 8), and cites Green on policies that assume humans can correct AI (p. 2). Zhu answers with a redesigned check, not with removal of the check.
- **P9 and ruling D3 (disclosure).** Supported. Zhu says explanations alone rarely fix inappropriate reliance, that interventions "that change the interaction" help more, and that generic transparency has "mixed or negative effects" (p. 3); it adds that explanation "is not a sufficient safeguard" (p. 18). This sits against D3's strong form ("doesn't affect our ability to navigate it"): the literature supports "weak and inconsistent," as the author's own flag in SOURCE.md already notes. Most of the mechanisms it lists are still things the person reads (rationales, traces, packs, confidence).
- **D4 and P11 (the contrast with the Nadella post).** Zhu fits the pattern the argument map attributes to the post: it grants that the model cannot be read, puts the weight on checks outside the model (circuit breakers, independent checkers, policy attribution), and leaves a person to verify and halt. Authority stays with the deploying organisation, which "commits to a target level of understanding" at design time (p. 10). So this paper is an academic version of the position the foundation paper argues against, and it also shows that oversight designs cover more than disclosure (against "his only move is disclosure"). Whether it matches the post's seven principles I have not checked, since I did not read the post here.
- **Third party and P10.** The paper's contestability definition names "affected parties" who can object and "receive a substantive response" (p. 9), and the appeal bundle exports reasons and provenance "to reviewers and courts" (p. 11). Those parties get a right to appeal, not a task-removing rule, and the interests of the system's owner are not examined. I found no passage that asks whether the owner can withdraw the mechanisms.
- **Buçinca.** The paper cites cognitive forcing functions as reducing over-reliance (p. 3), in line with the argument map's note on Buçinca et al.

## In conversation with

Cited by Zhu and in `../references.bib`:
- `green2022flaws`: oversight provisions assume humans can correct AI errors (p. 2).
- `parasuraman2010complacency`: complacent monitors versus over-intervening operators (p. 3).
- `bucinca2021trust`: cognitive forcing functions reduce over-reliance (p. 3).
- `lanham2023measuring`: source of the "reasoning faithfulness" notion (p. 4).
- `mitchell2019model`: model cards, cited for provenance and documentation mechanisms (Table 5).
- `santonidesio2018meaningful`: meaningful human control, the paper's stated starting point (pp. 2-3).

Leads not in the bib: Lee and See (2004) on appropriate reliance; Green and Chen (2019) on algorithm-in-the-loop decisions; Amershi et al. (2019) on human-AI interaction guidelines; Barandiaran, Di Paolo and Rohde (2009) on agency; Matthias (2004) on the responsibility gap.

## Caution

Do not cite this for evidence that any of its mechanisms works. The authors state that the evaluation is "interpretive rather than experimental" (p. 8) and that vendor documents show intended design, not practice (p. 19). The twelve cases are mostly commercial products documented by their makers. The paper concerns document evaluation by experts inside organisations, not platform users, and its examples (grant review, compliance checks, media monitoring) are not triads in which the system serves a party apart from the person using it. The concept of "agency" rests on one frame-dependent account (Abel et al., Barandiaran et al.). The author list in the bib is truncated ("and others"); the full list is Zhu, Lu, Ding, Lee and Wang. I did not open any of the vendor sources in the reference list.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the open-access publisher PDF (21 pp. plus a blank trailer; 'Page N of 21' headers match the card's locators). Checked 22 verbatim quotations (all exact, all page locators correct, including the abstract quote and the pp. 2, 3, 5, 8, 9, 10, 18, 19 passages), the dates (received 5 Nov 2025, accepted 15 Apr 2026, published 4 May 2026), 54 candidates screened and 12 cases retained, the count of Table 5 mechanisms (19 rows across pp. 11) and the 14 the card names, and the references to Green, Parasuraman and Manzey, Buçinca, Lanham, Mitchell, Santoni de Sio and van den Hoven, Barandiaran, Abel.

**Findings:** No issues found. The card's own caveats (Section 7 patterns and Tables 3 to 5 only skimmed; vendor sources not opened) are honest and limited, so full_text stands. Not verified: the card's reading that Zhu 'fits the pattern the argument map attributes to the Nadella post', which depends on the post, not the source.
