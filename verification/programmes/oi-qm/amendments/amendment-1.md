# OI → QM research programme — Amendment 1: formalization-first manuscript gate

Status base: `main` at `a3695ce27b25a468a9593e796fade1a1e938895c` (post-PR #550, Arc C closed).

This is a strategic roadmap amendment to `verification/programmes/oi-qm/PROGRAMME.md`. It is **not** a theorem, audit, preregistration, or execution result. Detailed mathematical status remains controlled by the Lean sources, frozen audits/results, verification ledger, and manuscript scope guards.

This amendment is intentionally separate from the Arc D control-plane PR. It does not modify, interpret, or freeze `verification/programmes/oi-qm/track-i/arc-d-operational-sourcing/preregistration.md`; Arc D keeps its own split-PR discipline and evidence standards.

## 1. Status update after Arcs B and C

The canonical programme map predates the closure of Arcs B and C. For current strategic sequencing, the following supersedes its older frontier/status language.

### Arc B — closed

For finite visible carriers, the OI-realizable rooted stochastic class is characterized intrinsically:

`C_OI(V) = PPer(V)`.

This is kernel-closed. The result is the exact visible stochastic boundary for finite reversible OI under the inherited realization interface.

### Arc C — closed

The all-time fixed-basis Born representation boundary is also kernel-closed. Over the frozen finite-visible universe the headline relation is **RC1 — proper overlap**:

- at the empty carrier, `Q*(V) = ∅ ⊊ C_OI(V)`;
- at every nonempty finite carrier, `C_OI(V) ⊆ Q*(V)`;
- at `V = Fin 2`, the inclusion is strict: `C_OI(V) ⊊ Q*(V)`;
- strictness at every nonempty finite carrier is not claimed.

The two failures of global inclusion occur at different carriers. Arc C establishes mathematical representability only. It does **not** source coherent control, phases, Hamiltonians, preparations, measurements, instruments, ancillas, composites, or any other physical operational repertoire. The #540 boundary remains binding.

### Current frontier — Arc D

Arc D is now the active frontier. Its task is to determine which operational quantum resources are physically **sourced by OI itself**, rather than merely present in some mathematical representation of OI-visible data.

Arc E remains the required composite/locality/Bell continuation wherever the final scientific claim uses subsystem composition, local operations, entanglement, incompatible measurements, or quantum correlation structure.

## 2. Formalization-first manuscript synchronization gate

The publication-facing manuscripts are now downstream of the formal programme.

**Gate.** Do not strengthen, reorganize, or newly integrate the central OI → QM scientific claims or proof narrative into the manuscripts while the load-bearing equivalence/classification chain is still being formalized. In particular, the newly closed Arc B and Arc C results remain verification-layer results until:

1. Arc D is kernel-closed, or every remaining Arc D resource has an explicit final disposition under the programme taxonomy (`Derived`, `Conditional`, `Independent`, or `Open`); and
2. the Arc E obligations actually required by the intended manuscript claim are kernel-closed or explicitly classified under the same taxonomy.

This gate is deliberately stricter than “the current prose seems correct.” Its purpose is to prevent nearby but inequivalent statements from being silently identified in prose — for example finite-horizon with all-time, P-indivisibility with a broader non-Markovianity claim, mathematical representability with physical sourcing, or a single-system theorem with a composite/Bell conclusion.

### Safety exception: corrections are never delayed

The gate does **not** prohibit corrections to publication-facing statements already shown to be false, over-scoped, or incorrectly qualified. If formal work establishes that a current manuscript sentence is wrong, the correction should be made promptly at the proved scope rather than preserved for synchronization convenience.

Likewise, bibliographic, typographic, formatting, or purely historical/provenance fixes may proceed when they do not change scientific claims.

What is deferred is **new strengthening and proof-narrative integration**, not correction of known errors.

### The under-claiming debt is deferred deliberately

The synchronization gate defers not only new strengthening but also integration of kernel-proved results currently absent from the publication-facing corpus, including the §3.7 under-claiming debt. Those results remain valid verification-layer results during the freeze and are to be integrated at their proved scope in the synchronized manuscript pass. Corrections to statements already known to be false, over-scoped, or misqualified remain exempt from the gate.

This is recorded explicitly because §3.7 classifies under-claiming as the same defect as overclaiming, reflected. Deferring it is a decision about sequencing, not a judgement that the debt is less real, and it should not be discharged piecemeal ahead of the pass.

## 3. Pre-publication theorem spine

Before the next substantive manuscript synchronization, construct an explicit theorem-to-prose spine for the OI → QM chain:

`OI assumptions`

`→ finite visible stochastic class (C_OI = PPer)`

`→ all-time quantum representation boundary (Q*)`

`→ physically sourced single-system operational resources`

`→ preparation / measurement / instrument / ancilla lift`

`→ composites / locality / Bell-capable structure where required`

`→ target operational QM`

`→ final equivalence or exact residual classification`.

Every load-bearing arrow must be assigned one of four statuses before manuscript integration:

- **Kernel-proved / Derived** — an exact formal theorem from accepted prior hypotheses;
- **Conditional** — proved after adding a named physical principle, with that principle stated explicitly;
- **Independent** — a countermodel proves the desired resource does not follow from the current OI assumptions;
- **Open** — not yet proved or refuted; failed formalization or failed construction is not a mathematical negative.

Where a theorem depends on a cited external premise rather than being fully kernel-closed, that evidence type must be recorded separately rather than rounded up to kernel-proved.

The manuscript wording must then be generated from the exact theorem statements and hypotheses in this spine. The publication-facing text is not allowed to strengthen an implication, swap quantifiers, suppress a carrier/horizon/preparation hypothesis, or promote representation to sourcing.

## 4. Synchronization rule

Once the relevant Arc D and Arc E obligations have reached final dispositions and the theorem spine is complete, perform one coordinated manuscript pass rather than incremental research edits scattered across papers and book chapters.

That pass should, for every substantive OI → QM statement:

1. identify the exact formal theorem or explicit non-kernel evidence supporting it;
2. record its load-bearing hypotheses and scope;
3. choose prose that is no stronger than that theorem;
4. census every publication-facing occurrence and mirror;
5. update the coverage ledger and scope guards in the same round;
6. preserve explicit `Conditional`, `Independent`, and `Open` labels rather than smoothing them into an equivalence narrative.

The synchronization pass may add results that are currently stronger in the kernel than in the manuscripts, but only at the scope actually proved.

## 5. Immediate programme state

Arcs B and C are kernel-closed. Finite reversible OI yields exactly `PPer` at the rooted stochastic level, and its all-time fixed-basis Born representation relation is RC1 proper overlap. That representation theorem does not establish a physical quantum repertoire.

Arc D is the active frontier, followed by the relevant Arc E composite/Bell obligations. The central manuscript proof narrative remains frozen against new strengthening until those formal obligations are closed or precisely classified and the theorem-to-prose spine is complete.

This amendment changes strategic sequencing only. It does not alter any frozen audit, theorem, Arc D target, backlog priority, or publication claim by itself.
