"""G3-HCOUNT tiny exact checks (NOTE.md, Node 3).

K1  spacetime-sublattice decoupling of second-order nearest-neighbour rules on
    checkerboard tori; countercontrols: odd torus, rule with a center term.
K2  separate conservation of the two sublattice parts E_A, E_B of
    E = u.u + v.v - u.Av: exact linear rule mod q (exhaustive), and the integer
    value of E on binary configurations at RD6 (d = 1, q = 2; exhaustive);
    with the labelling frozen at t = 0 the two parts exchange (Y = E_A - E_B
    alternates); nontriviality: on some shell of E, E_A takes more than one
    value; countercontrol: the split by the site's spatial parity alone is not
    conserved.

Run: python3 -I sublattice_checks.py   (exit 0 and a final line "ALL PASS").
"""
import itertools
import random
import sys


def sites(d, L):
    return list(itertools.product(range(L), repeat=d))


def nbrs(n, L):
    out = []
    for j in range(len(n)):
        for s in (1, -1):
            m = list(n)
            m[j] = (m[j] + s) % L
            out.append(tuple(m))
    return out


def step(u, v, d, L, rule, q):
    w = {}
    for n in sites(d, L):
        s = sum(v[m] for m in nbrs(n, L))
        if rule == "rounded":
            f = (s + 1) // 3
        elif rule == "linear":
            f = s
        elif rule == "center":  # countercontrol: F_n also reads x_t(n)
            f = s + v[n]
        w[n] = (f - u[n]) % q
    return v, w


def par(n, t):
    return (sum(n) + t) % 2


def k1(d, L, rule, q, steps, seed):
    """Perturb data of spacetime parity 1 at time t = 0; return True iff the
    parity-0 trajectory is unchanged for `steps` steps."""
    rng = random.Random(seed)
    S = sites(d, L)
    u = {n: rng.randrange(q) for n in S}
    v = {n: rng.randrange(q) for n in S}
    u2, v2 = dict(u), dict(v)
    for n in S:  # u at time -1, v at time 0
        if par(n, -1) == 1:
            u2[n] = (u2[n] + 1) % q
        if par(n, 0) == 1:
            v2[n] = (v2[n] + 1) % q
    for t in range(steps):
        for n in S:
            if par(n, t) == 0 and v[n] != v2[n]:
                return False
            if par(n, t - 1) == 0 and u[n] != u2[n]:
                return False
        u, v = step(u, v, d, L, rule, q)
        u2, v2 = step(u2, v2, d, L, rule, q)
    return True


def parts(u, v, d, L, t, mode):
    """E_A, E_B of E = u.u + v.v - u.Av at time t (u = x(t-1), v = x(t)).
    mode 'spacetime': term at spacetime point (n, s) goes to parity (|n|+s)%2.
    mode 'spatial'  : the same with s set to 0 (fixed spatial parity)."""
    E = [0, 0]
    for n in sites(d, L):
        pu = par(n, (t - 1) if mode == "spacetime" else 0)
        pv = par(n, t if mode == "spacetime" else 0)
        E[pu] += u[n] * u[n]
        E[pv] += v[n] * v[n]
        for m in nbrs(n, L):  # u_n v_m sits at (n, t-1), parity pu
            E[pu] -= u[n] * v[m]
    return E


def k2(d, L, q, modq):
    S = sites(d, L)
    ok_st, alt_sp, bad = True, True, 0
    shell = {}
    for vals in itertools.product(range(q), repeat=2 * len(S)):
        u = dict(zip(S, vals[: len(S)]))
        v = dict(zip(S, vals[len(S):]))
        u1, v1 = step(u, v, d, L, "linear", q)
        a0 = parts(u, v, d, L, 0, "spacetime")
        a1 = parts(u1, v1, d, L, 1, "spacetime")
        f1 = parts(u1, v1, d, L, 0, "spacetime")  # labelling frozen at t = 0
        s0 = parts(u, v, d, L, 0, "spatial")
        s1 = parts(u1, v1, d, L, 0, "spatial")
        red = (lambda x: x % q) if modq else (lambda x: x)
        shell.setdefault(red(a0[0] + a0[1]), set()).add(red(a0[0]))
        if any(red(a0[i]) != red(a1[i]) for i in (0, 1)):
            ok_st = False
        # frozen labelling: the two parts exchange (Y = E_0 - E_1 alternates)
        if not (red(f1[0]) == red(a0[1]) and red(f1[1]) == red(a0[0])):
            alt_sp = False
        # countercontrol: split by spatial parity of the site alone
        if red(s0[0]) != red(s1[0]):
            bad += 1
    split = max(len(x) for x in shell.values())
    return ok_st, alt_sp, bad, split


def main():
    fails = []
    q = 2 ** 16
    for (d, L) in ((1, 6), (3, 2), (3, 4)):
        for rule in ("rounded", "linear"):
            r = k1(d, L, rule, q, 12, 1000 + 10 * d + L)
            print(f"K1 decoupled d={d} L={L} {rule}: {r}")
            if not r:
                fails.append(("K1", d, L, rule))
    for (d, L, rule) in ((1, 5, "rounded"), (3, 3, "rounded"), (3, 4, "center")):
        r = k1(d, L, rule, q, 12, 2000 + 10 * d + L)
        print(f"K1 countercontrol d={d} L={L} {rule}: decoupled={r} (expect False)")
        if r:
            fails.append(("K1-cc", d, L, rule))
    for (d, L, qq, modq) in ((1, 4, 3, True), (1, 6, 3, True), (2, 2, 3, True),
                             (1, 4, 2, False), (1, 6, 2, False), (1, 8, 2, False)):
        ok_st, alt_sp, bad, split = k2(d, L, qq, modq)
        tag = "mod q" if modq else "integer (binary)"
        print(f"K2 d={d} L={L} q={qq} {tag}: spacetime parts conserved={ok_st}; "
              f"frozen-label parts exchange={alt_sp}; site-parity part changes on {bad} states; "
              f"max distinct E_A values on one E-shell={split}")
        if not (ok_st and alt_sp and bad > 0 and split > 1):
            fails.append(("K2", d, L, qq))
    if fails:
        print("FAIL", fails)
        sys.exit(1)
    print("ALL PASS")


if __name__ == "__main__":
    main()
