# REVIEW-OICORE-1: independent adversarial review of OICORE-1 (r1)

- **Reviewed file.** `OICORE-1.md`, sha256
  `ed828f1607c15e7c208cf4518c88093d58b7915202b01b98fae0b267d5788da6` (re-hashed before review; 333 lines).
- **Version note.** While this review was in progress the writer replaced `OICORE-1.md` with r2
  (sha256 `6e70e3cf23f235aa4cdfc83fbbba160b3f403af4d6d0ecf34f0594497839b680`, 368 lines, mtime 17:27:08Z). r1 is preserved
  byte-identical as `OICORE-1-r1.md` (sha256 re-checked: `ed828f16…88da6`). **This review covers r1 only.** Line numbers
  refer to r1. r2 has not been reviewed, and nothing here certifies it.
  Also reviewed: `controls/c1_core_access.py`, and `src/` (git-archive extract of `2cd49dc0`).
- **Snapshot.** `origin/main` = `2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`. All Lean, paper, book and record citations
  were re-read at that commit. No Lean build was run.
- **Governing text read.** #1169 c.6724391385 (authorization, amaybaum 2026-11-08T17:02:10Z), c.6723491138 (ADA ledger),
  c.6723571280 (witness principle), c.6723889799 (the two routes), c.6723585151 (EOI directions), and #1188 (body).
  AGENTS.md: Code Review Rules, §A.19, §A.29, §A.31, §A.34, §A.42, §A.46.
- **Standing.** This is a model-written, read-only review. It edits nothing in the repository, changes no scientific
  status, and is not human verification.
- **Controls run (labelled; not evidence).**
  - The draft's `c1_core_access.py` was re-run. Output: C-A True, C-B True, CC True. It reproduces.
  - `review/rc1_rot_root_of_unity.py` (new) is an exact check of the FIN-row algebra in §3.2. It is green:
    - `(3+4i)/5` has minimal polynomial `5x²−6x+5`.
    - `(−7+24i)/25` has minimal polynomial `25x²+14x+25`.
    - Neither polynomial is monic, so neither number is a root of unity.
    - Countercontrol: `i` has minimal polynomial `x²+1` and is a root of unity of order 4.

## Verdict: **REVISE**

The kernel-facing core of the audit holds:

- F1 is correct, conjunct by conjunct.
- F2 is correct.
- The `_hoi` observation is correct.
- The Lean, paper and record line citations check out, with one exception (N7).

The central answer is overstated or mis-scoped in ways that a reader would carry forward:

- Lemma M is applied to candidates that are never formalized as predicates on `T`. Its kernel witnesses do not satisfy
  the access candidates it is used for (B1).
- The no-go inheritance table treats non-implication results as if they were universal no-gos (B2).
- The open route of §5(c) conflates the owner's *accessible-but-uncertifiable* route with an *inaccessible* functional
  (B3).
- §5(b) and the §5(d) assumption-watch argue from *exact* control, which the draft's own FIN row already excludes. They
  also state as general a claim about restrictions that holds only for restrictions alone (B4).
- F3 reads OI's own C1 mechanism as a defect of the core (B5).
- The off-`main` gaps must be traced one by one and closed before the record lands (B6).

All of these can be fixed in text. None needs Lean or computation.

## What was verified (no change needed)

1. **F1 holds exactly.** `RealizesSealedOICore` (OIRealization.lean:234-242) has six conjuncts.
   - Conjunct 1, `CoreC1C4`, is a closed proposition, proved by `core_isC1C4` (IndependenceCensus.lean:187-200).
   - Conjunct 4 holds for every `T`. `T.readout` is a structure field, and `readout_is_localLuders`
     (OperationalAssembly.lean:658) forces it to equal `localLuders` for every theory.
   - Conjunct 5 holds for every `T`, by `readVisible_family_eq` and `readout_relabel_available` (:140-157).
   - Conjunct 6 does not mention `T`: `realizedFold` uses only `transport coreIdx`.
   - So `OICore T ⟺ Avail_T(σ̂) ∧ Avail_T(τ̂)`. The → direction is projection; the ← direction uses the four lemmas.
     Both directions are identified, as §A.34 requires.
   - `label_not_oiCore` uses `h.2.2.1.2 ()`, i.e. conjunct 3 (PassiveIndependence.lean:237-238).
2. **F2 holds.** The core is upward-closed in the level-4 `Unit` families. This is already the corpus's own reading:
   CompletedOI.lean:523-526 ("operationally rich enough to build the four-state hidden-memory gadget") and GR:228.
   "ELABORATING" is the right label.
3. **The `_hoi` binder is unused, and no paper or book file cites `oi_compatible_iff`.**
   - The binder is unused: `oi_compatible_iff` (GeneralCarrier.lean:177-179) is `exactAll_iff_wellFormed_substantive T`.
   - The citation half was checked with `git grep` over the whole tree. The only hits are
     `verification/lean/bohr_frequency_probe.py:7785`, `verification/lean/edge_rigidity_probe.py:884` and two
     audit-result JSON files.
   - On the classification of this finding, see N1.
4. **The kernel facts used by Lemma M are correct as cited.**
   - Upward closure of `HasCompositeUnitaryControl` (OperationalAssembly.lean:665-667).
   - `diag_not_control` (DiagonalTheory.lean:390), `permTheory_not_control` (SubstratumInterfaceAudit.lean:708) and
     `physical_of_exactAll` (PhysicalCharacterization.lean:301).
   - `five_way_minimality`, third clause (RankGapTheory.lean:711-714): V, I, Cl, L1 and the core hold, and control
     fails.
5. **The record quotes were checked.**
   - AP1:153-163 (Lemma 2) and AP1:338-343 ("The native dynamics does not enforce terminality … `φ^N = id`").
   - M2D:114-117 (M-INACC) and M2D:483-497 (Theorem NC).
   - Main:28, 34, 38, 40, 44, 46, 48, 50, 56, 60, 62, 72-80, 86, 556, 566, 582, 590, 592, 640; Intro:129;
     Structure:1095; GR:228, 262; ch01:20, 26, 30, 32, 36, 38, 41, 47, 213 and their FULL mirrors.
   - Spekkens 2007 at appendix-c:232 / FULL:6461 and at bibliography:67.
6. **#1188 is respected for `permTheory_not_control`.**
   - The draft uses that theorem only as stated: every nonempty finite carrier, kernel-only.
   - It does not use the vacuous `readWriteSourced_*` results. Note that Main:590 still cites them, a defect #1188
     already tracks.
   - See N3 for the edge that needs stating.

## Blocking findings

**B1. Lemma M is sound but trivial as stated. Its application to the candidate list is unsupported, and for ACC its
cited witnesses fail the candidate.** Lines 154-176, 185, 187, 219, 288-289.

- **(a) The lemma is a counterexample statement.** Its content is: if some core-realizer `T₀` satisfies `C` and lacks
  control, then `OICore ∧ C` does not imply control. The containment in `diagTheory` or `permTheory` is one way to show
  that `T₀` lacks control. The heading "U/E dichotomy" (and "class U/E", line 167) promises more than the proof gives.
- **(b) The candidates are never stated as predicates on `T`.** §3.1 (lines 170-176) classifies only two theories: the
  core's own words, and FIX via AP1 Lemma 2. Yet line 289 lists FIX, ACC-R1–R3, FIN, RET-w, RET-s, DIST and CERT as
  covered. None of them is stated as a predicate on `FiniteOperationalTheory (Fin 2)`, and several cannot be:
  - FIX, R1 and RET-s concern `(S, φ)`. The draft itself says `T` has no `φ` (F4, line 92).
  - CERT constrains the notion of operational equivalence, not `T`.
  - FIN-for-records is unsatisfiable by every `FiniteOperationalTheory`, because the structure forces ancillas of every
    size and products of outcome labels (F4). Lemma M then has no `T₀` at all.
- **(c) The kernel witnesses fail ACC.** `diagTheory` makes every diagonal-preserving CP instrument available
  (DiagonalTheory.lean:246-248). `permTheory_relabel` (SubstratumInterfaceAudit.lean:730-736) makes *every* core
  permutation available in `permTheory (Fin 2)`, including `g_hb`. Both witnesses therefore let the observer read `h` in
  zero dynamical steps, which is exactly what an operational ACC-R2 forbids.
  - So the ACC-row cell at line 187 ("NI (Lemma M: the core's own classical theory satisfies them)") has no exhibited
    witness.
  - "The core's own classical theory" (lines 173, 187, 219, 288) is not a defined object in the kernel or in the draft.
- **(d) The "NI (Lemma M)" cells in the V, I column (lines 185, 187, 189) are mis-cited, and may be wrong in the
  framework's favour.**
  - Lemma M speaks only of control and QM, not of V or I.
  - `CompositeOperationalValidity` (OperationalValidity.lean:88-93) is itself a restriction ("every available family is
    CP and trace-summing"), so it is inherited by every subtheory.
  - `diag_validity` (DiagonalTheory.lean:307) is kernel. So any candidate that confines `T` inside a valid theory
    *implies* V. FIX ⊆ `permTheory` gives FIX ⇒ V, conditional on `permTheory`'s validity, which this review did not
    locate as a kernel lemma.
  - The cell should be EI (conditional) or "not assessed", not NI.
- **(e) The overall verdict for ACC is understated.** If ACC-R2 is formalized operationally ("no available operation
  other than the law's step moves `h` into the visible register"), every theory with control violates it, because
  `relabel_available` gives `g_hb`. ACC-R2 then *excludes* control (CX), as FIX does. The "preserve negative results"
  boundary favours recording the stronger negative where it holds.

*Fix.* Restate Lemma M with its real scope, and add the recovery below. Then give each candidate a stated formalization
(or "not expressible in `FiniteOperationalTheory`") and a per-cell witness. Re-mark any cell without one as "not
assessed".

*Recovery sketch (paper level, reviewer's A-layer; unverified).*

- The fields of `FiniteOperationalTheory (Fin 2)` are Horn-type closure rules, plus readout data that
  `readout_is_localLuders` makes identical across all theories. So the pointwise intersection `T₁ ⊓ T₂` of two theories
  is again a theory.
- For any core-realizer `T₁`, set `T₀ := diagTheory ⊓ T₁`. Then `T₀` realizes the core (σ̂ and τ̂ are available in
  both), and `T₀` lacks control (upward closure plus `diag_not_control`).
- Hence: *for every downward-closed predicate `C` (closed under inclusion of `avail`, `availExt` and `prepAvail`) that
  some core-realizer satisfies, `OICore ∧ C` does not imply control or QM.*
- This is the theorem the draft needs. "Restriction-type" should be defined as "downward-closed".

**B2. The §3.3 inheritance rule is misapplied to non-implication and independence results.** Lines 215, 219, 222, 230.

- The rule "a restriction shrinks the class, so every no-go stated for a superclass still applies" is valid for
  universal no-gos of the form ∀T in the class, ¬P. Examples: `permTheory_not_control` and its inheritance by
  subtheories, the Bell ceiling, Main:640, and the M1D/M2D ceilings within their scopes.
- It is not valid for existential results, which survive only if their witness satisfies the candidate:
  - `oi_alone_not_qm` and `oiCore_not_completedOI`. Their witness is `diagTheory`; see B1(c).
  - `finiteOI_not_implies_inert/closure` (OIRealization.lean:360-370) and `oiPlus_independence`
    (CompletedOI.lean:506-513). Their witnesses (`countermodel`, `admissibleTheory`, and the richness/recursion
    witnesses) carry full composite control. Under FIX or FIN, which exclude exact control, they are not "still
    applying"; they are vacuous.
- Line 222 ("all except EMB") is therefore wrong as stated for FIX and FIN.

*Fix.* Split §3.3 into two tables:

- universal no-gos, inherited by restriction;
- existential or independence results, with a "witness satisfies the candidate?" column, entered as yes/no/not
  assessed.

**B3. §5(c) and §4 conflate two different routes.** Lines 143, 188, 254, 297-304.

- ACC-R4 is M2D's **M-INACC**: "an ontic functional that the fixed rule uses, that **no** permitted preparation, read,
  reuse or recombination **can access**" (M2D:114-117).
- The owner's route (c.6723889799) is "**accessible** but uncertifiable functionals … requiring an observer to certify
  an operation is stronger than requiring the observer to experience its measurable consequences". The owner restates
  it in c.6723571280 (Q-C2-2): "Distinguish genuine operational accessibility from an inability to certify it".
- §5(c) defines the open route as "neither accessible nor certifiable (ACC-R4, the owner's 'accessible but
  uncertifiable' route)". That contradicts the source.
- §4 line 254 then rejects "ACC-R4 / accessible-but-uncertifiable" together, so the rejection reads as applying to the
  owner's route. Structurally, the owner's route is CERT's negation (drop spanning certification, keep access), not
  M-INACC.

*Fix.* Separate them:

- ACC-R4 / M-INACC: an inaccessible, dynamically used functional.
- ACC-U: accessible but uncertifiable, the owner's route. Theorem NC's spanning-certification hypothesis is the one it
  targets.

Give each its own derivability row and guard verdict. §5(c) should name ACC-U as the open route the owner flagged.
State whether M-INACC remains a second open route.

**B4. §5(b) and §5(d) argue from *exact* control and over-generalize about restrictions.** Lines 284-309.

- **(a) Exact versus ε.**
  - Lemma M concerns exact `HasCompositeUnitaryControl`. The draft's own FIN row (line 189) already makes FIN, a native
    posit, exclude exact control.
  - The corpus's quantum claims are ε-form: Main:22, Main:566, and Main:582 ("finite-accuracy quantum statistics are
    compatible with one fixed reversible law").
  - So a negative about exact control under restrictions is close to vacuous for the physical question. Lemma M says
    nothing about ε-control or ε-QM.
  - §5(b) must say that its "no" concerns implying exact control or exact QM. It must also say that the ε question is
    answered here only by noting that Main:566/582 is consistent but imports QM; that is the draft's own pressure-test
    4, and it should be stated in §5(b).
- **(b) "Help explain": no versus partly.** §5(b) answers "no", but its own bullet (line 293) says the restrictions
  "contribute the Z/X sequential-measurement and eraser structure at stabilizer scope". That is a contribution to
  explaining a fragment of quantum behaviour. Under the owner's significance ladder (c.6723571280), the accurate answer
  is: "partly: conditionally on supplied posits, a noncontextual, classically reproducible fragment. No quantum-selecting
  property (control, ℂ, coherence, contextuality, Born exponent) within the searched scope." The answer should also be
  stated as the result of a finite search over ten candidates (witness principle), as line 286 begins to do.
- **(c) The (d) assumption-watch is too strong in three places.**
  - "Faithful OI principles are restrictions" (line 306) is false as stated. Axioms 1-2 and C1, C3 and C4 are
    existence principles. The draft says so itself at lines 115-118: "every positive (existence) part … is kept". The
    accurate statement is that the faithful OI content *missing from `OICore`* is restrictive.
  - "A restriction … cannot supply a floor" holds for restrictions *alone* (B1's recovery). It does not hold jointly: a
    downward-closed `R` can cut away the control-lacking models of an existence principle `E` with `E ⇏ control`, so
    that `E ∧ R ⇒ control`. Restrictions can therefore be active ingredients of a route.
  - OI does state existence content at the level of the law. A realization's `(φ, μ_H)` is free data (Main:60), and
    every finite stochastic law has a reversible realization (Main:22). An existence route need not be a principle
    "about the observer's operations". The watch should name that alternative, even though the draft judges Main:582
    imported.

*Fix.* Restate (d) along these lines: *Within `FiniteOperationalTheory`, no downward-closed predicate satisfied by a
core-realizer forces exact control. A route to exact control needs at least one existence-type premise, possibly
jointly with restrictions. Exact control is in any case excluded by FIN, so the operative target is ε-control, for
which this audit has no theorem.*

**B5. F3 misreads the core's designed C1 mechanism as a defect.** It also presents as QM-specific an access that the
classical witnesses share. Lines 68-82, 107, 278.

- **(a) One-step access through σ̂ is C1.** In the core, σ is the passive step, i.e. the law, with `σ(v,h,b) = (h,v,b)`
  (IndependenceCensus.lean:99-100). Its docstring says: "C1 … is literal: `v_{t+1} = h_t`, so the hidden bit drives the
  visible future". Main:74 defines C1 as hidden degrees of freedom affecting the visible evolution "at some accessible
  step".
  - F3(a)'s "read, apply σ̂, read" is therefore information reaching V *through φ*. That is ACC-R2 satisfied, not
    weakened.
  - "'Hidden' means not readable at the present step" is OI's own meaning of the hidden sector (Lemma 2: the complement
    of V), not a finding against the core.
- **(b) Zero-step access is not a QM feature.** The genuine point is access in zero law steps through a non-law
  operation (`g_hb`). That access is not specific to QM or to control: `permTheory_relabel` makes `g_hb` available in
  the classical `permTheory (Fin 2)`, and `diagTheory` contains it too.
- Line 79 ("exact … QM … gives the observer one-step access to exactly the bit the core designates hidden") and line
  278 ("readable in one step by every theory realizing it") present C1 as evidence of missing constraints.
- In P6 (line 107), "R2 W1 (present step only)" has the same mislabel.

*Fix.* Recast F3 as follows. The core's process satisfies R2. As a constraint on `T`, R2 is absent: any theory, the
classical witnesses included, may make available non-law operations such as `g_hb` that read `h` with no law step.
With external records (F4), R3 also fails for `T`. Correct §5(a) line 278 to match. F2 and §1.2's verdict do not depend
on F3 and survive.

**B6. The off-`main` support must be traced reference by reference and closed before landing (§A.42 item 8).**
Lines 36, 64, 124, 128, 131, 149, 186-192, 211, 253, 326.

- §7 row 1 gives one group classification to four session files. Item 8 requires each reference to be traced to the
  claim it supports.
- Several conclusions rest on off-`main` labels or readings:
  - "C2 outcome 2" sets the status of the encoded-carrier CX cells (lines 186, 224).
  - "C1, MQ-29" supports "imported, not explanatory" (line 211). Main:582 alone supports this, so the label can be
    dropped.
  - "C2 §15; auditor reading" supports the FIN all-time T(h) → 1 claim (line 190).
  - "PKG §3.5" and "PKG §6 item 1" are used for RET-s's guard entry (line 253).
  - "C1, MQ-01" supports `finite_horizon_equivalence`'s "Core not used" (line 124). This can be re-checked directly at
    Equivalence.lean:462-468.
- `arp/qc21/REACHABLE.md` sits inside a derivability cell (line 192) while being labelled "not used". Remove it from
  the cell.

*Fix.* Before the record lands, do one of the following for each reference:

- replace it with its on-`main` support (the kernel lemma, or the record and line);
- land the cited EOI material first;
- narrow the claim.

Classify each remaining reference individually. `controls/c1_core_access.py` must land with the record or be dropped.

## Non-blocking findings

- **N1. The `_hoi` item is CONFIRMING, not a new observation.** Lines 128 and 320.
  - The leading underscore is Lean's own "intentionally unused" signal.
  - `oi_compatible_classification`'s docstring (GeneralCarrier.lean:165-167) and GR:228 already say "OI realization is
    not what does the work".
  - The only addition is that the iff variant's binder is decorative. Relabel it CONFIRMING or ELABORATING in the
    §A.31 sense. Keep §6 item 5 as a record-only note.
- **N2. The P1 mirror citation is inaccurate.** Line 102.
  - ch01:22 = FULL:357 states the **thin** first axiom ("there is differentiated content"), not Main:38's perspectival
    "embedded representation occurs".
  - Main:40 says the thin reading needs embeddedness as a separate third axiom. ch01:24 calls the difference
    presentational.
  - Cite ch01:22 for what it says. Record the Main/book difference as a corpus-consistency finding, for a later
    authorized correction, not here.
- **N3. FIX's "native" typing needs to engage the corpus's own counter-readings.** Lines 104, 141.
  - Main:590 and GR:228 treat the phases as "a stated intervention principle rather than a consequence of its finite
    states and bijective dynamics". Main:22 speaks of "setting interventions".
  - The stronger basis for FIX is V ⊊ S together with the single `φ` on `S`: the observer is part of what `φ` moves.
    Main:46 argues time-homogeneity rather than the exclusion of interventions. Mark the observer-interventions clause
    *interp.*
  - The CX at line 185 covers FIX **without** the phase intervention (⊆ `permTheory`). FIX with the phase intervention
    lands in the substratum theory, whose no-control result `substratumGen_not_control` is only for `Fin 2`. State that
    the CX does not extend to that case on general carriers; extending it would broaden the two-state result, which
    #1188 forbids.
- **N4. The layer label on AP1 Lemma 2 is inconsistent.** Lines 175, 185, 231, 290.
  - AP1 is a W record (§0, line 35). "[P, re-derived]" and "[P + K]" should read "[W, re-derived A] + K".
  - The re-derivation (lines 174-176) covers the generators only. It should add that `permClass` is closed under the
    structure's bind, coarse-graining and discard rules, and that fresh-cell preparations are diagonal. This is why the
    generated theory lies inside `permTheory = genTheory permClass`.
- **N5. The ADA typing misuses "imp" for new hypotheses.** Lines 143, 148, 150.
  - c.6723491138's "imported" means imported mathematical or modelling assumptions, to be challenged one by one.
    ACC-R4 is a *proposed extension*; the ledger handles that case under "Native … unless we're explicitly testing an
    extension".
  - Use a separate tag, such as "ext (proposed)". "imp" fits RET-s (an idealization) and CERT (a framework requirement
    imported into Theorem NC).
- **N6. "Adjustable to fit any outcome" is asserted, not shown, for M-INACC.** Line 254.
  - M-INACC carries anti-fitting clauses: the functional must be one "the fixed rule uses", and the reason must be "not
    chosen to reach the quantum target".
  - The defensible verdict is that it is under-specified as a schema, not yet a testable hypothesis, and so fails
    hard-to-vary until it is instantiated. That is what OICORE-F3 proposes.
- **N7. Two small reference errors.**
  - `permTheory_not_phasesAvailable` is at SubstratumInterfaceAudit.lean:670, not "via :708" (line 185).
  - "fails exactly at τ̂" (line 56): the kernel shows a failure at τ̂. It does not show that σ̂ is available in
    `labelTheory`. Write "fails at τ̂".
- **N8. RET-s as "the smallest meaningful strengthening" needs the comparison made explicit.** Lines 253, 259-264.
  - The draft types RET-s as N/imp and as conflicting with P2 and P8 when exact. Its "testable consequences" are
    delegated to the unexecuted M-ARC variants, and its independent motivation is uncited literature.
  - FIX, a native clarification absent from `OICore` (OICORE-F2), is the smallest *faithful* strengthening of the
    formalization.
  - Suggested wording: "FIX is the smallest faithful strengthening, and it is restrictive. RET-s is the smallest crisp
    new hypothesis, with ε-bounded validity. Neither makes OI an active ingredient in a quantum-selecting property on
    present evidence." The draft's last paragraph already says the second half.
- **N9. The guard list is not a preregistration.** Line 235.
  - "Stated before evaluation" cannot be checked inside one document written with the results in hand. Call it the
    control list, or cite where it was fixed earlier.
  - §A.29's guard is written for revisions. Applying it to native clarifications (FIX, ACC, FIN) is a category
    extension and should be flagged. Natives are "preserve unless testing an extension" under the ADA ledger.
- **N10. P4's strong reading over-reaches.** Line 105. "Control (iv) asserts the opposite" conflates the availability
  of every unitary with control of the dynamics or of outcomes; QM with full control still has outcomes the observer
  does not choose. Soften this, and keep the *interp.* mark.
- **N11. "Independently justified" (line 281) is too strong for total finiteness.** Main:62 calls total finiteness "a
  physical posit … empirically motivated". Say "stated in the original texts, not chosen to reach QM".
- **N12. The W definition is too broad.** Line 21 calls every W record "WIP / UNVERIFIED". Only MI-R says so literally.
  AP1, M1D and M2D describe themselves as paper-only research units that adopt nothing. Treating them as unverified is
  conservative and correct under §A.46 item 7, but describe them accurately.

## Point-by-point answers to the review brief

1. **F1:** correct; every conjunct was checked against the definitions. **F2:** correct (ELABORATING).
2. **F2/F3:** the "capability floor" holds. F3 should be recast:
   - one-step access through σ̂ is C1;
   - zero-step access through `g_hb` holds in classical `permTheory` and `diagTheory` as well (B5).
3. **`_hoi`:** both halves verified. It is not new (N1).
4. **Faithfulness table:** the quotes are accurate except the P1 mirror (N2). Interpretation is mostly marked; P3
   needs the mark (N3). The "absent" verdicts are right as constraints on `T`. The P6 R2 class is mislabelled (B5).
5. **Typing:**
   - FIX's typing as native needs engagement with the corpus's own intervention principles (N3).
   - The ACC-R4 ADA tag is wrong (N5).
   - Nothing is promoted to native from a W record.
6. **Lemma M:**
   - The logic is valid but its content is thin.
   - It covers only restrictions satisfied by an exhibited control-lacking core-realizer, and none is exhibited for ACC
     (B1). With the downward-closure recovery it becomes a clean scoped theorem at the paper layer.
   - "No restriction-type candidate can supply control" is overstated until each candidate is formalized.
   - #1188 is respected (N3 gives the edge).
7. **The physical-carrier, encoded-carrier, EMB, RET-s and FIN points:**
   - FIX inside `permTheory`: sound as W plus a re-derivation plus K (N4), without the phase intervention (N3).
   - Encoded ceilings: correctly labelled W and conditional. Their status labels need on-`main` support (B6).
   - EMB ⇒ Cl is kernel, and EMB does not give control (kernel, via `permTheory`). Access gives no selection, but see
     B1(e) for the stronger negative.
   - RET-s versus recurrence: verified at AP1:338-343.
   - FIN and ε: the exact algebra is controlled (RC-1). The CX is A over W, for exact control only, which feeds B4(a).
8. **Guard:**
   - RET-s: see N8.
   - The ACC-R4 rejection is defensible as "under-specified". "Adjustable" is overstated (N6), and the owner's route
     must be separated out (B3).
   - The CTRL rejection is correct: it is not in the original principles, and Main:590 names it as an empirical
     resource.
9. **Central question:**
   - (a) is correct apart from the F3 evidence (B5) and the "independently justified" wording (N11).
   - (b) must be scoped to exact control and QM and to the finite candidate search, and must report the explained
     classical fragment (B4).
   - (c) is correct that no theorem excludes an existence-type route, but it mis-describes the owner's route (B3).
   - (d) is too strong (B4(c)).
10. **Off-`main`:** see B6. The #1169 and #1188 comments are owner records; using c.6723889799 to *define* the route
    makes it support, so it must be quoted accurately (B3). Spekkens is support on `main`. The Hardy-type remark is
    provenance only.
