# Shavit, Y., Agarwal, S., Brundage, M., Adler, S., O'Keefe, C., Campbell, R., Lee, T., Mishkin, P., Eloundou, T., Hickey, A., Slama, K., Ahmad, L., McMillan, P., Beutel, A., Passos, A., & Robinson, D. G. (2023). *Practices for governing agentic AI systems* [White paper]. OpenAI. https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf

**Identifier:** https://cdn.openai.com/papers/practices-for-governing-agentic-ai-systems.pdf (no DOI) · **Read depth:** full_text (the 23-page PDF from OpenAI's site; I read §§1–6 in full and the reference list for the items noted below; the PDF carries no date on its face; its embedded creation date is 18 Dec 2023, and its latest cited works are from 2023) · **Source-tier:** report (corporate white paper; not peer-reviewed) · **Evidence basis:** direct_read · **Design and sample:** none (position paper proposing seven practices, each with open questions) · **Parties modeled:** other (model developer, system deployer and user, with "third parties" and compute providers named as further actors) · **Facets:** R3 · **Read:** 2026-10-14

## What it argues

Authors at a model developer propose "baseline best practices" so that "at least one human entity is accountable for every uncompensated direct harm caused by an agentic AI system" (p. 3). They name three parties: the model developer, the system deployer and the user, with "third parties (e.g. other humans, or the providers of APIs)" as those the agent may interact with (p. 5). Seven practices follow (§4), which they say "alone are insufficient" (p. 8): evaluate suitability, constrain the action space and require approval, set default behaviours, make agent activity legible, monitor automatically, make agents attributable, and keep them interruptible.

The passages that bear on this paper:

- *Approval.* Requiring a user to authorise high-stakes actions "is a standard way to limit egregious failures", but this "is also made harder when the user must approve many decisions and thus must make each approval quickly, reducing their ability to meaningfully consider each one" (p. 9). One open question asks how to keep approvals from turning into a "rubber stamp" (p. 10).
- *Legibility.* A user aware of the agent's reasoning can "notice that something has gone wrong and intervene, either during operation or after the fact" (p. 11). Yet "'chain-of-thought' transparency comes with challenges and cannot yet be fully relied on" (p. 11), and long reasoning "may balloon beyond a user's ability to feasibly keep up" (p. 12). They recommend "a ledger of actions taken by the agent", adding that "Actions that can only be reviewed after the fact should be more easily reversible than those that require approval" (p. 12).
- *Monitoring.* "human users may not always have the time to go through the agent activity logs", so a second AI system may review them (p. 12), which brings privacy costs and a recursion problem (pp. 12–13).
- *Interruptibility.* "Interruptibility (the ability to 'turn an agent off'), while crude, is a critical backstop" (p. 14). Deployers "could be required to make sure that a user can always activate a graceful shutdown procedure for its agent at any time", and "an agent should not be able to halt or tamper with the user's attempt to shut them down" (p. 14). On outsiders: a user may be unwilling or unable to stop a harmful agent, which "raises important challenges around how third parties communicate to a user that their agent is causing harm, and in what circumstances an external party has the right or obligation to terminate a user's agent" (p. 15). They suggest "redundancy in the number of human parties that can turn off an AI agent instance", naming the deployer and the data-centre operator (p. 15).

## Relation to the argument

**Premise P13 and rulings D4–D5.** This is the nearest industry document to Nadella's post, and it overlaps him on logs, interruption and attribution. It supports the paper's reading that these controls belong to principals: the brake goes to the user, the deployer and the compute provider, not to the people the agent acts on. It also does what the paper says Nadella does not: it names the third party and states the problem of an outsider who is harmed but cannot stop the agent (p. 15). It leaves that as an open question. So the source narrows the paper's claim: the omission the paper finds in Nadella is recognised in this literature, and the proposed answer is more parties with a switch, not a different representation for the affected person.

**Ruling D3 and premise P8.** The paper's literacy critique of logs has support from inside industry. The white paper concedes that users will not read long reasoning or logs at speed and turns to automated monitors (p. 12). That is consistent with the paper's Target 4 critique, though the authors' remedy is more automation, not re-representation.

**Use in DRAFT_v2:**

Not cited in DRAFT_v2: a case-insensitive grep for "Shavit" and "agentic AI systems" over the paper (lines 1–714) finds no hit (S2 check, 2026-10-14). The lines below are where the source bears on the draft's claims.

- Line 182 (auditability: "tamper-proof human readable evidence"). Narrows: the same practice appears here as "a ledger of actions" (p. 12), with the concession that humans may not have time to read it (p. 12).
- Line 183 (interruption as an emergency brake). Supports the description of interruptibility as a principal's backstop: "a user can always activate a graceful shutdown procedure" (p. 14).
- Line 186 (the framework is internal principal–agent control). Supports for this document too: its parties are developer, deployer and user (p. 5).
- Line 211 ("does not hold the brake. They cannot interrupt the model in mid-inference"). Narrows: the authors name the third-party problem and ask "in what circumstances an external party has the right or obligation to terminate a user's agent" (p. 15). The draft's point stands for Nadella's post; it should not be generalised to enterprise AI governance as a whole without this counter-example.
- Line 213 ("a disclosure after the fact is an autopsy report"). Narrows: the authors pair after-the-fact review with reversibility ("should be more easily reversible", p. 12), which is a design response to the autopsy problem for the user, though not for a third party.

## In conversation with

- `crootof2023humans` — cited as [23] (the 2022 preprint "Humans in the loop") for the roles a human in the loop serves (p. 9, n. 15).
- `elish2019moral` — cited as [5] on blame landing on the nearest human (p. 3).
- `lanham2023measuring` — cited as [34] for chains of thought that the model does not rely on (p. 11).
- `nadella2026models` — a later post covering the same ground (logs, brake, outside controls); the post cites nothing.
- `hadfield2017offswitch` — the formal account of why an agent might resist shutdown. The white paper does not cite it (it cites Perez et al. [30] for an "instrumental goal of self-preservation" and Hadfield-Menell et al.'s 2016 cooperative inverse reinforcement learning paper [28]); it says it "may be important" to design agents to place graceful shutdown "as a primary goal" (p. 14).
- Not in the bib, as leads: Chan et al. (2023), "Harms from increasingly agentic algorithmic systems" (FAccT); Cobbe, Veale & Singh (2023), "Understanding accountability in algorithmic supply chains" (FAccT); Zerilli et al. (2019), "Algorithmic decision-making and the control problem" (*Minds and Machines*); Greshake et al. (2023) on prompt injection.

## Caution

A corporate white paper by a model developer, not peer-reviewed, with no data. The authors say they "do not yet have strong recommendations on how accountability ought to be structured" (p. 3). It concerns user-initiated agents (a personal assistant buying cake ingredients), not a platform allocating between two parties, so its "user" is the principal and the third party is incidental. The publication date is not printed on the PDF; 2023 rests on the file's creation date and its references.

## S2 adversarial verification (2026-10-14)

**Verdict:** corrected

**What I checked:** I re-opened the saved PDF (pdfs/R3/shavit2023practices.pdf, 23 pages; embedded creation date 18 Dec 2023) and located every quotation by page: pp. 3, 5, 8, 9, 10, 11, 12, 14, 15 all matched, including the third-party termination passage and the deployer/data-centre redundancy (p. 15). Checked reference numbers [5] Elish (cited p. 3 as [4, 5]), [23] Crootof et al. (p. 9 and n. 15), [34] Lanham et al. (p. 11), and what [28] and [30] are. Re-read DRAFT_v2 lines 182–186, 211, 213 and grepped the draft.

**Findings:**
1. The `hadfield2017offswitch` entry said the white paper "asks designers to make shutdown a primary goal (pp. 14–15)". The text says it "may be important" to do so (p. 14), and the paper does not cite the off-switch paper. Corrected.
2. Added that DRAFT_v2 does not cite this white paper; the relevance verdicts (narrows lines 182, 211, 213; supports 183, 186) stand as read.
3. Quotations otherwise matched word for word; the author list matches the PDF's title page.
