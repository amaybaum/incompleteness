# A1 recovery plan r1: P1, P12, P6 and P7

**Status:** paper-only plan. No proof attempt, Lean change or build, scientific computation, manuscript edit, premise adoption or recovery is performed by this document. Each unit needs its own later execution authorization under Q12(b). A1 remains an open, unadopted hypothesis; it is neither established nor disproved. A4 is unchanged.

**Goal link — #1169:** determine which existing mathematical conclusions can retain their strongest justified form without total finiteness, and identify the first missing hypotheses where they cannot. This serves the OI–QM foundations investigation; a negative result or a precisely parked gap is an acceptable outcome. Mathematical recovery alone does not establish an explanation of nature.

**Authority and writer.** Owner `amaybaum`, 2026-11-16T05:59:47Z, [#1169 comment 6908679641](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-6908679641), records the owner's own words: “I approve, although due to usage limits, lets run this in Codex. Can you prepare instructions?” The recorded decision authorizes Addendum 2 and this four-unit paper-only plan, with Codex as writer, separate review, no proof attempts and no merge. It does not authorize executing any step proposed here.

## 1. Source versions and interpretation

Primary theorem citations below are to `main` at `e4c6ba7f20da39fd57e67c8225457fe5f6c1f6f6`. Paths and line numbers were read from that version. Lean identifiers are read from the modules; no Lean compilation is performed for this plan, and no new kernel certification is claimed.

Supporting audit inputs are at research commit `c6e850583cd01163b87ae0b66b4966ad0eb603be`, under `verification/audits/foundations/a1-foundations-20261115/`:

| Input | Role and limit |
| --- | --- |
| `audit/A1-IMPACT-AUDIT-r9.md`, AM-1–AM-38, especially AM-2.1, AM-5, AM-11, AM-22, AM-30, AM-36 and §§12–14 | Recovery dependency inventory. Its classifications and proposed routes are planning assessments, not proofs that a recovery succeeds. Its review limitations remain those stated in its closing section. |
| `ef1/EF-1-r7.md`, especially §4.2 and its result-class tables | Reviewed-draft lineage, off main. Its header explicitly says r7 itself has not been reviewed in this form; earlier reviewed lemmas retain only their marked review scope. Neither that lineage nor the present plan certifies every r7 reading. Its line references use an older main snapshot, so primary citations here were checked again. |
| `assessment/FOUND-ASSESS-r7.md`, §§1.1–1.4 | Distinguishes mathematical representation, native physical sourcing and full quantum recovery. Used as an assessment, not as a substitute for the cited proofs. |
| `gauge-trace/GAUGE-A1-TRACE-r3.md`, §§1.2–1.6 and §3 | Separates proof-step uses of finiteness from finite model definitions and observer-branch construction. r3 carries the focused review of r2 and its nits; its own stated limitations remain. |

These off-main documents support the choice of proposed work, not an enduring new theorem. A later landing must separately trace and retain any off-main content needed by its claims under §A.42. This plan is not an integration decision.

“Weakest sufficient hypotheses” below means the least additional contract identified for the specified target, separating an algebraic implication from its realization and physical application. No claim of absolute logical minimality is made without a necessity proof. A hypothesis written on main may still be a posited model input or an open physical condition.

| Unit, in planning order | Already available | Genuinely outstanding | Present execution status |
| --- | --- | --- | --- |
| P1 | Finite-horizon realization; diagonal preservation; P-indivisibility implies CP-indivisibility in the stated channel class | Weighted-prior identification of that realization's rooted populations with its channel family | Plan only; no recovery credit |
| P12 | Local representation algebra and conditional stabilizer results; A1-use trace | An A1-independent setting and observer branch, plus separate continuum and common-model bridges | Plan only; A4 and branch gaps explicitly retained |
| P6 | Exact finite counting-prior reciprocity, including time-reversal qualifications | Measure-preserving measurable-carrier version, with an identified reference measure | Plan only; no reference measure adopted |
| P7 | Conditional finite-shell counting, reciprocal flux and calibration | A justified shell-state family without total finiteness, and its connection to the same measured transitions | Plan only; no shell state or thermal condition adopted |

## 2. P1 — finite-window channel and applicable Born-form identity

### Existing results to preserve

1. `papers/Main.md:268–270`: permutation unitarity. `verification/lean-mathlib/OIBridge/EquivalenceChain.lean:233–235`, `OIBridge.permConj_apply`, gives the permutation-conjugation identity; the finite permutation-unitarity support is already cited in Main's kernel inventory.
2. `papers/Main.md:286–288`: the Born-form representation for the uniform hidden prior. This is a representation identity, not a derivation of the Born exponent or of physically available quantum operations.
3. `papers/Main.md:326–328` and `verification/lean-mathlib/OIBridge/EquivalenceChain.lean:242–254`: `OIBridge.Phi` and `OIBridge.isDiag_Phi`. The latter proves diagonal preservation for an arbitrary complex hidden weight. Positivity and normalization of that weight are additional requirements for interpreting the expression as a CPTP channel.
4. **The P-to-CP implication is already proved**, in `papers/Main.md:330–332`, with the same reduction in `book/appendix-b-derivations.md:92–94`. CP-divisibility of a family preserving computational diagonals yields a stochastic intermediate population map; its contrapositive gives CP-indivisibility when the populations are P-indivisible. This paper proof is not a new recovery target. `papers/Main.md:334` states why the implication fails for general CPTP families, using the Hadamard boundary.
5. `papers/Main.md:520–524`: a finite-horizon law has a constructed finite reversible realization with a hidden prior independent of the visible initial state; arbitrary real kernels use the response-table extension. `verification/lean-mathlib/OIBridge/Equivalence.lean:245`, `:294`, `:422` and `:462` contain `Qfb_imp_S`, `D_imp_Qfb`, `S_imp_D` and `finite_horizon_equivalence`. The kernel realization statement and Main's separately stated root-independent process construction must not be conflated: Main itself states the formalization limit in the construction's proof.
6. `verification/lean-mathlib/OIBridge/CausalReadback.lean:54–68` defines window P-divisibility and rooted revival; `:134–144`, `OIBridge.CausalReadback.c4r_implies_pIndivisible`, is the recurrence-free mathematical diagnostic. It uses a finite visible matrix family, not global recurrence, reversibility, a hidden prior or a physical apparatus.

### Sufficient contract and statuses

| Hypothesis | Status and exact role |
| --- | --- |
| A finite visible alphabet and one finite horizon K | On main: the stated finite-observer/model scope. It does not imply finite total nature. |
| One chosen finite H, one permutation φ on V × H, and one fixed probability μ_H independent of the visible root | On main as constructed realization data in Main:520–524. Not a native preparation mechanism. Do not replace the common prior by separately fitted priors at different times or roots. |
| μ_H(h) ≥ 0 and its masses sum to one | Probability conditions, required for the state `diag μ_H` and the CPTP interpretation. `isDiag_Phi` alone does not certify them. |
| The channel family is the permutation dilation with that same μ_H, and its diagonal populations equal the rooted family Γ_t on the whole window | The family definition is available; the general weighted-prior identification is the remaining P1 application step. It is not a new physical premise. |
| Γ is P-indivisible within that window | An input to the implication. A measured rooted revival can certify it via `c4r_implies_pIndivisible`; no claim that memory alone supplies this input. |

For the P-to-CP implication alone, permutation dilation and finite H are stronger than necessary: diagonal preservation of the channels at the compared times, their matching population maps, and CPTP intermediate maps suffice, as Main:332 already proves. The stronger realization contract is needed here to connect the chosen law to those channels, not to reprove that implication.

### New step, not performed

State and verify the weighted-prior population identity for the chosen realization and all `t ≤ K`, with `ρ_H = diag μ_H`. At one step the target is `P(j|i) = Γ_1(i,j)` and the proposed Kraus weights are `sqrt(μ_H(k))`; at later times the same realization and prior must give the same rooted populations. This is the AM-5 representation application. Combining that identification with the existing implication is AM-2.1, not a new general theorem equating classical and quantum non-Markovianity.

**Cheapest decisive first step, named only:** attempt the weighted diagonal-action identity at one arbitrary window time, with the conventions for φ and its permutation matrix fixed, then check that Main's response-table realization supplies the same root-independent μ_H across the window. Reuse Main:332 and `isDiag_Phi`; do not start a new CP-divisibility theory, a simulation, a Lean development or a recurrence argument.

### Stopping and significance

- **Completes the mathematical unit:** an independently checked statement identifying the populations with Γ_t for a single chosen realization throughout the window, with the correct CPTP probability hypotheses, followed by explicit reuse of the existing P-to-CP proof. Preserve the uniform-prior theorem as a special case and the Hadamard qualification.
- **Refutes a proposed version:** a counterexample satisfying its stated hypotheses but failing its population identity or inference. A counterexample obtained by dropping diagonal preservation refutes that stronger version, not Main's scoped theorem.
- **Parks it:** the construction gives only a joint/root-conditioned prior, or the maps at different times require different realizations. Name the missing common-prior/window-identification lemma; do not fit it context by context.

The infinite-XOR construction on main, `verification/programmes/substratum/continuous-substates/infinite-xor-counterexample.md`, §§“Exact autonomous model and normalized state” and “OI diagnostics / scope”, is a standing countercontrol: accessible history memory can coexist with P-divisible rooted maps. It is not executed here. P1 would recover a representation application and a conditional diagnostic, not a universal revival prediction, Born-law selection, native preparation, coherent control or OI–QM equivalence. No converse CP-to-P-indivisibility assertion is proposed.

## 3. P12 — local gauge reconstruction and its finite-setting boundary

### Existing results to preserve

- `papers/Substratum.md:189–195`: Lemma 23.0 and Theorem 23, including their distinction between local-sector uniqueness and Bell-inclusive existence conditional on H-Bell. Neither establishes uniqueness of a full Bell completion.
- `papers/SM.md:224–228`: the local wave-form result within its nearest-neighbor, symmetry and linearity class. `:242–254`: Theorem 1a and Lemma 1c for the projected evolution and canonical/resummed branch. `:270–276`: Corollary 1b, with **observer-level** center-freedom as an extra condition.
- `papers/SM.md:340–344`: Theorem 5's stabilizer statement, conditional on H-link, its one-copy clause, H-cust and a generic O-equivariant condensate. `:374`: Theorem 7's exact six-link representation; `verification/lean-mathlib/OIBridge/LinkDecomposition.lean:479`, `OIBridge.LinkDecomposition.theorem_7`, is its link-representation witness, not a theorem that nature has this carrier.
- `papers/SM.md:575–610`: the separate charged-matter/anomaly steps in reducing to the stated SM group and hypercharges. The representation-group conclusion is not an independently sourced Yang–Mills action, confinement mechanism or binding-energy calculation.
- `verification/lean-mathlib/OIBridge/SubstratumInterfaceAudit.lean:106`, `a2_every_substratum`, and `verification/lean-mathlib/OIBridge/A6Instantiation.lean:541`, `as1_leap_covariant`, supply their stated algebraic bijectivity/covariance facts. They are not witnesses for all of Theorem 23, H-link, H-cust or the observer-level lift.

### Three distinct finiteness obligations

| Entry point | Existing source and status | Least sufficient replacement to investigate; not adopted |
| --- | --- | --- |
| **A4 + site factorization (viii) + finite alphabet (xiii)** | A4 explicitly specifies a finite periodic lattice (`papers/Substratum.md:98`, repeated at `:157`). The gauge trace §3 records that, with the other two inputs, this already makes the lattice carrier finite. Removing the separate A1 label does not remove that finite class. | For an abstract local algebra lemma, require only the finite link representation and the stated symmetry/condensate data. An infinite-lattice or undetermined-cardinality reconstruction needs a separately authorized class specification, such as U-A4, before it can claim to go beyond A4's current finite class. A4 is unchanged here. |
| **Continuum passage on finite graph families** | `papers/SM.md:150–152`, `:170–214`; `papers/Substratum.md:157`, `:171`: dimension selection and continuum interpretation retain their graph-family and physical-input assumptions. The already identified cubic hop-metric obstruction is not repaired by making the lattice infinite. | A compatible family of approximants and a controlled limit for the relevant propagation/curvature observable, with its assumptions explicit. A finite dependency patch, or a symbol written on Z^d, does not supply that limit. This remains a separate gap. |
| **Finite-S construction of the observer branch** | Theorem 1a starts “Let S be finite”; Lemma 1c uses an invariant measure/structured prior and a finite-dimensional determinant/Schur argument (`papers/SM.md:242–254`). The bridge from φ to the specified observer operator is open at `:232`. | A normalized invariant state or measure, a well-defined equivariant observer projection and dynamics, and the particular branch properties actually used. For a fixed number of steps, bounded operator products can be the proposed target; an infinite-dimensional meromorphic determinant/pole identity must not be inferred from the finite identity. H-cust/condensate data can instead be explicit conditional inputs, but that supplies no native source. |

These are separate gates. A local proof that never mentions |S| can still be stated on objects whose only available realization is finite. Conversely, one need not introduce a global measure merely to prove the finite link-module algebra with its inputs given.

### Hypothesis statuses for the intended local conclusion

| Required data | Status |
| --- | --- |
| The six-link complex carrier with cubic decomposition T1 ⊕ E ⊕ A1 and multiplicities (3,2,1) | Exact representation algebra on main. Its physical identification and single-copy selection are H-link, conditional/open. |
| A custodially scalar pre-condensate kinetic structure, an O-equivariant Σ, and three distinct block values | Theorem 5's named conditional data. At the bare algebraic level, a complex six-dimensional space with those three spectral blocks suffices for the product unitary stabilizer; this restates the algebraic input rather than deriving a physical condensate. Proposition 4b (`papers/SM.md:334–336`) supplies only its stated finite-counting, symmetric-point, component-complete case. |
| Observer-level translation, scalarity, locality, symmetry, constant preservation and center-freedom | Conditional branch requirements of Corollary 1b. Microscopic center-freedom does not establish the observer-level condition. The φ-to-observer bridge remains open. |
| A4's lattice class, A3/A5/A6, nearest-neighbor premise, E4–E7 and continuum conditions | Existing named model/physical inputs on main, not a derivation from OI alone. This plan neither relaxes A4 nor proves their necessity. |
| Amplitude-scale gauge, charged matter action, family pattern, anomaly conditions, hypercharge-branch qualification, H-spin′ and H-χ′ | Retained conditional inputs or scope qualifications of the existing matter/group chain. No assumption is removed because a narrower algebra lemma does not consume it. |
| P1/P5b/P6/P7 and the common Stage-1-to-lattice identification | Dependencies of a broader reconstruction, not automatically supplied by the local algebra. P5b is outside this plan's execution scope; P6/P7 have their own measure obligations. H-Bell and the full common-model problem remain separate. |

### Cheapest first step and stop rules

**No current route past unchanged A4 is asserted.** The class issue is already identified by the gauge trace; re-deriving that observation earns no recovery credit. If the owner keeps exactly that finite class, an “A1-free” theorem obtained solely by deleting the redundant A1 premise is not recovery for undetermined cardinality.

**Cheapest decisive first step, named only and conditional on later authorization:** before attempting Theorem 23, attempt the fixed-lag equivariant-projection lemma for a specified normalized invariant measure and bounded Koopman/observer operators on a proposed undetermined-cardinality carrier. The decisive question is whether that one defined branch actually meets the inputs of Corollary 1b and Theorem 5. Retain H-cust and observer-level center-freedom as hypotheses where they are not proved. Do not start a continuum limit, new condensate construction or full reconstruction proof first. If no authorized carrier/measure/projection is available, stop before the attempt with those named gaps. A genuinely infinite model also waits for the separate A4-class decision.

- **Completes a local subunit only:** a precise conditional local algebra/projection result with every branch input supplied or openly hypothesized, and no hidden use of a finite determinant or uniform total counting. Such completion does not complete full P12.
- **Completes full P12 only:** the three gates above are discharged at the claimed scope; Lemma 23.0/Theorem 23 are restated with the strongest supported hypotheses and each downstream step traced. Stage 3 retains P7 and H-slope; Bell-inclusive existence remains conditional on H-Bell and the common realization, with no uniqueness claim added.
- **Refutes a proposed extension:** a model satisfying its explicit replacement inputs but violating its claimed invariant, or a branch counterexample to the claimed descent. A failure of one projection or approximant refutes that route, not every possible reconstruction.
- **Parks it:** unchanged finite A4; no invariant normalized state/projection; unproved observer-level center-freedom; no controlled continuum step; or no common Stage-1/lattice interface. Name the first unsatisfied link. Supplying these as posits would change a conditional contract, not recover a native derivation.

No equivalence between the full SM group and an arbitrary underlying lattice is asserted here. The forward stabilizer/representation statements and any converse lattice-selection claim are separate obligations; Theorem 7b's prose converse is not certified by Theorem 7's kernel witness.

## 4. P6 — reciprocity with a specified invariant measure

### Existing result and target

`papers/SM.md:641–643`, Theorem 19, and `verification/lean-mathlib/OIBridge/Reciprocity.lean:79–81`, `:129–145` prove `count_reciprocity`, `theorem_19` and the `detailed_balance` specialization for a finite counted H. The kernel explicitly carries involutivity and `φ⁻¹ = Θ φ Θ`; it does not assume a finite visible type. Division by |H| is the counting-prior probability version. Preserve it without weakening its qualifications.

The proposed measurable-carrier target is `T_ij(n) = T_(θj)(θi)(n)` with an explicitly specified common hidden probability μ_H. It is a conditional extension of AM-30, not the source of μ_H or of physical time-reversal invariance.

### Sufficient contract and statuses

| Hypothesis | Status |
| --- | --- |
| Measurable H; finite discrete observer V; measurable bijection φ on V × H with measurable inverse | Proposed mathematical setting. Finite V is the operational scope, not a claim of necessity for the abstract result. Infinite-H version not proved by the existing counting kernel. |
| Partition-preserving measurable involution Θ = θ × θ_H and `φ⁻¹ = Θ φ Θ` | Explicit model conditions. Finite counting version is on main; their satisfaction by a selected infinite native carrier is not inferred from finite-S reversibility. |
| A normalized μ_H, independent of the visible root; `ν = counting_V ⊗ μ_H` invariant under φ; μ_H invariant under θ_H | Additional statistical contract. Given as conditional mathematical data, it adopts nothing. It is not an OI-derived measure of nature; physical adoption would require a separate Q6/§A.29 decision. |
| Measurable transition fibres for every tested n | Required to define T_ij(n) and compare their masses. Supplied by the proposed measurable setting, not by cardinality alone. |

The identity needs mass preservation of the reversal pairing on the relevant transition fibres. Global invariance of ν and Θ is the transparent sufficient all-n contract proposed here; necessity of that stronger global contract is not claimed. No shell condition or thermal assumption is needed for this abstract P6 target.

**What is already proved versus new.** The finite fibre bijection, its involution requirements and the passage to φ^n already exist. What remains is the measure version of the fibre-mass comparison and its well-posedness on the declared space. The audit's review of the algebraic route is not a published infinite-carrier theorem or a physical measure source.

**Cheapest decisive first step, named only:** attempt the measure-preserving transition-fibre identity for one arbitrary fixed n under the contract above, reusing the existing reversal algebra. This precedes any lattice, continuum or physical measure construction. If the exact required invariant measure cannot even be specified, park the physical application rather than launching a new source screen.

### Stopping and significance

- **Completes the conditional mathematical unit:** a checked measurable theorem with normalized μ_H and all hypotheses explicit, preserving the finite counting case and the `(θj,θi)` result at all stated n.
- **Refutes a proposed version:** a well-defined model satisfying every proposed hypothesis with unequal paired masses. A counterexample without ν-invariance refutes an unqualified extension, not the conditional target.
- **Parks it:** no selected invariant product measure or no partition-preserving reversible dynamics on the intended carrier. A state that changes with i or n does not meet the common-prior contract.

Ordinary `T_ij = T_ji` still requires θ to fix the compared coarse states. A nonuniform visible reference generally calls for a weighted flux relation, not this unweighted identity; it is not silently substituted for counting_V. P6 would constrain laws only under its premises. It would not fix the CKM invariant, choose a probability law, establish thermal detailed balance, construct apparatus, or establish quantum mechanics.

## 5. P7 — shell counting and horizon calibration

### Existing results to preserve

- `papers/GR.md:58`: finite-shell occupation weights and the entropy derivative β_E under H-count, including the negligible-interaction assumption for the Gibbs marginal and its finite-bath correction.
- `papers/GR.md:68–70`: time-reversal pairing of shell trajectories. Symmetric detailed balance requires time-reversal-even coarse states; otherwise only the time-reversed-label relation holds.
- `papers/GR.md:74–86`: the calibration `a_* = τ_K/β_E = c³ ε²/(4Gσ)`, conditional on H-slope, H-count and identifying the same operational transitions. H-spectrum implies H-balance implies H-slope; their converses are not supplied. The calibration fixes the relation between ε, σ and the action scale, not a parameter-free numerical prediction of ħ.
- `papers/GR.md:56`, `:98–102`, and §8.5(b): the exact de Sitter/horizon/frame/infrared conditions. It is not an established general dynamical-FLRW calibration.
- `papers/GR.md:122–132`: the separate H-BD and fixed-window deep-sector comparison. Its bounds on transition laws do not certify an invariant energy-shell measure, an exact reciprocal flux, a derivative of an entropy, or stability of a fitted calibration.

There is no Lean identifier in the traced corpus that proves this full shell-to-calibration chain. `OIBridge.Reciprocity.theorem_19` is a finite counting-prior reciprocity theorem, not a proof of the horizon density of states, H-slope or the shell application. This statement concerns the traced chain, not a claim that the entire repository contains no relevant formal mathematics.

### Sufficient contract and statuses

| Hypothesis | Status and scope |
| --- | --- |
| A defined conserved energy and a family of normalized shell states/laws at the compared energies, with finite positive relevant densities/multiplicities and the stated entropy derivative or controlled finite-difference regime | The finite counting form is on main at GR:58. An undetermined-cardinality replacement is new conditional data, not supplied by a finite window. A separately justified thermodynamic interpolation is needed where literal finite counts do not admit the derivative used. |
| A measure-preserving shell bijection and a shell-preserving time-reversal involution | The finite trajectory-count argument is on main. The replacement shell dynamics/state must satisfy these properties; neither P6's product-state theorem nor a finite causal cone supplies them. |
| Time-reversal-even coarse states for the symmetric rate ratio | Existing qualification, GR:68. Do not infer symmetry merely because Θ preserves the visible/hidden partition. |
| Boundary/deep entropy bookkeeping replacing the finite H-count justification | H-count is an existing named condition, not a derived source. The authorized but unmerged #1313 text explicitly carries A1 in that condition. An A1-free recovery cannot keep the full conjunct and claim to have removed A1. It must separately justify a replacement shell law whose energy-dependent entropy has the required boundary slope; this plan neither posits nor adopts it. |
| Negligible boundary interaction at the shell scale for the auxiliary Gibbs marginal | Existing condition at GR:58. Strong-coupling corrections require a different justified treatment. The calibration's scalar β_E route does not require imposing the stronger H-shell Gibbs factorization, as GR:86 explains. |
| H-slope on the actual accessible detector transitions, and identification of those transitions with the classical shell transitions | Existing open condition, GR:70–86. It is not a consequence of finite-law representation or of P1. Retaining it is weaker than demanding the full H-spectrum/KMS assumption. |
| Boundary mode count, σ, exact de Sitter calibration, horizon/frame assumptions and the conditions of GR §8.5(b) | Existing inputs or qualifications. No claim here that they follow from an arbitrary infinite substratum. |

P6 and P7 share the need to justify a statistical state, but their states differ. P6 proposes counting_V × μ_H with the same hidden law for each visible root. On a shell, `μ_H(h|i)` generally depends on the visible energy i. `papers/GR.md:86` expressly warns that substituting it into Main's product-preparation channel changes the preparation and projection theorem. A success for P6 cannot be carried into P7 without checking this distinction.

### New step and cheapest test

An independent normalized deep factor is a useful conditional reference case, not a physical producer. Even in that case, its energy dependence must be specified: an energy-dependent deep multiplicity changes β_E. With an interacting deep sector, preserving complete visible histories on a fixed window does not preserve an equilibrium shell law or its entropy–energy slope. EF-1 r7 §4.2 explicitly identifies this limitation; its product-measure invariance route does not carry shell counting.

**Cheapest decisive first step, named only:** attempt one conditional shell-state replacement lemma, before the calibration: specify a normalized family at the energies compared and check whether its shell reversal preserves the measured flux while its marginal entropy slope is the boundary value required by GR:58. Start with the exact decoupled reference case to separate elementary factor cancellation from the genuinely missing coupled-shell/state justification. If no candidate family with justified normalization, invariance and energy dependence is available, stop at that missing input; do not invent one to fit the desired coefficient. No shell is constructed and no count, derivative, counterexample or simulation is evaluated in this plan.

The coupled branch needs its own error statement. H-BD is posited, and GR:128 already shows that the slow-influence version fails for the stated linear rule at cuts where a deep site enters the boundary update. Do not retry that excluded route as if an untested small parameter existed. Even where a transition-law estimate holds, a bound on the logarithmic rate ratio needs nonzero probabilities or explicit lower bounds, and a slope/calibration estimate needs further regularity. None is provided by the old error bound alone.

### Stopping and significance

- **Completes a reference-case subunit only:** a checked decoupled-factor shell result with its energy-independence and invariance assumptions stated. This is not a native physical recovery or a coupled-sector result.
- **Completes P7 at its declared scope:** a justified A1-independent shell-state family, a checked reciprocal-flux/β_E statement with its corrections, and a calibration conclusion retaining H-slope, transition identification and all horizon conditions. A conditional theorem with a supplied shell family is labelled conditional; it does not establish that nature supplies the family.
- **Refutes a proposed version:** a model satisfying its explicit replacement assumptions but violating the flux, entropy slope or claimed error propagation. A deep sector with energy-dependent multiplicity only refutes a version that failed to exclude or control it.
- **Parks it:** no normalized invariant shell family; no energy-independent deep contribution where required; uncontrolled coupling; no justified slope; or no common operational transition. Keep the finite conditional theorem and name the missing input. Do not infer disproof of A1, absence of every possible shell construction, or recovery of the 1/4 coefficient.

Even full conditional P7 would not establish detector preparation, the Born exponent, coherent instrument availability, vacuum selection, the area-mode physical premise or a unique native OI mechanism. It would not independently validate all GR universality claims AM-36 or discharge Theorem 23's other links.

## 6. Dependencies, decisions and later execution

The planning order is **P1, P12, P6, P7**. P12 is scoped early because the three finite-setting gates must be visible before commissioning its broad reconstruction. Its full conclusion cannot be delivered before its downstream mathematical and source dependencies. P6/P7 may share a state-dependency inventory later, but remain different units with separate stopping records.

| Open owner question for a later authorization | Why it matters |
| --- | --- |
| Authorize only P1's weighted-realization application first? | It reuses the existing P-to-CP proof and needs no new physical premise. The plan does not itself authorize that attempt. |
| For P12, retain the current finite A4 class, or separately scope a local/infinite-class variant? | Retaining finite A4 cannot establish reconstruction for genuinely undetermined cardinality. A change of class is not a documentary deletion of A1. |
| Is a future P6/P7 unit a conditional theorem with a specified state, or also a separately justified physical state-source investigation? | Those have different burdens and authorizations. Neither state is adopted by this plan. No source screen is started. |
| Which P7 scope is wanted first: exact decoupled reference case or a specified coupled-shell extension? | The former can preserve a conditional calculation; it does not answer the physical coupled case. H-BD cannot be presumed at native cuts already excluded by GR:128. |

Any uncertain external literature used in later recovery is **to be checked first-hand** before it supports a proof or a priority decision. No external theorem is newly imported here to fill a missing hypothesis. The immediate deliverable is a separately reviewed plan, not a proof, an implementation or a premise-adoption packet.

**End condition for this assignment:** publish this immutable plan checkpoint, obtain an independent non-author review of theorem citations, hypothesis statuses, cheapest first steps and stop conditions, correct plan defects without executing the units, and report the location, verdict and remaining owner questions on #1169. No unit receives recovery credit. Physical source remains **NOT PASSED**; full OI–QM equivalence remains open.
