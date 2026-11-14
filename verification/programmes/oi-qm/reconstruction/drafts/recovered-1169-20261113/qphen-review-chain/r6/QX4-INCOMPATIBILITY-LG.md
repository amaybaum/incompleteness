# QX-4: measurement disturbance, incompatibility, and Leggett–Garg with invasiveness controls — Phase 1 experiment specification (draft r6)

## 0. Standing

- **Common conventions.** Standing, snapshot (`origin/main` = `fd539e15`), evidence layers (K, P, W, D, X, A, L), and the
  separate type and dependency columns are as in `QX3-ANTIBUNCHING.md` §0 (r6).
  - Types: EN, CS, IQ, IR, untyped.
  - Dependencies: MC, MECH-OPEN, —.
- **Status.** Paper only and model-written. No mechanism is built, no computation on any proposed OI mechanism is
  run, and no criterion is frozen (#1210 c.6736966265). Exact checks of paper claims on generic mathematical objects
  are allowed when labelled as such: "Allowed: generic checks" (#1210 c.6739250392, owner, 2026-11-09). The checks
  cited here (probes P1–P11 under `review/probes/`) are of that kind, and a result supported only by such a check is
  marked computation-supported in `SHARED-MECHANISM.md` §8.
- **Revisions.** Earlier texts are kept under `r1/`, `r2/`, `r3/`, `r4/` and `r5/`. The revision record is
  `DISPOSITIONS-r6.md`.
- **Claim status** of this file's claims (proved, disproved, open) is given in `SHARED-MECHANISM.md` §8, and the
  restrictions it uses in §9.

***

## 1. The phenomenon and its operational observables

One carrier, one detector set and one construction are shared by three parts.

**QX-4a. Disturbance and order dependence.** A two-valued carrier is prepared and read sequentially by detectors `S_Z`
and `S_X`: QX-0's path and port reads, and C's `S_Z` and `S_X` meters. The observables are:
- the sequential joint laws `P(z₁, x₂)`, `P(x₁, z₂)` and `P(z₁, x₂, z₃)`;
- order dependence, `P_{Z→X}(z, x) ≠ P_{X→Z}(z, x)`;
- repeatability, `P(z₃ = z₁)`, with and without an intervening `X` read;
- no-signalling in time (NSIT; Kofler and Brukner, PRA 87, 052115 (2013); L): `P(z₃)` with and without a read at
  `t₂`, the outcome of that read summed over.

**QX-4b. Incompatibility witnessed by a parity-oblivious task.**
- Four preparations are labelled by two bits `(b₀, b₁)`. A read of `S_Z` or `S_X` guesses `b_y`.
- The observable is the success rate `P_succ`, together with parity-obliviousness checked over the fragment's own
  operational equivalences.
- `P_succ > 3/4` with parity-obliviousness witnesses preparation contextuality: every preparation-noncontextual model
  gives `P_succ ≤ 3/4` (Spekkens et al., PRL 102, 010401 (2009); L).
- This is QX-5's method applied to a two-read fragment. It is proposed to run as a QX-5 scenario (§4; programme rule
  6).

**QX-4c. Leggett–Garg with invasiveness controls.**
- One binary quantity `Q = ±1` is read at `t₁ < t₂ < t₃`, with one fixed operation `G` applied between reads.
- `C_ij = ⟨Q_i Q_j⟩` comes from runs that read only at `t_i` and `t_j`.
- The four forms are `K₃^{(s)} = s₁C₁₂ + s₂C₂₃ + s₃C₁₃` with `s₁s₂s₃ = −1`. Macrorealism per se together with
  non-invasive measurability (and induction) bounds each by 1 (Leggett and Garg, PRL 54, 857 (1985); L). The standard
  form is `K₃ = C₁₂ + C₂₃ − C₁₃`.
- Three invasiveness controls:
  - **(i) Adroitness.** Each `t₂` read is applied to each eigen-preparation of `Q`, and its effect on the subsequent
    law of `Q₃` is measured. This reduces the clumsiness loophole to a collusion loophole (Wilde and Mizel, Found.
    Phys. 42, 256 (2012); abstract read).
  - **(ii) Ideal negative measurement (INM).** `Q₁` is fixed by preparation. A detector at `t₂` that couples only to
    one value of `Q` is used, and only its silent runs are kept, for each of the two placements (Knee et al., Nat.
    Commun. 7, 13253 (2016); Robens et al., PRX 5, 011003 (2015); L).
  - **(iii) NSIT at `t₂`.**

**Observer access.** Detector records only, with conditioning on recorded outcomes. Every detector is a meter cell
coupled through the native step and terminally registered (SA-1(b)).

**Validation layer** (from the construction; per detector):
- the kernel `K` of the unread conjugate functional (Q-C2-1 `DESIGN-DS.md` §4 [D]);
- for an INM detector, the kernel `K_null` of its silent branch;
- `D`;
- whether `Q` is identified with a configuration functional. This is an IR premise, and it decides whether
  macrorealism per se holds of `Q` in the ontic model.

## 2. QM's predictions and the classical alternatives each witness excludes

**QM predictions** (comparators; IQ; Lüders instruments unless another instrument is named).
- **4a.** For `Z⁺` then `X` then `Z`, `P(z₃ = z₁) = 1/2`; it is 1 without the `X` read. The sequential `Z/X` laws depend
  on order. For a Lüders read at `t₂` that does not commute with the evolved `Q₃`, NSIT fails for some preparation.
- **Joint measurability.** Unsharp `Z` and `X` with sharpnesses `η_Z`, `η_X` are jointly measurable iff
  `η_Z² + η_X² ≤ 1` (Busch, PRD 33, 2253 (1986); L). Classical mixing of sharp reads reaches only `η_Z + η_X ≤ 1`.
- **4b.** For a qubit, `P_succ = (1 + 1/√2)/2`. This needs non-stabilizer preparations or reads at `π/4`. With
  stabilizer preparations and Pauli reads, `P_succ ≤ 3/4`.
- **4c.** For a qubit rotated by `θ` about an axis `n` between `Z` reads, `C(θ) = n_z² + (1 − n_z²)cos θ`.
  - With `n ⊥ z`, `K₃ = 2cos θ − cos 2θ`, which is maximal at `θ = π/3` with `K₃ = 3/2`. All probabilities there are
    rational (Main:486, `lg_comb_probes.py`).
  - `3/2` is the **Lüders bound**: the maximum of `K₃` for dichotomic projective reads with the Lüders state update,
    in any dimension (Budroni and Emary, PRL 113, 050401 (2014); L, not read first-hand). Proof [A]:
    - For a Lüders read of `Q = P₊ − P₋` at `t_i` and a later read at `t_j`, `C_ij = ½⟨{Q_i, Q_j}⟩`, with Heisenberg
      operators `Q_i = (G^{i−1})† Q G^{i−1}` in the initial state. This follows from the identity
      `P₊AP₊ − P₋AP₋ = ½{Q, A}`, valid for every operator `A`, applied with `A = (G^{j−i})† Q G^{j−i}`.
    - Each `Q_i² = I`, so `0 ≤ ⟨(Q₁ − Q₂ + Q₃)²⟩ = 3 − 2(C₁₂ + C₂₃ − C₁₃)`, which gives `K₃ ≤ 3/2`. Degenerate `Q`
      is included. The other three forms follow by sign changes.
    - Exact symbolic checks of both identities: reviewer probe `p6_r3rev_lg.py` (3). A numerical search at
      dimensions 2 and 4 finds no value above `3/2` (P5-LG; numerical evidence only).
  - It is not a bound on every quantum protocol. Other quantum instruments exceed it.
    - A measure-and-reprepare instrument (read `Z`, then prepare the other eigenstate), used at every read time, with
      `G = X` and preparation `|0⟩`, gives `C₁₂ = C₂₃ = 1`, `C₁₃ = −1`, so `K₃ = 3`.
    - The instrument that reads `Z` and then prepares the other eigenstate with probability `w`, and the read
      eigenstate otherwise, gives `K₃ = 6w − 3` with the same `G` and preparation. So `K₃ = 2` at `w = 5/6` (P5-LG,
      exact).
    - For von Neumann (non-Lüders) projective reads of a degenerate `Q`, values above `3/2` are reported (Budroni and
      Emary; L, not read first-hand).
  - **QX-4c's comparator protocol** is: Lüders reads of the carrier's `Z`, with unitary `G` on the carrier and any
    mediator. Every comparison of `K₃` with QM in this file is with this protocol, and "QM-matching" means a value in
    its violating range `(1, 3/2]`.
- **INM.** Under the comparator protocol, QM predicts the same violation under ideal negative measurement, through
  the Lüders state update on the silent branch.

**The witnesses and the classes each excludes.**

| witness | excludes | does not exclude |
| --- | --- | --- |
| order dependence; loss of repeatability; NSIT violation (4a) | classical models whose reads are sharp and non-invasive | every invasive classical model. Epistemically restricted models reproduce the stabilizer sequential `Z/X` Lüders law with backaction (Spekkens' toy theory; for construction B, AP1 §0 [W] and OICORE-1 §5(b) [D]). Main's classical comb reproduces arbitrary sequential laws with permutation instruments (Main:478-486 [P, exact]) |
| intermediate incompatibility, a point beyond the line `η_Z + η_X = 1` | nothing classical: a classical wave with a partially rotated polarization marker reaches `V² + D² = 1` | — (quantum-compatible only) |
| 4b: `P_succ > 3/4` with parity-obliviousness on the fragment's equivalences | preparation-noncontextual models **over that fragment's equivalences** | models in which those equivalences fail ontically. A classical two-bit register read one bit at a time reaches `P_succ = 1` (Q-C2-1 `DESIGN-DS.md` §5 finding 6 and r6 review B3 [D]). Contextuality is relative to the fragment and needs an owner-typed access class with a completeness check. The coordinator's planning note #1210 c.6734406842 item 2 restates this; its support is the D finding above |
| 4c: `K₃ > 1` alone | macrorealism per se with non-invasive measurability | every invasive macrorealist model, Main's comb among them (`K₃ = 3/2` with a classical permutation realization; Main:486 [P, exact]) |
| 4c with adroitness control (i) | macrorealist models whose invasiveness shows on eigen-preparations, up to collusion | epistemically restricted invasive models in which the kick lands on a variable already unknown under the eigen-preparation (A4.3). Also the classes Maroney and Timpson identify as untouched by a Leggett–Garg violation (arXiv:1412.6139; abstract read) |
| 4c with INM control (ii), `Q₁` fixed by preparation | macrorealist models in which a silent detector leaves the ontic state unchanged, under A4.4's protocol hypotheses | models with null-result invasiveness, in which the detector acts on the ontic state on its silent branch (A4.4) |

## 3. What the experiment needs from an OI construction

| # | requirement | type | dependency | status |
| --- | --- | --- | --- | --- |
| R4.1 | the step, N2, the `Z±`/`X±` supplies, H-PREP | EN / CS | — | available (shared with QX-0) |
| R4.2 | `S_Z` and `S_X` meters with terminal registration | CS (SA-1(b)) | — | available (C's detectors; AP1) |
| R4.3 | backaction: each record carries a kick on the conjugate functional | EN reciprocity with CS SA-1(c) | — | available. The `Z/X` sequential Lüders law at stabilizer scope is conditional on the SA-1 posits (AP1 §0 [W]; OICORE-1 §5(b) [D]) |
| R4.4 | a fixed operation `G` between reads, applied repeatedly | EN for affine-symplectic `G` | MC for a non-Clifford `G` | Clifford class available; non-Clifford is Obligation C |
| R4.5 | reads at non-Pauli directions, or non-stabilizer preparations (4b's quantum value) | — | MC | not native. `V, D ∈ {0, 1}`; intermediate values only on `V + D = 1` (`DESIGN-DS.md` §5 finding 4 [D]) |
| R4.6 | an owner-typed access class and completeness check (4b) | CS (D15-type) | — | method available (Q-C2-2's exact LP, Farkas certificates, attributed completions [D]) |
| R4.7 | validation fields `K`, `K_null`, `D`; the configuration-functional status of `Q` | method; that status is IR | — | definable |
| R4.8 | the adroitness control | access and validation | — | posable natively with the `Z±` supplies |
| R4.9 | **an INM detector**: location-based detection by a detector on one branch only | untyped (dynamics) | MECH-OPEN | not posable in the encoded setting, where `Q` is a functional rather than a location. It needs QX-3's routing map (R3.6), which is affine under `NCONS_ready` (QX-3 A3.1(b)) and non-affine under `NCONS_global` (A3.1(c)). Over `F_2`, with location cell `c`, carrier conjugate `x` and meter slots `m`, `m′`: the copy coupling `m ← m + c` is affine but not symplectic, and the reciprocal coupling that adds the unconditional kick `x ← x + m′` is affine and symplectic (SHARED Q4-P15). That kick acts on both branches, so the reciprocal coupling is null-result invasive (A4.4). Every location-preserving affine-symplectic coupling whose meter write depends on occupation changes the carrier conjugate `x` on its silent branch, so it is null-result invasive (SHARED Q4-P19 (ii), on `F_2⁴`). An occupation-conditional kick `x ← x + c·m′` is not affine (P4(2), P5-LG(1)). Whether OI's step supplies a location detector of either kind is not evaluated |
| R4.10 | **null-result invasiveness** of the INM detector (`K_null ≠ id`), under A4.4's protocol hypotheses | a constraint on R4.9 | MECH-OPEN | required if QX-4c-INM is to match the comparator protocol (A4.4) |

**Paper derivations and scoped findings** (A unless marked).

**A4.1. Leggett–Garg correlators in the affine-symplectic class, by mode scope.** The read model is a `Z` read that
records `z` and adds an independent uniform kick to the carrier's `x` (SA-1(c) backaction).

- *(a) One mode [A].* For the encoded carrier `(z, x)` under affine-symplectic `G`:
  - an affine `M` sends the functional `z` to `z + c`, `x + c` or `z + x + c`, so `C ∈ {±1, 0}`;
  - by symplecticity, a map fixing `z` up to a constant sends `x` to `x` or `x + z`. So with `a = C₁₂`, `b = C₂₃`,
    `c = C₁₃`:
    - if `a, b ≠ 0`, then `c = ab`;
    - if exactly one of `a`, `b` is 0, then `c = 0`;
    - if `a = b = 0`, then `c ∈ {−1, 0, 1}`;
  - every case gives `K₃ ≤ 1`, and the relabellings give all four forms.
  - Clifford unitaries with Pauli reads give the same table.

  The reviewer's exact probe P3 confirms this over 24 maps with translations and preparations `Z±`, `X±`.
- *(b) Two modes [X: the reviewer's exhaustive finite scan, P3, reproduced by `p6_r3rev_lg.py` (5b);
  computation-supported].* Take the carrier plus one further mode, all 11,520
  affine-symplectic maps with translations.
  - With the second mode half-known (SA-1(c)) or a both-unknown environment, the correlators lie in `{−1, 0, 1}` and
    the maximum `K₃` is **1**.
  - With the second mode **sharp** (both slots known), the maximum is **2**. The witness is
    `G: z′ = z + v, x′ = w, w′ = z, v′ = x + w`, with carrier `X⁺` and mediator `(0, 0)`. It gives `C₁₂ = C₂₃ = 1` and
    `C₁₃ = 0`. The `t₁` read's kick reaches `z₃` through `v`.
  - `K₃ = 2` exceeds the Lüders bound `3/2` of the comparator protocol (§2). It does not exceed what QM reaches with
    other instruments (§2: `K₃ = 2` and `3` with measure-and-reprepare instruments).
  - These are scan results at two modes and one read model, not a theorem beyond that scope.
- *(c) The form relevant to the ladder [A].* Hypotheses: in the affine class, N2 supply laws uniform on a coset; in
  the Clifford class, pure stabilizer preparations of every mode, ancillas and mediators included, and Lüders `Z`
  reads.
  - Under these hypotheses the correlators lie in `{0, ±1}` at any number of modes, so `K₃` is an integer. In the
    affine class, a `±1`-valued affine functional of variables uniform on a coset has mean `0` or `±1`. In the
    Clifford class, a two-read Lüders correlator is `C_ij = Re⟨ψ_i| Z_c (G†)^{j−i} Z_c G^{j−i} |ψ_i⟩`, with
    `ψ_i = G^{i−1}ψ` a stabilizer state. The middle operator is a Pauli product because `G` is Clifford, and a
    stabilizer state gives every Pauli product an expectation in `{0, ±1, ±i}`. The comparator protocol's values in
    `(1, 3/2]` are not integers. So a QM-matching violation needs a non-Clifford `G`, and QX-4c's QM-matching form
    depends on Obligation C (MC). In the Clifford class, integrality and the Lüders bound (§2) give `K₃ ≤ 1` at
    any number of modes.
  - For convex mixtures of pure stabilizer states the correlators need not be integers, but `K₃ ≤ 1` still holds, by
    linearity in the preparation.
  - In the affine-symplectic class with A4.1's read model, the bound `K₃ ≤ 1` itself is established only at the
    scopes in (a) and (b).
  - *Without the stabilizer hypothesis both statements fail* (P5-LG, X, exact; computation-supported):
    - Integrality fails. A `CNOT` from an ancilla `cos θ|0⟩ + sin θ|1⟩` onto a carrier prepared in `|0⟩` gives
      `C₁₂ = cos 2θ`.
    - The need for a non-Clifford `G` fails at two modes, with a non-stabilizer ancilla. *Configuration:* tensor
      order carrier ⊗ mediator, basis `|c m⟩`; `G = (I ⊗ H) · CNOT_{m→c}`, so the `CNOT` has the mediator `m` as
      control and the carrier `c` as target, and then `H` acts on the mediator (the rightmost factor acts first).
      Prepare the carrier in `|+⟩` and the mediator with Bloch vector `(sin β, 0, cos β)`, and read the carrier's
      `Z` with Lüders reads. Then `(C₁₂, C₂₃, C₁₃) = (cos β, sin β, 0)`, so `K₃ = cos β + sin β`. This is `√2` at
      `β = π/4`, and `7/5` at `(cos β, sin β) = (4/5, 3/5)` (probe `p7_r4_lg_order.py`, exact; also P5-LG and
      `p6_r3rev_lg.py`).
    - It fails in the same way with a non-stabilizer carrier and a stabilizer mediator. Same tensor order;
      `G = (I ⊗ H) · SWAP · CNOT_{m→c}`, with `H` on the mediator slot; mediator `|0⟩`; carrier Bloch vector
      `(sin β, 0, cos β)`. Again `K₃ = cos β + sin β` (same probes).
    - The placement of `H` matters. With `H` on the carrier instead, `(H ⊗ I) · CNOT_{m→c}` gives
      `(C₁₂, C₂₃, C₁₃) = (0, 0, cos β)` and `K₃ = −cos β`, and `(H ⊗ I) · SWAP · CNOT_{m→c}` gives `K₃ = 0` (same
      probes).
    - So with a further mode, whether a QM-matching violation needs a non-Clifford `G` depends on the preparations.
      The OI value under C-NONSTABILIZER is not predicted.
  - At one mode the stabilizer hypothesis is not needed (A4.2).
- **Assumption-watch marker AW-QX4-1** (record only; not a result; §A.31 classification NEW, scoped).
  - SA-1(c) appears to carry the affine-scope bound `K₃ ≤ 1`: the bound holds with half-known or environment supplies
    and fails with a sharp one.
  - This rests on a two-mode finite scan with one read model.
  - If it generalized, it would be a consequence of SA-1(c) beyond the complementarity it was built for, a candidate
    §A.29 consequence.
  - Because that reading favours the framework, it needs an independent proof for `m` modes, and other read models,
    before any use.
  - Agreement of that bound with QM's Clifford-scope value is a consistency result (§A.23), not a justification of
    SA-1(c). It counts as an independent §A.29 consequence only if SA-1(c), a restriction modelled on quantum
    uncertainty, is shown not to have been fitted to it. SA-1(c) has no reason independent of QM on record
    (SHARED §9).

**A4.2. At one mode, non-stabilizer preparations alone do not help** [A]. With a single carrier, a Clifford-class `G`
and Lüders `Z` reads, the correlators of A4.1(a) do not depend on the preparation. So at one mode C-NONSTABILIZER
(non-stabilizer states with no non-Clifford fixed operation) does not give a QM-matching violation. With one further
mode the comparator protocol exceeds 1 with a Clifford `G`: A4.1(c)'s two-mode examples give `K₃ = √2` with one
non-stabilizer preparation. The OI value under C-NONSTABILIZER is not predicted.

**A4.3. Adroitness passes in construction B and in QM** [A].
- On a `Z±` preparation the conjugate slot is already uniformly unknown, so a `t₂` read's kick leaves the law of `Q₃`
  unchanged there. Construction B's reads pass the adroitness control.
- They stay invasive on `X±` preparations and at the ontic level: every recording carries a kick (`DESIGN-DS.md` §1
  [D]).
- QM's projective reads pass the same control.
- So adroitness does not exclude epistemically restricted models. A construction-B violation passing it would itself
  be "invasive but adroit".

**A4.4. When OI's ontic model obeys the INM bound** [A]. Hypotheses:
- *(H1)* `Q` is identified with a configuration functional (IR), so macrorealism per se holds of `Q` in the ontic
  model.
- *(H2)* `Q₁` is fixed by preparation from a setting-independent supply, or is itself read by an INM detector with
  `K_null = id`. An ordinary kicking read at `t₁` is excluded. Under A4.1(b)'s sharp-mediator witness, a `t₁` kick
  alone gives `K₃ = 2` while the `t₂` read is ineffective on `Q₃`.
- *(H3)* `K_null = id` for both detector placements.
- *(H4)* Detector placement is independent of the ontic state.

Under (H1)–(H4) the standard Leggett–Garg argument applies to OI's own deterministic model, and every INM form of
`K₃ ≤ 1` holds, against QM's prediction for the comparator protocol (§2).

**Consequence.** Given (H1), (H2) and (H4), an OI construction that matches the comparator protocol's prediction under
INM controls must violate (H3).
It must have null-result invasiveness: the coupling acts on the ontic state when the detector does not fire.
- In the affine reciprocal coupling the kick is independent of the outcome. But the encoded setting cannot pose INM
  (R4.9).
- So an OI QX-4c-INM needs a location-based detector on QX-3's routing map, with a coupling that acts on its silent
  branch (`K_null ≠ id`), for example by keeping the reciprocal, outcome-independent kick that A3.2's control
  requires from QX-3's side.

**A4.5. Leggett–Garg needs two applications of `G`** [A]. The fixity a C instance must show for QX-4c covers two
compositions. C-SIZE-DEPENDENT (fixed at `K = 6`) suffices for posing QX-4c, though not for Level 4's repeated
compositions.

**A4.6. Leggett–Garg values for the spectra C can report** (QM comparators on paper; IQ; not OI predictions; confirmed
by P3's controls).
- **R60 type**, a rotation by `π/3`: `K₃ = 3/2` with the axis `⊥ z`; `K₃ = 4/3` with the axis along a body diagonal
  (`C₁₂ = C₂₃ = 2/3`, `C₁₃ = 0`).
- **`arccos(3/5)`** (possible when `STAB(K)` is false; cone review [D]), axis `⊥ z`: `K₃ = 37/25`.
- **`S_3` type** `{−1, ω, ω²}`: the determinant is −1, so it is not a rotation. Its order-3 rotational part violates
  `C₁₂ + C₂₃ + C₁₃ ≥ −1` (value `−3/2`) when `z` lies in its rotation plane. Whether such a record map is a valid
  transformation is C's `VAL` and `CONS` question.
- The OI value depends on the C operation's axis relative to `S_Z`, its affine part `α`, and the `t₂` read's backaction
  after the gadget. None is computed here.

**Corpus search (§A.19).**
- Main:358 says the intervention dilation "reaches the intervention statistics of any finite instrument set
  (Leggett-Garg violations included, §3.4)".
- Main:486 *Remark (scope of the closure)*: the classical action-labelled comb reproduces `K = 3/2` with invasive
  permutation instruments (`lg_comb_probes.py`, exact). "The open remainder is therefore not the numbers."
- Main:488: *Proposition (no uniform finite realization)*.
- Main:654 (§3.4(iii)): Leggett–Garg protocols "are intervention-rooted and belong to the intervention dilation — the
  delivered formalism underdetermines them". Residual pre-division memory would appear as deviations from quantum
  multi-time predictions.
- Main [26] (Le et al.): temporal Tsirelson for divisible dynamics.

So QX-4c's numbers are already reachable classically in the corpus. QX-4's content is whether one fixed construction
produces them under the controls of §1, with the invasiveness structure of A4.3 and A4.4.

## 4. Reuse of the single shared construction

**Shared with QX-0, QX-1, QX-2 and QX-7.**
- The carrier and supplies, the `S_Z` and `S_X` meters, and the SA-1 clauses.
- The backaction of R4.3, which is the mechanism behind QX-0's complementarity.
- By the programme rule of one shared mechanism (#1210 requirement 1; SHARED §0), `G` is C's, QX-1's or QX-7's
  operation, under the same rule and detectors, and a QX-4-specific gate is not admissible.

**Shared with QX-5.** 4b is a prepare-measure fragment under Q-C2-2's method (exact LP, Farkas certificates,
Lemma NC-F, attributed completions) and QX-5's owner-typed access class.

**Shared with QX-3.** R4.9 and R4.10 need QX-3's routing map and location detectors. Under the same programme rule,
one routing map gives QX-3's exclusivity and QX-4's INM, with null-result invasiveness if INM is to match the
comparator protocol (R4.10), and keeps QX-0's complementarity as A3.2's control.

**Specific to QX-4.** The three-time schedule, the adroitness and INM control runs, `K_null`, and the NSIT pairs.

**Flagged.**
- The identification of `Q` with a detector functional (IR). For C's carrier this is L-CAL and L-UPRIME, under D18(a),
  conditional (#1169 c.6735014875).
- A supplied `π/3` rotation is IQ and is admitted only in a labelled benchmark arm.

## 5. A/B arms and candidate ablations (outline only; not frozen)

**Arms.**
- **`A_4`.** As in Q-C2-1, not posable without B's scaffolding. Its closest posable form drops SA-1(c), which admits
  sharp supplies.
  - 4a: order dependence vanishes for sharp carrier supplies.
  - 4c: `K₃` up to **2** is reachable in the generic affine-symplectic class with a sharp mediator (A4.1(b)). Whether
    `A_4`'s admissible `G` includes such a map is construction-specific. `A_4`'s value is open (Q4-O6).
- **`B_4-nat`.** Construction B with affine-symplectic `G`.
  - 4a: order dependence and NSIT violation (Level 1; classically imitable).
  - 4b: `P_succ ≤ 3/4` at stabilizer scope.
  - 4c: `K₃ ≤ 1` at one mode (A4.1(a)) and at two modes under SA-1(c) or environment supplies (A4.1(b), a scan). For
    `m > 2` it is open (AW-QX4-1).
- **`B_4-C`.** Construction B with `G` a C-EXPOSURE or C-SIZE-DEPENDENT operation. 4c is posable, with the value not
  predicted (A4.6). INM additionally needs routing (`B_4-C-route`).
- **Benchmark.** `G` is a supplied `π/3` rotation (IQ), labelled as a level-3 benchmark.
- **Comparators** (gate nothing):
  - CC-4, Main's classical comb: `K₃ = 3/2`, invasive;
  - NIM-4, a non-invasive macrorealist model: `K₃ ≤ 1`;
  - ER-4, the toy theory at stabilizer scope.

**Candidate ablations.** Each reports `pred_change`, `mech_change` and `access_only`.

| ablation | kind | paper expectation |
| --- | --- | --- |
| ABL-SA1c: sharp supplies admitted | state restriction; credit none | 4a: some reads record without kicking. 4c: `K₃ = 2` reachable (A4.1(b)), above the comparator protocol's Lüders bound `3/2`. `pred_change` true; `mech_change` true. This ablation tests AW-QX4-1 |
| ABL-SA1b: both slots of a meter registered | access; credit none | the observer reads the kick value, so conditioning can undo NSIT and order dependence. `access_only` true |
| ABL-RECIP: copy-only meter | dynamics | no backaction. `pred_change` true for 4a and 4c; `mech_change` true |
| ABL-G: a non-Clifford `G` replaced by a Clifford-class map | dynamics | with stabilizer preparations, `K₃` an integer (A4.1(c)), `≤ 1` with A4.1's read model at one mode, and at two modes under SA-1(c) or environment supplies. With a non-stabilizer preparation and a further mode, not predicted (A4.1(c)) |
| ABL-NULL: INM detector with `K_null = id`, under (H1), (H2), (H4) | dynamics | `K₃ ≤ 1` under INM (A4.4), against the comparator protocol |
| ABL-T1: `Q₁` read by an ordinary kicking detector instead of fixed by preparation | protocol | (H2) fails. `K₃ > 1` becomes reachable from the `t₁` kick alone (A4.1(b) witness). This is a control that INM credit is not taken from the `t₁` read |
| ABL-ACC4b: 4b's access class completed with every slot of every cell | access | an infeasibility, if present, is expected to be restored to a model (Lemma NC-F [D]). It reports the access-relativity |

## 6. Dependence on Q-C2-1's outcomes (decision tree)

```
Q-C2-1 P token
├─ P-VOID / P-NO-RECORD ── R4.3's backaction is unvalidated. 4a holds; 4b and 4c still depend on C.
├─ P-RECORD-WITHOUT-SUPPRESSION ── B admits reads without backaction, so 4a's disturbance is not universal over the
│                          read class. Record this, and require ABL-SA1c's reading (including K₃ = 2) before 4c.
└─ P-COMPLEMENTARITY ──── R4.3 validated (Level 1); 4a reuses P's apparatus.

Q-C2-1 C token (governs 4c and 4b)
├─ C-EXPOSURE
│   ├─ STAB(12) true, R60 type ── 4c posable with G = that operation, over two compositions (A4.5). K₃ depends
│   │                          on the axis and affine part (A4.6) and is not predicted. INM also needs routing.
│   ├─ STAB(12) true, S_3 type ── improper. Posable only for the C₁₂+C₂₃+C₁₃ ≥ −1 form, with z in the rotation
│   │                          plane, and only if VAL and CONS hold.
│   └─ STAB(12) false ──────── spectrum without an order bound; 4c posable; K₃ not predicted.
│   Note: C-EXPOSURE's W-CL conclusions rest on Theorem C [D] and Lemma P (proved, conditional on Theorem C(ii)
│         and L1–L3).
├─ C-SIZE-DEPENDENT ─────── 4c still posable (A4.5). Level 4 cannot be reached from it.
├─ C-NONSTABILIZER ──────── no non-Clifford fixed operation. At one mode 4c has no QM-matching value (A4.2). With a
│                          further mode, a Clifford G with non-stabilizer preparations is not excluded: the comparator
│                          protocol reaches K₃ = √2 there (A4.1(c)); the OI value is not predicted. 4b may be
│                          posable with non-stabilizer preparations, under QX-5's access typing.
├─ C-SURVIVAL ───────────── 4c's QM-matching form is benchmark-only. 4a stays Level 1. 4b's native fragment stays at
│                          stabilizer scope.
└─ C-VOID ───────────────── no reading.

Q-C2-1 B token
├─ B-CONTEXTUAL on B-P (Acc typed CS, D15(a)) ── 4b needs its own Acc and completeness check. Contextuality is not
│                          monotone, so a verdict does not transfer between fragments (Q-C2-2 [D]).
└─ B-CLASSICALLY-IMITABLE ── 4b at stabilizer scope is expected to be imitable too.

D18 ledger / REP-INV: if L-CAL or L-UPRIME is reclassified as imported, 4c on C's carrier is a benchmark result.
```

## 7. Known feasibility obstacles

1. **Invasiveness is constitutive in construction B.** Every read is a coupling through `φ`, and under SA-1(c) every
   record carries a kick (`DESIGN-DS.md` §1 [D]).
   - With `Q` identified with a configuration functional (an IR premise), `Q` is definite at all times.
   - Construction B is then a macrorealist-per-se, invasive model of `Q`. Its Leggett–Garg violation cannot refute
     macrorealism for it. It can only show that its invasiveness has the structure the controls test (A4.3, A4.4).
2. **No QM-matching violation without a non-Clifford `G`, with stabilizer preparations** (A4.1(c)). With a
   non-stabilizer preparation and a further mode this fails (A4.1(c)). In the affine-symplectic class with A4.1's
   read model, `K₃ ≤ 1` itself is established only at one mode, and at two modes under SA-1(c) or environment
   supplies (a scan); in the Clifford class with pure stabilizer preparations, or mixtures of them, and Lüders `Z`
   reads it holds at any number of modes (A4.1(c)). With a sharp mediator the affine-symplectic class reaches
   `K₃ = 2`, above the comparator protocol's Lüders bound `3/2` (A4.1(b)).
3. **INM is not posable in the encoded setting** (R4.9). It needs routing, and under (H1), (H2) and (H4), to match
   the comparator protocol, it needs null-result invasiveness (A4.4), which constrains the coupling QX-3's routing
   uses.
4. **Adroitness does not discriminate** against epistemically restricted models (A4.3).
5. **Incompatibility at native scope is classically imitable** (§2). Intermediate incompatibility (off the line
   `V + D = 1`) needs C's resource and is still only quantum-compatible.
6. **4b's contextuality is relative to the fragment** and needs an owner-typed access class (`DESIGN-DS.md` §5
   finding 6 [D]).
7. **Rational probabilities.** 4b's quantum optimum, `(1 + 1/√2)/2`, is irrational and exactly unreachable under N2.
   4c's `3/2` is rational.
8. **The numbers are not new.** Main:486 already gives `K₃ = 3/2` classically. QX-4c's content is the single fixed
   construction together with the controls.

## 8. Mapping to the significance ladder (no level is awarded from a lower one)

- **Level 1.** 4a with QX-0's validated backaction. A benchmark-form 4c is not credited.
- **Level 2.** At most one of the following, each printed with the classes it does not exclude (§2):
  - 4b's `P_succ > 3/4` over an owner-typed access class;
  - 4c's `K₃ ∈ (1, 3/2]` with the adroitness control. This excludes non-invasive macrorealism and the Wilde–Mizel
    class; construction B itself lies in the class that passes (A4.3).

  A value above `3/2` lies above the comparator protocol's Lüders bound. It is reported as such, not credited.
- **Level 3.** A 4c violation with `G` generated natively (C-EXPOSURE, or C-SIZE-DEPENDENT over two compositions)
  through the shared detectors, with Levels 1–2 holding.
- **Level 4.** Not tested.

## 9. Owner questions (neutral)

- **Q4-1.** Should 4b run as a QX-5 scenario (programme rule 6)? (a) Yes. (b) No; QX-4 carries it.
- **Q4-2.** Which control counts for 4c at Level 2? (a) Adroitness. (b) INM (needs routing; A4.4's hypotheses).
  (c) Both, reported separately.
- **Q4-3.** If C supplies no non-Clifford `G`, how is a supplied one treated for 4c? (a) An IQ benchmark arm only.
  (b) 4c is deferred.
- **Q4-4.** Should AW-QX4-1 (SA-1(c) and the affine-scope Leggett–Garg bound) be opened as its own paper-proof item?
  (a) Yes, with an `m`-mode statement and the sharp-supply countercontrol. (b) Record only.
  A proof would establish a property of SA-1(c). It would not justify SA-1(c).

## 10. References to content off `main` (§A.42 item 8), traced one by one

| reference | claim it is attached to | classification |
| --- | --- | --- |
| #1210 c.6736966265 | §0 scope | provenance (authority) |
| #1210 c.6734406842 item 2 (coordinator's planning note) | §2, 4b row | provenance only. Its content rests on `DESIGN-DS.md` §5 finding 6 [D], which is the support cited |
| #1169 c.6734304025, c.6735014875 (D15(a), D18(a) conditional) | §0 types; §4 flagged identifications; §6 | owner records; quoted where used |
| Main:358, :478-488, :654; `papers/oi_lattice_code/foundations/lg_comb_probes.py` | §2; §3 corpus search | on `main` (P; exact probe) |
| AP1 §0 (`apparatus-1-20261107/DESIGN.md`) | R4.3; §2 | on `main` (W), conditional |
| `oicore/OICORE-1.md` §5(b) | R4.3; §2 | off `main` (D) |
| Q-C2-1 r13 drafts (`DESIGN-DS.md` §§1, 4, 5 findings 4 and 6, 6; cone review; Lemma P review) | R4.3, R4.5; A4.3; A4.6; §6 | off `main` (D) |
| Q-C2-2 `ACCESS.md` §5 (Lemma NC-F) | 4b method; ABL-ACC4b | off `main` (D) |
| `review/REVIEW-PHASE1.md`; probe `review/probes/p3_lg_affine.py` (`82d2099c…`) | A4.1(a) confirmation; A4.1(b) scan and the `K₃ = 2` witness; AW-QX4-1 | off `main` (D). An exhaustive finite computation on generic affine-symplectic objects. It is support for A4.1(b) at its stated scope only |
| QX-3 A3.1 (this programme) | R4.9 | off `main` (A in QX-3) |
| SHARED Q4-P15 and Q4-P19 (this programme); `review/REVIEW-PHASE1-r4.md` (`755c3af0…`) with reviewer probe `review/probes/p8_r4rev_membership.py`; writer's probe `review/probes/p9_r5_symplectic_detector.py`; `review/REVIEW-PHASE1-r5.md` (`fa7fd9fe…`) with reviewer probe `review/probes/p10_r5rev_checks.py`; writer's probe `review/probes/p11_r6_checks.py` | R4.9: the copy and reciprocal couplings' symplecticity; Q4-P19 (i) and (ii) | off `main` (A in SHARED; D for the reviews); exact checks on generic `F_2⁴` objects, each probe importing no earlier one |
| `review/REVIEW-PHASE1-r2.md` (`47af406f…`); probe `review/probes/p4_r2_checks.py` (`2e7c2de9…`) | R4.9's affine and non-affine couplings | off `main` (D); exact finite computation on generic objects |
| writer's probe `review/probes/p5_r3_lg.py` | R4.9; §2's measure-and-reprepare values and the numerical Lüders search; A4.1(c)'s counterexamples | off `main` (D). Exact except the Lüders search, which is numerical evidence only |
| `review/REVIEW-PHASE1-r3.md` (`448614ea…`); reviewer probe `review/probes/p6_r3rev_lg.py` | §2's Lüders identities; A4.1(c)'s placements of `H`; ABL-T1's mixture; independent reproduction of A4.1(a)–(b), A4.6 and §2's values | off `main` (D); exact |
| writer's probe `review/probes/p7_r4_lg_order.py` | A4.1(c): the stated tensor order and gate placement, and the other placement of `H` | off `main` (D); exact; imports no earlier probe |
| Leggett–Garg 1985; Kofler–Brukner 2013; Wilde–Mizel 2012; Knee et al. 2016; Robens et al. 2015; Maroney–Timpson 2014; Spekkens et al. 2009; Busch 1986; Budroni–Emary 2014 (PRL 113, 050401) | §§1–2 | literature. The Wilde–Mizel and Maroney–Timpson abstracts were read; the others were not read first-hand |
