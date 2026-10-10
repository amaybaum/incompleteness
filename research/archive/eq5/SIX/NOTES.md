# EQ4-SIX — running notes (research only; base `bcbc516f`, read-only at `scratchpad/eq/base/`)

Protocol: `scratchpad/eq5/PROTOCOL.md`, section "EQ4-SIX" (frozen; never edited here). Nothing here is adopted, frozen or
governed. No Lean toolchain: every Lean text is UNBUILT. Writes only inside `scratchpad/eq5/SIX/`. Exact arithmetic for
anything certified; floating point only in files named `*_float*`, with a banner, never cited as evidence.

## N0. Integrity at start (2026-10-09 08:16 UTC)

- `.start_marker` written 2026-10-09T08:16:38Z (content = that timestamp).
- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0.
- `cd scratchpad/eq5/inputs && sha256sum -c --quiet ../inputs.manifest.sha256`: silent, exit 0.
- `/home/user/incompleteness`: `git status --porcelain` empty (0 lines); HEAD
  `f0d37906a83585efdaca8e3ee3404410e869c43e` on `claude/network-tool-access-8jtdhm` (matches the protocol).
- `scratchpad/eq5/SIX/` was empty at start.
- Library: `eq4_lib.py` copied unchanged from `scratchpad/eq4/P/eq4_lib.py` (sha256 first 16 hex `cc2c6aca94007ac8`,
  both copies). Tools: Python 3.11.15, sympy 1.14.0, numpy 2.4.6, scipy 1.17.1 (numpy/scipy only in `*_float*` files).

Inputs read in full before any work: `eq5/PROTOCOL.md`; `eq4/PROTOCOL.md`; `eq4/P/RESULT.md`, `eq4/P/NOTES.md`;
`eqreview/EQ4-AUDIT.md` (its corrections take precedence); probes p6, p7, p11, p12 (headers and outputs), x9, x11.

## N0.1 Productivity test (copied from the protocol before the walk; not edited afterwards)

A finding is a gem iff it is one of:
1. an exact certificate of (a) or (b) at a stated instance;
2. a theorem route with every step checked;
3. an exact obstruction for a stated class of lifts or extensions;
4. an exposed hidden assumption.

Otherwise it is record-only.

## N0.2 Decision rules for every script (rules, not expected numbers)

- R1 A script's header states its decision rule before its first run. A VERDICT line prints only when every check,
  control and countercontrol passed; otherwise `VERDICT NOT RENDERED`.
- R2 Linear identities are certified on a full basis of matrix units or as exact symbolic identities; signs by exact
  values; PSD by exact Hermitian elimination. Random exact instances are cross-checks of written proofs only.
- R3 Every favourable check gets a countercontrol that a wrong convention or a wrong object would fail.
- R4 No wall-clock time or other nondeterministic value in stdout (timings, if any, to stderr).
- R5 Harness errors are recorded; failed runs are kept as `.runN.*`; every exact script is replayed byte for byte at
  the end, with hashes recorded.

## N1. The six-token constraint system after uniformity (`s1_system.py`, run 1: 11/11, `S1-SYSTEM-EXACT`)

Two pre-run edits (no run before them), both from re-deriving the formulas by index computation: D used the filter
`A^T` where the identity needs `A^dag` (for complex A the check would have failed); G used `V = B conj(A)` where the
index computation gives `V = (1/2) conj(B) A^T`. Header lines changed to match. Decision rule otherwise unchanged.

**Enumeration (exhaustive, exact) [X E1–E4].** Over every subset S of {0..5} and every ordered pair of distinct
bipartitions (effects A|B, states C|D): a one-token part always gives an empty intersection (automatic constraint,
coordinator's remark, EQ4-P p3 M); crossings with all four intersections nonempty exist only for |S| = 4 (2|2 vs 2|2,
90 ordered pairs), |S| = 5 (parts of size 2 and 3, 360) and |S| = 6 (parts of size 2, 3, 4; 390): classes
(effects, states) = (2|4, 2|4) 120, (2|4, 3|3) 90, (3|3, 2|4) 90, (3|3, 3|3) 90. **No crossing with all
intersections nonempty has a five-token part**: K_5 enters P6 only through automatic constraints.

**Reduction (W, exact ingredients).** Let K_4 := cl cone(K1 (x) K3, K2 (x) K2 over all cuts, glued states
Glue_s(x, y; w) = tr_pq[(w_pq (x) 1)(x_{p r1 r2} (x) y_{q u1 u2})] over all splits), K_5, K_6 := cl cone of their
products. Then the P6 constraints are:
- 4-token sets: crossings are pair-level (2|2 vs 2|2), automatic in QM; L_4 <= max_4 needs only the pairings below.
- 5-token crossings (types (1,1,1,2)): each is a one-token map applied to a triple; for rank-one pair objects the map
  is Ad(Xi^T conj E) [X B, all 64 units], and every filter arises (E = 1, Xi = U^T); general PSD pair objects give
  sums: **five-token crossings <=> K3 invariant under one-token CP maps (with renames)**. (c = 1: twin objects give
  Ad((1/2) conj(B) A^T) [X G].)
- 6-token (3|3, 3|3) = the ring, implied by five tokens + co-self-duality (EQ4-P p7 R1–R3).
- 6-token (2|4, 3|3): glued states lie in K_4 (true by construction). (3|3, 2|4): glued effects
  Glue_e(e, f; z) = tr_st[(z_st (x) 1)(e (x) f)] lie in K_4* = L_4*, i.e. <Glue_e, g> >= 0 for every generator g of L_4.
  Against product generators: 1|3 products reduce to five-token crossings [X C]; 2|2 products crossing the glue split
  reduce to the theta value (1/8) tr(x T(Ad(1 (x) A^dag (x) B^dag) y)) >= 0 by (A2)+(A3) [X D]; 2|2 products along the
  glue split are pair-level. Against glued states of the same split: (1/4) tr(T(M) N) with M, N two-token
  contractions confined to PT(PSD_4) by a five-token crossing, and T(PT(PSD_4)) = PT(PSD_4) self-dual [X F].
  Against glued states of a crossing split: **the glue network N(x, y, e, f) — not reducible** (countercontrol F: the
  crossing-split value differs from the same-split formula).
- 6-token (2|4, 2|4): one-token CP maps on K_4, which preserve L_4 by construction (CP-invariance of K3 and of the
  glue). K_4's S_4 symmetry and uniformity (six-token teleportation, EQ4-P p3 T) hold for L_4 by construction.
- 1|5 bipartitions: automatic (one empty intersection) once K_5 is coherent, which needs only five-token crossings and
  L_4 <= max_4.

**Verdict N1: NEW (gem item 4 — the six-token wall is one network).** Under P6 (c = 0), after uniformity:
P6 holds for a family iff its K3 satisfies (A1) BS <= K3 <= BS*, closed convex; (A2) one-token CP invariance (incl.
renames: uniform, S_3); (A3) K3 = T(K3*); (A4) the crossing-split glue network N(x, y, e, f) >= 0 for x, y in K3,
e, f in K3* (Bell links WLOG, filters absorbed by (A2)). Directions, separately witnessed (§A.34): "=>" each of
(A1)–(A4) is a P6 consequence (EQ4-P p1/p2/p4 II1d for (A1)–(A3); for (A4): K_4 contains the glued states and K_4*
the glued effects); "<=" the minimal family K_4 = cl L_4, K_5, K_6 satisfies every P6 constraint, by the case list
above [W + X B–F]. c = 1: the same with B_tw <= K3 <= B_tw*, K3 = K3*, twin links (no T) [X G + W]. The sharpened wall
is therefore a statement about K3 alone: **does a K3 != PSD_8 satisfy (A1)–(A4)?** K_5 never matters; K_4 matters
only through the single glue network. QM controls: PSD nodes give N >= 0, W3 nodes 5/16 [X Q].

Note (exploration y2, float): with GHZ states and W3 effects the glue network is +1/16 in both splits — the glue
network does not by itself detect the GHZ–W3 conflict that the theta network detects (−1/16).

## N2. The lift (ML1) — formulation and explorations

### N2.1 Formulation (W)

Let Lift(K_A) := cl cone{Ad(k) g : k in GL(2,C)^3, g a generator of K_A} (it contains BS: the pair sums twirl from
biseparable states and their filter orbit closure contains every biseparable pure state). For any admissible K3 with
K3 cap GD = K_A: K3 contains K_A, is closed, convex, filter-invariant, so Lift(K_A) <= K3; dually
K3 = T(K3*) <= T(Lift(K_A)*) = Lift(K_A)* (T(Lift) = Lift since T(Ad(k) g) = Ad(conj k) g for GHZ-diagonal g).
Lift(K_A)* = {X : twirl(Ad(k) X) in K_A for all k} = BS* cap (GL^3 W3)* cap (GL^3 kappa')* cap (GL^3 omega)*
(pair sums give BS*). So **a K_A-lift exists iff some admissible co-self-dual K3 lies between Lift(K_A) and
Lift(K_A)***; necessary: Lift(K_A) self-positive. Pairings involving W3 (in Z) or BS are nonnegative (Z self-positive;
BS, kappa', omega in Z* — omega in Z* to be certified); the remaining orbit pairs are (kappa', kappa'), (kappa', omega),
(omega, omega), omega = 1/2 - P0 + P2 (P0, P2 in different fibres), kappa' = 1/2 - P0 + P1 = Z_1-image of kappa.

### N2.2 Explorations (leads only)

- y1 (FLOAT): min over filters of tr(g' Ad(k) g) for the three orbit pairs: -1.7e-17, 4.4e-18 / 0.125 (the same
  quantity in the two orders — BFGS minima are unreliable here), 3.0e-18; at the Clifford tight points (value 0) the
  Hessian has no negative eigenvalue beyond finite-difference error (-2.4e-8). No lead for a failure of
  self-positivity.
- y5 (FLOAT), sector Xi (S_3 and zero-sum phases; 6 real dims; twirled filters act linearly). Written (exact
  algebra in NOTES N2.3 below): BS* cap Xi = {|c| <= u0 + u1}, Tw_Xi(BS) = {|c| <= min(u0, 3 u1)}, QM {|c| <= u0}
  (u0 = sqrt(d0 d3), u1 = sqrt(d1 d2)). A geometric family phi_a = C_a u0^(1-a) (sqrt3 u1)^a (C_a^2 =
  (1-a)^-(1-a) a^-a) is self-dual in Xi, GHZ-free, contains Tw_Xi(BS) for a up to ~0.6 and passed random twirled
  filters (max ratio <= 0.81 for a >= 0.1). Lead: the Xi-sector conditions alone admit GHZ-free solutions.
- y6 (FLOAT): K_A fixes the Xi-profile on the locus rho = d0 d2^3/(d3 d1^3) = 1 to
  phi_A = min(u0 + u1, 3 u1, u0/2 + 3 u1/2), self-dual there. The rho-independent extension C_A is self-dual,
  contains Tw_Xi(BS), W3, kappa, is GHZ-free and invariant under every diagonal filter (Maclaurin; written); under
  optimized twirled non-diagonal filters the ratio never exceeds 1 (6000 random + 120 optimized points; W3 and kappa
  orbits optimized: 1.0000). Lead: the Xi sector does not obstruct K_A.

## N3. The glue network (A4) — explorations

- y2 (FLOAT, run 1 stopped by hand, kept as `.run1.*`): controls; GHZ states against W3 effects give +1/16 in both
  splits (the glue network does not see the theta conflict); unfiltered K_A generator quadruples: min 0.
- y3 (FLOAT, exact gradients; check 5.9e-11): Lift(K_A) nodes, 300 random generator quadruples x 2 BFGS starts with
  all four filters free: worst normalized min -3.4e-18 (zero). Countercontrols: GHZ states with Lift(K_A) effects,
  and mixed GHZ / Lift(K_A) nodes: minima -1.0e-18, -5.4e-19 — the glue network also does not detect those mixtures.
- y4 (FLOAT): zoo of BS* elements (GHZ, W, projector witnesses, kappa, nu, random PSD): the glue network goes
  negative, e.g. random PSD states with effects (W, W3): -2.2e-2; (kappa, PSD; PSD, W): -1.6e-2. So (A4) has teeth on
  general BS* node sets, but none was found on Lift(K_A).

### N2.3 Z and the orbit hull of K_A (`s2_zcone.py`, run 1: 5/5, `S2-ZCONE-EXACT`)

One pre-run edit (no run before it): the double-description routine was replaced by a standard incremental DD from a
simplicial start with the rank adjacency test (the first draft skipped the adjacency test before the cone was
pointed, which is not a valid shortcut). Header line D changed to match.

Exact [X P, D, G, C]: on GHZ-diagonal operators PT_1, PT_2, PT_3 keep the fibre populations and move the coherence
of fibre b to b xor 3, 2, 1; Z^GD = {|C_c| <= P_b, b != c} has 28 extreme rays (8 W3-type, 4 same-fibre pair sums,
16 "one projector per fibre" sums); all 92 generators of K_A pair >= 0 with them; Z^GD <= K_A. Countercontrols:
GHZ+ pairs to -1 with a ray; nu violates a K_A inequality (-2).
Written: the GHZ-stabilizer twirl is an LU average, so for GHZ-diagonal g, g in Z* <=> g in (Z^GD)*. Hence every
K_A generator is in Z*, and since Z* is closed, convex and filter-invariant, **Lift(K_A) <= Z*, i.e. Z <= Lift(K_A)***.
Every element of Z has a self-positive orbit (Z is self-positive and filter-invariant) and pairs >= 0 with
Lift(K_A); so cl cone(Lift(K_A) u Z) is self-positive iff Lift(K_A) is. Structural reading: K_A is a self-dual
section of the sandwich [cone(S u Z^GD), S* cap (Z^GD)*], the GD shadow of
[cone(BS u Z), BS* cap Z*] — the "Z-world" form of the lift question: is there a GL^3-invariant co-self-dual cone
between cone(BS u Z) and BS* cap Z*? (For two qubits the analogous sandwich collapses to the twin cone PT(PSD_4).)
Projector witnesses W_psi = lam(psi) I - |psi><psi| (lam = largest squared Schmidt coefficient over the cuts) are in
Z (written: the largest eigenvalue of PT_j of a pure state is its largest squared Schmidt coefficient), so they are
all in Lift(K_A)*; whether they are in Lift(K_A) is tested in y10.

Exploration y9 (FLOAT, c = 1): Lift(K_tw) self-positivity worst -4.3e-17; twin-link glue network on Lift(K_tw)
nodes, 120 random quadruples: min +2.0e-9. No lead against K_tw.
Exploration y8 (FLOAT; run 1 a harness error — a leftover placeholder einsum line raised ValueError before any
output; kept as `.run1.*`): the reshuffled operators H with <v|H|v> = tr(g' Ad(k) g) on product vectors are not PSD
for any orbit pair (min eigenvalue -1/4 for W3-W3, -3/4 otherwise), so a positive-semidefinite certificate of
self-positivity does not exist at that level; W3-W3 is positive only through the partial-transpose structure.

### N1.1 Correction and sharpening of N1: (A4) contains (A3) (`s3_glue_theta.py`, run 1: 5/5, `S3-GLUE-THETA-EXACT`)

No pre-run edit. Exact identities [X A–C]: with product effect nodes e = rho_s (x) eta_{r1 u1}, f = rho'_t (x)
zeta_{r2 u2} the glue value is tr[z (rho (x) rho')] times the theta value of the states x, y with pair effects
(w, eta, zeta); with Bell links and rho = rho' = 1/2 it is (1/32) tr(x T(y)) [X B, countercontrol without T];
symmetrically product state nodes give the theta value of the effects [X C]. Since BS <= K3 and BS <= K3* under (A1),
(A4) implies tr(x T y) >= 0 on K3 x K3 and on K3* x K3*, i.e. K3 <= T(K3*) and T(K3*) <= K3: **(A4) + (A1) => (A3)**.
N1's verdict is therefore restated: **P6 <=> (A1) and (A2) and (A4)**; (A3) is a consequence, listed for reference.
The earlier note that "the glue network does not detect the GHZ-W3 conflict" is true only when the GHZ and W3
nodes sit on opposite sides (states vs effects); with both on the same side and product nodes on the other, the glue
network is the theta network and detects it.
PN control [X P]: for the five-token countermodel (K3 = BS, K3* = BS*), product states (1/2 (x) Phi+) with effects
GHZ and W3 give -1/64: **PN violates (A4)** at six tokens (and (A3) at -1/16, EQ4-P p6 S); W3, W3 gives 1/16, QM
GHZ, GHZ gives 1/32. This is the mandatory N5 control for any route through (A4).

### N3.1 The glue network on the sector models, exhaustively (`s4_glue_sector.py`, run 1: 5/5, `S4-GLUE-SECTOR-EXACT`)

One pre-run edit (no run before it): countercontrol (i) first used pair-sum states with S* effects, whose sign I could
not predict (GD has no product states with an entangled pair factor, so the PN mechanism of s3 is not available
there); exploration y11 (integer scan) showed the S*-on-all-four-nodes quadruple (GHZ, GHZ; GHZ, W3) is negative, and
the countercontrol was changed to that before the first run.
Exact: the integer contraction agrees with eq4_lib on 6 random quadruples [X X]; **(A4) holds on all 92^4 quadruples
of K_A generators (c = 0, Bell links; minimum 0) and on all 36^4 quadruples of K_tw generators (c = 1, twin links;
minimum 0)** [X A, W]; countercontrols: S* on all four nodes reaches -4/64; K_tw with Bell links -128/64 [X C].
Structure seen in y11 (integer scan, exploration): on GD the glue tensor tau_{ijkl} has 256 nonzero entries, all equal
(4/64), supported on an index-16 subgroup of (Z_2^3)^4 cut out by four Z_2-linear relations (one of them: the four
sign bits sum to 0) — i.e. in stabilizer (Pauli) coordinates the GD glue network is a sum of 16 products of four
coordinates, one per consistent "Pauli flow" through the network.
Scope: unfiltered GD generators only — a necessary condition. Filtered nodes: exploration y3 (float).

### N2.4 Membership of Z-elements in Lift(K_A) (explorations)

- y7 (FLOAT, run 1 stopped by hand, kept as `.run1.*`): gen-vs-dual test by cutting planes in 64 dimensions did not
  converge in 400 iterations (first trial: unconverged LP bound 5.0775 vs generator max 4.9701); not informative.
- y10 (FLOAT): column generation for projector witnesses W_psi (in Z, so in Lift(K_A)*): after 300 pricing rounds
  the Farkas LP values were -1.8e-1, -7.9e-3, -3.4e-3 with pricing still finding violations (-7e-2 ... -4e-3): not
  converged; inconclusive.
- Written: S10-type projector witnesses (lam Q - GHZ with Q diagonal) are filtered W3 plus a diagonal PSD operator,
  so Z cap S10 <= Lift(K_A) (the three fibre ratios of a filtered W3 are free).

## N6. Literature (search summaries only; everything here is [L, unverified])

The search tool returned summaries; no source was read in full and nothing below is load-bearing.
- Arai–Hayashi, arXiv:2111.15019 (NJP 2023) and arXiv:2203.07968: for bipartite composites of quantum systems,
  self-duality together with local-unitary symmetry does not determine the standard entanglement structure; they
  construct infinitely many self-dual LU-symmetric models and conclude that global unitary symmetry is needed. Bearing:
  the KT setting imposes more than LU symmetry — invariance under all one-token CP maps (filters, a non-compact
  semigroup) — so their non-uniqueness does not transfer; it shows that self-duality plus a compact local symmetry is
  not enough, which is consistent with the sector models here (GD, Xi) admitting non-quantum self-dual solutions.
- Han–Kye, arXiv:1905.07678; arXiv:2010.01599; arXiv:1911.06496; arXiv:2112.05338: convex cones of three-qubit X-shaped
  operators (diagonal + anti-diagonal; GHZ-diagonal is a subclass), duals of the biseparable cones, and an infinite
  lattice generated by the three cut cones. Bearing: the X-shaped class is the twirl sector of <ZZI, IZZ> (16 dims),
  a natural intermediate sector between GD and the full space (used in y13).
- Gühne–Seevinck / Rafsanjani et al. (recalled, not retrieved): for X-states, biseparability <=> |z_i| <= sum over
  j != i of sqrt(a_j b_j). Bearing: with a single anti-diagonal pair this gives Tw(BS) cap S10 = {|c| <= min(u0,
  u1 + u2 + u3)}, which agrees with the own derivation in the S_3-symmetric sector Xi (min(u0, 3 u1)); not used.
- Barnum–Wilce arXiv:1202.4513; Barnum–Graydon–Wilce Quantum 4, 359 (2020): Jordan-algebraic systems + locally
  tomographic composites + a qubit => complex QM; without local tomography other composites exist. Bearing: they
  presuppose Jordan (homogeneous self-dual) systems; written observation (NOTES N2.5): the only GL^3-invariant
  symmetric (homogeneous self-dual) cones in Herm(8) are the PT_S(PSD_8), so any non-quantum K3 must be
  non-homogeneous.
- Das–Mani–Rai et al. (AQIS 2013 poster/submission): a GPT tripartite correlation respecting bipartite principles but
  exceeding the quantum Hardy bound — a correlation-level analogue, not a cone-level one.
- No source addressing three-token cones with quantum pairs, filter invariance and co-self-duality was found.

### N2.5 Homogeneity would force PT_S(PSD_8) (W, with the Koecher–Vinberg classification [L, unverified])

Claim: a GL(2,C)^3-invariant closed cone in Herm(8) that is symmetric (homogeneous and self-dual for some inner
product) is PT_S(PSD_8) for some token set S. Argument: GL^3 acts on Herm(8) = (R^{1,3})^{(x)3} absolutely
irreducibly (tensor product of absolutely irreducible real representations of different factors), so the connected
automorphism group cannot preserve a nontrivial decomposition into simple Jordan ideals: K is simple. Simple symmetric
cones of dimension 64 are PSD_8(C) and the Lorentz cone L_64; L_64 would need a GL^3-invariant quadratic form of
signature (1, 63), but the invariant forms are the multiples of eta^(x)3 (signature (28, 36)). So K = Phi(PSD_8)
with Phi intertwining the congruence action of an 8-dimensional representation R of GL^3 whose R (x) conj(R) matches
(C^2 (x) conj C^2)^(x)3; R is C^2 (x) C^2 (x) C^2 with some factors conjugated, and Phi is a partial transpose up to
scale (Schur). With BS <= K (c = 0) only S = {} or all tokens remain: K = PSD_8; with B_tw <= K (c = 1) no S works.
Bearing: a K3 != PSD_8 satisfying P6 must be non-homogeneous; Jordan-algebraic reconstructions (Barnum–Wilce)
presuppose exactly what is in question here. Status: written argument resting on a cited classification; not
certified; not load-bearing for any verdict.

### N2.6 The sector Xi, exactly (`s5_xi_sector.py`: run 1 6/7, VERDICT NOT RENDERED, kept as `.run1.*`; run 2 7/7, `S5-XI-SECTOR-EXACT`)

Pre-run edit before run 1 (no run before it): placeholder lines left in part A were removed.
**Run 1, harness error.** Check T compared the twirl of each of the 64 matrix units with `xi_op`, which writes the
000-111 coherence Hermitized (both entries (0,7) and (7,0)). As a linear map on all matrices the Xi projection keeps
X_07 and X_70 apart, so the two units |000><111| and |111><000| failed; the error is in the reference object, not in
the twirl. Run 2: reference `xi_proj` (the projection on all matrices), plus agreement with `xi_op` on the 64
Hermitian basis elements, plus a countercontrol (the average over all of (2 pi/4)Z^3, without the zero-sum condition,
does not keep the coherence). The header's T line carries a bracketed note recording this; nothing else changed.

Exact [X s5 + W]: (i) BS* cap Xi = {d >= 0, |c| <= u0 + u1} [X A: equality cases, countercontrol, SOS identity];
(ii) Tw_Xi(BS) = {|c| <= min(u0, 3 u1)} [X B]; (iii) K_A cap GD cap Xi = {|c| <= phi_A(u0, u1)}, phi_A = min(u0 + u1,
3 u1, (u0 + 3 u1)/2), self-dual for the form u0 v0 + 3 u1 v1 [X C]; (iv) c = 1: the bound |c| <= 2 u1 of B_tw* cap Xi is
attained by explicit PT_3 biproducts; PT_2(Psi+) (x) |+><+| twirls to |c| = (3/2) u1; K_tw cap GD cap Xi =
{|c| <= phi_tw}, phi_tw = min(2 u1, (u0 + 3 u1)/2), self-dual [X D]; (v) e1 e2 - 9 e3 = sum mu_k (mu_i - mu_j)^2 [X E].

Written, S10 (diagonal x in R^8 plus the 000-111 coherence c; pair moduli u_0 = sqrt(x_0 x_7), u_1 = sqrt(x_1 x_6),
u_2 = sqrt(x_2 x_5), u_3 = sqrt(x_4 x_3)):
- (vi) [W] GD cap S10 has GHZ eigenvalues (P0 + C, P0 - C, P1, P1, P2, P2, P3, P3). Of the 92 inequalities of K_A only
  lambda_{0-} + lambda_b >= 0, sum - 2 lambda_{0+} >= 0 and sum - 2 lambda_{0+} + 2 lambda_{0-} >= 0 involve C
  non-trivially, so K_A cap GD cap S10 = {P >= 0, |C| <= phi(P)}, phi(P) = min(P0 + min_b P_b, P1 + P2 + P3,
  (P0 + P1 + P2 + P3)/2). It is the twirl of K_A over the finite zero-sum phase group (on GD these phases only flip
  coherence signs fibre by fibre, i.e. permute GHZ labels, symmetries of the S_8-invariant K_A), so phi is self-dual for
  sum_j P_j P'_j. On Xi (P1 = P2 = P3) it is phi_A.
- (vii) [W] A diagonal filter (x) diag(1, t_j) maps x_a to x_a prod_j mu_j^{a_j} and c to c prod_j conj(t_j)
  (mu_j = |t_j|^2): every pair modulus and |c| scale by the same factor sqrt(mu1 mu2 mu3), and the only invariant of
  the populations is rho = x_0 x_3 x_5 x_6 / (x_7 x_1 x_2 x_4) (on Xi: d0 d2^3/(d3 d1^3)). On rho = 1 (x > 0) some
  diagonal filter brings X into GD. Hence, exactly: (a) {X in S10 : rho = 1, |c| <= phi(u)} <= Lift(K_A) (filter back
  an element of K_A); (b) Lift(K_A)* cap S10 cap {rho = 1} <= {|c| <= phi(u)} (filter into GD, where Tw_GD is the
  identity, and use the K_A condition). So **on the locus rho = 1 of S10 the decomposition inclusion Lift(K_A)* <=
  Lift(K_A) holds, with no self-positivity input.** Off rho = 1 the GD twirl replaces each pair's geometric mean by its
  arithmetic mean, which gives only an upper bound psi_diag for Lift(K_A)* cap S10.

### N2.7 Membership of the W witness (explorations y12, y14, y15)

- y12 (FLOAT): Wwit = (2/3) I - |W><W| is in Z, hence in Lift(K_A)* (s2 and the Schmidt-coefficient fact). In sector6
  (S_3 x U(1) phases, 6 dims) the cutting-plane LP for "Wwit not in Lift(K_A)" converged to -1.7e-6 (pricing
  -1.3e-16): lead for Wwit in Lift(K_A) up to precision. Not re-verified (see y15).
- y14 (FLOAT; W3 and BS generators only): an apparent converged value -1.12e-4. y15 (FLOAT) re-priced y14's final Y
  with 400 BFGS starts and found <Y, Ad(k) W3>/tr = -6.86e-5 < 0: y14's Y was not in the dual cone, and its
  "convergence" was a pricing artifact. **Method lesson:** a cutting-plane or column-generation value is a lead only
  after a verification re-pricing with many more starts; adopted for y16.

### N2.8 The S10 slice exactly (`s6_s10_slice.py`, run 1: 4/4, `S6-S10-SLICE-EXACT`; no pre-run edit)

Exact [X s6]: (A) the 92 inequalities of K_A restricted to GD cap S10 leave exactly the five C-bounds of phi (11
distinct C-bounds, 17 C-free forms, all with nonnegative coefficients); (B) H = {P >= 0, |C| <= phi(P)} is self-dual:
F F^T >= 0 on its 14 inequality rows and its 14 extreme rays pair >= 0 (countercontrol: dropping the form
(P0 + P1 + P2 + P3)/2 gives rays pairing to -2/9); (C) diagonal filters act on S10 by the predicted scaling and keep
rho (countercontrol: an upper-triangular filter leaves S10). This certifies the ingredients of N2.6 (vi)-(vii): the
inclusion Lift(K_A)* cap S10 cap {rho = 1} <= Lift(K_A) is now [W with exact ingredients].

### N2.9 Is the orbit hull Lift(K_A) self-dual?  Sector tests (explorations y13, y16; y19 and y20 below)

- y13 (FLOAT; gen(V) vs dual(V) for random directions V in a sector): sector6, 6 trials, all converged, gaps
  <= 3e-15 (no lead for a gap without the 000-111 coherence). S10: trial 1 converged with gap 4.8e-4; trials 0 and 2
  stopped at 299 rounds (gaps 2e-7, 4e-7); trial 3 gap 0. Omega3 (2 trials), Z3 (1 trial): unconverged at 299
  rounds, not informative; Omega3, Z3 and X16 stopped by hand (kept as `.run1.*`).
- y16 (FLOAT; sector Xi, column generation for f_low(d) = max{|c| : (d, c) in Tw_Xi(Lift(K_A))} at fixed d, with
  the bracket LP value <= f_low <= y.d + eps tr(d) and a 10x verification re-pricing). Run 1 stopped by hand (the BFGS
  floor ~5e-9 sat above the 1e-10 stopping threshold; brackets at stop agree with run 2), kept as `.run1.*`;
  run 2 (threshold 1e-8) results:

  | target d | rho | min(u0, 3u1) = Tw(BS) | f_low bracket | phi_A (C_A) | psi_diag (Lift* bound) | reading |
  |---|---|---|---|---|---|---|
  | (1,1,1,1) control | 1 | 1 | [2.00000000, 2.00000005] (support 8 kappa) | 2 | 2 | no gap |
  | (4,1,1,1) | 4 | 2 | [2.47398967, 2.47398973] | 2.5 | 2.53442 | gap lead |
  | (1,1,1,4) (XXX mirror of the previous) | 1/4 | 2 | [2.47398966, 2.47398971] | 2.5 | 2.53442 | gap lead |
  | (1,1,2,2) | 4 | 1.41421 | [2.60546426, 2.60546435] | 2.82843 | 2.82843 | gap lead |
  | (1,2,1,1) | 1/8 | 1 | [2.23633968, 2.23633974] | 2.41421 | 2.41421 | gap lead |
  | (16,1,1,1) | 16 | 3 | [2.99999995, 3.00000004] | 3 | 3 | no gap (BS already) |

  Control (run 1): the biseparable-only column set at (4,1,1,1) gives [1.99999999, 2.00000003] = min(u0, 3 u1), the
  exact Tw_Xi(BS) value of s5 B. The two mirror targets agree to 1e-8.
  Reading: off rho = 1 the Xi-section of Lift(K_A) is strictly inside C_A wherever phi_A exceeds the biseparable
  value. Since C_A is self-dual in Xi [X s5 C] and equals the section on rho = 1 [W + X s6], Lift(K_A) cap Xi
  strictly inside C_A gives Lift(K_A)* cap Xi strictly outside C_A, i.e. **Lift(K_A) != Lift(K_A)* (lead)**: the LP
  dual at (1,1,2,2), Y = sum_w (y_w / C(3,w)) Pi_w - (1/2)(|000><111| + h.c.), has moduli u0 = 1/3, u1 = 1/6,
  |c| = 1/2 (to the printed precision) — the corner |c| = u0 + u1 = 3 u1 of BS* cap Z* — outside C_A
  (phi_A = 5/12), at rho ~ 5.6e-3. y21 (FLOAT): its diagonal-filter bound is tight, psi_diag = 0.49999998 = |c|,
  through the piece P0 + min_b P_b (the BS* boundary; the middle piece has slack, 0.599 at the optimum), while the
  same moduli at rho = 1 give psi_diag = 5/12 < 1/2 (middle piece binding), as the exact statement N2.6 (vii)(b)
  requires. So the extra room in Lift(K_A)* comes from moving rho away from 1. Independent re-check of this Y: y19.

## N4. c = 1 (K_tw)

- Exact, earlier in this walk: twin-link (A4) on all 36^4 quadruples of K_tw generators, minimum 0 (Bell links
  instead give -128/64) [X s4]; the Xi facts of N2.6 (iv) [X s5 D]; the five-token twin conditional and the twin
  theta value (1/8) tr(x y) [X s1 G], so (A4) + (A1) give K3 = K3* exactly as at c = 0 [X s3 A + W].
- **S10 slice (`s7_s10_slice_c1.py`, run 1: 3/3, `S7-S10-SLICE-C1-EXACT`; no pre-run edit).** The 36 inequalities of
  K_tw restricted to GD cap S10 leave exactly the C-bounds (P0 + P1 + P2 + P3)/2, P1 + P2, P1 + P3, P2 + P3, i.e.
  |C| <= phi_tw(P) = min((P0 + P1 + P2 + P3)/2, P1 + P2 + P3 - max_b P_b); the slice is self-dual (12 rows, 12 rays;
  countercontrol -1/4). With s6 C (filter action, independent of c) the argument of N2.6 (vii) gives exactly as at
  c = 0: **on rho = 1, Lift(K_tw)* cap S10 <= Lift(K_tw)** [W with exact ingredients].
- y9 (FLOAT, earlier): Lift(K_tw) self-positivity worst -4.3e-17; twin-link glue network on filtered nodes, minimum
  +2.0e-9.
- y18 (FLOAT; c = 1 version of y16: generators t0a, t0b (twirls of twin-hull elements) and k0 = 1 - 2P_{0+} + 2P_{0-};
  pricing over pure twin-hull elements |a><a| (x) PT_j(|chi><chi|)): see N4.1 below.

### N4.1 Exploration y18 (FLOAT; c = 1 Xi profile)

| target d | rho | f_low bracket (after 10x verification re-pricing) | phi_tw (C_tw) | psi_tw | reading |
|---|---|---|---|---|---|
| (1,1,1,1) control | 1 | [2.00000000, 2.00000003] | 2 | 2 | no gap |
| (1,1,2,2) | 4 | [2.59028001, 2.59028013] | 2 sqrt 2 = 2.82843 | 2.82843 | gap lead |

The control ran as `.par` (in parallel with the chain); the chain's own repeat of the control (same seed) was stopped
by hand and kept as `.run1.*`; the chain's targets "t1 twin" (check of the written Tw_Xi(B_tw) value) and "t5" were
not run. Reading: as at c = 0, the orbit hull of K_tw is (lead) not co-self-dual off rho = 1, while on rho = 1 the lift
is forced exactly (N4, s7).

## N7. Integrity events during the walk (recorded when found, 11:00 UTC)

- **Write outside SIX by this thread (harness error), found by a concurrent review thread.** At 10:10:19 UTC a
  background launch of y13 for the Z3 sector used the shell form `cd SIX && A & B &`; the `cd` applies only to A's
  background subshell, so B ran in the session working directory, the repository root. It failed to open the script
  (relative path; exit 2), and its redirections created `y13_sector_gap_float.Z3.out` (empty) and
  `y13_sector_gap_float.Z3.err` (the interpreter's error line and "exit 2") in the repository working tree. This
  thread logged the launch as "ended immediately without files" and did not notice them. The review thread moved both
  files, content and mtime unchanged, to `scratchpad/eqreview/quarantine-SIX-stray/` with a hash manifest
  (10:21:33 UTC) and asked for this record. Checked read-only here: the hashes match the manifest (ddc51deb...,
  e3b0c442... = empty file), and neither file is in the working tree any more. They are not data. Lesson: background
  runs use the tool's background mode with absolute paths, never `cd X && A & B &`.
- **Unaccounted files in the repository working tree, not written by this thread.** `git status --porcelain` lists three
  untracked files: `verification/lean-mathlib/OIBridge/FourCopyBridge.lean` (mtime 10:56:02 UTC, 15961 bytes, sha256
  febb3d1fc9658275...), `FourCopyCore.lean` (10:54:50, 9740 bytes, 9fce26e66fdec1e9...), `FourCopyLocal.lean`
  (10:58:51, 13629 bytes, a9e9434d10b3c5e8...). This thread writes no Lean text. The names match drafts of a
  concurrent formalization thread (`scratchpad/eq5/F/drafts/`), whose FourCopyBridge.lean differs (15043 bytes,
  c14ac37e...), so the files cannot be sourced exactly to that thread or to the pristine checkout. Sweep (§A.26):
  SIX holds only files this thread wrote; no script of this thread reads the repository working tree (they read only
  SIX and the base snapshot); the base and inputs manifests are re-verified at the end; every exact script is replayed
  byte for byte. The files are left in place (writes outside SIX are not authorized here) and flagged for the owner.
- y22 pre-run edit (no run before it): its countercontrol first used rank-one product effects, for which the network is
  >= 0 by conditioning (it would test nothing); changed to the biseparable effects (1/2) 1 (x) Phi+, for which the
  unfiltered network is (1/32) tr(x T y) (s3 B).

### N2.10 Independent re-check of the dual, and the C_A boundary point (explorations y19, y20, y21)

- y19 (FLOAT; dense matrices, filters k_j = expm(H_j), 20000 random filters with log-normal scales, Nelder-Mead from
  the 30 best, S_3-symmetric filters; no code shared with y16's pricing). The y16 dual Y at (1,1,2,2): moduli
  u0 = 0.3333333, u1 = 0.1666667, |c| = 1/2, rho = 5.593e-3, phi_A(u_Y) = 5/12; <Y, X_t> = -0.2229629.
  Minima: <Y, Ad(k) W3>/tr -1.7e-16, kappa -5.2e-9, omega +2.7e-2; biseparable pure states -7.2e-9. All >= -1e-7:
  the lead "Y in Lift(K_A)*" survives the independent search (countercontrol below).
- y20 (FLOAT; same search code): the C_A boundary point X_t = ((1,1,2,2), c = 2 sqrt 2) at rho = 4.
  (i) X_t in Lift(K_A)*?  W3 orbit +0.433, kappa orbit +0.020, omega orbit +0.626, biseparable -4.2e-16: lead yes.
  So Lift(K_A)* contains both X_t (inside C_A, not in Lift(K_A) by y16) and Y (outside C_A), with
  <X_t, Y> = -0.223 < 0: **any K_A-lift contains at most one of them** — the lift is a choice (lead).
- y21: see N2.9 (the diagonal-filter bound of Y is tight through the BS* piece).

### N3.2 Random-start minima of normalized networks are not evidence (exploration y23) — hidden assumption exposed

- y22 (FLOAT, run 1 stopped by hand, kept as `.run1.*`): glue network with X_t or Y as nodes; its countercontrol
  (X_t, Y as states; (1/2) 1 (x) Phi+ effects) returned -2.6e-18 although s3 B predicts (1/32) tr(X_t T(Y)) < 0.
- y23 (FLOAT; harness check): the y3 contraction is right — at identity filters it gives -0.00696759 =
  (1/32) tr(X_t Y^T), and the s3 PN quadruple gives -0.015625 = -1/64 exactly as s3. But BFGS from 10 random filter
  starts returns minima in [-8e-20, 8e-14] for the y22 quadruple, while BFGS started at identity filters reaches
  -2.24e-3 (normalized). Random-start minimization of the normalized network slides to degenerate filters where the
  value vanishes. **Exposed hidden assumption (in this walk's own float evidence): that a random-start minimum near 0
  means no negative value exists.** It voids, as evidence, the minima of y1 (orbit-hull self-positivity), y3 (glue
  network on filtered Lift(K_A) nodes, including its GHZ countercontrols, which were never negative), y9 (c = 1) and
  y22. Found negative values (y4's zoo) stand. EQ4-P's float leads x9 and x16 (filter-orbit co-self-positivity,
  "worst -5e-17") were obtained by random-start searches as well (their headers, read here: "random starts + BFGS",
  starts `rng.normal(size=24)`), so the same caveat applies to them; y24 and y25 (i) re-check exactly those orbit
  pairs with structured starts. Re-checks with structured starts (Clifford points, perturbed): y24 (c = 0),
  y25 (c = 1).

### N3.3 Structured-start re-checks (explorations y24, y25), partial at the time of writing

- y24 (FLOAT, c = 0; starts at products of one-qubit Cliffords times exp(eps H), eps in {0, 0.02, 0.1, 0.3, 1}):
  (i) countercontrol (W3, GHZ) -0.354 (found); control (W3, W3) +8e-19; orbit-hull self-positivity minima:
  (kappa, kappa) -7.9e-17, (kappa -> omega) +1.8e-19, (omega -> kappa) +0.125, (omega, omega) -2.3e-17. No violation;
  the lead "Lift(K_A) is self-positive" is restored on this better search. (ii) glue network: below.
- y25 (FLOAT, c = 1, same starts): (i) countercontrol (k0, GHZ+) -0.250 (found); k0-orbit pairs minimum -7.0e-17.
  No violation. (ii) twin-link glue network: below.

### N2.5 addendum (a gap in the written argument, found while writing RESULT)

The bearing drawn in N2.5 ("a K3 != PSD_8 satisfying P6 must be non-homogeneous") needs, for c = 0, that a
homogeneous K3 with K3 = T(K3*) is symmetric, i.e. self-dual for some positive-definite inner product. K3 = T(K3*) is
self-duality for the indefinite form tr(X T Y) (on Herm(8) it is negative on, e.g., sigma_y in one token), so this step
is not justified here (it holds if K3 is T-invariant, since then K3* = K3 for the trace form). For c = 1 (K3 = K3*,
Euclidean) the step is immediate. N2.5 stays a remark, not load-bearing; RESULT §2 records the gap.

## N8. Pass accounting for the fixed point (§A.31)

Each pass is one depth-first branch closed by a check. Classification per §A.31:

| pass | branch | check | class |
|---|---|---|---|
| 1 | N1 constraint system | s1 | NEW (G1) |
| 2 | Xi sector leads | y5, y6 | ELABORATING |
| 3 | glue-network explorations | y2–y4 (y3 later void) | ELABORATING |
| 4 | Z-sandwich | s2 | POSITIVE |
| 5 | (A4) => (A3); PN control | s3 | NEW (sharpens G1) |
| 6 | (A4) on generator quadruples | s4, y11 | POSITIVE |
| 7 | Z-elements in Lift(K_A) | y7, y10, written | CONFIRMING / inconclusive |
| 8 | literature | N6 | BORDERLINE |
| 9 | homogeneity | N2.5 (+ addendum) | ELABORATING |
| 10 | Xi exactly | s5 | POSITIVE |
| 11 | W witness | y12, y14, y15 | CONFIRMING (+ method lesson) |
| 12 | sector gap scan | y13 | BORDERLINE |
| 13 | S10 slice; lift forced on rho = 1 | s6 | POSITIVE |
| 14 | Xi profile by column generation | y16 | NEW (F): orbit hull not co-self-dual |
| 15 | c = 1 profile and slice | y18, s7 | CONFIRMING / POSITIVE |
| 16 | independent re-check; C_A point | y19, y20, y21 | CONFIRMING / ELABORATING |
| 17 | glue network with the gap candidates; harness check | y22, y23 | NEW (G2: random-start minima are not evidence) |
| 18 | structured-start re-checks | y24, y25, y26 | CONFIRMING (no violation; leads restored) |
| 19 | which choice survives (A4) | y27 | CONFIRMING (neither choice excluded) |
| 20 | C_A boundary at other points; sign control | y20, y28, y29 | CONFIRMING (t1, t3); y20 artifact found and corrected (ELABORATING G2) |

### N3.3 (completed) Structured-start re-checks and the choice test (explorations y24, y25 run 2, y26, y27)

- y24 (ii) glue network on Lift(K_A) nodes, 40 random generator quadruples, structured starts: worst normalized
  minimum -1.2e-17; countercontrols found: PN quadruple -2.21e-2, y23 quadruple -2.24e-3. No violation: the lead
  "(A4) holds on filtered orbit-hull nodes" is restored on the better search (y24 output's stderr ended "done"; its
  exit code was not captured, the run having been launched with `&` from a foreground `cd`).
- y25 run 2 (c = 1): (ii) twin-link glue network on Lift(K_tw) nodes, 10 quadruples: worst +4.5e-14; countercontrol
  (GHZ+, k0; (1/2) 1 (x) SWAP/2 effects) -1.56e-2. Run 1 (20 quadruples, single final print) was stopped by hand as
  too slow and kept as `.run1.*`. No violation at c = 1.
- y26 (the y16 dual Y, structured starts): W3 -1.1e-16, kappa -5.2e-9, omega +2.73e-2; countercontrol (coherence
  x 1.05) -1.21e-2. The lead "Y in Lift(K_A)*" survives a third, independent search.
- y27 (which choice survives (A4)?): with the C_A point X_t, and separately with Y, as nodes among K_A generator nodes
  (all four positions; one position, 16 quadruples; both states, 16; both effects, 16), every minimum lies in
  [-1.2e-17, -1.7e-18]; countercontrols found (-2.21e-2, -2.24e-3). Reading: **(A4) excludes neither choice on these
  tests**; the choice between X_t and Y (they pair to -0.223) is not decided by (A4) at this level. CONFIRMING.

### N2.11 The C_A boundary at other points; a sign artifact in the y19/y20 search code (explorations y20 t1, t5; y28)

- y20 t5 (X_t = ((1,2,1,1), c = 1 + sqrt 2), rho = 1/8): W3 +0.553, kappa +0.144, omega +0.683, biseparable -2.2e-16,
  orbit self-positivity +0.212 (countercontrol: see below).
- y20 t1 (X_t = ((4,1,1,1), c = 5/2), rho = 4): kappa +0.016, omega +0.375, biseparable +0.219, orbit
  self-positivity 0.000, but **W3 -0.333**, with numpy overflow warnings in its stderr. Written argument: the true
  value is >= 0, since X_t is in Z* (Z* cap Xi = {|c| <= 3 u1} and 5/2 <= 3) and every Ad(k) W3 is in Z.
- y28 (sign control, §A.21): the same search with non-finite values discarded gives +1/6 at a unitary filter
  (condition numbers 1); the exact rational value at the rationalized minimizer is +1/6 (numerator and trace both
  positive); structured starts give +1/6. **The y20 t1 W3 value is an artifact**: y19/y20 let overflowed (inf/NaN)
  values from very large random filters enter the sort and the minimum. y19's t3 values are independently reproduced
  by y26 (structured starts: -1.1e-16, -5.2e-9, +2.73e-2, the same numbers), so y19 stands; y20 t3 and t5 values are
  positive or ~0 and consistent with the written Z/Z* bounds; y20 t1's W3 entry is replaced by y28's +1/6.
- Reading (provisional, before y29): the C_A boundary points tested looked compatible; see y29 below for the reading of record.
- y29 (FLOAT; y20 redone with y26's structured starts, non-finite values discarded):

  | point | W3 | kappa | omega | orbit self-pairing | countercontrol (x 1.05) | reading |
  |---|---|---|---|---|---|---|
  | t1 (4,1,1,1; 5/2) | +1/6 | +0.0162 | +0.375 | +0.135 | -0.0428 | X_t in Lift(K_A)*, self-positive orbit (lead) |
  | t3 (1,1,2,2; 2 sqrt 2) | +0.433 | +0.0203 | +0.625 | -4.7e-16 | -0.0473 | the same (lead) |
  | t5 (1,2,1,1; 1 + sqrt 2) | +0.553 | +0.144 | +0.573 | +0.212 | **+0.085** | not rendered |

  At t5 the countercontrol is not green: there X_t sits on the BS* bound |c| = u0 + u1 (exact, s5 A), so the 5%
  overshoot leaves BS*, a constraint this search does not contain (it tests the W3, kappa and omega orbits only). By
  the decision rule the t5 reading is not rendered; the t1 and t3 readings stand. The y20 values are superseded.

## N9. Integrity at the end (11:48 UTC)

- `cd scratchpad/eq/base && sha256sum -c --quiet ../base.manifest.sha256`: silent, exit 0. Inputs manifest: silent,
  exit 0. `eq5/PROTOCOL.md` unchanged (mtime 08:16:07, sha256 c0fbe625c416692d...).
- HEAD moved: `1310e62971299728f731f302a9896a2b63f711b2` on `claude/network-tool-access-8jtdhm`, "EQ4-F design run 1
  (not for merge): Pauli-free route KT(4) -> IE1 ∧ parity", 11:42:46 UTC (reflog read-only: HEAD@{0} that commit,
  HEAD@{1} f0d37906). It adds or modifies `verification/lean-mathlib/OIBridge.lean` and nine `OIBridge/FourCopy*.lean`
  files. This thread made no git write. Working tree clean at the end.
- The three untracked Lean files of N7 are in that commit (FourCopyCore identical to the recorded hash; Bridge and
  Local edited further before the commit): provenance resolved to the concurrent EQ4-F thread.
- No process of this thread is still running. Every exact script (s1-s7) was replayed byte for byte (`replay/`).
