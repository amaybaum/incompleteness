# Stage-4 integration note — the EXOTIC exclusion theorem and the minimum additional condition, Q-EX (research only; L = `9f9f8257`)

[DRAFT written while thread Z runs; every item marked [Z: pending] is filled from Z's audited record before this
note is final. Y's content is final as audited in `pt/audit/Y/AUDIT-Y.md`.]

Written by the coordinator after auditing threads Y (`pt/Y/`, exclusion) and Z (`pt/Z/`, countermodels).
Governing texts: `PROTOCOL-STAGE4.md` (`d3da2811…`) and the stage-1/2/3 protocols it names; the owner's notes 5 and
6 (`pt/audit/stage4-inputs/`) fix the verdict table's structure and the precision on the discrete element. Holds
unchanged: no repository change, branch, PR, CI run, governed round or publication. Evidence levels as in the
protocols: [K] certified at L, [D] design module, [W] written argument, [X] exact computation, [N] numerical,
[L] unverified literature. Labels for "K = Q3" follow amendment 2 (DERIVED / CONDITIONAL / INDEPENDENT /
UNRESOLVED).

## 0. Bottom line

**The owner's five questions (note 5), answered on the audited evidence.**

| question | verdict | evidence |
|---|---|---|
| Does full local plus CNOT exclude EXOTIC? | **Yes.** Every closed `K` with H1–H3 that is invariant under the rotations of one token (S4-C or S4-T) equals `Q3`; every stage-3 countermodel leaves itself under a single rotation (exact witnesses). The connected subgroup `{U⊗P₊ + V⊗P₋}` alone carries the proof; the discrete element CNOT contributes belongs to the group census only (note 6). | Y2 [W + X]; coordinator's pre-audit C, D and `indep_checkY` R5, R7 |
| Does it uniquely select the quantum cone? | **Yes, CONDITIONAL** on the composite action (b) and on trace self-duality H3. Nothing weaker than (b) is used; nothing at L supplies (b). | Y2, O; AUDIT-Y §4 |
| Is it the weakest sufficient condition? | **Among the protocol's fixed nodes, yes** (S4-C and S4-T are minimal: S0, S3, the finite extensions and the drive are EXOTIC with exact seeds). **In the refined lattice, no:** one rotation subgroup of one token about an axis off the native frame's coordinate axes (S3[n]) suffices, and so does a single order-3 rotation about (5,1,1) (R1). Minimality is supported by countermodels for each weakening: [Z: pending — explicit cones / EBF seeds for S1, S2, S3, the finite extensions]. H is UNIQUE but its minimality is UNRESOLVED (T and F decided only for the known cones). | Y3, Y4, Y5, Y7 [W + X]; Z [Z: pending] |
| Is the condition observer-native? | **Not derived at L.** (b), "rotations act on a token inside an arbitrary entangled pair preserving the pair cone", is INDEPENDENT of the certified pair premises plus self-duality: the stage-3 cones satisfy H1–H3 and violate it. (a), "an isolated token admits all rotations", is a body symmetry at L whose operational availability is itself unsourced (K∞-Act, K∞-Drive, K∞-Trans OPEN); (a) does not give (b). The corpus records the same gap (K2 obligation OPEN; idle extension of local operations "is IE1 itself", unsourced). | O [K + W + X]; AUDIT-Y §4 |
| Does it establish general quantum equivalence? | **No.** The theorem is a uniqueness statement for the certified two-qubit pair carrier `W 3`, CONDITIONAL on (b) or on H; no carrier beyond the pair, no derivation of (b), and nothing on the four-token route (OVL4) is claimed. | Y §3; stage-3 note §3 |

**The lattice.** (EXOTIC-X: an exact cone exhibited; EXOTIC-E: existence by EBF with the seed exact.)

| node | principle P added to H1–H3 | verdict | exact evidence |
|---|---|---|---|
| S0 | `G16` | EXOTIC-X | stage 3: `K(Z_F)` |
| S1 | + `SWAP` | [Z: pending; Y: EXOTIC-E, seed c = 517/512] | Y5; Z [pending] |
| S2 | + torus `actC Rz ∘ actT Rx` | [Z: pending; Y: EXOTIC-E, reachable set `G16·SEP`] | Y5; Z [pending] |
| S3 | + `actC Rx(θ)` | EXOTIC-E (exact certificate, c = 4609/4608; the Bell-type route provably unavailable) [Z: pending] | Y4; Z [pending] |
| S4-C, S4-T | + `actC SO(3)` or `actT SO(3)` | **UNIQUE**; "K = Q3" CONDITIONAL on (b) | Y2 |
| S5 | + all local rotations (IE1) | UNIQUE; CONDITIONAL on IE1; not minimal | Y2, Y3 |
| finite extensions | LPT (64), LPT + SWAP (192), `G16` + one-token Clifford (1536 / 768), Clifford + T (23040) | EXOTIC-E, one seed for all (d_min = 5/256) [Z: pending] | Y5; Z [pending] |
| H | homogeneity | UNIQUE [W + X + K + L]; CONDITIONAL on H and on Koecher–Vinberg + JvNW [L]; minimality UNRESOLVED | Y6 |
| T | Aut(K) transitive on extreme rays | EXCLUDES-KNOWN (invariant c = 15 on defects, 9 on products); EXCLUDES-ALL UNRESOLVED | Y6 |
| F | perfectness | `K(E0)` fails F; EXCLUDES-ALL UNRESOLVED | Y6 |
| V | `K ∩ V+ = Q3 ∩ V+` | not a selector (record) | stage 3 |
| C | OVL4 | not tested (record) | — |
| record S3[n] | one rotation subgroup of one token about axis n | UNIQUE iff n is off the native frame's coordinate axes (level (ii)); the coordinate axes EXOTIC-E | Y3, Y4 |
| record drive | the native drive through the NOT, one or both tokens | EXOTIC-E (on the exceptional set) | Y4 |
| record R1 | one order-3 rotation about (5,1,1), cnot only | UNIQUE [W + X]; its only proper sub-extension (cnot alone) EXOTIC-X | Y7 |

**Audit status.** Y: replays 8/8 byte-identical (coordinator's attempt 1 invalid by a missing `/usr/bin/time`,
kept; attempt 2 identical); independent checks `indep_checkY.py` 28/28 and `indep_checkY5.py` 6/6, written
without Y's code, replayed identically (run 1s kept, harness errors of the coordinator's own); 22/22 hashes;
proofs reviewed with no gap found (AUDIT-Y §4). Z: [Z: pending].

**The exclusion theorem (Y1, [W + X]).** For a closed `K` with H1–H3 and any compact group `Ĝ` of unitary or
antiunitary conjugations containing `cnot`: `K` is `Ĝ`-invariant only if either `Ĝ·SEP` is every pure state, in
which case `K = Q3`, or some pure state `φ₀` is unreachable, in which case an exotic `Ĝ`-invariant `K` exists
(cap defect `e = (I − cφ₀φ₀†)/8`, `1 < c ≤ min(2, 1/m)`, `m` the largest overlap of `φ₀` with the compact
reachable set; EBF). The protocol's Bell-type criterion is the case c = 2; the zone the protocol left open is
empty. Consequences: every finite symmetry group, and every compact one of dimension ≤ 1, is EXOTIC-E; UNIQUE needs
dimension ≥ 2.

**Route verdicts.** "H1–H3 plus a finite symmetry extension of `G16` ⇒ `Q3`" is refuted for every finite group
(dimension count) [W], with the explicit seed `φ₀ = (1, 2, 3i, −1+i)` entangled under all 23040 Clifford-with-transpose
images [X]. "H1–H3 plus the native drive ⇒ `Q3`" is refuted: the NOT's axis is on the exceptional set (EXOTIC-E,
exact). "H1–H3 plus one generic local rotation subgroup ⇒ `Q3`" holds (S3[n]). [Z: pending — explicit-cone
refutations and the finite-extension conjecture.]

## 1. The theorem and why it is hard to vary

- **Fixed in advance.** The two criteria were stated in the protocol before either thread ran; the coordinator's
  pre-audit (`PRE-AUDIT-QEX.md`, 14:47Z, 15/15) fixed the CNOT decomposition, the Lie closure, six reachability
  instances and the exact exit of both stage-3 cones under one rotation before Y or Z reported.
- **Controls.** `Q3` passes every retention test (Y2 Q1, Y3 Q1, H4, T4, F2); every stage-3 cone fails every
  exclusion claimed (K1–K2, Y3, Y7); every certificate fails on reachable states (y4 cc1, y5 cc, `indep_checkY`
  C6c, F6c) and on the oblique group (y4 cc3); the cap window is sharp (c = 1 and c = 5/2 countercontrols).
- **Predictions beyond the problem, written before their checks.** The full axis classification (NOTES N5, confirmed
  by y3 22/22 and `indep_checkY` A1–A4); EXOTIC-E for the native drive on both tokens (N6, y4); UNIQUE for a single
  off-frame order-3 rotation (N7–N8, after a pressure test of the favourable branch; y7 run 2, `indep_checkY` R5,
  R7).
- **Exposed assumptions (gem-finding).** The protocol's S3 sketch holds only on the exceptional axis set; "finite
  extension" must mean a finite group, since one extra element of finite order can generate an infinite group with
  cnot; the literal pair transfer of `BoundaryTransitive` fails for `Q3` itself (rank-2 states are non-extreme
  boundary points), so H is not the pair analogue of TRB-1's premise and T is.

## 2. Countermodels (thread Z)

[Z: pending — the explicit cones or exact seeds per node; the torus-invariant cone; the finite-extension
conjecture; Z's controls; what Z does not claim.]

## 3. Provenance, and what remains

**The precise additional freedom.** Given H1–H3, what makes `Q3` unique is (b) for one local rotation of one
token placed off the native frame's coordinate axes (S3[n] off-frame; R1 for a single order-3 rotation), or the
full rotation group of one token (S4), or structurally H. The drive the corpus attaches to the NOT (`nflip`, axis x;
corner axis `z3`) lies exactly on the exceptional set: its idle extension does not force `Q3`. Idle extension of the
drive together with its off-axis conjugate (`J_off_axis`, `ElementaryDrivability`, KInfFoundations.lean:264, 276)
contains S4 and does.

**Whether embedded observation demands (b): UNRESOLVED at L.** No premise at L supplies it; the exact countermodels
show the certified pair premises with self-duality do not; the corpus already records the gap (ROADMAP.md:68,
1001–1005, 1014–1022; KT4-PREM-1 result.md:171–172, 243; EQ2-SYNTHESIS.md:161–167; the kernel results
`control_not_implies_parallelReferenceExtension` (ReferenceExtension.lean:507) and `oiPlus_independence`
(CompletedOI.lean:506)). Label: "K = Q3" CONDITIONAL on (b) for the node's group; (b) INDEPENDENT of H1–H3 at L;
not a restatement (SEP and maxCone satisfy it, `K_gen` and the exotic cones do not).

**Open residuals, named.** T and F as exclusions of every exotic cone (decided only for `K(E0)`, `K(Z_F)`);
H's minimality; the quarter-turn's square in R1's family; explicit cones for the EXOTIC-E nodes [Z: pending];
whether (b) follows from any observer-native principle not yet at L (the next stage's question, for the owner's
decision; nothing launched).

## 4. Evidence log

Y: scripts y1–y7, y7x under `pt/Y/` with `.out/.err` and `.replay.*`; hashes in `pt/Y/RESULT.md` §4 (22/22
verified); coordinator's replays `pt/audit/Y/replay/` (invalid, kept) and `replay2/` (8/8 identical);
`pt/audit/Y/indep_checkY.py` (28/28, run 1 kept), `indep_checkY5.py` (6/6, run 1 kept), both replayed identically;
`pt/audit/Y/AUDIT-Y.md` (`a4d12a39…`); pre-audit `PRE-AUDIT-QEX.md` with `indep_checkQEX.py` (15/15, run 1 kept).
Owner's notes: `pt/audit/stage4-inputs/OWNER-NOTE5-STAGE4-PROVENANCE.md` (`e501aff8…`),
`OWNER-NOTE6-STAGE4-DISCRETE.md` (`740d23b7…`), `qex_owner_note6.py` (5/5, replay identical).
Z: [Z: pending].

## 5. Integrity

Both threads started with `.start_marker`, verified the six manifests, the base HEAD `9f9f8257…` with empty
porcelain, the seven protocol hashes and sidecars, and found no bytecode; each swept `pt/` and found only the
sibling's directory (names only). Neither read `pt/audit/stage3-inputs/OWNER-*`, `pt/audit/reviews/`,
`pt/audit/aborted-launches/` or the sibling thread. Coordinator's writes during the threads' runs: `pt/audit/`
only. [Z: pending — Z's integrity record.] Holds: no git write, branch, PR, CI, network, publication.
