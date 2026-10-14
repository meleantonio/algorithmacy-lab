# Koomen, P. (2025). *AI horseless carriages* [Essay]. koomen.dev.

**Identifier:** https://koomen.dev/essays/horseless-carriages/ · **Read depth:** full_text of the web essay (about 4,500 words, saved 2026-10-13). The essay's interactive demos did not run in my copy; I read the demo prompts printed in the text but did not use the demos. The text dates itself: "As of April 2025" · **Source-tier:** practitioner essay · **Evidence basis:** direct_read · **Design and sample:** none (argument with two built demos using gpt-4o-mini; no users) · **Parties modeled:** person–system (a user and an agent that acts for them; the email recipient is outside the loop) · **Facets:** Z · **Read:** 2026-10-13

## What it argues
Pete Koomen, a Y Combinator partner, argues that many AI apps are "horseless carriages": "They're bad because they mimic old ways of building software that unnecessarily constrain the AI models they're built with." His case study is Gmail's Gemini draft feature, whose output is "wordy and weirdly formal and so un-Pete." He splits the model prompt into a System Prompt (the general rules, written by the developer in current apps) and a User Prompt (the specific request). "The problem is that I'm not allowed to change it." His fix is to let users write the System Prompt: "when an LLM agent is acting on my behalf I should be allowed to teach it how to do that by editing the System Prompt," and "Most AI apps should be agent builders, not agents."

He shows that a short "Pete System Prompt" turns the draft into "Garry, my daughter has the flu. I can't come in today." He then shifts the use case from writing to reading: because his emails are short, drafting saves little, while an agent that labels, archives and drafts replies to incoming mail would save time. He argues that tools, not prompt separation, are the security layer: "It is much easier to enforce boundaries with tools written in code than it is to enforce them between System and User Prompts written in text," and "if any part of the prompt is in user space then the whole thing is in user space." The division of labour he rejects is "developers decide how software behaves in the general case, and users provide input" (section "Old world thinking").

## Relation to the argument
It is the nearest agent-acting-for-a-person neighbour in facet Z. It supports the paper's complaint that the conventions of the old interface were built for another job, and it locates control in who writes the rules of the agent, which parallels the paper's concern with who holds a convention (ruling D8). It differs on the point that matters most: Koomen gives the owner of the agent, the user, the pen, and assumes the user's interest is the agent's goal. It does not treat a mediator whose operator has a stake of its own (P10). His security remark, that boundaries belong in tools outside the prompt, agrees with the external-control principle in Nadella's post (P11).

Facet check: the facet says the email scenario involves a boss as recipient, not as a party the mediator reads. The text bears that out: Koomen's agent reads his own inbox and drafts as him. The facet's "only neighbour with an agent acting for a person" is a fair reading of what I saw, but I did not survey others.

## In conversation with
No scholarly references. Cites Trevithick's 1803 steam carriage (a Wikipedia image) as the horseless carriage, and names Superhuman and Zero as email clients with the idea in progress (footnote 2). In the bib, near `nadella2026models` on external controls and `wattenberger2023chatbots`, `appleton2023sketchbook` on the interface complaint.

## Caution
A venture investor's essay, April 2025, built on two toy demos. The claim that "prompt-writing is surprisingly intuitive" is an assertion without a test. Nothing here concerns users who cannot or will not write prompts, or settings where the operator's and user's interests diverge.

---

## S2 adversarial verification (2026-10-13)

**Verdict:** confirmed

**What I checked:** The saved web page text (about 4,500 words; the demos' interface text is mixed into the extraction). All 14 quotations from the essay matched word for word, including the "Old world thinking" division-of-labour sentence and the "As of April 2025" dating; also footnote 2 (Superhuman and Zero), the Trevithick 1803 steam carriage from Wikipedia, the gpt-4o-mini demos, the "YC Partner" self-description, and "prompt-writing is surprisingly intuitive".

**Findings:** No issues found. The facet phrase "only neighbour with an agent acting for a person" is not in the essay and was not checkable here. The links to `nadella2026models`, `wattenberger2023chatbots` and `appleton2023sketchbook` are the card's own bib associations; the essay cites none of them.
