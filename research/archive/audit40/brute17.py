"""All-alignment brute force at act 40's seventeen exact points: exact values, factor unitarity, no flat calculus (read-only)."""
import itertools, time
exec(open('probe_head.py', encoding='utf-8').read())
src = open('../a40/dita_torus_locus_probe.py', encoding='utf-8').read()
exec(src[src.index('def H3(u1, u2, u3)'):src.index('K2, K8, DD')])
exec(src[src.index('TESTU = '):src.index('face_ok = []')])
exec(src[src.index('PTS = ['):src.index('agree = []; counts = []')])
t1 = time.time()
def admitted(H, m, n, relaxed):
    out = {}
    for cp, rows, ok, _, _ in dita_orientations(H, m, n):
        col0 = [cp[c][0] for c in range(m)]
        def lam(r, r0, c): return H[r][col0[c]] * H[r0][col0[c]].conj()
        per = []
        for b in range(1, n):
            L = []
            for s in itertools.permutations(range(m)):
                rb = [rows[b][s[a]] for a in range(m)]
                if not relaxed:
                    good = all(lam(rb[a], rb[0], c) == lam(rows[0][a], rows[0][0], c) for a in range(m) for c in range(m))
                else:
                    good = all(lam(rb[a], rb[0], c) * lam(rows[0][a], rows[0][0], 0) == lam(rows[0][a], rows[0][0], c) * lam(rb[a], rb[0], 0) for a in range(m) for c in range(1, m))
                if good: L.append(s)
            per.append(L)
        M = 1
        for L in per: M *= len(L)
        if M == 0: continue
        if not relaxed:
            X = [[lam(rows[0][a], rows[0][0], c) for c in range(m)] for a in range(m)]
            if not is_unitary_s(X, m): continue
            okY = True
            for combo in itertools.product(*per):
                r0s = [rows[0][0]] + [rows[b + 1][combo[b][0]] for b in range(n - 1)]
                if not all(is_unitary_s([[H[r][cp[c][d]] for d in range(n)] for r in r0s], n) for c in range(m)): okY = False; break
            if not okY: continue
        out[(frozenset(map(frozenset, cp)), frozenset(map(frozenset, rows)))] = M
    return out
res = []
for nm_, u in PTS:
    H = H3(*u); HT = [list(c) for c in zip(*H)]
    row_s = []; row_r = []
    for relaxed, acc in ((False, row_s), (True, row_r)):
        n_ = 0
        for f, Mx in (('column', H), ('row', HT)):
            for mn in SHAPES3: n_ += len(admitted(Mx, *mn, relaxed))
        acc.append(n_)
    res.append((nm_, row_s[0], row_r[0]))
    print('%-18s strict %2d relaxed %2d   (%.0fs)' % (nm_, row_s[0], row_r[0], time.time() - t1), flush=True)
print('strict counts ', [r[1] for r in res])
print('relaxed counts', [r[2] for r in res])
print('act 40 sorted  [0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4]')
