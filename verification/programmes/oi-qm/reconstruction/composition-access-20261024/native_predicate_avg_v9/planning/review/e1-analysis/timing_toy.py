"""Timing on the toy class only (non-deterministic): production G closure, full reference GSS,
and the reference via Lemma G-D (GSS of the seed part only), over the 595 F_G records."""
import sys, time
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0ref as REF, l2config as CFG
setup = CFG.make_setup(G, 'toy')
recs = [tuple(sorted(G.record_at(setup, i))) for i in range(G.num_records(setup))]
def tips(q, geo):
    c = q[0]; _, d, near, far = geo.kind(q); out = []
    for i in range(geo.dim):
        for s in (1, -1):
            e = REF.unit(geo.dim, i, s); out.append((REF.shift(c, e, d), near))
            if d >= 1: out.append((REF.shift(c, e, d - 1), far))
    return out
tp = tf = td = 0.0; n = 0; same = 0
for r in recs:
    fixed, quants, geo, elig = REF.ref_context(3, setup.n, tuple(setup.port), r, 'G')
    Q0 = set(quants) - set(fixed)
    seed = {q for q in Q0 if any(elig(u) for u in tips(q, geo))}
    inframe = Q0 - seed
    t0 = time.perf_counter(); ret = G.Context(setup, r, 'G').run(); t1 = time.perf_counter()
    full, _ = REF.greatest(fixed, quants, geo, elig, 8); t2 = time.perf_counter()
    part, _ = REF.greatest(set(), seed, geo, elig, 8); dec = set(part) | inframe; t3 = time.perf_counter()
    tp += t1 - t0; tf += t2 - t1; td += t3 - t2; n += 1; same += set(full) == dec
print('records %d  decomposition equals full reference on %d' % (n, same))
print('mean ms: production %.2f  reference full %.2f  reference via Lemma G-D %.2f' % (1e3*tp/n, 1e3*tf/n, 1e3*td/n))
