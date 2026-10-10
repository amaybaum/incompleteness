"""A37 read-only census: every Dita factorization of the certified stratum point SIG = F4(z) x F4(w) found by A36's
exhaustive search (all block shapes 4x4, 8x2, 2x8; column and row forms), with its index maps and factors; then the
orbits of these factorizations under the certified stabilizer of SIG in G_ext (order 1024) and under transposition
(SIG is symmetric), which are the deduplicated census."""
import itertools, sys, time
src = open('a37/probe36.py', encoding='utf-8').read()
exec(src[:src.index("print('== 1.")])                                                   # objects: G, F4, kron, SIG, W, U60, P ...
exec(src[src.index('def is_unitary_s'):src.index('PT = [list(c)')])                       # section 2 search
S4 = list(itertools.permutations(range(4)))
exec(src[src.index('def deph(M)'):src.index('G4 = []')])                                   # deph, key
sec5 = src[src.index("X4, Y4 = F4(z), F4(w)"):src.index("check('conjugacy classes")]
sec5 = sec5.replace("check(", "(lambda *a, **k: None)(")                                  # keep the constructions, drop the checks
exec(sec5)                                                                                 # ops, order, elems (the stabilizer), apply
SIGT = [list(c) for c in zip(*SIG)]
print('SIG symmetric:', SIG == SIGT, '; stabilizer order', len(elems))

def twist(H, cp, rows, X, Y, m, n):
    """the twist D[c][b] = H[row(0,b)][col(c,0)] / (X[0][c] Y_c[b][0]); exact check that H is the Dita matrix of (X, Y, D)"""
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    D = [[None] * n for _ in range(m)]
    for c in range(m):
        for b in range(n):
            x = X[0][c] * Y[c][b][0]; h = H[row[(0, b)]][col[(c, 0)]]
            # divide exactly: h / x with x unimodular (scaled): h * conj(x) / |x|^2
            nx = x.norm2(); q = h * x.conj(); D[c][b] = G(q.a / nx, q.b / nx)
    ok = all(H[row[(a, b)]][col[(c, d)]] == X[a][c] * D[c][b] * Y[c][b][d] for a in range(m) for b in range(n) for c in range(m) for d in range(n))
    return D, ok

facts = []   # (kind, (m, n), colblocks, rowclasses, X, Y, D)
for (m, n) in ((4, 4), (8, 2), (2, 8)):
    for kind, H in (('column', SIG), ('row', SIGT)):
        for cp, rows, ok, X, Y in dita_orientations(H, m, n):
            if not ok: continue
            D, dok = twist(H, cp, rows, X, Y, m, n)
            assert dok, (kind, m, n, cp)
            facts.append((kind, (m, n), tuple(cp), tuple(rows), X, Y, D))
print('exact factorizations found:', len(facts))
for kind, mn, cp, rows, X, Y, D in facts:
    print('  %-6s %dx%d  column blocks %s  row classes %s' % (kind, mn[0], mn[1], cp, rows))

# the stabilizer as pairs (row permutation, column permutation, conj, transpose) on the 16-point carrier
def perm_pair(e):
    """decompose the entry permutation: product form p[i*16+j] = rp(i)*16 + cq(j), or transposed form
    p[i*16+j] = phi(j)*16 + psi(i); returns (form, first map on rows i, second map on columns j)"""
    p, s = e
    rp = [p[i * 16] // 16 for i in range(16)]; cq = [p[j] % 16 for j in range(16)]
    if all(p[i * 16 + j] == rp[i] * 16 + cq[j] for i in range(16) for j in range(16)): return 'product', tuple(rp), tuple(cq)
    psi = [p[i * 16] % 16 for i in range(16)]; phi = [p[j] // 16 for j in range(16)]
    assert all(p[i * 16 + j] == phi[j] * 16 + psi[i] for i in range(16) for j in range(16)), 'neither form'
    return 'transposed', tuple(psi), tuple(phi)
elems_t = []
for op, (A, B) in ops.items():
    for g1 in A:
        for g2 in B:
            elems_t.append((op, action(op, g1, g2)))
def canon(kind, mn, cp, rows):
    cpc = tuple(sorted(tuple(sorted(b)) for b in cp)); rc = tuple(sorted(tuple(sorted(r)) for r in rows))
    return (kind, mn, cpc, rc)
def act_on(kind, mn, cp, rows, op, e):
    """transport a structure through a stabilizer element. Column form (cp, rows) = column blocks and row classes of H;
    row form (cp, rows) = column blocks and row classes of H^T, i.e. row blocks and column classes of H.
    A product element sends entry (i, j) to (rp(i), cq(j)); a transposed element sends it to (phi(j), psi(i))."""
    form, f1, f2 = perm_pair(e)
    if form == 'product':
        rp, cq = f1, f2
        if kind == 'column': return canon('column', mn, [[cq[j] for j in b] for b in cp], [[rp[i] for i in r] for r in rows])
        return canon('row', mn, [[rp[i] for i in b] for b in cp], [[cq[j] for j in r] for r in rows])
    psi, phi = f1, f2
    if kind == 'column': return canon('row', mn, [[phi[j] for j in b] for b in cp], [[psi[i] for i in r] for r in rows])
    return canon('column', mn, [[psi[i] for i in b] for b in cp], [[phi[j] for j in r] for r in rows])
forms = {}
for op, e in elems_t: forms[(op[2], perm_pair(e)[0])] = forms.get((op[2], perm_pair(e)[0]), 0) + 1
print('element forms by (tr flag, decomposition):', forms)
keyset = {canon(k, mn, cp, rows): idx for idx, (k, mn, cp, rows, X, Y, D) in enumerate(facts)}
assert len(keyset) == len(facts)
seen = set(); orbits = []
for idx, (k, mn, cp, rows, X, Y, D) in enumerate(facts):
    if idx in seen: continue
    orb = set()
    for op, e in elems_t:
        img = act_on(k, mn, cp, rows, op, e)
        assert img in keyset, ('stabilizer image is not in the census', k, mn, img)
        orb.add(keyset[img])
    seen |= orb; orbits.append(sorted(orb))
print('orbits under the stabilizer (with transposition):', len(orbits))
for orb in orbits:
    k, mn, cp, rows, X, Y, D = facts[orb[0]]
    print('  size %d: representative %s %dx%d blocks %s classes %s' % (len(orb), k, mn[0], mn[1], cp, rows))
    print('     X keys:', [[x.key() for x in r] for r in X])
    print('     twist D:', [[d.key() for d in r] for r in D])
# which factorization contains the frozen 2x8 family (P at u60)?
PT = [list(c) for c in zip(*P)]
for kind, H in (('column', P), ('row', PT)):
    ex = [(cp, rows) for cp, rows, ok, X, Y in dita_orientations(H, 2, 8) if ok]
    for cp, rows in ex:
        c = canon(kind, (2, 8), cp, rows); print('P (u60) lies in the 2x8 %s factorization index %d, orbit %s' % (kind, keyset[c], [i for i, o in enumerate(orbits) if keyset[c] in o]))
