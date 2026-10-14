# Clérice, T. (2020). Evaluating deep learning methods for word segmentation of scripta continua texts in Old French and Latin. *Journal of Data Mining and Digital Humanities* (Special issue/vol. 2020).

**Identifier:** doi:10.46298/jdmdh.5581 · **Read depth:** full_text (publisher PDF from the journal's Episciences site; 12 pages with the journal's own page numbers 1–12; the volume, issue and article number are not printed in the PDF text, so the heading above gives the year only, as in the bib) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** a model comparison for word-boundary detection: three neural encoders (a CNN with position embeddings, a CNN without, an LSTM) against a dictionary baseline (`wordsegment`); Old French test set of 25,512 examples (193,734 for training), plus three Latin corpora (classical, medieval charters, epigraphic) · **Parties modeled:** none (a machine-learning evaluation) · **Facets:** Z · **Read:** 2026-10-13

## What it argues
Clérice treats the absence of word boundaries in medieval manuscripts and inscriptions as a text-mining problem. Tokenisation is "fairly simple" for modern European text because of spaces and punctuation, but in *scripta continua* "such markers are mostly absent" and spelling variation and rich morphology defeat dictionary methods (Abstract, p. 1). He cites Camps for 29 spellings of Old French *cheval*, with counts from 3,907 to 1 (Section I, p. 2). Boundary detection is cast as classifying each character as "word boundary" or "word content" (Section 2.1.1, p. 2).

Results, all by F-score (the harmonic mean of precision and recall) on word-boundary classification:
- Old French, in-domain (Table 3, p. 5): the dictionary baseline gets 0.985; the best CNN, without position embeddings, 0.990. The LSTM and GRU models do worst, 0.720 and 0.910. Clérice says the CNNs gain at most 0.005 and the baseline "already performs nearly perfectly on the test corpus" (Section 2.2.1.3, p. 5).
- Old French, out of domain (742 examples from four texts; Table 4, p. 6): 0.945 for the CNN against 0.838 for the baseline, which misses about 35% of spaces (3,658 false negatives in 10,193 boundaries).
- Latin (Tables 6–8, pp. 7–8), CNN without position embeddings against the baseline: classical prose and verse 0.988 against 0.968 in-domain and 0.954 against 0.893 out of domain; medieval charters and chronicles 0.995 against 0.982 and 0.962 against 0.881; epigraphy 0.981 against 0.939 and 0.932 against 0.825.

He concludes that the CNN "deals better with unknown corpora" than n-gram methods and expects it to "perform equally well no matter to which Medieval Western European language it is applied" (Section 2.3, p. 9). The training examples are artificial strings of 2–8 words built from edited transcriptions with space characters removed; noise was added to Old French only, as random full stops (20% chance) and copied words (10%) (Section 2.2.1.1, p. 4).

## Relation to the argument
The paper is the sort of hit a reviewer finds searching "scriptio continua" and "AI". It concerns tokenisation of historical text for machines, not reading, and cannot carry the analogy. It bears on the argument in three small ways.

First, it shows that the cost of word-boundary inference falls on any reader or process that lacks spaces and does not know the language well: a dictionary method fails on unseen vocabulary and spelling, a character-level model does not. That is an illustration of P5 (boundary-setting is an inferential task) for machines, not a finding about people, and nothing in it speaks to scribes' or readers' costs.

Second, one sentence can mislead on the chronology. Clérice writes that *scripta continua* "disappeared around the 8th century (see Zanna [1998])", but that "spacing remained erratic" (a footnote marker follows "erratic") "in later centuries" (Section I, p. 1). The argument map puts the Insular start in the late seventh century and the Continental adoption from the mid-tenth, standard by the mid-eleventh (P2, resting on Saenger 1997, pp. 83, 100, 176–177). The sentence is a one-line aside whose single source is a study of Irish Latin in the 7th–8th centuries. It does not contradict Saenger on the Continent so much as stop short of it. The paper must not cite Clérice for dating.

Third, it supports the narrow point that unspaced medieval Latin and Old French were segmentable by a model from character context alone, with high accuracy on edited text. Note that the test strings are cleaned transcriptions and not images of manuscripts.

Facet check: the facet file read the abstract and listed it as a technical use of the term. The full text bears that out. It adds the dating sentence above, which the abstract does not show.

## In conversation with
- `saenger1997space` is not cited; Clérice cites Stutzmann (2016) on erratic spacing in Psalm 101 manuscripts, 11th–15th c. (Section I, p. 1), and Zanna (1998) for the 8th-century end date. Neither is in the bib.
- Leads not in the bib: Stutzmann 2016, "Words as graphic and linguistic structures: word spacing in Psalm 101"; Zanna 1998 on Latin reading, writing and morphology in Ireland; Bluche et al. 2017 and Wahlberg et al. 2014 on keyword spotting in medieval manuscripts (cited as the only prior OCR/HTR work); Chen et al. 2015 on Chinese segmentation.

## Caution
A tool-evaluation paper. The training data are artificially cut transcriptions, not manuscript images, and the dictionary baseline is within 0.005 F of the best CNN on the in-domain Old French test set (0.985 against 0.990). No human readers appear. The generalisation to every medieval Western European language is asserted, not tested. The volume and issue of the journal record are not printed in the PDF.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** publisher PDF (clerice2020evaluating.pdf, 12 pp.), full text via pdftotext. 12 quoted strings, all F-scores in Tables 3, 4, 6, 7, 8, N = 193,734 / 25,512 / 742, 3,658 of 10,193 false negatives, Camps's 29 spellings (3907 to 1), the noise parameters (2-8 words, 20% full stops, 10% copies), and the reference list (Stutzmann, Zanna, Bluche, Wahlberg, Chen).

**Findings:** (1) "any Medieval Western European language" is not in the source; the text reads "the model should perform equally well no matter to which Medieval Western European language it is applied" (Section 2.3, p. 9). Fixed in both places. (2) Caution said the baseline "wins or ties" in domain; Table 3 shows baseline 0.985 against CNN P 0.990, so it trails by 0.005. Fixed. (3) The "spacing remained erratic in later centuries" quote had a footnote marker inside it in the source; the card now says so. All numbers otherwise match. The card's "11th-15th c." for Stutzmann comes from the reference-list title, not from Section I.
