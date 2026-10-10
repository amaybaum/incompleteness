# DS — review of the supplied double-slit analysis (thread DS, research-only)

Protocol `PROTOCOL-STAGE2-DS.md` (`086a4cb8…`) over `PROTOCOL-STAGE2.md` (`38603692…`), `PROTOCOL.md` (`239dc123…`),
amendments 1 (`b41aa0e7…`) and 2 (`2a2f78f3…`). Input `inputs3/DS-INPUT.md` (`ffb6eb75…`), read as data. Base L =
`9f9f8257a980a1819fbbc1dc0019917cf8678626` at `pt/base/`. Not read: `pt/S2/`, `pt/S3/`, `pt/audit/S2/`, `pt/audit/S3/`,
`pt/audit*-replay/`. No branch, PR, CI run, fetch or repository change.

Evidence levels, kept apart throughout: **[K]** certified at L (module in the certified build; route stated in §1.1);
**[D]** kernel-checked in the design run `ff9c3a35`, not certified; **[W]** written argument; **[X]** exact computation in
this directory, stated for the instance it checks; **[L, unverified]** literature not read at the source; **UNBUILT**
Lean (none written here). Repository facts cite `file:line` at L.

## 0. Answer

**Bottom line.**
1. Physics: both formulas are exact [X]; the second needs a record acting on the detector only, undisturbed propagation,
   normalized pure detector states and no readout; mixed detectors need γ = tr(U_L†U_Rρ₀), and D = 0 with V = 0 occurs [X].
2. Repository: AncillaInterference [K] and the finite-horizon equivalence [K] are read faithfully; Main §4.1 is not (the
   input puts the arrangement in the hidden sector, Main L662 the visible); the ROADMAP is quoted without its INDEPENDENT rows.
3. Levels: 1 drops the load-bearing "fixed-basis"; 2 is right; 3 understates (Main L568 [K]; the phase source [K]).
4. Target: not well-posed at L; R1–R3 are met exactly by a reversible model with no amplitudes and no OI memory [X].
5. Not independent of S2/S3: the record is the landed gate on a product (`bell_mem`'s (BS) instance [D]); only the eraser
   readout tells a coherent record from a separable one [X]; a cnot + phase-kick detector family leaves K_gen [X].
6. Labels: framework-specific target UNRESOLVED relative to L; the input's generic route refuted; nothing INDEPENDENT.
7. Take: description ≠ derivation (C2), the definite-path caveat (C31), the formulas with their assumptions (§2).
   Discard: C26, C41, C45a, C46, C53.

**Verdict table (DS.1).** Not numbered as assertions: the UI line "Worked for 1m 58s" and the three image links, which
were not fetched. C45 is split into C45a and C45b.

| id | claim (short) | verdict | anchor |
|---|---|---|---|
| C1 | the framework already offers a mathematical connection to the double slit | ACCURATE WITH CORRECTION | what exists is a universal representation (Main L534 "universal") and interpretive text (Main L660–664); ROADMAP L1442–1447 |
| C2 | describing ≠ proving embedded observation necessarily produces it | ACCURATE | Main L20 "representability alone does not distinguish"; L750 "it is not the selector" |
| C3 | "after reviewing the repository" | NOT CHECKABLE AT L | author's process |
| C4 | Level 1: exact Hilbert-space, unitary, Born representation of finite laws | ACCURATE WITH CORRECTION | ROADMAP L39–41 "exact **fixed-basis** Hilbert-space, unitary and Born-rule representation"; `finite_horizon_equivalence` [K] Equivalence.lean:459; Q_fb law collapses at every step :207–214; Main L534 |
| C5 | Level 2: interference explained by restricted access, as a proposal | ACCURATE | Main L660 "Interpretive Consequences"; Explainer L568; ROADMAP L1442–1447 |
| C6 | Level 3: necessary generation "not yet established" | UNDERSTATED | `S_imp_D` [K] Equivalence.lean:419 (every finite law is realized); Main L568 [K `readWriteSourced_not_qm` ReadWriteControl.lean:174]; ROADMAP L1399–1414 |
| C7 | "we can already explain the proposed connection mathematically" | OVERSTATED | ROADMAP L1442–1447; the certified constructions represent the law with no interference term [X ds7_models B9] |
| C8 | a full operational equivalence proof would strengthen it | ACCURATE WITH CORRECTION | a conditional one exists: OI⁺ ⟺ exact finite endomorphic QM, Main L564–568 [K `carrier_general_oiPlus` CarrierGeneralOIPlus.lean:213]; over complex matrix carriers, ROADMAP L973–974 |
| C9 | even that needs a concrete experimental model | ACCURATE | P0 OPEN ROADMAP L63; Main L622; observer interface ROADMAP L918–931 |
| C10 | the double slit is an excellent example | ACCURATE | the corpus's own showcase, Explainer L564–568; validation target ROADMAP L1442–1447 |
| C11 | both slits open ⇒ interference pattern | ACCURATE | [X ds5 F1, CC-F1a]; the experiment itself [L, unverified] |
| C12 | a which-slit record ⇒ interference disappears | ACCURATE WITH CORRECTION | only for a perfect record; partial records give V = V₀\|γ\| [X ds5 F2, F5] |
| C13 | no conscious observer needed | ACCURATE | the formula has the detector unread, traced out [X ds5 F2, CC-F2d]; Explainer L574 |
| C14 | availability of distinguishable path information is what matters | ACCURATE WITH CORRECTION | pure records: V² + D² = 1 [X ds5 F6]; mixed: γ = tr(U_L†U_Rρ₀) [X F3], and D = 0 with V = 0 occurs [X ds5 CC-F6; ds7_structure S2 at n = 0] |
| C15 | P(x) = \|ψ_L+ψ_R\|² (ψ's absorb the source amplitudes) | ACCURATE | [X ds5 F1, F2-unitary]; the received text lost "x" after "at position" |
| C16 | the expansion with 2Re(ψ_L*ψ_R) | ACCURATE | [X ds5 F1] |
| C17 | the last term makes fringes possible | ACCURATE | [X ds5 F1, F5] |
| C18 | with a detector: P = … + 2Re(ψ_L*ψ_R⟨d_L\|d_R⟩) | ACCURATE WITH CORRECTION | exact under the assumptions of §2 [X ds5 F2, F3; CC-F2a–d each fail when an assumption is dropped] |
| C19 | the overlap determines how much interference survives | ACCURATE WITH CORRECTION | \|γ\| fixes V = V₀\|γ\|; arg γ shifts the fringes [X ds5 F4-iii, F5] |
| C20 | identical detector states ⇒ full interference can remain | ACCURATE | [X ds5 F4-i] |
| C21 | perfectly distinguishable ⇒ overlap 0 ⇒ term disappears | ACCURATE | [X ds5 F4-ii, F6-charpoly]; mixed with orthogonal supports [W, §2] |
| C22 | the formula connects observational access, records and interference | ACCURATE WITH CORRECTION | it connects records (their overlap) with interference; access plays no role [X ds5 F2] |
| C23 | it is standard QM, not yet derived from OI foundations | ACCURATE | ROADMAP L1442–1447; the derivation uses amplitudes and a unitary coupling [X ds5] |
| C24 | Main §4.1 proposes a physical explanation | ACCURATE | Main L660 "### 4.1 Interpretive Consequences", L664 |
| C25 | the observer cannot access the complete state | ACCURATE | Main L16 "cannot access the complete state" |
| C26 | the hidden part includes the environment and the experimental arrangement | INACCURATE | Main L662 "photons, electrons, slits, detectors — are all visible-sector objects"; nearest: Explainer L568, hidden sector "includes the field configuration near both slits" |
| C27 | opening the second slit changes the complete dynamics, even if one path | ACCURATE WITH CORRECTION | Main L664 "changes the boundary conditions of the transition matrix"; φ is one fixed bijection, Substratum L414, Main L560; Main asserts the single path outright |
| C28 | a detector changes the dynamics and the information recorded elsewhere | ACCURATE WITH CORRECTION | Main L664 "couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix" |
| C29 | not a mysterious response to human observation | ACCURATE | Explainer L566–568, L574 (not in the cited Main lines) |
| C30 | it reflects dynamics of a larger system the observer cannot inspect | ACCURATE | Main L662 "downstream consequence of the trace-out"; Explainer L568 |
| C31 | a definite slit is an interpretation, not proved by the observable-law equivalence | ACCURATE | Main L660/L664; Substratum L412 "On the structural reading"; same law with and without a path variable [X ds7_models B2, B9] |
| C32 | two particularly relevant pieces of existing mathematics | ACCURATE WITH CORRECTION | the corpus has more directly relevant results, two negative for the target: ROADMAP L1399–1414, Main L568, Main L562, Main L20/L534, CompositeDimension.lean:1222 |
| C33 | the finite-horizon equivalence: finite laws admit reversible and fixed-basis unitary/Born representations | ACCURATE | Main L526–534; [K] Equivalence.lean:459–465, :419, :294; the missing expression is not recoverable from the received text (corpus: S⟺D⟺Q_fb, Main L18, L748) |
| C34 | it is universal, including classical processes | ACCURATE | Main L20, L534; Equivalence.lean:20–23 "its classes include Markov laws" |
| C35 | it does not force interference or select a phase mechanism | ACCURATE | stronger at L: the constructed representation has no interference term [K Equivalence.lean:294–342, :207–214; X ds7_models B9]; phases INDEPENDENT, ROADMAP L1399 |
| C36 | AncillaInterference.lean contains a kernel-proved result | ACCURATE | [K] route §1.1: OIBridge.lean:114; lakefile.toml:2; verify.yml:70, :127, :150; census :201–221 |
| C37 | it shows how creating and recombining coherence reveals an otherwise undetected operation | ACCURATE WITH CORRECTION | proved: KrausSound ∧ HasAncillaQubitInterference ⇒ the specific surplus `badOp 2` is unavailable (AncillaInterference.lean:302–304), via branches 3/2, −1/2 (:201–202) |
| C38 | it is mathematically related to interferometry | ACCURATE | seed, mixer, operation, mixer, readout (:17–27, :168–169) |
| C39 | it is not a derivation of the double slit from embedded observation | ACCURATE | stronger: its mixer moves the all-ones ray, so the stated access cannot make it available [W over K: InstrumentRealization.lean:398, PhaseSource.lean:79; X ds7_structure S6] |
| C40 | the ROADMAP explicitly recognizes this distinction | ACCURATE WITH CORRECTION | ROADMAP L1442–1447, but classed "a publication-facing validation target rather than a dependency gap" under "Deliberately not prioritized" (L1422) |
| C41 | the necessary mathematical machinery exists | OVERSTATED | ROADMAP L1443 says the machinery "that such a benchmark would consume"; same file L1399–1400, L1409–1414 and Main L568: phases and state mixing are not sourced (available → derived) |
| C42 | no dedicated theorem derives the formula from named OI premises | ACCURATE | ROADMAP L1443–1445 |
| C43 | the block-quoted target is particularly valuable | OVERSTATED | as stated, not well-posed at L and non-discriminating (§3(a)–(b)) |
| C44 | it would require demonstrating the three things R1–R3 | ACCURATE WITH CORRECTION | as necessary conditions, yes; not sufficient: met exactly by CL1 [X ds7_models B1–B4]; none tests record coherence [X ds7_structure S3] |
| C45a | narrower than completing K2 for every composite system | INACCURATE | K2 is the two-copy d = 3 composite, ROADMAP L1001–1006; arbitrary carriers are Kₙ, L1058–1069; the detector setting is itself a K2 object [K CompositeDimension.lean:1222; X ds7_structure S1] |
| C45b | potentially more accessible | OVERSTATED | only one fixed coupling fits inside stage-1's K_gen, with its premises; a cnot + phase-kick family leaves K_gen [X ds7_structure S5]; the eraser readout is not in the stated access [S6] |
| C46 | could be investigated now, independently of S2/S3 | INACCURATE | only R1 is single-system [X ds7_structure S2]; the record is `bell_mem`'s (BS) instance [D pt/inputs/fourcopy/FourCopyLocal.lean:266]; §3(c), §4 |
| C47 | full equivalence would show all preparations, transformations and measurements follow quantum rules under the premises | ACCURATE WITH CORRECTION | exists conditionally at L (OI⁺, Main L564–568 [K]); stated over complex matrix carriers (ROADMAP L973–974) |
| C48 | the double-slit probabilities would then follow once the operations were realized | ACCURATE WITH CORRECTION | the Born form follows; values need the relative evolution, not fixed by OI (ROADMAP L63; Main L622), and its phases (L1399) |
| C49 | it would not establish that embedded observation uniquely explains the physics | ACCURATE | Main L562 "not a uniqueness theorem: the same reversible machinery can realize non-quantum finite instrument families"; Main L22 |
| C50 | the stronger conclusion requires sourcing premises and connecting to an apparatus | ACCURATE WITH CORRECTION | matches the open rows (ROADMAP L66, L68, L918–931); "requires" is methodological, not a proved necessity |
| C51 | the biggest opportunity is not merely reproducing the equation | NOT CHECKABLE AT L | evaluative |
| C52 | quantum mechanics already reproduces it | ACCURATE | [X ds5 F1, F2] |
| C53 | demonstrate why incomplete access + reversible dynamics + hidden records + measurement interactions must produce that equation | INACCURATE | as phrased: [K] `S_imp_D`; [X ds7_models CC-B6, B8]: non-quantum patterns from those ingredients, with C4 memory; Main L568 [K] |
| C54 | doing that without assuming interference structure would be a genuine explanatory result | ACCURATE WITH CORRECTION | true as a conditional, but its antecedent fails for C53's ingredients alone; with named added principles the result would be CONDITIONAL |
| C55 | potentially one of the clearest ways to communicate OI's contribution | NOT CHECKABLE AT L | evaluative |

**Target assessment (DS.7), with labels (amendment 2) and evidence levels.**

| item | label / status | evidence |
|---|---|---|
| T-DS, framework-specific reading: the interference and which-path formulas follow from the framework's certified premises for a double slit realized in its substratum, with no amplitudes as premises | **UNRESOLVED** relative to L. L defines no double-slit arrangement, detector, observation map/ensemble (Obs, μ) or OI-native pair system in the physical substratum. The non-insertion clause is unformalized. Relative phase and nonclassical readouts are not sourced by the stated access | ROADMAP L918–931; [K] StochasticInterface.lean:118; [K] PhaseSource.lean:52, :104; INTEGRATION-REVIEW L119 |
| the input's generic route (C53, and the target's own premises "one observer embedded in a deterministic system"): such observers must produce the quantum formulas | **route refuted** (not INDEPENDENT: the countermodels satisfy the route's premises; I did not check every certified premise of the framework's physical substratum) | [K] `S_imp_D`; [X] CL0 (CC-B6), CL0m with a C4 witness (B8) |
| R1–R3 as success criteria | non-discriminating: CL1 (no amplitudes, no visible memory, so C4 fails) meets all three exactly at the stated instance | [X] ds7_models B1–B4; countercontrols CL0 (fails R1), CLfree (fails R2) |
| R2's record: the record state | the landed native gate applied to a product state: cnot(prodState xplus z3) = phiW | [K] CompositeDimension.lean:1222; [X] ds7_structure S1 |
| R2's derived amount | path coherence × n₁, where n₁ is the detector state's component on the gate's flip axis: a second-system quantity | [X] ds7_structure S2 |
| eraser variant | the only part that tells a coherent record (phiW) from a separable record (ω_B); it needs the pair correlation table | [X] ds7_structure S3 |
| path phase control plus two readouts | a CHSH scenario reaching 2√2 > 2 | [X] ds7_structure S4; H-Bell ROADMAP L67, L953–966 |
| detector family with cnot and phase-kick markings | the phase-kick record is the landed T_ψ = actT R_H phiW ∉ K_gen. A common state space needs IE1 at R_H, or frame covariance (flagged in stage 2) | [X] ds7_structure S5 + [W]; kt4_prem1_probe.py:560–562 |

**What the owner should take from the input.**
- The distinction between a mathematical description and a proof that embedded observation produces it (C2).
- The definite-path caveat (C31).
- The textbook formulas, with the assumptions of §2 attached.
- A double-slit benchmark as a communication target, in the hard-to-vary form of §3(b)–(d) only.

**What to discard.**
- "Narrower than K2 for every composite system" and "independently of the S2/S3 work" (C45a, C46).
- "The necessary mathematical machinery exists" (C41).
- The closing route "… must produce that equation" (C53).
- The paraphrase that puts the experimental arrangement in the hidden sector (C26).

## 1. Claim by claim (DS.1–DS.4, DS.6, DS.8)

### 1.1 DS.2 — the three cited locations

**(i) `papers/Main.md` L660–664.**
- L660 is the heading "### 4.1 Interpretive Consequences".
- L662: "The degrees of freedom involved in quantum experiments — photons, electrons, slits, detectors — are all visible-sector objects. Their quantum behavior is a downstream consequence of the trace-out".
- L664: "In the double-slit experiment, the particle traverses a single slit in the deterministic substratum. The interference pattern arises because opening or closing the second slit changes the boundary conditions of the transition matrix, altering the distribution of detection events. A which-path detector at one slit couples the trajectory to additional visible-sector degrees of freedom, changing the transition matrix and eliminating the interference terms." L664 continues with the Born rule as "part of the exact fixed-basis representation dictionary", "What remains open is the common coherent operational extension of that dictionary to all interventions and composites", and the equilibrium-of-the-cycle reading as "the cosmological realization's mechanism proposal rather than a theorem of this paper".

Faithfulness of the input's paraphrase (input L71–75): partly faithful.
- **Unfaithful:**
  - it puts the experimental arrangement in the hidden part, against L662 (C26);
  - it says opening a slit "changes the complete dynamics", whereas Main changes the boundary conditions of the transition matrix with one fixed φ (C27);
  - it softens Main's flat single-slit assertion to "even if";
  - it drops "visible-sector" for the detector's degrees of freedom (C28).
- **Omitted:** L664's own statement that the common coherent extension "to all interventions and composites" is open. That residual is exactly where a detector read in more than one way sits (§3(c)).

**(ii) `verification/lean-mathlib/OIBridge/AncillaInterference.lean`** (406 lines, read in full).

Definitions:
- `hSign`/`hRaw`/`hMat` (:87–94): the balanced mixer (1/√2)[[1,1],[1,−1]];
- `ancMix A = 1 ⊗ₖ hMat` (:97–99);
- `ancScale` (:144–145);
- `HasAncillaQubitInterference T := T.prepAvail 2 (pureAttach 2 0) ∧ T.availExt 2 Unit (fun _ => conjChannel (ancMix A))` (:161–163);
- `tauChain` (:168–169);
- `HasAncillaQubitSwapControl` (:358–360);
- `HasAncillaQubitInterferenceControl` (:365–366).

The surplus is `badOp 2`, which "Leaves every ancilla-diagonal block alone and DOUBLES every ancilla coherence" (HiddenCoherence.lean:461–465).

Theorems (variables `[Fintype A] [DecidableEq A]` throughout):
- `sqrt2_inv_sq`, `sqrt2_inv_star`, `hRaw_gram`, `hMat_unitary`, `ancMix_unitary` (:101–124): arithmetic and unitarity;
- `conjChannel_ancMix_tensor` (:128): the mixer acts on the ancilla factor only;
- `hMat_apply`, `hMat_conjTranspose_apply` (:136–141);
- `badOp_tensor` (:148): the surplus scales ancilla coherences;
- `mix_seed` (:172): after one mixer every entry is 1/2;
- `tauChain_diag` (:201): the branches are 3/2 and −1/2;
- `interference_branch` (:239): seed–mix–surplus–mix–read–discard multiplies the system state by `tauChain k k`;
- `form_of_one_single`, `smul_id_cp_nonneg` (:256, :281): a negative multiple of the identity is not completely positive;
- **`interference_exposes_badOp` (:302–304)**: `[Nonempty A] (T : FiniteOperationalTheory A) (hsound : KrausSound T) (hint : HasAncillaQubitInterference T) : ¬ T.availExt 2 Unit (fun _ => badOp 2)`;
- **`compositeControl_hasInterference` (:350–352)**: `HasCompositeUnitaryControl T → HasAncillaQubitInterference T`. The docstring says "One direction only … does NOT license 'strictly weaker'";
- `interferenceControl_hasInterference` (:369–371);
- **`interferenceControl_exposes_badOp` (:376–379)**: KrausSound and the control-side certificate exclude `badOp 2`;
- `compositeControl_hasInterferenceControl` (:382–385).

The file's own scope note (:63–67): "It kills THIS surplus, a specific non-CP block multiplier; it says nothing about every possible one."

*Evidence level, and how it was established.* **[K]**, by the build route at L:
- the root import `import OIBridge.AncillaInterference` (OIBridge.lean:114);
- `defaultTargets = ["OIBridge"]` (lean-mathlib/lakefile.toml:2);
- the CI job "Mathlib bridge" (.github/workflows/verify.yml:70) runs `lake --rehash build` (:127) and then the release gate (:150), whose step `lean-axioms` reads the kernel's `#print axioms` report (tools/release_gate.py:137–138);
- none of the 214 OIBridge files contains the token `sorry` (the nine whole-word `admit` hits are English prose in comments, checked);
- the census registry lists the module (lean-manuscript-census.json:213) in family "instruments, dilation and assembly" (:201), status "verification-only" (:220), with no manuscript anchor.

No Lean was rebuilt here (no toolchain). The [K] rests on L being certified main and the module being in its default build target.

Faithfulness of the input's paraphrase (C36–C39): faithful, with corrections.
- The theorem is an *exclusion* of one specific non-CP surplus in any Kraus-sound theory carrying a pure ancilla seed and the balanced mixer. "Reveal" means positivity forbids the −1/2 branch.
- Its premises carry complex-matrix kinematics (`FiniteOperationalTheory` over `Matrix A A ℂ`; ROADMAP L973–974 for the operational layer) and the mixer.
- The mixer moves the all-ones ray: hMat(1,1) = (√2, 0), with no scalar z solving (√2, 0) = z(1,1) [X ds7_structure S6]. The stated observer access is ones-fixing (`permClass_onesFixing`, PhaseSource.lean:79; `permTheory = genTheory permClass`, :104–106), and in a ones-fixing theory every available unitary conjugation fixes that ray (`instAvail_unitary_fixes_ones`, InstrumentRealization.lean:398–400). So `HasAncillaQubitInterference (permTheory A)` fails for nonempty A [W over K]. The theorem's interferometric premise is a resource the corpus certifies the stated access does not supply.

**(iii) `verification/ROADMAP.md` L1442–1447**, quoted: "**Named double-slit / Born-interference benchmark** — the repository already formalizes the probability, phase, realizability and quotient machinery that such a benchmark would consume, but there is no dedicated kernel theorem packaged as 'OI conditions X imply the textbook double-slit interference formula.' This is a publication-facing validation target rather than a dependency gap in the present equivalence chain; it returns to the queue if a central claim begins to depend on that explicit packaging." It sits under "## Deliberately not prioritized" (L1422).

Faithfulness: both halves of the input's sentence are there (C40, C42). The input omits two things:
- the classification: packaging, not a dependency gap;
- the same file's "Settled negatively — INDEPENDENT" rows in the section immediately above (L1392–1414), which bear directly on any non-conditional derivation. These are "The source of phases | **INDEPENDENT**" (L1399), "Dense/nonclassical operational control from the presently stated architecture | **INDEPENDENT**" (L1400), and "The remaining fixed nonclassical gate/control resource is therefore an **independent empirical datum relative to the present architecture**" (L1412–1414).

"Necessary machinery exists" (C41) therefore reads an available-to-represent statement as an available-to-derive one.

### 1.2 DS.3 — the finite-horizon equivalence

**Corpus statements.**
- Main §3.4, L526–530: "**Theorem (finite-horizon stochastic–reversible–unitary equivalence).** Fix a finite visible alphabet and a finite accessible horizon K. The following three classes of finite-horizon observable law P(x₀,…,x_K) coincide: (S) … (D) … (Q_fb)". Kernel names are cited at L530.
- Main also states it in the abstract (L16–20) and the conclusion (L746–750).
- ROADMAP L38–42: the "Programme interpretation boundary".

**Lean (Equivalence.lean)** [K: OIBridge.lean:58; census family "current", anchored in Main].
- `finite_horizon_equivalence {K : ℕ} (P : Traj V K → ℝ) : (Stochastic P ↔ RevRealizable P) ∧ (RevRealizable P ↔ QfbRealizable P) ∧ (QfbRealizable P ↔ Stochastic P)` (:459–465). Hypotheses: `[Fintype V] [DecidableEq V]` and a horizon K, nothing else.
- `S_imp_D` (:419), a clock-and-record carrier padded to a permutation.
- `D_imp_Qfb` (:294–342): U = permutation matrix of the inverse step, with the initial law kept diagonal.
- `Qfb_imp_S` (:245).
- The class Q_fb is defined (:190–217) by `QfbReal.chain` (:209–210), "The record of a projective fixed-basis measurement at EVERY step, with collapse" (:207–208).

**Status:** [K] for the stated hypotheses and conclusion.

**The paraphrase (C33)** is accurate. It states the S ⇒ D and S ⇒ Q_fb directions of what is a three-way equivalence. The received sentence lacks its expression. The corpus's display is S ⟺ D ⟺ Q_fb (Main L18, L748), but what the input originally contained is not recoverable from the received text.

**The two qualifications.**
- "Universal, including classical stochastic processes" (C34) is stated in the corpus:
  - Main L20: "it is also universal, so representability alone does not distinguish the memory-bearing sector from an ordinary Markov process";
  - Main L534: "universal: Markov and memory-bearing laws alike lie in Q_fb";
  - Equivalence.lean:20–23: "its classes include Markov laws".
- "Does not by itself force interference or select a particular underlying phase mechanism" (C35) is also stated:
  - Main L750: "The representation statement is universal; it is not the selector";
  - Main L534: "does not by itself prove that all coherent preparations, noncommuting interventions, and composites are represented …";
  - Main L622: representability does not select the relating evolution;
  - phase-source audit L49–51 and L77/L261 (P6 "representation (D2)");
  - ROADMAP L44–49.

The corpus supports something stronger than the input says. The representation the certified theorem *constructs* for any law is a permutation unitary acting on a diagonal prior, read with collapse at every step. So no cross term of the form conj(c_a)c_b with a ≠ b ever enters. I ran the kernel's two constructions on the double-slit law (horizon 1, alphabet {src,0,1,2,3}, P(src,x) = (1/2, 1/4, 0, 1/4)). The carrier step is a permutation of 250 states, and the Born chain law equals P for weights |U|^p with p = 1, 2, 3 [X ds7_models B9]. The quantum two-slit representation of the same law has the cross term 1/4 at x = 0 (CC-B9). The exponent is not selected (Main L20, L534).

### 1.3 DS.4 — the three levels, against the claim/evidence boundary (AGENTS.md L45–51)

**Level 1 (C4), "already established".**
- The theorem is [K] and universal over finite-horizon laws; no finite-test-to-universal step is involved.
- The input drops "fixed-basis" from the ROADMAP's own sentence (L39–41). That widens a fixed-basis statement into an apparently general Hilbert-space representation. The kernel class is collapse-at-every-step fixed-basis readout (Equivalence.lean:207–214), and Main L534 excludes coherent preparations, noncommuting interventions and composites from what it proves.
- "Your framework gives" reads like a framework-specific derivation. The representation exists for every finite law, quantum or not (Main L20), so it is available rather than derived from OI-specific structure.
- Verdict: ACCURATE WITH CORRECTION.

**Level 2 (C5), "already proposed".**
- The status matches Main L660, where the account sits under "Interpretive Consequences", and ROADMAP L1442–1447.
- The mechanism matches Explainer L568 and Main L750 (history readback).
- No boundary crossing. The input does not inherit the corpus's stronger wording at Explainer L568 ("The mystery dissolves not into another postulate but into a derivation"), which is not supported at L (§1.7).
- Verdict: ACCURATE.

**Level 3 (C6), "not yet established".**
- Relative to the stated architecture the corpus has already settled the question negatively in parts:
  - every finite law, including non-quantum ones, is realized by incomplete access to a reversible system [K `S_imp_D`];
  - "finite reversible read-write dynamics, even with genuine hidden-memory and readback behavior, does not itself generate quantum state mixing", with the phases entering "as a stated intervention principle rather than a consequence" (Main L568; [K] `readWriteSourced_not_qm` ReadWriteControl.lean:174–176);
  - phases and fixed nonclassical control are INDEPENDENT of the stated architecture (ROADMAP L1399–1414).
- Scope: the present architecture, not every extension (ROADMAP L1414 "This does not say an extended architecture cannot source it").
- Verdict: UNDERSTATED.

### 1.4 DS.6 — interpretation

**What the corpus asserts, and at what status.**
- Main L664 asserts the single-slit passage flatly, under the heading "Interpretive Consequences" (L660).
- Substratum.md:412 repeats it under "6.3 The measurement problem", "On the structural reading".
- Explainer.md:568 has "The particle goes through one slit". Explainer.md:574 has "the substratum holds exactly one configuration at every moment".

**What proves it: nothing at L.**
- The substratum's definiteness is a posit (Main L706, the posit ledger).
- That the slit passage is a function of the substratum configuration is a further, unproved identification.

**The observable-law equivalence is silent on paths.** It quantifies over visible laws only (Equivalence.lean:147–217). The same screen law is realized exactly by:
- a model with a definite hidden path variable (CL1, [X ds7_models B2]);
- the certified clock-and-record carrier, which has no path variable at all ([K] `S_imp_D`; [X B9]).

So the input's qualification (C31) is accurate.

**Two corrections to the input's reading of §4.1 (C26–C28).**
- In Main the arrangement and the detector are visible-sector (L662, L664). Record suppression in Main's account therefore comes from a coupling to visible degrees of freedom, not to the inaccessible sector. The hidden sector enters only Explainer's account of the fringes themselves (L568: "the hidden sector includes the field configuration near both slits").
- The substratum update φ is one fixed bijection. Arrangements are initial or boundary conditions: Substratum.md:414; Main L560, "One law, initial conditions vary".

### 1.5 DS.8 — what full equivalence would add (C47–C55)

**The corpus's operational equivalence is conditional.** It is OI⁺ ⟺ exact finite endomorphic operational QM (Main L564–566). The kernel results are `carrier_general_oiPlus` (CarrierGeneralOIPlus.lean:213), `oiPlus_iff_qm` (:207) and `oiPlus_independence` (:230) [K; root imports OIBridge.lean:138–139]. The typed form `typed_determined_iff` (Main L568) removes the endomorphic qualifier. Main L568 is explicit: "This is a characterization of a quantum-complete extension of OI, not a claim that bare OI entails the added principles". The K row (ROADMAP L68, L973–974) adds that these characterizations are "stated over complex matrix carriers, so the quantum kinematics is in its premises".

**C47 is ACCURATE WITH CORRECTION.** The theorem the input asks for exists in conditional form. The input speaks as though it did not.

**C48 is ACCURATE WITH CORRECTION.** An operational equivalence fixes the Born form. A double-slit pattern also needs the propagation, that is the relative evolution, and its phases.
- The corpus records that the visible family does not fix the relative evolution: P0 OPEN, ROADMAP L63; Main L622.
- It also records that the stated architecture does not source the relative phase: ROADMAP L1399.

**C49 is ACCURATE.** Main L562: "an operational realization theorem, not a uniqueness theorem: the same reversible machinery can realize non-quantum finite instrument families"; see also Main L22.

**C50 is ACCURATE WITH CORRECTION.** It matches the open obligations: K∞ unsourced (ROADMAP L1007–1009), physical C4 (L66), the stochastic observer interface (L918–931). Its "requires" is methodological; the corpus records these as open, not as proved necessary conditions.

**C53 is INACCURATE as phrased.** The four ingredients it names realize non-quantum two-slit laws [X ds7_models CC-B6]. They do so even with a C4 memory witness [X B8]. Every finite law is realized by them [K `S_imp_D`]. Read-write dynamics with hidden memory does not generate state mixing (Main L568 [K]). So "must produce that equation" fails for those ingredients alone.

**C54 holds only as a conditional.** With named additional principles the result would be CONDITIONAL in amendment 2's sense, and each principle would face the restatement test (§3(d)).

### 1.6 Remaining claims (DS.1)

Anchors are in the verdict table. Points the table compresses:
- **C12 and C14** are refined by §2: partial records, and mixed detectors with D = 0 and V = 0.
- **C22:** the formula contains only the record overlap; nobody's access enters it.
- **C32:** the omitted results are the phase-source finding and Main L568, both negative for the target. Also omitted: the gluing theorem's non-uniqueness (Main L562), the Born-exponent frontier (Main L20, L534) and the landed record gate (CompositeDimension.lean:1222).
- **C44:** R1–R3 are necessary for the target but met exactly by CL1. The target's discriminating content therefore rests entirely on its unformalized non-insertion clause.

### 1.7 Corpus markers found on the way (record-only; assumption-watch; nothing edited)

1. Explainer.md:568 calls its double-slit account "a derivation". Against it: ROADMAP L1442–1447 (no dedicated theorem), and Main L568, where the phases are "a stated intervention principle rather than a consequence".
2. Methodology.md:401 cites "the double-slit treatment of Main §3.4" as "the worked instance". The treatment is at Main §4.1 (L664) and is one interpretive paragraph with no computation.
3. ROADMAP L1442–1447 classes the benchmark as packaging, "not a dependency gap". That holds only for a benchmark whose premises X already contain what L1392–1414 records as INDEPENDENT of the stated architecture, or OI⁺'s added principles. With X equal to the stated architecture the formula is not implied (§1.5, C53).
4. Main L664 speaks of the detector "eliminating the interference terms". In the representation the certified equivalence constructs there are no interference terms (§1.2). The terms belong to a coherent representation the equivalence does not select.

## 2. Physics (DS.5)

All results below are [X] in `ds5_physics.py`: 27 checks, 7/7 blocks green, run 2; replay byte-identical. Symbols are exact (sympy, Rationals, √2). Inner products are conjugate-linear in the first slot.

**Formula 1.** |a+b|² = |a|²+|b|²+2Re(a*b) holds for symbolic complex a, b (F1). The cross term is not identically zero (CC-F1a: 2 at a = b = 1), and the sign-flipped form fails (CC-F1b).

**Formula 2.** The model:
- the path branches L, R carry ψ_L(x), ψ_R(x), which absorb the source's splitting amplitudes and the propagation to screen position x;
- the record is a path-conditioned map on a detector space that leaves the propagation unchanged, so the joint vector at x is ψ_L(x)d_L + ψ_R(x)d_R;
- the detector is not read.

Then, identically for arbitrary d_L, d_R (F2-general):

P(x) = |ψ_L|²‖d_L‖² + |ψ_R|²‖d_R‖² + 2Re(ψ_L*ψ_R⟨d_L|d_R⟩).

The input's formula differs from P by exactly |ψ_L|²(‖d_L‖²−1) + |ψ_R|²(‖d_R‖²−1) (F2-norm). It holds iff both detector states are normalized, which a unitary record on a normalized initial state guarantees. Exact instance (F2-unitary): U_L = 1, U_R = [[3i/5, −4i/5],[4/5, 3/5]], d₀ = (1,0), giving γ = 3i/5. On the 4-point screen ψ_L = 1/(2√2), ψ_R = iˣ/(2√2), P = (1/4, 1/10, 1/4, 2/5) = formula, and the sum is 1.

**The assumptions formula 2 needs.** (a)–(d) are each shown load-bearing by a countercontrol that fails exactly when the assumption is dropped; (e) has no countercontrol, because its failure is covered by the mixed-detector generalization F3 below:
- (a) normalized detector states: CC-F2a, unnormalized d_L = (1,1) misses by 1/8;
- (b) the conjugation order ⟨d_L|d_R⟩, not ⟨d_R|d_L⟩: CC-F2b, misses by 3/10;
- (c) a record that does not disturb the propagation: CC-F2c, a kick ψ_R(x) → (−1)ˣψ_R(x) breaks it;
- (d) the detector left unread: CC-F2d, the pattern conditioned on a detector outcome differs;
- (e) a pure detector state.

For a mixed detector ρ₀ the exact identity (F3) is

P = |ψ_L|²tr(U_Lρ₀U_L†) + |ψ_R|²tr(U_Rρ₀U_R†) + 2Re(ψ_L*ψ_R γ), with γ = tr(U_L†U_Rρ₀).

This equals ⟨U_Ld₀|U_Rd₀⟩ for ρ₀ = d₀d₀†. The screen amplitudes must be the same functions in every arrangement. In standard QM they come from free propagation; nothing at L supplies them in OI (§3(a)).

**Limiting cases (F4).**
- Identical normalized records give formula 1 exactly; the difference is 2Re(ψ_L*ψ_R)(‖u‖²−1).
- Orthogonal records leave cross term 0.
- Records equal up to a phase (d_R = i d_L) give |γ| = 1: full visibility with shifted fringes.

The input's statements C20 and C21 are accurate. C21 also holds for mixed detectors with orthogonal supports. [W] There each pair of eigen-components has zero overlap, so γ = Σ_k p_k⟨d_L^k|d_R^k⟩ = 0.

**Visibility, re-derived.** Write aL = |ψ_L|, aR = |ψ_R|, g = |γ|, and let the relative phase of ψ_L*ψ_Rγ sweep a full period across a fringe [W: the definition of fringe visibility]. Then Pmax/min = aL² + aR² ± 2aL·aR·g, and

V = (Pmax−Pmin)/(Pmax+Pmin) = 2aL·aR·g/(aL²+aR²)   (F5).

So V = V₀|γ|, and V = |γ| only at balanced amplitudes. CC-F5: aL = 1, aR = 2, g = 1 gives V = 4/5.

**Distinguishability, re-derived.** For arbitrary a, b ∈ ℂ², the characteristic polynomial of aa†−bb† is

t² − (‖a‖²−‖b‖²)t − (‖a‖²‖b‖²−|⟨a|b⟩|²),

and ‖a‖²‖b‖²−|⟨a|b⟩|² = |a₀b₁−a₁b₀|² (F6, Lagrange). For unit records the eigenvalues are ±√(1−|γ|²). [W] The trace norm is the sum of the absolute eigenvalues; in higher dimension the operator has rank ≤ 2 on span{a,b}. Hence D := ½‖ρ_L−ρ_R‖₁ = √(1−|γ|²), and at balanced amplitudes V² + D² = 1.

Operational reading [W]: max over 0 ≤ E ≤ 1 of tr(E(ρ_L−ρ_R)) is the sum of the positive eigenvalues, so the best single-shot discrimination probability is (1+D)/2.

CC-F6, purity is load-bearing: ρ₀ = 1/2, U_L = 1, U_R = X gives γ = 0 (V = 0), while the detector's two conditional states are equal (D = 0). The which-path information then sits in the detector's correlations with its own purification. ds7_structure S2 shows the same at n = 0: path coherence × n₁ = 0.

**The eraser (F7).** For the perfect record d_L = (1,0), d_R = (0,1), reading the detector in e± = (1,±1)/√2 gives P(x,±) = ½|ψ_L ± ψ_R|². These are fringes and antifringes summing to the fringe-free |ψ_L|²+|ψ_R|². In the record basis the two patterns are |ψ_L|² and |ψ_R|². CC-F7: P(0|+) = 1/2 against the fringe-free 1/4. Run 1 compared the joint probability instead of the conditional one; that harness error is recorded in §6.

## 3. The proposed target (DS.7)

**(a) Well-posedness.**

| object or premise the target needs | status at L |
|---|---|
| an observer embedded in a finite deterministic reversible system (S, φ, V) | certified as a class: `RevReal` (Equivalence.lean:150–183) [K]; the stated access is `permClass`, ones-fixing (PhaseSource.lean:79) [K] |
| the framework's physical substratum | present: ROADMAP L65 records the packaged K = 6 link-coupled rule with A1–A5 proved of it (kernel names not re-checked here); its identification with the physical substratum is that row's named hypothesis (CONDITIONAL) |
| the observation map and ensemble (Obs, μ) defining the observed law | **absent / OPEN**: ROADMAP L918–931; negative evidence `ensemble_underdetermined` (StochasticInterface.lean:118), `waveSubstratum_stochastic_interface_gap` (:191) [K] |
| "two controllable paths": opening and closing as settings | present for classical action-labelled controls (Main L536, L544–562); the gluing realization is in Main, kernel status not established here |
| a controllable relative phase, if "controllable" includes it | not sourced by the stated access: **INDEPENDENT** (ROADMAP L1399; `onesFixing_not_phasesAvailable` PhaseSource.lean:52, `permTheory_not_phasesAvailable_onesFixing` :104) [K]; enters only "as a stated intervention principle" (Main L568) |
| "a physically modeled detector": a second system and a correlating coupling | no OI-native pair system at L (INTEGRATION-REVIEW L119; K2 OPEN, ROADMAP L1001–1006). The ambient carrier W 3 with `cnot`, `prodState`, `phiW` is certified [K] (CompositeDimension.lean:97–1246) and encodes local tomography by its typing (:95–96) |
| a detector readout complementary to the record (any eraser variant) | not supplied by the stated access: such a readout needs a non-ones-fixing unitary [W over K: InstrumentRealization.lean:398 + PhaseSource.lean:79; X ds7_structure S6]; fixed nonclassical control is "an independent empirical datum relative to the present architecture" (ROADMAP L1412–1414) |
| the quadratic Born exponent | part of the definition of Q_fb, not selected (Main L20, L282, L534): frontier |
| the screen amplitudes (the propagation) | the relative evolution is not fixed by OI (P0 OPEN, ROADMAP L63; Main L622) |
| "without … inserting the desired detection probabilities" | **absent**: no formal non-insertion criterion anywhere. The corpus's realization theorems are existence results that take the law as input (`S_imp_D`; the gluing theorem's density register, Main L544–558) |

So the target is well-posed only relative to a fixed construction that L does not provide.

**(b) Discrimination.** Can R1–R3 be met by models carrying neither OI content nor quantum amplitudes? **Yes.** Exact finite instance CL1 [X ds7_models], on the 4-point screen of §2:
- **The model.** One reversible map φ = φ₃∘φ₂∘φ₁ on 5184 states. Its settings are the open slits and the detector coupling (off, half, on). The hidden variables are uniform. The particle takes a definite path. The record d ← d + p·rec. The landing table is the both-open table iff both slits are open and no record was made. Each step and φ are bijections, checked exhaustively (B1).
- **R1.** P(x|LR,off) = (1/2,1/4,0,1/4) = Q_LR[1]; the single-slit laws are uniform = Q_L = Q_R (B2). The control: Q_LR[1] satisfies the quantum two-path bound.
- **R2.** P(x|LR,half) = (3/8,1/4,1/8,1/4) = Q_LR[1/2] and P(x|LR,on) = uniform = Q_LR[0], exactly. The amount is derived in the model: V = 1 − r, with r the registration probability (B3).
- **R3.** One map; settings are initial conditions (B4).
- **No OI content.** CL1 has no visible memory: all histories before the landing step coincide, so C4 fails. Main L80 defines C4 as two histories with the same current state inducing different next-step laws. CL1 also has no amplitudes.
- **Countercontrols.** CL0 has the same architecture with a non-quantum both-open table. Its law (1,0,0,0) violates the quantum bound at x = 0 (CC-B6). CLfree has a perfect classical record (D = 1) that does not disturb the landing. It keeps V = 1 (CC-B7), so suppression is not implied by having a record.
- **Complementarity.** CL1 meets R1–R3 and has V² + D² = 1/2 at k = half (B5). The quantum pure-record equality V² + D² = 1 therefore discriminates CL1. A classical model can still be tuned to any (V, D), so that equality alone is fit-able by insertion.

**C4 neither necessary nor sufficient (on these instances).** CL0m carries a C4 witness: P(x | t=0,*) = (1,0,0,0) differs from P(x | t=1,*) = (1/2,0,1/2,0). It also has a C1 witness, and its screen marginal (3/4,0,1/4,0) violates the quantum bound (B8). Its realization by a reversible system is `S_imp_D` [K]. C1 and C3 follow from C4 in a faithful realization (Main L72, L78). So on these instances C4 is neither necessary (CL1) nor sufficient (CL0m) for R1–R3 [X].

**The further conditions that would make the target hard to vary** (AGENTS.md L23–35, L53–55):
- **H1, fixed construction (the decisive one).** The dynamics φ, the partition, (Obs, μ), the encoding of source, slits, detector and screen, and the record coupling are the framework's own construction. They are fixed and hashed before any double-slit quantity is computed, and nothing is fitted to the statistics. CL1, CL0 and CLfree are surrogates and fail H1 by provenance.
- **H2, cross-arrangement prediction.** The both-open law follows from the single-slit laws plus a phase function derived from the construction (fringe spacing), not fitted.
- **H3, complementarity over a detector family.** The family is parametrized independently of the screen. V = V₀|γ| with |γ|² + D² = 1 for pure records and ≤ 1 in general, with D computed from the detector's own conditional states. CL1 fails it (B5); CLfree fails it.
- **H4, eraser.** Conditioning on a readout complementary to the record restores fringes with the visibility fixed by the same γ, which rejects the separable record ω_B (ds7_structure S3). Where a relative phase is controllable, CHSH reaches 2√2 at the stated settings (S4). Under the framework's own Bell accounting that requires ontic parameter dependence (Main L22, §3.3).
- **H5, an independent postdiction.** No third-order interference: I₃ = 0 for three slits, from the same rule. I₃(2) ≡ 0 symbolically, while I₃(4) = 36 at a = b = c = 1 (B10). The exponent is not selected by the equivalence (Main L534). Empirical bounds are cited at Structure.md:1312 [L, unverified].

**(c) Relation to S2/S3/K2: the decisive structural check** [X ds7_structure, on the landed W 3 objects transcribed from CompositeDimension.lean; dictionary verified in S0, with countercontrols]:
1. **The record is the landed native gate applied to a product state.** cnot(prodState xplus z3) = phiW (S1), the kernel's `cnot_prodState_xplus_z3` (:1222) [K]. A detector prepared on the gate's flip axis records nothing (CC-S1).
2. **On the path alone, the unread record is a single-system dephasing,** but its strength is a second-system quantity. The path marginal of cnot(prodState x n) is (1, n₁x₁, n₁x₂, x₃) identically (S2), and n₁ = tr(Xρ_n) is the detector's coherence factor γ (S2-gamma). Two detector states give different path marginals for the same path state (S2-two-system); without the gate the marginal is independent of n (CC-S2). R1 is single-system. R2's *observable* is a single-system marginal, but its *derived amount* needs the detector, the correlating gate and the marginal map, which is pairing with the unit effect in a locally tomographic carrier.
3. **The eraser is a pair statement, and it is the only discriminating one.** The separable classical record ω_B = ½(prodState z3 z3 + prodState −z3 −z3) has the same path marginal, detector marginal and Z⊗Z statistics as phiW (S3-a). So the unread-detector pattern and the which-path statistics are identical. Conditioned on the X-readout, phiW gives path vectors ½(1,±1,0,0) (fringes and antifringes), while ω_B gives ½(1,0,0,0) (S3-b). The two states differ exactly in the X⊗X and Y⊗Y entries (S3-c); record-basis readouts cannot separate them (CC-S3).
4. **With path phase control the setting is a Bell scenario:** S(phiW) = 2√2 against a local deterministic maximum of 2 (S4); S(ω_B) = S(prodState xplus z3) = 0.
5. **A detector family containing both textbook markings leaves K_gen.** The phase-kick record CZ(|+⟩|+⟩) equals actT R_H phiW, the landed probe's T_ψ (S5-table; kt4_prem1_probe.py:560–562). The witness F = ½ − |ψ⟩⟨ψ| is ≥ 0 on every product and every cnot image of a product of ball points (exact SOS identities, S5-a/b), so ≥ 0 on K_gen = SEP + cnot SEP [W]. But tr(Fψψ†) = −1/2 (S5-c), and the path statistics equal those of the cnot record (S5-stats). Countercontrol: tr(F phiW) = 1/2 ≥ 0. For one fixed coupling, that coupling can serve as the native gate. For a family in which two couplings differ by a local rotation of the detector, the common state space needs IE1 at R_H, or frame covariance of the native gate. Frame covariance is a flagged route in stage 2 (PROTOCOL-STAGE2.md L82–87).

**Decision on the input's claims.**
- "Narrower than completing K2 for every composite system" is inaccurate. K2 at L is the two-copy d = 3 composite, and the detector setting is an instance of it (item 1).
- "Potentially more accessible" holds only for one fixed coupling read in product form, inside stage-1's K_gen, and inherits that construction's premises.
- "Independently of the S2/S3 work" is inaccurate:
  - the record presupposes S2's objects (products in the pair cone; the gate on a product — exactly `bell_mem`'s (BS) instance, pt/inputs/fourcopy/FourCopyLocal.lean:266 [D]; valid product effects);
  - the discriminating eraser needs a complementary readout that the stated access does not supply (§3(a));
  - general detectors need IE1, which the stage-1 route obtains from FCC/S3 through the [D] theorem.

**(d) A preregistrable decision rule for a future probe of the target.**
- **Freeze before any computation:**
  - (S, φ) named from the corpus, with its sourcing status;
  - (Obs, μ) with status;
  - the encodings of source, slits, detector family (parameter n independent of the screen) and screen;
  - the horizon;
  - which resources enter as named assumptions (phase intervention, mixer, composite), with hashes.
- **Compute exactly from the frozen construction:**
  - P_LR, P_L, P_R;
  - P_rec(·|n) and D(n) from the detector's own conditional states;
  - eraser conditionals for each readout;
  - CHSH where phase control is frozen in;
  - the three-slit I₃.
- **Controls (any failure voids the verdict):**
  - exact replay;
  - bijectivity of φ on the frozen carrier (exhaustive);
  - normalization of every law;
  - closing a slit removes exactly its contribution;
  - a §A.21 symmetry control (exchanging the slit labels mirrors P_LR);
  - S ⟺ D ⟺ Q_fb membership of every computed law.
- **Countercontrols (the rule must reject them):**
  - CL1, rejected by H1 provenance;
  - CLfree, rejected by H3;
  - ω_B, rejected by H4;
  - CL0, rejected by H2.
- **Criteria:** H2–H5 above, with all comparisons exact.
- **Outcome relative to L:**
  - **DERIVED** iff the criteria hold and every premise used is [K] at L. As L stands this first needs new kernel objects: a double-slit arrangement in the physical substratum, (Obs, μ), and an OI-native pair system.
  - **CONDITIONAL** iff the criteria hold from [K] plus named added principles, each assessed as independently motivated, with its strength relative to the target stated. A principle whose content is the target (for example "path and detector compose as a quantum tensor product with Born readout", or "visibility equals the record overlap") is a restatement and makes the target **UNRESOLVED**.
  - **INDEPENDENT** iff an exact countermodel satisfies every certified premise bearing on the frozen construction (the frozen φ class, the access class, the C1–C4 diagnostics) while a criterion fails, with each premise listed and checked.
  - **Route refuted** for a model of the probe's own route premises only.
  - **UNRESOLVED** otherwise, with the gap stated.

## 4. Relation to S2/S3/K2 and the stage-1 findings

| part of the setting | systems / operation | at L | stage-1 object (audited) | consequence |
|---|---|---|---|---|
| R1: interference without a detector | one system (path) and screen effects | the law has a Q_fb representation [K], universal; the qubit ball and its effects are K-programme data, with K∞ seams unsourced (ROADMAP L1007–1033) | none: single-system | independent of S2/S3, but not new, and not specific to OI |
| R2: suppression by a record | path, detector and the native gate on a product | `cnot`, `prodState`, `phiW`, `cnot_prodState_mem_maxCone` (:1152) [K] in W 3 (LT encoded :95–96) | `bell_mem` (BS) instance [D]; `hadm` (a) products in K_p; `hgate` at products, INDEPENDENT of L (AUDIT-B L39–44, verdict L81–93); K_gen (AUDIT-A, A-i DERIVED for the constructed systems) | inside K_gen for one fixed coupling; presupposes S2's objects and K2's local tomography |
| R2's derived amount | needs the detector's state n | S2-gamma [X] | none | two-system quantity |
| eraser (detector read two ways) | pair correlation table; product effects | phiW ∈ maxCone [K] `phiW_mem_jointStates` :1246 | `hadm` (b) K ⊆ maxCone; product-test cone (AUDIT-D T3) | the only discriminating part [X S3]; the complementary readout is not in the stated access (§3(a)) |
| detector family with cnot and phase-kick couplings | local rotation of the detector token | T_ψ ∉ K_gen [X S5]; landed probe M_cl | IE1, the K_gen → Q3 gap (INTEGRATION-REVIEW L48–57), supplied on the KT(4) route by FCC (S3) through the [D] theorem; frame covariance flagged | S3 territory |
| path phase control and two readouts | Bell scenario | none | H-Bell (ROADMAP L67, L953–966); INTEGRATION-REVIEW L221 "K2 does not discharge it" | beyond K2 |

**Stage-1 findings preserved, not generalized:**
- C's narrowed tree obstruction and the audit corrections are untouched; DS does not use them.
- Every INDEPENDENT in stage 1 is relative to a base with no pair system. Accordingly DS labels the framework-specific target UNRESOLVED, not INDEPENDENT.

## 5. What is not claimed

1. No claim that the framework cannot derive the double slit in any extension. The negative results quoted are relative to the stated architecture at L (ROADMAP L1414). The route refutations hold for the input's generic premises only.
2. INDEPENDENT is not claimed for any target. CL0 and CL0m satisfy the route's premises, but they were not checked against every certified premise of the framework's physical substratum (A1–A6, the packaged rule).
3. CL1, CL0, CL0m and CLfree are surrogate models built to test the input's criteria, not physics proposals.
4. The [X] results hold for the stated instances:
   - the 4-point screen;
   - real or Gaussian-rational γ;
   - the W 3 tables, symbolic where stated;
   - CHSH at the stated settings;
   - I₃(4) at one point.
   The [W] steps are marked: trace norm, visibility definition, mixed-support orthogonality, K_gen convexity, the ones-fixing corollary for the mixer.
5. Nothing here is kernel-checked. No Lean was written or built. [K] labels rest on the build route at L, not on a local rebuild.
6. The comparison with stage-1 objects uses audited results only (`pt/audit/{A,B,C,D}`, INTEGRATION-REVIEW). Stage-2 work (S2, S3) was not read.
7. Literature (Englert duality, Helstrom, Sorkin, Sinha) is named for orientation only, [L, unverified]. Every relation used in a verdict is re-derived in §2.
8. No corpus file was edited. The §1.7 markers are record-only.
9. Correctness bands are unchanged: this is consistency-axis review (AGENTS.md §A.23).

## 6. Evidence log

Each script ran as `python3 -I -B <script>` from `pt/DS/`; stdout went to `.out`, stderr to `.err` with `exit=N` appended. Each was replayed into `.replay.out` and `.replay.err`, and `cmp` reported both byte-identical. Decision rules sit in each header, fixed before the first run; pre-run edits are logged in NOTES.md.

| script | sha256 (script) | sha256 (.out) | checks | runs | replay |
|---|---|---|---|---|---|
| ds5_physics.py | `245a24dd38bc9241f5a3c0dc63e88b26a7b74d34f9e2960e9cf0f290eafb94d3` | `2de948fb1076bb8a09323c44534a1817c35224e2f8be65bdecd5bad5face2bcb` | 27/27 PASS, 7/7 blocks | 2 (run 1 kept) | identical |
| ds7_structure.py | `b14a95e0e1d470029c6f4ad19cc2bd6be864c40b020e9699c7407b8f87eee371` | `9c582278aa92d351f086d11100f3246355e77c6fb7ce8ddf72856a50bf05a04e` | 24/24 PASS, 7/7 blocks | 1 | identical |
| ds7_models.py | `8b03b2e6932e253dae96626ca36f6f2add8442ac8174c28bed3990374b1a475e` | `3005de6790f85371d10624eb3487de9858e3baaef35ad7dd675b9b88011adddf` | 19/19 PASS, 10/10 blocks | 1 | identical |

- Every `.err` and `.replay.err` is `exit=0`, sha256 `19eaf43821a7660ec323a87c8457bf74823beb296c39f5e01aa8a683aa50f061`.
- **Failed run kept.** `ds5_physics.run1.{py,out,err}`: script `3bdcd839788225de5733b30e85316f5545f93826d38ad4aea3a9854073102359`, out `ab4e9c3007bd873e43087c4b73ac00acf382187278b3e4caa31a47e50c5ec701`, err `19eaf438…`. 26/27 PASS. CC-F7 failed because of my own harness error: the code compared the joint P(0,+) where the frozen rule names the conditional pattern. The fix divides by P(+) and touches nothing else. The diff is in NOTES.md.
- No `__pycache__` was created (`-B`).

## 7. Integrity

**Start (2026-10-10T08:49:10Z; `pt/DS/.start_marker` written first into a freshly created, empty `pt/DS/`):**
- `sha256sum -c --quiet`: rc 0 on all four manifests:
  - `inputs.manifest.sha256` (41 lines);
  - `stage1.manifest.sha256` (209);
  - `inputs2.manifest.sha256` (3);
  - `inputs3.manifest.sha256` (1).
- Base HEAD `9f9f8257a980a1819fbbc1dc0019917cf8678626`; `git -C base status --porcelain` empty; no bytecode under `base/`.
- The five protocol hashes match.
- Two coordinator entries predated the marker and are recorded in it: `DS-LAUNCH-LOG.md` (read) and `auditS3-replay/` (excluded, not opened).

**End (2026-10-10T09:32:31Z), all start checks repeated:**
- The four manifests: rc 0, with the same line counts.
- Base HEAD `9f9f8257…`; status empty; no `__pycache__`, `.pyc` or `.pyo` under `base/`.
- The five protocol hashes are unchanged.
- No `__pycache__` in `pt/DS/`.

**Anomaly sweep.** Under `pt/`, excluding `pt/DS/`, `pt/audit/` and `pt/audit*-replay/`:
- No file is newer than `.start_marker` by mtime.
- No entry is newer by ctime (this catches renames and moves) except `pt/` itself.
- **Recorded observation, not an anomaly.**
  - `pt/` has mtime 09:14:01Z.
  - Its one new top-level entry is `auditS2-replay/`, created at 09:01:24Z. That is a coordinator directory the protocol excludes, and it was not opened.
  - The later directory-mtime change left no surviving entry outside the exclusions. It is consistent with a transient entry created and removed there.
  - Nothing was quarantined; `pt/DS/evidence/` was not needed.

**Hashes.** Every script and output hash in §6 was recomputed and matches. All seven `.err` files are `exit=0`, and all three replays are byte-identical.
