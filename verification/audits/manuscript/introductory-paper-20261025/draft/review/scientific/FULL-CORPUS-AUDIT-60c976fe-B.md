**Audit B2 of PR #918 (Introduction), full-corpus scientific audit, slice: papers/Introduction.md L190–L259 and L320–L346**

Target: `draft/oi-introductory-paper-20261025` at 60c976fec83677ee4bb6496bf48b03f2bc76823a. Its parents are 6251af27 and main 0d917665. Line numbers below are for that blob. The work was read-only, in a detached worktree, which has been removed without gc or prune. I did not build Lean; that is not possible here. Every kernel claim was checked by reading the Lean source at the head. The `verification/lean-mathlib` tree is 8624ba39 at 17b830bc, 55e3217b, 0d917665 and 60c976fe alike. The axiom footprint was checked from the retained `papers/introduction_repro/results-121598983127.json`.

## Verdict: BLOCK

The slice is accurate in most of what it states. Theorem 4, the five conditions, the §3.3 kernel results and the Bell ceiling are faithful to their sources. Nine blocking items remain:

- Two required audit changes that the owner has already ruled on (OD-2, OD-3) are not applied.
- One cited declaration formalizes a different clause from the one the text describes.
- Two results rest on census families marked `kernel-only`, and the census does not cover the Introduction at all.
- There are one miscitation, two missing Bell hypotheses, one missing kinematics hypothesis, and one heading that reads as a no-go.

Every item is a local text change, plus one corpus precondition (PR-G). The paper becomes ACCEPT once B1–B9 are resolved.

## Blocking findings

### B1. L226: what the substratum supplies is understated (audit R-06; owner OD-2)
- **Current text:** "Which of (iii)–(v) a physical substratum supplies is the open step toward full operational equivalence."
- **Source:** GR §3.3, Substratum-source form (GR L260) and Layer-flow form (L266). The kernel declarations are:
  - `realizesSealedOICore_of_control` (OIRealization:252)
  - `permClass_onesFixing` and `onesFixing_not_phasesAvailable` (PhaseSource:79, :52)
  - `monomialSource_not_control` (SubstratumInterface:186)
  - `readWriteSourced_not_control` (ReadWriteControl:169)
  - `substratum_residual` and `substratum_plus_control_qm` (StructuralClosure:383, :414)
- **What is wrong:**
  - For the substratum as formalized, the kernel settles part of the question.
    - The stated access supplies no quarter phase.
    - With the phase assumed, the operations are monomial.
    - On the qubit, condition (iv) fails.
    - Adding continuous control of the elementary transitions, with closure kept, gives exact finite operational QM on every nonempty finite carrier.
  - Presenting all of (iii)–(v) as open misrepresents this. The converse is also missing: condition (iv) alone realizes the OI core, so Theorem 4 classifies OI-compatible theories and does not derive QM from OI.
- **Proposed text:** R-06's L120 text. Starting at "Conversely, every qubit theory satisfying (iv) realizes that process, so Theorem 4 classifies the completions compatible with embedded observation and does not derive quantum mechanics from it. Because a bijective intervention acts on configurations as a permutation operator, … (machine-checked for the substratum class as formalized in [GR §3.3]). Whether a physical substratum supplies the phases and that control is open."
- **Same edit, outside the slice:** the abstract (L17), L304 and L312 item 1. The new declarations go into Appendix A, with their axiom reports added to `papers/introduction_repro/` (OD-15).

### B2. §3.4 (L240–L246): the ε-realization result is missing (audit R-07 as amended by R-40; owner OD-3)
- **Current text:** the section states only the obstruction, ending "The obstruction does not touch Theorem 1, whose realization is chosen per law."
- **Source:** Main §3.4:
  - Theorem (finite operational realization and gluing — ε-form), L560
  - Corollary (single controlled dynamics), L576
  - Theorem (uniform continuum realization — mutual ε-density), L592
  - the comb theorem, L476
  - SC-1 (#947, merged) restricts the proved result to the exact-arithmetic regime.
- **What is wrong:** as written, §3.4 reads the obstruction as the whole story. The owner ruled that the ε-realization result must appear. The #918 r16 record (item I-12) notes that it is absent.
- **Proposed text:**
  - Heading: "3.4 Finite realizations of quantum experiments".
  - Append R-07's L130 paragraph with R-40's substitutions:
    - "which holds the unnormalized quantum state exactly in its hidden sector and applies one fixed bijection per instrument, sampling outcomes on a finite grid"
    - "A fixed finite family is also realized exactly, by one fixed realization with a real-valued product prior […]; the accuracy ε enters with a rational uniform seed and with uniformity over the instrument continuum"
  - Mark the result "(proved on paper, in exact arithmetic)". State no finite-precision constant.

### B3. L244: miscitation of Montina (audit R-17)
- **Current text:** "explicit tasks are given by Galvão and Hardy [GH03] and Montina [Mon08]"
- **Source:** Mon08 proves a lower bound on ontological dimension and gives no task. The explicit finite prepare-and-measure tasks are in HKLP24 Thm 4, which Main L554 cites.
- **Proposed text:** "explicit tasks are given by Galvão and Hardy [GH03] and Heinosaari et al. [HKLP24, Thm 4]". Keep Mon08 for the report of Hardy's result.

### B4. L256: the lattice-Corollary clause drops the intervention hypothesis (disagrees with SC-33's corrected text)
- **Current text:** "The nearest-neighbour cubic update of the lattice substratum [SM] alone cannot supply that dependence for wings outside each other's causal cone [Main §3.3, Corollary …]."
- **Source:** Main §3.3 Corollary (Main L410). It requires setting interventions applied at one step to disjoint wing regions, each reading and writing only its own, and a ±1 outcome in every run. SC-33 (#968) adds exactly this hypothesis at book ch02:188: "…in a Bell protocol with one-step own-wing setting interventions whose wings lie outside each other's graph cone".
- **What is wrong:** with non-local interventions, parameter dependence arises whatever the graph is, so the hypothesis carries weight.
- **Proposed text:** "…cannot supply that dependence in a protocol whose setting interventions, applied at one step, each read and write only their own wing, and whose wings lie outside each other's graph cone [Main §3.3, Corollary (Bell–lattice obstruction and state-dependent escape)]."

### B5. L250: Bell's bound is stated without measurement independence
- **Current text:** "…explained by information the pair carried from the start, each outcome depending only on its own laboratory's setting. For any such explanation the Clauser–Horne–Shimony–Holt combination … is at most 2 in magnitude"
- **Source:** Main §3.3, Theorem (Bell ceiling for a screened local completion), hypothesis (iv) (Main ~L360). Main §3.3(b) shows that measurement-dependent models exceed 2.
- **What is wrong:** without measurement independence the stated bound is false.
- **Proposed text:** "…explained by information the pair carried from the start, independent of the settings later chosen, each outcome depending only on its own laboratory's setting."

### B6. Appendix A L339–L340, census and corpus consistency (§A.35, §A.25; audit OD-4)
- **The kernel-only families:**
  - Theorem 3 rests on `pIndivisible_of_rooted_identity_return_of_overlap` (RecurrenceHorizon:148).
  - The routed-readback result rests on PhysicalC4Discharge.
  - In `verification/lean-manuscript-census.json` both families are `kernel-only` with no anchor.
- **The census does not cover the Introduction:**
  - `papers/Introduction.md` is not in the registry's manuscripts list.
  - The tool's resolution step reads only `kernel:` parentheticals, and the Introduction has none.
  - So the release gate's `lean-manuscript` step resolves none of the 29 Appendix A identifiers. The census passes at the head only because of this.
- **Main contradicts the Introduction:**
  - Main §2.3 L139 says the kernel checks only `isPermMatrix_of_stochastic_inverse` and that "its composition with P-divisibility … [is] proved on paper".
  - The Introduction (L160, L162, L306, L339) says Theorem 3 is machine-checked in rooted form, which the kernel bears out.
  - So the Introduction is more accurate than its source and leaves the source uncorrected (owner policy 1).
  - No open source-correction PR (#961–#969) touches the census or this text.
- **Fix:** land PR-G before #918.
  - Main §2.3 states the rooted overlap form and the routed-readback result with their kernel anchors.
  - Both families move to `current` with anchors.
  - The Introduction is added to the census, and its Appendix A identifiers become resolvable: either the tool reads Appendix A, or the entries use the `kernel:` form.
  - Interim alternative: narrow L160, L162 and L306 to Main §2.3's present statement.

### B7. Appendix A L340: the cited declaration formalizes a different readback clause (audit R-13; owner OD-5)
- **Current text:** "`routed_forces_indivisible_somewhere` (PhysicalC4Discharge:122), indivisibility at some return horizon from routed readback"
- **Source:** the module header of PhysicalC4Discharge (lines 27–35) records a discrepancy it does not repair:
  - its `rootedPosterior` conditions the initial hidden seed;
  - the stated clause names the law of the hidden state at the storage time;
  - so the two readings are not the same predicate.
  
  The Introduction's gloss (L162: "a record of the visible history written into the hidden state is routed back") is the storage-time reading. That reading is formalized as `routedAtStorage_forces_indivisible_somewhere` (PhysicalC4StorageReadback:256, with its `#print axioms` at :709).
- **Proposed text:** cite `routedAtStorage_forces_indivisible_somewhere` (PhysicalC4StorageReadback:256) for the storage-time reading as primary, and `routed_forces_indivisible_somewhere` for the reading conditioned on the initial hidden state. Add the new axiom report to `papers/introduction_repro/`. That module's census family must also be made `current` (part of B6).

### B8. L214: Theorem 4's kinematics hypothesis is not stated
- **Current text:** "an operational theory specifying which finite outcome families of linear maps are available on the system"
- **Source:** `FiniteOperationalTheory` (OperationalAssembly:594). Availability is over maps `Matrix A A ℂ →ₗ Matrix A A ℂ` and over `A × Fin n` at each level. The complex matrix kinematics is assumed, not derived (audit CON-15/R-10).
- **What is wrong:** in an OI paper, "finite system" reads as a configuration set. The theorem presupposes complex-matrix quantum kinematics, and the text does not say so.
- **Proposed text:** "…which finite outcome families of linear maps on the complex matrices indexed by the system's states (and, at each ancilla level, by system and ancilla states) are available…".
- **Corpus pairing:** the same clause belongs in GR §3.3 (PR-B, CON-15).

### B9. L230: the §3.3 heading reads as an unscoped no-go (audit R-28)
- **Current text:** "### 3.3 The evolution relating two times is not selected"
- **Source:** Main §3.4, Remark (scope: representability, not selection of the relating evolution), L640: selection is open, and Main "neither closes the third nor claims it cannot be closed".
- **Proposed text:** "### 3.3 Representability does not select the evolution relating two times"

## Optional findings

- **O1. L200:** state the one implication that is proved. "Among what is proved" lists only non-implications. Main L622 proves that Markov implies P-divisible, so for positive-probability roots P-indivisibility on {0,…,n} implies M_t > 0 for some 0 < t < n. R-02's proposed sentence covers this.
- **O2. L234:** "and compose exactly across times" names a vacuous condition. CoherentLiftGauge's header says "The cocycle condition is vacuous … holds for every family whatsoever", and `CoherentLift` (CoherentLiftGauge:124) has no composition clause. Drop the phrase. Main L640 has the same wording.
- **O3. L236:** state the construction. The kernel's object is a trivial-ancilla lift at one time, taken as the fixed-basis evolution with uniform initial law and identity readout (TrackBQfbBridge header; Main L640).
- **O4. Appendix A L341 (§A.34 form):** name the directional witnesses of `rooted_eq_iff_slice_eq`. These are `slice_eq_of_rooted_eq` (TrackBQfbBridge:171) and `visible_congr` (:130); both have `#print axioms` lines.
- **O5. L204:** the Pauli-twirl classical-memory decomposition of the uniform-burn-card game is correct. I checked it: Σ_o Ad σ_o ∘ (σ_o·σ_o/4) = id. It is not in Main §4.5, which supports only the fixed-card clause. Either add it to Main §4.5 or mark it as shown here.
- **O6. L214:** "which an available operation may follow" overstates the closure rule. `prepAvail_post` allows only a deterministic (single-outcome) available operation to follow. Proposed: "which an available deterministic operation may follow".
- **O7. L256:** the gloss "settings statistically independent of the pre-setting state" is about the wrong variable. Main §3.3 says measurement independence fails for the full pre-setting microstate whenever more than one setting pair occurs, and that Ω is the response-relevant variable. Proposed: "…independent of the response-relevant pre-setting variable Ω".
- **O8. L256 and L258:** "preserving … the gravitational continuum limit" presupposes a limit that is not established for the reference graph. Main §3.3's Corollary paragraph says the hop-metric curvature route already fails for the reference graph, and GR §8.2 treats the continuum limit as a posit. SC-33 uses the same "preserve" wording and defers this caveat. Consider adding "(not yet established for the reference graph itself)".
- **O9. L244:** add the interface assumption that preparations and measurements interface only through the N ontic configurations (Main L554).
- **O10. `papers/introduction_repro/README.md`:** the table lists "The 28 declarations of Appendix A", but Appendix A has 29. `c3_necessity_via_hidden` is missing from the table; the JSON does contain it, with the three axioms.
- **O11. L324:** "the commit at which that result was retained" should read "produced". The result was produced by the run at 17b830bc and is retained on #918.

## Checked and correct

- **L192:** the three reasons are faithful.
- **L196:** the definitions are adequate.
- **L198:** a revival of distinguishability implies P-indivisibility (Main L153).
- **L200:**
  - The CP-indivisibility theorem, for a permutation unitary with a diagonal hidden state, matches Main L326 and the diagonal-preservation lemma at L322.
  - The Hadamard counterexample matches Main L330.
  - The three-notions citation matches Main L334.
- **L204:** for the card game, one step gives tr(ρ)I/2 (Main L286), two steps give the identity, so the family is CP-indivisible; the fixed-card realization admits no classical-memory decomposition (Main L714).
- **L208:** BLP09 and BJA17 match Main L332; the representation-not-explanation remark matches Main L632.
- **L214:** the standing structure matches the fields of `FiniteOperationalTheory`: identity, coarse-graining, composition at ancilla levels only, uniform preparation, the spectator-independent readout (`MapSpectatorIndependent`, id ⊗ Φ on product inputs) and discard. It is more complete than GR L216.
- **L216–L220:** conditions (i)–(v) match `CompositeOperationalValidity`, `SystemToLevelOne`, `InertSpectatorCompositionality`, `HasCompositeUnitaryControl` and `IteratedAncillaClosure`.
- **L222, Theorem 4:**
  - It matches `exactAll_iff_physical_general` for nonempty A (GR L218).
  - §A.34 is satisfied: ⇒ is `physical_of_exactAll` and ⇐ is `exactAll_of_physical_general`.
- **L226:** `five_way_minimality` gives one fixed C1–C4 core and qubit witnesses, each failing exactly one condition. `oi_alone_not_qm` uses `diagTheory`, which preserves diagonals. The well-formed/substantive split matches GR L220.
- **L234:**
  - `gl2_strong_gauge_moves_relative_candidate` is existential, on an exhibited pair of lifts.
  - `gl3_constant_gauge_preserves_relative` is general.
  - Main L640 says the same.
- **L236:** `bridge_traj`, `rooted_eq_iff_slice_eq` and `realData_traj_stochastic` (Q_fb-realizable and stochastic) say what the text says.
- **L244 (apart from B3 and O9):** the factorization is proved and the unboundedness is imported, as in Main L554; Theorem 1 is untouched.
- **L252, the Bell ceiling against Main §3.3:**
  - graph separation: (iii), d_G(B,R_A) > k_A and its mirror;
  - one-step own-wing interventions: (ii);
  - readouts outside the other wing's cone;
  - a ±1 outcome in every run;
  - measurement independence: (iv);
  - determinism: (i);
  - Ω response-complete;
  - ontic parameter independence: secured by (ii) and (iii) through the cone lemma.
  
  The conclusion matches. The ceiling is described as proved on paper, which is correct.
- **L256 (apart from B4, O7 and O8):**
  - The either/or is correctly placed.
  - The adopted branch is ontic parameter dependence with measurement independence retained and operational no-signalling.
  - There is no outcome-independence placement.
  - H-Bell is described as open.
  
  This agrees with SC-33 (#968) and SC-17 (#963).
- **L324:**
  - Lean v4.33.0 and Mathlib rev v4.33.0 are correct.
  - 17b830bc and 55e3217b are both on main, and the Lean trees are identical.
  - The `lean-axioms` semantics are described correctly.
- **L326:** the code paths exist at 55e3217b, the root LICENSE is MIT, and the DOI matches README.md.
- **Appendix A:**
  - All 29 declarations exist at the stated module:line.
  - The prose does not exceed any statement.
  - Every declaration has a `#print axioms` line in source, four of them fully qualified, so every one is in the lean-axioms set.
  - All 14 modules are imported by `OIBridge.lean`.
  - The retained JSON has exactly one report per declaration, each [propext, Classical.choice, Quot.sound].
  - Census families are `current` for 12 of the 14 modules; the two exceptions are covered in B6.
  - No sorry, admit or axiom tokens appear outside comments.
- **Open source-correction PRs:**
  - SC-29 (#961) makes comment-only Lean edits and joint-law wording changes in Main. Appendix A already says "joint-law form", and its line pins at 17b830bc are unaffected.
  - SC-28 (#962) and SC-31 (#967) change nothing the slice cites.
  - SC-22 (#964) changes the book only.
  - SC-32 (#969) changes SM only.
  - SC-17 (#963) and SC-33 (#968) agree with §3.5, apart from B4.
- **Register (§A.32/§A.33):** no hits in the slice.

## Outside the slice

- **L17, L304, L312:** these need the same edit as B1. L17's "stated minimal structure" claims a minimality the kernel does not prove.
- **L39:** "The results of §§3.2–3.5 are proved in [GR] and [Main]" (audit R-11).
  - Theorem 4 and §3.3 are proved in the Appendix A Lean declarations; GR and Main state them.
  - The §3.4 unboundedness is imported.
- **L188:** "no card arrangement violates a Bell inequality" is false without restricting the moves and settings; Main L356 realizes PR-box behaviour (audit R-32).
- **L306:** "Theorem 3 in its rooted form" machine-checked depends on B6.
- **Corpus, under owner policy 1:**
  - GR §3.3 L216 omits the structure fields that the Introduction states (CON-48, PR-B).
  - Main L139 understates the kernel (B6).
  - Main L640 has the vacuous "each composing exactly across times" (O2).
  
  None of these is covered by an open source-correction PR.
