"""Node 1b (d): AND-OR search for a DETERMINISTIC data channel by finite protocols with heralding and
feed-forward. Exact Gaussian-rational arithmetic (reuses det_solver's arithmetic, permutations and tests).

Object tracked: the branch operator M from the data token (token 0, arbitrary input) into the register
(data + ancillas), a 2^n x 2 matrix stored as its two columns, canonicalised jointly up to a scalar. The start
is M0 = I_data (x) |0...0>_anc (configuration ancillas), or another stated start. Moves: a native permutation
generator (deterministic) or a Lueders test of one token in a Pauli basis (branching; every positive-weight
outcome must win). A leaf wins when M is proportional to U (x) |a> for the target U and some ancilla vector a,
i.e. after discarding the ancillas every configuration-Kraus branch is proportional to U (or zero). Least fixed
point on the explored graph: a reported win is a real finite protocol; a loss is relative to the bound."""
import sys, itertools
sys.path.insert(0, '.')
import det_solver as D
from det_solver import F, c, add, mul, neg, inv, conj, Z0, ONE, I_, BASES, bit, apply_perm, perm_gens, test_outcomes

def canonM(cols):
    flat = cols[0] + cols[1]
    for a in flat:
        if a != Z0:
            ia = inv(a)
            return (tuple(mul(e, ia) for e in cols[0]), tuple(mul(e, ia) for e in cols[1]))
    return None

def test_M(M, j, basis, n):
    outs = []
    for w in BASES[basis]:
        cols = []
        for col in M:
            new = [Z0]*len(col)
            for i in range(len(col)):
                if bit(i, j, n) != 0: continue
                i1 = i | (1 << (n-1-j))
                amp = add(mul(conj(w[0]), col[i]), mul(conj(w[1]), col[i1]))
                new[i] = add(new[i], mul(amp, w[0])); new[i1] = add(new[i1], mul(amp, w[1]))
            cols.append(tuple(new))
        cm = canonM(cols)
        if cm is not None: outs.append(cm)
    return outs

def is_target(M, n, U):
    # M = U (x) a  <=>  for every ancilla configuration r: (M[(0,r)], M[(1,r)]) columns equal U * a_r
    # i.e. the 2x2 block B_r with B_r[x][y] = M_col_y[(x, r)] is proportional to U, with one common scalar family a_r
    na = n - 1; ref = None; nz = False
    for r in range(2**na):
        B = [[M[y][(x << na) | r] for y in range(2)] for x in range(2)]
        # find scalar s with B = s U
        s = None
        for x in range(2):
            for y in range(2):
                if U[x][y] != Z0 and s is None: s = mul(B[x][y], inv(U[x][y]))
        if s is None: return False
        for x in range(2):
            for y in range(2):
                if B[x][y] != mul(s, U[x][y]): return False
        if s != Z0: nz = True
    return nz

def solve(n, bases, U, start_anc=None, max_states=100000, test_data=True):
    gens = perm_gens(n, False)
    na = n - 1
    anc = start_anc if start_anc is not None else tuple(ONE if i == 0 else Z0 for i in range(2**na))
    cols = []
    for y in range(2):
        col = [Z0]*(2**n)
        for r in range(2**na): col[(y << na) | r] = anc[r]
        cols.append(tuple(col))
    s0 = canonM(cols)
    seen = {s0}; order = [s0]; edges = {}; q = 0; tr = False
    toks = range(n) if test_data else range(1, n)
    while q < len(order):
        s = order[q]; q += 1
        pm = {g: canonM([apply_perm(col, p) for col in s]) for g, p in gens.items()}
        tm = {}
        for j in toks:
            for b in bases:
                o = test_M(s, j, b, n)
                if o: tm[(j, b)] = o
        edges[s] = (pm, tm)
        for t in list(pm.values()) + [o for v in tm.values() for o in v]:
            if t not in seen:
                if len(seen) >= max_states: tr = True; continue
                seen.add(t); order.append(t)
    win = {s for s in order if is_target(s, n, U)}
    changed = True
    while changed:
        changed = False
        for s in order:
            if s in win or s not in edges: continue
            pm, tm = edges[s]
            if any(t in win for t in pm.values()) or any(len(o) >= 2 and all(x in win for x in o) for o in tm.values()):
                win.add(s); changed = True
    return s0 in win, len(order), tr

Zt = ((ONE, Z0), (Z0, neg(ONE))); Xt = ((Z0, ONE), (ONE, Z0)); It = ((ONE, Z0), (Z0, ONE))
# R_x(pi/2) up to scalar: [[1, -i], [-i, 1]]
Rx = ((ONE, neg(I_)), (neg(I_), ONE)); Sg = ((ONE, Z0), (Z0, I_))
MINUS = (ONE, neg(ONE)); MINUS2 = (ONE, neg(ONE), Z0, Z0)
rows = [
    ('POS  n=2 target I (trivial)', 2, 'XYZ', It, None, True),
    ('POS  n=2 target X (native correction)', 2, 'XYZ', Xt, None, True),
    ('POS  n=2 target R_x(pi/2) (TU layer-flow gadget)', 2, 'XYZ', Rx, None, True),
    ('POS  n=2 target Z with ancilla started in |-> (kickback, B7)', 2, 'XYZ', Zt, MINUS, True),
    ('NEG  n=2 target Z, configuration tests only', 2, 'Z', Zt, None, False),
    ('MAIN n=2 target Z, Pauli Lueders tests, feed-forward', 2, 'XYZ', Zt, None, False),
    ('MAIN n=2 target S, Pauli Lueders tests, feed-forward', 2, 'XYZ', Sg, None, False),
    ('MAIN n=3 target Z, Pauli Lueders tests, feed-forward', 3, 'XYZ', Zt, None, False),
]
fails = 0
for label, n, bases, U, st, expect in rows:
    if st is not None and n == 3: st = st + (Z0, Z0)
    got, ns, tr = solve(n, bases, U, st, max_states=60000)
    ok = got == expect; fails += 0 if ok else 1
    print('%s %-62s states=%-6d truncated=%-5s deterministic=%s' % ('PASS' if ok else 'FAIL', label, ns, tr, got), flush=True)
print('SUMMARY fails', fails)
sys.exit(1 if fails else 0)
