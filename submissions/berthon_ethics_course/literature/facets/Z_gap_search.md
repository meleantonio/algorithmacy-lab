# Facet Z: gap search (prior arguments from the literacy transition to AI; current AI-literacy rules; "algorithmacy" and its cousins; Berthon's record)

*Facet Z, 2026-10-13. Agent-drafted. The author has not reviewed it, and none of the text is the author's.*

## What this facet covers

Four questions, from `RESEARCH_PLAN.md` §5 and the lead's brief.

1. Who has already argued from the ethics or harms of the literacy (or print) transition to AI, platforms, algorithms or digital technology? That includes work that applies Graff's "literacy myth" to digital or AI literacy, critical-literacy and New Literacy Studies work that treats "digital literacy" as deficit framing, and AI-ethics work that uses literacy tests, colonial schooling or anti-literacy laws as a comparison.
2. How is "AI literacy" being written into rules and gates now? I record what each primary text requires and of whom. I do not evaluate.
3. Does anyone use "algorithmacy" or a close cousin, and what do they mean?
4. What has Pierre Berthon (Bentley) published on technology ethics, AI, attention or literacy beyond "Types of mindfulness in an age of digital distraction" (2019)?

**The question the synthesis answers.** Where does the paper's thesis (the global community failed ethically in the literacy transition and is repeating the pattern in the algorithmacy transition) sit relative to work that already exists, and what are the rules it must describe as of 13 October 2026?

Per §8, this facet carries the comparison that facets A to F may not. I keep it to what a source says; the lead adjudicates.

## Legend for read status

- **read in full**: I opened the whole text this session and the quotations come from it.
- **read in part**: I opened the named sections or pages only.
- **abstract only**: I saw the abstract (Crossref abstract field, a Consensus record, or a Semantic Scholar record). I paraphrase and do not quote beyond the abstract.
- **metadata only**: Crossref title, authors, venue; no text.
- **not accessible**: blocked or unavailable; the block is logged.

Locators for the UNESCO text are printed page numbers of the mirror copy; for the EC-OECD and OECD documents, printed page numbers; for statutes, article and recital numbers.

---

## (a) Search log

Queries that returned nothing are logged. "CR" = Crossref REST API, `query.bibliographic` (title/metadata match) unless noted. Hit counts for CR are the first 12 items I inspected, not total matches.

### Berthon (Q4)

| # | Source | Exact query | Hits | Notes |
| --- | --- | --- | --- | --- |
| 1 | CR | `query.author=Pierre Berthon`, rows=1000, offset 0/1000/2000 | 3,000 rows | Fuzzy; mostly other "Berthon"s. I kept records with an author "Pierre ... Berthon" and a co-author surnamed Pitt: 151 items, 1996 to 2023. |
| 2 | OpenAlex | `authors?search=Pierre Berthon` | 0 | Failed: "Rate limit exceeded ... daily budget ... used up"; resets midnight UTC. No OpenAlex cross-check was possible. |
| 3 | CR | author=Pierre Berthon + bibliographic: `artificial intelligence`; `ethics`; `attention digital`; `literacy`; `algorithm`; `digital addiction`; `ChatGPT generative`; `mindfulness`; `privacy surveillance`; `social media harm`; `truthiness fake news`; `AI`; `machine learning`; `technology society` | 3, 2, 2, **0**, **0**, 2, 1, 4, 1, 13, 7, 5, 5, 9 | "literacy" and "algorithm" returned no Berthon item. |
| 4 | CR | author=Pierre Berthon + bibliographic: `generative AI large language model`; `ethics responsibility`; `attention economy distraction`; `smartphone`; `digital wellbeing`; `algorithmic`; `human AI`; `explainability`; `education students AI`; `dark patterns manipulation`; `design experience`; `bias`; `regulation policy`; `brand AI`; `knowledge reading writing` | 13, 2, 4, **0**, 2, **0**, 7, 1, 8, **0**, 2, **0**, 2, 24, 7 | Filtered to Berthon, 2016 on. New items: Su 2023, Wang 2024/2025, Keaney 2025, Wang 2026, Du 2024, Berthon 2026 (two). |
| 5 | CR | `works/<doi>` for 20 Berthon DOIs | 20 resolved | Titles, authors, venues in the bib. |
| 6 | Unpaywall | 14 Berthon DOIs | 7 flagged OA | Of those, only Su et al. 2023 opened as text. The others hit bot walls or service errors (see (d)). |

### Q1: prior arguments

| # | Source | Exact query | Hits | Notes |
| --- | --- | --- | --- | --- |
| 7 | Scholar Gateway | `literacy myth Graff digital literacy AI literacy ethics` | 0 | `ACCESS_DENIED`, as in earlier runs. |
| 8 | Consensus | `AI literacy as deficit framing; critical comparison with historical literacy campaigns and the literacy myth` | 20 | Surfaced Kamperman and Graff 2026, Lund and Teel 2026, Shaw et al. 2024, Paljor et al. 2026, Shapiro et al. 2026, Yao and Lin 2026. |
| 9 | Consensus | `lessons from the history of mass literacy for artificial intelligence ethics and algorithmic governance` | 20 | Surfaced Rahm 2021, Kalantzis and Cope 2024, Burriss and Leander 2024, Bradley et al. 2024, Mohamed et al. 2020. |
| 10 | Consensus | `responsibilization: algorithmic literacy places burden on individual users instead of platforms` | 20 | Algorithmic-literacy empirical and review papers (Dogruel et al., Oeldorf-Hirsch and Neubaum, Gagrčin et al., König). |
| 11 | Consensus | `digital literacy discourse critique: deficit model, moral panic, literacy crisis rhetoric` | 20 | Nichols and Stornaiuolo 2019, Weninger 2023, Lea 2013, Hicks and Lloyd 2020, Tewell 2020, Bacalja et al., Gibson 2008. |
| 12 | Consensus | `AI literacy requirement as gatekeeping exclusion historical analogy to literacy tests or colonial education` | 20 | Mostly AI-literacy framework and review papers; no literacy-test comparison. Repeats Lund and Teel, Shaw et al., Bradley et al. |
| 13 | CR | `literacy myth digital literacy AI literacy Graff` | 12 | Hoffman 2026 (AERA); Graff's own 2010, 2017, 2022 pieces. |
| 14 | CR | `Graff literacy myth artificial intelligence` | 12 | Graff titles only; Katranci 2026 scale paper. |
| 15 | CR | `AI literacy deficit framing critique` | 12 | Mora and Yepes-Mora 2025; Velander et al. 2024; Dror et al. 2026 (SSRN). |
| 16 | CR | `New Literacy Studies AI literacy ideological model Street` | 12 | Street's own NLS pieces; Liebel 2021 (health literacy, autonomous vs ideological model); no AI-literacy hit. |
| 17 | CR | `digital literacy myth critique deficit` | 12 | Cole et al. 2024; Scolari 2019 ("digital native" myth). |
| 18 | CR | `the myth of digital literacy` | 12 | Same items; Tannen 1982 on orality and literacy. |
| 19 | CR | `AI literacy is the new literacy myth rhetoric` | 12 | Nothing new beyond Graff's pieces. |
| 20 | CR | `literacy tests voting rights comparison algorithmic AI` | 12 | Browne-Marshall 2016 on poll taxes and literacy tests; algorithmic-literacy papers; no item joins the two. |
| 21 | CR | `anti-literacy laws enslaved algorithmic oppression AI` | 12 | Willis 2023 (anti-Black literacy laws); Tanksley 2024 (AERA). |
| 22 | CR | `colonial schooling literacy lessons artificial intelligence education decolonial` | 12 | No item joins colonial schooling and AI literacy. |
| 23 | CR | `history of print ethics lessons artificial intelligence` | 12 | Cihon et al. 2020/2021 (AI governance, "design lessons from history"); Tokson 2026 (title only). |
| 24 | CR | `printing press Gutenberg analogy generative AI ethics regulation` | 12 | Neos 2026 (SSRN, "Gutenberg or the Great Firewall?"). |
| 25 | CR | `mass literacy history lessons for AI literacy policy` | 12 | Graff and Heath 2017 chapters; Ridley 2025 (SSRN). |
| 26 | CR | `compulsory schooling literacy campaign analogy artificial intelligence skills mandate` | 12 | Nothing relevant. |
| 27 | CR | `oversold promises literacy technology education returns AI` | 12 | Twining 2002 ("Oversold and underused": computers in classrooms); Bulger and Davison 2018; Yang 2026 (title only). |
| 28 | CR | `Eisenstein printing press generative AI comparison society` | 12 | Eisenstein items only. |
| 29 | arXiv API | `all:"AI literacy" AND all:"literacy myth"` | 0 | Empty feed. |
| 30 | WebSearch (extended) | `"AI literacy" "literacy test" Jim Crow OR "literacy tests" comparison gatekeeping AI skills requirement critique` | 9 | No source makes the comparison; Jim Crow quiz pages and AI-literacy scale reviews only. |
| 31 | WebSearch (extended) | `"AI literacy" "literacy myth" Graff critique schools AI literacy promises` | 9 | Black and Yasukawa 2014 (adult foundation skills; not AI); Holt 2026 Substack post (loose "literacy myth"). |
| 32 | WebSearch | `Kamperman Graff "On AI Literacy" Rhetorical and Historical Fallacies ... Change magazine` | 9 | Nothing retrieved about the article itself; a KU news item on a different Kamperman article. |
| 33 | CR `works/<doi>` | Kamperman and Graff 2026; Hoffman 2026; Mora and Yepes-Mora 2025; Shaw et al. 2024; Tanksley 2024 | 5 | Metadata and, for Kamperman and Graff and Shaw, the Crossref reference lists. |
| 34 | WebFetch | tandfonline `10.1080/00091383.2026.2706429` | 0 | HTTP 403. |
| 35 | WebFetch | SSRN abstract 5805364 (Neos) | 0 | HTTP 403. |
| 36 | WebFetch | `doi.org/10.1145/3796496.3811753` (Paljor) | 0 | Redirect to dl.acm.org; PDF fetch returned a bot challenge. |

### Q3: "algorithmacy" and cousins

| # | Source | Exact query | Hits | Notes |
| --- | --- | --- | --- | --- |
| 37 | CR | `algorithmacy` | **0** | |
| 38 | CR | `algoracy` | **0** | |
| 39 | CR | `algorithmic competence` | 12 | Education items on pupils' "algorithmic thinking/competence" (mathematics teaching), plus Ayasrah et al. 2026 (teachers' "AI-algorithmic competence"). Titles only. |
| 40 | CR | `algorithmic literacy definition` | 12 | Moss 2023 (AERA), Ehret 2024, Shultz Colby 2024. |
| 41 | CR | `algorithmic numeracy` | 12 | Only the journal *Numeracy*; nothing on algorithms. |
| 42 | CR | `algorithmic awareness literacy users` | 0 | HTTP 429 rate limit. Not retried. |
| 43 | WebSearch (extended) | `"algorithmacy"` | 9 | Results are the author's Substack posts, two GitHub mirrors of the lab, and algorithmacy.org; plus a paper titled "Designing for Critical Algorithmic Literacies" (arXiv 2008.01719) in the result list. I did not open any of them. |
| 44 | WebSearch | `"algoracy" OR "algorithmeracy" OR "algorithmic literacy" definition Dogruel Masur Joeckel "algorithm literacy"` | 9 | No hit for "algoracy" or "algorithmeracy". |
| 45 | Download | ssoar.info Dogruel, "What is Algorithm Literacy?" | 0 | Bot challenge ("Making sure you're not a bot"). Not circumvented. |

### Q2: rules and gates

| # | Source | Exact query / URL | Hits | Notes |
| --- | --- | --- | --- | --- |
| 46 | EUR-Lex | `eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32024R1689` and `.../eli/reg/2024/1689/oj/eng` | 0 | HTTP 202, empty body (AWS challenge). WebFetch also returned an empty page. Not circumvented. |
| 47 | Publications Office | `publications.europa.eu/resource/celex/32024R1689`, `Accept: application/xhtml+xml` | 1 | Official Journal text, 1.26 MB XHTML. Used for the AI Act. |
| 48 | WebSearch | `Digital Omnibus proposal amend Article 4 AI Act AI literacy ...` | 9 | Reported that Article 4 had been amended. I then fetched the primary text (row 49). The press summaries were not used as sources. |
| 49 | Publications Office | `.../celex/32026R1744`, XHTML | 1 | Regulation (EU) 2026/1744, OJ L 24.7.2026. |
| 50 | unesdoc | `.../ark:/48223/pf0000391105/PDF/391105eng.pdf.multi`, and `...391104...` | 0 | Cloudflare "Just a moment". |
| 51 | WebFetch | `unesdoc.unesco.org/ark:/48223/pf0000391105` and `.locale=en` | 0 | HTTP 403. |
| 52 | unesco.org | `/en/articles/ai-competency-framework-students`, `/digital-education/ai-future-learning/competency-frameworks` | 0 | CAPTCHA page. Not circumvented. |
| 53 | raise.mit.edu, policycommons.net | PDF mirrors | 0 | 404; 403. |
| 54 | archive.org Wayback availability | unesdoc PDF URLs | 0 | HTTP 429. Not retried. |
| 55 | WebSearch | `"AI competency framework for students" UNESCO ... pdf full text` | 10 | Pointed to an unofficial copy at youthguards.com, which I opened (80 pp., carries UNESCO's ISBN and DOI 10.54675/JKJB9835). Treated as a mirror, flagged in the bib. |
| 56 | WebSearch | `PISA 2029 Media and Artificial Intelligence Literacy assessment OECD European Commission framework` | 9 | Led to the draft framework; a copy on naer.edu.tw opened (63 pp.). oecd.org not opened. |
| 57 | WebSearch + WebFetch + download | `OECD European Commission AI Literacy Framework ... final version 2026`; `ailiteracyframework.org` | 10 | Found the final PDF; opened (64 pp.). |
| 58 | WebSearch + download | `executive order "Advancing Artificial Intelligence Education for American Youth"` | 10 | govinfo DCPD-202500511 opened. |
| 59 | WebSearch + download | `Department of Labor "Artificial Intelligence Literacy Framework" ...` | 9 | DOL PDF and press release: "Access Denied". Opened the CRS Insight IN12715 instead. |
| 60 | WebFetch / curl | `oaa.osu.edu/ai-fluency` | 1 | Opened as raw HTML. |
| 61 | WebSearch | `China Ministry of Education AI general education ... Beijing ... 8 class hours` | 10 | Xinhua (gov.cn) and China Daily pages opened. National MoE notice not opened. |
| 62 | WebSearch + curl | Shopify CEO memo on "reflexive AI usage" | 9 | Only secondary coverage; Digital Commerce 360 returned HTTP 403. Memo text not obtained. |

---

## (b) Entries

Order: (1) closest prior work and the literacy-critical literature; (2) algorithmic-literacy definitions; (3) rules and gates; (4) Berthon.

### B1. Kamperman and Graff, "On 'AI Literacy': The Rhetorical and Historical Fallacies of a Movement and Its Marketing" (2026)

- **Reference.** Kamperman, Sean, and Harvey J. Graff. 2026. *Change: The Magazine of Higher Learning* 58(4): 34-39. DOI 10.1080/00091383.2026.2706429. Bib key `kamperman2026ai`.
- **Verified how.** Crossref `works/<doi>`: title, two authors, volume 58, issue 4, pages 34-39, published 4 July 2026, 17 references.
- **Read status.** *Metadata only* plus the Crossref reference list. *Not accessible*: tandfonline HTTP 403; Unpaywall `is_oa=false`. I have not read a word of the article.
- **What the record shows.** The co-author is the historian who coined the literacy myth. The Consensus record snippet reads: "'Artificial intelligence [AI] literacy' initiatives in higher education too often conflate technology skills with reading and writing, obscuring the complex ways AI and literacy interact" (Consensus record, truncated "In Short" blurb; I did not see the article).
- **Reference list (Crossref, items I read).** Graff 2023a and 2023b (*The Literacy Myth*; *Literacy Myths, Legacies, and Lessons*, WAC Clearinghouse); Lewis 2015 (*Strategic Discourse: The Politics of (New) Literacy Crises*); OECD 2025 (EC-OECD AI literacy framework, draft); UNESCO 2024 (AI competency framework for teachers); US Department of Labor 2026 (AI Literacy Framework); the AI Action Plan 2025; Ohio State "AI Fluency" page (13 Feb 2026); a DeVry item (*Inside Higher Ed*, 30 Jan 2026); *The Economist* 22 Jan 2026 ("Ed tech is profitable. It is also mostly useless."); Johnson 2023 (on another literacy "crisis"). The authors therefore engage the same policy documents this facet records in section 2.
- **Scale.** Not known. Higher education and US policy, judging by the references.
- **Bearing on §4.** *Problem 5 (the myth cuts both ways)*: the reference list shows Graff's thesis aimed at AI-literacy promotion. Whether the article makes the ethical-failure argument, the withholding, gating and imposition arguments, or only the overselling argument is **not found** in anything I opened. This is the nearest prior work and it is unread. A human with Bentley library access should read it before the paper claims any position relative to it.

### B2. Lund and Teel, "AI Literacy: An Exercise in Power-Knowledge" (2026)

- **Reference.** Lund, Brady D., and Zoë Abbie Teel. 2026. arXiv:2607.27547. DOI 10.48550/arxiv.2607.27547. Key `lund2026ai`.
- **Verified how.** Downloaded `arxiv.org/pdf/2607.27547` (8 pp., AAAI template). Consensus had listed "Brady D. Lund et al."; the PDF title block gives Lund and Teel, University of North Texas.
- **Read status.** *Read in full* (text extraction; sections cited by heading, no printed page numbers in the arXiv layout).
- **What it argues.** Current AI-literacy frameworks teach a "competent consumer"; the paper wants literacy as critical practice and participation in governance (Freire, Foucault). It also argues that unequal access to AI tools reproduces "longstanding epistemic injustices."
- **Quotations.**
  - "From early debates over print literacy in the 18th and 19th centuries, the question of who should be taught to read – and to what end – has been bound up with questions of social power (Houston 1983)." (Introduction, section "Literacy as Empowerment")
  - "What is notably absent from these existing AI literacy frameworks is a robust account of power (Stamboliev 2023)." (Introduction)
  - "The gap between these users is not closed by AI. To the contrary, it may well be widened." (section "Democratization and Its Contradictions")
  - "They are trained, as Freire would put it, to adapt to the world rather than to transform it." (section "AI Literacy as Empowerment, Not Competency")
- **Scale.** Global in framing (geopolitical access paragraph); evidence is conceptual.
- **Bearing on §4.** Uses one historical item (print literacy and "who should be taught to read") in one sentence, then turns to Freire. It cites no documented wrong of the transition (no statute, no test, no school regime). It does not use Graff, literacy tests, colonial schooling or anti-literacy laws (a search of the extracted text for "Graff", "literacy myth", "literacy test", "anti-literacy" and "Jim Crow" returned no match; "colonial" appears only in two reference-list entries). *Complicates* problem 1 (it asserts the power link without the record) and *supports* the claim that a critique of competency-model AI literacy already exists.

### B3. Shaw, Toliver and Tanksley, "The Internet Doesn't Exist in the Sky: Literacy, AI, and the Digital Middle Passage" (2024)

- **Reference.** *Reading Research Quarterly* 59(4): 690-705. DOI 10.1002/rrq.537. Key `shaw2024internet`.
- **Verified how.** Crossref (three authors; 61 references listed).
- **Read status.** *Abstract only* (Crossref abstract, read in full). Not open.
- **What the abstract says.** A speculative and visual narrative about AI, "algorithmic oppression" and Black girls in schooling in the US and Haiti, offered as "a thought experiment on how literacy studies might refuse the oppressionist logics currently undermining the possibilities of AI in literacy education." The title frames digital infrastructure through the Middle Passage.
- **Scale.** US and Haiti.
- **Bearing on §4.** An ethics-of-harm argument about AI in literacy education that reaches back to slavery as a frame. Whether it invokes anti-literacy laws or any literacy-transition history is **not found** at abstract depth. Reference list (Crossref) shows Benjamin 2019, Crawford 2021, Brock 2020, Morozov 2013 and others; no entry that reads as a history of literacy among the first 40 I saw. *Supports* "someone has used slavery-era harms as a frame for AI in literacy education"; does not show a literacy-transition argument.

### B4. Hoffman, "Echoes of Urgency: Comparing Calls for AI Literacy, Financial Literacy, and Digital Literacy" (2026)

- **Reference.** *Proceedings of the 2026 AERA Annual Meeting*. DOI 10.3102/2281796. Key `hoffman2026echoes`.
- **Read status.** *Metadata only*. Crossref has no abstract; Unpaywall `is_oa=false`. **Not accessible.**
- **Why listed.** The title announces a comparison of the rhetoric of urgency across three "literacies." The content is unknown; it may be the nearest peer-reviewed counterpart to Problem 5 (overselling).

### B5. Mora and Yepes-Mora, "Framing a Critical, Historical, Proactive View of AI Literacies in 'Zero-Gravity' Spaces" (2025)

- **Reference.** In *Reimagining Literacy in the Age of AI*, Chapman and Hall/CRC, pp. 170-191. DOI 10.1201/9781003510635-13. Key `mora2025framing`.
- **Read status.** *Metadata only*; **not accessible.** The title promises a "historical" view; the content is unknown.

### B6. Critical-literacy and NLS work on "digital literacy" and "AI literacy" as discourse (abstract only)

All verified in Crossref; all read at abstract depth through Consensus records; none opened.

- **Nichols and Stornaiuolo 2019** (`nichols2019assembling`, *Media and Communication* 7(2), DOI 10.17645/mac.v7i2.1946). Traces the genealogy of "digital literacy" to show that earlier concerns about "technical infrastructures and socio-economic relations" were dropped in favour of "the interplay of users, devices, and content" (abstract). Scale: concept history in education research.
- **Weninger 2023** (`weninger2023digital`, ELT Journal, 10.1093/elt/ccad001). "Digital literacy as ideological practice"; the abstract says digital literacy is "fundamentally, an ideological practice" and critiques "the prevalent focus on skills."
- **Lea 2013** (`lea2013reclaiming`, 10.1080/13562517.2012.756465). "Digital literacies" used "rhetorically" to "promote competency-based agendas"; teachers positioned "in deficit" (abstract).
- **Hicks and Lloyd 2020** (`hicks2020deconstructing`, 10.1177/0961000620966027); **Tewell 2020** (`tewell2020problem`, 10.1353/pla.2020.0007). Deficit framing in information-literacy instruction (abstracts).
- **Bacalja et al. 2021** (`bacalja2021critical`, handbook chapter, 10.4324/9781003023425-43). Critical digital literacy, "following the precedents set by" NLS (abstract).
- **Gibson 2008** (`gibson2008beyond`, 10.1177/1329878x0812800109). "Beyond Literacy Panics: Digital Literacy and Educational Optimism"; literacy-crisis rhetoric around digital literacy (abstract).
- **Yao and Lin 2026** (`yao2026reframing`, 10.1057/s41599-026-07496-2). Argues dominant digital-literacy frameworks show "context blindness" and "power unconsciousness" and cause "cultural-cognitive injustices" in the Global South (abstract). Scale: Global South framing.
- **Shapiro et al. 2026** (`shapiro2026metacognitive`, 10.1080/17439884.2026.2652638). Conventional AI-literacy frameworks are "anchored in functional skills acquisition"; proposes a metacognitive social practice (abstract).
- **Paljor et al. 2026** (`paljor2026preparing`, 10.1145/3796496.3811753). Argues that when ethics is supplemental, AI literacy "prepares learners for compliance with AI systems rather than for critical, plural, and community-accountable participation," and that it "risks displacing responsibility for AI harms away from institutions and educational structures onto individual learners" (abstract). This is a responsibilization argument close to Problem 5 and to the gating question, with no historical comparison in the abstract.
- **Kalantzis and Cope 2024** (`kalantzis2024literacy`, RRQ, 10.1002/rrq.591). Treats generative AI as "perhaps as momentous ... as Pi Sheng's invention of moveable type and Gutenberg's printing press—and in its peculiar ways just as problematic" (abstract). This is a print-to-AI analogy in the literacy-education literature; the abstract names no ethical failure of the print era.
- **Burriss and Leander 2024** (`burriss2024critical`, RRQ, 10.1002/rrq.565). Critical posthumanist literacy for "reading, writing, and living ethically with everyday artificial intelligence" (abstract).
- **Bradley et al. 2024** (`bradley2024denaturalizing`, RRQ, 10.1002/rrq.540). AI as "a means to unsettle the hierarchies of intelligence"; "anti-colonial literacies" in higher education (abstract).
- **Rahm 2021** (`rahm2021education`, LMT, 10.1080/17439884.2021.1977948). A genealogy from the 1950s showing education "mobilized as an important tool for governance in computer policies" (abstract). Scale: national policy discourse; nearest to the "literacy as the policy answer to technology" pattern, but computer-era not literacy-era.
- **Mohamed, Png and Isaac 2020** (`mohamed2020decolonial`, 10.1007/s13347-020-00405-8). Decolonial theory for AI "using historical hindsight" (abstract); cited by Su, Wang and Berthon 2023.

**Common finding for B3 to B6.** In every abstract, the historical move is made to colonialism, slavery or earlier "digital literacy" discourse. In none does the abstract join the documented ethical wrongs of the alphabetic literacy transition (withholding, gating, imposing, overselling) to AI. Abstract depth cannot rule out that a full text does.

### B7. Holt, "AI Literacy Is a Comforting Lie" (2026)

- `holt2026ai`. Substack post, 1 Feb 2026. *Read in full.* Non-scholarly. Section heading: "The cost of the literacy myth." It uses "literacy myth" to mean the assumption that AI use is a stable competence, and contrasts print: "That framing made sense for print." It does not cite Graff. *Does not bear* on Problem 5 in Graff's sense. Logged because a web search for "AI literacy" + "literacy myth" returns it first.

### B8. Black and Yasukawa, "The literacy myth continues" (2014)

- `black2014literacy`, *Critical Studies in Education* 55(2), DOI 10.1080/17508487.2014.904809. *Metadata only* (title seen in a search result; not opened). By title it applies Graff's thesis to "contemporary policy discourses on adult 'foundation skills' in Australia." It is a precedent for carrying the literacy myth into current policy; AI is not in the title.

### B9. Algorithmic-literacy definitions (Q3)

**B9a. Ridley and Pawlick-Potts 2021** (`ridley2021algorithmic`, *Information Technology and Libraries* 40(2), DOI 10.6017/ital.v40i2.12963). *Read in full* (15 pp.).
- Definition (pdf p. 4, section "Defining algorithmic literacy"): "Algorithmic literacy is the skill, expertise, and awareness to / Understand and reason about algorithms and their processes / Recognize and interpret their use in systems (whether embedded or overt) / Create and apply algorithmic techniques and tools to problems in a variety of domains / Assess the influence and effect of algorithms in social, cultural, economic, and political contexts / Position the individual as a co-constituent in algorithmic decision-making."
- It builds on Scribner and Cole: "literacy = practices + symbol system + technology" (pdf p. 4).
- On need (section "Why algorithmic literacy?"): "Algorithmic literacy is needed to acknowledge both the technology's power (control) over people and power (empowerment) for people."
- Scale: library and information science; names the GDPR "right to explanation" and Finland's "Elements of AI" course.
- Bearing: a definition of an individual competence about algorithms. The competence to coordinate with another person through an algorithmic third party that commits outcomes binding on both is not stated in it. Its last bullet ("co-constituent in algorithmic decision-making") is the nearest.

**B9b. Dogruel, Masur and Joeckel 2021** (`dogruel2021development`, 10.1080/19312458.2021.1968361). *Abstract only.* Two dimensions: "awareness of algorithms use" and "knowledge about algorithms," 11 items each (Consensus abstract).

**B9c. Others** (abstract only): Cox 2024 (`cox2024algorithmic`; reviews definitions of algorithmic, AI and generative-AI literacy); Oeldorf-Hirsch and Neubaum 2023 (`oeldorf2023what`; a research agenda including "balancing users' expectations of algorithmic literacy with developers' responsibility for algorithmic transparency" and "addressing the new algorithmic divide"); Gagrčin et al. 2024 (`gagrcin2024algorithmic`; 169-paper review); König 2022 (`koenig2022challenges`; user control "demands an algorithmic literacy that also entails a certain way of making oneself knowable").

**B9d. "Algorithmacy" and "algoracy."** CR returned 0 for both (rows 37, 38). The web search for "algorithmacy" (row 43) returned the author's own Substack posts, two GitHub copies of the lab and algorithmacy.org (a conference page); I did not open any of them. The search summary described the term as "a recent, niche term, mostly used by one author." Within what I opened, **no independent use of "algorithmacy" exists.** "Algorithmic competence" appears in education titles as pupils' or teachers' skill with algorithms as procedures (titles only; not opened).

**B9e. Moss 2023** (AERA, "Critical Algorithmic Literacy: Addressing Algorithmic Epistemological Authority for K-12 Students"), **Ehret 2024** (`Literacy` 10.1111/lit.12363), **Tanksley 2024** (`tanksley2024critical`): metadata only; titles show "critical algorithmic literacy" is an existing label in literacy-education research. Not opened.

### B10. Rules and gates (Q2). Record only.

**R1. Regulation (EU) 2024/1689 (AI Act), as published 12.7.2024.** Key `euaiact2024`. *Read in part*: Art. 3(56), Art. 4, Art. 99, Art. 113, recitals 20 and 91, via the Publications Office XHTML copy of the Official Journal (EUR-Lex itself was blocked).

- **Article 4, "AI literacy"** (complete): "Providers and deployers of AI systems shall take measures to ensure, to their best extent, a sufficient level of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used."
- **Of whom.** The duty falls on providers and deployers; the literate parties are "their staff and other persons dealing with the operation and use of AI systems on their behalf." Article 4 does not impose a duty on persons who are subject to AI systems.
- **Definition, Art. 3(56):** "'AI literacy' means skills, knowledge and understanding that allow providers, deployers and affected persons, taking into account their respective rights and obligations in the context of this Regulation, to make an informed deployment of AI systems, as well as to gain awareness about the opportunities and risks of AI and possible harm it can cause."
- **Recital 20** (in part): "AI literacy should equip providers, deployers and affected persons with the necessary notions to make informed decisions regarding AI systems." And "in the case of affected persons, the knowledge necessary to understand how decisions taken with the assistance of AI will have an impact on them." And: "the Commission and the Member States should facilitate the drawing up of voluntary codes of conduct to advance AI literacy among persons dealing with the development, operation and use of AI."
- **Related use, recital 91:** "deployers should ensure that the persons assigned to implement the instructions for use and human oversight ... have the necessary competence, in particular an adequate level of AI literacy, training and authority to properly fulfil those tasks."
- **Application date, Art. 113:** "Chapters I and II shall apply from 2 February 2025." Article 4 sits in Chapter I.
- **Penalty.** Article 99(4) lists the provisions whose breach carries fines up to EUR 15,000,000 or 3 % of turnover; it names Articles 16, 22, 23, 24, 26, 31 (with 33 and 34) and 50. **Article 4 is not on the list.** I did not read Article 99(5) to (7) or any Member State penalty rules. Whether a national penalty attaches to Article 4: **not found.**

**R2. Regulation (EU) 2026/1744 (Digital Omnibus on AI), OJ L, 24.7.2026.** Key `euomnibus2026`. *Read in part* (recital 8; Art. 1(5); Art. 4).

- Adopted at Strasbourg, "Done at ... 8 July 2026." Article 4 (entry into force): "This Regulation shall enter into force on the third day following that of its publication in the Official Journal." By my arithmetic from the OJ date of 24.7.2026 that is 27 July 2026; the text does not state a date.
- **Replacement Article 4** (point (5) of Art. 1): "1. Providers and deployers of AI systems shall take measures to support the development of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf, taking into account their technical knowledge, experience, education and training and the context the AI systems are to be used in, and considering the persons or groups of persons on whom the AI systems are to be used. This obligation does not require providers or deployers to guarantee any specific level of AI literacy of any individual. 2. The Commission and the Member States shall support and facilitate the efforts of providers and deployers of AI systems, in particular SMEs, in fulfilling their obligation under paragraph 1 of this Article. ... 3. The Board shall adopt recommendations, taking into account European competence frameworks, to support the Commission and Member States in the promotion of AI literacy required under paragraph 1, including by setting out common objectives."
- **Stated reason, recital 8** (in part): "experience shared by stakeholders reveals that a solution imposing stringent obligations to ensure a sufficient level of AI literacy would not be suitable for all types of providers and deployers" and "imposing such obligations creates an additional compliance burden, particularly for smaller enterprises."
- **Status.** The duty on providers and deployers is now to "support the development of" literacy, with no guaranteed level. I did not read the rest of the Omnibus (other amendments to Chapters III to V).

**R3. UNESCO, *AI competency framework for students* (2024).** Key `unesco2024students`. *Read in full*, via an unofficial mirror (unesdoc blocked). Printed page numbers.

- **Status of the text.** A framework "to help educators" integrate AI learning into "official school curricula" (Short summary). It is not a legal instrument; I saw no binding language.
- **Structure** (Short summary): "12 competencies across four dimensions: Human-centred mindset, Ethics of AI, AI techniques and applications, and AI system design. These competencies span three progression levels: Understand, Apply, and Create."
- **Of whom, by level** (p. 20): "Level 1: Understand. This first level is designed for all students. ... All students must therefore develop the human-centred values, knowledge and skills needed to engage in a safe, informed and meaningful manner in their daily interaction with AI in various spheres of life." Level 2 "Apply": "relevant for all school students." (p. 20). Level 3 "Create": "For students who do not have a strong interest in pursuing deeper study in the field, the learning outcomes at this level, in particular under the 'AI system design' aspect, should be offered as elective programmes rather than as compulsory requirements for all students." (p. 21). On exit at Level 2: "For many, 'Apply' at Level 2 will be the point of exit for their AI-related competency development, at least at school." (p. 21)
- **Inclusion text** (section 2.4, p. 16): "Access to AI and AI competencies represent the two sides of citizens' basic rights in today's world. All students should have inclusive access to the environments required for learning about AI at the basic level." And: "engagement with AI without access to the internet and AI tools will limit the scope and mastery level of AI competencies."
- **State of adoption, 2022** (section 1.1, p. 12): "according to a recent survey conducted across 190 countries, only some 15 countries were found to be developing or implementing AI curricula in school education (UNESCO, 2022b)." I did not open UNESCO 2022b.
- **Not opened:** UNESCO *AI competency framework for teachers* (2024; cited in Kamperman and Graff's reference list).

**R4. OECD and European Union, *Empowering Learners for the Age of AI: An AI Literacy Framework for Primary and Secondary Education* (2026).** Key `oecd2026empowering`. *Read in part* (front matter, definition, scope; 64 pp.).

- **Status.** "This framework is non-binding and is intended to support teachers, school leaders and education authorities" (p. 1). "For the OECD, this work was approved and declassified by the PISA Governing Board (PGB) on 8 April 2026" (copyright page). Final version of the May 2025 draft.
- **Definition** (p. 5): "AI literacy represents the technical knowledge, durable skills and future-ready attitudes required to thrive in a world influenced by AI. It enables learners to engage, create with, manage and shape AI, while critically evaluating its benefits, risks and ethical implications." Four domains, in the contents listing: Engage with AI, Create with AI, Manage AI, Shape AI; the contents list "Competences and Learner Expectations" at pp. 25-43.
- **Link to assessment** (p. 1): "The AILit Framework contributes to the PISA 2029 Media & Artificial Intelligence (MAIL) Literacy assessment."
- **Of whom:** learners in primary and secondary education; addressed to teachers, school leaders, authorities.

**R5. OECD, first draft of the PISA 2029 Media and AI Literacy (MAIL) Assessment Framework (2026).** Key `oecd2026pisamail`. *Read in part* (63 pp. mirror).

- **Status.** "The following document is a preliminary draft. The PISA 2029 Media and Artificial Intelligence Literacy (MAIL) will be subject to revisions before the final version is released." (Note to the Reader, p. 2)
- **Definition** (p. 25): "The PISA 2029 Innovate Domain Assessment defines Media and Artificial Intelligence Literacy (MAIL) as a set of competences required to engage effectively, ethically and responsibly with digital content, media platforms, and AI systems."
- **Purpose** (p. 8): "The new PISA Assessment of Media and AI Literacy (MAIL) represents a valuable tool to provide insights into the extent to which young students have acquired the skills necessary to engage proactively and critically within environments increasingly influenced by media platforms and AI systems." And (p. 8) "The fundamental step for tackling these challenges ... is to develop Media and AI Literacy."
- **Resources** (p. 23): "Many schools lack sufficient resources and digital devices which makes access to media literacy opportunities challenging ... Education systems must then rise to the challenge by embedding the principles of Media and AI Literacy across curricula, ensuring equitable access to resources."
- **Not found in the draft text I read:** the age of the tested students (searched "15-year", "15 year", "fifteen", "age 15": no match); any consequence for individual students; a reporting date. The five competence areas the draft names are Access and Use, Analyse and Evaluate, Participate and Collaborate, Create, and Reflect and Act Ethically and Responsibly (definition boxes; progression tables 4.1 to 4.5 at pp. 27-35).

**R6. Executive Order 14277, "Advancing Artificial Intelligence Education for American Youth," 23 April 2025.** Key `eo14277`. *Read in part* (Sections 1 to 4(a)).

- Sec. 2: "It is the policy of the United States to promote AI literacy and proficiency among Americans by promoting the appropriate integration of AI into education, providing comprehensive AI training for educators, and fostering early exposure to AI concepts and technology to develop an AI-ready workforce and the next generation of American AI innovators."
- Sec. 1: "we can ensure that every American has the opportunity to learn about AI from the earliest stages of their educational journey through postsecondary education."
- Sec. 4(a) creates the White House Task Force on Artificial Intelligence Education, chaired by the Director of the Office of Science and Technology Policy. No student requirement or test in the sections I read.

**R7. US Department of Labor, AI Literacy Framework (February 2026), as described in CRS Insight IN12715 (20 July 2026).** Key `crs2026workforce`. CRS text *read in full* (2 pp.); the DOL text is *not accessible* ("Access Denied").

- CRS: "Federal workforce funding grantees are not required to engage in the recommended activities or use the provided framework." "In February 2026, DOL issued an AI Literacy Framework. The guidance document discusses the applicability of the framework to state and local agencies (including WIOA grantees), education and training providers, employers, and individual workers." "The 11-page framework is divided into 'foundational content areas of AI literacy' and 'delivery principles of AI literacy.'"

**R8. Beijing Municipal Education Commission work plan (March 2025) and Curriculum Outline (June 2025), as reported.** Keys `xinhua2025beijing`, `chinadaily2025beijing`. News items *read in full*; the plans themselves *not accessible*.

- Xinhua, 12 March 2025: "Starting from the upcoming fall semester, schools across the Chinese capital will offer at least eight class hours of AI instruction per academic year. These courses can either be delivered independently or integrated with other subjects."
- China Daily, 4 July 2025: "Skills related to AI applications will also be included in students' comprehensive assessments." The outline "will focus on three areas: AI awareness and cognitive abilities, AI applications and innovation capabilities, as well as ethics and social responsibility related to AI."
- Scale: one municipality. Other provinces: **not found** in anything I opened. The national Ministry of Education notice (December 2024) is mentioned by Xinhua; not opened.

**R9. The Ohio State University, "AI Fluency" (web page, 2026).** Key `osu2026aifluency`. *Read in full.*

- "The initiative will ensure that every Ohio State student, beginning with the class of 2029, will graduate being AI fluent — fluent in their field of study, and fluent in the application of AI in that field." "All undergraduates will develop foundational generative AI skills through the required General Education Launch Seminar and participate in GenAI workshops integrated into the First Year Success Series."
- Assessment or enforcement of the "fluent" status: **not found** on the page.

**R10. Employer requirements.** The only employer-addressed text I opened is R1 (EU duties on employers as deployers) and R7 (as described by CRS). A widely reported Shopify CEO memo (April 2025) that makes "reflexive AI usage" a "baseline expectation" appears in search summaries only; I did not obtain its text (Digital Commerce 360: HTTP 403). **Not found** as a quotation. No employer job-requirement data were collected.

### B11. Berthon: what I can verify (Q4)

Method: Crossref author search (3,000 rows, relevance-ranked; rows 1 to 5), filtered to "Pierre ... Berthon". Identity as Bentley's Berthon is inferred from co-authors (Pitt, Wang, Pehlivan, Rabinovich, DesAutels) and, for two records, an affiliation field (Crossref lists a "McCallum Graduate School of Business, Be..." entry for the 2018 *Journal of Macromarketing* paper and "Bentley University Department of Experie..." for the 2026 *Journal of Services Marketing* paper; both strings are truncated in the record). OpenAlex was unavailable, so there is no second database. Coverage is not exhaustive.

| Year | Item | DOI | Venue | Read status |
| --- | --- | --- | --- | --- |
| 2016 | Wang, Berthon, Pitt, McCarthy, "Service, emotional labor, and mindfulness" | 10.1016/j.bushor.2016.07.002 | *Business Horizons* 59(6) | metadata only |
| 2018 | Berthon and Pitt, "Brands, Truthiness and Post-Fact" | 10.1177/0276146718755869 | *Journal of Macromarketing* 38(2) | not accessible |
| 2019 | Berthon and Pitt, "Types of mindfulness in an age of digital distraction" (the known item) | 10.1016/j.bushor.2018.10.003 | *Business Horizons* 62(2) | abstract only |
| 2019 | **Berthon, Pitt, Campbell, "Addictive De-Vices: A Public Policy Analysis of Sources and Solutions to Digital Addiction"** | 10.1177/0743915619859852 | *Journal of Public Policy & Marketing* 38(4): 451-468 | abstract read in full; paper not open |
| 2019 | Berthon, Pehlivan, Yalcin, Rabinovich, "True, fake and alternative: a topology of news and its implications for brands" | 10.1108/jpbm-11-2018-2142 | *J. Product & Brand Management* 29(2) | metadata only |
| 2022 | Berthon, Chohan, Pehlivan, Rabinovich, "Fixing fake news: ..." | 10.1016/j.bushor.2022.07.006 | *Business Horizons* 65(6) | metadata only |
| 2023 | **Su, Wang, Berthon, "Ethical Marketing AI? A Structured Literature Review of the Ethical Challenges Posed by Artificial Intelligence in the Domains of Marketing and Consumer Behavior"** | 10.24251/hicss.2023.603 | HICSS-56 | **read in full** |
| 2024 | **Berthon, Yalcin, Pehlivan, Rabinovich, "Trajectories of AI technologies: Insights for managers"** | 10.1016/j.bushor.2024.03.002 | *Business Horizons* 67(5): 461-470 | not accessible |
| 2024 | Wang, Berthon, Su, "Sensemaking and Sustainability: A Sensemaking Perspective on the Ethical Use of Big Data in Marketing Strategizing" | 10.1007/978-3-031-72676-7_7 | book chapter | not accessible |
| 2024 | Du, Svizzero, Berthon, "Understanding Ageism in Tech: A Model and Propositions" | 10.1109/mitp.2024.3501612 | *IT Professional* | not accessible |
| 2025 | **Wang, Berthon, Su, "Rethinking AI and Big Data in Marketing Strategy: Emphasizing Ethics through a Sensemaking Perspective"** | 10.24251/hicss.2025.622 | HICSS-58 | not accessible (service unavailable) |
| 2025 | **Keaney and Berthon, "Balancing explainability and privacy in AI systems: A strategic imperative for managers"** | 10.1016/j.bushor.2025.10.004 | *Business Horizons* | not accessible |
| 2026 | Wang, Berthon, John, "The refined interaction value framework: ... human-AI service systems in the AI-era" | 10.1108/jsm-12-2025-0888 | *J. Services Marketing* | metadata + partial abstract |
| 2026 | Berthon, DesAutels, Rabinovich, Weinberg, "Reimagining customer experience as a 4E cognitive ecology in phygital service ecosystems" | 10.1108/jsm-06-2026-0516 | *J. Services Marketing* | metadata only |
| 2026 | Berthon, DesAutels, Divekar, "Field-Ready HCI: ... Agriculture for Low-Resource and Smallholder Contexts" | 10.3390/app16146985 | *Applied Sciences* | metadata only |

**What I read.**

- **Addictive De-Vices (abstract, Crossref).** "This addiction is both akratic (we are aware of the negative consequences) and engineered (designed on purpose). Marketers are complicit in this engineering ... The authors then turn to policy solutions and discuss how informing, guiding, and restricting can help ameliorate the problem and promote the public good." Scale: consumer-policy, US-weighted by venue (not stated). Bearing: a harms-and-policy argument on digital technology by Berthon; "informing" is one of three listed remedies. No literacy history in the abstract.
- **Types of mindfulness (abstract, Semantic Scholar, truncated).** "In an age of digital distractions, mindfulness has become a billion-dollar industry ... it is incumbent upon managers to understand the phenomenon of mindfulness." Remainder not seen.
- **Su, Wang and Berthon 2023 (read in full).** Abstract: "From privacy issues, through discrimination of marginalized groups, to emergent systemic social distortions, AI is changing the marketing ethical landscape." Clusters: "algorithm, society and existential." On the digital divide (pdf p. 6 of 10): "A well-established ethical concern focuses on the digital divide (McSorley, 2003). This concerns the divides between countries, genders, and ages, between rural and urban. AI can exacerbate each of these divides. Those who cannot access the underlying technology will miss the benefits." Same page: "digital technologies function in ways that perpetuate racial and colonial structures." A search of the extracted text for "literacy" returned no match; the paper contains no historical argument from literacy or print.

**Finding for Q4.** Beyond the 2019 mindfulness paper, Berthon has publications verified in Crossref on digital addiction and public policy (2019), fake news and truthiness (2018 to 2022), AI ethics (2023, 2024, 2025) and explainability and privacy (2025). I found **no Berthon publication with "literacy" in its title or Crossref metadata**, and none of the full or abstract texts I read argues from the history of literacy or print. The Business Horizons "Marketing & Technology" series (the 2019 mindfulness paper says it is "this installation of Marketing & Technology") is a possible venue register for the course.

---

## (c) Synthesis by question

### Q1. Who has already argued from the literacy (or print) transition to AI, platforms or digital technology?

I found **no work that** joins the documented ethical failures of the literacy transition (withholding it, gating civic standing on it, imposing it at the cost of other ways of life, overselling its returns) to a present ethical critique of AI, platforms or algorithms, **in** Crossref (22 title/metadata queries, rows 13 to 28 and 37 to 41), Consensus (5 queries), arXiv (1 query), and web search (rows 30 to 32) as of 13 October 2026. Three qualifications bind that statement.

1. **The nearest candidate is unread.** Kamperman and Graff 2026 (B1) has a historian of literacy as co-author, "Historical Fallacies" in the title and Graff's books plus the current AI-literacy policy documents in its references. I could not open it. It may do part of what this paper plans, probably the overselling strand (Problem 5). Until a human reads it, the paper cannot say what it adds relative to it.
2. **Partial neighbours exist and I have read the abstracts.** (i) Critiques of AI literacy as a "consumer" or compliance competence that leaves out power: Lund and Teel 2026 (read), Paljor et al. 2026, Shapiro et al. 2026 (abstracts). (ii) Genealogies and deficit-framing critiques of "digital literacy": Nichols and Stornaiuolo 2019, Weninger 2023, Lea 2013, Gibson 2008 (abstracts). (iii) A print analogy in literacy education: Kalantzis and Cope 2024 (abstract). (iv) Slavery- and colonial-frame critiques of AI in literacy education: Shaw et al. 2024, Bradley et al. 2024, Mohamed et al. 2020 (abstracts). (v) Berthon's own AI-ethics papers cite colonial structures and the digital divide without a literacy history (Su et al. 2023, read).
3. **Specific comparisons I did not find.** I found no work that: (a) uses Jim Crow-era or other voting literacy tests as a comparison for AI-literacy requirements (rows 20, 30); (b) uses anti-literacy statutes for the enslaved as a comparison for AI access or AI-literacy gating (row 21; Willis 2023 appears only as a hit on anti-literacy laws, with no AI content seen); (c) uses colonial or missionary schooling as a comparison for AI-literacy programmes (row 22); (d) applies Graff's literacy myth to AI literacy in a source I could open (rows 14, 19, 29, 31; B7 and B8 are near-misses, neither in Graff's sense nor about AI).

**Each failure the paper claims, against what I found.**

| Claimed failure | A prior AI/digital argument I found | Depth |
| --- | --- | --- |
| Withholding | Lund and Teel: unequal access to tools and "epistemic scaffolding" along income, education and geography. UNESCO 2024 §2.4 states access as a right. No comparison to anti-literacy laws found. | read |
| Gating civic standing on the competence | Paljor et al. (abstract): ethics as add-on prepares for "compliance." Oeldorf-Hirsch and Neubaum (abstract): "the new algorithmic divide." No source found that treats an AI-literacy test or requirement as a civic gate. | abstract |
| Imposition at the cost of other ways of life | Yao and Lin (abstract): "cross-cultural transplantation" of digital-literacy frameworks in the Global South. Bradley et al. (abstract): "anti-colonial literacies." | abstract |
| Overselling | Kamperman and Graff (title, references only); Lea 2013 (abstract: competency-based agendas); Holt 2026 (not Graff's sense). | metadata / abstract |

**Who objected at the time (Problem 2).** This facet does not cover the historical record; I note only that none of the AI-side sources I read treats contemporaries' objections to the literacy transition as evidence.

### Q2. How "AI literacy" is written into rules and gates now

Read together, the texts I opened differ on three things the paper will need.

- **Who carries the duty.** The EU Act puts the duty on providers and deployers for their staff (R1); the Omnibus keeps that and removes any guaranteed level of competence (R2). UNESCO, the EC-OECD framework and PISA MAIL address education systems and describe what students "should" acquire; they state non-binding or preliminary status (R3 to R5). The US order sets a policy to "promote AI literacy" (R6). The US DOL framework is voluntary for grantees (R7). Beijing sets a minimum of class hours, and reports say AI application skills enter students' assessments (R8). Ohio State makes it a graduation goal for undergraduates from the class of 2029 (R9).
- **Who is named as the beneficiary.** Recital 20 and Art. 3(56) of the AI Act list "affected persons" among those whom AI literacy should equip, while Article 4 itself binds providers and deployers only.
- **Whether a test attaches.** PISA 2029 MAIL is an assessment (R5). Beijing: "comprehensive assessments" (R8). I found no rule in the texts I opened that denies a legal status, a vote, a job or a service to an individual for failing an AI-literacy test. For individual hiring and performance requirements I have no verified text (R10).

**Scale.** Supranational: EU, UNESCO, OECD. National: US. Municipal: Beijing. Institutional: Ohio State.

### Q3. "Algorithmacy" and its cousins

Within what I opened and searched, "algorithmacy" is used by the author and the venues tied to the lab; I found no independent use and no use in Crossref. "Algoracy" returned no hit. The nearest established term is "algorithmic (or algorithm) literacy," defined as awareness, knowledge, critical evaluation and, in some versions, creation (Ridley and Pawlick-Potts 2021, read; Dogruel et al. 2021, abstract). None of the definitions I read names the two-party, third-party-binding structure that the paper's definition of algorithmacy contains.

### Q4. Berthon

See B11. His verified record on technology ethics, attention and AI is substantial and continuous from 2018; it does not include literacy or the history of writing or print.

### Claims the sources contradict, or that I could not confirm

1. **"Nobody has applied Graff to AI literacy."** Not contradicted by anything I opened, but the 2026 *Change* article with Graff as co-author (B1) and its reference list make it likely that someone has. The paper should not claim that gap until B1 is read.
2. **"AI literacy is being imposed as a gate."** The texts I opened do not show an individual gate. The EU duty binds firms; the amended Article 4 removes a guaranteed competence level (R2); UNESCO says its top level should be elective (R3); the DOL framework is voluntary (R7). Beijing and Ohio State are the closest to a requirement on learners (R8, R9).
3. **"The EU rule requires AI literacy of the public."** Article 4 requires measures for staff and persons acting for providers or deployers. It does not require it of affected persons (R1).
4. **"Article 4 is sanctioned."** I found it is not among the Article 99(4) fine categories; national rules unread.
5. **"Article 4 stands as enacted in 2024."** It was replaced by Regulation (EU) 2026/1744; the 2024 wording is superseded as of the Omnibus's entry into force (R2).
6. **"Algorithmacy is an established term."** Not supported by the databases searched; see Q3.
7. **Consensus listings that proved wrong on check:** Oeldorf-Hirsch and Neubaum is 2023, not 2021 (Crossref); the arXiv paper is by Lund and Teel, not "Lund et al." (PDF title block).

---

## (d) Gaps and unverified leads

**Not accessible (what, why, where a human would find it).**

- Kamperman and Graff 2026, *Change* 58(4): 34-39, DOI 10.1080/00091383.2026.2706429. tandfonline 403; paywalled. Bentley library, Taylor & Francis. **First priority.**
- Hoffman 2026 (AERA, DOI 10.3102/2281796) and Tanksley 2024 (AERA, 10.3102/2103035): AERA Online Paper Repository, `aera.net`.
- Shaw, Toliver, Tanksley 2024, RRQ 59(4): Wiley via library.
- Mora and Yepes-Mora 2025, chapter in *Reimagining Literacy in the Age of AI*, Routledge/CRC via library.
- Neos 2026, "Gutenberg or the Great Firewall?" (SSRN 5805364; 403) and Chen 2026 (SSRN 7358584; not opened).
- Paljor et al. 2026 (ACM; bot challenge) and Nichols and Stornaiuolo 2019 (open access at cogitatiopress.com; a browser is needed, the file download returned empty).
- Weninger 2023, Lea 2013, Hicks and Lloyd 2020, Tewell 2020, Bacalja et al. 2021, Kalantzis and Cope 2024 (RRQ has an OA location per Unpaywall, not downloaded), Burriss and Leander 2024, Bradley et al. 2024: abstract only.
- Graff's own 2022 "The New Literacy Studies and the Resurgent Literacy Myth" (Literacy in Composition Studies; likely open on the journal site) and Graff 2023 (WAC Clearinghouse books): not read; they show how Graff himself extends the myth to new literacies.
- UNESCO *AI competency framework for teachers* (2024): unesdoc blocked. UNESCO 2022b (the 190-country survey): not opened. The official unesdoc copy of the students' framework was also blocked; I read a mirror.
- OECD PISA 2029 MAIL: the oecd.org original; I read a mirror of the first draft. Whether a final framework has been released after January 2026: **not found.**
- US DOL AI Literacy Framework (TEN 07-25 per a search result; Feb 2026): `dol.gov` "Access Denied." I used the CRS description.
- Beijing Municipal Education Commission work plan and curriculum outline; the national Ministry of Education notice of December 2024.
- Shopify memo (April 2025) and any other employer AI-use requirement text.
- EUR-Lex pages (AWS challenge). I used the Publications Office copy; a human should confirm that the consolidated version of the AI Act at EUR-Lex shows the amended Article 4.
- Berthon: OpenAlex (rate limit; cooldown to midnight UTC), Google Scholar and Bentley's faculty page (not tried). Items marked "not accessible" in B11 need library access; `berthon2018brands` has an OA copy at `hdl.handle.net/10227/179387` behind a bot challenge.
- The author's own pages on algorithmacy (Substack, algorithmacy.org, GitHub): not opened; the claim that no independent use exists rests on search summaries and the empty Crossref results.

**Unverified leads (not opened; titles seen only).**

- Velander, Otero and Milrad 2024, "What is Critical (about) AI Literacy?" (10.1007/978-3-031-58622-4_8).
- Dror et al. 2026 (SSRN 6567200), "Framing Literacy and Practical Wisdom in AI Environments."
- Black and Yasukawa 2014 (B8).
- Willis 2023, *Anti-Black Literacy Laws and Policies* (10.4324/9781003296188).
- Twining 2002, "Oversold and underused: computers in the classroom."
- Cihon, Maas and Kemp 2020/2021, on lessons from history for AI governance (not literacy).
- Tokson 2026, SSRN 6875838, "Artificial Intelligence and the Lessons of History."
- Stoyanovich and colleagues' "Responsible AI literacy" (`dominguez2023responsible`) as a responsibilization-aware design.
- Couldry and Mejias on data colonialism (not searched here).

**Search limits.** OpenAlex and Scholar Gateway were unavailable, Semantic Scholar was used only for four Berthon abstracts, and Google Scholar, JSTOR, ERIC and Web of Science were not searched. The gap statements above are bounded by Crossref (title and metadata only, not full text), Consensus, arXiv's API and web search. A full-text search of AI-literacy work for "Graff", "literacy myth", "literacy test" or "anti-literacy" would test them properly.
