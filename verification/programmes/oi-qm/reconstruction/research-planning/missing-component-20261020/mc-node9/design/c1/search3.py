"""C-i exhaustive search, record-safe form (pruned).  Same word, classes and equivalence as
search2.py, with two changes:

1. Pruning.  L_j (the learnable input functionals after j readouts) only grows with j, so the
   learnable space of (q, p, P) -- L_j with uniform hidden idle inputs eliminated and known
   visible inputs dropped -- only grows.  R_u requires it to equal span{omega(u, .)}, a single
   nonzero functional of the toy coordinates alone.  A class whose learnable space already
   involves P or has dimension >= 2 can never reach a realization and is discarded.  The
   search is therefore complete for record-safe words, and says nothing about leaking words.
2. Designated status.  E : exact.  AV : equal to the target whenever every visible input is 0
   (the declared clean visible inputs: Q = 0 and any further visible cell, which must then be
   declared a clean ancilla).  AH : needs a hidden idle input in a known state.
   A deviation in a designated hidden coordinate (q, p, P) is a failure.
"""
import sys, time
from itertools import combinations, product, permutations
from f2 import rowmul, compose, lattice_update, identity
from search2 import all_graphs, basis_key, span_list, ordered_bases, eliminate, Cfg, configs

KMAX = 4
OB_CACHE = {}
PERM_CACHE = {}


def vkey(cls, vrows):
    if cls == "GL":
        return basis_key(vrows)
    if cls == "cell":
        return tuple(sorted(vrows))
    return tuple(vrows)


def vchoices(cls, key):
    if cls == "GL":
        if key not in OB_CACHE:
            OB_CACHE[key] = ordered_bases(key)
        return OB_CACHE[key]
    if cls == "cell":
        if key not in PERM_CACHE:
            PERM_CACHE[key] = list(set(permutations(key)))
        return PERM_CACHE[key]
    return [key]


def learn_space(cfg, L):
    return basis_key([f & cfg.qpP for f in eliminate(L, cfg.Zmask)])


def admissible(cfg, lam):
    # dimension <= 1 and supported on the toy coordinates (u0, v0) only
    if len(lam) > 1:
        return False
    return all((f & (1 << cfg.Pc)) == 0 for f in lam)


def final_check(cfg, cls, key):
    H, V, L = key
    Hd = dict(zip(cfg.hid, H))
    if cls == "GL":
        Qc = [f for f in span_list(V) if f]
    elif cls == "cell":
        Qc = list(set(V))
    else:
        Qc = [V[cfg.vis.index(cfg.Qc)]]
    lam = learn_space(cfg, L)
    hard = cfg.qpP                       # designated hidden coordinates
    out = []
    for lab, t, wu in cfg.tgts():
        if lam != basis_key([wu]):
            continue
        dev = 0
        ok = True
        for c in (0, cfg.n, cfg.Pc):
            d = Hd[c] ^ t[c]
            if d & hard:
                ok = False
                break
            dev |= d
        if not ok:
            continue
        best = None
        for f in Qc:
            d = f ^ t[cfg.Qc]
            if d & hard:
                continue
            a = dev | d
            cl = "E" if a == 0 else ("AH" if a & cfg.Zmask else "AV")
            if best is None or "E AV AH".split().index(cl) < "E AV AH".split().index(best):
                best = cl
        if best:
            out.append((lab, best))
    return out


def run_cfg(cfg, cls, kmax=KMAX, keep_paths=False):
    X0 = identity(cfg.N)
    H0 = tuple(X0[c] for c in cfg.hid)
    V0 = [X0[c] for c in cfg.vis]
    k0 = (H0, vkey(cls, V0), basis_key(V0))
    level = {k0}
    parent = {k0: None}
    per_k = {}
    for k in range(1, kmax + 1):
        nxt = set()
        for key in level:
            H, Vk, L = key
            for vr in vchoices(cls, Vk):
                Y = [0] * cfg.N
                for c, r in zip(cfg.hid, H):
                    Y[c] = r
                for c, r in zip(cfg.vis, vr):
                    Y[c] = r
                X = compose(cfg.M, Y)
                Vn = [X[c] for c in cfg.vis]
                Ln = basis_key(list(L) + Vn)
                if not admissible(cfg, learn_space(cfg, Ln)):
                    continue
                kn = (tuple(X[c] for c in cfg.hid), vkey(cls, Vn), Ln)
                if kn not in nxt:
                    nxt.add(kn)
                    if keep_paths and kn not in parent:
                        parent[kn] = (key, vr)
        level = nxt
        hits = []
        for key in level:
            for (lab, d) in final_check(cfg, cls, key):
                hits.append((lab, d, key))
        per_k[k] = (len(level), hits)
    return per_k, parent


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    modes = sys.argv[3].split(",")
    classes = sys.argv[4].split(",")
    GLMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    CELLMAX = 6
    t0 = time.time()
    for mode in modes:
        for n in range(nmin, nmax + 1):
            for cls in classes:
                ncfg = skipped = 0
                tally = {}
                examples = {}
                maxlev = 0
                for edges in all_graphs(n):
                    for (lab, vis, Qc, Pc) in configs(n, mode):
                        cfg = Cfg(n, edges, vis, Qc, Pc, lab)
                        if (cls == "GL" and cfg.dv > GLMAX) or (cls == "cell" and cfg.dv > CELLMAX):
                            skipped += 1
                            continue
                        ncfg += 1
                        per_k, _ = run_cfg(cfg, cls)
                        for k in range(1, KMAX + 1):
                            sz, hits = per_k[k]
                            maxlev = max(maxlev, sz)
                            cats = {}
                            for (tl, d, key) in hits:
                                cats.setdefault(d, tl)
                            for d, tl in cats.items():
                                tally[(k, d)] = tally.get((k, d), 0) + 1
                                ex = examples.setdefault((k, d), [])
                                if len(ex) < 3:
                                    ex.append((edges, lab, tl))
                print(f"[{mode}] n={n} ops={cls}: configurations={ncfg} skipped(visible dim)={skipped} "
                      f"max record-safe classes/level={maxlev}")
                for k in range(1, KMAX + 1):
                    cs = [f"{d}:{tally[(k, d)]}" for d in ("E", "AV", "AH") if (k, d) in tally]
                    print(f"    k={k}: record-safe designated matches: {', '.join(cs) if cs else 'none'}")
                for (k, d), ex in sorted(examples.items()):
                    for e in ex[:3]:
                        print(f"      example k={k} {d}: edges={e[0]} {e[1]} target {e[2]}")
                sys.stdout.flush()
    print(f"elapsed {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
