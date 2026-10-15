# M3 — The third party who writes, and the record that binds

*Facet M3, 2026-10-13. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

**What this facet covers.** The paper's §3.3 (record over voice), §5.3 (safeguards around human scribes against platforms) and §6.4 (counter-delegation as the modern notary and second interpreter). I looked in six places: lettered intermediaries as a class; files and registers as power; the law of signing what you cannot read; the duties of the modern intermediary; the triad in social theory; and what a legal historian or sociologist of documents would say the outline gets wrong.

**The question the synthesis answers.** Does the literature support the outline's claim that the safeguards that restrained human scribes "have no settled counterpart" for platforms, and what does it add or cut?

**Legend for read status.** *Text opened* = I downloaded or fetched the text this session and searched it, then read the passages cited. I did not read any long work end to end, so I use no "read in full" mark. The pages I read are named. *Abstract only* = a Crossref abstract or publisher description; I paraphrase and quote only what that abstract says. *Record only* = I verified the work exists (Crossref, archive.org metadata or a publisher page) and opened nothing. *Blocked* = a bot wall or login stopped me and I stopped. Page locators are the printed pages of the source where the text carried them; "PDF p." means a PDF page where it did not. A "Claude's reading" tag marks what I infer, not what the source says.

**Rules honoured.** Anonymous requests only. No e-mail address in any request, and none copied into these files. No Unpaywall. No git. No Chrome. No bot wall bypassed. All downloads are in `~/iit-playground/berthon_ethics_local/pdfs/M3/` and were only text-extracted.

**Read this first: three things the facet changes.**

1. The only present-day appellate holding I opened on the non-reading signer (*Hill v. Gateway 2000*) goes against the paper's premise that reading-before-binding is the missing safeguard. The court did not consider a rule that a third party read the contract to the signer; it said of a seller's staff reciting terms to buyers by telephone that "the droning voice would anesthetize rather than enlighten many potential buyers", and that vendors do better to "skip costly and ineffectual steps such as telephonic recitation".
2. The paper treats the platform as a third party who binds two people, but the doctrines that govern unread terms (adhesion, wrap, unconscionability) concern a *counterparty who drafts*. §5.3 needs to say which role it means.
3. The civil-law notary's duty is written down, by the profession's own union, as a duty to both parties and to the weaker one (UINL, notarial ethics 2004, principle 9: "both parties"; notarial function 2005, Part I: "inferiority"). Neither Balkin's information fiduciary nor Khan and Pozen's critique reaches a duty to two principals. That gap is the paper's strongest ground in §6.4, and no source in the outline states it.

---

## (a) Search log

OpenAlex returned "Insufficient budget … daily budget … used up" (HTTP 429) on the first batch, so I used Crossref, archive.org, publishers' pages and WebSearch. SSRN, Justia, BAILII, eScholarship, Taylor & Francis, CanLII, the SCC site and JSTOR all returned bot walls or login pages. I stopped at each. Scholar Gateway: not tried.

| # | Source | Query | Result |
|---|---|---|---|
| 1 | Crossref | Balkin, Khan–Pozen, Viljoen, Gillespie, Kessler, Rakoff, Bakos, Obar, Stovel–Shaw, Obstfeld, Burt, Ben-Shahar (title+author) | DOIs found for all but Balkin and Khan–Pozen (law-review articles with no Crossref record) |
| 2 | WebSearch | Balkin, "Information Fiduciaries and the First Amendment" UC Davis | citation 49 U.C. Davis L. Rev. 1183 (2016); a Yale repository PDF; opened |
| 3 | WebSearch | Khan Pozen "A Skeptical View of Information Fiduciaries" | 133 Harv. L. Rev. 497 (2019); Columbia repository page says "withdrawn"; HLR print page has the PDF link; the PDF is the full 45-page article |
| 4 | WebSearch | Viljoen "A Relational Theory of Data Governance" | Yale Law Journal 131:573, official PDF opened |
| 5 | curl | SSRN Delivery.cfm (Bakos, Obar, Ben-Shahar) | bot wall, stopped |
| 6 | WebSearch | Bakos et al. | NYU archive copy of the 2009 working paper; opened |
| 7 | WebSearch | Ben-Shahar and Schneider | a think-tank copy of the 2011 article; opened (font-encoded, decoded; see entry) |
| 8 | WebSearch | Obar and Oeldorf-Hirsch | no open copy; T&F returned a bot wall |
| 9 | curl | Justia (Specht, Nguyen, Meyer, Walker-Thomas), BAILII (*L'Estrange*), law.resource.org | bot walls or 404; stopped |
| 10 | WebSearch | Hill v. Gateway text | Harvard Cyberlaw copy opened |
| 11 | WebSearch | Walker-Thomas, Specht text | UVM copy (full) and Michigan 7-page excerpt opened |
| 12 | WebSearch | "non est factum" with click-wrap, electronic signature | **no decision found applying the plea to a click-through**; only general commentary |
| 13 | WebSearch | Messick, *Calligraphic State* | UC Press E-Books Collection archive carries the full text; opened |
| 14 | WebSearch | Justice, *Writing and Rebellion* | library records only; no open text |
| 15 | WebSearch | Hull, *Government of Paper* | commercial listings only; no open text |
| 16 | curl | archive.org advancedsearch (Rama, Goody, Scott, Hull, Kafka, Radin, Kim, Wolff's Simmel, Bowker–Star, Gitelman, Salomon, Weber) | Scott, Weber (Gerth–Mills), Simmel (Wolff) open text; the rest are lending copies behind login |
| 17 | WebSearch | Rama *La ciudad letrada* | secondary pages only; the eScholarship article (Gorman Malone 2010) returned a bot wall |
| 18 | WebSearch | Kalman, *Writing on the Plaza* | tourism pages only; the Crossref record is a review (Kamberelis 2001) |
| 19 | WebSearch | notary impartiality, UINL | two UINL pages opened |
| 20 | WebSearch / curl | Kolt, Gal and Elkin-Koren | arXiv and JOLT PDFs opened |
| 21 | WebSearch | Citron, "Technological Due Process" | WashU journal PDF opened |
| 22 | curl | legislation.gov.uk (CRA 2015 ss. 62, 68), eCFR (12 CFR 1002.9) | official text opened |
| 23 | WebSearch | Stovel and Shaw; Simmel "The Triad" | Crossref abstract for Stovel–Shaw; Wolff's Simmel via archive.org |
| 24 | WebSearch | platforms as brokers / tertius gaudens | no work found that applies the tertius gaudens to a platform (see Q5) |
| 25 | WebSearch | Radin *Boilerplate*; Kim *Wrap Contracts* | publisher and catalogue descriptions; one Radin working-paper abstract |
| 26 | WebSearch | Vismann *Files*; Kafka *Demon of Writing* | publisher-style descriptions only |
| 27 | WebSearch | UETA error provisions for electronic agents | Penn archive page did not carry the Act's text; not verified |
| 28 | WebSearch | *Uber v. Heller* 2020 SCC 16 | commentaries only; SCC and CanLII blocked; not verified at source |

---

## (b) Entries

Bib keys are in `M3_intermediaries_records.bib`.

### Group 1. Lettered intermediaries as a class

**Messick, *The Calligraphic State* (1993)** — `messick1993calligraphic`. Crossref DOI 10.1525/9780520917828 (title "Calligraphic State", UC Press, 1993). The UC Press E-Books Collection Archive carries the whole book at publishing.cdlib.org. **Text opened**, about 132,000 words, searched by keyword. I read the introduction, the section "The Chastity of Documents" (the ebook's inline page markers put it at pp. 209–210) and the passages on witnesses, notaries and scribes. Scale: one Muslim polity (highland Yemen), late nineteenth century to the 1970s.
- Introduction: "As understood here, the calligraphic state was both a political entity and a discursive condition." And: "Textual domination, in this analysis, entails the interlocking of a polity, a social order, and a discursive formation."
- On the court's evidence rules: "the manuals discuss witnessing support for documents, but they do not consider documents to be potential evidence." The same section says "an oral core is complemented by a written surround": the doctrine centres on oral testimony, while the court "in actuality relied heavily on the services of the written word."
- On the notary's origin: the "reliable witness" institution "evolved into the certified notary of the Malikis"; "an 'adil was a notary." A verifying witness is "a further intervening link in the human transmission of evidence."
- On scribes as a paid class: a prominent Ibb notary "began a lucrative parallel career writing legal instruments"; a mufti "acts as a notary (katib) who prepares written legal instruments."
- Bearing. **§3.3: complicates.** Record over voice is a choice a legal regime makes, not a property of writing. Classical shari'a evidence law did the reverse: the document is only worth the witnesses who attest to it. This is a worked alternative to the outline's mechanism, and it shows the notary as a witness-institution whose reliability is certified by character testimony. **§6.4: supports as a design precedent** (a chain of attesting witnesses around a written record). A historian of law would expect the paper to know that giving the document priority over the witness is not the only arrangement writing has produced. Messick also warns that the doctrine of oral primacy coexisted with heavy reliance on paper in practice, so I would not present the shari'a rule as a safeguard that worked. Referee would expect it: a Middle East legal historian, yes; a management referee, no.

**Rama, *La ciudad letrada* (1984; English 1996)** — `rama1996lettered`. archive.org record `letteredcity0000rama` confirms the 1996 English edition (Duke); it is a lending copy. No Crossref record found. **Not accessible (record only; secondary summaries seen in search results, none quoted).** The summaries I saw say Rama's thesis is that a cadre of *letrados* tied writing to the colonial state and reproduced the social order through an urban culture of the pen, from the colony to the mid-twentieth century. They also say later scholars faulted it for a one-directional view of writing and power and for ignoring Indigenous, mestizo and Afro-descendant literacies. I could not confirm either from the book. The summaries did not mention *escribanos*, so I cannot tell the paper what Rama says about notaries. Bearing: **§2.5 and §3.3, class-level frame; supports in outline, complicated by critics.** A Latin Americanist referee would expect Rama cited for "the written word as an instrument of rule." The paper should cite it from a library copy, not from this facet.

**Rappaport and Cummins, *Beyond the Lettered City* (2012)** — `rappaport2012beyond`. Crossref DOI 10.1215/9780822394754. **Record only** (three reviews found: Allen 2014, Ramírez 2014, Durston 2016, all unopened). The title and the reviews' framing place it as an answer to Rama on Indigenous literacies in the Andes. Bearing: **§3.3, probably complicates**; it is the book a Rama critic would reach for. Not read.

**Salomon and Niño-Murcia, *The Lettered Mountain* (2011)** — `salomon2011lettered`. Crossref DOI 10.1215/9780822394341; archive.org record `letteredmountain0000salo` (lending). **Record only.** The title says it concerns a Peruvian village's way with writing; two reviews exist (Hanz 2012, Leifsen 2013). I did not open them and cannot say what the book argues. Bearing: possibly **§6.4**, as a case of a community keeping its own record. Unverified.

**Justice, *Writing and Rebellion: England in 1381* (1994)** — `justice1994writing`. Crossref DOI 10.1525/9780520918405. **Record only.** A library record says the book centres on six short texts the rebels wrote; I did not see the book. Not used for any claim here. Bearing: **§3.3**, if the author wants the rebels who both burned records and made them.

**Kalman, *Writing on the Plaza* (Hampton Press)** — `kamberelis2001writing` (the only Crossref record I found is a review). Review DOI 10.1016/s0898-5898(01)00049-3, "Writing on the Plaza: Mediated Literacy Practices Among Scribes and Clients in Mexico", Kamberelis 2001, *Linguistics and Education* 12: 233–237. **Record only** (review title). The book's title establishes the topic: scribes and clients in Mexico City. I opened neither the review nor the book.

**Papen and Thériault (2016), "Youth Workers as Literacy Mediators"** — `papen2016youth`. Crossref DOI 10.1002/jaal.545, *Journal of Adolescent & Adult Literacy*. **Record only.** The title shows that "literacy mediator" is in use for someone who helps another deal with institutional documents. I did not find Baynham's 1993 chapter in Crossref.

### Group 2. Files, registers, paperwork

**Weber, "Bureaucracy", in Gerth and Mills, *From Max Weber* (1946)** — `weber1946bureaucracy`. archive.org item `frommaxweberessa00webe` (no lending restriction); OCR text opened. Scale: the ideal type of modern administration.
- p. 197 (item III of the characteristics): "The management of the modern office is based upon written documents ('the files'), which are preserved in their original or draught form. There is, therefore, a staff of subaltern officials and scribes of all sorts."
- p. 214: "Precision, speed, unambiguity, knowledge of the files, continuity, discretion, unity, strict subordination, reduction of friction and of material and personal costs — these are raised to the optimum point in the strictly bureaucratic administration."
- Bearing. **§3.3 and §4 "The Record": background; neither supports nor cuts.** Weber treats the file as a source of technical superiority and gives the scribe a place in the office, but says nothing in these pages about a record overriding a person's own account. The OCR is noisy; the quotes above are tidied only where the OCR dropped letters, and a page check against a clean copy is needed.

**Scott, *Seeing Like a State* (1998)** — `scott1998seeing`. Crossref DOI 10.12987/9780300128789 (Yale, 2017 reissue record). archive.org item `seeing-like-a-state`; OCR text opened and searched (introduction; the opening of Part 3).
- Introduction: state simplifications are "rather like abridged maps. They did not successfully represent the actual activity of the society they depicted, nor were they intended to." And: "a state cadastral map created to designate taxable property-holders does not merely describe a system of land tenure; it creates such a system through its ability to give its categories the force of law."
- Part 3, opening: "Legibility is a condition of manipulation."
- Bearing. **§3.3: supports the record-creates-reality point, but the frame conflicts with the author's ruling.** The author has ruled that algorithmacy is "not legibility". Scott's engine is the state making a population legible by simplification. The paper's record binds *two parties* through a third who reads both. If the paper cites Scott, it should cite him for the single point that a record "creates" the tenure it describes and say in a sentence why the legibility frame is not adopted. A referee in the sociology of the state would expect Scott in any discussion of records; the absence needs a stated reason. Page numbers: the OCR gave none I trust; locate by section.

**Vismann, *Files: Law and Media Technology* (2008)** — `vismann2008files`. Stanford University Press; German original *Akten* (2000). I found no Crossref record for the 2008 English edition. **Abstract only** (publisher-style description via search). The description opens with the maxim *Quod non est in actis, non est in mundo* ("What is not on file is not in the world") and says that, from a media-theoretical point of view, "subject, state, and law" appear as effects of record-keeping and filing practices. I could not check the maxim's place in the book. Bearing: **§3.3, §4**: a maxim that states record-over-voice in Latin, if the book bears it out.

**Kafka, *The Demon of Writing* (2012)** — `kafka2012demon`. Crossref DOI 10.2307/j.ctv14gpj6p. **Abstract only** (publisher and review descriptions). It treats paperwork as a medium that states depend on and that fails unpredictably. Bearing: **§3.3**, on the unreliability of the record, which cuts against treating the record as simply dominant. Not read.

**Hull, *Government of Paper* (2012)** — `hull2012government`. Crossref DOI 10.1525/9780520951884 (resolves to "Government of Paper", UC Press, 2012). **Record only**; no open text. I do not describe the book's argument. Bearing: **§3.3, §4**, a study of a paper-run bureaucracy; the author or a library should read it before it is cited.

**Gitelman, *Paper Knowledge* (2014)** — `gitelman2014paper`. Crossref DOI 10.1215/9780822376767. **Record only.**

**Bowker and Star, *Sorting Things Out* (1999)** — `bowker1999sorting`. Crossref DOI 10.7551/mitpress/6352.001.0001. **Record only.**

**Goody, *The Logic of Writing and the Organization of Society* (1986)** — `goody1986logic`. Crossref DOI 10.1017/cbo9780511621598. Cambridge Core page opened. **Abstract only.** The publisher says the book assesses the impact of writing on societies in the ancient Near East and twentieth-century Africa and explores "the introduction of writing and the development of a written tradition" as a mechanism for social difference. I found nothing on records overriding a person's account. Bearing: **§2.2, background.**

**Smith, "'K is Mentally Ill': the Anatomy of a Factual Account" (1978)** — `smith1978mentally`. Crossref DOI 10.1177/003803857801200103, *Sociology* 12(1): 23–53. **Abstract only.** The abstract says the text "is found to provide instructions for its interpretation and for the authorization of its facticity." Bearing: **§3.3, a lead.** This is a sociology-of-documents account of how a record becomes the authorised version of a person. A sociologist of documents would expect the outline to know this literature. Not read.

**Riles (ed.), *Documents: Artifacts of Modern Knowledge* (2006)** — `riles2006documents`. Crossref DOI 10.3998/mpub.185485. **Record only.**

### Group 3. Signing what you cannot read

**Hill v. Gateway 2000, Inc., 105 F.3d 1147 (7th Cir. 1997)** — `hill1997gateway`. Harvard Cyberlaw copy of the opinion (cyber.harvard.edu/ilaw/Contract/hill.htm). **Text opened**, the opening and reasoning (the copy shows no reporter pagination, so I give none). Easterbrook J. Scale: a national appellate court, still widely cited for terms that arrive after payment.
- "A contract need not be read to be effective; people who accept take the risk that the unread terms may in retrospect prove unwelcome."
- On a read-aloud rule: "If the staff at the other end of the phone for direct-sales operations such as Gateway's had to read the four-page statement of terms before taking the buyer's credit card number, the droning voice would anesthetize rather than enlighten many potential buyers."
- "Competent adults are bound by such documents, read or unread."
- Bearing. **§5.3: cuts against.** The paper says the old safeguards (reading the instrument aloud before witnesses) have no counterpart. This court looked at a neighbouring step, a seller's staff reading the terms aloud to a buyer, and called such recitation "costly and ineffectual" for mass sales, in passing, in support of an approve-or-return device. The buyers could read and the reader would have been the counterparty, so the opinion does not address a neutral third party reading to a signer who cannot read. It also states the duty-to-read rule for "competent adults", which is the line *non est factum* never crossed. The paper must concede that a court has said, in passing, that oral recitation of terms by the seller is ineffectual for mass sales, and must say what its alternative does that reading aloud did not.

**Williams v. Walker-Thomas Furniture Co., 350 F.2d 445 (D.C. Cir. 1965)** — `williams1965walker`. University of Vermont copy of the opinion (121 U.S. App. D.C. 315). **Text opened**, the holding and the unconscionability passage. Skelly Wright J.
- "we hold that where the element of unconscionability is present at the time a contract is made, the contract should not be enforced."
- "Unconscionability has generally been recognized to include an absence of meaningful choice on the part of one of the parties together with contract terms which are unreasonably favorable to the other party."
- "Did each party to the contract, considering his obvious education or lack of it, have a reasonable opportunity to understand the terms of the contract, or were the important terms hidden in a maze of fine print and minimized by deceptive sales practices?"
- "Ordinarily, one who signs an agreement without full knowledge of its terms might be held to assume the risk that he has entered a one-sided bargain. But when a party of little bargaining power, and hence little real choice, signs a commercially unreasonable contract with little or no knowledge of its terms, it is hardly likely that his consent, or even an objective manifestation of his consent, was ever given to all the terms."
- Bearing. **§5.3: complicates the claim of no counterpart.** The test asks about the signer's "education or lack of it", so the person who cannot read the terms is inside the doctrine's own wording. That is the nearest present-day relative of the protection the illiterate signer once had. It is also a substantive fairness test, not a procedural duty on the writer. Facts: an installment-sale case in the District of Columbia, relying on a Uniform Commercial Code provision the court found persuasive.

**Specht v. Netscape Communications Corp., 306 F.3d 17 (2d Cir. 2002)** — `specht2002netscape`. University of Michigan seven-page excerpt (websites.umich.edu), Sotomayor J., with the Westlaw summary and the opinion's reasoning. **Text opened (excerpt).**
- (306 F.3d at 32) "When products are 'free' and users are invited to download them in the absence of reasonably conspicuous notice that they are about to bind themselves to contract terms, the transactional circumstances cannot be fully analogized to those in the paper world of arm's-length bargaining."
- The opinion quotes California law (306 F.3d at 30): "an offeree, regardless of apparent manifestation of his consent, is not bound by inconspicuous contractual provisions of which he is unaware, contained in a document whose contractual nature is not obvious."
- Bearing. **§5.3: complicates.** This is a protection for the person who clicks, but it attaches to *notice and assent*, not to the user's inability to read. It protects the user who never saw the terms and does nothing for the user who saw and did not read. *Hill* and *Specht* sit side by side in the same body of law. I did not read *Nguyen v. Barnes & Noble* (9th Cir. 2014) or *Meyer v. Uber* (2d Cir. 2017); the sites that carry them were walled.

**Bakos, Marotta-Wurgler and Trossen, "Does Anyone Read the Fine Print?" (2009 working paper; 2014)** — `bakos2009does`, `bakos2014does`. JLS 43(1): 1–35, DOI 10.1086/674424 (Crossref). I opened the NYU archive copy of the 2009 working paper (NET Institute #09-04), not the published article. **Text opened (working paper), abstract and introduction.**
- Abstract: "We find that only one or two out of every thousand retail software shoppers chooses to access the license agreement, and those that do spend too little time, on average, to have read more than a small portion of the license text."
- Introduction: "only about 0.1 or 0.2 percent access a product's EULA for at least one second."
- Scale: 45,091 households and 66 online software companies in the working paper. The published JLS abstract (OpenAlex record for DOI 10.1086/674424) gives 48,154 monthly visitors to the sites of 90 online software companies and says "only one or two of every 1,000 retail software shoppers access the license agreement". The "0.1 or 0.2 percent" sentence is from the 2009 working paper; I could not open the JLS full text, so cite that figure to the working paper and the "one or two in 1,000" wording to the JLS version.
- Bearing. **§5.3: cuts against the read-aloud remedy; supports the outline's claim that disclosure does not restructure power.**

**Ben-Shahar and Schneider, "The Failure of Mandated Disclosure" (2011)** — `benshahar2011failure`. 159 U. Pa. L. Rev. 647. Crossref has the SSRN record (10.2139/ssrn.1567284) and the book version (10.23943/princeton/9780691161709.003.0003). I opened an Institute for Free Speech copy of the 2011 article. Its text layer is font-encoded; I decoded it by matching the abstract to a known alphabet shift, which gave a clean abstract, and I read the decoded passages below. A few digits are misrendered (for example "2ð11" for 2011). **Text opened (decoded), read in part.**
- Abstract (p. 647): the Article surveys "the failure of the mandated disclosure regime in informing people and in improving their decisions" and argues that mandated disclosure "not only fails to achieve its stated goal but also leads to unintended consequences that often harm the very people it intends to serve."
- p. 731: "If nobody reads disclosures, it does not matter that some nonreaders are sophisticated."
- p. 672 (quoting Marotta-Wurgler): "No matter how prominently [end-user license agreements] are disclosed, they are almost always ignored."
- Bearing. **§6.3, §5.3: cuts against, and the paper must answer it.** The "declared operating envelope" is, on its face, a disclosure mandate. The paper's own premise is that disclosure rarely restructures power; Ben-Shahar and Schneider supply the evidence for that premise and then aim it at §6.3. *Claude's reading:* the answer is that an envelope is a commitment that limits the operator, not a notice the user must process; the paper has to say so.

**Obar and Oeldorf-Hirsch, "The biggest lie on the Internet" (2018/2020)** — `obar2018biggest`. Crossref DOI 10.1080/1369118x.2018.1486870, *Information, Communication & Society* 23(1): 128–147 (online 2018). **Record only; blocked.** T&F returned a bot wall; Crossref carries no abstract. I did not see the paper, so I cannot report its finding. Referee would expect it next to Bakos et al.

**Kessler, "Contracts of Adhesion — Some Thoughts about Freedom of Contract" (1943)** — `kessler1943contracts`. Crossref DOI 10.2307/1117230, 43 Colum. L. Rev. 629. **Record only; JSTOR login.** **Rakoff, "Contracts of Adhesion: An Essay in Reconstruction" (1983)** — `rakoff1983contracts`. Crossref DOI 10.2307/1341009, 96 Harv. L. Rev. 1173. **Record only.** Neither opened; the paper should cite them from a library copy.

**Radin, *Boilerplate* (2013)** — `radin2013boilerplate`. Crossref DOIs 10.1515/9781400844838 and 10.23943/princeton/9780691155333.001.0001. **Record only.** Catalogue descriptions say Part I has chapters titled "Normative Degradation" and "Democratic Degradation"; I did not open the book. Her 2016 working paper, "Access to Justice and Abuses of Contract" (`radin2016access`, Michigan repository 355), I read **at abstract level only**: "Mass-market boilerplate impacts access to justice when it deletes rights to redress of grievances." It says such deletion "leads to normative degradation because it undermines agreement, the basis of justifiable contractual enforcement, and it leads to democratic degradation because it undermines the basis of civil society and the Rule of Law." Bearing: **§3.3 and §5.3**; the "democratic degradation" idea (private firms replacing public law) fits the paper's argument about who holds the record. A contracts referee would expect it.

**Kim, *Wrap Contracts* (2013)** — `kim2013wrap`. Crossref DOI 10.1093/acprof:oso/9780199336975.001.0001. **Record only; publisher blurbs.** The blurbs say courts impose a duty to read on consumers but no duty on businesses to make contracts easy to read, and that Kim proposes a duty to draft reasonably and specific assent. I did not open it.

**Consumer Rights Act 2015 (UK), ss. 62 and 68** — `cra2015`. legislation.gov.uk text opened. **Text opened, primary source.** s. 62(1): "An unfair term of a consumer contract is not binding on the consumer." s. 62(4): a term is unfair "if, contrary to the requirement of good faith, it causes a significant imbalance in the parties' rights and obligations under the contract to the detriment of the consumer." s. 68(1)–(2): a trader "must ensure that a written term of a consumer contract, or a consumer notice in writing, is transparent", and a notice is transparent "if it is expressed in plain and intelligible language and it is legible." Bearing: **§5.3, complicates.** A statute makes unfair standard terms non-binding without asking whether the consumer read them. It governs the counterparty-drafter, not a neutral third party. Jurisdiction differs from the paper's Anglo-American historical scope only by being current law.

**12 C.F.R. § 1002.9(a)(2) (Regulation B)** — `regb2026`. eCFR text opened (current). **Text opened, primary source.** A notice of adverse action "shall be in writing" and must contain "either: (i) A statement of specific reasons for the action taken; or (ii) A disclosure of the applicant's right to a statement of specific reasons within 30 days." Bearing: **§3.3, §5.3, §6.4.** In consumer credit there is already a duty to put reasons into the record for the person refused. I opened only the beginning of the section and did not check how courts or the CFPB treat reasons from machine-learning models.

### Group 4. Duties of the modern intermediary

**Balkin, "Information Fiduciaries and the First Amendment" (2016)** — `balkin2016information`. 49 U.C. Davis L. Rev. 1183. Verified at the review's archive page; I opened the Yale repository copy of the PDF. **Text opened, read in part** (introduction, Part III, Part VIII).
- p. 1209: "An information fiduciary is a person or business who, because of their relationship with another, has taken on special duties with respect to the information they obtain in the course of the relationship."
- p. 1232: "The analysis I have just offered does not change if a company uses algorithms or artificial intelligence agents to harm or otherwise abuse the trust of its end-users."
- p. 1233: the duty runs to users; where algorithms "use data about other people" and "users have no relationship of trust or confidence with the enterprise," "we can no longer rely on the notion of special fiduciary relationships between individuals and companies."
- Bearing. **§6.1, §6.4: supports the duty-of-the-intermediary frame, and exposes a gap.** Balkin's fiduciary owes duties to its *end-users*, one relationship at a time. Nothing in the pages I read treats an intermediary that owes duties to two parties who coordinate through it. A referee in law and technology would expect Balkin cited here.

**Khan and Pozen, "A Skeptical View of Information Fiduciaries" (2019)** — `khan2019skeptical`. 133 Harv. L. Rev. 497. The Harvard Law Review PDF at the cited URL is the full 45-page article (pp. 497-541); I read pp. 498 and 502-504 and did not read Parts II-V. **Text opened, read in part.** The Columbia repository entry I saw said the paper was withdrawn.
- p. 498: the argument had "garnered remarkably broad support and essentially zero critical pushback"; the authors fear it "invites an enervating complacency about issues of structural power and a premature abandonment of more robust visions of public regulation" (p. 502).
- Part I is headed "Fiduciaries for Whom?" (p. 502). On Delaware law (p. 503): officers and directors "must … treat stockholder welfare as the only end".
- p. 504: "A fiduciary with sharply opposed loyalties teeters on the edge of contradiction." And: "Insofar as the interests of stockholders and users diverge, the officers and directors of these companies may be put in the untenable position of having to violate their fiduciary duties (to stockholders) under Delaware law in order to fulfill their fiduciary duties (to end users)."
- Bearing. **§6.4, §6.5: cuts against a fiduciary route and supports the paper's structural turn.** A platform's loyalty runs to shareholders, so a duty of impartiality to two users cannot sit in the platform without a change in law. That is why the notary was an officer outside the parties' hierarchy ("outside any State hierarchy", UINL, below). Part II.A (pp. 508-510), which I did not read, maps four ways to reconcile duties to stockholders with duties to users and says "Balkin has never squarely addressed the issue of crosscutting loyalties" (p. 508); the conflict it treats is stockholders against users, so the inference to a duty of impartiality between two users is mine, not theirs.

**Viljoen, "A Relational Theory of Data Governance" (2021)** — `viljoen2021relational`. 131 Yale L.J. 573; the SSRN record (10.2139/ssrn.3727562) matched on Crossref; I opened the Yale PDF. **Text opened, read in part.**
- p. 573 (abstract): "Individualist data-subject rights cannot represent, let alone address, these population-level effects."
- p. 607: the "vertical" data relation is "between an individual data subject and an individual data collector"; the "horizontal" relation "relates data subjects not to data collectors, but to one another."
- Bearing. **§2.1, §6.1: partly supports.** Viljoen's horizontal axis connects people *through* the collector, which resembles the triad. But her relation is between data subjects whose data is pooled, not between two parties coordinating a transaction. Optional. It supports the paper's turn from the individual user to the structure.

**Gal and Elkin-Koren, "Algorithmic Consumers" (2017)** — `gal2017algorithmic`. 30 Harv. J.L. & Tech. 309. JOLT PDF opened. **Text opened, read in part** (introduction; p. 339).
- p. 339: "In agency law: Does the algorithm act as an agent for the consumer? Does it have fiduciary duties towards the consumer?"
- Bearing. **§6.4: supports.** An early statement that a user-side algorithm raises these questions. It is the nearest scholarship I found to "counter-delegation", and it asks the questions without answering them.

**Kolt, "Governing AI Agents" (Notre Dame L. Rev. 101, forthcoming)** — `kolt2025governing`. arXiv 2501.07913; the PDF I opened is dated 11 February 2025 on its footer. **Text opened, read in part** (abstract, p. 8, p. 10 n. 26, p. 25).
- Abstract: "new technical and legal infrastructure is needed to support governance principles of inclusivity, visibility, and liability."
- p. 10 n. 26, quoting the Restatement (Third) of Agency § 1.04 cmt. e: "a computer program is not capable of acting as a principal or an agent as defined by the common law. At present, computer programs are instrumentalities of the persons who use them." Kolt notes the words "at present" and the Restatement's thin support.
- p. 25: the agent's "fiduciary duty to act loyally for the principal's benefit in all matters connected with the agency relationship."
- Bearing. **§6.4: complicates.** If the user's counter-agent is not legally an agent, it cannot carry the notary's or interpreter's duties by analogy; it is the user's tool, and the duties fall on whoever supplies it. The paper should say who the supplier is.

**Citron, "Technological Due Process" (2008)** — `citron2008technological`. 85 Wash. U. L. Rev. 1249; WashU journal PDF opened. **Text opened, read in part** (abstract, p. 1253, p. 1305).
- p. 1253: "Some systems adjudicate in secret, while others lack recordkeeping audit trails, making review of the law and facts supporting a system's decisions impossible."
- p. 1305: "At a minimum, automated systems should generate audit trails that record the facts and rules supporting their decisions."
- Scale: US benefits administration and similar government systems (not private platforms).
- Bearing. **§5.3, §6.4: supports and pre-empts.** Citron proposed audit trails and reasons for automated decisions in 2008. §6.4's agent that "maintains independent, verifiable audit logs" extends a proposal that already exists, with the log held by the user instead of the system. The paper needs her for lineage. Her setting is government action, so the step to private platforms is the paper's to defend.

**UINL, *Principles of the notarial function* (Rome, 8 November 2005) and *Principles of notarial ethics*** — `uinl2005function`, `uinl2005ethics`. Both pages at uinl.org opened. The ethics page ends "Approved by the General Meeting of Member Chambers of Notaries of the UINL, Mexico City, Mexico - 17th October 2004", so the ethics principles are 2004 (Mexico City); only the function principles are 8 November 2005 (Rome). **Text opened, primary source of a professional body; not a statute.**
- Function, Part I: notaries "are professional lawyers and public officials appointed by the State to confer authenticity on judicial deeds and contracts contained in documents drafted by them and to advise persons who call upon their services. Although Notaries have official powers they are required to act both impartially and independently, outside any State hierarchy." Also: "a Notary's impartiality can also take the form of lending adequate assistance to whichever of the parties might be in a position of inferiority."
- Ethics, principle 9: "When acting in their official capacity notaries must balance the respective interests of the parties concerned and seek a solution with the sole objective of safeguarding both parties."
- Ethics, principle 10: "they must inform and advise the parties as to the possible consequences of their instructions … and ensure … awareness of the legal force of the deed."
- Bearing. **§5.3, §6.4: supports, and fills a gap in the outline.** It is the clearest written statement I found of the duty the paper calls the notary's. Two cautions. It is the union's own description, and facet G found reviews reporting that Cuzco notaries acted "for both litigants and judges" and could be moved by clients (Andrien on Burns); the norm and the practice differ. Second, the norm is for civil-law notaries; the outline cites the Castilian rule of 1503 and the English plea, and the English notary tradition is a different one. I did not search the national statutes behind the UINL text.

**Gillespie, "The politics of 'platforms'" (2010)** — `gillespie2010politics`. Crossref DOI 10.1177/1461444809342738, *New Media & Society* 12(3): 347–364. **Abstract only.** The abstract says providers use the word "platform" to position themselves to users, advertisers and policymakers, and "seek protection for facilitating user expression, yet also seek limited liability for what those users say." Bearing: **§4, §5.2**; the platform's self-description as a neutral facilitator is a claim to the mediator role. Optional.

**van Dijck, Poell and de Waal, *The Platform Society* (2018)** — `vandijck2018platform`. Crossref DOI 10.1093/oso/9780190889760.001.0001. **Record only** (the OUP chapter link returned a login page). **Cohen, *Between Truth and Power* (2019)** — `cohen2019between`. Crossref DOI 10.1093/oso/9780190246693.001.0001. **Record only.** **Delacroix and Lawrence, "Bottom-up data Trusts" (2019)** — `delacroix2019bottom`. Crossref DOI 10.1093/idpl/ipz014, *International Data Privacy Law*; the OUP PDF returned a login page. **Record only.** Their title and the Viljoen footnotes show that data trusts with independent trustees under fiduciary duties are a live proposal (Viljoen n. 182, PDF p. 76, cites the idea); I read neither Delacroix and Lawrence nor Cohen. Srnicek's *Platform Capitalism* and Khan's "The Separation of Platforms and Commerce": no book or article record found in Crossref in my searches; not verified.

### Group 5. The triad in social theory

**Simmel, *The Sociology of Georg Simmel*, ed. and trans. Wolff (1950)** — `simmel1950sociology`. archive.org full text (`in.ernet.dli.2015.215265`), opened. **Text opened, read in part** (the chapter "The Triad"; the index). Scale: social forms generally.
- p. 154, "The Tertius Gaudens": "the impartiality of the third element either served or harmed the group as a whole. Both the mediator and the arbitrator wish to save the group unity from the danger of splitting up. But, evidently, the non-partisan may also use his relatively superior position for purely egoistic interests." The translator glosses *tertius* as "the third who enjoys".
- The same passage describes the third party who "make[s] the interaction that takes place between the parties and between himself and them, a means for his own purposes."
- Index entries: *Tertius gaudens*, pp. 154–162 and 232–234; *Divide et impera*, pp. 162–169; "Distrust, as means of divide et impera", p. 166.
- Bearing. **§2.1, §5.2, §5.3: supports, with the vocabulary the outline lacks.** Simmel names three roles for the third (mediator or arbitrator; the third who profits; the third who divides). The notary is institutionalised mediator. A platform paid by a commission, or by one side, is in the second role. *Claude's reading:* this gives §5.3 a sharper question than "which safeguards are missing": which third is the platform, and how does it get paid. Page numbers outside p. 154 come from the index, not from reading the text.

**Stovel and Shaw, "Brokerage" (2012)** — `stovel2012brokerage`. Crossref DOI 10.1146/annurev-soc-081309-150054, *Annual Review of Sociology* 38: 139–158. **Abstract only** (Annual Reviews page walled). Abstract: "brokerage has the capacity to ease social interaction, enhance economic activity, and facilitate political development. On the other hand, brokerage often breeds exploitation, the pursuit of personal profit, corruption, and the accumulation of power; through these and other processes, brokerage can exacerbate existing inequalities." Bearing: **§5.3**; the review is a field-level statement of the dual aspect the paper needs: the same position eases and exploits.

**Obstfeld, "Social Networks, the *Tertius Iungens* Orientation, and Involvement in Innovation" (2005)** — `obstfeld2005social`. Crossref DOI 10.2189/asqu.2005.50.1.100, *ASQ* 50(1): 100–130. **Abstract only.** The abstract contrasts the *tertius iungens* ("third who joins") with "the *tertius gaudens* orientation emphasized in structural holes theory, which concerns the advantage of a broker who can play people off against one another for his or her own benefit." Study: an engineering division of one automotive firm. Bearing: **§6.4**; a third who connects rather than profits is a design target, though Obstfeld's evidence is intra-firm.

**Burt, "Structural Holes and Good Ideas" (2004)** — `burt2004structural`. Crossref DOI 10.1086/421787, *AJS* 110(2): 349–399. **Record only** (the author-site PDF returned an HTML page). Burt's *Brokerage and Closure* (2005): Crossref DOI 10.1093/oso/9780199249145.001.0001; `burt2005brokerage`. **Record only.**

**Platforms as brokers.** I searched for work that casts a platform as a tertius gaudens or structural-hole broker and **found none** in my searches. Related results: a Slovenian journal paper on platforms in food supply chains and a Finnish case study of a subcontracting platform, both described as using structural-hole ideas; I opened neither. Quintane and Carnabuci (2016, *Organization Science* 27: 1343–1360, DOI 10.1287/orsc.2016.1091, Crossref-verified; abstract seen in search only) separate gaudens and iungens modes in e-mail data. The claim "no one applies Simmel's tertius gaudens to platforms" is therefore "I found none in WebSearch and Crossref," not a settled gap.

---

## (c) Synthesis

### Q1. Lettered intermediaries as a class

I could open one book of the group, Messick. The rest I know only by record or by secondary description, so nothing below claims what Rama, Salomon or Justice say.

- **Writing as an instrument of rule is a literature with a name, and the outline does not cite it.** Rama is the standard citation (record verified); Messick is the opened counterpart, with the phrase "textual domination" and the notary as a paid class of scribes.
- **The class has a critique that belongs in the paper.** Reviews and a Rama critique found in search say the *lettered city* misses Indigenous literacies, and Rappaport and Cummins (2012) is the book titled as the answer. That bears on the outline's binary of a record-controller against a person who cannot make a record.
- **Messick complicates §3.3 directly.** Where the law makes testimony primary and a document only as good as its witnesses, writing does not override the voice. Record over voice is a legal choice. *Claude's reading:* the paper's mechanism should be stated as "a regime that lets the document outrank the witnesses", not as writing itself.
- **Public scribes and "literacy mediators".** I found records (Kalman reviewed by Kamberelis; Papen and Thériault) but opened none. I found no scholarship on India's letter-writers or on *écrivains publics* beyond what facet G logged.

### Q2. Files, registers and paperwork: what does each say about a record overriding a person's account?

| Source | What it says on the question | Depth |
|---|---|---|
| Weber (G&M 197, 214) | Files are the base of modern administration and "knowledge of the files" is a technical advantage. Nothing here on a record overriding a person | text opened |
| Scott (Intro) | A state's map "creates such a system through its ability to give its categories the force of law" | text opened |
| Vismann | *Quod non est in actis, non est in mundo* (per the description) | description only |
| Smith 1978 | A text carries "instructions for its interpretation and for the authorization of its facticity" | abstract only |
| Messick | The opposite arrangement: documents are not evidence, only witnesses are | text opened |
| Kafka; Hull; Gitelman; Bowker and Star; Goody | I cannot report an answer | description or record only |

**Where the frame conflicts.** The author has ruled that algorithmacy is "not legibility". Scott's account of records is a legibility account. The outline's §4 row "The Record" uses a different mechanism (a third party that reads both and commits an outcome). The paper can use Scott for the sentence on the map and nothing else, and should say so.

### Q3. Signing what you cannot read, then and now

**What present-day doctrine protects the non-reading signer?** From the texts I opened:

1. **The rule is that a competent adult is bound by what they sign or accept, read or unread.** *Hill*: "Competent adults are bound by such documents, read or unread." The empirical case that nobody reads is strong (Bakos et al., working paper: 0.1 to 0.2 percent open the licence; Ben-Shahar and Schneider on disclosures "almost always ignored").
2. **Non est factum.** Facet G found the plea narrow (a careless signer loses: *Saunders*, via Connell) and that the misreaders in the leading cases were counterparties. I searched for a decision applying it to a click-through and **found none**. Commentary I saw said the plea is confined to signers who could not read or understand and not careless. *Claude's reading:* it will not protect a competent person who clicks "I agree" without reading.
3. **Assent and notice (*Specht*).** This protects a user who was never given reasonably conspicuous notice. It does not protect one who saw and did not read.
4. **Unconscionability (*Walker-Thomas*).** The test asks about the signer's "education or lack of it" and "a reasonable opportunity to understand". This is the closest relative of the illiterate-signer protection and the one the paper should name. It is a fairness test, applied after the fact, and its use against platform terms was not something I could check (Heller, 2020 SCC 16, is reported to have held an Uber arbitration clause unconscionable; I could only see commentaries).
5. **Statute.** UK CRA 2015 s. 62 makes unfair terms non-binding whether or not read; s. 68 requires plain, legible writing. In US consumer credit, 12 C.F.R. § 1002.9 requires specific reasons for refusals. I did not search the EU directive on unfair terms (a fetch of EUR-Lex returned nothing).

**What this does to §5.3.** The sentence "platforms have no counterpart to non est factum" is true of the plea itself and too strong as a claim about the field. *Claude's reading of what survives:* no doctrine requires anyone to read, explain and certify understanding *before* the act, as the Castilian rule and the civil-law notary's duty did. Present law protects against unfair terms, inconspicuous terms and unclear terms, after the fact, and only for the party against whom the terms operate. It does not protect the other party in a three-way coordination.

**The two roles the paper runs together.** In the adhesion cases the platform is *the drafter and counterparty*. In the outline's triad it is a *third party who reads both and commits an outcome*. The doctrines above fit the first role. The notary's duty fits the second. The paper's §5.3 compares the first to the second. Facet G already found that the misreader in the leading *non est factum* cases was a counterparty, which makes the historical analogue closer to the first role than the outline assumes.

### Q4. Duties of the modern intermediary

- **Fiduciary route.** Balkin's duty runs to the end-user. Khan and Pozen argue that platform fiduciaries have "sharply opposed loyalties" and that the label "invites an enervating complacency". No source I opened gives a duty to two principals.
- **Notary.** UINL gives that duty in writing, with the added duty to assist "whichever of the parties might be in a position of inferiority". That is the notary the paper invokes, and it is stronger than the outline's "sworn notary".
- **Counter-delegation.** The closest literature is Gal and Elkin-Koren (the questions), Kolt (agency law and its Restatement obstacle), Citron (audit trails), and the data-trust proposals that Viljoen's footnote 182 cites. I found no work proposing a "digital notary" under that name. I found no scholarship that casts the user-side agent itself as a third party with its own conflict of interest.
- **Platforms as intermediaries.** Gillespie (abstract) shows the self-presentation as neutral; van Dijck et al., Cohen and Srnicek were not opened.

### Q5. The triad in social theory

Simmel gives three types of third: the mediator or arbitrator, the third who profits, and the third who sets the others against each other. Stovel and Shaw call brokerage dual: it "eases" and "breeds exploitation". Obstfeld splits the broker into the one who plays people off and the one who joins. None of these sources, as far as I opened them, says anything about platforms, and I found no work that applies the tertius gaudens to one. The paper can claim the application as its own, with the caveat that my search was shallow.

### Q6. What a legal historian or sociologist of documents would say the outline gets wrong or omits

1. **Who is the third party's principal, and who pays?** Simmel's types turn on this. The outline never says whether the platform is paid by one side, both, or a third.
2. **Which legal role?** Counterparty-drafter or neutral third party (see Q3).
3. **The doctrinal inheritance.** The outline names the English plea and the Castilian rule. A contracts scholar will ask for unconscionability, assent and statutory unfairness, and for the evidence that reading fails.
4. **A regime with the opposite rule.** Messick.
5. **Norm against practice.** The UINL text is a profession's statement; the facet-G reviews report notaries serving clients unevenly.
6. **Sociology of documents.** Smith (1978), Riles (2006), Hull, Kafka and Gitelman say how a record gets its authority. The outline's "the record" treats it as given.
7. **Existing lineage for counter-delegation.** Citron (2008) and the data-trust literature already propose audit trails and user-side fiduciaries.
8. **Regress.** A user-side agent is a new third party. Simmel and Burt both warn about the third's interest.

### Claims the sources contradict or qualify

1. **"The safeguards that restrained human scribes have no counterpart."** Qualified by unconscionability, notice doctrine, CRA 2015, Reg B 1002.9 and Citron's proposals. What has no counterpart is a duty to read and explain before the act.
2. **"Reading the instrument aloud is the safeguard."** *Hill* calls its modern form useless; Bakos et al. and Ben-Shahar and Schneider show the cost of disclosure that nobody reads.
3. **"Record over voice is what writing does."** Messick: not under shari'a evidence doctrine.
4. **"A fiduciary route would restrain the intermediary."** Khan and Pozen on shareholder primacy.
5. **"The user's agent can carry the notary's duties."** Restatement (Third) of Agency § 1.04 cmt. e, as quoted by Kolt, says a program is an instrumentality of its user.

---

## (i) Ranked list: works the paper must include

| # | Work | Section | Why |
|---|---|---|---|
| 1 | *Hill v. Gateway 2000* (7th Cir. 1997) | §5.3 | The paper must answer a court that rejected the read-aloud analogue |
| 2 | UINL, Principles of the notarial function (2005) and Principles of notarial ethics (2004) | §5.3, §6.4 | Source for the notary's duty to both parties and to the weaker one |
| 3 | *Williams v. Walker-Thomas* (D.C. Cir. 1965) | §5.3 | The nearest present doctrine; the test names "education or lack of it" |
| 4 | Ben-Shahar and Schneider (2011) with Bakos et al. | §6.3, §5.3 | Evidence that disclosure fails; §6.3 must show it is not disclosure |
| 5 | Balkin (2016) and Khan and Pozen (2019) | §6.1, §6.4 | The fiduciary frame and its loyalty problem |
| 6 | Simmel, "The Triad" (Wolff 1950, p. 154) with Stovel and Shaw (2012) | §2.1, §5.3 | Vocabulary for the third who profits |
| 7 | *Specht v. Netscape* (2d Cir. 2002) | §5.3 | Assent doctrine for the click |
| 8 | Messick (1993) | §3.3 | A regime that put voice over record |
| 9 | Citron (2008) | §5.3, §6.4 | Prior proposal for audit trails and reasons |
| 10 | Kolt (2025) and Gal and Elkin-Koren (2017) | §6.4 | The legal status of the user's agent |
| 11 | Radin (2013); Kim (2013); Kessler (1943); Rakoff (1983); Obar and Oeldorf-Hirsch (2018) | §3.3, §5.3 | A contracts referee expects them; none opened |
| 12 | Rama (1996) | §2.5, §3.3 | Class-level source; library copy needed |

## (ii) Optional

Weber (G&M 197, 214); Scott (one sentence, with the stated reason for not adopting legibility); Viljoen (2021); Gillespie (2010); CRA 2015 ss. 62, 68; 12 C.F.R. § 1002.9; Obstfeld (2005); Burt (2004); Smith (1978); Rappaport and Cummins (2012); Salomon and Niño-Murcia (2011); Goody (1986); Vismann (2008); Kafka (2012); Hull (2012).

## (iii) Works that cut against the paper, and what they force it to concede

- **Hill** forces a concession that a modern court has said, in passing, that a seller's oral recitation of terms is ineffectual for mass transactions; its holding is that competent adults are bound by terms they did not read.
- **Bakos et al.; Ben-Shahar and Schneider** force §6.3 to say why a declared envelope is not mandated disclosure.
- **Walker-Thomas, Specht, CRA 2015** force the claim of "no counterpart" to narrow to "no duty to read and explain before the act".
- **Khan and Pozen** force §6.4 to say who holds a duty to two parties if the platform's loyalty is to shareholders.
- **Kolt (Restatement note)** forces §6.4 to say who is the legal agent behind the user's software.
- **Messick** forces §3.3 to state record-over-voice as a legal choice.
- **Scott** conflicts with the author's ruling that algorithmacy is not legibility.

## (iv) Aspects the outline is missing (proposed paragraph topics)

1. Two roles of the platform (drafter-counterparty and neutral third party) and which doctrine fits each.
2. What replaced *non est factum*: assent, unconscionability, statutory unfairness, and the failure of mandated disclosure.
3. The notary's duty of impartiality and its absence from the fiduciary literature.
4. How the third party is paid, using Simmel's types.
5. A regime in which testimony outranks the document (Messick).
6. The lineage of counter-delegation (Citron, data trusts, Gal and Elkin-Koren, Kolt) and the regress of a user-side third party.
7. How a record gets its authority (sociology of documents).

## (d) What I could not open, and where a human would look

- **Rama, *The Lettered City*; Salomon and Niño-Murcia; Rappaport and Cummins; Justice; Kalman; Hull; Vismann; Kafka; Gitelman; Bowker and Star; Goody (chapters); Radin; Kim; Cohen; van Dijck et al.; Srnicek.** University library, or the lending copies at archive.org with a login.
- **Kessler (1943), Rakoff (1983), Burt (2004), Obstfeld (2005), Stovel and Shaw (2012), Obar and Oeldorf-Hirsch (2018), Gillespie (2010), Smith (1978).** JSTOR, Annual Reviews, SAGE, T&F.
- **Khan and Pozen, Parts II-V.** Not read; the Harvard Law Review PDF at the bib URL is the full article (45 pages), so read Part II.A (pp. 508-510, "Managing Divided Loyalties") before relying on the claim that no source treats divided loyalties.
- **Khan, "The Separation of Platforms and Commerce."** No Crossref record found.
- **Nguyen v. Barnes & Noble; Meyer v. Uber; Berman v. Freedom Financial; Uber v. Heller (2020 SCC 16); *L'Estrange v Graucob* [1934]; *Marvco v Harris*.** Justia, BAILII, CanLII and the SCC site returned bot walls. CourtListener (a US court-records site) search returned unrelated results.
- **The published JLS version of Bakos et al.** I used the 2009 working paper.
- **Delacroix and Lawrence (OUP, login); Baynham (1993); Garfinkel, "Good organizational reasons for bad clinic records."** Not located or not opened.
- **UETA's error-in-electronic-transaction provision** and the EU Directive 93/13/EEC. Fetches returned nothing usable.
- **Restatement (Third) of Agency on dual agency** (an agent acting for both sides needs informed consent). I did not look; it is a lead for §6.4, unverified.
- **OpenAlex** was unavailable for the whole session (daily budget).
