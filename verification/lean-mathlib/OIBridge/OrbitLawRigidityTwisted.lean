import OIBridge.RepresentativeNaturality
import OIBridge.IntermediateCrossTimeStructure

/-!
# Act 21 — the rigidity of the cross-time laws act 18 opened, re-frozen at act 20's certified naturality

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md`, blob
`316d635a31f91faebeeebef7688b30002d24b4ca`, as amended by
`verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md`,
blob `d140978e6f0031063e7aa4b9bbe3e960d9b7f8e1`, from `main` at
`10d1041bcc10f25d9f643629d4431acbd0f65a1e` — the certified merge commit of that amendment, which
Amendment 1 fixes as this round's mandated execution base `B` and whose two frozen blobs this
execution verified as its first act.

## What this round is

Act 19 froze a bounded rigidity census over a ladder of conditions and closed without a headline,
because its naturality rung was underspecified; act 20 classified the three notions that phrase was
standing in for and certified the carrier relabelling's lift **twisted-natural and not strictly
natural**. Act 21 re-freezes act 19's experiment with **one** mathematical change: the naturality
rung `L4n` is act 20's `TwistedNatural` itself, with act 20's two `RNT2` lifting obligations stated
across one time step and **no** constraint on the induced maps beyond act 20's two closure
conjuncts. Everything else — the question, the objects, the quotient list, `L0`, `L1`, `L2`, `L3i`,
`L3s`, `L4d`, `L5`, the shared theorem, the headlines, the discriminating test and the seven
candidates — is act 19's, carried by line range from act 19's pinned blob.

**THE CLAUSE, carried at this mention — the module docstring.**
Act 21 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.**

## The ladder, stated first

Section A states the ladder `L0`–`L5` as the eight definitions the freeze's budget names, **in the
wording the freeze fixes for each, before any discriminating result** — no theorem, no candidate
law, no census, no survivor, no witness of the discriminating test is present at the commit that
introduces this section. That ordering is the freeze's ordering obligation, and the commit at which
Section A is complete is the round's **ladder commit**, record 2 of the result note.

Every object is the merged record's own, consumed unmodified at merged strength: act 12's
`FibreGram`, `GramPhaseEquiv`, `RealizableGram` and `LeftFibreGroup`; act 11's
`WeakAnchorStabilizer`; act 7's `AdmissibleDilationAt` under act 7's readback convention with `D4b`
**negative**; act 17's `GramTrajEquiv`; act 18's `ProperAt` and `PropagatesFrom`; and act 20's
`TwistedNatural`. **A merged statement is not enlarged by being consumed.**

**Act 7's boundary is carried at every use of the visible family**: act 7's `D4b` came back negative
— Source A supplies no general map carrying the relative candidate on the dilated carrier back to
`V` — and the readback is the repository's own, frozen by act 7's readback amendment.

Act 19's control plane and closure are read and not edited; act 19's uncertified conclusions are
**uncertified and not refuted**; act 19's execution branch is research material which nothing here
cites, imports, adapts or counts. Everything this round uses, it proves under its own freeze.
-/

namespace OIBridge
namespace OrbitLawRigidityTwisted

open Matrix CoherentLiftGauge DilationChoice TwoSidedGauge GramTrajectorySelection
  IntermediateCrossTimeStructure RepresentativeNaturality

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the ladder `L0`–`L5`, in the freeze's wording, before any discriminating result

Throughout, a **transition family** is `Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)`, written at
representative level; the **law it generates** is `Law_Φ 𝔾 ≡ ∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`,
a law datum in act 18's sense — written from `(a₀, Γ, ℕ)` alone and consulting no lift. The
**admissible orbit state space** `Ω(Γ, t)` is the set of `GramPhaseEquiv`-classes of tuples
satisfying `RealizableGram A (Γ t)`, act 12's `SH1` characterizing membership with the `|A|` rank
bound inside it. -/

/-- **`TransitionLaw`** (budget slot 1) — the law a transition family generates, carrying the `L4d`
descent conjunct as its first conjunct: `Φ` respects act 12's `GramPhaseEquiv` in its argument at
every `t`, and `Law 𝔾 ↔ ∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`. Every rung and every candidate is
stated over it. The descent conjunct is part of the object and not commentary on it, for the reason
act 18 recorded for `LC3`: a representative-level transition that does not descend "selects" by
fixing an unphysical frame. -/
def TransitionLaw (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (Law : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  (∀ t (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    ∧ ∀ 𝔾 : ℕ → V → Matrix V V ℂ, Law 𝔾 ↔ ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))

variable (A) in
/-- **`L0` — `EvolvesTotally`** (budget slot 2), a well-defined total evolution on the admissible
orbit state space: for **every** `ω ∈ Ω_0` there is a pointwise realizable solution `𝔾` of `Law_Φ`
with `[𝔾 0] = ω`. Uniqueness modulo `≈_O` is act 18's propagation clause (i), the ladder's standing
hypothesis, so `L0` is the **existence** half and nothing else: the gap between "propagates from
every initial orbit it admits" and "admits every initial orbit". -/
def EvolvesTotally (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  ∀ G₀ : V → Matrix V V ℂ, RealizableGram A (Γ 0) G₀ →
    ∃ 𝔾 : ℕ → V → Matrix V V ℂ, (∀ t, RealizableGram A (Γ t) (𝔾 t))
      ∧ (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) ∧ GramPhaseEquiv (𝔾 0) G₀

variable (A) in
/-- **`L1` — `PreservesAdmissible`** (budget slot 3), preservation of pointwise admissibility, stated
**for the relation on the whole per-slice orbit space** and not merely along solutions: for every
`G` with `RealizableGram A (Γ t) G`, the tuple `Φ t G` satisfies `RealizableGram A (Γ (t+1)) (Φ t G)`.
Restricted to solutions the condition is close to vacuous; stated for the whole orbit space it is a
real demand on `Φ`, which is the demand the rung makes. -/
def PreservesAdmissible (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  ∀ t (G : V → Matrix V V ℂ), RealizableGram A (Γ t) G → RealizableGram A (Γ (t + 1)) (Φ t G)

variable (A) in
/-- **`L3` — `Reversible`** (budget slot 4), reversibility as **two conjuncts reported apart**,
stated of `Φ t` at each `t` (under `L2` a single `Φ̂`, so this is the freeze's statement of `Φ̂`):

* **`L3i`, injectivity on classes** — for `G`, `G'` admissible at time `t`,
  `GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G'`;
* **`L3s`, surjectivity** — every class admissible at time `t+1` is in the image: for every
  admissible `G'` there is an admissible `G` with `GramPhaseEquiv (Φ t G) G'`.

`Ω_t` is not known to be finite, so the two conjuncts are stated and reported apart, and a verdict
that reaches one is not reported as reaching the other. -/
def Reversible (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  (∀ t (G G' : V → Matrix V V ℂ), RealizableGram A (Γ t) G → RealizableGram A (Γ t) G' →
      GramPhaseEquiv (Φ t G) (Φ t G') → GramPhaseEquiv G G')
    ∧ ∀ t (G' : V → Matrix V V ℂ), RealizableGram A (Γ (t + 1)) G' →
        ∃ G : V → Matrix V V ℂ, RealizableGram A (Γ t) G ∧ GramPhaseEquiv (Φ t G) G'

variable (A) in
/-- **`L5` — `FactorizesOnProduct`** (budget slot 5, conditional — fired, `L5` being retained by owner
settlement), composition of independent systems at a **product configuration**: the carrier is
identified with a product `V ≃ V₁ × V₂` by `e`, the ancilla has the product cardinality
`|A| = |A₁| · |A₂|`, the visible family is the **pointwise product** of two visible families through
`e`, and the transition **factorizes on product classes**: there are transition families `Φ₁` on
`Ω(Γ₁, ·)` and `Φ₂` on `Ω(Γ₂, ·)` with `Φ t (G₁ ⊠ G₂) ≈ (Φ₁ t G₁) ⊠ (Φ₂ t G₂)` for every pair of
admissible `G₁`, `G₂`, the equivalence act 12's `GramPhaseEquiv` and `⊠` the product embedding on
fibre-Gram tuples — entrywise `(G₁ ⊠ G₂) i j k = G₁ i₁ j₁ k₁ · G₂ i₂ j₂ k₂` through `e` — which is
what the Kronecker product of admissible dilations induces.

Nothing in this statement mentions unitary evolution, a generator, a one-parameter group,
continuity, a Hamiltonian or Schrödinger's equation; every object in it is the repository's own. -/
def FactorizesOnProduct {V₁ V₂ : Type} [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂]
    (A₁ A₂ : Type) [Fintype A₁] [Fintype A₂] (e : V ≃ V₁ × V₂)
    (Γ₁ : ℕ → Matrix V₁ V₁ ℝ) (Γ₂ : ℕ → Matrix V₂ V₂ ℝ) (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  Fintype.card A = Fintype.card A₁ * Fintype.card A₂
    ∧ (∀ t i j, Γ t i j = Γ₁ t (e i).1 (e j).1 * Γ₂ t (e i).2 (e j).2)
    ∧ ∃ (Φ₁ : ℕ → (V₁ → Matrix V₁ V₁ ℂ) → (V₁ → Matrix V₁ V₁ ℂ))
        (Φ₂ : ℕ → (V₂ → Matrix V₂ V₂ ℂ) → (V₂ → Matrix V₂ V₂ ℂ)),
        ∀ t (G₁ : V₁ → Matrix V₁ V₁ ℂ) (G₂ : V₂ → Matrix V₂ V₂ ℂ),
          RealizableGram A₁ (Γ₁ t) G₁ → RealizableGram A₂ (Γ₂ t) G₂ →
            GramPhaseEquiv
              (Φ t (fun i => Matrix.of fun j k =>
                G₁ (e i).1 (e j).1 (e k).1 * G₂ (e i).2 (e j).2 (e k).2))
              (fun i => Matrix.of fun j k =>
                Φ₁ t G₁ (e i).1 (e j).1 (e k).1 * Φ₂ t G₂ (e i).2 (e j).2 (e k).2)

/-- **`LadderConds`** (budget slot 6) — the conjunction the headline quantifies over, as **one**
`Prop`, in the freeze's order: the standing hypothesis that the generated law is an `L-PROP` law in
act 18's frozen sense (`ProperAt` and `PropagatesFrom`), then `L0`, `L1`, `L2`, `L3` (both
conjuncts), `L4d`, `L4n` and `L5`. **This is the single declaration the ordering obligation pins.**

* **`L2`**, inline: there is a single `Φ₀` with `Φ t = Φ₀` at every `t`, so one law iterates
  consistently; the induced evolution then composes, `E_t = Φ₀^t` on classes, by induction once
  descent has made `Φ₀` a function on classes.
* **`L4d`**, inline: `Φ` respects act 12's `GramPhaseEquiv` in its argument — the first conjunct of
  `TransitionLaw`, and the shared theorem's own hypothesis (`L4d-HYP`).
* **`L4n`**, inline, **at act 20's certified strength**: at every `t`, `Φ t` admits a
  representative-level lift that is **twisted-natural** in act 20's frozen sense `N-TWIST` — there
  are a map `Ψ` on dilations and maps `αL`, `αR` on dilations, all three **fixed before the
  quantifier over inputs**, such that **(i) lifting**, `FibreGram a₀ (Ψ U) = Φ t (FibreGram a₀ U)` for
  every `U` admissible for `Γ t` at `a₀`; **(ii) admissibility**, `Ψ U` admissible for `Γ (t+1)` at
  `a₀` for every such `U`; and **(iii) twisted equivariance**, `TwistedNatural a₀ αL αR Ψ`, act 20's
  declaration consumed unrestated. The quantifier order is `∃ Ψ αL αR, ∀ L U K` and never
  `∀ L U K, ∃`; **no constraint is placed on the induced maps beyond act 20's two closure
  conjuncts**.
* **`L5`**, at the product configuration `e`, `Γ₁`, `Γ₂`, through `FactorizesOnProduct`. -/
def LadderConds {V₁ V₂ : Type} [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂]
    (A₁ A₂ : Type) [Fintype A₁] [Fintype A₂] (a₀ : A) (Γ : ℕ → Matrix V V ℝ) (e : V ≃ V₁ × V₂)
    (Γ₁ : ℕ → Matrix V₁ V₁ ℝ) (Γ₂ : ℕ → Matrix V₂ V₂ ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  ProperAt a₀ Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
    ∧ PropagatesFrom a₀ Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
    ∧ EvolvesTotally A Γ Φ
    ∧ PreservesAdmissible A Γ Φ
    ∧ (∃ Φ₀ : (V → Matrix V V ℂ) → (V → Matrix V V ℂ), ∀ t, Φ t = Φ₀)
    ∧ Reversible A Γ Φ
    ∧ (∀ t (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    ∧ (∀ t, ∃ Ψ αL αR : Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ,
        (∀ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt (Γ t) a₀ U →
          FibreGram a₀ (Ψ U) = Φ t (FibreGram a₀ U))
        ∧ (∀ U : Matrix (V × A) (V × A) ℂ, AdmissibleDilationAt (Γ t) a₀ U →
          AdmissibleDilationAt (Γ (t + 1)) a₀ (Ψ U))
        ∧ TwistedNatural a₀ αL αR Ψ)
    ∧ FactorizesOnProduct A A₁ A₂ e Γ₁ Γ₂ Γ Φ

variable (A) in
/-- **`LawEquiv`, `≈_L`** (budget slot 7) — the law equivalence of the frozen quotient list, which is
**not a new relation**: two laws are equivalent iff they have the same solution set among pointwise
realizable trajectories. It is set equality of solution sets, defined from act 12's `GramPhaseEquiv`,
act 17's `GramTrajEquiv` and equality alone, and identifies no objects those do not already identify.
-/
def LawEquiv (Γ : ℕ → Matrix V V ℝ) (Law Law' : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  ∀ 𝔾 : ℕ → V → Matrix V V ℂ, (∀ t, RealizableGram A (Γ t) (𝔾 t)) → (Law 𝔾 ↔ Law' 𝔾)

/-- **`SameInitialOrbitPair`, `SIOP`** (budget slot 8) — the discriminating test as one `Prop`, with
its quantifiers as the freeze writes them and **carrying the earlier-agreement conjunct**: two
transition families satisfying the frozen ladder at one configuration, whose laws are **not** `≈_L`,
with pointwise realizable solutions handed the **same initial orbit class** — agreement at every
`s < t*` — that **first diverge** at `t* ≥ 1`. The earlier-agreement conjunct is part of the witness
and not commentary on it: a difference at a later time caused by feeding already-different states
forward is a propagated divergence and not primitive non-uniqueness. The initial orbit `[𝔾 0]` is a
component of the existential witness and, under the freeze's witness rule, ranges over the frozen
supply and never outside it. -/
def SameInitialOrbitPair (V A V₁ V₂ A₁ A₂ : Type) [Fintype V] [DecidableEq V] [Fintype A]
    [DecidableEq A] [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂] [Fintype A₁]
    [Fintype A₂] : Prop :=
  ∃ (Γ : ℕ → Matrix V V ℝ) (a₀ : A) (e : V ≃ V₁ × V₂) (Γ₁ : ℕ → Matrix V₁ V₁ ℝ)
    (Γ₂ : ℕ → Matrix V₂ V₂ ℝ) (Φ Φ' : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (𝔾 𝔾' : ℕ → V → Matrix V V ℂ) (t : ℕ),
    LadderConds A₁ A₂ a₀ Γ e Γ₁ Γ₂ Φ ∧ LadderConds A₁ A₂ a₀ Γ e Γ₁ Γ₂ Φ'
      ∧ ¬ LawEquiv A Γ (fun 𝔾 => ∀ s, GramPhaseEquiv (𝔾 (s + 1)) (Φ s (𝔾 s)))
          (fun 𝔾 => ∀ s, GramPhaseEquiv (𝔾 (s + 1)) (Φ' s (𝔾 s)))
      ∧ (∀ s, RealizableGram A (Γ s) (𝔾 s)) ∧ (∀ s, RealizableGram A (Γ s) (𝔾' s))
      ∧ (∀ s, GramPhaseEquiv (𝔾 (s + 1)) (Φ s (𝔾 s)))
      ∧ (∀ s, GramPhaseEquiv (𝔾' (s + 1)) (Φ' s (𝔾' s)))
      ∧ 1 ≤ t
      ∧ (∀ s, s < t → GramPhaseEquiv (𝔾 s) (𝔾' s))
      ∧ ¬ GramPhaseEquiv (𝔾 t) (𝔾' t)


/-! ### Section B — `OL1`, the shared structural theorem, which runs first

`OL1` (a) is a **descent** statement: a transition family that respects act 12's `GramPhaseEquiv`
in its argument (`L4d`) induces, on the admissible orbit state spaces, the composable family of maps
`Φ̄_t` and the composite `E_t = Φ̄_{t-1} ∘ ⋯ ∘ Φ̄_0`, so that a solution's class at time `t` is a
function of its initial class alone. The composite is written inline with `Nat.rec`, spending no
definition slot. `OL1` (b) is the time-homogeneous form: with `L2` the family is one map `Φ₀` and
`E_t = Φ₀^[t]`, a monoid action of `(ℕ, +)` on the admissible orbit space.

**The `TJ1` dependence is named at the step and not in a footnote**: reading the solution set as a
composition of maps on per-time state spaces requires the ambient admissible set to be the product
over time of those spaces, which is act 17's `tj1_trajectory_set` and is consumed as the third
conjunct of (a). **`OL1` is not an existence statement** — that an `L-PROP` law exists is act 18's
— and it says nothing about faithfulness, transitivity, freeness or any symmetry of the induced
action; it realizes `Φ̄` as no operator, unitary, generator or group element. It is proved for every
transition family with descent, the standing `L-PROP` hypothesis playing no part in it. -/

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Descent transports along the composite: if `G ≈ G'` then `E_t G ≈ E_t G'`. -/
theorem composite_descends {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    (hd : ∀ t (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    {G G' : V → Matrix V V ℂ} (h : GramPhaseEquiv G G') (t : ℕ) :
    GramPhaseEquiv (Nat.rec (motive := fun _ => V → Matrix V V ℂ) G (fun s H => Φ s H) t)
      (Nat.rec (motive := fun _ => V → Matrix V V ℂ) G' (fun s H => Φ s H) t) := by
  induction t with
  | zero => exact h
  | succ n ih => exact hd n _ _ ih

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- A solution's slice at time `t` is `∼_D`-equivalent to the composite applied to its initial
slice: the class at time `t` is a function of the initial class. -/
theorem solution_eq_composite {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    (hd : ∀ t (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    {𝔾 : ℕ → V → Matrix V V ℂ} (hlaw : ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) (t : ℕ) :
    GramPhaseEquiv (𝔾 t) (Nat.rec (motive := fun _ => V → Matrix V V ℂ) (𝔾 0) (fun s H => Φ s H) t) := by
  induction t with
  | zero => exact gramPhaseEquiv_refl _
  | succ n ih => exact gramPhaseEquiv_trans (hlaw n) (hd n _ _ ih)

/-- **`OL1` (a), the general form.** A transition family satisfying `L4d` descends to a composition
of maps on the admissible orbit spaces: (1) every solution's class at time `t` is the composite
`E_t` of its initial class; (2) two solutions handed `∼_D`-equivalent initial slices have
`≈_O`-equivalent trajectories — the evolution from the initial orbit is a function of the initial
class alone; and (3) the ambient set of pointwise realizable trajectories is exactly the set of Gram
trajectories of coherent lifts, act 17's `TJ1`, cited here at the step where the solution set is
read as a composition over per-time state spaces. -/
theorem ol1a_descent (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    (hd : ∀ t (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')) :
    (∀ 𝔾 : ℕ → V → Matrix V V ℂ, (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) → ∀ t,
        GramPhaseEquiv (𝔾 t)
          (Nat.rec (motive := fun _ => V → Matrix V V ℂ) (𝔾 0) (fun s H => Φ s H) t))
      ∧ (∀ 𝔾 𝔾' : ℕ → V → Matrix V V ℂ, (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
          (∀ t, GramPhaseEquiv (𝔾' (t + 1)) (Φ t (𝔾' t))) →
          GramPhaseEquiv (𝔾 0) (𝔾' 0) → GramTrajEquiv 𝔾 𝔾')
      ∧ (∀ 𝔾 : ℕ → V → Matrix V V ℂ,
          (∃ U : ℕ → Matrix (V × A) (V × A) ℂ, CoherentLift a₀ Γ U ∧ ∀ t, FibreGram a₀ (U t) = 𝔾 t)
            ↔ ∀ t, RealizableGram A (Γ t) (𝔾 t)) := by
  refine ⟨fun 𝔾 hlaw t => solution_eq_composite hd hlaw t, fun 𝔾 𝔾' h h' h0 t => ?_,
    fun 𝔾 => tj1_trajectory_set a₀ 𝔾⟩
  exact gramPhaseEquiv_trans (solution_eq_composite hd h t)
    (gramPhaseEquiv_trans (composite_descends hd h0 t)
      (gramPhaseEquiv_symm (solution_eq_composite hd h' t)))

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Descent transports along iterates of one map. -/
theorem iterate_descends {Φ₀ : (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    (hd : ∀ G G' : V → Matrix V V ℂ, GramPhaseEquiv G G' → GramPhaseEquiv (Φ₀ G) (Φ₀ G'))
    {G G' : V → Matrix V V ℂ} (h : GramPhaseEquiv G G') (t : ℕ) :
    GramPhaseEquiv (Φ₀^[t] G) (Φ₀^[t] G') := by
  induction t with
  | zero => exact h
  | succ n ih => rw [Function.iterate_succ_apply', Function.iterate_succ_apply']; exact hd _ _ ih

omit [DecidableEq A] in
/-- **`OL1` (b), the homogeneous form.** At a time-homogeneous visible family and under `L2`, the
family of induced maps is constant, `Φ̄_t = Φ̄`, every solution's class at time `t` is `Φ̄^t` of its
initial class, and the iterates compose as a **monoid action of `(ℕ, +)`** on the admissible orbit
space: `E_0 = id`, `E_{t+s} = E_s ∘ E_t`, each `E_t` descending to classes, and every slice of every
solution admissible for the one visible slice `Γ 0`. Stated at time-homogeneous configurations
only: at a general `Γ` there is no single set for a monoid to act on. -/
theorem ol1b_monoid_action (Γ : ℕ → Matrix V V ℝ) (hΓ : ∀ t, Γ t = Γ 0)
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    (hd : ∀ t (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    {Φ₀ : (V → Matrix V V ℂ) → (V → Matrix V V ℂ)} (h2 : ∀ t, Φ t = Φ₀) :
    (∀ 𝔾 : ℕ → V → Matrix V V ℂ, (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) →
        ∀ t, GramPhaseEquiv (𝔾 t) (Φ₀^[t] (𝔾 0)))
      ∧ (∀ G : V → Matrix V V ℂ, Φ₀^[0] G = G)
      ∧ (∀ (t s : ℕ) (G : V → Matrix V V ℂ), Φ₀^[t + s] G = Φ₀^[s] (Φ₀^[t] G))
      ∧ (∀ (t : ℕ) (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' →
          GramPhaseEquiv (Φ₀^[t] G) (Φ₀^[t] G'))
      ∧ (∀ 𝔾 : ℕ → V → Matrix V V ℂ, (∀ t, RealizableGram A (Γ t) (𝔾 t)) →
          ∀ t, RealizableGram A (Γ 0) (𝔾 t)) := by
  have hd0 : ∀ G G' : V → Matrix V V ℂ, GramPhaseEquiv G G' → GramPhaseEquiv (Φ₀ G) (Φ₀ G') := by
    intro G G' h
    have := hd 0 G G' h
    rwa [h2 0] at this
  refine ⟨fun 𝔾 hlaw t => ?_, fun G => rfl, fun t s G => ?_, fun t G G' h => iterate_descends hd0 h t,
    fun 𝔾 hG t => by rw [← hΓ t]; exact hG t⟩
  · induction t with
    | zero => exact gramPhaseEquiv_refl _
    | succ n ih =>
      rw [Function.iterate_succ_apply']
      have h1 := hlaw n
      rw [h2 n] at h1
      exact gramPhaseEquiv_trans h1 (hd0 _ _ ih)
  · rw [add_comm, Function.iterate_add_apply]


/-! ### Section C — the frozen single-carrier configuration and its merged witness supply

Act 12's Hadamard objects at `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ ≡ ¼`, the frozen family
`H(z) = ½ · [[1,1,1,1],[1,z,−1,−z],[1,−1,1,−1],[1,−z,−1,z]]` at `z = 1, i, −1`, and the carrier
relabelling `σ = (2 3)` of act 19's `ΦP` entry. Every matrix is a bound variable pinned by an
equation, and every separation is certified through act 12's merged `∼_D`-invariant
`G^{(i₀)}_{i₁ i₀} · G^{(i₁)}_{i₀ i₁}` (`gramPhaseEquiv_cross_invariant`) read at a named fibre pair. -/

/-- **Realizability is a `∼_D`-class property.** If `G` is realizable and `G ≈ G'` then `G'` is
realizable: realize `G` by an admissible dilation (act 12's `sh1_sufficiency`), multiply on the
right by the weak anchored gauge carrying the phases (act 11's class, act 11's
`weak_preserves_admissible`), read the result's Gram data through act 12's
`fibreGram_mul_weak_apply`, and apply `sh1_necessity`. -/
theorem realizable_of_gramPhaseEquiv {Γ : Matrix V V ℝ} (a₀ : A) {G G' : V → Matrix V V ℂ}
    (hG : RealizableGram A Γ G) (h : GramPhaseEquiv G G') : RealizableGram A Γ G' := by
  classical
  obtain ⟨U, hU, hGU⟩ := sh1_sufficiency a₀ hG
  obtain ⟨c, hc, hGG'⟩ := h
  have hcc : ∀ j, c j * star (c j) = 1 := fun j => by
    rw [mul_comm, star_mul_self_eq_norm_sq, hc, one_pow, Complex.ofReal_one]
  have hKc : ∀ (p : V × A) (j : V),
      (Matrix.diagonal (fun p : V × A => c p.1) : Matrix (V × A) (V × A) ℂ) p (j, a₀)
        = if p = (j, a₀) then c j else 0 := by
    intro p j
    rw [Matrix.diagonal_apply]
    by_cases hp : p = (j, a₀)
    · subst hp; simp
    · simp [hp]
  have hKunit : (Matrix.diagonal (fun p : V × A => c p.1) : Matrix (V × A) (V × A) ℂ)
      ∈ Matrix.unitaryGroup (V × A) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.diagonal_conjTranspose,
      Matrix.diagonal_mul_diagonal]
    ext p q
    rw [Matrix.diagonal_apply, Matrix.one_apply]
    split_ifs with hpq <;> first | rfl | (subst hpq; simp only [Pi.star_apply]; exact hcc p.1)
  have hadm := weak_preserves_admissible hU ⟨hKunit, c, hKc⟩
  have hFG : FibreGram a₀ (U * Matrix.diagonal (fun p : V × A => c p.1)) = G' := by
    funext i
    ext j k
    rw [fibreGram_mul_weak_apply hKc, hGU, hGG']
  rw [← hFG]
  exact sh1_necessity hadm

/-- **The carrier relabelling preserves realizability**, at a visible slice invariant under it:
realize `G` (act 12's `sh1_sufficiency`), lift by act 20's `RelabelLift` (admissible by act 20's
`rnt2_admissible`), read its Gram data through act 20's `rnt2_lifting_property`. -/
theorem realizable_relabel {Γ : Matrix V V ℝ} (a₀ : A) (σ : Equiv.Perm V)
    (hΓ : ∀ i j, Γ (σ i) (σ j) = Γ i j) {G : V → Matrix V V ℂ} (hG : RealizableGram A Γ G) :
    RealizableGram A Γ (RelabelTransition σ G) := by
  obtain ⟨U, hU, hGU⟩ := sh1_sufficiency a₀ hG
  have h := sh1_necessity (rnt2_admissible hΓ hU)
  rwa [rnt2_lifting_property, hGU] at h

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Relabelling descends: `G ≈ G'` gives `Φ_σ G ≈ Φ_σ G'`, with the phases reindexed by `σ`. -/
theorem relabel_gramPhaseEquiv (σ : Equiv.Perm V) {G G' : V → Matrix V V ℂ}
    (h : GramPhaseEquiv G G') : GramPhaseEquiv (RelabelTransition σ G) (RelabelTransition σ G') := by
  obtain ⟨c, hc, hG⟩ := h
  exact ⟨fun j => c (σ j), fun j => hc (σ j), fun i j k => by
    simp only [RelabelTransition, Matrix.submatrix_apply]; exact hG (σ i) (σ j) (σ k)⟩

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Relabelling is invertible on tuples: `Φ_{σ⁻¹} (Φ_σ G) = G`. -/
theorem relabel_relabel_symm (σ : Equiv.Perm V) (G : V → Matrix V V ℂ) :
    RelabelTransition σ.symm (RelabelTransition σ G) = G := by
  funext i
  ext j k
  simp [RelabelTransition, Matrix.submatrix_apply]

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
theorem relabel_symm_relabel (σ : Equiv.Perm V) (G : V → Matrix V V ℂ) :
    RelabelTransition σ (RelabelTransition σ.symm G) = G := by
  funext i
  ext j k
  simp [RelabelTransition, Matrix.submatrix_apply]

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- Relabelling reflects `∼_D`: `Φ_σ G ≈ Φ_σ G'` gives `G ≈ G'` (`L3i` for the relabelling). -/
theorem gramPhaseEquiv_of_relabel (σ : Equiv.Perm V) {G G' : V → Matrix V V ℂ}
    (h : GramPhaseEquiv (RelabelTransition σ G) (RelabelTransition σ G')) : GramPhaseEquiv G G' := by
  have := relabel_gramPhaseEquiv σ.symm h
  rwa [relabel_relabel_symm, relabel_relabel_symm] at this

/-- **The frozen witness supply, pinned.** `Γ₀ ≡ ¼`; `H₁ = H(1)`, `Hᵢ = H(i)`, `Hm = H(−1)`, all
three admissible for `Γ₀` at the anchor; `σ = (2 3)`; and the separations and fixings this round's
verdicts consume, each certified through act 12's merged cross-invariant at a named fibre pair:
`[G(H₁)] ≠ [G(Hᵢ)]` (act 12's `TG3`, consumed), `[G(Hm)] ≠ [G(H₁)]` and `[G(Hm)] ≠ [G(Hᵢ)]` at
`(0,1)`, `Φ_σ G(H₁) = G(H₁)` exactly, `[G(Hᵢ)] ≠ [Φ_σ G(Hᵢ)]` at `(0,2)`, and `[G(H₁)] ≠ [Φ_σ G(Hᵢ)]`
at `(0,1)`. -/
theorem witness_supply :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ Hm : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ Hm = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)
        ∧ AdmissibleDilationAt Γ₀ (0 : Fin 1) H₁ ∧ AdmissibleDilationAt Γ₀ (0 : Fin 1) Hᵢ
        ∧ AdmissibleDilationAt Γ₀ (0 : Fin 1) Hm
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) Hᵢ)
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) Hm) (FibreGram (0 : Fin 1) H₁)
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) Hm) (FibreGram (0 : Fin 1) Hᵢ)
        ∧ RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) H₁)
            = FibreGram (0 : Fin 1) H₁
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) Hᵢ)
            (RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ))
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) H₁)
            (RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ)) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hunitM : (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1))
      ∈ Matrix.unitaryGroup (Fin 4 × Fin 1) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_four,
        Matrix.conjTranspose_apply] <;> norm_num [Complex.ext_iff]
  have hadmM : AdmissibleDilationAt Γ₀ (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)) := by
    refine ⟨hunitM, fun i j => ?_⟩
    rw [hΓ₀]
    fin_cases i <;> fin_cases j <;> simp <;> norm_num
  refine ⟨Γ₀, H₁, Hᵢ, _, hΓ₀, hH₁, hHᵢ, rfl, hadm₁, hadmᵢ, hadmM, hnotG, ?_, ?_, ?_, ?_, ?_⟩
  · intro h
    have := gramPhaseEquiv_cross_invariant h 0 1
    rw [hH₁] at this
    simp [fibreGram_apply] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    have := gramPhaseEquiv_cross_invariant h 0 1
    rw [hHᵢ] at this
    simp [fibreGram_apply] at this
    norm_num [Complex.ext_iff] at this
  · rw [hH₁]
    funext i
    ext j k
    simp only [RelabelTransition, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one]
    fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Equiv.swap_apply_def]
  · intro h
    have := gramPhaseEquiv_cross_invariant h 0 2
    rw [hHᵢ] at this
    simp [RelabelTransition, Matrix.submatrix_apply, fibreGram_apply, Equiv.swap_apply_def] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    have := gramPhaseEquiv_cross_invariant h 0 1
    rw [hH₁, hHᵢ] at this
    simp [RelabelTransition, Matrix.submatrix_apply, fibreGram_apply, Equiv.swap_apply_def] at this
    norm_num [Complex.ext_iff] at this


/-! ### Section D — the census at the frozen single-carrier configuration: `ΦI`, `ΦP`, and `SIOP`

At the single-carrier configuration the ladder's `L5` conjunct is read at the **trivial
decomposition** `V ≃ V × Fin 1` with the second visible family identically `1`, where it carries no
content (`factorizes_trivial`, proved for every transition family): `L5` is a condition at product
configurations and the single-carrier census is not where it bites. The census verdicts below are
each about the exact family frozen under its label at the exact frozen configuration. -/

omit [DecidableEq A] in
/-- **`L5` has no content at the trivial decomposition.** For any transition family `Φ`, any
visible family `Γ`, and `|A| = 1`, `FactorizesOnProduct` holds with `V ≃ V × Fin 1`, `Γ₂ ≡ 1`,
`Φ₁ = Φ` and `Φ₂` the constant `1`-tuple, because the product embedding with a realizable
`1 × 1` second factor is the identity on tuples. -/
theorem factorizes_trivial (hA : Fintype.card A = 1) (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) :
    FactorizesOnProduct A (Fin 1) (Fin 1) (Equiv.prodUnique V (Fin 1)).symm Γ
      (fun _ => Matrix.of fun _ _ => (1 : ℝ)) Γ Φ := by
  refine ⟨by simp [hA], fun t i j => by simp, Φ, fun _ _ => fun _ => (1 : Matrix (Fin 1) (Fin 1) ℂ),
    fun t G₁ G₂ _ hG₂ => ?_⟩
  have h1 : G₂ 0 0 0 = 1 := by
    have := hG₂.2.2.2 0 0
    simpa using this
  have hL : (fun i => Matrix.of fun j k =>
      G₁ ((Equiv.prodUnique V (Fin 1)).symm i).1 ((Equiv.prodUnique V (Fin 1)).symm j).1
          ((Equiv.prodUnique V (Fin 1)).symm k).1
        * G₂ ((Equiv.prodUnique V (Fin 1)).symm i).2 ((Equiv.prodUnique V (Fin 1)).symm j).2
          ((Equiv.prodUnique V (Fin 1)).symm k).2) = G₁ := by
    funext i
    ext j k
    simp [Fin.default_eq_zero, h1]
  have hR : (fun i => Matrix.of fun j k =>
      Φ t G₁ ((Equiv.prodUnique V (Fin 1)).symm i).1 ((Equiv.prodUnique V (Fin 1)).symm j).1
          ((Equiv.prodUnique V (Fin 1)).symm k).1
        * (1 : Matrix (Fin 1) (Fin 1) ℂ) ((Equiv.prodUnique V (Fin 1)).symm j).2
          ((Equiv.prodUnique V (Fin 1)).symm k).2) = Φ t G₁ := by
    funext i
    ext j k
    have hone : (1 : Matrix (Fin 1) (Fin 1) ℂ) ((Equiv.prodUnique V (Fin 1)).symm j).2
        ((Equiv.prodUnique V (Fin 1)).symm k).2 = 1 := by
      rw [Matrix.one_apply, if_pos (Subsingleton.elim _ _)]
    simp only [Matrix.of_apply, hone, mul_one]
    rfl
  rw [hL, hR]
  exact gramPhaseEquiv_refl _

/-- **`ΦI` satisfies the frozen ladder at the frozen configuration** — act 18's `LC3`, the baseline
survivor. Its `L-PROP` conjuncts are act 18's merged `lc3_generator_law`, consumed through the
symmetry of act 12's `GramPhaseEquiv` (act 18 writes the step as `𝔾 t ∼ 𝔾 (t+1)`, this round as
`𝔾 (t+1) ∼ Φ t (𝔾 t)`); `L4n` is witnessed by the identity lift with identity induced maps, act
20's `RNT1` (a) shape; `L5` by `factorizes_trivial`. -/
theorem phiI_ladder :
    ∃ Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ, (∀ t i j, Γ t i j = 1 / 4)
      ∧ LadderConds (Fin 1) (Fin 1) (0 : Fin 1) Γ (Equiv.prodUnique (Fin 4) (Fin 1)).symm Γ
          (fun _ => Matrix.of fun _ _ => (1 : ℝ)) (fun _ G => G) := by
  classical
  obtain ⟨Γ, Φ', Law', hΓ, hΦ', hLaw', _, _, hproper, hprop, _⟩ := lc3_generator_law
  have hlaw : Law' = fun 𝔾 : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ =>
      ∀ t, GramPhaseEquiv (𝔾 (t + 1)) ((fun _ G => G : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)
        → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) t (𝔾 t)) := by
    subst hΦ'
    subst hLaw'
    funext 𝔾
    exact propext ⟨fun h t => gramPhaseEquiv_symm (h t), fun h t => gramPhaseEquiv_symm (h t)⟩
  rw [hlaw] at hproper hprop
  have hΓc : ∀ t, Γ t = Γ 0 := fun t => by ext i j; rw [hΓ, hΓ]
  refine ⟨Γ, hΓ, hproper, hprop, fun G₀ hG₀ => ⟨fun _ => G₀, fun t => by rw [hΓc t]; exact hG₀,
    fun _ => gramPhaseEquiv_refl _, gramPhaseEquiv_refl _⟩, fun t G hG => by rw [hΓc (t + 1), ← hΓc t]; exact hG,
    ⟨fun G => G, fun _ => rfl⟩, ⟨fun _ _ _ _ _ h => h, fun t G' hG' => ⟨G', by rw [hΓc t, ← hΓc (t + 1)]; exact hG', gramPhaseEquiv_refl _⟩⟩,
    fun _ _ _ h => h, fun t => ⟨id, id, id, fun _ _ => rfl, fun U hU => by rw [hΓc (t + 1), ← hΓc t]; exact hU,
      rnt1_strict_imp_twisted ⟨fun _ _ _ => rfl, fun _ _ _ => rfl⟩⟩,
    factorizes_trivial (by simp) Γ _⟩

/-- **`ΦP` satisfies the frozen ladder at the frozen configuration** — the carrier relabelling by
`σ = (2 3)`, under which `Γ ≡ ¼` is invariant. Totality, admissibility preservation and
surjectivity come from `realizable_relabel`, injectivity from `gramPhaseEquiv_of_relabel`, descent
from `relabel_gramPhaseEquiv`, the `L-PROP` conjuncts from the witness supply (`[G(H₁)]` fixed by
`σ`, `[G(Hᵢ)]` moved, the two inequivalent), and **`L4n` from act 20's merged lift and exact law**:
`RelabelLift σ` with `rnt2_lifting_property`, `rnt2_admissible` and `rnt3_law_exact`, consumed at
merged strength. `L5` by `factorizes_trivial`. -/
theorem phiP_ladder :
    ∃ Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ, (∀ t i j, Γ t i j = 1 / 4)
      ∧ LadderConds (Fin 1) (Fin 1) (0 : Fin 1) Γ (Equiv.prodUnique (Fin 4) (Fin 1)).symm Γ
          (fun _ => Matrix.of fun _ _ => (1 : ℝ))
          (fun _ G => RelabelTransition (Equiv.swap (2 : Fin 4) 3) G) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  set σ : Equiv.Perm (Fin 4) := Equiv.swap (2 : Fin 4) 3 with hσ
  have hΓinv : ∀ i j, Γ₀ (σ i) (σ j) = Γ₀ i j := fun i j => by rw [hΓ₀]; simp
  have hΓinv' : ∀ i j, Γ₀ (σ.symm i) (σ.symm j) = Γ₀ i j := fun i j => by rw [hΓ₀]; simp
  have hrel : ∀ {G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}, RealizableGram (Fin 1) Γ₀ G →
      RealizableGram (Fin 1) Γ₀ (RelabelTransition σ G) :=
    fun hG => realizable_relabel (0 : Fin 1) σ hΓinv hG
  have hd : ∀ (t : ℕ) (G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv G G' →
      GramPhaseEquiv (RelabelTransition σ G) (RelabelTransition σ G') :=
    fun _ _ _ h => relabel_gramPhaseEquiv σ h
  have hG₁ := sh1_necessity hadm₁
  have hGᵢ := sh1_necessity hadmᵢ
  -- the iterated trajectory from a realizable initial tuple
  have hiter : ∀ (G₀ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₀ →
      ∀ t, RealizableGram (Fin 1) Γ₀ ((RelabelTransition σ)^[t] G₀) := by
    intro G₀ hG₀ t
    induction t with
    | zero => exact hG₀
    | succ n ih => rw [Function.iterate_succ_apply']; exact hrel ih
  have hlawiter : ∀ (G₀ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) t,
      GramPhaseEquiv ((RelabelTransition σ)^[t + 1] G₀)
        (RelabelTransition σ ((RelabelTransition σ)^[t] G₀)) := by
    intro G₀ t
    rw [Function.iterate_succ_apply']
    exact gramPhaseEquiv_refl _
  refine ⟨fun _ => Γ₀, fun t i j => by rw [hΓ₀]; rfl, ?_, ?_, ?_, ?_, ⟨_, fun _ => rfl⟩, ?_, hd, ?_,
    factorizes_trivial (by simp) _ _⟩
  · -- ProperAt
    refine ⟨fun _ => FibreGram 0 H₁, fun t => (RelabelTransition σ)^[t] (FibreGram 0 Hᵢ),
      fun t => if t = 0 then FibreGram 0 H₁ else FibreGram 0 Hᵢ, fun _ => hG₁, hiter _ hGᵢ,
      fun t => by dsimp only; split_ifs <;> assumption,
      fun _ => by dsimp only; rw [hfix]; exact gramPhaseEquiv_refl _,
      hlawiter _, fun h => h1i (h 0), fun h => ?_⟩
    have := h 0
    simp only [zero_add, one_ne_zero, if_false, if_true, hfix] at this
    exact h1i (gramPhaseEquiv_symm this)
  · -- PropagatesFrom
    refine ⟨fun G₁ G₂ _ _ h₁ h₂ h0 => (ol1a_descent (0 : Fin 1) (fun _ => Γ₀) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => FibreGram 0 H₁, fun t => (RelabelTransition σ)^[t] (FibreGram 0 Hᵢ), le_rfl,
      fun _ => hG₁, hiter _ hGᵢ, fun _ => by dsimp only; rw [hfix]; exact gramPhaseEquiv_refl _,
      hlawiter _, ?_⟩
    simpa using h1move
  · -- L0
    exact fun G₀ hG₀ => ⟨fun t => (RelabelTransition σ)^[t] G₀, hiter G₀ hG₀, hlawiter G₀,
      gramPhaseEquiv_refl _⟩
  · -- L1
    exact fun _ _ hG => hrel hG
  · -- L3i and L3s
    refine ⟨fun _ _ _ _ _ h => gramPhaseEquiv_of_relabel σ h, fun _ G' hG' =>
      ⟨RelabelTransition σ.symm G', realizable_relabel (0 : Fin 1) σ.symm hΓinv' hG', ?_⟩⟩
    dsimp only
    rw [relabel_symm_relabel]
    exact gramPhaseEquiv_refl _
  · -- L4n, from act 20's merged lift and exact law
    intro t
    exact ⟨RelabelLift σ, RelabelInducedLeft σ, RelabelInducedRight σ,
      fun U _ => rnt2_lifting_property σ 0 U, fun U hU => rnt2_admissible hΓinv hU,
      rnt3_law_exact σ 0⟩

/-- **`SIOP-YES` at `t* = 1`, from the initial class of `H(i)`.** `ΦI` against `ΦP`, both satisfying
the frozen ladder, their laws not `≈_L` (the constant trajectory at `[G(Hᵢ)]` solves `ΦI`'s law and
not `ΦP`'s), handed the **same** initial slice `G(Hᵢ)`, agreeing at time `0` and diverging at time
`1`: `[G(Hᵢ)] ≠ [Φ_σ G(Hᵢ)]`, certified through act 12's merged cross-invariant at the fibre pair
`(0, 2)`. The initial orbit is a member of the frozen witness supply, instantiating the existential
under the freeze's witness rule; the earlier-agreement conjunct is agreement at time `0`, the
hypothesis itself. -/
theorem siop_yes : SameInitialOrbitPair (Fin 4) (Fin 1) (Fin 4) (Fin 1) (Fin 1) (Fin 1) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨ΓI, hΓI, hI⟩ := phiI_ladder
  obtain ⟨ΓP, hΓP, hP⟩ := phiP_ladder
  have hIΓ : ΓI = fun _ => Γ₀ := by funext t; ext i j; rw [hΓI, hΓ₀]; simp
  have hPΓ : ΓP = fun _ => Γ₀ := by funext t; ext i j; rw [hΓP, hΓ₀]; simp
  rw [hIΓ] at hI
  rw [hPΓ] at hP
  set σ : Equiv.Perm (Fin 4) := Equiv.swap (2 : Fin 4) 3 with hσ
  have hΓinv : ∀ i j, Γ₀ (σ i) (σ j) = Γ₀ i j := fun i j => by rw [hΓ₀]; simp
  have hGᵢ := sh1_necessity hadmᵢ
  have hiter : ∀ t, RealizableGram (Fin 1) Γ₀ ((RelabelTransition σ)^[t] (FibreGram 0 Hᵢ)) := by
    intro t
    induction t with
    | zero => exact hGᵢ
    | succ n ih => rw [Function.iterate_succ_apply']; exact realizable_relabel (0 : Fin 1) σ hΓinv ih
  refine ⟨fun _ => Γ₀, 0, (Equiv.prodUnique (Fin 4) (Fin 1)).symm, fun _ => Γ₀,
    fun _ => Matrix.of fun _ _ => (1 : ℝ), fun _ G => G, fun _ G => RelabelTransition σ G,
    fun _ => FibreGram 0 Hᵢ, fun t => (RelabelTransition σ)^[t] (FibreGram 0 Hᵢ), 1, hI, hP, ?_,
    fun _ => hGᵢ, hiter, fun _ => gramPhaseEquiv_refl _,
    fun t => by dsimp only; rw [Function.iterate_succ_apply']; exact gramPhaseEquiv_refl _, le_rfl, ?_, ?_⟩
  · intro hLE
    have := (hLE (fun _ => FibreGram 0 Hᵢ) (fun _ => hGᵢ)).1 (fun _ => gramPhaseEquiv_refl _) 0
    exact hmove this
  · intro s hs
    have : s = 0 := by omega
    subst this
    exact gramPhaseEquiv_refl _
  · simpa using hmove


/-! ### Section E — the countercontrols `ΦX`, `ΦC`, `ΦT`, and the `L1` implication on the shared class -/

/-- **`ΦX` — the `L0` countercontrol.** The law datum `(∀ t, 𝔾 (t+1) ∼ 𝔾 t) ∧ ([𝔾 0] = [G(H₁)] ∨
[𝔾 0] = [G(Hᵢ)])` — act 18's `LC0` two-class condition conjoined with a genuinely cross-time
constancy — is an `L-PROP` law in act 18's frozen sense (proper at the configuration; propagates
with both clauses), **and totality fails**: the class of `H(−1)`, pointwise realizable, admits no
solution at all, because it is `∼_D`-inequivalent to both named classes. Stated at law level, as
act 19 froze it, with totality written inline. -/
theorem phiX_l0_restricts :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (Law : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ ProperAt (0 : Fin 1) Γ Law ∧ PropagatesFrom (0 : Fin 1) Γ Law
        ∧ ¬ (∀ G₀ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) (Γ 0) G₀ →
            ∃ 𝔾 : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, (∀ t, RealizableGram (Fin 1) (Γ t) (𝔾 t))
              ∧ Law 𝔾 ∧ GramPhaseEquiv (𝔾 0) G₀) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  have hG₁ := sh1_necessity hadm₁
  have hGᵢ := sh1_necessity hadmᵢ
  have hGm := sh1_necessity hadmM
  -- solutions have constant class
  have hconst : ∀ 𝔾 : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t)) → ∀ t, GramPhaseEquiv (𝔾 t) (𝔾 0) := by
    intro 𝔾 h t
    induction t with
    | zero => exact gramPhaseEquiv_refl _
    | succ n ih => exact gramPhaseEquiv_trans (h n) ih
  refine ⟨fun _ => Γ₀, fun 𝔾 => (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t))
      ∧ (GramPhaseEquiv (𝔾 0) (FibreGram 0 H₁) ∨ GramPhaseEquiv (𝔾 0) (FibreGram 0 Hᵢ)),
    fun t i j => by rw [hΓ₀]; rfl, ?_, ?_, ?_⟩
  · -- proper: two inequivalent constant solutions, and the constant at [G(H(−1))] is no solution
    refine ⟨fun _ => FibreGram 0 H₁, fun _ => FibreGram 0 Hᵢ, fun _ => FibreGram 0 Hm,
      fun _ => hG₁, fun _ => hGᵢ, fun _ => hGm,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inl (gramPhaseEquiv_refl _)⟩,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inr (gramPhaseEquiv_refl _)⟩,
      fun h => h1i (h 0), fun h => ?_⟩
    rcases h.2 with h' | h'
    · exact hm1 h'
    · exact hmi h'
  · -- propagates: clause (i) from constancy of class, clause (ii) at t = 1
    refine ⟨fun G₁ G₂ _ _ h₁ h₂ h0 t => ?_, 1, fun _ => FibreGram 0 H₁, fun _ => FibreGram 0 Hᵢ,
      le_rfl, fun _ => hG₁, fun _ => hGᵢ,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inl (gramPhaseEquiv_refl _)⟩,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inr (gramPhaseEquiv_refl _)⟩, h1i⟩
    exact gramPhaseEquiv_trans (hconst G₁ h₁.1 t)
      (gramPhaseEquiv_trans h0 (gramPhaseEquiv_symm (hconst G₂ h₂.1 t)))
  · -- totality fails at the class of H(−1)
    intro htot
    obtain ⟨𝔾, _, ⟨_, hinit⟩, h0⟩ := htot (FibreGram 0 Hm) hGm
    rcases hinit with h' | h'
    · exact hm1 (gramPhaseEquiv_trans (gramPhaseEquiv_symm h0) h')
    · exact hmi (gramPhaseEquiv_trans (gramPhaseEquiv_symm h0) h')

/-- **`ΦC` — the named `L3` countercontrol, and what the kernel says about it.** The constant
transition `Φ t G = G(H₁)` is total, admissibility-preserving, time-homogeneous, descending and
twisted-natural with the constant lift `Ψ U = H₁` and identity induced maps (the freeze's analysis
under `L4n`, here a theorem); it **fails `L3i`** (two inequivalent classes share the image) and
**fails `L3s`** (the class of `Hᵢ` is admissible and outside the image); it is proper at the
configuration and satisfies act 18's propagation clause (i); **and it fails act 18's propagation
clause (ii)**: every solution sits at `[G(H₁)]` from time `1` on, so no two solutions are
inequivalent at any `t ≥ 1` and the initial orbit contributes nothing. So `ΦC` is **not an `L-PROP`
law in act 18's frozen sense**, and is therefore not on the ladder at all. -/
theorem phiC_census :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ) (H₁ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ EvolvesTotally (Fin 1) Γ (fun _ _ => FibreGram (0 : Fin 1) H₁)
        ∧ PreservesAdmissible (Fin 1) Γ (fun _ _ => FibreGram (0 : Fin 1) H₁)
        ∧ (∀ t (G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv G G' →
            GramPhaseEquiv ((fun _ _ => FibreGram (0 : Fin 1) H₁ :
              ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) t G)
              ((fun _ _ => FibreGram (0 : Fin 1) H₁ :
              ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) t G'))
        ∧ (∀ t : ℕ, ∃ Ψ αL αR : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ
              → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
            (∀ U, AdmissibleDilationAt (Γ t) (0 : Fin 1) U →
              FibreGram (0 : Fin 1) (Ψ U) = FibreGram (0 : Fin 1) H₁)
            ∧ (∀ U, AdmissibleDilationAt (Γ t) (0 : Fin 1) U →
              AdmissibleDilationAt (Γ (t + 1)) (0 : Fin 1) (Ψ U))
            ∧ TwistedNatural (0 : Fin 1) αL αR Ψ)
        ∧ ¬ Reversible (Fin 1) Γ (fun _ _ => FibreGram (0 : Fin 1) H₁)
        ∧ ¬ (∀ t (G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) (Γ t) G →
            RealizableGram (Fin 1) (Γ t) G' →
            GramPhaseEquiv (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) H₁) →
            GramPhaseEquiv G G')
        ∧ ¬ (∀ t (G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) (Γ (t + 1)) G' →
            ∃ G, RealizableGram (Fin 1) (Γ t) G ∧ GramPhaseEquiv (FibreGram (0 : Fin 1) H₁) G')
        ∧ ProperAt (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (FibreGram (0 : Fin 1) H₁))
        ∧ (∀ G₁ G₂ : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
            (∀ t, RealizableGram (Fin 1) (Γ t) (G₁ t)) → (∀ t, RealizableGram (Fin 1) (Γ t) (G₂ t)) →
            (∀ t, GramPhaseEquiv (G₁ (t + 1)) (FibreGram (0 : Fin 1) H₁)) →
            (∀ t, GramPhaseEquiv (G₂ (t + 1)) (FibreGram (0 : Fin 1) H₁)) →
            GramPhaseEquiv (G₁ 0) (G₂ 0) → GramTrajEquiv G₁ G₂)
        ∧ ¬ (∃ (t : ℕ) (G₁ G₂ : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), 1 ≤ t
            ∧ (∀ s, RealizableGram (Fin 1) (Γ s) (G₁ s)) ∧ (∀ s, RealizableGram (Fin 1) (Γ s) (G₂ s))
            ∧ (∀ s, GramPhaseEquiv (G₁ (s + 1)) (FibreGram (0 : Fin 1) H₁))
            ∧ (∀ s, GramPhaseEquiv (G₂ (s + 1)) (FibreGram (0 : Fin 1) H₁))
            ∧ ¬ GramPhaseEquiv (G₁ t) (G₂ t))
        ∧ ¬ PropagatesFrom (0 : Fin 1) Γ
            (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (FibreGram (0 : Fin 1) H₁)) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  have hG₁ := sh1_necessity hadm₁
  have hGᵢ := sh1_necessity hadmᵢ
  have hone : WeakAnchorStabilizer (0 : Fin 1) (1 : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) :=
    ⟨one_mem _, fun _ => 1, fun p j => by rw [Matrix.one_apply]⟩
  -- clause (ii) fails: from time 1 on every solution sits at [G(H₁)]
  have hii : ¬ (∃ (t : ℕ) (G₁ G₂ : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), 1 ≤ t
      ∧ (∀ s, RealizableGram (Fin 1) Γ₀ (G₁ s)) ∧ (∀ s, RealizableGram (Fin 1) Γ₀ (G₂ s))
      ∧ (∀ s, GramPhaseEquiv (G₁ (s + 1)) (FibreGram (0 : Fin 1) H₁))
      ∧ (∀ s, GramPhaseEquiv (G₂ (s + 1)) (FibreGram (0 : Fin 1) H₁))
      ∧ ¬ GramPhaseEquiv (G₁ t) (G₂ t)) := by
    rintro ⟨t, G₁, G₂, ht, _, _, h₁, h₂, hne⟩
    obtain ⟨s, rfl⟩ : ∃ s, t = s + 1 := ⟨t - 1, by omega⟩
    exact hne (gramPhaseEquiv_trans (h₁ s) (gramPhaseEquiv_symm (h₂ s)))
  refine ⟨fun _ => Γ₀, H₁, fun t i j => by rw [hΓ₀]; rfl, hH₁, ?_, fun _ _ _ => hG₁,
    fun _ _ _ _ => gramPhaseEquiv_refl _, fun t => ⟨fun _ => H₁, fun _ => 1, fun _ => 1,
      fun _ _ => rfl, fun _ _ => hadm₁, fun _ _ => one_leftFibreGroup, fun _ _ => hone,
      fun _ _ _ => (one_mul _).symm, fun _ _ _ => (mul_one _).symm⟩, ?_, ?_, ?_, ?_, ?_, hii, ?_⟩
  · -- total
    intro G₀ hG₀
    exact ⟨fun t => if t = 0 then G₀ else FibreGram 0 H₁,
      fun t => by dsimp only; split_ifs <;> assumption,
      fun t => by simp only [Nat.succ_ne_zero, if_false]; exact gramPhaseEquiv_refl _,
      by simp only [if_true]; exact gramPhaseEquiv_refl _⟩
  · -- not reversible
    rintro ⟨hinj, _⟩
    exact h1i (hinj 0 _ _ hG₁ hGᵢ (gramPhaseEquiv_refl _))
  · -- L3i fails
    intro hinj
    exact h1i (hinj 0 _ _ hG₁ hGᵢ (gramPhaseEquiv_refl _))
  · -- L3s fails
    intro hsurj
    obtain ⟨_, _, h⟩ := hsurj 0 (FibreGram 0 Hᵢ) hGᵢ
    exact h1i h
  · -- proper
    refine ⟨fun _ => FibreGram 0 H₁, fun t => if t = 0 then FibreGram 0 Hᵢ else FibreGram 0 H₁,
      fun _ => FibreGram 0 Hᵢ, fun _ => hG₁, fun t => by dsimp only; split_ifs <;> assumption,
      fun _ => hGᵢ, fun _ => gramPhaseEquiv_refl _,
      fun t => by simp only [Nat.succ_ne_zero, if_false]; exact gramPhaseEquiv_refl _,
      fun h => ?_, fun h => h1i (gramPhaseEquiv_symm (h 0))⟩
    have := h 0
    simp only [if_true] at this
    exact h1i this
  · -- clause (i)
    intro G₁ G₂ _ _ h₁ h₂ h0 t
    cases t with
    | zero => exact h0
    | succ n => exact gramPhaseEquiv_trans (h₁ n) (gramPhaseEquiv_symm (h₂ n))
  · -- not L-PROP: clause (ii) fails
    rintro ⟨_, hex⟩
    exact hii hex

/-- **`ΦT` — the `L2` countercontrol.** The alternation `Φ t = ΦI` at even `t` and `ΦP` at odd `t`
is an `L-PROP` law, total and admissibility-preserving, and **no single transition equals it at
every time**: `Φ 0 = id` and `Φ 1 = Φ_σ` differ on `G(Hᵢ)`, whose class `σ` moves. -/
theorem phiT_l2_restricts :
    ∃ Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ, (∀ t i j, Γ t i j = 1 / 4)
      ∧ ProperAt (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1))
          ((fun t G => if Even t then G else RelabelTransition (Equiv.swap (2 : Fin 4) 3) G :
            ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) t (𝔾 t)))
      ∧ PropagatesFrom (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1))
          ((fun t G => if Even t then G else RelabelTransition (Equiv.swap (2 : Fin 4) 3) G :
            ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) t (𝔾 t)))
      ∧ EvolvesTotally (Fin 1) Γ
          (fun t G => if Even t then G else RelabelTransition (Equiv.swap (2 : Fin 4) 3) G)
      ∧ PreservesAdmissible (Fin 1) Γ
          (fun t G => if Even t then G else RelabelTransition (Equiv.swap (2 : Fin 4) 3) G)
      ∧ ¬ ∃ Φ₀ : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
          ∀ t, (fun t G => if Even t then G else RelabelTransition (Equiv.swap (2 : Fin 4) 3) G :
            ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)) t = Φ₀ := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  set σ : Equiv.Perm (Fin 4) := Equiv.swap (2 : Fin 4) 3 with hσ
  set Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) :=
    fun t G => if Even t then G else RelabelTransition σ G with hΦ
  have hΓinv : ∀ i j, Γ₀ (σ i) (σ j) = Γ₀ i j := fun i j => by rw [hΓ₀]; simp
  have hG₁ := sh1_necessity hadm₁
  have hGᵢ := sh1_necessity hadmᵢ
  have hrel : ∀ t {G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ}, RealizableGram (Fin 1) Γ₀ G →
      RealizableGram (Fin 1) Γ₀ (Φ t G) := by
    intro t G hG
    simp only [hΦ]
    split_ifs
    · exact hG
    · exact realizable_relabel (0 : Fin 1) σ hΓinv hG
  have hd : ∀ (t : ℕ) (G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), GramPhaseEquiv G G' →
      GramPhaseEquiv (Φ t G) (Φ t G') := by
    intro t G G' h
    simp only [hΦ]
    split_ifs
    · exact h
    · exact relabel_gramPhaseEquiv σ h
  have hfix' : ∀ t, Φ t (FibreGram 0 H₁) = FibreGram 0 H₁ := by
    intro t
    simp only [hΦ]
    split_ifs
    · rfl
    · exact hfix
  -- the composite trajectory from a realizable initial tuple
  have hcomp : ∀ (G₀ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₀ → ∀ t,
      RealizableGram (Fin 1) Γ₀
        (Nat.rec (motive := fun _ => Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) G₀ (fun s H => Φ s H) t) := by
    intro G₀ hG₀ t
    induction t with
    | zero => exact hG₀
    | succ n ih => exact hrel n ih
  refine ⟨fun _ => Γ₀, fun t i j => by rw [hΓ₀]; rfl, ?_, ?_, ?_, fun t _ hG => hrel t hG, ?_⟩
  · -- proper
    refine ⟨fun _ => FibreGram 0 H₁,
      fun t => Nat.rec (motive := fun _ => Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (FibreGram 0 Hᵢ)
        (fun s H => Φ s H) t,
      fun t => if t = 0 then FibreGram 0 H₁ else FibreGram 0 Hᵢ, fun _ => hG₁, hcomp _ hGᵢ,
      fun t => by dsimp only; split_ifs <;> assumption,
      fun t => by dsimp only; rw [hfix']; exact gramPhaseEquiv_refl _,
      fun t => gramPhaseEquiv_refl _, fun h => h1i (h 0), fun h => ?_⟩
    have := h 0
    simp only [zero_add, one_ne_zero, if_false, if_true, hfix'] at this
    exact h1i (gramPhaseEquiv_symm this)
  · -- propagates
    refine ⟨fun G₁ G₂ _ _ h₁ h₂ h0 => (ol1a_descent (0 : Fin 1) (fun _ => Γ₀) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => FibreGram 0 H₁,
      fun t => Nat.rec (motive := fun _ => Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (FibreGram 0 Hᵢ)
        (fun s H => Φ s H) t, le_rfl, fun _ => hG₁, hcomp _ hGᵢ,
      fun t => by dsimp only; rw [hfix']; exact gramPhaseEquiv_refl _,
      fun t => gramPhaseEquiv_refl _, ?_⟩
    show ¬ GramPhaseEquiv (FibreGram 0 H₁) (Φ 0 (FibreGram 0 Hᵢ))
    simp only [hΦ, Even.zero, if_true]
    exact h1i
  · -- total
    exact fun G₀ hG₀ => ⟨fun t => Nat.rec (motive := fun _ => Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) G₀
      (fun s H => Φ s H) t, hcomp G₀ hG₀, fun t => gramPhaseEquiv_refl _, gramPhaseEquiv_refl _⟩
  · -- not time-homogeneous
    rintro ⟨Φ₀, hΦ₀⟩
    have h01 : Φ 0 = Φ 1 := by rw [hΦ₀ 0, hΦ₀ 1]
    have := congrFun h01 (FibreGram 0 Hᵢ)
    simp only [hΦ, Even.zero, if_true, Nat.not_even_one, if_false] at this
    exact hmove (this ▸ gramPhaseEquiv_refl _)

/-- **`L1` on the class the shared theorem produces, at a time-homogeneous configuration.** Every
transition family satisfying `L0`, `L2` and `L4d` at a visible family with `Γ t = Γ 0` for all `t`
satisfies `L1`, for the relation on the whole per-slice orbit space: a realizable `G` at time `t` is
realizable at time `0`, `L0` gives a solution `𝔾` with `[𝔾 0] = [G]`, `𝔾 1` is realizable and
`∼_D`-equivalent to `Φ 0 G = Φ t G` by descent and `L2`, and realizability is a class property.
**The hypothesis `L2` is used**: without it the transition at a time `t ≥ 1` is unconstrained on
classes no solution reaches, and the implication is not claimed. -/
theorem l1_free_on_shared_class (Γ : ℕ → Matrix V V ℝ) (hΓ : ∀ t, Γ t = Γ 0) (a₀ : A)
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    (hd : ∀ t (G G' : V → Matrix V V ℂ), GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    (h2 : ∃ Φ₀ : (V → Matrix V V ℂ) → (V → Matrix V V ℂ), ∀ t, Φ t = Φ₀)
    (h0 : EvolvesTotally A Γ Φ) : PreservesAdmissible A Γ Φ := by
  intro t G hG
  obtain ⟨Φ₀, hΦ₀⟩ := h2
  rw [hΓ t] at hG
  obtain ⟨𝔾, hreal, hlaw, hinit⟩ := h0 G hG
  have h1 : GramPhaseEquiv (𝔾 1) (Φ t G) := by
    have := gramPhaseEquiv_trans (hlaw 0) (hd 0 _ _ hinit)
    rwa [hΦ₀ 0, ← hΦ₀ t] at this
  have := realizable_of_gramPhaseEquiv a₀ (hreal 1) h1
  rwa [hΓ 1, ← hΓ (t + 1)] at this


/-! ### Section F — the frozen product configuration: the product embedding, `ΦPP` and `ΦCTRL`

`V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`, `a₀ = (0, 0)`, `Γ ≡ 1/16`, the pointwise product of two
copies of `Γ ≡ ¼`. The product embedding `⊠` on fibre-Gram tuples is written inline throughout —
`(G₁ ⊠ G₂) i j k = G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2` — and spends no definition slot. The
**construction work the freeze names** is discharged first: the index-wise product of two
admissible single-carrier dilations is an admissible dilation for the product family at the product
anchor, its fibre-Gram tuple is the product of the factors' tuples, and so the product of two
realizable tuples is realizable — through act 18's merged `prod_mem_unitaryGroup` and
`prod_admissible` and act 12's `sh1_necessity`. -/

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- The cross-invariant of a product tuple is the product of the factors' cross-invariants at the
factor indices. -/
theorem product_cross {V₁ V₂ : Type} (X : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ)
    (a₁ b₁ : V₁) (a₂ b₂ : V₂) :
    (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2) (a₁, a₂)
        (b₁, b₂) (a₁, a₂)
        * (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2) (b₁, b₂)
          (a₁, a₂) (b₁, b₂)
      = (X a₁ b₁ a₁ * X b₁ a₁ b₁) * (Y a₂ b₂ a₂ * Y b₂ a₂ b₂) := by
  simp only [Matrix.of_apply]
  ring

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- The product permutation relabels a product tuple factorwise. -/
theorem relabel_product {V₁ V₂ : Type} (σ₁ : Equiv.Perm V₁) (σ₂ : Equiv.Perm V₂)
    (X : V₁ → Matrix V₁ V₁ ℂ) (Y : V₂ → Matrix V₂ V₂ ℂ) :
    RelabelTransition (Equiv.prodCongr σ₁ σ₂)
        (fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ => X i.1 j.1 k.1 * Y i.2 j.2 k.2)
      = fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
          RelabelTransition σ₁ X i.1 j.1 k.1 * RelabelTransition σ₂ Y i.2 j.2 k.2 := by
  funext i
  ext j k
  simp [RelabelTransition, Matrix.submatrix_apply]

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
theorem relabel_one (G : V → Matrix V V ℂ) : RelabelTransition (1 : Equiv.Perm V) G = G := by
  funext i
  ext j k
  simp [RelabelTransition, Matrix.submatrix_apply]

omit [Fintype A] [DecidableEq A] in
/-- At `|A| = 1` the visible-carrier block of a unitary on `V × Fin 1` is unitary on `V`. -/
theorem vpart_unitary {U : Matrix (V × Fin 1) (V × Fin 1) ℂ}
    (hU : U ∈ Matrix.unitaryGroup (V × Fin 1) ℂ) :
    (Matrix.of fun i j : V => U (i, 0) (j, 0)) ∈ Matrix.unitaryGroup V ℂ := by
  rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose] at hU ⊢
  ext i j
  have h := congrFun (congrFun hU (i, 0)) (j, 0)
  rw [Matrix.mul_apply, Fintype.sum_prod_type] at h
  simp only [Fin.sum_univ_one, Matrix.conjTranspose_apply] at h
  rw [Matrix.mul_apply]
  simp only [Matrix.conjTranspose_apply, Matrix.of_apply]
  rw [h]
  by_cases hij : i = j
  · subst hij; simp
  · simp [hij]

omit [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A] in
/-- **The product embedding lands in the realizable set** — the construction the freeze names as
`L5`'s honest cost. The index-wise product of admissible single-carrier dilations `U₁`, `U₂` (at
`|A₁| = |A₂| = 1`) is an admissible dilation for the pointwise-product family at the product
anchor, by act 18's merged `prod_mem_unitaryGroup` and `prod_admissible` (the `V`-factor being the
product of the two visible blocks and the `A`-factor the identity on `Fin 1 × Fin 1`), and its
fibre-Gram tuple is the product embedding of the factors' tuples. -/
theorem product_realizable {V₁ V₂ : Type} [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂]
    {Γ₁ : Matrix V₁ V₁ ℝ} {Γ₂ : Matrix V₂ V₂ ℝ}
    {U₁ : Matrix (V₁ × Fin 1) (V₁ × Fin 1) ℂ} {U₂ : Matrix (V₂ × Fin 1) (V₂ × Fin 1) ℂ}
    (h₁ : AdmissibleDilationAt Γ₁ (0 : Fin 1) U₁) (h₂ : AdmissibleDilationAt Γ₂ (0 : Fin 1) U₂) :
    ∃ U : Matrix ((V₁ × V₂) × (Fin 1 × Fin 1)) ((V₁ × V₂) × (Fin 1 × Fin 1)) ℂ,
      AdmissibleDilationAt (Matrix.of fun i j : V₁ × V₂ => Γ₁ i.1 j.1 * Γ₂ i.2 j.2)
          ((0 : Fin 1), (0 : Fin 1)) U
        ∧ FibreGram ((0 : Fin 1), (0 : Fin 1)) U
          = fun i : V₁ × V₂ => Matrix.of fun j k : V₁ × V₂ =>
              FibreGram (0 : Fin 1) U₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) U₂ i.2 j.2 k.2 := by
  classical
  set P₁ : Matrix V₁ V₁ ℂ := Matrix.of fun i j => U₁ (i, 0) (j, 0) with hP₁
  set P₂ : Matrix V₂ V₂ ℂ := Matrix.of fun i j => U₂ (i, 0) (j, 0) with hP₂
  have hP₁u : P₁ᴴ * P₁ = 1 := by
    have := vpart_unitary h₁.1
    rwa [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose] at this
  have hP₂u : P₂ᴴ * P₂ = 1 := by
    have := vpart_unitary h₂.1
    rwa [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose] at this
  set P : Matrix (V₁ × V₂) (V₁ × V₂) ℂ := Matrix.of fun p q => P₁ p.1 q.1 * P₂ p.2 q.2 with hP
  have hPu : Pᴴ * P = 1 := by
    have := prod_mem_unitaryGroup P₁ P₂ hP₁u hP₂u
    rwa [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose] at this
  have hWu : (1 : Matrix (Fin 1 × Fin 1) (Fin 1 × Fin 1) ℂ)ᴴ
      * (1 : Matrix (Fin 1 × Fin 1) (Fin 1 × Fin 1) ℂ) = (1 : Matrix (Fin 1 × Fin 1) (Fin 1 × Fin 1) ℂ) := by
    simp
  have hΓ : ∀ i j : V₁ × V₂,
      (Matrix.of fun i j : V₁ × V₂ => Γ₁ i.1 j.1 * Γ₂ i.2 j.2) i j = ‖P i j‖ ^ 2 := by
    intro i j
    have e₁ := h₁.2 i.1 j.1
    have e₂ := h₂.2 i.2 j.2
    simp only [Fin.sum_univ_one] at e₁ e₂
    rw [Matrix.of_apply, e₁, e₂, hP, Matrix.of_apply, norm_mul, mul_pow]
    simp [hP₁, hP₂]
  refine ⟨Matrix.of fun p q => P p.1 q.1 * (1 : Matrix (Fin 1 × Fin 1) (Fin 1 × Fin 1) ℂ) p.2 q.2,
    prod_admissible _ P 1 hPu hWu hΓ, ?_⟩
  funext i
  ext j k
  rw [fibreGram_apply, Matrix.of_apply, fibreGram_apply, fibreGram_apply]
  simp only [Fintype.sum_prod_type, Fin.sum_univ_one, Matrix.of_apply, Matrix.one_apply_eq, mul_one,
    hP, hP₁, hP₂, star_mul', star_one]
  ring

/-- **The entries the product-configuration verdicts read**, on the pinned Hadamard objects: the
diagonal `G^{(0)}_{00} = ¼` of both, the cross-invariant `G^{(0)}_{10} · G^{(1)}_{01}` at `(0,1)` —
`1/16` on `G(H₁)`, `i/16` on `G(Hᵢ)` — the invariant at `(0,2)` and at `(0,3)` on `G(Hᵢ)`, `1/16`
and `i/16`, and the two off-diagonal entries `G(Hᵢ)^{(0)}_{02} = G(Hᵢ)^{(0)}_{03} = ¼`. -/
theorem hadamard_entries (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ)
    (hH₁ : H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1))
    (hHᵢ : Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
        1, -Complex.I, -1, Complex.I] p.1 q.1)) :
    FibreGram (0 : Fin 1) H₁ 0 0 0 = 1 / 4 ∧ FibreGram (0 : Fin 1) Hᵢ 0 0 0 = 1 / 4
      ∧ FibreGram (0 : Fin 1) H₁ 0 1 0 * FibreGram (0 : Fin 1) H₁ 1 0 1 = 1 / 16
      ∧ FibreGram (0 : Fin 1) Hᵢ 0 1 0 * FibreGram (0 : Fin 1) Hᵢ 1 0 1 = Complex.I / 16
      ∧ FibreGram (0 : Fin 1) Hᵢ 0 2 0 * FibreGram (0 : Fin 1) Hᵢ 2 0 2 = 1 / 16
      ∧ FibreGram (0 : Fin 1) Hᵢ 0 3 0 * FibreGram (0 : Fin 1) Hᵢ 3 0 3 = Complex.I / 16
      ∧ FibreGram (0 : Fin 1) Hᵢ 0 0 2 = 1 / 4 ∧ FibreGram (0 : Fin 1) Hᵢ 0 0 3 = 1 / 4
      ∧ RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ) 0 0 0 = 1 / 4
      ∧ RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ) 0 1 0
          * RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ) 1 0 1
          = Complex.I / 16
      ∧ RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ) 0 2 0
          * RelabelTransition (Equiv.swap (2 : Fin 4) 3) (FibreGram (0 : Fin 1) Hᵢ) 2 0 2
          = Complex.I / 16 := by
  subst hH₁ hHᵢ
  simp [fibreGram_apply, RelabelTransition, Matrix.submatrix_apply, Equiv.swap_apply_def]
  norm_num [Complex.ext_iff]

/-- **The product-configuration separations and fixings**, on the products of the pinned classes,
each certified through act 12's merged cross-invariant read at a named fibre pair of the product
carrier, through `product_cross`: `[G(H₁) ⊠ G(H₁)] ≠ [G(Hᵢ) ⊠ G(Hᵢ)]` at `((0,0),(1,0))`;
`Φ_{1×σ}` moves `[G(H₁) ⊠ G(Hᵢ)]`, at `((0,0),(0,2))`; no product class with first factor `[G(H₁)]`
and a realizable second factor equals `[G(Hᵢ) ⊠ G(Hᵢ)]`, at `((0,0),(1,0))` with the second
factor's diagonal read from realizability; `Φ_{σ×σ}` moves `[G(Hᵢ) ⊠ G(Hᵢ)]`, at `((0,0),(0,2))`,
and sends it off `[G(H₁) ⊠ G(H₁)]`, at `((0,0),(1,0))`; and both product permutations fix
`G(H₁) ⊠ G(H₁)` exactly, since `σ` fixes `G(H₁)`. -/
theorem product_separations (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ)
    (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ) (G₁ Gᵢ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)
    (hΓ₀ : Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ)))
    (hH₁ : H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1))
    (hHᵢ : Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
        1, -Complex.I, -1, Complex.I] p.1 q.1))
    (hG₁ : G₁ = FibreGram (0 : Fin 1) H₁) (hGᵢ : Gᵢ = FibreGram (0 : Fin 1) Hᵢ)
    (hfix : RelabelTransition (Equiv.swap (2 : Fin 4) 3) G₁ = G₁) :
    ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2)
        (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => Gᵢ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2)
      ∧ ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2)
          (RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3))
            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2))
      ∧ (∀ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂ →
          ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => Gᵢ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2)
            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2))
      ∧ ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => Gᵢ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2)
          (RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3))
            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => Gᵢ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2))
      ∧ ¬ GramPhaseEquiv (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2)
          (RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3))
            (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => Gᵢ i.1 j.1 k.1 * Gᵢ i.2 j.2 k.2))
      ∧ RelabelTransition (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3))
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2)
          = (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2)
      ∧ RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3))
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2)
          = (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 => G₁ i.1 j.1 k.1 * G₁ i.2 j.2 k.2) := by
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  rw [← hG₁] at d1 c1
  rw [← hGᵢ] at di ci ci2 ci3 e2 e3 r0 r1 r2
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · intro h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [product_cross, product_cross, ci, di, c1, d1] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    rw [relabel_product, relabel_one] at h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4))
    rw [product_cross, product_cross, r2, d1, ci2] at this
    norm_num [Complex.ext_iff] at this
  · intro G₂ hG₂ h
    have hdiag : G₂ 0 0 0 = 1 / 4 := by
      rw [hG₂.2.2.2 0 0, hΓ₀, Matrix.of_apply]
      norm_num
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [product_cross, product_cross, c1, hdiag, ci, di] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    rw [relabel_product] at h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4))
    rw [product_cross, product_cross, r0, r2, di, ci2] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    rw [relabel_product] at h
    have := gramPhaseEquiv_cross_invariant h ((0 : Fin 4), (0 : Fin 4)) ((1 : Fin 4), (0 : Fin 4))
    rw [product_cross, product_cross, r1, r0, c1, d1] at this
    norm_num [Complex.ext_iff] at this
  · rw [relabel_product, hfix]
  · rw [relabel_product, relabel_one, hfix]

/-- **`ΦPP` satisfies the frozen ladder at the frozen product configuration**, `L5` included with
content: the product permutation `σ × σ` (`σ = (2 3)` on each factor) relabels product tuples
factorwise (`relabel_product`), so `FactorizesOnProduct` holds with `Φ₁ = Φ₂ = Φ_σ` **as an
equality**, before any equivalence. The remaining rungs are the carrier relabelling's, at the
product carrier: totality, admissibility preservation and surjectivity from `realizable_relabel`,
injectivity from `gramPhaseEquiv_of_relabel`, descent from `relabel_gramPhaseEquiv`, the `L-PROP`
conjuncts from the product separations (`G(H₁) ⊠ G(H₁)` fixed, `G(Hᵢ) ⊠ G(Hᵢ)` moved, the two
inequivalent, the realizability of both products by the product embedding), and **`L4n` from act
20's merged lift and exact law at `V = Fin 4 × Fin 4`, `A = Fin 1 × Fin 1`** — `RelabelLift (σ × σ)`
with `rnt2_lifting_property`, `rnt2_admissible` and `rnt3_law_exact`, consumed at merged strength. -/
theorem phiPP_ladder :
    ∃ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ) (Γ₁ : ℕ → Matrix (Fin 4) (Fin 4) ℝ),
      (∀ t i j, Γ t i j = 1 / 16) ∧ (∀ t i j, Γ₁ t i j = 1 / 4)
        ∧ LadderConds (Fin 1) (Fin 1) ((0 : Fin 1), (0 : Fin 1)) Γ (Equiv.refl (Fin 4 × Fin 4)) Γ₁ Γ₁
          (fun _ G => RelabelTransition
            (Equiv.prodCongr (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) G) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨s1, s2, s3, s4, s5, f1, f2⟩ :=
    product_separations Γ₀ H₁ Hᵢ _ _ hΓ₀ hH₁ hHᵢ rfl rfl hfix
  set σ : Equiv.Perm (Fin 4) := Equiv.swap (2 : Fin 4) 3 with hσ
  set τ : Equiv.Perm (Fin 4 × Fin 4) := Equiv.prodCongr σ σ with hτ
  set Γp : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
    Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 with hΓp
  set a₀ : Fin 1 × Fin 1 := ((0 : Fin 1), (0 : Fin 1)) with ha₀
  set P₁₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hP₁₁
  set Pᵢᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2
    with hPᵢᵢ
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨Uᵢᵢ, hUᵢᵢ, hFᵢᵢ⟩ := product_realizable hadmᵢ hadmᵢ
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1) Γp P₁₁ := by
    have := sh1_necessity hU₁₁; rwa [hF₁₁] at this
  have hRᵢᵢ : RealizableGram (Fin 1 × Fin 1) Γp Pᵢᵢ := by
    have := sh1_necessity hUᵢᵢ; rwa [hFᵢᵢ] at this
  have hΓinv : ∀ i j, Γp (τ i) (τ j) = Γp i j := fun i j => by simp [hΓp, hΓ₀]
  have hΓinv' : ∀ i j, Γp (τ.symm i) (τ.symm j) = Γp i j := fun i j => by simp [hΓp, hΓ₀]
  have hrel : ∀ {G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ},
      RealizableGram (Fin 1 × Fin 1) Γp G → RealizableGram (Fin 1 × Fin 1) Γp (RelabelTransition τ G) :=
    fun hG => realizable_relabel a₀ τ hΓinv hG
  have hd : ∀ (t : ℕ) (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (RelabelTransition τ G) (RelabelTransition τ G') :=
    fun _ _ _ h => relabel_gramPhaseEquiv τ h
  have hiter : ∀ (G₀ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G₀ →
      ∀ t, RealizableGram (Fin 1 × Fin 1) Γp ((RelabelTransition τ)^[t] G₀) := by
    intro G₀ hG₀ t
    induction t with
    | zero => exact hG₀
    | succ n ih => rw [Function.iterate_succ_apply']; exact hrel ih
  have hlawiter : ∀ (G₀ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ) t,
      GramPhaseEquiv ((RelabelTransition τ)^[t + 1] G₀)
        (RelabelTransition τ ((RelabelTransition τ)^[t] G₀)) := by
    intro G₀ t
    rw [Function.iterate_succ_apply']
    exact gramPhaseEquiv_refl _
  refine ⟨fun _ => Γp, fun _ => Γ₀, fun t i j => by simp [hΓp, hΓ₀]; norm_num,
    fun t i j => by rw [hΓ₀]; rfl, ?_, ?_, ?_, ?_, ⟨_, fun _ => rfl⟩, ?_, hd, ?_, ?_⟩
  · -- ProperAt
    refine ⟨fun _ => P₁₁, fun t => (RelabelTransition τ)^[t] Pᵢᵢ,
      fun t => if t = 0 then P₁₁ else Pᵢᵢ, fun _ => hR₁₁, hiter _ hRᵢᵢ,
      fun t => by dsimp only; split_ifs <;> assumption,
      fun _ => by dsimp only; rw [f1]; exact gramPhaseEquiv_refl _,
      hlawiter _, fun h => s1 (h 0), fun h => ?_⟩
    have := h 0
    simp only [zero_add, one_ne_zero, if_false, if_true, f1] at this
    exact s1 (gramPhaseEquiv_symm this)
  · -- PropagatesFrom
    refine ⟨fun G₁ G₂ _ _ h₁ h₂ h0 => (ol1a_descent a₀ (fun _ => Γp) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => P₁₁, fun t => (RelabelTransition τ)^[t] Pᵢᵢ, le_rfl,
      fun _ => hR₁₁, hiter _ hRᵢᵢ, fun _ => by dsimp only; rw [f1]; exact gramPhaseEquiv_refl _,
      hlawiter _, ?_⟩
    simpa using s5
  · -- L0
    exact fun G₀ hG₀ => ⟨fun t => (RelabelTransition τ)^[t] G₀, hiter G₀ hG₀, hlawiter G₀,
      gramPhaseEquiv_refl _⟩
  · -- L1
    exact fun _ _ hG => hrel hG
  · -- L3i and L3s
    refine ⟨fun _ _ _ _ _ h => gramPhaseEquiv_of_relabel τ h, fun _ G' hG' =>
      ⟨RelabelTransition τ.symm G', realizable_relabel a₀ τ.symm hΓinv' hG', ?_⟩⟩
    dsimp only
    rw [relabel_symm_relabel]
    exact gramPhaseEquiv_refl _
  · -- L4n, from act 20's merged lift and exact law at the product carrier
    intro t
    exact ⟨RelabelLift τ, RelabelInducedLeft τ, RelabelInducedRight τ,
      fun U _ => rnt2_lifting_property τ a₀ U, fun U hU => rnt2_admissible hΓinv hU,
      rnt3_law_exact τ a₀⟩
  · -- L5, as an equality
    refine ⟨by simp, fun t i j => by simp [hΓp], fun _ => RelabelTransition σ,
      fun _ => RelabelTransition σ, fun t G₁ G₂ _ _ => ?_⟩
    simp only [Equiv.refl_apply]
    rw [relabel_product]
    exact gramPhaseEquiv_refl _

open Classical in
/-- **`ΦCTRL` — the controlled relabelling at the frozen product configuration**, written from the
configuration's own data — the named class `ω̄₁ = [G(H₁)]` and the permutation `σ = (2 3)` of the
second factor — and consulting no lift: on a tuple whose class has a product representative
`G(H₁) ⊠ G₂` with `G₂` realizable, apply `Φ_{1×σ}`; on every other tuple, the identity. **The
branch condition is stated of the class** (a `GramPhaseEquiv`-invariant property, by
`gramPhaseEquiv_trans`), which is the well-definedness obligation the freeze names for this
candidate, discharged by construction; on the two product classes the `L5` refutation reads,
`[G(H₁) ⊠ G(Hᵢ)]` and `[G(Hᵢ) ⊠ G(Hᵢ)]`, the branch taken is the one the freeze's case split names,
the second by the certified separation `product_separations` (3).

**Census.** `ΦCTRL` is an `L-PROP` law (proper at the product configuration, with the two constant
solutions at `[G(H₁) ⊠ G(H₁)]` and `[G(Hᵢ) ⊠ G(Hᵢ)]` and the constant at `[G(H₁) ⊠ G(Hᵢ)]` no
solution; propagating with both clauses), total, admissibility-preserving, time-homogeneous,
reversible in both conjuncts (`Φ ∘ Φ = id` exactly, `σ` being an involution) and descending. **It
fails `L4n`**: no representative-level lift of it is twisted-natural at act 20's strength. The
obstruction is the **right closure and right intertwining conjuncts read together**: for the weak
anchored gauge `K` with phase `−1` at `(0,3)` and `1` elsewhere, the induced `αR K` is a weak
anchored gauge with phases `c'`, and reading the lifting obligation at `U K` and at `U` for an
admissible `U` in each branch — the product dilations of `G(H₁) ⊠ G(Hᵢ)` and of `G(Hᵢ) ⊠ G(Hᵢ)` —
forces `conj(c'_{(0,0)}) · c'_{(0,2)}` to equal `−1` on the relabelled branch and `1` on the identity
branch, at the entry `((0,0), (0,0), (0,2))`, where both Gram tuples are nonzero. **The induced map
is fixed before the input and cannot see the branch.** **It fails `L5`**, by the freeze's
two-instance argument made exact: at `G(H₁) ⊠ G(Hᵢ)` the transition relabels the second factor and
at `G(Hᵢ) ⊠ G(Hᵢ)` it does not, so a factorization `Φ₁ ⊠ Φ₂` would give `Φ₂ G(Hᵢ)` two
`∼_D`-inequivalent values, certified through act 12's cross-invariant read at `((0,0),(0,2))` and
`((0,0),(0,0))` on both instances. -/
theorem phiCTRL_census :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      Γ₀ = Matrix.of (fun _ _ => (1 / 4 : ℝ))
        ∧ H₁ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1] p.1 q.1)
        ∧ Hᵢ = Matrix.of (fun p q : Fin 4 × Fin 1 =>
            (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, Complex.I, -1, -Complex.I; 1, -1, 1, -1;
              1, -Complex.I, -1, Complex.I] p.1 q.1)
        ∧ ∀ (Γ : ℕ → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ)
            (Φ : ℕ → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)),
          Γ = (fun _ => Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2) →
          Φ = (fun _ G => if ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
                ∧ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
                    FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
              then RelabelTransition
                (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G
              else G) →
          ProperAt ((0 : Fin 1), (0 : Fin 1)) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ PropagatesFrom ((0 : Fin 1), (0 : Fin 1)) Γ
              (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
          ∧ EvolvesTotally (Fin 1 × Fin 1) Γ Φ
          ∧ PreservesAdmissible (Fin 1 × Fin 1) Γ Φ
          ∧ (∃ Φ₀ : (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
              → (Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), ∀ t, Φ t = Φ₀)
          ∧ Reversible (Fin 1 × Fin 1) Γ Φ
          ∧ (∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
              GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
          ∧ (∀ t, ¬ ∃ Ψ αL αR : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ
                → Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ,
              (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                FibreGram ((0 : Fin 1), (0 : Fin 1)) (Ψ U) = Φ t (FibreGram ((0 : Fin 1), (0 : Fin 1)) U))
              ∧ (∀ U, AdmissibleDilationAt (Γ t) ((0 : Fin 1), (0 : Fin 1)) U →
                AdmissibleDilationAt (Γ (t + 1)) ((0 : Fin 1), (0 : Fin 1)) (Ψ U))
              ∧ TwistedNatural ((0 : Fin 1), (0 : Fin 1)) αL αR Ψ)
          ∧ ¬ FactorizesOnProduct (Fin 1 × Fin 1) (Fin 1) (Fin 1) (Equiv.refl (Fin 4 × Fin 4))
              (fun _ => Γ₀) (fun _ => Γ₀) Γ Φ := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, Hm, hΓ₀, hH₁, hHᵢ, hHm, hadm₁, hadmᵢ, hadmM, h1i, hm1, hmi, hfix, hmove,
    h1move⟩ := witness_supply
  obtain ⟨s1, s2, s3, s4, s5, f1, f2⟩ :=
    product_separations Γ₀ H₁ Hᵢ _ _ hΓ₀ hH₁ hHᵢ rfl rfl hfix
  obtain ⟨d1, di, c1, ci, ci2, ci3, e2, e3, r0, r1, r2⟩ := hadamard_entries H₁ Hᵢ hH₁ hHᵢ
  obtain ⟨U₁₁, hU₁₁, hF₁₁⟩ := product_realizable hadm₁ hadm₁
  obtain ⟨U₁ᵢ, hU₁ᵢ, hF₁ᵢ⟩ := product_realizable hadm₁ hadmᵢ
  obtain ⟨Uᵢᵢ, hUᵢᵢ, hFᵢᵢ⟩ := product_realizable hadmᵢ hadmᵢ
  have hG₁r := sh1_necessity hadm₁
  have hGᵢr := sh1_necessity hadmᵢ
  refine ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, ?_⟩
  intro Γ Φ hΓ hΦ
  subst hΓ
  have hΦt : ∀ t, Φ t = Φ 0 := fun t => by rw [hΦ]
  set Γp : Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℝ :=
    Matrix.of fun i j : Fin 4 × Fin 4 => Γ₀ i.1 j.1 * Γ₀ i.2 j.2 with hΓp
  set P₁₁ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) H₁ i.2 j.2 k.2
    with hP₁₁
  set P₁ᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2
    with hP₁ᵢ
  set Pᵢᵢ : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ := fun i =>
    Matrix.of fun j k => FibreGram (0 : Fin 1) Hᵢ i.1 j.1 k.1 * FibreGram (0 : Fin 1) Hᵢ i.2 j.2 k.2
    with hPᵢᵢ
  have hR₁₁ : RealizableGram (Fin 1 × Fin 1) Γp P₁₁ := by
    have := sh1_necessity hU₁₁; rwa [hF₁₁] at this
  have hR₁ᵢ : RealizableGram (Fin 1 × Fin 1) Γp P₁ᵢ := by
    have := sh1_necessity hU₁ᵢ; rwa [hF₁ᵢ] at this
  have hRᵢᵢ : RealizableGram (Fin 1 × Fin 1) Γp Pᵢᵢ := by
    have := sh1_necessity hUᵢᵢ; rwa [hFᵢᵢ] at this
  have hΓinv : ∀ i j, Γp (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) i)
      (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) j) = Γp i j :=
    fun i j => by simp [hΓp, hΓ₀]
  have hΓinvσ : ∀ i j, Γ₀ (Equiv.swap (2 : Fin 4) 3 i) (Equiv.swap (2 : Fin 4) 3 j) = Γ₀ i j :=
    fun i j => by rw [hΓ₀]; simp
  have hτs : (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)).symm
      = Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3) := by
    rw [Equiv.prodCongr_symm, Equiv.symm_swap]; rfl
  have hττ : ∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ,
      RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3))
        (RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G)
        = G := by
    intro G
    calc RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3))
          (RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G)
        = RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)).symm
          (RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G) := by
            rw [hτs]
      _ = G := relabel_relabel_symm _ G
  -- the two branches
  have hΦyes : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ)
      (G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ), RealizableGram (Fin 1) Γ₀ G₂ →
      GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
        FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2) →
      Φ t G = RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G := by
    intro t G G₂ h2 h
    simp only [hΦ]
    rw [if_pos ⟨G₂, h2, h⟩]
  have hno : ∀ G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ, GramPhaseEquiv G Pᵢᵢ →
      ¬ ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2) := by
    rintro G h ⟨G₂, h2, h'⟩
    exact s3 G₂ h2 (gramPhaseEquiv_trans (gramPhaseEquiv_symm h) h')
  have hΦno : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G Pᵢᵢ → Φ t G = G := by
    intro t G h
    simp only [hΦ]
    rw [if_neg (hno G h)]
  have hΦ11 : ∀ t, Φ t P₁₁ = P₁₁ := fun t => by
    rw [hΦyes t P₁₁ (FibreGram (0 : Fin 1) H₁) hG₁r (gramPhaseEquiv_refl _), f2]
  have hΦii : ∀ t, Φ t Pᵢᵢ = Pᵢᵢ := fun t => hΦno t Pᵢᵢ (gramPhaseEquiv_refl _)
  -- descent, admissibility preservation, involution
  have hd : ∀ t (G G' : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G') := by
    intro t G G' h
    simp only [hΦ]
    by_cases hc : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
    · obtain ⟨G₂, h2, hh⟩ := hc
      rw [if_pos ⟨G₂, h2, hh⟩, if_pos ⟨G₂, h2, gramPhaseEquiv_trans (gramPhaseEquiv_symm h) hh⟩]
      exact relabel_gramPhaseEquiv _ h
    · rw [if_neg hc, if_neg (fun ⟨G₂, h2, hh⟩ => hc ⟨G₂, h2, gramPhaseEquiv_trans h hh⟩)]
      exact h
  have hrel : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ),
      RealizableGram (Fin 1 × Fin 1) Γp G → RealizableGram (Fin 1 × Fin 1) Γp (Φ t G) := by
    intro t G hG
    simp only [hΦ]
    split_ifs
    · exact realizable_relabel ((0 : Fin 1), (0 : Fin 1)) _ hΓinv hG
    · exact hG
  have hinv : ∀ t (G : Fin 4 × Fin 4 → Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ), Φ t (Φ t G) = G := by
    intro t G
    by_cases hc : ∃ G₂ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G₂
        ∧ GramPhaseEquiv G (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1 * G₂ i.2 j.2 k.2)
    · obtain ⟨G₂, h2, hh⟩ := hc
      have hh' : GramPhaseEquiv
          (RelabelTransition (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) G)
          (fun i : Fin 4 × Fin 4 => Matrix.of fun j k : Fin 4 × Fin 4 =>
            FibreGram (0 : Fin 1) H₁ i.1 j.1 k.1
              * RelabelTransition (Equiv.swap (2 : Fin 4) 3) G₂ i.2 j.2 k.2) := by
        have := relabel_gramPhaseEquiv
          (Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)) hh
        rwa [relabel_product, relabel_one] at this
      rw [hΦyes t G G₂ h2 hh, hΦyes t _ _ (realizable_relabel (0 : Fin 1) _ hΓinvσ h2) hh', hττ]
    · simp only [hΦ]
      rw [if_neg hc, if_neg hc]
  refine ⟨?_, ?_, ?_, fun t G hG => hrel t G hG, ⟨Φ 0, hΦt⟩, ?_, hd, ?_, ?_⟩
  · -- proper
    refine ⟨fun _ => P₁₁, fun _ => Pᵢᵢ, fun _ => P₁ᵢ, fun _ => hR₁₁, fun _ => hRᵢᵢ, fun _ => hR₁ᵢ,
      fun t => by rw [hΦ11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hΦii]; exact gramPhaseEquiv_refl _,
      fun h => s1 (h 0), fun h => ?_⟩
    have := h 0
    rw [hΦyes 0 P₁ᵢ (FibreGram (0 : Fin 1) Hᵢ) hGᵢr (gramPhaseEquiv_refl _)] at this
    exact s2 this
  · -- propagates
    exact ⟨fun G₁ G₂ _ _ h₁ h₂ h0 =>
        (ol1a_descent ((0 : Fin 1), (0 : Fin 1)) (fun _ => Γp) hd).2.1 G₁ G₂ h₁ h₂ h0,
      1, fun _ => P₁₁, fun _ => Pᵢᵢ, le_rfl, fun _ => hR₁₁, fun _ => hRᵢᵢ,
      fun t => by rw [hΦ11]; exact gramPhaseEquiv_refl _,
      fun t => by rw [hΦii]; exact gramPhaseEquiv_refl _, s1⟩
  · -- total
    intro G₀ hG₀
    refine ⟨fun t => (Φ 0)^[t] G₀, ?_, ?_, gramPhaseEquiv_refl _⟩
    · intro t
      induction t with
      | zero => exact hG₀
      | succ n ih =>
        show RealizableGram (Fin 1 × Fin 1) Γp ((Φ 0)^[n + 1] G₀)
        rw [Function.iterate_succ_apply']
        exact hrel 0 _ ih
    · intro t
      show GramPhaseEquiv ((Φ 0)^[t + 1] G₀) (Φ t ((Φ 0)^[t] G₀))
      rw [Function.iterate_succ_apply', hΦt t]
      exact gramPhaseEquiv_refl _
  · -- reversible
    exact ⟨fun t G G' _ _ h => by have := hd t _ _ h; rwa [hinv, hinv] at this,
      fun t G' hG' => ⟨Φ t G', hrel t G' hG', by rw [hinv]; exact gramPhaseEquiv_refl _⟩⟩
  · -- not L4n
    intro t
    rintro ⟨Ψ, αL, αR, hlift, -, -, hRclos, -, hR⟩
    obtain ⟨c, hc⟩ : ∃ c : Fin 4 × Fin 4 → ℂ,
        c = fun j => if j = ((0 : Fin 4), (3 : Fin 4)) then -1 else 1 := ⟨_, rfl⟩
    have hcval : ∀ j, c j = 1 ∨ c j = -1 := by
      intro j; rw [hc]; dsimp only; split_ifs <;> simp
    have hcnorm : ∀ j, ‖c j‖ = 1 := by
      intro j; rcases hcval j with h | h <;> simp [h]
    have hcc : ∀ j, c j * star (c j) = 1 := fun j => by
      rw [mul_comm, star_mul_self_eq_norm_sq, hcnorm, one_pow, Complex.ofReal_one]
    have hc00 : c ((0 : Fin 4), (0 : Fin 4)) = 1 := by rw [hc]; simp
    have hc02 : c ((0 : Fin 4), (2 : Fin 4)) = 1 := by rw [hc]; simp
    have hc03 : c ((0 : Fin 4), (3 : Fin 4)) = -1 := by rw [hc]; simp
    set K : Matrix ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ :=
      Matrix.diagonal (fun p : (Fin 4 × Fin 4) × (Fin 1 × Fin 1) => c p.1) with hK
    have hKc : ∀ (p : (Fin 4 × Fin 4) × (Fin 1 × Fin 1)) (j : Fin 4 × Fin 4),
        K p (j, ((0 : Fin 1), (0 : Fin 1))) = if p = (j, ((0 : Fin 1), (0 : Fin 1))) then c j else 0 := by
      intro p j
      rw [hK, Matrix.diagonal_apply]
      by_cases hp : p = (j, ((0 : Fin 1), (0 : Fin 1)))
      · subst hp; simp
      · simp [hp]
    have hKunit : K ∈ Matrix.unitaryGroup ((Fin 4 × Fin 4) × (Fin 1 × Fin 1)) ℂ := by
      rw [hK, Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose, Matrix.diagonal_conjTranspose,
        Matrix.diagonal_mul_diagonal]
      ext p q
      rw [Matrix.diagonal_apply, Matrix.one_apply]
      split_ifs with hpq <;> first | rfl | (subst hpq; simp only [Pi.star_apply]; exact hcc p.1)
    have hKw : WeakAnchorStabilizer ((0 : Fin 1), (0 : Fin 1)) K := ⟨hKunit, c, hKc⟩
    obtain ⟨-, c', hc'⟩ := hRclos K hKw
    have hτ00 : Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)
        ((0 : Fin 4), (0 : Fin 4)) = ((0 : Fin 4), (0 : Fin 4)) := by
      simp [Equiv.swap_apply_def]
    have hτ02 : Equiv.prodCongr (1 : Equiv.Perm (Fin 4)) (Equiv.swap (2 : Fin 4) 3)
        ((0 : Fin 4), (2 : Fin 4)) = ((0 : Fin 4), (3 : Fin 4)) := by
      simp
    -- the relabelled branch, read at U₁ᵢ K and at U₁ᵢ
    have hUyK := weak_preserves_admissible hU₁ᵢ hKw
    have hFyK : FibreGram ((0 : Fin 1), (0 : Fin 1)) (U₁ᵢ * K)
        = fun i => Matrix.of fun j k => star (c j) * P₁ᵢ i j k * c k := by
      funext i; ext j k; rw [fibreGram_mul_weak_apply hKc, hF₁ᵢ]; rfl
    have hQy : GramPhaseEquiv (fun i => Matrix.of fun j k => star (c j) * P₁ᵢ i j k * c k) P₁ᵢ :=
      gramPhaseEquiv_symm ⟨c, hcnorm, fun i j k => rfl⟩
    have E1 := hlift (U₁ᵢ * K) hUyK
    rw [hR U₁ᵢ K hKw, hFyK, hΦyes t _ (FibreGram (0 : Fin 1) Hᵢ) hGᵢr hQy] at E1
    have E1' := congrFun (congrFun (congrFun E1 ((0 : Fin 4), (0 : Fin 4))) ((0 : Fin 4), (0 : Fin 4)))
      ((0 : Fin 4), (2 : Fin 4))
    rw [fibreGram_mul_weak_apply hc', hlift U₁ᵢ hU₁ᵢ, hF₁ᵢ,
      hΦyes t P₁ᵢ (FibreGram (0 : Fin 1) Hᵢ) hGᵢr (gramPhaseEquiv_refl _)] at E1'
    simp only [RelabelTransition, Matrix.submatrix_apply] at E1'
    rw [hτ00, hτ02] at E1'
    simp only [hP₁ᵢ, Matrix.of_apply] at E1'
    rw [d1, e3, hc00, hc03, star_one] at E1'
    have hE1 : star (c' ((0 : Fin 4), (0 : Fin 4))) * c' ((0 : Fin 4), (2 : Fin 4)) = -1 := by
      linear_combination 16 * E1'
    -- the identity branch, read at Uᵢᵢ K and at Uᵢᵢ
    have hUnK := weak_preserves_admissible hUᵢᵢ hKw
    have hFnK : FibreGram ((0 : Fin 1), (0 : Fin 1)) (Uᵢᵢ * K)
        = fun i => Matrix.of fun j k => star (c j) * Pᵢᵢ i j k * c k := by
      funext i; ext j k; rw [fibreGram_mul_weak_apply hKc, hFᵢᵢ]; rfl
    have hQn : GramPhaseEquiv (fun i => Matrix.of fun j k => star (c j) * Pᵢᵢ i j k * c k) Pᵢᵢ :=
      gramPhaseEquiv_symm ⟨c, hcnorm, fun i j k => rfl⟩
    have E2 := hlift (Uᵢᵢ * K) hUnK
    rw [hR Uᵢᵢ K hKw, hFnK, hΦno t _ hQn] at E2
    have E2' := congrFun (congrFun (congrFun E2 ((0 : Fin 4), (0 : Fin 4))) ((0 : Fin 4), (0 : Fin 4)))
      ((0 : Fin 4), (2 : Fin 4))
    rw [fibreGram_mul_weak_apply hc', hlift Uᵢᵢ hUᵢᵢ, hFᵢᵢ,
      hΦno t Pᵢᵢ (gramPhaseEquiv_refl _)] at E2'
    simp only [hPᵢᵢ, Matrix.of_apply] at E2'
    rw [di, e2, hc00, hc02, star_one] at E2'
    have hE2 : star (c' ((0 : Fin 4), (0 : Fin 4))) * c' ((0 : Fin 4), (2 : Fin 4)) = 1 := by
      linear_combination 16 * E2'
    rw [hE1] at hE2
    norm_num at hE2
  · -- not L5
    rintro ⟨-, -, Φ₁, Φ₂, hfac⟩
    have E1 := hfac 0 (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) Hᵢ) hG₁r hGᵢr
    have E2 := hfac 0 (FibreGram (0 : Fin 1) Hᵢ) (FibreGram (0 : Fin 1) Hᵢ) hGᵢr hGᵢr
    simp only [Equiv.refl_apply] at E1 E2
    rw [hΦyes 0 _ (FibreGram (0 : Fin 1) Hᵢ) hGᵢr (gramPhaseEquiv_refl _), relabel_product,
      relabel_one] at E1
    rw [← hPᵢᵢ, hΦno 0 Pᵢᵢ (gramPhaseEquiv_refl _)] at E2
    have a1 := gramPhaseEquiv_cross_invariant E1 ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4))
    have b1 := gramPhaseEquiv_cross_invariant E1 ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    have a2 := gramPhaseEquiv_cross_invariant E2 ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (2 : Fin 4))
    have b2 := gramPhaseEquiv_cross_invariant E2 ((0 : Fin 4), (0 : Fin 4)) ((0 : Fin 4), (0 : Fin 4))
    rw [hPᵢᵢ] at a2 b2
    rw [product_cross, product_cross] at a1 b1 a2 b2
    rw [r2, d1] at a1
    rw [r0, d1] at b1
    rw [ci2, di] at a2
    rw [di] at b2
    have hw : Φ₂ 0 (FibreGram (0 : Fin 1) Hᵢ) 0 0 0 * Φ₂ 0 (FibreGram (0 : Fin 1) Hᵢ) 0 0 0 ≠ 0 := by
      intro h0
      rw [h0, mul_zero] at b1
      norm_num at b1
    have hx := mul_right_cancel₀ hw (b1.trans b2.symm)
    rw [hx, a2] at a1
    norm_num [Complex.ext_iff] at a1

end OrbitLawRigidityTwisted
end OIBridge

/-! ### The axiom table — one line per named result, printed by the kernel -/

#print axioms OIBridge.OrbitLawRigidityTwisted.composite_descends
#print axioms OIBridge.OrbitLawRigidityTwisted.solution_eq_composite
#print axioms OIBridge.OrbitLawRigidityTwisted.ol1a_descent
#print axioms OIBridge.OrbitLawRigidityTwisted.iterate_descends
#print axioms OIBridge.OrbitLawRigidityTwisted.ol1b_monoid_action
#print axioms OIBridge.OrbitLawRigidityTwisted.realizable_of_gramPhaseEquiv
#print axioms OIBridge.OrbitLawRigidityTwisted.realizable_relabel
#print axioms OIBridge.OrbitLawRigidityTwisted.relabel_gramPhaseEquiv
#print axioms OIBridge.OrbitLawRigidityTwisted.relabel_relabel_symm
#print axioms OIBridge.OrbitLawRigidityTwisted.relabel_symm_relabel
#print axioms OIBridge.OrbitLawRigidityTwisted.gramPhaseEquiv_of_relabel
#print axioms OIBridge.OrbitLawRigidityTwisted.witness_supply
#print axioms OIBridge.OrbitLawRigidityTwisted.factorizes_trivial
#print axioms OIBridge.OrbitLawRigidityTwisted.phiI_ladder
#print axioms OIBridge.OrbitLawRigidityTwisted.phiP_ladder
#print axioms OIBridge.OrbitLawRigidityTwisted.siop_yes
#print axioms OIBridge.OrbitLawRigidityTwisted.phiX_l0_restricts
#print axioms OIBridge.OrbitLawRigidityTwisted.phiC_census
#print axioms OIBridge.OrbitLawRigidityTwisted.phiT_l2_restricts
#print axioms OIBridge.OrbitLawRigidityTwisted.l1_free_on_shared_class
#print axioms OIBridge.OrbitLawRigidityTwisted.product_cross
#print axioms OIBridge.OrbitLawRigidityTwisted.relabel_product
#print axioms OIBridge.OrbitLawRigidityTwisted.relabel_one
#print axioms OIBridge.OrbitLawRigidityTwisted.vpart_unitary
#print axioms OIBridge.OrbitLawRigidityTwisted.product_realizable
#print axioms OIBridge.OrbitLawRigidityTwisted.hadamard_entries
#print axioms OIBridge.OrbitLawRigidityTwisted.product_separations
#print axioms OIBridge.OrbitLawRigidityTwisted.phiPP_ladder
#print axioms OIBridge.OrbitLawRigidityTwisted.phiCTRL_census
