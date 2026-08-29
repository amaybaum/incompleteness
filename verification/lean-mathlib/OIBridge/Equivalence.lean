/-
  OIBridge/Equivalence.lean — [Main] §3.4's finite-horizon stochastic–reversible–unitary
  equivalence, the centrepiece of the coverage backlog's Tier 1.

      Fix a finite visible alphabet and a finite accessible horizon K. The following three
      classes of finite-horizon observable law P(x_0, …, x_K) coincide:

        (S)    the finite stochastic laws;
        (D)    the visible marginals of finite reversible deterministic systems under
               incomplete observation;
        (Q_fb) the laws realizable by finite-dimensional unitary systems with Born-rule
               readout in a fixed basis.

  THREE CONSTRUCTIONS AND A WRAPPER. `S_imp_D`, `D_imp_Qfb` and `Qfb_imp_S` are proved
  separately, and `finite_horizon_equivalence` assembles them. The wrapper takes NONE of the three
  as a hypothesis — it would then encode the theorem rather than prove it.

  TWO SCOPE GUARDS, stated here because both are easy to blur.

  * HIDDEN PREDICTIVE MEMORY IS NOT AN ASSUMPTION OR A LEMMA OF THIS THEOREM. The equivalence is
    EXISTENTIAL and its classes include Markov laws; `OIBridge/HiddenMemory.lean` is UNIVERSAL over
    realizations and discriminates the readback sector afterwards. Neither is a lemma of the other
    and the manuscript is explicit about the separation.
  * THE ONE-STEP ANCILLA DILATION DOES NOT PROVE `S → D`. `EquivalenceChain.dilation_isometry` and
    its companions are a one-step representation result. `S → D` needs a MULTI-TIME carrier
    reproducing the whole joint law `P(x_0, …, x_K)`, and it is constructed here from scratch.

  A THIRD DISTINCTION, recorded rather than silently decided. The manuscript's PROOF of
  `D → Q_fb` remarks that `U_φ = e^{-iĤ}` for Hermitian `Ĥ`, giving a fixed autonomous generator at
  integer times. That is a property of the constructed representation, not a clause of the class
  `Q_fb` as the theorem states it — the class asks for a finite-dimensional unitary system with
  fixed-basis Born readout, nothing more. `Qfb` below is therefore defined WITHOUT an
  autonomous-generator clause, and the Hermitian-logarithm statement is left unformalized. If a
  later round widens the class definition, this is the line that has to change with it.

  `S → D` follows the two-step route: an INJECTIVE SUPPORTED dynamics is built first, and
  `exists_perm_extending` — an injective partial map on a finite type extends to a permutation —
  turns it into a global bijection. That lemma is stated on its own because it is reusable well
  beyond this theorem.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.EquivalenceChain
import OIBridge.FiniteEntropy

namespace OIBridge

namespace Equivalence

open Finset Matrix OIBridge.FiniteEntropy

set_option linter.unusedSectionVars false

/-! ### The padding lemma

An injective partial map on a finite type extends to a permutation of it. This is what turns a
"supported dynamics" — defined and injective only where the prior lives — into the REVERSIBLE
system class `(D)` demands, and it is the reusable half of the `S → D` construction. -/

theorem exists_perm_extending {A : Type*} [Fintype A] [DecidableEq A] (s : Finset A)
    (g : A → A) (hg : Set.InjOn g ↑s) : ∃ σ : Equiv.Perm A, ∀ a ∈ s, σ a = g a := by
  classical
  set t : Finset A := s.image g with ht
  have hcard : t.card = s.card := Finset.card_image_of_injOn hg
  have hcompl : (sᶜ : Finset A).card = (tᶜ : Finset A).card := by
    rw [Finset.card_compl, Finset.card_compl, hcard]
  have hce : Fintype.card {a // a ∈ (sᶜ : Finset A)} = Fintype.card {a // a ∈ (tᶜ : Finset A)} := by
    rw [Fintype.card_coe, Fintype.card_coe]
    exact hcompl
  obtain ⟨e⟩ : Nonempty ({a // a ∈ (sᶜ : Finset A)} ≃ {a // a ∈ (tᶜ : Finset A)}) :=
    ⟨Fintype.equivOfCardEq hce⟩
  set f : A → A := fun a => if h : a ∈ s then g a else (e ⟨a, by simpa using h⟩ : A) with hf
  have hmem_t : ∀ a ∈ s, f a ∈ t := by
    intro a ha; simp only [hf, dif_pos ha, ht]
    exact Finset.mem_image_of_mem g ha
  have hmem_tc : ∀ a, a ∉ s → f a ∉ t := by
    intro a ha
    simp only [hf, dif_neg ha]
    exact Finset.mem_compl.1 (e ⟨a, by simpa using ha⟩).2
  have hinj : Function.Injective f := by
    intro a b hab
    by_cases hA : a ∈ s <;> by_cases hB : b ∈ s
    · exact hg hA hB (by simpa [hf, dif_pos hA, dif_pos hB] using hab)
    · exact absurd (hab ▸ hmem_t a hA) (hmem_tc b hB)
    · exact absurd (hab ▸ hmem_tc a hA) (by simpa using hmem_t b hB)
    · have : e ⟨a, by simpa using hA⟩ = e ⟨b, by simpa using hB⟩ := by
        apply Subtype.ext
        simpa [hf, dif_neg hA, dif_neg hB] using hab
      simpa using congrArg Subtype.val (e.injective this)
  refine ⟨Equiv.ofBijective f (Finite.injective_iff_bijective.1 hinj), fun a ha => ?_⟩
  simp [Equiv.ofBijective, hf, dif_pos ha]

/-! ### The chain-normalisation lemma

A stochastic transition family and an initial distribution give trajectory weights that sum to
one. This is what makes `Q_fb → S` a theorem rather than a definition unfolding: the Born weights
must be SHOWN to be a probability law on trajectories, not declared to be one. -/

theorem sum_chain {S : Type*} [Fintype S] [DecidableEq S] (T : S → S → ℝ)
    (hT : ∀ s, ∑ s', T s s' = 1) (init : S → ℝ) (hi : ∑ s, init s = 1) :
    ∀ n : ℕ, ∑ σ : Fin (n + 1) → S,
      init (σ 0) * ∏ k : Fin n, T (σ k.castSucc) (σ k.succ) = 1 := by
  intro n
  induction n with
  | zero =>
      simpa using
        (Fintype.sum_equiv (Equiv.funUnique (Fin 1) S)
          (fun σ : Fin 1 → S => init (σ 0) * ∏ k : Fin 0, T (σ k.castSucc) (σ k.succ))
          (fun s => init s) (by intro σ; simp)).trans hi
  | succ m ih =>
      rw [← Equiv.sum_comp (Fin.snocEquiv (fun _ : Fin (m + 2) => S))
        (fun σ : Fin (m + 2) → S => init (σ 0) * ∏ k : Fin (m + 1), T (σ k.castSucc) (σ k.succ))]
      have hterm : ∀ q : S × (Fin (m + 1) → S),
          (fun σ : Fin (m + 2) → S => init (σ 0) * ∏ k : Fin (m + 1), T (σ k.castSucc) (σ k.succ))
            (Fin.snocEquiv (fun _ : Fin (m + 2) => S) q)
          = (init (q.2 0) * ∏ k : Fin m, T (q.2 k.castSucc) (q.2 k.succ))
              * T (q.2 (Fin.last m)) q.1 := by
        rintro ⟨y, σ'⟩
        have h0 : (Fin.snoc σ' y : Fin (m + 2) → S) 0 = σ' 0 := by
          rw [show (0 : Fin (m + 2)) = (0 : Fin (m + 1)).castSucc from rfl, Fin.snoc_castSucc]
        simp only [Fin.snocEquiv_apply, Fin.prod_univ_castSucc, Fin.snoc_castSucc,
          Fin.succ_castSucc, Fin.succ_last, Fin.snoc_last, h0]
        ring
      rw [Finset.sum_congr rfl fun q _ => hterm q, Fintype.sum_prod_type_right]
      have hin : ∀ σ' : Fin (m + 1) → S,
          ∑ y : S, (init (σ' 0) * ∏ k : Fin m, T (σ' k.castSucc) (σ' k.succ))
              * T (σ' (Fin.last m)) y
          = init (σ' 0) * ∏ k : Fin m, T (σ' k.castSucc) (σ' k.succ) := by
        intro σ'
        rw [← Finset.mul_sum, hT, mul_one]
      rw [Finset.sum_congr rfl fun σ' _ => hin σ']
      exact ih

/-! ### The three classes

Each is a genuine predicate on finite-horizon trajectory laws, and none of them is defined in terms
of another. -/

universe u

variable {V : Type u} [Fintype V] [DecidableEq V]

/-- Finite-horizon visible trajectories `x_0, …, x_K`. -/
abbrev Traj (V : Type*) (K : ℕ) := Fin (K + 1) → V

/-- **(S)** the finite stochastic laws. -/
def Stochastic {K : ℕ} (P : Traj V K → ℝ) : Prop :=
  (∀ τ, 0 ≤ P τ) ∧ ∑ τ, P τ = 1

/-- **(D)** a finite reversible deterministic system under incomplete observation: a bijection of
`C_V × C_H` with an initial law, observed through the visible factor.

The initial law is a datum of the system and is not required to factor as
`visible prior × hidden prior`. That STRONGER form — a hidden prior independent of the visible
initial state — is the manuscript's separate finite-horizon process-dilation theorem, proved there
by the response-table construction, and it is NOT what this theorem's class `(D)` asks for. -/
structure RevReal (V : Type u) (K : ℕ) : Type (u + 1) where
  Hid : Type u
  fH : Fintype Hid
  dH : DecidableEq Hid
  step : (V × Hid) ≃ (V × Hid)
  init : V × Hid → ℝ

attribute [instance] RevReal.fH RevReal.dH

/-- The initial datum is a probability law. Carried as a predicate rather than a structure field
because the sum needs the `Fintype` instance the structure itself supplies. -/
def RevReal.IsLaw {K : ℕ} (R : RevReal V K) : Prop :=
  (∀ s, 0 ≤ R.init s) ∧ ∑ s, R.init s = 1

/-- The state trajectory generated by iterating the bijection. -/
def RevReal.states {K : ℕ} (R : RevReal V K) (s : V × R.Hid) : Fin (K + 1) → V × R.Hid :=
  fun k => R.step^[(k : ℕ)] s

/-- The visible trajectory: the state trajectory read through the visible factor. -/
def RevReal.traj {K : ℕ} (R : RevReal V K) (s : V × R.Hid) : Traj V K :=
  fun k => (R.states s k).1

/-- The observed law: the pushforward of the initial law along the visible trajectory. -/
noncomputable def RevReal.law {K : ℕ} (R : RevReal V K) : Traj V K → ℝ := marg R.init R.traj

def RevRealizable {K : ℕ} (P : Traj V K → ℝ) : Prop :=
  ∃ R : RevReal V K, R.IsLaw ∧ R.law = P

/-- **(Q_fb)** a finite-dimensional unitary system with Born-rule readout in a fixed basis.

No autonomous-generator clause: the class as the theorem states it asks for a unitary and a fixed
basis, and the manuscript's `U = e^{-iĤ}` remark is a property of the construction rather than a
membership condition. -/
structure QfbReal (V : Type u) (K : ℕ) : Type (u + 1) where
  Bas : Type u
  fB : Fintype Bas
  dB : DecidableEq Bas
  U : Matrix Bas Bas ℂ
  init : Bas → ℝ
  read : Bas → V

attribute [instance] QfbReal.fB QfbReal.dB

/-- Unitarity of the evolution and normalisation of the initial law. -/
def QfbReal.IsLaw {K : ℕ} (Q : QfbReal V K) : Prop :=
  Q.U ∈ Matrix.unitaryGroup Q.Bas ℂ ∧ (∀ b, 0 ≤ Q.init b) ∧ ∑ b, Q.init b = 1

/-- The Born weight of the fixed-basis outcome `b'` one step after `b`. -/
noncomputable def QfbReal.born {K : ℕ} (Q : QfbReal V K) (b b' : Q.Bas) : ℝ := ‖Q.U b' b‖ ^ 2

/-- The record of a projective fixed-basis measurement at EVERY step, with collapse: the
trajectory weight is the initial weight times the Born weights along the way. -/
noncomputable def QfbReal.chain {K : ℕ} (Q : QfbReal V K) (σ : Fin (K + 1) → Q.Bas) : ℝ :=
  Q.init (σ 0) * ∏ k : Fin K, Q.born (σ k.castSucc) (σ k.succ)

/-- The observed law: the record, read through the fixed basis. -/
noncomputable def QfbReal.law {K : ℕ} (Q : QfbReal V K) : Traj V K → ℝ :=
  marg Q.chain (fun σ => fun k => Q.read (σ k))

def QfbRealizable {K : ℕ} (P : Traj V K → ℝ) : Prop :=
  ∃ Q : QfbReal V K, Q.IsLaw ∧ Q.law = P

/-! ### `Q_fb → S`: the Born weights are a stochastic law

Not a definitional unfolding. Nonnegativity is immediate, but normalisation is unitarity: the
columns of `U` are unit vectors, which is what makes each Born row sum to one. -/

theorem QfbReal.born_nonneg {K : ℕ} (Q : QfbReal V K) (b b' : Q.Bas) : 0 ≤ Q.born b b' :=
  sq_nonneg _

theorem QfbReal.sum_born {K : ℕ} (Q : QfbReal V K) (hU : Q.U ∈ Matrix.unitaryGroup Q.Bas ℂ)
    (b : Q.Bas) : ∑ b', Q.born b b' = 1 := by
  have h := Matrix.mem_unitaryGroup_iff'.1 hU
  have hbb := congrFun (congrFun h b) b
  rw [Matrix.mul_apply, Matrix.one_apply_eq] at hbb
  have hterm : ∀ r : Q.Bas, (star Q.U) b r * Q.U r b = ((‖Q.U r b‖ ^ 2 : ℝ) : ℂ) := by
    intro r
    rw [Matrix.star_eq_conjTranspose, Matrix.conjTranspose_apply, mul_comm,
      RCLike.star_def, Complex.mul_conj]
    norm_cast
    exact Complex.normSq_eq_norm_sq _
  rw [Finset.sum_congr rfl fun r _ => hterm r, ← Complex.ofReal_sum] at hbb
  exact_mod_cast hbb

theorem QfbReal.chain_nonneg {K : ℕ} (Q : QfbReal V K) (hi : ∀ b, 0 ≤ Q.init b)
    (σ : Fin (K + 1) → Q.Bas) : 0 ≤ Q.chain σ :=
  mul_nonneg (hi _) (Finset.prod_nonneg fun _ _ => Q.born_nonneg _ _)

theorem Qfb_imp_S {K : ℕ} (P : Traj V K → ℝ) (h : QfbRealizable P) : Stochastic P := by
  obtain ⟨Q, ⟨hU, hin, htot⟩, rfl⟩ := h
  refine ⟨fun τ => marg_nonneg (fun σ => Q.chain_nonneg hin σ) _ τ, ?_⟩
  rw [QfbReal.law, sum_marg]
  exact sum_chain Q.born (Q.sum_born hU) Q.init htot K

/-! ### `D → Q_fb`: the permutation unitary, and why the measurements do not disturb

Rank 2 of the backlog gives the permutation unitary and rank 3 gives diagonal preservation. What
is added here is the MULTI-TIME statement: repeated fixed-basis measurements reproduce the whole
trajectory distribution, not merely the one-step marginals. The Born weights of a permutation
matrix are an INDICATOR, so the measured chain is concentrated on the deterministic orbit — which
is exactly "the measurements do not disturb the state", in the form the multi-time claim needs. -/

theorem marg_id {α : Type*} [Fintype α] [DecidableEq α] (P : α → ℝ) : marg P id = P := by
  classical
  funext a
  rw [marg, show (univ.filter fun a' : α => id a' = a) = {a} by
    ext a'; simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton, id_eq],
    Finset.sum_singleton]

theorem RevReal.states_iff {K : ℕ} (R : RevReal V K) (σ : Fin (K + 1) → V × R.Hid) :
    (∀ k : Fin K, σ k.succ = R.step (σ k.castSucc)) ↔ R.states (σ 0) = σ := by
  constructor
  · intro h
    have key : ∀ j : ℕ, ∀ hj : j < K + 1, R.step^[j] (σ 0) = σ ⟨j, hj⟩ := by
      intro j
      induction j with
      | zero => intro hj; simp
      | succ i ih =>
          intro hj
          have hi : i < K + 1 := Nat.lt_of_succ_lt hj
          have hiK : i < K := Nat.lt_of_succ_lt_succ hj
          rw [Function.iterate_succ_apply', ih hi]
          have hk := h ⟨i, hiK⟩
          have e1 : (⟨i, hiK⟩ : Fin K).castSucc = (⟨i, hi⟩ : Fin (K + 1)) := rfl
          have e2 : (⟨i, hiK⟩ : Fin K).succ = (⟨i + 1, hj⟩ : Fin (K + 1)) := rfl
          rw [e1, e2] at hk
          exact hk.symm
    funext k
    have hk := key (k : ℕ) k.2
    simpa [RevReal.states] using hk
  · intro h k
    have h1 : σ k.succ = R.step^[((k : ℕ) + 1)] (σ 0) := by
      rw [← h]; rfl
    have h2 : σ k.castSucc = R.step^[(k : ℕ)] (σ 0) := by
      rw [← h]; rfl
    rw [h1, h2, Function.iterate_succ_apply']

theorem D_imp_Qfb {K : ℕ} (P : Traj V K → ℝ) (h : RevRealizable P) : QfbRealizable P := by
  classical
  obtain ⟨R, ⟨hn, ht⟩, rfl⟩ := h
  let Q : QfbReal V K :=
    { Bas := V × R.Hid, fB := inferInstance, dB := inferInstance,
      U := Equiv.Perm.permMatrix ℂ R.step.symm, init := R.init, read := Prod.fst }
  -- the Born weights of a permutation matrix are the indicator of the deterministic step:
  -- this is "the measurements do not disturb the state", in the form the multi-time claim needs
  have hborn : ∀ b b' : Q.Bas, Q.born b b' = if b' = R.step b then 1 else 0 := by
    intro b b'
    have hU : Q.U b' b = if b = R.step.symm b' then 1 else 0 := by
      simp [Q, Equiv.Perm.permMatrix, PEquiv.toMatrix_apply, Equiv.toPEquiv_apply, eq_comm]
    have hiff : (b = R.step.symm b') ↔ (b' = R.step b) :=
      ⟨fun hb => by rw [hb]; simp, fun hb => by rw [hb]; simp⟩
    rw [QfbReal.born, hU]
    by_cases hc : b' = R.step b
    · rw [if_pos (hiff.2 hc), if_pos hc]; simp
    · rw [if_neg (fun hx => hc (hiff.1 hx)), if_neg hc]; simp
  have hchain : Q.chain = marg R.init R.states := by
    funext σ
    have hprod : (∏ k : Fin K, Q.born (σ k.castSucc) (σ k.succ))
        = if R.states (σ 0) = σ then 1 else 0 := by
      by_cases hc : ∀ k : Fin K, σ k.succ = R.step (σ k.castSucc)
      · rw [if_pos ((R.states_iff σ).1 hc)]
        exact Finset.prod_eq_one fun k _ => by rw [hborn, if_pos (hc k)]
      · rw [if_neg (fun hx => hc ((R.states_iff σ).2 hx))]
        obtain ⟨k, hk⟩ := not_forall.1 hc
        exact Finset.prod_eq_zero (Finset.mem_univ k) (by rw [hborn, if_neg hk])
    rw [QfbReal.chain, hprod]
    by_cases hc : R.states (σ 0) = σ
    · have hfil : (Finset.univ.filter fun s => R.states s = σ) = {σ 0} := by
        ext s
        simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
        refine ⟨fun hs => ?_, fun hs => by rw [hs]; exact hc⟩
        have := congrFun hs 0
        simpa [RevReal.states] using this
      rw [marg, hfil, Finset.sum_singleton, if_pos hc, mul_one]
    · have hfil : (Finset.univ.filter fun s => R.states s = σ) = ∅ := by
        ext s
        simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.notMem_empty, iff_false]
        intro hs
        have h0 : s = σ 0 := by
          have := congrFun hs 0
          simpa [RevReal.states] using this
        exact hc (h0 ▸ hs)
      rw [marg, hfil, Finset.sum_empty, if_neg hc, mul_zero]
  refine ⟨Q, ⟨EquivalenceChain.permMatrix_mem_unitaryGroup _, hn, ht⟩, ?_⟩
  rw [QfbReal.law, hchain, marg_marg]
  rfl

/-! ### `S → D`: the multi-time reversible carrier

This is the direction to audit hardest, and the one the rank-4 one-step ancilla dilation does NOT
supply: a one-step representation says nothing about `P(x_0, …, x_K)` as a joint law. What is built
here is the manuscript's multi-time response-table carrier, from scratch.

The hidden sector is a CLOCK together with a COMPLETE TRAJECTORY RECORD, `Fin (K+1) × Traj V K`.
The coherent states are those whose visible value agrees with the record at the clock's reading,
and the dynamics advances the clock cyclically while preserving the record. That dynamics is
injective on the coherent set — the record identifies the orbit and the clock the position along
it — and `exists_perm_extending` pads it to a bijection of the whole finite state space. Reading
the visible factor along the orbit from clock `0` returns the record itself, so the pushforward of
the initial law is `P`.

The initial law is the pushforward of `P` along `τ ↦ (τ 0, (0, τ))`, which is why the law
computation is three rewrites rather than a support argument. -/

/-- The hidden sector: a clock and a complete trajectory record. -/
abbrev Hid (V : Type u) (K : ℕ) := Fin (K + 1) × Traj V K

/-- The coherent state at clock `k` of record `τ`: visible value `τ k`, hidden state `(k, τ)`. -/
def emb {K : ℕ} (p : Hid V K) : V × Hid V K := (p.2 p.1, p)

/-- The intended dynamics: advance the clock cyclically, preserve the record. The visible value is
then forced, which is what makes the carrier deterministic. -/
def adv {K : ℕ} (s : V × Hid V K) : V × Hid V K := emb (s.2.1 + 1, s.2.2)

/-- The coherent set: where the dynamics is defined and injective. -/
noncomputable def coh (V : Type u) [Fintype V] [DecidableEq V] (K : ℕ) :
    Finset (V × Hid V K) := by
  classical exact Finset.univ.image emb

theorem mem_coh {K : ℕ} (p : Hid V K) : emb p ∈ coh V K := by
  classical
  simp [coh]

theorem adv_emb {K : ℕ} (p : Hid V K) : adv (emb p) = emb (p.1 + 1, p.2) := rfl

/-- The advance is injective on the coherent set: the record identifies the orbit and the clock the
position along it, so the image determines the source. -/
theorem injOn_adv {K : ℕ} : Set.InjOn (adv (V := V) (K := K)) ↑(coh V K) := by
  classical
  intro a ha b hb hab
  simp only [coh, Finset.coe_image] at ha hb
  obtain ⟨p, -, rfl⟩ := ha
  obtain ⟨q, -, rfl⟩ := hb
  rw [adv_emb, adv_emb] at hab
  have h2 : ((p.1 + 1, p.2) : Hid V K) = (q.1 + 1, q.2) := congrArg Prod.snd hab
  rw [Prod.mk.injEq] at h2
  rw [show p = q from Prod.ext (add_right_cancel h2.1) h2.2]

/-- Iterating the padded bijection from a coherent state advances the clock and nothing else. -/
theorem iterate_emb {K : ℕ} (σ : Equiv.Perm (V × Hid V K))
    (hσ : ∀ a ∈ coh V K, σ a = adv a) (j : ℕ) (c : Fin (K + 1)) (τ : Traj V K) :
    (fun s => σ s)^[j] (emb (c, τ)) = emb ((fun x : Fin (K + 1) => x + 1)^[j] c, τ) := by
  induction j with
  | zero => simp
  | succ i ih =>
      rw [Function.iterate_succ_apply', ih, hσ _ (mem_coh _), adv_emb,
        Function.iterate_succ_apply' (f := fun x : Fin (K + 1) => x + 1)]

/-- Advancing the clock `j` times from `0` reads `j`, for `j` inside the horizon. -/
theorem clock_iterate {K : ℕ} (j : ℕ) (hj : j < K + 1) :
    (fun x : Fin (K + 1) => x + 1)^[j] (0 : Fin (K + 1)) = ⟨j, hj⟩ := by
  induction j with
  | zero => rfl
  | succ i ih =>
      have hi : i < K + 1 := Nat.lt_of_succ_lt hj
      rw [Function.iterate_succ_apply', ih hi]
      refine Fin.ext ?_
      have : ((⟨i, hi⟩ : Fin (K + 1)) : ℕ) + 1 < K + 1 := hj
      rw [Fin.val_add_one_of_lt' this]

/-- **`S → D`.** Every finite stochastic finite-horizon law is the visible marginal of a finite
reversible deterministic system. -/
theorem S_imp_D {K : ℕ} (P : Traj V K → ℝ) (h : Stochastic P) : RevRealizable P := by
  classical
  obtain ⟨hn, ht⟩ := h
  obtain ⟨σ, hσ⟩ := exists_perm_extending (coh V K) (adv (V := V) (K := K)) injOn_adv
  set ι : Traj V K → V × Hid V K := fun τ => emb ((0 : Fin (K + 1)), τ) with hι
  refine ⟨{ Hid := Hid V K, fH := inferInstance, dH := inferInstance,
            step := σ, init := marg P ι }, ⟨marg_nonneg hn ι, ?_⟩, ?_⟩
  · rw [sum_marg]; exact ht
  · have hcomp : ∀ τ : Traj V K,
        (RevReal.traj (V := V) (K := K)
          { Hid := Hid V K, fH := inferInstance, dH := inferInstance,
            step := σ, init := marg P ι } (ι τ)) = τ := by
      intro τ
      funext k
      have hit := iterate_emb σ hσ (k : ℕ) 0 τ
      rw [clock_iterate (k : ℕ) k.2] at hit
      simp only [RevReal.traj, RevReal.states]
      rw [show (fun s => σ s)^[(k : ℕ)] (ι τ) = emb ((⟨(k : ℕ), k.2⟩ : Fin (K + 1)), τ) from hit]
      simp [emb]
    show marg (marg P ι) _ = P
    rw [marg_marg]
    have : (RevReal.traj (V := V) (K := K)
        { Hid := Hid V K, fH := inferInstance, dH := inferInstance,
          step := σ, init := marg P ι }) ∘ ι = id := funext hcomp
    rw [this, marg_id]

/-! ### The theorem -/

/-- **Theorem (finite-horizon stochastic–reversible–unitary equivalence), [Main] §3.4.**

For every finite-horizon law on a finite visible alphabet, the three classes coincide:

* `(S)` finite stochastic laws;
* `(D)` visible marginals of finite reversible deterministic systems;
* `(Q_fb)` laws of finite-dimensional unitary systems with fixed-basis Born readout.

Every implication is discharged by one of the three constructions above — `S_imp_D`'s multi-time
clock-and-record carrier, `D_imp_Qfb`'s permutation unitary, `Qfb_imp_S`'s chain normalisation —
and NONE of them appears as a hypothesis here. A wrapper that took them as hypotheses would encode
the theorem instead of proving it. -/
theorem finite_horizon_equivalence {K : ℕ} (P : Traj V K → ℝ) :
    (Stochastic P ↔ RevRealizable P) ∧
    (RevRealizable P ↔ QfbRealizable P) ∧
    (QfbRealizable P ↔ Stochastic P) :=
  ⟨⟨S_imp_D P, fun h => Qfb_imp_S P (D_imp_Qfb P h)⟩,
   ⟨D_imp_Qfb P, fun h => S_imp_D P (Qfb_imp_S P h)⟩,
   ⟨Qfb_imp_S P, fun h => D_imp_Qfb P (S_imp_D P h)⟩⟩

/-! ### What these proofs rest on -/

#print axioms exists_perm_extending
#print axioms sum_chain
#print axioms Qfb_imp_S
#print axioms D_imp_Qfb
#print axioms injOn_adv
#print axioms iterate_emb
#print axioms clock_iterate
#print axioms S_imp_D
#print axioms finite_horizon_equivalence

end Equivalence

end OIBridge
