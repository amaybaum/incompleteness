# TUNE-1, Step 2, writer session 1: M0 record and M1 controls

**Plain summary.** This session recorded the owner's choices and then checked, on paper, every
control of the approved Step 2 plan. Controls are test cases whose correct classification is
fixed in advance; if the definitions misclassify one, the plan stops and the definitions go back
to the owner. Five controls came out differently from what the plan expects. The main cause: the
"whole Bloch ball" condition (Q6) is checked on the qubit model chosen to match the observer's
records, and parts of that model's states are not fixed by any record. A model of real quantum
theory, whose states fill only a disk, can be written with states that fill the whole ball while
matching every record exactly, so the condition meant to tell a disk from a ball does not. A
second, smaller cause: two compiled-simulator controls do not meet the ensemble robustness clause
they are expected to meet. The run is therefore void at this stage, as the plan's stopping rule
requires; the linear-rule analysis was not started. Twelve other controls behave as expected,
including the random-walk control, for which an explicit error constant is derived. Nothing here
concerns OI's correctness.

**WIP / UNVERIFIED research record.** Writer session 1 of 3 for Step 2 of TUNE-1 (Issue #1236),
under the owner's paper-only authorization recorded at Issue #1236 comment 6816189419
(2026-11-12), as relayed to the writer; the writer did not read that comment. Paper derivations
only: no code, interpreter or numerical computation was run; no manuscript or Lean file is
changed; no premise is adopted; nothing is frozen, dispatched, merged or promoted.

**Approved text.** `TUNE-1-STEP2-PROPOSAL.md` in this directory at
`e676c42adfe7ff1b4de171d37018d8a569dad1e6`, sha256
`2a081101efae469b39b747ef8f3641f259e55892705bc0f7759adf3ac7499fd5` (checked at the start of the
session; the proposal is not edited here). Section and clause names below are the proposal's.

**Labels.** As in the proposal: **[K]** a Lean statement under `verification/lean-mathlib/OIBridge/`
(statement read, nothing built); **[P]** a manuscript statement; **[R]** a research record on
`main` that states it is not independently reviewed; **[W]** this writer's derivation, unreviewed
and not kernel-checked.

**Sources.** Records are read at the Step 1 pin `cac5d26441dd33e9348151487e4df7b547195481`, as the
proposal fixes. `origin/main` was fetched at `1b27369816e0e26b39b9dcf1ad0335016c6082c9`. Between
the pin and that head, of the files read for M1 only `papers/Main.md` and `papers/SM.md` changed
(PR #1243). The changed lines of Main are the posit ledger (pin :726; it now lists a fourteenth
posit, measurement independence, and rewords items (ii) and (v)) and lines other than :560, :566,
:582, :596, :598; no M1 derivation below uses a changed line.

***

## 1. M0: the owner's choices

Recorded from the owner's authorization (Issue #1236, comment 6816189419, 2026-11-12, as relayed).
They are fixed for this question and are not reopened after a verdict (proposal, M0).

| Choice (proposal section 9) | Owner's option | Effect on Step 2 |
|---|---|---|
| 1. Rule | (b) R-lin first (node L5), then R-nl as a separate verdict under H-nl | R-lin node before any R-nl work; H-nl carried by every R-nl conclusion |
| 2. Alphabet | (a) every fixed `q ≥ 2`, `q = 2` first | Statements per fixed `q` |
| 3. World | (b) finite tori, and `𝓛_∞` under H-∞ as a separate conditional result | Separate tokens for `𝓛_fin` and `𝓛_∞` |
| 4. Error measure and horizon | (a) TV on complete records, every `K`, `N(ε, K)` explicit | Fixed-`K` results are `PARTIAL-FIXEDK` |
| 5. How the observer chooses | (c) both modes, reported separately | `init` and `exch` (under H-write) tokens kept apart |
| 6. Ensemble | (i)(c) every law of the list, each with its own token, with the robustness clause of D3 | Uniform law, level-set law (on `𝓛_fin`, exchange mode; "not defined" elsewhere, 6(iii)), non-uniform product law |
| 7. Rebit or qubit | (a) the whole Bloch ball (Q6) | A disk is `PARTIAL-REBIT` |
| 8. Partial results | (a) reported, each labelled as not answering the question | |
| 9. [R] premises of a negative | (a) re-derive in the unit (MECH-1 Lemma A, MECH-2 Lemma F) | |
| 10. Effort bound | (a) three writer sessions with reviews | This is session 1 |
| 11. Compiled simulators | (a) supplied (`OPERATIONAL-ONLY`) | D6 consists of tests (a) and (b) |

**Hypothesis ledger at M0.** H-μ, H-∞, H-nl and H-write are named and not adopted. No M1
derivation below uses any of them: the controls are classified from their own constructions.

**M0 approval statement.** The proposal requires the owner's approval record to state: "A
`PASS-DERIVED` would be a consistency-axis result (§A.23); it would move no correctness
assessment." The independent review of this session read comment 6816189419. It reports that the
owner's account posted the comment through the Claude GitHub app on 2026-11-12 at 06:11:10Z. The
comment quotes the owner's chat answers, it matches the choices in the table above, and it states
the paper-only scope. It does not contain this statement. The writer has not read the comment, and
records the absence as the review reports it. The statement is an open owner item, and it must be
supplied before any session that could render a pass (section 6, question 5).

***

## 2. M1: the controls

### 2.1 Readings of the text used in the evaluation

Where the definitions leave a choice open, the reading taken is listed with the rows whose
classification depends on it. No definition is changed.

- **Rd-1 (Q1's error).** "Distinguished with error at most `ε`" is read as: the two
  continuation-record laws are at total variation at least `1 − 2ε` (Bayes error at most `ε`
  under equal priors). Only the constant `ε_D` of C-ISO-2 depends on it.
- **Rd-2 (common continuation, Q1).** The continuation's labels are fixed or depend only on the
  continuation's own records. Under the other reading, in exchange mode every round record
  contains its label (section 1.2), so a continuation that copies the prefix labels separates any
  number of preparations with distinct labels, and Q1's upper half fails for every interface in
  that mode. C-ISO-2 depends on this reading. Its round records carry no label, and under the
  other reading the labels after a visit can depend on the prefix records, so Step C's statement
  that "the rest depends only on `R_J`" does not hold (section 2.5).
- **Rd-4 is also used by C-ISO-2.** Its argument applies the conditional-error requirement to
  Q1's heralded preparations, which section 1.2 imposes on Q1, Q5 and Q6 (section 2.5).
- **Rd-3 (Q5's "within ε").** The two-class coarse-graining of the read is compared through its
  effects: `|Tr(E_{a1} σ) − Tr(P_a σ)| ≤ ε` for every state `σ`. No post-measurement update is
  required; the text names the measurement by its effects `{P_a, 1 − P_a}`, and sharpness is a
  property of effects. C-NULL depends on this reading. In the C-NULL instance the only state
  tested is `𝟙/2`, so the effects `P_a, P_b` are themselves components of `𝔔` that no record
  fixes. Rd-3 is therefore an instance of RC-1, not a separate issue.
- **Rd-4 (conditional error).** The conditional error of a heralded preparation is the total
  variation between the world's and `𝔔`'s laws of the complete record conditional on the herald,
  for every protocol of `Π_K` that extends the prefix. `2 d_K / p_acc ≤ ε` is a sufficient
  condition for it (section 1.2, "which holds when"). C-NULL depends on this reading. C-ISO-2
  uses only the requirement that admissible heralded preparations meet conditional error `ε`,
  which holds under this reading and under the sufficient-condition reading alike.
- **Rd-5 (preparation prefixes, Q6).** Every prefix of a protocol of `Π_K`, of any length from 0
  to `K`, is a preparation prefix; C-POS-2's row uses "a menu prefix of horizon at most `K`".
  C-NULL depends on this reading; C-REBIT does not.
- **Rd-6 (D3 in control rows).** A D3 entry includes D3's robustness requirement. C-PROG and
  C-PROG-P depend on this reading.
- **Rd-7 (C-CARD (a)).** "Q3 and Q6 fail together" is read as "Q3 and Q6 cannot both hold", as the
  other rows' "cannot hold together".
- **Rd-8 (C-ISO-1).** The row specifies no `μ`; the world is read as deterministic (a point law).

### 2.2 Control table

Status `red` means the obtained classification differs from the expected one in some clause
entry or in the token (section 2.1 of the proposal: clause entries of every row are compared
clause by clause).

| ID | Expected (proposal row, abbreviated) | Obtained | Status | Support |
|---|---|---|---|---|
| C-SUP-1 | Q0–Q6 at the stated `(ε, K)`; D6 fails; D1 fails; `OPERATIONAL-ONLY` | Q1–Q6 at the stated `(ε, K)`; Q0 in the form available (explicit finite size per `(ε, K)`); D6 fails (a); D1 fails; also D2, D7 fail; `OPERATIONAL-ONLY` | green | Main:582, :596, :598 [P]; L2-, L3-type steps [W] |
| C-SUP-2 | D1 fails; Q4 not applicable; supplied | D1 fails; Q4 not applicable; supplied | green | `endpoints.md`:67 [R]; `whole-model-bridge.md`:283–287 [R] (the quoted sentence is at :293) |
| C-POS-1 | Q1–Q6 at `ε = 0` on its protocol class; D3, D5, D6, D7 fail; `OPERATIONAL-ONLY` | as expected | green | `history-architecture-v5/REPORT.md`:9–68, :305–312 [R] |
| C-POS-2 | Q2, Q3, Q5, Q6 at `ε ≥ b + δ`; Q4 from L3; Q1 on its range; D as C-POS-1; `OPERATIONAL-ONLY` | as expected; Q4 at `4(b + δ)` [W, L3]; Q1 for `b + δ_1 ≤ ε < 0.05 − b`, for menus with an antipodal preparation pair read along its axis [W] | green | `finite-a2-v5/REPORT.md`:9–60, :100–120 [R] |
| C-ISO-1 | Q1 fails; D7 fails; not `PASS-DERIVED` | Q1 fails (either half, by the affine dichotomy); D7 fails | green | section 2.4 [W] |
| C-ISO-2 | Q1, Q2, Q3, Q5, Q6 cannot hold together at `ε < ε_D`; D7 fails; not `PASS-DERIVED` | Q1, Q2, Q3, Q5 cannot hold together at `ε < ε_D = 7 × 10^{-4}`, for every `K`, interface and `μ`; D7 fails | green | section 2.5 [W]; depends on Rd-2 and on section 1.2's conditional-error requirement for Q1 |
| C-FIN | Q2 with Q3 fails below `1/15`; D fails; not `PASS-DERIVED` | as expected, at the record's scope (fixed decoder) | green | `operational-quotient-v3/REPORT.md`:9–30, :212–228 [R] |
| C-REBIT | Q1–Q5 hold and Q6 fails; never `PASS-DERIVED` | Q1–Q6 hold, at every `ε` and `K`, for a qubit model with `d_K = 0` | **red** | section 2.3.1 [W] |
| C-TAB | Q2 only with `d = N`; Q1 and Q2 at `d = 2` fail for three pairwise distinguishable preparations | as expected | green | `whole-model-bridge.md`:167–178, :204–211 [R] |
| C-B1 | Q1 fails; D2, D7 fail | as expected | green | `whole-model-bridge.md`:132–197 [R]; `two-mode-drive.md`:22–32 [R] |
| C-REP | No Q-condition reads a representation; padding cannot move `d_K`; not `PASS-DERIVED` | padding cannot move `d_K` and not `PASS-DERIVED`, as expected; the clause fails: Q3, Q5 and Q6 can each be met through components of `𝔔` that no record fixes | **red** | `padData_rooted` (OB/OperationalSourcing.lean:476) [K]; sections 2.3.1–2.3.2 [W] |
| C-CARD | (a) `ε₀(L) > 0` below which Q3 and Q6 cannot both hold; (b) well-defined on `ℤ^3` except the level-set law; (c) verdicts indexed by `K` | (a) Q3 fails below `π / (2 q^{2|C|})`; (b) as expected; (c) as expected | green | section 2.6 [W]; Main:560 [P, P-imp]; Step 1 B.12 [R] |
| C-MEAS | one-read match under uniform `μ`, fails under `μ′`; D3, D4, D7 fail; Q2 fails on the two-read law | as expected | green | `measurement-source.md`:29–33, :57–63, :65–73, :85–127 [R] |
| C-NULL | Q2, Q3, Q5, Q6 cannot hold together below an explicit constant; not `PASS-DERIVED` | in exchange mode, Q2, Q3, Q5, Q6 hold together at every `ε` and `K` (readings Rd-3, Rd-4, Rd-5) | **red** | section 2.3.2 [W] |
| C-PROG | under 11(a): D3, D5, D6(a) met; D6(b) fails (`r_O`), encoder `parameter`; D2, D7 fail; `OPERATIONAL-ONLY` | as expected except D3: the robustness clause is not met (fair bits drawn directly from the environment); token unchanged | **red** | section 2.3.3 [W] |
| C-PROG-P | under 11(a), both modes: D3, D5, D6(a) met; encoder `content` and a hit (presentations 1, 2), `unclassified` (3); D2, D7 fail; `OPERATIONAL-ONLY` | as expected except D3, as for C-PROG; token unchanged | **red** | section 2.3.3 [W] |
| C-EXACT | C-POS-1 at `ε = 0`; C-ISO-2 fails at every `ε` below its constant | as expected | green | C-POS-1, C-ISO-2 rows |

**M1 outcome.** Five rows are red. By section 2.2 step 1 of the proposal the run is
`VOID(C-REBIT, C-NULL, C-REP, C-PROG, C-PROG-P)`, and by section 7 and method step M1 the step
stops here and returns to the owner with the definitions. The R-lin node (L5, M3), its child nodes
and the re-derivations of choice 9(a) were not started (section 4 below).

The reds have two separate causes.

- **RC-1 (C-REBIT, C-NULL, C-REP).** Q3, Q5 and Q6 are statements about the comparator `𝔔`,
  and Q2 constrains `𝔔` only through record laws. Components of `𝔔` that no record of `Π_K`
  tests can be chosen freely: parts of its states, and the action of its instruments and effects
  on states that are never reached. Each of the three conditions can then be met through that
  choice. Q6 in C-REBIT and C-NULL, Q5 in C-NULL (Rd-3) and Q3 in C-NULL (gates acting on `𝟙/2`)
  are met this way. In C-REBIT the free
  component is the imaginary part of a qubit state representing a real one (no edge effect, no
  reading needed beyond "real quantum theory" including preparations of its states). In C-NULL it
  is the state after the last round of a full-horizon prefix, heralded on a record whose
  probability does not depend on the state.
- **RC-2 (C-PROG, C-PROG-P).** Their D3 entry "met" does not survive D3's robustness clause under
  choice 6(i)(c): the compiled controller's fair bits are drawn directly from the environment, so
  under the non-uniform product law the bits are biased, and the record law that the rows take
  from the controller's source record is not stated. The tokens are unaffected. The proposal
  treats a mismatch between a row's expectation and a general rule differently in C-SUP-1. Its
  expected Q0 against section 2.1's "Q0 is not applied" is green with observation O-1, because the
  obtained entry states what holds (an explicit finite size) and no clause of that row comes out
  false. C-PROG's D3 entry "met" is false under D3 as written, so that row is red.

### 2.3 Derivations of the red rows

#### 2.3.1 C-REBIT

*Construction.* `T` is real quantum theory of one system: states are real density matrices on
`ℝ²` (Bloch vectors in the `x`–`z` disk); operations are instruments with real Kraus operators,
among them the rotations `e^{−iθσ_y/2}` (real matrices; `realTheory_rot` is its
configuration-level analogue [K]), real Lüders reads, and, for each state `s` of the disk, the
outcome-free preparation `σ ↦ Tr(σ) s`.

*Lemma W-R* [W]. Write a qubit density operator as `σ = A + iB` with `A` real symmetric and `B`
real antisymmetric. Let `𝔔_Y` have initial state any `ρ₀` with real part `ρ₀^T`, implement each
preparation of `s` as `σ ↦ Tr(σ) m_s` with `m_s` a pure state whose real part is `s` (Bloch vector
`(s_x, ±(1 − |s|²)^{1/2}, s_z)`), and implement every other operation by its real Kraus operators.
Then for every protocol the record laws of `T` and `𝔔_Y` are equal, so `d_K(T, 𝔔_Y) = 0` for
every `K`.

*Proof.* By induction on the record history, the unnormalized state of `𝔔_Y` has real part equal
to the state of `T`. For a real Kraus operator `K`, the weight `Tr(K^T K σ) = Tr(K^T K A)`, since
the trace of a symmetric matrix times an antisymmetric one is zero; `K σ K^T = K A K^T + i K B K^T`
has real part `K A K^T`; and `Tr(σ) m_s` has real part `Tr(A) s`. ∎

*Q-conditions for `𝔔_Y`.* Q2 holds with `d_K = 0`. Q3 holds exactly with `n̂ = y`. Q4 holds
exactly. Q5 holds with the real Lüders reads along `x` and `z` (`Tr(P_x P_z) = 1/2`). Q1: two
orthogonal real pure states are perfectly distinguished; no three are pairwise distinguished at
error `ε < 0.05` (Rd-1), because three Bloch vectors with pairwise `|r_i − r_j| ≥ 2 − 4ε` satisfy
`|r_i + r_j| ≤ 4√ε`, hence `|r_2 − r_3| ≤ 8√ε < 2 − 4ε` [W]. Q6: take the one-label prefixes
"prepare `s`" for every `s` in the open disk. Choose the sign of the `y`-component of `m_s` to be
`+` if `s_x` is rational and `−` otherwise. The two sets `{s : s_x ∈ ℚ}` and `{s : s_x ∉ ℚ}` are
each dense in the open disk. The map `s ↦ (s_x, ±(1 − |s|²)^{1/2}, s_z)` is a homeomorphism of the
open disk onto the open upper or lower hemisphere, so the states `m_s` are dense in each open
hemisphere, and hence in the sphere. Q6 holds at every `ε`.

*Obtained.* Q1–Q6 hold at every `(ε, K)`; the token is unchanged (not a lattice interface; never
`PASS-DERIVED`). The expected entry "Q6 fails" is not obtained: red.

*Dependence on readings.* None of Rd-1 to Rd-8 is needed for Q6; Rd-1 enters only Q1's constant.
If `T` is restricted to rotations about the disk normal and real Lüders reads from a fixed real
`ρ₀^T`, the interior states of the disk arise only as unheralded mixtures, the read post-states of
`𝔔` are pure in-plane states (the reads are repeatable in `T`), and the reachable states of any
matching `𝔔` are one circle of latitude (the rotation orbit of `ρ₀`), the in-plane great circle and
their mixtures; Q6 then fails and the row is green. The row's construction is "real quantum theory
of one system (state space a disk)", whose state space includes the interior of the disk; the
evaluation takes every state of that state space as preparable.

*Bearing on the criterion.* A family in `𝕀_D` whose record theory is real quantum theory with
preparations of mixed states would meet Q6 through `𝔔_Y` and be classed with Q6 rather than
`PARTIAL-REBIT`. The separation of Q3 from Q6 that C-REBIT is meant to exercise is therefore not
made by Q6 as stated.

#### 2.3.2 C-NULL (exchange mode)

*Instance* [W], at `q = 2` (choice 2). The rule is of second-order form and outside 𝓡, as the row
allows. `C` consists of `m` cells; `O = C`. Each cell `z ∈ C` has `F_z(x) = x_{w(z)}`, the current
value of one wire cell `w(z)`; the wires lie on `m` disjoint rings parallel to `e_1`, each of
length `n`, on which `F_j(x) = x_{j−e_1} + x_{j+e_1}`; no `F_j` reads a cell of `C` (so the exchange
writes into cells that no `F_j` reads); all other cells have `F = 0`. `μ` is the uniform law on
`Λ ∖ O`.

*Wire values are uniform and independent* [W]. On one ring, let `u(t, j)` be the current value at
position `j` and time `t`. The recursion `u(t+1, j) = u(t, j−1) + u(t, j+1) − u(t−1, j)` gives
`u(t, 0)` the coefficient 1 on `u(0, t)` (the only path of `t` steps from `0` to `t`), and `u(s, 0)`
for `s < t` does not involve `u(0, t)`. For `n ≥ 2T + 2`, the map from the initial data to
`(u(0,0), …, u(T, 0))` is therefore unitriangular in the variables `u(0, 0), …, u(0, T)` for every
value of the others, and the uniform initial law pushes forward to the uniform law on `V^{T+1}`.
Distinct rings are independent.

*Records.* At the start of round `j`, `C` holds `c_j` (both components). Tick by tick,
`C`'s current value is a wire value minus `C`'s previous value, so the round's history of `O` is a
bijective function of `c_j` and of `τ` fresh wire values per cell. Given the labels, the round
records are therefore independent across rounds, and round `j`'s record has the law `p_{c_j}`,
uniform on a set `S_{c_j}` of `2^{mτ}` records, each containing `c_j`.

*Model `𝔔`.* `ρ₀ = 𝟙/2`. Gate labels `c^{(k)}`, `k = 0, …, M − 1`, with
`𝓘_{c^{(k)},h} = p_{c^{(k)}}(h) · Ad(U_{2πk/M})` about a fixed axis `n̂`, and `c(θ)` the nearest
`c^{(k)}`; Q3 holds at `ε ≥ π/M`, since rotations about one axis by angles differing by `Δ` are at
diamond distance `2 |sin(Δ/2)| ≤ |Δ|`. Two read labels `c_a, c_b`, with `a ⊥ b` in the Bloch ball
(`Tr(P_a P_b) = 1/2`) and each `S_{c_a}` split into halves `a1, a0`:
`𝓘_{c_a,h}(σ) = Tr(Q_h σ) · 𝟙/2` with `Q_h = 2 p_{c_a}(h) P_a` for `h ∈ a1` and
`2 p_{c_a}(h) (𝟙 − P_a)` for `h ∈ a0` (so `Σ_h Q_h = 𝟙` and the coarse-grained effects are exactly
`P_a, 𝟙 − P_a`). One label `c*` with a set `R ⊂ S_{c*}` of `N` records, `N` at least the size of an
`ε`-net of pure states `{m_h}`: `𝓘_{c*,h}(σ) = p_{c*}(h) Tr(σ) |m_h⟩⟨m_h|` for `h ∈ R` and
`p_{c*}(h) σ` otherwise. Every other label: `𝓘_{c,h} = p_c(h) · id`. Resources: `2^{2m} ≥ M + 3`
and `N · 2^{−mτ} ≤ ε/K`.

*Checks.* On every record history that contains no record of `R` in a `c*` round, the state of
`𝔔` is `𝟙/2` at every round and every round's outcome law is `p_{c_j}`, as in the world. The
histories that contain one have probability at most `K · N · 2^{−mτ} ≤ ε` in both, so Q2 holds at
`ε` for every adaptive protocol. Q3 holds at `π/M ≤ ε`. Q5 holds exactly under Rd-3. Q6: for
`h ∈ R`, the full-horizon protocol whose last round is `c*`, heralded on `h_K = h`, has
`p_acc = 2^{−mτ} > 0` and `𝔔`-state `m_h`. In the world the earlier records are independent of
`h_K`; in `𝔔` the weight of `h_K = h` is `p_{c*}(h) Tr(σ)`, independent of the earlier records; so
the conditional laws of the complete record are the two unconditional laws of the first `K − 1`
rounds, at distance at most `ε`, and the conditional error is at most `ε` (Rd-4); no protocol of
`Π_K` extends the prefix. By Rd-5 these are preparation prefixes, and their states are `ε`-dense in
the pure states. So Q2, Q3, Q5 and Q6 hold together at every `ε` and `K`. (Q1 fails here; the row's
expectation does not include Q1.)

*Obtained.* In exchange mode, Q2, Q3, Q5, Q6 can hold together at every `ε`: red. The token
(not `PASS-DERIVED`) is unchanged (D7 fails; Q1 fails).

*Dependence on readings* [W, sketch]. Under each of the following readings this instance does
not refute the row. None of the three is proved green over every model `𝔔` and every C-NULL
interface; each is a sketch.
(i) Q6 restricted to prefixes followed by at least one round. A read pins `a·r = b·r = 0`, so the
admissible states of the instance's `𝔔` lie on one line and are not dense. A general proof needs a
Step-B-type bound (section 2.5) over every `𝔔`.
(ii) Conditional error read as `2 d_K / p_acc ≤ ε`. For the instance's `𝔔`, the mismatch on the
`R`-histories gives `d_K` of order `K · N · 2^{−mτ}`, while `p_acc = 2^{−mτ}`. So `2 d_K / p_acc` is
of order `N ≫ 1/ε`, and a herald with `p_acc ≥ 2 d_K / ε` averages over many outputs of `c*`. This
is argued for that `𝔔` only.
(iii) Q5 read as within `ε` of the Lüders instrument. Two consecutive reads along `a` agree with
probability near 1 in `𝔔`. In the instance's world they agree with probability `1/2`, a value that
depends on the equal halves `a1, a0`. The general case needs a Step-B-type bound on the class
probabilities.

*Initial-condition mode.* The instance does not carry over: without the exchange, consecutive
round records share the boundary configuration of `O` (the previous-value component of the first
tick), and a qubit model cannot carry that memory together with Q5's reads (argued, not proved).
The row was not examined further in this mode. The red is for exchange mode, and a re-run must
cover both modes (section 6, question 8).

#### 2.3.3 C-REP, C-PROG and C-PROG-P

*C-REP.* `padData_rooted` [K] states that padding a datum with an ancilla unitary leaves its rooted
family unchanged, so padding cannot move `d_K`; a construction whose only evidence is a
representation proves no Q-condition, so it is not `PASS-DERIVED`. The row's first clause, "No
Q-condition reads a representation", is not obtained. Taken literally it is false by design,
since Q2–Q6 are all statements about `𝔔`, a Hilbert-space model of the records chosen subject only
to Q2. Its intended sense also fails: that no condition is met through components of `𝔔` that the
records do not fix. Sections 2.3.1–2.3.2 exhibit record laws for which Q6 holds or fails according
to the choice of `𝔔`. In C-NULL's instance, Q5's effects and Q3's gates act only on the untested
state `𝟙/2`. C-NULL's row itself records that Q3 "is constrained by data only through the states
reached". Red, cause RC-1. The red derives from C-REBIT's and C-NULL's.

*C-PROG and C-PROG-P.* Under choice 11(a), every other entry of both rows is obtained as stated:
the specification states `r_O` as a configuration only (D6(a) met); `r_O` is defined as the
compilation of a controller whose specification uses sphere rotations and a hemisphere-law sampler
(finite-a2-v5) or quantum instrument data (Main:582), so D6(b) fails for C-PROG with every encoder
component `parameter` (indices of menu settings) and not a hit; in C-PROG-P presentations 1 and 2
every encoder component is `content` and a hit (each label is the compilation output, or is
supplied by a capacity statement whose proof is the compilation), and in presentation 3 the proof
of the cited capacity statement is not available, so every component is `unclassified` and the D6
row is not `proved`; D2 and D7 fail since `F_U ∉ 𝓡`; the token is `OPERATIONAL-ONLY`. The D3 entry
"met" is not obtained. Choice 6(i)(c) requires every law of the list, and D3's robustness clause
counts a result only if it is also stated under a second law of the list. The rows take Q0–Q6 from
the controller's source record, which assumes exactly fair bits, and draw those bits directly from
the environment. The non-uniform product law is on the list in its own right under choice
6(i)(c). Choice 6(iii) substitutes nothing under 6(i)(c): it enters the level-set row as "not
defined" in initial-condition mode and on `ℤ^3`. Under the non-uniform product law the bits are
biased, and no record states the controller's record law for biased bits. So the result is not
stated under a second law, and the robustness requirement is not met. This record does not claim
that the result fails under that law; that would need its own proof. A compiled controller that
first debiases its bits would remove this, for example by von Neumann extraction, which is exact
for an i.i.d. product law. The rows as written contain no such step. Red on the D3 clause, cause
RC-2. The token and the test of D6(b) are unaffected.

### 2.4 C-ISO-1 (green)

The world is deterministic (Rd-8) and linear over `ℝ`; a label writes a real configuration into
`C`. Fix a preparation family `P_t` whose last label is `c₀ + t δ`, `t ∈ ℝ`, and any common
continuation. By linearity the continuation's records are `h(t) = h(0) + t v`. If `v ≠ 0` for some
choice, the preparations `P_t` for distinct `t` are pairwise perfectly distinguished (records
differ deterministically), so Q1's upper half fails. If `v = 0` for every choice, labels do not
reach the continuation's records; heralds of a deterministic world have `p_acc ∈ {0, 1}`; so no two
admissible preparations are distinguished, and Q1's lower half fails. Either way Q1 fails [W]. D7
fails (E-real). The interference statistics are not a failure of the control
(`observation-context-protocol.md`:37–38 [R]). If a random `μ` were supplied, the `v ≠ 0` branch
still fails Q1 (translates of a law by `t v` separate as `|t| → ∞` for a compactly supported or
Gaussian `μ`), and the `v = 0` branch would need its own analysis; the row supplies none.

### 2.5 C-ISO-2 (green): the constant `ε_D`

The row's own sketch is not used as written: its step (iii) applies Q3 conditionally on one
complete prefix record, which needs the factor `1/p_acc`, and its Q6 branch is subject to RC-1. The
following argument [W] does not use Q6. It has no `p_acc` factor only because it applies the
requirement of section 1.2 that heralded preparations used in Q1 meet conditional error `ε`
against `𝔔` (Rd-4, or the sufficient condition `2 d_K / p_acc ≤ ε`). If Q1's heralded preparations
were not bound by that requirement, Step A would hold for them only at error `2 d_K / p_acc`. The
argument also depends on Rd-2 (Step C). C-ISO-2's round record is the position-or-blank sequence
of its ticks and carries no label, so `p(0)` and the record laws of every label live on one record
set. Notation: `L ≥ 2` (the walker
starts in `Λ ∖ O`, which is non-empty); an *A-record* is a prefix record whose last tick shows the
walker in `O`, a *B-record* one whose last tick is blank; `p(0)` is Q3's vector at `θ = 0`;
`b₀` is the all-blank round record and `γ = 1 − p(0)(b₀)`.

*Facts of the construction.* (W1) The whole state is the walker's position, which is read whenever
it lies in `O`; a label acts only on a walker in `C ⊆ O`, which the preceding tick has read; after
a B-record every label acts as the identity. (W2) Laziness: from `x ∈ O`, the first tick of the
next round shows `y_c(x)` (`g_c(x)` if `x ∈ C`, else `x`) with probability at least `1/2`; from any
other starting point a given site receives at most `1/6`. (W3) At time zero the walker is outside
`O`.

*Step A (A-mass).* Let `P` be an admissible preparation of length `ℓ ≤ K − 1` (unheralded, or
heralded at conditional error `ε`), with prefix records `r`, world weights `w_r`, and world and
`𝔔` laws `L_r`, `L′_r` of the next round under `c(0)`. From the conditional error,
`Σ_r w_r TV(L_r, L′_r) ≤ 2ε` (pointwise `|wL − w′L′| ≥ w|L − L′| − |w − w′| L′`). By Q3,
`TV(L′_r, p(0)) ≤ ε/2` for every state. Hence `Σ_r w_r TV(L_r, p(0)) ≤ 2.5ε` (\*). For the empty
preparation, (\*) and (W3) give `TV(L_∅, p(0)) ≤ 2.5ε` with `L_∅` putting at most `1/6` on each site
of `O` at the first tick; by (W2) every A-record has `TV(L_r, L_∅) ≥ 1/3`, so
`TV(L_r, p(0)) ≥ 1/3 − 2.5ε`, and the A-mass of `P` is at most `2.5ε / (1/3 − 2.5ε) ≤ 10ε` for
`ε ≤ 1/30` (\*\*). By (W1), for any label `c` (also chosen adaptively),
`Σ_r w_r TV(L^c_r, p(0)) ≤ 2.5ε + 10ε = 12.5ε` (\*\*\*).

*Step B (`γ` is bounded below).* At round 1 every label acts as the identity (W3), so the read
`c_a` has world law within `2.5ε` of `p(0)` and `𝔔`-law within `ε` of the world (Q2), and its
class `a1` has `𝔔`-probability within `ε` of `Tr(P_a ρ₀)` (Rd-3). With `α = p(0)(a1)`,
`|Tr(P_a ρ₀) − α| ≤ 4.5ε`, and likewise for `b`. Since `b₀` lies in one class, `α` and `β` lie in
`[0, γ] ∪ [1 − γ, 1]`, so `|a·r₀|, |b·r₀| ≥ 1 − 2γ − 9ε` for the Bloch vector `r₀` of `ρ₀`. For unit
`a, b` with `|a·b| ≤ 1/2` (Q5) and `|r| ≤ 1`, `min(|a·r|, |b·r|) ≤ √3/2` (the sum `s a + t b` with
signs `s, t` has length at most `√3`). Hence `γ ≥ (1 − √3/2)/2 − 4.5ε ≥ 0.0624` for `ε ≤ 10^{-3}`.

*Step C (no two preparations are distinguished).* Let `P_1, P_2` be admissible preparations and
`κ` a common continuation of `m` rounds (Rd-2). A hybrid over rounds uses (\*\*\*), applied to the
admissible preparations "`P_i` followed by the first `j − 1` continuation rounds" (of length at
most `K − 1`, since `j ≤ m`). It gives `TV(R^i_s, Π_s) ≤ 12.5 s ε` for the records `R^i_s` of the
first `s` continuation rounds and the process `Π_s` that draws each round from `p(0)`. Two cases:
- `m ≤ J`: the continuation's records are `R^i_m`, so `TV(Q_1, Q_2) ≤ 25 m ε ≤ 25 J ε` directly.
- `m > J`: let `R_J` be the records of the first `J` rounds and `N` the event that they are all
  blank. Given `R_J ∉ N`, the law of the rest depends only on `R_J`. By W1 the last read position
  is the whole state, and by Rd-2 the labels depend only on continuation records. So
  `TV(Q_1, Q_2) ≤ TV(R^1_J, R^2_J) + max_i P_i(N) ≤ 25 J ε + max_i P_i(N)`.

In the second case the survival `u_j = P_i(first j rounds blank)` obeys
`u_j ≤ (1 − γ) u_{j−1} + 12.5ε`, so `P_i(N) ≤ (1 − γ)^J + 12.5ε/γ`. With `J = 40` and
`γ ≥ 0.0624`, `(1 − γ)^{40} ≤ 0.077` and `TV(Q_1, Q_2) ≤ 0.077 + 1000ε + 201ε`. Q1 needs
`TV ≥ 1 − 2ε` (Rd-1), which fails for `ε < 7 × 10^{-4}`.

*Obtained* (given Rd-2 and the conditional-error requirement on Q1's heralded preparations). For every `K`, interface, `O`, `C`, `τ` and `μ`, Q1, Q2, Q3 (at `θ = 0` only) and Q5
cannot hold together at `ε < ε_D = 7 × 10^{-4}`; a fortiori with Q6 added. D7 fails. Not
`PASS-DERIVED`. The properties used are W1, W2 and W3 (W3 is part of the construction's
definition of `μ`; the row lists W1 and W2).

### 2.6 The other green rows

- *C-SUP-1.* Main:598 (ii) gives, for the single realization `R` of the net at `(ε, K)`, a qubit
  model (initial state and net instruments) within `ε/2` of every `R`-protocol: Q2. The net is
  `δ`-dense in instruments, so it contains a channel within `δ` of `Ad U_θ` for every `θ` (Q3),
  projective measurements within `δ` (Q5) and preparations within `δ` of every pure state (Q6);
  Q1 from orthogonal preparations and the three-state bound of section 2.3.1; Q4 by L3. The
  realization is finite with an explicit size per `(ε, K)` (Main:598); section 2.1 of the proposal
  does not apply Q0 to a construction that is not a lattice interface, so Q0 is entered in that
  form (observation O-1, section 3). D6(a) fails: the specification holds instrument data and a
  density register (Main:566, :582). D1 fails: the generating rule takes the comparator's
  instruments (the net) as its argument. D2 and D7 also fail. `OPERATIONAL-ONLY`.
- *C-SUP-2.* A world, region or law chosen per `θ` makes the generating rule take the target as an
  argument (D1 fails); no single interface carries both `c(θ₁)` and `c(θ₂)`, so Q4 cannot be posed.
- *C-POS-1.* The record states that every single-qubit state and rotation is represented and that
  every finite adaptive rank-one projective record and outgoing state agree with the quantum
  reference (:9–20, :34–68); Q1–Q6 at `ε = 0` on that class. The record lists as supplied the
  cosine-hemisphere law (D3), the preparation cone and workspace isolation (D5), rotation
  primitives (D6(a)) and the continuum sphere (D7) (:305–312).
- *C-POS-2.* The record's bound `min(1, hκ + 2χ) = b` on complete records and outgoing state gives
  Q2 at `b`; the menu rotations are exact in `𝔔`, so Q3 holds at the menu gap and Q6 at `δ`; Q5
  holds for menus containing the two reads (a condition the row states); Q4 at `4(b + δ)` by L3.
  Q1's lower half holds at `ε ≥ b + δ_1`, where `δ_1` is the distance of the menu's closest
  antipodal preparation pair and read from an exact pair; its upper half holds for `ε + b < 0.05`
  (section 2.3.1, applied to `𝔔` at record distance `b`). The menu-dependence is the row's. D as C-POS-1.
- *C-FIN.* The record's floor (:212–228) is `7/15 ≤ ε + 1/3 + ε` for the fixed representation, the
  two allowed preparations and the target `R` followed by an `X` read; section 2.1 of the proposal
  takes a control's Q-conditions from its record at the scope it states. For a comparator not bound
  to the record's decoder the value `1/15` is not established by the record; with the model's
  finite label menu of `M` actions, Q3 fails below `π/(2M)` in any case (as in C-CARD (a))
  (observation O-2).
- *C-TAB, C-B1.* Lemma 2 of the bridge (:167–178) gives `d ≥ N` for `N` pairwise perfectly
  distinguished preparations, and the table on `ℂ^N` (:204–211) attains it; three such
  preparations fail Q1's upper half and Q2 at `d = 2`. B1's three-angle witness (:132–197) is such
  a triple; D2 fails (E-control) and D7 fails (E-pair, E-real) (`two-mode-drive.md`:22–32).
- *C-CARD.* (a) At fixed `L` the menu has at most `q^{2|C|}` labels; each label's instrument is
  within `ε` of `Ad U_θ` only on an arc of `θ` of length at most `2 arcsin ε` (two such rotations are
  within `2ε` of each other, and rotations about one axis by angles differing by `Δ` are at diamond
  distance `2 |sin(Δ/2)|`), so Q3 fails for `ε < sin(π / q^{2|C|})`, in particular for
  `ε < π/(2 q^{2|C|})` [W]; by Rd-7 Q3 and Q6 cannot both hold below that value. (b) On `ℤ^3` the
  product law exists, `O` is finite, records are finite and depend on a finite light cone; the
  level-set law is defined on `𝓛_fin` only [W]. (c) The finiteness audit's control (1), as Step 1
  records it (Step 1, table row at line 1077 of Step 1): a finite cyclic surrogate agrees through a
  pinned horizon and differs after it [R].
- *C-MEAS.* `p_1(θ) = F(cos²θ)` (:57–59); a match for every `θ` holds exactly when `F(t) = t`
  (:63). The record's competing symmetric law `6q(1 − q)` gives `F_B(1/4) = 5/32 ≠ 8/32` (:65–69),
  so the one-read match holds under the uniform law and fails under `μ′`, and D3 records the
  measure as supplied. Two reads: the deterministic port calibrations force the effects of any
  matching qubit read to be the projectors on two orthogonal pure states (orthogonal supports in
  `ℂ²`), and the two-use calibrations force the Lüders instrument (:94–114); at `θ = π/4` the native
  law gives `r_1 ≠ r_2` with probability `1/2` and the instrument gives `0` (:116–127), so Q2 fails
  [R, with the support argument W]. D4 fails (posited response function), D7 fails.
- *C-EXACT.* C-POS-1 is classified at `ε = 0` on its class with no slack; C-ISO-2 fails at every
  `ε < ε_D`, with `ε_D` explicit (section 2.5).

### 2.7 Proves-too-much check and two-way check of the encoder test

| Negative control | Properties its argument uses | C-POS-1 | C-POS-2 | Reversible rules, unread uniform environment (every member) | Applies? |
|---|---|---|---|---|---|
| C-ISO-1 | deterministic real-linear world; labels a real one-parameter family | fails (stochastic hidden sphere) | fails (finite carrier) | fails (a uniform law is on a finite alphabet) | no |
| C-ISO-2 | W1, W2, W3 | W1 fails (sphere point never read) | W1 fails (private workspace never read) | W1 fails (environment never read) | no |
| C-FIN | label actions form the 24-element Clifford group | fails | fails at menus with a non-Clifford rotation | fails for members with a non-Clifford operation | no |
| C-REBIT | (red; section 2.3.1) | — | — | — | not evaluated as a negative control |
| C-TAB, C-B1 | three pairwise perfectly distinguished preparations | fails | fails | fails for qubit-like members | no |
| C-CARD (a) | fixed `L`; conclusion an unspecified `ε₀(L)` | conclusion contradicts no stated classification | C-POS-2's floor is its own | taken at growing resources | no |
| C-MEAS | a read leaves the signal unchanged and draws a fresh seed | fails (re-preparation after a read) | fails (fresh index from `ν_(s a)`) | not true of every member | no |
| C-NULL | (red; section 2.3.2) | — | — | — | not evaluated as a negative control |

Two-way check (under choice 11(a)): C-PROG's encoder components are `parameter` and not a hit;
C-PROG-P's are `content` and a hit in presentations 1 and 2 and `unclassified` in presentation 3;
the property "the label encoder is a hit" does not hold for every member of the third case (for
example a member whose labels are indices of settings, as in C-NULL's instance with labels read as
`parameter`). Green.

***

## 3. Observations that do not change a status

- **O-1.** C-SUP-1's expected entry states Q0, while section 2.1 of the proposal does not apply Q0
  to a construction that is not a lattice interface; the obtained entry states the finite size.
- **O-2.** C-FIN's floor `1/15` holds at the record's scope (its decoder fixes the comparator).
- **O-3.** C-SUP-2 cites `whole-model-bridge.md`:283–287 for a sentence found at :293 at the pin.
- **O-4.** Rd-2: if a continuation's labels may depend on prefix records, Q1's upper half fails for
  every interface in exchange mode, because round records contain their labels. In C-ISO-2, whose records carry no label, that reading breaks Step C; C-ISO-2 depends on Rd-2.
- **O-5.** C-ISO-1 specifies no `μ`; its classification is obtained for the deterministic reading.

***

## 4. The R-lin node: not started

By the stop rule (proposal sections 3, 4 M1 and 7: "If any control is red, stop and return to the
owner"), no work after M1 was done in this session: L5 and M3 (the herald and record gap, the
joint-law route), the child nodes, the re-derivations of MECH-1 Lemma A and MECH-2 Lemma F
(choice 9(a)), M2's lemmas and the R-nl branch. No token other than `VOID` is computed, and no
`FAIL-CLASS`, `PASS` or `PARTIAL` statement is made for any subclass.

## 5. Pressure test of the red rows (§A.31)

- *C-REBIT.* The model `𝔔_Y` is a density operator and a family of CP instruments on `ℂ²` with
  outcome set the round records, fixed for all protocols (section 1.4); the proposal contains no
  clause that ties `𝔔`'s states to the record laws beyond Q2 (searched: "faithful", "minimal",
  "unique", "up to unitary", "tomograph"; no hit). The red depends only on mixed states of the
  disk being preparable, stated in section 2.3.1 with the restricted reading under which the row is
  green.
- *C-NULL.* The red rests on three readings (Rd-3, Rd-4, Rd-5), each the literal one, and on an
  instance whose independence claim is an exact unitriangularity argument. Under each of the
  three alternative readings the instance does not refute the row; that the row is then green is a sketch (section 2.3.2). The instance uses exchange mode
  only.
- *C-PROG, C-PROG-P.* The red rests on Rd-6 and on choice 6(i)(c); the token is unchanged, and the
  defect is in the D3 entry of the rows, not in D6(b), which the rows exercise.
- *Greens.* The favourable classification of C-ISO-2 rests on a new argument (section 2.5), not on
  the row's sketch; the row's sketch has the `1/p_acc` gap and a Q6 branch subject to RC-1.

## 6. What remains for sessions 2 and 3

Nothing in Step 2 proceeds before the owner decides on the definitions (section 7 of the
proposal). The decisions the reds raise, stated as questions:

1. **The comparator (RC-1).** Are Q3, Q5 and Q6 to be properties of the record laws, so that none
   can be met through components of `𝔔` that no record tests? Those components are the imaginary
   parts of the states in C-REBIT, and in C-NULL the effects and gates acting on the untested state
   `𝟙/2`. Options:
   - (a) restate Q3, Q5 and Q6 operationally, on record laws;
   - (b) require them to hold for every `𝔔` that meets Q2;
   - (c) keep them as stated, accepting C-REBIT's and C-NULL's classifications.
2. **Full-horizon prefixes (Rd-5).** Are states after a prefix of length `K`, which no record of
   `Π_K` tests, preparation prefixes for Q6? Options: (a) yes, as C-POS-2's row reads; (b) only
   prefixes followed by at least one round, or by two.
3. **Q5's comparison (Rd-3).** Effects only, or within `ε` of the Lüders instrument? Under question 1
   this is part of RC-1.
4. **Conditional error (Rd-4).** The conditional TV against `𝔔`, or the sufficient condition
   `2 d_K / p_acc ≤ ε`? C-NULL depends on the choice. So does C-ISO-2's freedom from a `1/p_acc`
   factor, through the requirement that Q1's heralded preparations meet conditional error `ε`.
5. **M0 statement.** The approval comment lacks the statement M0 requires ("A `PASS-DERIVED` would
   be a consistency-axis result (§A.23); it would move no correctness assessment."), as the
   independent review reports (section 1). It is to be supplied before any session that could
   render a pass.
6. **D3 in the compiled-controller rows (RC-2).** Does D3's robustness clause apply to controls
   whose Q-conditions are taken from records? If it does, options:
   - (a) enter D3 as not met in C-PROG and C-PROG-P;
   - (b) add to the compiled controller a debiasing step, such as von Neumann extraction, exact
     for an i.i.d. product law, so that the result is stated under the non-uniform product law.
7. **Row amendments.**
   - The C-ISO-2 row: is it amended to the session-1 argument (section 2.5), which drops Q6 and
     the conditional-error factor and states `ε_D = 7 × 10^{-4}`?
   - C-REBIT's proves-too-much text ("its conclusion is that Q6 fails below `1/2`") needs
     amendment, whatever is decided under question 1.
8. **C-NULL in initial-condition mode.** It was examined in exchange mode only. A re-run must cover
   both modes.
9. **Results an amendment must preserve (§A.29).** Any amended definition is to name in advance
   the results it preserves. These are the twelve green rows of section 2.2, in particular C-POS-1,
   C-POS-2 and C-ISO-2 with its constant. C-REBIT and C-NULL, with their intended
   classifications, are its new controls.
10. Readings Rd-1, Rd-2, Rd-7 and Rd-8, and observations O-1 to O-5, are offered for the same
    decision.

After an amended text is approved, M1 is re-run on it from the start; the derivations of sections
2.3–2.6 can be reused where the amendment leaves a row's definitions unchanged. The R-lin node
(L5/M3) with the re-derivation of MECH-1 Lemma A (and MECH-2 Lemma F if a `FAIL-CLASS` uses it),
then R-nl under H-nl, remain for the sessions after that, within the effort bound of choice 10.

## 7. Condition table (§A.44 schema)

| ID | Statement | Status | Layer | Source |
|---|---|---|---|---|
| W-R | Real quantum theory with preparations of every disk state has a qubit model with `d_K = 0` whose prepared states are dense in the pure states | proved | W | section 2.3.1 |
| W-N | The C-NULL instance in exchange mode meets Q2, Q3, Q5, Q6 at every `(ε, K)` under Rd-3, Rd-4, Rd-5 | proved | W | section 2.3.2 |
| W-I2 | C-ISO-2: Q1, Q2, Q3, Q5 cannot hold together at `ε < 7 × 10^{-4}`, given Rd-2 and the conditional-error requirement on Q1 | proved | W | section 2.5 |
| W-I1 | C-ISO-1: Q1 fails (deterministic reading) | proved | W | section 2.4 |
| W-C | C-CARD (a): Q3 fails at `ε < π/(2 q^{2|C|})` | proved | W | section 2.6 |
| L5 | Structure of R-lin record laws (proposal M3) | open | — | not started |

No row of this table is relied on by a verdict other than `VOID`.

***

## 8. Disclosure

- **Commands run in this session:** `git` (rev-parse, status, branch, fetch origin main,
  merge-base, ls-tree, show, diff, log, add, commit, push), `sha256sum`, `wc`, `ls`, `df`, `sed`,
  `grep`, `cut`, `fold`, `head`, `tail`, `cat`, `awk`, `sort`, `tr` (text handling of the record file only). No interpreter, script, probe, checker or Lean
  build was run. All arithmetic in sections 2.3–2.6 was done by hand. No GitHub comment was made;
  Issue #1236 and its comments were not read.
- **Read for this session, at the pin unless stated:** the proposal (whole); `papers/Main.md`:560,
  :566, :582, :596, :598, :726, and the diff of `papers/Main.md` and `papers/SM.md` from the pin to
  `origin/main`; `finite-a2-v5/REPORT.md`:1–60, :100–120; `history-architecture-v5/REPORT.md`:9–68,
  :295–320; `operational-quotient-v3/REPORT.md`:1–30, :180–240;
  `oi-qm-ext-1/whole-model-bridge.md`:132–211, :276–293; `oi-qm-ext-1/two-mode-drive.md`:22–32,
  :124–147; `oi-qm-ext-1/measurement-source.md`:25–35, :57–125, :141;
  `oi-qm-ext-1/endpoints.md`:64–69, :119–123; `verification/programmes/oi-qm/PROGRAMME.md`:216;
  `observation-context-protocol.md`:36–46; OB/OperationalSourcing.lean:462–482,
  OB/F2CoherenceControls.lean:300–320, OB/CubicIsotropy.lean:108–120; Step 1, line 1077 and the
  lines located by search for "finiteness audit". `.github/workflows/*.yml` were read for push
  triggers before pushing.
- **Not read:** MECH-1 and MECH-2 (the R-lin node was not started).

## 9. Review disposition

The independent review of `a387c0a8` (ACCEPT WITH CHANGES; held outside the repository) confirmed
`VOID` and the red classifications. Its findings F1–F9 were each checked by the writer and applied
in this revision:

- F1: C-REBIT's density step is replaced by the rational/irrational sign rule.
- F2: RC-1 is extended to Q3 and Q5.
- F3: C-ISO-2's dependence on the conditional-error requirement is recorded, Step C is split into
  its two cases, and the absence of labels from its records is stated.
- F4: C-ISO-2 is listed as depending on Rd-2.
- F5: the greens under C-NULL's alternative readings are tagged as sketches.
- F6: C-PROG's "fails under `μ′`" is withdrawn in favour of "not stated", the reading of 6(iii) is
  corrected, and the extractor option is added.
- F7: the C-SUP-1/C-PROG asymmetry is explained.
- F8: the missing M0 statement is recorded. The writer did not read the comment and relies on the
  review for its content.
- F9: the owner questions are completed.

No finding was rejected, and no status changed.

**Commands used in this revision:** `git` (rev-parse, status, add, commit, push), `cat`, `grep`,
`sed`, `cut`, `wc`, `sha256sum`. No interpreter was run. The review file was read in full.
