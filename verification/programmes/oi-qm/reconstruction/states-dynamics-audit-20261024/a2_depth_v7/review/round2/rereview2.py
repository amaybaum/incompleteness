"""Second independent re-review engine for #911 a2_depth_v7 at 61d90c4e.

Own code; imports nothing from the author's checker or the first reviewer.
Usage: python3 -I -B rereview2.py <result.json>
All checks exact (Fraction / integer) unless labelled NUMERIC.
"""
import sys, json, random
from fractions import Fraction as F
from itertools import product
from math import log

Q45 = F(4, 5)
res = json.load(open(sys.argv[1]))
fails = []


def ok(cond, msg):
    print(('PASS ' if cond else 'FAIL ') + msg)
    if not cond:
        fails.append(msg)


def tv(p, q):
    keys = set(p) | set(q)
    return sum(abs(p.get(k, 0) - q.get(k, 0)) for k in keys) / 2


def quantum_law(h):
    """Joint law of the h-read outcome record (agreement-bit coordinates)."""
    return {r: F(1) * eval_q(r) for r in product((1, 0), repeat=h)}


def eval_q(r):
    x = F(1)
    for g in r:
        x *= Q45 if g else 1 - Q45
    return x


# ---------------------------------------------------------------- 1. distance formula and depths
for B in range(1, 301):
    K = 1 << B
    k = min(range(K + 1), key=lambda j: abs(F(j, K) - Q45)) if B <= 12 else None
    # closed-form nearest without scanning for large B
    lo = (4 * K) // 5
    d = min(abs(F(lo, K) - Q45), abs(F(lo + 1, K) - Q45))
    if k is not None:
        ok_small = abs(F(k, K) - Q45) == d
        if not ok_small:
            fails.append('scan B=%d' % B)
    r = pow(2, B + 2, 5)
    closed = F(min(r, 5 - r), 5) / K
    if d != closed or d != F(2 if B % 2 else 1, 5 * K):
        fails.append('dist B=%d' % B)
ok(not any(f.startswith('dist') or f.startswith('scan') for f in fails),
   'dist(4/5,2^-B Z) = 2^-B*(2/5 odd, 1/5 even), B=1..300, residue form 2^(B+2) mod 5')

d24 = F(1, 5 * 2 ** 24)
c = d24 ** 2 / 4
h_rule = 1
# least h with (h-1)*c > 1, solved directly
h_rule = (1 / c).numerator // (1 / c).denominator + 2 if (1 / c).denominator == 1 else None
ok((h_rule - 1) * c > 1 and (h_rule - 2) * c <= 1 and h_rule == 28147497671065602
   == res['class_statement']['B24_depth_certified_T_above_half'],
   'B=24 class depth 28147497671065602 is least h with (h-1)d^2/4>1')
# NUMERIC (informational): the stronger 1-(1-c)^(h-1) form crosses 1/2 earlier
h_strong = 1 + log(2) / float(c)
print('INFO NUMERIC: 1-(1-c)^(h-1)>1/2 from h ~ %.4e (rule-specific depth, not minimal TV depth)' % h_strong)

dA, dB = F(res['controller']['dA']), F(res['controller']['dB'])


def S_of(h):
    na, nb = h // 2, (h + 1) // 2      # read 1 is B-type (reset X, read a)
    return (na * dA ** 2 + nb * dB ** 2) / 4


for lvl, key in ((F(1, 10), '1/10'), (F(1, 2), '1/2'), (F(9, 10), '9/10')):
    need = lvl / (1 - lvl)
    # direct: solve with integer search from a float guess then exact adjust
    h = int(float(need) / float((dA ** 2 + dB ** 2) / 8)) - 5
    while S_of(h) <= need:
        h += 1
    while S_of(h - 1) > need:
        h -= 1
    ok(h == res['certified_depth_lower_bound_exceeds'][key] and S_of(h) / (1 + S_of(h)) > lvl
       and S_of(h - 1) / (1 + S_of(h - 1)) <= lvl, 'certified depth %s = %d minimal' % (key, h))
ok(int(F(1, 10) / d24) == 8388608 == res['class_statement'][
    'B24_max_depth_coupling_T_at_most_tenth_nearest_dyadic_every_read'], 'coupling depth 8388608')

# ---------------------------------------------------------------- 2. Hellinger constant, exact proof check
# Claim: for Bernoulli p,q, H^2 = 1 - sqrt(pq) - sqrt((1-p)(1-q)) >= (p-q)^2/4.
# Proof: 2H^2 = (sqrt p - sqrt q)^2 + (sqrt(1-p) - sqrt(1-q))^2 and |p-q| = |sqrt p - sqrt q|(sqrt p + sqrt q)
# <= 2|sqrt p - sqrt q|, same for 1-p,1-q; so 2H^2 >= d^2/2.  Symbolic check of the identity:
try:
    import sympy as sp
    p, q = sp.symbols('p q', positive=True)
    lhs = (sp.sqrt(p) - sp.sqrt(q)) ** 2 + (sp.sqrt(1 - p) - sp.sqrt(1 - q)) ** 2
    rhs = 2 * (1 - sp.sqrt(p) * sp.sqrt(q) - sp.sqrt(1 - p) * sp.sqrt(1 - q))
    ok(sp.simplify(sp.expand(lhs - rhs)) == 0, 'sympy: 2H^2 = sum of squared root differences (Bernoulli)')
except ImportError:
    print('SKIP sympy')

# ---------------------------------------------------------------- 3. adaptive class members, joint-law checks
def member_law(h, B, kfun, p1):
    """Joint record law; read 1 has unconstrained prob p1 of agreement; read t>=2 agrees with
    probability kfun(t, past)/2^b(t,past) where b<=B: the response is a function of that slot's
    fresh block and the public record only."""
    law = {}
    cond = {}

    def walk(t, past, m):
        if t > h:
            law[past] = m
            return
        if t == 1:
            pr = p1
        else:
            k, b = kfun(t, past)
            pr = F(k, 1 << b)
        cond[past] = pr
        walk(t + 1, past + (1,), m * pr)
        walk(t + 1, past + (0,), m * (1 - pr))
    walk(1, (), F(1))
    return law, cond


def isqrt_hi(x, bits=200):
    from math import isqrt
    s = 1 << bits
    n = isqrt(x.numerator * s * s // x.denominator)
    while F(n, s) ** 2 < x:
        n += 1
    return F(n, s)


def isqrt_lo(x, bits=200):
    from math import isqrt
    s = 1 << bits
    n = isqrt(x.numerator * s * s // x.denominator)
    while n > 0 and F(n, s) ** 2 > x:
        n -= 1
    return F(n, s)


rng = random.Random(911)
nm = 0
all_dyadic = all_lower = all_upper = all_bc = True
for trial in range(40):
    B = rng.choice([2, 3, 4, 5, 6])
    h = rng.choice([3, 4, 5, 6, 7, 8])
    table = {}

    def kfun(t, past, B=B, table=table):
        if (t, past) not in table:
            b = rng.randint(1, B)
            K = 1 << b
            base = (4 * K) // 5
            table[t, past] = (min(K, max(0, base + rng.choice([-1, 0, 0, 1, 1, 2]))), b)
        return table[t, past]
    p1 = rng.choice([Q45, F(1, 3), F(13, 16), F(4, 5) + F(1, 10 ** 6)])
    law, cond = member_law(h, B, kfun, p1)
    ql = quantum_law(h)
    T = tv(law, ql)
    dist = F(2 if B % 2 else 1, 5 * (1 << B))
    # (i) conditional laws after read 1 in 2^-B Z
    all_dyadic &= all((pr * (1 << B)).denominator == 1 for past, pr in cond.items() if len(past) >= 1)
    # (ii) joint-law lower bound from chain rule: T >= 1-(1-dist^2/4)^(h-1) >= S/(1+S)
    S = (h - 1) * dist ** 2 / 4
    all_lower &= T >= 1 - (1 - dist ** 2 / 4) ** (h - 1) >= S / (1 + S)
    # (iii) joint-law upper bound from sequential coupling: T <= sum_t sup_past |cond - 4/5|
    sup = [max(abs(pr - Q45) for past, pr in cond.items() if len(past) == t - 1) for t in range(1, h + 1)]
    all_upper &= T <= sum(sup)
    # (iv) certified chain rule on the joint law: BC_joint <= prod_t sup_past BC_t (interval enclosure)
    bc_joint_lo = sum(isqrt_lo(law[r] * ql[r]) for r in ql)
    bct = []
    for t in range(1, h + 1):
        bct.append(max(isqrt_hi(pr * Q45) + isqrt_hi((1 - pr) * (1 - Q45))
                       for past, pr in cond.items() if len(past) == t - 1))
    prod_hi = F(1)
    for x in bct:
        prod_hi *= x
    bc_joint_hi = sum(isqrt_hi(law[r] * ql[r]) for r in ql)
    all_bc &= bc_joint_lo <= prod_hi and T >= 1 - bc_joint_hi
    nm += 1
ok(all_dyadic, '%d random adaptive class members: every conditional after read 1 in 2^-B Z' % nm)
ok(all_lower, 'joint-record TV >= 1-(1-dist^2/4)^(h-1) >= S/(1+S) for every member (exact)')
ok(all_upper, 'joint-record TV <= sum_t sup_past d_t (sequential coupling) for every member (exact)')
ok(all_bc, 'joint BC <= prod sup_past BC_t and TV >= 1-BC_joint (certified 2^-200 enclosures)')

# negative control: an adaptive member whose read-2 law depends on a retained seed bit leaves 2^-B Z
# (B=2: carrier after read 1 may read the read-1 block; conditional on public agree1 not dyadic)
# realised below by the retained-seed sampler.

# ---------------------------------------------------------------- 4. retained-seed counterexample
def rs_records(B, h):
    """Own brute force: seed integer k of N=B*h bits, decision at read t uses the top tB bits:
    agree iff prefix/2^(tB) < split of the current exact quantum interval."""
    N = B * h
    law = {}
    gap = F(0)       # coupling mass where source record != exact-decoder record of U in the cell
    for k in range(1 << N):
        lo, hi, rec = F(0), F(1), []
        for t in range(1, h + 1):
            m = lo + Q45 * (hi - lo)
            pre = k >> (N - t * B)
            g = 1 if pre * m.denominator < m.numerator * (1 << (t * B)) else 0
            rec.append(g)
            lo, hi = (lo, m) if g else (m, hi)
        rec = tuple(rec)
        law[rec] = law.get(rec, 0) + 1
        # U uniform on cell [k/2^N,(k+1)/2^N): exact decoder record is rec iff U in [lo,hi)
        a, b = F(k, 1 << N), F(k + 1, 1 << N)
        inside = max(F(0), min(b, hi) - max(a, lo))
        gap += (b - a) - inside
    return {r: F(v, 1 << N) for r, v in law.items()}, gap


for B in (2, 3, 4):
    law, _ = rs_records(B, 2)
    p1 = law.get((1, 1), 0) + law.get((1, 0), 0)
    cond = law[(1, 1)] / p1
    want = {2: '11/16', 3: '41/56', 4: '41/52'}[B]
    ok(str(cond) == want == res['class_statement']['limiting_counterexample_retained_seed_reset']['B%d' % B][
        'conditional_agree2_given_agree1'] and (cond * (1 << B)).denominator != 1,
       'retained-seed B=%d P(agree2|agree1)=%s, outside 2^-B Z' % (B, cond))

ex = res['class_statement']['limiting_counterexample_retained_seed_reset']['B4_tv_exact_h1_to_5']
for h in range(1, 6):
    law, gap = rs_records(4, h)
    T = tv(law, quantum_law(h))
    ub = sum(F(2 ** (t - 1), 2 ** (4 * t)) for t in range(1, h + 1))
    ok(str(T) == ex[str(h)] and T <= gap <= ub <= F(1, 14),
       'B=4 h=%d joint TV=%s = result; TV <= P(coupled records differ)=%s <= union %s <= 1/14'
       % (h, T, gap, ub))
for B, H in ((2, 8), (3, 6)):
    for h in range(1, H + 1):
        law, gap = rs_records(B, h)
        T = tv(law, quantum_law(h))
        ub = sum(F(2 ** (t - 1), 2 ** (B * t)) for t in range(1, h + 1))
        if not (T <= gap <= ub <= F(1, 2 ** B - 2)):
            fails.append('rs B=%d h=%d' % (B, h))
    ok(not any(f.startswith('rs B=%d' % B) for f in fails),
       'B=%d h=1..%d: joint TV <= coupling gap <= partial union sum <= 1/(2^B-2)' % (B, H))
ok(all(sum(F(2 ** (t - 1), 2 ** (B * t)) for t in range(1, 400)) < F(1, 2 ** B - 2) for B in (2, 3, 4, 24)),
   'partial union sums < 1/(2^B-2); geometric series 2^-B/(1-2^(1-B)) = 1/(2^B-2) exactly')
ok(all(F(1, 1 << B) / (1 - F(2, 1 << B)) == F(1, (1 << B) - 2) for B in range(2, 60)),
   'closed form of the infinite union sum, B=2..59')

print('FAILS:', fails)
sys.exit(1 if fails else 0)
