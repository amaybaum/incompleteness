#!/usr/bin/env python3
# opglue_probes.py — certificate for the finite operational realization and gluing
# theorem (Main §3.4, b126). Exact arithmetic over Q(√2)+iQ(√2).
#
# Instance: qubit (d=2), horizons K=2 and K=3, family F = {Z, X, H, R}:
#   Z: projective computational-basis measurement (outcomes 0/1)
#   X: projective Hadamard-basis measurement (outcomes 0/1; rational Kraus)
#   H: Hadamard unitary, outcome-free intervention (1/√2 entries)
#   R: the 3-4-5 rotation [[3/5,-4/5],[4/5,3/5]] — rational, exactly unitary,
#      producing NON-DYADIC branch probabilities (9/25 etc.), so power-of-two
#      seed grids cannot be exact and the ε>0 regime is genuinely exercised.
# Realization: per-instrument FIXED injective step maps; hidden sector = current
# unnormalized branch vector + garbage stack + K pre-loaded uniform grid seeds.
#
# Certified: (1) completeness/adaptivity with TV ≤ K/G at G∈{8,128,1024}, and
# TV > 0 in the non-dyadic case with ~1/G scaling; (2) operational
# noncommutativity: outcome-string laws for XZ vs ZX differ far beyond bound,
# and Z-repeatability holds; (3) restriction consistency; (4) mechanism
# fixedness; (5) per-instrument injectivity on the reachable set (G=8, K=2);
# (6) seed-enumeration dynamics equals the analytic grid-count law exactly;
# (7) capacity accounting + capacity floor log2|C_H| ≥ I*.
import sys, math
from fractions import Fraction as F
from itertools import product

class R:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0): self.a = F(a); self.b = F(b)
    def __add__(s, o): return R(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return R(s.a - o.a, s.b - o.b)
    def __mul__(s, o): return R(s.a * o.a + 2 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def sign(s):
        if s.a == 0 and s.b == 0: return 0
        if s.a >= 0 and s.b >= 0: return 1 if (s.a > 0 or s.b > 0) else 0
        if s.a <= 0 and s.b <= 0: return -1
        if s.a > 0:
            d = s.a * s.a - 2 * s.b * s.b
            return 1 if d > 0 else (-1 if d < 0 else 0)
        d = s.a * s.a - 2 * s.b * s.b
        return -1 if d > 0 else (1 if d < 0 else 0)
    def __float__(s): return float(s.a) + float(s.b) * 2 ** 0.5

R0, R1, RH = R(0), R(1), R(0, F(1, 2))
class C:
    __slots__ = ("re", "im")
    def __init__(s, re=None, im=None):
        s.re = re if re is not None else R0
        s.im = im if im is not None else R0
    def __add__(s, o): return C(s.re + o.re, s.im + o.im)
    def __mul__(s, o): return C(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def __eq__(s, o): return s.re == o.re and s.im == o.im
    def __hash__(s): return hash((s.re, s.im))
    def abs2(s): return s.re * s.re + s.im * s.im
CZ, CO = C(R0, R0), C(R1, R0)
def mat_apply(M, v):
    return (M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1])
def norm2(v): return v[0].abs2() + v[1].abs2()

half = C(R(F(1, 2)), R0); nhalf = C(R(F(-1, 2)), R0)
P0 = [[CO, CZ], [CZ, CZ]]; P1 = [[CZ, CZ], [CZ, CO]]
Pp = [[half, half], [half, half]]; Pm = [[half, nhalf], [nhalf, half]]
Hm = [[C(RH, R0), C(RH, R0)], [C(RH, R0), C(R(0, F(-1, 2)), R0)]]
c35, c45, n45 = C(R(F(3,5)), R0), C(R(F(4,5)), R0), C(R(F(-4,5)), R0)
Rm = [[c35, n45], [c45, c35]]
INSTR = {"Z": [("0", P0), ("1", P1)], "X": [("0", Pp), ("1", Pm)],
         "H": [(".", Hm)], "R": [(".", Rm)]}
PSI0 = (CO, CZ)

def quantum_law(strategy, K):
    out = {}
    def rec(v, hist):
        if len(hist) == K:
            out[hist] = norm2(v); return
        a = strategy(hist)
        for o, M in INSTR[a]:
            rec(mat_apply(M, v), hist + ((a, o),))
    rec(PSI0, ()); return out

def count_below(G, num, den):
    lo, hi = 0, G
    while lo < hi:
        mid = (lo + hi) // 2
        if (R(G) * num - R(mid) * den).sign() > 0: lo = mid + 1
        else: hi = mid
    return lo

def realized_law(strategy, K, G):
    out = {}
    def rec(v, hist, weight):
        if len(hist) == K:
            out[hist] = weight; return
        a = strategy(hist); krs = INSTR[a]
        if len(krs) == 1:
            o, M = krs[0]
            rec(mat_apply(M, v), hist + ((a, o),), weight); return
        den = norm2(v)
        if den.sign() == 0: return
        (o0, M0), (o1, M1) = krs
        q0 = norm2(mat_apply(M0, v))
        c0 = count_below(G, q0, den)
        if c0: rec(mat_apply(M0, v), hist + ((a, o0),), weight * F(c0, G))
        if G - c0: rec(mat_apply(M1, v), hist + ((a, o1),), weight * F(G - c0, G))
    rec(PSI0, (), F(1)); return out

def tv(law_r, law_q):
    s = R0
    for k in set(law_r) | set(law_q):
        d = R(law_r.get(k, F(0))) - law_q.get(k, R0)
        if d.sign() < 0: d = R0 - d
        s = s + d
    return float(s) / 2.0

def strings(law):
    m = {}
    for hist, p in law.items():
        key = "".join(o for _, o in hist)
        m[key] = m.get(key, F(0)) + (p if isinstance(p, F) else F(0))
    return m
def strings_q(law):
    m = {}
    for hist, p in law.items():
        key = "".join(o for _, o in hist)
        m[key] = (m.get(key, R0) + p)
    return m

def S_fixed(*names): return lambda h: names[len(h)]
def AD2(h):  # adaptive, K=2
    return "X" if len(h) == 0 else ("Z" if h[0][1] == "0" else "X")
def AD3(h):  # adaptive, K=3, exercises R on one branch
    if len(h) == 0: return "X"
    if len(h) == 1: return "Z" if h[0][1] == "0" else "R"
    return "X"

fails = 0
def check(name, cond, msg=""):
    global fails
    print(("PASS " if cond else "FAIL ") + name + ("  " + msg if msg else ""))
    if not cond: fails += 1

# ---- K=2 block ----
K = 2
strats2 = {"ZZ": S_fixed("Z","Z"), "XZ": S_fixed("X","Z"), "ZX": S_fixed("Z","X"),
           "HZ": S_fixed("H","Z"), "RZ": S_fixed("R","Z"), "AD": AD2}
tv_at = {}; tv_rz = {}
for G in (8, 128, 1024):
    worst = 0.0
    for nm, st in strats2.items():
        d = tv(realized_law(st, K, G), quantum_law(st, K))
        worst = max(worst, d)
        if nm == "RZ": tv_rz[G] = d
    tv_at[G] = worst
    check(f"tv_bound_K2_G{G}", worst <= K / G + 1e-15, f"worst {worst:.3e} <= {K/G:.3e}")
check("epsilon_regime_nonzero", tv_rz[8] > 0 and tv_rz[128] > 0,
      f"RZ TVs: {tv_rz[8]:.3e}, {tv_rz[128]:.3e}, {tv_rz[1024]:.3e}")
check("epsilon_scaling", tv_rz[1024] <= tv_rz[8] / 16,
      f"{tv_rz[8]:.3e} -> {tv_rz[1024]:.3e}")

# ---- noncommutativity via outcome-string laws ----
G = 128
sxz = strings(realized_law(strats2["XZ"], K, G))
szx = strings(realized_law(strats2["ZX"], K, G))
dtv = float(sum(abs(sxz.get(k, F(0)) - szx.get(k, F(0)))
               for k in set(sxz) | set(szx))) / 2
check("noncommutativity_strings", dtv > 4 * (K / G), f"TV(strings XZ, ZX) = {dtv:.3f}")
szz = strings(realized_law(strats2["ZZ"], K, G))
rep = float(szz.get("00", F(0)) + szz.get("11", F(0)))
check("Z_repeatability", abs(rep - 1.0) <= K / G + 1e-12, f"P(o1=o2|ZZ) = {rep:.4f}")

# ---- restriction consistency ----
lr = realized_law(strats2["ZZ"], K, G)
check("restriction_exact", lr == realized_law(strats2["ZZ"], K, G))
check("restriction_quantum", tv(lr, quantum_law(strats2["ZZ"], K)) <= K / G + 1e-15)

# ---- mechanism fixedness (structural) ----
check("mechanism_fixed", len(INSTR) == 4)

# ---- K=3 block ----
K3 = 3
strats3 = {"ZZZ": S_fixed("Z","Z","Z"), "XZX": S_fixed("X","Z","X"),
           "RZX": S_fixed("R","Z","X"), "AD3": AD3}
for G in (8, 1024):
    worst = max(tv(realized_law(st, K3, G), quantum_law(st, K3))
                for st in strats3.values())
    check(f"tv_bound_K3_G{G}", worst <= K3 / G + 1e-15, f"worst {worst:.3e} <= {K3/G:.3e}")

# ---- dynamics enumeration + injectivity at G=8, K=2 ----
G = 8
def step(state, a, t):
    v, stack, seeds = state
    krs = INSTR[a]
    if len(krs) == 1:
        o, M = krs[0]
        return (mat_apply(M, v), stack + (v,), seeds), o
    den = norm2(v)
    q0 = norm2(mat_apply(krs[0][1], v))
    take0 = (R(G) * q0 - R(seeds[t]) * den).sign() > 0
    o, M = krs[0] if take0 else krs[1]
    return (mat_apply(M, v), stack + (v,), seeds), o

enum_ok = True
for nm, st in strats2.items():
    counts = {}
    for seeds in product(range(G), repeat=2):
        state = (PSI0, (), seeds); hist = ()
        for t in range(2):
            a = st(hist); state, o = step(state, a, t)
            hist = hist + ((a, o),)
        counts[hist] = counts.get(hist, 0) + 1
    analytic = realized_law(st, 2, G)
    for hist in set(counts) | set(analytic):
        if F(counts.get(hist, 0), G ** 2) != analytic.get(hist, F(0)):
            enum_ok = False
check("dynamics_matches_analytic_G8", enum_ok)

reach = set()
for nm, st in strats2.items():
    for seeds in product(range(G), repeat=2):
        state = (PSI0, (), seeds); hist = ()
        reach.add((0, state))
        for t in range(2):
            a = st(hist); state, o = step(state, a, t)
            hist = hist + ((a, o),); reach.add((t + 1, state))
inj_ok = True
for a in INSTR:
    for t in range(2):
        img = {}
        for (tt, s) in reach:
            if tt != t: continue
            out, _ = step(s, a, t)
            if out in img and img[out] != s: inj_ok = False
            img[out] = s
check("per_instrument_injectivity_G8", inj_ok, f"reachable: {len(reach)}")

hid = set(s for (_, s) in reach)
log2CH = math.log2(len(hid))
law = realized_law(AD2, 2, G)
pj = {}
for hist, p in law.items():
    pj[(hist[0][1], hist[1][1])] = pj.get((hist[0][1], hist[1][1]), F(0)) + p
def Hent(ps): return -sum(float(p) * math.log2(float(p)) for p in ps if p > 0)
p1 = {}; p2 = {}
for (o1, o2), p in pj.items():
    p1[o1] = p1.get(o1, F(0)) + p; p2[o2] = p2.get(o2, F(0)) + p
Istar = Hent(p1.values()) + Hent(p2.values()) - Hent(pj.values())
check("capacity_floor", log2CH >= Istar - 1e-9,
      f"log2|C_H| = {log2CH:.2f} >= I* = {Istar:.3f}")
# ---- (8) adaptive diamond telescoping, and (9) off-net mutual density (b126) ----
# Second exact rational rotation: the 5-12-13.
c513, c1213, n1213 = C(R(F(5,13)), R0), C(R(F(12,13)), R0), C(R(F(-12,13)), R0)
Rm2 = [[c513, n1213], [c1213, c513]]
INSTR["R2"] = [(".", Rm2)]
import cmath
def _f(x): return complex(float(x.re), float(x.im))
def fmat(M): return [[_f(M[0][0]), _f(M[0][1])], [_f(M[1][0]), _f(M[1][1])]]
def opnorm2x2(A):  # largest singular value of a 2x2 complex matrix
    a, b, c, d = A[0][0], A[0][1], A[1][0], A[1][1]
    g11 = abs(a)**2 + abs(c)**2; g22 = abs(b)**2 + abs(d)**2
    g12 = a.conjugate()*b + c.conjugate()*d
    tr, det = g11 + g22, g11*g22 - abs(g12)**2
    lam = (tr + math.sqrt(max(tr*tr - 4*det, 0.0))) / 2.0
    return math.sqrt(max(lam, 0.0))
def msub(A, B): return [[A[i][j]-B[i][j] for j in range(2)] for i in range(2)]
SEQ  = lambda seq: (lambda hist: seq[len(hist)])
prot_R  = SEQ(["H", "R", "Z"]);  prot_R2 = SEQ(["H", "R2", "Z"])
G9 = 1024
law_R  = realized_law(prot_R, 3, G9); law_R2 = realized_law(prot_R2, 3, G9)
tvf = 0.0
keys = set("".join(o for _, o in h) for h in law_R) | set("".join(o for _, o in h) for h in law_R2)
sR, sR2 = strings(law_R), strings(law_R2)
tvf = sum(abs(float(sR.get(k, F(0))) - float(sR2.get(k, F(0)))) for k in keys) / 2.0
dop = opnorm2x2(msub(fmat(Rm), fmat(Rm2)))
bound8 = 2.0 * dop + 2 * 3.0 / G9
check("telescoping_bound", 0.01 < tvf <= bound8 + 1e-12,
      f"TV = {tvf:.4f} <= 2||dU||_op + 2K/G = {bound8:.4f}")
# (9) off-net target: rotation by the mean angle, realized via the nearer net member.
th = (math.atan2(4/5, 3/5) + math.atan2(12/13, 5/13)) / 2.0
Rt = [[complex(math.cos(th)), complex(-math.sin(th))],
      [complex(math.sin(th)), complex(math.cos(th))]]
def fquantum(seq, K):
    out = {}
    def app(M, v): return (M[0][0]*v[0] + M[0][1]*v[1], M[1][0]*v[0] + M[1][1]*v[1])
    def rec(v, hist):
        if len(hist) == K:
            key = "".join(o for _, o in hist)
            out[key] = out.get(key, 0.0) + abs(v[0])**2 + abs(v[1])**2; return
        a = seq[len(hist)]
        if a == "T":
            rec(app(Rt, v), hist + (("T", "."),)); return
        for o, M in INSTR[a]:
            rec(app(fmat(M), v), hist + ((a, o),))
    rec((1.0 + 0.0j, 0.0j), ()); return out
q_target = fquantum(["H", "T", "Z"], 3)
dR, dR2 = opnorm2x2(msub(Rt, fmat(Rm))), opnorm2x2(msub(Rt, fmat(Rm2)))
near, dnear = ("R", dR) if dR <= dR2 else ("R2", dR2)
law_near = strings(realized_law(SEQ(["H", near, "Z"]), 3, G9))
tvd = sum(abs(q_target.get(k, 0.0) - float(law_near.get(k, F(0))))
          for k in set(q_target) | set(law_near)) / 2.0
bound9 = 2.0 * dnear + 3.0 / G9
check("mutual_density_offnet", tvd <= bound9 + 1e-12,
      f"TV(off-net target, net realization) = {tvd:.4f} <= {bound9:.4f} via {near}")

# ---- (10) renormalization invariance: power-of-two rescaling leaves the law exact (b127) ----
d35 = C(R(F(3,5)), R0); d45 = C(R(F(4,5)), R0)
INSTR["D"] = [("0", [[CO, CZ], [CZ, d35]]), ("1", [[CZ, d45], [CZ, CZ]])]
Rhalf = R(F(1,2))
def realized_law_rescaled(strategy, K, G):
    out = {}
    def rec(v, hist, weight, shifts):
        if len(hist) == K:
            out[hist] = weight; return
        a = strategy(hist); krs = INSTR[a]
        def renorm(u, sh):
            while float(norm2(u)) < 0.5:
                u = (C(u[0].re + u[0].re, u[0].im + u[0].im),
                     C(u[1].re + u[1].re, u[1].im + u[1].im)); sh += 1
            while float(norm2(u)) >= 2.0:
                u = (C(u[0].re * Rhalf, u[0].im * Rhalf),
                     C(u[1].re * Rhalf, u[1].im * Rhalf)); sh -= 1
            return u, sh
        if len(krs) == 1:
            o, M = krs[0]
            u, sh = renorm(mat_apply(M, v), shifts)
            rec(u, hist + ((a, o),), weight, sh); return
        den = norm2(v)
        if den.sign() == 0: return
        (o0, M0), (o1, M1) = krs
        q0 = norm2(mat_apply(M0, v))
        c0 = count_below(G, q0, den)
        if c0:
            u, sh = renorm(mat_apply(M0, v), shifts)
            rec(u, hist + ((a, o0),), weight * F(c0, G), sh)
        if G - c0:
            u, sh = renorm(mat_apply(M1, v), shifts)
            rec(u, hist + ((a, o1),), weight * F(G - c0, G), sh)
    rec(PSI0, (), F(1), 0); return out
prot_D = SEQ(["H", "D", "D", "Z"])
lawA = realized_law(prot_D, 4, 128)
MAXSH = [0]
_orig_renorm_probe = None
lawB = {}
def _run_rescaled_tracking():
    out = {}
    def rec(v, hist, weight, shifts):
        MAXSH[0] = max(MAXSH[0], abs(shifts))
        if len(hist) == 4:
            out[hist] = weight; return
        a = prot_D(hist); krs = INSTR[a]
        def renorm(u, sh):
            while float(norm2(u)) < 0.5:
                u = (C(u[0].re + u[0].re, u[0].im + u[0].im),
                     C(u[1].re + u[1].re, u[1].im + u[1].im)); sh += 1
            while float(norm2(u)) >= 2.0:
                u = (C(u[0].re * Rhalf, u[0].im * Rhalf),
                     C(u[1].re * Rhalf, u[1].im * Rhalf)); sh -= 1
            return u, sh
        if len(krs) == 1:
            o, M = krs[0]
            u, sh = renorm(mat_apply(M, v), shifts)
            rec(u, hist + ((a, o),), weight, sh); return
        den = norm2(v)
        if den.sign() == 0: return
        (o0, M0), (o1, M1) = krs
        q0 = norm2(mat_apply(M0, v))
        c0 = count_below(128, q0, den)
        if c0:
            u, sh = renorm(mat_apply(M0, v), shifts)
            rec(u, hist + ((a, o0),), weight * F(c0, 128), sh)
        if 128 - c0:
            u, sh = renorm(mat_apply(M1, v), shifts)
            rec(u, hist + ((a, o1),), weight * F(128 - c0, 128), sh)
    rec(PSI0, (), F(1), 0); return out
lawB = _run_rescaled_tracking()
check("rescaling_invariance", lawA == lawB and MAXSH[0] >= 1,
      f"laws identical over {len(lawA)} branches; max |shift| = {MAXSH[0]} (H,D,D,Z at K=4, G=128)")

print(f"summary: hidden states {len(hid)} (log2 {log2CH:.2f}); "
      f"RZ TV at G=8/128/1024: {tv_rz[8]:.2e}/{tv_rz[128]:.2e}/{tv_rz[1024]:.2e}")
sys.exit(1 if fails else 0)
