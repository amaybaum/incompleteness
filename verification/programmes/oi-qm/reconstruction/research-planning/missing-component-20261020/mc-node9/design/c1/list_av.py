"""List every record-safe AV/E configuration at k = 1 (strict partition, relabelled outputs, ops = none)."""
import sys
from search2 import all_graphs, configs, Cfg
import search4, search5
n = int(sys.argv[1])
for edges in search5.all_graphs(n):
    for (lab, vis, Qc, Pc) in configs(n, "strict"):
        cfg = Cfg(n, edges, vis, Qc, Pc, lab)
        vc = search4.VCfg(cfg)
        per_k, _ = search4.run(vc, "none", search4.op_bits("none", cfg.dv)[1], kmax=1)
        outs = search5.out_assignments(cfg, "strict")
        hits = set()
        for row in per_k[1]:
            for (fn, d, oa) in search5.final_check_relabel(vc, "none", row, "strict", outs):
                if d in ("E", "AV"):
                    hits.add((fn, d, oa[1]))
        if hits:
            print(f"edges={edges} {lab}: {sorted(hits)}")
