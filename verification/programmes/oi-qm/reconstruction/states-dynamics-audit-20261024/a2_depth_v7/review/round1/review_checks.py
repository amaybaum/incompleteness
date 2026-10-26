"""Independent reviewer engine for a2_depth_v7 (draft #911). Imports nothing from the author.

Rebuilds the M=16,W=16,B=24 six-face grid and its CDF counts from the a2_efficiency_v6
construction, derives the agreement laws, exact T(h), the certified bracket and depths,
the class distance, and the sampler-level claims. Usage: python3 -I -B review_checks.py RESULT_JSON
"""
import sys, json, hashlib
from fractions import Fraction as F
from math import isqrt, comb
from itertools import product

OUT = []
def say(*a):
    s = ' '.join(str(x) for x in a); OUT.append(s); print(s, flush=True)
def need(c, msg):
    if not c: raise SystemExit('CONTROL FAILED: ' + msg)

M, W, BB = 16, 16, 24
K = 1 << BB
q = F(4, 5)

# ---- grid, in the v6 enumeration order (face, sign, u, v) ----
Z = []
for face in range(3):
    free = [j for j in range(3) if j != face]
    for s in (-1, 1):
        for u in range(-M + 1, M, 2):
            for v in range(-M + 1, M, 2):
                z = [0, 0, 0]; z[face] = s * M; z[free[0]] = u; z[free[1]] = v
                Z.append(tuple(z))
need(len(Z) == 1536 == len(set(Z)), 'grid size')
IDX = {z: i for i, z in enumerate(Z)}
ANTI = [IDX[tuple(-x for x in z)] for z in Z]

def counts_pos(num, den):
    """num: integer direction vector, den: its denominator; first nonzero coord positive."""
    fac = (1 << W) * M ** 3
    w = []
    for z in Z:
        a = sum(x * y for x, y in zip(num, z)); qq = sum(x * x for x in z)
        # floor(2^W M^3 (n.z)_+ / (z.z)^2) with n.z = a/den
        w.append(0 if a <= 0 else (fac * a) // (den * qq * qq))
    tot = sum(w); cum = 0; last = 0; c = []
    for x in w:
        cum += x; cut = K * cum // tot; c.append(cut - last); last = cut
    need(last == K and min(c) >= 0, 'CDF mass')
    return c

def counts(vec):
    """vec: tuple of Fractions, unit. Negative directions = antipodal pushforward (v6 rule)."""
    from math import lcm
    first = next(x for x in vec if x)
    if first < 0:
        c = counts(tuple(-x for x in vec)); return [c[ANTI[i]] for i in range(len(Z))]
    den = lcm(*(x.denominator for x in vec)); num = tuple(int(x * den) for x in vec)
    return counts_pos(num, den)

AX = {'X': (F(1), F(0), F(0)), 'Y': (F(0), F(1), F(0)), 'Z': (F(0), F(0), F(1)),
      'a': (F(3, 5), F(4, 5), F(0))}
BASE = dict(AX, p=(F(2, 3), F(-2, 3), F(1, 3)), q=(F(2, 3), F(-2, 3), F(-1, 3)))
PREP = {}
for nm, n in BASE.items():
    for s, sg in ((1, '+'), (-1, '-')):
        PREP[nm + sg] = tuple(s * x for x in n)
CNT = {nm: counts(n) for nm, n in PREP.items()}
dig = hashlib.sha256(json.dumps({k: tuple(v) for k, v in CNT.items()}, sort_keys=True,
                                separators=(',', ':')).encode()).hexdigest()
need(dig == '0637f0089fc5ce666d17ddaf828cc98bf317d46e3ea3cd22851bc21eb893a6a1', 'v6 digest')
say('grid digest matches v6:', dig)

def resp(axis, z):  # + iff axis.z >= 0 (zero -> +)
    d = sum(a * b for a, b in zip(AX[axis], z))
    return (1 if d >= 0 else -1), (d == 0)

def agree_mass(pole_name, pole_sign, axis):
    c = CNT[pole_name]; tot = 0; zeros = 0
    for ci, z in zip(c, Z):
        r, zr = resp(axis, z)
        if ci and zr: zeros += ci
        if r == pole_sign: tot += ci
    return F(tot, K), zeros

A_p, zA1 = agree_mass('a+', 1, 'X'); A_m, zA2 = agree_mass('a-', -1, 'X')
B_p, zB1 = agree_mass('X+', 1, 'a'); B_m, zB2 = agree_mass('X-', -1, 'a')
say('A(+)=', A_p, ' A(-)=', A_m, ' B(+)=', B_p, ' B(-)=', B_m, ' zero-response mass', zA1 + zA2 + zB1 + zB2)
need(A_p == A_m == F(13426743, K) and B_p == B_m == F(13424725, K), 'A,B values and sign symmetry')
need(zA1 + zA2 + zB1 + zB2 == 0, 'no zero responses')
# quantum controls: agreement 4/5 for both pairs
need((1 + F(3, 5)) / 2 == q, 'quantum agreement 4/5')
Aq, Bq = A_p, B_p
dA, dB = abs(Aq - q), abs(Bq - q)
say('dA=', dA, ' dB=', dB, ' kappa=6419131/419430400 ok:', dA <= F(6419131, 419430400) and dB <= F(6419131, 419430400))
need(dA == F(24851, 83886080) and dB == F(14761, 83886080), 'dA dB')

# ---- literal record-level engine for small h (no product assumption) ----
def literal_tv(h):
    """Enumerate records as outcome sequences; source law propagated through the controller's
    reset rule (carrier law = CNT[reset ray], response from carrier), quantum law via Born rule."""
    axes = ['a' if t % 2 == 0 else 'X' for t in range(h)]
    # quantum: P(outcome s | pole n) = (1 + s * axis.n)/2
    def qp(axis, pole, s):
        return (1 + s * sum(x * y for x, y in zip(AX[axis], pole))) / 2
    def sp(axis, pole_name, s):
        c = CNT[pole_name]
        return F(sum(ci for ci, z in zip(c, Z) if resp(axis, z)[0] == s), K)
    cache = {}
    def spc(axis, pn, s):
        k = (axis, pn, s)
        if k not in cache: cache[k] = sp(axis, pn, s)
        return cache[k]
    tv = F(0)
    for rec in product((1, -1), repeat=h):
        pn, pole = 'X+', AX['X']; P = F(1); Qv = F(1)
        for t, s in enumerate(rec):
            ax = axes[t]
            P *= spc(ax, pn, s); Qv *= qp(ax, pole, s)
            pn = ax + ('+' if s == 1 else '-'); pole = tuple(s * x for x in AX[ax])
        tv += abs(P - Qv)
    return tv / 2

# ---- product engine on agreement bits, exact integers ----
def params(h):  # t=1 is B (read a after X), then A, B, ...
    return [Bq if t % 2 == 0 else Aq for t in range(h)]

def tv_product(h):
    nB = (h + 1) // 2; nA = h // 2
    KA, KB = Aq.numerator * (K // Aq.denominator), Bq.numerator * (K // Bq.denominator)
    # integer weights with common denominator K^h * 5^h
    PA = [comb(nA, i) * KA ** i * (K - KA) ** (nA - i) for i in range(nA + 1)]
    PB = [comb(nB, j) * KB ** j * (K - KB) ** (nB - j) for j in range(nB + 1)]
    QA = [comb(nA, i) * 4 ** i for i in range(nA + 1)]
    QB = [comb(nB, j) * 4 ** j for j in range(nB + 1)]
    s5, sK = 5 ** h, K ** h
    tot = 0
    for i in range(nA + 1):
        a, b = s5 * PA[i], sK * QA[i]
        for j in range(nB + 1):
            tot += abs(a * PB[j] - b * QB[j])
    return F(tot, 2 * sK * s5)

def tv_product_fast(h):
    """Same quantity; uses monotone likelihood ratio in j for each i (prefix sums)."""
    nB = (h + 1) // 2; nA = h // 2
    KA, KB = Aq.numerator * (K // Aq.denominator), Bq.numerator * (K // Bq.denominator)
    PA = [comb(nA, i) * KA ** i * (K - KA) ** (nA - i) for i in range(nA + 1)]
    PB = [comb(nB, j) * KB ** j * (K - KB) ** (nB - j) for j in range(nB + 1)]
    QA = [comb(nA, i) * 4 ** i for i in range(nA + 1)]
    QB = [comb(nB, j) * 4 ** j for j in range(nB + 1)]
    s5, sK = 5 ** h, K ** h
    # P_j/Q_j (for B part) ratio: (KB/(4K/5))^j ((K-KB)/(K/5))^(nB-j); KB<4K/5 so decreasing in j
    need(5 * KB != 4 * K, 'B differs from 4/5')
    inc = 5 * KB > 4 * K  # P_j/Q_j increasing in j iff B > 4/5
    sPB = [0]; sQB = [0]
    for j in range(nB + 1): sPB.append(sPB[-1] + PB[j]); sQB.append(sQB[-1] + QB[j])
    tot = 0
    for i in range(nA + 1):
        a, b = s5 * PA[i], sK * QA[i]
        # f(j)=a*PB[j]-b*QB[j]; sign(f) = sign(ratio_j - b/a), ratio monotone in j
        pos_at = (lambda j: a * PB[j] - b * QB[j] >= 0)
        lo, hi = 0, nB + 1
        while lo < hi:   # first j where the predicate (j in upper block) holds
            mid = (lo + hi) // 2
            if pos_at(mid) == inc: hi = mid
            else: lo = mid + 1
        j0 = lo  # j<j0: lower block, j>=j0: upper block
        lowP, lowQ = a * sPB[j0], b * sQB[j0]
        upP, upQ = a * (sPB[-1] - sPB[j0]), b * (sQB[-1] - sQB[j0])
        if inc: tot += (upP - upQ) + (lowQ - lowP)
        else: tot += (lowP - lowQ) + (upQ - upP)
    return F(tot, 2 * sK * s5)

def trunc(x, k=12):  # author's display convention: truncation, not rounding
    v = x.numerator * 10 ** k // x.denominator
    return '0.' + str(v).zfill(k)

res = json.load(open(sys.argv[1]))
for h in range(1, 13):
    lt = literal_tv(h) if h <= 10 else None
    tp = tv_product(h)
    tf = tv_product_fast(h)
    need(tp == tf, 'fast vs direct product engine h=%d' % h)
    if lt is not None: need(lt == tp, 'literal record engine vs product h=%d' % h)
    if h <= 4:
        need(str(tp) == res['exact_tv_h1_to_4'][str(h)], 'author exact T(%d)' % h)
    say('h=%2d T=%s%s' % (h, '%.12f' % float(tp), ('  exact ' + str(tp)) if h <= 4 else ''),
        ' literal=match' if lt is not None else '')

# compare all tabulated h with author's display and sha256
hs = list(range(1, 65)) + [128, 256, 512, 1024, 2048]
mism = []
import time
for h in hs:
    t0 = time.time(); T = tv_product_fast(h)
    row = res['exact_tv_table'][str(h)]
    disp = trunc(T)
    sha = hashlib.sha256(f'{T.numerator:x}/{T.denominator:x}'.encode()).hexdigest()  # author's hash convention
    ok_d = (disp == row['display']); ok_s = (sha == row['sha256'])
    if not (ok_d and ok_s): mism.append((h, disp, row['display'], ok_s))
    need(T < F(1, 10), 'T(%d)<1/10' % h)
    # bracket
    d = [abs(p - q) for p in params(h)]
    S = sum(x * x for x in d) / 4
    need(S / (1 + S) <= T <= sum(d), 'bracket h=%d' % h)
    if h in (64, 256, 1024, 2048): say('h=%4d T=%s sha_match=%s disp_match=%s (%.1fs)' % (h, disp, ok_s, ok_d, time.time() - t0))
say('tabulated rows checked:', len(hs), ' mismatches:', mism)
need(not mism, 'author table')
need(tv_product(3) < F(17239332625914280559, 230584300921369395200), 'T(3) below h=3 certificate')

# ---- certified depths ----
def first_depth(level):
    # S(h) > level/(1-level); S(h) = ceil(h/2) dB^2/4 + floor(h/2) dA^2/4
    thr = level / (1 - level)
    def S(h): return ((h + 1) // 2) * dB * dB / 4 + (h // 2) * dA * dA / 4
    lo, hi = 1, 1
    while S(hi) <= thr: hi *= 2
    while lo < hi:
        m = (lo + hi) // 2
        if S(m) > thr: hi = m
        else: lo = m + 1
    return lo
dep = {str(L): first_depth(L) for L in (F(1, 10), F(1, 2), F(9, 10))}
say('certified depths:', dep)
need(dep == {k: res['certified_depth_lower_bound_exceeds'][k] for k in dep}, 'author depths')

# ---- proof-step checks (symbolic) ----
import sympy as sp
p, d = sp.symbols('p d', positive=True)
# claim: 1 - BC(p,p+d) >= d^2/4 ; stronger fact: BC <= sqrt(1-d^2) (Le Cam) -> 1-BC >= d^2/2
# numeric exhaustive grid check of Hellinger bound in exact rationals via squaring
bad = 0
for P in range(1, 200):
    for D in range(1, 200 - P):
        a, b = F(P, 200), F(P + D, 200); dd = b - a
        # BC = sqrt(ab)+sqrt((1-a)(1-b)); test BC <= 1 - dd^2/4  <=> sqrt(ab) <= c - sqrt(..)
        c = 1 - dd * dd / 4
        x, y = a * b, (1 - a) * (1 - b)
        # sqrt x + sqrt y <= c  <=>  x + y + 2 sqrt(xy) <= c^2  (c>0)  <=> 4xy <= (c^2-x-y)^2 and c^2-x-y>=0
        r = c * c - x - y
        if not (r >= 0 and 4 * x * y <= r * r): bad += 1
say('Hellinger d^2/4 bound violations on 19,701 rational pairs:', bad)
need(bad == 0, 'Hellinger bound')
# 1-prod(1-x_t) >= S/(1+S): with x_t = d_t^2/4, prod(1-x_t) <= exp(-S) <= 1/(1+S)
x = sp.symbols('x', nonnegative=True)
# 1-prod(1-x_t) >= 1-exp(-S) >= S/(1+S), the last since exp(S) >= 1+S; check exp(S)(1) - (1+S) has min 0 at S=0
say('exp(S)-1-S >= 0 on S>=0 (sympy minimum):', sp.calculus.util.minimum(sp.exp(x) - 1 - x, x, sp.Interval(0, sp.oo)))
# Le Cam: BC(p,p+d)^2 <= 1-d^2  => 1-BC >= d^2/2 >= d^2/4 (symbolic identity check at sample points done above)
# Sequential version used for class members: BC(P_1:h,Q_1:h) = sum_{x<h} sqrt(P Q)(x<h) BC(P_h(.|x<h),Q_h) <= sup BC_h * BC(P_<h,Q_<h)

# ---- class distance ----
def dist(B):
    m = q * 2 ** B; k = m.numerator // m.denominator
    return min(m - k, k + 1 - m) / 2 ** B
for B in range(1, 201):
    need(dist(B) == F(2 if B % 2 else 1, 5) / 2 ** B, 'dist formula B=%d' % B)
say('dist formula holds B=1..200; proof: 2^(B+2) mod 5 = +-1 (B even), +-2 (B odd) since 4 = -1 mod 5')
dl = dist(24); say('B=24 distance', dl)
thr = 4 / (dl * dl)  # S = n*dl^2/4 > 1 <=> n > thr
say('class: n reads constrained needed for S>1: n >=', int(thr) + 1,
    '; if the first read (preparation) is unconstrained, h >=', int(thr) + 2,
    '; author:', res['class_statement']['B24_depth_certified_T_above_half'])
say('best 24-bit sampler coupling T<=1/10 through h =', int(F(1, 10) / dl))

# ---- sampler level ----
def ceil_log2(t): return (t - 1).bit_length()
def Bt(t, B0=6): return B0 + 2 * ceil_log2(t)
def nd(B):
    m = q * 2 ** B; k = m.numerator // m.denominator
    return F(k if m - k <= k + 1 - m else k + 1, 2 ** B)
def tv_bern(ps, qv=q):
    # exact TV between prod Bern(ps) and Bern(q)^h by full enumeration (h<=12) via DP over likelihood
    h = len(ps); tot = F(0)
    for rec in product((0, 1), repeat=h):
        P = F(1); Qv = F(1)
        for x, pp in zip(rec, ps):
            P *= pp if x else 1 - pp; Qv *= qv if x else 1 - qv
        tot += abs(P - Qv)
    return tot / 2
for h in (1, 2, 4, 8, 12):
    T = tv_bern([nd(Bt(t)) for t in range(1, h + 1)])
    say('growing sampler h=%d T=%s' % (h, T))
    need(T == F(1, 320), 'growing sampler 1/320')
say('fresh bits through h=12:', sum(Bt(t) for t in range(1, 13)))
# uniform bound: sum_t d_t, d_t = dist(B_t); partial sums with tail bound
s = sum(dist(Bt(t)) for t in range(1, 1 << 16))
tail = F(1, 5) * F(1, 64) * F(1, 2) ** 16  # sum_{t>2^16} 4^-ceil(log2 t)/5/64 = (1/320)*sum_{k>16} 2^(k-1)/4^k
say('growing sampler sum d_t <=', float(s + tail), '(exact limit 3/640); author bound 1/80 valid:', s + tail <= F(1, 80))
# fixed B0=6
d6 = abs(nd(6) - q)
def tv_iid(h, pp):
    tot = 0; den = 0
    pn, pd = pp.numerator, pp.denominator
    for k in range(h + 1):
        a = comb(h, k) * F(pn, pd) ** k * (1 - pp) ** (h - k)
        b = comb(h, k) * q ** k * (1 - q) ** (h - k)
        tot += abs(a - b)
    return tot / 2
for h in (12, 256, 2048):
    T = tv_iid(h, nd(6)); disp = trunc(T)
    say('fixed B0=6 h=%d T=%s author=%s' % (h, disp, res['growing_bits_sampler_control']['fixed_B0_contrast']['tv_by_h_display'][str(h)]))
say('fixed B0=6 certified T>1/2 from h =', int(4 / (d6 * d6)) + 1)
say('ALL REVIEW CONTROLS GREEN')
