# Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review, 28*(4), 1060–1092. https://doi.org/10.3758/s13423-020-01859-9

**Identifier:** doi:10.3758/s13423-020-01859-9 (PMC8965574) · **Read depth:** full_text (the published PDF with the journal's pagination, posted on the author's lab site, search.bwh.harvard.edu/new/pubs/Wolfe2021_GS6.pdf; the Springer and Europe PMC copies returned bot pages. I read the whole text from the abstract to the acknowledgements, pp. 1060–1085, including the simulation sections; Figs. 1–15 I saw only through captions and the text that describes them; the reference list I searched rather than read) · **Source-tier:** peer-reviewed article (theoretical review with a simulation) · **Evidence basis:** direct_read · **Design and sample:** none for the model; a simulation of 10,000 trials at each of five prevalence levels, set sizes 5–20 (p. 1077) · **Parties modeled:** other (a single observer searching a visual display) · **Facets:** H · **Read:** 2026-10-14

## What it argues

Guided Search 6.0 (GS6) is Wolfe's revision of his model of how people find a target among distractors. Attention can recognise only one or a few items at a time, so it must be "guided" to likely targets. In GS6 "there are five types of guidance that combine to create an attentional 'Priority Map'" (p. 1064): top-down and bottom-up feature guidance, retained from earlier versions, plus history (e.g. priming), value (reward), and scene structure and meaning. Selective attention goes to "the most active location in the priority map approximately 20 times per second" (abstract, p. 1060). The priority map is a weighted average of the sources of guidance and changes continuously (p. 1071).

Bottom-up guidance is the stimulus-driven part. In the GS2 summary, "Salience is based on coarse representations of a limited number of basic features like color, size, etc. Bottom-up is defined as 'stimulus-driven'" (p. 1063). GS6 qualifies it: "Bottom-up salience, for instance, may be a very powerful but short-lived form of guidance" (p. 1069). Scene guidance, not salience, is the addition Wolfe treats as most important (p. 1065). Spatial layout matters too: "Spatial relations are at least as important as featural relations in feature guidance" (p. 1067), and density makes targets easier to find.

GS6 adds the eccentricity of the visual field. Reading is Wolfe's example: "As you read this sentence, you need to fixate one word after another, because acuity falls off with distance from the fovea" (p. 1067). Preattentive processing may run in parallel "across large swaths of the visual field at the same time", but its results "will vary with eccentricity and with the structure of the scene" (p. 1068). Three functional visual fields (resolution, exploratory eye movements, covert attention) constrain search (pp. 1080–1082). Recognition is modelled as an "asynchronous diffuser": items "may be selected to enter the processing pipeline every 50–60 ms or so" while recognition is "a diffusion process taking > 150 ms/item" (abstract) or "several hundred milliseconds", so search is serial and parallel at once (pp. 1073–1074). Search ends when a quitting signal reaches an adaptive threshold (p. 1075).

Wolfe states the limit: "GS6 remains a model of a specific class of laboratory search tasks" (p. 1084), repeated searches for a target among distractors. Reading text as such is outside the model; it appears as an example of foveal limits and as a "reading-style" scanning strategy that gives search more memory (p. 1082).

## Relation to the argument

**Premise P5 (re-representation, perceptual work).** The draft uses GS6 to say that the visual system can do parallel spatial work that spacing exploits. The model supports a weaker form: basic features and spatial layout guide where attention and the eyes go next, and the page's geometry is the kind of stimulus structure that guidance uses. GS6 does not discuss word spaces, saccade targeting in reading, or lexical segmentation; that link comes from the reading literature the draft cites next (Rayner et al. 1998), not from Wolfe.

**What it complicates.** Two of the draft's phrases go beyond the source. "The visual system processes spatial structure across the field in parallel" ignores GS6's insistence that guidance falls off with eccentricity and crowding (p. 1068). And GS6 makes bottom-up salience one of five sources and a transient one (p. 1069), so "bottom-up feature salience guides the allocation of focal attention" is true but partial. The model's term is "selective attention", not "focal attention".

**Use in DRAFT_v2:**
- **Line 113** ("Under Wolfe's (2021) Guided Search model, bottom-up feature salience guides the allocation of focal attention"). Partly supported: bottom-up salience is one of five sources feeding the priority map that directs selective attention (pp. 1063–1064, 1069). The sentence omits the other four sources and the transience of salience (p. 1069). The preceding sentence ("The visual system processes spatial structure across the field in parallel") is not attributed to Wolfe but sits next to him; GS6 says parallel preattentive processing is limited by eccentricity and crowding (p. 1068). The following sentences on white channels, saccade targets and lexical segmentation are not in Wolfe; they need Rayner et al. 1998 and the eye-movement literature.

## In conversation with

- `rayner1998unspaced`: not cited by Wolfe; the draft pairs them. Rayner supplies the reading evidence that GS6 does not.
- `zhang1994representations`, `larkin1987why`: not cited by Wolfe; P5 combines them with perceptual guidance.
- Leads not in the bib (all cited in the paper): Treisman & Gelade 1980, feature integration theory (p. 1062); Wolfe 1994, Guided Search 2.0 (p. 1062); Itti & Koch 2000, saliency-based search (p. 1065); Henderson & Hayes 2017, meaning maps (p. 1070); Hulleman & Olivers 2017, the fixation-based alternative to GS (p. 1080).

## Caution

A model of laboratory visual search, by its author's own statement (p. 1084), with a simulation that omits the priority map (p. 1076) and eye movements (p. 1080). It is not a model of reading, and it cannot be cited for any claim about word spacing, saccade landing positions or reading rate. The copy read is the lab-hosted publisher PDF; I did not compare it with the PMC version.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Re-opened the writer's saved lab-hosted publisher PDF (33 pages, journal pagination 1060–1092), extracted it in reading order (the layout extraction interleaves the two columns) with page breaks, and located every quotation by journal page. Checked the simulation parameters, the stated limits of the simulation and of the model, every mention of reading, and the pages of the leads. Checked Crossref (Wolfe; *Psychonomic Bulletin & Review* 28(4), 1060–1092). Re-read DRAFT_v2.md line 113 and the reference at line 709.

**Findings:**
1. The diffuser timing was rounded: the paper says items "may be selected to enter the processing pipeline every 50–60 ms or so" (p. 1073) and models recognition as "a diffusion process taking > 150 ms/item" (abstract, p. 1060), "several hundred milliseconds" in the main text. Replaced with the exact wording.
2. Verified verbatim with correct pages: "approximately 20 times per second" (abstract, p. 1060); the GS2 salience summary (p. 1063); "five types of guidance ... 'Priority Map'" (p. 1064); scene guidance as "the most important of these" three additions (p. 1065); "Spatial relations are at least as important ..." and "As you read this sentence ..." (p. 1067); "large swaths ... vary with eccentricity and with the structure of the scene" (p. 1068); "very powerful but short-lived" (p. 1069); 10,000 trials at five prevalence levels, set sizes 5–20 (p. 1077); "Even without the priority map" (p. 1076); "Eye movements are not implemented in the simulation" (p. 1080); reading-style plans "effectively provide more memory" (p. 1082); "GS6 remains a model of a specific class of laboratory search tasks" (p. 1084). "Focal attention" does not occur in the paper, as the card says.
3. Leads verified: Treisman & Gelade 1980 and Wolfe 1994 (p. 1062), Itti & Koch 2000 (p. 1065), Henderson & Hayes 2017 (p. 1070), Hulleman & Olivers 2017 (pp. 1062, 1080–1082).
4. Read depth (full text, figures through captions) is consistent with the saved PDF.
5. Use in DRAFT_v2 (line 113): verdict stands. "Partly supported": bottom-up salience is one of five guidance sources and a short-lived one (pp. 1064, 1069); the model's term is selective attention; nothing in Wolfe concerns word spaces, saccade targets in reading or lexical segmentation.
