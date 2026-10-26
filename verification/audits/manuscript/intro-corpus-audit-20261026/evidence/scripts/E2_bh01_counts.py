#!/usr/bin/env python3
"""E2: independent exhaustive recount of the BH-01 counts the Introduction (L158-L160) and
FINDINGS R-20 cite. Written from the definitions in bh01_access_v1/PLAN.md section 2 and the
layouts stated in REPORT.md; it imports nothing from checks.py. Integer arithmetic only:
2N*TV and |M|N*P_succ are integers, so every comparison is exact.

Usage: python3 -I E2_bh01_counts.py [out.json]
"""
import itertools, json, os, sys

def bit(x, r):
    return (x >> r) & 1

def records(p, msg_regs, hidden_regs, schedule, T):
    """counts[m][record] for the cumulative record at time T; p applied homogeneously."""
    out = {}
    for m in itertools.product((0, 1), repeat=len(msg_regs)):
        c = {}
        for h in itertools.product((0, 1), repeat=len(hidden_regs)):
            x = sum(v << r for r, v in zip(msg_regs, m)) + sum(v << r for r, v in zip(hidden_regs, h))
            rec = []
            for t in range(T + 1):
                rec.append(tuple(bit(x, r) for r in schedule[t]))
                if t < T:
                    x = p[x]
            rec = tuple(rec)
            c[rec] = c.get(rec, 0) + 1
        out[m] = c
    return out

def tv2n(c0, c1):
    return sum(abs(c0.get(y, 0) - c1.get(y, 0)) for y in set(c0) | set(c1))

def succ_num(cs):
    ys = set()
    for c in cs.values():
        ys |= set(c)
    return sum(max(c.get(y, 0) for c in cs.values()) for y in ys)

def w_dep_on_d(p):
    """True iff the (reg0, reg1) part of p(x) depends on reg2 of x."""
    return any((p[x] & 3) != (p[x | 4] & 3) for x in range(4))

def is_product(p):
    if w_dep_on_d(p):
        return False
    return all(bit(p[x], 2) == bit(p[x & 4], 2) for x in range(8))

def main():
    r = {"S8": 0, "MP1_t2_tv2n_hist": {}, "MP1_C1_t3_violations": 0, "MP1_C2_violations": 0,
         "MP2_t2_min_succ": None, "MP2_t2_attain_half": 0, "MP2_t2_blind": 0,
         "nested_t3_tv2n_hist": {}, "nestedW_recover": 0, "nestedW_recover_nonproduct": 0,
         "nestedW_recover_W_depends_on_D": 0}
    sched_mp = [(), (2,), (1, 2), (0, 1, 2)]
    for p in itertools.permutations(range(8)):
        r["S8"] += 1
        c = records(p, (0,), (1, 2), sched_mp, 2)
        k = tv2n(c[(0,)], c[(1,)])          # N = 4, so delta = k/8
        r["MP1_t2_tv2n_hist"][k] = r["MP1_t2_tv2n_hist"].get(k, 0) + 1
        if 2 * succ_num(c) < 2 * 4 * 1:      # P_succ >= 1/|K| = 1/2 at t=2
            r["MP1_C2_violations"] += 1
        c3 = records(p, (0,), (1, 2), sched_mp, 3)
        if succ_num(c3) != 2 * 4:
            r["MP1_C1_t3_violations"] += 1
        c2 = records(p, (0, 1), (2,), sched_mp, 2)   # |M| = 4, N = 2
        s = succ_num(c2)                               # P_succ = s/8
        if r["MP2_t2_min_succ"] is None or s < r["MP2_t2_min_succ"]:
            r["MP2_t2_min_succ"] = s
        r["MP2_t2_attain_half"] += (s == 4)
        r["MP2_t2_blind"] += (s == 2)
        cn = records(p, (1,), (2,), [(), (0,), (0,), (0,)], 3)   # V=reg0 blank, B=reg1 msg, D=reg2
        k = tv2n(cn[(0,)], cn[(1,)])        # N = 2, delta = k/4
        r["nested_t3_tv2n_hist"][k] = r["nested_t3_tv2n_hist"].get(k, 0) + 1
        cw = records(p, (1,), (2,), [(), (0,), (0,), (0, 1)], 3)
        if not (set(cw[(0,)]) & set(cw[(1,)])):
            r["nestedW_recover"] += 1
            r["nestedW_recover_nonproduct"] += (not is_product(p))
            r["nestedW_recover_W_depends_on_D"] += w_dep_on_d(p)
    # all 256 maps of {0,1}^2: reg0 = B, reg1 = R
    am = {"maps": 0, "AM1_bij_rec": 0, "AM1_bij_norec": 0, "AM1_nonbij_rec": 0, "AM1_nonbij_norec": 0,
          "AM2_bij_violate": 0, "AM2_nonbij_violate": 0, "AM2_violators_with_constant_read_register": 0}
    for F in itertools.product(range(4), repeat=4):
        am["maps"] += 1
        bij = len(set(F)) == 4
        img0 = {F[0 + 2 * h] for h in (0, 1)}
        img1 = {F[1 + 2 * h] for h in (0, 1)}
        rec = not (img0 & img1)
        am["AM1_%s_%s" % ("bij" if bij else "nonbij", "rec" if rec else "norec")] += 1
        distinct = len({bit(F[x], 1) for x in range(4)})    # P_succ = distinct/4
        if 2 * distinct < 4:                      # P_succ = distinct/4 < 1/|K| = 1/2
            am["AM2_%s_violate" % ("bij" if bij else "nonbij")] += 1
            am["AM2_violators_with_constant_read_register"] += (distinct == 1)
    out = {"S8": r, "maps2": am,
           "derived": {"MP1_zero_advantage": r["MP1_t2_tv2n_hist"].get(0, 0),
                       "MP1_exact_recovery_one_mode_unread": r["MP1_t2_tv2n_hist"].get(8, 0),
                       "nested_zero_advantage": r["nested_t3_tv2n_hist"].get(0, 0)}}
    js = json.dumps(out, sort_keys=True, indent=1, default=str)
    if len(sys.argv) > 1:
        if os.path.abspath(sys.argv[1]) == os.path.abspath(__file__):
            sys.exit("refusing to overwrite this script")
        open(sys.argv[1], "w").write(js + "\n")
    print(js)

if __name__ == "__main__":
    main()
