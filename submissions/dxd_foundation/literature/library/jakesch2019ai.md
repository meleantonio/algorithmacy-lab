# Jakesch, M., French, M., Ma, X., Hancock, J. T., & Naaman, M. (2019). AI-mediated communication: How the perception that profile text was written by AI affects trustworthiness. *Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI '19)*, Paper 239.

**Identifier:** doi:10.1145/3290605.3300469 · **Read depth:** full_text (the 13-page CHI 2019 paper as hosted by Cornell Tech; the copy carries the CHI page headers, so locators are section names and "Paper 239" pages as printed) · **Source-tier:** proceedings · **Evidence basis:** direct_read · **Design and sample:** three online experiments on Amazon Mechanical Turk with Airbnb host profiles written by humans: Study 1 (recruited 527, analysed 389), Study 2 (286 recruited), Study 3 (323 recruited, with a preregistered 4×2 mixed design); all profiles were human-written, and only participants' belief about their source was manipulated · **Parties modeled:** two parties + third party (sender, receiver, and an AI that operates on the sender's behalf) · **Facets:** H · **Read:** 2026-10-13

## What it argues
Jakesch and colleagues define AI-mediated communication (AI-MC) as interpersonal communication "not simply transmitted by technology but augmented—or even generated—by algorithms," in which "an AI system operates on behalf of the communicating person" (§1). They ask whether people trust a host less when they believe an AI wrote the host's profile.

Study 1 tells one group that all profiles were written by hosts and another that all were AI-generated, and shows 10 profiles (five high and five low in prior trust rating). There is no effect of the believed source: mean trust is 66.64 in both groups (SD 18.1 and 18.8), though high-baseline profiles outscore low-baseline ones (M = 75.4 against 57.8; F(1, 387) = 2046) (§Study 1). Study 2 mixes sources: the more a participant believed a profile AI-generated, the less they trusted its host; a regression with baseline, AI score and their interaction explains R² = .231, with a negative AI-score coefficient, and a weaker effect for low-baseline profiles (§Study 2). Study 3 uses 30 profiles pretested as AI-like or human-like and four conditions (control, unlabeled, labeled, primed). AI-like profiles lose trust in the labeled and primed conditions, and also when participants only suspected AI authorship; participants who rated a profile "definitely human-written" gave it a mean of 78.29, 16.6 points above a "definitely AI-generated" mean of 61.72 (§Study 3, Figure 5).

They name the pattern the Replicant Effect: "Only when participants thought they saw a mixed set of AI- and human-written profiles, they mistrusted hosts whose profiles were labeled as or suspected to be written by AI" (Abstract). They read it through the Hyperpersonal Model (receivers over-attribute from minimal cues) and the Elaboration Likelihood Model: a mixed set makes the source salient (§6). They also find that different respondents "reliably identify similar profiles to be written by AI," and attribute this to a folk theory of what AI text looks like (§1).

## Relation to the argument
Facet H uses the abstract only, as a case where an AI between two people changes what the receiver thinks of the sender. The full text shows the study's reach. The party that bears the cost is the sender, who did nothing different: the same human-written profile lost trust once it was believed to be AI-authored. So disclosure of mediation, in a mixed field, moved the receiver's judgment of a third party, which is a case the author's D3 ruling should expect: telling people about the AI changes what they conclude, but about the wrong thing, and no behaviour (renting) was measured (§6, Limitations). The mediator here acts for the sender, so this is counter-delegation, not a platform with its own objective (compare the facet's note on `hancock2020ai`). The effect depends on mixture, which means a labelling convention that applied to all profiles would, on Study 1, change nothing; that bears on D8 (who holds the convention) without settling it.

Facet check: the facet's quotation of the abstract is right. The full text adds that Study 1, with uniform AI labelling, found no effect, which the abstract's "only when" implies but does not report in numbers.

## In conversation with
The authors build on Ma et al.'s study of Airbnb host trustworthiness and its public dataset (refs. 38, 39), on the Hyperpersonal Model (Walther 1996, ref. 57; Walther 2011, ref. 56), warranting and signaling theory (Donath 2007), the Profile as Promise framework (Ellison, Hancock and Toma 2012, ref. 15), folk-theory work (DeVito et al. 2017, ref. 8; Eslami et al. 2016, ref. 17), and studies of machine-written news credibility (Wölker and Powell; Edwards et al.). In `references.bib`, `eslami2016first` matches ref. 17. Its authors overlap with `hancock2020ai` (Hancock, Naaman and Levy, the agenda paper that followed) and `jakesch2023co`; I did not find either in its reference list, as both are later. Leads: Ma et al. (Airbnb host dataset); Walther 1996; Ellison, Hancock and Toma 2012.

## Caution
Human-written text with a manipulated belief, not real AI output; MTurk workers; one scenario (Airbnb profiles); no behavioural outcome; mechanisms untested. Pagination is the CHI paper's; the ACM version of record may differ slightly.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The 13-page CHI 2019 PDF (two-column, so text interleaves; I matched phrases by context). Four quotations (AI-MC definition, Replicant Effect sentence, "reliably identify", the 78.29 and 61.72 means) and the numbers: N = 527 recruited and 389 analysed, 286, 323; Study 1 M = 66.64 (SD 18.1 and 18.8); 75.4 vs 57.8, F(1, 387) = 2046; Study 2 R² = .231; 4x2 mixed design and preregistration; 30 pretested profiles; 16.6-point gap.

**Findings:** No issues found. Note that the article prints Study 2 exclusions as "89 out of 285", while the card gives 286 recruited, which matches the Participants paragraph. Section locators (§1, §Study 1 etc.) are the card's own labels, not printed ones; the card says so.
