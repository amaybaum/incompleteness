# Coordinator's audit of thread Y (EXCLUSION), stage 4 (Q-EX) — 2026-10-10, 15:25Z–15:45Z

Audited record: `pt/Y/RESULT.md` (`991b01a8…`, 412 lines), `pt/Y/NOTES.md` (`ae1e54c4…`), `.start_marker`
(`fa455b7e…`), scripts y1–y7 and y7x with their outputs. Governing text: `pt/PROTOCOL-STAGE4.md` (`d3da2811…`),
amendment-2 labels, the owner's notes 5 and 6 (`pt/audit/stage4-inputs/`, not transmitted to the threads beyond the
erratum and the provenance requirement that Y records as NOTES N2). Reference fixed before Y reported:
`PRE-AUDIT-QEX.md` (14:47Z; `indep_checkQEX.py` 15/15). The four distinctions of owner note 4 are kept apart below:
reproducibility (§2), correctness (§3–§4), run history (§2, §3), the strongest warranted conclusion (§6).

## 1. Integrity (green)

- `pt/Y/` contains exactly the files RESULT §4 lists plus the eight `.replay.{out,err}` pairs. The 22 sha256 values
  printed in RESULT §4 were re-verified with `sha256sum -c` from Y's listing (`y_listed_hashes.txt`, this directory):
  22/22 OK. All 18 `.err` files hash to `28d3b9e8…` (the single line `exit 0`), as RESULT states.
- File modification times agree with the corrected chronology of NOTES N11 (y1 14:52:30 … y7 run 2 15:12:24,
  replays from 15:20:23). One slip: N11/N12 give the replay window as 15:20:23–15:21:33Z, while `y7x_probe.replay.out`
  was written at 15:21:54Z. Times only; no content effect.
- Y's start and end checks (manifests, base HEAD `9f9f8257…`, empty porcelain, protocol hashes and sidecars, no
  bytecode, sweep) are as recorded. Y's sweep found only `pt/Z/` created after its marker, read by name only.
- Scope: Y did not read `pt/Z/`, `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/reviews/` or
  `pt/audit/aborted-launches/`; it wrote only in `pt/Y/`. Its reading of `EQ2-SYNTHESIS.md` is within scope: the file
  sits at `pt/inputs/ledgers/`, a stage-1 input. No git write, branch, PR, CI, network or sub-agent.
- The launch message said "eight protocol hashes" and listed seven; the slip was the coordinator's. Y checked all
  seven plus their sidecars; nothing was missed.

## 2. Reproducibility (distinct from correctness)

**Y's own replays.** `cmp` of `y*.out` against `y*.replay.out`: 8/8 identical (stdout and stderr).

**Coordinator's replays of Y's eight scripts.**
- Attempt 1 (`replay/`, 15:25Z): INVALID — the loop called `/usr/bin/time`, which is absent here; every run exited 127
  with empty stdout (`y1_criteria.err`: `/usr/bin/time: No such file or directory`). A harness failure, not a script
  failure; kept as the record of the attempt.
- Attempt 2 (`replay2/`, 15:29–15:30Z): run from `pt/Y` as working directory, `python3 -I -B`, outputs redirected
  into `replay2/`. stdout 8/8 byte-identical to Y's originals. stderr differs in all eight only by the coordinator's
  exit-marker convention (`exit=0` against Y's `exit 0`, 7 bytes each); the scripts' own stderr is empty in both.

**Coordinator's independent checks** (replayed 15:38Z; `.replay.{out,err}` byte-identical to the final run):
- `indep_checkY.py`: run 2 28/28 `INDEP-Y-CONFIRMED`. Run 1 (kept as `indep_checkY.run1.*`) 26/28: two harness
  errors of mine — C6c demanded the zero quadratic form for a reachable state, where the correct countercontrol is a
  degenerate form (det Q = 0; the `X⊗X` torus does entangle `|00⟩`, M = 1); S1's spanning set lacked phases on two
  components (rank 12), fixed by phases on all components (rank 15). The other 26 lines are identical across runs.
- `indep_checkY5.py`: run 2 6/6 `INDEP-Y5-CONFIRMED`. Run 1 (kept) 5/6: F6c wrongly asserted that every Clifford
  image of `|00⟩` is a product; the countercontrol is min 0 over the group with some image entangled. Five lines
  identical across runs.
- A first `cmp` of the replays reported a difference caused only by my appending the exit line to stdout instead of
  stderr; redone with the original convention, identical.

Reproducibility of Y's record is therefore established; nothing in this section bears on whether its claims are true.

## 3. Correctness: independent checks (written without Y's code)

What the two coordinator scripts establish, against Y's claims:

| Y claim | coordinator's check | result |
|---|---|---|
| Y1 pairings `(1 − c⟨φ₀|φ⟩²)/2`, `(4 − 2c + c²⟨φ₀|gφ₀⟩²)/16`, spectrum `{1−c, 1, 1, 1}/8`, window `(1, 2]` sharp | D1–D4c (symbolic in c, exact instances; c = 1 and c = 5/2 countercontrols) | confirmed |
| largest product overlap `(1 + √(1 − 4|det Ψ|²))/2` | D5, D5c | confirmed |
| Y3 axis classification: control axes z (dim 1), x, y, (3,4,0) (dim 2) exceptional at level (i); off-axis closure dim 4 containing `{(0, b)}`; level (ii) leaves exactly x, y, z | A1–A4 (Lie closure in su(2)⊕su(2) by cross-product brackets, eight axes) | confirmed |
| Y4 det identity `cos2β·D − (i/2)sin2β·M`, positive definiteness of both `Q_ψ`, seed c = 4609/4608, window inequality, seed subdual on 66 torus images and negative on `P_φ₀` | C1–C6c (det/tr = 1/9, 121/42; x = 1/576) | confirmed |
| Y6 T: c(E0) = 15, c(P00) = 9, automorphism invariance | S1–S3 (120 cap-boundary pure states span E0⊥; PSD on `|00⟩⊥` spans Herm(3)) | confirmed |
| Y6 F: `y = P_f3 − E0` witnesses non-perfectness of K(E0) | S4, S5c | confirmed |
| Y7 R1: R rational of order 3, cos(RR′) = 127/162 (control), −113/162 (target), infinite order by the algebraic-integer argument; cyc3 gives −1/2 | R1–R4c | confirmed |
| Y7: `actC(R)E0 ∉ K(E0)` and a defect of Z_F leaves K(Z_F) | R5 (exact λ-interval decision on the characteristic coefficients: feasible set empty), R6, R7 (my own witness, pairing −2383/5316) | confirmed |
| Y5: Clifford group mod phase 11520 (23040 with T); d_min = 5/256 for φ₀ = (1, 2, 3i, −1+i), attained in G16; c = 517/512; T-invariant | F1–F5 (exact Gaussian-integer enumeration, representation independent of Y's) | confirmed |
| Y5 controls: `|00⟩` and the Bell vector give minimum 0 | F6c | confirmed |

Not independently recomputed: Y2's exact group census beyond the pre-audit (which already fixed the CNOT
decomposition, the Lie closure, `V⁻¹ZVZ`, the discrete factor and six reachability instances), Y4's four other
families (actC Ry, actT Ry, actT Rz, the drive; Y's seeds 1541/1536, 5677/5632, 17409/17408, 4609/4608), and Y6's
Z_F invariant values. These rest on Y's exact scripts (replayed identically) and the reviewed arguments below.

## 4. Correctness: proofs reviewed

- **Y1, the dichotomy.** Reachable ⇒ K ⊇ all pure states ⇒ K ⊇ Q3 ⇒ K = K* ⊆ Q3* = Q3: sound (PSD self-duality
  [K JordanClassification.lean:84]). Unreachable ⇒ EXOTIC-E: m < 1 by compactness of Ĝ·SEP; for 1 < c ≤ min(2, 1/m)
  the seed cone is Ĝ-invariant and subdual (D1–D2), closed because generated by a compact set in the open half-space
  `⟨E00, ·⟩ ≥ min(1, (4 − c)/8) > 0`, and e ∉ Q3 (D3); EBF (audited, AUDIT-X) extends it. The dimension count
  (finite or ≤ 1-dimensional compact Ĝ gives a reachable set of real dimension ≤ 5 in CP³) is correct. The gap
  between the protocol's two criteria is therefore empty for compact Ĝ: the Bell-type criterion is the case c = 2.
- **Y2, the group.** δ(g) = det A/det B is phase-invariant and multiplicative; the word
  `(V⁻¹⊗I)·CNOT·(V⊗I)·CNOT = I⊗P₊ + V⁻¹ZVZ⊗P₋` puts the connected group `C = {U⊗P₊ + V⊗P₋}` inside the generated
  group without a closure argument; `{A⊗P₊ + B⊗P₋ : det A = ±det B}` modulo phase is exactly `C ⊔ C·Ad(I⊗Rx(π/2))`
  (checked: det A = det B forces a common phase up to sign, absorbed in SU(2); det A = −det B is the other coset).
  **Owner note 6 is honoured by Y's text:** reachability is proved with `g ∈ C` alone (RESULT §1 Y2, "g = U⊗P₊ +
  V⊗P₋ ∈ C"); the discrete element enters only the exact census. The uniqueness proof does not use it.
- **Y3, axes.** Generators (n, n) and (n, Rz(π)n) for a control axis; abelian iff n ∥ Rz(π)n, i.e. n ∥ z or n ⊥ z;
  otherwise `(0, n − n′)` and `(0, n × n′)` give the second factor and the closure is ℝn ⊕ su(2), which contains
  `{(I, V)}`, enough for reachability (a ∝ u, V a ∝ v). Target side with Rx(π). Level (ii): T sends an axis to
  (nₓ, −n_y, n_z) up to sign and Ad(I⊗Z) acts by Rz(π), so (3,4,0) becomes reachable and only the native frame's
  coordinate axes stay exceptional (A4). Sound, and exactly as predicted in NOTES N5 before the run.
- **Y4, reduction and certificate.** Ĝ = T·G16 since G16 normalizes the abelian torus and the torus is generated
  with cnot; `|det Ψ|` is invariant under local unitaries and conjugation, CNOT exchanges L and N and is normalized
  by Loc8, so the minimum over Ĝ reduces to β ∈ S¹ and ψ ∈ {φ₀, CNOTφ₀}. The seed c = 1 + x/8 with
  x = 4·min(det Q/tr Q)/|φ₀|⁴ ≤ 4·λ_min/|φ₀|⁴ ≤ 4·d_min lies in the window because `2/(1 + √(1 − x)) ≥ 1 + x/8`
  (C4). The Bell-type route is provably unavailable for the S3 instance (cc2), so this node is decided only by the
  new direction of the dichotomy. Run 1 failed on Y's own discretization of c (list ending at 513/512); the rule
  change is recorded in the header and NOTES N6 and is the right one.
- **Y5.** Seeds inherit to subgroups (smaller reachable sets); S2's torus is local and normalized by G16, so its
  reachable set is G16·SEP. Sound. Cosmetic: ids `O-LPT`, `O-G16` each occur twice in `y5_finite.out` (Y notes it).
- **Y6 H.** Koecher–Vinberg and Jordan–von Neumann–Wigner remain [L]; the Lorentz exclusion by two non-proportional
  extreme rays whose sum is on the boundary (`⟨P00 + P01, P11⟩ = 0`) is correct and replaces stage 3's [L] input;
  `K = A(Q3)` self-dual gives `AᵀA ∈ Aut(Q3)`, and Aut(PSD₄) is now [K + W] through `orderIso_jordan`
  (OperationalRigidity.lean:848) and `matrixJordan_unitary_or_transpose` (JordanClassification.lean:825), both
  imported by the certified build (OIBridge.lean:91–92); twin fails H2 by `cnot_idW`, `chain_value`
  (K2Guard.lean:110, 134). Sound.
- **Y6 T, F.** `c(x) = dim span(K ∩ x⊥)` is Aut-invariant on a self-dual cone because `Aᵀ ∈ Aut(K)` and
  `y ↦ Aᵀy` is a linear bijection `K ∩ (Ax)⊥ → K ∩ x⊥`: sound. Non-perfectness witness sound (S4).
- **Y7 R1.** Infinite closed subgroup of SO(3) has identity component SO(2)_m or SO(3); an O(2)_m-type closure cannot
  contain two order-3 rotations about non-parallel axes; a closed finite-index subgroup of SO(3) is SO(3); the kernel
  of the first projection has finite index and its closure contains `{(I, V)}`. Sound. The favourable branch was
  pressure-tested (N7–N8) before the witness rule changed, and the exact run 2 plus my R5/R7 confirm the exit of both
  stage-3 cones.
- **Provenance (O).** Every UNIQUE symmetry node consumes (b), rotations acting on a token inside an arbitrary
  entangled pair preserving the pair cone. (b) is INDEPENDENT of H1–H3 at L: the stage-3 cones satisfy H1–H3 and
  violate (b) for S4-C, S4-T, S5, the listed S3[n] axes and R1 (exact), and for any other UNIQUE node by that node's
  own proof. Anchors verified in this audit (file:line as cited): `boundaryTransitive_fullAut3`
  (OrbitGeneration.lean:537), `BoundaryTransitive` (:79), `control_not_implies_parallelReferenceExtension`
  (ReferenceExtension.lean:507), `oiPlus_independence` (CompletedOI.lean:506),
  `not_boundaryTransitive_of_nonextreme_boundary` (TransitiveBody.lean:301), `ElementaryDrivability`
  (KInfFoundations.lean:264, `J_off_axis` :276), `ball3Drive` (:449), `nflip` (CompositeDimension.lean:797),
  `IE1` (inputs/fourcopy/FourCopyCore.lean:156), `ipW`/`dualW`/`transposeW` (FourCopyDefs.lean:31, 34, 49),
  `pauliW`/`Q3`/`twin` (FourCopyPackage.lean:176, 180, 183), the `W 3` definitions (CompositeDimension.lean:97–225,
  741–797, 1220), K2Guard.lean:46, 101, 104; ROADMAP.md:68, 1001–1005, 1014–1022; GR.md:212, 228; KT4-PREM-1
  result.md:171–172, 191–192, 243; EQ2-SYNTHESIS.md:161–167; PROTOCOL-STAGE2.md:82–86; S2/RESULT.md:343–354. The
  label "K = Q3 CONDITIONAL on (b)" is the amendment-2 label the evidence supports; Y's argument that (b) is not a
  restatement (SEP and maxCone satisfy it; K_gen and the exotic cones do not) is correct. The observation that the
  literal pair transfer of `BoundaryTransitive` fails for Q3 itself (rank-2 states are non-extreme boundary points)
  is correct and is a genuine exposed assumption in the protocol's wording of H's observer reading.

## 5. Corrections and observations

1. "Eight" protocol hashes in the launch message: coordinator's slip; seven exist and were checked.
2. Replay-window end time in NOTES N11/N12 (15:21:33Z) precedes the last replay file (15:21:54Z); times only.
3. Duplicate line ids `O-LPT`, `O-G16` in `y5_finite.out`; lines are distinguishable by group name.
4. Y's verdict table row H cites "[W + X + K + L]"; the [L] inputs (Koecher–Vinberg, JvNW) remain unverified
   literature, so H's UNIQUE verdict is CONDITIONAL on them as well as on H itself. Y's §3 says so; the table's
   evidence column should be read with §3.
5. Nothing in Y's record contradicts the pre-audit; items A–E of `PRE-AUDIT-QEX.md` are each matched (A: G2a/G2b;
   B: L1, G4, the discrete factor; C: the generic reachability case `u = 0 or v = 0` handled in Y2; D: K1–K2;
   E: Y1.2).

## 6. Verdict on thread Y

**Reproducible** (replays 8/8 and 8/8; independent checks 28/28 and 6/6, replayed identically) **and correct as
far as reviewed**, with the stated scope:

- The exclusion dichotomy for compact symmetry groups containing cnot is established [W + X]: UNIQUE iff Ĝ·SEP is
  every pure state; EXOTIC-E otherwise, by a cap defect whose window is sharp.
- S4-C and S4-T are UNIQUE and minimal among the fixed nodes; "K = Q3" is CONDITIONAL on (b) for the node's group,
  with (b) INDEPENDENT of H1–H3 at L. The uniqueness proof uses the connected subgroup alone (owner note 6).
- The precise additional freedom is (b) for one local rotation of one token off the native frame's coordinate axes
  (S3[n] off-frame; R1 for a single order-3 rotation); the native drive lies on the exceptional set and does not
  suffice (EXOTIC-E, exact seeds).
- S1, S2, S3, the finite extensions and the drive are EXOTIC-E (existence only; explicit cones are Z's).
- H is UNIQUE conditional on H and on two [L] inputs; its minimality is UNRESOLVED; T and F are EXCLUDES-KNOWN only.
- Whether embedded observation demands (b) is UNRESOLVED at L; no premise at L supplies it.

Rows of the owner's five-row table that Y settles, for the stage-4 integration (pending Z): excludes the stage-3
EXOTIC cones — yes, at S4-C, S4-T, S3[n] off-frame, R1, H (exact witnesses for every stage-3 cone); uniquely selects
Q3 — yes at those nodes, CONDITIONAL on the node's principle; weakest sufficient — S4-C/S4-T minimal among fixed
nodes, S3[n] off-frame and R1 strictly weaker in the refined lattice, H's minimality open; observer-native — not
derived at L, (b) INDEPENDENT; general equivalence — not claimed, CONDITIONAL on (b) or H. The independent row
"minimality supported by countermodels for each weakening" is Z's, to be evaluated separately (owner note 6).
