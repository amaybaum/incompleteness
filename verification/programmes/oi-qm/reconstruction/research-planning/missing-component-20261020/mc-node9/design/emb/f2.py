"""Exact F2 linear algebra for the C-i construction task (node 9, design stage).

Conventions (fixed once, used by every script in this directory):
  * n sites; coordinate index x is u_x, index n+x is v_x (x = 0..n-1).
  * A linear map T on F2^{2n} acts on column states s' = T s.  It is stored as a
    tuple of 2n row bitmasks: bit j of row i is the coefficient of input
    coordinate j in output coordinate i.
  * The lattice symplectic form is J = [[0, I], [I, 0]]: u_x is paired with v_x.
    T is symplectic iff T J T^T = J, i.e. iff omega(row_i, row_j) = J_ij for all i, j,
    where omega(a, b) = sum_x a_{u_x} b_{v_x} + a_{v_x} b_{u_x}  (mod 2).
  * Main.md l.290 update:  u'_x = sum_{z~x} u_z + v_x,  v'_x = u_x.
Everything is integer/bitmask arithmetic over F2; there is no floating point anywhere.
"""
from itertools import permutations, product


def popc(x):
    return bin(x).count("1")


def rowmul(f, A):
    """Functional f (bitmask over A's output coords) composed with A: returns f.A."""
    r = 0
    j = 0
    while f:
        if f & 1:
            r ^= A[j]
        f >>= 1
        j += 1
    return r


def compose(A, B):
    """Matrix product A B (apply B first, then A)."""
    return tuple(rowmul(a, B) for a in A)


def identity(N):
    return tuple(1 << i for i in range(N))


def rank(rows):
    rows = [r for r in rows]
    rk = 0
    basis = []
    for r in rows:
        for b in basis:
            r = min(r, r ^ b)
        if r:
            basis.append(r)
            rk += 1
    return rk


def is_invertible(T):
    return rank(T) == len(T)


def inverse(T):
    N = len(T)
    A = [T[i] | (1 << (N + i)) for i in range(N)]
    for c in range(N):
        piv = next((i for i in range(c, N) if (A[i] >> c) & 1), None)
        if piv is None:
            raise ValueError("singular")
        A[c], A[piv] = A[piv], A[c]
        for i in range(N):
            if i != c and (A[i] >> c) & 1:
                A[i] ^= A[c]
    mask = (1 << N) - 1
    return tuple((A[i] >> N) & mask for i in range(N))


def omega(a, b, n):
    m = (1 << n) - 1
    au, av = a & m, (a >> n) & m
    bu, bv = b & m, (b >> n) & m
    return (popc(au & bv) + popc(av & bu)) & 1


def J_entry(i, j, n):
    return 1 if (abs(i - j) == n) else 0


def is_symplectic(T, n):
    N = 2 * n
    for i in range(N):
        for j in range(N):
            if omega(T[i], T[j], n) != J_entry(i, j, n):
                return False
    return True


def lattice_update(n, edges):
    """Main.md l.290: u'_x = sum_{z~x} u_z + v_x ; v'_x = u_x."""
    adj = [0] * n
    for (a, b) in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    rows = [0] * (2 * n)
    for x in range(n):
        rows[x] = adj[x] | (1 << (n + x))   # u'_x
        rows[n + x] = 1 << x                # v'_x
    return tuple(rows)


def apply(T, s):
    """Apply T to a state bitmask s (bit j = coordinate j)."""
    out = 0
    for i, r in enumerate(T):
        if popc(r & s) & 1:
            out |= 1 << i
    return out


def visible_op(g_rows, vis):
    """Embed a linear map g on the visible coordinates `vis` (list of coordinate indices,
    g_rows[i] a bitmask over positions in vis) as a full matrix acting as identity on
    hidden coordinates."""
    N_total = None
    return g_rows, vis


def embed(g_rows, vis, N):
    rows = list(identity(N))
    for i, ci in enumerate(vis):
        r = 0
        for j, cj in enumerate(vis):
            if (g_rows[i] >> j) & 1:
                r |= 1 << cj
        rows[ci] = r
    return tuple(rows)


def gl_elements(d):
    """All invertible d x d matrices over F2, as tuples of row bitmasks."""
    out = []
    def rec(rows, span):
        if len(rows) == d:
            out.append(tuple(rows))
            return
        for r in range(1, 1 << d):
            if r in span:
                continue
            rec(rows + [r], span | {s ^ r for s in span})
    rec([], {0})
    return out


def perm_elements(d):
    return [tuple(1 << p[i] for i in range(d)) for p in permutations(range(d))]


def fmt_row(r, n, names=None):
    terms = []
    for j in range(2 * n):
        if (r >> j) & 1:
            terms.append(names[j] if names else (f"u{j}" if j < n else f"v{j-n}"))
    return " + ".join(terms) if terms else "0"


def fmt_matrix(T, n, names=None):
    lines = []
    for i, r in enumerate(T):
        lhs = names[i] if names else (f"u{i}" if i < n else f"v{i-n}")
        lines.append(f"  {lhs}' = {fmt_row(r, n, names)}")
    return "\n".join(lines)


def dense(T, N):
    return [[(T[i] >> j) & 1 for j in range(N)] for i in range(N)]
