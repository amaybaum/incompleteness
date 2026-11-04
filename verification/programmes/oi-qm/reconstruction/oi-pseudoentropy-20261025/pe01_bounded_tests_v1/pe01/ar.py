"""AR: the admissible region is derived, not reprinted (PLAN.md §5, §7).

Z(phi): the largest k such that for every control sequence c_0..c_{k-1} the first k increments
f(sigma_{c_0} h), f(sigma_{c_1} sigma_{c_0} h), ... are jointly uniform under uniform h, by
exhaustive equidistribution over all control sequences. K_cx(phi) = floor(l_med / 2) with l_med the
mu-median orbit length. The region at (n, m) for phi is the set of K with K >= Z + 4, K >= w,
K <= K_cx and footprint m + ceil(log2(K+1)) + 1 <= theta; it must equal the §7 tables cell for cell.
"""
import re

import numpy as np

from . import generators as G
from .composite import clock_bits

W = 3


def Z_of(gen):
    n = gen.n
    H = gen.H
    hs = np.arange(H, dtype=np.int64)
    k = 0
    while True:
        k1 = k + 1
        if k1 > n:            # 2^k1 patterns cannot be uniform over 2^n seeds beyond k1 = n
            return k, True
        ok = True
        for cs in range(1 << k1):
            h = hs.copy()
            key = np.zeros(H, dtype=np.int64)
            for t in range(k1):
                ct = (cs >> t) & 1
                h = gen.sig[ct, h]
                key |= gen.f[h].astype(np.int64) << t
            cnt = np.bincount(key, minlength=1 << k1)
            if not (cnt == H >> k1).all():
                ok = False
                break
        if not ok:
            return k, True
        k = k1


def kcx_of(gen):
    ol = G.orbit_lengths(gen.phi_table())
    w = gen.seed_w
    # mu-median over states (weight 1 each for the primaries): lower and upper medians
    s = np.sort(ol)
    lo, hi = int(s[(len(s) - 1) // 2]), int(s[len(s) // 2])
    return lo // 2, lo == hi, lo, hi


def kcx_independent(gen):
    """K_cx by a separately coded census: each state's orbit is walked with scalar steps of the
    generator (not the permutation table), and the mu-median taken by counting."""
    n = gen.n
    sig = [gen.sig[0].tolist(), gen.sig[1].tolist()]
    f = gen.f.tolist()
    S = 2 << n
    length = [0] * S
    for s0 in range(S):
        if length[s0]:
            continue
        x, h = s0 & 1, s0 >> 1
        orbit = [s0]
        while True:
            h = sig[x][h]
            x = x ^ f[h]
            s = x | (h << 1)
            if s == s0:
                break
            orbit.append(s)
        for s in orbit:
            length[s] = len(orbit)
    srt = sorted(length)
    return srt[(S - 1) // 2] // 2, srt[(S - 1) // 2], srt[S // 2]


def footprint(m, K):
    return m + clock_bits(K) + 1


def region(Z, kcx, m, th):
    ks = [K for K in range(W, kcx + 1) if K >= Z + W + 1 and footprint(m, K) <= th]
    return [min(ks), max(ks)] if ks else None


# ---------------------------------------------------------------- the plan's tables

def _cells(line):
    parts = re.split(r"(?<!\\)\|", line.strip())
    return [p.strip() for p in parts[1:-1]]


def parse_plan_tables(text):
    """Z table and both region tables of §7 from PLAN.md's text."""
    lines = text.split("\n")
    Zt = {}
    for ln in lines:
        mt = re.match(r"\s*\| Z\(`(G_\w+)`\) \|(.*)\|\s*$", ln)
        if mt:
            Zt[mt.group(1)] = [int(x.strip()) for x in mt.group(2).split("|")]
    tables = {}
    for key, head in (("n", r"\$\\theta = n\$:"), ("n+1", r"\$\\theta = n\+1\$:")):
        i = next(j for j, ln in enumerate(lines) if re.match(r"\s*" + head + r"\s*$", ln))
        rows = {}
        j = i + 1
        while j < len(lines) and not lines[j].strip().startswith("|"):
            j += 1
        j += 2   # header and rule
        while j < len(lines) and lines[j].strip().startswith("|"):
            c = _cells(lines[j])
            n = int(c[0])
            cells = []
            for cell in c[1:]:
                trip = [t.strip() for t in re.split(r"\\\|", cell)]
                cells.append([None if t == "–" else [int(a) for a in t.strip("[]").split(",")] for t in trip])
            rows[n] = cells
            j += 1
        tables[key] = rows
    return Zt, tables


def ar_check(plan_text):
    """Recompute Z, K_cx and both regions; compare with the plan cell for cell."""
    rec = {"checkpoint": "AR", "reasons": []}
    Zt, tables = parse_plan_tables(plan_text)
    names = ("G_lin", "G_filt", "G_clk")
    Zm, Km = {}, {}
    for n in range(3, 9):
        gs = G.named(n)
        for nm in names:
            z, _ = Z_of(gs[nm])
            kcx, uniq, lo, hi = kcx_of(gs[nm])
            Zm[(nm, n)] = z
            Km[(nm, n)] = kcx
            rec.setdefault("l_med", {}).setdefault(nm, []).append(lo)
            if not uniq:
                rec["reasons"].append("median orbit length not unique for %s n=%d" % (nm, n))
            # independent K_cx: closed form for G_lin and G_filt (two fixed points (x, 0), every other
            # state on a cycle of length 2^n - 1, since a balanced output sums to 0 over a period),
            # a separately coded orbit census for G_clk
            ind, l1, l2 = kcx_independent(gs[nm])
            want = (1 << (n - 1)) - 1 if nm in ("G_lin", "G_filt") else ind
            if kcx != want or ind != want or l1 != l2:
                rec["reasons"].append("K_cx(%s, n=%d) = %d disagrees with the independent value %d" % (nm, n, kcx, want))
    rec["Z"] = {nm: [Zm[(nm, n)] for n in range(3, 9)] for nm in names}
    rec["K_cx"] = {nm: [Km[(nm, n)] for n in range(3, 9)] for nm in names}
    for nm in names:
        if Zt.get(nm) != rec["Z"][nm]:
            rec["reasons"].append("Z(%s) differs from the plan: %s vs %s" % (nm, rec["Z"][nm], Zt.get(nm)))
    if rec["Z"]["G_lin"] != [3, 4, 5, 6, 7, 8]:
        rec["reasons"].append("Z(G_lin) != n")
    recomputed = {}
    for key, thf in (("n", lambda n: n), ("n+1", lambda n: n + 1)):
        rows = {}
        for n in range(3, 9):
            rows[n] = [[region(Zm[(nm, n)], Km[(nm, n)], m, thf(n)) for nm in names] for m in range(1, 5)]
            if tables[key].get(n) != rows[n]:
                rec["reasons"].append("region table theta=%s row n=%d differs from the plan" % (key, n))
        recomputed[key] = rows
    rec["region"] = {k: {str(n): v for n, v in r.items()} for k, r in recomputed.items()}
    rec["pass"] = not rec["reasons"]
    return rec
