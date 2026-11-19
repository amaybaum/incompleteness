#!/usr/bin/env python3
"""p10_r5rev_checks.py -- r5 reviewer probe (QPHEN Phase 1, #1210).

Exact checks of paper claims on generic mathematical objects only ("Allowed: generic
checks", #1210 c.6739250392). No OI mechanism is built or run. Imports no earlier probe.

Sections
  (1) Q4-P19 / Q4-D3: affine-symplectic maps of F_2^4 that are the identity on c = 0
      and change a meter slot on c = 1.  Enumeration is written independently of p8/p9:
      symplectic group built by closure from transvections, then cross-checked by a
      direct Gram-matrix test over all of GL(4, F_2) (enumerated column by column).
  (2) Q4-P19's three-line argument as stated, and its extension to three modes (F_2^6).
  (3) Couplings of R4.9 / Q4-P15: copy, reciprocal, occupation-conditional kick.
  (4) B2 / Q3-P11: alpha = 9/50 from a uniform law with non-affine functionals.
  (5) LG exact configuration of A4.1(c) / Q4-P4 (sympy, Schroedinger picture, Lueders).
  (6) Finding 5(b) companion: a non-affine, centre-free, neighbour-symmetric rule over
      Z_5 equivariant under every global additive automorphism x -> lam*x + c.
  (7) Q4-P19 in the strong sense used by R4.9 / T2 (meter write depends on c => the carrier
      conjugate x changes on some silent-branch state), and the weak sense's meter-only case.
Bit/coordinate order on F_2^4: (c, x, m, mp); symplectic pairs (c, x), (m, mp).
"""
import itertools
import sys
from fractions import Fraction

RESULTS = []


def check(name, cond):
    RESULTS.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)


# ---------------------------------------------------------------- F_2 linear algebra
def matvec(M, v):
    n = len(M)
    return tuple(sum(M[i][j] & v[j] for j in range(n)) & 1 for i in range(n))


def matmul(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] & B[k][j] for k in range(n)) & 1 for j in range(n)) for i in range(n))


def identity(n):
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def omega(u, v, pairs):
    s = 0
    for (a, b) in pairs:
        s ^= (u[a] & v[b]) ^ (u[b] & v[a])
    return s


def unit(n, i):
    return tuple(int(k == i) for k in range(n))


def is_symplectic(M, pairs):
    n = len(M)
    cols = [tuple(M[i][j] for i in range(n)) for j in range(n)]
    for i in range(n):
        for j in range(n):
            if omega(cols[i], cols[j], pairs) != omega(unit(n, i), unit(n, j), pairs):
                return False
    return True


def rank_f2(vectors):
    rows = [int("".join(map(str, v)), 2) for v in vectors]
    r = 0
    width = len(vectors[0]) if vectors else 0
    for bit in reversed(range(width)):
        piv = None
        for k in range(r, len(rows)):
            if (rows[k] >> bit) & 1:
                piv = k
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for k in range(len(rows)):
            if k != r and (rows[k] >> bit) & 1:
                rows[k] ^= rows[r]
        r += 1
    return r


N = 4
C, X, MM, MP = 0, 1, 2, 3
PAIRS = [(C, X), (MM, MP)]
VECS = list(itertools.product((0, 1), repeat=N))

# GL(4, F_2) column by column (independent columns)
GL = []


def build(cols):
    if len(cols) == N:
        GL.append(tuple(tuple(cols[j][i] for j in range(N)) for i in range(N)))
        return
    for v in VECS:
        if rank_f2(cols + [v]) == len(cols) + 1:
            build(cols + [v])


build([])
check("(1a) |GL(4,F_2)| = 20160 (column-by-column enumeration)", len(GL) == 20160)
SP_gram = [M for M in GL if is_symplectic(M, PAIRS)]
check("(1b) |Sp(4,F_2)| = 720 by Gram-matrix test", len(SP_gram) == 720)


# independent construction: closure of symplectic transvections T_v(y) = y + omega(y, v) v
def transvection(v):
    cols = []
    for j in range(N):
        e = unit(N, j)
        w = omega(e, v, PAIRS)
        cols.append(tuple(e[i] ^ (w & v[i]) for i in range(N)))
    return tuple(tuple(cols[j][i] for j in range(N)) for i in range(N))


gens = [transvection(v) for v in VECS if any(v)]
group = {identity(N)}
frontier = [identity(N)]
while frontier:
    nxt = []
    for g in frontier:
        for t in gens:
            h = matmul(t, g)
            if h not in group:
                group.add(h)
                nxt.append(h)
    frontier = nxt
check("(1c) transvection closure has 720 elements and equals the Gram-test set", len(group) == 720 and group == set(SP_gram))


def affine_apply(M, b, y):
    return tuple(a ^ c for a, c in zip(matvec(M, y), b))


def identity_on_silent(M, b):
    return all(affine_apply(M, b, y) == y for y in VECS if y[C] == 0)


def records(M, b):
    for y in VECS:
        if y[C] == 1:
            z = affine_apply(M, b, y)
            if z[MM] != y[MM] or z[MP] != y[MP]:
                return True
    return False


sym_id = [(M, b) for M in SP_gram for b in VECS if identity_on_silent(M, b)]
sym_bad = [(M, b) for (M, b) in sym_id if records(M, b)]
aff_id = [(M, b) for M in GL for b in VECS if identity_on_silent(M, b)]
aff_bad = [(M, b) for (M, b) in aff_id if records(M, b)]
check("(1d) affine-symplectic maps: 720 x 16 = 11520 examined", len(SP_gram) * 16 == 11520)
check("(1e) affine-symplectic, identity on c=0, recording on c=1: 0 of 11520", len(sym_bad) == 0)
check("(1f) affine-symplectic, identity on c=0: exactly 2 (identity; x <- x + c)", len(sym_id) == 2)
kick = tuple(tuple(int(i == j) ^ int(i == X and j == C) for j in range(N)) for i in range(N))
check("(1g) the non-identity one is the occupation-conditional kick x <- x + c", {M for (M, b) in sym_id} == {identity(N), kick})
check("(1h) affine bijections (not necessarily symplectic), identity on c=0, recording: 6 of 322560", len(aff_bad) == 6 and len(GL) * 16 == 322560)
check("(1i) affine bijections identity on c=0: 8, all with b = 0", len(aff_id) == 8 and all(not any(b) for (_, b) in aff_id))

# (2) the three-line argument, by its own steps
ok = True
for (M, b) in aff_id:
    d = tuple(M[i][C] ^ int(i == C) for i in range(N))
    if any(M[i][j] != int(i == j) for i in range(N) for j in range(N) if j != C):
        ok = False
    if d[C] != 0:
        ok = False
check("(2a) identity on c=0 => b = 0 and M = I + d e_c^T with d_c = 0 (8 maps)", ok)
ok = True
for d in VECS:
    if d[C]:
        continue
    M = tuple(tuple(int(i == j) ^ (d[i] if j == C else 0) for j in range(N)) for i in range(N))
    lhs = is_symplectic(M, PAIRS)
    rhs = all(omega(d, unit(N, j), PAIRS) == 0 for j in range(N) if j != C)
    span_x = d in [(0, 0, 0, 0), (0, 1, 0, 0)]
    if not (lhs == rhs == span_x):
        ok = False
check("(2b) for M = I + d e_c^T: symplectic <=> omega(d, e_j) = 0 (j != c) <=> d in span(e_x)", ok)
check("(2c) omega(d,e_x) = d_c, omega(d,e_m) = d_mp, omega(d,e_mp) = d_m for all d",
      all(omega(d, unit(N, X), PAIRS) == d[C] and omega(d, unit(N, MM), PAIRS) == d[MP]
          and omega(d, unit(N, MP), PAIRS) == d[MM] for d in VECS))
# extension (my own; not claimed by r5): three modes F_2^6, pairs (c,x),(m,mp),(e,ep)
N6 = 6
P6 = [(0, 1), (2, 3), (4, 5)]
ok = True
cnt = 0
for d in itertools.product((0, 1), repeat=N6):
    if d[0]:
        continue
    M = tuple(tuple(int(i == j) ^ (d[i] if j == 0 else 0) for j in range(N6)) for i in range(N6))
    if is_symplectic(M, P6):
        cnt += 1
        if any(d[k] for k in (2, 3, 4, 5)):
            ok = False
check("(2d) extension to F_2^6: symplectic maps identity on c=0 have d in span(e_x) (2 found)", ok and cnt == 2)

# (3) the couplings
copy = tuple(tuple(int(i == j) ^ int(i == MM and j == C) for j in range(N)) for i in range(N))
recip = tuple(tuple(int(i == j) ^ int(i == MM and j == C) ^ int(i == X and j == MP) for j in range(N)) for i in range(N))
check("(3a) copy m <- m + c: in GL, not symplectic, identity on c=0, records", copy in set(GL) and not is_symplectic(copy, PAIRS)
      and identity_on_silent(copy, (0,) * N) and records(copy, (0,) * N))
check("(3b) reciprocal (m <- m + c, x <- x + mp): symplectic, records, not identity on c=0",
      is_symplectic(recip, PAIRS) and records(recip, (0,) * N) and not identity_on_silent(recip, (0,) * N))


def cond_kick(y):
    c, x, m, mp = y
    return (c, x ^ (c & mp), m, mp)


aff_ok = False
for M in GL:
    for b in VECS:
        if all(affine_apply(M, b, y) == cond_kick(y) for y in VECS):
            aff_ok = True
check("(3c) occupation-conditional kick x <- x + c*mp is a bijection and not affine",
      len({cond_kick(y) for y in VECS}) == 16 and not aff_ok)

# (4) B2 / Q3-P11
cells = {(1, 1): 9, (1, 0): 151, (0, 1): 71, (0, 0): 25}
tot = sum(cells.values())
PA = Fraction(cells[(1, 1)] + cells[(1, 0)], tot)
PB = Fraction(cells[(1, 1)] + cells[(0, 1)], tot)
PAB = Fraction(cells[(1, 1)], tot)
check("(4a) cells sum to 256; P_A = 5/8, P_B = 5/16, P_AB = 9/256; alpha = 9/50",
      tot == 256 and PA == Fraction(5, 8) and PB == Fraction(5, 16) and PAB == Fraction(9, 256)
      and PAB / (PA * PB) == Fraction(9, 50))
# a uniform law on F_2^8 with functionals realizing these cells
pts = list(range(256))
fA = {p: int(p < 160) for p in pts}
fB = {p: int(p < 9 or 160 <= p < 231) for p in pts}
cnt = {(a, b): 0 for a in (0, 1) for b in (0, 1)}
for p in pts:
    cnt[(fA[p], fB[p])] += 1
check("(4b) uniform law on 256 points, functionals f_A, f_B with those cells", cnt == cells)
# an affine non-constant F_2 functional on F_2^8 has weight 128; 160 and 80 are not 128 => non-affine
check("(4c) f_A (weight 160) and f_B (weight 80) are not affine on F_2^8 (affine non-constant weight is 128)",
      sum(fA.values()) == 160 and sum(fB.values()) == 80)
# A3.1(a) re-check, exhaustive on F_2^3 cosets with affine functionals
alphas = set()
subspaces = set()
for gens3 in itertools.combinations(list(itertools.product((0, 1), repeat=3)), 3):
    span = {(0, 0, 0)}
    for g in gens3:
        span |= {tuple(a ^ b for a, b in zip(s, g)) for s in span}
    subspaces.add(frozenset(span))
for g1 in itertools.product((0, 1), repeat=3):
    span = frozenset({(0, 0, 0), g1})
    subspaces.add(span)
subspaces.add(frozenset({(0, 0, 0)}))
funcs = [(a, c0) for a in itertools.product((0, 1), repeat=3) for c0 in (0, 1)]
for V in subspaces:
    for s0 in itertools.product((0, 1), repeat=3):
        coset = {tuple(a ^ b for a, b in zip(s0, v)) for v in V}
        for (a, ca) in funcs:
            for (b, cb) in funcs:
                fa = [(sum(x & y for x, y in zip(a, s)) & 1) ^ ca for s in coset]
                fb = [(sum(x & y for x, y in zip(b, s)) & 1) ^ cb for s in coset]
                n = len(coset)
                pa = Fraction(sum(fa), n)
                pb = Fraction(sum(fb), n)
                pab = Fraction(sum(x & y for x, y in zip(fa, fb)), n)
                if pa and pb:
                    alphas.add(pab / (pa * pb))
check("(4d) A3.1(a) on F_2^3: every coset, every affine pair gives alpha in {0, 1, 2}", alphas == {0, 1, 2})

# (5) the LG configuration, exact, Schroedinger picture with Lueders projectors
try:
    import sympy as sp
except ImportError:
    sp = None
if sp is None:
    check("(5) sympy available", False)
else:
    b = sp.symbols("beta", real=True)
    I2 = sp.eye(2)
    Hd = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    Zc = sp.diag(1, -1)

    def kron(A, B):
        return sp.kronecker_product(A, B)

    # order carrier (x) mediator, basis |c m>
    def ket(cbit, mbit):
        v = sp.zeros(4, 1)
        v[2 * cbit + mbit] = 1
        return v

    CNOT_m_to_c = sp.zeros(4, 4)
    for cb in (0, 1):
        for mb in (0, 1):
            CNOT_m_to_c[2 * (cb ^ mb) + mb, 2 * cb + mb] = 1
    SWAP = sp.zeros(4, 4)
    for cb in (0, 1):
        for mb in (0, 1):
            SWAP[2 * mb + cb, 2 * cb + mb] = 1
    P = [kron(sp.diag(1, 0), I2), kron(sp.diag(0, 1), I2)]
    sgn = [1, -1]

    def rho_bloch(nx, nz):
        return (I2 + nx * sp.Matrix([[0, 1], [1, 0]]) + nz * Zc) / 2

    def correlators(G, rho0):
        def evolve(r, k):
            for _ in range(k):
                r = G * r * G.H
            return r

        def C(i, j):
            r = evolve(rho0, i - 1)
            tot = 0
            for a in range(2):
                ra = P[a] * r * P[a]
                ra = evolve(ra, j - i)
                for bb in range(2):
                    tot += sgn[a] * sgn[bb] * (P[bb] * ra).trace()
            return sp.simplify(sp.expand(tot))
        return C(1, 2), C(2, 3), C(1, 3)

    plus = rho_bloch(1, 0)
    med = rho_bloch(sp.sin(b), sp.cos(b))
    G1 = kron(I2, Hd) * CNOT_m_to_c
    r1 = correlators(G1, kron(plus, med))
    check("(5a) G1 = (I(x)H) CNOT_{m->c}, carrier |+>, mediator (sin b,0,cos b): (cos b, sin b, 0)",
          [sp.simplify(r1[0] - sp.cos(b)), sp.simplify(r1[1] - sp.sin(b)), sp.simplify(r1[2])] == [0, 0, 0])
    G2 = kron(I2, Hd) * SWAP * CNOT_m_to_c
    r2 = correlators(G2, kron(rho_bloch(sp.sin(b), sp.cos(b)), rho_bloch(0, 1)))
    K2 = sp.simplify(r2[0] + r2[1] - r2[2])
    check("(5b) G2 = (I(x)H) SWAP CNOT_{m->c}, mediator |0>, carrier (sin b,0,cos b): K3 = cos b + sin b",
          sp.simplify(K2 - sp.cos(b) - sp.sin(b)) == 0)
    K1 = r1[0] + r1[1] - r1[2]
    check("(5c) K3 = sqrt2 at b = pi/4 and 7/5 at (cos, sin) = (4/5, 3/5)",
          sp.simplify(K1.subs(b, sp.pi / 4) - sp.sqrt(2)) == 0
          and sp.nsimplify(K1.subs({sp.cos(b): sp.Rational(4, 5), sp.sin(b): sp.Rational(3, 5)})) == sp.Rational(7, 5))
    G1c = kron(Hd, I2) * CNOT_m_to_c
    r1c = correlators(G1c, kron(plus, med))
    G2c = kron(Hd, I2) * SWAP * CNOT_m_to_c
    r2c = correlators(G2c, kron(rho_bloch(sp.sin(b), sp.cos(b)), rho_bloch(0, 1)))
    check("(5d) H on the carrier instead: K3 = -cos b and K3 = 0",
          sp.simplify(r1c[0] + r1c[1] - r1c[2] + sp.cos(b)) == 0 and sp.simplify(r2c[0] + r2c[1] - r2c[2]) == 0)
    check("(5e) G1, G2 are unitary", sp.simplify(G1 * G1.H - sp.eye(4)) == sp.zeros(4, 4)
          and sp.simplify(G2 * G2.H - sp.eye(4)) == sp.zeros(4, 4))

# (6) finding 5(b) companion claim: global ("uniform") additive-automorphism equivariance
# does not force an affine rule in d >= 2.  Local rule over Z_5 reading the 6 neighbours
# of a site of the cubic lattice (no own-site term), fully symmetric in the 6 neighbours.
q = 5
inv6 = pow(6, -1, q)


def F_loc(nb):
    s = sum(nb) % q
    mean = (s * inv6) % q
    y = [(v - mean) % q for v in nb]
    p2 = sum(v * v for v in y) % q
    p3 = sum(v * v * v for v in y) % q
    return (2 * mean + p2 * p3) % q     # linear part 2*mean = (2/6) * sum


ALL6 = list(itertools.product(range(q), repeat=6))
Fv = {nb: F_loc(nb) for nb in ALL6}
equiv = all(Fv[tuple((lam * v + c) % q for v in nb)] == (lam * Fv[nb] + 2 * c) % q
            for lam in (1, 2, 3, 4) for c in range(q) for nb in ALL6)
check("(6a) F(lam*x + c) = lam*F(x) + 2c for every unit lam, every c (exhaustive over Z_5^6)", equiv)
# second-order step x' = F(x) - x_prev then commutes with x -> lam*x + c on both slices
check("(6b) hence the second-order step commutes with every global additive automorphism",
      all(((lam * Fv[nb] + 2 * c) - (lam * xp + c)) % q == (lam * ((Fv[nb] - xp) % q) + c) % q
          for lam in (1, 2, 3, 4) for c in range(q) for nb in ALL6 for xp in range(q)))
sym = all(Fv[nb] == Fv[nb[1:] + nb[:1]] and Fv[nb] == Fv[(nb[1], nb[0]) + nb[2:]] for nb in ALL6)
check("(6c) F is invariant under all permutations of the 6 neighbours (cubic group included)", sym)
# non-affine: an affine map g satisfies g(u+v) - g(u) - g(v) + g(0) = 0
zero = (0,) * 6
nonaff = any((Fv[tuple((a + b2) % q for a, b2 in zip(u, v))] - Fv[u] - Fv[v] + Fv[zero]) % q
             for u in ALL6[::97] for v in ALL6[::131])
check("(6d) F is not affine on Z_5^6 (a witness pair exists)", nonaff)
# first differences depend on base point (so the Substratum:272 lemma's hypothesis fails, as it must)
e0 = (1, 0, 0, 0, 0, 0)
diffs = {(Fv[tuple((a + b2) % q for a, b2 in zip(u, e0))] - Fv[u]) % q for u in ALL6}
check("(6e) the first difference in one neighbour coordinate is base-point dependent", len(diffs) > 1)

# (7) stronger reading used by R4.9, T2 and A4.4 ("acts on its silent branch" read as K_null != id on
# the system).  "Records" in the strong sense: the meter change depends on c.  "Disturbs the system on
# the silent branch": some c = 0 state has (c, x) changed.  Location preserved: c' = c.
def meter_delta(M, b, y):
    z = affine_apply(M, b, y)
    return (z[MM] ^ y[MM], z[MP] ^ y[MP])


def records_strong(M, b):
    for y in VECS:
        if y[C] == 0:
            y1 = tuple(v ^ int(i == C) for i, v in enumerate(y))
            if meter_delta(M, b, y) != meter_delta(M, b, y1):
                return True
    return False


def keeps_c(M, b):
    return all(affine_apply(M, b, y)[C] == y[C] for y in VECS)


def disturbs_system_on_silent(M, b):
    return any(affine_apply(M, b, y)[X] != y[X] for y in VECS if y[C] == 0)


strong = [(M, b) for M in SP_gram for b in VECS if keeps_c(M, b) and records_strong(M, b)]
bad7 = [(M, b) for (M, b) in strong if not disturbs_system_on_silent(M, b)]
weak_only = [(M, b) for M in SP_gram for b in VECS if keeps_c(M, b) and records(M, b)
             and not records_strong(M, b) and not disturbs_system_on_silent(M, b)]
print("     (7) location-preserving affine-symplectic maps recording in the strong sense:", len(strong))
check("(7a) every location-preserving affine-symplectic map whose meter change depends on c changes x on some c=0 state",
      len(strong) > 0 and len(bad7) == 0)
check("(7b) under Q4-P19's weak 'records' (some meter slot changed on c=1), maps exist that act on the silent branch "
      "only through the meter (e.g. the translation m <- m + 1)", len(weak_only) > 0)

print()
npass = sum(ok for _, ok in RESULTS)
print(f"{npass} of {len(RESULTS)} checks pass")
sys.exit(0 if npass == len(RESULTS) else 1)
