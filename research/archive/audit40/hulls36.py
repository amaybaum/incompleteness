"""Act 36's 4x4 hull census through SIG under every alignment (read-only, local)."""
import itertools, time
exec(open('probe36_head.py', encoding='utf-8').read())
t1 = time.time()
def exact_at(H, cp, rows, m, n):
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    lam = {}; Y = []
    for c in range(m):
        Yc = []
        for b in range(n):
            i0 = row[(0, b)]; base = [H[i0][col[(c, d)]] for d in range(n)]; Yc.append(base)
            for a in range(m): lam[(a, b, c)] = H[row[(a, b)]][col[(c, 0)]] * base[0].conj()
        Y.append(Yc)
    ok = all(lam[(a, b, c)] == lam[(a, 0, c)] * lam[(0, b, c)] for a in range(m) for b in range(n) for c in range(m))
    if not ok: return None
    X = [[lam[(a, 0, c)] for c in range(m)] for a in range(m)]
    if not (is_unitary_s(X, m) and all(is_unitary_s(Yc, n) for Yc in Y)): return None
    return X, Y, row, col
hulls = []; per = {}
for kind, H in (('column', SIG), ('row', SIGT)):
    for cp, rws, ok, _, _ in dita_orientations(H, 4, 4):
        nal = 0
        for s in itertools.product(itertools.permutations(range(4)), repeat=3):
            rows = [rws[0]] + [tuple(rws[b + 1][s[b][a]] for a in range(4)) for b in range(3)]
            r = exact_at(H, cp, rows, 4, 4)
            if r is None: continue
            nal += 1
            X, Y, row, col = r
            dX = circle_directions(X); dY = [circle_directions(Yc) for Yc in Y]
            for choice in itertools.product(dX, *dY):
                xi = choice[0]; etas = choice[1:]; vecs = []
                v = [0] * 256
                for a in range(4):
                    for b in range(4):
                        for c in range(4):
                            for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = xi[a * 4 + c]
                vecs.append(v)
                for c in range(4):
                    v = [0] * 256
                    for a in range(4):
                        for b in range(4):
                            for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = etas[c][b * 4 + d]
                    vecs.append(v)
                for c in range(4):
                    for b in range(4):
                        v = [0] * 256
                        for a in range(4):
                            for d in range(4): v[row[(a, b)] * 16 + col[(c, d)]] = 1
                        vecs.append(v)
                if kind == 'row': vecs = [[v[(mm % 16) * 16 + mm // 16] for mm in range(256)] for v in vecs]
                hulls.append((kind, tuple(cp), tuple(rows), vecs))
        per[(kind, tuple(cp))] = nal
        print(kind, cp, 'valid strict alignments', nal, flush=True)
print('4x4 partition structures with a valid alignment:', sum(1 for v in per.values() if v), 'of', len(per))
print('hulls (orientation x partition x alignment x circle choice):', len(hulls), ' sorted-alignment hulls in the landed count: 492', flush=True)
# distinct tangent spaces mod gauge, via a canonical reduced basis
def canon(vecs):
    R_, P_ = rref(GAUGE + vecs, 256)
    return tuple(tuple(r) for r in R_)
dist = {}
for kind, cp, rows, vecs in hulls:
    dist.setdefault(canon(vecs), 0); dist[canon(vecs)] += 1
print('distinct hull tangent spaces mod gauge:', len(dist), flush=True)
print('tangent dimensions mod gauge:', sorted(set(len(k) - 31 for k in dist)))
allv = [v for _, _, _, vecs in hulls for v in vecs]
print('span of all hull tangents mod gauge:', rank(GAUGE + allv) - 31)
Wv = list(W)
print('W in some hull tangent:', any(rank(GAUGE + vecs + [Wv]) == rank(GAUGE + vecs) for _, _, _, vecs in hulls))
print('audit time %.0fs' % (time.time() - t1))
