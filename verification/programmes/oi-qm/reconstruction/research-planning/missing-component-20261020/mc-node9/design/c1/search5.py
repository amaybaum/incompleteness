"""C-i record-safe search with OUTPUT RELABELLING (tally: best category per configuration, step count and read functional) (bookkeeping freedom), vectorized.

Identical to search4.py (same word, classes, quotient, pruning) except for the acceptance
test: the designated OUTPUT coordinates may differ from the input ones.
  toy out     : the two coordinates of any site whose coordinates are both hidden, either order;
  pointer out : relaxed partition -- any split site other than the toy-out site, Q_out its
                visible coordinate, P_out its hidden one;
                strict partition  -- Q_out any visible coordinate, P_out any coordinate of a
                hidden site other than the toy-out site.
Rows are compared with the target expressed in INPUT coordinates (q, p, Q, P at their input
positions).  Record-safety is unchanged: the learnable (q, p, P) space must be span{omega(u,.)}.
Also runs over isomorphism-reduced graphs: sites other than 0 (and 1, 2 in the strict mode)
are permuted and only the lexicographically least (graph, classes) form is searched.
"""
import sys, time
from itertools import permutations
import numpy as np
from search2 import all_graphs, configs, Cfg
import search4
from search4 import VCfg, op_bits, run, span_list

KMAX = 4


def out_assignments(cfg, mode):
    n = cfg.n
    vis = set(cfg.vis)
    hid_sites = [x for x in range(n) if x not in vis and (n + x) not in vis]
    split = [x for x in range(n) if (x in vis) != ((n + x) in vis)]
    outs = []
    for a in hid_sites:
        for (qo, po) in ((a, n + a), (n + a, a)):
            if mode == "relaxed":
                for b in split:
                    if b == a:
                        continue
                    Qo, Po = (b, n + b) if b in vis else (n + b, b)
                    outs.append((qo, po, Qo, Po))
            else:
                for Qo in cfg.vis:
                    for c in hid_sites:
                        if c == a:
                            continue
                        for Po in (c, n + c):
                            outs.append((qo, po, Qo, Po))
    return outs


def final_check_relabel(vc, cls, row, mode, outs):
    cfg = vc.cfg
    dh, dv = len(vc.hid), len(vc.vis)
    H = [vc.unmap(int(x)) for x in row[:dh]]
    Vb = [int(x) for x in row[dh:dh + dv]]
    L = [int(x) for x in row[dh + dv:]]
    Hd = dict(zip(vc.hid, H))
    if cls == "GL":
        Qset = [vc.unmap(f) for f in span_list(Vb) if f]
    elif cls == "cell":
        Qset = list({vc.unmap(f) for f in Vb})
    lam = []
    for f in L:
        if f:
            lead = 1 << (f.bit_length() - 1)
            if lead & vc.Dbits:
                lam.append(vc.unmap(f & vc.Dbits))
    hard = cfg.qpP
    res = []
    for lab, t, wu in cfg.tgts():
        if not (len(lam) == 1 and lam[0] == wu):
            continue
        # input-position targets
        n = cfg.n
        orient0 = lab.startswith("(q,p)=(u0,v0)")
        qi, pi_ = (0, n) if orient0 else (n, 0)
        tq, tp, tP, tQ = t[qi], t[pi_], t[cfg.Pc], t[cfg.Qc]
        for (qo, po, Qo, Po) in outs:
            dev = 0
            ok = True
            for (c, tt) in ((qo, tq), (po, tp), (Po, tP)):
                d = Hd[c] ^ tt
                if d & hard:
                    ok = False
                    break
                dev |= d
            if not ok:
                continue
            cands = Qset if cls != "none" else [vc.unmap(Vb[vc.vis.index(Qo)])]
            best = None
            for f in cands:
                d = f ^ tQ
                if d & hard:
                    continue
                a = dev | d
                cl = "E" if a == 0 else ("AH" if a & cfg.Zmask else "AV")
                if best is None or "E AV AH".split().index(cl) < "E AV AH".split().index(best):
                    best = cl
            if best:
                fn = {1: 'u_toy', 1 << n: 'v_toy', 1 | (1 << n): 'u_toy+v_toy'}[wu]
                res.append((fn, best, (lab, (qo, po, Qo, Po))))
    return res


def canonical(n, edges, classes, fixed):
    others = [x for x in range(n) if x not in fixed]
    best = None
    for perm in permutations(others):
        mp = {x: x for x in fixed}
        for a, b in zip(others, perm):
            mp[a] = b
        e2 = tuple(sorted(tuple(sorted((mp[a], mp[b]))) for a, b in edges))
        c2 = [None] * n
        for x in others:
            c2[mp[x]] = classes[others.index(x)]
        key = (e2, tuple(c2[x] for x in others))
        if best is None or key < best:
            best = key
    return best


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    modes = sys.argv[3].split(",")
    classes_ = sys.argv[4].split(",")
    only = sys.argv[6] if len(sys.argv) > 6 else None   # optional 'mode:cls' filter
    GLMAX = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    CELLMAX = int(__import__("os").environ.get("CELLMAX", "6"))
    opc = {}
    t0 = time.time()
    for mode in modes:
        for n in range(nmin, nmax + 1):
            fixed = [0, 1] if mode == "relaxed" else [0, 1, 2]
            for cls in classes_:
                if only and only != f"{mode}:{cls}" and only != mode:
                    continue
                ncfg = skipped = iso = 0
                tally, ex = {}, {}
                maxlev = 0
                for edges in all_graphs(n):
                    for (lab, vis, Qc, Pc) in configs(n, mode):
                        cl_str = lab.split("=")[-1]
                        cl_str = cl_str if all(ch in "VHab" for ch in cl_str) else ""
                        key = canonical(n, edges, list(cl_str), fixed)
                        mine = (tuple(sorted(edges)), tuple(cl_str))
                        if key != mine:
                            iso += 1
                            continue
                        cfg = Cfg(n, edges, vis, Qc, Pc, lab)
                        if (cls == "GL" and cfg.dv > GLMAX) or (cls == "cell" and cfg.dv > CELLMAX):
                            skipped += 1
                            continue
                        ncfg += 1
                        if (cls, cfg.dv) not in opc:
                            opc[(cls, cfg.dv)] = op_bits(cls, cfg.dv)
                        vc = VCfg(cfg)
                        per_k, _ = run(vc, cls, opc[(cls, cfg.dv)][1])
                        outs = out_assignments(cfg, mode)
                        for k in range(1, KMAX + 1):
                            lev = per_k[k]
                            maxlev = max(maxlev, lev.shape[0])
                            bestd = {}
                            for row in lev:
                                for (fn, d, oa) in final_check_relabel(vc, cls, row, mode, outs):
                                    if fn not in bestd or "E AV AH".split().index(d) < "E AV AH".split().index(bestd[fn][0]):
                                        bestd[fn] = (d, oa)
                            cats = {bd[0] + " read " + fn: bd[1] for fn, bd in bestd.items()}
                            for d, v in cats.items():
                                tally[(k, d)] = tally.get((k, d), 0) + 1
                                e = ex.setdefault((k, d), [])
                                if len(e) < 3:
                                    e.append((edges, lab, v))
                print(f"[{mode}, relabelled outputs] n={n} ops={cls}: configurations={ncfg} "
                      f"(isomorphic duplicates skipped={iso}, visible dim over cap={skipped}) "
                      f"max record-safe classes/level={maxlev}")
                for k in range(1, KMAX + 1):
                    cs = [f"{d}:{tally[(kk, d)]}" for (kk, d) in sorted(tally) if kk == k]
                    print(f"    k={k}: record-safe designated matches: {', '.join(cs) if cs else 'none'}")
                for (k, d), e in sorted(ex.items()):
                    for x in e:
                        print(f"      example k={k} {d}: edges={x[0]} {x[1]} {x[2]}")
                sys.stdout.flush()
    print(f"elapsed {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
