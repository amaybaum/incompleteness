# EF-1, r7: finite observational descriptions at a fixed horizon, uniform forms, and a finite-hidden-memory draft

**r7 is r6 with the attribution of ten #1169 comments corrected (table "r7 changes", at the end); it
has not been reviewed in this form. r6 is r5 with nits 1–8 of its independent recheck applied (table
"r6 changes"). r5 is a targeted correction of r4.** Paper-only and
read-only. No manuscript, Lean module, census entry or
record is edited; nothing is computed, built, committed or pushed, and no GitHub record is written.
Comments on #1169 were read through the GitHub tool for one purpose: to quote the owner and the adopted directions exactly.
Lean source was read, not built, so "kernel" below means "stated in a module on `main`". Every
citation is read at `main` `bf89ba133ee9f2926a317e8af067ccaa862ce2db`. Markings: **[IR]** is a
reading made here and not stated on `main`; **[IR, proof here]** is an [IR] statement whose proof is
written out here in full; **[unreviewed proof]** is a proof written out here that no independent
review has checked in the form given; **[checked by the review of r4]** is a paper proof that the
independent review of r4 re-derived step by step and found sound, as the statement with its stated
hypotheses (one independent check; not kernel-checked); **[checked by the recheck of r5]** is the
same for the independent recheck of r5, `RECHECK-EF-1-r5.md`; **[reviewer's lemma; re-derived by
writer; not independently checked]** and **[reviewer's refinement; not independently checked]**
were r5's marks for statements first given in the review of r4 and re-derived here by the writer;
the recheck of r5 has since checked those statements, and the two marks remain only in the table
"r5 changes". No premise is adopted, no status is decided and no result is
declared recovered. The finite-hidden-memory hypothesis of §5 is a draft for the owner, not a
proposal for adoption.

**Inputs of r5.** `EF-1-r4.md` (sha256
`b429d3afa017bfc260b1eea1eee169632902d5a5bb485019eaf27b55f537d1b1`, verified before reading) and its
independent review `REVIEW-EF-1-r4.md` (ACCEPT WITH CHANGES, findings 1–11). Each finding was
checked first-hand, against `main` or by re-derivation, before it was applied. All eleven are
applied and none is disputed; the points of scope that remain are in §12. While r5 was being written the coordinator relayed five further owner requirements,
labelled O15–O19 below and since recorded in c.6897859755 and c.6897946443; they are applied. What r5 changes is listed in the table "r5 changes" after
the response table; everything else is r4's text, unchanged.

**Inputs of r4 (kept).** `EF-1-r3.md` (sha256 `bba62a1431aa5759b3419baa0432817a097c3090baf655b2b4015057c208c224`,
verified before reading) and its independent review `REVIEW-EF-1-r3.md` (ACCEPT WITH CHANGES,
findings 1–13). Each finding was checked first-hand against `main` or by re-derivation before it was
applied. None is disputed in substance. Two are applied with a correction found while checking
(finding 5, the example; finding 3, an alphabet condition), and the points where this file and the
review still differ are listed in §12. During the round the coordinator relayed three further owner
requirements (O12–O14 below, since recorded in c.6897455387); they are applied. `A1-VALIDITY-GEM-r3.md` (cited as "the validity
note") and `A1-IMPACT-AUDIT-r2.md` with its review (cited as "the audit") are used for labels only.
Abbreviations: `Main:n` is `papers/Main.md:n`, likewise `GR`, `Sub` (Substratum), `Struct`
(Structure). Lean paths are under `verification/lean-mathlib/OIBridge/`.

## Owner directions and adopted directions in scope (2026-11-15)

**Source of the quotations.** Each quotation below is copied from the named comment on #1169, read
in this round. The comments are posted from the owner's account by the coordinating session and
record the quoted text as block quotations; the text here is taken from those block quotations.
"c.N" is the comment id. The latest comment on the issue when this file was written is c.6897946443.

**Attribution.** The owner's own words are those quoted from c.6894872312, c.6895032895 and
c.6896070253. The texts quoted in c.6896252651, c.6896496410, c.6896771264, c.6896890693,
c.6896940222, c.6897254631, c.6897455387, c.6897859755, c.6897946443 and c.6898395533 are review
text the owner relayed and adopted, not the owner's own words; the owner stated on 2026-11-15,
"Relayed, and I adopt them." (#1169 c.6898760764). In this file **adopted direction (c.N)** is
short for "adopted direction (review text relayed and adopted by the owner, #1169 c.N)". The
quoted text is unchanged.

**c.6894872312** (A1 results and the visible sector).
- "The whole idea around why it looks quantum is that the visible sector is finite. So I think we
  need to limit A1 results so it only applies to the visible sector, which we know is indeed finite."
- "Yes, start the impact audit. Anything that can't align with the visible sector only condition
  should be either recovered as such, or removed completely."

**c.6895032895** (is A1 valid).
- "Is A1 a valid assumption or not?" and, on the coordinator's proposal of a paper-only review,
  "Yes please proceed as suggested".

**c.6896070253** (this unit).
- "Yes proceed as suggested." The same comment continues with a question that opens "Perhaps it's
  possible to show that the effective hidden sector is finite", and asks whether a matching
  statement about the total would follow. The adopted direction of c.6896496410 tightened that wording (item 1
  below). This file answers the question in the tightened form and makes no finiteness claim about
  the substratum as a whole, under any "effective" label.

**c.6896252651**, adopted direction (wording; the required check).
- "The key distinction is "these results currently establish no justified constraint on
  observations", rather than "these results cannot constrain observations." The first describes the
  audit's finding; the second would require a stronger proof."
- "One particularly important check: is effective finiteness justified independently of A1, and is
  it sufficient for the specific results it is meant to recover?"

**c.6896496410**, adopted direction (three statements tightened; order of the claims).
- Lead: "This gives a promising recovery route: finite observational descriptions over any fixed
  horizon, without assuming a finite universe. It does not yet recover any particular result until
  that result's proof is checked."
- **O1** (item 1, after the coordinator's sentence that the adopted direction corrects): "What is finite is the
  information needed to determine the observations over those n steps. That does not make the
  actual whole substratum finite. The missing proof step should establish that matching initial data
  on the relevant patch gives matching observation histories."
- **O2** (item 2, likewise): "A finite connected region is sufficient, but necessity needs proof. An
  infinite connected system could contain sites that never affect the observer under its actual
  dynamics. Distinguish the growing geometric neighbourhood from the sites that genuinely influence
  observations."
- **O3** (item 3, likewise): "For an autonomous deterministic finite system, observations must be
  eventually periodic, allowing an initial transient. With continuing external inputs or settings, a
  finite system can produce nonperiodic output. The claim needs its operational conditions stated."
- **O4**: "So the defensible all-time conclusion is: the fixed-horizon argument does not, by itself,
  supply one finite model valid for every horizon. That is narrower than proving such a model
  impossible."
- Recurrence: "The recurrence conclusion is sound as stated: a finite description for a chosen
  horizon supplies no recurrence guarantee within that horizon."
- **O5**: "For recovery, the crucial check is the order of the claims:" then "For every horizon,
  there exists a finite description: potentially established here." and "There exists one finite
  description valid for every horizon: not established here." and "Any audited result requiring the
  second cannot be recovered merely by proving the first." The two forms are called **F-each** and
  **F-one** in this file.

**c.6896771264**, adopted direction (settings and policies).
- **O6**: "One detail belongs in the patch lemma: when settings or inputs are present, the comparison
  must hold them fixed—or specify the same adaptive policy and include the information it uses.
  Matching the initial patch alone need not give matching observations under different
  interventions."

**c.6896890693**, adopted direction (qualifications to the intervention lemma and the sufficiency result).
- "The counterexample identifies a substantive gap: the relevant patch must cover the full
  experiment, including interventions and the information used to choose them. A proof for the
  selected model does not establish the general intervention claim."
- **O7**: "Fixed horizon: show that the enlarged patch remains finite under the permitted
  interventions and policies. Including their read sites repairs the dependency statement;
  finiteness still requires those reads to have finite support."
- **O8**: "All horizons: finitely many influencing sites suffice for one autonomous finite model only
  if the complete relevant state is finite—including any controller or policy memory—and its
  evolution is determined by that state. An unbounded external controller is not made finite by
  acting on finitely many sites. If inputs remain external, state the result explicitly as a finite
  model with inputs."
- **O9**: "For Bell experiments, including the setting-generation regions establishes dependency
  coverage; it does not establish measurement independence. That remains a separate premise to
  track."
- **O10**: "These are qualifications to the repair and the new sufficiency result, within the
  existing review scope. The basic patch lemma can stand on its reviewed terms while the broader
  intervention claim is corrected. Nothing is recovered or adopted yet."

**c.6896940222**, adopted direction (assessment; what a finite description preserves).
- "The fixed-horizon idea is convincing. Its ability to rescue the A1-dependent physics is still
  unproved."
- "The repair works provided the interventions and their controllers satisfy the required
  finite-dependency conditions. Arbitrary interventions do not automatically satisfy them."
- The four-row table of that comment, cell by cell: "A finite description suffices for each fixed
  horizon" — "Convincing under the stated locality and finite-state premises"; "That description
  preserves everything needed by a particular A1-dependent theorem" — "Requires a separate proof";
  "One finite autonomous model works for all horizons" — "Not established by the fixed-horizon
  argument"; "Nature must recur, or observations obey a new measurable bound" — "Does not follow
  from this argument alone".
- **O11**: "A finite description of observations need not preserve the original system's
  bijectivity, invariant measure, recurrence structure, or other properties a downstream proof uses.
  That is the main risk: transferring properties of finite whole systems to finite observational
  descriptions without justification." And: "My judgment is therefore: keep effective finiteness as
  a candidate replacement premise, but give it no recovery credit until each theorem's actual
  requirements are checked."

**c.6897254631**, adopted direction (derived lemma; premise separation). Labelled
**OP** here. The review of r3 calls it "O12"; that label now belongs to a later item, below.
- "That correction is right: if the required conditions are already established, per-horizon
  finiteness is a derived lemma, not a new assumption. "Candidate replacement" describes its
  possible role in proofs that currently use A1. My earlier wording blurred that distinction."
- "One separation will help: finite dependency sets and finite alphabets establish the finite
  observational description. A normalized starting law supplies probabilities on that description;
  it is not needed merely to establish finiteness. Any stronger distributional properties require
  their own justification."
- "The preservation checks now address the central risk. My assessment remains: convincing core
  argument, with downstream recovery unproved and the exact premises awaiting verification in the
  reviewed text."

**c.6897455387**, adopted direction (full system versus description; per-run versus
all-branch support; standing). These reached this round first as a relay from the coordinator,
labelled O12–O14, and were then found on the issue; the text below is the comment's.
- **O14 (status)**: "This strengthens the case for the core effective-finiteness lemma, while showing
  that the downstream preservation assessment still needs substantive work. Missing proof
  requirements in seven of eight traced classes is more than a minor correction."
- **O12 (uniform measure)**: "The uniform-measure finding needs a precise distinction: a bijection of
  the full system may preserve its uniform product measure without making the finite observational
  description an autonomous, measure-preserving system. The reviewer's new proof could establish the
  first; transferring that property to the description remains a separate question." And: "The
  reviewer's new measure-preservation proof also needs independent checking before it supports any
  recovery classification."
- **O13 (finite support)**: "Likewise, finite support on each individual run does not by itself
  establish one finite patch covering every possible branch. The revised statement must make clear
  which it proves."
- "The planned r4 and re-pinned audit address the right issues. My assessment remains: the core
  argument looks increasingly convincing; its ability to recover particular A1-dependent results
  remains open."

**c.6897859755**, adopted direction (status of the proofs after the independent check; closure wording; compactness
phrasing). These reached this round first as a relay from the coordinator, labelled O15–O18, and
were then found on the issue; the text below is the comment's.
- **O15 (inheritance and existence)**: "That correction matters. Failure of automatic inheritance
  does not imply that no suitable finite closed model exists. Any wording suggesting the latter
  should be withdrawn."
- **O16 (three tiers)**: "The revised account should distinguish:" then "Checked: the full-system
  measure theorem, intervention lemma, compactness lemma and necessity result, under their stated
  hypotheses." and "Still unchecked: the reviewer's characterization of when a measure-preserving
  closure exists, including its application to second-order rules." and "Still unproved: whether
  such a closure preserves everything required to recover a particular audited result."
- **O17 (credit and disqualification)**: "So the closure result earns no recovery credit yet. Its
  being a chosen, window-valid model does not automatically disqualify it either: it could suffice
  for a theorem whose requirements are entirely confined to that window. That is what the
  proof-requirements check must determine."
- **O18 (the compactness lemma in brief)**: "For compactness, the summary should say "finite reads
  on every run, under the lemma's other hypotheses," so it does not turn a conditional theorem into
  an unrestricted claim."
- Assessment: "My assessment has strengthened: effective finiteness now has substantial checked
  mathematical support. Its physical consequences remain unresolved. The targeted r5 and audit
  re-pin are the appropriate next checkpoint; no additional review scope is needed."
- The same comment records, as adopted direction, a sentence from earlier in the session: "That addresses all
  three overstatements and preserves the key distinction: a recovery candidate is not a recovered
  result."

**c.6897946443**, adopted direction (the latest comment on the issue; conditions organized by claim; scope conceded;
the weakest sufficient proof for each observable claim). Relayed by the coordinator as **O19** and
then found on the issue; the text below is the comment's.
- "We should simplify how the conditions are organized, and concede limits where necessary. We
  should not relax a condition merely to make a recovery succeed." And: "The useful simplification
  is to stop treating every condition as a requirement for every result:"
- The six-row table of that comment, "Claim being made" — "Conditions it needs": "Finite
  description for a fixed observation window" — "The dependency and finite-state hypotheses of the
  checked patch/intervention lemmas"; "Probabilities for that description" — "A suitable starting
  probability law"; "Uniformity, invariance or measurement independence" — "Each property's own
  justification"; "A finite closed model reproducing the window" — "The closure theorem's
  conditions, once independently checked"; "Recovery of a particular A1 result" — "Only the
  properties that result's proof actually uses"; "One finite model valid for all time" — "A
  separate all-horizon argument".
- "What I would concede now is scope: effective finiteness does not, by itself, recover A1's full
  role. Some results may survive only as finite-model mathematics; some may need replacement
  theorems; others may remain conditional. That is an acceptable scientific outcome."
- "What I would simplify is the recovery target. If a result concerns only a finite experiment, ask
  whether we can prove that observable conclusion directly. We need not reconstruct an autonomous
  finite universe, global recurrence or a global invariant measure unless the proof genuinely
  requires them. A new direct proof could avoid conditions needed by the old proof."
- "But two shortcuts would be unjustified:" then "Adopting a new assumption solely because it
  rescues a desired result." and "Calling a conditional recovery an unconditional consequence of
  OI."
- "My recommendation is therefore: keep the checked effective-finiteness lemma, pursue the weakest
  sufficient proof for each observable claim, and explicitly concede everything that remains
  unsupported. That simplifies the programme without lowering its evidential standard. The exact
  conditions we can remove must come from the reviewed proof traces, not from the summaries alone."

**Rules given by the brief, stated in this file's words** (not quotations from a comment): no
finiteness claim is made about the substratum as a whole, under any "effective" label; F-each and
F-one are kept apart; with settings or inputs a comparison holds them the same in both runs, or uses
the same adaptive policy together with the information it uses; interventions must have finite
support; measurement independence is a separate premise; no class has recovery credit.

**"A recovery candidate is not a recovered result."** Source: adopted direction (c.6897859755),
given in the session of 2026-11-15. It is not separately recorded on #1169: no comment was made for it when it was
given, and r4 did not find it in the ten comments it read. c.6897859755 has since recorded it
beside other directions, as a sentence from earlier in that session (quoted above). It is
used here as an adopted rule.

**Quotations in r3 that could not be checked then.** r3 could not check three passages, and r2 had
printed two more. All are now located: the passages on the information that is finite, on the
all-time conclusion and on the recurrence statement are in c.6896496410; the counterexample passage
is in c.6896890693; the instruction to proceed with a question about the hidden sector is in
c.6896070253.

**Goal link (§A.47).** The item served is "priority item 2, A1 dependence of the main equivalence
and of the results built on it" (Goal-link line of c.6894872312 and of c.6896070253). This unit
decides which finiteness forms are theorems, from which inputs and at which layer, and which
A1-consuming result classes each form could carry once that result's proof is checked. It decides no
status and adopts no premise.

**Productivity test (set before r1, kept).** The obvious restatement is: "locality gives a finite
past cone at each horizon, and nothing uniform in the horizon follows." A finding is a gem only if
it is strictly stronger than that restatement and either constrains a result class of the audit, an
owner option or the validity note's findings, or exposes a hidden assumption. Output classes NEW,
POSITIVE, ELABORATING, CONFIRMING, BORDERLINE (§A.31). Stopping rule: about three consecutive passes
with no NEW finding. Decisive branch first: the uniform forms (§2), since only they could answer the
question about one finite model valid at every horizon.

## Status of the pieces

**Organized by claim (O19).** Adopted direction (c.6897946443): "The useful simplification is to stop treating
every condition as a requirement for every result". The table follows the owner's six claims, in
the owner's order. Each claim lists only the conditions it needs, each located on `main` or
flagged; the premise labels F, P, D are those of §4.0. "Checked" means re-derived by an independent
review, as a paper proof; every checked statement is conditional on the conditions in its row.

| # | Claim (statement) | Conditions it needs; on `main` (file:line) or flagged | Status | Where proved in this file |
|---|---|---|---|---|
| 1 | **A finite description for a fixed observation window.** Over `n` steps, equal data on a finite patch, under the same settings or the same policy with its information, give equal observations; the patch data are finitely many | The dependency and finite-state hypotheses of the patch and intervention lemmas. F1 site factorization: Main:724 (viii). F2 one deterministic update: Main:54, Main:44. F3 finite reading sets: Main:724 (xiii) for the selected model; **flagged** off it (Main:362 takes it from the finite site set). F4 a finite visible region with a site-local readout: **flagged**; used at Main:296, Main:744–746, GR:112, not stated separately. F5 finite site alphabets on the patch: Main:724 (xiii); off the selected model Main:362 only, **flagged**. With interventions also: F6 one shared protocol: Main:366–374 for one setting step, **flagged** for adaptive policies; F7 finite supports over every branch (FS-all), or finite reads on every run, under the lemma's other hypotheses: **flagged**; automatic on `main` from the finite site set of Main:362. No probability and no A1 | **Checked**, conditional on the flagged premises: Lemma PM by the review of r2 (kernel core for a single readout time); Lemma PM-I and Lemma K by the reviews of r3 and r4 | N1.3, N1.5; §4.0 claim 1 |
| 2 | **Probabilities for that description.** The law of the `n`-step record is the image of the patch marginal of the starting law (with a policy, of the joint law of patch data and policy information) | A suitable starting probability law. P1 a normalized starting law with the measurability condition of Lemma PM (b): for a finite carrier Main:54, Main:58; for an infinite carrier a hypothesis only (GR:132; Sub:92), **flagged**. P2, with a policy, the joint law: not on `main`, **flagged**. Claim 1's conditions | **Checked**, conditional on P1 (and P2): Lemma PM (b) by the review of r2; Lemma PM-I (c) by the reviews of r3 and r4 | N1.3 (b), N1.4, N1.5 (c); §4.0 claim 2 |
| 3 | **Uniformity, invariance or measurement independence.** Each is a further property of the starting law or of the dynamics, used by particular results and by none of claims 1 and 2 | Each property's own justification. Uniformity (D2): of the kind of posit (iv), Main:724; for a finite carrier Main:54, Main:58, Main:115; **flagged** for an infinite carrier. Invariance (D3): for a finite carrier Main:60, Main:274; for an infinite carrier it is proved here for the full system, given D2, from (xiii) (Main:724) by N3.2, or from a bijection with both locality clauses and finite alphabets at every site by (M-full). Measurement independence (D6): ledger item (xiv), Main:724; hypothesis (iv), Main:372–374 | Uniformity: **unproved**; a premise wherever it is used. Invariance: **checked** for the full system, conditional on its stated hypotheses and on D2 (N3.2 by the review of r2; (M-full) by the review of r4); not inherited automatically by the description. Measurement independence: **unproved**; a posit on `main`, not derived | N3.2, §P.3, N3.6; §4.0 claim 3 |
| 4 | **A finite closed model reproducing the window.** A finite set with a self-map whose record agrees with nature's on `[0, n]` | The closure theorem's conditions, once independently checked. For a self-map of the patch data that reproduces the window: claim 1's conditions for the autonomous case (F1–F5). For that self-map to be a bijection preserving the uniform patch measure: the window law under that measure is shift-stationary (Lemma C), which holds given D2 with D3; or the update has the second-order form (Lemma C′; Main:724 (xiii)). For that measure to be the description's probability: D2. Separately, a constructed finite realization on another carrier exists for every finite-horizon law: Main:516–520, Main:46 | **Checked**, each under its stated hypotheses, by the recheck of r5 (one independent check of paper proofs): Lemma C, its corollary and Lemma C′, which are the review of r4's, re-derived by the writer. No class cites them. The constructed realization is on `main` | §P.4 (b); N2.2; §4.0 claim 4 |
| 5 | **Recovery of a particular A1 result** | Only the properties that result's proof actually uses: listed per class from the proof traces, with their lines on `main` (§4.2) | **Unproved** for every class. No class has recovery credit | §4.2; §3; §4.0 claim 5 |
| 6 | **One finite model valid for all time** | A separate all-horizon argument. None is given for nature. Sufficient conditions: the complete relevant state is finite and its evolution is determined by it (N2.1 form (i)); or finitely many influencing sites with inputs kept external, which gives a model with inputs (form (ii)). Under N2.3's conditions the visible condition is pathwise eventual periodicity with uniform bounds. None of these is on `main` for nature without A1: **flagged** | **Unproved** for nature. The conditional statements about model classes (sufficiency, the necessity result, the periodicity criterion) are **checked** by the reviews of r2, r3 and r4 | N2.1–N2.6, N2.10; Verdict 3; §4.0 claim 6 |

**Detail by piece.** The first column gives the claim of the table above that each piece serves.

| Claim | Piece | Status in r5 |
|---|---|---|
| 1, 2 | Lemma PM (autonomous patch matching, N1.3) | Stands on its reviewed terms (O10): re-derived step by step by the review of r2, and confirmed unchanged in substance by the review of r3. Restated here with the deterministic form first and the law form second; no change of substance. A derived lemma: paper proof with a kernel-checked core for a single readout time |
| 1, 2 | Lemma PM-I (interventions and policies, N1.5) | The all-branch form was re-derived by the review of r3 and stood. Revised in r4: the policy may remember its earlier reads (finding 4); the per-run form and the all-branch form are stated apart (O13); a compactness lemma relating them (Lemma K) is added. All three were **checked sound by the review of r4**, under their stated hypotheses. r5 states which hypothesis gives one finite patch for every branch: FS-all, or finite reads on every run, under the lemma's other hypotheses (Verdict 2; N1.5) |
| 6 | Sufficiency for one finite model (N2.1) | Both forms checked by the review of r3. Necessity in the every-initial-configuration reading (Proposition N): **checked sound by the review of r4**, under its stated hypotheses. Added in r5: necessity under one initial law that gives positive probability to every finite pattern, **[reviewer's refinement; checked by the recheck of r5]**, under its stated hypotheses |
| 5; 3 for measurement independence | Bell-ceiling patch (N3.6) | Checked by the review of r3. Distance graph made exact (finding 7). Dependency coverage only; measurement independence is a separate premise |
| 3 | Measure preservation by the full system, (M-full) (§P.3) | The proof of the review of r3, re-derived step by step in r4 and **checked sound by the review of r4**, under its stated hypotheses (one independent check of a paper proof; not kernel-checked). Per the adopted direction (O12, c.6897455387) it "needs independent checking before it supports any recovery classification"; whether that one check is enough is the owner's decision, and no class cites it as support |
| 4 | The description and measure preservation (§P.4) | **Corrected in r5; awaiting check.** r4's single claim (M-desc) was existential, and its headline "(M-full) does not imply (M-desc)" was false as stated under a uniform product prior. Two things are now kept apart. (a) The finite observational description as defined is a window: it has no autonomous dynamics, and an invariant measure is not defined for it. (b) A closure can be *chosen* on the patch that reproduces the window: Lemma C (under the uniform patch measure, a measure-preserving bijection of the patch data that reproduces the window exists exactly when the window law is shift-stationary) and Lemma C′ (for second-order rules, the selected model included, every fixed-boundary closure is one), both **[reviewer's lemma; re-derived by writer; checked by the recheck of r5]**, each under its stated hypotheses. The property is not inherited automatically by the description; whether a suitable finite closed model exists is a separate question (O15). Such a closure is a chosen model valid on the window only; its existence is not the description being an autonomous measure-preserving system. It earns no recovery credit yet, and being chosen and window-valid does not automatically disqualify it either: it could suffice for a theorem whose requirements are entirely confined to the window (O17) |
| 5 | What each description preserves (§P), the per-class properties (§4.2) | Substantially revised in r4 (O14): every class was redone from a trace of its proof. The review of r4 retraced seventeen classes; it found requirements missing in two rows (readback; one-step coherence) and one consumer class of Main:60 without a row (the §3.4 obstructions for a fixed finite realization). r5 completes the two rows, adds the row, rewrites the measure column in the terms of §P.4 and adds the column "requirements confined to the window?" (O17). **The cells changed or added in r5 are awaiting check** |
| 1–6 | Premises (§4.0) | Organized by the six claims (O19); claims 1–3 are r4's three groups. **Finiteness premises** F1–F7: site factorization, one deterministic update, finite reading sets, a finite visible region, finite alphabets on the patch and, with interventions, a shared protocol and finite supports over all branches; F3 and F5 off the selected model, F4, F6 for adaptive policies and F7 are flagged as not established on `main`. **Probability premise** P1 (P2 with a policy): a normalized starting law; not needed for finiteness. **Further distributional properties** D1–D8 (product form across the patch boundary, uniformity, invariance, independence of visible and hidden data, stationarity, measurement independence, independence of policy information, a selected prior): none is used by the lemma; each needs its own justification where a result uses it |
| 1 | Fixed-horizon finiteness | A **derived lemma**, conditional on its premises being on `main` (§4.0 says which are). **Candidate replacement** names only its possible role in a given proof that currently uses A1. No recovery credit for any theorem until that theorem's requirements are checked |
| all | Everything else | As in r4 (r3 with the wording, labelling and scope repairs of the review of r3) |

Nothing is recovered or adopted.

**Proof status in three tiers (O16).** Adopted direction (c.6897859755), three items of one list: "Checked: the
full-system measure theorem, intervention lemma, compactness lemma and necessity result, under
their stated hypotheses."; "Still unchecked: the reviewer's characterization of when a
measure-preserving closure exists, including its application to second-order rules."; "Still
unproved: whether such a closure preserves everything required to recover a particular audited
result." In the table, "checked" means: re-derived step by step by the independent review of r4 or,
where the row says so, by the independent recheck of r5 (`RECHECK-EF-1-r5.md`), with no gap found.
That is one independent check of a paper proof; none of the checked items is kernel-checked.

| Tier | Item | Where | Hypotheses, or what is missing |
|---|---|---|---|
| **CHECKED** | The full-system measure theorem, (M-full), under its stated hypotheses | §P.3 | A bijection of the full system; finite reading sets; each site read by finitely many sites; finite alphabets at every site. Then it preserves the uniform product measure. The owner's condition on its use stands, and no class cites it |
| **CHECKED** | The intervention lemma, Lemma PM-I, under its stated hypotheses | N1.5 | All-branch form with policy memory, (a), (b), (c): one protocol shared by the runs compared, with declared supports; FS-all for finiteness. Per-run form (a′): run-wise finite reads on the given run |
| **CHECKED** | The compactness lemma, Lemma K, under its stated hypotheses | N1.5 (f) | One finite patch for every branch from finite reads on every run, under the lemma's other hypotheses: a finite alphabet at every site and finitely many values of the policy information |
| **CHECKED** | The necessity result, Proposition N, under its stated hypotheses | N2.1 | The autonomous substratum setting with finite reading sets, a finite visible region and no controller; the form "from every initial configuration"; finite alphabets on the influence set for the step from a finite influence set to finitely many records |
| **CHECKED** (by the recheck of r5) | The reviewer's characterization of when a measure-preserving closure exists, including its application to second-order rules, under its stated hypotheses | §P.4 | Lemma C with its corollary (the characterization), under the uniform patch measure, and Lemma C′ (second-order rules). They are the review of r4's, re-derived step by step by the writer and then, independently, by the recheck of r5 (its sections 1.2–1.4), which found them sound. No class cites them, and they give no recovery credit |
| **CHECKED** (by the recheck of r5) | The reviewer's refinement of the necessity result for one initial law that gives positive probability to every finite pattern, under its stated hypotheses | N2.1 | The hypotheses stated in N2.1 for the refinement. Re-derived by the writer and then, independently, by the recheck of r5 (its section 1.5), which found it sound |
| **STILL UNCHECKED** (listed by this file) | r5's restatement of §P.4; the cells of §4.2 changed or added in r5 | §P.4; §4.2 | Written by the writer; not independently checked |
| **STILL UNPROVED** | Whether such a closure preserves everything required to recover a particular audited result | §4.2 | Not proved for any class. The column "requirements confined to the window?" of §4.2 sorts the classes from their proof traces; that is a classification, not a proof (O17) |

Lemma C, Corollary C1, Lemma C′ and the one-law refinement were re-derived by the recheck of r5 and
found sound (one independent check; paper proofs; not kernel-checked). On that check r6 lists them
as checked, each under its stated hypotheses. The tier "still unproved", every class and every row
of §4.2 are unchanged by it, and no class gains recovery credit.

Re-derived by the review of r2 or of r3, as in r4: Lemma PM (N1.3); the all-branch intervention
form without memory; N2.1 forms (i) and (ii); N2.3–N2.6; N2.10; N3.2; B1–B3.

## Verdict

1. **F-each, autonomous case: a derived lemma, without A1 [IR, proof here; core for a single readout
   time kernel-checked].**
   - *Deterministic form (no probability).* Under the finiteness premises F1–F4 of §4.0 (site
     factorization, one deterministic update, finite reading sets, a finite visible region with a
     site-local readout), two initial configurations that agree on the finite patch `U_n` (the
     observer's sites and the hidden sites from which a chain of at most `n` reading steps reaches
     them) have the same observation history on `[0, n]`. With F5 (finite alphabets on the patch)
     there are finitely many patch data: this is the finite observational description.
   - *Law form.* Add premise P1, a normalized starting law. Then the law of the history is the
     pushforward of that law's marginal on `U_n`. P1 supplies probabilities on the description; it
     is not a premise of finiteness.
   - No further distributional property is used (§4.0, group C). What is finite is the information
     needed to determine the observations over those `n` steps; no bound on the number of sites is
     used or obtained.
2. **F-each with settings, inputs or policies [IR, proof here].** Deterministic form first: two runs
   under the same settings, or the same adaptive policy with the information it uses, whose initial
   data agree on the patch `E_n`, have the same observation history. The patch covers the full
   experiment: at every step it contains the observer's sites, the sites the policy reads and the
   sites the permitted interventions read or act on. Two forms are kept apart (O13):
   - **per-run**: for one realized run whose reads and actions are finite, a finite patch
     determines the record of that run and of every run that agrees with it on that patch;
   - **all-branch**: one finite patch serves every branch of the policy over `n` steps. It is
     proved here under either of two hypotheses:
     - *FS-all*: at each step, the union over every branch of the sites that can be read or acted
       on is finite. This gives the patch `E_n` with an explicit bound (N1.5 (b)).
     - *Lemma K*: finite reads on every run, under the lemma's other hypotheses. In full: finite
       reads at every step of **every** run (every initial configuration and every value of the
       policy information), a finite alphabet at **every** site, and finitely many values of the
       policy information. This gives one finite patch by compactness, with no bound on its size
       (N1.5 (f)).

     Finite reads on only the runs considered do not give it: not when some run is excepted, even
     a set of runs of probability zero (E1); and not when every run has finite reads but the policy
     information has unboundedly many values (E2) or some alphabet is infinite (E3). A bound on the
     size of each run's support does not give it either (E2).

   Adopted direction (c.6897455387): "finite support on each individual run does not by itself establish one
   finite patch covering every possible branch. The revised statement must make clear which it
   proves." The proofs of N1.5 establish the per-run form under run-wise finite reads on the given
   run, and the all-branch form under FS-all or under Lemma K's three hypotheses together. A law
   over outcomes, or a comparison across settings, needs the all-branch form. Neither FS-all nor
   Lemma K's hypotheses are separately stated premises on `main`.
3. **F-one is not established here.** The fixed-horizon argument does not, by itself, supply one
   finite model valid for every horizon. That is narrower than proving such a model impossible. Two
   sufficient conditions are proved (N2.1), neither known to hold for nature: (i) *autonomous form*:
   if the complete relevant state is finite, including any controller or policy memory, and its
   evolution is determined by that state, there is one autonomous finite model; finitely many
   influencing sites give this when no external controller exists; (ii) *model with inputs*: if
   inputs remain external and finitely many sites influence the observations under every input
   sequence, there is one finite model with inputs (a finite transducer), not an autonomous one. An
   unbounded external controller is not made finite by acting on finitely many sites.
   *Necessity* [Proposition N; checked by the review of r4]: in the autonomous substratum setting
   with finite alphabets, a finite influence set is also necessary for one finite autonomous model
   that reproduces the record from *every* initial configuration. Under one fixed initial law the
   answer depends on the law. It is not necessary for an arbitrary law (X3, a point mass, which
   gives probability zero to some finite patterns). It is necessary for a law that gives positive
   probability to every finite pattern, the uniform product prior included **[reviewer's
   refinement; checked by the recheck of r5]**. All of these are statements about model classes, not
   about nature.
4. **Operational conditions for periodicity [IR, proof here].** For an autonomous, deterministic,
   finite system without continuing inputs or settings, every observation record is eventually
   periodic, a transient allowed, with uniform bounds; exactly periodic for a bijective
   representative. A family of such systems of bounded size faithful at every horizon exists exactly
   when the visible law is pathwise eventually periodic with uniform bounds (N2.3–N2.5). With
   continuing inputs or settings, or with stochastic dynamics, a finite system can give nonperiodic
   output; form (ii) of item 3 carries no periodicity. Every finite-horizon law is the restriction of
   an exactly periodic law (N2.6), so no finite-horizon datum decides the all-time condition.
5. **Recurrence (kept).** A finite description for a chosen horizon supplies no recurrence guarantee
   within that horizon (N3.1).
6. **What the description preserves (O11, O12, O15, O17) [IR; §P; revised in r4, corrected in r5].**
   The fixed-horizon description keeps determinism, the causal cone and the observation law on the
   window with everything computed from it. It does not automatically inherit bijectivity or
   reversibility (it has no self-map of its own), an invariant measure or a selection principle
   among invariant measures, recurrence structure, absolute hidden cardinalities, conserved energy
   shells, spectral statements or measurement independence. On measure preservation, three
   statements are kept apart:
   - **(M-full)** [checked by the review of r4, under its stated hypotheses]: with finitely many
     values at every site, a bijection of the full system in which each site reads finitely many
     sites and is read by finitely many preserves the uniform product measure. Without the second
     locality clause the conclusion is not guaranteed: example B1 is a bijection with finite
     reading sets in which some site is read by infinitely many sites, and it does not preserve the
     measure.
   - **The description as defined (M-desc-own).** It is a window: a finite set of patch data with a
     map to records on `[0, n]`. It has no autonomous dynamics, and an invariant measure is not
     defined for it (§P.4 (a)). So the property is not inherited automatically by the description.
   - **A chosen closure on the patch (M-desc-some).** Whether a suitable finite closed model exists
     is a separate question. On the patch data themselves, under the uniform patch measure, a
     measure-preserving bijection that reproduces the window exists exactly when the window law is
     shift-stationary (Lemma C), hence whenever the uniform product measure is invariant for the
     full system; for second-order rules, the selected model included, every fixed-boundary closure
     is one (Lemma C′). Both lemmas are **[reviewer's lemma; re-derived by writer; checked by
     the recheck of r5]**.

   The distinction of the adopted direction (c.6897455387) is the form of the conclusion: "a bijection of the full
   system may preserve its uniform product measure without making the finite observational
   description an autonomous, measure-preserving system. The reviewer's new proof could establish
   the first; transferring that property to the description remains a separate question." A
   chosen closure is a model valid on the window only: its order, cycles, eventual image and
   spectrum are its own. Its existence is not the description being an autonomous
   measure-preserving system. Adopted direction (O17, c.6897859755): "So the closure result earns no recovery credit yet.
   Its being a chosen, window-valid model does not automatically disqualify it either: it could
   suffice for a theorem whose requirements are entirely confined to that window. That is what
   the proof-requirements check must determine." §4.2 records, class by class, whether the traced
   requirements are confined to the window. Whether a closure preserves everything a particular
   audited result requires is still unproved for every class.
7. **Recovery status.** Nothing is recovered or adopted. Fixed-horizon finiteness is a derived
   lemma, conditional on its premises being on `main`; §4.0 gives, in three groups, the finiteness
   premises, the probability premise and the further distributional properties, each with its place
   on `main` or a flag. It is a candidate replacement only for A1's role in a given proof, and has
   no recovery credit for any theorem until that theorem's actual requirements are checked. §4.2
   lists, for each result class, the properties its proof uses with their lines on `main`. A result
   that needs F-one is not recovered by F-each. A recovery candidate is not a recovered result.
8. **Bell ceiling (N3.6).** The patch that contains the wings' backward sets, the setting regions
   `A ∪ B` and, where the settings are generated inside the substratum, the setting-generation
   regions gives dependency coverage, in the all-branch form. It does not give measurement
   independence, which stays a separate premise: ledger item (xiv) on `main`, a posit, not derived.
9. **A candidate bearing on Main:638's open question (a) [IR, both directions proved here; candidate
   only].** Without inputs, a family of root-conditioned multi-time laws has an all-time realization
   (finite carriers, one bijection, one shared hidden prior) exactly when it is pathwise periodic
   with a uniform period (N2.5, N2.9). This proves *existence* of a realization. It does not prove
   that given per-horizon realizations *join*, and it does not cover action-labelled experiments.
10. **The finite-hidden-memory draft (H-mem)**, a uniform bound on the Hankel rank of the visible
    process, is compatible with exact qubit behaviour, carries none of the A1-consuming whole-carrier
    results, and with a free dimension bound is not hard to vary under §A.29 (§5). Not proposed for
    adoption.
11. **Standing of the downstream assessment (O14, O16).** The core argument (items 1 and 2) has
    been re-derived by independent reviews: Lemma PM by the review of r2, the all-branch
    intervention form by the review of r3, and the memory clause, the per-run form and Lemma K by
    the review of r4. The assessment of what it could recover (§P, §4.2) was substantially revised
    in r4, after the review of r3 found proof requirements missing in seven of the eight classes it
    traced. The review of r4 retraced seventeen classes; it found requirements missing in two rows,
    one consumer class without a row, and the statement about measure preservation on the
    description wrong as written. r5 repairs these, and the repaired parts are awaiting check. In
    the owner's tiers: checked, the four proofs of the table "Proof status", each under its stated
    hypotheses, and, by the recheck of r5, the reviewer's characterization of when a
    measure-preserving closure exists and the one-law refinement, each under its stated
    hypotheses; still unproved, whether such a closure preserves everything required to recover a
    particular audited result.
    The ability of the argument to recover any particular A1-dependent result remains open.

The four claims of the owner's assessment are answered one by one in §10.

## Scope conceded (O19)

Adopted direction (c.6897946443): "What I would concede now is scope: effective finiteness does not, by itself,
recover A1's full role. Some results may survive only as finite-model mathematics; some may need
replacement theorems; others may remain conditional. That is an acceptable scientific outcome."

What this file concedes, on the evidence of its own proof traces [IR]:

- The fixed-horizon lemma (claims 1 and 2 of the status table) recovers no A1-dependent result by
  itself. No class of §4.2 has recovery credit.
- Results whose traced requirements lie outside every observation window are not carried by the
  fixed-horizon form: the return at the recurrence time and what rests on it, the eventual-image
  and surjectivity steps, the selection among invariant measures, all-time periodicity,
  energy-shell counting, the Koopman statements of §4.6, and the obstructions for one fixed finite
  realization. On present evidence they stand as mathematics about finite models, with no claim
  here that nature is one.
- Results whose content is an observable conclusion about a finite experiment may need replacement
  theorems, proved directly for that conclusion. §4.2 names a direct-proof target for each such
  class and proves none.
- Results that rest on a premise not established on `main` without A1 remain conditional on it and
  are labelled so: the flagged finiteness premises (F3–F7), uniformity of the starting law,
  measurement independence.
- One finite model valid for all time (claim 6) is not established.

Which of the owner's three outcomes each class receives is for the audit and the owner. This file
decides no status.

**Two barred shortcuts (O19).** Adopted direction (c.6897946443): "But two shortcuts would be unjustified:"
"Adopting a new assumption solely because it rescues a desired result." and "Calling a conditional
recovery an unconditional consequence of OI." This file was checked against both.

- *The first.* No assumption is adopted here. The hypotheses under which more would follow are
  named and left unadopted: a uniform product starting law (D2), finite supports over every branch
  (FS-all), a finite complete relevant state (N2.1), the finite-hidden-memory draft (§5, not
  proposed for adoption). A chosen closure (§P.4) is a model, not a premise. Adopted direction (same comment):
  "We should not relax a condition merely to make a recovery succeed." No condition of any traced
  proof is dropped in §4.2; the direct-proof targets say what a direct proof would need and do not
  assert that any condition of an existing proof can be removed. Adopted direction (same comment): "The exact conditions we
  can remove must come from the reviewed proof traces, not from the summaries alone."
- *The second.* No recovery is claimed, conditional or unconditional. Each conditional statement
  carries its condition where it is stated: claims 1 and 2 are conditional on the flagged
  premises; (M-full), the intervention lemma, Lemma K and Proposition N hold under their stated
  hypotheses; invariance and double stochasticity on an infinite carrier are conditional on a
  uniform product starting law; N2.1's two forms and the periodicity criterion are conditional on
  hypotheses that nothing here supports for nature; the closure lemmas are conditional on their
  hypotheses, under which the recheck of r5 checked them. None of these is a consequence of OI without its conditions.

## Response table

Findings 1–13 of the review of r3, the owner items OP and O12–O14, and three points added by r4.
"Check" says how each was verified. This table and the class-by-class table after it are r4's
record of its response to the review of r3, kept as written except for row R4-c: "here" and "this
round" in them mean r4, their status marks are r4's, and "marked as needing (M-desc)" is r4's mark,
which r5 replaces (§P.4, §4.2). The current status of each proof is in the table "Proof status"
above, and what r5 changes is in the table "r5 changes" below.

| Item | Point | Check and disposition | Where |
|---|---|---|---|
| 1; OP | Separate what finiteness needs from what probabilities need; "derived lemma"; "candidate replacement" | Accepted. §4.0 is now three groups: finiteness premises F1–F7, probability premises P1–P2, further distributional properties D1–D8, each with its place on `main` or a flag and with where it is used. The split is carried into the verdict, the status table, §4.1, §10 and the summary. "Candidate replacement premise" is gone outside the owner's quotation; the wording is "derived lemma (conditional on its premises being on `main`); candidate replacement for A1's role in a given proof". "Nothing is available without them" is deleted. Lemma PM and Lemma PM-I state the deterministic form first and the law form second | §4.0, N1.3, N1.5, Verdict 1, 2, 7 |
| 2 | B1 lies outside the locality class of `main`; inside it invariance holds | Accepted. Checked: in B1 every output `i ≥ 2` reads site 0, so site 0 is read by infinitely many sites; (xiii) requires "each site read by finitely many $F_i$" (Main:724), and the kernel's class carries the same clause (`FiniteRange.infl`, `QuasilocalAlgebra.lean:919–921`; `ReversibleDynamics`, :956–959). The review's proposition was re-derived step by step and is stated as (M-full), **[unreviewed proof]**. The qualifier is applied at every site the review lists (twelve entries when the two P.2 rows are counted apart, eleven when counted as one): Verdict 6; §P.2 rows "Invariance" and "Double stochasticity"; B1's heading and body; N3.2; N3.11 candidate 3; §4.2 "Bijectivity" row; EF-G16; AW-EF11; question 6 (question 9 now asks for the independent check and no longer lists the example). N1.2's sentence on the read-by clause is corrected. EF-G5 and candidate 3 are extended to the class, marked unreviewed | §P.3, N1.2, N3.2, N3.11 |
| 3 | Form (i)'s hypothesis is close to its conclusion; necessity holds for every initial configuration | Accepted, with one condition added. Re-derived: finitely many records give a finite influence set with no alphabet condition; the converse needs finite alphabets on the influence set (a site with an infinite alphabet can influence through finitely many classes). Stated in N2.1 with the two readings; N2.8's row is split; Verdict 3 and §10 say which reading is necessary. **[unreviewed proof]** | N2.1, N2.8 |
| 4 | PM-I does not cover a policy that remembers earlier reads | Accepted. The rule is now `u_t = π_t(X_{0:t}, (s_τ\|_{R_τ})_{τ≤t}, ξ)`, the induction hypothesis is cumulative, and the argument set in the finiteness step is `(C_V)^{t+1} × ∏_{τ≤t} C_{R_τ}`. Patch and bound are unchanged; re-derived | N1.5 |
| 5; O13 | Finite support per run versus over all branches | Accepted, with a correction to the example. PM-I is stated in a per-run form and an all-branch form, with the exact hypothesis of each (run-wise finite reads; FS-all). The review's least-`j` example does not have finite reads on every run: on a configuration with no 1 beyond site 0 it reads every site. That matters: with finite alphabets at every site and finitely many values of the policy information, finite reads at *every* configuration do give one finite patch, by compactness (Lemma K, **[unreviewed proof]**). The examples used here are therefore of the two kinds that remain: finite reads on almost every run but not all (the least-`j` example), and unboundedly many branches (a policy that reads a site named by an unbounded seed, or by an observed value in an infinite alphabet). The summary's sentence is changed as asked | N1.5 |
| 6 | Form (ii): the hypothesis is not FS; the input set may be infinite | Accepted. The hypothesis now reads: each permitted intervention has a finite support; the union over the menu may be infinite; finiteness comes from the hypothesis on `J^in_∞`. Added: the machine has finitely many states and at most `\|B\|^{\|B\|}` distinct transition maps, so the inputs act through a finite alphabet | N2.1 |
| 7 | Which graph measures the Bell distance | Accepted. N3.6 takes `N(i)` to be the actual one-step dependency sets; given declared finite reading sets these are reading sets too (one-at-a-time argument), so `U_{k_A}(R_A) ⊆ B_{G_φ}(R_A, k_A)` and `W_A` does not meet `B` | N3.6 |
| 8 | §P has no entry for the all-horizon model | Accepted. Object (δ) added with its own list, re-derived. The row "Recurrence-scale P-indivisibility" of §4.2 is split into the counting form (Main:113–129) and the shared-prior form (Main:131–143) | §P.1, §P.5, §4.2 |
| 9; O14 | "Properties the proof uses" missed entries | Accepted as substantive. Every class was redone from a trace of its proof on `main`, not only the eight the review sampled. Each of the review's additions was confirmed at the line it gives. What changed per class is in the table that follows this one | §4.2 |
| 10 | Standing of the finite-visible-region premise | Accepted: "used on `main` for the spatial results (Main:296; Main:744–746; GR:112); not stated as a separate premise, and finite there only through the finite site set" | §4.0 |
| 11 | Summary and questions | Accepted: "kernel-checked for a single readout time"; premise groups; "the set of all sites they could read or act on at each step must be finite"; "whose evolution it alone determines"; A1 glossed in questions 6 and 8; qualifier in 9; rooted reading dropped from 7; the sentence on review status cut | §10, §11 |
| 12 | Quotations | Accepted. Every quotation is now copied from the comment, with its id. Two corrections follow from reading the comments: the sentence that a recovery candidate is not a recovered result is a rule of the brief and was not found in the comments, so it is no longer printed as a quotation; and OP's passages are added verbatim | Header |
| 13a | N2.10 (2): `V = {v_0}` not needed for the i.i.d. statement | Accepted; re-derived: the earlier current values at `v_0` do not involve `x_{v_0+ke}(0)` whatever `V` is | N2.10 |
| 13b | §5.2: which process has rank 1 | Accepted. The current-value process has rank 1; the observation at one site is the pair (previous, current), a Markov chain of rank `q`. Consequence recorded as marker AW-EF13 | §5.2, §7 |
| 13c | "on an infinite lattice of that class" | Accepted | §4.1, §10 |
| 13d | "a declared support" | Accepted | N1.5 |
| 13e | Name the scope of the kernel search | Accepted: the four modules searched are named, and `ImplementationLocality.lean` (namespace `InterventionLocality`, :95) is noted as concerning operational implementation classes on finite carriers | N1.5 |
| 13f | Main:216's first-order clause unchecked | Checked at Main:340. The estimate is a short-time statement (`t` of order `τ_S ≪ τ_B`) whose written derivation uses the §3.2 setup, a chosen interpolation, the slow-bath condition and a bounded coupling. Nothing in it is uniform in the horizon. Whether it holds with a horizon-dependent patch in place of the finite hidden space is not derived, so the row's form is "undetermined" | N3.5, §4.2 |
| O12 | (M-full) and (M-desc) are separate claims | Applied. Both are stated; (M-full) is the re-derived proposition; (M-desc) is assessed with a proof for each of three candidate closures and a counterexample; classes that need a measure on the description are marked as not served by (M-full) alone; the owner's sentence on independent checking is carried, and no class cites (M-full) as support. (r5: r4's two statements about (M-desc) are withdrawn and the matter is restated in §P.4; see "r5 changes", item 1 and O15) | §P.3, §P.4, §4.2 |
| O13 | Per-run versus all-branch | Applied; see row 5. Each result class is assigned the form it needs | N1.5, §4.2 |
| O14 | Status | Applied: the rework is treated as substantive, the per-class changes are listed, and the summary says that the downstream preservation assessment was substantially revised and is unreviewed | below, §10 |
| R4-a | (this round) Compactness relates the two PM-I forms | Lemma K: finite reads at every configuration, finite alphabets at every site and finitely many values of the policy information give one finite patch, with no bound on its size. **[unreviewed proof]** | N1.5 |
| R4-b | (this round) The kernel's locality class has both clauses | `FiniteRange` carries `nbhd` (sites read) and `infl` (sites influenced) with `mem_infl`; `ReversibleDynamics` asks both of the map and of its inverse; `agreeOffG_map` (`QuasilocalAlgebra.lean:943`) is the forward-locality step that the proof of (M-full) uses. No kernel statement of (M-full) was found by a name search of `QuasilocalAlgebra`, `RegionTower`, `SecondOrderDrive` and `SecondOrderLayer`; `uniform_invariant` (`RegionTower.lean:523`) is a finite-stage matrix statement | §P.3 |
| R4-c | (this round) A fixed-boundary closure reproduces the record; whether it preserves the uniform patch measure depends on the rule | For any boundary datum `b`, the self-map `f_b(d) = φ(d ⊔ b)\|_{U_n}` of the patch reproduces the record on `[0, n]` (checked by the review of r4). For the shift this particular closure is not injective, and another closure, the rotation, is a measure-preserving bijection; for second-order rules `f_b` itself is a measure-preserving bijection (Lemma C′, checked by the recheck of r5) | §P.4 |

**What changed in §4.2, class by class (O14).** "Review" marks an entry the review of r3 supplied;
"trace" marks one added by this round's trace.

| Class | Added to "properties the proof uses" | Other change |
|---|---|---|
| Finite-horizon equivalence and dilations | trace: rational kernels or the response-table form (Main:516, :518); the extension of an injective partial map of a finite set to a permutation (Main:520); independence of the hidden prior from the visible initial state "not formalized" (Main:520) | none |
| Hidden-memory theorem, capacity floor, quotient | trace: split from the row above; the realization is a bijection with a joint initial law (Main:602); `H(H_t) ≤ log₂\|C_H\|` (Main:610); the non-bijective case "proved on paper" (Main:614) | new row |
| Causal cone | review: the symmetrization (Main:362). trace: the intervention clause needs a support valid in every state | PM-I form stated |
| Bell ceiling | review: "the protocol records a $\pm1$ outcome in every run" (Main:374–375); `Ω` "fixes each wing's response to every setting" (Main:364–365). trace: the pointwise bound over sixteen response tables, then the average (Main:388–389) | all-branch form required |
| Baseline `T_ij` | trace: the uniform prior on the product carrier of a bijection, as distinct from the counting probability on an eventual image (Main:58, :60, :266); the preimage count behind double stochasticity (Main:60, :274) | (M-full) named and barred as support |
| Lemma 3 selection | trace: uniqueness on the orbit of the actual microstate (Main:60) | marked as needing (M-desc) |
| Bijectivity | trace: the two prongs and their inputs (Main:60); "On a finite set, injectivity implies surjectivity" (Main:60); the measure on the eventual image is not the uniform one (Main:60) | marked as needing (M-desc) |
| Recurrence-scale P-indivisibility, counting form | review: the uniform hidden prior that defines `T` (Main:115, :129). trace: the total-variation contraction direction only (Main:119) | split from the next row; marked as needing (M-desc) |
| Readback with finite recurrence; overlap and return | review: root and hidden state drawn independently (Main:135); the stochastic-inverse lemma (Main:131–133); rows of zero-probability roots kept (Main:137). trace: the overlap-and-return theorem needs only `Γ_n = I` and an overlap, for any shared prior (Main:141–143) | new row; form differs from the counting form |
| CP-indivisibility | review: the diagonal-preservation lemma and its channel family (Main:326–328). trace: stochasticity of `M` from positivity and trace preservation (Main:332) | marked as needing (M-desc) |
| §3.2 setup | trace: the reverse-direction lemma's use of "a uniform-prior bijection marginal preserves the uniform distribution" and Birkhoff–von Neumann (Main:274–276) | marked as needing (M-desc) |
| One-step coherence results | review: "initially uncorrelated and maximally mixed" (Main:316); no dependence on `\|H\|` (Main:322). trace: the boundary factorization, invertibility of the visible block, linearity over `F_2` (Main:298–310) | new row |
| §3.4 all-time periodicity | none | (δ) noted |
| Corner occupancy | review: the estimate of Main:340 with its interpolation (Main:272), slow-bath condition, bath motion at rate `1/τ_B`, bounded coupling. trace: the weak-coupling condition `‖V_int‖ τ_S ≪ 1` (Main:340) | form changed from F-one to undetermined |
| Deep-sector gauge | trace: GR:112 (a)'s proof uses the cone and the uniform prior only (GR:124); (b) uses injectivity and H-BD (GR:126) | none |
| Energy shells | review: negligible boundary interaction at the shell scale; H-count (GR:58). trace: time-reversal-even coarse states (GR:68) | marked as needing (M-desc) |
| Substratum Theorem 23 | trace: Stage 1 uses the constructed realization and the recurrence-cycle statement on a fixed finite representative (Sub:137); Stage 2 (a) takes "a finite periodic lattice" from A4 (Sub:98, :157); Stage 2 (f) uses transition counts (Sub:167); Stage 3 is the gap equation (Sub:181) | form changed from undetermined to mixed, partly untraced |
| §4.6 | review: bounded coupling-graph diameter (Main:746, :758); the compression `P_Σ U_φ P_Σ` (Main:744); the rate condition (Main:756). trace: the fast-bath erasure lemma under uniform erosion (Main:754); the exact compressions need not equal `𝒦_Σ^n` (Main:758) | none |

## r5 changes

Findings 1–11 of the review of r4, two points of the brief, and the owner items O15–O19. "Check"
says how each was verified first-hand before it was applied. Nothing outside this table is changed
from r4, apart from the status marks and cross-references that these changes require.

| Item | Point | Check | Change | Where |
|---|---|---|---|---|
| 1 | r4's (M-desc) is existential; "(M-full) does not imply (M-desc)" and "fails for the closures the description determines" are wrong as written | Lemma C re-derived in both directions, step by step; its corollary and Lemma C′, with the inverse map, re-derived; confirmed that the rotation satisfies r4's definition for the shift and that B1's window law is not stationary. The clause on off-diagonal action checked with a two-site example | Accepted. Both statements withdrawn. §P.4 rewritten: (a) the description as defined, a window with no autonomous dynamics, for which an invariant measure is not defined; (b) a chosen closure, with Lemma C, Corollary C1 and Lemma C′, each marked [reviewer's lemma; re-derived by writer; not independently checked]; the conclusion in the owner's form. The same correction at the status table, Verdict 6, §P.1–P.3, P.6, N3.3, N3.4, N3.7, N3.10, §4.0 (D8), EF-G16, EF-G17, AW-EF15, §10, the summary and question 9 (b). In §4.2 the mark "needs (M-desc)" is replaced, cell by cell, by the requirement itself | §P.4 and the places named |
| 2 | Verdict 2, the summary, one table cell and question 9 (c) contradict Lemma K | The four sentences compared with part (f) and its proof; E1–E3 re-read | Accepted. Stated in each place: one finite patch for every branch is proved under FS-all, or from finite reads on every run, under the lemma's other hypotheses; finite reads on only the runs considered do not give it. "it fails if" becomes "can fail if"; "and not otherwise" is removed. Lemma K's hypotheses are added under F7, with the statement that no class uses that route. The owner's sentence (O13) is quoted where the statement is made | Verdict 2; N1.5; §4.0; §4.1; EF-G18; §10; summary; question 9 |
| 3 | "Not necessary for one fixed initial law" is exact only for laws that miss some finite pattern | The refinement re-derived (continuity of the record map; a finite set of records is closed; an open set of probability zero is empty); found to need no compactness and no alphabet condition | Accepted. Refinement added, marked [reviewer's refinement; not independently checked]; "arbitrary law (X3, a point mass)" at each site; two rows added to N2.8, one per direction | Verdict 3; N2.1; N2.8; §4.1; EF-G19; §10 |
| 4 | The §3.4 obstructions for a fixed finite realization, a consumer class of Main:60, have no row | Main:60, :480–486, :556–562 read; the two propositions traced | Accepted. Row added to §4.2 and to its second table; bullet added to N3.10; the row for the A1-test candidates points to it | §4.2; N3.10 |
| 5 | The readback row and the one-step coherence row miss proof requirements | Main:135, :137; Main:280–282, :310, :324 read | Accepted. Both rows completed with the quoted requirements | §4.2 |
| 6 | (a) F5 unflagged; (b) (M-full) stated without "finite alphabets at every site"; (c) D3 | Main:362, Main:46, Main:724 read | Accepted. F5 flagged off the selected model and added to the sentence on premises not established without A1; the hypothesis added in Verdict 6, question 9 (a) and D3 | §4.0; Verdict 6; §11 |
| 7 | Corner occupancy: the form cell | N3.5 and N1.8 re-read | Accepted: "mixed: the cardinality clause is not a fixed-horizon statement in the native class; the estimate: undetermined" | §4.2 |
| 8 | "The locality class of `main`" | Main:724 (xiii), GR:132, `QuasilocalAlgebra.lean:916–959` read | Accepted. One paragraph in §P.3: the clauses are stated for `F`; N3.2 already covers (xiii); what (M-full) adds is the general class, which `main` does not select as nature's dynamics | §P.3 |
| 9 | Summary: three inexact points | — | The summary is rewritten (see O16, O18) | §10 |
| 10 | (a) E3's last sentence; (b) "the same sentence"; (c) AW-EF15 | (a) the review's example re-derived; (b) c.6896070253 re-read: the question is a second sentence of the comment | Accepted, all three | N1.5; header; §7 |
| 11 | Standing of the proofs | The review's table read against each proof | Proof status recorded; "[unreviewed proof]" replaced by "[checked by the review of r4]" on (M-full), Lemma PM-I's memory clause, (a′), Lemma K and Proposition N | Status section; throughout |
| Brief, 6 | Source of "a recovery candidate is not a recovered result" | The comments on #1169 re-read | Source stated: the owner (`amaybaum`), in the session of 2026-11-15; not separately recorded on #1169 when given; since recorded in c.6897859755 | Header; §12 |
| Brief, 1 | The owner's distinction, exactly | Compared with c.6897455387 | Quoted in full at Verdict 6, §P and §P.4; the conclusion follows its form | Verdict 6; §P.4 |
| O15 | Failure of automatic inheritance is not non-existence of a suitable finite closed model | The whole text searched for "does not transfer", "fails", "cannot hold", "not available" and kindred wording about the description or its closures | Each such statement restated: the property is not inherited automatically by the description; whether a suitable finite closed model exists is a separate question (Lemma C, unchecked). Wording that suggested no such model exists is withdrawn. Where a particular closure is not a bijection (the shift's fixed-boundary closure) or no bijective closure exists on the patch data (B1), the text says that this is not a statement about every closure or every carrier | §P; Verdict 6; N3.3; §4.0 (D8); §4.2; §10; summary |
| O16 | Three tiers | — | The proof-status section, §9 and the summary are in the tiers CHECKED, STILL UNCHECKED, STILL UNPROVED, with the owner's contents; each checked item carries "under its stated hypotheses" | Status section; §9; §10 |
| O17 | No recovery credit yet, and not automatically disqualified; window confinement per class | Each class's proof trace re-read for where its requirements lie | Both halves stated. §4.2 has a second table with the column "requirements confined to the window?" (yes, no, mixed or undetermined, with the reason) and the marks "closure could suffice; to be determined; no credit yet" and "closure cannot supply it" | Verdict 6; §P.4; §4.2 |
| O18 | The compactness lemma in brief | — | "finite reads on every run, under the lemma's other hypotheses" is used in the summary and wherever Lemma K's conclusion is stated in brief | Summary; status section; Verdict 2; N1.5; §4.0; §4.1; EF-G18; §10; question 9 |
| O19 | Conditions organized by claim; scope conceded; direct-proof targets; two barred shortcuts | Each condition located on `main` or flagged; each target read from the proof trace of its class, none from a summary | A claim-to-conditions table, in the owner's order, heads the status section; §4.0 is organized by the six claims, with new entries for claims 4–6; the section "Scope conceded" is added, with the two barred shortcuts quoted and the file checked against both; §4.2's second table gives a direct-proof target per class, each marked [IR; no proof given; not a recovery]. No condition of any traced proof is dropped | Status section; "Scope conceded"; §4.0; §4.2 |

## 1. Finite observational description at a fixed horizon (task a)

### N1.1 Setting and the two sets

Let `ι` be a set of sites of any cardinality, `Q_i` a nonempty alphabet at each site,
`C = ∏_{i∈ι} Q_i` with the product σ-algebra, and `φ : C → C`. Hypotheses:

- **(P-dep)** each output component `φ_i` depends only on the coordinates in a finite set `N(i) ⊆ ι`,
  so `φ_i(s) = φ̂_i(s|_{N(i)})` for a local rule `φ̂_i`;
- **(P-V)** the observation at time `k` is `X_k = (φ^k s)|_V` (or a given function of it) for a finite
  site set `V`;
- **(P-ω)** the initial law is a probability measure `ω` on `C`. For finite alphabets this is a
  consistent family of finite-region distributions (Kolmogorov extension, compact factors, any index
  set [IR, standard]).

*Autonomous* means: one update `φ`, iterated, with no setting, input, intervention or controller
acting after time 0. N1.1–N1.4 and N2.1's form (i) are autonomous; N1.5 and N2.1's form (ii) are not.

Two sets, kept apart throughout (O2):

- **(i) the syntactic backward dependency set.** `ball(V, 0) = V`, `ball(V, k+1) = ⋃_{i∈ball(V,k)} N(i)`
  (the kernel's `ball`), and `U_n = ⋃_{k≤n} ball(V, k)`: the sites from which a chain of at most `n`
  reading steps reaches `V`. `U_∞ = ⋃_n U_n`. Hidden part `B_n = U_n \ V`. These are read off the
  declared reading sets, not off the actual influence. Note `U_{k+1} = V ∪ ⋃_{i∈U_k} N(i)`.
- **(ii) the genuine-influence set.** `J_n` is the set of sites `j` for which some `s, s'` differing
  only at `j` have different observation histories on `[0, n]` under the actual rule; `J_∞ = ⋃_n J_n`.
  The definition ranges over all pairs of configurations and does not involve the initial law.

`U_n` is finite, with `|U_n| ≤ |V| Σ_{k≤n} Δ^k` if `|N(i)| ≤ Δ`. `J_n ⊆ U_n` and `J_n ⊆ J_{n+1}`
(N2.1). The inclusion `J_n ⊆ U_n` can be strict (X2).

A fourth hypothesis is used only where a statement says that the patch data are finitely many:
**(P-fin)**, the alphabets `Q_i` are finite at the sites of the patch in question.

(P-dep), (P-V) and (P-fin) are finiteness premises. (P-ω) is the probability premise: no
deterministic statement below uses it.

### N1.2 Is (P-dep) derivable from the dynamics on an infinite carrier?

**Notation.** In Main:362 `V` is the whole site set ("$S=\prod_{i\in V}S_i$, with $V$ and each
$S_i$ finite"), so "Finiteness of $V$ is used in the first step" is finiteness of the whole site set.
Here `V` is the visible region.

**Check (countercontrol) [IR].** Main:362 derives the dependency sets from insensitivity to each single
component. On `(Z/q)^ℕ`, `f(s) = 1` if `s` has infinitely many nonzero entries and `0` otherwise is
unchanged by every single-coordinate change and is a function of no finite coordinate set. So on an
infinite carrier single-component insensitivity does not give finite dependency. **Verdict:** (P-dep)
is a stated hypothesis. On the selected model it is supplied by (xiii), "each $F_i$ reading the
current values at finitely many sites and each site read by finitely many $F_i$" (Main:724); the kernel
carries it on any site type through `leapFiniteRange` (`SecondOrderDrive.lean:306`), a `FiniteRange`
(`QuasilocalAlgebra.lean:919`, extending `CouplingGraph`) with `nbhd := gateRegion R`, under
`[DecidableEq ι]` with `[Fintype V]` for the alphabet. Off the selected model it is a single-carrier
dependency form of A3, which is not ledger item (ix) as worded ("at a single finite lattice the bound
holds automatically", Main:724). Lemma PM uses only the clause that each site reads finitely many
sites. The clause that each site is read by finitely many is used neither by Lemma PM nor by the
growth bound, which needs only `|N(i)| ≤ Δ`. It is the clause that the measure-preservation
proposition (M-full) of §P.3 uses, and the one that example B1 lacks. CONFIRMING.

### N1.3 Lemma PM (patch matching), autonomous form — stands on its reviewed terms (O10)

The statement is r3's, arranged so that the deterministic form comes first and the law form second
(OP). The letters (a), (b), (c) are kept because later sections cite them.

**Lemma PM [IR, proof here; Lean support as stated].** Assume (P-dep) and (P-V), autonomous. Let
`n ≥ 0`.

*Deterministic form (no probability; premises (P-dep), (P-V)).*

- **(a) Matching patch data give matching observation histories.** If `s, s' ∈ C` agree on `U_n`,
  then `X_k(s) = X_k(s')` for every `k ≤ n`. There is a map
  `G_n : ∏_{i∈U_n} Q_i → (C_V)^{n+1}` with `X_{0:n}(s) = G_n(s|_{U_n})` for every `s`.
- **(c) Rules and carriers, pointwise clause.** `G_n` is determined by the labelled set `U_n` with
  its alphabets, the reading sets `N(i)` and the local rules `φ̂_i` for `i ∈ U_{n−1}`. Consequently,
  two systems `(ι, Q, φ, V)` and `(ι', Q', φ', V)` agree in their observation histories on `[0, n]`
  from initial data that agree on the patch, whenever there is an injection `e : U_n → ι'` that is
  the identity on `V`, preserves alphabets, carries `N(i)` onto `N'(e(i))` and `φ̂_i` to
  `φ̂'_{e(i)}` for every `i ∈ U_{n−1}`.
- **Finiteness.** `U_n` is a finite set of sites (N1.1). Under (P-fin), `∏_{i∈U_n} Q_i` is a finite
  set: there are finitely many patch data. The **finite observational description at horizon `n`**
  is the map `G_n` on that finite set. No probability enters it.

*Law form (adds the probability premise (P-ω)).*

- **(b) Law.** Let the alphabets be finite, or countable with the discrete σ-algebra, or let the
  local rules be measurable. If two initial laws `ω, ω'` on `C` have the same marginal on `U_n`, the
  laws of `(X_0, …, X_n)` under `ω` and `ω'` agree. The law is `(G_n)_#(ω|_{U_n})`. Under (P-fin) it
  is a finite sum, and the description with probabilities is the pair `(G_n, ω|_{U_n})`.
- **(c) Rules and carriers, law clause.** Under the conditions of the pointwise clause, the two
  systems agree in their observation laws from initial laws with equal patch marginals.

Nothing in the lemma bounds `|ι|`; what is finite is the information needed to determine the
observations over those `n` steps.

**Premises used, in the three groups of §4.0.** *Finiteness and dependency:* (viii) site
factorization; one deterministic update; (P-dep); (P-V); nonempty alphabets (to extend partial
configurations); for the statement that the patch data are finitely many, (P-fin) (the local half of
total finiteness, kept as a premise). *Probability:* for (b) and the law clause of (c) only, a
probability measure on the product σ-algebra, with the measurability condition stated in (b).
*Further distributional properties:* none for (a) and (b); the law clause of (c) has equal patch
marginals as its hypothesis. **Not used:** finiteness of `ι`, a product prior, invariance,
bijectivity, a uniform degree bound, A1 in any form.

**Proof of (c), which contains (a).** For `0 ≤ k ≤ n` put `D_k = U_{n−k}`, so `D_0 = U_n ⊇ D_1 ⊇ … ⊇
D_n = V`. Claim: for each `k ≤ n` there is a map `g_k : ∏_{U_n} Q_i → ∏_{D_k} Q_i`, built only from the
data listed in (c), with `(φ^k s)|_{D_k} = g_k(s|_{U_n})` for all `s`. Take `g_0` the identity. Suppose
`g_k` given, `k < n`. Let `i ∈ D_{k+1} = U_{n−k−1}`; then `i ∈ ball(V, m)` for some `m ≤ n−k−1`, so
`N(i) ⊆ ball(V, m+1) ⊆ U_{n−k} = D_k`, and `i ∈ U_{n−1}`. Hence
`(φ^{k+1} s)_i = φ_i(φ^k s) = φ̂_i((φ^k s)|_{N(i)}) = φ̂_i(g_k(s|_{U_n})|_{N(i)})`, which defines
`g_{k+1}` from `g_k`, `N(i)` and `φ̂_i` for `i ∈ D_{k+1} ⊆ U_{n−1}`. Since `V ⊆ D_k`,
`X_k = g_k(s|_{U_n})|_V` (composed with the readout function), and `G_n = (g_k(·)|_V)_{k≤n}`. For the
second system, the same induction run on `e(U_n)` uses only `e`-transported copies of the same data;
the reading sets agree on `U_{n−1}`, so `e(ball(V, m)) = ball'(V, m)` for `m ≤ n` by induction on `m`,
and the two recursions produce the same `g_k` under `e`. ∎

**Proof of (b).** `s ↦ s|_{U_n}` is measurable for the product σ-algebra, and `X_{0:n} = G_n(s|_{U_n})`
by (c). `G_n` is measurable: its domain is a finite or countable discrete set in the first two cases,
and it is a composition of measurable local rules in the third. So the law of `X_{0:n}` is the
pushforward of `ω|_{U_n}` under `G_n`, and equal patch marginals give equal pushforwards. `φ` itself
need not be measurable. ∎

**Lean support.** `DependsOnlyOn` (`RegionTower.lean:249`), `iterate_dependsOnlyOn_ball` (:283),
`site_iterate_dependsOnlyOn` (:297) and `readout_unaffected_outside_ball` (:304) prove, for any
`CouplingGraph` on any site type with `[DecidableEq ι]` (section variables :246; no `Fintype ι`, no
`Fintype Q`), that a function depending on a finite region `A` depends after `k` steps only on
`ball G A k`; the last of these says that two configurations agreeing on the backward set of a readout
region give the same readout `k` steps later. This is the one-time, one-site, single-alphabet core of
(a). Kernel: dependence of `X_k` at one site on `ball({i}, k)`. Paper [IR]: monotonicity
`ball({i}, k) ⊆ ball(V, k) ⊆ U_n` (a `biUnion` monotonicity), the assembly over `i ∈ V` and `k ≤ n`,
the per-site alphabets `∏ Q_i`, the rule clause (c) and the law step (b). On the selected model
`i ∈ gateRegion R i` (`self_mem_gateRegion`, `SecondOrderLayer.lean:210`), so `ball` is monotone in `k`
there and `ball(V, n) = U_n`. CONFIRMING (kernel core) and POSITIVE (the written step).

### N1.4 The prior condition

**Check (argument) [IR].** The deterministic form of Lemma PM uses no prior. The law form (b) uses
normalization only. Three cases:

- *The observation law (b):* any normalized initial law, correlated across the patch boundary or not.
- *Main's transition matrices:* `T_ij(t)` uses "an initial hidden prior $\mu_H$ independent of the
  visible initial state", the law `P_0 ⊗ μ_H` (Main:516): independence across the visible/hidden
  boundary, not across the patch boundary. This is a further distributional property (D4 of §4.0).
- *A comparison (c) between carriers:* the two patch marginals must agree (D1 of §4.0). A product
  prior with the same patch factor suffices; the uniform product family has uniform marginals on
  every finite region on any site type (`uniform_family_consistent`, `RegionTower.lean:447`;
  `restrict_uniform_apply`, :408; `uniformFamily_isStateFamily`, `QuasilocalAlgebra.lean:887`).

**Verdict.** Product structure across the patch boundary is a condition of carrier comparisons
(GR:132's "given a normalized product prior on it"), not of the fixed-horizon description. The
validity note's marker AW-1 is correct for the comparisons it lists and sharpened here: the observation
law depends on the deep sector only through the patch marginal, for every normalized prior. The
normalized initial law is a premise of the law form only, a statement about the whole carrier that
asserts no cardinality (the audit's Q11 kind). Under A1 the counting measure supplied it; Main:58
already makes the prior "part of the realization datum". The reconstruction direction (visible law to
realizations) uses no prior on nature's carrier (N2.2). **NEW (EF-G1).**

### N1.5 Lemma PM-I: settings, inputs and adaptive policies (O6, O7, O13)

**History.** r2 traced the patch back from the last time only, and its statement was false in
general. *Counterexample (the review of r2's; recomputed in r3).* Shift `φ(s)_i = s_{i+1}`, `V = {0}`,
`n = 2`; `u_0` copies site 5 into site 1 (support `{1, 5}`), `u_1 = id`. Then `X_0 = s_0(0)`,
`X_1 = (u_0 s_0)(1) = s_0(5)`, `X_2 = (u_0 s_0)(2) = s_0(2)`, while r2's patch was `{0, 1, 2}`. The
patch must cover the full experiment, including the interventions and the information used to choose
them. r3 corrected the patch; the review of r3 re-derived the corrected lemma and could not break
it. r4 changes two things: the policy may remember its earlier reads, and the per-run and all-branch
forms are stated apart.

**Setting.** States `s_0, …, s_n` with `s_{t+1} = φ(u_t(s_t))` for `t < n`: at each step an
intervention `u_t : C → C` is applied and then the update. The observation is `X_t = s_t|_V`,
`t = 0, …, n`. Observations and policy reads at step `t` are taken from `s_t`, before `u_t`; the
patches below also cover the convention in which the observation is read after `u_t`.

*All-branch data.*

- An intervention `u` has **support** `A ⊆ ι` if, **for every state `s`**, `(u s)_i = s_i` for
  `i ∉ A` and `(u s)|_A` is a function of `s|_A`. A support contains every site `u` can read in any
  state and every site it can act on (Main:362's "an intervention that reads and writes only region
  $A$"; Main:366–369's setting operation `u^A_a × u^B_b × id`, "each intervention reading and
  writing only its own region"). An intervention can have several supports; the intersection of two
  supports is a support [IR], so a least one exists when a finite one does. A **declared support**
  is one of them, fixed with the protocol.
- A **protocol** specifies, for each `t < n`: a set `𝒰_t` of permitted interventions, each with a
  declared support; a set `R_t ⊆ ι` of substratum sites the policy may read at step `t`; and a rule
  `u_t = π_t(X_{0:t}, (s_τ|_{R_τ})_{τ≤t}, ξ) ∈ 𝒰_t`. The policy may therefore use the record, its
  present read and every earlier read. `ξ` is policy information not carried on the sites (a seed,
  an external register, a table of settings). `Â_t` is the union of the declared supports of the
  members of `𝒰_t`. `R_t` and `Â_t` are taken over **every branch**: every record, every state and
  every value of `ξ`. They do not depend on the run. An **open-loop** protocol is the case
  `𝒰_t = {u_t}`, `R_t = ∅`, no `ξ`: a given setting sequence. A setting generator inside the
  substratum is read through `R_t`.

**Hypothesis FS-all (finite supports over all branches).** For every step `t < n`, `R_t` and `Â_t`
are finite. In words: at each step, the set of all sites that the policy could read, and that any
intervention it could select could read or act on, taken over every record so far, every state and
every value of the policy information, is finite. With finite alphabets this is the same as:
finitely many distinct interventions can be selected at each step, each with a finite support, and
the policy reads inside one finite set [IR: finitely many maps are supported in a finite set with
finite alphabets; a finite union of finite supports is finite]. **Two weaker conditions do not give
it:** finite reads and actions on each individual run (examples E1–E3 below), and a bound on the
*size* of the support on each branch (example E2, where every branch has a support of two sites).
One finite patch for every branch, though not FS-all itself, also follows from finite reads on
every run, under the lemma's other hypotheses (Lemma K, part (f) below).

*Uniformity over the steps.* At a fixed horizon, FS-all is required at each of the `n` steps
separately; a finite union of `n` finite sets is finite, so no bound on `|R_t ∪ Â_t|` uniform over
the steps is needed. A bound uniform over the steps is needed only for a growth estimate in `n`.
For all horizons at once, finiteness at each step does not bound the union over all time; N2.1's
form (ii) states its own hypothesis for that case.

**The all-branch patch.** `D_n = V`. For `t = n−1, …, 0`:

`D'_t = ⋃_{i∈D_{t+1}} N(i)`,  `D_t = V ∪ R_t ∪ Â_t ∪ D'_t`,  and `E_n := D_0`.

Every `D_t` contains `V`, the policy-read sites `R_t` and the intervention supports `Â_t`. `E_n` is the
patch at time 0; it is not a union over `t`, and `D_0 ⊇ D_1` need not hold. Without interventions
`D_t = V ∪ ⋃_{i∈D_{t+1}} N(i)`, so `D_t = U_{n−t}` and `E_n = U_n`: Lemma PM-I then reduces to Lemma PM.

*Per-run data.* Here interventions are arbitrary maps `C → C` and the policy is any rule
`u_t = π_t(X_{0:t}, s_0, …, s_t, ξ)`; no support over all states is declared. Fix a run
`ρ = (s_0, ξ)`, with states `s_t` and choices `u_t`.

- **(RW-π) run-wise finite policy reads.** There are finite sets `R^ρ_τ`, `τ < n`, such that any run
  `ρ'` with the same `ξ` whose record agrees with `ρ`'s up to `t` and whose states agree with `ρ`'s
  on `R^ρ_τ` for every `τ ≤ t` makes the same choice at step `t`.
- **(RW-u) run-wise finite intervention reads.** For each `t < n` there is a finite `A^ρ_t` such
  that every state `s'` that agrees with `s_t` on `A^ρ_t` has `(u_t s')|_{A^ρ_t} = (u_t s_t)|_{A^ρ_t}`
  and `(u_t s')_i = s'_i` for `i ∉ A^ρ_t`.
- **The per-run patch.** `D^ρ_n = V`, `D^ρ_t = V ∪ R^ρ_t ∪ A^ρ_t ∪ ⋃_{i∈D^ρ_{t+1}} N(i)`,
  `E^ρ := D^ρ_0`. It depends on the run.

**Lemma PM-I [IR, proof here; parts (a)–(e) re-derived by the review of r3 in the all-branch form;
the memory clause, (a′) and (f) are r4's and were checked by the review of r4, under their stated
hypotheses].** Assume (P-dep), (P-V) and the setting above.

*Deterministic forms (no probability).*

- **(a) All-branch dependency (no finiteness hypothesis).** Under a protocol with declared
  supports: for each `t ≤ n`, the states `s_τ|_{D_τ}` for `τ ≤ t`, the record `X_{0:t}` and the
  interventions `u_0, …, u_{t−1}` are functions of `(s_0|_{E_n}, ξ)` determined by the protocol.
  Hence **two runs under the same protocol** (the same setting sequence; or the same policy `π` with
  the same `ξ`) **whose initial data agree on `E_n` have the same observation history on `[0, n]`**,
  on every branch.
- **(b) All-branch finiteness (under FS-all).** Every `D_t` is finite, so `E_n` is finite: one
  finite patch covers every branch. If also `|N(i)| ≤ Δ` and `|R_t ∪ Â_t| ≤ r_t`, then
  `|E_n| ≤ Δ^n |V| + Σ_{t<n} Δ^t (|V| + r_t)`. With (P-fin) on `E_n` the policy information enters
  only through a finite-valued function `ξ̄` of `ξ`, and the **finite observational description at
  horizon `n` under the protocol** is the map `G_n^π` from pairs (patch datum, value of `ξ̄`) to
  `(C_V)^{n+1}`.
- **(a′) Per-run.** Let the run `ρ` satisfy (RW-π) and (RW-u) at every step. Then `E^ρ` is finite,
  and every run under the same protocol with the same `ξ` whose initial configuration agrees with
  `s_0` on `E^ρ` has the same record on `[0, n]` and the same chosen interventions as `ρ`. The
  statement is about `ρ` and the runs that agree with it on `E^ρ`. It gives no single patch for all
  runs, and no finite description of the law.
- **(d) Without a shared protocol the conclusion fails.** Matching the initial patch alone does not
  give matching observation histories under different interventions.
- **(e) Without FS-all.** (a) still holds, with `E_n` possibly infinite. One finite patch for every
  branch is then not given by (b). Part (f) gives it under its own three hypotheses. Outside both
  it can fail, even when every run has finite reads (E2, E3) or almost every run has (E1).
- **(f) Lemma K: from finite reads on every run to one patch, by compactness.** Suppose the
  alphabet is finite at **every** site of `ι`, the policy information takes finitely many values,
  and (RW-π), (RW-u) hold at every step of **every** run (every `s_0 ∈ C`, every value of `ξ`). Then
  there is one finite set `E` such that two runs with the same `ξ` whose initial data agree on `E`
  have the same record. No bound on `|E|` is obtained, and no declared support for any intervention.
  All three hypotheses are used, and the conclusion can fail when any one of them is dropped (E1,
  E2, E3). In brief: one finite patch from finite reads on every run, under the lemma's other
  hypotheses.

*Law form (adds the probability premises).*

- **(c) Law.** Under the measurability condition of Lemma PM (b), with `π_t` measurable in `ξ`, and
  in the all-branch form: the observation law is the pushforward of the *joint* law of
  `(s_0|_{E_n}, ξ)` under `G_n^π`. For an open-loop protocol it is the pushforward of the marginal
  `ω|_{E_n}`. Equal marginals of the patch data and of `ξ` separately do not suffice when `ξ` is
  correlated with the patch.

**Which form is proved under which hypothesis.**

| Form | Hypothesis | What is proved | What is not |
|---|---|---|---|
| All-branch dependency, (a) | Declared supports; no finiteness | The record on every branch is a function of the patch data and `ξ` | That the patch is finite |
| All-branch finiteness, (b) | FS-all | One finite patch `E_n` for every branch, with an explicit bound; a finite description | Nothing about protocols outside FS-all |
| Per-run, (a′) | (RW-π), (RW-u) on the given run | A finite patch for that run and the runs agreeing with it there | One patch for all runs; a description of the law |
| Lemma K, (f) | Finite reads on every run; finite alphabets at every site; finitely many values of `ξ` | One finite patch for every branch exists | Any bound on its size. The conclusion can fail if one configuration has infinite reads (E1), if `ξ` takes unboundedly many values (E2) or if some alphabet is infinite (E3) |

**What gives one finite patch for every branch, and what does not (O13).** Adopted direction (c.6897455387):
"finite support on each individual run does not by itself establish one finite patch covering every
possible branch. The revised statement must make clear which it proves." Two hypotheses give it.
The first is FS-all (part (b), with a bound). The second is the conjunction of Lemma K's three
hypotheses (part (f), without a bound): finite reads at every step of *every* run, a finite
alphabet at *every* site, and finitely many values of the policy information. Finite reads on only
the runs considered do not give it; nor do finite reads on almost every run (E1), or on every run
without the other two hypotheses (E2, E3). The examples show that no one of the three hypotheses
can be dropped. They do not show that the conclusion fails whenever one of them is absent.

**Which form a result needs.** A statement about one run and its neighbours (a pointwise causal
statement about a given microstate) can use the per-run form. A **law over outcomes**, a **finite
observational description**, or a **comparison across settings** (the Bell ceiling's four setting
pairs on one ensemble; any statement that two different interventions lead to the same or to
different records from the same data) needs the all-branch form: the law is a pushforward of one
marginal only when one patch serves almost every run, and a comparison needs one patch that serves
both settings. §4.2 says which form each result class needs.

*Proof of (a).* Induction on `t`, with the cumulative claim that for every `τ ≤ t` the state
`s_τ|_{D_τ}` is a function of `(s_0|_{E_n}, ξ)`, together with `X_{0:t}` and `u_0, …, u_{t−1}`. For
`t = 0`: `s_0|_{D_0}` is the patch datum, and `X_0 = s_0|_V` with `V ⊆ D_0`. Suppose the claim holds
at `t < n`.
(1) *The intervention is determined.* `u_t = π_t(X_{0:t}, (s_τ|_{R_τ})_{τ≤t}, ξ)`; `X_{0:t}` is
determined by the induction hypothesis, and for each `τ ≤ t`, `R_τ ⊆ D_τ`, so the read at step `τ` is
determined (each earlier read at its own step, by the cumulative claim).
(2) *The post-intervention state on `D_t` is determined.* Let `A ⊆ Â_t ⊆ D_t` be the declared
support of `u_t`. For `j ∈ D_t \ A`, `(u_t s_t)_j = s_t(j)`. For `j ∈ A`, `(u_t s_t)_j` is a function
of `s_t|_A`, and `A ⊆ D_t`.
(3) *The next state on `D_{t+1}` is determined.* For `i ∈ D_{t+1}`,
`s_{t+1}(i) = φ̂_i((u_t s_t)|_{N(i)})` and `N(i) ⊆ D'_t ⊆ D_t`.
(4) *The next observation is determined.* `X_{t+1} = s_{t+1}|_V` and `V ⊆ D_{t+1}` (for `t+1 = n`,
`D_n = V`).
Two runs with the same protocol, the same `ξ` and the same `s_0|_{E_n}` therefore agree on every
`s_t|_{D_t}`, every `u_t` and every `X_t`. ∎

*Proof of (b).* Backward induction. `D_n = V` is finite by (P-V). If `D_{t+1}` is finite, `D'_t` is a
finite union of the finite sets `N(i)` (P-dep), and `D_t = V ∪ R_t ∪ Â_t ∪ D'_t` is a union of four
finite sets by FS-all. The bound follows from `|D_t| ≤ |V| + r_t + Δ|D_{t+1}|`. For `ξ̄`: with `Â_t`
finite and finite alphabets there are finitely many maps supported in `Â_t`, so `𝒰_t` is finite; the
argument sets `(C_V)^{t+1} × ∏_{τ≤t} C_{R_τ}` are finite; so `ξ ↦ (π_t(·, ·, ξ))_{t<n}` takes
finitely many values, and the run depends on `ξ` only through that value. ∎

*Proof of (a′)* [checked by the review of r4]. *Finiteness.* `D^ρ_n = V` is finite, and each `D^ρ_t` is a
union of three finite sets and finitely many finite sets `N(i)`. *Matching.* Let `ρ'` have the same
`ξ` and `s'_0|_{E^ρ} = s_0|_{E^ρ}`. Claim, by induction on `t`: `s'_τ` agrees with `s_τ` on `D^ρ_τ`
for every `τ ≤ t`, `X'_{0:t} = X_{0:t}`, and `u'_τ = u_τ` for `τ < t`. For `t = 0` this is the
hypothesis, with `V ⊆ D^ρ_0`. Step: (1) `R^ρ_τ ⊆ D^ρ_τ` for `τ ≤ t`, so by (RW-π) `u'_t = u_t`.
(2) `s'_t` agrees with `s_t` on `A^ρ_t ⊆ D^ρ_t`, so by (RW-u) `(u_t s'_t)` and `(u_t s_t)` agree on
`A^ρ_t`; for `j ∈ D^ρ_t \ A^ρ_t`, `(u_t s'_t)_j = s'_t(j) = s_t(j) = (u_t s_t)_j`, the last equality
by (RW-u) applied to `s' = s_t`. (3) For `i ∈ D^ρ_{t+1}`, `N(i) ⊆ D^ρ_t`, so
`s'_{t+1}(i) = s_{t+1}(i)`. (4) `V ⊆ D^ρ_{t+1}`. ∎

*Proof of (c).* `X_{0:n} = G_n^π(s_0|_{E_n}, ξ)` by (a); pushforward. *Example for the last sentence:*
`V = {0}`, `Q = Z_2`, `φ = id`, `u_0` flips site 0 when `ξ = 1`. If `ξ` is uniform and independent of
`s_0(0)` (uniform), `X_1` is uniform; if `ξ = s_0(0)`, `X_1 = 0`. The marginals of `s_0(0)` and of `ξ`
are the same in both cases. ∎

*Proof of (d).* `V = {0}`, `φ` the identity, `u_0` writes `a` at site 0 in one run and `b ≠ a` in the
other; the patches agree and `X_1 = a ≠ b`. ∎

*Proof of (e).* Steps (1)–(4) of (a) never use finiteness of `R_t` or `Â_t`. The failures are the
examples that follow. ∎

*Proof of (f)* [checked by the review of r4]. Fix a value of `ξ`. For `s_0 ∈ C` let `ρ = (s_0, ξ)` and
`Z(s_0) = {s' ∈ C : s'|_{E^ρ} = s_0|_{E^ρ}}`. It is a cylinder set, open in the product topology, and
it contains `s_0`. By (a′) the record is the same for every initial configuration in `Z(s_0)`. `C` is
a product of finite discrete spaces, hence compact (Tychonoff; for countable `ι`, König's lemma), so
finitely many `Z(s^1), …, Z(s^m)` cover `C`. Put `E_ξ = ⋃_k E^{(s^k, ξ)}`, a finite set. If `s'` and
`s''` agree on `E_ξ`, then `s' ∈ Z(s^k)` for some `k`; `s''` agrees with `s'` on `E^{(s^k, ξ)}`, so
`s'' ∈ Z(s^k)`; both have the record of `(s^k, ξ)`. Take `E` to be the union of the `E_ξ` over the
finitely many values of `ξ`. ∎

**Examples: finite reads on runs, no single finite patch.**

- **E1 (finite reads on almost every run, not on all).** `ι = ℕ`, `Q = Z_2`, `V = {0}`, `φ = id`;
  `u_0` writes at site 0 the value 1 if `s_j = 1` for some `j ≥ 1`, and 0 otherwise. At a state
  whose first 1 beyond site 0 is at `j`, (RW-u) holds with `A = {0, …, j}`. At a state with no 1
  beyond site 0 it fails for every finite `A`: a state agreeing on `A` with a 1 further out gets a
  different value at site 0. `X_1` is a function of no finite set of coordinates, so no finite patch
  exists at horizon 1, although under any product law that gives 1 positive probability almost
  every run has finite reads. Every support of `u_0` is all of `ℕ`. The review of r3 gives a
  variant (find the least `j ≥ 1` with `s_j = 1` and write `s_{j+1}` at site 0) and describes it as
  having finite reads on every run; it has them on every run except those with no 1 beyond site 0,
  which is why Lemma K does not apply to it.
- **E2 (unboundedly many branches; every run reads two sites).** `ι = ℕ`, `Q = Z_2`, `V = {0}`,
  `φ = id`, `ξ ∈ {1, 2, 3, …}` a seed of unbounded range, `u_0` copies site `ξ` into site 0. Every
  run reads and acts on `{0, ξ}`, and (RW-π), (RW-u) hold on every run with `E^ρ = {0, ξ}`. Here
  `X_1 = s_0(ξ)`. For any finite `F` take `ξ ∉ F`: two configurations that agree on `F` and differ
  at `ξ` give different records. No finite patch covers every branch. The alphabets are finite and
  every support has two sites; only the number of branches is unbounded. `Â_0 = ℕ`, so FS-all
  fails, as it must.
- **E3 (a read site named by an unbounded observed value).** `V = {0, 1}`, alphabet `ℕ` at site 0
  and `Z_2` elsewhere, `φ = id`, no seed; the policy reads the record `X_0` and selects "copy site
  `s_0(0) + 2` into site 1". Every run reads finitely many sites; the record at time 1 contains
  `s_0(s_0(0) + 2)`, a function of no finite set of coordinates. With a finite alphabet on `V` and no
  seed this cannot happen at a fixed horizon, because the record then takes finitely many values.
  That sentence concerns a site named by an *observed* value. An intervention that reads a hidden
  site with an infinite alphabet gives the same failure with a finite alphabet on `V`, no policy
  and no seed [the review of r4's example, re-derived here]: alphabet `ℕ` at the hidden site 1 and
  `Z_2` elsewhere, `V = {0}`, `φ = id`, and the one intervention "copy site `s(1) + 2` into site
  0". At a state `s` it satisfies (RW-u) with `A = {0, 1, s(1) + 2}`, so every run has finite
  reads, and `X_1 = s_0(s_0(1) + 2)` is a function of no finite set of coordinates.

**Check on the r2 counterexample.** With the all-branch recursion: `D_2 = {0}`; `D'_1 = {1}`,
`D_1 = {0, 1}`; `D'_0 = N(0) ∪ N(1) = {1, 2}`, `D_0 = {0} ∪ {1, 5} ∪ {1, 2} = {0, 1, 2, 5}`. All of
`X_0 = s_0(0)`, `X_1 = s_0(5)`, `X_2 = s_0(2)` are read on `E_2`.

**Remark (a smaller patch).** If observations and reads are taken before `u_t`, an intervention whose
support does not meet `D'_t` leaves `(u_t s_t)|_{D'_t} = s_t|_{D'_t}`, so its support may be left out
of `D_t`; this is the conditional form of the review of r2. For an adaptive policy the omission is made per
permitted intervention. The unconditional patch above is used in the statement because it is valid for
both reading conventions and needs no case distinction.

**The selected model is a special case (O10).** On the selected model every site reads itself
(`i ∈ gateRegion R i`), so in r2's recursion `D'_t ⊇ D_{t+1}`, hence `D_0 ⊇ D_1 ⊇ … ⊇ D_n = V`, every
`D_t` contains `V`, and r2's `⋃_t D_t` equals `D_0`. Steps (2)–(4) then go through with r2's patch, so
r2's open-loop statement held there as written; its adaptive clause held there when the policy-read
sites are added to `D_t` before the recursion continues. This argument uses self-reading at every site
of the patch. It does not establish the general intervention claim, which is false for r2's patch (the
shift has no self-reading) and is carried by the corrected patch above.

**Single-step form.** One intervention with support `A` at time 0, settings the same in both runs,
then `n` autonomous updates. The recursion gives `D_t = U_{n−t}` for `t ≥ 1` and
`E_n = U_n ∪ A`. With a readout only at the end, on a region `R` after `k` updates, the patch is
`U_k(R) ∪ A`, where `U_k(R)` is the backward set of `R`. This is the form the Bell ceiling consumes
(N3.6).

**Where FS-all comes from on `main`.**

- *Interventions.* Main:362 and Main:366–369 speak of interventions "reading and writing only" a
  region. Neither states that the region is finite. On `main` finiteness is automatic because
  Main:362 takes the whole site set finite ("with $V$ and each $S_i$ finite"). It is therefore a
  consequence of the total-finiteness premise there, not a separately stated premise. In the kernel,
  regions are `Finset ι` (finite by type) for readouts and local observables
  (`RegionTower.lean:249–307`; `QuasilocalAlgebra.lean:919–960`). A name search of four modules,
  `RegionTower`, `QuasilocalAlgebra`, `SecondOrderDrive` and `SecondOrderLayer`, found no
  intervention map with a read or action support on a site set as a kernel object [IR]; in
  `RegionTower.lean` the word occurs in docstrings (:33, :301, :492, :538) and in the name of an
  opened namespace (:73, `InterventionLocality`, declared at `ImplementationLocality.lean:95`),
  which concerns operational implementation classes on finite carriers. Other modules were not
  searched. **Without A1, finite action and read support of the permitted interventions, over all
  branches, is a premise to track.**
- *Policies and setting generators.* Main:406–407 says "when the setting generators are part of the
  system, the settings are functions of the full pre-setting microstate". No finite read support of a
  setting generator or policy is stated on `main`. The adaptive protocols of the gluing theorem
  (Main:564–566) run over a finite instrument family and a finite horizon inside a constructed
  realization; that is not a statement about read sites in a spatial substratum. **Finite read support
  of the policy, over all branches, is not on `main`: a premise to track.**

**Lean support.** None beyond Lemma PM's core. `readout_unaffected_outside_ball`
(`RegionTower.lean:304`) covers the case in which a change lies outside the backward set of the readout
region. The intervention recursion, the policy, the two forms and the finiteness steps are paper [IR].
ELABORATING (EF-G13); NEW (EF-G18, the two forms and Lemma K), checked by the review of r4.

### N1.6 Can the patch lemmas live in Main?

**Check (citation and Lean source).**

- (viii), (xiii) and `ruleDynamics` are Main ledger items with Main kernel citations (Main:724). The
  induction is already Main's (Main:362, "by induction").
- `QuasilocalAlgebra.lean:75` imports `OIBridge.RegionTower`, census family 8 ("quasilocal
  completion") lists `RegionTower` with Main anchor `quasiState_unique`, and the proof term of
  `iterate_dependsOnlyOn_ball` uses only `DependsOnlyOn`, `ball`, `Finset.mem_biUnion` and
  `Function.iterate_succ_apply` (read at :249–295): no GR mathematics, so it is not downstream by
  dependency.
- **Main:588 is not an input of Lemma PM.** Lemma PM is classical: a combinatorial cone and a
  pushforward. Main:588's quasilocal completion is the setting of the channel form N1.7.

**Root test.** Lemma PM (a), (b) serve two Main:60-listed consumers, the §3.3 cone and, through it,
the Bell ceiling. Clause (c) and the torus comparison of N1.8 serve no Main root at present; Main:60
places infinite hidden sectors outside its own statement. Two possible Main consumers exist, each an
owner choice: a fixed-horizon scope statement for the corner-occupancy claim (Main:216; N3.5), and a
fixed-horizon §3.2 setup taken from a finite torus (N3.10). Without one of them, (c) belongs with
GR:112/132.

**Root test for Lemma PM-I.** The one Main root that consumes an intervention form is the
Bell ceiling, with Main:362's own sentence on a single intervention. Both need one setting step with
the settings held the same in the runs compared. No Main root is named for the multi-step adaptive
form. So only the single-step form of N1.5 is a candidate for Main; the multi-step adaptive form stays
with this unit unless a consuming root is named. Either form would bring FS-all with it as a stated
premise.

**Verdict.** Lemma PM could be stated in Main on Main-level premises. Its deterministic form (a)
needs (viii); (P-dep) from (xiii) on the selected model or a single-carrier dependency form of A3 off
it; and (P-V); finite alphabets (the local half of total finiteness) make the patch data finitely
many. Its law form (b) adds a normalized initial law, as a separate premise. GR:132 is not used. Two ledger points
remain owner matters: (xiii)'s listed role is "for the continuous path of $*$-automorphisms … in §3.2
and §3.4" (Main:724), so using it for the cone widens that role; and (P-V) is a premise of the spatial
constitution, since `|C_V| < ∞` (Main:46) does not make the readout depend on finitely many sites.
POSITIVE.

### N1.7 Reduced channels

**Check (Lean source).** `heis_iterate_emb` (`QuasilocalAlgebra.lean:1330`) proves that after `k` steps
the Heisenberg transport of an observable of `Λ` is an observable of `hatIter Φ Λ k` (:1324, iterating
`hat`, :1040), for any `ReversibleDynamics` (:956) on any site type with finite alphabet `Q`.
`quasiState_stage` (:858) gives the expectation of a stage-`Λ` observable in the state of a consistent
family as `trace(X ρ_Λ)`. **Verdict [IR].** The reduced channels up to `n`, with the hidden state a
consistent family independent of the visible input, depend on that family only through its stage on
`hatIter(V, n) \ V`. Kernel: the localization and the stage formula. Paper, not written out here: the
composition of the two through the embedding of local observables into the completion, and the
Schrödinger-picture reading of the channel. This step has the Main:588 setting as input. ELABORATING.

### N1.8 Finite versus infinite native carriers

**Check (argument) [IR].** In the native class (the second-order rule of (xiii), nearest-neighbour
`F`, translation-invariant, uniform product prior), let `T_L` be the torus of side `L` and `Z^3` the
infinite lattice. If `L > 2n + diam(V)`, the graph `n`-neighbourhood `U_n` of `V` embeds in `T_L`
injectively, reading sets of `U_{n−1}` map onto reading sets, the local rules agree, and both patch
marginals are uniform. By Lemma PM (c) the observation laws agree on `[0, n]`. The uniform product
prior is a premise of this comparison (D2 of §4.0), not a derived property. **Verdict:** the
sufficient direction of the validity note's finding G8 follows from Lemma PM with Main's inputs,
without GR:112 (a) or GR:132; its placement follows N1.6. ELABORATING.

### N1.9 Skeptical pass on the favourable reading

**Check (measure theory) [IR, standard].** Without (P-dep), any measurable `f : C → C_V` is, for each
`ε > 0`, within `ε` in `ω`-probability of a function of finitely many coordinates (cylinder
approximation; Halmos, *Measure Theory*, 1950, §13, Thm D [IR]). So an approximate fixed-horizon finite
description holds for every measurable dynamics under every normalized prior. **Verdict:** the
fixed-horizon property is weak. It is the past cone of ordinary causal physics, it holds for finite and
infinite carriers alike, and so it does not by itself separate them; a result that distinguishes them
needs more. ELABORATING.

## 2. Uniform forms (task b)

### N2.1 The syntactic cone, genuine influence, and two sufficient conditions for one finite model (O2, O8)

**Genuine influence [IR, proof here].** Autonomous setting, (P-dep), (P-V). `J_n ⊆ U_n`, since
histories on `[0, n]` depend only on `U_n` (Lemma PM). `J_n ⊆ J_{n+1}`, since a history on `[0, n]` is
part of one on `[0, n+1]`. The history on `[0, n]` is a function of `s|_{J_n}`: let `s, s'` agree on
`J_n`; replacing `s'` off `U_n` by `s` changes no history (Lemma PM), and then `s, s'` differ at
finitely many sites of `U_n \ J_n`; changing them one at a time changes no history, by the definition
of `J_n`.

**Sufficiency, form (i): the autonomous form (record-shift factor) [IR, proof here; found by the
review of r2, restated under O8, checked by the review of r3].**

*Setting.* The **complete state** `z ∈ Z` is everything whose present value can affect a later
observation: the substratum configuration and, where a controller or policy acts, its whole memory
(seeds, counters, stored records, tables of future settings). Hypotheses:

- **(i-a) Determined evolution.** One map `Φ : Z → Z` gives `z_{t+1} = Φ(z_t)`; nothing outside `z`
  acts after time 0. The observation is `X_t = π(z_t)` with values in a finite set `C_V`.
- **(i-b) Finite relevant state.** The full record `R(z) = (π(Φ^t z))_{t≥0}` depends on `z` only
  through a measurable function of `z` with finitely many values.

*A sufficient condition for (i-b).* `Z` is a product over components (substratum sites and, where
present, memory cells), each history on `[0, n]` depends on finitely many components, and the set
`J_∞` of components that influence the record, **counted over the complete state**, is finite with
finite alphabets. Then `R(z)` is a function of `z|_{J_∞}` by the paragraph above, so `R` takes at most
`|C_{J_∞}|` values. In the autonomous substratum setting of N1.1, where no controller exists, the
complete state is the configuration `s`, (i-a) is autonomy, and the condition is: `J_∞` finite, with
finite alphabets on it.

*Conclusion.* There is one autonomous, deterministic, finite model that reproduces the observation
record from every initial state, and the observation law at every horizon under every initial law: the
system `(Im R, σ)`, where `σ` is the left shift on records, with readout `w ↦ w_0` and initial law
`R_#ω`. It has at most `|C_{J_∞}|` states.

*Proof.* `Im R` is finite by (i-b). For every `z`, `σ(R(z)) = R(Φ(z))`, because
`R(Φ z)_t = π(Φ^{t+1} z) = R(z)_{t+1}`; this step is (i-a). So `σ` maps `Im R` into itself. Started at
`w = R(z)`, the model's record is `(σ^t w)_0 = w_t = X_t(z)`. `R` factors through a measurable
finite-valued map, so `R_#ω` is defined, and the model's record law is the law of `R` under `ω`, which
is the observation law at every horizon. ∎

*What the general statement contains (finding 3).* Under (i-a), a finite autonomous model that
reproduces the record of every initial state exists exactly when `Im R` is finite, and (i-b) says
that `Im R` is finite. The general statement is therefore close to a restatement. Its content is the
intertwining `σ ∘ R = R ∘ Φ` and the step from a finite influence set to a finite `Im R`.

*Periodicity consequence of form (i).* By N2.3, every record is eventually periodic, with transient
less than `|Im R|` and period dividing `lcm(1, …, |Im R|)`. If `Φ` is surjective,
`σ(Im R) = R(Φ(Z)) = R(Z) = Im R`, so `σ` is a bijection of `Im R` and every record is exactly
periodic; the visible law is then pathwise periodic and N2.5 gives a realization in Main's form (a
bijection of `C_V × C_H` with one shared hidden prior).

*Corollary (finite syntactic cone).* `J_∞ ⊆ U_∞`, so a finite `U_∞` with finite alphabets gives the
same conclusion. In that case the model can also be taken on the substratum's own sites: every
`i ∈ U_∞` has `N(i) ⊆ U_∞`, so `φ_U(s|_{U_∞}) := φ(s)|_{U_∞}` is well defined and
`π_U ∘ φ = φ_U ∘ π_U`; if `φ` is surjective so is `φ_U`, hence a bijection of the finite set
`C_{U_∞}`. On the selected model the restriction is again of second-order form.

*Recheck of the proof against O8's hypotheses.* The proof uses (i-a) in exactly one place,
`σ ∘ R = R ∘ Φ`, and (i-b) in exactly one place, finiteness of `Im R`. Finiteness of the set of
influencing *substratum sites* gives (i-b) only when the complete state is the substratum
configuration. If a controller acts whose memory is not counted, (i-a) fails for the substratum alone
(its next state is not determined by its present state) and (i-b) may fail for the complete state. So
the statement "finitely many influencing sites give one autonomous finite model" holds only with the
complete relevant state finite, including any controller or policy memory, and its evolution
determined by that state.

**Sufficiency, form (ii): a finite model with inputs [IR, proof here; checked by the review of r3].**

*Setting.* Inputs remain external. `𝒰` is a set of permitted interventions, the same at every step.
**Each member of `𝒰` has a finite support.** `𝒰` itself may be infinite and the union of the
supports may be infinite: FS-all of N1.5 is not assumed. An input sequence `(u_0, u_1, …) ∈ 𝒰^ℕ` is
chosen by anything outside the model: an experimenter, a controller of any size, a policy that reads
the record. `s_{t+1} = φ(u_t(s_t))`, `X_t = s_t|_V`. For a finite word `w = u_0 … u_{m−1}` write
`X_m(s; w)` for the observation after `w`. `J^in_n` is the set of sites `j` for which some word `w` of
length `n` and some `s, s'` differing only at `j` give different histories on `[0, n]`;
`J^in_∞ = ⋃_n J^in_n`.

*Hypothesis.* `J^in_∞` is finite, with finite alphabets on it. This hypothesis supplies the
finiteness; the finite supports are used only to make each history depend on finitely many
coordinates.

*Conclusion.* There is one finite deterministic model **with inputs**, a Moore machine (finite
transducer) `(B, 𝒰, δ, λ)` with at most `|C_{J^in_∞}|` states, such that for every initial
configuration `s` and every input sequence the machine started at the state assigned to `s` outputs
exactly `X_0, X_1, …`. Each input acts on `B` through its transition map `δ(·, u)`, and there are at
most `|B|^{|B|}` such maps, so the inputs act through a finite alphabet even when `𝒰` is infinite.
It is not an autonomous model.

*Proof.* For a given word `w` of length `n`, the history on `[0, n]` depends on finitely many
coordinates (Lemma PM-I (a), (b) for the open-loop protocol `w`, whose `n` interventions each have a
finite support), hence on `s|_{J^in_n}` by the one-at-a-time argument.
So the behaviour `β_s : 𝒰^* → C_V`, `β_s(w) = X_{|w|}(s; w)`, depends only on `s|_{J^in_∞}`, and
`B = {β_s}` is finite. Put `λ(β) = β(∅)` and `δ(β, u)(w) = β(uw)`. Then `δ(β_s, u) = β_{φ(u(s))}`,
because `X_{|w|}(φ(u s); w) = X_{|w|+1}(s; uw)`; so `δ` maps `B × 𝒰` into `B`. After inputs
`u_0, …, u_{t−1}` the machine is in state `β_{s_t}` and outputs `β_{s_t}(∅) = s_t|_V = X_t`. ∎
Without finite supports the one-at-a-time step fails: "write 1 at site 0 if infinitely many sites
hold 1" is influenced by no single site other than site 0.

*Periodicity consequence of form (ii).* None. Example: `V = {0}`, `φ = id`, `𝒰` the interventions
"write `a` at site 0". Then `J^in_∞ = {0}`, the machine has `|Q_0|` states, and `X_{t+1}` is the
input at step `t`: an aperiodic input sequence gives an aperiodic record. Eventual periodicity holds
only in form (i).

**An unbounded external controller is not made finite by acting on finitely many sites.** In the
example just given the controller acts on one site and one substratum site influences the record. If
the controller holds a table of settings that is not eventually periodic, the complete state (site 0
together with the table) is not finite, the record is not eventually periodic, and by N2.3 no
autonomous finite model reproduces it.
Form (ii) applies; form (i) does not.

*From (ii) to (i).* If the inputs are produced by a controller with finitely many memory states whose
next memory state and next input are determined by its present memory state and the observation, the
machine of form (ii) together with the controller is a finite autonomous system, and form (i) applies
to the pair. This is the only route from form (ii) to an autonomous model given here.

**Necessity (finding 3 of the review of r3) [Proposition N: checked by the review of r4; the
refinement for one initial law: reviewer's refinement, checked by the recheck of r5].** Both forms are
sufficiency statements under hypotheses
that nothing here supports for nature. Whether the hypothesis of form (i) is also necessary depends
on what the model is asked to reproduce.

*Proposition N.* Autonomous substratum setting, (P-dep), (P-V), no controller. Consider:

- (N1) `J_∞` is finite;
- (N2) `Im R` is finite: finitely many records occur as `s` ranges over `C`;
- (N3) one finite autonomous deterministic model reproduces the record **from every initial
  configuration**: a finite set `W`, a map `f : W → W`, a readout `λ : W → C_V` and an assignment
  `e : C → W` with `X_t(s) = λ(f^t(e(s)))` for all `s` and `t`;
- (N3′) one finite autonomous deterministic model `(W, f, λ)` reproduces the observation law **under
  every initial law**: for each initial law on `C` there is an initial law on `W` under which the
  model's record has the same law.

Then (N2) ⟺ (N3) ⟺ (N3′); (N2) ⟹ (N1); and (N1) ⟹ (N2) when the alphabets on `J_∞` are finite. So,
with finite alphabets: **`J_∞` finite ⟺ finitely many records ⟺ one finite autonomous model
reproduces the record from every initial configuration.**

*Proof.* (N3) ⟹ (N2): `R(s)` is determined by `e(s) ∈ W`. (N2) ⟹ (N3): the model `(Im R, σ)` with
`e = R` and `λ(w) = w_0` (form (i)). (N2) ⟹ (N1): two distinct records differ at a finite time, and
`Im R` is finite, so there is `T` such that any two distinct records in `Im R` differ at some
`t ≤ T`. Then `R(s)` is determined by `X_{0:T}(s)`, which is a function of `s|_{U_T}` (Lemma PM (a)).
If `j ∉ U_T` and `s, s'` differ only at `j`, then `R(s) = R(s')`, so `j ∉ J_n` for every `n`. Hence
`J_∞ ⊆ U_T`, a finite set. (N1) ⟹ (N2) with finite alphabets: `R(s)` is a function of `s|_{J_∞}`
(first paragraph of this section), so there are at most `|C_{J_∞}|` records. (N2) ⟹ (N3′): push each
initial law forward by `R`, as in form (i); `R` is measurable under the condition of Lemma PM (b),
being a function of `X_{0:T}`. (N3′) ⟹ (N2): a point mass at `s` is an initial law; the
model's record law must be the point mass at `R(s)`, so `R(s)` is one of the at most `|W|` records of
the model. ∎

*The alphabet condition is needed for (N1) ⟹ (N2)* [IR]: sites 0 and 1, a two-letter alphabet at the
visible site 0, alphabet `ℕ` at site 1 holding a counter that decreases to 0 and stays there, and
site 0 showing 1 exactly while the counter is positive. Then `J_∞ = {0, 1}` and there are infinitely
many records.

*One fixed initial law: the answer depends on the law.* For an arbitrary law it is not necessary.
**X3** [IR]: the shift `φ(s)_i = s_{i+1}` on `Q^ℤ`, `V = {0}`, initial law a point mass on a
configuration with `s_i = s_{i mod 2}`. The record is periodic, so a two-state model reproduces the
law, while `J_∞ = {0, 1, 2, …}`. The set `J_∞` does not involve the initial law. X3's law is a
point mass: it gives probability zero to some finite patterns.

*Refinement: one law that charges every cylinder* **[reviewer's refinement; checked by the recheck of
r5]** (the review of r4's, re-derived here step by step). Autonomous substratum setting,
(P-dep), (P-V), no controller, with the measurability condition of Lemma PM (b). Let `ω` give
positive probability to every nonempty cylinder `{s : s|_F = a}`, `F` finite. With finite alphabets
at every site the uniform product prior is such a law. Suppose one finite autonomous deterministic
model `(W, f, λ)`, with some initial law on `W`, reproduces the observation law under `ω` at every
horizon. Then (N2) holds, and hence (N1).
*Proof.* (1) The model has at most `|W|` records, one for each initial state; let `F_W` be the set
of them, a finite subset of `(C_V)^ℕ`. The model's record law and `R_# ω` agree at every horizon,
that is on every cylinder of `(C_V)^ℕ`, hence on the product σ-algebra; the model's law is carried
by `F_W`, so `ω(R^{−1}(F_W)) = 1`. (2) `R` is continuous for the product topologies of discrete
alphabets, because each `X_t` is a function of the finitely many coordinates in `U_t` (Lemma PM
(a)). `F_W` is finite, hence closed, so `O := R^{−1}((C_V)^ℕ \ F_W)` is open, and `ω(O) = 0` by
(1). (3) A nonempty open subset of `C` contains a nonempty cylinder, which has positive
probability. So `O` is empty, that is `Im R ⊆ F_W`: finitely many records, which is (N2). (4) (N2)
⟹ (N1) by Proposition N. ∎
This direction uses no compactness and no alphabet condition. In the other direction, with finite
alphabets on `J_∞`, (N1) ⟹ (N2) ⟹ (N3′) covers every law. So, for a law that charges every
cylinder and with finite alphabets on `J_∞`: `J_∞` finite ⟺ one finite autonomous deterministic
model reproduces the observation law under that law. This agrees with N2.10 (3), which reaches the
same conclusion for the linear class under the uniform product prior by an entropy count.

*Consequence, with N2.10.* On an infinite lattice of the linear nearest-neighbour class under (LE),
`J_∞` is infinite, so by (N2) ⟹ (N1) there are infinitely many records and no finite autonomous
model reproduces the record from every initial configuration. No prior enters. This is a statement
about a model class. It says nothing about nature, and Verdict 3 is unchanged.

**Related one-directional statements.**

- *"Bounded cone only if `V`'s connected component is finite": false.* **X1** [IR]: on `ℕ`, phase-space
  form of (xiii), `F_0 ≡ 0`, `F_i(c) = c_{i−1}` for `i ≥ 1` (`N(0) = ∅`, `N(i) = {i−1}`; a valid
  `Rule`). Then `U_∞({0}) = {0}`, while the symmetrized component (Main:362 symmetrizes) is all of
  `ℕ`. The observation process is that of the isolated site, `(p, c) ↦ (c, −p)`, of order dividing 4.
- *"Finite genuine influence only if `U_∞` is finite": false.* **X2** [IR, algebra below]: over `Z_2`,
  sites `0` (visible), `a`, `b`, `w` and an infinite chain `w = w_0, w_1, …`, with
  `F_0(c) = c_a + c_b`, `F_a(c) = F_b(c) = c_w`, `F_{w_k}(c) = c_{w_{k+1}}`. The graph is infinite and
  connected, the update is a bijection (second-order form) and `U_∞` contains the whole chain. Put
  `d = x_a + x_b`: `d(t+1) = 2x_w(t) − d(t−1) = d(t−1)` in `Z_2`, so `d` evolves on its own, and
  `x_0(t+1) = d(t) + x_0(t−1)`. Hence `J_∞ ⊆ {0, a, b}`; the chain never affects the observer. Form
  (i) applies: here `x_0(t+3) = x_0(t−1)`, the record is exactly periodic with period 4. X2 is not
  translation-invariant and is not the selected model.

**Condition under which an infinite connected system has a finite genuine-influence set:** the
observer's history is driven by a finite subsystem whose combined update does not read the rest, as for
`d` in X2 (cancellation of the rest's contribution), or whose reading sets point away from the rest, as
in X1. N2.10 shows that no such cancellation occurs along a lattice axis for a class of linear
nearest-neighbour rules.

**Verdict.** "Bounded only if the observer's connected region is finite" stays withdrawn. What holds:
form (i) and form (ii) above, each a sufficiency statement; a finite `U_∞` is a special case of form
(i); and, for model classes with finite alphabets, a finite influence set is necessary as well as
sufficient for one finite autonomous model of the record from every initial configuration
(Proposition N, checked by the review of r4), and of the observation law under one law that charges
every cylinder (reviewer's refinement, checked by the recheck of r5). None of this says anything about
nature, and the all-time conclusion of Verdict 3 is
unchanged: F-one is not established here. NEW (EF-G11, the two sets; EF-G14, the sufficiency in its
two forms; EF-G19, the necessity reading).

### N2.2 Fixed-horizon realizations: existence and floors

**Definition.** `E2(n)` is the least `|C_H|` over finite realizations faithful on `[0, n]`, in the
deterministic, deterministic bijective (Main's class D, Main:97) or native class.

- *Existence, every law.* Class D: kernel `S_imp_D` (`Equivalence.lean:422`; Main:97, :550, :552);
  constructively the process dilation and response-table form (Main:516, :518, :520). Inputs: a finite
  visible alphabet and a finite horizon (Lemma 1, Main:46), with no locality, no prior on nature's
  carrier and no A1 ("a finite hidden space is constructed, not assumed", Main:60). Native class: the
  torus of N1.8 [IR].
- *Memory floor.* `|C_H| ≥ 2^{I*}` (`card_hidden_ge_two_pow_Istar`, `C3Necessity.lean:117`; Main:514,
  :612).
- *Randomness floor [IR, elementary].* In a deterministic realization `X_{1:n}` is a function of
  `(X_0, H_0)`, so `H(X_{1:n} | X_0) ≤ log₂|C_H|`. Bijective realizations also satisfy
  `log₂|C_H| ≥ H(X_{<t} | X_t)` (Main:97, :614). The all-time form for finite reversible substrata is
  on `main` (Struct:1255).
- *Minimal deterministic form.* The canonical predictive quotient `T(P)` (Main:620) is terminal among
  faithful deterministic realizations.

**Verdict.** `E2(n)` is finite at every horizon. With conditional block entropy growing at rate `h > 0`,
the deterministic `E2(n)` grows at least as `2^{hn}`. N2.4 strengthens this to every law that is not
pathwise eventually periodic with uniform bounds. ELABORATING (EF-G3).

### N2.3 Finite autonomous systems: eventual periodicity and its operational conditions (O3)

**Conditions.** *Autonomous:* one single map `f` on a carrier `X`, iterated, with no input after time 0.
*Deterministic:* `f` is a function. *Finite:* `|X| = N_tot < ∞`. *Visible:* `X_k = π(f^k(z_0))` for
a given readout `π`. The initial datum `z_0` may be a point (a single record) or drawn from a law on
`X` (mixed initial data).

**Statement [IR, proof here].** Let `M = lcm(1, …, N_tot)`.

1. *Records.* For every `z_0`, `f^{k+M}(z_0) = f^k(z_0)` for all `k ≥ N_tot − 1`. So every record is
   eventually periodic, with transient less than `N_tot` and period dividing `M`, uniformly in `z_0`.
2. *Bijective (or recurrent) representative.* If `f` is a bijection, `f^M = id`, so every record is
   exactly periodic with period dividing `M`. The same holds for the restriction to the eventual image
   (Main:60's representative), on which `f` is a bijection.
3. *Laws.* Under any initial law the visible law is pathwise eventually periodic with those uniform
   bounds: `X_{k+M} = X_k` almost surely for `k ≥ N_tot − 1` (a mixture of finitely many eventually
   periodic records). Under an `f`-invariant initial law the law is pathwise exactly periodic, because an
   invariant law is carried by the eventual image (`μ = f^{N}_# μ` is carried by `f^N(X)`, and
   `f^N(X)` is the eventual image for `N ≥ N_tot`).
4. *Stationary visible law.* If the visible law is stationary and pathwise eventually periodic with
   transient `P` and period `M`, then `P(X_{k+M} = X_k)` does not depend on `k` and equals 1 for
   `k ≥ P`, so it equals 1 for every `k`: the transient disappears.

*Proof.* On a set of `N_tot` points every orbit of `f` enters a cycle within `N_tot − c ≤ N_tot − 1`
steps, `c` the cycle length, and every cycle length is at most `N_tot`, hence divides `M`. This gives
(1); (2) is the case of no transient; (3) and (4) are stated with their proofs. ∎

**Outside these conditions the conclusion fails [IR].**

- *Continuing inputs or settings.* A finite system with input, `z_{k+1} = g(z_k, u_k)`, can output a
  nonperiodic record: with `X_{k+1} = u_k` (two visible states, `g` copying the input), any aperiodic
  input sequence, for instance experimenter choices, gives an aperiodic record. This is form (ii) of
  N2.1. Main's gluing theorem gives one finite reversible realization for a bounded family of
  interventions and a finite horizon `K` (Main:562, :564), whose output follows the settings within its
  horizon; with a continuum of interventions the obstruction of Main:486 applies.
- *Stochastic dynamics.* A one-state system emitting a fair coin at each step gives an i.i.d. record:
  not eventually periodic.
- *Staged or clocked constructions.* Main's fixed-horizon realizations carry a clock in the carrier
  (Main:520), so their size grows with the horizon; they are finite at each horizon and not one model
  for every horizon.

**Verdict.** The all-time claim, with its operational conditions: an autonomous, deterministic, finite
system without continuing inputs or settings gives eventually periodic records, with a transient
allowed, and exactly periodic records when the representative is bijective, the initial law invariant,
or the visible law stationary. Without those conditions no periodicity follows. CONFIRMING (of Main:60,
Main:638) and ELABORATING (the operational conditions).

### N2.4 Families of bounded size faithful at every horizon

**Statement [IR, proof here].** Within autonomous finite realizations (N2.3's conditions; class D's
correlated initial law allowed):

- **(B)** A family `(R_n)` of bijective realizations, `R_n` faithful on `[0, n]`, with
  `|C_V| · |C_H^{(n)}| ≤ N_tot` for all `n`, exists **iff** there is `M > 0` with `X_{k+M} = X_k`
  almost surely for all `k` (pathwise periodicity with a uniform period).
- **(D)** The same with deterministic, not necessarily bijective, realizations exists **iff** there are
  `P ≥ 0`, `M > 0` with `X_{k+M} = X_k` almost surely for all `k ≥ P`.

*Proof of (B), forward.* Put `M = lcm(1, …, N_tot)`. Each `φ_n` permutes at most `N_tot` points, so
`φ_n^M = id` and `X_{k+M} = X_k` pointwise in `R_n`. For `k + M ≤ n` the event `{X_{k+M} = X_k}` is an
event of `X_{0:n}`, so it has probability 1 in nature's law. Each `k` has some `n ≥ k + M`. *Converse.*
The shared-prior construction of N2.5 gives one realization of size independent of `n`. *Proof of (D).*
Forward as in (B), with N2.3 (1): `X_{k+M} = X_k` for `k ≥ N_tot − 1`. Converse: N2.5's construction
with transient `P`. ∎

**Scope.** "Iff exactly periodic" holds for (B) only. For (D) the condition is eventual periodicity
with uniform bounds. Neither statement covers realizations whose size grows with `n`, stochastic hidden
dynamics, or continuing inputs. **NEW (EF-G2).** It covers zero-entropy aperiodic laws (Sturmian
records, for example), which N2.2's entropy floor does not.

### N2.5 One realization for every horizon; the shared-prior construction

**Forward (Main:638, paper).** "a bijection on a finite set has finite order $L$, so any fixed
realization with a fixed prior has an exactly $L$-periodic multi-time law ($\varphi^{k+L} =
\varphi^k$)". Read pathwise [IR, one line from the parenthesis]: `π_V φ^{k+L}(a, h) = π_V φ^k(a, h)`
for every root and every `h`, under any initial law.

**Converse, with one prior shared by every root [IR, proof here].** Let `(P_a)_{a∈C_V}` be
root-conditioned laws of visible sequences with `P_a(X_0 = a) = 1` and `X_{k+M} = X_k` `P_a`-a.s. for
all `k ≥ P` (bijective case: `P = 0`). Put `L = P + M`; if `L = 1` the record is constant and
`φ = id` works, so take `L ≥ 2` (replace `M` by `2M` if needed). Hidden states `(τ, p, r)`: a table
`τ : C_V → C_V^L` with `τ(a)_0 = a`; a phase `p ∈ {0, …, L−1}`; a root record `r ∈ C_V ∪ {□}`. Prior:
`τ ~ ⊗_a P_a(X_{0:L−1} ∈ ·)`, `p = 0`, `r = □`. It does not depend on the root. Steps:

- `(x, τ, 0, □) ↦ (τ(x)_1, τ, 1, x)`;
- `(x, τ, p, r) ↦ (τ(r)_{p+1}, τ, p+1, r)` for `1 ≤ p ≤ L−2`;
- `(x, τ, L−1, r) ↦ (r, τ, 0, □)` if `P = 0`; `(x, τ, L−1, r) ↦ (τ(r)_P, τ, P, r)` if `P ≥ 1`.

From root `a`, `X_k = τ(a)_k` for `k < L` and `X_k = τ(a)_{P + ((k−P) mod M)}` for `k ≥ P`. Given
`X_0 = a`, `τ(a)` has the law of `X_{0:L−1}` under `P_a`, and nature's law satisfies the same
periodicity almost surely, so every multi-time law agrees at every horizon.

*Bijectivity when `P = 0`.* Let `K` be the set of consistent states: `(x, τ, 0, □)` for every `x`, and
`(τ(r)_p, τ, p, r)` for `1 ≤ p ≤ L−1`, `r ∈ C_V`. The step maps `K` into `K`. It is injective on `K`:
an image with phase 0 comes only from phase `L−1` and determines `(τ, r)`, hence its preimage; an image
with phase 1 comes only from phase 0 (for `L ≥ 3`, phase `p ≥ 1` maps to `p+1 ≥ 2`; for `L = 2` phase 1
maps to phase 0) and its root record is the preimage's `x`; an image with phase `p' ≥ 2` comes from phase
`p' − 1` with the same `(τ, r)`, which determine its visible coordinate. An injective self-map of the
finite set `K` is a bijection of `K`; extend it by the identity off `K`. The hidden space has
`|C_V|^{|C_V|(L−1)} · L · (|C_V| + 1)` elements (tables with `τ(a)_0 = a`, phases, root records). For
`P ≥ 1` the map is deterministic and not injective, as (D) allows. ∎

**Rooted versus multi-time.** The kernel pair `pper_of_finiteRootedRealizable`
(`RootedClassification.lean`) and `pper_has_responseRealization` (`RootedClassificationAllTime.lean`),
assembled in `finiteRootedRealizable_iff_pper` (:192), classify the rooted one-time maps `Γ_t`; `PPer`
(`RootedClassification.lean:32`) is root identity, row stochasticity and `Γ_{t+M} = Γ_t`. That is weaker
than the multi-time condition. Example [IR]: `X_0 = a`, `X_k = a` for even `k`, `X_k` i.i.d. uniform
for odd `k`, with `|C_V| ≥ 2`. Then `Γ` is periodic with `M = 2` and `PPer` holds, so a finite rooted
realization exists at every time by the kernel. The multi-time law is not eventually periodic:
`P(X_{k+M} = X_k) = 1/|C_V| < 1` for odd `k` and every `M`. By N2.4 (D) no autonomous deterministic
finite model reproduces its multi-time law at every horizon. So the kernel witnesses no direction of
the multi-time statement; both directions here are paper [IR].

**Verdict.** Under N2.3's conditions, one finite autonomous model valid at every horizon exists exactly
when the visible law is pathwise eventually periodic with uniform bounds (deterministic) or pathwise
periodic with a uniform period (bijective). This is the visible content of A1 *for the bijective
representative*; for a non-bijective finite map A1 gives eventual periodicity (N2.3 (1)). NEW (EF-G2).

### N2.6 Every finite-horizon law extends to an exactly periodic law

**Statement [IR, proof here].** Every law on `C_V^{n+1}` is the restriction to `[0, n]` of a law that is
pathwise periodic with period `n + 1`: extend each word `w_0 … w_n` periodically. With N2.5 that law has
one finite bijective realization valid at every horizon, with a shared prior. So no datum at a finite
horizon decides whether nature's law is pathwise periodic: the condition of N2.5 is consistent with
every finite-horizon record. Sub:344 already declines the inference in its own setting ("it does not
infer an all-time carrier from arbitrary finite-horizon laws"). ELABORATING.

### N2.7 Weaker uniform forms

- **E3-HMM** (finite-state hidden Markov realization with a stochastic hidden step). Weaker than N2.5:
  an i.i.d. fair coin is a one-state HMM. A stochastic hidden step is not OI's deterministic substratum.
  A deterministic dilation valid at every horizon needs a hidden sector growing with the horizon unless
  the visible law is pathwise eventually periodic with uniform bounds (N2.4 (D)), whatever the entropy
  rate. The hidden states of an HMM are a finite *memory*; they bound no substratum.
- **E3-lin** (bounded Hankel rank). Weaker again: a finite HMM has rank at most its number of states,
  and some finite-rank processes admit no finite positive realization (§5.5 [IR]). Main records the
  question as open: a completion beyond one finite carrier "must additionally show that its chosen
  completion retains finite predictive dimension" (Main:562; Main:356). Nothing on `main` derives E3-lin
  for nature, and locality does not give it. This is H-mem (§5).

### N2.8 Directions (§A.34)

Each row is one direction with its own witness.

| Statement | Holds? | Witness |
|---|---|---|
| finite carrier ⟹ bounded `U_n` and `E2(n)` | yes | `U_n ⊆ ι`; the carrier itself |
| `U_n`, `E2(n)` finite for every `n` ⟹ finite carrier | no | infinite native lattice (N1.8) [IR] |
| `U_∞` finite (autonomous) ⟹ one finite autonomous model ∀n | yes | N2.1, corollary of form (i) [IR, proof here] |
| one finite autonomous model ∀n ⟹ `U_∞` finite | no | X2 [IR] |
| `U_∞` finite ⟹ `V`'s connected component finite | no | X1 [IR] |
| complete relevant state finite, evolution determined by it ⟹ one finite autonomous model ∀n | yes | N2.1 form (i) [IR, proof here] |
| `J_∞` finite with finite alphabets on it, no controller outside the configuration ⟹ one finite autonomous model ∀n | yes | N2.1 form (i) [IR, proof here] |
| one finite autonomous model reproducing the record from every initial configuration ⟹ `J_∞` finite | yes | Proposition N, (N3) ⟹ (N2) ⟹ (N1) [checked by the review of r4] |
| `J_∞` finite, finite alphabets on it ⟹ one finite autonomous model reproducing the record from every initial configuration | yes | N2.1 form (i); Proposition N [IR, proof here] |
| one finite autonomous model reproducing the law under an arbitrary fixed initial law ⟹ `J_∞` finite | no | X3, a point mass [IR] |
| one finite autonomous deterministic model reproducing the law under one initial law that charges every cylinder ⟹ `J_∞` finite | yes | N2.1, refinement: `R` is continuous, the model's finitely many records form a closed set, and an open set of probability zero is empty [reviewer's refinement; checked by the recheck of r5] |
| `J_∞` finite, finite alphabets on it ⟹ one finite autonomous deterministic model reproducing the law under that law | yes | Proposition N, (N1) ⟹ (N2) ⟹ (N3′) [checked by the review of r4] |
| `J^in_∞` finite, inputs external ⟹ one finite model with inputs ∀n | yes | N2.1 form (ii) [IR, proof here] |
| `J^in_∞` finite, inputs external ⟹ one finite autonomous model, or a periodic record | no | N2.1, write-at-site-0 example [IR] |
| finite autonomous bijective model ∀n ⟹ pathwise periodic | yes | Main:638 (paper); N2.3 (2) |
| pathwise periodic ⟹ finite autonomous bijective model ∀n, shared prior | yes | N2.5 [IR, proof here] |
| finite autonomous deterministic model ∀n ⟹ pathwise eventually periodic, uniform bounds | yes | N2.3 (1), (3) [IR, proof here] |
| pathwise eventually periodic, uniform bounds ⟹ finite autonomous deterministic model ∀n | yes | N2.5, `P ≥ 1` [IR, proof here] |
| bounded bijective `E2(n)` ⟹ pathwise periodic | yes | N2.4 (B) [IR, proof here] |
| pathwise periodic ⟹ bounded bijective `E2(n)` | yes | N2.5 [IR, proof here] |
| rooted `PPer` ⟹ multi-time pathwise periodic | no | N2.5 example [IR] |
| finite system with continuing inputs ⟹ periodic record | no | N2.3 input example [IR] |
| pathwise periodic ⟹ finite carrier | no | finite periodic component with an infinite decoupled factor under a product prior [IR] |
| pathwise periodic, period `M` ⟹ bounded Hankel rank | yes | the law is carried by at most `\|C_V\|^M` records, each contributing a rank-one term at every cut, so the rank is at most `\|C_V\|^M` [IR] |
| bounded Hankel rank ⟹ pathwise periodic | no | i.i.d. fair coin: rank 1 [IR] |

So a finite observational description at every horizon implies nothing about the cardinality of
nature's carrier, and one finite autonomous model at every horizon is, at the visible level, the
periodicity condition of N2.5, which N2.6 shows no finite-horizon datum decides.

### N2.9 Candidate bearing on Main:638's open question (a) [IR; candidate only; existence, not joining]

**Where the open question is carried on `main` (read at `bf89ba13`).**

- `papers/Main.md:638`: "The open questions are (a) exact all-time gluing for recurrent families of
  multi-time laws — which compatibility conditions on the per-horizon realizations suffice".
- `papers/Main.md:731`, table row: "recurrent multi-time-law gluing and pre-recurrence window
  approximation open". `papers/Main.tex:4583` and `:5453` carry both.
- `papers/Introduction.md:178`: "Joining the realizations of section 3.1 for successive stretches of
  time exactly into one world for recurrent multi-time patterns", with `papers/Introduction.tex:841–843`.
- `verification/lean-manuscript-census.json:875`: the string "exact all-time gluing for recurrent
  families of multi-time laws" is a required Main **anchor** of the rooted-classification family, so a
  rewording of Main:638 needs the registry changed in the same commit (§A.35).
- `verification/lean/edge_rigidity_probe.py:6928`: guard `R7-RCL` requires the
  string "(a) exact all-time gluing for recurrent families of multi-time laws" in Main's consolidation
  Remark. A rewording would fail the guard unless the guard is changed with it.
- Two records that would not be edited: `verification/ROADMAP.md:1604` ("Recurrent multi-time-law
  gluing and pre-recurrence-window approximation remain open", in the frozen queue), and the
  intro-corpus audit's closure ledger, row R-09
  (`verification/audits/manuscript/intro-corpus-audit-20261026/CLOSURE-LEDGER.md:92`), which quotes the
  census anchor.
- Search made: `git grep -i` at `bf89ba13` over the whole tree for "all-time gluing", "multi-time-law
  gluing", "recurrent famil", "recurrent multi", "successive stretches", "multi-time patterns", and
  over `book/` and `papers/*.md` for "gluing", "glue", "all-time", "one world", "stitch". The book's
  hits concern the operational gluing theorem (`book/glossary.md:107`, `book/ch19-open-problems.md:126`)
  and unrelated uses; no book passage carrying open question (a) was found under these patterns. A
  paraphrase outside them is not excluded.

**Candidate.** In Main:638's setting (finite `C_V`, `C_H`, one bijection, one `μ_H` shared by every
root, **no inputs**): a family of root-conditioned multi-time laws is realized at every time **iff** it
is pathwise periodic with a uniform period. Direction ⟹: Main:638's own forward sentence, read
pathwise (paper). Direction ⟸: N2.5 (paper, proof here). Neither direction is kernel-checked.

**What the candidate does and does not answer.**

- *Existence, not joining.* The Introduction reads (a) as *joining* the realizations for successive
  stretches of time. The candidate proves that *some* all-time realization exists when the family is
  pathwise periodic. It does not show that given per-horizon realizations are restrictions of one
  realization. "Bijective realizations of uniformly bounded size" (N2.4 (B)) is a condition under which
  an all-time realization exists; it is not a compatibility condition under which the given ones join.
- *No inputs.* The only result Main names "gluing" is the action-labelled theorem (Main:564–568,
  "Gluing by restriction" over instrument families and horizons). If (a) is meant with interventions,
  N2.3's conditions fail and the candidate does not apply; N2.1's form (ii) is the relevant shape and
  carries no periodicity.
- *Reading of "recurrent families".* Main:638 itself says that for the rooted visible maps the
  all-time question "has an exact answer", and the guard's comment records that Main "narrows open
  item (a) to multi-time laws" (`edge_rigidity_probe.py:6911–6912`). So (a) concerns multi-time laws.
  If "recurrent families" means pathwise periodic families, the candidate answers the existence part;
  the text of (a) does not say more. A rewording of (a) would be a change to the manuscript, the
  guard, the census and the generated files in one commit, and a statement that (a) is answered would
  be a status change (§A.25) with two directions, neither of which is in the kernel (§A.34).

**Remark (bounded families) [IR, proof here; checked by the review of r3].** Let `(R_n)` be
bijective realizations with total size at most `N_tot`, `R_n` faithful on `[0, n]` for every `n`, and
`M = lcm(1, …, N_tot)`. Then every member `R_n` with `n ≥ M − 1` is faithful at every horizon.
*Proof.* `R_n`'s record satisfies `X_{k+M} = X_k` pointwise (`φ_n^M = id`), and nature's law satisfies
it almost surely by N2.4 (B). Under either law the record on any horizon is the same function (periodic
extension) of `X_{0:M−1}`, and the two laws of `X_{0:M−1}` agree because `n ≥ M − 1`. ∎ So under a
uniform size bound no joining is needed: a long enough member already serves every horizon. The remark
does not show that shorter members are restrictions of it.

Owner question Q7. NEW (EF-G12), candidate only.

### N2.10 Skeptical pass on the sufficiency result: the leading edge [IR, proof here; checked by the review of r3]

N2.1's form (i) is favourable to a route toward F-one, so its hypothesis is tested on the class nearest
the selected model (§A.31).

**Setting.** `ι = Z^d`. Each site carries a previous and a current value in `Z_q`; the update is the
phase-space form of (xiii), `x(t+1) = F(x(t)) − x(t−1)`, with `F` linear,
`F_i(x) = Σ_{j∈N_F(i)} c_{ij} x_j`, and nearest-neighbour reading sets, `N_F(i) ⊆ {i} ∪ {i ± e_m}`.
`V` is finite, `e` a coordinate direction, `v_0 ∈ V` a site of largest `e`-coordinate in `V`, and
`γ_k = ∏_{m<k} c_{v_0+me, v_0+(m+1)e}`. **Condition (LE):** `γ_k ≠ 0` in `Z_q` for every `k`. For a
translation-invariant rule with axis coefficient `c` this says `c` is not nilpotent modulo `q`; a unit
`c` satisfies it.

**Lemma LE.**

1. Under (LE), `v_0 + ke ∈ J_k` for every `k ≥ 0`. So `J_∞` is infinite and the hypothesis of N2.1's
   form (i) fails for this system.
2. Under (LE) and the uniform product prior, `H(X_k | X_{0:k−1}) ≥ log₂|γ_k Z_q| ≥ 1` bit for every
   `k ≥ 1`. If every `γ_k` is a unit, the current values `x_{v_0}(0), x_{v_0}(1), …` at the site
   `v_0` are i.i.d. uniform on `Z_q`, whatever `V` is.
3. Hence, for the observation law of this infinite system under the uniform product prior, no
   autonomous deterministic finite model is faithful at every horizon, and deterministic
   fixed-horizon realizations have `|C_H| ≥ 2^{n}/|C_V|` at horizon `n`.

*Proof.* Write the initial datum as `(x(−1), x(0))`. By induction `x(k) = P_k(F) x(0) − P_{k−1}(F) x(−1)`
with `P_{−1} = 0`, `P_0 = 1`, `P_{k+1} = F P_k − P_{k−1}`; `P_k` is `F^k` plus terms of degree at most
`k − 2`. The matrix entry `(F^m)_{v_0, j}` is a sum over reading paths of length `m` from `v_0` to `j`,
so it vanishes when the lattice distance exceeds `m`. The site `v_0 + ke` is at distance `k`, and the
only path of length `k` reaching it takes the step `+e` every time, so `(F^k)_{v_0, v_0+ke} = γ_k`.
Therefore `x_{v_0}(k) = γ_k · x_{v_0+ke}(0) + ℓ_k`, where `ℓ_k` does not involve `x_{v_0+ke}(0)`.
(1) Changing `x_{v_0+ke}(0)` by 1 changes `x_{v_0}(k)` by `γ_k ≠ 0`. (2) Every site of `V` is at
distance at least `k` from `v_0 + ke`, with equality only for `v_0` (choice of `v_0`), so `X_{0:k−1}`,
`ℓ_k` and the other components of `X_k` do not involve `x_{v_0+ke}(0)`, which is uniform and
independent of all other initial coordinates. Conditionally on those, `x_{v_0}(k)` is uniform on a
coset of the subgroup `γ_k Z_q`, which has at least two elements; conditioning on less cannot lower the
entropy. For unit `γ_k` the coset is `Z_q`, so `x_{v_0}(k)` is uniform and independent of the earlier
values at `v_0`, none of which involves `x_{v_0+ke}(0)`. (3) `H(X_{0:n}) ≥ n` bits by (2), while a deterministic model's record is a function of its
initial state; apply N2.2's randomness floor, or N2.4 (D). ∎

**Scope.** (i) The instance named in ledger item (xiii), "its instance with $q = 2$ and $F$ the
nearest-neighbour sum" (Main:724), has axis coefficient 1, a unit (the display at Main:294,
`u'_x = Σ_{z∼x} u_z + v_x`, `v'_x = u_x`). (ii) Item 3 is a statement about one model class under one prior. It is not a statement about
nature, it asserts no infinite carrier, and it leaves the all-time conclusion of Verdict 3 as it is.
(iii) X2 escapes (LE) because two paths cancel (`1 + 1 = 0` in `Z_2`); on a lattice axis the path is
unique. (iv) Whether `J_n = U_n` for these rules (no cancellation in the interior) is not decided.

**Verdict.** On the linear nearest-neighbour class with a non-nilpotent axis coupling, an infinite
lattice has an infinite genuine-influence set, so N2.1's sufficiency does not apply there, and its
observation law under the uniform product prior has entropy rate at least one bit per step. The
uniform product prior in items 2 and 3 is a premise (D2 of §4.0). NEW (EF-G15); checked by the review
of r3.

## P. What each finite object preserves and what it does not (O11, O12)

**Substantially revised in r4 (O14). P.4 and the statements that depend on it are corrected in r5
and awaiting check.**

Adopted direction (c.6896940222): "A finite description of observations need not preserve the original system's
bijectivity, invariant measure, recurrence structure, or other properties a downstream proof uses.
That is the main risk: transferring properties of finite whole systems to finite observational
descriptions without justification." Adopted direction (c.6897455387): "a bijection of the full system may
preserve its uniform product measure without making the finite observational description an
autonomous, measure-preserving system. The reviewer's new proof could establish the first;
transferring that property to the description remains a separate question." Adopted direction (O15, c.6897859755): "Failure
of automatic inheritance does not imply that no suitable finite closed model exists."

### P.1 Four finite objects that must not be confused

- **(α) The patch description** at horizon `n`: the finite set `C_{U_n}` of patch data and the map
  `G_n` to observation histories (Lemma PM, deterministic form); with a starting law, the
  probability `ω|_{U_n}` on it; with interventions, the map `G_n^π` of Lemma PM-I (b) and the joint
  law of patch data and policy information. It is a *description of observations*. It has no
  self-map of its own: the recursion of N1.3 sends data on `D_k` to data on `D_{k+1}`, a different
  set.
- **(β) A constructed finite realization** faithful on `[0, n]` (Main:516–520): a finite *whole
  system* with a bijection, built from the observation law. Whatever it has beyond the law on `[0, n]`
  is a choice of the construction ("the realized process after time $K$ is unconstrained", Main:520).
- **(γ) A finite torus** of the native class (N1.8): a finite whole system with the same local rule,
  whose observation law equals the infinite lattice's on `[0, n]` and not beyond.
- **(δ) An all-horizon model**, where one exists: the record-shift model `(Im R, σ)` of N2.1 form
  (i), the transducer of form (ii), or the shared-prior realization of N2.5. Each exists only under
  its own hypothesis, which nothing here supports for nature. It is treated in P.5.

A **chosen closure on the patch** (P.4 (b)) is a further finite whole system, of the kind of (β) and
(γ): a self-map of the set of patch data, added by choice, whose record agrees with nature's on the
window.

A property of a finite whole system, whether (β), (γ), a chosen closure or nature under A1, does not
pass to (α) automatically, and a property of (β), (γ), a chosen closure or (δ) does not pass to
nature because their observation laws agree with nature's on a window, or at every horizon. Neither
sentence says that no finite closed model with the property exists; that is a separate question
(P.4; O15).

### P.2 Property by property, for the patch description (α)

| Property | On (α) | Proof or counterexample |
|---|---|---|
| Determinism | **Preserved** | Lemma PM (a): the history is a function of the patch data; with interventions, of the patch data and the policy information, under one protocol (PM-I (a)) |
| The observation law on `[0, n]` and every functional of it | **Preserved**, given a starting law | Lemma PM (b). Includes `T^{(k)}` and, for an initial law `P_0 ⊗ μ_H`, the rooted maps `Γ_k` for `k ≤ n`; conditional memory `M_t` for `t < n`; readback gaps of order at most `n`; a visible return `Γ_k = I` with `k ≤ n` where one occurs |
| Locality and the causal cone | **Preserved** | It is what the patch is built from (N1.3) |
| Bijectivity, reversibility | **Not defined** for (α) as given, which has no self-map of its own; **not inherited automatically** by the maps it does have. Whether a bijective closure can be chosen is a separate question (P.4 (b)) | Example B2: the step between successive patches is non-injective although `φ` is a bijection; `G_n` is non-injective in X2 |
| Counting (uniform) measure as a marginal | **Preserved** for a uniform product prior | `restrict_uniform_apply` (`RegionTower.lean:408`): the patch marginal is uniform on `C_{U_n}`. The uniform product prior is itself a further distributional property (D2 of §4.0) |
| Invariance of the uniform product measure | **Not defined** on (α) as given (M-desc-own, P.4 (a)): the property is not inherited automatically by the description; whether a suitable finite closed model exists is a separate question (M-desc-some; Lemma C, checked by the recheck of r5). For the **full system** it is a separate claim, (M-full), P.3: it holds for a bijection with both locality clauses and finite alphabets at every site, by a proof checked by the review of r4, and for the second-order form by N3.2; B1, a bijection with finite reading sets in which some site is read by infinitely many sites, does not have it | P.3, P.4 |
| Stationarity of the record law on the window | A property of the law, **preserved when it holds for the full system** | Holds under a uniform product prior given invariance for the full system ((M-full), checked by the review of r4; N3.2). Does not hold in B1 (`X_0` uniform, `P(X_1 = 0) = 3/4`) or in general with interventions. The description as given has no map for the law to be invariant under. Under the uniform patch measure, stationarity of the window law is exactly the condition for a measure-preserving bijection of the patch data that reproduces the window to exist (Lemma C, checked by the recheck of r5) |
| Maximal-entropy selection among invariant measures (Main:54) | **Not defined** for (α) as given; not inherited automatically | The description as given has no self-map and so no set of invariant measures; a chosen closure has invariant measures, which are its own (P.4); on an infinite carrier the global entropy is infinite |
| Double stochasticity of `T^{(k)}`, `k ≤ n` | A property of the law. **Preserved when it holds for the full system**; it does not hold for every bijection with finite reading sets | It needs the uniform product prior and invariance for the full system: N3.2 for the second-order form; (M-full) for bijections with both locality clauses and finite alphabets at every site (checked by the review of r4). B1, a bijection with finite reading sets in which some site is read by infinitely many sites, has a column sum `3/2` under the uniform product prior |
| Recurrence structure (order `L`, cycles, `φ^L = id`, periodicity of the law) | **Not defined** on (α); **not shared** between nature and (β), (γ) or a chosen closure, each of which has its own | N3.1; example B3 |
| Cardinality of the hidden sector, absolute counts | **Not preserved** | `\|C_{B_n}\|` depends on `n`. Ratios of counts are preserved under a uniform product prior; a quantity that uses `m = \|C_H\|` itself is horizon-dependent on (α) |
| Conserved quantities, energy shells | **Not defined** | A shell is a subset of the whole carrier invariant under `φ`; the patch is not invariant, and a shell prior is not a product prior |
| Spectrum of the Koopman (permutation) operator | **Not defined** for (α) as given | No self-map of its own; a chosen closure's spectrum is its own |
| Typicality of individual states | **Not preserved as stated** | Under a uniform product prior every patch marginal is exactly uniform, an ensemble statement; no typicality statement for an infinite carrier is on `main` |
| Measurement independence | **Not supplied** | It is a statement about the initial law and the setting generators, not about dependency (N3.6) |

### P.3 The full system: claim (M-full), and the counterexamples

**The locality class of `main`.** Two clauses: (L1) each site's next value reads finitely many
sites; (L2) each site is read by finitely many sites. On `main`: ledger item (xiii), "each $F_i$
reading the current values at finitely many sites and each site read by finitely many $F_i$"
(Main:724); GR:132, "a locally finite coupling graph"; in the kernel, `FiniteRange`
(`QuasilocalAlgebra.lean:919–921`: `nbhd`, and `infl` with `mem_infl`) and `ReversibleDynamics`
(:956–959), which asks finite range of the map and of its inverse. On a finite site set both clauses
hold trivially (Main:362).

*Scope of the name (finding 8 of the review of r4).* Ledger item (xiii) states its two clauses for
the force map `F`. For the phase-space map `(p, c) ↦ (c, F(c) − p)` they give reading sets
`N_F(i) ∪ {i}` and read-by sets `{i : j ∈ N_F(i)} ∪ {j}`, both finite, so (L1) and (L2) hold for
it. For (xiii) itself N3.2 already gives invariance of the uniform product measure, by a proof
checked by the review of r2 and with the first clause only. What (M-full) adds is the general class
of bijections with both clauses and finite alphabets at every site: the hypothesis class of
GR:132's infinite case and the kernel's `ReversibleDynamics`. `main` does not select that class as
nature's dynamics.

**(M-full) Proposition [the review of r3's; re-derived step by step in r4; checked by the review of
r4, Steps 1–6, under its stated hypotheses].** Let
`ι` be any set of sites, every `Q_i` finite, `C = ∏ Q_i` with the product σ-algebra and the uniform
product probability `μ`. Let `φ : C → C` be a bijection satisfying (L1), with reading sets `N(i)`,
and (L2): for each `j`, the set `{i : j ∈ N(i)}` is finite. Then `μ(φ(E)) = μ(E) = μ(φ^{−1}(E))` for
every measurable `E`.

*Proof.*
*Step 1 (`φ` and `φ^{−1}` are measurable).* By (L1) each coordinate of `φ` is a function of finitely
many coordinates, so `φ` is measurable for the product σ-algebra and continuous for the product
topology. `C` is compact and Hausdorff (a product of finite discrete spaces). A continuous bijection
of a compact Hausdorff space onto itself is a homeomorphism. So each coordinate of `φ^{−1}` is a
continuous map from `C` to a finite discrete set; its level sets are open and compact, hence finite
unions of cylinder sets, so it depends on finitely many coordinates. Hence `φ^{−1}` is measurable.
*Step 2 (conjugating a finitely supported permutation).* Let `F ⊆ ι` be finite and let `γ` act by a
permutation of `C_F` on the `F`-coordinates and fix every other coordinate. Put
`G = {i : N(i) ∩ F ≠ ∅}`. By (L2), `G` is a finite union of finite sets, hence finite. Put
`ψ = φ γ φ^{−1}`. For any `s`, let `t = φ^{−1}(s)`. Then `t` and `γ t` agree off `F`, so for
`i ∉ G`, where `N(i)` does not meet `F`, (L1) gives `φ(γ t)_i = φ(t)_i = s_i`. So `ψ(s)_i = s_i` for
every `i ∉ G`.
*Step 3 (`ψ` preserves `μ`).* `ψ` is a measurable bijection (Step 1) that fixes every coordinate off
the finite set `G`. Write `C = C_G × C_{G^c}` and `μ = μ_G ⊗ μ_{G^c}`, with `μ_G` uniform on the
finite set `C_G`. For each `r ∈ C_{G^c}`, `ψ` maps the finite fibre `C_G × {r}` into itself
injectively, so `ψ(x, r) = (π_r(x), r)` for a permutation `π_r` of `C_G`. For measurable `E` with
sections `E_r = {x : (x, r) ∈ E}`, Tonelli's theorem applied to the measurable set `ψ^{−1}(E)` gives
`μ(ψ^{−1}E) = ∫ μ_G(π_r^{−1}(E_r)) dμ_{G^c}(r) = ∫ μ_G(E_r) dμ_{G^c}(r) = μ(E)`, because the uniform
measure on a finite set is invariant under its permutations. So `ψ_# μ = μ`.
*Step 4 (the transported measure is invariant under every such `γ`).* Put `λ = (φ^{−1})_# μ`, that
is `λ(E) = μ(φ(E))`; it is a probability measure by Step 1. Since `γ φ^{−1} = φ^{−1} ψ`,
`γ_# λ = (γ φ^{−1})_# μ = (φ^{−1})_# (ψ_# μ) = (φ^{−1})_# μ = λ`.
*Step 5 (`λ = μ`).* Let `F` be finite, `a, b ∈ C_F`, and let `γ` exchange `a` and `b` on the
`F`-coordinates. Then `γ^{−1}[b] = [a]` for the cylinders, so `λ([b]) = (γ_# λ)([b]) = λ([a])`. The
marginal of `λ` on every finite `F` is therefore uniform. Cylinders form a family closed under
finite intersection that generates the product σ-algebra, so a probability measure is determined by
its values on them: `λ = μ`.
*Step 6.* `μ(φ(E)) = μ(E)` for every measurable `E`; applied to `φ^{−1}(E)` it gives
`μ(E) = μ(φ^{−1}(E))`. ∎

*Where each hypothesis is used.* (L1): measurability, continuity and Step 2. (L2): finiteness of `G`
in Step 2, and nowhere else. Finite alphabets: compactness in Step 1, finite fibres in Step 3, the
uniform marginal in Step 5. Bijectivity: Steps 1, 3 and 4. In the kernel's class the finite range of
the inverse is part of the datum, so the compactness argument of Step 1 is not needed there, and
Step 2 is the kernel's forward-locality step (`agreeOffG_map`, `QuasilocalAlgebra.lean:943`). No
kernel statement of (M-full) itself was found (response table, R4-b).

*Consequences, conditional on (M-full)* [IR]. Under a uniform product prior the law of the
configuration is `μ` at every time, so the observation process is stationary; and for the readout
`s|_V` the matrices `T^{(t)}` are doubly stochastic at every `t`, by the computation of N3.2.

*Standing.* (M-full) is favourable to the framework, so §A.31 asks for more skepticism, not less.
Adopted direction (c.6897455387): "The reviewer's new measure-preservation proof also needs independent checking
before it supports any recovery classification." The review of r4 re-derived Steps 1–6 and found no
gap. That is one independent check of a paper proof, not a kernel check, and whether it meets the
owner's condition is the owner's decision. **No class in this file cites (M-full) as support for a
recovery classification.** (M-full) is a statement about the full system, by its own proof. The
description does not inherit it automatically; what can be chosen on the patch is in P.4.

**B1 (a bijection with finite reading sets, in which some site is read by infinitely many sites,
that does not preserve the uniform product measure) [IR, proof here; checked by the review of r3].**
`ι = ℕ`, `Q = {0, 1}`. Every sequence begins with exactly one of the words `0`, `10`, `11`, and with
exactly one of `00`, `01`, `1`. Let `φ` replace the first by the second: `0x ↦ 00x`, `10x ↦ 01x`,
`11x ↦ 1x`. Then `φ` is a bijection of `C`; each output coordinate `i` depends on the inputs at
`{0, 1, i−1, i, i+1}`, so (L1) holds, and the same is true of the inverse. Under the uniform product
measure `μ`, the cylinder `[0]` has measure `1/2` and its image `[00]` has measure `1/4`, so `μ` is
not invariant. With `V = {0}`: `T(0, 0) = 1`, `T(1, 0) = 1/2`, `T(1, 1) = 1/2`, and the column sum for
the value 0 is `3/2`. **B1 lies outside the locality class of `main`:** for `i ≥ 2`, output `i` is
`s_{i−1}`, `s_i` or `s_{i+1}` according to the values at sites 0 and 1, so sites 0 and 1 are read by
every site and (L2) fails; in Step 2 of the proof above the set `G` would be infinite. B1 is not
translation-invariant. What B1 shows is the following and no more: bijectivity with finite reading
sets, without (L2), does not give invariance of the uniform product measure. Lemma PM applies to B1,
since it needs (L1) only.

**Inside the locality class and outside it.**

| | Bijection with (L1) and (L2): the locality class of `main` | Bijection with (L1) only |
|---|---|---|
| Lemma PM and the patch description | Hold | Hold |
| Invariance of the uniform product measure, for the full system | Holds by (M-full), checked by the review of r4, given finite alphabets at every site; for the second-order form by N3.2, checked by the review of r2 | Not guaranteed (B1) |
| Stationarity of the record law, and double stochasticity, under a uniform product prior | Hold given invariance | Not guaranteed (B1: `P(X_1 = 0) = 3/4`; column sum `3/2`) |
| The description as given, as an autonomous measure-preserving system (M-desc-own) | Not defined; not inherited automatically (P.4 (a)) | The same |
| A measure-preserving bijection of the patch data that reproduces the window, under the uniform patch measure (M-desc-some) | A separate question, answered by Lemma C: one exists, given invariance for the full system; for second-order rules every fixed-boundary closure is one (Lemma C′). Both checked by the recheck of r5 | Exists exactly when the window law is shift-stationary (Lemma C, checked by the recheck of r5); B1 has none on its patch data, though it has finite closed models on other carriers (β) |

**B2 (the step between patches is not injective).** The shift `φ(s)_i = s_{i+1}` on `Q^ℤ` is a
bijection in the locality class. With `V = {0}`, `D_k = {0, …, n−k}`, and the step
`C_{D_k} → C_{D_{k+1}}` drops the coordinate at site 0. The description's own maps do not inherit
reversibility automatically, so a proof step that uses a permutation of the description's own state
space (a unitary `U_φ`, an order `N` with `φ^N = id`, an eventual image, a time-reversal pairing of
trajectories) finds none there. A bijection can be chosen on this patch (the rotation of P.4 (b3));
its order, image and pairings are then those of the chosen map.

**B3 (recurrence is not shared).** Under an i.i.d. uniform prior the shift's observation record is
i.i.d.: no return occurs with certainty at any time. A patch description exists at every horizon, and
every constructed realization (β), like every bijective closure, recurs, at a time set by the
construction or the choice. In the native class,
a torus (γ) recurs with its own order, while the infinite lattice's observation law gains at least one
bit per step under (LE) (N2.10). In the other direction, if nature were finite with order `L > n`, the
patch description at horizon `n` would not show `L`.

### P.4 The description and measure preservation: what is defined, and what can be chosen (corrected in r5; awaiting check)

**Distinctions of the adopted directions.** (c.6897455387): "a bijection of the full system may preserve its
uniform product measure without making the finite observational description an autonomous,
measure-preserving system. The reviewer's new proof could establish the first; transferring that
property to the description remains a separate question." (O15, c.6897859755): "Failure of
automatic inheritance does not imply that no suitable finite closed model exists. Any wording
suggesting the latter should be withdrawn." (O17, same comment): "So the closure result earns no
recovery credit yet. Its being a chosen, window-valid model does not automatically disqualify it
either: it could suffice for a theorem whose requirements are entirely confined to that window.
That is what the proof-requirements check must determine."

**What r4 said, and what is withdrawn.** r4 stated one claim, (M-desc): "there is a self-map `f`
of the set of patch data whose iterates give the record, `X_k = (f^k d)|_V` for `k ≤ n` and every
patch datum `d`, and the description's probability is invariant under `f`". It then said that
(M-full) does not imply (M-desc), with the shift as witness, and that (M-desc) fails for the
closures the description determines. The definition is existential, and under a uniform product
prior those two statements are false as stated: for the shift the rotation of (b3) below is such
an `f`, and by Lemma C one exists whenever the uniform product measure is invariant for the full
system. r4's case proofs were sound (the review of r4 checked them); its headline did not follow
from them. Both statements are withdrawn, together with every wording that suggested that no
suitable finite closed model exists. Two different things had been put under one name. They are
(a) and (b).

**(a) The finite observational description as defined: (M-desc-own).** The description at horizon
`n` is the finite set `C_{U_n}` of patch data, the map `G_n` to records on `[0, n]` and, with a
starting law, the probability `ω|_{U_n}` (P.1 (α)). It is a window. Its own maps are the steps
`C_{D_k} → C_{D_{k+1}}` with `D_k = U_{n−k}`, which lose one layer per step; with interventions the
sets `D_t` of N1.5 can grow or shrink from one step to the next. A sequence of maps between
different sets is not an autonomous system, and "invariant measure" has no meaning for it. So
(M-desc-own), "the description, with no added datum, is an autonomous system with an invariant
probability", **is not defined**. (M-full) does not alter this: it is about the map `φ` on `C` and
the measure `μ` on `C`, and `φ` does not act on the description. **The property is not inherited
automatically by the description; whether a suitable finite closed model exists is a separate
question**, taken up in (b). What the description does inherit from invariance of the full system,
under a uniform product prior, is two properties of probabilities: the law of the data on `D_k` at
time `k` is uniform on `C_{D_k}` for each `k`, and the record law is the restriction of a
stationary law. B1, which lacks the second locality clause, has neither (`P(X_1 = 0) = 3/4`).

*The one case in which the description determines a self-map (restriction; r4's case (2a), checked
by the review of r4).* `φ_U(d) := φ(s)|_{U_n}` for any `s` extending `d` is well defined when
`N(i) ⊆ U_n` for every `i ∈ U_n`, that is when `U_{n+1} = U_n`: the cone has stopped growing and
`U_n = U_∞`. Then, by the corollary of N2.1, `φ_U` is a self-map of the finite set `C_{U_∞}`, and
if `φ` is surjective, `φ_U` is surjective, hence a bijection that preserves the uniform measure of
`C_{U_∞}`. That is the finite-cone case, an F-one hypothesis that nothing here supports for
nature. When some site of `U_n` genuinely depends on a site outside `U_n`, as on any lattice whose
cone keeps growing, the restriction is not well defined.

**(b) A chosen closure on the patch: (M-desc-some).** A *closure* is a self-map `f` of the set
`C_{U_n}` of patch data, added by choice, that *reproduces the window*: `X_0(f^k d) = X_k(d)` for
every patch datum `d` and every `k ≤ n`, where `X_k(d)` is the `k`th entry of `G_n(d)`. When the
observation is the visible configuration itself this reads `(f^k d)|_V = X_k(d)`. The patch data
with a closure are a finite closed model in the sense of O15: a finite set, closed under its own
dynamics, whose record agrees with nature's on the window. (M-desc-some) is the statement that
some closure is a bijection; on a finite set a self-map preserves the uniform measure exactly when
it is a bijection (each point then has exactly one preimage). Finite closed models on other
carriers exist as well: a constructed realization (β) for every finite-horizon law (Main:516–520),
with a structured prior, and in the native class a torus (γ).

- **(b1) A closure always exists: the fixed-boundary closure [r4's case (2b); checked by the review
  of r4].** Choose a datum `b` on the sites outside `U_n` and put `f_b(d) := φ(d ⊔ b)|_{U_n}`.
  *Claim:* for every `s` extending `d` and every `k ≤ n`,
  `(f_b^k d)|_{U_{n−k}} = (φ^k s)|_{U_{n−k}}`; in particular `f_b` reproduces the record on
  `[0, n]`. *Proof:* induction on `k`. For `k = 0` both sides are `d|_{U_n}`. If the claim holds at
  `k < n` and `i ∈ U_{n−k−1}`, then `N(i) ⊆ U_{n−k} ⊆ U_n`, so
  `f_b(f_b^k d)_i = φ̂_i((f_b^k d)|_{N(i)}) = φ̂_i((φ^k s)|_{N(i)}) = (φ^{k+1} s)_i`. ∎ So a
  closure exists for every rule and every `b`. It is not determined by the description: it depends
  on `b`, and its record after time `n` is an artefact of `b`. Whether this particular closure is
  a bijection depends on the rule. For the shift on `Q^ℤ`, `|Q| ≥ 2`, `V = {0}`,
  `U_n = {0, …, n}`, it is `f_b(d_0, …, d_n) = (d_1, …, d_n, b_{n+1})`: not injective, and it sends
  the uniform measure on `Q^{n+1}` to a measure that is a point mass in the last coordinate. That
  is a fact about this closure of the shift, not about every closure of it: see (b3).
- **(b2) Lemma C: exactly when a measure-preserving bijective closure exists [reviewer's lemma;
  re-derived by writer; checked by the recheck of r5].** Assume (P-dep), (P-V), autonomous, finite
  alphabets on `U_n` (P-fin), `n ≥ 1`. For `v ∈ (C_V)^n` put
  `A_v = {d ∈ C_{U_n} : X_{1:n}(d) = v}` and `B_v = {d ∈ C_{U_n} : X_{0:n−1}(d) = v}`. The following
  are equivalent:
  - (C-i) there is a bijection `f` of `C_{U_n}` with `X_0(f^k d) = X_k(d)` for every `d` and every
    `k ≤ n`: a closure that preserves the uniform measure on the patch data;
  - (C-ii) `|A_v| = |B_v|` for every `v`: under the uniform measure on the patch data, the law of
    `X_{1:n}` equals the law of `X_{0:n−1}`. In words, the window law is shift-stationary.

  *Proof.* Each of the families `(A_v)_v` and `(B_v)_v` is a partition of `C_{U_n}` into possibly
  empty parts, because every datum has exactly one value of `X_{1:n}` and exactly one of
  `X_{0:n−1}`.
  *(C-ii) ⟹ (C-i).* Step 1: for each `v` choose a bijection `f_v : A_v → B_v`; one exists because
  the two finite sets have the same size. Step 2: let `f` be the union of the `f_v`. It is defined
  on all of `C_{U_n}` because the `A_v` partition it; it is injective because each `f_v` is and
  distinct `v` have disjoint targets `B_v`; it is onto because the `B_v` cover `C_{U_n}`. Step 3:
  by construction `X_{0:n−1}(f d) = X_{1:n}(d)`, that is `X_j(f d) = X_{j+1}(d)` for
  `0 ≤ j ≤ n − 1`. Step 4: claim `X_j(f^k d) = X_{j+k}(d)` whenever `j + k ≤ n`, by induction on
  `k`. For `k = 0` it is trivial. If it holds for `k` and `j + k + 1 ≤ n`, then
  `X_j(f^{k+1} d) = X_j(f(f^k d)) = X_{j+1}(f^k d)` by Step 3, since `j ≤ n − 1`, and
  `X_{j+1}(f^k d) = X_{j+1+k}(d)` by the induction hypothesis. Step 5: `j = 0` gives (C-i).
  *(C-i) ⟹ (C-ii).* Step 1: for `0 ≤ j ≤ n − 1`, apply the hypothesis to the datum `f d` with
  `k = j` and then to `d` with `k = j + 1`:
  `X_j(f d) = X_0(f^j(f d)) = X_0(f^{j+1} d) = X_{j+1}(d)`. Step 2: so
  `X_{0:n−1}(f d) = X_{1:n}(d)`, and `f` maps `A_v` into `B_v` for every `v`. Step 3: `f` is
  injective, so `|A_v| ≤ |B_v|` for every `v`; both families partition the same finite set, so
  `Σ_v |A_v| = Σ_v |B_v|`, and equality holds for every `v`. ∎

  *Corollary C1 [same marking].* Let every alphabet be finite and let `φ` satisfy (L1), so that it
  is measurable. If the uniform product measure `μ` is invariant, `μ(φ^{−1}E) = μ(E)`, then (C-ii)
  holds at every horizon. *Proof.* `X_k(s) = X_0(φ^k s)`, so
  `{s : X_{1:n}(s) = v} = {s : X_{0:n−1}(φ s) = v} = φ^{−1}{s : X_{0:n−1}(s) = v}`, and the two
  events have equal `μ`-measure. Each depends on `s|_{U_n}` only (Lemma PM (a)), and the marginal
  of `μ` on `U_n` is uniform, so their measures are `|A_v|/|C_{U_n}|` and `|B_v|/|C_{U_n}|`. ∎
  Hence, **conditional on a uniform product prior**, invariance for the full system ((M-full), or
  N3.2 for a second-order rule) implies (M-desc-some): a measure-preserving bijective closure
  exists.

  *Scope of Lemma C.* (1) It is stated for the uniform measure on the patch data, which is the
  description's probability only under a uniform product prior (D2). For another patch
  probability `p`, the line of (C-i) ⟹ (C-ii) shows that a bijection that preserves `p` and
  reproduces the window forces the law of `X_{1:n}` under `p` to equal that of `X_{0:n−1}`;
  whether shift-stationarity is then also sufficient is not proved here [writer's remark; not
  independently checked]. (2) The `f` built in (C-ii) ⟹ (C-i) is far from unique: any choice of
  the bijections `f_v` will do. (3) Where (C-ii) does not hold, no bijection of the patch data
  that preserves their uniform measure reproduces the window. B1 is an instance
  (`P(X_0 = 0) = 1/2`, `P(X_1 = 0) = 3/4`). That is a statement about closures on the patch data
  under the uniform patch measure only: B1's window law, like every finite-horizon law, has a
  finite closed model on another carrier with another prior (β).
- **(b3) Lemma C′: second-order rules [reviewer's lemma; re-derived by writer; checked by the
  recheck of r5].** Let the rule have the second-order form on any site set: each site carries a pair
  `(p_i, c_i) ∈ G × G` (previous, current), `G` a finite abelian group, and
  `φ(p, c) = (c, F(c) − p)`, each `F_i` reading the current values on a finite set `N_F(i)`; so
  `N(i) = N_F(i) ∪ {i}`. Let `b` be any datum on the sites outside `U_n`, with current-value part
  `b^c`. Then the fixed-boundary closure `f_b` (i) reproduces the record on `[0, n]` from every
  patch datum, (ii) is a bijection of `C_{U_n} = G^{U_n} × G^{U_n}`, hence preserves its uniform
  measure, and (iii) is again of second-order form, on the finite site set `U_n`.
  *Proof.* (i) is (b1). (ii) For `i ∈ U_n`, `f_b(p, c)_i = (c_i, F_i(c ⊔ b^c) − p_i)`. Put
  `F^b_i(c) := F_i(c ⊔ b^c)`, a function of `c ∈ G^{U_n}`; then `f_b(p, c) = (c, F^b(c) − p)`.
  Define `g(p′, c′) := (F^b(p′) − c′, p′)`. Then
  `f_b(g(p′, c′)) = (p′, F^b(p′) − (F^b(p′) − c′)) = (p′, c′)` and
  `g(f_b(p, c)) = (F^b(c) − (F^b(c) − p), c) = (p, c)`. So `f_b` is a bijection with inverse `g`,
  for every `b` and every `F`, linear or not. (iii) `f_b` has the displayed form with force `F^b`,
  and `F^b_i` reads `N_F(i) ∩ U_n`. ∎ So for the selected model, ledger item (xiii), every
  fixed-boundary closure is a measure-preserving bijective closure. The shift is a first-order
  rule, and its fixed-boundary closure is not injective (b1); there the rotation
  `f(d_0, …, d_n) = (d_1, …, d_n, d_0)` is a bijection of the patch that preserves the uniform
  measure and reproduces the record on `[0, n]`. It is the periodic boundary condition, that is
  the torus (γ) of side `n + 1`; its record after time `n` repeats with period `n + 1`, which
  nature's i.i.d. record does not.

**What a chosen closure is, and what it is not.**

- It is chosen, not determined by the description: Lemma C's `f` depends on arbitrary bijections
  `f_v`, Lemma C′'s on the boundary datum `b`, the rotation on the choice of a periodic boundary.
- It agrees with nature on `[0, n]` and is valid there only. After time `n` its record is its own.
- Its order, cycles, eventual image, spectrum and set of invariant measures are its own. Nothing
  in Lemma C or Lemma C′ is a property the description has by itself.
- The measure it preserves is the uniform measure on the patch data, which is the description's
  probability only under a uniform product prior (D2), a further distributional property.
- It is a finite whole system of the kind of (β) and (γ).

**Conclusion, in the owner's form.**

1. A bijection of the full system may preserve its uniform product measure: (M-full), checked by
   the review of r4 under its stated hypotheses; N3.2 for the second-order form.
2. That does not make the finite observational description an autonomous, measure-preserving
   system. The description as defined is a window with no autonomous dynamics, and an invariant
   measure is not defined for it. The property is not inherited automatically.
3. Whether a suitable finite closed model exists is a separate question, and it is not answered in
   the negative. On the patch data themselves, under the uniform patch measure, a
   measure-preserving bijection that reproduces the window exists exactly when the window law is
   shift-stationary, hence whenever the full system preserves the uniform product measure; for
   second-order rules every fixed-boundary closure is one (Lemmas C and C′, checked by the recheck of r5).
4. Such a closure is a chosen model valid on the window only. Its existence is not the
   description being an autonomous measure-preserving system; the transfer the adopted direction separates
   out is not made by (M-full), by Lemma C or by Lemma C′.
5. The closure result earns no recovery credit yet. Its being a chosen, window-valid model does
   not automatically disqualify it either: it could suffice for a theorem whose requirements are
   entirely confined to that window. Whether it preserves everything required to recover a
   particular audited result is still unproved, for every class. No class cites (M-full), Lemma C
   or Lemma C′ as support.

**The record law under the uniform patch measure.** `(G_n)_#` of the uniform measure on `C_{U_n}`
need not be uniform on `(C_V)^{n+1}`: for `φ = id` it is carried by the constant records. Given
invariance for the full system and a uniform product prior it is stationary on the window; in B1
and with interventions it is not in general (P.2).

**Consequence for result classes (O17).** What decides is where a proof's requirements lie. §4.2
records this class by class, in the column "requirements confined to the window?".

- *Requirements entirely confined to the window* (a fixed number of steps `k ≤ n`: one-step
  channels and matrices, `T^{(k)}`, the cone, a return that occurs inside the window). The
  description itself carries those that are functionals of the record law. Where the proof also
  uses a bijection of a finite carrier with a uniform hidden state, a closure could supply one on
  the window; for second-order rules every fixed-boundary closure does (Lemma C′, checked by the recheck of r5). For
  such a class the closure could suffice. That is to be determined by checking the theorem's
  requirements against the closure, and there is no credit yet. One point is already visible. The
  populations, that is the matrices `T^{(k)}` for `k ≤ n`, are fixed by the window law. The action
  of a channel on off-diagonal inputs counts coincidences of the hidden states reached from two
  roots (Main:310 (ii) is the linear one-step instance); that count is not a functional of the
  record law, and it depends on the closure. Example [writer's; not independently checked]: over
  `Z_2` let `φ(s)_0 = s_0 + s_1`, `V = {0}`, `n = 1`, so the patch is `{0, 1}` and the record is
  `(d_0, d_0 + d_1)`. The maps `(d_0, d_1) ↦ (d_0 + d_1, d_1)` and `(d_0, d_1) ↦ (d_0 + d_1, d_0)`
  are both bijections of the patch data that reproduce the window. Under the first the hidden
  outputs from the two roots coincide for every hidden input; under the second they never do. So
  a statement about off-diagonal action proved on a closure is a statement about that closure.
  Whether the fixed-boundary closures of one rule agree with one another, and with the stage form
  of N1.7 for the full system, is not derived here.
- *A requirement outside the window* (all-time recurrence, or the order of nature's bijection; an
  eventual image; global bijectivity of nature's map on the whole carrier; a spectrum; a conserved
  shell of the whole system; one carrier serving every experiment). A closure cannot supply it:
  what a closure has of these is its own, fixed by the choice and not by nature (N3.1). This is a
  statement about what a window-valid model can establish about nature. It is not a statement that
  no finite closed model has the property.
- *A property of the record law on the window only* (double stochasticity of `T^{(k)}` for
  `k ≤ n`; stationarity). No closure is needed. It would follow from invariance for the full
  system together with a uniform product prior, as a statement about the full system: N3.2 for the
  second-order form, (M-full) for a bijection with both locality clauses and finite alphabets at
  every site. The owner's condition on (M-full) stands and the uniform product prior is a further
  distributional property (D2), so no recovery classification rests on this.

### P.5 The all-horizon model (δ) (finding 8)

The "F-one" rows of §4.2 refer to an all-horizon model, so the owner's risk applies to it as well.
For the record-shift model `(Im R, σ)` with readout `w ↦ w_0` and initial law `R_# ω` (N2.1 form
(i), under its hypothesis) [IR, proof here]:

| Property | On (δ) | Reason |
|---|---|---|
| Determinism; the observation law at every horizon | Kept | N2.1, proof of form (i) |
| Eventual periodicity of the record | Kept, and true of nature's record **under the hypothesis**, because the model reproduces the record at every horizon | N2.3 |
| Bijectivity of `σ` | Only if `Φ` is surjective (then `σ(Im R) = Im R`), or in N2.5's construction when the law is pathwise periodic | N2.1; N2.5 |
| Invariance of the initial law | `R_# ω` is `σ`-invariant exactly when the observation process is stationary: `σ_# R_# ω = (R ∘ Φ)_# ω` is the law of the record read from time 1 | direct |
| Uniform (counting) prior | Not supplied: `R_# ω` is in general not uniform on `Im R`, and `Im R` is not a product `C_V × C_H`. N2.5's realization has a product carrier and one prior shared by every root, a product of the root-conditioned laws, not the uniform one | N2.5 |
| A statement defined by counting over `C_H` (Main:115) | Not supplied | previous row |
| A statement for any prior shared by every root (Main:135–143) | Supplied by N2.5's realization when the law is pathwise periodic | N2.5 |
| Hidden cardinality, shells, spectra, order | The model's, not nature's | they are properties of the chosen model |
| Recurrence of nature's microstate | Not supplied | only the record is reproduced |
| Measurement independence | Not supplied | as for (α) |

For the transducer of form (ii): determinism and the record for every input sequence are kept; the
transition maps `δ(·, u)` need not be bijections; no periodicity and no invariant law are defined
without a law on the inputs.

### P.6 Consequence

The fixed-horizon description preserves determinism, the cone, and the observation law on the window
with everything computed from that law. It does not automatically inherit bijectivity, an invariant
measure, a selection principle among invariant measures, recurrence, absolute hidden cardinalities,
conserved shells, spectral statements or measurement independence. Each of these, where a downstream
proof uses it, needs its own argument: a proof that the property holds for the infinite system in a
form the proof can use (as N3.2 does for invariance on the second-order form, and as (M-full) does
for a bijection with both locality clauses, by a proof checked by the review of r4), together with a
proof that the theorem needs it only in that form; or a finite closed model that has the property
on the window, where the theorem's requirements are confined to the window (P.4; O17); or a direct
proof of the theorem's observable conclusion that does not use it (§4.2; O19). A property of the
full system is not thereby a property of the description, and that is not a statement that no
suitable finite closed model exists. §4.2 lists, class by class, the properties each proof uses.
NEW (EF-G16, what is and is not preserved; EF-G17, the measure claims, corrected in r5 and awaiting
check).

## 3. Result classes (task c)

### N3.1 Recurrence and indivisibility at `t_R` (kept)

**Check (argument) [IR, elementary].** Let `R` be a finite bijective realization faithful on `[0, n]`,
of order `L`. If `L ≤ n`, then `X_{k+L} = X_k` a.s. for `k ≤ n − L` and `Γ_L = I`: an exact visible
return inside the window. Hence, if nature's `Γ_L ≠ I` for every `1 ≤ L ≤ n`, every realization faithful
on `[0, n]` has order larger than `n`, and its recurrence lies outside the window on which it reproduces
the law ("the realized process after time $K$ is unconstrained", Main:520). Corollary: with Landau's
function `g` (the largest order of a permutation of `m` points), such a realization of total size
`N_tot` has `g(N_tot) > n`. If a return does occur within the window, the overlap-and-return theorem
certifies P-indivisibility from visible data (Main:141–143; `pIndivisible_of_identity_return_of_overlap`,
`RecurrenceHorizon.lean:119`, which assumes only that `Γ_s` is row-stochastic), with no A1.

**Verdict.** A finite description for a chosen horizon supplies no recurrence guarantee within that
horizon. What carries over is the visible-certificate part (Main:141–143; Main:157 with
`c4r_implies_pIndivisible`, `CausalReadback.lean:134`). Confirms the audit's treatments AM-1.1 and
AM-1.3b. NEW (EF-G4).

### N3.2 A1-test candidate 3 and ledger item (iii)

**Invariance for the second-order form [IR, proof here; standard; checked by the review of r2].**
Write the phase-space map of (xiii) as `φ = σ ∘ ψ` on `G^ι × G^ι` (previous, current), with
`ψ(y, x) = (F(x) − y, x)` and `σ` the sitewise swap. `σ` preserves the uniform product measure
`μ^ι ⊗ μ^ι`. For each `x`, `y ↦ F(x) − y` acts coordinatewise by bijections of the finite group `G`,
so it preserves every cylinder's measure and hence `μ^ι` (π–λ theorem). `ψ` is measurable because each
output coordinate depends on finitely many coordinates (local `F`). Tonelli:
`(μ^ι⊗μ^ι)(ψ^{−1}E) = ∫ μ^ι({y : (F(x) − y, x) ∈ E}) dμ^ι(x) = ∫ μ^ι(E^x) dμ^ι(x) = (μ^ι⊗μ^ι)(E)`,
with `E^x` the section at `x`. So `φ` preserves the uniform product measure, for every local `F`,
linear or not, on any site set. The observation process is then stationary. This proof uses the
second-order (shear) form and only clause (L1). It is independent of (M-full) of §P.3, which gives
the same conclusion for every bijection with both locality clauses and finite alphabets at every
site (checked by the review of r4, under its stated hypotheses).
Without the second clause the conclusion is not guaranteed: B1 is a bijection with finite reading
sets in which some site is read by infinitely many sites, and it does not preserve the measure.

**Double stochasticity [IR, proof here].** Take the visible readout to be `s|_V` (or a readout with
equal-size fibres). Under the uniform product measure `ω` the visible marginal is uniform and the hidden
part is independent of it (Main:516's `P_0 ⊗ μ_H` form). So
`Σ_i T(i, j) = Σ_i ω(π_V φ s = j | π_V s = i) = |C_V| · ω(π_V φ s = j) = |C_V| · ω(π_V s = j) = 1`,
and likewise for `φ^t`. The inputs are a uniform product prior (D2 of §4.0), its invariance (D3) and
the independence of visible and hidden initial data (D4); each is a further distributional property.

**Verdict.** Candidate 3 (audit §11: finite carrier, bijective dynamics, uniform hidden prior imply a
doubly stochastic one-step matrix) does not discriminate finite from infinite carriers within the
second-order class: the infinite native lattice gives a doubly stochastic matrix at every step. Given
(M-full), checked by the review of r4, the same holds for every bijection with both locality clauses
and finite alphabets at every site. Both statements are conditional on a uniform product prior. What the
candidate tests is an invariant prior with uniform visible marginal (the audit's AM-3, W3 kind). The
same fact bears on ledger item (iii), whose injectivity recovery uses "the observed statistics, in the
uniform-prior doubly stochastic scope" (Main:724): doubly stochastic statistics hold on infinite
carriers of the second-order class too, so they carry no information about the carrier's cardinality.
PR #1303 is provenance only (§9). NEW (EF-G5).

### N3.3 Counting measure and the uniform prior

The uniform family is consistent on any site type with uniform finite-region marginals
(`uniform_family_consistent`, `restrict_uniform_apply`; `uniformFamily_isStateFamily`,
`referenceState_stage`, `QuasilocalAlgebra.lean:887`, :904). So the baseline matrices with the uniform
prior have a fixed-horizon form on an infinite carrier, computed from the uniform measure on `C_{B_n}`
(Lemma PM). The *selection* of Lemma 3 is not inherited automatically by the description: global
maximal entropy is infinite there, and the description as given has no self-map, so no invariant
measures to select among. Whether a suitable finite closed model exists is a separate question
(§P.4; Lemma C, checked by the recheck of r5); a chosen closure has invariant measures, which are its own. A finite-stage characterization that could stand in for the
selection is on `main`: the uniform state is the unique normalized state invariant under every permutation matrix and
every phase gate (`invariant_normalized_eq_uniform`, `RegionTower.lean:507`), at each finite stage.
Adopting it as nature's prior selection is a premise (posit (iv) kind; audit Q6). ELABORATING.

### N3.4 Bijectivity and surjectivity

The eventual-image and surjectivity steps are statements about a self-map of a finite set (Main:60). The
description as given has no self-map of its own (§P, B2); a fixed-horizon realization is bijective by
construction (Main:520), and a chosen closure on the patch is bijective by choice or by the form of the
rule (§P.4). So the fixed-horizon form carries neither step as a statement about nature's map: both
concern the whole carrier, outside any window. On the selected model bijectivity on any site set is
definitional (`a2_every_substratum`, `leapEquiv`; the validity note's G4). CONFIRMING.

### N3.5 Corner occupancy (Main:216)

Main:216: "fundamental dynamics of continuous-time Markov type would require an actually infinite hidden
sector". In the native class, N1.8 gives for every horizon `n` a finite torus whose observation law
equals the infinite lattice's on `[0, n]`. So, in the native class, the *finite-versus-infinite
alternative* in that sentence is not distinguished by an observation over any fixed horizon, and as a
test of the carrier's cardinality it currently establishes no justified constraint on observations
over a fixed horizon there. This is narrower than a statement about the whole of Main:216.

*The first-order clause, checked at Main:340 (finding 13f).* Main:216 identifies Doukas's bound with
"the second-order estimate of §3.2", which is Main:340. That estimate is a short-time statement, for
`t` of order `τ_S` with `τ_S ≪ τ_B`. Its written derivation uses: the §3.2 setup with a finite hidden
space and `ρ_H = I_m/m` (Main:266, :280); a continuous interpolation of the permutation unitary,
"chosen rather than derived" (Main:272); a generator that is exactly Hamiltonian at `t = 0`; a bath
state moving at rate `1/τ_B`, whose first-order effect is a Hermitian drift of order
`(τ_S/τ_B)‖V_int‖`; a bounded coupling `V_int`; and, for near-unitarity, the weak-coupling condition
`‖V_int‖ τ_S ≪ 1` beside the slow-bath condition. Nothing in it is uniform in the horizon, and no
recurrence is used. Whether the same estimate holds with the stage state on a horizon-dependent patch
in place of the finite hidden space has not been derived here or on `main`. The finite/infinite
distinction in Doukas's bound itself is a continuum-time, long-time distinction. So the weakest
sufficient form for this class is undetermined. ELABORATING.

*Divergence window [IR] (EF-G10).* If the infinite-lattice observation process under the uniform
product prior, which is invariant by N3.2, has entropy rate `h > 0`, then
`H_{T_L}(X_{0:m}) ≤ log₂|C_{T_L}| = 2L³ log₂ q` while `H_{Z^3}(X_{0:m}) ≥ (m+1)h`, so the laws differ at
some `m ≤ 2L³ log₂ q / h`; by N1.8 they agree for `2m + diam V < L`. Under condition (LE) of N2.10,
`h ≥ 1` bit, so the condition `h > 0` holds on that class [IR, proof in N2.10, checked by the review of r3]. The
uniform product prior is a premise here (D2 of §4.0), not a derived property. NEW.

### N3.6 Causal cone and the Bell ceiling: dependency coverage, and measurement independence apart (O9)

**Reading sets and the distance (finding 7).** Main's hypothesis (iii) measures `d` in the
symmetrized graph `G_φ` of *actual* one-step dependence (Main:362). In this section `N(i)` is
therefore the actual one-step dependency set of site `i`: the sites `j` for which two states
differing only at `j` give different `i`th outputs. Given declared finite reading sets, the actual
sets are reading sets as well [IR: change the finitely many declared sites outside the actual set one
at a time]. Every `j ∈ N(i)` is a neighbour of `i` in `G_φ`, so `U_k(R) ⊆ B_{G_φ}(R, k)`.

**Dependency coverage [IR, proof here; checked by the review of r3].** In Main's Bell theorem
(Main:364–388) the settings are interventions `u^A_a × u^B_b × id` on disjoint regions `A`, `B` at one
step, and `Ω` is a pre-setting variable. Let `s` be the pre-setting state and `s'` the post-setting
state. Wing `A`'s outcome, `k_A` updates after the setting, is a function of `s'` on
`W_A := U_{k_A}(R_A)`, the backward set of the readout region (Lemma PM (a)). By hypothesis (iii),
`d(B, R_A) > k_A`, so `B` does not meet `B_{G_φ}(R_A, k_A) ⊇ W_A`. On `W_A \ A`, `s' = s`; on
`W_A ∩ A`, `s'` is determined by `a` and by `s` on **all of `A`**. So the outcome is a function `q_a`
of `s|_{W_A ∪ A}`, and symmetrically `r_b` of `s|_{W_B ∪ B}`. Put

`Ω_n :=` the pre-setting state on `W_A ∪ W_B ∪ A ∪ B`.

This is the single-step form of Lemma PM-I (N1.5), with the settings held the same in the runs
compared, which is how the theorem conditions on `(a, b)`.

**Which form of PM-I this is (O13).** The all-branch form. The theorem compares four setting pairs
on one ensemble and sums over `Ω` with one weight `p(Ω)` (Main:378), and `Ω` must fix "each wing's
response to every setting" (Main:364–365). So one patch has to serve every setting: the regions `A`
and `B` are the declared supports of all the settings `u^A_a`, `u^B_b`, and `Ω_n` does not depend on
`(a, b)`. `Ω_n` takes finitely many values when `A`, `B`, `R_A`, `R_B` are finite, the reading sets
are finite and the alphabets on the patch are finite. **Finiteness of `A`, `B`, `R_A` and `R_B` is a
premise here**: Main's clause (ii) does not state it, and on `main` it follows from the finite site
set of Main:362 (N1.5, "Where FS-all comes from"). A per-run patch would not do: it could differ
between settings and between runs, and no single `p(Ω)` would be defined on it.

*Settings generated inside the substratum.* If the settings are outputs of generator regions `G_A`,
`G_B` read at the setting step (the adaptive form of PM-I with `R_t = G_A ∪ G_B`), the patch that
determines the whole run, settings included, is `W_A ∪ W_B ∪ A ∪ B ∪ G_A ∪ G_B`, finite when the
generator regions are finite over every branch (FS-all).

**This is dependency coverage only.** Including the setting regions, and the setting-generation
regions, shows which finite data determine the outcomes. It does not establish measurement
independence.

**(MI) Measurement independence: a separate, named premise.** `p(Ω_n | a, b) = p(Ω_n)`: the
response-relevant pre-setting data on `W_A ∪ W_B ∪ A ∪ B` are statistically independent of the
settings. With (MI), the finite-`Ω` proof of Main:383–388 applies to `Ω_n` as written:
`P(q, r | a, b) = Σ_{Ω_n} p(Ω_n) 1[q = q_a(Ω_n)] 1[r = r_b(Ω_n)]`. Without (MI), nothing in the patch
argument gives it: when the generators are inside the substratum the settings are functions of the
patch data on `G_A ∪ G_B`, and conditioning on `(a, b)` reweights whatever those data are correlated
with. (MI) is a further distributional property (D6 of §4.0).

*Status of (MI) on `main`.* A posit, not derived:

- ledger item (xiv), Main:724: "measurement independence, $p(\Omega\mid a,b)=p(\Omega)$ — the
  response-relevant pre-setting variable $\Omega$ is uncorrelated with the setting generators' outputs —
  a posit about the initial condition, not derived";
- hypothesis (iv) of the theorem, Main:372–374: "the interventions act on one common pre-setting
  ensemble, so $p(\Omega\mid a,b)=p(\Omega)$";
- Main:404–408: measurement independence "is retained as a posit about the initial condition, not
  derived: when the setting generators are part of the system, the settings are functions of the full
  pre-setting microstate, and (iv) fails for that microstate whenever more than one setting pair
  occurs";
- no kernel statement: a search of the Lean sources under `verification/lean-mathlib/` and
  `verification/lean/` for "measurement independence" and "CHSH" (several spellings) found no file
  [IR].

The patch form needs (MI) for `Ω_n` only, which follows from (xiv) for any variable of which `Ω_n` is a
function, and is the weaker statement.

**Verdict.** The fixed-horizon form appears sufficient for the *dependency* part of the theorem for
experiments of finite duration; the audit's proposed restatement P4 would not be needed for that part.
(MI) is tracked separately and is untouched by this unit. A recovery candidate, not a recovered result.
ELABORATING (EF-G6).

### N3.7 GR:58 and GR:70, energy-shell counting

GR:58 starts from "the finite total system" restricted to a conserved energy shell, and GR:70 uses
`N_i = Ω_H(E − e_i)` with a time-reversal pairing of shell trajectories. The description as given is
not self-contained, so it has no shell of its own (§P); a shell is a property of the whole system,
outside any window. Growing tori have shells whose counts depend on their size; a
consistent family over growing tori needs a stated energy density, and its limit is a Gibbs-type
measure (equivalence of ensembles [IR, standard; e.g. Georgii, *Gibbs Measures and Phase Transitions*,
1988]). The shell prior is not a product prior (the validity note's G7), so Lemma PM (c) does not cover
it. **Verdict:** not carried. CONFIRMING.

### N3.8 Substratum Theorem 23

Traced at the lines given; the theorems of the SM paper that Stage 2 (b)–(e) cite were not traced.

- *Stage 1* (Sub:123–137). Inputs include A1 (Sub:123); the output is "a triple $(S, \varphi, V)$ with
  $S$ finite, $\varphi$ a bijection on $S$" (Sub:125). The derivation obtains the triple from Main's
  finite-horizon equivalence, "a deterministic bijection $\varphi$ on an enlarged finite space
  $\mathcal{C}_V \times \mathcal{C}_H$" (Sub:137): a constructed realization, object (β), which needs
  Lemma 1 only. It also uses that "on a fixed finite representative a non-permutation rooted map
  … forces indivisibility somewhere in the recurrence cycle" (Sub:137), a statement about one finite
  bijection over its whole cycle.
- *Stage 2* (Sub:145–169). Step (a) starts from "The coupling graph inherited from Stage 1" and takes
  from A4 that the coupling graph is "a finite periodic lattice" (Sub:98, :157). Step (f) uses
  "reciprocal visible transition counts at every scale" from T-invariance of the bijection (Sub:167).
- *Stage 3* (Sub:177–183). The gap equation of GR §3, conditional on H-slope (Sub:181); its counting
  argument is that of GR:58 and GR:70 (N3.7).

[IR] So the theorem's uses of finiteness are of three kinds: a constructed finite realization per
horizon (carried on `main` without A1); a recurrence-cycle statement (not carried by a fixed-horizon
form, N3.1); and a finite periodic lattice with transition counts and shell counting (statements about
the carrier itself). Lemma PM bears only on the first, which needs no help. The class is not carried
as a whole; what the untraced SM theorems use is undetermined. BORDERLINE.

### N3.9 §4.6

The round trip of Main:752 stays in `Σ_loc(V)` by the cone, which Lemma PM carries. Main:758 lists
"finiteness of $S$" and gives scope (ii)'s reason, "modulus-one spectrum" of the exact Koopman operator of a
finite permutation, specific to finite carriers. Under the invariant uniform product prior every finite
region's marginal is exactly uniform (ensemble local equilibrium); canonical typicality as Main:756 uses
it concerns typical individual states, and its infinite-carrier analogue is not on `main`. CONFIRMING.

### N3.10 The remaining Main:60 consumers

- *The finite hidden space of the §3.2 setup* (Main:266, "$\mathcal{C}_H$ under the total-finiteness
  posit"). At a fixed horizon, N1.7 gives the reduced channels on an infinite carrier from the stage on
  `hatIter(V, n)`; in the native class the torus of N1.8 gives a finite `C_H` with the same channels on
  `[0, n]` [IR, channel form of Lemma PM (c) not written]. The setup's own steps use a bijection of a
  finite product (`U_φ` "permutes the orthonormal basis", Main:270) and `m = |C_H|` in the Kraus form
  (Main:284); neither is defined for the description as given (§P). A chosen closure on the patch
  supplies both for itself on the window, for second-order rules by Lemma C′ (checked by the recheck of r5); these
  statements concern one step, so their requirements are confined to the window and the closure
  could suffice, which is to be determined (§P.4; §4.2). The CPTP property and the Born-form
  identity would have to be re-derived at a fixed horizon [IR]. The displacement `𝒟` of Main:216 ("whose bath-motion
  term is $\mathcal{O}((\tau_S/\tau_B)^2)$") is traced in N3.5 to the estimate of Main:340, which is
  written inside this setup; its form on a patch is not derived. Undetermined.
- *The CP-indivisibility theorem of §3.2* (Main:330). Its proof reduces CP-divisibility to P-divisibility
  for diagonal-preserving channels (Main:332); the reduction is a fixed-horizon step. Its input, the
  P-indivisibility of §2.3, is recurrence-scale (N3.1) and is not carried; an in-window visible
  certificate (Main:141–143) would supply it where one exists.
- *The all-time periodicity of a single realization in §3.4* (Main:638). True of every finite autonomous
  realization (N2.3) and kept as mathematics about finite models; for a fixed-horizon realization the
  periodicity lies after its horizon (AW-EF3), so it bears on nature only under the condition of N2.5.
- *The obstructions stated in §3.4 for a fixed finite realization* (Main:60's last consumer clause:
  they "bear on nature through it"; added in r5, finding 4 of the review of r4). Traced at Main:486
  and Main:558, with Main:480–484, :556 and :562. Main:486: "A fixed finite $S$ with a fixed prior
  and a fixed bijection supports only finitely many distinct action-labelled conditional families,
  whereas the instrument space of any non-trivial system is a continuum"; in the setting of the
  theorem at Main:480 the instruments are bijections of `S`, so the count is a count of maps of a
  finite set [IR]. Main:558: "Fix one realization: a substratum of $N < \infty$ ontic
  configurations with its observation map"; every behaviour then factors through `N` states, while
  qubit behaviours have unbounded nonnegative rank, "the elementary factorization half proved here,
  the unboundedness imported"; the obstruction "is independent of C1–C4 and of horizon growth" and
  "does not touch the equivalence theorem — there the realization is chosen per finite-horizon
  law". As mathematics about one fixed finite realization neither proposition uses A1. Their
  bearing on nature needs one finite model that serves *every* experiment: A1 through Main:60, or
  an F-one statement with inputs (N2.1 form (ii), whose machine likewise admits finitely many
  transition maps). A fixed-horizon description is made per horizon and per protocol and may grow
  with the experiment, so through F-each these propositions currently establish no justified
  constraint on observations. Not carried by F-each.

### N3.11 A1-test candidates (audit §11)

- *Candidate 1* (one finite carrier: qubit obstruction, finitely many conditional families, finite
  predictive dimension). Its all-time form is N2.5's condition, which no finite-horizon datum decides
  (N2.6). At a fixed horizon, `N_eff(n) = |C_{U_n}|` states suffice for every horizon-`n` behaviour
  [IR], a weak bound. The finite-predictive-dimension clause is H-mem's content (§5).
- *Candidate 2* (corner occupancy): in the native class its finite-versus-infinite alternative
  currently establishes no justified constraint on observations over a fixed horizon (N3.5).
- *Candidate 3* (double stochasticity): holds on infinite carriers of the second-order class (N3.2)
  and, given (M-full), checked by the review of r4, on infinite carriers of the class of bijections
  with both locality clauses and finite alphabets at every site; in both cases conditional on a
  uniform product prior. It does not hold for B1, a bijection with finite reading sets in which some
  site is read by infinitely many sites (§P). So it tests the locality class and the prior, not the
  cardinality.

None becomes a test of A1 through a fixed-horizon form. ELABORATING.

## 4. The owner's required check

Adopted direction (c.6896252651): "One particularly important check: is effective finiteness justified
independently of A1, and is it sufficient for the specific results it is meant to recover?" On its
standing (c.6896940222): "keep effective finiteness as a candidate replacement premise, but give it
no recovery credit until each theorem's actual requirements are checked." And (c.6897254631): "if
the required conditions are already established, per-horizon finiteness is a derived lemma, not a
new assumption. "Candidate replacement" describes its possible role in proofs that currently use
A1."

### 4.0 What kind of object fixed-horizon finiteness is (OP)

F-each is a **derived lemma**: Lemma PM (N1.3), and Lemma PM-I (N1.5) for experiments with
interventions. It is derived from the premises of group A below; where those are established it adds
no assumption. **Candidate replacement** describes only its possible role in a given proof that
currently uses A1; whether it can play that role is decided proof by proof (§4.2). The premises fall
into three groups, as the adopted direction separates them (c.6897254631): "finite dependency sets and finite
alphabets establish the finite observational description. A normalized starting law supplies
probabilities on that description; it is not needed merely to establish finiteness. Any stronger
distributional properties require their own justification."

**Organization by claim (O19).** Adopted direction (c.6897946443): "The useful simplification is to stop
treating every condition as a requirement for every result". The conditions are therefore listed
under the claim that needs them, in the order of the owner's table: claim 1, a finite description
for a fixed observation window (group A); claim 2, probabilities for that description (group B);
claim 3, uniformity, invariance or measurement independence (group C); claim 4, a finite closed
model reproducing the window; claim 5, recovery of a particular A1 result; claim 6, one finite
model valid for all time. A condition listed under one claim is not a condition of another unless
that claim's entry names it. The status of each claim is in the table "Organized by claim" of the
status section.

**Claim 1: a finite description for a fixed observation window. Group A, the finiteness and
dependency premises (deterministic; no probability).**

| # | Premise | On `main`? (file:line) |
|---|---|---|
| F1 | Site factorization: the configuration space is a product over sites | On `main`: ledger item (viii), Main:724; a posit |
| F2 | One deterministic, time-independent update | On `main`: determinism clause of Lemma 3, Main:54; iteration of a single map, Main:44 |
| F3 | Finite reading sets (P-dep): each site's next value depends on finitely many sites | On `main` for the selected model: clause of (xiii), Main:724 (a posit of the selected model; its listed role would widen); kernel `leapFiniteRange` (`SecondOrderDrive.lean:306`). On `main` as a hypothesis of GR:132's infinite case ("each component's update depends on finitely many components"). **Flagged** off the selected model: Main:362 obtains it from the finite site set, and on an infinite carrier it does not follow (N1.2) |
| F4 | A finite visible region with a site-local readout (P-V) | Used on `main` for the spatial results (Main:296; Main:744–746; GR:112); not stated as a separate premise, and finite there only through the finite site set. **Flagged.** Lemma 1 (Main:46) gives `\|C_V\| < ∞`, which is not this |
| F5 | Finite site alphabets on the patch (P-fin) | On `main` for the selected model: (xiii) ("a finite abelian group"), Main:724. Off the selected model its only source is the setup of Main:362 ("with $V$ and each $S_i$ finite"), where it is stated together with the finite site set; Lemma 1 (Main:46) gives a finite visible configuration space only. **Flagged** off the selected model: the local half of total finiteness, kept as a premise |
| F6 | With settings, inputs or policies: one protocol shared by the runs compared (the same settings, or the same policy with the information it uses) | On `main` for one setting step: the Bell theorem conditions on the settings (Main:366–374). **Flagged** for adaptive spatial policies, which `main` does not treat |
| F7 | With settings, inputs or policies: finite supports. For one patch over every branch: FS-all (N1.5), or, by the alternative route of Lemma K, finite reads on every run, under the lemma's other hypotheses (a finite alphabet at every site; finitely many values of the policy information). For a single run: run-wise finite reads | Not on `main` as a separate premise, in either form; automatic there from the finite site set of Main:362. **Flagged** (N1.5). No class of §4.2 uses the route of Lemma K |

*What group A gives, and which premise each statement needs.*

- **Matching patch data, under the same settings or the same policy with its information, give
  matching observation histories:** F1, F2, F3, F4, and F6 where interventions are present. F5 and
  F7 are not used.
- **The patch is a finite set of sites:** F3 and F4; with interventions, F7 in its all-branch form
  (FS-all, or the hypotheses of Lemma K).
- **There are finitely many patch data (the finite observational description):** F5 in addition.

Without A1, the premises of group A that are not established on `main` in the generality needed are
F3 and F5 off the selected model, F4, F6 for adaptive policies, and F7. Fixed-horizon finiteness is a
derived lemma exactly to the extent that these are established.

**Claim 2: probabilities for that description. Group B, the probability premise.**

| # | Premise | On `main`? |
|---|---|---|
| P1 | A normalized starting law on the carrier, with the measurability condition of Lemma PM (b) | For a finite carrier the counting measure supplies it (Main:54, :58), and Main:58 makes the prior "part of the realization datum". For an infinite carrier it appears on `main` only as a hypothesis (GR:132, "a normalized product prior on it"; Sub:92, "Infinite extensions require specified normalized measures or states"). **Flagged** for the infinite case. It asserts no cardinality |
| P2 | With a policy: the joint law of the patch data and the policy information | Not on `main`. **Flagged** |

*What group B adds:* the law of the `n`-step record is the pushforward of the patch marginal (with a
policy, of the joint law). **It is not a premise of group A:** every statement of group A holds
with no probability at all.

**Claim 3: uniformity, invariance or measurement independence. Group C, the further distributional
properties. None is used by the lemma; each needs its own justification wherever a result uses
it.**

| # | Property | Where this file uses it | On `main`? | Standing |
|---|---|---|---|---|
| D1 | Equal patch marginals in two carriers; product form across the patch boundary | Lemma PM (c), law clause; N1.4; N1.8; the deep-sector row of §4.2 | GR:132, as a hypothesis | A condition of each comparison; needs its own justification |
| D2 | Uniform product prior | N1.8; N2.10 (2)–(3); N3.2; N3.3; N3.5 (EF-G10); §5.2; §P; the baseline row of §4.2 | For a finite carrier: Main:54, :58, :115. For an infinite carrier the uniform family exists as a kernel object (`uniform_family_consistent`, `RegionTower.lean:447`); that nature's prior is this one is of the kind of posit (iv), Main:724 | Needs its own justification |
| D3 | Invariance of the prior under the dynamics | N3.2 (proved for the second-order form); (M-full), §P.3 (proved for a bijection with both locality clauses and finite alphabets at every site; checked by the review of r4); N2.3 (3) (hypothetical) | Finite carrier: the preimage count of Main:60 and Main:274. Infinite carrier: not on `main` | Derived where proved, as a property of the full system and conditional on D2. (M-full) has one independent check; the owner's condition on its use stands, and it supports no recovery classification here |
| D4 | Independence of the visible initial state from the hidden data (`P_0 ⊗ μ_H`) | N1.4; N3.2 (double stochasticity); §P.2 (rooted maps); the baseline and readback rows of §4.2 | A hypothesis of the theorems that use it: Main:516, Main:135 | Needs its own justification |
| D5 | Stationarity of the observation law | N2.3 (4); §5.4; §P | Not assumed on `main` | Follows from D2 with D3; otherwise needs its own justification |
| D6 | Independence of the settings from the response-relevant data (measurement independence) | N3.6 | Ledger item (xiv), Main:724; hypothesis (iv), Main:372–374: a posit, not derived | A separate premise, tracked |
| D7 | Independence of the policy information from the patch data | Lemma PM-I (c) | Not on `main` | Not assumed here: the joint law is used |
| D8 | A prior selected among invariant measures (maximal entropy; an energy shell) | N3.3; N3.7; the Lemma 3 and energy-shell rows of §4.2 | Posit (iv), Main:724; Main:54; GR:58 | Not inherited automatically by the description, which as given has no self-map and so no set of invariant measures; whether a suitable finite closed model exists is a separate question (§P.4; Lemma C, checked by the recheck of r5). Needs its own justification on the full system |

Not among the premises of the lemma, and not obtained from it: A1, bijectivity, an invariant measure,
a product prior, a uniform degree bound, recurrence, measurement independence. What the lemma
delivers: a finite set of patch data that determines the record on `[0, n]`; and, given P1, the
observation law on `[0, n]` as the pushforward of a probability on that finite set. What it does not
deliver is listed in §P.

**Claim 4: a finite closed model reproducing the window.** Adopted direction (c.6897946443): "The closure theorem's
conditions, once independently checked". They have had one independent check, by the recheck of r5 (Lemmas C and C′,
§P.4).

| # | Condition | For what | On `main`? |
|---|---|---|---|
| C1 | Claim 1's conditions for the autonomous case, F1–F5 | A closure of the patch data at all: the fixed-boundary closure reproduces the window (§P.4 (b1), checked by the review of r4) | As in group A |
| C2 | Under the uniform measure on the patch data, the law of `X_{1:n}` equals that of `X_{0:n−1}` (the window law is shift-stationary) | A closure that is a bijection preserving that measure: exactly when C2 holds (Lemma C, checked by the recheck of r5) | Not on `main`. It follows from D2 with D3 (Corollary C1, checked by the recheck of r5) |
| C3 | The second-order form of the update | Every fixed-boundary closure is such a bijection (Lemma C′, checked by the recheck of r5) | Main:724 (xiii), a posit of the selected model |
| C4 | A uniform product starting law (D2) | The measure the closure preserves is the description's probability | **Flagged** for an infinite carrier (group C) |
| — | A finite visible alphabet and a finite horizon | A constructed finite realization on another carrier, with a structured prior (β) | Main:46 (Lemma 1); Main:516–520 |

A closure is a chosen model, not a premise. It is valid on the window only (§P.4).

**Claim 5: recovery of a particular A1 result.** Adopted direction (c.6897946443): "Only the properties that result's proof
actually uses". They are listed per class in §4.2, from a trace of each proof, with their lines on
`main`. No condition is taken from a summary, and none is removed here.

**Claim 6: one finite model valid for all time.** Adopted direction (c.6897946443): "A separate all-horizon argument". None
is given for nature. The conditional statements are in N2.1–N2.6: the complete relevant state
finite with its evolution determined by it (form (i)); finitely many influencing sites with inputs
kept external (form (ii), a model with inputs); under N2.3's conditions, pathwise eventual
periodicity of the visible law with uniform bounds. None of these hypotheses is on `main` for
nature without A1: **flagged**. Claims 1–5 do not supply this claim (O5).

### 4.1 Justification, per form

| Form | Label | Justified without A1? | Inputs; support layer |
|---|---|---|---|
| Finite patch description, autonomous, deterministic form (Lemma PM (a), (c)) | F-each | A derived lemma on F1–F5; of these F3 and F5 (off the selected model) and F4 are flagged on `main` | Kernel core for a single readout time, paper [IR] for assembly and rules; re-derived by the review of r2 |
| The same with probabilities (Lemma PM (b)) | F-each | Adds P1, flagged for an infinite carrier | Paper [IR]; re-derived by the review of r2 |
| Finite patch description with interventions, all-branch form (Lemma PM-I (a), (b), (c)) | F-each | A derived lemma on F1–F7 with FS-all, and P1–P2 for the law; F6 (adaptive) and F7 are flagged | Paper [IR]; no kernel form; re-derived by the review of r3; the memory clause is r4's, checked by the review of r4 |
| Per-run form (Lemma PM-I (a′)); Lemma K | per run; F-each from finite reads on every run, under the lemma's other hypotheses | Conditional on hypotheses that are not premises on `main`: run-wise finite reads on the given run for (a′); for Lemma K, finite reads on every run, a finite alphabet at every site and finitely many values of the policy information | Paper [IR]; checked by the review of r4 |
| Fixed-horizon realization `E2(n)` | F-each | Yes (on `main`) | Lemma 1 only; kernel `S_imp_D` |
| Finite syntactic cone (`U_∞` finite) | F-one, under an assumption | No: an assumption (A1 on `U_∞`) | Sufficient for one finite autonomous model (N2.1); not necessary (X2) |
| Finite relevant complete state, evolution determined by it (form (i)); in particular `J_∞` finite with no outside controller | F-one, under an assumption | No: an assumption about nature that nothing here supports; fails on an infinite lattice of the linear nearest-neighbour class under (LE) (N2.10) | Sufficient (N2.1 (i)); with finite alphabets also necessary for a model of the record from every initial configuration (Proposition N, checked by the review of r4); for one fixed law, not necessary in general (X3, a point mass) and necessary when the law charges every cylinder (reviewer's refinement, checked by the recheck of r5) |
| Finite influence set with external inputs (form (ii)) | F-one for a model *with inputs*, under an assumption | No: an assumption | One finite transducer; no periodicity (N2.1 (ii)) |
| One finite autonomous model, every horizon | F-one | Not established here; under N2.3's conditions equivalent to pathwise (eventual) periodicity, which no finite-horizon datum decides | N2.4–N2.6 [IR, proof here] |
| Finite hidden memory (H-mem) | a bound `d` for every horizon | No: a hypothesis | §5 |

### 4.2 Sufficiency, per result class

**Substantially revised in r4 (O14); the cells changed or added in r5 are awaiting check.** In r3
the column "properties the proof uses" was read from cited lines; the review of r3 traced eight
classes and found entries missing in seven. In r4 every class was redone from a trace of its proof
on `main`, at the lines given; the class-by-class list of what changed then is in the response
section. The review of r4 retraced seventeen classes and agreed with the columns except in two
rows, readback and one-step coherence, where requirements were missing, and for one consumer class
of Main:60 that had no row, the §3.4 obstructions for a fixed finite realization. r5 completes the
two rows, adds the row, rewrites the measure column in the terms of §P.4, and adds a second table
with the window-confinement entry (O17) and the direct-proof target (O19) for each class.

Columns. *Properties the proof uses*: from the trace. *Form*: the weakest form that looks
sufficient, unchecked: **F-each**, **F-one**, **carrier finite** (a statement about the carrier
itself, which neither form supplies; X2 has a finite model of its observations at every horizon and
an infinite carrier), **mixed** or **undetermined**. *Carried?*: whether the fixed-horizon
description (α) of §P carries each property. *Measure; PM-I form*: whether the proof needs a measure
on the description, in the sense of §P.4, and which form of Lemma PM-I it needs where interventions
enter. Two things are told apart there: the description as given, which has no self-map of its own
(M-desc-own), and a chosen closure on the patch that reproduces the window (M-desc-some). A cell
that says a proof **needs a property of nature's own map** (its order or return, its cycles, its
eventual image, its spectrum, its invariant measures, its shells) names a requirement outside the
window: the description does not inherit it automatically, and a window-valid closure cannot
supply it, because what the closure has of it is the closure's own (N3.1). That is not a statement
that no finite closed model has the property. The form assignment and the last three columns are
[IR].

**Every class: no recovery credit until its theorem's requirements are checked.** No class cites
(M-full), Lemma C or Lemma C′ as support.

| Result class (site) | Properties the proof uses, from a trace (file:line) | Form | Carried by the fixed-horizon description (α)? | Measure on the description; PM-I form | Recovery |
|---|---|---|---|---|---|
| Finite-horizon S⟺D⟺Q_fb and the process dilation (Main:516–522, :546–552) | Finite `C_V`, `n ≥ 2`, finite horizon `K` (Main:516, :546). Rational kernels at positive-probability histories, or the response-table form for arbitrary kernels (Main:516, :518). A *constructed* finite `C_H`: ledger, tape, clock (Main:520). The step is injective by the ledger, and "extends to a bijection of the finite product, since an injective map … from a subset … of a finite set … extends to a permutation" (Main:520). A structured prior `μ_H` independent of the visible initial state (Main:516, :522); that independence "is not formalized" (Main:520). D ⟹ Q_fb: a permutation unitary preserves diagonality (Main:552). Q_fb ⟹ S: the Born rule (Main:552) | F-each | Nothing to transfer: already fixed-horizon statements from Lemma 1 ("a finite hidden space is constructed, not assumed", Main:60) | A constructed prior on a constructed carrier; none on (α). No interventions | No recovery credit until its theorem's requirements are checked; none is needed (A1-free on `main`) |
| Hidden-memory theorem, capacity floor, canonical quotient (Main:506–512, :602–620) | A faithful realization: a bijection of `C_V × C_H` with a joint initial law (Main:602). Determinism: `X_{t+1}` is a function of `(X_t, H_t)` (Main:610, :508). Data processing; `H(H_t) ≤ log₂\|C_H\|` for the realization's finite `C_H` (Main:610, :510). The vanishing criterion for conditional mutual information, "not formalized" (Main:97). For non-injective and staged completions the step is "proved on paper" (Main:614). Quotient: determinism, the shift, positive-probability tails (Main:620) | F-each | Nothing to transfer: statements about every finite faithful realization at a horizon | None on (α). No interventions | No recovery credit until its theorem's requirements are checked; none is needed (A1-free on `main`) |
| §3.3 coupling-graph causal cone (Main:362) | A product `S = ∏_{i∈V} S_i` "with $V$ and each $S_i$ finite". The graph of actual one-step dependence, "symmetrized for the spatial graph". Induction on `k`. An intervention "that reads and writes only region $A$". "Finiteness of $V$ is used in the first step, where insensitivity to each single component outside the dependency set makes the $i$th output a function of the components in it" | F-each | Induction and cone: yes (Lemma PM). The first step: no, it fails on an infinite carrier (N1.2); finite reading sets become a stated hypothesis (F3). The intervention clause: yes for an intervention with a support valid in every state | No measure: the statement is pointwise. PM-I: one intervention with a declared support (all-branch, single step) | No recovery credit until its theorem's requirements are checked. Recovery candidate |
| Bell ceiling (Main:364–389) | `Ω` "fixes each wing's response to every setting" (Main:364–365). (i) determinism. (ii) a product setting operation on disjoint regions at one step, "each intervention reading and writing only its own region" (Main:366–369). (iii) a `±1` outcome from the state on `R_A`, `k_A` updates later, with `d(B, R_A) > k_A`, and symmetrically (Main:369–372). (iv) one common pre-setting ensemble, `p(Ω\|a,b) = p(Ω)` (Main:372–374). "the protocol records a $\pm1$ outcome in every run" (Main:374–375). Proof: the post-setting state outside `B` does not depend on `b`; the cone lemma; point-mass conditionals from determinism; "the common ensemble supplies measurement independence" (Main:383–388); a pointwise bound over the sixteen response tables, then the average (Main:388–389) | F-each (given duration) | Determinism, cone: yes. A finite `Ω_n` on `W_A ∪ W_B ∪ A ∪ B` that fixes the response to every setting: yes, with `A`, `B`, `R_A`, `R_B` finite as a premise. An outcome in every run: a condition on the protocol, untouched. This is **dependency coverage only**. (iv), measurement independence: **not supplied**; ledger (xiv), Main:724, a posit | A probability `p(Ω_n)` on the patch data (P1) and measurement independence (D6); no invariant measure. PM-I: **all-branch** (a law over outcomes and a comparison across settings) | No recovery credit until its theorem's requirements are checked. Recovery candidate for the dependency part |
| Baseline `T_ij` with uniform hidden prior (Main:115–117, :129; Main:58; Main:266) | Finite `C_V`, `C_H`; a bijection of the product; `T_ij = \|{h : π_V φ(x_i, h) = x_j}\| / \|C_H\|` (Main:115), "under the uniform hidden prior that defines $T$" (Main:129); `T^{(k)}` from `φ^k` (Main:117). The prior is the uniform probability on the product carrier of a bijection, distinct from the counting probability on an eventual image (Main:58, :266). Double stochasticity: the preimage count, each set `{x_j} × C_H` having exactly `\|C_H\|` preimages (Main:60; Main:274) | F-each | The ratio: yes, as a count over `C_{B_n}` under a uniform product prior (D2; uniform marginal, kernel). `\|C_H\|` itself: no (horizon-dependent). Double stochasticity: a property of the record law that needs invariance for the full system (D3) | A uniform patch marginal (D2, a premise). For double stochasticity: invariance on the full system, by N3.2 for the second-order form; (M-full) covers bijections with both locality clauses and is not cited as support. No property of nature's own map beyond the window is needed for `T^{(k)}`, `k ≤ n`. Where a bijective closure is chosen (§P.4), it is a bijection of the finite product `C_V × C_{B_n}` with a uniform hidden state whose counting ratios are these matrices, as a chosen model. No interventions | No recovery credit until its theorem's requirements are checked. Recovery candidate |
| Lemma 3 counting / maximal-entropy selection (Main:54, :58, :60) | A bijection of a finite set; "On each finite cycle … the invariant probability measure is unique and uniform; globally, the counting measure is selected among invariant measures as the maximal-entropy one" (Main:54); "on the orbit of the actual microstate, the uniform measure is the unique $\varphi$-invariant measure" (Main:60) | carrier finite | Not inherited automatically: the description as given has no self-map, cycles or invariant measures of its own; global entropy is infinite on an infinite carrier | **Needs the invariant measures of nature's own map** on a finite set, and its orbits: not inherited automatically by the description; a chosen closure's invariant measures are its own (§P.4). Not supplied by (M-full), Lemma C or Lemma C′. No interventions | No recovery credit until its theorem's requirements are checked. Not carried by either form |
| Bijectivity: eventual image, surjectivity, ledger (iii) margin (Main:60, :724) | A map `f` on a finite set `X`; the eventual image `E = ⋂ f^n(X)`; `f^L = id` on `E`. Injectivity in two prongs: record preservation for registered content; for hidden differences, a visible merge "breaks the double stochasticity of the marginalized process" under the uniform prior, or the merge is removable on `E`. "On a finite set, injectivity implies surjectivity". The measure on `E` is the counting measure on `E`, which "need not reproduce the uniform-prior statistics" (all Main:60). "the observed statistics, in the uniform-prior doubly stochastic scope" (Main:724) | carrier finite | Not inherited automatically: not defined for the description as given (B2). Doubly stochastic statistics hold on the second-order class under a uniform product prior (N3.2); they do not follow for a bijection with finite reading sets in which some site is read by infinitely many sites (B1) | **Needs nature's own map on a finite set**, with its eventual image and the step from injective to surjective: not inherited automatically by the description; a chosen closure is bijective by choice or by the form of the rule, which says nothing about nature's map (§P.4). Not supplied by (M-full), Lemma C or Lemma C′. No interventions | No recovery credit until its theorem's requirements are checked. Not carried by either form |
| Recurrence-scale P-indivisibility, counting form (Main:113–129) | Finite `C_V` with `\|C_V\| ≥ 2`, finite `C_H`, a bijection (Main:113). `T` defined by counting over `C_H` (Main:115), the uniform hidden prior (Main:129). P-divisibility implies total-variation monotonicity, used in that direction only (Main:119). "$\varphi$ bijective on a finite set $\Rightarrow$ $\exists N: \varphi^N = \text{id}$. Thus $T^{(N)} = I$" (Main:121). A non-permutation `T` contracts strictly (Main:123–125) | F-one, with a counting prior | Strict contraction at one step: yes (law on `[0, 1]`). The return `T^{(N)} = I`: no (B3; N3.1). The all-horizon model (δ) does not supply the counting prior (§P.5) | **Needs the return `φ^N = id` of nature's own bijection**, with its counting measure: not inherited automatically by the description, and the return of a window-faithful closure is its own, outside the window (N3.1). Not supplied by (M-full), Lemma C or Lemma C′. No interventions | No recovery credit until its theorem's requirements are checked. Not carried by F-each; stays mathematics about finite models |
| History readback with finite recurrence; overlap and return (Main:131–143) | The stochastic-inverse lemma for a finite square stochastic matrix (Main:131–133). A bijection of order `L`; a hidden prior "shared by every root"; rooted maps for every root, "roots of visible probability zero included"; root and hidden state drawn "independently" (Main:135). The hypothesis: two positive-probability visible trajectories `(x_0, …, x_k) ≠ (x'_0, …, x'_k)` with `x_k = x'_k`, "in particular if a (C4) gap (§1.3) holds at order $k$"; the conclusion's range `1 ≤ s ≤ min(k, L−1)` (Main:135). `Γ_L = I`, `Γ_{t+L} = Γ_t`; "every row is kept" (Main:137). Three steps "are proved on paper": from two such histories to a non-permutation rooted map, from a non-permutation square stochastic matrix to two distinct rows sharing positive mass, and `Γ_L = I` (Main:137). Overlap and return: `Γ_n = I` for some `n`, two roots sharing mass at some `s < n`, any shared prior, "not required to have full support"; total variation does not increase under right multiplication by a stochastic matrix (Main:141–143) | Return at the order `L`: F-one. Overlap and return with a return inside the window: F-each | `Γ_k` for `k ≤ n`, as functionals of the law under `P_0 ⊗ μ_H` (D4): yes. The hypothesis, two positive-probability histories with a common endpoint at an order `k ≤ n`: yes, a property of the law on the window. `Γ_L = I`: only if it occurs inside the window. (δ): N2.5's realization supplies a shared prior when the law is pathwise periodic | A prior shared by every root and independent of the root (D4); no invariant measure for overlap and return. The order `L` **needs the order of nature's own bijection**: not inherited automatically by the description, and the order of a window-faithful closure is its own (N3.1). No interventions | No recovery credit until its theorem's requirements are checked. The in-window certificate is a recovery candidate; the recurrence-scale statement is not carried by F-each |
| §3.2 CP-indivisibility (Main:326–332) | Diagonal preservation for `Φ_t(ρ) = Tr_H[U^t(ρ ⊗ μ_H)U^{−t}]` "with $U$ a permutation unitary" (Main:326–328). The P-indivisibility of §2.3 as input (Main:330). `M_kj = ⟨j\|Λ(\|k⟩⟨k\|)\|j⟩` stochastic by positivity and trace preservation; `Φ_{t_1}(\|i⟩⟨i\|) = Σ_k T_ik(t_1)\|k⟩⟨k\|` (Main:332) | F-one (its input) | The reduction: a fixed-horizon step, given the channels. The input: no (two rows above). The permutation unitary: not defined on (α) | The reduction uses a permutation unitary of a finite carrier: not defined for the description as given; a chosen closure supplies one for itself on the window (§P.4). Its input **needs the return of nature's own bijection** (two rows above). Not supplied by (M-full), Lemma C or Lemma C′. No interventions | No recovery credit until its theorem's requirements are checked. Not carried by F-each |
| §3.2 finite hidden space, channel, Born form, reverse direction (Main:266–288) | Finite `C_H = {h_1, …, h_m}`; the uniform prior on the product carrier of a bijection (Main:266). "Since $\varphi$ is a bijection, $U_\varphi$ permutes the orthonormal basis, hence is unitary" (Main:270). `ρ_H = I_m/m` (Main:280). CPTP by a standard result; Kraus operators with `m^{−1/2}` (Main:284). "$U_\varphi$ is a permutation" (Main:288). Reverse direction: "a uniform-prior bijection marginal preserves the uniform distribution and is therefore doubly stochastic"; Birkhoff–von Neumann; rational entries (Main:274–276) | undetermined | `U_φ` and `m`: not defined on (α). A reduced channel exists through the stage formula (N1.7), by steps not written out here | Needs a bijection of a finite product with its uniform hidden state, for one step. Not defined for the description as given. A window-faithful closure, where one is chosen (for second-order rules every fixed-boundary closure, Lemma C′, checked by the recheck of r5), supplies both on `[0, n]` as a chosen model. The populations, `T^{(k)}` for `k ≤ n`, are fixed by the window law; the action on off-diagonal inputs counts coincidences of hidden states reached from two roots, is not a functional of the record law, and depends on the closure (§P.4). (M-full) alone gives neither. No interventions | No recovery credit until its theorem's requirements are checked. Undetermined |
| §3.2 one-step coherence results (Main:292–324) | The channel is that of the §3.2 setup: a finite `C_H`, `ρ_H = I_m/m` and the partial trace (Main:280–282). The displayed `q = 2` update on a lattice; "the visible sector being the sites of a region" (Main:294–296). The boundary factorization from nearest-neighbour support (Main:298–302). The normal form: an invertible visible block, linearity over `F_2`, "the hidden input uniform" (Main:304–310). Witt extension and Clifford implementation (Main:314). "the hidden sector initially uncorrelated and maximally mixed" (Main:316). The criterion carries no dependence on `\|H\|`, "since the coupling reads only the boundary" (Main:322). Abelianness of the Weyl family is the condition `C A^{−1} B = 0`, "which holds identically for this update" (Main:310 (iv)); for a general linear bijection it "can fail" (Main:324). Lemma 2, the theorem and both corollaries "are stated for $q = 2$"; the arguments "carry over to prime $q$", and composite `q` "is not covered" (Main:324) | F-each (one step), unchecked | Not checked. The statement concerns one step and reads only the boundary; that the infinite lattice's one-step channel equals the boundary patch's is the channel form of Lemma PM (c), not written out | A uniform prior on the hidden boundary sites (D2), uncorrelated with the visible input (D4); no invariant measure. Through Main:280–282 the channel is defined with a finite `C_H` and a permutation unitary; its form with a patch or a chosen closure in place of `C_H` is the unwritten channel step. No interventions | No recovery credit until its theorem's requirements are checked. Not examined before r4 |
| §3.4 all-time periodicity of a single realization (Main:638) | "a bijection on a finite set has finite order $L$, so any fixed realization with a fixed prior has an exactly $L$-periodic multi-time law" (Main:638) | F-one | No (B3). True of every finite autonomous realization; bears on nature only under N2.5's condition. (δ) carries record periodicity under its own hypothesis | **Needs the order `L` of nature's own bijection**: not inherited automatically by the description, and the order of a window-faithful closure is its own (N3.1). No interventions | No recovery credit until its theorem's requirements are checked. Not carried by F-each; stays mathematics about finite models |
| §3.4 obstructions for a fixed finite realization (Main:60; Main:486; Main:558; with Main:480–484, :556, :562). Row added in r5 | Main:60: "the obstructions stated in §3.4 for a fixed finite realization bear on nature through it", the finite representative. Main:486: "A fixed finite $S$ with a fixed prior and a fixed bijection supports only finitely many distinct action-labelled conditional families, whereas the instrument space of any non-trivial system is a continuum"; in the setting of the theorem at Main:480 the instruments are bijections of `S` ("permutation instruments", Main:484), so the count is a count of maps of a finite set [IR]; the continuum of instruments is stated without proof; "no fixed finite realization carries the whole instrument algebra". Main:558: "Fix one realization: a substratum of $N < \infty$ ontic configurations with its observation map"; the factorization of every behaviour through the `N` ontic states, under "the ordinary preparation $\to$ finite ontic system $\to$ measurement" interface; "the elementary factorization half proved here, the unboundedness imported" (unbounded nonnegative rank of qubit behaviours, [55]); "independent of C1–C4 and of horizon growth"; "It does not touch the equivalence theorem — there the realization is chosen per finite-horizon law". Main:556, :562: fixed finite families and bounded intervention families are realized; "What no fixed finite carrier can do is reproduce the entire exact continuum operational theory of even a qubit" (Main:562) | F-one, in the form of one fixed finite model serving every experiment (every instrument set; every prepare-and-measure set) | No. A fixed-horizon description is made per horizon and per protocol and may grow with the experiment; it is not one fixed realization, so the propositions do not apply to it. As mathematics about one finite realization they need nothing from (α) and no A1. Their bearing on nature needs one finite model for every experiment: A1 through Main:60, or an F-one statement with inputs (N2.1 form (ii)). Through F-each they currently establish no justified constraint on observations | A fixed prior on a fixed finite carrier (Main:486); preparations as distributions over `N` ontic states (Main:558); no invariant measure. Interventions: bijections of the whole carrier (Main:480–486); in a spatial reading the all-branch form and, beyond it, one model for every instrument set, which no form of Lemma PM-I supplies | No recovery credit until its theorem's requirements are checked. Not carried by F-each; stays mathematics about finite models |
| Corner occupancy (Main:216, with Main:340 and Main:272) | Doukas's bound, imported: "marginalization over a *finite* environment produces no first-order dissipative term, secular leakage requiring an infinite reservoir" (Main:216). "the second-order estimate of §3.2" (Main:216), which is Main:340: a chosen continuous interpolation (Main:272); a generator exactly Hamiltonian at `t = 0`; a bath state moving at rate `1/τ_B`; a bounded coupling `V_int`; the slow-bath condition `τ_S ≪ τ_B` and the weak-coupling condition `‖V_int‖ τ_S ≪ 1`; the §3.2 setup with `ρ_H = I_m/m`. "conditional on the total-finiteness posit" (Main:216) | mixed: the cardinality clause is not a fixed-horizon statement in the native class (N3.5); the estimate of Main:340: undetermined | Not checked whether the estimate holds with a horizon-dependent patch in place of the finite hidden space. In the native class the finite-versus-infinite alternative currently establishes no justified constraint on observations over a fixed horizon (N3.5) | Through the §3.2 setup: as that row. No interventions | No recovery credit until its theorem's requirements are checked. Undetermined |
| Deep-sector gauge (Main:60; GR:112, :124–126, :132) | Main:60: a finite factor with its own permutation, product dynamics, prepared independently in a normalized state; the visible coordinate does not depend on the added coordinate, and the added prior has total mass one. GR:112 (a): a bijective update on a finite product of site spaces, the causal cone, a uniform hidden prior; the proof uses the cone and the uniform prior only (GR:124). GR:112 (b): injectivity of `φ` and H-BD (GR:126). GR:132, infinite case: "a normalized product prior on it, a locally finite coupling graph and well-defined dynamics … in which each component's update depends on finitely many components" | F-each | Yes for the comparison (a), given equal patch marginals (Lemma PM (c)); bijectivity is not used by (a). Part (b) uses injectivity and a posited bound, and is not a patch statement | Equal patch marginals (D1), a condition of the comparison; no invariant measure. No interventions | No recovery credit until its theorem's requirements are checked. Recovery candidate for (a); placement per N1.6 |
| GR:58, :68–70 energy shells | "the finite total system" on "a conserved energy shell"; visible configuration `i` with energy `e_i`; "If the boundary interaction is negligible at the shell scale, uniform counting gives" `P(i) ∝ Ω_H(E − e_i)`; the named hypothesis H-count (GR:58). A time-reversal involution with time-reversal-even coarse states (GR:68). "time-reversal invariance gives a bijection between $i\to j$ and $j\to i$ trajectories, so $N_{ij}=N_{ji}$" (GR:70) | carrier finite | No: shells, conserved quantities and trajectory pairing are not defined on the patch; a shell prior is not a product prior | **Needs an invariant shell measure of nature's own bijection** of a finite carrier (D8): not inherited automatically by the description; a chosen closure's conserved quantities and shells, where it has any, are its own. Not supplied by (M-full), which concerns the uniform product measure, nor by Lemma C or Lemma C′. No interventions | No recovery credit until its theorem's requirements are checked. Not carried by either form |
| Substratum Theorem 23 (Sub:123–195) | Stage 1: A1 among the inputs (Sub:123); "a triple $(S, \varphi, V)$ with $S$ finite, $\varphi$ a bijection on $S$" (Sub:125), obtained as a constructed realization from Main's finite-horizon equivalence; "on a fixed finite representative a non-permutation rooted map … forces indivisibility somewhere in the recurrence cycle" (Sub:137). Stage 2 (a): "a finite periodic lattice" from A4 (Sub:98, :157); (f): "reciprocal visible transition counts at every scale" (Sub:167); (b)–(e) cite theorems of the SM paper, not traced. Stage 3: the gap equation under H-slope (Sub:181), with the shell counting of GR:58–70 | mixed: constructed realization F-each; recurrence-cycle clause F-one; periodic lattice, counts and shells carrier finite; the SM theorems undetermined | The constructed realization needs nothing from (α). The other uses: no (rows above) | Through the recurrence and shell rows: **needs the cycle and the shells of nature's own bijection**. No interventions | No recovery credit until its theorem's requirements are checked. Not carried as a whole; partly untraced |
| §4.6 (Main:742–758) | "a finite bijective $(S, \varphi)$" (Main:742). `Σ_loc(V)` reached within `τ_S/Δt` steps; the exact Koopman operator "a permutation operator: unitary, with modulus-one spectrum and exact recurrence"; the compression `𝒦_Σ = P_Σ 𝒰_φ P_Σ`; hypothesis (EM) (Main:744). `V` "of bounded coupling-graph diameter" (Main:746, :758 (i)). The causal cone keeps the round trip in `Σ_loc(V)` for `t ≤ τ_S`; canonical typicality supplies the local-equilibrium state (Main:752). The rate condition `τ_mix ≪ τ_S` (Main:742, :756). The fast-bath erasure lemma "under its uniform-erosion hypothesis" (Main:754). "bounded coupling, finiteness of $S$, the canonical-typicality result [31], and the effective-mixing hypothesis (EM)"; the exact compressions "need not equal $\mathcal{K}_\Sigma^n$" (Main:758) | carrier finite (cone step: F-each) | Cone: yes. Koopman spectrum, exact recurrence: not defined. The compression: its projection needs a reference measure on the full system [IR]. Typicality of individual states: not preserved as stated (ensemble uniformity is) | The Koopman statements **need the spectrum and recurrence of nature's own permutation**: not inherited automatically by the description, and those of a window-faithful closure are its own; an invariant reference measure on the full system for the compression (D2, D3). (M-full) alone does not supply these. No interventions | No recovery credit until its theorem's requirements are checked. Cone step only |
| A1-test candidates 1–3 (audit §11) | Tests proposed by the audit, not theorems on `main`; candidate 1 draws on the propositions of the row for the §3.4 obstructions | 1: F-one; 2: undetermined; 3: F-each | See N3.11 | Candidate 3 is a property of the record law (D2, D3) | No recovery credit until its theorem's requirements are checked. None becomes a test of A1 |
| Main:638 open question (a) | An open question, no proof | F-one | Not applicable | Not applicable | No recovery credit until its theorem's requirements are checked. Candidate answer for existence, without inputs (N2.9); owner question |

**Which form of Lemma PM-I each class needs (O13).** Interventions enter three classes on `main`. The
Bell ceiling needs the all-branch form: it is a law over outcomes and a comparison across settings.
The causal cone's intervention clause is a statement about one intervention with a region that it
reads and writes in every state, which is a declared support, the single-step all-branch form. The
§3.4 obstructions concern action-labelled families whose instruments act on the whole of one fixed
finite carrier; a spatial reading would need the all-branch form and, beyond it, one model for
every instrument set. Every other class is autonomous and uses Lemma PM. No class on `main` is
served by the per-run form alone, and none uses the route of Lemma K.

**Second table: window confinement (O17) and direct-proof target (O19).** The rows are those of
the table above, in the same order; the two entries are given separately because that table is
already six columns wide. Both columns are read from the proof traces of the table above, not
from summaries, and both are [IR].

*Requirements confined to the window?* Adopted direction (O17, c.6897859755): a chosen, window-valid model
"could suffice for a theorem whose requirements are entirely confined to that window. That is what
the proof-requirements check must determine." Values: **yes**, **no**, **mixed** or
**undetermined**, with the reason. A class, or a part of one, whose traced requirements are
entirely confined to the window is marked "closure could suffice; to be determined; no credit
yet"; where the description itself already carries the requirement the cell says so. A class, or
a part, with a requirement outside the window (all-time recurrence, global bijectivity, a property
of the whole system) is marked "closure cannot supply it". The marks concern what a window-valid
model can establish about nature; none says that no finite closed model with the property exists
(O15).

*Direct-proof target.* Adopted direction (O19, c.6897946443): "If a result concerns only a finite experiment,
ask whether we can prove that observable conclusion directly. We need not reconstruct an
autonomous finite universe, global recurrence or a global invariant measure unless the proof
genuinely requires them. A new direct proof could avoid conditions needed by the old proof." The
column says whether the class's content is an observable conclusion about a finite experiment
(**yes**, **no** or **partly**) and, if so, states that conclusion on its own and names which of
claims 1–4 of the status table a direct proof would need. Every entry is **[IR; no proof given;
not a recovery]**: it names a target, and neither proves it nor removes any condition of the
existing proof. Each target is conditional on the claims it names, and those claims are
conditional on their own premises (§4.0).

| Result class | Requirements confined to the window? (reason from the trace; mark) | Direct-proof target [IR; no proof given; not a recovery] |
|---|---|---|
| Finite-horizon S⟺D⟺Q_fb and the process dilation | **Yes.** Every statement is at a finite horizon `K`, and the realization is constructed from the law on `[0, K]` (Main:516–520). No closure is needed: the proofs are A1-free on `main` | **Yes.** Conclusion: every finite-horizon visible law has a finite deterministic bijective realization and a fixed-basis Born-form representation. Already proved on `main` from Lemma 1 and a finite horizon; needs none of claims 1–4 |
| Hidden-memory theorem, capacity floor, canonical quotient | **Yes.** Statements about any finite faithful realization at a horizon (Main:602–620). No closure is needed | **Yes.** Conclusion: the conditional memory visible on a finite horizon bounds from below the hidden size of every faithful finite realization at that horizon. Already on `main` without A1; needs none of claims 1–4 |
| §3.3 coupling-graph causal cone | **Yes.** A statement about `k` updates and one intervention (Main:362). The description itself carries it (Lemma PM, Lemma PM-I); no closure is needed. The open item is a premise, finite reading sets (F3) | **Yes.** Conclusion: an intervention that reads and writes only a region `A` cannot alter, `k` updates later, a readout region at graph distance greater than `k`. A direct proof needs claim 1 only (F1–F3 and a declared support); the dependency statement is the single-step form of Lemma PM-I |
| Bell ceiling | **Yes** for the dependency part: one setting step and `k_A`, `k_B` updates (Main:364–389); the description itself carries it, with finite regions as a premise. Measurement independence is a property of the starting law and the setting generators (claim 3), which neither the description nor a closure supplies | **Yes.** Conclusion: for a deterministic substratum with own-wing setting interventions, readouts outside the other wing's cone, an outcome in every run and measurement independence, the CHSH value is at most 2 in absolute value. A direct proof needs claim 1 (all-branch, single step; finite `A`, `B`, `R_A`, `R_B`), claim 2 (a probability on the patch data) and, from claim 3, measurement independence, a posit on `main`. Not claim 4 |
| Baseline `T_ij` with uniform hidden prior | **Yes** for `T^{(k)}` at a fixed number of steps `k ≤ n`: a ratio of counts at that step and, for double stochasticity, a property of the record law (Main:115–117; Main:60, :274). The absolute size of the hidden space is not a window quantity and is not needed by the ratio. Closure could suffice; to be determined; no credit yet | **Partly.** Conclusion: the `k`-step visible transition probabilities from a given visible state, with hidden data uniform and independent of it, are these ratios, and the matrix is doubly stochastic. A direct proof needs claims 1 and 2 and, from claim 3, uniformity, independence of visible and hidden data, and invariance for the full system (N3.2 for the second-order form). Not claim 4. The definition by counting over a finite hidden space is model-level and is not itself an observable statement |
| Lemma 3 counting / maximal-entropy selection | **No.** The proof uses the cycles of the map, the orbit of the actual microstate and the set of invariant measures (Main:54, :60): all-time properties of the whole system. Closure cannot supply it. [IR] One clause, that the counting measure is the maximal-entropy invariant measure of a bijection of a finite set, is true of every bijective closure and gives the uniform patch measure whichever closure is chosen; whether that could stand in for the selection is a question about a premise (N3.3), not examined here. It could not serve as an independent justification of a uniform starting law: that a bijective closure exists is itself a statement made under the uniform patch measure (Lemma C) | **No.** A selection principle for the starting law, not an observable conclusion about a finite experiment. Its observable consequence is the row above |
| Bijectivity: eventual image, surjectivity, ledger (iii) margin | **No.** The eventual image, `f^L = id` on it, and "On a finite set, injectivity implies surjectivity" (Main:60) are properties of the map on the whole carrier (global bijectivity). Closure cannot supply it. The statistical prong alone, double stochasticity at each step order, is a window statement about the record law | **Partly.** The conclusion, that nature's map is a bijection, is not an observable conclusion about a finite experiment. The statistical prong is: the visible statistics at each step order are doubly stochastic under a uniform prior; that is the target of the baseline row, with the same needs (claims 1–3) |
| Recurrence-scale P-indivisibility, counting form | **No.** The proof uses the return `T^{(N)} = I` at the order `N` of the bijection (Main:121): all-time recurrence. Closure cannot supply it. The one-step contraction (Main:123–125) is a window statement | **No** for the conclusion, which is a statement at the recurrence time `N` (Main:121). Its one-step ingredient belongs to the baseline row |
| History readback with finite recurrence; overlap and return | **Mixed.** Return at the order `L` (Main:135–137): no, all-time recurrence; closure cannot supply it. Overlap and return with `Γ_n = I` for some `n` inside the window (Main:141–143): yes; the rooted maps on the window are functionals of the law, so the description itself carries them, and the matrix form needs no bijection; closure could suffice; to be determined; no credit yet | **Partly.** Conclusion (in-window part): if the rooted visible maps return to the identity at a time `n` inside the window and two roots share mass at an earlier time, the rooted family is not P-divisible on `{0, …, n}`. A direct proof needs claims 1 and 2 and, from claim 3, independence of the root and the hidden data; the matrix form on `main` assumes only a row-stochastic `Γ_s` (Main:143). Not claim 4. The recurrence-scale statement: no ("a global recurrence-cycle result", Main:139) |
| §3.2 CP-indivisibility | **Mixed.** The reduction from CP- to P-divisibility for diagonal-preserving channels (Main:332) concerns the channels on the times considered: yes; closure could suffice; to be determined; no credit yet. Its input, P-indivisibility at the recurrence scale (Main:330): no; closure cannot supply it | **Partly.** Conclusion (in-window part): where the visible process is P-indivisible on a window, by an in-window return, the family of reduced channels on that window is CP-indivisible. A direct proof needs claims 1–3 as in the row above, and a channel family on the window: claim 4 (a finite closed model with a permutation unitary) or the unwritten channel form of N1.7 |
| §3.2 finite hidden space, channel, Born form, reverse direction | **Yes.** Each statement concerns one step: the channel `Φ`, the Born-form identity for `T_ij`, the reverse-direction lemma for a single one-step matrix (Main:266–288). What they use is a bijection of a finite product with a uniform hidden state, which a bijective closure has on the window. Closure could suffice; to be determined; no credit yet. Open within that: the action on off-diagonal inputs depends on the closure (§P.4) | **Partly.** Conclusion: the one-step visible transition probabilities under a uniform hidden prior are the Born-rule probabilities of a channel. The probabilities are observable; the channel is a representation. A direct proof needs claims 1–3 for the probabilities and claim 4, or the channel form of N1.7, to define the channel |
| §3.2 one-step coherence results | **Yes.** One step, and "the coupling reads only the boundary" (Main:322); the channel is the §3.2 channel (Main:280–282). Closure could suffice; to be determined; no credit yet. Open within that, as for the row above: the result concerns the action on off-diagonal inputs, which depends on the closure (§P.4) | **Partly.** Conclusion: for one step of the displayed update over `F_2` (Corollary 1, Main:316; stated for `q = 2`, Main:324), the reduced channel of a region is not entanglement-breaking exactly when `w < κ`, in particular when the smaller boundary is smaller than the region. It is a property of the one-step channel, not of the classical record. A direct proof needs claim 1 (the boundary factorization is a dependency statement), from claim 3 a uniform, uncorrelated starting law on the hidden boundary sites, and claim 4 or the channel form of N1.7 |
| §3.4 all-time periodicity of a single realization | **No.** All-time by its statement (Main:638). Closure cannot supply it: a closure's period is its own | **No.** A statement about all times |
| §3.4 obstructions for a fixed finite realization | **No.** The requirement is one fixed finite realization serving every experiment (Main:486, :558): a property of the whole system across experiments, not of a window. Closure cannot supply it: a closure is chosen per window and per protocol | **No.** Each experiment considered is finite, but the conclusion concerns one fixed model across all of them |
| Corner occupancy | **Mixed.** The estimate of Main:340 is a short-time statement, for times of order `τ_S`, written inside the §3.2 setup: yes as far as traced; closure could suffice; to be determined; no credit yet. The cardinality clause of Main:216 and the imported bound concern the whole hidden sector and long times: no for the clause, closure cannot supply it; the imported bound is untraced, undetermined | **Partly.** Conclusion (the estimate): the short-time form of the reduced visible dynamics given at Main:340. A direct proof needs claim 4 or the channel form of N1.7 for the setup, from claim 3 a uniform hidden state, and conditions outside claims 1–4 (the chosen interpolation, the slow-bath and weak-coupling conditions, a bounded coupling). The cardinality clause: no |
| Deep-sector gauge | **Mixed.** GR:112 (a) and the first statement of GR:132 concern the visible transition data on `[0, nΔt]`: yes; the description itself carries the comparison (Lemma PM (c)); no closure is needed. GR:112 (b) uses injectivity of the whole map and a posited bound (GR:126): no; closure cannot supply it. Main:60's finite-factor statement holds at all times by the product form and needs no window | **Yes** for (a). Conclusion: the visible transition data over `n` steps do not depend on the hidden sector beyond the cone. A direct proof needs claims 1 and 2 and, from claim 3, equal patch marginals in the carriers compared (a product form across the patch boundary). Not claim 4 |
| GR:58, :68–70 energy shells | **No.** A conserved shell of "the finite total system" and a pairing of shell trajectories (GR:58, :70): properties of the whole system. Closure cannot supply it | **Partly.** The conclusions, visible occupation weights and reciprocal transition counts, are statements about visible statistics; their derivation counts over a shell of the whole system. A direct proof would need, from claim 3, a justification of the shell measure, which is not a product law, so claim 1's carrier comparison does not cover it. No target is named beyond that |
| Substratum Theorem 23 | **Mixed.** The constructed realization of Stage 1: yes, and nothing is needed. The recurrence-cycle clause (Sub:137): no. The periodic lattice, transition counts and shell counting (Sub:157, :167, :181): no, properties of the whole carrier. Closure cannot supply these. The SM theorems of Stage 2 (b)–(e): untraced, undetermined | **Undetermined.** Partly untraced; no target is named |
| §4.6 | **Mixed.** The cone step, for `t ≤ τ_S` (Main:752): yes; the description itself carries it. The Koopman spectrum, exact recurrence, "finiteness of $S$" and canonical typicality (Main:744, :756, :758): no, all-time or whole-system properties; closure cannot supply them | **Partly.** Conclusion (cone step): the round trip stays in `Σ_loc(V)` for `t ≤ τ_S`; a direct proof needs claim 1. The spectral and recurrence statements: no |
| A1-test candidates 1–3 | 1: **no** (one carrier for every experiment, or all time). 2: as corner occupancy. 3: **yes**, a one-step matrix, a property of the record law; no closure is needed | 1: no. 2: as corner occupancy. 3: **yes**; the baseline row's target (claims 1–3) |
| Main:638 open question (a) | **No.** All-time by its statement | **No** |

## 5. Finite-hidden-memory draft, H-mem (task d; not adopted)

### 5.1 Statement

**H-mem (draft).** There is `d < ∞` such that, for every accessible horizon `K` and every cut
`0 ≤ t < K`, the matrix `𝐇_t(K)` with rows indexed by positive-probability pasts `x_{0:t}`, columns by
futures `x_{t+1:K}`, and entries `P(x_{0:t}, x_{t+1:K})` has rank at most `d`. [IR, standard] For a
stationary process this is equivalent to a `d`-dimensional quasi-realization with time-independent
operators, `P(x_0, …, x_K) = π τ_{x_0} ⋯ τ_{x_K} σ`; without stationarity the operators depend on time.
The intervention form, **H-mem-int**, asks the same of the action-labelled process.

H-mem bounds the *memory* the visible process uses, not the size of a substratum. A deterministic
substratum reproducing a process that satisfies H-mem still needs a hidden sector growing with the
horizon unless the law is pathwise eventually periodic with uniform bounds (N2.4 (D)).

### 5.2 Relation to the native model [IR]

For the selected linear rule under the uniform product prior (a premise, D2 of §4.0), the visible law on a
window is uniform on a
subgroup `W ⊆ A^P × A^F`. The future given a past is uniform on a coset of `F_0 = {f : (0, f) ∈ W}`,
distinct cosets have disjoint supports, so the Hankel rank is `|π_F(W)|/|F_0|` and
`I(past; future) = log₂(|π_F(W)|/|F_0|)`: **rank = 2^{I(past; future)}** exactly, at each cut, without
stationarity. The past includes the present, so `I* ≤ I(past; future) ≤ I* + log₂|C_V|`, with `I*` the
conditional quantity of `card_hidden_ge_two_pow_Istar`, which bounds `|C_H|` from below by `2^{I*}`.
On the native model H-mem is therefore equivalent to a uniform bound on `I*`. NEW (EF-G7). Whether the
selected rule's visible process satisfies the bound is not known in general; an exact rank computation
over `Z_q` would decide it and is proposed as H-mem's internal control, not run. One case is decided on
paper, for unit axis coefficients: the current values at a single site are i.i.d. (N2.10), so the
current-value process has rank 1 at every cut. The observation at that site is the pair (previous,
current); it is a Markov chain on `Z_q × Z_q`, its rank at every cut is `q` (the future depends on the
past through the current value only), and its conditional memory `M_t` is zero [IR; the rank
statement is the review of r3's]. So a single-site observer on the infinite lattice under the uniform
product prior has no conditional memory (marker AW-EF13). This says nothing for larger visible
regions, where interior sites are driven by visible neighbours.

### 5.3 What it would preserve (controls stated in advance)

- **K1.** `S ⟺ D ⟺ Q_fb` at each horizon (`finite_horizon_equivalence`; Main:546–552): untouched.
- **K2.** The readback lemma and (ii) ⟺ (iii) (Main:536–542, :628): H-mem must admit `M_k > 0`; it does
  for `d ≥ 2` [IR].
- **K3.** The C3 floor (Main:602–612; `card_hidden_ge_two_pow_Istar`): consistent; in the native class
  H-mem is equivalent to bounded `I*` (5.2).
- **K4.** The comb obstruction (Main:486, :496, :556): H-mem-int must restrict physical interventions to
  the subclass one representation can host, Main:496's option (a). A substantive selection claim.
- **K5.** Main:562's requirement that a completion beyond one finite carrier "retains finite predictive
  dimension": H-mem would supply it as a hypothesis.
- **K6 (internal).** The native model's visible process under the uniform product prior must satisfy
  H-mem, or the two are inconsistent (5.2).

It preserves none of the A1-consuming whole-carrier results: an i.i.d. process satisfies H-mem with
`d = 1` and has no recurrence, no periodicity and no finite autonomous deterministic model.

### 5.4 Consequences beyond the A1 problem, and refutation

- **Prediction [IR, standard; stationary case].** Every correlation `C(k) = E[f(X_0) g(X_k)]` satisfies a
  linear recurrence of order at most `d`, so its spectral density is rational in `e^{iω}`: finite sums of
  damped and oscillating exponentials, no exact power-law tail over all lags. This needs stationarity.
  It is a consequence of the hypothesis H-mem, not of the fixed-horizon argument.
- **Postdiction [IR, standard].** A `d_Q`-dimensional quantum system under repeated instruments gives
  Hankel rank at most `d_Q²`, so H-mem holds for every finite-dimensional quantum process. Unlike A1,
  H-mem does not revive the classical-dimension obstruction (Main:558): qubit prepare-and-measure
  behaviours have linear rank at most 4 and unbounded nonnegative rank.
- **Refutation by visible data.** Empirical Hankel ranks that keep growing with horizon and statistics
  (Ho–Kalman singular-value tests), or power-law correlations over many decades of lag, beyond what any
  `d` below a stated bound fits.

### 5.5 Literature (from memory; [IR] throughout, not checked against sources)

Gilbert (1959), *Ann. Math. Statist.* 30:688–697; Dharmadhikari (1963), *Ann. Math. Statist.*
34:1022–1032 and 1033–1041; Heller (1965), *Ann. Math. Statist.* 36:1286–1291; Fox and Rubin (1968),
*Ann. Math. Statist.* 39:938–946; Ho and Kalman (1966), *Regelungstechnik* 14:545–548; Ito, Amari and
Kobayashi (1992), *IEEE Trans. Inf. Theory* 38:324–333; Jaeger (2000), *Neural Computation* 12:1371–1398;
Littman, Sutton and Singh (2002), *NIPS* 14; Singh, James and Rudary (2004), *UAI*; Vidyasagar (2011),
*Math. Control Signals Systems* 23:1–65; Crutchfield and Young (1989), *Phys. Rev. Lett.* 63:105; Shalizi
and Crutchfield (2001), *J. Stat. Phys.* 104:817; Crutchfield and Feldman (2003), *Chaos* 13:25; Fannes,
Nachtergaele and Werner (1992), *Commun. Math. Phys.* 144:443.

### 5.6 §A.29 assessment

Results preserved: K1–K6. Independent prediction: the rational spectrum (5.4, stationary case) and the
native-model constraint (5.2). Hard to vary: **no, in the free-`d` form**, since every finite-horizon law
has finite rank and any finite data set is fitted by a large enough `d`. It would become hard to vary
only with `d` set by an independent argument; none is on `main`, and the analogy `d ≤ n_V²` gives an
astronomically large bound for `|C_V| ∼ 10^{183}` (Main:222). Status: recorded draft, not proposed.

## 6. Findings

- **EF-G1 (NEW).** The observation law on `[0, n]` depends on the initial law only through its marginal on
  the finite patch `U_n`, for every normalized prior; product structure across the patch boundary is a
  condition of carrier comparisons only (N1.4).
- **EF-G2 (NEW) [IR, proof here].** Under autonomy, determinism, finiteness and no inputs, one finite model
  valid at every horizon (or a family of bounded size) exists exactly when the visible law is pathwise
  eventually periodic with uniform bounds; pathwise periodic with a uniform period for bijective models,
  with one shared prior (N2.3–N2.5).
- **EF-G4 (NEW) [IR].** A finite description for a chosen horizon supplies no recurrence guarantee within
  that horizon (N3.1).
- **EF-G5 (NEW) [IR, proof here].** The uniform product measure is invariant under every local
  second-order update on any site set, so double stochasticity holds on infinite carriers of that class;
  candidate 3 and ledger item (iii)'s statistical input do not discriminate cardinality (N3.2). The
  extension to every bijection with both locality clauses and finite alphabets at every site rests
  on (M-full), checked by the review of r4. Both are conditional on a uniform product prior.
- **EF-G7 (NEW) [IR].** For the linear native model, Hankel rank at a cut equals `2^{I(past; future)}`, and
  H-mem is equivalent to a uniform bound on `I*` (5.2).
- **EF-G10 (NEW) [IR].** With entropy rate `h > 0`, torus and infinite lattice first differ between
  `(L − diam V)/2` and `2L³ log₂ q / h` (N3.5); `h ≥ 1` bit under (LE) (N2.10, checked by the review of r3). Under a
  uniform product prior, a premise.
- **EF-G11 (NEW) [IR].** Genuine influence `J_n` can be strictly smaller than the syntactic cone `U_n`; an
  infinite connected bijective system can have a finite `J_∞` and an exactly periodic record (X2)
  (N2.1).
- **EF-G12 (NEW, candidate) [IR].** The shared-prior criterion bears on Main:638's open question (a):
  existence of an all-time realization without inputs, not joining (N2.9).
- **EF-G14 (NEW) [IR, proof here; checked by the review of r3].** Sufficiency for one finite model at
  every horizon, in two forms: autonomous, when the complete relevant state (controller or policy
  memory included) is finite and its evolution is determined by it; with inputs, a finite transducer
  when inputs remain external. Eventual periodicity only in the first (N2.1).
- **EF-G15 (NEW) [IR, proof here; checked by the review of r3].** Leading-edge lemma: on linear
  nearest-neighbour second-order lattices with non-nilpotent axis coupling, `J_∞` is infinite and the
  uniform-prior observation law gains at least one bit per step; EF-G14's hypothesis fails on an
  infinite lattice of that class (N2.10).
- **EF-G16 (NEW) [IR; substantially revised in r4; wording corrected in r5].** What the fixed-horizon
  description preserves (determinism, cone, the law on the window) and what it does not inherit
  automatically (bijectivity, invariant measure, selection principle, recurrence, absolute
  cardinalities, shells, spectra, measurement independence). B1: a bijection with finite reading sets, in which some site is read by infinitely
  many sites, that does not preserve the uniform product measure; it lies outside the locality class
  of `main` (§P).
- **EF-G17 (NEW) [corrected in r5; awaiting check].** Measure preservation, three statements kept
  apart. (M-full): a bijection of the full system with both locality clauses and finite alphabets at
  every site preserves the uniform product measure (checked by the review of r4, under its stated
  hypotheses). The description as defined is a window with no autonomous dynamics, for which an
  invariant measure is not defined: the property is not inherited automatically. Whether a suitable
  finite closed model exists is a separate question: on the patch data, under the uniform patch
  measure, a measure-preserving bijection that reproduces the window exists exactly when the window
  law is shift-stationary (Lemma C), and for second-order rules every fixed-boundary closure is one
  (Lemma C′) [reviewer's lemmas; re-derived by writer; checked by the recheck of r5]. Such a
  closure is a chosen model valid on the window only; it earns no recovery credit yet, and being
  chosen and window-valid does not automatically disqualify it: it could suffice for a theorem
  whose requirements are entirely confined to the window (§P.3, §P.4).
- **EF-G18 (NEW) [checked by the review of r4, under its stated hypotheses].** Lemma PM-I has a
  per-run form and an all-branch form. Finite reads on each run, or on almost every run, do not by
  themselves give one finite patch (E1–E3); a bound on the size of each run's support does not
  either (E2). Lemma K gives one finite patch, non-constructively, from finite reads on every run,
  under the lemma's other hypotheses: a finite alphabet at every site and finitely many values of
  the policy information (N1.5).
- **EF-G19 (NEW) [Proposition N: checked by the review of r4; from finding 3 of the review of r3].**
  With finite alphabets, a finite influence set is necessary and sufficient for one finite
  autonomous model of the record from every initial configuration. Under one fixed initial law it
  is not necessary in general (X3, a point mass) and is necessary when the law charges every
  cylinder [reviewer's refinement; checked by the recheck of r5] (N2.1).
- **EF-G3 (ELABORATING).** Randomness floor and minimal deterministic form (N2.2).
- **EF-G6 (ELABORATING) [IR].** The Bell ceiling's finite-`Ω` proof applies to the pre-setting
  data on `W_A ∪ W_B ∪ A ∪ B` for finite-duration experiments: dependency coverage only, in the
  all-branch form; measurement independence is separate (N3.6).
- **EF-G8 (ELABORATING).** Measurability alone gives an approximate fixed-horizon description (N1.9).
- **EF-G9 (ELABORATING) [IR].** H-mem is compatible with exact qubit behaviour (5.4).
- **EF-G13 (ELABORATING) [IR, proof here; all-branch form checked by the review of r3].** Lemma PM-I:
  with interventions the patch must cover the full experiment (observer sites, policy-read sites and
  intervention supports at every step); the comparison needs a shared protocol; the patch is finite
  under FS-all; the policy may remember its earlier reads (N1.5).
- POSITIVE: N1.3 (the written patch-matching step), N1.6. CONFIRMING: N1.2, N3.4, N3.7, N3.9, N2.3
  (of Main:60, :638). BORDERLINE: N3.8. ELABORATING also: N1.7, N1.8, N2.6, N2.9's bounded-family
  remark and inventory, N3.3, N3.5, N3.10, N3.11, the full traces of §4.2.

## 7. Assumption-watch markers

- **AW-EF1 (comparison versus locality).** When a result is said to need a product prior, ask whether it
  needs it for the fixed-horizon description (it never does, EF-G1) or for equal patch marginals between
  two carriers.
- **AW-EF2 (memory versus randomness).** A finite hidden memory (H-mem, an HMM) bounds the memory the
  visible process uses; it bounds no substratum.
- **AW-EF3 (validity horizon).** Any property of a fixed-horizon realization located after its horizon
  (order, cycle, periodicity, asymptotic entropy rate) is a choice of the completion (Main:520).
- **AW-EF4 (readout locality).** Lemma 1 gives `|C_V| < ∞`, not a readout depending on finitely many
  sites; the patch needs the second.
- **AW-EF5 (quantifier order).** F-each does not give F-one; check which form a proof uses before
  counting anything toward it.
- **AW-EF6 (syntactic versus genuine).** A statement about declared reading sets is not a statement about
  what influences the observer; cancellations can make the second strictly smaller.
- **AW-EF7 (autonomy).** A periodicity conclusion holds only for an autonomous system without continuing
  inputs; settings, experimenter choices and stochastic steps remove it.
- **AW-EF8 (the full experiment).** A dependency patch traced back from the final readout alone misses
  interventions that feed earlier observations. Trace it from every observation time, and include what
  the interventions and the policy read.
- **AW-EF9 (the complete state).** "Finitely many sites matter" bounds a model only when everything that
  evolves is counted: a controller's memory is part of the state, or its outputs are external inputs.
- **AW-EF10 (coverage versus independence).** Showing which data determine an outcome says nothing about
  whether those data are statistically independent of the settings.
- **AW-EF11 (whole systems versus descriptions).** A property proved for a finite whole system (counting
  measure invariant under a bijection, finite order, eventual image, shell counting) is not
  automatically a property of a finite description of its observations; whether a finite closed
  model with the property exists is a separate question (§P.4). On an infinite product, invariance of the uniform
  measure needs both locality clauses or a special form of the rule; it fails for a bijection with
  finite reading sets in which some site is read by infinitely many sites (B1). Check each property a
  proof uses against §P before transferring it.
- **AW-EF12 (special case versus general claim).** A lemma verified on the selected model, where every
  site reads itself, is not thereby verified for general reading sets.
- **AW-EF13 (a memoryless observer).** For a single visible site on the infinite lattice with unit axis
  coefficients under the uniform product prior, the current values are i.i.d., and the observation
  (previous, current) is a Markov chain, so its conditional memory is zero [IR, unreviewed]. The
  framework's regime is the one with memory. Any argument that takes the uniform product prior on an
  infinite lattice as nature's should check that the observer it describes has memory at all.
- **AW-EF14 (per run versus all branches).** "Each run touches finitely many sites" is a statement
  about runs. A finite description, a law or a comparison needs one finite set for every branch. Ask
  which is meant whenever a controller, a setting generator or a search procedure is called local.
- **AW-EF15 (the full system versus its description).** A property of the full system's dynamics
  (measure preservation, bijectivity) is a different statement from the same property of a finite
  description of observations. The description inherits properties of the record law; it does not
  automatically inherit a self-map. One can be chosen on the patch in the cases of §P.4; it is then
  a chosen model, valid on the window only, and its properties are its own. Failure of automatic
  inheritance is not non-existence of a suitable finite closed model (O15).
- **AW-EF16 (a proof's requirements versus its cited lines).** Reading the lines a result is cited at
  under-reports what its proof uses. Seven of eight classes had missing requirements when traced.

## 8. Passes

- Pass 1 (r1): decisive branch, then the cone; NEW EF-G1, EF-G2.
- Pass 2 (r1): recurrence, candidate 3, corner occupancy, native rank; NEW EF-G4, EF-G5, EF-G7, EF-G10.
- Pass 3 (r2): the union repair of the patch; the genuine-influence set and X2; operational conditions;
  the shared-prior proof. NEW EF-G11, EF-G12; EF-G2 narrowed.
- Passes 4–6 (r2): skepticism on favourable readings; re-check against `main`; the result-class table.
  No NEW.
- Passes 7–10 (r3): the PM-I counterexample and the restated patch; finite supports; the two forms of
  the sufficiency result; the leading edge; the preservation table and B1. NEW EF-G14, EF-G15, EF-G16.
- Passes 11–13 (r3): inventory, re-derivation, citations. No NEW.
- Pass 14 (r4; findings 1, 2; OP; O12): the three premise groups; (M-full) re-derived step by step;
  (M-desc) assessed with three closures. NEW EF-G17.
- Pass 15 (r4; findings 4, 5; O13): the policy with memory; the per-run and all-branch forms; the
  check of the review's example, which led to Lemma K. NEW EF-G18.
- Pass 16 (r4; findings 3, 6, 7, 8): necessity re-derived with the alphabet condition; form (ii)'s
  hypothesis; the Bell distance graph; the all-horizon model in §P. NEW EF-G19.
- Pass 17 (r4; finding 9; O14): every class of §4.2 traced through its proof on `main`. The one-step
  coherence results enter the table. ELABORATING. No NEW.
- Pass 18 (r4): every r4 proof re-derived from the written text ((M-full) Steps 1–6; (a′); Lemma K;
  Proposition N; the fixed-boundary closure); every quotation compared with the comment or the line
  on `main`. No NEW.
- Pass 19 (r4): cross-references, the qualifier at each site that mentions B1, the summary and the
  questions. No NEW.

- Pass 20 (r5; findings 1–11 of the review of r4; O15–O19): Lemma C, its corollary, Lemma C′ and the
  one-law necessity refinement re-derived step by step; the statements on measure preservation and
  the description restated; the hypotheses that give one patch for every branch stated; the §3.4
  obstructions traced and added to §4.2; two rows completed; window confinement and direct-proof
  targets read from the traces; conditions organized by claim. Corrections and ELABORATING; the
  three re-derived statements are the reviewer's. No NEW finding of this file.

Four passes without a NEW finding after the last one; stopped.

## 9. Limits and off-`main` references (§A.42 item 8)

- No result here is kernel-checked unless a Lean declaration is named; nothing is computed. Paper steps
  written out here: Lemma PM (assembly, rule clause, law), Lemma PM-I (all forms), Lemma K, N2.1 (both
  forms and Proposition N, with the one-law refinement), N2.3–N2.6, N2.9's remark, N2.10, N3.2, N3.6,
  (M-full), the closures of §P.4 with Lemma C, Corollary C1 and Lemma C′, §P's examples. Steps not written: the channel form of Lemma PM (c) (N3.10, the one-step
  coherence row) and the composition in N1.7.
- **Re-derived by an independent review** (of r2 or of r3): Lemma PM; Lemma PM-I (a)–(e) in the
  all-branch form without the memory clause; N2.1 forms (i) and (ii); N2.3–N2.6; X1–X3; N3.2; N3.6's
  patch; the Main:638 candidate's two directions; N2.9's remark; N2.10; B1–B3.
- **Checked** by the review of r4 (one independent review; paper proofs; not kernel-checked), each
  under its stated hypotheses: the full-system measure theorem (M-full), Steps 1–6; the
  intervention lemma, Lemma PM-I, with policy memory in the all-branch form (a), (b), (c) and in
  the per-run form (a′); the compactness lemma, Lemma K; the necessity result, Proposition N. Also
  checked there: the case proofs of r4's §P.4 (the restriction, the fixed-boundary closure, the
  shift counterexample, the rotation).
- **Checked** by the recheck of r5, `RECHECK-EF-1-r5.md` (one independent check; paper proofs; not
  kernel-checked), each under its stated hypotheses: the reviewer's characterization of when a
  measure-preserving closure exists (Lemma C, Corollary C1), including its application to
  second-order rules (Lemma C′); the reviewer's one-law refinement of the necessity result (N2.1).
  All are the review of r4's, re-derived here by the writer. None gives any class recovery credit.
- **Still unchecked:** r5's restatement of §P.4 and the places that
  cite it; the cells of §4.2 changed or added in r5, the second table included; the claim tables
  of the status section and §4.0; the property list of (δ) (P.5, r4's).
- **Still unproved:** whether a closure preserves everything required to recover a particular
  audited result. No class has a proof of that, and the direct-proof targets of §4.2 are named,
  not proved.
- **Assessment:** §P and §4.2 were substantially revised in r4, and the review of r4 retraced
  seventeen classes (its section 4). The traces were made at the lines given; the SM theorems
  cited by Substratum Stage 2 (b)–(e) and the imported results (Doukas's bound, canonical
  typicality, the unbounded nonnegative rank of qubit behaviours) were not traced.
- **PR #1303** (RO-3 inventory r9, branch `research/ro3-carrier-inventory-1055-20261114` at `59514344`):
  formerly cited for EF-G5 and EF-G10. The invariance they use is derived in N3.2 from Main-level
  inputs, so the claims do not use its content: **provenance**.
- **#1169 comments** c.6894872312, c.6895032895, c.6896070253, c.6896252651, c.6896496410,
  c.6896771264, c.6896890693, c.6896940222, c.6897254631, c.6897455387, c.6897859755,
  c.6897946443: read to quote the owner and the adopted directions, and c.6898760764, read in r7
  for the attribution. They direct the
  work and are not evidence for any mathematical statement: **provenance**.
- **The validity note, the audit and its review:** unpushed drafts used for labels (G-, AM-, P-, Q-
  items). Every mathematical premise a finding here uses is derived here or read at `bf89ba13`:
  **provenance**.
- **The recheck of r5** (`RECHECK-EF-1-r5.md`): an unpushed input. It supplies the independent
  check recorded in the tiers; every statement it checked is proved in this file: **provenance**.
- **The reviews of r1, r2, r3 and r4:** unpushed inputs. Their counterexamples and derivations used
  here (the two shift counterexamples, X1, the induction, the shared-prior construction, the lcm
  argument, the shear/Tonelli argument, the record-shift factor, the measure-preservation
  proposition, the necessity argument, Lemma C with its corollary, Lemma C′, the one-law
  refinement, the infinite-alphabet intervention example) are re-derived in this file:
  **provenance**.
- This file lands nowhere; if any finding is carried into a record on `main`, item 8 applies to that
  record when it lands.

## 10. What is and is not established

The four-claim assessment of the adopted direction (c.6896940222, quoted in the header), with what this file shows for
each:

1. *"A finite description suffices for each fixed horizon": "Convincing under the stated locality and
   finite-state premises".* Lemma PM, a derived lemma. Its deterministic form rests on the finiteness
   premises F1–F5 of §4.0; a normalized starting law (P1) adds probabilities and is not a premise of
   finiteness; no further distributional property is used. With settings, inputs or policies: Lemma
   PM-I, on F1–F7, in a per-run form and in an all-branch form; the all-branch form is proved under
   FS-all, or from finite reads on every run, under the lemma's other hypotheses (Lemma K). Of the
   finiteness premises, the finite visible region (F4) and finite supports over all branches (F7)
   are not stated separately on `main`, and finite reading sets (F3) and finite site alphabets (F5)
   are on `main` without A1 for the selected model only. The lemma is conditional on these.
2. *"That description preserves everything needed by a particular A1-dependent theorem": "Requires a
   separate proof".* §P shows what is preserved (determinism, the cone, the law on the window) and what
   is not inherited automatically (bijectivity, invariant measure, recurrence, cardinalities, shells,
   spectra, measurement independence). Measure preservation by the full system, (M-full), is a
   separate claim, checked by the review of r4 under its stated hypotheses. It does not make the
   description an autonomous measure-preserving system: the description as defined is a window, for
   which an invariant measure is not defined. Whether a suitable finite closed model exists is a
   separate question; a measure-preserving closure that reproduces the window can be chosen on the
   patch in the cases of Lemmas C and C′ (checked by the recheck of r5). It is a chosen model valid
   on the window only; it earns no recovery credit yet, and being chosen and window-valid does not
   automatically disqualify it: it could suffice for a theorem whose requirements are entirely
   confined to the window. §4.2 lists the properties each proof uses, from a full trace, and
   says for each class whether they are confined to the window. No such separate proof is given
   here for any theorem; every class has no recovery credit.
3. *"One finite autonomous model works for all horizons": "Not established by the fixed-horizon
   argument".* Verdict 3. Two sufficient conditions are proved (N2.1), under hypotheses nothing here
   supports. With finite alphabets the first is also necessary for a model of the record from every
   initial configuration (Proposition N, checked by the review of r4). Under one fixed initial law it
   is not necessary in general (X3, a point mass) and is necessary when the law gives positive
   probability to every finite pattern (reviewer's refinement, checked by the recheck of r5). The
   hypothesis does not hold on an infinite lattice of the linear nearest-neighbour class (N2.10).
4. *"Nature must recur, or observations obey a new measurable bound": "Does not follow from this
   argument alone".* A fixed-horizon description gives no recurrence within its horizon (N3.1); every
   finite-horizon law is consistent with periodicity and with its absence (N2.6); none of the audit's
   three candidate tests becomes a test of A1 (N3.11). The measurable consequences listed in §5.4
   belong to the hypothesis H-mem, a draft, not to the argument.

Adopted direction (c.6897455387): "the core argument looks increasingly convincing; its ability to recover
particular A1-dependent results remains open." Adopted direction (c.6897859755): "effective finiteness now has
substantial checked mathematical support. Its physical consequences remain unresolved." That is the
state of this file: items 1 and 3 are proofs re-derived by reviews, the one-law refinement in item 3
by the recheck of r5; item 2's assessment was substantially revised in r4, retraced by the review of r4 and
corrected in r5 at the points that review found, and the corrections are awaiting check. In the
owner's six claims (O19; status section): claims 1 and 2 are checked and conditional on flagged
premises; in claim 3, invariance is checked for the full system, under its stated hypotheses, and
uniformity and measurement independence are premises; claim 4 is checked by the recheck of r5,
under its stated hypotheses; claims 5 and 6 are unproved.

### Plain-language summary for the owner

Over any chosen number of steps, the observations are fixed by starting data on a finite patch of
sites, given locality and a finite visible region; a starting law only adds probabilities. Runs
compared need the same settings, or the same policy with its information. One patch for every
branch needs finite supports over every branch, or finite reads on every run, under the lemma's
other hypotheses; finite reads on only the runs considered are not enough. Without A1, those
finite supports and a finite visible region are not stated as separate premises on `main`.

**Checked** (one independent check), each under its stated hypotheses: the full-system measure
theorem; the intervention lemma; the compactness lemma; the necessity result and its one-law
refinement; the characterization of when a measure-preserving closure exists, second-order rules
included.

**Still unchecked:** r5's rewording (§P.4, §4.2).

**Still unproved:** whether such a closure preserves everything required to recover a particular
audited result.

The description is a window: it does not automatically inherit the full system's measure
preservation. Whether a suitable finite closed model exists is a separate question. The closure
result earns no recovery credit yet; being a chosen, window-valid model does not automatically
disqualify it either. §4.2 marks window-confined requirements and unproved direct-proof targets.
No class has recovery credit; one finite model for all time is not established.

## 11. Owner questions

Each question is self-contained. "A1" is the posit that the total state space is finite (item (ii) of
the posit ledger, Main:724).

1. **A fixed-horizon lemma in Main.** Should Main state the autonomous patch lemma: over any `n`
   steps, two initial configurations that agree on the finite set of sites from which the observer can
   be reached within `n` reading steps give the same observations; and, given a normalized initial
   law, the law of those observations depends on it only through that set? It would be stated with
   its finiteness premises (site factorization, finite reading sets, a finite visible region, finite
   site alphabets), with the initial law as a separate premise for the probability statement, and
   with no recovery credit for any theorem until that theorem's requirements are checked. For
   experiments with settings, should Main take only the version with one setting step that the Bell
   ceiling uses (settings the same in the runs compared; the patch enlarged by the setting regions;
   those regions finite), and leave the multi-step version with adaptive policies out of Main unless a
   result of Main that uses it is named?
2. **Main:362.** Main:362 says "Finiteness of $V$ is used in the first step", where `V` there is the
   whole site set. Should that sentence give way to a stated hypothesis that each site's update reads
   finitely many sites, taken from ledger item (xiii) on the selected model (which widens that item's
   listed role) or from a single-lattice restatement of the bounded-degree item (ix), together with a
   finite visible region stated as a premise of the spatial constitution?
3. **Where the carrier comparison belongs.** The statement that two carriers with the same local rules
   on the patch and the same patch distribution give the same observations up to the horizon (so a
   large enough finite torus and the infinite lattice agree over `n` steps) has no consumer in Main at
   present. Should it stay downstream with GR:112 and GR:132, or should Main take one of two possible
   consumers: a fixed-horizon scope statement for the corner-occupancy sentence of Main:216, or a
   fixed-horizon version of the §3.2 setup?
4. **The initial law.** For an infinite carrier, is "a normalized initial law on the whole carrier"
   acceptable as the premise that supplies probabilities? It asserts no cardinality, it is not needed
   for finiteness, and the reconstruction direction (from the observation law to realizations) does
   not use it. Any further property of that law (uniform, product, invariant) would be a separate
   premise needing its own justification.
5. **Premises to track.** Without A1, three conditions are not separately stated premises on `main`:
   (a) that the visible region is a finite set of sites with a site-local readout; (b) that, at each
   step, the set of all sites the permitted interventions and policies could read or act on, over
   every branch, is finite, which on `main` follows from the finite site set of Main:362; and (c) for
   the Bell theorem, that the setting and readout regions are finite. Measurement independence is
   already ledger item (xiv), a posit. Where should (a)–(c) be recorded: in the posit ledger, in the
   hypotheses of the theorems that use them, or in an Issue until a manuscript change is decided?
6. **Double stochasticity as a test of A1.** The audit lists "bijective dynamics with a uniform hidden
   prior give a doubly stochastic one-step matrix" as a possible test of A1. It holds on infinite
   lattices with the second-order update, by a reviewed proof. A proof checked by one independent
   review extends it to every bijection in which each site reads, and is read by, finitely many
   sites, with finitely many values at every site. Both are conditional on a uniform product
   starting law. It does not hold for one bijection with finite reading sets in which some site is
   read by infinitely many sites. Should it be removed
   from the list of A1 tests, and should ledger item (iii) record that its statistical input does not
   bear on the carrier's cardinality?
7. **Main:638, open question (a).** Main:638 leaves open "exact all-time gluing for recurrent families
   of multi-time laws — which compatibility conditions on the per-horizon realizations suffice". Is the
   question meant with or without interventions? This file's candidate covers only the case without
   inputs, and proves existence of one all-time realization exactly for families that repeat with one
   common period along every path; it does not prove that given realizations join. Should that
   candidate be reviewed independently? A rewording of Main:638 would also touch Main:731,
   `papers/Introduction.md:178`, the census anchor at `verification/lean-manuscript-census.json:875`
   and the guard at `verification/lean/edge_rigidity_probe.py:6928`.
8. **A1's visible content.** If A1 is kept as an explicit hypothesis of the results that need it,
   should it carry its operational conditions: "for an autonomous, deterministic, finite system without
   continuing inputs, the visible record is eventually periodic, and exactly periodic for the bijective
   representative, with no bound on the period", together with the fact that every finite-horizon law
   is consistent with it?
9. **Independent checks before anything rests on the new proofs.** The review of r4 checked four
   paper proofs and found them sound, each under its stated hypotheses: (a) a bijection of the full
   system in which each site reads, and is read by, finitely many sites, with finitely many values
   at every site, preserves the uniform product measure; (c) one finite patch for every branch
   follows from finite reads on every run, under the lemma's other hypotheses (finitely many values
   at every site; finitely many values of the policy information), and the conclusion can fail when
   any one of the three conditions is dropped; (d) with finite alphabets, a finite set of
   influencing sites is necessary as well as sufficient for one finite autonomous model of the
   record from every initial configuration; and the intervention lemma with policy memory, in its
   all-branch and per-run forms. Two further statements of that review, re-derived here, were
   re-derived independently by the recheck of r5 and found sound, each under its stated
   hypotheses: (b) the finite description does not automatically inherit a measure-preserving map;
   on the patch data, with all patch data taken as equally likely, a one-to-one map that matches
   the observations up to the horizon can be chosen exactly when, under that measure, the
   statistics of steps 1 to `n` equal those of steps 0 to `n − 1`; and for updates of the
   second-order form (ledger item (xiii), Main:724) the map obtained by holding the sites outside
   the patch at any fixed values is always one;
   (e) under one starting law that gives positive probability to every finite pattern, a finite set
   of influencing sites is necessary as well. c.6897859755 says "no additional review scope is
   needed" for the targeted r5. Is that one independent check of (b) and (e) enough for the
   corrected text to be relied on? And is the one independent check of (a)
   enough for your condition that it be independently checked before it supports any recovery
   classification? No classification here rests on any of them.
10. **Which theorem to check first, and which direct proof to attempt first.** No result class has
    recovery credit. Which class should have its theorem's requirements checked first against the
    list of properties its proof uses (§4.2)? The classes for which the fixed-horizon form looks
    sufficient are the coupling-graph causal cone, the dependency part of the Bell ceiling, the
    baseline transition matrices under a uniform hidden prior, the deep-sector comparison, and the
    in-window form of the overlap-and-return theorem. The classes whose traced requirements are
    confined to the window and use a bijection of a finite carrier, so that a chosen closure (a
    self-map of the patch data, added by choice, that matches the observations up to the horizon)
    could suffice, are the one-step §3.2 setup, the one-step coherence results and the baseline matrices.
    For which of these should a direct proof of the observable conclusion be attempted first (§4.2,
    second table)? Each named target is conditional on the claims it lists, and none is proved.
11. **The finite-hidden-memory draft.** The draft hypothesis says that the matrix of joint
    probabilities of visible pasts and futures has rank at most one number `d` at every horizon and
    every cut. Should it be pursued as a named hypothesis for the operational-reconstruction route
    (Main:562), not as a replacement for A1? Is there an independent argument for `d`? Would you
    authorize, separately, an exact rank computation for the selected rule as its internal control?

## 12. Remaining disagreements

Both positions are given for each point. The first list is r4's, with the review of r3 and the
coordinator, updated where r5 or the review of r4 settles a point. The second list is with the
review of r4.

**With the review of r3 and the coordinator (r4's list).**

1. **The review's example for finite support per run (finding 5).** *Review of r3:* in the example
   that finds the least `j ≥ 1` with `s_j = 1`, "Every run reads finitely many sites", yet no finite
   patch exists. *This file:* the runs with no 1 beyond site 0 read every site, so the example has
   finite reads on almost every run, not on every run. The difference matters, because with finite
   alphabets at every site and finitely many values of the policy information, finite reads on every
   run do give one finite patch (Lemma K). Both agree that FS-all, as formally stated, excludes the
   example and that "finite for each run" is not the hypothesis of the lemma. *Settled:* the review
   of r4 checked Lemma K and confirmed that the example does not have finite reads on every run.
2. **How (M-full) is presented (finding 2).** *Review of r3:* after re-derivation, state it beside B1
   as the other half, a theorem about the infinite system, and extend EF-G5 and candidate 3 to the
   whole locality class. *This file, following O12:* it is stated as a proposition, kept apart from
   the statements about the description, and the extensions are marked conditional on it and on a
   uniform product prior; no class cites it. Both agree on its statement, on the proof's steps and
   on B1's scope. The review of r4 has since checked the proof.
3. **Necessity and alphabets (finding 3).** *Review of r3:* "`J_∞` finite with finite alphabets on it
   ⟺ finitely many records". *This file:* finitely many records give a finite `J_∞` with no alphabet
   condition; the converse needs finite alphabets on `J_∞`, with an example. A refinement, not a
   dispute.
4. **Main:216's first-order clause.** *Review of r2:* a fixed-horizon statement. *Review of r3:* still
   unchecked; the place to check is Main:340. *This file:* Main:340 is a short-time estimate with no
   property uniform in the horizon, but its written derivation runs inside the §3.2 setup with a
   finite hidden space, and no derivation with a patch in its place exists; so the form is
   undetermined, not F-each.
5. **Conditional or unconditional intervention patch.** *Review of r2:* add an intervention's region
   only when it meets the backward set. *r3, the review of r3 and this file:* always add it, with the
   smaller patch recorded as a remark.
6. **One sentence of the brief.** *The brief and the review of r3:* "a recovery candidate is not a
   recovered result" is owner wording. *r4:* it was not found in the ten comments then read, so it
   was used as a rule and not printed as a quotation from a comment. *Settled:* the source is
   adopted direction (c.6897859755), given in the session of 2026-11-15; it was not separately recorded on #1169, and
   c.6897859755 has since recorded it as a sentence from that session.
7. **Labels.** *Review of r3:* "O12" is the direction on derived lemmas and premise separation.
   *Coordinator:* O12–O14 are the three later requirements. *This file:* the earlier direction is
   labelled OP, and O12–O14 follow the coordinator.
8. **One relayed sentence.** *Coordinator's relay:* "the measure-preservation proof needs independent
   checking before it supports any recovery classification". *The comment (c.6897455387):* "The
   reviewer's new measure-preservation proof also needs independent checking before it supports any
   recovery classification." This file quotes the comment.
9. **Counting the B1 sites.** *Coordinator's note:* eleven sites. *Review's list:* twelve entries
   when the two rows of the preservation table are counted apart. This file applies the qualifier at
   all of them and at the other places that mention B1.

**With the review of r4.** Its three listed disagreements (its section 7) are accepted, and no
finding is disputed. What remains are points of scope.

1. **(M-full) and r4's (M-desc).** *Review of r4:* with a uniform product prior the first implies
   the second as r4 defined it (Lemma C), and for the selected model the fixed-boundary closure is
   a measure-preserving bijection (Lemma C′). *This file:* accepted after re-deriving both lemmas;
   r4's two statements are withdrawn and the matter is restated in the owner's form (§P.4). No
   disagreement remains. Both lemmas have since been checked by the recheck of r5.
2. **What the all-branch form needs.** *Review of r4:* FS-all or Lemma K's hypotheses. *This file:*
   accepted; Verdict 2, N1.5, §4.0 and the summary now say so. No disagreement remains.
3. **Necessity under one law.** *Review of r4:* not necessary for a law that misses some finite
   pattern; necessary for a law that charges every cylinder. *This file:* accepted after
   re-derivation, with one observation added by the writer, which the recheck of r5 confirmed: that
   direction uses no compactness and no alphabet condition.
4. **The channel off the diagonal (remedy of finding 1, one clause).** *Review of r4:* a
   window-faithful closure supplies "populations only; the channel off the diagonal depends on the
   closure". *This file:* accepted, after checking it first-hand with a two-site example in which
   two bijective closures of one window differ in their off-diagonal action (§P.4, "Consequence
   for result classes"). One question is added and left open: whether the fixed-boundary closures
   of one rule agree with one another and with the stage form of N1.7.
5. **Scope of Lemma C.** *Review of r4:* stated for the uniform patch measure. *This file:* the
   same, with the scope made explicit: it concerns bijections of the patch data under the uniform
   patch measure, which is the description's probability only under a uniform product prior, and a
   failure of its condition (as in B1) says nothing against a finite closed model on another
   carrier, which exists for every finite-horizon law (Main:516–520). Not a dispute.
6. **F5 (finding 6 (a)).** *Review of r4:* flag finite site alphabets off the selected model as F3
   is flagged. *This file:* flagged. One nuance: Main:362 does state the condition in terms ("each
   $S_i$ finite"), beside the finite site set, so off the selected model it is stated on `main`
   within a setup that also assumes A1's content, not absent from `main`.
7. **Whether one check of (M-full) suffices.** *Review of r4:* "Whether one check suffices is the
   owner's call". *This file:* the same; put to the owner in question 9.

## r6 changes

r6 is `EF-1-r5.md` (sha256 `3cf761f0313e57eb6718f82bf3d6dc54dbbe710a85736c3a5858c84ae0beb16d`) with
nits 1–8 of its independent recheck, `RECHECK-EF-1-r5.md` (CONFIRMED WITH NITS), applied. That
recheck re-derived Lemma C, Corollary C1, Lemma C′ and the one-law necessity refinement and found
them sound; its nits concern wording and status marks, and none touches a proof. Nothing outside
this table is changed from r5. No class gains recovery credit, and the tier "still unproved" is
unchanged.

| Item | Point | Change | Where |
|---|---|---|---|
| Round label | — | The title and the first sentence say r6; the mark "[checked by the recheck of r5]" is defined, and r5's two marks for statements not independently checked are described as r5's | Header |
| Nit 1 | The summary omits the settings condition, the statement that finite reads on only the runs considered are not enough, and the two premises not stated separately on `main` | All three restored. To keep the summary within 220 words: the owner's assessment quotation is left to §10, where it stands; the parenthesis on the compactness lemma is dropped, its content being in the restored sentence; "Conditions are listed per claim" and the label "Scope is conceded" are dropped; the sentence on §4.2 is shortened | Summary |
| Nit 2 | Two summaries of Lemma C drop its measure; questions 9 (b) and 10 use terms without a gloss | "under the uniform patch measure" restored in the row for §P.4; question 9 (b) restated with the measure and in plain terms; the gloss of "chosen closure" added to question 10 | Status section ("Detail by piece"); §11 |
| Nit 3 | Four sentences drop the owner's word "automatically" | "does not automatically disqualify it" restored, with the owner's clause "it could suffice for a theorem whose requirements are entirely confined to the window" where the nit gives it | Status section ("Detail by piece"); EF-G17; §10 item 2; summary; "r5 changes", row O17 |
| Nit 4 | "Under its stated hypotheses" missing at brief mentions | Added | Header (mark definition); Verdict 11; §10, last paragraph; "Detail by piece", rows for N2.1 and (M-full) |
| Nit 5 | One-step coherence row: the target omits the rule its conclusion is proved for; the window cell omits the dependence on the closure | Target restated for one step of the displayed update over `F_2` (Corollary 1, Main:316; stated for `q = 2`, Main:324; both lines re-read on `main`); the open point added to the window cell. The recheck's optional example is not added | §4.2, second table |
| Nit 6 | Lemma 3 row: a favourable aside without its caveat | Caveat appended: the existence of a bijective closure is itself a statement made under the uniform patch measure | §4.2, second table |
| Nit 7 | Two stale marks on N2.10 | "unreviewed" replaced by "checked by the review of r3" | N3.5; EF-G10 |
| Nit 8; proof-status tiers | Standing of Lemma C, Corollary C1, Lemma C′ and the one-law refinement after the recheck | The four are listed as checked, each under its stated hypotheses, with the recheck named as the one independent check; they remain paper proofs, not kernel-checked. The recheck's own remedy was to leave them under "still unchecked" until the owner accepts that check; r6 moves them on the coordinator's instruction, and the owner's quotation of the three tiers is unchanged. "Still unchecked" keeps r5's restatement of §P.4 and the cells of §4.2 changed or added in r5. "Still unproved" is unchanged. The status marks of the four statements are changed to match wherever they stood; the recheck is added to the list of unpushed inputs | Tier table and the line under it; claim table (claim 4); "Detail by piece" (N2.1, §P.4); Verdicts 3, 6, 11; "Scope conceded"; response table, row R4-c; N2.1; N2.8; §P.2; §P.3; §P.4 (b2), (b3), conclusion, consequence; N3.3; N3.10; §4.0 (D8; claim 4, C2, C3); §4.1; §4.2 (the §3.2 row); EF-G17; EF-G19; §9; §10 items 2, 3 and last paragraph; summary; question 9; §12 |
| Not applied | The recheck's optional remarks | Neither the example of its section 1.6 nor its remark on "Scope of Lemma C" (1) is added; both are unchecked. Question 9's letters keep their order | — |

## r7 changes

r7 is `EF-1-r6.md` (sha256 `34f3ec8f019053cb0755cc089d94a91f45ef6c19ac354e763b5b8285e6fe6d9f`) with one correction of attribution.
The owner stated on 2026-11-15, "Relayed, and I adopt them." (#1169 c.6898760764): the texts quoted
from c.6896252651, c.6896496410, c.6896771264, c.6896890693, c.6896940222, c.6897254631,
c.6897455387, c.6897859755, c.6897946443 and c.6898395533 are review text the owner relayed and
adopted, not the owner's own words; the owner's own words are in c.6894872312, c.6895032895 and
c.6896070253. Nothing outside this table is changed from r6. No quoted text, mathematical
statement, status mark or classification is changed, and no class gains recovery credit.

| Item | Point | Change | Where |
|---|---|---|---|
| Round label | — | The title and the first sentence say r7; the first sentence also states what r6 is | Header |
| Definition | The short label | A paragraph "Attribution" defines **adopted direction (c.N)** as "adopted direction (review text relayed and adopted by the owner, #1169 c.N)" and names the three comments that carry the owner's own words | "Owner directions and adopted directions in scope" |
| Section introduction | The section was introduced as the owner's directions and its quotations as the owner's words | The purpose sentence of the header, the section heading and the sentence on the source of the quotations name the adopted directions beside the owner | Header; "Owner directions and adopted directions in scope" |
| Comment headings | Nine quoted comments headed without attribution under the owner's heading | Each heading reads "adopted direction" | c.6896252651, c.6896496410, c.6896771264, c.6896890693, c.6896940222, c.6897254631, c.6897455387, c.6897859755, c.6897946443 |
| Quotation labels | Quotations from the ten comments introduced as "Owner", "Owner (c.N)", "Owner (O…)", "Per the owner", "The owner's distinction(s)", "The owner's four-claim assessment", "as the owner separates them" | Each relabelled "adopted direction", with the comment id where the label had only an O-label or none | Status section (claim table; "Detail by piece", row for (M-full); proof-status tiers); Verdicts 2 and 6; "Scope conceded" (four labels); N1.5; §P; §P.3; §P.4; §4; §4.0 (five labels); §4.2 (two labels); §10 (three labels) |
| Authorship verbs | "The owner tightened that wording", "the owner corrects", "the transfer the owner separates out" | The adopted direction is the subject | c.6896070253 entry; O1; §P.4, conclusion item 4 |
| "A recovery candidate is not a recovered result." | Its source was given as the owner's own sentence | Source: adopted direction (c.6897859755), given in the session of 2026-11-15; used as an adopted rule | Header (c.6897859755 entry and the paragraph on the sentence); §12, item 6 of the disagreements with the review of r3 |
| Off-`main` references | c.6898760764 was not listed | Added as provenance, read in r7 for the attribution | §9 |
| Not changed | — | The quoted text; the attribution of c.6894872312, c.6895032895 and c.6896070253 to the owner; possessive references to the adopted positions (for example "the owner's tiers", "the owner's six claims"), which the owner's adoption covers; the owner's decisions and questions; the response table and the tables "r5 changes" and "r6 changes", which record their rounds | — |
