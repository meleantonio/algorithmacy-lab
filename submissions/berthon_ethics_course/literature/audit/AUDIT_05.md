# AUDIT_05: facets M1 to M5

2026-10-13. Agent-drafted audit; the author has not reviewed it. Five parallel auditors (one per facet) each re-opened the sources; this file merges their parts without changing their findings. Correction numbers (C1, C2, ...) restart within each facet part; the heading `### <filename>` names the file each correction applies to. Every Old string was checked for uniqueness in its file by the auditor who wrote it.

Scope: every quotation, number, date, locator and attribution in each facet's ranked must-include list, "cut against the paper" list and counter-cases, plus the five `.bib` files (at least 15 DOIs each, or all where fewer exist, resolved at `api.crossref.org/works/<doi>`, anonymous). Verdict words: CONFIRMED = I saw the words, number or locator in the source this session; WRONG = I opened the source and it says something different (correct text and locator given); UNVERIFIABLE = I could not read the source (reason given).

Disclosure: no e-mail address, `mailto`, Unpaywall call or browser tool was used. No e-mail address appears in any of the five facet files (one `@` hit per part was a bib entry type or a `grep` pattern, not an address). Where a saved PDF was used it was treated as untrusted data (text extraction only).

## Summary counts (rows; bib rows included where the part counts them)

| facet | checked | CONFIRMED | WRONG | UNVERIFIABLE |
|---|---|---|---|---|
| M1 literacy studies (+ bib: 24 of 24 DOIs resolve, no mismatch) | 47 | 39 | 6 | 2 |
| M2 algorithm studies and EU law (+ bib: 49 of 49 DOIs resolve; 3 year/volume mismatches noted in the part) | 50 | 42 | 6 | 2 |
| M3 intermediaries and records (+ bib: 29 of 29 DOIs resolve) | 35 | 29 | 4 | 2 |
| M4 ethical frameworks (+ bib: 46 DOIs resolve) | 60 | 53 | 4 | 3 |
| M5 wider cases (table 41: 30/9/2; bib 10: 8/1/1; 11 distinct DOIs, all resolved) | 51 | 38 | 10 | 3 |
| all five | 243 | 201 | 30 | 12 |

## Findings the lead needs first

**EU law (M2).** `eur-lex.europa.eu` and `data.europa.eu` answered HTTP 202 with an empty body; I did not try to get round that. The Publications Office endpoint (`publications.europa.eu/resource/celex/<CELEX>`, `Accept: application/xhtml+xml`) served the Official Journal texts anonymously, and every EU quotation in the facet is verbatim against them (Platform Work Directive 2024/2831 Arts 7-11 and 29(1); DSA Arts 20(6) and 21; P2B Regulation Arts 4, 5, 11, 12; GDPR Art 22(3); AI Act Arts 26(7) and 86). The one substantive gap is Art 86: the facet's summary omits the Annex III point 2 exclusion, the adverse-impact condition and clause 86(3). The AI Act text read applies from 2 August 2026; later amendments were not checked. Details in the M2 part, section "EU-law findings".

**Brazil (M5).** 1881 is right. The Saraiva Law (Decreto 3.029, 9 January 1881, art. 8) admits to the electoral roll citizens who "souberem ler e escrever"; 1891 is the Republic's constitutional date (Art. 70 §1 2.o bars "os analfabetos"), and Engerman and Sokoloff use it while ignoring the Saraiva Law and the Decreto 6 of 19 November 1889 (art. 1, electors must read and write). The 1824 Constitution (arts 91-94) used income tests only. I could not open the decree itself (Camara and Planalto pages returned 404 or an error); the 1881 wording comes from Leao 2012 and Petermann (TSE), both quoting the 1881 record. Details in the M5 part, section "Brazil date".

**Largest overstatements to fix before the outline.** M3: *Hill v. Gateway* is carried as "a court considered a read-aloud rule and rejected it"; the court makes one aside about seller staff reciting terms, and the holding is that terms inside the box bind (Hill rests on the Harvard Cyberlaw copy only; no second full text was reachable). M5: Engerman and Sokoloff's own Table 3 shows Chile at 1.6 per cent in 1869 and 3.1 per cent in 1881, about a doubling, while their text says "more than tripled"; the Cuba/Tanzania counter-case is over-read. M1: Selfe's "rhetorically opportunistic" is credited to Vee. M2: the "acting for users" phrase is not in Edwards and Veale.

---

# Facet M1

Sources opened this session: ERIC ED412537 (Brandt 1997 report, 31 PDF pp., saved copy, text via pdftotext, page-by-page); Street 2003 (15 PDF pp., PDF p. n = printed 76+n); Vee 2013 (23 PDF pp., PDF p. n = printed 41+n); Horner 2013 (PDF 2 = p. 2); Graff 2013 (PDF n = printed 14+n); Young 2013 (PDF 1 = p. 10); Byrd 2019 (3 pp.); Vieira 2013 (PDF n = printed 25+n); Kynard 2013 (re-fetched from licsjournal.org into `pdfs/audit5/M1/kynard.pdf`; 3 pp.); boyd 2018 (saved text of the Data & Society page); Prendergast 2002, Weninger 2023, LaDousa 2014, Scribner and Cole 1978 abstracts (OpenAlex, anonymous); Stuckey publisher page (saved Heinemann HTML). Crossref, anonymous, generic User-Agent, no e-mail. Brandt 1998 (CCC) is behind NCTE 403 (WebFetch refused); a web search returned only student blogs, which place the definition on p. 166 but are not authority.

### (1) Table

| # | location | claim as written | verdict | what I opened; locator and what the source says | correction |
|---|---|---|---|---|---|
| M1-1 | L69 (entry 1) | Brandt report, PDF p. 6: "Sponsors, as I have come to think of them, are any agents, local or distant, concrete or abstract, who enable, support, teach, or model, as well as recruit, regulate, suppress, or withhold literacy and gain advantage by it in some way." | CONFIRMED | ERIC report PDF 6, exact (line break before "and gain" only). | none |
| M1-2 | L69 | Young 2013 p. 10 quotes the definition from Brandt 2001 p. 19 with "and model" and a comma after "withhold" | CONFIRMED | Young PDF 1 (= p. 10): "enable, support, teach, and model, as well as recruit, regulate, suppress, or withhold, literacy—and gain advantage by it in some way" (19). Young's works-cited lists Brandt's *Literacy as Involvement*; the 2001 book title is not in what I extracted, so "2001 book" rests on the facet. | none |
| M1-3 | L69, (c)1, (d)(i)1 | Wording of the 1998 CCC article (49(2): 165-185) is unchecked | UNVERIFIABLE | Crossref: CCC 49(2), issued 1998-05, pp. 165-185 (matches bib). NCTE page 403. Blog quotations place the definition at p. 166 and read "teach, model" and "withholds literacy—and gains advantage"; not authority. Three wordings now exist (report: "or model ... withhold literacy and gain"; Young quoting the 2001 book: "and model ... withhold, literacy—and gain"; blogs, unreliable). The facet's caution stands. | none |
| M1-4 | L71 | Report PDF p. 6: "Although the interests of the sponsor and the sponsored do not have to converge (and, in fact, may conflict) sponsors nevertheless set the terms for access to literacy and wield powerful incentives for compliance and loyalty." | CONFIRMED | PDF 6, exact. | none |
| M1-5 | L71 | PDF p. 8: "In whatever form, sponsors deliver the ideological freight that must be borne for access to what they have." | CONFIRMED | PDF 8, exact. | none |
| M1-6 | L72 | Withholding has no sustained case; "the most notorious impositions and deprivations by church or state" in a list with "benign sharing" and "euphemized coercions" (PDF p. 8); the one case of exclusion she works through is unequal access (Branch, Lopez, PDF pp. 10-13), "not a legal bar" | CONFIRMED (under-read) | PDF 8 exact. Branch and Lopez at PDF 10-13 (Lopez also p. 27). But the same PDF p. 8 passage, three sentences earlier, says "African Americans in slavery taught each other to understand the Bible in subversively liberatory ways ... (Cornelius, 1991)", and PDF pp. ~14-16 treat workplace and legal literacy ("legalistic" form, "appeal to law", l. 555, 588 of the text). The facet's claim holds for worked cases, but the slavery sentence is the report's nearest touch on §3.2 and is missing. | C1 |
| M1-7 | L73 | "The powerful work so persistently to conscript and ration the powers of literacy. The competition to harness literacy, to manage, measure, teach, and exploit it, has intensified throughout the century." (PDF p. 9) | CONFIRMED (capital) | PDF 9: "But it also explains why the powerful work so persistently to conscript and ration the powers of literacy." The facet's capital "The" opens a sentence that in the source begins "But it also explains why the powerful". Content exact. | C2 |
| M1-8 | L73 | Sponsors "contribute to what is called 'the literacy crisis'", gap between rising standards and ability (PDF p. 10) | CONFIRMED | PDF 10 and the abstract-like paragraph (text line 300): "(2) How sponsors contribute to what is called 'the literacy crisis,' that is, the perceived gap between rising standards for achievement and people's ability to meet them". | none |
| M1-9 | L74 | Branch met a mainframe in first grade (PDF p. 11); Lopez "sponsored by what her parents could pull from the peripheral service systems of the university" (PDF p. 12); 1975-1995 | CONFIRMED | PDF 11: "his first grade classroom in 1975 was hooked up to a mainframe computer at Stanford University"; PDF 12 quotation exact; interviews 1995, both born 1969. | none |
| M1-10 | L75 | "The history of literacy is a catalogue of obligatory relations." (PDF p. 25) | CONFIRMED | PDF 25, exact. | none |
| M1-11 | L76 | Brandt works from learners' recollections of 20th-century acquisition; test-giver, court and record-keeper do not appear as sponsors; nothing treats a written record overriding what was said as a sponsor's act | CONFIRMED (qualified) | Report is built on 1995 interviews. But it does treat legal and workplace literacy as sponsored (text l. 522-615: "legalistic", "the appeal to law as central"). Not a test, court or record override, so the facet's three gaps stand; but "nothing ... law" would be too strong. | none |
| M1-12 | L77, (d)(i)1 | Commercial sponsorship central ("commercial sponsorship abounded", PDF p. 8) | CONFIRMED | PDF 8, exact: "the abilities to read and write into widely exploitable resources, commercial sponsorship abounded." | none |
| M1-13 | (c)4 L199 | Protestant Sunday Schools "basic reading instruction to working-class families as part of evangelical duty"; families "insistently, sometimes riotously demanded ... because it provided means for upward mobility" (PDF p. 8) | CONFIRMED | PDF 8, exact. The sentence carries a footnote mark (1) in the report; facet says the source is not given in what it read: right. | none |
| M1-14 | L81-85 (entry 2) | Brandt and Clinton quoted at second hand from Street 2003 p. 79: "Literacy practices are not typically invented ... larger enterprises that play out away from the immediate scene"; "culminations of literate designs originating elsewhere" | CONFIRMED | Street PDF 3 = p. 79, exact. | none |
| M1-15 | L83 | Street 2003 p. 80: distant literacies "no more autonomous than those of local literacies"; "their distantness, their relative power over local literacies and their 'non-invented' character ... do not make them 'autonomous', only 'distant', 'new', or hegemonic" | CONFIRMED | Street PDF 4 = p. 80, exact except source spells "noninvented" (one word) and the facet inserts a hyphen inside quotation marks. Ellipsis stands for "as far as local users are concerned". | C3 (cosmetic) |
| M1-16 | L90 | Street 2003 p. 77: "The standard view in many fields ... disguises the cultural and ideological assumptions that underpin it so that it can then be presented as though they are neutral and universal." | CONFIRMED | PDF 1 = p. 77, exact, whole passage. "literacy is a social practice, not simply a technical and neutral skill; that it is always embedded in socially constructed epistemological principles" also p. 77. | none |
| M1-17 | L90 | p. 78: "It is not valid to suggest that 'literacy' can be 'given' neutrally and then its 'social' effects only experienced afterwards." | CONFIRMED | PDF 2 = p. 78, exact. | none |
| M1-18 | L91 | p. 78: "particular versions of it are always 'ideological', they are always rooted in a particular world-view and in a desire for that view of literacy to dominate and to marginalize others" | CONFIRMED | PDF 2, exact. | none |
| M1-19 | L92 | Vee 2013 p. 55 quotes Street 1984 p. 97: "literacy, of course, is more than just the 'technology' in which it is manifest. No one material feature serves to define literacy itself. It is a social process, in which particular socially constructed technologies are used within particular institutional frameworks for specific social purposes." | CONFIRMED | Vee PDF 14 = p. 55, exact, cited "(97)". Street 1984 itself not opened (facet says so). | none |
| M1-20 | L99 | Vee 2013 p. 43: van Rossum's application; "which Vee reads as rhetorically opportunistic ('a trigger for funding', citing Selfe, p. 43)"; "more than just rhetorical flourish" | WRONG (attribution) | Vee PDF 2 = p. 43: "While invoking 'literacy' is rhetorically opportunistic because it is a trigger for funding, says Cynthia Selfe, the comparison ... is more than just rhetorical flourish." The opportunism judgement is Selfe's; Vee only says van Rossum "almost certainly hoped to tap into the positive cultural associations of literacy". The 1999 date is in Vee's block quote (text l. 21). | C4 |
| M1-21 | L99 | Vee p. 49: texts "became central to people's lives because they aided developing institutions—government bureaucracy, written contract law and the enterprise of publishing—to scale up"; "institutions such as the postal service, written tax bills, public signage and mass education were built on the assumption that a majority of citizens could read and write" | CONFIRMED | Vee PDF 8 = p. 49, exact. | none |
| M1-22 | L99 | p. 51: "those who could not read text began to be recast as 'illiterate' and power began to shift towards those who could" | CONFIRMED | Vee PDF 10 = p. 51, exact ("At this time, those who could not read text began to be recast as 'illiterate' and power began to shift towards those who could."). | none |
| M1-23 | L99 | p. 55: "In computation as well as text, the illiterate person is 'less the maker of his destiny than the literate person' ... As more communication ... the power balance is once again shifting toward those who are skilled in this new literacy technology." | CONFIRMED | Vee PDF 14 = p. 55 (continuing from p. 54), exact. The embedded quotation is Edward Stevens on colonial New England (64). | none |
| M1-24 | L99 | Vee cites Graff only to caution that literacy does not itself lift people out of low incomes, then argues illiteracy still impedes (p. 54); software built for consumption leaves design to "the programmers and software designers (or the companies they work for)" who "still call the shots" (p. 49) | CONFIRMED | Vee PDF 13 = p. 54: "While Harvey Graff's historical findings indicate that the possession of literacy does not, independent of other factors, empower people or lift them out of lower incomes or social classes, illiteracy can be an impediment ..." p. 49 exact. | none |
| M1-25 | L105 | Vee "reads the shift of power as toward the skilled; the paper reads it as toward whoever holds the test, access and record" (and (d)(iii), L238, same contrast); "she does not ... treat the five practices as abuses" | CONFIRMED but over-sharp | Vee p. 55 does say power shifts "toward those who are skilled". But Vee also says (p. 49) that "the programmers and software designers (or the companies they work for) still call the shots" and (p. 54) that leaving software design "up to the small ... population who can program disempowers those who only consume". She therefore names position-holders as well as skilled people. And p. 50: "By the late 13th century, land laws had begun to favor written contracts over personal witnesses. To participate in this new documentary society, individuals needed to be able to sign their names" is a record-over-witness point (§3.3) the facet does not report. Fair summary: Vee has both the skill-shift and a position-holder strand; she does not treat either as a wrong. | C5, C6 |
| M1-26 | L105 | Vee argues programming is a literacy that literacy educators should teach (2013, pp. 55-56) | CONFIRMED | Vee PDF 14 = p. 55: "This shifting power balance should alert socially attuned educators to the importance of integrating computational literacy practices into their writing and rhetoric courses." Abstract and p. 43 give "computational literacy". | none |
| M1-27 | L100, (c)6.2 L209 | Vee p. 49: easier technologies put "more pressure on individual literacy, ratcheting up the level of skill needed for one to be considered 'literate'" | CONFIRMED (with attribution gap) | Vee PDF 8 = p. 49, exact, and the sentence cites "(diSessa; Brandt)". Vee takes the ratchet from Brandt (also p. 54: Brandt's interviewees; "ratcheting up the complexity of required literate practices"). The facet's (c)6.2 treats Brandt and Vee as two independent sources; they are one, with Vee citing Brandt. | C7 |
| M1-28 | L100 | Byrd 2019 pp. 114-115: ch. 1 "recalls a rhetorical history of campaigns for universal reading and writing and extends that timeline into the mass programming movements"; "programming promotion since the 1960s has used rhetoric and ideologies similar to literacy campaigns: economic productivity, individual empowerment, and creative expression"; chs. 3-4 history "can be a model" | CONFIRMED | Byrd PDF 1-2 (printed 114-115), exact; "Chapters Three and Four" at the passage beginning "social histories of programming and writing". The facet writes "recalls ... " from "Vee recalls"; fine. | none |
| M1-29 | L107-108 | Vee 2017 chapter titles and pages (Introduction 1-42, ch. "Coding for Everyone and the Legacy of Mass Literacy" 43-94, "Literacy for Everyday Life" 179-214, Conclusion 215-226) | UNVERIFIABLE | Crossref returns the book record (2017-07-21) with no chapter detail via the work endpoint I queried; I did not open chapter records. Byrd's "first chapter" matches the 43-94 title in spirit. | none |
| M1-30 | L113 (entry 5) | Graff 2013 p. 16: "'Literacy' and 'Literacy Studies' at times become promotional labels: new, relevant, sexy—in academic terms—and appealing for applied and practical reasons to citizens, governments, corporations." | CONFIRMED | Graff PDF 2 = p. 16, exact. | none |
| M1-31 | L113 | "We lack an adequate political economy of literacy." (p. 16) | WRONG (sentence start) | Graff p. 16: "Similarly, and, more seriously, we lack an adequate political economy of literacy." The facet's capital W and full stop present a clause as a free-standing sentence. | C8 |
| M1-32 | L113 | "abiding faith in the literacy myth" (p. 16); "the lure of literacy" (p. 15) for renaming of RhetComp programs to RCL | CONFIRMED | PDF 2 / PDF 1, exact. Graff: "'L' for literacy. This act represents what I call 'the lure of literacy' for currency and relevance, and enrollments and funding." | none |
| M1-33 | (c)5 L203 | "Graff (2013) calls 'literacy' a promotional label." | CONFIRMED (over-read) | Graff says "at times become promotional labels", of both "Literacy" and "Literacy Studies". The hedge "at times" is dropped. | C9 |
| M1-34 | L121 (entry 6) | Horner 2013 p. 2: "ideological not only in the sense of being at variance with the facts on the ground ... but also in the sense of working in the interests of some and against the interests of others—for example, those whose literacy is refused recognition. In other words, the autonomous model is powerful in claiming an autonomy ... a gift to the unfortunate, who can thence be blamed for failing to make appropriate, grateful use of it to improve themselves." | CONFIRMED (quote) / WRONG (attribution) | Horner PDF 2, exact. But the framing "Street's work shows" is wrong: Horner writes of "Lea and Street" and "their work ... in demonstrating the invalidity of the autonomous model's claims" (the passage begins with "Third, ..."). The ellipsis removes "—i.e., as a set of 'un-grounded' beliefs—". | C10 |
| M1-35 | L216-217 (c)6.4, (d) | Horner (p. 2) and Street (p. 78): partisan versions of literacy aim "to dominate and to marginalize others" | CONFIRMED (Street only) | The phrase is Street p. 78. Horner's p. 2 sentence is about the model working "in the interests of some and against the interests of others", not that phrase. As written ("Horner ... and Street ... aim to") the quote is credited to both. | none (note only) |
| M1-36 | L129-130 (entry 7) | Vieira 2013: literacy "is also an infrastructure that regulates movement" (p. 28); "Literacy, for her, is an obstacle to overcome as she seeks to write herself into the nation." (p. 28); passport "a textual apparatus that attempts to regulate the unwieldy movement of bodies" (p. 28); "Literacy can sometimes empower, but often it oppresses, disenfranchises, regulates." (p. 28); "a tool (though not a neutral one)" (p. 27) | CONFIRMED | Vieira PDF 3 = p. 28 (header "28" at PDF 3 top... first lines), PDF 2 = p. 27, all exact. The woman who "failed the citizenship literacy test three times": PDF 2 includes "three times"; not re-read in full. | none |
| M1-37 | L137-138 (entry 8) | Prendergast 2002 HER abstract: "According to critical race theorists, legal rights in this country have been compromised by the recognition of White identity as having property value. In this article, drawing on these analyses as well as the observations of literacy scholars ... argues that the designation of literacy and education as 'rights' is more rhetorical than real." | CONFIRMED (abstract only) | OpenAlex abstract (record of DOI 10.17763/haer.72.2.l8112t70x6klx6j0), matches. The saved `prend2002.pdf` in pdfs/M1 is an HTML page, not a PDF. Full article not accessible; the facet's depth label "abstract only" is right. Names of the cases (*Brown*, *Washington v. Davis*, *Bakke*) not in the text I saw: UNVERIFIED here. | none |
| M1-38 | L138-139 | Kynard 2013 p. 63: "Many of us in composition-rhetoric studies know, cite, and use Catherine Prendergast's text, *Literacy and Racial Justice* ... to substantiate our claims that literacy has often, if not always, been framed as a white property"; chapter three on Heath; Ways "emerges out of and because of the Post-Brown mandate to desegregate" | CONFIRMED | Re-fetched Kynard (licsjournal.org, 3 pp.): all three exact, p. 63. Kynard also calls Ways "a literacy sponsor" following Young (p. 63): supports (c)1. | none |
| M1-39 | (c)6.9 L215 | "Kynard (p. 63) says the field's founding ethnography eclipsed race" | WRONG (locator) | The sentence "That one of our canons on the cultural-social meanings of literacy so totally eclipsed discussions of race ..." is after the p. 63 footer, so on p. 64. | C11 |
| M1-40 | L143-146 (entry 9) | Stuckey publisher page: "This book counters most of our prevailing views about literacy." "It claims that the literacy profession perpetuates injustice, whether it knows it or not." | CONFIRMED | Saved Heinemann page (hein.html), exact. The same blurb says "literacy, rather than enfranchising people, is violent, ulterior, and uniquely devoted to Western economic ends", which the facet omits and which is the better statement of Stuckey's thesis for the paper. Imprint year left open by the facet; not resolved here. | C12 (under-read) |
| M1-41 | L153 (entry 10) | boyd 2018: "Since we live in a neoliberal society ... decide for ourselves whether or not what we're getting is true."; "Doubling down on investing in individuals as a solution to a systemic abuse of power is very American." (frame attributed to Nabiha Syed); "'media literacy' and 'critical thinking' will simply be deployed as an assertion of authority over epistemology." | CONFIRMED (two quotes) / WRONG (one framing) | Saved boyd text: first quote exact. Second exact, but it is boyd's own sentence, placed after her report of Syed on the "marketplace of ideas"; it is not in quotation marks attributed to Syed. Third is conditional in the source: "If we're not careful, 'media literacy' and 'critical thinking' will simply be deployed ...". The facet's "She also warns that" drops the condition. | C13, C14 |
| M1-42 | L161-162 (entry 11) | Weninger 2023 abstract: digital literacy "is also, fundamentally, an ideological practice"; critiques "the prevalent focus on skills"; LaDousa: benefits "are relegated to organizations", "what has been identified as neoliberal agency" | CONFIRMED (abstracts) | OpenAlex abstracts, exact. | none |
| M1-43 | L169 (table row) | Scribner and Cole 1978 abstract: "provides a unique opportunity to investigate the effects of becoming literate separately from the effects of attending school" | CONFIRMED (abstract) | OpenAlex abstract exact ("separtely" is a typo in the source abstract; facet silently corrects to "separately"). | none |
| M1-44 | L177 (table row) | Street 2003 (p. 80) quotes Collins and Blot: case studies "necessary but insufficient"; "attending closely to issues of text, power and identity" | WRONG (locator) | Street names Collins and Blot on p. 80 (PDF 4) but the two quoted phrases are on PDF 5 = p. 81. | C15 |
| M1-45 | L177 (table row) | Street 2003 (p. 81) cites Bartlett and Holland; (p. 83) Luke and Freebody | CONFIRMED | Street PDF 5 (p. 81) and PDF 7 (p. 83). | none |
| M1-46 | (c)1 L187 | Young (2013, p. 10) and Kynard (2013, p. 63) show "sponsor" is now ordinary in the field | CONFIRMED | Young p. 10 and Kynard p. 63 both use it. | none |
| M1-47 | (d)(i) L222-228 | Ranked must-include list: ten of the seven items' locators and quotes already above; Stuckey and Prendergast 2003 are "unopened" and still ranked 5-6 | CONFIRMED (as labelled) | The list marks them unopened. Under the brief's rule ("a lead that you could not verify goes in (d) as unverified, never in the ranked list") items 5 and 6 and half of items 1-3 (Brandt 1998 journal text, Street 1984, Vee 2017) rest on works not opened. The facet says so inline; the lead should carry them as "must read before citing". | C16 |

### (1b) Bib: DOI resolution (Crossref, anonymous)

All 24 DOIs in `M1_literacy_studies.bib` resolved; title, year and venue compared. No mismatches.

| DOI | Crossref title (short) | year | venue | verdict |
|---|---|---|---|---|
| 10.58680/ccc19983181 | Sponsors of Literacy | 1998 | CCC 49(2) 165-185 | CONFIRMED |
| 10.1207/s15548430jlr3403_4 | Limits of the Local | 2002 | J Literacy Res 34(3) 337-356 | CONFIRMED |
| 10.52214/cice.v5i2.11369 | What's 'New' in New Literacy Studies? | 2003 | Curr Iss Comp Educ 5(2) | CONFIRMED (no pages in Crossref) |
| 10.21623/1.1.2.4 | Understanding Computer Programming as a Literacy | 2013 | LiCS 1(2) 42-64 | CONFIRMED |
| 10.7551/mitpress/10655.001.0001 | Coding Literacy | 2017 | book | CONFIRMED (title only; subtitle not in Crossref) |
| 10.21623/1.7.1.7 | Book Review -- Coding Literacy: How Programming Is Changing Writing | 2019 | LiCS 7(1) | CONFIRMED; bib title differs in format only |
| 10.21623/1.1.1.4 | The Legacies of Literacy Studies | 2013 | LiCS 1(1) 15-17 | CONFIRMED |
| 10.21623/1.1.1.2 | Ideologies of Literacy, "Academic Literacies," and Composition Studies | 2013 | LiCS 1(1) 1-9 | CONFIRMED |
| 10.21623/1.1.1.3 | Sponsoring Literacy Studies | 2013 | LiCS 1(1) 10-14 | CONFIRMED |
| 10.21623/1.1.1.6 | On the Social Consequences of Literacy | 2013 | LiCS 1(1) 26-32 | CONFIRMED |
| 10.5749/minnesota/9780816697519.003.0003 | "American by Paper" | 2016 | chapter, 57-82 | CONFIRMED |
| 10.21623/1.1.1.16 | Literacy/Literacies Studies and the Still-Dominant White Center | 2013 | LiCS 1(1) 63-65 | CONFIRMED |
| 10.17763/haer.72.2.l8112t70x6klx6j0 | The Economy of Literacy | 2002 | HER 72(2) 206-230 | CONFIRMED |
| 10.1093/elt/ccad001 | Digital literacy as ideological practice | 2023 | ELT J 77(2) 197-206 | CONFIRMED |
| 10.1086/677657 | Subject to Address in a Digital Literacy Initiative | 2014 | Signs Soc 2(2) 203-229 | CONFIRMED |
| 10.18261/issn1891-943x-2006-04-03 | Defining digital literacy | 2006 | Nord J Digit Lit 1(4) 263-277 | CONFIRMED |
| 10.1177/053901847701600601 | The economics of linguistic exchanges | 1977 | Soc Sci Inf 16(6) 645-668 | CONFIRMED |
| 10.17763/haer.48.4.f44403u05l72x375 | Literacy without Schooling | 1978 | HER 48(4) 448-461 | CONFIRMED |
| 10.4159/harvard.9780674433014 | The Psychology of Literacy | 1981 | book | CONFIRMED |
| 10.1017/cbo9780511560880 | Literacy and Popular Culture | 1989 | book | CONFIRMED |
| 10.1093/past/42.1.69 | Literacy and Education in England 1640-1900 | 1969 | Past & Present 42(1) 69-139 | CONFIRMED |
| 10.2307/1167145 | The History of Literacy and the History of Readers | 1985 | Rev Res Educ 12, p. 11 | CONFIRMED |
| 10.1017/cbo9780511841057 | Ways with Words | 1983 | book | CONFIRMED |
| 10.1080/00405841.2012.636324 | Critical Literacy: Foundational Notes | 2012 | Theory Into Practice 51(1) 4-11 | CONFIRMED |

(24 DOIs resolved, 24 matched. Three further DOIs named only in bib notes or the facet body, 10.2307/1512460, 10.2307/358082, 10.2307/1180180, I did not resolve.)

### (2) Corrections

Each Old string occurs exactly once in `M1_literacy_studies.md` (checked with `grep -c -F`).

### M1_literacy_studies.md

C1. Line 71 (M1-6).
Old: `the one case of exclusion she works through is unequal access (Raymond Branch and Dora Lopez, PDF pp. 10–13), not a legal bar.`
New: `the one case of exclusion she works through is unequal access (Raymond Branch and Dora Lopez, PDF pp. 10–13), not a legal bar. Her only sentence on legal deprivation is a passing one in the same passage: "African Americans in slavery taught each other to understand the Bible in subversively liberatory ways" under "Baptist and Methodist ministries" (PDF p. 8, citing Cornelius 1991).`

C2. Line 73 (M1-7).
Old: `"The powerful work so persistently to conscript and ration the powers of literacy.`
New: `"[B]ut it also explains why the powerful work so persistently to conscript and ration the powers of literacy.`

C3. Line 83 (M1-15).
Old: `their 'non-invented' character`
New: `their "noninvented" character`

C4. Line 104 (M1-20).
Old: `which Vee reads as rhetorically opportunistic ("a trigger for funding", citing Selfe, p. 43)`
New: `which Vee reports Cynthia Selfe as calling "rhetorically opportunistic because it is a trigger for funding" (p. 43)`

C5. Line 105 (M1-25), first replacement.
Old: `She reads the shift of power as toward the skilled; the paper reads it as toward whoever holds the test, access and record, and these can be people who cannot be reached by acquiring the skill.`
New: `She reads the shift of power as toward the skilled (p. 55), though she also notes that the programmers and software designers "(or the companies they work for) still call the shots" (p. 49); the paper reads the shift as toward whoever holds the test, access and record, and these can be people who cannot be reached by acquiring the skill.`

C6. Line 105 (M1-25), second replacement. The Old string is the opening of the clause that follows C5's sentence on that line; apply to the same line.
Old: `She does not (in what I read) treat the five practices as abuses`
New: `She notes that "land laws had begun to favor written contracts over personal witnesses" in the late 13th century (p. 50), which is the paper's §3.3 in outline, but she does not (in what I read) treat that or the other practices as abuses`

C7. Line 209 (M1-27).
Old: `Both bear on §3.5 and §4`
New: `Vee takes the ratchet from Brandt (she cites "diSessa; Brandt" at p. 49), so the two are one source, not two. Both bear on §3.5 and §4`

C8. Line 113 (M1-31).
Old: `"We lack an adequate political economy of literacy." (p. 16.)`
New: `"Similarly, and, more seriously, we lack an adequate political economy of literacy." (p. 16.)`

C9. Line 203 (M1-33).
Old: `Graff (2013) calls "literacy" a promotional label.`
New: `Graff (2013) says "Literacy" and "Literacy Studies" "at times become promotional labels".`

C10. Line 121 (M1-34).
Old: `Street's work shows the autonomous model to be "ideological not only`
New: `Lea and Street's work, in Horner's account, shows the autonomous model to be "ideological not only`

C11. Line 215 (M1-39).
Old: `Kynard (p. 63) says the field's founding ethnography eclipsed race.`
New: `Kynard (p. 64) says the field's founding ethnography so "totally eclipsed discussions of race" at the time of desegregation (the chapter-three argument about Heath is on p. 63).`

C12. Line 144 area, Stuckey "Read depth" bullet (M1-40). The Old string is the second publisher quotation.
Old: `"It claims that the literacy profession perpetuates injustice, whether it knows it or not."`
New: `"It says that literacy, rather than enfranchising people, is violent, ulterior, and uniquely devoted to Western economic ends. It claims that the literacy profession perpetuates injustice, whether it knows it or not."`

C13. Line 153 (M1-41).
Old: `She also warns that "'media literacy' and 'critical thinking' will simply be deployed as an assertion of authority over epistemology."`
New: `She also warns that "[i]f we're not careful, 'media literacy' and 'critical thinking' will simply be deployed as an assertion of authority over epistemology."`

C14. Line 153 (M1-41).
Old: `of a frame she attributes to Nabiha Syed`
New: `of a frame she introduces after reporting Nabiha Syed on the "marketplace of ideas" (the sentence is boyd's own)`

C15. Line 177 (M1-44).
Old: `Street 2003 (p. 80) quotes them`
New: `Street 2003 (p. 80 names them; the quotations are on p. 81) quotes them`

C16. Line 221 (M1-47, structure; no change to words).
Old: `### (i) Must include`
New: `### (i) Must include (items 1-3 rest in part on works the facet did not open: Brandt 1998 journal text, Street 1984, Vee 2017; items 5-6 rest on abstracts or publisher pages only)`

### (3) Over-read and under-read

Over-read
1. The Vee-versus-paper contrast (L105, L238: "she sees the shift of power as toward the skilled; the paper ... toward the position-holders") is too tidy. Vee's own p. 49 and p. 54 sentences name the position-holders (programmers, software designers, firms). The paper's difference from Vee is that she does not treat the position as a wrong, not that she misses it (C5).
2. The "must include" ranking leans on four works not opened (Brandt journal text, Street 1984, Vee 2017, Stuckey) and two seen only as abstract (Prendergast). The facet labels them; a reader of the ranked list alone does not see the labels (C16).
3. Graff 2013 is cited as saying "literacy" is a "promotional label"; the source says "at times" (C9).
4. boyd: the warning is conditional ("If we're not careful") (C13).
5. Horner's sentence is credited to Street, but he is describing Lea and Street (C10).

Under-read
1. Vee 2013 p. 50: written contracts favoured over personal witnesses, and individuals "needed to be able to sign their names". That is the paper's §3.3 (record over voice) in a computing-literacy source, the single most useful sentence in Vee for the paper, and the facet missed it (C6).
2. Brandt report, PDF p. 8: enslaved African Americans, Cornelius 1991, and the workplace "legalistic" literacy passages; the facet says Brandt has no legal-bar case, which is true of worked cases only (C1).
3. Stuckey's blurb calls literacy "violent, ulterior, and uniquely devoted to Western economic ends" (C12).
4. Vee draws the ratchet from Brandt; so Brandt is upstream of Vee on both the ratchet and the commercial-sponsor point (C7).
5. Kynard also calls Heath's *Ways* "a literacy sponsor" (p. 63), which strengthens the facet's (c)1 point that "sponsor" is ordinary in the field.
6. Street 2003 p. 80 on Brandt and Clinton also has the sentence that distant literacies are "hegemonic" -- the word the paper could use for platform rules. Present in the facet at L83.

### (4) Counts for M1 (rows of the table in section (1), excluding the bib table)

Checked 47 rows: CONFIRMED 39 (qualified rows M1-6, 11, 25, 27, 33, 37, 47 counted here because every quotation matched; M1-7 and M1-15 are slips of capitalisation or hyphenation, counted CONFIRMED with cosmetic corrections), WRONG 6 (M1-20, M1-31, M1-34 attribution, M1-39, M1-41 framing, M1-44), UNVERIFIABLE 2 (M1-3, M1-29).
Bib: 24 DOIs resolved, 24 matched, 0 mismatches.

### (5) Not checkable

- Brandt 1998 CCC text (NCTE 403; no open copy I would use). The report wording is confirmed; the journal wording is not. A web search produced only student blogs, not reliable.
- Brandt 2001 *Literacy in American Lives* p. 19 (only Young's quotation seen); Street 1984 p. 97 (only via Vee); Vee 2017 (chapter titles and pages, no open copy; book not opened); Prendergast 2002 full text and 2003 book; Stuckey full text and imprint year (1990 v. 1991); Scribner and Cole full text; Bourdieu, Vincent, Stone, Kaestle, Heath, Luke, Buckingham full texts; Weninger and LaDousa beyond abstracts; Vieira 2016.
- Facet cross-references to Z, F and T files and to AUTHOR_DRAFT.md (e.g. "Intro ¶1" sentence) were not audited.
- The saved `prend2002.pdf` and `brandt_ncte.html` in pdfs/M1 are HTML pages, not usable sources.

---

# Facet M2

Files: `M2_algorithm_studies.md` (line numbers below are that file's), `M2_algorithm_studies.bib`.

Sources I opened: EU Official Journal texts (see "EU-law findings"); local PDFs in `pdfs/M2/` for Edwards and Veale (Duke pagination: PDF p. 50 = p. 67, 64 = p. 81, 65 = p. 82, 6 = p. 23), Dubal (PDF p. n = p. 1929 + n; PDF 52 = p. 1980), Selbst and Barocas (PDF 3 = p. 1086, 11 = p. 1094, 23 = p. 1106), Oeldorf-Hirsch and Neubaum preprint, Green, Li et al., Kolt, Gabriel et al., Lyons et al., Raghavan et al., Vincent et al. (text only, `pdftotext`); Crossref abstracts; arXiv abstract pages (Zhu et al., v1 to v3); Semantic Scholar abstract field for four ACM and SAGE items whose publisher pages are walled.

### (1) Table

| # | location | claim as written | verdict | what I opened; locator and what the source says | correction |
|---|---|---|---|---|---|
| M2-1 | l. 97 | PWD Directive (EU) 2024/2831, OJ L 11.11.2024, transposition by 2 December 2026 | CONFIRMED | OJ XHTML (Publications Office Cellar): header "11.11.2024", "of 23 October 2024"; Art 29(1): "bring into force ... by 2 December 2026". | none |
| M2-2 | l. 99 | Art 9(1)(b)(iii), (iv), 9(5), 9(6) quotations | CONFIRMED | OJ text, Art 9: (iii) "the categories of data and the main parameters ... influence the decisions"; (iv) "the grounds for decisions to restrict, suspend or terminate the account" (the OJ clause continues "of the person performing platform work, to refuse the payment ..."); 9(5) "persons undergoing a recruitment or selection procedure"; 9(6) "personal data generated through their performance of work ... including ratings and reviews", "free of charge", "directly to a third party". All verbatim. | none |
| M2-3 | l. 100 | Art 10(5), 10(2), 10(1) | CONFIRMED | OJ Art 10(5): "Any decision to restrict, suspend or terminate the contractual relationship or the account of a person performing platform work or any other decision of equivalent detriment shall be taken by a human being." 10(2) "competence, training and authority necessary to exercise that function, including for overriding automated decisions"; dismissal protection; 10(1) "regularly and in any event every two years". Verbatim. | none |
| M2-4 | l. 101 | Art 11(1)-(3), (5) | CONFIRMED | OJ Art 11 ("Human review"): (1) "right to obtain an oral or written explanation", "access to a contact person", "at the latest on the date on which it takes effect"; (2) "within two weeks of receipt"; (3) "within two weeks", "adequate compensation"; (5) "shall not apply to persons performing platform work who are also business users". Verbatim. | none |
| M2-5 | l. 102-103 | Art 8(1) DPIA "seek the views"; Arts 13-14; Art 7(1) bans incl. "racial or ethnic origin, migration status, political opinions" | CONFIRMED (nuance) | OJ Art 8(1) "shall seek the views of persons performing platform work and their representatives"; Art 7(1)(a),(b),(c),(e) match. Nuance: Art 13(3) is the expert provision; Art 14 is direct information to workers where there are no representatives. | none |
| M2-6 | l. 105 | DSA Art 20 incl. 20(6) quotations; six months; scope | CONFIRMED | OJ L 277 text: 20(1) "at least six months"; 20(4) "in a timely, non-discriminatory, diligent and non-arbitrary manner" and reversal duty; 20(6) "taken under the supervision of appropriately qualified staff, and not solely on the basis of automated means". Verbatim. Scope (1)(a)-(d) as stated. | none |
| M2-7 | l. 105 | DSA Art 21: "in good faith"; "shall not have the power to impose a binding settlement" | CONFIRMED | OJ Art 21(2): "Both parties shall engage, in good faith ..."; "The certified out-of-court dispute settlement body shall not have the power to impose a binding settlement of the dispute on the parties." Verbatim. | none |
| M2-8 | l. 107 | P2B Art 4 quotations | CONFIRMED | OJ L 186 (EU text, not the UK-retained one): 4(1) "on a durable medium"; 4(2) "at least 30 days"; 4(3) "to clarify the facts and circumstances". Identical to the facet's UK-version quotations. | none |
| M2-9 | l. 107 | P2B Art 5(1), 5(6) | CONFIRMED | OJ Art 5(1) "main parameters determining ranking and the reasons for the relative importance"; 5(6) "not be required to disclose algorithms or any information that, with reasonable certainty, would result in the enabling of deception of consumers or consumer harm through the manipulation of search results". Verbatim (the facet's "not required" omits the leading "be", acceptable inside quotes only as "not be required"; see C11). | C11 |
| M2-10 | l. 107 | P2B Arts 11, 12 | CONFIRMED | OJ Art 11(1) "free of charge"; 11(2)(c) "in an individualised manner"; Art 12(2)(a) "impartial and independent"; 12(3) "voluntary nature of mediation"; 12(4) "a reasonable proportion of the total costs". Both Arts exempt small-enterprise providers (11(5), 12(7)), which the facet omits. | none |
| M2-11 | l. 109 | GDPR Art 22(1), 22(3) | CONFIRMED | OJ L 119 text: 22(1) and 22(3) "at least the right to obtain human intervention on the part of the controller, to express his or her point of view and to contest the decision" verbatim; 22(3) applies to 22(2)(a) and (c). | none |
| M2-12 | l. 111 | AI Act Art 86(1) quotation | CONFIRMED (under-read) | OJ text 86(1): "shall have the right to obtain from the deployer clear and meaningful explanations of the role of the AI system in the decision-making procedure and the main elements of the decision taken" verbatim. The facet omits: Annex III "with the exception of systems listed under point 2" (critical infrastructure); the condition that the decision "produces legal effects or similarly significantly affects" the person "in a way that they consider to have an adverse impact on their health, safety or fundamental rights"; 86(3) "shall apply only to the extent that the right ... is not otherwise provided for under Union law". Art 113: "It shall apply from 2 August 2026" (original text; later amendments not checked). Annex III point 4 is employment. | C6 |
| M2-13 | l. 111 | AI Act Art 26(7) | CONFIRMED | OJ 26(7): "Before putting into service or using a high-risk AI system at the workplace, deployers who are employers shall inform workers' representatives and the affected workers that they will be subject to the use of the high-risk AI system." Facet's quotation is a verbatim substring. | none |
| M2-14 | l. 24 | Edwards and Veale p. 67: "transparency fallacy" passage | CONFIRMED | PDF 50 = printed p. 67: "Relying on individual rights to explanation as the means for users to take control of ML systems risks creating a similar 'transparency fallacy.' Individual data subjects are not empowered to make use of the kind of algorithmic explanations they are likely to be offered ... too time-poor, resource-poor, and lacking in the necessary expertise ..." Verbatim. | none |
| M2-15 | l. 25 | p. 67 "tremendous burden"; "disconnected from power"; "may occlude the true problems ..." | CONFIRMED | Same page. "placing a tremendous burden on individuals ... being 'disconnected from power'" is E&V's own gloss on Ananny and Crawford; "may occlude the true problems which rest in societal power relations and institutions as much as the software tools employed" verbatim. | none |
| M2-16 | l. 26 | p. 81: erasure and portability "rely too much on individual rights for what are too often group harms" | CONFIRMED | PDF 64 = p. 81, last paragraph, verbatim. | none |
| M2-17 | l. 27 | p. 82: "creating better systems, with less opacity, clearer audit trails, well and holistically trained designers, and input from concerned publics" / "grimly pursuing against the odds a 'meaningful' version of the interior of a black box" | CONFIRMED | PDF 65 = p. 82, verbatim. | none |
| M2-18 | l. 37 | E&V "agencies 'acting for users'" | WRONG | No such phrase anywhere in the 68-page text. Nearest wording, p. 23 (abstract/intro): "empowering agencies, such as NGOs, regulators, or civil society scrutiny organisations, to review the accuracy, lack of bias and integrity of a ML system in the round and not simply challenge ML decisions on behalf of individuals". | C1 |
| M2-19 | l. 60 | Dubal "p. 1980-1981": transparency and legibility are "one of the most frequently proposed policy reforms for platform labor" | WRONG (locator) | The sentence opens Part III.A on printed p. 1979 (PDF 51): "One of the most frequently proposed policy reforms for platform labor in the global fight to recognize the employment status ...". The Farrar/Aslam UK Supreme Court (February 2021) account is p. 1980. | C2 |
| M2-20 | l. 60-61 | Farrar/Aslam win (Feb. 2021); Farrar "what we really want are inference data ..." pp. 1981-1982 | CONFIRMED | PDF 52-54: "U.K. Supreme Court in February 2021"; "[W]hat we really want are inference data. What decisions has [the app] made about me? How has it profiled me? How does that affect my earnings? This is what Uber has not given us." Quote spans pp. 1981-1982. | none |
| M2-21 | l. 62-63 | p. 1982 "reverse engineer ... have yet to change firm practices"; p. 1983 Uber and Ola "safety and security" | CONFIRMED | PDF 54 (p. 1982) and 55 (p. 1983), verbatim. | none |
| M2-22 | l. 64 | p. 1984 Amsterdam (April 2023); "firm transparency ... does not by itself shift the power dynamics"; "Knowledge alone will not end or mitigate the precarities of digitalized pay." | CONFIRMED | PDF 56 = p. 1984, verbatim ("In April 2023, however, the Amsterdam appellate court overturned the decision, finding that Uber 'must explain how driver personal data and profiling is used in Uber's upfront, dynamic pay and pricing system.'"). | none |
| M2-23 | l. 65 | pp. 1985-1986 countercollect; contest errors; "lack of a formal appeals mechanisms" (1985); "primarily a structural problem" (1986); "do not address the most significant harms" (1986) | CONFIRMED | PDF 57-58, verbatim. | none |
| M2-24 | l. 37 | Dubal: "knowledge alone is 'ineffectual'" | WRONG (loose attribution) | p. 1984: "Absent a ban on algorithmic wage discrimination under Article 22 of the GDPR or through collective bargaining agreements, transparency requests are by themselves ineffectual." The word is said of transparency requests, conditional on no ban or bargaining; "Knowledge alone will not end or mitigate ..." is the next sentence. | C3 |
| M2-25 | l. 66 | Dubal remedy "a narrowly structured, nonwaivable peremptory ban" | CONFIRMED | Abstract/intro, p. 1940 (PDF 12): "a narrowly structured, nonwaivable peremptory ban on the practice" (algorithmic wage discrimination). "data abolition" is Dubal's term (p. 1979 and n. 214). | none |
| M2-26 | l. 109 | Dubal pp. 1982-1984 workers use Arts 15 and 22 and won in Amsterdam 2023 | CONFIRMED | PDF 54-56: GDPR Arts 15 and 22 discussed with nn. 225-226; Amsterdam April 2023 p. 1984. | none |
| M2-27 | l. 49 | Cameron and Rahman (2022): "everyday interactions with customers can influence and manipulate algorithms in ways that platforms cannot always observe" | CONFIRMED | Crossref abstract of 10.1287/orsc.2021.1557, last sentence, verbatim ("workers' everyday interactions ..."). Org Sci 33(1), 38-58 matches. | none |
| M2-28 | l. 49 | the 2021 conference version says "compared to customers, workers had greater knowledge of how the platforms' algorithms worked, and used this expertise to manipulate customers" | UNVERIFIABLE | Crossref gives doi 10.5465/ambpp.2021.237 the title "(Not) Seeing Like an Algorithm: Managerial Control and Worker Resistance in the Platform Economy" (not the 2022 title) with no abstract; doi.org answered with a Cloudflare challenge (403). Not bypassed. | C12 |
| M2-29 | l. 49 | Cameron (2024): "engagement" and "deviance" tactics; both "elicit consent"; "choice-based consent can mask the more-structurally problematic elements of the work"; "constant and confined choices" | CONFIRMED | Crossref abstract of 10.1177/00018392241236163, verbatim; title has "Constant and Confined Choices". ASQ 69(2) 458-514, June 2024. | none |
| M2-30 | l. 31 | Selbst and Barocas: "normatively defensible" (abstract, p. 1086); p. 1094 "The process of moving from observation to knowledge to accountability cannot be assumed ..."; "seek explanations of the process behind a model's development"; pp. 1106-1107 Art 22 | CONFIRMED | PDF 3 (p. 1086), 11 (p. 1094), 23 (p. 1106), verbatim. | none |
| M2-31 | l. 45 | Oeldorf-Hirsch and Neubaum: abstract direction 1; p. 23 "Having proposed that algorithmic literacy should not be solely the responsibility ..."; Eslami 62.5%; Rader and Gray; "the new algorithmic divide"; Rader et al. 2018 short statements p. 22 | CONFIRMED | Preprint PDF 2 (abstract), 10, 22, 23, verbatim. "necessary future work" on p. 16. | none |
| M2-32 | l. 91 | Green (2022): "rest on an uninterrogated assumption ..."; "false sense of security"; 41 policies | CONFIRMED | Abstract/p. 1: "I survey 41 policies"; both phrases verbatim. | none |
| M2-33 | l. 134 | Li et al. (2022) abstract quotation; "data divide"; "monopoly on data and algorithms"; "position paper" | CONFIRMED | Preprint pp. 1-2: "we argue that a bottom-up approach that empowers individual workers ... is a practical way to bridge AI inequality in gig work under the current paradigm of privately owned platforms. This position paper ..." (facet's "practical way" run is verbatim when the interleaved ACM reference block is removed). | none |
| M2-34 | l. 138 | Kolt: loyalty "ensuring that those agents act in the best interests of their users and seek user consent where appropriate" | CONFIRMED | arXiv PDF p. 8: "The third issue concerns loyalty, which is part of an agent's fiduciary obligation under common law. In the case of AI agents, it involves ensuring that ..." | none |
| M2-35 | l. 138 | Gabriel et al.: two assistants negotiating "on behalf of their users" | CONFIRMED | arXiv-paginated PDF p. 141: "two AI assistants negotiate on behalf of their users to determine a mutually beneficial restaurant choice". | none |
| M2-36 | l. 138 | Gabriel: "verifiable commitments (arXiv pp. 141-142)" | WRONG | Pages 141-142 do not discuss commitments. "Verifiable claims" appears on p. 134 (Brundage et al.). "credible commitment" appears on p. 147 (as a tool for coercion and tie-breaking) and p. 214 ("AI assistants may use credible commitments to pressure third parties"). | C4 |
| M2-37 | l. 138 | Zhu et al.: "deal-making with LLM agents in consumer settings is an inherently imbalanced game" with "large disparities" and "overspending" | WRONG | arXiv 2506.00073 abstract, identical in v1, v2, v3: "AI-mediated deal-making is an inherently imbalanced game -- different agents achieve significantly different outcomes for their users. Moreover, behavioral anomalies in LLMs can result in financial losses ..., such as overspending or accepting unreasonable deals." "large disparities" is not in the abstract. | C5 |
| M2-38 | l. 87 | Lyons et al.: "The ability to contest algorithmic decisions is being recognised as an important safeguard for individuals. Yet, there is little guidance ..."; "resembles contestability in relation to human decision-making" | CONFIRMED | arXiv v1 p. 1, verbatim; second phrase pp. 1, 15. | none |
| M2-39 | l. 79 | Raghavan et al.: "little is known ..."; "Cognitive assessments have imposed adverse impacts on minority populations ..."; "the gold standard for pre-employment assessments"; Uniform Guidelines | CONFIRMED | arXiv pp. 1, 4, verbatim. | none |
| M2-40 | l. 43 | Long and Magerko: "a concrete definition of AI literacy"; "a set of core competencies"; "learner-centered AI" | CONFIRMED | Semantic Scholar abstract of 10.1145/3313831.3376727, verbatim (ACM page walled; this is a secondary host). | none |
| M2-41 | l. 89 | Bayamlioglu: right to contest is "the core remedy"; Almada: human intervention can "introduce biases and limitations" | CONFIRMED | Crossref abstract (Bayamlioglu: "identifies the right to contest in Article 22 as the core remedy"); Semantic Scholar abstract (Almada: "the human intervention itself might introduce biases and limitations"). | none |
| M2-42 | l. 47, 49, 69 | Petrovcic N = 802 Slovenia and "algorithm knowledge was a significant determinant of internet uses"; Christin "buffering strategies" (foot-dragging, gaming, open critique); Karusala "intermediaries like NGO workers or lawyers" | CONFIRMED | Semantic Scholar abstracts, verbatim. | none |
| M2-43 | l. 136 | Vincent et al.: "reducing, stopping, redirecting, or otherwise manipulating data contributions" | CONFIRMED | Local PDF, p. 1 (two-column hyphenation: "oth- erwise"). | none |
| M2-44 | l. 33, 58 | Ananny and Crawford "10 limitations"; abstract wording | CONFIRMED | Crossref abstract: "present 10 limitations to its application"; "Being able to see a system is sometimes equated with being able to know how it works and govern it". | none |
| M2-45 | l. 58, 88, 90, 47 | Kellogg "algoactivism"; Kaminski and Urban volume/pages (121, 1957-2048) and "individual right to contest ... due process"; Karimi recourse gloss; Cotter and Reisdorf "varies according to socioeconomic advantage" | UNVERIFIABLE | Kellogg Crossref abstract truncated at "contested..."; Kaminski and Urban absent from Crossref (my query returned unrelated items); publisher pages walled. The facet marks all as unread. | none |
| M2-46 | l. 138 | Consumer Reports Innovation Lab post: author Dazza Greenwood; "legal foundations" | CONFIRMED | Saved page `crreport.html`: author schema "Dazza Greenwood"; "Legal Foundations" is in the post title; UETA section present. | none |
| M2-47 | bib (49 DOIs) | Every DOI resolves; title, venue, volume, pages | CONFIRMED | Crossref, 49 of 49 DOIs with a DOI field (all 49 queried, not a sample): titles and venues match; volume, issue and pages match except as in M2-48. Kaminski and Urban has no DOI (consistent). | none |
| M2-48 | bib, 3 entries | `oeldorf2023what` year 2023, vol. 27; `gagrcin2024algorithmic` year 2024, vol. 28; `petrovcic2024disentangling` year 2024, vol. 28 | WRONG | Crossref: Oeldorf-Hirsch and Neubaum, *New Media & Society* 27(2) 681-701, published-print 2025-02 (online 2023-07); Gagrcin et al. 28(1) 423-447, print 2026-01 (online 2024-11-08); Petrovcic et al., *Information, Communication & Society* 28(4) 557-574, print 2025-03-12 (online 2024-06-10). Volume and pages are print-issue, the year is online-first: they do not agree. (Online-first years for ananny2018seeing, bucher2017, wood2019, alfrink2023, bayamlioglu2022 differ from the Crossref "issued" year too, but those bib years are the print years and are right.) | C8, C9, C10 |
| M2-49 | bib EU notes | "EUR-Lex returned a bot challenge"/"blocked"; texts read in secondary copies | CONFIRMED (now superseded) | EUR-Lex and data.europa.eu returned HTTP 202 with an empty body (a bot challenge). The Publications Office Cellar endpoint did serve the official text (see EU-law findings), so the facet's quotations can be marked as checked against the Official Journal. | C7, C13, C14, C15 |
| M2-50 | l. 12-14 | Counts: 54 bib entries incl. 5 legal acts | CONFIRMED | `grep -c "^@"` = 54. | none |

### (2) Corrections

Grouped by file. Each Old string occurs once in its file (checked with `grep -cF`).

### M2_algorithm_studies.md

C1. Line 37 (M2-18).
Old: `agencies "acting for users"`
New: `agencies "such as NGOs, regulators, or civil society scrutiny organisations" (p. 23)`

C2. Line 60 (M2-19).
Old: `  - p. 1980-1981: transparency and legibility are "one of the most frequently proposed policy reforms for platform labor".`
New: `  - p. 1979: transparency and legibility are "One of the most frequently proposed policy reforms for platform labor" (opening of Part III.A). Pp. 1980-1981:`

C3. Line 37 (M2-24).
Old: `Dubal (below) goes further: knowledge alone is "ineffectual" and the remedy is a ban.`
New: `Dubal (below) goes further: "transparency requests are by themselves ineffectual" absent a ban or collective bargaining, and "Knowledge alone will not end or mitigate the precarities of digitalized pay" (p. 1984); her remedy is a ban on algorithmic wage discrimination.`

C4. Line 138 (M2-36).
Old: `negotiating "on behalf of their users" and verifiable commitments (arXiv pp. 141-142)`
New: `negotiating "on behalf of their users" (arXiv p. 141) and, elsewhere, "credible commitment" as a way to pressure the other side (arXiv pp. 147, 214)`

C5. Line 138 (M2-37).
Old: `"deal-making with LLM agents in consumer settings is an inherently imbalanced game" with "large disparities" between agents and risk of "overspending"`
New: `"AI-mediated deal-making is an inherently imbalanced game -- different agents achieve significantly different outcomes for their users", with LLM "behavioral anomalies" that can cause "overspending or accepting unreasonable deals" (arXiv abstract, v1 to v3)`

C6. Line 111 (M2-12).
Old: `a person subject to a decision taken on the output of a high-risk system listed in Annex III "shall have the right to obtain`
New: `a person subject to a decision taken by the deployer on the output of a high-risk system listed in Annex III (except point 2, critical infrastructure), where the decision produces legal effects or similarly significantly affects the person adversely "in a way that they consider to have an adverse impact on their health, safety or fundamental rights" (Art 86(3): only to the extent the right is not otherwise provided for under Union law), "shall have the right to obtain`

C7. Line 7 (M2-49).
Old: `Because EUR-Lex was blocked, **no EU legal text below is from the official portal**: each entry says which copy I read.`
New: `Because EUR-Lex was blocked, I first read the EU texts below in secondary copies; AUDIT_05 later checked each EU quotation against the Official Journal text served by the Publications Office (publications.europa.eu/resource/celex/<CELEX>, header Accept: application/xhtml+xml) and found them verbatim.`

C12. Line 49 (M2-28).
Old: `the 2021 conference version says "compared to customers, workers had greater knowledge of how the platforms' algorithms worked, and used this expertise to manipulate customers"`
New: `the 2021 conference version (Crossref title "(Not) Seeing Like an Algorithm: Managerial Control and Worker Resistance in the Platform Economy"; its abstract could not be opened in AUDIT_05, so this wording is UNVERIFIED) is said to say "compared to customers, workers had greater knowledge of how the platforms' algorithms worked, and used this expertise to manipulate customers"`

C11. Line 107 (M2-9).
Old: `providers are "not required to disclose algorithms or any information that, with reasonable certainty, would result in the enabling of deception`
New: `providers shall "not be required to disclose algorithms or any information that, with reasonable certainty, would result in the enabling of deception`

### M2_algorithm_studies.bib

C8. Line 90 (M2-48).
Old: `year    = {2023}, volume = {27}, pages = {681--701},`
New: `year    = {2025}, volume = {27}, number = {2}, pages = {681--701},`

C9. Line 115 (M2-48).
Old: `year    = {2024}, volume = {28}, pages = {423--447},`
New: `year    = {2026}, volume = {28}, number = {1}, pages = {423--447},`

C10. Line 124 (M2-48).
Old: `year    = {2024}, volume = {28}, pages = {557--574},`
New: `year    = {2025}, volume = {28}, number = {4}, pages = {557--574},`

(C8 to C10 change the year; the keys `oeldorf2023what`, `gagrcin2024algorithmic`, `petrovcic2024disentangling` carry the online-first year and may stay as keys to avoid breaking citations elsewhere.)

C13. Bib, P2B entry (M2-49).
Old: `Not the official EU text.}`
New: `Not the official EU text; AUDIT_05 later found Arts 4, 5, 11, 12 identical in the Official Journal text (OJ L 186, 11.7.2019, p. 57).}`

C14. Bib, DSA entry (M2-49).
Old: `that cites OJ L 277, p. 1-102. Not the official text.}`
New: `that cites OJ L 277, p. 1-102. Not the official text; AUDIT_05 later found Arts 20 and 21 verbatim in the Official Journal text.}`

C15. Bib, AI Act entry (M2-12, M2-49).
Old: `EUR-Lex blocked. Articles 26(7) and 86 READ in springlex.eu. Annex III (employment) NOT opened. Dates of application NOT checked.}`
New: `EUR-Lex blocked. Articles 26(7) and 86 READ in springlex.eu and later checked verbatim against the Official Journal text (AUDIT_05). Annex III point 4 is employment and workers' management; Art 113 of the original text: applies from 2 August 2026 (later amendments not checked).}`

### (3) Over-read and under-read

1. Over-read, edges of a quotation. Edwards and Veale never say "acting for users" (C1); Dubal's "ineffectual" is said of transparency requests, not of knowledge (C3); the Zhu and Gabriel strings are not in their sources (C4, C5). None of these changes a conclusion, but the author will carry the quoted words into the outline.
2. Over-read, the "zero leverage" test (l. 52). The facet says the author's §5.1 sentence is "too strong". `AUTHOR_DRAFT.md` l. 122 reads "achieving high algorithmic comprehension gives a platform worker zero leverage over a closed optimization model". The facet cuts the sentence before "over a closed optimization model". Cameron and Rahman's leverage is over customers' ratings; Cameron's choices are within the system. The facet's own "supportable claim" (no leverage over the pay rule, the termination, the record) is close to the draft as written. The conflict is smaller than the facet makes it.
3. Under-read, AI Act Art 86: it is limited to Annex III (minus point 2), requires an adverse impact on health, safety or fundamental rights, and is residual to other Union law (C6). In the facet's own §5.3 table (l. 122) the AI Act is not used, but §(iii) lists "AI Act Art 86" as a counterpart; it should carry those limits.
4. Under-read, P2B Arts 11 and 12 do not apply to small-enterprise providers (11(5), 12(7)); DSA Art 20 applies to online platforms and its scope is content, account and monetisation decisions (the facet says this). Both narrow the counterpart further.
5. Right and worth keeping: PWD Arts 9, 10(5), 11, 29(1) (all verbatim); DSA Art 21's non-binding bodies; the Edwards and Veale pp. 67, 81-82 passages; Dubal pp. 1983-1986; the facet's reading that the reviewer under PWD Art 11(2) is the platform itself ("The digital labour platform shall respond").
6. PWD Art 10(5) is stronger than the facet's table suggests for one point: it applies to "any other decision of equivalent detriment", not only termination. It is still platform-internal, so the facet's independence point holds.

### (4) EU-law findings

Hosts. `eur-lex.europa.eu` (HTML, PDF and ELI paths) and `data.europa.eu/eli/...` answered HTTP 202 with an empty body (a bot challenge); I did not try to get round it. The Publications Office's own Cellar endpoint, `https://publications.europa.eu/resource/celex/<CELEX>` with the header `Accept: application/xhtml+xml` (anonymous, generic User-Agent), returned the Official Journal text of 32024L2831, 32022R2065, 32019R1150, 32016R0679 and 32024R1689 (HTTP 200, the XHTML carries the OJ header: PWD "L series 2024/2831, 11.11.2024"; DSA "L 277/1, 27.10.2022"; P2B "L 186/57, 11.7.2019"; GDPR "L 119/1, 4.5.2016"; AI Act "2024/1689, 12.7.2024"). This is the official source; I used it for all wording below. Files are in `pdfs/audit5/M2/`.

Findings. Every EU quotation in the facet matches the Official Journal word for word: PWD Art 9(1)(b)(iii)-(iv), 9(5), 9(6), Art 10(1), 10(2), 10(5), Art 11(1)-(3) and (5), Art 8(1), Art 7(1), Art 13(3); transposition "by 2 December 2026" (Art 29(1)); DSA Art 20(1), 20(4), 20(6) and Art 21(2) ("shall not have the power to impose a binding settlement of the dispute on the parties"); P2B Arts 4, 5(1), 5(6), 11, 12 (the facet read the UK-retained text on legislation.gov.uk; the EU text is identical in every quoted phrase); GDPR Art 22(1), 22(3); AI Act Art 26(7) and 86(1). One quotation fragment misses "be" (C11). One legal characterisation is incomplete: AI Act Art 86 has a scope exclusion (Annex III point 2), a harm condition and a residual clause (C6). Art 113: the original text applies the Act from 2 August 2026; I did not check for later amendments or postponements of the Annex III duties. Recital and later amendments of the PWD were not checked either.

Edwards and Veale (2017): pp. 67 and 81-82 verified (PDF 50, 64, 65), except the invented "acting for users" (C1). Dubal (2023): p. 1984 verified; p. 1979 not 1980-1981 for "most frequently proposed" (C2). Cameron and Rahman (2022) and Cameron (2024): quoted abstract wording verified in Crossref; the 2021 conference-version quotation could not be opened (C12). The facet's use of Cameron and Rahman as "against zero leverage" is a fair reading of an abstract, but see over-read 2.

### (5) Counts

Rows: 50 checked; 42 CONFIRMED (M2-5 and M2-12 with qualifications; M2-49 confirmed but superseded); 6 WRONG (M2-18, 19, 24, 36, 37, 48); 2 UNVERIFIABLE (M2-28, M2-45; M2-45 groups several works). 42 + 6 + 2 = 50. EU-law rows M2-1 to M2-13 (13 rows): 13 confirmed.

### (6) Not checkable and why

- Cameron and Rahman 2021 conference abstract (AOM page: Cloudflare challenge, 403).
- Kellogg et al. "algoactivism" (Crossref abstract truncated; publisher page walled); Kaminski and Urban pages and argument (no DOI record; repositories walled); Karimi, Cotter and Reisdorf, Ng et al., Burrell, Wachter et al., Ananny and Crawford beyond the abstract (not opened by me).
- Long and Magerko, Almada, Christin, Karusala, Petrovcic: checked only against the Semantic Scholar abstract field (a secondary host; ACM, SAGE, Taylor and Francis pages walled).
- Kolt volume and "forthcoming" status; Crossref's SSRN record is dated 2024.
- Any later amendment to the AI Act or PWD after the original Official Journal texts.
- Disclosure: no e-mail address, `mailto`, Unpaywall or browser tool was used; no e-mail address appears in the two M2 files.

---

# Facet M3

Sources: Hill, Walker-Thomas and Specht texts as saved in `pdfs/M3/` (Harvard Cyberlaw copy of Hill; UVM copy of Walker-Thomas; Michigan excerpt of Specht with star paging), plus an independent CourtListener search record for Walker-Thomas (judge, date, dissent). Justia, casetext, openjurist and CourtListener opinion pages returned bot walls or 4xx on re-fetch; I could not obtain a second full-text copy of Hill, so its words rest on the Harvard copy only. CRA 2015 ss. 62 and 68 re-fetched from legislation.gov.uk (200). UINL pages re-read from the saved copies; canonical uinl.org URLs resolve (200). Khan and Pozen re-fetched from harvardlawreview.org (byte-identical to the saved file). Ben-Shahar and Schneider: only the saved font-decoded copy; the Penn Law repository page gave no PDF. Bakos et al.: 2009 working paper (saved) plus the OpenAlex abstract of the published JLS article. Crossref used for 29 DOIs in the bib.

Line numbers: those in the corrections (15, 17, 29, 69, 117, 126, 134, 163, 167, 190, 293, 311, 333) were grepped; the "location" column otherwise gives entry-level ranges (Messick 64-69, Hill 113-117, Walker-Thomas ~119-125, Specht ~126-130, Bakos ~131-137, Ben-Shahar ~138-143, CRA 151, Balkin/Khan/Kolt/Citron/UINL ~157-190, Simmel 202) and may be a few lines off.

| # | location (lines in M3 .md) | claim as written | verdict | what I opened; locator and what the source says | correction |
|---|---|---|---|---|---|
| M3-1 | 112-113 | Hill: "A contract need not be read to be effective; people who accept take the risk that the unread terms may in retrospect prove unwelcome." | CONFIRMED | Harvard Cyberlaw copy of 105 F.3d 1147, Easterbrook J. (opinion header "EASTERBROOK, Circuit Judge"); sentence follows the ProCD / Federal Arbitration Act paragraph. Exact. Copy has no reporter pagination, so no pin cite. | none |
| M3-2 | 117 | Hill: "Competent adults are bound by such documents, read or unread." | CONFIRMED | Same copy, final reasoning paragraph, after "Customers as a group are better off when vendors skip costly and ineffectual steps such as telephonic recitation, and use instead a simple approve-or-return device." Exact. | none |
| M3-3 | 115 | Hill read-aloud quotation: "If the staff at the other end of the phone ... droning voice would anesthetize rather than enlighten many potential buyers." | CONFIRMED | Same copy: "Cashiers cannot be expected to read legal documents to customers before ringing up sales. If the staff at the other end of the phone for direct-sales operations such as Gateway's had to read the four-page statement of terms before taking the buyer's credit card number, the droning voice would anesthetize rather than enlighten many potential buyers. Others would hang up in a rage over the waste of their time." Exact. | none |
| M3-4 | 15; 117; 311 | Characterisation: the court "considered a read-aloud rule and rejected it"; "looked at exactly that safeguard"; "judged and rejected the read-aloud analogue"; "weighed reading-aloud ... and rejected it" | WRONG (over-read) | Hill is about whether Gateway's own staff had to recite terms to buyers (cashiers, telephone sales); the court says this would be "costly and ineffectual" and offers it as an aside supporting the approve-or-return device. It is dicta in a ProCD-follow-on case on terms inside the box; the buyers could read, and the reader would be the counterparty, not a neutral third party reading to a non-reader. The paper's safeguard (a trusted person reading to a signer who cannot) is not what the court discusses. | C1-C4 |
| M3-5 | 123-127 | Walker-Thomas: "we hold that where the element of unconscionability is present at the time a contract is made, the contract should not be enforced."; "Unconscionability has generally been recognized to include an absence of meaningful choice ... together with contract terms which are unreasonably favorable to the other party." | CONFIRMED | UVM copy, 350 F.2d 445, 121 U.S. App. D.C. 315; both sentences adjacent, immediately after the court calls UCC § 2-302 "persuasive authority". Exact. | none |
| M3-6 | 125 | "Did each party to the contract, considering his obvious education or lack of it, have a reasonable opportunity to understand the terms of the contract, or were the important terms hidden in a maze of fine print and minimized by deceptive sales practices?" | CONFIRMED | Same copy, exact. "Ordinarily, one who signs an agreement without full knowledge of its terms might be held to assume the risk that he has entered a one-sided bargain. But when a party of little bargaining power, and hence little real choice, signs a commercially unreasonable contract with little or no knowledge of its terms, it is hardly likely that his consent, or even an objective manifestation of his consent, was ever given to all the terms." also exact. | none |
| M3-7 | 121 | Walker-Thomas: Skelly Wright J.; D.C. Cir. 1965 | CONFIRMED | CourtListener search record: judge panel "Bazelon, Danaher, Wright", filed 1965-08-11, opinion opens "J. SKELLY WRIGHT, Circuit Judge" (snippet spells "SHELLY"); decision date also in UVM copy header ("Decided August 11, 1965"). The same record shows a dissent by Danaher, which the facet does not mention (see under-read). | none |
| M3-8 | 128-131 | Specht: "When products are 'free' and users are invited to download them in the absence of reasonably conspicuous notice that they are about to bind themselves to contract terms, the transactional circumstances cannot be fully analogized to those in the paper world of arm's-length bargaining." | CONFIRMED | Michigan excerpt (306 F.3d 17, Sotomayor, Circuit Judge, per the excerpt), star page *32: exact. | C5 (adds pin) |
| M3-9 | 129 | Specht quotes California law: "an offeree, regardless of apparent manifestation of his consent, is not bound by inconspicuous contractual provisions of which he is unaware, contained in a document whose contractual nature is not obvious." | CONFIRMED | Same excerpt, star page *30, citing Windsor Mills. Exact. | C5 (adds pin) |
| M3-10 | 131-135 | Bakos, Marotta-Wurgler and Trossen working paper: "only one or two out of every thousand retail software shoppers chooses to access the license agreement ... spend too little time ... to have read more than a small portion"; "only about 0.1 or 0.2 percent access a product's EULA for at least one second"; 45,091 households, 66 companies | CONFIRMED | NET Institute Working Paper #09-04, August 2009 (saved copy): abstract and introduction, exact; "45,091 unique visitors" / "66 online software companies" exact. Note the 0.1-0.2 percent figure counts a visit of at least one second ("access" defined conservatively, same paper). | none |
| M3-11 | 134; 137 | Published JLS version has "different sample figures (48,154 visitors, 90 companies)"; "I did not open it" | CONFIRMED (and completed) | OpenAlex abstract for DOI 10.1086/674424 (J. Legal Studies 43(1): 1-35, Jan 2014; Crossref agrees on title, venue, year, pages): "We track the Internet browsing behavior of 48,154 monthly visitors to the Web sites of 90 online software companies ... only one or two of every 1,000 retail software shoppers access the license agreement and that most of those who do access it read no more than a small portion." The abstract does not use the "0.1 or 0.2 percent" wording; I could not open the JLS full text (publisher bot wall), so I cannot say whether the body repeats it. | C6 |
| M3-12 | 141-145 | Ben-Shahar and Schneider, 159 U. Pa. L. Rev. 647: abstract (p. 647) "the failure of the mandated disclosure regime in informing people and in improving their decisions"; "not only fails to achieve its stated goal but also leads to unintended consequences that often harm the very people it intends to serve"; p. 731 "If nobody reads disclosures, it does not matter that some nonreaders are sophisticated."; p. 672 quoting Marotta-Wurgler "No matter how prominently [end-user license agreements] are disclosed, they are almost always ignored." | CONFIRMED | Saved font-decoded copy: running head "The Failure of Mandated Disclosure 731"; page 672 header "University of Pennsylvania Law Review [Vol. 159: 647"; abstract sentences exact. Crossref: SSRN record 10.2139/ssrn.1567284 (issued 2010) and book chapter 10.23943/princeton/9780691161709.003.0003 (2014) both titled "The Failure of Mandated Disclosure". Decoding is the facet's own; I checked against the text, not an independent PDF. | none |
| M3-13 | 190 | UINL *Principles of the notarial function*, Part I: "professional lawyers and public officials appointed by the State ..."; "required to act both impartially and independently, outside any State hierarchy"; "a Notary's impartiality can also take the form of lending adequate assistance to whichever of the parties might be in a position of inferiority." Rome, 8 November 2005 | CONFIRMED | uinl.org/fundamental-principles/principles-of-the-notarial-function/ (saved copy; URL resolves): all three passages exact; page ends "Approved by the General Meeting of member Chambers of Notaries of the UINL Rome, Italy - 8th November 2005". | none |
| M3-14 | 192-193 | UINL notarial ethics principle 9: "must balance the respective interests of the parties concerned and seek a solution with the sole objective of safeguarding both parties"; principle 10: "inform and advise the parties as to the possible consequences of their instructions ... awareness of the legal force of the deed" | CONFIRMED | uinl.org/fundamental-principles/principles-of-notarial-ethics/ (saved copy): headings "9. Impartiality and independence" and "10. Diligence and liability"; wording exact. | none |
| M3-15 | 190; bib `uinl2005ethics`; 17; 293 | Ethics principles treated as 2005 / "Date not shown on the page opened"; "(UINL 2005)" for duty to both parties | WRONG | The ethics page ends: "Approved by the General Meeting of Member Chambers of Notaries of the UINL, Mexico City, Mexico - 17th October 2004." So the "both parties" text is 2004 (Mexico City), and the "weaker party" text is the 2005 Rome function document. | C7, C8, C9, C10 |
| M3-16 | 211-213 | Simmel (Wolff 1950) p. 154, "The Tertius Gaudens": "the impartiality of the third element either served or harmed the group as a whole. Both the mediator and the arbitrator wish to save the group unity from the danger of splitting up. But, evidently, the non-partisan may also use his relatively superior position for purely egoistic interests."; "a means for his own purposes"; gloss "the third who enjoys"; index pp. 154-162, 232-234; 162-169; 166 | CONFIRMED | archive.org full text (saved): section opens under running head "154 The Triad"; sentences exact (text has "non- partisan" line-break hyphen); translator's footnote 18 "Literally, 'the third who enjoys' ..." falls at the foot of p. 154. Contents: "3. The Tertius Gaudens 154"; "4. Divide et Impera 162". Index: "Tertius gaudens, 154-162, 232-234"; "Divide et impera, 162-169"; "Distrust, as means of divide et impera, 166". | none |
| M3-17 | 62-69 | Messick (1993): "the calligraphic state was both a political entity and a discursive condition"; "Textual domination, in this analysis, entails the interlocking of a polity, a social order, and a discursive formation"; "the manuals discuss witnessing support for documents, but they do not consider documents to be potential evidence"; "an oral core is complemented by a written surround"; "in actuality relied heavily on the services of the written word"; "evolved into the certified notary of the Malikis"; "an 'adil was a notary"; "a further intervening link in the human transmission of evidence"; "began a lucrative parallel career writing legal instruments"; "acts as a notary (katib) who prepares written legal instruments" | CONFIRMED | UC Press E-Books archive text (saved): all exact (the source prints "(katib )" with a space). "209 The Chastity of Documents" is a running head, so the oral-core and written-surround sentences are on p. 209 as the facet says; the "do not consider documents" sentence follows within the same section (pp. 209-210 as stated). Scale (highland Yemen) correct. | none |
| M3-18 | 69 | "the 'textual erasure of oral pacts' is not the only arrangement writing has produced" (in quotation marks) | WRONG | Searched the whole Messick text for "erasure", "erase", "pact": only a register notarial formula ("free of alteration and erasure") and a hadith about erasing notes turn up. The phrase is not in Messick, and is not in `AUTHOR_DRAFT.md` (grep: "erasure" occurs only in the facet's M2 and M3 files and in two unrelated lines of the draft about residential schools). The scare quotes imply a quotation that I cannot locate. | C11 |
| M3-19 | 163-167 | Khan and Pozen, 133 Harv. L. Rev. 497: p. 498 "garnered remarkably broad support and essentially zero critical pushback"; p. 502 "invites an enervating complacency about issues of structural power and a premature abandonment of more robust visions of public regulation"; Part I "Fiduciaries for Whom?" p. 502; p. 503 Delaware "must ... treat stockholder welfare as the only end"; p. 504 "A fiduciary with sharply opposed loyalties teeters on the edge of contradiction." and "the untenable position of having to violate their fiduciary duties (to stockholders) under Delaware law in order to fulfill their fiduciary duties (to end users)" | CONFIRMED | harvardlawreview.org PDF re-fetched (byte-identical to saved file); page-by-page extraction: "garnered" PDF p. 2 (= p. 498); "enervating complacency" sentence runs from p. 501 to the top of p. 502 (the abstract on p. 498 has the variant "toward online platforms' structural power"); "Fiduciaries for Whom?" p. 502; Delaware quotation p. 503; "teeters" and "untenable position" p. 504. Exact. | none |
| M3-20 | 29; 163; 333; bib line 24 | The HLR PDF "is a 10-page excerpt (abstract, introduction, start of Part I, footnotes)"; "Parts II-IV not read" | WRONG | The same URL, re-fetched, returns a 45-page PDF (399,907 bytes, same as the saved file): the full article, pp. 497-541, with Part II.A "Managing Divided Loyalties" at pp. 508-510, Part III, Part IV and Part V "Alternative Analogies". The facet's reading depth is understated and its "could not open" item is wrong. | C12-C15 |
| M3-21 | 163 | "The Columbia repository entry I saw said the paper was withdrawn." | CONFIRMED | Saved `khan_pozen.html`: "This paper has been withdrawn." (I did not re-fetch the repository.) | none |
| M3-22 | 167 | Khan and Pozen supports the claim that a duty "to two users" cannot sit in the platform | CONFIRMED (qualified) | The article's loyalty conflict is stockholders versus users, not user versus user; Part II.A (p. 508) says "Balkin has never squarely addressed the issue of crosscutting loyalties". The facet's inference ("a duty of impartiality to two users cannot sit in the platform without a change in law") is the facet's own extension and should be marked so. | C15 |
| M3-23 | 175-179 | Kolt: abstract "new technical and legal infrastructure is needed to support governance principles of inclusivity, visibility, and liability"; p. 10 n. 26 quoting Restatement (Third) of Agency § 1.04 cmt. e "a computer program is not capable of acting as a principal or an agent as defined by the common law. At present, computer programs are instrumentalities of the persons who use them."; Kolt notes "at present" and thin support; p. 25 "fiduciary duty to act loyally for the principal's benefit in all matters connected with the agency relationship" | CONFIRMED | arXiv PDF 48 pp. (saved): abstract on p. 1; n. 26 on PDF p. 10 (Restatement cited "(2006)"; Kolt: "First, the Restatement qualifies its position using the words 'at present' ... Second, the Restatement cites only one article in support"); loyalty quotation PDF p. 25. All exact. The facet's "p. 8" is where the sentence recurs in the introduction, not the abstract. Crossref's only match is the SSRN record 10.2139/ssrn.4772956 (issued 2024), whereas the bib gives 2025; the PDF footer date 11 Feb 2025 is the version read. | none |
| M3-24 | 100-109 | UK CRA 2015 s. 62(1) "An unfair term of a consumer contract is not binding on the consumer."; s. 62(4) "if, contrary to the requirement of good faith, it causes a significant imbalance in the parties' rights and obligations under the contract to the detriment of the consumer"; s. 68(1)-(2) "must ensure that a written term of a consumer contract, or a consumer notice in writing, is transparent"; "expressed in plain and intelligible language and it is legible" | CONFIRMED | legislation.gov.uk/ukpga/2015/15/section/62 and /68, fetched this session. Exact. Note s. 62(3): the consumer may still rely on an unfair term if they choose; s. 68 in force 1 Oct 2015. | none |
| M3-25 | 111 | 12 C.F.R. § 1002.9(a)(2): "shall be in writing" and "either: (i) A statement of specific reasons for the action taken; or (ii) A disclosure of the applicant's right to a statement of specific reasons within 30 days" | CONFIRMED | Saved eCFR text: exact. The 30 days run from a request made within 60 days of the creditor's notification, which the facet omits. | none |
| M3-26 | 157-159 | Balkin (2016) 49 U.C. Davis L. Rev. 1183: p. 1209 definition; p. 1232 "does not change if a company uses algorithms ..."; p. 1233 "we can no longer rely on the notion of special fiduciary relationships between individuals and companies" | CONFIRMED | Yale repository PDF page by page: definition on 1209 (PDF p. 27); "analysis I have just offered" on 1232 (PDF p. 50); "no longer rely" on 1233 (PDF p. 51). Exact. | none |
| M3-27 | 169-172 | Citron (2008) 85 Wash. U. L. Rev. 1249: p. 1253 "Some systems adjudicate in secret, while others lack recordkeeping audit trails ..."; p. 1305 "At a minimum, automated systems should generate audit trails that record the facts and rules supporting their decisions." | CONFIRMED | WashU PDF: PDF p. 5 (1253) and PDF p. 57 (1305). Exact. | none |
| M3-28 | 173-176 | Viljoen (2021) 131 Yale L.J. 573: p. 573 "Individualist data-subject rights cannot represent, let alone address, these population-level effects"; p. 607 vertical relation "between an individual data subject and an individual data collector"; horizontal "relates data subjects not to data collectors, but to one another" | CONFIRMED | Yale PDF: p. 573 abstract and p. 607 (PDF p. 35). Exact (source "effects" prints with a ligature). | none |
| M3-29 | 181-183 | Gal and Elkin-Koren (2017) 30 Harv. J.L. & Tech. 309, p. 339 "Does the algorithm act as an agent for the consumer? Does it have fiduciary duties towards the consumer?" | CONFIRMED | JOLT PDF p. 339. Exact. | none |
| M3-30 | 213-222 (Q2 table) | Scott: "creates such a system through its ability to give its categories the force of law"; Weber "knowledge of the files" (G&M 197, 214) | CONFIRMED | Scott introduction (saved `scott.txt`): "Thus a state cadastral map created to designate taxable property-holders does not merely describe a system of land tenure; it creates such a system through its ability to give its categories the force of law." Weber (G&M): "Precision, speed, unambiguity, knowledge of the files, continuity ..." and "The management of the modern office is based upon written documents ('the files')". G&M page numbers not checked. | none |
| M3-31 | 223 (table) | Smith (1978): text "carries instructions for its interpretation and for the authorization of its facticity" | CONFIRMED | Crossref abstract of DOI 10.1177/003803857801200103: "The text is found to provide instructions for its interpretation and for the authorization of its facticity." | none |
| M3-32 | 203-205 | Stovel and Shaw (2012) abstract: brokerage "ease[s] social interaction ... breeds exploitation"; Obstfeld (2005) tertius iungens vs gaudens; Gillespie (2010) abstract | CONFIRMED | Crossref abstracts for 10.1146/annurev-soc-081309-150054 (38(1): 139-158), 10.2189/asqu.2005.50.1.100 (50(1): 100-130; "an engineering division of an automotive manufacturer") and 10.1177/1461444809342738 (12(3): 347-364; "seek protection for facilitating user expression, yet also seek limited liability for what those users say"). | none |
| M3-33 | bib | Resolve 29 DOIs at Crossref; compare title, year, venue | CONFIRMED | 29 resolved (gillespie, bakos2014, obar, kessler, rakoff [1983, Harv. L. Rev. 96: 1173], radin2013, kim2013, messick, salomon, rappaport, justice, kamberelis, papen, scott1998, kafka, hull, gitelman, bowker, goody, smith1978, riles, stovel, obstfeld, burt2004, burt2005, quintane, cohen, vandijck, delacroix). No title, year or venue mismatch beyond: Crossref omits subtitles for book records (not a mismatch); `scott1998seeing` DOI resolves to a record issued 2017 (the Yale e-book reprint) while the bib gives 1998 (first edition; acceptable, but the DOI is not the 1998 edition); Messick is titled "Calligraphic State" in Crossref. Non-DOI entries checked against running heads: Balkin 49:1183, Khan and Pozen 133:497-541, Viljoen 131:573, Gal 30:309, Citron 85:1249, Ben-Shahar 159:647, Bakos NET #09-04. | none |
| M3-34 | 145; 153 | Radin (2016) working paper abstract; Obar and Oeldorf-Hirsch (record only); Kessler, Rakoff, Kim, Rama etc. (record only) | UNVERIFIABLE | Not opened by the facet or by me; Crossref confirms existence and venue for those with DOIs (M3-33). Radin 2016 abstract and the Michigan repository page not re-fetched. | none |
| M3-35 | 223 | Heller (2020 SCC 16) "is reported to have held an Uber arbitration clause unconscionable" | UNVERIFIABLE | I did not open the judgment (SCC and CanLII bot walls reported by the facet; not re-tried). The facet hedges it. | none |

### Corrections

#### M3_intermediaries_records.md

C1. Line 15 (M3-4).
Old: `The court considered a read-aloud rule and rejected it as useless for mass transactions.`
New: `The court did not consider a rule that a third party read the contract to the signer; it said of a seller's staff reciting terms to buyers by telephone that "the droning voice would anesthetize rather than enlighten many potential buyers", and that vendors do better to "skip costly and ineffectual steps such as telephonic recitation".`

C2. Line 117 (M3-4).
Old: `This court looked at exactly that safeguard in a modern setting and called it useless for mass sales.`
New: `This court looked at a neighbouring step, a seller's staff reading the terms aloud to a buyer, and called such recitation "costly and ineffectual" for mass sales, in passing, in support of an approve-or-return device. The buyers could read and the reader would have been the counterparty, so the opinion does not address a neutral third party reading to a signer who cannot read.`

C3. Line 117 (M3-4).
Old: `The paper must concede that a court has judged and rejected the read-aloud analogue`
New: `The paper must concede that a court has said, in passing, that oral recitation of terms by the seller is ineffectual for mass sales`

C4. Line 311 (M3-4).
Old: `**Hill** forces a concession that a modern court has weighed reading-aloud for mass transactions and rejected it.`
New: `**Hill** forces a concession that a modern court has said, in passing, that a seller's oral recitation of terms is ineffectual for mass transactions; its holding is that competent adults are bound by terms they did not read.`

C5. Line 126 (M3-8, M3-9), pin cites (an addition, source text unchanged). Two replacements.
Old: `- "When products are 'free'`
New: `- (306 F.3d at 32) "When products are 'free'`
Old: `The opinion quotes California law:`
New: `The opinion quotes California law (306 F.3d at 30):`

C6. Line 134 (M3-11).
Old: `A search snippet reported different sample figures for the published article (48,154 visitors, 90 companies); I did not open it, so check before citing numbers.`
New: `The published JLS abstract (OpenAlex record for DOI 10.1086/674424) gives 48,154 monthly visitors to the sites of 90 online software companies and says "only one or two of every 1,000 retail software shoppers access the license agreement". The "0.1 or 0.2 percent" sentence is from the 2009 working paper; I could not open the JLS full text, so cite that figure to the working paper and the "one or two in 1,000" wording to the JLS version.`

C7. Line 190 (M3-15).
Old: `Both pages at uinl.org opened.`
New: `Both pages at uinl.org opened. The ethics page ends "Approved by the General Meeting of Member Chambers of Notaries of the UINL, Mexico City, Mexico - 17th October 2004", so the ethics principles are 2004 (Mexico City); only the function principles are 8 November 2005 (Rome).`

C8. Line 17 (M3-15).
Old: `(UINL 2005)`
New: `(UINL, notarial ethics 2004, principle 9: "both parties"; notarial function 2005, Part I: "inferiority")`

C9. Line 293, ranked-list row 2 (M3-15).
Old: `| 2 | UINL, Principles of the notarial function (2005) and ethics |`
New: `| 2 | UINL, Principles of the notarial function (2005) and Principles of notarial ethics (2004) |`

C10. Line 69 (M3-18).
Old: `the "textual erasure of oral pacts" is not the only arrangement writing has produced`
New: `giving the document priority over the witness is not the only arrangement writing has produced`

C11. Line 163 (M3-20).
Old: `The Harvard Law Review PDF I downloaded is a **10-page excerpt** (abstract, introduction, the start of Part I, footnotes).`
New: `The Harvard Law Review PDF at the cited URL is the full 45-page article (pp. 497-541); I read pp. 498 and 502-504 and did not read Parts II-V.`

C12. Line 29 (M3-20).
Old: `the PDF is a 10-page excerpt |`
New: `the PDF is the full 45-page article |`

C13. Line 333 (M3-20).
Old: `- **Khan and Pozen, Parts II–IV.** The Harvard Law Review PDF was a 10-page excerpt. Full text at the Harvard Law Review print page or a library.`
New: `- **Khan and Pozen, Parts II-V.** Not read; the Harvard Law Review PDF at the bib URL is the full article (45 pages), so read Part II.A (pp. 508-510, "Managing Divided Loyalties") before relying on the claim that no source treats divided loyalties.`

C14. Line 167 (M3-22).
Old: `I did not read Parts II–IV, where they map conflict rules onto Balkin's proposal.`
New: `Part II.A (pp. 508-510), which I did not read, maps four ways to reconcile duties to stockholders with duties to users and says "Balkin has never squarely addressed the issue of crosscutting loyalties" (p. 508); the conflict it treats is stockholders against users, so the inference to a duty of impartiality between two users is mine, not theirs.`

#### M3_intermediaries_records.bib

C15. `khan2019skeptical` note (M3-20).
Old: `The PDF at this URL is a 10-page excerpt (abstract, introduction, start of Part I, footnotes); text opened, read in part: pp. 498, 502-504. Parts II-IV not read.`
New: `The PDF at this URL is the full 45-page article (pp. 497-541; re-fetched 2026-10-13); read in part: pp. 498, 502-504. Parts II-V not read by the facet.`

C16. `uinl2005ethics` note (M3-15). Also the entry has no `year` field and its key says 2005; the ethics text is 2004 (add `year = {2004}` and rename the key `uinl2004ethics`, updating the .md references on lines 190 and 193).
Old: `Date not shown on the page opened.`
New: `Approved by the General Meeting of Member Chambers of Notaries of the UINL, Mexico City, 17 October 2004 (stated at the foot of the page).`

### Over-read and under-read

Over-read:
1. Hill (C1-C4). The facet's headline ("a court considered a read-aloud rule and rejected it") is the strongest overstatement in the file and the lead will carry it into the outline as the first thing the paper must concede. What the court says is a single aside about seller staff reciting terms to buyers; the holding is that terms inside the box bind. It is still a fair challenge to the premise that "reading before binding" is a workable safeguard at scale, but it does not touch the notary-style reader for a non-reader.
2. Khan and Pozen (C14). "Neither Balkin's information fiduciary nor Khan and Pozen's critique reaches a duty to two principals" is right as to two users; Khan and Pozen do discuss divided loyalties (stockholders and users, Part II.A), and the facet had not read that part, so "cuts against a fiduciary route" rests on pp. 502-504 only.
3. Messick (C10). The facet sets Messick as a regime where "testimony outranks the document". Messick himself says the doctrine centred on oral testimony while the court "in actuality relied heavily on the services of the written word" (p. 209); the facet records this caution once, but the ranked list and cut-against list (iii: "forces §3.3 to state record-over-voice as a legal choice") drop it.
4. Walker-Thomas. "The test names 'education or lack of it'" is exact, but the passage is one factor in deciding whether there was a meaningful choice, framed as what the manner of contracting shows; the facet's own note that it is a substantive, after-the-fact test is right. The court also remanded for findings on unconscionability (it did not hold the contracts unconscionable) and Danaher dissented; the facet mentions neither.

Under-read:
1. Khan and Pozen Part II.A and Part V (pp. 508-510, 538-540) are in the saved file and bear on §6.4 (divided loyalties; structural remedies as an alternative to fiduciary duties).
2. The Bakos et al. published abstract is available and matches the facet's snippet; "0.1 to 0.2 percent" belongs to the working paper, and a footnote should say so when it is carried into the paper.
3. The UINL ethics principles are 2004, not 2005 (C7-C9, C16); the "weaker party" text is in the 2005 function document and the "both parties" text in the 2004 ethics document, so any single "UINL 2005" cite is wrong for one of the two claims.
4. Specht pin cites are available from the star-paged excerpt (C5).

### Counts (M3 .md and .bib together)

Rows: 35. CONFIRMED 29 (including M3-11 and M3-22, which carry a completion or qualification). WRONG 4 (M3-4, M3-15, M3-18, M3-20). UNVERIFIABLE 2 (M3-34, M3-35). That is 35 total; 29 + 4 + 2 = 35. Sixteen corrections (C1-C16). DOIs resolved: 29 of the 29 in the bib; zero title or year mismatches (two notes in M3-33).

### Not checkable, and why

- Hill: no second full-text host (Justia, openjurist, casetext returned a bot wall or 4xx; CourtListener opinion HTML returned a stub; law.resource.org 404). The Harvard Cyberlaw copy has no reporter pagination, so no pin cites for Hill or Walker-Thomas beyond the facet's none.
- Bakos et al. JLS 43(1) full text (publisher bot wall): whether the body states "0.1 or 0.2 percent".
- Ben-Shahar and Schneider: the saved copy is the facet's font-decoded text of an Institute for Free Speech PDF; I found no independent PDF (Penn Law repository page had no file link).
- Radin (2016), Obar and Oeldorf-Hirsch, Kessler, Rakoff, Kim, Rama, Rappaport and Cummins, Salomon and Niño-Murcia, Justice, Kalman, Vismann, Kafka, Hull, Gitelman, Bowker and Star, Goody, Riles, Cohen, van Dijck, Delacroix and Lawrence: not opened; existence confirmed by Crossref where a DOI exists.
- Uber v. Heller (2020 SCC 16), Nguyen, Meyer, Berman, L'Estrange, Marvco: not opened.
- Weber G&M page numbers (197, 214) and Messick's exact printed page for the "do not consider documents to be potential evidence" sentence (p. 209 or 210) not individually confirmed.
- Every e-mail address check: no address appears in `M3_intermediaries_records.md` or `.bib`.

---

# Facet M4

Sources I opened this session: the saved PDFs/text in `pdfs/M4/` (pdftotext only) for Walzer, Anderson, Fricker 2010, Symons and Alvarado, Muldoon and Raekstad, Giesler and Veresiu, McKeown, Guljar, Creel and Hellman, Lazar, Green, Mittelstadt, Winner (three copies), SEP republicanism, SEP capability approach, SEP critical theory, IEP epistemic injustice, Kay et al., Nissenbaum; page-by-page `pdftotext -f n -l n` to fix locators. Hoeksema: re-fetched from the PMC full-text page (PMC10007650) into `pdfs/audit5/M4/hoek.html` (HTTP 200). Jobin et al.: arXiv 1906.11668 into `pdfs/audit5/M4/jobin.pdf`. Crossref queried for 46 of the bib's DOIs (all entries that carry a DOI except a few that only returned 429 and were retried: Dotson 2012 resolved on retry). No e-mail address appears in either M4 file (grep for address patterns and `mailto`: none).

Page maps: Walzer Tanner PDF prints the folio at the top of the page (text after "34 / The Tanner Lectures" is p. 34). Anderson: running head "319" opens p. 319. Fricker 2010 author copy: folio at foot, 20 PDF pages. Muldoon and Raekstad: PDF n = printed 586 + n (pdf 8 = p. 594). Symons and Alvarado preprint: folio at foot, PDF n = page n. Giesler and Veresiu: PDF 1 = p. 840 (folio at foot), PDF 2 = p. 841, PDF 12 = p. 851, PDF 13 = p. 852. McKeown accepted MS: PDF n = page n. Creel and Hellman: PDF 2 = p. 27. Green: PDF 4 = p. 212.

| # | location (lines) | claim as written | verdict | what I opened; locator and what the source says | correction |
|---|---|---|---|---|---|
| M4-1 | 138, 197 (ranked 5) | Walzer p. 42: "The same men and women who act badly create and sustain the standards by which (at least sometimes) they know themselves to act badly" | CONFIRMED | Walzer, Tanner PDF, p. 42 (folio "42" precedes the page; the sentence closes the paragraph before section 3). Exact. | none |
| M4-2 | 138 | pp. 33-34: "the local judge, the connected critic, who earns his authority, or fails to do so, by arguing with his fellows" (pp. 33-34); "Social criticism ... is an internal argument" (p. 34); "are standards available to him that are internal to the practices and understandings of his own society, and at the same time properly critical?" (p. 34) | CONFIRMED | First phrase on p. 33 running over to p. 34; "internal argument" and the question on p. 34. Exact (the facet's ellipsis omits "for such people,"). Delivered Nov 13-14 1985 per the volume's own front matter. | none |
| M4-3 | 223 (cut against) | Walzer: criticism that stays inside a culture presses only on its own commitments; "connected critic" hypocrisy/distance worry applies | CONFIRMED (qualified) | p. 34 poses both worries ("Does his connection leave room enough for critical distance?"); p. 43 raises "his hatred for the hypocrisy of his fellows may well outmeasure hypocrisy itself". Walzer answers both in the same lecture, so "would force the paper to concede" is the facet's gloss, not Walzer's concession. | none |
| M4-4 | 90, 198 (ranked 6) | Anderson p. 319: "To be capable of standing as an equal in civil society requires literacy" | CONFIRMED (qualified) | Anderson 1999, p. 319, exact. The next sentences: "But in the U.S. context, it does not require literacy in any language other than English ... In other countries, multilingual literacy might be required for equal standing." The sentence is about sufficiency of capabilities, and the level is context-relative. | C5 |
| M4-5 | 90 | Anderson p. 288 "to end oppression, which by definition is socially imposed"; p. 315 "Equals are not dominated by others; they do not live at the mercy of others' wills" | CONFIRMED | pp. 288 and 315, exact. | none |
| M4-6 | 198, 90 | Anderson supplies "gating as oppression"; "gating it is a relation of inequality" | CONFIRMED (qualified; over-read) | I searched the text of pp. 287-319: Anderson does not discuss gating or any test for literacy. The link is the facet's inference from p. 288 plus p. 319. | C4, C5 |
| M4-7 | 122 (ranked 4) | Fricker 2010 abstract/p. 1: relativism of distance "unconvincing, even incoherent; but also that it is detachable from the rest of Williams' moral philosophy"; narrower thesis "when an agent's moral shortcomings by our lights are a matter of their living according to the moral thinking of their day, judgements of blame are out of order" | CONFIRMED | Abstract (author copy p. 1). Exact. | none |
| M4-8 | 123 | p. 2: "moral-epistemic disappointment", directed at "an individual agent whose behaviour we regard as morally lacking, but who was not in a historical or cultural position to think the requisite moral thought" | CONFIRMED | PDF 2, exact. | none |
| M4-9 | 124 | p. 19: availability test, "depending on whether the form of moral thought to which we would hold them was sufficiently available, despite not yet qualifying as routine"; "sufficiently routine in the collective moral repertoire"; "sufficiently close to becoming part of a newly emerging routine"; "one (or five, or ten) schoolboy[s]"; "can only be a matter of judgement" | CONFIRMED | PDF 19 (folio 19 at foot), all exact. | none |
| M4-10 | 125 (ranked 4) | p. 14: Fricker agrees "that non-culpable moral ignorance releases the agent from blame"; Rosen "casts the net of nonculpable ignorance extraordinarily wide"; "if someone wasn't in a cultural-historical position to know any different, then they weren't to know ... If, however, someone (whose thinking is not structurally hampered) deliberates as best they can, but arrives at a bad moral judgement, then they remain blameworthy" | CONFIRMED | PDF 14, exact. Also p. 14 area: structural ignorance "non-culpable" (the facet's cut-against reading of Fricker 2010 is right on the text). | none |
| M4-11 | 130 | Fricker's text never mentions Moody-Adams | CONFIRMED | Searched the full text of the author copy for "Moody": no hit. | none |
| M4-12 | 218 (cut against) | Fricker 2010: structural ignorance is non-culpable; "no present standard" rule is a choice; Moody-Adams contested | CONFIRMED | Supported by pp. 14, 19 and abstract (M4-7 to M4-10). The claim that the rule is "a choice" is the facet's inference (Fricker restricts blame, allows disappointment, p. 2). | none |
| M4-13 | 74, 215 | SEP: "Just because one is better able to cope with arbitrary power, it does not follow that one's domination is any less" | CONFIRMED | SEP "Republicanism", section 2.2 (revision 12 Aug 2026), exact. It is said of a slave who learns a master's behaviour, so "predictability does not end domination" is a fair reading. | none |
| M4-14 | 75 | procedural account: "to the extent that it is reliably controlled by effective rules, procedures, or goals that are common knowledge to all persons or groups concerned"; democratic: "to the extent that it is directly or indirectly controlled by the concerned persons or groups themselves" | CONFIRMED | SEP section 2.2, exact. The SEP adds that on the procedural view constraints "must be resilient over a wide range of possible changes", which supports the facet's remark (line 96) that a rule changeable at will does not end domination; the facet does not quote that clause. | none |
| M4-15 | 76, 189(b) | arbitrary power "should not be defined along substantive lines as power that is unjust or illegitimate" | CONFIRMED | SEP section 2.2, exact ("arbitrary or uncontrolled power should not be defined along substantive lines as power that is unjust or illegitimate"); SEP also says arbitrariness "simply means uncontrolled and vice versa". | none |
| M4-16 | 72 | Pettit: no one has "the capacity to interfere in their affairs on an arbitrary basis" (Pettit 1999, 165, as quoted) | CONFIRMED | SEP section 1, exact, cited "1999, 165". | none |
| M4-17 | 78 | employers' power an established concern; "stronger unions and workplace democracy" | CONFIRMED | SEP section on workplaces: "many advocate stronger unions and workplace democracy (Gourevitch 2015)". | none |
| M4-18 | 96 | declared envelopes supply the procedural test but "a declared rule the powerful can change at will does not end domination" | CONFIRMED (qualified) | The second half is the facet's inference; compatible with the SEP's "resilient" clause (M4-14). | none |
| M4-19 | 80 | Muldoon and Raekstad p. 596: drivers told the passenger's rating "but they were not informed about the passenger's destination" | CONFIRMED | PDF 10 = p. 596. Source: "the driver was told the passenger's average rating from previous trips, but they were not informed about the passenger's destination". Facet's "rating" is a fair compression. | none |
| M4-20 | 80 | p. 596: the asymmetries "decrease workers' ability both to understand and contest the decisions that are made over them" | WRONG (inflection inside quotation marks) | PDF 10 = p. 596: "Each of these three information and computational asymmetries effectively decreases workers' ability both to understand and contest the decisions that are made over them". | C3 |
| M4-21 | 80, 92 | p. 599: "Workers have had their accounts deleted by an algorithm without warning and with no right to contest the decision" | CONFIRMED | PDF 13 = p. 599, exact. | none |
| M4-22 | 80 | "owners and managers" as a "group agent" of domination; "remain agnostic about the broader question of whether only agents can dominate" (p. 594) | CONFIRMED | PDF 8 = p. 594, exact (both). | none |
| M4-23 | 189(a), 99 | republican non-domination works "without a collective agent"; "Domination needs a dominator" (cost 4) | CONFIRMED (qualified; over-read) | Muldoon and Raekstad (p. 594) themselves use a "group agent of domination" and say they "remain agnostic about the broader question of whether only agents can dominate (and not impersonal systems or ideologies)". So the item they would support is not "needs a dominator". Line 189(a) and line 99 pull in opposite directions. | C1, C2 |
| M4-24 | 82 | Hoeksema abstract: "republicans ought to give priority to structural elements"; "a more structural response to digital platforms over more direct and individualised forms of control ... such as securing exit options and requiring user consent" | CONFIRMED | PMC10007650 full text: abstract, exact (the "..." in the facet covers "that fit with a 'standard' republican approach,"). I read the full page, not only six snippets. | none |
| M4-25 | 82 | "domination exists where someone has the capacity to arbitrarily interfere with another" | CONFIRMED | PMC10007650 section "Freedom as Non-Domination": "In Philip Pettit's terms, domination exists where someone has the capacity to arbitrarily interfere with another, or where they have an uncontrolled power to do so". | none |
| M4-26 | 214, 97, 182 | Hoeksema: "Exit and consent are inadequate" | CONFIRMED | Conclusion: "preventing online domination requires more than securing exit options"; section on implications: "republicans cannot rely on the idea of exit options or of rationally consenting citizens". "§6.2 needs a backing duty" is the facet's inference. | none |
| M4-27 | 189, 193 (ranked 1) | Muldoon and Raekstad and Hoeksema "apply" republicanism "to platforms" and Muldoon and Raekstad use Rosenblat and Stark (2016) | CONFIRMED | Muldoon and Raekstad cite Rosenblat and Stark 2016 at pp. 3758, 3762, 3763 (their text); title and abstract confirm ride-hail and delivery platforms. Hoeksema: digital platforms (Google, Facebook, Uber). | none |
| M4-28 | 26 (ranked 3) | Symons and Alvarado preprint p. 17: supervisor wrote to the prison system, "This had no effect on either the process, the score, or on Rodriguez's overall situation"; "The supervisor in direct contact with the inmate was deemed less credible than the algorithmic assessment" | CONFIRMED | Preprint PDF 17, exact. The prisoner "found" a question skewing the COMPAS score ("When Rodriguez thought he found the question seemingly skewing his COMPAS score") and the supervisor "shared his assessment" (same page). | none |
| M4-29 | 26, 27 | p. 15 "when one is automatically considered a lesser knower vis-à-vis the tools themselves, one suffers a testimonial epistemic harm"; p. 10 "it is not a necessary condition for epistemic injustice that it results from malicious intent" and "should be distinguished from instances of deliberate, manipulative malice" | CONFIRMED | PDF 15 and PDF 10, exact (the facet's ellipsis joins two sentences). | none |
| M4-30 | 22, 29 | p. 10 testimonial injustice "incorrectly judged an unreliable source of testimony ... in virtue of his social position"; p. 15 hermeneutical definition; p. 13 "without epistemic recourse"; p. 14 "closed to recourse" (quoting Kitchin 2014) | CONFIRMED | PDF 10, 15, 13, 14, exact. Source reads "Chris is being incorrectly judged an unreliable source of testimony concerning his family life and finances in virtue of his social position". | none |
| M4-31 | 24 | abstract: data-science technologies diminish "individuals with respect to their standing as knowers or their credibility as sources of testimony" | CONFIRMED | Abstract: "the diminution of individuals with respect to their standing as knowers or their credibility as sources of testimony". | none |
| M4-32 | 167 (ranked 8) | Giesler and Veresiu: the four P.A.C.T. processes "through which responsibility is shifted away from the state and corporations and the responsible consumer subject is shaped" (p. 840) | WRONG (locator) | The sentence is on PDF 2 = p. 841 (folio 841 at foot of that page). Page 840 holds the title block and the abstract, which names P.A.C.T. but lacks this sentence. | C6 |
| M4-33 | 167 | p. 852: "the ethos of financial literacy, with its emphasis on values such as self-control, modesty, economic efficiency, and hard work, justifies the inequality of situations" | CONFIRMED | PDF 13 = p. 852, exact. | none |
| M4-34 | 167 | "financially literate consumer" introduced at p. 851; one of four cases; WEF study | CONFIRMED | PDF 12 = p. 851 heading "Fighting Financial Debt: The Cultivation of the Financially Literate Consumer"; "A fourth responsible-consumer type cultivated at the WEF is the financially literate consumer"; abstract lists four types. | none |
| M4-35 | 221 | Giesler and Veresiu: "individualisation of responsibility through literacy is already documented for finance" | CONFIRMED | Same p. 852 passage and p. 851 section. The article's subject is consumer responsibilization generally, with financial literacy one of four types. | none |
| M4-36 | 55 | McKeown p. 2: liability model "is backward-looking and isolating, seeking to attribute blame or liability to particular agents for harm that has already occurred"; "mere connection to structural injustice generates a nonblameworthy, shared and forward-looking political responsibility to collectively undermine the injustice" | CONFIRMED | PDF 2, exact. | none |
| M4-37 | 55 | p. 13: "Agents with power, privilege, interest or collective ability in relation to a particular structural injustice ought to focus their attention there" | CONFIRMED | PDF 13, exact. | none |
| M4-38 | 63 | the exploited "can be called to a responsibility they share with others" (McKeown p. 12, quoting Young) | WRONG (locator) | The quotation is on PDF 13 = p. 13, in the paragraph on victim-blaming ("the victims along with all the other participants in the processes 'can be called to a responsibility they share with others in the structures ...'"). It is absent from PDF 12. | C7 |
| M4-39 | 55 | McKeown's own claim is that "connection" means individuals "reproduce the background conditions in which they act" (abstract) | WRONG (locator) | The abstract (PDF 1) says "individuals reproduce structural injustice through their actions". The words "reproduce the background conditions in which they act" are in the body, p. 2 ("The most appropriate and consistent way to understand connection to structural injustice is that individuals reproduce the background conditions in which they act"). | C8 |
| M4-40 | 53 | Young 2006 abstract: "all agents who contribute by their actions to the structural processes that produce injustice have responsibilities to work to remedy these injustices"; five features "it does not isolate perpetrators; ... it can be discharged only through collective action" | CONFIRMED | Crossref abstract for 10.1017/s0265052506060043, exact. | none |
| M4-41 | 57 | Guljar quotes Young (2011, 186): "The liability model is the appropriate model ... The social connection model is the appropriate model for assigning responsibility for structural injustice" (Guljar p. 98); names Barry and Ferracioli (2013) | CONFIRMED | Guljar text: the quotation straddles the page break (running head "98 Reimagining Justice Beyond Blame" inside it), so pp. 97-98; Barry and Ferracioli (2013, 251) named as the indeterminacy critics. | none |
| M4-42 | 86 (ranked 9) | Creel and Hellman p. 27: "isolated arbitrary decisions are not of moral concern except when other rights make nonarbitrariness relevant"; "the problem with arbitrary algorithms is not fundamentally their arbitrariness but the systematicity of their arbitrariness"; "Automated decision-making systems that make uniform judgments across broad swathes of a sector" | CONFIRMED | PDF 2 = p. 27, exact. | none |
| M4-43 | 86, 98, 216 (cut against) | Creel and Hellman: "An isolated arbitrary decision is not a wrong as such; the sector-wide exclusion is" | CONFIRMED (qualified; over-read) | The line-86 quotations are exact, but lines 98 and 216 drop the exception "except when other rights make nonarbitrariness relevant", which is the very point that reconciles the registrar (voting is a right) with the hiring cell. Their wording for the sector-wide case is that such systems "limit people's opportunities in ways that are morally troubling", not that they are "the wrong". Their "arbitrary" is the sense of purple-shoelace criteria, not the republican sense. | C9, C10 |
| M4-44 | 88 (ranked 11) | Lazar: "standards of procedural legitimacy and proper authority"; "reasonably competent members of the governed community must be able to determine that they are being governed legitimately and with proper authority"; "can be satisfied only if the powerful can explain their decision-making" | CONFIRMED | arXiv text of the introduction, all three exact. | none |
| M4-45 | 151 (ranked 7) | Green: "vague and toothless, has a myopic focus on individual engineers and technology design, and is subsumed into corporate logics" (abstract); p. 213 "individual engineers typically have little power to shift corporate strategy"; p. 212 "ethics oversight boards and ethics principles lack the authority to veto projects or require certain behaviors" | CONFIRMED | PDF 4 = p. 212 (veto sentence), PDF 5 = p. 213 (engineers sentence), abstract exact. | none |
| M4-46 | 153 (ranked 7) | Mittelstadt: AI development lacks "(1) common aims and fiduciary duties, (2) professional history and norms, (3) proven methods to translate principles into practice, and (4) robust legal and professional accountability mechanisms"; "users cannot trust that developers will act in their best interests" | CONFIRMED | arXiv text, all strings present; the four items appear in the abstract. | none |
| M4-47 | 149 (ranked 10) | Winner: "to recognize the political dimensions in the shapes of technology does not require that we look for conscious conspiracies or malicious intentions"; disabled-access example "arose more from long-standing neglect than from anyone's active intention. But once the issue was brought to public attention, it became evident that justice required a remedy"; "settling an issue in the affairs of a particular community" | CONFIRMED | 1986 reprint copies (two of three saved files readable; the third has an unusable text layer, as the facet says). Exact. | none |
| M4-48 | 22, 44, 219 | IEP: Fricker calls hermeneutical injustice "purely structural" (Fricker 2007, 159, as quoted); wrong done "to someone specifically in their capacity as a knower" | CONFIRMED | IEP "Epistemic Injustice": "In the case of hermeneutical injustice, there is no agent; it is, as Fricker notes 'purely structural' (2007,159)". The "no agent" is the IEP's gloss. Facet marks it second-hand. | none |
| M4-49 | 37, 45 | IEP reports Medina's point that credibility excess is a related harm | CONFIRMED | IEP concluding section: "Many commentators have stressed the need to recognize instances of credibility excess ... (Davis 2016; Medina 2011)". | none |
| M4-50 | 108 (ranked 12) | Robeyns and Byskov SEP: capabilities "the doings and beings that people can achieve if they so choose"; functionings "capabilities that have been realized"; literacy example; conversion factors incl. "reading skills" and "public policies, social and cultural norms, practices that discriminate, societal hierarchies, or power relations ..."; Nussbaum ten capabilities with "senses, imagination and thought" (Nussbaum 2006: 76-78) | CONFIRMED | SEP capability-approach text, all strings present; "(Nussbaum 2006: 76-78)" appears with an en dash. | none |
| M4-51 | 139 (ranked 5) | Celikates and Flynn: internal critique "standards and standpoints that are already recognized by those criticized"; immanent critique "secure[s] its normative resources ... from the (often implicit) normative structures and epistemic possibilities of the practices and self-understandings"; credits Jaeggi | CONFIRMED | SEP Critical Theory section 2.1, exact. | none |
| M4-52 | 33 | Kay et al.: "Testimonial injustice can arise when algorithms are prioritized over human credibility ... hermeneutical injustices can occur when algorithms independently construct meanings and interpretive frameworks"; term "algorithmic epistemic injustice" coined by Byrnes and Spear (2023); Hull; Pozzi "automated hermeneutical appropriation" | CONFIRMED | Both quotations exact; Kay et al. say "a term coined by Byrnes and Spear (2023)" and attribute "automated hermeneutical appropriation" to Pozzi (2023). The facet's "credits ... did not verify" is accurate. | none |
| M4-53 | 101, 222 (cut against) | Oppegaard (2026): Oslo drivers find the algorithm "opaque, unpredictable, and non-negotiable" but "do not experience it as control, partly because they can work for several platforms"; "known only from a search snippet" | CONFIRMED (qualified) | Crossref abstract (DOI 10.1177/0143831x261437378, issued 2026-04-08): "although the algorithmic management is opaque, unpredictable, and non-negotiable, the drivers nonetheless highlight their flexibility and do not necessarily experience it as control"; reason one is "access to multiple platforms". The abstract also calls the management "a non-interventionist form of control". So the facet's claim is right but stronger ("do not") than the source ("do not necessarily"), and the work is readable at abstract depth, not snippet-only. | C11, C12 |
| M4-54 | 178 | Jobin et al.: "60 of 84 sets" profess non-maleficence | CONFIRMED | Jobin, Ienca and Vayena, arXiv 1906.11668, Table 2: "Non-maleficence 60/84". | none |
| M4-55 | 163 | Nissenbaum builds on Walzer's "spheres of justice" per her abstract | CONFIRMED | Abstract: "Building on the idea of 'spheres of justice,' developed by political philosopher Michael Walzer". | none |
| M4-56 | 35, 37, 84, 155, 157, 169 | Abstract quotations: Pozzi ("can be captured through the lenses of Miranda Fricker's account of hermeneutical injustice"), Dotson 2011 ("the failure, owing to pernicious ignorance, ..."), Maas ("neo-republican moral wrong of domination"; "increase contestability through design-for-values approaches"), Santoni de Sio and Mecacci ("at least four interconnected problems"), Rességuier and Rodrigues ("Using ethics as a substitute for law risks its abuse and misuse"), Maniates ("little room to ponder institutions ...") | CONFIRMED | Crossref abstract fields for each DOI contain each string. Not tested: Bietti, Shamir, Tsosie, Rosen, Nussbaum 2003, Robeyns 2005 (no abstract in Crossref). | none |
| M4-57 | bib, 58 entries | DOIs resolve to the stated work: title, year, venue, volume, issue, pages | CONFIRMED | 46 DOIs resolved at Crossref (all entries with a DOI; Dotson 2012 first returned 429, resolved on retry). Titles match (subtitle omitted by Crossref for Fricker 2007, Pettit 1997, 2012, Nussbaum 2000, Anderson 2017, Miller, Scanlon, Arpaly, Friedman and Hendry). Volume/issue/pages checked against Crossref for Fricker 2010 (84(1), 151-177), McKeown (49(3), 484-502), Mittelstadt (1(11), 501-507), Anderson (109(2), 287-337), Creel and Hellman (52(1), 26-43), Green (2(3), 209-225), Hoeksema (36(1)), Symons and Alvarado (200(2)), Gädeke (28(2), 199-221). Year differences only where Crossref uses the online date: Pettit 1997 (book 1997; Crossref 1999), Medina 2011 (2010), Gädeke (2019), Muldoon and Raekstad (2022), Maas (2022). No title mismatch. The Fricker 2010 bib note says "19 pp."; the author copy has 20 PDF pages, of which the last may be references. | none |
| M4-58 | 189, 237 | Pettit (1997, 2012) "I could not open either book"; "eyeball test" not verified; Fricker 2007 definitions second-hand | UNVERIFIABLE | Facet itself marks these; I did not open them either (books, no open copy). | none |
| M4-59 | 149 | Winner 1980 Daedalus original and pagination | UNVERIFIABLE | Crossref has no record; the three saved copies are the 1986 reprint; I did not fetch the JSTOR original. | none |
| M4-60 | 138, 239 | Walzer's 1987 book (Harvard University Press) and the year 1988 for the Tanner volume | UNVERIFIABLE | The lecture PDF shows "Delivered ... November 13 and 14, 1985" but no volume year; I did not open the book or a catalogue record. | none |

## Corrections for M4

### M4_ethical_frameworks.md

C1. Line 189 (M4-23).
Old: `without needing proof of intent and without a collective agent;`
New: `without needing proof of intent (Muldoon and Raekstad do, however, place the dominator in owners and managers acting as a "group agent of domination", p. 594);`

C2. Line 99 (M4-23).
Old: `*Domination needs a dominator.* Muldoon and Raekstad find the dominators in owners and managers.`
New: `*The sources I read name a dominator.* Muldoon and Raekstad find the dominators in owners and managers, though they "remain agnostic about the broader question of whether only agents can dominate (and not impersonal systems or ideologies)" (p. 594).`

C3. Line 80 (M4-20).
Old: `The asymmetries "decrease workers' ability both to understand and contest the decisions that are made over them" (p. 596).`
New: `Each asymmetry "effectively decreases workers' ability both to understand and contest the decisions that are made over them" (p. 596).`

C4. Line 198 (M4-6).
Old: `Literacy as a condition of equal standing (p. 319); gating as oppression.`
New: `Literacy as a condition of equal standing (p. 319); the gating-as-oppression reading is my inference from p. 288 ("to end oppression, which by definition is socially imposed") and not Anderson's wording.`

C5. Line 90 (M4-4, M4-6).
Old: `literacy is a condition of equal standing, and gating it is a relation of inequality.`
New: `literacy is a condition of equal standing, at a level she makes context-relative ("In other countries, multilingual literacy might be required for equal standing", p. 319); that gating it is a relation of inequality is my inference, not Anderson's wording.`

C6. Line 167 (M4-32).
Old: `and the responsible consumer subject is shaped" (p. 840)`
New: `and the responsible consumer subject is shaped" (p. 841)`

C7. Line 63 (M4-38).
Old: `(McKeown p. 12, quoting Young)`
New: `(McKeown p. 13, quoting Young)`

C8. Line 55 (M4-39).
Old: `"reproduce the background conditions in which they act" (abstract).`
New: `"reproduce the background conditions in which they act" (p. 2; the abstract says "individuals reproduce structural injustice through their actions").`

C9. Line 98 (M4-43).
Old: `Creel and Hellman say a single arbitrary decision does not wrong anyone as such.`
New: `Creel and Hellman say isolated arbitrary decisions "are not of moral concern except when other rights make nonarbitrariness relevant" (p. 27), so a registrar who gates a right such as the vote falls under the exception.`

C10. Line 216 (M4-43).
Old: `An isolated arbitrary decision is not a wrong as such; the sector-wide exclusion is.`
New: `An isolated arbitrary decision is "not of moral concern except when other rights make nonarbitrariness relevant"; the sector-wide exclusion limits "people's opportunities in ways that are morally troubling" (p. 27).`

C11. Line 222 (M4-53).
Old: `Some platform workers do not experience algorithmic management as control.`
New: `Some Oslo taxi drivers "do not necessarily experience it as control" (Crossref abstract), though the author still calls it "a non-interventionist form of control".`

C12. Line 101 (M4-53).
Old: `Record, known only from a search snippet`
New: `Abstract only (Crossref abstract, issued 2026-04-08)`

## Over-read and under-read (M4)

1. Over-read, Anderson (1999). The facet's "gating as oppression" (lines 90, 198) is not in the text. Anderson says nothing about tests or gates, and her p. 319 sentence sits in a passage on sufficiency and says the required literacy depends on the country (C4, C5).
2. Over-read, Creel and Hellman (2022). Lines 98 and 216 drop the exception "except when other rights make nonarbitrariness relevant" (p. 27). With the exception, the facet's worry (that the registrar and the hiring cell sit on different philosophical lines) mostly dissolves: the vote is a right. Their "arbitrary" also means criteria such as purple shoelaces, not Pettit's sense, and their conclusion is "morally troubling", not "the wrong" (C9, C10).
3. Over-read, Muldoon and Raekstad. The facet says republicanism works "without a collective agent" and then that "domination needs a dominator". Muldoon and Raekstad use a group agent and say they stay agnostic on whether impersonal systems dominate; the intermediary-as-dominator question is therefore open in their paper, which helps the triad point (C1, C2).
4. Over-read, Oppegaard: "do not experience" for "do not necessarily experience"; and the work is abstract-readable (C11, C12).
5. Under-read, the SEP: the procedural account demands rules that are "resilient over a wide range of possible changes", the real answer to "declared envelopes" in line 96. The facet reaches the right conclusion without quoting the clause. Worth adding in the lead's outline if §6.3 leans on this.
6. Under-read, Hoeksema: the paper explicitly names Breen (2017) and Gourevitch (2013) for "exit options are not enough" in the workplace, and Rahman on structural domination; Hoeksema is a synthesis, so a referee will want those primary republican sources too. Not in the facet.
7. Walzer cut-against row (line 223) puts the hypocrisy/distance worry as a concession the paper must make; Walzer poses and answers both in the same lecture. The facet should say the worry is Walzer's own and answered by him (p. 34, p. 43).
8. Right and worth keeping: Walzer p. 42 sentence; Fricker 2010 pp. 14, 19 (availability, "can only be a matter of judgement"); Symons and Alvarado p. 17 (supervisor); Muldoon and Raekstad pp. 596, 599 (destination withheld; deactivation "without warning and with no right to contest"); Giesler and Veresiu p. 852 ("ethos of financial literacy"); SEP "not moralised" and "better able to cope". I found no altered quotation among the quotations that the lead will carry; the four WRONG rows are three locators and one verb inflection.

## Counts (M4)

| file | checked | CONFIRMED | WRONG | UNVERIFIABLE |
|---|---|---|---|---|
| M4 `.md` (rows M4-1 to M4-56, M4-58 to M4-60) | 59 | 52 | 4 | 3 |
| M4 `.bib` (row M4-57) | 1 | 1 | 0 | 0 |
| total | 60 | 53 | 4 | 3 |

WRONG rows: M4-20, M4-32, M4-38, M4-39. CONFIRMED (qualified) rows counted as confirmed: M4-3, M4-4, M4-6, M4-18, M4-23, M4-43, M4-53.

## Could not check (M4)

- Pettit (1997, 2012, 1996), Young (2011), Fricker (2007), Anderson (2017), Dotson (2012), Medina (2011, 2013), Hull (2023), Nussbaum (2000), Scanlon, Arpaly, Jaeggi, Matthias, Friedman and Hendry: books or paywalled; I confirmed only Crossref records (and Crossref abstracts where present). The facet says it did not open them either.
- Winner 1980 Daedalus original: no copy; the 1986 reprint text was checked.
- Abstract-level claims for Bietti, Shamir, Tsosie, Rosen, Nussbaum 2003, Robeyns 2005: Crossref carries no abstract; publisher pages not fetched.
- Kay et al. on Hull's "physiognomic systems": not tested.
- Mittelstadt section number "2.1": arXiv text has no numbered section marks I could match; strings confirmed.

---

# Facet M5

Sources opened this session: NBER w8512.pdf (re-fetched, 43 pp.); planalto.gov.br Constituicao de 1891 and 1824 and Decreto 6 of 19 Nov 1889; Leao 2012 (Aedos 4(11)) and Petermann (TSE, Estudos Eleitorais) on Decreto 3.029; press.anu.edu.au ch13s04; bibliotecaliberale.it Ballini entry; eah.anu.edu.au Ye; ewjus.com Moser; hokudai Danylenko; encyclopediaofukraine.com; UC Press e-book of Leonard (ark:/13030/ft1f59n78v); archive.org Parnell, Buhler SBE 25 and SBE 2 (djvu text); roundtableindia.co.in Phule; cdn.sida.se Kater et al.; icwa.org Stansifer; arXiv 2605.29785; lawphil.net 1935 Constitution; Crossref for DOIs. Blocked: sacred-texts.com (Cloudflare bot wall, not circumvented; archive.org scans used instead); Camara dos Deputados and Planalto URLs for Decreto 3.029 returned 404 or an error page. Downloads under ~/iit-playground/berthon_ethics_local/pdfs/audit5/M5/. No e-mail address found in M5 .md or .bib.

## (1) Table

| # | location (M5_wider_cases.md lines) | claim as written | verdict | what I opened; locator and what the source says | correction |
|---|---|---|---|---|---|
| M5-1 | L69; ranked 1 (L274) | E&S: 'introduction and growing emphasis on a literacy requirement was the major change that occurred after independence'; U.S. literacy test only from 1890s | CONFIRMED | Re-fetched NBER w8512.pdf (43 pp.). Printed p. 23, exact, incl. 'Whereas a literacy qualification was not used in the U.S. until the 1890s...'. | none |
| M5-2 | L69, L213 | Country dates: Bolivia 1826 'maintained beyond the 1945 constitution'; Chile 'between 1833 and 1874, and then later from 1885 through 1970'; Ecuador 1861 'until 1978'; Peru 1826 'largely maintained through 1979'; Uruguay 1830 to 1918 | CONFIRMED | Printed pp. 23-24, exact. | none |
| M5-3 | L69 | Brazil 'replaced [property restrictions] with a literacy qualification in 1891; this restriction endured until 1988' | CONFIRMED (as E&S's words) | p. 24 text: 'Brazil, despite a different national heritage, also had property-based restrictions after independence, but replaced them with a literacy qualification in 1891; this restriction endured until 1988.' E&S say it; see Brazil row below for whether it is right. | none |
| M5-4 | L73, L213, L260, L274 | Brazil literacy rule dated 1891 'on this source'; paper's 1881 left 'to be reconciled' | WRONG (as a date of the rule's start) | Planalto, Constituicao de 1891, Art 70 s.1: 'Nao podem alistar-se eleitores... 2) os analfabetos'. Planalto, Decreto 6 of 19 Nov 1889, Art 1: electors are citizens 'que souberem ler e escrever'. Leao 2012 (Aedos 4(11), p. 611, quoting Senado Anais 1881 p. 348) gives Decreto 3.029 of 9 Jan 1881, Art 8 II: citizens who prove the qualities of elector 'e souberem ler e escrever'. Planalto, Constituicao de 1824, Arts 91-94: income test (200 mil reis for electors), no literacy test. So the literacy requirement began 1881; 1891 is the Republic's constitutional re-enactment. Decreto 3.029 itself not reachable (Camara and Planalto URLs 404/error). | C1-C3 |
| M5-5 | L70 | Table 3 note: 'After eliminating wealth and education requirements in 1878, Chile instituted a literacy requirement in 1885'; Table rows Chile 1869 Y 1.6%, 1881 N 3.1%, 1920 Y 4.4%, Ecuador 1888 Y 2.8% | CONFIRMED | Table 3, printed p. 24 and footnote 1, exact. Note: E&S's table and note (1878) differ from its text (1874), and Chile 1.6% to 3.1% is about a doubling. | C4 (qualification) |
| M5-6 | L70, L213, L243-244, L286 | 'after the literacy requirement in Chile was removed by the 1874 constitution (an action reversed in 1885), the proportion of voters in the population more than tripled within a few years' (p. 25) | CONFIRMED (text); qualified | Printed p. 25, exact. The Table 3 Chile rows the facet cites (1.6% in 1869, 3.1% in 1881) do not show a tripling; E&S do not reconcile them. | C4 |
| M5-7 | L69 | 'The only major Latin American countries that did not have literacy requirements at the national level were Argentina and Colombia' (pp. 23-24) | CONFIRMED | p. 24, exact (source has typo 'did not have had'). | none |
| M5-8 | L69 | Ecuador: facet says 'replaced property with literacy in 1861' | CONFIRMED (as E&S's text) | p. 23 text exact. Table 3 has Ecuador 1888 wealth Y, literacy Y, so property was not yet gone in 1888; E&S's own text and table differ. | none (flag in notes) |
| M5-9 | L78, L215 | Lake: Premier March 1897: 'founded on the American Act. But it goes one step further'; target 'perfectly well able to read and write in their own language'; English in the Bill; final Act 'any European language'; NSW law 'reserved'; 'wily Hindoo'; passed 'with few dissenting voices'; Chamberlain 1901 model | CONFIRMED | Re-fetched press.anu.edu.au ch13s04.html, section 'Founded on the American Act', exact (notes [44],[45]). | none |
| M5-10 | L78 | 'The Premier's stated ground for restriction: "We have got a large unenfranchised [Black] population of roughly 500,000..."' | WRONG (attribution) | Same page: 'In promising to limit Indian immigration, the Natal government insisted on...' then the block quotation [note 41]. Lake does not name the Premier as speaker of that passage. | C5 |
| M5-11 | L84-85, L217 | Philippines 1935 Const. Art V s.1 full text | CONFIRMED | lawphil.net/consti/cons1935.html, Art. V s. 1, exact. | none |
| M5-12 | L91, L219 | Ballini: 1882 reform 'indipendentemente dalla loro condizione economica... corso elementare obbligatorio'; electors 621,896 to 2,049,461; 6.9% of residents; 65.3% 'per capacita', 37.1% second grade, 10.7% regimental school | CONFIRMED | Re-fetched bibliotecaliberale.it entry, exact. | none |
| M5-13 | L91 | Entry prints the law as '22 gennaio 1881, n. 593'; facet takes 1882 | UNVERIFIABLE (1882) | The entry does print 1881 (confirmed). I did not open the law (Normattiva/Wikisource not tried); 1882 is not shown by any text I opened. | none |
| M5-14 | L91, L219 | 1912 law: 'whether illiterate men over 30 could then vote: NF' | CONFIRMED (entry silent) but under-read | Same entry gives the 1912-13 laws raising the electorate from 2,930,473 (1909) to 8,443,205, 8.3% to 23.2% of residents; Luzzatti 1910 bill quote 'di saper leggere e di saper trascrivere un brano di stampato' exact; 30 June 1912 n. 665 exact. The entry does not say illiterates were admitted. | C6 |
| M5-15 | L98 | Ye (2003) p. 69: 'The debased people were deprived of many legal rights, of which the most important was participation in the imperial examinations' | CONFIRMED | Re-fetched eah.anu.edu.au EAH25-26_04.pdf; PDF p. 5 = printed p. 69, exact. | none |
| M5-16 | L98, L221 | Ye p. 72: Qianlong 1771 order (fourth generation 'may take part in the examinations if all members of their clan, and all their relatives, remain clean'; 'second and third generation will not allowed...') and 1788 regulation (prostitutes, actors, yamen runners; forfeit degree; beaten one hundred times) | CONFIRMED | PDF p. 8 = printed p. 72, exact (OCR spacing only). | none |
| M5-17 | L98 | Ye pp. 71-72: emperor ordered actor beaten to death: 'You actors belong to the debased class, how dare you ask about official positions?' | CONFIRMED (locator) | Printed p. 72 (PDF p. 8) holds the quotation and the beating. | none |
| M5-18 | L98 | Ye p. 69: Yongzheng abolished jianmin status, reached yuehu not performers | CONFIRMED | PDF p. 5 (p. 69), n. 1 area. | none |
| M5-19 | L139, L225, L276 | Moser p. 3: Valuev directive 30 July (OS 18 July) 1863; quoted wording; 'belles-lettres'; Ems Ukaz 30 (OS 18) May 1876 'an even more rigorous ban'; 'stayed in force until the Russian Revolution of 1905' | CONFIRMED | Re-fetched ewjus.com PDF; exact, printed p. 3. | none |
| M5-20 | L139, L225 | Directive's ground 'a [distinct] Little Russian ... language did not, does not and cannot exist': 'as the censors put it' | WRONG (attribution) | Moser p. 3: 'as the Valuev Directive put it' (Miller 240-41). Synthesis L225 phrase 'the directive's reasoning' is right. | C7 |
| M5-21 | L139 | Moser p. 4: 'Ukrainians were denied'; 'doomed to largely remain a peasant language' | WRONG (locator) | Both are in the first PDF page = printed p. 3. 'no one should be allowed to ban, deny, or impose any language or identity' is p. 4 (correct). | C8 |
| M5-22 | L139, L225 | Moser pp. 5-6 (Remy): 'merely because of their Ukrainian language'; 'corruption of Russian censorship organs'; 'several Russian officials considered dismissing the imperial language bans'; 'gradually eroded before they were repealed' | CONFIRMED | Printed p. 6 (PDF p. 4, running head '6'); pp. 5-6 covers it. | none |
| M5-23 | L142, L225, L276 | Danylenko pp. 1-3: circular text; Remy 1874-76 eighteen publications, seventeen in Kyiv, one corrupt censor; Lemke/Katkov motive; Polish plotters | CONFIRMED | Re-fetched hokudai PDF; exact. | none |
| M5-24 | L147, L225 | Encyclopedia of Ukraine 'Ems Ukase': 30 May 1876; never examined by State Council, never formally revoked; no Ukrainian book in 1877; Drahomanov, Paris 1878; Yuzefovich | CONFIRMED | Re-fetched encyclopediaofukraine.com page, exact. | none |
| M5-25 | L159-160, L229, L277 | Leonard: Queen's instruction to House of Trade 4 April 1531, 'bad practice for the Indians'; 14 July 1536 Mendoza ('not been due care'; 'beginning to be adept in Latin'); 13 Sept 1543 (Prince Philip); 'largely ineffective from the outset' | CONFIRMED | Re-fetched UC Press e-book HTML (ark:/13030/ft1f59n78v); exact text; page marker '83' follows the 1543 order, 'largely ineffective' on p. 83. | none |
| M5-26 | L159-160, L229 | Inquisition tribunals Lima 29 Jan 1570, Mexico 4 Nov 1571; policed 'the official Index' (pp. 167-168) | CONFIRMED (text) | Dates and phrase exact; I did not read page markers for pp. 167-168. | none |
| M5-27 | L153, L227, L278 | Parnell p. 29: act to deprive Catholics 'of the means of educating their children either at home or abroad' (7th W. III c. 4); Burke 'worst species of tyranny' pp. 29-30 | CONFIRMED | Re-fetched archive.org djvu text (long-s OCR); exact; page '30' marker follows. | none |
| M5-28 | L153, L227 | 'a Catholic schoolmaster needed the ordinary's licence and the oath of supremacy' placed beside the 1695 act and cited pp. 29-30 | WRONG (attribution/locator) | Parnell pp. 27-28: item '5th' in a list of laws already in force at the treaty of Limerick, 'taken from the Report of the Committee of the House of Commons, appointed in 1697'. It is not the 1695 act (7 W. III c. 4), and is not on pp. 29-30. | C9 |
| M5-29 | L153 | Parnell p. 121: preamble 'considered as too severe, and have not answered the desired effect'; 21 & 22 Geo. III | CONFIRMED | Printed p. 121 (OCR 'defired efFe(ft'), exact. | none |
| M5-30 | L120, L223 | Manu 2.66: ceremonies for females 'but without (the recitation of) sacred texts' | CONFIRMED | archive.org mlbd.lawsofmanu0025unse_h6b1 (Buhler, SBE 25), p. 42, verse 66 exact. sacred-texts.com returned a Cloudflare bot wall; not used. | none |
| M5-31 | L120, L223 | Manu 2.172 (uninitiated 'should not pronounce (any) Vedic text... on a level with a Sudra before his birth from the Veda'); 4.80 ('Let him not give to a Sudra advice... nor let him explain the sacred law'); 8.272 hot oil mouth and ears | CONFIRMED | Same scan, verse numbers and wording exact. In 2.172 the subject is '(He who has not been initiated)'; in 8.272 the offender is the once-born man of 8.270-272. | none |
| M5-32 | L126, L223 | Gautama XII.4-6: ears filled with molten tin or lac; tongue cut out; body split | CONFIRMED (qualified) | archive.org mlbd.sacredlawsofarya0000gbuh_a4m2 (SBE 2): verses 4-6 exact, running head p. 239. Subject is the Sudra (XII.1 'A Sudra who intentionally reviles...'); the facet does not say so. | C10 |
| M5-33 | L130-132, L223, L280 | Phule deposition: Mahars and Mangs 'practically excluded from all schools owing to caste prejudices'; 'Under the promise of the Queen's Proclamation I beg to urge...'; compulsory to age 12; teachers 'almost all Brahmins'; 'virtual monopoly' | CONFIRMED | Re-fetched roundtableindia.co.in/?p=5296; exact. Source note: 'between pages 140-145 in Education Commission, Bombay, Vol II, Calcutta, 1884'. | none |
| M5-34 | L129, L266 | Phule's date 'unresolved' (1881 header or 1882) | WRONG (unresolved) | Same page, signature block: 'Poona, 19th October 1882. Joteerao Govindrao Phooley'. The 1881 is the page's editorial header. | C11, C12 |
| M5-35 | L190, L235, L243, L282 | Kater et al.: illiteracy 67% (1968) to 9.5% (1986); 13,759,014 sat tests 1975-86, 4,861,912 or 35% 'emerged as neo-literates'; 36% enrolled post-literacy; 'actual participation in programmes is far below the official statistics'; '67% in 1967 to 10% in the late 1980s' | CONFIRMED | Re-fetched cdn.sida.se PDF; exact (OCR). 4,861,912/13,759,014 = 35.3%. | none |
| M5-36 | L243 | Tanzania a counter-case: 'the number was met by the government's own tests' | WRONG (over-read) | Kater §3.3.1: only 35% of test-takers emerged as neo-literates, participation 'far below the official statistics', and a 'mis-match between statistics' is reported. The report does not say the 9.5% figure was met by tests. | C13 |
| M5-37 | L181, L235, L282 | Stansifer: 'Officials claim... 50 to 13 percent'; UNESCO Krupskaya award; 'Even if the figures are exaggerated, as they must be, the crusade certainly did achieve its major goal.' | WRONG (quotation truncated) | icwa.org CLS-1.pdf: sentence continues 'of drastically reducing the Nicaraguan illiteracy rate.' The facet ends the quotation at 'goal' with a full stop inside the marks. | C14 |
| M5-38 | L181 | Stansifer objectives 1,2,5,6; 'Adverse reaction occurred...'; 'tended to resist answering...'; 56 brigadistas died, 7 killed; 'Nonparticipation meant loss of prestige and likely charges of counterrevolutionaryism and somocismo' | CONFIRMED | Exact (icwa.org PDF). | none |
| M5-39 | L185-186 | Sandiford et al. abstract ('about 9 per cent'; women graduates) | UNVERIFIABLE | Abstract not reopened (Oxfam page not fetched). Crossref confirms title, journal, 4(1), 35-49, 1994. | none |
| M5-40 | L195, L235 | Cuba: 707,000 literate, 3.9%, 250,000 brigadistas; pre-revolution 60-76%; 'below 4 percent' from 20-40% | CONFIRMED | Re-fetched arXiv 2605.29785 (45 pp.): Appendix A.8 and s. 2.2 exact. Derivative source; facet says so. | none |
| M5-41 | L243 | Cuba and Tanzania as counter-cases to overselling | WRONG (over-read) | The only Cuba source is a preprint that cites Leiner/Seara Rey and that the facet itself says not to cite; Tanzania see above. | C13 |

Bib DOI rows (M5_wider_cases.bib; the bib carries only 11 distinct DOIs, so 15 could not be reached; all 11 plus the Ayalon chapter DOI were resolved):

| # | entry and DOI | verdict | Crossref result |
|---|---|---|---|
| M5-B1 | engerman2001evolution 10.3386/w8512 | CONFIRMED | Crossref: same title, Engerman/Sokoloff, 2001-10, NBER WP. |
| M5-B2 | engerman2005evolution 10.1017/s0022050705000343 | CONFIRMED | Crossref: JEH 65(4) 891-921, 2005. |
| M5-B3 | lake2006mississippi 10.22459/cw.03.2006 | WRONG | Crossref: title 'Connected Worlds: History in Transnational Perspective', editors Curthoys and Lake, 2006: the DOI is the volume's, not ch. 13's. Bib types it as @incollection with the chapter title. |
| M5-B4 | choi2026lifespans 10.25024/review.2026.29.1.002 | UNVERIFIABLE | Crossref 'Resource not found'; doi.org answered 302. Bib note already says no Crossref record; I did not open the target. |
| M5-B5 | moser2017introduction 10.21226/T2DK9B | CONFIRMED | Crossref: 'Introduction', East/West 4(2), p. 3, 2017. |
| M5-B6 | remy2007valuev 10.1080/00085006.2007.11092432 | CONFIRMED | Crossref: title, Canadian Slavonic Papers 49(1-2) 87-110, 2007. |
| M5-B7 | ayalon2016arabic 10.1017/cbo9781316584521 | CONFIRMED | Crossref (upper-case DOI form; lower-case returned not found): CUP book 2016. Chapter DOI .002 'Introduction', 1-17, 2016, also confirmed. |
| M5-B8 | schwartz2017did 10.1353/bh.2017.0000 | CONFIRMED | Crossref: Book History 20(1) 1-39, 2017. |
| M5-B9 | sandiford1994nicaraguan 10.1080/096145249100077481 | CONFIRMED | Crossref: Development in Practice 4(1) 35-49, 1994; authors Sandiford, Lankshear, Montenegro, Sanchez, Cassel. |
| M5-B10 | tuchscherer2002cherokee 10.2307/3172173 | CONFIRMED | Crossref: History in Africa 29, 427-486, 2002. |
## (2) Corrections

### M5_wider_cases.md

C1. Line 73 (M5-4). Brazil discrepancy.
Old: `this text dates the literacy rule to 1891 (and treats earlier rules as property-based). Facet D holds Brazil from other sources (`aleixo2010analfabetos`); reconcile there.`
New: `this text dates the literacy rule to 1891 (and treats earlier rules as property-based). 1891 is the Republic's constitutional re-enactment, not the start: the first national literacy requirement for enrolment is the Saraiva Law, Decreto 3.029 of 9 January 1881, art. 8, which admits to the roll citizens who prove the elector's qualities "e souberem ler e escrever" (quoted in Leão 2012, Aedos 4(11), p. 611, from Senado, Anais 1881, p. 348); Decreto 6 of 19 November 1889, art. 1, kept it; Constitution of 1891, art. 70 §1 2º bars "os analfabetos" (planalto.gov.br). The Constitution of 1824, arts 91-94, had an income test only. Facet D (F3) is right on 1881.`

C2. Line 213 (M5-4).
Old: `Brazil 1891–1988 on this source.`
New: `Brazil: the 1891 Constitution (to 1988 on this source), but the literacy bar on new enrolment dates from the Saraiva Law of 9 January 1881 (see C1).`

C3. Line 260 (M5-4), claims-in-the-paper item 1.
Old: `1. **Brazil's literacy rule dated to 1881 (§3.1).** Engerman and Sokoloff's working paper says 1891 for the literacy qualification. Facet D holds the Saraiva-law sources; the two dates need reconciling there.`
New: `1. **Brazil's literacy rule dated to 1881 (§3.1).** The paper is right. Engerman and Sokoloff's 1891 is the Republic's constitutional date; Decreto 3.029 of 9 January 1881 (art. 8) first required reading and writing for enrolment, and Decreto 6 of 19 November 1889 (art. 1) repeated it before the 1891 Constitution (art. 70 §1 2º). The 1881 law also tightened income proof, so 1881 is not a literacy-only change (Nicolau, via facet D).`

C4. Line 70 (M5-5, M5-6).
Old: `Table 3 (p. 24) lists, by country and year,`
New: `Table 3 (p. 24; its note dates the abolition of Chile's wealth and education requirements to 1878, the text to 1874; the Chile rows give 1.6% in 1869 and 3.1% in 1881, about a doubling, not "more than tripled") lists, by country and year,`

C5. Line 78 (M5-10).
Old: `The Premier's stated ground for restriction:`
New: `The Natal government's stated ground for restriction (Lake does not name the speaker):`

C6. Line 219 (M5-14).
Old: `Whether illiterate men over 30 could then vote: NF.`
New: `The same entry reports that the laws of 30 June 1912 (n. 665) and 1913 raised the political electorate from 2,930,473 (1909) to 8,443,205 (8.3% to 23.2% of residents); whether illiterate men over 30 could then vote: NF. The 1882 entry also records a tax qualification of 19.80 lire, so the 1882 rise is not due to the school route alone (65.3% of the 1882 lists were entered "per capacità").`

C7. Line 139 (M5-20).
Old: `The directive's ground, as the censors put it:`
New: `The directive's ground, as the Valuev Directive itself put it:`

C8. Line 139 (M5-21).
Old: `'peasant language'" (p. 4).`
New: `'peasant language'" (p. 3).`

C9. Line 227 (M5-28).
Old: `a Catholic schoolmaster needed the ordinary's licence and the oath of supremacy.`
New: `Parnell lists elsewhere (pp. 27-28, from the 1697 Commons committee report) an older law under which a Catholic schoolmaster needed the ordinary's licence and the oath of supremacy; that law is not the 1695 act.`

C10. Line 223 (M5-32).
Old: `Gautama XII.4–6 prescribes molten tin or lac in the ears, the tongue cut out, the body split.`
New: `Gautama XII.4–6 prescribes, for a Śūdra (XII.1), molten tin or lac in the ears for listening to the Veda, the tongue cut out for reciting it, the body split for remembering it.`

C11. Line 129 (M5-34).
Old: `The reprint gives the year as 1881 in its header; other sources give 1882. Treat date as unresolved.`
New: `The reprint's header says 1881, but the deposition's signature block on the same page reads "Poona, 19th October 1882"; take 19 October 1882.`

C12. Line 266 (M5-34).
Old: `7. **Phule's date.** 1881 (reprint header) or 1882 (other sources).`
New: `7. **Phule's date.** The reprint's header says 1881; its signature block reads "Poona, 19th October 1882" (Round Table India).`

C13. Line 243 (M5-36, M5-41).
Old: `these are cases where the number was met by the government's own tests.`
New: `these are cases where the government's count was met, but the Tanzanian report itself says the 9.5% headline and the 35% pass rate are not reconciled and that "actual participation in programmes is far below the official statistics" (Kater et al., §3.3.1), and the Cuban figures come from a preprint that repeats them from sources not opened; neither is yet a clean counter-case to overselling.`

C14. Line 181 (M5-37).
Old: `the crusade certainly did achieve its major goal." Stated`
New: `the crusade certainly did achieve its major goal of drastically reducing the Nicaraguan illiteracy rate." Stated`

### M5_wider_cases.bib

C15. Line 38 (M5-B3).
Old: `  doi       = {10.22459/cw.03.2006},`
New: `  doi       = {10.22459/cw.03.2006}, % Crossref: this DOI is the whole volume (Connected Worlds, ANU Press 2006), not ch. 13; no chapter DOI found`

## (3) Over-read and under-read

Over-read.
1. Tanzania and Cuba as counter-cases to overselling (L243): Kater's own report says official participation figures overstate and the statistics mismatch; Cuba rests on a preprint the facet itself says not to cite (C13).
2. Chile 1874 "more than tripled" as a counter-case to the gate (L243-244): the sentence is E&S's, but E&S's own Table 3 shows 1.6% (1869) to 3.1% (1881), and its note dates abolition to 1878 (C4). Say "E&S state", not "the data show". Also E&S's text puts Ecuador's property test out in 1861, while Table 3 has Ecuador 1888 with wealth Y.
3. Italy 1882 as a literacy-franchise counter-case: the qualifying titles are school completion (second grade) and regimental school, not a reading test, and a lower tax qualification was enacted in the same law (C6). The widening came with a looser property test and age 21; the entry does not isolate the school route's effect.
4. "Keju as route to office" (L244, L286): the pages read (Ye pp. 69-72) show only the exclusion; the facet itself says no historian's verdict was opened. Keep it as a flagged hypothesis.
5. Brazil: reporting 1891 without the Saraiva Law left a false conflict with the paper (C1-C3); the paper's 1881 was right.
6. Lake's block quotation attributed to "the Premier" (C5).

Under-read.
1. Italy 1912-13: the same entry has the electorate rising to 8.44 million (23.2% of residents) (C6).
2. Brazil: Decreto 6 of 19 Nov 1889 and the 1824 Constitution (income only) are primary texts the facet could not reach; both are now confirmed, and the 1881 law is the only case in M5's set where a literacy bar was added to an income test in the same law.
3. Gautama XII.4-6: the penalty is for a Śūdra (XII.1); stating the target strengthens the withholding reading (C10).
4. Parnell: the licence-and-oath law is a pre-treaty law, so the Irish case has two layers (older licensing, 1695 education act) (C9).

## (4) Brazil date

The paper (and facet D) are right: 1881. I could not open Decreto 3.029 itself (Camara URL 404; Planalto page error; Wikisource has no text). Evidence: (a) Leão, "Lei Saraiva (1881)", Aedos 4(11), 2012, p. 611, quotes Senado, Anais 1881, p. 348: Art. 8 II admits to the roll citizens who prove the elector's qualities "e souberem ler e escrever", the project having passed the Senate on 4 Jan 1881 and become Lei 3.029 of 9 Jan 1881; Petermann (Estudos Eleitorais) agrees on the 9 Jan 1881 date; Leão says the Sinimbu project of 1879 first proposed the exclusion, "condição esta inexistente na Constituição de 1824". (b) Planalto, Constituição de 1824, arts 91-94: only income tests (200 mil réis for electors), no literacy test. (c) Planalto, Decreto 6 of 19 Nov 1889, art. 1: electors are those "que souberem ler e escrever". (d) Planalto, Constituição de 1891, art. 70 §1 2º: "Não podem alistar-se eleitores... os analfabetos". Why they differ: E&S date the literacy qualification by the Republic's first constitution and treat the Empire as property-based; they do not mention the Saraiva Law or the 1889 decree. 1891 is the constitutional entrenchment (to EC 25/1985 for the vote, not 1988 as E&S say for the "restriction"; the 1988 Constitution made voting optional for illiterates, which I did not open). Nuance for the paper: the 1881 law was mainly an end to indirect elections, raised income proof, and let those already enrolled keep the vote (facet D, citing Nicolau; secondary).

## (5) Counts

Table rows: 41 checked; 30 CONFIRMED; 9 WRONG; 2 UNVERIFIABLE (M5-13 Italy law year; M5-39 Sandiford abstract; M5-14 is counted CONFIRMED with an under-read note). Bib: 10 rows (11 distinct DOIs plus the Ayalon chapter DOI resolved): 8 CONFIRMED, 1 WRONG (Lake DOI is the volume), 1 UNVERIFIABLE (Choi). The bib has only 11 DOIs, so the 15-DOI target could not be met. Combined M5: 51 checked, 38 confirmed, 10 wrong, 3 unverifiable.

## (6) Not checkable and why

Decreto 3.029 text (Camara and Planalto pages failed); sacred-texts.com (Cloudflare wall; archive.org scans of Bühler used instead; Gautama page differs by scan, p. 239 here vs 236 in facet C); Manu 9.18 not looked for; Italy law date 1882 (not opened); Sandiford abstract (not reopened); Choi 2026 p. 16 and Mair 2025 (optional list, not re-opened); Ayalon extract and Schwartz (facet itself could not open); Leonard pp. 167-168 page markers; Remy 2007, Tarnawsky (not accessible); the Ballini entry's year for the Dizionario volume.

---

## Tally

| facet | items checked | CONFIRMED | WRONG | UNVERIFIABLE |
|---|---|---|---|---|
| M1 | 47 | 39 | 6 | 2 |
| M2 | 50 | 42 | 6 | 2 |
| M3 | 35 | 29 | 4 | 2 |
| M4 | 60 | 53 | 4 | 3 |
| M5 | 51 | 38 | 10 | 3 |
| all five | 243 | 201 | 30 | 12 |
