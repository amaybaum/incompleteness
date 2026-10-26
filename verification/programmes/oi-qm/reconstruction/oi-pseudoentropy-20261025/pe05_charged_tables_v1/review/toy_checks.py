"""PE-02 plan review: design-only toy checks (no PE-02 experiment, no PE-01 cell recomputed).

T1  Lemma A-SIM: active m-bit observer O vs explicit passive (m+1)-bit sim(O), exact joint laws,
    on toy autonomous generators (G_lin, G_filt, G_clkfix matched/uniform, random autonomous
    generators with random non-uniform priors). Countercontrol: G_clk (must fail for some O),
    and two mutant sims (must fail).
T2  m = 0 observers: exact zero advantage at every K on bijective generators with phi-invariant
    uniform-on-support priors.
T3  G_weak_mut at K = 0 (x_0 = 0 deterministic): advantage of chi == 0.
T4  G_weak planted law Pr[X_K = 1] = K / 2^n.
T5  CA-EQ: passive record of G_clkfix (matched) equals G_clk pathwise.
T6  G_clkfix increments are not F2-affine in the seed for a fixed control sequence
    (the plan's rank method for Z presumes they are); exhaustive Z of G_clk vs G_clkfix.
T7  E code: prefix-freeness, lengths; inclusion F_E >= F_R for m <= 1.
"""
import itertools
import random
from fractions import Fraction
from math import ceil, log2, factorial

random.seed(20261026)

# ---------- generators: state (x, hid), hid an int; step(x, hid) -> (x', hid') ----------

def companion(p, n):
    cm = p & ((1 << n) - 1)
    return [(h >> 1) | ((bin(h & cm).count("1") & 1) << (n - 1)) for h in range(1 << n)]

def ell(h): return h & 1
def gfilt(h): return (h & 1) ^ ((h >> 1) & 1 & ((h >> 2) & 1))

def gen_template(n, p, kind):
    L = companion(p, n); L2 = [L[L[h]] for h in range(1 << n)]
    if kind == "lin":  s0, s1, f = L, L, ell
    elif kind == "filt": s0, s1, f = L, L, gfilt
    elif kind == "clk": s0, s1, f = L, L2, ell
    def step(x, h):
        h2 = (s1 if x else s0)[h]
        return x ^ f(h2), h2
    seeds = [((x, h), 1) for x in (0, 1) for h in range(1 << n)]
    return step, seeds

def gen_clkfix(n, p, prior):
    L = companion(p, n); L2 = [L[L[h]] for h in range(1 << n)]
    def step(x, hq):
        h, q = hq >> 1, hq & 1
        h2 = (L2 if q else L)[h]
        b = ell(h2)
        return x ^ b, (h2 << 1) | (q ^ b)
    if prior == "matched":
        seeds = [((x, (h << 1) | x), 1) for x in (0, 1) for h in range(1 << n)]
    else:
        seeds = [((x, (h << 1) | q), 1) for x in (0, 1) for h in range(1 << n) for q in (0, 1)]
    return step, seeds

def gen_random_autonomous(H):
    pi = list(range(H)); random.shuffle(pi)
    b = [random.randint(0, 1) for _ in range(H)]
    def step(x, h):
        h2 = pi[h]
        return x ^ b[h2], h2
    seeds = [((x, h), random.randint(1, 5)) for x in (0, 1) for h in range(H)]  # random non-uniform prior
    return step, seeds

# ---------- embedded observer simulation (PE-01 round order) ----------

def joint_law(step, seeds, m, rho0, rho1, a, K):
    """Return dict (v_K, x_K) -> weight for observer (rho0, rho1, a), v_0 = 0."""
    out = {}
    for (x, h), w in seeds:
        v = 0
        for _ in range(K):
            v = (rho1 if x else rho0)[v]
            x ^= a[v]
            x, h = step(x, h)
        out[(v, x)] = out.get((v, x), 0) + w
    return out

def sim_tables(m, rho0, rho1, a):
    """sim(O) as explicit passive (m+1)-bit tables; state index s = v + 2^m * A."""
    N = 1 << m
    r = [[0] * (2 * N) for _ in (0, 1)]
    for y in (0, 1):
        for A in (0, 1):
            for v in range(N):
                v2 = (rho1 if (y ^ A) else rho0)[v]
                r[y][v + N * A] = v2 + N * (A ^ a[v2])
    for y in (0, 1):
        assert sorted(r[y]) == list(range(2 * N)), "sim rho not a bijection"
    return r[0], r[1], [0] * (2 * N)

def perms(N): return [list(p) for p in itertools.permutations(range(N))]

def observers(m):
    N = 1 << m
    for r0 in perms(N):
        for r1 in perms(N):
            for a in itertools.product((0, 1), repeat=N):
                yield r0, r1, list(a)

def check_asim(name, step, seeds, mmax, Kmax, expect_hold=True, mutant=None):
    fails = 0; total = 0
    for m in range(0, mmax + 1):
        N = 1 << m
        for r0, r1, a in observers(m):
            if not any(a):
                continue  # passive: sim trivially equal; lemma is about active O
            s0, s1, sa = sim_tables(m, r0, r1, a)
            if mutant == "noA_in_rho":
                s0 = [(r0[s % N]) + N * (s // N ^ a[r0[s % N]]) for s in range(2 * N)]
                s1 = [(r1[s % N]) + N * (s // N ^ a[r1[s % N]]) for s in range(2 * N)]
            for K in range(0, Kmax + 1):
                J = joint_law(step, seeds, m, r0, r1, a, K)
                Js = joint_law(step, seeds, m + 1, s0, s1, sa, K)
                total += 1
                ok = True
                for chi in itertools.product((0, 1), repeat=N):
                    p1 = sum(w for (v, x), w in J.items() if chi[v] == x)
                    if mutant == "noA_in_chi":
                        p2 = sum(w for (s, x), w in Js.items() if chi[s % N] == x)
                    else:
                        p2 = sum(w for (s, x), w in Js.items() if (chi[s % N] ^ (s // N)) == x)
                    if p1 != p2:
                        ok = False; break
                if not ok:
                    fails += 1
    held = fails == 0
    tag = "PASS" if held == expect_hold else "UNEXPECTED"
    print("T1 %-34s cases=%6d mismatches=%6d lemma-identity-holds=%s expected=%s -> %s" % (
        name, total, fails, held, expect_hold, tag))
    return held == expect_hold

allok = True
P = {3: 0b1011, 4: 0b10011, 5: 0b100101}
# T1
for n in (3, 4):
    allok &= check_asim("G_lin n=%d" % n, *gen_template(n, P[n], "lin"), 2 if n == 3 else 1, 9)
    allok &= check_asim("G_filt n=%d" % n, *gen_template(n, P[n], "filt"), 2 if n == 3 else 1, 9)
    allok &= check_asim("G_clkfix matched n=%d" % n, *gen_clkfix(n, P[n], "matched"), 2 if n == 3 else 1, 9)
    allok &= check_asim("G_clkfix uniform n=%d" % n, *gen_clkfix(n, P[n], "uniform"), 1, 9)
for i in range(3):
    allok &= check_asim("random autonomous H=8 #%d" % i, *gen_random_autonomous(8), 2 if i == 0 else 1, 8)
allok &= check_asim("G_clk n=3 (countercontrol)", *gen_template(3, P[3], "clk"), 1, 9, expect_hold=False)
allok &= check_asim("mutant chi without A, G_lin n=3", *gen_template(3, P[3], "lin"), 1, 9,
                    expect_hold=False, mutant="noA_in_chi")
allok &= check_asim("mutant rho without A, G_filt n=3", *gen_template(3, P[3], "filt"), 1, 9,
                    expect_hold=False, mutant="noA_in_rho")

# T2: m = 0 exact zero
def adv_m0(step, seeds, a, chi, K):
    J = joint_law(step, seeds, 0, [0], [0], [a], K)
    tot = sum(J.values())
    return Fraction(sum(w for (v, x), w in J.items() if x == chi), tot) - Fraction(1, 2)

for name, (step, seeds) in [("G_lin n=4", gen_template(4, P[4], "lin")), ("G_filt n=4", gen_template(4, P[4], "filt")),
                            ("G_clk n=4", gen_template(4, P[4], "clk")), ("G_clk n=5", gen_template(5, P[5], "clk")),
                            ("G_clkfix matched n=4", gen_clkfix(4, P[4], "matched")),
                            ("G_clkfix uniform n=4", gen_clkfix(4, P[4], "uniform"))]:
    mx = max(abs(adv_m0(step, seeds, a, c, K)) for a in (0, 1) for c in (0, 1) for K in range(0, 40))
    print("T2 m=0 max |adv| over K<40, a, chi: %-22s %s" % (name, mx))
    allok &= mx == 0

# T3/T4: G_weak, G_weak_mut (x_0 = 0, h uniform)
def gen_weak(n, p, mut):
    L = companion(p, n); allones = (1 << n) - 1
    f = ell if mut else (lambda h: int(h == allones))
    def step(x, h):
        h2 = L[h]; return x ^ f(h2), h2
    return step, [((0, h), 1) for h in range(1 << n)]

n = 5
st, sd = gen_weak(n, P[5], True)
print("T3 G_weak_mut n=5: adv(chi==0) at K=0..7:", [str(adv_m0(st, sd, 0, 0, K)) for K in range(8)])
st, sd = gen_weak(n, P[5], False)
okw = all(adv_m0(st, sd, 0, 0, K) == Fraction(1, 2) - Fraction(K, 2 ** n) for K in range(1, 2 ** n))
print("T4 G_weak n=5: Pr[X_K=0]-1/2 == 1/2-K/2^n for 1<=K<=2^n-1:", okw); allok &= okw

# T5: CA-EQ
for n in (3, 4, 5):
    sc, _ = gen_template(n, P[n], "clk"); sf, _ = gen_clkfix(n, P[n], "matched")
    eq = True
    for x0 in (0, 1):
        for h0 in range(1 << n):
            x, h = x0, h0; y, hq = x0, (h0 << 1) | x0
            for _ in range(3 * (1 << n)):
                x, h = sc(x, h); y, hq = sf(y, hq)
                if x != y or h != hq >> 1:
                    eq = False
    print("T5 CA-EQ n=%d passive G_clkfix(matched) == G_clk pathwise:" % n, eq); allok &= eq

# T6: affine-ness of G_clkfix increments in h for fixed x0 (control seq irrelevant: hidden autonomous)
def increments_clkfix(n, p, x0, h, k):
    st, _ = gen_clkfix(n, p, "matched"); x, hq = x0, (h << 1) | x0; out = []
    for _ in range(k):
        x2, hq = st(x, hq); out.append(x2 ^ x); x = x2
    return out

def is_affine(fn, n):
    f0 = fn(0)
    for h1 in range(1 << n):
        for h2 in range(1 << n):
            if fn(h1) ^ fn(h2) ^ fn(h1 ^ h2) ^ f0:
                return False
    return True

n = 4
nonaff = [t for t in range(8) if not is_affine(lambda h: increments_clkfix(n, P[n], 0, h, 8)[t], n)]
print("T6 G_clkfix n=4: increments Y_t that are not F2-affine in h (x0=0), t<8:", nonaff)

def Z_exhaustive_clkfix(n, p):
    best = 0
    for k in range(1, 2 * n + 2):
        good = True
        for x0 in (0, 1):
            cnt = {}
            for h in range(1 << n):
                z = tuple(increments_clkfix(n, p, x0, h, k)); cnt[z] = cnt.get(z, 0) + 1
            if len(cnt) != 2 ** k or len(set(cnt.values())) != 1:
                good = False
        if not good:
            return best
        best = k
    return best

def Z_exhaustive_clk(n, p):
    """PE-01 definition: every fixed control sequence c_{0:k-1}, increments f(sigma_c h) jointly uniform."""
    L = companion(p, n); L2 = [L[L[h]] for h in range(1 << n)]
    best = 0
    for k in range(1, 2 * n + 2):
        for cs in itertools.product((0, 1), repeat=k):
            cnt = {}
            for h in range(1 << n):
                hh = h; z = []
                for c in cs:
                    hh = (L2 if c else L)[hh]; z.append(hh & 1)
                cnt[tuple(z)] = cnt.get(tuple(z), 0) + 1
            if len(cnt) != 2 ** k or len(set(cnt.values())) != 1:
                return best
        best = k
    return best

for n in (3, 4, 5):
    print("T6 n=%d Z(G_clk) all control sequences = %d ; Z(G_clkfix matched) exhaustive = %d" % (
        n, Z_exhaustive_clk(n, P[n]), Z_exhaustive_clkfix(n, P[n])))

# T7: E code
def gamma(x): b = bin(x)[2:]; return "0" * (len(b) - 1) + b
def lehmer(rho):
    N = len(rho); r = 0
    for i in range(N):
        d = sum(1 for j in range(i + 1, N) if rho[j] < rho[i]); r += d * factorial(N - 1 - i)
    return r
def E(m, r0, r1, a, chi, K):
    N = 1 << m; L = ceil(log2(factorial(N))) if m > 0 else 0
    f = lambda r: format(lehmer(r), "0%db" % L) if L else ""
    return gamma(m + 1) + f(r0) + f(r1) + "".join(map(str, a)) + "".join(map(str, chi)) + gamma(K + 1)
words = set()
for m in (0, 1, 2):
    N = 1 << m
    for r0, r1, a in observers(m):
        for chi in itertools.product((0, 1), repeat=N):
            for K in (1, 2, 3, 7, 8, 30, 63):
                words.add(E(m, r0, r1, a, list(chi), K))
ws = sorted(words)
pf = all(not ws[i + 1].startswith(ws[i]) for i in range(len(ws) - 1))
print("T7 E prefix-free on %d codewords (m<=2, sampled K): %s" % (len(ws), pf)); allok &= pf
c = lambda K: ceil(log2(K + 1)); g = lambda x: 2 * (x.bit_length() - 1) + 1
TR = lambda m, K: 2 * m * 2 ** m + 2 ** m + 2 ** (m + 1) + c(K)
TE = lambda m, K: g(m + 1) + 2 * (ceil(log2(factorial(2 ** m))) if m else 0) + 2 * 2 ** m + g(K + 1)
incl = all(TE(m, K) >= TR(m, K) for m in (0, 1) for K in range(1, 1 << 20))
print("T7 T_E >= T_R for m in {0,1}, 1<=K<2^20 (E-region subset of R-region):", incl)
print("T7 T_E - T_R at m=0,1 for K=4,7,15,63:", [(m, K, TE(m, K) - TR(m, K)) for m in (0, 1) for K in (4, 7, 15, 63)])
print("ALL EXPECTATIONS MET:", allok)
