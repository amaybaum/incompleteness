"""Thread G3, probe P2 -- composite side in DIM-1's own coordinates: what the gate relations force, what
positivity adds, and the gate-induced complex structure.

Read-only research against base 06b6f94e479bc19a28979c72316823cbdd0fb62b. Exact arithmetic only (Fraction).
The d = 3 gate `cnot` (tables pc, pt, sgn), the NOT `nflip`, the d = 1 gate `cnot1` and `neg1` are parsed or
checked literally from CompositeDimension.lean (path given as argv[1]); `actT`, `actC`, `homMap`, `prodState`,
`corner` and the NativeGate fields frame/relT/relC are transcribed from :112, :161, :198, :201, :207, :218.

DECISION RULES (written before the first run):
  K  Kernel controls: cnot satisfies frame, relT, relC with nflip; cnot1 with neg1; both are involutions.
     A failure voids every row below.
  S  Sector rule (the kernel's parity mechanism made explicit): for cnot, G preserves the target-odd sector and
     swaps its control-even and control-odd parts bijectively (4 <-> 4); for cnot1 (1 <-> 1).
  J  Gate complex structure: (actC N o G)^2 = actT N o G^2 as maps of W d (from relC); on the target-odd sector
     J := actC N o G has J^2 = -1 for cnot AND for the classical cnot1.  If cnot1 has it, "a complex structure
     induced by the gate" is not a fingerprint of C.
  F  Q-FWD covariance: for the rational rotation g about z with g e1 = (3/5, 4/5, 0), the conjugate
     G' = (actC g actT g) cnot (actC g actT g)^-1 satisfies frame, relT, relC with N' = g nflip g^T (a pi-rotation
     about an equatorial axis other than e1).  Positivity of G' is covariance [W]; a rational sample is printed.
  L  Linear-solve cross-check at d = 3: the solution space of {relT, relC} for N' (non-diagonal) and for the two
     antiunitary NOTs diag(1,1,-1), -I (diagonal), computed by exact elimination on 256 unknowns.  Every solution
     maps the target-odd sector's control-even part into its control-odd part and back (checked on a basis), so
     its rank is at most 16 - |p*m - m*m|; generic element rank printed.  Rule: an invertible solution exists
     iff the split is balanced.
  A  Algebraic-gate census, diagonal NOTs, d in {1,2,3,5,7,9} and every tangent split: for diagonal N the
     relations are entrywise (shown at d = 3 by L), so the solution space is the span of allowed entries and the
     maximal rank is the term rank (maximum matching).  Rule: full term rank <=> balanced.  For each balanced
     split an explicit G_J (identity on target-even; on target-odd a permutation of the control index swapping
     V+ <-> V-, unit <-> z) is built and checked for frame, relT, relC, invertibility.
  P  Positivity: the witness  x = e1 (control tangent +1 axis), y = z, a = (1, -u) with
     u = (3/5) J(e1) + (4/5) z, b = (1, z)  gives pairVal(a, b, G_J(prodState x y)) = 1 - 7/5 < 0 for every
     balanced G_J (d = 3, 5, 7, 9); the kernel cnot is nonnegative on the same exact sample grid (control of the
     evaluator only; cnot's positivity is a kernel theorem).

Run:  python3 -I g3_p2_gate_algebra.py <path>/CompositeDimension.lean
"""
import re
import sys
from fractions import Fraction as Fr
import itertools

SRC = open(sys.argv[1], encoding="utf-8").read()
CHECKS = []


def check(name, cond, detail=""):
    cond = bool(cond)
    CHECKS.append((name, cond))
    print(("PASS " if cond else "FAIL ") + name + (("  [" + detail + "]") if detail else ""))


# ------------------------------------------------------------------ parse the kernel d = 3 gate and NOT
def parse_table(name):
    m = re.search(r"def %s : Fin 4 → Fin 4 → Fin 4\n((?:\s*\|.*\n)+)" % name, SRC)
    tab = {}
    for a, b, c in re.findall(r"(\d), (\d) => (\d)", m.group(1)):
        tab[(int(a), int(b))] = int(c)
    assert len(tab) == 16
    return tab


PC, PT = parse_table("pc"), parse_table("pt")
msg = re.search(r"def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1", SRC)
NEG = {(int(msg.group(1)), int(msg.group(2))), (int(msg.group(3)), int(msg.group(4)))}
mfl = re.search(r"def nflip[^\n]*\n\s*toFun x := fun i => \(!\[(.*?)\] : Fin 3 → ℝ\) i \* x i", SRC)
NFLIP = [Fr(int(t)) for t in mfl.group(1).split(",")]
assert re.search(r"def cnot1Fun \(ω : W 1\) : W 1 := fun μ ν => ω \(μ \+ ν\) ν", SRC)
assert re.search(r"def neg1 : \(Fin 1 → ℝ\) →ₗ\[ℝ\] \(Fin 1 → ℝ\) := -LinearMap.id", SRC)
assert re.search(r"def z3 : Fin 3 → ℝ := !\[0, 0, 1\]", SRC)
print("parsed: sgn = -1 at %s; nflip = diag%s" % (sorted(NEG), [str(t) for t in NFLIP]))


# ------------------------------------------------------------------ linear algebra helpers (Fraction)
def zeros(r, c):
    return [[Fr(0)] * c for _ in range(r)]


def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = zeros(n, p)
    for i in range(n):
        Ai = A[i]
        for k in range(m):
            a = Ai[k]
            if a:
                Bk = B[k]
                row = out[i]
                for j in range(p):
                    if Bk[j]:
                        row[j] += a * Bk[j]
    return out


def mv(A, v):
    return [sum(a * b for a, b in zip(row, v) if a and b) for row in A]


def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def neg(A):
    return [[-x for x in r] for r in A]


def tr(A):
    return [list(r) for r in zip(*A)]


def rank(A):
    M = [list(r) for r in A]
    rows, cols = len(M), len(M[0])
    rk = 0
    for c in range(cols):
        piv = next((r for r in range(rk, rows) if M[r][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        pv = M[rk][c]
        M[rk] = [t / pv for t in M[rk]]
        for r in range(rows):
            if r != rk and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[rk])]
        rk += 1
    return rk


def nullspace(A, ncols):
    """exact nullspace; rows given as dense lists, eliminated sparsely (dict rows, reduced row echelon)."""
    piv = {}                                   # pivot column -> reduced row (dict)
    for dense in A:
        row = {i: v for i, v in enumerate(dense) if v != 0}
        for c in sorted(set(row) & set(piv)):
            if c in row:
                f = row[c]
                for k, v in piv[c].items():
                    row[k] = row.get(k, 0) - f * v
                    if row[k] == 0:
                        del row[k]
        if not row:
            continue
        c0 = min(row)
        pv = row[c0]
        row = {k: v / pv for k, v in row.items()}
        for c, r in piv.items():
            if c0 in r:
                f = r[c0]
                for k, v in row.items():
                    r[k] = r.get(k, 0) - f * v
                    if r[k] == 0:
                        del r[k]
        piv[c0] = row
    # reduce fully (eliminate later pivots from earlier rows)
    changed = True
    while changed:
        changed = False
        for c, r in piv.items():
            for c2 in [k for k in r if k != c and k in piv]:
                f = r[c2]
                for k, v in piv[c2].items():
                    r[k] = r.get(k, 0) - f * v
                    if r[k] == 0:
                        del r[k]
                changed = True
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * ncols
        v[f] = Fr(1)
        for c, r in piv.items():
            if f in r:
                v[c] = -r[f]
        basis.append(v)
    return basis


# ------------------------------------------------------------------ DIM-1 objects
def hommap(N):
    d = len(N)
    H = zeros(d + 1, d + 1)
    H[0][0] = Fr(1)
    for i in range(d):
        for j in range(d):
            H[i + 1][j + 1] = Fr(N[i][j])
    return H


def actT(N):
    H = hommap(N)
    return kron(eye(len(H)), H)


def actC(N):
    H = hommap(N)
    return kron(H, eye(len(H)))


def hom(x):
    return [Fr(1)] + [Fr(t) for t in x]


def prodstate(x, y):
    return [a * b for a in hom(x) for b in hom(y)]


def frame_ok(G, z):
    c = [z, [-t for t in z]]
    return all(mv(G, prodstate(c[a], c[b])) == prodstate(c[a], c[(a + b) % 2]) for a in (0, 1) for b in (0, 1))


def rels_ok(G, N):
    T, C = actT(N), actC(N)
    rt = mm(mm(T, G), T) == G
    rc = mm(mm(C, G), C) == mm(T, G)
    return rt, rc


def diagm(v):
    return [[Fr(v[i]) if i == j else Fr(0) for j in range(len(v))] for i in range(len(v))]


# kernel cnot as a 16x16 matrix: (cnot w)[mu,nu] = sgn(mu,nu) * w[pc(mu,nu), pt(mu,nu)]
CNOT = zeros(16, 16)
for mu in range(4):
    for nu in range(4):
        s = Fr(-1) if (mu, nu) in NEG else Fr(1)
        CNOT[mu * 4 + nu][PC[(mu, nu)] * 4 + PT[(mu, nu)]] = s
NF = diagm(NFLIP)
Z3 = [0, 0, 1]
CNOT1 = zeros(4, 4)
for mu in range(2):
    for nu in range(2):
        CNOT1[mu * 2 + nu][((mu + nu) % 2) * 2 + nu] = Fr(1)
NEG1 = [[Fr(-1)]]
Z1 = [1]

# K
rt, rc = rels_ok(CNOT, NF)
check("K cnot: frame, relT, relC with nflip; involution", frame_ok(CNOT, Z3) and rt and rc and mm(CNOT, CNOT) == eye(16))
rt1, rc1 = rels_ok(CNOT1, NEG1)
check("K cnot1: frame, relT, relC with neg1; involution", frame_ok(CNOT1, Z1) and rt1 and rc1 and mm(CNOT1, CNOT1) == eye(4))


# ------------------------------------------------------------------ S: sectors
def sector_basis(signs):
    """signs: homogenized diagonal signs s_0..s_d. returns index lists for (s_mu, s_nu) sectors."""
    n = len(signs)
    sec = {}
    for mu in range(n):
        for nu in range(n):
            sec.setdefault((signs[mu], signs[nu]), []).append(mu * n + nu)
    return sec


def sector_map(G, signs):
    n = len(signs)
    sec = sector_basis(signs)
    which = {}
    for key, idx in sec.items():
        for r in idx:
            which[r] = key
    images = {}
    for key, idx in sec.items():
        tgt = set()
        for c in idx:
            for r in range(n * n):
                if G[r][c] != 0:
                    tgt.add(which[r])
        images[key] = tgt
    return sec, images


for nm, G, signs in [("cnot", CNOT, [1] + NFLIP), ("cnot1", CNOT1, [1, -1])]:
    sec, images = sector_map(G, [int(s) for s in signs])
    pm, mmn = sec[(1, -1)], sec[(-1, -1)]
    blk = [[G[r][c] for c in pm] for r in mmn]
    blk2 = [[G[r][c] for c in mmn] for r in pm]
    ok = images[(1, -1)] == {(-1, -1)} and images[(-1, -1)] == {(1, -1)} and \
        images[(1, 1)] == {(1, 1)} and images[(-1, 1)] == {(-1, 1)} and \
        len(pm) == len(mmn) == rank(blk) == rank(blk2)
    check("S %s: target-odd sector, control-even (%d) <-> control-odd (%d) swapped bijectively; target-even "
          "sectors preserved" % (nm, len(pm), len(mmn)), ok)

# ------------------------------------------------------------------ J: gate complex structure
for nm, G, N in [("cnot", CNOT, NF), ("cnot1", CNOT1, NEG1)]:
    T, C = actT(N), actC(N)
    J = mm(C, G)
    ident = mm(J, J) == mm(T, mm(G, G))
    n = len(N) + 1
    signs = [1] + [int(N[i][i]) for i in range(len(N))]
    odd = sector_basis(signs)[(1, -1)] + sector_basis(signs)[(-1, -1)]
    Jodd = [[J[r][c] for c in odd] for r in odd]
    closed = all(J[r][c] == 0 for c in odd for r in range(n * n) if r not in odd)
    J2 = mm(Jodd, Jodd)
    check("J %s: (actC N o G)^2 = actT N o G^2 on W; J preserves the target-odd sector (dim %d) and J^2 = -1 there"
          % (nm, len(odd)), ident and closed and J2 == neg(eye(len(odd))))

# ------------------------------------------------------------------ F: Q-FWD covariance at d = 3
g = [[Fr(3, 5), Fr(-4, 5), Fr(0)], [Fr(4, 5), Fr(3, 5), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
gT = tr(g)
assert mm(g, gT) == eye(3)
Np = mm(mm(g, NF), gT)
A = mm(actC(g), actT(g))
Ainv = mm(actC(gT), actT(gT))
assert mm(A, Ainv) == eye(16)
Gp = mm(mm(A, CNOT), Ainv)
rtp, rcp = rels_ok(Gp, Np)
axis = [r[0] for r in g]
check("F N' = g nflip g^T is a pi-rotation about (3/5,4/5,0) flipping z; G' meets frame, relT, relC with N'",
      mv(Np, axis) == axis and mv(Np, Z3) == [-t for t in Z3] and mm(Np, Np) == eye(3) and
      frame_ok(Gp, Z3) and rtp and rcp, "N' = %s" % [[str(t) for t in r] for r in Np])

# rational sample points on the sphere and Lorentz effect rays
SPH3 = []
for v in itertools.permutations([Fr(3, 5), Fr(4, 5), Fr(0)]):
    for s in itertools.product([1, -1], repeat=3):
        w = [a * b for a, b in zip(v, s)]
        if w not in SPH3:
            SPH3.append(w)
for i in range(3):
    for s in (1, -1):
        w = [Fr(0)] * 3
        w[i] = Fr(s)
        SPH3.append(w)


def pairval(a, b, w):
    n = len(a)
    return sum(a[i] * w[i * n + j] * b[j] for i in range(n) for j in range(n) if a[i] and b[j])


def min_sample(G, pts):
    n = len(pts[0]) + 1
    effs = [[Fr(1)] + [-t for t in u] for u in pts]
    best = None
    for x in pts:
        for y in pts + [[Fr(0)] * len(pts[0])]:
            w = mv(G, prodstate(x, y))
            for a in effs:
                r = [sum(a[i] * w[i * n + j] for i in range(n) if a[i]) for j in range(n)]
                for b in effs:
                    val = sum(r[j] * b[j] for j in range(n))
                    if best is None or val < best:
                        best = val
    return best


mc = min_sample(CNOT, SPH3)
mp = min_sample(Gp, SPH3)
check("F sample: min pairVal over %d^3 rational pure products x effect rays is >= 0 for cnot (%s) and G' (%s)"
      % (len(SPH3), mc, mp), mc >= 0 and mp >= 0)

# ------------------------------------------------------------------ L: linear solve at d = 3
def relation_system(N):
    T, C = actT(N), actC(N)
    n2 = len(T)
    # unknown G[r][c] -> index r*n2 + c.  equations: (T G T - G)[r][c] = 0, (C G C - T G)[r][c] = 0
    rows = []
    for r in range(n2):
        for c in range(n2):
            e1 = {}
            for i in range(n2):
                if T[r][i]:
                    for j in range(n2):
                        if T[j][c]:
                            e1[i * n2 + j] = e1.get(i * n2 + j, 0) + T[r][i] * T[j][c]
            e1[r * n2 + c] = e1.get(r * n2 + c, 0) - 1
            e2 = {}
            for i in range(n2):
                if C[r][i]:
                    for j in range(n2):
                        if C[j][c]:
                            e2[i * n2 + j] = e2.get(i * n2 + j, 0) + C[r][i] * C[j][c]
            for i in range(n2):
                if T[r][i]:
                    e2[i * n2 + c] = e2.get(i * n2 + c, 0) - T[r][i]
            for e in (e1, e2):
                row = [Fr(0)] * (n2 * n2)
                for k, v in e.items():
                    row[k] = Fr(v)
                if any(row):
                    rows.append(row)
    return rows


def eig_proj(N, s):
    H = hommap(N)
    n = len(H)
    return [[(Fr(int(i == j)) + s * H[i][j]) / 2 for j in range(n)] for i in range(n)]


L_CASES = [("pi-rotation N' (unitary, non-diagonal)", Np),
           ("diag(1,1,-1) (antiunitary reflection)", diagm([1, 1, -1])),
           ("-I (antiunitary universal NOT)", diagm([-1, -1, -1])),
           ("nflip (kernel)", NF)]
for nm, N in L_CASES:
    sysrows = relation_system(N)
    basis = nullspace(sysrows, 256)
    Pp, Pm = eig_proj(N, 1), eig_proj(N, -1)
    p, m = rank(Pp), rank(Pm)
    S_pm = kron(Pp, Pm)       # control +, target -
    S_mm = kron(Pm, Pm)
    S_pp = kron(Pp, Pp)
    S_mp = kron(Pm, Pp)
    I16 = eye(16)
    ok_struct = True
    for v in basis:
        G = [v[r * 16:(r + 1) * 16] for r in range(16)]
        # G S_pm lands in S_mm and G S_mm lands in S_pm; target-even sectors preserved
        if mm(mm(S_pm, G), S_pm) != zeros(16, 16) or mm(mm(S_pp, G), S_pm) != zeros(16, 16) or \
           mm(mm(S_mp, G), S_pm) != zeros(16, 16):
            ok_struct = False
            break
        if mm(mm(S_mm, G), S_mm) != zeros(16, 16) or mm(mm(S_pp, G), S_mm) != zeros(16, 16) or \
           mm(mm(S_mp, G), S_mm) != zeros(16, 16):
            ok_struct = False
            break
    coeffs = [Fr(((7 * i * i + 3 * i + 1) % 23) - 11, (i % 5) + 1) for i in range(len(basis))]
    Ggen = [[sum(c * v[r * 16 + col] for c, v in zip(coeffs, basis)) for col in range(16)] for r in range(16)]
    rk = rank(Ggen)
    bound = 16 - abs(p * m - m * m)
    balanced = (p == m)
    check("L %s: split (%d,%d); solution space dim %d; sector rule on every basis element; generic rank %d; "
          "bound 16-|pm-mm| = %d; invertible solution exists iff balanced"
          % (nm, p, m, len(basis), rk, bound), ok_struct and rk <= bound and ((rk == 16) == balanced))


# ------------------------------------------------------------------ A: census for diagonal NOTs
def max_matching(adj, nl, nr):
    match_r = [-1] * nr

    def aug(u, seen):
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                if match_r[v] == -1 or aug(match_r[v], seen):
                    match_r[v] = u
                    return True
        return False
    size = 0
    for u in range(nl):
        if aug(u, [False] * nr):
            size += 1
    return size


def build_GJ(signs):
    """signs[0] = +1 (unit), signs[-1] = -1 (z = last). Balanced required."""
    n = len(signs)
    plus = [i for i in range(n) if signs[i] == 1]
    minus = [i for i in range(n) if signs[i] == -1]
    assert len(plus) == len(minus)
    perm = {}
    # unit <-> z, then pair the rest in order
    perm[0], perm[n - 1] = n - 1, 0
    rp = [i for i in plus if i != 0]
    rm = [i for i in minus if i != n - 1]
    for a, b in zip(rp, rm):
        perm[a], perm[b] = b, a
    G = zeros(n * n, n * n)
    for mu in range(n):
        for nu in range(n):
            if signs[nu] == 1:
                G[mu * n + nu][mu * n + nu] = Fr(1)
            else:
                G[perm[mu] * n + nu][mu * n + nu] = Fr(1)
    return G, perm


import sys as _s
_s.setrecursionlimit(10000)
census = []
GJS = {}
for d in (1, 2, 3, 5, 7, 9):
    for p in range(0, d):
        mtan = d - p
        signs = [1] + [1] * p + [-1] * mtan          # z is the last coordinate, in the -1 block
        n = d + 1
        # allowed entries: s_nu' = s_nu and s_mu' s_mu = s_nu
        adj = [[] for _ in range(n * n)]
        for mu, nu in itertools.product(range(n), range(n)):
            for mu2, nu2 in itertools.product(range(n), range(n)):
                if signs[nu2] == signs[nu] and signs[mu2] * signs[mu] == signs[nu]:
                    adj[mu * n + nu].append(mu2 * n + nu2)
        tr_rank = max_matching(adj, n * n, n * n)
        bal = (1 + p == mtan)
        census.append((d, p, mtan, tr_rank, n * n, bal))
        if bal:
            N = diagm(signs[1:])
            G, perm = build_GJ(signs)
            rt, rc = rels_ok(G, N)
            z = [0] * (d - 1) + [1]
            inv = rank(G) == n * n
            GJS[(d, p)] = (G, perm, signs)
            check("A d=%d tangent (%d,%d): explicit G_J meets frame, relT, relC and is invertible" % (d, p, mtan),
                  frame_ok(G, z) and rt and rc and inv)
print("     census (d, p_tan, m_tan, term rank / (d+1)^2, balanced):")
for row in census:
    print("       d=%d (%d,%d): %d/%d %s" % row)
check("A full term rank <=> balanced, over all %d diagonal cases" % len(census),
      all((tr == full) == bal for (_, _, _, tr, full, bal) in census))
check("A Hurwitz level-exchange NOTs (tangent (1,k)): algebraic gate exists exactly for C (d=3) and the classical "
      "bit (d=1, (0,1))",
      [(d, p) for (d, p, m, tr, full, bal) in census if tr == full and (p == 1 or d == 1) and d in (1, 2, 3, 5, 9)]
      == [(1, 0), (3, 1)])

# ------------------------------------------------------------------ P: positivity of the balanced G_J
for (d, p), (G, perm, signs) in sorted(GJS.items()):
    n = d + 1
    if p == 0:
        # d = 1: G_J is the classical gate (frame forces it); compare with cnot1
        check("P d=1: G_J equals the kernel cnot1", G == CNOT1)
        continue
    x = [Fr(0)] * d
    x[0] = Fr(1)                      # e1, the first +1 tangent axis (coordinate index 1)
    y = [Fr(0)] * d
    y[d - 1] = Fr(1)                  # z
    j1 = perm[1]                      # J(e1) as a homogenized index in V-
    u = [Fr(0)] * d
    u[j1 - 1] = Fr(3, 5)
    u[d - 1] += Fr(4, 5)
    a = [Fr(1)] + [-t for t in u]
    b = [Fr(1)] + [Fr(0)] * (d - 1) + [Fr(1)]
    val = pairval(a, b, mv(G, prodstate(x, y)))
    lor_ok = sum(t * t for t in u) == 1
    check("P d=%d tangent (%d,%d): Lorentz effects a, b; pairVal(a, b, G_J(prodState e1 z)) = %s < 0 (posFwd fails)"
          % (d, p, d - p, val), lor_ok and val < 0)
G3J = GJS[(3, 1)][0]
check("P d=3: G_J differs from the kernel cnot (cnot carries a target twist on the target-odd sector)", G3J != CNOT)
# the target twist of cnot: on control e1 (x), target-odd inputs e3 (z), e2 (y) -> control e2 (y) times K(target)
Kimg = {}
for t in (2, 3):
    col = mv(CNOT, [Fr(int(i == 1 * 4 + t)) for i in range(16)])
    Kimg[t] = [(i // 4, i % 4, str(v)) for i, v in enumerate(col) if v]
print("     cnot on control x (index 1) x target-odd: e1(x)e2(y) ->", Kimg[2], "; e1(x)e3(z) ->", Kimg[3])
Kmat = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]
for t in (2, 3):
    col = mv(CNOT, [Fr(int(i == 1 * 4 + t)) for i in range(16)])
    for i, v in enumerate(col):
        if v and i // 4 == 2:
            Kmat[(i % 4) - 2][t - 2] = v
check("P d=3: cnot's target twist K on V-_tan = span(y, z) satisfies K^2 = -1 (a complex structure on the target "
      "minus plane)", mm(Kmat, Kmat) == neg(eye(2)), "K = %s" % [[str(t) for t in r] for r in Kmat])

fails = [nm for nm, c in CHECKS if not c]
print("SUMMARY %d checks, %d failed" % (len(CHECKS), len(fails)))
if fails:
    print("VERDICT NOT RENDERED (a control failed)")
else:
    bal = sorted(set((d, p, d - p) for (d, p, m, tr, full, b) in census if tr == full))
    print("VERDICT RENDERED: an invertible G with frame+relT+relC exists exactly for balanced splits %s; "
          "the gate complex structure J (J^2 = -1 on the target-odd sector) holds for cnot and for the classical "
          "cnot1; balanced G_J fails posFwd at d = 3, 5, 7, 9 by an explicit witness; Q-FWD covariance holds for "
          "the rational pi-rotation N'" % bal)
