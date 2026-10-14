# Facet N2: law and legal scholarship on safeguards at the point of algorithmic decision (2026-10-14)

Facet N2, Round 6, 2026-10-14. Agent-drafted. The author has not reviewed it, and none of the text is the author's. Translations from Dutch are mine and are marked as such.

## What this facet covers

The brief asked for the law, and the legal scholarship, on safeguards at the point where an algorithmic system's output becomes a decision about a person, and for a check of one sentence in `MANUSCRIPT_v2.md` §4.4: "no independent party with binding authority stands at the point where an algorithmic intermediary's reading becomes a decision, and no rule requires anyone to read, explain, and certify a person's understanding before she is bound." The same section adds that "The checks that exist are recent, regional, after the fact, and in the first instance the intermediary's own."

I covered five groups: (1) EU instruments (Platform Work Directive 2024/2831; DSA 2022/2065; GDPR Art 15(1)(h), Art 22 and Recital 71; AI Act 2024/1689 as amended by the Digital Omnibus 2026/1744; P2B Regulation 2019/1150); (2) CJEU and national case law on those instruments (SCHUFA C-634/21; Dun & Bradstreet Austria C-203/22; Elite Taxi C-434/15; the Amsterdam Court of Appeal's Uber and Ola rulings of 4 April 2023); (3) US law (Colorado SB 26-189, which repealed and re-enacted the 2024 Colorado AI Act; NYC Local Law 144 and its DCWP rules, with the State Comptroller's 2025 audit; Regulation B and the CFPB's withdrawn Circular 2022-03); (4) contract law on standard forms (Radin; Kim; Cohen); (5) legal scholarship on explanation, contestation and due process (Wachter, Mittelstadt and Floridi; Wachter, Mittelstadt and Russell; Edwards and Veale; Kaminski; Kaminski and Urban; Citron; Crawford and Schultz; Selbst and Powles; Veale, Silberman and Binns; Adams-Prassl et al.; Aloisi et al.; Crootof, Kaminski and Price). I add one empirical source on the DSA's out-of-court bodies (Appeals Centre Europe, May 2026).

## Method notes

- **EU texts.** EUR-Lex itself returns a bot challenge (earlier facets M2 and Z recorded this; I did not retry it). I fetched every EU act and judgment from the Publications Office, `publications.europa.eu/resource/celex/<CELEX>` with `Accept: application/xhtml+xml`, which serves the Official Journal and ECR text. This is the method AUDIT_05 used. CELEX numbers: 32024L2831, 32022R2065, 32016R0679, 32024R1689, 32026R1744, 32019R1150, 62021CJ0634, 62022CJ0203, 62015CJ0434. Quotations below are verbatim from those copies. The brief said "quote article text from EUR-Lex"; this is the same Official Journal text from the EU's publisher, not EUR-Lex's page.
- **Case law.** The CJEU texts carry paragraph numbers, which I give. The Dutch judgments come from `data.rechtspraak.nl` (open data XML, ECLI:NL:GHAMS:2023:793, 796, 804). Paragraph numbers for the Dutch rulings are read from the `<nr>` tags in the XML and are approximate to ±1.
- **US texts.** Colorado SB 26-189 (signed act PDF from leg.colorado.gov; the bill page itself refused curl and I read it through the fetch tool); NYC DCWP Notice of Adoption of Final Rule (6 RCNY 5-300 ff.) and DCWP FAQ (PDFs from rules.cityofnewyork.us and nyc.gov); NY State Comptroller report 2024-N-6 (PDF from osc.ny.gov); 12 CFR 1002.9 (eCFR renderer API); CFPB Circular 2022-03 and the CFPB "Withdrawn Guidance" page (consumerfinance.gov). I did not open the text of NYC Local Law 144 itself (amlegal returned 403); I rely on the DCWP rule and the Comptroller's summary of it.
- **Scholarship.** Open copies only: Oxford ORA accepted manuscript (Wachter et al. 2017), arXiv (Wachter et al. 2018), LawArXiv/OSF (Kaminski 2019; Veale et al. 2023), Columbia Law Review site (Kaminski and Urban 2021), Washington University journal site (Citron 2008), Boston College LIRA repository (Crawford and Schultz 2014), the author's CC-licensed printable chapters (Cohen 2019). SAGE (Adams-Prassl et al.), OUP (Selbst and Powles), Kluwer (Aloisi et al.) and SSRN returned 403 or have no open copy; I recorded the block and did not work around it. Unpaywall was not used.
- **DOIs.** Each was resolved at `api.crossref.org/works/<doi>` and the title compared. Statutes and judgments have no DOI; they carry ELI, CELEX, ECLI or an official URL.
- **Pagination.** Where an open copy has its own pagination (Wachter et al. 2017 accepted manuscript; Wachter et al. 2018 arXiv; Kaminski 2019 preprint; Cohen's printable chapter), I give that copy's page and say so. Crawford and Schultz, Citron, Kaminski and Urban, and Veale et al. carry the journal's pagination.
- **Downloads.** All files are in `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/N2_platform_law/` (`eu/`, `us/`, `nl/`, `dsa/`, `scholarship/`), each with a `.txt` extraction. Nothing from them was executed; the HTML-to-text converter ran with `python3 -I` from a separate scratch directory.
- **Existing keys reused** (no new entry in `N2_platform_law.bib`; upgraded read depths are listed in an `@comment` block there): `eu2024platformwork`, `eu2022dsa`, `eu2016gdpr`, `eu2024aiact`, `euomnibus2026`, `eu2019p2b`, `regb2026`, `wachter2017why`, `kaminski2021right`, `citron2008technological`, `edwards2017slave`, `radin2013boilerplate`, `kim2013wrap`, `cohen2019between`, `williams1965walker`, `hill1997gateway`. `references.bib` holds two entries for the AI Act (`euaiact2024` and `eu2024aiact`); I use `eu2024aiact` and flag the duplicate.

## Read-depth key

- **Full**: read the whole text.
- **Part**: opened the text and read the named sections, articles or paragraphs.
- **Abstract**: database abstract only.
- **Record**: Crossref or official record verified; text not opened.

## 1. EU legislation

**Platform Work Directive, Directive (EU) 2024/2831** — `eu2024platformwork`. **Part** (Arts 1, 2, 7–15, 18–24, 29–31; Official Journal text). Eight provisions bear on §4.4.

1. *A human at the point of decision.* Art 10(5): "Any decision to restrict, suspend or terminate the contractual relationship or the account of a person performing platform work or any other decision of equivalent detriment shall be taken by a human being."
2. *Partial independence inside the firm.* Art 10(2): the persons charged with oversight "shall have the competence, training and authority necessary to exercise that function, including for overriding automated decisions. Those persons shall enjoy protection from dismissal or its equivalent, disciplinary measures and other adverse treatment where they exercise their functions."
3. *Reasons, at the latest when the decision bites.* Art 11(1): a written statement of reasons for a decision "to restrict, suspend or terminate the account", to refuse payment, on contractual status, or "any other decision affecting the essential aspects of the employment or other contractual relationships, without undue delay and at the latest on the date on which it takes effect."
4. *Review by the platform.* Art 11(2): the worker may "request the digital labour platform to review the decisions"; the platform replies "within two weeks". Art 11(3): where the decision "infringes the rights" of the worker, the platform "shall rectify that decision ... within two weeks", or "offer adequate compensation".
5. *Ex ante prohibitions.* Art 7(1) bars processing of emotional state, private conversations, off-duty data, data to predict the exercise of fundamental rights, inference of protected characteristics, and biometric identification; Art 7(2) applies these "from the start of the recruitment or selection procedure".
6. *Notice before the procedure and before changes.* Art 9(5): information to job applicants "before the start of the recruitment or selection procedure"; Art 9(3)(b): to workers "prior to the introduction of changes affecting working conditions". Art 9(1)(b)(iii) is the "main parameters ... and the relative importance of those main parameters" provision the manuscript quotes at §5.3 as "art. 9(1)(b)".
7. *The person's own record.* Art 9(6): portability of data "including ratings and reviews", with free tools, and "Where the person performing platform work so requests, the digital labour platform shall transmit such personal data directly to a third party."
8. *Courts and evidence.* Art 18: "timely, effective and impartial dispute resolution and a right to redress". Art 21(1): courts or competent authorities may "order the digital labour platform to disclose any relevant evidence which lies in its control". Art 23(3) shifts the burden of proof for retaliatory dismissal.

Scope and timing: Art 1(2) extends the algorithmic-management rules to "persons performing platform work ... including those who do not have an employment contract"; Art 11(5) excludes persons who are also business users under the P2B Regulation. Art 29(1): transposition "by 2 December 2026". Web trackers (mid-2026, secondary, not used as sources) report that no Member State had fully transposed; I could not confirm the October 2026 position.

*Bearing:* §4.4, §5.2, §5.4, §5.6. *Sharpens and partly challenges.* Art 10(5) puts a human at the point of decision, so "the checks listed above operate after the decision" is wrong for the Directive. Art 10(2) gives that human statutory protection against the operator, which is a step toward independence inside the firm. Neither makes the human independent of the operator or binding on it from outside; the first reviewer under Art 11(2) is the platform. Art 9(6) and Art 21 are the closest existing law to the "own record" half of counter-delegation (§5.4).

**Digital Services Act, Regulation (EU) 2022/2065** — `eu2022dsa`. **Part** (Arts 14, 17, 20, 21; OJ text).

- Art 14(1): terms and conditions must disclose "algorithmic decision-making and human review"; Art 14(2): providers "shall inform the recipients of the service of any significant change"; Art 14(4): restrictions applied "in a diligent, objective and proportionate manner".
- Art 17(2): the statement of reasons "shall apply at the latest from the date that the restriction is imposed".
- Art 20(6): complaint decisions "taken under the supervision of appropriately qualified staff, and not solely on the basis of automated means" (the manuscript quotes this correctly).
- Art 21(2): "The certified out-of-court dispute settlement body shall not have the power to impose a binding settlement of the dispute on the parties" (quoted correctly at §4.4). Art 21(3)(a): the body must be "impartial and independent, including financially independent, of providers of online platforms and of recipients". Art 21(5): if the body decides for the user, "the provider of the online platform shall bear all the fees", and a losing user need not reimburse the platform's fees save in bad faith.

*Bearing:* §4.4, §5.4. *Supports the bindingness half; challenges the cost sentence.* The DSA body is independent but not binding, which is the claim. But §4.4's "the cost of reaching it falls on the weaker party" is wrong for the DSA route, where Art 21(5) shifts fees to the platform. The sentence holds only for the court route. *Scope caution:* see Elite Taxi (§2 below); the DSA reaches "online platforms", which are information society services, and the CJEU has held a ride-hail intermediation service of the UberPop type not to be one. The paper's lead example (ride-hail drivers) may therefore fall outside Arts 20–21.

**GDPR, Regulation (EU) 2016/679** — `eu2016gdpr`. **Part** (Arts 15(1)(h), 22; Recital 71; OJ text).

- Art 22(1): "The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her."
- Art 22(3): in the contract and consent cases only, "at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision" (quoted correctly at §4.4).
- Recital 71 names "automatic refusal of an online credit application or e-recruiting practices without any human intervention" and lists the safeguard "to obtain an explanation of the decision reached after such assessment and to challenge the decision".
- Art 15(1)(h): "meaningful information about the logic involved, as well as the significance and the envisaged consequences".

*Bearing:* §4.4, §5.2. *Read with SCHUFA and Dun & Bradstreet below, it challenges §4.4's framing.* The manuscript presents Art 22 as an after-the-fact right to human intervention. The CJEU reads Art 22(1) as a "prohibition in principle" that applies before any decision is taken and that attaches to the intermediary's score itself.

**AI Act, Regulation (EU) 2024/1689** — `eu2024aiact`. **Part** (Arts 13, 14, 26, 27, 85, 86, 113; Annex III points 4–5; OJ text). As amended by **Digital Omnibus on AI, Regulation (EU) 2026/1744** — `euomnibus2026`. **Part** (Art 1 amendment of Art 113; recital on dates).

- Art 13(1): high-risk systems must be "sufficiently transparent to enable deployers to interpret a system's output and use it appropriately". The transparency duty runs to the deployer (the employer or lender), not to the person scored.
- Art 14(1): systems must be designed so that they "can be effectively overseen by natural persons during the period in which they are in use"; Art 14(4)(b) names "automation bias"; Art 14(4)(d): the overseer must be able "to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output".
- Art 26(2): deployers "shall assign human oversight to natural persons who have the necessary competence, training and authority"; Art 26(7): employers inform workers "Before putting into service or using a high-risk AI system at the workplace"; Art 26(11): deployers "that make decisions or assist in making decisions related to natural persons shall inform the natural persons that they are subject to the use of the high-risk AI system".
- Art 27(1), (3): deployers of credit-scoring systems (Annex III 5(b)) and public-service deployers perform a fundamental rights impact assessment "Prior to deploying" and "notify the market surveillance authority of its results".
- Art 85: complaints to a market surveillance authority "shall be taken into account for the purpose of conducting market surveillance activities" — an input to supervision, not an individual remedy.
- Art 86(1): a person subject to a deployer's decision based on an Annex III system "shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken"; Art 86(3): only "to the extent that the right ... is not otherwise provided for under Union law".
- Annex III point 4 covers recruitment and "decisions affecting terms of work-related relationships, the promotion or termination ... to allocate tasks"; point 5(b) covers creditworthiness and credit scoring.
- Dates. Original Art 113: applies from 2 August 2026. The Omnibus replaces Art 113(c): "Chapter III, Sections 1, 2, and 3 ... shall apply from: (i) 2 December 2027 as regards AI systems classified as high-risk pursuant to Article 6(2) and Annex III". Arts 13, 14, 26 and 27 sit in Chapter III Section 2–3, so for hiring and credit they do not apply until 2 December 2027. Art 86 (Chapter IX) was not amended; whether it bites before the Annex III obligations apply is unclear, and I found no authority on the point.

*Bearing:* §4.4, §5.3. *Supports and sharpens.* The Act puts a human with power to override at the point of decision (Art 14(4)(d)), but that human is the deployer's (Art 26(2)); no independent party appears. Art 13(1) is a precise legal instance of the paper's triad point: the law's transparency flows to the party that buys the reading, not to the party read. The Omnibus delay makes "recent" an understatement: for the paper's hiring and credit cases the oversight rules are not yet in force.

**P2B Regulation, Regulation (EU) 2019/1150** — `eu2019p2b`. **Part** (Arts 3, 4, 5, 11, 12; OJ text).

- Art 3(2): proposed changes to terms "shall not be implemented before the expiry of a notice period ... at least 15 days"; Art 3(3): non-compliant terms and changes "shall be null and void".
- Art 4(1): for restriction or suspension, a statement of reasons "prior to or at the time of the restriction or suspension taking effect"; Art 4(2): for termination of the whole service, "at least 30 days prior to the termination taking effect". Art 4(3): the user may "clarify the facts and circumstances" in the internal complaint process.
- Art 5(6): providers need not "disclose algorithms".
- Art 12(1)–(2): providers name "two or more mediators", who must be "impartial and independent"; Art 12(3) "Notwithstanding the voluntary nature of mediation"; Art 12(4): providers bear "a reasonable proportion of the total costs".

*Bearing:* §4.4, §5.3. *Corrects a fact and sharpens §5.3.* The manuscript says the regulation "requires a statement of reasons 'on a durable medium' before an account is restricted (art. 4)". Art 4(1) says "prior to or at the time of" the restriction, so "before" overstates it for restrictions; for termination Art 4(2) requires 30 days' notice in advance, which is an ex ante safeguard the paper does not mention. Art 3(2)–(3) is a legal constraint on re-declaring the rules (notice, with nullity as the sanction), which is what §5.3 says a declared operating envelope needs. The P2B protects business users only.

## 2. Case law

**CJEU, Case C-634/21, *OQ v Land Hessen (SCHUFA Holding)*, judgment of 7 December 2023, ECLI:EU:C:2023:957** — `cjeu2023schufa`. **Full** (judgment, about 7,700 words).

The court held that a credit bureau's score is itself an Art 22 decision when a lender "draws strongly" on it (para. 73). Four passages matter.

- Para. 52: Art 22(1) "lays down a prohibition in principle, the infringement of which does not need to be invoked individually by such a person."
- Para. 61: "in circumstances such as those at issue in the main proceedings, in which three stakeholders are involved, there would be a risk of circumventing Article 22 of the GDPR and, consequently, a lacuna in legal protection if a restrictive interpretation of that provision was retained, according to which the establishment of the probability value must only be considered as a preparatory act".
- Para. 63: without this reading, the bureau would not owe the Art 15(1)(h) information, and the lender "would not be able to provide that specific information because it generally does not have it."
- Para. 64: such scoring "is prohibited unless one of the exceptions set out in Article 22(2) ... is applicable".

Para. 16 records the facts the paper would recognise: SCHUFA gave the applicant her score and "outlined, in broad terms, the methods", but "referring to trade secrecy, it refused to disclose the various elements ... and their weighting", and said "it was those contractual partners which made the actual contractual decisions."

*Bearing:* §2.1 (the triad), §4.1 row 1 and row 3, §4.4, §5.2. *Supports the triad strongly; challenges the "no rule" half of §4.4.* The CJEU names the three-party structure and treats the intermediary's reading as the decision, which is the paper's §2.1 claim in legal form. It also means that, in the EU, a rule does stand at the point where the intermediary's reading becomes decisive: solely automated scoring that a lender relies on is prohibited unless law, contract necessity or explicit consent authorises it, with safeguards. That rule is enforced by supervisory authorities and courts after the fact, and the human it guarantees is still "on the part of the controller" (para. 66). Wachter, Mittelstadt and Floridi (2017, AM p. 33, p. 44) had read the earlier German *SCHUFA* judgments as a "loophole"; the CJEU closed it.

**CJEU, Case C-203/22, *CK v Dun & Bradstreet Austria GmbH*, judgment of 27 February 2025** — `cjeu2025dun`. **Part** (paras 40–76 and the operative part). ECLI not printed in the copy; the Publications Office CELEX is 62022CJ0203.

- Para. 57: "Article 15(1)(h) of the GDPR affords the data subject a genuine right to an explanation as to the functioning of the mechanism involved in automated decision-making of which that person was the subject and of the result of that decision."
- Para. 58: "a right to an explanation of the procedure and principles actually applied".
- Para. 59: not satisfied "either by the mere communication of a complex mathematical formula, such as an algorithm, or by the detailed description of all the steps".
- Para. 62: it may suffice "to inform the data subject of the extent to which a variation in the personal data taken into account would have led to a different result" — the counterfactual form Wachter, Mittelstadt and Russell (2018) proposed.
- Para. 74 and operative point 2: where the controller claims trade secrets, "that information must be disclosed to the competent supervisory authority or court, which must balance the rights and interests at issue".

*Bearing:* §1, §4.2, §5.3, §5.4. *Settles a debate the paper cites and sharpens counter-delegation.* The paper cites Kim and Routledge (2022) for a right to explanation and Edwards and Veale (2017) for its limits; the CJEU has now held that the right exists. That supports §4.2's framing ("I do not dispute that such a right exists") and makes Wachter et al. (2017) dated on the point. Para. 74 places an independent party with binding power — a court or supervisory authority — between the operator's trade secret and the person's claim to know. That is a partial legal precedent for §5.4's "independent party able to bind the operator on a dispute", but it operates after the decision and on request.

**CJEU, Case C-434/15, *Asociación Profesional Elite Taxi v Uber Systems Spain SL*, Grand Chamber, 20 December 2017** — `cjeu2017elite`. **Part** (paras 37–40 and the ruling).

- Para. 39: "Uber exercises decisive influence over the conditions under which that service is provided by those drivers ... Uber determines at least the maximum fare ... receives that amount from the client before paying part of it to the non-professional driver ... and ... exercises a certain control over the quality of the vehicles, the drivers and their conduct, which can, in some circumstances, result in their exclusion."
- Para. 40: the intermediation service "must be classified not as 'an information society service' ... but as 'a service in the field of transport'".

*Bearing:* §2.1 (the doubled role), §4.4 (DSA scope). *Supports §2.1; complicates §4.4.* The Grand Chamber describes the doubling §2.1 asserts (matcher, price-setter, controller of the driver's exclusion). It also limits the DSA's reach: the case concerned UberPop with non-professional drivers, and I found no ruling in this round on whether today's ride-hail apps are information society services. The paper should not rely on DSA Arts 20–21 for ride-hail drivers without saying so.

**Gerechtshof Amsterdam, 4 April 2023, ECLI:NL:GHAMS:2023:793 (drivers v Uber B.V.)** — `amsterdam2023uber`. **Part** (summary; facts at 2.x; rov. ≈3.21–3.24 on whether deactivations were solely automated; Dutch text, my translations). Companion: **ECLI:NL:GHAMS:2023:804 (drivers v Ola Netherlands B.V.)**, **Part** (summary; the fraud-probability score passage). Both in `nl/`.

- Uber deactivated four drivers for "fraud" and told them by e-mail that the decisions were "niet uitsluitend op basis van geautomatiseerde verwerking ... genomen" (not taken solely on automated processing). The court of appeal held (rov. ≈3.24, my translation) that Uber "has not sufficiently made plausible that ... there was actual human intervention", and that Uber bore a heavier duty to substantiate "since the information about any human intervention lies largely within Uber's domain." It rejected Uber's trade-secret objection to the Art 15(1)(h) request as not justifying a refusal of the whole request.
- In the Ola ruling the court held that a "fraud probability score" significantly affects drivers because "Van deze score hangt immers af of Ola al dan niet overgaat tot nadere maatregelen" (whether Ola takes further measures depends on this score) and noted one driver's difficulty in having the accusation erased "Doordat hij geen informatie had over hoe de beschuldiging tot stand was gekomen" (because he had no information about how the accusation had come about).

*Bearing:* §4.1 row 3 (the record), §4.4, §5.4. *Supports and sharpens.* A court did act as an independent, binding check on ride-hail deactivations, but years after the fact (decisions of 2018–2020, ruling in 2023), and its main tool was to shift the burden because the record of the decision sat with the platform. That is the §4.1 record row in a judgment. It is the strongest evidence I found that "after the fact" carries the claim, not "no independent party".

## 3. United States

**Colorado SB 26-189, "Concerning the use of automated decision-making technology in consequential decisions", signed 14 May 2026** — `colorado2026automated`. **Part** (signed act: Section 1 heading, §6-1-1701(15), §6-1-1705, Section 5). Section 1 says the act "repeal[s] and reenact[s], with amendments, part 17 of article 1 of title 6"; the official bill page (read through the fetch tool) says this replaces the protections "the general assembly enacted [in] Senate Bill 24-205". So the "Colorado AI Act" the brief names never took effect in its 2024 form.

- §6-1-1701(15) (p. 8): "'Meaningful human review' means review by a[n] individual designated by the deployer who has authority to approve, modify, or override a consequential decision and who ... (c) does not default to the system output".
- §6-1-1705(1)(a)(II) (p. 14): after an adverse outcome, "an opportunity for meaningful human review and reconsideration of the consequential decision, to the extent commercially reasonable."
- §6-1-1705(1)(c) (p. 15): the correction right "does not require correction of opinions, predictions, scores, or protected evaluations."
- Section 5 (p. 23): the act "takes effect January 1, 2027" and "applies to consequential decisions made on or after January 1, 2027."

*Bearing:* §4.1 row 3, §4.4, §5.2. *Supports.* The reviewer is the deployer's designee, review is after the adverse outcome and qualified by commercial reasonableness, and a person may correct her data but not the score — the reading itself stays the operator's. That last clause is the record row of Table 1 in statutory form. It also confirms that the check is not yet in force.

**NYC Local Law 144 of 2021 and DCWP Notice of Adoption of Final Rule, 6 RCNY §§ 5-300 to 5-304 (2023)** — `nycdcwp2023automated`. **Part** (rule notice pp. 1, 3, 9; DCWP FAQ notice section). Statute text not opened.

- Rule notice p. 1: LL144 "prohibits employers and employment agencies from using an automated employment decision tool unless the tool has been subject to a bias audit within one year of the use of the tool, information about the bias audit is publicly available, and certain notices have been provided".
- §5-300, p. 3: "'Independent auditor' means a person or group that is capable of exercising objective and impartial judgment", excluding anyone "involved in using, developing, or distributing the AEDT" or employed by the user or vendor.
- §5-304(a), p. 9: the notice "must include instructions for how an individual can request an alternative selection process or a reasonable accommodation under other laws, if available. Nothing in this subchapter requires an employer or employment agency to provide an alternative selection process."
- Notice "at least 10 business days before use of an AEDT" (§5-304(b), p. 9).

**New York State Comptroller, *Enforcement of Local Law 144 – Automated Employment Decision Tools*, Report 2024-N-6 (December 2025)** — `nyosc2025enforcement`. **Part** (pp. 1–2, 7–11).

- p. 8: "LL144 does not require employers to take specific action if they find an AEDT tool has produced biased or discriminatory outcomes."
- p. 1: "DCWP's AEDT complaint process is ineffective"; DCWP received "only two AEDT complaints during the audit's scope". p. 2: DCWP found one issue among 32 companies; the auditors found "at least 17 instances of potential non-compliance" (p. 10 gives 22 companies for the same comparison; the report is inconsistent).

*Bearing:* §4.4, §5.2. *The closest counterexample to "no independent party", and its limits.* LL144 is the only instrument I found that requires an independent party before the system is used. The auditor checks the tool, not the decision, and nothing must follow from a biased result (OSC p. 8). The DCWP rule states in terms that no alternative route is required (§5-304(a)), which is exactly what §5.2's structural refusal would add. Enforcement evidence (OSC) shows the requirement is weakly policed.

**12 C.F.R. § 1002.9 (Regulation B)** — `regb2026`. **Part** (§1002.9(a)(1)–(2), (b)(2)).

- (a)(1): notice of action "within ... 30 days after receiving a completed application"; (b)(2): reasons "must be specific and indicate the principal reason(s)"; "Statements that the adverse action was based on the creditor's internal standards or policies or that the applicant ... failed to achieve a qualifying score on the creditor's credit scoring system are insufficient."

**CFPB, Consumer Financial Protection Circular 2022-03, *Adverse action notification requirements in connection with credit decisions based on complex algorithms*, 87 FR 35864 (14 June 2022), withdrawn 12 May 2025** — `cfpb2022adverse`. **Part** (question, response, analysis; withdrawal page entry).

- The circular answered "Yes": creditors using "uninterpretable or 'black-box' models" must still give specific reasons, and quoted the purpose that "'if creditors know they must explain their decisions . . . they [will] effectively be discouraged' from discriminatory practices".
- The CFPB "Withdrawn Guidance" page lists: "Consumer Financial Protection Circular 2022-03 ... withdrawn on May 12, 2025". Circular 2023-03 (sample forms) was withdrawn the same day. Regulation B itself is unchanged.

*Bearing:* §4.4 ("recent, regional"), §5.3. *Challenges "recent, regional".* Specific-reasons rules for credit are US federal law and are not specific to algorithmic systems; the paper's "regional" (implying EU) and "recent" do not fit them. The CFPB's withdrawal of the algorithm-specific guidance supports the paper's broader point that such checks are fragile. Reasons come after the action (within 30 days), so the "after the fact" claim holds for credit. I did not verify ECOA's enactment date from an opened text.

## 4. Contract law and standard forms

**Radin, *Boilerplate* (2013)** — `radin2013boilerplate`. **Record** (unchanged from M3). Princeton's sample chapter was not found; the book was not opened.

**Kim, *Wrap Contracts* (2013)** — `kim2013wrap`. **Record** (unchanged from M3). SSRN record 2322255 seen in a search result only; no open text.

**Cohen, *Between Truth and Power* (2019), ch. 5 "The End(s) of Judicial Process"** — `cohen2019between`. **Part** (ch. 5, printable CC-licensed version from the author's site, its pp. 11–14; not the OUP pagination). Upgraded from Record.

- p. 12: courts "have become increasingly willing to enforce boilerplate clauses that constrain access to judicial process"; under "extreme deference to (presumed) individual waiver", "the underlying conception of individual agency is vanishingly thin, consisting of little more than the ability to decline a transaction or employment relationship."
- p. 12: "boilerplate waivers effectively instantiate private regulation of employment relationships and consumer rights and remedies".
- p. 13: "For the vast majority of consumers who become involved in disputes with providers of goods and services, the first and last stop is the provider's internal process for resolving customer complaints."

*Bearing:* §4.4 ("in the first instance the intermediary's own"), §5.6 (consent objection). *Supports; a referee in law and technology would expect it.* Cohen supplies the general claim behind the paper's narrower one: first-instance dispute resolution has been moved inside the firm, and consent has been reduced to the ability to decline. Radin and Kim remain unread; a contracts referee will expect one of them at §5.6, and the author needs a library copy.

## 5. Legal scholarship on explanation, contestation and due process

**Wachter, Mittelstadt and Floridi (2017), "Why a Right to Explanation of Automated Decision-Making Does Not Exist in the General Data Protection Regulation"** — `wachter2017why`. **Part** (Oxford ORA accepted manuscript, 47 pp., its own pagination: abstract, §2 pp. 5–6, pp. 33, 38, 43–46). Upgraded from "not accessible".

- Abstract: the GDPR "only mandates that data subjects receive meaningful, but properly limited, information (Articles 13-15) about the logic involved ... what we term a 'right to be informed'".
- AM p. 6 sets the distinction the paper needs: "an ex ante explanation occurs prior to an automated decision-making taking place. Note that an ex ante explanation can logically address only system functionality, as the rationale of a specific decision cannot be known before the decision is made".
- AM p. 33: the word "solely" "opens a loophole whereby any human involvement in a decision-making process could mean it is not 'automated decision-making'"; the strict reading "was reflected in the SCHUFA judgments".
- AM p. 38: Art 22(1) can be read as a prohibition or a right to object.
- AM p. 46, recommendation 7: "An ideal solution would allow for examination of automated decision-making systems, including the rationale and circumstances of specific decisions, by a trusted third party."

*Bearing:* §4.2, §4.4, §5.3, §5.4. *Partly overtaken; partly already says the paper's argument.* On the existence of an explanation right and on prohibition versus objection, SCHUFA (para. 52) and Dun & Bradstreet (para. 57) have since gone the other way; a referee will expect the paper to say so if it cites the debate. The p. 6 point gives §5.3 a sharper reason for the envelope: before the decision, only the system can be described, so any check at the point of decision must bind on the system's limits, not explain the case. Recommendation 7's "trusted third party" anticipates §5.4.

**Wachter, Mittelstadt and Russell (2018), "Counterfactual Explanations Without Opening the Black Box"** — `wachter2018counterfactual`. **Part** (arXiv 1711.00399, pp. 1–6). Published at 31 Harv. J.L. & Tech. 841 (citation as given in Kaminski and Urban 2021, p. 1964 n.; not checked against the journal).

- arXiv p. 4: three aims for explanations: "(1) to inform and help the subject understand why a particular decision was reached, (2) to provide grounds to contest adverse decisions, and (3) to understand what could be changed to receive a desired result in the future ... As we show, the GDPR offers little support to achieve any of these aims."

*Bearing:* §4.2, §5.3. *Sharpens.* The CJEU in Dun & Bradstreet (para. 62) endorsed the counterfactual form. Aim (3) is the "coping" the paper, after Lovett, says does not reduce domination (§2.2, §4.2).

**Edwards and Veale (2017)** — `edwards2017slave`. **Part** (unchanged; read by M2, used at §1 and §4.1). Not re-read. The paper already uses its "transparency fallacy".

**Kaminski (2019), "The Right to Explanation, Explained"** — `kaminski2019right`. **Part** (LawArXiv preprint of 15 June 2018, 25 pp., its own pagination: abstract, pp. 1–2, 14, 24–25). Published at 34 Berkeley Tech. L.J. 189 (citation as given in Kaminski and Urban 2021, n. 25, p. 1963).

- p. 14: the Working Party guidelines require a reviewer with "the appropriate authority and capability to change the decision" — "another form of transparency, albeit within a company"; the opportunity to be heard "risks being, as currently described, reduced to the provision of a contact email."
- p. 14: guidelines read "suitable safeguards" to include "quality assurance checks, algorithmic auditing, independent third party auditing".
- p. 24: "individual transparency rights largely occur after the fact of algorithmic development"; systemic measures are "ongoing and continuous".
- p. 25: "There is a right to explanation"; and "Its heavy reliance on collaborative governance in the absence of significant public or third-party oversight is not a known recipe for success".

*Bearing:* §4.4, §5.4. *Supports and already says part of it.* Kaminski predicted the CJEU's position on the existence of the right and named the gap the paper names (no significant third-party oversight), in a systemic rather than triadic frame.

**Kaminski and Urban (2021), "The Right to Contest AI"** — `kaminski2021right`. **Part** (Columbia Law Review PDF: abstract; Part III.F, p. 2030; Part IV.B.2 "A Legitimate Decision-Maker", pp. 2038–2039). Upgraded from "not read".

- p. 2038: "A neutral arbiter is considered core to due process. A neutral arbiter affords dignity to participants, tethers parties' discretion, and helps identify and eschew bias and error ... Schemes that lack a neutral arbiter may gain efficiency at the cost of legitimacy." Platforms in DMCA notice-and-takedown "are not neutral arbiters".
- p. 2039: "A right to contest private sector AI decisions, however, is unlikely to include a neutral arbiter, at least at first bite ... Neither our archetype contestation schemes nor Article 22 feature a neutral arbiter. To the contrary, interested actors make the decisions." They propose "requiring the arbiter to hold an independent position within a company or ... hybrid private–public systems for 'appeals.'"
- p. 2030 (III.F): "A contestation scheme may house contestation with a neutral arbiter, have a mediating platform adjudicate, or have one of the parties themselves adjudicate."

*Bearing:* §4.4, §5.4, §5.6. *Already says the paper's §4.4 claim, for private-sector AI generally.* The paper must cite them for the independence point; its own contribution is the triad (the "mediating platform" is the party the paper analyses) and the historical precedent. PWD Art 10(2) has since enacted a version of their "independent position within a company".

**Citron (2008), "Technological Due Process"** — `citron2008technological`. **Part** (pp. 1254, 1272; M3 read pp. 1253, 1305).

- p. 1254: "Even if an individual seeks and receives a hearing, a hearing officer's belief that computer decisions are error-resistant increases the likelihood of inaccurate outcomes"; "Programmers routinely change the substance of rules when translating them from human language into computer code."
- p. 1272: "Automation bias effectively turns a computer program's suggested answer into a trusted final decision ... little meaningful difference exists between a mixed system and its fully automated counterpart."

*Bearing:* §4.4, §5.2. *Challenges the weight a reader might give PWD Art 10(5) and AI Act Art 14.* A human at the point of decision is not a check if the human defers; the AI Act itself names "automation bias" (Art 14(4)(b)). Citron's setting is government, not private intermediaries.

**Crawford and Schultz (2014), "Big Data and Due Process"** — `crawford2014big`. **Part** (abstract; pp. 113, 118–120, 125–128). No DOI; Boston College LIRA copy with journal pagination.

- p. 113: due process requires "(1) participatory procedures ...; (2) a neutral arbiter; (3) prior process (i.e., the hearing precedes the adverse action); and (4) continuity".
- p. 120: "With many Big Data determinations, there is little or no regulation of the interactions among the algorithm's designer (the lawmaker), the person who oversees the queries (the executive), and the adjudicator (the computational output). Accordingly, there is no system of checks and balances".
- p. 127: in contexts with proprietary concerns, review "could be given to a trusted third party who would act as a neutral data arbiter"; the arbiter "could examine the relationship between those who designed the analytics and those who run the individual processes to make sure that their roles are appropriate and distinct." p. 128: this "would require some form of audit trail".

*Bearing:* §4.4 (the third feature, separation of roles), §5.4. *Already says it.* The "neutral data arbiter" is counter-delegation's second half, proposed in 2014; the separation of designer, executive and adjudicator is §4.4's "separation of roles". The paper's difference is the triad and the notarial precedent. A referee in law and technology would object if the paper omitted them.

**Veale, Silberman and Binns (2023), "Fortifying the algorithmic management provisions in the proposed Platform Work Directive"** — `veale2023fortifying`. **Part** (published version on OSF: abstract, §3.1–3.2, pp. 11–14). On the 2021 proposal, not the final text.

- p. 11: "substituting a human for a machine in a review process does not ameliorate concerns around the consequences of a decision without a substantive standard of review"; the proposal's standard (rectify decisions that infringe the worker's rights) turns review into "a new point of enforcement for existing rules".
- p. 13: "algorithms risk being both the mechanism of decision-making and the believed empirical basis for such a decision ... the human reviewer can do little but to look for obvious bugs or errors".
- p. 14: a substantive restatement may make platforms "less likely to see human review as a formality which itself can be passed out to precarious workers, such as through the emerging 'human in the loop as a service' industry".

*Bearing:* §4.4, §5.4. *Sharpens.* Independence is not the only gap; the standard against which the human reviews matters, and the reviewer may be outsourced labour. The final Directive kept the "infringes the rights" standard (Art 11(3)).

**Adams-Prassl, Abraha, Kelly-Lyth, Silberman and Rakshita (2023), "Regulating algorithmic management: A blueprint"** — `adamsprassl2023regulating`. **Abstract** (SAGE returned 403). The abstract sorts human involvement into "'in the loop' (banning fully automated terminations), 'after the loop' (a right to meaningful review), 'before the loop' (information and consultation rights) and 'above the loop' (impact assessments)".

*Bearing:* §4.4, §5. *Sharpens the timing claim.* This taxonomy would let §4.4 say precisely which loop lacks an independent party (all four, on the evidence above).

**Aloisi, Potocka-Sionek and Ratti (2025), "Straddling two horses"** — `aloisi2025straddling`. **Abstract** (Kluwer; not open). The abstract describes the Directive as "uniquely combining digital and social regulation" and analyses "workers' digital rights vis-à-vis automated systems". Crossref gives pages "1407-1148" (an evident error in the record). *Bearing:* §4.4. The current doctrinal commentary on the final Directive; a labour-law referee would expect it.

**Selbst and Powles (2017), "Meaningful information and the right to explanation"** — `selbst2017meaningful`. **Record** (OUP 403; Crossref has no abstract). The reply to Wachter et al.; Kaminski and Urban (2021, n. 127, p. 1979) cite it at 7 Int'l Data Priv. L. 233, 235. *Bearing:* §4.2, if the paper cites the 2017 debate at all.

**Crootof, Kaminski and Price (2022), "Humans in the Loop"** — `crootof2022humans`. **Abstract** (SSRN record). The abstract names "the MABA-MABA trap, which occurs when policymakers attempt to address concerns about algorithmic incapacities by inserting a human into [the] decisionmaking process". *Bearing:* §4.4, with Citron. Optional.

**Ponce del Castillo (2025), "The Right to Meaningful Explanation in Algorithmic Management: Commentary on ... Dun & Bradstreet Austria"** — `poncedelcastillo2025right`. **Abstract** (SSRN record). Applies C-203/22 to workplace ADM. *Bearing:* §4.4, §5.3. Optional, but a direct bridge from the judgment to platform work.

## 6. Empirical: the DSA's out-of-court bodies in practice

**Appeals Centre Europe, *Transparency Report* (May 2026, covering April 2025 to March 2026)** — `ace2026transparency`. **Part** (pp. 3, 4, 11, 23, 29). A certified Art 21 body covering Facebook, Instagram, Pinterest, Threads, TikTok and YouTube.

- p. 3: "While our decisions are non-binding, and it is up to platforms whether to implement them, they must engage in good faith."
- p. 11: of more than 10,200 decisions, 7,378 (72%) were default decisions because "despite the dispute being eligible, the platform did not provide us with the content"; "In the vast majority of account suspension disputes, platforms failed to provide us with the content". Where content was reviewed, the body overturned the platform 59% of the time. "We are still not receiving consistent data about whether platforms have implemented our decisions."
- p. 23: of more than 1,000 decisions communicated in one user group's cases, "we are only aware of a handful of cases thus far where platforms have implemented our decision."

*Bearing:* §4.4, §5.4. *Supports strongly, with numbers.* The non-binding independent body exists, and in practice the platform withholds the record (the content) in most suspension cases and need not implement the result. This is the §4.1 record row and the §5.4 gap in one document. It is a self-report by the body, covering social media, not ride-hail or hiring.

## 7. The §4.4 claim, checked

The claim has three parts. I take them in turn.

**(a) "No independent party with binding authority stands at the point where an algorithmic intermediary's reading becomes a decision."** *Holds, read literally, in every instrument I opened.* The human at or near the point of decision is the operator's: PWD Art 10(5) and 11(2) (the platform), GDPR Art 22(3) ("on the part of the controller"), AI Act Arts 14 and 26(2) (the deployer), Colorado §6-1-1701(15) ("designated by the deployer"). The independent parties are not binding or not at the decision: DSA Art 21 bodies are independent and non-binding (Art 21(2), (3)(a)); P2B Art 12 mediators are independent and voluntary; the LL144 auditor is independent but audits the tool before use, and nothing must follow from the audit (OSC p. 8). Kaminski and Urban (2021, p. 2039) state the same conclusion for private-sector AI and Article 22. The independent bodies that do bind — courts and supervisory authorities — act after the decision and on the person's initiative (Amsterdam 2023; Dun & Bradstreet para. 74).

Three qualifications the paper must add:
1. *Independence inside the firm now has a statutory form.* PWD Art 10(2) protects overseers from dismissal and adverse treatment and gives them authority to override. That is not independence from the operator, but it is more than "the intermediary's own" in the ordinary sense.
2. *A rule does stand at the point of decision in EU data-protection law.* SCHUFA (paras 52, 61, 64) makes Art 22(1) a prohibition in principle and attaches it to the intermediary's score in a three-party case. The rule binds, but no one stands there to apply it.
3. *Ex ante independent review exists at the level of the tool* (LL144), and the paper's "point of decision" should be distinguished from "before use of the system".

**(b) "No rule requires anyone to read, explain, and certify a person's understanding before she is bound."** *Holds.* I found notice-before-use rules (LL144 10 business days; PWD Art 9(5); AI Act Art 26(7), (11); Colorado notice "at the point of interaction" per the bill page), notice-before-termination (P2B Art 4(2)) and notice-before-change (P2B Art 3(2); PWD Art 9(3)(b); DSA Art 14(2)). None requires anyone to read the terms or the system's limits to the person and certify her understanding. I found no such rule in the EU and US instruments listed in "What this facet covers".

**(c) "The checks that exist are recent, regional, after the fact, and in the first instance the intermediary's own."**
- *Recent:* true for the algorithm-specific instruments, and stronger than the paper says: PWD not yet transposed (deadline 2 December 2026); AI Act Annex III obligations postponed to 2 December 2027 (Omnibus); Colorado effective 1 January 2027; CFPB algorithm circular withdrawn 12 May 2025. *False* for Regulation B's specific-reasons rule, which is general and not new.
- *Regional:* *false as stated.* Colorado, New York City and federal Regulation B are US law. The paper lists only EU instruments, which a US referee will notice.
- *After the fact:* *partly false.* PWD Art 10(5) puts the human at the decision; PWD Art 7 and GDPR Art 22(1) (as read in SCHUFA) prohibit ex ante; P2B Art 4(2) requires 30 days' reasoned notice before termination; LL144 requires an independent audit before use. What is after the fact is every check by a party independent of the operator that can bind it.
- *In the first instance the intermediary's own:* *true*, and Cohen (2019, ch. 5 printable p. 13) supplies the general claim.

**Factual corrections for the author** (flagged, not made):
1. §4.4: P2B Art 4 does not require reasons "before an account is restricted". Art 4(1): "prior to or at the time of the restriction or suspension taking effect". Art 4(2): "at least 30 days prior" for termination of the whole service. Source: Regulation (EU) 2019/1150, OJ L 186, 11.7.2019.
2. §4.4: "the cost of reaching it falls on the weaker party" is wrong for DSA Art 21 bodies; Art 21(5) puts the fees on the platform when the user wins.
3. §5.3: the quoted PWD clause is Art 9(1)(b)(iii), not Art 9(1)(b).
4. §4.4: Art 10(5) PWD covers any "person performing platform work", not only "platform workers" (Art 2(1)(c)–(d) distinguishes the two).
5. §4.4 lists DSA Arts 20–21 among checks available to the paper's ride-hail drivers; Elite Taxi (C-434/15, para. 40) puts at least UberPop-type ride-hail outside "information society services", so the DSA may not reach them.

## Synthesis

The law has moved since the paper's sources were written, and in two directions. It has put a human, with protected authority to override, at the point of decision for platform work (PWD Art 10) and for high-risk AI (AI Act Art 14, delayed); it has made the GDPR's Art 22 a prohibition that attaches to an intermediary's score in a three-party case (SCHUFA); and it has confirmed a "genuine right to an explanation" (Dun & Bradstreet). None of this puts a party independent of the operator, with power to bind it, at the moment of decision. The independent bodies the law creates are either non-binding (DSA Art 21; P2B Art 12), confined to the tool before use (LL144), or courts and authorities that act later on the person's initiative. The empirical source I found shows what that gap costs: in most account-suspension disputes the platform did not hand the independent body the record (ACE 2026, p. 11).

The paper's claim therefore survives in its literal form and fails in its gloss. "No independent party with binding authority at the point of decision" holds. "Recent, regional, after the fact" overstates: the checks are partly ex ante, partly US, and the general credit-reasons rule is old. The paper should replace the gloss with a narrower statement: the law now places the operator's own human at the decision and an independent party after it, and nowhere joins independence, bindingness and timing in one office, as the notary's office did.

On prior work, Kaminski and Urban (2021, p. 2039) already say that private-sector contestation, including Article 22, lacks a neutral arbiter, and Crawford and Schultz (2014, pp. 120, 127) already propose a "neutral data arbiter" and the separation of designer, executive and adjudicator. Wachter, Mittelstadt and Floridi (2017, AM p. 46) proposed a "trusted third party" with access to the rationale of specific decisions. The paper's §4.4 and §5.4 restate these proposals; what is new is the triad (the intermediary that binds two parties, which SCHUFA para. 61 now recognises in law) and the historical record of the notary and second interpreter. I found no work that grounds a neutral-arbiter requirement in the history of scribes and notaries, in the sources searched for this facet (the works listed above, the CJEU and Dutch case law, and the web searches recorded here); M3 reported the same gap for "digital notary".

## Counts by read depth

| Depth | Count | Works |
| --- | --- | --- |
| Full | 1 | SCHUFA C-634/21 |
| Part | 24 | PWD 2024/2831; DSA 2022/2065; GDPR; AI Act 2024/1689; Omnibus 2026/1744; P2B 2019/1150; Dun & Bradstreet C-203/22; Elite Taxi C-434/15; Amsterdam CoA Uber (793) with Ola (804); Colorado SB 26-189; NYC DCWP rule (LL144); NY OSC 2024-N-6; Reg B §1002.9; CFPB Circular 2022-03 and withdrawal page; Cohen 2019 ch. 5; Wachter et al. 2017; Wachter et al. 2018; Kaminski 2019; Kaminski and Urban 2021; Citron 2008; Crawford and Schultz 2014; Veale et al. 2023; Appeals Centre Europe 2026; Edwards and Veale 2017 (M2's reading, not re-read) |
| Abstract | 4 | Adams-Prassl et al. 2023; Aloisi et al. 2025; Crootof et al. 2022; Ponce del Castillo 2025 |
| Record | 3 | Radin 2013; Kim 2013; Selbst and Powles 2017 |

32 works. 18 new keys in `N2_platform_law.bib` (the Ola ruling sits inside `amsterdam2023uber`); 14 reuse existing keys (upgraded depths in its `@comment` block). Not counted: *Williams v. Walker-Thomas* and *Hill v. Gateway*, which the manuscript already cites and I did not re-read.

**Could not open or verify:** the text of NYC Local Law 144 (amlegal 403); EUR-Lex pages (bot challenge, Publications Office used instead); SAGE (Adams-Prassl), OUP (Selbst and Powles), Kluwer (Aloisi), SSRN (Crootof; Ponce del Castillo); Radin and Kim (no open copy); the Colorado bill page by curl (read through the fetch tool); national PWD transposition status after July 2026; the reports that a federal court enjoined enforcement of SB 24-205 (search summaries only, not used); whether AI Act Art 86 applies before 2 December 2027; whether present-day ride-hail apps are information society services for DSA purposes.

## Recommendations

### Must engage (a referee would object otherwise)

1. **SCHUFA, C-634/21** — §2.1, after "A credit bureau's score stands between a borrower and a lender": the CJEU has held that where "three stakeholders are involved", the bureau's score is itself the decision (paras 61, 73). And §4.4, at "The General Data Protection Regulation gives a person subject to a solely automated decision the right to obtain human intervention": add that Art 22(1) is "a prohibition in principle" (para. 52).
2. **Dun & Bradstreet Austria, C-203/22** — §4.2, at "I do not dispute that such a right exists": the CJEU has since held that Art 15(1)(h) gives "a genuine right to an explanation" (para. 57). §5.4, at "a dispute must be decidable against that record by a body that can bind the operator": trade-secret material goes to "the competent supervisory authority or court" (para. 74), a partial precedent.
3. **Kaminski and Urban (2021)** — §4.4, at "The second is independence at the first instance": they reached the same conclusion for private-sector AI ("Neither our archetype contestation schemes nor Article 22 feature a neutral arbiter", p. 2039). The paper must cite them and say what the triad adds.
4. **Crawford and Schultz (2014)** — §4.4, at "The third is the separation of roles" (their designer/executive/adjudicator, p. 120), and §5.4, at "submit disputes to a party the operator does not control" (their "neutral data arbiter", p. 127).
5. **PWD Art 10(2) and 10(5), stated precisely** — §4.4, at "The checks listed above operate after the decision": correct this sentence; the Directive puts a human, protected from dismissal and empowered to override, at the decision.
6. **P2B Art 4 corrected; Art 3(2)–(3) added** — §4.4, at "a separate regulation requires a statement of reasons 'on a durable medium' before an account is restricted"; and §5.3, at "An envelope is therefore only as good as the constraint on changing it": P2B already ties rule changes to 15 days' notice on pain of nullity.
7. **US law: Colorado SB 26-189 and NYC LL144/DCWP rule** — §4.4, at "recent, regional": the checks are not only EU; LL144 is the one instrument with an independent party before use, and its rule says "Nothing in this subchapter requires an employer ... to provide an alternative selection process" (§5-304(a)), which belongs at §5.2 after "keep open a route to the same standing that does not pass through the intermediary's reading".

### Should engage

8. **Appeals Centre Europe (2026)** — §5.4, at "they lack the binding power (art. 21)": 72% default decisions because platforms withheld the content, and implementation largely unknown (p. 11).
9. **AI Act Art 13(1), with the Omnibus dates** — §4.1, at the record row, or §5.3: transparency is owed "to enable deployers to interpret a system's output", not to the person read; and §4.4: Annex III obligations apply from 2 December 2027.
10. **Elite Taxi, C-434/15** — §2.1, at "the ride-hail firm presents itself as the neutral matcher ... and is also the driver's contractual counterparty" (para. 39: "decisive influence"); §4.4 as a scope caveat for the DSA.
11. **Amsterdam Court of Appeal, Uber (2023)** — §4.1, at "all argue against a record they did not make and cannot inspect": the court shifted the burden because the information "lies largely within Uber's domain" (my translation).
12. **Citron (2008, pp. 1254, 1272)** — §4.4 or §5.2, after the human-on-the-second-track objection: automation bias makes "little meaningful difference" between mixed and automated systems.
13. **Colorado §6-1-1705(1)(c)** — Table 1 record row, "Where the comparison is weak" or the text after it: the person may correct her data but not "opinions, predictions, scores".
14. **Cohen (2019, ch. 5)** — §5.6, at "*The users consented*": consent reduced to "the ability to decline a transaction or employment relationship".
15. **Wachter, Mittelstadt and Floridi (2017)** — §5.3, at "A fuller account of a model's workings would be read by fewer people still": ex ante explanation "can logically address only system functionality" (AM p. 6); and §5.4 for the "trusted third party" (AM p. 46). Cite with the note that the CJEU has since departed from its reading.

### Optional

16. Veale, Silberman and Binns (2023) — §5.2, on the second objection ("the human on the second track may be no fairer"): review without a substantive standard; "human in the loop as a service".
17. Adams-Prassl et al. (2023) — §4.4, for the in/after/before/above-the-loop vocabulary.
18. Kaminski (2019) — §4.4, "in the absence of significant public or third-party oversight".
19. Aloisi, Potocka-Sionek and Ratti (2025) — §4.4, as the doctrinal commentary on the final PWD.
20. CFPB Circular 2022-03 and its withdrawal; Regulation B §1002.9(b)(2) — §4.4, to show a long-standing reasons rule and the fragility of its algorithmic extension.
21. Wachter, Mittelstadt and Russell (2018); Ponce del Castillo (2025); Crootof, Kaminski and Price (2022); Selbst and Powles (2017) — only if §4.2 engages the explanation debate in more detail.
22. Radin (2013) and Kim (2013) — §5.6; listed as optional only because they remain unread. A contracts referee will expect one of them, so the author should obtain a copy before submission.
