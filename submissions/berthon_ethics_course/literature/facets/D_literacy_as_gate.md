# Facet D — literacy made a condition of standing (2026-10-13)

Agent-drafted. The author has not reviewed it, and none of the text is the author's.

Files: `D_literacy_as_gate.md` and `D_literacy_as_gate.bib`. Local copies of everything opened are in
`~/iit-playground/berthon_ethics_local/pdfs/D/` (not in the repo).

## What this facet covers

Places where the ability to read or write (sometimes "understand" or "interpret") was written into law as a
condition of standing: the vote (United States, Brazil, Peru, Chile), admission to a country (United States,
Natal, Australia), jury service, office and military rank. For each I record who designed the test, what its
authors said it was for, how it was administered, what it did to the people it met, who objected at the
time, and how it ended.

## The question the synthesis answers

Where was literacy made a condition of standing, who designed the test, what did its authors say it was
for, how was it administered, what did it do, and how did it end? The synthesis takes each documented
failure in turn (section c) and ends with the claims the sources contradict.

## Legend for read status

- **read in full**: I read the whole text of the item as served (a short page, a short message, a statute
  page).
- **read in part**: I read the stated pages or sections and not the rest. The locators say which.
- **abstract only**: I saw only an abstract or catalogue record.
- **not accessible**: I could not open the text; only the bibliographic record is verified.

Quotations come only from text I opened in this session. "Not found" means I looked and the sources I
opened do not say. Page numbers for U.S. Reports, Statutes at Large and the Virginia debates are the
printed page numbers in the scans I read. Where the web edition has no page numbers (Hansard on
historichansard.net, Cornell LII) I give the speaker and date.

## (a) Search log

| # | Source or tool | Exact query or URL | Hits | Notes |
| --- | --- | --- | --- | --- |
| 1 | Scholar Gateway `semanticSearch` | "literacy tests voting disfranchisement Southern constitutional conventions Kousser" | none | `ACCESS_DENIED: Access denied`. Failed as in earlier runs. |
| 2 | Justia (curl) | supreme.justia.com/cases/federal/us/{360/45, 170/213, 400/112, 395/285, 383/301} | none | HTTP 403 bot wall on all five. Not used. |
| 3 | Library of Congress `tile.loc.gov` (curl) | usrep PDF paths for 360/45 etc. | none | First attempts 404 (my URL error); later attempts with the corrected path returned code 000 from curl. Used govinfo instead. |
| 4 | govinfo US Reports (curl) | `govinfo.gov/content/pkg/USREPORTS-{360,170,238,395,383,400}/pdf/USREPORTS-<vol>-<page>.pdf` | 6 PDFs | Official copies; text extracted with `pdftotext`. Used for all U.S. Reports quotations. |
| 5 | Cornell LII (curl) | law.cornell.edu/supremecourt/text/{360/45, 170/213, 400/112, 395/285, 383/301, 238/347} | 6 pages | No page numbers; used only to cross-check wording of Oregon v. Mitchell. |
| 6 | govinfo Statutes at Large (curl) | `STATUTE-79/pdf/STATUTE-79-Pg437.pdf`; `STATUTE-89-Pg400`; `link/statute/84/314`; `link/statute/39/874` | 4 PDFs | Direct `STATUTE-84-Pg314` and `STATUTE-39-Pg874` PDFs held one page only; the `govinfo.gov/link/statute/<vol>/<page>?link-type=pdf` form returned the full run (6 and 25 pages). |
| 7 | WebSearch | "Wilson veto message immigration bill literacy test January 29, 1917 ..." | 10 | Located UCSB and Woodrow Wilson Library copies. |
| 8 | presidentwilson.org (curl) | /items/show/22067 | blocked | Anubis proof-of-work bot wall. Not bypassed. |
| 9 | UCSB American Presidency Project (curl) | presidency.ucsb.edu/documents/message-the-house-representatives-returning-without-approval-act-regulate-the-immigration | 1 page | Full text of Wilson's 29 Jan 1917 message. |
| 10 | WebSearch | "Alabama constitutional convention 1901 John B. Knox 'establish white supremacy in this State' ..." | 10 | Snippets only; then went to archive.org for the primary. |
| 11 | archive.org advancedsearch | title: constitutional convention, Alabama/Mississippi/Virginia/Louisiana, 1890-1903 | 15 | Found Alabama 1901 proceedings (4 vols), Louisiana 1898 journal, Virginia 1906 debates. |
| 12 | archive.org download | `alabama-constitutional-convention-proceedings-1901-v1/CC_1901_v01_djvu.txt` | 1 | Knox address located. |
| 13 | archive.org download | `officialjournal03convgoog_djvu.txt` (Louisiana 1898 journal) | 1 | Searched "supremacy", "Kruttschnitt". The opening address I looked for is not in the text I searched; nothing quotable found. Not used. |
| 14 | archive.org download | `reportofproceedi21virg_djvu.txt` (Virginia debates, vol. 2) | 1 | Glass speech of 4 Apr 1902 located. |
| 15 | archive.org advancedsearch | Mississippi 1890 convention proceedings; South Carolina 1895 convention journal | 0 usable | Mississippi: no hit. South Carolina: only a JSTOR item (jstor-27527896), not opened. Tillman is quoted second-hand through *South Carolina v. Katzenbach*. |
| 16 | archive.org advancedsearch / metadata / download | Kousser, *Shaping of Southern Politics* (`shapingofsouther0000kous`); Keyssar, *Right to Vote* (`righttovote00alex`) | metadata only | `_djvu.txt` returns HTTP 401: lending library. Not accessible. |
| 17 | Crossref | query.bibliographic "Kousser Shaping of Southern Politics" | 3 | Only JSTOR book-review records (10.2307/2206040, /202401, /1851337); not the book. |
| 18 | WebFetch | foundingdocs.gov.au/item-did-16.html (prompt for the Act's text) | 1 | The page does not hold the Act's text; links to a transcript PDF. Re-fetched with curl. |
| 19 | curl | foundingdocs.gov.au/resources/transcripts/cth4ii_doc_1901a.pdf | 1 | Transcript of Act No. 17 of 1901 (7 pp.). |
| 20 | curl | historichansard.net/hofreps/1901/{19010806,19010807,19010808,19010906}_reps_1_{3,4}/ | 4 | 7 Aug 1901 holds Barton's second-reading speech; 6 Sept 1901 holds later members. |
| 21 | WebSearch | "Natal Immigration Restriction Act 1897 text 'write out in the characters of any language of Europe' ..." | 10 | The Act itself not returned. Found the ANU Press chapter by Lake. |
| 22 | curl | press.anu.edu.au/downloads/press/p97101/mobile/ch13s0{2..6}.html | 5 | Lake, ch. 13. Footnotes not opened. |
| 23 | Crossref | DOI 10.22459/cw.03.2006 | 1 | *Connected Worlds*, eds Curthoys and Lake, ANU Press, issued 2006-03. |
| 24 | WebSearch | "Brasil Emenda Constitucional nº 25 de 15 de maio de 1985 voto do analfabeto ... Lei Saraiva 1881" | 9 | Led to the UnB article. Planalto and Câmara pages did not open (curl code 000 / HTTP 404; WebFetch ECONNRESET). Text of EC 25/1985 and Decreto 3.029/1881 **not opened**. |
| 25 | curl | repositorio.unb.br/bitstream/10482/20670/1/ARTIGO_AnalfabetosVoto.pdf | 1 | Aleixo and Kramer 2010. Two-column PDF; I read the raw-order extraction. |
| 26 | WebSearch | "literacy requirement for voting worldwide history countries abolished illiterate suffrage Latin America Brazil Peru Ecuador ..." | 10 | Found Nicolau (Oxford CBS working paper). No world-scale comparison found. |
| 27 | curl | brazil.ox.ac.uk/.../nicolau26.pdf | 1 | Nicolau 2002, 51 pp. |
| 28 | WebSearch | "Peru 1979 Constitution illiterate right to vote ... artículo 65" | 9 | Snippets name a PUCP thesis. |
| 29 | curl / WebFetch | repositorio.pucp.edu.pe/index/handle/123456789/201287; tesis.pucp.edu.pe/items/34e4410d-.../full | 0 | HTTP 403 (curl); WebFetch timed out. The thesis on illiterate suffrage in the southern Andes **not opened**. |
| 30 | WebSearch | "Constitución Política del Perú 1933 artículo 86 'saber leer y escribir' ... Constitución 1979 artículo 65 'analfabetos'" | 9 | Led to Ragas 2007. Text of art. 65 (1979) **not opened**. |
| 31 | curl | revistas.pucp.edu.pe/index.php/historica/article/download/233/227 | 1 | Ragas 2007, 28 pp. |
| 32 | Crossref | Ragas "Leer, escribir, votar" | 1 | DOI 10.18800/historica.200701.004, title matches. |
| 33 | WebSearch / curl | "Chile literacy requirement vote abolished 1970 Ley 17.284 ..." ; senado.cl/ciudadania/leyes-con-historia-0/la-eliminacion-del-voto-censitario-en-el-pais | 1 usable | Short Senate page read in full by curl. It does not name the 1970 law. A Berkeley catalogue record for Ley 17.284 does not mention literacy, so I do not link them. |
| 34 | WebSearch | "usccr.gov 1961 Commission on Civil Rights Report Book 1 Voting pdf ..." | 9 | usccr.gov PDF (scan, poor OCR) and crmvet.org copy (clean OCR). |
| 35 | curl | usccr.gov/files/historical/1961/61-001.pdf; crmvet.org/docs/ccr_61_voting.pdf | 2 | I read the crmvet text for pp. 139-141 and confirmed "six grades" appears in the usccr.gov scan. |
| 36 | Cornell LII (curl) | law.cornell.edu/uscode/text/28/1865 | 1 | Current text of the federal juror qualification. |
| 37 | archive.org download | `abstractsreport00benngoog` and `abstractsreport01benngoog` (Immigration Commission, *Abstracts*, 1911) | 2 | Vol. 1 pp. 47-48 (recommendation) and vol. 2 pp. 573-574 (legislative history). |
| 38 | WebSearch | "Army Special Training Units World War II illiterates fourth grade literacy standard ..." | 10 | Snippets only. DTIC ADA063747 returned HTTP 403. **Nothing on the military is used below.** |
| 39 | WebSearch | "Barton Immigration Restriction Bill second reading 1901 Hansard 'doctrine of the equality of man ...'" | 9 | I did not find the quoted sentence; I do not use it. |
| 40 | curl | naa.gov.au Immigration Restriction Act 1901 learning resource | 0 | curl code 000. Not opened. |

## (b) Entries

### Court opinions

**1. *Lassiter v. Northampton County Board of Elections*, 360 U.S. 45 (1959).** Key `lassiter1959lassiter`.
Verified: govinfo official U.S. Reports PDF `USREPORTS-360-45.pdf`; header "Argued May 18-19, 1959.—Decided June 8, 1959." Cornell LII copy agrees. URL:
https://www.govinfo.gov/content/pkg/USREPORTS-360/pdf/USREPORTS-360-45.pdf
Read status: **read in part** (statement of the case, the opinion of the Court at 50-53, and footnotes 5-7 on state practice at 51-53; the rest of the opinion at 54 not read).
Argues: a State may apply a literacy test to all voters; the test is not shown to be racially discriminatory on its face.
Quotations:
> "The ability to read and write likewise has some relation to standards designed to promote intelligent use of the ballot. Literacy and illiteracy are neutral on race, creed, color, and sex, as reports around the world show." — 360 U.S. at 51 (fn. 6 cites "World Illiteracy at Mid-Century, Unesco (1957)")

> "Literacy and intelligence are obviously not synonymous. Illiterate people may be intelligent voters." — at 52

> "It was said last century in Massachusetts that a literacy test was designed to insure an "independent and intelligent" exercise of the right of suffrage." — at 52

> "Of course a literacy test, fair on its face, may be employed to perpetuate that discrimination which the Fifteenth Amendment was designed to uproot. No such influence is charged here." — at 53

> "The legislative setting of that provision and the great discretion it vested in the registrar made clear that a literacy requirement was merely a device to make racial discrimination easy." — at 53 (on *Davis v. Schnell*)

Footnote 7 (pp. 52-53) lists "Nineteen States, including North Carolina," with "some sort of literacy requirement". The same footnote describes Georgia's alternative: a voter with good character who "can answer correctly 20 of 30 questions listed in the statute".
Scale: nation (U.S., 19 States). Bearing: problem 2 (supports: gives the 1959 official ground); problem 3 (the Court's world claim rests on one UNESCO report that I did not open); problem 5 (the Court itself separates literacy from intelligence).

**2. *Williams v. Mississippi*, 170 U.S. 213 (1898).** Key `williams1898williams`.
Verified: govinfo `USREPORTS-170-213.pdf`; "Argued and submitted March 18, 1898.—Decided April 25, 1898." URL:
https://www.govinfo.gov/content/pkg/USREPORTS-170/pdf/USREPORTS-170-213.pdf
Read status: **read in part** (syllabus; pp. 219-225).
Argues: Mississippi's 1890 suffrage and jury provisions do not discriminate on their face; a Black defendant's motion to quash an all-white grand jury fails.
Quotations:
> "do not, on their face, discriminate between the white and negro races, and do not amount to a denial of the equal protection of the law" — syllabus, 170 U.S. at 213-214 (the syllabus lists section 244, "making ability to read any section of the constitution, or to understand it when read, a necessary qualification to a legal voter", and section 264, "making it a necessary qualification for a grand or petit juror that he shall be able to read and write")

> "Within the field of permissible action under the limitations imposed by the Federal Constitution, the convention swept the field of expedients, to obstruct the exercise of suffrage by the negro race." — at 222, quoting *Ratcliff v. Beale*, 20 So. Rep. 865 (Mississippi Supreme Court)

> "Restrained by the Federal Constitution from discriminating against the negro race, the convention discriminates against its characteristics, and the offences to which its criminal members are prone." — at 222, same quotation

> "But nothing tangible can be deduced from this." — at 222 (the U.S. Supreme Court's reply)

> "it has not been shown that their actual administration was evil, only that evil was possible under them." — at 225

Scale: one State. Bearing: problem 1 (documents a framer-side admission of purpose, quoted by the Court that then declined to act on it); problem 2 (contemporaries on both sides). Also the one place in my sources where jury literacy is in a statute and litigated.

**3. *Guinn v. United States*, 238 U.S. 347 (1915).** Key `guinn1915guinn`.
Verified: govinfo `USREPORTS-238-347.pdf`; "Argued October 17, 1913.—Decided June 21, 1915." URL:
https://www.govinfo.gov/content/pkg/USREPORTS-238/pdf/USREPORTS-238-347.pdf
Read status: **read in part** (pp. 357, 366).
Argues: Oklahoma's grandfather clause violates the Fifteenth Amendment; the literacy test alone is not before the Court.
Quotations:
> "No person shall be registered as an elector of this State or be allowed to vote in any election herein, unless he be able to read and write any section of the constitution of the State of Oklahoma; but no person who was, on January 1, 1866, or at any time prior thereto, entitled to vote under any form of government, or who at that time resided in some foreign nation, and no lineal descendant of such person, shall be denied the right to register and vote because of his inability to so read and write sections of such constitution." — at 357 (the amendment as quoted)

> "No time need be spent on the question of the validity of the literacy test considered alone since as we have seen its establishment was but the exercise by the State of a lawful power vested in it not subject to our supervision, and indeed, its validity is admitted." — at 366

Scale: one State. Bearing: problem 1 (the exemption for white illiterates written into the text); how the test ended in part (the clause fell in 1915, the test stayed).

**4. *South Carolina v. Katzenbach*, 383 U.S. 301 (1966).** Key `katzenbach1966south`.
Verified: govinfo `USREPORTS-383-301.pdf`; "Argued January 17-18, 1966.—Decided March 7, 1966." (text from govinfo PDF, `us383_301`). URL:
https://www.govinfo.gov/content/pkg/USREPORTS-383/pdf/USREPORTS-383-301.pdf
Read status: **read in part** (pp. 310-314 and footnotes 9-13).
Argues: upholds the 1965 Voting Rights Act; narrates the history of the tests to show why case-by-case suits failed.
Quotations:
> "Meanwhile, beginning in 1890, the States of Alabama, Georgia, Louisiana, Mississippi, North Carolina, South Carolina, and Virginia enacted tests still in use which were specifically designed to prevent Negroes from voting." — at 310

> "These laws were based on the fact that as of 1890 in each of the named States, more than two-thirds of the adult Negroes were illiterate while less than one-quarter of the adult whites were unable to read or write." — at 311

> "At the same time, alternate tests were prescribed in all of the named States to assure that white illiterates would not be deprived of the franchise. These included grandfather clauses, property qualifications, "good character" tests, and the requirement that registrants "understand" or "interpret" certain matter." — at 311

> "White applicants for registration have often been excused altogether from the literacy and understanding tests or have been given easy versions, have received extensive help from voting officials, and have been registered despite serious errors in their answers. Negroes, on the other hand, have typically been required to pass difficult versions of all the tests, without any outside assistance and without the slightest error." — at 312

> "A white applicant in Louisiana satisfied the registrar of his ability to interpret the state constitution by writing, "FRDUM FOOF SPETGH."" — at 312 n.12

> "In Panola County, Mississippi, the registrar required Negroes to interpret the provision of the state constitution concerning "the rate of interest on the fund known as the 'Chickasaw School Fund.'"" — at 312 n.13 (n.13 adds that in Forrest County "the registrar rejected six Negroes with baccalaureate degrees")

> "Prior to the Civil War, most of the slave States made it a crime to teach Negroes how to read or write." — at 311 n.10

> "According to estimates by the Attorney General during hearings on the Act, registration of voting-age Negroes in Alabama rose only from 14.2% to 19.4% between 1958 and 1964; in Louisiana it barely inched ahead from 31.7% to 31.8% between 1956 and 1965; and in Mississippi it increased only from 4.4% to 6.4% between 1954 and 1964. In each instance, registration of voting-age whites ran roughly 50 percentage points or more ahead of Negro registration." — at 313

> Tillman, as the Court prints it: "[T]he only thing we can do as patriots and as statesmen is to take from [the 'ignorant blacks'] every ballot that we can under the laws of our national government." — at 310 n.9, citing Journal of the Constitutional Convention of the State of South Carolina 464, 469 (1895). Of the "understand and explain" exemption: "There is no particle of fraud or illegality in it. It is just simply showing partiality, perhaps, [laughter,] or discriminating." — same note. I did not open the 1895 Journal; this is a quotation at one remove.

Scale: seven States. Bearing: the best single official statement of design, administration and effect in the U.S. South (problem 1). The registration numbers are the Attorney General's estimates for years in which the tests were in force, not a before-and-after of the tests alone.

**5. *Gaston County v. United States*, 395 U.S. 285 (1969).** Key `gaston1969gaston`.
Verified: govinfo `USREPORTS-395-285.pdf`; "Argued April 23-24, 1969.—Decided June 2, 1969." URL:
https://www.govinfo.gov/content/pkg/USREPORTS-395/pdf/USREPORTS-395-285.pdf
Read status: **read in part** (pp. 288, 293-296).
Argues: a county that maintained "separate and inferior schools" for Black residents may not reinstate a literacy test under the 1965 Act.
Quotations:
> "Of those persons over 25 years old at the time of the 1960 census, the proportion of Negroes with no schooling whatever was twice that of whites in Gaston County" — at 294-295 (the proportion with four or fewer years of education "was slightly less than twice that of whites", at 295)

> "It is only reasonable to infer that among black children compelled to endure a segregated and inferior education, fewer will achieve any given degree of literacy than will their better-educated white contemporaries." — at 295

> "A registrar told a Negro leader not to bring illiterates to register. Some Negroes who attempted to register were, in fact, rejected because they could not pass the test, and others did not attempt to register, knowing that they could not meet the standard." — at 295

Scale: one county. Bearing: ties the test to the schooling the State supplied (problems 1 and 5). Footnote 11 (at 295) adds that "Appellant's registrars required only that a registrant copy one of three sentences of the Constitution."

**6. *Oregon v. Mitchell*, 400 U.S. 112 (1970).** Key `oregon1970oregon`.
Verified: govinfo `USREPORTS-400-112.pdf`; "Argued October 19, 1970—Decided December 21, 1970". Wording of quoted passages cross-checked against the Cornell LII text. URL:
https://www.govinfo.gov/content/pkg/USREPORTS-400/pdf/USREPORTS-400-112.pdf
Read status: **read in part** (syllabus; Black, J. at 117-118, 132-134; Douglas, J. at 145).
Argues: Congress could ban literacy tests nationwide for five years under the Fourteenth and Fifteenth Amendments (and not lower the voting age in state elections).
Quotations:
> "For reasons expressed in separate opinions, all of my Brethren join me in this judgment. Therefore the literacy-test provisions of the Act are upheld." — at 118 (Black, J.)

> "In enacting the literacy test ban of Title II Congress had before it a long history of the discriminatory use of literacy tests to disfranchise voters on account of their race." — at 132

> "There is substantial, if not overwhelming, evidence from which Congress could have concluded that it is a denial of equal protection to condition the political participation of children educated in a dual school system upon their educational achievement." — at 133

Scale: nation. Bearing: how the U.S. test ended in law (problem 1); the Court rests the ban on racial discrimination and unequal schooling, not on any finding that literacy is irrelevant to voting.

### Statutes and legislative messages

**7. Voting Rights Act of 1965, Pub. L. 89-110, 79 Stat. 437 (6 Aug 1965).** Key `usstat1965voting`.
Verified: govinfo, `govinfo.gov/content/pkg/STATUTE-79/pdf/STATUTE-79-Pg437.pdf` (10 pages). URL as given.
Read status: **read in part** (sections 1-5; pp. 437-439).
Quotations:
> "(c) The phrase "test or device" shall mean any requirement that a person as a prerequisite for voting or registration for voting (1) demonstrate the ability to read, write, understand, or interpret any matter, (2) demonstrate any educational achievement or his knowledge of any particular subject, (3) possess good moral character, or (4) prove his qualifications by the voucher of registered voters or members of any other class." — § 4(c), 79 Stat. at 438-439

> "(b) The provisions of subsection (a) shall apply in any State or in any political subdivision of a state which (1) the Attorney General determines maintained on November 1, 1964, any test or device, and with respect to which (2) the Director of the Census determines that less than 50 per centum of the persons of voting age residing therein were registered on November 1, 1964, or that less than 50 per centum of such persons voted in the presidential election of November 1964." — § 4(b), at 438

> "Congress hereby declares that to secure the rights under the fourteenth amendment of persons educated in American-flag schools in which the predominant classroom language was other than English, it is necessary to prohibit the States from conditioning the right to vote of such persons on ability to read, write, understand, or interpret any matter in the English language." — § 4(e)(1), at 439 (sixth-grade completion in such a school suffices, § 4(e)(2))

Scale: nation. Bearing: how the tests ended (suspension in covered jurisdictions, with a coverage formula that uses the test itself as the trigger).

**8. Voting Rights Act Amendments of 1970, Pub. L. 91-285, 84 Stat. 314 (22 June 1970).** Key `usstat1970voting`.
Verified: govinfo `govinfo.gov/link/statute/84/314?link-type=pdf` (6 pages).
Read status: **read in part** (pp. 314-316).
Quotation:
> "Prior to August 6, 1975, no citizen shall be denied, because of his failure to comply with any test or device, the right to vote in any Federal, State, or local election conducted in any State or political subdivision of a State as to which the provisions of section 4(a) of this Act are not in effect by reason of determinations made under section 4(b) of this Act." — § 201(a), 84 Stat. at 315
Also § 3 raises the suspension period in § 4(a) from "five years" to "ten years" (at 315).

**9. Voting Rights Act Amendments of 1975, Pub. L. 94-73, 89 Stat. 400 (6 Aug 1975).** Key `usstat1975voting`.
Verified: govinfo `STATUTE-89-Pg400.pdf` (7 pages).
Read status: **read in part** (pp. 400-403). I did not locate or read the operative section that makes the ban permanent; I rely on the title.
Quotations:
> "To amend the Voting Rights Act of 1965 to extend certain provisions for an additional seven years, to make permanent the ban against certain prerequisites to voting, and for other purposes." — title, at 400

> "The Congress finds that voting discrimination against citizens of language minorities is pervasive and national in scope. Such minority citizens are from environments in which the dominant language is other than English. In addition they have been denied equal educational opportunities by State and local governments, resulting in severe disabilities and continuing illiteracy in the English language." — § 4(f)(1), at 401

> "Among other factors, the denial of the right to vote of such minority group citizens is ordinarily directly related to the unequal educational opportunities afforded them, resulting in high illiteracy and low voting participation." — § 203(a), at 402-403

**10. Immigration Act of 1917 (39 Stat. 874, ch. 29, enacted 5 Feb 1917).** Key `usstat1917immigration`.
Verified: govinfo `govinfo.gov/link/statute/39/874?link-type=pdf` (25 pages); the chapter heading in the scan reads "February 5, 1917."
Read status: **read in part** (§ 3, 39 Stat. at 876-877).
Quotations:
> "All aliens over sixteen years of age, physically capable of reading, who can not read the English language, or some other language or dialect, including Hebrew or Yiddish" — § 3, at 877 (excluded)

> "That for the purpose of ascertaining whether aliens can read the immigrant inspectors shall be furnished with slips of uniform size, prepared under the direction of the Secretary of Labor, each containing not less than thirty nor more than forty words in ordinary use, printed in plainly legible type in some one of the various languages or dialects of immigrants. Each alien may designate the particular language or dialect in which he desires the examination to be made" — § 3, at 877

The Act exempts, among others, "all aliens who shall prove to the satisfaction of the proper immigration officer or to the Secretary of Labor that they are seeking admission to the United States to avoid religious persecution", and lets a citizen or admissible alien bring in a "father or grandfather over fifty-five years of age, his wife, his mother, his grandmother, or his unmarried or widowed daughter … whether such relative can read or not" (at 877).
Scale: nation. Bearing: statute text only. The Act's other effects (admissions refused) are **not found** in my sources.

**11. Woodrow Wilson, veto message on H.R. 10384, 29 January 1917.** Key `wilson1917message`.
Verified: American Presidency Project (UCSB) page; source line "House Documents, 64th Congress, 2nd Session". URL:
https://www.presidency.ucsb.edu/documents/message-the-house-representatives-returning-without-approval-act-regulate-the-immigration
Read status: **read in full** (one page).
Quotations:
> "I can not rid myself of the conviction that the literacy test constitutes a radical change in the policy of the Nation which is not justified in principle. It is not a test of character, of quality, or of personal fitness, but would operate in most cases merely as a penalty for lack of opportunity in the country from which the alien seeking admission came."

> "The opportunity to gain an education is in many cases one of the chief opportunities sought by the immigrant in coming to the United States, and our experience in the past has not been that the illiterate immigrant is as such an undesirable immigrant. Tests of quality and of purpose can not be objected to on principle, but tests of opportunity surely may be."

Scale: nation. Bearing: a contemporary naming the test a wrong of a stated kind (problem 2) and distinguishing literacy as opportunity from literacy as character (problem 5). Congress enacted the bill over this veto (statute dated 5 Feb 1917, entry 10); the override vote count is **not found** in a source I opened.

**12. Immigration Commission (Dillingham Commission), *Abstracts of Reports*, 2 vols (Washington: GPO, 1911).** Key `immcomm1911abstracts`.
Verified: archive.org scans `abstractsreport00benngoog` (vol. 1) and `abstractsreport01benngoog` (vol. 2), "Washington, Govt. Print. Off." Index entry: "Literacy test: Proposed by Commission as means of restriction, i, 47, 48; minority report, i, 49".
Read status: **read in part** (vol. 1 pp. 47-48; vol. 2 pp. 573-574).
Quotations:
> "8. The investigations of the Commission show an oversupply of unskilled labor in basic industries to an extent which indicates an oversupply of unskilled labor in the industries of the country as a whole, a condition which demands legislation restricting the further admission of such unskilled labor." — vol. 1, recommendation 8

> "A majority of the Commission favor the reading and writing test as the most feasible single method of restricting undesirable immigration." — vol. 1, p. 48

> "The educational test proposed is a selective test for which no logical argument can be based on the report." — vol. 1, p. 48, Views of the Minority (William S. Bennet). The scan prints "lo^cal"; I read it as "logical".

> Cleveland, vetoing the 1897 bill, preferred "to admit a hundred thousand immigrants who, though unable to read and write, seek among us only a home and opportunity to work, than to admit one of those unruly agitators who can not only read and write, but delights in arousing by inflammatory speech the illiterate and peacefully inclined to discontent." — vol. 2, pp. 573-574 (the Commission's paraphrase and quotation of the veto, 2 March 1897; the scan misprints "agitators" and "inflammatory" through OCR; I give the corrected words)

Scale: nation. Bearing: the official ground for the test was an oversupply of unskilled labour and assimilability, not civic competence (problem 2).

**13. 28 U.S.C. § 1865 (federal juror qualification).** Key `usc28sec1865`.
Verified: Cornell LII, https://www.law.cornell.edu/uscode/text/28/1865 ; history notes cite Pub. L. 90-274, 82 Stat. 58 (27 Mar 1968).
Read status: **read in full**.
Quotation:
> "is unable to read, write, and understand the English language with a degree of proficiency sufficient to fill out satisfactorily the juror qualification form" — § 1865(b)(2) (a person with this inability is not qualified for federal jury service; § 1865(b)(3) adds "is unable to speak the English language")

Bearing: shows that a literacy condition for jury service is still federal law, in the form in force after 1968. The statute does not say what the clause was for; the history notes I read do not either.

**14. Immigration Restriction Act 1901 (Cth), Act No. 17 of 1901.** Key `ira1901immigration`.
Verified: Museum of Australian Democracy, Documenting a Democracy, transcript PDF https://www.foundingdocs.gov.au/resources/transcripts/cth4ii_doc_1901a.pdf (header "No. 17 of 1901 … [Assented to 23rd December 1901]").
Read status: **read in part** (ss. 1-10 of the transcript; not the schedule).
Quotations:
> "(a) Any person who when asked to do so by an officer fails to write out at dictation and sign in the presence of the officer a passage of fifty words in length in an European language directed by the officer;" — s. 3(a). The transcript's marginal note reads "See Natal Act 1897, No. 1, s.3."

> "Any immigrant may at any time within one year after he has entered the Commonwealth be asked to comply with the requirements of paragraph (a) of section three, and shall if he fails to do so be deemed to be a prohibited immigrant offending against this Act." — s. 5(2)

> "Any prohibited immigrant within the meaning of paragraph (a) only of section three may if thought fit by an officer be allowed to enter the Commonwealth or to remain within the Commonwealth upon the following conditions:— (a) He shall on entering the Commonwealth or on failing to comply with the requirements of that paragraph deposit with an officer the sum of One hundred pounds." — s. 6

Scale: Commonwealth of Australia (federal), with explicit reference to Natal. Bearing: the statute never names race; the officer chooses the language and the passage.

**15. Museum of Australian Democracy, "Immigration Restriction Act 1901 (Cth)", Documenting a Democracy item page.** Key `foundingdocs0000immigration` (undated page; opened 2026-10-13).
URL: https://www.foundingdocs.gov.au/item-did-16.html
Read status: **read in full** (one page; it cites Jupp, *The Australian People* (1988) and Yarwood among its sources, which I did not open).
Quotations:
> "The mechanism restricting immigration could not be overtly based on race as this was opposed by Britain and frowned upon by Britain's ally, Japan. Instead, the basis was literacy, assessed by a Dictation Test."

> "It was initially proposed that the Test would be in English, but it was argued that this could discourage European migration and advantage Japanese people, and Americans of African descent. Instead, any 'European language' was specified. In 1905 this was changed to 'any prescribed language' to lessen offence to the Japanese."

> "The Dictation Test was administered 805 times in 1902–03 with 46 people passing and 554 times in 1904–09 with only six people successful. After 1909 no person passed the Dictation Test and people who failed were refused entry or deported."

> "The Act, frequently amended, remained in force until 1958."

Scale: nation. Bearing: the only administration counts I found for any entry test. The counts are a museum page's, from secondary sources; the original returns are not opened.

### Debates and proceedings (primary)

**16. Alabama Constitutional Convention, *Official Proceedings*, vol. 1 (1901).** Key `alabama1901official`.
Verified: archive.org item `alabama-constitutional-convention-proceedings-1901-v1` (metadata: "Official proceedings of the constitutional convention of the State of Alabama May 21st, 1901, to September 3rd, 1901. Volume one of four"). The address follows Knox's election on Wednesday, May 22, 1901.
Read status: **read in part** (printed pp. 7-10: Knox's address).
Quotations:
> "And what is it that we want to do? Why it is within the limits imposed by the Federal Constitution, to establish white supremacy in this State." — p. 8 (President John B. Knox)

> "But if we would have white supremacy, we must establish it by law—not by force or fraud." — p. 9, under the heading "WHITE SUPREMACY BY LAW"

Scale: one State. Bearing: the president of the convention states the purpose in the opening address (problem 1). A web-search snippet gave p. 9 for the first sentence; in the scan I read it is on printed p. 8.

**17. Virginia Constitutional Convention, *Report of the Proceedings and Debates*, vol. 2 (Richmond: Hermitage Press, 1906).** Key `virginia1906report`.
Verified: archive.org `reportofproceedi21virg` (Duke Law Library copy; metadata "Virginia. Constitutional Convention (1901-1902)", editor James H. Lindsay).
Read status: **read in part** (pp. 3074-3077: Carter Glass's speech, Friday, April 4, 1902).
Quotations:
> "This plan of popular suffrage will eliminate the darkey as a political factor in this State in less than five years" — p. 3076 (Mr. Glass)

> "the article of suffrage which the Convention will to-day adopt does not necessarily deprive a single white man of the ballot, but will inevitably cut from the existing electorate four-fifths of the negro voters. (Applause.) That was the purpose of this Convention; that will be the achievement." — p. 3076 (the scan's OCR reads "tne Convention"; I give "the")

> "Mr. Pedigo: Will it not be done by fraud and discrimination? Mr. Glass: By fraud, no; by discrimination, yes. But it will be discrimination within the letter of the law, and not in violation of the law. Discrimination! Why, that is precisely what we propose; that, exactly, is what this Convention was elected for—to discriminate to the very extremity of permissible action under the limitations of the Federal Constitution, with a view to the elimination of every negro voter who can be gotten rid of, legally, without materially impairing the numerical strength of the white electorate." — pp. 3076-3077

> "It has been attacked from one direction because it does not contain a permanent "understanding clause," and from another side because it does contain a temporary "understanding clause."" — p. 3076

Scale: one State. Bearing: a framer's prediction (four-fifths) is not a measurement; I did not find the count that followed in the sources I opened. Mr. Pedigo is a delegate who named the discrimination at the time (problem 2).

**18. Commonwealth of Australia, House of Representatives, Hansard, 7 August 1901 (Barton, second reading of the Immigration Restriction Bill).** Key `hansard1901barton`.
Verified: https://historichansard.net/hofreps/1901/19010807_reps_1_3/ . No page numbers in the web edition; I cite speaker and date.
Read status: **read in part** (three passages in Barton's speech).
Quotations:
> "It is because the Bills have been based on the educational test that objections have been avoided. The moment we begin to define - the moment we begin to say that every one of a certain nationality or colour shall be restricted, while other persons are not, then as between civilized powers, amongst whom must now be counted Japan, we are liable to trouble and objection" — Barton (the web edition prints "to. define" with a stray full stop; I give "to define")

> "we see no reason why we should, not convert this into an equal law, applying, so far as the power given to us is concerned, equally to all persons, without distinction of race, colour, or origin" — Barton

> "the fire of those who consider the provisions a piece of organized hypocrisy, and altogether too severe for a civilized power to adopt." — Barton, describing the objection from one side

> "The next difference is that the word " English " is substituted for the word " European " in the New South Wales Act. The reason for that is that if a man wants to come into an English-speaking country to pursue his avocation there, the language which the people of that country are concerned in his knowing, is the language which will enable them to- do business with- him." — Barton on the draft clause (the Act as passed says "an European language"; entries 14 and 15). Spacing and line-break hyphens as in the web edition.

> Barton read Joseph Chamberlain's dispatch on the Queensland Sugar Works Guarantee Bill into the record: "Disqualification by educational tests Such as are embodied in the immigration laws of various colonies, is not a measure to which the Government of Japan or any other Government can take exception in behalf of its subjects".

Bearing: the author of the bill says why a language test, not a racial one, was chosen. Other members, marked in the extract as Mr O'Malley (6 Sept 1901, https://historichansard.net/hofreps/1901/19010906_reps_1_4/) and Mr Manifold (same day), did not object on grounds of wrong done to the excluded. Mr O'Malley called "the proposed educational test … absolutely absurd" because it "will keep out a million Canadians if they want to come here" and "will not shut out the Japanese"; Mr Manifold wanted the Parliament to legislate "from the front", saying "A majority of the natives of the Indian Empire will soon be able to pass any test in the English language." Both read in part; both objected that the test would not exclude enough or was not candid, which is the opposite ground from Wilson's.

### Secondary and scholarly

**19. Lake, Marilyn, "From Mississippi to Melbourne via Natal: the invention of the literacy test as a technology of racial exclusion", chap. 13 in Curthoys and Lake (eds), *Connected Worlds: History in Transnational Perspective* (Canberra: ANU Press, 2006).** Key `lake2006mississippi`.
Verified: Crossref DOI 10.22459/cw.03.2006 for the volume (editors Curthoys and Lake, ANU Press, issued 2006-03); chapter title and author from the ANU Press web edition. URL: https://press.anu.edu.au/downloads/press/p97101/mobile/ch13.html
Read status: **read in part** (web sections "The Mississippi precedent", "A literacy test to restrict immigration to the United States", "Founded on the American Act", "The White Australia policy", "Conclusion"; the opening section and the endnotes not opened). Quotations below are Lake's quotation of other sources and I have not checked them against the originals.
Argues: the literacy test was invented as a way of excluding by race without naming race, and travelled from Mississippi (1890) through the Cape (1892) and Natal (1897) to Australia (1901); the American immigration bills of 1896 and later were its other branch.
Quotations:
> "Prevented by the 14th and 15th Amendments from disenfranchising Blacks on the grounds of race, the southern state of Mississippi led the way among self-styled white men's countries in deploying an education test – in this case a comprehension test – to achieve racial exclusion."

> "Other southern states followed suit: South Carolina in 1895, Louisiana in 1898, North Carolina in 1900, Alabama in 1901, Virginia in 1901, and Georgia in 1908."

> Gilbert Stephenson (1910), as Lake quotes him: "In one county in Mississippi, with a population of about 8,000 whites and 11,700 Negroes in 1900, there were only twenty-five or thirty qualified Negro voters in 1908, the rest being disqualified, it is said, on the educational test."

> "The great Republic of America has found it necessary to have recourse to that restriction and I may say generally that the Bill that I now have the honour to submit to this Assembly is founded on the American Act. But it goes one step further." — Natal Premier, second reading, March 1897, as Lake quotes the Natal debates

> "The final legislation actually specified that the application must be written in 'any European language', both to avoid discouraging other European immigrants and causing offence to Britain's European allies."

> "The Australian Immigration Restriction Act, following Natal and the United States, incorporated a literacy test, in this case, a dictation test, that was so framed as to give Customs Officers maximum flexibility in ensuring that all undesirable immigrants would fail."

> "Meeting with the colonial premiers at Queen Victoria's Jubilee, in London, in June 1897, Chamberlain impressed on them the importance of upholding the 'traditions of the empire' which made no 'distinction in favour of or against race or colour'."

> Japanese consul in Sydney, 3 May 1901, as Lake quotes his note: "The Japanese belong to an Empire whose standard of civilization is so much higher than that of Kanakas, Negroes, Pacific Islanders, Indians or other Eastern peoples, that to refer to them in the same terms cannot but be regarded in the light of a reproach, …".

Scale: transnational (U.S., Cape, Natal, Australia, with the Colonial Office as link). Bearing: the nearest I found to a world-scale account (problem 3). It is one author's argument, and several of its links (Bryce's advice to the Cape; the 1896 Lodge bill) are Lake's, not something I verified. The Natal Act itself I did not open.

**20. Aleixo, José Carlos Brandi, and Paulo Kramer, "Os analfabetos e o voto: da conquista da alistabilidade ao desafio da elegibilidade", *Senatus* 8(2), Oct. 2010, 68-79.** Key `aleixo2010analfabetos`.
Verified: UnB repository PDF (CC BY-NC-SA 3.0 Brazil licence page); no DOI found in Crossref. URL:
https://repositorio.unb.br/bitstream/10482/20670/1/ARTIGO_AnalfabetosVoto.pdf
Read status: **read in part** (pp. 68-72, introduction, history and the start of section 3). Two-column PDF; page ranges below are approximate for the 1879-1881 quotations. The authors argue for the eligibility of illiterates, so their framing is advocacy. The parliamentary speeches are quoted from the *Anais*, which I did not open.
Quotations (my translations in brackets are plain glosses, not quotations):
> "O inciso II do mesmo artigo rezava que, para ser incluído no alistamento, o cidadão deveria comprovar saber "ler e escrever"; logo a seguir, o parágrafo 1º esclarecia que essa comprovação seria "feita [...] pela letra e assinatura do cidadão", desde que ambas fossem reconhecidas "por tabelião"" — p. 69 (Lei Saraiva, Decreto 3.029 of 9 January 1881, art. 8) [the citizen proves reading and writing by handwriting and signature, notarised]

> "a revisão do alistamento realizada em 1887 revelou que os 200 mil eleitores alistados em todo o País representavam 1,5% da população. "É um dos menores eleitorados que se conhecem", conforme admitiu o próprio governo" — p. 69

> José Bonifácio o Moço, speech of 15 November 1880 as the article prints it (citing Bonifácio o Moço 1978, pp. 149-150): "A leitura e a escrita são meios de instruir-se, mas em si mesmos não aumentam o discernimento do homem, e muito menos dão bom senso a quem não o tem" — p. 70 [reading and writing are means of instruction, but do not in themselves increase a person's judgment]

> The same speech: "Como pena para forçar os descuidados a aprender o que não sabem, é desigual, injusta e contrária a seus fins" — p. 70 [as a penalty to force the careless to learn, it is unequal, unjust and defeats its own ends]

> Joaquim Nabuco: "Mais escandaloso do que manter o voto dos analfabetos, era julgar que esses mesmos votos dos analfabetos, que não podem escrever, seriam culpados pelas atas falsas" — p. 70

> "Logo em seguida à proclamação da República, em 15 de novembro de 1889, [...] um dos primeiros atos do governo provisório consistiu na proibição de que os cidadãos que não sabiam ler e escrever participassem nas eleições para o novo Poder Legislativo." — pp. 70-71

> Deputy Lauro Sodré, 13 January 1891: "Não posso dar o meu voto a este verdadeiro esbulho com que se tenta ferir todos os que não sabem ler nem escrever" — p. 71, citing the *Anais do Congresso Constituinte* [I cannot vote for this true despoiling of all who cannot read or write]

> "A Emenda Constitucional nº 25, de 15 de maio de 1985 – aprovada por 423 votos na Câmara dos Deputados e 61 no Senado Federal – e, em seguida, a Constituição Federal de 5 de outubro de 1988 repararam uma secular injustiça, garantindo aos analfabetos o direito de se alistarem como eleitores." — p. 68

> "Mas, apesar da conquista da alistabilidade, mantém-se, até hoje, a inelegibilidade dos analfabetos." — p. 68 [illiterates still cannot stand for office]

Scale: nation (Brazil). Bearing: problem 2 (named objectors in 1879-1891 who gave grounds); a documented exclusion that ran 1881-1985; office as well as vote.

**21. Nicolau, Jairo, "A participação eleitoral no Brasil", Oxford Centre for Brazilian Studies Working Paper CBS-26-2002 (Feb 2002).** Key `nicolau2002participacao`.
Verified: PDF title page; 51 pp. URL: https://www.brazil.ox.ac.uk/sites/default/files/lac/documents/media/nicolau26.pdf
Read status: **read in part** (pp. 10-11, 15, 21-22; abstract).
Quotations:
> "Mas o artigo 8º, que trata especificamente das revisões dos alistamentos futuros (à partir de 1882) introduziu como critério a exigência de se saber ler e escrever." — p. 10

> "aqueles alistados antes de 1881 poderiam continuar votando até 1889; os cadastrados a partir de 1882 precisavam demonstrar que sabiam, pelo menos escrever o próprio nome." — p. 10 [those enrolled before 1881 could keep voting until 1889; those enrolled from 1882 had to show they could at least write their name]

> "Quando se compara o número de votantes (1873) com o de eleitores (1882) observa-se um declínio acentuado, de 87%, caindo de 1,100 mil para 142 mil eleitores." — p. 21 [a fall of 87%, from 1.1 million voters (1873) to 142 thousand electors (1882)]

> "Apenas um quesito, a restrição de voto aos analfabetos, foi de fato, um obstáculo a incorporação eleitoral no país." — p. 15

> Turnout as a share of total population: "1% (1881), 1% (1885) e 0,9% (1886)." — p. 22

Scale: nation. Bearing: gives the one measured effect for a literacy gate that I could set beside a non-literacy change in the same law. Nicolau says the 1881 law tightened the income proof as well as adding the reading requirement (p. 21), so the 87% fall is not the effect of literacy alone, and the 1873 and 1882 counts are different kinds of list (votantes of the first stage against electors).

**22. Ragas, José, "Leer, escribir, votar. Literacidad y cultura política en el Perú (1810-1900)", *Histórica* 31(1), 2007, 107-134.** Key `ragas2007leer`.
Verified: Crossref DOI 10.18800/historica.200701.004 (title matches, issued 2007-03-12). URL: https://revistas.pucp.edu.pe/index.php/historica/article/download/233/227
Read status: **read in part** (abstract; pp. 108-110; pp. 131-133).
Quotations:
> "los iletrados participaron de manera activa en las elecciones hasta su exclusión legal en 1896, cuando se privilegió la lectoescritura como requisito para obtener la ciudadanía." — abstract, p. 107 [illiterates took part in elections until their legal exclusion in 1896]

> "la concesión del voto a los iletrados fue uno de los más relevantes, ya que significaba su reinserción como ciudadanos después de casi un siglo de exclusión por una norma promulgada en 1896 que solo concedía la ciudadanía a aquellos que pudiesen leer y escribir." — p. 108 (on the debates of the 1978-1979 constituent assembly) [the grant of the vote to illiterates was one of the assembly's most relevant debates, a re-entry after almost a century of exclusion]

> "Hacia fines del siglo XIX, los legisladores peruanos realizaron una serie de modificaciones al reglamento electoral con el propósito de restringir la amplia participación política que las Cortes de Cádiz habían implementado con la constitución de 1812. El criterio sobre el cual se basaron para regular el número de votantes fue la literacidad." — p. 133

> "Esta medida iba de la mano con el intento de mantener alejados de las urnas a los grupos rurales populares de la sierra y reorientar el control de las decisiones políticas hacia la costa." — p. 133

> "La ley electoral de 1833 manifestaba que los votantes de parroquia que no supieran leer y escribir podían nombrar a personas de confianza para que les leyeran los papeles adecuados y les firmaran las actas en su nombre." — p. 131 n.58

Scale: nation (Peru), with a view to the sierra against the coast. Bearing: complicates the picture (problem 1): before 1896 the written requirement existed but illiterates voted anyway through proxies and oral votes; the legal exclusion is later and has a stated regional-political purpose in the author's reading. The 1979 re-inclusion is stated in the article's opening; I did not open the 1979 text or the debates, and the article covers 1810-1900, not 1979.

**23. Senado de la República de Chile, "La eliminación del voto censitario en el país" (Leyes con historia).** Key `senadocl0000eliminacion`.
Verified: https://www.senado.cl/ciudadania/leyes-con-historia-0/la-eliminacion-del-voto-censitario-en-el-pais ; opened 2026-10-13; undated, no author.
Read status: **read in full** (a short web page).
Quotations:
> "Son ciudadanos activos con derecho de sufragio los chilenos que hubieren cumplido veintiún años de edad, que sepan leer y escribir y estén inscritos en los registros electorales" — quoted on the page from the reform of 1887

> "Vale destacar que recién en 1970, bajo el gobierno de Eduardo Frei Montalva, se eliminó como requisito saber leer y escribir para poder ejercer el derecho a sufragio."

Scale: nation (Chile). Bearing: thin. It gives a date for the end (1970) and does not name the law, the vote, or any effect. Two earlier-drafted leads (an 1874 date; Ley 17.284 as the instrument) are **not supported** by anything I opened.

**24. United States Commission on Civil Rights, *1961 Report, Book 1: Voting* (Washington: GPO, 1961).** Key `usccr1961voting`.
Verified: usccr.gov PDF (134 pages, scan) https://usccr.gov/files/historical/1961/61-001.pdf ; clean-OCR copy at https://www.crmvet.org/docs/ccr_61_voting.pdf (424 pages). I took the quoted text from the crmvet copy and confirmed that "at least six grades of formal" appears in the usccr.gov scan.
Read status: **read in part** (pp. 139-141: two dissents and recommendation 2). The body of the report on registration and the tests (about 130 pages) was not read.
Quotations:
> "Recommendation 2.—That Congress enact legislation providing that in all elections in which, under State law, a "literacy" test, an "understanding" or "interpretation" test, or an "educational" test is administered to determine the qualifications of electors, it shall be sufficient for qualification that the elector have completed at least six grades of formal education." — p. 141

> "The security and purity of the ballot can be destroyed by permitting illiterates to vote. And as the English language is still the official language of the United States, there is good justification for States requiring that voters have at least a rudimentary knowledge of this language." — p. 140 (dissent of Vice Chairman Storey, to recommendation 1)

Scale: nation. Bearing: shows a federal body in 1961 proposing a schooling floor instead of a ban, and a dissenting commissioner stating the case for the test (problem 2).

### Leads not opened

**25. Kousser, J. Morgan, *The Shaping of Southern Politics: Suffrage Restriction and the Establishment of the One-Party South, 1880-1910* (New Haven: Yale University Press, 1974).** Key `kousser1974shaping`. Verified by archive.org metadata (`shapingofsouther0000kous`; ISBN 0300016964). Read status: **not accessible** (lending copy, HTTP 401). I draw nothing from it.

**26. Keyssar, Alexander, *The Right to Vote: The Contested History of Democracy in the United States* (New York: Basic Books, 2000).** Key `keyssar2000right`. Verified by archive.org metadata (`righttovote00alex`; ISBN 0465029698). Read status: **not accessible** (lending copy, HTTP 401). I draw nothing from it. Lake (entry 19) credits the northern origin of literacy tests (Connecticut 1855, Massachusetts 1857) to Jacobsen, not Keyssar; the Massachusetts date is not in any primary I opened (Lassiter says only "last century in Massachusetts", entry 1).

## (c) Synthesis

I record five documented failures and two thin ones. Each states what was done, to whom, where and when, on what stated ground, who objected, and what ended it.

### F1. Reading-and-interpretation tests for the vote in the U.S. South, 1890-1965

**What was done.** Seven States "beginning in 1890" (Alabama, Georgia, Louisiana, Mississippi, North Carolina, South Carolina, Virginia) "enacted tests still in use which were specifically designed to prevent Negroes from voting" (*Katzenbach*, 383 U.S. at 310). Typically a voter had to read and perhaps interpret a section of the State constitution before a registrar. The *Williams* syllabus describes Mississippi's section 244 as "making ability to read any section of the constitution, or to understand it when read, a necessary qualification to a legal voter" (170 U.S. at 213); the section's own wording is in the opinion. The Lake chapter dates the other States: South Carolina 1895, Louisiana 1898, North Carolina 1900, Alabama and Virginia 1901, Georgia 1908 (secondary; Lake). The same constitutions put literacy into juror qualification: Mississippi's section 264 required a grand or petit juror "to read and write" (*Williams*, syllabus).

**To whom.** Black citizens, as the courts and the framers say. The Court found that in 1890 "more than two-thirds of the adult Negroes were illiterate while less than one-quarter of the adult whites were unable to read or write", and that "alternate tests were prescribed in all of the named States to assure that white illiterates would not be deprived of the franchise" (383 U.S. at 311). Oklahoma's text shows the device: the reading requirement did not apply to anyone entitled to vote on 1 January 1866 or any "lineal descendant" (*Guinn*, 238 U.S. at 357).

**On what stated ground.** Three layers.
- In the text of the laws: none about race. The *Williams* Court held the provisions "do not, on their face, discriminate".
- In the Massachusetts-type ground that the Court repeated in 1959: "independent and intelligent" suffrage (*Lassiter*, 360 U.S. at 52).
- In the framers' own mouths: Knox, Alabama, 22 May 1901: "to establish white supremacy in this State", "within the limits imposed by the Federal Constitution" (*Proceedings*, p. 8). Glass, Virginia, 4 April 1902: "to discriminate to the very extremity of permissible action under the limitations of the Federal Constitution" (*Debates*, pp. 3076-3077). The Mississippi Supreme Court, quoted by the U.S. Supreme Court in 1898: the convention "swept the field of expedients, to obstruct the exercise of suffrage by the negro race" (*Williams*, at 222). Tillman, as the Court prints him, wanted "to take from [the 'ignorant blacks'] every ballot that we can under the laws of our national government" (*Katzenbach*, at 310 n.9).

**How administered.** By registrar discretion. White applicants "have often been excused altogether … or have been given easy versions, have received extensive help"; Black applicants "have typically been required to pass difficult versions of all the tests, without any outside assistance and without the slightest error" (*Katzenbach*, at 312). Examples the Court records: a white applicant in Louisiana passed the interpretation test by writing "FRDUM FOOF SPETGH"; in Forrest County, Mississippi, "the registrar rejected six Negroes with baccalaureate degrees" (at 312 nn.12-13). In Gaston County, North Carolina, "A registrar told a Negro leader not to bring illiterates to register" (*Gaston*, at 294-295).

**Measured effect (source's own numbers only).**
- Attorney General's estimates quoted in *Katzenbach* (at 313): Black registration in Alabama "from 14.2% to 19.4% between 1958 and 1964"; Louisiana "from 31.7% to 31.8% between 1956 and 1965"; Mississippi "from 4.4% to 6.4% between 1954 and 1964"; "registration of voting-age whites ran roughly 50 percentage points or more ahead". These are levels long after the tests began and mix the tests with other devices.
- Stephenson (1910), quoted in Lake: a Mississippi county with 11,700 Black residents in 1900 had "only twenty-five or thirty qualified Negro voters in 1908" (second-hand; Stephenson not opened).
- The link between the test and the schooling the State supplied: in Gaston County in 1960 "the proportion of Negroes with no schooling whatever was twice that of whites" (*Gaston*, at 294-295).
- Virginia: Glass predicted the clause would "cut from the existing electorate four-fifths of the negro voters" (*Debates*, p. 3076). That is a prediction by the framer; **no measured result found**.
- Before-and-after figures for 1890-1910 from Kousser: **not found** (book not accessible).

**Who objected at the time.** Williams's counsel argued that "this officer can reject whomsoever he chooses, and register whomsoever he chooses" (*Williams*, at 221, in the Court's quotation of the argument). A Virginia delegate, Mr. Pedigo, asked "Will it not be done by fraud and discrimination?" (*Debates*, p. 3076). Delegates also objected from both sides on the shape of the Virginia clause (the "understanding clause" passage, same page). In 1961 the Civil Rights Commission proposed that six grades of schooling suffice wherever a test was used (p. 141), while Vice Chairman Storey dissented on the ground that "The security and purity of the ballot can be destroyed by permitting illiterates to vote" (p. 140).

**What ended it.** In pieces. *Guinn* (1915) struck the grandfather clause and left the test valid (238 U.S. at 366). *Lassiter* (1959) held a State may apply a literacy test to all voters unless it is used to discriminate (360 U.S. at 51-53). The 1965 Act defined "test or device" in § 4(c) and suspended tests where the formula applied (79 Stat. at 438-439). The 1970 Amendments barred tests nationwide until 1975 (84 Stat. at 315) and *Oregon v. Mitchell* (1970) upheld that ban, Black writing that "all of my Brethren join me in this judgment" (400 U.S. at 118). The 1975 Act's title says it makes "permanent the ban against certain prerequisites to voting" (89 Stat. at 400). *Gaston* (1969) tied the end to schools: a county with "separate and inferior schools" may not reinstate the test (395 U.S. at 293-296). The sources do not give a count of voters registered because the tests ended.

### F2. Literacy as a gate to admission: the American, Natal and Australian tests, 1896-1958

**What was done.**
- United States: bills with a reading test passed Congress in 1896-97 and were vetoed by Cleveland (2 March 1897; *Abstracts* vol. 2, pp. 573-574), and later by Taft and Wilson (Lake, secondary). The 1917 Act, passed over Wilson's veto of 29 January 1917, excludes "All aliens over sixteen years of age, physically capable of reading, who can not read the English language, or some other language or dialect, including Hebrew or Yiddish" (39 Stat. at 877). Inspectors use "slips" of "not less than thirty nor more than forty words", in a language the alien chooses (at 877).
- Natal (1897): a written application in a European language, per Lake's account of the Natal debates; the Natal Act **not opened**. The Australian transcript points back to it ("See Natal Act 1897, No. 1, s.3").
- Australia (1901): s. 3(a) of Act No. 17: a passage "of fifty words in length in an European language directed by the officer"; it could be demanded of an immigrant "at any time within one year" after entry (s. 5(2)); a failed candidate could be admitted on a deposit of "One hundred pounds" (s. 6).

**To whom.** The designers' targets differ by place. In the United States the Immigration Commission wanted fewer unskilled workers ("an oversupply of unskilled labor", vol. 1, rec. 8) and named the reading test "the most feasible single method of restricting undesirable immigration" (vol. 1, p. 48). In Natal the Premier said the people he meant to exclude were "perfectly well able to read and write in their own language" (Lake's quotation), so the Natal test required a European one. In Australia the Museum of Australian Democracy page says the aim was non-European migrants, and that the test "could not be overtly based on race as this was opposed by Britain and frowned upon by Britain's ally, Japan". The Japanese consul in Sydney protested in 1901 that Japan's "standard of civilization is so much higher than that of Kanakas, Negroes, Pacific Islanders, Indians or other Eastern peoples", which shows who read the test as aimed at them (Lake's quotation of the note).

**On what stated ground.** For the U.S. the 1917 statute states none. The Commission gave economic and assimilation grounds (rec. 8(c): exclude those who "would least readily be assimilated"). Lodge, in 1891, said the test "would in all probability shut out a large part of the undesirable portion of the present immigration" (Lake's quotation of Lodge; I did not open Lodge). Barton, introducing the Australian bill on 7 August 1901, said objections had "been avoided" because the Bills "have been based on the educational test", and that the test would apply "equally to all persons, without distinction of race, colour, or origin". The draft said "English" and the Act says "an European language" (entry 18 against entry 14).

**How administered.** The official chooses the passage and the language (Australia, s. 3(a)). The Museum page gives counts: "805 times in 1902-03 with 46 people passing and 554 times in 1904-09 with only six people successful. After 1909 no person passed." For the United States I found the statute's mechanism (slips, a chosen language, 39 Stat. at 877) and **no refusal counts**.

**Who objected at the time.** Cleveland (1897): safer "to admit a hundred thousand immigrants who, though unable to read and write, seek among us only a home and opportunity to work" than one agitator who can read (*Abstracts* vol. 2, pp. 573-574). Wilson (1917): the test "is not a test of character, of quality, or of personal fitness" but "a penalty for lack of opportunity"; "tests of opportunity surely may be" objected to. Bennet, minority of the Commission: "no logical argument can be based on the report". In Australia Barton himself described one side as saying the provisions were "a piece of organized hypocrisy" (7 Aug 1901). Lake reports that Higgins and others protested against what she calls "a cowardly subterfuge" and moved an amendment, which "almost passed", for a plain declaration against non-white immigration (secondary; the amendment is not in anything I opened). The Japanese consul asked in 1901 that the test be allowed in Japanese (Lake); his protest concerned the classing of Japanese with other non-Europeans, not the principle of the test. Members I read in the 6 September 1901 debate (O'Malley, Manifold) objected that the test would let in too many.

**What ended it.** Australia: "The Act, frequently amended, remained in force until 1958" (Museum page). United States: the 1917 clause's end is **not found** in my sources. Natal: **not found**.

### F3. Brazil, 1881-1985: illiterates barred from the electoral roll

**What was done.** The Lei Saraiva (Decreto 3.029 of 9 January 1881), art. 8, required that anyone added to the roll prove he could "ler e escrever" by handwriting and signature recognised by a notary (Aleixo and Kramer, p. 69; the decree itself not opened). Nicolau adds that those already enrolled could keep voting until 1889, while those enrolled from 1882 had to show they could at least write their name (p. 10). The Provisional Government's Decree 6 of 19 November 1889 limited the electors for the chambers to those who could read and write; the 1891 Constitution repeated the exclusion; later constitutions kept it (1934, 1937, 1946, 1967) (Aleixo and Kramer, pp. 70-72). The same article says illiterates still cannot stand for office (p. 68).

**To whom.** An "esmagadora maioria da população" in 1824, in the authors' words (p. 69). Nicolau's census figures: 84.2% of the total population illiterate in 1872 and 85.2% in 1890, and over half of adults still illiterate in 1940 (56%) (p. 11). He gives no breakdown by race or class in the passages I read.

**On what stated ground.** The 1881 law's main purpose was to end indirect elections, with the reading requirement added (Aleixo and Kramer, p. 69). I did not find a stated purpose of the reading clause in the debates I read; the objectors reply to claims the authors paraphrase ("corrupção", Bonifácio, p. 70).

**Measured effect.** Aleixo and Kramer: the 1887 roll of "200 mil eleitores" was "1,5% da população" (p. 69). Nicolau: from 1.1 million votantes (1873) to 142 thousand electors (1882), "um declínio acentuado, de 87%" (p. 21), with the caveat that the same law tightened income proof; turnout "1% (1881), 1% (1885) e 0,9% (1886)" of the total population (p. 22). No figure isolates the literacy clause.

**Who objected at the time.** Named, on stated grounds: José Bonifácio o Moço (1879-80: reading and writing "em si mesmos não aumentam o discernimento do homem"; it is "desigual, injusta e contrária a seus fins"; the State had not supplied the promised free schooling), Nabuco (the vices of elections came from "calígrafos" and the upper classes, not the illiterate), Saldanha Marinho (1880: an illiterate may head a family and make a will), and in 1891 Lauro Sodré (Aleixo and Kramer, pp. 70-71).

**What ended it.** Constitutional Amendment 25 of 15 May 1985 (423 votes in the Chamber, 61 in the Senate, p. 68) and the 1988 Constitution made enrolment optional for illiterates; eligibility stayed barred (p. 68). The text of EC 25 was **not opened**.

### F4. Peru, 1896-1979

**What was done.** "una norma promulgada en 1896" gave citizenship only to those who could read and write; the 1979 constituent assembly's grant of the vote to illiterates ended "casi un siglo de exclusión" (Ragas, p. 108). Ragas's footnote 1 (p. 108) points to the 1933 constitutional debates on the subject (Alarcón Quintana 1978); I did not open them or the text of the 1933 constitution.

**To whom.** In Ragas's reading the changes aimed at "mantener alejados de las urnas a los grupos rurales populares de la sierra y reorientar el control de las decisiones políticas hacia la costa" (p. 133) [keeping the rural popular groups of the sierra from the polls and moving political control to the coast].

**Stated ground and administration.** Ragas places the idea in eighteenth-century thought that only the autonomous could choose rulers (p. 108). Before 1896 the written requirement existed, but the 1833 electoral law let illiterate voters name trusted people to read and sign for them (p. 131 n.58) and ballots could be spoken or written by others (p. 131). The 1896 law's own text and debates: **not opened** (Chiaramonti 1995 is Ragas's cited source for them).

**Measured effect.** **Not found** in what I opened.

**Who objected / what ended it.** Ragas reports the position of Bartolomé Herrera (1849, "la soberanía de la inteligencia": only the instructed should take part in public decisions) and a reformist paper, *El Zurriago* (1848), that wished to bring illiterates into politics through public readings (p. 132). The 1979 assembly debate, which Ragas calls one of its most relevant, is not documented in the pages I read.

### F5. Chile

The Senate page says the 1887 reform required "que sepan leer y escribir" and that only in 1970, under Frei Montalva, was reading and writing removed as a requirement for the vote. Who designed it, what it was for, how it was applied and what it did: **not found**.

### F6. Jury service

The only documented cases are Mississippi's 1890 section 264 (in *Williams*, syllabus) and the current federal rule (28 U.S.C. § 1865(b)(2), added in its present form in 1968). The stated purpose, administration and effect of either: **not found**. Mississippi's juror clause sits in the same constitution and under the same convention as its voter clause, and the *Williams* plaintiff's complaint concerned an all-white grand jury.

### F7. Office and military rank

Office: Brazil's continuing bar on illiterate candidates (Aleixo and Kramer, p. 68). Military rank: **not found**; web-search snippets pointed to a World War II fourth-grade standard and Special Training Units, but the one official-looking source (DTIC ADA063747) returned HTTP 403 and I used none of the snippets.

### Scale (problem 3)

Every primary I opened is national, provincial or imperial: U.S. Reports, Statutes at Large, State conventions, the Australian Parliament, the Brazilian parliament as reported in 2010 and 2002 articles, the Peruvian article. The only transnational account is Lake's chapter (U.S.–Cape–Natal–Australia), and her links rest on sources I did not open. *Lassiter* names one world source (UNESCO, *World Illiteracy at Mid-Century*, 1957) for the claim that illiteracy is "neutral on race"; I did not open it. I found no comparative study of voting-literacy requirements across countries. The claim "as a global community" therefore has, for this facet, a lower bound of three documented national cases (U.S., Brazil, Peru) plus the colonial transfer between the U.S., Natal and Australia.

### Who named it a wrong at the time (problem 2)

From the table above: Bonifácio o Moço, Nabuco, Saldanha Marinho and Sodré in Brazil (1879-1891); Cleveland (1897) and Wilson (1917) in the United States, with Bennet in the Commission minority; a Japanese consul and Higgins in Australia (1901), on the Lake account (the House members I read objected only that the test excluded too little); a delegate in Virginia (1902); the Civil Rights Commission majority in 1961. In Peru, a press tendency in the 1840s (Ragas). I found no recorded objector to the Chilean test.

### Literacy as opportunity, not character (problem 5)

Four sources separate literacy from competence: Wilson ("tests of opportunity"), *Lassiter* ("Literacy and intelligence are obviously not synonymous"), Bonifácio ("em si mesmos não aumentam o discernimento") and *Gaston* (low literacy followed from "segregated and inferior" schools). These sources do not discuss what literacy delivered to the literate; they dispute whether lacking it should cost standing.

### Claims the sources contradict

1. **"Literacy tests are neutral."** *Lassiter* (1959): "Literacy and illiteracy are neutral on race, creed, color, and sex". *Katzenbach* (1966): the tests were "specifically designed to prevent Negroes from voting", on two-thirds against under one-quarter illiteracy, with white illiterates exempted by other clauses. The Court of 1959 nevertheless wrote that "a literacy test, fair on its face, may be employed to perpetuate that discrimination".
2. **The convention's admitted purpose and the court's ruling.** In *Williams* the Court quoted the Mississippi Supreme Court that the convention "swept the field of expedients, to obstruct the exercise of suffrage by the negro race" and answered "nothing tangible can be deduced from this".
3. **"English" or "European".** Barton in Parliament explained substituting "English" for "European". The Act as assented says "an European language". The Museum page says English was proposed and then dropped for "any 'European language'", and that the 1905 amendment changed it to "any prescribed language". Lake says the final Natal law also required "any European language".
4. **Equal on paper, targeted in intent (Australia).** Barton: "equally to all persons, without distinction of race, colour, or origin". The Museum page: "The mechanism … could not be overtly based on race". Lake: "so framed as to give Customs Officers maximum flexibility in ensuring that all undesirable immigrants would fail".
5. **Date and extent of Brazil's exclusion.** Nicolau: illiterates could vote "1822-1882"; the 1881 law's art. 8 applied to new enrolments, and those already enrolled kept the vote until 1889. Aleixo and Kramer present the 1881 law as "o efetivo início de um processo de marginalização" that the Republic completed. The 87% fall in the roll is also not a literacy effect alone (Nicolau).
6. **Peru: "illiterates were excluded before 1896."** Ragas: the written requirement stood in the regulations, but "entre 1810 y 1896 los analfabetos o iletrados participaron de manera efectiva en la toma de decisiones y en los procesos políticos del país" (p. 109), with proxies and oral votes (p. 131).
7. **Why America wanted the immigration test.** Lodge (1891, via Lake): "ignorance" as a danger to "free government". The Commission (1911): oversupply of unskilled labour and assimilability. Wilson and Cleveland: illiterate immigrants are not as such undesirable.
8. **Where the Knox sentence sits.** A search-result snippet put it on p. 9 of the Alabama journal. In the scan I read it is on printed p. 8 (heading "WHITE SUPREMACY BY LAW" on p. 9).
9. **The test's dependence on schooling vs. the Court's claim in 1959.** *Gaston* (1969) and Black's opinion in *Oregon v. Mitchell* (1970) rest the ban on unequal schooling ("separate but equal"), which *Lassiter* did not consider.

## (d) Gaps and unverified leads

Sources I could not open, and where a human with library access would find them.
- **Kousser (1974) and Keyssar (2000)**: lending copies only. Any library. Kousser would give before-and-after registration for 1880-1910 by State; Keyssar the Connecticut 1855 and Massachusetts 1857 origins. I used neither.
- **Natal Immigration Restriction Act No. 1 of 1897**: not found online in this run. Natal Government Gazette or the Colonial Office papers (CO 179, UK National Archives); a university law library holding *Statutes of Natal*. Bhana and Pachai (eds), *A Documentary History of Indian South Africans* (search result only).
- **Barton and the Australian Hansard in print**: the web edition has no page numbers. Commonwealth *Parliamentary Debates* vol. 4 (1901), 7 Aug 1901.
- **Cape Colony Franchise and Ballot Act 1892**: appears only in Lake. Cape Parliamentary papers.
- **Lodge, "The Restriction of Immigration", *North American Review* (Jan. 1891)** and the 1896 and 1917 *Congressional Record* debates: only Lake's quotation. JSTOR; the Record at govinfo or HathiTrust.
- **House vote to override Wilson's veto and U.S. refusal counts under the 1917 test**: not found. Annual Reports of the Commissioner General of Immigration, 1918 onward.
- **South Carolina 1895 Journal** (Tillman) and **Mississippi 1890 Journal**: only through *Katzenbach* n.9 and *Williams*. Duke or Library of Congress; HathiTrust.
- **Louisiana 1898 convention address (Kruttschnitt)**: I searched `officialjournal03convgoog` for "supremacy" and found nothing quotable; it may be in another volume or in a separate print.
- **Brazil: text of Decreto 3.029/1881, Decreto 6/1889, EC 25/1985, 1891 Constitution art. 70**: Planalto and Câmara pages would not open. Portal da Legislação, https://www.planalto.gov.br/ and https://www2.camara.leg.br/legin/. The *Anais do Parlamento Brasileiro* (1879-80) for Bonifácio, Nabuco, Saldanha Marinho.
- **Peru: the PUCP thesis on illiterate suffrage in the southern Andes (1933-1980)** and the text of art. 65 of the 1979 Constitution; Chiaramonti (1995) on the 1896 reform. repositorio.pucp.edu.pe (403 from curl; a browser may open it); Congreso del Perú archive.
- **Chile**: the law of 1970 that removed the literacy rule (the Senate page does not name it); the electoral-law history of 1874 and 1887. Biblioteca del Congreso Nacional, https://www.bcn.cl/leychile.
- **Italy** (1882 and 1912 franchise laws) and **colonial franchises in Africa beyond Natal and the Cape**: not searched. The brief names them as examples; I did not reach them.
- **Military and office literacy standards**: only search snippets (Army Special Training Units; DTIC ADA063747 returned HTTP 403). A browser may open DTIC; the official history is in *Army in World War II*.
- **UNESCO, *World Illiteracy at Mid-Century* (1957)**, cited by *Lassiter*: unesdoc.unesco.org. Not opened.
- **USCCR 1959 and 1963 reports and *Voting in Mississippi* (1965)**: cited in *Katzenbach* n.8-11; I read only 1961 pp. 139-141. The 1961 body pp. 1-138 has registration counts by county that a reader should check.
- **Oregon v. Mitchell separate opinions** (Harlan, Stewart, Brennan): I read only Black's and Douglas's parts.

Nothing in this file relies on a source I could not open, except where a line says "as X quotes".
