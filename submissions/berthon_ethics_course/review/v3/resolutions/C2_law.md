# Resolutions: group C2_law (law, contracts, platforms)

Checked 2026-10-14. `D` = `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/C2_law/` (this session's downloads).
`M2` = `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/audit5/M2/` (Official Journal texts already held: 32024L2831 = PWD, 32022R2065 = DSA, 32016R0679 = GDPR, 32019R1150 = P2B). Every quotation below was opened this session.

Markup in "proposed v3 text": `{+…+}` is text the lab drafted for insertion, and `[-…-]` is the author's text proposed for deletion. Everything else is the author's wording, unchanged.

Sources reached: EUR-Lex returned HTTP 202 (a bot challenge) on both the HTML and the PDF routes. The Publications Office Cellar (`publications.europa.eu/resource/celex/<CELEX>`, Accept: application/xhtml+xml) served the official OJ XHTML. That is how I got the CCD and the MCD. CourtListener's opinion pages and API need a login, so I took the reporter pagination from the Harvard Caselaw Access Project scans (`static.case.law`, inline `page-label` anchors). SEC EDGAR refused curl without a contact User-Agent. I read the 10-K through WebFetch instead and put no e-mail in any header.

---

## P1-004
- **row**: l. 13, "People now reach credit, work, and civic standing through algorithmic systems that read their behavior and commit binding decisions."
- **resolution**: cite-fixed. Credit and civic standing now have sources. Work is already carried by P1-028 and P1-029.
- **evidence**:
  - Civic standing (government systems): Citron 2008, p. 1252: "automated systems have become the primary decision makers. These systems often take human decision making out of the process of terminating individuals' Medicaid, food stamp, and other welfare benefits. … Voters are purged from the rolls without notice". `pdfs/M3/citron.txt:168-180`.
  - Credit (EU): Directive (EU) 2023/2225, recital 56: "AI systems used to evaluate the credit score or creditworthiness of natural persons should be classified as high-risk AI systems, since they determine those persons' access to financial resources or essential services". Art. 18(8) also assumes automated decisions: "Where the creditworthiness assessment involves the use of automated processing of personal data … the consumer has the right to request and obtain from the creditor human intervention". `D/32023L2225.txt:131, 665`.
  - Credit (US): Reg B, 12 C.F.R. § 1002.9(a)(2) requires that a notice of "adverse action" give "A statement of specific reasons for the action taken". This shows the decision binds, but the regulation does not mention algorithms. `pdfs/M3/regb.html`.
  - Caution: CFPB Circular 2022-03 says Reg B applies to "complex algorithms". It was **withdrawn on 12 May 2025** (`pdfs/N2_platform_law/us/cfpb_withdrawn.txt`). Do not cite it as current guidance.
- **proposed v3 text**: People now reach credit, work, and civic standing through algorithmic systems that read their behavior and commit binding decisions {+(Citron, 2008, p. 1252; Directive (EU) 2023/2225, recital 56)+}.
- **note**: Citron's examples are US public-benefits and voter-roll systems from the 2000s. "Read their behavior" is the paper's gloss. It fits credit scoring, and it fits benefits eligibility less well.

## P2-005
- **row**: l. 31, "the ride-hail firm … earns a commission on each match".
- **resolution**: narrower. Uber takes a variable "service fee" on most trips, and on some trips it takes none.
- **evidence**:
  - Uber, "Uber service fee" (US marketplace page, accessed 2026-10-14): "The service fee is the fee drivers pay Uber, and it varies from trip to trip. It's the difference between what a rider pays and what a driver earns on a trip". On the question "Does Uber charge drivers a service fee on every trip?" the page answers "No. If the rider payment is the same or less than the driver earnings, Uber does not receive a service fee." `D/uber_servicefee.txt`; https://www.uber.com/us/en/marketplace/pricing/service-fee/
  - *Uber BV v Aslam* [2021] UKSC 5, [11]: "Uber BV makes a weekly payment to the driver of sums paid by passengers … less a 'service fee' retained by Uber BV. In the cases of Mr Aslam and Mr Farrar, the service fee was 20% of the fares." `D/aslam.txt`; https://caselaw.nationalarchives.gov.uk/uksc/2021/5
  - Uber Form 10-K for FY2024 (Revenue Recognition), read through WebFetch: "We generate substantially all of our revenue from fees paid by Drivers and Merchants for use of our platform." https://www.sec.gov/Archives/edgar/data/1543151/000154315125000008/uber-20241231.htm
- **proposed v3 text**: … earns a commission on [-each-]{+most+} match{+es+} {+(*Uber BV v Aslam*, 2021, [11])+}, and is also …

## P2-006
- **row**: l. 31, "and is also the driver's contractual counterparty".
- **resolution**: supported, with a new legal source (cite-fixed).
- **evidence**:
  - *Uber BV v Aslam* [2021] UKSC 5, [52]: "The only written agreements to which drivers were parties were agreements with Uber BV, the Dutch parent company. No other Uber company was a party to those agreements."
  - Ibid. [43] gives the neutral-matcher self-presentation that the same sentence describes: "the only role of Uber BV is to provide technology services and to act as a payment collection agent for the driver and that the only role of Uber London … is to act as a booking agent for drivers."
  - The Court dismissed Uber's appeal ([139]). That upheld the finding that drivers worked "for Uber London" ([39]).
  - `D/aslam.txt`.
- **proposed v3 text**: … and is also the driver's contractual counterparty {+(*Uber BV v Aslam*, 2021, [52])+}.
- **note**: The case is English law and concerns the 2015 Services Agreement. Uber's 10-K (FY2024) says "In certain markets we are responsible for the Mobility or Delivery services" and elsewhere "We act as an agent". So the counterparty structure varies by market. I could not get Uber's current US driver agreement: the page renders by script and the static fetch returned no text.

## P2-007
- **row**: l. 31, "the law has historically treated the neutral third and the interested counterparty under different rules" (forward reference to §4).
- **resolution**: supported as the paper's synthesis of the §4 sources. No change is needed.
- **evidence**:
  - The neutral third: UINL, *Principles of notarial ethics*, §9: notaries "must balance the respective interests of the parties concerned and seek a solution with the sole objective of safeguarding both parties". `pdfs/M3/uinl_d96bfb.html`. UINL, *Principles of the notarial function*, Part I: "they are required to act both impartially and independently". `pdfs/M3/uinl_905bff.html`.
  - The interested counterparty: Kessler 1943, p. 632, terms "dictated by the stronger party" (see P5-033). *Hill*, 105 F.3d at 1148: "people who accept take the risk that the unread terms may in retrospect prove unwelcome."
- **proposed v3 text**: no change. The UINL texts are present-day statements of the notarial office, so "historically" rests on §3's history of the notary rather than on these cites.

## P4-071
- **row**: l. 145, "The intermediary's log is the only record of what passed between the two parties, and its determination is what binds them. … all argue against a record they did not make and cannot inspect."
- **resolution**: narrower. The log and its binding interpretation are documented. "The only record" is contradicted by the same source, because drivers keep their own logs and dash-cam footage. "Cannot inspect" is too strong where GDPR access rights apply.
- **evidence**:
  - Rosenblat & Stark 2016, p. 3765: "Uber claims that it has the data to adjudicate disputes between passengers and drivers … Its claim to adjudication is rooted in the notion that its data on both passengers and drivers are akin to an objective, third-party witness, and thus that its interpretation should be conclusive."
  - Same page: drivers "report having to gather their own data to prevent wages from being retracted" and "resist Uber's power of interpretation by tracking their trips with manual or electronic logs and dash-cams." `pdfs/v3_ledger/rosenblat2016stark.txt:383-417`.
  - PWD (2024/2831), recital 63: the relevant elements "could be in the possession of the digital labour platform and not easily accessible to persons performing platform work and competent authorities". `M2/32024L2831.txt:145`.
  - Against "cannot inspect": GDPR art. 15(1) gives a "right to obtain from the controller … access to the personal data" (`M2/32016R0679.txt`). PWD art. 9(6) gives a right to portability of work data.
  - PWD arts 9 and 11, which the ledger suggested, govern information about the systems and explanation and review of decisions. Neither gives access to the log, so neither supports this sentence.
- **proposed v3 text**: The intermediary's log is the [-only-]{+authoritative+} record of what passed between the two parties, and its determination is what binds them {+(Rosenblat & Stark, 2016, p. 3765)+}. A driver who disputes a fare, a rider who disputes a charge, and an applicant who asks why she was screened out all argue against a record they did not make and cannot {+readily+} inspect {+(Directive (EU) 2024/2831, recital 63)+}.

## P5-022
- **row**: l. 167, the *Williams v. Walker-Thomas* quotation.
- **resolution**: cite-fixed. The pin cite is **350 F.2d at 449**.
- **evidence**: Caselaw Access Project scan of 350 F.2d 445. The `*449` page label falls at "does not mean that | the common law …" and `*450` at "the terms of the | agreement". The sentence "Did each party to the contract, considering his obvious education or lack of it, have a reasonable opportunity to understand the terms of the contract …?" falls between them. `D/cap_walker.txt`; https://static.case.law/f2d/350/html/0445-01.html
- **proposed v3 text**: (*Williams v. Walker-Thomas Furniture Co.*, 1965{+, p. 449+}), or in legal style 350 F.2d 445, 449.

## P5-025
- **row**: l. 171, the two *Hill v. Gateway* quotations.
- **resolution**: cite-fixed. "A contract need not be read to be effective" is at **105 F.3d at 1148**. "Competent adults are bound by such documents, read or unread" is at **105 F.3d at 1149**.
- **evidence**: Caselaw Access Project scan of 105 F.3d 1147. Page labels: `*1149` falls at "one way a contract | could be formed", and `*1150` at "includes promises of | future performance". The first quotation comes before `*1149`, and the second comes between `*1149` and `*1150`. `D/cap_hill.txt`; https://static.case.law/f3d/105/html/1147-01.html
- **proposed v3 text**: (*Hill v. Gateway 2000, Inc.*, 1997{+, pp. 1148–1149+}).
- **note**: *Schnabel v. Trilegiant*, 697 F.3d at 125, pin-cites "Competent adults …" to 1150. The scan's inline page break puts the quotation on 1149, so use 1149.

## P5-023
- **row**: l. 167, "and courts and regulators stand behind all of these".
- **resolution**: supported. Each instrument names a court or regulator route. Adding cites is optional.
- **evidence**:
  - GDPR art. 77(1): "every data subject shall have the right to lodge a complaint with a supervisory authority". Art. 79(1): "each data subject shall have the right to an effective judicial remedy where he or she considers that his or her rights under this Regulation have been infringed". `M2/32016R0679.txt:1635-1647`.
  - PWD ch. V (Remedies and enforcement) runs to **arts 18–24**, not 18–21 as the ledger said:
    - Art. 18: "access to timely, effective and impartial dispute resolution and a right to redress".
    - Art. 21(1): "national courts or competent authorities are able to order the digital labour platform to disclose any relevant evidence".
    - Art. 24(1): GDPR supervisory authorities enforce arts 7–11.
    - Source: `M2/32024L2831.txt:376-409`.
  - DSA art. 21(1), 3rd subpara: the right "to initiate, at any stage, proceedings to contest those decisions … before a court". `M2/32022R2065.txt:656`.
  - P2B art. 14(1): representative actions "before competent national courts". Art. 14(9) keeps business users' own right of action. Art. 15(1): "Each Member State shall ensure adequate and effective enforcement". `M2/32019R1150.txt:314, 336, 337-339`.
- **proposed v3 text**: optionally, "… and courts and regulators stand behind all of these {+(e.g., Regulation (EU) 2016/679, arts. 77–79; Directive (EU) 2024/2831, arts. 18, 24)+}."

## P5-031
- **row**: l. 173, "A worker can reach a court".
- **resolution**: supported.
- **evidence**:
  - GDPR art. 79(1) (quoted under P5-023). Art. 79(2) adds that proceedings "may be brought before the courts of the Member State where the data subject has his or her habitual residence".
  - PWD art. 18, the right to redress, which applies "Without prejudice to Articles 79 and 82 of Regulation (EU) 2016/679".
  - DSA art. 21(1), 3rd subpara.
- **proposed v3 text**: no change. A cite is optional: {+(Regulation (EU) 2016/679, art. 79; Directive (EU) 2024/2831, art. 18)+}.

## P5-026
- **row**: l. 171, "The modern rule runs the other way" (then *Hill*).
- **resolution**: narrower. The duty-to-read rule is old and general. *Hill* is a modern application of it to terms that arrive after payment. Calling it "the modern rule" suggests that it replaced an earlier rule, and the record says the opposite.
- **evidence**:
  - *Upton v. Tribilcock*, 91 U.S. 45, 50 (1875): "It will not do for a man to enter into a contract, and, when called upon to respond to its obligations, to say that he did not read it when he signed it, or did not know what it contained." `D/cap_upton.txt`; https://static.case.law/us/91/html/0045-01.html
  - Restatement (Second) of Contracts § 211 cmt. b (1981), as quoted in *Schnabel v. Trilegiant Corp.*, 697 F.3d 110, 127 (2d Cir. 2012): "A party who makes regular use of a standardized form of agreement does not ordinarily expect his customers to understand or even read the standard terms." *Schnabel* names this the "'duty to read' rule" (p. 127). `D/cap_schnabel.txt`.
  - I did not open the Restatement itself. The ALI text is paywalled, so this quotation comes second-hand from the court.
- **proposed v3 text**: The [-modern-]{+settled+} rule runs the other way: "A contract need not be read to be effective," and "Competent adults are bound by such documents, read or unread" (*Hill v. Gateway 2000, Inc.*, 1997{+, pp. 1148–1149; see *Upton v. Tribilcock*, 1875, p. 50+}).

## P5-033
- **row**: l. 175, "The standard-form contract belongs to a different legal world, in which one party drafts and the other adheres."
- **resolution**: supported, and the citation is added (cite-fixed).
- **evidence**: Kessler 1943, p. 632: "Standard contracts are typically used by enterprises with strong bargaining power. … His contractual intention is but a subjection more or less voluntary to terms dictated by the stronger party, terms whose consequences are often understood only in a vague way, if at all. Thus, standardized contracts are frequently contracts of adhesion; they are à prendre ou à laisser." Full text from the Yale Law School repository (`D/kessler1943.pdf`; PDF pp. 1–14 = journal pp. 629–642, page 4 = p. 632). https://openyls.law.yale.edu/server/api/core/bitstreams/2c736339-fd4f-4008-8485-56131dd878ed/content
- **proposed v3 text**: … a different legal world, in which one party drafts and the other adheres {+(Kessler, 1943, p. 632)+}. Reference: add Kessler, F. (1943). Contracts of adhesion—Some thoughts about freedom of contract. *Columbia Law Review, 43*(5), 629–642. https://doi.org/10.2307/1117230

## P5-036
- **row**: l. 177, "no rule requires anyone to read, explain, and certify a person's understanding before she is bound".
- **resolution**: narrower. Read literally, the conjunction survives, because no instrument I found requires all three, and none requires certifying understanding. As a general claim about law it misleads. EU credit law requires a pre-contract **explanation**:
- **evidence**:
  - Consumer Credit Directive (EU) 2023/2225, art. 12(1) ("Adequate explanations"): "Member States shall ensure that creditors and, where applicable, credit intermediaries are required to provide adequate explanations to the consumer on the proposed credit agreements and any ancillary services that make it possible for the consumer to assess whether the proposed credit agreements and ancillary services are adapted to the consumer's needs and financial situation. Such explanations shall be provided free of charge and before concluding the credit agreement." Art. 48(1): Member States apply the measures "from 20 November 2026". `D/32023L2225.txt:569-570, 1107-1108` (OJ L, 2023/2225, 30.10.2023, via Cellar).
  - Mortgage Credit Directive 2014/17/EU, art. 16(1): "Member States shall ensure that creditors and, where applicable, credit intermediaries or appointed representatives provide adequate explanations to the consumer on the proposed credit agreements and any ancillary services, in order to place the consumer in a position enabling him to assess whether the proposed credit agreements and ancillary services are adapted to his needs and financial situation." Under art. 16(2), Member States "may adapt the manner by which and the extent to which the explanations … is given". `D/32014L0017.txt:503-519` (OJ L 60, 28.2.2014, p. 34).
  - Where a notarial deed is used, the notary's professed duty covers explaining: "they must inform and advise the parties as to the possible consequences of their instructions" (UINL, *Principles of notarial ethics*, §10, `pdfs/M3/uinl_d96bfb.html`). I did not verify which states require notarial authentication for which contracts.
- **proposed v3 text** (two options for the author):
  - (a) Scope it: "… and no rule requires anyone to read, explain, and certify a person's understanding before she is bound {+by an intermediary's terms+}."
  - (b) Acknowledge the exception: "… before she is bound{+; the nearest, in EU credit law, requires only 'adequate explanations' before signing (Directive 2014/17/EU, art. 16; Directive (EU) 2023/2225, art. 12)+}."
- **argument flag**: this narrows the paper's central negative claim, so it changes the argument and not only the wording. The author should rule on it.

## P5-043
- **row**: l. 185, "Contemporaries condemn the practice … drivers, the scholars who study them, and legislators".
- **resolution**: cite-fixed. The PWD recitals name the harm.
- **evidence**:
  - PWD recital 8: "Persons performing platform work subject to such algorithmic management often do not have access to information on how the algorithms work, which personal data are used or how the behaviour of those persons affects decisions taken by automated systems. … Moreover, persons performing platform work often do not know the reasons for decisions taken or supported by automated systems and are not able to obtain an explanation for those decisions, to discuss those decisions with a human contact person, to contest those decisions or to seek rectification or, where relevant, redress." `M2/32024L2831.txt:35`.
  - PWD recital 4: such technologies, "if unregulated, … can also result in technology-enabled surveillance, increase power imbalances and opacity about decision-making". `M2/32024L2831.txt:27`.
- **proposed v3 text**: (Rosenblat & Stark, 2016; Dubal, 2023; Muldoon & Raekstad, 2023{+; Directive (EU) 2024/2831, recitals 4, 8+}).
- **note**: the recitals describe a harm to be regulated. "Condemn" is the paper's verb for that.

## P6-020
- **row**: l. 225, Kolt quotes the Restatement; "the agent carries its user's interest and no duty to anyone else".
- **resolution**: narrower in the claim and cite-fixed in the reference.
- **evidence**:
  - Kolt, *Governing AI Agents*, 101 Notre Dame L. Rev. 335–386 (2026). The Notre Dame page proof (`D/kolt_101_335.pdf`, 52 pp.) runs pp. 335–386. The journal page gives the citation "101 Notre Dame L. Rev. 335 (2026)" and lists the article in Volume 101, Issue 1 (`D/nd_kolt.html`; https://ndlawreview.org/governing-ai-agents/).
  - p. 345 n. 28: "See RESTATEMENT (THIRD) OF AGENCY § 1.04 cmt. e (A.L.I. 2006) ('[A] computer program is not capable of acting as a principal or an agent as defined by the common law. At present, computer programs are instrumentalities of the persons who use them.')".
  - p. 362: agents "are also subject to an overarching 'fiduciary duty to act loyally for the principal's benefit …'".
  - I did not open the Restatement (ALI, paywalled). The quotation is Kolt's.
  - On the Restatement view a program owes no duty at all, including to its user. "Carries its user's interest" is the paper's gloss.
- **proposed v3 text**: "… the agent carries its user's interest and {+owes+} no duty to anyone{- else-}, and it is itself a new third party …". In-text: Kolt ([-2025-]{+2026+}, {+p. 345+}).
- **reference**: Kolt, N. ([-2025-]{+2026+}). Governing AI agents. *Notre Dame Law Review, 101*{+(1), 335–386+}. Changing the year is the author's decision. The SSRN and arXiv versions are dated 2024 and 2025.

## P6-023
- **row**: l. 225, "operators today invoke terms of service against tools that collect it" (the user-side record).
- **resolution**: cite-fixed (narrower). There is a documented instance. The tool read order data on the worker's side. It did not keep a long-term record.
- **evidence**: Fischels, J. (2021, July 31). Why DoorDash drivers are on strike. NPR: "Some Dashers solved this problem by downloading Para, a third-party app that used DoorDash's code to let drivers see the tip amount before accepting an order. … in mid-July, it no longer worked with DoorDash's app. … According to a statement from DoorDash, Para violated the company's terms of service. 'Para collects its information by scraping content without authorization from the DoorDash platform.'" `D/npr_doordash.txt`; https://www.npr.org/2021/07/31/1023265561/why-doordash-drivers-are-on-strike
- **proposed v3 text**: … operators today invoke terms of service against tools that collect it {+(Fischels, 2021)+}—…
- **note**: UberCheats was a closer fit: a 2021 Chrome extension that checked Uber's paid mileage against Google Maps. Uber had it removed on a **trademark** complaint under Lanham Act § 32, not on terms of service (Gault, Vice, 18 Feb 2021, https://vice.com/en/article/uber-shuts-down-app-that-lets-users-know-how-badly-theyve-been-cheated, read through WebFetch). If the author wants that case, the verb should be "invoke trademark and terms of service". Instacart's 2020 removal of batch-grabbing bots involved bots, not record tools, so it does not fit.

## P6-017
- **row**: l. 223, "Citron (2008) argued that automated decision systems owe their subjects audit trails."
- **resolution**: narrower. Citron's setting is government.
- **evidence**:
  - Citron 2008, p. 1252: "The twenty-first century's automated decision-making systems bring radical change to the administrative state".
  - p. 1305, under "Protecting Individual Rights" (due process): "At a minimum, automated systems should generate audit trails that record the facts and rules supporting their decisions."
  - `pdfs/M3/citron.txt:168-170, 3088-3101`.
- **proposed v3 text**: Citron (2008) argued that {+government+} automated decision systems owe their subjects audit trails.

---

## EU article numbers in the P5 rows (verification)

All of these were read in the Official Journal texts in `M2`.

| Instrument | Article as cited | Verified text | Verdict |
|---|---|---|---|
| PWD 2024/2831 | art. 9 (P4-071; P6-011 at l. 215, art. 9(1)(b)) | Art. 9 "Transparency with regard to automated monitoring systems and automated decision-making systems". The quoted words are art. **9(1)(b)(iii)**. | correct. Pin to 9(1)(b)(iii). Art. 9 does not support P4-071. |
| PWD | art. 10 (l. 167, human decision) | Art. 10 "Human oversight …". **10(5)**: "Any decision to restrict, suspend or terminate the contractual relationship or the account … shall be taken by a human being." | correct. Pin 10(5). |
| PWD | art. 11 (l. 167, reasons and review) | Art. 11 "Human review". 11(1) 2nd subpara: written statement of reasons. 11(2): review by "the digital labour platform", reply "within two weeks". 11(5) excludes P2B business users. | correct |
| PWD | ch. V | Arts **18–24** (redress, representation, communication channels, evidence, adverse treatment, dismissal, supervision and penalties) | the ledger's "arts 18–21" is incomplete |
| DSA 2022/2065 | art. 17 | "Statement of reasons", owed by providers of **hosting services** for restrictions on grounds of illegal content or incompatibility with T&Cs (17(1)) | correct. The manuscript does not cite art. 17. |
| DSA | art. 20(6) (l. 167) | "taken under the supervision of appropriately qualified staff, and not solely on the basis of automated means" | correct and verbatim. The art. 20(1) scope is content and T&C decisions, including account suspension (20(1)(c)). |
| DSA | art. 21 (ll. 173, 225) | The no-binding-settlement sentence is **21(2), 3rd subpara**. The court-access sentence is 21(1), 3rd subpara. | correct. Pin 21(2). |
| GDPR 2016/679 | art. 22(3) (l. 167) | "In the cases referred to in points (a) and (c) of paragraph 2, … at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision." | the number is correct. The claim is narrower (P5-019): 22(3) applies only to the contract and explicit-consent exceptions. |
| P2B 2019/1150 | art. 4 (l. 167) | 4(1): statement of reasons "prior to or at the time of the restriction or suspension taking effect … on a durable medium" for restriction "in relation to individual goods or services". 4(2): at least 30 days before a **termination**. | the number is correct. "before an account is restricted" is narrower (P5-020). |

Two related instruments for the author's note on l. 167: CCD 2023/2225 art. 18(8) gives a right to human intervention, an explanation, and a review of automated creditworthiness assessments, applying from 20 Nov 2026. CCD art. 13 requires telling the consumer about personalised offers "based on automated processing of personal data" (`D/32023L2225.txt`).

## Blocked or partly read
- None blocked outright.
- Read only second-hand (paywalled ALI texts): Restatement (Second) of Contracts § 211 cmt. b, via *Schnabel* at 127, and Restatement (Third) of Agency § 1.04 cmt. e, via Kolt p. 345 n. 28. If the author wants direct cites, the author must supply the ALI text of § 211 (with comment b) and § 1.04 (with comment e).
- Uber's current US driver agreement text was not obtained: uber.com/legal renders by script. If P2-006 should rest on US terms rather than *Aslam*, the author must supply the driver agreement PDF (Platform Access Agreement, the party clause).
- Uber Form 10-K FY2024 was read only through WebFetch, because SEC blocks clients that do not declare a contact User-Agent.
