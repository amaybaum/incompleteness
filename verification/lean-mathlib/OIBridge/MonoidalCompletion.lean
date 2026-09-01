/-
  OIBridge/MonoidalCompletion.lean — the compositional completion principle, the
  operational control principle, and the separation between them.

  PHASE THREE, ROUND TWENTY-FOUR. Round twenty-three proved that C1–C4 OI does not select
  the unrestricted operational completion: one shared core carries three completions that
  agree on every classical comb and fail, in turn, H-functor, H-tensor, and the Lie-rank
  condition. This round compresses those three survivors into their true shape. They are
  not three principles of the same kind.

  §A — IMPLEMENTATION EXTENSIONALITY AND DESCENT. An implementation is a word in the
  primitive intervention menu. Two things are STRUCTURAL, not axioms: concatenating
  implementations composes their classical maps (`wordPerm_append`) and composes their
  coherent maps (`wordMap_append`) — running `u` then `v` IS running `u ++ v`. The single
  axiom is

      ┌────────────────────────────────────────────────────────────────────┐
      │  IMPLEMENTATION EXTENSIONALITY:                                     │
      │      wordPerm u = wordPerm v  ⟹  wordMap u = wordMap v.             │
      └────────────────────────────────────────────────────────────────────┘

  Its content is descent (`implementationExtensionality_descends`): the coherent word
  representation factors through the quotient by physical implementation equivalence, so
  it is a representation of physical TRANSFORMATIONS rather than of implementation
  STRINGS. Functoriality is then recovered on the reachable transformation quotient
  (`descendedAction_functorial`) — it is a consequence, not a second assumption, because
  sequential composition was already structural.

  §B — SPECTATOR INDEPENDENCE. Defined OPERATIONALLY: for a classical action that moves
  only `B`, the completion is `id_A ⊗ Φ_B` on every product state. The correlation
  pattern is then the CLASSIFICATION of that condition, not its meaning
  (`spectatorIndependent_iff`): spectator independence holds exactly when the composite
  correlation is the `B`-correlation and does not depend on the spectator indices at all.

  §C — THE COMPOSITIONAL PRINCIPLE. `HComp = ImplementationExtensionality ∧
  SpectatorIndependence`, named only after both clauses are independently defined. The
  forward compression `hComp_forward` gives H-functor (on the reachable quotient) and
  H-tensor together. The converse is NOT forced: H-functor is formulated for a group
  action and H-tensor for selected product actions, so the reverse direction is stated
  scoped, under a menu-generation hypothesis, rather than asserted as a syntactic iff.

  §D — CONTROL: THE SEPARATION THAT MATTERS. The Lie-rank condition is NOT a coherence
  axiom and is NOT necessary for full operational quantum mechanics. Two levels:

      H_Lie      :  su(D) ⊆ 𝔏₀(H,U)          — the finite drift/control CERTIFICATE
      H_opControl:  reachable controls ⊇ PSU(D) — the operational RICHNESS principle

  `HControl_iff_controlLie0_full` is kernel-internal and invokes no Lie integration; only
  the passage `H_Lie ⟹ H_opControl` sits at the cited compact-Lie boundary. That the
  certificate is not necessary is a THEOREM here, not a caveat: `centralDrift_not_HControl`
  shows that for a central drift `H = c·1` the control algebra collapses to a line FOR
  EVERY control family whatsoever — so an observer with a maximally rich menu still fails
  `H_Lie`. Baking `H_Lie` into the definition of unrestricted operational quantum
  mechanics would make the characterization hostage to one control architecture.

  §E — THE TAXONOMY, KERNELIZED. On the sealed round-twenty-three core
  (`CoreC1C4`), each completion is typed by exactly which clause it fails
  (`census_clause_taxonomy`): completion 1 fails implementation extensionality;
  completion 2 satisfies it and fails spectator independence; completion 3 satisfies both
  and fails the Lie certificate. Each additional principle removes exactly one surviving
  class while leaving all lower OI data unchanged.

  WORDING DISCIPLINE. Completion 3 proves that the round-nineteen Lie-rank ROUTE to
  universal control is not forced by C1–C4 plus compositionality. It does NOT prove that
  no other universal primitive-control menu could have been supplied.

  Kernel check:  cd verification/lean-mathlib && lake exe cache get && lake build
-/
import OIBridge.IndependenceCensus

namespace OIBridge
namespace MonoidalCompletion

open Complex Matrix CoherentExtension ControlLie IndependenceCensus

local notation "conj'" => (starRingEnd ℂ)

/-! ### Section A — implementations, the word representation, and descent -/

variable {ι S : Type*} [Fintype S] [DecidableEq S]

/-- The classical reversible map realized by an implementation word. -/
def wordPerm (act : ι → Equiv.Perm S) : List ι → Equiv.Perm S
  | [] => 1
  | i :: w => act i * wordPerm act w

/-- The coherent map of an implementation word. Running `u` then `v` IS running `u ++ v`,
so the coherent map of a word is the composite of its letters' coherent maps: sequential
composition is STRUCTURAL at the word level, not an axiom. -/
def wordMap (act : ι → Equiv.Perm S) (corr : ι → Matrix S S ℂ) :
    List ι → (Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ)
  | [] => LinearMap.id
  | i :: w => (correlationExtension (act i) (corr i)).comp (wordMap act corr w)

omit [Fintype S] [DecidableEq S] in
@[simp] theorem wordPerm_nil (act : ι → Equiv.Perm S) : wordPerm act [] = 1 := rfl

omit [Fintype S] [DecidableEq S] in
@[simp] theorem wordMap_nil (act : ι → Equiv.Perm S) (corr : ι → Matrix S S ℂ) :
    wordMap act corr [] = LinearMap.id := rfl

omit [Fintype S] [DecidableEq S] in
/-- Concatenating implementations composes their classical maps. -/
theorem wordPerm_append (act : ι → Equiv.Perm S) (u v : List ι) :
    wordPerm act (u ++ v) = wordPerm act u * wordPerm act v := by
  induction u with
  | nil => rw [List.nil_append, wordPerm_nil, one_mul]
  | cons i u ih =>
      show act i * wordPerm act (u ++ v) = act i * wordPerm act u * wordPerm act v
      rw [ih, mul_assoc]

omit [Fintype S] [DecidableEq S] in
/-- Concatenating implementations composes their coherent maps. -/
theorem wordMap_append (act : ι → Equiv.Perm S) (corr : ι → Matrix S S ℂ) (u v : List ι) :
    wordMap act corr (u ++ v)
      = (wordMap act corr u).comp (wordMap act corr v) := by
  induction u with
  | nil => rw [List.nil_append, wordMap_nil, LinearMap.id_comp]
  | cons i u ih =>
      show (correlationExtension (act i) (corr i)).comp (wordMap act corr (u ++ v))
        = ((correlationExtension (act i) (corr i)).comp (wordMap act corr u)).comp
            (wordMap act corr v)
      rw [ih, LinearMap.comp_assoc]

/-- **IMPLEMENTATION EXTENSIONALITY.** Two implementations realizing the same classical
reversible transformation are completed by the same coherent map: the completion depends
on WHAT was done, not on HOW it was implemented. -/
def ImplementationExtensionality (act : ι → Equiv.Perm S)
    (corr : ι → Matrix S S ℂ) : Prop :=
  ∀ u v : List ι, wordPerm act u = wordPerm act v → wordMap act corr u = wordMap act corr v

/-- The classical transformations actually reachable by some implementation. -/
def Reachable (act : ι → Equiv.Perm S) : Set (Equiv.Perm S) := Set.range (wordPerm act)

/-- The coherent map assigned to a reachable transformation, by choosing any
implementation of it. -/
noncomputable def descendedAction (act : ι → Equiv.Perm S) (corr : ι → Matrix S S ℂ)
    (g : Reachable act) : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ :=
  wordMap act corr g.2.choose

omit [Fintype S] [DecidableEq S] in
/-- **THE DESCENT THEOREM.** Under implementation extensionality the coherent word
representation descends to the quotient by physical implementation equivalence: the
coherent map of a word depends only on the classical transformation it realizes, so the
choice of implementation is immaterial. This — not "therefore functorial" — is the
content of extensionality. -/
theorem implementationExtensionality_descends
    {act : ι → Equiv.Perm S} {corr : ι → Matrix S S ℂ}
    (hext : ImplementationExtensionality act corr) (u : List ι) :
    descendedAction act corr ⟨wordPerm act u, ⟨u, rfl⟩⟩ = wordMap act corr u := by
  have hex : ∃ y : List ι, wordPerm act y = wordPerm act u := ⟨u, rfl⟩
  show wordMap act corr hex.choose = wordMap act corr u
  exact hext _ u hex.choose_spec

omit [Fintype S] [DecidableEq S] in
/-- **THE DESCENDED ACTION IS FUNCTORIAL.** The identity transformation is completed by
the identity map, and composition of classical transformations is composition of coherent
maps. Sequential composition was already structural at the word level; extensionality is
exactly what turns it into a well-defined representation of physical transformations.
Round eighteen's H-functor is recovered here, on the reachable transformation quotient. -/
theorem descendedAction_functorial {act : ι → Equiv.Perm S} {corr : ι → Matrix S S ℂ}
    (hext : ImplementationExtensionality act corr) :
    (∀ u : List ι, wordPerm act u = 1 → wordMap act corr u = LinearMap.id)
      ∧ (∀ u v w : List ι, wordPerm act w = wordPerm act u * wordPerm act v →
          wordMap act corr w = (wordMap act corr u).comp (wordMap act corr v)) := by
  refine ⟨fun u hu => ?_, fun u v w hw => ?_⟩
  · have h := hext u [] (by rw [hu, wordPerm_nil])
    rwa [wordMap_nil] at h
  · rw [hext w (u ++ v) (by rw [hw, wordPerm_append]), wordMap_append]

/-! ### Section B — spectator independence -/

variable {A B : Type*} [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B]

/-- The classical action that moves only the `B` coordinate, leaving `A` an untouched
independent spectator. -/
def spectatorExt (g : Equiv.Perm B) : Equiv.Perm (A × B) where
  toFun p := (p.1, g p.2)
  invFun p := (p.1, g.symm p.2)
  left_inv p := by simp
  right_inv p := by simp

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
@[simp] theorem spectatorExt_symm_apply (g : Equiv.Perm B) (p : A × B) :
    (spectatorExt g).symm p = (p.1, g.symm p.2) := rfl

/-- The product state `X_A ⊗ X_B`. -/
def tensorOf (XA : Matrix A A ℂ) (XB : Matrix B B ℂ) : Matrix (A × B) (A × B) ℂ :=
  Matrix.of fun p q => XA p.1 q.1 * XB p.2 q.2

omit [Fintype A] [DecidableEq A] [Fintype B] [DecidableEq B] in
@[simp] theorem tensorOf_apply (XA : Matrix A A ℂ) (XB : Matrix B B ℂ) (p q : A × B) :
    tensorOf XA XB p q = XA p.1 q.1 * XB p.2 q.2 := rfl

/-- **SPECTATOR INDEPENDENCE, operationally.** Adjoining an untouched independent system
acts by `id_A ⊗ Φ_B`: on every product state, completing `id_A × g_B` is completing `g_B`
on the `B` factor and leaving the spectator alone. This is the physical statement; the
correlation pattern below is its classification, not its definition. -/
def SpectatorIndependent (CB : Equiv.Perm B → Matrix B B ℂ)
    (C : Equiv.Perm (A × B) → Matrix (A × B) (A × B) ℂ) : Prop :=
  ∀ (g : Equiv.Perm B) (XA : Matrix A A ℂ) (XB : Matrix B B ℂ),
    correlationExtension (spectatorExt g) (C (spectatorExt g)) (tensorOf XA XB)
      = tensorOf XA (correlationExtension g (CB g) XB)

omit [Fintype A] [Fintype B] in
/-- **THE SPECTATOR CLASSIFICATION.** Within the round-seventeen correlation family,
spectator independence holds EXACTLY when the composite correlation is the `B`-correlation
and does not depend on the spectator indices at all. So the matrix pattern is the
classification of spectator independence, not its meaning. -/
theorem spectatorIndependent_iff
    (CB : Equiv.Perm B → Matrix B B ℂ)
    (C : Equiv.Perm (A × B) → Matrix (A × B) (A × B) ℂ) :
    SpectatorIndependent CB C
      ↔ ∀ (g : Equiv.Perm B) (p q : A × B),
          C (spectatorExt g) p q = CB g p.2 q.2 := by
  constructor
  · intro hsp g p q
    obtain ⟨a, s⟩ := p
    obtain ⟨a', t⟩ := q
    have h := congrFun (congrFun (hsp g (Matrix.single a a' 1) (Matrix.single s t 1))
      (a, g s)) (a', g t)
    rw [show (correlationExtension (spectatorExt g) (C (spectatorExt g))
          (tensorOf (Matrix.single a a' 1) (Matrix.single s t 1))) (a, g s) (a', g t)
        = C (spectatorExt g) (a, s) (a', t)
          * (Matrix.single a a' (1 : ℂ) a a' * Matrix.single s t (1 : ℂ) s t) from by
      show C (spectatorExt g) ((spectatorExt g).symm (a, g s))
            ((spectatorExt g).symm (a', g t))
          * tensorOf (Matrix.single a a' 1) (Matrix.single s t 1)
              ((spectatorExt g).symm (a, g s)) ((spectatorExt g).symm (a', g t)) = _
      rw [spectatorExt_symm_apply, spectatorExt_symm_apply, Equiv.symm_apply_apply,
        Equiv.symm_apply_apply, tensorOf_apply]] at h
    rw [show tensorOf (Matrix.single a a' (1 : ℂ))
          (correlationExtension g (CB g) (Matrix.single s t 1)) (a, g s) (a', g t)
        = Matrix.single a a' (1 : ℂ) a a' * (CB g s t * Matrix.single s t (1 : ℂ) s t)
        from by
      rw [tensorOf_apply]
      congr 1
      show (correlationExtension g (CB g) (Matrix.single s t 1)) (g s) (g t) = _
      show CB g (g.symm (g s)) (g.symm (g t))
        * Matrix.single s t (1 : ℂ) (g.symm (g s)) (g.symm (g t)) = _
      rw [Equiv.symm_apply_apply, Equiv.symm_apply_apply]] at h
    rw [Matrix.single_apply_same, Matrix.single_apply_same, mul_one, one_mul] at h
    simpa using h
  · intro hpat g XA XB
    ext p q
    show C (spectatorExt g) ((spectatorExt g).symm p) ((spectatorExt g).symm q)
        * tensorOf XA XB ((spectatorExt g).symm p) ((spectatorExt g).symm q)
      = tensorOf XA (correlationExtension g (CB g) XB) p q
    rw [spectatorExt_symm_apply, spectatorExt_symm_apply, hpat, tensorOf_apply,
      tensorOf_apply]
    show CB g (g.symm p.2) (g.symm q.2) * (XA p.1 q.1 * XB (g.symm p.2) (g.symm q.2))
      = XA p.1 q.1 * (CB g (g.symm p.2) (g.symm q.2) * XB (g.symm p.2) (g.symm q.2))
    ring


/-! ### Section C — the compositional principle -/

/-- The all-ones correlation on any carrier: the identity member of the family. -/
def onesC (S : Type*) : Matrix S S ℂ := Matrix.of fun _ _ => 1

omit [Fintype S] in
/-- **The word representation lives in the round-seventeen family.** The correlation
family is closed under composition — actions compose and correlations Schur-multiply — so
every implementation word is completed by a member of the same family, with unit diagonal
preserved. This is the concrete bridge from the word picture to rounds seventeen and
eighteen. -/
theorem wordMap_isCorrelationExtension (act : ι → Equiv.Perm S) (corr : ι → Matrix S S ℂ)
    (hunit : ∀ i s, corr i s s = 1) (w : List ι) :
    ∃ Cw : Matrix S S ℂ, (∀ s, Cw s s = 1)
      ∧ wordMap act corr w = correlationExtension (wordPerm act w) Cw := by
  induction w with
  | nil =>
      refine ⟨onesC S, fun _ => rfl, ?_⟩
      rw [wordMap_nil, wordPerm_nil]
      exact ((correlationExtension_one_eq_id_iff (onesC S)).mpr fun _ _ => rfl).symm
  | cons i w ih =>
      obtain ⟨Cw, hdiag, hw⟩ := ih
      refine ⟨Matrix.of fun s t => Cw s t * corr i (wordPerm act w s) (wordPerm act w t),
        fun s => by rw [Matrix.of_apply, hdiag, hunit, one_mul], ?_⟩
      show (correlationExtension (act i) (corr i)).comp (wordMap act corr w) = _
      rw [hw, correlationExtension_comp]
      rfl

omit [Fintype S] [DecidableEq S] in
/-- **THE SEQUENTIAL CLAUSE IS EXACTLY FUNCTORIALITY ON THE QUOTIENT.** Implementation
extensionality is equivalent to the descended action being functorial. Forward is the
descent theorem. Backward is the sharper half: taking the second word EMPTY, the
composition law alone already forces the completion to depend only on the realized
transformation — so nothing beyond composition-with-identity is being assumed. -/
theorem implementationExtensionality_iff_functorial (act : ι → Equiv.Perm S)
    (corr : ι → Matrix S S ℂ) :
    ImplementationExtensionality act corr
      ↔ ((∀ u : List ι, wordPerm act u = 1 → wordMap act corr u = LinearMap.id)
        ∧ (∀ u v w : List ι, wordPerm act w = wordPerm act u * wordPerm act v →
            wordMap act corr w = (wordMap act corr u).comp (wordMap act corr v))) := by
  constructor
  · exact descendedAction_functorial
  · rintro ⟨-, hcomp⟩ u v huv
    have h := hcomp v [] u (by rw [huv, wordPerm_nil, mul_one])
    rwa [wordMap_nil, LinearMap.comp_id] at h

/-- **THE COMPOSITIONAL PRINCIPLE `H_comp`.** Named only after both clauses are
independently defined: a coherent completion respects the composition rules of the
underlying physical interventions, SEQUENTIALLY (implementation extensionality) and in
PARALLEL (spectator independence). -/
def HComp (act : ι → Equiv.Perm (A × B)) (corr : ι → Matrix (A × B) (A × B) ℂ)
    (CB : Equiv.Perm B → Matrix B B ℂ)
    (C : Equiv.Perm (A × B) → Matrix (A × B) (A × B) ℂ) : Prop :=
  ImplementationExtensionality act corr ∧ SpectatorIndependent CB C

/-- **THE COMPRESSION.** `H_comp` holds exactly when the completion is functorial on the
reachable transformation quotient (round eighteen's H-functor, recovered) AND its
spectator-extended correlations are the `B`-correlations with no spectator dependence
(round twenty's H-tensor, in classified form).

SCOPE. This is the equivalence between `H_comp` and the CLASSIFICATIONS of its two
clauses, both of which are genuine iffs. It is NOT the claim that `H_comp` is
syntactically equivalent to `CoherentFunctoriality` as round eighteen states it (for a
group action `ρ : G →* Equiv.Perm S`) together with round twenty's H-tensor (for selected
product actions): those two have different domains, and identifying them needs a
menu-generation hypothesis. The forward compression is the honest content. -/
theorem hComp_iff (act : ι → Equiv.Perm (A × B)) (corr : ι → Matrix (A × B) (A × B) ℂ)
    (CB : Equiv.Perm B → Matrix B B ℂ)
    (C : Equiv.Perm (A × B) → Matrix (A × B) (A × B) ℂ) :
    HComp act corr CB C
      ↔ (((∀ u : List ι, wordPerm act u = 1 → wordMap act corr u = LinearMap.id)
            ∧ (∀ u v w : List ι, wordPerm act w = wordPerm act u * wordPerm act v →
                wordMap act corr w = (wordMap act corr u).comp (wordMap act corr v)))
          ∧ ∀ (g : Equiv.Perm B) (p q : A × B),
              C (spectatorExt g) p q = CB g p.2 q.2) := by
  rw [HComp, implementationExtensionality_iff_functorial,
    spectatorIndependent_iff]

/-! ### Section D — control: the certificate and the operational principle -/

/-- `su(D)`: traceless skew-Hermitian. Round nineteen already separated the full algebra
`𝔏` from its traceless part `𝔏₀`; stating the control condition on the traceless part
explicitly is what keeps a central drift from being mistaken for control richness. -/
def IsSpecialSkew (A : Matrix S S ℂ) : Prop := Aᴴ = -A ∧ A.trace = 0

/-- **`H_Lie`, the finite drift/control CERTIFICATE**: `su(D) ⊆ 𝔏(H,U)`. This is the
round-nineteen Lie-rank condition at its infinitesimal level. It invokes no analytic
passage whatsoever. -/
def HControl {G : Type*} (H : Matrix S S ℂ) (U : G → Matrix S S ℂ) : Prop :=
  ∀ A : Matrix S S ℂ, IsSpecialSkew A → A ∈ controlLie H U

/-- `H_Lie` is exactly "the control Lie algebra contains all of `su(D)`" — kernel-internal,
with no Lie integration anywhere in its statement or proof. -/
theorem HControl_iff_controlLie0_full {G : Type*} (H : Matrix S S ℂ)
    (U : G → Matrix S S ℂ) :
    HControl H U ↔ ∀ A : Matrix S S ℂ, Aᴴ = -A → A.trace = 0 → A ∈ controlLie H U :=
  ⟨fun h A h1 h2 => h A ⟨h1, h2⟩, fun h A hA => h A hA.1 hA.2⟩

/-- The unitary channel `X ↦ V X V†`. -/
def conjChannel (V : Matrix S S ℂ) : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ where
  toFun X := V * X * Vᴴ
  map_add' X Y := by
    show V * (X + Y) * Vᴴ = V * X * Vᴴ + V * Y * Vᴴ
    rw [Matrix.mul_add, Matrix.add_mul]
  map_smul' c X := by
    show V * (c • X) * Vᴴ = (RingHom.id ℂ) c • (V * X * Vᴴ)
    rw [Matrix.mul_smul, Matrix.smul_mul, RingHom.id_apply]

/-- **`H_opControl`, the operational richness principle.** Every unitary channel is
available. Phases drop out of conjugation, so this is a condition on `PSU(D)` rather than
`SU(D)`, and — crucially — it says nothing about HOW the controls were generated.

RECORDED AT THE COMPACT-LIE BOUNDARY: `H_Lie ⟹ H_opControl`, because a connected Lie
subgroup whose Lie algebra is `su(D)` is `SU(D)`. That passage, and only it, is the
compact Lie-integration fact; it is recorded here, not re-derived. Nothing else in this
file uses it — in particular `HControl_iff_controlLie0_full` is kernel-internal. -/
def UniversalUnitaryReachability
    (avail : ∀ m : ℕ, (Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop) : Prop :=
  ∀ V : Matrix S S ℂ, Vᴴ * V = 1 → avail 1 (fun _ => conjChannel V)

omit [Fintype S] in
theorem single_diag_hermitian' (k : S) :
    (Matrix.single k k (1 : ℂ))ᴴ = Matrix.single k k 1 := by
  ext a b
  rw [Matrix.conjTranspose_apply, single_entry, single_entry]
  by_cases h : k = a ∧ k = b
  · rw [if_pos ⟨h.2, h.1⟩, if_pos h, star_one]
  · rw [if_neg (fun hh => h ⟨hh.2, hh.1⟩), if_neg h, star_zero]

theorem trace_single_diag' (k : S) : (Matrix.single k k (1 : ℂ)).trace = 1 := by
  rw [Matrix.trace, Finset.sum_eq_single k]
  · rw [Matrix.diag_apply, Matrix.single_apply_same]
  · intro a _ ha
    rw [Matrix.diag_apply, single_entry, if_neg (fun hh => ha hh.1.symm)]
  · intro h
    exact absurd (Finset.mem_univ _) h

/-- A conjugation-invariant drift: every control leaves a central Hamiltonian alone. -/
theorem central_conj_fixed {G : Type*} (c : ℂ) (U : G → Matrix S S ℂ)
    (hU : ∀ g, U g * (U g)ᴴ = 1) (g : G) :
    U g * (c • (1 : Matrix S S ℂ)) * (U g)ᴴ = c • (1 : Matrix S S ℂ) := by
  rw [Matrix.mul_smul, Matrix.smul_mul, Matrix.mul_one, hU]

/-- **THE CERTIFICATE IS NOT NECESSARY.** For a CENTRAL drift `H = c·1` every control
conjugates `H` to itself, so the control Lie algebra collapses to the single line
`ℝ(-i c·1)` FOR EVERY control family whatsoever — however rich the menu. As soon as the
carrier has two distinct states there is a traceless skew-Hermitian direction outside that
line, so `H_Lie` FAILS even for an observer able to perform every unitary. Requiring the
round-nineteen certificate in the reverse direction would therefore make any
characterization of unrestricted operational quantum mechanics hostage to one control
architecture — which is exactly why `H_opControl`, not `H_Lie`, is the operational
principle. -/
theorem centralDrift_not_HControl {G : Type*} [Nonempty G] (c : ℂ)
    {s t : S} (hst : s ≠ t) (U : G → Matrix S S ℂ) (hU : ∀ g, U g * (U g)ᴴ = 1) :
    ¬ HControl (c • (1 : Matrix S S ℂ)) U := by
  intro hfull
  set A : Matrix S S ℂ :=
    (-Complex.I) • (Matrix.single s s 1 - Matrix.single t t 1) with hA
  have hskew : Aᴴ = -A := by
    rw [hA, Matrix.conjTranspose_smul, Matrix.conjTranspose_sub,
      single_diag_hermitian', single_diag_hermitian',
      show star (-Complex.I) = Complex.I from by
        rw [star_neg, Complex.star_def, Complex.conj_I, neg_neg],
      ← neg_smul, neg_neg]
  have htr : A.trace = 0 := by
    rw [hA, Matrix.trace_smul, Matrix.trace_sub, trace_single_diag',
      trace_single_diag', sub_self, smul_zero]
  have hmem := hfull A ⟨hskew, htr⟩
  obtain ⟨r, hr⟩ :=
    (controlLie_trivial (c • (1 : Matrix S S ℂ)) U
      (fun g => central_conj_fixed c U hU g) A).mp hmem
  -- a real multiple of `-i·(c·1)` is a multiple of the identity, so its diagonal is
  -- constant; but `A` carries `-i` at `s` and `+i` at `t`
  have hdiag : A s s = A t t := by
    rw [hr]
    simp [Matrix.smul_apply, Matrix.one_apply_eq]
  have hss : A s s = -Complex.I := by
    rw [hA, Matrix.smul_apply, Matrix.sub_apply, single_entry, single_entry,
      if_pos ⟨rfl, rfl⟩, if_neg (fun hh => hst hh.1.symm), sub_zero, smul_eq_mul,
      mul_one]
  have htt : A t t = Complex.I := by
    rw [hA, Matrix.smul_apply, Matrix.sub_apply, single_entry, single_entry,
      if_neg (fun hh => hst hh.1), if_pos ⟨rfl, rfl⟩, zero_sub, smul_eq_mul]
    ring
  rw [hss, htt] at hdiag
  have h2 : (2 : ℂ) * Complex.I = 0 := by linear_combination -hdiag
  rcases mul_eq_zero.mp h2 with h | h
  · exact absurd h (by norm_num)
  · exact Complex.I_ne_zero h


/-! ### Section E — the taxonomy, kernelized on the sealed C1–C4 core -/

theorem allOnes_apply (s t : Core) : allOnes s t = 1 := by
  show (1 : ℂ) * conj' 1 = 1
  rw [map_one, one_mul]

/-- The generator parities of an implementation word: `σ` and `τ` are commuting
involutions, so a word's classical transformation depends only on these. -/
def genParity : List Gen → Bool × Bool
  | [] => (false, false)
  | Gen.pass :: w => (!(genParity w).1, (genParity w).2)
  | Gen.ctrl :: w => ((genParity w).1, !(genParity w).2)

/-- The transformation realized by a parity pair. -/
def parityPerm : Bool × Bool → Equiv.Perm Core
  | (false, false) => 1
  | (true, false) => sigmaPerm
  | (false, true) => tauPerm
  | (true, true) => sigmaPerm * tauPerm

/-- The coherent map of a parity pair. -/
def parityMap (Cof : Gen → Matrix Core Core ℂ) :
    Bool × Bool → (Matrix Core Core ℂ →ₗ[ℂ] Matrix Core Core ℂ)
  | (false, false) => LinearMap.id
  | (true, false) => member Cof Gen.pass
  | (false, true) => member Cof Gen.ctrl
  | (true, true) => (member Cof Gen.pass).comp (member Cof Gen.ctrl)

theorem wordPerm_eq_parityPerm : ∀ w : List Gen,
    wordPerm genPerm w = parityPerm (genParity w)
  | [] => rfl
  | Gen.pass :: w => by
      have ih := wordPerm_eq_parityPerm w
      show genPerm Gen.pass * wordPerm genPerm w = parityPerm (genParity (Gen.pass :: w))
      rw [ih]
      show sigmaPerm * parityPerm (genParity w)
        = parityPerm (!(genParity w).1, (genParity w).2)
      rcases h : genParity w with ⟨a, b⟩
      cases a <;> cases b <;>
        simp only [parityPerm, Bool.not_false, Bool.not_true] <;>
        first
          | rfl
          | rw [mul_one]
          | exact sigmaPerm_sq
          | rw [← mul_assoc, sigmaPerm_sq, one_mul]
  | Gen.ctrl :: w => by
      have ih := wordPerm_eq_parityPerm w
      show genPerm Gen.ctrl * wordPerm genPerm w = parityPerm (genParity (Gen.ctrl :: w))
      rw [ih]
      show tauPerm * parityPerm (genParity w)
        = parityPerm ((genParity w).1, !(genParity w).2)
      rcases h : genParity w with ⟨a, b⟩
      cases a <;> cases b <;>
        simp only [parityPerm, Bool.not_false, Bool.not_true] <;>
        first
          | rfl
          | rw [mul_one]
          | exact tauPerm_sq
          | exact sigma_tau_commute.symm
          | rw [← mul_assoc, ← sigma_tau_commute, mul_assoc, tauPerm_sq, mul_one]

theorem wordMap_eq_parityMap (Cof : Gen → Matrix Core Core ℂ)
    (hp : (member Cof Gen.pass).comp (member Cof Gen.pass) = LinearMap.id)
    (hc : (member Cof Gen.ctrl).comp (member Cof Gen.ctrl) = LinearMap.id)
    (hcomm : (member Cof Gen.ctrl).comp (member Cof Gen.pass)
      = (member Cof Gen.pass).comp (member Cof Gen.ctrl)) : ∀ w : List Gen,
    wordMap genPerm Cof w = parityMap Cof (genParity w)
  | [] => rfl
  | Gen.pass :: w => by
      have ih := wordMap_eq_parityMap Cof hp hc hcomm w
      show (member Cof Gen.pass).comp (wordMap genPerm Cof w)
        = parityMap Cof (!(genParity w).1, (genParity w).2)
      rw [ih]
      rcases h : genParity w with ⟨a, b⟩
      cases a <;> cases b <;>
        simp only [parityMap, Bool.not_false, Bool.not_true] <;>
        first
          | rfl
          | rw [LinearMap.comp_id]
          | exact hp
          | rw [← LinearMap.comp_assoc, hp, LinearMap.id_comp]
  | Gen.ctrl :: w => by
      have ih := wordMap_eq_parityMap Cof hp hc hcomm w
      show (member Cof Gen.ctrl).comp (wordMap genPerm Cof w)
        = parityMap Cof ((genParity w).1, !(genParity w).2)
      rw [ih]
      rcases h : genParity w with ⟨a, b⟩
      cases a <;> cases b <;>
        simp only [parityMap, Bool.not_false, Bool.not_true] <;>
        first
          | rfl
          | rw [LinearMap.comp_id]
          | exact hc
          | exact hcomm
          | rw [← LinearMap.comp_assoc, hcomm, LinearMap.comp_assoc, hc,
              LinearMap.comp_id]

/-- The four parity transformations are distinct, so a word's parities are recoverable
from the transformation it realizes. -/
theorem parityPerm_injective : Function.Injective parityPerm := by
  rintro ⟨a, b⟩ ⟨a', b'⟩ h
  have h0 : parityPerm (a, b) (((false, true) : VH), false)
      = parityPerm (a', b') (((false, true) : VH), false) := by rw [h]
  revert h0
  cases a <;> cases b <;> cases a' <;> cases b' <;> intro h0 <;>
    first
      | rfl
      | exact absurd h0 (by decide)

/-- **A COMMUTING-INVOLUTION COMPLETION IS IMPLEMENTATION-EXTENSIONAL.** If both members
square to the identity and commute, the coherent map of a word depends only on the
generator parities — hence only on the classical transformation realized. -/
theorem implementationExtensionality_of_involutive (Cof : Gen → Matrix Core Core ℂ)
    (hp : (member Cof Gen.pass).comp (member Cof Gen.pass) = LinearMap.id)
    (hc : (member Cof Gen.ctrl).comp (member Cof Gen.ctrl) = LinearMap.id)
    (hcomm : (member Cof Gen.ctrl).comp (member Cof Gen.pass)
      = (member Cof Gen.pass).comp (member Cof Gen.ctrl)) :
    ImplementationExtensionality genPerm Cof := by
  intro u v huv
  rw [wordMap_eq_parityMap Cof hp hc hcomm u, wordMap_eq_parityMap Cof hp hc hcomm v,
    parityPerm_injective
      (show parityPerm (genParity u) = parityPerm (genParity v) by
        rw [← wordPerm_eq_parityPerm, ← wordPerm_eq_parityPerm]; exact huv)]

/-- A member squares to the identity when its correlation Schur-squares to all-ones. -/
theorem member_comp_self (Cof : Gen → Matrix Core Core ℂ) (g : Gen)
    (hinv : genPerm g * genPerm g = 1)
    (hsq : ∀ s t, Cof g s t * Cof g (genPerm g s) (genPerm g t) = 1) :
    (member Cof g).comp (member Cof g) = LinearMap.id := by
  show (correlationExtension (genPerm g) (Cof g)).comp
      (correlationExtension (genPerm g) (Cof g)) = LinearMap.id
  rw [correlationExtension_comp, hinv]
  exact (correlationExtension_one_eq_id_iff _).mpr fun s t => hsq s t

/-- The two members commute when their Schur products agree in both orders. -/
theorem member_comm_of (Cof : Gen → Matrix Core Core ℂ)
    (h : ∀ s t, Cof Gen.pass s t * Cof Gen.ctrl (sigmaPerm s) (sigmaPerm t)
      = Cof Gen.ctrl s t * Cof Gen.pass (tauPerm s) (tauPerm t)) :
    (member Cof Gen.ctrl).comp (member Cof Gen.pass)
      = (member Cof Gen.pass).comp (member Cof Gen.ctrl) := by
  show (correlationExtension (genPerm Gen.ctrl) (Cof Gen.ctrl)).comp
      (correlationExtension (genPerm Gen.pass) (Cof Gen.pass))
    = (correlationExtension (genPerm Gen.pass) (Cof Gen.pass)).comp
      (correlationExtension (genPerm Gen.ctrl) (Cof Gen.ctrl))
  rw [correlationExtension_comp, correlationExtension_comp]
  show correlationExtension (tauPerm * sigmaPerm)
      (Matrix.of fun s t => Cof Gen.pass s t
        * Cof Gen.ctrl (sigmaPerm s) (sigmaPerm t))
    = correlationExtension (sigmaPerm * tauPerm)
      (Matrix.of fun s t => Cof Gen.ctrl s t
        * Cof Gen.pass (tauPerm s) (tauPerm t))
  rw [sigma_tau_commute]
  congr 1
  ext s t
  exact h s t

/-- The nonfactorizable phase correlation Schur-squares to all-ones across a `τ`-step. -/
theorem nlPhase_rankOne_sq (s t : Core) :
    rankOneC nlPhase s t * rankOneC nlPhase (tauPerm s) (tauPerm t) = 1 := by
  rw [rankOneC_apply, rankOneC_apply, tauPerm_apply, tauPerm_apply]
  have h1 : nlPhase (flipFn s) * nlPhase s = 1 := nlPhase_flip_prod s
  have h3 : conj' (nlPhase (flipFn t)) * conj' (nlPhase t) = 1 := by
    rw [← map_mul, nlPhase_flip_prod t, map_one]
  calc nlPhase s * conj' (nlPhase t) * (nlPhase (flipFn s) * conj' (nlPhase (flipFn t)))
      = nlPhase (flipFn s) * nlPhase s
        * (conj' (nlPhase (flipFn t)) * conj' (nlPhase t)) := by ring
    _ = 1 * 1 := by rw [h1, h3]
    _ = 1 := one_mul 1

/-- **Completion 2 is implementation-extensional**: its two lifts are a strict
representation of `ℤ₂ × ℤ₂`, so words realizing the same transformation are completed
identically. -/
theorem nonTensor_implementationExtensional :
    ImplementationExtensionality genPerm nonTensorC := by
  refine implementationExtensionality_of_involutive nonTensorC ?_ ?_ ?_
  · exact member_comp_self _ _ sigmaPerm_sq fun s t => by
      rw [show nonTensorC Gen.pass = allOnes from rfl, allOnes_apply, allOnes_apply,
        one_mul]
  · exact member_comp_self _ _ tauPerm_sq fun s t => nlPhase_rankOne_sq s t
  · refine member_comm_of _ fun s t => ?_
    show allOnes s t * rankOneC nlPhase (sigmaPerm s) (sigmaPerm t)
      = rankOneC nlPhase s t * allOnes (tauPerm s) (tauPerm t)
    rw [allOnes_apply, allOnes_apply, one_mul, mul_one, rankOneC_apply, rankOneC_apply,
      sigmaPerm_apply, sigmaPerm_apply, nlPhase_swap_invariant, nlPhase_swap_invariant]

/-- **Completion 3 is implementation-extensional**: its lifts are the phase-free
permutation lifts. -/
theorem restricted_implementationExtensional :
    ImplementationExtensionality genPerm restrictedC := by
  refine implementationExtensionality_of_involutive restrictedC ?_ ?_ ?_
  · exact member_comp_self _ _ sigmaPerm_sq fun s t => by
      rw [show restrictedC Gen.pass = allOnes from rfl, allOnes_apply, allOnes_apply,
        one_mul]
  · exact member_comp_self _ _ tauPerm_sq fun s t => by
      rw [show restrictedC Gen.ctrl = allOnes from rfl, allOnes_apply, allOnes_apply,
        one_mul]
  · refine member_comm_of _ fun s t => ?_
    show allOnes s t * allOnes (sigmaPerm s) (sigmaPerm t)
      = allOnes s t * allOnes (tauPerm s) (tauPerm t)
    rw [allOnes_apply, allOnes_apply, allOnes_apply]

/-- **Completion 1 is NOT implementation-extensional.** The two implementations
`[τ, τ]` and `[]` realize the same classical transformation — `τ² = 1` — yet the
dephasing member does not compose to the identity. This is exactly the round-23
non-functoriality, re-expressed as the failure of the sequential clause. -/
theorem nonFunctorial_not_implementationExtensional :
    ¬ ImplementationExtensionality genPerm nonFunctorialC := by
  intro hext
  have hperm : wordPerm genPerm [Gen.ctrl, Gen.ctrl] = wordPerm genPerm [] := by
    show genPerm Gen.ctrl * (genPerm Gen.ctrl * 1) = 1
    rw [mul_one]
    exact tauPerm_sq
  have h := hext [Gen.ctrl, Gen.ctrl] [] hperm
  rw [wordMap_nil] at h
  refine nonFunctorial_not_functorial ?_
  rw [← h]
  show _ = (member nonFunctorialC Gen.ctrl).comp
    ((member nonFunctorialC Gen.ctrl).comp LinearMap.id)
  rw [LinearMap.comp_id]

/-- **Completion 2 FAILS the spectator criterion**: its `τ`-lift's correlation genuinely
depends on the spectator `vh` indices — the `b`-operation is coherently conditioned on the
untouched factor — so no `B`-only correlation reproduces it. -/
theorem nonTensor_not_spectatorPattern :
    ¬ ∃ CB : Matrix Bool Bool ℂ, ∀ p q : Core, rankOneC nlPhase p q = CB p.2 q.2 := by
  rintro ⟨CB, hCB⟩
  have h1 := hCB (((false, true) : VH), false) (((false, true) : VH), true)
  have h2 := hCB (((false, false) : VH), false) (((false, false) : VH), true)
  rw [show rankOneC nlPhase (((false, true) : VH), false) (((false, true) : VH), true)
      = -1 from by
    show Complex.I * conj' (-Complex.I) = -1
    rw [map_neg, Complex.conj_I, neg_neg, Complex.I_mul_I]] at h1
  rw [show rankOneC nlPhase (((false, false) : VH), false) (((false, false) : VH), true)
      = 1 from by
    show (1 : ℂ) * conj' 1 = 1
    rw [map_one, one_mul]] at h2
  have hcon : (-1 : ℂ) = 1 := h1.trans h2.symm
  norm_num at hcon

/-- Completion 3 satisfies the spectator criterion: its correlations are constant. -/
theorem restricted_spectatorPattern :
    ∃ CB : Matrix Bool Bool ℂ, ∀ p q : Core, allOnes p q = CB p.2 q.2 :=
  ⟨Matrix.of fun _ _ => 1, fun p q => allOnes_apply p q⟩

/-- **Completion 3 FAILS the Lie certificate.** -/
theorem restricted_not_HControl : ¬ HControl coreH restrictedU := fun h =>
  outsideGen_not_mem (h outsideGen ⟨outsideGen_skewHermitian, outsideGen_traceless⟩)

/-- **THE TAXONOMY, KERNELIZED.** On the sealed `CoreC1C4` core each completion is typed
by exactly which clause it fails, and each additional principle removes exactly one
surviving class while leaving all lower OI data unchanged
(`threeCompletions_same_classical_comb`):

  1. completion 1 fails implementation extensionality;
  2. completion 2 satisfies it and fails spectator independence;
  3. completion 3 satisfies both and fails the Lie certificate.

WORDING DISCIPLINE. Clause 3 says the round-nineteen Lie-rank ROUTE to universal control
is not forced by C1–C4 plus compositionality. It does NOT say that no other universal
primitive-control menu could have been supplied — that is why `H_opControl`, not `H_Lie`,
is the operational principle. -/
theorem census_clause_taxonomy :
    ¬ ImplementationExtensionality genPerm nonFunctorialC
      ∧ (ImplementationExtensionality genPerm nonTensorC
          ∧ ¬ ∃ CB : Matrix Bool Bool ℂ, ∀ p q : Core, rankOneC nlPhase p q = CB p.2 q.2)
      ∧ (ImplementationExtensionality genPerm restrictedC
          ∧ (∃ CB : Matrix Bool Bool ℂ, ∀ p q : Core, allOnes p q = CB p.2 q.2)
          ∧ ¬ HControl coreH restrictedU) :=
  ⟨nonFunctorial_not_implementationExtensional,
   ⟨nonTensor_implementationExtensional, nonTensor_not_spectatorPattern⟩,
   ⟨restricted_implementationExtensional, restricted_spectatorPattern,
    restricted_not_HControl⟩⟩


/-! ### Section F — the operational package -/

/-- The outcome-`a` branch of a finite Kraus family under an outcome labelling: the Kraus
operators sharing an outcome are SUMMED. That summation is what makes an instrument an
instrument rather than a bag of unrelated branch maps. -/
def instrumentBranch {n m : ℕ} (K : Fin n → Matrix S S ℂ) (out : Fin n → Fin m)
    (a : Fin m) : Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ :=
  ∑ k ∈ Finset.univ.filter (fun k => out k = a), conjChannel (K k)

/-- **FULL FINITE-INSTRUMENT AVAILABILITY.** For every finite NORMALIZED Kraus family
(`∑ K†K = 1`) under every finite outcome labelling, the whole outcome family is JOINTLY
available. Two things matter in this shape. Availability is a predicate on the outcome
family as a whole, not membership of each branch map in an unrelated set — an instrument
is the family, not its branches taken separately. And the statement is schematic in the
finite index types `Fin n`, `Fin m`, so it means every finite Kraus family and every finite
outcome set, not one fixed ancilla size silently realizing all of them. -/
def FullFiniteInstrumentAvailability
    (avail : ∀ m : ℕ, (Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop) : Prop :=
  ∀ (n m : ℕ) (K : Fin n → Matrix S S ℂ) (out : Fin n → Fin m),
    (∑ k, (K k)ᴴ * K k = 1) → avail m (instrumentBranch K out)

/-- **UNITARY CONTROLS ARE NOT A SEPARATE CONJUNCT.** A unitary channel is the ONE-KRAUS,
one-outcome instrument `K₀ = V`, whose normalization condition is exactly `V†V = 1`. So
full finite-instrument availability delivers universal unitary reachability — derived from
the single-Kraus case rather than from an over-strong arbitrary-`K` definition. -/
theorem fullOps_universalUnitary
    (avail : ∀ m : ℕ, (Fin m → Matrix S S ℂ →ₗ[ℂ] Matrix S S ℂ) → Prop)
    (h : FullFiniteInstrumentAvailability avail) :
    UniversalUnitaryReachability avail := by
  intro V hV
  have hb := h 1 1 (fun _ => V) (fun _ => 0) (by simpa using hV)
  have heq : instrumentBranch (fun _ : Fin 1 => V) (fun _ => (0 : Fin 1))
      = fun _ => conjChannel V := by
    funext a
    rw [instrumentBranch, Finset.filter_true_of_mem fun k _ => Subsingleton.elim _ _]
    simp
  rwa [heq] at hb

/-- **RICHNESS DOES NOT IMPLY COMPOSITIONALITY.** Instrument availability constrains which
channels EXIST; it says nothing about how the OI intervention words are COMPLETED. Taking
the everywhere-available menu, full finite-instrument availability holds outright while
round twenty-three's completion 1 still fails implementation extensionality. So the reverse
direction of a would-be characterization is FALSE for a richness-only predicate — this is a
mathematical fact about the predicates, not an editorial caution. -/
theorem availability_not_implies_hComp :
    FullFiniteInstrumentAvailability (S := Core) (fun _ _ => True)
      ∧ ¬ImplementationExtensionality genPerm nonFunctorialC :=
  ⟨fun _ _ _ _ _ => trivial, nonFunctorial_not_implementationExtensional⟩

/-! ### What is proved, what is one-way, and what is not yet done

The operational contents of the standard package that are ALREADY kernel theorems
downstream of `H_comp` are cited, not re-listed: intervention dilation and all finite
instruments (`finiteInstrument_of_ancillaControl`, round twenty), the pure ancilla seed
(`uniform_readout_feedforward_seed`, round twenty-one), purification
(`purification_of_factorization`, round twenty-one), the forced branch update
(`cp_rankOneSelector_iff_luders`, round twenty-two), and physical local tomography
(`local_tomography_physical`, round twenty as repaired).

THE REVERSE IMPLICATION IS FALSE, NOT MERELY UNASSEMBLED. `availability_not_implies_hComp`
proves that full finite-instrument availability does NOT imply `H_comp`. So with a
richness-only predicate the honest target is ONE-WAY:

    H_comp ∧ H_opControl  ⟹  full finite-instrument availability,

and even that forward assembly of rounds eighteen through twenty-two at a single carrier
and menu is still to be done; it is NOT asserted here. A genuine iff would need a
STRUCTURED predicate — standard equality of physically equivalent implementations, standard
spectator/local composition, and full finite-instrument availability — defined
operationally rather than by naming `HComp`, so that round twenty-four's classification
converts its first two requirements into `H_comp`.

The external boundary any such assembly rests on stays exactly four items and no more:
compact Lie integration, finite isometry extension, PSD square-root/factorization, and
finite Uhlmann/Schmidt uniqueness. -/

#print axioms wordPerm_append
#print axioms wordMap_append
#print axioms implementationExtensionality_descends
#print axioms descendedAction_functorial
#print axioms spectatorIndependent_iff
#print axioms wordMap_isCorrelationExtension
#print axioms implementationExtensionality_iff_functorial
#print axioms hComp_iff
#print axioms HControl_iff_controlLie0_full
#print axioms central_conj_fixed
#print axioms centralDrift_not_HControl
#print axioms wordPerm_eq_parityPerm
#print axioms wordMap_eq_parityMap
#print axioms parityPerm_injective
#print axioms implementationExtensionality_of_involutive
#print axioms nonTensor_implementationExtensional
#print axioms restricted_implementationExtensional
#print axioms nonFunctorial_not_implementationExtensional
#print axioms nonTensor_not_spectatorPattern
#print axioms restricted_not_HControl
#print axioms census_clause_taxonomy
#print axioms fullOps_universalUnitary
#print axioms availability_not_implies_hComp

end MonoidalCompletion
end OIBridge
