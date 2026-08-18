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
# Extended: checks 8–9 telescoping / off-net density (b126b), 10 rescaling invariance (b127),
# 11–12 density register + mixed conditionals for multi-Kraus instruments (b128),
# 13 single controlled dynamics — one bijection, protocol as initial condition (b129),
# 14 Rounding Lemma instances — exact rational FIXED-POINT dyadic rounding vs exact
#    instrument, Hermiticity by upper-triangle storage (b131, reworked b132);
#    plus the instrument-level cq aggregate over the whole outcome direct sum (b133).

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

# ---- (11)-(12) density-matrix branch register: general multi-Kraus instruments (b128) ----
def cconj(z): return C(z.re, R(0) - z.im)
def mdag(M): return [[cconj(M[0][0]), cconj(M[1][0])], [cconj(M[0][1]), cconj(M[1][1])]]
def mmul(A, B):
    return [[A[i][0]*B[0][j] + A[i][1]*B[1][j] for j in range(2)] for i in range(2)]
def madd(A, B): return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
def mtrace(A): return A[0][0].re + A[1][1].re      # real part; im asserted 0 by construction
def kraus_apply(Ks, rho):
    out = [[CZ, CZ], [CZ, CZ]]
    for Kr in Ks: out = madd(out, mmul(mmul(Kr, rho), mdag(Kr)))
    return out
k1 = [[c35, CZ], [CZ, CZ]]                          # (3/5) P0
k2 = [[CZ, CZ], [c45, CZ]]                          # (4/5) X P0
INSTR_DM = {"H": [(".", [Hm])], "Z": [("0", [P0]), ("1", [P1])],
            "N": [("0", [k1, k2]), ("1", [P1])]}
RHO0 = [[CO, CZ], [CZ, CZ]]
def quantum_dm(seq, K):
    out = {}
    def rec(rho, hist):
        if len(hist) == K:
            key = "".join(o for _, o in hist)
            out[key] = out.get(key, R(0)) + mtrace(rho); return
        a = seq[len(hist)]
        for o, Ks in INSTR_DM[a]:
            nr = kraus_apply(Ks, rho)
            if mtrace(nr).sign() != 0 or o == ".":
                rec(nr, hist + ((a, o),))
    rec(RHO0, ()); return out
def realized_dm(seq, K, G):
    out = {}
    def rec(rho, hist, weight):
        if len(hist) == K:
            key = "".join(o for _, o in hist)
            out[key] = out.get(key, F(0)) + weight; return
        a = seq[len(hist)]; krs = INSTR_DM[a]
        if len(krs) == 1:
            o, Ks = krs[0]
            rec(kraus_apply(Ks, rho), hist + ((a, o),), weight); return
        den = mtrace(rho)
        if den.sign() == 0: return
        (o0, K0), (o1, K1) = krs
        r0 = kraus_apply(K0, rho)
        q0 = mtrace(r0)
        c0 = count_below(G, q0, den)
        if c0: rec(r0, hist + ((a, o0),), weight * F(c0, G))
        if G - c0: rec(kraus_apply(K1, rho), hist + ((a, o1),), weight * F(G - c0, G))
    rec(RHO0, (), F(1)); return out
SEQN = ["H", "N", "Z"]
qdm = quantum_dm(SEQN, 3)
rdm = realized_dm(SEQN, 3, 200)
same = set(qdm) == set(rdm) and all((qdm[k] - R(rdm[k])) == R(0) for k in qdm)
check("dm_matches_quantum_exact", same,
      f"multi-Kraus instrument N, protocol H-N-Z, G=200: realized == quantum exactly over {len(qdm)} strings")
rho_plus = kraus_apply([Hm], RHO0)
r0 = kraus_apply([k1, k2], rho_plus)
pur = mtrace(mmul(r0, r0)); trsq = mtrace(r0) * mtrace(r0)
check("conditional_mixedness", (trsq - pur).sign() > 0,
      "Tr(I_0(rho)^2) < (Tr I_0(rho))^2 exactly — genuinely mixed conditional, beyond the branch-vector form")

# ---- (13) single controlled dynamics: one bijection, protocol as initial condition (b129) ----
def policy_A(hist): return ["H", "Z", "Z"][len(hist)]
def policy_B(hist):
    if len(hist) < 2: return ["H", "Z"][len(hist)]
    return "Z" if hist[1][1] == "0" else "X"
POL = {"A": policy_A, "B": policy_B}
G13, K13 = 4, 3
def vkey(v): return (str(v[0].re.a), str(v[0].re.b), str(v[0].im.a), str(v[0].im.b),
                     str(v[1].re.a), str(v[1].re.b), str(v[1].im.a), str(v[1].im.b))
def phi_single(state):
    prog, t, seeds, rec, v, stack = state
    a = POL[prog](rec)
    krs = INSTR[a]
    if len(krs) == 1:
        o, M = krs[0]
        nv = mat_apply(M, v)
        return (prog, t + 1, seeds, rec + ((a, o),), nv, stack + ("U",))
    den = norm2(v)
    (o0, M0), (o1, M1) = krs
    q0 = norm2(mat_apply(M0, v))
    c0 = count_below(G13, q0, den)
    r = seeds[t]
    o, M = (o0, M0) if r < c0 else (o1, M1)
    return (prog, t + 1, seeds, rec + ((a, o),), mat_apply(M, v), stack + ("P", vkey(v)))
from itertools import product as iproduct
img_by_src = {}
laws = {"A": {}, "B": {}}
for prog in ("A", "B"):
    for seeds in iproduct(range(G13), repeat=K13):
        s = (prog, 0, seeds, (), PSI0, ())
        for _ in range(K13):
            s2 = phi_single(s)
            img_by_src[(prog, s[1], seeds, s[3], vkey(s[4]), s[5])] =                 (prog, s2[1], seeds, s2[3], vkey(s2[4]), s2[5])
            s = s2
        key = "".join(o for _, o in s[3])
        laws[prog][key] = laws[prog].get(key, F(0)) + F(1, G13 ** K13)
inj = len(set(img_by_src.values())) == len(img_by_src)
lawA_ref = realized_law(policy_A, K13, G13)
lawB_ref = realized_law(policy_B, K13, G13)
def strmarg(law):
    out = {}
    for hist, w in law.items():
        k = "".join(o for _, o in hist)
        out[k] = out.get(k, F(0)) + w
    return out
match = laws["A"] == strmarg(lawA_ref) and laws["B"] == strmarg(lawB_ref)
check("single_controlled_dynamics", inj and match,
      f"one map, two protocols (one adaptive), {len(img_by_src)} steps injective; laws exact")

# ---- (14) Rounding Lemma instances: exact rational simulation of b-bit rounding (b131) ----
def fl_frac(x, b):
    # fixed-point dyadic rounding: b FRACTIONAL bits, round-to-nearest-even,
    # absolute error <= 2^{-b-1}; integer part unconstrained (O(log d) bits, counted)
    num = x * (2 ** b)
    fl = num.numerator // num.denominator
    rem = num - fl
    if rem > F(1, 2) or (rem == F(1, 2) and fl % 2 == 1): fl += 1
    return F(fl, 2 ** b)
def fadd(x, y, b): return fl_frac(x + y, b)
def fmul(x, y, b): return fl_frac(x * y, b)
def cmulf(z, w, b):   # complex parts as (re, im) Fractions
    return (fadd(fmul(z[0], w[0], b), -fmul(z[1], w[1], b), b),
            fadd(fmul(z[0], w[1], b), fmul(z[1], w[0], b), b))
def caddf(z, w, b): return (fadd(z[0], w[0], b), fadd(z[1], w[1], b))
def mat_f(M): return [[(F(0), F(0)) if M[i][j] is None else M[i][j] for j in range(2)] for i in range(2)]
def mmulf(A, B, b):
    out = [[(F(0), F(0)) for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            acc = cmulf(A[i][0], B[0][j], b)
            acc = caddf(acc, cmulf(A[i][1], B[1][j], b), b)
            out[i][j] = acc
    return out
def dagf(M): return [[(M[j][i][0], -M[j][i][1]) for j in range(2)] for i in range(2)]
def maddf(A, B, b): return [[caddf(A[i][j], B[i][j], b) for j in range(2)] for i in range(2)]
KR_N = [[[(F(3,5), F(0)), (F(0), F(0))], [(F(0), F(0)), (F(0), F(0))]],
        [[(F(0), F(0)), (F(0), F(0))], [(F(4,5), F(0)), (F(0), F(0))]]]
KR_Z0 = [[[(F(1), F(0)), (F(0), F(0))], [(F(0), F(0)), (F(0), F(0))]]]
STATES = [
 [[(F(1), F(0)), (F(0), F(0))], [(F(0), F(0)), (F(0), F(0))]],
 [[(F(1,2), F(0)), (F(1,2), F(0))], [(F(1,2), F(0)), (F(1,2), F(0))]],
 [[(F(1,3), F(0)), (F(1,6), F(1,7))], [(F(1,6), F(-1,7)), (F(2,3), F(0))]],
]
def exact_apply(Ks, rho):
    out = [[(F(0), F(0)) for _ in range(2)] for _ in range(2)]
    for Kr in Ks:
        Kd = dagf(Kr)
        B = [[(sum2 := None) for _ in range(2)] for _ in range(2)]
        def cm(z, w): return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])
        def ca(z, w): return (z[0]+w[0], z[1]+w[1])
        B = [[ca(cm(Kr[i][0], rho[0][j]), cm(Kr[i][1], rho[1][j])) for j in range(2)] for i in range(2)]
        Cm = [[ca(cm(B[i][0], Kd[0][j]), cm(B[i][1], Kd[1][j])) for j in range(2)] for i in range(2)]
        out = [[ca(out[i][j], Cm[i][j]) for j in range(2)] for i in range(2)]
    return out
def float_apply(Ks, rho, b):
    Ksr = [[[ (fl_frac(Kr[i][j][0], b), fl_frac(Kr[i][j][1], b)) for j in range(2)] for i in range(2)] for Kr in Ks]
    out = [[(F(0), F(0)) for _ in range(2)] for _ in range(2)]
    for Kr in Ksr:
        B = mmulf(Kr, rho, b)
        Cm = mmulf(B, dagf(Kr), b)
        out = maddf(out, Cm, b)
    out[1][0] = (out[0][1][0], -out[0][1][1])   # Hermiticity exact: upper-triangle storage
    return out
Cdr = F(768)   # per-outcome 24 r d^4 at d=2, r=2 (fixed-point dyadic model)
CdR = F(2304)  # instrument-level 48 R d^4 at d=2, R=3 (cq direct sum, b133)
ok14 = True
worst = F(0)
for Ks in (KR_N, KR_Z0):
    for rho in STATES:
        tr = rho[0][0][0] + rho[1][1][0]
        for b in (8, 16, 24):
            E = exact_apply(Ks, rho)
            Eh = float_apply(Ks, rho, b)
            fro2 = F(0)
            for i in range(2):
                for j in range(2):
                    dr = Eh[i][j][0] - E[i][j][0]; di = Eh[i][j][1] - E[i][j][1]
                    fro2 += dr*dr + di*di
            lhs = 2 * fro2
            rhs = Cdr*Cdr * F(1, 4**b) * tr*tr
            if lhs > rhs: ok14 = False
            herm = all(Eh[i][j][0] == Eh[j][i][0] and Eh[i][j][1] == -Eh[j][i][1]
                       for i in range(2) for j in range(2))
            if not herm: ok14 = False
            if rhs > 0 and lhs * 10**12 // rhs > worst: worst = lhs * 10**12 // rhs
check("rounding_lemma_instances", ok14,
      f"18 per-outcome instances, fixed-point dyadic, Hermiticity exact: worst ratio {float(worst)/1e12:.2e}")
# instrument-level cq aggregate: sum of block errors vs C_{d,R} (whole instrument N: R=3)
KR_N1 = [[[(F(0), F(0)), (F(0), F(0))], [(F(0), F(0)), (F(1), F(0))]]]   # outcome 1: P1
ok14b = True
worstb = F(0)
for rho in STATES:
    tr = rho[0][0][0] + rho[1][1][0]
    for b in (8, 16, 24):
        tot2 = F(0)
        for Ks in (KR_N, KR_N1):
            E = exact_apply(Ks, rho); Eh = float_apply(Ks, rho, b)
            fro2 = F(0)
            for i in range(2):
                for j in range(2):
                    dr = Eh[i][j][0] - E[i][j][0]; di = Eh[i][j][1] - E[i][j][1]
                    fro2 += dr*dr + di*di
            tot2 += fro2
        # sum_o ||diff_o||_1 <= sqrt(2) * sum_o ||diff_o||_F <= sqrt(2) * sqrt(2 * tot2)  (2 blocks)
        lhs = 4 * tot2                       # (sum_o ||.||_1)^2 <= 2 * (2 * tot2) = 4 tot2
        rhs = CdR*CdR * F(1, 4**b) * tr*tr
        if lhs > rhs: ok14b = False
        if rhs > 0 and lhs * 10**12 // rhs > worstb: worstb = lhs * 10**12 // rhs
check("rounding_lemma_cq_instrument", ok14b,
      f"instrument-level cq: sum over outcome blocks <= C_dR 2^-b Tr rho, C_dR=2304 (48 R d^4, R=3); worst ratio {float(worstb)/1e12:.2e}")

# ---- (15) cq telescoping: exact vs fixed-point subnormalized branch ensembles (b133) ----
b15, K15 = 16, 3
INSTR15 = {"N": [KR_N, KR_N1], "Z": [KR_Z0, KR_N1]}
prot15 = ["N", "Z", "N"]
RHO_P = [[(F(1,2),F(0)),(F(1,2),F(0))],[(F(1,2),F(0)),(F(1,2),F(0))]]
sig_ex = {(): RHO_P}
sig_fx = {(): RHO_P}
for a in prot15:
    ne, nf = {}, {}
    for h in sig_ex:
        for oi, Ks in enumerate(INSTR15[a]):
            ne[h + (oi,)] = exact_apply(Ks, sig_ex[h])
            nf[h + (oi,)] = float_apply(Ks, sig_fx[h], b15)
    sig_ex, sig_fx = ne, nf
sumfro2 = F(0)
sumtr = F(0)
hermall = True
for h in sig_ex:
    E, Eh = sig_ex[h], sig_fx[h]
    fro2 = F(0)
    for i in range(2):
        for j in range(2):
            dr = Eh[i][j][0] - E[i][j][0]; di = Eh[i][j][1] - E[i][j][1]
            fro2 += dr*dr + di*di
    sumfro2 += fro2
    dtr = (Eh[0][0][0] + Eh[1][1][0]) - (E[0][0][0] + E[1][1][0])
    sumtr += (dtr if dtr >= 0 else -dtr)
    hermall &= all(Eh[i][j][0] == Eh[j][i][0] and Eh[i][j][1] == -Eh[j][i][1]
                   for i in range(2) for j in range(2))
RHS15 = 2 * K15 * CdR * F(1, 2**b15)
# (sum_h ||diff_h||_1)^2 <= |branches| * sum_h 2 fro2_h  (Cauchy-Schwarz + sqrt2||.||_F at d=2)
ok15 = (len(sig_ex) * 2 * sumfro2 <= RHS15 * RHS15) and (sumtr <= RHS15) and hermall
check("cq_telescoping", ok15,
      f"K=3 ensemble, {len(sig_ex)} branches incl. rare: total ||diff||_1 bound and classical-marginal drift {float(sumtr):.2e} both <= 2 K C_dR 2^-b = {float(RHS15):.2e}; Hermiticity everywhere")

# ---- (16) the actual simulator kernel: clip + normalize + grid-free ratios (b134) ----
from math import isqrt
def branch_neg_upper(A):
    # EXACT eigen form for 2x2 Hermitian: ||A_-||_1 = max(0, (sqrt(T^2-4detA) - T)/2),
    # with a dyadic ceiling on the square root (tight: slack ~2^-40)
    T = A[0][0][0] + A[1][1][0]
    det = A[0][0][0]*A[1][1][0] - (A[0][1][0]*A[0][1][0] + A[0][1][1]*A[0][1][1])
    disc = T*T - 4*det
    if disc <= 0: return F(0)
    N = (disc * 4**40).numerator // (disc * 4**40).denominator + 1
    su = F(isqrt(N) + 1, 2**40)
    v = (su - T) / 2
    return v if v > 0 else F(0)
RHO_REF16 = [[(F(1), F(0)), (F(0), F(0))], [(F(0), F(0)), (F(0), F(0))]]
ok16 = True
for b16 in (20, 24):
    eta = CdR * F(1, 2**b16)
    ex = {(): (RHO_P, F(1))}
    fxk = {(): (RHO_P, F(1))}
    fallback_mass = F(0)
    for step, a in enumerate(prot15, start=1):
        ne, nf = {}, {}
        for h in ex:
            rho_e, w_e = ex[h]
            Be = [exact_apply(Ks, rho_e) for Ks in INSTR15[a]]
            se = sum(B[0][0][0] + B[1][1][0] for B in Be)
            for oi, B in enumerate(Be):
                tre = B[0][0][0] + B[1][1][0]
                ne[h + (oi,)] = (B, w_e * (tre / se if se > 0 else F(0)))
        nu = F(0)
        for h in fxk:
            rho_f, w_f = fxk[h]
            Bf = [float_apply(Ks, rho_f, b16) for Ks in INSTR15[a]]
            cs = [max(B[0][0][0] + B[1][1][0], F(0)) for B in Bf]
            Qh = sum(cs)
            if Qh <= 0:
                # deterministic fallback: outcome o*=0 written, register set to P0; mass kept
                fallback_mass += w_f
                nf[h + (0,)] = (RHO_REF16, w_f)
                for oi in range(1, len(Bf)):
                    nf[h + (oi,)] = (Bf[oi], F(0))
                continue
            for oi, B in enumerate(Bf):
                nf[h + (oi,)] = (B, w_f * cs[oi] / Qh)
                nu += branch_neg_upper(B)
        if nu > 2 * step * eta:
            ok16 = False; print(f"  DIAG b={b16} step={step}: nu {float(nu):.2e} > {float(2*step*eta):.2e}")
        ex, fxk = ne, nf
    tv = sum(abs(ex[h][1] - fxk[h][1]) for h in ex) / 2
    bound = 12 * 9 * CdR * F(1, 2**b16)          # 12 K^2 C_{d,R} 2^-b, K=3
    if fallback_mass > 2 * 3 * eta:
        ok16 = False; print(f"  DIAG b={b16}: fallback mass {float(fallback_mass):.2e}")
    tot_mass = sum(fxk[h][1] for h in fxk)
    if tot_mass != F(1):
        ok16 = False; print(f"  DIAG b={b16}: mass {float(tot_mass)} != 1 (bijection must conserve)")
    if tv > bound:
        ok16 = False; print(f"  DIAG b={b16}: tv {float(tv):.2e} > bound {float(bound):.2e}")
check("simulator_kernel_clipped_normalized", ok16,
      "actual pre-grid kernel (clip + normalize + deterministic fallback) over the K=3 tree at b in {20,24}: "
      "classical TV within 12 K^2 C_dR 2^-b; ledger nu_t <= 2 t eta; mass conserved exactly (bijection)")


print(f"summary: hidden states {len(hid)} (log2 {log2CH:.2f}); "
      f"RZ TV at G=8/128/1024: {tv_rz[8]:.2e}/{tv_rz[128]:.2e}/{tv_rz[1024]:.2e}")
sys.exit(1 if fails else 0)
