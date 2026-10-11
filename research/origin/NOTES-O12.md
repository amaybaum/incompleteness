# NOTES-O12 — the angle condition of `denseUnitaryControl_of_fixedGate` at level one

Thread `research/origin`, round 4, node O12. Base L = `9f9f8257`; kernel paths under
`verification/lean-mathlib/OIBridge/` at L. Evidence levels as in NOTES-O1 ([K] kernel at L, [D] design module, [X]
exact computation, [W] written argument, [L] literature). Script: `experiments/o12_angle.py`. Design module:
`lean/OriginAngle.lean` (dev branch `dev-origin/angle`, cut from L).

Kernel objects. `StateMixingCoupling.rot θ` = [[cos θ, −sin θ], [sin θ, cos θ]] (StateMixingCoupling.lean:45);
`DenseUnitaryControl` (DiscreteCompletion.lean:45) and its level-one clause (the case n = 1 of that definition);
`FixedGateSourced` (:34); `denseUnitaryControl_of_fixedGate` (:1522), whose angle hypothesis is `Irrational (α / π)`;
`levelOne_dense` (:762); `blockRepertoire_levelOne` (:736); the level-one group `Gen2` (:1548); the Pauli set `Pauli`
(:1603, sixteen matrices); `Gen2.pauli_conj` (:1734); `gen2_multiple_finite_upToScalar` (:1834); the canonical
theory `fixedGateTheory α = mixTheoryR {α} (Fin 2)` (:1926) with `fixedGateTheory_derivedOI` (:1929) and
`fixedGateTheory_fixedGateSourced` (:1933); the class `MixR` (StateMixingCoupling.lean:56; inventory I4.175);
`instAvail_mono` (ImplementationLocality.lean:305); the echo identity (DiscreteCompletion.lean:844).

"`rot α` is a Clifford element" is read as the kernel-native predicate `RotClifford α`: conjugation by `rot α`
carries every element of `Pauli` into `Pauli` (by `pauli_conj_of_XZ`, :1666, it suffices to test X and Z).

**Productivity test, fixed before starting (§A.31).** A finding counts only if it is strictly stronger than O9-E (the
level-one clause fails at π/4 and holds at π/8) and either (i) decides, for every rational angle, whether the
level-one clause holds, with each step labelled by evidence layer, or (ii) states the weakened hypothesis as a
design-module statement whose two controls — the countermodel `fixedGateTheory (π/4)` and the positive instance π/8 —
are decided inside the module, together with a reduction of the general level-one statement to inputs named in the
module. A restatement of O9-E at two angles is a non-gem.

**The suspected hidden assumption, recorded before any computation.** The kernel's hypothesis `Irrational (α / π)`
enters its proof only through `dense_angles` (:518): powers of one exact rotation about the y-axis by an irrational
angle are dense among those rotations, and `BlockRepertoire` (:562) needs that exact rotation. Reading the hypothesis
as the obstruction ("dense control fails because α/π is rational") assumes that this route is the only route to
density. Suspected instead: at level one the obstruction is the Clifford property of `rot α`, and a rational
non-Clifford angle gives density by a different route (an infinite-order word whose closure meets every axis), with no
exact irrational y-rotation available at all. A second assumption to watch: that a level-one weakening carries to
every level by the kernel's route. The echo (:844) isolates `rot (2α)` on one block, which at α = π/8 is `rot (π/4)`,
itself a Clifford element; so the kernel's all-level route does not run at π/8 whatever holds at level one.

## S0 — predictions, written before the first run of `o12_angle.py` and before any dispatch (2026-10-11T04:21:02Z)

Exact script (`o12_angle.py`; arithmetic in ℤ[ζ_N][1/2] with N = lcm(2q, 4), elements as integer coordinates in the
power basis over a power of two; equality and integrality are exact):

- **A1 (the predicate on a grid).** Over every reduced angle α = πp/q with q ≤ 36 and 0 ≤ p < 2q (792 angles),
  conjugation by `rot α` carries X and Z into the sixteen-element Pauli set exactly at the 8 angles kπ/4.
- **A2 (finite at the Clifford angles).** The level-one group ⟨rot α, S, X⟩ (S = diag(1, i)), taken modulo scalars
  (a class is the pair (G X G†, G Z G†)), closes with 8 classes at α ∈ {0, π/2, π, 3π/2} and with 24 at
  α ∈ {π/4, 3π/4, 5π/4, 7π/4} (the 24 is O9-L1d's channel count).
- **A3 (infinite at the other rational angles).** At each of the 784 non-Clifford grid angles the word
  W(α) = rot α · rx α (rx α = S rot α S†, `rx_eq_conj` :333) has det 1 and trace 2cos²α = 1 + cos 2α, and this trace
  is not an algebraic integer — by two independent methods: (a) its coordinates in the power basis of ℤ[ζ_N] are not
  all integers; (b) sympy's minimal polynomial of cos 2α, in primitive integer form, has leading coefficient > 1. At
  the 8 Clifford angles both methods report an algebraic integer (t ∈ {0, 1, 2}).
- **A4 (closure input).** At every non-Clifford grid angle sin 2α ≠ 0.
- **A5 (the π/8 certificate in the module's form).** With p₀ = 0, p₁ = 1, p_{k+1} = (1 + √2/2)p_k − p_{k−1} and the
  integer pairs (x₁, y₁) = (1, 0), (x₂, y₂) = (1, 1), x_{k+1} = x_k + 2y_k − 2x_{k−1}, y_{k+1} = x_k + y_k − 2y_{k−1}:
  √2^{k−1} p_k = x_k + y_k √2 and x_k is odd for 1 ≤ k ≤ 400 (exact in ℚ(√2)); W(π/8)^k = p_k W − p_{k−1} 1 and
  W(π/8)^k is not a scalar for 1 ≤ k ≤ 96 (exact in ℚ(ζ₁₆)).
- **A6 (the reductions).** rot(kπ/4) = rot(π/4)^k for k = 0, …, 7; X rot(π/4) X = rot(−π/4); rot(π/8)² = rot(π/4);
  at level two the echo product of `mixImage 2 (π/8)` isolates rot(π/4) on the chosen block (4 × 4, exact).
- **Positive controls (expected True).** PC1 the trace test fires at π/8 (t = 1 + √2/2); PC2 the group at π/4 closes
  with 24 classes; PC3 the test reports (3 + √5)/4 = 2cos²(π/5) not integral.
- **Countercontrols (each expected False).** CC1 the trace test fires at a Clifford angle; CC2 the trace test reports
  the algebraic integer 2cos(2π/5) = (√5 − 1)/2 not integral; CC3 the group closes within 3000 classes at π/8, π/3,
  π/6, π/5 or 3π/8; CC4 the Pauli test accepts rot(π/8) or rot(π/6); CC5 the recurrence p_k avoids zero up to k = 50
  at the finite-order traces t = 1 or t = √2 (zeros at k = 3 and k = 4 expected); CC6 rot(π/8) lies in the group
  generated by rot(π/4) and X (sixteen matrices).

Decision rule (fixed in the script's header before run 1): `VERDICT O12-CLIFFORD-ANGLES-EXACTLY` if A1–A6 hold, the
two methods of A3 agree at every grid angle, PC1–PC3 are True and CC1–CC6 are False; `VOID` if any countercontrol is
True or any positive control False; `UNDECIDED` otherwise.

Design module (`OriginAngle.lean`, one dispatch, 2/3 of the round):

- **D1.** The build succeeds and every `#print axioms` line shows [propext, Classical.choice, Quot.sound], no
  `sorryAx`; the release gate is red only on `lean-manuscript` (the new module has no census disposition).
- **D2 (the predicate).** `rotClifford_iff : RotClifford α ↔ ∃ k : ℤ, α = k * (π / 4)`.
- **D3 (weaker than the kernel's hypothesis).** `Irrational (α / π) → ¬ RotClifford α`; π/8 satisfies
  `¬ RotClifford` with α/π rational.
- **D4 (the countermodel family reduces to π/4).** `MixR {k·β} ⊆ MixR {β}`; availability passes from k·β to β at
  every level; at every Clifford angle the level-one clause implies the clause at π/4.
- **D5 (the level-one group at the controls).** Finite up to scalar at every Clifford angle; not finite up to scalar
  at an irrational angle; not finite up to scalar at π/8, by W(π/8) and the recurrence of A5.
- **D6 (the statement and the reduction).** `AngleWeakenedLevelOne` (every theory with `DerivedOI` and the gate at an
  angle with `¬ RotClifford α` has the level-one clause) follows from one named input, density up to phase of the
  level-one group at the rational non-Clifford angles; with a second named input, the failure of the clause at π/4
  (O9-L1), an angle suffices at level one for every such theory exactly when `¬ RotClifford α`.

Written (not kernel-checked), predicted to close the inputs: for rational α ∉ (π/4)ℤ, W(α) has infinite order (a
finite-order element of SU(2) has an algebraic-integer trace; 1 + cos 2α is one only when cos 2α ∈ {0, ±1}, by the
norm of cos 2α over ℚ), so the image of the level-one group in SO(3) is infinite; it contains the quarter-turn about z
and the half-turn about x, and the rotation by 2α about y, which moves the z-line since sin 2α ≠ 0; the closed
subgroups of SO(3) [L] then leave only SO(3). The Clifford side is O9-L1 (written, with exact checks), carried to every
Clifford angle by D4.

Run 1 of `o12_angle.py` (2026-10-11T04:24:36Z, 17 s): `VERDICT O12-CLIFFORD-ANGLES-EXACTLY` — 792 grid angles, Clifford
exactly at the 8 angles kπ/4; classes 8 or 24 as predicted; the trace 1 + cos 2α not an algebraic integer at all 784
other grid angles, by both methods (199 distinct values of cos 2α, degree ≤ 15); A4–A6 True; PC1–PC3 True; CC1–CC6
False. Every S0 prediction met. Replay byte-identical. One pre-run edit before any run (the Pauli set cached per ring);
one library check before run 1 (sympy `minimal_polynomial` of cos(2πr) at four values), logged.

## 0. Verdict

Every statement below is an **availability** statement (an operation obtainable through the kernel's protocols:
`availExt`, `InstAvail`, the available level-one group), except the predicate `RotClifford` itself, which is a property
of the datum's matrix; none is a cone-invariance statement.

1. **The Clifford angles.** `RotClifford α` holds exactly when α ∈ (π/4)ℤ (`rotClifford_iff` [D]: the (0,0) and (0,1)
   entries of rot α · Z · rot α† are cos²α − sin²α and 2 sin α cos α, every Pauli matrix is diagonal or off-diagonal, so
   sin 4α = 0; conversely rot(kπ/4) lies in the group at π/4, which normalizes the Pauli set, `Gen2.pauli_conj`
   [K DiscreteCompletion.lean:1734]). On the grid of 792 reduced rational angles πp/q, q ≤ 36: exactly the 8 angles
   kπ/4 [X A1].
2. **Strictly weaker than the kernel's hypothesis.** Irrational(α/π) ⇒ ¬RotClifford α (`not_rotClifford_of_irrational`
   [D]); π/8 satisfies ¬RotClifford with α/π = 1/8 (`not_rotClifford_pi_div_eight`, `not_irrational_pi_div_eight`,
   `rotClifford_weaker` [D]).
3. **The countermodel side: every Clifford angle reduces to π/4.** The class at k·β lies in the class at β
   (`mixR_of_int_mul` [D]; for k < 0 through the exchange conjugation `mixImage_neg_eq_conj` [K :1853]), so availability
   in `fixedGateTheory (k·β)` is availability in `fixedGateTheory β`, at every level and for every family
   (`availExt_of_int_mul` [D], by `instAvail_mono` [K ImplementationLocality.lean:305]); at every Clifford angle the
   level-one clause implies the clause at π/4 (`levelOneClause_pi_div_four_of_rotClifford` [D]). The level-one group is
   finite up to scalar at every Clifford angle (`gen2Finite_of_rotClifford` [D], from the kernel's T3
   `gen2_multiple_finite_upToScalar` [K :1834]): 8 classes at α ∈ (π/2)ℤ, 24 at α ∈ π/4 + (π/2)ℤ [X A2]. With O9-L1
   (the clause fails at π/4: only the 24 Clifford channels are available at level one, by every route [W + X]), the
   clause fails at every Clifford angle: `fixedGateTheory α` is a countermodel to "DerivedOI ∧ FixedGateSourced α ⇒ the
   level-one clause" at every α ∈ (π/4)ℤ.
4. **The positive instance π/8.** The level-one group at π/8 is not finite up to scalar
   (`not_gen2Finite_pi_div_eight` [D]). The word W = rot(π/8) · rx(π/8) lies in it (`gen2_wordW` [D]; rx = S rot S†,
   S† = S³), has determinant 1 and trace 1 + √2/2 (`wordW_det`, `wordW_trace_pi_div_eight` [D]), so by
   Cayley–Hamilton W^{k+1} = p_{k+1} W − p_k 1 with p the Chebyshev sequence of that trace (`mul_self_fin_two`,
   `wordW_sq`, `wordW_pow` [D]); √2^k p_{k+1} = x_{k+1} + y_{k+1}√2 with integers whose x is odd at every step
   (`oddPair_spec`, `oddPair_odd` [D]: x_{k+2} ≡ x_{k+1} mod 2), so p_{k+1} ≠ 0 (`cheb_succ_ne_zero` [D], through the
   irrationality of √2), and since W's off-diagonal entry cos(π/8) sin(π/8)(i − 1) is not zero
   (`wordW_apply_01_ne_zero` [D]) no positive power of W is a scalar; a group finite up to scalar would give one
   (`exists_pow_scalar` [D], pigeonhole). Exact replication: the sequence identity and the parity to k = 400, the power
   formula and non-scalarity to k = 96 in ℚ(ζ₁₆) [X A5]. Availability at π/4 is availability at π/8 at every level
   (`availExt_pi_div_four_le_pi_div_eight` [D]): the positive instance contains the countermodel. Density: the image of
   the group in SO(3) contains the octahedral group (rot(π/4) = rot(π/8)², S, X) and an element of infinite order, so
   its closure is an infinite closed subgroup containing the octahedral group, which only SO(3) is [W + L: the closed
   subgroups of SO(3) are the finite ones, SO(2) and O(2) about an axis, and SO(3); O(2) about an axis contains
   order-four rotations about that axis only]. Hence the group is dense in U(2) up to phase and, by
   `levelOneClause_of_gen2Dense` [D], the level-one clause holds at π/8 in every theory with the closure and the gate.
5. **The rational angles at which the level-one clause fails are exactly the Clifford angles.** For α/π rational,
   α ∉ (π/4)ℤ: W(α) has determinant 1 and trace 2cos²α = 1 + cos 2α [X A3: exact at all 784 grid angles]. If W(α)
   had a scalar power, its eigenvalues would be roots of unity and its trace an algebraic integer, so cos 2α would be
   one; a nonzero algebraic integer cos 2α has its Galois conjugates cos 2αj in [−1, 1] and a nonzero integer norm, so
   all of them have modulus 1 and cos 2α = ±1 [W + L]. So cos 2α ∈ {0, ±1}, i.e. α ∈ (π/4)ℤ — excluded; W(α) has
   infinite order up to scalar [W + L; X A3 by two independent exact methods on the grid]. The image of the level-one
   group in SO(3) is then infinite and contains the quarter-turn about z (S), the half-turn about x (X) and the
   rotation by 2α about y (rot α); the quarter-turn about z forces any O(2) containing the group to be O(2) about z, and
   the y-rotation moves the z-line because sin 2α ≠ 0 [X A4]; so the closure is SO(3) and the group is dense up to
   phase [W + L] — `RationalDensityInput`. At α/π irrational the kernel gives the clause (`levelOne_dense`
   [K :762]). Hence, for every real α: the level-one clause holds in `fixedGateTheory α` ⟺ ¬RotClifford α ⟺
   α ∉ (π/4)ℤ — CONDITIONAL on O9-L1 (⇒) and on the written density argument (⇐ at the rational angles).
6. **The design-module statement and its reduction.** `AngleWeakenedLevelOne` — in every theory with `DerivedOI` and
   the gate at an angle with ¬RotClifford α, the level-one clause holds — follows from `RationalDensityInput`
   (`angleWeakened_of_rational` [D]); its irrational part is the kernel's (`angleSuffices_of_irrational` [D] from
   [K :762]). Adding `BalancedFailureInput` (O9-L1): `AngleSufficesLevelOne α ⟺ ¬RotClifford α` for every α
   (`angleSuffices_iff` [D]), and the gate at π/4 does not suffice (`not_angleSuffices_pi_div_four` [D]). The two
   controls are decided in the module: `control_countermodel` and `control_positive` [D].
7. **Scope: level one.** The kernel's route to every level isolates rot(2α) on one block (the echo identity
   [K :844]); at α = π/8 that is rot(π/4), a Clifford element (`echo_angle_rotClifford` [D]; [X A6], the level-two echo
   exactly), so the kernel's block-repertoire route does not run at π/8 at any level n ≥ 2 by itself, and inside the
   level-one group at π/8 there is no exact rotation about y by an irrational angle (entries in ℤ[ζ₁₆][1/2]; 2 is totally
   ramified in ℚ(ζ₁₆), so an element of modulus one there is a root of unity [W, not checked]). The clauses n = 2 and
   n = 3 hold at π/8 because availability at π/4 is availability at π/8 [D] and at π/4 they hold with the kernel's
   quarter phase (O9-L2C, O7-L3 [X + W + L]); n ≥ 4 at π/8 is not decided here. Whether ¬RotClifford α gives
   `DenseUnitaryControl` at every level is OPEN.

## 1. Hypotheses, by kind (the coordinator's rule)

| statement | hypotheses | kind | form |
|---|---|---|---|
| items 1, 2 (`rotClifford_iff`, `rotClifford_weaker`) | none: statements about the matrix rot α | — | a characterization of the datum's matrix |
| item 3 (reduction to π/4, finiteness) | the canonical theory's class `MixR` (I4.175, definition) with the gate at k·β | the gate: introduced, not an OI premise (I4.239 records the fixed nonclassical gate/control resource as an independent datum relative to the present architecture) | OI + {the gate at kπ/4} ⇒ availability at kπ/4 ⊆ availability at π/4 |
| item 4 (π/8) | the gate at π/8 in the canonical theory | as above | OI + {the gate at π/8} ⇒ the level-one group is not finite up to scalar |
| item 6, `AngleWeakenedLevelOne` | `DerivedOI T` (I1.49 = I4.241; status assumed, flag "do not assume"; holds for every canonical theory [K DiscreteCompletion.lean:1929]); `FixedGateSourced α T`; ¬RotClifford α; `RationalDensityInput` (a mathematical statement about a matrix group, [W + L]) | DerivedOI kind (i) at its status; the gate and the angle condition kind (ii): introduced, not OI premises | OI + {FixedGateSourced α, ¬RotClifford α} ⇒ the level-one clause |
| item 6, `angleSuffices_iff` | as above, and `BalancedFailureInput` (O9-L1, [W + X]) | as above | the angle condition is exact for the implication |

The kernel's own angle hypothesis `Irrational (α / π)` is of the same kind (the module header of DiscreteCompletion
says no irrationality condition is a physical principle); ¬RotClifford α replaces it at level one by a weaker,
exact one.

## 2. Disguise test of the predicate ¬RotClifford α

- *Letter:* passes. It names no non-monomial operator, complex structure or balanced state beyond the datum already
  assumed; it is an arithmetic condition on the datum's angle, decidable from α (α ∉ (π/4)ℤ).
- *Kernel carrier:* given the gate, it is equivalent for the canonical theories to the level-one clause itself (item 5).
  As a principle it adds nothing to the gate except the exclusion of the angles at which the gate is a Clifford
  element — the balanced mixer rot(π/4) and its powers. FAILED as an independent sourcing principle (it presupposes the
  gate, I4.239's independent datum, and restates the level-one conclusion in angle form); exact as a weakening of the
  kernel theorem's hypothesis at level one.
- It does not give exactness: `fixedGateTheory α` is not quantum mechanics at any angle (`fixedGateTheory_not_qm`
  [K :1948]).

## 3. Alternatives defeated (the coordinator's rule for O12–O13, in those words)

- The rational angle π/8, at which the clause holds, defeats *"dense unitary control at level one requires α/π
  irrational"*.
- The rational angles kπ/4, at which the clause fails (π/4 and π/2 among them, where rot α is not a scalar), defeat
  *"the gate at any angle at which rot α is not a scalar suffices for the level-one clause"*.
- Every Clifford angle being a countermodel (given O9-L1) defeats *"an angle condition weaker than ¬RotClifford α
  suffices at level one for every theory with the closure and the gate"*.
- The infinite level-one group at π/8 defeats *"the level-one group is finite at every rational angle"*.

## 4. Classification (§A.31)

The productivity test is met on both counts: (i) every rational angle is decided, each step labelled by layer; (ii) the
weakened hypothesis is a design-module statement whose two controls are decided in the module, with the general
statement reduced to two inputs named there.

- **NEW, O12-N1.** At level one the angle condition of `denseUnitaryControl_of_fixedGate` is exactly that rot α is not
  a Clifford element: the irrationality hypothesis is sufficient and not necessary, and the obstruction at π/4 is the
  finite Clifford group, not rationality.
- **NEW, O12-N2 (assumption-watch marker).** A level-one weakening of the angle hypothesis does not carry to every level
  by the kernel's route: the echo isolates rot(2α), so the all-level route needs the angle condition at 2α as well
  (at π/8 the isolated block is Clifford).
- **CONFIRMING.** O9-E (the two angles), HO-22 item 2 read as a cross-check (z-rotations of orders 1, 2, 4 only at a
  finite stage holding J — the same norm argument), O11-T6 (π/4 finite, π/8 infinite on the token body).

## 5. Design-module record

- Run 38111982910 (dispatch 2/3, dev commit 9dd6a173): Build failure with one error, in `blockOf_gen2_mem` (case
  `mul`: the kernel's `blockOf_mul` rewrites a product of blocks into the block of a product, so the goal needed the
  reverse rewrite); every other declaration elaborated; the error's stand-in reached the four theorems that use it. Kept
  as `lean/OriginAngle.run38111982910.lean` (blob 105d0d54).
- Run 38112242400 (dispatch 3/3, dev commit f0cd9272, the one rewrite reversed and nothing else): Mathlib bridge job
  114390032425, Build success (3644 jobs; the module built with four linter warnings, `<;>` where `;` suffices); all 52
  `#print axioms` lines on [propext, Classical.choice, Quot.sound] except `oddPair_odd` on [propext, Quot.sound]; no
  `sorryAx`; release gate red only on `lean-manuscript` (the new module has no census disposition, by construction),
  `lean-axioms` PASS (5912 named results). `lean/OriginAngle.lean` is the verbatim f0cd9272 file (blob f4da8c3d, sha256
  b1beafcc…2955b1, 678 lines). Design evidence only; not certified.

## 6. Open

- The density inputs are written: the closed subgroups of SO(3) [L], the norm lemma for cos 2πr [W + L]; O9-L1 is
  written with exact checks. None is kernel-checked.
- Levels n ≥ 2 at rational non-Clifford angles other than through the inclusion from π/4; `DenseUnitaryControl` under
  ¬RotClifford α at every level.
