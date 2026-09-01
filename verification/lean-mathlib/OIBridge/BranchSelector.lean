/-
  OIBridge/BranchSelector.lean — the rank-one selector uniqueness theorem and the
  monomial–Lüders compatibility that together close the H-pure-seed guard.

  PHASE THREE, ROUND TWENTY-TWO. Round twenty-one reduced H-pure-seed to a single
  remaining question: does bare OI license the rank-one selective branch update? This
  file removes that guard without inventing an H-readout assumption.

  §A — RANK-ONE SELECTOR UNIQUENESS. `RankOneSelector Φ k`: a linear map with
  `Φ(E_ss) = δ_sk E_kk`. The capstone

      ┌────────────────────────────────────────────────────────────────────┐
      │  `cp_rankOneSelector_iff_luders`:  a completely positive map is a    │
      │  rank-one classical selector for outcome k  ⟺  Φ(X) = P_k X P_k.    │
      └────────────────────────────────────────────────────────────────────┘

  The forward direction is the round-seventeen Choi argument specialized: the Choi
  diagonal vanishes except at `((k,k),(k,k)) = 1`, the PSD zero-diagonal lemma kills
  every other row and column, so `J_Φ = E_{(k,k),(k,k)}` and reconstruction gives
  exactly the Lüders map. So a CP coherent completion of the classical branch has NO
  ALTERNATIVE to Lüders — the branch update is forced, not a new freedom.

  §B — MONOMIAL–LÜDERS COMPATIBILITY. `monomial_luders_classicalBranch`: on a diagonal
  (classical) state, the fixed-basis Lüders readout after any H-functor monomial lift
  `U_g = D·P_g` is the phase-free classical branch:

      P_k (U_g diag(w) U_g†) P_k = w(g⁻¹ k) · P_k,

  independent of the unimodular phases `D`. So the same Lüders readout composes with
  every monomial lift the round-eighteen classification allows: H-functor's phases do
  not disturb the branch.

  THE CLOSED CHAIN. (1) the bare Q_fb construction supplies a CP rank-one branch
  extension; (2) `cp_rankOneSelector_iff_luders` says any such extension is Lüders;
  (3) `monomial_luders_classicalBranch` says H-functor's monomial phases do not disturb
  it; (4) H-tensor supplies the ancilla as a genuine local factor; (5) round twenty-one's
  `uniform_readout_feedforward_seed` produces the pure seed. So H-pure-seed disappears —
  NOT replaced by an H-readout assumption — and the endpoint is genuinely three
  conditions: H-functor, H-tensor, and sufficient composite Lie rank.

  §C — THE COARSE SELECTOR (probe F35). For a rank-`|F|` fibre the surviving freedom is
  a correlation-matrix family inside the selected block (Lüders is all-ones `C`, complete
  within-block dephasing is `C = I`); rank one kills that freedom automatically. F35
  exhibits the rank-two family (Lüders vs dephasing agree on every classical branch
  probability, differ on `E_{01}`) and its rank-one collapse.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.Purification

namespace OIBridge
namespace BranchSelector

open Complex Matrix CoherentExtension DynamicsGlue Purification
open scoped ComplexOrder

local notation "conj'" => (starRingEnd ℂ)

variable {S : Type*} [Fintype S] [DecidableEq S]

/-! ### Section A — rank-one selector uniqueness -/

/-- The Lüders branch map `X ↦ P_k X P_k = X_kk · E_kk`, as a linear map. -/
def ludersLift (k : S) : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun X := X k k • Matrix.single k k 1
  map_add' X Y := by
    show (X + Y) k k • Matrix.single k k 1
      = X k k • Matrix.single k k 1 + Y k k • Matrix.single k k 1
    rw [Matrix.add_apply, add_smul]
  map_smul' c X := by
    show (c • X) k k • Matrix.single k k 1
      = (RingHom.id ℂ) c • (X k k • Matrix.single k k 1)
    rw [Matrix.smul_apply, smul_eq_mul, RingHom.id_apply, mul_smul]

omit [Fintype S] in
@[simp] theorem ludersLift_apply (k : S) (X : Matrix S S ℂ) :
    ludersLift k X = X k k • Matrix.single k k 1 := rfl

/-- A rank-one classical selector for outcome `k`: `Φ(E_ss) = δ_sk E_kk`. -/
def RankOneSelector (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (k : S) : Prop :=
  ∀ s, Φ (Matrix.single s s 1) = if s = k then Matrix.single k k 1 else 0

/-- The Lüders map is a rank-one selector. -/
theorem ludersLift_selector (k : S) : RankOneSelector (ludersLift k) k := by
  intro s
  rw [ludersLift_apply, single_entry]
  by_cases h : s = k
  · rw [if_pos ⟨h, h⟩, if_pos h, one_smul]
  · rw [if_neg (fun hh => h hh.1), if_neg h, zero_smul]

omit [Fintype S] in
/-- The Choi matrix of the Lüders map is the diagonal indicator of `(k,k)`. -/
theorem choi_ludersLift (k : S) :
    choiMatrix (ludersLift k)
      = Matrix.diagonal (fun q : S × S => if q = (k, k) then (1 : ℂ) else 0) := by
  ext p q
  obtain ⟨p1, p2⟩ := p
  obtain ⟨q1, q2⟩ := q
  show (ludersLift k (Matrix.single p1 q1 1)) p2 q2
    = Matrix.diagonal (fun q : S × S => if q = (k, k) then (1 : ℂ) else 0) (p1, p2) (q1, q2)
  simp only [ludersLift_apply, Matrix.smul_apply, smul_eq_mul, Matrix.single_apply,
    Matrix.diagonal_apply, Prod.mk.injEq]
  by_cases hp1 : p1 = k <;> by_cases hq1 : q1 = k <;> by_cases hp2 : p2 = k <;>
    by_cases hq2 : q2 = k <;> simp_all [eq_comm]

/-- The Lüders map is completely positive. -/
theorem ludersLift_cp (k : S) : IsCompletelyPositive (ludersLift k) := by
  show (choiMatrix (ludersLift k)).PosSemidef
  rw [choi_ludersLift]
  refine Matrix.PosSemidef.diagonal (fun q => ?_)
  show (0 : ℂ) ≤ if q = (k, k) then (1 : ℂ) else 0
  by_cases h : q = (k, k)
  · rw [if_pos h]; exact zero_le_one
  · rw [if_neg h]

/-- **THE FORWARD DIRECTION.** A completely positive rank-one classical selector is the
Lüders map: the Choi diagonal vanishes off `(k,k)`, PSD kills the rest, and what
survives reconstructs `X ↦ P_k X P_k`. -/
theorem cp_rankOneSelector_forces_luders (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
    (k : S) (hCP : IsCompletelyPositive Φ) (hsel : RankOneSelector Φ k) :
    Φ = ludersLift k := by
  have hJdiag : ∀ s a, choiMatrix Φ (s, a) (s, a)
      = if s = k ∧ a = k then (1 : ℂ) else 0 := by
    intro s a
    show Φ (Matrix.single s s 1) a a = _
    rw [hsel s]
    by_cases hs : s = k
    · rw [if_pos hs]
      show (Matrix.single k k 1) a a = _
      rw [single_entry]
      by_cases ha : a = k
      · rw [if_pos ⟨ha.symm, ha.symm⟩, if_pos ⟨hs, ha⟩]
      · rw [if_neg (fun hh => ha hh.1.symm), if_neg (fun hh => ha hh.2)]
    · rw [if_neg hs, Matrix.zero_apply, if_neg (fun hh => hs hh.1)]
  have hoff : ∀ (s a : S) (q : S × S), ¬(s = k ∧ a = k)
      → choiMatrix Φ (s, a) q = 0 ∧ choiMatrix Φ q (s, a) = 0 := by
    intro s a q hsa
    exact psd_diag_zero_entry_zero hCP (by rw [hJdiag]; exact if_neg hsa) q
  have hbasis : ∀ s t, Φ (Matrix.single s t 1) = ludersLift k (Matrix.single s t 1) := by
    intro s t
    ext a b
    have hlhs : Φ (Matrix.single s t 1) a b = choiMatrix Φ (s, a) (t, b) := rfl
    rw [hlhs, ludersLift_apply, Matrix.smul_apply, smul_eq_mul, single_entry,
      single_entry]
    by_cases h1 : s = k ∧ a = k
    · by_cases h2 : t = k ∧ b = k
      · rw [if_pos ⟨h1.1, h2.1⟩, if_pos ⟨h1.2.symm, h2.2.symm⟩, mul_one,
          h1.1, h1.2, h2.1, h2.2]
        have hh := hJdiag k k
        rwa [if_pos ⟨rfl, rfl⟩] at hh
      · rw [(hoff t b (s, a) h2).2]
        by_cases ht : t = k
        · rw [if_neg (show ¬(k = a ∧ k = b) from fun hh => h2 ⟨ht, hh.2.symm⟩),
            mul_zero]
        · rw [if_neg (show ¬(s = k ∧ t = k) from fun hh => ht hh.2), zero_mul]
    · rw [(hoff s a (t, b) h1).1]
      by_cases hs : s = k
      · rw [if_neg (show ¬(k = a ∧ k = b) from fun hh => h1 ⟨hs, hh.1.symm⟩), mul_zero]
      · rw [if_neg (show ¬(s = k ∧ t = k) from fun hh => hs hh.1), zero_mul]
  refine LinearMap.ext fun X => ?_
  conv_lhs => rw [Matrix.matrix_eq_sum_single X]
  conv_rhs => rw [Matrix.matrix_eq_sum_single X]
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun s _ => ?_
  rw [map_sum, map_sum]
  refine Finset.sum_congr rfl fun t _ => ?_
  rw [single_eq_smul, map_smul, map_smul, hbasis]

/-- **THE CAPSTONE.** Complete positivity plus the rank-one classical selector condition
is EXACTLY the Lüders branch map: a CP coherent completion of the classical branch has
no alternative to `X ↦ P_k X P_k`. -/
theorem cp_rankOneSelector_iff_luders (Φ : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) (k : S) :
    (IsCompletelyPositive Φ ∧ RankOneSelector Φ k) ↔ Φ = ludersLift k := by
  constructor
  · rintro ⟨hCP, hsel⟩
    exact cp_rankOneSelector_forces_luders Φ k hCP hsel
  · rintro rfl
    exact ⟨ludersLift_cp k, ludersLift_selector k⟩

/-! ### Section B — monomial–Lüders compatibility -/

/-- **THE PHASES VANISH ON THE BRANCH.** On a diagonal (classical) state, the
fixed-basis Lüders readout after any H-functor monomial lift `U_g = D·P_g` is the
phase-free classical branch `w(g⁻¹ k)·P_k` — independent of the unimodular phases `D`.
So the same Lüders readout composes with every monomial lift the round-eighteen
classification allows. -/
theorem monomial_luders_classicalBranch (g : Equiv.Perm S) (d : S → ℂ)
    (hd : ∀ s, d s * conj' (d s) = 1) (w : S → ℂ) (k : S) :
    rankOneProj k
        * (Matrix.diagonal d * CoherentLift.permMatrix g * Matrix.diagonal w
            * (Matrix.diagonal d * CoherentLift.permMatrix g)ᴴ)
        * rankOneProj k
      = w (g.symm k) • rankOneProj k := by
  rw [branch_project]
  congr 1
  rw [monomial_conj_apply, Matrix.diagonal_apply_eq, hd k, one_mul]

#print axioms ludersLift_selector
#print axioms choi_ludersLift
#print axioms ludersLift_cp
#print axioms cp_rankOneSelector_forces_luders
#print axioms cp_rankOneSelector_iff_luders
#print axioms monomial_luders_classicalBranch

end BranchSelector
end OIBridge
