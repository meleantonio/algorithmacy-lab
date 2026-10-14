# Pucci, E., Piro, L., & Matera, M. (2027). From tabbing to talking: LLM-driven conversational agents for web form interaction. *International Journal of Human-Computer Studies, 218*, Article 103925. https://doi.org/10.1016/j.ijhcs.2026.103925

⚠ Not read in full.

**Identifier:** doi:10.1016/j.ijhcs.2026.103925 · **Read depth:** partial: Crossref record (title, authors, volume 218, article number 103925, issue date February 2027, CC BY 4.0 licence on the version of record from 4 September 2026) and the abstract as reconstructed from OpenAlex's inverted index (W7208815650). The article is open access (hybrid, CC BY), but the ScienceDirect HTML and PDF returned a Cloudflare block page to curl and HTTP 403 to WebFetch, and the Politecnico di Milano repository search returned a Cloudflare challenge; I did not try to get past either. No arXiv preprint was found. · **Source-tier:** peer-reviewed article · **Evidence basis:** abstract only · **Design and sample:** human-centred design study: guidelines analysis, stakeholder consultations, prototyping, and a study with 18 blind and visually impaired (BVI) participants using an LLM-driven conversational agent to fill in web forms (abstract) · **Parties modeled:** person–system (a BVI user, a conversational agent, a web form) · **Facets:** cited in §2 (in-flow scaffolding) · **Read:** 2026-10-14

## What it argues

From the abstract only. Web forms are hard for BVI users even with accessibility standards; screen-reader workflows are "frustrating and error-prone." The authors ask how LLM-driven conversational agents can make form filling accessible by voice, covering "data entry, navigation, and input verification." In the 18-participant study, participants "valued the system's intuitiveness and reliability but highlighted tensions around verbosity, pacing, and control." The authors derive design patterns that turn abstract voice-interaction guidelines into concrete strategies for conversational form filling.

I could not see the patterns, the study tasks, any measures, or what the paper says about error correction.

## Relation to the argument

**Ruling D3 and P8.** The study is about accessibility, not disclosure or mediated decisions. Its relevance is narrow: a conversational interface that replaces tabbing through a form is a re-representation of the same task (P5), aimed at a group for whom the original representation required skill. That rhymes with the spacing precedent, but the paper does not frame it so, and with one person and one form it is not a triad.

**What it shows on the abstract.** Participants raised "verbosity" and "pacing" as tensions, which is consistent with the draft's claim that long explanatory turns cost the user. Whether the paper recommends economy or discoverable error-correction is not visible in the abstract.

**Use in DRAFT_v2:**
- **Line 39** ("Dialogue systems similarly depend on economy in interaction and discoverable error-correction rather than lengthy explanatory turns (Pucci, Piro, & Matera, 2027)"). Partly supported on the abstract: verbosity was a tension participants named, and "input verification" was a function studied. "Discoverable error-correction" and "rather than lengthy explanatory turns" could not be checked. The scope is narrower than the sentence: the paper studies LLM conversational agents for web form filling with 18 BVI participants, not "dialogue systems" in general. The paragraph places it under "in-flow friction and situated scaffolding", as its last sentence after Buçinca et al. (2021), Disley and Khan (2026) and Horvath et al. (2022) (S2 precision); nothing in the abstract concerns friction against over-reliance. Recommend opening the article (it is CC BY) before keeping the sentence, and narrowing it to "for blind and visually impaired users filling web forms."
- Also listed in the change log (line 773) among sources "confirmed at Crossref, texts not read"; that remains true.

## In conversation with

- No bib work could be confirmed as cited, since the reference list was not seen.
- Related work by the same group (from search results, not opened): Piro, Di Fede, Pucci, Tolomeo & Matera, "Leveraging LLMs for voice-based form filling on the Web: The ConWeb approach" (ICWE 2025 demo); Pucci et al., "Speaking with LLMs: Co-designing voice interaction patterns with blind and visually impaired users" (*International Journal of Human–Computer Interaction*, details unconfirmed).

## Caution

Abstract only. Small qualitative-design sample (18 BVI participants). Dated 2027 by issue (February 2027, vol. 218); the licence date suggests online publication in September 2026, so the year in the reference entry is correct for the issue but the article was available in 2026. A dyadic accessibility study; do not cite it for triads, disclosure or algorithmacy.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Tried the open routes again. OpenAlex (W7208815650) and its best_oa_location point only to the ScienceDirect PDF, which returned HTTP 403 with a block page to curl; the files the writer saved as `r4_50/pucci2027.pdf` and `pucci.html` are that same 832,805-byte block page, not the article. Europe PMC and OpenAIRE have no record; arXiv showed nothing. I did not try to get past the block. I re-checked the Crossref record (authors Emanuele Pucci, Ludovica Piro, Maristella Matera; vol. 218; article 103925; issued February 2027; CC BY 4.0 on the version of record from 2026-09-04; copyright "© 2026 The Author(s)"). I reconstructed the abstract from OpenAlex's inverted index and checked every quoted phrase in the card against it. I re-read DRAFT_v2.md lines 39 and 773.

**Findings:**
1. Reference record, licence dates and abstract quotations ("frustrating and error-prone", "data entry, navigation, and input verification", "valued the system's intuitiveness and reliability but highlighted tensions around verbosity, pacing, and control", 18 BVI participants) all match. OpenAlex gives the online date as 2026-09-05.
2. The card said the paragraph places the source "after Buçinca et al." It is the paragraph's last sentence, after Buçinca et al., Disley and Khan, and Horvath et al. Wording made precise; the verdict is unchanged.
3. Use in DRAFT_v2, line 39: the verdict stands. The abstract supports "verbosity" and "pacing" as tensions and input verification as a function studied. "Discoverable error-correction" and "rather than lengthy explanatory turns" cannot be checked from the abstract. The claim about "dialogue systems" in general is wider than the paper's scope.
4. Read depth (abstract only, ⚠ Not read in full) is accurate.

