# Amin, R. M., Adatepe, A., Fernandes, D., Buschek, D., & Butz, A. (2026). Conversations in space: Non-linear LLM interaction in everyday use. arXiv:2605.15848.

**Identifier:** arXiv:2605.15848 · **Read depth:** full_text (arXiv v2, 15 Sep 2026; every page is stamped "Unpublished working draft. Not for distribution."; 18 pages, pagination is that PDF's; I read the whole text, including results and discussion, and skimmed the appendix tables and the reference list) · **Source-tier:** preprint / working draft · **Evidence basis:** direct_read · **Design and sample:** a formative interview study with 8 expert LLM users (3 UI/UX researchers, 5 developers), then a five-day field deployment of the authors' prototype, CanvasConvo, with 24 participants (17 men, 6 women, 1 non-binary; ages 21 to 54, M = 28.6), self-directed tasks, no control condition; interaction logs, SUS, NASA-TLX, Likert items and interviews · **Parties modeled:** person–system (one user and one LLM chat) · **Facets:** H · **Read:** 2026-10-13

## What it argues

Amin and colleagues build an interface that keeps a normal chat and adds a synchronised canvas: every message becomes a node, users can branch a conversation from any message, and a timeline links the two views (pp. 5–7). The formative study names three problems with linear chat: context fragmentation, iteration friction, and the "forking problem" (pp. 4–5). The field study asks how people take up the two views in their own work.

The findings sit in the abstract: "Participants selectively moved between the two views rather than replacing chat with the canvas", chat stayed central, and the canvas served "overview, revisitation, and exploration of alternatives" (p. 1). The logs back the split. Of recorded events, chat took 47.2%, canvas 28.3%, sidebar navigation 11.4% (p. 11). The 24 participants made 165 conversations and 1,225 messages (p. 11), 79 branches (M = 3.29 per participant; p. 12), 132 timeline clicks and 881 canvas zooms (p. 12). Mean SUS was 78.9 (SD 11.2, range 56.7 to 94.4; p. 11). On 7-point items, 91% agreed they could guide the system and 96% agreed they could revisit earlier content, while ownership of ideas drew 65% agreement and 22% disagreement (Figures 4–5, p. 11).

The adoption was uneven. P19 "just scrolled up... I never ended up using the canvas due to force of habits" (p. 9); P20 found switching between views "confusing" (p. 10); P23 did not know "what the branch knows and what it doesn't know" (p. 10). The authors conclude that transitions between representations and the visible state of the conversation matter, "not simply exposing additional structure" (p. 13).

They flag what the data cannot show. Canvas sessions lasted longer (mean 34.1 minutes against 13.0 for chat), but the logs record wall-clock time and cannot separate "sustained organization" from "lower interface familiarity"; a controlled within-participant study would be needed (p. 12). They also list a short deployment and an experienced-user sample as limits (p. 12).

## Relation to the argument

**Ruling D7 and the argument map's third exposure.** The author's D7 says understanding is becoming something done through deciding and quickly taking in results, and the map's exposure 3 says the engagement layer collides with P8. Amin gives a small piece of dyadic evidence on how people use structure: they do not give up the fast chat loop, and they reach for the spatial overview when a task has grown long. That is consistent with D7's emphasis on acting and ingesting results, and it shows no sign that an overview replaces the loop. It does not touch the coordination case, since there is one user and one model, and no counterpart.

**Premise P9.** The prototype is an aid the person reads and works. The paper shows uneven uptake and good subjective ratings, with no measure of task quality, accuracy or speed. It adds one more entry to the "aids to read or tune" family with perception-only outcomes, which is the weakness the map already notes for that family ("mostly satisfaction measures").

**Premise P5.** The discussion leans on Kirsh (2010), "Thinking with external representations", to say that externalising work into manipulable representations supports reasoning (p. 13). That is the same family as the project's external-representation sources, but the paper tests nothing about it directly.

**Facet check:** the facet's reading (canvas plus chat, five-day deployment, 24 participants, "Adoption was uneven", chat stayed central) matches the text. I add that the status is a working draft marked not for distribution.

## In conversation with

- `suh2023sensecape` — cited as Sensecape [31], a hierarchical workspace for exploration and sensemaking, in the related work and in Table 1 (pp. 3–4).
- `shneiderman1983direct` — listed as reference [28] and cited in the discussion for moving between overview and detail (p. 13). The design goals instead cite Shneiderman's 1996 mantra [29] (p. 5).
- `buschek2024collage` — shares an author (Buschek) with this paper, but this paper does not cite it; I searched the text for "Collage" and found nothing.
- Not in the bib, as leads: Masson et al. (2024), DirectGPT; Zamfirescu-Pereira et al. (2023), "Why Johnny can't prompt"; Kirsh (2010); Pirolli & Card (2005) on sensemaking; Li et al. (2026), Branchat.

## Caution

A working draft, five days, 24 mostly experienced and young participants, a prototype built by the authors, no control group, and mostly self-report plus telemetry that the authors themselves treat cautiously. Do not cite it for a performance benefit of non-linear interfaces, and do not cite it as peer-reviewed.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened arXiv:2605.15848v2 PDF (15 Sep 2026, 18 pp., 'Unpublished working draft' stamp present); checked 8 quotations with page locators (page-wise extraction) and about 30 numbers (47.2/28.3/11.4% events; 165 conversations, 1,225 messages; 79 branches M=3.29; 132 clicks; 881 zooms; SUS 78.9, SD 11.2, 56.7-94.4; Likert 91/96/65/22%; 34.1 vs 13.0 minutes; demographics 17/6/1, age 21-54 M=28.6; 8 formative participants, 3 UI/UX), plus Sensecape, Shneiderman [28], Kirsh [13] citations; searched for Collage (absent).

**Findings:** No issues found. Not checked line by line: the appendix tables and the reference list, which the card says it only skimmed; the card's Read depth line is honest about that.
