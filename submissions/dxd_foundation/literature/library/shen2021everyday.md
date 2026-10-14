# Shen, H., DeVos, A., Eslami, M., & Holstein, K. (2021). Everyday algorithm auditing: Understanding the power of everyday users in surfacing harmful algorithmic behaviors. *Proceedings of the ACM on Human-Computer Interaction, 5*(CSCW2), Article 433, 1–29. https://doi.org/10.1145/3479577

**Identifier:** doi:10.1145/3479577; arXiv:2105.02980 · **Read depth:** full_text (arXiv v2 of 24 August 2021, which carries the CSCW2 article header and pagination 433:1–29; read whole, including Table 1 and the reference list; Figure 1 seen through its caption) · **Source-tier:** peer-reviewed article (CSCW journal track) · **Evidence basis:** direct_read · **Design and sample:** exploratory case study: 15 cases of user-driven auditing gathered from news and social media, four analysed in depth (Twitter image cropping, racial and gender; Yelp review filtering; Booking.com rating), from discussion threads, news and prior research · **Parties modeled:** two parties + third party in two cases (Yelp businesses and reviewers; Booking.com guests and hotels, each through the platform's algorithm); person–system in the Twitter cases · **Facets:** R4 · **Read:** 2026-10-14

## What it argues

Shen and colleagues name "everyday algorithm auditing": "a process in which users detect, interrogate, and understand problematic machine behaviors via their daily interactions with algorithmic systems" (p. 2). Drawing on Suchman, they treat these practices as "situated actions in which everyday users encounter problematic machine behaviors via their routine interactions with algorithmic systems, then adjust their behaviors to understand and act on what they encountered" (p. 5). Audits move through initiation, awareness raising, hypothesising and testing, and remediation (§6, pp. 16–19).

The cases show users probing algorithms by acting. Twitter users tested the cropping algorithm by posting images that swapped positions, tie colours, backgrounds and skin tones (pp. 11–12). Yelp business owners tested whether filtering followed refusals to advertise, and reviewers visited businesses to see whether their reviews would show; "These conjectures were often based on users' folk theories about how the filtering algorithm operated and not on concrete data" (p. 15), and of the almost 700 lawsuits that followed, all "were ultimately unsuccessful" (p. 15); the authors add that "the Yelp case was ultimately dismissed due to the lack of scientific evidence" (p. 16). Booking.com users found by trying inputs that the lowest computable score was 2.5, and the platform later changed it to 1 (pp. 15–16). On folk theories: "These theories, regardless of their validity, shape user behaviors and inform how they act around a system" (p. 17). The authors argue audits work best "when audits are conducted collectively" (p. 3) and propose design supports: community, expert, algorithmic and organisational guidance, and incentives (§7). They call the work "highly exploratory" (p. 25).

## Relation to the argument

**Ruling D7 and premise P9.** The paper is a close neighbour of the draft's §5.2. It already describes people learning an opaque algorithm by acting through it, in Suchman's terms, and doing so collectively, with collective sensemaking credited to Weick (1995) (p. 9). That supports the draft's claim that learning a mediator is "social as well as enacted" (line 266). It also narrows the novelty claim on the same line ("extending Kirsh and Maglio's concept to them is this paper's move"): the extension to epistemic action may be new, but the phenomenon is documented and theorised. I did not find epistemic action in this paper.

**Line 283 (folk theories as a symptom of failure).** The paper treats folk theories as the working hypotheses of successful audits, not only as a fallback. The Yelp case shows the risk the draft names (theories not checked against data); the Booking.com and Twitter cases show folk theories leading to correct findings and to platform change.

**Use in DRAFT_v2:** This paper is not cited in DRAFT_v2.md (grep "Shen", "Eslami", "auditing": no hits in the paper body or references). The lines below are where the draft makes claims this source bears on.
- Line 266 (workers form theories from the system's responses to their moves and trade them in forums; "Learning a mediator is social as well as enacted"): supports (pp. 11–17).
- Line 266 ("extending Kirsh and Maglio's concept to them is this paper's move"): narrows. User probing of algorithms is already theorised as situated action and collective sensemaking (pp. 5, 9); the epistemic-action framing is not.
- Line 268 ("These probes are epistemic actions designed to extract information from an opaque mediator"): supports in substance; the paper's term is hypothesis testing (§6.3).
- Line 283 ("The user is left relying on folk theories and defensive gaming"): complicates. Folk theories were the starting point of audits that found real bias and changed platforms (pp. 15–19); in the Yelp case they were unsupported (p. 15).

## In conversation with

- `eslami2016first` — cited for folk theories and seamful design (pp. 17–18).
- `weick1988enacted` — not cited; the paper cites Weick (1995), *Sensemaking in Organizations*, for collective sensemaking (p. 9).
- `ehsan2024seamful` — not cited; the seamful-design line the paper draws on via Eslami et al.
- `bucher2020pacifying`, `kellogg2020algorithms` — not cited; worker-side accounts of algorithmic resistance.
- Not in the bib, as leads: DeVito et al. (2018), "How people form folk theories of social media feeds"; Eslami et al. (2019), "User attitudes towards algorithmic opacity and transparency in online reviewing platforms"; Eslami et al. (2017) on Booking.com ratings; Velkova and Kaun (2019), "Algorithmic resistance"; Sandvig et al. (2014), "Auditing algorithms".

## Caution

Cases were chosen for visibility and data access, not sampled; accounts rest on public threads and news. The focus is harmful bias, not the everyday task of transacting well through a mediator. No measure of how many users probe or how accurate their theories are.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the writer's saved copy (dxd_foundation_local/pdfs/r4c/shen2021.pdf, arXiv:2105.02980v2, 24 Aug 2021, with the CSCW2 article header and pages 433:1–29) and extracted it page by page, confirming each page from its printed number. I matched all seven quotations word for word with their pages (2, 5, 15, 16, 17, 3, 25). I checked the 15 cases (Table 1, p. 6; p. 10); the Twitter tests, including the swapped ties and the skin tones (pp. 11–12); "almost 700" lawsuits (p. 15; "close to 700", p. 18); the Booking.com 2.5 floor and the change to 1 (pp. 15–16); Weick (1995) as [95] for collective sensemaking (p. 9); Eslami et al. [27] on folk theories and seamful design (pp. 17–18); and the stage structure of §6 (pp. 16–19). I confirmed that the paper never uses "epistemic action" or cites Kirsh. I checked the record against Crossref (PACMHCI 5(CSCW2), 1–29, four authors, DOI) and re-read DRAFT_v2.md lines 266, 268 and 283.

**Findings:**
1. The card said the roughly 700 Yelp lawsuits "were dismissed 'due to the lack of scientific evidence' (p. 16)". The paper says the lawsuits "were ultimately unsuccessful" (p. 15). The dismissal for lack of scientific evidence is said of "the Yelp case" (p. 16). Corrected so that the quotation is attached to what it describes.
2. "Use in DRAFT_v2" did not say the source is uncited; I added that statement. The four verdicts (lines 266 ×2, 268, 283) stand on re-reading.
3. The other quotations, the page locators, the reference record and the full-read claim (arXiv v2 with the journal pagination) all check out.
