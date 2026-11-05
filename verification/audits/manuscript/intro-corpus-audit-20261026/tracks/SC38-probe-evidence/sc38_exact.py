#!/usr/bin/env python3
"""SC-38: exact re-checks behind the probe and evidence statements of Main §2.3, §2.4, §1.3 and §3.4.

Every verdict below is decided in exact arithmetic. Probabilities are Fractions. An information
quantity sum_i p_i log2 r_i with rational p_i, r_i is held exactly as a vector of rational
coefficients on log2 of primes; since the logarithms of distinct primes are linearly independent
over Q, it is zero iff every coefficient is zero. A strict sign is decided by mpmath interval
arithmetic (outward rounding) on that exact vector, and a check fails if the interval does not
exclude zero. Floating-point values are printed as diagnostics only.

Sections:
  A  CON-24: the size of a model reproducing Main §2.4 (2, 3 and 6 hidden states; one hidden value).
  B  CON-25: the five families of c4_backflow_probes.py, readback-lemma inequality decided exactly.
  C  CON-26: Main §3.4 "Remark (a variational question)" count at (n_V,|C_H|) = (2,3), t = 2.
  D  exact re-check of the floating-point parts of memory_probes.py (c), primitive_probes.py (B),(C)
     and purification_probes.py (6), which Main cites as certifications.
Controls: each section carries a must-fire countercontrol; see the CONTROL lines.

Usage: python3 -I sc38_exact.py
"""
import sys
from fractions import Fraction as F
from itertools import permutations
from collections import defaultdict
from mpmath import iv
import sympy as sp

iv.dps = 60
FAIL = []


def check(name, ok, msg=""):
    print(("PASS " if ok else "FAIL ") + name + ((" : " + msg) if msg else ""))
    if not ok:
        FAIL.append(name)


# ---------------------------------------------------------------- exact log algebra
_fcache = {}


def factor(n):
    if n in _fcache:
        return _fcache[n]
    out, m, p = {}, n, 2
    while p * p <= m:
        while m % p == 0:
            out[p] = out.get(p, 0) + 1
            m //= p
        p += 1
    if m > 1:
        out[m] = out.get(m, 0) + 1
    _fcache[n] = out
    return out


class L:
    """exact element of the Q-span of {log2 p : p prime}: {p: rational coefficient}."""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {p: v for p, v in (c or {}).items() if v != 0}

    @staticmethod
    def log2(r):
        r = F(r)
        assert r > 0
        c = defaultdict(F)
        for p, e in factor(r.numerator).items():
            c[p] += e
        for p, e in factor(r.denominator).items():
            c[p] -= e
        return L(c)

    def __add__(self, o):
        c = defaultdict(F, self.c)
        for p, v in o.c.items():
            c[p] += v
        return L(c)

    def __sub__(self, o):
        return self + o.scale(-1)

    def scale(self, k):
        return L({p: v * k for p, v in self.c.items()})

    def is_zero(self):
        return not self.c

    def rational(self):
        """the value if it is a rational number (only log2 2 = 1 present), else None."""
        if all(p == 2 for p in self.c):
            return self.c.get(2, F(0))
        return None

    def interval(self):
        s = iv.mpf(0)
        for p, v in self.c.items():
            s += iv.mpf(v.numerator) / iv.mpf(v.denominator) * iv.log(iv.mpf(p)) / iv.log(iv.mpf(2))
        return s

    def sign(self):
        if self.is_zero():
            return 0
        x = self.interval()
        if x.a > 0:
            return 1
        if x.b < 0:
            return -1
        raise RuntimeError("interval does not decide the sign")

    def __float__(self):
        return float(self.interval().mid)


def cmi(joint):
    """exact I(A;B|C) in bits from {(a, c, b): p}."""
    pc, pac, pcb = defaultdict(F), defaultdict(F), defaultdict(F)
    for (a, c, b), p in joint.items():
        pc[c] += p
        pac[(a, c)] += p
        pcb[(c, b)] += p
    out = L()
    for (a, c, b), p in joint.items():
        if p:
            out = out + L.log2(p * pc[c] / (pac[(a, c)] * pcb[(c, b)])).scale(p)
    return out


def entropy(dist):
    out = L()
    for p in dist.values():
        if p:
            out = out - L.log2(p).scale(p)
    return out


# ---------------------------------------------------------------- A. CON-24
print("== A  CON-24: hidden-state count of a model reproducing Main §2.4 ==")


def model(flip, swaps, nH):
    """sigma on {0,1} x {1..nH}: h in flip -> (0,h)<->(1,h); swaps -> (x,a)<->(x,b) for both x."""
    s = {(x, h): (x, h) for x in (0, 1) for h in range(1, nH + 1)}
    for h in flip:
        s[(0, h)], s[(1, h)] = (1, h), (0, h)
    for a, b in swaps:
        for x in (0, 1):
            s[(x, a)], s[(x, b)] = (x, b), (x, a)
    assert sorted(s.values()) == sorted(s), "not a bijection"
    return s


def numbers(s, nH):
    """T(1,0), T(2,0), Lambda(2,1) (or None if T1 singular), P(x2=0|x1=1,x0=0), P(x2=0|x1=1)."""
    w = F(1, 2 * nH)
    T = [[[F(0)] * 2 for _ in range(2)] for _ in range(2)]
    j3 = defaultdict(F)
    for (x, h) in s:
        y = s[(x, h)]
        z = s[y]
        T[0][x][y[0]] += F(1, nH)
        T[1][x][z[0]] += F(1, nH)
        j3[(x, y[0], z[0])] += w
    T1, T2 = T
    det = T1[0][0] * T1[1][1] - T1[0][1] * T1[1][0]
    lam = None
    if det != 0:
        inv = [[T1[1][1] / det, -T1[0][1] / det], [-T1[1][0] / det, T1[0][0] / det]]
        lam = [[sum(inv[i][k] * T2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    c1 = j3[(0, 1, 0)] / (j3[(0, 1, 0)] + j3[(0, 1, 1)])
    p1 = sum(v for (a, b, c), v in j3.items() if b == 1)
    c2 = sum(v for (a, b, c), v in j3.items() if b == 1 and c == 0) / p1
    return T1, T2, lam, c1, c2


half = F(1, 2)
J2 = [[half, half], [half, half]]
I2 = [[F(1), F(0)], [F(0), F(1)]]
T1_main = [[F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]]
lam_main = [[F(2), F(-1)], [F(-1), F(2)]]

s6 = model([1, 2], [(3, 4), (5, 6)], 6)        # Main §2.4 / book §1.5
T1, T2, lam, c1, c2 = numbers(s6, 6)
check("A1 six-hidden model (Main §2.4): T(1,0), T(2,0)=I, Lambda(2,1), conditionals 1 and 1/3",
      T1 == T1_main and T2 == I2 and lam == lam_main and c1 == 1 and c2 == F(1, 3))
s3 = model([1], [(2, 3)], 3)
T1, T2, lam, c1, c2 = numbers(s3, 3)
check("A2 three-hidden model (h=1 flips x; h=2,3 swap) reproduces every number of Main §2.4",
      T1 == T1_main and T2 == I2 and lam == lam_main and c1 == 1 and c2 == F(1, 3))
s2 = model([1], [], 2)
T1, T2, lam, c1, c2 = numbers(s2, 2)
check("A3 two-hidden model (h=1 flips, h=2 fixes): T(1,0) = J/2 and T(2,0) = I",
      T1 == J2 and T2 == I2 and lam is None)
# T(2,0) = T(1,0) Lambda is impossible with T(1,0) = J/2: J/2 . Lambda has identical rows.
lsym = [[sp.Symbol(f"l{i}{j}") for j in range(2)] for i in range(2)]
prod = [[sp.expand(sum(sp.Rational(T1[i][k].numerator, T1[i][k].denominator) * lsym[k][j] for k in range(2))) for j in range(2)] for i in range(2)]
check("A3' (J/2) Lambda has identical rows for a symbolic 2x2 Lambda, so T(2,0) = I has no divisor",
      prod[0] == prod[1] and I2[0] != I2[1])
swap = {(x, h): (h, x) for x in (0, 1) for h in (0, 1)}   # book ch01 card game: hole <-> burn
w = F(1, 2)
Tg1 = [[F(0)] * 2 for _ in range(2)]
Tg2 = [[F(0)] * 2 for _ in range(2)]
for (x, h) in swap:
    Tg1[x][swap[(x, h)][0]] += w
    Tg2[x][swap[swap[(x, h)]][0]] += w
check("A4 card game of book §1.11 (one burn card, swap): two hidden values, T1 = J/2, T2 = I",
      Tg1 == J2 and Tg2 == I2)
# one hidden value: every phi^k is a permutation of C_V, so every T(k,0) is a permutation matrix
ok = True
for perm in permutations(range(2)):
    for k in (1, 2, 3):
        x = list(range(2))
        for _ in range(k):
            x = [perm[v] for v in x]
        Tk = [[F(int(x[i] == j)) for j in range(2)] for i in range(2)]
        ok &= all(sorted(r) == [0, 1] for r in Tk)
check("A5 one hidden value: every T(k,0) is a permutation matrix (no indivisibility witness)", ok)
check("A6 CONTROL (must differ): a four-hidden model flipping on h=1,2 has T(1,0) = J/2, not Main's",
      numbers(model([1, 2], [(3, 4)], 4), 4)[0] == J2 != T1_main)

# ---------------------------------------------------------------- B. CON-25
print("\n== B  CON-25: c4_backflow_probes.py families, readback lemma decided exactly ==")


def gap_bound(tab):
    """max over endpoint-sharing history pairs of p0 * delta^2 (exact); the lemma's bound is this / ln 2."""
    laws = defaultdict(lambda: defaultdict(F))
    for (a, c, b), p in tab.items():
        laws[(a, c)][b] += p
    best = F(0)
    keys = list(laws)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            if keys[i][1] != keys[j][1]:
                continue
            w1, w2 = sum(laws[keys[i]].values()), sum(laws[keys[j]].values())
            sup = set(laws[keys[i]]) | set(laws[keys[j]])
            tv = sum(abs(laws[keys[i]][b] / w1 - laws[keys[j]][b] / w2) for b in sup) / 2
            best = max(best, min(w1, w2) * tv * tv)
    return best


def lemma_holds(I, b):
    """I (bits) >= b/ln2  <=>  I*ln2 - b >= 0, decided on an interval enclosure."""
    if b == 0:
        return I.sign() >= 0
    x = I.interval() * iv.log(iv.mpf(2)) - iv.mpf(b.numerator) / iv.mpf(b.denominator)
    if x.a >= 0:
        return True
    if x.b < 0:
        return False
    raise RuntimeError("undecided")


tab = {((x0,), x1, (x0,)): F(1, 4) for x0 in (0, 1) for x1 in (0, 1)}
I, b = cmi(tab), gap_bound(tab)
check("B1 Q1 gap family: I = 1 bit exactly, p0 delta^2 = 1/4, lemma holds",
      I.rational() == 1 and b == F(1, 4) and lemma_holds(I, b))
phiR = {(0, 0): (0, 0), (0, 1): (0, 1), (1, 0): (1, 0), (1, 1): (2, 0), (2, 0): (1, 1), (2, 1): (2, 1)}
tab = defaultdict(F)
for x0 in range(3):
    for h in range(2):
        s1 = phiR[(x0, h)]
        tab[((x0,), s1[0], (phiR[s1][0],))] += F(1, 6)
I, b = cmi(tab), gap_bound(tab)
check("B2 Q2 revival family: I = 2/3 bit exactly, p0 delta^2 = 1/6, lemma holds",
      I.rational() == F(2, 3) and b == F(1, 6) and lemma_holds(I, b))
tab = {}
for x0 in (0, 1):
    s = F(1, 8) if x0 == 0 else F(-1, 8)
    for x1 in (0, 1):
        for x2 in (0, 1):
            tab[((x0,), x1, (x2,))] = F(1, 4) * ((half + s) if x2 == 0 else (half - s))
I, b = cmi(tab), gap_bound(tab)
check("B3 Q5 small-gap family: p0 delta^2 = 1/64, I irrational (not in Q), lemma holds strictly",
      b == F(1, 64) and I.rational() is None and lemma_holds(I, b),
      f"I = {float(I):.12f} bits, bound = {1 / 64 / 0.6931471805599453:.12f} (diagnostic floats)")
# Q3: the i.i.d. fair coin at horizon 4 (the law the dilation realizes; exact product law)
traj = {tuple((n >> i) & 1 for i in range(5)): F(1, 32) for n in range(32)}
ok = True
for k in range(1, 4):
    tab = defaultdict(F)
    for tr, p in traj.items():
        tab[(tr[:k], tr[k], tr[k + 1:])] += p
    ok &= cmi(tab).is_zero() and gap_bound(tab) == 0
check("B4 Q3 fair coin: the target product law of X0..X4 checked directly (not the dilation): I = 0 and no gap at every order, exactly", ok)
check("B5 CONTROL (must fire): Q1 with readback removed (X2 independent of X0) has I = 0 and no gap",
      cmi({((x0,), x1, (x2,)): F(1, 8) for x0 in (0, 1) for x1 in (0, 1) for x2 in (0, 1)}).is_zero()
      and gap_bound({((x0,), x1, (x2,)): F(1, 8) for x0 in (0, 1) for x1 in (0, 1) for x2 in (0, 1)}) == 0)
check("B6 CONTROL (must fire): the decision refutes I >= p0 delta^2/ln2 for I = 1 bit and p0 delta^2 = 1",
      not lemma_holds(L.log2(2), F(1)))  # I = 1 bit < 1/ln 2


# ---------------------------------------------------------------- shared enumeration helpers
def runs(perm, nV, nH, prior, steps):
    """[(visible path x0..x_steps, hidden h at each time, weight)] from prior on C_V x C_H."""
    out = []
    for s in range(nV * nH):
        if prior[s] == 0:
            continue
        xs, hs, t = [s // nH], [s % nH], s
        for _ in range(steps):
            t = perm[t]
            xs.append(t // nH)
            hs.append(t % nH)
        out.append((tuple(xs), tuple(hs), prior[s]))
    return out


# ---------------------------------------------------------------- C. CON-26
print("\n== C  CON-26: Main §3.4 variational remark at (n_V,|C_H|) = (2,3), t = 2, uniform prior ==")
nV, nH = 2, 3
N = nV * nH
uni = [F(1, N)] * N
by_law = defaultdict(list)
by_sig = defaultdict(list)
recs_all = []
for perm in permutations(range(N)):
    rs = runs(perm, nV, nH, uni, 3)
    law = defaultdict(F)
    for xs, hs, p in rs:
        law[xs] += p
    law = tuple(sorted(law.items()))
    # M_2 = I(X0X1; X3 | X2) and I_XH = I(X0X1; H2 | X2)
    jm, jh = defaultdict(F), defaultdict(F)
    for xs, hs, p in rs:
        jm[(xs[:2], xs[2], xs[3])] += p
        jh[(xs[:2], xs[2], hs[2])] += p
    M, IXH = cmi(jm), cmi(jh)
    # memory_probes.py's grouping key: the next-step conditional law for each (history, x2)
    tot = defaultdict(F)
    for xs, hs, p in rs:
        tot[xs[:3]] += p
    sig = defaultdict(F)
    for xs, hs, p in rs:
        sig[(xs[:3], xs[3])] += p / tot[xs[:3]]
    rec = (perm, M, IXH, law)
    recs_all.append(rec)
    by_law[law].append(rec)
    by_sig[tuple(sorted(sig.items()))].append(rec)


def hcond(law):
    """exact H(X0X1 | X2 X3) of a law of (x0..x3)."""
    j, m = defaultdict(F), defaultdict(F)
    for xs, p in law:
        j[xs] += p
        m[xs[2:]] += p
    return entropy(j) - entropy(m)


def summarize(groups, label):
    pos = att = 0
    resid = []
    bad_identity = 0
    for recs in groups.values():
        Ms = [r[1] for r in recs]
        if all(m.is_zero() for m in Ms):
            continue
        pos += 1
        best = None
        for perm, M, IXH, law in recs:
            r = IXH - M
            # identity of the Remark: every bijective completion has I_XH - M_t = H(X_<t | X_t, X_t+1)
            bad_identity += not (r - hcond(law)).is_zero()
            if best is None or (r - best).sign() < 0:
                best = r
        att += best.is_zero()
        resid.append(best)
    mx = resid[0]
    for r in resid[1:]:
        if (r - mx).sign() > 0:
            mx = r
    print(f"  {label}: {pos} groups with M_2 > 0; min_R I(X_<2;H_2|X_2) = M_2 in {att}; "
          f"max residual = {mx.rational() if mx.rational() is not None else float(mx)} bits")
    return pos, att, mx, bad_identity


pl, al, ml, bl = summarize(by_law, "grouped by the law of (X0..X3)")
ps, as_, ms, bs = summarize(by_sig, "grouped by memory_probes.py's conditional signature")
merged = [g for g in by_sig.values() if len({r[3] for r in g}) > 1]
check("C1 identity I(X_<2;H_2|X_2) - M_2 = H(X_<2|X_2,X_3) holds for all 720 realizations, exactly",
      bl == 0 and bs == 0)
check("C2 by law: 16 processes with M_2 > 0, of which 2 attain M_2 at |C_H| = 3", (pl, al) == (16, 2))
check("C3 by memory_probes.py's signature: 15 groups, 1 attaining (reproduces the probe's '1 of 15')",
      (ps, as_) == (15, 1))
check("C4 the signature merges distinct laws (so it does not count processes)",
      len(merged) >= 1, f"{len(merged)} signature group(s) hold {[len({r[3] for r in g}) for g in merged]} laws")
check("C5 the maximal residual is 2/3 bit exactly", ml.rational() == F(2, 3) and ms.rational() == F(2, 3))
# an attaining law has H(X_<2 | X_2, X_3) = 0, which no prior on its realizations changes (C1)
att_laws = [law for law, recs in by_law.items() if not all(r[1].is_zero() for r in recs) and hcond(law).is_zero()]
check("C6 the attaining laws are exactly those with H(X_<2 | X_2, X_3) = 0", len(att_laws) == 2)


def hcond_x2(law):
    """exact H(X0X1 | X2) of a law of (x0..x3): the wrong conditioning, for the must-fail control."""
    j, m = defaultdict(F), defaultdict(F)
    for xs, p in law:
        j[xs[:3]] += p
        m[xs[2]] += p
    return entropy(j) - entropy(m)


n_bad = sum(not ((IXH - M) - hcond_x2(law)).is_zero() for perm, M, IXH, law in recs_all)
check("C7 CONTROL (must fail): the identity with H(X_<2|X_2) in place of H(X_<2|X_2,X_3) fails",
      n_bad > 0, f"{n_bad} of 720 realizations violate it")
# horizon dependence of the count: group by the law of (X0..XK)
counts = {}
for K in range(3, 13):
    groups = defaultdict(list)
    for perm, M, IXH, law3 in recs_all:
        lawK = defaultdict(F)
        for xs, hs, p in runs(perm, nV, nH, uni, K):
            lawK[xs] += p
        groups[tuple(sorted(lawK.items()))].append((M, law3))
    pos = [g for g in groups.values() if not g[0][0].is_zero()]
    assert all(len({x[1] for x in g}) == 1 for g in groups.values())
    counts[K] = (len(pos), sum(hcond(g[0][1]).is_zero() for g in pos))
print("  (laws with M_2 > 0, attaining) by horizon K:", counts)
check("C8 the count depends on the horizon: 16 laws (2 attaining) of (X0..X3); 18 (2 attaining) for every K = 4..12",
      counts[3] == (16, 2) and all(counts[K] == (18, 2) for K in range(4, 13)))

# ---------------------------------------------------------------- D. other float-evidenced checks
print("\n== D  exact re-check of floating-point clauses cited as certified ==")


def hist_laws(perm, nV, nH, steps):
    """next-step laws per history (x0..xk) under the uniform prior (primitive_probes.py conditionals)."""
    hn = defaultdict(lambda: defaultdict(F))
    for xs, hs, p in runs(perm, nV, nH, [F(1, nV * nH)] * (nV * nH), steps):
        for k in range(1, steps + 1):
            hn[xs[:k]][xs[k]] += p
    return hn


def gap_and_istar(hn, nV):
    """(max TV gap between endpoint-sharing histories of length >= 2, max over orders of I(X_<k;X_{k+1}|X_k))."""
    best = F(0)
    per = defaultdict(L)
    groups = defaultdict(list)
    for h in hn:
        if len(h) >= 2:
            groups[(len(h), h[-1])].append(h)
    for (Lh, c), hs in groups.items():
        W = sum(sum(hn[h].values()) for h in hs)
        bar = {v: sum(hn[h][v] for h in hs) / W for v in range(nV)}
        for i, a in enumerate(hs):
            na = sum(hn[a].values())
            P = {v: hn[a][v] / na for v in range(nV)}
            for v in range(nV):
                if P[v]:
                    per[Lh] = per[Lh] + L.log2(P[v] / bar[v]).scale(na * P[v])
            for b in hs[i + 1:]:
                nb = sum(hn[b].values())
                best = max(best, sum(abs(P[v] - hn[b][v] / nb) for v in range(nV)) / 2)
    istar = L()
    for v in per.values():
        if (v - istar).sign() > 0:
            istar = v
    return best, istar


def istar_h3(perm, nV, nH):
    """I* at horizon 3: max over t in {1, 2} of I(X_<t; X_>t | X_t), uniform prior, exact."""
    best = L()
    rs = runs(perm, nV, nH, [F(1, nV * nH)] * (nV * nH), 3)
    for t in (1, 2):
        j = defaultdict(F)
        for xs, hs, p in rs:
            j[(xs[:t], xs[t], xs[t + 1:])] += p
        v = cmi(j)
        if (v - best).sign() > 0:
            best = v
    return best


for nV, nH in [(2, 2), (2, 3), (3, 2), (2, 4)]:
    cap = L.log2(nH)
    n = ngap = sat = viol = disagree = viol_ctl = differ = 0
    for perm in permutations(range(nV * nH)):
        n += 1
        g, I = gap_and_istar(hist_laws(perm, nV, nH, 3), nV)      # I = max_k M_k (per order)
        disagree += (g > 0) != (not I.is_zero())
        if g == 0:
            continue
        ngap += 1
        s = (cap - I).sign()
        viol += s < 0
        sat += s == 0
        viol_ctl += (L({2: F(1, 2)}) - I).sign() < 0
        if (nV, nH) != (2, 4):
            differ += not (istar_h3(perm, nV, nH) - I).is_zero()
    tag = f"({nV},{nH})"
    check(f"D1 primitive_probes (B) {tag}: max_k M_k <= log2|C_H| on all {ngap} gap realizations, exactly", viol == 0,
          f"{sat} saturate exactly")
    check(f"D1c CONTROL (must fail) {tag}: with the bound replaced by 1/2 bit it is violated", viol_ctl > 0,
          f"{viol_ctl} violations")
    if (nV, nH) != (2, 4):
        check(f"D1i {tag}: max_k M_k equals I* = max_t I(X_<t;X_>t|X_t) (horizon 3) on all {ngap} gap realizations, exactly",
              differ == 0)
        check(f"D2 primitive_probes (C) {tag}: gap > 0 iff max_k M_k > 0 on all {n} bijections, exactly", disagree == 0)
    if (nV, nH) in [(2, 2), (3, 2)]:
        check(f"D3 saturation max_k M_k = log2|C_H| attained {tag}, exactly", sat > 0)

for nV, nH in [(2, 2), (2, 3), (3, 2)]:
    ok = ok_ctl = 0
    n = 0
    for perm in permutations(range(nV * nH)):
        n += 1
        rs = runs(perm, nV, nH, [F(1, nV * nH)] * (nV * nH), 3)
        jm, jh = defaultdict(F), defaultdict(F)
        for xs, hs, p in rs:
            jm[(xs[:2], xs[2], xs[3])] += p
            jh[(xs[:2], xs[2], hs[2])] += p
        M, IXH = cmi(jm), cmi(jh)
        ok += (IXH - M).sign() >= 0 and (L.log2(nH) - IXH).sign() >= 0
        ok_ctl += (IXH - M).sign() >= 0 and (L.log2(nH) + L({2: F(-1, 2)}) - IXH).sign() >= 0
    check(f"D4 memory_probes (c) ({nV},{nH}): M_2 <= I(X_<2;H_2|X_2) <= log2|C_H| on {ok}/{n}, exactly", ok == n)
    check(f"D4c CONTROL (must fail) ({nV},{nH}): with capacity log2|C_H| - 1/2 some realization violates (c)",
          ok_ctl < n, f"{n - ok_ctl} violations")

K = 3
for nV, nH in [(2, 2), (2, 3), (3, 2)]:
    states = [(x, h) for x in range(nV) for h in range(nH)]
    priors = [{h: F(1, nH) for h in range(nH)}, {h: F(h + 1, sum(range(1, nH + 1))) for h in range(nH)}]
    laws = set()
    for perm in permutations(states):
        phi = dict(zip(states, perm))
        for mu in priors:
            law = defaultdict(F)
            for h in range(nH):
                cx, ch, tr = 0, h, []
                for _ in range(K):
                    cx, ch = phi[(cx, ch)]
                    tr.append(cx)
                law[tuple(tr)] += mu[h]
            laws.add(tuple(sorted(law.items())))
    ok = ok_ctl = 0
    for law in laws:
        good = good_ctl = True
        for t in range(1, K):
            joint = defaultdict(F)
            tails = set()
            for tl, p in law:
                joint[(tl[:t - 1], tl[t - 1], tl[t:])] += p
                tails.add(tl[t:])
            good &= (L.log2(len(tails)) - cmi(joint)).sign() >= 0
            good_ctl &= (L.log2(len(tails)) + L({2: F(-1, 2)}) - cmi(joint)).sign() >= 0
        ok += good
        ok_ctl += good_ctl
    check(f"D5 purification_probes (6) ({nV},{nH}): log2 #tails_t >= I(X_<t;X_>t|X_t) on {ok}/{len(laws)} laws, exactly",
          ok == len(laws))
    check(f"D5c CONTROL (must fail) ({nV},{nH}): with the floor log2 #tails_t - 1/2 some law violates it",
          ok_ctl < len(laws), f"{len(laws) - ok_ctl} violations")
check("D6 CONTROL (must fire): the exact sign test separates log2 3 from 1.585 = 317/200",
      L.log2(3).sign() > 0 and (L.log2(3) - L({2: F(317, 200)})).sign() < 0)

print("\nsc38_exact:", "ALL CHECKS PASS" if not FAIL else f"{len(FAIL)} FAILURE(S): {FAIL}")
sys.exit(1 if FAIL else 0)
