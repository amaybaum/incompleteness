"""E2 probe 1 -- K-inf-Copy: is "type covariance of native inversion" a sufficient weakening?  (exact; Fractions)

QUESTION (ROADMAP.md:1027-1030 at L).  Copy naturality (one NOT N in both of DIM-1's relations) is load-bearing: the
two-NOT J/K maps of NB-1 at d = 5 and d = 7 meet every two-copy relation with mismatched NOTs.  The candidate weakening:
the target copy's NOT is the conjugate of the control copy's NOT by a body automorphism fixing the corner axis
("type covariance").  The design module EqvSeams (branch dev-equivalence/kinf-seams) states the reduction
(two-NOT data + type covariance => a one-NOT native gate, hence d in {1, 3}); this probe checks it on instances and
checks that the surviving countermodels are excluded by the weaker premise.

REPRESENTATION.  W d = (d+1) x (d+1) real tables w[c][t] (c control index, t target index; index 0 = unit u,
index d = the corner axis z).  A NOT or a local map is given by its homogenized (d+1) x (d+1) matrix H (H[0][0] = 1).
  actT H w = w H^T   (target index),   actC H w = H w   (control index)        [CompositeDimension.lean:198-203]
  prodState x y = hom(x) hom(y)^T,  corners hom(+z) = u + z, hom(-z) = u - z.
Relations (two-NOT reading, NC on the control side, NT on the target):
  frame:  G(k_a (x) k_b) = k_a (x) k_(a+b)
  relT :  actT NT (G (actT NT w)) = G w            for every w (checked on the full basis of W d)
  relC :  actC NC (G (actC NC w)) = actT NT (G w)  for every w
The d = 3 gate `cnot` is PARSED from CompositeDimension.lean (sgn, pc, pt; cnotFun w mu nu = sgn * w (pc) (pt)).
The J/K maps are rebuilt here from NB-1's construction (data as in research/archive/threads/B/part2_three_copy.py:60-70
and blib.jk_gate); every relation check below is this script's own code.

CHECKS.
  C1  kernel cnot with nflip: frame, relT, relC (one NOT)                          -- positive control of the code
  C2  swapped gate G2 = actT s . cnot . actT s (s = swap of axes 0,1; s z = z): frame, relT(NT), relC(nflip, NT),
      with NT = s nflip s
  C3  NT != nflip; both involutive isometries flipping z with the same split (1,1)
  C4  G2 is not a one-NOT gate: relT(nflip) fails for G2, relC(NT, NT) fails for G2
  C5  the reduction: actT s . G2 . actT s == cnot exactly, and it meets the one-NOT relations with nflip
  J1  d = 5, 7 J/K maps: frame, relT(NB), relC(NA, NB) hold                         -- countermodel clauses re-derived
  J2  d = 5, 7: split(NA) != split(NB) (exact ranks of H -/+ I); hence NA, NB are not similar, so no conjugator of any
      kind exists and type covariance FAILS for these data
  J3  d = 5, 7 one-NOT countercontrol: relC(NB, NB) fails and relT(NA) fails for the J/K map
  S1  transfer countercontrol: a shear g fixing z (g = diag(2,1,1) on R^3) does not preserve the ball, and
      actT g carries the product state prodState(0, e0) (in maxCone) to a table on which the product effect
      (unit) (x) (sharp effect along -e0) takes the value -1/2 < 0  -- the ball-preservation hypothesis of the
      transfer lemma `actT_mem_maxCone` is load-bearing
DECISION RULE (fixed before the first run).  VERDICT TYPE-COVARIANCE-CONSISTENT is printed iff every check
C1-C5, J1-J3, S1 passes.  Otherwise the verdict line is "VERDICT NOT RENDERED" followed by the failing checks.
The verdict says only: on these instances the reduction behaves as the [D] theorem states, and the two known two-NOT
countermodels violate type covariance.  Positivity of the J/K maps is NOT re-checked here (thread B / NB-1, [A]); the
swapped gate's positivity is the [D] theorem's (`actT_mem_maxCone`), not a check of this script.
"""
import re
import sys
from fractions import Fraction as Fr

KERNEL = '../../../verification/lean-mathlib/OIBridge/CompositeDimension.lean'
RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print('%s %s%s' % ('PASS' if ok else 'FAIL', name, (' -- ' + detail) if detail else ''))


# ------------------------------------------------------------------ linear algebra on tables
def zeros(n, m=None):
    m = n if m is None else m
    return [[Fr(0)] * m for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = Fr(1)
    return M


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), Fr(0)) for j in range(len(B[0]))] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def diag(v):
    M = zeros(len(v))
    for i, x in enumerate(v):
        M[i][i] = Fr(x)
    return M


def rank(M):
    M = [list(r) for r in M]
    r = 0
    rows, cols = len(M), len(M[0])
    for c in range(cols):
        p = next((i for i in range(r, rows) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(rows):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == rows:
            break
    return r


def split(H):
    n = len(H)
    I = eye(n)
    plus = n - rank([[H[i][j] - I[i][j] for j in range(n)] for i in range(n)])
    minus = n - rank([[H[i][j] + I[i][j] for j in range(n)] for i in range(n)])
    return (plus - 1, minus - 1)  # transverse split (p, q): u is +1, z is -1


def actT(H, w):
    return mm(w, tr(H))


def actC(H, w):
    return mm(H, w)


def basis(n):
    for c in range(n):
        for t in range(n):
            w = zeros(n)
            w[c][t] = Fr(1)
            yield w


def hom_corner(n, a):
    v = [Fr(0)] * n
    v[0] = Fr(1)
    v[n - 1] = Fr(1) if a == 0 else Fr(-1)
    return v


def prod_state(x, y):
    return [[a * b for b in y] for a in x]


def frame_ok(G, n):
    for a in (0, 1):
        for b in (0, 1):
            if G(prod_state(hom_corner(n, a), hom_corner(n, b))) != prod_state(hom_corner(n, a), hom_corner(n, a ^ b)):
                return False
    return True


def relT_ok(G, n, NT):
    return all(actT(NT, G(actT(NT, w))) == G(w) for w in basis(n))


def relC_ok(G, n, NC, NT):
    return all(actC(NC, G(actC(NC, w))) == actT(NT, G(w)) for w in basis(n))


def is_invol_isometry_flipping_z(H):
    n = len(H)
    return mm(H, H) == eye(n) and mm(tr(H), H) == eye(n) and [H[i][n - 1] for i in range(n)] == \
        [Fr(0)] * (n - 1) + [Fr(-1)]


# ------------------------------------------------------------------ the kernel's d = 3 gate, parsed
def parse_table(src, name):
    m = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, src)
    entries = re.findall(r'(\d), (\d) => (\d)', m.group(1))
    T = {(int(a), int(b)): int(c) for a, b, c in entries}
    assert len(T) == 16
    return T


def parse_sgn(src):
    m = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1', src)
    neg = {(int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4)))}
    return {(a, b): (Fr(-1) if (a, b) in neg else Fr(1)) for a in range(4) for b in range(4)}


src = open(KERNEL, encoding='utf-8').read()
PC, PT, SGN = parse_table(src, 'pc'), parse_table(src, 'pt'), parse_sgn(src)
nflip_m = re.search(r'def nflip : \(Fin 3 → ℝ\) →ₗ\[ℝ\] \(Fin 3 → ℝ\) where\n  toFun x := fun i => \(!\[(.*?)\] : Fin 3 → ℝ\) i \* x i', src)
NFLIP_DIAG = [int(s.strip()) for s in nflip_m.group(1).split(',')]
z3_m = re.search(r'def z3 : Fin 3 → ℝ := !\[(.*?)\]', src)
Z3 = [int(s.strip()) for s in z3_m.group(1).split(',')]
print('parsed: pc, pt, sgn tables (16 entries each); nflip diagonal %s; z3 = %s' % (NFLIP_DIAG, Z3))
assert Z3 == [0, 0, 1], 'the probe assumes the corner axis is the last coordinate'


def cnot(w):
    return [[SGN[(m, v)] * w[PC[(m, v)]][PT[(m, v)]] for v in range(4)] for m in range(4)]


NFLIP = diag([1] + NFLIP_DIAG)
S = [[Fr(1), 0, 0, 0], [0, 0, Fr(1), 0], [0, Fr(1), 0, 0], [0, 0, 0, Fr(1)]]  # homogenized swap01
S = [[Fr(x) for x in r] for r in S]
NT3 = mm(mm(S, NFLIP), S)

print('== d = 3 (kernel cnot, nflip, swapped target)')
check('C1 kernel cnot meets frame, relT(nflip), relC(nflip, nflip)',
      frame_ok(cnot, 4) and relT_ok(cnot, 4, NFLIP) and relC_ok(cnot, 4, NFLIP, NFLIP))


def G2(w):
    return actT(S, cnot(actT(S, w)))


check('C2 G2 = actT s . cnot . actT s meets frame, relT(NT), relC(nflip, NT) with NT = s nflip s',
      frame_ok(G2, 4) and relT_ok(G2, 4, NT3) and relC_ok(G2, 4, NFLIP, NT3),
      'NT diagonal %s' % [str(NT3[i][i]) for i in range(4)])
check('C3 NT != nflip; both involutive isometries flipping z; equal splits',
      NT3 != NFLIP and is_invol_isometry_flipping_z(NT3) and is_invol_isometry_flipping_z(NFLIP)
      and split(NT3) == split(NFLIP), 'splits %s %s' % (split(NFLIP), split(NT3)))
check('C4 G2 is not a one-NOT gate: relT(nflip) fails and relC(NT, NT) fails',
      (not relT_ok(G2, 4, NFLIP)) and (not relC_ok(G2, 4, NT3, NT3)))


def RED(w):
    return actT(S, G2(actT(S, w)))


check('C5 the reduction actT s . G2 . actT s equals cnot on the basis of W 3 and meets the one-NOT relations',
      all(RED(w) == cnot(w) for w in basis(4)) and frame_ok(RED, 4) and relT_ok(RED, 4, NFLIP)
      and relC_ok(RED, 4, NFLIP, NFLIP))


# ------------------------------------------------------------------ the J/K maps (NB-1's construction)
def jk_gate(d, NB, J, K):
    """NB-1's J/K map, M_0 = I (rebuilt from research/archive/threads/B/blib.py:249).  Returns the gate as a
    dict col -> {row: coef} on the flat index c*n + t."""
    n = d + 1
    plus = [i for i in range(1, d) if NB[i] == 1]
    assert len(plus) == 1
    x = plus[0]
    G = {}
    for j in range(n):
        if NB[j] == 1:
            G[0 * n + j] = {0 * n + j: Fr(1)}
            G[d * n + j] = {d * n + j: Fr(1)}
        else:
            G[0 * n + j] = {d * n + j: Fr(1)}
            G[d * n + j] = {0 * n + j: Fr(1)}
    for c in range(1, d):
        G[c * n + 0] = {c * n + x: Fr(1)}
        G[c * n + x] = {c * n + 0: Fr(1)}
        for j in range(1, n):
            if NB[j] == -1:
                s1, cc = J[c]
                s2, l = K[j]
                G[c * n + j] = {cc * n + l: Fr(s1 * s2)}
    return G


def as_fun(Gd, n):
    def f(w):
        out = zeros(n)
        for col, rows in Gd.items():
            c0, t0 = divmod(col, n)
            if w[c0][t0] != 0:
                for row, coef in rows.items():
                    r0, s0 = divmod(row, n)
                    out[r0][s0] += coef * w[c0][t0]
        return out
    return f


MODELS = {
    5: dict(NB=[1, 1, -1, -1, -1, -1], NA=[1, 1, -1, 1, -1, -1],
            J={1: (1, 2), 2: (-1, 1), 3: (1, 4), 4: (-1, 3)}, K={2: (1, 5), 5: (-1, 2), 3: (1, 4), 4: (-1, 3)}),
    7: dict(NB=[1, 1, -1, -1, -1, -1, -1, -1], NA=[1, 1, 1, 1, -1, -1, -1, -1],
            J={1: (1, 4), 4: (-1, 1), 2: (1, 5), 5: (-1, 2), 3: (1, 6), 6: (-1, 3)},
            K={2: (1, 3), 3: (-1, 2), 4: (1, 5), 5: (-1, 4), 6: (1, 7), 7: (-1, 6)}),
}
for d, M in MODELS.items():
    n = d + 1
    print('== d = %d J/K map' % d)
    G = as_fun(jk_gate(d, M['NB'], M['J'], M['K']), n)
    NA, NB = diag(M['NA']), diag(M['NB'])
    check('J1 d=%d frame, relT(NB), relC(NA, NB) hold' % d,
          frame_ok(G, n) and relT_ok(G, n, NB) and relC_ok(G, n, NA, NB))
    sa, sb = split(NA), split(NB)
    check('J2 d=%d split(NA) = %s != split(NB) = %s: NA, NB not similar, no conjugator; type covariance fails' %
          (d, sa, sb), sa != sb and is_invol_isometry_flipping_z(NA) and is_invol_isometry_flipping_z(NB))
    check('J3 d=%d one-NOT countercontrol: relC(NB, NB) fails and relT(NA) fails' % d,
          (not relC_ok(G, n, NB, NB)) and (not relT_ok(G, n, NA)))

# ------------------------------------------------------------------ transfer countercontrol
print('== transfer countercontrol (shear)')
g = diag([1, 2, 1, 1])  # homogenized shear: x0 -> 2 x0, fixes x1 and z
x0 = [Fr(1), Fr(0), Fr(0), Fr(0)]          # hom(0)
e0 = [Fr(1), Fr(1), Fr(0), Fr(0)]          # hom(e0), e0 on the unit sphere
w = prod_state(x0, e0)
w2 = actT(g, w)
unit = [Fr(1), Fr(0), Fr(0), Fr(0)]        # ehom of the unit effect
sharp_neg_e0 = [Fr(1, 2), Fr(-1, 2), Fr(0), Fr(0)]   # ehom of (1 - x0)/2
val = sum(unit[m] * w2[m][v] * sharp_neg_e0[v] for m in range(4) for v in range(4))
val0 = sum(unit[m] * w[m][v] * sharp_neg_e0[v] for m in range(4) for v in range(4))
check('S1 shear fixing z: value on prodState(0, e0) is %s >= 0, on its actT g image %s < 0' % (val0, val),
      val0 >= 0 and val == Fr(-1, 2) and g[3][3] == 1)

fails = [nm for nm, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(fails)))
if not fails:
    print('VERDICT TYPE-COVARIANCE-CONSISTENT')
else:
    print('VERDICT NOT RENDERED: ' + '; '.join(fails))
sys.exit(0)
