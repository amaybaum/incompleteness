"""Act 36's 4x4 hull census through SIG under every alignment, with a frozen equality criterion (read-only, local).
A hull at an index map and a circle choice is the family SIG o prod_k t_k^{v_k} over its generating exponent vectors v_k;
as a set of matrices it is determined by the rational span of the v_k (the image of a torus homomorphism is the subtorus
of that span), and as a set of classes by that span plus the gauge. Hulls are compared by those two spans, exactly."""
import itertools, time
exec(open('probe36_head.py', encoding='utf-8').read())
exec(open('probe36_q.py', encoding='utf-8').read())
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
    if not all(lam[(a, b, c)] == lam[(a, 0, c)] * lam[(0, b, c)] for a in range(m) for b in range(n) for c in range(m)): return None
    X = [[lam[(a, 0, c)] for c in range(m)] for a in range(m)]
    if not (is_unitary_s(X, m) and all(is_unitary_s(Yc, n) for Yc in Y)): return None
    return X, Y, row, col
def canon(rows_):
    R_, P_ = rref([list(r) for r in rows_], 256)
    return tuple(tuple(r) for r in R_ if any(r))
hulls = []; per = {}; sorted_hulls = 0
for kind, H in (('column', SIG), ('row', SIGT)):
    for cp, rws, ok, _, _ in dita_orientations(H, 4, 4):
        nal = 0
        for s in itertools.product(itertools.permutations(range(4)), repeat=3):
            rows = [rws[0]] + [tuple(rws[b + 1][s[b][a]] for a in range(4)) for b in range(3)]
            r = exact_at(H, cp, rows, 4, 4)
            if r is None: continue
            nal += 1
            is_sorted = all(x == tuple(range(4)) for x in s)
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
                hulls.append((kind, tuple(cp), tuple(rows), is_sorted, vecs))
                sorted_hulls += is_sorted
        per[(kind, tuple(cp))] = nal
        print(kind, cp, 'valid strict alignments', nal, '(%.0fs)' % (time.time() - t1), flush=True)
print('4x4 partition structures admitted:', sum(1 for x in per.values() if x), 'of', len(per))
print('hull parametrizations (orientation, partition, alignment, circle choice):', len(hulls), '; of them at sorted alignments:', sorted_hulls, flush=True)

gens = {}
for h in hulls:
    k = frozenset(tuple(v) for v in h[4])
    if k not in gens: gens[k] = h
print('distinct generator sets:', len(gens), flush=True)
bymat = {}; bycls = {}
for k, h in gens.items():
    k1 = canon(h[4]); k2 = canon(GAUGE + h[4])
    bymat.setdefault(k1, h); bycls.setdefault(k2, h)
print('distinct hulls as matrix families (rational span of generators):', len(bymat))
print('distinct hulls modulo the gauge (span + gauge):', len(bycls), flush=True)
sorted_cls = set(canon(GAUGE + h[4]) for h in gens.values() if h[3])
print('distinct hulls modulo the gauge among the sorted parametrizations:', len(sorted_cls))
print('tangent dimensions mod gauge over distinct hulls:', sorted(set(len(k) - 31 for k in bycls)))
# second equality test: two hulls equal iff rank of joint span equals rank of each (on the distinct-by-rref reps, pairwise on a sample of all pairs is quadratic; check all pairs of reps)
reps = list(bycls.values()); rk = [rank(GAUGE + h[4]) for h in reps]
eq_pairs = sum(1 for i in range(len(reps)) for j in range(i + 1, len(reps)) if rank(GAUGE + reps[i][4] + reps[j][4]) == rk[i] == rk[j])
print('second equality test: pairs of distinct representatives found equal by joint rank:', eq_pairs, flush=True)
bad_ker = sum(1 for h in bymat.values() if not all(in_ker_df(v) for v in h[4]))
bad_q = sum(1 for h in bymat.values() if not all(q_zero(u, w) for u in h[4] for w in h[4]))
print('distinct hulls with a generator outside ker DF:', bad_ker, '; with D2F not vanishing on a generator pair:', bad_q, flush=True)
allv = [v for h in bycls.values() for v in h[4]]
print('rank of the combined tangent span mod gauge:', rank(GAUGE + allv) - 31)
Wv = list(W)
print('distinct hulls whose tangent contains W:', sum(1 for h in bycls.values() if rank(GAUGE + h[4] + [Wv]) == rank(GAUGE + h[4])))
print('audit time %.0fs' % (time.time() - t1))
