# Niizato, T., Sakamoto, K., Mototake, Y., Murakami, H., Tomaru, T., Hoshika, T., & Fukushima, T. (2020). Finding continuity and discontinuity in fish schools via integrated information theory. *PLOS ONE, 15*(2), Article e0229573. https://doi.org/10.1371/journal.pone.0229573

**Identifier:** doi:10.1371/journal.pone.0229573 (also arXiv:1812.00718) · **Read depth:** full_text (published open-access PLOS ONE PDF, 29 pages, article-page numbering "n / 29"; I read the whole text, Tables 1–4, Methods, the supporting-information captions and the reference list; Figures 1–11 I read through captions and the text that reports them; the S1–S11 figures and the S1 TPM table were not opened) · **Source-tier:** peer-reviewed article · **Evidence basis:** direct_read · **Design and sample:** observational animal study plus simulation. Video tracking of juvenile ayu (*Plecoglossus altivelis*) schools of N = 2, 4, 5 (three recordings each) and N = 3 (four), 10–15 minutes each, about 83,000–107,000 time steps per recording (Table 3); trajectories binarised into ON/OFF states per fish; IIT 3.0 Φ computed with PyPhi using the cut-one approximation; compared with mutual information, transfer entropy, Boids simulations and random Markov chains · **Parties modeled:** other (groups of 2–5 fish; no mediator) · **Facets:** R5 · **Read:** 2026-10-14

## What it argues

Niizato and colleagues apply IIT 3.0 to real animal collectives. They binarise each fish's state by whether another fish is within a distance and a visual field and whether it turned sharply (AND of three conditions, pp. 4–5), assume a fully connected network with self-loops (p. 5), estimate a transition probability matrix from the data, and compute Φ with PyPhi's "CUT_ONE_APPROXIMATION" (p. 21). They then scan all parameter settings.

The main result is a discontinuity between three- and four-fish schools: mean Φ in schools of four or five is high when each fish has a blind spot, whereas in schools of two or three it is high only with a full visual field (Fig 2, p. 7; Table 1, p. 9). Mutual information and summed transfer entropy show no such break (Figs 3–5, pp. 8–10). In four- and five-fish schools, the minimum information partition usually cuts off a single OFF-state fish, and that fish is the positional leader in 82–96% of cases against 13–21% with no blind spot (Table 2, p. 12). They read this as "IIT leadership" (pp. 11–13).

Two controls matter for anyone measuring Φ on groups. First, Boids simulations with similar-looking trajectories gave "completely different" Φ distributions (p. 17). Second, and more important, Φ is not zero when simulated agents do not interact (Boids models with coupling strength C = 0; the authors did not and could not uncouple the real fish) [S2 clarification]: "We expected a coupling strength value of C = 0 to lead to a ⟨Φ⟩ of 0 for all values of N; however, ⟨Φ⟩ is non-zero and increases as N grows" (p. 17). The authors attribute this to size effects and to a "boundary effect" created by binarising continuous motion (pp. 17–18); random Markov chains likewise show Φ rising with system size (Fig 11, p. 18). They add that "the present practical computational limit of IIT 3.0 is around seven or eight individuals" (p. 20).

## Relation to the argument

**Claim 1 and its operationalisation (§8.1).** This is an application of IIT 3.0 Φ, not a Barrett–Seth proxy, to a real collective of interacting agents, with the transition matrix estimated from behaviour. It shows the tool can be run on coded group behaviour and can pick up structure that mutual information and transfer entropy miss, which supports the paper's use of Φ as a lens on group integration. It also shows what the pre-specification promised at line 450 has to guard against.

**The size and coding artefact.** Claim 1 predicts that Φ on the triad will exceed Φ on each person–mediator pair. Niizato et al. find that Φ rises with N even with zero coupling in their Boids simulations, and in random Markov chains, which they attribute to size and to a boundary effect of the binarisation (pp. 17–18). A three-node system can therefore beat its two-node parts for reasons unrelated to irreducible coordination. The draft's design already has the right answer: fix coding and partition in advance and validate on Boolean models (line 450). This paper says the validation must include an uncoupled null of the same size and coding, and that the second half of Claim 1 (the excess shrinks when M is made independent of one party) is the stronger test, because it holds N fixed.

**Use in DRAFT_v2:** Not cited in DRAFT_v2 (a grep for "Niizato" finds no line, 2026-10-14); the verdicts below say how the source, as read, bears on the lines that make the claims it concerns. [S2 note]
- **Line 449** (Claim 1: triad Φ exceeds pair Φ; the excess shrinks when M is made independent of one party). Complicates the first half: Φ grows with N under zero coupling in simulated Boids and in random Markov chains (p. 17; Fig 11, p. 18), so "triad > pair" is expected even without integration. Supports the second half as the discriminating test, since it compares systems of equal size.
- **Line 450** ("Integrated information (Φ) has so far been applied to human groups only by proxy … Φ itself has not been computed on a real physical system"). Consistent with the human-groups clause: these are fish, not people. On the second clause, the paper computes IIT 3.0 Φ on a model estimated from a real system's behaviour, with the cut-one approximation (p. 21). In Barrett et al.'s terms that is still not Φ of the physical system, so the draft's sentence survives, but a reader may raise this paper against it; a sentence acknowledging animal-group applications would pre-empt that.
- **Line 450** ("validate them on small Boolean models where exact values can be computed"). Supports and sharpens: include uncoupled and random-TPM controls of matching size and binarisation (pp. 17–18), and note the practical ceiling of seven or eight nodes (p. 20).

## In conversation with

- `engel2018integrated` — cited (in an *Artificial Life and Robotics* listing, ref. 84) among works linking IIT to group interaction; Engel and Malone used Barrett–Seth estimates on humans, this paper IIT 3.0 on fish.
- `mediano2019measuring` — cited (ref. 74) for the computational comparison of Φ versions.
- `barrett2011practical` — cited (ref. 60) for empirical Φ measures.
- `barrett2026integrated` — later; its distinction between proxies and Φ of a physical system is the yardstick for reading this paper.
- Leads not in the bib: Oizumi, Albantakis & Tononi (2014), IIT 3.0, *PLoS Comput Biol*; Mayner et al. (2018), PyPhi; Albantakis & Tononi (2015) on cellular automata and animats; Marshall et al. (2017) on causal analysis and autonomy.

## Caution

Small samples: three or four recordings per group size. The binarisation is the authors' choice, and they scan many parameter settings, so the striking contrasts are partly selected from a heat map (Figs 2, 8). The cut-one approximation evaluates only a subset of bipartitions (p. 23). The Discussion states that the three-to-four discontinuity "not only exists in the IIT of real fish but also in the IIT of the Boids model" (p. 19), which contradicts the Results' statement that the Boids model "lacked the discontinuity" (p. 17); cite the Results. Fish, not people, and no mediator.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** Downloaded the PLOS ONE PDF myself (byte-identical to the writer's niizato_plos.pdf; 29 pp.). Checked Crossref (PLOS ONE 15(2), e0229573, 27 Feb 2020; seven authors as listed). Checked every quotation, Tables 1–3, the network assumption, the PyPhi option, the cut-one note in Methods, the Boids and Markov-chain controls and reference numbers 60, 74 and 84. Re-read DRAFT_v2.md lines 278, 314, 319–329, 345–358, 408, 417–441, 449–459, 470, 475 and 498 myself and grepped the surname: the source is not cited anywhere in DRAFT_v2, so I added a note saying so at the head of "Use in DRAFT_v2"; the line numbers and quoted draft wording in the verdicts match the current file.

**Findings:**

1. All quotations are verbatim and correctly paged (pp. 17, 19, 20, 21). Table 2 (p. 12) gives match rates 82–96% with a blind spot against 13% (N = 4) and 21% (N = 5) at full visual field; Table 3's 83,654–107,206 time steps and the 10–15-minute recordings check. The Results/Discussion contradiction on the Boids discontinuity (p. 17 vs p. 19) is real.
2. Clarified that the zero-coupling result comes from Boids simulations with C = 0 and from random Markov chains, not from real fish (p. 17; Fig 11, p. 18); the card's "when agents do not interact" read as if it covered the fish data. Adjusted the same point in "Relation to the argument" and the line-449 verdict.
3. Added the not-cited note. The line-450 verdicts hold; the card correctly marks that the PyPhi result is Φ of an estimated TPM, not of the physical system.
