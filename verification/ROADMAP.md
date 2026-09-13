# Verification roadmap — the live obligation queue

The authoritative strategic queue for the verification programme. It sits **above** the proof
layers, not inside them: `lean/` is the zero-import layer, `lean-mathlib/` the Mathlib project,
`coverage/` the ledger, and each has its own narrower roadmap. This file is where a load-bearing
obligation is tracked from whichever layer it happens to live in.

**What this file is for.** The Lean-to-manuscript census is coverage-complete and
propagation-complete: it guarantees that every registered manuscript claim tracks the strongest
applicable formal result. It is **not** theorem-complete, and it was never meant to be. A premise
can be load-bearing in a manuscript, correctly labelled there as a named hypothesis, and have no
formal result behind it at all — the census will report that consistently and will not rank it
against anything else. This file does the ranking.

**Each row links to its audit or preregistration and carries no proof discussion of its own.** When
a row's status changes, the change belongs in that linked artifact first; this file follows it.

## Status vocabulary

The labels are not interchangeable and the distinctions are the point.

| Status | Meaning |
| --- | --- |
| **ACTIVE** | A round is running, or is **frozen and merged** and awaiting execution. A drafted or closed control plane is not a frozen one. |
| **OPEN** | A named obligation not closed at the required scope: no closing construction or theorem, and no impossibility theorem. It does **not** mean untouched — several `OPEN` rows carry substantial partial and audit work, and the row's linked artifact is where that work is recorded. |
| **GAP** | The manuscript states the condition, and the formal interface has **no predicate for it at all** — not a weak one, not an image. Closing it starts with defining the object. |
| **EXTERNAL** | A published result consumed as a cited premise. Formalizing it is an independent job; until then it is an assumption, and every result above it says so. |
| **CONDITIONAL** | Formally present, carrying a named hypothesis this programme has not discharged. The manuscript states the hypothesis; the row tracks it. |
| **DERIVED** | Kernel-proved and propagated to the manuscript. Rows reach this state and then leave the queue. |
| **INDEPENDENT** | The kernel has **settled it negatively**: the resource is not sourced by the stated architecture. This is a result, not a debt, and it never appears as unfinished work. |

**`INDEPENDENT` is the label this queue exists to protect.** A negative result about sourcing looks,
in a list of obligations, exactly like a thing nobody got round to. It is not, and anything recorded
`INDEPENDENT` below has a formal finding behind it.

## The queue

| Priority | Obligation | Track | Status | Unlocks |
| --- | --- | --- | --- | --- |
| **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**, and now STRUCTURAL: act 11's `GL2` proved the visible family does not fix the relative evolution; its `GI2` proved the **lift space** exceeds the maximal uniform weak stabilizer, but with *identical* relative objects, so the **shape** of the missing structure stays open | the conditional OI ⇔ QM statement; `P0a`/`P0b` closed, act 11's `GL2`/`GI2` landed |
| **P1** | Substratum Lemma 24.1 — semigroup transfer | Reconstruction | **OPEN** | unconditional `𝒢_sub` completeness |
| **P1** | A6 — background independence / local gauge covariance | Substratum | **GAP** | the complete A1–A6 formal package |
| **P1** | Physical C4 discharge at the cosmological and lattice cuts | Physical realization | **OPEN** | the actual physical realization |
| **P1** | H-Bell — composite and Bell closure | OI→QM / Bell | **OPEN** | Bell-inclusive completion |
| **P2** | Bekir–Golomb integer classification | Reconstruction | **EXTERNAL** | removes the last reconstruction premise |
| **P2** | H-link — physical-carrier identification | Standard Model | **CONDITIONAL** | the physical `K = 6` carrier |
| **P2** | H-state / H-frame / H-slope | Gravity | **CONDITIONAL** | the `ℏ` and `1/4` calibration |
| **P2** | Covariant matter→boundary coupling (the G3 map) | Gravity | **OPEN** | the MOND / dark-sector chain |
| **P3** | GR states → Level-III quasilocal states | Gravity / Level III | **OPEN** | formal state-layer integration |

### P0 — what fixes the relative evolution: act 11's no-go, and what it leaves

**`P0a`, the MAP axis, is CLOSED.** Act 9 proved that **`R-2` alone** forces every same-interface
readback to agree with the merged `R_{a₀}` on every modulus-squared unitary on the dilated carrier
(`RB3`) — `R-1` and `R-3` being redundant for that theorem — and derived from it that each of act 7's
two witnesses keeps its `DC1` divergence under **every** member of the frozen `R-1`/`R-2`/`R-3`
same-interface class (`RB1-A`, `RB1-B`, reported separately). Class nonemptiness was proved first,
from act 7 layer 2's three merged theorems.

**So act 7 layer 2's caveat sharpens, in the wording act 9 froze in advance and no further:**

> not an artifact of the readback map within the `R-1`/`R-2`/`R-3` same-interface class; dependence
> on the **anchoring convention** remains open.

**`P0b`, the ANCHOR axis, was run — and it COLLAPSED.** Act 10 asked the frozen question: holding
act 7's compared dilations fixed, is there an anchor at which they *all* still reproduce their
visible slices, under which the two visible candidates agree?

**Availability was answered first, and answered in the negative on both witnesses.** The jointly
reproducing anchors of each compared configuration are **exactly the singleton `{a₀ = 0}` act 7
already used** — proved by exhaustion over the finite anchor domain, in both directions, so the
domain is a singleton and not empty. That is **`AB0-A`** and **`AB0-B`**, reported separately.

**`AB1` was therefore NOT assigned on either witness, although its proposition is TRUE on both.**
Every jointly reproducing anchor does preserve the divergence — trivially, there being only one. A
universal satisfied only because its domain has no new element is not a robustness result, and act
10's freeze refused the label in advance for exactly this case. `AB2` is false on both: the collapse
conceals no agreement.

**So `P0` is NOT closed, and the anchor-axis dependence is not resolved — it is RECLASSIFIED** as not
reachable by this construction. The collapse localizes entirely to the `G₁` side: the identity
dilation of `G₂ = 𝟙` is admissible at **every** anchor, proved for any carrier.

**The reclassification rests on `AB0` alone.** `AB0` is a statement about act 7's **fixed** compared
configuration: what collapses is joint reproduction by those four dilations, at the only other anchor
the frozen ancilla provides. **Whether some other anchor admits some other dilation is neither asked
nor answered** — in either direction. Constructing a dilation to make a different anchor admissible
is a dilation-choice result whatever it is framed as, act 10's freeze puts it out of scope for `P0b`,
and it belongs with `D3`.

**What stays live is therefore the UPSTREAM choice, wholly untouched.** Act 7's dilations were built
around `a₀ = 0`; a different anchor chosen upstream would have produced **different dilations**, and
whether that pairing diverges is out of scope here and needs its own freeze. Act 7 layer 2's caveat
**stands unchanged**; if anything `AB0` makes it more necessary, since the convention could not even
be varied to test it.

**Act 7's `D3` gap remains separately OPEN and was not used.** Stinespring supplies **pointwise**
existence, with no coherent time-indexed family derived or selected and no stated link from the
visible family's regularity to `Θ`'s or `U`'s. It is still the live route by which a `DC4`-shaped
invariance could hold on a **narrower** class — one cut down by a coherence condition — which is why
act 7's refutation is recorded at exactly the class its statement names.

## Act 11 moved the question above the convention layer, and answered it in the negative

**Acts 9 and 10 were characterizing conventions on a structure underdetermined one level up.**
`AdmissibleDilationAt G a₀ U` constrains `U` only through `G i j = ∑_a ‖U (i,a) (j,a₀)‖²`: that
fixes an anchored modulus-squared marginal and **determines no channel**. Stinespring uniqueness
cannot close the gap, for a reason of order — it speaks about dilations *of a given channel*, and
here the channel is not yet pinned.

**Act 11 asked what a coherent time-indexed lift on a fixed carrier determines, and proved it
determines less than uniqueness needs.**

- **`GL2`** — a **time-dependent** element of the anchored stabilizer carries a coherent lift to
  another coherent lift of the **same** visible family, with exact cross-time composition for both,
  while the relative candidate **moves**. Proved over the *strong* stabilizer, the smaller of the
  two classes, which makes the statement stronger. The cocycle condition is recorded **vacuous** —
  it holds for every family whatsoever — and nothing in the round draws force from it.
- **`GL3`** — a **constant** gauge leaves every relative object unchanged, so time-dependence is
  **necessary**. One direction only: `GL2` supplies that it *can be* sufficient, and neither says
  every time-dependent gauge moves every candidate.
- **`GI2`** — and this the freeze predicted at **no strength on either side**: there are two
  coherent lifts of one visible family whose forced relating element lies **outside the maximal
  uniform weak stabilizer**. So the **lift space** is not exhausted by that class. The same theorem
  proves this pair has the **same relative object at every pair of times**, so `GI2` is **not**
  evidence that the relative evolution carries non-gauge ambiguity; `GL2` is the only
  relative-evolution no-go here.

**Two stabilizers, because conflating them was the error act 11's control plane was corrected for.**
Fixing the anchored columns is **sufficient** for invisibility, not necessary: the **strong** class
`𝒢ˢ ≅ U(|V|(|A|−1))` is a subgroup whose size is a **lower bound** on invisible freedom, while the
**weak** class `𝒢ʷ ≅ U(1)^{|V|} × U(|V|(|A|−1))` adds the anchored phases and is the maximal
*uniform* visibility-preserving class **for `|V| ≥ 2`**. At `|V| = 1` the visible datum is
identically `1`, every unitary preserves it, and the maximal class is all of `U(|A|)` — so `𝒢ʷ` is
**not** maximal there, and act 11 does not claim it is. **The two `≅` identifications above are
arithmetic, not kernel-certified**: the module proves the structural characterizations and the
complement's cardinality, and nothing rests on the group identities or dimensions.

**What this changes about `P0`.** The open question is no longer whether some convention rescues
uniqueness — it does not, by `GL2` — but **what additional structure determines the relative
evolution**. Act 11 does **not** constrain that structure's shape. `GI2` does not do it: its
witness lies outside the weak class yet has *identical* relative objects, so it separates the lift
space from the gauge class without separating the relative evolutions. **The shape question stays
open**, and what would bear on it is a same-visible pair that is **both** outside the weak class
**and** different in relative evolution. Act 11 supplies none and shows neither that one exists nor
that one cannot.

**What act 11 does NOT license.** `P0` is not closed. Act 7 layer 2's caveat **stands unchanged** —
made structural rather than provisional, which is not the same as retired. Nothing proves OI and QM
inequivalent: the claim is that the visible family does not *by itself* fix the relative evolution,
and a conditional equivalence with an additional stated principle is untouched. No
candidate-selection principle is claimed or shown to be required.

**Act 7's `D3` is partially subsumed, precisely.** Act 11 subsumes it as a proposed *uniqueness
mechanism* and **does not close its source-level existence/regularity audit**, which remains open.
Coherent-lift existence was not presumed: the round exhibits concrete lifts where it needs them.

→ [act 11 result](programmes/oi-qm/track-b/act-11-coherent-lift-gauge/result.md) (`GL1s`, `GL1w`,
`GL2`, `GL3`, `GI2`, and what none of them licenses)
→ [act 11 preregistration](programmes/oi-qm/track-b/act-11-coherent-lift-gauge/preregistration.md)
(the two stabilizers, the targets, and the `|V| ≥ 2` scoping)

**Act 7's merged `DC1` is unrevised**, and acts 9, 10 and 11 cite rather than rewrite it. Act 7 layer 2's
`D5` chronological-ordering control also stands **NOT CERTIFIED**: acts 9 and 10 repaired the
*practice*, pinning their own ordering in git, but that repair is forward-looking and does not
certify the earlier round. `DC2a` and `CE1` are unrevised, and no manuscript was touched by any of
them.

**The chronology guard strengthened twice more.** Act 9's `R7-RBR` was repaired in review to recover
shallow history itself and to ask its question of the real `pull_request.head.sha` rather than the
synthetic PR merge commit. Act 10's `R7-ABR` reuses that mechanism and strengthens the **predicate**:
head-only ancestry admits a commit made before the freeze and merged in alongside it, so `R7-ABR`
additionally enumerates `git rev-list H ^B` and requires **every** commit of the execution-only
history to descend from the freeze, fail-closed, recovery included. The property certified is *no
commit reachable from the execution head lies outside the freeze's descendants*.

→ [act 10 result](programmes/oi-qm/track-b/act-10-anchor-robustness/result.md) (`AB0-A`, `AB0-B`,
the withheld `AB1` labels, and why `P0` is reclassified rather than closed)
→ [act 10 preregistration](programmes/oi-qm/track-b/act-10-anchor-robustness/preregistration.md)
(the property cut, the three-valued grid, the availability prerequisite, and the strengthened
chronology contract)
→ [act 9 result](programmes/oi-qm/track-b/act-09-readback-robustness/result.md) (`RB3`, `RB1-A`,
`RB1-B`, and why `P0` is not closed)
→ [act 9 preregistration](programmes/oi-qm/track-b/act-09-readback-robustness/preregistration.md)
(the frozen class cut, the outcome grid, the formalization stop condition, and the chronology
control)
→ [act 7 layer-2 result](programmes/oi-qm/track-b/act-07-dilation-choice/layer-2-result.md) (the
`DC1` exhibitions this round quantifies over, and the limitation it half-closes)
→ [act 7 readback amendment](programmes/oi-qm/track-b/act-07-dilation-choice/readback-amendment.md)
(the frozen map, and `R-1`/`R-2`/`R-3` in their original role)
→ [act 7 resumption result](programmes/oi-qm/track-b/act-07-dilation-choice/resumption-result.md)
(the `D4a`/`D4b` answers with coordinates)
→ [act 7 result](programmes/oi-qm/track-b/act-07-dilation-choice/result.md) (the `DC2a` stop and the
frozen stop table)
→ [act 8 result](programmes/oi-qm/track-b/act-08-continuous-extension/result.md) (`CE1`, the object
that made the adjudication reachable)

### P1 — Substratum Lemma 24.1, the semigroup-transfer step

This is the row to watch, and it differs in kind from most of what follows. The other P1/P2
hypotheses are **explicitly chosen physical assumptions**, stated as such. Lemma 24.1 is a
**mathematical step** — Stinespring/GNS uniqueness extended from one CP map to the whole discrete
unitary-generated semigroup — and the claim it supports is that the substratum gauge freedom has
been **exhaustively classified**. The exhaustiveness of the four generator families of `𝒢_sub`, and
with it the strongest reconstruction and gauge-uniqueness language, is conditional on it. The
manuscripts identify this exact step for specialist verification.

That combination — a mathematical step carrying an exhaustiveness claim — is precisely what this
Lean programme is built to close, which is why it ranks above obligations that are larger in scope.

→ [`papers/Structure.md`](../papers/Structure.md) (Theorem 23, §G3),
[`papers/Complexity.md`](../papers/Complexity.md) (Theorem 24's conditional closure),
[`REPRESENTATION-SECTOR-AUDIT.md`](audits/manuscript/representation-sector-audit.md) (the finite-stage GNS setting)

### P1 — A6, and what is and is not already represented

`SubstratumInterfaceAudit.lean` carries a `Substratum` structure holding the manuscript substrate
data, and against it: **A1, A2 and A5 stated outright; A3 with the degree as a parameter and in
family form; A4 with the gauge as a parameter; A6 a gap with no predicate.** The manuscripts'
discrete wave rule is an instance, `waveSubstratum`, satisfying A1–A5 as stated.

**Two qualifications this row keeps attached, because dropping either would overstate the position.**
A3's single-lattice form is vacuous — `a3_of_fintype` bounds the degree by the site count — so A3's
content is the family form, not the per-lattice one. And A4 is carried up to a gauge parameter, with
the exact form recovered at trivial gauge.

A6 needs internal indices and a coupling matrix that the substratum type does not carry, and the
manuscript wording admits distinct invariant-versus-covariant readings which must not be silently
identified. Closing it is a definitional job before it is a proof job.

**A separate and still-true statement, about a different carrier.** `ManuscriptAxioms.lean` records
that no manuscript-level conjunct of A1–A6 is a faithful predicate of the **bare operational
theory**, which has no distinguished substratum: there A1 and A2 have realized-core *images*, and
images are not the axioms. That finding is about the operational interface; the paragraph above is
about the substratum structure. Both hold, of different objects.

→ [`MANUSCRIPT-AXIOM-AUDIT.md`](programmes/substratum/manuscript-axiom-audit.md),
[`SUBSTRATUM-INTERFACE-AUDIT.md`](programmes/substratum/interface-audit.md),
[`lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`](lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean)

### P1 — physical C4 discharge

The abstract realization and readback structure is clarified in the kernel. The **physical**
realization is not: at the cosmological cut C4 is open, and at the lattice cut C2 and C4 both remain
hypotheses. Prose inferring C4 from bidirectional coupling was corrected in the audit; the row
tracks the discharge, not the wording.

→ [`C4-CAUSAL-READBACK-AUDIT.md`](audits/physical-realization/c4-causal-readback/preregistration.md),
[`CONCRETE-CUT-AUDIT.md`](audits/physical-realization/concrete-cut/preregistration.md)

### P1 — H-Bell and composite closure

Full operational quantum mechanics in the sense of entangled composites, local operations and Bell
correlations needs more than the finite rooted-law equivalence. H-Bell requires the
preparation-indexed state-dependent graph family to preserve operational no-signaling **and** to
satisfy a curvature/metric convergence condition strong enough for the Ollivier–Ricci continuum step
the Einstein reconstruction uses.

**And H-Bell is downstream of a harder obligation**, which this row records rather than leaves
buried: for the degree-6 cubic reference graph the intrinsic hop metric is exactly `ℓ¹`, a `√2`
diagonal stretch that does not decay at any scale, so the hop-metric curvature route fails for the
reference family **before any Bell edge is added**. The curvature functional has to be re-founded on
the propagation/Laplacian geometry rather than on shortest-path counts. Bell-inclusive
full-substratum uniqueness is not established.

→ [`papers/Main.md`](../papers/Main.md) (the Bell–lattice obstruction corollary and the standing
scope conditions)

### P2 — Bekir–Golomb integer classification

`TurnpikeScopeTransfer.lean` consumes `BGIntegerClassification` as a cited premise. Everything around
it is kernel-proved — the integer-to-real passage and the final assembly included — and the probe's
own scope block names it the sole remaining K3 backlog item. Formalizing the 2007 classification is
an excellent independent job and can run in parallel with everything above it.

→ [`lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean`](lean-mathlib/OIBridge/TurnpikeScopeTransfer.lean)

### P2 — H-link

The six signed simple-cubic links and their `3 ⊕ 2 ⊕ 1` decomposition are unconditional geometry.
What is conditional is identifying that link space with the **complete physical carrier**; the
single-copy clause is what turns it into `K = 6`, so every downstream statement consuming `K = 6`,
`N_f = 6`, or a fixed three-sector count inherits it. H-cust and the named spin/chirality conditions
are further downstream qualifications.

→ [`papers/Main.md`](../papers/Main.md), [`papers/SM.md`](../papers/SM.md)

### P2 — H-state, H-frame, H-slope

The `ℏ` and `1/4` calibration is not unconditional, and the manuscript says so. H-frame is not
derived. H-state requires an additional state-selection principle, because the same partition admits
both vacuum-like and excited laws. H-slope is inherited by the temperature calibration.

→ [`papers/GR.md`](../papers/GR.md)

### P2 — covariant matter→boundary coupling

The MOND / dark-sector / entropy-displacement chain needs more than nonzero C1 coupling: the
emergent rest energy and heat must be delivered to the boundary in the required covariant way. The
manuscript assigns that to the open coupling theorem.

→ [`papers/GR.md`](../papers/GR.md)

### P3 — GR states to Level-III quasilocal states

The representation/sector audit found no independent representation-choice problem. It left open
whether the GR and H-state conditions **transport** to states of the formal quasilocal lattice
algebra. A real interface seam, and downstream of the core OI→QM question, which is why it sits at
P3 rather than higher.

→ [`REPRESENTATION-SECTOR-AUDIT.md`](audits/manuscript/representation-sector-audit.md),
[`QUASILOCAL-COMPLETION-AUDIT.md`](audits/operational/quasilocal-completion-audit.md)

## Settled negatively — `INDEPENDENT`, and not queue items

**These are findings. They do not belong on the list above and are recorded here so they are not
re-added to it.**

| Finding | Status |
| --- | --- |
| The source of phases | **INDEPENDENT** |
| Executable intermediate layer flow | **INDEPENDENT** |
| The presently stated observer-level lift | **INDEPENDENT** |

The kernel result is negative and it is a result: the stated configuration-level observer access does
**not** source the quarter phase or an executable intermediate layer flow, and none of the lift
formulations that actually land in the operational interface repairs that. Under the current
architecture these are identified independent resources — proofs nobody has neglected to write.

→ [`PHASE-SOURCE-AUDIT.md`](audits/foundations/phase-source-audit.md),
[`FLOW-ENDPOINT-AUDIT.md`](audits/foundations/flow-endpoint-audit.md),
[`LIFT-AUDIT.md`](audits/foundations/lift-audit.md), [`LIFT-SOURCE-AUDIT.md`](audits/foundations/lift-source-audit.md)

## Deliberately not prioritized

Three candidates that a reader might expect here, with the reason each is absent:

- **Infinite-support instruments** — the instrument audits show no live central prediction requires
  them.
- **Hilbert-space representation selection** — the representation/sector audit found no live
  prediction requires a representation choice; the framework's setting is finite and the question
  becomes which representative within an equivalence class.
- **CT3's single static Hamiltonian generator** — continuous-time autonomous generation is explicitly
  **extra structure** relative to the already-formalized discrete-time and quasilocal theory, and
  `RegionLimit.lean` carries the countermodel showing continuous time is not determined by the
  discrete dynamics.

Absent means *adjudicated and set aside with a reason*, not overlooked. Any of the three returns to
the queue if a live prediction starts depending on it.

## Where new artifacts go

New audits, preregistrations and results go under a **programme** or **audit** directory, never at
the `verification/` root. [`MIGRATION-MANIFEST.md`](MIGRATION-MANIFEST.md) records the destination
for every artifact currently at the root and is the grandfather list for `artifact_placement_check`.
