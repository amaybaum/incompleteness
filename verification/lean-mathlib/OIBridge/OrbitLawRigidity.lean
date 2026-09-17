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

end OrbitLawRigidity
end OIBridge

/-! ### Axiom report — one line per named result -/

#print axioms OIBridge.OrbitLawRigidity.ol1a_descends_to_composition
#print axioms OIBridge.OrbitLawRigidity.ol1b_monoid_action
