# COMPLETENESS — round 4 completeness critic

*Agent-written (Claude), 2026-10-14, research round 4. The author has not reviewed it. Nothing in DRAFT_v2.md, the bib,
INDEX.md or any card was edited. Line numbers are DRAFT_v2.md's as of today.*

**Method.** Scripts in the session scratchpad parsed the 104 reference-list entries (lines 505–711), matched each to a card
by DOI in the card header and then by surname + year, and checked each was cited in lines 11–502 (and the reverse, by
extracting every parenthetical and narrative author–year citation). Ledger coverage was computed from the `Line` column
of the seven `CLAIMS_0*.md` tables, including their range rows such as "95–109", over the 148 blank-line-separated
blocks of lines 11–502. For check 5, I paired each card's "Use in DRAFT_v2" paragraph with the ledger rows for the same
line and source, then read every pair.

## Summary

| Check | Result |
|---|---|
| 1. Every reference entry has a card | **Yes: 104/104.** No reference is uncarded. |
| 2. In-text citations ↔ reference list | **No orphans by author–year in either direction.** Line 123 names three primary sources that have no reference entries, and line 121 uses an unattributed term (details below). |
| 3. Ledgers cover every paragraph of 11–502 | **All prose paragraphs are covered.** Two signposting sentences, two mock-ups recorded only in prose, and the top of one diagram have no ledger row. |
| 4. Cards read 2026-10-14 have an S2 section | **114 of 117 do.** Three do not: `boretius1883capitularia`, `charlemagne1900letter`, `dummler1881alcuini`. |
| 5. Card verdict vs ledger verdict | **4 clear conflicts, 7 softer mismatches, 2 cards silent on lines the ledger flags.** 45 reference-list cards have no "Use in DRAFT_v2" section, so they could not be compared. |

## 1. Reference list → cards

All 104 entries match a card. Nine are matched by name rather than by DOI or surname + year:

| Reference entry (line) | Card |
|---|---|
| Bundesministerium der Justiz, BetrVG § 87 (515) | `de1972betrvg` |
| Directive (EU) 2024/2831 (547) | `eu2024platform` |
| FCA 2014 press release (557) | `fca2014fines` |
| FSB 2014 final report (559) | `fsb2014foreign` |
| NYDFS 2015 consent order (637) | `nydfs2015barclays` (the press release is a separate card, `nydfs2015barclayspr`) |
| Nottingham 2020, RFC 8890 (641) | `rfc8890` |
| Regulation (EU) 2019/1150 (667) | `eu2019p2b` |
| Regulation (EU) 2022/2065 (669) | `eu2022dsa` |
| Rules Enabling Act, 28 U.S.C. § 2073 (673) | `usc1988rules` and `us2073usc` (two overlapping cards for one entry; `us2072usc` also exists) |

Notes:
- The Nadella entry (635) cites the X post. The matching card, `nadella2026models`, was read from the blog page and checked
  against the X capture paragraph by paragraph, so it covers the entry. Two other Nadella cards (`nadella2026reverse`,
  `nadella2026frontier`) are not in the reference list.
- The Casella card key reads `casella2025fragility`, but the entry and the in-text citation give 2026. The DOI matches.
- **INDEX.md is stale.** It lists none of the 117 cards marked Read 2026-10-14, among them reference-list cards such as
  `bansal2021whole`, `schemmer2022meta`, `vaccaro2024when` and `rfc8890`. `build_index.py` is in the library, but INDEX.md
  is outside this stage's write scope.

## 2. In-text citations ↔ reference list

- **Reference entries never cited in 11–502:** none. Every one of the 104 entries is cited at least once.
- **Author–year citations with no reference entry:** none.
- **Sources named in the text with no reference entry:**
  - Line 123: Charlemagne, *De litteris colendis*; the *Admonitio generalis* of 789, c. 72; and Alcuin, *Carmen* XCIV.
    The ledger marks all three needs_citation (C03-36, C03-37, C03-38). Each now has a card (`charlemagne1900letter`,
    `boretius1883capitularia`, `dummler1881alcuini`) and a bib key, but none has a reference-list entry.
    CLAIMS_07 point 8 still says the letter and the *Admonitio* are "bib keys without cards". That is out of date.
  - Line 121: "behavioral surplus" is Zuboff's term, and Zuboff appears in no reference entry, bib key or card (C03-33,
    needs_citation).
- **Year or form mismatches:** none found in the in-text citations. The Özçetin & Wiltse year (2023 against volume 40,
  2025) is already flagged in C02-31 as miscited.

## 3. Ledger coverage of lines 11–502

Every prose paragraph and list item in lines 11–502 has at least one ledger row. Headings have no rows. Some carry
claims ("Enterprise Compliance as the Zenith of Literacy Dogma", line 178; "Four Falsifiable Claims", line 445), but
those claims are restated and checked in the body. The following have no ledger row:

| Lines | Content | Status |
|---|---|---|
| 49–52 | "Classic HCI Dyad" mock-up | Recorded only in CLAIMS_02's prose ("Mock-ups recorded, not checked", ledger line 61), with no table row. |
| 56–71 | "Irreducible Algorithmic Triad" mock-up | As above. |
| 133–140 | Top of the disclosure-taxonomy diagram (Targets 1–2 boxes) | C04-47 gives the range as "141–153". The diagram runs from 133 to 153, so 133–140 falls outside the row as written. |
| 412 | "To evaluate how custody functions in practice, I examine three institutional environments:" | Signposting. Not recorded. |
| 495 | "To ensure theoretical precision, this framework establishes five explicit scope boundaries:" | Signposting. Not recorded. |

Line 414, the header row of the custody table, is not a claim. The table's body rows (416–418) are covered by C07-05
onward.

## 4. S2 sections on cards read today

117 cards carry **Read: 2026-10-14**. 114 have a `## S2 adversarial verification` section. Three do not:

| Card | Read depth | Missing |
|---|---|---|
| `boretius1883capitularia` | partial (OCR of no. 22, cc. 71–73) | S2 section; not in INDEX.md |
| `charlemagne1900letter` | full_text of the Munro English translation only | S2 section; not in INDEX.md |
| `dummler1881alcuini` | partial (*Carmen* XCIV, p. 320) | S2 section; not in INDEX.md |

The CLAIMS_03 writer made all three during claim verification (file times 09:05–09:06). They support C03-34 to C03-41,
so an S2 pass on them would also secure those ledger rows.

## 5. Card "Use in DRAFT_v2" verdict vs ledger verdict

60 of the 104 reference-list cards have a "Use in DRAFT_v2" paragraph. The other 45 were written on 2026-10-13, before
that section was required, and could not be compared. They are listed at the end of this section.

### 5a. Clear conflicts (the card and the ledger reach different verdicts on the same words)

| Line | Source / ledger row | Card says | Ledger says | Note |
|---|---|---|---|---|
| 176 | `nouwens2020dark` / C04-31 | "Layout alone" is "slightly loose": removing the button also raised the clicks needed to reject, so effort changed as well as layout. | **supported (revised by skeptic)**: "a layout manipulation and nothing else". | The two readings are opposed. Settle against Study 2's design. |
| 39 | `disley2026designing` / C02-26 | "**overstates** the evidence": "productive" rests on self-report in an unblinded study, and the authors disclaim creativity claims (p. 34). | **supported_narrower** (the skeptic revised it from overstated). | The card was not updated after the skeptic's revision, or the skeptic did not weigh p. 34. |
| 123 | `westwell2018dissemination` / C03-41 | The closing claim "an authority with standing over the scribe" is "in tension with Westwell's distributed picture (pp. 255, 289–290); a reader could cite him against it". | **supported (revised by skeptic)**, on c. 72 and Alcuin. | The ledger lists no "cuts against" for Westwell on this row. CLAIMS_07 point 8 makes the same narrowing for lines 441/501. |
| 325 | `gonczarowski2024describing` / C06-18 | "One **substantive misdescription**": the 71% came from Menu-SP, a property-only menu, while the menu description of the algorithm (Menu-DA) scored 58%. | **supported_narrower (revised by skeptic)**. | CLAIMS_06 main point 2 states the card's reading. The verdict code is milder than the ledger's own text. |

### 5b. Softer mismatches (same direction, different strength)

| Line | Source / row | Card | Ledger |
|---|---|---|---|
| 31 | `lee2004trust` / C02-09 | "partly supported, partly **contradicted**" (MS pp. 4, 14) | overstated |
| 35 | `lee2025impact` / C02-21 | "partly supported"; "when they do" **misplaces** the finding, since the reduction goes with *not* reading closely | supported_narrower |
| 39 | `horvath2022understanding` / C02-27 | "partly supported, and partly **cut against**" (p. 13: the annotation "is missing this full context") | supported_narrower (revised from overstated) |
| 33 | `metzger2001role` / C02-16 | "only partly supported": the study is not about prolonged reliance or automated aids, and has nothing on manual skill | supported_narrower |
| 113 | `wolfe2021guided` / C03-21 | "partly supported": salience is one of five guidance sources | supported (revised by skeptic: "guides", not "alone guides") |
| 420 | `usc1988rules` / C07-12 | "mostly supported, with one **correction of agency**": the Supreme Court prescribes, committees recommend | supported (revised by skeptic; the ledger's correction column carries the same agency point) |
| 325 | `gonczarowski2024describing` / C06-20 | (d) "Correct" (59/56/48%, p. 28) | supported_narrower |
| 85 | `burnyeat1997postscript`, `gavrilov1997techniques` / C03-10 | neither card could check the claim against the article's own words | supported (revised by skeptic), resting on Knox, read in full |
| 497 | `scribner1981psychology` / C07-72 | "Supported in principle", but from the 1978 article; no page of the 1981 book seen | UV (unverifiable). The card's verdict rests on a different work from the one cited. |

### 5c. Cards silent on lines where the ledger flags an error

- `gonczarowski2024describing`: its Use section skips **line 327**. The ledger has C06-22 **contradicted** ("better
  understanding moved play only a little" against the paper's fourth main result) and C06-21 flagged **broken** (rounds,
  not participants). Both rows cite the paper as "implied".
- `schemmer2022meta`: its Use section covers line 168 only. It skips **line 19** (C01-25, supported after the skeptic's
  revision).

### 5d. Agreements worth noting

For the remaining 41 cards the card and the ledger agree. Among them are the main negative findings:
- `cameron2022expanding` (266, not_in_source)
- `ehsan2021expanding` (31, not_in_source)
- `knijnenburg2012explaining` (31, not_in_source)
- `korber2018theoretical` (31, not_in_source)
- `herlocker2000explaining` (31, overstated)
- `rfc8890` (428: "voluntary" not_in_source; "little part" supported)
- `de1972betrvg` (439, supported_narrower)
- `eu2024platform` (438, item by item)
- `kluger1996effects` (366: first sentence supported, second sentence needs_citation)
- `masuda2022net` (329, overstated "behavior … more than outcomes")
- `hertwig2017nudging` (499: S, with the boost cut-against recorded on both sides)

### 5e. Reference-list cards with no "Use in DRAFT_v2" section (45; not comparable)

`bai2008reading` `bassetti2012effects` `bucinca2021trust` `cabrera2023improving` `cert2022common`
`chantavarin2025effects` `colvin2011empirical` `cui2023eye` `eu2019p2b` `eu2022dsa` `fca2014fines` `fsb2014foreign`
`galanter1974why` `globalfxc2024code` `heilmann2020reading` `hohenstein2023artificial` `hutchins1995cockpit`
`jensen1976theory` `jhaver2019suspect` `kahneman2009conditions` `kirsh1995intelligent` `kirshmaglio1994distinguishing`
`klonick2018new` `knox1968silent` `li2017obviously` `mathews1976eldridge` `matsuo2026educational` `nadella2026models`
`nydfs2015barclays` `oberschelp1995developing` `oversight2022q1` `parasuraman2010complacency`
`poursabzi2021manipulating` `rahmandad2023delays` `risko2016cognitive` `seira2017are` `shneiderman1983direct`
`street2003whats` `suzor2018digital` `tumey1927ohio` `us2073usc` `vasconcelos2023explanations` `weick1988enacted`
`winskel2009eye` `zhang1994representations`

Several of these carry ledger errors with no card-side verdict to check against:
- `nadella2026models`: C04-38 and C04-40 miscited
- `parasuraman2010complacency`: C02-12 not_in_source
- `nydfs2015barclays`: line 417, benchmark versus Last Look (CLAIMS_07 point 1)
- `fca2014fines` and `fsb2014foreign`: line 424 (CLAIMS_07 point 2)
- `oversight2022q1`: line 418, "advisory" (CLAIMS_07 point 7)

## Open items for the next stage (no action taken here)

1. Add reference entries for the three Carolingian primary sources (line 123), and decide on Zuboff (line 121).
2. Run S2 on `boretius1883capitularia`, `charlemagne1900letter` and `dummler1881alcuini`.
3. Resolve the four 5a conflicts, starting with Nouwens (176) and Westwell (123), where the readings are opposed.
4. Rebuild INDEX.md (`library/build_index.py`) so the 117 cards from today appear.
5. Add ledger rows for lines 49–52, 56–71 and 133–140 (illustrations) if every block is to have a row.
