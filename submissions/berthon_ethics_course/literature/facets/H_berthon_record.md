# Facet H: Berthon's record on remedies for digital harm

*Note added by the lead, 2026-10-13: this facet is a dated record. Full texts supplied later were read in `L1_berthon_fulltext.md`, which lists the statements here that they correct; where the two differ, `L1_berthon_fulltext.md` and `T_adjudication.md` §9 govern.*

Facet H, 2026-10-13. Agent-drafted. The author has not reviewed it, and none of the text is the author's.

## What this facet covers

Pierre Berthon's published position on who should remedy the harms of attention-capturing and algorithmic technology: the user, the firm or the regulator. The author has ruled that the draft passage at `sources/design_ethics_DRAFT.md` line 120 stays, and that Berthon's later work is added so the paper states his position as it now stands. The reader of the finished paper is Berthon himself. Every reading below that is mine and not the source's is marked "agent's reading".

**The question the synthesis answers.** Does Berthon's work, read in date order, move from individual remedies toward structural ones, stay mixed, or neither? Does the draft passage, which uses Berthon and Pitt (2019, mindfulness) and sets it against Williams (2018), represent him fairly?

## Legend for read status

- *read in full*: every page opened this session.
- *read in part*: pages named.
- *abstract only*: abstract seen, paper not opened. Paraphrase only; no quotation from the paper.
- *secondary only*: a press release or summary of the paper, not the paper.
- *not accessible*: could not be opened. The reason is logged.

Page locators for the two HICSS papers are the proceedings footers ("Page 4938"). Locators for Berthon and Pitt (2019) are the page numbers of the Elsevier "Corrected proof" PDF (pp. 1 to 7). The earlier library card adds 130 to reach the issue pages (131 to 137). I have not checked that mapping against the typeset issue, so treat "p. 136" as "proof p. 6, probably 136".

Rules followed: no e-mail address in any request, no Unpaywall, no `mailto` on Crossref or OpenAlex; no git; no browser tools; no paywall or bot-wall bypass.

## (a) Search log

| # | Source | Query or action | Result | Notes |
|---|---|---|---|---|
| 1 | Crossref | `works/<doi>` for 16 DOIs (all items below plus Williams) | all resolved; titles match | Crossref gives the HICSS-58 container as both the 58th and the 57th proceedings; the PDF header says 58th. Crossref escapes "&" as `&amp;` in two titles. |
| 2 | OpenAlex | `works/doi:<doi>?select=open_access,best_oa_location,locations` for 8 DOIs | HICSS-58: OA copy on ScholarSpace. Trajectories: flagged hybrid CC BY but no PDF URL. Brands (2018): Helda handle. Others closed. | anonymous, no `mailto` |
| 3 | ScholarSpace | `scholarspace.manoa.hawaii.edu/bitstreams/f8abcdc6-.../download` (the OpenAlex `oa_url` for HICSS-58) | 200, PDF, 10 pages | Read in full. The earlier facet got "service unavailable" for this paper. |
| 4 | AISeL | `aisel.aisnet.org/context/hicss-58/article/1573/viewcontent/download.pdf` | 403 | Not needed; ScholarSpace copy worked. |
| 5 | Local files | search under `~/iit-playground` and `~/Downloads` for Berthon, mindfulness, Bushor | found `~/Downloads/Berthon - Types of Mindfulness in an Age of Digital Distraction copy 2.pdf` (Elsevier corrected proof, 7 pp.) | The author's own copy. Text extracted with `pdftotext` only. |
| 6 | Local files | Su, Wang, Berthon (2023) from `pdfs/Z/` | present | Re-opened and re-read in full. |
| 7 | Local files | Williams (2018), Cambridge Core OA PDF of the whole book, held in `pyphi-experiments/dissertation/research/library/pdfs/williams2018.pdf` | 152 pp.; the passage is on PDF p. 120 | Page image of PDF p. 120 rendered and read: printed page 102. I did not re-download from Cambridge. |
| 8 | doi.org redirect for `10.1016/j.bushor.2024.03.002` and ScienceDirect `pii/S0007681324000284` (+ `/pdfft`) | 403 | bot or access wall; not bypassed. |
| 9 | WebFetch ScienceDirect `pii/S0007681325001715` (Keaney and Berthon) | 403 | not bypassed |
| 10 | `hdl.handle.net/1959.3/451892` (OpenAlex location for Addictive De-Vices) | redirects to a "Swinburne Research Bank has moved" page | no file; Swinburne figshare search via public API returned `[]` |
| 11 | `hdl.handle.net/10227/179387` (Helda, Brands, Truthiness and Post-Fact) | Anubis proof-of-work page | not bypassed |
| 12 | Semantic Scholar API, DOI lookups | abstract for Addictive De-Vices (full), Ageism in Tech (full), Refined interaction value, 4E; none for Trajectories, Keaney, Fixing fake news, 2016, 2024 chapter | `openAccessPdf` empty for Addictive De-Vices |
| 13 | OpenAlex abstract index | Trajectories, Fixing fake news, Brands, True/fake, Field-Ready HCI: abstracts. Keaney, 2016, 2024 chapter: none | |
| 14 | Crossref abstract field | JSM 2026 (both): full structured abstracts | |
| 15 | WebSearch | "Addictive De-Vices" informing guiding restricting pdf | no full text; SFU press release found; Hanken portal and Bentley news page are bibliographic only | Hanken portal (`harisportal.hanken.fi`) fetched: only a DOI link under "Access to Document". Bentley news teaser: no content. |
| 16 | curl + WebFetch | ScienceDaily copy of the SFU release (3 Oct 2019) | 200; read in full | secondary source for the policy paper |
| 17 | WebSearch (2 queries) | Trajectories abstract | Bentley portal listing relayed in summary; direct fetch of the portal URL gave 404 | OpenAlex abstract used instead |
| 18 | WebSearch (extended) | Keaney and Berthon abstract | ScienceDirect listing relayed in summary only | paraphrased, abstract only |
| 19 | mdpi.com `/2076-3417/16/14/6985/pdf` | 403 | open access paper, but the site refuses anonymous requests; not bypassed |
| 20 | SAGE, Emerald, Springer, IEEE full texts | not attempted | paywalled (Crossref `link` fields point to publisher PDFs); no open copy found by OpenAlex or Semantic Scholar | where a library login reaches them: section (d) |

## (b) Entries

### H1. Berthon and Pitt (2019), "Types of mindfulness in an age of digital distraction"

*Business Horizons* 62(2): 131–137. DOI 10.1016/j.bushor.2018.10.003. Key `berthon2019types`. Crossref title matches. **Read in full** (proof pp. 1–7). Genre: the "Marketing & Technology" department column, seven pages, aimed at managers.

**What is diagnosed.** Three reasons for the surge in mindfulness (proof p. 2): an "ever-rising tsunami of information and stimuli that clamor for our attention"; the rising costs of mindlessness in a technological age; and the appeal of an individual practice "relatively free of religious baggage". The attention-economy diagnosis proper is in section 5 (proof pp. 5–6): platforms "devour our attention" (the paper's report of Tristan Harris: "Harris argues that the big platforms ... devour our attention with their offerings", proof p. 5), Firms "are also spending billions on cutting-edge psychological research to reveal how to get consumers hooked", and then the passage the draft quotes.

**The quotation at line 120, checked word for word.** Proof p. 6: "Increasingly, our attention is not under our own control. Choices are made for us not necessarily in our interest but in the interest of social media companies and the advertisers they serve. In short, business models are designed to make us mindless." The draft's quotation is "our attention is not under our own control. Choices are made for us not necessarily in our interest but in the interest of social media companies and the advertisers they serve. In short, business models are designed to make us mindless". The words match exactly. The draft begins mid-sentence and drops the sentence-opening "Increasingly,". That is a fair excerpt, but the dropped word is a hedge Berthon and Pitt chose, and a reader who knows the paper will see it is missing. Page: proof p. 6; the issue page is 136 only if the proof and issue pagination agree, which I could not check.

The next paragraph, which the draft does not use, qualifies the indictment: "Now before we get all hot and bothered about nasty companies commandeering our minds, it is worthwhile to reflect on how we got to where we are now." The authors then trace the advertising model to the collapse of digital marginal cost: "Consumers got used to getting stuff for free, so business had to develop new models to generate revenues." (proof p. 6).

**What is prescribed, and who bears it.**

- The user, by implication only. The paper's stated addressee is the manager ("it is incumbent upon managers in general and marketers in particular to understand the phenomenon", proof pp. 1–2), and it gives no instruction to consumers. Its individual-level content is the typology itself: four modes of attention (observation, remembering, discrimination, contemplation), nested as awareness, returning, evaluation and insight (proof pp. 3–5). The paper says of the first mode (proof p. 6): "observational mindfulness may be of little help with addictive technology platforms and their associated content—being more immersed in a moment-by-moment Snapchat streak may even be counterproductive. Here, evaluative (right) mindfulness is needed, with the ability to discern the wholesome from unwholesome capturing of attention and thereby opening us up to the possibility of choice." And: "wise mindfulness or mindfulness that leads to insight is essential if we are to see how our minds are undermined by the technologies and content we interact with, and equally importantly, how the mind undermines itself." (proof p. 6). So Berthon and Pitt themselves say the thin, popular form of mindfulness does not suffice against the platforms.
- The firm, as seller. The typology "allows firms to develop offerings to help particular modes of mindfulness" (proof p. 6). Agent's reading: this is a product opportunity, not a duty.
- The firm, as business-model designer. The typology "allows marketers to rethink the 'attention capturing' and 'more consumption is better' business models and innovate so as to develop more mindful modes of business practice" (proof p. 6), and the summary ends: "challenges to innovate to develop new business models that do not run on attention become readily apparent" (proof p. 6). No mechanism, incentive or enforcement is given.
- The employer. The paper reports that "firms see mindfulness practice as a way of enhancing employee's productivity and well-being" (proof p. 6). This is description, not endorsement of that use or critique of it. Two sentences.
- The regulator, the designer as a regulated party, public policy: **not addressed.** A search of the extracted text for "regulat", "polic", "law" and "legislat" returned nothing relevant (the hits are "mindful lawyers" and a K-12 reference title).
- Literacy, reading, print: none. "Education" appears only as "mindful education" in a list of products and in a reference title.

**Scale.** The individual and the firm; no state or world scale.

**Bearing on the draft.** The earlier library card (`berthon2019.md`) reads the remedy locus as "subject", with two firm-side sentences. My reading agrees with the card on the facts. Where I differ: the card and the draft treat the firm-side line as an exhortation with no mechanism, which is accurate, but the draft's final sentence ("leaves the underlying corporate incentives untouched") goes beyond the paper by implying Berthon and Pitt think mindfulness neutralises the architectures. They say the opposite about observational mindfulness (quoted above).

### H2. Berthon, Pitt and Campbell (2019), "Addictive De-Vices: A Public Policy Analysis of Sources and Solutions to Digital Addiction"

*Journal of Public Policy & Marketing* 38(4): 451–468. DOI 10.1177/0743915619859852. Key `berthon2019addictive`. Crossref title matches; published online 28 July 2019. **Paper not opened** (SAGE closed access; no open copy found, see log 10, 12, 15). Abstract read in full. Secondary source read in full: the SFU press release (key `sfu2019addictive`).

**Abstract (read in full).** "We spend our days looking at them, talking to them, and touching them. We sleep with them, work with them, and play with them. They increasingly consume our time, attention, and money: we are addicted to our digital devices—or, more precisely, the digital experiences they enable. This addiction is both akratic (we are aware of the negative consequences) and engineered (designed on purpose). Marketers are complicit in this engineering: through digital networks and big data they ubiquitously monitor and experiment on consumers. This knowledge is used to create ever-more addictive digital experiences enabled by devices, their platforms, and their content. In this article, the authors explore marketing's role in the rise of the phenomenon: from product design, through advertising and big data, to the dynamics of ubiquitous distribution and 'free' pricing. The authors then turn to policy solutions and discuss how informing, guiding, and restricting can help ameliorate the problem and promote the public good. The article concludes by outlining multiple areas for marketing and public policy research." (abstract only; Semantic Scholar record of the SAGE abstract).

**Sources of addiction named (abstract).** Engineered design; marketing's monitoring of and experiments on consumers; product design, advertising, big data, ubiquitous distribution, "free" pricing (the four Ps). The addiction is called "akratic", so awareness does not cure it. Agent's reading: that single word already says an informed individual will not simply stop, which bears on the draft's claim that the individual remedy is outmatched.

**Solutions: informing, guiding, restricting.** The abstract names them and nothing more. The detail below is **secondary only**: an SFU press release of 3 October 2019 in which Leyland Pitt answers questions in the first person ("I would like to see…") and presents "his team's recommendations". It is not a quotation from the paper, and the paper may say more or differently. Organised by the paper's four Ps:

| P | What the release reports | Who acts |
|---|---|---|
| Product | "mandatory labeling for apps"; warning labels "would likely prompt more conscious decision-making on the part of consumers, and reduce the automaticity often inherent to addiction"; "mandate natural 'stopping points' in digital offerings … endless games and infinite scrolls would be punctuated with natural breaks, in the same way that books have chapters" | regulator mandates; firm complies; user decides (labels) |
| Promotion | "Disclosures could be included in ads for digital products and services, similar to prescription drug ads … This could include explicit information on how much time a user spends using an app or service, as well as how much a company is making from a user's attention and information." | the release says disclosures "could be included" in ads and names no body that would require them; firm discloses |
| Place | "distracted walking"; "Rather than ban phones in these busy areas, government intervention could shape behavior", with the German ground-level crossing signals as the example | government shapes the environment (guiding) |
| Price | "Digital products could disclose, on average, what in-app purchases typically end up costing"; "regulators could impose taxes directly on the most addictive offerings, as they have done in the case of tobacco products; alcohol; and, in some cases, prescription drugs." | regulators "could impose taxes" (restricting); products "could disclose" typical in-app costs, no mandating body named (informing) |

Agent's reading, labelled as such: mapping the release onto the abstract's three verbs, "informing" is labels and disclosures, "guiding" is environmental design by government, and "restricting" is mandated stopping points and taxes. The paper's own definitions of the three verbs I have not seen. What the release makes clear is that at least three of the remedies are mandated by regulators and borne by firms, and the one individual-facing remedy (warning labels) is itself imposed on firms by regulation.

**Scale.** Consumer-policy; the release's examples are US, Canadian, German and Chinese (a "Fast Facts" box in the release, not the paper).

**Bearing.** This is the strongest evidence in the record against reading Berthon as an individual-remedy author. See synthesis Q1 and Q4.

### H3. Su, Wang and Berthon (2023), "Ethical Marketing AI?"

HICSS-56, pp. 4933–4942. DOI 10.24251/hicss.2023.603. Key `su2023ethical`. Crossref title matches. **Read in full** (re-opened this session; 10 pages).

**Ethical position.** A structured literature review (Web of Science, 456 hits, 377 studies kept, p. 4935). It sorts AI ethics into three clusters, "algorithm, society and existential" (abstract), and maps them to marketing systems, brands and consumers. It concludes the field "is still very much in its infancy" (abstract). It takes no stand beyond calling AI ethics important; its stance is descriptive.

**What it asks of whom.**

- Marketers and academics: "The challenge for academics and marketers is how to develop clear programs that embrace the practical significance and societal impact of AI while mitigating the risks caused by ethical dilemmas." (p. 4940)
- Marketers and policymakers: "Marketing and policymakers also need to cultivate a forward-looking mindset and see how ethical concerns embedded in technological innovation will translate into the practical domain. In this way, marketers will not miss the opportunity to take action proactively to address ethical issues." (p. 4940)
- Brands, on transparency: "a transparent and customer-centric data policy that encourages customers to share information may turn these regulations from a threat into a chance, improving the trust in AI (Wang et al., 2020)." (p. 4940)
- Users: nothing is asked of them. The consumer appears as a bearer of harm: "the average citizen's ability to make autonomous choices" is reduced by firms' use of AI (p. 4938).

**Explanation, transparency.** Opacity is named as a problem: machine learning algorithms "suffer from a long-standing problem of being opaque when it comes to interpreting the results" (p. 4938); "Transparency of AI … gives brands an idea of whether the models have been thoroughly tested … This aspect has been a challenge since technical complexities perpetuate Black Box AI." (p. 4940). It is transparency for the brand, not a right of the consumer.

**Literacy.** A search of the extracted text for "literac" returns only "literature". The paper makes no argument from literacy, reading, print or education. The nearest passage is on the digital divide (p. 4938): "A well-established ethical concern focuses on the digital divide (McSorley, 2003). This concerns the divides between countries, genders, and ages, between rural and urban. AI can exacerbate each of these divides. Those who cannot access the underlying technology will miss the benefits. In terms of societal impact, there are concerns that digital technologies function in ways that perpetuate racial and colonial structures." This is about access, and it is reported from the literature, not argued.

**On attention and addiction** (p. 4938): "The Netflix film 'The Social Dilemma' focuses on how big social media companies manipulate users by using algorithms that encourage addiction to their platforms."

### H4. Berthon, Yalcin, Pehlivan and Rabinovich (2024), "Trajectories of AI technologies: Insights for managers"

*Business Horizons* 67(5): 461–470. DOI 10.1016/j.bushor.2024.03.002. Key `berthon2024trajectories`. Crossref title matches. **Abstract only; not accessible** (ScienceDirect 403; OpenAlex marks it hybrid gold CC BY, but no anonymous route to the PDF).

Abstract (OpenAlex, in full): "Generative artificial intelligence (AI) was always 'in the future.' With the release of the chatbot ChatGPT 4 there is emerging consensus that the future may have begun. Long in gestation this new technology promises a cornucopia of benefits to humankind, but worries remain that as general artificial intelligence scales, exceeding human intelligence, the servant may become the master. However, in the hyperbole the more nuanced trajectories of this technology have been neglected. In this article we use the Trajectories of Technology (ToT) framework developed by Berthon and colleagues to explore the disparate paths that AI and its present incarnation in chatbots has and will take in the coming years. This framework provides managers with a conceptual tool to strategically plan for the enormous promises and perils of AI in general and chatbots specifically."

From the abstract only: the addressee is the manager; the paper is a strategic-planning tool; it names "promises and perils". No ethical position, no mention of regulators, users, explanation or literacy appears in the abstract. I cannot say what the paper says on those points.

### H5. Wang, Berthon and Su (2025), "Rethinking AI and Big Data in Marketing Strategy"

HICSS-58, pp. 5184–5193. DOI 10.24251/hicss.2025.622. Key `wang2025rethinking`. Crossref title matches. **Read in full.** Footnote 1 (p. 5184) says it is "partly based on a forthcoming book chapter by Wang, Berthon, and Su" (the 2024 chapter, not accessible).

**Argument.** A problematization (Alvesson and Sandberg) of three assumptions about big data and AI (inevitability, objectivity, prediction beats explanation), reread through Weick's sensemaking. It rejects "dataism" as "both strategically shortsighted and ethically deficient" (p. 5184). Technology "should not be viewed as an inevitable consequence of a technological juggernaut with a life of its own, entirely divorced from social influence. We are not mere bystanders in this process." (p. 5188)

**Ethical position and who bears what.**

- Managers carry the responsibility, explicitly: "a sensemaking perspective puts control over big data and AI firmly back in managers hands; and places the ethical responsibility squarely on their shoulders." (p. 5191)
- Organizations: "it is crucial for organizations to advocate for legal, transparent, ethical, and sustainable data practices" (p. 5190), citing OpenAI employees seeking "increased transparency and stronger protections for whistleblowers"; firms should "reconsider their success metrics" because ad-click metrics "can exploit vulnerable individuals" (p. 5190).
- Platforms, as design: "social media platforms and news aggregators should use big data algorithms to provide users with diverse viewpoints" and "Removing filter bubbles and echo chambers can help reduce polarization" (p. 5190).
- Firms and stakeholders: "'experimenting for learning' communities with AI assistance, where managers, employees, customers, and other stakeholders use company data" (p. 5191), with "Clear guidelines for data sharing, usage, and privacy protection". And a limit: "it is unethical to conduct experiments without users' knowledge" (p. 5191).
- Regulators: left to future research. "Future research should develop and assess regulations that promote both ethical and sustainable practices", including to "propose new regulations for transparency and ethical audits" and to explore "Enforcement mechanisms and accountability measures" (p. 5192). The paper itself proposes no regulation.
- Users: diagnosed as acted upon, not asked to act. both sentences report other writers: "Leonard (2013) notes that companies can use big data to influence individual choices more effectively than individuals can influence themselves, often prioritizing profit over personal autonomy" (p. 5188); and "Data is typically privately owned and exploited for profit and influence, with the public excluded from the process and encouraged to trust algorithms (O'Neil, 2017)" (p. 5190).

**Explanation, transparency, literacy.** "Prediction trumps explanation" is the third assumption it contests, but this concerns managers' reasoning with data, not a user's right to an explanation (p. 5186). Transparency appears as a property of firms' practices and experiments. "Literacy" does not occur; "education" occurs only in a list of areas of discrimination (p. 5188) and a reference title.

**Note on the attention economy.** It cites *The Social Dilemma* for the claim that "technology that connects us also divides us, manipulates us, polarize us, distract us, monetize us and controls us" (epigraph, p. 5184). It does not cite the 2019 mindfulness or policy papers (reference list checked for "Berthon": only Su, Wang and Berthon 2023).

### H6. Keaney and Berthon (2025), "Balancing explainability and privacy in AI systems"

*Business Horizons*, online 28 October 2025. DOI 10.1016/j.bushor.2025.10.004. Key `keaney2025balancing`. Crossref title matches. **Abstract only, and the abstract only as relayed in a search-tool summary** (not verbatim); **not accessible** (ScienceDirect 403). The summary says: explainable AI supports regulatory compliance and stakeholder confidence, yet the methods that open the model can expose sensitive data; the authors offer a strategic framework that maps these vulnerabilities, reviews privacy-preserving solutions, and recommends a tiered explainability approach, privacy-preserving XAI techniques, and interdisciplinary AI governance teams. The addressee is the manager. I cannot give a locator or a quotation. First author Scott Keaney is listed as a doctoral candidate at Google.

### H7. The 2026 items

- **Wang, Berthon and John (2026), "The refined interaction value framework", *J. Services Marketing*.** DOI 10.1108/jsm-12-2025-0888. Key `wang2026refined`. Abstract read in full (Crossref); paper not accessible. Conceptual framework for "value co-creation and value co-destruction in AI-enabled services". It treats trust as "dynamically calibrated" by users and names the managerial lens: "designing, governing and monitoring AI-enabled service interactions", with "cross-functional priorities across design, operations and customer communication" and diagnostic indicators for "overreach, trust erosion, constrained exploration and contextual mismatch". Abstract only.
- **Berthon, DesAutels, Rabinovich and Weinberg (2026), "Reimagining customer experience as a 4E cognitive ecology".** DOI 10.1108/jsm-06-2026-0516. Key `berthon2026reimagining`. Abstract read in full; paper not accessible. Practical implication: "Service organizations should design connectors as cognitive prostheses that reduce friction, clarify action possibilities and support customer agency." Social implication: well-designed ecologies "can improve inclusion, service access and collective well-being". The burden sits on service designers. Abstract only.
- **Berthon, DesAutels and Divekar (2026), "Field-Ready HCI".** DOI 10.3390/app16146985. Key `berthon2026field`. Abstract read in full (OpenAlex); paper open access but not accessible to me (403). Five antecedents include "inclusive usability and accessibility", "contextual and cultural fit" and "trust and transparency". Whether the full text discusses user literacy or skills I cannot say; the abstract does not use the word.

### H8. Other Berthon items checked at abstract level

- **Berthon and Pitt (2018), "Brands, Truthiness and Post-Fact".** DOI 10.1177/0276146718755869. Key `berthon2018brands`. Abstract only (OpenAlex). It "offer[s] managers a way out of the postmodern cul-de-sac, discussing ways brands can be rethought and managed in a post-rational world." Manager-addressed.
- **Berthon, Pehlivan, Yalcin and Rabinovich (2019), "True, fake and alternative".** DOI 10.1108/jpbm-11-2018-2142. Key `berthon2019true`. Abstract only. A semiotic typology of news; no remedy.
- **Berthon, Chohan, Pehlivan and Rabinovich (2022), "Fixing fake news".** DOI 10.1016/j.bushor.2022.07.006. Key `berthon2022fixing`. Abstract only. "Remedies to fake news have generally emphasized identification of false content (information fact-checking) and censorship (curtailing information dissemination). In this article, we focus on the systems within which fake news travels, rather than the information per se." The remedy is "making substantive changes to the system", including "changing the elements of the system, adding feedback loops, and changing the goals of the system", and it falls on managers. This is a structural, not an individual, remedy (abstract only).
- **Du, Svizzero and Berthon (2024), "Understanding Ageism in Tech".** DOI 10.1109/mitp.2024.3501612. Key `du2024ageism`. Abstract only. Institutional logics of profit maximisation, diversity and inclusion, and culture fit "perpetuat[e] ageist design practices in digital products and services". Structural diagnosis.
- **Wang, Berthon and Su (2024), chapter "Sensemaking and Sustainability".** DOI 10.1007/978-3-031-72676-7_7. Key `wang2024sensemaking`. Not accessible; no abstract anywhere I looked. The HICSS-58 paper is "partly based on" it.
- **Wang, Berthon, Pitt and McCarthy (2016), "Service, emotional labor, and mindfulness".** DOI 10.1016/j.bushor.2016.07.002. Key `wang2016service`. Not opened; no abstract found.

### H9. Williams (2018), *Stand Out of Our Light*, pp. 100–102

Cambridge University Press. DOI 10.1017/9781108453004. Key `williams2018stand`. Crossref title matches ("Stand out of our Light"). **Read in part**: printed pp. 100–102 in full (PDF pp. 118–120 of the Cambridge Core OA copy); the surrounding chapter 11 and the structure of the book come from the earlier library card, not from my reading. Printed page 102 confirmed from a rendered page image.

**What Williams calls "as dangerous as it is futile."** The text, spanning pp. 101–102 (the sentence break falls at the page turn after "relevant to"):

> "Above all, we must not put any stock whatsoever in the notion that advancing 'mindfulness' among employees in the technology industry is in any way relevant to or supportive of reforming the dynamics of the digital attention economy. The hope, if not the expectation, that technology design will suddenly come into alignment with human well-being if only enough CEOs and product managers and user experience researchers begin to conceive of it in Eastern religious terms is as dangerous as it is futile. This merely translates the problem into a rhetorical and philosophical frame that is unconnected to the philosophical foundations of Western liberal democracy, and thus is powerless to guide it." (pp. 101–102)

The thing called "as dangerous as it is futile" is the hope, or expectation, that technology design will align with well-being if its makers (CEOs, product managers, UX researchers) conceive of it in Eastern religious terms. It sits in a list of "things we must not do in response to the challenges of the attention economy" (p. 100). Williams does not name Berthon and Pitt: a text search of the whole book for "Berthon" and "Pitt," returns nothing, and "mindful" occurs twice in the whole book: once in this passage (p. 101, "mindfulness") and once as the index entry "mindfulness, 101" (text search of the extracted Cambridge OA PDF of the whole book, not a page-by-page read).

**Other items on the same list, which bear on user-side remedies** (all printed pages):

- p. 100: "we must not reply that if someone doesn't like the choices on technology's menu, their only option is to 'unplug' or 'detox.'"
- p. 101: "we must reject the impulse to ask users to 'just adapt' to distraction".
- p. 101: "Additionally, education is necessary – but not sufficient – for transcending this problem. Nor will 'media literacy' alone lead us out of this forest."
- p. 101: "We also can't expect companies to self-regulate, or voluntarily refrain from producing the full effects they're organizationally structured and financially incentivized to produce."

## (c) Synthesis by question

### Q1. Berthon and Pitt (2019): diagnosis and prescription

The diagnosis is structural: "business models are designed to make us mindless" (proof p. 6), and firms spend "billions" on psychological research to hook consumers. The prescription, to the extent there is one, is individual in content though addressed to managers: a typology of four modes of attention, of which the thin popular mode "may be of little help" and the evaluative and insight modes are what the platforms demand (proof p. 6). Two firm-side lines accompany it: a market for mindfulness offerings and a challenge to "innovate to develop new business models that do not run on attention". The paper names no regulator, no design standard and no law. So within this paper the remedy sits in the individual's attention practice, but the paper tells managers, not users, what to do with the typology, and it gestures at firms. Berthon and Pitt do not claim mindfulness defeats the platforms; they say the shallow form fails against them. The quotation at p. 136 is word for word correct (see "Claims the sources contradict" for the dropped "Increasingly,").

### Q2. Addictive De-Vices: sources and solutions

Sources named in the abstract: engineered design, marketers' monitoring and experimentation on consumers through "digital networks and big data", and the dynamics of distribution and "free" pricing. The addiction is "akratic" as well as "engineered". Solutions: informing, guiding and restricting. From the SFU release only, not the paper: mandatory labels and proposed disclosures (informing; the release calls the labels mandatory and says disclosures "could be included" in ads and could cover in-app costs, without naming who would require them), government shaping of the physical environment (guiding), and mandated stopping points and taxes on "the most addictive offerings" (restricting; regulator acts, firm bears). The paper's own treatment of each verb is unread. If the release is faithful, no remedy in it is asked of the user alone.

### Q3. The AI papers

- *Position.* Su, Wang and Berthon (2023) is descriptive and calls for "forward-looking" marketers and policymakers. Wang, Berthon and Su (2025) is the most explicit: ethical responsibility "squarely on [managers'] shoulders". Trajectories (2024) and Keaney and Berthon (2025) are manager-addressed at abstract level. The 2026 items address service designers and managers.
- *Managers.* All of them.
- *Designers.* The 2026 abstracts ask service organisations to design for "customer agency", "inclusion, service access" and calibrated trust. The 2025 HICSS paper asks platforms to design against filter bubbles.
- *Regulators.* Only the 2025 HICSS paper and the 2023 review name policy, and both treat it as future research or a mindset for policymakers, not as a measure. The paper does not propose a rule. Keaney and Berthon (2025) mention "regulatory compliance" in the abstract summary only.
- *Users.* Never asked to do anything in the papers I opened. They are the party acted on.
- *Explanation, transparency.* Present as managerial and firm-side concerns (opacity, black-box AI, explainability versus privacy in the 2025 abstract), not as a user's right or a user competence.
- *Literacy, education, user competence.* None in the full texts I read (Su et al. 2023; Wang et al. 2025). Unknown for Trajectories, Keaney and Berthon, and the three 2026 papers, which I read at abstract level only.

### Q4. Individual toward structural, mixed, or neither?

My answer rests on dates and locators. In date order: March 2019 issue, mindfulness column, individual remedy plus two firm-side lines (proof p. 6). July 2019 online, policy paper, which prescribes "informing, guiding, and restricting" (abstract) and, in the SFU release, mandated labels, stopping points and taxes. Then 2022 to 2026, manager and firm addressed (Wang et al. 2025 p. 5191; Berthon et al. 2022 abstract). The work is mixed from the start and does not run from individual to structural, because the structural, regulator-facing remedy appears in 2019 in the same year as the mindfulness column and is then largely absent: the later work shifts toward managers and firms and treats regulation as future research (Wang et al. 2025, p. 5192).

**Sentences that support a move toward structural remedies.** "business models are designed to make us mindless" (proof p. 6) already names the structure in 2019. "Remedies to fake news have generally emphasized identification of false content … we focus on the systems within which fake news travels" (2022 abstract). "We are not mere bystanders in this process." (Wang et al. 2025, p. 5188).

**Sentences that cut against it.** The remedy of the 2019 policy paper is regulatory, yet the 2025 paper places it with managers: "places the ethical responsibility squarely on their shoulders" (p. 5191), and regulation arrives only as "Future research should develop and assess regulations" (p. 5192). The later "structural" remedies are managerial and self-governing, which is not the restriction the 2019 policy paper reportedly prescribes. Agent's reading: Berthon writes for manager audiences (*Business Horizons*, HICSS marketing tracks), and the remedy follows the audience as much as any change of view.

**If the 2019 policy paper already prescribes restriction, say so.** It does. The abstract itself lists "restricting", and the press release reports mandated stopping points and taxes on the most addictive offerings. The draft passage's use of the mindfulness paper alone therefore under-represents his position: a reader who knows the policy paper will see that the draft sets Williams's call for design reform against an author who co-wrote a call for regulated design reform in the same year. The author has ruled to keep the passage and add the later work; this finding bears on how the addition should be framed.

### Q5. Is the Williams quotation accurate and in context?

The words "as dangerous as it is futile" are accurate and on the stated pages (101–102). Two points of context differ from the draft. (1) The draft writes that Williams calls "employee mindfulness programs in tech" "as dangerous as it is futile". Williams applies the phrase to the hope that design will align with well-being if the makers of technology (CEOs, product managers, UX researchers) conceive of it in Eastern religious terms, and the sentence before it rejects the notion that mindfulness among "employees in the technology industry" is relevant to reforming the attention economy. That is mindfulness as a route to reforming design from inside firms, not mindfulness as a practice for users or consumers. (2) The draft sets this against Berthon and Pitt as a refusal of the "subject-side remedy". Berthon and Pitt's subject is the consumer's own attention, not the tech-industry employee's, and the only place they discuss employee mindfulness is the two descriptive sentences on firms promoting it for productivity. Williams does reject user-side remedies on the same pages ("just adapt", "unplug" or "detox", "media literacy alone"), so the draft's underlying point can be supported with different sentences. Agent's reading: the quotation is real, but it answers a claim Berthon and Pitt did not make.

### Q6. Literacy, reading, writing, print, media history

None. Full texts opened: Berthon and Pitt (2019), Su et al. (2023), Wang et al. (2025). None mentions literacy, print or the history of media. Berthon and Pitt use a Buddhist and psychological, not a historical-media, frame. Su et al. discuss the "digital divide" as an access problem and cite "The Social Dilemma". No full text shows any literacy argument; the abstracts and titles of the others show none either. This confirms facet Z's finding at full-text depth for three papers and at abstract depth for the rest. The paper's literacy history therefore cannot be presented as continuous with anything Berthon has argued.

### Claims the sources contradict

1. **Draft line 120: Williams calls "employee mindfulness programs in tech" "as dangerous as it is futile."** Williams's phrase targets "the hope, if not the expectation, that technology design will suddenly come into alignment with human well-being" if makers of technology conceive of it in Eastern religious terms (p. 102). The sentence before it rejects "the notion that advancing 'mindfulness' among employees in the technology industry is in any way relevant to or supportive of reforming the dynamics of the digital attention economy" (p. 101), so he does address mindfulness among tech employees; "programs" is the draft's word, and the "dangerous ... futile" clause attaches to the design-alignment hope. He does not discuss users' own mindfulness, and he does not discuss Berthon and Pitt.
2. **Draft line 120: Williams "refuses the subject-side remedy by name."** The named target of the "dangerous … futile" line is a design-side hope. The user-side refusals ("just adapt", "unplug", "media literacy alone") are on pp. 100–101 and are not named as mindfulness.
3. **Draft line 120: "Expecting personal mindfulness … to neutralize architectures built to tune and herd behavior … leaves the underlying corporate incentives untouched."** Berthon and Pitt do not expect mindfulness to neutralise the architectures: observational mindfulness "may be of little help with addictive technology platforms" (proof p. 6). They also pose a business-model challenge ("innovate to develop new business models that do not run on attention", proof p. 6), though without a mechanism.
4. **Draft line 120 uses Berthon and Pitt (2019) alone as Berthon's remedy.** Berthon, Pitt and Campbell (2019) prescribe informing, guiding and restricting (abstract), and at least three of the remedies in the SFU release are regulator-imposed. The mindfulness paper alone under-represents his position.
5. **Minor: the Berthon and Pitt quotation drops the opening "Increasingly,".** The words that remain are verbatim. The page number "136" rests on an unchecked mapping from proof page 6.
6. **Facet Z, B11: "Types of mindfulness ... abstract only" and the 2023 HICSS finding.** The library card shows the mindfulness paper was read in full earlier; I confirm that, so the Z table's "abstract only" status is superseded. Z's statement that HICSS-58 was "not accessible (service unavailable)" is also superseded: the paper opens via the OpenAlex `oa_url`.

## (d) Gaps and unverified leads

Not opened, and where a Bentley library login would reach each:

| Paper | Why not opened | Where to get it |
|---|---|---|
| Berthon, Pitt and Campbell (2019), *JPP&M* 38(4), DOI 10.1177/0743915619859852 | SAGE closed access; no open copy found | SAGE Journals via Bentley (Business Source Complete / EBSCO or the AMA journals package). This is the priority: it settles what "informing, guiding, and restricting" mean and whether the SFU release is faithful |
| Berthon, Yalcin, Pehlivan and Rabinovich (2024), *Business Horizons* 67(5), DOI 10.1016/j.bushor.2024.03.002 | ScienceDirect 403 to anonymous requests (OpenAlex says CC BY open access) | ScienceDirect; open access, so a browser session without a bot challenge may open it |
| Keaney and Berthon (2025), *Business Horizons*, DOI 10.1016/j.bushor.2025.10.004 | ScienceDirect 403; closed | ScienceDirect via Bentley |
| Wang, Berthon and Su (2024), chapter 7 in *Sustainable Development Seen Through the Lenses of Ethnoeconomics and the Circular Economy* (Springer), DOI 10.1007/978-3-031-72676-7_7 | paywalled; no abstract found | SpringerLink via Bentley |
| Wang, Berthon and John (2026), *J. Services Marketing*, DOI 10.1108/jsm-12-2025-0888 | Emerald closed | Emerald Insight via Bentley |
| Berthon, DesAutels, Rabinovich and Weinberg (2026), *J. Services Marketing*, DOI 10.1108/jsm-06-2026-0516 | Emerald closed | Emerald Insight via Bentley |
| Berthon, DesAutels and Divekar (2026), *Applied Sciences* 16(14): 6985, DOI 10.3390/app16146985 | mdpi.com 403 to anonymous requests (open access) | mdpi.com in a browser; check for any treatment of user skills or literacy |
| Berthon and Pitt (2018), *J. Macromarketing* 38(2) | SAGE closed; Helda copy behind a bot wall | SAGE via Bentley, or the Helda handle in a browser |
| Berthon, Pehlivan, Yalcin and Rabinovich (2019), *JPBM* 29(2) | Emerald closed | Emerald via Bentley |
| Berthon, Chohan, Pehlivan and Rabinovich (2022), *Business Horizons* 65(6) | ScienceDirect 403 | ScienceDirect via Bentley |
| Du, Svizzero and Berthon (2024), *IT Professional* | IEEE paywall | IEEE Xplore via Bentley |
| Wang, Berthon, Pitt and McCarthy (2016), *Business Horizons* 59(6) | not opened; no abstract found | ScienceDirect via Bentley |

Other gaps.

- **Page numbers of the mindfulness quotation.** The version-of-record pages (131–137) were not checked against my proof PDF. Confirm that "business models are designed to make us mindless" is on p. 136 in the issue.
- **Williams, rest of the book.** I read pp. 100–102 only. A text search of the extracted OA PDF found no "Berthon" or "Pitt," and two uses of "mindful" (the p. 101 sentence and the index entry "mindfulness, 101"); the extraction may have missed OCR errors.
- **Berthon's wider record.** Coverage rests on the Crossref author search of facet Z (not exhaustive) and on OpenAlex. Books, book chapters and working papers by Berthon on technology, if they exist, were not searched for here. His Trajectories of Technology framework papers (the "ToT" the 2024 abstract cites) are not in the list and may bear on history of technology; none was found or opened.
- **The SFU release is secondary.** Its wording is Pitt's, in interview. It may differ from the paper in emphasis or detail.
- **Berthon on literacy and media history.** I found nothing in titles, abstracts or the three full texts. I cannot rule out a passage in the unopened papers.
