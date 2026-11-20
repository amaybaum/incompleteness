#!/usr/bin/env python3
"""A1-EXIT Q1 exact checks (stdlib only, deterministic). Exit status 0 iff every check passes.

Notation: P is the period lattice (P = 0 is Z^3), X_P = Z^3/P the quotient carrier, given by a
lower-triangular Hermite basis B (rows (a,0,0), (x,c,0), (y,z,f)). A corner eta in {0,1}^3 has
character chi_eta(n) = (-1)^(eta.n).

Parts
  K   Controls. K1: on a window of Z^3 nearest-neighbour hopping is odd-supported for the
      coordinate-sum parity and both parities occur (Theorem 3's kernel hypotheses). K3: O-A4's
      countermodels reproduce (bipartiteness, corner counts, stabilizer orders 720 and 48). K4: odd
      cubic tori do not carry the staggered phases. K5: the disguised-A1 test separates a class
      that contains P = 0 from one that requires finite index.
  A   Brute-force (edge-consistency) well-definedness of every corner character, of the checkerboard
      and of the staggered phases of every axis ordering, on 125 rectangular tori and on skew and
      cubic-invariant quotients; compared with the closed-form conditions on P.
  B   Theorem 2 on Z^3: the phase-shift fields of Staggered.Gens for axes 0-2 and the padding, and
      (sum_i A_i)^2 = sum_i S_i^2 applied to delta_m for the 8 classes m mod 2 (the operators commute
      with translations by 2Z^3, so this covers every m). The same identity on the non-bipartite
      torus 4x4x3 (two-step-stencil reading); failure of the phases on 3x3x4 for every axis ordering;
      no Gens instance on 4x4x3; the blocked-lattice reading needs P in 2Z^3.
  C   Graph automorphisms fixing a vertex, and their action on the corner characters: cubic torus
      L = 6 (triplet lines form one orbit), L = 4 (the corner span is not invariant), the
      non-cubic-invariant torus 4x4x6 (no automorphism maps the X_3 line to the X_1 line); taste-cell
      spectra on 4x4x6 (illustration).
  D   Hypercube blocking n = 2y + eta is well defined on X_P iff P is in 2Z^3.
  E   Cubic-invariant period lattices: exhaustive Hermite enumeration of all sublattices of index
      <= NMAX; the O-invariant ones are exactly m Z^3, m D_3, m B_3; those inside 2Z^3 are listed.
  F   Theorem 8b: chi_eta is an eigenfunction of the normalized neighbour average with eigenvalue
      sigma(eta)/3 on every quotient on which it is defined.
Run:  python3 -I verification/audits/foundations/a1exit-q1-20261120/checks/q1_checks.py
"""
from fractions import Fraction
from itertools import product, permutations
import sys

FAIL = []
CORNERS = list(product((0, 1), repeat=3))
E3 = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
NMAX = 96


def check(label, ok, detail=""):
    print(f"{'PASS' if ok else 'FAIL'}  {label}{(': ' + detail) if detail else ''}")
    if not ok:
        FAIL.append(label)


def add(u, v):
    return tuple(a + b for a, b in zip(u, v))


def sub(u, v):
    return tuple(a - b for a, b in zip(u, v))


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


# ------------------------------------------------------------------ quotient carriers
def reduce_(v, B):
    v = list(v)
    for k in reversed(range(3)):
        f = v[k] // B[k][k]
        v = [v[t] - f * B[k][t] for t in range(3)]
    return tuple(v)


class Quotient:
    def __init__(self, name, B):
        self.name, self.B = name, B
        self.reps = [(a, b, c) for a in range(B[0][0]) for b in range(B[1][1]) for c in range(B[2][2])]
        self.idx = {r: t for t, r in enumerate(self.reps)}
        self.N = len(self.reps)

    def nb(self, t, e, s=1):
        r = self.reps[t]
        return self.idx[reduce_(add(r, tuple(s * x for x in e)), self.B)]

    def adj(self):
        return [[self.nb(t, e, s) for e in E3 for s in (1, -1)] for t in range(self.N)]


def rect(a, b, c):
    return Quotient(f"{a}x{b}x{c}", [[a, 0, 0], [0, b, 0], [0, 0, c]])


def sign_function_defined(Q, signs):
    """Is there a function g on X_P with g(0) = 1 and g(n + e_j) = signs[j] g(n)?  Brute force:
    propagate from 0 along edges and test every edge for consistency."""
    g = {0: 1}
    order = [0]
    for t in order:
        for j, e in enumerate(E3):
            for s in (1, -1):
                u = Q.nb(t, e, s)
                val = g[t] * signs[j]
                if u not in g:
                    g[u] = val
                    order.append(u)
                elif g[u] != val:
                    return False
    return True


def corner_defined(Q, eta):
    return sign_function_defined(Q, [(-1) ** x for x in eta])


def basis_rows(Q):
    return Q.B


def cf_corner(B, eta):  # closed form: eta.b even for every period vector b
    return all(dot(eta, b) % 2 == 0 for b in B)


def cf_even_sum(B):
    return all(sum(b) % 2 == 0 for b in B)


def cf_in_2Z3(B):
    return all(x % 2 == 0 for b in B for x in b)


def phase_etas(order):
    """Characters needed by the staggered phases for axis ordering `order`: e_k = (-1)^(sum of
    coordinates of the axes preceding k in the order)."""
    out = []
    for k in range(3):
        eta = [0, 0, 0]
        for j in order[:k]:
            eta[j] = 1
        out.append(tuple(eta))
    return out


def phases_defined(Q, order):
    return all(corner_defined(Q, eta) for eta in phase_etas(order))


def cf_phases_some_order(B):
    """Closed form: some axis a such that every period vector is even off a."""
    return any(all(b[j] % 2 == 0 for b in B for j in range(3) if j != a) for a in range(3))


def bipartite(Q):
    adj = Q.adj()
    col = {0: 0}
    order = [0]
    for u in order:
        for w in adj[u]:
            if w not in col:
                col[w] = 1 - col[u]
                order.append(w)
            elif col[w] == col[u]:
                return False
    return True


def o_invariant(B):
    gens = [lambda v: (-v[1], v[0], v[2]), lambda v: (v[1], v[2], v[0])]
    return all(reduce_(g(b), B) == (0, 0, 0) for g in gens for b in B)


# ------------------------------------------------------------------ automorphisms
def bfs_dist(adj, s):
    dist = {s: 0}
    order = [s]
    for u in order:
        for w in adj[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                order.append(w)
    return dist, order


def stabilizer_maps(adj, s=0):
    nbset = [set(a) for a in adj]
    dist, order = bfs_dist(adj, s)
    n = len(adj)
    by_dist = {}
    for v, dv in dist.items():
        by_dist.setdefault(dv, []).append(v)
    out, img, used = [], {s: s}, {s}

    def rec(k):
        if k == len(order):
            out.append(dict(img))
            return
        v = order[k]
        if v in img:
            rec(k + 1)
            return
        assigned = [w for w in adj[v] if w in img]
        for x in by_dist[dist[v]]:
            if x in used:
                continue
            if all(img[w] in nbset[x] for w in assigned):
                img[v] = x
                used.add(x)
                rec(k + 1)
                del img[v]
                used.discard(x)

    rec(0)
    return [m for m in out if all(m[w] in nbset[m[v]] for v in range(n) for w in adj[v])]


def char_vec(Q, eta):
    return tuple((-1) ** dot(eta, r) for r in Q.reps)


def corner_action(Q, maps):
    """For each automorphism m and defined corner eta, the pulled-back function chi_eta o m.
    Returns (span_preserved, line_orbits) where line_orbits partitions the defined corners by the
    induced action on the lines R chi_eta (only meaningful if span_preserved)."""
    defined = [eta for eta in CORNERS if corner_defined(Q, eta)]
    vecs = {eta: char_vec(Q, eta) for eta in defined}
    lookup = {}
    for eta, v in vecs.items():
        lookup[v] = eta
        lookup[tuple(-x for x in v)] = eta
    preserved = True
    edges = {eta: {eta} for eta in defined}
    for m in maps:
        for eta in defined:
            v = vecs[eta]
            w = tuple(v[m[t]] for t in range(Q.N))
            if w not in lookup:
                preserved = False
            else:
                edges[eta].add(lookup[w])
    # orbits by closure
    orbits, seen = [], set()
    for eta in defined:
        if eta in seen:
            continue
        orb, stack = set(), [eta]
        while stack:
            x = stack.pop()
            if x in orb:
                continue
            orb.add(x)
            stack.extend(edges[x])
        seen |= orb
        orbits.append(sorted(orb))
    return preserved, orbits, defined


# ------------------------------------------------------------------ K
def part_K():
    print("== K. controls ==")
    # K1: Theorem 3 hypotheses on a window of Z^3
    R = 4
    win = list(product(range(-R, R + 1), repeat=3))
    par = {n: sum(n) % 2 for n in win}
    odd_supported = all(par[n] != par.get(add(n, e), 1 - par[n]) for n in win for e in E3)
    both = {0, 1} <= set(par.values())
    check("K1 Z^3 window: nearest-neighbour hopping is odd-supported for the coordinate-sum parity; "
          "both parities occur", odd_supported and both)
    # K3: O-A4 countermodels
    expect = {"L=3": (False, 1), "L=4": (True, 8), "L=5": (False, 1), "L=6": (True, 8),
              "skew even-sum <(4,0,0),(0,4,0),(1,1,4)>": (True, 4)}
    qs = {"L=3": rect(3, 3, 3), "L=4": rect(4, 4, 4), "L=5": rect(5, 5, 5), "L=6": rect(6, 6, 6),
          "skew even-sum <(4,0,0),(0,4,0),(1,1,4)>":
              Quotient("skew4", [[4, 0, 0], [0, 4, 0], [1, 1, 4]])}
    for name, Q in qs.items():
        got = (bipartite(Q), sum(corner_defined(Q, eta) for eta in CORNERS))
        check(f"K3 {name}: (bipartite, corners) = {got}", got == expect[name], f"O-A4 expects {expect[name]}")
    for L, order in [(4, 720), (6, 48)]:
        Q = rect(L, L, L)
        n = len(stabilizer_maps(Q.adj()))
        check(f"K3 cubic torus L={L}: vertex stabilizer order {n}", n == order, f"O-A4 expects {order}")
    # K4: odd cubic tori carry no staggered phases for any axis ordering
    for L in (3, 5):
        Q = rect(L, L, L)
        bad = [o for o in permutations(range(3)) if phases_defined(Q, o)]
        check(f"K4 cubic torus L={L}: staggered phases defined for no axis ordering", not bad)
    # K5: disguised-A1 test is live
    def da1(pred):
        return pred([])  # P = 0: no period vectors
    q_good = lambda B: all(x % 2 == 0 for b in B for x in b)
    q_disguised = lambda B: len(B) == 3 and q_good(B)  # requires finite index
    check("K5 disguised-A1 test: 'P in 2Z^3' contains P = 0; 'finite-index P in 2Z^3' does not",
          da1(q_good) and not da1(q_disguised))


# ------------------------------------------------------------------ A
def test_lattices():
    out = [rect(a, b, c) for a in range(2, 7) for b in range(2, 7) for c in range(2, 7)]
    skews = [("skew4 <(4,0,0),(0,4,0),(1,1,4)>", [[4, 0, 0], [0, 4, 0], [1, 1, 4]]),
             ("skew5 <(5,0,0),(0,5,0),(1,2,5)>", [[5, 0, 0], [0, 5, 0], [1, 2, 5]]),
             ("skew <(4,0,0),(0,4,0),(2,2,4)>", [[4, 0, 0], [0, 4, 0], [2, 2, 4]]),
             ("skew <(4,0,0),(2,4,0),(0,0,4)>", [[4, 0, 0], [2, 4, 0], [0, 0, 4]]),
             ("skew <(3,0,0),(1,4,0),(0,0,4)>", [[3, 0, 0], [1, 4, 0], [0, 0, 4]]),
             ("2D_3 <(4,0,0),(2,2,0),(2,0,2)>", [[4, 0, 0], [2, 2, 0], [2, 0, 2]]),
             ("2B_3 <(4,0,0),(0,4,0),(2,2,2)>", [[4, 0, 0], [0, 4, 0], [2, 2, 2]]),
             ("4D_3 <(8,0,0),(4,4,0),(4,0,4)>", [[8, 0, 0], [4, 4, 0], [4, 0, 4]]),
             ("D_3-type 3D_3 <(6,0,0),(3,3,0),(3,0,3)>", [[6, 0, 0], [3, 3, 0], [3, 0, 3]])]
    out += [Quotient(n, B) for n, B in skews]
    return out


def part_A():
    print("== A. corner characters, checkerboard, staggered phases: brute force vs closed form ==")
    lat = test_lattices()
    mism = []
    stats = {"corners8": 0, "bip": 0, "phases": 0, "n": 0}
    for Q in lat:
        stats["n"] += 1
        for eta in CORNERS:
            if corner_defined(Q, eta) != cf_corner(Q.B, eta):
                mism.append((Q.name, "corner", eta))
        b = bipartite(Q)
        if b != cf_even_sum(Q.B):
            mism.append((Q.name, "bipartite"))
        if b != corner_defined(Q, (1, 1, 1)):
            mism.append((Q.name, "checkerboard=corner(1,1,1)"))
        all8 = all(corner_defined(Q, eta) for eta in CORNERS)
        if all8 != cf_in_2Z3(Q.B):
            mism.append((Q.name, "all eight"))
        ph = any(phases_defined(Q, o) for o in permutations(range(3)))
        if ph != cf_phases_some_order(Q.B):
            mism.append((Q.name, "phases"))
        stats["corners8"] += all8
        stats["bip"] += b
        stats["phases"] += ph
    check(f"A brute force = closed form on {stats['n']} quotients (corner characters, checkerboard, all eight "
          f"corners iff P in 2Z^3, phases of some ordering iff P even off one axis)", not mism,
          f"{mism[:5]}" if mism else
          f"all eight corners on {stats['corners8']}, bipartite on {stats['bip']}, phases on {stats['phases']}")
    # strictness witnesses
    Q = rect(4, 4, 3)
    check("A 4x4x3: staggered phases (ordering 1,2,3) defined; not bipartite; corners defined 4 of 8",
          phases_defined(Q, (0, 1, 2)) and not bipartite(Q)
          and sum(corner_defined(Q, e) for e in CORNERS) == 4)
    Q = Quotient("skew4", [[4, 0, 0], [0, 4, 0], [1, 1, 4]])
    check("A skew even-sum quotient: bipartite, but staggered phases defined for no ordering",
          bipartite(Q) and not any(phases_defined(Q, o) for o in permutations(range(3))))


# ------------------------------------------------------------------ B
# Finite-range operators act on finitely supported functions stored as dicts {site: value}.
def apply_shift(f, j, s, Q=None):
    # (T f)(n) = f(n + s e_j)  =>  support moves by -s e_j
    e = tuple(-s * x for x in E3[j])
    out = {}
    for n, v in f.items():
        m = add(n, e)
        if Q is not None:
            m = reduce_(m, Q.B)
        out[m] = out.get(m, 0) + v
    return {k: v for k, v in out.items() if v}


def apply_eta(f, eta):
    return {n: v * (-1) ** dot(eta, n) for n, v in f.items()}


def lin(*terms):
    out = {}
    for c, f in terms:
        for n, v in f.items():
            out[n] = out.get(n, 0) + c * v
    return {k: v for k, v in out.items() if v}


def S_op(f, j, Q=None):
    return lin((1, apply_shift(f, j, 1, Q)), (-1, apply_shift(f, j, -1, Q)))


def A_op(f, j, order, Q=None):
    return apply_eta(S_op(f, j, Q), phase_eta_for_axis(order, j))


def phase_eta_for_axis(order, j):
    k = order.index(j)
    return phase_etas(order)[k]


def D_op(f, order, Q=None):
    return lin(*[(1, A_op(f, j, order, Q)) for j in range(3)])


def part_B():
    print("== B. Theorem 2 (staggered square) on Z^3 and on quotients ==")
    order = (0, 1, 2)
    # Gens fields on Z^3 as local identities: e_i t_j = +/- t_j e_i <=> chi(n + e_j) = +/- chi(n)
    R = 3
    win = list(product(range(-R, R + 1), repeat=3))
    ok = True
    for i in range(3):
        eta = phase_eta_for_axis(order, i)
        ki = order.index(i)
        for j in range(3):
            kj = order.index(j)
            want = -1 if kj < ki else 1  # anticommute with strictly earlier axes, commute otherwise
            for n in win:
                if (-1) ** dot(eta, add(n, E3[j])) != want * (-1) ** dot(eta, n):
                    ok = False
    # padding for the N-indexed fields of Staggered.Gens: e_i = chi_(1,1,1), t_i = s_i = 0 for i >= 3;
    # the only nontrivial padded fields say that chi_(1,1,1) anticommutes with t_0, t_1, t_2
    pad = all((-1) ** dot((1, 1, 1), add(n, E3[j])) == -(-1) ** dot((1, 1, 1), n) for n in win for j in range(3))
    check("B Z^3 window: the nine phase-shift relations of Staggered.Gens for axes 0-2 hold (phases commute "
          "with own and later shifts, anticommute with earlier ones); padding e_i = chi_(1,1,1) (i >= 3) "
          "anticommutes with t_0, t_1, t_2", ok and pad)
    # factorization on Z^3, delta_m for the 8 classes mod 2
    ok = True
    for m in CORNERS:
        d = {m: 1}
        lhs = D_op(D_op(d, order), order)
        rhs = lin(*[(1, S_op(S_op(d, j), j)) for j in range(3)])
        ok &= lhs == rhs
    check("B Z^3: (sum_i A_i)^2 delta_m = sum_i S_i^2 delta_m for all 8 classes m mod 2 (so for all m: "
          "the operators commute with translations by 2Z^3)", ok)
    # countercontrol: wrong phase pattern (all phases = 1) breaks it on Z^3
    d = {(0, 0, 0): 1}
    plain = lambda f: lin(*[(1, S_op(f, j)) for j in range(3)])
    check("B countercontrol Z^3: without staggered phases (sum_i S_i)^2 != sum_i S_i^2",
          plain(plain(d)) != lin(*[(1, S_op(S_op(d, j), j)) for j in range(3)]))
    # quotient 4x4x3 (not bipartite): identity holds on every delta
    Q = rect(4, 4, 3)
    ok = all(D_op(D_op({r: 1}, order, Q), order, Q) ==
             lin(*[(1, S_op(S_op({r: 1}, j, Q), j, Q)) for j in range(3)]) for r in Q.reps)
    check("B 4x4x3 torus (not bipartite): D_st^2 = two-step stencil on every basis vector", ok)
    Q = rect(3, 3, 4)
    check("B 3x3x4 torus: staggered phases defined for no axis ordering",
          not any(phases_defined(Q, o) for o in permutations(range(3))))
    # the N-indexed Gens needs an involution anticommuting with all three shifts: on 4x4x3 the period
    # vector (0,0,3) has odd sum, and the diagonal candidate chi_(1,1,1) is not defined there
    Q = rect(4, 4, 3)
    check("B 4x4x3: the diagonal candidate chi_(1,1,1) for an involution anticommuting with t_0, t_1, t_2 is "
          "undefined (the general no-instance statement is the paper argument of RESULT section 2)",
          not corner_defined(Q, (1, 1, 1)))
    # blocked-lattice reading: the two-step shifts preserve the blocking label n mod 2 iff P in 2Z^3
    # brute force, independent of the closed form: does every two-step shift keep the parity label of
    # every representative?
    def block_local(Q):
        return all(tuple(x % 2 for x in reduce_(add(r, tuple(2 * x for x in e)), Q.B)) ==
                   tuple(x % 2 for x in r) for r in Q.reps for e in E3)
    check("B blocked-lattice reading: on 4x4x3 the two-step stencil is not block-local (no blocked lattice "
          "2Z^3/P); on 4x4x4 and 6x6x6 it is", (not block_local(rect(4, 4, 3))) and block_local(rect(4, 4, 4))
          and block_local(rect(6, 6, 6)))
    mism = [Q.name for Q in test_lattices() if block_local(Q) != cf_in_2Z3(Q.B)]
    check("B two-step stencil block-local (brute force) iff P in 2Z^3 (closed form), on all test quotients",
          not mism, f"{mism}")


# ------------------------------------------------------------------ C
def cos_turn(m, L):
    """cos(2 pi m / L) for L in {1,2,3,4,6}, exactly."""
    t = Fraction(m % L, L)
    table = {Fraction(0): 1, Fraction(1, 6): Fraction(1, 2), Fraction(1, 4): 0, Fraction(1, 3): Fraction(-1, 2),
             Fraction(1, 2): -1, Fraction(2, 3): Fraction(-1, 2), Fraction(3, 4): 0, Fraction(5, 6): Fraction(1, 2)}
    return Fraction(table[t])


def cell_spectrum(sides, eta):
    """Multiset of sigma(k) = sum cos k_i over momenta k_i = 2 pi m_i / L_i in the cell
    pi*eta + (-pi/2, pi/2]^3."""
    vals = []
    for ms in product(*[range(L) for L in sides]):
        ok = True
        for m, L, h in zip(ms, sides, eta):
            a = Fraction(m, L) - Fraction(h, 2)  # turns relative to the corner
            a = a - (a + Fraction(1, 2)).__floor__()  # into [-1/2, 1/2)
            if a == Fraction(-1, 2):
                a = Fraction(1, 2)
            if not (Fraction(-1, 4) < a <= Fraction(1, 4)):
                ok = False
        if ok:
            vals.append(sum(cos_turn(m, L) for m, L in zip(ms, sides)))
    return sorted(vals)


def part_C():
    print("== C. automorphisms of the carrier and the corner lines ==")
    Q = rect(6, 6, 6)
    maps = stabilizer_maps(Q.adj())
    pres, orbs, _ = corner_action(Q, maps)
    trip = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    check(f"C cubic torus L=6: |Stab| = {len(maps)}; corner span preserved; triplet lines one orbit; "
          f"singlet lines fixed", pres and sorted(trip) in orbs and [(0, 0, 0)] in orbs and [(1, 1, 1)] in orbs,
          f"orbits {orbs}")
    Q = rect(4, 4, 4)
    maps = stabilizer_maps(Q.adj())
    pres, orbs, _ = corner_action(Q, maps)
    check(f"C cubic torus L=4 (Q_6): |Stab| = {len(maps)}; the span of the eight corner characters is NOT "
          f"invariant under the carrier's automorphisms", not pres)
    # the corner-coupling eigenspace sigma = 1 has dimension 15 on L=4 (3 corners + 12 others)
    cnt = sum(1 for ms in product(range(4), repeat=3) if sum(cos_turn(m, 4) for m in ms) == 1)
    check("C cubic torus L=4: eigenvalue sigma = 1 has multiplicity 15 (3 corners X_j and 12 momenta "
          "(+-pi/2, +-pi/2, 0) up to axis order)", cnt == 15, f"{cnt}")
    Q = rect(4, 4, 6)
    maps = stabilizer_maps(Q.adj())
    pres, orbs, _ = corner_action(Q, maps)
    v3 = char_vec(Q, (0, 0, 1))
    images3 = {tuple(v3[m[t]] for t in range(Q.N)) for m in maps}
    fixed3 = images3 <= {v3, tuple(-x for x in v3)}
    check(f"C torus 4x4x6 (P in 2Z^3, not O-invariant): |Stab| = {len(maps)} (order 48, but not O_h); every "
          f"automorphism maps the X_3 line to itself, so none relates X_3 to X_1 or X_2",
          fixed3 and [(0, 0, 1)] in orbs,
          f"corner span preserved: {pres} (the C_4 x C_4 factor is the 4-cube, as for L=4); orbits of corner "
          f"lines mapped to corner lines {orbs}")
    links = Q.adj()[0]
    orb_sizes = sorted(len({m[a] for m in maps}) for a in links)
    check("C torus 4x4x6: the stabilizer's orbits on the six links have sizes 4 and 2 (it fixes the pair "
          "+-e_3), so it does not act as the cubic point group", sorted(set(orb_sizes)) == [2, 4],
          f"orbit size per link {orb_sizes}")
    o_inv = o_invariant(Q.B)
    check("C torus 4x4x6: P is not O-invariant; 6x6x6 is", (not o_inv) and o_invariant(rect(6, 6, 6).B))
    s1, s3 = cell_spectrum((4, 4, 6), (1, 0, 0)), cell_spectrum((4, 4, 6), (0, 0, 1))
    s1c, s3c = cell_spectrum((6, 6, 6), (1, 0, 0)), cell_spectrum((6, 6, 6), (0, 0, 1))
    check("C illustration: taste-cell spectra of sigma differ between X_1 and X_3 on 4x4x6, agree on 6x6x6",
          s1 != s3 and s1c == s3c, f"4x4x6: X_1 {[str(x) for x in s1]} vs X_3 {[str(x) for x in s3]}")
    # O-invariance is sufficient, not necessary, for a symmetry relating the triplet lines:
    # a period lattice inside 2Z^3 invariant under the cyclic axis permutation but not under O
    B = hermite([(2, 4, 0), (0, 2, 4), (4, 0, 2)])
    Q = Quotient("cyclic <(2,4,0),(0,2,4),(4,0,2)>", B)
    cyc = lambda v: (v[2], v[0], v[1])  # e_1 -> e_2 -> e_3 -> e_1
    gens = [(2, 4, 0), (0, 2, 4), (4, 0, 2)]
    det = abs(sum(s * gens[0][p[0]] * gens[1][p[1]] * gens[2][p[2]] for p, s in
                  [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((0, 2, 1), -1), ((1, 0, 2), -1), ((2, 1, 0), -1)]))
    check("C Hermite basis spans the generators and has index |det|",
          all(in_lattice(g, B) for g in gens) and B[0][0] * B[1][1] * B[2][2] == det, f"det {det}")
    cyc_inv = all(in_lattice(cyc(b), B) for b in B)
    simple = all(len(set(a)) == 6 and t not in a for t, a in enumerate(Q.adj()))
    # the induced map on X_P is a graph automorphism, and pulls chi_{e_{j+1}} back to chi_{e_j}
    m = {t: Q.idx[reduce_(cyc(r), B)] for t, r in enumerate(Q.reps)}
    nbset = [set(a) for a in Q.adj()]
    is_aut = all(m[w] in nbset[m[v]] for v in range(Q.N) for w in Q.adj()[v])
    moves = all(tuple(char_vec(Q, E3[(j + 1) % 3])[m[t]] for t in range(Q.N)) == char_vec(Q, E3[j])
                for j in range(3))
    check(f"C {Q.name} (index {Q.N}): inside 2Z^3, invariant under the 3-cycle of axes, not O-invariant; the "
          f"3-cycle is a carrier automorphism relating the three triplet lines",
          cf_in_2Z3(B) and cyc_inv and not o_invariant(B) and simple and is_aut and moves, f"Hermite basis {B}")


def hermite(gens):
    """Lower-triangular Hermite basis (rows (a,0,0), (x,c,0), (y,z,f), 0 <= x,y < a, 0 <= z < c) of
    the full-rank lattice spanned by gens."""
    rows = [list(g) for g in gens]
    basis = [None, None, None]
    for k in (2, 1, 0):
        while True:
            nz = [r for r in rows if r[k] != 0]
            if len(nz) <= 1:
                break
            nz.sort(key=lambda r: abs(r[k]))
            p = nz[0]
            for r in nz[1:]:
                q = r[k] // p[k]
                for t in range(3):
                    r[t] -= q * p[t]
        piv = [r for r in rows if r[k] != 0][0]
        if piv[k] < 0:
            piv = [-x for x in piv]
        rows = [r for r in rows if r[k] == 0]
        basis[k] = piv
    a, (x, c, _), (y, z, f) = basis[0][0], basis[1], basis[2]
    q = z // c
    y, z = y - q * x, z - q * c
    x, y = x % a, y % a
    return [[a, 0, 0], [x, c, 0], [y, z, f]]


# ------------------------------------------------------------------ D
def part_D():
    print("== D. hypercube blocking n = 2y + eta ==")
    mism = []
    for Q in test_lattices():
        # r and r + b (b a period vector) are two lifts of one site of X_P; the blocking label
        # eta = n mod 2 is well defined iff they always agree
        direct = all(tuple(x % 2 for x in add(r, b)) == tuple(x % 2 for x in r) for r in Q.reps for b in Q.B)
        if direct != cf_in_2Z3(Q.B):
            mism.append(Q.name)
    check("D blocking eta(n) = n mod 2 is constant on P-classes iff P in 2Z^3 (all test quotients)", not mism,
          f"{mism}")


# ------------------------------------------------------------------ E
def in_lattice(v, B):
    return reduce_(v, B) == (0, 0, 0)


def same_lattice(B1, B2):
    return all(in_lattice(b, B2) for b in B1) and all(in_lattice(b, B1) for b in B2)


def part_E():
    print(f"== E. O-invariant sublattices of Z^3 of index <= {NMAX} (exhaustive Hermite enumeration) ==")
    found = []
    total = 0
    for a in range(1, NMAX + 1):
        for c in range(1, NMAX // a + 1):
            for f in range(1, NMAX // (a * c) + 1):
                for x in range(a):
                    for y in range(a):
                        for z in range(c):
                            total += 1
                            B = [[a, 0, 0], [x, c, 0], [y, z, f]]
                            if o_invariant(B):
                                found.append(B)
    fam = []
    for m in range(1, NMAX + 1):
        for name, B in [("Z^3", [[m, 0, 0], [0, m, 0], [0, 0, m]]),
                        ("D_3", [[2 * m, 0, 0], [m, m, 0], [m, 0, m]]),
                        ("B_3", [[2 * m, 0, 0], [0, 2 * m, 0], [m, m, m]])]:
            idx = B[0][0] * B[1][1] * B[2][2]
            if idx <= NMAX:
                fam.append((f"{m}{name}", B, idx))
    match = len(found) == len(fam) and all(any(same_lattice(B, F) for _, F, _ in fam) for B in found)
    names = sorted([n for n, _, i in fam], key=lambda s: [i for nn, _, i in fam if nn == s][0])
    check(f"E {total} sublattices enumerated; the {len(found)} O-invariant ones are exactly m Z^3, m D_3, m B_3",
          match, ", ".join(names))
    inside = [n for n, B, i in fam if cf_in_2Z3(B)]
    check("E O-invariant and inside 2Z^3 (index <= NMAX): exactly those with m even",
          all((int(n.split('Z')[0].split('D')[0].split('B')[0]) % 2 == 0) == (n in inside) for n, _, _ in fam),
          ", ".join(inside))
    for n, B, i in fam:
        if not o_invariant(B):
            check(f"E family member {n} is O-invariant", False)
    # O-invariance equals O_h-invariance (-1 maps every lattice to itself): trivially true; and the
    # reflection x -> (-x1, x2, x3) preserves every O-invariant lattice found
    refl_ok = all(in_lattice((-b[0], b[1], b[2]), B) for B in found for b in B)
    check("E every O-invariant lattice found is also invariant under a coordinate reflection (so O_h-invariant)",
          refl_ok)


# ------------------------------------------------------------------ F
def part_F():
    print("== F. Theorem 8b: corner characters as eigenfunctions of the normalized neighbour average ==")
    bad = []
    for Q in test_lattices() + [rect(6, 6, 6)]:
        for eta in CORNERS:
            if not corner_defined(Q, eta):
                continue
            sigma = sum((-1) ** x for x in eta)
            mu = Fraction(sigma, 3)
            for t, r in enumerate(Q.reps):
                chi = (-1) ** dot(eta, r)
                avg = Fraction(sum((-1) ** dot(eta, Q.reps[Q.nb(t, e, s)]) for e in E3 for s in (1, -1)), 6)
                if avg != mu * chi:
                    bad.append((Q.name, eta))
                    break
    check("F on every test quotient, each defined corner character satisfies avg chi = (sigma/3) chi; "
          "values 1, 1/3, -1/3, -1", not bad, f"{bad[:5]}")


def main():
    part_K()
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    part_F()
    if FAIL:
        print(f"FAILED: {len(FAIL)} check(s)")
        sys.exit(1)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
