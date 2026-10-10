# Thread C — observation/update source audit (read-only)

Base: `wt-threads` at `4507b025` (landed main, PR #775). K0's audit was at `fdebc6e3`. All paths below are relative to
`wt-threads`; `OIB/` = `verification/lean-mathlib/OIBridge/`. ✓ = the cited lines were opened and read in this thread.
Scripts and outputs: `threads/C/update_controls.py` (`.out`), `threads/C/hexagon_probe.py` (`.out`),
`threads/C/span_check.out`. All arithmetic is exact (Fractions or sympy rationals); there is no floating point anywhere.

**Vocabulary used here.** `e` is a sharp test effect with certain face `F_e = {ω ∈ Ω : e(ω) = 1}`. A branch `T` is a
linear map on the state cone that is positive and satisfies `u∘T = e`. Each branch property below has a short name.
- **SI** (state-independent): `T ω = e(ω)·ω₀` for one fixed `ω₀`. The weak form **SI_cert** asks this only for
  `ω ∈ F_e`. That is the brief's "independent of the incoming state within that outcome".
- **Ideal**: `T ω = ω` for every `ω ∈ F_e`, so a state already certain for the outcome is not disturbed.
- **Repeatable**: `e∘T = e`.
- **SF**: `F_e` is a subsingleton (Thread A's corrected form, for proper effects).

## 1. Finding

The question was whether the corpus, before matrix QM is assumed, says that a certain sharp outcome leaves a
post-observation state independent of the incoming state. **Nothing in it says so in a form that bears on (SF).**
- **The update the corpus uses is Bayesian conditioning on a visible outcome**, followed by marginalizing over the
  hidden sector (`Main.md:630` ✓; `HiddenMemory.post`, `OIB/HiddenMemory.lean:69` ✓). Conditioning is ideal: a
  state already certain for the outcome passes through unchanged.
- **The corpus's own pre-matrix results go against state-independence for visible sharp tests.**
  - C4 (`Main.md:80` ✓) says two histories with the same current visible value can induce different next-step laws.
  - The worked computation (`Main.md:194` ✓) gives `P(x₂=0|x₁=1,x₀=0)=1` against `1/3` without conditioning on `x₀`.
  - The pushforward identity (`OIB/HiddenMemory.lean:83` ✓) makes the post-observation prediction a function of the
    incoming hidden law.
  - So two incoming states that are both certain for `X₁=1` keep different post-states, with total variation 1
    between their next-step laws (exact control C1).
  - These all concern a test that is coarse on `V×H`, and that a later visible readout can refine. They do not
    contradict (SF) for atomic tests, which matches K∞ §14(d).
- **Every statement found that does assert a state-independent post-state is one of three kinds:**
  - matrix-level: `ludersLift`/`cp_rankOneSelector_iff_luders`, `recordInstr`, the pure-seed reset;
  - stipulated prose: the book's card-table "re-burn", `ch01-observation.md:269,280` ✓;
  - imported and approximate: Barandes division events, kept out of the kernel by `T₀ = {0}`.
  
  Each of these achieves state-independence by **re-preparing** the state (measure-and-prepare), not by an ideal
  update.
- **The exact controls show why state-independence cannot source (SF).**
  - In the square gbit, the atomic edge test has a valid, repeatable, state-independent measure-and-prepare branch.
  - The square gbit has **no** ideal branch for that test.
  - The GPT analogue of the corpus's selector capstone (positivity plus a classical rank-one selector) forces the
    state-independent, non-ideal branch there, just as it forces Lüders on `M_n(ℂ)`.
- **(SF)-as-update is therefore a relocation.** What it needs is ideality together with state-independence; given
  repeatability and ideality, state-independence is equivalent to (SF). Neither ideality nor state-independence is
  sourced pre-matrix.

## 2. Evidence level

**Per-claim evidence.**
- U1, the logic linking Ideal, SI and SF: written proof, in §4.
- Square gbit A1–A3, trit B1–B3, disk B4 and hexagon: exact computation, in `update_controls.out`,
  `hexagon_probe.out` and `span_check.out`.
- C4 and the card table, C1–C3: exact computation, which reproduces `Main.md:194` and the `ch01:273-278` table.
- The source classifications: read and spot-checked, in the table below.
- Barandes division events: literature, as quoted in the corpus's own act-01 and act-08 records. The external PDF
  was not re-read here.

**Principle-by-principle table.** The layer column uses four labels:
- **pre-M**: pre-matrix;
- **M**: complex-matrix level (recorded, but **sources nothing pre-quantum**);
- **imp**: imported;
- **prose**: book or essay register.

The verdict is one of: *silent*; *SI stated*; *contradicts SI* (the statement rules out a state-independent update);
*non-selecting*.

| # | principle / source | layer | verdict | strongest citation | note |
| --- | --- | --- | --- | --- | --- |
| 1 | Substratum dynamics: bijection, record preservation | pre-M | **contradicts SI on the total ontic state** | `Main.md:56` ✓ (Lemma 3); `Main.md:62` ✓ ("merging them would erase a distinction") | SI on a subsystem is possible only by exporting the incoming state into the complement, as re-burn does. It is not possible as a global update |
| 2 | Measure selection (max-ent "compatible with the observer's records") | pre-M | silent | `Main.md:56, 60` ✓; posit ledger `Main.md:706` (iv) ✓ | A prior selection, not an update rule. Read as an update it conditions on *all* records, so it depends on the history |
| 3 | The corpus's update rule: conditioning on a visible outcome | pre-M | **contradicts SI within a coarse outcome**; ideal | `Main.md:630` ✓; `HiddenMemory.post` `OIB/HiddenMemory.lean:69` ✓ | SI holds only on a maximal *ontic* outcome, a simplex vertex. That is the same triviality as SF-M in K∞ §14(a) |
| 4 | C4 history readback; hidden-memory theorem | pre-M | **contradicts SI** for visible sharp tests | `Main.md:80` ✓; `Main.md:194` ✓; `Main.md:580-590` ✓; `pushforward_identity` `OIB/HiddenMemory.lean:83` ✓; `unavoidable_hidden_predictive_memory` `:185` ✓ | Exact control C1 gives TV = 1. The visible test is coarse on `V×H` and refinable by a later readout, so it is not a counterexample to SF for atomic tests |
| 5 | C2 record persistence; fast-bath erasure | pre-M | **in tension with history-erasing updates** | `Main.md:76` ✓; `Structure.md:114` ✓; `Main.md:159-161` ✓ | An update that erased hidden records at every observation would remove C4's gap. Exact control C2 shows this for one step |
| 6 | C1, C3 | pre-M | silent | `Main.md:74, 78` ✓ | |
| 7 | Observation axiom (Level A), record writing in prose | pre-M | silent | `Structure.md:108, 118` ✓ | "records distinguishable outcomes"; nothing about the post-state |
| 8 | Itinerary classes; passive quotient | pre-M | non-selecting | `itiRelK`/`itiRelInf` `OIB/ObservabilityQuotient.lean:79, 83` ✓; `hiddenExt_not_separating` `OIB/PassiveQuotient.lean:534` ✓; `quotient_itinerarySeparating` `:222` ✓; `itiRelInf_iff_orderOf` `OIB/ObservabilityQuotient.lean:304` | On the raw carrier the complete-history outcome is certain on a non-singleton class, so conditioning is state-dependent. On the quotient it picks out a point, but that is a simplex vertex, reached by a multi-time record that may need a horizon up to `orderOf φ` |
| 9 | Stochastic observer interface | pre-M | silent | `readWriteFamily_exists` `OIB/StochasticInterface.lean:156` ✓ (no readout privileged); `ensemble_underdetermined` `:118` ✓ | No readout is selected, so there is no update rule |
| 10 | Deterministic-realization class (response table, ε-realization) | pre-M | **non-selecting** | `Main.md:576` ✓ ("realizes arbitrary finite stochastic behavior, quantum or not"); `Main.md:558` ✓ | It realizes any finite update statistics, including gbit-like ones. It can reproduce a given update; it does not choose one |
| 11 | Native ancilla readout `id_A ⊗ ℒ_k` | M | contradicts SI on the system; SI on the register | `readout_is_localLuders` `OIB/OperationalAssembly.lean:658` ✓; `localLuders` `:191` ✓ | A certain outcome fixes the ancilla index and leaves A's block untouched, as K∞ §9 already noted |
| 12 | Rank-one selector ⇒ Lüders | M | **SI stated (derived from CP)** | `ludersLift` `OIB/BranchSelector.lean:64` ✓; `RankOneSelector` `:80` ✓; `cp_rankOneSelector_iff_luders` `:172` ✓ | Non-sourcing, because it imports the PSD cone. Its GPT analogue in the square gbit forces a state-independent but **non-ideal** branch (A3) |
| 13 | Coarse selector freedom (F35) | M | contradicts SI within rank > 1 | `OIB/BranchSelector.lean:43-47` ✓ | In a block of rank 2 or more, classical data does not fix the update |
| 14 | Recorder ("measure A, write the register") | M | **SI stated**, non-ideal | `recordInstr_apply` `OIB/InternalObserver.lean:252` ✓ (output `∝ E_{(a,a),(a,a)}` for every input); `recordInstr_not_passive` `:290` ✓ | Shows inside the corpus that SI ⇏ SF: the certain face for outcome `a` is large on `A×A`, yet the post-state is fixed |
| 15 | Passive and internal observation | M | contradicts SI within record blocks | `passive_branch_scalar` `OIB/PassiveObservation.lean:215` ✓; `central_classification` `OIB/CentralObservation.lean:433` ✓; `internal_branch_eq_blockPart` `OIB/InternalObserver.lean:137` ✓; `no_complete_internal_observer` `:206` ✓ | The ideal (passive) readouts are `P_o ρ P_o`, which depends on the state within a block |
| 16 | Pure-seed reset | M | SI stated, via control | `pureSeedPrep_available_of_swap` `OIB/OperationalAssembly.lean:675` ✓ | Readout plus a swap correction resets the ancilla, and needs swap control |
| 17 | Embedded observation | M | inherits row 11 | `OIB/EmbeddedObservation.lean:31, 160-175` ✓ | Consumes `localLuders` |
| 18 | Emergent channel `ρ_H = I/m` | M | SI-like if iterated (a hidden re-burn every step) | `Main.md:276-280` ✓; scope limited to one step: "the scope is the matrix, not the process" `Main.md:270` ✓ | Multi-time behaviour comes in through the dilation with a structured prior, not by iterating this channel |
| 19 | Lüders as a "transcription" of Bayes | M (emergent) | SI only on the visible marginal | `Main.md:630` ✓ | "Re-marginalizing over the hidden sector" can be read in two ways: tracing out (state-dependent hidden posterior) or a hidden reset (re-burn). The same paragraph calls agreement on multi-time statistics *supported by* chaotic-mixing suppression, which is open per posit (v) `Main.md:706` ✓, and treats residual pre-division memory as a falsifiable deviation |
| 20 | Barandes division events | imp | SI on the configuration simplex, approximate | `OIB/BarandesTuple.lean:17, 33-37, 387-396` ✓ (`T₀ = {0}`, not adopted); `verification/programmes/oi-qm/track-b/act-01-indivisibility/result.md:157-162, 468-470` ✓ ("generically always approximate"); `.../act-08-continuous-extension/layer-1-checkpoint.md:264` ✓ (derived from an environment interaction) | Re-preparation by the environment, a measure-and-prepare mechanism. The kernel does not carry it |
| 21 | Card table: "revelation is an intervention … burned and replaced under a fixed rule" | prose | **SI stated (stipulated)**, non-ideal | `book/ch01-observation.md:269` ✓, `:278-282` ✓, `:290` ✓; `book/glossary.md:35` ✓ | The only explicit pre-matrix SI statement found. It is stipulated, not derived. A passive peek gives 1, not 1/2 (C3), so the "1/2" row needs the re-burn |
| 22 | Measurement problem, epistemic reading | prose | silent | `Substratum.md:412-414` ✓; `Explainer.md:572-574` ✓ | "Collapse" is the observer's ledger. Nothing about the form of the update |

**No statement of a state-independent post-state for a maximal or atomic test was found at any pre-matrix level.**
The search terms were: collapse, post-measurement/observation, Lüders, posterior, Bayes, repeatab-, ideal
measurement, first kind, non-disturb-, state-independent, re-marginaliz-, division, re-burn, peek. They were run
over `papers/*.md` and `OIB/*.lean`. In the kernel: no `Certain`, `Ideal`, `Repeatable` or post-state predicate
exists, and the only measure-and-prepare hit is a comment, `OIB/Separability.lean:17`. In the papers: the only
repeatability hit is the imported quantum instrument in the ε-realization certificate, `Main.md:558`.

## 3. Countermodels and controls

All of the following are in `update_controls.py`, and every assertion passes.

**A — square gbit, the brief's mandated control.** The state space is `|x|,|y| ≤ t`, the test is
`e = (t+x)/2`, and `F_e` is the edge `{(1,1,±1)}`.
- `e` and `u−e` each vanish on rays spanning a plane (rank 2), so `(e, u−e)` is an **atomic** binary test.
- **A1: no ideal branch exists.** Fourier–Motzkin elimination finds the system infeasible. By hand: the branch kills
  `(1,−1,0)`, which forces `T(1,−1,1) = (0,0,1) ∉ C`.
- **A2: the branch `T = v₁eᵀ`, `v₁ = (1,1,1)`, is valid and SI.** It is positive, normalized and repeatable, and it
  disturbs the certain state `(1,1,−1)`.
- **A3: a selector query.** This is the GPT analogue of `cp_rankOneSelector_iff_luders`: impose `T v₁ = v₁` and
  `T v₂ = 0` on the frame `{(1,1,1),(1,−1,−1)}`. The feasible set is the single point `T = v₁eᵀ`. So positivity plus
  a classical selector forces an SI, **non-ideal** branch in a theory where SF fails.

**B — positive controls and countercontrols**, run through the same query code so that A1's infeasibility is not an
artifact of the method.
- **B1: trit, coarse `e = δ₀+δ₁`.** An ideal branch exists, and it is not SI, so ideality alone does not give SF.
- **B2: trit, fine `e = δ₀`.** The ideal branch is unique and SI.
- **B3: trit, coarse selector.** The selector query returns a non-unique feasible set, so A3's uniqueness is a real
  result rather than something the method always reports.
- **B4: disk.** `F_e` is the single point `(1,1,0)` (exact solve), and `e(·)(1,1,0)` is ideal and SI.

**Hexagon side probe** (`hexagon_probe.py`, using a rational affine frame of the regular hexagon). For the atomic edge
test, `dim(span F_e ∩ span F_{u−e}) = 1`, and no ideal branch exists. The square gives the same dimension, 1; the
coarse trit gives 0 (`span_check.out`).

**C — the corpus's own update rule.**
- **C1: coin-and-die, `Main.md:178-196`.** Roots `x₀ = 0` and `x₀ = 1` give different post-states after the certain
  outcome `X₁=1`, with next-step laws `δ₀` and `δ₁` (TV = 1). This reproduces `Main.md:194` exactly, including
  `1/3` without the root.
- **C2: re-burn update.** The post-states coincide and the history gap at that step is killed. Re-burn is not ideal:
  `δ_(1,3)` changes. Conditioning is ideal.
- **C3: card table.** The values are 1/2, 1, 1/2 and 1/2, matching `ch01:273-278`, for re-burn with either a uniform
  or a fixed replacement card. A passive peek gives **1**, so the text's "1/2" peek row depends on the stipulated
  re-burn.

**Skepticism applied to the favourable branches.**
1. "Conditioning is ideal and the substratum is classical, so SF holds at the ontic level." True, but non-selecting.
   It is the simplex-vertex fact, which every classical theory satisfies and no test of a non-classical body depends
   on.
2. "The book states an SI update pre-matrix." True, but stipulated, in the essay register, and non-ideal, and A2
   shows non-ideal SI exists in the square gbit, so it cannot source SF.
3. "BranchSelector derives SI from a classical selector." This is a matrix-level derivation, and A3 shows that its
   GPT analogue yields SI without SF.
4. "Ideality alone excludes the square gbit and the hexagon (A1, hexagon)." This is the favourable reading most in
   need of pressure. Ideality is **also unsourced** pre-matrix. B1 shows it does not imply SF for coarse tests. Whether
   it implies SF for *atomic* tests is untested on the torus and Stiefel orbitopes (§4 Q1).

## 4. Proposed next theorem

- **U1 (written now; Lean candidate, field-neutral, elementary).** Let `Ω` be convex, let `e` be an effect with
  `F_e ≠ ∅`, and let `T` be a branch.
  - (a) Ideal ∧ SI_cert ⇒ `F_e = {ω₀}`. Proof: `ω = Tω = ω₀` for every `ω ∈ F_e`.
  - (b) Repeatable ∧ SF ⇒ SI on `{e > 0}`. Proof: `Tω/e(ω) ∈ F_e = {ω₀}`.
  - (c) Hence, under Ideal ∧ Repeatable, SI_cert ⇔ SF.

  Layer: Lean, in the corrected KInfFoundations vocabulary of Thread A.
- **U2 (exact; Lean candidate as a finite decidable certificate).** For the square gbit and `e = (t+x)/2`:
  - (a) the branch `v₁eᵀ` is positive, normalized, repeatable, SI and not ideal;
  - (b) no ideal branch exists;
  - (c) positivity together with `T v₁ = v₁` and `T v₂ = 0` forces `T = v₁eᵀ`.

  Corollary: SI ⇏ SF, and the selector-to-SI mechanism of `cp_rankOneSelector_iff_luders` carries no ideality.
  Layer: exact, with Lean as a candidate.
- **U3 (written).** If `e` admits an ideal branch, then `span F_e ∩ span F_{u−e} = {0}`. Proof: `T` is the identity
  on `span F_e`, and `T` vanishes on `span F_{u−e}` by normalization, positivity and pointedness. Corollary: atomic
  edge tests of even polygons have no ideal branch (square and hexagon checked exactly). Layer: written, with Lean
  as a candidate.
- **U4 (exact; Lean candidate on `HiddenMemory.Realization`).** In the coin-and-die realization there are two
  incoming states, both certain for `X₁ = 1`, whose conditioned next-step laws are at TV distance 1. This makes the
  failure of SI_cert for visible tests a kernel fact. It is scoped to coarse tests on `V×H`, not to atomic tests.
- **Q1 (open; next exact probe, not a theorem).** Does "every atomic sharp test admits an ideal branch" imply SF?
  Run U3 and an exact ideal-branch query on the torus and Stiefel orbitopes (K∞ §11). If either has atomic tests with
  non-singleton faces *and* ideal branches, ideality is not a route to SF. If not, ideality + SI is the sharpest
  candidate form of "SF ← measurement update", and it is still a premise, not a derivation.

## 5. Dependencies

- **On Thread A.** U1 and U3 need a field-neutral state space and effect objects, and Thread A's corrected "proper
  effect" / "subsingleton certain face" definitions. No such object exists in the kernel; this is K0 row 8.
- **On Thread D.** D's route (3), "repeatable nondemolition tests on maximal frames", is directly constrained by A1
  and U3: the square gbit and the hexagon have no ideal branch for their atomic tests. Q1 overlaps D's
  torus/Stiefel checks. No result here assumes D's.
- **Corpus declarations used.**
  - `OIB/HiddenMemory.lean:54, 69, 83, 185`
  - `OIB/BranchSelector.lean:64, 80, 172`
  - `OIB/InternalObserver.lean:137, 252, 290`
  - `OIB/OperationalAssembly.lean:191, 658, 675`
  - `OIB/PassiveQuotient.lean:222, 534`
  - `OIB/ObservabilityQuotient.lean:79, 83`
  - `OIB/StochasticInterface.lean:118, 156`
  - `OIB/BarandesTuple.lean:387-396`
- **Unsourced premises that any SF-as-update route would add.**
  - Ideality of the emergent sharp tests.
  - State-independence of their post-states.
  - Equivalently, given repeatability and ideality: SF itself (U1(c)).
  - Also open: the chaotic-mixing suppression that `Main.md:630` invokes for vanishing pre-division memory, posit (v)
    at `Main.md:706`. It is in tension with C2/C4 via `Main.md:159-161`.
