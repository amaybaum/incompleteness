# Thread C5 (BRIDGE-COUNTER), stage 5 (relaunch) — running notes

All clock times below are read from `date -u`; none are estimated.

## N0 — start (2026-10-10T16:45:05Z)

- `pt/C5/` did not exist at launch (checked 16:44:45Z); created at 16:44:59Z; `.start_marker` written first
  (utc_start 2026-10-10T16:44:59Z).
- Start checks (recorded in full in `.start_marker`): six manifests verify from `pt/` (rc=0 each);
  `audit/stage3-inputs/ns.manifest.sha256` verifies from its own directory (`ns/NS-INPUT.md: OK`, nothing else
  read there); `pt/base` HEAD = 9f9f8257a980a1819fbbc1dc0019917cf8678626, `status --porcelain` empty, no
  `__pycache__`/`.pyc` under `pt/base/`; nine protocol files with the required sha256 prefixes and all nine
  sidecars verify (STAGE4/STAGE5/STAGE5-AMENDMENT-1 from SCRATCH, others from `pt/`); `pt/` top-level listing
  with mtimes recorded. All start checks pass.
- Governing texts: `PROTOCOL-STAGE5.md` (9e01f098…) and `PROTOCOL-STAGE5-AMENDMENT-1.md` (1f639115…) read in full
  at 16:45Z. Working directory `pt/C5/`; sibling `pt/D5/` never read.

## N1 — reading complete, productivity test and plan fixed before the first node (2026-10-10T16:53:42Z)

**Read (in the prescribed order), 16:45–16:53Z.** `PROTOCOL-STAGE5.md`, `PROTOCOL-STAGE5-AMENDMENT-1.md`,
`PROTOCOL-STAGE4.md`, `PROTOCOL-STAGE3.md`, `PROTOCOL-STAGE2.md`, `PROTOCOL.md`, both amendments,
`PROTOCOL-STAGE2-DS.md`; `INTEGRATION-NOTE-STAGE4.md`, `audit/Y/AUDIT-Y.md`, `audit/Z/AUDIT-Z.md`, `Y/RESULT.md`,
`Z/RESULT.md`, `INTEGRATION-NOTE-STAGE3.md`, `audit/X/AUDIT-X.md`, `S2/RESULT.md`; ledgers `EQ5-SOURCE-RESULT.md`
(§0–§3.5), `EQ5-SOURCE-AUDIT.md`, `EQ2-SYNTHESIS.md:140–184`, `EQ3-P-RESULT.md:1–80` (plus a grep of the ledgers for
M_ρ/M_tw/anchor sum); the KT4-PREM-1 `result.md` in full; at L: `CompositeDimension.lean:85–234, 735–869`,
`KInfFoundations.lean:250–300, 395–490`, `CompletedOI.lean:1–160, 470–540`, `ReferenceExtension.lean:1–80, 425–552`,
`LiftAudit.lean:1–215`, `ExecSource.lean:1–40, 95–140`, `ReadWriteControl.lean:1–50, 140–185`,
`CompositeInterface.lean:205–245, 620–700`; design modules `FourCopyPackage.lean:150–300`, `FourCopyCore.lean:150–165`,
`FourCopyDefs.lean:40–55`. `base/AGENTS.md` was supplied in the launch context (code-review rules, §A.21, §A.31).
Disclosure: one version check at 16:53Z ran `python3 -c` without `-I -B` (sympy 1.14.0, Python 3.11.15); it wrote
nothing under `pt/` (checked at the end).

**Transcription facts fixed from L before any script (to be re-verified exactly in C1).**
- `nflip = diag(1,−1,−1)` on Bloch coordinates (CD:797): the half-turn about the first axis x; corner axis `z3 = e_z`
  (CD:793). In the Pauli dictionary (`pauliW`, coordinate order 1, X, Y, Z, first index = control) `actC nflip =
  Ad(X⊗I)`, `actT nflip = Ad(I⊗X)`.
- The certified drive `ball3Drive` (KIF:449) has `flow = rot3` = rotations about the THIRD axis z, `t₀ = π`, so its NOT
  is `rot3 π = diag(−1,−1,1)` (= Ad Z), not `nflip`; `J = cyc3`, `(x,y,z) ↦ (z,x,y)` (KIF:416–425), the order-3
  rotation about (1,1,1) carrying e_x→e_y→e_z→e_x, and `cyc3 ∘ rot3 t ∘ cyc3⁻¹` is the rotation about e_x. So "the flow
  through the NOT" (the protocol's flow, axis of `nflip`) is the J-conjugate of the certified `ball3Drive` flow. Both
  axes are coordinate axes of the native frame. The census treats the protocol's flow (axis x) as primary and the
  certified flow (axis z) as a record line.
- `NativeGate.relT/relC` (CD:224–225) are identities between `cnot` and `actT/actC nflip`; `CopyNatural` (KIF:284) is
  an identity between two copies' NOTs. Neither mentions a pair cone.

**Productivity test (fixed now).** A node is a gem iff it yields (1) an exact countermodel (H1–H3 and the candidate's
transcription verified exactly on it, `K ≠ Q3` exact) or an exact EBF seed with its overlap bound proved over the whole
reachable set, at a stated instance; or (2) an exact decision of a census subset (Lie closure exact + reachability
witness, or seed); or (3) an exposed hidden assumption (a transcription that changes a verdict). Restating a stage-4
verdict without a new exact check is record-only.

**Decision vocabulary (fixed now).** Per candidate: INDEPENDENT (exact countermodel: EXOTIC-X explicit cone; or
EXOTIC-E: existence by EBF [W, audited AUDIT-X] over an exact seed — never merged), CONDITIONAL / DERIVED (only if a
census subset forces Q3, stated as "forces Q3 given P", i.e. the P ⇒ (b_min) direction is thread D's), UNRESOLVED (no
countermodel and no forcing). EXOTIC-X/EXOTIC-E always written out.

**Plan (depth-first, decisive first).**
- C1 census (`c1_census.py`): exact transcription checks (cnot, actC/actT, nflip, cyc3, rot3 ↔ Ad of Gaussian-rational
  unitaries on all 16 basis tables); for every subset {flow}, {J}, {NOT,J}, {flow,NOT}, {flow on both}, {flow,J}, each
  placement (control/target/mixed) and level (i) cnot / (ii) G16: the exact Lie closure dimension, the reachability
  criterion (does the algebra contain su(2)⊗P₋ resp. |1⟩⟨1|⊗su(2) or the mixed analogue), and for every
  unreachable node an exact seed with its overlap bound proved over the whole reachable set (finite groups: exhaustive
  enumeration of signed-permutation actions; tori: the |det|² quadratic-form bound, local factors removed). Controls:
  Q3 retention (all maps are unitary/antiunitary conjugations); countercontrols: a reachable state must fail the seed
  test; a product must fail; a UNIQUE node's algebra must reach a stage-4 unreachable state.
- C2 closure picture (`c2_closure.py`): K_gen ≠ dualW K_gen (cite S2/RESULT.md S2.6), closure under cnot+flow and
  cnot+J proper and not self-dual (seed certificates), closure under cnot+flow+J = Q3.
- C3 countermodels in order η, θ, κ, ζ, ι (`c3_*`), then NOT/J/finite forms of α–δ, then λ without tok. K(Z_F) and
  K(E0) rebuilt from their definitions with H1 (symbolic SOS), H2 (permutation of defects), H3 certificates (spectra,
  orthogonality; SD2 [W, audited]); each candidate's transcription verified exactly on the cone; `K ≠ Q3` exactly.
- C4 kernel no-go theorems: scope transcription [K + W] (no script).

## N2 — node C1, the minimal-subset census (script written 16:58–17:00Z; run 1 17:01:14–17:02:50Z)

- Pre-run edit (before run 1, 17:00Z): the first draft of `main()` appended `UNDECIDED-<node>` to the failure list for
  census nodes; this contradicted the header's R5 ("UNDECIDED is printed, not a failure") and was removed so that the
  code matches the frozen rule. No other edit.
- Run 1: `python3 -I -B c1_census.py` → 60 PASS, 0 FAIL, `VERDICT C1-CENSUS-EXACT (undecided nodes: none)`, exit 0.
  Final (no failed run).
- Transcription (T0–T7, G1): the Lean `cnotFun` = Ad(CNOT) (control first); `actC/actT nflip` = Ad(X⊗I)/Ad(I⊗X);
  `actC/actT cyc3` = Ad(U_J⊗I)/Ad(I⊗U_J) with U_J = (I − i(X+Y+Z))/2; `rot3` (ball3Drive's flow) = Ad(Rz); the flow
  through `nflip` is `cyc3 ∘ rot3 ∘ cyc3⁻¹` = Ad(Rx), whose half-turn is `nflip`, while `rot3 π = diag(−1,−1,1) ≠
  nflip`; `transposeW` = complex conjugation; |G16| = 16 = Loc8 ∪ cnot·Loc8.
- Census (level (i) cnot, level (ii) G16; EXOTIC-E at (ii) implies (i); UNIQUE at (i) implies (ii)):
  {flow}@C dim 2 (span{XI, XX}), {flow}@T dim 1, {flow on both} dim 3, {flow, NOT} = {flow} (dims 2 / 1): all
  EXOTIC-E, seeds φ₀ = (1,2,3i,−1+i): d_low = 1/2304 (N = X⊗X) resp. 5/256 (no non-local direction); {J}, {NOT, J}
  (either token, and both tokens as record): finite groups (orbits of φ₀'s ray 384–11520), EXOTIC-E, d_low = 5/256;
  {flow, J}@C and @T: dim 6 (su(2)⊕su(2)), UNIQUE at level (i), exact reachability witnesses for φ₀ and ψ_a.
  Records: flow@C + J@T: dim 15 = su(4), UNIQUE; flow@T + J@C: dim 1, EXOTIC-E (the target flow commutes with cnot
  and with J on the control — an asymmetry); ball3Drive's own flow (axis z) reproduces the same pattern
  (z@C dim 1, z@T dim 2 with N = Z⊗Z, d_low = 1/8704; {z-flow, J} UNIQUE on either token).
- Cross-check against stage 4 (audited): d_low = 1/2304 gives Y4's c = 1 + (4·d_low)/8 = 4609/4608 for actC Rx and
  the drive; 1/8704 gives 17409/17408 for actT Rz; 5/256 is Y5's d_min. Same numbers from independently written code.
- Verdict for the bridge: among the native single-token operations idle-extended on one token, the minimal subsets
  that force Q3 are exactly {flow, J} (same token, either token) — and, as a record, flow on the control with J on the
  target; every subset without both a continuous flow and J admits an exotic invariant cone (EXOTIC-E). No subset
  of the census admits an EXOTIC-X cone except where the stage-3 cone K(Z_F) is itself invariant (checked in C3:
  the NOT-only forms). Gem type (2) and (3): the asymmetry of the mixed placement, and the identification of the
  protocol's flow with the J-conjugate of the certified ball3Drive flow.

## N3 — node C3, the countermodels η, θ, κ, ζ, ι, the NOT/J/finite forms, λ without tok, closure picture
(script written 17:03–17:08Z; runs 1–3 at 17:09:30Z, 17:10:23Z, 17:11:40Z; logged 17:12:08Z)

- Pre-run edits (before run 1, 17:09Z): (a) the ι countercontrol's witness search over Gaussian vectors in
  {−2..2}⁴ was preceded by an explicit candidate derived by hand (joint eigenvectors of X⊗Z and Y⊗Y with weights 4:9,
  giving pairings 3/13 and −5/13, Z's stage-4 values); (b) the κ circle checks used `sp.Abs`; replaced by x·conj(x)
  to keep the zero tests polynomial. Header (decision rule) unchanged.
- **Run 1 (kept as `c3_countermodels.run1.*`): 18 PASS, 6 FAIL, NO VERDICT.** Two errors of mine, both caught by the
  rule: (i) the defect vectors: I had taken ψ_s = (1, s1s2, s1, −s2)/2 from Z's RESULT as the vector of my e_s; with
  e_s = (E00 + s1E13 + s2E22 − s1s2E31)/4 the vector of pauliW(e_s) = (I − 2ψψ†)/8 is ψ_s = (1, s1s2, −s1, s2)/2 (the
  same SET, labels exchanged s ↔ −s; derived by hand from the joint eigenvectors of X⊗Z, Y⊗Y). Z1, Z5, KAPPA-cc2,
  LAMBDA-b, CL1 failed for this reason only. (ii) ETA-cc asserted ⟨E0, actC nflip E0⟩ = −1; by hand it is +1
  (actC nflip E0 = E00 + E13 + E22, which is outside K(E0) for another reason: E0'' − λE0 always has the negative
  eigenvalue −(1+λ)/4); the countercontrol needs only the target NOT (−1). Fixes for run 2: the corrected ψ_s; ETA-cc
  reduced to actT; LAMBDA-b made to check all four s (no witness search).
- **Run 2 (kept as `c3_countermodels.run2.*`): 24 PASS, 0 FAIL, VERDICT.** One description string (KAPPA) still named
  the κ seed with Z's label ("psi_(1,1)"); in the corrected labels C1(w=1) = (1,1,1,−1)/2 = ψ_(−1,−1), the vector of
  e_(−1,−1) = F (AUDIT-X S4). No computation involved the label.
- **Run 3 (final): 24 PASS, 0 FAIL, `VERDICT C3-COUNTERMODELS-EXACT`**, exit 0; `diff` against run 2: the KAPPA
  description line only.
- Content (all exact; K(Z_F) at level (ii) unless said): Z1 spectra/orthonormality/orthogonality (SD2 ingredients),
  Z2 H1 symbolic SOS, Z3 H2 with G16 generators, Z5 K ≠ Q3, Z6 K(E0) spectrum and level-(i) facts; ETA-a relT/relC;
  ETA-b NOT on either token permutes the defects; ETA-c copy naturality under exchange; ETA-cc K(E0) fails η-b;
  THETA defects in maxCone, conditional states in the ball, pure steering for every sharp effect; THETA-ns
  no-signalling identity; THETA-cc idW ∈ maxCone, cnot idW = chainW ∉ maxCone (−1/2); IOTA; IOTA-cc (3/13, −5/13);
  KAPPA gate flow U(w), CNOT = U(−1), circles C1 ∪ C2 invariant under U(w) and G16 generators, all maximally
  entangled → Bell seed F, EXOTIC-E; KAPPA-cc1 non-vacuity; KAPPA-cc2 K(Z_F) not κ-invariant (w = −i, −1/2);
  ZETA-1/2 pair-level drive (D(w), D(−1), J = monomial permutation unitary, J_off_axis at an exact body state);
  FORM-J block identities (no Bell-type defect with J on one token); LAMBDA-b every defect leaves K(Z_F) under actC
  cyc3 (so K(Z_F) violates (b)); LAMBDA-tw the twin is rotation-invariant (M_ρ, M_tw satisfy (b)); CL1 K_gen ≠ dualW
  K_gen (F ∈ dualW K_gen \ Q3).

## N4 — kernel theorems, closure picture, RESULT §0–§3 (17:12–17:16Z), and the hard-to-vary review (17:16:21Z)

- C4 (no script): the five theorems read at L (ReferenceExtension.lean:425–552, CompletedOI.lean:470–540,
  LiftAudit.lean:100–215, ExecSource.lean:95–140, ReadWriteControl.lean:140–185); line numbers re-confirmed by grep
  (ReferenceExtension :447, :507; CompletedOI :129, :327, :506; LiftAudit :112, :200; ExecSource :129;
  ReadWriteControl :158, :174; DerivedQ3 :222). Scope: all five on matrix carriers; the two spectator results fail on
  the non-CP Φ₂ of the round-34 countermodel, which has composite unitary control; the three availability results are
  L1/L0 statements. None decides (b) for reversible operations on W 3.
- Two citation slips corrected in RESULT before hashing (reflY is K2Guard.lean:46, actT/actC are CD:198/201). The
  protocol's ":365 quantumArchitecture_iff_drives_of_closed" is at StructuralClosure.lean:364 at L (thread D's anchor;
  recorded, not used here).
- **Hard-to-vary review.**
  - Rules fixed before data: both script headers (decision rules R1–R6, D1–D4) were written before their first runs;
    the only changes after a run were the c3 corrections recorded in N3 (a label error and a wrong countercontrol
    claim of mine, both caught by the rules; the rules themselves unchanged).
  - Controls: Q3 passes every retention check (c1 c5, c3 ZETA-ret, unitarity throughout); every EXOTIC-E node rejects
    a product and a reachable Bell state as seeds; no UNIQUE node admits a seed; K(E0) fails η-b and ι (so those checks
    discriminate); maxCone accepts idW and rejects cnot idW; the κ invariance check rejects (H⊗I)C1.
  - Predictions beyond the problem, checked: the census reproduced stage 4's audited seed numbers (4609/4608,
    17409/17408, 5/256) from independent code before I compared them; the protocol's pre-audit statement for (b_DJ)
    (Lie closure su(2)⊕su(2)) was confirmed (dim 6) rather than assumed.
  - Maximum skepticism on the favourable branches: (1) {flow, J} forcing Q3 — tested at level (i), for both flows
    (protocol's and ball3Drive's), with exact witnesses on a stage-4-unreachable state; recorded as "Q3 given (b)",
    not as a derivation. (2) θ looked as if steering might select Q3: the check shows the non-quantum defects steer
    maximally, and maxCone (θ) does not even give H2. (3) The finite form: rather than declaring "finite ⇒ countermodel",
    recorded that one off-frame order-3 rotation forces Q3 (stage 4 R1), so only the native finite data are
    countermodelled. (4) λ: M_ρ/M_tw were the launch message's named countermodels, but their cones satisfy (b); the
    exact check (LAMBDA-tw) moved the λ countermodel to the anchor sum with K(Z_F).
  - Exposed assumptions (gem type 3): the protocol's "flow through the NOT" is the J-conjugate of the certified
    ball3Drive flow (whose NOT is rot3 π ≠ nflip); M_ρ/M_tw do not bear on (b); the mixed-placement asymmetry; matrix
    sufficiency of one layer flow (DerivedQ3:222) does not transfer to W 3.
- Fixed point: passes over the candidate list after C3 found no further candidate assigned to C without an exact
  verdict (κ's explicit cone and ζ-3 remain UNRESOLVED, named).

## N5 — end checks, sweep, anomaly, quarantine (17:18:14–17:19Z; logged 17:19:17Z)

- Replays (17:16:26–17:18:00Z): `c1_census` and `c3_countermodels` replayed into `.replay.{out,err}`; `cmp`:
  both IDENTICAL on stdout and stderr.
- End checks (17:18:14Z): the six manifests rc=0; `ns.manifest.sha256` rc=0 (checked from its own directory only);
  base HEAD 9f9f8257a980a1819fbbc1dc0019917cf8678626, porcelain empty; no bytecode under `base/` or `C5/`; the nine
  protocol hashes unchanged (239dc123, b41aa0e7, 2a2f78f3, 38603692, 086a4cb8, 1a649168, d3da2811, 9e01f098,
  1f639115) and all nine sidecars rc=0.
- Sweep. A first sweep command at 17:18:14Z was malformed (its `-newer` test sat outside the pruned branch, so it
  listed every file under `pt/`); harness error of mine, no file written by it under `pt/` (the tool runner kept the
  oversized listing in its own tool-results file outside `pt/`). Redone correctly at 17:18:22Z.
- **ANOMALY (§A.26).** Files under `pt/` newer than `C5/.start_marker` outside `C5/`, `D5/`, `audit/`,
  `audit*-replay/`: `pt/PROTOCOL-STAGE6.md` and `pt/PROTOCOL-STAGE6.sha256` (mtimes 16:49:36Z, 16:49:55Z, i.e. after
  my marker at 16:44:59Z), and four new directories `pt/I1/`, `pt/I2/`, `pt/I3/`, `pt/I4/` (157 files, directory
  mtimes 17:17–17:18Z, still being written). I did not write them and cannot source them to the launch inputs; they
  look like a concurrent writer's work (another stage's protocol and threads), but that is not established here.
  Not read (content not opened); names, sizes, mtimes and hashes only.
- **Quarantine (never delete; write only inside C5):** moving the originals would write outside `pt/C5/` and could
  disrupt a concurrent writer, so the quarantine is a COPY: `pt/C5/evidence/sweep-20261010T1818Z/snapshot/` (159 files,
  relative paths and mtimes preserved, taken 17:18:56–17:18:58Z) with `MANIFEST.originals.txt` (sha256, size, mtime of
  each original, recorded before copying) and `MANIFEST.snapshot.sha256`; copies match the recorded originals. The
  originals are left in place untouched.
- Effect on results: none detected. Every script of this thread is self-contained (stdlib and sympy; it reads no file),
  every decisive run finished at 17:11:45Z (C3 run 3) and 17:02:50Z (C1), and every record this thread read is covered
  by the verified manifests or by `pt/base` at L (clean). Substantive work halted at the anomaly; only the records
  (NOTES, RESULT §4–§5, hashes) were completed afterwards. Reported for the coordinator's decision.
