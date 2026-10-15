# Facet M2: the present-day half (algorithm studies, transparency, workers, contestability, law in force, counter-delegation)

Facet M2, 2026-10-13. Agent-drafted. The author has not reviewed it, and none of the text is the author's.

**What this file does.** It tests the paper's present-day claims (§4, §5, §6) against scholarship and against the law as written. Quotations and page numbers come only from text I opened this session; every other entry says so. Downloads are in `~/iit-playground/berthon_ethics_local/pdfs/M2/`. The entries use the bib keys in `M2_algorithm_studies.bib`.

**Method and blocks.** Crossref (anonymous, no e-mail) resolved every DOI in the bib. OpenAlex refused requests (shared daily budget spent). Consensus supplied abstracts. SAGE, ACM, OUP, Springer, ScienceDirect, SSRN, escholarship, Taylor and Francis, the Berkeley and Colorado law repositories and EUR-Lex all returned 403 or a bot challenge; I did not try to get round any of them. Because EUR-Lex was blocked, I first read the EU texts below in secondary copies; AUDIT_05 later checked each EU quotation against the Official Journal text served by the Publications Office (publications.europa.eu/resource/celex/<CELEX>, header Accept: application/xhtml+xml) and found them verbatim.

**Counts by read depth** (54 bib entries, including 5 legal acts and 1 grey source; the groups below are approximate and a few works sit in two):

- Read in full: 0.
- Read in part, with locators: 14 (Edwards and Veale 2017; Selbst and Barocas; Dubal; Oeldorf-Hirsch and Neubaum, preprint; Raghavan et al.; Green; Li et al.; Kolt; Gabriel et al.; Lyons et al.; Directive 2024/2831; and, in secondary or UK-amended copies, the DSA Arts 20-21, P2B Arts 4, 5, 11, 12, GDPR Art 22, AI Act Arts 26(7) and 86).
- Abstract only: 15 (Ananny and Crawford; Edwards and Veale 2018; Long and Magerko; Cotter and Reisdorf; Petrovcic; Cameron and Rahman; Cameron 2024; Christin 2017; Vincent et al.; Karimi et al.; Bayamlioglu; Almada; Karusala et al.; Zhu et al.; Kellogg et al., truncated).
- Bibliographic record only: 19 (Burrell 2016, Wachter et al., Pasquale, Ng et al., Bucher, DeVito et al., Eslami et al., Bishop, Vallas and Schor, Wood et al., Calacci and Pentland, Delacroix and Lawrence, Fourcade and Healy twice, Burrell and Fourcade, Kiviat, Vaccaro et al., Hirsch et al., Alfrink et al., Gagrcin et al., Rahman).
- Not accessible and not verified in Crossref: Kaminski and Urban (no DOI record found; two repository copies returned 403).
- Could not verify at all, so not in the bib: Benjamin, *Race After Technology*; Noble, *Algorithms of Oppression*; Eubanks, *Automating Inequality*; the Amsterdam Court of Appeal judgments of April 2023 (known only from web summaries).

---

## 1. Transparency and explanation as a remedy

**Edwards and Veale (2017)** (`edwards2017slave`; read in part, Duke pagination). This is the strongest pre-emption of the paper's opening move, and the paper does not cite it.

- p. 67: "Relying on individual rights to explanation as the means for users to take control of ML systems risks creating a similar 'transparency fallacy.' Individual data subjects are not empowered to make use of the kind of algorithmic explanations they are likely to be offered even if (unlikely as it seems) the problems identified in section III are overcome. Individuals are mostly too time-poor, resource-poor, and lacking in the necessary expertise to meaningfully make use of these individual rights."
- p. 67, summarising Ananny and Crawford: transparency "placing a tremendous burden on individuals both to seek out information about a system, interpret it, and determine its significance, only then to find out they have little power to change things anyway, being 'disconnected from power'". The authors add that dependence on transparency "may occlude the true problems which rest in societal power relations and institutions as much as the software tools employed."
- p. 81: the right to erasure and to portability "rely too much on individual rights for what are too often group harms."
- p. 82: they prefer "creating better systems, with less opacity, clearer audit trails, well and holistically trained designers, and input from concerned publics" to "grimly pursuing against the odds a 'meaningful' version of the interior of a black box."

*Bearing.* It says informing the individual is the wrong remedy and moves the duty to system builders (privacy by design, DPIAs, certification). The paper's thesis is therefore not new in legal scholarship. What the paper adds is the historical mechanism (test, access, record) and the adaptivity claim. It must cite Edwards and Veale at the Introduction and §6.1 and say what it adds.

**Selbst and Barocas (2018)** (`selbst2018intuitive`; read in part). They separate "inscrutable" from "nonintuitive" models and argue explanation of the model does not tell you whether its basis is "normatively defensible" (abstract, p. 1086). p. 1094: "The process of moving from observation to knowledge to accountability cannot be assumed; in many cases, the ability to leverage observations for accountability requires preexisting knowledge that allows observers to appreciate the significance of a disclosure." They conclude that one must "seek explanations of the process behind a model's development, not just explanations of the model itself" (p. 1086). pp. 1106-1107 quote GDPR Art. 22. *Bearing:* it supports §5.1 (understanding does not become leverage) and §6.3 (declare the envelope, the process, rather than explain the case). It does not say the subject is the wrong party.

**Ananny and Crawford (2018)** (`ananny2018seeing`; abstract only; the two passages above reach me through Edwards and Veale p. 67 and Selbst and Barocas p. 1094). Abstract: "Being able to see a system is sometimes equated with being able to know how it works and govern it ... can 'black boxes' ever be opened, and if so, would that ever be sufficient?" They present "10 limitations". I did not read them. Referees will expect the citation; read the article before it is used.

**Wachter, Mittelstadt and Floridi (2017)** (`wachter2017why`) and **Burrell (2016)** (`burrell2016machine`): not accessible. I know Wachter et al. only through a web-search summary (no GDPR "right to explanation", at most a "right to be informed"), which I cannot quote. Selbst and Powles (*Int. Data Privacy Law* 7(4), 2017, "Meaningful information and the right to explanation") is a reply; I opened the file but read only its title page, so it is not in the bib. **Pasquale (2015)**: not read.

**Does anyone argue the subject is the wrong party?** Not in those words in anything I read. Edwards and Veale come closest (individuals cannot use explanations; burden belongs on system design and agencies "such as NGOs, regulators, or civil society scrutiny organisations" (p. 23)). Dubal (below) goes further: "transparency requests are by themselves ineffectual" absent a ban or collective bargaining, and "Knowledge alone will not end or mitigate the precarities of digitalized pay" (p. 1984); her remedy is a ban on algorithmic wage discrimination. Neither uses the literacy-transition frame.

---

## 2. "AI literacy" and "algorithmic literacy": definitions, critics, evidence

- **Long and Magerko (2020)** (`long2020what`; abstract only). Abstract offers "a concrete definition of AI literacy" and "a set of core competencies", and design considerations "to support AI developers and educators in creating learner-centered AI". The definition sentence itself I did not see. This is the field's reference definition; a referee will expect it.
- **Ng et al. (2021)** (`ng2021conceptualizing`): not read; cite as a review of definitions only.
- **Oeldorf-Hirsch and Neubaum (2023)** (`oeldorf2023what`; preprint, read in part, preprint pagination). Their first research direction is "balancing users' expectations of algorithmic literacy with developers' responsibility for algorithmic transparency" (abstract), and p. 23: "Having proposed that algorithmic literacy should not be solely the responsibility of the social media user, the current reality is that individuals must endure most of effort in improving literacy." They also say effects of literacy on behaviour are "necessary future work" (section on decoding algorithms). They report Eslami et al. 2015 (62.5 per cent unaware of feed filtering) and Rader and Gray 2015 (users knew posts were filtered but "did not understand how such filtering worked, or why it was done, which meant they had little power to influence or leverage it"). They name "the new algorithmic divide". *Bearing:* the proponents themselves concede shared responsibility, so the paper's target ("AI literacy as the primary safeguard") must be aimed at the policy and guideline layer (Jobin et al.), not at this scholarship. This is the best answer to a referee who says the paper attacks a straw man.
- **Dogruel, Masur and Joeckel (2021)** (key already in `references.bib`; abstract only): awareness and knowledge as dimensions.
- **Cotter and Reisdorf (2020)** (`cotter2020algorithmic`; abstract only): algorithmic knowledge "varies according to socioeconomic advantage" in a US survey on search, so the competence is itself unequally distributed. **Petrovcic et al. (2024)** (abstract only): in a Slovenian survey (N = 802) "algorithm knowledge was a significant determinant of internet uses". Together these give a measured link between knowledge and use, not between knowledge and bargaining power.
- **Empirical evidence on whether knowing gives leverage (§5.1).** I found three kinds of evidence, and they do not agree.
  1. *Against the paper's "zero leverage".* Cameron and Rahman (2022) (`cameron2022expanding`, abstract only) report that workers' "everyday interactions with customers can influence and manipulate algorithms in ways that platforms cannot always observe"; the 2021 conference version (Crossref title "(Not) Seeing Like an Algorithm: Managerial Control and Worker Resistance in the Platform Economy"; its abstract could not be opened in AUDIT_05, so this wording is UNVERIFIED) is said to say "compared to customers, workers had greater knowledge of how the platforms' algorithms worked, and used this expertise to manipulate customers". Cameron (2024) (`cameron2024making`, abstract only) finds workers use "engagement" and "deviance" tactics and both "elicit consent", and that "choice-based consent can mask the more-structurally problematic elements of the work". Christin (2017) (`christin2017algorithms`, abstract only) documents "buffering strategies" (foot-dragging, gaming, open critique). Rahman (2021) (the paper's own source) shows opacity itself produces conformity. So knowledge does give covert, individual leverage over ratings; what it does not give is leverage over terms.
  2. *For the paper.* Dubal (2023, p. 1984): "Knowledge alone will not end or mitigate the precarities of digitalized pay." Selbst and Barocas p. 1094 (above).
  3. *Interventions.* Oeldorf-Hirsch and Neubaum report that short explanations raised understanding (Rader et al. 2018, via the preprint, p. 22). Nothing I opened tests whether understanding changed an outcome for a person bound by a platform's decision.
  **Result:** the §5.1 sentence "achieving high algorithmic comprehension gives a platform worker zero leverage" is too strong as written. The supportable claim is that comprehension gives leverage over one's own ratings and tactics, and none over the pay rule, the termination, or the record. The author should decide the wording; the sources are Cameron and Rahman, Cameron, and Dubal.

---

## 3. Workers and users coping with algorithmic intermediaries

- **Kellogg, Valentine and Christin (2020)** (`kellogg2020algorithms`): Consensus returned a truncated abstract ("We use Edwards' (1979) perspective of 'contested terrain' ..."). I could not open the text and so cannot confirm "algoactivism" from a source I read. It is the field's survey of how algorithms change who controls the test and the record; a referee will expect it.
- **Dubal (2023)** (`dubal2023algorithmic`; read in part, Columbia pagination). The most useful single source for §4, §5.1 and §6.4. Facts and quotations:
  - p. 1979: transparency and legibility are "One of the most frequently proposed policy reforms for platform labor" (opening of Part III.A). Pp. 1980-1981: James Farrar and Yaseen Aslam of the App Drivers and Couriers Union won at the UK Supreme Court (Feb. 2021) on worker status.
  - p. 1981-1982: Worker Info Exchange and ADCU sued firms for data. Farrar: "what we really want are inference data. What decisions has [the app] made about me? How has it profiled me? How does that affect my earnings? This is what Uber has not given us."
  - p. 1982: efforts "to gain transparency over—and even to 'reverse engineer'—the labor management structures ... have yet to change firm practices."
  - p. 1983: Uber and Ola "have argued that 'the safety and security of their platform may be compromised if the logic of such data processing is disclosed to their workers.'"
  - p. 1984: an Amsterdam appellate court (April 2023) found Uber "must explain how driver personal data and profiling is used in Uber's upfront, dynamic pay and pricing system." Then: "firm transparency, or a worker right to algorithmic explainability—while crucial to understanding the logic of existing practices—does not by itself shift the power dynamics". And "Knowledge alone will not end or mitigate the precarities of digitalized pay."
  - p. 1985-1986: worker data cooperatives (Driver's Seat, WeClock) "countercollect data collected by on-demand firms using separate apps" and "have been useful for workers who have been able to contest unfair suspensions or terminations based on errors in facial recognition or in geolocation checks", but "a common complaint of workers in my research is the lack of a formal appeals mechanisms" (p. 1985), and "This, then, is primarily a structural problem, not necessarily one that is rooted in control over and legibility of data." (p. 1986). Cooperatives "do not address the most significant harms" because they leave the economic relationship untouched (p. 1986).
  - Remedy: "a narrowly structured, nonwaivable peremptory ban" on the practice.
  *Bearing.* §4 (record): supports. §5.1: supports with workers' own words. §6.2: Dubal's ban is a sharper form of structural refusal and should be cited. §6.3: Uber and Ola's security objection is the first thing a referee will raise against declared envelopes. **§6.4: workers already build counter-records (Driver's Seat, WeClock) and Dubal says they help with contesting errors and do not change the relationship.** The paper must answer that.
- **Bucher (2017)**, **DeVito et al. (2017)**, **Eslami et al. (2015)**, **Bishop (2019)**, **Wood et al. (2019)**, **Vallas and Schor (2020)**: bibliographic records only. Standard for folk theories and algorithmic gossip; the paper can cite them for the claim that users build their own models, only after they are read.
- **Karusala et al. (2024)** (abstract only): in public-service contestation in India and the US, "intermediaries like NGO workers or lawyers" help people exercise rights. This is a human counter-delegation that already exists and is a model for §6.4.

---

## 4. The gate, at scale

I opened none of these in text. Records resolve in Crossref: Fourcade and Healy (2013), *The Ordinal Society* (2024), Burrell and Fourcade (2021), Kiviat (2019), all not read. Eubanks, Benjamin and Noble are books I could not verify from a record or a text (Crossref returned only reviews for Eubanks and Benjamin). **I could not check whether Benjamin draws the Jim Crow or literacy-test parallel explicitly.** Search snippets show only that "New Jim Code" is her title term. Do not attribute it until someone reads the introduction (Polity 2019).

One source I did read bears on the gate:

- **Raghavan, Barocas, Kleinberg and Levy (2020)** (`raghavan2020mitigating`; read in part, arXiv v3). Abstract: "little is known about how these methods are used in practice"; they document vendors' disclosures on development, validation and bias. Section 2 (arXiv pp. 3-4) says "Cognitive assessments have imposed adverse impacts on minority populations since their introduction into mainstream use" and explains that US employers are held to the EEOC's Uniform Guidelines on Employment Selection Procedures, under which "the gold standard for pre-employment assessments" is validation, with disparate treatment and disparate impact as the two routes to challenge an assessment. *Bearing:* (a) it is the right source for a hiring-vendor claim beyond Bommasani et al.; (b) it shows the US already has a validation-and-adverse-impact regime for employment tests, a counterpart to the historical safeguards that §5.3 says is missing for hiring. Whether that regime reaches algorithmic vendors in practice is the paper's question; Raghavan et al. find vendors' claims about bias are thin.

---

## 5. Contestability, appeal, recourse, and the law as written

### 5.1 The scholarship

- **Lyons, Velloso and Miller (2021)** (`lyons2021conceptualising`; abstract and introduction read). "The ability to contest algorithmic decisions is being recognised as an important safeguard for individuals. Yet, there is little guidance on what 'contestability' ... requires." Findings from submissions on Australia's AI Ethics Framework: contestability "resembles contestability in relation to human decision-making".
- **Kaminski and Urban (2021)** (`kaminski2021right`): not read. From a web summary only: they propose an individual right to contest AI decisions modelled on due process. This is the paper that argues the safeguard of the old procedure should be rebuilt for AI, which is §6's claim; a referee will expect it. Get a library copy.
- **Alfrink et al. (2023)**, **Hirsch et al. (2017)**, **Vaccaro et al. (2020)**: records only. **Almada (2019)** and **Bayamlioglu (2022)** (abstracts only): Art 22(3)'s right to contest is "the core remedy" (Bayamlioglu) and "contestability by design" is needed because human intervention can "introduce biases and limitations" (Almada).
- **Karimi et al. (2022)** (abstract only): recourse tells a rejected person what to change in their own inputs. That is the remedy aimed at the subject; it is the technical counterpart of "AI literacy" and a useful foil for §6.
- **Green (2022)** (`green2022flaws`; read in part; scope is government algorithms). Abstract: "these policies rest on an uninterrogated assumption: that people are able to effectively oversee algorithmic decision-making", and human oversight policies "provide a false sense of security". He surveys 41 policies. *Bearing:* it cuts against treating a human reviewer as the restored notary. If §5.3 or §6 asks for human review, Green is the reply to expect.

### 5.2 What the law in force actually says

Read in these copies: Directive (EU) 2024/2831 from a PDF carrying the Official Journal header (`eu2024platformwork`), the others from reproductions (see bib notes). Quotations are verbatim from the copy.

**Platform Work Directive (EU) 2024/2831** (OJ L, 11.11.2024). Transposition by 2 December 2026, so it is adopted but not yet national law as of today.

- Art 9(1)(b): platforms must inform persons performing platform work of automated decision-making systems, including "(iii) the categories of data and the main parameters that such systems take into account and the relative importance of those main parameters in the automated decision-making, including the way in which the personal data or behaviour of the person performing platform work influence the decisions" and "(iv) the grounds for decisions to restrict, suspend or terminate the account". Art 9(5) extends this to "persons undergoing a recruitment or selection procedure". Art 9(6): a right to portability of "personal data generated through their performance of work ... including ratings and reviews", with "tools" supplied "free of charge" and transmission "directly to a third party" on request.
- Art 10(5): "Any decision to restrict, suspend or terminate the contractual relationship or the account of a person performing platform work or any other decision of equivalent detriment shall be taken by a human being." Art 10(2): oversight staff "shall have the competence, training and authority necessary ... including for overriding automated decisions" and protection from dismissal for doing so. Art 10(1): evaluation of impact "with the involvement of workers' representatives, regularly and in any event every two years".
- Art 11(1): a right "to obtain an oral or written explanation ... for any decision taken or supported by an automated decision-making system", "access to a contact person" with "competence, training and authority", and a written statement of reasons for account restriction, suspension, termination or refusal of payment "at the latest on the date on which it takes effect". Art 11(2): a right to request review; the platform replies "within two weeks of receipt". Art 11(3): if the decision infringes the worker's rights it must be rectified "within two weeks", otherwise "adequate compensation". Art 11(5): the article "shall not apply to persons performing platform work who are also business users" under the P2B Regulation.
- Art 8(1): a data-protection impact assessment is mandatory and must "seek the views of persons performing platform work and their representatives". Arts 13-14: information and consultation of workers' representatives, who may be assisted by an expert.
- Art 7(1): bans on processing emotional or psychological state data, private conversations, off-duty data, and inferences of "racial or ethnic origin, migration status, political opinions ..." by automated systems. This is a legal counterpart to "structural refusal" for specified inferences.

**Digital Services Act (EU) 2022/2065** (springlex copy). Art 20: "access to an effective internal complaint-handling system" for at least six months; complaints "in a timely, non-discriminatory, diligent and non-arbitrary manner"; reversal where the complaint has sufficient grounds; and "decisions ... are taken under the supervision of appropriately qualified staff, and not solely on the basis of automated means" (Art 20(6)). Scope: decisions on content removal or visibility, suspension or termination of service, account, or monetisation, taken because information is illegal or against terms. Art 21: users may choose any certified out-of-court body; platforms must engage "in good faith"; but "The certified out-of-court dispute settlement body shall not have the power to impose a binding settlement of the dispute on the parties." It does not cover pay, matching or hiring.

**P2B Regulation (EU) 2019/1150** (UK-retained version on legislation.gov.uk; EU Exit amendments flagged there). Art 4: statement of reasons "on a durable medium" before restriction or suspension and "at least 30 days" before termination, with the opportunity "to clarify the facts and circumstances" through the Art 11 process. Art 5(1): "main parameters determining ranking and the reasons for the relative importance" stated in terms and conditions; Art 5(6): providers shall "not be required to disclose algorithms or any information that, with reasonable certainty, would result in the enabling of deception of consumers or consumer harm through the manipulation of search results". Art 11: internal complaint handling, "free of charge", with outcomes communicated "in an individualised manner". Art 12: two or more mediators named in the terms, who must be "impartial and independent"; mediation is voluntary and the platform bears "a reasonable proportion of the total costs". It protects business users (traders, self-employed sellers), not employees or consumers.

**GDPR Art 22** (springlex copy): "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her." Exceptions for contract necessity, authorising law, explicit consent; in the contract and consent cases the controller must implement "at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision" (Art 22(3)). Dubal (p. 1982-1984) reports workers using Arts 15 and 22 and the Amsterdam court finding for them in 2023, while saying practice has not changed.

**AI Act (EU) 2024/1689** (springlex copy; Annex III and dates of application not opened). Art 86(1): a person subject to a decision taken by the deployer on the output of a high-risk system listed in Annex III (except point 2, critical infrastructure), where the decision produces legal effects or similarly significantly affects the person adversely "in a way that they consider to have an adverse impact on their health, safety or fundamental rights" (Art 86(3): only to the extent the right is not otherwise provided for under Union law), "shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken". Art 26(7): "deployers who are employers shall inform workers' representatives and the affected workers that they will be subject to the use of the high-risk AI system."

### 5.3 Does "no settled counterpart to the historical safeguards" survive?

**It does not survive as an unqualified statement.** In the EU, for platform work, there are now statutory counterparts to three of the historical safeguards the paper names:

| Historical safeguard (paper §5.3) | Present counterpart in text | Where it falls short |
| --- | --- | --- |
| Reading the instrument aloud before witnesses | PWD Art 9 (main parameters, grounds), Art 11(1) (explanation, written reasons, contact person); P2B Arts 4-5 | Information goes to the subject, the party Edwards and Veale and Dubal say cannot use it; P2B Art 5(6) exempts algorithms |
| Sworn, independent notary | PWD Art 10(5) (a human decides termination), Art 11(2)-(3) (review in two weeks, rectification, compensation); DSA Art 20(6) | The reviewer is the platform itself ("the digital labour platform shall respond"); Green (2022) and Dubal show human review and rights have not changed practice |
| Second interpreter or an independent check | DSA Art 21 and P2B Art 12 (external bodies) | DSA Art 21 bodies cannot bind; P2B mediation is voluntary; neither covers pay or matching |
| *Non est factum* (relief for the misled signer) | PWD Art 11(3) (rectify or compensate); GDPR Art 22(3) (contest) | Scope: platform workers only (PWD), content decisions only (DSA), solely automated decisions only (GDPR) |

What the paper can still say, and these are my readings, not the author's: (1) the counterparts are recent, regional and partly not yet in force (PWD transposition 2 December 2026); (2) in each, the reviewer is the intermediary or a body without binding power, whereas the notary and second interpreter were independent of the party they checked; (3) nothing I opened covers hiring screening, credit or search outside platform work, except GDPR Art 22 and the AI Act's duties; (4) there is evidence the existing rights have not changed firm practice (Dubal); (5) there is evidence human review is weak (Green, government algorithms). The paper must concede the Directive in §4 or §5.3 and recast the claim as "no independent, binding check at the point of decision".

US law was not searched beyond what Raghavan et al. and Selbst and Barocas name (Uniform Guidelines, FCRA, ECOA); I did not open any of those texts.

---

## 6. Personal agents and counter-delegation (§6.4)

Does anyone already propose it? Yes, in parts. None joins it to the notary or interpreter.

- **Li et al. (2022)** (`li2022bottom`; read in part). The closest proposal. Abstract: "a bottom-up approach that empowers individual workers to access AI-enabled work planning support and share data among a group of workers through a network of end-user-programmable intelligent assistants is a practical way to bridge AI inequality in gig work under the current paradigm of privately owned platforms." They name a "data divide" and say platforms hold "a monopoly on data and algorithms". It is a position paper, with no evaluation.
- **Dubal (2023)**: Driver's Seat and WeClock "countercollect" data (p. 1985); useful for contesting errors; "primarily a structural problem" (p. 1986). **Calacci and Pentland (2022)** (`calacci2022bargaining`; record only, known through Dubal p. 1980 n. 215): worker-centric audit tools.
- **Vincent et al. (2021)** (abstract only): "data leverage" through "reducing, stopping, redirecting, or otherwise manipulating data contributions". A collective counter-tool, not an agent.
- **Delacroix and Lawrence (2019)** (record only): bottom-up data trusts; not read, so I cannot say whether they treat an agent that acts in a person's name against a platform.
- **Kolt (2025)** (`kolt2025governing`; read in part). Applies agency law to AI agents. The roadmap names loyalty as the third issue: "ensuring that those agents act in the best interests of their users and seek user consent where appropriate." This is the problem for §6.4: a counter-delegate supplied by the platform or a vendor may not be loyal. **Gabriel et al. (2024)** (`gabriel2024ethics`; read in part): discusses two assistants negotiating "on behalf of their users" (arXiv p. 141) and, elsewhere, "credible commitment" as a way to pressure the other side (arXiv pp. 147, 214); it treats the second party as a person or another assistant, not as a platform that holds the record. **Zhu et al. (2025)** (abstract only): in experiments, "AI-mediated deal-making is an inherently imbalanced game -- different agents achieve significantly different outcomes for their users", with LLM "behavioral anomalies" that can cause "overspending or accepting unreasonable deals" (arXiv abstract, v1 to v3). **Consumer Reports Innovation Lab (2024)** (grey, opening only): a pro-consumer agent project with "legal foundations" in existing e-transaction law.
- **Karusala et al. (2024)** (abstract only): human intermediaries (NGO staff, lawyers) accompany people through contestation.
- I found no source that calls a personal agent a modern notary or second interpreter, and none that applies the literacy-transition history to it. That is the paper's contribution, and it is an absence in what I searched (Crossref, Consensus, web search; one pass), not a proven gap.

---

## 7. What an algorithmic-management or FAccT reader would say the outline gets wrong or omits

These are Claude's readings of the sources above, for the author to rule on.

1. It treats "informing the subject" as the field's remedy, but the field has moved to contestability and recourse (Lyons; Kaminski and Urban; Almada) and to regulated process (Edwards and Veale). The paper needs to say it joins that move and adds the history.
2. It states a procedural void while the PWD, DSA and P2B exist (section 5.3).
3. Its target is partly a straw man: the algorithmic-literacy proponents already say responsibility is shared (Oeldorf-Hirsch and Neubaum, pp. 21-23).
4. §5.1 "zero leverage" contradicts the ethnographies in which workers gain covert leverage (Cameron and Rahman; Cameron 2024), and Cameron's finding that choice and knowledge can manufacture consent bears on §6.2: "refusal" and "alternative pathways" can themselves become the "constant and confined choices" Cameron describes.
5. "Declared operating envelopes" (§6.3) meet the trade-secret and gaming objection that Uber and Ola actually raised (Dubal p. 1983) and that P2B Art 5(6) writes into law. The paper must say what an envelope discloses without disclosing the model; the PWD's "main parameters and their relative importance" is the existing wording.
6. Counter-delegation (§6.4) is an individual tool for what Edwards and Veale call "group harms", and Dubal says counter-data does not change the relationship. Li et al. pool data across workers; the paper should say whether its agents are individual or networked.
7. The platform is not a neutral third party like a notary; in gig work it is the counterparty (Calo and Rosenblat is in the source drafts). The historical safeguards existed because the notary was independent. This is probably the paper's best point and it needs the sentence "the intermediary has an interest" (facet G found a documented divergent interest only at Waitangi).
8. Abolition and prohibition (Dubal's "data abolition", PWD Art 7(1)) are alternatives to design obligations and need to be addressed in §6.5.

---

## Synthesis

### (i) Must-include, ranked

1. **Directive (EU) 2024/2831, Arts 9-11** (§5.3, §4, §6). The paper's "no settled counterpart" claim is false for EU platform work unless qualified. Cite the article numbers above and recast the claim.
2. **Edwards and Veale (2017), pp. 67, 81-82** (Introduction, §6.1). Already argues informing the individual is the wrong remedy; the paper must position against it.
3. **Dubal (2023), pp. 1979-1986** (§4 record, §5.1, §6.2-6.4). Workers' own use of data rights, what it did and did not change; ban as remedy; Uber and Ola's security objection.
4. **Green (2022)** (§5.3, §6): human review as a safeguard has an evidence problem. Scope is government.
5. **Cameron and Rahman (2022) and Cameron (2024)** (§5.1): knowledge gives workers covert leverage; the paper must narrow "zero leverage". Read the full texts first.
6. **Oeldorf-Hirsch and Neubaum (2023)** (Introduction, §2.1): the literacy field's own statement of shared responsibility.
7. **Selbst and Barocas (2018), pp. 1086, 1094** (§5.1, §6.3).
8. **Li et al. (2022)** (§6.4): the nearest existing counter-delegation proposal.
9. **Kolt (2025)** (§6.4): loyalty of the agent.
10. **Kaminski and Urban (2021)**, **Kellogg et al. (2020)**, **Long and Magerko (2020)**, **Ananny and Crawford (2018)**: a referee will expect all four; none was readable this session.

### (ii) Optional

Raghavan et al. (2020) (hiring vendors and the Uniform Guidelines); Lyons et al. (2021); Karimi et al. (2022); Cotter and Reisdorf (2020) and Petrovcic et al. (2024) (knowledge gaps); Christin (2017); Karusala et al. (2024); Vincent et al. (2021); Gabriel et al. (2024); DSA Arts 20-21 and P2B Arts 4, 5, 11, 12 (for completeness of §5.3); GDPR Art 22; AI Act Arts 26(7), 86.

### (iii) Works that cut against the paper, and what they force it to concede

- **PWD Arts 7-11, DSA Arts 20-21, P2B Arts 4-12, GDPR Art 22(3), AI Act Art 86:** concede that procedural safeguards now exist in EU law for platform workers, business users, content decisions and solely automated decisions. Narrow the claim to independence and bindingness; say they are recent and not yet tested (PWD not transposed until 2 December 2026).
- **Edwards and Veale (2017):** concede the transparency-fallacy argument is already made in law.
- **Cameron and Rahman; Cameron 2024:** concede knowledge produces some leverage (over ratings) and that autonomy-rich designs can manufacture consent.
- **Oeldorf-Hirsch and Neubaum:** concede the literacy scholars already call for shared responsibility.
- **Green (2022):** concede human review is not the restored notary without independence and evidence it works.
- **Dubal (2023):** concede counter-data and transparency requests have helped contest errors, but have not changed firm practice; and that the stronger remedy may be prohibition, not a design obligation.

### (iv) Missing aspects (proposed paragraph topics, not prose)

1. The law in force for algorithmic management (PWD, GDPR Art 22, AI Act, DSA, P2B) and how far each reaches the five positions; US counterparts not yet searched.
2. Human review and its failure (Green; Almada): why a platform-employed reviewer is not a notary.
3. Workers' counter-records in practice (Worker Info Exchange, ADCU litigation, Driver's Seat, WeClock, Calacci and Pentland) and what Dubal says they do not do.
4. Workers' covert knowledge and consent manufacture (Cameron and Rahman; Cameron; Rahman; Christin).
5. The loyalty and supply problem for personal agents (Kolt; Li et al.; Zhu et al.).
6. Prohibition as an alternative remedy (Dubal; PWD Art 7).
7. Trade secret, gaming and disclosure (Dubal p. 1983; P2B Art 5(6); PWD Art 9 as a workable disclosure wording).

### (v) What I could not open

EUR-Lex (all acts; bot challenge). Ananny and Crawford; Wachter et al.; Burrell; Long and Magerko; Ng et al.; Kellogg et al.; Cameron and Rahman; Cameron 2024; Rahman; Kaminski and Urban; Vaccaro et al.; Hirsch et al.; Alfrink et al.; Calacci and Pentland; Delacroix and Lawrence; Bucher; DeVito et al.; Eslami et al.; Bishop; Vallas and Schor; Wood et al.; Fourcade and Healy (both); Burrell and Fourcade; Kiviat (publisher walls, 403). Not located at all: Benjamin, Noble, Eubanks, Worker Info Exchange documents, the Amsterdam judgments (ECLI), Annex III of the AI Act, AI Act dates of application, "algoactivism" in a source I read, any scholarship using "custobots" (one web search returned none). OpenAlex and Unpaywall were not used (OpenAlex refused; Unpaywall barred by the brief).
