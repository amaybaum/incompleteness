#!/usr/bin/env python3
"""DELIVER-1 exact controls (paper-only unit; small exact cases, no sweeps).

Every probability is an exact Fraction. Entropies that are needed are exact
elements a + b*log2(3) (class L), compared by integer arithmetic; no floating
point value certifies an equality or inequality. Lattice checks are exact
integer computations on small periodic cubic lattices.

Run:  python3 -I deliver_checks.py      (exit status 0 iff every check holds)
"""
from fractions import Fraction as Fr
from itertools import product
from math import comb
import sys

RESULTS = []


def check(name, ok):
    RESULTS.append((name, bool(ok)))
    print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")


# ----------------------------------------------------------------- exact logs
class L:
    """a + b*log2(3), a and b rational."""

    def __init__(self, a=0, b=0):
        self.a, self.b = Fr(a), Fr(b)

    def __add__(self, o):
        o = o if isinstance(o, L) else L(o)
        return L(self.a + o.a, self.b + o.b)

    __radd__ = __add__

    def __neg__(self):
        return L(-self.a, -self.b)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, L) else L(o)))

    def scale(self, r):
        return L(self.a * Fr(r), self.b * Fr(r))

    def __eq__(self, o):
        o = o if isinstance(o, L) else L(o)
        return self.a == o.a and self.b == o.b

    def __repr__(self):
        return f"{self.a} + {self.b}*log2(3)"


def _v(n, p):
    k = 0
    while n % p == 0:
        n //= p
        k += 1
    return k, n


def log2_23(x):
    """exact log2 of a positive rational whose factors are only 2 and 3."""
    x = Fr(x)
    a2, rn = _v(x.numerator, 2)
    a3, rn = _v(rn, 3)
    b2, rd = _v(x.denominator, 2)
    b3, rd = _v(rd, 3)
    if rn != 1 or rd != 1:
        raise ValueError(f"not a {{2,3}}-rational: {x}")
    return L(a2 - b2, a3 - b3)


def entropy(dist):
    h = L()
    for p in dist.values():
        if p:
            h = h - log2_23(p).scale(p)
    return h


def marg(law, f):
    out = {}
    for s, p in law.items():
        k = f(s)
        out[k] = out.get(k, 0) + p
    return out


H2_QUARTER = L(2, Fr(-3, 4))  # h2(1/4) = 2 - (3/4) log2 3


# ===================================================== cubic-lattice helpers
def sites(n):
    return list(product(range(n), repeat=3))


def nbrs(i, n):
    x, y, z = i
    return [((x + 1) % n, y, z), ((x - 1) % n, y, z), (x, (y + 1) % n, z),
            (x, (y - 1) % n, z), (x, y, (z + 1) % n), (x, y, (z - 1) % n)]


def gq(s, q):
    """rounded stencil value on representatives: floor((s+1)/3) mod q."""
    return ((s + 1) // 3) % q


def g2(s):
    return gq(s, 2)


def step_sets(prev, cur, n):
    """binary rule on a vacuum background, perturbation sets: returns next set."""
    cnt = {}
    for j in cur:
        for i in nbrs(j, n):
            cnt[i] = cnt.get(i, 0) + 1
    new = {i for i, c in cnt.items() if g2(c) == 1}
    return new ^ prev  # symmetric difference = XOR with x_{t-1}


def closure2(A, n):
    D = set(A)
    changed = True
    while changed:
        changed = False
        cnt = {}
        for j in D:
            for i in nbrs(j, n):
                if i not in D:
                    cnt[i] = cnt.get(i, 0) + 1
        add = {i for i, c in cnt.items() if c >= 2}
        if add:
            D |= add
            changed = True
    return D


def box(lo, hi):
    return set(product(*[range(a, b + 1) for a, b in zip(lo, hi)]))


def is_closed(D, n):
    for i in sites(n):
        if i in D:
            continue
        if sum(1 for j in nbrs(i, n) if j in D) >= 2:
            return False
    return True


# ============================================================ Node 1 controls
def conveyor_law(m, M, r):
    """state = (H, belt[0..m-1], carriers[0..M-1]); H and belt cells are 0 w.p. r."""
    law = {}
    for bits in product((0, 1), repeat=1 + m + M):
        p = Fr(1)
        for b in bits[:1 + m]:
            p *= r if b == 0 else 1 - r
        p *= Fr(1, 2 ** M)
        if p:
            law[bits] = law.get(bits, 0) + p
    return law


def conveyor_tick(s, m, M):
    H, belt, k = s[0], list(s[1:1 + m]), list(s[1 + m:])
    H ^= k[0]                       # write the current carrier into the ready cell
    H, belt[0] = belt[0], H         # exchange with the arriving belt cell
    belt = belt[1:] + belt[:1]      # belt advances
    k = k[1:] + k[:1]               # carrier stream advances
    return (H,) + tuple(belt) + tuple(k)


def push(law, f):
    out = {}
    for s, p in law.items():
        t = f(s)
        out[t] = out.get(t, 0) + p
    return out


def node1():
    m, M = 3, 4
    for tag, r in (("conveyor", Fr(1)), ("bath", Fr(3, 4))):
        law = conveyor_law(m, M, r)
        ready = []
        Ks = None
        for t in range(1, m + 2):
            law = push(law, lambda s: conveyor_tick(s, m, M))
            ready.append(marg(law, lambda s: s[0]).get(0, 0))
            if t == m:
                # K(H u belt) = (m+1) - H(H u belt | carriers)
                Hj = entropy(law)
                Hc = entropy(marg(law, lambda s: s[1 + m:]))
                Ks = L(m + 1) - (Hj - Hc)
        D0 = L(m + 1) - entropy(marg(conveyor_law(m, M, r), lambda s: s[:1 + m]))
        exp_ready = [r] * m + [Fr(1, 2)]
        check(f"D{1 if tag == 'conveyor' else 2}a {tag}: P(H ready) after ticks 1..{m + 1} = "
              f"{[str(x) for x in ready]}", ready == exp_ready)
        if r == 1:
            exp = L(m + 1)
        else:
            exp = (L(1) - H2_QUARTER).scale(m + 1)
        check(f"D{1 if tag == 'conveyor' else 2}b {tag}: D0 = K(H u belt) at tick m = "
              f"(N+1)(1-h2(eps)) with N=m={m} (per-cycle bound attained)",
              D0 == exp and Ks == exp)


# ============================================================ Node 2 controls
def node2():
    # E1: stencil table for q = 2
    tab = [g2(s) for s in range(7)]
    check("E1 binary stencil value is 1 exactly for neighbour sums {2,3,4}: " + str(tab),
          tab == [0, 0, 1, 1, 1, 0, 0])

    # E2: complement invariance and the 16 parity-uniform backgrounds
    ok = all(g2(sum(y)) == g2(sum(1 - b for b in y)) for y in product((0, 1), repeat=6))
    n = 4
    S = sites(n)
    pats = {"0": {i: 0 for i in S}, "1": {i: 1 for i in S},
            "cb": {i: sum(i) % 2 for i in S}, "1+cb": {i: 1 - sum(i) % 2 for i in S}}
    const_on_nbhd = all(len({c[j] for j in nbrs(i, n)}) == 1 for c in pats.values() for i in S)
    sol = True
    for c0, c1 in product(pats.values(), repeat=2):
        prev, cur = c0, c1
        for _ in range(2):
            nxt = {i: g2(sum(cur[j] for j in nbrs(i, n))) ^ prev[i] for i in S}
            prev, cur = cur, nxt
        if not (prev == c0 and cur == c1):  # period 2
            sol = False
    check("E2 g(y)=g(complement y) on all 64 neighbourhoods; the 4 parity-uniform patterns are "
          "constant on every neighbourhood; all 16 (c_even, c_odd) backgrounds are period-2 "
          "solutions (n=4)", ok and const_on_nbhd and sol)

    # E3: box closure on the n=6 torus; countercontrol at side n-1
    n = 6
    boxes = [((0, 0, 0), (0, 0, 0)), ((0, 0, 0), (1, 0, 0)), ((0, 0, 0), (1, 1, 0)),
             ((0, 0, 0), (1, 1, 1)), ((0, 0, 0), (2, 1, 0)), ((0, 0, 0), (3, 3, 3)),
             ((0, 0, 0), (3, 5, 5))]  # last: sides 4,6,6 (full extent in y,z)
    closed = all(is_closed(box(lo, hi), n) for lo, hi in boxes[:-1])
    full_ok = is_closed(box(*boxes[-1]), n)  # side 4 <= n-2, full torus in y,z: closed
    counter = not is_closed(box((0, 0, 0), (4, 0, 0)), n)  # side 5 = n-1: not closed
    check("E3 boxes with every side <= n-2 (or the full extent) are closed on the n=6 torus; "
          "a box of side n-1 is not (countercontrol)", closed and full_ok and counter)

    # E4: exhaustive one-step confinement for all 2^16 perturbations of a 2x2x2 box,
    # on the vacuum and on the (cb, 1+cb) background; perturbation dynamics identical.
    n = 6
    B = sorted(box((1, 1, 1), (2, 2, 2)))
    W = sorted(set(B) | {j for i in B for j in nbrs(i, n)})
    Wn = {i: nbrs(i, n) for i in W}
    bgs = {"vacuum": ({i: 0 for i in sites(n)}, {i: 0 for i in sites(n)}),
           "(cb,1+cb)": ({i: sum(i) % 2 for i in sites(n)},
                         {i: 1 - sum(i) % 2 for i in sites(n)})}
    conf_ok, same_ok = True, True
    vac_next = {}
    for name, (b_prev, b_cur) in bgs.items():
        b_next = b_prev  # background has period 2
        for bits in product((0, 1), repeat=16):
            yp = dict(zip(B, bits[:8]))
            yc = dict(zip(B, bits[8:]))
            xp = lambda i: b_prev[i] ^ yp.get(i, 0)
            xc = lambda i: b_cur[i] ^ yc.get(i, 0)
            pert = tuple(g2(sum(xc(j) for j in Wn[i])) ^ xp(i) ^ b_next[i] for i in W)
            if any(v for i, v in zip(W, pert) if i not in yp):
                conf_ok = False
            if name == "vacuum":
                vac_next[bits] = pert
            elif vac_next[bits] != pert:
                same_ok = False
    check("E4 all 65536 two-slice perturbations of a 2x2x2 box stay in the box for one step, "
          "on the vacuum and on the (cb,1+cb) background (the inverse step has the same form)",
          conf_ok)
    check("E4b the perturbation's next slice is identical on both backgrounds (symmetry)", same_ok)

    # E5: closure invariance along trajectories, n = 10, 60 ticks
    n = 10
    pats5 = [
        ({(0, 0, 0), (2, 0, 0), (1, 1, 0), (1, 0, 2)}, {(1, 0, 0)}),
        ({(3, 3, 3), (3, 5, 3), (4, 4, 3), (2, 4, 4), (4, 3, 5)}, {(3, 4, 3), (4, 4, 4)}),
        ({(0, 0, 0), (0, 2, 0), (5, 5, 5), (5, 5, 7)}, {(0, 1, 0)}),
    ]
    inv_ok, sub_ok, moved = True, True, False
    for prev, cur in pats5:
        A0 = prev | cur
        C0 = closure2(A0, n)
        p, c = set(prev), set(cur)
        for _ in range(60):
            p, c = c, step_sets(p, c, n)
            At = p | c
            if not At <= C0:
                sub_ok = False
            if closure2(At, n) != C0:
                inv_ok = False
            if not At <= A0:
                moved = True
    check("E5 along three trajectories (60 ticks, n=10) the support stays in cl2(A0) and "
          "cl2(A_t) = cl2(A0) at every tick", inv_ok and sub_ok)
    check("E5b countercontrol: the support itself is not invariant (it leaves A0)", moved)

    # E6: component independence at distance 3; interaction at distance 2
    n = 12

    def run(prev, cur, T):
        out = []
        p, c = set(prev), set(cur)
        for _ in range(T):
            p, c = c, step_sets(p, c, n)
            out.append(frozenset(c))
        return out

    a_cur = {(1, 1, 1), (3, 1, 1)}
    a_prev = {(2, 1, 1)}

    def shift(S, d):
        return {((x + d) % n, y, z) for x, y, z in S}

    ok3 = True
    for d, expect_same in ((5, True), (4, False)):
        joint = run(a_prev | shift(a_prev, d), a_cur | shift(a_cur, d), 40)
        A = run(a_prev, a_cur, 40)
        Bs = run(shift(a_prev, d), shift(a_cur, d), 40)
        same = all(j == (x | y) for j, x, y in zip(joint, A, Bs))
        if same != expect_same:
            ok3 = False
    check("E6 two clusters at l1-distance 3 evolve exactly as if alone (40 ticks); at distance 2 "
          "they interact (countercontrol)", ok3)

    # E7: three-site closed apparatus {-e1,0,e1}: permutation, period 4, readiness by un-writing
    n = 6
    Bx = [(5, 0, 0), (0, 0, 0), (1, 0, 0)]
    perm = {}
    closed_ok = True
    for bits in product((0, 1), repeat=6):
        p = {s for s, b in zip(Bx, bits[:3]) if b}
        c = {s for s, b in zip(Bx, bits[3:]) if b}
        nx = step_sets(p, c, n)
        if not nx <= set(Bx):
            closed_ok = False
        perm[bits] = bits[3:] + tuple(1 if s in nx else 0 for s in Bx)
    bij = len(set(perm.values())) == 64
    per_ok = True
    for s in perm:
        t, k = perm[s], 1
        while t != s:
            t, k = perm[t], k + 1
        if 4 % k:
            per_ok = False
    # law: centre ready (0,0); ends uniform on both slices
    law = {}
    for a, b, a2, b2 in product((0, 1), repeat=4):
        law[(a, 0, b, a2, 0, b2)] = Fr(1, 16)
    ready, K_ok = [], True
    for t in range(5):
        ready.append(marg(law, lambda s: (s[1], s[4])).get((0, 0), 0))
        # centre is a function of the ends at every t (H(centre|ends)=0), so K(centre)=2=D0
        fn = {}
        for s in law:
            key = (s[0], s[2], s[3], s[5])
            if fn.setdefault(key, (s[1], s[4])) != (s[1], s[4]):
                K_ok = False
        law = push(law, lambda s: perm[s])
    check("E7 apparatus box {-e1,0,e1} is closed; its dynamics is a bijection of 64 states with "
          "every orbit length dividing 4", closed_ok and bij and per_ok)
    check("E7b centre readiness 1,3/4,9/16,3/4,1 at t=0..4 while K(centre)=2=D0 at every t "
          "(in this box readiness returns when the record is un-written): " + str([str(x) for x in ready]),
          ready == [1, Fr(3, 4), Fr(9, 16), Fr(3, 4), 1] and K_ok)

    # E12: the review's example (#1425 c.7023337287): closed segment {0..4}e1 in the vacuum,
    # x_{-1} = 0, x_0 = (c,0,1,0,1), carrier c at site 0, H = site 1, w* = (0,0).
    n = 8
    seg = [(k, 0, 0) for k in range(5)]
    traj, orbit_len = {}, {}
    closed12 = True
    for cval in (0, 1):
        p, c = set(), {s for s, b in zip(seg, (cval, 0, 1, 0, 1)) if b}
        start = (frozenset(p), frozenset(c))
        tr = [(set(p), set(c))]
        for t in range(1, 13):
            p, c = c, step_sets(p, c, n)
            if not (p | c) <= set(seg):
                closed12 = False
            tr.append((set(p), set(c)))
        orbit_len[cval] = next(t for t in range(1, 13)
                               if (frozenset(tr[t][0]), frozenset(tr[t][1])) == start)
        traj[cval] = tr
    H1 = (1, 0, 0)
    W = {cv: [(int(H1 in traj[cv][t][0]), int(H1 in traj[cv][t][1])) for t in range(13)]
         for cv in (0, 1)}
    ready0 = W[0][0] == W[1][0] == (0, 0)
    dep = all(W[0][t] != W[1][t] for t in (1, 2, 3, 4))
    ready5 = W[0][5] == W[1][5] == (0, 0)
    rec = all(int((3, 0, 0) in traj[cv][5][1]) == 1 - cv for cv in (0, 1))
    check(f"E12 review example on the n=8 torus: segment closed; orbit lengths {orbit_len[0]} "
          f"(c=0) and {orbit_len[1]} (c=1), common period 12; H ready at t=0, depends on c at "
          "t=1..4, ready at t=5 for both c, while site 3 holds not-c at t=5",
          closed12 and orbit_len == {0: 4, 1: 6} and ready0 and dep and ready5 and rec)
    site3_t0 = {cv: (int((3, 0, 0) in traj[cv][0][0]), int((3, 0, 0) in traj[cv][0][1]))
                for cv in (0, 1)}
    check("E12b clause (R) for E12: site 3 carries no information about c before the first use "
          "(t=0)", site3_t0[0] == site3_t0[1])

    # E13: the re-review's example (#1425 c.7023506974): segment {0..4}e1, n=8 torus;
    # (x_{-1}, x_0) per site: 0:(a,a) 1:(1,1) 2:(1,1) 3:(b,0) 4:(1,1); H = site 1, w* = (1,1).
    n = 8
    init = lambda a, b: [(a, a), (1, 1), (1, 1), (b, 0), (1, 1)]
    TR, OL, closed13 = {}, {}, True
    for a, b in product((0, 1), repeat=2):
        p = {s for s, v in zip(seg, init(a, b)) if v[0]}
        c = {s for s, v in zip(seg, init(a, b)) if v[1]}
        start = (frozenset(p), frozenset(c))
        tr = [(set(p), set(c))]
        for t in range(1, 25):
            p, c = c, step_sets(p, c, n)
            if not (p | c) <= set(seg):
                closed13 = False
            tr.append((set(p), set(c)))
        OL[(a, b)] = next(t for t in range(1, 25)
                          if (frozenset(tr[t][0]), frozenset(tr[t][1])) == start)
        TR[(a, b)] = tr

    def content(k, t, sites_):
        return tuple((int(s in TR[k][t][0]), int(s in TR[k][t][1])) for s in sites_)

    def depends(t, var, sites_):
        """exact I(content; var) > 0 for uniform independent (a, b)."""
        d = [sorted(content(k, t, sites_) for k in TR if k[var] == v) for v in (0, 1)]
        return d[0] != d[1]

    Hs = [(1, 0, 0)]
    ready13 = [t for t in range(17) if all(content(k, t, Hs) == ((1, 1),) for k in TR)]
    use_a = [t for t in range(17) if depends(t, 0, Hs)]
    use_b = [t for t in range(17) if depends(t, 1, Hs)]
    logs = [(2, 0, 0), (4, 0, 0)]
    det16 = len({content(k, 16, logs) for k in TR}) == 4
    check(f"E13 re-review example: segment closed; orbit lengths {sorted(OL.values())}; H ready "
          f"at {[t for t in ready13 if t in (0, 4, 16)]}; H depends on a at t={use_a[:3]}, on b exactly "
          f"at t={use_b}; sites 2,4 at t=16 determine (a,b)",
          closed13 and sorted(OL.values()) == [4, 6, 6, 12] and {0, 4, 16} <= set(ready13)
          and use_a[:3] == [1, 2, 3] and use_b == [5, 6, 7, 8, 9, 10] and det16)
    # clause (R): a log block that determines the carrier at t=16 and carries no information
    # about it at any time before the carrier's first use
    def R_ok(var, first_use):
        for L_ in ([logs[0]], [logs[1]], logs):
            det = all(len({content(k, 16, L_) for k in TR if k[var] == v}
                          & {content(k, 16, L_) for k in TR if k[var] == 1 - v}) == 0
                      for v in (0, 1))
            if det and not any(depends(t, var, L_) for t in range(first_use)):
                return True
        return False
    check("E13b clause (R) at t=16: holds for carrier a (first use t=1); fails for carrier b "
          "(first use t=5): every log block determining b at t=16 already depends on b before t=5",
          R_ok(0, use_a[0]) and not R_ok(1, use_b[0]))

    # E14: reduced exact search (pure vacuum supply, carriers in the box, eps = 0, horizon 30).
    # A delivery: t1 < s < t2 with H at (0,0) at t1 and t2 for all carrier values, I(W_s(H); c_k) > 0,
    # and the non-carrier, non-H sites at t2 determining c_k. In-box dynamics is exact (Lemma 2.3(a)).
    def boxsites(dims):
        S_ = list(product(*[range(d) for d in dims]))
        ix = {s: i for i, s in enumerate(S_)}
        NB_ = []
        for s_ in S_:
            nb = []
            for ax in range(len(dims)):
                for d in (1, -1):
                    t_ = list(s_)
                    t_[ax] += d
                    if tuple(t_) in ix:
                        nb.append(ix[tuple(t_)])
            NB_.append(nb)
        return S_, NB_

    def found(dims, ncar, T=30, base=None, only=None):
        from itertools import combinations
        S_, NB_ = boxsites(dims)
        k_ = len(S_)
        bp, bc = base if base else ([0] * k_, [0] * k_)
        for cs in (combinations(range(k_), ncar) if only is None else [only]):
            for modes in product((0, 1, 2), repeat=ncar):
                trs = []
                for cv in product((0, 1), repeat=ncar):
                    p_, c_ = list(bp), list(bc)
                    for s_, m_, v_ in zip(cs, modes, cv):
                        if m_ in (0, 2):
                            c_[s_] = v_
                        if m_ in (1, 2):
                            p_[s_] = v_
                    tr = [(tuple(p_), tuple(c_))]
                    for _ in range(T):
                        p_, c_ = c_, [g2(sum(c_[j] for j in NB_[i])) ^ p_[i] for i in range(k_)]
                        tr.append((tuple(p_), tuple(c_)))
                    trs.append((cv, tr))
                for H_ in range(k_):
                    if H_ in cs:
                        continue
                    logs_ = [s_ for s_ in range(k_) if s_ not in cs and s_ != H_]
                    ready_ = [all(tr[t][0][H_] == 0 and tr[t][1][H_] == 0 for _, tr in trs)
                              for t in range(T + 1)]
                    for kk in range(ncar):
                        dep_ = [sorted((tr[t][0][H_], tr[t][1][H_]) for cv, tr in trs if cv[kk] == 0)
                                != sorted((tr[t][0][H_], tr[t][1][H_]) for cv, tr in trs if cv[kk] == 1)
                                for t in range(T + 1)]
                        for t1 in range(T + 1):
                            if not ready_[t1]:
                                continue
                            for t2 in range(t1 + 2, T + 1):
                                if not ready_[t2] or not any(dep_[t1 + 1:t2]):
                                    continue
                                m_ = {}
                                ok_ = True
                                for cv, tr in trs:
                                    key = tuple(tr[t2][0][s_] for s_ in logs_) + \
                                        tuple(tr[t2][1][s_] for s_ in logs_)
                                    if m_.setdefault(key, cv[kk]) != cv[kk]:
                                        ok_ = False
                                        break
                                if ok_:
                                    return True
        return False

    cases = [((3,), 1), ((4,), 1), ((4,), 2), ((5,), 1), ((5,), 2), ((6,), 1), ((6,), 2),
             ((7,), 1), ((7,), 2), ((2, 2), 1), ((2, 2), 2), ((2, 3), 1), ((2, 3), 2),
             ((3, 3), 1), ((3, 3), 2), ((4,), 3), ((5,), 3), ((6,), 3), ((2, 3), 3)]
    none = all(not found(d, k) for d, k in cases)
    positive = found((5,), 1, base=([0] * 5, [0, 0, 1, 0, 1]), only=(0,))
    check("E14 reduced exact search, pure vacuum supply: no delivery with a determined log in lines "
          "3..7 and boxes 2x2, 2x3, 3x3 with 1-2 carriers, lines 4..6 and 2x3 with 3 carriers "
          "(horizon 30); evidence only", none)
    check("E14b positive control: the same search routine finds the E12 delivery when given its "
          "designed pattern", positive)

    # E8: q >= 3 countercontrol (insulation fails): single value 2 at the origin
    ok8 = True
    for q in (3, 2 ** 16):
        n = 6
        cur = {i: 0 for i in sites(n)}
        cur[(0, 0, 0)] = 2
        nxt = {i: (gq(sum(cur[j] for j in nbrs(i, n)), q) - 0) % q for i in sites(n)}
        leaked = [i for i in nbrs((0, 0, 0), n) if nxt[i] != 0]
        if len(leaked) != 6:
            ok8 = False
    check("E8 countercontrol q=3 and q=2^16: a single symbol 2 in the vacuum reaches all six "
          "neighbours in one step (no box confinement)", ok8)
    # E8b countercontrol: the SM 3.1 ring rule f_i = X_(i-1) XOR (X_(i+1) OR X_(i+2)),
    # F(X,Y) = (f(X) XOR Y, X): a single excitation of its vacuum spreads in one step
    Lr = 9
    X = [0] * Lr
    X[0] = 1
    f = [X[(i - 1) % Lr] ^ (X[(i + 1) % Lr] | X[(i + 2) % Lr]) for i in range(Lr)]
    spread = sorted(i if i <= Lr // 2 else i - Lr for i in range(Lr) if f[i])
    check(f"E8b countercontrol SM 3.1 ring (L=9): a single excitation reaches sites {spread} "
          "in one step (insulation is specific to the binary rounded-cubic rule)",
          spread == [-2, -1, 1])

    # E9: noise controls
    surv = Fr(sum(1 for y in product((0, 1), repeat=6) if g2(sum(y)) == 0), 64)
    def pert(k):
        return Fr(sum(1 for y in product((0, 1), repeat=k) if g2(sum(y)) == 1), 2 ** k)
    check(f"E9 a ready site in product-uniform noise stays 0 w.p. {surv} (= 1 - 25/32); a vacuum "
          f"site with 1/2/3 noisy neighbours is perturbed w.p. {pert(1)}/{pert(2)}/{pert(3)}",
          surv == Fr(7, 32) and (pert(1), pert(2), pert(3)) == (0, Fr(1, 4), Fr(1, 2)))

    # E10: slab insulation; E11: bounded vacuum box in noise has full closure
    n = 6
    slab2 = box((0, 0, 0), (1, 5, 5))
    comp2 = set(sites(n)) - slab2
    slab1 = box((0, 0, 0), (0, 5, 5))
    comp1 = set(sites(n)) - slab1
    check("E10 the complement of a width-2 slab is closed (noise never enters the slab); "
          "for width 1 it is not (countercontrol)",
          is_closed(comp2, n) and not is_closed(comp1, n))
    n = 8
    V = box((2, 2, 2), (4, 4, 4))
    check("E11 bounded vacuum box 3x3x3 in noise (n=8): cl2(exterior) = whole torus",
          closure2(set(sites(n)) - V, n) == set(sites(n)))


# ============================================================ Node 3 controls
def node3():
    # M1: PREP-REGRESS C13 system: the 'gained' block was at its level already at t0
    law = {(0, 0): Fr(1, 2), (0, 1): Fr(1, 2)}  # mu-O on {00, 01}
    phi = lambda s: (s[0], 1 - s[1]) if s[0] == 0 else s
    def K(law, idx):
        Hj = entropy(law)
        Hr = entropy(marg(law, lambda s: s[1 - idx]))
        return L(1) - (Hj - Hr)
    K0_cell0, K0_cell1 = K(law, 0), K(law, 1)
    law1 = push(law, phi)
    K1_cell0 = K(law1, 0)
    check("M1 external schedule cell1@t0 -> cell0@t1 'gains' 0 -> 1, but K_t0(cell0) = "
          "K_t1(cell0) = 1 (relabelling)", K0_cell1 == L(0) and K0_cell0 == L(1) and K1_cell0 == L(1))

    # M2: native pointer under mu-O
    S = [(q, h) for q in range(3) for h in product((0, 1), repeat=3)]
    phi2 = lambda s: ((s[0] + 1) % 3, (s[1][2], s[1][0], s[1][1]))
    s0 = (0, (0, 1, 1))
    orbit, s = [s0], phi2(s0)
    while s != s0:
        orbit.append(s)
        s = phi2(s)
    muO = {o: Fr(1, len(orbit)) for o in orbit}
    inv = push(muO, phi2) == muO
    p_ptr = sum(p for (q, h), p in muO.items() if h[q] == 0)
    p_fixed = [sum(p for (q, h), p in muO.items() if h[j] == 0) for j in range(3)]
    p_ext, lw = [], dict(muO)
    for t in range(3):
        p_ext.append(sum(p for (q, h), p in lw.items() if h[t % 3] == 0))
        lw = push(lw, phi2)
    uE = Fr(sum(1 for (q, h) in S if h[q] == 0), len(S))
    D_muO = log2_23(Fr(len(S), len(orbit)))
    # d(1 || 1/2) = 1 bit <= D(muO||u) = log2(24/3) = 3 bits
    check(f"M2 mu-O invariant (orbit length {len(orbit)}); pointer-selected cell ready w.p. "
          f"{p_ptr}; each fixed cell and the external schedule w.p. {p_fixed[0]} / "
          f"{[str(x) for x in p_ext]}; u(H_Q=0) = {uE}; cost d(1||1/2)=1 <= D(muO||u) = 3",
          inv and p_ptr == 1 and p_fixed == [Fr(1, 3)] * 3 and p_ext == [Fr(1, 3)] * 3
          and uE == Fr(1, 2) and D_muO == L(3))
    # M2c countercontrol: a 'pointer' computed from the cells themselves (first zero cell)
    first0 = lambda h: next((j for j in range(3) if h[j] == 0), 0)
    uE2 = Fr(sum(1 for (q, h) in S if h[first0(h)] == 0), len(S))
    check(f"M2c countercontrol: selection by the cells' own content has u-mass {uE2} "
          "(= 7/8), so disjointness of pointer and cells is needed", uE2 == Fr(7, 8))

    # M3: blinker orbit on the n=4 torus
    n = 4
    p, c = set(), {(0, 0, 0)}
    start, k = (frozenset(p), frozenset(c)), 0
    while True:
        p, c = c, step_sets(p, c, n)
        k += 1
        if (frozenset(p), frozenset(c)) == start:
            break
    D_bits = 2 * n ** 3 - 1  # log2(2^(2N)/2)
    check(f"M3 single excitation in the vacuum (n=4) has orbit length {k}, so D(mu-O||u) = "
          f"{D_bits} bits and every block has entropy <= log2({k}) = 1 bit under mu-O",
          k == 2 and D_bits == 127)


def main():
    node1()
    node2()
    node3()
    bad = [n for n, ok in RESULTS if not ok]
    print(f"{len(RESULTS) - len(bad)}/{len(RESULTS)} checks hold")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
