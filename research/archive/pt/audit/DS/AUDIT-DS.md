# Coordinator's audit of thread DS — review of the supplied double-slit analysis

Audited: `pt/DS/RESULT.md`, sha256 `26c33475983c5d389d0e14b803a01980b8659a9bf8eb192c9172490de03989c8`. `pt/DS/` holds 21 files and no subdirectory.

Protocol: `PROTOCOL-STAGE2-DS.md` (`086a4cb8…`). Input: `inputs3/DS-INPUT.md` (`ffb6eb75…`).

## Integrity
- **Coordinator's check, 09:35Z.**
  - The `inputs`, `stage1`, `inputs2` and `inputs3` manifests are OK.
  - Base HEAD is `9f9f8257…`; status is clean; there is no bytecode.
  - The five protocol files are unchanged.
  - Outside `pt/DS/`, `pt/audit/` and `pt/audit*-replay/`, no file is newer than DS's start marker.
- **The start marker** was written into a freshly created `pt/DS/`. The time inside it is 08:49:10Z; the file mtime is 08:49:42Z.
- **The observation DS recorded, accounted for.** DS found that `pt/` itself had mtime 09:14:01Z and no surviving new entry. That was me.
  - At about 09:12Z I wrote a draft of the stage-2 integration addendum into `pt/`.
  - At 09:14:01Z I moved it to `scratchpad/drafts/`, so that DS's end-of-run sweep, which does not exclude `pt/*.md`, would not meet it.
  - The file's content was my own draft, and DS never read it.
  - DS classified the event correctly: an observation, not an anomaly.
- **Hashes.** Every script and output hash in RESULT §6 matches the files.

## Replays
Run as `python3 -I -B` from `pt/auditDS-replay/`. All three reproduce stdout and `.err` byte for byte:
- `ds5_physics`: 27 checks;
- `ds7_structure`: 24;
- `ds7_models`: 19.

Afterwards the base status is empty and there is no bytecode. The kept failed run `ds5_physics.run1` (26/27, a harness error at CC-F7: joint where a conditional was meant) was not re-executed.

## Independent check (no thread code)
`indep_checkDS.py`: sha256 `de074180…`; output `1df40160…`; the replay is identical. **13/13 CONFIRMED** on the first run.

Sections P and F were drafted, and pre-run, before DS finished, with DS's outputs unread. That pre-run is `scratchpad/drafts/indep_checkDS_physics.*`, outside `pt/`, 6/6.

- **P1–P3.**
  - Both displayed formulas hold symbolically for complex amplitudes.
  - The general form carries `‖d_L‖²` and `‖d_R‖²`, so the input's form is the normalized case.
  - For pure records, visibility² + distinguishability² = 1, with D the trace distance.
- **F1, F2, F1c (new).** These are on the certified `cnot` table, symbolically for every product preparation.
  - After the record, the path's reduced Bloch vector is `(a₁b₁, a₂b₁, a₃)`: coherence is multiplied by `b₁`, and the populations are unchanged.
  - `b₁ = ⟨d₀|X|d₀⟩` is the overlap of the two record states `d₀` and `X d₀`.
  - So the textbook which-path law V = |⟨d_L|d_R⟩| for this record family is a computation on certified objects. It agrees with DS's S2 ("path coherence × n₁"), derived independently.
- **B1–B3.**
  - With real record overlap g, the quantum screen law is exactly the mixture `(1−g)Q[0] + gQ[1]` (symbolic). Any classical device that registers with probability r = 1 − g therefore reproduces requirements R1–R3. This is the one-line reason DS's CL1 succeeds.
  - The law (1,0,0,0) breaks the two-path bound 1/2.
  - A classical record has V² + D² = 1/2 at r = 1/2.
- **S1–S4.**
  - `phiW` and the separable record `ω_B` share both marginals and the Z⊗Z entry. They differ only in X⊗X and Y⊗Y, which only an eraser readout sees.
  - At my settings CHSH(`phiW`) = 2√2 and CHSH(`ω_B`) = √2 ≤ 2. DS reports 0 for `ω_B` at its own settings; both are ≤ 2.
  - The phase-kick record CZ|+⟩|+⟩ equals the landed `T_ψ`, and S2's K_gen-positive witness F is negative on it.
  - The balanced mixer moves the all-ones ray.

**Citations spot-checked at L**, every one resolving as DS quotes it:
- `papers/Main.md`:
  - L660, L662 (`slits, detectors — are all visible-sector objects`), L664;
  - L20, L534, L562, L564, L568 (`finite reversible read-write dynamics, even with genuine hidden-memory and readback behavior, does not itself generate quantum state mixing`; phases `as a stated intervention principle rather than a consequence`);
  - L750.
- `verification/ROADMAP.md`:
  - L38–42 (`exact fixed-basis Hilbert-space, unitary and Born-rule representation`, so the input's Level 1 is this sentence with "fixed-basis" dropped);
  - L973–974;
  - L1001–1006 (K2 is the two-copy `d = 3` composite);
  - L1392–1414 (phases and nonclassical control: INDEPENDENT);
  - L1422;
  - L1442–1447.
- **Lean:**
  - `readWriteSourced_not_qm` (ReadWriteControl.lean:174);
  - `oiPlus_iff_qm`, `carrier_general_oiPlus` and `oiPlus_independence` (CarrierGeneralOIPlus.lean:207, :213, :230);
  - `S_imp_D` and `finite_horizon_equivalence` (Equivalence.lean:419, :459), with the collapse-at-every-step class at :207;
  - `onesFixing_not_phasesAvailable`, `permClass_onesFixing` and `permTheory_not_phasesAvailable_onesFixing` (PhaseSource.lean:52, :79, :104);
  - `instAvail_unitary_fixes_ones` (InstrumentRealization.lean:398);
  - `ensemble_underdetermined` (StochasticInterface.lean:118).

  All of these modules are root imports of `OIBridge.lean`, at lines 58, 139, 146, 177, 179 and 192. `AncillaInterference` is at 114.
- **Design:** `bell_mem` (FourCopyLocal.lean:266) [D].
- **Corpus markers:**
  - `papers/Explainer.md:568` reads "The mystery dissolves not into another postulate but into a derivation";
  - `papers/Methodology.md:401` cites "the double-slit treatment of Main §3.4". The treatment is at §4.1, L664.

## Assessment
- **The verdict table is sound.** Every non-trivial verdict carries an anchor I could resolve.
- **The corrections with most weight for the owner:**
  - **C6, UNDERSTATED.** The corpus already records, relative to the stated architecture, that every finite law, non-quantum ones included, is realized by incomplete access to reversible dynamics [K]. Read-write dynamics does not generate state mixing [K]. The source of phases is INDEPENDENT. So "not yet established" is weaker than what is known: the stated architecture alone provably does not force the double-slit structure.
  - **C41, OVERSTATED.** "Necessary machinery exists" reads available-to-represent as available-to-derive.
  - **C53, INACCURATE.** The closing route is refuted by `S_imp_D` together with exact non-quantum two-slit laws.
  - **C45a and C46.** The target is not "narrower than K2 for every composite system", and not independent of S2/S3. The detector is a second system, and the record is the native gate applied to a product.
- **One refinement to C46.** The input says the target "could be investigated now, independently of the S2/S3 work".
  - The first half is accurate. R1, and R2 for the CNOT record family, are computable on certified objects now (my F1, F2; DS's S2).
  - Only "independently" is inaccurate.
  - Splitting the claim would leave every label unchanged.
- **Target labels.**
  - The framework-specific double-slit derivation is UNRESOLVED relative to L.
  - The generic route is refuted.
  - R1–R3 are non-discriminating.
  - Nothing is INDEPENDENT.

  This scoping is correct. L defines no double-slit arrangement, no observation map or ensemble, and no OI-native pair system in the physical substratum, so a valid countermodel to *every* certified premise bearing on the target cannot yet be stated.
- **DS's hard-to-vary criteria H1–H5 and its decision rule (§3(d))** are a sound basis for any future probe.
  - H1, a construction fixed and hashed before computing, is the decisive one.
  - The eraser criterion (H4) and the detector family (H3) put the target on the S2/S3 axis: the pair system, IE1 and Q3.
- **The §1.7 corpus markers** are record-only and verified above. They would be repository-hygiene items under AGENTS.md §A.25 and §A.30 for a future, owner-authorized change. Nothing was edited; the holds apply.

## Verdict for integration
- **The input is a useful orientation, and it rests on standard quantum mechanics.**
  - Its physics formulas are exact under stated assumptions.
  - Its definite-path caveat (C31) and its description/derivation distinction (C2) are accurate.
  - It misreads Main §4.1 in one place: Main places the apparatus in the visible sector (C26).
- **Its claims about the repository are partly overstated, and its strategic claim is wrong.**
  - A double-slit derivation is not a shortcut around K2 or S2/S3; it is an instance of them.
  - For a single CNOT-type record the textbook visibility law already follows from the certified pair data. That is a consistency-axis illustration, not a derivation from the substratum.
  - Any family of records richer than one coupling, any eraser and any Bell-type readout needs the composite state space S2 and S3 identify as missing.
- **Evidence levels.**
  - [K]: the cited landed theorems.
  - [D]: `bell_mem`.
  - [X]: DS's three scripts and my 13 checks, instance-scoped or symbolic as stated.
  - [W]: the trace-norm, visibility, convexity and ones-fixing steps.
  - [L, unverified]: Englert, Helstrom, Sorkin, named for orientation only.
- **Bands:** unchanged. This is consistency-axis review.
