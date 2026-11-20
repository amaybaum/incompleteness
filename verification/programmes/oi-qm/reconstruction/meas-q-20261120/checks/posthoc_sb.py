#!/usr/bin/env python3
"""MEAS-Q post hoc diagnostic X1 (not preregistered; it decides no verdict).

S-B found DT_s deliveries across classes (a site outside the breaching box is used, returns to the
background in both branches, and a log holds the carrier then). This script re-runs the ten
examples stored in results.json in Q itself on the torus (Z/100)^3, where every site within
l1-distance 8 of the box has its exact Z^3 value up to t = 87, and records for each example:
  - whether H stays at (c, c) in both branches on [t2, 87] (persistent readiness);
  - whether the log site is part of the disturbance at t2 (non-background in some branch);
  - DT_A with A = the exact region (distance 1..8), persistence 60, t2 <= 27;
  - the two-slice support size at t = 28, 56, 87 (growth of the disturbance).
Run from the record directory after measq_checks.py --search:
  python3 -I checks/posthoc_sb.py      writes posthoc-sb.json; exit 0 iff it ran to completion.
"""
import json
import os
import sys

import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import measq_checks as M  # noqa: E402

C, q = M.C, M.q
n, T, R = 100, 87, 8


def main():
    base = os.path.dirname(here)
    r = json.load(open(os.path.join(base, "results.json")))
    ex = r["searches"]["S-B"]["examples"]
    out = []
    grid = np.indices((n, n, n)).reshape(3, -1).T
    for e in ex:
        h = e["hit"]
        B = M.Box(tuple(h["dims"]))
        ix = [tuple(int(v) + 40 for v in (tuple(s) + (0,) * (3 - len(s)))) for s in B.S]
        L = M.Ledger((n, n, n), C)
        L.add("environment", [(sl, ix[i], v) for (sl, i), v in zip(h["eslots"], h["env"]) if v != 0])
        cs = [(1, h["j"])] if h["mode"] == "c" else [(0, h["j"])] if h["mode"] == "p" else \
            [(0, h["j"]), (1, h["j"])]
        L.add_carrier("carrier", [(sl, ix[i], 1) for sl, i in cs])
        arr = np.array(ix)
        dist = np.abs(grid[:, None, :] - arr[None, :, :]).sum(axis=2).min(axis=1)
        E = np.nonzero((dist >= 1) & (dist <= R))[0]
        Y, supp = [], []
        for cv in (0, 1):
            p, c_ = L.build(cv)
            ys, ss = [], {}
            for t in range(T + 1):
                ys.append(np.stack([p.reshape(-1)[E], c_.reshape(-1)[E]]))
                if t in (28, 56, 87):
                    ss[t] = int(((p != C) | (c_ != C)).sum())
                p, c_ = M.q_step(p, c_)
            Y.append(np.stack(ys))
            supp.append(ss)
        Y0, Y1 = Y
        site = tuple(int(v) for v in e["site"])
        # translate the S-B site (box at offset 4 on n = 42) to this torus (offset 40)
        site = tuple(v + 36 for v in site)
        Hflat = np.ravel_multi_index(site, (n, n, n))
        H = int(np.nonzero(E == Hflat)[0][0])
        logs = [k for k in range(len(E)) if k != H]
        res = M.dt_eval(Y0, Y1, H, logs, A=list(range(len(E))), persist=60, tmax=27)
        res28 = M.dt_eval(Y0, Y1, H, logs, tmax=28)
        t2 = res28.get("t2")
        persist_ready = None
        log_in_disturbance = None
        if t2 is not None:
            bg = (Y0[:, :, H] == C).all(axis=1) & (Y1[:, :, H] == C).all(axis=1)
            persist_ready = bool(bg[t2:].all())
            lg = res28["log"]
            log_in_disturbance = bool((Y0[t2, :, lg] != C).any() or (Y1[t2, :, lg] != C).any())
        out.append(dict(example=e["site"], d=e["d"], dts_t2=t2, persist_ready_to_87=persist_ready,
                        log_in_disturbance=log_in_disturbance, dta_t2_le_27=res["dta"],
                        support=supp))
        print(out[-1], flush=True)
    with open(os.path.join(base, "posthoc-sb.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
