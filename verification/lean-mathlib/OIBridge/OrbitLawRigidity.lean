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
   representatives naturally under act 12's two-sided moves: there is a map on dilations inducing
   the transition on fibre-Gram tuples which commutes with the constant and time-dependent in-fibre
   left moves of `LeftFibreGroup` and with the right gauges at the anchor — the two merged
   transformation laws being act 12's `fibreGram_left_mul`, under which the left move is invisible,
   and act 12's `fibreGram_mul_weak_apply`, under which the right gauge acts by the anchored
   phases. **`L4n` is a genuine strengthening of `L4d` and is tested as one.** Descent says the
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
          ∧ (∀ (t : ℕ) (L U : Matrix (V × A) (V × A) ℂ),
              LeftFibreGroup L → Ψ t (L * U) = L * Ψ t U)
          ∧ ∀ (t : ℕ) (U K : Matrix (V × A) (V × A) ℂ),
              WeakAnchorStabilizer a₀ K → Ψ t (U * K) = Ψ t U * K)
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

end OrbitLawRigidity
end OIBridge
