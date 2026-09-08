# OI → QM research programme map

Status base: `main` at `7d4b9ec3d2df5d6ace28fe24d0cb83f853235ba6` (post-PR #542).

This file is the canonical **strategic map** for the larger OI → QM research programme. It is not a theorem, an audit, a preregistration, or a replacement for the detailed verification ledger. Its purpose is to state, in one place:

- the ultimate research objective;
- what has already been established;
- what is still open;
- the order in which the remaining questions should be attacked;
- what different success and failure outcomes would mean for the final scientific claim.

Detailed theorem status remains controlled by the Lean sources, audit files, verification ledger, and manuscript scope guards. Where this map and a theorem/audit disagree, the theorem/audit controls.

---

## 1. Ultimate objective

The strongest possible endpoint is a theorem of the form

`OI + C  <->  operational quantum mechanics`,

where `C` is an explicit set of physical conditions that are either derived from the OI substratum or clearly identified as additional principles.

If that cannot be proved, the programme should instead terminate in a classification theorem of the form

`OI  ->  precisely characterized family of possible operational theories`,

with quantum mechanics identified as one subclass and every additional principle needed to select it stated explicitly.

The programme therefore has two acceptable scientific endpoints:

1. **Equivalence:** OI, with a justified and explicit condition set, is operationally equivalent to QM.
2. **Classification:** OI does not uniquely force QM, but the exact OI-compatible theory space and the extra principles selecting QM are known.

A negative result at an intermediate bridge is not a failure of the programme if it sharpens this classification.

---

## 2. Three notions that must not be conflated

The programme distinguishes three increasingly strong claims.

### A. Quantum representation

The observer-accessible stochastic data can be represented in Hilbert-space / Born-rule form.

This is a mathematical representation statement. By itself it does **not** imply that the underlying physics supplies arbitrary coherent phases, Hamiltonians, unitary controls, instruments, or composite-system operations.

### B. Quantum operational repertoire

The physically available preparations, reversible controls, measurements, instruments, composites, and transformations are exactly those of quantum mechanics, at the stated finite or quasilocal level.

This is stronger than merely admitting a Hilbert-space representation.

### C. Full physical equivalence to QM

The OI physical theory, including composition, locality, dynamics, measurement, state preparation, correlations, and the relevant infinite-system/continuum qualifications, is equivalent to the target version of quantum mechanics.

The research programme is complete only when the scope of the final claim is explicit about which of A, B, or C has actually been established.

---

## 3. What is already established

### 3.1 Finite operational completion is classified

The Mathlib verification programme gives a finite operational-QM completion classification. Bare finite OI does not uniquely select quantum mechanics. Exact finite operational QM is obtained when the required well-formedness and substantive operational principles are added; the substantive principles have been separated by explicit countermodels.

The strongest carrier-general forms reduce the operational package to implementation locality, a sufficient reversible/control richness condition, and embedded observation. The development further reduces the control side to an elementary continuously driven transition plus exchanges, with no quarter-phase primitive required.

**Interpretation:** the abstract operational conditions selecting finite QM are understood. The open question is whether the concrete OI physics itself supplies those conditions.

### 3.2 Concrete substratum sourcing reaches a sharp control boundary

The substratum-source audits show that the current concrete OI substratum supplies the structural closure properties needed by the finite operational theory, but its directly sourced observable operators are monomial/permutation-like. Bijective dynamics and the existing read-write couplings do not by themselves source a continuously tunable off-diagonal generator.

Thus the current substratum plus continuous off-diagonal controllability yields finite operational QM, but that controllability resource is not presently derived from the current OI axioms.

**Interpretation:** this is a sourcing boundary, not a representation theorem and not a proof that OI forbids the missing control resource.

Historical statements that the “OI → QM derivation programme is closed” refer to this completed Level-I substratum/control sourcing branch. They do **not** mean that the larger equivalence/classification programme described in this file is finished.

### 3.3 Typed and quasilocal extensions are substantially understood

The typed-completion audit shows that, within the natural carrier-general operational interface, the endomorphic restriction is a typing artifact: the finite typed theory is determined by its quantum endomorphic shadow.

The quasilocal-completion work constructs and characterizes the fixed-lattice infinite-region C*-system generated by the finite stages, with states and OI-induced discrete dynamics. It also records the remaining qualifications: no preferred Hilbert representation is selected, continuous time is not uniquely determined by the discrete dynamics, and general infinite-support operational availability is not forced by the frozen structure.

**Interpretation:** the finite-to-quasilocal mathematical completion is much clearer than the physical sourcing of the full operational repertoire.

### 3.4 A rooted stochastic observer family is sourced at the realization level

The observer-realization layer supplies a legitimate rooted stochastic family

`Gamma_t(a,j) = P(X_t = j | X_0 = a)`

once the finite reversible realization and fixed hidden prior are specified.

A unique global invariant ensemble is not required for this rooted conditional family. The fixed hidden prior remains part of the realization datum, and different allowed priors can change the visible rooted family.

### 3.5 The Barandes boundary is a representation boundary, not an operational-sourcing result

The Barandes audit supports the use of rooted/conditional stochastic data for the mathematical stochastic-to-quantum representation route. It does not supply physical coherent controls or identify OI P-indivisibility with every notion of stochastic indivisibility used in the external literature.

The programme must therefore keep two routes separate:

`rooted stochastic family -> quantum mathematical representation`

and

`OI physical realization -> physically available quantum operations`.

### 3.6 Causal hidden readback does not force accessible-window P-indivisibility

PR #542 establishes a realization-level `CausalReadback` notion with physical write/store/read meaning, but shows that the local consequences are weaker than initially hoped.

In particular, on an arbitrary same accessible window:

- `CausalReadback -> C4e` is false;
- `CausalReadback -> C4r` is false;
- `CausalReadback -> PIndivisibleWithin K` is false.

The exact countermodel `I -> B_(3/4) -> B_(5/8)` is parent-positive and P-divisible through the audited two-step window.

The history-sensitive `C4w` implication survives only with the correct visible-preparation support condition on the two witness roots.

This exposes two independent preparation dependencies:

1. the hidden prior can change the rooted stochastic family itself;
2. the visible initial law can change whether process-level history dependence is actually witnessed.

**Interpretation:** real hidden causal memory is not enough to guarantee short-time quantum-style information backflow.

### 3.7 Part of what is established is carried by no manuscript

The registry classifies sixteen kernel families as carried by no publication-facing statement. Among them is the operational pair-flow equivalence, whose own registry entry records the closure with one sourced pair flow as exactly quantum mechanics — a statement stronger than anything the corpus presently asserts.

This is a scope gap in the direction opposite to overclaiming. The reporting rules in §7 all guard against asserting more than has been proved; a result proved in the kernel and narrated nowhere is the same defect reflected, and it is not visible from the manuscripts alone.

**Interpretation:** the publication-facing corpus is not an inventory of what the programme has established. Closing this debt is a matter of stating results at the scope they were proved, which is separate from, and must not be used to soften, the corrections owed where publication wording is too strong.

---

## 4. Current frontier

The active frontier after PR #542 is the **recurrence-scale indivisibility and horizon-tightness problem**.

The primary mathematical route is now:

`storage overlap + later visible return to identity -> TV revival -> P-indivisibility`.

The important question is not merely whether a recurrence-scale obstruction exists, but whether that horizon is tight.

The active audit asks whether there can be a finite reversible parent-positive realization that remains P-divisible on every shorter horizon and becomes indivisible only when the relevant visible-return horizon is reached.

This distinction controls the physical interpretation:

- if tightness succeeds, the universally guaranteed obstruction may occur only at a potentially inaccessible recurrence/readback-return scale;
- if some shorter-horizon obstruction is mathematically unavoidable, the OI → QM bridge is physically stronger.

No recurrence-scale result should be described as accessible quantum-like nonclassicality without an independent accessibility bound.

---

## 5. Next major research arcs

The remaining programme should proceed in the following order unless a later audit supplies a reason to reorder it.

### Arc A — finish the stochastic/nonclassicality boundary

1. Complete the recurrence-scale theorem at the exact controlling visible-return horizon.
2. Determine horizon tightness.
3. Record the hypotheses actually used, and do not assert that they are the weakest available unless that has itself been proved; in particular distinguish storage overlap from the full write/store/read parent when the stronger clauses are not load-bearing.
4. Correct publication wording where preparation or horizon scope is demonstrably too strong.
5. If tightness succeeds, determine whether the controlling visible-return horizon admits an independent bound for physically relevant realizations. §4 and reporting rule 2 both make an accessibility bound the condition under which a recurrence-scale obstruction could carry a physical reading; obtaining or excluding such a bound is therefore programme work, not a standing caveat. If tightness succeeds and no bound is available, the guaranteed obstruction is exact but of unknown physical reach, and the equivalence claim must say so.

**Exit condition:** we know exactly what nonclassical stochastic behavior finite reversible OI forces, at what horizon, under which preparation assumptions, and whether that horizon is reachable.

### Arc B — characterize the full class of OI-realizable rooted stochastic families

Move beyond examples and individual memory criteria. Seek an intrinsic characterization of the complete family of rooted stochastic processes realizable by finite reversible OI with the allowed observation and preparation structure.

Ideal endpoint:

`finite OI realizations  <->  C_OI`,

where `C_OI` is described without reference to a hidden permutation construction.

Questions include:

- which row-stochastic families admit one finite reversible dilation with one fixed hidden prior?
- what consistency, recurrence, memory, preparation, and support constraints characterize them?
- which visible stochastic families are impossible under OI?

**Why this matters:** if full QM equivalence fails, `C_OI` is the natural precise answer to “what other theories does OI allow?”

### Arc C — close the quantum-representation boundary in both directions

Formalize the exact interface between the sourced rooted family and the stochastic-to-Hilbert/Born representation theorem.

Keep the result explicitly representation-level.

Then audit the converse direction:

- which finite quantum stochastic/measurement structures correspond to OI-realizable rooted families?
- is every relevant finite quantum representation realizable by an OI hidden reversible realization, or only a subclass?

**Exit condition:** the precise mathematical relation between `C_OI` and the quantum representation class is known in both directions.

### Arc D — attack physical sourcing of the quantum operational repertoire

This is likely the decisive equivalence stage.

Determine whether the physical OI architecture itself can source, rather than merely represent or assume:

- continuous coherent state mixing;
- relative phases;
- unitary control;
- Hamiltonian or continuous-time evolution where claimed;
- measurements and update rules;
- Kraus instruments;
- preparation operations;
- ancilla use and discard;
- the required closure rules across carriers.

Existing conditional results should be used as assembly theorems: once a resource is physically sourced, determine exactly what operational repertoire follows from it.

The crucial question is whether the currently missing continuous off-diagonal control resource can be derived from a deeper OI condition, or whether it is genuinely an independent empirical principle.

#### Physical lift seam: from sourced single-system control to sourced instruments and composites

Sourcing a coherent operator or control law on one visible carrier is not by itself enough to claim that OI physically supplies the full instrument or composite repertoire. After any single-system control resource is sourced, audit whether that **same physical source** survives and is compatible with:

- adjoining and discarding ancillas;
- locality / inert-spectator requirements;
- subsystem restriction and regrouping;
- composition of sourced operations;
- measurement/instrument dilation;
- the composite interfaces used by the finite operational-QM assembly theorems.

Abstract completion theorems may be used to assemble the consequences of a physically sourced resource, but they must not substitute for proving that the source itself lifts through these interfaces. In particular, do not infer “OI sources composite operational QM” merely from “OI sources one-carrier coherent control” plus an abstract availability theorem whose hypotheses have not themselves been physically sourced.

**Exit condition:** every operational-QM resource is either derived from OI, proved reducible to a smaller physical condition, or explicitly classified as additional, and any single-system source used in that derivation has been shown to lift through the instrument/composite interfaces actually required.

### Arc E — composites, locality, entanglement, and Bell structure

Single-system operational equivalence is not the end of the programme.

Audit how OI sources the composite-system structure required for genuine quantum correlations:

- tensor/composite structure;
- local operations;
- incompatible measurements;
- entanglement;
- allowed correlation sets;
- causal/locality constraints;
- Bell/CHSH behavior.

The existing Bell correction is controlling: a deterministic completion with pointwise graph-cone locality, local setting interventions, readout before the cones meet, and one setting-independent pre-setting ensemble is a local hidden-variable model and obeys CHSH <= 2.

Therefore quantum Bell correlations cannot be claimed from that local hidden completion without an additional structural ingredient or a change in one of those assumptions.

**Exit condition:** the relation between OI composite physics and the quantum correlation set is explicitly characterized, including any additional principle required to reach it.

### Arc F — final equivalence-or-classification theorem

Assemble the previous arcs into the strongest justified final statement.

**Which endpoint is live must be decidable in advance, not chosen at assembly time.** §1 records that a negative result at an intermediate bridge is not a programme failure if it sharpens the classification. That is correct, but on its own it lets every outcome be read as progress, which leaves the programme unfalsifiable at the strategic level. The endpoints are therefore governed by an explicit retirement condition, fixed here rather than after the fact:

> **F1 is retired** when any arc returns an *Independent* verdict in the sense of §6 on a resource that F1 requires — a countermodel showing the resource does not follow from the OI axioms then in force. The standing candidate is Arc D's continuous off-diagonal control: a countermodel there retires F1, and the programme commits to F2 or F3 with that resource named as an additional principle.
>
> An *Open* verdict retires nothing. A construction or formalization that fails without an impossibility theorem leaves F1 live, and recording it otherwise would be the error §6 already forbids.

Retiring F1 is a result, not a defeat: it converts the programme's endpoint from an equivalence claim to a classification with an explicitly identified selection principle, which §1 names as an acceptable terminus.

Possible endpoints are:

#### F1. Full conditional equivalence

`OI + explicitly justified physical conditions  <->  target QM`.

Every condition is named, its sourcing status is known, and the target version of QM is explicitly scoped: finite, typed, quasilocal, discrete-time/continuous-time, operational availability, and composite structure as applicable.

#### F2. Minimal extension theorem

OI does not alone force QM, but there is a small, independently meaningful set of additional physical principles that is necessary and sufficient for QM.

This remains a strong reconstruction result if the added principles are physically transparent and separately testable.

#### F3. Exact classification without uniqueness

OI admits a larger theory space. The programme characterizes that space, identifies the QM subclass, and proves which additional principles select it.

This is the correct endpoint if some quantum resources are independent of OI rather than derivable from it.

---

## 6. Decision tree for interpreting future results

For every future bridge, distinguish four outcomes.

### Derived

The desired quantum structure follows from previously accepted OI physics. This strengthens the equivalence direction.

### Conditional

The structure follows once a named additional physical condition is assumed. Record whether the condition has independent motivation and whether it is necessary, sufficient, or both.

### Independent

A countermodel shows that the structure does not follow from the current OI assumptions. This bounds the equivalence claim and identifies an additional selection principle.

### Open

The current construction or formalization fails, but there is no impossibility theorem. Do not report tooling or construction failure as mathematical independence.

These four statuses should remain separate in both audits and manuscript summaries.

---

## 7. Programme-level reporting rules

1. Do not report mathematical representability as physical availability.
2. Do not report recurrence-scale nonclassicality as accessible-time nonclassicality without an accessibility bound.
3. State preparation assumptions explicitly: hidden-prior choice and visible-root preparation are different dependencies.
4. Keep finite, typed, quasilocal, and continuous-time claims distinct.
5. Keep single-system and composite/Bell claims distinct.
6. When a resource is not derived, distinguish “not derived under current axioms” from “forbidden by OI.”
7. Prefer exact classification of the residual theory space over forcing a false equivalence claim.
8. Every final equivalence statement must identify which direction is proved and which hypotheses are load-bearing.
9. State the evidence type of every reported result: kernel-checked, exact-probe-checked, or prose. Rules 1–8 guard the scope of a claim; this one guards its standing. A prose proof is not a formalized success, and a formalization or tooling failure is not a mathematical negative — the second half of that is already §6's *Open*, and the first half is its counterpart. Where a round's positive and negative results carry different evidence types, say so in the same place they are reported, so the asymmetry is visible without reading the sources.
10. Do not treat the publication-facing corpus as the inventory of what is proved. Where the kernel carries a result at a scope no manuscript states, that is a recorded debt (§3.7), not an absence of the result — and closing it means stating the result at the scope proved, never at a stronger one.

---

## 8. Parallel research tracks outside this roadmap

This roadmap covers the **OI → QM equivalence/classification programme only**. Other major corpus programmes remain active or backlogged, but they are not prerequisites for the equivalence chain unless a later theorem explicitly connects them.

Parallel tracks include, in particular:

- gravity / G3 sourcing and the remaining locality/interacting-sector debts;
- curved-continuum or geometry reconstruction questions;
- IR Lorentz / universal-cone questions;
- full-response, memory-resummed, or related dynamical-response programmes;
- other model-specific physics programmes whose results may constrain OI but do not currently sit on the logical path from the OI observer structure to operational QM.

These tracks retain their own theorem, audit, and backlog status. Progress on them must not be counted as progress on the OI → QM equivalence chain unless an explicit bridge is proved; conversely, the equivalence programme should not silently absorb or supersede their unresolved questions.

---

## 9. Relation to existing documentation

This file is intentionally high-level.

Use the following sources for detailed status:

- `verification/README.md` — technical verification status and theorem inventory;
- `verification/coverage/LEDGER.json` — statement-by-statement proof coverage;
- `verification/CENSUS-oi-compatible-theories.md` — finite OI-compatible completion classes;
- the individual `*-AUDIT.md`, `*-RESULT.md`, and amendment files — preregistered questions and exact outcomes;
- `verification/lean-mathlib/OIBridge/` — kernel statements and their hypotheses;
- `papers/GR.md`, `papers/Main.md`, the Explainer, and book chapters — publication-facing statements under their scope guards.

`verification/ROADMAP.md` remains the historical roadmap for the original zero-import verification layer. It is not the strategic roadmap for the larger OI → QM equivalence/classification programme.

---

## 10. Current one-line programme state

At the post-#542 boundary:

**OI already has a strong finite operational completion classification and a clear quantum-representation route, but bare OI does not yet physically source the full quantum operational repertoire; the immediate task is to finish the stochastic recurrence/tightness boundary, then characterize the full OI-realizable stochastic class before returning to coherent-control sourcing and composite/Bell equivalence.**