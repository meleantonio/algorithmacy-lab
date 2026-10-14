# Knijnenburg, B. P., Willemsen, M. C., Gantner, Z., Soncu, H., & Newell, C. (2012). Explaining the user experience of recommender systems. *User Modeling and User-Adapted Interaction, 22*(4–5), 441–504. https://doi.org/10.1007/s11257-011-9118-4

**Identifier:** doi:10.1007/s11257-011-9118-4 · **Read depth:** partial: the publisher's open-access PDF (CC BY) as deposited in the TU/e repository (pure.tue.nl, 65 pp. with a one-page cover; journal pagination, pdf p. 2 = p. 441). I read §§1–3 in full (framework, review, research requirements, including §3.6.3 "Explanations"), §4.1–4.3 (background, Table 1, method, FT1 in full), the discussion subsection of every study (FT2–EX2), §5 (validation, Table 2), §6 Conclusion and §7 Future research. I did not read the results subsections of FT2–EX2 line by line (path models, coefficients) or Appendices A–B. The Springer page is behind a bot check, so I used the repository copy · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** a user-centric evaluation framework (objective system aspects → subjective system aspects → experience → interaction, with personal and situational characteristics) tested in four field trials and two experiments with media recommenders: FT1 n = 43, FT2 n = 108, FT3 n = 59, FT4 n = 58, EX1 n = 174, EX2 n = 137 (Table 1, pp. 458–459), analysed with factor analysis and structural equation models · **Parties modeled:** person–system (a user and a recommender) · **Facets:** none (cited only in DRAFT_v2 §2.1) · **Read:** 2026-10-14

## What it argues

The title's "explaining" refers to the researchers explaining user experience, not to a system explaining its recommendations. Knijnenburg and colleagues argue that algorithm accuracy is a poor proxy for what users experience. Their framework holds that objective system aspects (algorithm, interface, presentation) affect experience through users' perceptions of them: "the presumed link between algorithm accuracy (an OSA) and user experience (EXP) is all but evident" (p. 450).

Across six studies the core chain held: "the link from algorithm or preference input data (OSA) to subjective recommendation quality (SSA) to experience (EXP)—is upheld throughout every conducted study" (p. 485). Other results: diversified lists were not seen as more diverse but as more accurate (Table 2, p. 484); "reduced browsing and increased consumption are indicators of effective systems" (p. 485); feedback intentions trade off experience against privacy, and intention and actual feedback can diverge (p. 485). The authors limit scope: "we only tested a small number of media-oriented recommender systems" (p. 487), all collaborative-filtering systems built on one framework (p. 457).

Explanations appear in one short review paragraph, §3.6.3 (p. 455): "Herlocker et al. (2000) found that users like explanations in collaborative filtering recommender systems." It adds that explanations raised perceived competence and trust in knowledge-based recommenders (Felfernig et al. 2007; Cramer et al. 2008) and that personalised explanations may be "less effective than generic explanations" (Tintarev & Masthoff 2012). None of the six studies manipulates explanations.

## Relation to the argument

**Premise P8 (disclosure is a literacy intervention).** The paper offers indirect support: in its studies what users perceive matters more than what the system objectively does, and perception mediates every effect. That is consistent with D3's point that handing people information about a system is not the same as changing how they act. It does not test disclosure or explanation.

**What it cuts.** Nothing against the author. It simply does not bear on transparency.

**Use in DRAFT_v2:** Line 31: "The initial remedy was straightforward: attach an explanation showing neighboring user ratings or item similarities (Herlocker, Konstan, & Riedl, 2000; Knijnenburg et al., 2012)." **Not supported as a primary source.** Knijnenburg et al. do not design, test or advocate explanations showing neighbours' ratings; they mention explanations once, in a review paragraph that cites Herlocker et al. (2000) (p. 455). The "explaining" in the title concerns the researchers' model of user experience. If the draft wants a second citation for explanation interfaces in recommenders, the works Knijnenburg et al. cite at p. 455 (Cramer et al. 2008, on transparency and trust in an art recommender; Tintarev & Masthoff 2012) are closer. The author's earlier facet work used a different Knijnenburg paper, `knijnenburg2012inspectability` (Knijnenburg, Bostandjiev, O'Donovan & Kobsa, RecSys 2012), which does test inspectability; the draft's reference list cites this 2012 UMUAI article instead. The author may have meant the RecSys paper.

## In conversation with

- `herlocker2000explaining` — cited at p. 455 as the finding that users like explanations in collaborative filtering; that is the primary source for the draft's line.
- `knijnenburg2012inspectability` — same first author, same year, a different paper (inspectability and control in a social recommender); possibly the intended citation.
- `vaccaro2018illusion` — on control settings in feeds; same family as the preference-input manipulations here, not cited by this paper.
- Not in the bib, as leads: Cramer et al. (2008), "The effects of transparency on trust in and acceptance of a content-based art recommender", *UMUAI* 18 (p. 455); Tintarev & Masthoff (2012) on explanation effectiveness (p. 455); Pu & Chen (2010) on recommender user-experience questionnaires (p. 446); McNee et al. (2006) on accuracy not being enough (p. 443).

## Caution

Media recommenders only, collaborative filtering only, mostly self-report perceptions analysed with SEM; the authors call the validation "preliminary" for parts of the framework (p. 456). The results subsections of five studies were read only through their discussions and Table 2, so specific coefficients are not reported here. The TU/e cover page misprints the pages as "411-504"; the journal pages are 441–504, as the draft has them.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the TU/e repository copy saved at dxd_foundation_local/pdfs/R4b/knij.pdf (65 pp.; cover page, then the publisher's PDF with journal pagination, pdf p. 2 = p. 441) and located every quotation by page: "all but evident" (p. 450), the OSA → SSA → EXP chain "upheld throughout every conducted study" (p. 485), "reduced browsing and increased consumption…" (p. 485), "we only tested a small number of media-oriented recommender systems" (p. 487), the §3.6.3 "Explanations" paragraph with the Herlocker sentence and "less effective than generic explanations" (p. 455), and "preliminary" (p. 456). I checked the six sample sizes in Table 1 (FT1 43, FT2 108, FT3 59, FT4 58, EX1 174, EX2 137; pp. 458–459), the Table 2 row on diversification (p. 484), the single-framework limitation (p. 457), and the cover page's "411-504" misprint. The record matches Crossref (UMUAI 22(4–5), 441–504, 2012). I re-read DRAFT_v2.md line 31.

**Findings:**
1. All quotations, numbers and locators match. No changes to the card body.
2. The read depth is honestly stated as partial (results subsections of FT2–EX2 and appendices not read line by line); nothing the card asserts depends on the unread parts.
3. The "Use in DRAFT_v2" verdict stands: the article does not design or test neighbour-rating explanations; it mentions explanations once, in a review paragraph citing Herlocker et al. (2000) (p. 455). Citing it as a source for "attach an explanation showing neighboring user ratings or item similarities" is not supported. The suggestion that the author may have meant `knijnenburg2012inspectability` is flagged for them to decide.
