# I2 inventory — established theorems and the physical layer (stage 6, Q-EX-FULL, step 1)

Thread I2. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`). Governing text `pt/PROTOCOL-STAGE6.md`.
The inventory records; it does not decide, derive or upgrade. Paths are relative to `pt/base/`.

**Format.** One block per record. `statement [file:line]` carries exact fragments of that line, each between
« and », fragments separated by " … " (omitted text). A fragment never crosses a line of the source file; the
quote check (`checks.py`, check Q) verifies every fragment as a substring of the cited line.

**Status vocabulary.** As the protocol: `proved [K]` (kernel anchor at L, named), `assumed` (hypothesis of a
theorem, never discharged), `conditional-on <item>`, `empirically motivated`, `refuted (by <record>)`,
`open (ROADMAP entry)`. One further value is needed for this scope and is marked so the coordinator can map it:
`proved [M]` — the manuscript states the item as proved (written proof, exact probe where it says so) and no
kernel anchor was located at L. `scope statement` — a corpus sentence that fixes what a result does or does not
deliver; its components carry their own status in the records it names.

**Levels.** H hidden deterministic history / substratum; O single-system operational; P pair cone; M
matrix-level operational theory; G general carrier / typed / quasilocal; X manuscript physical layer.

**Bridge result for this scope (mechanical, `checks.py` check B).** None of the 32 kernel modules of the I2 census
names or imports `CompositeDimension`, `K2Guard`, `KInfFoundations`, `maxCone`, `cnot`, `prodState`, `dualW`,
`NativeGate`, `W 3` or `eball`. No record below has a bridge theorem to the pair cone at L; every `bridge` field is
`none at L`, and where the corpus itself says the transfer is not available the record quotes it (`transfer
denied by the corpus`).

***

## A. Composition, locality, subsystems, operations (depth-first: these bear most directly on the pair cone)

### I2.1 — Coupling-graph causal cone
- kind: theorem · level: H · status: proved [M] (written proof by induction; no kernel anchor located at L) · flag: —
- statement [papers/Main.md:358]: «Write the spatial substratum as $S=\prod_{i\in V}S_i$ and define the coupling graph $G_\varphi$ by one-step dependency» … «Then, by induction, $(\varphi^k(s))_i$ depends only on initial components in the graph ball $B_{G_\varphi}(i,k)$.» … «Thus a setting intervention supported in region $A$ cannot alter a readout in region $B$ before the corresponding causal cones meet.»
- provenance: Main §3.3 (358); restated Main.md:22 (abstract), :752 (conclusion); used by SM.md:226 ("by [Main]'s cone theorem").
- depends_on: site factorization of S; the coupling graph read from φ (the "full spatial OI constitution").
- yields: I2.2, I2.5, I2.7; Main §4.6 proof step (I2.72).
- bridge: none at L. bearing: none at L.

### I2.2 — Dynamical causal separation of visible regions
- kind: manuscript-principle · level: H · status: proved [M] (as I2.1) for the causal-cone part; the further structures named are not established · flag: —
- statement [papers/Main.md:628]: «Spatially separated visible regions $V_A,V_B\subset V$ inherit an exact **dynamical causal separation** from the dependency graph» … «This establishes the causal-cone part of locality without the stronger simple-cubic nearest-neighbor stipulation. It does not alone establish statistical product structure after conditioning, local tomography, or one common tensor-product instrument category.» … «The common local quantum composite/instrument structure is the content of the inert-spectator and iterated-composition conditions of the operational-completion characterization»
- provenance: Main §3.4 Remark (scope of the equivalence) (ii), 628.
- depends_on: I2.1.
- yields: —; the composite structure is referred to I2.29 conditions (iii), (v).
- bridge: none at L — transfer denied by the corpus ("does not alone establish statistical product structure after conditioning, local tomography, or one common tensor-product instrument category").
- bearing: none at L.

### I2.3 — The operational-extension boundary
- kind: manuscript-principle · level: G (operational completion) with H inputs · status: scope statement (components: I2.39 proved [K]; I2.12 proved [M]; I2.17 proved [M] with imported half; I2.29 manuscript statement of an I4 kernel result) · flag: do not assume (it names the five completion conditions (i)–(v))
- statement [papers/Main.md:542]: «At fixed observable horizon, $S\iff D\iff Q_{\mathrm{fb}}$ is exact.» … «What no fixed finite carrier can do is reproduce the entire exact continuum operational theory of even a qubit at all preparations/effects and all precisions, by the classical-dimension obstruction above.» … «Any exact-completion reconstruction beyond a fixed finite carrier must additionally show that its chosen completion retains finite predictive dimension; local tomography/composite completeness and all-level operational purification are sufficient reconstruction routes only after their hypotheses are actually established for that completion.» … «The framework's adopted Bell branch therefore requires ontic parameter dependence while retaining operational no-signaling (§3.3).»
- provenance: Main §3.4 Remark (the operational-extension boundary), 542.
- depends_on: I2.39, I2.12, I2.16, I2.17, I2.29, I2.6.
- yields: —.
- bridge: none at L — transfer denied by the corpus (local tomography / composite completeness usable "only after their hypotheses are actually established for that completion").
- bearing: none at L.

### I2.4 — Composite systems "on a different footing" (scope condition (ii) of the correspondence)
- kind: manuscript-principle · level: H/M · status: scope statement · flag: —
- statement [papers/Main.md:212]: «Composite systems are on a different footing.» … «That kinematic locality does **not**, by itself, prove local tomography or that all visible composites and coherent interventions belong to one common tensor-product quantum instrument category. Those are the narrowly stated operational-lifting conditions of §3.4.» … «Promotion to the full standard operational quantum theory is the coherent-instrument/composite bridge; compatibility of the specific local lattice realization with Bell-required ontic parameter dependence is the independent H-Bell bridge.»
- provenance: Main §3.1, scope of the correspondence, condition (ii).
- depends_on: I2.1. yields: —.
- bridge: none at L — transfer denied by the corpus (quoted). bearing: none at L.

### I2.5 — Bell ceiling for a screened local completion
- kind: theorem · level: H · status: proved [M] (written proof; "Certified in `equivalence_recovery_probes.py` (check 11)"; no kernel anchor: no Lean module mentions CHSH) · flag: —
- statement [papers/Main.md:360]: «**Theorem (Bell ceiling for a screened local completion).** *Let $\Omega$ be a»
- statement [papers/Main.md:371]: «*so the model is Bell-local and $|S_{\rm CHSH}|\le 2$.*»
- statement [papers/Main.md:380]: «completion that keeps the pointwise graph cone and a setting-independent»
- provenance: Main §3.3, 360–377 (hypotheses (i)–(iv) at 362–366); restated Main.md:22, :82, :628, :752; Substratum.md:48, :109.
- depends_on: (i) determinism; (ii) setting operations are interventions supported in the respective regions; (iii) readout before the post-setting cones meet; (iv) one common pre-setting ensemble, p(Ω|a,b)=p(Ω); I2.1.
- yields: I2.6 (forces the choice), I2.7.
- bridge: none at L. bearing: none at L.

### I2.6 — The adopted Bell branch: ontic parameter dependence
- kind: hypothesis (adopted branch) · level: H/X · status: assumed (adopted; its compatibility with the SM/GR representative is open: H-Bell, I2.102) · flag: —
- statement [papers/Main.md:392]: «**(a) Ontic parameter dependence — the option taken.** The Bell-relevant response structure is not finite-range at the separation of the wings: at the microstate level, one wing's response depends on the remote setting. This is not an operational signal, and the no-signaling statement below is untouched.» … «the natural branch-(a) target is therefore **preparation-indexed adjacency**»
- provenance: Main §3.3; restated Main.md:22, :82, :542, :562, :628, :752, :756; Substratum.md:22, :109, :122 (M1-B).
- depends_on: I2.5 (the alternative it rejects); I2.10 (operational no-signaling retained).
- yields: I2.87 (M1-B), I2.102 (H-Bell).
- bridge: none at L. bearing: none at L.

### I2.7 — Bell–lattice obstruction and state-dependent escape
- kind: theorem (corollary) · level: H/X · status: proved [M] (corollary of I2.5); the escape route is open (H-Bell) · flag: —
- statement [papers/Main.md:394]: «Hence the **reference nearest-neighbor graph alone** cannot supply option (a).» … «What remains to be proved is H-Bell: the prepared graph family must preserve operational no-signaling and satisfy a curvature/metric convergence condition strong enough for the Ollivier--Ricci continuum step used by the Einstein reconstruction.» … «so the hop-metric curvature route FAILS for the reference family, before any Bell edge is added»
- provenance: Main §3.3, 394; mirrors ROADMAP.md:956–966, Substratum.md:170, SM.md:14.
- depends_on: I2.5; nearest-neighbor cubic update with maximal speed c (SM).
- yields: I2.102.
- bridge: none at L. bearing: none at L.

### I2.8 — Measurement-dependence bound (recorded, not adopted)
- kind: theorem · level: H · status: proved [M] (data processing + Pinsker + Jensen); branch not adopted · flag: —
- statement [papers/Main.md:399]: «S_{\rm CHSH}\le\min\!\left\{4,\;2+4\sqrt{2\ln 2\,I_{\rm ont}}\right\},»
- statement [papers/Main.md:403]: «This is a **model-independent necessary lower bound from the stated inequality, not an achievable cost and not claimed tight**.»
- provenance: Main §3.3 (396–403), boxed; Main.md:405 (response-completeness requirement); restated Main.md:22, :752.
- depends_on: Z=(A,B) uniform; response-complete ontic variable Ω (Main.md:405).
- yields: —. bridge: none at L. bearing: none at L.

### I2.9 — Unrestricted OI realizes PR-box behaviour (negative control)
- kind: theorem (statement of construction) · level: H · status: proved [M] (by the response-table construction, I2.40) · flag: —
- statement [papers/Main.md:356]: «Bare finite OI representability is too broad to select the quantum Bell set: if the two wings are allowed to share globally coupled setting-dependent hidden dynamics, the same reversible response-table construction that realizes arbitrary finite stochastic laws also realizes PR-box behavior.» … «The selector in a Bell experiment is therefore causal locality, not representability.»
- provenance: Main §3.3, 356; :407 ("the mandatory negative control"); :752.
- depends_on: I2.40. yields: I2.5 context.
- bridge: none at L. bearing: none at L.

### I2.10 — Operational no-signaling (scope of the no-signaling claim)
- kind: manuscript-principle · level: H/O · status: assumed for the adopted branch; its preservation by the prepared graph family is open (H-Bell, I2.102) · flag: —
- statement [papers/Main.md:407]: «Outcome correlations are nonfactorizable operationally through the shared preparation and the indivisible joint process, and under (a) at the ontic level as well; but a later local setting cannot produce an operational signal at the remote wing.» … «Dropping that spatial/intervention structure returns the unrestricted OI behavior class, including PR, which is the mandatory negative control.»
- provenance: Main §3.3, 407; ROADMAP.md:957.
- depends_on: I2.1, I2.6. yields: I2.102.
- bridge: none at L. bearing: none at L.

### I2.11 — Observer covariance and the joint description of two disjoint observers
- kind: manuscript-principle (with a classical existence statement) · level: H · status: proved [M] for the joint marginal (definition by counting); the covariance reading is interpretive · flag: —
- statement [papers/Main.md:672]: «**Joint description.** The marginal transition matrix $T_{WF}(\alpha, \beta \to \alpha', \beta') = |\{h \in H : \pi_{V_W \cup V_F}(\varphi(\alpha, \beta, h)) = (\alpha', \beta')\}|/|H|$ exists and is unique given $\varphi$. Its marginals reproduce Wigner's $T_W$ and Friend's $T_F$ respectively.»
- statement [papers/Main.md:666]: «it is a covariance property of the framework under observer-partition choice, which resolves the standard nested-observer paradoxes.»
- provenance: Main §4.1, 666–674.
- depends_on: Lemma 3 counting measure (I1). yields: —.
- bridge: none at L (a classical joint stochastic law of two visible partitions; no statement about a composite state cone). bearing: none at L.

### I2.12 — Finite operational realization and gluing (ε-form)
- kind: theorem · level: H realization of an M-level experiment · status: proved [M] ("both regimes are unconditional, the exact-ring one additionally probe-certified end-to-end"; `opglue_probes.py`; no kernel anchor located) · flag: —
- statement [papers/Main.md:544]: «There is a finite reversible deterministic embedded realization» … «one FIXED injective step map $\varphi_a$ per instrument, extended to a bijection by finite padding — with:*»
- statement [papers/Main.md:548]: «*(2) **Gluing by restriction.** For every $\mathcal{F}' \subseteq \mathcal{F}$ and $K' \leq K$, the same realization with the agent confined to $\mathcal{F}'$ and stopped at $K'$ realizes the subexperiment»
- statement [papers/Main.md:552]: «*(4) **Composition.** Sequential composition by construction; for spatially separated experiments the product construction implements the joint family by applying the local instruments' CP maps as $\mathcal{I}_a \otimes \mathcal{I}_b$ on the joint branch register, visible sectors in product — necessarily joint for entangled preparations, in the factorizability-failing, locality-retaining pattern of §3.3.*»
- provenance: Main §3.4, 544–558 (clauses (1) completeness 546, (5) capacity 554, Rounding Lemma 556, proof 558); restated Main.md:22, :542, :754.
- depends_on: a given quantum experiment (dimension d, finite instrument family 𝓕 of CP maps, horizon K, grid G) — the tensor product of clause (4) is part of the input experiment.
- yields: I2.15, I2.16, I2.18; the "operational realization theorem" of I2.18.
- bridge: none at L. The direction is M → H (a given quantum composite is realized), not H → P; the joint map is the input's I_a ⊗ I_b, not derived.
- bearing: none at L.

### I2.13 — Context-independent implementation (clause (3)) and contextual values
- kind: theorem clause · level: H · status: proved [M] (part of I2.12) · flag: —
- statement [papers/Main.md:550]: «Each labelled instrument is one fixed map, applied whenever chosen, in every context; context enters only through the state. The outcome VALUES remain contextual — the only combination Kochen–Specker permits of any account reproducing these statistics. This is implementation-fixedness of labelled instruments, not Spekkens noncontextuality, which concerns operationally equivalent procedures and is not claimed.*»
- provenance: Main §3.4, gluing theorem clause (3).
- depends_on: I2.12. yields: I2.14.
- bridge: none at L. bearing: none at L.

### I2.14 — Kochen–Specker inheritance
- kind: manuscript-principle · level: M/H · status: conditional-on the coherent operational lift reproducing the standard observable algebra (book), stated as conditional in Main · flag: —
- statement [papers/Main.md:562]: «The Kochen–Specker inheritance (§3.2) remains conditional exactly at that operational-algebra layer.*»
- statement [book/The-Incompleteness-of-Observation-FULL.md:1042]: «conditional on the coherent operational lift reproducing the standard observable algebra, it inherits the Kochen–Specker obstruction» … «Contextuality, in the framework, is the partition-dependence of emergent valuation.»
- provenance: Main.md:562; book FULL.md:1040–1042 and mirror `book/ch03-structural-realism.md:168`. Cross-reference defect: Main.md:562 points to "§3.2", and Main §3.2 at L contains no Kochen–Specker statement (Kochen occurs in Main.md only at :550 and :562).
- depends_on: I2.13; the coherent operational lift (open, I2.69 layer 4).
- yields: —. bridge: none at L. bearing: none at L.

### I2.15 — Single controlled dynamics (corollary of the gluing theorem)
- kind: theorem (corollary) · level: H · status: proved [M] (check 13, `opglue_probes.py`) · flag: —
- statement [papers/Main.md:560]: «the policy-controlled step $\Phi(x) = \varphi_{\pi(x_{\mathrm{vis}})}(x)$, the instrument selected by the protocol from the retained record, is a single reversible deterministic map realizing the entire adaptive experiment» … «One dynamics; the program is paid for as an initial condition, not obtained free.*»
- provenance: Main §3.4, 560. depends_on: I2.12. yields: I2.16.
- bridge: none at L. bearing: none at L.

### I2.16 — Uniform continuum realization (mutual ε-density), the telescoping lemma, finite-test density
- kind: theorem (with lemma and corollary) · level: H/M · status: proved [M] (checks 8–9, `opglue_probes.py`) · flag: —
- statement [papers/Main.md:572]: «Then the outcome-sequence laws obey $\mathrm{TV}(P_\pi, P_{\pi'}) \leq \sum_{t \leq K} \max_a \|I_t^a - I_t'^a\|_\diamond$.*»
- statement [papers/Main.md:574]: «The two operational theories are therefore mutually $\varepsilon$-dense at horizon $K$, in the finite-test metric the density Corollary below makes explicit.»
- statement [papers/Main.md:576]: «As classes this is density, not identity: $D_{\mathrm{finite}}$ is strictly larger — the response-table construction realizes arbitrary finite stochastic behavior, quantum or not — so its closure contains non-quantum operational theories too, and the remaining question (route (ii)) is the operational-lifting problem»
- provenance: Main §3.4, 572–576. depends_on: I2.12, I2.15. yields: I2.18.
- bridge: none at L. bearing: none at L.

### I2.17 — Finite-substratum operational obstruction (classical-dimension form) and the SIC remark
- kind: theorem (proposition) · level: H/O · status: proved [M] for the factorization half; the unbounded nonnegative-rank half imported ([55], [L]) · flag: —
- statement [papers/Main.md:538]: «Hence no fixed finite realization is exactly operationally equivalent to even a single qubit's full theory — the elementary factorization half proved here, the unboundedness imported.» … «The obstruction is independent of C1–C4 and of horizon growth.»
- statement [papers/Main.md:540]: «What it cannot carry is the sharp effects»
- provenance: Main §3.4, 538–540 (`nogo_probes.py`); restated Main.md:542, :578.
- depends_on: factorization interface preparation → finite ontic system → measurement; [55] (imported).
- yields: I2.3, I2.18. bridge: none at L. bearing: none at L.

### I2.18 — What the gluing theorem does and does not deliver; the summary at maximum proved strength
- kind: manuscript-principle · level: G/H · status: scope statement (components I2.12, I2.17, I2.26, I2.29) · flag: —
- statement [papers/Main.md:562]: «It is an **operational realization theorem**, not a uniqueness theorem: the same reversible machinery can realize non-quantum finite instrument families, so the theorem by itself does not identify the standard local quantum instrument category as the only coherent completion.» … «exact finite operational quantum mechanics on a carrier and its composites is equivalent to five named conditions, none supplied by bare finite OI»
- statement [papers/Main.md:578]: «Per (3), density is the maximum: the equivalence cannot be strengthened to exact class identity at any fixed carrier, so what remains is precisely selection — route (ii).»
- provenance: Main §3.4, 562, 578.
- depends_on: I2.12, I2.17, I2.26, I2.29. yields: —.
- bridge: none at L — transfer denied by the corpus (the realization theorem "does not identify the standard local quantum instrument category"). bearing: none at L.

### I2.19 — The visible–hidden tensor product (Stinespring route, level one)
- kind: theorem (construction) · level: H → M (V ⊗ H split, not token ⊗ token) · status: proved [M] (Main.md:348 "Level one (generic, proved)"); permutation-unitary lemma anchored `permMatrix_mem_unitaryGroup` [K] EquivalenceChain.lean:178 · flag: —
- statement [papers/Main.md:626]: «The Stinespring route (§3.2) constructs $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$ and derives the CPTP channel $\Phi$ by partial trace. The visible–hidden tensor product is therefore given by the construction, not postulated.»
- statement [papers/Main.md:348]: «*Level one (generic, proved):* the tensor product $\mathcal{H}_V \otimes \mathcal{H}_H$, a unitary representation of the enlarged basis dynamics, and a CPTP reduced channel — the representation of the basis statistics.» … «*Level three (open):* coherent preparation, noncommuting interventions, and the instrument algebra — the operational bridge (§3.2 checklist).»
- provenance: Main §3.4 Remark (scope of the equivalence) (i); §3.2 comparison of routes.
- depends_on: I2.58 (permutation unitarity), I2.59 (channel). yields: I2.21.
- bridge: none at L. The tensor factorization constructed is visible ⊗ hidden of one observer; the corpus places visible-subsystem product structure in I2.2 (not established). bearing: none at L.

### I2.20 — Nested partitions: classical associativity, quantum–classical consistency, Hamiltonian consistency
- kind: theorem (A.1, A.2) and corollary (A.3) · level: H/M · status: proved [M] (Fubini; Tr_B ∘ Tr_D = Tr_BD) · flag: —
- statement [papers/GR.md:725]: «**Theorem A.1.** *The direct and sequential procedures produce the same transition probabilities on $\mathcal{C}_V$.*»
- statement [papers/GR.md:739]: «**Theorem A.2** (Quantum-classical consistency of nested trace-outs). *Let $\Phi_V^{\text{dir}}$ and $\Phi_V^{\text{seq}}$ be the CPTP channels on $\mathcal{H}_V$ produced by the direct and sequential procedures respectively. Then $\Phi_V^{\text{dir}} = \Phi_V^{\text{seq}}$.*»
- statement [papers/GR.md:745]: «**Corollary A.3** (Hamiltonian consistency). *The direct and sequential procedures yield the same emergent dynamics in two regimes.»
- provenance: GR Appendix A.1–A.4 (709–752); Substratum.md:48 (nested local trace-out).
- depends_on: a bijection on C_V × C_B × C_D; I2.27 (two-branch theorem) for A.3. yields: —.
- bridge: none at L. bearing: none at L.

### I2.21 — Separability threshold, boundary bound, channel normal form, Corollaries 1–2
- kind: theorem (with lemmas, corollaries) · level: M (visible channel of one lattice region) · status: proved [K] for the threshold (`entanglementBreaking_twirl` WeylLift.lean:652, `not_entanglementBreaking_twirl` WeylLift.lean:781, `exists_lagrangian_tuple` WeylLift.lean:361, `isotropic_iff_commute` WeylTwirl.lean:263, `separable_imp_ppt` Separability.lean:199); Lemmas 1–2 and the corollaries proved [M] (`coherence_theorem_tests.py`) · flag: —
- statement [papers/Main.md:308]: «*Let $G$ be an abelian subgroup of the Weyl group on $s$ qubits, of order $2^{t}$ modulo phases. Then $\Phi_G = |G|^{-1}\sum_{g \in G} g\,\cdot\,g^{\dagger}$ is entanglement-breaking if and only if $t = s$.*»
- statement [papers/Main.md:314]: «**Corollary 2.** *If $\min(|\partial^{-}R|, |\partial^{+}R|) < |R|$ then $\Phi$ is not entanglement-breaking.*»
- statement [papers/Main.md:320]: «it supplies neither the observable algebra, nor preparations and interventions, nor tensor composition, nor multi-time statistics»
- provenance: Main §3.2, 288–320 (Lemma 1 at 294, Lemma 2 at 300, Corollary 1 at 312).
- depends_on: the q = 2 linear update u'_x = Σ u_z + v_x, v'_x = u_x (Main.md:290); hidden sector uncorrelated and maximally mixed.
- yields: I2.62 (level two of the comparison of routes).
- bridge: none at L — transfer denied by the corpus ("supplies neither the observable algebra, nor preparations and interventions, nor tensor composition"). bearing: none at L.

### I2.22 — (C1) does not suffice: entanglement-breaking is not fixed by single-system inputs
- kind: theorem (remark with exhaustive enumeration) · level: M · status: proved [M] (`papers/oi_lattice_code/coherence/`) · flag: —
- statement [papers/Main.md:286]: «Condition (C1) does not suffice.» … «The obstruction is structural: (C1) constrains the diagonal of $\Phi$, whereas entanglement-breaking is a property of $\mathrm{id} \otimes \Phi$ and is not fixed by the action on single-system inputs.»
- provenance: Main §3.2, 286; Main.md:320 ("the swap example satisfies (C1) while its channel is entanglement-breaking").
- depends_on: I2.59. yields: I2.21 (the replacement condition on the partition).
- bridge: none at L — transfer denied by the corpus (a composite property, id ⊗ Φ, "not fixed by the action on single-system inputs"). bearing: none at L.

### I2.23 — Passive observation, kept apart from the characterization (four statements)
- kind: theorem (four) · level: M · status: proved [K] (`complete_passive_iff_commutative` CentralObservation.lean:620, `central_classification` :433, `no_complete_passive_observation` PassiveObservation.lean:259, `passivelyIncomplete_of_card` PassiveIndependence.lean:80, `oiCore_to_passive_vacuous` :248, `passivelyIncomplete_without_oiCore` :255, `passive_nondiscriminating` :269, `internal_branch_eq_blockPart` InternalObserver.lean:137, `internal_outcome_law` :150, `recordInstr_writes` :272, `recordInstr_not_passive` :290, `no_full_passive_self_record` :92) · flag: —
- statement [papers/Main.md:570]: «Quantum noncommutativity cannot coexist with complete passive observation.» … «Passive incompleteness is therefore not evidence for a hidden ontology» … «All four statements are finite-dimensional, and none bears on the equivalence.»
- provenance: Main §3.4, 570; `qm_implies_oiCore` (CompletedOI, I4) and `realizesSealedOICore_of_control` (OIRealization, I1) cited in the same paragraph are out of scope (I4, I1).
- depends_on: block-diagonal observable algebra; passive instrument (branches fix the block projectors). yields: —.
- bridge: none at L. bearing: none at L.

### I2.24 — Coherent extension is not fixed by the equivalence
- kind: manuscript-principle · level: M · status: proved [M] (existence of one conservative coherent extension, stated) · flag: —
- statement [papers/Main.md:455]: «*Remark (coherent extension).* The equivalence holds between the operational, dilated, and fixed-basis descriptions and is exact at that level; it does not by itself determine a coherent extension of the fixed-basis theory, and at least one conservative coherent extension preserves the fixed-basis theory exactly as a quotient while adding coherent structure not fixed by the equivalence.»
- provenance: Main §3.4, 455. depends_on: I2.39. yields: I2.26 (existence question).
- bridge: none at L. bearing: none at L.

### I2.25 — Representability is not selection of the relating evolution (Track B, manuscript form)
- kind: theorem (kernel-anchored remark) · level: M · status: proved [K] for the fixed-basis image (`bridge_traj` TrackBQfbBridge.lean:276, `rooted_eq_iff_slice_eq` :180, `realData_traj_stochastic` :286, `padData_rooted` OperationalSourcing.lean:476); the cross-time selection question open (ROADMAP P0, I2.90) · flag: —
- statement [papers/Main.md:622]: «One visible family can admit distinct coherent unitary lifts — each reproducing the visible law at every time, each composing exactly across times — whose relating evolutions differ» … «The fixed-basis correspondence therefore acts on the quotient by visible equality, and two lifts of one visible law in different two-sided classes are not separated by it.» … «exact finite operational quantum mechanics is *characterized conditionally*, under the explicit completion principles of [GR §3.3], none of which bare embedded observation supplies; and selection of a unique relating evolution from the coherent lifts of one visible family is *open*.»
- provenance: Main §3.4, 622; kernel scope (TrackBQfbBridge.lean:16–19): "Trivial ancilla; interventions in `permClass`; the relation proved is equality of the visible slice."
- depends_on: I2.39; trivial ancilla; interventions in `permClass`.
- yields: I2.90–I2.101 (ROADMAP P0 and its acts). bridge: none at L. bearing: none at L.

### I2.26 — Coherent-completion classification: existence, classification, orientation
- kind: theorem (three statuses) · level: M · status: classification proved [K] (`sameData_unitary_or_transpose`, JordanClassification.lean — kernel side I4); existence: no visible-local CPTP coherent lift for an explicit carrier proved [K] (`twoByTwo_no_local_lift` TwoByTwoNoGo.lean:606, `twoByTwo_nonCP` :590, `twoByTwo_affine_rigidity` :246; `shell_representation_from_comb` CoherentLift.lean:371, `comb_mixture_of_shell_representation` :392, `uniform_overlap_obstruction` :433); orientation no-go proved [K] (`operational_orientation_noGo` OrientationSelection.lean:139, `transpose_data_eq` :118, `transpose_completion_admissible` :207, `transpose_realizes_second_branch` :228, `transpose_not_inner` :239; `no_universal_oriented_property` OrientationClosure.lean:249) · flag: —
- statement [papers/GR.md:190]: «Visible-local interventions impose further invariants and complete-positivity constraints, and an explicit finite carrier — preparation-feasible, with a globally reachable intervention table — admits no visible-local CPTP coherent lift at all» … «Not every nominal carrier belongs to the coherent-completion class, and every statement below is about the completions that exist.»
- statement [papers/GR.md:196]: «Every two existing OI-compatible coherent completions with identical complete operational data are therefore equivalent either by ordinary unitary gauge or by one global antiunitary orientation reversal.»
- statement [papers/GR.md:204]: «$$\boxed{\;\mathrm{OI} \;+\; \text{OI-compatible coherent-completion conditions} \;\Longrightarrow\; \mathrm{QM}/\mathbb{Z}_2^{\mathrm{anti}}\;}$$»
- statement [papers/GR.md:208]: «$$\boxed{\;\mathrm{OI} \;+\; \text{coherent completion} \;+\; \text{positive thermodynamic orientation} \;\Longrightarrow\; \mathrm{QM}\;}$$»
- provenance: GR §3.3, 188–210 (Theorem coherent-completion classification 194; orientation no-go 200; premises 202); Main.md:562 mirror.
- depends_on: I2.38 (ShellRepresentationConsistency; orientation conditions); "the stated carrier, locality, genericity, and operational-completeness hypotheses" (GR.md:206).
- yields: I2.18. bridge: none at L. bearing: none at L.

### I2.27 — Bohr-frequency completeness, two-branch D-gauge theorem, antiunitary invariance, thermodynamic orientation
- kind: theorem (with corollaries) · level: M · status: proved [K] conditional on the external premise I2.28 (`twoBranch_of_BGClassification` TurnpikeScopeTransfer.lean:826); corollaries proved [K] (`circuit_invariance` AntiunitaryInvariance.lean:71, `string_invariance` :119, `transposeMap_kraus` :97, `kraus_normalization` :107, `unitary_channel_transpose` :143; `transported_gibbs` ThermalOrientation.lean:153, `gibbs_orientation` :104, `passivity_selector_nonuniform` :239, `orientation_excludes_reflection` :179, `gibbs_strictlyPassive` :198, `counting_passive` :256); H-orientation transport open · flag: —
- statement [papers/GR.md:174]: «If $|U'_{ij}(t)|^2 = |U_{ij}(t)|^2$ for all $i, j, t$, then $H' = DHD^\dagger + E_0$ or $H' = -D\bar{H}D^\dagger + E_0$, for a time-independent diagonal unitary $D$ and a real $E_0$.*»
- statement [papers/GR.md:180]: «**Corollary (operational antiunitary invariance).** *Transposing the preparation, every operation, and the effect simultaneously»
- statement [papers/GR.md:186]: «Whether the substratum *derives* such a state is not claimed here; it is the H-orientation transport question»
- provenance: GR §3.3, 168–186 (Bohr-frequency completeness 168; dimensional obstruction 172; kernel remark 178).
- depends_on: non-degenerate gaps, non-vanishing overlaps; I2.28. yields: I2.20 (Corollary A.3), I2.26.
- bridge: none at L. bearing: none at L.

### I2.28 — `BGIntegerClassification` (the Bekir–Golomb premise)
- kind: hypothesis-structure (`def … : Prop`) · level: M (integer rulers) · status: assumed (explicit premise of `twoBranch_of_BGClassification`; ROADMAP P2 "Bekir–Golomb integer classification | Reconstruction | **EXTERNAL**", ROADMAP.md:71) · flag: —
- statement [papers/GR.md:178]: «with a single exception consumed as a cited external theorem: the integer classification of Bekir–Golomb, stated in the kernel as the explicit premise `BGIntegerClassification`»
- provenance: kernel `def BGIntegerClassification` TurnpikeScopeTransfer.lean:542.
- depends_on: —. yields: I2.27.
- bridge: none at L. bearing: none at L.

### I2.29 — The operational-completion characterization (manuscript statement; kernel side I4)
- kind: theorem (manuscript statement of a kernel result) · level: G (every nonempty finite carrier and ancilla levels) · status: proved [K] per the manuscript's kernel citation (`exactAll_iff_physical_general`, `general_characterization`, GeneralCarrier.lean) — kernel side out of scope: I4 · flag: do not assume (conditions (i)–(v))
- statement [papers/GR.md:212]: «(iii) *Inert spectators*: an untouched independent system can be adjoined without changing an intervention. (iv) *Full reversible control*: every finite unitary on every composite is available. (v) *Iterated composition*: a composite may itself serve as the working system of a larger experiment»
- statement [papers/GR.md:214]: «*For every nonempty finite visible system, the available outcome families on the system and on every positive ancilla level are exactly the normalized finite Kraus instruments if and only if conditions (i)–(v) hold.*»
- statement [papers/GR.md:216]: «Each of the five is independent of the other four and of the observation process itself»
- provenance: GR §3.3, 212–224; Main.md:352, :542, :562, :620, :628 (mirrors).
- depends_on: conditions (i) valid probabilities, (ii) trivial-ancilla consistency, (iii) inert spectators, (iv) full reversible control, (v) iterated composition.
- yields: I2.30, I2.31. bridge: none at L (statement at level G; no theorem at L transfers it to `W 3`; out of scope: I4 for the matrix-to-pair bridge census). bearing: none at L.

### I2.30 — Bare finite OI does not imply QM; OI-compatible theory plus (i)–(v) iff finite operational QM
- kind: theorem (boxed, manuscript statement; kernel side I4) · level: G · status: proved [K] per manuscript citation (`main_result`, `oi_compatible_classification`, `oi_alone_not_qm` in GeneralCarrier.lean; `five_way_minimality` in RankGapTheory.lean) — kernel side out of scope: I4 · flag: do not assume ((i)–(v))
- statement [papers/GR.md:218]: «$$\boxed{\;\text{bare finite OI} \;\not\Rightarrow\; \mathrm{QM}\;}$$»
- statement [papers/GR.md:222]: «$$\boxed{\;\text{OI-compatible operational theory} \;+\; \text{(i)–(v)} \;\iff\; \text{finite operational QM}\;}$$»
- statement [papers/GR.md:224]: «The OI clause is not what does the work» … «so the theorem is a classification of the completions compatible with embedded observation, not a derivation of quantum mechanics from it.»
- provenance: GR §3.3, 216–224; Main.md:352 ("Bare finite OI therefore does not select quantum mechanics").
- depends_on: I2.29. yields: —. bridge: none at L. bearing: none at L.

### I2.31 — Quantum-complete OI (OI⁺): observational independence, reversible richness, observer recursion
- kind: definition-as-hypothesis with an equivalence theorem (manuscript statement; kernel side I4) · level: G · status: equivalence proved [K] per manuscript citation (`carrier_general_oiPlus`, `oiPlus_iff_completedOI`, `oiPlus_independence`) — kernel side out of scope: I4; the three principles assumed (not derived from bare OI: "None of observational independence, reversible richness, or observer recursion follows from the OI core") · flag: do not assume (observational independence, reversible richness, observer recursion)
- statement [papers/GR.md:228]: «1. *Observational independence*: an available operation remains the same operation when an untouched system is adjoined. Equivalently, inert spectators do not change the operational possibilities; in particular, independently available operations on disjoint factors can be performed jointly»
- statement [papers/GR.md:236]: «$$\boxed{\;\mathrm{OI}^{+} \;\iff\; \text{exact finite endomorphic operational QM}\;}$$»
- statement [papers/GR.md:240]: «This equivalence is an axiomatic completion theorem, not a derivation of the additional principles from bare OI.» … «None of observational independence, reversible richness, or observer recursion follows from the OI core: each can fail while the core, well-formedness, and the other two remain satisfied»
- provenance: GR §3.3, 226–240; Main.md:564–568 (mirror; box at 566).
- depends_on: OI core (I1), well-formedness (i)–(ii), the three principles. yields: I2.32.
- bridge: none at L. bearing: none at L.

### I2.32 — Primitive-source form: implementation locality, phase-free richness, embedded observation
- kind: theorem (manuscript statement; kernel side I4) with three principles · level: G · status: equivalence proved [K] per manuscript citation (`carrier_general_oiPlusMin`, `oiPlusMin_iff_qm`, `carrier_general_oiPlusPos`) — kernel side out of scope: I4; the principles assumed · flag: do not assume (implementation locality's spectator clause; embedded observation = observer recursion source)
- statement [papers/GR.md:244]: «the branches of an intervention arise together as the outcomes of one protocol, and admissibility is invariant under relabelling and under adjoining an uncoupled spectator.»
- statement [papers/GR.md:248]: «3. *Embedded observation.* One relabelling- and regrouping-invariant family of finite operational theories on all finite carriers has the given theory as its ambient member.»
- statement [papers/GR.md:254]: «It refines the OI⁺ characterization, and it is not a claim that bare observation incompleteness entails these principles»
- provenance: GR §3.3, 242–254 (box 250–252); Main.md:568.
- depends_on: the three principles. yields: I2.33. bridge: none at L. bearing: none at L.

### I2.33 — Substratum-source form
- kind: theorem (manuscript statement; kernel side I4) · level: G/H · status: proved [K] per manuscript citation (`substratum_plus_control_qm`, `substratum_extension_quantum_iff_drives`, `readWriteSourced_not_qm`) — kernel side out of scope: I4; the phase intervention and the controllability resource are assumed ("an empirical extension of the current substratum") · flag: do not assume (structural closure of an extension)
- statement [papers/GR.md:256]: «The phase intervention enters as an assumption on the substratum class, not as a consequence of the finite states with the bijective read-write dynamics» … «and that class, with nothing added, is closed under composition, coarse-graining, and ancilla blocks, stable under an uncoupled spectator, invariant under relabelling, and closed under the adjoint» … «Finite reversible read-write dynamics, even with genuine hidden-memory and readback behavior, does not itself generate quantum state mixing»
- statement [papers/GR.md:260]: «The controllability resource is not entailed by A1–A6; it is an empirical extension of the current substratum, entering as a hypothesis on the extended architecture»
- provenance: GR §3.3, 256–260 (box 258); Main.md:568.
- depends_on: substratum class (monomial operators), phase intervention (assumed), continuous off-diagonal controllability (assumed).
- yields: I2.34, I2.37. bridge: none at L (kernel side I4). bearing: none at L.

### I2.34 — Layer-flow form
- kind: theorem (manuscript statement; kernel side I4) · level: G · status: proved [K] per manuscript citation (`derivedOI_qm_iff_layerFlowExecutable'`, `substratumTheory_not_layerFlowExecutable`, `obs_not_layerFlowExecutable`) — kernel side out of scope: I4; executability assumed, not derived · flag: do not assume (`LayerFlowExecutable`)
- statement [papers/GR.md:262]: «exact finite endomorphic operational quantum mechanics holds exactly when the continuous layer flow of one involution of the configuration space that moves some configuration, the ancilla a spectator, is an available operation at every level and every intermediate time»
- statement [papers/GR.md:266]: «Fractional-time access to one layer flow is therefore an additional physical intervention assumption, as the phase intervention is»
- statement [papers/GR.md:268]: «$$\boxed{\text{stated substratum dynamics with observer access} \;\not\Rightarrow\; \text{one nontrivial layer flow executable}}$$»
- provenance: GR §3.3, 262–270 (box 264); Main.md:568.
- depends_on: I2.33 closure with the phase intervention stated. yields: —. bridge: none at L. bearing: none at L.

### I2.35 — Typed form
- kind: theorem (manuscript statement; kernel side I4) · level: G · status: proved [K] per manuscript citation (`typed_determined_iff`, `typed_determined_of_oiPlusMin`, `typed_interface_not_quantum`) — kernel side out of scope: I4 · flag: do not assume (inherits I2.33's resource)
- statement [papers/GR.md:272]: «The interface itself carries no quantum content: the typed theory whose branches preserve diagonal matrices satisfies every rule and is not quantum mechanics»
- statement [papers/GR.md:276]: «uniform attachment and discard are not derived from the endomorphic formulation» … «The scope of this statement is finite-dimensional.»
- provenance: GR §3.3, 272–276 (box 274); Main.md:568.
- depends_on: I2.33; typed operational interface. yields: I2.36. bridge: none at L. bearing: none at L.

### I2.36 — Level III: the canonical infinite-region (quasilocal) completion, as a manuscript statement
- kind: theorem (boxed isomorphism; manuscript statement) · level: G (quasilocal C*-algebra) · status: proved [K] per manuscript citation (`closure_iUnion_stage`, `quasiState_unique` QuasilocalAlgebra.lean; `canonEquiv`, `canon_unique`, `systemEquiv_dyn` QuasilocalCharacterization.lean — kernel side out of scope: I4; `state_selection_audit` RegionTower.lean:539 and `continuous_extension_not_unique` RegionLimit.lean:296 in I2's census) · flag: —
- statement [papers/GR.md:278]: «Every consistent family of finite-region density matrices extends uniquely to a state of that algebra, and the reversible finite-range substratum update extends uniquely to an isometric $*$-automorphism»
- statement [papers/GR.md:280]: «Any such system is canonically and uniquely $*$-isomorphic to the region completion»
- statement [papers/GR.md:284]: «where $\mathrm{OI}_Q$ denotes the quantum-completed substratum of the statements above — the current OI substratum together with continuous off-diagonal controllability — and not bare observation incompleteness.» … «it is not a characterization of all infinite-dimensional quantum instruments, nor of all locality-preserving quantum dynamics.»
- statement [papers/GR.md:290]: «The uniqueness is among systems built from the substratum's finite-region matrix algebras rather than among all $C^{*}$-algebras, and no Hilbert-space representation and no superselection sector is selected at the level of the laws»
- provenance: GR §3.3, 278–290 (box 282); Main.md:568 mirror; ROADMAP H-∞ (I2.103) and P3 (I2.104). Directionality (§A.34): the box is an isomorphism/uniqueness statement, not an equivalence.
- depends_on: I2.33 (OI_Q = substratum + controllability, assumed); fixed-spacing lattice; disjoint-region commutation.
- yields: I2.103, I2.104. bridge: none at L. bearing: none at L.

### I2.37 — Restriction to the substratum-induced dynamics; continuous time is separate
- kind: theorem (two statements) · level: G · status: proved [K] (`phaseQ_ne_heisQ`, `phase_localityPreserving` QuasilocalCharacterization — I4; `continuous_extension_not_unique` RegionLimit.lean:296; `leap_eq_swap_shear` SecondOrderCircuit.lean:85, `gate_comm` :191, `depth_two_circuit` :313, `leap_leap_symm` :124; `layerQ_add_time` SecondOrderLayer.lean:966; `swapQ_add_time` SwapLayer.lean:494; `driveQ_isContinuousPath`, `driveQ_one_eq_heisQ` SecondOrderDrive — I4); one-parameter-group law and generator open · flag: —
- statement [papers/GR.md:286]: «General locality-preserving automorphisms form a strictly larger class: conjugation by a phase unitary at one site preserves locality and is induced by no reversible finite-range substratum bijection»
- statement [papers/GR.md:288]: «The discrete substratum dynamics does not determine a continuous one-parameter interpolation» … «For the composite path no one-parameter-group law is established and no generator is exhibited»
- statement [papers/Main.md:268]: «A finite permutation does not by itself generate a continuous flow»
- provenance: GR §3.3, 286–288; Main §3.2, 268.
- depends_on: I2.36. yields: —. bridge: none at L. bearing: none at L.

### I2.38 — Existence and orientation premises of the classification (hypothesis-structures)
- kind: hypothesis-structure (`def … : Prop`) · level: M · status: assumed (named premises; `ShellRepresentationConsistency` "is an existence condition"; `OperationalTransitionIdentification` / `OrientedShellRepresentation` orientation alignment, not consequences of transpose-symmetric data) · flag: —
- statement [papers/GR.md:202]: «The two named premises are accordingly not symmetric obligations. `ShellRepresentationConsistency` is an existence condition» … «Orientation requires additional alignment — `OperationalTransitionIdentification`, or an `OrientedShellRepresentation`»
- provenance: kernel `def ShellRepresentationConsistency` ShellAssignment.lean:149; `def OperationalTransitionIdentification` ThermalOrientation.lean:318; `def OrientedShellRepresentation` OrientationClosure.lean:151; `shellRepresentation_transpose_stable` OrientationClosure.lean:109.
- depends_on: —. yields: I2.26. bridge: none at L. bearing: none at L.

***

## B. Equivalence, dilation, hidden memory, recurrence

### I2.39 — Finite-horizon stochastic–reversible–unitary equivalence, S ⟺ D ⟺ Q_fb
- kind: theorem · level: H/M (finite-horizon observable laws of one visible alphabet) · status: proved [K] (`finite_horizon_equivalence` Equivalence.lean:459; `S_imp_D` :419; permutation-unitarity `permMatrix_mem_unitaryGroup` EquivalenceChain.lean:178; diagonal preservation `isDiag_Phi` EquivalenceChain.lean:252) · flag: —
- statement [papers/Main.md:526]: «**Theorem (finite-horizon stochastic–reversible–unitary equivalence).** *Fix a finite visible alphabet and a finite accessible horizon $K$. The following three classes of finite-horizon observable law $P(x_0, \ldots, x_K)$ coincide:*»
- statement [papers/Main.md:534]: «The theorem does not by itself prove that all coherent preparations, noncommuting interventions, and composites are represented simultaneously by one standard local quantum instrument theory.»
- statement [verification/lean-mathlib/OIBridge/Equivalence.lean:459]: «theorem finite_horizon_equivalence {K : ℕ} (P : Traj V K → ℝ) :»
- provenance: Main §3.4, 526–534; kernel classes `def Stochastic` Equivalence.lean:147, `def RevRealizable` :182, `def QfbRealizable` :216, `def RevReal.IsLaw` :168, `def QfbReal.IsLaw` :201. Restated Main.md:16–20, :30, :82, :350, :542, :620, :664, :746–756.
- depends_on: finite visible alphabet; finite horizon K; (D) with an arbitrary initial law (kernel docstring Equivalence.lean:150–155).
- yields: I2.3, I2.24, I2.25, I2.41, I2.43, I2.69. bridge: none at L. bearing: none at L.

### I2.40 — Finite-horizon process dilation (and the response-table extension)
- kind: theorem · level: H · status: proved [M] for the stated form (hidden prior independent of the visible initial state; `process_dilation_probes.py`, `review4_probes.py` P-G); the cited kernel anchor `S_imp_D` (Equivalence.lean:419) proves the weaker class (D) whose initial law need not factor (docstring Equivalence.lean:150–155) · flag: —
- statement [papers/Main.md:496]: «Then there exist a finite $\mathcal{C}_H$, a bijection $\varphi$ on $\mathcal{C}_V \times \mathcal{C}_H$, and an initial hidden prior $\mu_H$ independent of the visible initial state, such that the marginal process of $(\varphi, \mu_H)$ reproduces $\mathcal{S}$'s full multi-time joint law for all $k \leq K$.»
- statement [papers/Main.md:498]: «The characterization below therefore quantifies over general finite-horizon laws.»
- statement [verification/lean-mathlib/OIBridge/Equivalence.lean:154]: «visible prior × hidden prior`. That STRONGER form — a hidden prior independent of the visible»
- provenance: Main §3.4, 496–502 (kernel citation at 500); restated Main.md:20, :30, :82, :754.
- depends_on: rational law (uniform tape) or the response-table product prior (arbitrary kernels).
- yields: I2.9, I2.12 (construction family), I2.41. bridge: none at L. bearing: none at L.

### I2.41 — The characterization theorem: (ii) ⟺ (iii); (i) under (T)
- kind: theorem · level: H · status: (ii) ⟺ (iii) proved [M] ("Both directions of the equivalence are theorems of this paper"); its C2 leg conditional-on the conditional-mixing hypothesis (I1); (i) conditional-on (T) (I2.42) · flag: —
- statement [papers/Main.md:516]: «Then (ii) $\iff$ (iii); and, under (T), (i) holds for $\mathcal{S}$»
- statement [papers/Main.md:522]: «$\mathcal{S}$ arises from marginalizing a deterministic bijection on $\mathcal{C}_V \times \mathcal{C}_H$ — the hidden space may grow with the horizon — with (C1) non-trivial coupling, (C3) sufficient capacity, and (C4) history readback at such a $k$»
- provenance: Main §3.4, 516–522, proof 606; status ledger Main.md:712–720; restated Main.md:678, :688.
- depends_on: I2.40, I2.54 (readback lemma), I2.42; C1–C4 (I1).
- yields: I2.67, I2.69. bridge: none at L. bearing: none at L.

### I2.42 — Definition (unitarily evolving QM), (Q1)/(Q2), and translation hypothesis (T)
- kind: definition-as-hypothesis / hypothesis (T) · level: M · status: (T) assumed (instantiation-checked at (2,2), (2,3), (3,2), `tuple_probes.py`); (Q2) proved [M] in-house (I2.43) · flag: —
- statement [papers/Main.md:508]: «**Translation hypothesis (T) is the claim that this data instantiates the source's tuple, so that its theorem applies.**» … «Condition (i) of the characterization means (Q1); the in-house chain proves (Q2)» … «Additional quantum-mechanical structures — the tensor product decomposition for spatially separated visible-sector subsystems, state update, and the measurement formalism — are addressed in the remarks following the theorem.»
- provenance: Main §3.4, 504–508; Main.md:204, :210, :352.
- depends_on: Barandes correspondence (I2.56). yields: I2.41.
- bridge: none at L. bearing: none at L.

### I2.43 — Fixed-Ĥ form for realized processes
- kind: lemma · level: M · status: proved [M] ("Certified exactly … in `review4_probes.py`, P-F(a)–(c)") · flag: —
- statement [papers/Main.md:510]: «Then the fixed-$\hat{H}$ ancilla-marginal form of (i) holds constructively at every horizon time»
- statement [papers/Main.md:514]: «The chain (ii) $\implies$ (iii) $\implies$ fixed-$\hat{H}$ form is in-house per horizon *in the uncompressed sense*»
- provenance: Main §3.4, 510–514; ledger Main.md:714. depends_on: I2.40, I2.58. yields: I2.41, I2.42.
- bridge: none at L. bearing: none at L.

### I2.44 — Unavoidable hidden predictive memory (universal over faithful realizations)
- kind: theorem · level: H · status: proved [K] (`unavoidable_hidden_predictive_memory` HiddenMemory.lean:185, `distinguishability_floor` :114, `capacity_floor` :170) · flag: —
- statement [papers/Main.md:580]: «Let $\mathcal{S}$ be a visible process and let $\mathcal{R}$ be ANY faithful deterministic realization of it»
- statement [papers/Main.md:590]: «**if the visible process remembers its past, then every deterministic completion reproducing it must carry that memory in the hidden sector, with distinguishability surviving to readback and capacity at least $M_t$.**»
- statement [verification/lean-mathlib/OIBridge/HiddenMemory.lean:185]: «theorem unavoidable_hidden_predictive_memory [Nonempty H] :»
- provenance: Main §3.4, 580–590; restated Main.md:20, :82, :578, :750.
- depends_on: a faithful deterministic realization (bijection with a hidden prior). yields: I2.45, I2.47.
- bridge: none at L. bearing: none at L.

### I2.45 — Canonical predictive quotient (a purification ingredient, substratum form)
- kind: theorem · level: H · status: proved [M] (exhaustive certification `purification_probes.py`, 2,928 instances; `fiber_freedom` is a probe name, no Lean declaration at L) · flag: —
- statement [papers/Main.md:598]: «$T(P)$ is the canonical terminal predictive quotient of the category of faithful realizations» … «full completions are NOT claimed unique up to reversible relabeling, and same-law realizations with non-relabel-equivalent fibers exist»
- statement [papers/Main.md:600]: «The result is an in-house ingredient toward that lift, not yet the all-level operational purification principle itself.»
- provenance: Main §3.4, 598–600. depends_on: I2.44. yields: —.
- bridge: none at L — transfer denied by the corpus (translation "into the operational composite language" open, Main.md:600). bearing: none at L.

### I2.46 — Variational identity (open; naive form false)
- kind: obligation (manuscript-stated open question) · level: H · status: open (manuscript; no ROADMAP row located) — naive fixed-dimension form refuted (by `memory_probes.py`, Main.md:592) · flag: —
- statement [papers/Main.md:592]: «The reading in which the infimum ranges over realizations of FIXED hidden dimension is FALSE» … «leaving open only the variational VALUE question: whether the post-quotient minimum of $I(X_{<t}; H_t \mid X_t)$ attains $M_t$.»
- provenance: Main §3.4, 592. depends_on: I2.44, I2.45. yields: —. bridge: none at L. bearing: none at L.

### I2.47 — The conditions are diagnostics; the bare non-Markovianity–realization form is false
- kind: theorem (remark) · level: H · status: proved [M] (`primitive_probes.py` enumeration; argument from I2.40) · flag: —
- statement [papers/Main.md:595]: «$$\text{accessible non-Markovianity} \iff \text{a per-horizon finite reversible deterministic realization exists}$$»
- statement [papers/Main.md:596]: «is **false**: the process-dilation construction of §3.4 realizes Markov laws as well»
- provenance: Main §3.4, 594–596; conditions C1–C4 themselves out of scope: I1.
- depends_on: I2.40, I2.44. yields: —. bridge: none at L. bearing: none at L.

### I2.48 — P-indivisibility from recurrence (non-permutation T on a finite bijection)
- kind: theorem (minimal model of §2.4 folded as its witness) · level: H · status: proved [M] (written proof; the §2.4 model computes Λ(2,1) with negative entries) · flag: —
- statement [papers/Main.md:119]: «If $T$ is not a permutation matrix, then the process is P-indivisible.*»
- statement [papers/Main.md:123]: «*Step 1 (Recurrence).* $\varphi$ bijective on a finite set $\Rightarrow$ $\exists N: \varphi^N = \text{id}$.»
- statement [papers/Main.md:192]: «Negative entries — no valid stochastic matrix exists. **P-indivisible.** $\square$»
- provenance: Main §2.3, 115–131; §2.4, 178–196 (lemma-folded witness); restated Main.md:415 (non-permutation witness lemma).
- depends_on: finite C_V, C_H (total-finiteness posit, I1); bijection φ; non-permutation T.
- yields: I2.50, I2.60. bridge: none at L. bearing: none at L.

### I2.49 — Stochastic inverse lemma
- kind: lemma · level: H · status: proved [M] · flag: —
- statement [papers/Main.md:133]: «**Lemma (stochastic inverse).** *If a finite square stochastic matrix has a stochastic left or right inverse, then it is a permutation matrix.*»
- provenance: Main §2.3, 133–135. depends_on: —. yields: I2.50. bridge: none at L. bearing: none at L.

### I2.50 — History readback plus finite recurrence implies indivisibility (global recurrence-cycle result)
- kind: theorem · level: H · status: proved [M] · flag: —
- statement [papers/Main.md:137]: «*For a fixed finite reversible OI representative, genuine C4 history readback implies that the rooted visible stochastic process is indivisible somewhere in its full recurrence cycle.*»
- statement [papers/Main.md:141]: «It does **not** say that C4 forces P-indivisibility on every accessible short-time window; the XOR control remains a counterexample to that stronger statement.»
- provenance: Main §2.3, 137–141; restated Main.md:20, :82, :411, :750.
- depends_on: I2.49; finite order of φ; C4 (I1). yields: I2.69. bridge: none at L. bearing: none at L.

### I2.51 — Genericity of the non-permutation precondition
- kind: theorem (counting) · level: H · status: proved [M] · flag: —
- statement [papers/Main.md:143]: «A bijection $\varphi$ on $\mathcal{C}_V \times \mathcal{C}_H$ produces $T$ equal to a permutation matrix if and only if $\varphi$ has the form $\varphi(x_i, h) = (\varphi_V(x_i), \sigma_{x_i}(h))$ — the V-dynamics is independent of $h$.»
- provenance: Main §2.3, 143–147. depends_on: I2.48. yields: —. bridge: none at L. bearing: none at L.

### I2.52 — Continuous-time extension (Poincaré recurrence)
- kind: theorem (sketch) · level: H · status: proved [M] (as stated, by Poincaré recurrence) · flag: —
- statement [papers/Main.md:151]: «For small $\delta$, this gives non-monotonic trace distance, establishing P-indivisibility in continuous time.»
- provenance: Main §2.3, 151. depends_on: I2.48; Liouville measure on compact energy surfaces. yields: —. bridge: none at L. bearing: none at L.

### I2.53 — Fast bath erases readback
- kind: lemma · level: H · status: conditional-on uniform erosion at rate e^{-τ_S/τ_B} (hypothesis of the lemma) · flag: —
- statement [papers/Main.md:161]: «*A fast, uniformly erasing bath therefore drives the readback gap to zero exponentially, and (C4) — which requires a gap at some order in the accessible window — fails.*»
- provenance: Main §2.3, 159–165. depends_on: τ_B ≪ τ_S; uniform erosion. yields: I2.72 (anti-Boltzmann-brain chain).
- bridge: none at L. bearing: none at L.

### I2.54 — Accessible backflow from readback
- kind: lemma · level: H · status: proved [M] (Pinsker; certified `c4_backflow_probes.py`) · flag: —
- statement [papers/Main.md:168]: «$$I(X_{<k};\,X_{k+1} \mid X_k)\ \geq\ \frac{p_0\,\delta^2}{\ln 2}\ >\ 0.$$»
- provenance: Main §2.3, 167–170; ledger Main.md:715. depends_on: a C4 gap at order k (I1). yields: I2.41 ((iii) ⟹ (ii)).
- bridge: none at L. bearing: none at L.

### I2.55 — One-step ancilla dilation
- kind: lemma · level: M · status: proved [M] (certified `tdilate_probes.py`) · flag: —
- statement [papers/Main.md:206]: «**Lemma (one-step ancilla dilation).** *For any stochastic $T$ on $n$ states, the map $W|i\rangle = \sum_j \sqrt{T_{ij}}\,|j\rangle \otimes |i\rangle$ is an isometry $\mathbb{C}^n \to \mathbb{C}^n \otimes \mathbb{C}^n$ whose ancilla-marginal is $T$»
- provenance: Main §3.1, 204–210. depends_on: —. yields: I2.42. bridge: none at L. bearing: none at L.

### I2.56 — The imported stochastic–quantum correspondence and its scope conditions (i)–(iv); the single external dependency (v)
- kind: hypothesis (external import, under (T)) · level: M · status: assumed (published external theorem [11, 12], [L]; load-bearing only for the compressed ≤ n³ form) · flag: —
- statement [papers/Main.md:212]: «we state its scope precisely rather than treat it as a black-box equivalence» … «(ii) *Scaffolding versus full QM.*»
- statement [papers/Main.md:634]: «the import retains the compressed ($\leq n^3$) representation and the interpretive apparatus that travels with it, under (T).»
- provenance: Main §3.1, 204–212; §3.4 Remark (v), 634; Main.md:350.
- depends_on: I2.42 (T). yields: I2.41 (i). bridge: none at L. bearing: none at L.

### I2.57 — Phase-locking (strict and ancilla-marginal forms)
- kind: lemma and theorem · level: M · status: lemma proved [M]; ancilla-marginal theorem proved [M] at seven listed block structures (`phaselock_probes.py`), no uniform-in-(n, m_a) statement · flag: —
- statement [papers/Main.md:224]: «Then $T_{ij}(t) = |\langle i | e^{-iHt} | j \rangle|^2$ for all $i, j, t$ uniquely determines $H$ up to an overall energy shift, basis phase conventions, and the antiunitary conjugation $H \to -H^*$»
- statement [papers/Main.md:246]: «The reconstruction is therefore locally identifiable up to eigenbasis rephasing at those structures.*»
- provenance: Main §3.1, 222–256 (hypotheses G1–G3 at 224; reformulation lemma 242; scope 250–256).
- depends_on: (G1)–(G3) genericity. yields: I2.61. bridge: none at L. bearing: none at L.

### I2.58 — Permutation unitarity and the reverse direction (scoped)
- kind: lemma (two) · level: H/M · status: permutation unitarity proved [K] (`permMatrix_mem_unitaryGroup` EquivalenceChain.lean:178); reverse direction proved [M] (matrix scope, Birkhoff–von Neumann) · flag: —
- statement [papers/Main.md:264]: «**Lemma (permutation unitarity).** *Any bijection $\varphi: \mathcal{C}_V \times \mathcal{C}_H \to \mathcal{C}_V \times \mathcal{C}_H$ defines a unitary $U_\varphi$ on $\mathcal{H} = \mathcal{H}_V \otimes \mathcal{H}_H$.*»
- statement [papers/Main.md:274]: «It is *not* a full CPTP-channel correspondence — channels that create coherences from diagonal inputs have no permutation-unitary realisation with uniform ancilla.»
- provenance: Main §3.2, 262–274. depends_on: —. yields: I2.19, I2.43, I2.59. bridge: none at L. bearing: none at L.

### I2.59 — The visible quantum channel and the Born-form representation theorem
- kind: theorem · level: M · status: proved [M] (CPTP by [16, Theorem 8.1]) · flag: —
- statement [papers/Main.md:278]: «$$\Phi(\rho_V) = \mathrm{Tr}_H\!\left[U_\varphi\,(\rho_V \otimes \rho_H)\,U_\varphi^\dagger\right]$$»
- statement [papers/Main.md:282]: «**Theorem (Born-form representation of the transition probabilities).** *The classical transition probabilities $T_{ij}$ (§1.4) equal the Born-rule probabilities of $\Phi$ — a representation identity: it exhibits the Born form and does not select the quadratic exponent (§3.4).*»
- provenance: Main §3.2, 276–284. depends_on: I2.58; ρ_H = I_m/m. yields: I2.19, I2.21, I2.22, I2.60.
- bridge: none at L. bearing: none at L.

### I2.60 — Diagonal preservation and CP-indivisibility (framework scope); three notions kept apart
- kind: lemma and theorem · level: M · status: proved [M] (`c1_cp_scope_probes.py`); diagonal preservation anchored `isDiag_Phi` [K] EquivalenceChain.lean:252 · flag: —
- statement [papers/Main.md:326]: «*For the permutation-dilation family $\{\Phi_t\}$ above, the P-indivisibility of §2.3 implies CP-indivisibility»
- statement [papers/Main.md:330]: «Stochastic P-indivisibility must therefore not be equated with open-system non-Markovianity outside the diagonal-preserving class»
- provenance: Main §3.2, 322–334; ledger Main.md:716. depends_on: I2.48, I2.59. yields: —. bridge: none at L. bearing: none at L.

### I2.61 — Approximate unitarity (frozen-bath and bath-motion contributions)
- kind: manuscript-principle (estimate) · level: M/X · status: conditional-on the slow-bath and weak-coupling conditions (stated) · flag: —
- statement [papers/Main.md:336]: «Consequently the dynamics is approximately the Schrödinger equation generated by $\hat{H}_{\text{eff}}$ to the extent that *both* the slow-bath condition $\tau_S\ll\tau_B$ *and* a weak-coupling condition»
- provenance: Main §3.2, 336. depends_on: I2.57; C2 (I1). yields: —. bridge: none at L. bearing: none at L.

### I2.62 — Comparison of routes and dependency scope: in-house, imported, additional
- kind: manuscript-principle · level: M/G · status: scope statement (components I2.39, I2.44, I2.56, I2.29) · flag: do not assume (it names the five completion conditions)
- statement [papers/Main.md:350]: «*Additional, with neither route supplying it:* the operational instrument algebra and coherent preparation — supplied exactly by the five operational completion conditions of the characterization in [GR §3.3] (§3.4 Remark), none of which bare finite OI provides»
- provenance: Main §3.2, 338–350. depends_on: I2.19, I2.21, I2.39, I2.56, I2.29. yields: —.
- bridge: none at L — transfer denied by the corpus (quoted). bearing: none at L.

### I2.63 — Operational-reconstruction route: target conditions and the outstanding bridge
- kind: manuscript-principle · level: G/O · status: scope statement · flag: do not assume (five completion conditions)
- statement [papers/Main.md:352]: «The purification, continuous-transitivity, and tomographic-locality axioms of the cited reconstructions are hypotheses of their continuum endpoint, which the classical-dimension obstruction places beyond any fixed finite carrier; they are not what the finite characterization uses.» … «Bare finite OI therefore does not select quantum mechanics; the route classifies the OI-compatible completions by those conditions.» … «The route is therefore a classification conditional on the five completion conditions, not an independent derivation.»
- provenance: Main §3.2, 352. depends_on: I2.17, I2.29, I2.64. yields: —.
- bridge: none at L — transfer denied by the corpus (tomographic locality "not what the finite characterization uses"). bearing: none at L.

### I2.64 — Intervention dilation: the finite classical action-labelled comb; passive scope
- kind: theorem · level: H · status: proved [M] ("Certified exactly … in `intervention_probes.py`"; Leggett–Garg case `lg_comb_probes.py`) · flag: —
- statement [papers/Main.md:460]: «There exist a finite set $S$, a bijection $\varphi$, a fixed prior $\mu_H$, and bijections $\{\mathcal{I}_a\}_{a \in \mathcal{A}}$ on $S$ such that, for every action sequence, alternating $\mathcal{I}_{a_k}$ then $\varphi$ from the initial ensemble reproduces the target conditional law at every step»
- statement [papers/Main.md:464]: «The theorem closes the classical rung of the intervention bridge: classical action labels, permutation instruments, comb statistics of the visible configurations.»
- statement [papers/Main.md:458]: «Conditioning on interventions — $P(X_{k+1} \mid X_{\leq k}, A_{\leq k})$ — requires the instrument-augmented realization $(S, \varphi, \mu_H, \{\mathcal{I}_a\})$»
- provenance: Main §3.4, 458–464; restated Main.md:352, :536, :756. depends_on: I2.40. yields: I2.65, I2.12.
- bridge: none at L. bearing: none at L.

### I2.65 — No uniform finite realization; no horizon-independent intervened representation; the open remainder
- kind: theorem (two propositions) and obligation (three successor problems) · level: H/M · status: propositions proved [M] (`repconsistency_probes.py`); the successor problems (a)–(c) open (manuscript; "none is supplied here") · flag: —
- statement [papers/Main.md:466]: «Hence no fixed finite realization carries the whole instrument algebra»
- statement [papers/Main.md:468]: «What stays open on the operational bridge is accordingly the instrument *algebra* rather than the statistics: multilinearity of the process tensor over the full instrument space, complete positivity of the induced slot maps, composition of noncommuting interventions»
- statement [papers/Main.md:472]: «generic action-labelled combs are not hostable on any fixed passive representation.*»
- provenance: Main §3.4, 466–476. depends_on: I2.64. yields: I2.3. bridge: none at L. bearing: none at L.

### I2.66 — Consolidation: no exact all-time realization by one fixed finite substratum
- kind: theorem (remark) with obligations (a)–(b) · level: H · status: proved [M] (finite-order periodicity); (a) exact gluing for recurrent families and (b) pre-recurrence approximation open (ledger Main.md:713) · flag: —
- statement [papers/Main.md:616]: «a bijection on a finite set has finite order $L$, so any fixed realization with a fixed prior has an exactly $L$-periodic multi-time law ($\varphi^{k+L} = \varphi^k$) — a nonperiodic target admits no exact all-time realization by one fixed finite substratum.»
- provenance: Main §3.4, 616. depends_on: I2.48 step 1. yields: —. bridge: none at L. bearing: none at L.

### I2.67 — Remarks fixing the scope of the characterization
- kind: manuscript-principle (six remarks) · level: H/M · status: proved [M] where they state counterexamples (diagonal Ĥ; `review3_probes.py`; `U(t) = e^{-iσ_x t²}`) · flag: —
- statement [papers/Main.md:608]: «so the unrestricted every-horizon form of (iii) is false, while every horizon containing a witness supports the construction.»
- statement [papers/Main.md:610]: «(i) alone does not imply (ii): a diagonal Hamiltonian satisfies the definition with $T(t) = I$ for all $t$»
- statement [papers/Main.md:612]: «The two readings are logically independent.»
- statement [papers/Main.md:618]: «(ii) without homogeneity does not deliver (i) as defined.»
- provenance: Main §3.4, 604–620 (two notions of memory 604; representation not explanation 614; closing statement 620).
- depends_on: I2.41. yields: —. bridge: none at L. bearing: none at L.

### I2.68 — Scope of the equivalence, items (iii) state update and (iv) classical P-indivisibility
- kind: manuscript-principle · level: M · status: scope statement · flag: —
- statement [papers/Main.md:630]: «the general operational update for noncommuting interventions belongs to that algebra, reached exactly under the operational completion conditions (§3.4; [GR §3.3])»
- statement [papers/Main.md:632]: «while *operational* interference and entanglement predictions require in addition the instrument and observable structure of the operational bridge, stated as open (§3.2, §3.4).»
- provenance: Main §3.4, 630–632. depends_on: I2.29, I2.57. yields: —.
- bridge: none at L — transfer denied by the corpus (entanglement predictions need the operational bridge, "stated as open"). bearing: none at L.

### I2.69 — The claim structure: the four layers, the four-part theorem statement, the conclusion
- kind: manuscript-principle · level: H/M/G · status: scope statement (layers 1–3 proved; layer 4 / part (4) requires additional hypotheses) · flag: do not assume (operational-lifting and composition hypotheses)
- statement [papers/Main.md:82]: «**(4) Full operational extension:** identifying one common *standard local quantum instrument/composite theory* for all coherent interventions requires the additional operational-lifting and composition hypotheses stated in §3.4.»
- statement [papers/Main.md:99]: «A Layer-1 result does not by itself establish any Layer-4 claim.»
- statement [papers/Main.md:756]: «Full equality with the standard local operational quantum theory requires a common compatible representation of the complete coherent instrument/composite hierarchy.»
- provenance: Main abstract 16–22, §1.3 Theorem statement 82, §1.5 97–99, §5 744–756.
- depends_on: I2.39, I2.44, I2.50, I2.40, I2.12, I2.5. yields: —.
- bridge: none at L — transfer denied by the corpus ("A Layer-1 result does not by itself establish any Layer-4 claim"). bearing: none at L.

### I2.70 — Status ledger of the foundational argument (Main §4.5)
- kind: manuscript-principle (status table) · level: H · status: status source for I2.41, I2.43, I2.54, I2.60 (and C1–C4 rows, out of scope: I1) · flag: —
- statement [papers/Main.md:708]: «It introduces no new claims; a row may not state a status stronger than its cited site, and any apparent strengthening is an error in the table, not a result.»
- statement [papers/Main.md:713]: «Proved constructively, per accessible horizon — finite-horizon process dilation reproducing the full multi-time law»
- provenance: Main §4.5, 708–720 (rows 712–720; C1–C4 necessity rows 717–720 out of scope: I1).
- depends_on: —. yields: statuses. bridge: none at L. bearing: none at L.

### I2.71 — Rest-frame selection lemma, its converse, and the boost/rotation corollary
- kind: lemma (with converse, corollary) · level: X · status: proved [M] (little-group / maximal-compact classification, [L]) · flag: —
- statement [papers/Main.md:642]: «Then the invariance group of $T$ within the local frame transformations $O(3,1)$ is the stabilizer of $n$ — the spatial rotation group $O(3)$, the little group of a timelike vector.»
- statement [papers/Main.md:650]: «> *The coarse-graining map $T$ selects a unique preferred timelike direction $n$ **if and only if** its invariance group within the local frame group $O(3,1)$ is a maximal compact subgroup $O(3)$.*»
- provenance: Main §3.5, 638–656. depends_on: horizon partition fixes a simultaneity foliation (hypothesis). yields: —.
- bridge: none at L (Lorentz frames of the substratum; not the native frame of the pair carrier). bearing: none at L.

### I2.72 — Structural observer selection (conditional on (EM)) and its corollaries
- kind: theorem (with two corollaries) · level: H/X · status: conditional-on (EM), the effective-mixing hypothesis ("an explicit physical hypothesis … not derived from φ") · flag: —
- statement [papers/Main.md:726]: «**Effective-mixing hypothesis (EM).** *The local effective channel $\mathcal{K}_{\Sigma_{\text{loc}}(V)}$ mixes, with mixing time $\tau_{\text{mix}}(\Sigma_{\text{loc}}(V))$ set by its (dissipative) spectral gap.*»
- statement [papers/Main.md:728]: «**Theorem (structural observer selection — conditional on (EM)).** Under the effective-mixing hypothesis, for any partition $V$ of bounded coupling-graph diameter,»
- statement [papers/Main.md:738]: «so the valid form is that a SUFFICIENTLY FAST-MIXING equilibrium supports no (C2)/(C4) observer.»
- provenance: Main §4.6, 722–740 (anti-Boltzmann-brain corollary 736; scope 740).
- depends_on: (EM); bounded coupling (I2.1 cone); canonical typicality [31] ([L]); I2.53.
- yields: —. bridge: none at L. bearing: none at L.

### I2.73 — What "the theorem" requires; falsifiability of the physical identification
- kind: manuscript-principle · level: X · status: empirically motivated (the identification of nature with a finite deterministic ontology; "the classical-memory test … is therefore the primary falsifiability route") · flag: —
- statement [papers/Main.md:702]: «so no experiment falsifies the theorem itself; what is empirically falsifiable is the framework's physical identification of nature with its deterministic finite ontology.»
- statement [papers/Main.md:678]: «The theorem does not identify which physical systems satisfy the conditions; this is an empirical question.»
- provenance: Main §4.2 (678), §4.5 (698–704); posit ledger Main.md:706 out of scope: I1.
- depends_on: I2.41. yields: —. bridge: none at L. bearing: none at L.

### I2.74 — Dimensional obstruction (ℏ is not fixed by transition data)
- kind: theorem (remark) · level: X · status: proved [M] · flag: —
- statement [papers/GR.md:294]: «No dimensionless data can fix a dimensionful constant — Step 4's thermal self-consistency provides the necessary dimensionful input.»
- provenance: GR §3.3, 172 and 294. depends_on: I2.27. yields: —. bridge: none at L. bearing: none at L.

***

## C. The physical layer (SM, Substratum) as far as it constrains observers or composites

### I2.75 — The nearest-neighbour reference lattice is Bell-local; the prepared-graph route is open
- kind: manuscript-principle · level: X · status: Bell-locality proved [M] (I2.7); the prepared-graph route open (H-Bell, I2.102) · flag: —
- statement [papers/SM.md:14]: «The nearest-neighbor **reference** lattice is Bell-local under measurement independence for spacelike-separated local settings and readouts»
- provenance: SM abstract 14; SM.md:60 ("This local object does not by itself supply the ontic parameter dependence required for quantum Bell violation under measurement independence; the joint-completion issue is H-Bell").
- depends_on: I2.5, I2.7. yields: I2.102. bridge: none at L. bearing: none at L.

### I2.76 — Bounded coupling degree (locality) and the minimal object
- kind: manuscript-principle (structural requirement) · level: H/X · status: assumed (bounded coupling degree: Substratum A3, out of scope: I1 as an axiom; recorded here as the locality premise of the composite statements) · flag: —
- statement [papers/SM.md:60]: «The theorems require exactly: a deterministic bijection on a finite set, whose state space factors into local degrees of freedom coupled by a bounded-degree graph with statistical isotropy, partitioned into visible and hidden sectors satisfying C1–C4.»
- statement [papers/SM.md:48]: «it is therefore a theorem for that state class, not a universal entropy theorem for every admissible prepared state.»
- provenance: SM §2.1 (48), §2.3 (60). depends_on: —. yields: I2.1, I2.77, I2.79.
- bridge: none at L. bearing: none at L.

### I2.77 — Factorization uniqueness for translation-invariant dynamics; H-link
- kind: theorem; hypothesis (H-link) · level: X · status: theorem proved [M]; H-link conditional (ROADMAP P2 H-link CONDITIONAL, ROADMAP.md:72) · flag: —
- statement [papers/SM.md:70]: «Then the natural factorization is the unique minimizer of coupling degree among all product decompositions $S = S_1 \times \cdots \times S_M$ with $|S_k| = q$ for all $k$.*»
- provenance: SM §2.4, 64–74; Main.md:4 (H-link, H-cust). depends_on: (a) translation invariance, (b) range-1 coupling, (c) bidirectional coupling.
- yields: the site factorization used by I2.1. bridge: none at L. bearing: none at L.

### I2.78 — Space as coupling structure
- kind: manuscript-principle · level: X · status: scope statement (structural reading) · flag: —
- statement [papers/SM.md:84]: «Locality is defined by the dynamics, and space emerges from locality.»
- provenance: SM §2.5, 82–86. depends_on: I2.76. yields: I2.1. bridge: none at L. bearing: none at L.

### I2.79 — Area law for the mod-q wave equation (uniform state class)
- kind: lemma · level: X/H (bipartition V | V^c of the lattice) · status: proved [M] for the uniform state class only (SM.md:48) · flag: —
- statement [papers/SM.md:118]: «For the mod-q wave equation over $\mathbb{Z}/q\mathbb{Z}$, in the uniform state class, the mutual information between V and its complement is bounded by the boundary: $I(V;\,V^c) \le |\partial V| \log_2 q$.*»
- provenance: SM §3.1, 118–120; restated SM.md:146.
- depends_on: range-1 dynamics; uniform initial conditions. yields: GR horizon entropy (physical layer).
- bridge: none at L (a classical mutual-information bound across a lattice bipartition; no statement on a composite state cone). bearing: none at L.

### I2.80 — Observer-level propagation: equivariant finite projection; the form of the center-free rule
- kind: theorem (Theorem 1a) and lemma · level: H/X · status: Theorem 1a proved [M] with kernel anchors for its isotropy step (`ohInvariant_iff`, `rem_littleO`, `rem_bigO` CubicIsotropy.lean:116 and module); the normalized A/(2d) operator conditional on observer-level center-freedom · flag: —
- statement [papers/SM.md:238]: «**Theorem 1a (equivariant finite projection preserves spatial symmetry).**»
- statement [papers/SM.md:220]: «These conditions fix the form, not the observer-level normalization of $\alpha$.*»
- statement [papers/SM.md:226]: «by [Main]'s cone theorem, $(\varphi^k(s))_i$ depends only on initial variables within graph distance $k$, so one update propagates dependence at most one edge whatever $\alpha$ multiplies the neighbour sum.»
- provenance: SM §4.1, 216–279 (Theorem 1a at 238; proof 262); Main.md:4; GR.md:266 (the observer-level lift of [SM §4.1] derives no layer flow — kernel side I4).
- depends_on: [U,R_g] = [P,R_g] = 0; I2.1. yields: I2.34 (as the lift GR.md:266 audits).
- bridge: none at L. bearing: none at L.

### I2.81 — The trace-out grading and conditional chirality (bipartite structure under observation)
- kind: theorem (Theorem 13, conditional identification) · level: X · status: conditional-on H-χ' ("H-χ' sharpened, open"); the grading's survival under marginalization proved [M] (`chirality_grading_probes.py`, Main.md:212) · flag: —
- statement [papers/SM.md:537]: «*On the visible sector the spin-chirality and taste-chirality operators coincide, so a gauge coupling is spin-chiral on the visible sector if and only if its embedding is taste-chirality-selective, while any taste-blind coupling is vector-like.»
- statement [papers/Main.md:212]: «the bipartite grading itself survives observation exactly — the effective kernel obeys $\Gamma_V K_{\text{eff}}(E)\,\Gamma_V = -K_{\text{eff}}(-E)$ for any site partition»
- provenance: SM §4.8, 535–566; Main §3.1 scope (ii).
- depends_on: staggered-to-Dirac reconstruction; H-χ'. yields: —. bridge: none at L. bearing: none at L.

### I2.82 — Genericity of observers (Theorem 22) and corollary
- kind: theorem · level: H/X · status: proved [M] for C1 and the C3 floor; C2 and C4 enter as explicit hypotheses (assumed) · flag: —
- statement [papers/SM.md:1356]: «Then for any connected subgraph V with $|V| \leq N/3$, the partition (V, H) satisfies C1, with the C3 capacity floor holding for the realized process»
- statement [papers/SM.md:1368]: «The coupled, capacious partition is a mathematical consequence; the memory-bearing observer require»
- provenance: SM §8.2, 1354–1369. depends_on: connected bounded-degree coupling graph of diameter ≥ 4; energy-conserving dynamics; C2, C4 (hypotheses).
- yields: —. bridge: none at L. bearing: none at L.

### I2.83 — The trace-out as a Jordan–Chevalley projection (SM Appendix A, Theorems A.1–A.4)
- kind: theorem (four) · level: X · status: proved [M] · flag: —
- statement [papers/SM.md:1594]: «Then: (i) N is nilpotent with N² = 0»
- statement [papers/SM.md:1630]: «The nilpotent monodromy $N$ contributes nothing to the emergent description»
- provenance: SM Appendix A, 1576–1635. depends_on: q prime, gcd(L, q) = 1. yields: Substratum.md:62 (mathematics and physics remark).
- bridge: none at L. bearing: none at L.

### I2.84 — Substratum: Theorem 23 reconstructs the local residue; Bell-inclusive existence needs H-Bell
- kind: manuscript-principle (abstract/introduction statements of I2.89) · level: X · status: as I2.89 · flag: —
- statement [papers/Substratum.md:16]: «Bell-inclusive existence additionally requires H-Bell and Bell-inclusive uniqueness is not established.»
- provenance: Substratum abstract/introduction 12–40 (also :22, :24, :32). depends_on: I2.89. yields: —. bridge: none at L. bearing: none at L.

### I2.85 — The domain of the local lattice dynamics (what observer access does and does not give)
- kind: manuscript-principle · level: H/X · status: scope statement · flag: —
- statement [papers/Substratum.md:48]: «the partition $V$ imposes observer access without changing the local update. This is enough for (i) the trace-out of [Main] over lattice-hidden degrees of freedom, (ii) the nested local trace-out of [GR §8.4], and (iii) the link-carrier construction of [SM §4.7.1.2]. It is not enough for the Bell-violating deterministic completion under measurement independence»
- provenance: Substratum §2, 48. depends_on: I2.5, I2.20. yields: I2.102.
- bridge: none at L — transfer denied by the corpus ("not enough for the Bell-violating deterministic completion"). bearing: none at L.

### I2.86 — Empirical input E2 (Bell violations)
- kind: hypothesis (empirical input) · level: X · status: empirically motivated · flag: —
- statement [papers/Substratum.md:78]: «(E2) **Bell violations.** The observed correlations violate Bell inequalities, ruling out local hidden-variable theories with factorizable distributions.»
- provenance: Substratum §3.1, 78; critical dependency Substratum.md:109. depends_on: —. yields: I2.87, I2.89.
- bridge: none at L. bearing: none at L.

### I2.87 — Stage-1 premises M1-T and M1-B
- kind: hypothesis · level: H/X · status: assumed (modeling premises of Theorem 23) · flag: —
- statement [papers/Substratum.md:122]: «**M1-B**, Bell-violating composites take [Main §3.3]'s measurement-independent, ontically parameter-dependent branch with operational no-signaling. M1-T and M1-B are logically distinct; Bell violation is not taken to imply temporal P-indivisibility.»
- provenance: Substratum §3.2, 120–141. depends_on: I2.6, I2.10, I2.86. yields: I2.89.
- bridge: none at L. bearing: none at L.

### I2.88 — Stage 2: Bell compatibility of the local lattice sector
- kind: theorem (status line) · level: X · status: theorem for the local lattice sector [M]; one-object Bell compatibility conditional-on H-Bell (I2.102) · flag: —
- statement [papers/Substratum.md:170]: «Step (b)'s nearest-neighbor **reference** cone cannot itself realize M1-B in a spacelike Bell protocol while retaining measurement independence.»
- statement [papers/Substratum.md:172]: «**Status:** Theorem for the local lattice sector; one-object Bell compatibility conditional on H-Bell.»
- provenance: Substratum §3.3, 142–172 (inputs 144; "Identification of this local lattice output with the Bell-violating Stage-1 completion additionally assumes H-Bell").
- depends_on: I2.87, I2.7; E4–E7, A3–A6 (A-axioms out of scope: I1). yields: I2.89.
- bridge: none at L. bearing: none at L.

### I2.89 — Lemma 23.0 and Theorem 23 (layered local reconstruction with Bell compatibility)
- kind: theorem (with lemma) · level: X · status: conditional-on Lemma 24.1's semigroup-transfer/completeness step (ROADMAP P1, OPEN, ROADMAP.md:64), the hidden-sector mixing hypothesis (I1), and H-Bell for the Bell-inclusive completion · flag: —
- statement [papers/Substratum.md:192]: «A single measurement-independent deterministic completion that also realizes the Bell-violating M1-B composites exists only conditional on H-Bell. The theorem does **not** establish uniqueness of that Bell-incl»
- statement [papers/Substratum.md:190]: «They do **not** compare preparation-indexed Bell edge rules or other Bell-nonlocal composite data, because neither Lemma 24.1 nor the Stage-2 uniqueness argument acts on that extra structure.»
- provenance: Substratum §3.5, 186–195; restated Substratum.md:16, :24, :32, :68.
- depends_on: E1–E7, M1-T, M1-B (I2.87), A1–A6 (I1), Lemma 24.1, mixing hypothesis. yields: I2.84.
- bridge: none at L. bearing: none at L.

***

## D. ROADMAP obligations in scope (Track B / H-Bell / H-∞ / Level III)

### I2.90 — P0 (Track B): what additional structure determines the relative quantum evolution OI leaves free
- kind: obligation (ROADMAP) · level: M · status: open (ROADMAP P0, "**OPEN**, and now LOCALIZED") · flag: —
- statement [verification/ROADMAP.md:63]: «| **P0** | What additional structure determines the relative quantum evolution OI leaves free | OI→QM / Track B | **OPEN**, and now LOCALIZED»
- provenance: ROADMAP.md:63 (queue row) and section 77–664; manuscript form I2.25 (Main.md:622).
- depends_on: I2.25. yields: —. bridge: none at L. bearing: none at L.

### I2.91 — P0a, the MAP axis (act 9)
- kind: obligation (closed) · level: M · status: proved [K] per ROADMAP ("**`P0a`, the MAP axis, is CLOSED.**"; `RB3`, `RB1-A`, `RB1-B`) · flag: —
- statement [verification/ROADMAP.md:79]: «**`P0a`, the MAP axis, is CLOSED.** Act 9 proved that **`R-2` alone** forces every same-interface»
- provenance: ROADMAP.md:79–89; act 9 result `verification/programmes/oi-qm/track-b/act-09-readback-robustness/result.md` (ROADMAP.md:649).
- depends_on: act 7 layer 2's merged theorems. yields: I2.92. bridge: none at L. bearing: none at L.

### I2.92 — P0b, the ANCHOR axis (act 10): collapsed and reclassified
- kind: obligation (reclassified) · level: M · status: open — "RECLASSIFIED as not reachable by this construction" (`AB0-A`, `AB0-B`; `AB1` withheld; `AB2` false) · flag: —
- statement [verification/ROADMAP.md:106]: «**So `P0` is NOT closed, and the anchor-axis dependence is not resolved — it is RECLASSIFIED** as not»
- provenance: ROADMAP.md:91–121; act 10 result (ROADMAP.md:644). depends_on: I2.91. yields: I2.94. bridge: none at L. bearing: none at L.

### I2.93 — Act 7's D3 gap (coherent time-indexed dilation family)
- kind: obligation · level: M · status: open ("**Act 7's `D3` gap remains separately OPEN and was not used.**"); partially subsumed by act 11 (ROADMAP.md:180) · flag: —
- statement [verification/ROADMAP.md:123]: «**Act 7's `D3` gap remains separately OPEN and was not used.** Stinespring supplies **pointwise**»
- provenance: ROADMAP.md:123–127, 180–186. depends_on: —. yields: I2.94. bridge: none at L. bearing: none at L.

### I2.94 — Act 11: GL2, GL3, GI2 (the visible family does not fix the relative evolution)
- kind: theorem (round result; ROADMAP record) · level: M · status: proved [K] per ROADMAP record (act 11 merged results) · flag: —
- statement [verification/ROADMAP.md:140]: «- **`GL2`** — a **time-dependent** element of the anchored stabilizer carries a coherent lift to»
- statement [verification/ROADMAP.md:174]: «**What act 11 does NOT license.** `P0` is not closed.»
- provenance: ROADMAP.md:129–188; kernel names cited there resolve to `CoherentLiftGauge.lean` (`def CoherentLift` :124, `def StrongAnchorStabilizer` :101, `def WeakAnchorStabilizer` :114, `def GaugeRelated` :135).
- depends_on: I2.25. yields: I2.95. bridge: none at L. bearing: none at L.

### I2.95 — Act 12: LG1, RO1, TG2, TG3, SH1 (per-slice lift freedom classified)
- kind: theorem (round result) · level: M · status: proved [K] per ROADMAP record ("**both directions at kernel level**" for SH1) · flag: —
- statement [verification/ROADMAP.md:215]: «- **`SH1`** — the shape theorem, **both directions at kernel level**: a Gram tuple is realizable iff»
- statement [verification/ROADMAP.md:223]: «**What act 12 does NOT license.** No inequivalence of OI and QM.»
- provenance: ROADMAP.md:189–244. depends_on: I2.94. yields: I2.96. bridge: none at L. bearing: none at L.

### I2.96 — Act 13: CT1–CT4, CL1 (cross-time data bounded; threading localized)
- kind: theorem (round result) · level: M · status: proved [K] per ROADMAP record (`ct2a_relative_conj` CrossTimeInvariants.lean:368; `def ConstRightRelated` :118, `def ConstLeftRelated` :123) · flag: —
- statement [verification/ROADMAP.md:256]: «- **`CT1`** — the relative evolution is exactly the lift modulo a constant right unitary, both»
- statement [verification/ROADMAP.md:292]: «**What act 13 does NOT license.** No selection principle is named, endorsed or excluded; no»
- provenance: ROADMAP.md:245–304. depends_on: I2.95. yields: I2.97. bridge: none at L. bearing: none at L.

### I2.97 — Act 14: PQ0–PQ4 (the residual freedom, carrier by carrier)
- kind: theorem (round result) · level: M · status: proved [K] per ROADMAP record; no carrier adopted · flag: —
- statement [verification/ROADMAP.md:324]: «- **`PQ1`** — the constant in-fibre left move is **redundancy relative to the visible carrier**, and»
- statement [verification/ROADMAP.md:366]: «**What act 14 does NOT license.** No carrier is adopted as the physical one and none is asserted not»
- provenance: ROADMAP.md:305–384. depends_on: I2.96. yields: I2.98. bridge: none at L. bearing: none at L.

### I2.98 — Act 15: CF0–CF5 (the cancellation fork answered `PQ3-d⁺`)
- kind: theorem (round result) · level: M · status: proved [K] per ROADMAP record ("at evidence level 2") · flag: —
- statement [verification/ROADMAP.md:408]: «- **`CF5`** — **the fork is answered `PQ3-d⁺`**, at evidence level 2, by an exhibited cancelling»
- provenance: ROADMAP.md:385–471. depends_on: I2.97. yields: I2.99. bridge: none at L. bearing: none at L.

### I2.99 — Act 16: RN0–RN4 (the re-anchored-channel carrier: `RN3⁺`)
- kind: theorem (round result) · level: M · status: proved [K] per ROADMAP record · flag: —
- statement [verification/ROADMAP.md:497]: «- **`RN3` (b)** — **the fork is answered `RN3⁺`, at line 1 of its four-outcome hierarchy**, at»
- provenance: ROADMAP.md:472–540. depends_on: I2.98. yields: I2.100. bridge: none at L. bearing: none at L.

### I2.100 — Act 17: TJ0–TJ3 (no cross-time coupling; class-level selection impossibility)
- kind: theorem (round result) · level: M · status: proved [K] per ROADMAP record (`def GramTrajEquiv` GramTrajectorySelection.lean:121, `def SelectsAt` :131) · flag: —
- statement [verification/ROADMAP.md:579]: «- **`TJ3`, the second axis** — **line 4 of the five-line hierarchy, `TJ3-IMP`**, at evidence level 2:»
- statement [verification/ROADMAP.md:592]: «**What act 17 does NOT license.** It **endorses no selection principle** and says none is required;»
- provenance: ROADMAP.md:541–629. depends_on: I2.99. yields: —. bridge: none at L. bearing: none at L.

### I2.101 — Act 7 records standing (DC1, D5, DC2a, CE1) and the chronology guard
- kind: obligation (status record) · level: M · status: `DC1` unrevised; `D5` chronological-ordering control "**NOT CERTIFIED**"; `DC2a`, `CE1` unrevised · flag: —
- statement [verification/ROADMAP.md:631]: «`D5` chronological-ordering control also stands **NOT CERTIFIED**: acts 9 and 10 repaired the»
- provenance: ROADMAP.md:630–663. depends_on: —. yields: —. bridge: none at L. bearing: none at L.

### I2.102 — H-Bell: composite and Bell closure
- kind: obligation (ROADMAP) · level: X/H · status: open (ROADMAP P1, H-Bell, "**OPEN**") · flag: —
- statement [verification/ROADMAP.md:67]: «| **P1** | H-Bell — composite and Bell closure | OI→QM / Bell | **OPEN** | Bell-inclusive completion |»
- statement [verification/ROADMAP.md:955]: «Full operational quantum mechanics in the sense of entangled composites, local operations and Bell»
- statement [verification/ROADMAP.md:965]: «the propagation/Laplacian geometry rather than on shortest-path counts. Bell-inclusive»
- provenance: ROADMAP.md:67, 953–969; Main.md:22, :394; Substratum.md:144, :170–172, :192–194; SM.md:14, :60.
- depends_on: I2.6, I2.7, I2.10. yields: I2.88, I2.89 (Bell-inclusive clause). bridge: none at L. bearing: none at L.

### I2.103 — H-∞: finite operational theory to continuum / infinite-dimensional completion
- kind: obligation (ROADMAP) · level: G · status: open (ROADMAP P1, H-∞, "**OPEN**") · flag: —
- statement [verification/ROADMAP.md:70]: «no theorem upgrades the full finite OI→QM characterization to arbitrary infinite-dimensional or QFT systems.»
- statement [verification/ROADMAP.md:939]: «continuum and quasilocal infrastructure — including region limits, continuum-source statements and»
- provenance: ROADMAP.md:70, 936–951 (`RegionLimit.lean`, `CoherentContinuumSource.lean` — `def NonMonomialCountablyCovered` :135, `def UncountableNonMonomialRays` :143 — and the quasilocal-completion audit).
- depends_on: I2.36. yields: —. bridge: none at L. bearing: none at L.

### I2.104 — P3: GR states to Level-III quasilocal states
- kind: obligation (ROADMAP) · level: G/X · status: open (ROADMAP P3, "**OPEN**") · flag: —
- statement [verification/ROADMAP.md:75]: «| **P3** | GR states → Level-III quasilocal states | Gravity / Level III | **OPEN** | formal state-layer integration |»
- statement [verification/ROADMAP.md:1151]: «whether the GR and H-state conditions **transport** to states of the formal quasilocal lattice»
- provenance: ROADMAP.md:75, 1148–1156. depends_on: I2.36. yields: —. bridge: none at L. bearing: none at L.

***

## E. Kernel-census entries mapped to records (definitions used in the recorded statements)

Every entry of `kernel_census.out` (run 2) is mapped in `CENSUS.md` §(a). Definitions that carry a hypothesis role
in a recorded theorem are named in that record's `provenance` or `status` field; the rest are mapped to the record
whose statement uses them, with the role "definition used in the statement".

## C (addendum). Records added while mapping the manuscript census

### I2.105 — State-dependent coupling graph G(x) (background independence) and its locality constraints
- kind: manuscript-principle (with an explicit construction) · level: H/X · status: assumed (the state-dependent-geometry principle; A6 itself out of scope: I1); the "reference derivation chain survives" under constraints (i)–(iii) — proved [M] for the stated construction · flag: —
- statement [papers/SM.md:104]: «(i) *Local graph-dependence:* in the reference vacuum/uniform state class, $G(x)$ at site $i$ depends only on $x_j$ within a bounded range of $i$.»
- statement [papers/SM.md:100]: «If space is the coupling graph, background independence in the geometric sense — the state-dependent-geometry principle of this section — requires the graph to evolve with t»
- provenance: SM §3.1, 98–116; Main.md:392 ("[SM §3.1] already uses a state-dependent coupling graph $G(x)$"); SM.md:152 (sparse-neighbourhood diagnostic for prepared Bell edges).
- depends_on: A6 (I1). yields: I2.6 (preparation-indexed adjacency), I2.102.
- bridge: none at L. bearing: none at L.

### I2.106 — Lattice-physics lemmas of SM §3.1 (dispersion, lattice Bisognano–Wichmann, emergent-Lorentz scope)
- kind: lemma (several) · level: X · status: proved [M] for the stated classes (the BW lemma "proved analytically [6]" for coupled harmonic oscillators, [L]) · flag: —
- statement [papers/SM.md:122]: «**Lemma** (Relativistic dispersion, one spatial dimension)»
- statement [papers/SM.md:136]: «**Lemma** (Lattice Bisognano-Wichmann)»
- provenance: SM §3.1, 118–165. depends_on: linear wave equation on the lattice. yields: GR thermodynamic chain (physical layer).
- bridge: none at L. bearing: none at L.

## C (addendum 2). In-scope statements found by the residual screen (e) outside the first section list

### I2.107 — Tensor-product structure of the emergent Hilbert space from the spatial product structure (GR §6.1)
- kind: manuscript-principle (asserted consequence) · level: H → M (cells of the visible configuration space) · status: proved [M] as a kinematic identification (stated, no separate proof, no kernel anchor) · flag: —
- statement [papers/GR.md:326]: «The emergent Hilbert space decomposes as $\mathcal{H} = \bigotimes_k \mathcal{H}_k$ — a lattice-regularized QFT with UV cutoff at $\epsilon = 2\,l_p$. The tensor product structure follows from the spatial product structure of the classical configuration space $\mathcal{C}_V = \mathcal{C}_1 \times \cdots \times \mathcal{C}_N$ (one factor per cell), which is not required by Lemma 1 but is a consequence of spatial locality in the classical substratum»
- provenance: GR §6.1, 326. Contrast in the corpus: Main.md:628 (I2.2) and Main.md:212 (I2.4) state that causal locality does not alone establish statistical product structure, local tomography or a common tensor-product instrument category.
- depends_on: site factorization C_V = C_1 × … × C_N (I2.77); the fixed-basis Hilbert-space representation (I2.39).
- yields: I2.108. bridge: none at L (a Hilbert-space factorization of configuration cells at level M; no theorem at L carries it to the field-neutral pair cone; operational composite structure not supplied, per I2.2). bearing: none at L.

### I2.108 — Locality preservation of the emergent Hamiltonian, conditional on H-local-lift
- kind: theorem (conditional) and hypothesis (H-local-lift) · level: H → M · status: conditional-on H-local-lift ("this is a missing hypothesis, not an impossibility"); H-local-lift is named only at GR.md:328 (no ROADMAP row located) · flag: —
- statement [papers/GR.md:328]: «A radius-1 reversible discrete map does not by itself fix a local continuous generator.» … «The infinitesimal argument $T_{xx'}(dt)=|H_{x'x}|^2dt^2+\cdots$ presupposes observer-level locality rather than deriving it from locality of $\varphi$» … «The theorem below therefore holds under **H-local-lift**: the selected continuous observer generator is local or quasi-local.» … «Under H-local-lift: *If the classical Hamiltonian is spatially local (couples only neighbors), then the emergent quantum Hamiltonian inherits spatial locality.*»
- provenance: GR §6.1, 328–330 (proof 330 uses the D-gauge theorem, I2.27).
- depends_on: H-local-lift (assumed); I2.27; I2.107.
- yields: —. bridge: none at L — transfer denied by the corpus (locality of φ does not by itself give a local observer generator: the four-site shift counterexample). bearing: none at L.

### I2.109 — Nested partitions beyond A.4: additive dissipators, generalized second law, effective bipartite pure state, Page curve
- kind: theorem (A.5–A.7) and conditional theorems (A.8–A.9) · level: M/X · status: A.5–A.7 proved [M]; A.8 conditional-on H-scramble; A.9 conditional-on A.8 · flag: —
- statement [papers/GR.md:755]: «*Let the classical Hamiltonian be spatially local with coupling chain $V \leftrightarrow B \leftrightarrow D$ (no direct $V$-$D$ coupling).»
- statement [papers/GR.md:813]: «**Theorem A.7** (Effective bipartite pure state). *On timescales $t \ll \tau_B^D$, the joint state of $B$ and $R$ is effectively pure»
- statement [papers/GR.md:817]: «**Theorem A.8** (Cycle typicality, conditional on H-scramble).»
- provenance: GR Appendix A.5–A.9, 753–866; GR.md:118 (coupling chain V ↔ B ↔ D by spatial locality).
- depends_on: spatial locality of the classical Hamiltonian; I2.20; H-scramble (A.8). yields: GR physical layer (GSL, Page curve).
- bridge: none at L. bearing: none at L.

### I2.110 — Weak ER=EPR at the emergent level (entangled subsystems share boundary modes)
- kind: manuscript-principle · level: X · status: scope statement (claimed "structural consequence"; no proof or kernel anchor located; "a structural prediction rather than a testable one at present") · flag: —
- statement [papers/Substratum.md:238]: «any pair of entangled subsystems in the emergent QM description shares boundary modes via the partition trace-out»
- provenance: Substratum §5 (236–242).
- depends_on: the holographic dictionary (physical layer); the emergent QM description of composites (not supplied at L; I2.2). yields: —.
- bridge: none at L. bearing: none at L.

### I2.111 — Bell/Tsirelson test: graph locality and bare C1–C4 do not enforce Tsirelson
- kind: manuscript-principle (pre-registered falsification condition) · level: X/H · status: scope statement; the Tsirelson bound is retained "only at that weaker stochastic layer" (Substratum.md:416) · flag: —
- statement [papers/Substratum.md:430]: «A confirmed loophole-free excess above $2\sqrt2$ would falsify standard quantum mechanics and any claim that the operational lift lands in the standard quantum Bell set; it would not by itself falsify P-indivisibility. Bare C1–C4 or graph locality do not enforce Tsirelson.»
- statement [papers/Substratum.md:416]: «The framework therefore does not obtain quantum Bell violation from screening plus indivisibility.»
- provenance: Substratum §6.3 (414–416), §6.4 (430).
- depends_on: I2.5, I2.6. yields: —.
- bridge: none at L — transfer denied by the corpus ("Bare C1–C4 or graph locality do not enforce Tsirelson"). bearing: none at L.

### I2.112 — H-blind: the component-blind reading of the observer's trace-out
- kind: hypothesis (named condition on the observer class) · level: X (physical carrier) · status: proved [M] for the branch's component-complete site observer at the symmetric point (SM Proposition 4b); assumed (named condition) for other observer classes and for rule extensions coupling components through a hidden sector · flag: —
- statement [papers/SM.md:12]: «the component-blind reading of the observer's trace-out — that the observation commutes with signed permutations of the six carrier components — is **H-blind**; at the symmetric point it holds for the branch's observer class, the component-complete site observer whose visible variable is the six-component field on its sites, and it is carried as a named condition for other observer classes and for extensions of the rule that couple components through a hidden sector (§4.4).»
- statement [papers/SM.md:328]: «**Proposition 4b (symmetric-point custodial scalarity for a component-complete site observer).**»
- provenance: SM abstract 12; §4.4, 328–332 (outside the census sections; located by reading); ROADMAP.md:1122 (named in the P2 H-link section, not an I2 row).
- depends_on: M = μI₆; signed-permutation-invariant counting measure; component-complete observer projection.
- yields: SM.md:126, :134 (custodially scalar response). bridge: none at L. bearing: none at L.

### I2.113 — H-observer-bundle and H-Y-vertex (conditions on the observer's trace-out for the native hypercharge coupling)
- kind: hypothesis (two named conditions) · level: X · status: assumed (named conditions of the hypercharge row; no ROADMAP row names them: `grep -c 'H-observer-bundle' ROADMAP.md` = 0) · flag: —
- statement [papers/SM.md:791]: «**H-observer-bundle**: the trace-out produces a local observer-state bundle with nonzero projective curvature in the hypercharge channel. **H-Y-vertex**: that observer connection enters the observer fermion operator with the same compact nearest-neighbour vertex and charge normalization used in §6.1. The second does not follow from the first»
- provenance: SM §6.5, 779–794 (located by reading SM §6 for the gauge-coupling scope; outside the census sections); also named at SM.md:683, :759, :773, :1294 ("conditional on H-observer-bundle and H-Y-vertex" at :683).
- depends_on: the trace-out (I2.59 channel structure, physical layer); amplitude-scale gauge (Substratum §4, out of scope: I1). yields: the native reading of the U(1) coupling.
- bridge: none at L. bearing: none at L.
