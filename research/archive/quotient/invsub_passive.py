"""Largest W-invariant subspace of passive effects (futures of length <= Le) on pasts <= 8, exact (n = 8 counts).
W* e = 'idle then e' = sum over the next outcome (passivity), i.e. the future marginalized over its first bit."""
import sys
from fractions import Fraction as Fr
from itertools import product
sys.path.insert(0, '.'); sys.path.insert(0, '../rank')
from lattice_rank import record_counts
from oistage_helpers import rank, nullspace
from invsub import reduce_basis, in_span
rule = sys.argv[1]; Le = int(sys.argv[2]); n = 8
arr = record_counts(n, rule).reshape([2] * (2 * n))
pasts0 = [h for l in range(n + 1) for h in product((0, 1), repeat=l)]
def val(h, f):
    sl = [slice(None)] * (2 * n)
    for i, b in enumerate(h): sl[n - len(h) + i] = b
    for i, b in enumerate(f): sl[n + i] = b
    return int(arr[tuple(sl)].sum())
pasts = [h for h in pasts0 if val(h, ()) > 0]
W = [val(h, ()) for h in pasts]
futs = [f for l in range(Le + 1) for f in product((0, 1), repeat=l)]
row = {f: [Fr(val(h, f), W[i]) for i, h in enumerate(pasts)] for f in futs}
dom = [f for f in futs if len(f) <= Le - 1]
print(f'SETUP {rule}: passive effects <= {Le} on pasts <= 8: rank = {rank([row[f] for f in futs])}', flush=True)
# W* f = (0,)+f + (1,)+f
Wrow = {f: [a + b for a, b in zip(row[(0,) + f], row[(1,) + f])] for f in dom}
rels = nullspace([row[f] for f in dom])
well = all(all(x == 0 for x in [sum((c[i] * Wrow[f][j] for i, f in enumerate(dom)), Fr(0)) for j in range(len(pasts))]) for c in rels)
print(f'WELLDEF {rule}: {well} ({len(rels)} relations)', flush=True)
nd = len(dom)
Uf = [[Fr(int(i == j)) for j in range(nd)] for i in range(nd)]
ev = lambda c: [sum((c[i] * row[dom[i]][j] for i in range(nd)), Fr(0)) for j in range(len(pasts))]
wv = lambda c: [sum((c[i] * Wrow[dom[i]][j] for i in range(nd)), Fr(0)) for j in range(len(pasts))]
it = 0
while True:
    it += 1
    UB = reduce_basis([ev(c) for c in Uf]); dimU = len(UB)
    red = []
    for c in Uf:
        v = wv(c)
        for (piv, b) in UB:
            if v[piv] != 0:
                f_ = v[piv] / b[piv]; v = [x - f_ * y for x, y in zip(v, b)]
        red.append(v)
    ker = nullspace(red) if red else []
    newUf = [[sum((t[k] * Uf[k][i] for k in range(len(Uf))), Fr(0)) for i in range(nd)] for t in ker]
    dimNew = len(reduce_basis([ev(c) for c in newUf]))
    print(f'ITER {rule} {it}: dim U = {dimU} -> {dimNew}', flush=True)
    if dimNew == dimU or dimNew == 0:
        Uf = newUf if dimNew < dimU else Uf
        break
    Uf2, B = [], []
    for c in newUf:
        r = ev(c)
        if not in_span(r, B):
            Uf2.append(c); B = reduce_basis([b for (_, b) in B] + [r])
    Uf = Uf2
UB = reduce_basis([ev(c) for c in Uf])
unit = [Fr(1)] * len(pasts)
print(f'INV {rule}: largest W-invariant subspace of passive effects(<= {Le-1}) on pasts<=8: dim = {len(UB)}; unit in U: {in_span(unit, UB)}', flush=True)
# ---- structure of U: basis (as combinations of futures), induced W matrix, characteristic polynomial
import sympy as sp
Urows = [ev(c) for c in Uf]
UB2 = reduce_basis(Urows)
basis_c = []
B = []
for c in Uf:
    r = ev(c)
    if not in_span(r, B):
        basis_c.append(c); B = reduce_basis([b for (_, b) in B] + [r])
for k, c in enumerate(basis_c):
    terms = [(dom[i], c[i]) for i in range(nd) if c[i] != 0]
    print(f'UBASIS {rule} {k}:', ' + '.join(f'({co})*[{"".join(map(str, f)) or "()"}]' for f, co in terms[:12]) + (' ...' if len(terms) > 12 else ''))
# induced W on U: express W*(basis_k) in the basis
from invsub import coords
brows = [ev(c) for c in basis_c]
Wm = []
for c in basis_c:
    co = coords(wv(c), brows)
    Wm.append(co)
if all(co is not None for co in Wm):
    Mx = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in Wm]).T
    lam = sp.symbols('lam')
    print(f'WMAT {rule}: induced W on U (dim {len(basis_c)}) char poly = {sp.factor(Mx.charpoly(lam).as_expr())}')
    print(f'WMAT {rule}: eigenvalues = {Mx.eigenvals()}')
