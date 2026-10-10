# Audit of thread C5 (stage 5, Q-EX-BRIDGE, countermodel side) — coordinator

Base L = `9f9f8257…` (read-only). Governing texts `PROTOCOL-STAGE5.md` (`9e01f098…`) and
`PROTOCOL-STAGE5-AMENDMENT-1.md` (`1f639115…`). Audit inputs: `pt/C5/` as frozen by the thread (RESULT.md
`36c32e05…`, NOTES.md `cc2014f3…`), the pre-audit `pt/audit/stage5-inputs/preaudit_bridge.py` (7/7, run 3), the
stage-3/4 audits and integration notes, the kernel at L, and one clarification C5 gave by message at 17:47Z
(terminal only; it wrote nothing). Written 2026-10-10, 17:55Z.

## 1. Records and integrity

- **Hashes.** Every hash C5 quotes in RESULT §4 and its final report verifies on disk (16/16,
  `c5_listed_hashes.txt`); all six `.err` files (runs 1–3 and both replays) are the single line `exit 0`
  (`28d3b9e8…`); no `__pycache__`. The quarantine snapshot manifest verifies from `snapshot/` (159/159).
- **Replays.** C5's own: 2/2 byte-identical. Coordinator replays from `pt/C5/` into `pt/audit/C5/replay/`:
  `c1_census` and `c3_countermodels` both IDENTICAL on stdout and stderr (17:30:38Z, 17:30:42Z).
- **Failed runs kept.** `c3_countermodels.run1` (18/24, no verdict): C5's own label convention for the defect
  vectors (s ↔ −s against its `e_s`) and a wrong countercontrol sign (`⟨E0, actC nflip E0⟩` is +1, not −1); both
  caught by its decision rule, corrected for run 2 (24/24); run 3 differs from run 2 in one description line.
  Pre-run edits (two in c3, one in c1) are recorded in NOTES N2–N3 and precede each first run; decision rules
  unchanged after any run.
- **Start/end checks** (NOTES N0, N5): manifests 6/6, `ns.manifest` OK, base HEAD = L with empty porcelain,
  nine protocol prefixes and sidecars OK at both ends.
- **Disclosed deviations** (harmless): one `python3 -c` version check without `-I -B` (wrote nothing); a
  malformed first sweep whose oversized listing the tool runner kept outside `pt/`; redone correctly.

## 2. The anomaly C5 reported — attribution, and the copies inside C5's record

C5's sweep found `pt/PROTOCOL-STAGE6.md`, `pt/PROTOCOL-STAGE6.sha256` and `pt/I1/`–`pt/I4/` (159 files at
17:18:56Z) newer than its marker. **These are the coordinator's stage-6 launch** (the stage-6 protocol and the
four inventory threads), written while stage 5 ran; see `pt/audit/D5/AUDIT-D.md` §2 for the record of the
coordinator's process breach and the lesson. C5 confirmed at 17:47Z that it never opened, displayed or inspected
their contents (names, sizes, mtimes and hashes only). C5 quarantined by copy: `pt/C5/evidence/sweep-20261010T1818Z/
snapshot/` holds byte copies of those 159 files as they stood at 17:18:56–58Z (several were still being written;
21 of the originals changed afterwards). Those copies are the coordinator's and the I-threads' in-progress files,
not evidence for any stage-5 or stage-6 result; per §A.26 they are never adopted as data, and the authoritative
stage-6 records are the frozen `pt/I1/`–`pt/I4/` directories with their own hash lists (verified in
`pt/audit/stage6-inputs/I-audit/`). No C5 result reads any file (its scripts are self-contained), and both
decisive runs finished before the sweep.

## 3. Independent check (`indep_checkC.py`, run 2: 41/44 CONFIRMED; replay identical)

Written from C5's claims, not from its code: Pauli-string commutators with discrete closure by exact conjugation
(and the antiunitary `T` as a sign on each string); projective orbits by BFS on canonical rays; the torus minimum
of `|det|²` taken exactly as the smallest eigenvalue of C5's 2×2 form, not bounded; K(Z_F) rebuilt from the stage-3
defect formula with its states as eigenvectors. Run 1 (kept, `indep_checkC.run1.*`, 33/42) had three errors of
mine, all fixed for run 2 and recorded in the script: `|det|²` normalized by `‖v‖²` instead of `‖v‖⁴`, the Bell
countercontrol taken without its `D`-orbit, and a Rational compared with a Python float in K11.

| C5 claim | check | verdict |
|---|---|---|
| `U_J = (I − i(X+Y+Z))/2` realizes `cyc3`; `cyc3 ∘ rot3 ∘ cyc3⁻¹` = rotations about x; `R_x(π) = nflip`; `rot3(π) = diag(−1,−1,1) ≠ nflip` | T1 | CONFIRMED |
| `CNOT = I⊗P₊ + Z⊗P₋ = I − 2|1−⟩⟨1−|` | T2 | CONFIRMED |
| `|G16| = 16`, `|⟨G16, SWAP⟩| = 48` (projective, `T` antiunitary) | T3 | CONFIRMED |
| census Lie closures, levels (i)/(ii): {flow}@C 2/2, @T 1/1, both 3/3, {flow,NOT} 2/1, {J} and {NOT,J} 0, {flow,J}@C 6/6, @T 6/6, flow@C+J@T 15, flow@T+J@C 1, z-flow @C/@T/both 1/2/3, {z-flow,J} 6/6 | L1–L12 | CONFIRMED (all 12) |
| UNIQUE criterion: `L({flow,J}@C) ⊇ su(2)⊗P±`, `L({flow,J}@T) ⊇ |0⟩⟨0|⊗su(2), |1⟩⟨1|⊗su(2)`; the flow-only node contains neither | U1, U2, U1c | CONFIRMED |
| exact reachability witnesses: an element `U₊⊗P₊ + U₋⊗P₋` carries a product to `ψ₀ = φ₀/4` and to `ψ_a = (15,−1,7,7)/18` | U3, U4 | CONFIRMED (weights √13/4, √3/4 and 7/9, 4√2/9) |
| "φ₀-orbits 768 / 384" for {J} and {NOT,J} | O1–O3 | MISMATCH as printed; **reconciled**: see below |
| `d_low = 5/256` over the full orbits of {J} and {NOT,J}, levels (i) and (ii) | O4, O5, O6 | CONFIRMED (level-(ii) orbits 768, 384) |
| {flow}@C: `|det|²` along `e^{−iβXX}` is a homogeneous form in (cos 2β, sin 2β); `det Q/tr Q` bounds the exact minimum; the bound at the minimizing orbit element is `1/2304`; `α = 499783/500000` admissible | S1, S2, S3 | CONFIRMED (exact minimum `9/128 − √5/32 ≈ 0.00043538`; bound `1/2304 ≈ 0.00043403`) |
| z-flow@T (`N = Z⊗Z`): `d_low = 1/8704` | S4 | CONFIRMED (exact minimum ≈ 0.00011499) |
| stage-4 seeds `4609/4608`, `17409/17408` lie in the windows from the exact minima and from the bounds | S5 | CONFIRMED |
| FLOAT sanity: 20000-point scan never below the exact minimum | S6 | CONFIRMED |
| countercontrol: the reachable Bell state gives minimum 0 | S1c | CONFIRMED |
| every generator of `⟨G16, SWAP⟩` and both NOTs permute Z_F | K1 | CONFIRMED |
| θ: `4⟨prodState(a,b), z_s⟩ = 1 + aᵀM_s b`, `M_s` orthogonal (symbolic) | K2 | CONFIRMED |
| κ: `U(−1) = CNOT`; circles C1, C2 mapped into C1 ∪ C2 by `U(w)`, CNOT, Z⊗I, I⊗Z, T; every point maximally entangled; defect of `C1(1)/√2` is `z_(−1,−1)` | K3 | CONFIRMED |
| κ-cc: at `w = −i` a defect leaves K(Z_F), witness in K(Z_F), pairing −1/2 | K4 | CONFIRMED (overlaps 1/2, 0, 0, 1/2) |
| ζ-1: `D(w)` fixes `x = T(ψ_(1,−1) + ψ_(−1,1))`; the permutation unitary `J` is an automorphism; `J D(−1) J⁻¹` moves `x` | K5 | CONFIRMED |
| ι-cc: `(5,−5,−1,−1)` in Q3 ∩ E0*, pairings 3/13 and −5/13 | K6 | CONFIRMED |
| η-cc: `⟨E0, actT nflip E0⟩ = −1`, `⟨E0, actC nflip E0⟩ = +1` | K7 | CONFIRMED |
| FORM-J: `(U_J⊗I) CNOT (U_J⊗I)† = I⊗P₊ + X⊗P₋`; X and Z have no common eigenvector | K8 | CONFIRMED |
| CL1: `F = z_(−1,−1)` pairs ≥ 0 with products and cnot-images of products (orthogonal forms), `F ∉ Q3`, `F` pairs −1/2 with its own state | K9 | CONFIRMED |
| LAMBDA-tw: `reflY R reflY` is a rotation | K10 | CONFIRMED |
| THETA-cc: `chainW = cnot idW` (K2Guard.lean:104) pairs −1/2 with the sharp effects of −e₁, −e₃; `idW` pairs ≥ 0 with sharp products | K11 | CONFIRMED |

**The orbit counts, reconciled.** My level-(i) ray orbits of φ₀ under `⟨U_J⊗I, CNOT⟩` and `⟨I⊗U_J, CNOT⟩` have
48 rays each (free actions of projective groups of order 48); with the NOT added, 192 each; under the level-(ii)
groups (G16 with `T`, plus J, with or without the NOT) 768 and 384 — C5's figures (O6). C5 confirmed at 17:47Z
that its 768/384 are the level-(ii) orbits (its census computes the seed at level (ii), which also serves level
(i)), that at level (ii) the NOT adds nothing because `U_J Z U_J† = X`, that its canonicalization is the same
rule as mine, and that `d_low` is the minimum over the whole orbit. Its census output lines say `seed@(ii)`; the
RESULT table does not name the level. **Correction to record** (C5's own request, its records being frozen):
the table entry "φ₀-orbits 768 / 384" should read "level-(ii) orbits 768 / 384; level (i) 48 / 48, with the NOT
192 / 192". No verdict changes; `d_low = 5/256` at every level.

## 4. Kernel and record citations

Opened at L and found as cited: CompositeDimension.lean:186 (`maxCone`), :198–202 (`actT`/`actC`), :224–225,
:741–797, :854 (`cnot_relT`), :860 (`cnot_relC`); K2Guard.lean:46 (`reflY`), :95 (`CandidateCone`), :101 (`idW`),
:104 (`chainW`), :134 (`chain_value`); KInfFoundations.lean:264, :284, :411 (`rot3`), :416–425, :449;
TransitiveBody.lean:301; CompletedOI.lean:129, :327, :506; ReferenceExtension.lean:447; LiftAudit.lean:112, :200;
ExecSource.lean:129; ReadWriteControl.lean:174; DerivedQ3.lean:222; FourCopyDefs.lean:49; FourCopyPackage.lean:176,
:180, :183; EQ5-SOURCE-RESULT §3.1–3.3 and the audit's "Anchor sum … Confirmed"; KT4-PREM-1 `result.md` rows;
stage-4 AUDIT-Y (4609/4608, 17409/17408, 5/256 at lines 60, 65, 70) and `pt/S2/RESULT.md:373–380` (K_gen not
self-dual). `ReferenceExtension.lean:507` (`control_not_implies_parallelReferenceExtension`) and
`ReadWriteControl.lean:158` were checked by grep for the names only.

## 5. Assessment of the verdicts

- **The census.** All twelve closure dimensions, the UNIQUE criterion's containments, the exact reachability
  witnesses and every seed value are reproduced from independent code. The two UNIQUE claims are "Q3 given (b)
  for {flow, J}" — C5 says so explicitly (pressure test, §1 C1) — and the criterion's written step (a
  conditioned-control group `{|p⟩⟨p|⊗V + |p⊥⟩⟨p⊥|⊗I}` carries a product to every pure state) is correct: expand
  the target in the target token's `p/p⊥` basis and choose the two control unitaries. The minimal-subset verdict
  stands: among the native single-token operations, only {flow, J} on one token (or the flow on the control with
  J on the target) forces Q3 given (b); every proper subset admits an exotic invariant cone, by exact seed.
- **η, θ, ι, ζ-1, the NOT-only forms: INDEPENDENT by the explicit cone K(Z_F) (EXOTIC-X).** Confirmed (K1, K2,
  K5; stage-3 H1–H3 of K(Z_F) audited at stage 3). θ adds nothing: every K with H1–H3 lies in `maxCone` (`K = K*
  ⊆ SEP* = maxCone`) — a correct written step; θ does not even give H2 (K11 shows `cnot idW ∉ maxCone`).
- **κ: INDEPENDENT (EXOTIC-E), explicit cone UNRESOLVED.** The circle construction is exact (K3); the seed's
  subduality follows because every circle point is maximally entangled (overlap ≤ 1/2 with products) and
  Bell-type defects pair ≥ 0 with each other; existence is by EBF [W, audited AUDIT-X]. K(Z_F) is not
  κ-invariant (K4). Correctly labelled.
- **ζ-2/ζ-3.** Literal pair transitivity is not admissible (Q3 fails it); extreme-ray transitivity (stage 4's T)
  UNRESOLVED. Consistent with stage 4 and with D5.
- **α–δ restricted forms.** NOT-only: K(Z_F) (confirmed). NOT and J: EXOTIC-E over `φ₀` with `d_low = 5/256`
  (O5, O6) and no Bell-type defect (K8's block identity plus the common-eigenvector argument, which is correct:
  the image of `u⊗|+⟩ + v⊗|−⟩` under `(I, W)` is maximally entangled iff `Wv ∥ v`). Finite native groups:
  EXOTIC-E with the same seed; the class of all finite groups is not uniformly independent (stage 4 R1), as C5
  says. Flow only: EXOTIC-E with `1/2304` or `5/256` (S2, O4). Flow and J: forces Q3 — it is (b_DJ).
- **λ without `tok`: INDEPENDENT of (b_min)**, by the anchor sum with uniform K(Z_F) (audited at EQ5-SOURCE);
  `M_ρ`/`M_tw` do not serve because the twin is rotation-invariant on either token (K10 confirms the step
  `reflY R reflY ∈ SO(3)`). Correct, and it sharpens the launch message's own suggestion.
- **C4, the five matrix-level theorems.** Scope statements confirmed by reading: the two spectator no-gos fail on
  the non-completely-positive `Φ₂` of the round-34 countermodel, which has composite unitary control; the three
  availability results are L0/L1 statements. None decides (b) for reversible operations on `W 3`. This matches
  D5's N1e and the stage-6 inventory finding that no theorem at L connects the matrix carrier to `W 3`.
- **Closure picture.** `K_gen` not self-dual (stage 2, re-verified K9); the closures under cnot + drive and
  cnot + J proper and not self-dual (by the seeds); the closure under cnot + drive + J is Q3. Confirmed by the
  census and K9.
- **Exposed facts.** (1) The protocol's "flow through the NOT" is the J-conjugate of the certified `ball3Drive`
  flow, whose own NOT `rot3 π = diag(−1,−1,1)` fixes `z3` and is not `nflip` (T1) — a genuine identification
  gap in the PT construction, consistent with I3's exposed fact 3. (2) The mixed-placement asymmetry (L9: 15;
  L10: 1). (3) `M_ρ`/`M_tw` satisfy (b). (4) Matrix sufficiency of one layer flow does not transfer to `W 3`.

## 6. Wording items (no result changes)

1. The census table's orbit counts: state the level (C5's correction above).
2. "The NOT adds nothing" holds at level (ii); at level (i) the NOT enlarges the orbit (48 → 192) without
   changing `d_low`.
3. The RESULT cites `ReferenceExtension.lean:507` for `control_not_implies_parallelReferenceExtension`; the
   statement is at the line the name resolves to (grep), consistent.
4. C5's `d_low` values are lower bounds (`det Q/tr Q`), below the exact minima by under 0.4 %; the text calls
   them "the minimum over the orbit" of the bound, which is right as stated in the script header but reads as
   the exact minimum in the table. Say "certified lower bound".

## 7. Verdict

C5's results stand as stated, with the orbit-count level correction recorded. Bands unchanged (consistency-axis
work; no certified label changes).

**Files (sha256).** `indep_checkC.py`, `.out`, `.err` and the replay pair are listed in the stage-5 archive
manifest; run 1 kept as `indep_checkC.run1.{py,out,err}`; `replay/REPLAY-LOG.txt` with both replay pairs;
`c5_listed_hashes.txt` (16 lines, all OK).
