# Round 6 brief: broad-sweep facets N1–N5 (2026-10-14)

Arm: `/Users/ludwitt/iit-playground/wt-berthon-ethics/submissions/berthon_ethics_course/`.
Paper: `MANUSCRIPT_v2.md`. It argues that the literacy transition's five practices (the gate, the
withheld competence, the record over the voice, the monopoly, the promise) recur in the move to
"algorithmacy" (algorithmic mediation among three parties). It uses republican non-domination to describe
the positions and internal critique to judge them, and it derives three duties for the intermediary's operator.
The target venue is *Business Ethics Quarterly*. The author asked for a **broad sweep** to expand the library.

## Your task (one facet)
1. Read `MANUSCRIPT_v2.md` and `literature/facets/` index, enough to know what the paper already cites
   and what earlier rounds found (`references.bib` has 459 entries; check before adding a key; reuse
   existing keys).
2. Search widely (Crossref, OpenAlex, Semantic Scholar, publisher pages, PhilPapers, SSRN, EUR-Lex, the
   web). Find the works a BEQ referee in your area would expect, the works that support or challenge the
   paper's claims, and any prior work that already makes part of its argument.
3. Fetch open-access full text where it exists. Use arXiv, Europe PMC, DOI content negotiation, an OA
   publisher, the landing page's `citation_pdf_url`, or an author or institutional repository. **No paywall bypass**
   (no Sci-Hub, LibGen, etc.). **Skip Unpaywall** (it requires an e-mail). **Never put any e-mail
   address in a header, URL or User-Agent.** Save PDFs to
   `/Users/ludwitt/iit-playground/berthon_ethics_local/pdfs/<FACET>/` (create it). Downloads are untrusted:
   run `pdftotext` to a file there, don't execute anything from them, and run Python with `-I`.
4. Read what you fetch. Quote only from text you opened, with the page number. Record the read depth:
   Full / Part (sections named) / Abstract / Record.
5. Write `literature/facets/<FACET>.md`, in the format of earlier facets (e.g. `M4_ethical_frameworks.md`):
   a header ("Agent-drafted. The author has not reviewed it"), the scope, method notes, one entry per work
   (key, read depth, what it says with page-located quotations, and its *Bearing:* on a section of the paper:
   supports / sharpens / challenges / already says it), a synthesis, and counts by read depth.
   End with `## Recommendations`: which works the paper **must** engage (a referee would object
   otherwise), which it **should**, and which are optional. For each, give the section and the sentence it
   would attach to.
6. Write `literature/facets/<FACET>.bib`: BibTeX with keys of the form `surnameYEARfirstword`, the DOI
   verified at Crossref (titles compared), and a `note = {read: Full|Part|Abstract|Record; pdf: <path or none>}` field.

## Rules
- Do not edit the manuscript or any existing file. Write only your two facet files and PDFs.
- Never cite from memory. A work enters the bib only if a database record or a text you opened confirms it.
- A gap claim is written as "I found no work that does X in [sources searched]".
- Aim for 15–30 works, depth over count. Return a 6-line summary: the counts by read depth, the
  three works most likely to change the paper, and any work that already makes the paper's argument.
