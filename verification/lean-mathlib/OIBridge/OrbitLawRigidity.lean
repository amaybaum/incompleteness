import OIBridge.IntermediateCrossTimeStructure

/-!
# Act 19 — the rigidity of the cross-time laws act 18 opened

Executed under the frozen control plane
`verification/programmes/oi-qm/track-b/act-19-orbit-law-rigidity/preregistration.md`,
blob `8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`, from the merge commit of that control plane,
`84b469a8f78d538b204353e66c6066ab197d1a82`, which the freeze fixes as this round's mandated base.

## What this round is

Act 18 showed that a genuine cross-time law plus one initial orbit can propagate: a law writable
from the anchor and the visible family before any lift exists, stated at orbit level so that it
descends, whose solution set at one exhibited configuration is nonempty, non-singleton modulo act
17's `GramTrajEquiv` and proper, has the property that two of its solutions agreeing at time `0`
have the same trajectory, with the initial orbit doing work. **That answers an existence question
and opens a uniqueness question**, and the uniqueness question is this round's whole subject:
**given that a genuine cross-time law plus one initial orbit can propagate, how rigid is the class
of such laws?**

**The round does NOT try to derive Schrödinger evolution.** It classifies what act 18 opened.
Deriving or recognising quantum evolution is a **later round** and is an explicit non-doing here.
No statement of this module says, implies or approaches the claim that a surviving law is,
resembles, approximates or points toward quantum evolution, and no condition of the ladder below is
stated with quantum evolution as its standard of correctness.

## The condition ladder, frozen before any census

The eight definitions below are the round's whole definition budget, and six of them carry the
ladder the freeze fixes **before** any census of surviving laws is run:

* `TransitionLaw` — the law a transition family generates, whose **first conjunct is `L4d`**, the
  descent of the transition to `GramPhaseEquiv`-classes. `L4d` is the shared structural theorem's
  own hypothesis and is reported as a hypothesis and not as a discharged rung.
* `EvolvesTotally` — **`L0`**, the totality of the induced evolution on the admissible orbit state
  space at time `0`. Act 18's propagation supplies uniqueness from the initial orbit and
  non-degeneracy; it does **not** supply that every admissible initial orbit extends to a solution
  at all, and `L0` is that gap and nothing else.
* `PreservesAdmissible` — **`L1`**, stated for the relation on the **whole** per-slice orbit space
  and not merely along the law's own solutions, which is the strictly stronger reading and the
  demand the condition is meant to make.
* `LadderConds` — the conjunction, carrying **`L2`** (time-homogeneity, and the composition of the
  induced evolution, as two conjuncts so that a candidate failing either is reported against the
  conjunct it fails) and **`L4n`** (representative-level gauge-naturality against act 12's merged
  `fibreGram_left_mul` and `fibreGram_mul_weak_apply`) inline.
* `Reversible` — **`L3i`** and **`L3s`**, injectivity and surjectivity on classes, **stated and
  reported apart**. On a finite set the two coincide, but the admissible orbit space is a quotient
  of a set cut out by `RealizableGram` over a complex matrix space and nothing merged says it is
  finite, so a verdict reaching one is not reported as reaching the other.
* `FactorizesOnProduct` — **`L5`**, factorization on product classes at a product configuration,
  the product presentation supplied as explicit data and `⊠` written inline as the entrywise
  product of fibre-Gram tuples induced by the Kronecker product of admissible dilations. **Nothing
  in it mentions unitary evolution, a generator, a one-parameter group, continuity, a Hamiltonian
  or Schrödinger's equation**: every object in it is the repository's own.

The remaining two slots are `LawEquiv` — the law equivalence `≈_L`, equality of solution sets among
pointwise realizable trajectories, which **introduces no new identification**, both laws compared
being class-invariant by the descent conjunct they carry — and `SameInitialOrbitPair`, the
discriminating test, carrying the **earlier-agreement conjunct** so that what an exhibited witness
exhibits is primitive non-uniqueness and not a divergence propagated forward from an earlier one.

**Every equivalence any verdict of this round is taken modulo is one of three**, each established
before act 19: act 12's `GramPhaseEquiv`, act 17's `GramTrajEquiv`, and `LawEquiv`, which is set
equality of solution sets and is defined from those two and equality alone. **No other equivalence
is adopted**: not raw Gram equality, not the uniform-phase relation, not act 13's level-2 or
level-3 relations, and no conjugacy or similarity relation on transition families.

## What none of this licenses

**THE CLAUSE, carried at this mention — the module docstring's statement of what is not licensed.**
Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.**

**The condition list and the law list are closed and are neither exhaustive.** Six conditions and
seven named transition families are frozen for testing; a condition outside them is neither imposed
nor refuted here, and a law outside them is neither refuted nor endorsed. **A rung found to be
implied stays in the ladder** and stays in the conjunction the headline quantifies over: no
artifact of this round reports the ladder as having fewer rungs than the freeze names.

**Nothing here is about the threading, the cross-time representative, the relative evolution or the
relative candidate.** These are invisible to `GramTrajEquiv` by construction, and a round that
cannot see a distinction may not report one, in either direction: act 11's `GL2` pair is **one**
trajectory here. Act 16's cancellation cell and act 15's fork are untouched in either direction, no
carrier of act 14 is read, defined or adopted, act 10's anchor-axis reclassification is untouched,
and act 18's `D`-axis and its readback data are untouched — this round consumes the `L`-axis
element of act 18's headline pair and says nothing about the other. `GL1s`, `GL1w`, `GL2`, `GL3`,
`GI2`, `LG1`, `RO1`, `TG2`, `TG3`, `SH1`, `SH1-C1`, `SH1-C2`, `AB0`–`AB2`, `CT1`–`CT4`, `CL1`,
`PQ0`–`PQ4`, `CF0`–`CF5`, `RN0`–`RN4`, `TJ0`–`TJ3` and `XS0`–`XS5` are consumed and none is
revised. **Act 12's classification, act 17's `TJ1` and `TJ3` and act 18's `XS1` and `L-PROP` are
consumed at merged strength**, and act 12's `GramPhaseEquiv` and act 17's `GramTrajEquiv` are
consumed and neither is redefined — act 12 supplies the slice equivalence and act 17 supplies the
trajectory lift of it.

`P0` stays **OPEN** and two-part and its threading part is untouched. `CoherentLift` is
`ℕ`-indexed and this round does not change that: no continuity, smoothness, derivative or continuum
limit is introduced or used, and the first-divergence conjunct uses nothing beyond successor and
order on `ℕ`. Nothing here realizes a transition as an operator, a unitary, a generator or a group
element. Nothing here says OI and QM are inequivalent, and every visibility statement is under act
7's own readback convention with `D4b` **negative**. Nothing is imported from the substratum Lemma
24.1 rounds, and nothing here is about Track I.
-/

namespace OIBridge
namespace OrbitLawRigidity

set_option linter.unusedSectionVars false

open Finset Matrix DilationChoice CoherentLiftGauge TwoSidedGauge CrossTimeInvariants
  GramTrajectorySelection IntermediateCrossTimeStructure

open scoped ComplexOrder

variable {V A : Type} [Fintype V] [DecidableEq V] [Fintype A] [DecidableEq A]

/-! ### Section A — the budgeted definitions: the condition ladder, frozen before any census

**Eight top-level definitions, and these are the eight the freeze budgets.** No lift, gauge
element, witness, matrix, visible family, Gram tuple, entry value, permutation, class or
configuration is a top-level definition here: each is a bound variable pinned by an equation in the
statement that needs it, exactly as acts 10 through 18 did. Acts 7's, 10's, 11's, 12's, 13's, 17's
and 18's definitions are **reused, not redefined**. -/

/-- **THE LAW A TRANSITION FAMILY GENERATES** (definition slot 1), carrying the **`L4d`** descent
conjunct as its first component.

A transition family `Φ` is written at representative level and is required to **descend**:
`GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G')` at every `t`. The descent conjunct is part
of the object and is not commentary on it, for the reason act 18 recorded for its own generator
law: a representative-level transition that does not descend "selects" by fixing an unphysical
frame, and what it determines is the frame and not the orbit.

The law the family generates is `Law_Φ 𝔾 ≡ ∀ t, GramPhaseEquiv (𝔾 (t+1)) (Φ t (𝔾 t))`. This is a
**law datum** in act 18's frozen sense: it is written from `(a₀, Γ, ℕ)` alone, it is constructed
before any lift exists and it consults no lift at any point. **The property that does the work is
lift-blindness, not canonicity** — act 18's own candidates take a prescribed matrix family and a
named pseudometric and neither is a canonical function of the visible family — and this round reads
act 18's definition exactly as act 18 wrote it, neither narrowing nor widening it.

**`L4d`'s honest rung status is `L4d-HYP`.** It is the shared structural theorem's own hypothesis,
so it cannot be a further restriction on the action class that theorem produces, and neither
`L4d-RESTRICTS` nor `L4d-FREE` is a meaningful verdict about it. -/
def TransitionLaw (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (Law : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  (∀ (t : ℕ) (G G' : V → Matrix V V ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    ∧ ∀ 𝔾 : ℕ → V → Matrix V V ℂ, Law 𝔾 ↔ ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))

set_option linter.unusedVariables false in
/-- **`L0` — A WELL-DEFINED TOTAL EVOLUTION ON THE ADMISSIBLE ORBIT STATE SPACE** (definition slot
2). For **every** class in the admissible orbit state space at time `0` there is a pointwise
realizable solution of the law starting in it.

**Totality is the content, and it is not already given.** Act 18's propagation supplies
**uniqueness** from the initial orbit and **non-degeneracy**. It does **not** supply that every
admissible initial orbit extends to a solution at all: a law whose solutions exist only through a
named subset of the orbit space satisfies both of act 18's clauses while failing to be an evolution
of the state space — it is an evolution of part of it. Together with act 18's uniqueness clause,
`L0` is what makes the induced `E_t` a **total function** on the orbit space at time `0`, with
`E_0` the identity. -/
def EvolvesTotally (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (Law : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  ∀ G₀ : V → Matrix V V ℂ, RealizableGram A (Γ 0) G₀ →
    ∃ 𝔾 : ℕ → V → Matrix V V ℂ,
      (∀ t, RealizableGram A (Γ t) (𝔾 t)) ∧ Law 𝔾 ∧ GramPhaseEquiv (𝔾 0) G₀

set_option linter.unusedVariables false in
/-- **`L1` — PRESERVATION OF POINTWISE ADMISSIBILITY** (definition slot 3). The transition carries
admissible tuples to admissible tuples as a **relation on the whole per-slice orbit space**, and
not merely along the law's own solutions.

**Stated for the relation and not for its restriction to solutions, deliberately.** Restricted to
solutions the condition is close to vacuous, a solution being pointwise realizable by definition.
Stated for the whole orbit space it is a real demand on the transition, and it is the demand the
condition is meant to make: an evolution that must be truncated to stay admissible is not an
evolution of the admissible orbit space. -/
def PreservesAdmissible (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  ∀ (t : ℕ) (G : V → Matrix V V ℂ),
    RealizableGram A (Γ t) G → RealizableGram A (Γ (t + 1)) (Φ t G)

set_option linter.unusedVariables false in
/-- **`L3` — REVERSIBILITY, AS TWO CONJUNCTS** (definition slot 4), so that each is reported apart.

**`L3i`, the first conjunct — injectivity on classes.** `GramPhaseEquiv (Φ̂ G) (Φ̂ G') →
GramPhaseEquiv G G'` for `G`, `G'` admissible at the configuration.

**`L3s`, the second conjunct — surjectivity on classes.** Every admissible class is in the image.

**"Where appropriate" is made precise here rather than left to the execution.** On a finite set
injectivity and surjectivity coincide and it would be convenient to state `L3` as one conjunct.
**The admissible orbit space need not be finite**: it is a quotient of a set cut out by
`RealizableGram` over a complex matrix space, and nothing merged says it is finite at any
configuration where this round works. So the two conjuncts are **stated and reported apart**, and a
verdict that reaches one is not reported as reaching the other. Where the orbit space **is** shown
finite in the kernel at the frozen configuration, one conjunct may be derived from the other and
the derivation is recorded with the configuration it was run at; finiteness is never assumed. -/
def Reversible (a₀ : A) (Γ₀ : Matrix V V ℝ)
    (Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  (∀ G G' : V → Matrix V V ℂ, RealizableGram A Γ₀ G → RealizableGram A Γ₀ G' →
      GramPhaseEquiv (Phih G) (Phih G') → GramPhaseEquiv G G')
    ∧ ∀ G' : V → Matrix V V ℂ, RealizableGram A Γ₀ G' →
        ∃ G : V → Matrix V V ℂ, RealizableGram A Γ₀ G ∧ GramPhaseEquiv (Phih G) G'

set_option linter.unusedVariables false in
/-- **`L5` — COMPOSITION OF INDEPENDENT SYSTEMS** (definition slot 5, conditional — **fired**, the
owner settlement retaining `L5` in the ladder).

At a **product configuration** — carrier presented as `V₁ × V₂`, ancilla as `A₁ × A₂`, anchor the
corresponding pair, and the visible family the **pointwise product**
`Γ ((i₁,i₂),(j₁,j₂)) = Γ₁ (i₁,j₁) · Γ₂ (i₂,j₂)` — the time-homogeneous transition **factorizes on
product classes**: there are transitions on the two factors' orbit spaces with
`Φ̂ (G₁ ⊠ G₂) ≈ (Φ̂₁ G₁) ⊠ (Φ̂₂ G₂)` for every pair of admissible `G₁`, `G₂`, the equivalence being
act 12's `GramPhaseEquiv`.

`⊠` is written inline as the **entrywise product** of fibre-Gram tuples,
`(G₁ ⊠ G₂) (i₁,i₂) (j₁,j₂) (k₁,k₂) = G₁ i₁ j₁ k₁ · G₂ i₂ j₂ k₂`, which is what the fibre-Gram tuple
of the Kronecker product of two admissible dilations computes to, index by index, by the same
argument act 18's `prod_mem_unitaryGroup` and `prod_admissible` already carry for the
carrier–ancilla product. The product presentation is supplied as explicit data — two equivalences
and the two factor families — rather than as a definitional identification of the carrier, so that
the condition is stateable at a configuration whose carrier is not literally a product type.

**Nothing in this statement mentions unitary evolution, a generator, a one-parameter group,
continuity, a Hamiltonian or Schrödinger's equation.** Every object in it is the repository's own:
the entrywise product of matrices, act 12's `FibreGram`, act 12's `GramPhaseEquiv` and act 12's
`RealizableGram`. **The identity transition satisfies it**, which is the freeze's certificate that
`L5` does not presuppose the answer: the identity transition is manifestly not quantum evolution in
any sense. -/
def FactorizesOnProduct (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) : Prop :=
  ∀ (V₁ V₂ A₁ A₂ : Type) [Fintype V₁] [DecidableEq V₁] [Fintype V₂] [DecidableEq V₂]
      [Fintype A₁] [Fintype A₂] (eV : V ≃ V₁ × V₂) (eA : A ≃ A₁ × A₂)
      (Γ₁ : Matrix V₁ V₁ ℝ) (Γ₂ : Matrix V₂ V₂ ℝ)
      (Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ)),
    (∀ t, Φ t = Phih) →
    (∀ i j : V, Γ 0 i j = Γ₁ (eV i).1 (eV j).1 * Γ₂ (eV i).2 (eV j).2) →
      ∃ (Phi1 : (V₁ → Matrix V₁ V₁ ℂ) → (V₁ → Matrix V₁ V₁ ℂ))
        (Phi2 : (V₂ → Matrix V₂ V₂ ℂ) → (V₂ → Matrix V₂ V₂ ℂ)),
        ∀ G₁ G₂, RealizableGram A₁ Γ₁ G₁ → RealizableGram A₂ Γ₂ G₂ →
          GramPhaseEquiv
            (Phih fun i => Matrix.of fun j k =>
              G₁ (eV i).1 (eV j).1 (eV k).1 * G₂ (eV i).2 (eV j).2 (eV k).2)
            (fun i => Matrix.of fun j k =>
              Phi1 G₁ (eV i).1 (eV j).1 (eV k).1 * Phi2 G₂ (eV i).2 (eV j).2 (eV k).2)

/-- **THE LADDER, AS ONE `Prop`** (definition slot 6). **This is the single declaration the ordering
obligation pins**, and the ladder cannot be made checkable without it.

The conjuncts, in order:

1. `TransitionLaw Φ Law` — the object itself, whose first component is **`L4d`**.
2. `ProperAt` and `PropagatesFrom`, act 18's own definitions consumed unmodified — the standing
   hypothesis that the candidate is an **`L-PROP` law in act 18's frozen sense**. A candidate that
   is not one is not on this ladder at all, and its exclusion is a consequence of act 18's
   definitions and not a condition of this round. Propagation carries **both** of act 18's frozen
   clauses, uniqueness from the initial orbit and the initial orbit contributing.
3. `EvolvesTotally` — **`L0`**.
4. `PreservesAdmissible` — **`L1`**.
5. **`L2`, inline, as two conjuncts.** Time-homogeneity: a single `Φ̂` with `Φ t = Φ̂` at every `t`,
   so one law iterates consistently. And compositionality of the induced evolution on classes,
   `E_{t+s} = E_s ∘ E_t` with `E_t = Φ̂^t`. Independence of `t` gives `E_t = Φ̂^t` by induction only
   once the descent conjunct has made `Φ̂` a function on classes; the two are kept as two conjuncts
   so that a candidate failing either is reported against the conjunct it fails.
6. `Reversible` — **`L3i`** and **`L3s`**, of the time-homogeneous transition.
7. **`L4n`, inline — representative-level gauge-naturality.** The transition lifts to
   representatives naturally under act 12's two-sided moves: there is a map `Ψ` on dilations
   inducing the transition on fibre-Gram tuples, and it **commutes with the two merged
   transformation laws on `FibreGram`** — act 12's `fibreGram_left_mul`, under which the constant
   and time-dependent in-fibre left moves of `LeftFibreGroup` are invisible, and act 12's
   `fibreGram_mul_weak_apply`, under which a right gauge at the anchor acts by the anchored phases
   (the strong right gauge being the special case of the weak one in which those phases are
   trivial). Commuting with them is exactly this: an in-fibre left move on `Ψ`'s input produces an
   in-fibre left move on its output, and a right gauge at the anchor on its input produces a right
   gauge at the anchor on its output, so that **the invisible gauge cannot see the transition's
   action beyond the class**. **`L4n` is a genuine strengthening of `L4d` and is tested as one.**
   Descent says the
   transition is a function on classes; naturality says it comes from a move on representatives
   that the invisible gauge cannot see. The second does not follow from the first, and act 18 named
   the alternative route explicitly: its generator law discharged descent by writing the candidate
   at orbit level, precisely so that a representative-level naturality proof would not be needed.
8. `FactorizesOnProduct` — **`L5`**.

**Neither a `RESTRICTS` nor a `FREE` verdict enlarges or shrinks this conjunction.** A rung found
to be implied stays in the ladder and stays in the conjunction the headline quantifies over. -/
def LadderConds (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (Law : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  TransitionLaw Φ Law
    ∧ ProperAt a₀ Γ Law
    ∧ PropagatesFrom a₀ Γ Law
    ∧ EvolvesTotally a₀ Γ Law
    ∧ PreservesAdmissible a₀ Γ Φ
    ∧ (∃ Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ), ∀ t, Φ t = Phih)
    ∧ (∀ Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ), (∀ t, Φ t = Phih) →
        ∀ (t s : ℕ) (G : V → Matrix V V ℂ), RealizableGram A (Γ 0) G →
          GramPhaseEquiv (Phih^[t + s] G) (Phih^[s] (Phih^[t] G)))
    ∧ (∀ Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ), (∀ t, Φ t = Phih) →
        Reversible a₀ (Γ 0) Phih)
    ∧ (∃ Ψ : ℕ → Matrix (V × A) (V × A) ℂ → Matrix (V × A) (V × A) ℂ,
        (∀ (t : ℕ) (U : Matrix (V × A) (V × A) ℂ), AdmissibleDilationAt (Γ t) a₀ U →
            Φ t (FibreGram a₀ U) = FibreGram a₀ (Ψ t U))
          ∧ (∀ (t : ℕ) (L U : Matrix (V × A) (V × A) ℂ), LeftFibreGroup L →
              ∃ L' : Matrix (V × A) (V × A) ℂ, LeftFibreGroup L' ∧ Ψ t (L * U) = L' * Ψ t U)
          ∧ ∀ (t : ℕ) (U K : Matrix (V × A) (V × A) ℂ), WeakAnchorStabilizer a₀ K →
              ∃ K' : Matrix (V × A) (V × A) ℂ,
                WeakAnchorStabilizer a₀ K' ∧ Ψ t (U * K) = Ψ t U * K')
    ∧ FactorizesOnProduct a₀ Γ Φ

set_option linter.unusedVariables false in
/-- **`≈_L`, THE LAW EQUIVALENCE** (definition slot 7) — two laws have the **same solution set**
among pointwise realizable trajectories.

**This is not a new relation.** It is set equality of solution sets, and it identifies no objects
that act 12's `GramPhaseEquiv` and act 17's `GramTrajEquiv` do not already identify: both laws
compared carry the descent conjunct of `TransitionLaw`, so the two sets compared are already
saturated under act 17's trajectory equivalence. **`≈_L` introduces no new identification and is
defined from act 12's slice equivalence, act 17's trajectory lift of it, and equality alone.**

All three headline outcomes are stated over it. **No equivalence outside the freeze's three may be
used to reach a rigidity verdict**: a plurality that would collapse only under some other
equivalence **is a plurality**, and any such candidate is recorded as an observation for a later
round with its own freeze and is never applied to this round's verdict. -/
def LawEquiv (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (Law Law' : (ℕ → V → Matrix V V ℂ) → Prop) : Prop :=
  ∀ 𝔾 : ℕ → V → Matrix V V ℂ, (∀ t, RealizableGram A (Γ t) (𝔾 t)) → (Law 𝔾 ↔ Law' 𝔾)

set_option linter.unusedVariables false in
/-- **`SIOP`, THE SAME-INITIAL-ORBIT PAIR, EXHIBITED AT ITS FIRST DIVERGENCE** (definition slot 8) —
the discriminating test, as one `Prop`.

Two transition families both satisfying the condition predicate supplied, whose laws are **not**
`≈_L`-equivalent, with two pointwise realizable solutions that **agree at every time strictly
before `t*`** and are inequivalent at `t*`, with `1 ≤ t*`.

**The earlier-agreement conjunct is what makes `t*` the FIRST divergence, and it is part of the
witness and not commentary on it.** A difference at a later time caused merely by feeding
already-different states forward is **not primitive non-uniqueness** — it is the same divergence
propagated, and reporting it as the discriminating witness would overstate what was found. A clean
first-divergence formulation is available because `ℕ` carries successor and order and is
well-ordered, so a pair of trajectories that differ at all has a **least** time at which they
differ; **nothing beyond successor and order is used**, no continuity, no limit and no metric on
the index.

**At `t* = 1` the earlier-agreement conjunct reduces to agreement at time `0`**, which is the
same-initial-orbit hypothesis itself: the two laws are handed the same initial orbit and disagree
at the very next step. That is primitive non-uniqueness in the plainest available sense.

The condition predicate is supplied as a parameter so that the proposition can be stated over the
exact conjunction the kernel discharges, with that conjunction named at every use. **Searching and
not finding earns nothing**: the absence of an exhibited pair is not a proof that none exists. -/
def SameInitialOrbitPair (a₀ : A) (Γ : ℕ → Matrix V V ℝ)
    (Conds : (ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)) →
      ((ℕ → V → Matrix V V ℂ) → Prop) → Prop) : Prop :=
  ∃ (Φ Φ' : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (Law Law' : (ℕ → V → Matrix V V ℂ) → Prop)
    (𝔾 𝔾' : ℕ → V → Matrix V V ℂ) (tstar : ℕ),
    Conds Φ Law ∧ Conds Φ' Law' ∧ ¬ LawEquiv a₀ Γ Law Law'
      ∧ (∀ t, RealizableGram A (Γ t) (𝔾 t)) ∧ (∀ t, RealizableGram A (Γ t) (𝔾' t))
      ∧ Law 𝔾 ∧ Law' 𝔾'
      ∧ 1 ≤ tstar
      ∧ (∀ s, s < tstar → GramPhaseEquiv (𝔾 s) (𝔾' s))
      ∧ ¬ GramPhaseEquiv (𝔾 tstar) (𝔾' tstar)

/-! ### Section B — `OL1`, the shared structural theorem, which RUNS FIRST

**This target runs before the census and before the discriminating test.** It is assumption-light
and structural, and it is what turns "a law that propagates" into "an action on a state space",
which is the object the ladder's rungs are conditions on.

**What `OL1` is NOT.** It is **not** a statement that such a law exists — act 18's `L-PROP` supplies
that and this round consumes it. It is **not** a statement that the action is faithful, transitive,
free, continuous or by any kind of symmetry. It is **not** a statement about laws that fail `L2` or
`L4d`, about which it says nothing in either direction. And it is **not** a bridge to any
representation theory: `Φ̄` is a function on classes and is realized here as no operator, no
unitary, no generator and no group element. -/

/-- **`OL1` (a), THE GENERAL FORM — AN `L-PROP` LAW THAT IS QUOTIENT-WELL-DEFINED AND COMPOSITIONAL
DESCENDS TO A COMPOSITION OF MAPS ON THE ADMISSIBLE ORBIT SPACES.**

The composite `E` is a **bound variable pinned by its two defining equations** — `E 0` the identity
and `E (t+1) = Φ t ∘ E t` — and is not a definition of this round. Four conjuncts:

1. **`E t` is well defined on `GramPhaseEquiv`-classes**, at every `t`: this is `L4d`, the first
   conjunct of `TransitionLaw`, propagated along the composite by induction. So each `E t` induces a
   map `Ω_0 → Ω_t`, and the evolution from the initial orbit is **a function of the initial class
   alone**.
2. **The solution set is read off the transition**: a trajectory solves the law iff
   `[𝔾 (t+1)] = Φ̄_t [𝔾 t]` at every `t`.
3. **Every solution is the composite applied to its own initial slice**, `[𝔾 t] = [E t (𝔾 0)]`.
4. **And the composite's own trajectories are solutions that are realized by a coherent lift.**

**The `TJ1` dependence is named at the step and not in a footnote, and it is conjunct 4.** Reading
the solution set as a composition of maps on per-time state spaces requires the ambient admissible
set to be the **product over time** of those spaces: intersecting a product constraint with a
non-product ambient set need not factor, and it is act 17's merged `tj1_sufficiency` that proves the
ambient set **is** the product, so that a trajectory assembled slice by slice from the composite
stays inside it. Without `TJ1` conjunct 4 does not follow. `TJ1` is consumed at merged strength and
is neither enlarged nor re-proved here. -/
theorem ol1a_descends_to_composition {a₀ : A} {Γ : ℕ → Matrix V V ℝ}
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    {Law : (ℕ → V → Matrix V V ℂ) → Prop}
    (hTL : TransitionLaw Φ Law)
    (E : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (hE0 : ∀ G, E 0 G = G) (hEs : ∀ t G, E (t + 1) G = Φ t (E t G)) :
    (∀ (t : ℕ) (G G' : V → Matrix V V ℂ),
        GramPhaseEquiv G G' → GramPhaseEquiv (E t G) (E t G'))
      ∧ (∀ 𝔾 : ℕ → V → Matrix V V ℂ, Law 𝔾 ↔ ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
      ∧ (∀ 𝔾 : ℕ → V → Matrix V V ℂ, Law 𝔾 → ∀ t, GramPhaseEquiv (𝔾 t) (E t (𝔾 0)))
      ∧ (∀ G₀ : V → Matrix V V ℂ, (∀ t, RealizableGram A (Γ t) (E t G₀)) →
          Law (fun t => E t G₀)
            ∧ ∃ U : ℕ → Matrix (V × A) (V × A) ℂ,
                CoherentLift a₀ Γ U ∧ ∀ t, FibreGram a₀ (U t) = E t G₀) := by
  refine ⟨?_, hTL.2, ?_, ?_⟩
  · intro t
    induction t with
    | zero => intro G G' h; rw [hE0, hE0]; exact h
    | succ n ih => intro G G' h; rw [hEs, hEs]; exact hTL.1 n _ _ (ih G G' h)
  · intro 𝔾 hLaw t
    induction t with
    | zero => rw [hE0]; exact gramPhaseEquiv_refl _
    | succ n ih =>
        rw [hEs]
        exact gramPhaseEquiv_trans ((hTL.2 𝔾).1 hLaw n) (hTL.1 n _ _ ih)
  · intro G₀ hreal
    refine ⟨(hTL.2 _).2 fun t => ?_, tj1_sufficiency a₀ hreal⟩
    rw [hEs]
    exact gramPhaseEquiv_refl _

/-- **`OL1` (b), THE HOMOGENEOUS FORM — AT A TIME-HOMOGENEOUS VISIBLE FAMILY THE LAW IS A MONOID
ACTION OF `(ℕ, +)` ON THE ADMISSIBLE ORBIT SPACE.**

At `Γ t = Γ₀` at every `t` the admissible orbit space is the same set at every time, so there **is**
a single set for a monoid to act on; with `L2` the transition family is constant and the composite
is `E_t = Φ̂^t`. Five conjuncts: the state space is constant; `E_0` is the identity; the semigroup
law `E_{t+s} = E_s ∘ E_t`; well-definedness of every `E_t` on classes; and every solution sitting at
`[Φ̂^t (𝔾 0)]`.

**The theorem is split in two and this half is stated at time-homogeneous configurations only.**
When the orbit space varies with `t` there is no single set for a monoid to act on, and what one has
is a composable family of maps between different sets — a composition and not an action. Writing (b)
as though it held generally would overstate the theorem, and writing only (a) would lose the
statement the round actually wants.

**This is a descent statement and not an existence statement.** That an `L-PROP` law exists is act
18's and is consumed. It says nothing about faithfulness, transitivity, freeness or any symmetry
property of the induced action, and **the action is not a group**: `(ℕ, +)` is a monoid and no
inverse is claimed for `Φ̂` here. Reversibility is a separate rung of the ladder and is reported
separately. -/
theorem ol1b_monoid_action {a₀ : A} {Γ : ℕ → Matrix V V ℝ} {Γ₀ : Matrix V V ℝ}
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    {Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    {Law : (ℕ → V → Matrix V V ℂ) → Prop}
    (hTL : TransitionLaw Φ Law) (hhom : ∀ t, Φ t = Phih) (hconst : ∀ t, Γ t = Γ₀) :
    (∀ t, RealizableGram A (Γ t) = RealizableGram A Γ₀)
      ∧ (∀ G : V → Matrix V V ℂ, Phih^[0] G = G)
      ∧ (∀ (t s : ℕ) (G : V → Matrix V V ℂ), Phih^[t + s] G = Phih^[s] (Phih^[t] G))
      ∧ (∀ (t : ℕ) (G G' : V → Matrix V V ℂ),
          GramPhaseEquiv G G' → GramPhaseEquiv (Phih^[t] G) (Phih^[t] G'))
      ∧ (∀ 𝔾 : ℕ → V → Matrix V V ℂ, Law 𝔾 → ∀ t, GramPhaseEquiv (𝔾 t) (Phih^[t] (𝔾 0))) := by
  have hd : ∀ G G' : V → Matrix V V ℂ,
      GramPhaseEquiv G G' → GramPhaseEquiv (Phih G) (Phih G') := by
    intro G G' h
    have h0 := hTL.1 0 G G' h
    rwa [hhom 0] at h0
  have hstep : ∀ (t : ℕ) (G G' : V → Matrix V V ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Phih^[t] G) (Phih^[t] G') := by
    intro t
    induction t with
    | zero => intro G G' h; simpa using h
    | succ n ih =>
        intro G G' h
        rw [Function.iterate_succ_apply', Function.iterate_succ_apply']
        exact hd _ _ (ih G G' h)
  refine ⟨fun t => by rw [hconst t], fun G => rfl, ?_, hstep, ?_⟩
  · intro t s G
    rw [add_comm t s]
    exact Function.iterate_add_apply Phih s t G
  · intro 𝔾 hLaw t
    induction t with
    | zero => simpa using gramPhaseEquiv_refl (𝔾 0)
    | succ n ih =>
        rw [Function.iterate_succ_apply']
        have hs := (hTL.2 𝔾).1 hLaw n
        rw [hhom n] at hs
        exact gramPhaseEquiv_trans hs (hd _ _ ih)

/-! ### Section C — `OL2` and `OL3`: the rung statuses and the census of the frozen candidate list

Every countercontrol below is at the configuration the freeze names for the obligation it
discharges, and at no other. **The frozen configuration for the single-carrier candidates** is act
12's: `V = Fin 4`, `A = Fin 1`, `a₀ = 0`, `Γ ≡ ¼`, with act 12's frozen Hadamard family. Every
visible family, lift, matrix, permutation and class below is a **bound variable pinned by an
equation in the statement that needs it**, never a top-level definition. -/

/-- Auxiliary, and **not a definition**: pointwise realizability is invariant under act 12's
per-slice equivalence. The four conjuncts of act 12's `RealizableGram` each transport across a
conjugation by the anchored phases — positive semidefiniteness because the conjugating matrix is
`Dᴴ · D`, the rank bound because rank does not increase under multiplication, the sum because `D`
is unitary, and the diagonal because the phases have modulus one.

Act 12's `RealizableGram` is **consumed and not redefined**; what is added is the observation that
it is a property of the orbit class and not merely of the representative, which is what lets a
verdict about admissibility be stated at class level at all. -/
theorem realizableGram_of_gramPhaseEquiv {Γ₀ : Matrix V V ℝ} {G G' : V → Matrix V V ℂ}
    (h : GramPhaseEquiv G G') (hG : RealizableGram A Γ₀ G) : RealizableGram A Γ₀ G' := by
  obtain ⟨c, hc, hGG⟩ := h
  have hcc : ∀ j, star (c j) * c j = 1 := by
    intro j
    rw [star_mul_self_eq_norm_sq, hc j, one_pow, Complex.ofReal_one]
  have key : ∀ (M : Matrix V V ℂ) (j k : V),
      ((Matrix.diagonal c)ᴴ * M * Matrix.diagonal c) j k = star (c j) * M j k * c k := by
    intro M j k
    rw [Matrix.diagonal_conjTranspose, Matrix.mul_diagonal, Matrix.diagonal_mul]
    simp
  have hEq : ∀ i, G' i = (Matrix.diagonal c)ᴴ * G i * Matrix.diagonal c := by
    intro i; ext j k; rw [key, hGG]
  refine ⟨fun i => ?_, fun i => ?_, ?_, fun i j => ?_⟩
  · rw [hEq i]; exact (hG.1 i).conjTranspose_mul_mul_same _
  · rw [hEq i]
    exact le_trans (Matrix.rank_mul_le_left _ _)
      (le_trans (Matrix.rank_mul_le_right _ _) (hG.2.1 i))
  · ext j k
    rw [Matrix.sum_apply]
    have : ∀ i : V, G' i j k = star (c j) * G i j k * c k := fun i => hGG i j k
    rw [Finset.sum_congr rfl fun i _ => this i, ← Finset.sum_mul, ← Finset.mul_sum]
    have hs : (∑ i : V, G i j k) = (1 : Matrix V V ℂ) j k := by
      rw [← Matrix.sum_apply]; rw [hG.2.2.1]
    rw [hs]
    by_cases hjk : j = k
    · subst hjk; rw [Matrix.one_apply_eq, mul_one, hcc]
    · rw [Matrix.one_apply_ne hjk]; ring
  · rw [hGG i j j, hG.2.2.2 i j]
    calc star (c j) * (Γ₀ i j : ℂ) * c j = (Γ₀ i j : ℂ) * (star (c j) * c j) := by ring
      _ = (Γ₀ i j : ℂ) := by rw [hcc j, mul_one]

/-- **`OL2`, `L1` — `L1-FREE` AT A TIME-HOMOGENEOUS CONFIGURATION, PROVED UNIVERSALLY AND NOT
SEARCHED FOR.** Every transition family satisfying the earlier rungs — the descent conjunct `L4d`,
`L0`, and `L2`'s time-homogeneity — satisfies `L1` at a time-homogeneous visible family.

The argument is the freeze's own and is three steps. `L0` hands every admissible class a solution
starting there; the law puts that solution's next slice at the transition's value on the class it
started in, by `L4d`; and that next slice is admissible because it is a slice of a pointwise
realizable solution. Admissibility being a property of the class, the transition's value on an
arbitrary admissible tuple is admissible.

**This is stated for the relation on the whole per-slice orbit space**, which is the strictly
stronger reading `L1` is frozen at, and not merely along the law's own solutions, where the
condition would be close to vacuous. **`L1-FREE` is a finding and not a shortfall**: it says the
rung was stated, tested and found to be implied. **The rung stays in the ladder** and stays in the
conjunction the headline quantifies over, and no artifact of this round reports the ladder as
having fewer rungs than the freeze names. -/
theorem ol2_l1_free {a₀ : A} {Γ : ℕ → Matrix V V ℝ} {Γ₀ : Matrix V V ℝ}
    {Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ)}
    {Law : (ℕ → V → Matrix V V ℂ) → Prop}
    (hTL : TransitionLaw Φ Law) (hconst : ∀ t, Γ t = Γ₀)
    (hhom : ∃ Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ), ∀ t, Φ t = Phih)
    (hL0 : EvolvesTotally a₀ Γ Law) :
    PreservesAdmissible a₀ Γ Φ := by
  obtain ⟨Phih, hP⟩ := hhom
  intro t G hG
  rw [hconst t] at hG
  obtain ⟨𝔾, hreal, hLaw, h0⟩ := hL0 G (by rw [hconst 0]; exact hG)
  have h3 : GramPhaseEquiv (𝔾 1) (Φ 0 G) :=
    gramPhaseEquiv_trans ((hTL.2 𝔾).1 hLaw 0) (hTL.1 0 _ _ h0)
  have h4 : RealizableGram A Γ₀ (𝔾 1) := by rw [← hconst 1]; exact hreal 1
  rw [hconst (t + 1), hP t, ← hP 0]
  exact realizableGram_of_gramPhaseEquiv h3 h4

/-- **`OL3`, `ΦI` — THE IDENTITY TRANSITION SURVIVES EVERY RUNG OF THE FROZEN LADDER**, at the
configuration this freeze names for it: `V = Fin 4`, `A = Fin 1`, anchor `0`, `Γ ≡ ¼`.

`ΦI` is **act 18's own `LC3`**, the generator law that carried act 18's `L-PROP`, with its descent
obligation discharged at orbit level by that round. It is consumed here as a merged instance and is
**not rebuilt**: act 18's `ProperAt` and `PropagatesFrom` conjuncts are taken at merged strength,
the only bridge being that the law this round writes as `[𝔾 (t+1)] = [𝔾 t]` and the law act 18
writes as `[𝔾 t] = [𝔾 (t+1)]` are the same predicate, act 12's per-slice equivalence being
symmetric.

Each rung is discharged separately: `L0` by the constant trajectory through any admissible class,
`L1` because the visible family is constant in time, `L2` because the transition is independent of
`t` and the identity iterates to itself, `L3i` and `L3s` because the identity is injective and
surjective on classes, `L4n` by the identity lift on representatives — which carries every in-fibre
left move and every right gauge at the anchor to itself — and `L5` because the identity factorizes
as the identity on each factor, **for every product presentation whatever**.

**`L5`'s satisfaction by `ΦI` is the freeze's certificate that `L5` does not presuppose the
answer**: the identity transition is manifestly not quantum evolution in any sense.

**THE CLAUSE, carried at this mention — the identity transition's census verdict.**
Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.** -/
theorem ol3_phiI_survives :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Law : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop),
      (∀ t i j, Γ t i j = 1 / 4) ∧ (∀ t, Γ t = Γ 0)
        ∧ Φ = (fun _ G => G)
        ∧ Law = (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t))
        ∧ LadderConds (0 : Fin 1) Γ Φ Law := by
  classical
  obtain ⟨Γ, Φ18, Law18, hΓ, hΦ18, hLaw18, _h1, _h2, hproper, hprop, _h3⟩ := lc3_generator_law
  have hΓc : ∀ t, Γ t = Γ 0 := by
    intro t; ext i j; rw [hΓ t i j, hΓ 0 i j]
  have hLeq : (fun 𝔾 : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ =>
      ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t)) = Law18 := by
    rw [hLaw18, hΦ18]
    funext 𝔾
    exact propext ⟨fun h t => gramPhaseEquiv_symm (h t), fun h t => gramPhaseEquiv_symm (h t)⟩
  refine ⟨Γ, fun _ G => G, fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t), hΓ, hΓc, rfl, rfl, ?_⟩
  refine ⟨⟨fun _ _ _ h => h, fun _ => Iff.rfl⟩, by rw [hLeq]; exact hproper,
    by rw [hLeq]; exact hprop, ?_, ?_, ⟨fun G => G, fun _ => rfl⟩, ?_, ?_, ?_, ?_⟩
  · intro G₀ hG₀
    exact ⟨fun _ => G₀, fun t => by rw [hΓc t]; exact hG₀, fun _ => gramPhaseEquiv_refl _,
      gramPhaseEquiv_refl _⟩
  · intro t G hG
    rw [hΓc (t + 1), ← hΓc t]
    exact hG
  · intro Phih hPhih t s G _
    have hp : Phih = fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => G := (hPhih 0).symm
    subst hp
    have hid : (fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => G) = id := rfl
    simp only [hid, Function.iterate_id, id_eq]
    exact gramPhaseEquiv_refl G
  · intro Phih hPhih
    have hp : Phih = fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => G := (hPhih 0).symm
    subst hp
    exact ⟨fun G G' _ _ h => h, fun G' h => ⟨G', h, gramPhaseEquiv_refl _⟩⟩
  · exact ⟨fun _ U => U, fun _ _ _ => rfl, fun _ L _ hL => ⟨L, hL, rfl⟩,
      fun _ _ K hK => ⟨K, hK, rfl⟩⟩
  · intro V₁ V₂ A₁ A₂ _ _ _ _ _ _ eV eA Γ₁ Γ₂ Phih hPhih _
    refine ⟨id, id, fun G₁ G₂ _ _ => ?_⟩
    have hp : Phih = fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => G := (hPhih 0).symm
    subst hp
    exact gramPhaseEquiv_refl _

/-- Auxiliary, and **not a definition**: a transition that **descends**, **preserves pointwise
realizability** and is an **involution** satisfies `L0`, `L1`, `L2` and both conjuncts of `L3` at a
time-homogeneous configuration, and is injective on classes.

Each rung comes from exactly one of the three hypotheses, and the proof records which. `L0` is the
orbit of the transition through the given class, admissible at every time by the second hypothesis
and a solution by construction. `L1` is the second hypothesis itself, the configuration being
constant in time. `L2`'s composition conjunct is the iteration identity and needs nothing. `L3i`
follows because the transition descends and squares to the identity, so an equivalence between two
images pushes forward to an equivalence between the arguments; `L3s` because the transition is its
own inverse and preserves admissibility.

**The three hypotheses are exactly what the rungs need and nothing more.** In particular no
finiteness of the admissible orbit space is assumed anywhere, and neither conjunct of `L3` is
derived from the other. -/
theorem ladder_of_involutive_transition {Γ₀ : Matrix V V ℝ} (a₀ : A)
    (P : (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (hdesc : ∀ G G', GramPhaseEquiv G G' → GramPhaseEquiv (P G) (P G'))
    (hreal : ∀ G, RealizableGram A Γ₀ G → RealizableGram A Γ₀ (P G))
    (hinvol : ∀ G, P (P G) = G) :
    TransitionLaw (fun _ => P) (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)))
      ∧ EvolvesTotally a₀ (fun _ => Γ₀) (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)))
      ∧ PreservesAdmissible a₀ (fun _ => Γ₀) (fun _ => P)
      ∧ (∀ Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ),
          (∀ t : ℕ, (fun _ => P) t = Phih) → ∀ (t s : ℕ) (G : V → Matrix V V ℂ),
            RealizableGram A Γ₀ G → GramPhaseEquiv (Phih^[t + s] G) (Phih^[s] (Phih^[t] G)))
      ∧ (∀ Phih : (V → Matrix V V ℂ) → (V → Matrix V V ℂ),
          (∀ t : ℕ, (fun _ => P) t = Phih) → Reversible a₀ Γ₀ Phih)
      ∧ (∀ X, RealizableGram A Γ₀ X → ∀ t, RealizableGram A Γ₀ (P^[t] X))
      ∧ (∀ G G', GramPhaseEquiv (P G) (P G') → GramPhaseEquiv G G') := by
  have horb : ∀ X, RealizableGram A Γ₀ X → ∀ t, RealizableGram A Γ₀ (P^[t] X) := by
    intro X hX t
    induction t with
    | zero => simpa using hX
    | succ n ih => rw [Function.iterate_succ_apply']; exact hreal _ ih
  have hPI : ∀ G G', GramPhaseEquiv (P G) (P G') → GramPhaseEquiv G G' := by
    intro G G' h
    have h2 := hdesc _ _ h
    rwa [hinvol, hinvol] at h2
  refine ⟨⟨fun _ G G' h => hdesc G G' h, fun _ => Iff.rfl⟩, ?_, fun _ G h => hreal G h, ?_, ?_,
    horb, hPI⟩
  · intro G₀ hG₀
    refine ⟨fun t => P^[t] G₀, horb G₀ hG₀, fun t => ?_, ?_⟩
    · show GramPhaseEquiv (P^[t + 1] G₀) (P (P^[t] G₀))
      rw [Function.iterate_succ_apply']
      exact gramPhaseEquiv_refl _
    · simpa using gramPhaseEquiv_refl G₀
  · intro Phih hPhih t s G _
    have hp : P = Phih := hPhih 0
    subst hp
    rw [add_comm t s, Function.iterate_add_apply]
    exact gramPhaseEquiv_refl _
  · intro Phih hPhih
    have hp : P = Phih := hPhih 0
    subst hp
    exact ⟨fun G G' _ _ h => hPI G G' h,
      fun G' hG' => ⟨P G', hreal _ hG', by rw [hinvol]; exact gramPhaseEquiv_refl _⟩⟩

/-- Auxiliary, and **not a definition**: reindexing a square matrix by one equivalence on both sides
commutes with the conjugate transpose. -/
theorem submatrix_conjTranspose_equiv {m : Type} [Fintype m] [DecidableEq m]
    (M : Matrix m m ℂ) (e : m ≃ m) : (M.submatrix e e)ᴴ = Mᴴ.submatrix e e := by
  ext p q; simp [Matrix.conjTranspose_apply, Matrix.submatrix_apply]

/-- Auxiliary, and **not a definition**: reindexing a unitary by one equivalence on both sides
leaves it unitary, because the reindexing commutes with the conjugate transpose and with the
product, and carries the identity to the identity. -/
theorem submatrix_mem_unitaryGroup {m : Type} [Fintype m] [DecidableEq m]
    {M : Matrix m m ℂ} (hM : M ∈ Matrix.unitaryGroup m ℂ) (e : m ≃ m) :
    M.submatrix e e ∈ Matrix.unitaryGroup m ℂ := by
  have h1 : Mᴴ * M = 1 := by
    have h := Matrix.mem_unitaryGroup_iff'.1 hM
    rwa [Matrix.star_eq_conjTranspose] at h
  rw [Matrix.mem_unitaryGroup_iff', Matrix.star_eq_conjTranspose,
    submatrix_conjTranspose_equiv, Matrix.submatrix_mul_equiv, h1, Matrix.submatrix_one_equiv]

theorem ol3_phiP_survives_through_l4 :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (P : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (G₀ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      (∀ t i j, Γ t i j = 1 / 4) ∧ (∀ t, Γ t = Γ 0)
        ∧ (∀ (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4),
            P G i = (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix
              (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3))
        ∧ RealizableGram (Fin 1) (Γ 0) G₀
        ∧ ¬ GramPhaseEquiv (P G₀) G₀
        ∧ TransitionLaw (fun _ => P) (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)))
        ∧ ProperAt (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)))
        ∧ PropagatesFrom (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)))
        ∧ EvolvesTotally (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)))
        ∧ PreservesAdmissible (0 : Fin 1) Γ (fun _ => P)
        ∧ (∀ Phih, (∀ t : ℕ, (fun _ => P) t = Phih) →
            ∀ (t s : ℕ) (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
              RealizableGram (Fin 1) (Γ 0) G →
                GramPhaseEquiv (Phih^[t + s] G) (Phih^[s] (Phih^[t] G)))
        ∧ (∀ Phih, (∀ t : ℕ, (fun _ => P) t = Phih) → Reversible (0 : Fin 1) (Γ 0) Phih)
        ∧ (∃ Ψ : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
              Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
            (∀ (t : ℕ) (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
                AdmissibleDilationAt (Γ t) (0 : Fin 1) U →
                (fun _ => P) t (FibreGram (0 : Fin 1) U) = FibreGram (0 : Fin 1) (Ψ t U))
              ∧ (∀ (t : ℕ) (L U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ), LeftFibreGroup L →
                  ∃ L', LeftFibreGroup L' ∧ Ψ t (L * U) = L' * Ψ t U)
              ∧ ∀ (t : ℕ) (U K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
                  WeakAnchorStabilizer (0 : Fin 1) K →
                  ∃ K', WeakAnchorStabilizer (0 : Fin 1) K' ∧ Ψ t (U * K) = Ψ t U * K')
        ∧ (∀ G G', GramPhaseEquiv (P G) (P G') → GramPhaseEquiv G G')
        ∧ (∀ X, RealizableGram (Fin 1) (Γ 0) X →
            ∀ t, RealizableGram (Fin 1) (Γ 0) (P^[t] X)) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hσσ : ∀ i : Fin 4, Equiv.swap (2 : Fin 4) 3 (Equiv.swap (2 : Fin 4) 3 i) = i :=
    fun i => Equiv.swap_apply_self 2 3 i
  have hinvol : ∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      (fun i : Fin 4 => (((fun (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4) =>
          (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix (Equiv.swap (2 : Fin 4) 3)
            (Equiv.swap (2 : Fin 4) 3)) G) (Equiv.swap (2 : Fin 4) 3 i)).submatrix
              (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = G := by
    intro G; funext i; ext j k; simp only [Matrix.submatrix_apply, hσσ]
  have hdesc : ∀ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, GramPhaseEquiv G G' →
      GramPhaseEquiv (fun i => (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix
          (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3))
        (fun i => (G' (Equiv.swap (2 : Fin 4) 3 i)).submatrix
          (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
    rintro G G' ⟨c, hc, h⟩
    exact ⟨fun j => c (Equiv.swap (2 : Fin 4) 3 j), fun j => hc _, fun i j k => by
      simp only [Matrix.submatrix_apply]; exact h _ _ _⟩
  have hreal : ∀ G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) Γ₀ G →
      RealizableGram (Fin 1) Γ₀ (fun i => (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix
        (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) := by
    intro G hG
    refine ⟨fun i => (hG.1 _).submatrix _, fun i => ?_, ?_, fun i j => ?_⟩
    · rw [Matrix.rank_submatrix]; exact hG.2.1 _
    · ext j k
      rw [Matrix.sum_apply]
      have hs : (∑ i : Fin 4, G (Equiv.swap (2 : Fin 4) 3 i)
            (Equiv.swap (2 : Fin 4) 3 j) (Equiv.swap (2 : Fin 4) 3 k))
          = (1 : Matrix (Fin 4) (Fin 4) ℂ)
              (Equiv.swap (2 : Fin 4) 3 j) (Equiv.swap (2 : Fin 4) 3 k) := by
        rw [Equiv.sum_comp (Equiv.swap (2 : Fin 4) 3)
          (fun i => G i (Equiv.swap (2 : Fin 4) 3 j) (Equiv.swap (2 : Fin 4) 3 k)),
          ← Matrix.sum_apply, hG.2.2.1]
      simp only [Matrix.submatrix_apply]
      rw [hs]
      by_cases hjk : j = k
      · subst hjk; simp
      · rw [Matrix.one_apply_ne
          (fun h => hjk ((Equiv.swap (2 : Fin 4) 3).injective h)), Matrix.one_apply_ne hjk]
    · simp only [Matrix.submatrix_apply]
      rw [hG.2.2.2 _ _, hΓ₀]
      simp
  obtain ⟨hTL, hL0, hL1, hL2, hL3, horb, hPI⟩ :=
    ladder_of_involutive_transition (Γ₀ := Γ₀) (0 : Fin 1)
      (fun (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4) =>
        (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix (Equiv.swap (2 : Fin 4) 3)
          (Equiv.swap (2 : Fin 4) 3))
      hdesc hreal hinvol
  refine ⟨fun _ => Γ₀,
    fun (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4) =>
      (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix (Equiv.swap (2 : Fin 4) 3)
        (Equiv.swap (2 : Fin 4) 3),
    FibreGram (0 : Fin 1) Hᵢ,
    fun _ i j => by rw [hΓ₀]; rfl, fun _ => rfl, fun G i => rfl, sh1_necessity hadmᵢ, ?_,
    hTL, ?_, ?_, hL0, hL1, hL2, hL3, ?_, hPI, horb⟩
  · -- the transition MOVES the class of `H(i)`
    intro h
    have hinv := gramPhaseEquiv_cross_invariant h 0 2
    have hs0 : Equiv.swap (2 : Fin 4) 3 0 = 0 := by decide
    have hs2 : Equiv.swap (2 : Fin 4) 3 2 = 3 := by decide
    simp only [Matrix.submatrix_apply, hs0, hs2] at hinv
    rw [fibreGram_apply, fibreGram_apply, fibreGram_apply, fibreGram_apply,
      Fin.sum_univ_one, Fin.sum_univ_one, Fin.sum_univ_one, Fin.sum_univ_one, hHᵢ] at hinv
    norm_num [Matrix.of_apply, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons, Complex.ext_iff] at hinv
  · -- ProperAt
    refine ⟨fun t => _^[t] (FibreGram (0 : Fin 1) H₁), fun t => _^[t] (FibreGram (0 : Fin 1) Hᵢ),
      fun t => if t = 0 then FibreGram (0 : Fin 1) H₁
        else (fun i => ((FibreGram (0 : Fin 1) Hᵢ) (Equiv.swap (2 : Fin 4) 3 i)).submatrix
          (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)),
      horb _ (sh1_necessity hadm₁), horb _ (sh1_necessity hadmᵢ), fun t => ?_, fun t => ?_,
      fun t => ?_, fun h => hnotG ?_, fun h => ?_⟩
    · by_cases ht : t = 0
      · simp only [if_pos ht]; exact sh1_necessity hadm₁
      · simp only [if_neg ht]; exact hreal _ (sh1_necessity hadmᵢ)
    · show GramPhaseEquiv (_^[t + 1] _) _
      rw [Function.iterate_succ_apply']
      exact gramPhaseEquiv_refl _
    · show GramPhaseEquiv (_^[t + 1] _) _
      rw [Function.iterate_succ_apply']
      exact gramPhaseEquiv_refl _
    · simpa using h 0
    · have hh := h 0
      simp only [if_pos rfl, if_neg (by decide : ¬ ((0 : ℕ) + 1 = 0))] at hh
      exact hnotG (gramPhaseEquiv_symm (hPI _ _ hh))
  · -- PropagatesFrom
    obtain ⟨_, _, _, hiter, hsolve⟩ :=
      ol1b_monoid_action (a₀ := (0 : Fin 1)) (Γ := fun _ => Γ₀) (Γ₀ := Γ₀)
        (Phih := fun (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4) =>
          (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix (Equiv.swap (2 : Fin 4) 3)
            (Equiv.swap (2 : Fin 4) 3))
        hTL (fun _ => rfl) (fun _ => rfl)
    refine ⟨fun G₁ G₂ _ _ h₁ h₂ h0 t =>
      gramPhaseEquiv_trans (hsolve G₁ h₁ t)
        (gramPhaseEquiv_trans (hiter t _ _ h0) (gramPhaseEquiv_symm (hsolve G₂ h₂ t))),
      1, fun t => _^[t] (FibreGram (0 : Fin 1) H₁), fun t => _^[t] (FibreGram (0 : Fin 1) Hᵢ),
      le_refl 1, horb _ (sh1_necessity hadm₁), horb _ (sh1_necessity hadmᵢ), fun t => ?_,
      fun t => ?_, fun h => hnotG (hPI _ _ ?_)⟩
    · show GramPhaseEquiv (_^[t + 1] _) _
      rw [Function.iterate_succ_apply']
      exact gramPhaseEquiv_refl _
    · show GramPhaseEquiv (_^[t + 1] _) _
      rw [Function.iterate_succ_apply']
      exact gramPhaseEquiv_refl _
    · simpa using h
  · -- L4n
    refine ⟨fun _ U => U.submatrix
        ((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1)))
        ((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1))), ?_, ?_, ?_⟩
    · intro t U _
      funext i
      ext j k
      simp only [Matrix.submatrix_apply, fibreGram_apply, Equiv.prodCongr_apply,
        Equiv.coe_refl, Prod.map_apply, id_eq]
    · intro t L U hL
      refine ⟨L.submatrix ((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1)))
          ((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1))),
        ⟨submatrix_mem_unitaryGroup hL.1 _, fun p q hpq => ?_⟩, ?_⟩
      · refine hL.2 _ _ ?_
        simp only [Equiv.prodCongr_apply, Equiv.coe_refl, Prod.map_apply, id_eq]
        exact fun hc => hpq ((Equiv.swap (2 : Fin 4) 3).injective hc)
      · rw [Matrix.submatrix_mul_equiv]
    · intro t U K hK
      obtain ⟨hKu, c, hc⟩ := hK
      refine ⟨K.submatrix ((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1)))
          ((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1))),
        ⟨submatrix_mem_unitaryGroup hKu _, fun j => c (Equiv.swap (2 : Fin 4) 3 j),
          fun p j => ?_⟩, ?_⟩
      · have hiff : (((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1))) p
              = ((Equiv.swap (2 : Fin 4) 3 j), (0 : Fin 1))) ↔ p = (j, (0 : Fin 1)) := by
          constructor
          · intro hcon
            have h1 : Equiv.swap (2 : Fin 4) 3 p.1 = Equiv.swap (2 : Fin 4) 3 j :=
              congrArg Prod.fst hcon
            have h2 : p.2 = (0 : Fin 1) := congrArg Prod.snd hcon
            exact Prod.ext ((Equiv.swap (2 : Fin 4) 3).injective h1) h2
          · intro hcon; subst hcon; rfl
        have hep : (((Equiv.swap (2 : Fin 4) 3).prodCongr (Equiv.refl (Fin 1)))
            ((j : Fin 4), (0 : Fin 1))) = ((Equiv.swap (2 : Fin 4) 3 j), (0 : Fin 1)) := rfl
        rw [Matrix.submatrix_apply, hep, hc]
        simp only [hiff]
      · rw [Matrix.submatrix_mul_equiv]

/-- Auxiliary, and **not a definition**: at a time-homogeneous configuration, a transition family
that preserves pointwise realizability satisfies **`L0`**. The witness is the orbit of the given
class through the family, admissible at every time by induction and a solution by construction.

**This is used only to discharge `L0` for named candidates**; it is not a rung verdict, and no
`Li-FREE` is claimed from it. `L0`'s own rung verdict is reported from the exhibited
countercontrol. -/
theorem evolvesTotally_of_preservesAdmissible {Γ₀ : Matrix V V ℝ} (a₀ : A)
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (hpres : ∀ t G, RealizableGram A Γ₀ G → RealizableGram A Γ₀ (Φ t G)) :
    EvolvesTotally a₀ (fun _ => Γ₀) (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) := by
  intro G₀ hG₀
  refine ⟨fun t => Nat.rec (motive := fun _ => V → Matrix V V ℂ) G₀ (fun n ih => Φ n ih) t,
    ?_, fun t => gramPhaseEquiv_refl _, gramPhaseEquiv_refl _⟩
  intro t
  induction t with
  | zero => exact hG₀
  | succ n ih => exact hpres n _ ih

/-- Auxiliary, and **not a definition**: act 18's propagation clause (i) holds for the law a
descending transition family generates. Two pointwise realizable solutions whose classes agree at
time `0` agree at every time, by induction along the transition.

**This is clause (i) alone.** Act 18's clause (ii) — that the initial orbit contributes — is a
separate demand, is not supplied here, and is reported separately wherever it is at issue. The two
non-propagation mechanisms stay apart and named. -/
theorem propagates_uniqueness (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (hdesc : ∀ (t : ℕ) (G G' : V → Matrix V V ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (Φ t G) (Φ t G'))
    (G₁ G₂ : ℕ → V → Matrix V V ℂ)
    (h₁ : ∀ t, GramPhaseEquiv (G₁ (t + 1)) (Φ t (G₁ t)))
    (h₂ : ∀ t, GramPhaseEquiv (G₂ (t + 1)) (Φ t (G₂ t)))
    (h0 : GramPhaseEquiv (G₁ 0) (G₂ 0)) : GramTrajEquiv G₁ G₂ := by
  intro t
  induction t with
  | zero => exact h0
  | succ n ih =>
      exact gramPhaseEquiv_trans (h₁ n)
        (gramPhaseEquiv_trans (hdesc n _ _ ih) (gramPhaseEquiv_symm (h₂ n)))

/-- Auxiliary, and **not a definition**: act 12's merged Hadamard objects together with the
carrier-relabelling transition of this round's `ΦP`, and the four facts about it the census uses —
that it descends, that it preserves pointwise realizability, that it is an involution, and that it
**moves** the admissible class of act 12's `H(i)`.

The last is certified through act 12's merged `∼_D`-invariant read at the fibre pair `(0,2)`, whose
values are `1/16` on that class and `i/16` on its image. **One merged witness family, several
consequences**: act 12's own exhibited Hadamard pair is consumed at its own existential strength and
is neither enlarged nor re-proved, and what this round draws from it is reported as consequences of
one witness and never as several independent findings. -/
theorem relabelling_transition_data :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ Hᵢ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ)
      (P : (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)),
      (∀ i j, Γ₀ i j = 1 / 4)
        ∧ (∀ (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4),
            P G i = (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix (Equiv.swap (2 : Fin 4) 3)
              (Equiv.swap (2 : Fin 4) 3))
        ∧ AdmissibleDilationAt Γ₀ (0 : Fin 1) H₁ ∧ AdmissibleDilationAt Γ₀ (0 : Fin 1) Hᵢ
        ∧ ¬ GramPhaseEquiv (FibreGram (0 : Fin 1) H₁) (FibreGram (0 : Fin 1) Hᵢ)
        ∧ (∀ G G', GramPhaseEquiv G G' → GramPhaseEquiv (P G) (P G'))
        ∧ (∀ G, RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (P G))
        ∧ (∀ G, P (P G) = G)
        ∧ ¬ GramPhaseEquiv (P (FibreGram (0 : Fin 1) Hᵢ)) (FibreGram (0 : Fin 1) Hᵢ) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hσσ : ∀ i : Fin 4, Equiv.swap (2 : Fin 4) 3 (Equiv.swap (2 : Fin 4) 3 i) = i :=
    fun i => Equiv.swap_apply_self 2 3 i
  refine ⟨Γ₀, H₁, Hᵢ,
    fun (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4) =>
      (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix (Equiv.swap (2 : Fin 4) 3)
        (Equiv.swap (2 : Fin 4) 3),
    fun i j => by rw [hΓ₀]; rfl, fun G i => rfl, hadm₁, hadmᵢ, hnotG, ?_, ?_, ?_, ?_⟩
  · rintro G G' ⟨c, hc, h⟩
    exact ⟨fun j => c (Equiv.swap (2 : Fin 4) 3 j), fun j => hc _, fun i j k => by
      simp only [Matrix.submatrix_apply]; exact h _ _ _⟩
  · intro G hG
    refine ⟨fun i => (hG.1 _).submatrix _, fun i => ?_, ?_, fun i j => ?_⟩
    · rw [Matrix.rank_submatrix]; exact hG.2.1 _
    · ext j k
      rw [Matrix.sum_apply]
      have hs : (∑ i : Fin 4, G (Equiv.swap (2 : Fin 4) 3 i)
            (Equiv.swap (2 : Fin 4) 3 j) (Equiv.swap (2 : Fin 4) 3 k))
          = (1 : Matrix (Fin 4) (Fin 4) ℂ)
              (Equiv.swap (2 : Fin 4) 3 j) (Equiv.swap (2 : Fin 4) 3 k) := by
        rw [Equiv.sum_comp (Equiv.swap (2 : Fin 4) 3)
          (fun i => G i (Equiv.swap (2 : Fin 4) 3 j) (Equiv.swap (2 : Fin 4) 3 k)),
          ← Matrix.sum_apply, hG.2.2.1]
      simp only [Matrix.submatrix_apply]
      rw [hs]
      by_cases hjk : j = k
      · subst hjk; simp
      · rw [Matrix.one_apply_ne
          (fun h => hjk ((Equiv.swap (2 : Fin 4) 3).injective h)), Matrix.one_apply_ne hjk]
    · simp only [Matrix.submatrix_apply]
      rw [hG.2.2.2 _ _, hΓ₀]
      simp
  · intro G; funext i; ext j k; simp only [Matrix.submatrix_apply, hσσ]
  · intro h
    have hinv := gramPhaseEquiv_cross_invariant h 0 2
    have hs0 : Equiv.swap (2 : Fin 4) 3 0 = 0 := by decide
    have hs2 : Equiv.swap (2 : Fin 4) 3 2 = 3 := by decide
    simp only [Matrix.submatrix_apply, hs0, hs2] at hinv
    rw [fibreGram_apply, fibreGram_apply, fibreGram_apply, fibreGram_apply,
      Fin.sum_univ_one, Fin.sum_univ_one, Fin.sum_univ_one, Fin.sum_univ_one, hHᵢ] at hinv
    norm_num [Matrix.of_apply, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons, Complex.ext_iff] at hinv


/-- Auxiliary, and **not a definition**: the orbit of an admissible class through a transition
family, pinned by its two defining equations, with admissibility at every time. -/
theorem orbit_of_family {Γ₀ : Matrix V V ℝ}
    (Φ : ℕ → (V → Matrix V V ℂ) → (V → Matrix V V ℂ))
    (hpres : ∀ t G, RealizableGram A Γ₀ G → RealizableGram A Γ₀ (Φ t G))
    (X : V → Matrix V V ℂ) (hX : RealizableGram A Γ₀ X) :
    ∃ 𝔾 : ℕ → V → Matrix V V ℂ, 𝔾 0 = X ∧ (∀ t, 𝔾 (t + 1) = Φ t (𝔾 t))
      ∧ ∀ t, RealizableGram A Γ₀ (𝔾 t) := by
  refine ⟨fun t => Nat.rec (motive := fun _ => V → Matrix V V ℂ) X (fun n ih => Φ n ih) t,
    rfl, fun t => rfl, ?_⟩
  intro t
  induction t with
  | zero => exact hX
  | succ n ih => exact hpres n _ ih

/-- **`OL3`, `ΦT` — THE TIME-INHOMOGENEOUS ALTERNATION FAILS `L2`**, at the configuration this
freeze names for it: `V = Fin 4`, `A = Fin 1`, anchor `0`, `Γ ≡ ¼`, with `σ` the transposition act
18's fourth admissible dilation exhibits.

`ΦT` applies the identity transition at even times and the relabelling at odd times. It is the least
contrived failure of one law iterating consistently: two perfectly good transitions, applied in
alternation. It satisfies every earlier rung — it descends, it is an `L-PROP` law in act 18's frozen
sense with **both** propagation clauses, it is total and it preserves pointwise admissibility — and
**no single transition equals it at every time**, which is `L2`'s first conjunct failing. The
separation is act 18's already-exhibited class inequivalence, read at `t = 0` against `t = 1`: were
one transition to serve at both, the identity and the relabelling would agree, and they disagree at
the admissible class of act 12's `H(i)`.

**So `L2` is a genuine restriction on the class the shared theorem produces and is not decoration.**
This is a statement about the exact condition frozen under the label `L2`, at the configuration
named, and it does **not** endorse the condition, does **not** say the programme requires it, and
does **not** say it is the right condition to impose. It settles this family against this rung and
nothing in its neighbourhood, and it is **not** a statement that families of its shape fail in
general. -/
theorem ol3_phiT_fails_l2 :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ)),
      (∀ t i j, Γ t i j = 1 / 4) ∧ (∀ t, Γ t = Γ 0)
        ∧ Φ 0 = (fun G => G)
        ∧ (∀ (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) (i : Fin 4),
            Φ 1 G i = (G (Equiv.swap (2 : Fin 4) 3 i)).submatrix (Equiv.swap (2 : Fin 4) 3)
              (Equiv.swap (2 : Fin 4) 3))
        ∧ TransitionLaw Φ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
        ∧ ProperAt (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
        ∧ PropagatesFrom (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
        ∧ EvolvesTotally (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
        ∧ PreservesAdmissible (0 : Fin 1) Γ Φ
        ∧ ¬ (∃ Phih, ∀ t, Φ t = Phih) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, P, hΓ₀, hPdef, hadm₁, hadmᵢ, hnotG, hdescP, hrealP, hinvolP, hmove⟩ :=
    relabelling_transition_data
  set T : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) :=
    fun t => if t % 2 = 0 then (fun G => G) else P with hT
  have hT0 : T 0 = fun G => G := by rw [hT]; norm_num
  have hT1 : T 1 = P := by rw [hT]; norm_num
  have hdescT : ∀ (t : ℕ) (G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      GramPhaseEquiv G G' → GramPhaseEquiv (T t G) (T t G') := by
    intro t G G' h
    rw [hT]
    by_cases ht : t % 2 = 0
    · simp only [if_pos ht]; exact h
    · simp only [if_neg ht]; exact hdescP G G' h
  have hpresT : ∀ (t : ℕ) (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      RealizableGram (Fin 1) Γ₀ G → RealizableGram (Fin 1) Γ₀ (T t G) := by
    intro t G hG
    rw [hT]
    by_cases ht : t % 2 = 0
    · simp only [if_pos ht]; exact hG
    · simp only [if_neg ht]; exact hrealP G hG
  obtain ⟨𝔾₁, h10, h1s, h1r⟩ := orbit_of_family T hpresT _ (sh1_necessity hadm₁)
  obtain ⟨𝔾₂, h20, h2s, h2r⟩ := orbit_of_family T hpresT _ (sh1_necessity hadmᵢ)
  have hLaw1 : ∀ t, GramPhaseEquiv (𝔾₁ (t + 1)) (T t (𝔾₁ t)) := fun t => by
    rw [h1s t]; exact gramPhaseEquiv_refl _
  have hLaw2 : ∀ t, GramPhaseEquiv (𝔾₂ (t + 1)) (T t (𝔾₂ t)) := fun t => by
    rw [h2s t]; exact gramPhaseEquiv_refl _
  have hsep1 : ¬ GramPhaseEquiv (𝔾₁ 1) (𝔾₂ 1) := by
    rw [h1s 0, h2s 0, h10, h20, hT0]
    exact hnotG
  refine ⟨fun _ => Γ₀, T, fun _ i j => hΓ₀ i j, fun _ => rfl, hT0, fun G i => by
      rw [hT1]; exact hPdef G i,
    ⟨hdescT, fun _ => Iff.rfl⟩, ?_, ?_,
    evolvesTotally_of_preservesAdmissible (0 : Fin 1) T hpresT, fun t G hG => hpresT t G hG, ?_⟩
  · refine ⟨𝔾₁, 𝔾₂, fun t => if t = 0 then FibreGram (0 : Fin 1) H₁
      else FibreGram (0 : Fin 1) Hᵢ, h1r, h2r, fun t => ?_, hLaw1, hLaw2,
      fun h => hnotG ?_, fun h => hnotG ?_⟩
    · by_cases ht : t = 0
      · simp only [if_pos ht]; exact sh1_necessity hadm₁
      · simp only [if_neg ht]; exact sh1_necessity hadmᵢ
    · have h0 := h 0
      rw [h10, h20] at h0
      exact h0
    · have hh := h 0
      simp only [if_pos rfl, if_neg (by decide : ¬ ((0 : ℕ) + 1 = 0)), hT0] at hh
      exact gramPhaseEquiv_symm hh
  · exact ⟨fun G₁ G₂ _ _ k₁ k₂ h0 => propagates_uniqueness T hdescT G₁ G₂ k₁ k₂ h0,
      1, 𝔾₁, 𝔾₂, le_refl 1, h1r, h2r, hLaw1, hLaw2, hsep1⟩
  · rintro ⟨Phih, h⟩
    have he : (fun G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => G) = P := by
      rw [← hT0, ← hT1, h 0, h 1]
    exact hmove (by rw [← he]; exact gramPhaseEquiv_refl _)


/-- **`OL3`, `ΦC` — THE CONSTANT TRANSITION FAILS BOTH CONJUNCTS OF `L3`, AND ALSO FAILS ACT 18's
PROPAGATION CLAUSE (ii)**, at the configuration this freeze names for it.

`ΦC` sends every state to one named admissible class. It is the crudest evolution that is still an
evolution. It descends — the image being a single class, descent is immediate — it is total, it
preserves pointwise admissibility, it is time-homogeneous and its induced evolution composes; it is
proper at the configuration; and act 18's propagation clause (i) holds for it. **Both conjuncts of
`L3` fail**: two `∼_D`-inequivalent admissible classes, those of act 12's `H(1)` and `H(i)`, have
the same image, so injectivity on classes fails; and the image is the single class of `H(1)`, while
the class of `H(i)` is admissible and outside it, so surjectivity fails.

**The last conjunct is recorded because the freeze's standing hypothesis makes it load-bearing, and
it is reported rather than repaired.** Act 18's propagation carries two clauses, and clause (ii)
asks that the initial orbit **contribute**. Every solution of `ΦC`'s law sits at the one named class
from time `1` onward, so no two solutions are inequivalent at any time after the initial one, and
clause (ii) **fails**. Act 18 named that mechanism and kept it apart from the other: it is the
outcome in which the initial orbit does no work. Since this freeze's ladder carries act 18's
`PropagatesFrom` as a standing hypothesis and says that a candidate which is not an `L-PROP` law is
not on the ladder at all, **`ΦC` is exhibited in full and its rung status is reported conservatively
in the result note**, with the tension between the freeze's countercontrol table and the freeze's
own standing hypothesis recorded as a discrepancy and not repaired.

This settles this family against these rungs and nothing in its neighbourhood. **A failure of `ΦC`
at `L3i` is not a refutation of irreversible evolutions in general.** -/
theorem ol3_phiC_fails_l3 :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (Φ : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (G₀ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      (∀ t i j, Γ t i j = 1 / 4) ∧ (∀ t, Γ t = Γ 0)
        ∧ Φ = (fun _ _ => G₀)
        ∧ RealizableGram (Fin 1) (Γ 0) G₀
        ∧ TransitionLaw Φ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
        ∧ ProperAt (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
        ∧ EvolvesTotally (0 : Fin 1) Γ (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t)))
        ∧ PreservesAdmissible (0 : Fin 1) Γ Φ
        ∧ (∃ Phih, ∀ t, Φ t = Phih)
        ∧ (∀ Phih, (∀ t, Φ t = Phih) → ∀ (t s : ℕ) (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
            RealizableGram (Fin 1) (Γ 0) G →
              GramPhaseEquiv (Phih^[t + s] G) (Phih^[s] (Phih^[t] G)))
        ∧ (∀ G₁ G₂ : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
            (∀ t, GramPhaseEquiv (G₁ (t + 1)) (Φ t (G₁ t))) →
            (∀ t, GramPhaseEquiv (G₂ (t + 1)) (Φ t (G₂ t))) →
            GramPhaseEquiv (G₁ 0) (G₂ 0) → GramTrajEquiv G₁ G₂)
        ∧ (∀ Phih, (∀ t, Φ t = Phih) → ¬ Reversible (0 : Fin 1) (Γ 0) Phih)
        ∧ (∃ G G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
            RealizableGram (Fin 1) (Γ 0) G ∧ RealizableGram (Fin 1) (Γ 0) G'
              ∧ GramPhaseEquiv (Φ 0 G) (Φ 0 G') ∧ ¬ GramPhaseEquiv G G')
        ∧ (∃ G' : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ, RealizableGram (Fin 1) (Γ 0) G'
            ∧ ∀ G, RealizableGram (Fin 1) (Γ 0) G → ¬ GramPhaseEquiv (Φ 0 G) G')
        ∧ ¬ PropagatesFrom (0 : Fin 1) Γ
            (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (Φ t (𝔾 t))) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hr₁ : RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) H₁) := sh1_necessity hadm₁
  have hrᵢ : RealizableGram (Fin 1) Γ₀ (FibreGram (0 : Fin 1) Hᵢ) := sh1_necessity hadmᵢ
  refine ⟨fun _ => Γ₀, fun _ _ => FibreGram (0 : Fin 1) H₁, FibreGram (0 : Fin 1) H₁,
    fun _ i j => by rw [hΓ₀]; rfl, fun _ => rfl, rfl, hr₁,
    ⟨fun _ _ _ _ => gramPhaseEquiv_refl _, fun _ => Iff.rfl⟩, ?_,
    evolvesTotally_of_preservesAdmissible (0 : Fin 1) _ (fun _ _ _ => hr₁),
    fun _ _ _ => hr₁, ⟨fun _ => FibreGram (0 : Fin 1) H₁, fun _ => rfl⟩, ?_,
    fun G₁ G₂ k₁ k₂ h0 =>
      propagates_uniqueness (fun _ _ => FibreGram (0 : Fin 1) H₁)
        (fun _ _ _ _ => gramPhaseEquiv_refl _) G₁ G₂ k₁ k₂ h0,
    ?_, ⟨FibreGram (0 : Fin 1) H₁, FibreGram (0 : Fin 1) Hᵢ, hr₁, hrᵢ,
      gramPhaseEquiv_refl _, hnotG⟩,
    ⟨FibreGram (0 : Fin 1) Hᵢ, hrᵢ, fun G _ => hnotG⟩, ?_⟩
  · refine ⟨fun _ => FibreGram (0 : Fin 1) H₁,
      fun t => if t = 0 then FibreGram (0 : Fin 1) Hᵢ else FibreGram (0 : Fin 1) H₁,
      fun t => if t = 0 then FibreGram (0 : Fin 1) H₁ else FibreGram (0 : Fin 1) Hᵢ,
      fun _ => hr₁, fun t => ?_, fun t => ?_, fun _ => gramPhaseEquiv_refl _, fun t => ?_,
      fun h => hnotG ?_, fun h => hnotG ?_⟩
    · by_cases ht : t = 0
      · simp only [if_pos ht]; exact hrᵢ
      · simp only [if_neg ht]; exact hr₁
    · by_cases ht : t = 0
      · simp only [if_pos ht]; exact hr₁
      · simp only [if_neg ht]; exact hrᵢ
    · simp only [if_neg (by omega : ¬ (t + 1 = 0))]
      exact gramPhaseEquiv_refl _
    · have h0 := h 0
      simp only [if_pos rfl] at h0
      exact h0
    · have hh := h 0
      simp only [if_pos rfl, if_neg (by decide : ¬ ((0 : ℕ) + 1 = 0))] at hh
      exact gramPhaseEquiv_symm hh
  · intro Phih hPhih t s G _
    rw [add_comm t s, Function.iterate_add_apply]
    exact gramPhaseEquiv_refl _
  · intro Phih hPhih hrev
    have hp : (fun _ : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => FibreGram (0 : Fin 1) H₁) = Phih :=
      hPhih 0
    exact hnotG (hrev.1 _ _ hr₁ hrᵢ (by rw [← hp]; exact gramPhaseEquiv_refl _))
  · rintro ⟨-, t, G₁, G₂, ht, -, -, k₁, k₂, hne⟩
    obtain ⟨s, rfl⟩ : ∃ s, t = s + 1 := ⟨t - 1, by omega⟩
    exact hne (gramPhaseEquiv_trans (k₁ s) (gramPhaseEquiv_symm (k₂ s)))

/-- **`OL3`, `ΦX` — THE RESTRICTED-INITIAL LAW FAILS `L0`**, at the configuration this freeze names
for it: `V = Fin 4`, `A = Fin 1`, anchor `0`, `Γ ≡ ¼`.

`ΦX` is act 18's `LC0` law datum — the two-class pointwise condition — conjoined with a genuinely
cross-time constancy requirement, so the law admits a trajectory iff its orbit class is constant in
time **and** its initial class is one of two named ones. **It is not pointwise**, so act 18's `XS1`
says nothing about it in either direction.

It is an `L-PROP` law in act 18's frozen sense: nonempty and non-singleton modulo act 17's
trajectory equivalence, proper against the constant trajectory at the class of act 12's `H(−1)`,
with clause (i) holding because a solution's class is constant and pinned by its initial class, and
with clause (ii) holding at `t = 1`, where two solutions from the two named initial classes sit at
`∼_D`-inequivalent classes. **And `L0` fails**: the class of `H(−1)` is admissible, by act 12's
merged `sh1_necessity` applied to the third member of act 12's own frozen family, and it is
`∼_D`-inequivalent to both named classes, so it extends to no solution at all. The law is an
evolution of part of the admissible orbit state space and not of the space.

**So `L0` is a genuine restriction on the class the shared theorem produces and is not decoration.**
This is a statement about the exact condition frozen under the label `L0`, at the configuration
named, and it does **not** endorse the condition, does **not** say the programme requires it, and
does **not** say it is the right condition to impose. -/
theorem ol3_phiX_fails_l0 :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (G₁ Gᵢ Gneg : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
      (∀ t i j, Γ t i j = 1 / 4) ∧ (∀ t, Γ t = Γ 0)
        ∧ RealizableGram (Fin 1) (Γ 0) G₁ ∧ RealizableGram (Fin 1) (Γ 0) Gᵢ
        ∧ RealizableGram (Fin 1) (Γ 0) Gneg
        ∧ ¬ GramPhaseEquiv G₁ Gᵢ
        ∧ ¬ GramPhaseEquiv Gneg G₁ ∧ ¬ GramPhaseEquiv Gneg Gᵢ
        ∧ ProperAt (0 : Fin 1) Γ (fun 𝔾 => (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t))
            ∧ (GramPhaseEquiv (𝔾 0) G₁ ∨ GramPhaseEquiv (𝔾 0) Gᵢ))
        ∧ PropagatesFrom (0 : Fin 1) Γ (fun 𝔾 => (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t))
            ∧ (GramPhaseEquiv (𝔾 0) G₁ ∨ GramPhaseEquiv (𝔾 0) Gᵢ))
        ∧ ¬ EvolvesTotally (0 : Fin 1) Γ (fun 𝔾 => (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t))
            ∧ (GramPhaseEquiv (𝔾 0) G₁ ∨ GramPhaseEquiv (𝔾 0) Gᵢ)) := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  have hunit : (Matrix.of (fun p q : Fin 4 × Fin 1 =>
      (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1))
      ∈ Matrix.unitaryGroup (Fin 4 × Fin 1) ℂ := by
    rw [Matrix.mem_unitaryGroup_iff, Matrix.star_eq_conjTranspose]
    ext p q
    obtain ⟨x, y⟩ := p
    obtain ⟨u, v⟩ := q
    fin_cases x <;> fin_cases y <;> fin_cases u <;> fin_cases v <;>
      simp [Matrix.mul_apply, Fintype.sum_prod_type, Fin.sum_univ_four,
        Matrix.conjTranspose_apply] <;> norm_num [Complex.ext_iff]
  have hadmNeg : AdmissibleDilationAt Γ₀ (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)) := by
    refine ⟨hunit, fun i j => ?_⟩
    rw [hΓ₀]
    fin_cases i <;> fin_cases j <;> simp <;> norm_num
  have hne₁ : ¬ GramPhaseEquiv (FibreGram (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)))
      (FibreGram (0 : Fin 1) H₁) := by
    intro hG
    have hinv := gramPhaseEquiv_cross_invariant hG 0 1
    rw [hH₁] at hinv
    simp [fibreGram_apply] at hinv
    norm_num [Complex.ext_iff] at hinv
  have hneᵢ : ¬ GramPhaseEquiv (FibreGram (0 : Fin 1)
      (Matrix.of (fun p q : Fin 4 × Fin 1 =>
        (1 / 2 : ℂ) * !![1, 1, 1, 1; 1, -1, -1, 1; 1, -1, 1, -1; 1, 1, -1, -1] p.1 q.1)))
      (FibreGram (0 : Fin 1) Hᵢ) := by
    intro hG
    have hinv := gramPhaseEquiv_cross_invariant hG 0 1
    rw [hHᵢ] at hinv
    simp [fibreGram_apply] at hinv
    norm_num [Complex.ext_iff] at hinv
  have hconst : ∀ 𝔾 : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ,
      (∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t)) → ∀ t, GramPhaseEquiv (𝔾 t) (𝔾 0) := by
    intro 𝔾 h t
    induction t with
    | zero => exact gramPhaseEquiv_refl _
    | succ n ih => exact gramPhaseEquiv_trans (h n) ih
  refine ⟨fun _ => Γ₀, FibreGram (0 : Fin 1) H₁, FibreGram (0 : Fin 1) Hᵢ,
    FibreGram (0 : Fin 1) _, fun _ i j => by rw [hΓ₀]; rfl, fun _ => rfl,
    sh1_necessity hadm₁, sh1_necessity hadmᵢ, sh1_necessity hadmNeg, hnotG, hne₁, hneᵢ,
    ⟨fun _ => FibreGram (0 : Fin 1) H₁, fun _ => FibreGram (0 : Fin 1) Hᵢ,
      fun _ => FibreGram (0 : Fin 1) _,
      fun _ => sh1_necessity hadm₁, fun _ => sh1_necessity hadmᵢ,
      fun _ => sh1_necessity hadmNeg,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inl (gramPhaseEquiv_refl _)⟩,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inr (gramPhaseEquiv_refl _)⟩,
      fun h => hnotG (h 0), fun h => h.2.elim hne₁ hneᵢ⟩,
    ⟨fun G₁ G₂ _ _ k₁ k₂ h0 t =>
      gramPhaseEquiv_trans (hconst G₁ k₁.1 t)
        (gramPhaseEquiv_trans h0 (gramPhaseEquiv_symm (hconst G₂ k₂.1 t))),
      1, fun _ => FibreGram (0 : Fin 1) H₁, fun _ => FibreGram (0 : Fin 1) Hᵢ, le_refl 1,
      fun _ => sh1_necessity hadm₁, fun _ => sh1_necessity hadmᵢ,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inl (gramPhaseEquiv_refl _)⟩,
      ⟨fun _ => gramPhaseEquiv_refl _, Or.inr (gramPhaseEquiv_refl _)⟩, hnotG⟩, ?_⟩
  intro h
  obtain ⟨𝔾, _, hL, h0⟩ := h (FibreGram (0 : Fin 1) _) (sh1_necessity hadmNeg)
  exact hL.2.elim
    (fun hc => hne₁ (gramPhaseEquiv_trans (gramPhaseEquiv_symm h0) hc))
    (fun hc => hneᵢ (gramPhaseEquiv_trans (gramPhaseEquiv_symm h0) hc))


/-- **`OL4` — `SIOP-YES`: A SAME-INITIAL-ORBIT PAIR, EXHIBITED AT ITS FIRST DIVERGENCE, WITH
`t* = 1`.**

Two transition families satisfying every condition of this freeze's ladder from `L0` through `L4` —
the identity transition and the carrier relabelling, both certified survivors of the census — whose
laws are **not** equivalent under this round's frozen law equivalence, are handed the **same initial
orbit class**, that of act 12's `H(i)`, and their solutions **first diverge at `t* = 1`**.

**The earlier-agreement conjunct is part of the witness and is discharged, not assumed.** At
`t* = 1` it reduces to agreement at time `0`, which is the same-initial-orbit hypothesis itself: the
two laws are handed the same initial orbit and disagree at the very next step. **So what is
exhibited is primitive non-uniqueness and not a divergence propagated forward from an earlier one.**
The separating quantity is act 12's merged `∼_D`-invariant at the fibre pair `(0,2)`, whose values
are `1/16` and `i/16`.

**So rigidity is cleanly falsified at the configuration named.** This settles the exact ladder this
freeze fixes and is **not** a statement that no condition set yields rigidity, **not** a statement
about conditions this round does not test, and **not** a licence to add one.

The condition predicate the pair satisfies is named in the statement and is the conjunction `L0`
through `L4`; `L5` is reported UNDECIDED for the relabelling and the headline is computed over the
conditions the kernel actually discharges, exactly as this freeze's `L5` fallback prescribes. -/
theorem ol4_siop_yes :
    ∃ Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ,
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ SameInitialOrbitPair (0 : Fin 1) Γ
            (fun Φ Law => TransitionLaw Φ Law ∧ ProperAt (0 : Fin 1) Γ Law
              ∧ PropagatesFrom (0 : Fin 1) Γ Law ∧ EvolvesTotally (0 : Fin 1) Γ Law
              ∧ PreservesAdmissible (0 : Fin 1) Γ Φ
              ∧ (∃ Phih, ∀ t, Φ t = Phih)
              ∧ (∀ Phih, (∀ t, Φ t = Phih) → ∀ (t s : ℕ) (G : Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
                  RealizableGram (Fin 1) (Γ 0) G →
                    GramPhaseEquiv (Phih^[t + s] G) (Phih^[s] (Phih^[t] G)))
              ∧ (∀ Phih, (∀ t, Φ t = Phih) → Reversible (0 : Fin 1) (Γ 0) Phih)
              ∧ (∃ Ψ : ℕ → Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ →
                    Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ,
                  (∀ (t : ℕ) (U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
                      AdmissibleDilationAt (Γ t) (0 : Fin 1) U →
                      Φ t (FibreGram (0 : Fin 1) U) = FibreGram (0 : Fin 1) (Ψ t U))
                    ∧ (∀ (t : ℕ) (L U : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
                        LeftFibreGroup L → ∃ L', LeftFibreGroup L' ∧ Ψ t (L * U) = L' * Ψ t U)
                    ∧ ∀ (t : ℕ) (U K : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
                        WeakAnchorStabilizer (0 : Fin 1) K →
                        ∃ K', WeakAnchorStabilizer (0 : Fin 1) K' ∧ Ψ t (U * K) = Ψ t U * K'))
        ∧ (∃ (Law Law' : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop)
             (𝔾 𝔾' : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ),
            ¬ LawEquiv (0 : Fin 1) Γ Law Law'
              ∧ (∀ t, RealizableGram (Fin 1) (Γ t) (𝔾 t))
              ∧ (∀ t, RealizableGram (Fin 1) (Γ t) (𝔾' t))
              ∧ Law 𝔾 ∧ Law' 𝔾'
              ∧ GramPhaseEquiv (𝔾 0) (𝔾' 0)
              ∧ ¬ GramPhaseEquiv (𝔾 1) (𝔾' 1)) := by
  classical
  obtain ⟨ΓI, ΦI, LawI, hΓI, hΓIc, hΦI, hLawI, hLadderI⟩ := ol3_phiI_survives
  obtain ⟨ΓP, P, G₀, hΓP, hΓPc, hPdef, hG₀, hmove, hTLP, hproperP, hpropP, hL0P, hL1P, hL2P,
    hL3P, hL4nP, hPI, horbP⟩ := ol3_phiP_survives_through_l4
  have hΓeq : ΓI = ΓP := by
    funext t; ext i j; rw [hΓI t i j, hΓP t i j]
  subst hΓeq
  subst hΦI
  subst hLawI
  obtain ⟨hTLI, hproperI, hpropI, hL0I, hL1I, hhomI, hL2I, hL3I, hL4nI, _hL5I⟩ := hLadderI
  have hrealK : ∀ t, RealizableGram (Fin 1) (ΓI t) G₀ := fun t => by
    rw [hΓPc t]; exact hG₀
  have hrealO : ∀ t, RealizableGram (Fin 1) (ΓI t) (P^[t] G₀) := fun t => by
    rw [hΓPc t]; exact horbP G₀ hG₀ t
  have hsolI : ∀ t, GramPhaseEquiv ((fun _ : ℕ => G₀) (t + 1)) ((fun _ : ℕ => G₀) t) :=
    fun _ => gramPhaseEquiv_refl _
  have hsolP : ∀ t, GramPhaseEquiv ((fun t => P^[t] G₀) (t + 1)) (P ((fun t => P^[t] G₀) t)) := by
    intro t
    show GramPhaseEquiv (P^[t + 1] G₀) (P (P^[t] G₀))
    rw [Function.iterate_succ_apply']
    exact gramPhaseEquiv_refl _
  have hne : ¬ GramPhaseEquiv ((fun _ : ℕ => G₀) 1) ((fun t => P^[t] G₀) 1) := by
    show ¬ GramPhaseEquiv G₀ (P^[1] G₀)
    rw [Function.iterate_one]
    exact fun h => hmove (gramPhaseEquiv_symm h)
  have hnotequiv : ¬ LawEquiv (0 : Fin 1) ΓI
      (fun 𝔾 : ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t))
      (fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t))) := by
    intro heq
    have h2 := (heq (fun _ => G₀) hrealK).1 hsolI
    exact hmove (gramPhaseEquiv_symm (h2 0))
  refine ⟨ΓI, hΓI,
    ⟨fun _ G => G, fun _ => P,
      fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t),
      fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)),
      fun _ => G₀, fun t => P^[t] G₀, 1,
      ⟨hTLI, hproperI, hpropI, hL0I, hL1I, hhomI, hL2I, hL3I, hL4nI⟩,
      ⟨hTLP, hproperP, hpropP, hL0P, hL1P, ⟨P, fun _ => rfl⟩, hL2P, hL3P, hL4nP⟩,
      hnotequiv, hrealK, hrealO, hsolI, hsolP, le_refl 1, ?_, hne⟩,
    ⟨_, _, _, _, hnotequiv, hrealK, hrealO, hsolI, hsolP, ?_, hne⟩⟩
  · intro s hs
    interval_cases s
    exact gramPhaseEquiv_refl _
  · exact gramPhaseEquiv_refl _


/-- **`OL5` — THE PLURALITY THE HEADLINE RESTS ON: TWO `≈_L`-INEQUIVALENT SURVIVORS.**

Two transition families, both satisfying `L4d`, act 18's `ProperAt` and `PropagatesFrom`, `L0`,
`L1`, `L2` and both conjuncts of `L3` at the configuration named, generate laws whose solution sets
among pointwise realizable trajectories **differ**. The separating trajectory is the constant
trajectory at the admissible class of act 12's `H(i)`, which solves the first law and not the
second.

**The quotient is act 12's per-slice equivalence, act 17's trajectory lift of it, and the law
equivalence derived from them, and no other relation.** The law equivalence is set equality of
solution sets and introduces no new identification. **A plurality that would collapse only under an
equivalence outside that list is a plurality**, and no equivalence was introduced or widened during
execution.

**This is the plurality and not a characterization.** The both-directions characterization theorem
is **not** reached here, and the obstruction is named in the result note. **The absence of a
characterization is what the headline records, not the presence of a big one.**

**THE CLAUSE, carried at this mention — the headline's plurality.**
Act 19 classifies the cross-time laws a frozen ladder of conditions leaves standing, and adopts
none. A law that survives every condition this freeze names is a law that survives **those**
conditions, at the configuration frozen for it, and it is **not** a finding that it obtains in
nature, **not** a finding that the programme requires it, and **not** an adoption of it as the
physical law of evolution. **Surviving is not standing.** A rigidity verdict is a statement about
the frozen ladder and about the frozen quotient list, and a family or wide verdict is not a licence
to add one more condition, or to widen one more equivalence, until a plurality becomes a point.
**No law gains physical status by surviving, no carrier and no principle is adopted as the physical
one, and nothing here derives, recognises or approaches quantum evolution.** -/
theorem ol5_two_inequivalent_survivors :
    ∃ (Γ : ℕ → Matrix (Fin 4) (Fin 4) ℝ)
      (Φ Φ' : ℕ → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → (Fin 4 → Matrix (Fin 4) (Fin 4) ℂ))
      (Law Law' : (ℕ → Fin 4 → Matrix (Fin 4) (Fin 4) ℂ) → Prop),
      (∀ t i j, Γ t i j = 1 / 4)
        ∧ TransitionLaw Φ Law ∧ TransitionLaw Φ' Law'
        ∧ ProperAt (0 : Fin 1) Γ Law ∧ ProperAt (0 : Fin 1) Γ Law'
        ∧ PropagatesFrom (0 : Fin 1) Γ Law ∧ PropagatesFrom (0 : Fin 1) Γ Law'
        ∧ EvolvesTotally (0 : Fin 1) Γ Law ∧ EvolvesTotally (0 : Fin 1) Γ Law'
        ∧ PreservesAdmissible (0 : Fin 1) Γ Φ ∧ PreservesAdmissible (0 : Fin 1) Γ Φ'
        ∧ (∃ Phih, ∀ t, Φ t = Phih) ∧ (∃ Phih, ∀ t, Φ' t = Phih)
        ∧ (∀ Phih, (∀ t, Φ t = Phih) → Reversible (0 : Fin 1) (Γ 0) Phih)
        ∧ (∀ Phih, (∀ t, Φ' t = Phih) → Reversible (0 : Fin 1) (Γ 0) Phih)
        ∧ ¬ LawEquiv (0 : Fin 1) Γ Law Law' := by
  classical
  obtain ⟨ΓI, ΦI, LawI, hΓI, hΓIc, hΦI, hLawI, hLadderI⟩ := ol3_phiI_survives
  obtain ⟨ΓP, P, G₀, hΓP, hΓPc, hPdef, hG₀, hmove, hTLP, hproperP, hpropP, hL0P, hL1P, hL2P,
    hL3P, hL4nP, hPI, horbP⟩ := ol3_phiP_survives_through_l4
  have hΓeq : ΓI = ΓP := by
    funext t; ext i j; rw [hΓI t i j, hΓP t i j]
  subst hΓeq
  subst hΦI
  subst hLawI
  obtain ⟨hTLI, hproperI, hpropI, hL0I, hL1I, hhomI, hL2I, hL3I, hL4nI, _hL5I⟩ := hLadderI
  refine ⟨ΓI, fun _ G => G, fun _ => P,
    fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (𝔾 t),
    fun 𝔾 => ∀ t, GramPhaseEquiv (𝔾 (t + 1)) (P (𝔾 t)),
    hΓI, hTLI, hTLP, hproperI, hproperP, hpropI, hpropP, hL0I, hL0P, hL1I, hL1P, hhomI,
    ⟨P, fun _ => rfl⟩, hL3I, hL3P, ?_⟩
  intro heq
  have h2 := (heq (fun _ => G₀) (fun t => by rw [hΓPc t]; exact hG₀)).1
    (fun _ => gramPhaseEquiv_refl _)
  exact hmove (gramPhaseEquiv_symm (h2 0))

/-- **A DISCREPANCY IN THE FROZEN TEXT, CERTIFIED IN THE KERNEL AND NOT REPAIRED.** The
countercontrol table of this round's control plane names the discriminating witness as the identity
transition against the carrier relabelling **from the initial class of act 12's `H(1)`**, with the
relabelling taken at `σ` the column transposition act 18's fourth admissible dilation exhibits. Under
the freeze's own statement of the relabelling — the **simultaneous** relabelling of the fibre index
and of both matrix indices by `σ` — that pair does **not** separate: the relabelling **fixes** the
fibre-Gram tuple of `H(1)` exactly, because `H(1)` is invariant under relabelling both of its indices
by that transposition.

The freeze's `ΦP` statement and the freeze's `SIOP` countercontrol entry are therefore inconsistent
with each other at the configuration and the permutation both name. **The execution records the
discrepancy and does not repair the freeze.** The discriminating test is reported from the initial
class of act 12's `H(i)` instead, which is inside this freeze's own frozen witness supply and at the
frozen configuration, with the substitution named in the result note. -/
theorem phiP_fixes_hadamard_one :
    ∃ (Γ₀ : Matrix (Fin 4) (Fin 4) ℝ) (H₁ : Matrix (Fin 4 × Fin 1) (Fin 4 × Fin 1) ℂ),
      (∀ i j, Γ₀ i j = 1 / 4) ∧ AdmissibleDilationAt Γ₀ (0 : Fin 1) H₁
        ∧ (fun i : Fin 4 => ((FibreGram (0 : Fin 1) H₁) (Equiv.swap (2 : Fin 4) 3 i)).submatrix
            (Equiv.swap (2 : Fin 4) 3) (Equiv.swap (2 : Fin 4) 3)) = FibreGram (0 : Fin 1) H₁ := by
  classical
  obtain ⟨Γ₀, H₁, Hᵢ, hΓ₀, hH₁, hHᵢ, hadm₁, hadmᵢ, hnotG, _⟩ := hadamard_slices_not_twoSided
  refine ⟨Γ₀, H₁, fun i j => by rw [hΓ₀]; rfl, hadm₁, ?_⟩
  funext i
  ext j k
  simp only [Matrix.submatrix_apply, fibreGram_apply, Fin.sum_univ_one, hH₁,
    Equiv.swap_apply_def]
  fin_cases i <;> fin_cases j <;> fin_cases k <;>
    norm_num [Matrix.of_apply, Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons,
      Matrix.tail_cons, Fin.ext_iff]

end OrbitLawRigidity
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.OrbitLawRigidity.ol1a_descends_to_composition
#print axioms OIBridge.OrbitLawRigidity.ol1b_monoid_action
#print axioms OIBridge.OrbitLawRigidity.realizableGram_of_gramPhaseEquiv
#print axioms OIBridge.OrbitLawRigidity.ol2_l1_free
#print axioms OIBridge.OrbitLawRigidity.ol3_phiI_survives
#print axioms OIBridge.OrbitLawRigidity.ladder_of_involutive_transition
#print axioms OIBridge.OrbitLawRigidity.submatrix_conjTranspose_equiv
#print axioms OIBridge.OrbitLawRigidity.submatrix_mem_unitaryGroup
#print axioms OIBridge.OrbitLawRigidity.ol3_phiP_survives_through_l4
#print axioms OIBridge.OrbitLawRigidity.evolvesTotally_of_preservesAdmissible
#print axioms OIBridge.OrbitLawRigidity.propagates_uniqueness
#print axioms OIBridge.OrbitLawRigidity.relabelling_transition_data
#print axioms OIBridge.OrbitLawRigidity.orbit_of_family
#print axioms OIBridge.OrbitLawRigidity.ol3_phiT_fails_l2
#print axioms OIBridge.OrbitLawRigidity.ol3_phiC_fails_l3
#print axioms OIBridge.OrbitLawRigidity.ol3_phiX_fails_l0
#print axioms OIBridge.OrbitLawRigidity.ol4_siop_yes
#print axioms OIBridge.OrbitLawRigidity.ol5_two_inequivalent_survivors
#print axioms OIBridge.OrbitLawRigidity.phiP_fixes_hadamard_one
