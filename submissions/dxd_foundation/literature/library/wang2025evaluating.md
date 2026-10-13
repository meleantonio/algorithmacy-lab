# Wang, L., Friedman, N., Zhu, C., Zhu, Z., & Mountford, S. J. (2025). Evaluating node-tree interfaces for AI explainability. arXiv:2510.06457.

**Identifier:** arXiv:2510.06457v1 (7 Oct 2025) · **Read depth:** full_text (arXiv v1 preprint, 5 pp.; the text has no page numbers on the extract, so locators are section numbers. I read all of it, including the reference list of ten items) · **Source-tier:** preprint (workshop-format short paper; the authors refer to "the workshop format limitations") · **Evidence basis:** direct_read · **Design and sample:** between-subjects comparison, N = 20 business users (6 male, 14 female; ages 23 to 59, mean 45.3; 10 from North America, 10 from Europe) recruited through Respondent.io, 10 per condition; four scripted tasks; self-rated trust, helpfulness and ease · **Parties modeled:** person–system (one user, one text-based AI assistant) · **Facets:** H · **Read:** 2026-10-13

## What it argues

The authors, who work at SAP, ask whether showing an LLM's answer as a hierarchy of nodes, instead of as chat bubbles, makes the answer easier to follow and trust. Their node-tree interface breaks a reply into parent and child nodes, lets a user pick up to five nodes to summarise, ask a follow-up on any node, and regenerate or delete a node (§III.A.2). The control is a chatbot "designed based on standard AI chatbots, like ChatGPT." Both interfaces were text-only (§III.A.2). The four tasks were an exploratory trip-planning task, a follow-up on flight savings, a three-site choice for a city park, and a food-distribution event for a non-profit (§III.A.3).

Measures were three self-ratings after each task: trust in the assistant (1 to 10), whether the node tree "help[ed] you understand the problem better" (five-point helpfulness), and ease of navigation (five-point) (§III.A.4). The authors report 15 of the questions they asked.

Results (§IV):
- Trust: "90% of the Node-tree users reported that the Node-tree influenced their trust in AI responses positively," and none reported lower trust. On the problem-solving task 80% of node-tree participants and 70% of chatbot participants were positive about using AI suggestions in real life; "this difference is not significant (t(19)= .21, p=.6)" (§IV.B).
- Performance: in exploratory and decision-making tasks "the Node-tree group also consistently outperformed the chatbot group," while on the step-by-step problem-solving task the chatbot group did better (§IV.C). No performance figure, accuracy score or test is given; "performance" is the helpfulness rating.
- Usability: 90% of node-tree users found it easy to navigate (§IV.D).
- Qualitative: chatbot users lost context on follow-ups; one wrote that "several times, the context is lost and a generic answer is provided" (§IV.C).

The authors conclude that effectiveness depends on the task: node trees for brainstorming and decision-making, chat for single-step and linear work, and an interface that switches between them (§V, §VI). They also say: "We do not report statistical significance because the sample size was not high enough, and instead we report user data trends" (§V.B).

## Relation to the argument

**P9 (aids that hand the person something to read show weaker, less consistent effects on what people do).** The source fits P9 only weakly because it measures nothing the person does. All three outcomes are self-reports of trust, helpfulness and ease, after scripted tasks that had no correct answer or checked outcome. The one inferential test reported is a null result. It sits with the facet's list of non-chat interfaces as one more case of "perceived" gains.

**D3 and the explanation-for-trust line.** The paper's premise is that an interface which structures the answer will raise trust and "transparency" (abstract, §I). The trust measure is self-rated and no check on whether trust was warranted is made. In terms of the paper's argument, higher trust in an output is not evidence of better navigation of the system.

**Third party.** Dyadic; no one other than the user and the assistant is modeled.

Facet check: the facet says "n = 20 business users, self-reported trust and task performance." Two corrections from the full text. First, the abstract states that "Quantitative and qualitative findings indicate that Node-tree interfaces not only improve task performance and decision-making support but also promote higher levels of user trust"; the body gives only percentage descriptives, one non-significant test, and an admission that significance is not reported. Second, "task performance" is a helpfulness rating, not a measured outcome. The facet's reading is therefore too generous if "task performance" is read literally.

## In conversation with

The source cites ten works (§II and the reference list):
- De Graaf and Malle 2017 on explainable agents forming correct mental models.
- Edmonds et al. 2019 (*Science Robotics*): real-time visual explanations of a robot's decisions built more trust than text summaries.
- Han, Phillips and Yanco 2021 on verbal robot explanations.
- Bensch and Eriksson 2023 on adapting to the user.
- Commercial tools Mapify, Xmind, Think Machine and Mymap.ai.

None of these is in `../references.bib`, and it does not cite Sensecape (`suh2023sensecape`) or VisCanvas (`ueno2026viscanvas`), which the facet groups with it. Leads: Edmonds et al. 2019 and De Graaf and Malle 2017 as sources on explanation and trust.

## Caution

A short exploratory study with ten people per condition. The authors report that the questions differed by task and so "were not directly comparable" (§V.B). The reported t-test has 19 degrees of freedom, which does not fit a between-subjects design with two groups of ten (18 would be expected); treat the statistic as unreliable. The paper contradicts itself on performance and significance (see Facet check). The authors work at the firm whose enterprise tools the paper recommends; the paper discloses SAP's support in the acknowledgments. It cannot support any claim about decisions made through a third party.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** Opened the arXiv v1 PDF (5 pp.) and extracted it. Checked 8 verbatim quotations (all exact; the abstract quote differs only by a pdftotext hyphenation artifact), the participant counts, ages, scales and answer options, the 90/80/70% figures and t(19) = .21, p = .6, the task list, the ten references, the SAP acknowledgment, and the absence of Sensecape and VisCanvas.

**Findings:** No issues found. The card's two checks on its own inference (t-test with 19 df looks odd for two groups of 10; 'task performance' is a helpfulness rating) are correct readings of the text.
