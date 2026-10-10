# PT — four parallel research threads on the missing premises of `kt4_forward_ie1` (research only; frozen at launch)

**Owner's direction (verbatim excerpts).**
> "I recommend opening four parallel research threads, each on its own branch and draft PR, starting from certified L
> `9f9f8257`."
> "All four remain research-only: no F designation, no governed round, no receipts, no changes to `main`, ROADMAP,
> manuscripts or established Lean results. No merge is authorized."
> "Each thread should report either a derivation, an exact counterexample, or a precise remaining gap. It must
> distinguish assumptions already certified on `main` from additional assumptions introduced by the proposed route."
> "The important point is that these threads do not need to succeed together. A counterexample in one thread may save
> substantial work in another."

The threads:
- **A — PAIR-COMP** (`pt/A/`): composite completion. Derive `hcl` without simply assuming P-STAGE2 or smuggling in K2.
- **B — PAIR-ACT** (`pt/B/`): gate preservation. Source `hgate` rather than restating it as P-ACT2; test whether a
  weaker condition than full `hgate` suffices.
- **C — FOUR-COMP** (`pt/C/`): four-copy coherence. Derive FCC, token clauses included, from a genuine composition
  principle, without operation-level idle extension.
- **D — NCLASS-ADM** (`pt/D/`): the smallest additional assumptions for `hcls` (N-CLASS) and `hadm` (admissibility).

Nothing here is adopted, frozen or governed. The coordinator (not a thread) audits each result, then publishes each
thread's audited outputs on its own branch and draft PR. Threads make no outward action of any kind.

## Base and inputs (read-only for every thread)

`pt/` below means `/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/pt/`.

- **Base:** certified `main` at L = `9f9f8257a980a1819fbbc1dc0019917cf8678626`, checked out read-only at `pt/base/`
  (a detached git worktree). Everything certified on `main` is read there:
  - the Lean sources `pt/base/verification/lean-mathlib/OIBridge/*.lean`, `pt/base/verification/lean-mathlib/OIBridge.lean`;
  - `pt/base/verification/ROADMAP.md`, `pt/base/papers/*.md`, `pt/base/book/*.md`;
  - the landed KT4-PREM-1 record:
    `pt/base/verification/programmes/oi-qm/reconstruction/round-kt4-prem-1-premise-audit/{preregistration,result}.md`,
    and its exact scripts `pt/base/verification/lean/kt4_prem1_probe.py` (every model: `M_Q`, `M_cl`, `M_max`, `M_D`,
    `M_refl`, `M_id`, `M_class`, `M_mix`, `M_int`, `M_tok`, `M_tokC`, the carrier, the dictionary) and
    `pt/base/verification/lean/kt4_prem1_indep_check.py`. **Start by reading `result.md` in full**: its source map
    (Q3), the pair-route gap (Q2), the dependency map and the four open questions define your problem.
- **The audited theorem's design modules** (kernel-checked in a design run, not certified, not on `main`), exported
  from `ff9c3a358c57ce938978f15f2915d2145ae7b4a5`: `pt/inputs/fourcopy/FourCopy*.lean` and that commit's
  `OIBridge.lean`. Definitions of `NClass`, `PairAdm`, `KT4Core`, `FourCopyCoherent`, `TokenCoherent`, IE1,
  `EvenCycle`, `kt4_forward_ie1`, Lemma B1 (`fourCopyCoherent_of_kt4Core`), Lemma R, `bell_mem`, `link_mem`,
  `bell_mem_dual`, `parity_witnesses` are there.
- **Prior research (audited; read as leads, re-verify what you use):** `pt/inputs/ledgers/` —
  `ASSUMPTIONS.md` and `DEPGRAPH.md` (USES vs SUPPLIES of the headline), `DEPENDENCY-MAP.md`, the EQ5-PREM and
  EQ5-SOURCE results, notes and audits (countermodels: the anchor sum, `M_ρ`, `M_tw`, `M_id`, `M_T`, the transposed
  factor model; `TokProdState`; STMC), `EQ4-AUDIT.md`, `EQ4-P-RESULT.md`, `EQ5-SIX-RESULT.md`, `EQ4-SIX-AUDIT.md`
  (the five-token pair network PN₅), `EQ3-*`, `EQ2-SYNTHESIS.md`, `INTEGRATION-DESIGN.md`, `K2-LEDGER.md`,
  `SA-LEDGER.md`, `KN-CENSUS-RESULT.md`, `K-INF-DESIGN.md`, `HINF-REVIEW.md`, `OISTAGE-RESULT.md` (the protocol tower
  as `DirectedStages`), `OPACT-RESULT.md`, `DRIVE-RESULT.md`. Where an audit corrects a result, the audit takes
  precedence. `pt/inputs/premise/` holds the premise and classification probes and their outputs.
- **Mathlib v4.33.0 source** (grep only): `/home/user/leanprover-community/mathlib4`.
- **Manifest:** `pt/inputs.manifest.sha256` (41 files).

## Vocabulary fixed by the landed record

- The audited theorem: for four pair cones `K_p ⊆ W 3` (`p = 01, 23, 02, 13`), `hcls ∧ hadm ∧ hcl ∧ hgate ∧ H ⇒ C`,
  with `C` = IE1 at every pair and `EvenCycle`. `H` is the `KT4Core` structure; under `hadm`, `H ⟺ FCC`.
- **P-STAGE2** — the pair system as a directed system whose completion has a chart onto `W 3` with chart body the
  normalized slice of `K_p`. **P-ACT2** — the gate `N_p` as an operation datum on that system with an inverse datum,
  inducing `N_p` on the chart. Both are named in `result.md`; assuming either for the premise it delivers is a
  restatement, not a derivation.
- **K2** — the open composite obligation of the ROADMAP (two-copy local tomography; the pair as a coordinate-model
  composite in `W 3`). It may be used only as a named additional assumption, never silently, and every result that
  uses it is stated as conditional on it.

## Shared rules

**Claims (owner's P/A/C rule).**
- `P ∧ A ⇒ C` is sufficiency. An exact model of `P ∧ ¬C` shows only that P alone does not give C. Necessity of A
  relative to P needs a proof of `P ∧ C ⇒ A`. Never write "required" or "necessary" without that proof.
- §A.34: every displayed equivalence carries a separately identified witness for each direction.
- **Certified versus added.** Every route carries a ledger with one row per premise it uses, classed:
  - [K] certified on `main` at L: a landed kernel identifier, `file:line` in `pt/base/`, with an exact statement match
    (give the diff if not exact);
  - [D] design-run only (the FourCopy modules at `ff9c3a35`): kernel-checked in a design run, not certified;
  - [A] adopted posit or recorded premise (ROADMAP/manuscript anchor and its recorded status);
  - [N] new additional assumption introduced by the route, stated precisely, with an independence assessment: is it
    independently motivated, or the target restated in other words? A restatement is a relabelling, not a source.
- **Test against the countermodels first.** Every proposed implication "candidate ⇒ target" is tested against every
  relevant exact countermodel (the landed models; the EQ5 models; any you build) before a derivation is written. An
  implication is refuted if a model satisfies the candidate and violates the target.
- **Forbidden as premises** (flag any route that uses one): IE1, IE2, the quantum cone `Q3`/PSD as a premise, the
  complex region tower, an operation on part of a larger composite (an (o) step), operation-level idle extension, and
  the thread's own target in other words. If a further principle is genuinely needed, name it as an [N] candidate and
  report every result that uses it as conditional on it.

**Evidence tags:** [K], [D] as above; [X] exact computation in your directory, replayed byte for byte; [W] written
argument; [E] exact exploration (a lead); [F] floating-point exploration (certifies nothing); [L, unverified] literature
not read at the source.

**Scripts.**
- Exact arithmetic only for anything certified (`fractions`, `sympy` with rationals). Run as `python3 -I -B`.
- State the decision rule in the script header before the first run, as rules, not expected numbers.
- A VERDICT line prints only over green controls; every favourable check has a countercontrol that must fail.
- No wall-clock time or other nondeterministic value in stdout (timings, if any, to stderr).
- Keep failed runs as `.runN.*`; record pre-run edits. Replay every certified script at the end; it must be
  byte-identical; record sha256 of script and output.
- Lean: there is no Lean toolchain here, so any Lean text you write is UNBUILT and labelled so. No CI.

**Integrity.**
- At start and end: `cd pt && sha256sum -c --quiet inputs.manifest.sha256`; `git -C pt/base rev-parse HEAD` must be
  `9f9f8257a980a1819fbbc1dc0019917cf8678626`; `git -C pt/base status --porcelain` must be empty. Write
  `.start_marker` in your directory with the start checks' output.
- Write only inside your own thread directory. Never modify `pt/base/`, `pt/inputs/` or another thread's directory.
- Read-only git commands only (`git -C pt/base log|show|grep|ls-files`). Never run a git command that writes
  (checkout, commit, worktree, fetch, stash, reset, branch, tag, gc, push).
- If anything you did not write appears in your directory, stop substantive work, record it (path, hash, mtime) in
  `INTEGRITY.md`, move it to `quarantine/` in your directory unchanged, and continue only after recording (§A.26).

**Limits.** No git writes, branches, pushes, PRs, CI or GitHub access. Do not spawn agents. Network egress is
restricted: do not route around it; mark literature [L, unverified].

**Investigation mode:** §A.31, gem-finding, depth-first.
- Number the branch nodes; select the decisive branch at each level; record a verdict at each node, closed by an
  explicit check (code, algebra, citation).
- Apply maximum skepticism to every branch whose outcome favours the framework; pressure-test the favourable reading
  before accepting it.
- **Productivity test** (fixed now): a finding is a gem iff it is (1) an exact certificate (derivation with every step
  checked, or an exact countermodel) at a stated instance, (2) an exact obstruction for a stated class of routes, or
  (3) an exposed hidden assumption. Otherwise it is record-only.
- Fixed point: stop after 3–4 consecutive passes with no NEW finding, or when the thread's question is answered.

**Outcome classes** (each a successful outcome):
- **DERIVED-ON-MAIN** — the target follows from [K] premises alone (plus [W]/[X] steps).
- **DERIVED-CONDITIONAL** — the target follows from [K] premises plus named [N]/[A] premises; each is stated precisely,
  classed independent or restatement, and tested against the countermodels.
- **COUNTEREXAMPLE** — an exact model of the route's stated premises (or of everything certified on `main` that bears
  on the target) in which the target fails.
- **GAP** — the precise missing link, sharpened beyond the landed record's statement.

## Thread A — PAIR-COMP: composite completion (`pt/A/`) — highest priority

**Question.** Construct a directed system for two balls and determine whether its completion naturally produces a
closed pair-state space in `W 3`. Goal: derive `hcl` without simply assuming P-STAGE2 or smuggling in K2.

**Facts to start from** (re-verify): the landed completion layer is typed for one directed system:
`StageCompletion.body` is the closed convex hull of the preparation vectors (`body_isClosed`); an operation datum with
an inverse datum induces a body-preserving equivalence of the chart (`preservesBody_inducedEquiv`); the only
`DirectedStages` values at L are `badD`, `bitTower`, `midD`; COMP-1 places the stage-level product of two directed
systems outside its module. Q2 of `result.md`: the normalized slice of `K_cl` is a COMP-1 `Composite` whose body is not
closed and which `cnot` preserves, so COMP-1's composite interface alone does not give `hcl`.

**Nodes** (depth-first; decisive first; refine as you go):
- A1. The stage-level product. Define the product of two `DirectedStages` at the stage level (preparations, effects,
  stage maps, the laws). State every choice the definition must make (which joint preparations exist at a stage: only
  products of the factors' preparations? products closed under joint operations? mixtures?). Check the laws exactly
  where they are finite.
- A2. Its completion. Determine the completed body for each choice in A1, exactly on the d = 3 ball instance: is it
  closed (in the completion, and after any chart)? Which cone is it (the closed hull of the products, `Q3`, something
  else)? Is it invariant under the native gate? Which choice, if any, is not a disguised P-STAGE2?
- A3. The chart onto `W 3`. What does identifying the completion's state space with `W 3` require (product effects
  separating pair states: local tomography, K2)? Is any of it certified at L? Can a chart exist without local
  tomography, and does closedness survive the passage from the completion to the image in `W 3` (images of closed
  sets need not be closed; state exactly what is used, e.g. a compact base)?
- A4. `M_cl`. Show exactly which feature of the construction excludes `K_cl` (or that none does). Conversely, decide
  whether the theorem's `K_p` is identified with a completed body by the construction or by an extra identification
  principle; name that principle and test it against `M_cl` and `M_int`.
- A5. Ledger and independence: classify every premise of the route ([K]/[D]/[A]/[N]) and decide whether any [N]
  principle is independently motivated (e.g. "the pair state space is the closure of what is preparable at finite
  stages") or P-STAGE2 restated.

## Thread B — PAIR-ACT: gate preservation (`pt/B/`)

**Question.** Investigate whether an observer-native reversible operation induces a valid operation on the composite,
and whether a weaker condition than full `hgate` suffices. Goal: source gate preservation rather than restating it as
P-ACT2.

**Facts to start from** (re-verify): `hgate` is not necessary (`M_max`) and cannot be dropped (`M_D`); the design
proof uses it at product states (`bell_mem`, `link_mem`) and, through Lemma R, for the inverse gate (`bell_mem_dual`,
`parity_witnesses`); `cnot` preserves neither `ball3MinComposite` nor `ball3MaxComposite`; idle extension of one-copy
data is IE1 itself for local rotations and fails for `reflY` on every `cnot`-invariant candidate cone
(`no_candidateCone_cnot_reflY`); an operation datum carries preparations into the completed body (`OpDatum.mem_body`),
so P-ACT2 states gate preservation on preparations.

**Nodes:**
- B1. A weaker clause. From the design modules, list every use of `hgate` and `hinv` on the proof path, with the exact
  instances used. Formulate the weakest clause the proof actually consumes (open question 1 of `result.md` proposes one
  stated at product states, with the Bell table in the dual of `K_p`). Decide, exactly: does it hold in `M_max`? does
  it fail in `M_D` (it must, or it does not suffice)? Does the theorem hold with it in place of `hgate` (proof route,
  UNBUILT Lean if useful), or is there a countermodel?
- B2. Sources. Candidates (not limited to): COMP-1 `JointReversible`/`PreservesBody`; OPACT-1's operation datum and
  completion action; the K1 premises (`IsNot`, `CtrlGate`, the entangling clause); EFF-1 / K1-BRIDGE-1 availability;
  physical reversibility of the native gate as an operation on the pair system with an inverse. For each: state it
  precisely, class it, and test "candidate ⇒ `hgate`" and "candidate ⇒ the B1 clause" against `M_D`, `M_max`, `M_int`,
  the landed min/max composites with `cnot`, and any model you build.
- B3. Restricted idle extension: does an idle extension restricted to the native gate, or to product states, evade the
  recorded obstruction without circularity (IE1, (o) steps)?
- B4. For each survivor: a written derivation with exact ingredients, and the independence assessment (P-ACT2 restated
  or not).

## Thread C — FOUR-COMP: four-copy coherence (`pt/C/`)

**Question.** Investigate whether consistent composition across four systems implies FCC, including the token
compatibility conditions. Goal: derive the four-copy premise from a genuine composition principle, without assuming
operation-level idle extension.

**Facts to start from** (re-verify): under `hadm`, `H ⟺ FCC` (Lemma B1 one way, the explicit carrier the other); the
token clauses cannot be dropped (`M_tok`: `(Q3, Q3, Q3, twin)`, FCC fails at `−1/8` [F10]); the token clauses of a
given carrier are not necessary (`M_tokC`); EQ5-SOURCE: no statement with three or more tokens on `main`, and KT4
minus `tok` is vacuous (the anchor sum); EQ5-PREM: independent preparation, regrouping invariance and their relation to
`TokProdState`/`TokenCoherent`.

**Nodes:**
- C1. Make "consistent composition across four systems" precise: candidates include regrouping invariance
  (associativity/commutativity of composing four tokens), one four-token state space whose two bipartitions `01|23`
  and `02|13` are both composites of pairs, independent preparation, the one-body clause. Relate each, field by field,
  to `KT4Core` (`prod_mem`, `prodEff_effect`, `prodEff_apply`, bilinearity, `one_body`, `tokA`, `tokB`) and to FCC.
- C2. Test "candidate ⇒ FCC" and "candidate ⇒ tok" against `M_tok`, `M_tokC`, the anchor sum, `M_ρ`, `M_tw`, the
  transposed-factor model, and PN₅ where relevant.
- C3. The mixed assignment `(Q3, Q3, Q3, twin)`: which composition principle excludes it, exactly? Is it a consistency
  condition (e.g. one pair type across bipartitions) or something stronger?
- C4. For each survivor: a written derivation with exact ingredients, and the independence assessment (a principle
  that only says "a four-copy carrier exists" restates `H`).

## Thread D — NCLASS-ADM: remaining premise sources (`pt/D/`)

**Question.** Investigate whether the native controlled-gate conditions yield N-CLASS, and whether the composite
interface supplies admissibility. Goal: identify the smallest additional assumptions required for `hcls` and `hadm`.

**Facts to start from** (re-verify): the source map's rows for `hcls` (`nativeGate_cnot`, `CtrlGate`,
`dim_of_ctrlGate`, `three_of_ctrlGate`; the K1 inputs `IsNot`, `CtrlGate` and the entangling clause are open premises of
ROADMAP row K1; `M_refl` cannot-drop, `M_id` not-necessary) and for `hadm` (`prodState_mem_maxCone`; COMP-1
`PreComposite`, `subset_maxBody`; K2-GUARD-1 `CandidateCone`; the coordinate-model presupposition K2; `M_class`
cannot-drop, `M_mix` not-necessary).

**Nodes:**
- D1. N-CLASS. From `NClass` in the design modules and DIM-1's native-gate hypotheses at L: does every gate meeting the
  landed native-gate hypotheses at `d = 3` have N-CLASS form? Either a derivation, or an exact gate meeting every
  landed hypothesis that is not N-CLASS (check `M_refl`'s gate first). Name the smallest additional assumption, and
  whether it is one of the K1 inputs or new.
- D2. Admissibility, clause by clause: product states in `K_p`; `K_p ⊆ maxCone (eball 3)`; `K_p` a convex cone. Which
  clause does each landed fact supply, under which presupposition (the coordinate model, K2)? Test against `M_class`
  and `M_mix`. Name the smallest additional assumption per clause.
- D3. Dependencies: does any route for `hcls` or `hadm` use `hgate`, `hcl`, IE1 or the target, directly or through a
  landed lemma's hypotheses?

## Deliverables (each thread, in its own directory)

- `RESULT.md`:
  0. Answer: the outcome class per target, the instance, and the named premise(s) or gap — in two or three sentences.
  1. The route(s) and countermodel(s), node by node, with verdicts.
  2. The ledger: every premise used, classed [K]/[D]/[A]/[N], with anchors; certified versus added kept separate.
  3. The candidate table: candidate, statement, class, implication tested, verdict per countermodel, independence.
  4. Cross-thread notes: anything that bears on another thread's target (a counterexample, a shared assumption).
  5. What is not claimed.
  6. Evidence log: every script with sha256 of script and output, run count, replay status.
  7. Integrity: start and end checks.
- `NOTES.md` (working notes, node log) and the scripts with their `.out`/`.err` and replays.
