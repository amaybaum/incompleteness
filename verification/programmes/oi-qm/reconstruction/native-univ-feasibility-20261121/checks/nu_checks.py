#!/usr/bin/env python3
"""NATIVE-UNIV feasibility checks C1-C5 (PREREG.md). Exact integer arithmetic.

Run: python3 -I checks/nu_checks.py   (a few seconds). Exit 0 iff the controls are green and
C1, C2, C5 hold. Prints one JSON object; the verdict line is generated from the measurements.
"""
import itertools, json, sys
import numpy as np

T = 24
SIDES = {1: 16, 2: 8, 3: 6}
QS = [2, 3, 64, 1 << 16]
SEEDS = [0, 1, 2]


def nbsum(x):
    return sum(np.roll(x, s, a) for a in range(x.ndim) for s in (1, -1))


def F_native(x, q):          # SM 4.2 rounded rule, on representatives 0..q-1
    return (nbsum(x) + 1) // 3


def F_self(x, q):            # countercontrol: adds the site's own present value
    return (nbsum(x) + x + 1) // 3


def second_order(F, xp, x, q):
    out = [(xp, x)]
    for _ in range(T):
        xp, x = x, (F(x, q) - xp) % q
        out.append((xp, x))
    return out


def parity(shape):
    return sum(np.indices(shape)).astype(np.int64) % 2


def staggered(F, xp, x, q, comp):
    """Component comp: sites with (parity(i) + t) % 2 == comp, t the slice index.
    Single configuration y: at slice t, sites of parity (t+comp)%2 hold x_t, the others x_{t-1}.
    Start at t = 0: parity comp holds x_0, parity 1-comp holds x_{-1}."""
    P = parity(x.shape)
    y = np.where(P == comp, x, xp)
    ys = [y.copy()]
    inv_ok = True
    for t in range(T):
        upd = (P == (t + 1 + comp) % 2)          # sites whose x_{t+1} lies in this component
        new = np.where(upd, (F(y, q) - y) % q, y)
        back = np.where(upd, (F(new, q) - new) % q, new)   # half-step twice
        inv_ok &= bool(np.array_equal(back, y))
        y = new
        ys.append(y.copy())
    return ys, inv_ok


def compare(F, xp, x, q):
    full = second_order(F, xp, x, q)
    P = parity(x.shape)
    ok, inv = True, True
    for comp in (0, 1):
        ys, iv = staggered(F, xp, x, q, comp)
        inv &= iv
        for t in range(T + 1):
            cur_mask = (P == (t + comp) % 2)
            xpt, xt = full[t]
            want = np.where(cur_mask, xt, xpt)
            ok &= bool(np.array_equal(ys[t], want))
    return ok, inv


def main():
    res = {"C1": {}, "C2": {}, "C3": {}, "C4": {}}
    for q, d in itertools.product(QS, SIDES):
        shape = (SIDES[d],) * d
        c1 = c2 = True
        c3_fail = False
        for s in SEEDS:
            rng = np.random.default_rng(1000 * s + 10 * d + (q % 997))
            xp = rng.integers(0, q, shape, dtype=np.int64)
            x = rng.integers(0, q, shape, dtype=np.int64)
            ok, inv = compare(F_native, xp, x, q)
            c1 &= ok; c2 &= inv
            okc, _ = compare(F_self, xp, x, q)
            c3_fail |= not okc
        key = f"q={q},d={d}"
        res["C1"][key] = c1; res["C2"][key] = c2; res["C3"][key + " fails"] = c3_fail
    for q in (3, 1 << 16):
        fail = False
        for s in SEEDS:
            rng = np.random.default_rng(77 + s)
            xp = rng.integers(0, q, (15,), dtype=np.int64)
            x = rng.integers(0, q, (15,), dtype=np.int64)
            ok, _ = compare(F_native, xp, x, q)
            fail |= not ok
        res["C4"][f"q={q},odd side 15 fails"] = fail
    table = [((s + 1) // 3) % 2 for s in range(7)]
    res["C5"] = {"table": table, "equals_indicator_2_3_4": table == [int(s in (2, 3, 4)) for s in range(7)]}

    controls = all(res["C3"].values()) and all(res["C4"].values())
    if not controls:
        bad = [k for k, v in {**res["C3"], **res["C4"]}.items() if not v]
        verdict = "no verdict for C1/C2: control not green: " + ", ".join(bad)
        good = False
    else:
        c12 = all(res["C1"].values()) and all(res["C2"].values())
        if c12:
            verdict = ("controls green; component lemma consistent with exact runs on the sampled "
                       f"instances ({len(res['C1'])} (q,d) pairs x {len(SEEDS)} seeds, {T} ticks); "
                       "every half-step is an involution on them")
        else:
            bad = [k for k in res["C1"] if not (res["C1"][k] and res["C2"][k])]
            verdict = "controls green; component lemma contradicted by instance(s): " + ", ".join(bad)
        good = c12
    verdict += f"; C5 q=2,d=3 table {table} {'equals' if res['C5']['equals_indicator_2_3_4'] else 'differs from'} the indicator of {{2,3,4}}"
    good &= res["C5"]["equals_indicator_2_3_4"]
    res["verdict"] = verdict
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main())
