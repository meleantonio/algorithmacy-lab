# Simkute, A., Tankelevitch, L., Kewenig, V., Scott, A. E., Sellen, A., & Rintel, S. (2024). Ironies of generative AI: Understanding and mitigating productivity loss in human-AI interaction. *International Journal of Human–Computer Interaction*. Advance online publication. https://doi.org/10.1080/10447318.2024.2405782

**Identifier:** doi:10.1080/10447318.2024.2405782; preprint arXiv:2402.11364v1 · **Read depth:** full_text of the preprint (arXiv v1, 17 Feb 2024, 23 pages in ACM manuscript format, the only version on arXiv). The journal version (online 15 Oct 2024, pp. 1–22 per Crossref) is closed and was not seen; page locators below are the preprint's. I read the whole text and searched the reference list · **Source-tier:** peer-reviewed article (read as preprint) · **Evidence basis:** direct_read · **Design and sample:** none (narrative synthesis of Human Factors automation research and recent GenAI user studies, mostly on programming with GitHub Copilot) · **Parties modeled:** person–system (a user and a GenAI tool) · **Facets:** none (cited in DRAFT_v2 only) · **Read:** 2026-10-14

## What it argues

The paper maps Bainbridge's "ironies of automation" onto generative AI. Its claim is that GenAI's reported productivity losses repeat problems Human Factors research documented decades ago. It groups them into four challenges: "(i) the production-to-evaluation shift, (ii) unhelpful workflow restructuring, (iii) task interruptions, and (iv) task-complexity polarization" (p. 3), and proposes five remedies: "(i) continuous feedback, (ii) system personalization, (iii) ecological interface design, (iv) main task stabilization and timing, and (v) clear task allocation" (p. 3).

The first challenge is the one the draft uses. "In the context of GenAI, users' roles have shifted from producing output to evaluating it, often with little contextual information and situational awareness" (p. 2). Evaluation is hard because outputs are large, opaque and unreliable. Copilot users said the work "felt like a 'proofreading task'" (p. 4), and in one study "assessing the correctness of generated code created an efficiency bottleneck" (p. 5, summarising Vaithilingam et al.). GenAI systems "can introduce subtle or non-intuitive errors into outputs, particularly in long outputs such as multi-line code suggestions" (p. 6). The authors report complacency too: "some programmers reported skimming through the output rather than reading and evaluating the code rigorously" (p. 7).

On remedies, the paper asks for more feedback and more explanation, not less: "feedback is tied to carefully designed explainability features" (p. 13), with the caveat that "Feedback can be overwhelming if it is poorly presented or excessive" (p. 13). It also asks that tasks be allocated clearly between user and system (pp. 16–17). The authors call the paper "an initial bridge" between Human Factors and HCI (p. 17); there is no new data.

## Relation to the argument

**Supports the cost of reading output.** The production-to-evaluation shift is a clean statement of the inspection cost the draft attributes to text-generation tools: the user is turned into a reader and checker of machine output. That fits the draft's claim that a reading remedy adds reading.

**Cuts the other way on remedies.** Its first prescription is continuous feedback tied to explainability (p. 13), which is a disclosure-style remedy in D3's terms. The authors expect it to help situation awareness; they cite no test. So the source documents the reading burden and then proposes more legible output, not a change of convention. A reader of the paper should not take it as an ally of D3 beyond the diagnosis.

**Not a triad.** Every case is one user and one tool, mostly a programmer and Copilot. It cannot speak to mediated coordination (P11–P12).

**Use in DRAFT_v2:**
- **Line 35** ("Text-generation tools impose an output-inspection cost (Mozannar, Bansal, Fourney, & Horvitz, 2024; Simkute et al., 2024)"). Supported in substance: the production-to-evaluation shift (pp. 2, 4–7) is an inspection cost. Two qualifications. The evidence is mostly code generation, not "fluent, probabilistically generated text" in general; writing studies appear but are secondary (p. 3: "We focus primarily on programming"). And the paper is a synthesis of others' studies; it measures nothing itself. The next sentence ("Operators must read through fluent ... text to catch subtle errors") matches p. 6's "subtle or non-intuitive errors" for code.

## In conversation with

- `bainbridge1983ironies`: ref. [7], the paper's frame (p. 2).
- `parasuraman2000types`: ref. [93], cited among Human Factors mitigation work (p. 12).
- `endsley1995out`: not cited; the paper cites Endsley's 1995 measurement paper (ref. [35]) for situation awareness (p. 5).
- Leads not in the bib: Barke, James & Polikarpova 2023, "Grounded Copilot" (ref. [8], the most-used source); Vaithilingam, Zhang & Glassman 2022 on Copilot usability (ref. [118]); Sarkar et al. 2022, "What is it like to program with AI?" (ref. [109]); Endsley 2023, "Ironies of artificial intelligence" (ref. [37], the closest prior parallel); Woodruff et al. on knowledge workers' need to review GenAI output (ref. [126]).

## Caution

Read as the arXiv preprint; the journal version is closed, may differ in wording, structure and page count, and its locators are not these. The preprint's title differs slightly from the journal's ("interactions" vs "Interaction"). The paper is a narrative synthesis without a search protocol; the strength of its claims rests on the user studies it cites, several of them small qualitative studies. Crossref (checked 2026-10-14) still records no volume or issue, so "Advance online publication" in the draft's entry is current.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's saved arXiv v1 PDF (arXiv:2402.11364v1, 17 Feb 2024) with page breaks preserved (23 pages) and located every quotation by PDF page. Checked the reference numbers ([7], [8], [35], [37], [93], [109], [118], [123], [126]) against the reference list and the pages where [7], [35] and [93] are cited. Checked the record against Crossref (six authors as listed; *International Journal of Human–Computer Interaction*; online 2024-10-15; pages 1–22; no volume or issue). Re-read DRAFT_v2.md line 35 and the reference at line 687.

**Findings:**
1. The five remedies were paraphrased with one item misnamed ("task stabilization and interruption timing"); the preprint lists "(iv) main task stabilization and timing" (p. 3). Replaced with the exact list.
2. All quotations verified verbatim on the stated preprint pages: the four challenges (p. 3), "users' roles have shifted ..." (p. 2), "proofreading task" (p. 4, attributed in the paper to Weisz et al., ref. [123]), "efficiency bottleneck" (p. 5, Vaithilingam et al. [118]), "subtle or non-intuitive errors" (p. 6), "skimming through the output" (p. 7), the two feedback sentences (p. 13), "an initial bridge" (p. 17), "We focus primarily on programming" (p. 3).
3. Reference-list links verified: Bainbridge [7] cited p. 2; Endsley 1995 [35] p. 5; Parasuraman et al. [93] p. 12; leads [8], [37], [109], [118], [126] match the list.
4. Read depth (full text of the preprint, journal version not seen) is accurate.
5. Use in DRAFT_v2 (line 35): verdict stands. The production-to-evaluation shift supports an output-inspection cost, with the stated qualifications (mostly code, a synthesis with no data of its own). The card rightly flags that the paper's remedy, explainability-tied feedback, runs against D3.
