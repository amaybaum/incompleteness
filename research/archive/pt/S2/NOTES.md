# S2 — PAIR-CONS — working notes (launch 2)

Research only. Base L = `9f9f8257a980a1819fbbc1dc0019917cf8678626` (`pt/base/`, read-only).
Governing: PROTOCOL.md, AMENDMENT-1, AMENDMENT-2, PROTOCOL-STAGE2.md (stage-2 governs where they differ).
Writes only in `pt/S2/`. No git writes, no agents, no PR/CI, no publication.

## Log

- 07:26Z start checks all OK; `.start_marker` written first (S2 was empty).
- Read: PROTOCOL, AM-1, AM-2, STAGE2 (hashes verified), INTEGRATION-REVIEW, AUDIT-A, AUDIT-D, AUDIT-B, A/RESULT.

## Reading notes (to re-verify what is used)

- A: narrow product P1 (cone SEP), P3 with cnot (cone K_gen = SEP + cnot SEP) both DERIVED as constructions; LT by
  construction (product labels only). `actT reflY ∘ cnot` closure invalid (−1/2). D_cl: infinite-rank pair system with
  joint labels whose read-out is K_cl (not closed). K_E = dualW(K_gen) = maxCone ∩ cnot(maxCone) largest admissible
  cnot-invariant cone. Every admissible cnot-invariant convex cone lies in [K_gen, K_E].
- A pass 3 "open lead": N-CLASS gate of infinite order — Milman converse of Krein–Milman.
- D: T3 hadm ⟺ pair cone = product-test cone of a COMP-1 pre-composite of two balls (no lt). paddedBall3 non-LT.
- B: product-only pair system admits no OpDatum for cnot (F = diag(1,−1,1,−1), ipW F phiW = −2). Sources of hgate
  restate it.
- Read further: D/RESULT, B/RESULT, C/RESULT, AUDIT-C, landed KT4-PREM-1 result.md, inputs2 RANK/QUOTIENT/RECORD (verdicts),
  K2-LEDGER §1-§3 (PTQ, D3, D6), design modules FourCopyDefs/Core/Headline/IE1/Local/Bipolar/Parity (definitions and the
  consumption of FCC), landed CompositeDimension §A-§K, CompositeInterface (ProductData, PreComposite, Composite, lt,
  paddedPre/paddedBall3, JointReversible), StageCompletion (DirectedStages, prepVec, body, FiniteRank), KInfFoundations
  (FiniteStage, IsEffectOn, ball3), CompletionAction (OpDatum, AffineRespect), K2Guard (CandidateCone, reflY, idW,
  chainW, cnotOrbit, no_candidateCone_cnot_reflY), OrbitGeneration (PreservesBody, fullAut3), TransitiveBody (eball).

## Definitions re-verified at source (anchors)

- `W 3` = 4x4 real tables, index 0 unit (CD:97; docstring CD:95-96 "Local tomography is the premise this carrier
  encodes"). `prodState x y = hom x hom y^T` (CD:161). `prodEffVal e f w = ehom e^T w ehom f` (CD:182).
  `maxCone` (CD:186). `actT N w = w homMap(N)^T` (CD:198), `actC N w = homMap(N) w` (CD:201).
  `cnot` = signed permutation `sgn/pc/pt` (CD:741-790), involution `cnotFun_cnotFun` (CD:770).
  `nflip = diag(1,-1,-1)` (CD:797), `z3 = e_3` (CD:793), `xplus` (CD:1213), `phiW` (CD:1220).
  `NativeGate` (CD:218: frame, posFwd, posInv, relT, relC), `IsNot` (CD:210).
- `reflY = diag(1,-1,1)` (K2G:46); `idW`, `chainW` (K2G:101,104); `CandidateCone` (K2G:95); `cnotOrbit` (K2G:182);
  `no_candidateCone_cnot_reflY` (K2G:143).
- COMP-1: `ProductData` (CI:210), `PreComposite` (CI:223), `LocallyTomographic` (CI:235), `Composite.lt` (CI:243),
  `JointReversible` (CI:445), `paddedPre` (CI:848), `paddedBall3` (CI:909), `not_locallyTomographic_paddedBall3` (CI:912).
- Completion: `DirectedStages` (SC:63), `SCInf` (SC:78), `prepVec` (SC:135), `body` (SC:141), `FiniteRank` (SC:299);
  `FiniteStage` (KIF:63); `OpDatum` (CA:46), `AffineRespect` (CA:58).
- Single-system reversible operations at L: `fullAut3` (OG:521, all affine automorphisms of ball3 = O(3)),
  `transBody_fullAut3` (TB:694), `rot3` (KIF:411, about the 3rd axis), `rotX` (ON:581, about the 1st axis),
  `refls3` (TB:700). `eball_three : eball 3 = ball3` (TB:671).
- Design [D]: `ipW` = Frobenius (FDefs), `dualW`, `FourCopyCoherent` famI/famII over FULL duals, `IE1` = invariance under
  every rotation (SO(3)) on either token (FCore), `NClass`, `orient`, `bellOf`.
- FCC consumption in the design proof (to re-check by source scan): `cross_rel` uses `h.upper` with E,F = Bell tables
  (gate images of sharp products) and free X in K, Y in K'; uses `h.lower` with L, L' = Bell tables and FREE e in dualW K,
  f in dualW K' (+ the bidual). `inv_*` lemmas: `h.lower` with link/Bell states and free full-dual effects.

## Plan (depth-first; decisive branch first)

Decisive question (S2.5): does a data-generated construction without operation-level idle extension reach beyond
K_gen / reach Q3? Expected decisive lemma: every NativeGate gate in the fixed frame is cnot dressed by signed-diagonal
locals (D1.4), and Pauli/transpose dressings are absorbed (Clifford normalization) => consistent fixed-frame native
constructions generate exactly K_gen or its twin. Then: finite-group obstruction (dimension), and exact reductions of
the natural infinite families (frame covariance, CtrlGate frame family, ZZ-type) to local operations.
Second line (S2.2/S2.3): abstract-carrier construction; LT of a test-generated tower <=> PTQ of its generators;
PTQ of the native gate from INV2 (operational involution) + certified product action; register model (N^4=id) and
clock model (infinite order) as countermodels; real-QT rebit control for the product-action ingredient.
Third line (S2.6): generated effects = generated states (cnot orthogonal involution); FCC restricted to generated
effects holds for uniform K_gen; the design proof consumes full duals in famII's free slots; no-restriction <=> Q3 for
unitary-generated systems.

Scripts (exact, `python3 -I -B`, run from pt/S2/): s2_a_construction, s2_b_inv2, s2_c_rank, s2_d_native, s2_e_beyond,
s2_f_effects. Decision rules in each header before the first run.

## Node log

### N1 (S2.5 decisive) — the fixed-frame native family generates only K_gen or its twin. Verdict: NEW (exact obstruction)
- s2_1_native.py run 1 (script sha256 bfc060b4…): 42/42 PASS, all countercontrols fail as required.
- Within signed-diagonal dressings, frame+relT+relC (NativeGate at (z3, nflip)) select exactly D1.4's family: 32 distinct
  gates (64 combos), 8 per orientation pair (pre, post). One orientation pair per gate (T2 cross-check).
- Absorption: cnot o L o cnot is a signed-diagonal local iff L is orientation-even (all 64 locals); odd L give
  non-product images (exact).
- Consistency: all 512 ordered pairs with odd residue have an exact negative product-effect witness on axis data;
  even residues are absorbed. So consistent native sets lie in one orientation class (even-even or odd-odd).
- Each class generates a group of order 16, every element L or L o cnot o L' with even post-local; L o cnot =
  cnot o L''. Hence the generated cone of ANY consistent nonempty set of fixed-frame native gates is
  SEP + cnot SEP = K_gen (even class) or sigma K_gen (odd class). [W + X]
- Pressure test pending: completeness of the native family beyond signed-diagonal dressings rests on D1.4/T1 [W + X,
  audited]; my exact cross-check covers the 4096 signed-diagonal dressings only.

### N2 (S2.5 continued) — beyond the fixed-frame native family. Verdict: NEW (class obstruction) + ELABORATING
- Pre-run edits to s2_2_beyond.py (before run 1): header wording of Q2's finite cross-check aligned with the code;
  Q3's monomiality check made convention-free (rotation read off Ad(I(x)Uz), not guessed). No run preceded them.
- s2_2_beyond.py run 1 (sha256 a18988f5…): 38/38 PASS, all countercontrols fail as required.
- CtrlGate (landed RSB:45) = NativeGate without relT; it KEEPS relC. Its fixed-frame family is continuous through the
  target pre-local R0 (rotations about z3): G_t = cnot o actT Rz(t) is CtrlGate, not NativeGate (relT fails), and
  cnot o G_t = actT Rz(t): a local rotation acting on every table (a fragment of local agency, generated, not assumed).
- Every unitary gate meeting the frame clause maps computational basis vectors to phased basis vectors (monomial) [W];
  exact instance G' = Ad(CNOT (I (x) Uz)).
- Monomial obstruction: psi_w = (3|00>+4|01>+5|11>)/sqrt50 is pure, in Q3, Schmidt-equivalent to
  cnot(prodState((3/5,0,4/5), z3)) (equal reduced Bloch length 16/25); its modulus pattern (9,16,0,25)/50 has no
  rank-one arrangement. Written step: for a compact group H of monomial unitaries (and the global transpose), pure
  states of cl cone(H.SEP) lie in H.(pure products) (Milman + extremality), whose modulus patterns are permuted rank-one
  patterns. So no frame-monomial construction reaches Q3 or an IE1 cone (contains cnot images, misses psi_w).
- SWAP (token exchange, [N] datum, monomial): <cnot, SWAP> has order 6; its cone strictly contains K_gen (pure witness
  s_w, ranks 4,4) and misses psi_w (finite rank test over the 6 elements).
- Diagonal entangling family: cnot o Ad(ZZ) o cnot = actT Rz (local) exactly.
- Frame covariance words: W_A = cnot o C(Rx,I) o C(I,Zpi) o C(Rx,Zpi) = actC(rotation about x0 by 2phi) and
  W_B = cnot o C(I,Rz) o C(Xpi,I) o C(Xpi,Rz) = actT(rotation about x2 by 2phi), symbolically mod c^2+s^2=1.
- Local agency instance: T_psi = actT R_H phiW pure, ranks 4,4 (outside K_gen), one local rotation on phiW.

### N3 (S2.3) — local tomography of a pair system realizing the certified gate. Verdict: NEW (source + countermodels)
- s2_3_lt.py run 1 (sha256 d614b9fd…): 35/35 PASS.
- Block lemma (symbolic): with product action (A = cnot, forced since products span W 3), PTQ of N on the generated
  span <=> B C = 0; the W3-block of N o N is I + B C, so INV2 (N o N = id) => PTQ => LT of the test-generated
  completion (labels = product tests after N-words read cnot^k of the table).
- LT <=> PTQ of the generators, for test-generated towers [W, both directions] (sharpens K2-LEDGER D3/D6: the padded
  PTQ-not-LT control is invisible to a test-generated completion).
- Countermodels: register model (N^4 = I, N^2 = cnot (+) cnot): product action, validity, unit, closure under N and
  N^-1, finite rank (dim 32), NOT LT (pi s = pi s' = phiW, pi(N s) = phiW vs pi(N s') = pxz). Rebit control (d=2): N o N
  = I but the product action C has C(X(x)Z) = 0, LT fails ((I+YY)/4 vs I/4). Order-3 model: carrier INV2 fails, LT holds
  (carrier INV2 strictly stronger than LT; completion-level INV2 <=> LT relative to generation + product action).
- Pressure test of the favourable reading: (a) product action reads only product tests of gate images of products,
  no LT; (b) generation is load-bearing: N = [[cnot, Delta],[0, 1]], cnot Delta = -Delta, is an involution with the
  product action, and an ungenerated preparation (E00, t) breaks LT (to be checked exactly in the tower script);
  (c) renaming test: INV2 states an identity of one operation, LT a separation property of all states; equivalent only
  relative to generation + certified product action: not a renaming. Precedent: IsNot.invol (CD:212) for the
  single-system NOT; cnotFun_cnotFun (CD:770) for the table datum.

### N4 (S2.2) — finite rank. Verdict: NEW (countermodels) + ELABORATING
- s2_4_rank.py run 1 (sha256 62969064…): 15/15 PASS. Clock model (gate of infinite order, certified product action,
  test generation, valid tables): protocol sections full rank at L = 8,16,32,48,64; sigma run lengths 1,3,5,...;
  written pigeonhole step: finite Hankel rank => eventually periodic => contradiction; not LT either. Periodic
  countercontrol bounded (rank 4). Compact padded model: rank = 16 + L, sup-distance 2^-(J+1): compact, infinite rank.
  Register model: finite rank 22 without LT. Involutive model: rank 16.
- s2_5_tower.py: pre-run edits before run 1 (T2 vacuous comparison removed and restated as the inclusion check;
  T3/T5 moved to stage 2; T5 tested by exact rank equality; table caching). Run 1 (sha256 321ac1ee…) 17/17 PASS.
  Tower valid (stages 1-3), SC by inclusion, table rule (LT built in), rank 16, gate generative with AffineRespect,
  read-out closed under cnot; g_D countercontrol invalid; generation load-bearing (hidden-parameter model).

### N5 (S2.6) — effects. Verdict: NEW
- s2_6_effects.py: one pre-run edit (rho(F) non-PSD certified by Tr(rho(F) rho(T_psi)) = -1/8 instead of symbolic
  eigenvalues). Run 1 (sha256 9c3f1d9f…) 22/22 PASS.
- E_gen = K_gen as cones (cnot symmetric orthogonal; sharp product effects = prodState/4). dualW K_gen strictly larger
  (F: forms 1/4 - x^T M y/4 with M, M' orthogonal; Tr(rho F rho T_psi) = -1/8). FCC on generated objects >= 0 on all
  checked instances; the -1/8 instance uses two non-generated effects (T_psi/4 and F).
- Source scan: cross_rel's first half consumes FCC with Bell effects (bound) and free states; cross_rel's second half
  and inv_left_ctrl, inv_right_ctrl, inv_left_partner, inv_right_partner consume it with gate-supplied states (bound)
  and FREE full-dual effects; target02 maps upper->famII, lower->famI (so both families); parity binds all slots.
  => the theorem consumes no-restriction exactly in the free effect slots of the second-half/invariance uses.

### N6 (S2.4/S2.5 supplement) — table cells. Verdict: CONFIRMING
- s2_7_supp.py run 1 (sha256 6e43f762…): 13/13 PASS; replay byte-identical. The CtrlGate family strictly exceeds K_gen
  (s_c = actT Rz cnot prodState(xplus, yplus): pure, ranks 4, 4; countercontrol ranks 4, 1). An improper target
  pre-local (Rz o reflY) in the CtrlGate family is inconsistent (value -11/50). The odd class: sigma K_gen is
  g_Tw-invariant (g_Tw o sigma o cnot = sigma) and not cnot-invariant (chainW, -1/2).

### Passes after N5 (fixed point)
- Pass A: GateRel (PN:42) = relT + relC only: no frame, no positivity, so it does not define an available native gate;
  scope note, no analysis. Pass B: the dual completion (states := dualW of generated tests) gives K_E (Thread A): more
  than K_gen, overshoots Q3, fails FCC (-1/2) and IE1 (-2/5) [A, audited]; a self-dual completion is a choice of cone,
  not a generation; uniqueness of a cnot-invariant self-dual cone between K_gen and K_E is S3's open W2 (record only).
  Bit symmetry => self-duality (Mueller-Ududec 2012) [L, unverified]: needs a rich reversible group (lead only).
  Pass C: reflections act harmlessly on products and inconsistently as operations (orientation residue): ELABORATING
  K2-GUARD-1. No NEW finding in passes A-C: fixed point reached; the thread's question is answered.

### Close-out
- Correction to N2's wording: the frame-covariance words are rotations by -2phi (sign), per the symbolic matrices
  printed by s2_2_beyond Q5; RESULT.md states -2phi.
- Replays: all seven scripts byte-identical (stdout and stderr). Totals 182 PASS, 0 FAIL; no failed run, no .runN files.
- End integrity (2026-10-10T08:34:50Z): manifests OK; base HEAD 9f9f8257…, status empty, no pycache; protocol hashes
  unchanged; no foreign file in S2; no file outside S2/ (and S3/) newer than the start marker.
- RESULT.md written (sections 0-7). Labels: FR CONDITIONAL (INV2 / finite group), LT CONDITIONAL (INV2 + product
  action + generation), GC DERIVED for the generated system (CONDITIONAL on INV2 on an abstract carrier), SS INDEPENDENT
  of L with class impossibility (N, M, F), FC <=> IE1 given hgate (flagged), EFF: no-restriction consumed in the free
  effect slots.

### Final re-check (after RESULT edits; not part of RESULT)
```
final re-check utc: 2026-10-10T08:36:31Z
inputs.manifest OK
stage1.manifest OK
inputs2.manifest OK
base HEAD 9f9f8257a980a1819fbbc1dc0019917cf8678626, status lines 0
PROTOCOL OK
PROTOCOL-AMENDMENT-1 OK
PROTOCOL-AMENDMENT-2 OK
PROTOCOL-STAGE2 OK
foreign-newer-files outside S2/S3: 0
S2 entries: 38
```
