# Erickson, T., & Kellogg, W. A. (2000). Social translucence: An approach to designing systems that support social processes. *ACM Transactions on Computer-Human Interaction, 7*(1), 59–83.

**Identifier:** doi:10.1145/344949.345004 · **Read depth:** full_text (published PDF, journal pagination, pp. 59–83, including the reference list and figure captions) · **Source-tier:** peer-reviewed article, design-framework paper with a prototype · **Evidence basis:** direct_read · **Design and sample:** conceptual framework illustrated with everyday anecdotes; one prototype (Babble) that its implementers used daily "for two years" and that ran in about eight other groups "for periods of two to six months," mostly small groups whose members knew one another (pp. 73–74); no controlled test, no N · **Parties modeled:** other: groups of people communicating through a system (many-to-many), with the system as the medium, not an agent with its own aims · **Facets:** E · **Read:** 2026-10-13

## What it argues

The authors ask what in the physical world supports "graceful" face-to-face communication, and propose that digital systems can "support coherent behavior by making participants and their activities visible to one another" (abstract). They call such systems "socially translucent" and name three properties: visibility, awareness and accountability (abstract; §2.1).

The founding example is a stairwell door that slams into people. A sign, "Please Open Slowly," "is not a particularly effective solution." A glass window "means that the sign is no longer required" (p. 61). Three reasons follow (pp. 61–62). The window "makes socially significant information visible", since people notice movement and faces more readily than "a printed sign." It "supports awareness: I do not open the door quickly because I know that you are on the other side." It supports accountability: "I will open the door slowly because I know that you know that I know you are there," even if I do not care about hurting others. The authors add that awareness and accountability "usually cooccur in the physical world" but "are not necessarily coupled in the digital realm" (p. 62).

§2.2 adds that "translucence stands in more generally for the power of constraints" (p. 62), meaning translucent, not transparent. A 30-author workshop that reorganised a book of 30 chapters in half an hour showed how the spatial layout constrained who could dominate. The authors separate three levels: constraints exist, participants are aware of them, and participants are aware that others are aware. In digital environments these "are not necessarily coupled" and "it is rarely evident what the constraints are, nor whether the constraints are necessarily shared" (p. 64). Privacy matters too: an election needs some aspects private and others public, so that voters are not accountable for their votes but the counters are accountable to all (p. 62).

§3 applies the idea to knowledge management ("knowledge communities," built on conversation; pp. 65–69). §4 sorts ways to show social cues as realist, mimetic or abstract (pp. 70–71) and describes Babble, with a persistent shared conversation document and a "social proxy" of coloured dots (pp. 71–73). Observed practices include waylaying, group awareness, and concern when strangers appeared, including "an unannounced conversational software agent" (pp. 73–74). The authors treat Babble as "an existence proof" (p. 74). §5 lists research issues, among them showing the conventions of an interaction so participants can enforce them (§5.2, pp. 76–78, citing a limerick game in which violations were visible). The conclusion contrasts technologies that "impose walls between people" with those that "create windows" (p. 80).

## Relation to the argument

Problem 2 (design in place of training) and the premise P7 (coordination through an algorithmic third party places on each party work that no convention yet carries). The door is the cleanest short instance in the library of changing the artefact so that the person's task changes: the sign asks the person to read, interpret and adjust ("extra work—noticing the sign, interpreting its words," p. 80), and the window removes that work by making the fact visible. That parallels the argument that spacing turned an inferential task into a perceptual one (P5). It also shows that making things visible (the paper's own phrases are "making social information more visible" and "making knowledge work visible") is an established design move, so the author's ruling against "legibility" cannot rest on visibility as such. D3 is the live issue: the window is not disclosure of a rule but display of the counterpart's presence, which people then read with skills they already have ("the already established social rules and mechanisms", p. 80).

The source is closer to the paper's concern on one point: the three-level distinction among constraints, awareness of them and shared awareness (p. 64), and §5.2's idea that conventions can be made visible so participants enforce them. That is the nearest thing in the library to a design programme for conventions, and the authors raise it as an open question, not a result.

It cuts against the author on P10. The accountability argument assumes the parties see and are seen by each other with symmetric information, and the system is a neutral medium. The authors note that "assurances of communicative symmetry" are "not automatically present in the digital realm" (p. 64) but treat the cure as more visibility, and never consider a system owner with interests of its own. Facet check: the facet describes this card's content accurately (pp. 61–62, abstract, "I know that you know that I know you are there"). The facet read only pp. 59–62; the rest adds the constraint argument, the privacy tension (§2.2, "translucent" not "transparent"), and the Babble evidence, which the facet did not use. The facet's "one anecdote and a chat system" is right but undercounts: the paper has several vignettes (restaurant, reception, wine shop, book-ordering workshop, limerick game).

## In conversation with

Related bib keys, matched against the paper's own text and references:

- `gutwin2002descriptive`: the paper cites Gutwin, Greenberg & Roseman (1996), "Workspace awareness in real-time distributed groupware," under the heading of "awareness" research (p. 65). The bib item is the 2002 article by Gutwin and Greenberg, a different paper by the same group; confirm which the project needs.
- `clark1991grounding`: the paper cites Clark (1996), *Using Language*, for conversation as an interactive process drawing on common ground (p. 68), not the 1991 chapter.
- No other bib entry matches the reference list (checked surnames Norman, Hutchins, Goffman, Grudin, Dourish, Ackerman, Donath, Viegas).

Leads not in the bib: Dourish & Bellotti (1992), awareness and coordination in a shared workspace; Heath & Luff (1991), the paper's own citation on control rooms (the bib has a different Heath & Luff paper, `heath1992collaboration`); Harper et al. (1991), air traffic control; Erickson (1999), "Rhyme and punishment," on conventions in an online limerick genre; Erickson et al. (1999), the CHI paper on Babble.

## Caution

A design-framework paper; the evidence is anecdote plus an uncontrolled prototype in small, acquainted groups, and the authors say "one should be cautious about generalizing from a few experiences" (p. 74). It was written in 2000 about chat and groupware, before platform recommenders; it concerns people seeing one another, not people inferring what an algorithm will do. It does not test the door, and it does not compare translucent with opaque designs. Accountability is argued, not measured. It cannot be cited as evidence that visibility interventions change behaviour at scale or that they work when one party controls the display.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** The ACM TOCHI PDF (25 pp., journal pp. 59-83), pdftotext; 34 quotations and their page locators (page by page; all quotations verbatim, all locators match); the anecdotes and numbers (30 authors / 30 chapters / half an hour; two years; two to six months); the cited works (Gutwin et al. 1996 on p. 65 and in the references, Clark 1996 on p. 68, Dourish and Bellotti, Heath and Luff, Harper et al. all appear); the bib key list.

**Findings:** (1) The string "making visible" in quotation marks does not occur in the paper; replaced by the paper's own phrasings. (2) The Heath and Luff lead should note that the bib already holds a different Heath and Luff paper (1992), not the 1991 one the paper cites; added. The facet strings in quotation marks ("one anecdote and a chat system") are repo quotations, not checked against this paper.
