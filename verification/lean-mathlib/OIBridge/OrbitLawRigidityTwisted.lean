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
    simp [fibreGram_apply, Fin.sum_univ_one] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    have := gramPhaseEquiv_cross_invariant h 0 1
    rw [hHᵢ] at this
    simp [fibreGram_apply, Fin.sum_univ_one] at this
    norm_num [Complex.ext_iff] at this
  · rw [hH₁]
    funext i
    ext j k
    simp only [RelabelTransition, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one]
    fin_cases i <;> fin_cases j <;> fin_cases k <;> simp [Equiv.swap_apply_def] <;> norm_num
  · intro h
    have := gramPhaseEquiv_cross_invariant h 0 2
    rw [hHᵢ] at this
    simp [RelabelTransition, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one,
      Equiv.swap_apply_def] at this
    norm_num [Complex.ext_iff] at this
  · intro h
    have := gramPhaseEquiv_cross_invariant h 0 1
    rw [hH₁, hHᵢ] at this
    simp [RelabelTransition, Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one,
      Equiv.swap_apply_def] at this
    norm_num [Complex.ext_iff] at this


/-! ### Section D — the census at the frozen single-carrier configuration: `ΦI`, `ΦP`, and `SIOP`

At the single-carrier configuration the ladder's `L5` conjunct is read at the **trivial
decomposition** `V ≃ V × Fin 1` with the second visible family identically `1`, where it carries no
content (`factorizes_trivial`, proved for every transition family): `L5` is a condition at product
configurations and the single-carrier census is not where it bites. The census verdicts below are
each about the exact family frozen under its label at the exact frozen configuration. -/

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

end OrbitLawRigidityTwisted
end OIBridge
