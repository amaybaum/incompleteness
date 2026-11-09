# Independent review: OI-QM-APPROX-1 (#1216) unit 1, `APPROX-UNIT1.md` r1

**Reviewer:** a fresh, independent Claude Code subagent, 2026-11-09. Paper-only review. No git, repository
or GitHub write; no manuscript change. This review authorizes nothing (#1216 body, "Unit 1"; c.6741763726).

- **Under review:** `approx/APPROX-UNIT1.md`, sha256
  `310b907a7adcab8d81b32be104719e2d9d48934f9cb78c8011fc15e3e892151b` (verified), 547 lines, read in full.
  Its probes: `approx/probes/approx_generic_checks{,.r0,.r1}.{py,out}` (hashes in §8).
- **Sources.** `git fetch origin main` gives `cac5d264`; it differs from `fd539e15` only in `papers/SM.*`, so every
  cited Main, GR, Substratum, OIBridge and MECH-2/AP1 line is current. Read with `git show fd539e15:<path>`:
  Main:362, :480–:488, :520, :538–:606, :640; GR:250–:270; Substratum:131–133; MECH-2 `DESIGN.md` §0 and
  nodes 2–3; AP1 (`apparatus-1-20261107/DESIGN.md`) §4.2 (R1); the Lean statements cited (§3 below). #1216 body
  and all three comments (c.6741763726, c.6742051100, c.6742191828). #945 body and all five comments. Accepted
  inputs BRIDGE r5 (`78f1098e…`, verified) §5.1 and A868 r3a (`d97c4b6b…`, verified) §§4.1–4.3, J3.
- **Reviewer probes:** `approx/review/rv_frames.py`, `rv_routeC.py`, `rv_Er.py`, `rv_finiteb.py`, each importing
  nothing earlier, exact arithmetic, run `python3 -I -B` from `/tmp`; all four ALL PASS (§8).

## Verdict: REVISE

Three blockers, each with a short repair that this review supplies and checks. Most of the text holds: the line
remapping, the Level-A verdict and its scope, the "mechanism, not table" verdict with its skeptical note, NX-1 ⇒
FI-1, the route-C ε-robust obstruction, the Q4 answer and its drive scoping, the treatment of #945, and the
register-encoding "yes".

- **B1.** On route C, quantum compatibility is reported as failing. By the unit's own definition and the owner's,
  it holds. What fails is coverage of the target class. This error propagates to §5.1, to the independence
  witnesses and to the §0 item 6 headline.
- **B2.** The route-E_f "states yes" is false for R1, the frame that §1 names and that Lemma F is stated for. The
  computations behind it use Main:562's SIC frame, and D21's "assumed reading" that the two frames coincide is
  false.
- **B3.** The NX-1 relations are stated as proved, but two non-implications lack a theory-level witness: FI-1 ⇏
  NX-1, and "strictly weaker than layer-flow executability". Both are true, and witnesses are given below.

***

## 1. Line remapping (F0): confirmed

At `fd539e15`:
- the gluing theorem is Main:566, with clauses (1)–(5) at :568–:576, the Rounding Lemma at :578 and the proof at :580;
- the single-dynamics Corollary is at :582, the telescoping Lemma at :596, the uniform theorem at :598 and the density
  Corollary at :600;
- Main:556 is the Remark "what this equivalence does and does not say".

Main:578 ends: "the Corollary's estimate is not established for the simulator's Hermitian branches. A bound on the
classical-marginal rounding term at finite $b$ is open." Main:568 also states the finite-b law bound open. No
"negativity" ledger text remains (grep).

`git show 7c6ceaaa:papers/Main.md` and its parent still have the gluing theorem, Rounding Lemma, uniform theorem and
density Corollary at 544, 556, 576 and 578. `02009693` has them at 566, 578, 598 and 600. So the +22 shift happened
after `7c6ceaaa`, as F0 says, and #1216's :544/:576/:578/:556 are pre-shift numbers. *Nit N8:* c.6567863298 says
"moved the theorem from Main:556 to Main:566–:580 at `02009693`". The "+22" is the writer's inference. It is correct
and is now verified on `main` history, so cite it as such.

## 2. Q1 (Level A): confirmed, with two nits

- **A1.** The comb table meets Level A exactly. Main:482 states the theorem "for every action sequence", Main:486
  reproduces quantum instrument statistics, and Main:602 says "a fixed finite instrument family is realized exactly
  by the intervention dilation above, with a product prior carrying the quantum conditionals (Extension,
  response-table form)".
- **A2 and A3.** Gluing (Main:566–:580) meets Level A within $K(|O_{\max}|-1)/G$, in exact-ring arithmetic. The
  uniform theorem (Main:598) meets it within ε at fixed (d, m, K).
- **Scope and access.** The stated scope is correct: finite d, finitely many outcomes, declared K, a fixed initial
  state, and preparations as channels. The stated access is also correct: labels written to the visible record,
  outcome registers read, and the state held in hidden registers (Main:566, :582).
- **Finite b.** The bound is open, correctly cited to Main:568, :578, :580, :598 and :602 item 4.
- **Capacity.** The [A] estimate log₂|C_H| = O(K² m d⁴ log(K/ε)) follows from Main:576 and the volumetric |N| bound
  at :598.
- *N11.* A1's coverage of adaptive protocols is the writer's chain-rule reading [A], since Main:482 says "every
  action sequence". The reading is correct: the contexts (x_{≤k}, a_{≤k}) are distinct and the prior is a product.
  Label it [A]. The |C_H| formula quoted from Main:520 is the passive one. For the action-labelled comb, N counts the
  (x, a) contexts.

## 3. Q2 (table or mechanism): the verdict is fair; one scope nit

The skeptical reading (§A.31) was applied to the favourable claim. It does not overturn it.
- On a finite carrier every bijection is extensionally a table. In the exact ring, the carrier is indexed by
  V_reach(ρ₀, F, K), so the configuration set enumerates quantum branch states, and the stack holds the full
  history.
- The writer states both facts (§3.1 "Skeptical note") and moves the criterion to description: compression, and
  reuse on protocols not used to build the realization ("the construction never asks which protocol is running",
  Main:580).
- Under that criterion the construction encodes **the theory**, not **its predictions**. It loads states and Kraus
  data and computes predictions. The comb (A1) instead loads the predictions.
- "Mechanism, whose compression is quantum mechanics itself" is therefore accurate. So is "classical simulator of
  QM". Main:582 says "Quantum mechanics enters as the instrument data and as the state held in the hidden register
  … the construction uses no property of the substratum beyond finiteness and reversibility". Main:584 and :600 say
  the same machinery realizes non-quantum families.
- B-1's conclusion is sound and well sourced (Main:556 "representability alone is not the framework's
  discriminating content"; Main:602 "What remains is selection"): Level B as worded does not discriminate.
- **N9 (scope).** "At fixed (d, m, K, ε) it meets Level B's shape" should carry B-3 in the sentence itself.
  Composition is covered only by treating the composite as one system of dimension d_A d_B, built with the tensor
  rule (Main:574). The composite realization is not assembled from the components' realizations, and no statement
  relates A's own realization to the composite's A-marginal. "Shape" therefore holds for one fixed system, composites
  included as such a system. It does not hold for a compositional mechanism.
- *Harrigan–Spekkens.* The ψ-ontic, ψ-supplemented reading holds for pure preparations entered as channels from the
  fixed initial state: distinct ψ give distinct registers, and the seeds and stack supplement them. Precisely, the
  model stores an unnormalized density register ("ρ-ontic"). The citation, Found. Phys. 40, 125 (2010), matches the
  reviewer's recollection; it was not re-read.

## 4. NX-1 (§4.2): ⇒ FI-1 confirmed; the strictness claims need witnesses (B3); scope nits

**NX-1 ⇒ FI-1 (route C): confirmed by composing kernel lemmas.** Each was checked at `fd539e15`:

| Lemma | Location | Statement |
| --- | --- | --- |
| `realized_of_instAvail` | ImplementationLocality.lean:530 | every branch of an available family in `genTheory 𝓘 arch` is a finite sum of conjugations by 𝓘-operators on the same carrier |
| `IsMonomial` | SubstratumInterface.lean:75 | definition |
| `preservesDiag_conj_of_monomial` | SubstratumInterface.lean:126 | |
| `PreservesDiag` | DiagonalTheory.lean:68 | definition |
| `preservesDiag_sum` | DiagonalTheory.lean:84 | |
| `ConfigurationLevel`, `substratumClass_configurationLevel` | ManuscriptAxioms.lean:125, :129 | |
| `exists_nonMonomial_of_layerFlowExecutable` | ExecSource.lean:52 | |

The kernel proof of `exists_nonMonomial_of_layerFlowExecutable` is exactly this composition, applied to the gate flow
at t = ½ through `availExt 1`, on the carrier S × Fin 1. That carrier is FI-1's "level one" (BRIDGE r5 §5.1). The
writer's description is accurate.

*N3.* The step "the stated substratum with its access fails NX-1" also needs `obs_availExt_le_substratum`
(SubstratumInterfaceAudit.lean:837, used in ExecSource.lean:129): the observer theory lies in the substratum theory. It also needs the reading that a native
system-level procedure built with rule (f) is available at `availExt 1`. Cite both.

**B3. The strictness claims need theory-level witnesses.**
- *FI-1 ⇏ NX-1.* The witness K = |0⟩(⟨0|+⟨1|)/√2 shows only that one non-monomial operator preserves diagonals. A
  non-implication between properties of theories needs a theory in which FI-1 holds and NX-1 fails (§A.34, each
  direction separately). Two facts make one available:
  - an architecture needs closure under identity, product, contraction, ancilla projectors and ancilla blocks
    (`Architecture`, ImplementationLocality.lean:506–515; `ancBlock`, AncillaClosure.lean:457);
  - `InstAvail.op` requires Kᴴ K = 1 (ImplementationLocality.lean:271–272).

  **Counter-model:** the column-monomial class CM, the matrices with at most one nonzero entry in each column.
  - CM is an architecture.
  - It contains K, so FI-1 holds.
  - Every CM conjugation preserves diagonals, so by `realized_of_instAvail` and `preservesDiag_sum` every branch
    of `genTheory CM` preserves diagonals, and NX-1 fails.
  - The isometries in CM are exactly the monomial ones.

  Reviewer check C4 (rv_routeC.py) verifies this symbolically: all 64² products of 3×3 CM patterns, all 625 4×4
  patterns' ancilla blocks, conjugation of symbolic diagonals, the unitary ⇒ monomial step, and a Hadamard
  countercontrol. Replace the operator witness with this model ([A + G], kernel-definition-level).
- *"Strictly weaker than layer-flow executability"* has no argument in the text. One direction: executability ⇒ an
  available branch that does not preserve diagonals, by `hex 1 (1/2)` and `gateFlow_half_not_preservesDiag`
  (LiftAudit.lean:155). Strictness follows by composing existing kernel lemmas:
  - `polarizedTheory_swap_half_level_one` (C5Discovery.lean:325) makes the gate flow at t = ½ available at level one
    in `polarizedTheory (Fin 2)`;
  - `gateFlow_half_not_preservesDiag` shows that branch does not preserve diagonals;
  - `polarizedTheory_not_layerFlowExecutable` (PolarizationClosure.lean:395) shows the theory is not executable.

  Cite these three lemmas, or drop "strictly".

**Necessity and scope (N4).**
- *Metric.* The necessity argument is stated at the instrument level ("a target instrument at distance c > 0 from 𝒞
  is approximated by none of them"). Level B is a law-level target. On route C the gap transfers, because the
  identified carrier holds the whole state, with no memory outside ℂ^S. State that, and give a law-level witness.
  Reviewer check C5: on two configurations, any classical stochastic map reused for "H" errs by at least (√2 − 1)/2
  in TV on (|0⟩, H, Z) or (|0⟩, H, H, Z). The bound is attained, and the coherent countercontrol has gap 0.
- *Carrier labels.* The §2.1 table labels A1's carrier "C", and D2, D3, D9, D10 and D11 use "C" for
  configuration-level dynamics. §1 defines route C as the configuration set read as the quantum carrier under
  Main:564's interface. These differ. A1 and A2 are configuration-level dynamics with hidden memory, and they
  reproduce the laws (D2, D3), so NX-1's necessity holds relative to the route-C *identification*, not to
  configuration-level dynamics as such. Relabel those rows (e.g. "C-dynamics") and add this scope sentence to §4.2.

**Route E_f.** The single-qubit witness holds in both candidate frames (§5 below). It is conditional on Lemma F, as
stated. *N-E1:* Lemma F (MECH-2 node 2) is stated "by an orthogonal frame". Main:562's SIC reconstruction frame is not
orthogonal (tr D₀D₁ = −1, rv_frames R1a). Lemma F's proof of (a)–(b) does not use orthogonality, only that operations
are stochastic on laws and the identification is linear and injective. Its application to the SIC frame is therefore
the writer's [A] extension and should be labelled so. This is folded into B2.

## 5. §5 owner addition

**B1. Route-C quantum compatibility is misclassified.**
- §1 defines quantum compatibility as "the realized laws are, within the stated accuracy, laws of quantum
  instruments on quantum states". The owner's wording (c.6742051100) is "the resulting joint states correspond to
  quantum states under the stated comparison".
- On route C every reachable state is diagonal, hence a quantum state. Every branch is a CP diagonal-preserving
  map. Every realized law is therefore a quantum law. Compatibility **holds**, as do validity and closure.
- What fails is a fourth property: coverage, or inclusion, of the target class. The needed coherent states and
  instruments are not reached within TD < ½, which is the ε-robust obstruction the writer proves (G4; reviewer C2
  confirms TD ≥ ½, attained exactly at D = diag ρ).

Required changes:
- §5.1 route-C row: compatibility holds, and a separate "coverage of the target" entry fails.
- "Independence witnessed": drop route C as a witness. The other three witnesses (finite b, QP node 10, A1 with
  non-quantum data) suffice.
- §0 item 6 and the §5.2 verdict: replace "no on the configuration carrier" with "closure, validity and
  compatibility hold trivially; inclusion of the needed joint states fails, ε-robustly (TD ≥ ½)". The §5.2 item 1
  body already says "Closure holds trivially, but inclusion fails". The headline reading, J3 together with closure,
  folds inclusion into closure, contrary to the owner's request that the outcomes be reported separately.
- Align §1's definition with the owner's text, which is now posted.

**B2. Route E_f "states yes" depends on the frame and is false for R1.**
- §1 defines E_f by "a fixed frame (QP's U′, MECH-2's R1^⊗n)", and D21 assumes "tetrahedral frame as R1's frame [A,
  assumed reading]". AP1 §4.2 defines R1: an ontic point (z, x) ↔ Bloch vector ((−1)^z, (−1)^x, (−1)^{z+x}), with
  |v| = √3 and ρ = Σ μ_λ (I + v_λ·σ)/2, an orthogonal frame. Main:562's frame is p_i = (1 + a_i·r)/4 with |a_i| = 1,
  which is a SIC POVM. These are different identifications.
- rv_frames.py results:
  - R1a: R1 is orthogonal and SIC is not. R1's coordinate functionals are not PSD (eigenvalue (1 − √3)/4).
  - R1b: for all 24 single-qubit Clifford rotations the frame matrices **coincide** in the two frames. The 12 A₄
    rotations give permutations, and the other 12 have minimum entry exactly −1/2. So §4.2's single-qubit claims and
    G3 hold under either frame.
  - R1c: for CNOT the frame matrices **differ**. The minimum is 1/4 − √3/3 in SIC, confirming G5b exactly, and −1/4
    in R1. "Entangling continuation no" (conditional on Lemma F) holds in both frames; the quoted value is SIC-only.
  - R1d: every quantum state has nonnegative SIC coordinates. Under R1 the pure state r = −v₀/√3 has coordinate
    (1 − √3)/4 < 0, and Φ⁺ has a product-frame coordinate −1/8.

  So under R1, the frame Lemma F, Theorem U2 and §1 refer to, "representing approximate joint states is not
  obstructed by the frame" is false: non-stabilizer states and Φ⁺ itself have negative coordinates.
- Repair: split E_f into E_f(SIC, Main:562) and E_f(R1, AP1/MECH-2).
  - States: yes under SIC, no under R1 (with the exact witnesses above).
  - Entangling continuation: no under both, conditional on Lemma F. Under SIC this rests on the writer's [A]
    extension of Lemma F (N-E1).
  - Give the CNOT minimum per frame.
  - Correct D21's assumption, and §0 item 6.

**Route E_r "yes": confirmed, in exact ring, with the complex structure as data.**
- rv_Er.py builds Main:566/:580's construction from scratch for a 2-qubit experiment with complex instruments
  (H, S, CNOT, a 3-4-5 rotation, and Z, X and Y reads). Its configurations hold the Q(i) register, stack, record and
  seeds. One fixed step map per instrument uses exact cumulative thresholds. Results:
  - E1: each of the 8 step maps is injective on all 1,008 reachable pre-horizon configurations, and one map extends
    to an explicit bijection of a finite set.
  - E2: all 16 reachable registers are Hermitian PSD.
  - E3: realized laws are valid, and 0 < TV ≤ (#measuring steps)/G ≤ K/G, for a fixed protocol (TV 1/24) and an
    adaptive one (TV 1/100).
  - E4: complex entries are reached.
  - Countercontrols: a partial-transpose step gives a non-PSD register; removing the stack is caught as
    non-injective; a wrong target law violates the bound.
- This is an instance check, labelled; the general statement is Main's [P]. The writer's verdict is correct and
  correctly scoped as "mathematically available, not derived". In the exact ring this is exact closure, not an
  approximation phenomenon.

**Finite b: confirmed, with stronger support available (N5).**
- §5.1 "Closure fails" at finite b cites only Main:578's general sentence. rv_finiteb.py gives an explicit
  reachable instance:
  - setup: one digitized y-rotation (θ = π/4), applied to the exact initial register |0⟩⟨0|, under a stated
    round-to-nearest reading of Main:578's fixed-point model;
  - result: a register with det < 0 at b = 12, inside the Rounding Lemma window for K = 1 (det = −325/2097152);
  - control: the unrounded product is rank one and PSD;
  - validity: the clipped pre-grid probabilities stay valid.
- This supports "validity holds, closure fails" as a witness inside Main's own model. Cite it as reviewer
  instance-level support under that reading. It does not bear on the open law-level bound.

**Separation of the three outcomes.** Apart from B1, each entry gives its own reason. The one derivation used,
closure ⇒ validity for exact CP maps on a PSD register, is stated where it is used. This is correct.

## 6. Q4 (continuous coherent mixing): confirmed, with citation nits

- **Not necessary for Level A or Level B's shape.** This holds because Main's proofs are in the exact ring and the
  coherence sits in the supplied Kraus data.
- **The discrete core is necessary for an OI-native approximate target on route C**: an operation that does not
  preserve diagonals, and a non-real operation. Both necessity arguments are correct. The first is the G1/G4/C2
  obstruction. The second is reviewer C3: tr(RY) = 0 for real symmetric R, and real Kraus operators keep real states
  real.
- **The drive scoping is kept.** §0 item 4 says "that it can carry the phase does not show that OI supplies the
  drive", and §6 quotes Main:590 ("as an empirical controllability resource"). GR:250 (the driven transition) and
  GR:258 ("the quarter phase is dispensable at every level") support "carries the phase". `obligations_independent`
  (C5Discovery.lean:59) is correctly read as phase-versus-layer-flow independence on Fin 2 only.
- **N10 (citations, [L], recalled, not re-read).** The details match the reviewer's recollection: Lloyd, PRL 75, 346
  (1995); Deutsch–Barenco–Ekert, Proc. R. Soc. A 449, 669 (1995); Dawson–Nielsen, QIC 6, 81 (2006).
  - Lloyd and Deutsch–Barenco–Ekert concern almost every two-qubit gate applied to chosen qubit pairs. "One generic
    unitary with the permutations of S" is the analogous generic-pair density statement. Label it [A, by analogy]
    rather than attribute it to them.
  - The O(log^c(1/ε)) rate of Solovay–Kitaev and Dawson–Nielsen assumes a generating set closed under inverses.
    Inverse-free versions exist; they are recalled, not checked.
  - D19's assumption should read "a gate set generating a dense subgroup (inverse-closed, for the stated rate)".

## 7. Dependency matrix (D1–D26)

The rows were checked against their sources.
- **Lean citations.** D1 `finite_horizon_equivalence` (Equivalence.lean:462), D2 `S_imp_D` (:422), D13
  `exactAll_iff_physical_general` (GeneralCarrier.lean:100), `five_way_minimality` (RankGapTheory.lean:702), D15
  ExecSource.lean:52, D16 ExecSource.lean:129 and LiftAudit.lean:183, D26 `PhaseSource.lean`: identifiers and lines
  are confirmed.
- **Probe files.** `opglue_probes.py`, `intervention_probes.py`, `lg_comb_probes.py`, `review4_probes.py`,
  `nogo_probes.py` and `equivalence_recovery_probes.py` exist at `fd539e15`.
- **Statuses.** These match their sources:
  - proved: D3, D6 and D7 in the exact ring;
  - open: D4, and the finite-b capacity part of D6;
  - the D8 split between the proved factorization half and the imported unboundedness;
  - D11 (Main:584/:600/:362);
  - D12 open (Main:602);
  - D20 W-conditional;
  - D24 Substratum:131–133 (H-Bell).
- **Corrections.**
  - D17: "FI-1 ⇏ NX-1" and "strictly weaker" need B3's witnesses.
  - D20: add "orthogonal frame" to Lemma F's assumptions.
  - D21: the frame assumption is false as worded (B2); split it by frame.
  - D5 (N6): Main:578 states "the instrument-level inequality is proved". #945's off-main review (c.6567863298,
    owner question 6, undecided) finds the complex-entry constant only estimated. Write "stated proved on `main`;
    the complex-entry constant is contested off `main`; owner question 6 undecided", not "open" without qualification.
  - Carrier column: see N4.
- **#945's disproved step (§A.42 item 8, N7).** §1's [OFF] entry applies one group label, "Provenance and support
  off `main`". Item 8 requires a classification for each reference. Read claim by claim:
  - D4a "disproved" uses the counterexample. Its record is at `6d494e30` (#945 c.6657435508 names the kept-branch
    head `16fc745d`; both are verified *not* ancestors of `main`), and the d = 4, b = 24 instance with 6.9063 against
    4.0000 is from c.6567879503 §2. These are **support off `main`**, a gap if this record ever lands.
  - The same holds for D4b (Kη ≤ 1/64, 14K²C) and D5's complex-entry qualifier, and for §2.2's account of the
    counterexample.
  - The F0 shift is now support on `main` (git history, §1 above).
  - What `main` itself supports is "open" (Main:568, :578), not "disproved".

  Since nothing here lands, the gap is to be recorded, not closed, and the classification corrected. The values
  quoted (d = 4, b = 24, 6.9063 against 4.0000, 14K²C, Kη ≤ 1/64, "reachability … not shown") match #945's comments
  verbatim.
- **Independence of #945.** Correct: the OI-derived rows do not depend on the finite-b repair.

## 8. Probes and disclosures

- **Writer's probe.** `approx_generic_checks.py` (sha256 `12aac10f…72c0`, verified) was re-run: exit 0, and its
  output is byte-identical to `approx_generic_checks.out` (`4337d4af…5c35`; 25 PASS). r0 and r1 also re-run
  byte-identically (r0: G1a FAIL; r1: G1–G3 ALL PASS).
- **Disclosure.** It is accurate. r0 failed on sympy's `Abs` simplification and passed with a determinant test.
  Two G4–G5 intermediates failed, one stopped and one an assertion before `expand`, all in checking code. *N13:*
  say explicitly that the two G4–G5 intermediates were not retained; only r0, r1 and the final version are kept.
  Note also that r1 is a passing G1–G3-only run, not a failure.
- **Labelling.** G5's frame is Main:562's SIC frame, and its docstring says so. The text's attribution of G5 to
  "R1's frame" is the B2 issue, not a probe defect. G1b's `solve`-based check is weak; the closed form is decisive.

Reviewer probes (all exit 0, ALL PASS):

| File | sha256 | Checks |
| --- | --- | --- |
| `rv_frames.py` | `7169b7d38a637a24fe1d315161996178c887fee1483fe51369b3662067ee6d22` | 23 PASS |
| `rv_frames.out` | `45790a004ddf96e82ed79cb2a3b3c8774723262701fdaa7424f48002b2bb6642` | |
| `rv_routeC.py` | `6b9a4cead5df01f01b4bbfe813c6f03129a59a33f4bc210fb1e410eec79f4c15` | 23 PASS |
| `rv_routeC.out` | `bded494419ac8dbee719519ee6c4ec478c208338ff31ed6d3460408002ef1a01` | |
| `rv_Er.py` | `0b74887ef3ca13e3d80ea6d61cfccf31efc318d15d7fdc42955ebba4ec92478e` | 15 PASS |
| `rv_Er.out` | `62534a343989f0593c8797b742794734743b02a51e8bbbb12fc506a508805f61` | |
| `rv_finiteb.py` | `7676fcf29358a668ece160f4326b65c6539d6a291e6dab5c69f9c0dfaed38f47` | 5 PASS |
| `rv_finiteb.out` | `1e15387c77587412ca3962f0d81c560eaa4351eadee880a50b4d0d55c472cb6f` | |

Each group has a control or countercontrol that fails or passes as stated. The checks run on generic matrices and on
one from-scratch instance of Main's published construction (rv_Er), not on any OI mechanism. rv_Er and rv_finiteb are
instance checks under stated readings, and no verdict above rests on them alone.

## 9. General

- **Three-column separation.** Kept. Column (iii) is never used for (ii). §8's ledger is consistent.
- **Owner's distinctions.** Configuration versus encoded carriers, available versus derived, and mixing versus the
  full rules are kept, apart from the carrier-label slip (N4). The three outcomes are separated, apart from B1.
- **Scope of every negative.**
  - B-2 is scoped to a fixed finite S with compositional repetition. G2 checks it, and the
    lcm(1..|S|)-periodicity is correct.
  - Route C is scoped to Main:564's interface, but needs the no-hidden-memory sentence (N4).
  - Route E_f is conditional on Lemma F and needs the frame split (B2).
  - Nothing is turned into impossibility for every observer-level extension.
- **Register.** Neutral and in WIP voice; no self-narration or reader instruction found. *N12:* "QP" is used (QP's U′,
  QP node 10) but not defined in §1.
- **Authorization.** None is implied. The header, §11 and OQ1–OQ5 are neutral questions, and the record states no
  write.
- **§A.31.** The fixed-point statement, "not yet reached", is accurate. This review adds one NEW finding (B2: the
  frame dependence of E_f representability) and one ELABORATING finding (B1).

## 10. Blockers and nits

**Blockers**
- B1. §5.1, the independence list, §0 item 6 and §5.2: route-C quantum compatibility holds; the failure is coverage.
  Report coverage separately and align §1 with c.6742051100.
- B2. §0 item 6, §4.2, §5.2, D20 and D21: E_f "states yes" is false under R1. Split SIC from R1, give CNOT's minimum
  per frame, and label Lemma F's use under SIC as [A].
- B3. §4.2 and D17: FI-1 ⇏ NX-1 needs a theory-level counter-model (CM architecture, C4), and "strictly weaker than
  executability" needs `polarizedTheory_swap_half_level_one`, `gateFlow_half_not_preservesDiag` and
  `polarizedTheory_not_layerFlowExecutable`.

**Nits**
- N3. Cite `obs_availExt_le_substratum` and the rule-(f) to `availExt 1` reading in the route-C composition.
- N4. Give a law-level necessity witness (C5, (√2−1)/2). State that route C has no memory outside the carrier.
  Relabel "C" for A1, A2, D2, D3, D9, D10 and D11 as configuration-level dynamics.
- N5. Cite the reachable non-PSD finite-b instance (rv_finiteb) for "closure fails".
- N6. D5: "stated proved on `main`; complex-entry constant contested off `main` (owner question 6)".
- N7. Classify each [OFF] reference under §A.42 item 8. D4a, D4b, D5-complex and §2.2 are support off `main`; F0 is
  on `main`.
- N8. The "+22" is the writer's inference, verified via `7c6ceaaa` and `02009693`.
- N9. Put B-3's composite scope into the "meets Level B's shape" sentence.
- N10. Lloyd and DBE are cited by analogy, and Solovay–Kitaev needs inverse closure. Adjust D19's assumption.
- N11. A1's adaptive coverage is [A]. The :520 |C_H| formula is the passive one.
- N12. Define QP.
- N13. State that the G4–G5 intermediates were not retained.
