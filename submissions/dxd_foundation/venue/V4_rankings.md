# V4 — Rankings table and the meaning of "tier A"

*Compiled 2026-10-13 by the V4 agent. Every cell comes from a file or page opened this session; anything else is "not verified". The ABDC cells are parsed by script from the official workbook. No Chrome tools were used and no wall was bypassed.*

## Part 1 — what "tier A" could mean for this author

### Bentley University

I found no Bentley journal list, research-quality tier, or "A journals" document that I could open.

- `https://www.bentley.edu/phd` (opened): names no journals and sets no publication requirement. It says finalists submit "an 8 to 10 page research proposal" that "will serve as an early preview of a dissertation topic" (this text describes the Executive PhD).
- `https://bentley.edu/offices/phd` (opened): "There is less of a focus on producing publishable work" (a contrast with the DBA). No journal list, no placement statement.
- `https://www.bentley.edu/academics/phd-programs/phd-business` (HTTP 403 to curl and WebFetch; **not opened**). A web-search summary of this page says it names Academy of Management Journal, Strategic Management Journal and Organization Science as outlets where Bentley faculty have published. This is a search-engine summary only: **not verified**, and the claim concerns faculty, not a rule for students.
- `https://catalog.bentley.edu/graduate/programs/phd-programs/business-phd/` returned an empty body (HTTP 202); **not read**. The search summary says only that full-time tracks prepare students to "conduct rigorous, publishable research". **Not verified.**
- The PhD student handbook (reached via `https://www.bentley.edu/offices/registrar/student-catalogues`) was not retrieved. If Bentley defines "top-tier", it would be there, in the faculty/promotion guidelines, or from the PhD office. **Ask the programme director.**
- Tracks named in the search summary: Information Systems, Management, Marketing, Business Analytics (Business PhD); the Executive PhD offers Leadership, Advanced Business Analytics, Experience Design. Bentley is AACSB-accredited (catalog accreditation PDF listed in search; not opened).

### How the common "A" definitions work (from the sources opened)

I did not find a source that states how US business schools "commonly" define A journals, so I make no claim about common practice. The five candidate definitions are the ones in the table below.

- **UT Dallas 24:** a fixed list of 24 journals used to rank schools by publication counts, not a quality grade. Official page (opened with curl; WebFetch failed on a certificate error): `https://jsom.utdallas.edu/the-utd-top-100-business-school-research-rankings/`.
- **FT50:** a fixed list of 50 journals used in the Financial Times research rank. The official ft.com page returned HTTP 403 (bot wall) to curl and "unable to fetch" to WebFetch, so FT50 cells are **secondary**, from two university library guides (see notes).
- **ABDC JQL:** grades A*, A, B, C. Official workbook downloaded.
- **Chartered ABS AJG:** grades 4*, 4, 3, 2, 1. Login-walled; secondary copy used.

## Part 2 — the rankings table

### Sources and editions

| Source | Edition used | Status |
|---|---|---|
| ABDC JQL | The workbook `ABDC-JQL-2025-v3-210926.xlsx` ("2025 major review ... Current to September 2026") holds a **2025 sheet** and a **2022 sheet** ("review finalised 15 March 2023"). I report both. Official file: `https://abdc.edu.au/wp-content/uploads/2026/09/ABDC-JQL-2025-v3-210926.xlsx`, linked from `https://abdc.edu.au/abdc-journal-quality-list/`. | Official, opened |
| Chartered ABS AJG | **2024** edition (1,822 journals, per the sheet header and `https://businessperspectives.org/about-us/news/academic-journal-guide-2024`). Read from a **third-party Google Sheet copy** (`https://docs.google.com/spreadsheets/d/1AC3zhcbK4Kjb-ZkffDJTsujqLmKx5H9I`, exported as xlsx), not from charteredabs.org (that page returned 404 to curl; the guide is login-walled). | **Secondary and unofficial.** No library guide found. Treat as unconfirmed until checked at charteredabs.org. |
| FT50 | List shown by Bodleian Libraries (last updated 14 May 2026; has a "Journals Removed from the FT50 - 2026" section naming Human Relations, Journal of Business Ethics, Organization Studies): `https://libguides.bodleian.ox.ac.uk/ft-top50`. Cross-checked against Sheridan College (last updated 1 Oct 2026): `https://sheridancollege.libguides.com/ft50list`. The two guides agree on every journal in this table. | **Secondary** (ft.com blocked) |
| UTD 24 | Current list on the official page above | Official, opened |
| Scimago SJR | `scimagojr.com` returns a Cloudflare challenge (HTTP 403) to curl and WebFetch, for both the journal pages and the CSV download | **Not verified, all rows** |
| Impact factor | Only journal-owned pages that opened are used. Most publisher sites (Sage, T&F, Elsevier, Wiley, AOM, INFORMS, ACM, Springer) returned HTTP 403 or an auth redirect, or showed no figure in the static page | See column |

ABDC note: "absent" means the title and its ISSN do not appear in that sheet, i.e. unrated by ABDC, not rated C. The Springer pages (EIT, AI & Society, Philosophy & Technology, JBE, JCP) opened but stated no impact factor in their static HTML.

### Table

Columns: ABDC 2025 sheet (ABDC 2022 sheet in brackets if it differs); ABS 2024 (secondary); FT50 (secondary); UTD 24; SJR; stated impact factor.

| Journal | ABDC 2025 [2022] | ABS 2024 (sec.) | FT50 | UTD 24 | SJR | Stated IF (own site) |
|---|---|---|---|---|---|---|
| Human Factors | absent | 3 | No | No | not verified | not verified |
| Ergonomics | absent | 3 | No | No | not verified | not verified |
| Applied Ergonomics | absent | 3 | No | No | not verified | not verified |
| Theoretical Issues in Ergonomics Science | absent | not listed | No | No | not verified | not verified |
| Journal of Cognitive Engineering and Decision Making | absent | 2 | No | No | not verified | not verified |
| International Journal of Human-Computer Studies | B | 2 | No | No | not verified | not verified |
| Human-Computer Interaction | A | 1 | No | No | not verified | not verified |
| ACM Transactions on Computer-Human Interaction | absent [A*] | not listed | No | No | not verified | not verified |
| International Journal of Human-Computer Interaction | C [B] | not listed | No | No | not verified | not verified |
| Behaviour & Information Technology | A | 2 | No | No | not verified | not verified |
| Interacting with Computers | B [C] | 2 | No | No | not verified | 1.9 (2025); 5-yr 2.2 (2025) — `https://academic.oup.com/iwc` |
| Computers in Human Behavior | A | 2 | No | No | not verified | not verified |
| Academy of Management Review | A* | 4* | Yes | Yes | not verified | not verified |
| Academy of Management Perspectives | A | 4 | No | No | not verified | not verified |
| Organization Science | A* | 4* | Yes | Yes | not verified | not verified |
| Organization Theory | A [absent] | not listed | No | No | not verified | not verified |
| Organization Studies | A* | 4 | No (removed 2026 per Bodleian) | No | not verified | not verified |
| Journal of Management Studies | A* | 4 | Yes | No | not verified | not verified |
| Journal of Management Inquiry | A | 3 | No | No | not verified | not verified |
| MIS Quarterly | A* | 4* | Yes | Yes | not verified | not verified |
| Information Systems Research | A* | 4* | Yes | Yes | not verified | not verified |
| Journal of the Association for Information Systems | A* | 4* | No | No | not verified | not verified |
| Journal of Information Technology | A* | 4 | No | No | not verified | not verified |
| Information and Organization | A* | 3 | No | No | not verified | not verified |
| Information Systems Journal | A* | 4 | No | No | not verified | not verified |
| Journal of Management Information Systems | A* | 4 | Yes | No | not verified | not verified |
| Research Policy | A* | 4* | Yes | No | not verified | not verified |
| California Management Review | A | 3 | No | No | not verified | not verified |
| Design Studies | A | not listed | No | No | not verified | not verified |
| She Ji | absent | 1 | No | No | not verified | not verified |
| Design Science | absent | not listed | No | No | not verified | 2.8 (2-yr), 3.5 (5-yr); year not stated on the metrics page (banner alt text reads "2025") — `https://www.cambridge.org/core/journals/design-science/information/about-this-journal/journal-metrics` |
| New Media & Society | absent | not listed | No | No | not verified | not verified |
| Big Data & Society | absent | not listed | No | No | not verified | not verified |
| Information, Communication & Society | A | 2 | No | No | not verified | not verified |
| Journal of Computer-Mediated Communication | absent | 3 | No | No | not verified | 7.4 (2025) — `https://academic.oup.com/jcmc` |
| Science, Technology, & Human Values | A | 2 | No | No | not verified | not verified |
| Ethics and Information Technology | B [C] | 1 | No | No | not verified | not verified |
| AI & Society | absent | not listed | No | No | not verified | not verified |
| Philosophy & Technology | absent | not listed | No | No | not verified | not verified |
| Regulation & Governance | A | 3 | No | No | not verified | not verified |
| Policy & Internet | absent | not listed | No | No | not verified | not verified |
| Journal of Business Ethics | A | 3 | No (removed 2026 per Bodleian) | No | not verified | not verified |
| Business Ethics Quarterly | A | 3 | No | No | not verified | 4.3 (2-yr), 4.7 (5-yr); year not stated on the metrics page — `https://www.cambridge.org/core/journals/business-ethics-quarterly/information/about-this-journal/journal-metrics` |
| Organizational Behavior and Human Decision Processes | A* | 4 | Yes | No | not verified | not verified |
| Journal of Behavioral Decision Making | A | 3 | No | No | not verified | not verified |
| Judgment and Decision Making | A | 3 | No | No | not verified | 2.5 (2025) — `https://www.cambridge.org/core/journals/judgment-and-decision-making` |
| Behavioural Public Policy | absent | 1 | No | No | not verified | 2.9 (2025) — `https://www.cambridge.org/core/journals/behavioural-public-policy` |
| Journal of Economic Behavior & Organization | A* | 3 | No | No | not verified | not verified |
| Journal of Consumer Policy | C | 2 | No | No | not verified | not verified |
| Journal of Public Policy & Marketing | A | 3 | No | No | not verified | not verified |

Caveats on specific cells:

- **ABDC titles** matched by normalised title and ISSN (ABDC spells "Behaviour and Information Technology", "Regulation and Governance", "Journal of Economic Behavior and Organization", "Journal of Public Policy and Marketing"). Design Studies and Judgment and Decision Making are filed under FoR 3599, Regulation and Governance under 4801; the rest sit in FoR 3507 (strategy, management, organisational behaviour), 4609 (information systems) or 3801/3503/3506.
- **ACM TOCHI** is A* on the 2022 sheet and has no row on the 2025 sheet. I grepped the 2025 review report (`https://abdc.edu.au/wp-content/uploads/2026/03/JQL-Review-2025-report-26.03.26.pdf`) for "Computer-Human" and "TOCHI" and found nothing; the report says only "149 titles are removed". Whether TOCHI was removed or dropped from the sheet is **not verified**.
- **ABS "not listed"** means the title is absent from the third-party copy of the 1,822-journal list. The copy may be wrong or the title may be filed under a variant name (checked: "human computer interaction", "transactions on computer", "organization theory", "design", "new media", "big data", "society", "internet"). It is not confirmation that the official guide omits the journal. The sheet lists "Information Communication and Society" and "Science Technology and Human Values" (no ampersand/comma); I treated them as the same journals. ABS 2024 rates Human-Computer Interaction 1 and AIS Transactions on Human-Computer Interaction 2.
- **Impact factors** came from journal-owned pages on Cambridge (JDM, BPP, Design Science, BEQ) and Oxford (JCMC, IWC). The JDM and BPP pages carry the label "2025 Impact Factor". For the two Cambridge metrics pages the figure is stated without a year. I did not confirm that these are Clarivate JCR figures. The other 41 journals' pages were walled or gave no figure.

## Part 3 — which journals count as "A" under each definition

Computed from the table above. The ABS rows depend on the unofficial AJG copy.

**ABDC A or A\* (2025 sheet), 30 journals:** Human-Computer Interaction; Behaviour & Information Technology; Computers in Human Behavior; Academy of Management Review; Academy of Management Perspectives; Organization Science; Organization Theory; Organization Studies; Journal of Management Studies; Journal of Management Inquiry; MIS Quarterly; Information Systems Research; Journal of the Association for Information Systems; Journal of Information Technology; Information and Organization; Information Systems Journal; Journal of Management Information Systems; Research Policy; California Management Review; Design Studies; Information, Communication & Society; Science, Technology, & Human Values; Regulation & Governance; Journal of Business Ethics; Business Ethics Quarterly; Organizational Behavior and Human Decision Processes; Journal of Behavioral Decision Making; Judgment and Decision Making; Journal of Economic Behavior & Organization; Journal of Public Policy & Marketing.
- A\* only (14): AMR; Organization Science; Organization Studies; JMS; MISQ; ISR; JAIS; JIT; Information and Organization; ISJ; JMIS; Research Policy; OBHDP; JEBO.
- Using the 2022 sheet instead: ACM TOCHI is A\* (absent in 2025); Organization Theory is unrated; the other A/A\* journals are unchanged.
- Not A under ABDC, though they fit the topic: Human Factors, Ergonomics, Applied Ergonomics, TIES, JCEDM (all absent); IJHCS (B); IJHCI (C); Interacting with Computers (B).

**ABS 4 or 4\* (2024, secondary), 13 journals:** AMR (4\*); Organization Science (4\*); MIS Quarterly (4\*); Information Systems Research (4\*); JAIS (4\*); Research Policy (4\*); Academy of Management Perspectives; Organization Studies; Journal of Management Studies; Journal of Information Technology; Information Systems Journal; Journal of Management Information Systems; OBHDP.
- 4\* only (6): AMR; Organization Science; MISQ; ISR; JAIS; Research Policy.

**ABS 3 and above (2024, secondary), 27 journals:** the 13 above plus Human Factors; Ergonomics; Applied Ergonomics; Journal of Management Inquiry; Information and Organization; California Management Review; Journal of Computer-Mediated Communication; Regulation & Governance; Journal of Business Ethics; Business Ethics Quarterly; Journal of Behavioral Decision Making; Judgment and Decision Making; Journal of Economic Behavior & Organization; Journal of Public Policy & Marketing. (Organization Theory is not in the copy; ABDC rates it A.)

**FT50 (secondary), 8 journals:** Academy of Management Review; Organization Science; MIS Quarterly; Information Systems Research; Journal of Management Information Systems; Journal of Management Studies; Organizational Behavior and Human Decision Processes; Research Policy. (Organization Studies and Journal of Business Ethics were on the earlier list and are shown as removed in 2026 by Bodleian.)

**UT Dallas 24 (official), 4 journals:** Academy of Management Review; Organization Science; MIS Quarterly; Information Systems Research.

## What the author should settle

- None of the five human-factors journals (Human Factors, Ergonomics, Applied Ergonomics, TIES, JCEDM) is rated by ABDC; on the unofficial ABS copy Human Factors, Ergonomics and Applied Ergonomics are 3 and JCEDM is 2. If "tier A" means ABDC A/A\*, FT50 or UTD 24, the paper has to go to a management, organisation or information-systems journal.
- Organization Theory is ABDC A on the 2025 sheet only (unrated in 2022), and absent from the ABS copy.
- Verify with the Bentley PhD office what the programme counts, and confirm the ABS grades and the FT50 membership at charteredabs.org and ft.com, which I could not open.
