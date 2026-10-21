"""Owner's two exact E1 controls (2026-10-21), by forward simulation of explicit states only (no
matrix powers, no rank algebra): fixed global update, the visible cells present at the evaluation
time, no history, no feedback.  Every stopping time t = 0 .. ord(M) - 1 (M^ord = I is checked by
simulating every state), conditioning on every visible cell.

E1-K2: path 0 - 1, R = {0} clean (0,0), toy = site 1 uniform (a, b).
E1-C1: path pointer 1 - toy 0 - bath 2, R = {1} clean, toy and bath uniform; and each of the six
       uniform two-point toy preparations with an independent uniform bath.
"""
from itertools import product, combinations
from f2 import lattice_update, apply


def period_by_states(n, M):
    k = 1
    while True:
        ok = True
        for s in range(1 << (2 * n)):
            x = s
            for _ in range(k):
                x = apply(M, x)
            if x != s:
                ok = False
                break
        if ok:
            return k
        k += 1


def run(n, edges, R, toy, toy_prep, others_uniform):
    """toy_prep: list of (u, v) toy states (uniform over the list).  Every other hidden site
    uniform; visible sites clean at 0.  Returns per t: (min, max) toy support given the current
    visible configuration, and the support-1 branch probability."""
    M = lattice_update(n, edges)
    per = period_by_states(n, M)
    hid_other = [x for x in range(n) if x not in R and x != toy]
    init = []
    for (a, b) in toy_prep:
        for vals in product((0, 1), repeat=2 * len(hid_other)):
            s = (a << toy) | (b << (n + toy))
            for i, x in enumerate(hid_other):
                s |= vals[2 * i] << x
                s |= vals[2 * i + 1] << (n + x)
            init.append(s)
    vc = [x for x in R] + [n + x for x in R]
    rows = []
    for t in range(per):
        br = {}
        for s in init:
            x = s
            for _ in range(t):
                x = apply(M, x)
            key = tuple((x >> c) & 1 for c in vc)
            br.setdefault(key, set()).add(((x >> toy) & 1, (x >> (n + toy)) & 1))
        sizes = [len(v) for v in br.values()]
        rows.append((t, min(sizes), max(sizes)))
    return per, rows


print("E1-K2 (two-site K-SYMP2): path 0-1, R = {0} clean, toy site 1 uniform")
M = lattice_update(2, ((0, 1),))
ok = True
for a, b in product((0, 1), repeat=2):
    s = (a << 1) | (b << 3)          # u1 = a, v1 = b
    x = apply(M, apply(M, s))
    vis = ((x >> 0) & 1, (x >> 2) & 1)
    hid = ((x >> 1) & 1, (x >> 3) & 1)
    ok &= vis == (b, a) and hid == (0, b)
    print(f"  (a,b)=({a},{b}): after 2 steps visible (u0,v0)={vis}, hidden (u1,v1)={hid}")
print("  visible = (b, a), hidden = (0, b) for all four:", "PASS" if ok else "FAIL")
per, rows = run(2, ((0, 1),), (0,), 1, [(a, b) for a in (0, 1) for b in (0, 1)], True)
print(f"  period {per}; toy support given the current visible site, t = 0..{per - 1}: "
      + " ".join(str(mn) if mn == mx else f"{mn}-{mx}" for (t, mn, mx) in rows))

print("\nE1-C1 (pointer 1 - toy 0 - bath 2, R = {1})")
per, rows = run(3, ((0, 1), (0, 2)), (1,), 0, [(a, b) for a in (0, 1) for b in (0, 1)], True)
seq = [mn for (t, mn, mx) in rows]
print(f"  period by state simulation: {per} (owner: M^8 = I)")
print(f"  uniform toy, uniform bath: min toy support t = 0..{per - 1}: {' '.join(map(str, seq))}"
      f"   (owner: 4 2 2 4 4 4 2 2) {'PASS' if seq == [4, 2, 2, 4, 4, 4, 2, 2] else 'FAIL'}")
states = [(a, b) for a in (0, 1) for b in (0, 1)]
allok = True
for pair in combinations(states, 2):
    per, rows = run(3, ((0, 1), (0, 2)), (1,), 0, list(pair), True)
    mins = [mn for (t, mn, mx) in rows]
    allok &= min(mins) >= 2 or False
    print(f"  toy uniform on {pair}, bath uniform: min toy support t = 0..{per - 1}: {' '.join(map(str, mins))}")
print("  no point mass at any stopping time for the six two-point preparations:", "PASS" if allok else "FAIL")
