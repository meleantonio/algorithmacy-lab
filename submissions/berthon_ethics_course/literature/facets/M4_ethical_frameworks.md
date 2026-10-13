# Facet M4: the moral philosophy the paper needs (2026-10-13)

Facet M4, 2026-10-13. Agent-drafted. The author has not reviewed it, and none of the text is the author's.

## What this facet covers

The paper's ethical apparatus is thin: three internal standards for calling a past practice a failure, Moody-Adams (1994) on affected ignorance, and Hirschman on exit and voice (`T_adjudication.md` §5 and §9.4; `X_counter_case.md` Q2). I checked eight bodies of moral and political philosophy against the outline in `AUTHOR_DRAFT.md`: epistemic injustice, structural responsibility, domination, capabilities, judging the past, technology ethics, responsibilization, and the objections a philosopher would raise. For each I record what I could open, what it says, which section it bears on, and what adopting it would cost.

Method notes. I resolved every DOI at Crossref or found the work by title query there, and compared titles. Where I opened text, quotations and page numbers come from that text. Some PDFs were bot-walled (Wiley, Springer, SAGE, ACM, PhilArchive, SSRN); I recorded the block and did not work around it. Four open copies are third-party or author-hosted (Anderson 1999 on a course site, Winner 1986 reprint on a course site, Fricker 2010 on a Sheffield page, Giesler and Veresiu 2014 on a York page); I flag each. Page numbers are the journal's where the copy carries them, and the copy's own where it does not. Bib keys follow `surnameYEARfirstword`. `moodyadams1994culture`, `delgamuukw1997` and `marshall1999` already exist in `references.bib` and I reuse them; the rest are in `M4_ethical_frameworks.bib`.

Counts by read depth are at the end of the document, after the synthesis.

## Read-depth key

- **Full**: read the whole text.
- **Part**: opened the text and read the named sections.
- **Abstract**: database abstract only.
- **Record**: Crossref or publisher record verified; text not opened.

## 1. Epistemic injustice

**Fricker (2007), `fricker2007epistemic`. Record.** Not opened. Two chapters are in Crossref (testimonial injustice, pp. 9-29; hermeneutical injustice, pp. 147-175). I know the definitions only second-hand. Symons and Alvarado (2022) give testimonial injustice as a speaker "incorrectly judged an unreliable source of testimony ... in virtue of his social position" (preprint p. 10) and hermeneutical injustice as the case where "unjust social conditions prevent the subject of the harm from having access to the relevant terms, criteria, words, ideas, etc. necessary to understand or articulate that a harm has been done to them" (p. 15). The Internet Encyclopedia of Philosophy entry (Sinclair, `sinclair0000epistemic`, Part) reports Fricker as saying hermeneutical injustice is "purely structural" (Fricker 2007, 159, as quoted there) and describes the wrong as done "to someone specifically in their capacity as a knower". The author needs the book itself before citing it.

**Symons and Alvarado (2022), `symons2022epistemic`. Part** (abstract, sections 1 to 4, author-hosted preprint). They argue that data-science technologies diminish "individuals with respect to their standing as knowers or their credibility as sources of testimony" (abstract). Two moves matter for the paper.

1. *Algorithm over witness.* Their parole case: a prisoner found that one question skewed his COMPAS score; his supervisor agreed and wrote to the prison system, "This had no effect on either the process, the score, or on Rodriguez's overall situation". They conclude: "The supervisor in direct contact with the inmate was deemed less credible than the algorithmic assessment" (preprint p. 17). This is the §3.3 structure in a modern setting: a recorded output outranks what a person said, and the person closest to the facts loses. Symons and Alvarado say the same of the person scored: "when one is automatically considered a lesser knower vis-à-vis the tools themselves, one suffers a testimonial epistemic harm" (p. 15).
2. *No intent needed.* Fricker's harms "should be distinguished from instances of deliberate, manipulative malice ... it is not a necessary condition for epistemic injustice that it results from malicious intent" (p. 10). That bears on §5.4, where the paper declines to prove intent.

Their treatment of opacity is also relevant to §4 row 2 (withheld competence): opacity leaves us "without epistemic recourse" (p. 13), and the data-science systems are "closed to recourse" (p. 14, quoting Kitchin 2014).

*Bearing:* §3.3 and §4 row 3 (the record), §5.3. *Supports and sharpens.* A referee in AI ethics would expect it.

**Kay, Kasirzadeh and Mohamed (2024), `kay2024epistemic`. Part** (abstract, introduction, literature review; arXiv v1). Gives a map of the field: "Testimonial injustice can arise when algorithms are prioritized over human credibility ... hermeneutical injustices can occur when algorithms independently construct meanings and interpretive frameworks". It credits Byrnes and Spear (2023) with the term "algorithmic epistemic injustice"; I did not verify that source. It lists Hull (2023) on COMPAS and physiognomic systems, and Pozzi (2023) on "automated hermeneutical appropriation". Use this as a map, not as a source for Hull or Pozzi.

**Hull (2023), `hull2023dirty`. Record.** The Springer page redirected and SSRN returned 403. **Pozzi (2023), `pozzi2023automated`. Abstract.** She argues the wrong done to patients scored by an opioid-risk system "can be captured through the lenses of Miranda Fricker's account of hermeneutical injustice" (abstract).

**Dotson (2011), `dotson2011tracking`. Abstract.** She defines epistemic violence as "the failure, owing to pernicious ignorance, of hearers to meet the vulnerabilities of speakers in linguistic exchanges". The terms "testimonial quieting" and "testimonial smothering" are hers (the brief names them), but the abstract does not define them and I did not open the text, so I do not characterise them. **Dotson (2012), `dotson2012cautionary`; Medina (2013), `medina2013epistemology`; Medina (2011), `medina2011relevance`. Record.** The IEP entry reports Medina's point that credibility excess is a related harm; that is relevant if a record or an algorithm receives more credit than a person. I have only the IEP's word for it.

**Indigenous oral testimony and epistemic injustice.** I found one work that applies the framework to Indigenous peoples: Tsosie (2017), `tsosie2017indigenous` (Abstract). It concerns anthropology, and its abstract says it offers "case studies demonstrating the continuing existence of hermeneutical injustice and testimonial injustice". Miller (2011), `miller2011oral` (Record), is the book on oral history in the courts, and it does not appear to use Fricker. I found no work in Crossref, OpenAlex or the web search that applies the Fricker framework to *Delgamuukw*, to treaty interpretation, or to oral history in court; and I found none that links such a case to algorithmic systems. That is a documented gap in those sources, not a claim of novelty.

**Does it fit "record over voice"?** Partly, and the paper must choose which part.

- Fricker's testimonial injustice needs an *identity prejudice* in the hearer. A written-text rule that outranks oral evidence is a rule, not a prejudice, unless the paper shows the prejudice behind it. A search snippet reports Hibbitts (1992) saying that common-law courts associate the oral with fraud; I did not open it and do not rely on it.
- Hermeneutical injustice fits the Waitangi translation problem (a gap in shared concepts for what the Maori text conveyed) and the "closed ticketing" scenario of the introduction. But per the IEP, Fricker calls it "purely structural", with no agent. That sits badly with §2.5, which wants named courts and chartered bodies. The paper needs a line on how it reconciles the two (see section 2 below).
- Credibility excess (Medina, via IEP) may describe the record better than credibility deficit does: the text or the score is over-credited. Symons and Alvarado's supervisor case is the cleanest example.

*Cost of adopting:* a new vocabulary (knowers, credibility economy) and a commitment to say whose prejudice. It does not touch the internal-standards rule, because epistemic injustice is a description of the wrong, not a test for calling it a failure.

*A check for the author.* The draft says *Delgamuukw* noted "the systematic discounting of oral histories in contract interpretation" (§3.3). Search snippets describe the case as about aboriginal title and the trial judge's treatment of oral histories, with the Supreme Court later giving them "independent weight". I have not opened *Delgamuukw*. Please check the draft's phrase against the judgment.

## 2. Structural injustice and responsibility

**Young (2006), `young2006responsibility`. Abstract.** From the abstract: the social connection model says "all agents who contribute by their actions to the structural processes that produce injustice have responsibilities to work to remedy these injustices". It differs from the liability model in five features: "it does not isolate perpetrators; it judges background conditions of action; it is more forward looking than backward looking; its responsibility is essentially shared; and it can be discharged only through collective action". Young (2011), `young2011responsibility`: Record only (the book is not open).

**McKeown (2018), `mckeown2018iris`. Part** (accepted manuscript, pp. 1-3, 12-13). The liability model "is backward-looking and isolating, seeking to attribute blame or liability to particular agents for harm that has already occurred" (p. 2). On the connection model, "mere connection to structural injustice generates a nonblameworthy, shared and forward-looking political responsibility to collectively undermine the injustice" (p. 2). Degree depends on position: "Agents with power, privilege, interest or collective ability in relation to a particular structural injustice ought to focus their attention there" (p. 13). McKeown's own claim is that "connection" means individuals "reproduce the background conditions in which they act" (p. 2; the abstract says "individuals reproduce structural injustice through their actions").

**Guljar (2026), `guljar2026reimagining`. Part** (a recent single-author defence; use sparingly). It quotes Young (2011, 186): "The liability model is the appropriate model for assigning responsibility for specific harms that are traceable to the actions of particular agents. The social connection model is the appropriate model for assigning responsibility for structural injustice" (Guljar p. 98). Guljar reads the two as complementary and names Barry and Ferracioli (`barry2013young`, Record) as the indeterminacy critics. I did not read those critics.

**What this gives the paper.** It gives the history/present asymmetry a principled home. The historical practices are discrete wrongs by identifiable bodies, with intent in the record (Knox's convention speech; the statutes), so the liability model fits §2.5: name the courts, parliaments and charters. The platform present is the case §5.4 already concedes, where the paper "cannot prove subjective malicious intent". Young's model assigns forward-looking responsibility to those with the most power over the structure, without proof of intent and without a collective agent called "the global community". That answers §6.1: the four parameters (power, privilege, interest, collective ability, as McKeown p. 13 and Guljar list them) point at the operators of the intermediary.

**What it costs.**

1. *Users share responsibility.* Young includes the victims: the exploited "can be called to a responsibility they share with others" (McKeown p. 13, quoting Young). So §6.1's "not to the individuals trying to navigate it" is stronger than the model allows. The model ranks users' responsibility below operators' by position; it does not remove it. The paper should say "primarily".
2. *The model is forward-looking and non-blaming* (McKeown p. 2). It cannot ground the verdict "failed" for 1901 or 1740. The paper therefore uses two models and has to say so: liability for §3, connection for §6.
3. *Fricker and Young pull apart.* Hermeneutical injustice has no agent (IEP on Fricker); Young's model spreads responsibility across all connected agents; §2.5 wants specific bodies. The liability/connection split is the way to hold all three.
4. I found one application of the model to firms (Bziuk 2022, `bziuk2022can`, Record) and none to algorithmic platforms in this search.

*Bearing:* §2.5, §5.4, §6.1. *Complicates* §6.1 (shared responsibility) and *supports* §5.4 and the §2.5/§6.1 pairing. A political-philosophy referee would expect Young at §2.5.

## 3. Domination and arbitrary power

**Lovett, "Republicanism" (SEP), `lovett2026republicanism`. Part** (sections 1 to 2.2; the workplace passage). Pettit's definition, as quoted: a person enjoys freedom to the extent that no one has "the capacity to interfere in their affairs on an arbitrary basis" (Pettit 1999, 165, as quoted). Three points from the entry bear on the paper.

- *Arbitrary is not unpredictable.* "Just because one is better able to cope with arbitrary power, it does not follow that one's domination is any less."
- *Two accounts of non-arbitrary power.* The procedural one: power is not arbitrary "to the extent that it is reliably controlled by effective rules, procedures, or goals that are common knowledge to all persons or groups concerned". The democratic one: power is not arbitrary "to the extent that it is directly or indirectly controlled by the concerned persons or groups themselves".
- *Not moralised.* Arbitrary power "should not be defined along substantive lines as power that is unjust or illegitimate".

The entry also notes that employers' power is an established republican concern, with "stronger unions and workplace democracy" proposed in response.

**Muldoon and Raekstad (2023), `muldoon2023algorithmic`. Part** (journal pagination). They apply the republican account to ride-hail and delivery platforms and use Rosenblat and Stark (2016), which the draft already cites. On the withheld destination: drivers were told the passenger's rating "but they were not informed about the passenger's destination" (p. 596). Each asymmetry "effectively decreases workers' ability both to understand and contest the decisions that are made over them" (p. 596). On deactivation: "Workers have had their accounts deleted by an algorithm without warning and with no right to contest the decision" (p. 599). They locate the dominator in "owners and managers" acting as a "group agent", and "remain agnostic about the broader question of whether only agents can dominate" (p. 594).

**Hoeksema (2023), `hoeksema2023digital`. Part, through the fetch tool** (abstract, headings, six quotations of under 125 characters; no page locators). He argues that "republicans ought to give priority to structural elements" and that this implies "a more structural response to digital platforms over more direct and individualised forms of control ... such as securing exit options and requiring user consent" (abstract). Also: "domination exists where someone has the capacity to arbitrarily interfere with another".

**Gädeke (2020), `gadeke2020mugger`. Abstract.** Domination "is a structurally constituted form of power". **Aytac (2024), `aytac2024big`. Abstract.** Proposes randomly selected citizen boards to govern Big Tech's algorithmic infrastructure. **Maas (2023), `maas2023machine`. Abstract.** Grounds end-user dependence on developers in "the neo-republican moral wrong of domination" and proposes "increase contestability through design-for-values approaches". Pettit (1997), `pettit1997republicanism`; Pettit (2012), `pettit2012peoples`; Pettit (1996), `pettit1996freedom`: Record. I did not open them and give no quotation from them. I could not verify the "eyeball test" from any text I opened, so I do not describe it.

**Creel and Hellman (2022), `creel2022algorithmic`. Part.** They argue that "isolated arbitrary decisions are not of moral concern except when other rights make nonarbitrariness relevant" (p. 27), and that "the problem with arbitrary algorithms is not fundamentally their arbitrariness but the systematicity of their arbitrariness": "Automated decision-making systems that make uniform judgments across broad swathes of a sector" (p. 27) are the wrong. This is the position behind the draft's Bommasani et al. citation (one hiring model rejecting an applicant across a sector).

**Lazar (2024), `lazar2024legitimacy`. Part** (introduction of the arXiv preprint). Power relations must meet "standards of procedural legitimacy and proper authority"; for governing power, "reasonably competent members of the governed community must be able to determine that they are being governed legitimately and with proper authority", which "can be satisfied only if the powerful can explain their decision-making". This puts the duty to be legible on the powerful, which is the paper's thesis in political-philosophy terms.

**Anderson (1999), `anderson1999point`. Part** (introduction; pp. 314-319; third-party copy with journal pagination). Her relational account: the negative aim of egalitarian justice is "to end oppression, which by definition is socially imposed" (p. 288). "Equals are not dominated by others; they do not live at the mercy of others' wills" (p. 315). On capabilities and standing: "To be capable of standing as an equal in civil society requires literacy" (p. 319). That sentence puts the paper's §2.6 and §3.1 in one place: literacy is a condition of equal standing, at a level she makes context-relative ("In other countries, multilingual literacy might be required for equal standing", p. 319); that gating it is a relation of inequality is my inference, not Anderson's wording. Anderson (2017), `anderson2017private` (Record), the book on employers as private governments, is the natural source for the platform case; I could not open it.

**Do the registrar and the platform count?** On the definition as quoted, yes. A registrar who chooses the passage and judges the answer, with no rules known to the examinee and no way to contest the result, has "the capacity to interfere ... on an arbitrary basis"; the *Katzenbach* record the draft already cites (discretion left to local officials) fits the procedural test. A platform that deactivates a driver "without warning and with no right to contest" meets the same test (Muldoon and Raekstad p. 599).

**What it costs, and where it cuts against the paper.**

1. *Predictability is not freedom.* §6.3 says declared envelopes create "predictable conditions where users can learn and respond". On the republican account that is at best half a remedy. The procedural view asks for rules that are common knowledge, which declared envelopes supply, but a declared rule the powerful can change at will does not end domination, and the democratic view asks for control by those affected. The paper should say declared envelopes are necessary, and add a contestation route (§6.4 counter-delegation is the natural carrier).
2. *Exit is not enough.* Hoeksema names "securing exit options and requiring user consent" as the standard republican response and argues for more. §6.2 (structural refusal) is exit-shaped. The paper should say what backs it: a duty on the operator, not only an alternative path.
3. *Arbitrariness is not the whole wrong, or not a wrong at all, on one reading.* Creel and Hellman say isolated arbitrary decisions "are not of moral concern except when other rights make nonarbitrariness relevant" (p. 27), so a registrar who gates a right such as the vote falls under the exception. If the paper takes the republican line for the registrar and the Creel-Hellman line for the Bommasani cell, it should say why both hold: the registrar's power was discretionary and unchecked; the hiring model's harm is the sector-wide exclusion.
4. *The sources I read name a dominator.* Muldoon and Raekstad find the dominators in owners and managers, though they "remain agnostic about the broader question of whether only agents can dominate (and not impersonal systems or ideologies)" (p. 594). That fits §2.5. It also means the algorithm is the instrument, and the paper's intermediary is a place where an owner's power sits.
5. *The triad.* The sources I read describe company over worker. The paper's claim that the intermediary dominates both of two coordinating parties is not in them. I found no republican account of that triadic case.
6. *Counter-evidence.* A 2026 study of Oslo taxi drivers (Oppegaard, `oppegaard2026dependence`, Abstract only (Crossref abstract, issued 2026-04-08)) reports drivers who find the algorithm "opaque, unpredictable, and non-negotiable" but do not experience it as control, partly because they can work for several platforms. Domination does not depend on how it is felt, on the republican view, but a referee can raise it.
7. *Internal standards.* Non-domination is a present-day theory. The paper's ruling forbids it as the test of failure for 1901. The answer is to use domination as the *description* of what the five positions share and keep the three internal standards as the *test* (section 8 below).

*Bearing:* §2.6, §3.1, §4, §5.3, §6.2 to §6.4. *Supports* the diagnosis, and *complicates* §6.2 and §6.3.

## 4. Capabilities and literacy

**Robeyns and Byskov, "The Capability Approach" (SEP), `robeyns2025capability`. Part.** Capabilities are "the doings and beings that people can achieve if they so choose"; functionings are "capabilities that have been realized". The entry uses literacy as its example of a general capability ("being literate, being mobile, being able to hold a decent job"). The mechanism it names is the *conversion factor*: whether a resource becomes a functioning depends on personal factors (the entry lists "reading skills" among them), social factors ("public policies, social and cultural norms, practices that discriminate, societal hierarchies, or power relations related to, for example, class, gender, race, or caste") and environmental factors. Nussbaum's list is given with "senses, imagination and thought" among the ten central capabilities (the entry cites Nussbaum 2006: 76-78).

**Nussbaum (2003), `nussbaum2003capabilities`. Abstract**, **Robeyns (2005), `robeyns2005capability`. Abstract**, **Nussbaum (2000), `nussbaum2000women`. Record.** Nussbaum argues the approach gives guidance for justice "only if we specify a definite set of capabilities as the most important ones to protect" (abstract). I did not verify any passage in which Nussbaum names literacy in her list; I recall one but cannot cite it. Sen's *Development as Freedom* did not come up as a clean Crossref record, so I list it as unverified.

**Fit.** The capability approach supports §2.6: reading is a capability worth having, the people who sought it were pursuing real freedom, and a *capability* is something one can choose, which matches Graff's require/reward distinction already in the drafts. The conversion-factor vocabulary also states the paper's thesis in the approach's own terms: AI literacy works on a *personal* conversion factor (skill); the harms the paper describes sit in *social* ones (rules, power relations, who holds the test). Douglass learning to read and gaining no leverage (§5.1) is a personal factor raised while a social factor stayed shut.

**Cost.** The approach needs a list or a threshold to guide policy (Nussbaum 2003), which is a present-day commitment; the paper can use it for §2.6 and §5.1 as a description of why literacy was valued, not as a test of historical failure. Anderson (1999, p. 319) is the shorter route to the same point.

*Bearing:* §2.6, §5.1, §6.1. *Supports.* A referee in development ethics would expect Sen and Nussbaum if "literacy is valuable" is argued philosophically.

## 5. Judging the past

**Fricker (2010), `fricker2010relativism`. Full** (Sheffield author copy; page numbers are the copy's). This is the most useful text for §2.3 and §2.4.

- She argues that Williams's relativism of distance is "unconvincing, even incoherent; but also that it is detachable from the rest of Williams' moral philosophy" (abstract, p. 1). She keeps a narrower thesis: "when an agent's moral shortcomings by our lights are a matter of their living according to the moral thinking of their day, judgements of blame are out of order" (p. 1).
- She adds a second judgement that stops short of blame, "moral-epistemic disappointment", directed at "an individual agent whose behaviour we regard as morally lacking, but who was not in a historical or cultural position to think the requisite moral thought" (p. 2).
- The test for both is *availability*: "depending on whether the form of moral thought to which we would hold them was sufficiently available, despite not yet qualifying as routine" (p. 19). For blame the thought must be "sufficiently routine in the collective moral repertoire"; for disappointment "sufficiently close to becoming part of a newly emerging routine" (p. 19). She asks whether "one (or five, or ten) schoolboy[s]" objecting would make a thought available, and says this "can only be a matter of judgement" (p. 19).
- On Rosen (2003): she agrees "that non-culpable moral ignorance releases the agent from blame", but says Rosen "casts the net of nonculpable ignorance extraordinarily wide" (p. 14). Her own line: "if someone wasn't in a cultural-historical position to know any different, then they weren't to know, as we say, and cannot appropriately be blamed. If, however, someone (whose thinking is not structurally hampered) deliberates as best they can, but arrives at a bad moral judgement, then they remain blameworthy" (p. 14).

*What it does to the paper's ruling.*

- *Supports standard 1 (contemporary objection).* A recorded objection by a contemporary is the evidence that the thought was available. This gives the standard a citable philosophical rationale: Douglass (1845) makes the bar on teaching reading an available thought. It also shows the standard's limit: an objection by a few people is not decisive (her schoolboys), so the paper should claim "available", not "universal".
- *Undermines the use of Moody-Adams as the only anchor.* Fricker holds that structural (cultural-historical) ignorance is non-culpable. Moody-Adams, as `T_adjudication.md` §9.4 summarises her, holds that a culture cannot make criticism unavailable ("affected ignorance"). They disagree about the very point §2.4 turns on. Fricker's text does not mention Moody-Adams, so far as this copy shows (I searched it). A referee who knows Fricker will raise her; the paper should cite both and say which it follows for which practice.
- *Shows the ruling is stricter than the philosophy requires.* Fricker limits *blame* over distance. She allows a critical judgement of the agent "by our lights" (disappointment). So the rule "no present-day standard" is a choice of the paper, as `T_adjudication.md` §9.4 point 2 already says, and not forced by Williams. Williams's *Ethics and the Limits of Philosophy* (1985) I did not open; I know the relativism of distance only through Fricker, so the paper should not cite Williams for the rule unless the author reads him.
- *Equivocation to avoid.* Williams's "internal reasons" (which Fricker discusses before her section on blame) are reasons grounded in an agent's own motivations. They are not the same thing as the paper's "internal standards", which are standards internal to a period or an institution.

**Rosen (2003), `rosen2003culpability`. Abstract:** an agent "is culpable for his action only if he is culpable for the ignorance from which he acts", and the author argues this holds for moral ignorance too. It underlies Fricker's discussion and supports the culpable-ignorance route that Moody-Adams takes. **Calhoun (1989), `calhoun1989responsibility`; Scanlon (2008), `scanlon2008moral`; Arpaly (2002), `arpaly2002unprincipled`: Record only.** I verified that each exists (Scanlon's "Blame" chapter, pp. 122-214, has its own record) and did not open them, so I do not characterise their arguments. They are candidates if the author wants a fuller account of blame; none is needed for the three internal standards.

**Is internal critique a recognised method?** Yes. Two citable statements:

- **Walzer (1988), `walzer1988interpretation`. Part** (the Tanner Lectures delivered in 1985; first lecture, printed pp. 33-43; the book of the same title is Harvard University Press, 1987, not opened). He describes "the local judge, the connected critic, who earns his authority, or fails to do so, by arguing with his fellows" (pp. 33-34), for whom "Social criticism ... is an internal argument" (p. 34). He asks of this critic: "are standards available to him that are internal to the practices and understandings of his own society, and at the same time properly critical?" (p. 34). His answer includes: "The same men and women who act badly create and sustain the standards by which (at least sometimes) they know themselves to act badly" (p. 42). That sentence is the philosophical statement of standard 2 (the institution broke its own professed standard). The "connected critic" is the name for standard 1 (Douglass is one).
- **Celikates and Flynn, "Critical Theory (Frankfurt School)" (SEP), `celikates2023critical`. Part.** Section 2.1 separates internal critique ("standards and standpoints that are already recognized by those criticized") from external critique, and describes immanent critique as a third model that "secure[s] its normative resources ... from the (often implicit) normative structures and epistemic possibilities of the practices and self-understandings" of a society. It credits Jaeggi (2014 [2018]) with developing the method. **Jaeggi (2018), `jaeggi2018critique`. Record** (not opened).

*Consequence for the paper.* The author's standards 2 and 3 are internal critique in the narrow sense. Immanent critique, as the SEP states it, allows *implicit* norms too, which would widen the rule beyond "professed" standards. The paper should keep the narrow wording, name Walzer for it, and say it is the narrow form.

**Archer and Matheson (2024), `archer2024different`; Levy (2024), `levy2024does`; Mason (2015), `mason2015moral`; Peacock (2011), `peacock2011inability`:** already in `X_counter_case.md`. None of them contradicts the section above.

*Bearing:* §2.3, §2.4. *Supports standard 1, complicates §2.4.* Fricker (2010) and Walzer are the two a philosophy referee would expect to see.

## 6. Technology ethics proper

**Winner (1980), `winner1980artifacts`. Part, via the 1986 reprint on a course page** (no page marks). He distinguishes two ways artifacts carry politics: where "the invention, design, or arrangement of a specific technical device or system becomes a way of settling an issue in the affairs of a particular community", and "inherently political technologies". For the paper the relevant passage is on intent: "to recognize the political dimensions in the shapes of technology does not require that we look for conscious conspiracies or malicious intentions". His example is access for disabled people: designs "arose more from long-standing neglect than from anyone's active intention. But once the issue was brought to public attention, it became evident that justice required a remedy". That is §5.4 and §6.1 in one paragraph. Caution: a search snippet says the Moses-bridge example is disputed (Joerges); I did not verify that, and the paper should not lean on the bridges. The JSTOR copy I opened had an unusable text layer, and Crossref has no record for the 1980 article, so the 1980 citation rests on that copy's header and on search results. The author should check the Daedalus pages.

**Green (2021), `green2021contestation`. Part.** Tech ethics, he says, is "vague and toothless, has a myopic focus on individual engineers and technology design, and is subsumed into corporate logics" (abstract). On the second: "individual engineers typically have little power to shift corporate strategy" (p. 213). On the first: "ethics oversight boards and ethics principles lack the authority to veto projects or require certain behaviors" (p. 212).

**Mittelstadt (2019), `mittelstadt2019principles`. Part** (arXiv). AI development lacks "(1) common aims and fiduciary duties, (2) professional history and norms, (3) proven methods to translate principles into practice, and (4) robust legal and professional accountability mechanisms". The absence of a fiduciary relationship means "users cannot trust that developers will act in their best interests" (section 2.1).

**Bietti (2020), `bietti2020ethics`. Abstract:** "ethics" is "weaponized in support of deregulation, self-regulation or hands-off governance". **Rességuier and Rodrigues (2020), `resseguier2020ai`. Abstract:** "Using ethics as a substitute for law risks its abuse and misuse." **Wagner (2018), `wagner2018ethics`; Floridi (2019), `floridi2019translating`: Record.**

**Matthias (2004), `matthias2004responsibility`. Record. Santoni de Sio and Mecacci (2021), `santonidesio2021four`. Abstract:** the responsibility gap is "at least four interconnected problems", in "culpability, moral and public accountability, active responsibility". **Nissenbaum (2004), `nissenbaum2004privacy`. Part** (abstract; the two norm types, appropriateness and distribution). **Friedman and Hendry (2019), `friedman2019value`. Record.**

**Which belong in §6.**

- *Must:* Green and Mittelstadt, for §6.1 and §6.5. The draft's design obligations are "architectural"; the literature says principles without enforcement are toothless and that "designers" must not mean individual engineers. The paper should state that the duty falls on the organisation that controls the test, the access and the record, and that it needs legal backing (§6.5 now mentions law only for monopoly).
- *Should, after reading:* Matthias (2004) with Santoni de Sio and Mecacci (2021), for §5.2 and §5.3. The paper's adaptivity claim (§5.2) is close to Matthias's learning-automata gap, and the "void of safeguards" (§5.3) is a gap in what Santoni de Sio and Mecacci call accountability. I could not open Matthias.
- *Optional:* Bietti, Wagner, Floridi (the ethics-washing cluster; one cite suffices once Green is in); Nissenbaum (declared envelopes as information-flow norms; she builds on Walzer's "spheres of justice" per her abstract); value sensitive design (a method for §6, not an argument). Vallor (2016, 2024) is already in the drafts and I did not re-check it.

## 7. Paternalism and responsibilization

**Giesler and Veresiu (2014), `giesler2014creating`. Part** (a Journal of Consumer Research article; author-posted copy with journal pagination). They theorise "consumer responsibilization" as four processes, the P.A.C.T. routine (personalization, authorization, capabilization, transformation), "through which responsibility is shifted away from the state and corporations and the responsible consumer subject is shaped" (p. 841). One of their four cases is the *financially literate consumer*. On it: "the ethos of financial literacy, with its emphasis on values such as self-control, modesty, economic efficiency, and hard work, justifies the inequality of situations" (p. 852). The financially literate consumer is introduced at p. 851, in a study of initiatives at the World Economic Forum.

**Shamir (2008), `shamir2008age`. Abstract:** "the moralization of markets further sustains, rather than undermining, neo-liberal governmentalities". **Maniates (2001), `maniates2001individualization`. Abstract:** "When responsibility for environmental problems is individualized, there is little room to ponder institutions, the nature and exercise of political power, or ways of collectively changing the distribution of power and influence in society."

**Does it already say what the paper says about AI literacy?** For financial literacy, yes: Giesler and Veresiu show literacy-as-responsibilization, in a marketing-field journal. For AI literacy I found nothing in one web search using "responsibilization" and "governmentality"; adjacent items surfaced (an arXiv item titled "AI Literacy: An Exercise in Power-Knowledge", which I did not open and whose identifier I could not confirm). Kamperman and Graff (2026), already in the drafts, make the historical version of the point. So the paper's contribution is not "AI literacy individualises responsibility", which this literature supplies, but the history of what institutions did with literacy and the triadic positions.

*Bearing:* the introduction, §3.5, §4 row 5. *Supports and narrows the novelty claim.* A marketing-ethics reader would expect Giesler and Veresiu at §3.5 and §4 row 5.

## 8. What a moral philosopher would say the outline gets wrong or leaves out

1. *The wrong is never named.* The five practices are called "abuses", "extraction" and "failures". A philosopher asks what makes each wrong, and to whom. The sources point to different wrongs: the gate and the registrar are domination (Pettit); the withheld competence is oppression and unequal standing (Anderson p. 288, p. 319); record over voice is epistemic injustice (Fricker, Symons and Alvarado); the monopoly is domination over the means (Anderson 2017 is the lead, unopened); the oversold promise is responsibilization (Giesler and Veresiu). One umbrella term is enough; non-domination is the best candidate (section 9).
2. *The design obligations have no stated ground.* This is the asymmetry objection. The paper forbids a present-day standard when it judges 1901, then states three obligations for 2026 without saying on what standard they rest. A philosopher will ask why the past is judged internally and the present is not. A possible answer, which is my proposal and not a finding: apply the same three internal tests to today. The AI-ethics guidelines profess non-maleficence (the draft cites Jobin et al.: 60 of 84 sets); the platforms break or ignore it (standard 2). Contemporary voices object (Berthon, Pitt and Campbell 2019; Williams 2018; Kamperman and Graff 2026) (standard 1). "AI literacy" is promised as the remedy and has not delivered (standard 3). That makes the obligations internal to our era's own commitments.
3. *A duty with no claimant.* A design obligation without a rights-holder is toothless. The sources say so directly (Green; Mittelstadt; Rességuier and Rodrigues; Bietti). The paper should say who holds the claim: the user (a right to refuse, a right to contest), a regulator, or the public. Lazar's publicity requirement and the republican democratic account (control by the affected) both name the governed as the claimant. The three obligations then become the content of a claim, not advice to firms.
4. *Responsibility has two models and the outline uses one for both periods.* §2.5 and §6.1 mix them (section 2 above).
5. *Is the internal-standards rule arbitrary?* Not as a method (Walzer; the SEP's internal/external/immanent triad). But three gaps remain. (a) It lets off a practice nobody objected to and nobody had a professed standard against; Moody-Adams and Fricker disagree on whether that silence excuses. (b) The surviving record of objection is itself shaped by who could write, which is the paper's own theme; the rule should say so. (c) It judges the practice, and Fricker (2010) shows the philosophical issue is mostly about judging persons; the paper should say that its verdicts are on practices and institutions and that it makes no claim about individual blame.
6. *Exit and voice.* The brief lists Hirschman; the outline does not use him by name. Hoeksema (2023) argues that exit and consent are the weak republican answers to platform power. If Hirschman appears elsewhere in the drafts, §6.2 (refusal, an exit) and §6.4 (counter-delegation, a voice) map onto his two terms, and Hoeksema is the sharpest published warning against stopping at exit.
7. *The triad.* The philosophical literature I read treats domination as a dyad. The paper's claim that one intermediary binds two parties who coordinate through it has no counterpart in the sources. That is a place where the paper adds something, and a place a referee will test.

## 9. Synthesis, in the brief's order

### (i) Ranked must-include list

The ONE framework I judge the best fit for the whole paper is **republican non-domination** (Pettit 1997, 2012; applied to platforms by Muldoon and Raekstad 2023 and Hoeksema 2023). Reasons: (a) it names, in one idea, what the five practices share (arbitrary power held by whoever holds the test, the access and the record) without needing proof of intent (Muldoon and Raekstad do, however, place the dominator in owners and managers acting as a "group agent of domination", p. 594); (b) the entry in the SEP says arbitrary power is *not* defined as unjust power, so the concept is a description, not a moral verdict, and sits alongside the internal-standards ruling instead of overriding it; (c) its two accounts of non-arbitrary power (rules that are common knowledge; control by the affected) match declared envelopes (§6.3) and counter-delegation (§6.4), and its warning that exit is not enough tells the paper what to add to §6.2; (d) it has been applied to the paper's own cited case (Rosenblat and Stark, in Muldoon and Raekstad). The condition: use domination to *describe* the positions, keep the three internal standards as the *test* of failure, and read Pettit in the original before citing him; I could not open either book.

Ranked works, with sections:

1. **Pettit (1997) or (2012), with Muldoon and Raekstad (2023) and Hoeksema (2023).** Whole paper; §4, §6.2 to §6.4. Names the wrong and shapes the remedies.
2. **Young (2006, 2011) with McKeown (2018).** §2.5, §5.4, §6.1. Responsibility without proof of intent or a collective agent; needs the liability/connection split.
3. **Fricker (2007) with Symons and Alvarado (2022).** §3.3, §4 row 3, §5.3. The algorithm-over-witness case is the §3.3 mechanism, printed.
4. **Fricker (2010).** §2.3, §2.4. The availability test; the counter to Moody-Adams that a referee will raise. The only text here I read in full.
5. **Walzer (1988) (and Celikates and Flynn, SEP).** §2.3. The citable statement of internal critique.
6. **Anderson (1999).** §2.6, §3.1. Literacy as a condition of equal standing (p. 319); the gating-as-oppression reading is my inference from p. 288 ("to end oppression, which by definition is socially imposed") and not Anderson's wording.
7. **Green (2021) and Mittelstadt (2019).** §6.1, §6.5. Designers must mean the organisation; principles need enforcement.
8. **Giesler and Veresiu (2014).** Introduction, §3.5, §4 row 5. Responsibilization in a marketing-field journal.
9. **Creel and Hellman (2022).** §3.1, §4 row 1. What is wrong with the Bommasani cell.
10. **Winner (1980).** §5.4, §6.1. No conspiracy needed; read the Daedalus text first.
11. **Lazar (2024).** §6.3. The duty to explain falls on the powerful.
12. **Robeyns and Byskov (SEP) with Sen and Nussbaum.** §2.6, §5.1. Personal versus social conversion factors, in the thesis's own terms.

### (ii) Optional

Kay et al. (2024) as a field map; Dotson (2011, 2012) and Medina (2011, 2013) if the epistemic-injustice paragraph grows; Hull (2023), Pozzi (2023), Tsosie (2017); Gädeke (2020), Maas (2023), Aytac (2024), Anderson (2017); Guljar (2026); Matthias (2004) and Santoni de Sio and Mecacci (2021) (should be read first); Nissenbaum (2004); Friedman and Hendry (2019); Bietti, Wagner, Floridi, Rességuier and Rodrigues; Shamir (2008), Maniates (2001); Rosen (2003).

### (iii) Works that cut against the paper

| Work | What it would force the paper to concede |
| --- | --- |
| Hoeksema (2023) | Exit and consent are inadequate; §6.2 needs a backing duty. |
| Lovett (SEP), on Pettit | Predictability does not end domination; §6.3 is half a remedy. |
| Creel and Hellman (2022) | An isolated arbitrary decision is "not of moral concern except when other rights make nonarbitrariness relevant"; the sector-wide exclusion limits "people's opportunities in ways that are morally troubling" (p. 27). |
| McKeown (2018) on Young | Users share political responsibility; the model is forward-looking and cannot say "failed". |
| Fricker (2010) | Structural ignorance is non-culpable; the "no present standard" rule is a choice, not a philosophical requirement; Moody-Adams is contested. |
| Fricker (2007) via IEP | Hermeneutical injustice is "purely structural" and has no agent; §2.5 needs a reply. |
| Green (2021); Mittelstadt (2019) | "Designer" obligations are myopic if they mean engineers, and toothless without enforcement. |
| Giesler and Veresiu (2014) | The individualisation of responsibility through literacy is already documented for finance; the paper's novelty narrows. |
| Oppegaard (2026), snippet only | Some Oslo taxi drivers "do not necessarily experience it as control" (Crossref abstract), though the author still calls it "a non-interventionist form of control". |
| Walzer (1988) | Criticism that stays inside a culture can only press on that culture's own commitments, and the "connected critic" worry about hypocrisy and distance applies. |

### (iv) Missing aspects, as paragraph topics (not prose)

1. *What the five practices have in common*: a short passage naming arbitrary power held by test-holder, access-holder and record-holder as the shared wrong; kept apart from the internal standards that decide "failure".
2. *The ground of the §6 obligations*: the three internal standards applied to the present (professed non-maleficence; contemporary objection; the unrealised promise of AI literacy).
3. *Who holds the claim*: user, regulator or public, and what makes the duty enforceable.
4. *Two models of responsibility*: liability for the historical bodies; connection by position for platform operators; users' residual share.
5. *Epistemic injustice for the record*: credibility excess for the written or scored output; the Symons and Alvarado parole case beside *Marshall* and Waitangi.
6. *Responsibilization*: one paragraph at §3.5 with Giesler and Veresiu and Maniates.
7. *The triad*: a note that existing domination theory is dyadic and the paper's intermediary binds two parties.

### (v) What I could not open

- **Not opened, record verified:** Fricker (2007); Dotson (2012); Medina (2011, 2013); Hull (2023); Young (2011); Pettit (1996, 1997, 2012); Anderson (2017); Nussbaum (2000); Calhoun (1989); Scanlon (2008); Arpaly (2002); Jaeggi (2018); Friedman and Hendry (2019); Matthias (2004); Floridi (2019); Wagner (2018); Miller (2011); Barry and Ferracioli (2013); Bziuk (2022); Oppegaard (2026).
- **Bot-walled or redirected:** Wiley (Gädeke 2020; McKeown's journal PDF, replaced by the Oxford accepted manuscript), ACM (Bietti), SAGE (Rességuier and Rodrigues), Springer (Hull; Symons and Alvarado journal version, replaced by the author preprint; Maas; Santoni de Sio and Mecacci; Floridi), PhilArchive (Aytac), SSRN (Hull), Northeastern (Winner), the Utrecht repository (login).
- **Not found as a clean database record:** Winner (1980) in Crossref and OpenAlex (the JSTOR copy I opened had an unusable text layer); Sen, *Development as Freedom*; Williams, *Ethics and the Limits of Philosophy* (1985); Walzer's 1987 book (reviews only).
- **Named in the brief or by a source, not verified by me:** Pettit's "eyeball test"; Nussbaum naming literacy in her list; Byrnes and Spear (2023) as coiner of "algorithmic epistemic injustice" (reported by Kay et al. only); Hibbitts (1992) on the oral as fraud; Joerges on the Moses bridges; the arXiv item on AI literacy as power-knowledge.
- **Not searched:** applications of the social connection model to AI beyond Bziuk; any work on the *triad* in republican theory; Pohlhaus on wilful hermeneutical ignorance (I recall the term but did not search); Winner's Daedalus pagination.

## Counts by read depth

By the highest depth reached. "Part" means I opened the text and read the named sections; the page locators above are from those sections.

| Depth | Count | Works |
| --- | --- | --- |
| Full | 1 | Fricker (2010) |
| Part, text opened | 18 | Anderson (1999); Walzer (1988); Symons and Alvarado (2022); Kay et al. (2024); McKeown (2018); Guljar (2026); Green (2021); Mittelstadt (2019); Muldoon and Raekstad (2023); Creel and Hellman (2022); Lazar (2024); Winner (1986 reprint); Giesler and Veresiu (2014); Nissenbaum (2004); Lovett SEP; Robeyns and Byskov SEP; Celikates and Flynn SEP; Sinclair IEP |
| Part, through the fetch tool only | 1 | Hoeksema (2023) |
| Abstract only | 15 | Young (2006); Dotson (2011); Pozzi (2023); Tsosie (2017); Gädeke (2020); Aytac (2024); Maas (2023); Bietti (2020); Rességuier and Rodrigues (2020); Shamir (2008); Maniates (2001); Santoni de Sio and Mecacci (2021); Rosen (2003); Nussbaum (2003); Robeyns (2005) |
| Record only | 23 | listed in (v) |

That is 58 works with a verified record, of which 20 were read in part or in full. Ten further leads have no clean database record or no verified source text (six named in (v), plus Sen 1999, Williams 1985, Walzer's 1987 book and the 1980 Daedalus original of Winner); none is in the ranked list.
