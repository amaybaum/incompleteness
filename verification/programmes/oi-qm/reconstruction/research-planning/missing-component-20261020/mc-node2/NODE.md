# Node 2: dense availability from measurement, and operational completion as a candidate

Research only, consistency axis (§A.23). No premise adopted, no limit-closure or completion rule adopted, no status
changed, nothing written to `main`. Operational completion is treated throughout as a candidate under test.

**Base.** Kernel and papers at `origin/main` = `df9e601ebe2a4e5af2a82f2d06ca2797c3a10f88`; every [AT] name below was
confirmed by `git grep` of its declaration there (Lean paths under `verification/lean-mathlib/OIBridge/`). Paper lines
(Main.md:n, GR.md:n) are at `df9e601e`. N1 = `../oa-node1/NODE.md`, MC1 = `../mc-node1/NODE.md` (with node 1b, §9),
both with their review outcomes, on `research/missing-component-20261020` @ `623426e9`. LG =
`f2-ledger-20261020/LEDGER.md`. XS = `x-screen-20261018/REPORT.md`, EXC = `x-screen-20261018/sources/EXCERPTS.md`, on
`research/x-screen-20261018` @ `76383997`. DIB = `verification/audits/operational/dense-instrument-bridge-audit.md`.

**Tags.** [AT] adopted kernel theorem; [W] written argument here; [EC] exact computation here (SymPy, two runs
byte-identical); [NUM] floating-point evidence (mpmath, 40 digits, two runs byte-identical), never evidence of
exactness; [UP] unsourced premise; [L] literature; [rec] recorded in the cited record, not re-derived.

**Productivity test (fixed before the node).** Gem iff the node yields a fact strictly stronger than "no OI principle
is known to supply (a) the continuum of measurement bases, (b) operational completion (a deterministic phase by
almost-surely terminating protocols or limits), (c) O-B", and either constrains the form such a principle must take or
exposes a hidden assumption.

***

## 1. The A2 question: does TU satisfy `KrausDense` and `DenseFiniteQM`?

### 1.1 The definitions, read exactly

- `ChanWithin ε Φ Ψ` (DiscreteCompletion.lean:39): ‖Φ X − Ψ X‖ ≤ ε‖X‖ for every X, matrices in the L2 operator norm
  (`open scoped Matrix.Norms.L2Operator`, :26). A uniform operator-norm bound on the difference of the two linear maps.
- `KrausDense T` (:52): for every level k + 1, every outcome count m and every `IsFiniteEndomorphicKrausInstrument F`
  with `F : Fin m → …` on `Fin 2 × Fin (k + 1)` (KrausSoundness.lean:112: a finite Kraus list with Σ KᴴK = 1 and an
  outcome labelling), and every ε > 0, there is G with `T.availExt (k + 1) (Fin m) G` and `ChanWithin ε (F a) (G a)` for
  **every outcome a**. The available family has exactly the outcome type `Fin m`; matching is outcome by outcome; the
  m = 1 case asks for a one-outcome (deterministic) family near each channel.
- `DenseFiniteQM T` (:59) = `KrausSoundExt T ∧ KrausDense T`; `KrausSoundExt` (CompositeSoundness.lean:123): every
  available family at every positive level is a Kraus family.
- `DenseUnitaryControl T` (D1, :45): every unitary U at every level is within ε of c • V in operator norm, V unitary
  with `conjChannel V` available as a one-outcome family.
- The kernel's route to the dense endpoint is `krausDense_of_denseControl : DerivedOI T → DenseUnitaryControl T →
  KrausDense T` (DenseInstrumentBridge.lean:437; `denseFiniteQM_of_denseControl` :496), instantiated for the fixed-gate
  theory (`fixedGateTheory_denseFiniteQM` :521). `DerivedOI` (RouteB.lean:141) contains `PhasesAvailable` (:128), the
  exact one-outcome quarter phase. Neither hypothesis holds for TU: D1 fails by MC1 §9.2 d1, and `PhasesAvailable` fails
  by MC1 T2 (a ray-moving unitary is never a one-outcome TU family). **The kernel route is closed for TU; the question
  needs a direct argument.**

### 1.2 The theory tested

`TU_B`: the `InstAvail` constructors (ImplementationLocality.lean:268) over the native class `permClass`
(SubstratumInterfaceAudit.lean:236: every permutation matrix of every carrier), with one added constructor: a sharp
Lüders test on a qubit factor of the carrier in a basis from a set B. Two choices of B:
- `B_cont`: the Y basis and every real basis w(φ) = (cos φ, sin φ), w⊥(φ) = (−sin φ, cos φ) (MC1's TU).
- `B_fin`: the X basis, the Y basis and the single real basis w(1) (angle one radian). Three non-configuration bases.

Ancillas are attached by the `discard` constructor with m = 2 (uniform), and |0⟩ is obtained inside it by
configuration readout and a conditional native X (MC1 T1 [W]).

### 1.3 Result

**Claim [W, with EC for every gadget identity and the generation step, NUM for an end-to-end instance].** For
B = `B_fin`, and hence for B = `B_cont`:
- `KrausSoundExt (TU_B)` and `KrausDense (TU_B)`, so `DenseFiniteQM (TU_B)`;
- `¬ DenseUnitaryControl (TU_B)`, `¬ PhasesAvailable (TU_B)`, hence `¬ DerivedOI (TU_B)`;
- `¬ ExactAllFiniteEndomorphicQuantumOps (TU_B)` (A1 fails).

**Proof.**
1. *Theory-hood and soundness [W].* That `TU_B` forms a `FiniteOperationalTheory (Fin 2)` (the fields of
   OperationalAssembly.lean:594 filled as in `genTheory`, ImplementationLocality.lean:855, with the added constructor)
   is a written argument. `KrausSoundExt` (CompositeSoundness.lean:123) is too: every constructor yields a finite Kraus
   family with Σ KᴴK = 1, the added test having complete projectors, along the kernel route
   `krausSoundExt_of_implementationGenerated` (ImplementationLocality.lean:963) through `cp_of_instAvail`, which is not
   re-run for the added constructor.
2. *Exact deterministic X-type flows [EC A1, A2a–A2e].* Prepare |+i⟩ (Y test, native X on outcome −i; A1a–c). Apply the
   ancilla-controlled transposition X_ab of two configurations a, b of the carrier (a permutation matrix, A2a). Test the
   ancilla in w(φ), and on w⊥ apply the native X_ab. Both branches are ∝ exp(iφ X_ab) = cos φ·I + i sin φ·X_ab (A2c,
   A2d; exact at d = 4 and 6 with φ symbolic). The one-outcome channel Ad exp(iφX_ab) is available exactly. It fixes the
   all-ones ray (A2e), as MC1 T2 requires.
3. *Heralded phase gadget [EC A3a–A4b].* Prepare |+i⟩, apply the data-controlled ancilla flip on a subset s of the
   carrier (a permutation, A2a), test the ancilla in w(φ). The branches are ∝ D_s(φ) = diag(1 off s, i e^{−2iφ} on s)
   and ∝ Z_s D_s(φ), Z_s = 1 − 2P_s, each with probability ½ (A3a, A3b). In the X basis (φ = π/4), D_s = I and the
   instrument is the heralded Z_s of MC1 §9.1(i) on any subset (A4).
4. *Phase channels to any accuracy [EC A5, A6].* Repeat-until-success for Z_s truncated at depth n is
   Φ_n = (1 − 2^{−n}) Ad Z_s + 2^{−n} id, and Φ_n X − Z_s X Z_s = 2^{−n}(X − Z_s X Z_s) (A5a); hence
   `ChanWithin (2^{1−n}) (Ad Z_s) Φ_n`, the constant attained (A5b). Correcting the Z_s D_s branch of step 3 by Φ_n gives
   the one-outcome family (1 − 2^{−n−1}) Ad D_s + 2^{−n−1} Ad(Z_s D_s) (A6a), within 2^{−n} of Ad D_s (A6b). It is a
   mixture of unitary conjugations, hence unital with ∞-norm 1 (A6c), so errors add under composition [W].
5. *Generation [EC A7, W4; W].* The Lie algebra generated by {iX_ab} alone has dimension (d − 1)² and commutes with the
   uniform projector (A7a; d = 2, 4, 6): the exact flows stay in the stabilizer of the all-ones ray. Adding the phase
   generators {iP_c} gives u(d) (A7b; d = 2, 4, 6). For every d, [P_a, X_ab] = E_ab − E_ba and
   X_ab − Σ_{c∉{a,b}} P_c = E_ab + E_ba (W4; d = 2, 3, 5, 7, all pairs), so i·diagonals, i(E_ab + E_ba) and
   E_ab − E_ba span u(d) on every carrier [W]. With `B_fin`, the steps exp(iX_ab) and D_c(1) (relative phase
   π/2 − 2) are irrational rotations (A8a, A8b), so their powers are dense in the one-parameter groups generated by
   iX_ab and iP_c, and the closure of the generated group is U(d) [W; standard]. Phases on every subset are not
   needed: {iX_ab} with the single generator iP₀ already generates u(d) at d = 2, 3, 4 (review `rev_exact2.py`, info
   rows).
6. *Channel-dense unitary control, then instruments [W; NUM].* For a target unitary U on any carrier, take a word
   within δ of U up to phase in the generated group; replace each phase letter by its step-4 approximant. The composite
   one-outcome family is within 2δ + L·2^{−n} of Ad U (`conj_within` DiscreteCompletion.lean:96 for the word,
   triangle inequality and unit ∞-norm for the letters). For an instrument F with Kraus list K and labelling `out`, run
   the Stinespring circuit of the kernel's assembly with this family in place of the exact unitary: attach a pure seed,
   apply the family, Lüders-read the seed register, coarse-grain along `out`, discard. Attach, the Lüders selector and the
   partial trace are bounded maps with carrier-only constants, so each outcome is within a carrier constant times the
   channel error. For the unitary case `branch_within` (DenseInstrumentBridge.lean:165) gives 2(r + 1)δ per branch for
   ‖U − V‖ ≤ δ. With a mixed-unitary approximant within ε of Ad U in place of conj V, each Kraus index is within
   (r + 1)ε (the partial trace), and coarse-graining adds a factor r + 1; errors add because unital positive maps have
   norm 1 [W, review account]. All steps are `InstAvail` constructors with outcome type `Fin m` after coarse-graining.

   End-to-end instance [NUM, `a2_num.py`]: a two-outcome target instrument on `Fin 2 × Fin 1` whose Kraus operators are
   non-monomial and whose Stinespring unitary moves the all-ones ray (T0–T2); an exact 40-letter word (6 exact X-letters,
   34 phase letters, T3). Per-outcome bounds ε_0, ε_1 fall as 2^{−n} with the RUS depth (1.1 at n = 1, 2.7·10^{−4} at
   n = 16, 9.7·10^{−19} at n = 64; T4, T6); every family built is trace-preserving in aggregate (T5). With `B_fin`, the
   error tracks the angle tolerance: 3.7·10^{−2}, 3.7·10^{−3}, 4.5·10^{−4} at δ = 10^{−2}, 10^{−3}, 10^{−4} (T8).
   Countercontrol: without the RUS correction the error stays 1.13 (T7). Only level one is exercised numerically. The review's
   independent instance (`rev_num2.py`, run once) is a three-outcome target on `Fin 2 × Fin 1` with a three-level
   Stinespring seed (carrier d = 6) and a 111-letter exact word; its per-outcome errors are 6.4·10^{−14},
   2.9·10^{−14} and 5.9·10^{−14} at n = 48.
7. *Failures.* D1 fails: every one-outcome unitary family of `TU_B` fixes the all-ones ray (MC1 T2, `instAvail_unitary_
   fixes_ones` InstrumentRealization.lean:398, transfer [W]), and (Z ⊗ I)u ⊥ u (A9), so ‖Z ⊗ I − cV‖ ≥ √2 at every level.
   `PhasesAvailable` fails for the same reason. A1 fails: QM implies `DerivedOI` (`derivedOI_pairFlowSourced_of_qm`
   PairFlowEquivalence.lean:93), which contains `PhasesAvailable`. ∎

### 1.4 The owner's questions on matching

- **Topology.** Uniform operator-norm closeness of each outcome map (`ChanWithin`), not trace distance of Choi states
  and not convergence of the coarse-grained channel alone.
- **Per outcome.** Each outcome a of the target is matched by outcome a of an available family with outcome type
  exactly `Fin m` (T4 reports both outcomes and the coarse-grained channel separately).
- **Heralded branches** count as outcomes of an available multi-outcome family. The target {½ Ad Z, ½ id} (m = 2) is
  available exactly (MC1 §9.1(i), b5). Inside the step-6 circuit the heralds of the RUS sub-protocols are coarse-grained
  away; the outcomes that remain are the seed readout.
- **Postselected branches**, renormalized and kept as one-outcome families, are not available families: `InstAvail`
  has no outcome-selection constructor (MC1 §9.1(i)), and a state-dependent renormalization is not linear, so it would
  violate `KrausSoundExt`. The construction uses none.
- **The m = 1 target Ad Z** is met only approximately (Φ_n, T9). That is the exact point where A1 fails and A2 holds.

### 1.5 What it means

- **The phase gap exists only at A1.** At the existing A2 endpoint TU has no phase gap: `KrausDense` holds although no
  ray-moving unitary is ever a one-outcome family.
- **The continuum of bases is also an A1 requirement only.** Three fixed non-configuration bases suffice for
  `DenseFiniteQM`. The countability obstruction (CR, N1 §2.1) does not bind at A2, consistently with the kernel's
  countable `fixedGateTheory` being dense (`fixedGateTheory_denseFiniteQM`, `fixedGateTheory_not_qm`
  DiscreteCompletion.lean:1948).
- **Consequence for O-A.** Relative to the native class, the missing component splits by endpoint:
  - at A2: one non-native primitive, finitely many non-configuration sharp test bases (it breaks `NonnegBounded`
    through its non-monomial Kraus branches), and nothing else on the operation side;
  - at A1: in addition, (a) an uncountable primitive family and (b) a deterministic ray-moving channel, i.e. a
    non-`OnesNormal` primitive or a completion rule (§2).
  Items (a) and (b) are exactly the A1 increment over A2. Which of them is a problem at all is fixed by the target
  decision (G8, EXC:170), not by the resources. For (a) this is already recorded ("A2: a countable X becomes
  admissible", EXC:82–83); the addition here is that (b) is A1-only as well.
- **G4's uniform-ray clause is A1-specific.** G4 (EXC:166) requires a candidate to break the uniform-ray invariant.
  `TU_fin` is dense (A2) while every one-outcome unitary family in it fixes the uniform ray (MC1 T2). Under A2 the
  uniform-ray clause is therefore not necessary; it is a requirement of the A1 endpoint and should be marked as such
  wherever G4 is applied. The `NonnegBounded` and reality clauses are broken by `TU_fin`'s gadget channels (A2c with
  φ = 1 is non-monomial and non-real).
- **Directional record (§A.34).** The kernel proves `DerivedOI ∧ DenseUnitaryControl → KrausDense`. The converse fails:
  `TU_B` satisfies `KrausDense ∧ KrausSoundExt` with neither `DerivedOI` nor `DenseUnitaryControl` [W]. D1 is
  sufficient for the dense endpoint, not necessary.
- **Not supplied.** The result is about a posited theory. It does not source the test bases (OI's readout is
  configuration readout, Main.md:632), it does not source the continuous choices of `B_cont`, and it says nothing on O-B,
  which is a cone condition. The A2 endpoint is defined on the `Fin 2` carrier family only (EXC:83) and is not the
  adopted target (A1, EXC:17).

### 1.6 Pressure test of the favourable reading

1. *Per-outcome, every level?* The quantifier ranges over all carriers `Fin 2 × Fin (k + 1)`, not only qubit registers.
   The gadgets act on any carrier with a qubit ancilla, and the generation step is proved for every d (W4); exact
   instances at d = 4, 6 (A2–A4) and d = 2, 4, 6 (A7).
2. *Hidden phase input?* No step uses a deterministic phase. The only phase-type operations are the heralded gadget
   branches and finite RUS truncations, each a finite `InstAvail` tree; every family built is `OnesNormal` (MC1 T2
   transfer), consistent with A6a being a mixture.
3. *Does the countercontrol bite?* Without RUS correction the error does not shrink (T7). With configuration ancillas
   or configuration tests the gadget yields only scalars or monomial branches (A10a, A10b). Native-only protocols keep
   `NonnegBounded` (`obsTheory_nonnegBounded` FrozenSourcing.lean:84), so the native theory is not dense.
4. *Irrationality as a knob.* Irrational angles are sufficient, not shown necessary; a Clifford+T-type pair of rational
   angles would likely serve as well [L-type remark, not checked]. Either way the basis set is a stated datum, like the
   fixed gate of `fixedGateTheory` (DIB outcome: "the fixed gate the sole remaining sourcing question and a stated
   datum").
5. *Floating-point.* The end-to-end numbers are [NUM] and are evidence for the approximation scheme, not a proof; the
   proof is steps 1–7, with the exact identities in [EC].

***

## 2. Operational completion as a candidate

### 2.1 The Kraus-word lemma [W; EC W1–W3]

*Statement.* Let A be a countable alphabet of primitive Kraus operators (up to scalars), including the ancilla
embeddings and co-embeddings (|j⟩ ⊗ · and ⟨j| ⊗ ·, with the constants of the uniform attachment), so that the Kraus
operators of a discarded family are again words. Suppose a completion rule makes
available only families each of whose outcomes is a countable sum Σ_ℓ conj(K_ℓ), every K_ℓ a scalar multiple of a
finite word over A. If such an outcome equals conj(V), then V ∝ K_ℓ for some ℓ (or V = 0). Hence the available
one-outcome conjugation channels lie in countably many rays, the `hmem` hypothesis of `countable_not_pairFlowSourced`
(PairFlowEquivalence.lean:218) holds with D the set of words, and the theory is not A1 QM (via
`derivedOI_pairFlowSourced_of_qm` :93).

*Proof.* The Choi matrix of conj(V) is |V⟩⟩⟨⟨V|, of rank at most one. It equals Σ_ℓ |K_ℓ⟩⟩⟨⟨K_ℓ|, a convergent sum of
positive terms, each below the sum; a positive operator below a rank-one projector's multiple lies in its span, so
|K_ℓ⟩⟩ ∝ |V⟩⟩. ∎ (W1: Choi(Ad Z) has rank 1; W2: Choi(Φ_n) has rank 2; W3: an operator not ∝ U fails the order bound,
exactly; review G7 checks the order step for arbitrary λ.) The argument covers non-unitary V, as `hmem` requires (N1
review). `hmem` is needed only at level one (`Fin 2 × Fin 1`), so only the level-one words enter D.

*Scope.* An almost-surely terminating protocol over A has exactly this form: its channel is the sum over terminating
leaves, each leaf a finite word; the non-terminating paths carry zero weight. The RUS leaves for Ad Z are each ∝ Z
(A11a, A11b).

### 2.2 The discriminating control

`fixedGateTheory_not_qm` (DiscreteCompletion.lean:1948) together with `fixedGateTheory_denseFiniteQM`
(DenseInstrumentBridge.lean:521) is the kernel's own A1/A2 separation on a countable theory, `MixR {α}` being countable
up to scalar and closed under products (`mixR_countable_upToScalar` StateMixingCoupling.lean:662). A completion rule
that makes `fixedGateTheory` exact QM erases that separation, which is what XS:33 and XS:164 call "the dense endpoint
relabelled". A rule that keeps it does not. **Control fixed for every completion candidate: `fixedGateTheory α` stays
non-QM.** The Kraus-word lemma gives one direction: every word-type rule keeps it [W]. The converse (every rule keeping
it is word-type) is not claimed.

### 2.3 The forms, checked

Countercontrols for (i): `permTheory_not_qm` (SubstratumInterfaceAudit.lean:716), `substratum_residual`
(StructuralClosure.lean:383), `NonnegBounded` for the native class, and the new control of §2.2. K_B, K(Z_F) and
Γ(Q3) are cone fixtures; no availability rule acts on them.

| form | (i) native classes | (ii) relabelling? | (iii) CR | supplies |
|---|---|---|---|---|
| F1 almost-sure termination: the channel of every protocol tree terminating with probability 1 | stay non-QM: unitary channels are words, hence monomial; countable sums of conjugations by monomial words preserve entrywise nonnegativity (A10c; closed cone [W]) | no: keeps `fixedGateTheory_not_qm` (lemma); on `TU_fin` gives exact Ad Z yet stays non-QM, while the topological closure of `TU_fin` is exact QM (§1) | preserved for unitary rays (lemma), although the set of infinite trees is uncountable | (b) only |
| F2 stopping-time rules (E[τ] < ∞, geometric tails, heralded success) | as F1 | as F1 | as F1 | (b) only; subclasses of F1 |
| F3 σ-convex closure (countable mixtures) | stay non-QM, `NonnegBounded` kept | no | preserved (words) | neither: a unitary channel is extremal |
| F4 postselection on a state-independent herald, renormalized | as F1 | no | preserved | (b); coincides with F1 when the branch is a fixed unitary |
| F5 general postselection | — | — | — | rejected: renormalization by a state-dependent probability is not linear; violates `KrausSoundExt` |
| F6 ω-closure: convergent infinite compositions (deterministic infinite circuits and infinite trees) | stay non-QM: products of permutation matrices converge only when eventually constant; mixtures keep nonnegativity [W] | **yes**: with D1 and the group property, every unitary is a convergent product W_1W_2⋯ with W_n → 1 (telescoping), so `fixedGateTheory` becomes QM through `DerivedOI` (`derivedOI_qm_iff_phaseFree` RouteB.lean:161) [W] | broken: infinite sequences are uncountable and yield every angle | (a) and (b) |
| F7 topological closure of availability in `ChanWithin` | stay non-QM: `NonnegBounded` is limit-closed (`preservesNonneg_of_approx` FrozenSourcing.lean:127; channel limits [W]) and the native theory is not dense | **yes, by definition**: the closure of T is exact QM iff `KrausDense T` (with soundness and closedness of the Kraus set) [W] | broken | (a) and (b) |
| F8 closure of the set of testable bases (orbit of B under available unitaries, closed) | native: only the configuration basis is testable; its orbit under permutations is finite and closed; unchanged | **yes**: in `fixedGateTheory` the orbit is dense, its closure is every basis, then MC1 T1 gives exact flows and `DerivedOI` the phases [W] | broken | (a); (b) with F1 or with exact phases |

**Dichotomy, for the forms F1–F8 only [W].** Word-type rules (F1–F4) supply at most (b), keep CR's countability of
unitary rays and keep the A1/A2 separation. The rules that supply (a) from countable primitives (F6–F8) admit
non-word limits, and each erases `fixedGateTheory_not_qm`: they are the dense endpoint relabelled. **No listed rule
supplies (a) and (b) together without being the relabelling.** Among these forms, a completion that covers both and
keeps §2.2's control needs an uncountable primitive family posited alongside it; (b) can then come from a word-type
rule or from a non-`OnesNormal` primitive. Rules outside F1–F8 are not covered, and §2.2's converse is not claimed.

### 2.4 Pressure test of the most favourable form: F1 with `TU_cont`

- *Does it reach A1?* Yes [W]: `TU_cont` gives every exp(iφX_ab) exactly (§1.3 step 2); F1 gives every D_s(φ) exactly
  (each terminating leaf of the corrected gadget applies D_s); these generate U(d) by finite products (the generated
  group contains the ray stabilizer and a non-stabilizer element, whose generated Lie algebra is u(d) by W4); exact
  Stinespring assembly then gives every instrument.
- *Is F1 the source of (a)?* No. The continuum is `TU_cont`'s; with `TU_fin` F1 stays non-QM (lemma). F1 contributes
  (b) only.
- *Can a fixed finite OI representative run F1?* No, and no fixed representative realizes any A1-exact continuum
  either [W; EC W5]. Total finiteness of S is a posit (Main.md:708 (ii)), φ has finite order (Main.md:123, :139), and a
  fixed realization with a finite-support prior (Main.md:60) has finitely many event probabilities. The RUS law needs
  P(not terminated by step n) = 2^{−n} for every n, infinitely many values (W5: 2^{−11} is not an event probability of
  a 2^{10}-state uniform realization). The same count excludes exact Born weights cos²φ at a continuum of angles φ, so
  it bars the continuum flows of (a) and A1 exactness in general, not repetition in particular; Main.md:538 records
  the fixed-carrier obstruction in that general form. OI's realization theorems are finite-horizon (Main.md:82 layers
  (1) and (3); Main.md:542), and OI escapes the fixed-carrier obstruction by carriers that grow with the experiment
  (MC1 HA-M7). Deep-sector enlargement (Main.md:708 (ii)) likewise gives an unbounded family of finite
  representatives. F1 therefore exceeds any fixed representative, as every A1-exact continuum does; no asymmetry
  between (a) and (b) is shown.
- *Bounded duration.* A protocol of bounded depth is a finite `InstAvail` tree, so with `OnesNormal` primitives it
  realizes no deterministic ray-moving unitary (MC1 T2). An exact deterministic phase operation of bounded duration
  therefore needs a non-`OnesNormal` primitive [W]. If laboratory phase gates are modelled as bounded-duration
  protocols over the primitive set, F1 cannot be their physical origin; F1 is then at most a mathematical closure.
- *Verdict.* Among F1–F8, F1 is the form that supplies (b) without being the relabelling. It supplies only (b), only
  through unbounded running time, and it exceeds any fixed finite representative, as every A1-exact continuum does.

***

## 3. OI sources for (a), (b), (c)

| candidate | location | would supply | posit / derivation | non-circular? | covers |
|---|---|---|---|---|---|
| C1, C4 readback | Main.md:74, :80; primitive :604 | diagnostics of the visible law | derivation-level diagnostics | yes | none: configuration-diagonal (MC1 row 7 [rec]) |
| C2 record persistence | Main.md:76 | records persist to readback: classical feed-forward (`bind`) across steps | physical-regime premise | yes | none of (a)–(c); it supports the heralds' feed-forward that §1 uses |
| C3 capacity | Main.md:78 | many fresh ancillas and records: RUS depth n up to the capacity | posit (realization clause, 10^{122}) | yes | (b) to accuracy 2^{−n} only, an A2-type approximant; never (a) |
| recurrence, total finiteness, deep-sector enlargement | Main.md:123, :139, :708 (ii) | bounded protocols in each representative; an unbounded family of representatives | posits (ii), Axiom 2 | yes | against any A1-exact continuum in a fixed representative, unbounded repetition included (§2.4); OI's growing carriers and deep-sector enlargement give unbounded families of finite representatives |
| unavoidable predictive memory | Main.md:582 | classical memory bounds | theorem | yes | none (MC1 row 11 [rec]) |
| open purification lift; CDP purification | Main.md:600–602 | existence of a purifier; in the uniqueness form [L: Chiribella–D'Ariano–Perinotti 2011] transitivity of reversibles on pure states, which would give (a), (b) and a self-dual cone toward (c) | the uniqueness half is a posit; Main.md:602 states it is strictly stronger than what is derived, and fiber freedom shows completions are not unique | no: uniqueness asserts the availability of reversibles relating purifications (O-A restated); classical theory has no purification, so it presupposes coherent states; substratum-sourced purifier reversibles are countable (N1 HA8) | (a), (b), (c) only as a posit; screened (XS op-fork [rec]) |
| time reversal; global antiunitary orientation | Main.md:56 (bijectivity); GR.md:188–190 | inverses (dagger-stability); one ℤ₂ | derivation (inverses), conditional result (orientation) | yes | none: complex conjugation fixes real vectors, so antiunitary compositions with ones-fixing unitaries fix the all-ones ray [W]; discrete |
| GR orientation transport | GR.md:190 | a passive oriented state | open question | yes | none for (a), (b); O-B only as TH, class (iii) (MC1 row 26 [rec]) |
| phase intervention; layer flow | GR.md:260, :266–272 | (b) and (a) as stated assumptions | posits | excluded as sources (E0) | (b), (a) by fiat |
| native Lüders update; test–preparation symmetry ("every outcome state of an available test is deterministically preparable") | Main.md:632; MC1 B4, B7 | the native update gives heralded preparation; the symmetry would give deterministic |−⟩, a non-`OnesNormal` primitive, hence Z by kickback | posit | partly: it presupposes the test set; with the full complex test set and validity (X-5) it fixes K = PSD, which is PS-type saturation, rejected by G2 (EXC:164) | (b); (a) only by converting an assumed test continuum into a preparation continuum; (c) only in the rejected saturated form |

**Single principle for (a) and (b).** From §2.3: among the forms F1–F8, no completion rule over countable primitives
supplies both without erasing `fixedGateTheory_not_qm`. The candidates that cover both in one statement (CDP purification uniqueness; the
test–preparation symmetry over a full test set; F6–F8) either posit an uncountable family of available operations or
tests, or are the relabelling. None is derived from OI's posits.

**Link to (c) [W; consistent with LG §3].** Given A1 operations (full control), the pair theorem
(`pairCone_eq_Q3_iff_drive_maxCone` EqvK2MaxCone.lean:174) reduces O-B to X-4 (available operations preserve K) and X-5
(test validity) with G3: hH2 and hA are instances of X-4, and hH1 follows from X-4 and one product state. No completion
rule acts on states, so none supplies X-4; defining states as the reachable set would, and G2 rejects it (EXC:164). The
link from (a)+(b) to (c) passes only through a barred definition.

***

## 4. Controls fixed in advance for surviving candidates (§A.29)

Candidates: **K0** `TU_fin` at A2 (meaningful only under a separate target decision, G8); **K1** `TU_cont` with F1;
**K2** `TU_cont` with the test–preparation symmetry. Each must:
1. keep `permTheory_not_qm`, `substratum_residual` and `obsTheory_nonnegBounded` when its addition is removed;
2. keep `fixedGateTheory_not_qm` (§2.2); K1 and K2 keep it (word lemma; K2 adds no limit), K0 adds no rule;
3. keep the rooted law (`finiteRootedRealizable_iff_pper` RootedClassificationAllTime.lean:192) and M1 on retained
   protocols: the additions add protocols and change no native one;
4. must-fail: finite protocols over `OnesNormal` primitives give no deterministic ray-moving channel (MC1 T2);
   preparations alone give no coherent control (LG §3);
5. name the CR premise given up: K1 and K2 give up P2 through `TU_cont`; like every A1-exact continuum, K1 exceeds any
   fixed finite representative (§2.4); K0 gives up neither countability premise, and is excluded at A1 by CR;
6. respect the fixed-carrier obstruction (Main.md:538);
7. leave K_B, K(Z_F) and Γ(Q3) to the G3 identification and the multi-token clauses: none of K0–K2 claims O-B.

**Independent prediction (G6): OPEN.** The only consequences found are retrodictions or internal: K1 predicts
unbounded running-time tails for every deterministic ray-moving operation built from `OnesNormal` primitives (§2.4); K2
predicts deterministic preparability of every testable state, which laboratory practice already shows. A G6 prediction
would have to be a preregistered consequence of the candidate outside the resource it supplies; none is proposed.

***

## 5. Hidden-assumption watch

| # | assumption | where | finding |
|---|---|---|---|
| HA-N1 | the A1/A2 choice is a target decision independent of the missing resources | EXC:82–91 | continuum half CONFIRMING (EXC:82–83 already records that A2 admits a countable X); **exposed** half: (b) is A1-only too, since with `TU_fin` the deterministic phase is not needed at A2 (§1.5). Corollary: G4's uniform-ray clause (EXC:166) is A1-specific |
| HA-N2 | the A2 route goes through dense unitary control | DIB; `krausDense_of_denseControl` | **exposed**: `KrausDense` holds for `TU_B` without D1 and without `DerivedOI` (§1.3); D1 is sufficient, not necessary |
| HA-N3 | "limit closure" names one notion | XS:33, :164; MC1 §9.3 | CONFIRMING: MC1 §9.3 already separates RUS-closure from the dense endpoint "in kind". Added here: `fixedGateTheory_not_qm` as the discriminating control, and the word lemma for one direction (§2.2) |
| HA-N4 | an embedded observer can run unboundedly long protocols | MC1 §9.6 | in a fixed finite representative, protocols are bounded and event probabilities finitely many (§2.4). This bars every A1-exact continuum alike, not repetition in particular; OI's carriers grow per experiment (MC1 HA-M7). Unbounded repetition exceeds any fixed representative, as every A1-exact continuum does |
| HA-N5 | one principle might explain (a), (b), (c) together | owner framing | **constrained, for the forms F1–F8 only**: among them, a completion covering (a) and (b) without being the relabelling needs a posited uncountable primitive; the link to (c) passes through X-4, which only a barred definition supplies (§3) |
| HA-N6 | the Choi-rank argument needs leaf-wise word decompositions | §2.1 | holds for a.s.-terminating trees by definition; fails for infinite deterministic compositions (F6), which is where countability breaks |

Assumption-watch markers:
- **AW-MC2-1.** The deterministic-phase gap of TU is an A1 phenomenon: at A2 (`KrausDense`) it vanishes, with three
  fixed non-configuration bases. Records citing the phase gap should say "at A1".
- **AW-MC2-2.** `KrausDense` does not imply `DenseUnitaryControl`, nor `DerivedOI` (witness `TU_B`, [W]).
- **AW-MC2-3.** A completion rule is tested against `fixedGateTheory_not_qm`. Word-type rules keep it and supply at most
  the phase; rules supplying the continuum from countable primitives erase it.
- **AW-MC2-4.** Almost-sure termination exceeds any fixed finite OI representative, as every A1-exact continuum does.
  It is not singled out by finiteness relative to (a).
- **AW-MC2-5.** G4's uniform-ray clause (EXC:166) is necessary only at A1: `TU_fin` is dense while all its one-outcome
  unitaries fix the uniform ray.

***

## 6. Files (`probe/`)

| file | role |
|---|---|
| `a2_exact.py`, `a2_exact.run1.out`, `.run2.out` | blocks A1–A11, 40 checks, exact (SymPy 1.14.0, Python 3.13.16, `-I -B`); 40 PASS |
| `a2_num.py`, `a2_num.run1.out`, `.run2.out` | T0–T9, end-to-end per-outcome `KrausDense` instance, modes CONT and FIN, countercontrol [NUM]; 10 PASS |
| `word_lemma.py`, `word_lemma.run1.out`, `.run2.out` | W1–W5: Choi ranks, the exact order-bound failure, the u(d) identities, the finite value count; 6 PASS |
| `review/rev_exact2.py`, `review/rev_exact2.out` | independent review, exact: gadgets at d = 3, Lie dimensions d = 2–6, single-phase-generator rows, spanning identities d = 2–7, order step; 11 PASS, run once |
| `review/rev_num2.py`, `review/rev_num2.out` | independent review [NUM]: three-outcome target with carrier d = 6, FIN mode at d = 2; run once |

Each `.run2.out` is byte-identical to its `.run1.out`. Digests are in `probe/SHA256SUMS`; the review files are copied
unchanged with their own `probe/review/SHA256SUMS`.

***

## 7. Not verified

- The `KrausDense` claim is [W]. Not formalized; the `TU_B` theory has no kernel definition; the added test constructor,
  its soundness and the transfer of `instAvail_onesNormal` are written arguments (as in MC1 T2).
- The channel-approximant version of the Stinespring assembly is written, not compiled; its constants are taken to
  match `branch_within` and are not re-derived.
- The density of the generated group is the standard one-parameter-subgroup argument [W]; exact Lie dimensions are
  computed for d = 2, 4, 6 only, the spanning identities for d = 2, 3, 5, 7.
- The end-to-end instance is one target instrument at level one, in floating point.
- The relabelling verdicts for F6 and F8 rest on written telescoping and orbit-closure arguments; the topological
  closure statement for F7 is definitional and not formalized. The dichotomy is shown for the listed forms only.
- The finite-horizon count (§2.4) is [W]; it applies to every A1-exact continuum alike and does not examine
  extensions with an infinite deep sector.
- Only level-one targets are exercised numerically (here d = 4; review d = 6).
- The CDP purification row is [L] and [rec]; the purification consequences in CDP's framework were not re-derived.
- Rational-angle sufficiency (Clifford+T-type) for `B_fin` is not checked.

***

## 8. Productivity verdict

**Gem: yes.** Facts strictly stronger than "no OI principle is known to supply (a)–(c)":
1. With the native class, three fixed non-configuration sharp test bases give `DenseFiniteQM` outcome by outcome,
   while D1, `PhasesAvailable`, `DerivedOI` and A1 fail. Both (a) and (b) are therefore exactly the A1 increment over
   A2 (constrains the form; exposes HA-N2 and the (b) half of HA-N1; the (a) half is recorded at EXC:82–83).
2. Word-type completion rules, almost-sure termination included, keep countability of unitary rays and the kernel's
   A1/A2 separation on `fixedGateTheory`, so they supply at most (b). The listed rules that supply (a) from countable
   primitives erase that separation and are the dense endpoint relabelled. Among the forms F1–F8, a completion
   covering (a) and (b) without being the relabelling needs a posited uncountable primitive (constrains the form;
   HA-N3 confirming, HA-N5 scoped).
3. Almost-sure termination exceeds any fixed finite OI representative, as every A1-exact continuum does; a
   bounded-duration deterministic phase needs a non-`OnesNormal` primitive (constrains the form).
4. G4's uniform-ray clause is necessary only at A1 (§1.5).

No OI posit supplies (a), (b) or (c); operational completion stays a candidate, not adopted; G6 stays OPEN.

**Classification (as corrected by the independent review): NEW (narrow, [W])** for `KrausDense ∧ KrausSoundExt`
without `DenseUnitaryControl` or `DerivedOI`, the converse of the kernel's sufficiency route failing (item 1, with the
G4 remark of item 4). **ELABORATING** for the word lemma and the F1–F8 table (item 2) and for item 3 and §3.
**CONFIRMING** for HA-N1's continuum half and for HA-N3.

***

## Independent review outcome

Review: `probe/review/` (`rev_exact2.py`, 11 PASS, and `rev_num2.py`, each run once, with their outputs and
`SHA256SUMS`, copied unchanged from the reviewer's working copy). The corrections below are applied in place. The
pre-review text is not kept here; its sha256 is `a1af6c05680318eda89d3d542acd82997c25ab2ff7fd02564c60661b0df08654`.

| item | verdict | applied as |
|---|---|---|
| (1) A2 for `TU_fin` | CONFIRMED as [W] | only level one exercised numerically; the review's three-outcome d = 6 instance gives 6·10^{−14} per outcome at n = 48 (§1.3 step 6); theory-hood and soundness marked [W] (step 1); the review's account of the `branch_within` constants added (step 6); one phase generator iP₀ suffices at d = 2–4 (step 5) |
| (2) heralded branches as outcomes | CONFIRMED | — |
| (3) Kraus-word lemma | CONFIRMED; dichotomy for the listed forms only | alphabet names ancilla embeddings and co-embeddings; `hmem` needed at level one only (§2.1); dichotomy, §3 and HA-N5 scoped to F1–F8 |
| (4) finite horizon | CORRECTED | the finite-value count bars every A1-exact continuum (exact Born weights cos²φ included), not repetition in particular; §2.4, HA-N4, AW-MC2-4, §4 item 5 and §8 item 3 restated |
| (5) no OI source for (a), (b), (c) | CONFIRMED as recorded | — |
| G4 | NEW remark (missed) | the uniform-ray clause of G4 is A1-specific (§1.5, AW-MC2-5, §8 item 4) |
| HA-N1, HA-N3 | RECLASSIFIED | HA-N1: continuum half CONFIRMING (EXC:82–83), only "(b) is A1-only" new; HA-N3 CONFIRMING (MC1 §9.3) |

**Final classification: NEW (narrow, [W])** for "`KrausDense ∧ KrausSoundExt` without `DenseUnitaryControl` or
`DerivedOI`". ELABORATING for the word lemma and the F1–F8 table; CONFIRMING for HA-N1's continuum half and HA-N3.
