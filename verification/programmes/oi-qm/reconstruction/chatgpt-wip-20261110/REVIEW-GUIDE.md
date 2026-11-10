# Reviewer guide — OI–QM preparation, selection and approximate operational equivalence

> **Draft research archive. Codex independent paper review: ACCEPT WITH NITS on pinned head `6879c7c023259d00d2b9a7ba152c694328d56458` (2026-11-10); physical source gate: NOT PASSED.**
>
> This guide organizes temporary, writer-only paper analyses for critical review. The writer drafts were originally unreviewed. They subsequently received a separately documented, scope-bounded Codex paper review; that review is not Lean/kernel certification, experiment, physical-source acceptance, GitHub formal review submission, or authorization for manuscript integration. The draft PR is for **preservation and review preparation**, not approval to merge.
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
| 1 | [01](01-joint-milestone-bl.md), [02](02-preparation-span-rs1.md), [03](03-unit2-nonlocal-weight-and-cone.md), **[04 critical audit](04-unit2-critical-audit-v1a.md)** | Bell-local CHSH TV floor, affine-preparation span, local-content and no-signalling quantifiers. Do not claim the 41.4% local-content complement is novel. | Codex paper review: ACCEPT for 01/02 and ACCEPT WITH NITS for combined 03/04; physical nonlocal source open |
| 2 | [05](05-prep-syn1.md), [06](06-prep8.md) | A single-bit syndrome correction changes the root/interface; an eight-bit abstract SWAP/XOR factory requires clean resources and imported operations. | Codex paper review: ACCEPT at pinned head; assumptions remain supplied, not native execution |
| 3 | [07](07-prep-native1.md), [08](08-prep-native2.md) | Closed-ring fixed-time and bounded passive preparation limits; conditional entropy capacity with independent versus correlated reservoirs. | Codex paper review: ACCEPT at pinned head; scoped ring/full-state calculations only |
| 4 | [09](09-prep-corr1.md), [10](10-prep-obs1.md), [11](11-prep-read2.md) | Actual SM ring transfers hidden information to declared records; observer-cut dependent one-tick herald, two-tick original-observer obstruction and a third-tick influence witness. | Codex paper review: ACCEPT at pinned head; no physically sourced herald or reusable apparatus |

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


## Independent paper review and forward bibliographic correction (2026-11-10)

**Review provenance:** Codex, acting as a separate non-author reviewer, inspected all eleven archival writer drafts on exact head `6879c7c023259d00d2b9a7ba152c694328d56458` and reported **ACCEPT WITH NITS** for the bounded paper arguments, with **no blocking mathematical errors**. The full off-repository reviewer report is preserved at [Codex review Page](https://chatgpt.com/space/page_2f791d4a97fc8191ade6141a5ed9bdfe). Codex reported that all eleven drafts matched their original Pages verbatim, that 13 added documentation files were scoped to this archive, and that an existing verify workflow completed successfully. This was **not submitted as a GitHub review**. The reviewer accepted PREP-READ-2's two-tick posterior bound and third-tick influence witness, with three ticks necessary but **not proved sufficient**, and PREP-8's reversible abstract construction and eight-bit capacity converse under its supplied clean auxiliaries and gates. None of this is an accepted physical apparatus.

**P3 forward correction — archived attribution only:** The historical writer-audit [04-unit2-critical-audit-v1a.md, line 21](04-unit2-critical-audit-v1a.md) incorrectly says **“Chaves et al.”** for the linked 2021 PNAS paper. **Correct attribution: Błasiak et al.** — Paweł Błasiak, Emmanuel M. Pothos, James M. Yearsley, Christoph Gallus and Ewa Borsuk, *Violations of locality and free choice are equivalent resources in Bell experiments*, PNAS 118(17), e2020569118 (2021), [DOI 10.1073/pnas.2020569118](https://doi.org/10.1073/pnas.2020569118). This was also cross-checked against [the institutional repository citation](https://openaccess.city.ac.uk/id/eprint/26021/). The archived `04` file is **not edited**, preserving its exact historical provenance; readers must use this forward correction. The cited bounded Bell local-content argument remains subject to its declared setting, response and measurement assumptions and is **not a novel OI theorem**.

**Change boundary:** The original review applies to head `6879c7c0`, not automatically to subsequent documentation commits. The forward citation/status edits in this guide are documentary; any later scientific content change requires the appropriate focused independent diff review. No fresh review verdict of the modified head is claimed.

**Unchanged hard gates:** PR #1222 stays **draft/unmerged**. The #866 physical-source gate remains **NOT PASSED / UNSOURCED**. No physics premise, native computation, Lean execution, F/E, dispatch, publication or merge is authorized by this review or erratum.

## Separate independent reviews: PREP-HIST-4 and CARD-GAUGE-1 (2026-11-10)

The first [Codex ACCEPT WITH NITS at `6879c7c0`](https://chatgpt.com/space/page_2f791d4a97fc8191ade6141a5ed9bdfe) covered only the original eleven research drafts. Two subsequent papers have received **distinct pinned independent paper reviews**:

- [12-prep-history4-and-finite-decision.md](12-prep-history4-and-finite-decision.md): [Codex ACCEPT at `4fe17de6df1e96c14e76e4018ca69bbba229a72b`](https://chatgpt.com/space/page_47a9041813248191952a4c746fb6d1d4), without required corrections; covers the c=1 three-tick ready/nonready pairing, four-tick counterexample and finite-state stopping criterion. **Five ticks necessary for a universal classifier, not proved sufficient.** The historical file remains unchanged.
- [13-cardinality-observational-equivalence.md](13-cardinality-observational-equivalence.md): [Codex ACCEPT WITH NITS at `c9f0d16c8084075cd387beff3994a2731dfb86b0`](https://chatgpt.com/space/page_af453671fa5c8191b7c9a5fced83c24a), no blocking mathematics error; covers the effective-description Halting reduction, uniformly computable normalized hidden source, complete-history product-factor equivalence, and scope-limited gauge terminology. Three nonblocking clarifications were subsequently applied to the paper: (i) **common operational dictionary** for preparations/protocols/records, with model-specific microscopic carriers, dynamics and implementations; (ii) a **common-menu two-tick distinguisher** comparing swap `(v,h)→(h,v)` and three-cycle `(v,h,k)→(h,k,v)`, with visible second-reading TV = 1/2 when v=0 and h,k are independent fair bits; (iii) proper PREP-HIST-4 review metadata. This later textual revision still needs **focused diff verification**; the previous verdict remains pinned to `c9f0d16c`.

**Forward review status:** Archive documents created before the corresponding reviews may contain historically accurate "review pending" headers. Read the newer pinned reviewer reports and this guide for current standing. Do not silently rewrite the first eleven reviewed drafts or the separately accepted file 12.

### #1169 dependency-matrix amendment (reviewed bounded evidence, physical sourcing open)

| Field | Precise entry |
| --- | --- |
| Dependency / node | **CARD-OBS — observer-relative nonidentifiability of total carrier cardinality under normalized, exactly decoupled extensions** |
| Mathematical status | **ACCEPT WITH NITS**, pinned to CARD-GAUGE-1 at `c9f0d16c`; corrections in subsequent paper WIP |
| Premises | Shared preparation-label/protocol-label/complete-accessible-record dictionary; every admitted protocol acts only on the base factor; any added factor has a **normalized independent** source and **exactly decoupled reversible** dynamics |
| Consequence | Finite, countably infinite and uncountably infinite complete carriers can generate **identical complete accessible-history measures** for every admitted finite/adaptive protocol; total carrier cardinality is not identified by that fixed interface |
| Independent control | **CARD-COMP** effective-description undecidability is a distinct result, **not a premise** of CARD-OBS |
| Limits / open | Interacting deep-sector equivalence; resource-sensitive comparison; physical availability of observer/controller/readout; Born, Bell, compositional quantum histories and uniform scalable approximation all **OPEN / UNSOURCED** |
| Relationship to existing OI | Existing finite [Substratum Theorem 24(iii)](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md) is not silently extended to an infinite quantum-channel theorem; finite A1 and PREP-HIST recurrence/stopping proofs keep their original finite premises |

**Terminology guard:** Use *observer-relative operational equivalence* or *stable equivalence under decoupled hidden-factor enlargement*, rather than claiming finite-to-infinite carrier changes are automorphisms in the existing gauge group. The explicit two-tick coupled-sector countercontrol shows why the qualifier matters.

Neither paper review closes the #866 native physical-source gate, grants experimental execution, validates a quantum-operational construction or authorizes a merge. #1169 and #1216 remain equally prioritized; the #1220 physical/algorithmic resource ledger remains separate.

## Independent ACCEPT — INT-FACTOR-1 interacting hidden sector at `1736a596`

[14-interacting-hidden-factor.md](14-interacting-hidden-factor.md) received its own **[independent Codex ACCEPT at immutable `1736a59637ae4c1f2ed8c39e48ab3282e53cc8d0`](https://chatgpt.com/space/page_b4f63a8bd3a88191a1e9318ec0e3577f)** for the factor theorem, explicit reversible witness, order-four exclusion and TV=1 enlarged-access countercontrol. This is separate from the accepted CARD-GAUGE-1 decoupled-extension argument, and is **not** a new physical theory or an already sourced SM-ring operation.

**Proposed mathematical statements to inspect:**

- **INT-FACT:** For a shared preparation/protocol/complete-record dictionary, a surjective factor map `q:S'→S` that pushes forward all prepared laws and intertwines the deterministic updates, every *admitted* reversible control and every accessible record is **sufficient** to make all fixed/adaptive finite complete-history laws equal. It is not claimed necessary.
- **INT-BIT:** With base swap `T(v,r)=(r,v)`, the three-bit reversible update `T'(v,h,k)=(h⊕k,k,k⊕v)` and `q(v,h,k)=(v,h⊕k)`, prepared fair independent h,k and common visible-flip controls, the entire admitted visible histories agree exactly. In original coordinates, the hidden k both affects visible v' and is changed by visible v.
- **INT-ORD:** `T'^4=id` but `T'^2≠id`; the base T and any independent *one-bit* spectator permutation have order dividing two, so the extension cannot be conjugate to that restricted trivial product. This does not exclude other representations or guarantee physical sourcing.
- **INT-ACCESS:** Adding the same labelled hidden-k toggle to both protocol dictionaries, implemented as identity on base and k-flip on extended model, produces a later visible read of p versus p⊕1 after two ticks. This is a **different admitted protocol family**, not a contradiction of INT-FACT.

**Interpretive correction retained from the review:** In factor coordinates `r=h⊕k`, the update is `(v,r,k)→(r,v,k⊕v)`. Thus the **observable two-bit factor is autonomous** and the hidden fibre is nontrivially driven by it. Two-way dependence of the original `v,k` coordinates is not evidence that the erased fibre feeds information back into that autonomous factor. The order-four exclusion remains valid relative to the same two-bit base times an independent one-bit permutation.

**Preliminary native SM diagnostic:** On the canonical-root class at `c=0`, the all-zero initial ring and the ring changed only at `X₂=1` have identical initial two-site/two-slice readouts. Under the actual SM rule they produce different next observed current pairs `(0,0)` and `(1,1)`. Therefore the **raw two-site projection alone is not an autonomous deterministic factor** on that class. This does **not** rule out a larger factor carrying hidden predictive state, nor does it source that factor's preparations, controls, records or apparatus. The required follow-up is source-qualified, not an ad hoc toy-gate substitution.

**Source-control classification:** The classical reversible toy map is mathematically explicit and couples coordinates, but **has not been sourced as a physical transition, preparation, detector, clock or quantum operation in the native SM ring**. [#866](https://github.com/amaybaum/incompleteness/issues/866) remains NOT PASSED; #1169/#1216 physics and source mechanism obligations remain OPEN. The new packet is **not** an independent review or acceptance of itself. Reviewer should compare [Substratum §4 Theorem 24](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md) and [CP-PREP-1](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/verification/programmes/oi-qm/reconstruction/controller-preparation-1-20261108/SELECTION.md) before proposing further physical interpretations.

**#1216 crosswalk:** If the base complete-history law were already within ε of a target family uniformly for admitted protocols/horizons, the exact factor equivalent extension would inherit **the same ε**, since its law is identical. This algebraic preservation does not generate quantum coverage or certify a scalable OI-derived approximation mechanism. #1220 resource costs need a separate comparison; one additional microscopic bit is not a free resource by default.

**Completed separate review gates:** Codex independently [ACCEPTED the focused CARD-GAUGE-1 correction diff `c9f0d16c→cc819d5d`](https://chatgpt.com/space/page_b4f63a8bd3a88191a1e9318ec0e3577f), resolving all three P3 nits; the corrected CARD blob remains unchanged at `1736a596`. Codex separately [ACCEPTED INT-FACTOR-1 at `1736a596`](https://chatgpt.com/space/page_b4f63a8bd3a88191a1e9318ec0e3577f). These two verdicts do not certify future documentation changes, physical sourcing, OI→QM selection or any resource-cost equivalence. A separate owner decision remains necessary before integration.

## Independent ACCEPT WITH NITS — NATIVE-PRED-1 at `95cead38`

[15-native-predictive-factor-bound.md](15-native-predictive-factor-bound.md) received a **separate [independent Codex ACCEPT WITH NITS at immutable `95cead387e119b31f6b7c069d9d430693e4a434c`](https://chatgpt.com/space/page_fa9ae3c07c208191bdf87950b734488b)**. The mathematical paper passed **without required proof correction**. The only nonblocking nits were documentary: the README must distinguish the accepted finite classical interacting-factor example from *physically sourced* interacting equivalence, and classify U_c as **source-pinned mathematical realization data**, not a physically produced initial distribution. The paper itself and all earlier research papers remain unchanged.

**Independently accepted scoped calculation:** For the unchanged reversible ring `F(X,Y)=(f(X)⊕Y,X)`, original two-site two-slice readout and canonical-root U_c (c∈{0,1}), let first and second post-root current read pairs be (A0,A1) and (C0,C1). Show the transformed four bits `(A0,A1⊕c,C0,C1⊕A0)` are mutually independent with Bernoulli parameters `(1/2,3/4,1/2,3/4)`. All **16** two-update output histories consequently have positive probability on the *same initial visible root*, with entropy `2+2h₂(1/4)≈3.622556` bits under U_c.

**Autonomous-factor consequence:** Any deterministic passive state factor `q:S_L→Q` with `q∘F=F_Q∘q` and `o=o_Q∘q` must distinguish all 16 histories, hence `|q(b_c)|≥16` for either c, and ≥32 over the two distinguishable root sets. A fixed-length binary factor label needs at least four bits of predictive capacity over a single visible root; **this is not physical apparatus memory or energy cost**.

**Existing theorem versus new bound:** The existence of the canonical *future-trace quotient* is already contained in [Substratum Proposition 24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md). Its mathematical state is not an executable readout, and its physical controller/intervention intertwinement is **not supplied**. Under the conditioned ready source η_c, only two candidate second-output histories occur; the 16-way result is **specific to canonical U_c**.

**Source and falsifiers:** The raw two-site projection is already non-autonomous (separate Codex native source check). Evaluate any later native q proposal against both the one-step ambiguity and the 16-way two-step calculation. Do not assume the full predictive quotient is small or physically sourced. CP-PREP-1's original native physical ready/request producer, measurement/clock/record apparatus and renewal are still **NOT PASSED**, and no coherent quantum control, Bell pair, Born selection or #1216 Level-B approximation is inferred.

**Independent review completed:** Codex checked full joint independence (including L=9 modular indices), all 16 positive-probability histories, entropy, ≥16 per-root and ≥32 across-roots labels, the η_c contrast and existing Substratum Proposition 24.4 attribution. [Verdict: ACCEPT WITH NITS at `95cead38`](https://chatgpt.com/space/page_fa9ae3c07c208191bdf87950b734488b); **no mathematical correction**. The present README/guide documentation change is later than the reviewed head and is an author-side clarification, not a new independently reviewed checkpoint. No numerical, Lean, physical or scientific execution took place.

## NATIVE-FACTOR-SRC-1: actual native factor candidates and source stop (NEW, review pending)

[16-native-factor-source-screen.md](16-native-factor-source-screen.md) is **new mathematical/source research, independent review PENDING**, and is distinct from the accepted [NATIVE-PRED-1 at `95cead38`](https://chatgpt.com/space/page_fa9ae3c07c208191bdf87950b734488b).

**Candidate A: finite-horizon native causal cone.** For native `F(X,Y)=(f(X)⊕Y,X)` on a binary ring L≥9 and original two-site/two-slice observer, the first T observations depend only on initial X in `[-T,1+2T]` and Y in `[-(T−1),1+2(T−1)]` (mod L). For T=2 this is a **13-bit** coordinate snapshot (eight X and five Y sites), nine bits unconstrained under a fixed canonical root U_c. It determines the complete two-update *passive* record word but is **not** itself an autonomous factor: a root-preserving X_(−3) toggle leaves q₂ unchanged yet changes the q₂-projected next state at A_(−2). No physical extra-site observation port is sourced.

**Candidate B: passive future-trace quotient.** The already-established finite-permutation quotient [Substratum Proposition 24.4](https://github.com/amaybaum/incompleteness/blob/cac5d26441dd33e9348151487e4df7b547195481/papers/Substratum.md) is an exact deterministic passive autonomous factor. It has at least the previously accepted 16 labels per root under U_c, but actual quotient cardinality, properness, locality, physical accessibility and intertwinement with controllers remain OPEN. Its state cannot be calculated from the constant initial two-site root observation.

**Candidate C: accessible-history Bayesian belief filter.** Standard filtering of the complete hidden ring using the supplied mathematical prior U_c and successive passive outcomes gives an exact *classical stochastic predictive state* `ρ_t`. This is not a deterministic microscopic q-factor or a physically sourced memory/computational device; do not infer quantum-state kinematics.

**New scoped obstruction:** Any nonempty proper subset I of ring sites retaining both X and Y only on I fails autonomous one-step intertwining on the full ring: some i∈I has i−1∉I, and flipping the unseen initial X_(i−1) changes next A_i. If I contains observed sites 0 and 1, the two witnesses can also share a canonical visible root. This rules out **all proper raw coordinate-site patches**, *not* arbitrary nonlinear/aggregated factors.

**Actual physical-source screen:** CP-PREP-1 #866 did not supply a ready/request producer, physical clock/readout/record apparatus, or an admitted native control operator. The 13-bit cone is not an available detector; the future-trace quotient is not an actual readout; the Bayesian filter is not a supplied device. **Source disposition: STOPPED — NOT PASSED / UNSOURCED**, without asserting a mathematical no-go for all possible native factors.

**Independent review required:** (1) verify cone dependency induction and T=2 count for all L≥9; (2) reproduce root-compatible q₂ nonautonomy witness; (3) check cyclic predecessor boundary proof for all proper I and exact scope; (4) preserve prior attribution for q∞; (5) check Bayesian filtering normalization and nondisturbing-passive limitation; (6) confirm first missing physical source and no false upgrade to OI–QM soundness/completeness. Reviewer to pin **exact Git head** and issue ACCEPT / ACCEPT WITH NITS / REVISE. No native numerical, Lean, F/E or dispatch is authorized by this packet.

## Decision gate after independent review

Permitted paper-review outcomes are **ACCEPT**, **ACCEPT WITH NITS**, or **REVISE** with exact file/section/assumption references. A scope-bound **UNSOURCED** physical outcome is a valid research result.

Even if the paper algebra is accepted, the specific **native physical source remains NOT PASSED** until one full prepared carrier, its readout interactions, failure/renewal and complete-history evidence are separately established under the existing issue and execution gates.

This PR must remain **draft / unmerged** pending an explicit owner integration decision. Creating or reviewing the documentation does **not** authorize native numerical/Lean execution, freeze, F/E designation, dispatch, new physical premise adoption, manuscript claims or publication. Do not modify active research branches or maintained source papers merely to make this archive easy to merge.

## Suggested next paper-only proof obligation

With the **original two-site observer cut and unchanged F**, determine whether longer native histories distinguish all full-precursor classes; prove a specified finite-horizon decoder or a scoped indistinguishability obstruction. If positive, separately source the actual physical record/register/clock and an honest heralded continuation. If negative, preserve the exact access and time scope rather than inferring a universal OI no-go.

If a fully sourced detector cannot be identified, retain **UNSOURCED** and stop. The same physical interface must be evaluated for classical contexts and for quantum approximations; no target-fitted probability or operation is an allowed substitute.
