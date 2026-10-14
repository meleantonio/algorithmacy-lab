# Jakesch, M., Bhat, A., Buschek, D., Zalmanson, L., & Naaman, M. (2023). Co-writing with opinionated language models affects users' views. In *Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems* (CHI '23).

**Identifier:** doi:10.1145/3544548.3581196 · **Read depth:** full_text (arXiv:2302.00560v1, 1 Feb 2023, 22 pages; preprint, not the proceedings PDF. The bib entry gives the proceedings as pp. 1–15, so my page numbers are the preprint's and will not match the version of record). I read all of it, including the reference list; the OSF materials the paper cites were not opened · **Source-tier:** preprint of a conference paper (peer-reviewed proceedings) · **Evidence basis:** direct_read · **Design and sample:** preregistration not stated; online experiment, N = 1,506 Prolific participants (post-exclusion; 507 control, 508 "techno-optimist" model, 491 "techno-pessimist" model) writing about whether social media is good for society, plus 500 judges labelling 9,223 sentences · **Parties modeled:** person–system (a writer and a language-model suggestion tool); the later readers appear only in the framing · **Facets:** H · **Read:** 2026-10-13

## What it argues

The authors call the mechanism *latent persuasion*: a model that produces some views more often than others can shift its users' views without any persuader designing a message (pp. 1–2). Treatment groups saw GPT-3 ("text-davinci-002", 175B) completions, steered by a hidden prefix prompt and an infix prompt to argue one side; the control group had no assistant (pp. 5–6). Writers could accept suggestions by tab or button.

Writing shifted. Participants given the pro-social-media model were 2.04 times as likely to argue that social media is good for society (95% CI 1.83–2.30); those given the critical model were 2.0 times as likely to argue it is bad (p. 9). The mean opinion difference was about 0.29 on a −1 to 1 scale (d = 0.5) (p. 10). Attitudes shifted too, in a survey asked after the writing task: 45% of the pro model's users said social media is good for society against 35% of controls (d = 0.22, p < 0.001), and the critical model moved opinion the other way (d = 0.19, p < 0.005) (p. 11). The effect was not mere convenience: participants wrote 63% of sentences themselves and fully accepted 11.5% of model sentences (p. 9), and writers taking four to six minutes still differed from controls (d = 0.34) (p. 10). They also did not see it. Only 10% of participants whose view the model shared noticed its imbalance, and 30% of those it contradicted (pp. 12–13); about 20% of participants who disagreed with the model thought it had influenced them (p. 13). 84% of participants whose view the model shared said it was knowledgeable and had expertise; where it contradicted them, only 15% said it was not (pp. 11–12).

The authors weigh three routes, informational, normative and behavioural, and conclude: "the influence was at least partly subconscious and not simply due to the convenience and new information that the language model provided" (p. 15), a claim they hedge: "further research will be required to identify the mechanisms" (p. 15). Limits: one topic, one GPT-3 writing assistant, one session (p. 16).

## Relation to the argument

**P9 (aids that hand the person something to read show weaker effects).** The paper cuts the other way for a different aid: a suggestion tool changed what people wrote and thought, strongly, without their awareness. The relevant contrast is with disclosure-type aids. Here the participants were not told the model was skewed, so the study shows what an *undisclosed* opinionated mediator can do, not what disclosure would do.

**Ruling D3.** It does not test disclosure either way. The finding that participants rated the model as balanced and did not see its effect (pp. 12–13) is consistent with the author's claim that people lack the ability to navigate what they cannot read, but the study does not vary information, so it cannot show that disclosure would fail.

**P10 / the interested mediator.** This is the clearest demonstration in the batch that a tool's built-in preference can move the user, and the authors list "targeted opinion influence" by "commercial and political interest groups" and monetisation by operators as a risk (p. 16). It supports the worry that the party who sets the tool's behaviour is not the user, though the study's model was set by the researchers.

**Against the author.** The model was told to take a side by the experimenters; in deployed tools "model opinions … will be less definite than in our study" (p. 17). Effects came from a strong manipulation, which the authors chose deliberately (p. 6).

**Facet check:** facet H reads "Abstract only: N = 1,506; an opinionated writing assistant shifted what users wrote and thought." The full text agrees.

## In conversation with

- `hancock2020ai`: cited as ref. 51 (Hancock, Naaman and Levy 2020) on AI-mediated communication.
- Leads not in the bib: Arnold, Chauncey and Gajos (2018) on sentiment bias in predictive text and biased writing; Bhat et al. (2021, 2022) on biased text prediction; Thaler and Sunstein on nudges, which the authors extend to opinions (refs. 42, 72); Jakesch et al. (2022) on how different groups prioritise AI values (ref. 55).

## Caution

A preprint (v1) of the CHI paper; check the published version before quoting numbers or page numbers. One topic, one session, crowdworkers, a strong manipulation, a self-reported proxy for pre-task opinion (which the authors say is biased by the treatment effect, p. 7). No test of persistence or of disclosure.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** corrected

**What I checked:** arXiv:2302.00560v1 PDF (22 pages; the card's page numbers are the preprint's). Four verbatim quotations and about 25 numbers: 2.04 (CI 1.83-2.30), 2.0, mean difference 0.29 with d = 0.5, 45% vs 35% with d = 0.22 and d = 0.19, 63% and 11.5%, d = 0.34 for four-to-six-minute writers, 10% and 30% noticing imbalance, about 20% believing they were influenced, 84% and 15% on expertise, group sizes 507/508/491, 500 judges, 9,223 sentences, 175B model, prefix and infix prompts.

**Findings:** One locator error: the "model opinions ... will be less definite than in our study" quotation is on preprint p. 17, not p. 16; fixed. All other quotations and numbers match. Facet quotation ("Abstract only: ...") belongs to the project's facet file and was not checkable here.
