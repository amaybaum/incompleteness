# MECH-1: native reciprocity as a selection of quantum-compatible operations, and the control it excludes

**Standing.** Paper-only research unit under #1169. Author: Claude Code session,
2026-11-07. Scope:

- [owner authorization](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6714000230);
- [research question](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6713955150);
- [owner addendum](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6714136234):
  composition and changed-measurement tests, and the three shortcut checks of §4.

This file proposes no premise for adoption and promotes no claim. No simulation,
enumeration campaign, Lean build, V3 execution, manuscript change, freeze,
dispatch or merge is part of it. Small exact or floating-point checks of this
file's own algebra were run as author self-checks (§9). They are controls on that
algebra, not evidence, and no verdict rests on them.

**Source snapshot.** Every repository link is pinned to `main` at
`313a93efcab581465919a4ff82ecda1e4b81e990` (cited as `main@313a93ef`), which
contains apparatus-1 (#1183), Q-A (#1184), and the Q-A forward repair and
feedback result (#1189). Abbreviations:

- **AP1**: [apparatus-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md);
- **QA**: [Q-A DESIGN](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md);
- **PR-QA**: [Q-A PROOF-RECOVERY](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/PROOF-RECOVERY.md);
- **FB**: [feedback RESULT](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md).

**Labels used from earlier records.**

- **SA-1**: AP1's access candidate. Reciprocal coupling (a); arming per tick and
  per edge, P3 (a′); terminal registration, P1 (b); half-known ready cells, P2 (c).
- **PC-F1**: the gauge control requiring one encoded identification fixed for all
  settings (AP1 §1.3).
- **E-AR**: the obstruction that unboundedly many perfectly distinguishable
  preparations exclude a fixed `C²` carrier (AP1 C4).
- **Native A**: the nonlinear `F_2`-triple rule of the record-control record
  (§1.4).
- **P-SDC**: #1110's state-dependent-coupling proposal.
- **H-INF-μ**: a normalized product law on a cone of an infinite hidden sector
  (QA ledger).

## 0. Result

1. **Where the monomial obstruction sits (§1).**
   - On the physical carrier every deterministic bijective apparatus lies in
     `permClass` (AP1 Lemma 2), whatever its dynamics.
   - Non-monomial behaviour can only appear on an encoded carrier. There the
     native reads are already phase-sensitive (AP1 §4.4).
   - What is missing is a reversible encoded operation that is non-monomial
     **and** completely positive (CP).
   - Over `F_2` the existing results give no encoded `S` in the one-cell frame
     (AP1 Lemma 5). With a same-sublattice coupling (NNB), `S` comes together
     with encoded reflections (QA Lemma R). FB forces reflections for uniform
     linear qubit encodings with available translations, adaptive protocols
     included.
2. **Selected lead (§1.4): the characteristic of the native alphabet.**
   - The native rule `x(t+1) = Σ k x_nbr − x(t−1)` has a `−x(t−1)` memory term
     (Substratum A4, SM form lemma). Together with symmetric coupling, that makes
     each step symplectic with multiplier `+1`. With `+x(t−1)` the step would be
     anti-symplectic (node 2).
   - Over `F_2`, `+1 = −1`, so the multiplier cannot tell rotations from
     reflections. Over an odd prime alphabet it can.
   - The question is whether, at odd `q`, this native structure excludes
     non-quantum operations without a rule defined by the target.
3. **Selection (nodes 2–4).** Fix Gross's Clifford-covariant phase-space frame
   R-W, a mathematical representation chosen once (§2.1), at odd prime `q`.
   - **Theorem W.** Every protocol of the native class N acts on the encoded
     carrier as a quantum stabilizer instrument. This includes adaptive
     protocols, recombination and NNB. Every branch is CP and composition
     corresponds exactly.
   - **Proposition AS.** The encoded action of an ontic bijection is CP **iff**
     the bijection is affine symplectic.
   - O3 is therefore met in this precise form: the native rule is affine
     symplectic, and there is one fixed frame in which the affine symplectic
     bijections are exactly the CP ones.
   - At `q = 2`, R1 represents some symplectic maps as reflections, and the
     multiplier cannot exclude them (node 2).
4. **Capability (nodes 5–7).**
   - **Lemma S (bipartite graph, every prime `q`, record feedback included).**
     No functional mixing a cell's two slots is ever determined.
   - **Lemma G (bipartite graph, odd `q`, record feedback included).** Every
     available reversible encoded operation is graded, so it is monomial in the
     sector-adapted product basis.
   - **At `q = 2`.** Non-adaptive gradedness is QA node 1. Corollary S holds with
     feedback, so there is no single-cell `P`. Adaptive gradedness is open.
   - **Lemma N and Lemma M (NNB, odd `q`).** Explicit words give both
     single-cell shears and hence the full single-qudit Clifford group. No fixed
     product basis makes every available operation monomial.
   - The composition battery (C-COMP) is passed. **It is passed equally by the
     mechanism's own classical model.** By Proposition C(d) the native `P` is
     the epistricted noncontextual model. No test inside the reachable fragment
     distinguishes it from a classical statistical model. C-COMP rejects only
     the weaker measure-and-prepare imitation (CC-IMIT).
   - **Proposition C (odd `q`).** No protocol supplies the quarter phase, an
     infinite-order encoded unitary, or a Wigner-negative state.
5. **Physical source (nodes 1 and 8).**
   - **Lemma A.** Under one fixed affine rule, a setting held in the state can
     only translate values.
   - **Theorem T.** At odd `q`, in R-W, a fixed bijective rule whose joint
     encoded action is CP is affine, so in-world setting selection then fails.
   - **Proposition T′ (exact, every odd `q`).** Take any rule that leaves the
     controller slot `u_c` unchanged and in which `u_c` selects a carrier linear
     part `S(u_c)` that is not constant. Then a reachable stabilizer input with
     an X-type controller goes to a non-quantum encoded state. A native cell
     does not keep `u_c` fixed: a static slot or a one-parity schedule is a
     supplied element (node 8).
   - Conversely, quantum compatibility holds if every `S(s)` is symplectic and,
     given `u_c`, the controller's `v_c` is uniform and independent of all
     other cells.
   - Confinement is shown necessary only in this sense: if any pure stabilizer
     controller law other than a `u_c`-eigenstate is admissible, C-CP fails on
     a reachable input. It is not shown for every non-diagonal law.
6. **Qubit encodings (node 7).**
   - FB's proof uses only homomorphisms to `Z_2`, so it holds for every finite
     abelian configuration group whose `Hom(V, Z_2)` has rank at least 2. For
     `V = Z_m^{2n}` this means exactly when `m` is even, which includes a `Z_4`
     alphabet. For such groups the combined `S` + C-CP target fails.
   - At odd order there is no uniform level-set qubit encoding and no quarter
     phase.
7. **Outcome type (ii): stop (§6).**
   - Selection passes natively at odd `q` in the stated form.
   - Continuation passes under the carried-over posits.
   - Capability needs NNB, and it stays inside a fragment that a classical model
     reproduces exactly.
   - Setting selection fails natively.
   - The missing physical premise for in-world setting selection is **M1**. It
     is a non-affine coupling coefficient set by a controller slot, together with
     a physical reason that keeps controllers' laws diagonal in that slot. As a
     bare confinement it is a target-motivated restriction (CC-RECON). A
     dynamical form, CTRL-MON (§6.2), monitors the controller with terminal
     ready meters. It removes the restriction on controller laws but relocates
     the premise. Still supplied are: the meter supply; terminality of
     unregistered meters (also flagged CC-RECON); per-tick meter delivery and
     arming; a static controller slot or parity clock; and the non-affine,
     gauge-violating coefficient. Nothing smaller was found.
   - For the qubit quarter phase with C-CP, no premise in this class supplies it
     (M3, open). No V3 round is proposed.

## 1. Locating the obstruction

### 1.1 The physical carrier

AP1 [Lemma 2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L153)
covers every apparatus that does the following on a finite configuration set:

- acts by bijections;
- attaches fresh cells with fixed laws;
- discards by marginalization;
- conditions on configuration records.

Each branch of each such instrument is a sum of conjugations by scaled partial
permutations, that is,
[`permClass`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L236).
Restricted to a finite cone,
[`permTheory_not_control`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L708)
and [`permTheory_not_qm`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L717)
apply by QA §4.1's monotonicity transfer. This holds for every update rule and
every alphabet. Three premises produce it:

- (P-a) the operational state is a law on configurations;
- (P-b) every step is bijection-valued;
- (P-c) reads are of configuration functions.

Other kernel and paper results agree:

- [`ReadWriteControl.lean`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/ReadWriteControl.lean#L1)
  names "an extended substratum with a genuinely continuous (non-bijective-valued)
  coupling" as open. That would change (P-b).
- [`ExecSource.lean`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/ExecSource.lean#L52)
  and [`LiftSource.lean`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/LiftSource.lean#L251)
  show two things. Fractional-time layer flows need a non-monomial admissible
  operator. The coherent and stochastic lifts are configuration-level.
- [GR:270](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/GR.md#L270)
  records the site-space wave-operator formulation as unresolved.

### 1.2 The encoded carrier

AP1 keeps (P-a)–(P-c) on the physical carrier. It changes only the
**identification**: a fixed, setting-independent map from laws on one cell to
states of `C²`, the tetrahedral frame R1
([AP1 §4.2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L498)).
On that carrier:

- **Phase-sensitive instruments are native.** The native minimal read is the
  encoded `Z` or `X` Lüders instrument. It consists of a coupled tick with a
  half-known meter, then terminal registration.
- **Non-monomial CP reversible operations are missing.**
  - AP1 [Lemma 5](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L731)
    excludes `S` under R1 by any stochastic map.
  - QA [G1](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L240)
    and [G2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L342)
    exclude it for non-adaptive bipartite processes.
  - With NNB, QA [Lemma R](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L667)
    shows `S` comes with two separately available encoded reflections.
  - FB [§§3–5](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md#L85)
    excludes the combined `S` + C-CP target. Its scope is uniform linear
    encodings with a common lift and available translations, feedback included.

All of these results are over `F_2`. Each reflection is an encoded map of
determinant `−1` on the Bloch octahedron (the transpose class), which is not CP.

### 1.3 What would have to change

| Premise | Change | Covered by |
| --- | --- | --- |
| (P-b) bijection-valued steps | Continuous or non-bijective coupling | `ReadWriteControl` open question; B1's E-real and E-control |
| (P-c) configuration reads | Reads of non-configuration observables | F2-1 A★ Θ-D and N8 (these fail its screen item 2) |
| Identification R1 | Larger or different encoded frame | AP1 §5.2 (P-8); QA (U′, NNB) |
| Native alphabet `F_2` | Odd characteristic | AP1 §5.6 (an expectation only); QA G1 (generation only, no C-CP) |
| Access P1–P3 | Changed registration, supply or arming | AP1 C3, C4, C9; QA Lemma Q |

### 1.4 Leads, dispositions and selection

| Lead | Prior coverage | Disposition |
| --- | --- | --- |
| Observer-level coarse-grained or traced description (Koopman, Fourier or Bogoliubov change of observable basis) | Main §3.2 [Lemma 2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Main.md#L306) (the traced one-step channel is a Clifford-conjugated Weyl mixture with monomial Kraus operators); LiftSource T3; F2-1 A★ [Θ-K, Θ-F](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md#L73); PC-F1 | Covered. Its usable part, a **fixed** encoded frame, is kept as a representation, not as a source |
| Fractional-time layer-flow access | [`obs_not_layerFlowExecutable`](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/lean-mathlib/OIBridge/ExecSource.lean#L129); LiftSource T4; F2-1 [N4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md#L79) | Covered |
| Continuum or large-`q` limit with metaplectic quantization | F2-1 [N8](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/recursive-substates/f2-1-coherence-sourcing/amendments/A-star.md#L83); [interface source §4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/observer-interface-source.md#L192), row L3; B1 | Partly covered. Its exact finite form is the selected lead: at odd `q` the finite Weil representation exists exactly. The continuum form is left to Q-B (§6.5) |
| Preparation-contextual or nonlinear encodings | Left open by FB §5 | Not selected. No physical lead in the corpus. Node 7 sharpens what such a lead must break |
| B1 conditional two-mode mixing | [B1 §6](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-mode-drive.md#L124); its E-control is externally loaded | Covered. Lemma A (node 1) shows why that control cannot be internal under a fixed affine rule |
| A native record entering control | [Record-control](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/record-control-20261107/DESIGN.md#L11): a record-bearing field enters a neighbouring Native A gate (nonlinear, `F_2` triples) without an added write, and stops at conversion into a usable controlled operation. [Setting-source feasibility](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/continuous-substates/native-setting-source-feasibility.md#L7): record-derived labels cannot steer an independent coordinate without a state-changing operation, and a supplied ideal actuator does not close that gate | Not re-surveyed. Both bear on M1 (§6.2): they show native delivery without a usable actuator, and they mark a supplied actuator as a countercontrol, not a source |
| **L-χ: alphabet characteristic and native reciprocity** | AP1 §5.6 states the odd-`q` stabilizer case as an expectation. QA G1 settles non-adaptive bipartite generation. No record decides C-CP at odd `q`; Lemma R, PR-QA and FB are all over `F_2` | **Selected** |

**Justification.**

- **Expected decisiveness.** The third obligation asks for an independently
  motivated structure that excludes reflections. The native step has
  symplectic multiplier `+1`. In AP1 §4.1's block form
  `M = [[K, sI],[I, 0]]`, one finds
  `MᵀΩM = [[Kᵀ−K, −sI],[sI, 0]]`, which equals `Ω` iff `K = Kᵀ` and `s = −1`,
  and equals `−Ω` iff `K = Kᵀ` and `s = +1`. So the multiplier rests on two
  native features:
  - the memory term `−x(t−1)`
    ([Substratum A4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Substratum.md#L98),
    [SM form lemma](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L224));
  - the symmetry of the coupling.

  Over `F_2` both multipliers coincide. Whether the multiplier selects at odd
  `q` is decidable by exact argument.
- **Independent motivation.** The symmetric coupling with that memory term is
  the native rule, and the same reciprocity supplies the measurement backaction
  in SA-1. The alphabet size is a native parameter that OI does not fix
  ([SM §2.7](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L88)).
  No value of `q` is adopted; both characteristics are computed.

## 2. Question, decision rule and controls

The decision rule, controls and countercontrols below are stated in the same
commit as the derivation of §3. Their priority over the result is not
separately recorded. The verdicts are paper proofs, so no verdict depends on
that order.

### 2.1 Target, comparator and identification

- **Comparators (imported, I1).**
  - At `q = 2`: the single-qubit stabilizer subtheory (QA §1.1).
  - At odd prime `q`: the `n`-qudit stabilizer subtheory of dimension `q`. This
    means stabilizer states and their mixtures, Weyl (Pauli) reads with Lüders
    continuation, and the Clifford group.
- **Identification R-W (mathematical representation).** For odd `q`, use
  Gross's phase-space point operators `A(λ)`, `λ ∈ F_q^{2n}`.
  - Each cell's slots `(u, v)` are identified with Gross's (position, momentum)
    by one fixed symplectic convention, in AP1's encoded frame `J^{−t}` per cell.
  - The free tick `J: (u, v) ↦ (−v, u)` of the `−x(t−1)` rule is symplectic.
    By Gross's Theorem 7 the choice of frame within this family is immaterial.
  - A law `μ` maps to `ρ_μ = Σ_λ μ(λ) A(λ)`. R-W is fixed for all settings,
    as PC-F1 requires.
  - At `q = 2`, Gross's construction needs `2^{−1}`. R1 is Wootters' `q = 2`
    analogue.
  - R-W is singled out by Clifford covariance, a property of the comparator.
    O3 is stated with that qualification (node 4).
- **Facts from Gross (arXiv:quant-ph/0602001, odd `d`; read first-hand).**
  - (W1) The `A(λ)` have unit trace and `tr A(λ)A(μ) = q^n δ_{λμ}`
    (Theorem 6.1).
  - (W2) Pauli level-set marginals are Born probabilities:
    `Π_{f=c} = q^{−n} Σ_{f(λ)=c} A(λ)`. This is Theorem 6.3 for position, and
    holds for every Pauli functional by Theorem 7 and the transitivity of
    `Sp(2n, F_q)` on nonzero vectors.
  - (W3) Multi-cell `A` factor as tensor products (Theorem 6.4).
  - (W4) Clifford covariance. For affine symplectic `g = S· + a`,
    `U_g = w(a)μ(S)` satisfies `U_g A(λ) U_g† = A(gλ)`. The Weil representation
    `μ` is projective, which leaves conjugation channels unaffected (Theorems 3
    and 7, Lemma 4).
  - (W5) Discrete Hudson. A pure state has a nonnegative Wigner function iff it
    is a stabilizer state (Theorem 2).
  - (W6) A unitary that keeps every nonnegative-Wigner state nonnegative is
    Clifford (Theorem 19).
  - (W7) A stabilizer state `|M, v⟩` has Wigner function uniform on the affine
    Lagrangian `M + v` (Lemma 9). Such a state exists for every pair `(M, v)`
    (Lemma 8).
  - (W8) A unitary that permutes the phase-space point operators is Clifford
    (Lemma 29).

### 2.2 The class

N is QA's class
([§1.2](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L124))
over a prime alphabet `F_q`. It contains:

- second-order, linear, symmetric, center-free updates with the `−x(t−1)`
  memory term, native or armed per tick and per edge under P3, with E-iso;
- P2 ready cells;
- P1 terminal registration;
- discarding;
- constant translations;
- record-conditioned armings and translations.

N+NNB adds QA's armable same-sublattice symmetric coupling. The carried posits
keep their AP1/QA classification as supplied
([ledger](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L411)).

### 2.3 The four obligations and their pass conditions

- **O1 Physical source.** Pass iff one fixed rule executes the preparation, the
  receipt of a setting request held in the state, and the operation, including
  failures and records. A supplied posit (P3, H-PREP, P2, or a premise of §6.2)
  gives the verdict "supplied", not "pass".
- **O2 Quantum capability.**
  - Pass iff no fixed product basis makes every available reversible encoded
    operation monomial, **or** the quarter phase is available.
  - In either case the operation must pass the composition battery C-COMP. A
    one-step averaged match is not a pass.
  - Whether a classical statistical model also passes C-COMP is reported
    separately (CC-IMIT′). It decides whether the pass carries any
    nonclassicality.
- **O3 Quantum selection.**
  - Pass iff every available encoded branch, and every coarse-graining of
    branches, has a CP extension (C-CP).
  - The exclusion must follow from a structure stated without reference to the
    comparator.
  - A rule that defines the operation set as "the quantum ones", or restricts
    resources only because an unwanted operation must disappear, is flagged by
    CC-RECON. QA premise I is such a rule.
- **O4 Operational continuation.** Pass iff each operation has a derived
  complete instrument with all of the following:
  - success branches;
  - the heralded failure branch;
  - retained records;
  - retained hidden information;
  - an outgoing state on which the next operation acts with the comparator's
    statistics.

### 2.4 Controls and countercontrols

| ID | Requirement | Required outcome |
| --- | --- | --- |
| C-PH | Encoded quarter phase (`PhasesAvailable` transported) | Reported. Escape iff available |
| C-ROT | Encoded `rot`, or at odd `q` an encoded unitary of infinite order | Reported. Escape iff available. Every finiteness and measure hypothesis is named |
| C-CP | Per encoding: every available encoded branch is CP | Required for O3 |
| C-IS | AP1's per-state diagnostic | Diagnostic only. At odd `q`: whether the reachable encoded states have nonnegative Wigner functions |
| C-NS | No-signalling of complete local histories, with wing-local operations | Required |
| C-LEAK | The two-system leak ([two-system §4](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/two-system-interface.md#L241)), reuse and recombination | No protocol extracts information beyond what the comparator allows |
| C-Q | QA Lemma Q parity protection | Whether it survives at odd `q` |
| C-COMP | Composition battery (below) | Required for O2 |
| CC-OFF | Mechanism off | (a) at `q = 2` the reflection returns; (b) without NNB the phase gate vanishes |
| CC-IMIT | Measure-and-prepare imitation | Must fail C-COMP |
| CC-IMIT′ | The mechanism's own noncontextual model, or Gross sampling | Reported: whether it passes C-COMP |
| CC-RECON | Reconstruction flag | An operation set or a resource restriction motivated by the target is labelled, not counted as a source |
| C-EX | §A.21 exactness | Structural identities are checked together with controls that must break them |

**C-COMP (owner addendum).** The tests are applied to the candidate operation
`O`. At `q = 2` this is `S`. At odd `q` it is the phase gate
`P: (u, v) ↦ (u, v + u)`, of order `q`.

- K1: `O∘O` on every encoded eigenstate family.
- K2: `O^m = I`, with reads.
- K3: G2's sequence `X_+ → O^{m−1} → X → O → X`, including the herald-failure
  branch `R0`.
- K4: repeated use with continuation, for every read choice.
- K5: every available read axis after `O`, on one preparation.
- K6: the complete instrument, with every branch and the failure branch.

**Pass** means the joint record laws equal the comparator's for all finite
sequences. It must be shown by an exact homomorphism, or by induction over a
family closed under the class.

### 2.5 Shortcut checks (owner addendum)

- **SC-1.** Is a unitary, an interference mechanism or a CP restriction imported?
- **SC-2.** Does an outside agent select couplings or prepare special inputs?
- **SC-3.** Does the non-monomial operation exist in the physical dynamics or
  only in the representation?

### 2.6 Decision rule

- **D0.** A failed C-EX or CC-OFF voids the verdict of the branch it controls.
  A candidate that passes only after the encoded operation set, or a resource,
  is restricted by reference to the comparator is labelled under CC-RECON.
- **D1.** Each obligation is decided in N first. If it fails there, it is
  decided under the smallest single departure found. That departure is stated
  as a conditional premise, with what it preserves, what it buys and its
  independent consequences (§A.29).
- **D2.** O2 counts only with C-COMP passed and CC-IMIT failing C-COMP. If
  CC-IMIT′ also passes C-COMP, the O2 verdict is stated as "not separated from
  classical imitation within the reachable fragment".
- **D3.** Outcome types:
  - (i) O1–O4 pass, with C-CP, C-NS and C-LEAK green;
  - (ii) any obligation needs a new premise or fails;
  - (iii) the decisive remaining question is a finite search.

## 3. Derivation

### Node 1. Settings under one fixed affine rule (O1)

**Lemma A (affine settings).** Assume:

- the whole system evolves under one fixed affine bijection `Φ` of `F_q^N` per
  tick, for any `q`. The whole system means the carrier, meters, ready
  supplies, controller, heralds and record cells;
- the setting `c` sits in controller coordinates at time 0;
- the rest of the initial law is independent of `c` (AP1 C1).

Then:

- (i) every slot is `ℓ(x) + β·c + const`, with `ℓ` and `β` independent of `c`;
- (ii) neither the functional of the carrier that a record registers nor the
  subspace determined by the records depends on `c`;
- (iii) `c` changes each encoded branch only by translations of slot values and
  by relabelling of record values.

*Proof.* Write `Φ^t(x, c) = L_t(x, c) + a_t`. The `c`-block of `L_t` contributes
only an additive term. A record is a slot, which gives (ii). Conditioning fixes
values and leaves the determined subspace unchanged, which gives (iii). ∎

**Corollary A′.** Choosing afterwards which record to consult does not escape
Lemma A. The physical joint law of all records does not depend on the setting.
The comparator's `(r0, r2)` marginal does depend on it: AP1 §4.4 gives
independence at `(s, s') = (0, 1)` and equality at `(1, 1)`.

**Consequences.**

- SA-1's controller arms an edge when "`s = 0` and `e = 1`". That is a product,
  so the controller is not affine. P3 loads coefficients from outside the rule,
  and so does B1's E-control.
- Any in-world source of setting selection must make the rule non-affine in the
  joint state.

**Verdict for O1 within N: fails.** Setting selection is supplied by P3.

### Node 2. The characteristic-2 collapse and the memory sign

- **Memory sign.** With `s = −1` (Substratum A4, SM L224, AP1 §4.1) a symmetric
  step is symplectic. With `s = +1` it is anti-symplectic at odd `q`.
  [Main L296](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Main.md#L296)
  displays the `F_2` rule with `+ v`, which is the same rule at `q = 2`. This
  file uses the `−x(t−1)` form throughout. The sign question for Main is not
  resolved here (§7).
- **At `q = 2`.**
  - In AP1's adopted frame `J^{−t}`, the free tick is the identity (AP1 C8).
    In the non-rotating frame it is the swap `(z, x) ↦ (x, z)`. R1 represents
    that swap as `Z ↔ X` with `Y` fixed, a reflection with Choi eigenvalue `−1`
    (self-check c3).
  - The reflections of QA Lemma R are symplectic maps over `F_2`, such as
    transvections `x += z` and the swap. R1 represents them as odd permutations
    of the four points.
  - Under R1, `AGL(2, F_2) ≅ S_4`. Even permutations act as rotations: the
    3-cycles such as `(z, x) ↦ (x, z + x)` are Clifford rotations of order 3,
    and translations are Paulis (c3). Odd permutations act as reflections.
  - The operative fact is that R1 is not covariant under the `q = 2` symplectic
    group: no Clifford-covariant Wigner function exists in even prime-power
    dimension (Zhu). `+1 = −1` explains only why the multiplier cannot flag the
    reflections.
- **At odd `q`.** The anti-symplectic map `(u, v) ↦ (u, −v)` has an R-W image in
  the transpose class, with Choi eigenvalue `−1` (c1).

### Node 3. Theorem W: native processes are stabilizer instruments at odd `q` (O3, O4)

**Theorem W.** Assume:

- `q` is an odd prime;
- R-W is the identification;
- the protocol is any finite protocol of N or N+NNB, adaptive or not, including
  recombination of unregistered meters and reuse;
- every ancilla law has a quantum state as its R-W image. This covers P2 ready
  laws, the uniform carrier source and stabilizer mixtures.

Then the protocol's linear action on signed laws, conjugated by R-W, is a
quantum stabilizer instrument. Every branch is CP, and composition corresponds
exactly.

*Proof.* R-W is a linear bijection between functions on `F_q^{2n}` and
operators (W1). Each primitive is checked as an identity on **all** signed laws,
so no inference from conditioning is used.

1. **Coupled step.** A native, armed or NNB step is linear and symplectic (node
   2: symmetric coupling with `s = −1`; center-freeness is not needed here). By
   (W4) it acts as `Σ μ(λ) A(Mλ) = U_M ρ_μ U_M†`.
2. **Constant translation.** `A(λ + w) = w(w) A(λ) w(w)†`, by (W4).
3. **Attaching a cell with law `ν`.** The map is `ρ ↦ ρ ⊗ ρ_ν` (W3). A P2 law is
   uniform with mass `1/q` on the line `{f = c}`. By (W2) it maps to the Pauli
   eigenprojector `Π_{f=c}` itself, a pure state of trace 1.
4. **Registering a slot `f` of a meter that then stays terminal (P1).** By (W2)
   and (W3),
   `tr_m[(I ⊗ Π^m_{f=c})(A(λ_c) ⊗ A(λ_m))] = A(λ_c)·[f(λ_m) = c]`.
   This is "measure the meter's Pauli `f`, then discard the meter". A registered
   meter is never coupled again and is re-registered only on the same functional
   (AP1 SA-1(b)). Keeping it is therefore equivalent to discarding it.
5. **Discarding.** Marginalizing is the partial trace (W3, W1).
6. **Feedback and heralds.** Record-conditioned armings and translations are
   classically controlled Cliffords. Heralds are independent classical coins.

Compositions and convex combinations of CP maps are CP. ∎

**Scope.**

- The proof does not use PR-QA's case split. The
  [masked-record example](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/PROOF-RECOVERY.md#L75)
  is covered automatically.
- Hidden backgrounds whose R-W image is not a state are not covered.
- P1 is load-bearing. Without it, registration is a restriction without a kick,
  with Choi eigenvalue `−1` (c7; AP1 C9).
- P2 is load-bearing. With a sharp meter the read has Choi eigenvalue `−1` (c7′;
  AP1 C4, E-AR).

### Node 4. Proposition AS: CP characterizes the affine symplectic bijections

**Proposition AS.** Let `q` be an odd prime and `g` a bijection of
`F_q^{2n}`. Define `T_g(A(λ)) = A(gλ)`. Then `T_g` is CP iff `g` is affine
symplectic.

*Proof.*

- **(⇐)** This is (W4).
- **(⇒) Purity.** `T_g` permutes an orthogonal basis of equal norms (W1). So it
  is trace-preserving, unital and a Hilbert–Schmidt isometry, and if it is CP it
  sends pure states to pure states. Write `T_g = Σ_i K_i · K_i†`. For every pure
  `ψ`, the vectors `K_iψ` are pairwise parallel, because a sum of rank-one terms
  has rank one only then.
- **(⇒) One Kraus operator.**
  - Suppose some `K_i` has rank at least 2.
  - For each `j`, write `K_jψ = λ(ψ)K_iψ` wherever `K_iψ ≠ 0`. Comparing at
    `ψ + φ`, for `ψ, φ` with independent images, gives `λ(ψ) = λ(φ)`.
  - If `K_iψ = 0`, take `y, y′` with independent images. Comparing at `ψ + ty`
    for all `t` forces `K_jψ = 0`.
  - Hence `K_j = λK_i`, and `T_g = Ad(K)` with `K†K = I`.
  - If instead every `K_i` has rank at most 1, the outputs share one range.
    `T_g` is then constant on pure states, which contradicts injectivity.
- **(⇒) Clifford.** `Ad(U)` permutes the `A(λ)`, so `U` is Clifford by (W8).
  Write `U = w(a)μ(S)`. By (W4), `A(gλ) = A(Sλ + a)` for every `λ`, and the
  `A(λ)` are distinct, so `g = S· + a`. ∎

**Second proof of (⇒).** Apply `T_g ⊗ id` to the stabilizer state uniform on
the graph `{(λ, Rλ)}`, with `R` anti-symplectic (W7). The output is pure and
has a nonnegative Wigner function. By (W5) it is a stabilizer state, and by
(W7) its support is an affine Lagrangian. That support is the set
`{(gλ, Rλ)}`, a graph over the reference coordinates, so `g` is affine
symplectic. This form also gives Proposition T′ (node 8).

**Consequences (§A.34; each direction named).**

- **Among all ontic bijections:** CP ⇔ affine symplectic. (⇐) is W4. (⇒) is the
  proof above.
- **Within rules of the native second-order form**
  `u′ = F(u) − v, v′ = u`: affine symplectic ⇔ (`F` affine) ∧ (the linear part
  of `F` is symmetric).
  - (⇐): an affine `F = K· + b` with `K = Kᵀ` gives a step that is affine and,
    by AP1 §4.1, symplectic.
  - (⇒): if the step is affine, then `F` is affine. If the step is symplectic,
    then `K = Kᵀ` by the same identity.

  This second equivalence does not hold among all bijections. Many affine
  symplectic maps are not of the second-order form.
- **O3 at odd `q`, in its precise form.** The native rule lies in this class.
  There is one fixed frame, singled out by the comparator's Clifford covariance,
  in which this class is exactly the CP bijections. The operation set is not
  restricted: anti-symplectic, non-reciprocal and non-affine bijections all
  remain conceivable, and each is computed to be non-CP.
- **Verdict for O3 at odd `q`: pass natively.** This holds for all of N and
  N+NNB, adaptive protocols included. P1 and P2 are load-bearing, and the frame
  carries the qualification above.
- **At `q = 2`: fails** (QA Lemma R, FB). CC-OFF(a) is green (node 2).

### Node 5. Lemmas S and G: bipartite N is monomial in one product basis (O2 within N)

**Sectors.** In the encoded frame `J^{−t}`, the encoded `z` of a colour-`χ` cell
has type `χ` and its `x` has type `χ + 1`, both mod 2 (QA G1 types). Write `E`
for type 0 and `O` for type 1.

**Lemma S (sector splitting).** Assume `q` prime, a bipartite armed coupling
graph, and any process of N, record feedback included. At every tick, the
subspace `D` of functionals determined by known slots and registered records
splits as `D = D_E ⊕ D_O`.

*Proof.* Condition on all records. Each branch is then a fixed sequence of
graded linear steps and constant translations. Translations do not change which
functionals are determined (QA Lemma Q (iii)). `D` is spanned by two kinds of
single-sector vector:

- transported known slots (P2 supplies one slot per cell);
- transported registered record slots.

A span of single-sector vectors splits. ∎

**Corollary S.** Combine Lemma S with AP1 Lemma 3 (isotropy) and
`ω(z, x) = 1`. No active cell ever has a determined mixed functional `a z + b x`
with `ab ≠ 0`. The phase gate `P`, which maps the `x`-eigenstate to the
`(x − z)`-eigenstate, is therefore unavailable. At `q = 2` this is AP1's type
invariant, extended to all of N with feedback.

**Lemma G (available unitaries are graded).** Assume the hypotheses of Lemma S
and `q` odd. Let a protocol act on a carrier block `C` as a unitary channel
`Ad U`. Then `U` is a graded Clifford, `U = w(a)·μ(A ⊕ A^{−T})` on `(E_C, O_C)`.

*Proof.*

1. `U` is Clifford by Theorem W and (W6).
2. Take an untouched reference copy `R` of `C`, with the same colours.
3. Prepare the pure stabilizer state on `C ∪ R` whose determined functionals
   are `e_c − e_r` for `e ∈ E` and `o_c + o_r` for `o ∈ O`. It is reachable in
   N. Start from carrier cells with a known `O`-sector slot and reference cells
   with a known `E`-sector slot (P2). For each pair, apply the graded
   transvection that adds the carrier's `E`-slot to the reference's `E`-slot,
   through a mediator. For a colour-0 pair this is `z_r += z_c`, `x_c −= x_r`,
   giving determined `z_r − z_c` and `x_c + x_r`.
4. Apply `U` on `C`. The output is pure, so every record branch has that same
   output, and its determined subspace on `C ∪ R` is the Lagrangian
   `L_out = {(Ue, −ē)} + {(Uo, ō)}`. By Lemma 3, `D_b ∩ (C ∪ R)` is isotropic
   and contains `L_out`, so it equals `L_out`. By Lemma S it splits by sectors.
5. Take `e ∈ E_C`. The `O`-part of `(Ue, −ē)` is `((Ue)_O, 0)` and must lie in
   `L_out`.
6. An element of `L_out` with zero `R`-part is zero, since the `R`-part of
   `(Uf, −f̄) + (Ug, ḡ)` determines `f` and `g`. So `(Ue)_O = 0`, and
   `U(E_C) ⊂ E_C`.
7. Likewise `U(O_C) ⊂ O_C`. Symplecticity then forces the form `A ⊕ A^{−T}`. ∎

**The basis.** Let the **sector-adapted product basis** have, as each cell's
position slot, its `E`-sector encoded slot: `z` for colour-0 cells and `x` for
colour-1 cells. In this basis:

- `μ(A ⊕ A^{−T})` is the permutation unitary `|y⟩ ↦ |Ay⟩`, up to phase. It
  conjugates `Z^b` to `Z^{A^{−T}b}` and `X^a` to `X^{Aa}`, and Weyl
  irreducibility fixes it up to phase;
- Weyl operators are monomial.

So every available reversible encoded operation of bipartite N is monomial in
this basis.

**A different basis gives a different answer.** In the colour-blind basis,
where every cell's position slot is `z`, the odd-tick edge step
`z_1 += k x_2, z_2 += k x_1` is a CP Clifford that is **not** monomial. This is
why O2 is stated without reference to a basis.

**Self-checks.** Random graded protocols at `q = 3, 5` gave no determined mixed
functional. With an NNB edge added, the breaking control fires (c6). CC-OFF(b)
is green.

**Verdict for O2 within N (bipartite, odd prime `q`, adaptive): fails** under
the basis-free criterion. The native reads are phase-sensitive, but every
available reversible encoded operation is monomial in the sector-adapted basis.

**At `q = 2`.** Lemma G is not proved there, since it uses Theorem W and (W6).

- Non-adaptive gradedness is QA node 1 (G1).
- Corollary S holds with feedback, so there is no determined mixed functional
  and no single-cell `P`.
- Whether every adaptive unitary is graded at `q = 2` is open (QA §4.3).

### Node 6. Lemmas N and M: NNB at odd `q`, the composition battery and its limit

**Lemma N.** Take two same-colour cells in the common encoded frame, with
coordinates `(z_1, z_2, x_1, x_2)` and `S = [[0,1],[1,0]]`.

- **The two NNB ticks.** `Na_k: x ↦ x + kSz` and `Nb_k: z ↦ z + kSx`. The coupled
  step equals `J ∘ (u, v ↦ v − kSu)`.
- **The graded transvections.**
  - `G = diag(A, A^{−T})` with `A = [[1,0],[1,1]]`. This is QA's `C12`.
  - `G′ = diag(A′, A′^{−T})` with `A′ = [[1,1],[0,1]]`. This is `C21`.

  Both are available through the returned-mediator commutator, which is valid
  over any ring.

Then:

- `G^{−1} Na_k G Na_{−k}` gives `x_1 += 2k z_1`, with cell 2 returned;
- `G′^{−1} Nb_k G′ Nb_{−k}` gives `z_1 += −2k x_1`, with cell 2 returned.

*Proof.* `G^{−1}Na_kG` is the shear `k AᵀSA = k[[2,1],[1,0]]`, and subtracting
`kS` leaves `[[2k,0],[0,0]]`. Likewise `A′^{−1} S A′^{−T} − S = [[−2,0],[0,0]]`. ∎

At odd `q` both single-cell shears are available on cell 1, with any
coefficient. They generate `SL(2, F_q) = Sp(2, F_q)`. With the constant
translations this gives the full single-qudit Clifford group modulo phases,
`F_q² ⋊ SL(2, F_q)` (W4). At `q = 2` both words are the identity, consistent
with QA Lemma Q. Self-check c4.

**Lemma M (no monomial product basis).** At odd prime `q`, no orthonormal basis
`B` of one cell makes every element of the single-qudit Clifford group monomial.
Hence, under N+NNB, no fixed product basis makes every available reversible
encoded operation monomial.

*Proof.*

1. Monomials in `B` permute the `q` lines `ℂb`. This gives a homomorphism
   `φ: Ḡ → S_q` from the projective Clifford group `Ḡ = T ⋊ SL(2, F_q)`, where
   `T ≅ F_q²` is the Weyl group.
2. `K = ker φ` consists of classes whose lifts are diagonal in `B`. Their lifts
   commute exactly.
3. `K ∩ T` is therefore isotropic. It is normal, hence `SL(2)`-invariant. Since
   `SL(2)` is transitive on nonzero vectors, `K ∩ T` is `0` or `F_q²`. The
   whole of `F_q²` is not isotropic, so `K ∩ T = 0`.
4. Both `K` and `T` are normal, so `[K, T] ⊂ K ∩ T = 0` and `K` centralizes `T`.
   An element `w(a)μ(S)` centralizes `T` projectively iff `S = I`. So
   `K ⊂ T ∩ K = 0`.
5. Then `T ≅ Z_q²` embeds in `S_q`. That is impossible, since `q²` does not
   divide `q!`.
6. For a product basis, an available `U ⊗ I` (partner returned) that is monomial
   in `B_1 ⊗ …` is monomial in `B_1`. ∎

**C-COMP for `P` (N+NNB, odd `q`).** `P` is an exact ontic permutation. By
Theorem W, protocols compose as instruments do, and reads are exact Lüders
instruments as linear maps.

- **K1.** `P²X_0` is the `(x − 2z)`-eigenstate with value 0.
- **K2.** `P^q = I`.
- **K3.** On `R0` the final `X` is deterministic. On `R1`, after record `c`, the
  final `X` is uniform and independent of `c`. G2 does not apply, because NNB
  breaks G1.
- **K4–K6.** These hold for every one of the `q + 1` axes and for the failure
  branch. K5 needs only `P^a` and the native reads.

All six match the comparator.

**CC-IMIT (measure-and-prepare).** `M_P` reads `X`, records `c`, and prepares
the law uniform on `{x − z = c}`.

- On the `X_c` family it matches every one-step read (c5, exact).
- It fails K1: `M_P ∘ M_P` on `X_0` makes the read of `x − 2z` uniform.
- It fails K5: on `Z_0` the `Z` read becomes uniform.

**CC-IMIT′ (a classical statistical model).** Gross's Wigner-sampling model of
the odd-`q` stabilizer subtheory is a noncontextual hidden-variable model. It
reproduces every K1–K6 sequence, because the reachable fragment lies inside its
operational scope (Spekkens §V.A). The native mechanism is such a model
(Proposition C(d)). **CC-IMIT′ passes C-COMP.**

**D2 outcome.** C-COMP discriminates measure-and-prepare imitation only.

**Verdict for O2 under N+NNB at odd `q`.**

- At stabilizer scope, O2 passes on the basis-free criterion (Lemmas N and M)
  with C-COMP passed.
- The operation is realized by a noncontextual hidden-variable model. No test
  within the reachable fragment distinguishes it from a classical statistical
  imitation.

At `q = 2` under NNB, `S` passes C-COMP by QA
[node 8](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L560),
but O3 fails.

### Node 7. The ceiling at odd `q`, and qubit encodings

**Proposition C (odd prime `q`, R-W).** For every protocol of N or N+NNB:

- **(a)** Every reachable encoded state has a nonnegative Wigner function, since
  native laws are nonnegative. By (W5), reachable pure states are stabilizer
  states.
- **(b)** Every available encoded unitary channel is Clifford (W6). The Clifford
  group modulo phases is finite, so there is no encoded unitary of infinite
  order. The transported C-ROT holds.
- **(c)** The single-state quarter phase `D_i` is not Clifford. Any two nonzero
  entries of a Weyl operator differ by a `q`-th root of unity. `D_i X D_i†` has
  two entries that differ by `i`, which is not a `q`-th root of unity for odd
  `q`. So C-PH holds.
- **(d)** The reachable class lies inside the odd-prime quadrature epistricted
  theory. Spekkens (arXiv:1409.5041 §V.A–B) shows that theory is operationally
  equivalent to the stabilizer subtheory and is a local noncontextual
  hidden-variable model.

**Observation E (FB on finite abelian groups).** FB §§3–4 use four facts:

- the encoded bits are homomorphisms `f_a: V → Z_2`, pairwise distinct;
- preparations are uniform on level sets;
- the kernel is common to all preparations;
- translations map level sets to level sets.

None of these needs `F_2`-vector-space structure. Uniform level-set qubit
encodings exist iff `Hom(V, Z_2)` has rank at least 2, so that three distinct
nonzero homomorphisms exist. For `V = Z_m^{2n}` this holds exactly when `m` is
even. For every such `V`, including a native `Z_4` alphabet, FB's dichotomy
holds whenever all translations are available.

| Configuration group | Uniform level-set qubit encodings | Combined `S` + C-CP |
| --- | --- | --- |
| `Hom(V, Z_2)` of rank ≥ 2 (`q = 2`, `Z_4`, …) | Exist | Fails whenever all translations are available (FB, extended) |
| Odd order (odd `q`) | None | C-CP holds for all of N (Theorem W). No quarter phase (Prop. C) |

This agrees with two results from the literature. Clifford-covariant Wigner
functions exist only in odd prime-power dimension and not in even (Zhu,
abstract). Every ontological model of the single-qubit stabilizer subtheory is
contextual (LWE Theorem 1, as read in AP1 §5.2).

**What this leaves for qubits.** At odd order, reciprocity separates rotations
from reflections. A qubit-compatible selection would have to break FB's H-L or
H-T by a sourced mechanism. A change of native alphabet alone does neither.
Proposition C is an odd-`q`, R-W statement and does not bear on even-order
qubit contextuality.

### Node 8. Theorem T and Proposition T′: in-world control against selection (O1 against O3)

**Theorem T.** Let `q` be an odd prime and use R-W. Take a fixed bijective rule
on a phase space that includes a controller cell, whose encoded action on all
joint laws is CP. By Proposition AS every tick of the rule is affine symplectic.
By Lemma A, a setting held in the controller can then only translate values. ∎

**Proposition T′ (exact, every odd prime `q`).** The setup:

- a carrier block `a` and a reference block `r` of `n_a` cells each;
- one controller cell `c`;
- `m = 2n_a + 1` cells in total;
- a rule that leaves `u_c` and `λ_r` unchanged and sends
  `λ_a ↦ S(u_c)λ_a + t(u_c)`, with each `S(s)` invertible linear;
- `v_c` changed by any function that keeps the rule bijective.

**The static-slot hypothesis.** The rule must leave `u_c` unchanged, and a
native cell does not. Under the second-order rule its lab slot runs
`z, −x, −z, x` over successive ticks (AP1 §4.2 frame). A time-independent
`k(u_c)` on a native cell would therefore be controlled by complementary
functionals on alternate ticks. T′ applies to:

- a controller cell exempt from the native rule; or
- a native controller used at one tick parity only.

Either is a supplied element (§6.2).

Take as input the law uniform on
`L = {(λ_a, Rλ_a)} × {(s, 0) : s ∈ F_q}`, with `R(u, v) = (u, −v)` per cell.
This input is reachable in N. The carrier–reference correlation is obtained by
graded transvections (node 5, Lemma G proof). The controller is a ready cell
with known `v_c`, which is X-type.

- **(i)** If `S(s)` depends on `s`, the output's encoded operator is not
  positive semidefinite (PSD).
- **(ii)** Suppose every `S(s)` is symplectic and, given `u_c`, the
  controller's `v_c` is uniform and independent of all other cells. Then the
  output is a valid state for every carrier and reference input.

*Proof.*

- **(i)** `L` is an affine Lagrangian, so the input is a stabilizer state (W7).
  1. The output is the uniform law on `g(L)`, with `|g(L)| = q^m`.
  2. Hence `ρ_out = q^{−m} Σ_{g(L)} A(λ)` has `tr ρ_out = 1` and
     `tr ρ_out² = q^{−2m}·q^m·q^m = 1` (W1). Its Wigner function is the law,
     which is nonnegative.
  3. If `ρ_out ≥ 0`, it is pure. By (W5) it is a stabilizer state, and by (W7)
     `g(L)` is an affine subspace.
  4. Project onto `(λ_a′, λ_r, u_c)`. The image is the graph of
     `(λ_r, s) ↦ S(s)R^{−1}λ_r + t(s)` over all of `F_q^{2n_a} × F_q`.
  5. An affine subspace that is a graph over a whole space is the graph of an
     affine map. So `S(s)` is constant.
- **(i), extended.** The same argument applies to any pure stabilizer
  controller law that is not a `u_c`-eigenstate. Then `u_c` ranges over all of
  `F_q`, and the projection in step 4 is again a full graph.
- **(ii)** Under this hypothesis the joint input is classical–quantum,
  `Σ_s p_s |s⟩⟨s| ⊗ X_s` with `X_s ≥ 0`, and `v_c` stays uniform and
  independent. The output is `Σ_s p_s |s⟩⟨s| ⊗ (Ad U_{S(s),t(s)} ⊗ id)(X_s)`,
  which is positive. ∎

**Reading.**

- Within this class, the two directions are as follows.
  - (⇐) Proposition T′(ii): symplectic branch maps with controllers whose
    `v_c` is uniform and independent given `u_c`.
  - (⇒), symplectic half: by Proposition AS, with a `Z_s` controller.
  - (⇒), confinement half: shown only in this sense. If any pure stabilizer
    controller law other than a `u_c`-eigenstate is admissible, C-CP fails on a
    reachable input (T′(i), extended). This is not shown for every non-diagonal
    controller law.
- An X-type controller on a reachable input produces a non-quantum encoded
  state.
- This is the exact, all-`q` statement. The `q = 3` floating-point instances in
  §9 (c8, c9) are controls consistent with it and carry no verdict.
- Take a controller with a static slot, or used at one tick parity, that is
  read by a fresh terminal ready meter before each controlled tick. It is in
  such a law at every coupling (§6.2, CTRL-MON).

**SM §3.1 as a candidate source.** SM's state-dependent coupling graph
([SM:104](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L104),
[explicit construction](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L110))
couples `i` to `i + 2`, a same-sublattice (NNB-type) edge, when `x_{i+1} = 0`.
Read at odd `q` in R-W:

- the rule is a non-affine bijection, so its joint encoded action is not CP
  (Proposition AS);
- in a branch with the switching cells fixed, on a ring of `L ≥ 5` sites, `i`
  reads `i + 2`, while `i + 2` reads `i + 1` and `R(i + 2, x) ∈ {i + 3, i + 4}`,
  never `i`. The adjacency is not symmetric, so the branch map is not
  symplectic (AP1 §4.1) and not CP;
- its controlling cells are ordinary dynamical cells, which Proposition T′(i)
  does not permit.

These are consequences of the paper argument. No computation on the ring was
run.

## 4. Shortcut checks

| Check | Finding |
| --- | --- |
| SC-1 Imported quantum behaviour | **No import in the dynamics.** Every native step is a bijection of configurations, and CP is computed as a test, not assumed. Among bijections the native class is exactly the CP class (Proposition AS). Three qualifications. (1) The frame R-W is singled out by Clifford covariance, a property of the comparator; O3 is therefore stated as "the native rule is in a class that is exactly the CP class in one fixed frame" (node 4). (2) The model contains no interference. It is the noncontextual epistricted model (Prop. C(d)), so no interference is derived because none exists. (3) The controller confinement of M1 in its bare form, and the terminality of unregistered monitoring meters in CTRL-MON, are restrictions motivated by the CP target. Both are flagged under CC-RECON (§6.2). The selection also inherits the status of A5 (affine part derived from amplitude-scale gauge, linearity imposed) and of the `−x(t−1)` memory term (node 2) |
| SC-2 Hidden external control | **Present, and disclosed.** P3 selects every coupling, coefficient and arming. This includes Lemma N's words (`k = 2^{−1}`, `−k`), the mediator schedule for `C12` and `C21`, every NNB edge, and the read axis (tick parity). An outside agent executes the adaptive feedback. P2 and H-PREP supply the ready cells, the known values and the reference correlations; heralds are supplied. Lemma A shows that no fixed affine rule can internalize the setting. M1 does not remove observer dependence while "controller" is defined by registration (§6.2). CTRL-MON still needs, supplied: per-tick delivery and arming of fresh meters (P3, E-iso or a conveyor); a static controller slot, or a parity clock or P3-type arming (node 8); the P2 meter supply; and terminality of unregistered meters |
| SC-3 Representation versus physical implementation | **Representation only.** On the physical carrier every step is a permutation of `F_q^{2n}` (AP1 Lemma 2; the kernel ceiling holds). `U_P` exists only in R-W, and even there monomiality depends on the basis (node 5). What is physical is the record statistics, which equal the stabilizer-circuit statistics and are produced by an exact noncontextual hidden-variable model. The capability reached at odd `q` is therefore exactly what a classical statistical model provides |

## 5. Ledger

| Item | Content | Classification | Status |
| --- | --- | --- | --- |
| N1 | Second-order linear update `x(t+1) = Σ k x_nbr − x(t−1)` with symmetric coupling; symplectic with multiplier `+1` | Native | Substratum A4, A5; SM L224; AP1 §4.1. Carries O3 at odd `q`. The `−x(t−1)` sign is load-bearing (node 2) |
| N1-A5 | Linearity (affine part derived, linearity imposed) | Native premise, partly derived | Substratum A5. The selection inherits this status |
| N1-CI | Center independence | Native | Used by QA G1 and Lemma S, not by symplecticity |
| N1-BIP | Bipartite nearest-neighbour graph | Native, selected branch | SM L224–L226. Carries Lemmas S and G |
| Nq | Alphabet `F_q`; `q` not fixed | Native parameter | Both characteristics computed, none adopted. `α = 1/d` needs `3 ∤ q` (SM §2.7), which excludes `q = 3` for the normalized native coefficient, the main self-check case. The results use P3 coefficients |
| N2 | Uniform law on unknown slots | Native measure, through H-PREP | As in AP1 and QA; H-INF-μ for an infinite hidden sector |
| P1 | Terminal registration | Supplied (AP1) | Load-bearing for Theorem W (c7) |
| P2 | Half-known ready cells | Supplied (AP1) | Load-bearing for Theorem W (c7′) and Lemma S |
| P3, E-iso | Per-tick, per-edge arming; isolation | Supplied (AP1) | O1 fails on P3 (Lemma A) |
| H-PREP | Record-conditioned classes read as preparations | Supplied (open hypothesis) | As in AP1 |
| NNB | Armable same-sublattice symmetric coupling | Supplied (QA conditional premise) | At odd `q` it gives the Clifford group with C-CP intact |
| R-W | Gross's phase-space frame, fixed for all settings | Mathematical representation, singled out by Clifford covariance | Comparator dictionary only |
| M1 / CTRL-MON | §6.2: non-affine coefficient `k(u_c)`; P2 meter supply; terminality of unregistered meters; per-tick meter delivery and arming; static controller slot or parity clock | Supplied (conditional premise, not adopted). CC-RECON flag on the bare confinement and on the unregistered-meter terminality | Missing premise for O1; removes P3 from the setting value only |
| I1 | Qubit and qudit stabilizer comparators | Imported (comparator) | — |
| I2 | Gross Theorems 2, 3, 6, 7, 19, Lemmas 4, 8, 9, 29; Spekkens §V.A–B; Zhu (abstract); LWE Theorem 1 (via AP1) | Imported literature | §8.2 |

## 6. Outcome

### 6.1 Obligation verdicts

| Obligation | `q = 2` | Odd prime `q`, N | Odd prime `q`, N+NNB |
| --- | --- | --- | --- |
| O1 Physical source | Supplied (P3, H-PREP, P2); fails natively (Lemma A) | Same | Same; NNB is also P3-armed |
| O2 Capability | Reads only (AP1); `S` needs NNB (QA); no single-cell `P` (Corollary S); adaptive gradedness open | Fails: every reversible encoded operation is monomial in the sector-adapted basis (Lemmas S, G) | Passes at stabilizer scope (Lemmas N, M; C-COMP). Not separated from classical imitation within the reachable fragment (CC-IMIT′). No quarter phase, no infinite-order unitary (Prop. C) |
| O3 Selection | Fails (QA Lemma R, FB) | **Pass natively**, in the form of node 4 | **Pass natively** |
| O4 Continuation | Pass under P1, P2, H-PREP (AP1 §4.4) | Pass (Theorem W) | Pass |
| C-NS | Green with wing-local cells (QA) | Green: wing-local operations; Main [cone theorem](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Main.md#L366) | Green with wing-local NNB edges |
| C-LEAK | Green within a wing; shared parity signals (QA) | Green: every reuse or recombination protocol is a stabilizer protocol (Theorem W) | Green |
| C-Q | Lemma Q protects `Q* = 1` | `Q = Σ u_i v_i` is not conserved (`Q′ = uᵀKu − Q`); no parity sector is needed in the one-cell frame | Same |
| Composites | Fail Mermin–Peres (QA node 10) | Stabilizer correlations, Bell-local (Prop. C(d)) | Same |

### 6.2 Type (ii) stop: the missing premises

**M1 (primary): a controller-dependent coupling with controllers kept diagonal
in their controlling slot.**

- **Why it is needed.** Lemma A forces any in-world setting source to be
  non-affine. Proposition T′ gives three conditions:
  - (⇐) symplectic branch maps `S(s)` with controller `v_c` uniform and
    independent of all other cells given `u_c` suffice;
  - (⇒) symplectic branch maps are necessary;
  - (⇒) confinement is necessary whenever some pure stabilizer controller law
    other than a `u_c`-eigenstate is admissible.
- **Bare form, CTRL-REC: "the controller is a registered record".** This form
  does not meet the bar, for three reasons.
  - *"Registered" has no dynamical meaning.* Registration is observer
    conditioning. The rule `k(s)` acts the same way on unregistered cells, and
    there Proposition T′(i) gives non-quantum states.
  - *The confinement is CP-motivated.* Confining controllers to record laws, and
    keeping the record's conjugate slot unrecoverable, are adopted only so that
    non-quantum states do not appear. This is the controller-side analogue of QA
    premise I and is flagged under **CC-RECON**.
  - *No independent prediction (§A.29).* Its candidate consequences do not
    qualify: "controlling records are irreversible archives" restates the
    confinement, "each setting consumes a record" is definitional, and the
    violation of SM §2.7's additive-automorphism gauge is a conflict, not a
    prediction.
- **Dynamical form, CTRL-MON.** The coefficient is a fixed function `k(u_c)` of
  a controller slot, and the branch maps are symplectic (symmetric adjacency in
  each branch). Before every controlled tick, a fresh ready meter reads the
  controller through a coupled tick, and the meter is never coupled to anything
  again.
  - *Controller dynamics (required).* A native controller cell rotates: its lab
    slot runs `z, −x, −z, x`. Monitoring at every tick would alternate `Z` and
    `X` reads (AP1 §4.2), which randomizes the setting at every odd tick. As
    stated without a further element, CTRL-MON erases the setting it is meant
    to hold. It needs one of two supplied elements:
    - a controller cell exempt from the second-order rule (non-native); or
    - control and monitoring confined to one tick parity, which needs a clock
      or P3-type per-tick arming.
  - *Derivation (paper).* The read with the meter discarded is the
    `Z`-dephasing channel `Δ_Z` on the controller (Theorem W). After `Δ_Z`,
    every joint input is block-diagonal in `u_c`, so by Proposition T′(ii) the
    composite `T_g ∘ Δ_Z` is the controlled channel with Kraus operators
    `|s⟩⟨s| ⊗ U_{S(s)}`. With the monitoring meters discarded, it is CP on
    **all** controller–carrier inputs. The joint map that includes the meters is
    the bare non-affine rule. Its CP failure returns if any meter's kick slot
    is recovered. Self-check c10 is a control.
  - *What it relocates.* CTRL-MON removes the restriction on controller laws.
    It relocates the supplied premise rather than removing it. What remains
    supplied:
    - (a) the P2 supply of ready meters;
    - (b) a terminality condition on **unregistered** monitoring meters, a
      supplied strengthening of P1. If such a meter is recombined, the dephasing
      can be undone (AP1 §4.5 eraser) and Proposition T′(i) applies again. Its
      only motivation here is to keep the dephasing irreversible. AP1's
      archive argument covers registered records only. **CC-RECON applies to
      this condition as well**;
    - (c) per-tick delivery of a fresh meter to the controller and disarming of
      the used edge, by P3/E-iso arming or a supplied meter conveyor. A cell at
      a fixed site would otherwise be coupled again at the next tick;
    - (d) a static controller slot or a parity clock (controller dynamics,
      above);
    - (e) the non-affine coefficient dependence, which violates A5 and the gauge
      of [SM §2.7](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L96).
  - *What it buys.* It removes P3 from the setting **value** only. Per-tick
    meter delivery and arming, and the clock or static slot, remain supplied. It
    does **not** give O1 a pass: by §2.3, O1 is still "supplied", resting on
    (a)–(e), H-PREP and CTRL-MON itself.
  - *Independent consequences.* None established beyond resource accounting:
    each controlled coupling consumes ready meters, and the setting value is
    copied into the environment at every tick. Whether the latter has a testable
    signature is open.
- **Relation to existing records.**
  - [Record-control](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/record-control-20261107/DESIGN.md#L67)
    shows that a record-bearing field natively enters a neighbouring nonlinear
    gate. It stops because the gate output is masked by other fields and private,
    so no usable controlled operation follows. CTRL-MON assumes exactly the clean
    coefficient dependence that record shows the native Native A gate does not
    supply. Proposition AS is an odd-`q` statement and does not decide the `F_2`
    Native A gate.
  - [Setting-source feasibility](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/substratum/continuous-substates/native-setting-source-feasibility.md#L59)
    shows that record-derived labels cannot steer an independent coordinate
    without a state-changing operation. It marks a supplied ideal actuator as a
    countercontrol, not a source.
  - CTRL-MON is such a supplied actuator. It does not close that gate.
- **What would derive it.** A symmetrized form of SM §3.1's state-dependent graph
  with continually monitored switching cells. The first check is whether SM's
  constraints (i)–(iii)
  ([SM:108](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L108))
  allow symmetric adjacency with monitored switches. The explicit ring fails
  both conditions (node 8).
- **What would rule it out.** Retaining the additive-automorphism gauge as a
  physical symmetry of every coupling, or retaining terminality only for
  registered cells.
- **What would weaken it.** Nothing smaller was found. A one-way controller is
  equally CP-compatible after `Δ_Z` (c10), but it drops reciprocity, which
  carries O3. P3 is M1 with an external controller.

**M2 (NNB, carried from QA).** At odd `q`, NNB gives the single-qudit Clifford
group with C-CP intact (Lemmas N, M; Theorem W). QA's reflection cost does not
arise. Derivation and ruling-out conditions are as in
[QA §4.1](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L805).

**M3 (qubit quarter phase with C-CP; open, no premise proposed).**

- At odd order there is no uniform level-set qubit encoding.
- For `Hom(V, Z_2)` of rank at least 2, FB's dichotomy holds (Observation E).
- A sourced mechanism must break H-L or H-T without a restriction motivated by
  the target, which would be QA premise I and is flagged by CC-RECON. By LWE
  Theorem 1 it must be contextual.
- First check: whether an even-order carrier with a protected inaccessible
  sector (QA Lemma Q) admits non-uniform preparations, outside H-L, reachable by
  native reads under P1 and P2. QA's U′ preparations are uniform level sets.

### 6.3 No V3 round

The verdicts rest on paper proofs: Lemmas A, S, G, N, M, Theorems W and T,
Propositions AS, T′ and C, and Observation E. The open items, sourcing M1 and
M3, concern which physical principle holds, not a finite search.

### 6.4 Not claimed

- A physical setting source.
- Adoption of NNB, M1 or any `q`.
- An escape of C-PH or C-ROT.
- Contextuality, interference, a Bell violation, Born-rule selection beyond the
  stabilizer values, or `J_exact(A)`.

Theorems W and T and Propositions AS and T′ are paper derivations that use
Gross's theorems. They are not kernel theorems.

### 6.5 Bearing on Q-B

The outcome is (ii), so nothing is handed to Q-B. Proposition AS has a continuum
counterpart in the Liouville epistricted theory (Bartlett, Rudolph and Spekkens,
arXiv:1111.5057; abstract via AP1). If Q-B is activated, its first test is
whether AS survives the real or large-`q` limit: exact continuous symplectic
rotations of quadratures, with C-CP. A qubit `rot` would still need non-Gaussian,
Wigner-negative resources. This is not derived here.

## 7. Classification (§A.31) and assumption-watch markers

| Finding | Class |
| --- | --- |
| Lemma A: a fixed affine rule cannot select a linear part from an in-world setting | New for this programme |
| Theorem W: at odd `q`, every protocol of N (adaptive, NNB, recombination) is a stabilizer instrument in R-W | New for this programme; built from Gross's covariance and Spekkens' equivalence |
| Proposition AS: in R-W at odd `q`, CP ⇔ affine symplectic, for ontic bijections | New for this programme |
| Theorem T and Proposition T′: in-world control under a static controller slot is quantum-compatible if branch maps are symplectic and `v_c` is uniform and independent given `u_c`. It fails if a non-eigenstate pure stabilizer controller law is admissible | New |
| `q = 2`: R1 is not `Sp(2, F_2)`-covariant, and the multiplier cannot flag its reflections | Elaborating (QA, AP1 C8, Zhu) |
| Lemma S (every prime `q`) and Lemma G (odd `q`): bipartite N, with feedback, has no mixed determined functional, and at odd `q` is monomial in the sector-adapted product basis. Adaptive gradedness at `q = 2` is open | New; extends AP1's type invariant and QA G1 to the adaptive class |
| Lemmas N and M: in the one-cell frame, NNB gives the single-qudit Clifford group exactly iff 2 is invertible. (⇐) is Lemma N; the witness for (⇒) is QA Lemma Q, since at `q = 2` a single-cell mixed functional has `Q* = 1`. No product basis is then monomial. QA node 8 does give `S` at `q = 2`, in a two-cell encoding | New for this programme |
| C-COMP is passed by the mechanism's own classical model (CC-IMIT′) | Confirming (Spekkens, Gross); a limit on what C-COMP can establish |
| Observation E | Elaborating (FB) |
| Proposition C | Confirming (Gross, Spekkens) |

**Assumption-watch markers.**

- **Memory-term sign.** The multiplier `+1`, and with it the odd-`q` selection,
  needs the `−x(t−1)` term.
  [Main L296](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Main.md#L296)
  displays `u′ = Σu + v`, and the remark after its Lemma 1
  ([L304](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/Main.md#L304))
  states that the factorization "holds verbatim over `Z_q`". That remark
  concerns Lemma 1's cross-block factorization, which does not depend on the
  memory sign, and is not in error. The divergence is only over which rule is
  native at odd `q`: the displayed `+v` rule is anti-symplectic there, unlike
  Substratum A4 and SM. It is logged for a separate unit. No edit is implied
  here.
- **Alphabet-size hypothesis.** The encoded operation class differs qualitatively
  between `q = 2` and odd `q`. Any correspondence built for
  [SM's hypothesis](https://github.com/amaybaum/incompleteness/blob/313a93efcab581465919a4ff82ecda1e4b81e990/papers/SM.md#L94)
  must account for this. It is not a refutation.
- **Linearity and reciprocity select at odd `q`.** Any nonlinear, state-dependent
  or non-symmetric rule must re-check C-CP on joint laws. This covers the SM
  §3.1 graph, Native A and P-SDC (Proposition AS).
- **Registers used as controllers.** They are quantum-compatible only while kept
  diagonal in the controlling slot (Proposition T′). Under CTRL-MON that depends
  on the terminality of the monitoring meters, and on a static controller slot
  or a one-parity schedule.

## 8. Sources

### 8.1 Repository sources (all on `main@313a93ef`)

All repository sources are on `main` at the pinned commit and are cited at their
stated scope. Issue and PR comments are **provenance** only.

| Source | Use | Classification (§A.42 item 8) |
| --- | --- | --- |
| AP1 Lemma 2, §4.1, §4.2, Lemma 3, Lemma 5, C1, C4, C8, C9, §4.4, §4.5, §5.2, §5.6, ledger | Ceiling; native read; isotropy; R1; `q = 2` baseline | Support on `main` (#1183) |
| QA §1.2, G1, G2, node 5, Lemma Q, node 8, Lemma R, §4.1, node 10 | Class N; NNB; grading; reflections | Support on `main` (#1184, #1189) |
| PR-QA §§1–3 | R1 C-CP recovery | Support on `main` (#1189) |
| FB §§2–5 | Combined obstruction; Observation E | Support on `main` (#1189) |
| Record-control DESIGN §§1–2, 5; setting-source feasibility (Result; setting-preparation section) | M1 relation | Support on `main` at their reviewed scopes |
| Main L44, L56, L82, L296, L304, L306, L366 | Native model; measure; traced channel; memory-sign marker; C-NS | Manuscript text |
| Substratum L48, A1 L92, A4 L98, A5 L100, A6 L102 | Native rule and its status | Manuscript text |
| SM L88–L96, L104–L110, L224, L226, L296 | Alphabet; gauge; state-dependent graph; form lemma | Manuscript text |
| GR L260, L266, L270 | Monomial-sourcing negatives | Manuscript text |
| Kernel: `permClass`, `permTheory_not_control`, `permTheory_not_qm`, `onesFixing_not_phasesAvailable`, `permClass_onesFixing`, `substratumGen_not_control`, `exists_nonMonomial_of_layerFlowExecutable`, `obs_not_layerFlowExecutable`, `stochasticChannel_kraus_monomial`, `coherentLiftClass_eq_substratumClass`; `ReadWriteControl.lean` header | §1.1 (read, not rebuilt). `readWriteSourced_*` is not cited (#1188) | Kernel statements on `main` |
| oi-qm-ext-1 README, B1, observer-interface source, two-system interface §4; F2-1 A★ | Lead dispositions; C-LEAK | Support on `main` |
| #1169 comments 6714000230, 6713955150, 6713653816; owner addendum, [#1169 c.6714136234](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6714136234); PR #1184 and #1189 review records; the independent review of this file | Scope, authorization, review history | Provenance |

### 8.2 Imported literature

| Work | Used for | Read in this unit |
| --- | --- | --- |
| D. Gross, arXiv:quant-ph/0602001 | (W1)–(W8): Theorems 2, 3, 6, 7, 19; Lemmas 4, 8, 9, 29 | §§I–II in full; statements of Theorems 2 and 19 and Lemmas 9 and 29 |
| R. W. Spekkens, arXiv:1409.5041 | Odd-prime equivalence and noncontextuality; `d = 2` inequivalence | Introduction and §V.A–B |
| H. Zhu, arXiv:1504.03773 | No Clifford-covariant Wigner function in even prime-power dimension | Abstract |
| P. Lillystone, J. J. Wallman, J. Emerson, arXiv:1802.06121v2 | Theorem 1 | Not re-read; as read in AP1 §5.2 |
| M. Howard et al., arXiv:1401.4174 | Context only | Abstract |
| S. D. Bartlett, T. Rudolph, R. W. Spekkens, arXiv:1111.5057 | §6.5 remark | Abstract via AP1 |

Lemmas A, S, G, N and M, Proposition T′ (given W5 and W7), Theorem T (given AS)
and Observation E are self-contained algebra.

## 9. Verification scope

Every verdict rests on the paper arguments of §3. The author self-checks are
uncommitted controls and carry no verdict. "Exact" means modular or `Fraction`
arithmetic; the others are floating-point eigenvalues at tolerance `1e−8`.

| Check | What it controls |
| --- | --- |
| c1 | Gross frame at `q = 3, 5`; `J` and `P` give rank-1 Choi matrices; the anti-symplectic map gives `−1` |
| c2 | `q = 3`, two cells: the coupled tick and the read branches are CP |
| c3 | `q = 2` R1: the non-rotating swap gives `−1`; a 3-cycle and a translation are CP |
| c4 | Lemma N words at `q = 2, 3, 5, 7` (exact) |
| c5 | `D_i` not Clifford at `q = 3`; CC-IMIT laws (exact) |
| c6 | Lemma S on random graded protocols at `q = 3, 5` (exact); the NNB breaking control |
| c7, c7′ | P1 removed and P2 removed: `−1` |
| c8, c9 | `q = 3` instances of Theorem T and Proposition T′(i): controlled shears; an X-type controller gives a non-PSD output. Consistent with the exact argument; not its support |
| c10 | CTRL-MON composite `T_g ∘ Δ_Z` is CP at `q = 3` |

The independent review's own cross-checks (an exhaustive Proposition AS check at
`q = 3`; the colour-blind odd-tick step; the memory-sign check) are review
provenance, not evidence here.

No Lean build, simulation campaign, enumeration, manuscript edit, freeze,
dispatch or merge was performed. Independent review of this revision is a
separate step.
