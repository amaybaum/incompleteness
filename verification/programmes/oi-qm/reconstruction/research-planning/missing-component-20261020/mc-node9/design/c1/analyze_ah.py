"""Analyze record-safe AH hits (strict and relaxed, relabelled outputs, ops = none/cell, n <= 4):
print designated rows and their deviation from the target, and test whether the deviation is
a pure re-basing of the kick source: replacing P by P_eff = P + z (z a sum of hidden idle input
coordinates) on the input side, and by the corresponding functional on the output side, makes
the rows exact.  Re-basing needs no known hidden state; anything else is genuine AH."""
import sys
from search2 import all_graphs, configs, Cfg
import search4, search5
from f2 import lattice_update

def nm(n, j):
    return f"u{j}" if j < n else f"v{j-n}"

def fmt(n, r):
    return " + ".join(nm(n, j) for j in range(2 * n) if r >> j & 1) or "0"

for mode in ("strict", "relaxed"):
    for n in (3, 4):
        for edges in all_graphs(n):
            for (lab, vis, Qc, Pc) in configs(n, mode):
                cfg = Cfg(n, edges, vis, Qc, Pc, lab)
                vc = search4.VCfg(cfg)
                per_k, _ = search4.run(vc, "none", search4.op_bits("none", cfg.dv)[1], kmax=4)
                outs = search5.out_assignments(cfg, mode)
                for k in range(1, 5):
                    for row in per_k[k]:
                        hits = search5.final_check_relabel(vc, "none", row, mode, outs)
                        for (fn, d, (tl, oa)) in hits:
                            if d != "AH":
                                continue
                            # rebuild designated rows from the class row (ops=none: exact rows)
                            dh, dv = len(vc.hid), len(vc.vis)
                            H = dict(zip(vc.hid, [vc.unmap(int(x)) for x in row[:dh]]))
                            V = dict(zip(vc.vis, [vc.unmap(int(x)) for x in row[dh:dh + dv]]))
                            allrows = {**H, **V}
                            qo, po, Qo, Po = oa
                            rq, rp, rQ, rP = allrows[qo], allrows[po], allrows[Qo], allrows[Po]
                            z_in = rP & cfg.Zmask   # hidden idle part of P'
                            print(f"[{mode}] n={n} k={k} edges={edges} {lab} {tl} read {fn} out(q,p,Q,P)={tuple(nm(n,c) for c in oa)}")
                            print(f"     q'={fmt(n,rq)} | p'={fmt(n,rp)} | Q'={fmt(n,rQ)} | P'={fmt(n,rP)}")
