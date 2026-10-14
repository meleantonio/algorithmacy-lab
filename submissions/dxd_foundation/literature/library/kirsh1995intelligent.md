# Kirsh, D. (1995). The intelligent use of space. *Artificial Intelligence, 73*(1–2), 31–68.

**Identifier:** doi:10.1016/0004-3702(94)00017-U · **Read depth:** full_text, but of the author's web version, not the journal article. The page (interactivity.ucsd.edu/articles/Space/AIJ1.html, saved as `kirsh1995intelligent.html`) says: "This article in a slightly revised form appeared in Artficial Intelligence 1995. Received September 1992. Revised June 1993." It carries no journal page numbers, so locators are section headings. It cites Kirsh & Maglio and Hutchins as "in press" and Agre as "forthcoming", so it predates the printed article. I could not compare it with the journal text and do not know what the "slight" revisions are. I read the abstract, introduction, all four main sections, conclusion, summary table and reference list; the ten figures were read through their captions only (the images are not in the saved file) · **Source-tier:** peer-reviewed article (web version of the author) · **Evidence basis:** direct_read · **Design and sample:** a taxonomy built from videotapes of cooking, assembly and packing, informal observation in supermarkets, workshops and playrooms, and Kirsh & Maglio's Tetris experiments; no sample sizes or statistics are given for the observations · **Parties modeled:** person–workspace (one expert agent arranging its own surroundings; other agents appear at the edges) · **Facets:** E · **Read:** 2026-10-13

## What it argues

Kirsh offers "the beginning of a principled classification of some of the ways space is intelligently used" (Abstract), in three classes: arrangements that simplify choice, arrangements that simplify perception, and spatial dynamics that simplify internal computation. His stance: "Space is a resource that must be managed, much like time, memory, and energy" (Introduction). Four assumptions frame the work: the agents are experts; experts find enough information locally to avoid on-line planning; experts "partially jig" or informationally structure the environment; and human work environments are already pre-structured (§"How to Think About Everyday Activity"). A jig can be informational (cues that change what the agent perceives) or physical (constraints that change what the agent can do); Kirsh's focus is the informational kind (same section).

**Choice** (§"Using Space to Simplify Choice"). Five cases: production lines hide affordances; blocking cues prohibitions (a door jam, a rag on a hot pipe); arrangements draw attention to affordances (grocery baggers cluster fragile, heavy and upright items); space encodes temporal order (parts laid out in assembly sequence); space encodes where a part goes (a desk's panels laid out as the data for a "simple assemblage program"). He adds that an informational arrangement "achieves nothing that could not equally well be achieved by asking an oracle" (same section, "Pre-structured environments").

**Perception** (§"Spatial Arrangements That Simplify Perception"). The text the facet quoted is here: "Perhaps the most obvious way of simplifying perception is to arrange objects in space so that they form equivalence classes, or partitions, that reflect relevant preconditions, or properties that are useful to track, notice, or exploit" (§"Clustering To Categorize"). Washed and unwashed tomatoes are kept apart: "By segregating the two groups we highlight their differences." The section goes on to the Gestalt factors that make a group (proximity, similarity, common fate, good continuation, surroundedness), with a bicycle repairer's sheet of newspaper as a region; to symbolic marking (a knife laid on the measured half of a butter stick); and to "vernier" grouping, where sorting jigsaw pieces into coarse piles lets the player see finer differences, cutting search "from O(N) to O(log N)".

**Computation** (§"Saving Internal Computation"). Tetris players rotate pieces on screen to save mental rotation: "mental rotation of tetrazoids takes between 1000 and 1800 ms; physical rotation can take place in 200 ms" (§"High Speed Offloading"). Figure 10's caption gives external rotation "as fast as 150 ms", internal "five to ten times as long", which does not match the text. The section closes on externalised representations: after Chambers & Reisberg, people cannot find the ambiguity in a mental image of a duck/rabbit but can in their own drawing of it.

**Chunking.** In the introduction Kirsh contrasts KXTNJQXTARWOYE with IBMCIANBCDARPA, which readers chunk into IBM CIA NBC DARPA, and notes that "experimentalists rarely allow the subject to play with the stimulus itself to highlight the chunks". In the conclusion he writes that one puts "a much smaller strain on Working Memory if we manage the environment so that the stimulus we see is chunked as in PET TAPE APPLE SOCRATES" (the web file garbles the sentence that precedes this clause). Of costs he says the examples matter "not how much they reduce computation -- for that we cannot meaningfully estimate -- but how easily they reduce it" (§"A word about complexity analysis").

## Relation to the argument

**Premise P5 and the problem-2 vocabulary.** Kirsh gives the closest cognitive-science description of what a gap between words does: a partition that makes equivalence classes visible and cuts the cost of search and recognition, and a way to preprocess a stimulus so the reader's chunking is done in the world. Nothing in the text mentions reading, writing, script or word boundaries. The match is by function, as with Zhang & Norman.

**Facet check:** the facet reads Kirsh's agent as arranging its own workspace and the scribe as arranging another's, and treats this as a gap in fit. Kirsh's text is less sharp than that. He says arrangements cue "cognitive events or processes in himself or herself, or another agent", and his example is supermarket managers who bias "consumer choice" with displays; his fourth assumption says work environments are pre-structured by others for the agent. So an arrangement made by one party for another is inside Kirsh's frame. The supermarket case is also one in which the arranger's interest differs from the shopper's, which touches **P10** and ruling D8, though Kirsh does not draw that out. The facet's quotations match the web text exactly.

**Cue against constraint (my inference, not Kirsh's).** His split between informational jigs (cues) and physical jigs (constraints), and his oracle test, line up with the argument's contrast between aids that give the person something to read and rules in the mediator that remove a task (**P8, P9**; rulings D3, D4). Kirsh's text supports only the distinction itself.

**Limits for the argument.** His agents are experts, and he warns that "how an expert might store information in arrangements may not be evident to novices" (Introduction), a caution for any claim about learners. He also declines to quantify the savings, which limits any use of the paper for **H-cost** numbers.

## In conversation with

- `kirshmaglio1994distinguishing` — cited as "in press" for the Tetris studies and epistemic action; the blocks-world passage already uses the term "external epistemic actions".
- `larkin1987why` — cited in the references; the conclusion remarks that "diagrams facilitate problem solving".
- `hutchins1995cockpit` — "Hutchins in press (a)", cited for the idea that agent and environment can form one computational system.
- `hutchins1995cognition` — "Hutchins, E. (in press b). Cognition in the Wild" (MIT Press).
- `kirsh1996adapting` — listed under "Other Articles" on the page; the text does not cite it.
- The reference list does not cite `zhang1994representations`. Rasmussen (1980, 1986) and Reason (1990) appear, but those editions differ from the bib's `rasmussen1983skills`, `rasmussen1989coping` and `reason2000human`, so I record no match.

Leads not in the bib: Chase & Simon (1973); Chambers & Reisberg (1985); Gibson (1977); Norman (1988); Agre & Chapman (1987).

## Caution

This is the author's web version, so check any quotation against the journal text and take its page numbers from there. The observations are anecdotal and unquantified; the one experimental thread (Tetris) belongs to Kirsh & Maglio, and the text and a figure caption disagree on the external rotation time (200 ms against 150 ms). The paper is about experts' own workspaces and has no data on readers, text or learners.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The saved web page (interactivity.ucsd.edu AIJ1.html, text extracted; it is the author's web version, not the journal text, as the card says). About 35 quotations and section headings, the Tetris timings (1000-1800 ms mental, 200 ms physical in the text; 150 ms and "five to ten times" in the Figure 10 caption, 800-1800 ms burst), the chunking strings, the butter-knife, bicycle-newspaper and oracle passages, and the reference-list entries for Hutchins (in press a and b), Larkin & Simon 1987, Rasmussen 1980/1986, Reason 1990, Chambers & Reisberg 1985.

**Findings:** One citation-form fix: the card put "Hutchins in press (b), Cognition in the Wild" in quotation marks, but the reference list reads "Hutchins, E. (in press b). Cognition in the Wild"; corrected. Everything else matches, including the 200 ms vs 150 ms discrepancy between text and caption. The Read depth line is honest (figures read through captions only). Zhang & Norman is indeed absent from the reference list.
