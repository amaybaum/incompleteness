# MECH-2: the state-dependent coupling graph `G(x)` at `q = 2`, encoded operations and their classical model

**Standing.** Paper-only research unit under #1169. Writer: Claude Code session,
2026-11-08. Scope:

- [owner authorization](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6717234497)
  (amaybaum, 2026-11-08T04:28:40Z), quoted in part in §2.1;
- [earlier owner addendum](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6714136234):
  composition, changed measurement choices, and the three shortcut checks of §4.

This file proposes no premise for adoption and promotes no claim. No simulation,
search or enumeration campaign, Lean build, V3 execution, manuscript change,
freeze, dispatch or merge is part of it. Small exact checks of this file's own
algebra were run as author self-checks (§9). They are controls on that algebra,
not evidence, and no verdict rests on them.

**Source snapshot.** Every repository link is pinned to `main` at
`120b3ca40d94fdab8db1ad271db299ff44360f2c` (cited as `main@120b3ca4`).
Abbreviations:

- **M1D**: [MECH-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md);
- **AP1**: [apparatus-1 DESIGN](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md);
- **QA**: [Q-A DESIGN](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md);
- **FB**: [feedback RESULT](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/quarter-phase-feedback-20261107/RESULT.md);
- **PI**: [one common physical experimental interface](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/physical-interface.md),
  the earlier screen of SM's ring rule at `q = 2`.

Labels carried from those records keep their meaning there: R1 (AP1's
tetrahedral one-cell frame), P1 (terminal registration), P2 (half-known ready
cells), P3 (per-tick, per-edge arming), H-PREP (record-conditioned classes read
as preparations), N (the native linear class), NNB, U′, Lemma Q, Lemma R, C-PH,
C-ROT, C-IS, C-CP, C-NS, C-LEAK, C-COMP, CC-IMIT, CC-IMIT′, CC-RECON, M1,
CTRL-MON, MP-1, P-8.

## 0. Result

1. **The construction (§1).** `G_SM` is SM's explicit ring rule
   ([SM:112](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L112))
   at `q = 2`. It reduces exactly to
   `f_i(u) = u_{i−1} ⊕ (u_{i+1} ∨ u_{i+2})`, `F(u, v) = (f(u) ⊕ v, u)`
   (PI eq. (1)). It is a fixed bijection (A2), has range 2 (A3) and is
   center-free and translation invariant (A4). It is not affine (A5 fails),
   and for `L ≥ 5` its edges are not reciprocal. Its status is an
   independently motivated proposal: SM's state-dependent-geometry principle
   is a stated hypothesis, and the ring is SM's example of it. It is not a
   physically sourced mechanism. Switching the state dependence off
   (`R(i) ≡ i + 1`) gives the linear, symmetric, center-free ring of class N.
2. **Ceilings for every fixed bijection at `q = 2` (§3, nodes 2–4).** They hold
   under Lemma F's operation set (attach cells in fixed laws, apply the rule,
   feedback, discard, condition on configuration records) and H-LIFT (every
   cell correlated with the carrier at an operation's input is part of the
   encoded carrier). Within that scope they cover `G_SM` and every other `G(x)`.
   - **Lemma F.** Under a fixed linear identification by an orthogonal frame,
     every encoded branch is a nonnegative matrix on frame coordinates.
   - **Theorem U2.** Under the product frame R1^⊗n, the ontic permutations whose
     encoded action is completely positive (CP) are exactly `A_4 ≀ S_n`: local
     tetrahedral rotations, which are Clifford, and permutations of cells.
     Every encoded unitary channel, deterministic or heralded, that a fixed
     bijection induces lies in this group. So there is no encoded `S`, `T`,
     CNOT, CZ, `rot`, or any entangling unitary. The proof uses a Hamming-graph
     rigidity argument written out in full (Lemma H). These CP verdicts are
     relative to R1, whose covariance group is `A_4 ≀ S_n` and not the Clifford
     group. Joint-CP failure therefore also covers class N and does not single
     out `G_SM`.
   - **Theorem NC.** Under an injective identification, with operational
     equivalences certified by spanning reads, the configuration-level model
     is a preparation-, transformation- and measurement-noncontextual model of
     the whole encoded operational theory, whatever the dynamics. With product
     encoded effects it gives CHSH ≤ 2. At `q = 2`, spanning certification
     needs a `Y` read, which is not exhibited natively. Over the native `Z`/`X`
     reads alone, Theorem NC does not apply.
3. **What `G_SM` adds at `q = 2` (§3, nodes 5–6).**
   - Lemma Q's argument does not apply to `G_SM`. The identity
     `Q(F(u, v)) = Q(u, v) + Σ_i u_i f_i(u)` holds for every second-order rule
     over `F_2`. For `G_SM` the sum is not identically 0, so Lemma Q's
     conclusion (i), conservation of `Q = Σ u_i v_i`, fails, and transport is
     nonlinear. A symmetric, center-free switched graph conserves `Q`
     (Lemma Qσ). Whether the protection of Lemma Q(iii) fails under P1 and P2
     is open.
   - Nonlinear conditioning reaches laws that are not uniform on affine sets.
     The instance P★ (§3, node 6) heralds, with probability 5/8, the encoded
     state `r = (3/5, 1/5, 3/5)`. It is valid and lies outside the stabilizer
     octahedron (`|r|₁ = 7/5`). Its `(⟨Z⟩, ⟨X⟩)` lies inside the stabilizer
     diamond, so only a `Y` read distinguishes it.
   - The complementary branch of the same instrument is not a quantum state
     (`|r|² = 11/9`), and the heralding branch is not positive on other inputs.
     The complete instrument therefore fails C-CP.
   - P★'s background without any record, at `t = 3`, already gives a carrier
     channel that is not CP. Its Choi eigenvalues are
     `{3/4, 3/4, (1 ± √2)/4}`. Its Bloch linear part has determinant `−1/16`:
     a positive, orientation-reversing map of Lemma R's reflection type. The
     C-CP failure does not need record conditioning.
   - Mechanism off, the same protocol gives valid stabilizer outputs.
4. **The six acceptance criteria at `q = 2` (§6.1).**
   - Native mechanism: defined. Its status is a proposal.
   - Non-stabilizer capability: no reversible escape for any fixed bijection
     (Theorem U2, under H-LIFT). A non-stabilizer state appears only in a
     C-CP-failing instrument.
   - Quantum selection: fails. P★'s channels are not CP, one of them
     reflection-type without any record. Joint-CP failure under R1 holds for
     every coupling rule and does not single out `G_SM`.
   - In-world control: the selection is ontically in-world. It fails C-CP in
     P★, whose switch cells are in `X_+` laws.
   - Operational completeness: not met.
   - Classical countercontrol: under R1^⊗n with H-LIFT and spanning-read
     certification, an exact noncontextual imitation exists (Theorem NC). At
     the native read level (`Z` and `X` only) A6 is undecided.
5. **Outcome type (ii): stop (§6.2).**
   - Under injective encodings with H-LIFT and spanning-read certification, no
     dynamics escapes Theorem NC. Within that scope a nonclassical
     observer-level theory needs a change in the identification and access,
     not in the dynamics alone. Whether `G_SM` supplies the native `Y` read
     that this certification needs at `q = 2` is open.
   - The missing premise is **M-INACC**: per encoded system, an ontic
     functional that the fixed rule uses, that no permitted preparation, read,
     reuse or recombination can access, and whose inaccessibility has a reason
     not chosen to reach the quantum target.
   - `G_SM` does not supply M-INACC, and Lemma Q's argument does not apply to
     it.
   - The first decisive check of a symmetrized `G(x)`: whether Lemma Q(iii)'s
     protection survives nonlinear transport under P1 and P2.
   - For Bell composites, given determinism and measurement independence,
     Proposition B derives a necessary condition implied by H-Bell (i)–(ii)
     together with a violation (M-FIX): the available preparations' laws on
     the response-relevant variable do not span. Some nonconstant
     response-relevant function `g` then has the same mean under every
     available preparation (equivalently, some nonzero `g` has mean 0 under
     all of them). A variable with a fully preparation-independent law
     is sufficient but not necessary; an exact counter-model is in node 4.
   - No V3 round is proposed.

## 1. The construction

### 1.1 What the corpus fixes and what it leaves open

| Item | Source | Status in the corpus |
| --- | --- | --- |
| Principle `s(t+1) = φ_{s(t)}(s(t))`, with the graph varying with the state | [SM:104](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L104) | Stated as a principle of background independence in the geometric sense. It is distinct from A6 ([Substratum A6](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Substratum.md#L102)) |
| Bijectivity of every second-order rule `x(t+1) = f(x(t)) − x(t−1)` | [SM:106](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L106) | Proved: inverse `(a, b) ↦ (b, f(b) − a)` |
| Constraints (i) local, (ii) center-free, (iii) statistically isotropic graph dependence | [SM:108](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L108) | Conditions under which the reference chain survives |
| Prepared states may carry bounded-degree, preparation-indexed edges | [SM:110](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L110); [SM:152–156](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L152) | Permitted. No edge law is given |
| Explicit ring: `R(i, x) = i + 2` if `x_{i+1} = 0`, else `i + 1`; `L(i) = i − 1` | [SM:112](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L112) | One example satisfying (i)–(iii) |
| H-Bell: preparation-indexed graphs must supply ontic parameter dependence, keep operational no-signalling and meet a curvature-stability condition | [Substratum:131–133](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Substratum.md#L131); [Main:414–416](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Main.md#L414) | Open hypothesis |
| The deep sector reaches the visible sector only through the boundary | [GR §3.2](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/GR.md#L112) | Uses spatial locality. A range-2 ring keeps it; long preparation-indexed edges would need it re-checked |

**Left open by the corpus.**

- The functional form of `G(x)` beyond the ring example.
- Whether edges are reciprocal.
- Any law for preparation-indexed edges.
- Any preparation or apparatus that produces them.

H-Bell stays an open hypothesis throughout this file.

### 1.2 `G_SM` at `q = 2`

Take a ring of `L` sites with alphabet `F_2`. At `q = 2`,
`x_{R(i,x)} = x_{i+1} ∨ x_{i+2}`: if `x_{i+1} = 1` the selected value is that 1,
and otherwise it is `x_{i+2}`. Write `u = x(t)` and `v = x(t − 1)`. Then

```text
f_i(u) = u_{i−1} ⊕ u_{i+1} ⊕ u_{i+2} ⊕ u_{i+1} u_{i+2},
F(u, v) = (f(u) ⊕ v, u),     F^{−1}(a, b) = (b, a ⊕ f(b)).          (1)
```

This is PI's eq. (1). Self-check c3 confirms it exhaustively against SM's
`R`-rule for `L = 4, …, 7`. At `q = 2` the `+v` and `−v` memory terms coincide,
so nothing in (1) depends on #1193.

**Encoded frame.** AP1 §4.2 frame: at tick `t` a cell's encoded pair is
`(z, x) = (u, v)` for `t` even and `(v, u)` for `t` odd. R1 maps a point `(z, x)`
to the Bloch-type vector `((−1)^z, (−1)^x, (−1)^{z+x})` for `(⟨Z⟩, ⟨X⟩, ⟨Y⟩)`.
Its frame operators are

`A(z, x) = ½(I + (−1)^z Z + (−1)^x X + (−1)^{z+x} Y)`.

They have unit trace and satisfy `tr A(λ)A(μ) = 2δ_{λμ}`. On `n` cells
`A(λ) = ⊗_k A(λ_k)`, with `tr A(λ)A(μ) = 2^n δ_{λμ}`. A law `μ` maps to
`ρ_μ = Σ_λ μ(λ) A(λ)`. This map is a linear bijection between signed laws and
Hermitian operators, with total mass going to trace.

### 1.3 Axioms kept and broken

| Property | `G_SM` | Reason |
| --- | --- | --- |
| A2 bijection | Kept | (1) has an explicit inverse (c3) |
| A3 bounded degree | Kept | `f_i` reads `i − 1, i + 1, i + 2`; dependency radius `2t` after `t` ticks (PI §6). SM:112's "range 1" refers to the graph dependence (`R(i, x)` reads `x_{i+1}`); the reach of `f_i` is 2 |
| A4, center-free sense | Kept | `f_i` does not read `u_i` |
| A4, translation sense | Kept | The rule is the same at every site |
| A5 linearity | Broken | The term `u_{i+1}u_{i+2}`. The second difference of `F` along `u_1, u_2` is nonzero (c3). Each fixed graph is linear, but the map is not |
| Reciprocal (symmetric) coupling | Broken for `L ≥ 5` | `i` can read `i + 2`, while `i + 2` reads `i + 1` and `i + 3` or `i + 4`. At `L = 4`, `i + 4 = i` (M1D [node 8](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L877)) |
| Nearest-neighbour premise ([SM:226](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L226)) | Broken | Range 2 |
| Lemma Q's argument | Does not apply | Its conclusion (i), conservation of `Q`, fails (Lemma Qσ, node 5) |

**Mechanism off.** Set `R(i) ≡ i + 1`. Then `f_i = u_{i−1} ⊕ u_{i+1}`: the
symmetric, center-free linear ring of class N (bipartite iff `L` is even). It
conserves `Q` (c3).

### 1.4 Classification of ingredients

| Ingredient | Classification | Where OI motivates it |
| --- | --- | --- |
| Second-order bijective form, memory term | Native (A2; SM form lemma) | [SM:106](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L106), [SM:224](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L224) |
| State dependence of the graph | Independently motivated proposal | SM:104 (background independence as state-dependent geometry); Substratum:131 and Main:414 use it as the route for M1-B |
| The particular ring `R(i, x)` | Example of the proposal | SM:112. It is not derived or selected by OI |
| Alphabet `q = 2` | Native parameter value, chosen for this unit | Owner authorization item 2; [SM §2.7](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/SM.md#L88) |
| Ready cells, hidden uniform cells, carrier inputs, choice of record and time | Supplied (P2, H-PREP; counting measure N2) | AP1 ledger |
| R1 | Mathematical representation | AP1 §4.2 |
| Preparation-indexed long edges | Not constructed. H-Bell is an open hypothesis | Substratum:133 |

## 2. Question, decision rule and controls

The decision rule, controls and countercontrols below are stated in the same
commit as the derivation of §3. Their priority over the result is not
separately recorded. The verdicts are paper proofs plus one exhibited instance
(P★) whose numbers are stated exactly, so no verdict depends on that order.

### 2.1 Question

The owner's main objective
([authorization](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6717234497)):

> My main objective for MECH-2 is to determine whether state-dependent dynamics
> supply genuinely new quantum-operational capabilities, rather than simply
> another representation of classical behavior.

At `q = 2`, does `G_SM` produce, on a physically specified encoding, an
operation outside the applicable stabilizer fragment? If so, is it CP, is it
selected in-world, is it operationally complete, and does it escape every
classical (noncontextual) model?

**Comparator (imported, I1).** The `n`-qubit stabilizer subtheory: stabilizer
states and their mixtures, Pauli reads with Lüders continuation, and the
Clifford group.

**Encoding.** The physically specified encoding is R1 per cell. This is AP1's
identification, fixed for all settings as PC-F1 requires. In it the native
slot reads are encoded `Z` and `X` Lüders reads. Node 7 treats non-injective
encodings (QA's U′, FB's linear encodings, P-8).

### 2.2 Acceptance criteria and pass conditions

| # | Criterion (owner) | Pass condition in this file |
| --- | --- | --- |
| A1 | Native mechanism | One explicitly defined fixed rule. The verdict states whether it is native, an independently motivated proposal, or a posit |
| A2 | Non-stabilizer capability | An available encoded operation outside the stabilizer fragment: a non-Clifford unitary, a non-stabilizer state, effect or channel. It must belong to a complete instrument that passes C-CP. Otherwise the verdict says what was exhibited and what fails |
| A3 | Quantum selection | Every available encoded branch, and every coarse-graining of branches, is CP. The exclusion of non-CP operations follows from a structure stated without reference to the comparator. CC-RECON labels any target-motivated restriction |
| A4 | In-world control | The setting (which coupling acts) is selected by the state under the fixed rule, with C-CP intact on the inputs that selection reaches |
| A5 | Operational completeness | Preparations, success and failure branches, records, retained hidden information, an outgoing state usable by the next operation, composition, and changed measurement choices on one preparation (C-COMP K1–K6, M1D [§2.4](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L342)) |
| A6 | Classical countercontrol | Report whether a noncontextual model reproduces the observer-level statistics: CC-IMIT′, or a certified witness with tomographically complete equivalences |

### 2.3 Controls and countercontrols

| ID | Requirement | Required outcome |
| --- | --- | --- |
| C-PH | Encoded quarter phase | Reported; escape iff available |
| C-ROT | Encoded `rot` (infinite-order unitary) | Reported |
| C-CP | Per encoding, every available branch CP | Required for A2–A5 |
| C-IS | Per-state diagnostic (`|r|₁ ≤ 1`) | Diagnostic only |
| C-NS | No-signalling of complete local histories | Required |
| C-LEAK | Retained hidden correlations, reuse, recombination | Reported against the comparator |
| C-Q | QA Lemma Q | Whether it survives under `G_SM` |
| C-COMP | Composition battery K1–K6 | Required for A2, applied to any candidate operation |
| CC-OFF | Mechanism off (`R ≡ i + 1`) | Must fall back to class N behaviour |
| CC-IMIT, CC-IMIT′ | Measure-and-prepare; the mechanism's own classical model | Reported |
| CC-RECON | Reconstruction flag | Target-motivated premises are labelled, not counted |
| C-EX | §A.21 exactness | Structural identities checked with controls that must break them |

### 2.4 Shortcut checks (owner addendum)

- **SC-1.** Is a unitary, an interference mechanism or a CP restriction imported?
- **SC-2.** Does an outside agent select couplings or prepare special inputs?
- **SC-3.** Does the operation exist in the physical dynamics or only in the
  representation?

### 2.5 Decision rule

- **D0.** A failed C-EX or CC-OFF voids the verdict of the branch it controls.
- **D1.** A2 counts only with C-CP passed on the complete instrument and
  C-COMP passed.
- **D2.** If a noncontextual model reproduces every observer-level statistic
  under tomographically complete equivalences, the A2 verdict is stated as
  "not separated from classical behaviour".
- **D3.** Outcome types:
  - (i) A1–A5 pass with C-CP, C-NS and C-LEAK green, and the countercontrol
    reported;
  - (ii) a criterion needs a new premise or fails. The premise is named;
  - (iii) the decisive remaining question is a finite search.

## 3. Derivation

### Node 1. The physical carrier

AP1 [Lemma 2](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L153)
applies unchanged. `G_SM` is a bijection, so every branch of every instrument
is a sum of conjugations by scaled partial permutations of the configuration
basis. Every branch is therefore in
[`permClass`](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L236),
and on finite cones
[`permTheory_not_control`](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L708)
and [`permTheory_not_qm`](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean#L717)
apply. State dependence does not change premises (P-a)–(P-c) of M1D §1.1. The
kernel's [`substratumClass`](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/lean-mathlib/OIBridge/StructuralClosure.lean#L180)
is monomial and covers a state-dependent bijection equally. Any escape has to be
sought on an encoded carrier.

### Node 2. Lemma F: frame stochasticity for every dynamics

**Hypotheses.**

- A fixed bijection `Φ` of a finite configuration set acts at every tick. It
  may be any rule, including any `G(x)`.
- The observer's operations are the following:
  - attaching cells in fixed nonnegative laws;
  - applying `Φ` any number of times;
  - choosing later operations from records (feedback);
  - discarding by marginalization;
  - conditioning on configuration records.
- **H-LIFT.** At the input of an operation, every cell whose law is correlated
  with the encoded carrier belongs to the encoded carrier. This is FB's
  common-lift condition H-C, stated for the identification.
- The identification is `μ ↦ Σ_λ μ(λ) A(λ)` with an orthogonal frame
  `{A(λ)}` of unit-trace operators (R1^⊗n at `q = 2`; Gross's R-W at odd `q`).

**Lemma F.**

- (a) Every encoded state of a reachable law has nonnegative frame coordinates.
- (b) Every encoded branch, including feedback, is represented by a
  nonnegative matrix `B` on frame coordinates. The branch is unique as a linear
  map on signed laws.
- (c) Every read effect has a symbol in `[0, 1]` on frame points.

*Proof.* Frame coordinates are the law itself. Each operation is a nonnegative
matrix on laws:

- a permutation matrix for `Φ`;
- a tensor product with a fixed law;
- a marginal sum;
- a `0/1` diagonal for conditioning.

Feedback composes these conditionally on records, and products and sums of
nonnegative matrices are nonnegative. Under H-LIFT the carrier-level branch is
a fixed matrix. Uniqueness holds because the identification is a bijection on
signed laws. ∎

Without H-LIFT the carrier law alone does not fix later statistics, and the
encoded description must be enlarged until H-LIFT holds (node 7).

### Node 3. Theorem U2: the CP permutations and encoded unitaries of R1^⊗n

For a permutation `π` of `Γ_n = (F_2²)^n`, write `T_π(A(λ)) = A(πλ)`. Let
`d(λ, μ)` be the number of cells in which `λ` and `μ` differ.

**Single-cell triple traces** (c1, exact). Write
`t(a, b, c) = tr A(a)A(b)A(c)`. With `A(a) = ½(I + n_a·σ)` and the four `n_a`
the vertices of a regular tetrahedron (`n_a·n_b = −1` for `a ≠ b`):

- `t(a, a, a) = 5/2`;
- `t(a, a, b) = t(a, b, a) = t(b, a, a) = 1/2` for `a ≠ b`;
- `t(a, b, c) = −1/2 ± i` for distinct `a, b, c`. The sign is the orientation
  `sgn det(n_a, n_b, n_c)`, which a transposition of two arguments reverses.

On `n` cells, `T(λ, μ, ν) = tr A(λ)A(μ)A(ν) = Π_k t(λ_k, μ_k, ν_k)`. In
particular `T(λ, λ, μ) = (5/2)^{n−d}(1/2)^d` with `d = d(λ, μ)`.

**Lemma H (rigidity of the cell-Hamming graph).** A permutation `π` of `Γ_n`
that preserves `d` has the form
`π(v)_{τ(i)} = σ_i(v_i)`, with `τ ∈ S_n` and each `σ_i` a bijection of `F_2²`.

*Proof.* Let `𝓗` be the graph with edges `d = 1`. A **line** is a set of the
four points that agree outside one cell `i` (its direction).

1. **Lines are the maximal cliques.** If `a ~ b` differ in cell `i` and
   `a ~ c` in cell `j ≠ i`, then `b, c` differ in cells `i` and `j`. So a clique
   of three or more points lies in one line. Lines are cliques of four points,
   and every edge lies in exactly one line. Hence `π` maps lines to lines.
2. **Directions are preserved.** Call disjoint lines `L, L′` *matched* if every
   vertex of each has exactly one neighbour in the other.
   - Lines of the same direction `i` whose points differ in exactly one other
     cell are matched: `v` with cell `i` set to `s` is adjacent only to the point
     of `L′` with cell `i` set to `s`.
   - Lines of different directions are never matched. Let `L` have direction
     `i` and `L′` direction `k ≠ i`, and let `c` be the number of cells outside
     `{i, k}` in which their points differ. The three points of `L` whose cell
     `i` differs from `L′`'s fixed value differ from every point of `L′` in cell
     `i`. If `c ≥ 1` they have no neighbour in `L′`. If `c = 0` all three are
     adjacent to the same single point of `L′`, which then has three
     neighbours in `L`.
   - Lines of the same direction whose points differ in two or more other
     cells have no edges between them.

   "Same direction" is the transitive closure of "matched". Since `π`
   preserves matching, it permutes direction classes, by some `τ ∈ S_n`.
3. **Coordinates are separated.** If `v, v′` agree in cell `i`, join them by a
   path that changes one cell `j ≠ i` at a time. Each step runs along a line of
   direction `j`, whose image has direction `τ(j) ≠ τ(i)`. So cell `τ(i)` of
   `π(v)` is constant along the path, and `π(v)_{τ(i)} = σ_i(v_i)`. `π` maps a
   line of direction `i` bijectively onto a line of direction `τ(i)`, so `σ_i`
   is bijective. ∎

(Lemma H uses four values per cell. With two values per cell the "matched"
test does not separate directions.)

**Theorem U2.** Let `π` be a permutation of `Γ_n`.

- (i) `T_π` is CP iff `π ∈ A_4 ≀ S_n`, that is, `π` is a permutation of cells
  composed with even permutations `σ_i ∈ A_4` of each cell's four points.
- (ii) Let `Φ` be any fixed bijection and any protocol of node 2 (H-LIFT) on
  `n` encoded cells. If one of its branches acts on the encoded carrier as
  `p · Ad U` with `p > 0` independent of the input, then `Ad U = T_π` for some
  `π ∈ A_4 ≀ S_n`.

*Proof of (i), (⇐).* `A_4` is the rotation group of the tetrahedron:

- its three involutions act as the Pauli conjugations (translations of
  `F_2²`);
- its 3-cycles act as order-3 Clifford rotations about the tetrahedron's
  vertex axes.

c1 checks all 24 single-cell permutations exactly: the 12 even ones have
rank-1 PSD Choi matrices and the 12 odd ones do not. A permutation of cells is
conjugation by SWAPs. All of these are Clifford unitaries.

*Proof of (i), (⇒).*

1. `T_π` permutes an orthogonal basis of equal norms, so it is
   trace-preserving, unital and a Hilbert–Schmidt isometry. If it is CP, it
   maps pure states to pure states.
2. M1D's [Proposition AS](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L516)
   (⇒, "one Kraus operator") then gives `T_π = Ad U` with `U` unitary. That
   step is dimension-free and uses no property of odd `q`.
3. `Ad U` is a `*`-automorphism, so it preserves `T`:
   `T(πλ, πμ, πν) = T(λ, μ, ν)`.
4. From `T(λ, λ, μ)`, `π` preserves `d`. By Lemma H, `π = (σ_i, τ)`.
5. Take `λ, μ, ν` equal outside cell `i` and pairwise distinct in cell `i`.
   Preservation of `T` gives
   `t(σ_iλ_i, σ_iμ_i, σ_iν_i) = t(λ_i, μ_i, ν_i)`, so `σ_i` preserves every
   orientation. A transposition reverses the orientation of any triple
   containing the swapped pair, so `σ_i` is even. ∎

*Proof of (ii).*

1. By Lemma F the branch is a nonnegative matrix `B`. Since valid states span
   and the identification is injective, `M = B/p` equals the frame
   representation of `Ad U` on all signed laws.
2. `Ad U` is a Hilbert–Schmidt isometry and
   `‖Σ w_λ A(λ)‖²_HS = 2^n ‖w‖²`, so `M` is a real orthogonal matrix.
3. A real orthogonal matrix with nonnegative entries is a permutation matrix:
   - its columns are pairwise orthogonal with nonnegative entries, so they
     have disjoint supports;
   - `4^n` disjoint nonempty supports in `4^n` coordinates are singletons;
   - unit norm makes the entries 1.
4. So `Ad U = T_π`, and (i) gives `π ∈ A_4 ≀ S_n`. ∎

**Consequences (every fixed bijection, R1^⊗n, under Lemma F's operation set and H-LIFT).**

- **No encoded entangling unitary.** No encoded CNOT, CZ or other entangling
  unitary exists, heralded or not, for any fixed bijection: linear, `G_SM`,
  any `G(x)`, or Native A.
- **No other unitary escape.** There is no encoded `S`; for `n = 1` this is
  AP1 [Lemma 5](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L731).
  There is no encoded `T`, and no infinite-order unitary, which agrees with AP1
  [§5.3](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L955).
  C-PH and C-ROT hold for `G_SM`.
- **No coupling rule is jointly CP.** A fixed rule whose joint encoded action
  on R1 cells is CP is in `A_4 ≀ S_n`, so it couples no two cells. This is the
  `q = 2` analogue of M1D [Theorem T](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L799),
  and it is stronger: no in-world selection of any coupling is jointly CP.
  `G_SM`'s step, the native linear step and AP1's coupled read tick all fail
  joint CP. This failure is relative to R1, whose covariance group is
  `A_4 ≀ S_n` and not the Clifford group, so it does not single out `G_SM`.
  C-CP can only be tested in a discriminating way on reduced branches, with
  ancillas in supplied laws. There AP1's read passes, and P★ (node 6) fails,
  with and without its record.

*Controls.* c2 (`n = 2`, exact Gaussian-rational triple traces) finds 288
automorphisms of `T`, equal as a set to `A_4 ≀ S_2`, and 1152 = `|S_4 ≀ S_2|`
automorphisms of `d`. A numerical Choi control gives minimum eigenvalue about
`−7·10^{−16}` over the 288 and `−1` for the cross-cell transvection
`x_1 += z_2`, which must break. These are controls on Lemma H and Theorem U2,
not their support.

### Node 4. Theorem NC: the configuration model is noncontextual for every dynamics

**Theorem NC.** Assume Lemma F's hypotheses, with an injective identification
(R1^⊗n, or R-W at odd `q`). Take as operational equivalences those of the
encoded description: equal operators for preparations and effects, equal
linear maps for transformations. These coincide with statistical equivalence
once the reachable preparations span the operator space and the reachable
reads span its dual. Then:

- each preparation is assigned its law;
- each transformation branch its matrix `B`;
- each read outcome its response function.

These assignments are a preparation-, transformation- and
measurement-noncontextual ontological model of the encoded operational theory,
whatever the bijection `Φ`.

*Proof.*

- **Preparations.** The law is `R^{−1}(ρ)`, a function of the operator alone.
- **Transformations.** `B` is the unique matrix with `R ∘ B = Φ_enc ∘ R` (Lemma
  F(b)).
- **Effects.** If `Σ_λ W(λ)ξ(λ) = tr(ρE)` for all `ρ`, then `ξ` is determined by
  `E`, because frame coordinates of states span.
- **Validity.** Nonnegativity and normalization hold by Lemma F. ∎

**Corollary NC-B (product encoded effects).**

- *Setup.* Two wings carry product-frame identifications. The joint effects
  are products `E_a ⊗ E_b`.
- *Response.* Then `ξ_{ab}(λ) = ξ_a(λ_A) ξ_b(λ_B)`.
- *Correlations.* For every reachable law `W`,
  `P(a, b) = Σ W(λ) ξ_a ξ_b`. This is a local model, so CHSH ≤ 2.

**Scope.**

- Theorem NC holds for every `G(x)` under an injective encoding with H-LIFT.
  Where the equivalences are certified by spanning reads, it decides A6.
- With fewer reads, statistical equivalence is coarser than operator
  equality. A classical model then can appear contextual:
  - a law on two bits read only one bit at a time generates the square state
    space, a gbit;
  - AP1's [Lemma 4′ scope](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L698)
    records the same effect for `Z`/`X` reads.

  Such apparent contextuality is not a nonclassicality witness unless the
  missing reads are absent for a physical reason. That is M-INACC (§6.2).
- At `q = 2`, an encoded `Y` read is not exhibited. AP1 §4.2 excludes one by a
  type grading proved for its linear apparatus class. That exclusion does not
  carry over to `G_SM`, whose nonlinearity breaks the grading: P★'s record-1
  branch (node 6) reaches a carrier law with `z + x` determined (support
  `{01, 10}`), which the grading forbids. Whether `G_SM` supplies a native `Y`
  read is open. Until a `Y` read is available (from `G_SM`, NNB or another
  source), the spanning certification fails at the native read level, and
  Theorem NC leaves A6 undecided there.
- **Context.** Theorem NC is a direct instance of the "nonnegative frame
  representation ⇒ noncontextual model" direction of Spekkens' equivalence of
  negativity and contextuality (PRL 101, 020401 (2008)). That work was not read
  in this unit, and the proof above is self-contained.

**Proposition B (spanning no-signalling; H-Bell bearing).**

- *Setup.* Outcomes are deterministic functions `a = A(x, y, ω)` and
  `b = B(x, y, ω)` of a response-relevant variable `ω`. Settings are
  independent of `ω`. A family `𝒫` of available preparations gives laws
  `p_P(ω)`.
- *Claim.* If the laws `{p_P}` span the functions of `ω`, and every `P ∈ 𝒫`
  is operationally no-signalling, then `A` does not depend on `y`, nor `B` on
  `x`, at any `ω`. CHSH ≤ 2 then holds for every `P`, even when the rule has
  ontic parameter dependence, such as long edges.
- *Proof.* `Σ_ω p_P(ω)[A(x, y, ω) = a]` is the same for `y` and `y′` for
  every `P`. By spanning, `[A(x, y, ω) = a] = [A(x, y′, ω) = a]` at every
  `ω`. Main's [screened-ceiling argument](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/papers/Main.md#L366)
  then applies pointwise. ∎
- *Example.* A shared hidden bit `h` with `a = h ⊕ xy` and `b = h` is
  no-signalling for every preparation that leaves `h` uniform, and it gives
  CHSH = 4. It violates the spanning hypothesis only because no preparation
  changes the law of `h`.
- *Reading (**M-FIX**).* Given determinism and measurement independence,
  H-Bell (i)–(ii) together with a violation imply that the available laws
  `{p_P}` do not span. Equivalently, some nonzero response-relevant function
  `g` has `Σ_ω p_P(ω) g(ω) = 0` for every available preparation; equivalently
  again, some nonconstant `g` has the same mean under every available
  preparation. This is a necessary condition derived from H-Bell,
  not an added requirement.
- *A sufficient form, not a necessary one.* A response-relevant variable
  whose whole law no available preparation can change (the bit `h` of the
  example) gives non-spanning. It is not forced, as the following exact model
  shows:
  - `ω = (h, k)`, `a = h ⊕ k·xy` and `b = h`;
  - the preparations set `P(k = 1) = s` and `P(h = 0 | k = 0) = c` freely, and
    keep `h` uniform given `k = 1`.

  This model has four properties:
  - every such preparation is no-signalling: `a` is uniform given `k = 1` and
    equals `h` given `k = 0`, and `b = h`;
  - CHSH = `2 + 2s`, which reaches 4 at `s = 1`;
  - no nonconstant function of `ω` has a law independent of `(s, c)`;
  - the laws do not span. The function `1_{(1,1)} − 1_{(0,1)}` (over
    `(h, k)`) has mean 0 under every preparation: what is fixed is the
    conditional law of `h` given `k = 1`.
- *Native candidate.* In OI the natural candidate for such a fixed conditional
  law is the hidden sector's counting measure (N2, H-PREP). Whether
  preparation-indexed edges couple only to response-relevant functions of that
  kind is part of H-Bell (ii) and is not decided here.
- *Status.* This elaborates H-Bell's stated requirement. It is not a no-go.
- *Context.* Proposition B is a linear-algebra form of the Wood–Spekkens point
  that causal explanations of Bell violations need fine-tuning to reproduce
  no-signalling (NJP 17, 033002 (2015)). That work was not read in this unit.

### Node 5. Lemma Qσ: QA's Lemma Q argument does not apply to `G_SM`

**Lemma Qσ.** For every second-order rule `F(u, v) = (f(u) ⊕ v, u)` over
`F_2`, `Q(F(u, v)) = Q(u, v) ⊕ Σ_i u_i f_i(u)`, where `Q(u, v) = Σ_i u_i v_i`.
Hence:

- (a) If `f_i(u) = Σ_{j ∈ N_i(u)} u_j` for a state-dependent graph that is
  symmetric and loop-free at every `u`, then `Q` is conserved.
- (b) For `G_SM`, `Q` is not conserved.

*Proof.*

- `Q(f(u) ⊕ v, u) = Σ_i (f_i(u) ⊕ v_i) u_i`.
- For (a), each undirected edge `{i, j}` present at `u` contributes
  `2u_iu_j ≡ 0`.
- For (b), `Σ_i u_i f_i(u) = Σ_i u_iu_{i+2} ⊕ Σ_i u_iu_{i+1}u_{i+2}`, because
  the two nearest-neighbour terms cancel. At `u = (1, 0, 1, 0, 0)` on `L = 5`
  this is 1. ∎

c3 finds `Q` changed on 320 of 1024 configurations at `L = 5`, and conserved by
the mechanism-off ring (CC-OFF). c6 confirms the identity for `L = 5, 6, 7`. It
also finds `Q` conserved by a symmetric switched graph (edge `{i, i + 2}`
present iff `u_{i+1} = 0`, read by both ends; center-free). That graph is a
control variant here, not a proposal.

**C-Q verdict.** QA's Lemma Q assumes symmetric couplings with `k_ii = 0` and
a linear step. `G_SM` meets neither, and Lemma Q's argument does not apply:

- its conclusion (i), conservation of `Q`, fails (Lemma Qσ(b));
- its proof of (iii) transports determined functionals linearly, and `G_SM`'s
  transport is nonlinear.

P★'s record-1 branch (node 6) determines the carrier's `Q* = 1` functional
`z + x`. Its record is a ring site that keeps evolving, so P1 is not
implemented there. Whether the protection of Lemma Q(iii) fails under P1 and
P2 is open, for `G_SM` and for a symmetric `G(x)` (§6.2).

### Node 6. What `G_SM` does on one R1 carrier: the instance P★

**P★ (exact; c4, at `L = 9, 12, 13` with identical output).**

- Carrier: site 0, in the encoded `Z_+` law (`u_0(0) = 0`, `u_{−1}(0)` uniform).
- Sites 1 and 2: current slots uniform and hidden, previous slots 0. In the
  `t = 0` frame each is in the `X_+` law.
- Every other site: ready `(0, 0)`.
- Run `G_SM` for three ticks.
- Condition on the record `u_3(−1)`.
- Carrier frame at `t = 3`: `(z, x) = (u_2(0), u_3(0))`.

| Record | Probability | Carrier law on `(00, 01, 10, 11)` | `r = (⟨Z⟩, ⟨X⟩, ⟨Y⟩)` | `|r|₁` | `|r|²` | Encoded state |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 5/8 | (3/5, 1/5, 0, 1/5) | (3/5, 1/5, 3/5) | 7/5 | 19/25 | Valid; outside the stabilizer octahedron |
| 1 | 3/8 | (0, 2/3, 1/3, 0) | (1/3, −1/3, −1) | 5/3 | 11/9 | Not PSD |

Further results:

- **Not positive on other inputs.** Applied to the input `Z_−`, the same
  record-0 branch gives `r = (1, −1, −1)`, which is not PSD. So the branch is
  not even a positive map on the carrier.
- **Mechanism off (c5).** With `R ≡ i + 1` and everything else unchanged, both
  records give valid stabilizer states `Z_±`. With the switch cells' current
  slots known (0), `G_SM` gives `Z_+`. CC-OFF is green.
- **Unconditioned channels.** The carrier channels with uniform hidden
  backgrounds and no record (c4: backgrounds B1–B3, `t = 1, 2`) send every
  Pauli eigenstate into the octahedron. Their Choi spectra are nonnegative.
- **P★'s own background, with no record (c7, exact).** At `t = 3`, P★'s
  background without any conditioning gives a carrier channel that is not CP:
  - it sends `Z_± ↦ (±1/2, 0, 0)`, `X_± ↦ (0, ∓1/4, ∓1/4)` and
    `Y_± ↦ (0, ∓1/4, ±1/4)`, all inside the octahedron;
  - its Choi eigenvalues are `{3/4, 3/4, (1 + √2)/4, (1 − √2)/4}`, and the last
    is negative;
  - its Bloch linear part, in `(⟨Z⟩, ⟨X⟩, ⟨Y⟩)` coordinates, is
    `[[1/2, 0, 0], [0, −1/4, −1/4], [0, −1/4, 1/4]]`, with determinant `−1/16`.

  It is a positive, orientation-reversing map: the reflection signature of QA
  [Lemma R](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/quarter-phase-native-20261107/DESIGN.md#L667).
  So the C-CP failure of `G_SM` does not need record conditioning. The switch
  cells' `X_+` laws are still supplied.

**What P★ shows.**

- **Switch cells in non-eigenstate laws.** Sites 1 and 2 hold the switch
  values `u_{i+1}` that select the edge, and they are in `X_+` laws. The record
  then registers an OR of carrier and switch values. Conditioning on it gives a
  non-affine conditioned set, so the carrier law is not uniform on an
  affine subspace. One branch is a valid non-stabilizer state, while the
  complementary branch is not a quantum state.
- **Mechanism.** This is a `q = 2` analogue of M1D Proposition T′(i), in which
  a controller that is not in an eigenstate of its controlling slot produces
  non-quantum encoded states. It is not an instance: T′ is stated at odd `q`,
  in R-W, for a static controller slot, and M1D excludes native dynamical
  controllers from it. P★ is one witness; no `q = 2` dichotomy is derived.
- **Native relaxation of C-IS.** P★ is a native, rational relaxation of C-IS.
  AP1's rung MP-1 posited such a non-isotropic law; here a specified native
  process supplies one. AP1 classifies MP-1-type laws as
  "a per-state relaxation, not a nonclassicality witness"; Theorem NC confirms
  that classification for every protocol.
- **Visibility of the failure.** The record-1 failure is visible only with a
  `Y` read: the pair `(⟨Z⟩, ⟨X⟩) = (1/3, −1/3)` lies inside the disk.
- **Records and access.** P★ registers a ring site that keeps evolving, so P1
  terminality is not implemented. Its record is a configuration function used
  as an H-PREP conditioning.

**Scope.** P★ is one exhibited instance. Two questions are not decided:

- whether some `G_SM` protocol gives a complete instrument with every branch
  CP and one non-stabilizer branch;
- whether unconditioned `G_SM` channels ever leave the octahedron.

Theorem NC makes either outcome classical under R1.

### Node 7. Other encodings

- **Uniform linear encodings (FB).** FB's proof uses only the common Markov
  kernel of any adaptive stochastic protocol, so the dynamics never enters.
  Under H-L, H-C and H-T, `S` with C-CP is excluded for `G_SM` exactly as for
  N. To escape, `G_SM` would have to break one of these hypotheses:
  - H-L, with non-uniform level-set preparations. P★-type conditioning
    produces such laws, but together with non-quantum branches;
  - H-C, with lifts that depend on the preparation. Nonlinear conditioning
    can make hidden lifts depend on preparation history (asserted, not shown here; linear record-conditioning can also correlate hidden cells with the carrier in a preparation-dependent way). This is the native
    opening, discussed below;
  - H-T. Withholding translations only to remove reflections is CC-RECON
    (QA premise I).
- **Non-injective encodings (QA's U′; P-8).**
  - Theorem U2's Birkhoff-free step needs injectivity. For a non-injective
    `R`, `B` is not unique and need not be orthogonal. QA's encoded `S` in U′
    lives there, with the reflections of Lemma R.
  - Theorem NC fails for the native model exactly when two reachable laws with
    the same encoded operator are both used. The model is then
    preparation-contextual, and no conclusion follows about other models.
  - AP1's [remark beyond R1](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/apparatus-1-20261107/DESIGN.md#L933)
    adds a constraint. A finite carrier realizing the full single-qubit
    stabilizer subtheory needs ontic directions that its preparations and
    reads do not span, as P-8's parity does.
- **Common conclusion.** Every nonclassical route at `q = 2` needs an ontic
  functional that the dynamics uses and the observer can never access. A
  preparation-dependent hidden lift (the H-C break) is such a functional only
  if it stays inaccessible under every permitted read, reuse and
  recombination. Otherwise H-LIFT enlarges the carrier and Theorem NC applies
  again. `G_SM` provides the use but not the inaccessibility, and Lemma Q's
  argument does not apply to it (node 5; whether the protection fails under
  P1 and P2 is open).

### Node 8. Odd `q` (conditional remarks)

The statements below are conditional on #1193 (WAVE-SIGN-1) wherever the
memory sign enters. M1D uses `u′ = F(u) − v`.

- **Sign-independent.**
  - Lemma F, Theorem NC and Proposition B hold verbatim with R-W.
  - Theorem U2(ii)'s step "nonnegative orthogonal ⇒ permutation" holds, and
    M1D Proposition AS then gives: every encoded unitary induced by any fixed
    bijection is Clifford. This extends M1D Proposition C(b) from N to all
    dynamics.
  - `G_SM` at odd `q` is a non-affine bijection: the switch tests
    `x_{i+1} = 0`. So its joint encoded action is not CP (AS). This repeats
    M1D [node 8](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L877)
    with the sign removed from the argument.
- **Sign-dependent.**
  - The mechanism-off control at odd `q` falls back to a CP native step only
    with the `−v` rule. The `+v` rule is anti-symplectic (M1D node 2).
  - The odd-`q` selection statement of M1D node 4 is likewise conditional.

## 4. Shortcut checks

| Check | Finding |
| --- | --- |
| SC-1 Imported quantum behaviour | **None imported into the dynamics.** `G_SM` is a configuration bijection taken verbatim from SM. CP is computed as a test (Theorem U2, P★), not assumed. R1 is the representation fixed by AP1, with native reads as encoded Pauli reads. No unitary, interference or CP restriction enters as a premise. The comparator enters only as the test. The CP verdicts are relative to R1, whose covariance group is `A_4 ≀ S_n` and not the Clifford group. Joint-CP failure under R1 therefore also covers class N and AP1's read tick. The discriminating C-CP evidence against `G_SM` is P★, including its record-free channel (node 6) |
| SC-2 Hidden external control | **Coupling selection is in-world. Preparation is supplied.** The edge choice is made by switch cells under the fixed rule, with no P3 arming. P★'s carrier input, ready cells, hidden-cell pattern, choice of record cell and time, and the conditioning are supplied (P2, H-PREP). P1 is not implemented. A physical preparer for the ready region is unsupplied, as in PI §4.1. The C-CP failure itself does not need the supplied conditioning: P★'s record-free channel at `t = 3` is already not CP (node 6). The switch cells' `X_+` laws remain supplied |
| SC-3 Representation versus physical implementation | **The capability is in the representation.** On the physical carrier every step is a permutation (node 1). The non-stabilizer state of P★ is a law on four points whose R1 image lies outside the octahedron. Its `(⟨Z⟩, ⟨X⟩) = (3/5, 1/5)` lies inside the stabilizer diamond, so only a `Y` read, not exhibited natively, distinguishes it from an octahedron state. Under H-LIFT and spanning certification the noncontextual configuration model reproduces all of its statistics (Theorem NC) |

## 5. Ledger

| Item | Content | Native or supplied | Classification | Status |
| --- | --- | --- | --- | --- |
| G1 | Second-order bijective form, memory term | Native | Native (A2; SM:106, SM:224) | At `q = 2` independent of the memory sign |
| G2 | State dependence of the graph | Supplied | Independently motivated proposal (SM:104) | Not physically sourced |
| G3 | Ring `R(i, x)` of SM:112 | Supplied | Example of G2 | Not selected by OI |
| G4 | Non-affinity (A5 fails), non-reciprocity (`L ≥ 5`) | Consequence of G3 | — | Lemma Q's argument does not apply (node 5) |
| Nq | `q = 2` | Native parameter value | Chosen per owner item 2 | Odd `q`: node 8, conditional |
| N2 | Uniform law on unknown slots | Native measure through H-PREP | As in AP1 | — |
| P1, P2, H-PREP | Terminal registration; ready cells; record-conditioned preparations | Supplied | Carried from AP1 | P★ uses P2 and H-PREP; P1 not implemented |
| H-LIFT | Correlated cells belong to the encoded carrier | Supplied | Modelling condition (FB H-C) | Hypothesis of Lemma F and Theorem NC |
| R1 | Tetrahedral frame per cell | — | Mathematical representation | Comparator dictionary only |
| H-Bell | Preparation-indexed edges with no-signalling and curvature stability | Supplied | Open hypothesis | Unchanged. Proposition B derives M-FIX as a necessary consequence of its clauses (i)–(ii) with a violation |
| M-INACC | Dynamically used, permanently inaccessible functional per encoded system | Supplied | Missing premise (§6.2); not adopted | CC-RECON if adopted only to reach the target |
| M-FIX | The available laws on the response-relevant variable do not span: some nonconstant response-relevant function has the same mean under every available preparation (equivalently, some nonzero function has mean 0 under all) | Derived necessary condition | Elaboration of H-Bell (i)–(ii); not adopted | A variable with a fully fixed law is sufficient, not necessary (node 4 counter-model) |
| I1 | Qubit stabilizer comparator | — | Imported (comparator) | — |
| I2 | Proposition AS (M1D), using Gross's theorems as read in M1D | — | Repository support on `main` | Used in Theorem U2 (⇒, Kraus step) and node 8 |

## 6. Outcome

### 6.1 Acceptance criteria at `q = 2`

| Criterion | Verdict | Basis |
| --- | --- | --- |
| A1 Native mechanism | **Defined.** One fixed rule, `G_SM`. Its status is an independently motivated proposal, not a physically sourced mechanism | §1 |
| A2 Non-stabilizer capability | **Not met.** Reversible operations fail for every fixed bijection under R1^⊗n and H-LIFT (Theorem U2). A valid non-stabilizer state appears in P★'s record-0 branch. Its instrument fails C-CP, so D1 does not count it. No C-COMP candidate exists | Nodes 3, 6 |
| A3 Quantum selection | **Fails.** P★'s branches are not CP. P★'s record-free channel at `t = 3` is not CP either: Choi eigenvalue `(1 − √2)/4`, Bloch determinant `−1/16`, the reflection signature of QA Lemma R. No structure of `G_SM` excludes such reflections. Lemma Q's argument does not apply (node 5). That no coupling rule is jointly CP under R1 (Theorem U2) holds for class N too and does not discriminate | Nodes 3, 5, 6 |
| A4 In-world control | **Ontically in-world; fails C-CP in P★.** Switch cells select the coupling under the fixed rule. In P★, whose switch cells are in `X_+` laws, the outputs are non-quantum, with and without the record. By Theorem U2, joint CP under R1 admits no selection at all. M1D's remedy at odd `q` is CTRL-MON-type supplied monitoring; its `q = 2` form is not derived here | Nodes 3, 6; [M1D M1](https://github.com/amaybaum/incompleteness/blob/120b3ca40d94fdab8db1ad271db299ff44360f2c/verification/programmes/oi-qm/reconstruction/mechanism-1-20261107/DESIGN.md#L940) |
| A5 Operational completeness | **Not met.** P★'s complete instrument has a non-quantum branch. Its outgoing world is not in a ready slice (as PI §5.2 finds for the same rule). K1–K6 have no CP candidate to act on | Node 6 |
| A6 Classical countercontrol | **Classical imitation is exact under R1^⊗n, H-LIFT and spanning-read certification.** There the configuration model is universally noncontextual for every protocol and every `G(x)` (Theorem NC), and product encoded effects give CHSH ≤ 2 (Corollary NC-B). At `q = 2` the certification needs a `Y` read that is not exhibited natively. At the native read level (`Z` and `X` only) statistical equivalence is coarser, Theorem NC does not apply, and A6 is undecided: there is neither a witness nor a proved exact imitation | Node 4 |

| Control | Result |
| --- | --- |
| C-PH, C-ROT | Hold for every dynamics under R1^⊗n and H-LIFT (Theorem U2; AP1 Lemma 5 and §5.3) |
| C-CP | Fails on P★'s branches and on its record-free channel at `t = 3` (reflection type). No jointly CP coupling exists under R1, for any rule |
| C-IS | Fails natively on P★'s record-0 branch, which is valid but outside the octahedron. This is a per-state relaxation |
| C-NS | `G_SM` has range 2: for wings outside each other's `2t` envelope, the screened ceiling applies (PI §6; Main:366). For preparation-indexed edges, Proposition B gives M-FIX |
| C-LEAK | P★'s record-1 branch has statistics no quantum state has (a deterministic `Y` with biased `Z` and `X`). The excess over the comparator is reached through a record, not through a hidden channel |
| C-Q | Lemma Q's argument does not apply (Lemma Qσ(b); nonlinear transport). Conservation of `Q` returns with mechanism off and with a symmetric switched graph. Whether the protection fails under P1 and P2 is open |
| CC-OFF | Green: mechanism off gives class N's conserved `Q` (c3) and stabilizer outputs on P★ (c5) |
| CC-IMIT′ | Passes everything under H-LIFT and spanning-read certification (Theorem NC). Undecided at the native `Z`/`X` read level |
| CC-RECON | No premise was adopted. M-INACC is flagged in advance if it is ever adopted only to reach the target |
| C-EX | c1–c7. Controls that must break did break: odd permutations, the transvection, `Q` under `G_SM`, and P★ with the mechanism on |

### 6.2 Type (ii) stop: the missing premise

**What the result says about state-dependent dynamics.**

- Under an injective identification (the programme's R1 encoding, or Gross's
  frame at odd `q`), with H-LIFT and spanning-read certification, the dynamics
  does not decide nonclassicality: Theorem NC holds for every fixed bijection.
  At `q = 2` that certification needs a `Y` read that is not exhibited
  natively. At the native `Z`/`X` read level A6 is undecided.
- What state dependence adds at `q = 2` is non-affine conditioning. This
  relaxes per-state bounds. In P★ it produces non-quantum branches, and the
  record-free channel is already a non-CP reflection-type map.
- It adds no reversible capability (Theorem U2, under H-LIFT). Under H-LIFT
  and spanning-read certification it adds no capability that a classical
  model lacks.

The answer to the owner's main objective, at this scope (R1^⊗n, H-LIFT,
spanning-read certification): `G_SM`'s new encoded behaviour is another
representation of classical behaviour. With only the native `Z`/`X` reads the
question is not decided. Whether `G_SM` supplies a native `Y` read (node 4) is
the first item that bears on it.

**M-INACC (conditional extension premise, not adopted).**

- *Statement.* For each encoded system there is an ontic functional with
  three properties:
  - the fixed rule uses it, so later statistics depend on it;
  - no permitted preparation, read, reuse or recombination determines it or
    changes its conditional law;
  - its inaccessibility follows from a structure stated without reference to
    the quantum target.
- *Why it is needed.* By Theorem NC, a contextual observer-level theory
  needs operational equivalences coarser than ontic equalities, and they must
  hold for a physical reason. Otherwise a list of omitted reads gives
  artefactual contextuality (node 4 scope).
- *What it preserves.* AP1 Lemma 2, Theorem U2 for injective sub-encodings,
  FB within H-L, H-C and H-T, and Lemma F.
- *What it buys.* It opens the class in which AP1's rung P-8 and QA's U′ live,
  with LWE-type transformation contextuality relative to the encoded
  subtheory (QA node 8; AP1 §5.2).
- *Independent consequence (§A.29).* None established. As a bare posit it is
  easy to vary, and it is flagged CC-RECON if adopted only to obtain `S`.
- *Relation to `G(x)`.*
  - Native class N has a native instance: Lemma Q protects every functional
    with `Q* = 1`.
  - Lemma Q's argument does not apply to `G_SM`: its conclusion (i),
    conservation of `Q`, fails (Lemma Qσ(b)), and transport is nonlinear.
    P★'s record-1 branch determines the carrier's `Q* = 1` functional `z + x`,
    but through a non-terminal record (not under P1). Whether the protection
    fails under P1 and P2 is open.
  - A symmetric, center-free switched graph keeps the conservation (Lemma
    Qσ(a)).
- *What would derive it.* A symmetric `G(x)` under which Lemma Q(iii)'s
  conclusion survives nonlinear transport: no protocol under P1 and P2
  determines a `Q* = 1` functional. Such a graph would also have to keep FB's
  reflections out by a sourced structure.
- *What would rule it out.* Either of the following:
  - a protocol of the symmetric graph under P1 and P2 that determines a
    `Q* = 1` functional;
  - a proof that every functional the dynamics uses becomes determinable
    through reuse or recombination.
- *What would weaken it.* Nothing smaller was found.

**M-FIX (composites; necessary condition derived from H-Bell, not adopted).**

- *Statement.* Given determinism and measurement independence, H-Bell
  (i)–(ii) together with a Bell violation imply that the available
  preparations' laws on the response-relevant variable do not span. Some
  nonconstant response-relevant function `g` then has the same mean under
  every available preparation; equivalently, some nonzero `g` has mean 0
  under all of them (Proposition B).
- *Strength.* A response-relevant variable with a fully preparation-independent
  law is sufficient but not necessary. The counter-model of node 4 fixes only
  the conditional law of `h` given `k = 1`, and reaches CHSH = `2 + 2s`.
- *Native candidate.* A conditional law fixed by the hidden sector's counting
  measure.
- *Open.* Whether preparation-indexed edges couple only to response-relevant
  functions of that kind.

### 6.3 No V3 round

The verdicts rest on paper proofs: Lemmas F, H and Qσ, Theorems U2 and NC,
Proposition B, and the exactly stated instance P★.

- **Decisive and finite, but not proposed.** The first check of a symmetric
  `G(x)` (§6.2) can be decided for a fixed small ring and bounded protocol
  depth. That would only settle a premise this unit does not adopt, so no
  round is proposed.
- **Not finite.** The general question, which physical structure supplies
  M-INACC, is not a finite search.

### 6.4 Bearing on Q-B (not activated)

- Under any finite orthogonal frame and H-LIFT, encoded unitaries induced by
  any dynamics are frame symmetries (Theorem U2(ii), whose proof uses only the frame and Lemma F).
- They therefore form a finite group, with no encoded rotation of infinite
  order.
- So on a finite carrier there is no exact encoded `rot` and no encoded
  unitary of infinite order, for any fixed bijection under H-LIFT (with AP1
  §5.3).
- `G(x)` on an infinite carrier or an infinite hidden sector is not assessed
  here; finite observer capacity does not imply a finite world.

### 6.5 Not claimed

- A physical source for `G(x)`, H-Bell, M-INACC or M-FIX.
- A non-stabilizer operation that passes C-CP.
- Contextuality, interference, a Bell violation, or quantum equivalence.
- Any statement about preparation-indexed long edges beyond Proposition B.

Theorems U2 and NC, Proposition B and Lemmas F, H and Qσ are paper derivations,
not kernel theorems.

## 7. Classification (§A.31) and assumption-watch markers

| Finding | Class |
| --- | --- |
| Theorem U2 with Lemma H: CP permutations of R1^⊗n are `A_4 ≀ S_n`. Every encoded unitary of any fixed bijection is among them. No coupling rule is jointly CP at `q = 2` | New for this programme (under H-LIFT). It generalizes AP1 Lemma 5 to `n` cells, to all unitaries and to all fixed bijections. Lemma H is the classical rigidity `Aut H(n, q) = S_q ≀ S_n` of Hamming graphs, proved here for `q = 4` and credited as context |
| Theorem NC: under an injective identification, H-LIFT and spanning-read certification, the configuration model is universally noncontextual for every dynamics | New application for this programme; an instance of the nonnegativity ⇒ noncontextuality direction of Spekkens (2008), credited as context. AP1 Lemma 4′ is its one-cell, preparation-only instance |
| Proposition B: spanning no-signalling removes ontic parameter dependence pointwise | Elaborating (Main §3.3, H-Bell (i)–(ii)); a linear-algebra form of the Wood–Spekkens fine-tuning point, credited as context. Derives non-spanning (M-FIX) as necessary for a violation |
| Lemma Qσ: Lemma Q's conservation fails for `G_SM`, so Lemma Q's argument does not apply; symmetric center-free switched graphs keep the conservation | New |
| P★: a native heralded non-stabilizer encoded state, inside a C-CP-failing instrument; its record-free channel is a non-CP reflection-type map | New instance; confirming AP1's MP-1 classification |
| FB applies to every `G(x)` | Confirming (FB's proof never uses the dynamics) |

**Assumption-watch markers.**

- **Injective identifications decide classicality, not dynamics.** Any future
  mechanism proposal under R1-type encodings, whether nonlinear, state-dependent
  or Native A, falls under Theorem NC wherever H-LIFT holds and the equivalences
  are certified by spanning reads. A nonclassical claim must show where
  injectivity, H-LIFT or the spanning certification fails, and why.
- **Access lists.** A contextuality witness certified over an incomplete read
  set, such as `Z`/`X` without `Y` at `q = 2`, can be an artefact of the
  omitted reads (node 4 scope).
- **Switch cells as controllers.** In `G(x)` the switch cell is a controller.
  P★ is a `q = 2` analogue of M1D's T′(i). T′ itself is odd-`q`, R-W and
  static-controller, and no `q = 2` dichotomy is derived here.
- **Non-reciprocal state dependence escapes native protection arguments.**
  Lemma Q is proved for symmetric center-free linear rules only, and the SM
  ring is neither symmetric nor linear. Whether its protection actually fails
  under P1 and P2 is open.

## 8. Sources

### 8.1 Repository sources (all on `main@120b3ca4`)

All repository sources are on `main` at the pinned commit and are cited at their
stated scope. Issue comments are cited as **provenance** only.

| Source | Use | Classification (§A.42 item 8) |
| --- | --- | --- |
| SM:88, :104–:112, :152–:158, :224, :226 | Construction; constraints; preparation-indexed edges; form lemma; nearest-neighbour scope | Manuscript text (support on `main`) |
| Substratum A2–A6 (L94–L102), :131–:133, :171 | Axioms; H-Bell | Manuscript text |
| Main:296, :364–:366, :414–:416, :429 | Sign marker; cone and screened ceiling; option (a); no-signalling requirement | Manuscript text |
| GR:112–:118 | Boundary-only dependence | Manuscript text |
| M1D Proposition AS (L516), Theorem T (L799), Proposition T′ (L804), node 8 (L877), M1 (L940), C-COMP (L360) | Kraus step; odd-`q` remarks; controller dichotomy | Support on `main` (#1191), at its reviewed scope |
| AP1 Lemma 2 (L153), §4.2 (L498), Lemma 4′ (L698), Lemma 5 (L731), MP-1 (L843), remark beyond R1 (L933), §5.3 (L955) | Ceiling; R1; certification scope; `S`; MP-1; P-8; `rot` | Support on `main` (#1183) |
| QA Lemma Q (L460), Lemma R (L667), premise I (L833) | C-Q; reflections; CC-RECON | Support on `main` (#1184, #1189) |
| FB §§2–5 | Dynamics-independent obstruction | Support on `main` (#1189) |
| PI eq. (1) (L110), §§4–6 | Binary reduction; preparation counts; dependency envelope | Support on `main` (#1173), at its stated scope |
| Kernel: `permClass` (SubstratumInterfaceAudit:236), `permTheory_not_control` (:708), `permTheory_not_qm` (:717), `substratumClass` (StructuralClosure:180) | Node 1 (read, not rebuilt). `readWriteSourced_*` is not cited (#1188) | Kernel statements on `main` |
| #1169 comments 6717234497 (authorization), 6714136234 (addendum), 6713653816 (conditions trace); #1193 (memory sign) | Scope, authorization, the conditions profile, conditional status | Provenance |

The conditions trace (#1169 c.6713653816) finds (i), (ii), (iii) and (v)
supplied and (iv) failing for the stated interventions, with monomiality as the
obstruction. Node 1 is consistent with it: `G_SM` adds no non-monomial physical
operator. Its encoded operations stay within the classical model of node 4.

### 8.2 Imported literature

No external work is relied on. The external host `arxiv.org` was not reachable
from this session, and nothing was read first-hand in this unit.

- **Recomputed here.** Facts about the qubit tetrahedral frame and the
  Hamming-graph rigidity are proved or recomputed in this file (c1, c2,
  Lemma H). The real orthogonal nonnegative-matrix step is elementary.
- **Used through repository records.** Gross's theorems enter only through
  M1D's Proposition AS, at the scope M1D read them. Lillystone–Wallman–Emerson
  enters only through AP1 and QA.
- **Context, not premises.** None of the following was read in this unit;
  the proofs here are self-contained.
  - Theorem NC is an instance of the "nonnegative frame representation ⇒
    noncontextual model" direction of Spekkens, *Negativity and contextuality
    are equivalent notions of nonclassicality*, PRL 101, 020401 (2008),
    arXiv:0710.5549.
  - Proposition B is a linear-algebra form of the point of Wood and Spekkens,
    NJP 17, 033002 (2015), arXiv:1208.4119: causal explanations of Bell
    violations need fine-tuning to reproduce no-signalling.
  - Lemma H is the `q = 4` case of the classical rigidity
    `Aut H(n, q) = S_q ≀ S_n` of Hamming graphs.

## 9. Verification scope

Every verdict rests on the paper arguments of §3 and the exactly stated
instance P★. The author self-checks are uncommitted controls. "Exact" means
`Fraction`, integer or `sympy` arithmetic.

| Check | What it controls |
| --- | --- |
| c1 | R1 single cell (exact): unit trace and orthogonality; triple-trace values `5/2`, `1/2`, `−1/2 ± i`; the 12 even permutations CP, the 12 odd not; triple-trace automorphisms equal to the even permutations |
| c2 | `n = 2`: the 288 triple-trace automorphisms equal `A_4 ≀ S_2` (exact); 1152 Hamming automorphisms; numerical Choi control (automorphisms ≥ −7·10^{−16}; transvection −1) |
| c3 | SM ring at `q = 2`, `L = 4, …, 7` (exhaustive): binary reduction (1), bijectivity, `Q` changes, mechanism-off conserves `Q`; `q = 3` bijectivity; nonzero second difference |
| c4 | P★ at `L = 9, 12, 13` (exact): laws, records and Bloch vectors as tabulated. Hand-chosen backgrounds B1–B4 at `t = 1, 2, 3` were evaluated as stated instances; no sweep was run |
| c5 | CC-OFF on P★: the mechanism-off rule gives `Z_±`; the known-switch case gives `Z_+` |
| c6 | Lemma Qσ identity, `L = 5, 6, 7` (exhaustive); conservation under the symmetric switched graph |
| c7 | P★'s background without a record at `t = 3`, `L = 12` (exact): Choi eigenvalues `{3/4, 3/4, (1 ± √2)/4}`, Bloch linear part with determinant `−1/16`, all Pauli eigenstates mapped into the octahedron |

No Lean build, simulation campaign, enumeration campaign, manuscript edit,
freeze, dispatch or merge was performed. Independent review of this file is a
separate step.
