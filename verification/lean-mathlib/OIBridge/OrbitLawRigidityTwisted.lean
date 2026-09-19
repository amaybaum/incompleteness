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

end OrbitLawRigidityTwisted
end OIBridge
