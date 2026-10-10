# PT integration review — the missing premises of `kt4_forward_ie1`

Research only, from certified `main` at L = `9f9f8257`. Protocol and amendments 1–2 applied. Nothing here is adopted,
frozen or governed, and no branch, PR, CI run or repository change was made.

Inputs: the four thread results and the coordinator's audits.

| thread | RESULT.md (sha256) | audit |
|---|---|---|
| A | `b39eedca…` | `audit/A/AUDIT-A.md` |
| B | `acd8b8a1…` | `audit/B/AUDIT-B.md` |
| C | `1fe5af4c…` | `audit/C/AUDIT-C.md` |
| D | `0207e264…` | `audit/D/AUDIT-D.md` |

Every thread script replayed byte for byte in a fresh directory. Each audit has an independent exact check written
without thread code:
- A: 7/7;
- B: 16/16, plus a census scan;
- C: 33/33;
- D: 16/16.

Two of my own runs failed on harness errors (D run 1; B runs 1–2). They are kept and recorded, and none bore on a thread
claim.

Evidence levels are kept apart:
- **[K]** certified at L;
- **[D]** kernel-checked in the design run `ff9c3a35`, not certified;
- **[W]** written argument;
- **[X]** exact computation, scoped to the instance it checks;
- **[L]** literature;
- **UNBUILT** — Lean text never compiled.

**Labels (amendment 2).**
- A target is **DERIVED** if certified premises suffice.
- It is **CONDITIONAL** if sufficiency is proved from a named principle that is independently motivated and not a
  restatement.
- It is **INDEPENDENT** if a valid countermodel satisfies every certified premise that bears on it.
- Otherwise it is **UNRESOLVED**.

Independence from the certified base is reported in its own column, whatever the label. Every INDEPENDENT below means
independent of the premises certified at L as stated, not of every extension of the framework.

The audited theorem (design-run [D], not certified):
`hcls ∧ hadm ∧ hcl ∧ hgate ∧ H ⇒ (∀p, IE1 K_p) ∧ EvenCycle`, with `H ⟺ FCC` under `hadm`.

## 0. Bottom line

1. **The framework can construct a two-system composite. It cannot yet construct the quantum one.**
   - Thread A shows the narrow product of two one-ball directed systems is DERIVED: closed, finite rank, locally
     tomographic by construction. So is its closure under `cnot`.
   - Their cones are `SEP` and `K_gen = SEP + cnot SEP`. `K_gen` satisfies every per-pair premise: `hcls`, `hadm`,
     `hcl`, `hgate`.
   - With uniform `K_gen` it fails four-copy coherence (−1/8 at A's witness, −1 at C's) and IE1, because it misses the
     locally rotated Bell states.
   - The quantum cone `Q3` is exactly the closure of `K_gen` under local rotations [W + L, Schmidt decomposition].
   - So the distance from the native construction to quantum theory's composite is idle extension of local rotations.
     The audited theorem obtains it from four-copy coherence and the per-pair premises.
2. **Some properties must, on present evidence, remain independent principles.** Of the five premises:
   - one reduces to premises the project already records (`hcls` → K1's gate premises): CONDITIONAL;
   - one has an independently motivated equivalent (FCC ⟺ regrouping invariance of a four-token composite):
     CONDITIONAL, with equal strength;
   - three are INDEPENDENT with only restating sources (`hadm`, `hcl`, `hgate`).

   The three per-pair premises together say one thing in the certified vocabulary [W, assembled from audited parts]:
   *the two balls form a compact COMP-1 pre-composite whose body the native gate preserves*.
3. **K2 is mapped, not resolved.** No K2 obligation is discharged at the certified level. On the `d = 3` KT(4) route,
   the composite cone is pinned to `Q3`, with IE1 and EvenCycle, conditional on:
   - three structural principles (§3);
   - local tomography, which is still encoded in the `W 3` carrier;
   - a [D] theorem;
   - a [W + L] classification.

   The derivation of those principles from observer-native data is UNRESOLVED. It is not INDEPENDENT: L does not
   define the objects (an OI-native pair system, three or more tokens) that could carry them.

## 1. Per thread (A first)

| | strongest result | certified assumptions used | added assumptions that remain | explain or restate |
|---|---|---|---|---|
| **A** PAIR-COMP | (A-i) completion DERIVED for constructed systems: closed in ℓ^∞ (`body_isClosed`), finite rank, compact read-out; local tomography by construction (named). (A-ii) `hcl` for the theorem's `K_p` INDEPENDENT, by `M_cl` read out of a valid infinite-rank `D_cl`. Exposed: the closedness content is **finite rank of the pair completion**, not completion and not local tomography. | `DirectedStages`/`SCInf`/`FiniteStage`, `body_isClosed` [K]; `FiniteRank` (definition only) [K]; COMP-1 [K]; `cnot_prodState_mem_maxCone` [K]; the audited theorem [D] | FiniteRank of an OI-native pair completion (K∞-Stage, open), and ID: the theorem's cone is that completion's read-out | FiniteRank **explains** closedness (compact body ⇒ closed cone). ID **restates** `hcl` relative to `hadm` (both directions proved), as do P-STAGE2, twisted self-duality and no-restriction |
| **B** PAIR-ACT | `hgate` INDEPENDENT (`M_max`, `M_D13`; all 13 certified items checked; census complete). Weaker consumed clauses CONS, OQ1, SECT ⟺ GT-COMP and PREC suffice [W over D; UNBUILT], are strictly weaker (`M_pre`, `M_DD`), and are INDEPENDENT. Lemma O: no σ-invariant clause both suffices and holds in `M_max`. Exposed: `hgate` constrains the pre-locals, which C never reads. | K1 predicates (`NativeGate`, `CtrlGate`, `GateRel`, `Entangling`, `…Of`) [K]; COMP-1 `JointReversible`/`PreservesBody` [K]; OPACT-1 `OpDatum`, `preservesBody_inducedEquiv` [K]; K2-GUARD-1 [K]; design lemmas [D] | `hgate`, or the weaker CONS | every source found **restates** `hgate` (JR/PreservesBody of the pair slice, P-ACT2, reversibility on the pair state space) or is forbidden (gate-factor idle extension) |
| **C** FOUR-COMP | FCC from N0 ∧ N1 ∧ N2 (four-token carrier, one body, TokProdState), sufficiency proved [W + X; Lemma B1 D]. Converse via MSIG: `∃V.(N0∧N1∧N2) ⟺ FCC` under `hadm`. Token clauses from N2 alone. On {Q3, twin}⁴, FCC holds exactly at the 8 coboundary patterns. | COMP-1 `ProductData`/`PreComposite` [K, CI:210–230]; `exists_effect_rescale` [K]; the `W 3` typing; Lemma B1 [D] | N0 ∧ N1 ∧ N2, regrouping invariance of a four-token composite | **explains without reducing**: stated with no cone, inequality, operation or local tomography, but of exactly FCC's strength over carriers |
| **D** NCLASS-ADM | `hcls` from K1's gate premises (unit corner axis, CNOT frame, two-sided product positivity), T1 [W + K + X; UNBUILT]; `N-CLASS ⟺ P± ∧ frame` up to local frames, both directions; T2: orientation is a gate invariant. `hadm` (a), (b), (c) each INDEPENDENT; T3: `hadm ⟺` product-test cone of a COMP-1 pre-composite of two balls, no `lt` needed. | `corner_form`, `lor_cornerMap`, `tens_hom_inj`, `lor_of_forall_pair` [K]; `ctrlGate_of_nativeGate` [K]; `cnot_frame` [K]; COMP-1, `paddedBall3` [K] | K1's gate premises (recorded, unsourced) for `hcls`; the three `hadm` clauses | `hcls`: **explains** (N-CLASS adds exactly a classical CNOT frame to two-sided positivity). `hadm`: **restates** (independent preparation, validity of product tests, mixing closure) |

Audit corrections:
- **C's tree obstruction B3** holds for conditions on cones and gate *maps*. It fails as stated for conditions that may
  read the supplied locals: two chart-invariant 3-pair conditions on the post-local determinants imply EvenCycle, and
  with "each cone is Q3 or twin" they imply FCC [X + W]. C's own conclusion (B5, about pair *cones*) is unaffected.
- Otherwise none. D's `M_refl`, B's `M_pre` and Lemma O, and the B3 correction share one theme: the theorem's supplied
  locals carry a chart trivialization, and EvenCycle is a property of the gates (T2).

## 2. Property by property

| property | vs certified L | best sufficient principle | explain / restate | label | evidence |
|---|---|---|---|---|---|
| pair completion closed, finite rank (constructed systems) | follows | the construction itself | — | **DERIVED** (for the constructed systems) | [K + W]; UNBUILT Lean; [X] finite instance |
| `hcls` (N-CLASS gate form) | independent (`M_refl`: gate premises hold, supplied locals not a decomposition) | K1 gate premises ⇒ ∃ N-CLASS form (T1); locals by choice (T2) | explains | **CONDITIONAL** | [W + K + X]; UNBUILT |
| `hadm` (a) products in K | INDEPENDENT (`M_class`) | independent preparation | restates | **INDEPENDENT** | landed + [X] |
| `hadm` (b) K ⊆ maxCone | INDEPENDENT (uniform `W 3`) | validity of product tests | restates | **INDEPENDENT** | [X + W] |
| `hadm` (c) convex cone | INDEPENDENT (scaled `cnotOrbit`) | mixing closure + cone convention | restates | **INDEPENDENT** | [K + X] |
| `hcl` closed cone | INDEPENDENT (`M_cl` via `D_cl`) | FiniteRank + ID | ID restates | **INDEPENDENT** | landed + [X] + [W] |
| `hgate` gate preserves K | INDEPENDENT (`M_max`, `M_D13`) | JR/PreservesBody, P-ACT2 | restates | **INDEPENDENT** | landed + [X] + [K] |
| CONS (weakest sufficient gate clause) | INDEPENDENT | — | none found | **INDEPENDENT** | [W over D]; UNBUILT |
| FCC (⟺ H under `hadm`) | INDEPENDENT (`M_tok`, `K_gen`) | N0 ∧ N1 ∧ N2 | explains, equal strength | **CONDITIONAL** | [W + X]; B1 [D] |
| token clauses `tokA`, `tokB` | independent (`M_tok`) | N2 (TokProdState) | explains | **CONDITIONAL** | [W + X] |
| local tomography of the pair | INDEPENDENT of the COMP-1 fields (landed `paddedBall3`) | encoded by the `W 3` typing | — | **INDEPENDENT** | [K] |
| IE1 and EvenCycle (conclusion C) | fails in `K_gen`, `M_tok`, `M_D` | the five premises | — | **CONDITIONAL** on the five premises | [D] |
| composite cone = Q3 (instance: `d = 3`, `cnot`, identity locals, uniform cone) | — | the five premises; the models without `hcl` are the cnot-invariant convex cones between `K_cl` and Q3, so `hcl` forces Q3 | — | **CONDITIONAL** | [D + W + L]; not kernel-checked |

The INDEPENDENT entries are not cheap in one respect: each countermodel also satisfies the theorem's other premises.
- `M_refl`: everything but `hcls`.
- `M_cl`: everything but `hcl`.
- `M_max`, `M_D13`: everything but `hgate`.
- `M_class`, uniform `W 3`: everything but one `hadm` clause.
- `M_tok`, `K_gen`: everything but H.

So, apart from `hadm` (c), whose countermodel does not claim H, no premise of the theorem follows from the others.

They are cheap in another respect: L defines no pair system at all, so no certified statement constrains any `K_p`.

## 3. Can the observer-native framework construct the composite quantum theory requires?

**What it constructs** (A, DERIVED). From two one-ball directed systems:
- the product completion, a closed, finite-rank, locally tomographic composite with cone `SEP`;
- its `cnot` closure, with cone `K_gen`;
- the dual `K_E`.

`K_gen` satisfies `hcls`, `hadm`, `hcl` and `hgate`. As a uniform assignment it fails FCC (−1/8 at A's witness, −1 at
C's) and IE1: `T_ψ = actT R_H phiW ∈ Q3 \ K_gen`. `SEP` fails `hgate`. `K_E` fails FCC (−1/2).

**What quantum theory needs.** The quantum composite is `Q3`. It is the smallest local-rotation-invariant cone
containing `K_gen`, because every pure two-qubit state is a local-unitary image of a `cnot` image of a product [W + L].
The theorem derives exactly that closure (IE1) from FCC and the per-pair premises, together with the orientation
parity. On the instance, with `hcl`, it pins the cone to `Q3` [D + W + L].

**What must be added.** On present evidence, these remain principles. Each is INDEPENDENT of the certified base, and
none is DERIVED.

| principle | content | covers | status of its source |
|---|---|---|---|
| **S1 Gate** | the native pair gate meets K1's gate premises: unit corner axis, CNOT frame, two-sided product positivity | `hcls` (T1, T2) | already recorded as K1 premises, unsourced |
| **S2 Pair** | the normalized slice of `K_p` is the body of a **compact** COMP-1 pre-composite of two balls on the table carrier, and the native gate **preserves** it in both directions | `hadm ∧ hcl ∧ hgate` [W, assembled: D T3 (model pre-composite, `q = id`); A W-A3.1/ID and the bound `\|ω_μν\| ≤ ω₀₀` on maxCone (closed ⟺ compact slice); B B2.2 with Lemma R, relative to `hcls`] | restating sources only. The non-restating route would be an OI-native pair system (not defined at L) with FiniteRank (K∞-Stage) and reversible operation data (K∞-Act): UNRESOLVED |
| **S3 Four tokens** | the four tokens compose into one regrouping-invariant system (N0 ∧ N1 ∧ N2) | FCC ⟺ H | independently motivated equivalent. L has no structure with three or more tokens: UNRESOLVED whether the framework supplies it |
| **LT** | two-copy local tomography | encoded by `W 3`; consumed at the gate-descent interface (B, D) | K2 obligation, open. Not needed by `hadm`, by closedness or by FCC beyond the typing (A, C, D) |

**So the answer to the question.** The framework constructs a composite. The properties that make it the quantum one
must, on present evidence, remain independent principles:
- the compact, gate-reversible pair structure (S2), which in present terms is K2's composite cone with compatible
  actions, stated in COMP-1 vocabulary;
- four-token regrouping invariance (S3).

The gate form (S1) is not new: it is K1's. Whether a future observer-native pair or four-token system would *derive* S2
and S3 is **UNRESOLVED**, not INDEPENDENT. Present independence is relative to a base that does not define those
systems.

## 4. INDEPENDENT versus UNRESOLVED

**INDEPENDENT** (valid countermodels to the premises certified at L):
- `hadm` (a), (b), (c);
- `hcl`;
- `hgate` and its weaker consumed clauses;
- FCC and H;
- local tomography relative to the COMP-1 pre-composite fields.

**UNRESOLVED** (no derivation, no countermodel; the objects are not defined at L):
- **U1.** An OI-native two-ball pair system (for example a protocol tower) and whether it is a COMP-1 pre-composite.
- **U2.** FiniteRank of its completion (K∞-Stage), the non-restating source of `hcl`.
- **U3.** A non-restating source of the gate's action on the pair: K∞-Act on a pair system restates `hgate` given
  P-STAGE2. Lemma O requires any sufficient clause that holds in `M_max` to read the post-local orientation.
- **U4.** Whether the framework supplies regrouping invariance. It needs three or more tokens.
- **U5.** The sources of K1's gate premises (`IsNot`, `NativeGate`, `Entangling`).
- **U6.** A derivation of local tomography.
- **U7.** Kernel status of the route itself:
  - the audited theorem, Lemma B1, `NClass`/`orient` [D];
  - T1, T2, T3, C's A2 route, B's CONS replacement and A's closure form (UNBUILT or [W]);
  - the classification `P ∧ IE1 ⇒ {Q3, twin}` [W + L].

## 5. How much of K2 is resolved

ROADMAP K2 (OPEN) lists: local tomography; the composite cone; local actions compatible with it; the formal
composition theorem; the antiunitary and complete-positivity bridge; the relation to K3.

| K2 obligation | status after PT |
|---|---|
| local tomography | **open, scope narrowed**: not consumed by `hadm`, by closedness or by FCC beyond the `W 3` typing; consumed where a gate on a carrier must descend to tables |
| composite cone | **reduced, not discharged**: on the `d = 3` instance it is Q3, CONDITIONAL on S1–S3 and local tomography [D + W + L]; S2 and S3 are not derived |
| local actions compatible with it | **reduced**: IE1 is the theorem's conclusion, CONDITIONAL on the five premises [D]; IE₂ open |
| formal composition theorem | **not addressed**: the route is [D], UNBUILT or [W]; no governed round |
| antiunitary / CP bridge | **not addressed**: the Q3/twin (transpose) ambiguity persists in the classification |
| relation to K3 | **not addressed** |

**Assessment.** None of K2 is resolved at the certified level. What the threads resolved is the logical structure of
K2's core on the one route that reaches the quantum cone: every premise is located, its independence from the
certified base is proved, and its weakest known sufficient form is identified.
- The natively constructible composite and the quantum one differ by exactly IE1.
- FCC is the premise that supplies IE1 against the native construction.
- That premise has a physically motivated equivalent: regrouping invariance.

This is consistency-axis work, and bands are unchanged.

## 6. What remains for full finite-dimensional operational quantum mechanics

1. **K2 at `d = 3`.**
   - Source S2 and S3 from observer-native constructions, or adopt them as named principles. Sourcing requires
     defining an OI-native pair system and four-token systems.
   - Derive or adopt local tomography.
   - Certify the route: the theorem, B1, T1–T3, the A2 route and the CONS replacement in the kernel, and a kernel proof
     of the classification.
   - The antiunitary/CP bridge (the transpose ambiguity) and the relation to K3.
2. **Beyond two elementary systems.**
   - IE₂, three-token structure, KT(n) for n ≠ 4, the grouping 03|12.
   - The multi-party state space: on uniform Q3, N0–N2 do not force the four-token body to PSD₁₆ (MSIG and PN₄ are
     other models).
3. **K1.** The dimension is CONDITIONAL on unsourced gate premises. S1 inherits them.
4. **K∞.** The field-neutral seams (Stage including FiniteRank, Act, Drive, Trans, Seed, V4, Copy, Geom) are all
   unsourced. S2's non-restating route runs through Stage and Act.
5. **Kₙ.** The lift from elementary systems to arbitrary finite carriers is open. K2's route composes elementary
   systems only.
6. **K3.** It is CONDITIONAL on complex matrix kinematics at every finite size. Reaching Q3 for two qubits is a step
   toward it, not the hypothesis it needs.
7. **H-Bell.** K2 does not discharge it.
