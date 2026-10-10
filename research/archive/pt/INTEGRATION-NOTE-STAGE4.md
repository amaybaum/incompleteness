# Stage-4 integration note — the EXOTIC exclusion theorem and the minimum additional condition, Q-EX (research only; L = `9f9f8257`)

Written by the coordinator after auditing threads Y (`pt/Y/`, exclusion) and Z (`pt/Z/`, countermodels).
Governing texts: `PROTOCOL-STAGE4.md` (`d3da2811…`) and the stage-1/2/3 protocols it names; the owner's notes 5 and
6 (`pt/audit/stage4-inputs/`) fix the verdict table's structure and the precision on the discrete element. Holds
unchanged: no repository change, branch, PR, CI run, governed round or publication. Evidence levels as in the
protocols: [K] certified at L, [D] design module, [W] written argument, [X] exact computation, [N] numerical,
[L] unverified literature. Labels for "K = Q3" follow amendment 2 (DERIVED / CONDITIONAL / INDEPENDENT /
UNRESOLVED). EXOTIC-X: an exact cone exhibited; EXOTIC-E: existence by EBF over a seed exhibited exactly.

## 0. Bottom line

**The owner's five questions (note 5), answered on the audited evidence.**

| question | verdict | evidence |
|---|---|---|
| Does full local plus CNOT exclude EXOTIC? | **Yes.** Every closed `K` with H1–H3 that is invariant under the rotations of one token (S4-C or S4-T) equals `Q3`; every stage-3 countermodel leaves itself under a single rotation, with exact witnesses. The connected subgroup `{U⊗P₊ + V⊗P₋}` alone carries the proof; the discrete element CNOT contributes belongs to the group census only (note 6). | Y2 [W + X]; pre-audit C, D; `indep_checkY` R5, R7 |
| Does it uniquely select the quantum cone? | **Yes, CONDITIONAL** on the composite action (b) and on trace self-duality H3. Nothing weaker than (b) is used; nothing at L supplies (b). | Y2, Y O; AUDIT-Y §4 |
| Is it the weakest sufficient condition? | **Among the protocol's fixed nodes, yes.** S4-C and S4-T are minimal: every strictly weaker fixed node has an audited countermodel (S0 and S1 explicitly with `K(Z_F)`; S2, S3 and the finite extensions explicitly or by existence over exact seeds). **In the refined lattice, no:** cnot plus one generic one-parameter local rotation group (an axis off the native frame's coordinate axes; Y's S3[n], Z's S3-g) is UNIQUE, and so is cnot plus a single order-3 rotation about (5,1,1) (Y's R1), whose only proper sub-extension is EXOTIC-X. H is UNIQUE with minimality UNRESOLVED. | Y3, Y4, Y5, Y7; Z z1–z5 [W + X] |
| Is the condition observer-native? | **Not derived at L.** (b), "rotations act on a token inside an arbitrary entangled pair preserving the pair cone", is INDEPENDENT of the certified pair premises plus self-duality: the stage-3 cones satisfy H1–H3 and violate it. (a), "an isolated token admits all rotations", is a body symmetry at L whose operational availability is itself unsourced (K∞-Act, K∞-Drive, K∞-Trans OPEN), and (a) does not give (b). The corpus records the same gap (the K2 obligation "local actions compatible with the composite cone" OPEN; idle extension of local operations "is IE1 itself", unsourced). | Y O [K + W + X]; AUDIT-Y §4 |
| Does it establish general quantum equivalence? | **No.** The theorem is a uniqueness statement for the certified two-qubit pair carrier `W 3`, CONDITIONAL on (b) or on H; no carrier beyond the pair, no derivation of (b), and nothing on the four-token route (OVL4) is claimed. | Y §3; Z §3; stage-3 note §3 |

**The lattice.**

| node | principle P added to H1–H3 | verdict | exact evidence |
|---|---|---|---|
| S0 | `G16` | EXOTIC-X | stage 3: `K(Z_F)`; re-checked by Z |
| S1 | + `SWAP` | EXOTIC-X: `K(Z_F)` is `SWAP`-invariant; its full stabilizer among unitary and antiunitary conjugations is a 3-torus (unitaries diagonal in the four Bell-type states) by `S4 × Z2`, with `⟨G16, SWAP⟩` (order 48) a complement | Z z1; coordinator P1; Y5 (seed) |
| S2 | + torus `actC Rz ∘ actT Rx` | EXOTIC-E: Bell-type seeds exactly the two circles `C1 ∪ C2` through the four stage-3 defects; also for the 3-torus of all product-diagonal unitaries. **Explicit cone UNRESOLVED:** the only `G16 ⋊ T²`-invariant Bell-type surgery is not self-dual (exact pair, pairing −24/625); no finite surgery can serve this node | Z z2c, z2e; Y5 C2; coordinator K1–K6c, P2–P3 |
| S3 | + `actC Rx(θ)` | EXOTIC-E with exact seeds (Y: cap c = 4609/4608; Z: `α = 7/8` at `ψ_a = (15,−1,7,7)/18`); no Bell-type defect exists, so the protocol's second criterion is silent and the dichotomy decides | Y4; Z z3; coordinator C1–C6c, S1–S6c |
| S4-C, S4-T | + `actC SO(3)` or `actT SO(3)` | **UNIQUE**; "K = Q3" CONDITIONAL on (b) | Y2; pre-audit |
| S5 | + all local rotations (IE1) | UNIQUE; CONDITIONAL on IE1; not minimal | Y2, Y3 |
| finite extensions | subgroups of `Stab_Cl(Z_F)` (order 1536; among them LPT 64, LPT + SWAP 192) | EXOTIC-X with `K(Z_F)` | Z z1, z4; coordinator P6, G2 |
| | `G_S = ⟨G16, Ad(S⊗I)⟩` (32); `G_H = ⟨G16, Ad(I⊗H)⟩` (128); the Clifford group with the transpose (23040); `G16` + one-token Clifford (1536 / 768) | EXOTIC-E, one seed for all (`ψ_a`: `α = 9/10` for `G_H`, `99/100` for the Clifford group; Y: cap c = 517/512 at `φ₀ = (1,2,3i,−1+i)`); every finite group is EXOTIC-E | Z z4; Y5; coordinator G1–G8, F1–F6c |
| H | homogeneity | UNIQUE [W + X + K + L]; CONDITIONAL on H and on Koecher–Vinberg + Jordan–von Neumann–Wigner [L]; minimality UNRESOLVED | Y6 |
| T | Aut(K) transitive on extreme rays | EXCLUDES-KNOWN (invariant c = 15 on defects, 9 on products); EXCLUDES-ALL UNRESOLVED | Y6; coordinator S1–S3 |
| F | perfectness | `K(E0)` fails F; EXCLUDES-ALL UNRESOLVED | Y6; coordinator S4 |
| V | `K ∩ V+ = Q3 ∩ V+` | not a selector (record) | stage 3 |
| C | OVL4 | not tested (record) | — |
| record S3[n] | one rotation subgroup of one token about axis n | UNIQUE iff n is off the native frame's coordinate axes (level (ii); at level (i) iff n is neither parallel nor perpendicular to the frame's gate axis); the coordinate axes EXOTIC-E | Y3, Y4; Z z5; coordinator A1–A4, Z-A1–A3c |
| record drive | the native drive through the NOT, one or both tokens | EXOTIC-E (on the exceptional set) | Y4 |
| record R1 | one order-3 rotation about (5,1,1), cnot only | UNIQUE [W + X]; its only proper sub-extension (cnot alone) EXOTIC-X | Y7; coordinator R1–R7 |

**Audit status.** Y: replays 8/8; independent checks 28/28 and 6/6; 22/22 hashes; proofs reviewed with no gap
(`pt/audit/Y/AUDIT-Y.md`). Z: replays 9/9; independent check 29/29; pre-audit 9/9; 26/26 hashes; proofs reviewed
with one [W] extrapolation narrowed to level (i) (`pt/audit/Z/AUDIT-Z.md`). Every independent check was written
without the threads' code, replayed byte-identically, and keeps its failed runs with the reasons (all harness
errors of the coordinator's own). The two threads never read each other and converged on the same exclusion
theorem, the same axis dependence of S3, and the same verdict at every shared node.

**The exclusion theorem (Y1 = Z's claim D, [W + X]).** For a closed `K` with H1–H3 and any compact group `Ĝ` of
unitary or antiunitary conjugations containing `cnot`: if `Ĝ·SEP` is every pure state then every `Ĝ`-invariant
such `K` is `Q3`; if some pure state `φ₀` is unreachable then an exotic `Ĝ`-invariant `K` exists, seeded by the
defect `(I − cφ₀φ₀†)/8` with `1 < c ≤ min(2, 1/m)`, `m` the largest overlap of `φ₀` with the compact reachable set
(Z's form `αE00 − T_ψ/4`, `α = 1/c`). The protocol's Bell-type criterion is the case c = 2; the zone the protocol left
open is empty, and it is exotic (S3 lies in it). Consequences: every finite symmetry group, and every compact one of
dimension ≤ 1, is EXOTIC-E; UNIQUE needs dimension ≥ 2; reachability alone decides every symmetry node.

**Route verdicts.**
- "H1–H3 plus a finite symmetry extension of `G16` ⇒ `Q3`": refuted for every finite group [W], with explicit
  cones for the stabilizer subgroups and exact seeds elsewhere [X]. The protocol's conjecture "no finite group
  containing `G16` excludes all Bell-type defects" is refuted: `G_H` (order 128) and the Clifford group admit none
  and are exotic nonetheless.
- "H1–H3 plus the native drive ⇒ `Q3`": refuted; the NOT's axis lies on the exceptional set (EXOTIC-E, exact seeds).
- "H1–H3 plus one generic local rotation subgroup ⇒ `Q3`": holds (S3[n] off-frame; R1 for one order-3 rotation).
- "An explicit torus-invariant exotic cone by surgery": refuted for every Bell-type surgery and every finite
  surgery; existence stands; the explicit cone is UNRESOLVED.

## 1. The theorem and why it is hard to vary

- **Fixed in advance.** The two criteria were stated in the protocol before either thread ran; the coordinator's
  pre-audits (`PRE-AUDIT-QEX.md`, 14:47Z, 15/15; `PRE-AUDIT-Z.md`, 15:52Z, 9/9) fixed the CNOT decomposition, the
  Lie closure, six reachability instances, the exact exit of both stage-3 cones under one rotation, `SWAP` and the
  local Paulis permuting the Bell-type defects, and the exit of a defect under the control Hadamard, before Y or Z
  reported.
- **Controls.** `Q3` passes every retention test; every stage-3 cone fails every exclusion claimed; every certificate
  fails on reachable states and on the oblique group; the cap window is sharp; the pair obstruction vanishes exactly
  at the Bell boundary c = 1/2 and is positive beyond it; members of the refuted surgery pair nonnegatively with its
  dual witnesses.
- **Predictions beyond the problem, written before their checks.** Y's full axis classification (confirmed by y3 and
  by Z's independent z5); EXOTIC-E for the native drive (Y4); UNIQUE for a single off-frame order-3 rotation (Y7,
  after a pressure test of the favourable branch); Z's prediction that S3 is exotic although no Bell-type defect
  exists (confirmed by an exact seed) and that the Clifford group has no Bell-type defect yet is exotic (confirmed).
- **Exposed assumptions (gem-finding).** The protocol's S3 sketch holds only on the exceptional axis set; "finite
  extension" must mean a finite group; the literal pair transfer of `BoundaryTransitive` fails for `Q3` itself, so H
  is not the pair analogue of TRB-1's premise and T is; stage 3's [N] guidance on the torus surgery never sampled
  the cross-defect elements that break it.
- **Convergence.** Two threads that never read each other derived the same dichotomy and the same axis dependence,
  and their shared nodes carry the same verdicts with different exact seeds.

## 2. Countermodels (thread Z, audited)

- **Explicit.** `K(Z_F)` serves every node whose group stabilizes the four Bell-type defects: `SWAP` (its orbit is
  permuted), the local Paulis, and every subgroup of the order-1536 stabilizer inside the Clifford group. Its full
  symmetry group among unitary and antiunitary conjugations is exactly the monomial unitaries in the Bell-type
  basis: a 3-torus by `S4 × Z2`; no one-parameter group of local maps preserves it.
- **Existence with exact seeds.** S2 (the two circles of Bell-type seeds, proved over the whole reachable set), S3
  (`ψ_a`, `α = 7/8`), the target-z variant (`(7,4,0,4)/9`, `α = 24/25`), `G_S` (a Bell seed with a non-orthogonal
  orbit of eight), `G_H` (`α = 9/10`) and the Clifford group (`α = 99/100`).
- **Obstructions.** Two Bell-type defects at squared overlap in (0, 1/2) never give a self-dual surgery
  (`tr(yw) = c − 1/(4c)`); the two-circle surgery `K_T` for S2 fails by an exact pair; a plain surgery over two
  generalized seeds fails even for orthogonal states; every exotic torus-invariant cone contains a continuous family
  of non-PSD elements, so no finite surgery can serve S2.
- **Correction applied in audit.** Z's extrapolation of EXOTIC-E to every equatorial control axis and every target
  axis perpendicular to the gate axis holds at level (i) only; with `G16`, whose transpose and `Ad(I⊗Z)` move a
  non-coordinate axis to a non-parallel image, those nodes are UNIQUE and only the coordinate axes stay exceptional
  (Y3; `indep_checkZ` A2). Z's exact verdicts are unaffected.

## 3. Provenance, and what remains

**The precise additional freedom.** Given H1–H3, what makes `Q3` unique is (b) for one local rotation subgroup of
one token placed off the native frame's coordinate axes, or for a single off-frame rotation of finite order (R1),
or the full rotation group of one token (S4), or structurally H. The drive the corpus attaches to the NOT (`nflip`,
axis x; corner axis `z3`) lies exactly on the exceptional set: its idle extension does not force `Q3`. Idle extension
of the drive together with its off-axis conjugate (`J_off_axis` of `ElementaryDrivability`, KInfFoundations.lean:264,
276) contains S4 and does.

**Whether embedded observation demands (b): UNRESOLVED at L.** No premise at L supplies it; the exact countermodels
show that the certified pair premises with self-duality do not; the corpus records the gap (ROADMAP.md:68,
1001–1005, 1014–1022; KT4-PREM-1 result.md:171–172, 243; EQ2-SYNTHESIS.md:161–167;
`control_not_implies_parallelReferenceExtension`, ReferenceExtension.lean:507; `oiPlus_independence`,
CompletedOI.lean:506). Label: "K = Q3" CONDITIONAL on (b) for the node's group; (b) INDEPENDENT of H1–H3 at L; not a
restatement (SEP and maxCone satisfy it; `K_gen` and the exotic cones do not).

**Open residuals, named (nothing launched; for the owner's decision).**
1. Whether (b), for one off-frame rotation of one token, follows from an observer-native principle not yet at L.
   This is the question the owner's note 5 names, and the one the audited evidence sharpens: the freedom needed is
   small (one generic one-parameter local rotation, or one off-frame rotation of order 3) and is exactly what the
   native drive lacks.
2. An explicit torus-invariant exotic cone (S2): non-surgery constructions, or surgeries over non-Bell seeds with
   larger orbits; the obstruction is named.
3. T and F as exclusions of every exotic cone (decided only for `K(E0)`, `K(Z_F)`); H's minimality; the quarter-turn's
   square in R1's family; the target-axis analogue of R1.
4. The Origin targets (Priority 2) remain queued and unchanged.

## 4. Evidence log

- Y (`pt/Y/`): scripts y1–y7, y7x with `.out/.err` and `.replay.*`; hashes in `RESULT.md` §4 (`991b01a8…`; 22/22
  verified); coordinator's replays `pt/audit/Y/replay/` (invalid, kept) and `replay2/` (8/8 identical);
  `pt/audit/Y/indep_checkY.py` (28/28, run 1 kept), `indep_checkY5.py` (6/6, run 1 kept), both replayed identically;
  `pt/audit/Y/AUDIT-Y.md` (`a4d12a39…`); pre-audit `PRE-AUDIT-QEX.md` (`34a0909f…`) with `indep_checkQEX.py`
  (15/15, run 1 kept).
- Z (`pt/Z/`): scripts z1, z2a–z2e, z3, z4, z5 with `.out/.err` and `.replay.*`, kept failed runs `z1_swap.run1.*`
  and `z2e_s2_surgery.run1.*`; hashes in `RESULT.md` §4 (`dca18d91…`; 26/26 verified); coordinator's replays
  `pt/audit/Z/replay/` (9/9 identical, `REPLAY-LOG.txt` `0d8dd2db…`); `pt/audit/Z/preaudit_z.py` (9/9, runs 1–2
  kept) with `PRE-AUDIT-Z.md` (`09a11780…`); `pt/audit/Z/indep_checkZ.py` (29/29, run 1 kept), replayed
  identically; `pt/audit/Z/AUDIT-Z.md` (`4be00ec5…`).
- Owner's notes: `pt/audit/stage4-inputs/OWNER-NOTE5-STAGE4-PROVENANCE.md` (`e501aff8…`, with the coordinator's
  erratum), `OWNER-NOTE6-STAGE4-DISCRETE.md` (`740d23b7…`), `qex_owner_note6.py` (`7760197e…`, 5/5, replay
  identical). Protocol: `pt/PROTOCOL-STAGE4.md` (`d3da2811…`), frozen at launch; the erratum and the owner's
  requirement reached the threads by message and are recorded verbatim in both NOTES (Y N2, Z N1).
- Archive: `evidence/pt-stage4-evidence.tar.gz` with `evidence/stage4.manifest.sha256`, built by
  `drafts/build_stage4_evidence.sh` (deterministic); hashes in the final report.

## 5. Integrity

Both threads started with `.start_marker` (Y 14:24:15Z, Z 14:24:43Z), verified the six manifests, the base HEAD
`9f9f8257…` with empty porcelain, the protocol hashes and sidecars, and found no bytecode; each swept `pt/` and found
only the sibling's directory (names only). Neither read `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/reviews/`,
`pt/audit/aborted-launches/` or the sibling thread. Coordinator's writes during the threads' runs: `pt/audit/` only
(the pre-audit records, the owner's notes, the Y audit area). Corrections of the coordinator's own: the protocol's
CNOT decomposition (owner's note 5, transmitted); "eight protocol hashes" for seven in the launch message (harmless,
both threads checked what exists). Holds: no git write, branch, PR, CI, network, publication.
