"""Re-basing test for every record-safe AH hit (relabelled outputs).

An AH hit has hidden idle terms z in its designated rows.  It is a mere RE-BASING of the kick
(no known hidden state needed) iff, for one hidden idle functional z:
  q' = q + uq K + (visible), p' = p + up K + (visible), K = P + z   [hidden idle terms exactly uq z, up z],
  Q' has no hidden idle term, and
  in the basis (q, p, K, idle) the learnable space of (q, p, K) is exactly span{omega(u,.)}
  (so the kick K is uniform and independent of every record).
P' is not required to equal K (P is discarded in R_u).  Tallies: per (mode, n, ops, k), read
functional -> number of configurations with a re-based (category 'AK') hit."""
import sys, os
from itertools import product
from search2 import all_graphs, configs, Cfg
import search4, search5
from search4 import VCfg, op_bits, run, span_list
from search2 import eliminate, basis_key

def ak_hits(vc, cls, row, mode, outs):
    cfg = vc.cfg
    n = cfg.n
    dh, dv = len(vc.hid), len(vc.vis)
    H = dict(zip(vc.hid, [vc.unmap(int(x)) for x in row[:dh]]))
    Vb = [int(x) for x in row[dh:dh + dv]]
    L = [vc.unmap(int(x)) for x in row[dh + dv:] if int(x)]
    if cls == "GL":
        Qset = [vc.unmap(f) for f in span_list(Vb) if f]
    elif cls == "cell":
        Qset = list({vc.unmap(f) for f in Vb})
    else:
        Qset = None
    Z = cfg.Zmask
    res = set()
    for lab, t, wu in cfg.tgts():
        orient0 = lab.startswith("(q,p)=(u0,v0)")
        qi, pi_ = (0, n) if orient0 else (n, 0)
        uq = (t[qi] >> cfg.Pc) & 1
        up = (t[pi_] >> cfg.Pc) & 1
        for (qo, po, Qo, Po) in outs:
            dq, dp = H[qo] ^ t[qi], H[po] ^ t[pi_]
            if (dq | dp) & cfg.qpP:
                continue
            zq, zp = dq & Z, dp & Z
            z = zq if uq else zp
            if (uq and zq != z) or (up and zp != z) or (not uq and zq) or (not up and zp) or z == 0:
                continue
            cands = Qset if Qset is not None else [vc.unmap(Vb[vc.vis.index(Qo)])]
            if not any(((f ^ t[cfg.Qc]) & (cfg.qpP | Z)) == 0 for f in cands):
                continue
            # learnable space in basis (q, p, K=P+z, idle): f -> f with Z-part ^= z if f has P
            Lt = [f ^ (z if (f >> cfg.Pc) & 1 else 0) for f in L]
            lam = basis_key([f & cfg.qpP for f in eliminate(Lt, Z)])
            if lam == basis_key([wu]):
                fn = {1: "u_toy", 1 << n: "v_toy", 1 | (1 << n): "u_toy+v_toy"}[wu]
                res.add(fn)
    return res

jobs = [("strict", 3, "none"), ("strict", 4, "none"), ("strict", 4, "cell"), ("strict", 4, "GL"),
        ("relaxed", 4, "none"), ("relaxed", 4, "cell"), ("relaxed", 4, "GL"),
        ("strict", 5, "none"), ("relaxed", 5, "none"), ("strict", 5, "GL")]
GLMAX, CELLMAX = 3, 6
opc = {}
for (mode, n, cls) in jobs:
    fixed = [0, 1] if mode == "relaxed" else [0, 1, 2]
    tally = {}
    ncfg = 0
    for edges in all_graphs(n):
        for (lab, vis, Qc, Pc) in configs(n, mode):
            cl = lab.split("=")[-1]
            cl = cl if all(ch in "VHab" for ch in cl) else ""
            if search5.canonical(n, edges, list(cl), fixed) != (tuple(sorted(edges)), tuple(cl)):
                continue
            cfg = Cfg(n, edges, vis, Qc, Pc, lab)
            if (cls == "GL" and cfg.dv > GLMAX) or (cls == "cell" and cfg.dv > CELLMAX):
                continue
            ncfg += 1
            if (cls, cfg.dv) not in opc:
                opc[(cls, cfg.dv)] = op_bits(cls, cfg.dv)
            vc = VCfg(cfg)
            per_k, _ = run(vc, cls, opc[(cls, cfg.dv)][1])
            outs = search5.out_assignments(cfg, mode)
            for k in range(1, 5):
                fns = set()
                for row in per_k[k]:
                    fns |= ak_hits(vc, cls, row, mode, outs)
                for fn in fns:
                    tally[(k, fn)] = tally.get((k, fn), 0) + 1
    s = "; ".join(f"k={k} AK read {fn}: {v}" for (k, fn), v in sorted(tally.items())) or "no re-based (AK) hit"
    print(f"[{mode}] n={n} ops={cls} (configurations {ncfg}; GL dim<=3): {s}", flush=True)
