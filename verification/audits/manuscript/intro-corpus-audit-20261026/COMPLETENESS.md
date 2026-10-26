# Completeness: established results the Introduction omits or understates (audit step 5)

Mapper C. Introduction at `4a260ca9`; corpus at `eae01647`. Machine-readable rows: `completeness.json`. Each row was checked against the source it cites; kernel rows against the `.lean` statement.

The question for each row is the owner's: does the corpus establish, proved or conditionally derived, something on the Introduction's subject that the Introduction omits or states more weakly? A row is not a recommendation to add it: the Introduction limits its scope on purpose, and each row says whether that scope should carry the result.

**Counts.** 26 rows: 4 strengthen, 3 add, 7 cite, 12 leave out. Priority: 2 high, 7 medium, 17 low.

## What the Introduction should change

1. **CMP-01 (high), with CMP-08.** §3.4 gives only the obstruction (no fixed finite carrier reproduces a qubit). Main proves the positive half on paper: for fixed dimension, instrument family, horizon and accuracy, one finite reversible realization reproduces every adaptive protocol within ε, and the realized and quantum operational theories are mutually ε-dense. Main's own summary calls this the maximal equivalence available. The Introduction should state it, with its limit (density, not identity).
2. **CMP-02 (high), with CMP-03.** The Introduction says which of (iii)–(v) a physical substratum supplies is open. For the substratum as stated the kernel settles part of it: the stated finite read-write architecture does not supply (iv), and with an assumed phase intervention one continuous state-mixing operation completes it to exact finite operational QM. What is open is whether a physical substratum supplies that operation. Add also that full control realizes the OI core, so Theorem 4 classifies and does not derive.
3. **CMP-22.** L56 restricts the independent-prior realization to rational laws; Main's response-table extension removes the restriction (confirms B1's I-071).
4. **CMP-05, CMP-07, CMP-09, CMP-12, CMP-14, CMP-23, CMP-25: cite.** One clause each, optional, all sharpening statements the Introduction already makes.
5. **CMP-17, CMP-24: §6.3's open list.** Add the assumed complex matrix kinematics, H-∞, the (Obs, μ) interface and the lattice cut of (C4); reword (C2) necessity as proved under an open hypothesis.

Nothing in the corpus makes the Introduction's central claims too weak to stand: the deliberate limits (no derivation of QM, Born exponent not selected, Λ a proposal, Page curve not established) are all borne out.

## Main's Characterization theorem (Main:516, proof Main:608)

Main's Characterization theorem (Main:516, proof Main:608): for a time-homogeneous process on a finite C_V with |C_V|≥2, on accessible timescales, (ii) accessible non-Markovianity (I(X_<k;X_k+1|X_k)>0 at some accessible k) ⟺ (iii) for some accessible k and every horizon K≥k+1 a realization by a bijection of C_V×C_H with C1, C3 and C4 at k and a fixed hidden prior; and, under (T), (i) a ≤n^3-dimensional unitarily evolving representation (fixed-Ĥ ancilla-marginal form).

- **Proof and status.** Both directions of (ii)⟺(iii) are proved in prose (Main:608) and neither is formalized: (iii)⟹(ii) is the Pinsker readback lemma (Main:167); (ii)⟹(iii) is existence by process dilation (Main:496), whose correlated-prior form is the kernel's `S_imp_D`. Clause (i) is imported from Barandes under (T), which is checked only by probes at (2,2), (2,3), (3,2). The theorem has no ledger or census row (signal S1).
- **Introduction.** It does not name the theorem but carries its proved content at equal or higher rigor: Theorem 1 (kernel) for existence and for the representation, which supersedes (i) in rigor; the Corollary (L82) for the per-witness biconditional; L84 and L86 for the readback bound and C1/C3 following from C4. Omitted: the compressed ≤n³ form of (i) under (T), and the time-homogeneous fixed-Ĥ form.
- **Recommendation.** Leave the name out; optionally one sentence assembling the biconditional, labelled 'proved on paper; not machine-checked' and 'time-homogeneous'. Corpus issues found while checking: CON-17 (no ledger row), CON-18 (Main:72 vs :76), CON-19 (appendix B's proof structure differs from Main's).

## Summary table

| ID | Pri. | Result | Status (weakest link) | Introduction | Recommendation |
|---|---|---|---|---|---|
| CMP-01 | high | ε-realization, gluing and finite-test density (Main §3.4) | proved-paper | weaker (130, 12, 185) | **strengthen** |
| CMP-02 | high | Stated substratum does not supply condition (iv); one control resource completes it (GR §3.3, kernel) | proved-kernel | weaker (120, 12, 173, 183) | **strengthen** |
| CMP-03 | medium | Full reversible control realizes the OI core: Theorem 4 classifies, it does not derive | proved-kernel | absent (120, 172) | **add** |
| CMP-04 | low | OI⁺ and its primitive-source and typed forms | proved-kernel | absent (114, 116) | **leave out** |
| CMP-05 | medium | Coherent-completion classification and orientation no-go | proved-kernel | absent (124, 126, 173) | **cite** |
| CMP-06 | low | Bohr-frequency completeness; two-branch form conditional on H-BG | conditional (on H-BG (open; kernel unsigned premise refuted)) | absent (124) | **leave out** |
| CMP-07 | low | Exact one-time classification of lift freedom (fibre-Gram data) | proved-kernel | weaker (124) | **cite** |
| CMP-08 | medium | Intervention dilation (classical comb) and the horizon obstruction | proved-paper | absent (130, 185) | **add** |
| CMP-09 | low | Bell: cost of measurement dependence; PR-box countercontrol | proved-paper | absent (136) | **cite** |
| CMP-10 | medium | Main's Characterization theorem (Main:516, proof :608) | conditional (on (T) and Barandes [11,12] for clause (i) only; time-homogeneity for the fixed-Ĥ form of (i)) | deferred-to-citation (piecewise) (48, 82, 84, 86) | **leave out** |
| CMP-11 | low | Fixed-Ĥ form; non-unique continuous interpolation | proved-paper | absent (58, 124) | **leave out** |
| CMP-12 | low | Canonical predictive quotient | proved-paper | weaker (185) | **cite** |
| CMP-13 | low | Passive observation in the kernel | proved-kernel | deferred-to-citation (22) | **leave out** |
| CMP-14 | low | Lemma 3 measure selection in the kernel | proved-kernel | deferred-to-citation (38) | **cite** |
| CMP-15 | low | Deep-sector cardinality is gauge | proved-paper | weaker (20) | **leave out** |
| CMP-16 | low | Separability threshold (lattice realization) | proved-kernel | absent (251) | **leave out** |
| CMP-17 | medium | Open obligations missing from §6.3 (kinematics, H-∞, (Obs, μ), lattice C4) | open | absent (114, 183, 185) | **add** |
| CMP-18 | low | SM exact geometry (H-link conditional) | proved-kernel | absent (26) | **leave out** |
| CMP-19 | low | Further black-hole theorems (A.1–A.7, Page-time β-dependence) | proved-paper | absent (162) | **leave out** |
| CMP-20 | low | GR's further Λ claims | conditional (on the coupling step G3; the emergent cone, matter content and spin-2 mode (GR:166)) | absent (142, 148) | **leave out** |
| CMP-21 | low | Genericity of the non-permutation witness | proved-paper | absent (92) | **leave out** |
| CMP-22 | medium | Independent-prior realization for every law, not only rational ones | proved-paper | weaker (56, 60) | **strengthen** |
| CMP-23 | medium | All-time rooted classification: realizable ⟺ periodic (kernel only) | proved-kernel | weaker (68, 185) | **cite** |
| CMP-24 | low | (C2) necessity is proved under the mixing hypothesis | conditional (on hidden-sector conditional-mixing hypothesis (ETH-motivated)) | weaker (185, 86) | **strengthen** |
| CMP-25 | low | BHb C2: permutation entanglement capped by initial basis entropy | proved-paper | absent (162) | **cite** |
| CMP-26 | low | BHa D1/D2 and the linear rank law | proved-paper | weaker (160) | **leave out** |

Introduction line numbers are at `4a260ca9`.

## Rows

### CMP-01 — ε-realization, gluing and finite-test density (Main §3.4)

- **Result.** Finite operational realization and gluing (epsilon-form), uniform continuum realization and finite-test density. For a d-dimensional system, a finite family of finite-Kraus instruments, a horizon K and a grid G, one finite reversible deterministic realization reproduces the outcome-sequence law of every adaptive protocol within K(|O_max|-1)/G in total variation (plus a fixed-point term 12 K^2 C_{d,R} 2^-b), with gluing by restriction, one fixed map per instrument, sequential and product composition, and hidden capacity linear in K up to logarithms; one controlled dynamics serves every protocol. Applied to a delta-net of <=m-outcome instruments, the realized and the quantum operational theories are mutually epsilon-dense at horizon K, so Q_operational^(d,m) lies in the finite-test closure of D_finite^(d,m). Density, not identity: the same machinery realizes non-quantum instrument families. Main's own summary calls this 'the maximal equivalence available to a fixed finite substratum'.
- **Sources.** `papers/Main.md:544@eae01647`; `papers/Main.md:556@eae01647`; `papers/Main.md:560@eae01647`; `papers/Main.md:562@eae01647`; `papers/Main.md:574@eae01647`; `papers/Main.md:576@eae01647`; `papers/Main.md:578@eae01647`; `papers/Main.md:580@eae01647`; `papers/Main.md:22@eae01647`; `book/ch01-observation.md:195@eae01647`
- **Proof location.** Main:558 (construction and bound), Rounding Lemma proof inside Main:556, Main:574 (telescoping lemma), Main:576 and :578 (proofs closed inside the statements); exact probes opglue_probes.py checks 8-16.
- **Status.** proved-paper; layer: paper-derivation + exact probes; kernel: none; ledger: MAIN:T-finite-operational-realization-gluing-form P; MAIN:T-uniform-continuum-realization-mutual-density P; Rounding Lemma, the two corollaries and the density corollary have no ledger row. Hypotheses: finite dimension d; finite instrument family, each instrument finitely many Kraus operators; finite horizon K; fixed accuracy; density at fixed (d, m) only, the union over (d, m) not taken; standard volumetric bound on the instrument net (cited). Weakest link: the instrument-level Rounding Lemma in the fixed-point dyadic model (paper proof, instance-certified); no kernel check of any clause.
- **Introduction.** weaker — `papers/Introduction.md:130@4a260ca9`, `papers/Introduction.md:12@4a260ca9`, `papers/Introduction.md:185@4a260ca9`. §3.4 states only the negative half (no fixed finite carrier reproduces a qubit's full prepare-and-measure theory). The positive half, which Main places in its abstract and its 'Summary (the equivalence at maximum proved strength)', is absent; open problem (3) at L185 names a different question (windows short compared with recurrence).
- **Should the scope carry it?** Yes. It is Main's central operational result on the Introduction's own topic (§3.4 'No fixed finite carrier reproduces a qubit'); without it the Introduction reads the obstruction as the whole story.
- **Recommendation: strengthen.** Add to §3.4 after the obstruction: "Approximately, the converse holds: for fixed dimension, a finite instrument family, a horizon and an accuracy ε, one finite reversible realization reproduces the outcome law of every adaptive protocol to within ε in total variation, and with an ε-net of instruments the realized and the quantum operational theories are mutually ε-dense at that horizon (proved on paper, with exact probes) [Main §3.4, Theorems (finite operational realization and gluing — ε-form) and (uniform continuum realization)]. This is density, not identity: the same construction also realizes non-quantum instrument families."
- **Notes.** Pressure-tested: Main:562 itself limits the result (no uniqueness, non-quantum families realized); the proposed text keeps both limits. Rigor is paper-level only, so the text must not say machine-checked.

### CMP-02 — Stated substratum does not supply condition (iv); one control resource completes it (GR §3.3, kernel)

- **Result.** Substratum-source form and its limits. (a) The stated substratum class — bijective (permutation) operators, with a relative-phase intervention stated as an assumption — is closed under composition, coarse-graining, ancilla blocks, uncoupled spectators, relabelling and the adjoint, and contains the exchanges and the phases. (b) It does not supply continuously tunable state mixing: a theory whose available reversible operations are permutation matrices has no composite unitary control and is not finite operational QM; bijective dynamics with the stated observer access does not source the phases (ones-fixing) and executes no layer flow at intermediate times. (c) Adding continuous off-diagonal controllability to the substratum class gives exactly finite endomorphic operational QM on every nonempty finite carrier (a structurally closed extension is quantum iff it drives the elementary transitions). ROADMAP records the corresponding resources as settled negatively (INDEPENDENT) for the present architecture.
- **Sources.** `papers/GR.md:260@eae01647`; `papers/GR.md:262@eae01647`; `papers/GR.md:264@eae01647`; `papers/GR.md:266@eae01647`; `papers/GR.md:272@eae01647`; `papers/Main.md:568@eae01647`; `book/ch19-open-problems.md:126@eae01647`; `verification/ROADMAP.md:1521@eae01647`; `verification/ROADMAP.md:1531@eae01647`; `lean:OIBridge/StructuralClosure.lean:316:substratumClass_structurallyClosed`; `lean:OIBridge/StructuralClosure.lean:414:substratum_plus_control_qm`; `lean:OIBridge/ReadWriteControl.lean:174:readWriteSourced_not_qm`; `lean:OIBridge/PhaseSource.lean:196:substratumClass_not_onesFixing`; `lean:OIBridge/ExecSource.lean:129:obs_not_layerFlowExecutable`; `lean:OIBridge/DerivedQ3.lean:222:derivedOI_qm_iff_layerFlowExecutable'`; `lean:OIBridge/FrozenSourcing.lean:318:frozen_sourcing_verdict`; `lean:OIBridge/StructuralClosure.lean:383:substratum_residual`; `verification/ROADMAP.md:1529@eae01647`; `verification/ROADMAP.md:1538@eae01647`; `verification/ROADMAP.md:69@eae01647`
- **Proof location.** kernel only (GR §3.3 states and cites; no paper proof); every cited declaration has #print axioms in source, gated by tools/lean_axiom_check.py.
- **Status.** proved-kernel; layer: kernel; kernel: StructuralClosure, ReadWriteControl, PhaseSource, ExecSource, DerivedQ3, LiftSource; ledger: no census statement (prose in GR §3.3); declarations resolve in the census registry. Hypotheses: the substratum's reversible operations are modelled as permutation/monomial operators (definitions ReadWriteSourced, substratumClass) — a modelling identification, not derived; the relative-phase intervention is assumed, not derived; finite, endomorphic carriers (the typed form removes 'endomorphic'); readWriteSourced_not_qm is stated on the qubit carrier Fin 2. Weakest link: the identification of the physical substratum's accessible operations with the stated class; the not-QM direction is close to definitional once that identification is granted.
- **Introduction.** weaker — `papers/Introduction.md:120@4a260ca9`, `papers/Introduction.md:12@4a260ca9`, `papers/Introduction.md:173@4a260ca9`, `papers/Introduction.md:183@4a260ca9`. The Introduction says only that which of (iii)–(v) a physical substratum supplies is open. The corpus settles the question for the substratum as stated: (iv) is not supplied without an added controllability resource, and that one resource plus an assumed phase intervention suffices.
- **Should the scope carry it?** Yes. It is the most specific established statement about the Introduction's central open question (which completion conditions a substratum supplies); omitting it understates what is known and leaves the open question broader than it is.
- **Recommendation: strengthen.** Replace the last sentence of §3.2 (L120) with: "For the substratum as stated — finite bijective dynamics with the observer's read and write access — part of this is settled: its operations satisfy the structural closure rules, but a theory whose reversible operations are permutations has no composite unitary control and is not quantum, so condition (iv) is not supplied; with a relative-phase intervention assumed and one continuously tunable state-mixing operation added, the substratum yields exact finite operational quantum mechanics on every nonempty finite carrier (machine-checked) [GR §3.3]. Whether a physical substratum supplies that operation, or the phases, is open." Make the abstract's and §6.3's open item read "whether a physical substratum supplies continuous state-mixing control and the phases". Add substratumClass_structurallyClosed, readWriteSourced_not_qm, substratum_plus_control_qm to Appendix A.
- **Notes.** Pressure-tested against the Lean: readWriteSourced_not_qm assumes every available composite conjugation is a permutation matrix; frozen_sourcing_verdict is stated for permTheory (Fin 2) (no phases, no dense unitary control); both are only as physical as that modelling premise, which the proposed text names ('as stated'). ROADMAP:1529/:1538 record the resource as INDEPENDENT for the present architecture and ROADMAP F2 (:69) keeps the extension open. Confirms mapper B4's item.

### CMP-03 — Full reversible control realizes the OI core: Theorem 4 classifies, it does not derive

- **Result.** The converse containment: every theory with full reversible control realizes the sealed OI core (realizesSealedOICore_of_control), exact finite QM realizes it (qm_implies_oiCore), and the OI-core conjunct of completed OI is redundant once full control holds (completedOI_iff_physical). Hence Theorem 4 classifies completions compatible with embedded observation; it does not derive QM from it.
- **Sources.** `papers/GR.md:228@eae01647`; `papers/GR.md:240@eae01647`; `papers/Main.md:570@eae01647`; `lean:OIBridge/OIRealization.lean:252:realizesSealedOICore_of_control`; `lean:OIBridge/CompletedOI.lean:549:qm_implies_oiCore`
- **Proof location.** kernel only.
- **Status.** proved-kernel; layer: kernel; kernel: OIRealization, CompletedOI; ledger: prose in GR §3.3 and Main §3.4. Hypotheses: the sealed OI core is one specific qubit C1–C4 process with its visible readout (GR:240); finite carriers. Weakest link: none beyond the scope (qubit core).
- **Introduction.** absent — `papers/Introduction.md:120@4a260ca9`, `papers/Introduction.md:172@4a260ca9`. The Introduction gives the half 'OI alone does not imply QM' (oi_alone_not_qm) but not the other half, that QM trivially satisfies the OI core, which is what makes Theorem 4 a classification rather than a derivation.
- **Should the scope carry it?** Yes, as one clause: it fixes how much work the OI hypothesis does inside Theorem 4, a claim about OI's reach.
- **Recommendation: add.** After "So OI alone does not imply quantum mechanics" (L120), add: "Conversely, every theory with full reversible control realizes that observation process (machine-checked), so Theorem 4 classifies the completions compatible with embedded observation and does not derive quantum mechanics from it [GR §3.3]."
- **Notes.** Guards against overclaim as much as underclaim.

### CMP-04 — OI⁺ and its primitive-source and typed forms

- **Result.** OI⁺ and its refinements: conditions (iii)–(v) restated as observational independence, reversible richness and observer recursion, OI⁺ ⟺ exact finite endomorphic operational QM on every nonempty finite carrier, each added principle independent of the OI core and the other two; primitive-source form (implementation locality, phase-free richness, embedded observation); typed form removing 'endomorphic'.
- **Sources.** `papers/GR.md:230@eae01647`; `papers/GR.md:240@eae01647`; `papers/GR.md:246@eae01647`; `papers/GR.md:276@eae01647`; `papers/Main.md:564@eae01647`; `papers/Main.md:568@eae01647`; `lean:OIBridge/CarrierGeneralOIPlus.lean:213:carrier_general_oiPlus`; `lean:OIBridge/CarrierGeneralOIPlus.lean:230:oiPlus_independence`; `lean:OIBridge/TypedCompletion.lean:850:typed_determined_iff`
- **Proof location.** kernel only.
- **Status.** proved-kernel; layer: kernel; kernel: CarrierGeneralOIPlus, MinimalRepertoire, PositivePackage, TypedCompletion; ledger: prose. Hypotheses: finite carriers; added principles are hypotheses, not consequences of OI (GR:242). Weakest link: none (scope only).
- **Introduction.** absent — `papers/Introduction.md:114@4a260ca9`, `papers/Introduction.md:116@4a260ca9`. Theorem 4 is given in its five-condition form only.
- **Should the scope carry it?** Optional. It is a re-expression of Theorem 4, not a stronger result about OI; including it risks being read as a derivation.
- **Recommendation: leave out.**
- **Notes.** If the owner wants it, one clause in §3.2: "(iii)–(v) can be restated as observational independence, reversible richness and observer recursion, each independent of the OI core [GR §3.3]".

### CMP-05 — Coherent-completion classification and orientation no-go

- **Result.** Coherent-completion classification and the orientation no-go. Existence can fail: an explicit finite carrier admits no visible-local CPTP coherent lift. Where completions exist, two that carry identical complete operational data are related by a unitary or by one global transpose (antiunitary) map; transposition preserves all operational data, so no selector depending only on that data fixes the orientation.
- **Sources.** `papers/GR.md:194@eae01647`; `papers/GR.md:198@eae01647`; `papers/GR.md:204@eae01647`; `papers/GR.md:208@eae01647`; `papers/GR.md:214@eae01647`; `lean:OIBridge/JordanClassification.lean:1109:sameData_unitary_or_transpose`; `lean:OIBridge/OrientationSelection.lean:139:operational_orientation_noGo`; `lean:OIBridge/TwoByTwoNoGo.lean:606:twoByTwo_no_local_lift`
- **Proof location.** kernel only (GR:198, GR:204: ledger 'kernel-only').
- **Status.** proved-kernel; layer: kernel; kernel: JordanClassification, OrientationSelection, OrientationClosure, TwoByTwoNoGo; ledger: GR:T-coherent-completion-classification K3; GR:T-operational-orientation-no-go K3. Hypotheses: existence of the completions; Hermitian accessible menus spanning the full matrix algebra with a common unit; separating, cone-generating state families; finite visible dimension. Weakest link: existence: not every carrier admits a coherent completion, and whether the OI substratum does is open (GR:214).
- **Introduction.** absent — `papers/Introduction.md:124@4a260ca9`, `papers/Introduction.md:126@4a260ca9`, `papers/Introduction.md:173@4a260ca9`. §3.3 shows non-selection from visible data; the corpus also shows that complete operational data select the completion up to one antiunitary, and that the visible law is far from complete data.
- **Should the scope carry it?** Yes, as one or two sentences in §3.3: it locates the non-selection precisely (visible data are incomplete; complete data leave only the orientation).
- **Recommendation: cite.** Add to §3.3: "Where coherent completions exist — on some finite carriers none does — two completions with the same complete operational data are related by a unitary or by one global antiunitary, and no selector that reads only those data fixes which (machine-checked) [GR §3.3]; the freedom above arises because the visible law is not complete operational data."
- **Notes.** State the existence caveat with the classification so the result is not read as 'OI determines QM up to orientation'.

### CMP-06 — Bohr-frequency completeness; two-branch form conditional on H-BG

- **Result.** Bohr-frequency completeness: for U(t)=e^{-iHt} with non-degenerate eigenvalues and non-vanishing overlaps, the transition probabilities fix the Bohr-frequency set. Two-branch D-gauge completeness and the phase-locking lemma: the probabilities fix H up to diagonal rephasing, energy shift and H→−H̄, conditional on H-BG; the unsigned kernel premise BGIntegerClassification is false and the sign-aware classification is open.
- **Sources.** `papers/GR.md:172@eae01647`; `papers/GR.md:178@eae01647`; `papers/GR.md:182@eae01647`; `papers/Main.md:224@eae01647`; `book/appendix-b-derivations.md:434@eae01647`; `lean:OIBridge/BohrFrequency.lean:291:bohr_frequency_completeness`
- **Proof location.** GR:174 (paper proof) and kernel for Bohr-frequency completeness; GR:180 conditional proof for the two-branch form.
- **Status.** conditional (on H-BG (open; kernel unsigned premise refuted)); layer: kernel (Bohr frequencies) / paper (two-branch, conditional); kernel: BohrFrequency (K3); twoBranch_of_BGClassification rests on a refuted premise (K1); ledger: GR:T-bohr-frequency-completeness K3; GR:T-d-gauge-completeness-two-branch K1. Hypotheses: trivial ancilla (strict T=|U|^2); continuous-time data; non-degenerate spectrum and gaps, non-vanishing overlaps; H-BG for the two-branch form. Weakest link: H-BG.
- **Introduction.** absent — `papers/Introduction.md:124@4a260ca9`. §3.3 treats dilated lifts at discrete times; the trivial-ancilla continuous-time case, where the data fix more, is not mentioned.
- **Should the scope carry it?** Optional. The Introduction works with discrete-time fixed-basis laws; the result needs continuous-time data and a trivial ancilla, and its strong half rests on an open hypothesis.
- **Recommendation: leave out.**
- **Notes.** If cited, cite only the kernel-proved frequency statement and give H-BG as open; never cite the two-branch form as established.

### CMP-07 — Exact one-time classification of lift freedom (fibre-Gram data)

- **Result.** Exact one-time classification of lift freedom: two lifts are related by the two-sided uniform invisible action iff their fibre-Gram data agree modulo anchored phases; the visible law is exactly the diagonal of those data, every PSD rank-bounded identity-summing family with that diagonal is realized, and the off-diagonal residue is neither empty nor inert (lifts in different classes can differ in relating evolution). Across time, both the trajectory and the threading questions are open.
- **Sources.** `papers/Main.md:624@eae01647`; `book/ch01-observation.md:185@eae01647`; `verification/ROADMAP.md:63@eae01647`; `lean:OIBridge/TwoSidedGauge.lean:115:fibreGram_apply`
- **Proof location.** Main:624 states the result without proof or kernel identifier; ROADMAP P0 (acts 12–13) records SH1 'both directions at kernel level' and TG2; the TwoSidedGauge module exists, but its declarations are not cited by any manuscript.
- **Status.** proved-kernel; layer: kernel (programme record); kernel: TwoSidedGauge (not in the census registry's manuscript citations); ledger: none. Hypotheses: one time slice; the stated uniform two-sided action. Weakest link: manuscript-to-kernel citation missing: Main:624 gives no declaration.
- **Introduction.** weaker — `papers/Introduction.md:124@4a260ca9`. The Introduction says lifts 'can differ by a time-dependent right action'; the corpus classifies the one-time freedom exactly.
- **Should the scope carry it?** Optional; one sentence would sharpen §3.3 without new claims.
- **Recommendation: cite.** Add to §3.3: "At one time the freedom is classified exactly: what the visible law leaves free is the off-diagonal part of the fibre-Gram data modulo phases, and lifts differing there can differ in relating evolution [Main §3.4, Remark (scope: representability, not selection of the relating evolution)]."
- **Notes.** Do not call it machine-checked in the Introduction until Main cites the declarations (census contract, AGENTS §A.35). Act 17's cross-time findings (no coupling between slices from coherence; class-level selection impossibility for four named candidates) are record-only and should stay out.

### CMP-08 — Intervention dilation (classical comb) and the horizon obstruction

- **Result.** Intervention dilation: for any finite action alphabet and horizon, one finite realization with permutation instruments reproduces any action-labelled conditional family (the classical comb), including Leggett–Garg-violating statistics (K=3/2 reproduced exactly). No fixed finite realization carries the whole instrument algebra, and generic action-labelled combs are not hostable on any fixed passive representation as the horizon grows (d ~ (n_V|A|)^{K/4}).
- **Sources.** `papers/Main.md:460@eae01647`; `papers/Main.md:464@eae01647`; `papers/Main.md:466@eae01647`; `papers/Main.md:472@eae01647`; `papers/Main.md:474@eae01647`; `papers/Main.md:536@eae01647`
- **Proof location.** Main:462 (construction), Main:466 and :472 (arguments closed inside the statements); exact probes intervention_probes.py, lg_comb_probes.py, repconsistency_probes.py.
- **Status.** proved-paper; layer: paper-derivation + exact probes; kernel: none; ledger: MAIN:T-intervention-dilation-finite-classical-action P; MAIN:P-no-horizon-independent-intervened-representation P; no-uniform-finite-realization has no ledger row. Hypotheses: finite action alphabet; finite horizon; classical action labels; permutation (invasive) instruments. Weakest link: paper construction (no kernel).
- **Introduction.** absent — `papers/Introduction.md:130@4a260ca9`, `papers/Introduction.md:185@4a260ca9`. Interventions are not discussed; §3.4 covers only prepare-and-measure.
- **Should the scope carry it?** Yes, folded into the CMP-01 sentence: it is the classical rung of the same operational question.
- **Recommendation: add.** Fold into the CMP-01 addition: "... including adaptive interventions; for classical action labels the realization is exact [Main §3.4, Theorem (intervention dilation)], while no fixed representation dimension hosts generic intervention families as the horizon grows."

### CMP-09 — Bell: cost of measurement dependence; PR-box countercontrol

- **Result.** Bell, the other horn and the countercontrol. With setting-dependent ontic ensembles, S_CHSH ≤ min{4, 2+4√(2 ln2 I_ont)}, so the quantum value needs I_ont ≥ 0.0309 bits (a necessary bound, not achievable or tight). Without the spatial and intervention structure, bare finite OI representability realizes PR-box behaviour, so causal locality, not representability, selects.
- **Sources.** `papers/Main.md:356@eae01647`; `papers/Main.md:396@eae01647`; `papers/Main.md:398@eae01647`; `papers/Methodology.md:393@eae01647`
- **Proof location.** Main:396 (data processing + Pinsker + Jensen, in the statement paragraph); PR-box: Main:356 by the response-table construction; check 11 of equivalence_recovery_probes.py.
- **Status.** proved-paper; layer: paper-derivation; kernel: none; ledger: no ledger row. Hypotheses: response-complete ontic variable (Main:398); Z=(A,B) uniform. Weakest link: paper derivation.
- **Introduction.** absent — `papers/Introduction.md:136@4a260ca9`. §3.5 names the dichotomy but not the quantitative cost of the horn not taken, nor the PR-box control.
- **Should the scope carry it?** Optional; one clause in §3.5.
- **Recommendation: cite.** Add to §3.5: "Giving up measurement independence instead costs at least 0.031 bits of setting–microstate mutual information for the quantum CHSH value (a necessary bound) [Main §3.3]; without the spatial structure, the realizations of Theorem 1 also produce PR-box correlations, so locality and not representability is what bounds them."

### CMP-10 — Main's Characterization theorem (Main:516, proof :608)

- **Result.** Main's Characterization theorem (Main:516, proof Main:608): for a time-homogeneous process on a finite C_V with |C_V|≥2, on accessible timescales, (ii) accessible non-Markovianity (I(X_<k;X_k+1|X_k)>0 at some accessible k) ⟺ (iii) for some accessible k and every horizon K≥k+1 a realization by a bijection of C_V×C_H with C1, C3 and C4 at k and a fixed hidden prior; and, under (T), (i) a ≤n^3-dimensional unitarily evolving representation (fixed-Ĥ ancilla-marginal form).
- **Sources.** `papers/Main.md:516@eae01647`; `papers/Main.md:518@eae01647`; `papers/Main.md:520@eae01647`; `papers/Main.md:522@eae01647`; `papers/Main.md:608@eae01647`; `papers/Main.md:610@eae01647`; `papers/Main.md:504@eae01647`; `papers/Main.md:508@eae01647`; `book/appendix-b-derivations.md:454@eae01647`
- **Proof location.** Main:608: (iii)⟹(ii) by the readback lemma (Main:167, Pinsker); (ii)⟹(iii) by finite-horizon process dilation (Main:496, kernel S_imp_D for the correlated-prior form); both 'proved here in prose and neither is formalized'; (i) imported from Barandes [11,12] under (T), (T) checked by tuple_probes.py at (2,2),(2,3),(3,2).
- **Status.** conditional (on (T) and Barandes [11,12] for clause (i) only; time-homogeneity for the fixed-Ĥ form of (i)); layer: paper-derivation ((ii)⟺(iii)); literature + probes ((i)); kernel: the ingredients only: S_imp_D, HiddenMemory; the biconditional itself is not formalized; ledger: no ledger row (signal S1); supporting theorems have rows. Hypotheses: time-homogeneous S; |C_V|≥2; accessible timescales t ≪ t_R; witness-anchored order k; every horizon K≥k+1; fixed hidden prior as realization datum; C2 outside the equivalence. Weakest link: (ii)⟺(iii): paper proof resting on the vanishing criterion for conditional mutual information and the time-t identification (both not formalized); (i): the imported correspondence under (T).
- **Introduction.** deferred-to-citation (piecewise) — `papers/Introduction.md:48@4a260ca9`, `papers/Introduction.md:82@4a260ca9`, `papers/Introduction.md:84@4a260ca9`, `papers/Introduction.md:86@4a260ca9`. The Introduction does not name the theorem, but carries its proved content at equal or higher rigor: (ii)⟹(iii) existence via Theorem 1 (kernel S_imp_D) with C4 = M_t>0 and C1, C3 following (L86); (iii)⟹(ii) via the Pinsker bound (L84); the per-witness biconditional is the Corollary (L82); the fixed-basis representation (Theorem 1, kernel) supersedes (i) in rigor. What is omitted is only (i)'s compressed ≤n^3 form under (T) and the fixed-Ĥ generator form.
- **Should the scope carry it?** Partly. The Introduction's choice of Theorem 1 + Corollary over the Characterization theorem is sound (kernel over prose; Q_fb internal over (i) imported). It need not be named; if named, its status must be stated.
- **Recommendation: leave out.** Optional, one sentence in §2.4 if the owner wants the named result: "Assembled, these give Main's characterization theorem: a time-homogeneous law has accessible memory at some order k exactly when, at every horizon beyond k, it has a finite reversible realization with (C1), (C3) and (C4) at k (proved on paper; not machine-checked) [Main §3.4]."
- **Notes.** Pressure-tested: stating the Characterization theorem as an equivalence would need both directions' status (§A.34): (iii)⟹(ii) Main:167 + Main:608 (paper); (ii)⟹(iii) Main:496 + Main:608 (paper, kernel only for the correlated-prior realization). Related corpus findings: CON-04 (Main:72 vs :76 naming), CON-05 (no ledger row, S1), CON-06 (appendix B restatement).

### CMP-11 — Fixed-Ĥ form; non-unique continuous interpolation

- **Result.** Fixed-Ĥ form for realized processes: Ĥ := i log U_φ reproduces every realized law exactly at integer horizon times (uniform, slice and weighted priors). The continuous-time interpolation is not unique: two Hermitian generators can agree at every integer time and differ at t=1/2 (kernel).
- **Sources.** `papers/Main.md:510@eae01647`; `papers/Main.md:268@eae01647`; `papers/GR.md:292@eae01647`; `lean:OIBridge/RegionLimit.lean:296:continuous_extension_not_unique`
- **Proof location.** Main:512 (paper proof, review4_probes.py); kernel for non-uniqueness.
- **Status.** proved-paper; layer: paper-derivation (fixed-Ĥ); kernel (non-uniqueness); kernel: RegionLimit; ledger: MAIN:L-fixed-hat-h-form-realized P. Hypotheses: integer times; fixed bijection and prior. Weakest link: paper proof.
- **Introduction.** absent — `papers/Introduction.md:58@4a260ca9`, `papers/Introduction.md:124@4a260ca9`
- **Should the scope carry it?** Optional.
- **Recommendation: leave out.**
- **Notes.** If §3.3 is extended, the kernel non-uniqueness of continuous interpolation is a second, independent non-selection result that could be cited in one clause.

### CMP-12 — Canonical predictive quotient

- **Result.** Canonical predictive quotient: the tail object T(P) completes P, admits a reversible ledger extension, and is the terminal predictive quotient of the category of faithful realizations; any two faithful realizations of P share it, while their hidden fibres can differ (completions are not unique up to relabelling).
- **Sources.** `papers/Main.md:600@eae01647`; `papers/Main.md:596@eae01647`
- **Proof location.** Main:600 (inline proof); purification_probes.py exhaustive at (2,2),(2,3),(3,2).
- **Status.** proved-paper; layer: paper-derivation + exhaustive computation; kernel: none; ledger: MAIN:T-canonical-predictive-quotient-purification-ingredient P. Hypotheses: finite horizon; faithful deterministic realizations; morphisms visible-preserving. Weakest link: paper proof.
- **Introduction.** weaker — `papers/Introduction.md:185@4a260ca9`. Open problem (2) speaks of quotienting ledger bits; the corpus has constructed the quotient and leaves only the value question open.
- **Should the scope carry it?** Yes, as a citation in open problem (2).
- **Recommendation: cite.** Open problem (2): "... whether the minimal hidden predictive memory over realizations reduced to the canonical predictive quotient [Main §3.4] equals M_t (the fixed-dimension form is false) ..."

### CMP-13 — Passive observation in the kernel

- **Result.** Passive observation: complete passive observation of a finite-dimensional algebra is possible iff it is commutative; passive incompleteness holds in every finite operational theory on ≥2 states and so does not discriminate the OI core; a passive internal observer can only read an existing record.
- **Sources.** `papers/Main.md:570@eae01647`; `papers/Main.md:572@eae01647`; `lean:OIBridge/CentralObservation.lean:620:complete_passive_iff_commutative`; `lean:OIBridge/PassiveIndependence.lean:269:passive_nondiscriminating`
- **Proof location.** kernel only.
- **Status.** proved-kernel; layer: kernel; kernel: CentralObservation, PassiveObservation, PassiveIndependence, InternalObserver; ledger: prose. Hypotheses: finite dimension; block-diagonal passive instruments. Weakest link: none (scope).
- **Introduction.** deferred-to-citation — `papers/Introduction.md:22@4a260ca9`. L22 states the contrast with uncertainty relations and cites [Main §3.4]; the kernel results behind it are not mentioned.
- **Should the scope carry it?** Optional.
- **Recommendation: leave out.**
- **Notes.** The Introduction's sentence is faithful as written; adding 'machine-checked' would need the declarations in Appendix A.

### CMP-14 — Lemma 3 measure selection in the kernel

- **Result.** Lemma 3 in the kernel: on each accessible orbit the invariant law is unique and uniform; the counting measure is invariant and has maximal entropy among invariant laws; invariance alone does not select a measure.
- **Sources.** `papers/Main.md:56@eae01647`; `papers/Main.md:60@eae01647`; `lean:OIBridge/CanonicalMeasure.lean:276:determinism_reversibility_selected_measure`; `lean:OIBridge/CanonicalMeasure.lean:242:invariance_does_not_select`
- **Proof location.** kernel (ledger MAIN:L-3 K3); Main:62 Remark.
- **Status.** proved-kernel; layer: kernel; kernel: CanonicalMeasure; ledger: MAIN:L-3 K3. Hypotheses: φ a permutation of a finite set (taken as given). Weakest link: none.
- **Introduction.** deferred-to-citation — `papers/Introduction.md:38@4a260ca9`. L38 states 'not selected by invariance' and 'maximal-entropy default' with a Main citation, without marking it machine-checked.
- **Should the scope carry it?** Optional.
- **Recommendation: cite.** L38: append "(machine-checked)" after "maximal-entropy default" and list determinism_reversibility_selected_measure (CanonicalMeasure:276) in Appendix A.
- **Notes.** Low value; only if Appendix A is being revised anyway.

### CMP-15 — Deep-sector cardinality is gauge

- **Result.** Deep-sector cardinality is gauge: within the leading-order accessible-timescale transition law, systems differing only in an uncoupled or slowly coupled deep sector are indistinguishable; total finiteness is scoped as the choice of the minimal finite representative, and accessible-timescale conclusions transfer across the gauge class.
- **Sources.** `papers/GR.md:136@eae01647`; `papers/GR.md:138@eae01647`; `papers/Substratum.md:262@eae01647`; `papers/Main.md:708@eae01647`
- **Proof location.** GR:138 (paper proof); Substratum:262 (argument in the statement).
- **Status.** proved-paper; layer: paper-derivation; kernel: none; ledger: GR:C-deep-sector-cardinality-gauge GAP; SUBSTRATUM:C-effective-finiteness-gauge-class-transfer GAP. Hypotheses: leading order in τ_S/τ_B; accessible timescales; recurrence-scale conclusions excluded. Weakest link: paper argument (ledger GAP).
- **Introduction.** weaker — `papers/Introduction.md:20@4a260ca9`. L20: 'finiteness of all of S is posited'. Faithful to Main:62; the corpus shows the posit is largely a gauge choice for accessible-timescale content.
- **Should the scope carry it?** Optional.
- **Recommendation: leave out.**
- **Notes.** Theorem 3 and §2.5 use recurrence, which needs the finite representative; adding the gauge statement would need that exception stated, so the gain is small.

### CMP-16 — Separability threshold (lattice realization)

- **Result.** Separability threshold: an abelian Weyl twirl is entanglement-breaking iff its order is maximal; for the F_2 lattice update the one-step visible channel is not entanglement-breaking iff w<κ, in particular whenever the region has a non-empty bulk.
- **Sources.** `papers/Main.md:308@eae01647`; `papers/Main.md:312@eae01647`; `papers/Main.md:314@eae01647`; `lean:OIBridge/WeylLift.lean:652:entanglementBreaking_twirl`
- **Proof location.** Main:310 (paper) and kernel.
- **Status.** proved-kernel; layer: kernel + paper; kernel: WeylLift, WeylTwirl, Separability; ledger: MAIN:T-separability-threshold K3; corollaries GAP. Hypotheses: the specific linear F_2 update; one step; uniform hidden state. Weakest link: corollaries GAP; single-step, realization-specific.
- **Introduction.** absent — `papers/Introduction.md:251@4a260ca9`. Appendix B.3 shows the card game's channel is entanglement-breaking; the corpus shows a lattice realization whose channel is not.
- **Should the scope carry it?** No: realization-specific (lattice), one step, and the Introduction avoids the lattice construction.
- **Recommendation: leave out.**

### CMP-17 — Open obligations missing from §6.3 (kinematics, H-∞, (Obs, μ), lattice C4)

- **Result.** Open obligations the Introduction's open list (§6.3) omits: (a) Theorem 4 and its refinements take complex matrix kinematics as given; deriving that kinematics from field-neutral operational premises is open (ROADMAP P1 'K'); (b) all operational-completion results are finite-dimensional; no theorem extends them to infinite-dimensional or field-theoretic systems (H-∞), the quasilocal region completion settling only the algebra, states and discrete dynamics; (c) the stochastic observer interface — which observation map and ensemble (Obs, μ) define the physical law — is unsourced (ROADMAP P1); (d) the physical (C4) discharge is open at the lattice cut as well as the cosmological one (ROADMAP P1). The selection of the relating evolution (P0) and the origin of the Born exponent are stated as open in §3.3 and §3.5 but are not repeated in §6.3.
- **Sources.** `verification/ROADMAP.md:68@eae01647`; `verification/ROADMAP.md:71@eae01647`; `verification/ROADMAP.md:70@eae01647`; `verification/ROADMAP.md:66@eae01647`; `verification/ROADMAP.md:63@eae01647`; `papers/GR.md:276@eae01647`; `papers/GR.md:288@eae01647`; `papers/Main.md:568@eae01647`
- **Proof location.** ROADMAP rows (status OPEN); GR:288 scope sentence.
- **Status.** open; layer: none; kernel: partial results only (K1, K3 conditional; quasilocal completion kernel); ledger: ROADMAP P1 OPEN. Hypotheses: none beyond scope. Weakest link: open.
- **Introduction.** absent — `papers/Introduction.md:114@4a260ca9`, `papers/Introduction.md:183@4a260ca9`, `papers/Introduction.md:185@4a260ca9`. Theorem 4 is stated over 'finite outcome families of linear maps'; the Introduction does not say that the matrix kinematics is assumed or that the results stop at finite dimension.
- **Should the scope carry it?** Yes, one clause: the owner asked for 'what remains open'; (b) also bounds Theorem 4's reach.
- **Recommendation: add.** §6.3: add "(5) the complex matrix kinematics that Theorem 4 assumes, and the extension of the finite operational results to infinite-dimensional systems; (6) which observation map and ensemble define the physical visible law" [GR §3.3; ROADMAP], and widen the (C4) item to "at the cosmological and lattice partitions". Optionally repeat the relating-evolution and Born-exponent items so §6.3 is complete.
- **Notes.** Items (a) and (c) are stated only in ROADMAP, not in any manuscript: see CON-28 (missing assumption in GR §3.3 and Main §3.4). Folds in mapper B4's 'open items §6.3 omits'.

### CMP-18 — SM exact geometry (H-link conditional)

- **Result.** SM exact geometry: the six signed simple-cubic links decompose exactly as 3⊕2⊕1 (kernel theorem_7), with the physical-carrier reading conditional on H-link; tastes 4=1⊕3 (kernel); Yang–Mills coupling dimensionless iff d=3 (kernel).
- **Sources.** `papers/SM.md:372@eae01647`; `papers/SM.md:432@eae01647`; `papers/SM.md:587@eae01647`; `book/ch19-open-problems.md:337@eae01647`
- **Proof location.** SM inline proofs + kernel (ledger K3).
- **Status.** proved-kernel; layer: kernel; kernel: LinkDecomposition, QuarterTurn, TasteBranching, GaugeDimension; ledger: SM:T-7, T-8, T-16 K3. Hypotheses: physical reading needs H-link and H-cust. Weakest link: H-link (physical identification).
- **Introduction.** absent — `papers/Introduction.md:26@4a260ca9`. The Introduction limits itself to foundations, Λ and black holes, and points to [GR] and [Book].
- **Should the scope carry it?** No: outside the deliberate scope; the physical readings are conditional and would need H-link.
- **Recommendation: leave out.**
- **Notes.** If the owner wants OI's reach acknowledged, one pointer sentence citing [SM] with 'conditional on the carrier hypothesis H-link' would suffice.

### CMP-19 — Further black-hole theorems (A.1–A.7, Page-time β-dependence)

- **Result.** Further proved black-hole results: nested-partition consistency (Theorems A.1–A.5), the sector-entropy inequality (Theorem A.6, subadditivity), the effective pure state (A.7), and the Page-time dependence t_P=[1−(β/(1+β))^{3/2}]t_evap on the radiation's entropy ratio β (conditional on A.9).
- **Sources.** `papers/GR.md:729@eae01647`; `papers/GR.md:797@eae01647`; `papers/GR.md:811@eae01647`; `papers/GR.md:857@eae01647`
- **Proof location.** GR App. A inline proofs (ledger GAP; A.3 K2).
- **Status.** proved-paper; layer: paper-derivation; kernel: A.3 only (K2); ledger: GR:T-a.1…T-a.9 GAP. Hypotheses: A.8–A.9: H-scramble, H-decouple, full product space as shell. Weakest link: for the Page-time result: H-scramble and H-decouple.
- **Introduction.** absent — `papers/Introduction.md:162@4a260ca9`. §5 reports A.8–A.9 with their conditions and that the GSL is not derived.
- **Should the scope carry it?** No: none bears on recovery by an observer; adding the Page time would lend a conditional curve more weight than §5 gives it.
- **Recommendation: leave out.**

### CMP-20 — GR's further Λ claims

- **Result.** GR's further CC claims: the 10^122 ratio read as the de Sitter entropy and 'non-adjudicability follows from the equivalence itself' (GR §6.3); four routes (thermodynamic, closure, Lovelock, spin-2) said to converge on Einstein–Hilbert dynamics given the emergent cone, matter content and a spin-2 mode (GR:166).
- **Sources.** `papers/GR.md:364@eae01647`; `papers/GR.md:166@eae01647`
- **Proof location.** argument only; external theorems cited.
- **Status.** conditional (on the coupling step G3; the emergent cone, matter content and spin-2 mode (GR:166)); layer: literature + paper argument; kernel: none; ledger: none. Hypotheses: none beyond scope. Weakest link: G3 open.
- **Introduction.** absent — `papers/Introduction.md:142@4a260ca9`, `papers/Introduction.md:148@4a260ca9`. The Introduction keeps the identity ('a dimensional identity, not an independent prediction') and drops the reading.
- **Should the scope carry it?** No: interpretive and conditional on the open G3 step; including them would overstate (see CON-12).
- **Recommendation: leave out.**

### CMP-21 — Genericity of the non-permutation witness

- **Result.** Genericity of the non-permutation witness: the fraction of bijections with permutation T is n_V!(n_H!)^{n_V}/(n_V n_H)!, decaying like n_V^{-n_V n_H}.
- **Sources.** `papers/Main.md:143@eae01647`
- **Proof location.** Main:143 (counting argument).
- **Status.** proved-paper; layer: exact-algebra; kernel: none; ledger: none. Hypotheses: uniform counting over bijections. Weakest link: none.
- **Introduction.** absent — `papers/Introduction.md:92@4a260ca9`
- **Should the scope carry it?** No: it bears on a measure over bijections, which the Introduction does not use.
- **Recommendation: leave out.**

### CMP-22 — Independent-prior realization for every law, not only rational ones

- **Result.** Independent-prior realization for every finite-horizon law, not only rational ones: the response-table extension replaces the uniform tape by a response coordinate u=(u_c) over the horizon's history contexts with product prior ∏_c kern_c(u_c), independent of the visible initial state, and reproduces the full multi-time law for arbitrary real kernels; 'rationality tracks the prior, not the mechanism'.
- **Sources.** `papers/Main.md:496@eae01647`; `papers/Main.md:498@eae01647`; `papers/Main.md:715@eae01647`
- **Proof location.** Main:498 (construction in the Extension paragraph; review4_probes.py P-G); the correlated-prior realization is kernel (S_imp_D).
- **Status.** proved-paper; layer: paper-derivation + probe; kernel: S_imp_D covers only the correlated-prior form; ledger: MAIN:T-finite-horizon-process-dilation P. Hypotheses: finite visible alphabet; finite horizon; finite hidden set C_V^{contexts} × ledger × clock. Weakest link: paper construction (independence of the prior from x_0 is not formalized).
- **Introduction.** weaker — `papers/Introduction.md:56@4a260ca9`, `papers/Introduction.md:60@4a260ca9`. L56: 'For a law with rational probabilities, a realization whose hidden prior is independent of x_0 also exists'. Main's response-table extension removes the rationality restriction.
- **Should the scope carry it?** Yes; it is a one-word correction to a sentence the Introduction already carries.
- **Recommendation: strengthen.** L56: "For every law, a realization whose hidden prior is independent of x_0 also exists [Main §3.4, Theorem (finite-horizon process dilation) and its response-table extension]; it is proved on paper, with probes."
- **Notes.** Confirms mapper B1's underclaim I-071. The attribution sentence at L60 (EGGH26 Prop. 16, without reversibility) is unaffected. The probe for the arbitrary-prior form (P-G) is not exhaustive exact arithmetic over all laws, so 'exact probes' should not be claimed for it.

### CMP-23 — All-time rooted classification: realizable ⟺ periodic (kernel only)

- **Result.** Exact all-time classification for rooted families (kernel only): a rooted family Γ (Γ_0=I, row-stochastic) is realized at every time by one finite reversible system exactly when it is periodic (finiteRootedRealizable_iff_pper); some family in the fixed-basis quantum class Q* is not finitely rooted-realizable (qStar_not_subset_finiteRootedRealizable).
- **Sources.** `lean:OIBridge/RootedClassificationAllTime.lean:192:finiteRootedRealizable_iff_pper`; `lean:OIBridge/QuantumRepresentationT2.lean:163:qStar_not_subset_finiteRootedRealizable`; `papers/Main.md:618@eae01647`
- **Proof location.** kernel only; no manuscript cites either declaration (grep of papers/ and book/ at eae01647 finds none).
- **Status.** proved-kernel; layer: kernel; kernel: RootedClassification, RootedClassificationAllTime, QuantumRepresentationT2; ledger: none (not in the census registry). Hypotheses: finite visible carrier; rooted families (one-time marginal maps from time 0), not full multi-time laws. Weakest link: scope: rooted families only.
- **Introduction.** weaker — `papers/Introduction.md:68@4a260ca9`, `papers/Introduction.md:185@4a260ca9`. L68 gives the necessity half for multi-time laws (finite order ⇒ periodic); open problem (3) lists 'exact gluing for recurrent target families' as open. At the rooted-family level the kernel settles both directions.
- **Should the scope carry it?** Yes in substance, but the manuscript layer does not carry it: Main:618 still lists recurrent-family gluing as open.
- **Recommendation: cite.** After Main carries it (census contract §A.35), L68: "... and for the rooted maps Γ_t the converse holds: a rooted family is realized at every time by one finite reversible system exactly when it is periodic (machine-checked)"; narrow open problem (3) to multi-time laws.
- **Notes.** Confirms mapper B4's item. Until Main or another manuscript states it, the Introduction would be the only publication-facing site; that is a corpus-propagation decision for the owner. Corpus side: CON-29.

### CMP-24 — (C2) necessity is proved under the mixing hypothesis

- **Result.** (C2) necessity is proved on paper under the conditional-mixing hypothesis: ||T^(k)−T^k|| ≤ (k−1)ε with optimal constant, and the process form I(X_<k;X_k+1|X_k) ≤ 2[ε log(n_V−1)+h(ε)], so observed memory forces ε ≥ ε_min(I*,n_V).
- **Sources.** `papers/Main.md:433@eae01647`; `papers/Main.md:447@eae01647`; `papers/Main.md:720@eae01647`
- **Proof location.** Main:439, Main:451 (paper proofs; c2_mixing_probes.py).
- **Status.** conditional (on hidden-sector conditional-mixing hypothesis (ETH-motivated)); layer: paper-derivation; kernel: none; ledger: MAIN:T-c2-necessity-quantitative-mixing-form P; MAIN:T-physical-memory-c2-process-form P. Hypotheses: mixing hypothesis. Weakest link: the mixing hypothesis.
- **Introduction.** weaker — `papers/Introduction.md:185@4a260ca9`, `papers/Introduction.md:86@4a260ca9`. Open problem (4) lists '(C2) necessity, which is conditional on a hidden-sector mixing hypothesis' among open problems; the theorem is proved, and what is open is the hypothesis.
- **Should the scope carry it?** Yes; wording only.
- **Recommendation: strengthen.** Open problem (4): "whether the hidden-sector mixing hypothesis, under which (C2) necessity is proved [Main §3.4], holds for a physical hidden sector (it is motivated by eigenstate thermalization)".
- **Notes.** Confirms mapper B4's item.

### CMP-25 — BHb C2: permutation entanglement capped by initial basis entropy

- **Result.** BHb C2 (entropy budget): under any permutation the amplitude multiset, the overlap F=|<+^n|ψ>|^2 and the support are conserved, so at every step and aligned bipartition the Schmidt rank is at most |supp ψ0|, S(R) ≤ min(H(p_R),H(p_B)) ≤ H(p0), λ_max(ρ_R) ≥ F and S_2 ≤ −2 ln F; tight (CNOT network). Page-like entanglement therefore requires the initial state to carry it in its basis entropy.
- **Sources.** `verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:15@eae01647`; `verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:30@eae01647`; `verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:40@eae01647`
- **Proof location.** BHb REPORT.md 'Proofs of the exact statements' C2(i)–(iii); exhaustive exact check over S_8 at n=3.
- **Status.** proved-paper; layer: paper-derivation + exhaustive computation; kernel: none; ledger: research record, internally reviewed, not adopted. Hypotheses: permutation unitaries on a configuration-basis Hilbert space; aligned bipartitions. Weakest link: unpublished research record.
- **Introduction.** absent — `papers/Introduction.md:162@4a260ca9`. §5 cites BHb C1 and C6(a)–(b) for the failure of H-scramble on definite configurations; C2 is its quantitative form for every initial state.
- **Should the scope carry it?** Optional, one clause; it sharpens the H-scramble caveat that §5 already carries.
- **Recommendation: cite.** §5, after the H-scramble failure: "more generally, under a permutation the entanglement at an aligned bipartition never exceeds the basis entropy of the initial state [BHb, C2]".
- **Notes.** From mapper B3's list; verified in the record. Relevant also to CON-31 (A.8's own setting).

### CMP-26 — BHa D1/D2 and the linear rank law

- **Result.** BHa D1 and D2: under cumulative records the accessible advantage is nondecreasing (written proof: refinement of the record), while snapshot advantage can decrease (21,632 bijections; swap-in/swap-out 0,1,0). BHa C4 (Lemma L): for linear bijections over GF(2), P_succ = 2^{r_t−k} with max(0,t−(n−k)) ≤ r_t ≤ min(k,t).
- **Sources.** `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:25@eae01647`; `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:26@eae01647`; `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:27@eae01647`; `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:125@eae01647`; `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:134@eae01647`
- **Proof location.** BHa REPORT.md 'Proofs' (C4 Lemma L, D1); exhaustive over GL(4,2) and S_8; independent review confirms D1's proof.
- **Status.** proved-paper; layer: paper-derivation + exhaustive computation; kernel: none; ledger: research record. Hypotheses: finite toy classes; cumulative (not snapshot) records for D1; linear dynamics for C4. Weakest link: unpublished research record.
- **Introduction.** weaker — `papers/Introduction.md:160@4a260ca9`. The Introduction cites the linear case as 'the secret-sharing threshold' (C4 carried); D1/D2 absent.
- **Should the scope carry it?** Optional; D1 is a clean statement about accessible recovery over time, but the Introduction's §5 is already long.
- **Recommendation: leave out.**
- **Notes.** From mapper B3's list; verified. If added: "accessible advantage cannot decrease as records accumulate, though advantage from the current records alone can [BHa, D1–D2]".

## Mapper items folded in

Each was re-verified at the cited source before inclusion. B1: ε-realization (CMP-01), coherent completions and OI⁺ (CMP-05, CMP-04), comb (CMP-08), independent prior (CMP-22, confirms I-071), Characterization theorem optional (CMP-10). B2: negative sourcing (CMP-02), OI⁺ (CMP-04), coherent uniqueness (CMP-05); the general Theorem 3 is already in the Introduction, kernel-only in the corpus (CON-41). B3: BHb C2 (CMP-25), A.6 (CMP-19, leave out), BHa D1 and the linear rank law (CMP-26). B4: negative sourcing (CMP-02, adds `frozen_sourcing_verdict`, `substratum_residual`), all-time rooted classification (CMP-23), (C2) necessity (CMP-24), open items (CMP-17). B5: independent prior (CMP-22).
