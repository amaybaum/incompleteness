#!/usr/bin/env python3
"""MEAS-Q run S-B-long (preregistered in amendments/A02-before-sb-long.md).

Every 10th configuration of S-B's selected list, re-run in Q itself on (Z/100)^3 (box at offset 40,
background 2^15, both carrier branches, horizon 87). For every site H at l1-distance 1..8 from the
box (exact to t = 87): DT_s and DT_A (PREREG §2, tau2 <= 27, A = that region, persistence 60) and
DT_A^h (DT_A with H at w* in both branches on [tau2, tau2 + 8]).
Run from the record directory:  python3 -I checks/sb_long.py   writes results-sb-long.json;
exit 0 iff the sample size equals the preregistered 398 and every run completed.
"""
import json
import math
import os
import sys

import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import measq_checks as M  # noqa: E402

C, q = M.C, M.q
n, T, R, T2MAX, PERSIST, HOLD = 100, 87, 8, 27, 60, 8


def pool():
    out = []
    for d in [(3,), (4,), (2, 2)]:
        out += M.enumerate_box("RZ", d, want_hits=True)["breach_list"]
    m = max(1, math.ceil(len(out) / 4000))
    return out[::m]


def evaluate(Y0, Y1):
    """Y: (T+1, 2, k). Returns per-H booleans for DT_s, DT_A, DT_A^h (vectorized over H)."""
    k = Y0.shape[2]
    diff = (Y0 != Y1).any(axis=1)                                   # (T+1, k)
    hv = Y0[:, 0, :].astype(np.int64) * (2 * q + 7) + Y0[:, 1, :]  # value code of branch 0
    ready = ~diff
    used = diff[:T2MAX + 1].any(axis=0)
    smin = np.where(diff.any(axis=0), diff.argmax(axis=0), 10 ** 6)  # first use (any t)
    fd = np.where(diff.any(axis=0), diff.argmax(axis=0), 10 ** 6)    # first difference per site
    okR = fd[:, None] >= smin[None, :]                               # okR[L, H]
    np.fill_diagonal(okR, False)
    rec = (diff.astype(np.int32) @ okR.astype(np.int32)) > 0         # (T+1, k): some admissible L differs
    dts = np.zeros(k, bool)
    dta = np.zeros(k, bool)
    dtah = np.zeros(k, bool)
    lastuse = np.full(k, -1)
    for t2 in range(T2MAX + 1):
        cand = ready[t2] & (lastuse >= 0) & used
        if cand.any():
            ok = np.zeros(k, bool)
            for t1 in range(t2):
                ok |= ready[t1] & (hv[t1] == hv[t2]) & (t1 < lastuse)
            deliv = cand & ok
            dts |= deliv & rec[t2]
            pers = rec[t2:t2 + PERSIST + 1].all(axis=0) if t2 + PERSIST <= T else np.zeros(k, bool)
            dta |= deliv & pers
            held = (ready[t2:t2 + HOLD + 1] & (hv[t2:t2 + HOLD + 1] == hv[t2][None])).all(axis=0)
            dtah |= deliv & pers & held
        lastuse = np.where(diff[t2], t2, lastuse)
    return dts, dta, dtah


def main():
    sel = pool()[::10]
    grid = np.indices((n, n, n)).reshape(3, -1).T
    rows = []
    for idx, h in enumerate(sel):
        B = M.Box(tuple(h["dims"]))
        ix = [tuple(int(v) + 40 for v in (tuple(s) + (0,) * (3 - len(s)))) for s in B.S]
        L = M.Ledger((n, n, n), C)
        L.add("environment", [(sl, ix[i], v) for (sl, i), v in zip(h["eslots"], h["env"]) if v != 0])
        cs = [(1, h["j"])] if h["mode"] == "c" else [(0, h["j"])] if h["mode"] == "p" else \
            [(0, h["j"]), (1, h["j"])]
        L.add_carrier("carrier", [(sl, ix[i], 1) for sl, i in cs])
        arr = np.array(ix)
        lo, hi = arr.min(axis=0) - R, arr.max(axis=0) + R
        sub = np.nonzero(((grid >= lo) & (grid <= hi)).all(axis=1))[0]
        dist = np.abs(grid[sub][:, None, :] - arr[None, :, :]).sum(axis=2).min(axis=1)
        E = sub[(dist >= 1) & (dist <= R)]
        boxflat = np.array([np.ravel_multi_index(s, (n, n, n)) for s in ix])
        Y, supp, conf = [], [], []
        for cv in (0, 1):
            p, c_ = L.build(cv)
            ys = []
            inbox = True
            for t in range(T + 1):
                ys.append(np.stack([p.reshape(-1)[E], c_.reshape(-1)[E]]))
                p, c_ = M.q_step(p, c_)
            nz = ((p != C) | (c_ != C)).reshape(-1)
            supp.append(int(nz.sum()))
            conf.append(bool(not np.delete(nz, boxflat).any()))
            Y.append(np.stack(ys))
        dts, dta, dtah = evaluate(Y[0], Y[1])
        rows.append(dict(i=idx, dims=h["dims"], tb=h["tb"], dts=bool(dts.any()), dta=bool(dta.any()),
                         dtah=bool(dtah.any()), n_dts=int(dts.sum()), n_dta=int(dta.sum()),
                         n_dtah=int(dtah.sum()), support87=supp, confined87=conf,
                         hit=h if dtah.any() else None))
        if idx % 40 == 0:
            print(f"  {idx}/{len(sel)}", flush=True)
    summ = dict(sample=len(sel),
                dts=sum(r["dts"] for r in rows), dta=sum(r["dta"] for r in rows),
                dtah=sum(r["dtah"] for r in rows),
                one_branch_confined=sum(r["confined87"][0] != r["confined87"][1] for r in rows),
                both_unconfined=sum(not r["confined87"][0] and not r["confined87"][1] for r in rows),
                dta_with_one_branch_confined=sum(r["dta"] and (r["confined87"][0] != r["confined87"][1])
                                                 for r in rows),
                support87_median=float(np.median([max(r["support87"]) for r in rows])))
    print("S-B-long:", summ, flush=True)
    base = os.path.dirname(here)
    with open(os.path.join(base, "results-sb-long.json"), "w") as f:
        json.dump(dict(summary=summ, rows=rows), f, indent=1)
    sys.exit(0 if len(sel) == 398 else 1)


if __name__ == "__main__":
    main()
