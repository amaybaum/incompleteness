# EOI audit phase 2 — Cluster C2: scope of negative / no-go results (interface limit vs OI limit; A2, A3) — r2

Snapshot: `origin/main` = `5ce4f98ec3a76aee6fdd17ed1bad7b278f1d9732`. Read-only; every citation below was re-read at
that commit. r2 applies REVIEW-C2.md; r3 applies REVIEW-C2-r2.md. r1 and r2 are kept as AUDIT-C2-r1.md and
AUDIT-C2-r2.md.

Path abbreviations:
- `OIB/` = `verification/lean-mathlib/OIBridge/`
- `R/` = `verification/programmes/oi-qm/reconstruction/`
- `P/` = `verification/programmes/oi-qm/`
- `FULL` = `book/The-Incompleteness-of-Observation-FULL.md`

Evidence layers are named at each use:
- **kernel** — a Lean theorem, `#print axioms` clean;
- **paper** — a written derivation with author self-checks, and model or internal review recorded as provenance;
- **exact probe** — exact arithmetic, not kernel;
- **finite test**.

For each claim, the audit gives:
- the statement as made;
- where it is proved, and at which layer;
- the hypotheses, and where each enters;
- the outcome: 1 (valid as stated), 2 (valid but conditional) or 3 (needs new investigation);
- the class: native, conditional, imported or n.a.;
- the over-reading texts;
- the follow-up questions, if any.

No replacement wording is drafted. Arguments marked **(auditor, paper)** were checked by hand against the quoted Lean
definitions only. No kernel check was run.

## 0. The common object: the stated observer interface

The no-gos MQ-14, MQ-15, PROG, TI-D and Intro:129 share one modelling step.

**Kinematics.** Operations are complex-linear maps on complex matrices indexed by the configuration set, at every
ancilla level. This kinematics is taken as given (GR:216; Main:564).

**Carrier identification.** Configurations are orthonormal basis vectors. Each intervention is represented by its
permutation matrix (bijections, read-write couplings) or by a diagonal phase where one is stipulated. The objects
that encode this are:
- `IsMonomial` and `MonomialSource` (OIB/SubstratumInterface.lean:73-75, 180-182);
- `substratumClass` (OIB/StructuralClosure.lean:178-180);
- `permClass` (OIB/SubstratumInterfaceAudit.lean:236);
- `ReadWriteSourced` (OIB/ReadWriteControl.lean:156-160), which is defective (§1, B1).

MECH-1 names the premises behind this identification (R/mechanism-1-20261107/DESIGN.md:159-161; paper):
- (P-a) the operational state is a law on configurations;
- (P-b) every step is bijection-valued;
- (P-c) every read is of a configuration function.

**What the kernel covers for hidden registers.** Coverage differs by layer.
- **Kernel.**
  - **Hidden cells inside the carrier.** `obsTheory 𝒮 = permTheory (Conf 𝒮)` acts on the whole configuration space,
    hidden cells included (OIB/SubstratumInterfaceAudit.lean:17-24). Its no-gos are statements about which operations
    are available, not about which input states are allowed. Any correlation between hidden and visible cells in the
    input state is therefore irrelevant to them.
  - **Hidden registers outside the carrier.** Here the kernel covers only fresh ancillas. They are attached in the
    maximally mixed product state `uniformAttach`, "the only preparation the theory assumes"
    (OIB/OperationalAssembly.lean:490-494, 628-630), and are evolved, read and discarded inside one instrument
    (`InstAvail.discard`, OIB/ImplementationLocality.lean:285-289; `genTheory`, :852-884).
- **Paper.**
  - AP1 Lemma 2 extends coverage to fresh cells in any fixed law (R/apparatus-1-20261107/DESIGN.md:153-163).
  - A hidden register outside the carrier that is already correlated with the carrier at the input is covered only
    by the diagonal-preservation argument. That argument is AP1 Lemma 1 (DESIGN.md:132-142), the operational reading
    of `preservesDiag_conj_of_monomial`, *applied to the enlarged carrier* C × H (auditor, paper). As stated, Lemma 1
    assumes ancillas "attached in diagonal states", that is, as tensor products. On C × H its proof goes through
    verbatim with no ancilla. A channel formalism on the carrier C cannot state this case.
  - Act 45 is relevant at its own layer (exact probe, not kernel). It finds that "an ancilla carried between steps
    as hidden basis states separates two dilations of one slice … at two steps, while an ancilla attached as a
    tensor factor leaves the rooted family equal to `Gᵗ`" (P/track-b/act-45-fixed-basis-image/result.md:5, 36-39).
    Carried hidden memory and a fresh discarded ancilla are not interchangeable objects, and its full treatment
    belongs to the A5 cluster.

**Access.** The observer reads and writes every configuration. A restricted observer acts on a different carrier, a
visible subsystem. Its theory falls under the no-go only by the paper argument above. `obs_availExt_le_substratum`
proves only `obsTheory ⊆ substratumTheory` (OIB/SubstratumInterfaceAudit.lean:836-840).

**Rule-independence holds by definition.**
- `obsTheory_rule_independent` closes by `rfl` (OIB/SubstratumInterfaceAudit.lean:780-782).
- `sourcing_rule_independent` closes by `Iff.rfl` (OIB/FrozenSourcing.lean:295-299).
- `phase_ceiling_rule_independent` is a genuine theorem, and it holds for every substratum (:302-305).

**Outside the statement.** Encoded carriers fall outside the no-gos' statements: a fixed map from laws on several
cells to density operators (AP1, MECH-1, MECH-2, ε-gluing). They are representation, not mechanism. MECH-1's SC-3
check reads: "**Representation only.** On the physical carrier every step is a permutation … What is physical is the
record statistics, which … are produced by an exact noncontextual hidden-variable model"
(R/mechanism-1-20261107/DESIGN.md:901). MECH-2's reads: "The capability is in the representation"
(R/mechanism-2-20261108/DESIGN.md:763). Arc D's S1 makes "represented" a disqualified ground for sourcing as a
theorem (P/track-i/arc-d-operational-sourcing/result.md:40-43; kernel, OIB/OperationalSourcing.lean).

**Phase-1 flags after re-verification.**
- **MQ-14, "witness→theorem".**
  - For Main:590's own kernel citation, the flag stands (§1, B1).
  - The universal content exists in `substratumGen_not_control`, `substratum_residual` and `permTheory_not_control`.
    Main:590 does not cite these; GR:260 cites `substratum_residual`.
- **MQ-14, A3 "hidden register not modelled".** Partly confirmed. At the kernel layer only fresh uniform ancillas
  outside the carrier are modelled. Pre-correlated external memory is covered on paper only (AP1 Lemma 1 on the
  enlarged carrier).
- **MQ-16, A3 "hidden sector is not a carrier".** Incorrect: "the system qubit carries the HIDDEN bit"
  (OIB/OIRealization.lean:15-18).

***

## 1. MQ-14: "finite reversible read-write dynamics, even with genuine hidden-memory and readback behavior, does not itself generate quantum state mixing" (with Intro:129)

**Statement as made.** Main:590 reads "…while finite reversible read-write dynamics, even with genuine hidden-memory
and readback behavior, does not itself generate quantum state mixing (kernel: `substratum_plus_control_qm`, with the
converse `qm_generated_by_substratum_extension`, in `OIBridge/StructuralClosure.lean`, `readWriteSourced_not_qm` in
`OIBridge/ReadWriteControl.lean`)".

The same sentence appears verbatim at:
- GR:260;
- FULL:500 and FULL:5271;
- book/ch01-observation.md:165 and book/ch19-open-problems.md:126;
- the generated derivatives papers/Main.tex:3915, papers/GR.tex:1850 and
  book/The-Incompleteness-of-Observation-FULL.tex:2235 and :24181;
- verification/programmes/substratum/source-audit.md:199-200. This record declares itself frozen ("The audit is
  complete and frozen at this entry", :191), but it has been appended to since (":211 Fifth entry, recorded after
  the freeze"). It is not listed in `verification/infrastructure/legacy-records.json`. It is therefore an
  append-only record by its own convention, not a governed frozen record. The owner decides how it is corrected.

Related restatements: Main:82 and :584 ("(iv) … not supplied … on the two-state carrier"), Main:216, :354 and :776
(without the two-state qualifier), GR:228, and Intro:129.

**B1: `ReadWriteSourced` is unsatisfiable, so `readWriteSourced_not_control` and `readWriteSourced_not_qm` hold
vacuously.** This finding is not new. It is already recorded on `main`:
- R/quarter-phase-native-20261107/DESIGN.md:864-866: "the vacuity of `ReadWriteSourced`, which requires an available
  `V` to equal `permMatrix σ` exactly although `id = conjChannel(i·1)`";
- R/minacc-1-20261108/DESIGN.md:585 ("The vacuous `ReadWriteSourced` family (#1188) is not cited") and :619, a control that checks the family is not cited;
- R/minacc-1-20261108/RESULT.md:613;
- R/quarter-phase-feedback-20261107/RESULT.md:187.

It is tracked in open Issue #1188, "KERNEL-VAC-1: `ReadWriteSourced` is vacuous; repair or retire
`readWriteSourced_not_qm`/`_not_control` and repoint their citations" (read via the REST API, 2026-11-08). #1188 is the
accountable home for every citation defect listed below. This audit opens no separate obligation. The argument below
is the auditor's independent re-derivation on paper. No kernel proof of the unsatisfiability exists on `main`. The
relevant definitions, quoted:
- `def ReadWriteSourced (T : FiniteOperationalTheory A) : Prop := ∀ (n : ℕ) (V : Matrix (A × Fin n) (A × Fin n) ℂ),
  T.availExt n Unit (fun _ => conjChannel V) → ∃ σ : Equiv.Perm (A × Fin n), V = permMatrix σ`
  (OIB/ReadWriteControl.lean:158-160).
- The `FiniteOperationalTheory` fields `readout_avail : ∀ n : ℕ, availExt n (Fin n) (readout n)` and `readout_local`
  (OIB/OperationalAssembly.lean:642-644), with `theorem readout_is_localLuders … : T.readout n k = localLuders k`
  (:658-660).
- `availExt_coarse : … availExt n O F → availExt n O' (fun a => ∑ j ∈ Finset.univ.filter (fun j => f j = a), F j)`
  (:608-612).
- `def localLuders (k : B) … toFun X := Matrix.of fun p q => if p.2 = k ∧ q.2 = k then X (p.1, k) (q.1, k) else 0`
  (:191-193).
- `def conjChannel (V : Matrix S S ℂ) … toFun X := V * X * Vᴴ` (OIB/MonoidalCompletion.lean:360-361).
- `def permMatrix (g : S ≃ S) : Matrix S S ℂ := fun i j => if g j = i then 1 else 0` (OIB/CoherentLift.lean:92-93).

The argument, for any `T`:
1. Take `n = 1`. On `A × Fin 1`, `p.2 = 0` always holds and `(p.1, 0) = p`, so `localLuders 0` is the identity map.
2. By `readout_avail 1` and `readout_is_localLuders`, `availExt 1 (Fin 1) (fun _ => id)` holds. Coarse-graining along
   `Fin 1 → Unit` gives `availExt 1 Unit (fun _ => id)`, because the filtered sum has the single term `j = 0`.
3. `conjChannel (-1) X = (-1)·X·(-1)ᴴ = X`, so `fun _ => id` equals `fun _ => conjChannel (-1)` by `funext` and
   `LinearMap.ext`.
4. `ReadWriteSourced T` would then give `-1 = permMatrix σ` for some σ. The diagonal entries of `permMatrix σ` lie in
   {0, 1}, and `A × Fin 1` is nonempty whenever `A` is, so this is impossible.

Hence `∀ T (A nonempty), ¬ ReadWriteSourced T`. The root cause is that the definition demands exact equality with a
permutation matrix, while `conjChannel` cannot see a global phase. `MonomialSource` is not affected, because
`IsMonomial` is closed under unit scalars, as QA DESIGN.md:864-866 notes for `permClass`. `readWriteSourced_monomialSource` (:162-166) is vacuous for the same
reason. `readWriteOperator_monomial` (:99-102) is not vacuous, but it is the triviality "a bijection's matrix is a
permutation matrix".

**Consequences for the citations.**
- Main:590's only kernel citation for the negative clause is a vacuous theorem; its other two citations are the
  positive endpoint.
- GR:260 also cites `substratum_residual` (StructuralClosure.lean:383-392), which contains the non-vacuous
  `substratumGen_not_qm`.
- The book mirrors defer to GR §3.3.
- Records citing `readWriteSourced_not_qm`:
  - verification/README.md:298 cites it alone.
  - verification/programmes/substratum/source-audit.md:100 and :121 cite it, the former beside
    `offDiagonal_interp_not_monomial`.
  - verification/audits/operational/completion-assumption-audit.md:95 cites it beside the non-vacuous
    `substratumClass_not_drivesElementary`.
  - verification/programmes/substratum/route-b-audit.md:29 cites it beside `substratum_residual`.
- The Lean docstring OIB/RouteB.lean:13 also cites it.
- Several entries only record that the theorem is present and carry no support:
  - the probes `verification/lean/bohr_frequency_probe.py:9048-9055` and `edge_rigidity_probe.py:1016-1017, 1946-1947`;
  - the census entries at verification/audits/manuscript/intro-corpus-audit-20261026/unit5-evidence/REVIEW.md:686-687;
  - `unit5-evidence/u5_reports.tsv:169-170`;
  - `introduction-repro-ext/results-121598983127-28.json:4120` and `:4129`.
- **Kernel check: deferred to #1188, not a new obligation.** A one-lemma check would settle the vacuity:
  `theorem not_readWriteSourced [Nonempty A] (T : FiniteOperationalTheory A) : ¬ ReadWriteSourced T`, built from
  `readout_avail 1`, `availExt_coarse`, `readout_is_localLuders` and `conjChannel (-1) = LinearMap.id`. It is
  decisive in one direction. If it compiles, the vacuity is kernel-certain. A failed attempt is diagnostic only,
  since it may be a proof-engineering failure.

**Where the non-vacuous content is proved.**
- `substratumGen_not_control` and `substratumGen_not_qm` (OIB/StructuralClosure.lean:348-361; kernel; on `Fin 2`;
  phases stipulated in `substratumClass`). The read-write operators are in the class (`readWriteOperator_supplied`,
  :336-338). These are universal over the class, not a witness.
- `permTheory_not_control [Nonempty A]` (OIB/SubstratumInterfaceAudit.lean:708-709; kernel; every carrier; the
  phase-free access).
- `monomialSource_not_control` (OIB/SubstratumInterface.lean:186-189; kernel; on `Fin 2`).
- **For general carriers with phases stipulated (N4).** `¬ HasCompositeUnitaryControl (substratumTheory S)` for
  |S| ≥ 2 follows in a few lines (auditor, paper). Take σ a transposition. `substratumTheory_not_avail_gateFlow_half`
  (OIB/ExecSource.lean:113-117) shows the conjugation by the time-½ gate flow is unavailable at level 1.
  `gateFlow_unitary` (OIB/LiftAudit.lean:68-72) shows that operator is unitary. `HasCompositeUnitaryControl`
  (OIB/OperationalAssembly.lean:665-667) would make it available. This is an unstated kernel corollary, so the
  omission of "two-state" at Main:216, :354 and :776 is minor.
- `memorySwap` / `readWriteControl_independent` (ReadWriteControl.lean:216-218; kernel) is a witness. It shows the
  read-write class contains a nontrivial exchange. The kernel identifies it with "C4/readback" only in a docstring
  (:46-51, 186-187).

**Hypotheses, and where each enters.**
1. **Complex kinematics.** It is the type of `FiniteOperationalTheory` (GR:216), so it is imported as the setting and
   labelled as such.
2. **The carrier identification (§0).** It enters through the definitions of `substratumClass` and `permClass`.
3. **Two-state carrier.** `substratumGen_not_control` is on `Fin 2`; the general carrier follows by the corollary
   above.
4. **Hidden memory.**
   - Kernel: hidden cells inside the carrier, and fresh uniform ancillas outside it.
   - Paper: fresh cells in fixed laws (AP1 Lemma 2), and pre-correlated external memory (AP1 Lemma 1 applied to
     the enlarged carrier).
   - Not covered at any layer: encoded identifications.

**Outcome 2 (valid but conditional), for the result.** The result is: no operation generated through the
configuration-carrier interface is a non-monomial conjugation. It is supported universally by
`substratumGen_not_control` (on `Fin 2`) and by `permTheory_not_control`, but not by Main:590's own citation, which
is vacuous. It is conditional on hypotheses 1–3. For hypothesis 4, the support is kernel-level as stated in §0
and paper-level for pre-correlated external memory.

**Class:** conditional.

**Texts that read it more strongly.**
- **Main:590, its mirrors and the source-audit record listed above.** The phrase "does not itself generate quantum state
  mixing" is unqualified as to carrier. The proof supports the interface statement above.
  - GR:260 gives the reason, "induces only permutation operators", which names the interface implicitly.
  - Main:590 and the book give no reason.
  - Main:590's kernel citation for the negative clause is vacuous (B1).
- **Main's ε-gluing theorem in the same section** applies the 3-4-5 rotation exactly to a hidden density register
  and realizes its outcome statistics. The visible law is off by at most `(|O|−1)/G` per step in total variation,
  strictly positive for 3-4-5 (Main:580). Each instrument has one fixed step map, selected by the intervention label
  (Main:566). The instrument is supplied as data. So at the level of statistics the sentence is true only through
  "itself", read as native sourcing.
- **Intro:129** opens with "A finite reversible world does not supply condition 4 on its own." That headline is
  OI-level. The scoped clause that follows ("Under the observer access stated in [GR §3.3] … condition 4 therefore
  fails for them on every system with two or more states") is supported by `permTheory_not_control`. The "cannot
  blend them" sentence is true of the ontic map; applying it to the observer's operations is the carrier
  identification.

**Merged records outside the statement (B3, B4).** None exceeds the no-go's physical content.
- **Encoded carriers.** AP1 and MECH-1 make encoded `Z`/`X` Lüders reads available under R1. The record's own words
  are "Phase-sensitive instruments are native" (MECH-1:183-185; paper). MECH-1 Lemmas N and M give the full
  single-qudit Clifford group at odd `q` through "explicit words" using NNB. NNB is "Supplied (QA conditional
  premise)" and P3-armed (MECH-1:85-87, :915, :917, :929-930; paper). Both are classified "Representation only" by
  SC-3 (MECH-1:901), and the reachable fragment is an exact noncontextual model (Proposition C(d), :763-766; paper,
  citing Spekkens).
- **ε-gluing (Main:566-580; paper plus exact probes `opglue_probes.py`).** It exhibits an **imported**
  infinite-order encoded unitary, the 3-4-5 rotation, applied exactly in the ring at horizon K. Its angle
  arccos(3/5) is not a rational multiple of π by Niven's theorem, so the rotation has infinite order in PU(2)
  (auditor, paper).
- **Native sourcing.** No merged record exhibits a **natively sourced** non-Clifford or infinite-order encoded
  unitary. These records bound it:
  - MECH-1 Proposition C(b): odd `q`, R-W frame, classes N and N+NNB (:751-758; paper).
  - MECH-2 node 8: odd `q`, R-W frame, Lemma F's hypotheses including H-LIFT (:742-747; paper).
  - MECH-2 Theorem U2: `q = 2`, frame R1, H-LIFT (:55-64; paper).
- **Open.** Whether encoded record statistics ever lack a classical model is open (§17, Q-C2-2).

***

## 2. MQ-15: layer-flow executability is not sourced (GR:266-274; Main:590, last two sentences)

**Statement as made.** GR:272 states "stated substratum dynamics with observer access ⇏ one nontrivial layer flow
executable". Main:590 states "…in every formulation stated that lands in the operational interface … the site-space
wave-operator formulation being unresolved rather than excluded".

**Where it is proved (kernel).**
- `obs_not_layerFlowExecutable` (OIB/ExecSource.lean:129-134);
- `bijectionLevel_not_layerFlowExecutable` (:89-92);
- `configurationLevel_not_avail_gateFlow_half` (:97-110);
- `coherentLiftClass_eq_substratumClass` and `derivedOI_qm_iff_layerFlowExecutable'`, as cited at GR:270.

The ExecSource header disclaims "anything about a richer observer architecture than the stated one" (:29-31).

**Hypotheses.**
- Complex kinematics.
- The identification of §0, entering via `ConfigurationLevel` and `BijectionLevel`.
- Exact availability at every time; the failure is at `t = ½`, level 1.

**Outcome 1.** GR:270 records both open routes: "whether every realization of those channels is
configuration-level is not decided" and the wave-operator formulation.

**Class:** conditional. **Over-reading texts:** none found.

***

## 3. MQ-16: "bare finite OI ⇏ QM" (GR:222; Intro:127; Main:564)

**Where it is proved (kernel).**
- `oi_alone_not_qm` (OIB/GeneralCarrier.lean:160-163), witnessed by `diagTheory` on `Fin 2`.
- `five_way_minimality`, as cited at GR:220.
- The core is one fixed C1–C4 process with the hidden bit as the system qubit (OIB/OIRealization.lean:15-27,
  234-242).

**Outcome 1.** A non-implication by countermodel. Physically, it says a classical theory realizes the classical OI
process.

**Class:** n.a.

**Texts.**
- GR:222 and Intro:127 match the result.
- "none supplied by bare finite OI" (Main:82, 216, 354, 356, 556, 584, 776) means "not entailed by the core", which
  `five_way_minimality` supports.
- Precision note: §1 uses the same word "supply" to mean "fails in the generated theory".

***

## 4. MQ-18: the classical-dimension obstruction (Main:560)

**Statement as made.** "no fixed finite realization is exactly operationally equivalent to even a single qubit's full
theory" (Main:560).

**Where it is proved.**
- The factorization `B = ΞM` is a paper derivation (Main:560).
- Unboundedness is imported from HKLP [55], with Garner–Müller [56] as an alternative.
- There is no Lean proof. The SIC remark is an exact probe (`nogo_probes.py`, Main:562).
- Main:602(3): "proved under the stated operational interface, the unbounded-dimension half imported".

**Hypotheses.**
- (a) **Fixed finite N for the whole realization.** Hidden memory is counted in N, so it cannot rescue the result.
- (b) **Factorization.** The post-preparation ontic law does not depend on the measurement choice, and effects are
  fixed response functions. Main:560 states this as an interface ("the ordinary preparation → finite ontic system
  → measurement one"); [55]'s coordinated version covers finite shared coordination.
- (c) **Exact equality** with the full continuum theory.

**B7: re-examined, and the r1 charge is withdrawn.**
- **Closed-world reading.** Setting generators are among the N configurations. A fixed finite world then has
  finitely many distinct settings and preparations. It supports only finitely many action-labelled families, while
  the qubit's instrument space is a continuum. This is Main:488's counting proposition (paper), which uses no (b).
  The qualitative conclusions restated at Main:584, :600, :774 and FULL:1254 therefore hold without (b).
- **Open-system reading.** Here (b) is load-bearing: settings are external, and (b) is the standard free-choice
  premise. In this reading a setting-dependent ontic law on N = 2 states could match any finite table, which is a
  standard remark and was not computed here. (b) is also load-bearing for the paper's own proof route, and for the
  quantitative claim that a specific finite HKLP experiment is not reproducible by N states.
- **Intro:135.** "runs through distributions over those N states" holds even with setting-dependent laws.

**Outcome 2.** The result is conditional on (b) only in the open-system reading and on the HKLP route. The closed-world
conclusion follows from (a), (c) and counting.

**Class:** conditional.

**Over-reading texts:** none established.

**Precision note.** Main:560 calls (b) an interface, while Main:403-412 calls the Bell analogue (iv) a posit.

**Records outside the class.** These are consistent with the no-go:
- ε-gluing and the uniform continuum grow N with accuracy (Main:598).
- The response table realizes a fixed finite family exactly (Main:602).

***

## 5. MQ-20: the Bell ceiling for a screened local completion (Main:366-395)

**Where it is proved.**
- A paper proof (Main:385-391).
- An exhaustive finite check over the 16 deterministic tables (`equivalence_recovery_probes.py`, check 11, Main:391).
- There is no Lean proof.

**Hypotheses, stated in the theorem.**
- (i) Determinism.
- (ii) One-step own-wing setting interventions (Main:368-371).
- (iii) Readouts outside the other wing's cone (:372-374).
- (iv) Measurement independence, labelled "a posit about the initial condition, not derived" (:374-376, 403-412).
- A ±1 outcome in every run (:376).
- The I_ont bound additionally requires a response-complete Ω (:427).

Ω contains all hidden memory, so hidden memory cannot rescue the bound. FULL:6271 states this correctly.

**Outcome 1.** **Class:** conditional.

**Restatements.** All carry the hypotheses:
- Main:22, :393-395, :564, :772;
- Substratum:48, :131, :467;
- Intro:143-145;
- FULL:4906, :6263, :6271.

**Outside the class.**
- The response-table construction realizes PR-box behavior when the wings share globally coupled, setting-dependent
  hidden dynamics, which violates (ii) and (iii) (Main:362).
- The adopted escape is ontic parameter dependence, H-Bell, which is open (Main:414).

***

## 6. MQ-23: "an explicit finite carrier … admits no visible-local CPTP coherent lift at all" (GR:194)

**Where it is proved (kernel).**
- `twoByTwo_affine_rigidity`, `twoByTwo_nonCP` and `twoByTwo_no_local_lift` (OIB/TwoByTwoNoGo.lean:246, 590, 606).
- The predicate `TwoTimeCoherentLift` (OIB/CoherentLift.lean:1206-1220) consists of:
  - CPTP Kraus operators on the visible factor, entering through `vlift K = K ⊗ 1` (:747-748);
  - fixed coherent dynamics;
  - a match at every `t`.

**Outcome 1.** The statement is witness-scoped.

**Class:** imported, as a representation target.

**Outside the class, in the record itself.** The table is globally reachable. This is probe F16, an exact rational
probe, not kernel (TwoByTwoNoGo.lean:6-7, 13-15, 32-33).

**Over-reading texts:** none. GR:194 keeps both "visible-local" and "explicit".

***

## 7. Main:590, "even with genuine hidden-memory and readback behavior"

This clause is covered in §1. Within the interface it is supported at the kernel layer for hidden cells inside the
carrier and for fresh uniform ancillas. For pre-correlated external memory the support is paper only. It is not
supported for encoded identifications, and no record claims it is. Main:590's own citation for the clause is vacuous
(B1), so on that citation alone the clause rests on the `memorySwap` witness.

***

## 8. MQ-17: ε-gluing as a possible counter-witness (Main:566-584, 598-602)

**Where it is proved.**
- A paper proof (Main:580).
- Exact probes in `opglue_probes.py`.
- The bound on the realized law at finite b is open (Main:580, 602).

**Hypotheses.**
- The CP instruments are supplied as data and computed exactly on a hidden density register.
- K uniform seeds are pre-loaded.
- Each instrument has one fixed step map, selected by its label (Main:566).
- The grid error is at most `(|O|−1)/G` per step (Main:580).

**Outcome 1** for the theorem in exact arithmetic.

**Class:** imported.

**Role in this cluster.**
- The construction lies outside the statement of MQ-14 (§1). It is an imported, infinite-order encoded unitary, not
  native generation.
- It does not counter MQ-18, because N grows with accuracy.

***

## 9. PROG: the F1-retirement reading (P/PROGRAMME.md:40, 82, 456, 515-521, 559-561, 634)

**Statements as made.**
- :40: "…every operation the present observer interface sources preserves nonnegative entries … and that the
  microscopic update rule contributes no availability beyond the configuration-level observer theory".
- :521: "returns an *Independent* verdict … F1 is therefore retired for this architecture".
- :634: "that architecture does not source the phase structure or dense unitary control".
- §6 defines *Independent* as "A countermodel shows that the structure does not follow from the current OI
  assumptions" (:559-561).

**Where it is proved (kernel).**
- `frozen_sourcing_verdict` on `permTheory (Fin 2)` (OIB/FrozenSourcing.lean:318-323).
- `nonnegBounded_verdict` (:327-330).
- `phase_ceiling_rule_independent`, for every substratum (:302-305).
- `DenseUnitaryControl` is defined only on `Fin 2` (OIB/DiscreteCompletion.lean:45-48). The restriction lies in the
  predicate's domain; it is not a narrowing of a more general result.
- The audit freezes "the observer architecture … nothing here adds … a carrier map" (FrozenSourcing.lean:6-9).

**Outcome 2.** The kernel verdicts are valid. The *Independent* label counts the frozen interface, carrier map
included, among "the current OI assumptions". The text bounds the conclusion by "for the presently stated
architecture" (:3, :40, :84, :521, :634), and that architecture includes the carrier map.

**Class:** conditional.

**Texts that read it more strongly.**
- **PROGRAMME:40, :82 and :521, "the microscopic update rule contributes no availability".** The kernel support is
  `rfl` / `Iff.rfl` (§0). That support shows only that the interface, as defined, does not read the rule. Under an
  encoded identification the rule does decide CP-ness. MECH-1 Proposition AS (:516-545; paper, odd prime `q`, R-W
  frame) shows the encoded action is CP iff the bijection is affine symplectic. This, too, is a representation-level
  statement (SC-3).
- **PROGRAMME:634 (reader-clarity note only, B3).** It keeps "for the presently stated architecture" but omits the
  "observer interface" wording that :40 carries. The encoded-carrier records do not show a physical mechanism
  beyond the frozen ceiling: they are representation only (§0).

The Clifford-only encoded ceilings (§1) give the dense-control half wider, paper-level support under H-LIFT. The
programme text does not cite them.

***

## 10. TI-D: Arc D RD1 (P/track-i/arc-d-operational-sourcing/result.md)

**Statement as made.** "…contributes no admissible operator outside `permClass` … That is an **access-level**
negative and it is bounded at the access" (result.md:124-131). The *Additional* phase disposition is inherited from
PR #521 and PR #515 (:28-30, :199-204).

**Proof.** Kernel: OIB/OperationalSourcing.lean, 53 results (:13-15).

**Outcome 1.** **Class:** conditional.

**Texts.**
- PROGRAMME:456 is scoped.
- PROGRAMME:638's "proved disqualified ground" matches S1 (P/amendments/amendment-2.md:11-14).

**Over-reading texts:** none.

***

## 11. TI-CR: causal readback (P/track-i/causal-readback-discovery/)

**Statement as made.** "`CausalReadback -> PIndivisibleWithin K` is **false on the same audited horizon**"
(result.md:18), witnessed by `I → B_(3/4) → B_(5/8)` (:20-26). The result is window-local (:37-40). The prior can flip
the verdict (:298-308).

**Hypotheses.**
- A fixed prior common to every root (preregistration.md:30-31).
- The W/S/R clauses (:50-66).

**Outcome 1.** A non-implication by countermodel. It is robust to relaxing M1: a fixed prior is a special case of a
root-dependent one.

**Class:** n.a.

**Texts.** PROGRAMME:143 ("not enough to guarantee") and Main:141 match the result.

***

## 12. IF-L3B: the H₀ rank profile is not stable under H₁ (P/interface/round-l3b-orthogonal-rule-controls/)

**Statement as made.**
- Outcome `L3B-READ`: "rank behaviour tracks edge-permutivity" (result.md:13-15, 50-52).
- Block 2 (:65-72), under H₁:
  - R_LL and R_LS: 80/143 κ OVER-RANK, all at rank 5;
  - R_5: 142/143 κ OVER-RANK;
  - R_NL: OVER-RANK under every hidden law.
- Under H₂ the edge-permutive cells show no OVER-RANK.

**Hypotheses.**
- H₀ is the uniform product law; H₁ is a correlated Markov law along the lattice; H₂ is the equal-slice null
  (preregistration.md:164-168).
- The observer OBS-R keeps its record external (:75).
- Exact integer certification. The record calls itself "Not a QM test" (result.md:177-185).

**Outcome 1** (computational classification). **Class:** n.a.

**Sign (N6).**
- OVER-RANK is "terminal for R4(r; G₃)", and AT-RANK feeds the EXPOSED label (preregistration.md:144-151, 173-177).
- The rank ≤ 4 profile under H₀ is therefore the property that **fits** the rank-4 target. Under H₁ that fit is
  removed in every edge-permutive cell.
- So this is hidden-law sensitivity of a reading favourable to the framework. It is not a no-go that a hidden law
  rescues.
- "NO-OVER-RANK-AT-A" is "never preservation of the ceiling" (:173-177).

**Provenance.**
- M5 can rest on R_LS and R_5, whose Block-1 records are in result.md.
- R_LL's H₀ figures come from "sealed, off-repository artifacts" (preregistration.md:42-50). This is §A.42 item 8,
  flagged and not adjudicated here.

**Over-reading texts:** none ("touches no manuscript", result.md:183-185).

***

## 13. MECH-2 and AW-EOI-1: H-C, H-LIFT, Theorem NC, and the M-INACC framing (R/mechanism-2-20261108/DESIGN.md)

**Statements as made.**
- :109-111: "Under injective encodings with H-LIFT and spanning-read certification, no dynamics escapes Theorem NC.
  Within that scope a nonclassical observer-level theory needs a change in the identification and access, not in
  the dynamics alone."
- :728-733: "Every nonclassical route at `q = 2` needs an ontic functional that the dynamics uses and the observer
  can never access. … Otherwise H-LIFT enlarges the carrier and Theorem NC applies again."
- :114-117: M-INACC is named "the missing premise".

**Layer.** Paper. Lemma F (:307-347), Theorem U2 (:349 ff.) and Theorem NC (:65-71) carry author self-checks only
(:13-15).

**Hypotheses, H-C and H-LIFT separated (B6).**
1. **Lemma F's operation set** (:313-318).
2. **H-LIFT** (:319-321): "every cell whose law is correlated with the encoded carrier belongs to the encoded
   carrier". This is achievable by enlarging the carrier: "the encoded description must be enlarged until H-LIFT
   holds" (:346-347; also :731-732). In a finite world the enlargement terminates.
3. **H-C** (FB, R/quarter-phase-feedback-20261107/RESULT.md:47-61; paper). The hidden lift `κ_v` may be correlated
   with `v`, but it is common to all preparations. Preparation-dependent lifts are excluded (:58-59). This is a
   genuine exclusion, and enlargement does not remove it.
4. **An injective fixed frame** (:322-323, :717-723).
5. **For Theorem NC, spanning-read certification.** At `q = 2` this needs a `Y` read "not exhibited natively"
   (:69-71, :795).

**What is substantive.**
- The substantive step is not H-LIFT, which enlargement supplies. It is transferring the enlarged-carrier conclusion
  back to the carrier the observer can access. That needs spanning certification on the enlarged carrier
  (hypothesis 5). At `q = 2` with native `Z`/`X` reads, the records show no spanning certification
  (MECH-2:69-71, :795). No general statement about embedded observers is made here.
- H-C excludes preparation-dependent hidden residues. Main:76 (C2-structural) says reversibility retains hidden
  records of visible history "for every law". Correlation-recombination (R/correlation-recombination-20261107/DESIGN.md:11-19;
  paper) exhibits native use of a hidden correlation without decoding, as a classical effect.

**Outcome.**
- Lemma F, Theorem U2 and Theorem NC, on hypotheses 1, 2, 4 and 5: **outcome 2**.
- The M-INACC framing at :728-733: **outcome 3**. It is justified by three facts:
  - Theorem NC needs spanning certification (:69-71), and the record itself says A6 is undecided at the native
    `Z`/`X` level (:795).
  - "every nonclassical route" rests on an enumeration of routes (:706-727), not a theorem.
  - An accessible but uncertifiable functional falls in neither horn of the dichotomy.
- :713 shows only that the H-C route is unshown (N9).

**Class:** conditional.

**Context.** M-INACC-1 is "WIP / UNVERIFIED" and model-reviewed only (R/minacc-1-20261108/RESULT.md:3-7). It finds
that the protected `Q* = 1` functional of the symmetric graph `G_σ` is determined by an allowed protocol
(RESULT.md:41-53). This is one failed inaccessibility instance, not a verdict on the framing.

***

## 14. MECH-1 "Selection passes natively" (R/mechanism-1-20261107/DESIGN.md:1, 64-74, 120, 931) and AW-EOI-5 (C-CP as filter)

**Statement as made.**
- The title (:1).
- "Selection passes natively at odd `q` in the stated form" (:120).
- O3: "**Pass natively**, in the form of node 4" (:931).

**Layer.** Paper. Independent cross-checks are review provenance only (:11-15, :1173-1177).

**What carries the O3 verdict.**
- **Proposition AS** (:516-545): odd prime `q`, R-W frame, proved in both directions. It is bijection-level.
- **Theorem W** (:66-69) for "every available branch CP". This needs:
  - P1, supplied and load-bearing (:913);
  - P2, supplied and load-bearing (:914);
  - N2 via the open H-PREP (:912, :916).
- **Further supplied or imposed premises.**
  - N1-A5, "linearity imposed" (:908).
  - P3 arming (:915; O1 fails on P3, :929).
  - NNB for the N+NNB column (:917).
- **The R-W frame**, "singled out by Clifford covariance, a property of the comparator" (:899, :918).
- **The C-CP criterion** as the O3 pass condition (:325-330).
- **The memory sign** is conditional on #1193 (R/mechanism-2-20261108/DESIGN.md:739, 755).

**Outcome 2.** **Class:** conditional, with an imported comparator.

**Over-read.** "natively" (:120, :931) is supported only for the affine-symplectic dynamics. The record discloses each
supplied element (:899-901, :907-921), but the headline exceeds them. The selected fragment is classical: Proposition
C(d) (:763-766), and C-COMP "is passed equally by the mechanism's own classical model" (:88-92).

**AW-EOI-5.** C-CP verdicts are frame-relative: "These CP verdicts are relative to R1" (R/mechanism-2-20261108/DESIGN.md:61-63).
- "fails C-CP" means only that the encoded map in that frame is not a quantum channel. It does not mean the
  statistics are physically unrealizable.
- "passes C-CP" does not imply nonclassicality.

"Quantum selection: fails" (MECH-2:99, :792) is valid as a frame-relative statement: outcome 2, imported comparator.

***

## 15. states-dynamics 8.a and AW-EOI-4: the bounded-state controller obstruction (R/states-dynamics-audit-20261024/)

**Statement as made.**
- "every controller whose whole persistent state is finite, with a time-independent update and B fair fresh bits per
  slot, also has T(h)->1 on this protocol, for any initial law" (CURRENT-HANDOFF.md:77-80).
- The class allows an arbitrary initial law, "non-dyadic laws included" (a2_memory_v8/REPORT.md:29-34).
- The retained-seed reset escapes with linearly growing memory, "granted the target cuts" (CURRENT-HANDOFF.md:84-85).
- The five-valued source escapes, "computed exactly through h = 12" (:90-93).
- "Nothing here concerns … OI" (REPORT.md:6-7).

**Layer.**
- A paper proof (REPORT.md:64-95).
- An exhaustive finite check of step 5 (:110 ff.).
- Internal review recorded under `review/` (CURRENT-HANDOFF.md:72-77).

**Outcome 1** for the record's own statement. **Class:** n.a. as the record states it.

**The OI reading (B5; auditor observation, not in the record).**
- Step 5 needs only that the transition entries lie in `2^-B·ℤ`. With B = 0 the matrix `D_1` has integer entries,
  and λ = 4/5 is not an integer, so the proof goes through unchanged (REPORT.md:91-95; auditor, paper).
- A finite closed OI world is therefore inside the no-go. It has a fixed bijection, a finite prior (possibly
  non-dyadic, for example uniform on `F_5`), and finite whole state including any clock. In such a world T(h) → 1
  on this protocol. This is consistent with Main:640's all-time negative for fixed finite realizations.
- Every exhibited escape needs memory or randomness that grows with depth:
  - the retained seed uses linearly growing private memory;
  - the five-valued source needs a fresh symbol every slot, which a finite world can supply only from pre-loaded
    seeds growing with h (compare Main:566's K seeds);
  - the five-valued escape is in any case a finite test to h = 12.
- The record does not call the obstruction a limit of the controller model. r1's statement that it does is
  withdrawn.

**Texts.** R/oi-pseudoentropy-20261025/README.md:66-76 keeps the record's scope.

***

## 16. Markers M1, M4, M5 and M7

- **M1.** M1 is not load-bearing for this cluster's negatives.
  - TI-CR's countermodel survives any enlargement of the prior class (§11).
  - The periodicity necessity of `C_OI ⊆ PPer` (Main:640) holds root by root. This is an auditor remark on paper.
- **M4.** M4 lands on three texts:
  - MQ-14's prose and citation (§1);
  - the Intro:129 headline;
  - PROGRAMME :40, :82 and :521, plus a clarity note at :634 (§9).

  It does not land on GR:272, TI-D or GR:194.
- **M5.** L3B (§12) confirms M5, with the sign corrected: it is hidden-law sensitivity of a favourable fit.
- **M7.** M7 affects positive readings only (P/track-i/arc-b-rooted-classification/result.md:60-63, 86-91).

***

## 17. Follow-up questions

Both questions below are **named only, for owner decision. They are not authorized, adopted or started.** The owner
direction reads: "No … new scientific investigations are authorized until the reconciled findings are reviewed". The
`ReadWriteSourced` kernel lemma (§1) belongs to the existing Issue #1188. It is not a new question here.

**Q-C2-1 (B6). r1's question is withdrawn as posed and split.**
- **Disjunct (ii), dropping H-C, is merged into Q-C2-2.** Without H-LIFT, enlarging the carrier restores Theorem U2
  on the enlarged carrier (MECH-2:346-347). A preparation-dependent branch on the small carrier therefore decides
  nothing. The decisive object is the operational theory the observer can access.
- **Disjunct (i), non-injective identifications, keeps one narrow question.** It is already recorded as open
  (MECH-2:717-727).
  - **Setting.** U′ is two `F_2` cells `(z_1, x_1)` and `(z_2, x_2)`, 16 configurations, with
    `f_z = z_1`, `f_x = x_1`, `f_y = z_1 + x_1 + z_2 + x_2` (R/quarter-phase-native-20261107/DESIGN.md:448-450).
    - The identification R is the Bloch map `r_a(μ) = E_μ[(−1)^{f_a}]`, a ∈ {x, y, z}. Derived (auditor/reviewer,
      paper); no record states it on all laws. Its two ingredients are stated separately:
      - native read: "A read of axis a returns f_a; bit 0 denotes the + eigenvalue" (FB RESULT.md:43-44); node 8 read
        transitions on the level-set family only (QA DESIGN.md:583-589);
      - outcome rule: "probability (1 + (−1)^b r_a)/2" (QA DESIGN.md:116-117), which belongs to the imported comparator
        (I1, QA DESIGN.md:108-113).
      - Together these give `r_a(μ) = μ(f_a = 0) − μ(f_a = 1)` on every law.
      - It agrees with QA node 8 on that record's family: `r(Λ_{a,b}) = (−1)^b e_a` and `r(Λ_0) = 0`
        (QA DESIGN.md:580-601).
    - **Caveat (reviewer, paper).** On all laws, R is not state-valued.
      - Point laws give `|r| = √3`.
      - No positive extension of U′'s identification to all laws exists: point laws with `z_1 = 0` would have to be
        `|0⟩⟨0|`, and those with `x_1 = 0` would have to be `|+⟩⟨+|`.
      - R therefore maps all laws onto the cube `[−1,1]³`, as a read-statistics (frame-type) map, like MECH-2's
        Lemma F frames on signed laws.
    - R is not injective: 16 configurations map to 3 Bloch coordinates.
    - A protocol is any stochastic map B on laws of the 16 configurations built from Lemma F's operations: fixed
      bijections of the carrier together with attached cells, cells attached in **any fixed law** and **discarded
      by marginalization**, and record conditioning with a state-independent herald probability.
    - Φ is *encoded-induced* on a set L of laws if `R∘B = Φ∘R` holds on L.
  - **Reduction lemma (auditor, paper; re-derived by reviewer; not in any record).** Suppose L is *all* laws on the
    16 configurations. Then every encoded-induced unitary Φ is a single-qubit Clifford channel. Because R is
    frame-type (caveat above), the all-laws form is a frame-type statement, stronger than any requirement on states.
    - *Proof sketch.*
      - Write `h_a = Bᵀ(−1)^{f_a}`, a function on the 16 configurations. Its values satisfy `|h_a(w)| ≤ q`, where q
        is the herald probability (q = 1 if there is no conditioning).
      - Over all laws the 16 character expectations are independent coordinates. So `r'_a = E_μ[h_a]/q` can be a
        function of `r(μ)` only if `h_a ∈ span{1, χ_x, χ_y, χ_z}`. Write `h_a/q = α_a + Σ_b β_ab χ_b`.
      - f_x, f_y and f_z are linearly independent, so all eight joint sign patterns occur. Hence
        `|α_a| + Σ_b |β_ab| = sup|h_a|/q ≤ 1`.
      - Unitarity needs α = 0 and β ∈ SO(3). A row with ℓ2 norm 1 and ℓ1 norm ≤ 1 has exactly one entry ±1.
        So β is a signed permutation matrix with determinant +1, an octahedral rotation, which is Clifford.
    - *Second proof (reviewer, paper).*
      - R maps laws onto the cube, and `R(Bμ)`, normalized after any herald, is again R of a law.
      - So `β(cube) ⊆ cube`, and a rotation with that property is octahedral.
      - This proof also covers state-dependent heralds and any stochastic map B, bijective or not.
    - So the all-laws form of the question is **closed at paper level (auditor; re-derived by reviewer)**, negatively,
      for every bijection, every attached-cell law and every number of steps, with no enumeration.
  - **The reachable-laws form.** L is the set of laws reachable from the supplied preparations (P2, H-PREP). There Φ
    need agree only on R(L), and B is non-unique (MECH-2:718-720).
    - **Closable sub-case (reviewer, paper; integer control for m ≤ 5 only).** Protocols with no record
      conditioning and with dyadic supplies (N2 uniform), following QA's C-ROT premise (QA DESIGN.md:646-651).
      - The columns of β then have entries in `2^{−m}ℤ`.
      - An orthogonal row then needs integers with `k₁² + k₂² + k₃² = 4^m`. By 2-adic descent the only solutions
        are `(±2^m, 0, 0)` up to order, which forces a signed permutation, hence octahedral.
      - The reviewer's integer control checked the descent only for m ≤ 5.
    - **Still open.**
      - Non-dyadic supplies: non-uniform hidden or attached-cell laws. QA says "With non-uniform hidden priors the
        dyadic argument is unavailable" (:649-650).
      - Any record-conditioned protocol. Heralds introduce other denominators: a 3/4 herald gives denominator 3,
        and non-octahedral orthogonal rows such as `(2/3, 2/3, −1/3)` exist.
    - No runnable cheap check is named for the open part. It first needs a characterization of L, which the records
      do not state.
  - **AGL(4,2) confirmation.** It covers only the bijection subclass, where `h_a` takes only the values ±1, so it
    does not exercise the fractional case of the ℓ1 step.
    - The check runs over the affine bijections of the bare 16-configuration carrier, |AGL(4,2)| = 322,560, with no
      attached cell, nothing discarded and L = all laws.
    - The reviewer ran it as a control (`rv4/agl.py`). Of the 322,560, 768 induce a Φ:
      - 384 are octahedral rotations (det +1);
      - 384 are reflections (det −1, Lemma R type). These are encoded-induced maps but not CP, so not unitary
        channels.
    - No other case occurs.
    - This is a control, not evidence. It decides nothing about attached cells, discards, non-affine maps or
      reachable-law restrictions.

**Q-C2-2. The M-INACC dichotomy (MECH-2:728-733).**
- **Question.** At `q = 2`, with native `Z`/`X` reads only, is there a protocol satisfying all three conditions?
  - (a) A functional of an active hidden cell is used by the fixed rule and is partially accessible, with an
    explicit accessibility witness. The witness must be for the functional that `G_SM` uses in P★. M-INACC-1's
    protocols `E_A` and `E_B` are for a different rule, `G_σ`, so they serve as a template only
    (R/minacc-1-20261108/RESULT.md:41-53; WIP/UNVERIFIED).
  - (b) That functional is not spanning-certifiable, checked for the same `G_SM`/P★ instance.
  - (c) The encoded record statistics admit no exact noncontextual model.
- **Cheapest check.** The finite noncontextuality linear program on P★'s fragment (MECH-2 node 6):
  - preparations: P★'s heralded branches and the mechanism-off stabilizer preparations;
  - effects: the native `Z` and `X` reads at the record times stated there;
  - operational equivalences: only those certified by native reads;
  - exact rational arithmetic.
- **Why it is decisive.**
  - Infeasibility refutes the "never access" dichotomy for that instance only together with instance-specific
    checks of (a) and (b). Contextuality alone does not show partial accessibility.
  - Feasibility closes the instance.
- **Caveat.** P★ fails C-CP, so an infeasible result would give a nonclassical fragment that is not quantum.

No outcome-3 question is raised for MQ-15, MQ-16, MQ-18, MQ-20, MQ-23, TI-D, TI-CR, L3B or 8.a.

***

## Summary (≤ 25 lines)

1. Outcome 1: MQ-15, MQ-16, MQ-20, MQ-23, TI-D, TI-CR, L3B, 8.a. Outcome 2: MQ-14, MQ-18, PROG, MECH-2 NC/U2, MECH-1
   "selection", C-CP verdicts. Outcome 3: the M-INACC framing (MECH-2:728-733).
2. B1 (on `main` already, #1188; re-derived): `ReadWriteSourced` is unsatisfiable (id = `conjChannel (-1)`), so
   `readWriteSourced_not_qm`/`_not_control` are vacuous: Main:590's only negative citation, also at GR:260,
   verification/README.md:298, source-audit.md:100/121, completion-assumption-audit.md:95, route-b-audit.md:29.
3. The MQ-14 content survives on `substratumGen_not_control` (on `Fin 2`), `permTheory_not_control` (every carrier)
   and an unstated corollary. The witness→theorem flag stands for Main:590's own citation.
4. "does not itself generate quantum state mixing" lacks the interface qualifier at Main:590, GR:260,
   FULL:500/5271, ch01:165, ch19:126, Main.tex:3915, GR.tex:1850, FULL.tex:2235/24181 and the
   self-declared-frozen, appended source-audit.md:199-200.
5. Hidden memory: the kernel covers in-carrier cells and fresh uniform ancillas; pre-correlated external memory is
   paper only (AP1 Lemma 1, enlarged carrier). Act 45's probe separates carried ancillas from fresh ones.
6. Encoded carriers lie outside the no-gos' statements and are representation only (SC-3, Arc D S1). No natively
   sourced non-Clifford encoded unitary exists on `main`; ε-gluing exhibits an imported, infinite-order one.
7. PROGRAMME:40/82/521's "the rule contributes no availability" is definitional (`rfl`/`Iff.rfl`). :634 warrants a
   clarity note only.
8. MQ-18: the r1 charge is withdrawn; closed-world conclusions follow by counting (Main:488), and (b) is
   load-bearing only for the open-system/HKLP route. MQ-20's restatements all carry their hypotheses.
9. H-LIFT is supplied by enlargement; H-C excludes the residues Main:76 makes generic. The gap is the transfer
   back to the accessible carrier without spanning certification (MECH-2:69-71, 795).
10. MECH-1 "natively" exceeds what is native: P1/P2/H-PREP, P3, NNB and imposed linearity are supplied, and the
    frame and C-CP come from the comparator.
11. 8.a (auditor, paper): a finite closed OI world with any prior is inside T→1 (B = 0). Every escape needs memory
    growing with depth. L3B: H₁ removes a favourable rank-4 fit; no no-go is rescued.
12. Q-C2-1(i) all-laws form closed at paper level (auditor; re-derived by reviewer); reachable form open (§17).

## Cross-cluster assumption-watch markers

- **CI-1, carrier identification.** Statements that OI or its substratum "does not source X" are relative to
  (P-a)–(P-c). Encoded re-identifications are outside the statement but representation only. Physical exceedance
  needs record statistics without a classical model.
- **VQ-1, vacuous hypotheses.** An exact-equality predicate on `conjChannel` operators can be unsatisfiable when it
  excludes `c·V` for some unit scalar `c`, because every theory has `id = conjChannel (c·1)` available at level 1.
  `ReadWriteSourced` is the recorded case (#1188). Check whether a hypothesis is closed under unit scalars.
- **RI-1, definitional rule-independence.** `obsTheory` reads only `Conf`.
- **HC-1, H-C versus H-LIFT.**
  - H-LIFT is supplied by enlargement.
  - H-C excludes preparation-dependent residues, which Main:76 says reversibility retains.
  - Spanning certification is the transfer step.
  - The kernel models external hidden memory only as fresh uniform ancillas.
- **MI-1, measurement independence.** It is load-bearing for Bell (iv). For MQ-18 it is load-bearing only in the
  open-system/HKLP route, and it is labelled an interface rather than a posit.
- **FV-1, frame-relative CP.** C-CP pass/fail depends on the frame (R1 or R-W). A pass does not imply
  nonclassicality.
- **FT-1, finite tests.** The five-valued escape is tested only to h = 12. The TwoByTwo global witness is a probe.
  MECH-2's "every route" is an enumeration.
- **SG-1, sign of hidden-law sensitivity.** Check whether a hidden law removes a no-go or removes a favourable fit
  (L3B is the latter).
- **PV-1, provenance (§A.42 item 8).** L3B's R_LL and 3A inputs are off-repository.
