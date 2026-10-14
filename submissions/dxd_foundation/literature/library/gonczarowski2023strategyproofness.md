# Gonczarowski, Y. A., Heffetz, O., & Thomas, C. (2023). Strategyproofness-exposing descriptions of matching mechanisms (NBER Working Paper 31506; rev. October 2025). National Bureau of Economic Research.

**Identifier:** doi:10.3386/w31506 · **Read depth:** partial (NBER working paper, "July 2023, Revised October 2025", 67 PDF pages; I cite printed page numbers, which run two below the PDF page). I read Sections 1 to 7 (printed pp. 1–24) and the reference list. I skimmed the appendices (A, the proof of Theorem 5.3; B, further proofs; Supplemental S and T) by headings and opening paragraphs and did not check the proofs · **Source-tier:** working paper · **Evidence basis:** direct_read · **Design and sample:** theory (definitions, two constructions, one impossibility theorem); no data, no participants · **Parties modeled:** person–system (one applicant at a time facing a matching mechanism); other applicants enter only through their reports; institutions are non-strategic (p. 1, fn. 3) · **Facets:** H · **Read:** 2026-10-13

## What it argues

The authors begin from the fact that "real participants in strategyproof mechanisms often play theoretically dominated strategies, raising the possibility that they do not perceive the mechanisms as strategyproof" (p. 1). They hold the mechanism fixed and change its description: "we propose changing only the (ex ante) description of a given static, direct-revelation mechanism" (p. 1). A *menu description* has two steps. Step 1 uses only the other applicants' reports to compute the applicant's menu of reachable outcomes. Step 2 gives her the favourite item on it. Strategyproofness then follows in one sentence, because her own report cannot change her menu (pp. 2, 9).

Three results follow. (1) A menu description of Deferred Acceptance (DA): run institution-proposing DA without the applicant; her menu is every institution that ranks her above its hypothetical match (Description 1, p. 11; Table 1, p. 2). (2) A menu-in-outcome description of Top Trading Cycles (TTC) that changes only the order in which cycles are eliminated, which gives a new proof that TTC is strategyproof (Section 4, pp. 13–14). (3) An impossibility: any applicant-proposing menu-in-outcome description of DA needs quadratic memory, so no "slight tweak" of DA's traditional description can expose its strategyproofness (Theorem 5.3, p. 19). Serial Dictatorship already exposes it, TTC can be tweaked to, DA cannot (p. 4).

The behavioural claim stays outside this paper. The Discussion says strategyproofness is meant to level the field for players who do not strategize well, "However, we observe that if participants do not all understand that the mechanism is strategyproof, then disparities may remain" (p. 23). It then summarises an empirical companion (Gonczarowski, Heffetz, Ishai and Thomas 2024): understanding is "similar under both descriptions of DA", and "very high" under a stripped-down menu description that omits how the menu is computed (p. 23). Menu descriptions may also "obscure other properties", such as feasibility (p. 24).

## Relation to the argument

**P8.** This is the source in the batch that treats the presentation of a task-removing rule as a design object. It separates the rule (strategyproof, task removed) from the description (what the person is told), and says the second can fail while the first holds. That fits the second clause of P8. It does not test it, since it reports no participant data.

**Ruling D3.** The paper supports classing description redesign as a literacy-side intervention: the rule already removes the strategic task, and the description is changed to raise understanding. It also bears on the flag in SOURCE.md that "doesn't affect" is too strong. If the companion's result is as summarised here, the form of the description matters (the stripped-down version did best), which argues for "which disclosure and how short" over a flat "disclosure doesn't help". I did not read the companion, so this rests on the authors' summary.

**Against the author.** Institutions are non-strategic by assumption (p. 1, fn. 3), so the mediator has no interest of its own. That is the P8 weak point the argument map already names. Nothing here speaks to P10.

**Facet check:** facet H (line 173) says the authors "show with a lab experiment on two elementary mechanisms 'the promise and challenges of menu descriptions'". The October 2025 revision has no experiment, and that phrase does not occur in it. The experiments are in the companion and, per the authors, in the earlier version, which "conduct[ed] an experiment for a second-price auction and median voting" (p. 23; arXiv 2209.13148v2). The facet's abstract came from a different version than the PDF on file.

## In conversation with

- `li2017obviously`: the "strategic simplicity" programme that inspires the paper; obviously strategy-proof mechanisms are dynamic, and TTC has none (p. 21).
- `ashlagi2018stable`: DA has no obviously strategy-proof implementation (p. 21).
- Leads not in the bib: Hammond (1979) on menus; Katuščák and Kittsteiner (2025) on describing mechanisms to participants; the Gonczarowski–Heffetz–Ishai–Thomas (2024) companion; Rees-Jones and Shorrer (2023) and Hakimov and Kübler (2021) on non-straightforward play (p. 1); Morrill and Roth (2024), quoted at p. 3, fn. 4.

## Caution

A theory paper. Cite it for what a menu description is and for the DA/TTC results, not for any finding about what participants understand or do. The version on file (October 2025) differs from the version the facet read. The impossibility result holds for a formal notion of "slight tweak" that the authors call a necessary condition, not a full definition (p. 19). Proofs not checked.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the NBER w31506 PDF (Oct 2025 revision, 67 pp.), extracted with pdftotext. Checked all 8 in-source quotations (exact words) and page locators (printed = PDF minus 2) for the pp. 1, 2, 4, 11, 19, 21, 23, 24 claims, fn. 3, fn. 4, Table 1 and the Related-work citations of Li 2017 and Ashlagi-Gonczarowski 2018. Quotations from SOURCE.md and the facet file were not checkable against this source.

**Findings:** One fix: the Read depth line said full_text although the card states the appendices (printed pp. 25-65, about two thirds of the PDF) were only skimmed; changed to partial and kept the list of what was not read. Quotations, locators, the Table 1 / Description 1 content, the companion-paper summary and the fn. 3 non-strategic-institutions assumption all match. The absence of the phrase 'the promise and challenges of menu descriptions' in this version is confirmed by search.
