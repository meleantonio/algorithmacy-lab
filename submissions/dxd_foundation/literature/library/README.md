# Contextual bibliography — card library

*Built 2026-10-13 at the author's request. Agent-written; the author has not reviewed the cards, and
none of the text is his.*

One card per source, `<bibkey>.md`, keyed to `../references.bib`. A card exists only where an agent read
the full text of the source in the session that wrote it. Sources reachable only as an abstract, a
snippet or a preview have no card and stay in the facet files with their read status. Full texts are
kept outside this public repo; a card quotes in short passages with locators.

## Card format

```
# <Full reference in APA form>

**Identifier:** doi/arXiv/URL · **Read depth:** full_text (which version: published PDF, accepted
manuscript, preprint vN, working paper; say if pagination is the journal's) · **Source-tier:**
(peer-reviewed article / proceedings / working paper / preprint / report / statute / book chapter) ·
**Evidence basis:** direct_read · **Design and sample:** (method, N, setting; "none" for a position
piece) · **Parties modeled:** (person–artefact / person–system / two parties + third party / other) ·
**Facets:** (letters of the facets that cite it) · **Read:** 2026-10-13

## What it argues
The claim, the method and the main results, with exact quotations and page or section locators, and
every number given with its unit, comparison and N.

## Relation to the argument
What the source supports, complicates or refutes in this paper's argument: the word-separation
precedent, the author's ten rulings (`../../SOURCE.md`), and the premises in `../../ARGUMENT_MAP.md`.
Name the ruling or premise. Say plainly when the source cuts against the author.

## In conversation with
The contextual bibliography proper: works in `../references.bib` that this source cites, answers or is
answered by, each with its bib key and one line on the relation, taken from the source's own text or
reference list. Then up to five works it leans on that are not in the bib, as leads.

## Caution
What the source cannot be cited for: limits of design, sample, date, version read, and any difference
between this version and the version of record.
```

A second agent then appends `## S2 adversarial verification (date)` with a verdict (confirmed /
corrected / could not verify), what it checked and what it changed.

[`INDEX.md`](INDEX.md) lists the cards by facet with their verification status.
