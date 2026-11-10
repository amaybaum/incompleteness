# Reviewer guide — OI–QM preparation, selection and approximate operational equivalence

> **Draft research archive. Scientific status: UNREVIEWED; physical source gate: NOT PASSED.**
>
> This guide organizes temporary, writer-only paper analyses for critical review. It makes no claim that the new results are Lean-certified, experimentally tested, independently accepted, physically sourced, or authorized for manuscript integration. The draft PR is for **preservation and review preparation**, not approval to merge.
>
> Read [README.md](README.md) for the file-by-file source index and exact original ChatGPT Page links. The original drafts are intentionally kept intact for provenance. **Apply corrections in [04-unit2-critical-audit-v1a.md](04-unit2-critical-audit-v1a.md) before interpreting [03-unit2-nonlocal-weight-and-cone.md](03-unit2-nonlocal-weight-and-cone.md).**

## Scientific question

Can a deterministic observational-incompleteness (OI) substratum physically produce one reusable preparation–controller–measurement–record mechanism that realizes classical observations and quantum operational behavior under different legitimate measurements, with controlled approximation error and complete observable histories?

**Accountability:** [#1169](https://github.com/amaybaum/incompleteness/issues/1169) and [#1216](https://github.com/amaybaum/incompleteness/issues/1216) retain equal foundational priority. [#866](https://github.com/amaybaum/incompleteness/issues/866) owns the native preparer/controller source; [#1143](https://github.com/amaybaum/incompleteness/issues/1143) the selection/classical-preservation obligation; [#868](https://github.com/amaybaum/incompleteness/issues/868) physical pair validity and composition; [#1220](https://github.com/amaybaum/incompleteness/issues/1220) full resource accounting. #945's finite-bit repair remains a separate workstream.

The archive is **not** a claim that deterministic OI derives QM. Reversible representability of supplied output laws, physical generation of a reusable apparatus, uniform approximation of *complete histories*, and efficient classical simulation are different propositions.

## What is already accepted — not newly proved by this PR

The independently reviewed historical inputs are preserved and must not be re-labelled as new acceptance of the archived drafts:

| Existing source | Use and limitation |
| --- | --- |
| [#1169 dependency matrix](https://chatgpt.com/space/page_9580d355639c81919a21ae4d8af34201) | Source statuses for FI-1/mixing, phase, H-Bell, Born, joint states, approximation and costs; overall physical interface remains open |
| [#1143 C0/C1 selection assessment](https://chatgpt.com/space/page_91b4e980d730819182254df477ae8218) | Classical and restricted-affine countermodels defeat naive sufficiency of observational incompleteness and preparation property E; classical contexts must be preserved |
| [#1220 r1a resource contract](https://chatgpt.com/space/page_472c33bfa4fc819182fe3dd26fbea24f) | Physical resource ledger distinct from classical weak-sampler cost; efficient simulation remains undetermined |
| [Preparation-loading on main](../oi-qm-ext-1/preparation-loading.md) | Exact binary ring F, common-prior conditional loader, eight precursor constraints, counting deficit, full output and source stop |
| [Controller source-selection LEAD](../physical-controller-20261107/LEAD.md) and [CP-PREP-1](../controller-preparation-1-20261108/SELECTION.md) | Actual native physical producer, controller source and Fredkin/Toffoli-to-ring execution mapping **not sourced** |

Historical source snapshot for the original paper comparisons: `cac5d26441dd33e9348151487e4df7b547195481`. The WIP branch was created from this `main` commit. Later changes to `main` or other PRs need a fresh source/rebase assessment before integration.

## Research packets in suggested review order

| Order | Files | Proposed claim to test | Standing |
| --- | --- | --- | --- |
| 1 | [01](01-joint-milestone-bl.md), [02](02-preparation-span-rs1.md), [03](03-unit2-nonlocal-weight-and-cone.md), **[04 critical audit](04-unit2-critical-audit-v1a.md)** | Bell-local CHSH TV floor, affine-preparation span, local-content and no-signalling quantifiers. Do not claim the 41.4% local-content complement is novel. | Writer proofs only; physical nonlocal source open |
| 2 | [05](05-prep-syn1.md), [06](06-prep8.md) | A single-bit syndrome correction changes the root/interface; an eight-bit abstract SWAP/XOR factory requires clean resources and imported operations. | Conditional mathematical constructions; not native execution |
| 3 | [07](07-prep-native1.md), [08](08-prep-native2.md) | Closed-ring fixed-time and bounded passive preparation limits; conditional entropy capacity with independent versus correlated reservoirs. | Scoped ring/full-state calculations only |
| 4 | [09](09-prep-corr1.md), [10](10-prep-obs1.md), [11](11-prep-read2.md) | Actual SM ring transfers hidden information to declared records; observer-cut dependent one-tick herald, two-tick original-observer obstruction and a third-tick influence witness. | Mathematical record laws; no physically sourced herald or reusable apparatus |

**Important:** A successful conditional probability calculation is not a factory success rate. A full-state total-variation bound is not automatically an observable-history bound. A mathematical readout or hypothetical site enlargement is not a physically executable observer operation. A necessary Bell condition is not a sufficient Born or composition principle.

## Specific scientific review checklist

- [ ] **Frozen source and exact scope.** Verify the binary SM ring `F(X,Y)=(f(X) XOR Y,X)`, the visible root, all eight extra precursor constraints and modulo-`L` index assumptions (`L≥9`).
- [ ] **Mathematical correctness.** Independently verify each claimed probability, TV dual bound, capacity bound, conditional entropy inequality, locality cone, observer-history dependency and explicit countercontrol. Flag claims that repeat earlier reviewed results as corollaries, not new theorems.
- [ ] **Bell and preparation assumptions.** Separate setting independence, ontic parameter dependence, local-output conditioning, no-signalling on **complete accessible histories**, quantum-only upper bounds, and physical availability of preparations. Do not transfer a one-benchmark error `ε` to the all-preparations signalling defect `η`.
- [ ] **Apparatus source and operations.** Identify the exact native update, physically executable operations, source of clean/conditioned ancillary bits or reservoir correlation, real sensor/record, program generator, clock and renewal. Distinguish a theorem about a permutation from an implemented observation/read-write interaction.
- [ ] **Observer access and continuation.** Include input/preparer/controller/herald/failure records, all post-read accessible registers and outgoing full state. Check whether enlarging from 2 to 7 sites changes the compared theory.
- [ ] **Approximation and complexity.** Keep #1216 Level A finite-law representability separate from OI-derived Level B across sizes and adaptive settings. Charge #1220's total resource ledger; do not infer BQP/BPP or an energy/tick lower bound from Shannon entropy alone.
- [ ] **Classical-preservation negative controls.** Classical-register contexts must remain possible; C0/C1, PR/no-signalling, local CHSH and unsourced-R-Born controls remain live.
- [ ] **Evidence status and authorship.** Review each draft on its exact head and identify accepted, conditional, disproved-in-class or open propositions. A GitHub draft PR, ordinary CI pass or writer-side audit does **not** confer independent mathematical or physical acceptance.

## Decision gate after independent review

Permitted paper-review outcomes are **ACCEPT**, **ACCEPT WITH NITS**, or **REVISE** with exact file/section/assumption references. A scope-bound **UNSOURCED** physical outcome is a valid research result.

Even if the paper algebra is accepted, the specific **native physical source remains NOT PASSED** until one full prepared carrier, its readout interactions, failure/renewal and complete-history evidence are separately established under the existing issue and execution gates.

This PR must remain **draft / unmerged** pending an explicit owner integration decision. Creating or reviewing the documentation does **not** authorize native numerical/Lean execution, freeze, F/E designation, dispatch, new physical premise adoption, manuscript claims or publication. Do not modify active research branches or maintained source papers merely to make this archive easy to merge.

## Suggested next paper-only proof obligation

With the **original two-site observer cut and unchanged F**, determine whether longer native histories distinguish all full-precursor classes; prove a specified finite-horizon decoder or a scoped indistinguishability obstruction. If positive, separately source the actual physical record/register/clock and an honest heralded continuation. If negative, preserve the exact access and time scope rather than inferring a universal OI no-go.

If a fully sourced detector cannot be identified, retain **UNSOURCED** and stop. The same physical interface must be evaluated for classical contexts and for quantum approximations; no target-fitted probability or operation is an allowed substitute.
