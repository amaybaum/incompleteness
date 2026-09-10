import OIBridge.OperationalSourcing

/-!
  OIBridge/CandidateSelection.lean — targets of `BARANDES-CANDIDATE-SELECTION-PREREGISTRATION.md`.

  Frozen preregistration: commit `2fb894192bc9ae3bddc8bfa19301eeee1195a3fc`, blob
  `64e07da7f20f362386da01087a260723a2213e68`, merged to `main` by PR #564.

  Track B act 3.  The eight frozen definitions and the four targets C1–C4 are carried here in
  exactly the form the freeze fixes; control 4 of that freeze forbids reshaping any of them to fit
  a proof.

  WHAT THIS ROUND IS FOR.  Track B is heading toward whether OI forces a nonzero interference
  discrepancy, which needs the chain

      OI stochastic family  →  representation  →  candidate intermediate  →  discrepancy.

  Arc D round 1 settled that the first arrow does not determine operator content.  This round asks
  the next question down: does the *representation* determine the candidate intermediate?  The
  scoping pass (`BARANDES-REPRESENTATION-FREEDOM-SCOPING.md`, PR #563) is cited as motivation only,
  and its Findings 2 and 3 are provisional by its own terms — C3 is where Finding 2 becomes a
  theorem, and Finding 3 is used as a premise nowhere.

  WHAT IT IS NOT.  Nothing here identifies `candidateOf` with any external object.  Act 1
  (`BARANDES-INDIVISIBILITY-BRIDGE-AUDIT-RESULT.md`, PR #560) established that the external
  diagnostic discussion uses a *particular* candidate while this programme's `PDivisible` quantifies
  existentially over all stochastic candidates; that determination is neither reopened nor extended,
  and no theorem below is a correspondence claim or a sourcing claim.

  EVERY DECISIVE OUTCOME IS EARNED BY A PROOF.  Three of the eight frozen definitions are
  outcome-bearing propositions rather than constructions: `NamedRuleInadmissible` is the negative of
  C1's named-rule admissibility subtarget and is what `CU3` requires, and `AdmissibleNonUnique` /
  `AdmissibleAgree` are C4's two sides.  Failing to prove one of them is never evidence for its
  negation; that case is `CU4`.
-/

namespace OIBridge

namespace CandidateSelection

open Finset Matrix
open OIBridge.QuantumRepresentation OIBridge.CausalReadback OIBridge.OperationalSourcing

variable {V : Type} [Fintype V] [DecidableEq V]

/-! ### The frozen definitions

All eight are stated here in the form the freeze fixes.  `FibreWeight`, `candidateOf`,
`initWeight`, `uniformWeight` and `Admissible` are the constructions; `NamedRuleInadmissible`,
`AdmissibleNonUnique` and `AdmissibleAgree` are the outcome-bearing propositions and appear with
their targets below. -/

/-- Weight assigned to each basis point of the visible fibre over `k`, from which a visible
candidate propagator is marginalized. -/
def FibreWeight (Q : QfbData V) : Type := V → Q.Bas → ℝ

/-- The visible candidate propagator induced by a representation and a fibre weighting: push
`bornPow n` down to the visible carrier by weighting each source fibre and summing each target
fibre. -/
noncomputable def candidateOf (Q : QfbData V) (μ : FibreWeight Q) (n : ℕ) : Matrix V V ℝ :=
  fun k j => ∑ b ∈ univ.filter (fun b => Q.read b = k),
               ∑ b' ∈ univ.filter (fun b' => Q.read b' = j), μ k b * Q.bornPow n b b'

/-- The init-weighted rule: weight the fibre by the normalized initial law. -/
noncomputable def initWeight (Q : QfbData V) : FibreWeight Q :=
  fun k b => if Q.read b = k then Q.init b / Q.rootMass k else 0

/-- The uniform-on-fibre rule: weight every basis point over `k` equally. -/
noncomputable def uniformWeight (Q : QfbData V) : FibreWeight Q :=
  fun k b => if Q.read b = k
    then 1 / (univ.filter (fun c => Q.read c = k)).card else 0

/-- Admissibility: the weight is a probability distribution on the source fibre — supported there,
nonnegative, and normalized.  None of the three clauses mentions `init`, `U` or the fibre's
cardinality, so none privileges `initWeight` or `uniformWeight`. -/
def Admissible (Q : QfbData V) (μ : FibreWeight Q) : Prop :=
  (∀ k b, Q.read b ≠ k → μ k b = 0) ∧ (∀ k b, 0 ≤ μ k b) ∧ (∀ k, ∑ b, μ k b = 1)

/-! ### Shared arithmetic

Three facts the targets share.  They are stated here so that no target re-proves them, and none of
them is a frozen object. -/

omit [Fintype V] [DecidableEq V] in
/-- Born weights are nonnegative: they are squared norms. -/
theorem born_nonneg (Q : QfbData V) (b b' : Q.Bas) : 0 ≤ Q.born b b' := by
  unfold QfbData.born
  positivity

/-- `bornPow` is nonnegative at every horizon. -/
theorem bornPow_nonneg (Q : QfbData V) : ∀ (n : ℕ) (b b' : Q.Bas), 0 ≤ Q.bornPow n b b' := by
  intro n
  induction n with
  | zero =>
      intro b b'
      by_cases h : b = b' <;> simp [QfbData.bornPow, h]
  | succ m ih =>
      intro b b'
      show (0 : ℝ) ≤ ∑ c, Q.bornPow m b c * Q.born c b'
      exact Finset.sum_nonneg fun c _ => mul_nonneg (ih b c) (born_nonneg Q c b')

omit [DecidableEq V] in
/-- One elapsed step of the Born chain is one Born weight. -/
theorem bornPow_one (Q : QfbData V) (b b' : Q.Bas) : Q.bornPow 1 b b' = Q.born b b' := by
  show (∑ c, Q.bornPow 0 b c * Q.born c b') = Q.born b b'
  have hterm : ∀ c : Q.Bas, Q.bornPow 0 b c * Q.born c b'
      = if c = b then Q.born c b' else 0 := by
    intro c
    by_cases h : b = c
    · subst h; simp [QfbData.bornPow]
    · have h' : ¬ c = b := fun hc => h hc.symm
      simp [QfbData.bornPow, h, h']
  rw [Finset.sum_congr rfl fun c _ => hterm c]
  simp

omit [Fintype V] in
/-- An admissible weight sums to one over the fibre it names, not merely over the whole basis. -/
theorem sum_fibre_of_admissible {Q : QfbData V} {μ : FibreWeight Q} (hμ : Admissible Q μ) (k : V) :
    ∑ b ∈ univ.filter (fun b => Q.read b = k), μ k b = 1 := by
  rw [Finset.sum_subset (Finset.filter_subset _ _)]
  · exact hμ.2.2 k
  · intro b _ hb
    exact hμ.1 k b (by simpa using hb)

/-! ### C1 — both rules are admissible, and admissible rules give candidates

Without C1 the later targets would compare objects that are not candidates.

**The negative of C1's named-rule admissibility subtarget is frozen too, and `CU3` requires it.**
All three positive statements below could fail to close without that proving anything about the
criterion — exactly the proof-search-versus-negation gap that C2's "not established" status exists
to respect.  Criterion failure is therefore its own frozen target, `NamedRuleInadmissible`, covering
the **first two** statements; `candidateOf_isRowStochastic` has no frozen negative, and its
non-closure would be `CU4`.

`CU3` is claimed **only** on a proof of that proposition, and no such proof appears here.  Note the
two distinct reasons that could hold.  In general, absence of a proof is not evidence against a
proposition.  In *this* case something stronger is true and is worth stating rather than blurring:
`NamedRuleInadmissible` carries `IsLaw`, `PositiveRootMass`, inhabited fibres and `Nonempty V` as its
own hypotheses, and under exactly those the two C1 theorems below give both named rules admissible —
so C1 independently **excludes** that witness.  What licenses the stronger reading is C1, not the
absence.  No corollary is added for it: that would be a new target introduced after seeing the
results. -/

/-- CRITERION FAILURE.  Some representation meeting C1's hypotheses carries a named rule that the
frozen `Admissible` does not admit.  This is the `CU3` side; nothing in this module proves it. -/
def NamedRuleInadmissible : Prop :=
  ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (_ : Nonempty V) (Q : QfbData V),
    Q.IsLaw ∧ Q.PositiveRootMass ∧ (∀ k, ∃ b, Q.read b = k)
    ∧ (¬ Admissible Q (initWeight Q) ∨ ¬ Admissible Q (uniformWeight Q))

/-- **C1, first statement.** -/
theorem initWeight_admissible (Q : QfbData V) (hQ : Q.IsLaw) (hP : Q.PositiveRootMass) :
    Admissible Q (initWeight Q) := by
  refine ⟨fun k b hb => ?_, fun k b => ?_, fun k => ?_⟩
  · simp [initWeight, hb]
  · by_cases h : Q.read b = k
    · simpa [initWeight, h] using div_nonneg (hQ.2.1 b) (le_of_lt (hP k))
    · simp [initWeight, h]
  · have hfil : ∑ b, initWeight Q k b
        = ∑ b ∈ univ.filter (fun b => Q.read b = k), Q.init b / Q.rootMass k := by
      rw [Finset.sum_filter]
      rfl
    rw [hfil, ← Finset.sum_div]
    exact div_self (ne_of_gt (hP k))

/-- **C1, second statement.** -/
theorem uniformWeight_admissible (Q : QfbData V) [Nonempty V] (h : ∀ k, ∃ b, Q.read b = k) :
    Admissible Q (uniformWeight Q) := by
  refine ⟨fun k b hb => ?_, fun k b => ?_, fun k => ?_⟩
  · simp [uniformWeight, hb]
  · by_cases hb : Q.read b = k
    · simp only [uniformWeight, if_pos hb]
      positivity
    · simp [uniformWeight, hb]
  · obtain ⟨b₀, hb₀⟩ := h k
    have hmem : b₀ ∈ univ.filter (fun c => Q.read c = k) := by simp [hb₀]
    have hcard : ((univ.filter (fun c => Q.read c = k)).card : ℝ) ≠ 0 := by
      have : 0 < (univ.filter (fun c => Q.read c = k)).card :=
        Finset.card_pos.mpr ⟨b₀, hmem⟩
      positivity
    have hfil : ∑ b, uniformWeight Q k b
        = ∑ _b ∈ univ.filter (fun b => Q.read b = k),
            (1 : ℝ) / (univ.filter (fun c => Q.read c = k)).card := by
      rw [Finset.sum_filter]
      rfl
    rw [hfil, Finset.sum_const, nsmul_eq_mul]
    field_simp

/-- **C1, third statement.**  This is where the sign clause of `Admissible` is load-bearing: support
and normalization alone force the row *sums*, while each *entry* is only an affine combination of
the fibre's visible rows. -/
theorem candidateOf_isRowStochastic (Q : QfbData V) (hQ : Q.IsLaw) (μ : FibreWeight Q)
    (hμ : Admissible Q μ) (n : ℕ) : IsRowStochastic (candidateOf Q μ n) := by
  constructor
  · intro k j
    exact Finset.sum_nonneg fun b _ => Finset.sum_nonneg fun b' _ =>
      mul_nonneg (hμ.2.1 k b) (bornPow_nonneg Q n b b')
  · intro k
    have hswap : ∀ j : V, candidateOf Q μ n k j
        = ∑ b ∈ univ.filter (fun b => Q.read b = k),
            ∑ b' ∈ univ.filter (fun b' => Q.read b' = j), μ k b * Q.bornPow n b b' := fun _ => rfl
    calc ∑ j, candidateOf Q μ n k j
        = ∑ j, ∑ b ∈ univ.filter (fun b => Q.read b = k),
            ∑ b' ∈ univ.filter (fun b' => Q.read b' = j), μ k b * Q.bornPow n b b' := by
          exact Finset.sum_congr rfl fun j _ => hswap j
      _ = ∑ b ∈ univ.filter (fun b => Q.read b = k),
            ∑ j, ∑ b' ∈ univ.filter (fun b' => Q.read b' = j), μ k b * Q.bornPow n b b' :=
          Finset.sum_comm
      _ = ∑ b ∈ univ.filter (fun b => Q.read b = k), μ k b := by
          refine Finset.sum_congr rfl fun b _ => ?_
          rw [Finset.sum_fiberwise (s := (univ : Finset Q.Bas)) (g := fun b' => Q.read b')
            (f := fun b' => μ k b * Q.bornPow n b b')]
          rw [← Finset.mul_sum, Q.sum_bornPow hQ.1 n b, mul_one]
      _ = 1 := sum_fibre_of_admissible hμ k

/-! ### C2 — the decisive question: must the two rules agree?

The witness holds the representation **fixed**: no appeal to representation freedom is made or
needed.  Visible carrier `Fin 2`, basis `Fin 3`, and the fibre over the visible value `0` carries
the two basis points `0` and `1`, which the evolution sends to different visible values and on which
the initial law is unequal.  Both requirements are necessary — on a one-point visible carrier the
single entry of `candidateOf` *is* the row sum, hence `1` for every admissible weight. -/

/-- **C2.**  The two named rules differ on one lawful representation, with the representation held
fixed.  This is what makes underdetermination a theorem rather than an audit observation.

The witness is constructed **inside this proof** rather than named at top level, so that the round
introduces exactly the eight definitions the freeze fixes and no others. -/
theorem candidate_rules_disagree :
    ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (Q : QfbData V) (n : ℕ),
      Q.IsLaw ∧ Q.PositiveRootMass
      ∧ candidateOf Q (initWeight Q) n ≠ candidateOf Q (uniformWeight Q) n := by
  classical
  -- Visible carrier `Fin 2`, basis `Fin 3`.  The fibre over the visible value `0` carries basis
  -- points `0` and `1`; the evolution is the transposition exchanging basis points `1` and `2`, so
  -- it fixes point `0` inside that fibre and moves point `1` out of it, giving the two points
  -- different visible rows.  The initial law weights them unequally.
  set Q : QfbData (Fin 2) :=
    { Bas := Fin 3
      fB := inferInstance
      dB := inferInstance
      U := !![1, 0, 0; 0, 0, 1; 0, 1, 0]
      init := fun b => if b = 0 then 1 / 2 else 1 / 4
      read := fun b => if b = 2 then 1 else 0 } with hQdef
  have hread : ∀ b : Fin 3, Q.read b = (if b = 2 then 1 else 0 : Fin 2) := fun _ => rfl
  have hinit : ∀ b : Fin 3, Q.init b = (if b = 0 then 1 / 2 else 1 / 4 : ℝ) := fun _ => rfl
  have hborn : ∀ b b' : Fin 3, Q.born b b'
      = ‖(!![1, 0, 0; 0, 0, 1; 0, 1, 0] : Matrix (Fin 3) (Fin 3) ℂ) b' b‖ ^ 2 := fun _ _ => rfl
  -- the fibre over the visible value `0`
  have hfib0 : (univ.filter (fun c : Fin 3 => Q.read c = 0)) = ({0, 1} : Finset (Fin 3)) := by
    ext b
    fin_cases b <;> simp [hread]
  have hlaw : Q.IsLaw := by
    refine ⟨?_, fun b => ?_, ?_⟩
    · show (!![1, 0, 0; 0, 0, 1; 0, 1, 0] : Matrix (Fin 3) (Fin 3) ℂ)
        ∈ Matrix.unitaryGroup (Fin 3) ℂ
      rw [Matrix.mem_unitaryGroup_iff]
      ext i j
      fin_cases i <;> fin_cases j <;>
        simp [Matrix.mul_apply, Fin.sum_univ_three, Matrix.conjTranspose_apply, Matrix.one_apply]
    · rw [hinit b]; split <;> norm_num
    · show (∑ b : Fin 3, Q.init b) = 1
      rw [Fin.sum_univ_three, hinit 0, hinit 1, hinit 2]
      norm_num [Fin.ext_iff]
  have hrm0 : Q.rootMass 0 = 3 / 4 := by
    show (∑ b ∈ univ.filter (fun b : Fin 3 => Q.read b = 0), Q.init b) = 3 / 4
    rw [hfib0, Finset.sum_pair (by decide : (0 : Fin 3) ≠ 1), hinit 0, hinit 1]
    norm_num
  have hrm1 : Q.rootMass 1 = 1 / 4 := by
    show (∑ b ∈ univ.filter (fun b : Fin 3 => Q.read b = 1), Q.init b) = 1 / 4
    have h1 : (univ.filter (fun c : Fin 3 => Q.read c = 1)) = ({2} : Finset (Fin 3)) := by
      ext b
      fin_cases b <;> simp [hread]
    rw [h1, Finset.sum_singleton, hinit 2, if_neg (by decide : ¬ (2 : Fin 3) = 0)]
  have hpos : Q.PositiveRootMass := by
    intro a
    fin_cases a
    · show (0 : ℝ) < Q.rootMass 0
      rw [hrm0]; norm_num
    · show (0 : ℝ) < Q.rootMass 1
      rw [hrm1]; norm_num
  -- at one elapsed step the `(0,0)` entry reads the rule off at basis point `0` alone
  have hentry : ∀ μ : FibreWeight Q, candidateOf Q μ 1 0 0 = μ 0 (0 : Fin 3) := by
    intro μ
    show (∑ b ∈ univ.filter (fun b : Fin 3 => Q.read b = 0),
            ∑ b' ∈ univ.filter (fun b' : Fin 3 => Q.read b' = 0),
              μ 0 b * Q.bornPow 1 b b') = μ 0 (0 : Fin 3)
    have hb : ∀ b b' : Fin 3, Q.bornPow 1 b b'
        = ‖(!![1, 0, 0; 0, 0, 1; 0, 1, 0] : Matrix (Fin 3) (Fin 3) ℂ) b' b‖ ^ 2 := fun b b' =>
      (bornPow_one Q b b').trans (hborn b b')
    simp only [Finset.sum_filter, hb, hread]
    rw [Fin.sum_univ_three]
    simp only [Fin.sum_univ_three]
    norm_num [Fin.ext_iff]
  have hiw : initWeight Q 0 (0 : Fin 3) = 2 / 3 := by
    show (if Q.read 0 = 0 then Q.init 0 / Q.rootMass 0 else 0) = 2 / 3
    rw [if_pos (by rw [hread 0]; decide), hrm0, hinit 0]
    norm_num
  have huw : uniformWeight Q 0 (0 : Fin 3) = 1 / 2 := by
    show (if Q.read 0 = 0
            then 1 / ((univ.filter (fun c : Fin 3 => Q.read c = 0)).card : ℝ) else 0) = 1 / 2
    rw [if_pos (by rw [hread 0]; decide), hfib0]
    norm_num
  refine ⟨Fin 2, inferInstance, inferInstance, Q, 1, hlaw, hpos, fun hcontra => ?_⟩
  have h00 := congrFun (congrFun hcontra 0) 0
  rw [hentry (initWeight Q), hentry (uniformWeight Q), hiw, huw] at h00
  norm_num at h00

/-! ### C3 — the subsidiary padding theorems, at exact scope

The first is essentially definitional and is stated so that the second is seen not to be.  The
second is the real content: the ancilla marginalizes away despite `padData` multiplying every fibre
by `Anc`.  Because it is stated at general `n`, the merged route it consumes is the general-horizon
one — `padData_bornPow` for the factorization at every horizon and `sum_ancPow` for the ancilla
marginal being one at every step.  The one-step `padData_born` and `sum_ancBorn` are the ingredients
those two are proved from, not the theorems applied here. -/

/-- **C3, first statement.**  The init-weighted candidate *is* the rooted family. -/
theorem candidateOf_initWeight_eq_rooted (Q : QfbData V) (hQ : Q.IsLaw) (hP : Q.PositiveRootMass)
    (n : ℕ) (k j : V) : candidateOf Q (initWeight Q) n k j = Q.rooted n k j := by
  have hiw : ∀ b, Q.read b = k → initWeight Q k b = Q.init b / Q.rootMass k := by
    intro b hb
    show (if Q.read b = k then Q.init b / Q.rootMass k else 0) = Q.init b / Q.rootMass k
    exact if_pos hb
  show (∑ b ∈ univ.filter (fun b => Q.read b = k),
          ∑ b' ∈ univ.filter (fun b' => Q.read b' = j),
            initWeight Q k b * Q.bornPow n b b')
      = (∑ b ∈ univ.filter (fun b => Q.read b = k),
          ∑ b' ∈ univ.filter (fun b' => Q.read b' = j), Q.init b * Q.bornPow n b b')
        / Q.rootMass k
  rw [Finset.sum_div]
  refine Finset.sum_congr rfl fun b hb => ?_
  have hbk : Q.read b = k := by simpa using hb
  rw [Finset.sum_div]
  refine Finset.sum_congr rfl fun b' _ => ?_
  rw [hiw b hbk]
  ring

/-- **C3, second statement.**  The uniform-on-fibre rule is padding-invariant.  `padData` multiplies
every visible fibre by `Anc`, so the uniform weight really does change; the candidate does not,
because the ancilla factor marginalizes to one at every horizon. -/
theorem candidateOf_uniformWeight_padData_eq (Q : QfbData V) (Anc : Type) [Fintype Anc]
    [DecidableEq Anc] [Nonempty Anc] (W : Matrix Anc Anc ℂ) (hW : W ∈ Matrix.unitaryGroup Anc ℂ)
    (w : Anc → ℝ) (n : ℕ) (k j : V) :
    candidateOf (padData Q Anc W w) (uniformWeight _) n k j
      = candidateOf Q (uniformWeight Q) n k j := by
  have hcard : (0 : ℝ) < (univ : Finset Anc).card := by
    have : 0 < (univ : Finset Anc).card := Finset.card_pos.mpr univ_nonempty
    exact_mod_cast this
  have hAnc : ((univ : Finset Anc).card : ℝ) ≠ 0 := ne_of_gt hcard
  have hfib : ∀ v : V, (univ.filter (fun p : Q.Bas × Anc => Q.read p.1 = v))
      = (univ.filter (fun b => Q.read b = v)) ×ˢ (univ : Finset Anc) := by
    intro v
    ext ⟨b, x⟩
    simp
  show (∑ p ∈ univ.filter (fun p : Q.Bas × Anc => Q.read p.1 = k),
          ∑ q ∈ univ.filter (fun q : Q.Bas × Anc => Q.read q.1 = j),
            uniformWeight (padData Q Anc W w) k p * (padData Q Anc W w).bornPow n p q)
       = ∑ b ∈ univ.filter (fun b => Q.read b = k),
           ∑ b' ∈ univ.filter (fun b' => Q.read b' = j),
             uniformWeight Q k b * Q.bornPow n b b'
  rw [hfib k, hfib j, Finset.sum_product]
  refine Finset.sum_congr rfl fun b hb => ?_
  have hbk : Q.read b = k := by simpa using hb
  have hpw : ∀ x : Anc, uniformWeight (padData Q Anc W w) k (b, x)
      = 1 / (((univ.filter (fun c => Q.read c = k)).card : ℝ)
              * ((univ : Finset Anc).card : ℝ)) := by
    intro x
    show (if Q.read b = k
            then 1 / ((univ.filter (fun c : Q.Bas × Anc => Q.read c.1 = k)).card : ℝ)
            else 0) = _
    rw [if_pos hbk, hfib k, Finset.card_product]
    push_cast
    ring
  have hqw : uniformWeight Q k b
      = 1 / ((univ.filter (fun c => Q.read c = k)).card : ℝ) := if_pos hbk
  -- collapse the ancilla on the target side, then count the ancilla on the source side
  have hinner : ∀ x : Anc,
      (∑ q ∈ (univ.filter (fun b' => Q.read b' = j)) ×ˢ (univ : Finset Anc),
          uniformWeight (padData Q Anc W w) k (b, x) * (padData Q Anc W w).bornPow n (b, x) q)
        = ∑ b' ∈ univ.filter (fun b' => Q.read b' = j),
            (1 / (((univ.filter (fun c => Q.read c = k)).card : ℝ)
                    * ((univ : Finset Anc).card : ℝ))) * Q.bornPow n b b' := by
    intro x
    rw [Finset.sum_product]
    refine Finset.sum_congr rfl fun b' _ => ?_
    have hfac : ∀ x' : Anc, uniformWeight (padData Q Anc W w) k (b, x)
        * (padData Q Anc W w).bornPow n (b, x) (b', x')
        = (1 / (((univ.filter (fun c => Q.read c = k)).card : ℝ)
                  * ((univ : Finset Anc).card : ℝ)))
          * Q.bornPow n b b' * ancPow W n x x' := by
      intro x'
      rw [hpw x, padData_bornPow Q W w n b b' x x']
      ring
    rw [Finset.sum_congr rfl fun x' _ => hfac x', ← Finset.mul_sum, sum_ancPow hW n x, mul_one]
  -- the summand no longer mentions the ancilla index, so the source-side ancilla is a plain count
  have hFk : ((univ.filter (fun c => Q.read c = k)).card : ℝ) ≠ 0 := by
    have : 0 < (univ.filter (fun c => Q.read c = k)).card := Finset.card_pos.mpr ⟨b, hb⟩
    positivity
  rw [Finset.sum_congr rfl fun x _ => hinner x, Finset.sum_const, nsmul_eq_mul,
    Finset.mul_sum, hqw]
  refine Finset.sum_congr rfl fun b' _ => ?_
  field_simp

/-! ### C4 — do the admissibility conditions force uniqueness?

Both competing propositions are frozen; the execution contract is that if C4 closes, exactly one of
the two theorem statements appears here, and under `CU4` neither would.  C2 closes, and C1 makes
both named rules admissible, so the C2 witness instantiates the existential directly: it is
`AdmissibleNonUnique` that is proved, and `AdmissibleAgree` is stated but asserted by nothing. -/

/-- NON-UNIQUENESS.  Some lawful representation carries two admissible weights whose induced visible
candidates differ at some elapsed time. -/
def AdmissibleNonUnique : Prop :=
  ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (Q : QfbData V) (μ ν : FibreWeight Q) (n : ℕ),
    Q.IsLaw ∧ Q.PositiveRootMass ∧ Admissible Q μ ∧ Admissible Q ν
    ∧ candidateOf Q μ n ≠ candidateOf Q ν n

/-- UNIVERSAL AGREEMENT.  On every lawful representation, any two admissible weights induce the same
visible candidate at every elapsed time. -/
def AdmissibleAgree : Prop :=
  ∀ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (Q : QfbData V) (μ ν : FibreWeight Q) (n : ℕ),
    Q.IsLaw → Q.PositiveRootMass → Admissible Q μ → Admissible Q ν →
    candidateOf Q μ n = candidateOf Q ν n

/-- **C4.**  The admissibility conditions do **not** force uniqueness.

Proved **from C2 and C1**, not by re-instantiating the witness. The freeze says the C2 witness
instantiates C4's existential directly; this is that sentence as a derivation rather than as prose.
Two side facts are needed and both come from C2's own payload: the visible carrier is inhabited
because over an empty carrier every matrix equals every other, so the two candidates could not
differ; and every fibre is inhabited because `rootMass` is a sum over that fibre and
`PositiveRootMass` makes it positive. -/
theorem admissible_nonUnique : AdmissibleNonUnique := by
  obtain ⟨V, hV, hDV, Q, n, hQ, hP, hne⟩ := candidate_rules_disagree
  have hVne : Nonempty V := by
    rcases isEmpty_or_nonempty V with _ | h
    · exact absurd (funext fun i => (IsEmpty.false i).elim) hne
    · exact h
  have hfib : ∀ k, ∃ b, Q.read b = k := by
    intro k
    by_contra hno
    push_neg at hno
    have hempty : (univ.filter (fun b => Q.read b = k)) = ∅ := by
      ext b
      simp [hno b]
    have hzero : Q.rootMass k = 0 := by
      show (∑ b ∈ univ.filter (fun b => Q.read b = k), Q.init b) = 0
      rw [hempty, Finset.sum_empty]
    exact absurd hzero (ne_of_gt (hP k))
  exact ⟨V, hV, hDV, Q, initWeight Q, uniformWeight Q, n, hQ, hP,
    initWeight_admissible Q hQ hP, uniformWeight_admissible Q hfib, hne⟩

/-! ### What these proofs rest on

Printed at build time so the kernel's own answer, not a claim in a comment, is what the log carries.
`sorryAx` in any of these lines would mean a hole. -/

#print axioms OIBridge.CandidateSelection.initWeight_admissible
#print axioms OIBridge.CandidateSelection.uniformWeight_admissible
#print axioms OIBridge.CandidateSelection.candidateOf_isRowStochastic
#print axioms OIBridge.CandidateSelection.candidate_rules_disagree
#print axioms OIBridge.CandidateSelection.candidateOf_initWeight_eq_rooted
#print axioms OIBridge.CandidateSelection.candidateOf_uniformWeight_padData_eq
#print axioms OIBridge.CandidateSelection.admissible_nonUnique

end CandidateSelection

end OIBridge
