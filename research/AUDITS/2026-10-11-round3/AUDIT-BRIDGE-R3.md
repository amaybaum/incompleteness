# Coordinator audit — `research/bridge`, round 3

Thread head `7abe4da4` (2026-10-11; round-3 commits `0ccc1bef` … `7abe4da4`). Base L = `9f9f8257`. Audited: the
round-3 rows of `RESULTS.md` (B10-1 … B10-7; B11-1, B11-2; B12-1 … B12-5; B13-1, B13-2; the standing verdict V-3),
`NOTES-B10.md` … `NOTES-B13.md`, `experiments/b10_transfer`, `b11_preflight`, `b12_stagecross`, `b12_followup`,
`b13_preflight`, the design modules `lean/BridgeDictionary.lean` (round 3; the round-2 draft kept beside it) and
`lean/BridgeReach.lean`, the receipts in `inbox/`, the handoff proposals HP-7 … HP-10, `LOG.md`.

## Method

1. **Receipts.** HO-9 v1, HO-13 v1 and HO-16 v1 copied verbatim (sha256 `4b2c4a0f…`, `1d2c884c…`, `bd5a7af3…`, each
   equal to the overview file at `2a055180`, re-checked by the coordinator) and committed at `0ccc1bef`, with the
   reliance recorded in `LOG.md`: HO-9 item 3 in B12 at CONDITIONAL and item 6 as a constraint, items 1, 4, 5 as
   context; HO-13 item 2 as B10's target (the trace, infinite order and irrationality of `R_z(θ₀)` recomputed in the
   thread's own scripts), item 1 only for what the conjunction forces, item 3 as context; HO-16 as context. The four
   kernel declarations the handoffs name were re-read at L before use. Protocol satisfied.
2. **Replay.** Five scripts re-run (`python3 -I -B`, cwd `experiments/`): stdout IDENTICAL 5/5
   (`bridge/replay3/REPLAY-LOG.txt`). The thread's own closing replay found two scripts first run without `-I -B` and
   re-ran them with the flags, byte-identical; the coordinator's replays all used the flags.
3. **Independent check.** `bridge/indep_checkB3.py` (own code; the kernel's gate, action, NOT and rotation definitions
   transcribed from L; own Gaussian-rational and `Q(√5)` arithmetic; reads nothing from the thread; decision rule fixed
   before the first run): run 2 **4/4 CONFIRMED**, `INDEP-B3-FIXED`, replay identical. Run 1 (kept) scored 2/4 through
   two defects of the coordinator's harness (a structural rather than simplified comparison of two sympy matrices; a
   sign error in the explicit second column of a 2×2 unitary); every other sub-assertion held in run 1 and no thread
   claim was involved.
   - X1 (B11, against the kernel's own definitions): the kernel's `cnotFun` (`sgn`, `pc`, `pt`, CompositeDimension.lean
     :741–:758) equals `Ad(CNOT)` through the dictionary on all 16 basis tables and is an involution; `actT (rotZ c s)`
     and `actC (rotZ c s)` (`homMap` :112, `actT` :198, `actC` :201) equal `Ad(1 ⊗ diag(1, c + is))` and
     `Ad(diag ⊗ 1)` at the circle points `(3/5, 4/5)`, `(−5/13, 12/13)` and symbolically on `c² + s² = 1`; the kernel's
     `nflip = diag(1, −1, −1)` (:797) gives `Ad(1 ⊗ X)` and `Ad(X ⊗ 1)`; at `(0, 0)` the phase conjugation does not fix
     `σ₀`; `pauliW(prodState x y) = ρ(x) ⊗ ρ(y)`.
   - X2 (B10): `nflip` on either token permutes `Z_F` and is a signed permutation of the sixteen coordinates (T1);
     `R_z(π)` on the target permutes `Z_F` and pairs nonnegatively with the coordinator's certified members of K(Z_F)
     (T6); `actT R_z(θ₀)` carries defects of `Z_F` to tables pairing negatively with certified members (48 negative
     pairings in the coordinator's pool, e.g. `−4/5`), so K(Z_F) is not invariant — the content of T4 (B4's value
     `−2/5` is not recomputed: it needs B4's effect, audited in round 1); `6/5` is not an algebraic integer;
     `tr(actT R_z(θ₀)) = 64/5` on `W 3` and `16/5` on `HVec 3`, `tr(cnot ∘ actT R_z(θ₀)) = 16/5` (T7, U4); the
     monomial groups `G_n` have orders 16, 64, 256, 1024 modulo phase with `G_n ≤ G_{n+1}` (T8); the Lie closure of
     `{1 ⊗ Z}` under `Ad(CNOT)`, `Ad(1 ⊗ X)` and commutators has dimension 2 and is abelian (`span{1⊗Z, Z⊗Z}`), and
     with `Ad(1 ⊗ U_J)` dimension 6 = `span{1⊗X, 1⊗Y, 1⊗Z, Z⊗X, Z⊗Y, Z⊗Z}`, non-abelian, every element commuting with
     `Z ⊗ 1` (T9, U6); the 3-4-5 rotation's Bloch image is a rotation about `y` with trace `11/25` (T10).
   - X3 (B12): as signed permutations of the table coordinates, `⟨cnot, actT J⟩` has order 48 with integer traces
     `{0, 2, 4, 8, 16}` and fixes `E(3,0)`; `⟨cnot, actT J, actT S, actT nflip⟩` has order 384 and equals
     `⟨cnot, actT S, actT J⟩`; `⟨cnot, actC J, actT J⟩` has order 11520 and equals the Clifford group
     `⟨cnot, actC J, actT J, actC S, actT S⟩`, whose stabiliser of `E(3,0)` is the 384 group and whose orbit of `E(3,0)`
     has 30 elements (U1, U2); the orbit of the 36 octahedral product rays under the lift of the 384 group has 60 rays
     whose tables span 16 dimensions (U3); the minimal polynomial of `−1 − sin(2π/m)` is monic over `ℤ` exactly for
     `m ∈ {1, 2, 4}` among `m ≤ 24` (control: `2 cos(2π/m)` monic for every `m`; countercontrol: `cos(2π/m)` monic exactly
     for `m ∈ {1, 2, 4}`), and `tr(J R_z(φ)) = −sin φ` symbolically in the kernel's orientation (U5, V1);
     `|⟨J, R_z(π)⟩| = 12`, `|⟨J, R_z(π/2)⟩| = 24` (V3); `⟨J, R_z(π), 2uuᵀ − 1⟩`, `u = (φ − 1, φ, 1)/2`, has order 60 in
     `Q(√5)` and exactly two `z`-axis rotations, `1` and `R_z(π)` (V2); `φ₀ = (1, 2, 3i, −1+i)/4` is
     `(P₀⊗U₀ + P₁⊗U₁)(a ⊗ |0⟩)` with `a = (√5, √11)/4` and explicit unitaries, and no element of the 384 group carries
     its table to a product table (reduced-state purity test) (U6); the word-length stage `Λ₁` has exactly 588 rays, with
     `RΛ₀ ⊄ Λ₀` and `RΛ₁ ⊄ Λ₁` (U7).
   - X4 (B13): `prodDet(1,2,3,5) = −1` and `−7` after CNOT; the polarisation identity; the three-root lemma on an
     instance; a common non-root on five points of a line for two unitaries.
4. **Written arguments read.** B10 §3 (H-T as the weakest premise in NOTES-B1's vocabulary; the disguise test fails
   because H-T is OI⁺-1's spectator clause at level H for one operation — consistent with stage 5/6 and B5-1): sound as
   an identification; §4 (local finiteness through the monomial groups; the union's closure contains every `R_z(t)`
   by density of the dyadic angles): sound, [W] beyond `n ≤ 4`; §5 (the torus identity component, X2's dimension 2):
   sound; §6 (the configuration-wise reading of `substratumClass_contextStable` is L-REG and Bell-local: the
   assumption-watch marker, consistent with B1-4): sound. B12 §2 (permutation-character integrality: a rational induced
   map of finite order has integer trace): sound; §3 (the norm argument: the Galois conjugates of `cos(2πr)` lie in
   `[−1, 1]`, and an algebraic integer with all conjugates of modulus `< 1` is zero): sound, exact for `m ≤ 24` by X3;
   §4 (the determinant-ratio homomorphism confining the group to `{det U₀/det U₁ = ±1}`, whose identity component is
   `SU(2) × SU(2)`; every pure state in the product orbit by a control-basis Schmidt form): sound, with X2's dimension
   6 and X3's instance; §5 (the word-length filtration): the stage sizes verified (X3). B13: the avoidance lemma is
   elementary and kernel-checked; the module's `ReachUnitary` and `ReachAnti` state B7-1 in `U(4)` with the identity
   component taken in the subgroup, the two coset conditions making `H ∪ Hκ` a group; `reachUnitary_finite` and
   `reachAnti_finite` carry no hypothesis on the identity component or on `K`, as the rows say.
5. **Kernel citations.** The coordinator's sweep (`cite_check_r3.py`, lines added since `3686049e`) finds 25 distinct
   `File.lean:NNN` strings; **25/25 resolve at L** (`cite_check_r3_bridge.out`). The citing lines the checker could not
   pair with a declaration name were inspected: OIRealization.lean:360 `finiteOI_not_implies_inert` and
   SpectatorBridge.lean:223 `InertSpectatorCompositionality` (cited with :233); AncillaInterference.lean:123 and
   ClosureObstruction.lean:282 (precedents for the Kronecker rewrites, the Mathlib lemma names on the cited lines);
   ClosureObstruction.lean:133 (`Finset.induction_on` pattern) and BarandesTuple.lean:445 (`Matrix.mem_unitaryGroup_iff`);
   TransitiveBody.lean:109 `chartBody_isCompact`, quoted from HO-9 item 3's composition list. All correct.
6. **Design runs** (`CI-RUNS-R3.md`): 38099134414 (`dev-bridge/r3-dict` @ `3d554e7e`): Build success (3644 jobs,
   `Built OIBridge.BridgeDictionary (23s)`), **20/20** prints on `[propext, Classical.choice, Quot.sound]`, `lean-axioms`
   OK (5880, no sorry); 38101591388 (`dev-bridge/r3-reach` @ `747bcf94`): Build success (3646 jobs,
   `Built OIBridge.BridgeReach (1.7s)`), **21/21**, `lean-axioms` OK (5881, no sorry). Both gates red exactly at
   `claims` (7), `duplicate` (104) and `lean-manuscript` (1) — the dev branches are cut from `research/bridge`, which
   carries `research/archive/`, as the thread records. Each run 32 jobs success, 1 failure (the bridge job's gate),
   nothing cancelled. Design evidence only; nothing certified.

## Findings by row

| row | thread label | audit |
|---|---|---|
| B10-1 | CONJECTURE for K(Z_F); the B4 part CONDITIONAL (branch (a)) | accepted; X2 (T1); the 129-table closure replayed, not re-derived (B4 audited in round 1) |
| B10-2 | CONDITIONAL (branch (a), B4-1; B1.1 [D]) | accepted; K(Z_F)'s non-invariance under `actT R_z(θ₀)` confirmed with the coordinator's own certified witnesses; the value `−2/5` is B4's |
| B10-3 | CONDITIONAL (H-T assumed); FAILED as a bridge | accepted; the identification with OI⁺-1's clause read (method 4) |
| B10-4 | CONDITIONAL (claim (D) [A]; HO-13 item 2) | accepted; X2 (T9: dimension 2, abelian) |
| B10-5 | CONJECTURE ([X] `n ≤ 4`, [W]); H-level form CONDITIONAL on (A) at each stage | accepted; X2 (T8 orders and inclusions; the traces) |
| B10-6 | CONDITIONAL on the reading; the matrix theorem CERTIFIED (StructuralClosure.lean:261) | accepted; the kernel line verified; assumption-watch marker carried to the overview |
| B10-7 | CONDITIONAL (reading of Main.md:544–558); OIRealization.lean:360 CERTIFIED | accepted; X2 (T10); the kernel line verified |
| B11-1 | CONJECTURE ([D], run 38099134414) | accepted; X1 checks (D1) and (D2) against the kernel's own gate, action and NOT definitions, independently of the module; the run verified |
| B11-2 | CONJECTURE ([D]); injectivity OPEN in the module | accepted; convergence point: `dict_injective` is [D] in the equivalence thread's `EqvK2Schema` (HO-18) |
| B12-1 | CONJECTURE (exhaustive exact computation) | accepted; X3 (48, 384, 11520, the stabiliser, the orbit of 30, the 60 states, rank 16) |
| B12-2 | CONJECTURE (written proof); the tower clause CONDITIONAL on [L]; FAILED as a token-local tower route | accepted; X3 (minimal polynomials to `m = 24`, orders 12/24/60, the two `z`-rotations); the norm argument read |
| B12-3 | CONJECTURE (exact computation and written proof); the tower exclusion CONDITIONAL on Jordan [L] | accepted; X2 (dimension 6, commutation with `Z ⊗ 1`), X3 (`φ₀`'s block-diagonal reach; unreachable by the 384 group) |
| B12-4 | CONJECTURE ([X] stages computed; [W] all stages); B4 part CONDITIONAL | accepted; X3 (`\|Λ₁\| = 588`, the stage-crossing of `R`) |
| B12-5 (B12-S) | CONDITIONAL (HO-9 items 3–5, HO-13 item 2, [L]) | accepted at its label |
| B13-1 | CONJECTURE ([D], run 38101591388) | accepted; the module's statements read (method 4); X4; the run verified |
| B13-2 | CONDITIONAL (claim (D) [A]) for the fixed-finite case | accepted |
| V-3 | CONDITIONAL on H-OI_g; the route from embedded observation alone FAILED | accepted; sharpens V-2 without changing its substance |

No label changes. The thread's recorded deviations (one import line per dev module; two LOG stamps corrected forward;
two pre-run edits logged in the script headers; S0-5's range `m ≤ 24` covered by the follow-up; a false draft sentence
of NOTES-B12 §3 replaced before commit by what the certificate proves; two scripts first run without `-I -B`, re-run
identically) are each in the LOG and change nothing audited here.

## Handoff items

- HP-7 (H-T, the transfer clause's weakest H-level premise; the disguise test; strictly weaker than H-OI_g; local
  finiteness; the L-REG marker) → **HO-20** to the origin and equivalence threads.
- HP-8 (the dictionary module (D1), (D2) and `transfer_phase`) → **HO-21** to the equivalence and countermodels
  threads, cross-referencing HO-18.
- HP-9 (the finite half as `Stab_C(Z ⊗ 1)`; the `z`-rotation bound; the `SU(2) × SU(2)` closure; B12-S) → **HO-22** to
  the origin, equivalence and countermodels threads.
- HP-10 (B7-1's formal statement and its finite case) → **HO-23** to the countermodels and equivalence threads.
