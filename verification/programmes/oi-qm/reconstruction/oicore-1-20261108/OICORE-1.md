# OICORE-1: faithfulness of `OICore` to observational incompleteness, candidate strengthenings, and the backward dependency map (r6)

## 0. Standing and scope

**What this is.**

- A paper-only, read-only foundational audit under #1169, authorized by the owner at #1169 c.6724391385 (amaybaum, 2026-11-08T17:02:10Z).
- It is model-written and independently model-reviewed: one reviewer, five rounds, ending in ACCEPT at r6 with one optional nit,
  R6-n1, which this text applies (§9; review texts in `review/`; trail recorded at #1169 c.6725037236). That is not human verification.
  Every statement keeps the layer and class it carries below; the review promotes none of them.
- It adopts no premise, edits nothing, builds no Lean, runs no scientific computation, and changes no scientific status (§A.45 rule 1).
- It is kept separate from M-ARC, Q-C2-1, Q-C2-2 and the drive-phase check.

**Revisions.**

| Revision | File | sha256 | Notes |
|---|---|---|---|
| r1 | not on `main` | `ed828f1607c15e7c208cf4518c88093d58b7915202b01b98fae0b267d5788da6` | reviewed in `review/REVIEW-OICORE-1.md`: REVISE, B1–B6, N1–N12 |
| r2 | not on `main` | `dbeca5b4cb68bd5a5d598e20878bd3f2ef3aad57914c114e9f73e7afdb56477d` | final r2. The reviewer saw an intermediate state, `6e70e3cf…`. Not reviewed |
| r3 | not on `main` | `93156b287c3349be7e3fead75726609224ea3fdd3cf9f61fcec9aab34e585d78` | folds in B1–B6, N1–N12, §8 and the four distinctions. Reviewed in `review/REVIEW-OICORE-1-r3.md` (`5912885b…`): REVISE, R3-B1–B6, R3-n1–n8 |
| r4 | not on `main` | `e090309cfc87e761d643a8691533d20cabeb656536645d62dbec8e19f3b6267b` | applies R3-B1–B6 and R3-n1–n8. Reviewed in `review/REVIEW-OICORE-1-r4.md` (`8ab55e2d…`): REVISE (minor), R4-1–R4-6 |
| r5 | not on `main` | `9c273525600aef5cbf40fa8a110080750cd18e1f2629cabb95bc6ce781d3738a` | applies R4-1–R4-6. Accepted with two nits in `review/REVIEW-OICORE-1-r5.md` (`365c0be4…`) |
| r6 | not on `main` | `ec7966c955a17043c85f85be3f2bbe178049ed3a0f4286e0b61e3bd1c4aa078b` | applies R5-n1 and R5-n2 only. Dispositions are in §9.4. Reviewed in `review/REVIEW-OICORE-1-r6.md` (`d02b5310…`): ACCEPT, with optional nit R6-n1 |
| final | this file | `9b82ecc25dbf7ce4bfd5e40ed313d22af45a4bd175a31ff48b06955a5bda5970` before the landing edits | r6 with R6-n1 applied: the §8.7(e) table header reads "Route" for "ε-route", and §8.10 reads "Three routes" for "Three ε-routes". The landing edits state the review status (§0) and replace or trace session-local references (§0, the §3.2 ACC-U cell, §7, the §9.1 B6 row); nothing else changes |

**Snapshot.**

- `origin/main` = `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`, fetched without `--depth`, gc or prune.
- The sources were read from a `git archive` extract of that commit.
- Line numbers refer to that commit. Lean paths are under `verification/lean-mathlib/OIBridge/`.
- `R/` = `verification/programmes/oi-qm/reconstruction/`.

**Questions answered (verbatim).**

- *Central* (c.6724391385): "Does the original principle of observational incompleteness contain independently justified physical
  constraints that are missing or weakened in its current formalization, and could those constraints help explain quantum behavior?"
- *Hierarchy* (#1169 c.6724620166, amaybaum, 2026-11-08T17:22:38Z): "Which added properties can be traced back to observational
  incompleteness itself, rather than to independent assumptions about the available operations?" Also: "Do any of these strengthened
  formulations capture physical consequences of incomplete observation that the original `OICore` misses, without assuming the quantum
  behavior we want to derive?"
- *Mixing* (c.6724668737, 17:27:00Z): "Can incomplete observation, together with native reversible dynamics and record-dependent access,
  produce the effective coherent mixing that OIPlusMin currently assumes?"
- *Synthesis* (c.6724721208, 17:31:47Z): "whether the approximate-versus-exact distinction exposes a genuinely new physical route, or
  merely shifts the missing assumption into an approximation or limiting procedure."
- *Separation* (c.6724832474, 17:42:02Z): "The OICORE-1 revisions remain separate".

**Boundaries.**

- c.6724391385: recover the strongest defensible meaning; separate original content from new hypotheses; give explicit proof dependencies;
  preserve negative results; prefer the smallest meaningful strengthening.
- Witness principle (c.6723571280).
- ADA ledger (c.6723491138).

**Four distinctions kept throughout (c.6724721208).**

- **D1, exact vs approximate.** Every no-go is tagged *exact*, *approx* or *both*. An exact-control obstruction is never used against an
  ε-level construction.
- **D2, restriction vs constructive resource.** Restrictions are assessed together with OI's existence principles (Axioms 1–2, C1–C4, and
  the law-level realization data).
- **D3, accessibility vs certification.** ACC-U (accessible but uncertifiable) and ACC-R4 / M-INACC (inaccessible functional) are separate
  rows.
- **D4, classical vs quantum.** Reading hidden information is not, by itself, evidence of quantum behaviour.

**Evidence layers.**

| Layer | Meaning |
|---|---|
| **K** | a kernel statement read from the Lean source; proofs read only where a dependency matters |
| **P** | a paper proof on `main` |
| **W** | a reconstruction record on `main` (AP1, M1D, M2D, QA, MI-R) |
| **D** | an off-`main` draft (ARP drafts and reviews); used only where named, and labelled each time |
| **A** | an audit derivation in this file, at the paper layer |
| **L** | external standard mathematics or literature |

On W:

- AP1, M1D and M2D describe themselves as paper-only research units that adopt nothing (for example M2D:3-15). MI-R is marked
  "WIP / UNVERIFIED" (MI-R:3-7).
- All are model-reviewed only. Under §A.46 item 7 none is used as an established premise. A W input makes a conclusion conditional.

**Derivability classes.**

| Class | Meaning |
|---|---|
| **EI** | established implication, dependency named |
| **CI** | conditional implication |
| **CX** | *proved unable*: excluded within a stated class |
| **CX†** | excluded *if* the candidate is consistent with the core; that consistency is open, so the exclusion may be vacuous (R4-1) |
| **NI-M** | not implied, by Lemma M (§3.1) with an exhibited witness |
| **NI-W** | not implied: a witness satisfies the candidate and lacks the property. The candidate does *not* exclude the property (R3-B2) |
| **NS** | *not shown*: no implication and no witness |
| **OC** | open conjecture |
| **n/e** | not expressible as a condition on `T` |

**Controls.** The author control `c1_core_access.py` enumerates the core's eight states. It is a control, not evidence, and it is not
landed: every statement it touches has a kernel anchor (§1.1). The reviewer's RC-1 control is no longer cited (R3-n8).

## 1. Faithfulness

### 1.1 What `OICore` actually requires

`OICore T := RealizesSealedOICore T` (CompletedOI.lean:96). The latter is a six-fold conjunction (OIRealization.lean:234-242).

**F1 [A over K; confirmed by review]. `OICore T ⟺ Avail_T(σ̂) ∧ Avail_T(τ̂)`.**

`σ̂` and `τ̂` are the transported permutation channels at level 4 (:236-237).

- The → direction is projection.
- For ←, the other four conjuncts hold for every `T`:
  - `CoreC1C4` is a closed proposition (IndependenceCensus.lean:187-200).
  - Conjunct 6 does not mention `T`; `realizedFold` (:177-179) is proved by `realizedFold_diagonal` (:213).
  - Conjunct 4 holds by `readVisible_eq_localLuders` with `readout_is_localLuders` (OperationalAssembly.lean:658-660).
  - Conjunct 5 holds by `readVisible_family_eq` and `readout_relabel_available` (OIRealization.lean:140-157).
- The kernel's falsifier `label_not_oiCore` fails at `τ̂` (PassiveIndependence.lean:237-238).

**F2 [A].** The core is upward-closed in the level-4 availabilities and carries no upper bound. The corpus says the same: CompletedOI.lean:523-526
and GR:228. Classification: ELABORATING.

**F3, recast (B5) [K lemmas composed by A].**

- (a) *The core's process satisfies ACC-R2.* In every core-realizing theory, read → `σ̂` → read determines the full core state
  (`core_observer_minimal`, IndependenceCensus.lean:150; control C-B). `σ` is the law's passive step, and `v_{t+1} = h_t` is C1 by design
  (IndependenceCensus.lean:25-26; Main:74). This is hidden information reaching `V` *through `φ`*. It is OI's own meaning, not a defect.
- (b) *As a constraint on `T`, R2 is absent.* Any theory may make available non-law operations that read `h` with no law step. The
  relabelling `g_hb` (`h ↔ b`) is available in every theory with control (`relabel_available`, OIRealization.lean:245-249). It is also
  available in the classical theories `permTheory (Fin 2)` (`permTheory_relabel`, SubstratumInterfaceAudit.lean:730-736) and `diagTheory`,
  whose availability is every diagonal-preserving CP family (DiagonalTheory.lean:246-248). So zero-step access is not a quantum feature
  (D4).
- (c) *R3 also fails for `T`.* Records are external outcome labels (F4).

**F4 [K]. The operational setting is an open-system, external-observer setting.**

`FiniteOperationalTheory` (OperationalAssembly.lean:594-653) has:

- a uniformly mixed ancilla of every size (`prepAvail_uniform`, :630);
- classical outcome labels, external and unbounded under `availExt_bind` (:617-623);
- arbitrary complex-linear families;
- no `S`, no `φ`, and no map from operations to a fixed law.

Its only faithful feature is that the maximally mixed preparation is the only one assumed (:628-630), matching Lemma 3's measure.

### 1.2 Principle-by-principle table

Classes: **E** = expressed as a constraint on `T`; **W1** = kept as a property of the one fixed core process, reducing on `T` to F1;
**W2** = weakened by idealization; **X** = absent.

| # | Principle (file:line) | Strongest defensible reading (*interp.* marked) | OICore / setting | Class |
|---|---|---|---|---|
| P1 | Axiom 1 (Main:38): "embedded representation occurs"; the proper-part decomposition is "constitutive". The book states the thin form, "there is differentiated content" (ch01:22 = FULL:357) | Main: a locus registers a distinction against a remainder, and the registering is part of `S`. Main:40 says the thin reading needs embeddedness as a third axiom; ch01:24 calls the difference presentational | `∃ p q, vis p ≠ vis q` on the core (OIRealization.lean:300); records of `T` external (F4) | W1; embedding of records X |
| P2 | Axiom 2, recurrence (Main:38) | differentiation recurs | `swapFn (swapFn p) = p` (:299) | W1 |
| P3 | Definition `(S, φ, V)` (Main:44; ch01:26 = FULL:361) | **FIX**: one law `φ` on `S`, and `V ⊊ S` is moved by it. That observer interventions are themselves steps of `φ` is *interp.*. Main:46 argues time-homogeneity, and the corpus also uses "setting interventions" (Main:22) and a stated phase "intervention principle" (Main:590; GR:260) | core: one bijection plus one control; `T`: no `φ` | W1 core; FIX X |
| P4 | outcomes "of interactions with a system not wholly under the observer's control" (Main:34; ch01:20 = FULL:355) | Weak: outcomes are not chosen. A stronger reading (*interp.*) restricts which dynamics the observer can choose. Full unitary availability does not contradict the weak reading, since outcomes stay unchosen | weak: any nontrivial instrument | weak E; strong X |
| P5 | Lemma 1 (Main:48; ch01:30 = FULL:365); total finiteness is "a physical posit … empirically motivated" (Main:62) | **FIN**: the observer and its records are finite parts of a finite `S` | core 4/8; `T`: unbounded ancillas and records | W1 core; W2 for `T` |
| P6 | Lemma 2 (Main:50; ch01:36 = FULL:371) | **ACC-R2**: `V` registers only its own configuration, and `H` reaches `V` only through `φ`. **ACC-R3**: `V` cannot represent the whole (Main:40; ch01:213 = FULL:548) | the core process satisfies R2 (F3a); `T` is unrestricted (F3b) | R2 W1 (process), X (`T`); R3 X |
| P7 | "beyond causal reach … permanently hidden" (Main:28; GR:18; ch01:47 = FULL:382) | **ACC-R1**: causal inaccessibility | no causal structure | X |
| P8 | Lemma 3 (Main:56, 62; ch01:38-41 = FULL:373-376) | **RET-w**: records are never erased; bijective `φ` | core bijection, invariant counting measure (:296-298) | W1 core; X for `T` |
| P9 | the measure as a realization datum (Main:56, 60) | counting measure as the default; `μ_H` is free realization data | `prepAvail_uniform` | E (setting) |
| P10 | C1–C4 (Main:74-80) | diagnostics of a realization (Main:72), with existence content | hold of the fixed core | W1 |
| P11 | "covers every registering locus" (Main:38); partition-relativity (Main:86) | uniform rules for every locus (*interp.*) | `EmbeddedObservation` exists, but not in the core | X (core) |
| P12 | C2-structural (Main:76) | RET-w at the coarse-grained level | `v_{t+2} = v_t` | W1 |

**Verdict.** The *existence* content is kept, as properties of one witness process (`sealedCore_is_finiteOI`, OIRealization.lean:305). The
restrictive content is absent as constraints on `T`: FIX, ACC-R1–R3, FIN for records, and RET for `T`.

**Consistency finding (record only, for a later authorized correction).** Main:38 gives the perspectival Axiom 1. ch01:22 gives the thin one.

### 1.3 Work done by the core in the main theorems [K]

| Theorem | → | ← |
|---|---|---|
| `finite_horizon_equivalence` (Equivalence.lean:462-468; imports `EquivalenceChain`, `FiniteEntropy` only, :43-44) | core not used | same |
| `oiPlus_iff_qm` (CompletedOI.lean:440) | discarded (`obtain ⟨-, …⟩`, :424) | produced from control (:433) |
| `completedOI_iff_physical` (:110-112) | redundant | from control |
| `general_characterization`, `main_result` (GeneralCarrier.lean:107-110, 188) | no OI clause on general carriers | — |
| `oi_compatible_iff` (:177-179), `oi_compatible_classification` (:168-173) | binders `_hoi`, `_` unused. CONFIRMING: the leading underscore is Lean's own signal, and GeneralCarrier.lean:165-167 and GR:228 already say this (N1) | control ⇒ core |
| `oiPlusMin_iff_qm` (MinimalRepertoire.lean:569) | no OI object in either direction | — |
| `substratum_plus_control_qm` (StructuralClosure.lean:414-417) | `ExtendsSubstratum` bound anonymously, unused | `fullClass` |
| `oi_alone_not_qm` (GeneralCarrier.lean:160-163) | the core appears only as the insufficient hypothesis | — |

## 2. Candidate constraints

The "Formal on `T`" column states each candidate as a condition on `FiniteOperationalTheory (Fin 2)` where one exists (B1). ADA tags:
**nat**; **emp**; **imp** (an imported mathematical or modelling assumption); **ext** (a proposed extension; N5).

| ID | Candidate; source | Type | ADA | Formal on `T` |
|---|---|---|---|---|
| FIX | one law for all operations (Main:44, 46, 582; Intro:129) | C (*interp.* for interventions, N3) | nat | n/e. **Shadow FIX_op**: `T ⊆ permTheory (Fin 2)` (physical carrier, no phase intervention). With the phase intervention: `T ⊆ genTheory substratumClass` |
| ACC-R2 | Main:50 | C | nat | **ACC_op**: every relabelling `g` of `Core` whose transported channel is available at level 4 lies in ⟨σ, τ⟩ = {id, σ, τ, στ} (downward-closed; R3-B1). A predicate-level dense form is **not stated** |
| ACC-R1, R3 | Main:28, 40 | C | nat | R1 n/e (no causal structure). R3 unsatisfiable by any core-realizer (F3a, F4) |
| ACC-R4 = M-INACC | M2D:114-117 | N | ext | n/e (an ontic functional of an encoded identification) |
| ACC-U (owner's route) | c.6723889799: "accessible but uncertifiable functionals … requiring an observer to certify an operation is stronger than requiring the observer to experience its measurable consequences" | **removal of an imported assumption**: CERT's negation, keeping access | — (removal) | n/e (the encoded framework of M2D Theorem NC) |
| FIN | Main:48, 62 | C | nat (posit) | for records: unsatisfiable (F4). **FIN_op**: at each level, the available unit conjugations are countable up to scalar |
| RET-w | Main:62, 76 | C | nat | automatic under bijectivity; no `T`-content |
| RET-s (P1, terminal registration) | AP1 SA-1(b); AP1:338-343 | N | imp (idealization, below recurrence) | n/e (concerns `(S, φ)`) |
| DIST | Main:34, 48 | C (weak) | nat | non-discriminating; no constraint |
| CERT (spanning certification) | M2D:483-497 | N | imp (a framework requirement of Theorem NC) | n/e (constrains operational equivalence) |
| CTRL | GR:262; Main:590 ("an empirical controllability resource") | N | emp + imp | `HasCompositeUnitaryControl` (upward-closed) |
| EMB | EmbeddedObservation.lean:123; *interp.* of Main:38, 86 | N in form | imp, with nat motivation | `EmbeddedObservation` (existence of a family) |

**Existence principles (D2).** Axioms 1–2 and C1, C3, C4 are existence principles. In `T` they appear only as F1's two availabilities. At law
level, OI's existence content is realization data: every finite stochastic law has a reversible realization (Main:22; `S_imp_D`), and
`(φ, μ_H)` are free data (Main:60).

## 3. Derivability

### 3.1 Lemma M (recast, B1)

**Lemma I (intersection) [A, paper].** The pointwise intersection `T₁ ⊓ T₂` of two `FiniteOperationalTheory A` (intersecting `avail`,
`availExt` and `prepAvail`, with readout `localLuders`) is a `FiniteOperationalTheory A`.

*Proof.*

- Every field other than the readout is a Horn-type closure rule (OperationalAssembly.lean:601-653). Each holds in the intersection because
  it holds in both components. These are `avail_id`, the two coarse-grainings, `availExt_bind`, `prepAvail_uniform`, `prepAvail_post` and
  `prepAvail_discard`.
- `readout_is_localLuders` makes both readouts equal to `localLuders`, so `readout_avail` and `readout_local` hold. ∎

**Lemma M [A over K; on `FiniteOperationalTheory (Fin 2)`].** Let `C` be *downward-closed*: preserved under shrinking `avail`, `availExt`
and `prepAvail`. If some core-realizer `T₁` satisfies `C`, then `OICore ∧ C` implies neither `HasCompositeUnitaryControl`, nor exact QM,
nor `DenseUnitaryControl`. All three are statements on the `Fin 2` system carrier, every ancilla level (DiscreteCompletion.lean:45-48;
R3-n7).

*Proof.*

1. Take `T₀ := permTheory (Fin 2) ⊓ T₁`.
2. `T₀` realizes the core: by F1 it needs only `σ̂` and `τ̂`, which are available in both (`permTheory_realizesSealedOICore`,
   SubstratumInterfaceAudit.lean:741).
3. `T₀ ⊆ T₁`, so `T₀` satisfies `C`.
4. `T₀ ⊆ permTheory`. Control and dense control are both upward-closed, so `T₀` has neither, by `permTheory_not_control` (:708) and
   `permTheory_dense_ceiling` (FrozenSourcing.lean:187-188).
5. QM requires control (`physical_of_exactAll`). ∎

*Dependencies.* Lemma I (A), and the K lemmas cited, which are kernel-only under R7-SUB/R7-SRCP (#1188). The lemma is used here as a kernel
statement, and nothing about OI generally is broadened.

*Scope (B4c).* The lemma covers restrictions **alone**, with the core. It says nothing about `E ∧ R` for an existence-type `E` that `T₀` may
lose. A downward-closed `R` can cut away the control-lacking models of `E`, so restrictions *can* be active ingredients jointly with
existence principles.

*Applicability.* Lemma M applies only where some core-realizer satisfies `C`:

- **FIX_op**: witness `permTheory` itself.
- **FIN_op**: witness `permTheory`. Its conjugations are by scaled partial permutations, so countable up to scalar [A].
- **ACC_op**: no witness is exhibited. `permTheory` and `diagTheory` both make `g_hb` available (F3b), so **Lemma M is not used for
  ACC** (B1c). No core-realizing theory satisfying ACC_op has been exhibited at all. Its consistency with `OICore` is open (OICORE-F2).

### 3.2 Derivability by candidate

Properties: validity (V), inert spectators (I), control exact (iv) and dense (iv-ε), closure and seam (Cl/L1), complex kinematics (ℂ), a
non-monomial coherent operation (Coh), contextuality or Bell violation (Ctx).

| Candidate | V | I | iv (exact) | iv-ε (dense) | Cl/L1 | Coh, Ctx |
|---|---|---|---|---|---|---|
| FIX_op | **EI**: `permTheory` has reversible implementation locality (`permTheory_sourcedOI`, SubstratumInterfaceAudit.lean:660), so validity holds (`validity_of_implementationLocality`), and V is downward-closed [A over K] | NS (I is not downward-closed) | **CX**: `T ⊆ permTheory` and `permTheory_not_control` [K]. Containment of the FIX apparatus is AP1 Lemma 2 (AP1:153-163) [W, re-derived A]: generators are permutation matrices, fresh fixed-law cells are diagonal preparations, and discard and conditioning are scaled-partial-permutation sums, so the apparatus's families are instrument-realized by `permClass`, and `permTheory = genTheory permClass` | **CX**: `permTheory_dense_ceiling` [K on the `Fin 2` system carrier, every ancilla level]. A carrier-general form via `NonnegBounded` is A (R3-B3) | NS for `T` (`permTheory` itself has EMB) | CX: no quarter phase (`permTheory_not_phasesAvailable`, :670) |
| FIX with phase intervention | as above | NS | **CX on `Fin 2` only** (`substratumGen_not_control`, StructuralClosure.lean:348). Not extended to general carriers: that would broaden the two-state result (#1188; N3) | A: substratum operators are monomial, and monomial unitaries up to unit scalar form a closed set not containing `rot`. Paper sketch | NS | — |
| ACC_op | NS | NS | **CX†, exact** [A over K]. The implication is definitional: control makes every unitary available (`relabel_available`, OIRealization.lean:245-249), including `g_hb ∉ ⟨σ, τ⟩`. Hypotheses: (i) the kernel's embedding `coreIdx`, which places `h` on the system qubit (OIRealization.lean:15-18); (ii) R2 read as ACC_op; (iii) **ACC_op is consistent with `OICore`: open**. No core-realizing theory satisfying ACC_op is exhibited, so the exclusion may be vacuous (the #1188 pattern; OICORE-F2) | **NS**: no predicate-level dense form is stated (R3-B1) | NS | NS. A positive fragment is CI: with FIX and AP1's supplied posits, the Z/X sequential Lüders law and eraser behaviour at stabilizer scope (AP1 §0 items 3–4) [W]; no quarter phase (AP1 Lemma 5) [W] |
| ACC-R4 (M-INACC) | — | — | OC | OC | — | OC. No native instance: Lemma Q(iii) relies on supplied P1 (AP1:338-343); `G_σ` exposes (MI-R:91-96) [W] |
| ACC-U | — | — | OC | OC | — | **OC**. *Draft-conditional* [D, off `main`]: in the ARP-3 fragment F0, read-record dependence without certification holds and an exact noncontextual model exists (the ACCESS note's Prop. F0; its r2 re-review, N1). If that draft stands, ACC-U is not sufficient by itself. Theorem NC's spanning hypothesis is the one ACC-U removes (M2D:483-497) [W] |
| FIN_op | NI-M | NS | **CX, exact only** [A over K]: control makes uncountably many non-proportional conjugations available (trivially, by cardinality). Kernel analogue on `Fin 2`: `countable_not_pairFlowSourced` (PairFlowEquivalence.lean:218), whose companion `pairFlowSourced_of_qm` (:85) is stated from QM but uses only control (R3-n4) | **not excluded**: `fixedGateTheory` is countable and dense (DiscreteCompletion.lean:1942; D1 below) | NS | NS |
| RET-s | — | — | NS | NS | — | excluded within those scopes, **conditionally**: retains single-time isotropy (AP1 Lemma 3) [W]; draft confinement to the octahedron (REACHABLE Theorem C) [D, draft-conditional] |
| DIST, RET-w | — | — | NS | NS | — | NS |
| CERT | — | — | — | — | — | excluded within NC's scope, **conditionally** on W. NC's hypotheses are Lemma F's operation set, an injective identification (R1^⊗n or R-W) and spanning reads; under them a noncontextual model exists (M2D:483-497) [W] |
| CTRL | with WF + I + Cl: EI to QM (`general_characterization`) [K] | — | definitional | — | — | EI via QM |
| EMB | — | — | **NI-W**: `permTheory` has EMB and no control [K, kernel-only]; `lieRank_not_redundant` (LieRankSource.lean:156-162) [K]. EMB does not exclude control: QM satisfies it (`embeddedObservation_of_qm`, EmbeddedObservation.lean:327) (R3-B2) | NI-W (dense): `permTheory_dense_ceiling` [K on `Fin 2`] | **EI** (`closure_of_embeddedObservation`, `systemToLevelOne_of_embeddedObservation`, EmbeddedObservation.lean:211, 223) | — |

### 3.3 Inheritance of negative results (B2; D1 tag)

**Universal no-gos, inherited by any candidate that confines `T` inside their class.**

| No-go | Layer | Class | D1 |
|---|---|---|---|
| `permTheory_not_control`, `obs_not_control` | K, kernel-only | `permTheory` and its subtheories | exact |
| `permTheory_dense_ceiling`; `nonnegBounded_not_denseUnitaryControl` (FrozenSourcing.lean:173) | K on the `Fin 2` system carrier, every ancilla level. The kernel refutes density through the quarter phase (`phaseGate_not_preservesNonneg`, :177). The carrier-general form and the mixing-specific form ("no real rotation is approximable", via `preservesNonneg_of_approx`) are A | NonnegBounded (configuration-level) theories | both |
| `substratumGen_not_control` | K, `Fin 2` | the substratum theory and its subtheories | exact |
| `monomialSource_not_control` (SubstratumInterface.lean:186-189; not vacuous, since monomiality is closed under unit scalars) | K, `Fin 2` | monomial-only theories | exact; the dense form is A (closed-set sketch above) |
| `onesFixing_not_phasesAvailable` (PhaseSource.lean:55) | K | ones-fixing generated theories | exact (an approximate form is not stated) |
| `countable_not_pairFlowSourced`, `mixTheoryR_not_qm` | K, `Fin 2` | countable theories | **exact only** |
| `readWriteOperator_monomial`, `offDiagonal_interp_not_monomial` | K | operator level | exact (tangent) |
| Bell ceiling (Main:22, 366-395) | P + exhaustive | local setting interventions | both (an inequality) |
| Main:640 (`pper_of_finiteRootedRealizable`) | K | all-time exact laws | exact; ε windows unaffected |
| M2D U2 (finite group `A₄ ≀ S_n`), NC | W, scope as stated | q = 2, R1, H-LIFT | both (a finite group is not dense) |
| M1D Theorem W, Prop. C | W | odd `q`, R-W | both |
| AP1 Level 3 (AP1:955-968) | W | exact induced statistics on finite carriers | exact |

**Existential and independence results. These survive a candidate only if their witness satisfies it.**

| Result | Witness | FIX_op | FIN_op | ACC_op |
|---|---|---|---|---|
| `oi_alone_not_qm`, `oiCore_not_completedOI` | `diagTheory` | not assessed (contains non-permutation diagonal channels) | **no**: its monomial unitaries carry arbitrary phases, uncountable up to scalar [A] | **no** (`g_hb`) |
| — the replacement under FIX_op | `permTheory_twoState` (SubstratumInterfaceAudit.lean:754-758): core, no control | yes | yes [A] | no |
| `finiteOI_not_implies_inert/closure` (OIRealization.lean:360-370) | `countermodel`, `admissibleTheory` (both with control) | no | no | no |
| `oiPlus_independence`, `five_way_minimality` | witnesses with control in all clauses but the control clause | no; control-lacking clause not assessed | no; control-lacking clause not assessed | no; control-lacking clause not assessed (R3-n5) |

These become **vacuous**, not inherited, under FIX_op, FIN_op and ACC_op, because those candidates exclude exact control outright.

## 4. The §A.29 guard

**Control list.** This is a list, not a preregistration (N9). The candidates must preserve:

- `finite_horizon_equivalence`;
- `realizesSealedOICore_of_control`;
- the universal no-gos of §3.3, within their scopes;
- Main:566/582 as ε-consistency results.

**Category note.** §A.29 is written for revisions. Applying it to native clarifications is an extension. Under the ADA ledger, natives are
"preserve unless … testing an extension".

| Candidate | Preserves the controls | Consequence beyond the target | Hard to vary | Disposition |
|---|---|---|---|---|
| FIX | yes | quantum behaviour must sit on encoded carriers | yes (definitional) | **the smallest faithful strengthening**; restrictive (N8) |
| ACC-R2 | yes | in `coreIdx`'s embedding ACC_op excludes exact control (definitional; its consistency with the core is open); dense: NS (§3.2) | yes | native; the stronger exact negative is kept with its three hypotheses |
| FIN | yes | departures from exact continuous groups; recurrence | no while ε is free. ch01:32 = FULL:367 says ε is tied to the Planck length; not audited | conditional |
| RET-s | yes | M-ARC's two variants (owner c.6723277401: "Test replacing the supplied, isolated archive with an archive that remains in the world") | yes (crisp) | **the smallest crisp new hypothesis**, valid only below recurrence (AP1:338-343) |
| ACC-R4 | targets NC's hypotheses | none stated | **under-specified as a schema** (N6): its anti-fitting clauses exist, but no functional is fixed | not yet testable. Instantiate first (OICORE-F3) |
| ACC-U | removes CERT; must keep valid probabilities and consistent repeated behaviour (c.6723491138: "relaxing an assumption is not sufficient by itself") | instance-specific witnesses (c.6723571280) | it is a route, not a premise; the ARP-3 instance fixes it | **open**; one instance (F0) is classically imitable [D] |
| CTRL | contradicts FIX_op | — | — | rejected as an OI strengthening; it remains Main:590's empirical premise |
| EMB | yes | none empirical | yes | an interpretive clarification of P11; supplies composition only |

**FIX against RET-s (N8).** FIX is the smallest faithful strengthening, and it is restrictive. RET-s is the smallest crisp new hypothesis,
with validity bounded by ε / recurrence. Neither, on present evidence, makes OI an active ingredient in a quantum-selecting property.

## 5. Answer to the central question

**(a) Missing constraints: yes.** The original texts state restrictive content that `OICore` lacks: FIX, ACC-R1–R3, FIN for embedded records,
and RET for `T`.

- They are stated in the original texts and not chosen to reach QM (N11; total finiteness is an empirically motivated posit, Main:62).
- `OICore` keeps only existence content (F1, F2).
- As a constraint on `T`, R2 is absent: non-law reads of `h` are available even in classical theories (F3b). That this access occurs in QM is
  not evidence about QM (D4).

**(b) Could they help explain quantum behaviour? Partly, and only for classically reproducible fragments, within a finite search of
twelve candidate rows.**

- *Exact control and exact QM.*
  - FIX_op and FIN_op are *proved unable* (CX, §3.2).
  - ACC_op excludes exact control definitionally, under `coreIdx` and the R2 reading. Its consistency with the core is open, so this
    exclusion may be vacuous.
  - Downward-closed restrictions with a core-realizing witness do not imply exact or dense control (Lemma M, on `Fin 2`).
  - FIN excludes exact control anyway, so these negatives bear on the dense or ε level only where marked "both".
- *Dense control.*
  - Excluded for FIX_op: K on the `Fin 2` system carrier; A carrier-general.
  - Not shown for ACC_op: no dense predicate is stated.
  - **Not excluded** for FIN_op, since `fixedGateTheory` is countable and dense.
- *What the restrictions do explain.* Conditional on supplied posits, the Z/X sequential Lüders law with backaction, and eraser behaviour, at
  stabilizer scope. A noncontextual model reproduces them (AP1 §0 [W]; M1D Prop. C(d) [W]).
- *No quantum-selecting property* (control, ℂ, a non-monomial operation, contextuality, the Born exponent) follows from any candidate in the
  search **other than CTRL**. CTRL yields QM (EI) and is rejected as the target's own resource (R3-n3).
- *ε-level statistics.* Main:566 and 582 realize finite-menu quantum statistics to ε with one fixed reversible law. They are consistent
  with FIX, FIN and ACC-R2, but "Quantum mechanics enters as the instrument data and as the state held in the hidden register" (Main:582).
  So they show consistency, not explanation, and they are no bridge to operational QM (§8.7).

**(c) What remains open (D3; witness principle).**

- **ACC-U**, the owner's accessible-but-uncertifiable route. It removes the imported spanning-certification requirement that Theorem NC
  uses. It is open. *Draft-conditional* [D, off `main`]: one ARP-3 instance (Prop. F0 with its re-review N1) shows that experience without
  certification can be classically imitable. If that draft stands, ACC-U is not sufficient by itself.
- **ACC-R4 / M-INACC.** A second, distinct route. It is an under-specified schema, and it has no native instance [W].
- **The existence route at law level (D2).** A selection principle on the realization data `(φ, μ_H)` native to OI, rather than an added
  operation. It is open. Every existing realization of quantum statistics imports them.

**(d) Assumption-watch (recast, B4c).**

- Within `FiniteOperationalTheory (Fin 2)`, no downward-closed predicate satisfied by a core-realizer forces exact or dense control (Lemma M).
- A route to control needs at least one existence-type premise, possibly jointly with restrictions.
- OI does contain existence content:
  - Axioms 1–2 and C1–C4 for the process;
  - realizability of every finite law, with free `(φ, μ_H)`, at law level.
- Exact control is excluded by FIN in any case, so the operative target is dense or ε control (§8.7).
- Check which existence premise does the work before crediting an "OI-native" source.

**(e) The hierarchy and the mixing question.** See §8.10.

**(f) The owner's defensible position, assessed.** "Some strengthened OI constraints explain classical and classically reproducible quantum
fragments. Whether their combination with native existence principles can produce genuinely nonclassical, approximately quantum operations
remains open."

The analysis supports this statement. It adds three locating remarks (R3-B4):

1. "Explain" is conditional on supplied interface posits (P1–P3, E-iso).
2. Within the open question, some neighbouring sub-cases are already excluded:
   - exact control, for every countable mechanism. This is K on `Fin 2` and A in general. It is an *exact* result and is not used against
     the ε question (D1).
   - dense control on the configuration-level carrier. This is K on the `Fin 2` system carrier and A carrier-general. Configuration-level
     operations are not the effective operations the owner's question concerns (c.6724668737).
   - encoded gates within U2's scope (W) and Theorem C's (D). These exclusions are **conditional on those unverified records**.

   Beyond these, the question stands as the owner stated it. Within it, two cases are named and remain open, each not excluded and not a
   candidate mechanism: the horizon-limited finite-order gate (ENC-G-2) and a non-linear identification in a finite world (§8.7(e);
   R5-n2).
3. Accessibility (ACC-U) is open. Inaccessibility (ACC-R4) is not yet a testable hypothesis.

## 6. Proposed follow-ups (named only; none authorized)

1. **OICORE-F1.** A kernel lemma `oiCore_iff_two_availabilities` (F1). Lean work, not authorized.
2. **OICORE-F2.** A typed realization interface `(S, φ, V) → T` carrying FIX, FIN and embedded records. It would decide ACC_op's witness
   question.
3. **OICORE-F3.** Instantiate ACC-R4 as a fixed native-rule invariant, with fixed reads and a fixed fragment. Run it as a new round after
   Q-C2-2. ARP order and criteria unchanged.
4. **OICORE-F4.** Audit the ε–Planck pin (ch01:32).
5. Record-only: `oi_compatible_iff`'s decorative `_hoi`, next to `ExtendsSubstratum` (N1).
6. **OICORE-F5.** Correct the record characterizations of §8.3 R-1/R-2: the completion-assumption audit is mutable; the source audit is
   self-declared frozen (§A.42 item 6).
7. **OICORE-F6.** An approximate bridge theorem (§8.7): from an approximately available gate, or a horizon-limited gate, to `DenseFiniteQM`
   within an accessible horizon; or a counterexample.
8. **OICORE-F7.** "OI†" does not exist (§8.2 row 8). Define it first, if wanted.
9. **OICORE-F8.** A kernel statement of the idle `DerivedOI` conjuncts in `qm_iff_derivedOI_pairFlowSourced`'s backward direction.
10. **OICORE-F9.** A carrier-general dense theorem (§8.1 dense row; `Fin 2` only today).
11. **OICORE-F10.** Book/Main consistency of Axiom 1's statement (ch01:22 vs Main:38).

## 7. References off `main` (§A.42 item 8), traced one by one (B6)

| Reference | Claim it is attached to | Classification |
|---|---|---|
| `c1_core_access.py` (author control; `controls/` in the reviews) | F3(a)/(b) | provenance: F3 rests on `core_observer_minimal`, `relabel_available` and `permTheory_relabel`. Not landed |
| `review/REVIEW-OICORE-1.md` | §9 dispositions; Lemma I's sketch | on `main` beside this record; provenance: Lemma I is proved here (A) |
| Theorem C of the REACHABLE note, an ARP-2 (Q-C2-1) draft (named by its session path in `review/REVIEW-OICORE-1.md` B6) | §3.2 RET-s cell; §5(f) item 2; §8.4 capability table; §8.6 RET-s row; §8.7(c) row 4; §8.7(e) row 2; §8.8; §8.10 | **support off `main` (gap), open.** Every conclusion that uses it is marked *draft-conditional* and is never called "proved". §8.7(c) row 4 rests on it alone; its hypotheses (affine, P1, P2/N2) differ from U2's. No recorded owner decision covers the gap. It closes only if the draft lands, or the claims are narrowed further |
| Prop. F0 of the ACCESS note, an ARP-3 (Q-C2-2) draft, and N1 of that note's r2 re-review | §3.2 ACC-U cell; §5(c) ("not sufficient by itself") | **support off `main` (gap), open.** The §5(c) conclusion is stated as draft-conditional. It closes when ARP-3's record lands |
| EOI audit files (`AUDIT-C1/2/3`, `PACKAGE`) | none in r3 | **replaced**. Every label was swapped for its record or kernel line, or dropped (B6): MQ-01 → Equivalence.lean:43-44, 462-468; MQ-29 → Main:582; "C2 outcome 2" → W with hypotheses; C3's "joint property" → AP1:338-343 and MI-R:91-96; 8.a's OI reading dropped; PKG §3.5 dropped; PKG §6 → owner c.6723277401 |
| the `git archive` extract of the sources (`src/` in the reviews) | sources | an extract of `2cd49dc0`; support on `main` |
| owner comments c.6724391385, c.6723491138, c.6723571280, c.6723889799, c.6723277401; #1188 | scope; route definitions (c.6723889799 quoted verbatim); M-ARC | owner records. Using c.6723889799 to *define* ACC-U makes it support, so it is quoted exactly |
| owner directions c.6724620166 (hierarchy), c.6724668737 (dependency map), c.6724721208 (four distinctions, synthesis), c.6724832474 (separation) | §§0, 5(f), 8 | owner records of direction on #1169, quoted verbatim. No scientific claim rests on them. Coordinator messages are not cited as authority |
| `review/REVIEW-OICORE-1-r3.md` | §9.2 | on `main` beside this record; provenance |
| `review/REVIEW-OICORE-1.md`, `-r3`, `-r4`, `-r5`, `-r6` | §0: independently model-reviewed, ACCEPT at r6 | **support on `main`**: the review texts, landed beside this record. Each landed copy differs from its hashed original (revisions table) only in the reviewed-file path, which drops the session directory prefix, and in `REVIEW-OICORE-1.md` l. 239, which reads "session files" for that prefix's name. The trail is recorded at #1169 c.6725037236 (provenance) |
| the texts r1–r6 and the reviewed final text (sha256 in the revisions table) | the reviews' line-numbered findings | provenance: no conclusion here uses their content; the reviews' line numbers refer to them |
| `rc1_rot_root_of_unity.py` (reviewer control, named in `review/REVIEW-OICORE-1.md`) | none (R3-n8) | provenance; not landed |
| `DIR4-1169.md` (named in `review/REVIEW-OICORE-1-r3.md`) | the four distinctions | provenance: the session copy of owner direction c.6724721208, which is cited here |
| L: Niven's theorem, Perron–Frobenius, Spekkens 2007 (on `main`, appendix-c:232), the Hardy N/K remark | §§3, 8 | standard mathematics; Spekkens is support on `main`; Hardy is provenance only. The reviewer's RC-1 control is not cited (R3-n8) |

## 8. Strengthened formulations and the backward dependency map

### 8.1 The anchors: the strongest proved operational equivalences [K]

| Target | Theorem | Direction | Carrier |
|---|---|---|---|
| exact finite endomorphic operational QM | `carrier_general_oiPlusMin` (MinimalRepertoire.lean:569 ff.) | both | every nonempty finite carrier |
| exact typed QM | `typed_determined_iff` (TypedCompletion.lean:850), with `typed_determined_of_oiPlusMin` (Main:590) | as cited | typed |
| exact QM | `qm_iff_derivedOI_pairFlowSourced` (PairFlowEquivalence.lean:199-201) | both | `Fin 2` |
| **dense** finite QM: `DenseFiniteQM = KrausSoundExt ∧ KrausDense` (DiscreteCompletion.lean:52-60) | `denseUnitaryControl_of_fixedGate` (:1522), then `denseFiniteQM_of_denseControl` (DenseInstrumentBridge.lean:496-498) | **sufficiency only**; "soundness is not a consequence of density" (:494-495) | `Fin 2` |

**The dense row's hypotheses.**

- `DerivedOI`, with its stipulated phases.
- `FixedGateSourced α`: one *fixed* gate `mixImage n α` exactly available at every level (DiscreteCompletion.lean:34-35).
- `α/π` irrational.
- `KrausSoundExt`.

Its witness `fixedGateTheory` is dense and not QM (:1942-1952).

### 8.2 The formulations [K]

| # | Formulation | Adds beyond `OICore` | Equivalence, scope | Idle | Mixing term |
|---|---|---|---|---|---|
| 1 | `CompletedOI` (CompletedOI.lean:99-100) | the five conditions (PhysicalCharacterization.lean:295-297) | `completedOI_iff_qm`, `Fin 2` | core | `HasCompositeUnitaryControl` |
| 2 | OI⁺ under one name, two definitions: qubit `OIHierarchy.OIPlus` (CompletedOI.lean:418-420) and general `OIHierarchyGeneral.OIPlus` (CarrierGeneralOIPlus.lean:185-186) | WellFormed, independence, `ReversibleRichness`, `ObserverRecursion` | `Fin 2` (:440); every carrier (:213); `oiPlus_qubit_iff` (:224) | core (qubit form) | `ReversibleRichness` (:110-117): an inverse clause, plus a drift `H` with `∀ t, flow H t` available and `HControl` |
| 3 | `OIPlusEmbedded` (EmbeddedObservation.lean:366-368) | validity, independence, `ReversibleRichness`, EMB | every carrier (:394) | — | `ReversibleRichness` |
| 4a | `OIPlusLocal` (ImplementationLocality.lean:1053-1054) | `ImplementationLocality` (:370-371: *some* context-stable, label-invariant class generates availability), `ReversibleRichness`, EMB | every carrier (:1079) | — | `ReversibleRichness` |
| 4b | `OIPlusMicro` (MicroscopicReversibility.lean:336-337) | reversible implementation locality (adds `DaggerStable`, :216-225), `LieRankRichness` (:93-98), EMB | every carrier | **`DaggerStable` idle in →**: dropped at :227-230, used at :343-347 | `LieRankRichness` |
| 4c | `OIPlusElem` (LieRankSource.lean:527-528) | reversible implementation locality, `ElementaryTransitionRichness` (:436-441: flows of every transition, every swap, the quarter phase, all as availabilities), EMB | every carrier | dagger idle (via 4b) | every pair flow, plus the phase |
| 5 | `OIPlusPos` (PositivePackage.lean:35-36) | implementation locality, `ElementaryTransitionRichness`, EMB | every carrier; `oiPlusPos_iff_oiPlusElem` | — | as 4c |
| 6 | `OIPlusMin` (MinimalRepertoire.lean:544-545) | implementation locality, `PhaseFreeRichness` (:423-428), EMB | every carrier | — | at each level with ≥ 2 states, *some* pair with `∀ t, flow (transition a b) t` available, plus every exchange |
| 7 | `DerivedOI` (RouteB.lean:146-148) + `PairFlowSourced` (PairFlowEquivalence.lean:48-50) | reversible implementation locality, EMB, exchanges, phases ("stipulated", RouteB:141-145), `ReadWriteAvailable`, plus a real pair flow (RealPairFlow.lean:41-47) | `Fin 2` | **in ←, `ReadWriteAvailable` and `DaggerStable` are idle**. Consumed: the phases (PairFlowEquivalence:180; DerivedQ3:210), the exchanges (DerivedQ3:210), implementation locality and EMB (RouteB:166-169) [A, proof-term reading] | `PairFlowSourced`, plus the stipulated phases |
| 8 | "OI†" | **not defined** at `2cd49dc0` (`git grep` for `OI†`, `OIDagger`, `OI^†`: none). Nearest objects: `DaggerStable`, `InverseAccessibility` (:88-90) | — | dagger is idle in 4b, 4c and 7; `OIPlusPos` drops it | — |

**The owner's OIPlusMin description is accurate, with two precisions.**

- The driven pair is chosen *per level*.
- The flow is complex. For `D ≥ 3`, `flow(X_ab, π/2)·swap_ab = diag(−i, −i, 1, …)` [A, re-derived here]:
  - on the pair, `exp(−iθX) = cos θ·I − i sin θ·X`;
  - at `θ = π/2` this is `−iX`;
  - multiplying by `X` gives `−i`.

  "No phase operation" therefore holds of the primitives only.

### 8.3 Record characterizations checked

- **R-1 (discrepancy).** Two records misdescribe `ElementaryTransitionRichness`:
  - The completion-assumption audit says of `OIPlusElem` that no conjunct "is a Lie-algebraic, reachability or availability condition".
  - The source audit says the principles are "stated at the level of physical implementations".
  - In fact `ElementaryTransitionRichness` *is* a conjunction of availabilities (LieRankSource.lean:436-441). The class-level
    `DrivesElementary` (SubstratumSource.lean:77-82) is a different predicate, and `OIPlusElem` does not use it.
- **R-2 (restatement).** The completion-assumption audit's "DERIVED", defined as "from a strictly more primitive principle that mentions
  neither the assumption nor its operational vocabulary", fails for control.
  - Every richness conjunct is availability of unitary conjugations.
  - The Lie-generation theorems reduce *how much* must be available. They do not source it.
  - The pair-flow audit's own boundary classes such conditions as "a restatement of the target".
- **R-3 (confirmed).**
  - The source audit's endpoint matches `substratum_plus_control_qm` and its converse.
  - Its fifth entry moves the phases out of what the substratum supplies (`onesFixing_not_phasesAvailable`).
  - Its negative half cites the vacuous `readWriteSourced_not_qm` (#1188).

### 8.4 The backward dependency map

```
Exact QM ⟺ WellFormed ∧ Inert ∧ Control ∧ Closure ∧ Seam          (general_characterization; exactAll_iff_substantive)
  Validity ⟸ ImplementationLocality  (validity_of_implementationLocality; normalization a stated trace clause)
  Inert    ⟸ ImplementationLocality  (observationalIndependence_of_implementationLocality)
  Closure  ⟸ EmbeddedObservation     (closure_of_embeddedObservation)     ┐ OI⁺: ObserverRecursion ⇒ Closure
  Seam     ⟸ EmbeddedObservation     (systemToLevelOne_of_embeddedObservation) ┘
  Control  ⟸ PhaseFreeRichness ∧ Closure   (control_of_phaseFree; Closure used for the descent at D ≤ 2)
             PhaseFreeRichness = [exchanges] ∧ [ONE CONTINUOUS DRIVE per level]        ← first assumed capability
             OIPlusLocal / Embedded / OI⁺: Control ⟸ ReversibleRichness = [inverse] ∧ [continuous drift + Lie generation]
             CompletedOI: Control assumed outright
Dense QM (Fin 2) ⟸ DerivedOI ∧ [ONE FIXED GATE, α/π irrational] ∧ KrausSoundExt  (sufficiency only)
             DerivedOI = RevImplLocality ∧ EMB ∧ Exchanges ∧ [PHASES, stipulated] ∧ ReadWrite (idle)
```

**Every leaf except the mixing term, and the phases where they are used, has a kernel instance generated by OI's own substratum.**

- The substratum class is an architecture, context-, label- and dagger-stable (`substratum_residual`, StructuralClosure.lean:383-386).
- Its generated theory therefore has implementation locality, EMB, validity, inert spectators, closure, the seam and the exchanges.
- It lacks the drive (`substratumClass_not_drivesElementary`, :370).
- *Interp.* (R3-n6): `ImplementationLocality` reads as FIX with the class left existential. Fix the class to OI's substratum class, and
  the drive fails.

**The owner's capability rows.**

| Capability | Leaf | Corpus establishes | Strength (D1) | Traced to OI? |
|---|---|---|---|---|
| Embedded observation | EMB → closure, seam | OI-generated theories have it (`genTheory_embeddedObservation`; `permTheory_sourcedOI`) | **established** (K) | *interp.* clarification (Main:38, 86) |
| Implementation locality | → validity, inert | the substratum class has every stability | **established** (K) | clarification: Lemma 2's uncoupled product; substratum gauge; FIX's weak form |
| State exchanges | the swap clause | bijections | **established** (K) | native: Lemma 3 under FIX |
| Continuous pair mixing | the drive / pair flow / richness | never supplied | exact: **CX** for countable mechanisms (A; K analogue on `Fin 2`). Dense on the configuration-level carrier: **excluded** (K on `Fin 2`; A in general). Dense on encoded carriers: excluded **conditionally** within U2 [W] and Theorem C [D]; **open** beyond. ε-level: open, and the horizon-limited finite-order gate is not excluded by any result found (it needs OICORE-F6; open conjecture) | **not traceable**: new hypothesis (Main:590, "an empirical controllability resource") |
| Operational consistency | validity; `KrausSoundExt` in the dense route | positivity derived for every class (`cp_of_instAvail`); normalization stated; dense soundness a separate hypothesis | **established** (exact packages); **assumed** (dense) | clarification at the classical level (marginals of bijections); the CP form inherits the ℂ import |
| (Phases) | `PhasesAvailable` | stipulated | **CX** from observer machinery (K) | not traceable |
| (ℂ kinematics) | the setting | imported (GR:216) | — | not traceable |

### 8.5 The first assumed capability against OI's meaning

- The Definition's dynamics is "iteration of a single transition map" on a finite `S` (Main:46, 62).
- Intro:129: "A reversible rule on finitely many states can only permute whole states; it cannot blend them."
- The read-write tangent test makes this a kernel fact for read-write families (ReadWriteControl.lean:100, 106-115).

So the missing capability is not a weakened OI principle. At the configuration level, it is coherent blending of distinguishable states,
which OI's finite bijective picture does not contain.

At the effective (encoded) level, ε-blending does appear: Main:566 and 582 realize it, though only with imported instruments and state.
Whether native data produce it is the open question of §8.7. The two levels are kept apart (D1/D4; R3-n6).

### 8.6 Can access, retention, certification, observer recursion or hidden-state dynamics supply it?

| Candidate | Supplies mixing? | Strength (D1) |
|---|---|---|
| Access, ACC_op | no. It excludes exact control definitionally, under (i) `coreIdx`, (ii) the R2 reading, and (iii) consistency with the core, which is open (§3.2) | **CX†, exact** (possibly vacuous). Dense: **NS** |
| Access, read/write observer theory | no (`permTheory_not_control`; `permTheory_dense_ceiling`, K on `Fin 2`; `obs_not_layerFlowExecutable`; kernel-only, #1188) | **CX**: exact (every carrier, K) and dense (K on `Fin 2`, A in general) |
| Accessible-but-uncertifiable (ACC-U) | not shown. One instance is classically imitable [D, draft-conditional] | **OC** |
| Retention (RET-s) | not shown. Affine + P1 confines to the octahedron [D, draft-conditional]; U2 [W, conditional] | NS; excluded within those scopes, conditionally |
| Certification (CERT) | no: it yields a noncontextual model [W] | excluded within NC's scope, **conditionally** on W (both) |
| Observer recursion (EMB) | not implied: it supplies closure only. Witnesses: `lieRank_not_redundant` (K, `Fin 2`) and `permTheory`. It does not exclude control, since QM satisfies EMB | **NI-W**: exact; dense via `permTheory_dense_ceiling` (K on `Fin 2`) |
| Hidden-state dynamics (read-write, C1/C4 memory) | no: idle in `DerivedOI`'s backward route; permutation-valued (`readWriteOperator_monomial`); memory without control (`readWriteControl_independent`, :216) | **CX** within finite bijective read-write dynamics (exact; the dense form via the monomial closed-set sketch, A). Open only for a "genuinely continuous (non-bijective-valued) coupling" (source audit). On the reading of Main:44-46 and 62, that lies outside OI's axioms (*interp.*; R3-n6) |

**Restatement verdict.** Every mixing conjunct (`ReversibleRichness`, `LieRankRichness`, `ElementaryTransitionRichness`, `PhaseFreeRichness`,
`PairFlowSourced`, `FixedGateSourced`, `HasCompositeUnitaryControl`) is availability of unitary conjugations. Each fails the pair-flow
audit's restatement boundary as a "source". None of the five candidates appears as their source.

### 8.7 Exact against effective mixing (D1), and what an ε-route must assume

**(a) Exact continuous drive: proved unable for every countable mechanism.**

- `countable_not_pairFlowSourced` with `pairFlowSourced_of_qm` [K, `Fin 2`], and `mixTheoryR_not_qm` [K].
- A finite world with finite protocol words has countably many operations [A].
- The necessity directions (`oiPlusMin_of_qm` etc.) make this independent of the microscopic form. The owner's caveat does not open the
  exact route.

**(b) The approximate form exists and needs no continuous drive.**

- The dense theorem needs one *fixed* exactly available gate, `mixImage n α`.
- That gate is built from `StateMixingCoupling.rot θ` (StateMixingCoupling.lean:45-51). Take `α = arccos(3/5)` (R3-n2): the gate is
  rational, and `α/π` is irrational [L: Niven; A].
- So exact rational reach does not forbid it. The REACHABLE note's §3.1 [D] excludes only irrational-entry gates, such as `T`.

**(c) Native supply of that gate, by context.**

| Context | Status |
|---|---|
| Configuration-level (physical) carrier | **excluded, both**: K on the `Fin 2` system carrier, every ancilla level (`nonnegBounded_not_denseUnitaryControl`, `permTheory_dense_ceiling`, which refute density through the quarter phase). The carrier-general and mixing-specific forms are A (R3-B3) |
| Closed finite world, one fixed induced map | **excluded, exact** [A, sketch; R3-n1]. Hypotheses: the identification `E` is linear; `E S = G E` on an `S`-invariant preparable span, with `S` the (sub)stochastic configuration map of one fixed protocol; one induced map `G` for every run. Then `spec G ⊆ spec S`. The unit-modulus eigenvalues of a (sub)stochastic matrix are roots of unity (Perron–Frobenius, L). The channel of `mixImage α` has the eigenvalues `e^{±2iα}`, which are not roots of unity. A finite-order gate whose order exceeds the accessible horizon is **not** excluded. AP1 Level 3 (AP1:955-968) [W] makes the point for `rot` |
| Open supplies, `q = 2`, R1^⊗n, H-LIFT | **excluded, both, conditional on W**: the finite group `A₄ ≀ S_n` (U2). Not "proved", by §A.46 item 7 |
| Affine rules with P1, P2/N2 and forward conditioning | **excluded, both, draft-conditional**: octahedral (REACHABLE Theorem C) [D, off `main`, conditional on WIP records]. This row rests on the draft alone |
| Non-affine bounded rules (Q-C2-1 tests this case), other frames, non-linear identifications, failure of H-LIFT | **open**. The region's boundary is itself conditional on the W and D rows above |

**(d) Do the ε-results bridge to operational QM? No, as they stand.**

- **Main:566 and 582.** These are menu-indexed. One realization exists per finite instrument family, horizon `K` and grid `G`, so the rule
  family is indexed by accuracy. The instruments and the state are imported. They give ε-statistics for a menu, not `KrausDense` for one
  theory.
- **The dense kernel route.** Its conclusion is approximate, but its hypothesis (`FixedGateSourced`) is exact. No theorem in the hierarchy
  takes an *approximately* available gate, a horizon-limited gate or a growing family of systems as hypothesis.
- **The infinite-region form.** `driveQ_isContinuousPath` (SecondOrderDrive.lean:225) gives a strongly continuous path with "Not claimed: a
  group law" and no generator. It is not an availability statement.

**(e) Synthesis: new route, or shifted assumption? (c.6724721208; R3-B5)**

*What the distinction does.* It **removes continuity** from the requirement. One fixed discrete gate suffices for density (K, `Fin 2`),
and rational arithmetic permits that gate. This is a real mathematical reduction of the target.

*What it does not remove, under the existing theorems.* An exactly available non-monomial gate of infinite order, together with the
stipulated phases. A bridge theorem of the OICORE-F6 kind could change the order requirement.

*By route:*

| Route | Assumes | Verdict |
|---|---|---|
| Growing systems, or a rule family indexed by ε (as in Main:566) | more than one `φ`, or a growing `S`: not an OI principle (Main:44-46). Still imports instrument data | **shift** into a new hypothesis |
| An infinite world, open supplies or an infinite hidden sector, for an exact infinite-order gate | conflicts with the total-finiteness posit (Main:62). Meets U2 [W] and Theorem C [D, draft-conditional] in their scopes | **shift** into a new hypothesis |
| *Separate open dense case (not an ε-route).* A non-linear identification in one fixed finite world, for an exact infinite-order gate | outside §8.7(c) row 2's hypotheses (a linear identification, an invariant span, one fixed induced map), which alone exclude such a gate in a finite world. §8.7(c) row 5 leaves it open | **not excluded; not a candidate mechanism** (R4-3, R5-n2) |
| A free ε tuned to the experimental precision | adjustable to any outcome | **shift**, and it fails §A.29. The ε–Planck pin is unaudited (OICORE-F4) |
| **Horizon-limited gate**: one fixed finite world, an exactly available gate of finite order exceeding the accessible horizon (ENC-G's second disjunct) | no premise beyond OI's axioms is needed to *state* it. Whether native dynamics supplies such a gate is open: it is ENC-G's second disjunct, an open conjecture typed as a new hypothesis (§8.8). It is not excluded by (c) row 2 | **not excluded by any result found; open conjecture (ENC-G-2); not a candidate mechanism**. Two counts are missing: (1) a bridge theorem from such gates to `DenseFiniteQM` within the horizon (OICORE-F6), which is mathematical; (2) a native mechanism, which is physical and must lie outside the W/D scopes of (c) |

*Headline.* Over the five rows above, the approximate-versus-exact distinction does not show any route to be OI-native.

- **Three routes shift** the missing assumption into a new hypothesis: growing systems or ε-indexed rules; an infinite world or open
  supplies; a free ε.
- **Two cases stay open.** Each is *not excluded; not a candidate mechanism*:
  - the horizon-limited finite-order gate (ε-route). It is open on two named counts, F6 and a native mechanism. It remains an open
    conjecture (ENC-G-2), typed as a new hypothesis per §8.8;
  - a non-linear identification in a finite world (a dense case, not an ε-route; §8.7(c) row 5).

It is not shown that every route falls into one of these five rows.

**Gap classification.**

| Route | Missing |
|---|---|
| Exact | a physical capability. The mathematics exists; the capability is excluded for countable mechanisms |
| Dense, with an exact infinite-order gate | a **physical** capability: a native exact non-monomial infinite-order encoded gate, plus a phase source. Also a **mathematical** gap for carriers other than `Fin 2` |
| Horizon-limited finite-order gate | **both**: a bridge theorem (F6) and a native mechanism. Not excluded by any result found; open conjecture (ENC-G-2); not a candidate mechanism |
| Non-linear identification in a finite world (dense) | a **physical** capability: a native mechanism realizing an exact infinite-order gate outside row 2's hypotheses. Not excluded; not a candidate mechanism |
| Growing systems / ε-indexed rules / infinite world or open supplies / free ε | a **new hypothesis** in each case; growing systems and ε-indexed rules also import instruments |

### 8.8 The weakest candidate that could act, and the consequence requirement

No OI principle as stated implies a non-monomial gate. Restrictions alone cannot (Lemma M). The weakest candidate is an existence claim:

> **ENC-G (new hypothesis, not adopted).** Some native reversible rule, with record-dependent access, exactly induces one fixed encoded
> non-monomial gate of infinite order, or of order exceeding the recurrence-bounded horizon, on a two-level encoded system.

- **Typing.** ext, motivated by the owner's record-dependent-access route.
- **§A.29.**
  - It must lie outside the scopes of U2, NC and Theorem C: non-affine, beyond R1/H-LIFT, and below recurrence.
  - It is hard to vary only if the rule, the identification and the reads are fixed in advance.
  - Consequences independent of dense QM:
    - non-octahedral reachable laws;
    - aperiodic encoded dynamics below recurrence;
    - a specified H-LIFT failure.
  - No empirical consequence is stated.
- **Status: open (OC).**
  - Its second disjunct (ENC-G-2) is the horizon-limited route of §8.7(e). It is not excluded by any result found, and it is not a
    candidate mechanism.
  - Its first disjunct, an exact infinite-order gate, is excluded in a closed finite world only under §8.7(c) row 2's hypotheses. Otherwise
    it is open (row 5: non-linear identifications). That case is not excluded and is not a candidate mechanism (§8.7(e), separate dense
    case). Pursued through an infinite world or open supplies, it is a new hypothesis against the total-finiteness posit (R4-3, R5-n2).

### 8.9 No-gos at their scope

See §3.3 for the D1 tags. For the formulations:

- `oi_alone_not_qm`, `five_way_minimality`, `oiPlus_independence`, `redundancy_fails`, `core_not_embeddedObservation`, `lieRank_not_redundant`
  and `elementary_not_redundant` (K, `Fin 2`) show the added principles are independent of the core and of each other.
- `substratum_residual` (K) shows OI's substratum supplies every leaf except the drive.

### 8.10 Answers

**Hierarchy.** The added properties that trace to OI's principles are the structural ones:

- implementation locality, through context and label stability;
- embedded observation and observer recursion, *interp.*;
- the exchanges;
- operational consistency at the classical level.

The kernel shows OI's own substratum supplies them. The coherent-mixing resource, the quarter phase where it is used, and ℂ kinematics
are independent assumptions about the available operations.

**Mixing.** "Can incomplete observation, together with native reversible dynamics and record-dependent access, produce the effective
coherent mixing that OIPlusMin currently assumes?"

- **Exactly: no.** It is proved unable for every countable mechanism (A; K analogue on `Fin 2`), whatever the microscopic form. This is
  an exact result and is not used against ε-constructions (D1).
- **Densely:**
  - excluded on the configuration-level carrier (K on the `Fin 2` system carrier; A in general);
  - excluded on encoded carriers within U2's scope and Theorem C's affine scope, **conditionally** on those W and D records;
  - **open** otherwise: non-affine rules (Q-C2-1 tests the non-affine bounded case), other frames and identifications, and failures of
    H-LIFT.

  Under the existing theorems, a dense route needs one exact infinite-order non-monomial gate and the stipulated phases. In a finite
  world such a gate is excluded only under §8.7(c) row 2's hypotheses. A non-linear identification stays open: not excluded, and not a
  candidate mechanism (R5-n2).
- **ε-effectively: open, and not bridged.**
  - No approximate-hypothesis theorem exists, and the existing ε-realizations import their instruments.
  - No route is shown to be OI-native. Three routes shift the gap into a new hypothesis. Two cases stay open, each not excluded and
    not a candidate mechanism (§8.7(e)):
    - the horizon-limited finite-order gate (ENC-G-2, an open conjecture; open on OICORE-F6 and a native mechanism);
    - a non-linear identification in a finite world (dense).

**c.6724620166's question.** "Do any of these strengthened formulations capture physical consequences of incomplete observation that the
original `OICore` misses, without assuming the quantum behavior we want to derive?"

- Partly. Their structural conjuncts capture physical content that `OICore` misses and that OI's substratum supplies:
  - implementation locality, with spectator stability and label invariance;
  - embedded observation, with closure and the seam;
  - reversibility;
  - the exchanges.
- None captures the mixing resource without assuming it. Every formulation that reaches QM assumes an availability of non-monomial
  unitary conjugations (§8.6, restatement verdict).

## 9. Dispositions

### 9.1 r1 review (REVIEW-OICORE-1.md) and the directions, as applied in r3

| Item | Disposition |
|---|---|
| B1 | Lemma I and Lemma M are proved (A over K, using `permTheory` so that dense control is covered). Candidates are formalized or marked n/e (§2). NI-M is used only with a witness. ACC carries no Lemma-M claim. ACC_op's classification was revised in r4 (§9.2, R3-B1). The V and I cells are corrected: FIX_op ⇒ V is EI, I is NS |
| B2 | §3.3 is split into universal no-gos (with D1 tags) and existential results (with witness columns); the latter are vacuous under FIX_op, FIN_op and ACC_op |
| B3 | ACC-U and ACC-R4 are separate rows (§2, §3.2, §4, §5(c)). The ACCESS r2 re-review N1 / F0 instance is cited [D] |
| B4 | §5(b) is "partly", within a finite search, with exact vs dense vs ε separated. §5(d) is recast. Law-level existence through `(φ, μ_H)` is named |
| B5 | F3 is recast (C1 by design; zero-step access is classical). P6 and §5(a) are fixed |
| B6 | §7 traces each reference. EOI labels are replaced by on-`main` lines. the REACHABLE note is labelled D in two cells, by direction |
| N1 | `_hoi` is CONFIRMING (§1.3) |
| N2 | the P1 mirror is fixed; the Main/book difference is recorded (§1.2; F10) |
| N3 | FIX is marked *interp.*; the phase-intervention scope is `Fin 2` only |
| N4 | AP1 Lemma 2 is labelled W, re-derived (A), with the generation argument |
| N5 | the ext tag is introduced |
| N6 | ACC-R4 is "under-specified schema" |
| N7 | `permTheory_not_phasesAvailable` at :670; "fails at τ̂" |
| N8 | FIX and RET-s are compared explicitly (§4) |
| N9 | "control list"; category note added |
| N10 | P4 softened |
| N11 | "stated in the original texts, not chosen to reach QM" |
| N12 | the W definition is made accurate |
| Hierarchy direction | §8.2–8.3, §8.10 |
| Dependency-map direction | §8.4–8.8, including the pressure-test and the dense form |
| Four distinctions | D1–D4 tags in §§0, 3.3, 5, 8; CX ("proved unable") separated from NS ("not shown") |

### 9.2 r3 re-review (REVIEW-OICORE-1-r3.md, `5912885b…`), applied in r4

| Item | Disposition |
|---|---|
| R3-B1 | ACC_op is restated as "every available relabelling lies in ⟨σ, τ⟩" (§2). Its exact exclusion of control is kept, marked *definitional*, with three hypotheses: `coreIdx`; the R2 reading; consistency with `OICore`, which is open, since no core-realizer satisfying ACC_op is exhibited (#1188 pattern; OICORE-F2). The dense form is NS. Changed in §§2, 3.1, 3.2, 4, 5(b) and 8.6 |
| R3-B2 | A new class NI-W (§0). EMB is NI-W in §3.2 and §8.6; QM satisfies EMB. CX is kept for class-confinement results |
| R3-B3 | Every dense ceiling now reads "K on the `Fin 2` system carrier, every ancilla level". Carrier-general and mixing-specific forms are A (§§3.2, 3.3, 5(b), 5(f), 8.4, 8.6, 8.7(c), 8.10) |
| R3-B4 | §5(f) item 2 is replaced by a neutral locating list. Exact results are flagged as not used against ε. Configuration level and effective level are kept apart. W/D exclusions are marked conditional. §8.4 and §8.10 match |
| R3-B5 | §8.7(e) is rewritten by route. Three routes shift the gap into a new hypothesis. The horizon-limited finite-order gate is open on two named counts (F6 and a native mechanism); r5 rewords it as "not excluded" (R4-2). The infinite-order requirement is stated "under the existing theorems". The gap table is split. §8.8's status and §8.10 match |
| R3-B6 | Theorem C and ACCESS F0 are listed as open gaps in §7. Every conclusion using them is marked draft-conditional, and none is called "proved". Owner directions are cited by comment id (c.6724620166, c.6724668737, c.6724721208, c.6724832474). No coordinator message is cited as authority |
| R3-n1 | §8.7(c) row 2 uses the spectral (Perron–Frobenius) argument, with its hypotheses stated. The horizon-limited gap is noted |
| R3-n2 | The gate is cited as `StateMixingCoupling.rot` (:45-51) with α = arccos(3/5) |
| R3-n3 | §5(b) makes the CTRL exception explicit |
| R3-n4 | The FIN_op exact cell is "A over K" |
| R3-n5 | The control-lacking clause of `five_way_minimality` / `oiPlus_independence` is "not assessed" |
| R3-n6 | *Interp.* is marked at §8.4 (ImplementationLocality as FIX) and at §8.6 (continuous coupling). §8.5 is scoped to the configuration level, with the effective level kept apart |
| R3-n7 | Lemma M's statement names `FiniteOperationalTheory (Fin 2)` |
| R3-n8 | RC-1 is no longer cited. `c1_core_access.py` lands with the record or is dropped |

### 9.3 r4 re-review (REVIEW-OICORE-1-r4.md, `8ab55e2d…`), applied in r5

| Item | Disposition |
|---|---|
| R4-1 | Legend entry **CX†** added (§0). ACC_op's cells are CX† in §3.2 and §8.6. The §3.2 RET-s cell reads "excluded within those scopes, conditionally" |
| R4-2 | "Consistent with OI" is replaced at every site (§8.7(e) table, headline and gap table; §8.8; §8.10; §9.2) by "not excluded by any result found; open conjecture (ENC-G-2); not a candidate mechanism". "Nothing beyond OI's axioms" and "exposes" are dropped. The synthesis answer now says that no ε-route is shown to be OI-native |
| R4-3 | §8.7(e) row 2 and §8.8 state the exclusion of an exact infinite-order gate as conditional on §8.7(c) row 2's hypotheses, with non-linear identifications open (row 5) |
| R4-4 | §8.4: the horizon-limited route is moved from "dense" to an ε clause |
| R4-5 | §7 lists every Theorem C use site. The §3.2 ACC-U cell is draft-conditional |
| R4-6 | §5(d) names `FiniteOperationalTheory (Fin 2)` |
| Summaries | Checked against the body: §5(b), (c), (d), (f) and §8.4, 8.6, 8.10 agree. No §5 item refers to the horizon-limited route except through §8.10 |

### 9.4 r5 review nits (REVIEW-OICORE-1-r5.md, `365c0be4…`), applied in r6

| Item | Disposition |
|---|---|
| R5-n1 | The CERT cells in §3.2 and §8.6 read "excluded within NC's scope, conditionally on W" |
| R5-n2 | §8.7(e) row 2 is split. The infinite-world / open-supplies route is a shift. The non-linear identification in a finite world is its own open dense case: not excluded, not a candidate mechanism. The count the body supports is three shifts and two open cases (ENC-G-2 and non-linear identification). The headline, gap table, §8.8, §8.10 and §5(f) are updated to match |
