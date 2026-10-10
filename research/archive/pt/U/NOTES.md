# Thread U (UNIQ) — running notes (launch 3)

## N0. Start (11:23:27Z)
- `.start_marker` written first into a fresh `pt/U/` (did not exist). All start checks green (see marker).
- Governing texts read in the required order (STAGE3, STAGE2, PROTOCOL, A1, A2, STAGE2-DS, owner direction,
  addendum §3, AUDIT-S3, AUDIT-S2, S3 §1.2 item 3 + s5_pairlevel.out, S2 §S2.5–S2.6, base AGENTS.md rules).
- Toolchain: Python 3.11.15, sympy 1.14.0, numpy 2.4.6, scipy 1.17.1. Floats only in sections marked [N].
- Tooling constraint (launches 1–2 aborted on output size): files written in parts of <= ~250 lines,
  scripts <= ~300 lines, long computations split across scripts.

## N1. Definitions used (re-implemented here, cross-checked against L)
- `W 3` = 4x4 real tables [K CompositeDimension.lean:97]; `prodState x y` = hom x ⊗ hom y [K CD:161];
  `cnot` = signed permutation `sgn/pc/pt` [K CD:741–786]; `ipW` = Euclidean sum [D FourCopyDefs:31];
  `pauliW w = (1/4) Σ w_mn σ_m ⊗ σ_n` [D FourCopyPackage:176]; `Q3 = {pauliW ⪰ 0}` [D FCP:180].
- My own check: `cnot` equals conjugation by the CNOT unitary (control token 0) on the Pauli basis.
- E0 = E00 + E13 − E22; G = −1/4 eigenprojector of pauliW E0; R_H = [[0,0,1],[0,−1,0],[1,0,0]]
  [landed kt4_prem1_probe.py:117]; T_psi = actT R_H phiW = E00+E13+E22+E31; F = E00/2 − T_psi/4.

## N2. Plan (depth-first; decisive first)
Decisive structural observation to test first (pre-run, written before any script):
- Equivariant Barker–Foran (BF): a maximal cnot-invariant self-positive cone M ⊇ C0 is self-dual iff
  M* ⊆ Q_g := {y : <y, cnot y> >= 0}. So "C0* ⊆ Q_g" for some admissible C0 ∋ E0 would give an
  exotic K by a written (Zorn) argument; a y ∈ K_E with <y, cnot y> < 0 shows the naive version fails.
- Candidate y = E00 + E13 + E22 (pauli: (I + XZ + YY)/4): in maxCone and cnot maxCone by a Bloch
  bound, <y, cnot y> = −1. To be checked exactly in u1.
- V+ sub-problem (U3): plain (non-equivariant) BF in V+ gives a self-dual cone in V+ containing
  K_gen+ and E0 (E0 ∈ V+, E0 ∈ maxCone ∩ V+ = (K_gen+)^{*V+}); so PSD(3)⊕R+ is NOT unique in V+ by a
  [W] argument. Exact ingredients to be checked in u1/u3.
- U2: local Wigner step — elementary proof via (i) qubit Wigner on each slice, (ii) cross-ratio
  constancy, (iii) rank-one coefficient matrices, (iv) Segre-line argument. Exact lemma checks in u2.

## N3. Pre-run edits / runs / anomalies
(none yet)

## N4. u1_struct run 1 (11:3xZ): 21/21 PASS, VERDICT U1-STRUCT-EXACT. Pre-run edit: C8a/C8c decision rules
made property-only (nonnegativity, >= 2) instead of comparing to an expected value set.

## N5. Decision record (written before any exotic-cone script): the surgery cone K★
Pencil derivation, to be checked exactly before anything is claimed:
- Let z = E0 (cnot E0 = E0, E0 ∈ maxCone, <E0,E0> = 3, pauliW E0 = (I + XZ − YY)/4, spectrum 3/4,1/4,1/4,−1/4).
- K★ := (Q3 ∩ E0*) + R+ E0. Self-positive (each pairing >= 0), cnot-invariant (cnot Q3 = Q3, cnot E0 = E0),
  contains SEP (products are in Q3 and pair >= 0 with E0 ∈ maxCone), closed.
- Dual: K★* = (Q3 + R+E0) ∩ E0* (bipolar; Q3 + R+E0 closed since −E0 ∉ Q3).
- Projection lemma (PL): for q ∈ Q3 with <q,E0> < 0, Π(q) := q − (<q,E0>/3) E0 ∈ Q3. Then any
  y = q + σE0 ∈ K★* with <q,E0> < 0 rewrites as Π(q) + (σ + <q,E0>/3)E0 ∈ K★. So K★ = K★*.
- PL reduces (extreme rays of Q3 ∩ {<.,E0> <= 0}: cap-pure states and rays on E0^⊥) to pure ψ in the cap;
  by the determinant lemma + interlacing it is 11|c_g|^2 >= |c_1|^2 + 11(|c_2|^2+|c_3|^2), implied by the
  cap inequality |c_g|^2 > 3|c_1|^2 + |c_2|^2 + |c_3|^2 (coordinates in the E0 eigenbasis).
- If all of this survives exact checks: an explicit EXOTIC cone at level (i). Skepticism items to check:
  (a) the bipolar/closedness step, (b) the extreme-ray reduction, (c) the determinant-lemma sign logic,
  (d) H1 for mixed products (ball, not sphere) by a symbolic SOS identity, (e) level (ii) separately.
- Countercontrols planned: a z with two negative eigenvalues (PL fails, K_z not self-dual, exact witness);
  z = F (one negative eigenvalue, PL holds, K_F self-dual ⊇ SEP but NOT cnot-invariant); z ∈ Q3 gives Q3.

## N6. u1_kstar run 1: 27/27 PASS, VERDICT KSTAR-INGREDIENTS-EXACT. Pre-run edits: D5c rewritten twice before the
first run (witness now computed from the table via pairval). The determinant identity
det pauliW(Pi q) = -B^3 (11 ng - n1 - 11(n2+n3))/6912 holds symbolically; 11ng - n1 - 11(n2+n3) = -11B + 32 n1.
With the principal (e1,e2,e3) block k diag(3,1,1) + cc^H (k = -B/12 > 0) positive definite, the Schur complement
gives pauliW(Pi q) positive definite for every pure q strictly inside the cap. No interlacing needed.

## N7. u1_kstar_cc run 1: 11/11 PASS, VERDICT KSTAR-CONTROLS-EXACT.
- PL is load-bearing: z = (psi psi^H)^Gamma, psi = 2|00>+|11>, is in maxCone with one negative eigenvalue, yet
  its surgery cone is not self-dual (cap state |01>-|10>+|11>, det of projection -1296/390625).
- H2 needs a cnot-fixed surgery vector: Y1 (E0's partial transpose) and F give self-positive surgeries that
  contain the vector but not its cnot image.
- Level (ii): the 8 (even,even) gates satisfy frame/relT/relC exactly and generate a group of order 16 containing
  Z_c = actC diag(-1,-1,1); <E0, Z_c E0> = -1. So K* is a level-(i) countermodel only; at level (ii) no valid
  cone contains E0, and the fixed space (dim 3, diagonal tables) cannot host a one-vector surgery.
- Decision: level (ii) gets its own node (orbit surgery with z_a = aE00 + E13 - E22, orbit {aE00 ± E13 ± E22},
  self-positive iff a^2 >= 2, non-PSD iff a < 2). Test numerically first [N], then exactly.

## N8. u5_level2_N run 1 [N, numerical; no verdict]: pre-run edit lowered maxiter 4000->1500 and starts 12->8 (time).
Minima of <y,h>/|y||h| over K_Z*: a=1.00 -0.0956, 1.25 -0.0559, 1.50 +0.0588 (optimizer did not converge: the true
minimum is <= 0), 1.75 -0.0095. Leads only. Pencil analysis then gave an exact obstruction for every a in [√2, 2):
y = P_e3 + ((2-a)/a^2) z_{+-} lies in K_Z*, <y, z_{++}> = 0, y ∉ Q3, and every <z_s, z_{++}> > 0, so y ∉ K_Z.
Mechanism: with a non-orthogonal orbit, other surgery vectors can pay a violated constraint, which the projection
cannot absorb. Orthogonality of the orbit is load-bearing.

## N9. Decision record (before scripting): the level-(ii) cone K_F
Z_F := G16-orbit of F = {(1/4)(E00 + s1 E13 + s2 E22 - s1 s2 E31)}; F is the member s = (-1,-1).
pauliW z_s = (1/8)(I - 2 P_{f(-s)}) with f the (XZ, YY) eigenbasis (e1, e2, e3, g). Facts to check exactly:
mutually orthogonal; each on the boundary of maxCone (bilinear part a signed permutation); a PSD q violates at
most one constraint (<q, z_s> = (1/2)(tr - 2<f(-s)|q|f(-s)>)); PL for spectrum (1,1,1,-1)/8 (det of the projection
= (B'/4)^3 (3B'/4) with B' = n_g - sum n_i > 0 in the cap); G16 permutes Z_F and preserves Q3.
Then K_F := (Q3 ∩ Z_F*) + cone(Z_F) is G16-invariant, contains SEP, and is self-dual (y = q + Σσ z ∈ K_F* with
q violating only t has σ_t >= -<q,z_t>/n by orthogonality; rewrite with Π_t q). Level (ii) EXOTIC if all holds.

## N10. u5_kf run 1: 14/15, VERDICT KF-INGREDIENTS-FAILED, kept as u5_kf.run1.{py,out,err}. The single FAIL was the
countercontrol PLc: for psi = f(1,1) against z_(1,1) the projection is P_f(1,1) - I/4 + P_f(-1,-1)/2, negative on
f(1,-1) and f(-1,1); run 1 probed f(-1,-1) (value +1/4), a wrong witness, so the countercontrol did not register.
No claim line changed. Fix (only this line): probe f(1,-1). Rerun as run 2.

## N11. u5_kf run 2: 15/15, VERDICT KF-INGREDIENTS-EXACT (all non-PLc lines identical to run 1).
u2_wigner run 1: 10/10 VERDICT U2-LEMMAS-EXACT (pre-run edit: W3 reduction modulo c^2+s^2-1 via sp.rem instead of
a subs dictionary). u3_vplus run 1: 8/8 VERDICT U3-VPLUS-EXACT.

## N12. Decision record (before scripting): U4 and the general surgery theorem
Theorem S (written): Q self-dual, Z finite with (a) pairwise orthogonal, (b) every q ∈ Q violates at most one
constraint <q,z> >= 0, (c) PL for each z, (d) -Σσz ∉ Q for σ >= 0, σ ≠ 0. Then K_Z = (Q ∩ Z*) + cone Z is
self-dual; invariant under any orthogonal group preserving Q and permuting Z; contains SEP if Q ⊇ SEP and Z ⊆ maxCone.
Cases: Z = {E0} (K*), Z = G16·F (K_F), Z = {F, cnot F} (K_F2: <F, cnot F> = 0, cap centres t ⊥ Ut).
Claim for U4: K_F2 ∩ V+ = Q3+ exactly (P+F = (F + cnot F)/2 is PSD; any q ∈ Q3+ pairs >= 0 with F and cnot F).
So even V+-uniqueness would not force K = Q3: the exoticness of K_F2 lives entirely in the V- fibres.

## N13. u4_kf2 run 1: 5/5 VERDICT U4-KF2-EXACT. Replays of all eight scripts launched in one background job
(sequential, same command form as the runs). RESULT.md drafted §0–§3 while the replays ran.
Design-module reads for the downstream note: IE1 = rotation invariance on both tokens [D FourCopyCore:156];
kt4_general_ie1 takes FCC as a hypothesis [D FourCopyHeadline:102]; PairAdm = CandidateCone ∧ convex cone
[D FourCopyDefs:43, K K2Guard:95]. Uniform K★ with cnot gates and identity locals meets hcls/hadm/hcl/hgate; IE1
fails via Ad(Z⊗I) E0 (pairing −1), so FCC fails by the contrapositive [D].

## N14. Replays and end of run (12:52Z)
All eight scripts replayed byte-identically (.out and .err). End integrity checks green; no file newer than the start
marker outside pt/U (excluding pt/X, pt/audit, pt/audit*-replay). All 18 hashes in RESULT §4 re-verified.
Outcome recorded: Q-SD EXOTIC at level (i) (K★, K_F, K_F2) and level (ii) (K_F). Fixed point: question answered.
