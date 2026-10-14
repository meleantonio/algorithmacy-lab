# V2: management, organization theory and information systems journals

*Written by Claude (research agent V2) on 2026-10-13 for `venue/BRIEF.md`. Everything below comes from pages or database records opened this session. Where a source was blocked I say "not verified". I did not use Chrome tools and did not try to get round any wall.*

## How to read the evidence

- **Opened** = I read the page text myself (curl or fetch). **Mirror** = the page was SAGE's own submission-guidelines text hosted at `sage.cnpereading.com`, because `journals.sagepub.com` returns 403. The mirror carries template residue (lorem ipsum, "tags to display this section"), so I use it only for statements that read as the journal's own.
- **Blocked** (HTTP 403 or a Cloudflare challenge): all of `journals.sagepub.com`, INFORMS (`pubsonline.informs.org`), Wiley (`onlinelibrary.wiley.com`), ScienceDirect, `misq.umn.edu`, `tandfonline.com`, `journals.aom.org`, `scimagojr.com`, `ft.com`. I recorded the block and did not try to work round it.
- **Fit evidence** comes from Crossref queries by ISSN (2023 onward). I list only records that Crossref returned. Crossref does not say whether a piece is conceptual or empirical; where I say "theory" or "conceptual" it is from the title or from knowing the format, and I mark it "(title only)".
- **Rankings, shared across sections.**
  - ABDC: 2025 Journal Quality List, "current to September 2026" (file `ABDC-JQL-2025-v3-210926.xlsx`, downloaded from `https://abdc.edu.au/abdc-journal-quality-list/`). Every ABDC grade below is read from that file.
  - UTD 24: the list on `https://jsom.utdallas.edu/the-utd-top-100-business-school-research-rankings/` (opened). In this cluster it contains Information Systems Research, MIS Quarterly, Academy of Management Review and Organization Science, and none of the other journals here.
  - FT50: `ft.com` was blocked. I used the Bodleian Libraries guide `https://libguides.bodleian.ox.ac.uk/ft-top50` (secondary; "last updated May 14, 2026"; the author of the guide links the 2016 FT list). Its 50 entries in this cluster: AMR, ISR, JMIS, JMS, MISQ, Organization Science, Research Policy, MIT Sloan Management Review. Its "Journals Removed from the FT50 - 2026" section lists Human Relations, Journal of Business Ethics and Organization Studies.
  - **ABS/CABS Academic Journal Guide, Scimago SJR quartile, impact factors: not verified for any journal.** The ABS guide needs a login; Scimago and the publishers' pages were blocked. I found no journal-stated impact factor on any page I could open.
  - **Bentley University**: I found no Bentley list of target journals. A search result (not opened) described a Bentley job posting that names journals where its faculty have published, including AMJ, SMJ, Organization Science, MIS Quarterly, Research Policy, and Business Ethics Quarterly. That is a faculty publication list, not a programme requirement. Not verified.

### Rankings table

| Journal | ABDC 2025 | FT50 (secondary) | UTD 24 | ABS | SJR | JIF |
|---|---|---|---|---|---|---|
| Academy of Management Review | A* | yes | yes | nv | nv | nv |
| Academy of Management Perspectives | A | no | no | nv | nv | nv |
| Organization Science | A* | yes | yes | nv | nv | nv |
| Organization Theory | A | no | no | nv | nv | nv |
| Organization Studies | A* | removed 2026 | no | nv | nv | nv |
| Journal of Management Studies | A* | yes | no | nv | nv | nv |
| Journal of Management Inquiry | A | no | no | nv | nv | nv |
| MIS Quarterly | A* | yes | yes | nv | nv | nv |
| Information Systems Research | A* | yes | yes | nv | nv | nv |
| Journal of the Association for Information Systems | A* | no | no | nv | nv | nv |
| Journal of Information Technology | A* | no | no | nv | nv | nv |
| Information and Organization | A* | no | no | nv | nv | nv |
| Information Systems Journal | A* | no | no | nv | nv | nv |
| Journal of Management Information Systems | A* | yes | no | nv | nv | nv |
| Research Policy | A* | yes | no | nv | nv | nv |
| California Management Review | A | no | no | nv | nv | nv |
| MIT Sloan Management Review | A | yes | no | nv | nv | nv |

nv = not verified. Others checked in ABDC only: Academy of Management Annals A*, Academy of Management Discoveries A*, Human Relations A*, Organization A, Strategic Organization A, Journal of Business Ethics A, Journal of Strategic Information Systems A*, European Journal of Information Systems A*, MIS Quarterly Executive A, Communications of the AIS A. *Big Data & Society* is not in the ABDC file.

## Generative-AI policies that apply across several journals

**Academy of Management (AMR, AMP), exact text.** Page `https://www.aom.org/publications/journals/publishing-with-aom/author-and-reviewer-resources/author-resources/submitting-to-review/` (opened):

> "All work submitted to AOM must be created by the authors and not the product of artificial intelligence tools unless appropriate to the research question and is properly cited. Authors must be transparent in disclosing any AI use in the manuscript cover letter and in the article acknowledgements. Authors must also confirm that they read and understand AOM's AI policy."

The AMJ page carries a slightly different wording: "...must be created by the authors and must not be the product of artificial intelligence tools—unless it is appropriate to the research question and properly cited."

The full AOM policy, `https://www.aom.org/publications/journals/publishing-with-aom/aom-artificial-intelligence-policy/` (opened), says in part:

> "Authors may use AI tools in their research, but AI cannot replace human judgment or accountability at any stage of the research process."
> "Follow a two-step process when reporting the use of AI in their research: a. Disclosure: For each stage of the research process, authors must identify whether AI tools were used; b. Accountability: If AI tools were used, authors must explicitly confirm that they carefully reviewed, verified, and accepted any AI-involved output."
> The stages are "Conceptualization — Idea generation, problem framing, literature review, or theoretical development", Research Design, Data Preparation and Analysis, Presentation of Results, and "Writing and Editing — Drafting, refining, or finalizing manuscripts."
> "Clearly indicate the use of language models in the manuscript cover letter and acknowledgements (for journal submissions)... including which model was used and for what purpose."
> "Provide a list of sources used to generate content and citations, including those generated by language models."
> "We will take appropriate corrective action where we identify published articles with undisclosed use of such tools."

**Consequence for this paper.** The abstract, introduction and outline were drafted by Gemini and Claude, and the literature review was run by agents. Under the AOM policy that is AI use at the Conceptualization (literature review, theoretical development) and Writing stages, and the opening sentence demands that the work be "created by the authors". An AOM submission would need the author's own rewritten text, a stage-by-stage disclosure, and the author's explicit confirmation that he reviewed and accepted every AI-involved output.

**Sage (Organization Theory, Organization Studies, Journal of Management Inquiry, Journal of Information Technology, California Management Review).** Page `https://us.sagepub.com/en-us/nam/artificial-intelligence-policy` (opened):

> "We distinguish various uses for AI and related technologies as: assistive (and no longer requiring disclosure), generative (requiring disclosure), and prohibitive."
> "The primary or partial use of AI tools and/or LLMs that produce content such as references, text, images, or any other content that directly impacts the research methodology, analysis, results and/or conclusions must be disclosed upon submission so the editorial team can evaluate the content generated."
> Disclosure "within the methods or acknowledgements" is listed for "Assistance with literature review or compilation of relevant sources" and "Assistance with compilation of references".
> "While submissions will not be rejected solely because of the disclosed use of GenAI tools, if the editor becomes aware that GenAI was inappropriately used in the preparation of a submission without disclosure, the editor reserves the right to reject the submission at any time during the publishing process."
> Inappropriate use includes "Generation of incorrect text or content" and "Fabricated references or falsified claims".

The journal pages add: "AI chatbots, for example ChatGPT, should not be listed as authors."

**Elsevier (Information and Organization, Research Policy).** Page `https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals` (opened):

> "Authors preparing a manuscript for an Elsevier journal can use AI tools to support them in these tasks. However, these tools must never be used as a substitute for human critical thinking, expertise and evaluation."
> "for the use of AI tools we require a disclosure statement upon submission."
> "Authors should disclose the use of AI tools for manuscript preparation in a separate AI declaration statement included in their manuscript upon submission. This statement will appear in the published article to ensure transparency. Authors should document their use of AI, including the name of the AI tool used, the purpose of its use, and the extent of their oversight."
> "Basic checks of grammar, spelling and punctuation do not need a declaration statement. However, when an AI tool makes substantive changes to sentence structure or organization of a part of the text, this should be disclosed."

**Wiley (Journal of Management Studies, Information Systems Journal).** Page `https://www.wiley.com/en-us/publish/article/ai-guidelines/` (opened): "Wiley requires disclosure of AI when used to generate substantial text or restructure arguments." Disclosure goes "In your Acknowledgments when AI assists with manuscript drafting, editing, translation, or formatting" and "In your Methods when AI is used to assist with your research methodology, data collection or analysis, or literature review processes." Text generation, restructuring arguments and "identif[ying] gaps in argument structure" require disclosure; grammar and spelling correction do not.

**Taylor & Francis (Journal of Management Information Systems).** Page `https://taylorandfrancis.com/our-policies/ai-policy/` (opened): T&F supports use for "Idea generation and idea exploration", "Copyediting, language improvement and translations", "Literature classification" and "Coding assistance". "Authors must clearly acknowledge within the article or book any use of Generative AI tools through a statement that includes: the full name of the tool used (with version number), how it was used and the reason for use." Authors should not submit work with "Text or code generation without rigorous revision". "Note that some journals may not allow use of Generative AI tools beyond language improvement."

**INFORMS (Organization Science, Information Systems Research): not verified.** The INFORMS pages were blocked. A web search returned INFORMS reviewer and editor rules (do not upload manuscripts to AI tools) and other INFORMS journals' author wording, but no Organization Science or ISR author policy.

**AIS (JAIS) and MIS Quarterly: not verified.** I found no generative-AI policy on the JAIS policies page or the JAIS "Manuscript Categories and Information for Authors" page (both opened; the policies page lists Archiving, Green Open Access, Data Policies, Code of Research Conduct, Copyright, Appeals). MIS Quarterly's own site was blocked. For the sister practitioner journal MIS Quarterly Executive, `https://aisel.aisnet.org/misqe/publication_ethics.html` (opened) says: "MISQE encourages the use of novel technologies, including generative AI. All authors must be humans. Authors are singularly responsible for the integrity and originality of their work." That is MISQE, not MISQ, and I do not apply it to MISQ.

---

## 1. Academy of Management Review (AMR)

1. **Publisher, ISSN, access.** Academy of Management; ISSN 0363-7425 / 1930-3807 (Crossref). Subscription journal; APC not stated on the page I read. Not verified.
2. **Scope.** "Academy of Management Review (AMR) is a theory development journal for global management and organization scholars. AMR publishes novel, insightful and carefully crafted conceptual articles that challenge conventional wisdom concerning all aspects of organizations and their role in society. AMR is particularly interested in interesting and important theoretical advances that incorporate thought from multiple disciplines or areas within management." (`aom.org/.../submitting-to-review/`)
3. **Conceptual papers.** Yes, conceptual only. "AMR articles advance theory ... through developing new theories, significantly challenging current theory, synthesizing recent advances and ideas into current theory, initiating a search for new theory by pointing out and carefully delineating a novel type of problem, or crafting ways to improve the process of theory development." "Formal research propositions are not required." Length: "initial submissions should not be more than 30 double-spaced pages, excluding references, tables, and figures"; "a contribution-to-length ratio will be assessed". No proposal or pre-submission enquiry. One-submission rule: "Papers can be submitted to AMR only once"; authors "are expected to reciprocate by reviewing for AMR if called upon." Working papers must be taken down during review. No page says anything about author status (sole author, doctoral student); not stated.
4. **Fit evidence (Crossref, ISSN 0363-7425).**
   - Lu, Yan (2026). "Syncing Minds and Machines: Hybrid Cognitive Alignment as an Emergent Coordination Mechanism in Human–AI Collaboration." doi:10.5465/amr.2024.0546
   - Chen, Zhou, Chan (2026). "Algorithm Envelopment in Platform Markets." doi:10.5465/amr.2023.0156
   - Grote, Parker, Crowston (2026). "Taming Artificial Intelligence: A Theory of Control-Accountability Alignment among AI Developers and Users." doi:10.5465/amr.2023.0117
   - Leavitt, Barnes, Shapiro (2025). "The Role of Human Managers within Algorithmic Performance Management Systems: A Process Model of Employee Trust in Managers through Reflexivity." doi:10.5465/amr.2022.0058
   - Raisch, Fomina (2025). "Combining Human and Artificial Intelligence: Hybrid Problem-Solving in Organizations." doi:10.5465/amr.2021.0421
   - Gregory, Beck, Henfridsson, Yaraghi (2025). "Cooperation among Strangers: Algorithmic Enforcement of Reciprocal Exchange with Blockchain-Based Smart Contracts." doi:10.5465/amr.2023.0023
   The topic is clearly live in AMR. None of these uses a human-factors or design framing (title only).
5. **Special issues / CFPs.** None found. I did not open an AOM calls page. Not verified.
6. **Review model, speed, acceptance.** Peer review; double-blind by instruction ("title page and all author-identifying references have been removed"). Time to first decision and acceptance rate: not stated on the page. Not verified.
7. **AI policy.** See the AOM block above, quoted exactly.
8. **Fit: workable in topic, hard in form.** Topic fit is good: AMR is publishing human–AI coordination and algorithmic-platform theory right now, and DXD plus the literacy/algorithmacy boundary is a theory claim. The obstacles are three. First, a theory contribution to management and organization is required; a human-factors argument about re-representation (the medieval-spacing precedent, distributed cognition) would be read as an import unless it is recast as a claim about organizing and coordination. Second, the AOM AI rule requires that the work be "created by the authors", which the Gemini-written abstract and introduction do not satisfy as they stand. Third, one submission only, and the paper proposes an experiment and runs none, so the theory must carry the whole contribution. To submit, the author would rewrite the abstract and introduction himself, drop or shrink the history-of-reading section to what the coordination argument needs, and cut to about 30 pages excluding references.

## 2. Academy of Management Perspectives (AMP)

1. **Publisher, ISSN.** Academy of Management; ISSN 1558-9080 / 1943-4529 (Crossref). APC not verified.
2. **Scope.** Page `aom.org/.../submitting-to-perspectives/` (opened): manuscripts must be "Relevant: ... an issue that matters to managers." "AMP does not publish theory driven papers, even if they have managerial implications tacked on." "AMP does not publish opinion pieces, or practical translations of previously published studies."
3. **Conceptual papers.** "AMP articles may be empirical or conceptual. ... Conceptual analysis is used in AMP to systematically organize relevant literature into novel perspectives that aid practical understanding of managerial problems." "An AMP manuscript should be no longer than 20 double-spaced pages." Types: Standard Articles, Constructive Confrontations, Practitioner Perspectives, Book Briefs. No proposal required on the page.
4. **Fit evidence (ISSN 1558-9080).** Atanassova, Khan, Khan (2026), "When Should Your Team Override AI? A Trust Calibration Routine," doi:10.5465/amp.2025.0019; Lavie, Pollicino, Valletti (2025), "Certification of Business Practices and Algorithms as a Complementary Approach to Platform Regulation," doi:10.5465/amp.2023.0421; Hutzschenreuter, Lämmermann (2025), "What Is Your AI Strategy?..." doi:10.5465/amp.2023.0243; Cennamo, Gianiodis, Kretschmer, McIntyre (2025), "Platform Regulation: Beyond Power and Size," doi:10.5465/amp.2025.0261. These are policy and practice pieces.
5. **CFPs.** None found.
6. **Review, speed, acceptance.** Not verified.
7. **AI policy.** AOM block above.
8. **Fit: poor.** The paper is a theory paper and AMP excludes theory-driven work. The practical angle (what designers and regulators should do about disclosure) would have to become the whole paper, with a managerial reader, 20 pages, and rigorous original analysis.

## 3. Organization Science

1. **Publisher, ISSN, access.** INFORMS; ISSN 1047-7039 / 1526-5455 (Crossref). APC not verified (page blocked).
2. **Scope.** Not opened (INFORMS blocked). A search result summarised the Editorial Statement as covering "fundamental research on organizations" and being "receptive to a broad range of theoretical perspectives". Secondary; not verified.
3. **Conceptual papers.** Not verified for article types. A search result reported the guideline "under 50 double-spaced pages ... all-inclusive, or 40 pages in 11-point font" (secondary). My Crossref sample shows empirical papers on algorithmic topics. I found no pure-theory paper with algorithms in the 2023–2026 results.
4. **Fit evidence (ISSN 1047-7039).** Sundaresan, Guler (2025), "Algorithmic Recommendation Tools and Experiential Learning in Clinical Care," doi:10.1287/orsc.2022.16738; Burbano, Koo, Luo (2026), "A Platform Rating System and Vulnerable Workers: Evidence from Field Experiments in Singapore," doi:10.1287/orsc.2023.18153; van Angeren, Karunakaran (2023), "Anchored Inferential Learning: Platform-Specific Uncertainty, Venture Capital Investments by the Platform Owner, and the Impact on Complementors," doi:10.1287/orsc.2022.1607. All appear to be empirical (title only).
5. **CFPs.** Not verified.
6. **Review, speed, acceptance.** Double-blind per search result. Not verified.
7. **AI policy.** Not verified (INFORMS).
8. **Fit: poor to unverified.** Organization Science is a data-led journal and I found no conceptual precedent in the sample. A sole-author, no-data paper that proposes an experiment is a weak match unless the experiment is run. Its ABDC A*, FT50 and UTD24 standing make it a prestige target only if the experiment exists.

## 4. Organization Theory (OT; Sage / EGOS)

1. **Publisher, ISSN, access.** Sage, in collaboration with EGOS; ISSN 2631-7877 (Crossref). Fully open access. "The Article Processing Charge (APC) is $1000 USD. Article Processing Charges discounts up to 100% might apply depending on the affiliation of the lead author and the respective institutional arrangements in place." "in case you do not have institutional funds to cover APCs ... the European Group for Organization Studies (EGOS) might be able to offer financial support." No charge for submitting. (mirror of `journals.sagepub.com/author-instructions/ott`)
2. **Scope.** "OT publishes work in all areas of organization theory, including papers that develop new substantive theories or offer theoretical extensions." The full Aims & Scope page was not retrievable. (mirror)
3. **Conceptual papers.** Yes, it is the main type. "Submissions to OT fall in three categories: regular full-length submissions ('theory article'); review papers ('review article'), and shorter, essay-style contributions ... ('controversies and conversations')." "OT publishes theory articles on different subjects within the broad domains of organizations (in their environment), processes of organizing, and the organized, including work within subject areas such as strategy, organizational behavior, work and employment relations, human resource management, ..." "Submissions to OT may feature different approaches to theory development, including approaches centred on proposition development, process theorizing, or on a theoretical critique and synthesis of the existing literature." Limit: "Submissions should generally not exceed 11,000 words (including references), although in some cases longer versions may be accepted." No proposal for theory or review articles; only Controversies and Conversations needs one. Organization Studies directs authors here: "Conceptual and theory papers can be submitted to our sibling Journal: Organization Theory."
4. **Fit evidence (ISSN 2631-7877).**
   - Stark, Vanden Broeck (2024). "Principles of Algorithmic Management." doi:10.1177/26317877241257213
   - Hinds, von Krogh (2024). "Generative AI, Emerging Technology, and Organizing: Towards a theory of progressive encapsulation." doi:10.1177/26317877241293478
   - Orlikowski, Scott (2023). "The Digital Undertow and Institutional Displacement: A Sociomaterial Approach." doi:10.1177/26317877231180898
   - Justesen, Plesner (2024). "Invisible Digi-Work: Compensating, connecting, and cleaning in digitalized organizations." doi:10.1177/26317877241235938
   - Grodal, Ha, Hood, Rajunov (2024). "Between Humans and Machines: The social construction of the generative AI category." doi:10.1177/26317877241275125
   - Hsu, Bechky (2024). "Exploring the Digital Undertow: How generative AI impacts social categorizations in creative work." doi:10.1177/26317877241275118
   This is the closest cluster of any journal I searched: a 2024 run of theory papers on AI and organizing, and an algorithmic-management theory paper.
5. **CFPs.** None found. OT's own calls page was blocked. Not verified.
6. **Review model, speed, acceptance.** "Identity transparency: Double anonymized." "Two independent reviews are required for a manuscript to reach a Revise or Accept decision." "All manuscripts are reviewed as rapidly as possible, while maintaining rigor." No time to first decision or acceptance rate on the page; Sage shows one on the journal homepage, which was blocked. Not verified.
7. **AI policy.** The Sage block above. The journal page links to the Sage policy and says chatbots cannot be authors.
8. **Fit: strong.** OT states that it publishes theory with no data, takes a "theoretical critique and synthesis" route, has no proposal step for theory articles, and has a 2024 run of AI-and-organizing theory. The paper's own diagnostic in `DRAFT.md` already names OT as the register. The main obstacle is framing: OT's domain is "organizations, processes of organizing, and the organized". A paper that opens on human-factors design and ends on an experiment must lead with the triadic coordination problem and the platform-governance comparison (courts, FX dealers, platforms; section 7), and treat word separation and distributed cognition as the precedent, not the thesis. The ABDC grade is A, not A*; OT is outside FT50 and UTD24. Cut to 11,000 words including references.

## 5. Organization Studies

1. **Publisher, ISSN, access.** Sage; ISSN 0170-8406 / 1741-3044. "There are no fees payable to submit or publish in this journal." Optional open access by fee.
2. **Scope.** The scope text was not retrievable (mirror links out).
3. **Conceptual papers.** No. "From June 2025, we welcome empirical research articles only. Conceptual and theory papers can be submitted to our sibling Journal: Organization Theory." Other types: "X and Organization Studies" essays (7,500 words), Perspectives (13,000), Method/ology (13,000), Agora (2,000 words), media reviews. Research articles 13,000 words including references.
4. **Fit evidence (ISSN 0170-8406).** Brossard (2026), "Emancipatory Agency and Rebalancing of Power in Algorithmic Systems: A Simondonian perspective," doi:10.1177/01708406261459055; Lu, Kjellberg, Strom (2026), "Seeing like a Platform: Netflix and the reorganizing of markets for audiovisual production and consumption," doi:10.1177/01708406261488553. Neither is clearly comparable.
5. **CFPs.** None found.
6. **Review.** Double-anonymized; "Two independent reviews are required before a Revise or Accept decision." Speed and acceptance not verified.
7. **AI policy.** Sage block.
8. **Fit: poor.** The journal now refuses conceptual papers. It was also removed from the FT50 in 2026 (Bodleian guide, secondary).

## 6. Journal of Management Studies (JMS)

1. **Publisher, ISSN.** Wiley; ISSN 0022-2380 / 1467-6486. Access model and APC not verified (Wiley blocked).
2. **Scope.** Not verified (blocked).
3. **Conceptual papers.** Not verified from an official page. A vLex copy of the journal's notes for contributors (undated; secondary; not opened by me beyond the search snippet) gave "usually between 7,000 and 11,000 words" and said "papers submitted ... with a length exceeding 15,000 words may be returned". JMS publishes theory papers in practice (see Wu and Teece below), but I could not confirm article types.
4. **Fit evidence (ISSN 0022-2380).** Lindebaum, Moser, Islam (2023), "Big Data, Proxies, Algorithmic Decision-Making and the Future of Management Theory," doi:10.1111/joms.13032; Stelmaszak, Joshi, Constantiou (2025), "Artificial Intelligence as an Organizing Capability Arising from Human-Algorithm Relations," doi:10.1111/joms.70003; Humberd, Latham (2025), "When AI Becomes an Agent of the Firm: Examining the Evolution of AI in Organizations Through an Agency Theory Lens," doi:10.1111/joms.13274; Wu (2026), "Algorithmic Status Inequality: An Integrative Perspective on AI-Driven Social Stratification," doi:10.1111/joms.70134; Teece (2026), "Algorithmic Status Inequality Through a Dynamic Capabilities Lens: A Market-Based Perspective," doi:10.1111/joms.70136; Benischke, Post (2026), "From Platform Design to Attention Governance: Rethinking Social Media Externalities," doi:10.1111/joms.70118. A search also returned a JMS special-issue PDF on AI in organizations (`onlinelibrary.wiley.com/pb-assets/assets/14676486/JMS%20SI-AI%20Call%20for%20Papers-1659516051077.pdf`), probably from about 2022; I did not open it and its deadline is not verified.
5. **CFPs.** Not verified (see above).
6. **Review, speed, acceptance.** Not verified.
7. **AI policy.** Wiley block.
8. **Fit: workable, unverified.** JMS carries management theory on AI and algorithms and is ABDC A* and in the FT50, but I could not read its scope or article types. Obstacle: same as AMR (needs a management contribution), plus the unknown length and article-type rules.

## 7. Journal of Management Inquiry (JMI)

1. **Publisher, ISSN, access.** Sage; ISSN 1056-4926 / 1552-6542. Subscription; "There are no fees payable to submit or publish in this journal." Optional open access by fee (mirror).
2. **Scope.** Not retrievable.
3. **Conceptual papers.** The mirror says only: "The Journal of Management Inquiry publishes full length articles, research notes and editorials." No word limit found. Not verified.
4. **Fit evidence (ISSN 1056-4926).** Baum (2026), "The Appearance of Knowing: Why Epistemic Technologies Demand New Organization Theory," doi:10.1177/10564926261460391 (title only: theory, AI); Ocasio (2024), "Attentional Control: Institutions, Management, Organizations, and Algorithms," doi:10.1177/10564926241278520; Bathini, Parth, Kandathil (2026), "The Legitimacy Lie as Dark Institutional Work: Rhetoric and Reality in India's Platform Economy," doi:10.1177/10564926261427991; Bunders, De Moor (2023), "Paradoxical Tensions as a Double-Edged Sword: ... Platform Cooperatives in the European Gig Economy," doi:10.1177/10564926231202422.
5. **CFPs.** None found.
6. **Review.** "Identity transparency: Double anonymized." Speed and acceptance not verified.
7. **AI policy.** Sage block.
8. **Fit: workable, unverified.** JMI takes essays and conceptual work, and Baum (2026) shows it takes theory on AI. I could not read its length limits or section types. A reasonable second tier after OT, but the data are thin.

## 8. MIS Quarterly (MISQ)

1. **Publisher, ISSN.** MIS Quarterly (University of Minnesota Press per ABDC); ISSN 0276-7783 / 2162-9730. Access and APC not verified.
2. **Scope.** Not verified (site blocked).
3. **Conceptual papers.** Probably yes, through the Theory and Review track, but the official category page `misq.umn.edu/categories` returned 403. Secondary only, from search results: the Theory and Review materials recommend a brief proposal of about 5 to 10 pages to the department editor before a full manuscript; a 2014-era editorial said MISQ gets few "pure theory" manuscripts and encourages them; a MISQ editorial describes Research Curations as 3-to-4-page syntheses that "do not ... build new theory" (so a curation is the wrong vehicle). I did not open those documents. Page limits: not verified. A third-party skill file listed 55 and 65 pages; I discard it as unofficial. I found no official page for "Issues and Opinions".
4. **Fit evidence (ISSN 0276-7783).**
   - Grisold, Berente, Seidel (2025). "Guardrails for Human-AI Ecologies: Norm-Based Coordination and Design for Predictability." doi:10.25300/misq/2025/18058 (closest in framing: coordination plus design)
   - Rai, Tian, Xue (2026). "FAIR: A Design Theory for Artificial Intelligence Fairness." doi:10.25300/misq/2026/17971
   - Stelmaszak, Möhlmann, Sørensen (2025). "When Algorithms Delegate to Humans: Exploring Human-Algorithm Interaction at Uber." doi:10.25300/misq/2024/17911
   - Jussupow, Benbasat, Heinzl (2024). "An Integrative Perspective on Algorithm Aversion and Appreciation in Decision-Making." doi:10.25300/misq/2024/18512
   - Kronblad, Essén, Mähring (2024). "When Justice is Blind to Algorithms: Multilayered Blackboxing of Algorithmic Decision-Making in the Public Sector." doi:10.25300/misq/2024/18251
   - Seidel, Frick, Brocke (2025). "Regulating Emerging Technologies: Prospective Sensemaking Through Abstraction And Elaboration." doi:10.25300/misq/2024/18039
5. **CFPs.** A search result pointed to `misq.umn.edu/pages/call_for_papers_ai_ia` ("Special Issue on AI-IA Nexus"). Blocked; deadline and content not verified.
6. **Review, speed, acceptance.** Not verified.
7. **AI policy.** Not verified.
8. **Fit: workable in topic, blocked in verification.** IS journals sit closer to design and human-factors framing than management journals do, and Grisold et al. (2025) is a near neighbour. Obstacles: MISQ expects an IS contribution, the Theory and Review proposal step is, if current, extra work, and a no-data paper from a first-time author is a long shot at an A*, FT50, UTD24 journal. Verify the track rules by hand before deciding.

## 9. Information Systems Research (ISR)

1. **Publisher, ISSN.** INFORMS; ISSN 1047-7047 / 1526-5536. APC not verified.
2. **Scope.** Not verified (blocked).
3. **Conceptual papers.** Not verified. The Crossref sample is almost all empirical or analytical.
4. **Fit evidence (ISSN 1047-7047).** Jiang, Wiener, Benlian, Adam (2026), "How Platform Workers Contest Algorithmic Management: Theorizing the Dynamics of Algoactivistic Practices," doi:10.1287/isre.2024.0927; Bauer, Gill (2024), "Mirror, Mirror on the Wall: Algorithmic Assessments, Transparency, and Self-Fulfilling Prophecies," doi:10.1287/isre.2023.1217; Leong, Lin, Tan, Yu (2024), "Coordination in a Digital Platform Organization," doi:10.1287/isre.2023.1226; Dehling, Sunyaev (2024), "A Design Theory for Transparency of Information Privacy Practices," doi:10.1287/isre.2019.0239; Rhue (2024), "The Anchoring Effect, Algorithmic Fairness, and the Limits of Information Transparency for Emotion Artificial Intelligence," doi:10.1287/isre.2019.0493.
5. **CFPs.** Not verified.
6. **Review, speed, acceptance.** Not verified.
7. **AI policy.** Not verified.
8. **Fit: poor to unverified.** The transparency-limits theme is on point (Bauer and Gill; Rhue), but ISR leans empirical and I could not read the article types.

## 10. Journal of the Association for Information Systems (JAIS)

1. **Publisher, ISSN, access.** Association for Information Systems; ISSN 1536-9323. Green open access: "authors of accepted papers can self-archive their accepted papers without an embargo period". APC: not stated on the pages I read.
2. **Scope.** "JAIS particularly welcomes contributions that provide theoretical insights that advance our understanding of information systems and information technology in organizations and society. New insights may include proposing a new theoretical model, challenging or clarifying existing theory, integrating diverse strands of research in information systems so as to advance new concepts and relationships, or developing a compelling argument for the field to develop a new theory." (`https://aisel.aisnet.org/jais/authorinfo.html`, opened)
3. **Conceptual papers.** Yes, with a named category. "2. Theory ... The Theory section of JAIS seeks to publish theory articles that advances our understanding of novel IS and digital technology-related phenomena. Submissions are expected to contribute original theory that proposes new concepts/constructs, advances propositions/theoretical insights and/or integrates existing theories into a novel theoretical framework. ... Contributions should be grounded in a precise understanding of the phenomenon as well as theoretical perspectives from within or outside the IS field. When submitting a manuscript to this section, authors should, in their cover letter, designate the manuscript as such, and nominate this section's Senior Editor." The Theory Senior Editor is named on the page as Gerald C. Kane. Length: manuscripts in the Theory category "that are more than 15,000 words are very likely to receive extra scrutiny"; "Manuscripts that exceed 65 pages including everything will not be sent out for review." Other categories: Literature Reviews, Research Perspectives (about 10,000 words), Policy and Impact (5,000–7,000 words), Foundational Research on Novel Digital Phenomena (empirical). No proposal step for Theory. Reviews are double-blind.
4. **Fit evidence (ISSN 1536-9323).**
   - Möhlmann, Salge et al. (2023). "Algorithm Sensemaking: How Platform Workers Make Sense of Algorithmic Management." doi:10.17705/1jais.00774
   - Constantiou, Joshi et al. (2023). "Organizations as Digital Enactment Systems: A Theory of Replacement of Humans by Digital Technologies in Organizational Scanning, Interpretation, and Learning." doi:10.17705/1jais.00833
   - Jarvenpaa, Klein et al. (2024). "New Frontiers in Information Systems Theorizing: Human-gAI Collaboration." doi:10.17705/1jais.00868
   - Avital, Chatterjee et al. (2023). "Sensing the Future: A Design Framework for Context-Aware Predictive Systems." doi:10.17705/1jais.00821
   - Pumplun et al. (2023). "Bringing Machine Learning Systems into Clinical Practice: A Design Science Approach to Explainable Machine Learning-Based Clinical Decision Support Systems." doi:10.17705/1jais.00820
   (Crossref returned only some author names for JAIS; the lead author's surname is the first one listed.)
5. **CFPs.** A joint JAIS and MISQE call PDF (`aisel.aisnet.org/jais/Call_for_Papers_JAIS-MISQE.pdf`) was returned by search and downloaded (536 KB) but I did not read it; the search summary called it old. Not verified.
6. **Review, speed, acceptance.** Double-blind. The page mentions a "JAIS Promise Review Option" (authors indicate it in the cover letter); I did not read what it promises. Time to decision and acceptance: not verified.
7. **AI policy.** None found on the JAIS policies page or the author-information page. Not verified whether AIS has a separate policy.
8. **Fit: strong.** JAIS is the only journal in this cluster whose opened page names a Theory category that takes a new construct ("algorithmacy"), a framework ("DXD") and cross-field theory "from within or outside the IS field". The IS tradition also accepts design framing. Obstacles: the contribution must be tied to IS and digital-technology phenomena, so the platform and algorithm material has to lead, and the medieval-reading history must be shown to explain a digital phenomenon. A sole-author student paper in a journal with a named Senior Editor is a normal route. No AI policy found means the author should write to the editor before submitting and state the AI use in the cover letter anyway.

## 11. Journal of Information Technology (JIT)

1. **Publisher, ISSN, access.** Sage; ISSN 0268-3962 / 1466-4437. "There are no fees payable to submit or publish in this journal." "Accepts preprints? No" (mirror).
2. **Scope.** "The Journal of Information Technology publishes original research of interest to the Information Systems academic community. Submissions are expected to have clear theoretical foundations and to make a substantial contribution to our knowledge of Information Systems. Papers must demonstrate the breadth of their relevance to multiple contexts. The journal does NOT publish papers that merely describe technologies or propose implementations to solve particular technical problems." (mirror of `.../author-instructions/jin`)
3. **Conceptual papers.** Types: "original research articles", "Scholarly reviews", "State of the art overviews (these are typically invited contributions ...)", "Debates and perspectives". "The Journal does not have a fixed policy on word length ... For the initial submission of original research articles 6,000-9,000 words is usually acceptable." Cover letter statement of at most 80 words. Whether a no-data theory paper counts as an "original research article" is not stated. Not verified.
4. **Fit evidence (ISSN 0268-3962).** Kokshagina, Reinecke, Karanasios (2023), "To regulate or not to regulate: unravelling institutional tussles around the regulation of algorithmic control of digital platforms," doi:10.1177/02683962221114408; Gleiss, Degen, Pousttchi (2023), "Identifying the patterns: Towards a systematic approach to digital platform regulation," doi:10.1177/02683962221146803. Two close hits.
5. **CFPs.** None found.
6. **Review.** Double anonymized. Speed and acceptance not verified.
7. **AI policy.** Sage block.
8. **Fit: workable.** Range of 6,000–9,000 words is shorter than the 9,000–12,000 the paper is likely to reach, and the theory-only route is unclear. The author would cut toward 9,000 words and ask the editors whether a theory paper is an "original research article."

## 12. Information and Organization

1. **Publisher, ISSN, access.** Elsevier; ISSN 1471-7727. Access and APC: not verified.
2. **Scope.** Not opened (blocked). A search snippet from a secondary site quoted: "Information and Organization seeks to publish original scholarly articles on the relationships between information technologies and social organization. It seeks a scholarly understanding that is based on empirical research and relevant theory." Also quoted: "A particular focus ... is to publish qualitative and interpretive research which adopts case studies, ethnography and in-depth longitudinal empirical studies". Secondary; not verified.
3. **Conceptual papers.** Not verified. The snippet said the journal also takes papers that "review empirical research and provide directions for future research and theory development."
4. **Fit evidence (ISSN 1471-7727).** Sullivan, Veen, Riemer (2024), "Furthering engaged algorithmic management research: Surfacing foundational positions through a hermeneutic literature analysis," doi:10.1016/j.infoandorg.2024.100528; Cecez-Kecmanovic (2025), "Ethics in the world of automated algorithmic decision-making – A Posthumanist perspective," doi:10.1016/j.infoandorg.2025.100587; Krakowski (2025), "Human-AI agency in the age of generative AI," doi:10.1016/j.infoandorg.2025.100560; Aaltonen, Stelmaszak (2026), "Data design: A constitutive rules perspective," doi:10.1016/j.infoandorg.2026.100647; Scott, Orlikowski (2025), "Exploring AI-in-the-making: Sociomaterial genealogies of AI performativity," doi:10.1016/j.infoandorg.2025.100558.
5. **CFPs.** Not verified.
6. **Review, speed, acceptance.** Not verified.
7. **AI policy.** Elsevier block.
8. **Fit: workable, interpretive-leaning.** Topic overlap is strong, but the journal favours interpretive and sociomaterial scholarship, and the paper's cognitive-science and mechanism-design base is a different register. Obstacle: the critical-sociomaterial reader may reject the experiment-and-design stance. Would need to engage that literature (Orlikowski, Cecez-Kecmanovic) before submission.

## 13. Information Systems Journal (ISJ)

1. **Publisher, ISSN.** Wiley; ISSN 1350-1917 / 1365-2575. Access and APC not verified.
2. **Scope, conceptual papers, review, CFPs.** Not verified (Wiley blocked; a web search returned no ISJ author page).
3. **Fit evidence (ISSN 1350-1917).** Gerlings, Keramidis, Shollo, Constantiou (2026), "Explainable AI in Context: Investigating How AI Use Cases Shape Stakeholders' Use in High-Stakes Organizations," doi:10.1111/isj.70059; Ochmann, Michels, Tiefenbeck, Maier (2024), "Perceived algorithmic fairness: An empirical study of transparency and anthropomorphism in algorithmic recruiting," doi:10.1111/isj.12482; Muthukannan, Gozman, Tan, Dhavamani (2026), "From Open Banking Regulation to Platform Orchestration: The Evolution of Digital Platform Governance," doi:10.1111/isj.70030; Shi, Constantinides, Iannacci (2026), "Accelerating Platform User Growth: Pinduoduo's Multi-Motivational Selfish Referral Strategy," doi:10.1111/isj.70050. Mostly empirical.
4. **AI policy.** Wiley block.
5. **Fit: unverified.** Cannot judge article types. Topic fit moderate (explainability and platform governance appear), form unknown.

## 14. Journal of Management Information Systems (JMIS)

1. **Publisher, ISSN.** Taylor & Francis; ISSN 0742-1222 / 1557-928X. Access and APC not verified.
2. **Scope.** Official contributor page `https://jmis-web.org/info-for-contributors` (opened): abstract "up to 150 words"; "The length of the complete MS should not surpass 50 pages"; "The intention to shorten the paper at later time is not a persuasive justification." Double-blind. The page states no scope text, no article types and no AI policy. Third-party guides (not opened) describe JMIS as requiring an organisational question and a theory contribution; not verified.
3. **Conceptual papers.** Not stated on the page I opened. Not verified.
4. **Fit evidence (ISSN 0742-1222).** Möhlmann, Gregory, Henfridsson (2025), "Algorithmic Stakeholder Governance on Content Platforms: A Lead Role Perspective," doi:10.1080/07421222.2025.2520177; Claggett, Karahanna (2025), "Understanding the Role of Technology in Coordination Through Affordance Configurations," doi:10.1080/07421222.2025.2487306; Liel, Zalmanson (2025), "Turning Off Your Better Judgment: Algorithmic Conformity in Artificial Intelligence-Human Collaboration," doi:10.1080/07421222.2025.2561390.
5. **CFPs, review, speed.** Not verified.
6. **AI policy.** T&F block.
7. **Fit: poor to unverified.** JMIS leans empirical and analytical (economics and behavioural studies) in the sample.

## 15. Research Policy

1. **Publisher, ISSN.** Elsevier; ISSN 0048-7333. Access and APC not verified.
2. **Scope, article types, conceptual papers.** Not verified (ScienceDirect blocked).
3. **Fit evidence (ISSN 0048-7333).** Koehler, Sauermann (2024), "Algorithmic management in scientific research," doi:10.1016/j.respol.2024.104985; Koo (2024), "Hybrid governance of platform entrepreneurs," doi:10.1016/j.respol.2023.104916; Hassan, Nair (2026), "Searching together: Human–AI complementarities in innovation search," doi:10.1016/j.respol.2026.105597. The sample is empirical, innovation-policy work.
4. **CFPs, review, speed.** Not verified.
5. **AI policy.** Elsevier block.
6. **Fit: poor.** The journal's subject is research, innovation and technology policy and the sample is empirical. The paper's institutional-custody section (section 7 of the outline) is the only part that could be argued as policy.

## 16. California Management Review (CMR)

1. **Publisher, ISSN, access.** Sage, edited at Berkeley Haas; ISSN 0008-1256 / 2162-8564. Subscription. "There is no fee for submitting a manuscript."
2. **Scope.** "CMR primarily publishes original articles that are both research based and address issues of current concern to managers." "every manuscript should also be practitioner oriented, including recommendations that will improve the practice of management." (`https://cmr.berkeley.edu/resources/submit/` and the Sage mirror)
3. **Conceptual papers.** Not as a pure-theory type. Types on the journal's site: In-Depth Article "6,000–8,000 words" ("blending academic research and theory with practitioner relevance"), Spotlight 3,000–4,000, Insight 500–3,000, Submission Inquiry (500 characters). The Sage mirror gives an older "5,000 to 9,000 words"; I follow the journal's own site. Peer review for In-Depth and Spotlight; no proposal needed beyond the optional inquiry.
4. **Fit evidence (ISSN 0008-1256).** Kolbjørnsrud (2023), "Designing the Intelligent Organization: Six Principles for Human-AI Collaboration," doi:10.1177/00081256231211020; Schreieck, Ondrus, Wiesche, Krcmar (2025), "Platform Governance for Established Companies," doi:10.1177/00081256251338251; Ho, Yeung (2026), "Principal Workers: Orchestrating AI Agents Improves Productivity," doi:10.1177/00081256261470827. Practitioner-oriented.
5. **CFPs.** None found.
6. **Review and speed.** "authors can typically expect a preliminary publication decision within 8 to 12 weeks"; "Accepted articles are generally published within 6 to 10 months." The Sage mirror says 12 to 16 weeks; the journal's own page is newer in wording, but I could not date either. Acceptance rate not verified.
7. **AI policy.** The journal's page has none; Sage block applies.
8. **Fit: workable only as a practitioner rewrite.** The "Six Principles for Human-AI Collaboration" precedent shows the genre. The paper would become an 8,000-word piece for managers and regulators with the experiment kept as a proposal, and no theory apparatus. ABDC A; not FT50 or UTD24.

## 17. MIT Sloan Management Review (practitioner)

1. **Publisher, ISSN.** MIT Sloan School of Management / MIT Press; ISSN 1532-9194 / 1532-8937.
2. **Status.** MIT Sloan announced it would "cease production" of the magazine. The press page `https://mitsloan.mit.edu/press/update-mit-sloan-management-review` (opened) says the magazine "will cease print publication following the magazine's fall issue" and that digital content continues through November 2026. A search summary of the submission portal said it takes drafts of 1,000–2,500 words (not proposals) until November 2026; I could not open the portal (404 from my fetch), so that is secondary.
3. **Fit.** Not a venue for a 9,000-word theory paper, and the magazine is closing. Excluded from the shortlist. A new MIT Sloan digital series is promised; no submission route is known.

## 18. Others found

- **Human Relations (Sage).** ABDC A*, removed from FT50 in 2026 (Bodleian). Crossref shows algorithmic-management work: Dasgupta, Carbery, McDonnell, Jooss (2026), doi:10.1177/00187267261445807; Stollberger, Anand, Dick (2025), "Capturing a moving target: Developing research on and with AI for *Human Relations*," doi:10.1177/00187267251332075. Article types, limits, and policy: not verified.
- **Organization (Sage).** ABDC A. Zientara (2026), "Against acceptance as legitimacy: Ethics and algorithmic management," doi:10.1177/13505084261443023; den Hond, Vesa (2025), doi:10.1177/13505084251331396. Critical register; not verified otherwise.
- **Academy of Management Annals.** ABDC A*, FT50. Review-only; Karunakaran, Lebovitz, Narayanan, Rahman (2025), "Artificial Intelligence at Work: An Integrative Perspective on the Impact of AI on Workplace Inequality," doi:10.5465/annals.2023.0230. A literature review, not this paper's form.
- **European Journal of Information Systems.** ABDC A*; Alizadeh, Wiener, Benlian (2025), doi:10.1080/0960085x.2025.2576230. Not verified otherwise.
- **Journal of Strategic Information Systems.** ABDC A*; Heyder, Passlack, Posegga (2023), "Ethical management of human-AI interaction: Theory development review," doi:10.1016/j.jsis.2023.101772. Not verified otherwise.
- **Journal of Business Ethics.** ABDC A, removed from FT50 in 2026. Cordasco, Véliz (2026), "The Accuracy-Explainability Trade-off, the Right to Explanation, and the Implications for Organisations," doi:10.1007/s10551-026-06305-9, and others on algorithmic transparency. Not verified otherwise.
- **Big Data & Society (Sage, ISSN 2053-9517).** Not in the ABDC file. Publishes much critical work on algorithmic accountability and transparency (Crossref, e.g. Raz, Heinrichs, Avnoon, Eyal 2024, "Prediction and explainability in AI: Striking a new balance?", doi:10.1177/20539517241235871). Outside the A-tier lists; not verified otherwise.
- **MIS Quarterly Executive.** ABDC A; practitioner IS journal. Page `aisel.aisnet.org/misqe/...` shows a permissive AI policy. A search result reported a special issue on delegating work to AI agents (deadline 1 March 2027; agentic-AI issue with a final accepted-paper deadline of 1 October 2027). Not opened; not verified.

---

## Ranked shortlist: three best fits in this cluster

**1. Organization Theory.** It is the only journal here whose opened pages say it takes theory with no data (theory article, "theoretical critique and synthesis"), has no proposal step, and shows a 2024 run of AI-and-organizing theory papers (Stark and Vanden Broeck on algorithmic management; Hinds and von Krogh on generative AI and organizing). Sage's AI policy asks for disclosure and does not forbid AI-assisted drafting. Costs: ABDC A, not A*, outside FT50 and UTD24; the APC is $1,000 with possible waiver or EGOS support; the paper must lead with the organizing problem and cut to 11,000 words including references.

**2. Journal of the Association for Information Systems.** It has a named Theory category that welcomes new constructs and frameworks and theory "from within or outside the IS field", and the IS tradition is the least hostile to a design framing. ABDC A*. I found no AI policy to violate. The cost is that the paper has to be recast around a digital-technology phenomenon, and a Senior Editor must be nominated in the cover letter. Not in FT50 or UTD24.

**3. Academy of Management Review.** It is the only journal here that is explicitly for conceptual work and has the full prestige set (ABDC A*, FT50, UTD24), and it is printing human–AI coordination theory now (Lu and Yan 2026; Raisch and Fomina 2025). It ranks third because it is the hardest route: it requires a management-theory contribution, allows one submission only, and enforces the strictest AI rule I found ("created by the authors"), which the current Gemini-drafted abstract and introduction would not meet without rewriting.

Runner-up not ranked because I could not verify the rules: MIS Quarterly (Theory and Review track; Grisold, Berente and Seidel 2025 is the nearest paper to DXD in any journal I searched), and Journal of Management Studies.

Would a human-factors and design framing be desk-rejected? No page I opened says so in terms. The signals point one way. AMP excludes "theory driven papers"; Organization Studies now takes empirical papers only; AMR and OT require a contribution about organizations, organizing or management. That is my reading of their scope statements, not a stated rule. JAIS names theory from outside IS as acceptable. In every case the paper needs a statement of what it contributes to the field's own theory.

## What I could not verify

- **ABS/CABS grades for all journals** (login wall). **Scimago SJR quartiles for all** (Cloudflare). **Impact factors for all.** **FT50 from the FT itself** (blocked; the list is from the Bodleian guide, which says it links the 2016 list and records the 2026 removals).
- **Bentley's own journal list.** None found; one search snippet only.
- **Official scope, article types, length, review model and AI policy** for: Organization Science, Information Systems Research (INFORMS), MIS Quarterly (misq.umn.edu), Journal of Management Studies and Information Systems Journal (Wiley), Information and Organization and Research Policy (Elsevier scope pages), Journal of Management Information Systems (T&F; only the contributor page was readable). Their publishers' generic AI policies are quoted above where they were readable.
- **AI policy for JAIS and MISQ.** None found; absence is not proof there is none.
- **Time to first decision and acceptance rates**, for every journal except CMR's stated 8 to 12 weeks.
- **Open special issues with a deadline after today (2026-10-13)** at any journal here. The MISQ AI-IA nexus call, the JMS AI special issue (probably old), and the JAIS/MISQE joint call were found by search but not read or dated.
- **Sage page text** came from the `sage.cnpereading.com` mirror with template residue, not from `journals.sagepub.com`. Statements on OT, Organization Studies, JMI and JIT should be re-read on the live Sage pages before submission. The mirror's CMR length (5,000–9,000 words) disagrees with the journal's own site (6,000–8,000 for an In-Depth article).
- **Whether any journal restricts sole-author or doctoral-student submissions.** No page I opened says so; I did not find the question addressed.
- **Author-level quotes marked "fetch"**: the AMR and AMP page text I read directly; the Bodleian FT50 listing and the Sage OT page summary passed through the fetch tool's extraction, so the exact wording of the Bodleian "removed" section and of any text I attribute to those fetches is the tool's rendering, not my own reading of the raw page.
