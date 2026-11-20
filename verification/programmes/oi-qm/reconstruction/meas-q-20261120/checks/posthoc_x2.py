#!/usr/bin/env python3
"""MEAS-Q post hoc diagnostic X2 (not preregistered; decides no verdict).

A02 asks that any DT_A^h delivery of S-B-long be re-run with a ledger audit and reported as a
candidate for review. This script takes the first 40 S-B-long configurations with a DT_A^h
delivery (in sample order), re-runs each in Q on (Z/100)^3 (box at offset 40, horizon 87), runs
the ledger audit on both branches for the first 5, and records for the first qualifying H:
  t2; |Lb| (largest admissible record block); the fraction of A whose content differs between the
  branches at t2 and at t2 + 60; the fraction of A minus {H} at (c,c) in both branches at t2;
  whether H stays ready to t = 87; whether a single site of Lb holds the record on [t2, t2+60];
  the l1 distance of H from the box.
Run from the record directory after sb_long.py:  python3 -I checks/posthoc_x2.py
"""
import json
import os
import sys

import numpy as np

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import measq_checks as M  # noqa: E402
import sb_long as SB  # noqa: E402

C, q = M.C, M.q
n, T, R, T2MAX, PERSIST, HOLD = SB.n, SB.T, SB.R, SB.T2MAX, SB.PERSIST, SB.HOLD


def detail(Y0, Y1, dist_E):
    k = Y0.shape[2]
    diff = (Y0 != Y1).any(axis=1)
    hv = Y0[:, 0, :].astype(np.int64) * (2 * q + 7) + Y0[:, 1, :]
    ready = ~diff
    fd = np.where(diff.any(axis=0), diff.argmax(axis=0), 10 ** 6)
    used = diff[:T2MAX + 1].any(axis=0)
    for H in range(k):
        if not used[H]:
            continue
        smin = fd[H]
        okR = fd >= smin
        okR[H] = False
        Lb = np.nonzero(okR)[0]
        lastuse = -1
        for t2 in range(T2MAX + 1):
            if ready[t2, H] and lastuse >= 0 and t2 + PERSIST <= T:
                t1s = [t1 for t1 in range(t2) if ready[t1, H] and hv[t1, H] == hv[t2, H] and t1 < lastuse]
                rec = diff[t2:t2 + PERSIST + 1][:, Lb].any(axis=1).all() if len(Lb) else False
                held = (ready[t2:t2 + HOLD + 1, H] & (hv[t2:t2 + HOLD + 1, H] == hv[t2, H])).all()
                if t1s and rec and held:
                    bg = (Y0[t2] == C).all(axis=0) & (Y1[t2] == C).all(axis=0)
                    single = bool(diff[t2:t2 + PERSIST + 1][:, Lb].all(axis=0).any())
                    return dict(H_dist=int(dist_E[H]), t2=t2, Lb=int(len(Lb)),
                                frac_A_differs_t2=round(float(diff[t2].mean()), 3),
                                frac_A_differs_t2p60=round(float(diff[t2 + PERSIST].mean()), 3),
                                frac_A_bg_both_t2=round(float(np.delete(bg, H).mean()), 3),
                                H_ready_to_87=bool((ready[t2:, H] & (hv[t2:, H] == hv[t2, H])).all()),
                                single_site_record=single)
            if diff[t2, H]:
                lastuse = t2
    return None


def main():
    base = os.path.dirname(here)
    sl = json.load(open(os.path.join(base, "results-sb-long.json")))
    rows = [r for r in sl["rows"] if r["dtah"]][:40]
    grid = np.indices((n, n, n)).reshape(3, -1).T
    out = []
    for z, r in enumerate(rows):
        h = r["hit"]
        B = M.Box(tuple(h["dims"]))
        ix = [tuple(int(v) + 40 for v in (tuple(s) + (0,) * (3 - len(s)))) for s in B.S]
        L = M.Ledger((n, n, n), C)
        L.add("environment", [(sl_, ix[i], v) for (sl_, i), v in zip(h["eslots"], h["env"]) if v != 0])
        cs = [(1, h["j"])] if h["mode"] == "c" else [(0, h["j"])] if h["mode"] == "p" else \
            [(0, h["j"]), (1, h["j"])]
        L.add_carrier("carrier", [(sl_, ix[i], 1) for sl_, i in cs])
        arr = np.array(ix)
        lo, hi = arr.min(axis=0) - R, arr.max(axis=0) + R
        sub = np.nonzero(((grid >= lo) & (grid <= hi)).all(axis=1))[0]
        dist = np.abs(grid[sub][:, None, :] - arr[None, :, :]).sum(axis=2).min(axis=1)
        sel = (dist >= 1) & (dist <= R)
        E, dist_E = sub[sel], dist[sel]
        Y, audits = [], []
        for cv in (0, 1):
            p0, c0 = L.build(cv)
            p, c_ = p0.astype(np.int32), c0.astype(np.int32)
            ys = []
            status = "ok"
            for t in range(T + 1):
                ys.append(np.stack([p.reshape(-1)[E], c_.reshape(-1)[E]]))
                pn, cn = SB.q_step32(p, c_)
                if z < 5 and status == "ok":
                    # streaming ledger audit: the run's tick equals Q's own iterate (int64 rule)
                    ep, ec = M.q_step(p.astype(np.int64), c_.astype(np.int64))
                    if not (np.array_equal(ep, pn) and np.array_equal(ec, cn)):
                        status = f"unaccounted controller (tick {t + 1})"
                p, c_ = pn, cn
            Y.append(np.stack(ys))
            if z < 5:
                # initial state against the ledger (checked by Ledger.build above, by construction)
                audits.append(status)
        d = detail(Y[0], Y[1], dist_E)
        out.append(dict(i=r["i"], audit=audits or None, **(d or {"none": True})))
        print(out[-1], flush=True)
    keys = ["frac_A_differs_t2", "frac_A_differs_t2p60", "frac_A_bg_both_t2"]
    summ = {k: dict(min=min(o[k] for o in out if k in o), median=float(np.median([o[k] for o in out if k in o])),
                    max=max(o[k] for o in out if k in o)) for k in keys}
    summ["H_ready_to_87"] = sum(o.get("H_ready_to_87", False) for o in out)
    summ["single_site_record"] = sum(o.get("single_site_record", False) for o in out)
    summ["Lb_median"] = float(np.median([o["Lb"] for o in out if "Lb" in o]))
    summ["audits_ok"] = all(o["audit"] == ["ok", "ok"] for o in out if o["audit"])
    summ["n"] = len(out)
    print("X2:", summ)
    with open(os.path.join(base, "posthoc-x2.json"), "w") as f:
        json.dump(dict(summary=summ, rows=out), f, indent=1)


if __name__ == "__main__":
    main()
