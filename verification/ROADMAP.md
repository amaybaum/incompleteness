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
| **ACTIVE** | A round is running, or is frozen and awaiting execution. |
| **OPEN** | A named obligation with neither a formal result nor an impossibility proof. Work is possible; nobody has done it. |
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
| **P0** | Continuous off-direct extension | OI→QM / Track B | **ACTIVE** | act 7 layer 2 |
| **P1** | Substratum Lemma 24.1 — semigroup transfer | Reconstruction | **OPEN** | unconditional `𝒢_sub` completeness |
| **P1** | A6 — background independence / local gauge covariance | Substratum | **GAP** | the complete A1–A6 formal package |
| **P1** | Physical C4 discharge at the cosmological and lattice cuts | Physical realization | **OPEN** | the actual physical realization |
| **P1** | H-Bell — composite and Bell closure | OI→QM / Bell | **OPEN** | Bell-inclusive completion |
| **P2** | Bekir–Golomb integer classification | Reconstruction | **EXTERNAL** | removes the last reconstruction premise |
| **P2** | H-link — physical-carrier identification | Standard Model | **CONDITIONAL** | the physical `K = 6` carrier |
| **P2** | H-state / H-frame / H-slope | Gravity | **CONDITIONAL** | the `ℏ` and `1/4` calibration |
| **P2** | Covariant matter→boundary coupling (the G3 map) | Gravity | **OPEN** | the MOND / dark-sector chain |
| **P3** | GR states → Level-III quasilocal states | Gravity / Level III | **OPEN** | formal state-layer integration |

### P0 — continuous off-direct extension

Construct a Source-A-admissible continuous extension of a lawful off-direct OI/`PPer` witness — with
the discrete restriction identified and off-directness preserved — or prove no such extension
exists.

Track B act 7 layer 1 stopped at `DC2a`: Source A's §3.4 dilation runs on an inherited continuity
contract that the `ℕ`-indexed off-direct witness does not instantiate. Until this is resolved there
is **no object in hand that is simultaneously a lawful OI visible family, off the direct branch, and
inside Source A's stated contract** — so the dilation-choice test cannot be run on anything. Act 7
reopens only on a positive outcome; an impossibility proof is itself a classification result.

→ [`BARANDES-DILATION-CHOICE-RESULT.md`](BARANDES-DILATION-CHOICE-RESULT.md) (the `DC2a` stop and
the obligation it names)

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
[`REPRESENTATION-SECTOR-AUDIT.md`](REPRESENTATION-SECTOR-AUDIT.md) (the finite-stage GNS setting)

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

→ [`MANUSCRIPT-AXIOM-AUDIT.md`](MANUSCRIPT-AXIOM-AUDIT.md),
[`SUBSTRATUM-INTERFACE-AUDIT.md`](SUBSTRATUM-INTERFACE-AUDIT.md),
[`lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean`](lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean)

### P1 — physical C4 discharge

The abstract realization and readback structure is clarified in the kernel. The **physical**
realization is not: at the cosmological cut C4 is open, and at the lattice cut C2 and C4 both remain
hypotheses. Prose inferring C4 from bidirectional coupling was corrected in the audit; the row
tracks the discharge, not the wording.

→ [`C4-CAUSAL-READBACK-AUDIT.md`](C4-CAUSAL-READBACK-AUDIT.md),
[`CONCRETE-CUT-AUDIT.md`](CONCRETE-CUT-AUDIT.md)

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

→ [`REPRESENTATION-SECTOR-AUDIT.md`](REPRESENTATION-SECTOR-AUDIT.md),
[`QUASILOCAL-COMPLETION-AUDIT.md`](QUASILOCAL-COMPLETION-AUDIT.md)

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

→ [`PHASE-SOURCE-AUDIT.md`](PHASE-SOURCE-AUDIT.md),
[`FLOW-ENDPOINT-AUDIT.md`](FLOW-ENDPOINT-AUDIT.md),
[`LIFT-AUDIT.md`](LIFT-AUDIT.md), [`LIFT-SOURCE-AUDIT.md`](LIFT-SOURCE-AUDIT.md)

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
