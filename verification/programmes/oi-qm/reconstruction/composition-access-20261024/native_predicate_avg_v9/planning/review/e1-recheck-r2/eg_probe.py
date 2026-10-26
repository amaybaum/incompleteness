"""Toy only: E_G = records whose Out(R) has a shared ELIGIBLE near tip (closure-free; contains
Surv_G by P_G). Also F_G and their overlap."""
import sys
sys.path.insert(0, sys.argv[1])
import s0geom as G, s0ref as REF, l2config as CFG
setup = CFG.make_setup(G, 'toy')
recs = [tuple(sorted(G.record_at(setup, i))) for i in range(G.num_records(setup))]
def near(q, geo):
    c = q[0]; _, d, nr, _ = geo.kind(q)
    return [((REF.unit(3, i, s)), (REF.shift(c, REF.unit(3, i, s), d), nr)) for i in range(3) for s in (1, -1)]
def tipsall(q, geo):
    c = q[0]; _, d, nr, fr = geo.kind(q); out = []
    for i in range(3):
        for s in (1, -1):
            e = REF.unit(3, i, s); out.append((REF.shift(c, e, d), nr))
            if d >= 1: out.append((REF.shift(c, e, d - 1), fr))
    return out
def shared(Q, geo, elig=None):
    seen = {}
    for q in sorted(Q):
        for e, u in near(q, geo):
            if elig is not None and not elig(u): continue
            if (e, u) in seen and seen[(e, u)] != q: return True
            seen.setdefault((e, u), q)
    return False
EG = FG = both = 0
for r in recs:
    fixed, quants, geo, elig = REF.ref_context(3, setup.n, tuple(setup.port), r, 'G')
    Q0 = set(quants) - set(fixed)
    out = {q for q in Q0 if any(elig(u) for u in tipsall(q, geo))}
    e = shared(out, geo, elig); f = shared(Q0 - out, geo)
    EG += e; FG += f; both += e and f
print('toy G: E_G (Out has shared eligible near tip) =', EG, ' F_G =', FG, ' both =', both, ' of', len(recs))
