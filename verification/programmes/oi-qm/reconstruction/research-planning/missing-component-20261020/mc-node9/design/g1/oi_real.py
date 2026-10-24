"""(2) OI-side realizability of the sign/phase record by deterministic substratum updates (exact).
 (I)  record level: a record is a cell block (u, r), u in V (relation label cells), r in C (phase cell).
      Is (u, r) -> (Su, r + g_S(u)) affine for some extension, lift and section (coordinatization)?
 (II) ontic level: card phase-space cells (q_A,p_A,q_B,p_B) plus ONE extra F2 cell h; every card map extended
      affinely  s' = S s + t h,  h' = h + lambda.s + k ; reads as for the cards.  Does any such model reproduce
      the QM calibration on the witness alphabet?"""
from g1lib import *
from a_classify import brute_n1
from itertools import product
from collections import Counter

def anf_degree(g, nbits):
    a = list(g)
    for i in range(nbits):
        for x in range(1 << nbits):
            if (x >> i) & 1: a[x] ^= a[x ^ (1 << i)]
    return max([popc(x) for x in range(1 << nbits) if a[x]] + [-1])

print("== (I-a) n=1, every normalized cocycle (= every section of every class) and every lift of swap (H)")
Hs = relpush(onticmap("swap0", 1), 1)
for m in (2, 4):
    _, _ = None, None
    ncoc, classes = brute_n1(m)
    # recompute the full cocycle list (not just class reps)
    from itertools import product as P
    nz = [1, 2, 3]; allc = []
    for vals in P(range(m), repeat=9):
        b = [[0]*4 for _ in range(4)]; k = 0
        for u in nz:
            for v in nz: b[u][v] = vals[k]; k += 1
        if all((b[u][v] + b[u ^ v][w] - b[v][w] - b[u][v ^ w]) % m == 0 for u in nz for v in nz for w in nz) and \
           not any((b[u][v] - b[v][u] - (m//2)*omega(u, v, 1)) % m for u in nz for v in nz):
            allc.append(b)
    for cact in ((1,) if m == 2 else (1, -1)):
        nl = 0; naff = 0; nbitlin = 0
        for b in allc:
            E = Ext(1, m, b)
            for phi in E.lifts(Hs, cact):
                nl += 1
                g = [E.cval(phi[E.el(0, u)]) for u in range(4)]
                if all((g[u ^ v] - g[u] - g[v]) % m == 0 for u in range(4) for v in range(4)): naff += 1
                if any(all((g[u] - sum(l[i] for i in range(2) if (u >> i) & 1)) % m == 0 for u in range(4))
                       for l in P(range(m), repeat=2)): nbitlin += 1
        print("  C=Z%d, lifts %s on C: %d cocycles, %d (cocycle, lift) pairs; sign update additive in %d; bit-linear into Z%d in %d"
              % (m, "trivial" if cact == 1 else "INVERTING", len(allc), nl, naff, m, nbitlin))
print("  [W] reason: for any lift of S acting trivially on C with Su = v, Sv = u, omega(u,v) = 1:  g(u+v) - g(u) - g(v) = beta(v,u) - beta(u,v) = -(m/2) != 0,")
print("      while an additive g (and a bit-linear g at disjoint-support u, v) gives 0.")

print("== (I-b) n=2, C=Z2 real class: all 2^15 sections f (beta_f = beta0 + delta f), ANF degree of each sign update")
n = 2; R = card_relmaps(n)
E = Ext(n, 2, bilinear_beta(n, 2, real_pauli_coeff(n, 1))); d = default_dict(E)
base = {nm: ert_lift(E, S, d)[0] for nm, S in R.items()}
g0 = {nm: [E.cval(base[nm][E.el(0, u)]) for u in range(16)] for nm in R}
print("  real section s(u) = X^x Z^z: deg g =", {nm: anf_degree(g0[nm], 4) for nm in R},
      "; g_swapA == x_A z_A:", g0["swap0"] == [((u >> 0) & 1) & ((u >> 1) & 1) for u in range(16)],
      "; g_couple == 0:", g0["couple"] == [0]*16)
hist = Counter(); minmax = 9; nlin = 0
for fv in range(1 << 15):
    f = [0] + [(fv >> i) & 1 for i in range(15)]
    degs = []
    for nm, S in R.items():
        g = [g0[nm][u] ^ f[u] ^ f[S[u]] for u in range(16)]
        degs.append(anf_degree(g, 4))
    hist[tuple(degs)] += 1; minmax = min(minmax, max(degs))
    if degs[0] <= 1: nlin += 1
print("  sections with an affine (deg <= 1) swap_A update: %d of 32768; min over sections of max degree (swapA, swapB, couple): %d"
      % (nlin, minmax))
print("  degree profiles (swapA, swapB, couple) -> #sections:", dict(sorted(hist.items())))
print("  (other lifts differ by a linear character, which changes no degree >= 2)")

print("== (I-c) formula checks against the engine (C=Z4 Pauli class, Hermitian section i^{x.z} X^x Z^z = Aaronson-Gottesman)")
E4 = Ext(n, 4, bilinear_beta(n, 4, real_pauli_coeff(n, 2))); d4 = default_dict(E4)
L4 = {nm: ert_lift(E4, S, d4)[0] for nm, S in R.items()}
def herm(u): return E4.el(sum(((u >> 2*j) & 1) * ((u >> (2*j+1)) & 1) for j in range(n)), u)
assert all(E4.sq(herm(u)) == 0 for u in range(16))
def bits(u):
    return {"xa": u & 1, "za": (u >> 1) & 1, "xb": (u >> 2) & 1, "zb": (u >> 3) & 1}
AG = {"swap0": lambda b: b["xa"] & b["za"], "swap1": lambda b: b["xb"] & b["zb"],
      "couple": lambda b: b["xa"] & b["zb"] & (b["xb"] ^ b["za"] ^ 1)}
for nm, S in R.items():
    ok = all(L4[nm][herm(u)] == E4.mul[E4.el(2*AG[nm](bits(u)), 0)][herm(S[u])] for u in range(16))
    gH = [E4.cval(E4.mul[L4[nm][herm(u)]][E4.inv[herm(S[u])]]) // 2 for u in range(16)]
    print("  %-7s AG phase rule reproduced on all 16 Hermitian records: %s ; ANF degree in this section: %d" % (nm, ok, anf_degree(gH, 4)))

print("== (II) ontic: card cells + one extra F2 cell h, affine extensions of the card maps")
qm = QMTheory(n)
def ext_map(base, t, lam, k):
    def f(s):
        lo = s & 15; h = (s >> 4) & 1
        lo2 = base(lo) ^ (t if h else 0); h2 = h ^ (popc(lam & lo) & 1) ^ k
        return lo2 | (h2 << 4)
    return f
def bijective(f): return len({f(s) for s in range(32)}) == 32
cands = {}
for nm in ("swap0", "swap1", "couple"):
    b = onticmap(nm, n); L = []
    for t, lam, k in product(range(16), range(16), (0, 1)):
        f = ext_map(b, t, lam, k)
        if bijective(f): L.append(((t, lam, k), f))
    cands[nm] = L
print("  bijective affine extensions per card map:", {k: len(v) for k, v in cands.items()})
alph1 = ["swap0", "couple", "read0", "read1"]
ctrl = CardTheory(n, maps={"swap0": ext_map(onticmap("swap0", n), 0, 0, 0), "couple": ext_map(onticmap("couple", n), 0, 0, 0)},
                  hbit=True, init_h=None)
print("  control: h-decoupled extension == cards on", alph1, ":", equivalent(ctrl, CardTheory(n), alph1)[0],
      "; == QM:", equivalent(ctrl, qm, alph1)[0])
surv = Counter(); match1 = []
for init_h, rrh in product((0, 1, None), (False, True)):
    for (pa, fa), (pc, fc) in product(cands["swap0"], cands["couple"]):
        T = CardTheory(n, maps={"swap0": fa, "couple": fc}, hbit=True, init_h=init_h, read_refresh_h=rrh)
        if run_word(T, W6, "read1") != {1: 1} or run_word(T, W7, "read1") != {1: 1}: continue
        surv[(init_h, rrh)] += 1
        if equivalent(T, qm, alph1)[0]: match1.append((init_h, rrh, pa, pc))
print("  models passing both K-G1 witnesses (QM values), by (initial h, reads refresh h):", dict(surv))
print("  ... of which exactly equivalent to QM on every word over", alph1, ":", len(match1))
if match1:
    print("  examples (init_h, refresh, (t,lam,k)_swapA, (t,lam,k)_couple):", match1[:6])
    alph2 = ["swap0", "swap1", "couple", "read0", "read1"]; full = []
    for init_h, rrh, pa, pc in match1:
        fa = dict(cands["swap0"])[pa]; fc = dict(cands["couple"])[pc]
        for pb, fb in cands["swap1"]:
            T = CardTheory(n, maps={"swap0": fa, "swap1": fb, "couple": fc}, hbit=True, init_h=init_h, read_refresh_h=rrh)
            if equivalent(T, qm, alph2)[0]: full.append((init_h, rrh, pa, pb, pc))
    print("  extended by swap_B, exactly equivalent to QM on every word over", alph2, ":", len(full))
    if full: print("  examples:", full[:6])
