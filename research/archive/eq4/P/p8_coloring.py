"""EQ4-P probe p8 -- twisted network positivity (the coloring lemma) and the maximality certificate, exact.

Usage:  python3 -I -B p8_coloring.py <base>/verification/lean-mathlib/OIBridge
Imports only the own library eq4_lib.py (and sympy for two small symbolic identities).

Z := { X on three tokens : PT_1(X), PT_2(X), PT_3(X) are PSD }  (so PT_S(X) is PSD for every S with |S| in {1, 2}).
Coloring lemma (written, NOTES N3.4): in a closed KT network (each token shared by one state node and one effect node)
whose nodes are one-token PSD operators, two-token PSD operators and elements of Z, choose a token set X meeting every
two-token node in 0 or 2 tokens and every Z node in 1 or 2 tokens (always possible: contract the two-token nodes to
edges; an edge 2-colouring of a multigraph with no monochromatic vertex of degree 3 exists by an Euler-tour argument);
applying PT_X to every node leaves the value unchanged and makes every node PSD, so the value is >= 0.
Maximality certificate (written): nu = I - 2 GHZ+ + 4 GHZ- (GHZ-diagonal; lambda = (-1, 5, 1, 1, 1, 1, 1, 1)) lies in
BS* and is nonnegative on Z (its pairing with every GHZ-diagonal element of Z is a nonnegative combination of the
defining inequalities), so nu is in T(cone(BS u Z)*); with Z the Pauli Z on one token, <nu, Z nu> < 0.  Hence no
co-self-dual K3 lies inside cone(BS u Z): it would contain nu and Z nu.

DECISION RULE (fixed before the first run; rules, not expected numbers).  VERDICT `P8-COLORING-EXACT` iff all pass:
  K  transcription control.
  Z  (Z1) W3 is in Z (PT_1, PT_2, PT_3 of W3 PSD; W3 itself not PSD; its pair marginals PSD); (Z2) PT_1(Ad(A (x) B (x)
     C) X) = Ad(conj(A) (x) B (x) C)(PT_1 X) on all 64 units (3 random rational filters), and PT_j(Ad(k) W3) is PSD for
     3 random rational product filters k and j = 1, 2, 3 (Z is closed under local filters); (Z3) for a GHZ-diagonal
     operator with symbolic populations P_b and coherences C_b, PT_j acts block-diagonally with blocks
     [[P_b, C_{pi_j(b)}], [C_{pi_j(b)}, P_b]]/2, pi_1(b) = complement of b, pi_2 flips the first bit, pi_3 the second
     (symbolic), so Z^GD = { |C_b'| <= P_b for all b != b' }.
  C  (C1) for the networks theta (Bell links and random PSD links), ring, K4 (both splits) and the 3 x 3 Latin square,
     with nodes W3 or Ad(k) W3 (and random PSD pair links), a colouring X exists (exhaustive search), PT_X makes every
     node PSD (exact) and leaves the value unchanged; the value is >= 0; (C2) countercontrol: the theta network with a
     GHZ node and a W3 node admits no colouring and its value is negative.
  M  (M1) nu is in BS* (nu - 4 GHZ- = 2 W3 with W3 in BS*: p1 P1; GHZ- PSD); (M2) for symbolic z in Z^GD the pairing
     2<nu, z> = 4 P_00 + 2 sum_{b != 00} (P_b - C_00) (a nonnegative combination of the Z^GD inequalities; symbolic);
     (M3) <nu, Z nu> < 0 and Z nu is the image of nu under the Pauli Z on token 0 (exact).
  P  record (not a pass condition beyond exactness): kappa = 1/2 + |000><111| + h.c. is in BS*, is not PSD after any
     partial transpose (all 8 subsets), pairs negatively with nu, and its Bell-link networks with W3 are reported.
"""
import itertools
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, __file__.rsplit("/", 1)[0] if "/" in __file__ else ".")
import sympy as sp  # noqa: E402

import eq4_lib as L  # noqa: E402

BASE = sys.argv[1]
rep = L.Report("p8_coloring")
rng = random.Random(20261009 + 8)
rep.check("K0 transcription control", L.transcription_control(BASE)[0])
X3 = (0, 1, 2)
W = L.w3(X3)


def inZ(Xop):
    return all(L.psd(L.ptranspose(Xop, [q]))[0] for q in Xop.qs)


marg_ok = all(L.psd(L.ptrace(W, keep))[0] for keep in ((0, 1), (0, 2), (1, 2)))
rep.check("Z1 W3 is in Z (PT on each single token PSD), W3 is not PSD, its pair marginals are PSD",
          inZ(W) and not L.psd(W)[0] and marg_ok)


def rmat():
    while True:
        M = [[L.G(Fr(rng.randint(-3, 3), rng.randint(1, 3)), Fr(rng.randint(-2, 2), rng.randint(1, 3)))
              for _ in range(2)] for _ in range(2)]
        if not (M[0][0] * M[1][1] - M[0][1] * M[1][0]).is_zero():
            return M


def conjm(M):
    return [[x.conj() for x in r] for r in M]


ok_z2 = True
for _ in range(3):
    A, B, C = rmat(), rmat(), rmat()
    k = L.tensor(L.op(A, (0,)), L.op(B, (1,)), L.op(C, (2,)))
    kc = L.tensor(L.op(conjm(A), (0,)), L.op(B, (1,)), L.op(C, (2,)))
    for _, u in L.units(X3):
        ok_z2 &= L.ptranspose(L.ad(k, u), [0]) == L.ad(kc, L.ptranspose(u, [0]))
    ok_z2 &= inZ(L.ad(k, W))
rep.check("Z2 PT_1 o Ad(A (x) B (x) C) = Ad(conj A (x) B (x) C) o PT_1 on all units, and Ad(k) W3 is in Z (3 random "
          "rational product filters)", ok_z2)
# Z3 symbolic: GHZ-diagonal operator from (P_b, C_b)
Ps = sp.symbols("P0:4", real=True)
Cs = sp.symbols("C0:4", real=True)
fib = [(0, 0), (0, 1), (1, 0), (1, 1)]


def gd_sym():
    M = sp.zeros(8, 8)
    for i, (b1, b2) in enumerate(fib):
        lo = 4 * 0 + 2 * b1 + b2
        hi = 4 * 1 + 2 * (1 - b1) + (1 - b2)
        M[lo, lo] += Ps[i] / 2
        M[hi, hi] += Ps[i] / 2
        M[lo, hi] += Cs[i] / 2
        M[hi, lo] += Cs[i] / 2
    return M


def pt_sym(M, j):
    out = sp.zeros(8, 8)
    for r in range(8):
        for c in range(8):
            rb = [(r >> (2 - q)) & 1 for q in range(3)]
            cb = [(c >> (2 - q)) & 1 for q in range(3)]
            rb[j], cb[j] = cb[j], rb[j]
            out[4 * rb[0] + 2 * rb[1] + rb[2], 4 * cb[0] + 2 * cb[1] + cb[2]] = M[r, c]
    return out


Mgd = gd_sym()
ok_z3 = True
pis = {0: lambda b: (1 - b[0], 1 - b[1]), 1: lambda b: (1 - b[0], b[1]), 2: lambda b: (b[0], 1 - b[1])}
for j in range(3):
    PT = pt_sym(Mgd, j)
    expect = sp.zeros(8, 8)
    for i, b in enumerate(fib):
        lo = 2 * b[0] + b[1]
        hi = 4 + 2 * (1 - b[0]) + (1 - b[1])
        partner = fib.index(pis[j](b))
        expect[lo, lo] += Ps[i] / 2
        expect[hi, hi] += Ps[i] / 2
        expect[lo, hi] += Cs[partner] / 2
        expect[hi, lo] += Cs[partner] / 2
    ok_z3 &= (PT - expect).applyfunc(sp.expand).is_zero_matrix
rep.check("Z3 PT_j of a GHZ-diagonal operator is block-diagonal with blocks [[P_b, C_pi_j(b)],[C_pi_j(b), P_b]]/2, "
          "pi_1 = complement, pi_2, pi_3 = single bit flips (symbolic): Z^GD = { |C_b'| <= P_b, b != b' }", ok_z3)


# ------------------------------------------------------------------------------------------------ C coloring on networks
def find_coloring(nodes, tokens):
    """nodes: list of (kind, tokens) with kind in {'Z', 'P2', 'P1', 'Q'}; returns a feasible X or None."""
    for bits in itertools.product((0, 1), repeat=len(tokens)):
        Xs = {t for t, bt in zip(tokens, bits) if bt}
        ok = True
        for kind, tk in nodes:
            m = len(Xs & set(tk))
            if kind == "Z" and m not in (1, 2):
                ok = False
            elif kind == "P2" and m not in (0, 2):
                ok = False
            elif kind == "Q" and m not in (0, len(tk)):
                ok = False
            if not ok:
                break
        if ok:
            return Xs
    return None


def run_network(states, effects):
    """states/effects: lists of (kind, Op).  Returns (value, coloring found, all-PSD after PT_X, value preserved)."""
    allnodes = states + effects
    tokens = sorted({t for _, o in allnodes for t in o.qs})
    Xs = find_coloring([(k, o.qs) for k, o in allnodes], tokens)
    S = L.tensor(*[o for _, o in states])
    E = L.tensor(*[o for _, o in effects])
    val = L.pair(E, S)
    if Xs is None:
        return val, False, False, False
    Sx = L.tensor(*[L.ptranspose(o, list(Xs & set(o.qs))) for _, o in states])
    Ex = L.tensor(*[L.ptranspose(o, list(Xs & set(o.qs))) for _, o in effects])
    allpsd = all(L.psd(L.ptranspose(o, list(Xs & set(o.qs))))[0] for _, o in allnodes)
    return val, True, allpsd, L.pair(Ex, Sx) == val


def zel(qs):
    """W3 or a random SLOCC image of it on the token tuple qs."""
    base = L.reorder(L.relabel(W, {0: qs[0], 1: qs[1], 2: qs[2]}), qs)
    if rng.random() < 0.5:
        return base
    k = L.tensor(*[L.op(rmat(), (q,)) for q in qs])
    return L.ad(k, base)


def rpair(a, b):
    return L.rand_psd(rng, (a, b), rank=rng.choice([1, 2]))


results = []
ok_c1 = True
for trial in range(2):
    lk = [("P2", L.phi_plus(0, 3)), ("P2", L.phi_plus(1, 4)), ("P2", L.phi_plus(2, 5))] if trial == 0 else \
        [("P2", rpair(0, 3)), ("P2", rpair(1, 4)), ("P2", rpair(2, 5))]
    results.append(("theta%d" % trial,) + run_network([("Z", zel((0, 1, 2))), ("Z", zel((3, 4, 5)))], lk))
results.append(("ring",) + run_network([("Z", zel((0, 1, 3))), ("Z", zel((2, 4, 5)))],
                                       [("Z", zel((0, 1, 2))), ("Z", zel((3, 4, 5)))]))
for sp_ in (0, 1):
    xq = (12, 1, 3) if sp_ == 0 else (12, 1, 4)
    yq = (13, 2, 4) if sp_ == 0 else (13, 2, 3)
    results.append(("K4-%d" % sp_,) + run_network([("Z", zel((10, 1, 2))), ("Z", zel((11, 3, 4))), ("P2", rpair(12, 13))],
                                                  [("P2", rpair(10, 11)), ("Z", zel(xq)), ("Z", zel(yq))]))
rows = [(3 * i, 3 * i + 1, 3 * i + 2) for i in range(3)]
cols = [(j, 3 + j, 6 + j) for j in range(3)]
results.append(("Latin",) + run_network([("Z", zel(r)) for r in rows], [("Z", zel(c)) for c in cols]))
for name, val, found, allpsd, same in results:
    ok_c1 &= found and allpsd and same and val.im == 0 and val.re >= 0
rep.check("C1 colourings exist and certify positivity: " + ", ".join("%s = %s" % (r[0], r[1]) for r in results), ok_c1)
gval, gfound, _, _ = run_network([("Q", L.ghz((0, 1, 2))), ("Z", L.reorder(L.relabel(W, {0: 3, 1: 4, 2: 5}),
                                                                          (3, 4, 5)))],
                                 [("P2", L.phi_plus(0, 3)), ("P2", L.phi_plus(1, 4)), ("P2", L.phi_plus(2, 5))])
rep.check("C2 countercontrol: theta with a GHZ node and a W3 node admits no colouring; value %s < 0" % gval,
          (not gfound) and gval.im == 0 and gval.re < 0)

# ------------------------------------------------------------------------------------------------ M maximality
G = [L.ket_op([1, 0, 0, 0, 0, 0, 0, s], X3).scale(Fr(1, 2)) for s in (1, -1)]       # GHZ+, GHZ-


def gd_op(lam):
    """GHZ-diagonal operator from lambda over labels (s, b), order (+,00),(-,00),(+,01),(-,01),(+,10),(-,10),(+,11),(-,11)."""
    out = L.Op(X3, {})
    i = 0
    for (b1, b2) in fib:
        for s in (1, -1):
            v = [0] * 8
            v[2 * b1 + b2] = 1
            v[4 + 2 * (1 - b1) + (1 - b2)] = s
            out = out + L.ket_op(v, X3).scale(Fr(lam[i], 2))
            i += 1
    return out


nu = gd_op([-1, 5, 1, 1, 1, 1, 1, 1])
rep.check("M1 nu = I - 2 GHZ+ + 4 GHZ- (lambda = (-1,5,1,1,1,1,1,1)); nu - 4 GHZ- = 2 W3 (in BS*, p1 P1) and GHZ- PSD: "
          "nu is in BS*", nu == L.identity(X3) - G[0].scale(2) + G[1].scale(4)
          and nu - G[1].scale(4) == W.scale(2) and L.psd(G[1])[0])
# M2 symbolic: nu has P_00 = 4, C_00 = -6, P_b = 2, C_b = 0 (b != 00); 2<nu,z> = sum_b (P^nu P^z + C^nu C^z)
pz = sp.symbols("q0:4", real=True)
cz = sp.symbols("d0:4", real=True)
nuP, nuC = [4, 2, 2, 2], [-6, 0, 0, 0]
two_ip = sum(nuP[i] * pz[i] + nuC[i] * cz[i] for i in range(4)) / 2 * 2
cert = 4 * pz[0] + 2 * sum(pz[i] - cz[0] for i in (1, 2, 3))
rep.check("M2 2<nu, z> = 4 P_00 + 2 sum_{b != 00}(P_b - C_00) (symbolic): a nonnegative combination of the Z^GD "
          "inequalities P_00 >= 0, P_b >= C_00", sp.expand(two_ip - cert) == 0)
Zop = L.op(L.SZ, (0,))
Znu = L.ad(Zop, nu)
ip_ = L.pair(nu, Znu)
rep.check("M3 Z nu (Pauli Z on token 0) is GHZ-diagonal with lambda = (5,-1,1,...); <nu, Z nu> = %s < 0" % ip_,
          Znu == gd_op([5, -1, 1, 1, 1, 1, 1, 1]) and ip_.im == 0 and ip_.re < 0)

# ------------------------------------------------------------------------------------------------ P kappa record
kap = L.identity(X3).scale(Fr(1, 2)) + L.Op(X3, {(0, 7): L.ONE, (7, 0): L.ONE})
pt_any = any(L.psd(L.ptranspose(kap, list(S)))[0] for r in range(4) for S in itertools.combinations(X3, r))
lkB = L.tensor(L.phi_plus(0, 3), L.phi_plus(1, 4), L.phi_plus(2, 5))
th_k = L.pair(lkB, L.tensor(kap, L.reorder(L.relabel(W, {0: 3, 1: 4, 2: 5}), (3, 4, 5))))
rep.note("P kappa = 1/2 + |000><111| + h.c.: kappa - G+ = 1/2 - G- (a W3-type element of BS*); PSD after some partial "
         "transpose: %s; <kappa, nu> = %s; Bell theta(kappa, W3) = %s" % (pt_any, L.pair(kap, nu), th_k))
rep.check("P record is exact: kappa - GHZ+ = 1/2 - GHZ- and kappa is not PSD after any partial transpose",
          kap - G[0] == L.identity(X3).scale(Fr(1, 2)) - G[1] and not pt_any)

rep.verdict("P8-COLORING-EXACT")
