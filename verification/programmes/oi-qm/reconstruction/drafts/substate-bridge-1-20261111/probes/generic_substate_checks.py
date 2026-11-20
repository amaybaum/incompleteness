#!/usr/bin/env python3
"""SUBSTATE-BRIDGE-1 unit 1 -- exact generic checks S1-S7 (13 lines).

Run:  python3 -I -B generic_substate_checks.py
Exact arithmetic only (fractions, integers). Fixed seed. No OI rule, carrier,
coupling, preparation or simulator is encoded: every object below is a generic
mathematical object (stochastic matrices, a qubit frame, response tables).
The checks support the paper arguments of SUBSTATE-BRIDGE-UNIT1.md; they do not
replace them.
"""
from fractions import Fraction as Fr
from itertools import product
import random
import sys

random.seed(20261111)
RESULTS = []


def record(name, ok, detail=""):
    RESULTS.append((name, bool(ok), detail))


# ---------------------------------------------------------------------------
# S1. Saturation: every finite outcome-indexed nonnegative column-stochastic
#     family on a finite carrier is induced by a *finite* hidden register with a
#     fixed prior and one bijection.  (So an infinite hidden carrier cannot add
#     a single-procedure induced map to the class K: K_infinite subset K = K_finite.)
# ---------------------------------------------------------------------------
def random_family(n_in, n_out, n_a, denom=7):
    """T[(s2,a)][s] >= 0 rational, column sums 1."""
    fam = {}
    cols = []
    for s in range(n_in):
        w = [random.randint(0, denom) for _ in range(n_out * n_a)]
        if sum(w) == 0:
            w[0] = 1
        tot = sum(w)
        cols.append([Fr(x, tot) for x in w])
    for idx, (s2, a) in enumerate(product(range(n_out), range(n_a))):
        fam[(s2, a)] = [cols[s][idx] for s in range(n_in)]
    return fam


def s1_case(n_in, n_out, n_a):
    fam = random_family(n_in, n_out, n_a)
    outs = list(product(range(n_out), range(n_a)))
    m = len(outs)
    # hidden register: all functions r : carrier -> outputs, product prior
    regs = list(product(range(m), repeat=n_in))
    prior = {}
    for r in regs:
        p = Fr(1)
        for s in range(n_in):
            p *= fam[outs[r[s]]][s]
        prior[r] = p
    if sum(prior.values()) != 1:
        return False
    # one bijection on carrier x register x Z_m : (s, r, o) -> (s, r, o + r(s))
    states = [(s, r, o) for s in range(n_in) for r in regs for o in range(m)]
    image = {(s, r, (o + r[s]) % m) for (s, r, o) in states}
    if len(image) != len(states):
        return False
    # induced kernel, output register started at o = 0, prior independent of s
    for s in range(n_in):
        acc = {o: Fr(0) for o in range(m)}
        for r in regs:
            acc[r[s] % m] += prior[r]
        for o in range(m):
            if acc[o] != fam[outs[o]][s]:
                return False
    return True


record("S1 finite dilation realizes arbitrary nonnegative families (6 cases)",
       all(s1_case(*shape) for shape in [(2, 2, 2), (2, 2, 2), (2, 3, 1), (3, 2, 1), (2, 2, 3), (3, 2, 2)]))


# ---------------------------------------------------------------------------
# S2. A continuum frame in which a unitary acts by a point map (qubit Husimi
#     frame):  Q_rho(n) = 1 + r.n  on the unit sphere (density w.r.t. normalized
#     area), and Q_{U rho U^dagger}(n) = Q_rho(R^T n) for the rotation R of U.
#     Checked exactly at rational points of the sphere with a rational rotation.
# ---------------------------------------------------------------------------
def rational_sphere_points():
    pts = set()
    for (p, q, r, t) in [(1, 2, 2, 3), (2, 3, 6, 7), (1, 4, 8, 9), (4, 4, 7, 9), (2, 6, 9, 11), (6, 6, 7, 11)]:
        for signs in product((1, -1), repeat=3):
            for perm in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
                v = [Fr(p, t), Fr(q, t), Fr(r, t)]
                v = [signs[i] * v[perm[i]] for i in range(3)]
                pts.add(tuple(v))
    return sorted(pts)


def matvec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(3)) for i in range(3))


def transpose(M):
    return [[M[j][i] for j in range(3)] for i in range(3)]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


c, s_ = Fr(3, 5), Fr(4, 5)
R1 = [[c, -s_, 0], [s_, c, 0], [0, 0, 1]]           # rational rotation about z
R2 = [[1, 0, 0], [0, c, -s_], [0, s_, c]]           # rational rotation about x
R = [[sum(R1[i][k] * R2[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
PTS = rational_sphere_points()
ok_sphere = all(dot(n, n) == 1 for n in PTS)
ok_orth = all(sum(R[i][k] * R[j][k] for k in range(3)) == (1 if i == j else 0)
              for i in range(3) for j in range(3))
blochs = [(Fr(1, 3), Fr(-1, 2), Fr(1, 4)), (Fr(0), Fr(0), Fr(1)), (Fr(2, 3), Fr(2, 3), Fr(-1, 3))]
ok_cov = True
ok_pos = True
for r in blochs:
    assert dot(r, r) <= 1
    Rr = matvec(R, r)
    for n in PTS:
        q_rot = 1 + dot(Rr, n)                       # Q of the rotated state at n
        q_pull = 1 + dot(r, matvec(transpose(R), n))  # Q of the state at R^T n
        ok_cov &= (q_rot == q_pull)
        ok_pos &= (q_rot >= 0)
record("S2 qubit Husimi frame: rotation acts as a point map; densities nonnegative "
       f"({len(PTS)} rational points, 3 states)", ok_sphere and ok_orth and ok_cov and ok_pos)

# S2b. Countercontrol: in a finite frame the same kind of operation is NOT nonnegative.
#      Rational tetrahedral frame E_k = (I + r_k.sigma)/4, r_k = (+-1/2, +-1/2, +-1/2) (even signs).
#      Frame matrix of a rotation R solves  p_k(R r) = sum_j F_kj p_j(r)  for all r.
RK = [(Fr(1, 2), Fr(1, 2), Fr(1, 2)), (Fr(1, 2), Fr(-1, 2), Fr(-1, 2)),
      (Fr(-1, 2), Fr(1, 2), Fr(-1, 2)), (Fr(-1, 2), Fr(-1, 2), Fr(1, 2))]


def frame_matrix(Rm):
    # p_k(r) = (1 + r_k.r)/4.  Dual frame: r = (4/ (4*|r_k|^2/3)) * sum_j p_j r_j ... solved directly:
    # sum_j p_j r_j = (1/4) sum_j (r_j.r) r_j = (1/4) * (4 * 1/4) r = r/4   (since sum_j r_j r_j^T = I)
    # hence r = 4 sum_j p_j r_j and, with sum_j p_j = 1,
    # p_k(R r) = 1/4 + (1/4) r_k.R(4 sum_j p_j r_j) = sum_j p_j (1/4 + r_k.(R r_j))
    return [[Fr(1, 4) + dot(RK[k], matvec(Rm, RK[j])) for j in range(4)] for k in range(4)]


gram_ok = all(sum(RK[j][a] * RK[j][b] for j in range(4)) == (1 if a == b else 0)
              for a in range(3) for b in range(3))
F = frame_matrix(R1)
col_ok = all(sum(F[k][j] for k in range(4)) == 1 for j in range(4))
# verify F reproduces the action on test states
act_ok = True
for r in blochs:
    p = [(1 + dot(RK[k], r)) / 4 for k in range(4)]
    pR = [(1 + dot(RK[k], matvec(R1, r))) / 4 for k in range(4)]
    act_ok &= (pR == [sum(F[k][j] * p[j] for j in range(4)) for k in range(4)])
min_entry = min(min(row) for row in F)
record("S2b finite tetrahedral frame: frame matrix of a rational rotation has a negative entry "
       f"(min {min_entry})", gram_ok and col_ok and act_ok and min_entry < 0)


# S2c. Overcomplete finite frame: octahedral frame p_k(r) = (1 + r.n_k)/6 on the six
#      axis points.  It is linear and injective but does not span R^6.  The Hadamard
#      rotation (x,y,z) -> (z,-y,x) permutes the six points, so it acts on the frame
#      by a permutation matrix (nonnegative), although its conjugation does not
#      preserve diagonal matrices.
OCT = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
HAD = [[0, 0, 1], [0, -1, 0], [1, 0, 0]]
perm_ok = sorted(matvec(HAD, n) for n in OCT) == sorted(OCT)
act_ok2 = True
for r in blochs:
    p = {n: (1 + dot(r, n)) / 6 for n in OCT}
    Hr = matvec(HAD, r)
    for n in OCT:
        # p_n(H r) = p_{H^T n}(r): a permutation of the six entries
        act_ok2 &= ((1 + dot(Hr, n)) / 6 == p[matvec(transpose(HAD), n)])
# the Hadamard conjugation sends the diagonal state r = (0,0,1) to r = (1,0,0), not diagonal
nondiag = matvec(HAD, (0, 0, 1)) == (1, 0, 0)
rel_ok = all(((1 + dot(r, OCT[2 * a])) / 6 + (1 + dot(r, OCT[2 * a + 1])) / 6) == Fr(1, 3) for r in blochs for a in range(3))
record("S2c octahedral (non-spanning) finite frame: Hadamard acts by a permutation of the frame",
       perm_ok and act_ok2 and nondiag and rel_ok)


# ---------------------------------------------------------------------------
# S3. Single-POVM lemma, finite instance: every post-processing of one fixed
#     POVM is unsharp.  For the tetrahedral qubit POVM, an effect
#     F = sum_k w_k E_k (0 <= w_k <= 1) is (t I + v.sigma) with t = sum w/4,
#     v = sum w_k r_k / 4.  A rank-one projector needs t = 1/2 and |v| = 1/2.
#     On {w in [0,1]^4 : sum w = 2} the convex function |v|^2 is maximal at a
#     vertex (two weights 1, two 0).  Enumerate the vertices exactly.
# ---------------------------------------------------------------------------
best = Fr(0)
for w in product((0, 1), repeat=4):
    if sum(w) != 2:
        continue
    v = tuple(sum(w[k] * RK[k][a] for k in range(4)) / 4 for a in range(3))
    best = max(best, dot(v, v))
record(f"S3 no post-processing of the tetrahedral POVM is a rank-one projector (max |v|^2 = {best} < 1/4)",
       best < Fr(1, 4))


# ---------------------------------------------------------------------------
# S4. Channel + pad.  A fair shared bit d (the 'pad') and a response of wing A
#     that depends on the remote setting b (the 'channel'):
#         h_A = d xor (a and b),  h_B = d.
#     (i) with a fair pad: no-signalling marginals and CHSH = 4 (the PR box);
#     (ii) with a biased pad: wing A's marginal depends on b (signalling);
#     (iii) without the channel (h_A = d xor (a and c), c local): CHSH <= 2.
# ---------------------------------------------------------------------------
def joint(pd1, with_channel=True):
    P = {}
    for a, b in product((0, 1), repeat=2):
        law = {}
        for d, pd in ((0, 1 - pd1), (1, pd1)):
            hA = d ^ ((a & b) if with_channel else (a & 1))
            hB = d
            law[(hA, hB)] = law.get((hA, hB), Fr(0)) + pd
        P[(a, b)] = law
    return P


def marg_A(P, a, b):
    return sum(p for (hA, _), p in P[(a, b)].items() if hA == 1)


def chsh(P):
    def E(a, b):
        return sum((1 if hA == hB else -1) * p for (hA, hB), p in P[(a, b)].items())
    return E(0, 0) + E(0, 1) + E(1, 0) - E(1, 1)


P_fair = joint(Fr(1, 2))
P_bias = joint(Fr(1, 3))
P_loc = joint(Fr(1, 2), with_channel=False)
ns_fair = all(marg_A(P_fair, a, 0) == marg_A(P_fair, a, 1) for a in (0, 1))
ns_bias = all(marg_A(P_bias, a, 0) == marg_A(P_bias, a, 1) for a in (0, 1))
record("S4 channel + fair pad: no-signalling and CHSH = 4", ns_fair and chsh(P_fair) == 4)
record("S4 channel + biased pad: signalling (countercontrol)", not ns_bias)
record("S4 pad without channel: CHSH <= 2 (countercontrol)", abs(chsh(P_loc)) <= 2)


# ---------------------------------------------------------------------------
# S5. A shared mode that both wings read and neither setting writes is a common
#     cause: for random response functions h_A(m, lA, a), h_B(m, lB, b) and random
#     rational priors on (m, lA, lB) -- correlated priors included -- |CHSH| <= 2.
# ---------------------------------------------------------------------------
def s5_case():
    M, LA, LB = 3, 2, 2
    hA = {(m, l, a): random.choice((-1, 1)) for m in range(M) for l in range(LA) for a in (0, 1)}
    hB = {(m, l, b): random.choice((-1, 1)) for m in range(M) for l in range(LB) for b in (0, 1)}
    w = {k: random.randint(0, 5) for k in product(range(M), range(LA), range(LB))}
    tot = sum(w.values()) or 1
    def E(a, b):
        return sum(Fr(w[(m, x, y)], tot) * hA[(m, x, a)] * hB[(m, y, b)] for (m, x, y) in w)
    S = E(0, 0) + E(0, 1) + E(1, 0) - E(1, 1)
    return abs(S) <= 2


record("S5 read-only shared mode is Bell-local (300 random cases)", all(s5_case() for _ in range(300)))


# ---------------------------------------------------------------------------
# S6. Trace-out over a hidden factor with an invariant product prior is doubly
#     stochastic; with a non-invariant prior it need not be (finite illustration
#     of the identity used in the text for a general hidden measure).
# ---------------------------------------------------------------------------
def s6():
    V, H = 2, 4
    states = [(v, h) for v in range(V) for h in range(H)]
    perm = states[:]
    random.shuffle(perm)
    phi = dict(zip(states, perm))
    def T(prior):
        return [[sum(prior[h] for h in range(H) if phi[(i, h)][0] == j) for j in range(V)] for i in range(V)]
    uni = [Fr(1, H)] * H
    Tu = T(uni)
    ds_uniform = all(sum(Tu[i][j] for i in range(V)) == 1 for j in range(V))
    return ds_uniform, phi


ok6 = True
found_counter = False
for _ in range(50):
    ds, phi = s6()
    ok6 &= ds
    pt = [Fr(1), Fr(0), Fr(0), Fr(0)]
    Tp = [[sum(pt[h] for h in range(4) if phi[(i, h)][0] == j) for j in range(2)] for i in range(2)]
    if any(sum(Tp[i][j] for i in range(2)) != 1 for j in range(2)):
        found_counter = True
record("S6 invariant (uniform) hidden prior: trace-out doubly stochastic (50 bijections)", ok6)
record("S6 non-invariant hidden prior: double stochasticity can fail (countercontrol)", found_counter)


# ---------------------------------------------------------------------------
# S7. A relabelling that preserves the *unconditional* law of the hidden bit
#     does not give no-signalling when the remote setting is correlated with it.
#     One hidden bit r, remote setting b, near history h = r xor b.
#     Joint law of (b, r): P(b=0) = 1/3, P(r=0|b=0) = 1, P(r=0|b=1) = 1/4.
#     Then r is uniform (the flip r -> 1-r preserves its law, and h(flip r, b')
#     = h(r, b) for b' != b), the history laws computed under the unconditional
#     law of r agree for b = 0, 1, and yet P(h=0|b) differs.
#     Control: same marginals, b independent of r -> no signalling.
# ---------------------------------------------------------------------------
def s7(joint_br):
    pb = {b: sum(joint_br[(b, r)] for r in (0, 1)) for b in (0, 1)}
    pr = {r: sum(joint_br[(b, r)] for b in (0, 1)) for r in (0, 1)}
    flip_preserves_marginal = pr[0] == pr[1]
    # history law under the unconditional law of r, for each fixed b
    uncond = {b: sum(pr[r] for r in (0, 1) if r ^ b == 0) for b in (0, 1)}
    # operational law: P(h = 0 | b)
    cond = {b: sum(joint_br[(b, r)] for r in (0, 1) if r ^ b == 0) / pb[b] for b in (0, 1)}
    return flip_preserves_marginal, uncond[0] == uncond[1], cond[0] == cond[1], cond


J_corr = {(0, 0): Fr(1, 3), (0, 1): Fr(0), (1, 0): Fr(1, 6), (1, 1): Fr(1, 2)}
J_ind = {(b, r): (Fr(1, 3) if b == 0 else Fr(2, 3)) * Fr(1, 2) for b in (0, 1) for r in (0, 1)}
f1, u1, c1, cond1 = s7(J_corr)
f2, u2, c2, _ = s7(J_ind)
record(f"S7 marginal-preserving relabelling, setting correlated with the pad: signalling "
       f"(P(h=0|b) = {cond1[0]}, {cond1[1]})", f1 and u1 and not c1)
record("S7 same marginals, setting independent of the pad: no signalling (control)", f2 and u2 and c2)


# ---------------------------------------------------------------------------
width = max(len(n) for n, _, _ in RESULTS)
for name, ok, detail in RESULTS:
    print(f"{'PASS' if ok else 'FAIL'}  {name}")
n_fail = sum(1 for _, ok, _ in RESULTS if not ok)
print(f"{len(RESULTS)} checks, {n_fail} failed")
sys.exit(1 if n_fail else 0)
