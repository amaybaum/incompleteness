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
