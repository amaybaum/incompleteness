"""P2 (generic exact check; not an OI mechanism). #1059 re-assessment, ASSESS-1059.md §4.3.

Claims checked, on generic stabilizer states only:
 (a) Enumerating all n-qubit stabilizer states for n = 1, 2, 3 by closure of |0...0> under
     H, S, CNOT (exact Gaussian-integer arithmetic, global phase and norm removed) gives
     6, 60, 1080 states (control: the known counts), and every one has computational-basis
     amplitude moduli that are equal on a support of size 2^k (so |amp| = 2^{-k/2}).
 (b) Countercontrol: f(u) = u^2 + u^2 * prod_{k=0..3} (u^2 - 2^{-k})^2 satisfies f >= 0 on
     [0,1], f(0) = 0, f != u^2, and sum_i f(|psi_i|) = 1 exactly on every stabilizer state
     with n <= 3.  So agreement at stabilizer scope (all modulus-only normalisations)
     fixes the readout only at the points 2^{-k/2}; it does not select f(u) = u^2.
 (d) Mutation control: removing the k = 3 factor breaks (b) on an 8-element support.
 (c) Control that (b) is not vacuous: on the non-stabilizer state (cos pi/8, sin pi/8),
     sum f != 1 and f(cos pi/8) != cos^2 pi/8.
Exit status 0 iff all pass.
"""
import sys
from math import gcd
import sympy as sp

fails = []
def need(cond, msg):
    if not cond:
        fails.append(msg)

# Gaussian integers as (a, b) = a + b i
def gadd(x, y): return (x[0] + y[0], x[1] + y[1])
def gsub(x, y): return (x[0] - y[0], x[1] - y[1])
def gmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def gnorm(x): return x[0] * x[0] + x[1] * x[1]
def gdivexact(x, y):
    n = gnorm(y); c = (y[0], -y[1]); t = gmul(x, c)
    assert t[0] % n == 0 and t[1] % n == 0
    return (t[0] // n, t[1] // n)
def gdiv_ok(x, y):
    n = gnorm(y); t = gmul(x, (y[0], -y[1]))
    return t[0] % n == 0 and t[1] % n == 0
UNITS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ONEI = (1, 1)

def canon(v):
    v = list(v)
    # divide out common rational integer factor
    g = 0
    for a, b in v:
        g = gcd(g, gcd(abs(a), abs(b)))
    v = [(a // g, b // g) for a, b in v]
    # divide out common (1+i) factors
    while all(gdiv_ok(x, ONEI) for x in v):
        v = [gdivexact(x, ONEI) for x in v]
    first = next(x for x in v if x != (0, 0))
    # fix the unit so the first nonzero entry is a positive-real-leaning representative
    best = None
    for u in UNITS:
        w = tuple(gmul(x, u) for x in v)
        f = next(x for x in w if x != (0, 0))
        if f[0] > 0 and f[1] >= 0:
            if best is None or w < best:
                best = w
    return best

def apply_H(v, q, n):
    w = list(v)
    for idx in range(2 ** n):
        if not (idx >> q) & 1:
            j = idx | (1 << q)
            w[idx] = gadd(v[idx], v[j]); w[j] = gsub(v[idx], v[j])
    return tuple(w)
def apply_S(v, q, n):
    return tuple(gmul(x, (0, 1)) if (idx >> q) & 1 else x for idx, x in enumerate(v))
def apply_CX(v, c, t, n):
    w = list(v)
    for idx in range(2 ** n):
        if (idx >> c) & 1:
            w[idx] = v[idx ^ (1 << t)]
    return tuple(w)

def stab_states(n):
    start = canon(tuple([(1, 0)] + [(0, 0)] * (2 ** n - 1)))
    seen = {start}; frontier = [start]
    while frontier:
        nxt = []
        for v in frontier:
            outs = []
            for q in range(n):
                outs.append(apply_H(v, q, n)); outs.append(apply_S(v, q, n))
            for c in range(n):
                for t in range(n):
                    if c != t:
                        outs.append(apply_CX(v, c, t, n))
            for w in outs:
                w = canon(w)
                if w not in seen:
                    seen.add(w); nxt.append(w)
        frontier = nxt
    return seen

u = sp.symbols('u', nonnegative=True)
f = u**2 + u**2 * sp.prod([(u**2 - sp.Rational(1, 2**k))**2 for k in range(4)])
expected = {1: 6, 2: 60, 3: 1080}
for n in (1, 2, 3):
    S = stab_states(n)
    need(len(S) == expected[n], f"(a) count n={n}: {len(S)}")
    for v in S:
        norms = [gnorm(x) for x in v]
        supp = [m for m in norms if m]
        k = len(supp)
        need(len(set(supp)) == 1 and k & (k - 1) == 0, f"(a) uniform-modulus support n={n} {v}")
        total = sum(sp.Rational(m, sum(norms)) for m in norms)   # |amp|^2 profile
        need(total == 1, "(a) profile normalised")
        # modulus of each amplitude = sqrt(m / sum(norms))
        sf = sum(f.subs(u, sp.sqrt(sp.Rational(m, sum(norms)))) for m in norms)
        need(sp.nsimplify(sp.expand(sf)) == 1, f"(b) f normalises stabilizer state n={n}")
    print(f"(a)/(b) n={n}: {len(S)} stabilizer states; uniform-modulus supports; f-normalised:", not fails)

# (b) f >= 0 on [0,1], f(0)=0, f != u^2
need(f.subs(u, 0) == 0, "(b) f(0)=0")
need(sp.expand(f - u**2) != 0, "(b) f != u^2")
need(sp.expand(f - u**2).as_poly(u).LC() > 0, "(b) extra term is a positive multiple of a square times u^2")
# (c) non-stabilizer control
c, s = sp.cos(sp.pi / 8), sp.sin(sp.pi / 8)
tot = sp.nsimplify(sp.simplify(f.subs(u, c) + f.subs(u, s)))
need(sp.simplify(tot - 1) != 0, "(c) f fails on cos/sin pi/8")
need(sp.simplify(f.subs(u, c) - c**2) != 0, "(c) f(cos pi/8) != cos^2 pi/8")
print("(c) non-stabilizer control: sum f =", sp.N(tot, 20), "(!= 1):", not fails)

# (d) mutation control: dropping the k = 3 factor must break normalisation on 3-qubit states
#     with an 8-element support (moduli 2^{-3/2}); shows (b)'s check is sensitive.
f_mut = u**2 + u**2 * sp.prod([(u**2 - sp.Rational(1, 2**k))**2 for k in range(3)])
v8 = 8 * f_mut.subs(u, sp.sqrt(sp.Rational(1, 8)))
need(sp.nsimplify(v8) != 1, "(d) mutation f_mut must fail on uniform 8-support")
print("(d) mutation control: 8*f_mut(2^{-3/2}) =", v8, "(!= 1):", not fails)

if fails:
    print("FAIL:", fails[:10])
    sys.exit(1)
print("ALL P2 CHECKS PASS")
