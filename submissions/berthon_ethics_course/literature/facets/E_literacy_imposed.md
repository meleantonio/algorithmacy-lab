# E — Literacy imposed: schooling, language policy and script reform as instruments of rule

*Facet E of the Berthon ethics course paper. Agent-drafted on 2026-10-13. The author has not reviewed it, and none of the text is the author's.*

**What this facet covers.** Places where reading and writing, or the schooling that carried them, were brought by force or as an instrument of rule: residential and boarding schools for Indigenous children (Canada, the United States, Australia, Hawaii, Soviet Siberia), colonial language-of-instruction policy (India, Kenya, Wales, revolutionary France), script reform (Turkey, the USSR), and the measured loss of languages. Every source is sorted by what it attributes to *literacy teaching* and what it attributes to *schooling, removal or language suppression* more broadly. The two are not the same, and the sources I could open rarely blame literacy teaching itself.

**The question the synthesis answers.** Where was literacy brought by force or as an instrument of rule, what was taken in exchange, and who objected at the time?

**Legend for read status.** *Read in full*: I read the whole text this session. *Read in part*: I obtained the full text, searched it, and read the stated pages or sections only (a 400-page report counts here). *Abstract only*: I saw only an abstract or database summary. *Not accessible*: I could not open the text; only bibliographic records were checked. **Locators**: "p." is the printed page of the edition named; "PDF p." is the page of the file I opened when the file carries no printed numbers. Spelling in quotations follows the source; line-end hyphens are removed.

---

## (a) Search log

All requests ran on 2026-10-13. Downloads are under `~/iit-playground/berthon_ethics_local/pdfs/E/`.

| # | Source | Exact query / request | Hits | Notes |
|---|---|---|---|---|
| 1 | repo | Read `RESEARCH_PLAN.md` in full | 1 | Facet E, §7 format, §8 rules. |
| 2 | curl | TRC *Summary* PDF, `ehprnh2mwo3.exactdn.com/wp-content/uploads/2021/01/Executive_Summary_English_Web.pdf` | 535 pp, 218k words | Text layer good. Word "literacy" occurs **zero** times in the extracted text (searched `literac`). |
| 3 | curl | `bia.gov` Federal Indian Boarding School Initiative Vol. I (May 2022) and Vol. II (July 2024) PDFs | 106 pp; 105 pp | Both have text layers. "literacy" occurs zero times in either. |
| 4 | curl | `humanrights.gov.au/.../bringing_them_home_report.pdf` and `.../bringing_them_home_20.pdf` | 403 | Cloudflare bot wall ("Just a moment..."). Not circumvented. |
| 5 | curl | `austlii.edu.au/au/other/IndigLRes/1997/3/` (http and https) | 403 | Same wall. |
| 6 | curl | Wayback copy `web.archive.org/web/2023/https://humanrights.gov.au/sites/default/files/content/pdf/social_justice/bringing_them_home_report.pdf` | 524 pp, 234k words | Opened. Archived copy of the official file; no printed page numbers in the text layer, so I cite PDF pages. |
| 7 | curl | `columbia.edu/itc/mealac/pritchett/.../txt_minute_education_1835.html` | Cloudflare page | Blocked. |
| 8 | curl | Wayback copy of the same Columbia page | 32,550 chars | Opened. A transcription (source line says `mssu.edu/projectsouthasia`), paragraph numbers added by "FWP". Not the 1835 print. |
| 9 | archive.org advancedsearch | `title:(state of education in Wales)` | 3 copies of the 1848 *Reports* | Downloaded `reportsofcommiss00grearich_djvu.txt` (1.86M chars, OCR). |
| 10 | Crossref | `query.bibliographic` Bromham et al. | DOI found | `10.1038/s41559-021-01604-y`; also a Publisher Correction `10.1038/s41559-022-01684-4`. |
| 11 | Unpaywall | `v2/10.1038/s41559-021-01604-y` | failed | The email file named in the plan (`org_frontier/research/oa_acquire.py`) is not in this worktree; no address available. Not retried. |
| 12 | curl | `nature.com/articles/s41559-021-01604-y.pdf` | 21 pp, 0 words | PDF has no extractable text (font errors). |
| 13 | Europe PMC REST | `PMC8825282/fullTextXML` | full text | Opened (81k chars). Locators are section-level; the XML carries no page numbers. |
| 14 | WebFetch | `unesco.org/en/languages-atlas` | 404 | |
| 15 | WebSearch | `UNESCO Atlas of the World's Languages in Danger number of languages vulnerable endangered extinct since 1950` | 10 links, secondary | Gave no global extinct count. Led to the `webarchive.unesco.org` copy of unesdoc 187026. Search summary not relied on. |
| 16 | curl | `webarchive.unesco.org/web/20151214150659/http://unesdoc.unesco.org/images/0018/001870/187026e.pdf` | 222 pp, 87k words | Opened: Moseley (ed.) 2010 *Atlas*, 3rd edition. Two-column layout; I reconstructed sentences from the left or right column and say so. |
| 17 | Scholar Gateway `semanticSearch` | "Did colonial and missionary schooling suppress indigenous languages and oral traditions in Africa, and how did teaching of literacy relate to language loss?" | `ACCESS_DENIED: Access denied` | Failed (one attempt, as the plan allows). |
| 18 | Consensus | `Soviet Latinization of alphabets and Turkish 1928 alphabet reform effect on literacy and suppression of Arabic script` | 20 | Abstract-level only: Wood 1929, Dietrich 2006, Musaev 2019, Can 2023, Islam 2026, Kuzuoğlu 2020, Shegebayev 2019, others. |
| 19 | Consensus | `Welsh Not punishment in schools nineteenth century evidence historiography` | 20 | Found Johnes 2024 (open access), Roberts 2020, G. E. Jones 2006, G. Williams 1999. |
| 20 | curl | `doi.org/10.16922/welshnot` | 302 to `uwp.co.uk/app/uploads/9781837721818_WEB.pdf` | Opened: 458 pp, 160k words, printed pages in the footer. |
| 21 | archive.org advancedsearch + metadata | titles: *Decolonising the Mind*, *Darker Side of the Renaissance*, *Literacy and Literacies*, *Literacy in Theory and Practice* | Ngũgĩ: 7 items; Mignolo: 2 | Ngũgĩ: only `DecolonisingTheMindNgugiTheFullBook` served text (a private upload of a ZPH/Heinemann-edition scan, bundled with another book). `decolonisingmind0000ngug`, `decolonisingmind00ngug` returned 401. Mignolo `darkersideofrena0000mign` returned 302 (borrow only). Not accessible. |
| 22 | Crossref | chapter DOIs `10.1017/cbo9780511486661.003`–`.011` | titles and pages | Collins and Blot chapter list verified. No abstracts. |
| 23 | WebFetch | `cambridge.org/core/books/literacy-and-literacies/literacies-and-identity-formation-american-cases/` | 404 | |
| 24 | OpenAlex | `works?search=Mignolo+darker+side...` | rate-limit error | Daily budget exhausted. Not retried. |
| 25 | curl | `books.openbookpublishers.com/10.11647/obp.0025.pdf`; `doi.org/10.11647/obp.0025` | empty PDF; 429 | Blocked. Used the OAPEN copy on archive.org instead: `oapen-20.500.12657-31251/633751_djvu.txt` (231k words). |
| 26 | Wikisource API | `fr.wikisource.org/w/api.php?action=parse&page=Rapport sur la nécessité…&prop=text` | 49,775 chars | Opened. Transcription of the 1794 Convention nationale print (pp. 1–19); the transcription does not give page numbers inside the text. |
| 27 | WebFetch | same Wikisource page, with a prompt asking for quotations | summary | A model summary, not text I opened. **Not relied on**; all Grégoire quotations below come from #26. |
| 28 | Crossref `/works/{doi}` | 11 DOIs (Bromham; Johnes; Collins and Blot; Wood; Musaev; Roberts; Kuzuoğlu; others) | titles matched | Two DOIs I guessed for Street (1984) and Mignolo returned a different work or nothing. I discarded them. No DOI for either book is in this file. |
| 29 | Crossref | `query.bibliographic` Street, *Literacy in Theory and Practice* | 4 | Only reviews and Street 2013; no record for the 1984 book itself. |

---

## (b) Entries

### 1. TRC Canada, *Honouring the Truth, Reconciling for the Future* (Summary of the Final Report), 2015 — `trc2015honouring`

- **Reference.** Truth and Reconciliation Commission of Canada. 2015. *Honouring the Truth, Reconciling for the Future: Summary of the Final Report of the Truth and Reconciliation Commission of Canada.* Winnipeg: TRC. URL as in #2.
- **Verified exists.** Opened the PDF; title page and copyright page read. Page numbers below are the printed ones (PDF page minus 7 in the body).
- **Read status.** Read in part: Introduction pp. 1–6; the history chapter on language and culture (pp. 80–82), half-day labour (pp. 77–79), mortality (p. 92), parental protest (p. 117); the Legacy section on education (pp. 144–145); the 1883 and 1920 statements. The remainder of the 535 pages searched by keyword only.
- **Source type.** Official commission report; a primary source for the commission's findings and, through its quotations, for 1880s–1940s Indian Affairs documents (which I did not open at source).
- **Scale.** Nation (Canada), 1870s to late 1990s.
- **Attribution.** The TRC attributes the harm to *removal, assimilation, labour, abuse and language suppression*. It does not attribute it to literacy teaching. The word "literacy" does not occur in the Summary. Where it speaks of reading, it speaks of failure to teach it.

**What it says (quotations).**
- p. 1: "For over a century, the central goals of Canada's Aboriginal policy were to eliminate Aboriginal governments; ignore Aboriginal rights; terminate the Treaties; and, through a process of assimilation, cause Aboriginal peoples to cease to exist as distinct legal, social, cultural, religious, and racial entities in Canada. The establishment and operation of residential schools were a central element of this policy, which can best be described as 'cultural genocide.'" (The quotation marks around the last two words are the report's own.)
- p. 2, quoting Prime Minister John A. Macdonald to the House of Commons in 1883: "When the school is on the reserve the child lives with its parents, who are savages; he is surrounded by savages, and though he may learn to read and write his habits, and training and mode of thought are Indian. He is simply a savage who can read and write. It has been strongly pressed on myself, as the head of the Department, that Indian children should be withdrawn as much as possible from the parental influence, and the only way to do that would be to put them in central training industrial schools where they will acquire the habits and modes of thought of white men." The TRC's gloss, same page: "This was done not to educate them, but primarily to break their link to their culture and identity."
- p. 3, on Duncan Campbell Scott's 1920 statement to a parliamentary committee: "our object is to continue until there is not a single Indian in Canada that has not been absorbed into the body politic." And the commission's reading of the motive, same page: "The Canadian government pursued this policy of cultural genocide because it wished to divest itself of its legal and financial obligations to Aboriginal people and gain control over their land and resources."
- p. 3: "The federal government has estimated that at least 150,000 First Nation, Métis, and Inuit students passed through the system." Same page: "although most of the schools had closed by the 1980s, the last federally supported residential schools remained in operation until the late 1990s."
- p. 80, on language directives (the TRC quotes Indian Affairs documents): in 1883 Commissioner Dewdney told the Battleford principal that great attention was to be given "towards imparting a knowledge of the art of reading, writing and speaking the English language rather than that of Cree"; in 1890 Commissioner Reed proposed "At the most the native language is only to be used as a vehicle of teaching and should be discontinued as such as soon as practicable"; the 1893 *Programme of Studies* advised "Every effort must be made to induce pupils to speak English, and to teach them to understand it; unless they do the whole work of the teacher is likely to be wasted."
- p. 81: the Onion Lake school in 1898 was "one of the few exceptions. There, the children were taught to 'read and write both Cree and English.'" Same page: inspectors "viewed the continued use of Aboriginal languages by the students as a sign of failure." A 1903 inspector called Cree use "a serious drawback to school work, as well as an evidence of bad discipline." Oblate Superior General Labouré, after a 1935 tour: "The forbidding of children to speak Indian, even during recreation, was so strict in some of our schools that any lapse would be severely punished—to the point that children were led to consider it a serious offense."
- pp. 77–78: most schools "operated on what was referred to as the 'half-day system'", and p. 78: "the reality was that every student worked."
- p. 92: "A January 2015 statistical analysis of the Named Register for the period from 1867 to 2000 identified 2,040 deaths. The same analysis of a combination of the Named and Unnamed registers identified 3,201 reported deaths." (Deaths, not literacy outcomes.)
- p. 96: Dr. Peter Bryce, Indian Affairs chief medical officer, "published a damning report on the conditions at prairie boarding schools" in 1907 (the TRC cites Bryce's *Report on the Indian Schools of Manitoba and the North-West Territories*, 1907, and says "The following year"); he found ventilation "extremely inadequate."
- p. 117, parents and chiefs: Chief Napahkesit of Pine Creek said in 1917 he was sorry he had supported the school; the local agent reported he felt "the children know less when they come out than they did when they went in." "Calls for day schools were, in fact, a common parental request." In 1937 Dene people refused Treaty payments over conditions at Fort Resolution; their children, they said, were "living in hell." In 1931 the League of Indians called for closure of boarding schools and for "greater class time" (p. 117, paraphrase by the TRC).
- p. 144: "The residential school system failed as an education system. It was based on racist assumptions about the intellectual and cultural inferiority of Aboriginal people—the belief that Aboriginal children were incapable of attaining anything more than a rudimentary elementary-level or vocational education." And: "The government and church officials who operated the residential schools ignored the positive emphasis that the Treaties and many Aboriginal families placed on education."
- p. 145: "The Commission has heard many examples of students who attended residential school for eight or more years, but left with nothing more than Grade Three achievement, and sometimes without even the ability to read. According to Indian Affairs annual reports, in the 1950s, only half of each year's enrolment got to Grade Six."

**Bearing on the five problems.**
1. *Documented wrong*: **supports**. Dates, places, numbers, official directives.
2. *Presentism*: **supports**, with the objectors named in the passages above: Bryce (1907), Napahkesit (1917), the League of Indians (1931), Labouré (1935), Dene refusal (1937), parents who asked for day schools and withheld children (1917, 1949).
3. *Scale*: **complicates**. National only.
4. *Comparison may break*: **supports the break**. Macdonald 1883 states that the point was removal from the parents, and treats reading and writing as insufficient to do the work; the instrument was custody of the child.
5. *Literacy myth*: **complicates**. The commission reports that many left without the ability to read (p. 145); the stated aim was not literacy. Charging the schools with overselling literacy would misdescribe them.

---

### 2. US Department of the Interior, Federal Indian Boarding School Initiative Investigative Report, Vol. I (May 2022) — `newland2022federal`

- **Reference.** Newland, Bryan (Assistant Secretary, Indian Affairs). 2022. *Federal Indian Boarding School Initiative Investigative Report* (Vol. I). Washington, DC: US Department of the Interior, May 2022. URL as in #3.
- **Verified exists.** Opened; cover reads "Federal Indian Boarding School Initiative Investigative Report May 2022 Assistant Secretary – Indian Affairs Bryan Newland"; transmittal letter dated 1 April 2022 to Secretary Haaland.
- **Read status.** Read in part: the letter (PDF p. 3), executive summary (PDF pp. 10–13), pp. 35–40 (compulsion), 42–44, 51–54 (methods), 75–77 (Hawaii), findings (pp. 91–92). Printed page = PDF page minus 4. The rest searched by keyword only.
- **Source type.** Official government report, drawing on Annual Reports of the Commissioner of Indian Affairs (ARCIA), the Meriam Report and the Kennedy Report. I did not open those at source; the quotations from them below are as the Department prints them.
- **Scale.** Nation (United States, including Alaska and Hawaii), 1819–1969.
- **Attribution.** *Boarding schools as a system of removal, militarised discipline and assimilation*; language prohibition is one named method. "Literacy" does not occur. English instruction is treated as the vehicle of assimilation.

**Quotations.**
- p. 91 (finding 1 and 2): "The Federal Indian boarding system was expansive, consisting of 408 Federal Indian boarding schools, comprised of 431 specific sites, across 37 states or then-territories, including 21 schools in Alaska and 7 schools in Hawaii. 2. Multiple generations of American Indian, Alaska Native, and Native Hawaiian children were induced or compelled by the Federal Government to experience the Federal Indian boarding school system, given their political and legal status as Indians and Native Hawaiians." The 408 schools span 1819–1969 (PDF p. 3, letter).
- p. 92 (finding 7): "The Federal Indian boarding school system discouraged or prevented the use of American Indian, Alaska Native, and Native Hawaiian languages or cultural or religious practices through punishment, including corporal punishment."
- p. 9: "approximately 19 Federal Indian boarding schools accounted for over 500 American Indian, Alaska Native, and Native Hawaiian child deaths. As the investigation continues, the Department expects the number of recorded deaths to increase." (PDF p. 13.) Vol. II raises this (entry 3).
- pp. 35–36, compulsion: "After 1871, Congress enacted laws to compel Indian parents to send their children to school". Under the Act of 3 March 1893 the Secretary of the Interior could "prevent the issuing of rations or the furnishing of subsistence either in money or in kind to the head of any Indian family for or on account of any Indian child or children between the ages of eight and twenty-one years who shall not have attended school during the preceding year". The Department notes that treaty-guaranteed rations were covered.
- p. 35 epigraph, attributed to the Kennedy Report (US Senate, 1969): "Many Indian families resisted the assault of the Federal Government on their lives by refusing to send their children to school."
- p. 38, the Meriam Report (Brookings, 1928) as quoted: "[O]n the whole government practices may be said to have operated against the development of wholesome [Indian] family life. Chief of these is the long continued policy of educating the [Indian] children in boarding schools far from their homes, taking them from their parents when small and keeping them away until parents and children become strangers to each other."
- p. 51, quoting the Kennedy Report at 12: the schools "were designed to separate a child from his reservation and family, strip him of his tribal lore and mores, force the complete abandonment of his native language, and prepare him for never again returning to his people."
- p. 54, quoting ARCIA for 1904 at 391: "Teaching the young Indian child to speak English is essentially the first step in his training, and special attention has been directed to giving him a working knowledge of the language in the shortest possible time."
- p. 40, on mixing tribes (ARCIA 1886): a school official noted that mixing pupils of different tribes "necessitates a more frequent recourse to the English language as a common medium" (PDF p. 44).
- p. 75, Hawaii: the Hawaiian-language public school system "eventually repressed 'Ōlelo Hawai'i in education by promoting English. By 1888, only 16 percent of children were taught in Hawaiian." (footnote 312 cites a legal treatise, *Native Hawaiian Law*, not a primary count). PDF p. 80 adds that "various governments controlling the Hawaiian Islands banned 'Ōlelo Hawai'i and required the use of the English language in public education"; PDF p. 81 says that by 1902 the Territory had "203 English-required schools".

**Bearing.** 1 supports (system size, compulsion, language ban). 2 supports for the Meriam Report (1928) and Indigenous refusal; the report names few other objectors. 3 complicates (nation). 4 supports the break (instrument is custody). 5 not addressed.

---

### 3. Federal Indian Boarding School Initiative Investigative Report, Vol. II (July 2024) — `newland2024federal`

- **Reference.** Newland, Bryan. 2024. *Federal Indian Boarding School Initiative Investigative Report* (Vol. II). US Department of the Interior, July 2024.
- **Verified exists.** Opened; cover reads "Vol. II July 2024 Assistant Secretary for Indian Affairs Bryan Newland".
- **Read status.** Read in part: executive summary (PDF p. 5), PDF pp. 15–16, 39, 42. Printed page = PDF page for these pages.
- **Quotations.** p. 15: "Based on available records, the Department concludes at least 973 documented Indian child deaths occurred across the Federal Indian boarding school system between 1819 and 1969." p. 16: "has now identified 74 marked or unmarked burial sites at 65 different schools" (53 marked, 21 unmarked). PDF p. 5 (executive summary): "more than $23.3 billion in FY23 inflation-adjusted dollars between 1871 and 1969" in appropriations. p. 39: the figure "is not complete".
- **Bearing.** Deaths and burial sites are harms of the boarding system, not of literacy teaching. The Vol. I figure ("over 500", 19 schools) and Vol. II figure (973) are not in conflict: the Department says the count is expected to rise and is incomplete.

---

### 4. Australia, *Bringing Them Home*, 1997 — `hreoc1997bringing`

- **Reference.** Human Rights and Equal Opportunity Commission. 1997. *Bringing Them Home: Report of the National Inquiry into the Separation of Aboriginal and Torres Strait Islander Children from Their Families.* Sydney: HREOC. Archived copy as in #6.
- **Verified exists.** Opened archived PDF; title page, copyright page ("Commonwealth of Australia 1997") and Terms of Reference read.
- **Read status.** Read in part: PDF pp. 31, 33, 36, 37, 53, 90, 95, 103, 122, 133, 137, 231. Full text searched for "literacy" (two hits, both quoted below).
- **Scale.** Nation (Australia) by state, c. 1910–1970 for the national estimate; earlier episodes from 1788.
- **Attribution.** *Forcible removal* from families, to institutions and domestic service. Schooling is incidental; the report treats removal, not literacy teaching, as the wrong.

**Quotations.**
- PDF p. 31: "Nationally we can conclude with confidence that between one in three and one in ten Indigenous children were forcibly removed from their families and communities in the period from approximately 1910 until 1970."
- PDF p. 137 (Moore River Settlement, Western Australia, 1938): "The children were taught basic literacy, numeracy and hygiene, with a view to employment as domestic servants and rural labourers."
- PDF p. 103 (South Australia, 1839 on): the 'Native Location' School and later schools "All became boarding schools so as to maximise control over the children."
- PDF p. 133: "Missionaries in the Kimberley region of WA as late as the 1960s continued to pursue this policy of forbidding the use of Aboriginal languages" (the report's summary of confidential evidence 505), followed by a witness: "Aboriginal people weren't allowed to speak their language while white people were around."
- PDF p. 36, objections at the time (New South Wales Parliament, 1914–15, on the 1915 amending Act): the Hon. P. McGarry said it allowed the Board "to steal the child away from its parents"; another member called it "reintroduction of slavery in NSW" (Parliamentary Debates 1914–15, as cited by the report).
- PDF p. 95: "Aboriginal women from Broome sent a petition to the Commission in which they asked 'would you like to think that when you send your children to school that you would never see them again?'" (Quoted by the report from Paisley 1995, p. 267; I did not open Paisley. The report passage does not date the commission; the year is *not found* in what I read.)

**Bearing.** 1 supports (removal numbers, dates). 2 supports (McGarry; Broome petition). 3 complicates (national, plus state-level variation the report itself stresses). 4 supports the break: the wrong is separation; literacy appears twice, as a minor curriculum item aimed at servant labour. 5 not addressed.

---

### 5. Macaulay, *Minute on Education*, 2 February 1835 — `macaulay1835minute`

- **Reference.** Macaulay, Thomas Babington. 1835. "Minute by the Hon'ble T. B. Macaulay, dated the 2nd February 1835." Wayback copy of the Columbia Pritchett page, #8; the page says it is taken from `mssu.edu/projectsouthasia`, with paragraph numbers added by "FWP".
- **Verified exists.** Opened. The text is a classroom transcription, not a scan of the 1835 document. I did not compare it with the print (Bureau of Education, *Selections from Educational Records*, Part I, ed. H. Sharp, 1920 is the usual source; not opened).
- **Read status.** Read in part: paragraphs [1], [10]–[12], [34]–[35]; remainder searched.
- **Scale.** British India (the empire's largest colony), a policy decision of the Governor-General's Council.
- **Attribution.** A *language-of-instruction* decision (English rather than Sanskrit, Arabic or the vernaculars). It is about which learning the state funds. It concerns mass literacy by saying it will not provide it.

**Quotations (by paragraph number).**
- [10]: "I have never found one among them who could deny that a single shelf of a good European library was worth the whole native literature of India and Arabia." Macaulay writes in [10] that he has "no knowledge of either Sanscrit or Arabic."
- [12]: "We have to educate a people who cannot at present be educated by means of their mother-tongue. We must teach them some foreign language."
- [34]: "I feel with them that it is impossible for us, with our limited means, to attempt to educate the body of the people. We must at present do our best to form a class who may be interpreters between us and the millions whom we govern,--a class of persons Indian in blood and colour, but English in tastes, in opinions, in morals and in intellect."
- [1]: he writes in answer to "adverse statements" prepared by members of the Committee of Public Instruction (the Orientalist side).

**Bearing.** 1 supports as a stated ground (rule through an English-educated intermediary class). 2: the Orientalist members of the Committee opposed it; their text I did not open. 3 complicates (one empire). 4 supports the break: the policy states that mass literacy is *not* the object. 5 complicates: [34] is the opposite of a promise of universal literacy.

---

### 6. Reports of the Commissioners of Inquiry into the State of Education in Wales (the "Blue Books"), 1847, published 1848 — `greatbritain1848reports`

- **Reference.** Great Britain, Committee of Council on Education. 1848. *Reports of the Commissioners of Inquiry into the State of Education in Wales … in three parts.* London: W. Clowes for HMSO. Internet Archive `reportsofcommiss00grearich` (University of California copy; OCR).
- **Verified exists.** Opened OCR text; title page and contents read (Part I Carmarthen, Glamorgan, Pembroke, p. 1; Part II Brecknock, Cardigan, Radnor, Monmouth, p. 201; Part III North Wales, p. 421). The Part II report is signed Jelinger C. Symons; Part III is headed "By Henry Vaughan Johnson, Esq."
- **Read status.** Read in part: Part II section IX "The Welsh Language" (pp. 309–310); Part III p. 452–453. OCR text, so spelling may carry OCR errors; I checked the quoted words against the OCR text.
- **Scale.** Region of a state (Wales, 1846–47).
- **Attribution.** The Commissioners were charged to inquire into "the means afforded to the labouring classes of acquiring a knowledge of the English language" (title page). They attribute harm to the *Welsh language*, not to teaching literacy. Johnson's Part III records a school punishment for speaking Welsh.

**Quotations.**
- p. 309 (Part II, Symons): "The Welsh language is a vast drawback to Wales, and a manifold barrier to the moral progress and commercial prosperity of the people. It is not easy to over-estimate its evil effects. It is the language of the Cymri, and anterior to that of the ancient Britons. It dissevers the people from intercourse which would greatly advance their civilization, and bars the access of improving knowledge to their minds."
- p. 452 (Part III, report on a school at Llandyrnog, Denbighshire): "My attention was attracted to a piece of wood, suspended by a string round a boy's neck, and on the wood were the words, 'Welsh stick.' This, I was told, was a stigma for speaking Welsh. But, in fact, his only alternative was to speak Welsh or to say nothing. He did not understand English, and there is no systematic exercise in interpretation." And: "The Welsh stick, or Welsh, as it is sometimes called, is given to any pupil who is overheard speaking Welsh, and may be transferred by him to any schoolfellow whom he hears committing a similar offence. It is thus passed from one to another until the close of the week, when the pupil in whose possession the Welsh is found is punished by flogging. Among other injurious effects, this custom has been found to lead children to visit stealthily the houses of their schoolfellows for the purpose of detecting those who speak Welsh to their parents, and transferring to them the punishment due to themselves."
- p. 452: "of 19,521 scholars examined, only 149 were found able to read with propriety and expression." In the same passage, the report blames teachers "unable to pronounce English". Whether this test was of reading in English or Welsh: not stated in the lines I read.
- Terminology: the OCR text contains no "Welsh Not" (zero hits); the object is "Welsh stick" or "Welsh".

**Bearing.** 1 supports (a documented school punishment and a stated official judgement). 2: the report itself names the "injurious effects" of the stick; the public Welsh objection is documented only in entry 8 (abstract). 3 complicates (region). 4: mixed. 5 complicates: the same state inquiry reports that children examined in a language they did not speak could not read.

---

### 7. Johnes, *Welsh Not*, 2024 — `johnes2024welsh`

- **Reference.** Johnes, Martin. 2024. *Welsh Not: Elementary Education and the Anglicisation of Nineteenth-Century Wales.* Cardiff: University of Wales Press. DOI 10.16922/welshnot (Crossref-resolved, title matched; open access PDF via the DOI redirect).
- **Read status.** Read in part: pp. 51, 98–99, 103, 309; chapter list; searched for "literacy" and "Blue Books". The 458 pages were not read in full.
- **Scale.** Wales, nineteenth century.
- **Attribution.** *Exclusion of Welsh from the classroom*, often with corporal punishment. Johnes argues that this hindered learning English; he does not blame literacy teaching.

**Quotations.**
- p. 51: "It is difficult to be sure of how widely employed the Welsh Not was. Education inquiries offered no clear statements, while the autobiographical writings are too unsystematic to offer any conclusive evidence of patterns or certainty about its frequency." And: "The Blue Books were the most comprehensive survey of Welsh education ever conducted but they only contain one mention of it." (My reading of Part III in entry 6 found one mention, at p. 452, consistent with this.)
- p. 98: "Sunday schools and popular literacy": "According to the Blue Books, 71 per cent of Sunday schools in north Wales were held in Welsh and 21 per cent were bilingual." Sunday schools "were important in developing literacy", though Johnes cautions "it is important not to exaggerate their reach or their impact on Welsh literacy levels, especially since many only taught reading rather than writing" (pp. 98).
- p. 99: "In 1845, 46.3 per cent of men and 69.5 per cent of women who got married in Wales signed with a cross rather than writing their name. The advances made in education were clear in 1865 when the figures had fallen to 35.5 per cent for men and 50.5 per cent for women."
- p. 103: "What the Welsh Not did was not spread English but prevent that from happening. The irony of the Welsh Not is that what it achieved is exactly the opposite of what many people today think happened. Welsh was not beaten out of children. That could not happen if children did not learn another language. Instead, many children were just beaten."
- p. 309: "Contemporaries aplenty recorded how parents wanted English to dominate the schools and feared the use of Welsh might hinder their children in learning the new language. That probably translated into tacit rather than open support of the Welsh Not."

**Bearing.** 1 supports with qualification: the punishment is documented, its frequency is not. 2: complicates; contemporaries mostly did *not* object, and parents sought English. 3 complicates. 4 and 5: complicates, because the cost fell on literacy in the language the child could not read. Johnes rebuts the popular claim that the Welsh Not killed Welsh.

---

### 8. Roberts, "'At Once Illogical and Unfair'": Jane Williams (Ysgafell) and the 1847 Education Report, 2020 — `roberts2020illogical`

- **Reference.** Roberts, Gwyneth. 2020. In *Women's Writing from Wales before 1914*. Routledge. DOI 10.4324/9780429330865-5 (Crossref-resolved, title matched).
- **Read status.** **Abstract only** (as returned by Consensus). Not accessible beyond that.
- **What the abstract says.** The three commissioners were "middle-class English Anglicans" who concluded that "most Welsh people were liars, cheats, thieves and sexually promiscuous", linking these traits to being Welsh-speaking Nonconformists; "The commissioners' report appeared in 1847 and sparked outrage in Wales"; Jane Williams's 1848 pamphlet *Artegall* answered it.
- **Bearing.** Names a contemporary objector (Williams, 1848) and a ground (the report's political motives and character libel). I cannot quote her; the abstract is a paraphrase by Roberts.

---

### 9. Grégoire, *Rapport sur la nécessité et les moyens d'anéantir les patois et d'universaliser l'usage de la langue française*, 1794 — `gregoire1794rapport`

- **Reference.** Grégoire, Henri. 1794. Rapport … Paris: Convention nationale, 19 pp. Wikisource transcription (#26).
- **Verified exists.** Opened the transcription; header gives author, title and "Convention nationale, 1794 (p. 1–19)".
- **Read status.** Read in part: the passage on numbers and two further passages on unity of language; the full 49,775-character text was searched but not read. No page numbers appear in the transcription, so locators below are "p. not found".
- **Scale.** Nation (France), a proposal to the legislature, not an enforced policy in this document.
- **Attribution.** *Language unification*. The report names both speaking and writing.

**Quotations (French, as printed).**
- "On peut assurer sans exagération qu'au moins six millions de Français, sur-tout dans les campagnes, ignorent la langue nationale ; qu'un nombre égal est à-peu-près incapable de soutenir une conversation suivie ; qu'en dernier résultat, le nombre de ceux qui la parlent purement n'excède pas trois millions ; & probablement le nombre de ceux qui l'écrivent correctement est encore moindre. Ainsi, avec trente patois différens, nous sommes encore, pour le langage, à la tour de Babel, tandis que pour la liberté nous formons l'avant-garde des nations." (These counts are Grégoire's own assertions; I did not check them.)
- "Il faut donc que l'unité de langue entre les enfants de la même famille éteigne les restes des préventions résultantes des anciennes divisions provinciales".
- "ils ont abjuré & combattu le fédéralisme politique ; ils combattront avec la même énergie celui des idiômes."

**Bearing.** 1: a stated ground (unity of language as a political aim, in the passages above). 2: I did not find an objector in what I opened. 3: nation. 4 and 5: I did not read the full argument, so I make no claim about whether he treats access to the national language as a benefit or about literacy returns.

---

### 10. Ngũgĩ wa Thiong'o, *Decolonising the Mind: The Politics of Language in African Literature*, 1986 — `ngugi1986decolonising`

- **Reference.** Ngũgĩ wa Thiong'o. 1986. *Decolonising the Mind: The Politics of Language in African Literature.* London: James Currey; Portsmouth, NH: Heinemann (publisher per the Internet Archive record `decolonisingmind0000ngug`, which I could not open).
- **Verified exists.** The copy I read is a private upload (`DecolonisingTheMindNgugiTheFullBook`, uploaded 2018) of a Zimbabwe Publishing House–series printing. The edition and its pagination may differ from the Currey/Heinemann print. The text carries inline page numbers, which I use as approximate locators ("scan p."). A human should confirm all page numbers against a print copy.
- **Read status.** Read in part: the Introduction and Statement, and Chapter 1 pp. 3–12 (scan pages); searched the rest.
- **Scale.** One country (Kenya), generalised to Africa.
- **Attribution.** *Language of instruction*, and the replacement of oral and vernacular literature by English literature. He does not argue against literacy; he argues against the replacement of Gikuyu as the language of schooling and literature. He writes: "This book, Decolonising the Mind, is my farewell to English as a vehicle for any of my writings." (Statement, scan p. xii–xiii; the scan's OCR renders the title imperfectly.)

**Quotations.**
- Statement (scan p. xii): "In 1977 I published *Petals of Blood* and said farewell to the English language as a vehicle of my writing of plays, novels and short stories."
- scan p. 9: "Berlin of 1884 was effected through the sword and the bullet. But the night of the sword and the bullet was followed by the morning of the chalk and the blackboard. The physical violence of the battlefield was followed by the psychological violence of the classroom." And: "The bullet was the means of the physical subjugation. Language was the means of the spiritual subjugation."
- scan pp. 10–11, on his schooling: for his first four years at the school there "was still harmony between the language of my formal education and that of the Limuru peasant community. … It was after the declaration of a state of emergency over Kenya in 1952 that all the schools run by patriotic nationalists were taken over by the colonial regime and were placed under District Education Boards chaired by Englishmen. English became the language of my formal education." Then: "one of the most humiliating experiences was to be caught speaking Gikuyu in the vicinity of the school. The culprit was given corporal punishment—three to five strokes of the cane on bare buttocks—or was made to carry a metal plate around the neck with inscriptions such as I AM STUPID or I AM A DONKEY." Of the button system he writes: "children were turned into witchhunters".
- scan p. 12: "Orature (oral literature), in Kenyan languages stopped. In primary school I now read simplified Dickens and Stevenson alongside Rider Haggard."
- scan pp. 5–6 (the contrary view among his contemporaries): he quotes Mphahlele, that English and French "have become the common language with which to present a nationalist front"; Senghor commending Diop for using French "to rescue the spirit and style of old African fables"; and Achebe in 1964 on the African writer and English. (Quoted by Ngũgĩ; I did not open those texts.)

**Bearing.** 1 supports for Kenya after 1952 (a participant account, not an official count). 2: Ngũgĩ names the objection in 1986, and his own account shows African writers of the 1960s divided. 3 complicates (one colony). 4: the wrong is the displacement of a literate vernacular and an oral tradition by another language of schooling. Supports the break from literacy as such. 5: he reports he was literate in Gikuyu before the change.

---

### 11. Bromham et al., "Global predictors of language endangerment and the future of linguistic diversity," *Nature Ecology & Evolution*, 2022 — `bromham2022global`

- **Reference.** Bromham, Lindell; Dinnage, Russell; Skirgård, Hedvig; Ritchie, Andrew; Cardillo, Marcel; Meakins, Felicity; Greenhill, Simon; Hua, Xia. 2022. *Nat Ecol Evol* 6(2): 163–173. DOI 10.1038/s41559-021-01604-y (online 16 Dec 2021; Crossref-resolved, title matched). Open access (CC BY 4.0). PMC8825282.
- **Read status.** Read in part: abstract, introduction, the Discussion paragraphs on schooling, the variable table. No page numbers in the Europe PMC XML; locators are section names. A Publisher Correction exists (`10.1038/s41559-022-01684-4`); I did not read it, so I cannot say what it changed.
- **Scale.** World: 6,511 spoken languages, "over 90% of the world's spoken languages", 51 predictor variables.
- **Attribution.** *Years of schooling*, a national average (Barro–Lee data), not literacy rates and not language of instruction. The authors say they cannot resolve variation within countries.

**Quotations.**
- Abstract: "Higher average years of schooling is also associated with greater endangerment, evidence that formal education can contribute to loss of language diversity. Without intervention, language loss could triple within 40 years, with at least one language lost per month."
- Main text, first paragraph: "Of the approximately 7,000 documented languages, nearly half are considered endangered."
- Discussion: "There is consistent global support for higher average levels of schooling being associated with greater language endangerment (Fig. 1). The association between schooling and language endangerment cannot be interpreted as a side effect of growing socioeconomic development, because years of schooling is a much stronger predictor of endangerment patterns than other socioeconomic indicators. Instead, it is consistent with a growing number of studies showing a negative impact of formal schooling on minority language vitality, particularly where bilingual education is not supported or, in some cases, is actively discouraged." And: "having a minority education policy is not globally associated with reduced threats to language diversity".
- Abstract: "contact with other languages per se is not a driver of language loss."

**Bearing.** 3: the only world-scale, quantified source in this facet. It is cross-national and correlational, and it measures schooling, not literacy teaching and not coercion. It cannot tell a forced school from a wanted one. 5: complicates. "Language loss could triple within 40 years" is the authors' model projection, not a count of what has been lost.

---

### 12. Moseley (ed.), *Atlas of the World's Languages in Danger*, 3rd edition, UNESCO, 2010 — `moseley2010atlas`

- **Reference.** Moseley, Christopher, ed. 2010. *Atlas of the World's Languages in Danger.* 3rd ed. Paris: UNESCO Publishing. unesdoc 187026 (archived copy, #16).
- **Read status.** Read in part: Preface and Introduction (printed pp. 5–18), the North-east Asia section (p. 49), table pages searched. Printed page = PDF page minus 2. Two-column layout: the quotations below are re-assembled from one column.
- **Scale.** World (regional editors by chapter), 2010 snapshot.
- **Attribution.** Language endangerment broadly. The Atlas treats literacy as a factor *in maintenance* and warns the evidence is confused.

**Quotations.**
- p. 5: "the number listed in the present edition now approaches the estimate generally accepted by linguists of some 2,500 endangered languages worldwide."
- p. 12: "Lastly, a word should be added about an all-important factor in the transmission of language: literacy. … First, the speakers may possess literacy, but not in their own tongue – rather, in one of greater prestige and a longer written tradition."
- p. 18: "The presence of a written form of an indigenous language will usually contribute to its preservation, enhance its prestige relative to other languages, make the language transmissible to unseen generations and locations, and thus ensure its future. Unfortunately the issue is not clear-cut, … too often, in the available data, mother-tongue literacy and second- or majority-language literacy are confused. Some endangered languages, such as Sorbian in Germany, do have a literary standard (in this case, two distinct standards) and a high degree of mother-tongue literacy, but this has not prevented its endangerment. Perhaps it has delayed its extinction."
- p. 49 (North-east Asia, Russia): "the system of compulsory education during the Soviet period involved the forced separation of children from their native communities. In the school centres, the children were placed in multiethnic boarding schools in which Russian was the only language. Returning to their native communities after completing their education, children no longer mastered their own ethnic languages."
- p. 20 (Africa, PDF p. 22; a caption on the page names Matthias Brenzinger and Herman Batibo): "Up to 10 per cent of the African languages – especially those spoken by small speech communities – may disappear within the next hundred years." (A projection by regional authors.)

**Bearing.** 3 supports as a world-scale frame. The Atlas contradicts a simple "literacy kills languages" claim: a written form "will usually contribute" to preservation. The harm it names is the replacement of the language of schooling. It gives no count of extinct languages in the pages I read ("not found").

---

### 13. Finnegan, *Oral Literature in Africa*, 2012 open edition (first published 1970) — `finnegan2012oral`

- **Reference.** Finnegan, Ruth. 2012. *Oral Literature in Africa.* Cambridge: Open Book Publishers. DOI 10.11647/obp.0025 (the Crossref `query.bibliographic` returned this monograph record; a direct `/works/` call failed). OAPEN copy via archive.org.
- **Read status.** Read in part: Chapter 2 passage on missionary linguistics (pp. 30–31); keyword search of the rest.
- **Scale.** Continent (Africa), nineteenth to twentieth centuries.
- **Attribution.** Missionary linguistics *recorded* oral texts. The book is about oral literature as literature, not about loss.

**Quotation.** pp. 30–31: "The main motive of many of these linguistic studies was to aid the evangelization of Africa, and grammars, vocabularies, and collections of texts appeared by and for missionaries. There was close collaboration between linguists and missionaries, and many of the great collections of texts in the nineteenth century were a result of professional or amateur linguists working in full sympathy with the missionary movement."

**Bearing.** 4 and 5: complicates. The missionary effort that brought writing also produced the written record of oral texts. I found no passage on measured loss of oral traditions in the parts I searched ("not found").

---

### 14. Script reform: abstract-level sources only

All four were reached through Consensus and are **abstract only**. I quote only what the abstract says.

- **Wood, M. M. 1929.** "Latinizing the Turkish Alphabet: A Study in the Introduction of a Cultural Change." *American Journal of Sociology* (issued September 1929 per Crossref). DOI 10.1086/214978 (`wood1929latinizing`). Abstract: "The old Turkish writing required nearly five hundred separate Arabic characters. Its difficulty to learn was a factor in Turkish educational lag and isolation from European culture." "In November, 1928, the Grand National Assembly passed a law forbidding the use of the old writing in newspapers and other periodicals after December 1, 1928". "All people between the ages of sixteen and forty eventually will be subject to fine if they cannot read or write Turkish in the new alphabet and have not attended school." This is a 1929 report written close to the event; the abstract calls it "a remarkable example of the quick acceptance by a people of a basic cultural change instituted by their leaders." The stated ground was ease of learning.
- **Dietrich, A. 2006.** "Language policy and the status of Russian in the Soviet Union and the successor states outside the Russian Federation." *Australian Slavonic and East European Studies* (`dietrich2006language`). Abstract: in 1925 "all materials printed in the Arabic script were banned"; Latin was adopted for Kazakh, Tajik, Uzbek, Kyrgyz and Turkmen "between 1927 and 1930"; "between 1938 and 1940, the Latin alphabet was abandoned in favour of the Cyrillic script throughout Central Asia". Aims included "increasing literacy and creating new alphabets."
- **Musaev, V. 2019.** "Script Reforms in Early Soviet Ethnic Policy." *Vestnik of Saint Petersburg University. History.* DOI 10.21638/11701/spbu02.2019.408 (`musaev2019script`). Abstract: "In total in the early thirties, 66 alphabets were Latinized". Latinization was tied to "overcoming 'remnants of the past'", in particular Arabic script for traditionally Muslim peoples.
- **Contested claims, abstract only.** Can (2023, *Journal of Oriental Studies*, DOI 10.26577/jos.2023.v104.i1.01) says Soviet policy aimed to cut Turkic peoples off from the past; Shegebayev (2019, DOI 10.1007/978-3-030-02438-3_216) says the adapted Latin alphabet "played an important role in nation building and elimination of illiteracy". I did not add these to the bib file because I read neither past the abstract.

**Bearing.** These are the one case where *literacy teaching itself was the stated purpose of the imposition* (Wood; Dietrich's "increasing literacy"), and the objection was about severance from earlier texts and religious learning (Can; Islam 2026 abstract). I cannot confirm any literacy result or any objector's words from them. Scale: nation (Turkey) and union (USSR).

---

### 15. Collins and Blot, *Literacy and Literacies: Texts, Power, and Identity*, 2003 — `collins2003literacy`

- **Reference.** Collins, James, and Richard K. Blot. 2003. Cambridge: Cambridge University Press. DOI 10.1017/cbo9780511486661 (Crossref-resolved, title matched).
- **Read status.** **Not accessible.** Cambridge Core returned 404 via WebFetch (#23); no full text found. Chapter titles and pages verified from Crossref: `.004` "The literacy thesis: vexed questions of rationality, development, and self" (pp. 9–33); `.005` "Situated approaches to the literacy debate" (34–66); `.006` "Literacies and power in modern nation states: Euro-American lessons" (67–98); `.007` "Literacies and identity formation: American cases" (99–120); `.008` "Literacy, power, and identity: colonial legacies and indigenous transformations" (121–154).
- **Chapter 4 flag.** The lead said "ch. 4 especially". Crossref gives DOI suffixes, not chapter numbers. If the Introduction is unnumbered and `.004` is chapter 1, then chapter 4 is `.007` ("American cases", pp. 99–120). That is an inference. The colonial-legacy chapter is `.008`. A human should check the table of contents.

---

### 16. Mignolo, *The Darker Side of the Renaissance: Literacy, Territoriality, and Colonization*; Street, *Literacy in Theory and Practice*

- **Mignolo** (`mignolo1995darker`). Internet Archive record `darkersideofrena0000mign` gives: Ann Arbor: University of Michigan Press, date "1994" in the record, ISBNs 047210327X / 9780472103270 (paper) and 0472084372 / 9780472084371. **Not accessible**: the full-text file redirected (302; borrow-only). The year differs from what I would have written from memory; the imprint year must be checked against the book.
- **Street** (`street1984literacy`). Cited from the repo's existing record (copied unchanged from the Part 1 bib). Crossref has no record for the 1984 book itself (#29), only reviews and Street 2013. **Not opened.** Under the standing ruling in the plan, Street's critique stands; I added nothing from it.

---

## (c) Synthesis by question

Throughout: *literacy teaching* means teaching to read or write; *schooling* means the institution; *removal* means taking the child from the family; *language suppression* means banning or punishing a language. No source I could open attributes a harm to literacy teaching alone.

### F1. Canadian Indian Residential Schools (1880s to late 1990s)

- **What was done.** Children were taken from their families, placed in church-run, federally funded schools, made to work half the day, forbidden to speak their languages, and punished for it. At least 150,000 passed through (TRC, p. 3). The TRC counts 3,201 reported deaths on its registers (p. 92).
- **To whom, where, when.** First Nations, Métis and Inuit children across Canada. Federal industrial schools opened 1883–84 (Battleford, Qu'Appelle, High River; TRC p. 57, PDF p. 64). The last federally supported schools closed in the late 1990s (p. 3).
- **Stated ground.** Macdonald 1883: a child at a day school on the reserve "may learn to read and write" but remains "a savage who can read and write"; the child must be removed to acquire "the habits and modes of thought of white men" (p. 2). Scott 1920: absorption "into the body politic" (p. 3). The TRC adds a fiscal and land motive (p. 3).
- **What literacy was.** Both a stated tool (Dewdney 1883: "reading, writing and speaking the English language rather than that of Cree", p. 80) and a failed output ("Grade Three achievement, and sometimes without even the ability to read", p. 145). One school, Onion Lake, taught reading and writing in Cree and English (p. 81) and the TRC calls it an exception.
- **Who objected at the time.** Bryce (1907), Napahkesit (1917), Cowessess parents (1949, successful), Shoal Lake parents (1917, principal resigned), Dene Treaty-payment refusal (1937), the League of Indians (1931), Oblate Superior General Labouré on punishment severity (1935) (TRC pp. 80–81, 96, 117). The TRC says families and Treaties valued education (p. 144), so the objection was not to schooling as such.
- **What ended it.** Gradual closure by the 1980s; the last federally supported schools by the late 1990s (p. 3). The mechanism of ending: not found in what I read.

### F2. United States Indian boarding schools (1819–1969)

- **What was done.** 408 federal schools in 37 states or territories, with compulsion by law and by withholding rations, English-only rules, renaming, hair-cutting, military discipline, unpaid labour (Vol. I, pp. 91–92). At least 973 documented child deaths and 74 burial sites at 65 schools (Vol. II, pp. 15–16).
- **To whom, where, when.** American Indian, Alaska Native and Native Hawaiian children, 1819–1969.
- **Stated ground.** Officials' words as printed by the Department: Kennedy Report's account of the design to "force the complete abandonment of his native language" (p. 51); the 1904 Commissioner's report that learning English is "the first step in his training" (p. 54); and the 1902 caged-bird passage of Commissioner Jones (Vol. I, p. 51; I read only its opening).
- **Who objected at the time.** Indigenous families who refused to send children (Kennedy Report, quoted on p. 35); Congress responded with compulsion (the 1893 ration-withholding Act, p. 35–36). The Meriam Report (1928) named the boarding school as the chief damage to family life (p. 38). The Department's report does not give other objectors in the pages I read.
- **What ended it.** Not found in what I read.

### F3. Australia, removal of Indigenous children (c. 1910–1970; earlier episodes from 1788)

- **What was done.** "between one in three and one in ten Indigenous children were forcibly removed" (PDF p. 31), many into dormitory institutions that taught "basic literacy, numeracy and hygiene" for service work (PDF p. 137), and where the use of Aboriginal languages was forbidden by some missions into the 1960s (PDF p. 133).
- **Stated ground.** Protection and "best interests" (Neville, PDF p. 95); assimilation (McLean, PDF p. 53).
- **Who objected at the time.** McGarry and another member of the NSW Parliament, 1914–15 (PDF p. 36); the Broome women (PDF p. 95); Aboriginal parents who left the stations (PDF p. 36). 
- **What ended it.** Not found in what I read.
- **Caution.** Literacy teaching is peripheral here. The wrong is removal.

### F4. Language of instruction imposed

| Case | What | Ground | Objectors | Source and depth |
|---|---|---|---|---|
| British India, 1835 | English as the funded language of higher instruction; no mass schooling | form "interpreters between us and the millions" | Orientalists on the Committee (text not opened) | Macaulay [34], transcription, in part |
| Wales, 1840s | "Welsh stick" in schools; English-only inquiry | "vast drawback"; "manifold barrier" | Jane Williams 1848 (abstract); the Blue Books record the stick's "injurious effects" | Blue Books pp. 309, 452; Johnes pp. 51, 103, 309 |
| Hawaii, 1888–1902 | Hawaiian-medium schools reduced to 16 percent of children by 1888; 203 English-required schools by 1902 | not found in what I read | not found | FIBSI Vol. I pp. 75–77 |
| Kenya, after 1952 | Gikuyu-medium nationalist schools taken over; English the language of schooling; Gikuyu punished | not stated by the colonial side in what I read | Ngũgĩ, writing in the 1980s; other writers in the 1960s argued the other way | Ngũgĩ, scan pp. 9–12 |
| Soviet North, 20th century | Boarding schools in which Russian was the only language | not found | not found | Moseley 2010, p. 49 |
| France, 1794 | Proposal to eliminate *patois* and universalise French | national unity and access to the law | not found | Grégoire, transcription |

### F5. Script reform

- **What was done.** Turkey replaced Arabic script by law from 1928, with fines for adults unable to read the new script who had not attended the new national schools (Wood 1929, abstract). The USSR Latinized, then in 1938–40 Cyrillicized, the scripts of Central Asian peoples (Dietrich 2006, abstract). 66 alphabets were Latinized in the early 1930s (Musaev 2019, abstract).
- **Stated ground.** Ease of learning and mass literacy (Wood; Dietrich), and "overcoming remnants of the past" (Musaev).
- **Who objected.** Abstract-level claims only that Kazakh intellectuals (Baitursynov) preferred a reformed Arabic script (Islam 2026 abstract, via Consensus). I did not open the source and I do not carry it into the bib.
- **Evidence status.** Weakest part of the facet. I read no full text.

### F6. The measured loss of languages

- **What the best source shows.** Bromham et al. (2022): about 7,000 documented languages, nearly half endangered; years of schooling, a national average, is a stronger predictor of endangerment than other socioeconomic variables; contact between languages "per se is not a driver". UNESCO (2010): about 2,500 endangered languages, and literacy in a written form usually helps preservation.
- **What it does not show.** That literacy teaching causes loss; that a particular school was coercive; any count of oral traditions lost. I found no measured count for oral traditions. Finnegan (2012) and Ngũgĩ (1986) assert displacement of oral literature by schooling (Ngũgĩ: "Orature … stopped" in his school) without a count.

### Claims the sources contradict

1. **"Literacy teaching harmed Indigenous peoples."** The TRC, the US Department and the Australian inquiry attribute the harm to removal, labour, abuse and language suppression. Macdonald's 1883 statement says reading and writing were not what he wanted taught at home. "Literacy" does not appear in either US volume or in the TRC Summary.
2. **"The Welsh Not beat Welsh out of children."** Johnes (p. 103) says it did not, and that it hindered the learning of English. The Blue Books mention it once (Johnes p. 51; my search of Part III found the single passage on p. 452).
3. **"Schooling and written forms kill languages."** The UNESCO Atlas (p. 18) says a written form "will usually contribute" to preservation, and cites Sorbian as a case where mother-tongue literacy did not prevent endangerment. Bromham et al. find schooling, not contact, is the global predictor. These are not in direct conflict, but they point to the language of instruction, not literacy, as the variable.
4. **"The colonised resisted schooling."** The TRC (p. 144) says Treaties and families valued education. Johnes (p. 309) says Welsh parents wanted English. Ngũgĩ was literate in Gikuyu and had an ovation for a Gikuyu composition (scan p. 10). Objections were to the terms.
5. **"Colonial rule promoted mass literacy."** Macaulay [34] says the means were too limited "to educate the body of the people"; the TRC reports Grade Three and half the enrolment reaching Grade Six in the 1950s (p. 145).
6. **Scholars of the day on African languages in school.** Ngũgĩ (1986) against English as the language of literature; Mphahlele, Senghor and Achebe, as Ngũgĩ quotes them, for it. Not a contradiction in facts but in contemporaries' ground.
7. **Death counts.** US Vol. I "over 500" at 19 schools; Vol. II "at least 973". The Department says the first was provisional. Canada's 3,201 (TRC) is a different system and registry. They should not be added together.

**On the five problems.**
1. *Documented wrongs*: F1–F3 are well documented in official reports. F4 is documented for Wales and Hawaii; F5 and the oral-tradition loss are not documented to the standard.
2. *Presentism*: contemporaries named F1, F2, F3 and F4 (Wales, in the Blue Books themselves and by Williams) as wrongs. For India, France, Hawaii, Soviet Siberia, I found no contemporary objector in what I opened.
3. *Scale*: all but Bromham and Moseley are national or regional. Nothing here is a world-scale account of coerced literacy.
4. *The comparison may break*: in every documented case the instrument was custody of the child or control of the language of instruction, not the competence. Script reform is the exception, where the competence was the stated goal.
5. *The literacy myth*: in the sources I opened, the stated aims of the boarding schools were assimilation, 'civilizing' and Christianizing (TRC p. 144), and I found no promise of literacy returns; the TRC finds the schools failed even at elementary teaching.

---

## (d) Gaps and unverified leads

**Sources I could not open or only saw in abstract.**
- Mignolo 1995, *Darker Side of the Renaissance*. Borrow on archive.org (`darkersideofrena0000mign`) or a library; check the imprint year.
- Collins and Blot 2003. Chapter list verified from Crossref; full text at Cambridge Core (`10.1017/cbo9780511486661`), library access. The chapter numbering needs checking against the table of contents.
- Street 1984. Library copy; no record found in Crossref.
- The full Canadian TRC Final Report (six volumes), especially vol. 1 *Origins to 1939* and vol. 2 *1939–2000*, which the US Department of the Interior cites. I read only the Summary.
- Original ARCIA volumes (1850–1906), the Kennedy Report (1969) and the Meriam Report (1928). I read them only through the Department's quotations.
- Bryce 1907 *Report on the Indian Schools of Manitoba and the North-West Territories*, and Bryce 1922 *The Story of a National Crime*. TRC cites both.
- Macaulay 1835 in print (Sharp 1920, *Selections from Educational Records*, Part I). Also H. T. Prinsep's and other Orientalist minutes of 1835, for the objections.
- Johnes's sources on the Welsh Not; Roberts 2020 and Jane Williams's *Artegall* (1848); G. E. Jones 2006 on the "Treason of the Blue Books".
- Wood 1929, Dietrich 2006, Musaev 2019, Can 2023, Islam 2026, Shegebayev 2019: abstract only. Any claim about the Turkish or Soviet reforms needs the full text; also Soviet *likbez* literacy campaign figures, which I did not search.
- The UNESCO Atlas online database (the current, interactive edition) and Ethnologue (SIL), for counts. I did not open Ethnologue. Krauss 1992 (*Language* 68) and Nettle and Romaine on language death: not searched.
- Ngũgĩ's book in a print copy with page numbers.
- Finnegan 2012: search for passages on oral literature under colonial schooling and for any measured loss.
- Goody and Finnegan on oral traditions beyond Finnegan's chapter 2: not pursued here. The plan's standing ruling says no claim of cognitive restructuring.

**Leads I did not follow.**
- India: William Adam's 1830s surveys of indigenous schools in Bengal; the later debate over them. Not searched, so I make no claim.
- Missionary scripts and Bible translation as literacy imposed or offered (Africa, Pacific, the Americas). Finnegan p. 30–31 is the only source here.
- The Philippines, French West Africa, Belgian Congo, Algeria, Quebec, Ireland, Scotland and Gaelic (the Statutes of Iona), Sámi and Greenland schools, Norwegianisation, Prussian Poland, Japanese policy in Korea and Ainu schooling. None searched.
- Sources from the objectors' side in their own words (petitions, chiefs' speeches, Welsh press 1847–48). I have the objectors' names from the official reports and one abstract.
- Why and how the US and Canadian systems ended. Not found in what I read.

**Tool notes.** Scholar Gateway failed (#17). Unpaywall could not be used (#11). OpenAlex was over budget (#24). The humanrights.gov.au, AustLII and Columbia pages are behind bot walls (#4, #5, #7); I used archived copies of the first and third. A human with a browser can open them directly.
