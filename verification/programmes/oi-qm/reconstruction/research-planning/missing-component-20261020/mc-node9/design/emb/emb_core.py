"""Embedded-observer reconstruction engine (node 9 follow-up, exploratory design evidence).

Conventions are those of f2.py (copied unchanged from mc-node9/design/c1, sha256 855df88d...):
coordinate x is u_x, coordinate n+x is v_x; a linear map is a tuple of row bitmasks; the update
is Main.md l.290, u'_x = sum_{z~x} u_z + v_x, v'_x = u_x, over F2.

Heisenberg picture.  After t steps every cell is a linear functional (row of M^t) of the initial
state.  The initial state has
  * clean coordinates K (declared visible ancilla coordinates, value known; WLOG 0 by linearity),
  * unknown coordinates (every other coordinate) iid uniform (counting measure).
Conditioned on the observer's records (a set F of functionals, their values known), the toy's
current state (two functionals T) is uniform on a coset of size
      2^( rank(F_u + T_u) - rank(F_u) ),     X_u := X restricted to the unknown coordinates,
the same in every branch, and every branch has probability 2^(-rank F_u).  The prior support of
the toy's current state (no records at all) is 2^rank(T_u).  Everything is exact over F2; an
independent brute-force enumeration (forward simulation of states, no matrix powers, no
subspace algebra) checks this formula in check_core.py.
"""
from itertools import permutations, combinations
from f2 import lattice_update, compose, identity, rank, omega, apply, popc


def gated_update(n, edges):
    """External selection (E3): the displayed update restricted to an active edge set."""
    return lattice_update(n, edges)


def vis_coords(n, R):
    return [x for x in R] + [n + x for x in R]


def clean_coords(n, R, decl):
    if decl == "FULL":
        return vis_coords(n, R)
    if decl == "U":
        return list(R)
    if decl == "V":
        return [n + x for x in R]
    if decl == "NONE":
        return []
    raise ValueError(decl)


def mask_of(coords):
    m = 0
    for c in coords:
        m |= 1 << c
    return m


def post_rank(F, T, umask):
    """log2 of the toy's posterior support given records F (functionals), unknowns umask."""
    Fu = [f & umask for f in F]
    Tu = [g & umask for g in T]
    return rank(Fu + Tu) - rank(Fu)


def prior_rank(T, umask):
    return rank([g & umask for g in T])


def order(M, cap=100000):
    N = len(M)
    I = identity(N)
    P = M
    for k in range(1, cap + 1):
        if P == I:
            return k
        P = compose(M, P)
    return None


def iso_graphs(n):
    """One labelled representative per isomorphism class of simple graphs on n vertices."""
    pairs = list(combinations(range(n), 2))
    idx = {p: i for i, p in enumerate(pairs)}
    perms = list(permutations(range(n)))
    pmaps = []
    for p in perms:
        pm = []
        for (a, b) in pairs:
            x, y = p[a], p[b]
            pm.append(idx[(min(x, y), max(x, y))])
        pmaps.append(pm)
    seen = bytearray(1 << len(pairs))
    reps = []
    for g in range(1 << len(pairs)):
        if seen[g]:
            continue
        reps.append(tuple(pairs[i] for i in range(len(pairs)) if (g >> i) & 1))
        for pm in pmaps:
            h = 0
            for i in range(len(pairs)):
                if (g >> i) & 1:
                    h |= 1 << pm[i]
            seen[h] = 1
    return reps


def toy_rows(P, n, toy):
    return [P[toy], P[n + toy]]
