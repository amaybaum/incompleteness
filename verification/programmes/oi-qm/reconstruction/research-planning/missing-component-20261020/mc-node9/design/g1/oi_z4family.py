"""(I-d) C=Z4 Pauli class, n=2: can one section f: V -> Z4 make the phase update of swap_A, swap_B and couple
simultaneously additive (a homomorphism V -> Z4), for each choice of trivial / inverting action on C per operation?
Exact: f = f1 + 2 f2; mod-2 condition enumerated over all f1 (2^15), the mod-4 remainder solved as an F2 linear
system in f2 (Gaussian elimination)."""
from g1lib import *
from itertools import product
n = 2; R = card_relmaps(n); names = ["swap0", "swap1", "couple"]
E = Ext(n, 4, bilinear_beta(n, 4, real_pauli_coeff(n, 2)))
base = {}
for nm in names:
    base[(nm, 1)] = E.lifts(R[nm], 1)[0]; base[(nm, -1)] = E.lifts(R[nm], -1)[0]
g0 = {k: [E.cval(phi[E.el(0, u)]) for u in range(16)] for k, phi in base.items()}
pairs = [(u, v) for u in range(1, 16) for v in range(1, 16)]
def delta(g): return [(g[u ^ v] - g[u] - g[v]) % 4 for u, v in pairs]
def gf(nm, c, f): S = R[nm]; return [(g0[(nm, c)][u] + c*f[u] - f[S[u]]) % 4 for u in range(16)]
# linear map f2 -> (delta(gf with f=2 f2)/2 mod 2) is F2-linear; build its matrix columns
def f2_columns(nm, c):
    cols = []
    for i in range(15):
        f = [0]*16; f[i+1] = 2
        cols.append([x // 2 for x in delta([(c*f[u] - f[R[nm][u]]) % 4 for u in range(16)])])
    return cols
def solvable(cols_list, rhs_list):
    rows = []   # each equation: (bitmask over 15 unknowns, rhs bit)
    for cols, rhs in zip(cols_list, rhs_list):
        for e in range(len(rhs)):
            mask = 0
            for i in range(15):
                if cols[i][e]: mask |= 1 << i
            rows.append((mask, rhs[e]))
    piv = {}
    for mask, r in rows:
        for b in sorted(piv, reverse=True):
            if (mask >> b) & 1: pm, pr = piv[b]; mask ^= pm; r ^= pr
        if mask: piv[mask.bit_length()-1] = (mask, r)
        elif r: return False
    return True
for cacts in product((1, -1), repeat=3):
    cols = [f2_columns(nm, c) for nm, c in zip(names, cacts)]
    nsol1 = 0; nsol = 0
    for fv in range(1 << 15):
        f1 = [0] + [(fv >> i) & 1 for i in range(15)]
        ds = [delta(gf(nm, c, f1)) for nm, c in zip(names, cacts)]
        if any(x % 2 for dd in ds for x in dd): continue
        nsol1 += 1
        # need delta(g_{f1}) + delta(g_{2 f2}) = 0 mod 4  ->  F2 system  M f2 = delta(g_{f1})/2
        if solvable(cols, [[x // 2 for x in dd] for dd in ds]): nsol += 1
    print("action on C (swapA, swapB, couple) = %s: f1 passing mod 2: %d ; f1 completing to an additive section: %d"
          % (tuple("triv" if c == 1 else "inv" for c in cacts), nsol1, nsol))
print("-- single operations (control: n=1 found additive inverting swap lifts, so swap alone + inverting must be solvable)")
def additive(g): return all((g[u ^ v] - g[u] - g[v]) % 4 == 0 for u in range(16) for v in range(16))
for nm in names:
    for c in (1, -1):
        cols = [f2_columns(nm, c)]; nsol = 0; witness = None
        for fv in range(1 << 15):
            f1 = [0] + [(fv >> i) & 1 for i in range(15)]
            dd = delta(gf(nm, c, f1))
            if any(x % 2 for x in dd): continue
            if solvable(cols, [[x // 2 for x in dd]]):
                nsol += 1
                if witness is None:
                    # explicit completion by brute force over f2 restricted search (verify exactly)
                    for f2v in range(1 << 15):
                        f = [(f1[u] + 2*((f2v >> (u-1)) & 1 if u else 0)) % 4 for u in range(16)]
                        if additive(gf(nm, c, f)): witness = f; break
        print("  %-7s %s on C: f1 completing to an additive section: %d ; explicit verified section: %s"
              % (nm, "triv" if c == 1 else "inv ", nsol, witness))
print("-- pairs of operations")
from itertools import combinations
for pair_ in combinations(names, 2):
    for cacts in product((1, -1), repeat=2):
        cols = [f2_columns(nm, c) for nm, c in zip(pair_, cacts)]; nsol = 0
        for fv in range(1 << 15):
            f1 = [0] + [(fv >> i) & 1 for i in range(15)]
            ds = [delta(gf(nm, c, f1)) for nm, c in zip(pair_, cacts)]
            if any(x % 2 for dd in ds for x in dd): continue
            if solvable(cols, [[x // 2 for x in dd] for dd in ds]): nsol += 1
        print("  %s with %s on C: f1 completing to a common additive section: %d" % (pair_, tuple("triv" if c == 1 else "inv" for c in cacts), nsol))
