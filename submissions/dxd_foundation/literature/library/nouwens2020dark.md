# Nouwens, M., Liccardi, I., Veale, M., Karger, D., & Kagal, L. (2020). Dark patterns after the GDPR: Scraping consent pop-ups and demonstrating their influence. In *Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems* (pp. 1–13). ACM. https://doi.org/10.1145/3313831.3376321

**Identifier:** doi:10.1145/3313831.3376321; arXiv:2001.02479 · **Read depth:** full_text (arXiv v1, 8 January 2020, 13 pages in the CHI two-column format with the CHI '20 copyright block; I read the whole paper, Tables 1–2 and the reference list, and saw Figures 1–3 only through captions; the ACM version of record was not opened, so the text may differ from the published version in small ways; locators are section names) · **Source-tier:** proceedings (read as preprint) · **Evidence basis:** direct_read · **Design and sample:** Study 1: a scraper over the top 10,000 UK sites (Alexa), September 2019, finding 680 sites with one of the five largest consent-management platforms. Study 2: a field experiment with a Chrome extension injecting eight pop-up designs into participants' own browsing; 48 finished, 8 removed, N = 40 US residents (mean age 26.1, mostly university-educated); two within-subject Latin-square experiments, four answers per design, 1,280 answers · **Parties modeled:** two parties + third party (a website, the user, and the CMP vendor and regulator) · **Facets:** L · **Read:** 2026-10-14

## What it argues

Nouwens and colleagues measure how common unlawful consent designs are and how much design moves consent. Study 1: only 11.8% of the 680 sites met three minimal legal conditions (explicit consent, rejecting as easy as accepting, no pre-ticked boxes); 50.1% had no "reject all" button; 32.5% used implied consent; the median site listed 315 vendors, whose descriptions average 7,985 words, "roughly 31.9 minutes of reading" (Study 1, Results).

Study 2. Notification style (banner or barrier) did not change consent, though banners were ignored more often. "Removing the 'reject all' button from the first page increased the probability of consent by 22−23 percentage points": slope 0.220 for barriers (95% CI 0.149 to 0.290, R² = 0.117) and 0.231 for banners (R² = 0.135) (Study 2, "Button prominence"). Showing more granular choices on the first page cut consent by 8.8 to 20.0 points (Table 2). Only 17 of 1,280 answers (1.3%) were a specific selection of purposes or vendors; 93.1% of interactions stayed on the first page; "anything not immediately visible to the user, anything requiring interaction to access, might as well not exist" (Study 2, "General interaction patterns"). Most participants said their answers did not match their ideal settings and blamed the interface (Participant strategies). The authors call for enforcement against CMP vendors and for binding browser-level settings (Discussion).

## Relation to the argument

**Ruling D3 and premise P8.** The study holds the information on offer fixed in one sense (the same options exist on the second page) and shows that where an option sits decides behaviour. That supports the draft's turn from text to the structure of the interface. It also shows the structure working against the user: the website and the CMP vendor are interested parties who set the layout, which is premise P12 in miniature.

**Ruling D8 and premise P12.** The authors' remedy is legal force on the vendor and binding browser settings, not better notices, which fits the draft's argument that conventions bend toward the weaker party only under outside force.

**Use in DRAFT_v2:**
- Line 176 ("Nouwens et al. (2020) demonstrated in cookie consent interfaces that layout alone moves behavior: removing the opt-out button from the first page raised consent by 22 to 23 percentage points"): supported (Study 2, "Button prominence"; abstract uses "opt-out button"). "Layout alone" is slightly loose: removing the button also raised the clicks needed to reject, so the manipulation changes effort as well as layout. The sample is 40 young, mostly university-educated US residents.
- Line 643 (reference entry): matches Crossref.

## In conversation with

- `utz2019informed` — Utz et al. (2019), summarised in Related Work: at least 57.4% of CMPs use dark patterns; acceptance rose from 0.16% to 83.55% with preselected options.
- `gray2018dark` — Gray et al. (2018), cited for the term "dark patterns".
- `mathur2019dark` — not cited here; the companion large-scale dark-patterns crawl.
- `obar2018biggest` — Obar & Oeldorf-Hirsch, cited on unread privacy policies (ref. 43).
- `kelley2009nutrition` — cited for the privacy "nutrition label" (ref. 34).
- Not in the bib, as leads: Matte, Bielova & Santos (2020) on consent signals; Degeling et al. (2019); Jensen & Potts (2004); Forbrukerrådet, *Deceived by Design* (2018).

## Caution

Forty participants recruited through personal networks and a computer-science mailing list, all in the US, answering EU-style pop-ups; order effects not fully controlled; exposure counts varied (Study 2, Limitations). The banner regression reports a 95% CI of 0.163 to 0.230 around a slope of 0.231, an internal error in the preprint; the barrier figure (0.149 to 0.290) is coherent. Scraper results are a ceiling on compliance and cover five vendors on UK sites.

## S2 adversarial verification (2026-10-14)

**Verdict:** confirmed

**What I checked:** I re-opened the arXiv v1 PDF and text the writer saved (dxd_foundation_local/pdfs/R4/nouwens2020_arxiv.pdf, 13 pages, "arXiv:2001.02479v1 [cs.HC] 8 Jan 2020") and read Study 1, Study 2, Limitations and Discussion. I checked every number (680 of the top 10,000 UK sites, five CMPs; 11.8%; 50.1% without "reject all"; 32.5% implied consent; median 315 vendors; mean 7,985 words, 31.9 minutes; 48 finished, 8 removed, N = 40, mean age 26.1, US residents; Latin-square designs, four answers per interface, 1,280 answers; slopes 0.220 [0.149, 0.290], R² = 0.117 and 0.231 [0.163, 0.230], R² = 0.135; Table 2 −0.088, −0.200, −0.119; 17 of 1,280; 93.1%), the quotations ("22−23 percentage points", "might as well not exist") with their section names, the recruitment and limitations, the Discussion's remedies (enforcement against CMP vendors; legally binding browser settings), and the record against Crossref (CHI 2020, pp. 1–13, five authors). I re-read DRAFT_v2.md lines 176 and 643.

**Findings:**
1. No errors found. The internal inconsistency the card flags in the banner regression (a 95% CI of 0.163 to 0.230 around a slope of 0.231) is in the preprint as stated.
2. Use verdict for line 176 confirmed: the 22–23 point figure and the "opt-out button" wording are the paper's (abstract; Study 2, "Button prominence"); the card's caveat that removing the button changes effort as well as layout is a fair reading, since the reject option moved to a second page.
