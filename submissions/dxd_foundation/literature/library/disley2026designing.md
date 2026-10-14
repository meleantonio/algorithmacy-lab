# Disley, M., & Khan, M. (2026). Designing cognitive friction with concept suppression in large language models. *Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/07370024.2026.2708617

**Identifier:** doi:10.1080/07370024.2026.2708617 · **Read depth:** full_text (the published version of record, CC BY 4.0, published online 21 Sep 2026, 42 journal pages plus a T&F cover sheet, obtained from the UAL Research Online repository (eprint 27844) because the tandfonline.com PDF link returned a bot wall (HTTP 403); local copy `dxd_foundation_local/pdfs/round4/disley2026.pdf`. Pagination is the journal's (pdf page n = p. n − 1). I read §§1–8 in full, Tables 1–9 and the behavioural-validation appendix tables; Figures 1–6 through captions and text; the reference list scanned) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** a system (Llama-3.2-3B-Instruct with "chair" suppressed by concept-saliency pruning, vocabulary pruning and repair fine-tuning) and a within-subject study, three 15-minute conditions in Latin-square order (unaided; unmodified Llama3.2:3b; the suppressed model "Unlearning to Rest"); 47 recruited, 38 completed, N = 37 analysed (26 students of UAL's undergraduate Diploma in Creative Computing in a classroom session; 11 University of Edinburgh postgraduates in one-to-one video sessions with think-aloud) (p. 15); not blinded; outcomes are a NASA-TLX-like 21-point self-report with one added ownership item, and coded free text · **Parties modeled:** person–system · **Facets:** none yet (cited in DRAFT_v2 §2.2) · **Read:** 2026-10-14

## What it argues

Disley and Khan argue that a fluent language model can "collapse early-stage ideation into selection and curation" and propose to restore effort by editing the model itself: "treating the learned conceptual manifold of a pre-trained model as a design surface for human–AI interaction" (abstract, p. 1). The friction they want "need not arise from making systems less capable, but from shaping when and how their capabilities are deployed" (p. 2). They contrast this with friction placed "into the interface or the interaction sequence – an added step, a delay, a reframed prompt" (§2.3, p. 5), and use Gärdenfors' conceptual spaces "as a diagnostic geometry, not because LLMs implement them" (p. 7).

Results (Tables 1–3, p. 19; text pp. 20–22):

- **Mental Demand**: lowest with the unmodified model (7.24), higher with Unlearning to Rest (10.19) and unaided (11.49); omnibus F(2, 72) = 12.62, p < .001. Unlearning to Rest did not differ from unaided (pFDR = 0.1868).
- **Effort**: 7.65 vs 10.76 vs 10.70; F = 7.95, p < .001; Unlearning to Rest vs unaided not different (pFDR = 0.9471).
- **Ownership** (one item): 6.38 vs 9.16 vs 11.49; F = 12.43, p < .001; all three pairs differ after correction, unaided above Unlearning to Rest (g = 0.425).
- **Frustration** was highest with Unlearning to Rest (9.54) but the omnibus test was not significant (p = 0.094); Performance and Temporal Demand were not significant either.
- Qualitatively, most participants described the suppressed concept as a "productive constraint" that pushed them to re-frame "what a chair is"; a minority, "represented by two extracts", treated it as a defect and tried to teach the model (pp. 24–26). Participants proposed a "stage-fit" use: the constrained model early, the fluent one for development (p. 26).

Relative to the fluent model, Unlearning to Rest "recovered just over half of the ownership lost to fluent assistance" (p. 31). Their limits are explicit: "We did not operationalize fixation, novelty, or diversity directly. Claims about 'defixation' or 'increased creativity' would therefore be overreaching" (§7.8, p. 34); "Our contribution is to establish the mechanism and demonstrate feasibility" (p. 32). Participants knew which condition used the modified model (p. 15).

## Relation to the argument

**Premise P5 and the word-separation precedent.** This is the closest recent HCI paper to the draft's "re-representation" move, and it runs the other way. Word separation re-represented the page to remove work from the reader; Disley and Khan re-shape the model's representation to return work to the user. Both locate the intervention in the representation rather than in a disclosure or a training regime, which supports the draft's broader claim that representation is a design site distinct from explanation (D3). It does not test a triad, a mediator with its own objective, or any measure of decision quality.

**Ruling D7 and P9.** The paper's case for friction rests on effort and ownership, not on feedback from acting. It is about ideation, where there is no correct answer to learn from, so it neither supports nor cuts the "understand by deciding" claim.

**Use in DRAFT_v2:**

- **Line 39** ("Disley and Khan (2026) reframe system representations as an active 'design surface,' showing that selectively suppressing a concept in a model can introduce productive cognitive friction"). **"Design surface" is the authors' phrase** (abstract, p. 1; §3.1, p. 7; §7.5, p. 32). **"Showing … productive cognitive friction" overstates the evidence.** What the study shows is that suppression held self-reported mental demand and effort at unaided levels while ownership (one item) rose relative to the fluent model (pp. 19–21); "productive" rests on participants' own descriptions, in an unblinded study, and the authors disclaim claims about creativity or defixation (p. 34). "Report that … participants experienced as productive friction" would match the source. Also, the representation suppressed is the model's internal one, not a representation shown to the user; "system representations" is accurate only in that sense.
- **Reference-list entry (line 549):** both initials are wrong. The authors are **Martin** Disley and **Murad** Khan, so "Disley, S., & Khan, H." should be "Disley, M., & Khan, M." (Crossref record and the article's byline, p. 1). Crossref gives pages 1–42 for the online version; no volume or issue yet.

## In conversation with

- `bucinca2021trust` — not cited by this name in the text I read; the paper reaches cognitive forcing through Lee et al. (2025) (p. 6), in the same line as Buçinca et al.
- `cox2016design` — cited for "microboundaries", small frictions placed before an action (§2.3, p. 5); the interface-level friction the authors set against their own.
- `appleton2023sketchbook` — cited on tools for thought (p. 6).
- `hutchins1995cognition` — cited on distributed cognition and cognitive prostheses (p. 2).
- Not in the bib, as leads: Bjork & Bjork (2011) on desirable difficulties; Doshi & Hauser (2024) and Anderson et al. (2024) on homogenization; Tankelevitch et al. (2025) on "challenge-oriented" AI; Shin et al. (2025), 280 designers, no gain in problem framing from LLM use; Qin et al. (2025) on timing of LLM introduction in ideation.

## Caution

Self-report only, one ownership item, 15-minute sessions, one domain (furniture) and one suppressed concept; small, mostly student sample from the authors' institutions; not blinded, so demand effects are possible; two cohorts run differently (classroom vs one-to-one with think-aloud). Transcript coding was LLM-assisted (GPT-5.2) against a human-built codebook (pp. 18–19). No output-quality analysis. Very recent (online 21 Sep 2026); no replications.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's local copy (`dxd_foundation_local/pdfs/round4/disley2026.pdf` / `.txt`: the T&F version of record, CC BY 4.0, published online 21 Sep 2026, cover sheet plus 42 journal pages; text index confirms pdf p. n = journal p. n − 1). Located every quotation and number by page: abstract (p. 1), "need not arise …" (p. 2), "into the interface or the interaction sequence" (p. 5), "as a diagnostic geometry" (p. 7), sample (p. 15), Latin square and 15-minute sessions (p. 16), Tables 1–3 (p. 19), pFDR 0.1868 and 0.9471 (p. 22), "represented by two extracts" (p. 26), "recovered just over half" and g = 0.425 (p. 31), "establish the mechanism and demonstrate feasibility" (p. 32), the defixation disclaimer (p. 34), the non-blinding statement (p. 15), GPT-5.2 coding (p. 19). Checked the record against Crossref (Martin Disley, Murad Khan; *Human–Computer Interaction*, online 21 Sep 2026, pp. 1–42). Re-read DRAFT_v2.md line 39 and the reference at line 549.

**Findings:**

1. All quotations verbatim; all means (7.24/10.19/11.49; 7.65/10.76/10.70; 6.38/9.16/11.49; frustration 9.54), omnibus F values (12.62, 7.95, 12.43; df 2, 72), p-values and effect sizes match Tables 1–3 and pp. 20–22.
2. Reference-list error understated: the card corrected only the first author's initial. DRAFT_v2 line 549 has "Disley, S., & Khan, H."; Crossref and the byline give Martin Disley and **Murad** Khan, so both initials are wrong ("Disley, M., & Khan, M."). Fixed in the Use-in-DRAFT_v2 note.
3. Sample detail tightened: 47 recruited, 38 completed every part, one excluded, N = 37 (p. 15); the UAL cohort were students of an undergraduate Diploma in Creative Computing. Fixed in the header.
4. Use-in-DRAFT_v2 verdict on line 39 confirmed: "design surface" is the authors' phrase (p. 1 and later); "showing … productive cognitive friction" overstates a self-report, unblinded study whose authors disclaim claims about defixation or creativity (p. 34). Read depth (full text) is consistent with the copy.

