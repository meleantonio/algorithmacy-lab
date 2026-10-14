# Rogers, R., Subramaniam, S., Peng, S., Durfee, D., Lee, S., Kancha, S. K., Sahay, S., & Ahammad, P. (2021). LinkedIn's Audience Engagements API: A privacy preserving data analytics system at scale. *Journal of Privacy and Confidentiality, 11*(3). https://doi.org/10.29012/jpc.782

**Identifier:** doi:10.29012/jpc.782 · **Read depth:** full_text (the journal's open-access PDF, CC BY-NC-ND 4.0, 27 pp., submitted April 2021, published December 2021, marked "TPDP 2020"; read whole, including the appendix proofs, which I followed in outline only) · **Source-tier:** peer-reviewed article (practitioner systems paper by LinkedIn staff) · **Evidence basis:** direct_read · **Design and sample:** system description with parameter-setting rationale and empirical runs on LinkedIn data (1,000 trials per configuration for Figures 3–4; budget-exhaustion curves from logged analyst queries, Figure 5) · **Parties modeled:** two parties + third party (LinkedIn as platform, its members whose data are queried, and marketing analysts who receive noisy results) · **Facets:** R4 · **Read:** 2026-10-14

## What it argues

Rogers and colleagues describe how LinkedIn added differential privacy to an API that gives marketers aggregated insight into what members engage with. The design choice is stated plainly: "To make such a product private, it is apparent that one must add noise, to prevent differencing attacks, and limit the number of accesses to the API" (p. 2). Results returned to analysts carry Laplace or Gumbel noise (§5, Algorithms 1–4), top-k queries can return fewer than k items because of a noisy threshold, and each analyst has a monthly "information budget" and "call budget" after which queries are refused (§6). Once a budget is spent, "a marketing partner would recycle old queries to get the same results or wait some fixed amount of time for the privacy budget to be refreshed" (p. 17).

The paper reports how the noise was tuned. A per-query ε of 0.15 gives about an 11% chance that averaging 30 days of answers to the same query recovers a true count (§8.3.1, p. 20); an information budget of about 3,000 and a call budget of 30 would leave at least 93% and 95% of analysts respectively unaffected (p. 18; restated pp. 21 and 22); the overall guarantee is (34.9, 7 × 10⁻⁹)-DP per month (§8.4, p. 22). Answers are kept consistent by seeding the noise with the query and the date, so "if someone asks the same query, then they get the same result" (p. 18) within a day. The data are loaded daily and kept 30 days (p. 19). The team rolled the system out in phases because they were "Not knowing how external marketing partners would respond to budgeting access to queries and noisy results" (p. 17); at writing the API was "still only available to a set of trusted users and pre-general availability (pre-GA)" (p. 17). Table 2 (p. 22) lists other deployed differential-privacy systems by Google, Apple and Microsoft, and the text names Uber's FLEX for internal analytics (p. 3).

## Relation to the argument

**The draft's account of mediated distortion (§5.3).** Line 279 says no source shows a platform introducing noise on purpose. Here a platform, in a peer-reviewed paper by its own engineers, adds calibrated noise to the feedback it gives business users about its audience, caps how much they can ask, and refreshes the data on a daily cycle. The purpose is privacy for third parties, not control of the users who receive the noise. That purpose matters for the paper's moral reading but not for the cognitive point at line 281: the analyst gets a deliberately perturbed answer.

The source also shows a mediator with a legitimate reason to keep feedback noisy. A convention that demands "valid and noise-filtered" feedback (line 368) will meet privacy law and third-party interests that require noise. This is a design constraint the draft does not mention.

**Use in DRAFT_v2:** This paper is not cited in DRAFT_v2.md (grep "Rogers", "LinkedIn", "differential": no hits in the paper body or references). The lines below are where the draft makes claims this source bears on.
- Line 279 ("No source I have found shows that a platform introduces noise or delay on purpose"): contradicts. LinkedIn adds noise to analytics returned to marketers by design (pp. 2, 10–13), and the paper lists other firms' deployed differential-privacy systems (p. 22).
- Line 278 (strategic rule secrecy justified "to prevent 'gaming'"): bears only indirectly. What LinkedIn limits and perturbs is data about members, not the rules of an allocation, so this is not rule secrecy. It does show a stated reason for limiting what users can learn that is neither gaming nor control: preventing differencing and reconstruction attacks on members' data (pp. 1–2).
- Line 368 ("feedback that is valid and noise-filtered first"): complicates. Some mediator noise is required to protect third parties and cannot be filtered out without undoing the protection (§8.3).

## In conversation with

- `li2010contextual` — deliberate randomisation of what a platform serves; together the two are the platform-side sources for line 279.
- `chen2015peeking` — the draft's example of unintended noise (Uber surge jitter).
- `rahman2019invisible` — the draft's source on secrecy as control; this paper gives a different, privacy-based reason for limiting what users learn.
- Not in the bib, as leads: Kenthapadi and Tran (2018), "PriPeARL", LinkedIn's ad-analytics privacy system; Erlingsson, Pihur and Korolova (2014), RAPPOR; Dwork, McSherry, Nissim and Smith (2006) on calibrating noise; Johnson, Near and Song (2018) on Uber's FLEX.

## Caution

The users receiving noise are marketers querying aggregate audience data, not workers or consumers trying to learn how a matching or ranking algorithm treats them. The paper reports no study of how analysts understood or reacted to the noise. It describes a pre-GA product in 2020–2021; whether it shipped in this form is not stated.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the writer's saved copy (dxd_foundation_local/pdfs/r4c/rogers2021.pdf, the JPC open-access PDF, Vol. 11(3), TPDP 2020, submitted Apr 2021, published Dec 2021) and extracted it page by page, using the printed page numbers. I matched all five quotations word for word with their pages (2, 17, 18, 17, 17). I checked ε_per = 0.15 and the 11% attack probability (§8.3.1, p. 20), the 3000 information budget and 93% (pp. 18, 21), the 30-call budget and 95% (pp. 18, 22), (34.9, 7 × 10⁻⁹)-DP monthly (§8.4, p. 22), the daily load with 30-day retention (p. 19), the 1000 trials (p. 16), Uber's FLEX (p. 3) and Table 2 (p. 22). I checked the record against Crossref: eight authors, 11(3), DOI. Crossref truncates the title to "LinkedIn's Audience Engagements API"; the full title is from the PDF. I re-read DRAFT_v2.md lines 278–281 and 368.

**Findings:**
1. The locator for the 95% call-budget figure was wrong: the card gave pp. 18 and 21, but it appears on pp. 18 and 22 (the 93% figure is on pp. 18 and 21). Corrected.
2. The line-278 verdict "narrows" overstated the source's relevance. LinkedIn perturbs data about members, not the rules of an allocation, so the source is not evidence about rule secrecy. The verdict is reworded to "bears only indirectly", and the card says why.
3. "Use in DRAFT_v2" did not say the source is uncited; I added that statement. The line-279 verdict (contradicts, for deliberate noise) and the line-368 verdict (complicates) stand on re-reading.
4. The quotations, the other numbers, the reference record and the full-read claim all check out.
