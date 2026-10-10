# PT stage 2 — sourcing S3 and S2 (research only; frozen at launch)

**Owner's direction (verbatim excerpts).**
> "1. Source S3 independently. Find an observer-native principle of multi-system composition that actually implies FCC.
> Crucially, distinguish ordinary associativity from the stronger cross-pairing consistency required by the four-copy
> theorem. We should not merely rename FCC as regrouping invariance."
>
> "2. Source S2 independently. Construct a pair system from preparation, effect and operation data without choosing its
> desired cone in advance. Investigate which natural conditions provide finite rank, local tomography and compatibility
> with the native gate."
>
> "These questions are closely related, and I would investigate them in parallel."
>
> "One important qualification: INDEPENDENT relative to L doesn't mean these must remain independent principles forever.
> A stronger observer-native theory of composition might eventually derive them."
>
> "I would also preserve Thread C's narrowed tree-obstruction result and the independent audit corrections exactly as
> recorded, rather than generalizing them."
>
> "My recommendation is not to open governed rounds or spend CI on these results yet. The next valuable achievement would
> be discovering an independently motivated source for S2 or S3, or establishing with a rigorous countermodel that a
> proposed source cannot work."
>
> "Any external presentation should clearly distinguish the computational findings, written arguments and unbuilt or
> design-checked Lean results."
>
> "Why should independently observable systems, when combined, obey the same consistency rules that produce quantum
> entanglement?"

The threads:
- **S3 — COMP-CONS** (`pt/S3/`): an observer-native composition principle that implies FCC, not FCC renamed.
- **S2 — PAIR-CONS** (`pt/S2/`): a pair system built from data, and the natural conditions for finite rank, local
  tomography and native-gate compatibility.

Nothing here is adopted, frozen in the repository, or governed. The coordinator audits each result. There is no
publication page, PR, CI run, branch or repository change.

## Governing texts

`pt/PROTOCOL.md` (sha256 `239dc123…`), amendment 1 (`b41aa0e7…`) and amendment 2 (`2a2f78f3…`) govern stage 2, except
where this file differs: their shared rules, evidence tags, script rules, integrity rules, limits, investigation mode,
labels, and the separation of sufficiency proved from survives the countermodels. Where this file differs, it governs.

`pt/` below means `/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/`.

## Base and inputs (read-only for both threads)

- **Base:** certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, at `pt/base/` (unchanged).
- **Stage-1 inputs:** `pt/inputs/` (manifest `pt/inputs.manifest.sha256`, 41 files).
- **Stage-1 results, audits and review:** `pt/A/`, `pt/B/`, `pt/C/`, `pt/D/`, `pt/audit/`, `pt/INTEGRATION-REVIEW.md`,
  and the protocol files. Manifest: `pt/stage1.manifest.sha256` (209 files). The audits take precedence over the
  results they audit. **Start by reading `pt/INTEGRATION-REVIEW.md`, then the audits, then the results relevant to
  your thread.**
- **Stage-2 inputs:** `pt/inputs2/oi-substratum/` — the RANK, QUOTIENT and RECORD results on OI-native substratum
  protocol towers (read as leads). Manifest: `pt/inputs2.manifest.sha256`.
- **Mathlib v4.33.0 source** (grep only): `/home/user/leanprover-community/mathlib4`.

## Stage-1 findings to preserve exactly (cite as recorded; do not generalize)

- **Thread C's tree obstruction, narrowed (AUDIT-C).** B3 holds for chart-invariant conditions on the cones and gate
  *maps* of at most three of the four pairs. It does not hold, as stated, for conditions that may read the supplied
  locals: two chart-invariant 3-pair conditions on the post-local determinant pattern imply EvenCycle, and with "each
  cone is Q3 or twin" they imply FCC.
- **The audit corrections and labels** in `pt/audit/AUDIT-{A,B,C,D}.md` and `pt/INTEGRATION-REVIEW.md` §1–§2.
- **Scope of INDEPENDENT.** Every INDEPENDENT means independent of the premises certified at L as stated, a base that
  defines no pair system and nothing with three or more tokens. It is not a claim about every observer-native extension.

## Shared rules for stage 2 (in addition to the governing texts)

- **Labels (amendment 2), per target:** DERIVED / CONDITIONAL / INDEPENDENT / UNRESOLVED.
  - A principle whose content is the target in other words makes the target UNRESOLVED, with the restatement recorded.
    It does not make it CONDITIONAL.
  - Every CONDITIONAL also states the principle's strength relative to the target on the families examined: strictly
    stronger, equivalent, or weaker.
  - A model of one route's premises in which the target fails is "route refuted", never INDEPENDENT.
- **Renaming test (owner's warning).** Before classing a principle as a source, decide in writing whether its content,
  unfolded into the definitions, is the target's own content. Examples: cross-positivity of one grouping's product
  effects on the other grouping's product states, for FCC; preservation of the pair body by the gate, for `hgate`. If
  it is, it is a restatement, whatever its vocabulary.
- **Forbidden as premises:** as in `PROTOCOL.md` (IE1, IE2, `Q3`/PSD as a premise, the complex region tower, (o) steps,
  operation-level idle extension, the thread's target in other words).
- **Flagged routes.** A flagged route may be analysed but never used as a premise: what it yields is recorded exactly,
  with why it is excluded, and it is never counted as sourcing S2 or S3. The flagged routes are:
  - local agency: single-system operations act on a token of a pair state with the `W 3` coordinate action, which is
    operation-level idle extension;
  - frame covariance of the native gate: every local-rotation conjugate of `cnot` is native;
  - any principle shown to be equivalent to one of these.
- **Evidence levels in every summary.** Kept apart:
  - kernel: [K] certified at L, [D] design-run;
  - written arguments [W];
  - exact computations [X], stated for the instance they check;
  - literature [L, unverified];
  - UNBUILT Lean.

  An exact computation is called universal only when it is exhaustive over the object in question or lifted by a
  written argument.
- **Integrity.** At start and end:
  - `sha256sum -c --quiet` on `inputs.manifest.sha256`, `stage1.manifest.sha256` and `inputs2.manifest.sha256`;
  - base HEAD `9f9f8257…`, with empty status;
  - the four protocol files unchanged (this file's hash is in `PROTOCOL-STAGE2.sha256`).

  Write only inside your own thread directory.
- **Limits.** No git writes, branches, pushes, PRs, CI or GitHub access. No publication. No agents spawned. Network
  egress is restricted, so mark literature [L, unverified].

## Thread S3 — COMP-CONS (`pt/S3/`)

**Question.** Find an observer-native principle of multi-system composition that actually implies FCC, together with the
pair hypotheses it needs. Distinguish ordinary associativity from the stronger cross-pairing consistency the four-copy
theorem requires. Do not rename FCC as regrouping invariance.

**Facts to start from** (re-verify what you use).
- **C, audited.**
  - `N0 ∧ N1 ∧ N2 ⇒ KT4Core ⇒ FCC` under `hadm` (Lemma B1 [D]).
  - Converse via the MSIG hull body: `∃V.(N0 ∧ N1 ∧ N2) ⟺ FCC` relative to `hadm`. The cross values of that
    construction are exactly the FCC forms.
  - Every proper sub-conjunction of {N0, N1, N2} holds on every quadruple of nonempty pair bodies.
- **The mixed assignment and its family.** On {Q3, twin}⁴, FCC holds exactly at the 8 coboundary (even) twist
  patterns. Under `hcls ∧ hgate` on such cones the orientation bits equal the twist bits (AUDIT-C, [W + X]), and
  orientation is a gate invariant (D, T2).
- **Uniform foils.** Uniformity, one-pair-type matchings and U* are refuted by uniform `K_c = K_gen = SEP + cnot SEP`:
  closed, admissible, `cnot`-invariant, with FCC −1 (C) and −1/8 (A) and IE1 failing.
- **Entangled core.** FCC holds automatically when any one argument is separable, so uniform `SEP` and uniform
  `maxCone` satisfy it.
- **Effect quantifier.** FCC quantifies its effects over the full duals `dualW K_p` (no-restriction). The design proof
  reads FCC only at gate-supplied link instances (C, c4 [W]).
- **Stage 1.** `Q3` is the local-rotation closure of `K_gen` [W + L], and the theorem obtains IE1 from FCC.

**Nodes** (depth-first; decisive first; refine as you go):
- **S3.1 Associativity versus cross-pairing** (the owner's required separation).
  - Define precisely:
    - ordinary associativity for a fixed token order: the bracketings of 0, 1, 2, 3 that keep the order, as conditions
      on a family of carriers or pre-composites;
    - cross-pairing consistency: relating `01|23` to `02|13`, which exchanges tokens 1 and 2, and the minimal extra
      structure it needs (an exchange or braiding of tokens; naturality on states).
  - Establish exactly, with a separately identified witness per direction (§A.34):
    - what associativity alone implies about pair 02 and about FCC;
    - what cross-pairing adds;
    - where N0, N1 and N2 sit on this ladder;
    - the precise content of the cross-pairing step.
- **S3.2 Candidate sources whose statement does not contain FCC's cross-positivity.** Test each for sufficiency (a
  written derivation with exact ingredients) or refutation (an exact countermodel satisfying the candidate and the pair
  hypotheses, with FCC failing). Candidates include, but are not limited to:
  - **Pair-level structural principles,** with and without type uniformity: self-duality `K = dualW K`; strong
    self-duality; homogeneity; Jordan or Koecher–Vinberg structure [L, unverified].
    - The narrowed B3 says per-pair cone and gate-map principles cannot exclude the mixed assignment.
    - Establish what they can do (for instance, restrict each cone to {Q3, twin}) and exactly what residue they leave.
    - Prefer an exact self-dual, admissible, `cnot`-invariant cone other than Q3 (or a proof that none exists) to any
      appeal to an existence theorem.
  - **Token-level orientation coherence:** each token carries one orientation shared by every pair it belongs to.
    - It is a Z₂ principle about frames, related to K∞-Copy and the landed OrientationSelection/OrientationClosure
      records.
    - On the classified family it would supply exactly the coboundary condition.
    - Decide whether it is FCC renamed or an independent principle. State what it needs in order to apply: a reason the
      pair cones lie in {Q3, twin}.
  - **Conditioning principles:** "measuring part of a composite leaves the rest in a valid state". C classed
    swap/conditioning closure as ⟺ FCC. Re-examine whether an operational formulation that does not presuppose the full
    duals is weaker than FCC, equivalent to it, or independent of it.
  - **Purification-type principles** (a pair state has a purification on four tokens), **entanglement-swapping
    consistency**, and **no-restriction for four-token effects**.
- **S3.3 Independence and obstruction.**
  - For any candidate that implies FCC, give the renaming test and the independence assessment.
  - For any refuted candidate, give the exact countermodel.
  - For any class of candidates, give an exact obstruction where one exists.
- **S3.4 The owner's central question, as far as this thread reaches.** Why should independently observable systems,
  combined, obey cross-pairing consistency? Report:
  - the most explanatory non-renaming principle found;
  - its exact strength relative to FCC on the stated families;
  - the remaining gap.

## Thread S2 — PAIR-CONS (`pt/S2/`)

**Question.** Construct a pair system from preparation, effect and operation data without choosing its desired cone in
advance. Investigate which natural conditions provide finite rank, local tomography and compatibility with the native
gate.

**Facts to start from** (re-verify what you use).
- **A, audited.**
  - The narrow product of two one-ball directed systems, and its `cnot` closure, are DERIVED constructions: closed in
    ℓ^∞, finite rank, compact read-out.
  - Local tomography holds there by construction (product labels only), and their cones are `SEP` and `K_gen`.
  - Closing under `actT reflY ∘ cnot` gives an invalid table (−1/2).
  - For the theorem's cone, the closedness content is finite rank of the pair completion; ID restates `hcl` relative to
    `hadm`.
- **D, audited.** T3: `hadm ⟺` the pair cone is the product-test cone of a COMP-1 pre-composite of two balls, with no
  `lt` needed. `paddedBall3` is a non-locally-tomographic pre-composite with an admissible cone.
- **B, audited.**
  - The sources found for `hgate` restate it (JR/PreservesBody of the pair slice; P-ACT2; reversibility on the pair
    state space).
  - A product-only pair system admits no operation datum for `cnot` (`F = diag(1,−1,1,−1)`).
  - `hgate` as stated constrains the pre-locals.
- **Stage 1.**
  - S2 = `hadm ∧ hcl ∧ hgate`. Relative to `hcls`, on the table carrier, it says the normalized slice of `K_p` is the
    body of a compact COMP-1 pre-composite that the native gate preserves in both directions [W, assembled].
  - `K_gen` satisfies S2; uniform `K_gen` fails FCC and IE1.
- **Upstream (inputs2).** The OI-native substratum towers tested so far (RANK, QUOTIENT, RECORD) do not give a
  qubit-sized single system: the rank or effect dimension is over or under the target for the tested rules (ALL FAIL).
  A pair built from substratum data inherits that open problem (K∞-Stage). Work primarily from the certified
  single-system data, taken as given, and record the dependency: the ball `eball 3`, its effects, its automorphisms.

**Nodes** (depth-first; decisive first; refine as you go):
- **S2.1 Data and construction.** Specify a pair system generated from data:
  - single-system preparations and effects;
  - single-system reversible operations — state exactly which (rotations; reflections);
  - the native pair operation `cnot`, and any other pair operation data;
  - product preparations, product tests, and tests generated from these by operations.

  Define the pair state space from the data (for instance, the completion of what is preparable at finite stages, with
  tests generated likewise), not chosen as a cone. State every choice the construction makes.
- **S2.2 Finite rank.** Which natural condition gives it? Candidates: local tomography with finite single-system ranks
  (`rank_pair + 1 ≤ (rank_A + 1)(rank_B + 1)`); finitely many independent tests; compactness. Give exact countermodels
  where a candidate fails.
- **S2.3 Local tomography.** Does it follow from a natural condition, rather than being built in by product-label-only
  constructions?
  - Candidates: every test is a product test preceded by available operations, with operations acting by a rule that
    does not presuppose local tomography; parameter counting; local discriminability [L, unverified].
  - Give exact non-locally-tomographic countermodels where a candidate fails.
  - Name every place local tomography is used.
- **S2.4 Native-gate compatibility.** Generativity (the gate is an available operation, so the generated body is closed
  under it) and its consistency (the generated tables stay valid). Which operation sets are consistent? The relation of
  generativity to `hgate`/`hinv` for the theorem's cone.
- **S2.5 What the generated systems are.** For each consistent construction:
  - compute exactly the generated state and effect cones;
  - say which theorem premises they satisfy (`hadm`, `hcl`, `hgate`, H/FCC).

  In particular: does any construction from data that excludes operation-level idle extension produce more than
  `K_gen`? If the gap from `K_gen` to Q3 can be filled only by local operations acting on entangled pair states, prove
  it as an exact obstruction for a stated class of constructions; otherwise give the construction that fills it.
- **S2.6 Generated effects versus full duals.** For each construction, compare the generated effect cone with
  `dualW` of the generated state cone. Determine which effect set the theorem's premises (`hadm` (b), FCC, the consumed
  (BD) instance) actually need. Cross-note to S3.
- **Flagged routes, analysed and classed but not used as premises.**
  - Local agency. Record exactly what it yields (IE1 by construction; with `cnot`, the cone Q3 [W + L]) and why it is
    excluded.
  - Frame covariance of the native gate. Establish or refute, exactly, whether it is equivalent to IE1 given `hgate`.

## Deliverables (each thread, in its own directory)

`RESULT.md`, with these sections:
- **0. Answer:**
  - per target, the label, whether the principle renames the target, and its strength relative to the target;
  - sufficiency proved kept apart from survives the countermodels;
  - two or three sentences on the owner's central question, as far as the thread reaches.
- **1.** Routes and countermodels, node by node, with verdicts.
- **2.** The ledger: every premise, classed [K]/[D]/[A]/[N], with anchors.
- **3.** The candidate table.
- **4.** Cross-thread notes.
- **5.** What is not claimed.
- **6.** The evidence log: every script with the sha256 of script and output, run count and replay status.
- **7.** Integrity: start and end checks.

Also `NOTES.md` (working notes, node log) and the scripts, with their `.out`/`.err` and replays.
