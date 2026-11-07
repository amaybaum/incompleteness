# MECH-1: native reciprocity as a selection of quantum-compatible operations, and the control it excludes

**Standing.** Paper-only research unit under #1169. Author: Claude Code session,
2026-11-07. Scope: [owner authorization](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6714000230)
and [research question](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6713955150),
with the owner addendum of 2026-11-07 (composition and changed-measurement
tests; the three shortcut checks of §4) relayed by the coordinator in this
session. This file proposes no premise for adoption and promotes no claim. No
simulation, enumeration campaign, Lean build, V3 execution, manuscript change,
freeze, dispatch or merge is part of it. Small exact or floating-point checks of
this file's own algebra were run as author self-checks (§9). They are controls
on that algebra, not evidence, and no verdict rests on them.

**Source snapshot.** Every repository link is pinned to `main` at
`313a93efcab581465919a4ff82ecda1e4b81e990` (cited as `main@313a93ef`), which
contains apparatus-1 (#1183), Q-A (#1184) and the Q-A forward repair and
feedback result (#1189). Abbreviations: **AP1** =
[apparatus-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md);
**QA** = [Q-A DESIGN](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md);
**PR-QA** = [Q-A PROOF-RECOVERY](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/PROOF-RECOVERY.md);
**FB** = [feedback RESULT](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md).

## 0. Result

1. **Where the monomial obstruction sits (§1).** On the physical carrier every
   deterministic bijective apparatus lies in `permClass` (AP1 Lemma 2), whatever
   its dynamics. Non-monomial behaviour can only appear on an encoded carrier.
   There the native reads are already phase-sensitive (AP1 §4.4). What is missing
   is a reversible encoded operation that is non-monomial **and** completely
   positive. On the native `F_2` alphabet the three existing results locate the
   failure: no encoded `S` under the one-cell frame (AP1 Lemma 5); with a
   same-sublattice coupling (NNB) `S` appears together with encoded reflections
   (QA Lemma R); and reflections are forced for uniform linear qubit encodings
   with available translations, adaptive protocols included (FB).
2. **Selected lead (§1.4).** The characteristic of the native alphabet. The native
   step is symplectic with multiplier `+1` because the coupling is symmetric
   (reciprocity). Over `F_2`, `+1 = −1`, so symplectic and anti-symplectic maps
   coincide and reciprocity cannot separate rotations from reflections. Over an
   odd prime alphabet `F_q` they differ. The question is whether, at odd `q`,
   reciprocity excludes non-quantum operations by itself.
3. **Selection (§3, nodes 2–4).** At odd prime `q`, under Gross's
   Clifford-covariant phase-space identification R-W (a fixed mathematical
   representation, §2.1):
   - **Theorem W.** Every protocol of the native class N, adaptive protocols,
     recombination and NNB included, acts on the encoded carrier as a quantum
     stabilizer instrument. Every branch is CP, and every composition matches
     exactly.
   - **Proposition AS.** For an ontic bijection of the phase space, the encoded
     action is CP **iff** the bijection is affine symplectic.
   - The native rule (linear, A5; symmetric and center-free, A4) is affine
     symplectic, so the reflection-type operations are excluded by native
     structure, not by a rule defined from the target. At `q = 2` the same frame
     makes the native free tick itself a reflection (§3 node 2).
4. **Capability (§3, nodes 5–7).**
   - **Lemma S.** On a bipartite coupling graph, for every prime `q` and every
     process of N including record feedback, no functional mixing a cell's two
     slots is ever determined. Hence no encoded phase gate under one-cell frames:
     the reversible encoded operations stay monomial in the frame.
   - **Lemma N.** With NNB at odd `q`, an explicit word gives the single-cell
     phase gate `P` exactly, with the partner cell returned. Its composition
     battery (S∘S-type powers, the G2 sequence, repeated use with continuation,
     changed reads) matches the comparator. A measure-and-prepare imitation
     matches one step and fails the battery (CC-IMIT).
   - **Proposition C.** At odd `q` no protocol of N, with or without NNB,
     supplies the quarter phase, an infinite-order encoded unitary, or any
     Wigner-negative state. The encoded theory is the noncontextual qudit
     stabilizer theory.
5. **Physical source (§3, nodes 1 and 8).**
   - **Lemma A.** Under one fixed affine rule, a setting held anywhere in the
     state can only translate values. It cannot select which functional is read
     or the linear part of an operation.
   - **Theorem T.** At odd `q` under R-W, no fixed bijective rule both lets an
     in-world setting select a linear part and keeps a CP encoded action on all
     joint laws, controller included. A controlled coupling (non-affine) maps a
     reachable stabilizer state with an X-type controller to a non-quantum
     encoded state. The setting-selection obligation and the selection
     obligation are therefore in direct tension within this class.
6. **Qubits (§3 node 7).** FB's proof uses only that the encoded functionals are
   group homomorphisms to `Z_2`. It therefore holds for every finite abelian
   configuration group, including a `Z_4` alphabet. Uniform level-set qubit
   encodings exist exactly when that group has even order, and then the combined
   `S` + C-CP target fails. At odd order reciprocity supplies C-CP, but there is
   no qubit and no quarter phase.
7. **Outcome type (ii): stop (§6).** One obligation passes natively (selection,
   at odd `q`). Continuation passes under the carried-over posits. Capability
   needs NNB and stays inside the noncontextual stabilizer fragment.
   Physical-source setting selection fails. The smallest missing physical
   premise is **CTRL-REC**: an armable coupling whose coefficient is a fixed
   function of the registered slot of a terminal record cell. Theorem T shows
   why the controller must be confined to record laws. For the qubit quarter
   phase, no premise in this class supplies it (M3, open). No V3 round is
   proposed.

## 1. Locating the obstruction

### 1.1 The physical carrier

AP1 [Lemma 2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L153)
covers every apparatus that acts on a finite configuration set by bijections,
attaches fresh cells with fixed laws, discards by marginalization and conditions
on configuration records. Each branch of each such instrument is a sum of
conjugations by scaled partial permutations, which is
[`permClass`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L236).
Restricted to a finite cone, the kernel results
[`permTheory_not_control`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L708)
and [`permTheory_not_qm`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L717)
then apply by the monotonicity transfer of QA §4.1. This holds for **every** update
rule, linear or not, and for every alphabet. The premises that produce it are
three:

- (P-a) the operational state is a law on configurations;
- (P-b) every step is bijection-valued;
- (P-c) reads are of configuration functions.

The adjacent kernel audits agree.
[`ReadWriteControl.lean`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/ReadWriteControl.lean#L1)
names "an extended substratum with a genuinely continuous (non-bijective-valued)
coupling" as the open question, which is a change to (P-b).
[`ExecSource.lean`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/ExecSource.lean#L52)
and [`LiftSource.lean`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/LiftSource.lean#L251)
show that fractional-time layer flows need a non-monomial admissible operator,
and that the coherent and stochastic lifts are configuration-level.
[GR:270](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/GR.md#L270)
records the site-space wave-operator formulation as unresolved.

### 1.2 The encoded carrier

AP1 keeps (P-a)–(P-c) on the physical carrier and changes the
**identification**: a fixed, setting-independent map from laws on one cell to
states of `C²`, namely R1, the tetrahedral frame
([AP1 §4.2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L498)).
On that carrier:

- **Phase-sensitive instruments are native.** The native minimal read (a coupled
  tick with a half-known meter, then terminal registration) is the encoded `Z` or
  `X` Lüders instrument. Its `X` branch has Kraus operator `|+⟩⟨+|`, which is
  non-monomial in the `Z` basis.
- **Non-monomial CP reversible operations are missing.**
  - AP1 [Lemma 5](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L731)
    excludes encoded `S` under R1 by any stochastic map.
  - QA [Lemma G1](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L240)
    and [G2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L342)
    exclude it for non-adaptive processes on bipartite graphs under any
    encoding.
  - With NNB, QA [Lemma R](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L667)
    shows that `S` comes with two separately available encoded reflections.
  - FB [§§3–5](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md#L85)
    excludes the combined `S` + C-CP target for uniform linear encodings with a
    common lift and available translations, record feedback included.

All three results are stated over `F_2`. Each reflection in them is an encoded
map of determinant `−1` on the Bloch octahedron: the transpose class, which is
not CP.

### 1.3 What would have to change

| Premise | Change | Covered by |
| --- | --- | --- |
| (P-b) bijection-valued steps | Continuous or non-bijective coupling | `ReadWriteControl` open question; B1's E-real/E-control |
| (P-c) configuration reads | Reads of non-configuration observables | F2-1 A★ Θ-D, N8 (declared projectors fail its screen item 2) |
| Identification R1 | Larger or different encoded frame | AP1 §5.2 (P-8), QA (U′ and NNB) |
| Native alphabet `F_2` | Odd characteristic | AP1 §5.6 (expectation only), QA G1 (generation only, no C-CP) |
| Access P1–P3 | Changed registration, supply or arming | AP1 C3, C4, C9; QA Lemma Q |

### 1.4 Leads, dispositions and selection

| Lead | Prior coverage | Disposition |
| --- | --- | --- |
| Observer-level coarse-grained or traced description (Koopman, Fourier or Bogoliubov change of observable basis) | Main §3.2 [Lemma 2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Main.md#L306): the traced one-step channel of the native rule is a Clifford-conjugated mixture of Weyl operators, all monomial. LiftSource T3: the stochastic channel has monomial Kraus operators. F2-1 A★ [Θ-K, Θ-F](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md#L73); PC-F1 gauge control | Covered. A basis change is a frame change. Its usable part, a **fixed** encoded frame, is retained in the selected lead as a representation, not as a source |
| Fractional-time layer-flow access | [`obs_not_layerFlowExecutable`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/ExecSource.lean#L129); LiftSource T4; F2-1 [N4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md#L79) | Covered (kernel negative; executability is an added intervention) |
| Continuum or large-`q` limit with metaplectic quantization | F2-1 [N8](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md#L83); [interface source §4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md#L192), row L3; B1 | Partly covered. Its finite, exact form is the selected lead: at odd `q` the Weil (finite metaplectic) representation exists exactly, with no continuum or Hilbert-space premise. The continuum version is left to Q-B (§6.5) |
| Preparation-contextual or nonlinear encodings | Left open by FB §5 | Not selected. No physical lead for a contextual lift is in the corpus; node 7 sharpens what such a lead must break |
| B1 conditional two-mode mixing | [B1 §6](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-mode-drive.md#L124) (density-dictionary obstruction); its E-control is externally loaded | Covered. Lemma A (node 1) shows why its control cannot be internal under a fixed affine rule |
| **L-χ: alphabet characteristic and native reciprocity** | AP1 §5.6 states the odd-`q` stabilizer case as an expectation. QA G1 settles generation for non-adaptive bipartite processes. No record decides C-CP at odd `q`, and Lemma R, PR-QA and FB are all over `F_2` | **Selected** |

**Justification of the selection.**

- **Expected decisiveness.** The third obligation asks for an independently
  motivated structure that excludes reflections. The only native structure
  that distinguishes a rotation from a reflection in phase space is the
  multiplier of the symplectic form: `+1` for symplectic maps, `−1` for
  anti-symplectic ones. The native step has multiplier `+1` because the
  coupling is symmetric (AP1 §4.1:
  `[[A,−I],[I,0]]ᵀ Ω [[A,−I],[I,0]] = Ω` iff `A = Aᵀ`). Over `F_2` the
  distinction is empty. Whether it does the selecting at odd `q` is decidable
  by exact paper argument.
- **Independent motivation.** Neither ingredient is chosen for the target. The
  symmetric coupling is the native rule
  ([Substratum A4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Substratum.md#L98),
  [A5](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Substratum.md#L100);
  [SM form lemma](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L224)),
  and it is the same reciprocity that supplies the measurement backaction in
  SA-1. The alphabet size is a native parameter that OI does not fix
  ([SM §2.7](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L88)).
  No value of `q` is adopted here: §3 computes both characteristics.

## 2. Question, decision rule and controls

The decision rule, controls and countercontrols below are stated in the same
commit as the derivation of §3. Their priority over the result is not separately
recorded.

### 2.1 Target, comparator and identification

- **Comparators (imported, I1).** At `q = 2`: the single-qubit stabilizer
  subtheory, as in QA §1.1. At odd prime `q`: the stabilizer subtheory of
  `n` qudits of dimension `q`, meaning stabilizer states and their mixtures,
  Pauli (Weyl) reads with Lüders continuation, and the Clifford group. The
  comparators are definitions, not native postulates.
- **Identification R-W (mathematical representation).** For odd `q`, use
  Gross's phase-space point operators `A(λ)`, `λ ∈ F_q^{2n}`. Each cell's slots
  `(u, v)` are identified with Gross's (position, momentum) by one fixed
  symplectic convention, and the encoded frame is AP1's `J^{−t}` per cell. Since
  `J` is symplectic, Theorem 7 of Gross makes the choice immaterial for
  everything below. A law `μ` maps to `ρ_μ = Σ_λ μ(λ) A(λ)`. R-W is fixed for
  all settings, which is the PC-F1 requirement. At `q = 2`, R-W reduces to AP1's
  R1 tetrahedral frame (Wootters).
- **Gross's facts used (read first-hand, arXiv:quant-ph/0602001; odd `d`).**
  - (W1) The `A(λ)` have unit trace and are orthogonal with
    `tr A(λ)A(μ) = q^n δ_{λμ}` (Theorem 6.1).
  - (W2) Marginals over a Pauli level set are Born probabilities. Equivalently,
    each Pauli eigenprojector is `Π_{f=c} = q^{−n} Σ_{f(λ)=c} A(λ)` (Theorem 6.3).
  - (W3) Multi-cell `A` factor as tensor products (Theorem 6.4).
  - (W4) **Clifford covariance.** For affine symplectic `g = S· + a`, a unitary
    `U_g = w(a)μ(S)` exists with `U_g A(λ) U_g† = A(gλ)`. `μ` is the Weil
    representation, projective, which leaves conjugation channels unaffected
    (Theorems 3 and 7, Lemma 4).
  - (W5) **Discrete Hudson.** A pure state has a nonnegative Wigner function
    iff it is a stabilizer state (Theorem 2).
  - (W6) A unitary that keeps every nonnegative-Wigner state nonnegative is
    Clifford (Theorem 19).

### 2.2 The class

N is QA's class
([§1.2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L124)),
read over a prime alphabet `F_q`:

- second-order, linear, center-free, symmetric updates, either native or armed
  per tick and per edge under P3, with E-iso;
- P2 ready cells, each with one known slot whose value is supplied through
  H-PREP;
- P1 terminal registration;
- discarding;
- constant translations;
- record-conditioned armings and translations (adaptive).

N+NNB adds QA's armable same-sublattice symmetric coupling. The carried-over
posits keep their AP1 and QA classification as supplied
([ledger](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L411)).

### 2.3 The four obligations and their pass conditions

- **O1 Physical source.**
  - Pass iff the preparation, the receipt of a setting request and the operation
    are executed by one fixed rule.
  - The setting is held in the state, and the request is not loaded into the
    dynamics from outside.
  - Failures and records are part of the same dynamics.
  - A supplied posit (P3, H-PREP, P2) gives the verdict "supplied", not "pass".
- **O2 Quantum capability.** Pass iff some available reversible encoded
  operation is non-monomial in the frame **or** is the quarter phase. In
  addition, the operation must pass the composition battery C-COMP. A one-step
  averaged match is not a pass.
- **O3 Quantum selection.**
  - Pass iff every available encoded branch, and every coarse-graining of
    branches, has a CP extension (C-CP).
  - The exclusion of reflection-type maps must follow from a structure stated
    without reference to the comparator.
  - A rule that defines the operation set as "the quantum ones", or restricts
    resources only because an unwanted operation must disappear (QA premise I),
    is flagged by CC-RECON.
- **O4 Operational continuation.** Pass iff each operation has a derived
  complete instrument: success branches, the heralded failure branch, the
  retained records, the retained hidden information, and an outgoing state on
  which the next operation of the class acts with the comparator's statistics.

### 2.4 Controls and countercontrols

| ID | Requirement | Required outcome |
| --- | --- | --- |
| C-PH | Encoded quarter phase (`PhasesAvailable` transported) | Reported. Escape iff available |
| C-ROT | Encoded `rot`, or at odd `q` an encoded unitary of infinite order | Reported. Escape iff available. Every finiteness and measure hypothesis is named |
| C-CP | Per encoding: every available encoded branch is CP | Required for O3 |
| C-IS | AP1's per-state isotropy diagnostic | Diagnostic only. At odd `q`: whether reachable encoded states lie in the nonnegative-Wigner set |
| C-NS | No-signalling of complete local histories, wing-local operations | Required |
| C-LEAK | Two-system hidden-retention leak ([two-system §4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L241)), reuse and recombination | No protocol extracts information beyond the comparator |
| C-Q | QA Lemma Q parity protection, where relevant | Checked for whether it survives at odd `q` |
| C-COMP | Composition battery (below) | Required for O2 |
| CC-OFF | Mechanism off | (a) at `q = 2` the reflection must return; (b) with NNB removed, the phase gate must vanish |
| CC-IMIT | Classical statistical imitation | A hidden-variable model matching one-step statistics must fail C-COMP |
| CC-RECON | Reconstruction flag | Any operation set defined by the target is labelled a reconstruction, not physical sourcing |
| C-EX | §A.21 exactness | Each structural identity is checked together with a control that must break it |

**C-COMP (owner addendum).** The tests are applied to the candidate operation
`O`: `S` at `q = 2`, or the phase gate `P: (u, v) ↦ (u, v + u)` at odd `q`,
whose order is `q`.

- K1: `O∘O` on every encoded eigenstate family.
- K2: `O^m = I`, with reads.
- K3: G2's sequence `X_+ → O^{m−1} → X → O → X`, including the heralded-failure
  branch `R0` of the middle read.
- K4: repeated use with continuation: `O`, a read, `O` again, a read, for every
  read choice.
- K5: changed measurement choices: on one preparation, every available read axis
  after `O`.
- K6: the complete instrument, with every branch and the failure branch, never
  only a postselected success.

**Pass:** equality of the joint record laws with the comparator for **all**
finite sequences. This must be shown by an exact homomorphism or by induction
over a family closed under the class, not by checking finitely many sequences.

### 2.5 Shortcut checks (owner addendum)

- **SC-1, imported quantum behaviour.** Is a unitary, an interference mechanism
  or a CP restriction assumed rather than derived?
- **SC-2, hidden external control.** Does the construction rely on an outside
  agent selecting a coupling or preparing special inputs?
- **SC-3, representation versus physical implementation.** Does the
  non-monomial operation exist in the physical dynamics, or only in the
  observer's mathematical representation?

### 2.6 Decision rule

- **D0.** A failed C-EX or CC-OFF voids the verdict of the branch it controls.
  A candidate that passes only after the encoded operation set is restricted
  by reference to the comparator is labelled under CC-RECON.
- **D1.** Each obligation is decided in N first, then under the smallest single
  departure, which is stated as a conditional premise with what it preserves,
  what it buys and its independent consequences (§A.29).
- **D2.** O2 passes only together with C-COMP. CC-IMIT must fail C-COMP, or
  C-COMP is void.
- **D3.** Outcome types:
  - (i) O1–O4 pass, with C-CP, C-NS and C-LEAK green;
  - (ii) any obligation needs a new premise or fails;
  - (iii) the decisive remaining question is a finite search.

## 3. Derivation

### Node 1. Settings under one fixed affine rule (O1)

**Lemma A (affine settings).** The hypotheses:

- the whole system (carrier, meters, ready supplies, controller, heralds and
  record cells) evolves under one fixed affine bijection `Φ` of `F_q^N` per tick
  (any `q`);
- the setting `c` is a value in controller coordinates at time 0;
- the rest of the initial law is independent of `c` (AP1 C1, Gate A).

Then:

- (i) every slot at every time is `ℓ(x) + β·c + const`, where `ℓ` is a linear
  functional of the non-controller initial variables and `ℓ` and `β` do not
  depend on `c`;
- (ii) which functional of the carrier a record registers does not depend on
  `c`, and neither does the subspace of functionals determined by the records;
- (iii) changing `c` changes each encoded branch only by translations of slot
  values and relabellings of record values.

*Proof.* `Φ^t(x, c) = L_t (x, c) + a_t`, with `L_t` and `a_t` fixed. Split
`L_t` into its blocks on `x` and on `c`. The `c`-block contributes only an
additive term. A record is a slot, so (i) gives (ii). Conditioning on records
fixes values and leaves the determined subspace unchanged. ∎

**Corollary A′.** The observer's later choice of which existing record to
consult does not repair Lemma A. The physical process is the same for both
settings, so the joint law of all physical records is setting-independent. In
the comparator (AP1 §4.4 table) the `(r0, r2)` marginal differs between
`(s, s') = (0, 1)` and `(1, 1)`: independent versus equal. No coarse-graining of
a setting-independent process reproduces that difference.

**Consequences.**

- The SA-1 controller arms an edge when "`s = 0` and `e = 1`", a product, so it
  is not affine. P3 loads coefficients from outside the rule.
- B1's E-control is also externally loaded.

Under one fixed affine OI rule, a setting request therefore cannot select a `Z`
versus `X` read, nor `I` versus `P`. Any in-world source of setting selection
must make the rule non-affine in the joint state.

**Verdict for O1 within N:** fails. The setting selection is supplied (P3), and
Lemma A shows it cannot be internal while the rule is affine.

### Node 2. The characteristic-2 collapse

The free tick of an isolated cell is `J: (u, v) ↦ (−v, u)`, which is symplectic.

- **At `q = 2`, `J` is the swap `(z, x) ↦ (x, z)`.** In R1 (the `q = 2` frame)
  this swap acts on the Bloch octahedron as `Z ↔ X` with `Y` fixed:
  determinant `−1`, a reflection. Its encoded linear action has a Choi
  eigenvalue `−1` (self-check c3). AP1 uses the rotating frame `J^{−t}` (its C8)
  and so absorbs this. The reflection reappears in QA's Lemma R because over
  `F_2` every anti-symplectic map is symplectic.
- **Within R1, the CP subgroup of the affine maps is the even permutations of
  the four ontic points.** `AGL(2, F_2) ≅ S_4`. The 3-cycles, such as
  `(z, x) ↦ (x, z + x)`, are Clifford rotations of order 3 (c3). The linear
  transpositions are reflections. Translations are Pauli rotations.
- **At odd `q`, multiplier `+1` and `−1` differ.** The anti-symplectic map
  `(u, v) ↦ (u, −v)` is not symplectic. Its R-W image is the transpose class,
  with a Choi eigenvalue `−1` (c1).

### Node 3. Theorem W: native processes are stabilizer instruments at odd `q` (O3, O4)

**Theorem W.** Hypotheses:

- `q` an odd prime;
- R-W as in §2.1;
- any finite protocol of N or N+NNB, adaptive or not, including recombination of
  unregistered meters and reuse;
- ancilla laws whose R-W images are quantum states. P2's ready laws, uniform on
  `{slot = c}`, qualify, and so do the uniform carrier source and any
  stabilizer mixture.

Conclusion: the linear map that the protocol induces on signed laws, conjugated
by R-W, equals the action of a quantum stabilizer instrument. Every branch is
CP, the full instrument is trace-preserving, and composition of protocols
corresponds to composition of instruments.

*Proof.* R-W is a linear bijection from functions on `F_q^{2n}` onto operators
(W1). Each primitive is checked as a linear identity on **all** signed laws, so
no conditioning or noise-independence inference is used.

1. **Native, armed or NNB step.** Each is linear and symplectic (symmetric,
   center-free). By (W4), `Σ μ(λ) A(Mλ) = U_M ρ_μ U_M†`.
2. **Constant translation.** `A(λ + w) = w(w) A(λ) w(w)†`, a Weyl conjugation
   (W4 with `S = I`).
3. **Attaching a cell with law `ν`.** `ρ ↦ ρ ⊗ ρ_ν` by (W3). For a P2 law,
   `ρ_ν` is a Pauli eigenprojector divided by `q` (W2), which is a state.
4. **Registering a slot `f` of a meter that is then terminal (P1).** On laws this
   restricts to `{f = c}` and marginalizes the meter. By (W2) and (W3),
   `tr_m[(I ⊗ Π^m_{f=c})(A_c(λ_c) ⊗ A_m(λ_m))] = A_c(λ_c)·[f(λ_m) = c]`.
   This is "measure the meter's Pauli `f`, record `c`, discard the meter", which
   is CP. Under P1 the registered meter is never coupled again, so retaining it
   is equivalent to discarding it for every later operation.
5. **Discarding.** Marginalization equals partial trace (W3, unit traces).
6. **Feedback.** A record-conditioned arming or translation is a classically
   controlled Clifford or Weyl conjugation. A herald is an independent
   classical coin.

Compositions and convex combinations of CP maps are CP. ∎

**What the proof does not need.** It does not use PR-QA's sector case split or
the independence of raw offsets, so the masked-record example of
[PR-QA §3](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/PROOF-RECOVERY.md#L75)
is covered automatically. It does not need non-adaptivity, bipartiteness or
the absence of NNB.

**Load-bearing posits.**

- **P1.** Registering a slot of an active cell without discarding it is a
  restriction without a kick. Its encoded map has a Choi eigenvalue `−1` (c7).
  This is AP1's C9 sharpening.
- **P2.** A meter with both slots known gives a kick-free read with a Choi
  eigenvalue `−1` (c7′). This is AP1's C4 and the E-AR obstruction.
- **H-PREP.** It reads record-conditioned classes as preparations.

**Self-checks.** At `q = 3`, two cells: the coupled tick for `k = 0, 1, 2` has a
rank-1 Choi matrix (a unitary), and the read branches have rank-1 Choi matrices
(c2).

### Node 4. Proposition AS: CP exactly characterizes affine symplectic bijections

**Proposition AS.** Let `q` be odd prime, `g` a bijection of `F_q^{2n}`, and
`T_g` its R-W action, `T_g(A(λ)) = A(gλ)`. Then `T_g` is CP iff `g` is affine
symplectic.

*Proof.*

- (⇐) This is (W4).
- (⇒), first step. `T_g` permutes an orthogonal basis of equal norms (W1). It
  is therefore trace-preserving, unital and Hilbert–Schmidt isometric, so
  `tr(T_g ρ)² = tr ρ²`. If `T_g` is CP, it sends pure states to pure states.
- (⇒), second step. Write `T_g = Σ_i K_i · K_i†`. For each pure `ψ`, the vectors
  `K_i ψ` are pairwise parallel, since a sum of rank-one positive terms has rank
  one only then.
  - If some `K_i` has rank at least 2, write `K_j ψ = λ(ψ) K_i ψ` for every `j`.
    For `ψ, φ` with independent images, comparing at `ψ + φ` forces
    `λ(ψ) = λ(φ)`, so `K_j = λ K_i`. Then `T_g = Ad(K)` with `K†K = I`.
  - If every `K_i` has rank at most 1, their ranges coincide, so `T_g` is
    constant on pure states. That contradicts injectivity.
- (⇒), third step. So `T_g = Ad(U)`. `T_g` sends each nonnegative law to a
  nonnegative law, so `U` preserves Wigner nonnegativity of states. By (W6),
  `U` is Clifford, `U = w(a)μ(S)`. By (W4), `A(gλ) = A(Sλ + a)` for all `λ`.
  The `A(λ)` are distinct, so `g = S· + a`. ∎

**Consequences.**

- At odd `q` under R-W, among all ontic bijections, **CP ⇔ affine symplectic ⇔
  (linear rule, A5) ∧ (symmetric coupling)**. Both native properties carry the
  selection.
- Anti-symplectic maps (reflections), non-symmetric (non-reciprocal) linear
  couplings, and non-affine rules all give non-CP encoded actions on joint laws.
- This answers O3 without CC-RECON. The permitted operations are fixed by the
  native rule. Their CP property is computed, and its failure for every
  alternative is also computed.

**Verdict for O3 at odd `q`:** **pass natively**, for every protocol of N and
N+NNB, adaptive included, with P1 and P2 load-bearing. At `q = 2`: fails (QA
Lemma R, FB). CC-OFF(a) is green: switching the characteristic to 2 returns the
reflection (node 2).

### Node 5. Lemma S: no mixed-functional knowledge on bipartite graphs (O2 within N)

**Lemma S (sector splitting).** Hypotheses:

- `q` prime;
- a bipartite armed coupling graph;
- any process of N, record feedback included.

At every tick, the subspace `D` of functionals of the current state that are
determined by the supplied known slots and the registered records is the direct
sum `D_E ⊕ D_O` of its intersections with QA's two G1 sectors. If, for an
active cell, `a u + b v` with `ab ≠ 0` were determined, then `u` and `v` would
both be determined.

*Proof.* Condition on all record values. Each branch is a fixed sequence of
graded linear steps and constant translations. Translations change values, not
the determined subspace (QA Lemma Q (iii) argument). `D` is spanned by:

- the transported known slots of ready cells (P2: one slot each, so
  single-sector, and graded steps keep them single-sector);
- the registered record slots, transported to the current time (single-sector
  for the same reason).

A span of single-sector vectors splits by sectors. For a cell, `u` and `v` lie
in different sectors (QA Lemma G1). So `a u + b v ∈ D` forces `a u ∈ D_E` and
`b v ∈ D_O`. ∎

**Corollary S.** By AP1 Lemma 3, the determined functionals on active cells are
isotropic, and `ω(u, v) = 1`. So no active cell ever has a determined mixed
functional. Under any one-cell frame, the reachable encoded states are
eigenstates of the slot functionals only: 2 of the `q + 1` Pauli axes per cell.

- The phase gate `P` sends the eigenstate of `v` to the eigenstate of `v − u`,
  so it is unavailable.
- At `q = 2` this is AP1's type invariant (§4.2), extended from its §3.3
  apparatus class to all of N with feedback.
- The reversible encoded operations available in the frame are the graded
  maps `A ⊕ A^{−T}` composed with translations: permutation unitaries
  `|x⟩ ↦ |Ax + b⟩` up to Weyl phases, which are monomial.

**Self-checks.** Random graded protocols at `q = 3, 5` gave no determined mixed
carrier functional. With an NNB edge added, the breaking control fires (c6).
CC-OFF(b) is green.

**Verdict for O2 within N:** phase-sensitive reads, yes; non-monomial reversible
encoded operations, no. This holds at every prime `q`, adaptive included.

### Node 6. Lemma N: NNB gives the phase gate at odd `q`, with the composition battery

**Lemma N.** Take two same-colour cells in the common encoded frame, with
coordinates `(z_1, z_2, x_1, x_2)`.

- Let `N_k` be the NNB tick, a symmetric shear `x ↦ x + kSz` with
  `S = [[0,1],[1,0]]`. It is one coupled tick of the NNB edge: the coupled
  step equals `J ∘ (u, v) ↦ (u, v − kSu)`.
- Let `G = diag(A, A^{−T})` with `A = [[1,0],[1,1]]`. This is QA's graded
  transvection `C12`, available through the returned-mediator commutator, which
  holds over any ring.

Then `G^{−1} N_k G N_{−k}` is the shear `x_1 ↦ x_1 + 2k z_1`, with cell 2
returned exactly. At odd `q` with `k = 2^{−1}`, it is `P` on cell 1 and the
identity on cell 2.

*Proof.* `G^{−1} N_k G` is the shear with matrix `k AᵀSA = k [[2,1],[1,0]]`.
Shears add, and `k[[2,1],[1,0]] − k[[0,1],[1,0]] = [[2k,0],[0,0]]`. ∎

At `q = 2` the word is the identity (`2 = 0`). This agrees with QA Lemma Q:
`Q* (z_1 + x_1) = 1` is never determined. Self-check: c4 at `q = 2, 3, 5, 7`.

**The composition battery for `P` (N+NNB, odd `q`).** `P` is an exact ontic
permutation, not an average over hidden states. By Theorem W the correspondence
"protocol ↦ stabilizer instrument" is a homomorphism under composition, and the
reads are exact Lüders instruments as linear maps.

- K1: `P²` on `X_0` gives the eigenstate of `v − 2u` with value 0, as in the
  comparator.
- K2: `P^q = I`.
- K3: `X_0 → P^{q−1} → X → P → X`.
  - On `R0` (herald failure) the final `X` is deterministic, since `P^q = I`.
  - On `R1`, after the record `c`, the state is `X_c` and `P X_c` is the
    eigenstate of `v − u`. The final `X` is uniform and independent of `c`.
  - Both match the comparator. Lemma G2's obstruction does not apply, because
    NNB breaks G1.
- K4, K5, K6: hold by the same homomorphism, for every read axis `f`
  available after `P`. These are the `q + 1` axes, each realized as a native
  read conjugated by an available Clifford word. The failure branch is
  included.

**CC-IMIT (classical statistical imitation).** `M_P`: read `X` (native), record
`c`, then prepare the law uniform on `{v − u = c}`.

- On the `X_c` family, every single-step read (`Z`, `X`, `v − u`) matches
  `P` exactly (c5).
- It fails K1: after `M_P ∘ M_P` on `X_0`, the read of `v − 2u` is uniform; the
  comparator gives 0 with certainty.
- It fails K5 on `Z_0`: the `Z` read after `M_P` is uniform; the comparator
  gives 0.

C-COMP therefore discriminates. **D2 is satisfied.**

**Verdict for O2 under NNB at odd `q`:** pass at stabilizer scope. `P`, and with
it the full single-qudit Clifford group, is available. Every element is CP
(Theorem W) and passes C-COMP. At `q = 2` under NNB: `S` passes C-COMP by QA
[node 8](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L560)'s
induction, but O3 fails.

### Node 7. The ceiling at odd `q`, and the qubit case

**Proposition C (odd `q` ceiling).** For every protocol of N or N+NNB at odd
prime `q`, under R-W:

- (a) every reachable encoded state has a nonnegative Wigner function, because
  native laws are nonnegative. By (W5) the reachable pure states are stabilizer
  states;
- (b) every available encoded unitary channel is Clifford, by (W6). The Clifford
  group modulo phases is finite, so no encoded unitary of infinite order is
  available. This is the transported C-ROT, and it holds;
- (c) the quarter phase `D_i` (relative phase `i` on one basis state) is not
  available. The nonzero entries of a Weyl operator differ by `q`-th roots of
  unity, while `D_i X D_i†` has two nonzero entries differing by a factor `i`,
  which is not a `q`-th root of unity for odd `q`. So `D_i` is not Clifford. C-PH
  holds, with no escape (self-check c5);
- (d) the encoded theory is the noncontextual one. Spekkens (arXiv:1409.5041
  §V.A–B, read first-hand) shows that the odd-prime quadrature epistricted
  theory is operationally equivalent to the stabilizer subtheory and is itself a
  local noncontextual hidden-variable model. The native model is that model.

So no protocol at odd `q`, with or without NNB, leaves the noncontextual
stabilizer fragment.

**Observation E (FB at any finite abelian configuration group).** FB's proof
([§3](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md#L85),
[§4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md#L115))
uses only four facts:

- the three encoded bits are group homomorphisms `f_a: V → Z_2`;
- preparations are uniform on their level sets;
- the success kernel is common to all preparations;
- for `p(w) = 1`, the translation `t_w` maps level sets to level sets.

None of these uses a vector-space structure over `F_2`. So FB's dichotomy holds
for every finite abelian `V`, including `V = Z_4^{2n}` for a native `Z_4`
alphabet. A nonzero homomorphism to `Z_2` exists iff `|V|` is even. Hence:

| Configuration group | Uniform level-set qubit encodings | Combined `S` + C-CP |
| --- | --- | --- |
| Even order (`q = 2`, `Z_4`, …) | Exist | Fails whenever all translations are available (FB, extended) |
| Odd order (odd `q`) | None | No qubit. C-CP holds for all of N (Theorem W). No quarter phase (Prop. C) |

This agrees with the literature. For odd prime powers a Clifford-covariant
Wigner function exists, while none exists in any even prime-power dimension
(Zhu, arXiv:1504.03773, abstract read first-hand). And every ontological model
of the single-qubit stabilizer subtheory is contextual (LWE Theorem 1, as read
in AP1 §5.2).

**What this leaves for qubits.** Reciprocity separates rotations from
reflections only where the encoded Weyl group has odd order. A qubit-compatible
selection would have to break FB's H-L (non-uniform or non-level-set
preparations) or H-T (parity-flipping translations not separately available)
by a sourced mechanism. A native alphabet change alone does neither.

### Node 8. Theorem T: in-world control versus selection (O1 against O3)

**Theorem T.** Let `q` be an odd prime and use R-W. Suppose a single fixed
bijective rule acts on a phase space that includes a controller cell, and its
encoded action on all joint laws is CP. Then every tick of the rule is affine
symplectic (Proposition AS), and by Lemma A a setting held in the controller can
only translate values. So it cannot select a linear part of the carrier
operation. ∎

**Instance.** Take the reciprocal controlled shear on carrier `a` and
controller `c`, generated by `h = s·u_a²/2` with `s = u_c`:
`v_a −= s u_a` and `v_c −= u_a²/2`. Also take its one-way version, without the
kick on `v_c`. Both are bijections at `q = 3`.

- **Joint action.** Not CP: minimum Choi eigenvalues `−3` and `−4.24`
  respectively (c8).
- **Controller in a `Z` eigenstate `Z_s`, then traced out.** The carrier map is
  the Clifford `P^{−s}`, which is CP.
- **A reachable stabilizer input.** Take carrier–reference correlation
  `u_a = u_r`, `v_a = −v_r` (reachable by a graded transvection), with the
  controller in an `X`-type law. Its image has an encoded operator with
  eigenvalue `−1/3` (reciprocal) or `−0.47` (one-way): a non-quantum state
  (c9). With the controller in `Z_1` the output is a valid state.

So a controlled coupling preserves quantum compatibility only while every
controller is confined to setting-eigenstate laws, which are the laws of a
registered record.

**SM §3.1 as a candidate source.** SM's state-dependent coupling graph
([SM:104](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L104),
[explicit construction](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L110))
is the corpus's in-world controlled coupling. Its ring rule couples `i` to
`i + 2`, a same-sublattice and therefore NNB-type edge, when `x_{i+1} = 0`.
Read at odd `q` under R-W:

- the rule is a non-affine bijection, so by Proposition AS its joint encoded
  action is not CP;
- in a branch with the switching cells fixed, the adjacency is not symmetric:
  on a ring of `L ≥ 5` sites, `i` reads `i + 2` while `i + 2` reads `L(i + 2) = i + 1`
  and `R(i + 2, x) ∈ {i + 3, i + 4}`, never `i`. By AP1 §4.1 the
  branch map is then not symplectic, and by Proposition AS it is not CP even
  with classical controllers;
- its controllers are ordinary dynamical cells, not records.

As stated, it does not supply CTRL-REC (§6.2). This is a consequence of the
paper argument; no computation on the ring was run.

## 4. Shortcut checks

| Check | Finding |
| --- | --- |
| SC-1 Imported quantum behaviour | No unitary, interference mechanism or CP restriction is a premise. The operations are native bijections of configurations. That their R-W images are Clifford unitaries is derived (W4, Theorem W), and that every alternative bijection is non-CP is derived (Proposition AS). The quantum comparator and Gross's frame are imported as comparator and representation (ledger I1, R-W). The selection rests on A5 linearity and symmetric coupling. A5 is "partly derived" in Substratum: its affine part follows from amplitude-scale gauge, and the restriction to linear is imposed. The selection carries that status |
| SC-2 Hidden external control | Present, as in AP1 and QA. P3 arms every coupling that selects a setting, and NNB edges. H-PREP reads record classes as preparations, P2 supplies ready cells, and heralds are supplied. Lemma A shows that P3 cannot be replaced by any internal setting under a fixed affine rule. Theorem T shows that an internal non-affine controller is CP-compatible only with record-confined controllers |
| SC-3 Representation versus physical implementation | **Representation.** On the physical carrier every step is a permutation of `F_q^{2n}` (monomial; AP1 Lemma 2 and the kernel ceiling hold). The non-monomial operator `U_P` exists only in the R-W representation. What is physical is the record statistics under every composition and every change of read, which equal the Born statistics of the stabilizer circuits exactly (Theorem W). The physical model is an exact noncontextual hidden-variable model of that subtheory (Proposition C(d)) |

## 5. Ledger

| Item | Content | Classification | Status |
| --- | --- | --- | --- |
| N1 | Second-order linear update with symmetric, center-free coupling; symplectic with multiplier `+1` | Native | Substratum A4, A5; AP1 §4.1. Carries O3 at odd `q` (Proposition AS) |
| N1-A5 | Linearity (affine part from amplitude-scale gauge; linearity imposed) | Native premise, partly derived | Substratum A5. The selection inherits its status |
| N1-BIP | Bipartite nearest-neighbour graph | Native, selected branch | SM L224–L226. Carries Lemma S |
| Nq | Alphabet `F_q`; `q` not fixed by OI | Native parameter | Both characteristics computed; no `q` adopted. The native normalization `α = 1/d` needs `3 ∤ q` ([SM §2.7](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L88)) |
| N2 | Uniform law on unknown slots | Native measure, through H-PREP | As in AP1 and QA; H-INF-μ for an infinite hidden sector |
| N3 | Bijective steps | Native | — |
| P1 | Terminal registration | Supplied (AP1) | Load-bearing for Theorem W (c7) |
| P2 | Half-known ready cells | Supplied (AP1) | Load-bearing for Theorem W (c7′) and Lemma S |
| P3, E-iso | Per-tick, per-edge arming; isolation | Supplied (AP1) | O1 fails on P3 (Lemma A) |
| H-PREP | Record-conditioned classes read as preparations | Supplied (open hypothesis) | As in AP1 |
| NNB | Armable same-sublattice symmetric coupling | Supplied (QA conditional premise) | At odd `q` it buys `P` with no reflection cost |
| R-W | Gross phase-space frame, fixed for all settings | Mathematical representation | Unique Clifford-covariant choice at odd prime powers (Zhu); comparator dictionary only |
| CTRL-REC | §6.2 | Supplied (conditional premise, not adopted) | Named missing premise for O1 |
| I1 | Qubit and qudit stabilizer comparators, Lüders reads, CP | Imported (comparator) | — |
| I2 | Gross Theorems 2, 3, 6, 7, 19 and Lemma 4; Spekkens §V.A–B; Zhu (abstract); LWE Theorem 1 (via AP1) | Imported literature | §8.2 |

## 6. Outcome

### 6.1 Obligation verdicts

| Obligation | `q = 2` | Odd prime `q`, N | Odd prime `q`, N+NNB |
| --- | --- | --- | --- |
| O1 Physical source | Supplied (P3, H-PREP, P2); fails natively (Lemma A) | Same | Same; NNB is also P3-armed |
| O2 Capability | Reads only (AP1); `S` needs NNB (QA) | Reads only; reversible encoded operations monomial (Lemma S) | `P` and the Clifford group, exact under C-COMP; no quarter phase, no infinite-order unitary, noncontextual (Prop. C) |
| O3 Selection | Fails (QA Lemma R, FB) | **Pass natively** (Theorem W, Prop. AS) | **Pass natively** |
| O4 Continuation | Pass under P1, P2, H-PREP (AP1 §4.4) | Pass (Theorem W): heralded failure, terminal records, stabilizer outgoing state | Pass |
| C-NS | Green with wing-local cells (QA) | Green: wing-local operations act on wing cells; Main's [cone theorem](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Main.md#L366) | Green, with NNB edges wing-local |
| C-LEAK | Green within a wing; a shared parity signals (QA) | Green: every reuse or recombination protocol is a stabilizer protocol (Theorem W) | Green |
| C-Q | Lemma Q protects `Q* = 1` | `Q = Σ u_i v_i` is not conserved (`Q' = uᵀKu − Q`); no parity sector is needed in the one-cell frame | Same |
| Composites | Fail Mermin–Peres (QA node 10) | Reachable two-qudit stabilizer correlations, Bell-local (Prop. C(d)) | Same |

### 6.2 Type (ii) stop: the missing premises

**M1 — CTRL-REC (primary).** An armable symmetric coupling whose coefficient is
a fixed function `k(s)` of the registered slot `s` of a terminal record cell.
If the coupling is reciprocal, the record's conjugate slot receives the kick
`∂_s h` and is never coupled or read again.

- **Why this premise, and why the smallest.**
  - Lemma A forces any in-world setting source to be non-affine.
  - Theorem T forces its controllers to be confined to setting-eigenstate laws,
    or C-CP fails on reachable inputs (c9).
  - Under P1, registered records are exactly the cells confined to such laws.
  - CTRL-REC changes only the coefficient of an existing coupling and adds no
    other operation.
- **What it preserves.** In each branch with a fixed record value, the carrier
  map is affine symplectic, so Theorem W, Lemma S (bipartite), C-NS, C-LEAK and
  the composition battery are preserved. The setting is a physical record of an
  earlier read: "receives a setting request" is then a coupling read from a
  record.
- **What it buys.** O1 within the stated class: setting selection by one fixed
  rule, the AP1 apparatus without P3 for the `Z`/`X` choice and, if the
  controlled edge is NNB, the phase gate.
- **Independent consequences (§A.29).**
  1. A record that has controlled a coupling holds, in its conjugate slot, a
     nonlinear function of the controlled slots. Recovering it gives
     non-quantum encoded states (c9), so such records must be irreversible
     archives. This prediction is fixed by the premise and cannot be tuned.
  2. Every setting change consumes a record.
  3. The rule violates the additive-automorphism gauge of
     [SM §2.7](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L96)
     (any non-constant `k(s)` fails shift invariance).
- **What would derive it.** A symmetrized form of SM §3.1's state-dependent
  graph in which the switching variables are registered records. The first
  decisive check is whether SM's state-dependent-geometry principle can be
  stated with symmetric adjacency and record-valued switches while keeping its
  constraints (i)–(iii) (SM:108). As written, its explicit ring fails both
  conditions (node 8).
- **What would rule it out.** Retaining the additive-automorphism gauge as a
  physical symmetry of every coupling, or retaining P1 in its present form ("a
  registered cell is not coupled to any cell afterwards").
- **What would weaken it.** Nothing smaller was found. A one-way controller is
  equally CP-compatible in each branch (c8) but drops reciprocity, the property
  that carries O3. P3 is CTRL-REC with an external record.

**M2 — NNB (carried from QA).** At odd `q` NNB buys the full single-qudit
Clifford group with C-CP intact (Lemma N, Theorem W). QA's reflection cost
(Lemma R) does not arise. Derivation and ruling out are as in
[QA §4.1](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L805).
SM §3.1's ring produces NNB-type edges under state control, subject to the M1
conditions.

**M3 — qubit quarter phase with C-CP (open; no premise proposed).** Within the
class of this file, no premise supplies it.

- At odd order there is no qubit, and the native theory is the noncontextual
  stabilizer fragment (Prop. C).
- At even order FB's dichotomy holds (Observation E), so a native alphabet change
  does not help.
- A sourced mechanism must break H-L or H-T without restricting resources
  because of the target, which would be QA premise I and is flagged by
  CC-RECON.
- By LWE Theorem 1 it must be contextual. Proposition C(a) shows that, under
  R-W, nonnegative native laws cannot carry that contextuality.

The first check is whether an even-order carrier with a protected inaccessible
sector (QA Lemma Q at `q = 2`) admits non-uniform preparations, outside H-L,
reached by native reads under P1 and P2. QA's U′ preparations are uniform level
sets, so they do not.

### 6.3 No V3 round

The verdicts rest on paper proofs: Lemma A, Theorem W, Proposition AS, Theorem
T, Lemmas S and N, Proposition C and Observation E. The open items, CTRL-REC
sourcing and M3, concern which physical principle holds, not a finite search
over update rules, so no finite enumeration would be decisive.

### 6.4 Not claimed

- No physical setting source and no adoption of NNB, CTRL-REC or a value of `q`.
- No escape of C-PH or C-ROT: Proposition C shows neither escapes at odd `q`.
- No contextuality, Bell violation, Born-rule selection beyond the stabilizer
  values, or `J_exact(A)`.
- Theorem W and Proposition AS are paper derivations that use imported theorems
  of Gross. They are not kernel theorems.

### 6.5 Bearing on Q-B

The outcome is (ii), so no candidate is handed to Q-B. Proposition AS has a
continuum counterpart in the Liouville epistricted theory (Bartlett, Rudolph,
Spekkens, arXiv:1111.5057, abstract via AP1), where symplectic affine maps
correspond to Gaussian unitaries. If Q-B is activated, its first test would be
whether Proposition AS holds in the real or large-`q` limit, which would give
exact continuous symplectic rotations of mode quadratures with C-CP. A qubit
`rot` would still need non-Gaussian, hence Wigner-negative, resources, which
Proposition C(a) excludes for native nonnegative laws. This is not derived here.

## 7. Classification (§A.31) and assumption-watch markers

| Finding | Class |
| --- | --- |
| Lemma A: a fixed affine rule cannot select a linear part from an in-world setting | New for this programme |
| Theorem W: at odd `q`, every protocol of N (adaptive, NNB, recombination) is a stabilizer instrument under R-W | New for this programme. Its components are Gross's covariance and Spekkens' equivalence |
| Proposition AS: under R-W at odd `q`, CP ⇔ affine symplectic, for ontic bijections | New for this programme |
| Theorem T: CP-compatible in-world control needs record-confined controllers | New |
| Characteristic-2 collapse: Lemma R's reflections stem from `+1 = −1`; the native free tick is a reflection in R1's lab frame | Elaborating (QA, AP1 C8) |
| Lemma S: no mixed-functional knowledge on bipartite graphs, with feedback, at every prime `q` | New. Extends AP1's type invariant and QA G1 to the adaptive class |
| Lemma N: NNB gives the single-cell phase gate exactly iff 2 is invertible | New for this programme. Consistent with QA Lemma Q |
| Observation E: FB holds for every finite abelian configuration group | Elaborating (FB) |
| Proposition C: the odd-`q` ceiling | Confirming (Gross, Spekkens) |

**Assumption-watch markers.**

- **Alphabet-size hypothesis.** At stabilizer level, the encoded operation class
  differs qualitatively between `q = 2` (non-CP reflections) and odd `q` (all CP).
  Any correspondence constructed for
  [SM's alphabet-size hypothesis](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L94)
  would have to account for this. This is not a refutation: that hypothesis
  concerns emergent transition probabilities under a correspondence that is not
  constructed.
- **Linearity does the selecting at odd `q`.** Any proposal that adds a
  nonlinear or state-dependent rule, including the SM §3.1 graph, Native A and
  P-SDC, must re-check C-CP on joint laws (Proposition AS).
- **Reciprocity does the selecting at odd `q`.** A non-symmetric (one-way)
  coupling, even if linear, is not CP under R-W.
- **Records as controllers.** Using a register as a classical control input is
  CP-compatible only if its conjugate slot is never recovered (Theorem T and its
  instance).

## 8. Sources

### 8.1 Repository sources (all on `main@313a93ef`)

Every repository source below is on `main` at the pinned commit and is cited at
its stated scope. Issue and pull-request comments are cited as **provenance**
only (scope, authorization, review history). No claim here uses their content
as support.

| Source | Use | Classification (§A.42 item 8) |
| --- | --- | --- |
| AP1 Lemma 2, §4.1, §4.2, Lemma 3, Lemma 5, C4, C9, §4.4, §5.2, §5.6, ledger | Physical ceiling; native read; isotropy; R1; the `q = 2` baseline | Support on `main`; reviewed and merged (#1183) |
| QA §1.2, G1, G2, node 5, Lemma Q, node 8, Lemma R, §4.1, node 10 | Class N; NNB; grading; parity; reflections | Support on `main` (#1184, repaired by #1189) |
| PR-QA §§1–3 | The R1 C-CP recovery that Theorem W generalizes without its case split | Support on `main` (#1189) |
| FB §§2–5 | Combined-target obstruction; Observation E | Support on `main` (#1189) |
| Main Definition L44, Lemma 3 L56, L82, Lemma 2 L306, cone theorem L366 | Native model, measure, traced channel, C-NS | Manuscript text at the snapshot |
| Substratum L48, A1 L92, A4 L98, A5 L100, A6 L102 | Native rule and its status | Manuscript text |
| SM L88–L96 (§2.7), L104–L110 (§3.1), L224, L226, L296 | Alphabet, gauge, state-dependent graph, form lemma | Manuscript text |
| GR L260, L266, L270 | Monomial sourcing and layer-flow negatives | Manuscript text |
| Kernel: `permClass`, `permTheory_not_control`, `permTheory_not_qm`, `onesFixing_not_phasesAvailable`, `permClass_onesFixing`, `substratumGen_not_control`, `exists_nonMonomial_of_layerFlowExecutable`, `obs_not_layerFlowExecutable`, `stochasticChannel_kraus_monomial`, `coherentLiftClass_eq_substratumClass`; `ReadWriteControl.lean` header | §1.1 ceiling (read, not rebuilt). `readWriteSourced_*` is not cited (#1188) | Kernel statements on `main` |
| oi-qm-ext-1 README, B1, observer-interface source, two-system interface §4; F2-1 A★ (Θ-K, Θ-F, N4, N8) | Lead dispositions; C-LEAK | Support on `main` at their reviewed scopes |
| #1169 comments 6714000230, 6713955150, 6713653816; owner addendum, [#1169 c.6714136234](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6714136234); PR #1184 and #1189 review records | Scope, authorization, review history | Provenance |

### 8.2 Imported literature

| Work | Used for | Read in this unit |
| --- | --- | --- |
| D. Gross, "Hudson's theorem for finite-dimensional quantum systems", arXiv:quant-ph/0602001 | (W1)–(W6): Theorems 2, 3, 6, 7, 19; Lemma 4 | Full text of §§I–II and the statements of Theorems 2 and 19 |
| R. W. Spekkens, "Quasi-quantization", arXiv:1409.5041 | Odd-prime equivalence and noncontextuality; `d = 2` inequivalence | Introduction and §V.A–B |
| H. Zhu, "Permutation symmetry determines the discrete Wigner function", arXiv:1504.03773 | Clifford-covariant Wigner functions exist only in odd prime-power dimensions (besides the noted exceptions); none in even prime-power dimensions | Abstract |
| P. Lillystone, J. J. Wallman, J. Emerson, arXiv:1802.06121v2 | Theorem 1 (qubit stabilizer contextuality) | Not re-read; used as read first-hand in AP1 §5.2 and QA |
| M. Howard et al., arXiv:1401.4174 | Context only (contextuality and magic); no result used | Abstract |
| S. D. Bartlett, T. Rudolph, R. W. Spekkens, arXiv:1111.5057 | Q-B remark (§6.5) | Abstract via AP1; not a premise |

Theorem W, Proposition AS and Proposition C use Gross's stated theorems, with
their odd-dimension hypothesis. Lemma A, Lemma S, Lemma N, Theorem T and
Observation E are self-contained algebra.

## 9. Verification scope

Every verdict rests on the paper arguments of §3. Author self-checks were run
locally as controls. They are not committed, are not evidence and carry no
verdict. Checks marked "exact" used modular integer or `Fraction` arithmetic.
The others used floating-point eigenvalues at tolerance `1e−8`.

| Check | What it controls |
| --- | --- |
| c1 | Gross frame at `q = 3, 5`: unit trace, orthogonality, Pauli projectors as line sums. `J` and `P` give rank-1 Choi matrices; the anti-symplectic `(u, −v)` gives Choi eigenvalue `−1` |
| c2 | `q = 3`, two cells: the coupled tick (`k = 0, 1, 2`) and the read branches are CP |
| c3 | `q = 2` tetrahedral frame: the free tick (swap) has Choi eigenvalue `−1`; a 3-cycle and a translation are CP |
| c4 | Lemma N word at `q = 2, 3, 5, 7` (exact); symplecticity |
| c5 | `D_i` not Clifford at `q = 3`; CC-IMIT laws (exact) |
| c6 | Lemma S on random graded protocols at `q = 3, 5` (exact); the NNB breaking control fires |
| c7, c7′ | P1 removed (restriction without kick) and P2 removed (sharp meter): Choi eigenvalue `−1` |
| c8 | Controlled shears: joint action not CP; carrier map CP with the controller in a `Z` eigenstate |
| c9 | A reachable stabilizer input with an `X`-type controller is mapped to a non-PSD encoded operator |

No Lean build, simulation campaign, enumeration, manuscript edit, freeze,
dispatch or merge was performed. Independent review of this file is a separate
step.
