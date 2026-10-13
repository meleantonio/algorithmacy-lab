# Mejia, J., & Parker, C. (2021). When transparency fails: Bias and financial incentives in ridesharing platforms. *Management Science, 67*(1), 166–184.

**Identifier:** doi:10.1287/mnsc.2019.3525 · **Read depth:** full_text (preprint dated "History: September 20, 2019", an SSRN-header manuscript from the Indiana University repository; it is not the journal version, so the figures should be re-checked against the published article; locators are manuscript sections) · **Source-tier:** peer-reviewed article (preprint read) · **Evidence basis:** direct_read · **Design and sample:** randomised field experiment on a major ridesharing platform, Washington DC, early October to mid November 2018; 3,200 requested rides (1,600 peak, 1,600 non-peak), 3,189 distinct drivers who accepted; two MTurk surveys (200 drivers screened, 149 kept; a rainbow-filter perception check) · **Parties modeled:** two parties + third party (rider, driver, platform) · **Facets:** H · **Read:** 2026-10-13

## What it argues
The platform had already removed the rider's race and gender from the ride request shown to drivers, so the information reached the driver only after acceptance. Mejia and Parker ask whether this change in the timing of customer transparency removed bias or moved it (§1). They send ride requests through the platform's API, varying name and profile photo (female or male; Caucasian or under-represented minority, URM) and a rainbow filter on the photo (LGBT support or none), and they vary time of day (peak or non-peak) (§3.1). The driver sees only the general pickup area at the request stage; after acceptance, the name, photo and exact location appear, and the researchers wait three minutes for a driver cancellation (§3.1).

Results (§4). At the request stage the bias has gone: time to match is "close to 23.5 seconds for all of the treatments" and quoted wait about six minutes for all. After acceptance, the cancellation rate is 3.1% for Caucasian riders and 7.5% for URM riders (§1, aggregate). In the logistic regression URM riders are 2.60 times as likely to be cancelled on and riders with the rainbow filter 1.46 times; there is no gender difference. Peak times lower cancellations (odds ratio 0.54). The peak moderation applies to URM riders only: odds ratio 3.57 for URM in non-peak time, falling to 0.45 of that in peak time; the LGBT-support estimate changes from 1.72 to 0.66 times but that change is not significant (§4, Table 2).

The authors draw the management lesson that "small" pieces of information and their timing change service outcomes, and that nudges which delay information "can backfire on the very users it sought to protect" (§1). They suggest the platform could penalise biased cancellation or policymakers could mandate what drivers may see (§5).

## Relation to the argument
Facet H uses this paper as the clearest triadic field experiment in which the mediator's rule about what each party sees changed behaviour. It fits premise P8: a rule held in the mediator (what the driver sees, and when) is the lever, and no reading aid is involved. The full text also shows the limit of the lever: the removed task relocated. The bias moved from the request stage to the cancel stage, and the authors say minority riders may be worse off for it because they pay the cost of waiting and re-requesting (§5.1; the authors offer this as a conjecture for future research, not a finding). That supports the facet's "the removed task relocates" caveat (cf. Arteaga et al. in P8). It also bears on P10: the platform has its own objective ("platforms are trying to maximize the number of participants"), so a rule the platform can withdraw alone is not a convention, and the authors propose external mandate (§5).

Facet check: the facet cites "3,200 requested rides" and the authors; both confirmed. This preprint reports the pre-publication figures; I did not compare them with the journal version.

## In conversation with
The paper builds on the operational-transparency literature (Buell and Norton 2011; Buell et al. 2016, 2019), on ridesharing discrimination studies (Ge et al. 2016; Cui et al. 2016; Edelman et al. 2017) and on the audit-study method of Bertrand and Mullainathan 2004 (the rider names come from that paper, §3.1). It sits against the economic view that reducing information asymmetry raises efficiency (Stiglitz 2002, 2003). I found no entry from its reference list in `references.bib` by surname search. Within the bib, `fradkin2021reciprocity` (review timing on Airbnb) is the parallel timing-of-disclosure experiment, not cited by this paper. Leads outside the bib: Ge et al. 2016; Buell et al. 2016; Bertrand & Mullainathan 2004.

## Caution
A preprint of 2019; no pre-change baseline, so the paper cannot say the transparency change raised or lowered bias (§5.1). Driver characteristics could not be recorded under IRB limits, so the peak result rests on an MTurk driver survey. The rainbow filter is read by 42.5% of surveyed respondents as signalling LGBT membership and by 87% as support (§4), so the mechanism is not separated. One city, one platform, one route.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** Opened the SSRN-header manuscript (Indiana University repository copy; title, authors, 'History: September 20, 2019' match). Checked 5 quotations and about 30 numbers (3,200 rides, 1,600 per period, 3,189 drivers, 23.5 s, 3.1% vs 7.5%, odds ratios 2.60, 1.46, 0.54, 3.57, 0.45, 1.72, 0.66, 200 and 149 MTurk drivers, 42.5% and 87%), and the cited works.

**Findings:** Locator fix: the worse-off-for-minority-riders point and the no-pre-change-data limitation sit in section 5.1 (Limitations and Future Research), not 5; the first is the authors' conjecture, now flagged as such. All quotations and numbers match. 'the removed task relocates' and 'Arteaga' are the facet's/project's terms, not the paper's.
