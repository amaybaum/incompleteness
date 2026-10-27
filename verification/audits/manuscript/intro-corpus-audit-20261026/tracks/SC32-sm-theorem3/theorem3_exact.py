#!/usr/bin/env python3
"""SC-32: SM Theorem 3 (center independence and staggered chirality), exact checks.

Objects, as SM defines them.
  * The reversible isotropic nearest-neighbour rule of SM 4.1/4.4, scalar case:
        phi(n,t+1) = C phi(n,t) + alpha sum_j [phi(n+e_j,t) + phi(n-e_j,t)] - phi(n,t-1).
    Center independence (CI) is C = 0 (SM 4.4). Theorem 1's branch is alpha = 1/d.
  * Its operator on a periodic lattice, axis 0 = time, d spatial axes:
        R(C,alpha) = T0 + T0^-1 - alpha sum_j (Tj + Tj^-1) - C.
    Theorem 2 reads it on the doubled lattice, where the shifts are Tmu^2:
        K(C,alpha) = T0^2 + T0^-2 - alpha sum_j (Tj^2 + Tj^-2) - C.
  * The staggered generators A_mu = eta_mu (T_mu - T_mu^-1), eta_mu(x) = (-1)^(x_0+...+x_{mu-1}),
    so B = 2 D_st (the repository convention), and the site parity eps(x) = (-1)^(sum x).
  * Exact chiral symmetry is SM's criterion chi -> eps chi, i.e. {D, eps} = 0.
  * Isotropic staggered family: B(a0,a) = a0 A_0 + a S with S = sum_j A_j; a scalar on-site
    mass enters as B + m (with K = (B - m)(B + m) = B^2 - m^2) or as B + m eps
    (with (B + m eps)^2 = B^2 + m^2).  With a0 = 1 and a^2 = -alpha (a = i sqrt(alpha)),
    B^2 = A_0^2 - alpha S^2 once {A_0, S} = 0 is checked, so every entry below is rational.

Everything is exact: sparse matrices over Fraction, equality by entries. No floating point.
Deterministic output. Exit status nonzero on any failed check.
"""
from fractions import Fraction as Fr
import itertools
import sys

FAILS = []


def check(cond, label):
    if not cond:
        FAILS.append(label)
    return bool(cond)


# ---------------------------------------------------------------- sparse exact matrices
class M:
    def __init__(self, n, rows=None):
        self.n = n
        self.r = rows if rows is not None else {}

    @staticmethod
    def eye(n, c=1):
        return M(n, {i: {i: Fr(c)} for i in range(n)}) if c else M(n)

    @staticmethod
    def diag(vals):
        return M(len(vals), {i: {i: Fr(v)} for i, v in enumerate(vals) if v})

    def _clean(self):
        self.r = {i: {j: v for j, v in row.items() if v} for i, row in self.r.items()}
        self.r = {i: row for i, row in self.r.items() if row}
        return self

    def __add__(self, o):
        out = {i: dict(row) for i, row in self.r.items()}
        for i, row in o.r.items():
            tgt = out.setdefault(i, {})
            for j, v in row.items():
                tgt[j] = tgt.get(j, 0) + v
        return M(self.n, out)._clean()

    def scale(self, c):
        c = Fr(c)
        return M(self.n, {i: {j: c * v for j, v in row.items()} for i, row in self.r.items()})._clean()

    def __sub__(self, o):
        return self + o.scale(-1)

    def __matmul__(self, o):
        out = {}
        for i, row in self.r.items():
            acc = {}
            for k, v in row.items():
                for j, w in o.r.get(k, {}).items():
                    acc[j] = acc.get(j, 0) + v * w
            if acc:
                out[i] = acc
        return M(self.n, out)._clean()

    def __eq__(self, o):
        return self.n == o.n and self._clean().r == o._clean().r

    def __ne__(self, o):
        return not self == o

    def iszero(self):
        return not self._clean().r

    def get(self, i, j):
        return self.r.get(i, {}).get(j, Fr(0))


def anti(X, Y):
    return X @ Y + Y @ X


# ---------------------------------------------------------------- the lattice
class Lattice:
    def __init__(self, d, L):
        self.d, self.L, self.nax = d, L, d + 1
        self.sites = list(itertools.product(range(L), repeat=self.nax))
        self.idx = {x: i for i, x in enumerate(self.sites)}
        self.N = len(self.sites)

    def shift(self, mu, k):
        """(T_mu^k f)(x) = f(x + k e_mu)."""
        rows = {}
        for x, i in self.idx.items():
            y = list(x)
            y[mu] = (y[mu] + k) % self.L
            j = self.idx[tuple(y)]
            rows.setdefault(i, {})
            rows[i][j] = rows[i].get(j, 0) + Fr(1)
        return M(self.N, rows)._clean()

    def eta(self, mu, staggered=True):
        return M.diag([(-1) ** sum(x[:mu]) if staggered else 1 for x in self.sites])

    def eps(self):
        return M.diag([(-1) ** sum(x) for x in self.sites])

    def A(self, mu, staggered=True):
        return self.eta(mu, staggered) @ (self.shift(mu, 1) - self.shift(mu, -1))

    def K(self, C, alpha):
        """The rule's operator on the doubled lattice, built from shifts only."""
        out = self.shift(0, 2) + self.shift(0, -2)
        for j in range(1, self.nax):
            out = out - (self.shift(j, 2) + self.shift(j, -2)).scale(alpha)
        return out - M.eye(self.N, C)


def R_rule(d, Lh, C, alpha):
    """The rule's operator on the spacing-1 lattice Z_Lh^(d+1)."""
    lat = Lattice(d, Lh)
    out = lat.shift(0, 1) + lat.shift(0, -1)
    for j in range(1, lat.nax):
        out = out - (lat.shift(j, 1) + lat.shift(j, -1)).scale(alpha)
    return lat, out - M.eye(lat.N, C)


def fmt(x):
    return str(Fr(x))


out = []


def say(s):
    out.append(s)


# ---------------------------------------------------------------- G1 generator relations
say("G1  staggered generator relations (exact, even periodic extents)")
CASES = [(1, 4), (1, 6), (2, 4), (2, 6), (3, 4), (3, 6)]
cache = {}
for d, L in CASES:
    lat = Lattice(d, L)
    A = [lat.A(mu) for mu in range(lat.nax)]
    eps = lat.eps()
    I = M.eye(lat.N)
    ok_anti = all(anti(A[m], A[n]).iszero() for m in range(lat.nax) for n in range(m + 1, lat.nax))
    ok_sq = all(A[m] @ A[m] == lat.shift(m, 2) + lat.shift(m, -2) - I.scale(2) for m in range(lat.nax))
    ok_eps = all(anti(A[m], eps).iszero() for m in range(lat.nax)) and eps @ eps == I
    check(ok_anti and ok_sq and ok_eps, f"G1 d={d} L={L}")
    say(f"    d={d} L={L} sites={lat.N}: {{A_mu,A_nu}}=0 {ok_anti}; A_mu^2=T^2+T^-2-2 {ok_sq}; "
        f"{{A_mu,eps}}=0, eps^2=I {ok_eps}")
    cache[(d, L)] = (lat, A, eps, I)

# Countercontrols: the relations have teeth.
lat = Lattice(2, 4)
A_flat = [lat.A(mu, staggered=False) for mu in range(lat.nax)]
c1 = not anti(A_flat[0], A_flat[1]).iszero()
lat_odd = Lattice(1, 3)
A_odd = [lat_odd.A(mu) for mu in range(lat_odd.nax)]
c2 = not anti(A_odd[0], A_odd[1]).iszero()
check(c1 and c2, "G1 countercontrols")
say(f"    countercontrol, eta := 1 (no staggering), d=2 L=4: {{A_0,A_1}} != 0 {c1}")
say(f"    countercontrol, odd extent d=1 L=3: {{A_0,A_1}} != 0 {c2}")

# ---------------------------------------------------------------- G2 mass identity
say("")
say("G2  K(C,alpha) = B^2 - mu*I with mu = C - 2(1 - d*alpha), B = A_0 + i sqrt(alpha) S")
say("    (B^2 = A_0^2 - alpha S^2 after {A_0,S} = 0 is checked; K built from shifts only)")
GRID_C = [Fr(0), Fr(-2), Fr(-4), Fr(3, 2)]
for d, L in CASES:
    lat, A, eps, I = cache[(d, L)]
    S = A[1]
    for j in range(2, lat.nax):
        S = S + A[j]
    ok_cross = anti(A[0], S).iszero()
    A0sq, Ssq = A[0] @ A[0], S @ S
    allok = ok_cross
    for alpha in (Fr(1), Fr(1, d), Fr(1, 2)):
        B2 = A0sq - Ssq.scale(alpha)
        for C in GRID_C + [2 * (1 - d * alpha)]:
            mu = C - 2 * (1 - d * alpha)
            allok &= (B2 - lat.K(C, alpha)) == I.scale(mu)
    check(allok, f"G2 d={d} L={L}")
    say(f"    d={d} L={L}: {{A_0,S}}=0 {ok_cross}; identity on alpha in {{1, 1/d, 1/2}} x C grid {allok}")

# Countercontrol: the identity rejects a wrong mass formula (the d-blind mu' = C - 2(1 - alpha)).
lat, A, eps, I = cache[(2, 4)]
S = A[1] + A[2]
B2 = A[0] @ A[0] - (S @ S).scale(Fr(1, 2))
wrong = (B2 - lat.K(Fr(0), Fr(1, 2))) != I.scale(Fr(0) - 2 * (1 - Fr(1, 2)))
check(wrong, "G2 countercontrol")
say(f"    countercontrol, d=2 L=4 alpha=1/2 C=0: d-blind mu' = C - 2(1 - alpha) rejected {wrong}")

# The doubled-lattice reading: K restricted to the sublattice 2Z^(d+1) is the spacing-1 rule,
# and K never couples different cosets of 2Z^(d+1).
say("")
say("G3  doubled-lattice reading: K(C,alpha) on (2Z_L)^(d+1) equals R(C,alpha) on Z_(L/2)^(d+1)")
for d, L in [(1, 6), (2, 6), (3, 6)]:
    lat = cache[(d, L)][0]
    ok = True
    for C, alpha in ((Fr(0), Fr(1, d)), (Fr(2 * (1 - d)), Fr(1)), (Fr(0), Fr(1))):
        Kd = lat.K(C, alpha)
        latH, Rh = R_rule(d, L // 2, C, alpha)
        coset = lambda x: tuple(c % 2 for c in x)
        nomix = all(coset(lat.sites[i]) == coset(lat.sites[j]) for i, row in Kd.r.items() for j in row)
        emb = {latH.idx[tuple(c // 2 for c in x)]: i for i, x in enumerate(lat.sites)
               if all(c % 2 == 0 for c in x)}
        same = all(Kd.get(emb[a], emb[b]) == Rh.get(a, b) for a in emb for b in emb)
        ok &= nomix and same
    check(ok, f"G3 d={d}")
    say(f"    d={d} L={L}: cosets decouple and the even coset carries R(C,alpha), three (C,alpha) {ok}")

# ---------------------------------------------------------------- G4 decisive cases
say("")
say("G4  decisive cases (d=3, L=6 unless stated; mu = C - 2(1 - d alpha))")
lat, A, eps, I = cache[(3, 6)]
S = A[1] + A[2] + A[3]
A0sq, Ssq = A[0] @ A[0], S @ S
# Chirality of the massless operator, checked on the two real parts of B = A_0 + i b S:
# {B, eps} = {A_0, eps} + i b {S, eps}, so both real anticommutators must vanish.
chiral_B = anti(A[0], eps).iszero() and anti(S, eps).iszero()
check(chiral_B, "G4 {B,eps}=0")
say(f"    {{B, eps}} = 0 for every b (both real parts vanish): {chiral_B}")
m_I = lambda m: anti(I.scale(m), eps) == eps.scale(2 * m)      # {B + m, eps} = 2 m eps
m_E = lambda m: anti(eps.scale(m), eps) == I.scale(2 * m)      # {B + m eps, eps} = 2 m I
check(m_I(2) and m_E(2), "G4 mass anticommutators")
say(f"    {{B + m, eps}} = 2m eps and {{B + m eps, eps}} = 2m I at m=2: {m_I(2) and m_E(2)}")

d = 3
rows = [
    ("T1  Theorem 1 branch, CI", Fr(0), Fr(1, 3)),
    ("RM  SM Remark, C = 2(1-d), alpha = 1", Fr(2 * (1 - d)), Fr(1)),
    ("U1  CI at unit coefficient alpha = 1", Fr(0), Fr(1)),
    ("T2  alpha = 1/d with C = 2(1-d)", Fr(2 * (1 - d)), Fr(1, 3)),
    ("H   alpha = 1/2, C = 2(1 - d/2)", Fr(2) * (1 - Fr(3, 2)), Fr(1, 2)),
]
RES = {}
for name, C, alpha in rows:
    tag = name.split()[0]
    mu = C - 2 * (1 - d * alpha)
    B2 = A0sq - Ssq.scale(alpha)
    K = lat.K(C, alpha)
    ident = (B2 - K) == I.scale(mu)
    # The emergent staggered operator F = B + (on-site mass), with K = (B - m)(B + m) when
    # mu = m^2 > 0 and K = (B + m eps)^2 when mu = -m^2 < 0. The rows have |mu| a perfect square.
    m = next(Fr(k) for k in range(0, 10) if k * k == abs(mu))
    if mu > 0:
        mass = I.scale(m)
        fact = (B2 - I.scale(m * m)) == K
    elif mu < 0:
        mass = eps.scale(m)
        fact = (B2 + I.scale(m * m)) == K          # (B + m eps)^2 = B^2 + m^2 since {B, eps} = 0
    else:
        mass = M(lat.N)
        fact = B2 == K
    chiral = chiral_B and anti(mass, eps).iszero()   # {F, eps} = {B, eps} + {mass, eps}
    Kones = [sum(v for v in K.r.get(i, {}).values()) for i in range(lat.N)]
    const_kernel = all(v == 0 for v in Kones)
    ci = (C == 0)
    check(ident and fact, f"G4 {tag}")
    check(chiral == const_kernel, f"G4 constant-preservation {tag}")
    RES[tag] = dict(ci=ci, chiral=chiral, m=m, C=C, alpha=alpha)
    say(f"    {name}: C={fmt(C)} alpha={fmt(alpha)} -> mu={fmt(mu)}, mass {fmt(m)}"
        f"{' (m eps)' if mu < 0 else ''}; K factorizes {fact}; CI {ci}; "
        f"{{F, eps}} = 0 {chiral}; K annihilates constants {const_kernel}")

# ---------------------------------------------------------------- G5 uniqueness in the family
say("")
say("G5  coefficient identification: supports of I, T_0^{+-2}, T_j^{+-2} are disjoint")
for dd, LL in [(1, 6), (2, 6), (3, 6)]:
    lat = cache[(dd, LL)][0]
    def offsets(Mx):
        s = set()
        for i, row in Mx.r.items():
            for j in row:
                xi, xj = lat.sites[i], lat.sites[j]
                s.add(tuple((b - a) % LL for a, b in zip(xi, xj)))
        return s
    pieces = [M.eye(lat.N), lat.shift(0, 2) + lat.shift(0, -2)]
    pieces += [lat.shift(j, 2) + lat.shift(j, -2) for j in range(1, lat.nax)]
    sets = [offsets(p) for p in pieces]
    disjoint = all(not (sets[a] & sets[b]) for a in range(len(sets)) for b in range(a + 1, len(sets)))
    check(disjoint, f"G5 d={dd}")
    say(f"    d={dd} L={LL}: disjoint {disjoint}")
say("    hence lambda K(C,alpha) = B(a0,a)^2 -+ m^2 forces a0^2 = lambda, a^2 = -lambda alpha and")
say("    m^2 = +-lambda (C - 2(1 - d alpha)): m = 0 iff C = 2(1 - d alpha) within the family")

# ---------------------------------------------------------------- verdict text from measurements
say("")
if FAILS:
    say("VERDICT  VOID (failed checks: " + ", ".join(FAILS) + ")")
else:
    say("VERDICT  all controls green")
    T1, RM, U1, T2 = RES["T1"], RES["RM"], RES["U1"], RES["T2"]
    say("  CI => chiral at alpha = 1/d (T1): " + ("holds" if T1["ci"] and T1["chiral"] else "fails"))
    say("  CI => chiral at alpha = 1 (U1): "
        + ("holds" if U1["chiral"] else "fails, staggered mass " + fmt(U1["m"])))
    say("  chiral => CI at alpha = 1 (RM, C = " + fmt(RM["C"]) + "): "
        + ("fails" if RM["chiral"] and not RM["ci"] else "not refuted"))
    say("  chiral => CI at fixed alpha = 1/d (T2, center-dependent): "
        + ("T2 not chiral, consistent" if not T2["chiral"] else "refuted"))
    agree = all(r["chiral"] == (r["C"] + 2 * d * r["alpha"] == 2) for r in RES.values())
    say("  chirality coincides with C + 2 d alpha = 2 in every row: " + str(agree))
print("\n".join(out))
sys.exit(1 if FAILS else 0)
