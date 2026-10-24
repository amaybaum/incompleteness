"""(a) Central extensions of V = F2^{2n} by C = Z_m with commutator (m/2) omega, by cocycle class.
n = 1: brute force over ALL normalized cocycles (m = 2: 2^9 functions; m = 4: 4^9), classes mod coboundaries.
n = 1, 2: the representatives beta_B = (m/2) [bilinear B, B + B^T = omega] (+ carry terms for m = 4), with the
class invariant (squares of lifts) shown to separate them; counts compared with |Ext(V, C)| = 2^{2n}."""
from g1lib import *
from itertools import product
import sys

def coboundary(f, N, m):
    return [[(f[u] + f[v] - f[u ^ v]) % m for v in range(N)] for u in range(N)]

def brute_n1(m):
    n = 1; N = 4; nz = [1, 2, 3]
    cocs = []
    for vals in product(range(m), repeat=9):
        b = [[0]*4 for _ in range(4)]
        k = 0
        for u in nz:
            for v in nz: b[u][v] = vals[k]; k += 1
        ok = all((b[u][v] + b[u ^ v][w] - b[v][w] - b[u][v ^ w]) % m == 0 for u in nz for v in nz for w in nz)
        if not ok: continue
        if any((b[u][v] - b[v][u] - (m//2)*omega(u, v, 1)) % m for u in nz for v in nz): continue
        cocs.append(tuple(tuple(r) for r in b))
    # classes mod coboundaries
    cobs = []
    for fv in product(range(m), repeat=3):
        f = [0] + list(fv); cobs.append(coboundary(f, N, m))
    cs = set(cocs); classes = []
    while cs:
        b = cs.pop(); cl = {b}
        for c in cobs:
            b2 = tuple(tuple((b[u][v] + c[u][v]) % m for v in range(N)) for u in range(N))
            cl.add(b2)
        cs -= cl; classes.append(sorted(cl)[0])
    return len(cocs), classes

def invariants(E):
    """isomorphism-type data: element-order histogram; squares of lifts of each u (class invariant)."""
    hist = {}
    for g in range(E.size): o = E.order(g); hist[o] = hist.get(o, 0) + 1
    sq = {u: sorted({E.cval(E.sq(E.el(a, u))) for a in range(E.m)}) for u in range(1, E.N)}
    return dict(sorted(hist.items())), sq

def ntype(hist, m, n):
    if m == 2 and n == 1: return {(1, 1), (2, 5), (4, 2)} == set(hist.items()) and "D4" or ("Q8" if hist.get(4) == 6 else "?")
    return ""

def reps(n, m):
    """representatives: m=2: beta0 + sum eps_i u_i v_i (diagonal); m=4: 2*beta0 + sum l_i u_i v_i (carry)."""
    out = []
    for eps in product((0, 1), repeat=2*n):
        c = real_pauli_coeff(n, m//2)
        for i in range(2*n): c[i][i] = (c[i][i] + (eps[i] if m == 2 else eps[i])) % m
        out.append((eps, bilinear_beta(n, m, c)))
    return out

if __name__ == "__main__":
    for m in (2, 4):
        ncoc, classes = brute_n1(m)
        print("== n=1, C=Z%d: normalized cocycles with commutator %d*omega: %d ; classes mod coboundary: %d" % (m, m//2, ncoc, len(classes)))
        for b in classes:
            E = Ext(1, m, [list(r) for r in b]); h, sq = invariants(E)
            rec = [u for u in range(1, 4) if E.involution_lifts(u)]
            lab = {1: "X", 2: "Z", 3: "Y"}
            print("   class rep beta(X,Z)=%d beta(Z,X)=%d diag(X,Z,Y)=(%d,%d,%d) | order hist %s %s | squares of lifts %s | recordable relations %s"
                  % (b[1][2], b[2][1], b[1][1], b[2][2], b[3][3], h, ntype(h, m, 1),
                     {lab[u]: s for u, s in sq.items()}, [lab[u] for u in rec]))

    for n in (1, 2):
        for m in (2, 4):
            rs = reps(n, m); invs = set(); rows = []
            for eps, b in rs:
                E = Ext(n, m, b)
                assert E.is_cocycle() and E.commutator_is(lambda u, v: (m//2)*omega(u, v, n))
                h, sq = invariants(E)
                key = tuple(tuple(sq[u]) for u in range(1, E.N)); invs.add(key)
                nrec = sum(1 for u in range(1, E.N) if E.involution_lifts(u))
                gens_rec = all(E.involution_lifts(1 << i) for i in range(2*n))
                rows.append((eps, h, nrec, gens_rec))
            print("== n=%d, C=Z%d: %d representatives, %d distinct square-invariants (=> pairwise inequivalent); |Ext(V,C)| = %d"
                  % (n, m, len(rs), len(invs), 2**(2*n)))
            types = {}
            for eps, h, nrec, gr in rows:
                types.setdefault(tuple(sorted(h.items())), []).append(eps)
            for t, l in types.items():
                print("   order histogram %s : %d classes" % (dict(t), len(l)))
            print("   classes in which every elementary relation (X_j, Z_j) is recordable (has an involutive lift):",
                  [eps for eps, h, nrec, gr in rows if gr])
            if n == 2 and m == 2:
                # Arf invariant of the quadratic refinement q(u) = beta(u,u)
                for eps, b in rs:
                    pass
                arf = {}
                for eps, b in rs:
                    E = Ext(n, m, b); q = [b[u][u] for u in range(E.N)]
                    a = 1 if sum(q) > E.N//2 else 0   # Arf = majority value of q
                    arf[a] = arf.get(a, 0) + 1
                print("   Arf invariant counts {0: plus-type 2^{1+4}_+, 1: minus-type}:", arf)
