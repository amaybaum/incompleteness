import OIBridge.ReanchoredChannelScope

/-!
# Act 17 — what selects or constrains the cross-time Gram/orbit trajectory

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-17-gram-trajectory-selection/preregistration.md`,
blob `3b5570102aa6aacb09788059989a70d8cdd5b70f`, from the merge commit of that control plane,
`02cfc9be141a44aaebf847d8e7d9fdd0d0a18f08`, which the freeze fixes as this round's mandated base.

## What this round is

Act 12 classified the per-slice orbit exactly and act 13 localized the threading. `P0`'s remaining
first part is **what selects or constrains the Gram/orbit trajectory across time**, and this module
asks that and nothing else. The ask is **constraints-only**: what excludes cross-time trajectories.
Neither uniqueness nor a classification is undertaken, and falling short of either is not a
shortfall of the round.

**The round's cross-time equivalence is `GramTrajEquiv`**, act 12's per-slice `GramPhaseEquiv`
applied pointwise in time with the phase family chosen independently at each time. It is the only
relation any quotient here is taken over. Three relations are deliberately **not** adopted: raw Gram
equality, which is a representative-level equality; uniform-phase equality, which couples the slices
and would answer the round's question in the relation rather than in the kernel; and act 13's
level-2 and level-3 cross-time relations, which see the threading.

## What is proved

* `gramTrajEquiv_refl`, `gramTrajEquiv_symm`, `gramTrajEquiv_trans` — the adopted relation is an
  equivalence relation on trajectories, proved before it is used to compare anything.
* `gramTrajEquiv_of_threading` — **the scope boundary, demonstrated and not asserted**: every pair
  act 13 localized as threading-related is **one** trajectory here, through act 12's
  `fibreGram_left_mul` and act 13's `ct3g_fibreGram_strong_right`. No statement of this round
  distinguishes two lifts the relation identifies.
* `tj1_necessity` and `tj1_sufficiency` — **`TJ1`**, both directions, act 12's merged `SH1` consumed
  slice by slice, with `CoherentLift`'s own definition supplying no cross-time conjunct and a choice
  principle assembling the per-time dilations into one lift. `tj1_trajectory_set` is the two
  directions as one biconditional.
* `tj1_no_universal_cross_time_constraint` — the **positive** consequence: any property holding of
  every coherent lift's trajectory holds of **every** pointwise realizable assignment, so there is
  no additional universal cross-time constraint beyond pointwise realizability.
* `tj2a_sp1l_add`, `tj2c_sp2_add`, `tj2b_sp1g_add`, `tj2d_sp3_add`, `tj2e_sp5_add` — question (A)
  for the five named candidates: each **fails** for an exhibited coherent lift of an exhibited
  visible family, so each is **additional structure**.
* `tj2a_sp1l_nosel`, `tj2c_sp2_nosel`, `tj2d_sp3_nosel` — question (B) for three members of the
  frozen class: two inequivalent trajectories survive at the exhibited configuration.
* `tj2e_sp5_empty` — question (B) for the fourth: **no** coherent lift of that family satisfies it,
  with the excluded quantity computed.
* `tj2f_sp4_containment` — the out-of-regime probe: act 13's level-2 datum **contains** the Gram
  trajectory at its diagonal, so a rule permitted to read it determines the trajectory by containing
  it. That is a theorem about containment and not a selection.
* `tj3_imp_class_level_selection_impossibility` — **line 4 of the graded hierarchy**, in the order
  `∃ C ∀ S`: one configuration, admissible under this round's own constraints, at which **every**
  member of the frozen four-member class fails to select, each for a recorded reason.

## What none of this licenses

**No candidate is endorsed.** Each is named as an object of test and for no other purpose. Where a
candidate is refuted, what is refuted is the exact proposition the freeze states under that label, on
the exact data grant frozen for it, and nothing in its neighbourhood: no other memorylessness,
stationarity, determination or decoherence condition is refuted, named or excluded. **The candidate
class is four named propositions and is not exhaustive**; a candidate outside it is neither refuted
nor endorsed here. **Nothing here says a selector is required**, on any carrier or carrier-free.

**Line 4 is impossibility within that frozen class at one exhibited configuration.** It is not
impossibility over all conceivable selection principles, not a statement that no selection principle
exists, and not a statement that selection fails at every configuration — act 12's `SH1-C2` supplies
deterministic visible laws where the per-slice orbit is unique for free. The reversed quantifier
order `∀ S ∃ C` is the conjunction of the per-candidate verdicts and is **not** this statement.

**Nothing here is about the threading, the cross-time representative, the relative evolution or the
relative candidate.** These are invisible to `GramTrajEquiv` by construction, and a round that cannot
see a distinction may not report one, in either direction. Act 11's `GL2` pair is **one** trajectory
here. No carrier of act 14 is read, defined or adopted, and none is asserted not to be the physical
one. `GL1s`, `GL1w`, `GL2`, `GL3`, `GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`,
`CT1`–`CT4`, `CL1`, `PQ0`–`PQ4`, `CF0`–`CF5` and `RN0`–`RN4` are consumed and none is revised: act
12's `SH1` is consumed in both directions at its own strength and `TG3` existentially, about its own
exhibited dilations — **a merged existential is not enlarged to a universal by being consumed**.
`P0` stays **OPEN** and two-part and its threading part is untouched. `CoherentLift` is `ℕ`-indexed
and this round does not change that: no continuity, smoothness, derivative or continuum limit is
introduced or used. Nothing here says OI and QM are inequivalent, and every visibility statement is
under act 7's own readback convention with `D4b` **negative**. Nothing is imported from the
substratum Lemma 24.1 rounds, and nothing here is about Track I.

**THE CLAUSE, carried at this mention — the module docstring's statement of what is not licensed.**
Act 16's `RN3⁺` and act 15's `PQ3-d⁺` are **carrier-specific** cancellation verdicts. Each says
that on one named carrier — the relative-candidate carrier `𝒪₂` for act 15, the
re-anchored-channel carrier `𝒪₃` for act 16 — a constant in-fibre left move together with a
time-dependent strong right gauge can be redundancy as a pair while neither part is. **That is a
statement about the threading pair on a named carrier, and it is not a statement about the
cross-time Gram/orbit trajectory freedom this round studies.** The existence of cancellation on
those two carriers **does not license the assumption that all residual trajectory freedom is
gauge**: act 16 established a cancellation on named carriers and established **nothing** about
whether the trajectory freedom is redundancy, on any carrier or carrier-free, and act 14's status
rule that there is no carrier-free verdict binds this round too. **No outcome of this round may
treat act 16's positive, or act 15's, as evidence that the trajectory freedom is gauge or that it
is physical; no target of this round consumes either for that purpose; and no candidate selection
principle is named, rated, predicted, admitted or refuted on their strength.**
-/

namespace OIBridge
namespace GramTrajectorySelection

open Finset Matrix DilationChoice CoherentLiftGauge TwoSidedGauge CrossTimeInvariants

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the budgeted definitions -/

/-- **THE ROUND'S FROZEN CROSS-TIME EQUIVALENCE `≈_O`** (definition slot 1) — two Gram trajectories
are the same iff their per-slice tuples are `∼_D`-equivalent at **every** time, the phase family
being chosen **independently at each time** and not required to be the same at two times.

This is act 12's per-slice quotient applied pointwise in time: it **adds no cross-time
identification of its own**, which is exactly the point. Act 12's relation is consumed, not
redefined; what is added is a name for it as a relation on **trajectories**, so that trajectories
not yet known to be a lift's can be compared — which `TJ1` needs.

**Assuming a cross-time coupling in the relation would answer the round's question in the relation
rather than in the kernel.** The uniform-phase relation, with one time-independent phase family,
does exactly that and is recorded as a distinct relation this round does **not** adopt. -/
def GramTrajEquiv (𝔾 𝔾' : ℕ → V → Matrix V V ℂ) : Prop :=
  ∀ t, GramPhaseEquiv (𝔾 t) (𝔾' t)

/-- **THE SELECTION PREDICATE** (definition slot 2) — a candidate `S` **selects at the
configuration** `(a₀, Γ)` iff the `≈_O`-classes of the trajectories of the coherent lifts of `Γ`
satisfying `S` number exactly one: some coherent lift satisfies `S`, and every coherent lift
satisfying `S` has the same trajectory class as it.

The quotient is taken over `GramTrajEquiv`, this round's frozen cross-time equivalence, **and over
no other relation**. -/
def SelectsAt (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (S : (ℕ → Matrix (V × A) (V × A) ℂ) → Prop) : Prop :=
  ∃ U₀ : ℕ → Matrix (V × A) (V × A) ℂ, CoherentLift a₀ Γ U₀ ∧ S U₀ ∧
    ∀ U : ℕ → Matrix (V × A) (V × A) ℂ, CoherentLift a₀ Γ U → S U →
      GramTrajEquiv (fun t => FibreGram a₀ (U t)) (fun t => FibreGram a₀ (U₀ t))

/-! ### Section B — the adopted relation is an equivalence relation -/

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Reflexivity of the per-slice relation, with the trivial phase family. -/
theorem gramPhaseEquiv_refl (G : V → Matrix V V ℂ) : GramPhaseEquiv G G :=
  ⟨fun _ => 1, fun _ => by simp, fun _ _ _ => by simp⟩

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Symmetry of the per-slice relation: invert the phases. -/
theorem gramPhaseEquiv_symm {G G' : V → Matrix V V ℂ} (h : GramPhaseEquiv G G') :
    GramPhaseEquiv G' G := by
  obtain ⟨c, hc, hG⟩ := h
  refine ⟨fun j => star (c j), fun j => by simpa using hc j, fun i j k => ?_⟩
  have hj : c j * star (c j) = 1 := by
    rw [mul_comm, star_mul_self_eq_norm_sq, hc, one_pow, Complex.ofReal_one]
  have hk : c k * star (c k) = 1 := by
    rw [mul_comm, star_mul_self_eq_norm_sq, hc, one_pow, Complex.ofReal_one]
  show G i j k = star (star (c j)) * G' i j k * star (c k)
  rw [hG, star_star]
  calc G i j k = G i j k * ((c j * star (c j)) * (c k * star (c k))) := by
        rw [hj, hk, one_mul, mul_one]
    _ = c j * (star (c j) * G i j k * c k) * star (c k) := by ring

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Transitivity of the per-slice relation: compose the phases. -/
theorem gramPhaseEquiv_trans {G G' G'' : V → Matrix V V ℂ}
    (h : GramPhaseEquiv G G') (h' : GramPhaseEquiv G' G'') : GramPhaseEquiv G G'' := by
  obtain ⟨c, hc, hG⟩ := h
  obtain ⟨d, hd, hG'⟩ := h'
  refine ⟨fun j => c j * d j, fun j => by rw [norm_mul, hc, hd, one_mul], fun i j k => ?_⟩
  rw [hG', hG, star_mul]
  ring

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- `≈_O` is reflexive. -/
theorem gramTrajEquiv_refl (𝔾 : ℕ → V → Matrix V V ℂ) : GramTrajEquiv 𝔾 𝔾 :=
  fun t => gramPhaseEquiv_refl (𝔾 t)

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- `≈_O` is symmetric. -/
theorem gramTrajEquiv_symm {𝔾 𝔾' : ℕ → V → Matrix V V ℂ} (h : GramTrajEquiv 𝔾 𝔾') :
    GramTrajEquiv 𝔾' 𝔾 :=
  fun t => gramPhaseEquiv_symm (h t)

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- `≈_O` is transitive. -/
theorem gramTrajEquiv_trans {𝔾 𝔾' 𝔾'' : ℕ → V → Matrix V V ℂ}
    (h : GramTrajEquiv 𝔾 𝔾') (h' : GramTrajEquiv 𝔾' 𝔾'') : GramTrajEquiv 𝔾 𝔾'' :=
  fun t => gramPhaseEquiv_trans (h t) (h' t)

/-! ### Section C — the scope boundary against threading, demonstrated -/

/-- **EVERY PAIR ACT 13 LOCALIZED AS THREADING-RELATED IS ONE TRAJECTORY FOR THIS ROUND.** If
`U'_t = W · U_t · K_t` with `W ∈ 𝒢_L` **constant** and `K_t` strong at every `t` — which is act 13's
residual threading freedom exactly — then the two lifts have the **same** fibre-Gram tuple at every
time, by act 12's `fibreGram_left_mul` on the left factor and act 13's
`ct3g_fibreGram_strong_right` on the right, hence the same trajectory with the trivial phase family.

**The threading freedom is invisible to every object of this round**, and this is the enforcement of
the scope boundary: it is mechanical and not a matter of prose. The cost is accepted deliberately —
no outcome of this round can bear on the relative evolution, on the threading, or on any carrier of
act 14. In particular act 11's `GL2` pair, which shares every fibre-Gram matrix at every time and
differs in relative evolution, is **one** trajectory here and this round says nothing whatever about
the difference. -/
theorem gramTrajEquiv_of_threading {a₀ : A} (W : Matrix (V × A) (V × A) ℂ)
    (hW : LeftFibreGroup W) (U K : ℕ → Matrix (V × A) (V × A) ℂ)
    (hK : ∀ t, StrongAnchorStabilizer a₀ (K t)) :
    GramTrajEquiv (fun t => FibreGram a₀ (W * U t * K t)) (fun t => FibreGram a₀ (U t)) := by
  have hstep : ∀ t, FibreGram a₀ (W * U t * K t) = FibreGram a₀ (U t) := by
    intro t
    funext i
    have h1 : FibreGram a₀ ((fun s => W * U s) t * K t) i
        = FibreGram a₀ ((fun s => W * U s) t) i :=
      ct3g_fibreGram_strong_right (fun s => W * U s) K hK i t
    exact h1.trans (fibreGram_left_mul hW a₀ (U t) i)
  intro t
  show GramPhaseEquiv (FibreGram a₀ (W * U t * K t)) (FibreGram a₀ (U t))
  rw [hstep t]
  exact gramPhaseEquiv_refl _

/-! ### Section D — `TJ1`: the admissible trajectory set, characterized pointwise -/

/-- **`TJ1`, NECESSITY** — every coherent lift's Gram trajectory is **pointwise** realizable. Act
12's merged `sh1_necessity` applied at each `t`, with no assembly required and no cross-time content
whatever: `CoherentLift` is definitionally `∀ t, AdmissibleDilationAt (Γ t) a₀ (U t)`. -/
theorem tj1_necessity {a₀ : A} {Γ : ℕ → Matrix V V ℝ} {U : ℕ → Matrix (V × A) (V × A) ℂ}
    (hU : CoherentLift a₀ Γ U) (t : ℕ) :
    RealizableGram A (Γ t) (FibreGram a₀ (U t)) :=
  sh1_necessity (hU t)

/-- **`TJ1`, SUFFICIENCY** — every **pointwise** realizable assignment is some coherent lift's Gram
trajectory. Act 12's merged `sh1_sufficiency` is stated per slice with no hypothesis on `Γ` beyond
realizability, and `CoherentLift` carries no cross-time conjunct, so the assembly is a choice over
`t`. `Classical.choice` appears here and its appearance is not a defect.

**The rank bound `|A|` inside `RealizableGram` is act 12's and is load-bearing**: without it
`sh1_sufficiency` is false. It is consumed here, not re-proved, enlarged or revised. -/
theorem tj1_sufficiency (a₀ : A) {Γ : ℕ → Matrix V V ℝ} {G : ℕ → V → Matrix V V ℂ}
    (hG : ∀ t, RealizableGram A (Γ t) (G t)) :
    ∃ U : ℕ → Matrix (V × A) (V × A) ℂ, CoherentLift a₀ Γ U ∧ ∀ t, FibreGram a₀ (U t) = G t := by
  classical
  choose U hU hGram using fun t => sh1_sufficiency (Γ := Γ t) a₀ (hG t)
  exact ⟨U, hU, hGram⟩

/-- **`TJ1`, THE CHARACTERIZATION** — the Gram trajectories of the coherent lifts of a visible family
are **exactly** the pointwise realizable assignments, so the admissible set is the **product over
time** of the per-slice realizable sets.

**This is the round's null and it is not a selection principle.** It says what the merged record
constrains, which is each slice separately, and it asserts no coupling between slices and denies
none. The narrowing the rank bound effects is **pointwise** and is labelled pointwise: a per-slice
constraint lifted to trajectories is **not** a coupling between times. -/
theorem tj1_trajectory_set (a₀ : A) {Γ : ℕ → Matrix V V ℝ} (G : ℕ → V → Matrix V V ℂ) :
    (∃ U : ℕ → Matrix (V × A) (V × A) ℂ,
        CoherentLift a₀ Γ U ∧ ∀ t, FibreGram a₀ (U t) = G t)
      ↔ ∀ t, RealizableGram A (Γ t) (G t) :=
  ⟨fun ⟨_, hU, hG⟩ t => (hG t) ▸ tj1_necessity hU t, fun hG => tj1_sufficiency a₀ hG⟩

/-- **THERE IS NO ADDITIONAL UNIVERSAL CROSS-TIME CONSTRAINT ON COHERENT GRAM TRAJECTORIES BEYOND
POINTWISE REALIZABILITY**, and the exclusion is a **theorem of this round**, not a failure to find
one.

A cross-time constraint would be a property `Q` holding of `𝔾(U)` for **every** coherent lift `U`
while some **pointwise realizable** assignment failed it. Sufficiency realizes every pointwise
realizable assignment by a coherent lift, and universality then forces `Q` of it: the two demands
are jointly unsatisfiable. What the statement below says is exactly that — universality alone
already forces `Q` of every pointwise realizable assignment, so no such `Q` leaves anything out.

**That is a statement about `CoherentLift` as the programme defines it**, `ℕ`-indexed and pointwise
in time. It is **not** a statement that no cross-time structure could be added to the programme,
**not** a statement that the trajectory question is closed, and **not** a bound on what a later
round could constrain under a different notion of coherence or a larger licensed data set. -/
theorem tj1_no_universal_cross_time_constraint (a₀ : A) (Q : (ℕ → V → Matrix V V ℂ) → Prop)
    (huniv : ∀ (Γ : ℕ → Matrix V V ℝ) (U : ℕ → Matrix (V × A) (V × A) ℂ),
      CoherentLift a₀ Γ U → Q (fun t => FibreGram a₀ (U t)))
    (Γ : ℕ → Matrix V V ℝ) (G : ℕ → V → Matrix V V ℂ)
    (hG : ∀ t, RealizableGram A (Γ t) (G t)) : Q G := by
  obtain ⟨U, hU, hGram⟩ := tj1_sufficiency a₀ hG
  have := huniv Γ U hU
  rwa [funext hGram] at this

/-! ### Section E — `TJ2`: the per-candidate verdicts

Every countercontrol below is at the configuration the freeze names and at no other: act 12's
Hadamard objects at `Γ ≡ ¼`, `|V| = 4`, `|A| = 1`, together with the deterministic island `SH1-C2`
supplies and which is cited but never used as a witness. **No configuration is chosen after an
outcome is known**, and every visible family, lift and matrix below is a **bound variable pinned by
an equation in the statement that needs it**, never a top-level definition. -/

/-- **`TJ2` (a), question (A) — `SP1L-ADD`.** The per-lift law-determination constraint `SP1L` —
if `Γ t = Γ s` then the per-slice orbit classes at `t` and `s` agree — **fails** for act 12's
exhibited lifted `TG3` pair's second member: a coherent lift of a visible family **constant** in
time whose orbit classes at `t = 0` and `t = 1` are inequivalent. The objects are pinned by
equations in the statement and the lift's coherence is a conjunct discharged from act 12's merged
`hadamard_lifts_not_twoSided`.

**So `SP1L` is additional structure and not a consequence of coherence**, which is what a selection
principle must be. This is a verdict on the exact proposition the freeze states under `SP1L`, on its
frozen data grant of `Γ` and the index alone, and on nothing in its neighbourhood. -/
theorem tj2a_sp1l_add :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t s, Γ t = Γ s) ∧ CoherentLift (0 : Fin 1) Γ U
        ∧ Γ 0 = Γ 1
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) (U 0)) (FibreGram (0 : Fin 1) (U 1)) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, _hΓ₀, _hH₁, _hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  refine ⟨fun _ => Γ₀, fun t => if t = 0 then H₁ else Hᵢ, fun _ _ => rfl, ?_, rfl, ?_⟩
  · intro t
    by_cases ht : t = 0
    · simp only [if_pos ht]; exact hadm₁
    · simp only [if_neg ht]; exact hadmᵢ
  · simp only [if_neg (by decide : (1 : ℕ) ≠ 0)]
    exact hnotG

/-- **`TJ2` (c), question (A) — `SP2-ADD`.** Orbit stationarity under a **constant** visible law
fails on the same exhibited lifted `TG3` pair: the visible family is constant and the orbit is not.
`SP2` is the weakest member of the frozen chain `SP5 ⟹ SP1G ⟹ SP1L ⟹ SP2`, so this is the
refutation the other three inherit, and the propagation is reported as propagation rather than as
four discoveries.

**So `SP2` is additional structure.** The verdict is on the exact frozen proposition and on nothing
in its neighbourhood: no other stationarity condition is refuted, named or excluded by it. -/
theorem tj2c_sp2_add :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t s, Γ t = Γ s) ∧ CoherentLift (0 : Fin 1) Γ U
        ∧ ¬ ∀ t s, GramPhaseEquiv (FibreGram (0 : Fin 1) (U t)) (FibreGram (0 : Fin 1) (U s)) := by
  obtain ⟨Γ, U, hconst, hcU, _h01, hne⟩ := tj2a_sp1l_add
  exact ⟨Γ, U, hconst, hcU, fun h => hne (h 0 1)⟩

/-- **`TJ2` (b), question (A) — `SP1G-ADD`.** The cross-lift law-determination claim — a universal
statement **across** lifts — fails at the two **constant** coherent lifts `U ≡ H(1)` and
`U' ≡ H(i)` of one visible family, read across lifts at `t = s = 0`: their visible laws agree by
hypothesis and their per-slice orbit classes do not.

`SP1G` is **not** a member of the frozen selector class `𝒮`: it is a determination claim, not a
predicate on a single lift, and line 4's `∀ S` does not range over it. `SP1G` implies `SP1L` and the
converse fails, so `SP1G` is strictly the stronger and this verdict is the one `SP1L`'s inherits. -/
theorem tj2b_sp1g_add :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      CoherentLift (0 : Fin 1) Γ U ∧ CoherentLift (0 : Fin 1) Γ U'
        ∧ Γ 0 = Γ 0
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) (U 0)) (FibreGram (0 : Fin 1) (U' 0)) := by
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, _hH₁, _hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  exact ⟨fun _ => Γ₀, fun _ => H₁, fun _ => Hᵢ, fun _ => hadm₁, fun _ => hadmᵢ, rfl, hnotG⟩

/-- **`TJ2` (d), question (A) — `SP3-ADD`.** The homogeneous transition rule — one time-independent
rule stepping the hidden datum forward — **fails** for the exhibited coherent lift of the constant
family whose slices are `H(1)`, `H(i)`, `H(1)`, `H(1)` at `t = 0, 1, 2` and `t ≥ 3`: the orbits at
`t = 0` and `t = 2` agree while those at `t = 1` and `t = 3` do not. Each slice's admissibility is
merged, and the inequivalence is merged.

**So `SP3` is additional structure.** What is refuted is the exact parameter-free proposition the
freeze states under `SP3`, on its narrower data grant — the index and its successor only, not `Γ` —
and **no other memorylessness or homogeneity condition** is refuted, named or excluded by it; the
law-reading variant is a different and weaker proposition, named by the freeze and **not executed**
in this round. -/
theorem tj2d_sp3_add :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t s, Γ t = Γ s) ∧ CoherentLift (0 : Fin 1) Γ U
        ∧ GramPhaseEquiv (FibreGram (0 : Fin 1) (U 0)) (FibreGram (0 : Fin 1) (U 2))
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) (U 1)) (FibreGram (0 : Fin 1) (U 3)) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, _hΓ₀, _hH₁, _hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  refine ⟨fun _ => Γ₀, fun t => if t = 1 then Hᵢ else H₁, fun _ _ => rfl, ?_, ?_, ?_⟩
  · intro t
    by_cases ht : t = 1
    · simp only [if_pos ht]; exact hadmᵢ
    · simp only [if_neg ht]; exact hadm₁
  · simp only [if_neg (by decide : (0 : ℕ) ≠ 1), if_neg (by decide : (2 : ℕ) ≠ 1)]
    exact gramPhaseEquiv_refl _
  · simp only [if_neg (by decide : (3 : ℕ) ≠ 1)]
    exact fun h => hnotG (gramPhaseEquiv_symm h)

/-- The two **constant** coherent lifts of the one frozen configuration, `U ≡ H(1)` and
`U' ≡ H(i)`: both coherent lifts of `Γ ≡ ¼`, with trajectories inequivalent under `GramTrajEquiv`
at **every** time and in particular at the named time `t = 0`, certified through act 12's named
`∼_D`-invariant `G^{(0)}_{10} G^{(1)}_{01}`.

**One merged witness family, several consequences.** This is the single pair act 12's `TG3`
exhibits, consumed at its own existential strength; the consequences this round draws from it are
reported as consequences of one witness and never as several independent findings. -/
theorem hadamard_constant_lifts :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U U' : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t s, Γ t = Γ s) ∧ (∀ t s, U t = U s) ∧ (∀ t s, U' t = U' s)
        ∧ CoherentLift (0 : Fin 1) Γ U ∧ CoherentLift (0 : Fin 1) Γ U'
        ∧ ¬ GramTrajEquiv (fun t => FibreGram (0 : Fin 1) (U t))
            (fun t => FibreGram (0 : Fin 1) (U' t)) := by
  obtain ⟨Γ₀, H₁, Hᵢ, _hΓ₀, _hH₁, _hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  exact ⟨fun _ => Γ₀, fun _ => H₁, fun _ => Hᵢ, fun _ _ => rfl, fun _ _ => rfl, fun _ _ => rfl,
    fun _ => hadm₁, fun _ => hadmᵢ, fun h => hnotG (h 0)⟩

/-- **`TJ2` (a), question (B) — `SP1L-NOSEL`.** At the exhibited configuration `Γ ≡ ¼` on
`|V| = 4`, `|A| = 1`, the two constant coherent lifts **both** satisfy `SP1L` — a constant lift has
a constant trajectory, so the implication holds with the trivial phase family — and their
trajectories are **inequivalent under `GramTrajEquiv`** at the named time `t = 0`.

**So `SP1L` does not select there.** This settles **one configuration**: it is not a statement that
`SP1L` fails to select at every configuration, and act 12's `SH1-C2` supplies configurations — the
deterministic visible laws — where the per-slice orbit is unique for free. It is **not** a statement
that no principle selects. -/
theorem tj2a_sp1l_nosel :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (S : (ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) → Prop),
      S = (fun U => ∀ t s, Γ t = Γ s →
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U t)) (FibreGram (0 : Fin 1) (U s)))
        ∧ (∃ U₀, CoherentLift (0 : Fin 1) Γ U₀)
        ∧ ¬ SelectsAt (0 : Fin 1) Γ S := by
  obtain ⟨Γ, U, U', _hΓc, hUc, hU'c, hcU, hcU', hne⟩ := hadamard_constant_lifts
  refine ⟨Γ, _, rfl, ⟨U, hcU⟩, ?_⟩
  rintro ⟨U₀, _hcU₀, _hSU₀, hall⟩
  refine hne (gramTrajEquiv_trans
    (hall U hcU fun t s _ => by rw [hUc t s]; exact gramPhaseEquiv_refl _)
    (gramTrajEquiv_symm
      (hall U' hcU' fun t s _ => by rw [hU'c t s]; exact gramPhaseEquiv_refl _)))

/-- **`TJ2` (c), question (B) — `SP2-NOSEL`.** The same two constant lifts are **stationary** by
construction, so both satisfy orbit stationarity under the constant visible law, and their
trajectories are inequivalent at the named time `t = 0`.

**So `SP2` does not select at that configuration**, and this settles one configuration only. -/
theorem tj2c_sp2_nosel :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (S : (ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) → Prop),
      S = (fun U => (∀ t s, Γ t = Γ s) → ∀ t s,
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U t)) (FibreGram (0 : Fin 1) (U s)))
        ∧ (∃ U₀, CoherentLift (0 : Fin 1) Γ U₀)
        ∧ ¬ SelectsAt (0 : Fin 1) Γ S := by
  obtain ⟨Γ, U, U', _hΓc, hUc, hU'c, hcU, hcU', hne⟩ := hadamard_constant_lifts
  refine ⟨Γ, _, rfl, ⟨U, hcU⟩, ?_⟩
  rintro ⟨U₀, _hcU₀, _hSU₀, hall⟩
  refine hne (gramTrajEquiv_trans
    (hall U hcU fun _ t s => by rw [hUc t s]; exact gramPhaseEquiv_refl _)
    (gramTrajEquiv_symm
      (hall U' hcU' fun _ t s => by rw [hU'c t s]; exact gramPhaseEquiv_refl _)))

/-- **`TJ2` (d), question (B) — `SP3-NOSEL`.** The same two constant lifts each have a constant
trajectory, so each satisfies the homogeneous transition rule — the conclusion of the implication is
reflexivity — and they are inequivalent at the named time `t = 0`.

**So `SP3` does not select at that configuration**, and this settles one configuration only. -/
theorem tj2d_sp3_nosel :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (S : (ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) → Prop),
      S = (fun U => ∀ t s,
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U t)) (FibreGram (0 : Fin 1) (U s)) →
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U (t + 1))) (FibreGram (0 : Fin 1) (U (s + 1))))
        ∧ (∃ U₀, CoherentLift (0 : Fin 1) Γ U₀)
        ∧ ¬ SelectsAt (0 : Fin 1) Γ S := by
  obtain ⟨Γ, U, U', _hΓc, hUc, hU'c, hcU, hcU', hne⟩ := hadamard_constant_lifts
  refine ⟨Γ, _, rfl, ⟨U, hcU⟩, ?_⟩
  rintro ⟨U₀, _hcU₀, _hSU₀, hall⟩
  refine hne (gramTrajEquiv_trans
    (hall U hcU fun t s _ => by
      rw [hUc (t + 1) (s + 1)]; exact gramPhaseEquiv_refl _)
    (gramTrajEquiv_symm
      (hall U' hcU' fun t s _ => by
        rw [hU'c (t + 1) (s + 1)]; exact gramPhaseEquiv_refl _)))

/-- **`TJ2` (e), question (B) — `SP5-EMPTY`.** At the exhibited configuration `Γ ≡ ¼` on `|V| = 4`,
`|A| = 1`, **no** coherent lift satisfies the decoherence rule, proved **universally over the lifts
of that family**, while the family **does** have coherent lifts, exhibited.

**The excluded quantity is computed.** At `|A| = 1` admissibility forces `‖U_t(i,0)(j,0)‖² = ¼` at
every entry, so `‖G^{(i)}_{jk}‖ = ¼` at every `j`, `k` — the off-diagonal Gram mass is `¼` and never
zero — while phase equivalence preserves vanishing entrywise and the diagonal tuple's off-diagonal
entries are zero. Every coherent lift of this family is therefore excluded.

**So `SP5` does not select there, by excluding every trajectory rather than by leaving several.**
The two mechanisms are kept apart: this is **not** the outcome in which several trajectories
survive. It settles one configuration and is not a statement about every configuration. -/
theorem tj2e_sp5_empty :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U₀ : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t i j, Γ t i j = 1 / 4) ∧ CoherentLift (0 : Fin 1) Γ U₀
        ∧ (∀ U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, CoherentLift (0 : Fin 1) Γ U →
            ∀ t j k, ‖FibreGram (0 : Fin 1) (U t) 0 j k‖ = 1 / 4)
        ∧ (∀ U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ, CoherentLift (0 : Fin 1) Γ U →
            ¬ ∀ t, GramPhaseEquiv (FibreGram (0 : Fin 1) (U t))
                (fun i => Matrix.diagonal (fun j => (((Γ t) i j : ℝ) : ℂ)))) := by
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, _hH₁, _hHᵢ, hadm₁, _hadmᵢ, _hnotG, _⟩ := hadamard_slices_not_twoSided
  have hentry : ∀ (U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      CoherentLift (0 : Fin 1) (fun _ => Γ₀) U → ∀ t i j, ‖U t (i, 0) (j, 0)‖ = 1 / 2 := by
    intro U hU t i j
    have h := (hU t).2 i j
    rw [hΓ₀] at h
    simp only [Matrix.of_apply, Fin.sum_univ_one] at h
    have hsq : ‖U t (i, 0) (j, 0)‖ ^ 2 = (1 / 2 : ℝ) ^ 2 := by rw [← h]; norm_num
    have hnn : (0 : ℝ) ≤ ‖U t (i, 0) (j, 0)‖ := norm_nonneg _
    nlinarith [hsq, hnn]
  have hgram : ∀ (U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      CoherentLift (0 : Fin 1) (fun _ => Γ₀) U →
      ∀ t j k, ‖FibreGram (0 : Fin 1) (U t) 0 j k‖ = 1 / 4 := by
    intro U hU t j k
    rw [fibreGram_apply]
    simp only [Fin.sum_univ_one]
    rw [norm_mul, norm_star, hentry U hU t 0 j, hentry U hU t 0 k]
    norm_num
  refine ⟨fun _ => Γ₀, fun _ => H₁, fun _ i j => by rw [hΓ₀]; rfl, fun _ => hadm₁, hgram, ?_⟩
  intro U hU hSP5
  obtain ⟨c, hc, heq⟩ := hSP5 0
  have h01 := heq 0 0 1
  simp only [Matrix.diagonal_apply_ne _ (show (0 : Fin 4) ≠ 1 by decide)] at h01
  have hz : ‖FibreGram (0 : Fin 1) (U 0) 0 0 1‖ = 0 := by
    have hzz : ‖star (c 0) * FibreGram (0 : Fin 1) (U 0) 0 0 1 * c 1‖ = 0 := by
      rw [← h01]; simp
    rwa [norm_mul, norm_mul, norm_star, hc, hc, one_mul, mul_one] at hzz
  rw [hgram U hU 0 0 1] at hz
  norm_num at hz

/-- **`TJ2` (e), question (A) — `SP5-ADD`.** The decoherence rule — the per-slice orbit is the class
of the diagonal tuple built from the visible law, so that the orbit carries no off-diagonal Gram
mass at all — **fails** at `H(1)` itself, the exhibited coherent lift of the exhibited constant
visible family `Γ ≡ ¼` on `|V| = 4`, `|A| = 1`.

At `|A| = 1` the tuple is `G^{(i)}_{jk} = conj(U_{ij}) U_{ik}` by act 12's `fibreGram_apply`, and
admissibility forces every anchored entry to have modulus `½`, so the off-diagonal entry
`G^{(0)}_{01}` has modulus `¼` and is **nonzero** while the diagonal tuple's is zero — and phase
equivalence preserves vanishing entrywise. At this configuration the verdict is the emptiness
verdict's specialization to the exhibited lift, which is why it is read off `tj2e_sp5_empty` rather
than recomputed.

`SP5` implies `SP1G` and the converse fails, so `SP5` is strictly the strongest of the four
law-facing candidates. **So `SP5` is additional structure and not a consequence of coherence.** What
is refuted is the exact proposition the freeze states under `SP5`, on its frozen data grant of `Γ`
and the index alone: **no decoherence condition in general** is refuted, named or excluded by it,
and nothing in its neighbourhood is touched. -/
theorem tj2e_sp5_add :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (U : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      CoherentLift (0 : Fin 1) Γ U
        ∧ ‖FibreGram (0 : Fin 1) (U 0) 0 0 1‖ = 1 / 4
        ∧ ¬ ∀ t, GramPhaseEquiv (FibreGram (0 : Fin 1) (U t))
            (fun i => Matrix.diagonal (fun j => (((Γ t) i j : ℝ) : ℂ))) := by
  obtain ⟨Γ, U₀, _hΓ, hcU₀, hgram, hempty⟩ := tj2e_sp5_empty
  exact ⟨Γ, U₀, hcU₀, hgram U₀ hcU₀ 0 0 1, hempty U₀ hcU₀⟩

/-- **`TJ2` (f) — `SP4-THM`, and vacuous.** The out-of-regime probe, granted act 13's level-2
cross-time datum which is forbidden to every member of the frozen class: two coherent lifts with the
same fibre cross-Gram trajectory have the same Gram trajectory.

**The finding is the containment and not a selection.** Act 13's `fibreCrossGram_diag` is a
definitional identity — `Ξ_i^{(t,t)}(U) = G^{(i)}(U_t)` — so the level-2 datum **contains** the Gram
trajectory at its diagonal, and a rule permitted to read it determines the trajectory by containing
it. The hypothesis is never satisfied by anything this round licenses a candidate to consult.

**`SP4` is not a member of the frozen selector class**, no line of the hierarchy quantifies over it,
and no outcome of `SP4` is evidence for or against any member of that class, in either direction. -/
theorem tj2f_sp4_containment {a₀ : A} {Γ Γ' : ℕ → Matrix V V ℝ}
    {U U' : ℕ → Matrix (V × A) (V × A) ℂ}
    (_hU : CoherentLift a₀ Γ U) (_hU' : CoherentLift a₀ Γ' U')
    (h : ∀ (i : V) (t s : ℕ), FibreCrossGram a₀ U i t s = FibreCrossGram a₀ U' i t s) :
    GramTrajEquiv (fun t => FibreGram a₀ (U t)) (fun t => FibreGram a₀ (U' t)) := by
  intro t
  have : (fun i => FibreGram a₀ (U t) i) = fun i => FibreGram a₀ (U' t) i := by
    funext i
    rw [← fibreCrossGram_diag a₀ U i t, ← fibreCrossGram_diag a₀ U' i t]
    exact h i t t
  show GramPhaseEquiv (FibreGram a₀ (U t)) (FibreGram a₀ (U' t))
  rw [show FibreGram a₀ (U t) = FibreGram a₀ (U' t) from this]
  exact gramPhaseEquiv_refl _

/-! ### Section G — `TJ3` line 4: class-level selection impossibility, `∃ C ∀ S` -/

/-- **`TJ3`, LINE 4 — `TJ3-IMP`, CLASS-LEVEL SELECTION IMPOSSIBILITY.**

**THERE EXISTS a configuration** — `|V| = 4`, `|A| = 1`, anchor `0`, the visible family `Γ ≡ ¼`
constant in time — **ADMISSIBLE under exactly this round's own constraints**, the family having at
least one coherent lift, exhibited as a conjunct, **AND such that FOR EVERY selector `S` in the
frozen four-member class `𝒮 = {SP1L, SP2, SP3, SP5}`, `S` FAILS TO SELECT there.**

The statement records which of the two mechanisms holds for each member separately: `SP1L`, `SP2`
and `SP3` are each satisfied by **two** coherent lifts whose trajectories are
`GramTrajEquiv`-inequivalent, while `SP5` is satisfied by **no** coherent lift of the family at all.

**The quantifier order is `∃ C ∀ S` and it is load-bearing**: the countermodel is chosen **first**
and defeats all four. The reversed order `∀ S ∃ C` is a strictly weaker statement — the conjunction
of the four per-candidate verdicts — and is **not** this theorem.

**This is impossibility within a frozen class of four named principles at one exhibited
configuration.** It is **not** impossibility over all conceivable selection principles, **not** a
statement that no selection principle exists, **not** a statement that selection fails at every
configuration — act 12's `SH1-C2` supplies deterministic visible laws where the per-slice orbit is
unique for free — and **not** a bound on what a later round could name or prove. It was earned by an
**exhibited** countermodel and never by a search. -/
theorem tj3_imp_class_level_selection_impossibility :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (SP1L SP2 SP3 SP5 : (ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) → Prop)
      (U₀ U₁ : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ SP1L = (fun U => ∀ t s, Γ t = Γ s →
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U t)) (FibreGram (0 : Fin 1) (U s)))
        ∧ SP2 = (fun U => (∀ t s, Γ t = Γ s) → ∀ t s,
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U t)) (FibreGram (0 : Fin 1) (U s)))
        ∧ SP3 = (fun U => ∀ t s,
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U t)) (FibreGram (0 : Fin 1) (U s)) →
            GramPhaseEquiv (FibreGram (0 : Fin 1) (U (t + 1))) (FibreGram (0 : Fin 1) (U (s + 1))))
        ∧ SP5 = (fun U => ∀ t, GramPhaseEquiv (FibreGram (0 : Fin 1) (U t))
            (fun i => Matrix.diagonal (fun j => (((Γ t) i j : ℝ) : ℂ))))
        ∧ CoherentLift (0 : Fin 1) Γ U₀ ∧ CoherentLift (0 : Fin 1) Γ U₁
        ∧ (SP1L U₀ ∧ SP1L U₁ ∧ SP2 U₀ ∧ SP2 U₁ ∧ SP3 U₀ ∧ SP3 U₁)
        ∧ ¬ GramTrajEquiv (fun t => FibreGram (0 : Fin 1) (U₀ t))
            (fun t => FibreGram (0 : Fin 1) (U₁ t))
        ∧ (∀ U, CoherentLift (0 : Fin 1) Γ U → ¬ SP5 U)
        ∧ ∀ S ∈ ({SP1L, SP2, SP3, SP5} : Set ((ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) → Prop)),
            ¬ SelectsAt (0 : Fin 1) Γ S := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, _hH₁, _hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  obtain ⟨Γe, U₀e, hΓe, hcU₀e, hgrame, hempty⟩ := tj2e_sp5_empty
  -- the configuration is fixed FIRST, before any selector is quantified over
  set Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ := fun _ => Γ₀ with hΓdef
  set U₀ : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ := fun _ => H₁ with hU₀def
  set U₁ : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ := fun _ => Hᵢ with hU₁def
  have hcU₀ : CoherentLift (0 : Fin 1) Γ U₀ := fun _ => hadm₁
  have hcU₁ : CoherentLift (0 : Fin 1) Γ U₁ := fun _ => hadmᵢ
  have hineq : ¬ GramTrajEquiv (fun t => FibreGram (0 : Fin 1) (U₀ t))
      (fun t => FibreGram (0 : Fin 1) (U₁ t)) := fun h => hnotG (h 0)
  have hconstΓ : ∀ t i j, Γ t i j = 1 / 4 := by
    intro _ i j; rw [hΓdef, hΓ₀]; rfl
  -- SP5 is satisfied by NO coherent lift of this family: the emptiness is transported from
  -- `tj2e_sp5_empty` at the same configuration, whose visible family is the same constant `¼`.
  have hΓeq : Γe = Γ := by
    funext t; ext i j; rw [hΓe t i j, hconstΓ t i j]
  have hSP5empty : ∀ U, CoherentLift (0 : Fin 1) Γ U →
      ¬ ∀ t, GramPhaseEquiv (FibreGram (0 : Fin 1) (U t))
          (fun i => Matrix.diagonal (fun j => (((Γ t) i j : ℝ) : ℂ))) := by
    rw [← hΓeq]; exact hempty
  refine ⟨Γ, _, _, _, _, U₀, U₁, hconstΓ, rfl, rfl, rfl, rfl, hcU₀, hcU₁,
    ⟨fun t s _ => gramPhaseEquiv_refl _, fun t s _ => gramPhaseEquiv_refl _,
     fun _ t s => gramPhaseEquiv_refl _, fun _ t s => gramPhaseEquiv_refl _,
     fun t s _ => gramPhaseEquiv_refl _, fun t s _ => gramPhaseEquiv_refl _⟩,
    hineq, hSP5empty, ?_⟩
  -- and now, the configuration being fixed, EVERY member of the four-member class fails to select
  have hsurv : ∀ S : (ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) → Prop,
      S U₀ → S U₁ → ¬ SelectsAt (0 : Fin 1) Γ S := by
    rintro S hS₀ hS₁ ⟨W, _hcW, _hSW, hall⟩
    exact hineq (gramTrajEquiv_trans (hall U₀ hcU₀ hS₀)
      (gramTrajEquiv_symm (hall U₁ hcU₁ hS₁)))
  rintro S (rfl | rfl | rfl | rfl)
  · exact hsurv _ (fun t s _ => gramPhaseEquiv_refl _)
      (fun t s _ => gramPhaseEquiv_refl _)
  · exact hsurv _ (fun _ t s => gramPhaseEquiv_refl _)
      (fun _ t s => gramPhaseEquiv_refl _)
  · exact hsurv _ (fun t s _ => gramPhaseEquiv_refl _)
      (fun t s _ => gramPhaseEquiv_refl _)
  · rintro ⟨W, hcW, hSW, _⟩
    exact hSP5empty W hcW hSW

end GramTrajectorySelection
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.GramTrajectorySelection.gramPhaseEquiv_refl
#print axioms OIBridge.GramTrajectorySelection.gramPhaseEquiv_symm
#print axioms OIBridge.GramTrajectorySelection.gramPhaseEquiv_trans
#print axioms OIBridge.GramTrajectorySelection.gramTrajEquiv_refl
#print axioms OIBridge.GramTrajectorySelection.gramTrajEquiv_symm
#print axioms OIBridge.GramTrajectorySelection.gramTrajEquiv_trans
#print axioms OIBridge.GramTrajectorySelection.gramTrajEquiv_of_threading
#print axioms OIBridge.GramTrajectorySelection.tj1_necessity
#print axioms OIBridge.GramTrajectorySelection.tj1_sufficiency
#print axioms OIBridge.GramTrajectorySelection.tj1_trajectory_set
#print axioms OIBridge.GramTrajectorySelection.tj1_no_universal_cross_time_constraint
#print axioms OIBridge.GramTrajectorySelection.tj2a_sp1l_add
#print axioms OIBridge.GramTrajectorySelection.tj2c_sp2_add
#print axioms OIBridge.GramTrajectorySelection.tj2b_sp1g_add
#print axioms OIBridge.GramTrajectorySelection.tj2d_sp3_add
#print axioms OIBridge.GramTrajectorySelection.tj2e_sp5_add
#print axioms OIBridge.GramTrajectorySelection.hadamard_constant_lifts
#print axioms OIBridge.GramTrajectorySelection.tj2a_sp1l_nosel
#print axioms OIBridge.GramTrajectorySelection.tj2c_sp2_nosel
#print axioms OIBridge.GramTrajectorySelection.tj2d_sp3_nosel
#print axioms OIBridge.GramTrajectorySelection.tj2e_sp5_empty
#print axioms OIBridge.GramTrajectorySelection.tj2f_sp4_containment
#print axioms OIBridge.GramTrajectorySelection.tj3_imp_class_level_selection_impossibility
