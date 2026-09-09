/-
  OIBridge/QuantumRepresentation.lean — target T1 of `OI-QUANTUM-REPRESENTATION-AUDIT.md`.

  Frozen preregistration: commit `38a8f09d9d314fdd3d7747d0d0351f07c693c582`, authoritative blob
  `8177527b11a0970c7fc71f1bff382112aaf93aa6`, merged at
  `073ef65ae286e67e84ce4dfc0f634252cf29939f`.  Amendment 1, blob
  `e809e04aee45181d162bd4a2cc2782751b65f509`, merged at
  `64565efc4441e266f552db2b85438d6a994d0285`, retires the adversarial/bias machinery and nothing
  else.

  THIS FILE IS T1 ONLY — the translation layer.  It defines the all-time class `Q*` and proves the
  finite-horizon compatibility theorem.  It decides NEITHER inclusion: `Q* ⊆ C_OI` (T2) and
  `C_OI ⊆ Q*` (T3) are untouched here, and nothing below may be read as evidence for either.

  WHICH CLAUSES OF THE MERGED `QfbReal` ARE CARRIED.  All four data fields are carried unchanged —
  the basis, the single unitary, the initial weight, and the readout — together with `IsLaw`
  (unitarity plus a normalised nonnegative initial weight) and the one-step Born weight
  `‖U b' b‖^2`.  What is dropped is the horizon index `K`.  That is not a weakening: `QfbReal V K`
  has `K` as a parameter and NO field of it mentions `K`, so the horizon lives only in the
  trajectory length, never in the datum.  `QfbData` below is that same datum with the vestigial
  index removed.

  WHAT IS ADDED, AND WHY IT IS FORCED.  `QfbReal` carries ONE GLOBAL `init` and no root-indexed
  field of any kind, while the Arc B object is conditioned on a prepared visible root.  The frozen
  preregistration therefore fixes the rooted object by CONDITIONING the single process on the
  visible event `read (B_0) = a`, and requires positive mass on every root fibre so that the
  conditioning is defined.  Both appear below as `rootMass` and `PositiveRootMass`.

  THE THREE REJECTED MAPS, kept out structurally rather than by comment:

  * root-indexed initial laws — `QStar` quantifies ONE `QfbData` outside `∀ a t j`, so a per-root
    `init` cannot be supplied;
  * an imported OI-style hidden prior — `QfbData` has no prior field, only `init` on the basis;
  * a finer basis-level conditioning event — every conditioning sum below runs over the READ FIBRE
    `Q.read b = a`, never over a basis point.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.Equivalence

namespace OIBridge

namespace QuantumRepresentation

open Finset Matrix OIBridge.Equivalence OIBridge.FiniteEntropy

universe u

set_option linter.unusedSectionVars false

variable {V : Type u} [Fintype V] [DecidableEq V]

/-! ### The all-time representation datum

The merged `QfbReal` datum with the vestigial horizon index dropped.  One basis, one unitary, one
initial law, one readout — the same four fields, serving every root and every time. -/

/-- **The all-time `Q_fb` datum.**  Identical to `QfbReal` field for field; only the unused horizon
index is gone. -/
structure QfbData (V : Type u) : Type (u + 1) where
  Bas : Type u
  fB : Fintype Bas
  dB : DecidableEq Bas
  U : Matrix Bas Bas ℂ
  init : Bas → ℝ
  read : Bas → V

attribute [instance] QfbData.fB QfbData.dB

/-- Unitarity of the evolution and normalisation of the initial law, verbatim from `QfbReal`. -/
def QfbData.IsLaw (Q : QfbData V) : Prop :=
  Q.U ∈ Matrix.unitaryGroup Q.Bas ℂ ∧ (∀ b, 0 ≤ Q.init b) ∧ ∑ b, Q.init b = 1

/-- The one-step Born weight, verbatim from `QfbReal`. -/
noncomputable def QfbData.born (Q : QfbData V) (b b' : Q.Bas) : ℝ := ‖Q.U b' b‖ ^ 2

/-- The trajectory weight of the fixed-basis record: projective measurement at every step, with
collapse.  Verbatim from `QfbReal.chain`. -/
noncomputable def QfbData.chainW {K : ℕ} (Q : QfbData V) (σ : Fin (K + 1) → Q.Bas) : ℝ :=
  Q.init (σ 0) * ∏ k : Fin K, Q.born (σ k.castSucc) (σ k.succ)

/-! ### The frozen root-preparation map

`rootMass` is the mass of the visible root FIBRE — the conditioning event is `read b = a`, never a
basis point.  `PositiveRootMass` is the frozen side condition that makes the conditioning defined. -/

/-- Mass of the visible root fibre at time zero: `P[read (B_0) = a]`. -/
noncomputable def QfbData.rootMass (Q : QfbData V) (a : V) : ℝ :=
  ∑ b ∈ univ.filter (fun b => Q.read b = a), Q.init b

/-- **The frozen positive-root-mass clause.**  Not a formality: conditioning is undefined without
it, and it restricts which data may witness membership. -/
def QfbData.PositiveRootMass (Q : QfbData V) : Prop := ∀ a : V, 0 < Q.rootMass a

theorem QfbData.rootMass_nonneg {Q : QfbData V} (hQ : Q.IsLaw) (a : V) : 0 ≤ Q.rootMass a :=
  Finset.sum_nonneg fun b _ => hQ.2.1 b

/-! ### The finite-horizon root-conditioned trajectory law

A truncation of `Γ` is a collection of rooted marginals, not a joint trajectory law, so the object
to be represented is named here rather than assumed: `rootTraj` is the length-`K` joint law of
`(read (B_0), …, read (B_K))` conditioned on the visible event `read (B_0) = a`.

It is defined from the UNCONDITIONED chain weight and the root mass.  It is deliberately NOT
defined as the law of some re-conditioned datum: were it, the compatibility theorem below would
hold by construction and would establish nothing. -/

/-- `P^a_K`: the length-`K` root-conditioned visible trajectory law. -/
noncomputable def QfbData.rootTraj (Q : QfbData V) (K : ℕ) (a : V) (τ : Traj V K) : ℝ :=
  if τ 0 = a then marg Q.chainW (fun σ => fun k => Q.read (σ k)) τ / Q.rootMass a else 0

/-! ### The re-conditioned horizon datum

Same basis, same unitary, same readout.  Only the initial law is re-conditioned — and that reuse is
DEFINITIONAL here, so `condReal_Bas`, `condReal_U` and `condReal_read` below are `rfl`.  A witness
produced per horizon out of unrelated data could not satisfy them. -/

/-- The root fibre, renormalised.  The only field that differs from `Q`. -/
noncomputable def QfbData.condInit (Q : QfbData V) (a : V) (b : Q.Bas) : ℝ :=
  if Q.read b = a then Q.init b / Q.rootMass a else 0

/-- The horizon-`K` datum reusing `Q`'s basis, unitary and readout verbatim. -/
noncomputable def QfbData.condReal (Q : QfbData V) (a : V) (K : ℕ) : QfbReal V K where
  Bas := Q.Bas
  fB := Q.fB
  dB := Q.dB
  U := Q.U
  init := Q.condInit a
  read := Q.read

@[simp] theorem QfbData.condReal_Bas (Q : QfbData V) (a : V) (K : ℕ) :
    (Q.condReal a K).Bas = Q.Bas := rfl

@[simp] theorem QfbData.condReal_U (Q : QfbData V) (a : V) (K : ℕ) :
    (Q.condReal a K).U = Q.U := rfl

@[simp] theorem QfbData.condReal_read (Q : QfbData V) (a : V) (K : ℕ) :
    (Q.condReal a K).read = Q.read := rfl

@[simp] theorem QfbData.condReal_born (Q : QfbData V) (a : V) (K : ℕ) (b b' : Q.Bas) :
    (Q.condReal a K).born b b' = Q.born b b' := rfl

/-! ### `Q*`, the all-time class

The existential block stands OUTSIDE `∀ a t j`: one basis, one unitary, one initial law and one
readout serve every root and every time.  Moving any of them inside the root quantifier is a
different class, and is rejected by the frozen preregistration. -/

/-- `t`-step transition weight of the Born chain. -/
noncomputable def QfbData.bornPow (Q : QfbData V) : ℕ → Q.Bas → Q.Bas → ℝ
  | 0, b, b' => if b = b' then 1 else 0
  | (t + 1), b, b' => ∑ c, Q.bornPow t b c * Q.born c b'

/-- Joint weight of `read (B_0) = a` and `read (B_t) = j`. -/
noncomputable def QfbData.jointMass (Q : QfbData V) (t : ℕ) (a j : V) : ℝ :=
  ∑ b ∈ univ.filter (fun b => Q.read b = a),
    ∑ b' ∈ univ.filter (fun b' => Q.read b' = j), Q.init b * Q.bornPow t b b'

/-- The rooted family entry: `P[read (B_t) = j | read (B_0) = a]`. -/
noncomputable def QfbData.rooted (Q : QfbData V) (t : ℕ) (a j : V) : ℝ :=
  Q.jointMass t a j / Q.rootMass a

/-- **`Q*(V)`.**  Note the quantifier order, which is the frozen one: the existential block is
outside `∀ a t j`. -/
def QStar (Γ : ℕ → Matrix V V ℝ) : Prop :=
  ∃ Q : QfbData V, Q.IsLaw ∧ Q.PositiveRootMass ∧ ∀ (a : V) (t : ℕ) (j : V), Γ t a j = Q.rooted t a j

/-! ### The finite-horizon compatibility theorem

The frozen statement, and not the weaker one: the witnessing representation is `Q.condReal a K`,
built from `Q`'s own basis, unitary and readout with only the initial law re-conditioned.  The
per-horizon existential `∀K ∃Q_K` follows as a corollary and is explicitly NOT the theorem — a proof
supplying a different basis or unitary at each horizon would satisfy the corollary while
establishing nothing about `Q*`. -/

theorem QfbData.condReal_chain (Q : QfbData V) (a : V) (K : ℕ) (σ : Fin (K + 1) → Q.Bas) :
    (Q.condReal a K).chain σ = if Q.read (σ 0) = a then Q.chainW σ / Q.rootMass a else 0 := by
  show Q.condInit a (σ 0) * ∏ k : Fin K, Q.born (σ k.castSucc) (σ k.succ) = _
  unfold QfbData.condInit QfbData.chainW
  split
  · rw [div_mul_eq_mul_div]
  · rw [zero_mul]

theorem QfbData.condReal_isLaw (Q : QfbData V) (hQ : Q.IsLaw) (hpos : Q.PositiveRootMass)
    (a : V) (K : ℕ) : (Q.condReal a K).IsLaw := by
  refine ⟨hQ.1, fun b => ?_, ?_⟩
  · show 0 ≤ Q.condInit a b
    unfold QfbData.condInit
    split
    · exact div_nonneg (hQ.2.1 b) (hpos a).le
    · exact le_rfl
  · show ∑ b, Q.condInit a b = 1
    unfold QfbData.condInit
    rw [← Finset.sum_filter, ← Finset.sum_div]
    exact div_self (hpos a).ne'

/-- **T1 finite-horizon compatibility.**  The root-conditioned trajectory law is the law of the
datum that reuses `Q`'s basis, unitary and readout.

No positivity hypothesis: the identity holds for every `Q`.  Positive root mass is what makes the
re-conditioned initial law NORMALISED (`condReal_isLaw`), and what makes the conditional reading of
`rootTraj` meaningful; it is not needed for the two sides to agree, and carrying it here would
advertise a dependency this proof does not have. -/
theorem QfbData.condReal_law (Q : QfbData V) (a : V) (K : ℕ) :
    (Q.condReal a K).law = Q.rootTraj K a := by
  funext τ
  -- Everything is put in one type world before any rewrite fires.  `(Q.condReal a K).Bas` reduces
  -- to `Q.Bas`, but `rw` matches syntactically, so leaving the structure projections standing
  -- produced an `Application type mismatch` on `σ k` — the same shape as the Arc B padding bug.
  -- Unfolding the datum to its literal makes the projections reduce and the two sums comparable.
  unfold QfbData.rootTraj QfbReal.law marg QfbData.condReal QfbReal.chain QfbReal.born
    QfbData.chainW QfbData.born QfbData.condInit
  dsimp only
  split
  · rename_i hτ
    rw [Finset.sum_div]
    refine Finset.sum_congr rfl fun σ hσ => ?_
    have hr : Q.read (σ 0) = τ 0 := congrFun (Finset.mem_filter.1 hσ).2 0
    rw [if_pos (by rw [hr]; exact hτ), div_mul_eq_mul_div]
  · rename_i hτ
    refine Finset.sum_eq_zero fun σ hσ => ?_
    have hr : Q.read (σ 0) = τ 0 := congrFun (Finset.mem_filter.1 hσ).2 0
    rw [if_neg (by rw [hr]; exact hτ), zero_mul]

/-- The weaker per-horizon form, DERIVED from the theorem above.  Stated as a corollary precisely so
that it cannot be mistaken for the theorem: `∀K ∃Q_K` does not constrain the representing data to be
the same across horizons, and is not what T1 asks for. -/
theorem qfbRealizable_rootTraj (Q : QfbData V) (hQ : Q.IsLaw) (hpos : Q.PositiveRootMass)
    (a : V) (K : ℕ) : QfbRealizable (Q.rootTraj K a) :=
  ⟨Q.condReal a K, Q.condReal_isLaw hQ hpos a K, Q.condReal_law a K⟩

end QuantumRepresentation

end OIBridge

/-! ### Axiom reporting

Every named result above, printed here, so that the set of theorem names equals the set of print
targets and neither can drift from the other. -/

#print axioms OIBridge.QuantumRepresentation.QfbData.rootMass_nonneg
#print axioms OIBridge.QuantumRepresentation.QfbData.condReal_Bas
#print axioms OIBridge.QuantumRepresentation.QfbData.condReal_U
#print axioms OIBridge.QuantumRepresentation.QfbData.condReal_read
#print axioms OIBridge.QuantumRepresentation.QfbData.condReal_born
#print axioms OIBridge.QuantumRepresentation.QfbData.condReal_chain
#print axioms OIBridge.QuantumRepresentation.QfbData.condReal_isLaw
#print axioms OIBridge.QuantumRepresentation.QfbData.condReal_law
#print axioms OIBridge.QuantumRepresentation.qfbRealizable_rootTraj
