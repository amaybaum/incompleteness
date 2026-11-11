#!/usr/bin/env python3
"""qc21_check.py -- the checker of native round ARP-2-QC21 (Q-C2-1).

Preregistration r15 (owner-approved R1–R10), sections *Test P*, *Test B*, *Obligation C*, *The controls*, *Decisive builders and the
guard*, *Control modes* and Appendix C (ARP-3-QC22 r13's exact method, guard machinery and execution design,
copied under D10(a) with D12's removals).

Entry points (C.5):
    --event <name> [--dispatch-sha <40 hex>]   the default computation; four keys select decisive mode
    --stress                                   canonical-JSON stress.json, schema arp2-qc21-stress v2
    --self-test                                every self-test and mutation; exit 0 iff all pass

Exit statuses: 0 complete decisive output (including scientific VOID) or fixture expectations met; 3 a
fixture expectation unmet (including fixture control/cap failures); 4 refusal (no --event, malformed --dispatch-sha).

Arithmetic is exact: integers, Fraction and F_2 only (C-EXACT). The one Fraction helper that uses "/" is q_div.
Stdlib only. Reads no file. `os` is referenced at exactly two sites, each `os.environ` passed whole to s_mode.
The solver's functions are s_*, the independent verifier's v_* (C-INDEP), self-tests t_*.
"""
from fractions import Fraction
import itertools
import json
import os
import sys

# ------------------------------------------------------------------------------------------------------------
# Frozen constants
# ------------------------------------------------------------------------------------------------------------
DISPATCH_EVENT = "workflow_dispatch"
ROUND_REF = "refs/heads/research/arp2-qc21-20261108"
SCHEMA = "arp2-qc21-measurements"
SCHEMA_VERSION = 1
STRESS_SCHEMA = "arp2-qc21-stress"
STRESS_VERSION = 2

# C.1 step 6: the deterministic budgets. PENDING until the design run (mechanical freeze rule); None = no budget.
P_MAX = None
B_MAX = None
W_MAX = None

# C.1 caps (frozen).
CAP_GENERATORS = 16
CAP_D = 16
CAP_FACET_SUBSETS = 100000
CAP_EFFECTS = 200

# C.1 stress-fixture seeds are fixed; stress measurements/caps/budgets remain unrun until a separately authorized design.
STRESS_SEEDS = (20261108, 1, 2)

BP_P_MAX = None
BP_B_MAX = None
BP_W_MAX = None
BP_CAP_GENERATORS = None
BP_CAP_D = None
BP_CAP_FACET_SUBSETS = None
BP_CAP_EFFECTS = 200
S_MAX = 100000  # Initial owner budget, #1169 c.6778994857; other measured budgets remain unset.
SOURCE_BASE = None  # Draft provenance. Bind to the authorized round D before the first local A3/design tree.
REFUSAL_CALLS = 0

HEX = "0123456789abcdef"


class QC21Refusal(Exception):
    """Raised by the refusal check outside a decisive run."""


class OutOfScope(Exception):
    """A fragment exceeded a budget or a cap."""


# ------------------------------------------------------------------------------------------------------------
# Exact helpers (shared, not v_*)
# ------------------------------------------------------------------------------------------------------------
def q_div(a, b):
    """The one Fraction helper that uses "/" (C-EXACT)."""
    return Fraction(a) / Fraction(b)


def fstr(x):
    """A Fraction or int as the canonical "p/q" (or "p") string."""
    x = Fraction(x)
    if x.denominator == 1:
        return str(x.numerator)
    return "%d/%d" % (x.numerator, x.denominator)


def jsonable(o):
    if isinstance(o, bool) or o is None or isinstance(o, str):
        return o
    if isinstance(o, int):
        return o
    if isinstance(o, Fraction):
        return fstr(o)
    if isinstance(o, dict):
        return {str(k): jsonable(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jsonable(v) for v in o]
    raise TypeError("not jsonable: %r" % (type(o),))


def canonical(o):
    """Canonical JSON text: sorted keys, (",", ":") separators, final newline."""
    return json.dumps(jsonable(o), sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n"


def parse_q(s):
    if isinstance(s, int):
        return Fraction(s)
    if "/" in s:
        n, d = s.split("/")
        return Fraction(int(n), int(d))
    return Fraction(int(s))


# Pure-Python SHA-256 (FIPS 180-4). The frozen import list (fractions, itertools, json, os, sys) has no hashlib.
_SHA_K = (
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2)
_SHA_H0 = (0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a, 0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19)


def h_sha256(data):
    m = 0xffffffff

    def rotr(x, n):
        return ((x >> n) | (x << (32 - n))) & m

    msg = bytearray(data)
    bitlen = (len(msg) * 8) & 0xffffffffffffffff
    msg.append(0x80)
    while len(msg) % 64 != 56:
        msg.append(0)
    msg += bitlen.to_bytes(8, "big")
    h = list(_SHA_H0)
    for off in range(0, len(msg), 64):
        w = [int.from_bytes(msg[off + 4 * i:off + 4 * i + 4], "big") for i in range(16)]
        for i in range(16, 64):
            s0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^ (w[i - 15] >> 3)
            s1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^ (w[i - 2] >> 10)
            w.append((w[i - 16] + s0 + w[i - 7] + s1) & m)
        a, b, c, d, e, f, g, hh = h
        for i in range(64):
            s1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
            ch = (e & f) ^ ((~e) & g)
            t1 = (hh + s1 + ch + _SHA_K[i] + w[i]) & m
            s0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
            mj = (a & b) ^ (a & c) ^ (b & c)
            t2 = (s0 + mj) & m
            hh, g, f, e, d, c, b, a = g, f, e, (d + t1) & m, c, b, a, (t1 + t2) & m
        h = [(x + y) & m for x, y in zip(h, (a, b, c, d, e, f, g, hh))]
    return "".join("%08x" % x for x in h)


def ordered_unique(values=()):
    """Order-preserving membership/iteration, without unordered set construction."""
    return {key: None for key in values}


def ordered_key(values=()):
    """Hashable unordered-coordinate key, represented by a canonical sorted tuple."""
    return tuple(sorted(dict.fromkeys(values)))


def bits_of(x):
    """Bit length of an integer entry (sign ignored)."""
    return abs(x).bit_length()


# ------------------------------------------------------------------------------------------------------------
# C.1 The exact method: the solver (s_*)
# ------------------------------------------------------------------------------------------------------------
def s_rank_basis(rows):
    """Indices of a maximal linearly independent subset of `rows`, first in order (exact)."""
    basis, red = [], []
    for i, r in enumerate(rows):
        v = [Fraction(x) for x in r]
        for piv, b in red:
            if v[piv] != 0:
                f = q_div(v[piv], b[piv])
                v = [a - f * c for a, c in zip(v, b)]
        nz = [k for k, a in enumerate(v) if a != 0]
        if nz:
            red.append((nz[0], v))
            basis.append(i)
    return basis


def s_rank(rows):
    return len(s_rank_basis(rows))


def s_rref(rows, ncols):
    """Reduced row echelon form over the first `ncols` columns; returns (rows, pivot columns)."""
    a = [[Fraction(x) for x in r] for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        p = next((i for i in range(r, len(a)) if a[i][c] != 0), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pv = a[r][c]
        a[r] = [q_div(x, pv) for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        piv.append(c)
        r += 1
    return a[:r], piv


def s_solve_square(m, rhs):
    """Exact Gauss-Jordan for a square invertible system."""
    n = len(m)
    rows = [[Fraction(x) for x in m[i]] + [Fraction(rhs[i])] for i in range(n)]
    red, piv = s_rref(rows, n)
    if len(piv) != n:
        raise ArithmeticError("singular system")
    return [red[i][n] for i in range(n)]


def s_nullvec(rows, d):
    """The kernel vector of `rows` (d columns) if the kernel is one-dimensional, else None."""
    red, piv = s_rref([list(r) + [0] for r in rows], d)
    free = [c for c in range(d) if c not in piv]
    if len(free) != 1:
        return None
    f = free[0]
    v = [Fraction(0)] * d
    v[f] = Fraction(1)
    for i, c in enumerate(piv):
        v[c] = -red[i][f]
    return v


def s_primitive(v):
    """A rational vector scaled to the primitive integer vector with the same direction."""
    den = 1
    for x in v:
        x = Fraction(x)
        den = den * x.denominator // _gcd(den, x.denominator)
    iv = [int(Fraction(x) * den) for x in v]
    g = 0
    for x in iv:
        g = _gcd(g, abs(x))
    if g == 0:
        return iv
    return [x // g for x in iv]


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def s_dot(u, v):
    return sum(Fraction(a) * Fraction(b) for a, b in zip(u, v))


def s_table(laws, reads):
    """N(p, e) = sum_omega mu_p(omega) xi_e(omega); the unit effect is effect 0."""
    out = []
    for mu in laws:
        row = [sum(Fraction(x) for x in mu)]
        for xi in reads:
            row.append(sum(Fraction(m) * Fraction(x) for m, x in zip(mu, xi)))
        out.append(row)
    return out


def s_factor(n_tab):
    """N = A B^T exactly, with A = N restricted to a column basis (rows a_p) and B solved (rows b_e)."""
    cols = [list(c) for c in zip(*n_tab)]
    cb = s_rank_basis(cols)
    d = len(cb)
    a = [[Fraction(n_tab[p][c]) for c in cb] for p in range(len(n_tab))]
    rb = s_rank_basis(a)
    sq = [a[r] for r in rb]
    b = []
    for e in range(len(n_tab[0])):
        b.append(s_solve_square(sq, [n_tab[r][e] for r in rb]))
    return a, b, d


def s_reduce_effects(b):
    """Step 1: drop every effect vector that duplicates, or is a positive multiple of, an earlier one. The unit
    effect (index 0) is kept; non-extreme effects are not pruned. Returns the kept indices."""
    kept, seen = [], []
    for e, v in enumerate(b):
        nz = next((x for x in v if x != 0), None)
        key = tuple(v) if nz is None else tuple(q_div(x, abs(nz)) for x in v)
        if e == 0 or key not in seen:
            kept.append(e)
            seen.append(key)
    return kept


def s_generators(a):
    """The preparation generators: the rows of A up to positive multiples (first occurrence kept)."""
    out, seen = [], []
    for v in a:
        nz = next((x for x in v if x != 0), None)
        key = tuple(v) if nz is None else tuple(q_div(x, abs(nz)) for x in v)
        if key not in seen:
            seen.append(key)
            out.append(list(v))
    return out


def s_facets(gens, d, visit_limit=None):
    """Facets of cone{gens}: brute force over (d-1)-subsets; primitive integer normals, sorted."""
    out = []
    visits = 0
    for sub in itertools.combinations(range(len(gens)), d - 1):
        visits += 1
        if visit_limit is not None and visits > visit_limit:
            raise OutOfScope("facet-subsets")
        n = s_nullvec([gens[i] for i in sub], d)
        if n is None:
            continue
        vals = [s_dot(n, g) for g in gens]
        if all(v >= 0 for v in vals):
            pass
        elif all(v <= 0 for v in vals):
            n = [-x for x in n]
        else:
            continue
        pn = s_primitive(n)
        if pn not in out:
            out.append(pn)
    return sorted(out)


def s_comb(n, k):
    if k < 0 or k > n:
        return 0
    r = 1
    for i in range(k):
        r = r * (n - i) // (i + 1)
    return r


class Budget:
    """C.1 step 6: pivot, bit and work budgets for one fragment, across steps 3 and 4 and all phases."""

    def __init__(self, p_max=None, b_max=None, w_max=None):
        self.p_max, self.b_max, self.w_max = p_max, b_max, w_max
        self.pivots = 0
        self.max_bits = 0
        self.work = 0

    def see(self, bits):
        if bits > self.max_bits:
            self.max_bits = bits

    def check(self):
        if self.p_max is not None and self.pivots > self.p_max:
            raise OutOfScope("pivots")
        if self.b_max is not None and self.max_bits > self.b_max:
            raise OutOfScope("bits")
        if self.w_max is not None and self.work > self.w_max:
            raise OutOfScope("work")

    def record(self):
        return {"pivots": self.pivots, "max_bits": self.max_bits, "work": self.work}


def s_phase1(a_eq, b_eq, budget):
    """Phase-1 simplex for {x >= 0 : A x = b}, fraction-free (Bareiss) integer tableau.
    Entering: Dantzig (most negative reduced cost, lowest index); after 50 consecutive degenerate pivots, Bland
    for the rest of the phase. Leaving: minimum ratio, ties to the lowest basic-variable index.
    Returns ("feasible", x) or ("infeasible", pi) with pi a dual vector on the original rows:
    pi^T A <= 0 componentwise and pi^T b > 0."""
    m = len(a_eq)
    n = len(a_eq[0]) if m else 0
    tab, sgn, scale = [], [], []
    for i in range(m):
        row = [Fraction(x) for x in a_eq[i]] + [Fraction(b_eq[i])]
        den = 1
        for x in row:
            den = den * x.denominator // _gcd(den, x.denominator)
        irow = [int(x * den) for x in row]
        s = 1
        if irow[-1] < 0:
            irow = [-x for x in irow]
            s = -1
        sgn.append(s)
        scale.append(den)
        tab.append(irow[:n] + [1 if j == i else 0 for j in range(m)] + [irow[n]])
    ncol = n + m
    obj = [-sum(tab[i][j] for i in range(m)) for j in range(n)] + [0] * m + [-sum(tab[i][ncol] for i in range(m))]
    tab.append(obj)
    for r in tab:
        for x in r:
            budget.see(bits_of(x))
    budget.check()
    basis = [n + i for i in range(m)]
    dd = 1
    stall = 0
    bland = False
    while True:
        z = tab[m]
        neg = [j for j in range(ncol) if z[j] < 0]
        if not neg:
            break
        if bland:
            ent = neg[0]
        else:
            ent = min(neg, key=lambda j: (z[j], j))
        cand = [i for i in range(m) if tab[i][ent] > 0]
        if not cand:
            raise ArithmeticError("unbounded phase 1")
        best = None
        for i in cand:
            if best is None:
                best = i
                continue
            lhs = tab[i][ncol] * tab[best][ent]
            rhs = tab[best][ncol] * tab[i][ent]
            if lhs < rhs or (lhs == rhs and basis[i] < basis[best]):
                best = i
        r = best
        degenerate = tab[r][ncol] == 0
        p = tab[r][ent]
        for i in range(m + 1):
            if i == r:
                continue
            f = tab[i][ent]
            ri = tab[i]
            rr = tab[r]
            new = [(p * ri[j] - f * rr[j]) // dd for j in range(ncol + 1)]
            tab[i] = new
            for x in new:
                bx = bits_of(x)
                budget.work += bx
                budget.see(bx)
        budget.pivots += 1
        budget.check()
        dd = p
        basis[r] = ent
        stall = stall + 1 if degenerate else 0
        if stall >= 50:
            bland = True
    objval = q_div(-tab[m][ncol], dd)
    if objval == 0:
        x = [Fraction(0)] * n
        for i in range(m):
            if basis[i] < n:
                x[basis[i]] = q_div(tab[i][ncol], dd)
        return "feasible", x
    pi = []
    for k in range(m):
        yk = 1 - q_div(tab[m][n + k], dd)
        pi.append(yk * sgn[k] * scale[k])
    return "infeasible", pi


def s_param_farkas(eqs, nvar, ineqs, budget):
    """Decide {x : E x = r, c_i . x >= 0} by solving the equalities exactly (x = x0 + N t) and deciding
    {t : a_i . t + c_i >= 0} through its Farkas alternative (phase-1 simplex with T + 1 equality rows and one
    nonnegative column per inequality). eqs: rows of nvar coefficients followed by the right-hand side.
    Returns ("feasible", x) or ("infeasible", (y, x0, nulls)) or ("inconsistent", None)."""
    red, piv = s_rref(eqs, nvar)
    for rrow in red:
        if all(x == 0 for x in rrow[:nvar]) and rrow[nvar] != 0:
            return "inconsistent", None
    free = [v for v in range(nvar) if v not in piv]
    x0 = [Fraction(0)] * nvar
    for i, p in enumerate(piv):
        x0[p] = red[i][nvar]
    nulls = []
    for f in free:
        v = [Fraction(0)] * nvar
        v[f] = Fraction(1)
        for i, p in enumerate(piv):
            v[p] = -red[i][f]
        nulls.append(v)
    t_dim = len(free)
    rows = []
    for c in ineqs:
        nzc = [(k, ck) for k, ck in enumerate(c) if ck != 0]
        cst = sum(ck * x0[k] for k, ck in nzc)
        coef = [sum(ck * nulls[f][k] for k, ck in nzc) for f in range(t_dim)]
        rows.append((coef, cst))
    nyv = len(rows)
    a_eq = [[rows[i][0][f] for i in range(nyv)] for f in range(t_dim)] + [[rows[i][1] for i in range(nyv)]]
    b_eq = [Fraction(0)] * t_dim + [Fraction(-1)]
    st, sol = s_phase1(a_eq, b_eq, budget)
    if st == "feasible":
        return "infeasible", (sol, t_dim)
    pi = sol
    s = -pi[t_dim]
    if s <= 0:
        raise ArithmeticError("phase-1 dual without a positive scale")
    t = [q_div(-pi[f], s) for f in range(t_dim)]
    x = [x0[i] + sum(t[f] * nulls[f][i] for f in range(t_dim)) for i in range(nvar)]
    return "feasible", (x, t_dim)


def s_step3(laws, b_kept, a, b, d, unit_idx, budget):
    """Step 3, applicable only when r_S = d: a linear K: Q^d -> Q^{Omega_c} with K b_e >= 0, K b_u = 1 and
    mu_p^T K b_e = N(p, e), decided by the same phase-1 simplex as step 4 (reduced form). Returns K or None.
    Since N(p, e) is linear in mu_p and in b_e, the equalities on a basis of preparations and of effects
    imply them on all."""
    om = len(laws[0])
    ip = s_rank_basis(laws)
    ie = [b_kept[k] for k in s_rank_basis([b[e] for e in b_kept])]
    nvar = om * d

    def kidx(w, c):
        return w * d + c

    eqs = []
    for p in ip:
        for e in ie:
            row = [Fraction(0)] * nvar
            for w in range(om):
                if laws[p][w] == 0:
                    continue
                for c in range(d):
                    row[kidx(w, c)] += Fraction(laws[p][w]) * b[e][c]
            eqs.append(row + [s_dot(a[p], b[e])])
    for w in range(om):
        row = [Fraction(0)] * nvar
        for c in range(d):
            row[kidx(w, c)] = Fraction(b[unit_idx][c])
        eqs.append(row + [Fraction(1)])
    ineqs = []
    for e in b_kept:
        for w in range(om):
            row = [Fraction(0)] * nvar
            for c in range(d):
                row[kidx(w, c)] = Fraction(b[e][c])
            ineqs.append(row)
    st, data = s_param_farkas(eqs, nvar, ineqs, budget)
    if st != "feasible":
        return None
    x = data[0]
    return [[x[kidx(w, c)] for c in range(d)] for w in range(om)]


def s_step4(a, b, d, b_kept, unit_idx, budget, facets=None):
    """Step 4: the reduced state-facet LP with orientation fixed. Returns (verdict, data)."""
    gens = s_generators(a)
    g = s_facets(gens, d) if facets is None else facets
    m = len(g)
    br = [b[e] for e in b_kept]
    ne = len(br)
    nv = m * d

    def idx(j, c):
        return j * d + c

    eqs = []
    for r in range(d):
        for c in range(d):
            row = [Fraction(0)] * nv
            for j in range(m):
                row[idx(j, c)] = Fraction(g[j][r])
            eqs.append(row + [Fraction(1 if r == c else 0)])
    ineqs = []
    for j in range(m):
        for e in range(ne):
            row = [Fraction(0)] * nv
            for c in range(d):
                row[idx(j, c)] = Fraction(br[e][c])
            ineqs.append(row)
    st, data = s_param_farkas(eqs, nv, ineqs, budget)
    if st == "inconsistent":
        raise ArithmeticError("inconsistent regrouping")
    t_dim = data[1]
    info = {"m": m, "E": ne, "T": t_dim}
    if st == "infeasible":
        y = data[0]
        cols = s_rank_basis(g)
        sq = [[Fraction(x) for x in g[j]] for j in cols]
        w_mat = []
        for r in range(d):
            yb = [sum(y[j * ne + e] * br[e][r] for e in range(ne)) for j in cols]
            w_mat.append(s_solve_square(sq, yb))
        yy = [[y[j * ne + e] for e in range(ne)] for j in range(m)]
        return "infeasible", {"facets": g, "W": w_mat, "y": yy, "info": info}
    kap = data[0]
    kmat = [[kap[idx(j, c)] for c in range(d)] for j in range(m)]
    bu = b[unit_idx]
    keep = [j for j in range(m) if s_dot(kmat[j], bu) != 0]
    mu = [[s_dot(g[j], ap) * s_dot(kmat[j], bu) for j in keep] for ap in a]
    xi = [[q_div(s_dot(kmat[j], be), s_dot(kmat[j], bu)) for j in keep] for be in b]
    return "feasible", {"facets": g, "kappa": kmat, "mu": mu, "xi": xi, "info": info}


def s_cert_bytes(cert):
    return canonical(cert).encode("utf-8")


def s_decide(frag, budget_vals=(None, None, None), force_step4=False, mutate=None, cap_vals=None, budget=None):
    """C.1 decision with certified reduction and the caller's role-specific caps/budget."""
    laws = [[Fraction(x) for x in mu] for mu in frag["laws"]]
    reads = [[Fraction(x) for x in xi] for xi in frag["reads"]]
    unit = [Fraction(1)]*len(laws[0])
    all_reads = [unit]+reads
    rec = {"name": frag["name"], "preps": len(laws), "reads": len(reads),
           "lp_settings": list(frag.get("lp_settings", [])),
           "budget_values": [budget.p_max, budget.b_max, budget.w_max] if budget is not None else list(budget_vals)}
    if budget is None:
        budget = Budget(*budget_vals)
    caps = (CAP_GENERATORS, CAP_D, CAP_FACET_SUBSETS, CAP_EFFECTS) if cap_vals is None else cap_vals
    n_tab = s_table(laws, reads)
    a, b, d = s_factor(n_tab)
    r_s, r_e = s_rank(laws), s_rank(all_reads)
    effects = sum(1 for e in range(len(b)) if any(n_tab[p][e] > 0 for p in range(len(a))))
    effect_kept = s_reduce_effects(b)
    rec.update({"d": d, "r_S": r_s, "r_E": r_e, "effects_reduced": len(effect_kept),
                "effects_before_reduction": effects, "tomo": d == r_s == r_e,
                "n_distinct": len(s_generators(a)), "n_extreme": None, "generators": None,
                "cap_values": list(caps)})

    def out_of_scope(reasons):
        rec.update({"lp": "out_of_scope", "decided_by": None, "caps": reasons, "cert": None,
                    "cert_sha256": None, "verified": False})
        rec.update(budget.record())
        return rec

    over = []
    if caps[1] is not None and d > caps[1]:
        over.append("d")
    if caps[3] is not None and effects > caps[3]:
        over.append("effects")
    if over:
        return out_of_scope(over)
    try:
        prep_kept, removals = s_reduce_extreme(a, budget)
        rec["reduction_verified"] = v_reduction(a, prep_kept, json.loads(canonical(removals)))
        if rec["reduction_verified"] is not True:
            failure = out_of_scope(["unverified-reduction"])
            failure["lp"] = "undecided"
            failure["caps"] = []
            failure["verification_reason"] = "unverified-reduction"
            return failure
        n, c = len(prep_kept), s_comb(len(prep_kept), d-1)
        rec.update({"n_extreme": n, "generators": n, "c": c})
        if caps[0] is not None and n > caps[0]:
            over.append("generators")
        if caps[2] is not None and c > caps[2]:
            over.append("facet-subsets")
        if over:
            return out_of_scope(over)
        cert = {"A": a, "B": b, "d": d, "effects_kept": effect_kept,
                "prep_kept": prep_kept, "prep_removals": removals, "facet_limit": caps[2]}
        verdict, step = None, None
        if not force_step4 and d == r_s == r_e:
            verdict, step = "feasible", 2
            cert.update({"step": 2, "verdict": verdict, "mu": laws, "xi": all_reads})
        if verdict is None and not force_step4 and r_s == d:
            kmat = s_step3(laws, effect_kept, a, b, d, 0, budget)
            if kmat is not None:
                verdict, step = "feasible", 3
                xi = [[s_dot(kmat[w], be) for w in range(len(laws[0]))] for be in b]
                cert.update({"step": 3, "verdict": verdict, "K": kmat, "mu": laws, "xi": xi})
        if verdict is None:
            facets = s_facets([a[p] for p in prep_kept], d, caps[2])
            verdict, data = s_step4(a, b, d, effect_kept, 0, budget, facets=facets)
            step = 4
            cert.update({"step": 4, "verdict": verdict, "facets": data["facets"], "T": data["info"]["T"],
                         "m": data["info"]["m"]})
            if verdict == "infeasible":
                cert.update({"W": data["W"], "y": data["y"]})
            else:
                cert.update({"kappa": data["kappa"], "mu": data["mu"], "xi": data["xi"]})
    except OutOfScope as error:
        return out_of_scope(["budget:"+str(error)])
    if mutate is not None:
        cert = mutate(cert)
    cb = s_cert_bytes(cert) if cert is not None else b"null"
    rec.update({"lp": verdict, "decided_by": step, "cert": cb, "cert_sha256": h_sha256(cb),
                "T": cert.get("T") if isinstance(cert, dict) else None})
    rec.update(budget.record())
    # The verifier's visit limit is certificate data; the driver binds it to the actual role cap.
    rec["verified"] = (isinstance(cert, dict) and cert.get("facet_limit") == caps[2]
                       and v_verify(cb, frag["laws"], frag["reads"]) == "verified")
    if not rec["verified"]:
        rec["lp_reported"], rec["lp"] = verdict, "undecided"
    return rec


def s_decide_effect_facet(frag, budget):
    """C-SYM with the original fragment's budget and an independently verified exchanged certificate."""
    laws = [[Fraction(x) for x in mu] for mu in frag["laws"]]
    reads = [[Fraction(x) for x in xi] for xi in frag["reads"]]
    n_tab = s_table(laws, reads)
    a, b, d = s_factor(n_tab)
    h = s_facets(s_generators(b), d)
    verdict, data = s_step4(b, a, d, list(range(len(a))), 0, budget, facets=h)
    cert = {"A": a, "B": b, "d": d, "facets": h, "verdict": verdict,
            "facet_limit": None}
    if verdict == "infeasible":
        cert.update({"W": data["W"], "y": data["y"]})
    else:
        kappa = data["kappa"]
        scales = [s_dot(normal, b[0]) for normal in h]
        kept = [i for i, value in enumerate(scales) if value != 0]
        mu = [[s_dot(kappa[i], row)*scales[i] for i in kept] for row in a]
        xi = [[q_div(s_dot(h[i], effect), scales[i]) for i in kept] for effect in b]
        cert.update({"mu": mu, "xi": xi, "kappa": kappa})
    raw = s_cert_bytes(cert)
    verified = v_verify_effect(raw, frag["laws"], frag["reads"]) == "verified"
    return {"lp": verdict if verified else "undecided", "verified": verified,
            "cert": raw, "cert_sha256": h_sha256(raw), "decided_by": 4 if verified else None,
            "T": data["info"]["T"], **budget.record()}


# ------------------------------------------------------------------------------------------------------------
# C.1 The independent verifier (v_*). C-INDEP: inside every v_* function, calls target only v_* functions,
# Fraction, json.loads, itertools.combinations and the whitelisted builtins; it shares no code with the solver.
# ------------------------------------------------------------------------------------------------------------
def s_reduce_extreme(a, budget):
    """Frozen row-order conic reduction with explicit nonnegative removal witnesses."""
    kept, removals = list(range(len(a))), []
    for p in range(len(a)):
        if p not in kept:
            continue
        others = [q for q in kept if q != p]
        if not others:
            continue
        equations = [[a[q][j] for q in others] for j in range(len(a[p]))]
        status, weights = s_phase1(equations, a[p], budget)
        if status == "feasible":
            sources = [q for q, weight in zip(others, weights) if weight != 0]
            values = [weight for weight in weights if weight != 0]
            removals.append({"row": p, "sources": sources, "weights": values})
            kept.remove(p)
    return kept, removals


def v_reduction(a, retained, removals):
    """Independent ordered witness validation; never calls the solver or a shared helper."""
    try:
        if not isinstance(retained, list) or not isinstance(removals, list):
            return False
        if any([not isinstance(index, int) or index is True or index is False for index in retained]):
            return False
        remaining = list(range(len(a)))
        previous = -1
        for item in removals:
            if not isinstance(item, dict):
                return False
            p, sources, values = item.get("row"), item.get("sources"), item.get("weights")
            if not isinstance(p, int) or p is True or p is False or p not in remaining:
                return False
            if p <= previous:
                return False
            previous = p
            if not isinstance(sources, list) or not isinstance(values, list) or len(sources) != len(values):
                return False
            if not sources or len(v_unique(sources)) != len(sources):
                return False
            if any([not isinstance(q, int) or q is True or q is False or q == p or q not in remaining for q in sources]):
                return False
            weights = [v_q(x) for x in values]
            if any([x < 0 for x in weights]):
                return False
            for j in range(len(a[p])):
                if sum([weight*a[q][j] for q, weight in zip(sources, weights)]) != a[p][j]:
                    return False
            remaining.remove(p)
        return retained == remaining

    except (ValueError, TypeError, KeyError, IndexError, ArithmeticError):
        return False


def v_verify_effect(raw, laws, reads):
    """Independent C-SYM: reconstruct the pairing, exchanged facets and explicit model/witness."""
    try:
        if not v_plain(laws) or not v_plain(reads):
            return "input-types"
        cert = json.loads(raw)
        n_tab = v_table(laws, reads)
        a, b, d = v_mat(cert["A"]), v_mat(cert["B"]), cert["d"]
        if len(a) != len(n_tab) or len(b) != len(n_tab[0]):
            return "factor-shape"
        if any([len(row) != d for row in a+b]) or not (v_rank(a) == v_rank(b) == v_rank(n_tab) == d):
            return "factor-rank"
        for p in range(len(a)):
            for e in range(len(b)):
                if v_dot(a[p], b[e]) != n_tab[p][e]:
                    return "factor-product"
        own = v_facets(b, d, cert["facet_limit"])
        theirs = sorted([[int(x) for x in row] for row in cert["facets"]])
        if own != theirs:
            return "effect-facet-list"
        if cert["verdict"] == "feasible":
            return v_check_model(v_mat(cert["mu"]), v_mat(cert["xi"]), n_tab, a, b)
        if cert["verdict"] != "infeasible":
            return "verdict"
        w, y = v_mat(cert["W"]), v_mat(cert["y"])
        if len(w) != d or any([len(row) != d for row in w]) or sum([w[i][i] for i in range(d)]) >= 0:
            return "W-shape-or-trace"
        if len(y) != len(own):
            return "y-shape"
        for j in range(len(own)):
            if len(y[j]) != len(a) or any([x < 0 for x in y[j]]):
                return "y-sign"
            if [v_dot(w[r], own[j]) for r in range(d)] != [sum([y[j][p]*a[p][r] for p in range(len(a))]) for r in range(d)]:
                return "W-effect-identity"
        return "verified"
    except (ValueError, TypeError, KeyError, IndexError, ArithmeticError):
        return "malformed-effect-certificate"


def v_unique(values):
    """Independent verifier membership map; no solver helper or unordered set."""
    return {key: None for key in values}


def v_plain(x):
    """Runtime types: plain dict, list, tuple, Fraction and int only, recursively."""
    if isinstance(x, Fraction) or isinstance(x, int):
        return True
    if isinstance(x, dict):
        return all(v_plain(k) or isinstance(k, int) for k in x) and all(v_plain(v) for v in x.values())
    if isinstance(x, list) or isinstance(x, tuple):
        return all(v_plain(v) for v in x)
    return False


def v_q(s):
    if s is True or s is False:
        return Fraction(1, 0)  # Boolean is not a rational encoded as a number.
    if isinstance(s, int) or isinstance(s, Fraction):
        return Fraction(s)
    if not isinstance(s, str):
        return Fraction(1, 0)  # A handled malformed-rational error.
    parts = s.split("/")
    if len(parts) == 1:
        return Fraction(int(parts[0]))
    return Fraction(int(parts[0]), int(parts[1]))


def v_vec(r):
    return [v_q(x) for x in r]


def v_mat(m):
    return [v_vec(r) for r in m]


def v_gcd(a, b):
    a = abs(a)
    b = abs(b)
    while b:
        a, b = b, a % b
    return a


def v_eliminate(rows, ncols):
    """Own Gauss-Jordan: (reduced rows, pivot columns)."""
    a = [[Fraction(x) for x in r] for r in rows]
    piv = []
    r = 0
    for c in range(ncols):
        p = -1
        for i in range(r, len(a)):
            if a[i][c] != 0:
                p = i
                break
        if p < 0:
            continue
        tmp = a[r]
        a[r] = a[p]
        a[p] = tmp
        pv = a[r][c]
        a[r] = [Fraction(x, pv) for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c] != 0:
                f = a[i][c]
                a[i] = [x - f * y for x, y in zip(a[i], a[r])]
        piv.append(c)
        r = r + 1
    return a[:r], piv


def v_rank(rows):
    if len(rows) == 0:
        return 0
    red, piv = v_eliminate(rows, len(rows[0]))
    return len(piv)


def v_dot(u, v):
    return sum([Fraction(a) * Fraction(b) for a, b in zip(u, v)])


def v_table(laws, reads):
    """N(p, e) = sum_omega mu_p(omega) xi_e(omega), re-derived from the definition; unit effect first."""
    out = []
    for mu in laws:
        row = [sum([Fraction(x) for x in mu])]
        for xi in reads:
            row.append(sum([Fraction(m) * Fraction(x) for m, x in zip(mu, xi)]))
        out.append(row)
    return out


def v_solve_linear_map(src, dst):
    """A matrix L with L s = t for every pair (s, t) of rows of src, dst, or None."""
    if len(src) == 0:
        return None
    d = len(src[0])
    red, piv = v_eliminate(src, d)
    if len(piv) != d:
        return None
    basis = []
    for i in range(len(src)):
        if v_rank([src[k] for k in basis] + [src[i]]) > len(basis):
            basis.append(i)
        if len(basis) == d:
            break
    out_dim = len(dst[0])
    lmat = []
    for o in range(out_dim):
        aug = [list(src[k]) + [dst[k][o]] for k in basis]
        red2, piv2 = v_eliminate(aug, d)
        if len(piv2) != d:
            return None
        lmat.append([red2[i][d] for i in range(d)])
    for s, t in zip(src, dst):
        for o in range(out_dim):
            if v_dot(lmat[o], s) != Fraction(t[o]):
                return None
    return lmat


def v_nullvec(rows, d):
    red, piv = v_eliminate([list(r) for r in rows], d)
    free = [c for c in range(d) if c not in piv]
    if len(free) != 1:
        return None
    f = free[0]
    v = [Fraction(0) for _ in range(d)]
    v[f] = Fraction(1)
    for i, c in enumerate(piv):
        v[c] = -red[i][f]
    return v


def v_primitive(v):
    den = 1
    for x in v:
        den = den * Fraction(x).denominator // v_gcd(den, Fraction(x).denominator)
    iv = [int(Fraction(x) * den) for x in v]
    g = 0
    for x in iv:
        g = v_gcd(g, x)
    if g == 0:
        return iv
    return [x // g for x in iv]


def v_facets(a, d, visit_limit=None):
    """Own facet list of cone{a_p}: every (d-1)-subset of distinct generators, supporting, with d-1 independent
    tight generators; primitive integer normals, sorted."""
    gens = []
    for r in a:
        nz = [x for x in r if x != 0]
        key = r if len(nz) == 0 else [Fraction(x, abs(nz[0])) for x in r]
        if key not in gens:
            gens.append(key)
    out = []
    if visit_limit is not None and (not isinstance(visit_limit, int) or visit_limit < 1):
        return None
    visits = 0
    for sub in itertools.combinations(range(len(gens)), d - 1):
        visits += 1
        if visit_limit is not None and visits > visit_limit:
            return None
        n = v_nullvec([gens[i] for i in sub], d)
        if n is None:
            continue
        vals = [v_dot(n, g) for g in gens]
        if all([x >= 0 for x in vals]):
            pass
        elif all([x <= 0 for x in vals]):
            n = [-x for x in n]
        else:
            continue
        tight = [g for g in gens if v_dot(n, g) == 0]
        if v_rank(tight) != d - 1:
            continue
        pn = v_primitive(n)
        if pn not in out:
            out.append(pn)
    return sorted(out)


def v_check_model(mu, xi, n_tab, a, b):
    """A feasible certificate, checked by definition."""
    if len(mu) != len(n_tab) or len(xi) != len(n_tab[0]):
        return "model-shape"
    width = len(mu[0]) if mu else 0
    if width == 0 or any([len(row) != width for row in mu+xi]):
        return "model-width"
    for row in mu:
        if any([x < 0 for x in row]):
            return "model-negative"
        if sum(row) != 1:
            return "model-normalization"
    for row in xi:
        if any([x < 0 or x > 1 for x in row]):
            return "model-response-range"
    for p in range(len(mu)):
        for e in range(len(xi)):
            if sum([m * x for m, x in zip(mu[p], xi[e])]) != n_tab[p][e]:
                return "model-reproduction"
    if v_solve_linear_map(a, mu) is None:
        return "model-not-linear-in-a"
    if v_solve_linear_map(b, xi) is None:
        return "model-not-linear-in-b"
    return "verified"


def v_verify(cert_bytes, laws, reads):
    """C-CERT: the independent verifier. Inputs: the solver's certificate as bytes, the charged laws and the read
    response tables as produced by the fragment builder. Returns "verified" or a reason."""
    try:
        if not v_plain(laws) or not v_plain(reads):
            return "input-types"
        cert = json.loads(cert_bytes)
        if not isinstance(cert, dict):
            return "no-certificate"
        if "A" not in cert or "B" not in cert or "d" not in cert or "step" not in cert or "verdict" not in cert:
            return "certificate-fields"
        n_tab = v_table(laws, reads)
        a = v_mat(cert["A"])
        b = v_mat(cert["B"])
        d = cert["d"]
        if not isinstance(d, int) or d is True or d is False or d < 1:
            return "factor-dimension"
        if any([len(row) != d for row in a+b]):
            return "factor-width"
        if len(a) != len(n_tab) or len(b) != len(n_tab[0]):
            return "factor-shape"
        for p in range(len(a)):
            for e in range(len(b)):
                if v_dot(a[p], b[e]) != n_tab[p][e]:
                    return "factor-product"
        if not (v_rank(a) == d and v_rank(b) == d and v_rank(n_tab) == d):
            return "factor-rank"
        if not v_reduction(a, cert["prep_kept"], cert["prep_removals"]):
            return "prep-reduction"
        step = cert["step"]
        if step not in (2, 3, 4):
            return "step"
        verdict = cert["verdict"]
        if step == 4:
            own = v_facets([a[p] for p in cert["prep_kept"]], d, cert["facet_limit"])
            theirs = sorted([[int(x) for x in g] for g in cert["facets"]])
            if own != theirs:
                return "facet-list"
        if verdict == "infeasible":
            if step != 4 or "W" not in cert or "y" not in cert:
                return "infeasible-fields"
            w = v_mat(cert["W"])
            y = v_mat(cert["y"])
            kept = cert["effects_kept"]
            if len(v_unique(kept)) != len(kept) or any([k < 0 or k >= len(b) for k in kept]):
                return "effects-kept"
            g = sorted([[int(x) for x in gg] for gg in cert["facets"]])
            if len(y) != len(g):
                return "y-shape"
            if len(w) != d or any([len(row) != d for row in w]):
                return "W-shape"
            if sum([w[i][i] for i in range(d)]) >= 0:
                return "trace-nonnegative"
            for j in range(len(g)):
                if len(y[j]) != len(kept) or any([x < 0 for x in y[j]]):
                    return "y-sign"
                lhs = [v_dot(w[r], g[j]) for r in range(d)]
                rhs = [sum([y[j][k] * b[kept[k]][r] for k in range(len(kept))]) for r in range(d)]
                if lhs != rhs:
                    return "W-identity"
            return "verified"
        if verdict == "feasible":
            if "mu" not in cert or "xi" not in cert:
                return "feasible-fields"
            return v_check_model(v_mat(cert["mu"]), v_mat(cert["xi"]), n_tab, a, b)
        return "verdict"
    except (ValueError, TypeError, KeyError, IndexError, ArithmeticError):
        return "malformed-certificate"


# ------------------------------------------------------------------------------------------------------------
# Fragments: charged configurations Omega_c, charged laws, read response tables (the fragment builder)
# ------------------------------------------------------------------------------------------------------------
def frag_from_laws(name, laws, read_slots, settings, acc=None):
    """laws: list of dicts {configuration tuple: probability}; read_slots: the slots Acc's effects read;
    settings: list of (setting name, fn) with fn(projected tuple) -> outcome.
    Omega_c: the joint values of the read slots with positive probability under some preparation (TOMO's
    configuration space). One effect per (setting, outcome) occurring on Omega_c; the unit effect is added by
    the solver. Returns the fragment."""
    proj = []
    for mu in laws:
        pm = {}
        for cfg, pr in mu.items():
            if pr == 0:
                continue
            key = tuple(cfg[i] for i in read_slots)
            pm[key] = pm.get(key, Fraction(0)) + Fraction(pr)
        proj.append(pm)
    omega = sorted(ordered_unique([k for pm in proj for k in pm]))
    lvec = [[pm.get(w, Fraction(0)) for w in omega] for pm in proj]
    reads, labels = [], []
    for sname, fn in settings:
        outs = sorted(ordered_unique([fn(w) for w in omega]))
        for o in outs:
            reads.append([1 if fn(w) == o else 0 for w in omega])
            labels.append([sname, list(o) if isinstance(o, tuple) else o])
    names = [s for s, _ in settings]
    return {"name": name, "laws": lvec, "reads": reads, "omega": [list(w) for w in omega],
            "effect_labels": labels, "lp_settings": names, "acc": list(names if acc is None else acc)}


def frag_outcome_table(frag):
    """The per-(setting, outcome) probability table, preparations x effects, unit excluded."""
    return [[sum(Fraction(m) * x for m, x in zip(mu, xi)) for xi in frag["reads"]] for mu in frag["laws"]]


def bitlaw(nbits, known, unknown_pairs=()):
    """Uniform law over F_2^nbits with `known` {slot: value} fixed; `unknown_pairs` (i, j, c) forces
    bit_j = bit_i + c."""
    out = {}
    tot = 0
    for cfg in itertools.product((0, 1), repeat=nbits):
        if any(cfg[k] != v for k, v in known.items()):
            continue
        if any(cfg[j] != (cfg[i] + c) % 2 for i, j, c in unknown_pairs):
            continue
        out[cfg] = 1
        tot += 1
    return {k: Fraction(1, tot) for k in out}


def productlaw(probs0):
    """Independent bits with P(bit_k = 0) = probs0[k]."""
    out = {}
    for cfg in itertools.product((0, 1), repeat=len(probs0)):
        w = Fraction(1)
        for b, p in zip(cfg, probs0):
            w *= p if b == 0 else 1 - p
        if w:
            out[cfg] = w
    return out


def pointlaw(cfg):
    return {tuple(cfg): Fraction(1)}


def _bit(i):
    return lambda w: w[i]


def _bits(*idx):
    return lambda w: tuple(w[i] for i in idx)


def _parity(*idx):
    return lambda w: sum(w[i] for i in idx) % 2


def _bloch_law(rz, rx):
    return productlaw([q_div(1 + Fraction(rz), 2), q_div(1 + Fraction(rx), 2)])


RECT = ((Fraction(3, 5), Fraction(4, 5)), (Fraction(-3, 5), Fraction(-4, 5)),
        (Fraction(3, 5), Fraction(-4, 5)), (Fraction(-3, 5), Fraction(4, 5)))


def fx_b_pos():
    """B-POS: rebit +-(3/5, 4/5), +-(3/5, -4/5) as (r_z, r_x), reads Z, X; laws on F_2^2 (product)."""
    return frag_from_laws("B-POS", [_bloch_law(rz, rx) for rz, rx in RECT], (0, 1), [("Z", _bit(0)), ("X", _bit(1))])


def fx_b_stab():
    """B-STAB: Z+-, X+- with Z, X."""
    laws = [bitlaw(2, {0: 0}), bitlaw(2, {0: 1}), bitlaw(2, {1: 0}), bitlaw(2, {1: 1})]
    return frag_from_laws("B-STAB", laws, (0, 1), [("Z", _bit(0)), ("X", _bit(1))])


def fx_b_class():
    """B-CLASS: a classical two-bit register (point laws) with spanning reads (bit 1, bit 2, both jointly)."""
    laws = [pointlaw(c) for c in itertools.product((0, 1), repeat=2)]
    return frag_from_laws("B-CLASS", laws, (0, 1), [("bit1", _bit(0)), ("bit2", _bit(1)), ("joint", _bits(0, 1))])


def fx_b_reg(with_parity=False, acc_parity=False):
    """B-REG: a classical register read through bit 1 and bit 2 only; the completion adds parity. With
    acc_parity, Acc = {bit 1, bit 2, parity} while the LP reads only bits 1 and 2."""
    laws = [pointlaw(c) for c in itertools.product((0, 1), repeat=2)]
    st = [("bit1", _bit(0)), ("bit2", _bit(1))]
    if with_parity:
        st.append(("parity", _parity(0, 1)))
    acc = ["bit1", "bit2", "parity"] if acc_parity else None
    return frag_from_laws("B-REG" + ("+parity" if with_parity else ""), laws, (0, 1), st, acc=acc)


def cw_stokes_table(stokes):
    """CW-P's single-detector, intensity-normalized table: polarization Stokes (s1, s2) analysed in the H/V (Z)
    and D/A (X) bases; transmitted fraction (1 + s)/2. Returned as product laws over the two analyser outcomes."""
    return [productlaw([q_div(1 + s1, 2), q_div(1 + s2, 2)]) for s1, s2 in stokes]


def fx_b_wave():
    """B-WAVE: CW-P's intensity-normalized table at B-POS's settings."""
    return frag_from_laws("B-WAVE", cw_stokes_table(RECT), (0, 1), [("Z", _bit(0)), ("X", _bit(1))])


def cw_alpha_two_detector():
    """Two square-law detectors behind a 50/50 splitter of a constant-intensity classical field:
    alpha = <I1 I2> / (<I1><I2>), exact."""
    i_tot = Fraction(1)
    i1 = i2 = q_div(i_tot, 2)
    return q_div(i1 * i2, i1 * i2)


def fx_zpt():
    """ZPT: Z+- with point reads: r_S = d = 2 < r_E = 4."""
    return frag_from_laws("ZPT", [bitlaw(2, {0: 0}), bitlaw(2, {0: 1})], (0, 1), [("point", _bits(0, 1))])


def fx_f10():
    """F10: four point laws, Z read only: d = 2 < r_S = 4."""
    laws = [pointlaw(c) for c in itertools.product((0, 1), repeat=2)]
    return frag_from_laws("F10", laws, (0, 1), [("Z", _bit(0))])


# ------------------------------------------------------------------------------------------------------------
# Stress fixtures (C.1; adaptation table: B-P's size and B-C's maximal size). Frozen generator, 32-bit xorshift.
# ------------------------------------------------------------------------------------------------------------
def seeded_coset(g, nbits, dimensions):
    """One xorshift stream; exact GF(2) independence and a uniform coset law."""
    dim = dimensions[next(g) % len(dimensions)]
    mask, basis, span = (1 << nbits)-1, [], [0]
    while len(basis) < dim:
        vector = next(g) & mask
        if vector not in span:
            basis.append(vector)
            span += [x ^ vector for x in list(span)]
    shift = next(g) & mask
    return {tuple((value >> (nbits-1-i)) & 1 for i in range(nbits)): Fraction(1, 1 << dim)
            for value in [x ^ shift for x in span]}


def fx_b_s4f():
    """Frozen B-S4F definition; execution belongs to the separately authorized design fixtures."""
    omega = list(itertools.product((0, 1), repeat=2))
    laws = [[Fraction(1 if i == j else 0) for j in range(4)] for i in range(4)]
    reads = []
    for i in (0, 1):
        response = [Fraction(3, 8)+Fraction(1 if w[i] == 0 else 0, 4) for w in omega]
        reads += [response, [1-x for x in response]]
    return {"name": "B-S4F", "laws": laws, "reads": reads, "omega": omega,
            "effect_labels": [["E0", 0], ["E0", 1], ["E1", 0], ["E1", 1]],
            "lp_settings": ["E0", "E1"], "acc": ["E0", "E1"]}


def fx_b_ray(base, name):
    """Append the frozen half-mixture of the first two preparations, preserving read order."""
    result = dict(base)
    result["name"] = name
    result["laws"] = list(base["laws"])+[[q_div(a+b, 2) for a, b in zip(base["laws"][0], base["laws"][1])]]
    return result


def qm_restricted_run(src, phi, arm):
    """D22(a)'s exact four CNOT-marker arms, separate from QM-P's five-arm P comparator."""
    h = Fraction(1, 2)
    state = {"X+": [[h, h], [h, h]], "X-": [[h, -h], [-h, h]],
             "Z+": [[1, 0], [0, 0]], "Z-": [[0, 0], [0, 1]]}[src]
    if phi:
        state = _mm(_mm(QZ, state), QZ)
    markers = {"off": [[1, 0], [0, 0]], "on": [[1, 0], [0, 0]],
               "SH-0": [[h, h], [h, h]], "SH-K": [[h, 0], [0, h]]}
    initial = _kron(state, markers[arm])
    return initial if arm == "off" else _mm(_mm(QCNOT, initial), _tr(QCNOT))


def xorshift32(seed):
    x = seed & 0xffffffff
    if x == 0:
        x = 0x9e3779b9
    while True:
        x ^= (x << 13) & 0xffffffff
        x ^= x >> 17
        x ^= (x << 5) & 0xffffffff
        yield x


def _seeded_law(g, nbits):
    cfgs = list(itertools.product((0, 1), repeat=nbits))
    w = {}
    for c in cfgs:
        r = next(g)
        if r % 3 == 0:
            w[c] = 1 + (r >> 8) % 4
    if not w:
        w[cfgs[next(g) % len(cfgs)]] = 1
    tot = sum(w.values())
    return {c: Fraction(v, tot) for c, v in w.items()}


def stress_fixture(kind, seed):
    """C.8.2: a separate coset instance per seed; SF-1 has 32 distinct laws."""
    g, laws = xorshift32(seed), []
    nbits, dimensions, count = (5, (2, 3, 4), 32) if kind == "SF-1" else (4, (1, 2, 3), 91)
    while len(laws) < count:
        law = seeded_coset(g, nbits, dimensions)
        if kind != "SF-1" or law not in laws:
            laws.append(law)
    if kind == "SF-1":
        settings = []
        for ai, an in ((None, "0"), (1, "1"), (2, "2")):
            for pi, pn in ((None, "0"), (3, "1"), (4, "2")):
                indices = [0] + [i for i in (ai, pi) if i is not None]
                settings.append(("M"+an+pn, _bits(*indices)))
    else:
        settings = [("S_Z", _bit(0)), ("S_X", _bit(1)), ("S_Y", _parity(0, 1, 2, 3))]
    return frag_from_laws(kind+"/"+str(seed), laws, tuple(range(nbits)), settings)


# ------------------------------------------------------------------------------------------------------------
# Decision functions (checker side; controls.py carries its own decide-* and X checks that the two agree)
# ------------------------------------------------------------------------------------------------------------
KER_ID = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)))
KER_UNIF = ((Fraction(1, 2), Fraction(1, 2)), (Fraction(1, 2), Fraction(1, 2)))

P_TOKENS = ("P-VOID", "P-NO-FRINGES", "P-NO-RECORD", "P-RECORD-WITHOUT-SUPPRESSION", "P-COMPLEMENTARITY")
B_TOKENS = ("B-VOID", "B-CONTEXTUAL", "B-CLASSICALLY-IMITABLE")
C_TOKENS = ("C-VOID", "C-EXPOSURE", "C-SIZE-DEPENDENT", "C-NONSTABILIZER", "C-SURVIVAL")
ATTR_VALUES = ("attributable to which-path recording", "not attributable", "undefined")


def k_decide_p(rec):
    """Decision rule P (first match). Reads the admissible class, each member's V, D, NONABS and SPI, the off
    and on arms and the P controls; nothing else."""
    try:
        adm = rec["adm"]
        arms = rec["arms"]
        red = rec["controls_red"]
        off = arms[rec["off"]]
        on = arms[rec["on"]]
        for a in adm:
            for f in ("V", "D", "NONABS", "SPI"):
                if f not in arms[a]:
                    return {"token": "P-VOID", "codes": ["missing:" + a + ":" + f]}
        for f in ("V", "D"):
            if f not in off or f not in on:
                return {"token": "P-VOID", "codes": ["missing:off-or-on:" + f]}
    except (KeyError, TypeError):
        return {"token": "P-VOID", "codes": ["missing-field"]}
    if red:
        return {"token": "P-VOID", "codes": list(red)}
    bad = [a for a in adm if arms[a]["NONABS"] is not True or arms[a]["SPI"] is not True]
    if bad:
        return {"token": "P-VOID", "codes": ["NONABS-or-SPI:" + a for a in bad]}
    v_off = Fraction(off["V"])
    if v_off == 0:
        return {"token": "P-NO-FRINGES", "codes": []}
    if Fraction(on["D"]) == 0:
        return {"token": "P-NO-RECORD", "codes": []}
    rws = [a for a in adm if Fraction(arms[a]["D"]) > 0 and Fraction(arms[a]["V"]) >= v_off]
    if rws:
        return {"token": "P-RECORD-WITHOUT-SUPPRESSION", "codes": [], "list": rws}
    return {"token": "P-COMPLEMENTARITY", "codes": []}


def _ker(k):
    return tuple(tuple(Fraction(x) for x in row) for row in k)


def k_attr(off, on, shk):
    """ATTR (owner condition on D14(d)): validation layer; printed beside the P token, never folded into it."""
    try:
        v_off, v_on, d_on = Fraction(off["V"]), Fraction(on["V"]), Fraction(on["D"])
        d_shk, v_shk = Fraction(shk["D"]), Fraction(shk["V"])
        k_shk, k_on = _ker(shk["K"]), _ker(on["K"])
    except (KeyError, TypeError, ValueError):
        return {"value": "undefined", "failing": ["missing-field"]}
    failing = []
    if not (d_on > 0 and v_on < v_off):
        failing.append("the marker does not record and suppress")
    if not (d_shk == 0 and k_shk == k_on):
        failing.append("the kick-matched sham is not valid")
    if failing:
        return {"value": "undefined", "failing": failing}
    if v_shk == v_off:
        return {"value": "attributable to which-path recording", "failing": []}
    return {"value": "not attributable", "failing": []}


def k_ab_p(rec_a, rec_b):
    """A/B report (not read by decide-p): existence and universality for A_P and B, with the owner's case."""
    out = {}
    for lab, rec in (("A_P", rec_a), ("B", rec_b)):
        arms, adm = rec["arms"], rec["adm"]
        v_off = Fraction(arms[rec["off"]]["V"])
        rec_arms = [a for a in adm if Fraction(arms[a]["D"]) > 0]
        rws = [a for a in rec_arms if not Fraction(arms[a]["V"]) < v_off]
        ex = v_off > 0 and any(Fraction(arms[a]["V"]) < v_off for a in rec_arms)
        un = v_off > 0 and len(rec_arms) > 0 and len(rws) == 0
        out[lab] = {"existence": ex, "universality": un, "record_without_suppression": rws}

    def case(key):
        a, b = out["A_P"][key], out["B"][key]
        if not b:
            return "B fails"
        return "both succeed" if a else "A fails and B succeeds"

    out["existence_case"] = case("existence")
    out["universality_case"] = case("universality")
    return out


def k_decompose_p(arms, off, on, sh0, shk):
    """decompose-p: the decomposition by the shams, reported, gating nothing."""
    a0, ak, ao = arms[sh0], arms[shk], arms[on]
    return {"V_SH0": a0["V"], "K_SH0": a0["K"], "V_SHK": ak["V"], "K_SHK": ak["K"], "D_SHK": ak["D"],
            "valid_D_SH0_zero": Fraction(a0["D"]) == 0, "valid_D_SHK_zero": Fraction(ak["D"]) == 0,
            "valid_K_SHK_eq_K_on": _ker(ak["K"]) == _ker(ao["K"]),
            "dephasing_lookalike_V_SHK_eq_V_on": Fraction(ak["V"]) == Fraction(ao["V"]),
            "CPL": {a: arms[a].get("CPL") for a in arms}}


def k_decide_b(rec):
    """Only the unique SG-1 B-P record decides B; other fragment roles are report-only."""
    try:
        if rec["controls_red"]:
            return {"token": "B-VOID", "codes": list(rec["controls_red"])}
        candidates = [f for f in rec["fragments"] if f.get("role") == "B-P"]
        if len(candidates) != 1:
            return {"token": "B-VOID", "codes": ["one-B-P-required"]}
        bp = candidates[0]
        expected = ["M"+a+b for a in ("0", "1", "2") for b in ("0", "1", "2")]
        if bp.get("preps") != 32 or sorted(bp.get("lp_settings", [])) != expected:
            return {"token": "B-VOID", "codes": ["SG-1:32-preparations-nine-settings"]}
        if bp.get("lp_reads_equal_acc") is not True or sorted(bp.get("acc", [])) != expected:
            return {"token": "B-VOID", "codes": ["lp_reads_equal_acc:B-P"]}
        if bp.get("lp") not in ("feasible", "infeasible") or bp.get("verified") is not True:
            return {"token": "B-VOID", "codes": ["B-P:"+str(bp.get("lp")), "limitation:SG-2"]}
        if bp["lp"] == "infeasible":
            return {"token": "B-CONTEXTUAL", "codes": [], "contextual": [bp["name"]]}
        return {"token": "B-CLASSICALLY-IMITABLE", "codes": []}
    except (KeyError, TypeError, ValueError):
        return {"token": "B-VOID", "codes": ["missing-field"]}


def k_decide_c(rec):
    """Decision rule C (first match over test rules and rounds)."""
    try:
        red = rec["controls_red"]
        if red or rec["complete"] is not True or rec["flags_agree"] is not True:
            return {"token": "C-VOID", "codes": list(red) or ["incomplete-or-flags"]}
        inst = rec["instances"]
    except (KeyError, TypeError):
        return {"token": "C-VOID", "codes": ["missing-field"]}

    def conj(i, k):
        return i["HC"][k] and i["CONS"][k] and i["VAL"][k] and i["WCL"] and i["ABL"] and i["EMB"]

    try:
        hit = [i["id"] for i in inst if conj(i, "12")]
        if hit:
            return {"token": "C-EXPOSURE", "codes": [], "instances": hit}
        hit = [i["id"] for i in inst if conj(i, "6") and not conj(i, "12")]
        if hit:
            return {"token": "C-SIZE-DEPENDENT", "codes": [], "instances": hit}
        hit = [i["id"] for i in inst if i["HC"]["12"] and i["VAL"]["12"] and i["WOCT"]["12"] and i["ABL"]
               and i["EMB"]]
        if hit:
            return {"token": "C-NONSTABILIZER", "codes": [], "instances": hit}
    except (KeyError, TypeError):
        return {"token": "C-VOID", "codes": ["missing-field"]}
    return {"token": "C-SURVIVAL", "codes": []}


IDENT_LEVELS = {"L-PATH": (1, 2), "L-PORT": (1, 2), "L-CAL": (3,), "L-UPRIME": (3,)}
LEVEL1_SENTENCE = ("Level 1 here records that the run reproduces a known paper construction (AP1 §4.5 with "
                   "SA-1(c); AP1 Lemma 3) under frozen controls. It is a consistency check, not a new derivation "
                   "and not an independently generated mechanism.")
LEVEL3_SENTENCE = ("Level 3 here joins B-P (P's two-path apparatus) with C-EXPOSURE (the U′ gadget), two "
                   "unrelated instances")
OWNER_LEVEL_SENTENCE = ("… reaching Level 2 does not automatically establish Level 3, and even Level 3 does not "
                        "establish full equivalence.")
UPR_BC_LABEL = "contextuality supplied by U′'s read set"


def k_decide_levels(rec):
    """decide-levels: the largest n whose own conditions and all lower ones hold, with the representation rule
    and UPR-BC. rec: {"P", "B_P": {"contextual", "lp_reads_equal_acc", "acc_owner_typed", "acc_typing"},
    "C", "imported": [ids], "upr_bc": [{"contextual", "restored_by_full"}]}."""
    imported = list(rec.get("imported", []))
    withheld = sorted(ordered_unique([n for i in imported for n in IDENT_LEVELS.get(i, ())]))
    bp = rec.get("B_P", {})
    l1 = rec.get("P") == "P-COMPLEMENTARITY" and 1 not in withheld
    l2 = (l1 and bp.get("contextual") is True and bp.get("lp_reads_equal_acc") is True
          and bp.get("acc_owner_typed") is True and 2 not in withheld)
    l3 = l2 and rec.get("C") == "C-EXPOSURE" and 3 not in withheld
    level = 3 if l3 else 2 if l2 else 1 if l1 else 0
    bench = []
    for i in imported:
        if i in ("L-PATH", "L-PORT"):
            bench += ["P", "B-P"]
        if i in ("L-CAL", "L-UPRIME"):
            bench += ["C"]
    upr = [u for u in rec.get("upr_bc", []) if u.get("contextual") and u.get("restored_by_full")]
    lines = []
    if level >= 1:
        lines.append(LEVEL1_SENTENCE)
    if level >= 2:
        lines.append("B-P's access class is typed " + str(bp.get("acc_typing")) + ".")
    if level >= 3:
        lines.append(LEVEL3_SENTENCE)
    lines.append(OWNER_LEVEL_SENTENCE)
    return {"level": "none" if level == 0 else level, "withheld_levels": withheld,
            "benchmark": sorted(ordered_unique(bench)), "upr_bc_imported_for_bc": len(upr) > 0,
            "upr_bc_label": UPR_BC_LABEL if upr else None, "lines": lines}


# ------------------------------------------------------------------------------------------------------------
# Comparators in fixture mode: CW-P (classical two-beam field) and QM-P (stabilizer QM). Exact rationals.
# ------------------------------------------------------------------------------------------------------------
def isqrt_q(q):
    """The exact square root of a nonnegative rational if it is a perfect square, else None."""
    q = Fraction(q)

    def isq(n):
        if n < 2:
            return n
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x

    a, b = isq(q.numerator), isq(q.denominator)
    if a * a == q.numerator and b * b == q.denominator:
        return Fraction(a, b)
    return None


def _p_quantities(s, d_val, ker, nonabs, spi, eraser, extra=None):
    """Assemble one arm's record: s(src, phi), V, Delta, D, K, NONABS, SPI, CPL, eraser."""
    v = abs(s[("X+", 0)] - s[("X+", 1)])
    delta = {str(f): s[("X+", f)] - q_div(s[("Z+", f)] + s[("Z-", f)], 2) for f in (0, 1)}
    rec = {"s": {"%s,%d" % k: val for k, val in s.items()}, "V": v, "Delta": delta, "D": d_val, "K": ker,
           "NONABS": nonabs, "SPI": spi, "CPL": v * v + d_val * d_val, "eraser": eraser}
    if extra:
        rec.update(extra)
    return rec


def cw_p_model():
    """CW-P: a classical two-beam field, exact. Path amplitudes sqrt(w0), sign*sqrt(w1) with real Jones vectors and
    0/pi phases; square-law intensities at the two ports, optionally behind a polarization analyser.
    Arms: off; polarization marker (H on path 0, V on path 1); SH-0 analogue (the same rotation on both paths);
    SH-K analogue (a recorded random 0/pi phase on path 1). The eraser: the diagonal analyser (conjugate record),
    the H/V analyser (path record), and the recorded phase. D: total variation of the held records (the
    polarization the light carries and the recorded phase) given Z+ against Z-. K: P(port | coherent input) at
    phi = 0, the reduced channel on the relative phase."""
    h = Fraction(1, 2)
    jones = {"off": ((1, 0), (1, 0)), "on": ((1, 0), (0, 1)), "SH-0": ((0, 1), (0, 1)), "SH-K": ((1, 0), (1, 0))}
    analysers = {"none": None, "H": (1, 0), "V": (0, 1), "D": (1, 1), "A": (1, -1)}

    def weights(src):
        if src in ("X+", "X-"):
            return (h, h), (1 if src == "X+" else -1)
        return ((1, 0) if src == "Z+" else (0, 1)), 1

    def branches(src, phi, arm, an):
        """[(probability, I_port0, I_port1, record)] behind analyser `an`."""
        (w0, w1), sign = weights(src)
        j0, j1 = jones[arm]
        out = []
        noise = (0, 1) if arm == "SH-K" else (0,)
        for nz in noise:
            sg = sign * (-1 if phi else 1) * (-1 if nz else 1)
            if analysers[an] is None:
                c00, c11, c01 = Fraction(1), Fraction(1), Fraction(j0[0] * j1[0] + j0[1] * j1[1])
            else:
                a = analysers[an]
                na = a[0] * a[0] + a[1] * a[1]
                p0 = j0[0] * a[0] + j0[1] * a[1]
                p1 = j1[0] * a[0] + j1[1] * a[1]
                c00, c11, c01 = Fraction(p0 * p0, na), Fraction(p1 * p1, na), Fraction(p0 * p1, na)
            amp = isqrt_q(Fraction(w0) * w1)
            base = w0 * c00 + w1 * c11
            i0 = q_div(base + 2 * sg * amp * c01, 2)
            i1 = q_div(base - 2 * sg * amp * c01, 2)
            pol = tuple(j0) if w1 == 0 else tuple(j1) if w0 == 0 else None
            out.append((q_div(1, len(noise)), i0, i1, (pol, nz)))
        return out

    def s_of(src, phi, arm, an="none"):
        num = sum(p * i0 for p, i0, i1, _ in branches(src, phi, arm, an))
        den = sum(p * (i0 + i1) for p, i0, i1, _ in branches(src, phi, arm, an))
        return q_div(num, den) if den else None

    def s_noise(src, phi, nz):
        br = [b for b in branches(src, phi, "SH-K", "none") if b[3][1] == nz]
        return q_div(br[0][1], br[0][1] + br[0][2])

    arms = {}
    for arm in ("off", "on", "SH-0", "SH-K"):
        s = {(src, f): s_of(src, f, arm) for src in ("X+", "X-", "Z+", "Z-") for f in (0, 1)}
        rz = {}
        for src in ("Z+", "Z-"):
            law = {}
            for p, i0, i1, rcd in branches(src, 0, arm, "none"):
                law[rcd] = law.get(rcd, Fraction(0)) + p
            rz[src] = law
        keys = ordered_unique(rz["Z+"]) | ordered_unique(rz["Z-"])
        d_val = q_div(sum(abs(rz["Z+"].get(k, 0) - rz["Z-"].get(k, 0)) for k in keys), 2)
        ker = tuple((s_of(src, 0, arm), 1 - s_of(src, 0, arm)) for src in ("X+", "X-"))
        eraser = {}
        for an_pair, lab in ((("D", "A"), "conjugate"), (("H", "V"), "path")):
            cond = {}
            for b, an in enumerate(an_pair):
                ps = [s_of("X+", f, arm, an) for f in (0, 1)]
                cond[str(b)] = None if None in ps else abs(ps[0] - ps[1])
            eraser[lab] = cond
        if arm == "SH-K":
            eraser["noise"] = {str(nz): abs(s_noise("X+", 0, nz) - s_noise("X+", 1, nz)) for nz in (0, 1)}
        eraser["unsorted"] = abs(s[("X+", 0)] - s[("X+", 1)])
        spi = all(s[(src, f)] == s_of(src, f, "off") for src in ("Z+", "Z-") for f in (0, 1))
        arms[arm] = _p_quantities(s, d_val, ker, True, spi, eraser)
    return {"adm": ["off", "on", "SH-0", "SH-K"], "arms": arms, "off": "off", "on": "on", "sh0": "SH-0",
            "shk": "SH-K", "controls_red": [], "alpha": cw_alpha_two_detector()}


def _mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def _kron(a, b):
    n, m = len(a), len(b)
    return [[Fraction(a[i // m][j // m]) * b[i % m][j % m] for j in range(n * m)] for i in range(n * m)]


def _tr(a):
    return [list(r) for r in zip(*a)]


QI2 = [[1, 0], [0, 1]]
QX = [[0, 1], [1, 0]]
QZ = [[1, 0], [0, -1]]
QCNOT = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
QCZ = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, -1]]


def qm_run(src, phi, arm):
    """Stabilizer QM under P's protocol (path S first, environment E second): Z^phi on S, the arm, then the
    screen's X read of S. Returns the 4x4 real density matrix after the arm."""
    h = Fraction(1, 2)
    s = {"X+": [[h, h], [h, h]], "X-": [[h, -h], [-h, h]], "Z+": [[1, 0], [0, 0]], "Z-": [[0, 0], [0, 1]]}[src]
    s = [[Fraction(x) for x in r] for r in s]
    if phi:
        s = _mm(_mm(QZ, s), QZ)
    e0 = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(0)]]
    if arm == "off":
        return _kron(s, e0)
    if arm == "on":
        return _mm(_mm(QCNOT, _kron(s, e0)), _tr(QCNOT))
    if arm == "SH-0":
        u = _kron(QI2, QX)
        return _mm(_mm(u, _kron(s, e0)), _tr(u))
    if arm == "SH-K":
        rho = [[Fraction(0)] * 4 for _ in range(4)]
        for w in (0, 1):
            sw = _mm(_mm(QZ, s), QZ) if w else s
            ew = [[Fraction(1 - w), Fraction(0)], [Fraction(0), Fraction(w)]]
            t = _kron(sw, ew)
            rho = [[rho[i][j] + h * t[i][j] for j in range(4)] for i in range(4)]
        return rho
    if arm == "purified":
        e = [[h, h], [h, h]]
        return _mm(_mm(QCZ, _kron(s, e)), _tr(QCZ))
    raise ValueError(arm)


def _ptrace_e(rho):
    return [[rho[2 * i][2 * j] + rho[2 * i + 1][2 * j + 1] for j in range(2)] for i in range(2)]


def _ptrace_s(rho):
    return [[rho[i][j] + rho[2 + i][2 + j] for j in range(2)] for i in range(2)]


def _p_plus(m):
    return q_div(m[0][0] + m[0][1] + m[1][0] + m[1][1], 2)


def _joint_s_e(rho, ebasis):
    """P(screen outcome x, environment outcome b) for the S X-read and an E read in basis 'Z' or 'X'."""
    h = Fraction(1, 2)
    px = {0: [[h, h], [h, h]], 1: [[h, -h], [-h, h]]}
    pz = {0: [[1, 0], [0, 0]], 1: [[0, 0], [0, 1]]}
    pe = px if ebasis == "X" else pz
    out = {}
    for x in (0, 1):
        for b in (0, 1):
            proj = _kron(px[x], pe[b])
            out[(x, b)] = sum(proj[i][j] * rho[j][i] for i in range(4) for j in range(4))
    return out


def qm_p_model():
    """QM-P: arms off, CNOT marker (on), X on E (SH-0), recorded classical noise Z^w (SH-K), purified dephasing
    (E in |+>, CZ). D: trace distance of E's state given path |0> vs |1>, max over phi (exact; perfect squares)."""
    arms = {}
    for arm in ("off", "on", "SH-0", "SH-K", "purified"):
        s = {(src, f): _p_plus(_ptrace_e(qm_run(src, f, arm))) for src in ("X+", "X-", "Z+", "Z-") for f in (0, 1)}
        dvals = []
        for f in (0, 1):
            a, b = _ptrace_s(qm_run("Z+", f, arm)), _ptrace_s(qm_run("Z-", f, arm))
            dd = [[a[i][j] - b[i][j] for j in range(2)] for i in range(2)]
            dvals.append(isqrt_q(dd[0][0] * dd[0][0] + dd[0][1] * dd[0][1]))
        d_val = max(dvals)
        ker = []
        for src in ("X+", "X-"):
            pp = _p_plus(_ptrace_e(qm_run(src, 0, arm)))
            ker.append((pp, 1 - pp))
        ker = tuple(ker)
        nonabs = all(_ptrace_e(qm_run(src, f, arm))[z][z] == 1 for src, z in (("Z+", 0), ("Z-", 1)) for f in (0, 1))
        spi = all(s[(src, f)] == _p_plus(_ptrace_e(qm_run(src, f, "off"))) for src in ("Z+", "Z-") for f in (0, 1))
        eraser = {}
        for eb in ("Z", "X"):
            cond = {}
            for b in (0, 1):
                ps = []
                for f in (0, 1):
                    j = _joint_s_e(qm_run("X+", f, arm), eb)
                    tot = j[(0, b)] + j[(1, b)]
                    ps.append(q_div(j[(0, b)], tot) if tot else None)
                cond[str(b)] = None if None in ps else abs(ps[0] - ps[1])
            eraser[eb] = cond
        eraser["unsorted"] = abs(s[("X+", 0)] - s[("X+", 1)])
        arms[arm] = _p_quantities(s, d_val, ker, nonabs, spi, eraser)
    return {"adm": ["off", "on", "SH-0", "SH-K", "purified"], "arms": arms, "off": "off", "on": "on",
            "sh0": "SH-0", "shk": "SH-K", "controls_red": []}


QM_SLOT_BASIS = {0: "X", 1: "Z"}


def qm_p_fragment():
    """QM-P's fragment on the p-free settings M00, M10, M20: preparations {X+-, Z+-} x phi x {off, on, SH-0,
    SH-K}; M00 reads the screen; M10 (M20) the screen and E in the basis of held slot 0 (slot 1). Laws in the
    product embedding over the three settings' outcomes (a configuration model reproducing the table)."""
    laws = []
    for src in ("X+", "X-", "Z+", "Z-"):
        for f in (0, 1):
            for arm in ("off", "on", "SH-0", "SH-K"):
                rho = qm_restricted_run(src, f, arm)
                m00 = {x: _p_plus(_ptrace_e(rho)) if x == 0 else 1 - _p_plus(_ptrace_e(rho)) for x in (0, 1)}
                m10 = _joint_s_e(rho, QM_SLOT_BASIS[0])
                m20 = _joint_s_e(rho, QM_SLOT_BASIS[1])
                law = {}
                for x0 in (0, 1):
                    for k1, p1 in m10.items():
                        for k2, p2 in m20.items():
                            w = m00[x0] * p1 * p2
                            if w:
                                law[(x0,) + k1 + k2] = w
                laws.append(law)
    st = [("M00", _bit(0)), ("M10", _bits(1, 2)), ("M20", _bits(3, 4))]
    return frag_from_laws("QM-P", laws, (0, 1, 2, 3, 4), st)


# ------------------------------------------------------------------------------------------------------------
# The model of P (frozen): the armed-edge step and the simulator. Every probability is an N2 configuration count.
# ------------------------------------------------------------------------------------------------------------
def native_step(state, edges):
    """The class-N step on armed edges: u_i' = sum_{j armed with i} u_j + v_i, v_i' = u_i. An unarmed cell
    swaps its slots (empty sum). state: {cell: (u, v)}; edges: set of frozenset pairs."""
    out = {}
    for i, (u, v) in state.items():
        nb = [j for j in state if j != i and ordered_key((i, j)) in edges]
        out[i] = ((sum(state[j][0] for j in nb) + v) % 2, u)
    return out


SRC_SPEC = {"X+": ("c", 0), "X-": ("c", 1), "Z+": (0, "c"), "Z-": (1, "c"), "L": ("c", "c2")}


def _slot_val(spec, env, prefix):
    if isinstance(spec, int):
        return spec
    if spec.endswith("+1"):
        return (env[prefix + spec[:-2]] + 1) % 2
    return env[prefix + spec]


def _symbols(spec, prefix):
    out = []
    for x in spec:
        if isinstance(x, str):
            out.append(prefix + (x[:-2] if x.endswith("+1") else x))
    return out


def p_sim(src, phi, arm, opts=None):
    """One P run, exactly enumerated. arm: {"cells": [supply, ...], "mode": "armed" | "off" | "copy" | "xswap" |
    "absorb"}; a supply is a pair of slot specs (0, 1, a symbol "w", or "w+1"), stated at its coupling tick.
    opts: {"path": None | "alpha" | "beta", "port": None | "alpha" | "beta" | "plant"} (REP-INV, REP-PLANT).
    Returns rows {w, kept, port, z0, z1, xb, xa, arms (end), phase (end), carrier (end), screen (end)}."""
    opts = opts or {}
    path_alt, port_alt = opts.get("path"), opts.get("port")
    cspec = SRC_SPEC[src]
    if path_alt == "alpha" and src in ("Z+", "Z-"):
        cspec = SRC_SPEC["Z-" if src == "Z+" else "Z+"]
    cells = arm["cells"]
    mode = arm["mode"]
    syms = _symbols(cspec, "c:") + ["p:w", "s:w"]
    for k, sup in enumerate(cells):
        syms += _symbols(sup, "a%d:" % k)
    syms = sorted(ordered_unique(syms))
    rows = []
    weight = Fraction(1, 2 ** len(syms))
    shift = 1 if path_alt == "beta" else 0
    for bits in itertools.product((0, 1), repeat=len(syms)):
        env = dict(zip(syms, bits))
        c0 = (_slot_val(cspec[0], env, "c:"), _slot_val(cspec[1], env, "c:"))
        st = {"c": (c0[1], c0[0]) if shift else c0}
        if shift:
            st = native_step(st, ordered_unique())                       # beta: the prepended free tick
        st["p"] = (phi, env["p:w"])                           # the phase cell at its coupling tick
        st = native_step(st, ordered_unique([ordered_key(("c", "p"))]))          # c-p armed
        st = native_step(st, ordered_unique())                            # free
        for k, sup in enumerate(cells):                         # arm cells at their coupling tick
            st["a%d" % k] = (_slot_val(sup[0], env, "a%d:" % k), _slot_val(sup[1], env, "a%d:" % k))
        z0, xb = st["c"]                                        # before the arm tick: (z, x) = (u, v)
        kept = True
        anames = ["a%d" % k for k in range(len(cells))]
        if mode in ("armed", "absorb"):
            st = native_step(st, ordered_unique([ordered_key(("c", a)) for a in anames]))
            if mode == "absorb" and z0 == 1:
                kept = False
        elif mode == "copy":
            new = native_step(st, ordered_unique())
            for a in anames:
                new[a] = ((st["c"][0] + st[a][1]) % 2, st[a][0])
            st = new
        elif mode == "xswap":
            a0 = anames[0]
            cu, cv = st["c"]
            au, av = st[a0]
            st = dict(st)
            st["c"], st[a0] = (cu, au), (cv, av)
            st = native_step(st, ordered_unique())
        elif mode == "off":
            st = native_step(st, ordered_unique())
        else:
            raise ValueError(mode)
        xa, z1 = st["c"]                                        # after the arm tick: (z, x) = (v, u)
        st["s"] = (env["s:w"], 0)                               # the screen (w_s, 0) at its coupling tick
        st = native_step(st, ordered_unique([ordered_key(("c", "s"))]))          # c-s armed; u_s registered
        us = st["s"][0]
        if port_alt == "beta":
            us = native_step({"s": st["s"]}, ordered_unique())["s"][1]     # one free tick later, from the slot holding it
        port = us
        if port_alt == "alpha":
            port = (us + 1) % 2
        if port_alt == "plant":
            port = (us + st["a0"][0]) % 2 if cells else us      # REP-PLANT: XOR with the marker's kick slot
        rows.append({"w": weight, "kept": kept, "port": port, "z0": z0, "z1": z1, "xb": xb, "xa": xa,
                     "arms": tuple(st[a] for a in anames), "phase": st["p"], "carrier": st["c"],
                     "screen": st["s"]})
    return rows


def _law(rows, key):
    out = {}
    for r in rows:
        if r["kept"]:
            k = key(r)
            out[k] = out.get(k, Fraction(0)) + r["w"]
    return out


def _tv(a, b):
    return q_div(sum(abs(a.get(k, 0) - b.get(k, 0)) for k in ordered_unique(a) | ordered_unique(b)), 2)


def p_arm_record(arm, opts=None, coherent="X+"):
    """Every P quantity of one arm (observer layer and validation layer)."""
    runs = {(src, f): p_sim(src, f, arm, opts) for src in ("X+", "X-", "Z+", "Z-", "L") for f in (0, 1)}

    def s_of(src, f):
        rows = runs[(src, f)]
        tot = sum(r["w"] for r in rows if r["kept"])
        return q_div(sum(r["w"] for r in rows if r["kept"] and r["port"] == 0), tot) if tot else None

    s = {(src, f): s_of(src, f) for src in ("X+", "X-", "Z+", "Z-", "L") for f in (0, 1)}
    ok = all(v is not None for v in s.values())
    v_val = abs(s[(coherent, 0)] - s[(coherent, 1)]) if ok else None
    held = lambda r: r["arms"] + (r["phase"],)
    d_val = max(_tv(_law(runs[("Z+", f)], held), _law(runs[("Z-", f)], held)) for f in (0, 1))
    d_phase = max(_tv(_law(runs[("Z+", f)], lambda r: r["phase"]), _law(runs[("Z-", f)], lambda r: r["phase"]))
                  for f in (0, 1))
    cnt = {}
    for src in ("X+", "X-"):
        for f in (0, 1):
            for r in runs[(src, f)]:
                if r["kept"]:
                    cnt[(r["xb"], r["xa"])] = cnt.get((r["xb"], r["xa"]), Fraction(0)) + r["w"]
    ker = []
    for xb in (0, 1):
        tot = cnt.get((xb, 0), 0) + cnt.get((xb, 1), 0)
        ker.append(tuple(q_div(cnt.get((xb, xa), 0), tot) if tot else None for xa in (0, 1)))
    nonabs = all(r["kept"] for rows in runs.values() for r in rows) and all(
        r["z1"] == r["z0"] for src in ("Z+", "Z-") for f in (0, 1) for r in runs[(src, f)])
    eraser = {}
    for k in range(len(arm["cells"])):
        for sl in (0, 1):
            cond = {}
            for b in (0, 1):
                ps = []
                for f in (0, 1):
                    rows = [r for r in runs[(coherent, f)] if r["kept"] and r["arms"][k][sl] == b]
                    tot = sum(r["w"] for r in rows)
                    ps.append(q_div(sum(r["w"] for r in rows if r["port"] == 0), tot) if tot else None)
                cond[str(b)] = None if None in ps else abs(ps[0] - ps[1])
            eraser["cell%d.slot%d" % (k, sl)] = cond
    eraser["unsorted"] = v_val
    rec = {"s": {"%s,%d" % k: v for k, v in s.items()}, "V": v_val, "D": d_val, "D_phase": d_phase,
           "K": tuple(ker), "NONABS": nonabs, "eraser": eraser}
    if ok:
        rec["Delta"] = {str(f): s[(coherent, f)] - q_div(s[("Z+", f)] + s[("Z-", f)], 2) for f in (0, 1)}
        rec["CPL"] = v_val * v_val + d_val * d_val
    world = {}
    for (src, f), rows in runs.items():
        world["%s,%d" % (src, f)] = _law(rows, lambda r: (r["carrier"], r["phase"], r["arms"], r["screen"]))
    return rec, runs, world


def p_olc(runs, k=0):
    """OLC for a read-set ablation: both slots of held arm cell k registered jointly with the screen."""
    out = {}
    keys = sorted(ordered_unique([r["arms"][k] for f in (0, 1) for r in runs[("X+", f)] if r["kept"]]))
    joint = False
    for key in keys:
        ps, pz = [], None
        for f in (0, 1):
            sub = [r for r in runs[("X+", f)] if r["kept"] and r["arms"][k] == key]
            tot = sum(r["w"] for r in sub)
            ps.append(q_div(sum(r["w"] for r in sub if r["port"] == 0), tot) if tot else None)
            if f == 0 and tot:
                pz = abs(2 * q_div(sum(r["w"] for r in sub if r["z0"] == 0), tot) - 1)
        v = None if None in ps else abs(ps[0] - ps[1])
        out["%d%d" % key] = {"V": v, "Pz": pz}
        if v == 1 and pz == 1:
            joint = True
    return {"subsets": out, "joint": joint}


def sup_name(sup):
    def one(x):
        if isinstance(x, int):
            return str(x)
        return {"w": "w", "w'": "w'", "w+1": "w+1"}.get(x, x)
    return "(%s,%s)" % (one(sup[0]), one(sup[1]))


ALPHABET_SLOTWISE = [(a, b) for a in (0, 1, "w") for b in (0, 1, "w'")]
ALPHABET_UV = [("w", "w"), ("w", "w+1")]


def p_classes():
    """Adm_B and Adm_A generated by rule from the frozen alphabet Sigma (re-review r8-N3)."""
    off = ("off", {"cells": [("w", 0)], "mode": "off"})
    sigma = [(sup_name(s), {"cells": [s], "mode": "armed"}) for s in ALPHABET_SLOTWISE + ALPHABET_UV]

    def one_known(s):
        return isinstance(s[0], int) != isinstance(s[1], int)

    adm_b = [off] + [(sup_name(s), {"cells": [s], "mode": "armed"}) for s in ALPHABET_SLOTWISE if one_known(s)]
    adm_b += [("(w,w')", {"cells": [("w", "w'")], "mode": "armed"})]
    adm_a = [off] + sigma
    return adm_b, adm_a


NAME_ON, NAME_SH0, NAME_SHK = "(w,0)", "(0,w')", "(w,w')"


def p_class_record(arms, controls_red=(), opts=None, coherent="X+"):
    recs, runs, worlds = {}, {}, {}
    for name, arm in arms:
        recs[name], runs[name], worlds[name] = p_arm_record(arm, opts, coherent)
        recs[name]["SPI"] = None
    off_s = recs["off"]["s"]
    for name in recs:
        recs[name]["SPI"] = all(recs[name]["s"]["%s,%d" % (src, f)] == off_s["%s,%d" % (src, f)]
                                for src in ("Z+", "Z-") for f in (0, 1))
    return {"adm": [n for n, _ in arms], "arms": recs, "off": "off", "on": NAME_ON, "sh0": NAME_SH0,
            "shk": NAME_SHK, "controls_red": list(controls_red)}, runs, worlds


def _cell(r):
    return (fstr(r["V"]) if r["V"] is not None else None, fstr(r["D"]),
            tuple(tuple(fstr(x) if x is not None else None for x in row) for row in r["K"]))


def p_mechmap(cls, arms_def):
    m = {}
    for name, arm in arms_def:
        coupling = {"armed": "reciprocal", "copy": "copy-only", "off": "unarmed"}.get(arm["mode"], arm["mode"])
        mech = (tuple(sup_name(c) for c in arm["cells"]), coupling)
        m.setdefault(_cell(cls["arms"][name]), {})[mech] = None
    return m


def p_observer(rec):
    return {k: rec.get(k) for k in ("s", "V", "Delta", "eraser")}


def p_ablation_fields(ref_cls, ref_def, ref_worlds, abl_cls, abl_def, abl_worlds, olc=None):
    """pred_change, mech_change and access_only (computed)."""
    ref_obs = {n: p_observer(ref_cls["arms"][n]) for n in ref_cls["adm"]}
    abl_obs = {n: p_observer(abl_cls["arms"][n]) for n in abl_cls["adm"]}
    if olc is not None:
        added = ["OLC.joint"]
        for subset in sorted(olc["subsets"]):
            added += ["OLC."+subset+".V", "OLC."+subset+".Pz"]
        pred = {"common": canonical(ref_obs) != canonical(abl_obs), "added": sorted(added)}
    else:
        pred = canonical(ref_obs) != canonical(abl_obs)
    mr, ma = p_mechmap(ref_cls, ref_def), p_mechmap(abl_cls, abl_def)
    changed = []
    for c in sorted(ordered_unique(mr) | ordered_unique(ma), key=lambda x: canonical(list(x))):
        if mr.get(c, ordered_unique()) != ma.get(c, ordered_unique()):
            changed.append({"cell": list(c), "B": sorted(map(list, mr.get(c, ordered_unique()))),
                            "ablation": sorted(map(list, ma.get(c, ordered_unique())))})
    names_r, names_a = ordered_unique(ref_cls["adm"]), ordered_unique(abl_cls["adm"])
    access = names_r == names_a and all(canonical(ref_worlds[n]) == canonical(abl_worlds[n]) for n in names_r)
    return {"pred_change": pred, "mech_change": changed, "access_only": access}


ABL_KIND = {"ABL-SA1c": ("state restriction", "none"), "ABL-SA1b": ("access restriction", "none"),
            "ABL-RECIP": ("dynamics", "a different mechanism"), "ABL-ENV-u": ("state restriction", "none"),
            "ABL-ENV-v": ("state restriction", "none"), "ABL-P3": ("dynamics", "-")}


def s_build_p():
    """Decisive family: P's arm classes Adm_A and Adm_B, the ablations, OLC, the A/B report, and the
    decisive-mode P controls (AB-P-FIX, MECH-FIX, ACC-ONLY-FIX, PL-*)."""
    s_refusal()
    adm_b, adm_a = p_classes()
    cls_b, runs_b, worlds_b = p_class_record(adm_b)
    cls_a, runs_a, worlds_a = p_class_record(adm_a)
    out = {"Adm_B": {"size": len(adm_b), "members": [n for n, _ in adm_b]},
           "Adm_A": {"size": len(adm_a), "members": [n for n, _ in adm_a]},
           "arms": cls_b["arms"], "arms_A": cls_a["arms"]}
    out["decide_p_inputs"] = {"adm": cls_b["adm"], "off": "off", "on": NAME_ON,
                              "arms": {n: {k: cls_b["arms"][n][k] for k in ("V", "D", "NONABS", "SPI")}
                                       for n in cls_b["adm"]}}
    out["ATTR"] = k_attr(cls_b["arms"]["off"], cls_b["arms"][NAME_ON], cls_b["arms"][NAME_SHK])
    out["decompose_p"] = k_decompose_p(cls_b["arms"], "off", NAME_ON, NAME_SH0, NAME_SHK)
    out["ab_p"] = k_ab_p(cls_a, cls_b)
    # A_P against B: the three fields
    out["ab_p_fields"] = p_ablation_fields(cls_b, adm_b, worlds_b, cls_a, adm_a, worlds_a)
    abl = {}
    abl["ABL-SA1c"] = (adm_a, cls_a, worlds_a, None)
    recip = adm_b + [("copy:" + n, {"cells": a["cells"], "mode": "copy"}) for n, a in adm_b if a["mode"] == "armed"]
    abl["ABL-RECIP"] = (recip,) + p_class_record(recip)[0::2] + (None,)
    env_u = [(n, a) for n, a in adm_b if n != NAME_SHK] + [("ENV-u:(0,w')", {"cells": [(0, "w'")], "mode": "armed"})]
    env_v = [(n, a) for n, a in adm_b if n != NAME_SHK] + [("ENV-v:(w,0)", {"cells": [("w", 0)], "mode": "armed"})]
    abl["ABL-ENV-u"] = (env_u,) + p_class_record(env_u)[0::2] + (None,)
    abl["ABL-ENV-v"] = (env_v,) + p_class_record(env_v)[0::2] + (None,)
    olc = p_olc(runs_b[NAME_ON], 0)
    abl["ABL-SA1b"] = (adm_b, cls_b, worlds_b, olc)
    out["ablate_p"] = {}
    for name, (adef, acls, aworlds, aolc) in abl.items():
        fields = p_ablation_fields(cls_b, adm_b, worlds_b, acls, adef, aworlds, aolc)
        kind, credit = ABL_KIND[name]
        rec = dict(fields, kind=kind, dynamics_credit=credit)
        if aolc is not None:
            rec["token"] = "not applicable (access ablation)"
            rec["OLC"] = aolc
        else:
            rec["token"] = k_decide_p(acls)["token"]
        if name in ("ABL-ENV-u", "ABL-ENV-v"):
            env_name = [n for n in acls["adm"] if n.startswith("ENV-")][0]
            rec["env_arm"] = {k: acls["arms"][env_name][k] for k in ("V", "D", "K")}
        out["ablate_p"][name] = rec
    out["ablate_p"]["ABL-P3"] = {"token": "not posable (NR-16)", "kind": "dynamics", "dynamics_credit": "-"}
    out["controls"] = p_decisive_controls(cls_b, adm_b, out)
    return out


def p_decisive_controls(cls_b, adm_b, out):
    """AB-P-FIX, MECH-FIX, ACC-ONLY-FIX and the PL-* fixtures (decisive mode)."""
    ctl = {}
    ab = out["ab_p"]
    sharp = ["(0,0)", "(0,1)", "(1,0)", "(1,1)"]
    ctl["AB-P-FIX"] = {"green": ab["existence_case"] == "both succeed"
                       and ab["A_P"]["universality"] is False and ab["B"]["universality"] is True
                       and sorted(ab["A_P"]["record_without_suppression"]) == sharp,
                       "existence_case": ab["existence_case"], "universality_case": ab["universality_case"],
                       "listed": ab["A_P"]["record_without_suppression"]}
    mc = out["ablate_p"]["ABL-SA1c"]["mech_change"]
    sharp_cells = [c for c in mc if c["cell"][0] == "1" and c["cell"][1] == "1"
                   and any(m[0][0] in sharp for m in c["ablation"])]
    mr = out["ablate_p"]["ABL-RECIP"]["mech_change"]
    copy_added = any(m[1] == "copy-only" for c in mr for m in c["ablation"])
    ctl["MECH-FIX"] = {"green": len(sharp_cells) == 2 and copy_added, "sharp_cells": len(sharp_cells),
                       "copy_added": copy_added}
    ctl["ACC-ONLY-FIX"] = {"green": out["ablate_p"]["ABL-SA1b"]["access_only"] is True
                           and out["ablate_p"]["ABL-SA1c"]["access_only"] is False}

    def with_on(on_arm):
        arms = [(n, a) for n, a in adm_b if n != NAME_ON] + [(NAME_ON, on_arm)]
        return p_class_record(arms)[0]

    conf = with_on({"cells": [(0, 0), ("w", "w'")], "mode": "armed"})
    tok = k_decide_p(conf)["token"]
    attr = k_attr(conf["arms"]["off"], conf["arms"][NAME_ON], conf["arms"][NAME_SHK])
    ctl["PL-CONFOUND"] = {"green": tok == "P-COMPLEMENTARITY" and _ker(conf["arms"][NAME_ON]["K"]) == KER_UNIF
                          and attr["value"] != "attributable to which-path recording", "token": tok,
                          "ATTR": attr["value"]}
    norec = with_on({"cells": [("w", "w'")], "mode": "armed"})
    tok = k_decide_p(norec)["token"]
    ctl["PL-NOREC"] = {"green": tok == "P-NO-RECORD", "token": tok}
    sharp_cls = p_class_record(adm_b + [("(0,0)", {"cells": [(0, 0)], "mode": "armed"})])[0]
    d = k_decide_p(sharp_cls)
    ctl["PL-SHARP"] = {"green": d["token"] == "P-RECORD-WITHOUT-SUPPRESSION" and "(0,0)" in d.get("list", [])
                       and sharp_cls["arms"]["(0,0)"]["CPL"] == 2, "token": d["token"], "list": d.get("list"),
                       "CPL": sharp_cls["arms"]["(0,0)"]["CPL"]}
    absorb = with_on({"cells": [("w", 0)], "mode": "absorb"})
    d = k_decide_p(absorb)
    ctl["PL-ABSORB"] = {"green": d["token"] == "P-VOID" and absorb["arms"][NAME_ON]["NONABS"] is False,
                        "token": d["token"]}
    spi = with_on({"cells": [(0, 0)], "mode": "xswap"})
    d = k_decide_p(spi)
    k_spi = _ker(spi["arms"][NAME_ON]["K"])
    const = k_spi[0] == k_spi[1] and all(x in (0, 1) for x in k_spi[0])
    ctl["PL-SPI"] = {"green": d["token"] == "P-VOID" and spi["arms"][NAME_ON]["SPI"] is False and const
                     and k_spi != KER_ID and k_spi != KER_UNIF, "token": d["token"], "K": k_spi}
    nofr = p_class_record(adm_b, coherent="L")[0]
    tok = k_decide_p(nofr)["token"]
    ctl["PL-NOFR"] = {"green": tok == "P-NO-FRINGES", "token": tok}
    return ctl


# ------------------------------------------------------------------------------------------------------------
# B's fragments from P's construction (decisive): B-P, construction A of B, completions; and B-P against QM-P
# ------------------------------------------------------------------------------------------------------------
BP_SLOTS = {"c_u": 0, "c_v": 1, "p_u": 2, "p_v": 3, "a_u": 4, "a_v": 5, "s_u": 6, "s_v": 7}
ACC_BP = ["M00", "M01", "M02", "M10", "M11", "M12", "M20", "M21", "M22"]
ACC_BP_TYPING = "owner-typed candidate strengthened access principle (D15(a); c.6735014875)"


def bp_settings():
    """Acc(B-P) under D15(a): the screen u_s with at most one slot of a and at most one slot of p."""
    sl = BP_SLOTS
    st = []
    for an, ai in (("0", None), ("1", sl["a_u"]), ("2", sl["a_v"])):
        for pn, pi in (("0", None), ("1", sl["p_u"]), ("2", sl["p_v"])):
            idx = tuple([sl["s_u"]] + [i for i in (ai, pi) if i is not None])
            st.append(("M" + an + pn, idx))
    return sorted(st)


def bp_laws(opts=None):
    """B-P's 32 preparations: {X+-, Z+-} x phi in {0, 1} x arms {off, on, SH-0, SH-K}; each the joint law of all
    eight slots at the end of the run."""
    adm_b, _ = p_classes()
    sel = dict(adm_b)
    order = [("off", sel["off"]), (NAME_ON, sel[NAME_ON]), (NAME_SH0, sel[NAME_SH0]), (NAME_SHK, sel[NAME_SHK])]
    laws, labels = [], []
    for src in ("X+", "X-", "Z+", "Z-"):
        for f in (0, 1):
            for name, arm in order:
                rows = p_sim(src, f, arm, opts)
                law = {}
                for r in rows:
                    if r["kept"]:
                        cfg = r["carrier"] + r["phase"] + r["arms"][0] + (r["port"], r["screen"][1])
                        law[cfg] = law.get(cfg, Fraction(0)) + r["w"]
                laws.append(law)
                labels.append([src, f, name])
    return laws, labels


def _proj_setting(idx, read_slots):
    pos = [read_slots.index(i) for i in idx]
    return lambda w: tuple(w[k] for k in pos)


def bp_fragment(laws, settings, read_slots, name, acc):
    st = [(n, _proj_setting(idx, read_slots)) for n, idx in settings]
    return frag_from_laws(name, laws, read_slots, st, acc=acc)


def s_build_b(p_out=None, c_out=None, budget_vals=(None, None, None)):
    """Decisive family: B-P, construction A of B, their completions, and B-C for flagged C instances."""
    s_refusal()
    sl = BP_SLOTS
    laws, labels = bp_laws()
    read5 = tuple(sorted([sl["s_u"], sl["a_u"], sl["a_v"], sl["p_u"], sl["p_v"]]))
    all8 = tuple(range(8))
    sts = bp_settings()
    frs = []
    bp = bp_fragment(laws, sts, read5, "B-P", ACC_BP)
    rec = s_decide(bp, (BP_P_MAX, BP_B_MAX, BP_W_MAX),
                   cap_vals=(BP_CAP_GENERATORS, BP_CAP_D, BP_CAP_FACET_SUBSETS, BP_CAP_EFFECTS))
    rec.update({"role": "B-P", "lp_reads_equal_acc": sorted(bp["lp_settings"]) == sorted(bp["acc"]),
                "acc": bp["acc"], "acc_typing": ACC_BP_TYPING, "TOMO": rec["tomo"]})
    frs.append(rec)
    completions = [("held-joint", sts + [("JH", read5)], read5), ("all-joint", sts + [("JA", all8)], all8)]
    rec["completion"] = None
    if rec["lp"] == "infeasible":
        for cname, cst, rs in completions:
            cf = bp_fragment(laws, cst, rs, "B-P+" + cname, ACC_BP + [cst[-1][0]])
            cr = s_decide(cf, budget_vals)
            cr.update({"role": "completion", "rank_added": cr["d"] - rec["d"]})
            frs.append(cr)
            if cr["lp"] == "feasible" and cr["verified"]:
                rec["completion"] = cname
                break
    a_of_b = bp_fragment(laws, [("JA", all8)], all8, "A-of-B", ["JA"])
    ra = s_decide(a_of_b, budget_vals)
    ra.update({"role": "A-of-B", "lp_reads_equal_acc": True, "TOMO": ra["tomo"]})
    frs.append(ra)
    restricted = bp_restricted_equals_qmp(laws, labels)
    out = {"fragments": frs, "bp_equals_qmp": restricted, "B1": {"alpha": 0}}
    out["B-C"] = []
    for inst in (c_out or {}).get("flagged", []):
        out["B-C"].append(bc_fragment_decide(inst, budget_vals))
    return out


def bp_restricted_equals_qmp(laws, labels):
    """Exact comparison on M00/M10/M20, under D22's map, with no outcome relabelling; report only."""
    sl = BP_SLOTS
    qmap = {"off": "off", NAME_ON: "on", NAME_SH0: "SH-0", NAME_SHK: "SH-K"}
    result = {}
    for arm, qm_arm in qmap.items():
        exact, checked = True, 0
        for law, (src, phi, label) in zip(laws, labels):
            if label != arm:
                continue
            rho = qm_restricted_run(src, phi, qm_arm)
            screen = sum(prob for cfg, prob in law.items() if cfg[sl["s_u"]] == 0)
            exact = exact and screen == _p_plus(_ptrace_e(rho))
            for slot, key in ((0, "a_u"), (1, "a_v")):
                actual = {}
                for cfg, prob in law.items():
                    outcome = (cfg[sl["s_u"]], cfg[sl[key]])
                    actual[outcome] = actual.get(outcome, Fraction(0))+prob
                target = _joint_s_e(rho, QM_SLOT_BASIS[slot])
                exact = exact and all(actual.get(key, 0) == value for key, value in target.items())
            checked += 1
        result[arm] = {"exact": exact and checked == 8, "preparations_checked": checked}
    result["holds"] = all(result[arm]["exact"] for arm in qmap)
    return result


# ------------------------------------------------------------------------------------------------------------
# Obligation C: the ring Z_3, U' on cells 0-1, the rules Phi_g, 150 rounds, orbits, detectors, witnesses
# ------------------------------------------------------------------------------------------------------------
RULES = {"0": (0, 0, 0), "AND": (0, 0, 1), "XOR": (0, 1, 0), "OR": (0, 1, 1),
         "NOR": (1, 0, 0), "XNOR": (1, 0, 1), "NAND": (1, 1, 0), "1": (1, 1, 1)}
TEST_RULES = ("AND", "NAND", "OR", "NOR")
AFFINE_RULES = ("0", "1", "XOR", "XNOR")


def g_eval(g, a, b):
    t = RULES[g]
    return t[a + b] if a + b != 1 else t[1]


def ring_idx(cfg):
    """cfg = (u0, v0, u1, v1, u2, v2) -> 0..63; carrier = idx >> 2, mediator = idx & 3."""
    i = 0
    for b in cfg:
        i = 2 * i + b
    return i


def ring_cfg(i):
    return tuple((i >> (5 - k)) & 1 for k in range(6))


def phi_g_cfg(g, cfg):
    u = (cfg[0], cfg[2], cfg[4])
    v = (cfg[1], cfg[3], cfg[5])
    out = []
    for i in range(3):
        out += [(g_eval(g, u[(i - 1) % 3], u[(i + 1) % 3]) + v[i]) % 2, u[i]]
    return tuple(out)


def phi_perm(g, k):
    base = [ring_idx(phi_g_cfg(g, ring_cfg(i))) for i in range(64)]
    p = list(range(64))
    for _ in range(k):
        p = [base[x] for x in p]
    return p


def inverse_phi_cfg(g, cfg):
    """C-STEP's independently written inverse: (u, v) = (v', u' + g(v'_{i-1}, v'_{i+1}))."""
    up = (cfg[0], cfg[2], cfg[4])
    vp = (cfg[1], cfg[3], cfg[5])
    out = []
    for i in range(3):
        out += [vp[i], (up[i] + g_eval(g, vp[(i - 1) % 3], vp[(i + 1) % 3])) % 2]
    return tuple(out)


CARRIER_CFGS = list(itertools.product((0, 1), repeat=4))   # (u0, v0, u1, v1), index = 8u0+4v0+2u1+v1


def f_z(w):
    return w[0]


def f_x(w):
    return w[1]


def f_y(w):
    return (w[0] + w[1] + w[2] + w[3]) % 2


FUNCTIONALS = {"x": f_x, "y": f_y, "z": f_z}


def law_from_pred(pred):
    sup = [w for w in CARRIER_CFGS if pred(w)]
    return [Fraction(1, len(sup)) if w in sup else Fraction(0) for w in CARRIER_CFGS]


def qa_family():
    """Q: Lambda_0 and Lambda_{a,b} (uniform on {f_a = b}), a in x, y, z; Lambda_{y,b} under NNB (supplied)."""
    q = [("L0", law_from_pred(lambda w: True))]
    for a in ("x", "y", "z"):
        for b in (0, 1):
            q.append(("L%s%d" % (a, b), law_from_pred(lambda w, a=a, b=b: FUNCTIONALS[a](w) == b)))
    return q


MED_SUPPLIES = [("u2=0", {(0, 0): Fraction(1, 2), (0, 1): Fraction(1, 2)}),
                ("u2=1", {(1, 0): Fraction(1, 2), (1, 1): Fraction(1, 2)}),
                ("v2=0", {(0, 0): Fraction(1, 2), (1, 0): Fraction(1, 2)}),
                ("v2=1", {(0, 1): Fraction(1, 2), (1, 1): Fraction(1, 2)}),
                ("source", {(a, b): Fraction(1, 4) for a in (0, 1) for b in (0, 1)})]
REGS = [None, ("u2", 0), ("u2", 1), ("v2", 0), ("v2", 1)]
ROUNDS = [(m, k, reg) for m in range(5) for k in range(1, 7) for reg in REGS]


def round_name(r):
    m, k, reg = r
    return "%s/k%d/%s" % (MED_SUPPLIES[m][0], k, "none" if reg is None else "%s=%d" % reg)


def apply_round(law, g, rnd, perms):
    """One round on a carrier law (list of 16 Fractions): attach the mediator, Phi_g^k, register and condition
    (forward, terminal), discard. Returns (law, herald) or (None, 0)."""
    m, k, reg = rnd
    med = MED_SUPPLIES[m][1]
    perm = perms[(g, k)]
    out = [Fraction(0)] * 16
    for c, pc in enumerate(law):
        if pc == 0:
            continue
        for (u2, v2), pm in med.items():
            j = perm[c * 4 + u2 * 2 + v2]
            mu2, mv2 = (j >> 1) & 1, j & 1
            if reg is not None and (mu2 if reg[0] == "u2" else mv2) != reg[1]:
                continue
            out[j >> 2] += pc * pm
    q = sum(out)
    if q == 0:
        return None, Fraction(0)
    return [q_div(x, q) for x in out], q


def detector_tables():
    """The native detectors as response tables P(S_a = 0 | carrier configuration), computed by simulating the
    meters under the native rule (L-HET): S_Z a ready meter (w, 0) armed to cell 0 for one tick, record its u;
    S_X the same after one free tick; S_Y the triangle round (mediator ready u_2 = 0, two XOR ticks, register u_2)."""
    tabs = {"x": [], "y": [], "z": []}
    for w in CARRIER_CFGS:
        st0 = {"c0": (w[0], w[1]), "c1": (w[2], w[3])}
        for name, free_first in (("z", False), ("x", True)):
            hits = Fraction(0)
            for mw in (0, 1):
                st = dict(st0)
                if free_first:
                    st = native_step(st, ordered_unique())
                st["m"] = (mw, 0)
                st = native_step(st, ordered_unique([ordered_key(("c0", "m"))]))
                hits += 1 if st["m"][0] == 0 else 0
            tabs[name].append(q_div(hits, 2))
        perm = phi_perm("XOR", 2)
        hits = Fraction(0)
        for v2 in (0, 1):
            j = perm[ring_idx(w + (0, v2))]
            hits += 1 if ((j >> 1) & 1) == 0 else 0
        tabs["y"].append(q_div(hits, 2))
    return tabs


def rho_of(law, tabs):
    return (Fraction(1),) + tuple(sum(p * t for p, t in zip(law, tabs[a])) for a in ("x", "y", "z"))


def r_direct(law):
    return tuple(sum(p * (1 if FUNCTIONALS[a](w) == 0 else -1) for p, w in zip(law, CARRIER_CFGS))
                 for a in ("x", "y", "z"))


def mat_inv(m):
    n = len(m)
    rows = [[Fraction(x) for x in m[i]] + [Fraction(1 if j == i else 0) for j in range(n)] for i in range(n)]
    red, piv = s_rref(rows, n)
    if len(piv) != n:
        return None
    return [r[n:] for r in red]


def matmul(a, b):
    return [[sum(Fraction(a[i][k]) * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def matvec(a, v):
    return tuple(sum(Fraction(a[i][k]) * v[k] for k in range(len(v))) for i in range(len(a)))


def calibration(rho0, rhos_a0):
    """L-CAL: the affine R_op on record vectors sending rho(Lambda_0) to 0 and rho(Lambda_{a,0}) to e_a."""
    basis = [list(rho0)] + [list(r) for r in rhos_a0]
    inv = mat_inv([list(col) for col in zip(*basis)])
    if inv is None:
        return None
    targets = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
    tmat = [list(col) for col in zip(*targets)]
    return matmul(tmat, inv)


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def charpoly3(a):
    """lambda^3 + c2 lambda^2 + c1 lambda + c0."""
    tr = a[0][0] + a[1][1] + a[2][2]
    m2 = sum(a[i][i] * a[j][j] - a[i][j] * a[j][i] for i, j in ((0, 1), (0, 2), (1, 2)))
    return [Fraction(1), -Fraction(tr), Fraction(m2), -Fraction(det3(a))]


def _divisors(n):
    n = abs(n)
    out, i = [], 1
    while i * i <= n:
        if n % i == 0:
            out += [i, n // i]
        i += 1
    return sorted(ordered_unique(out))


def rational_roots(coeffs):
    """All rational roots, with multiplicity, of a polynomial (coefficients high to low), and the cofactor."""
    roots = []
    poly = [Fraction(c) for c in coeffs]
    while len(poly) > 1:
        den = 1
        for c in poly:
            den = den * c.denominator // _gcd(den, c.denominator)
        ip = [int(c * den) for c in poly]
        if ip[-1] == 0:
            cand = [Fraction(0)]
        else:
            cand = [Fraction(s * p, q) for p in _divisors(ip[-1]) for q in _divisors(ip[0]) for s in (1, -1)]
        found = None
        for r in sorted(ordered_unique(cand)):
            val = Fraction(0)
            for c in poly:
                val = val * r + c
            if val == 0:
                found = r
                break
        if found is None:
            break
        roots.append(found)
        new = [poly[0]]
        for c in poly[1:-1]:
            new.append(c + new[-1] * found)
        poly = new
    return roots, poly


def unit_spectrum(beta):
    """The unit-modulus eigenvalues of beta with multiplicity, exactly: counts of +1 and -1, and the parameter b of
    an irreducible quadratic factor lambda^2 + b lambda + 1 with |b| < 2 (a complex unit pair), if any."""
    roots, rest = rational_roots(charpoly3(beta))
    plus = sum(1 for r in roots if r == 1)
    minus = sum(1 for r in roots if r == -1)
    pair = None
    if len(rest) == 3:
        lead = rest[0]
        b, c = q_div(rest[1], lead), q_div(rest[2], lead)
        if c == 1 and -2 < b < 2:
            pair = b
    return {"plus": plus, "minus": minus, "pair_b": pair}


def wcl_spectrum_fires(beta):
    """W-CL on one matrix: the unit-modulus multiset is not a sub-multiset of any 3x3 signed-permutation spectrum
    (cycle types 1+1+1, 2+1 ({1,-1} or {i,-i}), 3 ({1, w, w^2} or {-1, e^{+-i pi/3}}))."""
    u = unit_spectrum(beta)
    b = u["pair_b"]
    if b is None:
        return False
    if b == 0:
        return False
    if b == 1:
        return u["minus"] > 0
    if b == -1:
        return u["plus"] > 0
    return True


P_SWAP = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]


def mpow(m, k):
    out = [[Fraction(1 if i == j else 0) for j in range(3)] for i in range(3)]
    for _ in range(k):
        out = matmul(m, out)
    return out


def wcl(beta, k, p=P_SWAP):
    """W-CL on beta and on P^k beta; fires if either fires."""
    enc = matmul(mpow(p, k), beta)
    a, b = wcl_spectrum_fires(beta), wcl_spectrum_fires(enc)
    return {"fires": a or b, "fixed": a, "encoded": b, "spectrum_fixed": unit_spectrum(beta),
            "spectrum_encoded": unit_spectrum(enc), "det_fix": det3(beta), "det_enc": (-1) ** k * det3(beta)}


def orbit_stats(q_laws, step_fn, rho_fn, k_ticks, kmax=12, cal_laws=None, horizons=(6, 12)):
    """Orbits O_K = {pi^j Lambda : Lambda in Q, 0 <= j <= K}, with HC, CONS, VAL, W-CL, W-OCT for K in (6, 12).
    q_laws: [(label, law)]; step_fn(law, j) -> (law, herald) or (None, 0); rho_fn(law) -> record vector.
    cal_laws: the laws in the roles of Lambda_0 and Lambda_{a,0} (default: from Q's labels)."""
    lab = dict(q_laws)
    cal = cal_laws or {"0": lab["L0"], "x": lab["Lx0"], "y": lab["Ly0"], "z": lab["Lz0"]}
    rop = calibration(rho_fn(cal["0"]), [rho_fn(cal[a]) for a in ("x", "y", "z")])
    cons_check = None
    if cal_laws is None:
        cons_check = all(tuple(rho_fn(lab["L%s0" % a])[i] + rho_fn(lab["L%s1" % a])[i] for i in range(4))
                         == tuple(2 * x for x in rho_fn(lab["L0"])) for a in ("x", "y", "z"))

    def rcal(law):
        return matvec(rop, rho_fn(law))

    orbits, heralds = {}, {}
    for name, law in q_laws:
        seq, hs = [law], []
        cur = law
        for j in range(kmax):
            nxt, h = step_fn(cur, j)
            hs.append(h)
            if nxt is None:
                break
            seq.append(nxt)
            cur = nxt
        orbits[name], heralds[name] = seq, hs
    alpha = None
    beta = None
    first = {}
    for key in ("0", "x", "y", "z"):
        nxt, h = step_fn(cal[key], 0)
        first[key] = nxt
    if all(first[k] is not None for k in first):
        alpha = rcal(first["0"])
        cols = [tuple(rcal(first[a])[i] - alpha[i] for i in range(3)) for a in ("x", "y", "z")]
        beta = [[cols[j][i] for j in range(3)] for i in range(3)]
    res = {"HC": {}, "CONS": {}, "VAL": {}, "WOCT": {}, "counts": {}, "STAB": {}, "span_rank": {}}
    for kk in horizons:
        # STAB(K) = [rank span O_{K-1} = rank span O_K] (r12 hook; reported, read by no decide-*)
        prev = [l for name in orbits for l in orbits[name][:kk]]
        full = [l for name in orbits for l in orbits[name][:kk + 1]]
        rp, rf = s_rank(prev), s_rank(full)
        res["span_rank"][str(kk)] = {"O_K-1": rp, "O_K": rf}
        res["STAB"][str(kk)] = rp == rf
        hs = [h for name in heralds for h in heralds[name][:kk]]
        complete = all(len(heralds[name]) >= kk and len(orbits[name]) > kk for name in heralds)
        res["HC"][str(kk)] = complete and len(ordered_unique(hs)) == 1 and hs[0] > 0
        laws_k = [l for name in orbits for l in orbits[name][:kk + 1]]
        rs = [rcal(l) for l in laws_k]
        res["VAL"][str(kk)] = all(sum(x * x for x in r) <= 1 for r in rs)
        res["WOCT"][str(kk)] = any(sum(abs(x) for x in r) > 1 for r in rs)
        res["counts"][str(kk)] = {"laws": len(laws_k),
                                  "inside_ball_outside_octahedron": sum(1 for r in rs if sum(x * x for x in r) <= 1
                                                                        and sum(abs(x) for x in r) > 1)}
        if beta is None or not complete:
            res["CONS"][str(kk)] = False
        else:
            ok = True
            for name in orbits:
                for j in range(kk):
                    pred = tuple(alpha[i] + sum(beta[i][c] * rcal(orbits[name][j])[c] for c in range(3))
                                 for i in range(3))
                    if pred != rcal(orbits[name][j + 1]):
                        ok = False
            res["CONS"][str(kk)] = ok
    res["alpha"] = alpha
    res["beta"] = beta
    res["WCL"] = wcl(beta, k_ticks) if beta is not None else {"fires": False}
    res["calibration_consistency"] = cons_check
    res["horizon_requested"] = kmax
    res["complete_enumeration"] = True
    res["orbits"] = orbits
    res["rop"] = rop
    return res


def canonical_law_for(r):
    """A carrier law with R = r (|r_a| <= 1): independent (f_z, f_x, f_y) bits, realized as u0 = f_z, v0 = f_x,
    u1 = f_y + f_z + f_x, v1 = 0. Used only by supplied-operation fixtures."""
    rx, ry, rz = r
    out = [Fraction(0)] * 16
    for a in (0, 1):
        for b in (0, 1):
            for c in (0, 1):
                p = (q_div(1 + rz, 2) if a == 0 else q_div(1 - rz, 2)) * \
                    (q_div(1 + rx, 2) if b == 0 else q_div(1 - rx, 2)) * \
                    (q_div(1 + ry, 2) if c == 0 else q_div(1 - ry, 2))
                w = (a, b, (a + b + c) % 2, 0)
                out[CARRIER_CFGS.index(w)] += p
    return out


def supplied_op(betas, alpha=(0, 0, 0)):
    """A supplied operation acting on R: the j-th application uses betas[j % len(betas)]."""
    def step(law, j):
        r = r_direct(law)
        b = betas[j % len(betas)]
        nr = tuple(Fraction(alpha[i]) + sum(Fraction(b[i][c]) * r[c] for c in range(3)) for i in range(3))
        return canonical_law_for(nr), Fraction(1)
    return step


def _fm(rows):
    return [[Fraction(x) for x in r] for r in rows]


R60 = _fm([[Fraction(2, 3), Fraction(-1, 3), Fraction(2, 3)], [Fraction(2, 3), Fraction(2, 3), Fraction(-1, 3)],
           [Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)]])
CL_H = _fm([[0, 0, 1], [0, -1, 0], [1, 0, 0]])            # Hadamard on (x, y, z)
CL_S = _fm([[0, -1, 0], [1, 0, 0], [0, 0, 1]])            # phase gate
ROT35 = _fm([[Fraction(3, 5), Fraction(-4, 5), 0], [Fraction(4, 5), Fraction(3, 5), 0], [0, 0, 1]])
CYC = _fm([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
REFL111 = _fm([[1 - Fraction(2, 3) if i == j else -Fraction(2, 3) for j in range(3)] for i in range(3)])
S3_ROTOREFL = matmul(CYC, REFL111)


def signed_perms():
    out = []
    for p in itertools.permutations(range(3)):
        for s in itertools.product((1, -1), repeat=3):
            out.append([[Fraction(s[i]) if j == p[i] else Fraction(0) for j in range(3)] for i in range(3)])
    return out


def c_fixture_run(name, betas, k_ticks=0, alpha=(0, 0, 0)):
    tabs = detector_tables()
    q = qa_family()
    st = orbit_stats(q, supplied_op(betas, alpha), lambda l: rho_of(l, tabs), k_ticks)
    return st


def planted_laws():
    """PC-PLANT (REACHABLE §3.3 S4): six laws on disjoint two-point supports with images +-e_a, their mixture,
    and a stochastic B_P on their supports sending them to images +-beta0 e_a (beta0 = R60)."""
    trip = {"+x": [(0, 0, 0), (0, 1, 1)], "-x": [(1, 0, 1), (1, 1, 0)], "+y": [(0, 0, 1), (1, 0, 0)],
            "-y": [(0, 1, 0), (1, 1, 1)], "+z": [(0, 0, 0), (1, 1, 0)], "-z": [(0, 1, 1), (1, 0, 1)]}

    def pts(t):   # (f_x, f_y, f_z) -> the two carrier configurations with these values
        fx_, fy_, fz_ = t
        return [w for w in CARRIER_CFGS if f_x(w) == fx_ and f_y(w) == fy_ and f_z(w) == fz_]

    used, supp = ordered_unique(), {}
    for key in ("+x", "-x", "+y", "-y", "+z", "-z"):
        pair = []
        for t in trip[key]:
            w = [w for w in pts(t) if w not in used][0]
            used[w] = None
            pair.append(w)
        supp[key] = pair
    laws = {}
    for key, pair in supp.items():
        laws[key] = [Fraction(1, 2) if w in pair else Fraction(0) for w in CARRIER_CFGS]
    mix = [sum(laws[k][i] for k in laws) * Fraction(1, 6) for i in range(16)]
    vert = {}
    for key, pair in supp.items():
        for w in pair:
            vert.setdefault((f_x(w), f_y(w), f_z(w)), w)

    def law_at(r):
        out = [Fraction(0)] * 16
        for (bx, by, bz), w in vert.items():
            p = Fraction(1)
            for bit, ra in ((bx, r[0]), (by, r[1]), (bz, r[2])):
                p *= q_div(1 + ra, 2) if bit == 0 else q_div(1 - ra, 2)
            out[CARRIER_CFGS.index(w)] += p
        return out

    img = {}
    for key in supp:
        sgn = 1 if key[0] == "+" else -1
        e = {"x": (1, 0, 0), "y": (0, 1, 0), "z": (0, 0, 1)}[key[1]]
        img[key] = law_at(matvec(R60, tuple(sgn * x for x in e)))
    bp = {}
    for key, pair in supp.items():
        for w in pair:
            bp[CARRIER_CFGS.index(w)] = img[key]

    def step(law, j):
        out = [Fraction(0)] * 16
        for i, p in enumerate(law):
            if p == 0:
                continue
            row = bp.get(i)
            if row is None:
                out[i] += p
            else:
                out = [o + p * x for o, x in zip(out, row)]
        return out, Fraction(1)

    return laws, mix, step


def ne1_carrier(law):
    """NE-1 on a carrier law: a QA family law (Lambda_{y,b} conditional on NNB), or a product of per-cell laws each
    a P2 ready cell (one known slot, value 0 or 1, other uniform) or a uniform source cell."""
    for _, ql in qa_family():
        if list(law) == list(ql):
            return True
    m0, m1 = {}, {}
    for p, w in zip(law, CARRIER_CFGS):
        m0[(w[0], w[1])] = m0.get((w[0], w[1]), Fraction(0)) + p
        m1[(w[2], w[3])] = m1.get((w[2], w[3]), Fraction(0)) + p
    for p, w in zip(law, CARRIER_CFGS):
        if p != m0[(w[0], w[1])] * m1[(w[2], w[3])]:
            return False
    return ne1_cell(m0) and ne1_cell(m1)


def ne1_cell(m):
    vals = {(a, b): Fraction(m.get((a, b), 0)) for a in (0, 1) for b in (0, 1)}
    if all(v == Fraction(1, 4) for v in vals.values()):
        return True
    for slot in (0, 1):
        for b in (0, 1):
            want = {k: (Fraction(1, 2) if k[slot] == b else Fraction(0)) for k in vals}
            if vals == want:
                return True
    return False


def c_fixture_controls():
    """Fixture-mode C controls: C-STAB, C-R60, C-R60-ODD, C-35, C-S3, C-PLANT, C-CONSX, C-DET, C-STEP, REP-FRAME."""
    out = {}
    hs = matmul(CL_H, CL_S)
    stab = [c_fixture_run("C-STAB", [m]) for m in (CL_H, CL_S, hs)]
    out["C-STAB"] = {"green": all(not s["WCL"]["fires"] and not s["WOCT"]["12"] and s["CONS"]["12"] for s in stab)}
    r = c_fixture_run("C-R60", [R60])
    sp = r["WCL"]["spectrum_fixed"]
    out["C-R60"] = {"green": r["WCL"]["fires"] and sp["plus"] == 1 and sp["pair_b"] == -1 and r["VAL"]["12"]
                    and r["CONS"]["12"]}
    odd = matmul(P_SWAP, R60)
    r = c_fixture_run("C-R60-ODD", [odd], k_ticks=1)
    out["C-R60-ODD"] = {"green": r["WCL"]["fires"] and not r["WCL"]["fixed"] and r["WCL"]["encoded"]}
    r = c_fixture_run("C-35", [ROT35])
    out["C-35"] = {"green": r["WCL"]["fires"] and r["VAL"]["12"] and r["CONS"]["12"],
                   "pair_b": r["WCL"]["spectrum_fixed"]["pair_b"]}
    r = c_fixture_run("C-S3", [S3_ROTOREFL])
    sp = r["WCL"]["spectrum_fixed"]
    out["C-S3"] = {"green": r["WCL"]["fires"] and sp["minus"] == 1 and sp["pair_b"] == 1}
    laws, mix, step = planted_laws()
    tabs = detector_tables()
    cal = {"0": mix, "x": laws["+x"], "y": laws["+y"], "z": laws["+z"]}
    src = [("L0", mix)] + [("P" + k, v) for k, v in laws.items()]
    r = orbit_stats(src, step, lambda l: rho_of(l, tabs), 0, kmax=1, cal_laws=cal)
    out["C-PLANT"] = {"green": r["WCL"]["fires"] and r["beta"] == R60
                      and not any(ne1_carrier(l) for l in laws.values())}
    r = c_fixture_run("C-CONSX", [CL_H, CL_S])
    out["C-CONSX"] = {"green": r["CONS"]["12"] is False}
    ok = True
    for w in CARRIER_CFGS:
        pl = [Fraction(1) if v == w else Fraction(0) for v in CARRIER_CFGS]
        ok = ok and all(rho_of(pl, tabs)[1 + i] == (1 if FUNCTIONALS[a](w) == 0 else 0)
                        for i, a in enumerate(("x", "y", "z")))
    for _, ql in qa_family():
        ok = ok and all(rho_of(ql, tabs)[1 + i] == q_div(1 + r_direct(ql)[i], 2) for i in range(3))
    out["C-DET"] = {"green": ok}
    out["C-STEP"] = c_step_control()
    fixture_perms = {(g, k): phi_perm(g, k) for g in ("0", "XOR") for k in range(7)}
    out["C-AFFB-fixture"] = c_affb_fixture(fixture_perms)
    miss = 0
    for s in signed_perms():
        sinv = [list(col) for col in zip(*s)]
        b2 = matmul(matmul(s, odd), sinv)
        p2 = matmul(matmul(s, P_SWAP), sinv)
        if not wcl(b2, 1, p2)["fires"]:
            miss += 1
    out["REP-FRAME"] = {"green": miss == 0, "lost": miss, "of": 48}
    return out


def c_step_control(mutate_inverse=False):
    """C-STEP: every Phi_g against an independently written inverse; g symmetric; reads neighbours only;
    affine classification by algebraic normal form; XOR's matrix symplectic. mutate_inverse: the transport
    mutation (Phi_g^{-1} in place of Phi_g) must turn it red."""
    ok = True
    for g in RULES:
        for i in range(64):
            c = ring_cfg(i)
            img = phi_g_cfg(g, c)
            if mutate_inverse:
                img = inverse_phi_cfg(g, c)
            if inverse_phi_cfg(g, img) != c:
                ok = False
        if any(g_eval(g, a, b) != g_eval(g, b, a) for a in (0, 1) for b in (0, 1)):
            ok = False
        t = RULES[g]
        anf_and = (t[0] + t[1] + t[1] + t[2]) % 2          # coefficient of a*b in the algebraic normal form
        if (anf_and == 0) != (g in AFFINE_RULES):
            ok = False
    xor_lin = []
    for i in range(6):
        e = [0] * 6
        e[i] = 1
        img = phi_g_cfg("XOR", tuple(e))
        xor_lin.append(img)
    jmat = [[1 if (r // 2 == c // 2 and r != c) else 0 for c in range(6)] for r in range(6)]
    m = [[xor_lin[c][r] for c in range(6)] for r in range(6)]
    mt = [list(col) for col in zip(*m)]
    prod = [[sum(mt[i][k] * sum(jmat[k][l] * m[l][j] for l in range(6)) for k in range(6)) % 2 for j in range(6)]
            for i in range(6)]
    if prod != jmat:
        ok = False
    return {"green": ok}


def rc2_classes():
    """L-UPRIME's alternatives: affine carrier bijections A of F_2^4 with f_a o A in {f_b, f_b + 1} for a
    permutation of (x, y, z) (r5's reviewer control RC2: 768 maps, 48 induced signed permutations). For each
    class, the first symplectic representative in the frozen enumeration order, else the first."""
    duals = {"x": (0, 1, 0, 0), "y": (1, 1, 1, 1), "z": (1, 0, 0, 0)}
    cols = list(itertools.product((0, 1), repeat=4))
    classes = {}

    def apply_l(l, t, w):
        return tuple((sum(l[i][j] * w[j] for j in range(4)) + t[i]) % 2 for i in range(4))

    def symplectic(l):
        jm = [[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]]
        lt = [list(c) for c in zip(*l)]
        prod = [[sum(lt[i][k] * sum(jm[k][q] * l[q][j] for q in range(4)) for k in range(4)) % 2
                 for j in range(4)] for i in range(4)]
        return prod == jm

    count = 0
    for c0 in cols:
        for c1 in cols:
            for c2 in cols:
                for c3 in cols:
                    l = [[c0[i], c1[i], c2[i], c3[i]] for i in range(4)]
                    if s_rank([[Fraction(x) for x in r] for r in l]) < 4:
                        continue
                    # induced map on the three functionals (linear part)
                    perm = {}
                    for a, da in duals.items():
                        img = tuple(sum(da[i] * l[i][j] for i in range(4)) % 2 for j in range(4))
                        match = [b for b, db in duals.items() if db == img]
                        if not match:
                            break
                        perm[a] = match[0]
                    if len(perm) != 3 or len(ordered_unique(perm.values())) != 3:
                        continue
                    for t in cols:
                        count += 1
                        signs = tuple(sum(duals[a][i] * t[i] for i in range(4)) % 2 for a in ("x", "y", "z"))
                        key = (tuple(perm[a] for a in ("x", "y", "z")), signs)
                        cur = classes.get(key)
                        cand = (l, t, symplectic(l))
                        if cur is None or (cand[2] and not cur[2]):
                            classes[key] = cand
    return classes, count


def bc_fragment(name, laws):
    st = [("S_Z", lambda w: w[0]), ("S_X", lambda w: w[1]), ("S_Y", lambda w: (w[0] + w[1] + w[2] + w[3]) % 2)]
    dl = [{tuple(w): p for p, w in zip(l, CARRIER_CFGS) if p} for l in laws]
    return frag_from_laws(name, dl, (0, 1, 2, 3), st, acc=["S_Z", "S_X", "S_Y"])


def bc_fragment_decide(inst, budget_vals):
    """B-C for one flagged instance: preparations its largest flagged O_K orbit laws (distinct), measurements S_Z, S_X, S_Y;
    the completion "every slot of every cell, registered jointly" (the four carrier slots); UPR-BC's inputs."""
    laws = []
    for l in inst["orbit_laws"]:
        if l not in laws:
            laws.append(l)
    fr = bc_fragment("B-C:" + inst["id"], laws)
    rec = s_decide(fr, budget_vals)
    rec.update({"orbit_horizon": inst["orbit_horizon"], "role": "B-C", "lp_reads_equal_acc": sorted(fr["lp_settings"]) == sorted(fr["acc"]),
                "acc_typing": "imported (L-UPRIME)", "TOMO": rec["tomo"]})
    rec["restored_by_full"] = None
    if rec["lp"] == "infeasible":
        st = [("S_Z", lambda w: w[0]), ("S_X", lambda w: w[1]),
              ("S_Y", lambda w: (w[0] + w[1] + w[2] + w[3]) % 2), ("J", lambda w: tuple(w))]
        dl = [{tuple(w): p for p, w in zip(l, CARRIER_CFGS) if p} for l in laws]
        cf = frag_from_laws("B-C+all-joint:" + inst["id"], dl, (0, 1, 2, 3), st)
        cr = s_decide(cf, budget_vals)
        rec["restored_by_full"] = cr["lp"] == "feasible" and cr["verified"]
        rec["completion_record"] = strip_bytes(cr)
        rec["restored_by_full"] = (cr["lp"] == "feasible") if cr["verified"] and cr["lp"] in ("feasible", "infeasible") else None
    return rec


def s_build_c():
    """Decisive family: C's test-rule orbits, the affine and idle ablations (ABL), C-A, the decisive-mode C
    controls (CC-NAT, CC-DYAD, C-XB, C-AFFB, C-FRAME, C-SCOPE, C-EMB) and r5's diagnostics (D1(a))."""
    s_refusal()
    tabs = detector_tables()
    q = qa_family()
    perms = {(g, k): phi_perm(g, k) for g in RULES for k in range(0, 7)}
    rho = lambda l: rho_of(l, tabs)
    cache = {}

    def stats(g, rnd):
        key = (g, rnd)
        if key not in cache:
            st = orbit_stats(q, lambda law, j: apply_round(law, g, rnd, perms), rho, rnd[1])
            cache[key] = st
        return cache[key]

    def zero_tick(rnd):
        return ("0", (rnd[0], 0, rnd[2]))

    instances, emb = [], c_emb_static(q)
    for g in TEST_RULES:
        for rnd in ROUNDS:
            st = stats(g, rnd)
            abl_ok = True
            for g2 in AFFINE_RULES:
                s2 = stats(g2, rnd)
                if (s2["WCL"]["fires"] and s2["CONS"]["12"] and s2["HC"]["12"]) or s2["WOCT"]["12"]:
                    abl_ok = False
            zg, zr = zero_tick(rnd)
            sz = stats(zg, zr)
            if (sz["WCL"]["fires"] and sz["CONS"]["12"] and sz["HC"]["12"]) or sz["WOCT"]["12"]:
                abl_ok = False
            instances.append({"id": g + ":" + round_name(rnd), "g": g, "round": round_name(rnd), "HC": st["HC"],
                              "CONS": st["CONS"], "VAL": st["VAL"], "WOCT": st["WOCT"], "WCL": st["WCL"]["fires"],
                              "WCL_detail": {k: v for k, v in st["WCL"].items() if k != "fires"},
                              "STAB": st["STAB"], "span_rank": st["span_rank"],
                              "alpha": st["alpha"], "beta": st["beta"], "ABL": abl_ok, "EMB": emb["holds"],
                              "counts": st["counts"], "_rnd": rnd})
    flagged = []
    for i in instances:
        c12 = all(i[f]["12"] for f in ("HC", "CONS", "VAL")) and i["WCL"] and i["ABL"] and i["EMB"]
        c6 = all(i[f]["6"] for f in ("HC", "CONS", "VAL")) and i["WCL"] and i["ABL"] and i["EMB"]
        cn = i["HC"]["12"] and i["VAL"]["12"] and i["WOCT"]["12"] and i["ABL"] and i["EMB"]
        if c12 or c6 or cn:
            g, rnd = i["g"], i["_rnd"]
            ca = stats(g, (rnd[0], rnd[1], None))
            i["C-A"] = {"CONS": ca["CONS"], "WCL": ca["WCL"]["fires"], "WOCT": ca["WOCT"], "HC": ca["HC"]}
            st = stats(g, rnd)
            i["orbit_horizon"] = 12 if c12 or cn else 6
            i["orbit_laws"] = [l for name in st["orbits"] for l in st["orbits"][name][:i["orbit_horizon"]+1]]
            flagged.append(i)
    ccnat = {"green": not any((stats(g, r)["WCL"]["fires"] and stats(g, r)["CONS"]["12"]) or stats(g, r)["WOCT"]["12"]
                              for g in AFFINE_RULES for r in ROUNDS)}
    controls = {"CC-NAT": ccnat, "C-EMB": emb}
    diagnostic_controls = c_r5_controls(perms, tabs)
    controls.update({name: control for name, control in diagnostic_controls.items() if name == "C-AFFB"})
    for g in RULES:
        for rnd in ROUNDS:
            stats(g, rnd)
    controls.update(c_orbit_controls(cache, perms, tabs))
    controls["diagnostic-controls-depth-1"] = {"green": all(record["green"] for record in diagnostic_controls.values()),
                                               "reported_only": True, "records": diagnostic_controls}
    diagnostics = r5_diagnostics(perms, tabs)
    controls["C-SCOPE"] = {"green": len(q) == 7 and len(MED_SUPPLIES) == 5 and len(ROUNDS) == 150
                           and len(instances) == 4*150 and len(cache) == 8*150
                           and all(record["horizon_requested"] == 12 and record["complete_enumeration"] for record in cache.values())
                           and len(s0_laws()) == 23 and all(record["depth"] == 1 for record in diagnostics.values()),
                           "complete": True, "diagnostic_depth": 1}
    for i in instances:
        i.pop("_rnd", None)
    return {"instances": instances, "flagged": flagged, "controls": controls,
            "diagnostics_r5": diagnostics, "cache": cache}


def c_emb_static(q):
    """C-EMB (d) and (b): NE-1 on every supply (Q and M), NE-2/NE-4/NE-5 by the round schema."""
    planted_negative = all(not ne1_carrier(law) for law in diagnostic_planted_laws())
    supplies_ok = all(ne1_carrier(l) for _, l in q) and all(
        ne1_cell(m) for _, m in MED_SUPPLIES)
    schema_ok = all(reg is None or (reg[0] in ("u2", "v2") and reg[1] in (0, 1)) for _, _, reg in ROUNDS)
    enum_sha = h_sha256(canonical([round_name(r) for r in ROUNDS]).encode())
    laws, mix, _ = planted_laws()
    planted_fail = not any(ne1_carrier(l) for l in laws.values())
    return {"holds": supplies_ok and schema_ok and planted_negative and planted_fail,
            "green": supplies_ok and schema_ok and planted_negative and planted_fail,
            "enumeration_sha256": enum_sha, "planted_fail_NE1": planted_fail}


# r5's diagnostics (D1(a); labelled, read by no token) and r5's controls carried in Appendix B
def p2_products():
    out = []
    for s0 in (0, 1):
        for b0 in (0, 1):
            for s1 in (0, 1):
                for b1 in (0, 1):
                    out.append(law_from_pred(lambda w, s0=s0, b0=b0, s1=s1, b1=b1:
                                             w[s0] == b0 and w[2 + s1] == b1))
    return out


def s0_laws():
    return [l for _, l in qa_family()] + p2_products()


def l_scope(g, perms, rounds=ROUNDS, base=None):
    seen, out = ordered_unique(), []
    for l in (base or s0_laws()):
        t = tuple(l)
        if t not in seen:
            seen[t] = None
            out.append(l)
    level = list(out)
    for _ in range(1):
        nxt = []
        for l in level:
            for rnd in rounds:
                o, h = apply_round(l, g, rnd, perms)
                if o is not None and tuple(o) not in seen:
                    seen[tuple(o)] = None
                    out.append(o)
                    nxt.append(o)
        level = nxt
    return out


def affine_basis(laws):
    """The first laws in order spanning aff(laws), containing the first (Lambda_0 and Lambda_{a,0} lead S_0)."""
    rows, idx = [], []
    for i, l in enumerate(laws):
        cand = rows + [list(l)]
        if s_rank(cand) > len(rows):
            rows.append(list(l))
            idx.append(i)
        if len(rows) == 16:
            break
    return idx


def induced_map(g, rnd, laws, perms, basis_only=True):
    record = diagnostic_fit(laws, lambda law: apply_round(law, g, rnd, perms), basis_only)
    return record["fit"] if record["herald_constant"] else None


def diagnostic_fit(laws, step, basis_only=False):
    """Frozen diagnostic affine fit, with herald constancy reported separately from the identity."""
    selected = affine_basis(laws) if basis_only else list(range(len(laws)))
    outputs = [step(law) for law in laws]
    if any(result[0] is None or result[1] <= 0 for result in outputs):
        return {"herald_constant": False, "fit": None}
    herald_constant = len(ordered_unique(outputs[i][1] for i in selected)) == 1
    q = dict(qa_family())
    zero, hz = step(q["L0"])
    alpha = r_direct(zero)
    columns = []
    for axis in ("x", "y", "z"):
        image, herald = step(q["L"+axis+"0"])
        if image is None:
            return {"herald_constant": herald_constant, "fit": None}
        columns.append(tuple(r_direct(image)[i]-alpha[i] for i in range(3)))
    beta = [[columns[j][i] for j in range(3)] for i in range(3)]
    fit = all(r_direct(outputs[index][0]) == tuple(alpha[i]+sum(beta[i][j]*r_direct(laws[index])[j] for j in range(3))
                                                  for i in range(3)) for index in selected)
    return {"herald_constant": herald_constant, "fit": (alpha, beta) if fit else None}


def diagnostic_branch(law):
    """Reported finite support/coset/isotropy predicates, under the frozen four-slot symplectic pairing."""
    support = [i for i, value in enumerate(law) if value > 0]
    if not support:
        return {"nonaffine": True, "nonisotropic": False, "sharp": False}
    translated = [i ^ support[0] for i in support]
    uniform = all(law[i] == Fraction(1, len(support)) for i in support)
    affine = uniform and all((a ^ b) in translated for a in translated for b in translated)
    determined = []
    for mask in range(16):
        values = [sum(((mask >> j) & 1)*((i >> j) & 1) for j in range(4)) % 2 for i in support]
        if len(ordered_unique(values)) == 1:
            determined.append(tuple((mask >> (3-j)) & 1 for j in range(4)))
    nonisotropic = affine and any((a[0]*b[1]+a[1]*b[0]+a[2]*b[3]+a[3]*b[2]) % 2 != 0
                                  for a in determined for b in determined)
    coordinates = r_direct(law)
    return {"nonaffine": not affine, "nonisotropic": nonisotropic,
            "sharp": abs(coordinates[0]) == 1 and abs(coordinates[2]) == 1}


def diagnostic_planted_laws():
    biased = [((Fraction(4, 5) if w[0] == 0 else Fraction(1, 5))
               *(Fraction(4, 5) if w[1] == 0 else Fraction(1, 5))*Fraction(1, 4)) for w in CARRIER_CFGS]
    invalid = law_from_pred(lambda w: w[1] == 0 and f_y(w) == 0)
    return [biased, invalid]


def c_affb_fixture(perms):
    planted, mixed, operation = planted_laws()
    point_laws = [[Fraction(1 if i == j else 0) for i in range(16)] for j in range(16)]
    laws = list(s0_laws())+list(planted.values())+[mixed]+diagnostic_planted_laws()+point_laws
    good = len(laws) == 48 and len(affine_basis(laws)) == 16
    for g in ("0", "XOR"):
        for rnd in [round_ for round_ in ROUNDS if round_[1] == 1]:
            step = lambda law, g=g, rnd=rnd: apply_round(law, g, rnd, perms)
            left, right = diagnostic_fit(laws, step, True), diagnostic_fit(laws, step, False)
            good = good and left["herald_constant"] == right["herald_constant"]
            if left["herald_constant"]:
                good = good and left["fit"] == right["fit"]
    good = good and diagnostic_fit(laws, lambda law: operation(law, 0), True) == diagnostic_fit(laws, lambda law: operation(law, 0), False)
    return {"green": good, "laws": len(laws), "basis_size": len(affine_basis(laws))}


def r5_diagnostics(perms, tabs):
    output = {}
    for g in RULES:
        laws = l_scope(g, perms)
        coordinates = [r_direct(law) for law in laws]
        outside = sum(1 for r in coordinates if sum(value*value for value in r) > 1)
        nonstab = sum(1 for r in coordinates if sum(value*value for value in r) <= 1 and sum(abs(value) for value in r) > 1)
        parity_zero = list(s0_laws())
        branches = {"nonaffine_branches": 0, "nonisotropic_branches": 0, "sharp_branches": 0}
        for law in s0_laws():
            for rnd in ROUNDS:
                image, herald = apply_round(law, g, rnd, perms)
                if image is not None:
                    if rnd[1] % 2 == 0 and image not in parity_zero:
                        parity_zero.append(image)
                    if rnd[2] is not None:
                        flags = diagnostic_branch(image)
                        for field, key in (("nonaffine_branches", "nonaffine"), ("nonisotropic_branches", "nonisotropic"), ("sharp_branches", "sharp")):
                            branches[field] += 1 if flags[key] else 0
        induced, parity_records, all_rounds, nonconstant = [], [], [], []
        for rnd in ROUNDS:
            record = diagnostic_fit(laws, lambda law, rnd=rnd: apply_round(law, g, rnd, perms))
            fitted = record["fit"]
            details = {"round": round_name(rnd), "herald_constant": record["herald_constant"], "fit": fitted is not None}
            if fitted is not None:
                alpha, beta = fitted
                orthogonal = matmul([list(row) for row in zip(*beta)], beta) == _fm([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
                octahedral = all(sorted(abs(value) for value in row) == [0, 0, 1] for row in beta) and orthogonal
                unitary = alpha == (0, 0, 0) and orthogonal and (-1)**rnd[1]*det3(beta) == 1
                details.update({"alpha": alpha, "beta": beta, "orthogonal": orthogonal, "alpha_zero": alpha == (0, 0, 0),
                                "det_fix": det3(beta), "det_enc": (-1)**rnd[1]*det3(beta), "octahedral": octahedral, "unitary": unitary})
                if record["herald_constant"]:
                    induced.append(dict(details))
                elif unitary and not octahedral:
                    nonconstant.append(round_name(rnd))
            all_rounds.append(details)
            parity_fit = induced_map(g, rnd, parity_zero, perms)
            if parity_fit is not None and not (record["herald_constant"] and fitted is not None):
                parity_records.append({"round": round_name(rnd), "alpha": parity_fit[0], "beta": parity_fit[1]})
        candidate = any(record["unitary"] and not record["octahedral"] for record in induced)
        category = "INVALID" if outside else "CANDIDATE" if candidate and c_emb_static(qa_family())["holds"] else "NONSTAB" if nonstab else "STAB"
        output[g] = {"affine": g in AFFINE_RULES, "L_scope_size": len(laws), "outside_ball": outside,
                     "nonstab_valid": nonstab, "offaxis_unit": sum(1 for r in coordinates if sum(value*value for value in r) == 1
                                                                      and sorted(abs(value) for value in r) != [0, 0, 1]),
                     "category": category, "induced": induced, "rounds": all_rounds, "induced_parity0": parity_records,
                     "herald_failure_non_octahedral_fit": nonconstant, **branches,
                     "label": "diagnostic (D1(a)), depth 1; no token reads it", "depth": 1}
    return output


def c_orbit_controls(cache, perms, tabs):
    """D.6 orbit versions of the named controls, in addition to labelled depth-one diagnostics."""
    mismatches, dyadic, frame, cases = 0, True, True, 0
    for g in RULES:
        for rnd in ROUNDS:
            stats = cache[(g, rnd)]
            for sequence in stats["orbits"].values():
                for law in sequence[:12]:
                    actual, herald = apply_round(law, g, rnd, perms)
                    direct = cxb_direct(law, g, rnd)
                    cases += 1
                    if (actual is None) != (direct is None) or (actual is not None and actual != direct):
                        mismatches += 1
                if rnd[2] is None:
                    for law in sequence[:13]:
                        coordinates = r_direct(law)
                        for value in coordinates:
                            denominator = Fraction(value).denominator
                            if denominator & (denominator-1):
                                dyadic = False
                        if sum(value*value for value in coordinates) == 1 and sorted(abs(value) for value in coordinates) != [0, 0, 1]:
                            dyadic = False
            beta, alpha = stats["beta"], stats["alpha"]
            if rnd[2] is None and stats["HC"]["12"] and stats["CONS"]["12"] and beta is not None and alpha == (0, 0, 0):
                transpose = [list(row) for row in zip(*beta)]
                if matmul(transpose, beta) == _fm([[1, 0, 0], [0, 1, 0], [0, 0, 1]]):
                    dyadic = dyadic and all(sorted(abs(value) for value in row) == [0, 0, 1] for row in beta)
            if g == "0" and rnd[1] == 1 and stats["HC"]["12"] and beta is not None:
                frame = frame and stats["CONS"]["12"]
                frame = frame and alpha == (0, 0, 0) and beta == _fm(P_SWAP) and det3(beta) == -1
                frame = frame and matmul(P_SWAP, beta) == _fm([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    return {"C-XB": {"green": mismatches == 0, "mismatches": mismatches, "cases": cases, "scope": "O_12"},
            "CC-DYAD": {"green": dyadic, "scope": "non-register O_12"},
            "C-FRAME": {"green": frame, "scope": "zero-rule k=1 orbits"}}



def c_r5_controls(perms, tabs):
    """Appendix B's controls (C-XB, C-FRAME, CC-DYAD, C-AFFB); C-STEP and C-SCOPE are elsewhere."""
    out = {}
    mism = 0
    s0 = s0_laws()
    for g in RULES:
        for l in s0:
            for rnd in ROUNDS:
                o, h = apply_round(l, g, rnd, perms)
                o2 = cxb_direct(l, g, rnd)
                if (o is None) != (o2 is None) or (o is not None and o != o2):
                    mism += 1
    out["C-XB"] = {"green": mism == 0, "mismatches": mism, "cases": 8 * len(s0) * len(ROUNDS)}
    laws0 = l_scope("0", perms)
    ok = True
    for rnd in [r for r in ROUNDS if r[1] == 1]:
        im = induced_map("0", rnd, laws0, perms)
        if im is None:
            continue
        alpha, beta = im
        enc = matmul(P_SWAP, beta)
        ok = ok and alpha == (0, 0, 0) and beta == _fm(P_SWAP) and det3(beta) == -1 and enc == _fm(
            [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    out["C-FRAME"] = {"green": ok}
    nonereg = [r for r in ROUNDS if r[2] is None]
    dy = True
    for g in RULES:
        laws = l_scope(g, perms, rounds=nonereg)
        for l in laws:
            for x in r_direct(l):
                d = Fraction(x).denominator
                if d & (d - 1):
                    dy = False
            r = r_direct(l)
            if sum(x * x for x in r) == 1 and sorted(abs(x) for x in r) != [0, 0, 1]:
                dy = False
        for rnd in nonereg:
            im = induced_map(g, rnd, laws, perms)
            if im is not None:
                alpha, beta = im
                bt = [list(c) for c in zip(*beta)]
                if alpha == (0, 0, 0) and matmul(bt, beta) == _fm([[1, 0, 0], [0, 1, 0], [0, 0, 1]]):
                    if not all(sorted(abs(x) for x in row) == [0, 0, 1] for row in beta):
                        dy = False
    out["CC-DYAD"] = {"green": dy}
    affb = True
    for g in AFFINE_RULES:
        laws = l_scope(g, perms)
        for rnd in ROUNDS:
            if induced_map(g, rnd, laws, perms, True) != induced_map(g, rnd, laws, perms, False):
                affb = False
    out["C-AFFB"] = {"green": affb}
    return out


def cxb_direct(law, g, rnd):
    """C-XB's independent propagation: direct enumeration of the 64 joint configurations with integer weights over
    a common denominator, sharing no code with the permutation path."""
    m, k, reg = rnd
    den = 1
    for p in law:
        den = den * p.denominator // _gcd(den, p.denominator)
    med = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    for key, p in MED_SUPPLIES[m][1].items():
        med[key] = int(p * 4)
    acc = [0] * 16
    for ci, w in enumerate(CARRIER_CFGS):
        wc = int(law[ci] * den)
        if wc == 0:
            continue
        for (u2, v2), wm in med.items():
            if wm == 0:
                continue
            u = [w[0], w[2], u2]
            v = [w[1], w[3], v2]
            for _ in range(k):
                nu = [(g_eval(g, u[(i + 2) % 3], u[(i + 1) % 3]) + v[i]) % 2 for i in range(3)]
                v = u
                u = nu
            if reg is not None and (u[2] if reg[0] == "u2" else v[2]) != reg[1]:
                continue
            acc[u[0] * 8 + v[0] * 4 + u[1] * 2 + v[1]] += wc * wm
    tot = sum(acc)
    if tot == 0:
        return None
    return [Fraction(a, tot) for a in acc]


# ------------------------------------------------------------------------------------------------------------
# r12a: STAB-TRUE (fixture mode; supplied identity map, built outside DECISIVE_BUILDERS). STAB-FALSE rebuilds its
# orbits from the pinned certificate copies and runs in controls.py, since this checker reads no file.
# ------------------------------------------------------------------------------------------------------------
R12_STAB = True    # STAB certificates are mandatory from the authorized design stage onward


def stab_true_control(horizons=(1, 2, 6, 12)):
    """STAB-TRUE: the supplied identity map on the seven QA laws (each law is its own image, herald 1), so
    rank span O_{K-1} = rank span O_K at every horizon; with HC and CONS holding and W-CL silent."""
    tabs = detector_tables()
    st = orbit_stats(qa_family(), lambda law, j: (list(law), Fraction(1)), lambda l: rho_of(l, tabs), 0,
                     kmax=max(horizons), horizons=horizons)
    ok = all(st["STAB"][str(k)] is True and st["HC"][str(k)] and st["CONS"][str(k)] for k in horizons)
    return {"green": ok and not st["WCL"]["fires"], "STAB": st["STAB"], "span_rank": st["span_rank"]}


# ------------------------------------------------------------------------------------------------------------
# The representation ledger: REP-INV (decisive; validation layer) and REP-PLANT
# ------------------------------------------------------------------------------------------------------------
P_ALTS = (("L-PATH", "alpha"), ("L-PATH", "beta"), ("L-PORT", "alpha"), ("L-PORT", "beta"))


def bp_table_relabelled(opts, ident, alt):
    """B-P's outcome table under an alternative, mapped back through the alternative's own relabelling
    (L-PATH alpha: Z+ <-> Z-; L-PORT alpha: the port outcome flipped)."""
    laws, labels = bp_laws(opts)
    sl = BP_SLOTS
    tab = {}
    for law, (src, f, arm) in zip(laws, labels):
        if ident == "L-PATH" and alt == "alpha" and src in ("Z+", "Z-"):
            src = "Z-" if src == "Z+" else "Z+"
        for name, idx in bp_settings():
            out = {}
            for cfg, pr in law.items():
                vals = [cfg[i] for i in idx]
                if ident == "L-PORT" and alt == "alpha":
                    vals[0] = 1 - vals[0]
                out[tuple(vals)] = out.get(tuple(vals), Fraction(0)) + pr
            tab[(src, f, arm, name)] = out
    return tab


def p_token_inputs(cls):
    arms = cls["arms"]
    return {"per_arm": {n: {"V": arms[n]["V"], "D": arms[n]["D"], "K": arms[n]["K"]} for n in cls["adm"]},
            "class_predicate": k_decide_p(cls)["token"],
            "ATTR": k_attr(arms["off"], arms[NAME_ON], arms[NAME_SHK])["value"],
            "eraser": {n: arms[n]["eraser"] for n in cls["adm"]}}


def diff_keys(a, b, prefix=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(ordered_unique(a) | ordered_unique(b), key=str):
            if k not in a or k not in b:
                out.append(prefix + str(k))
            else:
                out += diff_keys(a[k], b[k], prefix + str(k) + ".")
        return out
    return [] if canonical(a) == canonical(b) else [prefix.rstrip(".")]


def s_build_repinv(p_out=None, b_out=None, c_out=None):
    """Decisive family: REP-INV on decisive data (P: L-PATH, L-PORT; C: L-CAL, L-UPRIME with the encoded
    transposition transported to S P S^-1), REP-PLANT, UPR-BC, and the reclassification rule's inputs."""
    s_refusal()
    adm_b, _ = p_classes()
    base_cls = p_class_record(adm_b)[0]
    base = p_token_inputs(base_cls)
    base_tab = bp_table_relabelled(None, None, None)
    out = {"P": {}, "C": {}, "reclassified": []}
    for ident, alt in P_ALTS:
        opts = {"path": alt} if ident == "L-PATH" else {"port": alt}
        cls = p_class_record(adm_b, opts=opts)[0]
        ch = diff_keys(base, p_token_inputs(cls))
        if canonical(bp_table_relabelled(opts, ident, alt)) != canonical(base_tab):
            ch.append("B-P table")
        out["P"]["%s/%s" % (ident, alt)] = "invariant" if not ch else ch
    plant_cls = p_class_record(adm_b, opts={"port": "plant"})[0]
    plant_ch = diff_keys(base, p_token_inputs(plant_cls))
    plant_levels = k_decide_levels({"P": base["class_predicate"], "imported": ["L-PORT"] if plant_ch else []})
    out["REP-PLANT"] = {"changed": plant_ch, "V_on_changed": "per_arm.%s.V" % NAME_ON in plant_ch,
                        "levels": plant_levels,
                        "green": "per_arm.%s.V" % NAME_ON in plant_ch and 1 in plant_levels["withheld_levels"]
                        and 2 in plant_levels["withheld_levels"]}
    if c_out is not None:
        out["C"] = c_repinv(c_out)
    for key, val in list(out["P"].items()) + list(out["C"].items()):
        ident = key.split("/")[0]
        if val != "invariant" and ident not in out["reclassified"]:
            out["reclassified"].append(ident)
    out["UPR-BC"] = [{"id": r["name"], "contextual": r["lp"] == "infeasible",
                      "restored_by_full": r.get("restored_by_full"),
                      "completion_status": (r.get("completion_record") or {}).get("lp", "not attempted"),
                      "imported_for_BC": r["lp"] == "infeasible" and r.get("restored_by_full") is True}
                     for r in (b_out or {}).get("B-C", [])]
    return out


def c_repinv(c_out):
    """L-CAL: every recalibration by one of the 48 signed permutations S (R' = S R, beta' = S beta S^-1,
    P' = S P S^-1). L-UPRIME: the 48 RC2 classes, detectors transported (f_a o A), recalibrated from the
    same source labels. Witnesses per test-rule instance: W-CL (either frame), W-OCT(12), VAL(12), CONS(12)."""
    cache = c_out["cache"]
    bc_horizons = {(item["g"], item["round"]): item["orbit_horizon"] for item in c_out["flagged"]}
    base = {}
    for (g, rnd), st in cache.items():
        if g in TEST_RULES:
            base[(g, rnd)] = (st["WCL"]["fires"], st["WOCT"]["12"], st["VAL"]["12"], st["CONS"]["12"])
    res = {}
    for n, s in enumerate(signed_perms()):
        sinv = [list(col) for col in zip(*s)]
        p2 = matmul(matmul(s, P_SWAP), sinv)
        changed = []
        for (g, rnd), flags in base.items():
            st = cache[(g, rnd)]
            if st["beta"] is None:
                continue
            b2 = matmul(matmul(s, st["beta"]), sinv)
            w = wcl(b2, rnd[1], p2)["fires"]
            rs = [matvec(s, matvec(st["rop"], rho_of(l, detector_tables_cached()))) for name in st["orbits"]
                  for l in st["orbits"][name][:13]]
            woct = any(sum(abs(x) for x in r) > 1 for r in rs)
            val = all(sum(x * x for x in r) <= 1 for r in rs)
            if (w, woct, val, flags[3]) != flags:
                changed.append(g + ":" + round_name(rnd))
        res["L-CAL/%d" % n] = "invariant" if not changed else changed
    classes, _ = rc2_classes()
    for n, (key, (l, t, _)) in enumerate(sorted(classes.items())):
        def amap(w, l=l, t=t):
            return tuple((sum(l[i][j] * w[j] for j in range(4)) + t[i]) % 2 for i in range(4))
        tabs = {a: [Fraction(1) if FUNCTIONALS[a](amap(w)) == 0 else Fraction(0) for w in CARRIER_CFGS]
                for a in ("x", "y", "z")}
        changed = []
        for (g, rnd), flags in base.items():
            st = cache[(g, rnd)]
            replay = {}
            for name in st["orbits"]:
                seq = st["orbits"][name]
                for j in range(len(seq) - 1):
                    replay[tuple(seq[j])] = seq[j + 1]
            st2 = orbit_stats(qa_family(), lambda law, j: (replay.get(tuple(law)), Fraction(1)),
                              lambda law: rho_of(law, tabs), rnd[1])
            if (st2["WCL"]["fires"], st2["WOCT"]["12"], st2["VAL"]["12"], st2["CONS"]["12"]) != flags:
                changed.append(g + ":" + round_name(rnd))
            # R7: compare the B-C read table under the alternative's own axis/outcome relabelling.
            # A changed table is reported/reclassified; it is never re-decided by the LP here.
            horizon = bc_horizons.get((g, round_name(rnd)))
            if horizon is not None:
                laws = [law for sequence in st["orbits"].values() for law in sequence[:horizon+1]]
                columns, transported = [], []
                for axis in ("x", "y", "z"):
                    original = tuple(sum(prob*value for prob, value in zip(law, detector_tables_cached()[axis])) for law in laws)
                    alternative = tuple(sum(prob*value for prob, value in zip(law, tabs[axis])) for law in laws)
                    columns.append(min(original, tuple(1-value for value in original)))
                    transported.append(min(alternative, tuple(1-value for value in alternative)))
                if sorted(columns) != sorted(transported):
                    changed.append("B-C table:"+g+":"+round_name(rnd))
        res["L-UPRIME/%d" % n] = "invariant" if not changed else changed
    return res


_DT_CACHE = []


def detector_tables_cached():
    if not _DT_CACHE:
        _DT_CACHE.append(detector_tables())
    return _DT_CACHE[0]


# ------------------------------------------------------------------------------------------------------------
# The guard: s_mode, the refusal, the single gated entry s_decisive (Decisive builders and the guard; C.5)
# ------------------------------------------------------------------------------------------------------------
def s_mode(argv, environ):
    """The pure mode function: "refuse" without --event; "decisive" iff all four keys hold; else "fixture"."""
    if "--event" not in argv:
        return "refuse"
    i = argv.index("--event")
    if i + 1 >= len(argv):
        return "refuse"
    keys = (argv[i + 1] == DISPATCH_EVENT,
            environ.get("GITHUB_EVENT_NAME") == DISPATCH_EVENT,
            environ.get("GITHUB_RUN_ATTEMPT") == "1",
            environ.get("GITHUB_REF") == ROUND_REF)
    return "decisive" if all(keys) else "fixture"


DECISIVE_BUILDERS = (s_build_p, s_build_repinv, s_build_b, s_build_c)


def s_refusal():
    """One instrumented refusal counter; every decisive entry checks the real process keys."""
    global REFUSAL_CALLS
    REFUSAL_CALLS += 1
    if s_mode(sys.argv, os.environ) != "decisive":
        raise QC21Refusal("decisive mode required")


# Reviewed paper scopes: Lemma P is conditional; the cone bound requires STAB. CC-NAT gates C.
LEMMA_P_REVIEW = "proved_conditional"
CONE_REVIEW = "proved_under_STAB"


def s_decisive():
    """The single gated entry through which every decisive family is built."""
    s_refusal()
    budgets = (P_MAX, B_MAX, W_MAX)
    p_out = s_build_p()
    c_out = s_build_c()
    b_out = s_build_b(p_out, c_out, budgets)
    r_out = s_build_repinv(p_out, b_out, c_out)
    return assemble_decisive(p_out, b_out, c_out, r_out)


def strip_bytes(rec):
    return {k: v for k, v in rec.items() if k not in ("cert",)}


def k_fragment_controls(records):
    """C-CERT and C-BUDGET: a decided result requires every typed resource slot."""
    failures, leaked, over = [], [], []
    budget_keys = ("pivots", "max_bits", "work")
    cap_keys = ("n_extreme", "d", "c", "effects_before_reduction")
    for record in records:
        named = str(record.get("name"))
        decided = record.get("lp") in ("feasible", "infeasible")
        if record.get("verified") is not True:
            failures.append(named)
            if decided:
                leaked.append(named)
        if not decided:
            continue
        budgets, caps = record.get("budget_values"), record.get("cap_values")
        typed = (type(budgets) is list and len(budgets) == 3 and
                 type(caps) is list and len(caps) == 4 and
                 all(x is None or (type(x) is int and x >= 0) for x in budgets + caps))
        counters = [record.get(k) for k in budget_keys + cap_keys]
        typed = typed and all(type(x) is int and x >= 0 for x in counters)
        if not typed:
            over.append(named)
            continue
        if any(limit is not None and value > limit
               for value, limit in zip(counters[:3], budgets)):
            over.append(named)
            continue
        if any(limit is not None and value > limit
               for value, limit in zip(counters[3:], caps)):
            over.append(named)
    return {"C-CERT": {"green": not leaked, "unverified": len(failures),
                       "unverified_fragments": failures, "given_verdict_without_certificate": leaked},
            "C-BUDGET": {"green": not over, "given_verdict_over_limit": over}}

def assemble_decisive(p_out, b_out, c_out, r_out):
    fx = fixture_section()
    p_red = [k for k, v in p_out["controls"].items() if not v["green"]]
    p_red += [k for k in ("CW-P", "QM-P", "ATTR-FIX") if not fx["controls"][k]["green"]]
    if not r_out["REP-PLANT"]["green"]:
        p_red.append("REP-PLANT")
    p_rec = {"adm": p_out["decide_p_inputs"]["adm"], "arms": p_out["arms"], "off": "off", "on": NAME_ON,
             "controls_red": p_red}
    p_tok = k_decide_p(p_rec)
    b_red = [k for k in ("B-POS", "B-STAB", "B-CLASS", "B-REG", "B-WAVE", "B-S4F", "B-RAY", "QM-P", "C-CERT", "C-NCF", "C-SYM", "ZPT",
                         "F10") if not fx["controls"][k]["green"]]
    frs = [strip_bytes(f) for f in b_out["fragments"]] + [strip_bytes(f) for f in b_out["B-C"]]
    monitored = list(frs)+[f["completion_record"] for f in frs if isinstance(f.get("completion_record"), dict)]
    decisive_controls = k_fragment_controls(monitored)
    b_red += [name+"-decisive" for name, control in decisive_controls.items() if not control["green"]]
    b_tok = k_decide_b({"controls_red": b_red, "fragments": frs})
    c_red = [k for k, v in c_out["controls"].items() if not v["green"] and not v.get("reported_only")
]
    c_red += [k for k in ("C-STAB", "C-R60", "C-R60-ODD", "C-35", "C-S3", "C-PLANT", "C-CONSX", "C-DET", "C-STEP",
                          "REP-FRAME", "C-AFFB-fixture") if not fx["controls"][k]["green"]]
    if not r_out["REP-PLANT"]["green"]:
        b_red.append("REP-PLANT")
        c_red.append("REP-PLANT")
        b_tok = k_decide_b({"controls_red": b_red, "fragments": frs})
    c_tok = k_decide_c({"controls_red": c_red, "complete": True, "flags_agree": True,
                        "instances": c_out["instances"]})
    bp = b_out["fragments"][0]
    levels = k_decide_levels({"P": p_tok["token"], "C": c_tok["token"], "imported": r_out["reclassified"],
                              "B_P": {"contextual": b_tok["token"] == "B-CONTEXTUAL", "lp_reads_equal_acc":
                                      bp["lp_reads_equal_acc"], "acc_owner_typed": True,
                                      "acc_typing": ACC_BP_TYPING},
                              "upr_bc": [{"contextual": u["contextual"], "restored_by_full": u["restored_by_full"]}
                                         for u in r_out["UPR-BC"]]})
    c_inst = []
    for i in c_out["instances"]:
        c_inst.append({k: v for k, v in i.items() if k not in ("orbit_laws",)})
    m = {"schema": SCHEMA, "version": SCHEMA_VERSION, "mode": "decisive", "complete": True,
         "parameters": {"dispatch_sha": None},
         "P": {k: v for k, v in p_out.items() if k not in ("controls",)},
         "P_controls": p_out["controls"],
         "REP_INV": r_out,
         "B": {"fragments": frs, "bp_equals_qmp": b_out["bp_equals_qmp"], "B1": b_out["B1"], "decisive_controls": decisive_controls},
         "C": {"instances": c_inst, "controls": c_out["controls"], "diagnostics_r5": c_out["diagnostics_r5"],
               "flagged": [i["id"] for i in c_out["flagged"]], "lemma_p_review": LEMMA_P_REVIEW,
               "cone_review": CONE_REVIEW},
         "fixtures": fx["fixtures"], "controls": fx["controls"],
         "budget": {"P_max": P_MAX, "B_max": B_MAX, "W_max": W_MAX, "S_max": S_MAX, "BP": {"P_max": BP_P_MAX, "B_max": BP_B_MAX, "W_max": BP_W_MAX,
                    "caps": [BP_CAP_GENERATORS, BP_CAP_D, BP_CAP_FACET_SUBSETS, BP_CAP_EFFECTS]},
                    "respected": {f["name"]: (f.get("lp") in ("feasible", "infeasible") and
                         k_fragment_controls([f])["C-BUDGET"]["green"]) for f in frs}},
         "flags": {"P": p_tok["token"], "B": b_tok["token"], "C": c_tok["token"], "levels": levels,
                   "refusal_calls": REFUSAL_CALLS, "controls_red": {"P": p_red, "B": b_red, "C": c_red}}}
    return m


# ------------------------------------------------------------------------------------------------------------
# Fixture mode: every fixture-mode control, decided with the full method and the independent verifier
# ------------------------------------------------------------------------------------------------------------
FIXTURE_EXPECT = {
    "B-POS": ("infeasible", 4), "B-STAB": ("feasible", 2), "B-CLASS": ("feasible", 2), "B-REG": ("infeasible", 4),
    "B-REG+parity": ("feasible", 2), "B-WAVE": ("infeasible", 4), "ZPT": ("feasible", 3), "F10": ("feasible", 4),
    "QM-P": ("infeasible", 4), "B-S4F": ("feasible", 4),
    "B-RAY-S": ("feasible", 2), "B-RAY-P": ("infeasible", 4), "B-RAY-F": ("feasible", 4)}


def fixture_fragments():
    return [fx_b_pos(), fx_b_stab(), fx_b_class(), fx_b_reg(), fx_b_reg(True), fx_b_wave(), fx_zpt(), fx_f10(),
            qm_p_fragment(), fx_b_s4f(), fx_b_ray(fx_b_stab(), "B-RAY-S"),
            fx_b_ray(fx_b_pos(), "B-RAY-P"), fx_b_ray(fx_b_s4f(), "B-RAY-F")]


def attr_fix():
    """ATTR-FIX: synthetic field records fed to ATTR; and the decide-p mutation flipping sham-specific fields."""
    def a(v, d, k):
        return {"V": v, "D": d, "K": k}
    off = a(1, 0, KER_ID)
    on = a(0, 1, KER_UNIF)
    i = k_attr(off, on, a(1, 0, KER_UNIF))["value"]
    ii = k_attr(off, on, a(0, 0, KER_UNIF))["value"]
    iii = k_attr(off, on, a(1, 1, KER_UNIF))
    rec = {"adm": ["off", "on", "shk"], "off": "off", "on": "on", "controls_red": [],
           "arms": {"off": dict(off, NONABS=True, SPI=True), "on": dict(on, NONABS=True, SPI=True),
                    "shk": dict(a(0, 0, KER_UNIF), NONABS=True, SPI=True)}}
    t0 = k_decide_p(rec)["token"]
    rec2 = json.loads(canonical(rec))
    rec2["arms"]["shk"]["V"] = "1"
    rec2["shk"] = "flipped"
    rec2["sh0"] = "flipped"
    t1 = k_decide_p(rec2)["token"]
    return {"green": i == "attributable to which-path recording" and ii == "not attributable"
            and iii["value"] == "undefined" and len(iii["failing"]) > 0 and t0 == t1,
            "i": i, "ii": ii, "iii": iii, "token_unchanged": t0 == t1}


def upr_bc_fix():
    r1 = k_decide_levels({"P": "P-COMPLEMENTARITY", "upr_bc": [{"contextual": True, "restored_by_full": True}]})
    r2 = k_decide_levels({"P": "P-COMPLEMENTARITY", "upr_bc": [{"contextual": True, "restored_by_full": False}]})
    r3 = k_decide_levels({"P": "P-COMPLEMENTARITY", "upr_bc": [{"contextual": True, "restored_by_full": None,
                                                                 "completion_status": "out_of_scope"}]})
    return {"green": r1["upr_bc_imported_for_bc"] and r1["upr_bc_label"] == UPR_BC_LABEL
            and not r2["upr_bc_imported_for_bc"] and not r3["upr_bc_imported_for_bc"]
            and r1["level"] == r2["level"] == r3["level"] == 1,
            "unresolved_completion_status": "out_of_scope"}


_FX_CACHE = []


def fixture_section(budget_vals=None):
    if budget_vals is None and _FX_CACHE:
        return _FX_CACHE[0]
    bv = (P_MAX, B_MAX, W_MAX) if budget_vals is None else budget_vals
    fixtures, controls = {}, {}
    unverified, ncf_bad, sym_bad = 0, 0, 0
    over = []
    recs = {}
    for fr in fixture_fragments():
        r = s_decide(fr, bv)
        recs[fr["name"]] = r
        exp = FIXTURE_EXPECT.get(fr["name"])
        rec = {"lp": r["lp"], "decided_by": r["decided_by"], "d": r["d"], "r_S": r["r_S"], "r_E": r["r_E"],
               "tomo": r["tomo"], "T": r.get("T"), "pivots": r["pivots"], "max_bits": r["max_bits"],
               "work": r["work"], "cert_sha256": r["cert_sha256"], "verified": r["verified"],
               "expected": list(exp) if exp else None,
               "as_expected": exp is not None and (r["lp"], r["decided_by"]) == exp}
        if r["lp"] == "out_of_scope":
            over.append(fr["name"])
        if not r["verified"]:
            unverified += 1
        if r["d"] == r["r_S"] == r["r_E"] and r["decided_by"] != 2:
            ncf_bad += 1
        if r["decided_by"] in (2, 3):
            r4 = s_decide(fr, bv, force_step4=True)
            rec["step4_check"] = {"lp": r4["lp"], "verified": r4["verified"]}
            if r4["lp"] != r["lp"] or not r4["verified"]:
                ncf_bad += 1
        sym_budget = Budget(*bv)
        try:
            sym = s_decide_effect_facet(fr, sym_budget)
        except OutOfScope as error:
            sym = {"lp": "out_of_scope", "verified": False, "cert": None,
                   "cert_sha256": None, "decided_by": None, "reason": str(error), **sym_budget.record()}
        rec["effect_facet"] = strip_bytes(sym)
        if sym["lp"] != r["lp"] or sym["verified"] is not True:
            sym_bad += 1
        fixtures[fr["name"]] = rec
    reg_acc = fx_b_reg(acc_parity=True)
    lp_eq = sorted(reg_acc["lp_settings"]) == sorted(reg_acc["acc"])
    tok_reg = k_decide_b({"controls_red": [], "fragments": [dict(strip_bytes(recs["B-REG"]), role="B-P",
                                                                 lp_reads_equal_acc=lp_eq, preps=32, lp_settings=list(ACC_BP), acc=list(ACC_BP))]})["token"]
    lev_reg = k_decide_levels({"P": "P-COMPLEMENTARITY", "B_P": {"contextual": True, "lp_reads_equal_acc": True,
                                                                  "acc_owner_typed": False,
                                                                  "acc_typing": "design-chosen"}})
    fixtures["B-REG"]["acc_subset_case"] = {"lp_reads_equal_acc": lp_eq, "decide_b": tok_reg,
                                            "level_design_chosen_acc": lev_reg["level"]}
    ok = lambda n: fixtures[n]["as_expected"] and fixtures[n]["verified"]
    controls["B-POS"] = {"green": ok("B-POS")}
    controls["B-STAB"] = {"green": ok("B-STAB")}
    controls["B-CLASS"] = {"green": ok("B-CLASS")}
    controls["B-REG"] = {"green": ok("B-REG") and ok("B-REG+parity") and fixtures["B-REG"]["tomo"] is False
                         and lp_eq is False and tok_reg == "B-VOID" and lev_reg["level"] == 1}
    alpha = cw_alpha_two_detector()
    controls["B-WAVE"] = {"green": ok("B-WAVE") and alpha >= 1, "alpha": alpha}
    controls["ZPT"] = {"green": ok("ZPT")}
    controls["F10"] = {"green": ok("F10") and fixtures["F10"]["T"] == 0}
    controls["B-S4F"] = {"green": ok("B-S4F") and fixtures["B-S4F"]["T"] == 3}
    controls["B-RAY"] = {"green": all(ok(n) and recs[n]["n_distinct"] == 5 and recs[n]["n_extreme"] == 4
                                          for n in ("B-RAY-S", "B-RAY-P", "B-RAY-F"))}
    controls["C-CERT"] = {"green": unverified == 0, "unverified": unverified}
    controls["C-NCF"] = {"green": ncf_bad == 0, "bad": ncf_bad}
    controls["C-SYM"] = {"green": sym_bad == 0, "mismatches": sym_bad}
    cw = cw_p_model()
    cw_tok = k_decide_p(cw)["token"]
    cw_attr = k_attr(cw["arms"]["off"], cw["arms"]["on"], cw["arms"]["SH-K"])["value"]
    ce = cw["arms"]["on"]["eraser"]
    cw_ref = (cw["arms"]["off"]["V"] == 1 and cw["arms"]["off"]["D"] == 0 and cw["arms"]["on"]["V"] == 0
              and cw["arms"]["on"]["D"] == 1 and cw["arms"]["SH-0"]["V"] == 1 and cw["arms"]["SH-0"]["D"] == 0
              and cw["arms"]["SH-K"]["V"] == 0 and cw["arms"]["SH-K"]["D"] == 0
              and ce["conjugate"] == {"0": 1, "1": 1} and ce["path"] == {"0": 0, "1": 0} and ce["unsorted"] == 0
              and cw["arms"]["SH-K"]["eraser"]["noise"] == {"0": 1, "1": 1})
    controls["CW-P"] = {"green": cw_tok == "P-COMPLEMENTARITY" and cw_attr == "not attributable" and cw_ref
                        and cw["alpha"] >= 1, "token": cw_tok, "ATTR": cw_attr, "alpha": cw["alpha"]}
    qm = qm_p_model()
    qm_tok = k_decide_p(qm)["token"]
    qm_attr = k_attr(qm["arms"]["off"], qm["arms"]["on"], qm["arms"]["SH-K"])["value"]
    qmf = fixtures["QM-P"]
    controls["QM-P"] = {"green": qm_tok == "P-COMPLEMENTARITY" and qm_attr == "not attributable"
                        and qm["arms"]["purified"]["D"] == 1 and qm["arms"]["SH-K"]["D"] == 0
                        and qmf["verified"] and qmf["lp"] in ("feasible", "infeasible"),
                        "token": qm_tok, "ATTR": qm_attr}
    fixtures["CW-P"] = {a: {k: cw["arms"][a][k] for k in ("V", "D", "K", "eraser")} for a in cw["arms"]}
    fixtures["QM-P_arms"] = {a: {k: qm["arms"][a][k] for k in ("V", "D", "K", "eraser")} for a in qm["arms"]}
    controls["ATTR-FIX"] = attr_fix()
    controls["UPR-BC"] = upr_bc_fix()
    controls.update(c_fixture_controls())
    if R12_STAB:
        controls["STAB-TRUE"] = stab_true_control()
    controls["C-BUDGET-fixtures"] = {"green": not over, "out_of_scope": over}
    adm_b, adm_a = p_classes()
    controls["ADM-SIZES"] = {"green": len(adm_a) == 12 and len(adm_b) == 6}
    sec = {"fixtures": fixtures, "controls": controls, "out_of_scope": over}
    if budget_vals is None:
        _FX_CACHE.append(sec)
    return sec


def fixture_mismatches(sec):
    bad = [n for n, r in sec["fixtures"].items() if "as_expected" in r and not r["as_expected"]]
    bad += [n for n, c in sec["controls"].items() if not c["green"]]
    return bad


PLACEHOLDER = "placeholder"


def fixture_measurements(dispatch_sha=None):
    sec = fixture_section()
    return {"schema": SCHEMA, "version": SCHEMA_VERSION, "mode": "fixture", "complete": False,
            "parameters": {"dispatch_sha": dispatch_sha},
            "P": PLACEHOLDER, "P_controls": PLACEHOLDER, "REP_INV": PLACEHOLDER,
            "B": {"fragments": [{"name": n, "lp": PLACEHOLDER} for n in ("B-P", "A-of-B")],
                  "bp_equals_qmp": PLACEHOLDER, "B1": PLACEHOLDER},
            "C": PLACEHOLDER,
            "fixtures": sec["fixtures"], "controls": sec["controls"],
            "budget": {"P_max": P_MAX, "B_max": B_MAX, "W_max": W_MAX, "respected": PLACEHOLDER},
            "flags": {"P": PLACEHOLDER, "B": PLACEHOLDER, "C": PLACEHOLDER, "levels": PLACEHOLDER,
                      "refusal_calls": REFUSAL_CALLS, "fixture_mismatches": fixture_mismatches(sec)}}


def stress_record(result, role, seed=None):
    item = strip_bytes(result)
    item.update({"class": role, "seed": seed, "verdict": result["lp"],
                 "certificate_verified": result["verified"],
                 "certificate": json.loads(result["cert"]) if result["cert"] is not None else None})
    return item


def fixture_completion(fragment):
    """The full configuration read, reporting the copied full-read completion (CC-F0)."""
    result = dict(fragment)
    size = len(fragment["laws"][0])
    result["name"] = fragment["name"]+"+all-joint"
    result["reads"] = list(fragment["reads"])+[[Fraction(1 if i == j else 0) for i in range(size)] for j in range(size)]
    result["lp_settings"] = list(fragment["lp_settings"])+["all-joint"]
    result["acc"] = list(result["lp_settings"])
    return result


def stress_output():
    """Six independent coset instances, ST-BP, and all frozen fixture decisions/completions; no native family."""
    if not isinstance(S_MAX, int) or S_MAX < 1:
        raise QC21Refusal("S_MAX is unset")
    fragments, w_fix, w_stress = [], 0, 0
    for kind in ("SF-1", "SF-2"):
        for seed in STRESS_SEEDS:
            fragment = stress_fixture(kind, seed)
            caps = (None, None, S_MAX, None) if kind == "SF-1" else (None, None, None, None)
            result = s_decide(fragment, cap_vals=caps)
            item = stress_record(result, "ST-BP" if kind == "SF-1" else "stress", seed)
            item["over_maximum"] = (kind == "SF-1" and result.get("c", 0) > S_MAX)
            fragments.append(item)
            w_stress += result["work"]
    for fragment in fixture_fragments():
        result = s_decide(fragment, cap_vals=(None, None, None, None))
        fragments.append(stress_record(result, "fixture"))
        w_fix += result["work"]
        if result["decided_by"] in (2, 3):
            forced = s_decide(fragment, force_step4=True, cap_vals=(None, None, None, None))
            forced["name"] += ":step4-check"
            fragments.append(stress_record(forced, "fixture"))
            w_fix += forced["work"]
        exchanged = s_decide_effect_facet(fragment, Budget())
        exchanged["name"] = fragment["name"]+":C-SYM"
        fragments.append(stress_record(exchanged, "fixture"))
        w_fix += exchanged["work"]
        completion = s_decide(fixture_completion(fragment), cap_vals=(None, None, None, None))
        fragments.append(stress_record(completion, "fixture"))
        w_fix += completion["work"]
    return {"schema": STRESS_SCHEMA, "version": STRESS_VERSION, "seeds": list(STRESS_SEEDS),
            "S_max": S_MAX, "fragments": fragments, "W_fix": w_fix, "W_stress": w_stress}


# ------------------------------------------------------------------------------------------------------------
# Self-tests (never building a decisive family)
# ------------------------------------------------------------------------------------------------------------
SELFTEST_LOG = []


def t_builder_refuses():
    try:
        s_decisive()
    except QC21Refusal:
        SELFTEST_LOG.append(("t_builder_refuses", True))
    else:
        SELFTEST_LOG.append(("t_builder_refuses", False))


def t_check(name, cond):
    SELFTEST_LOG.append((name, bool(cond)))


def t_mguard_checker():
    """M-GUARD, the checker's keys: through the entry with synthetic argv and environment."""
    hexsha = "0123456789abcdef0123456789abcdef01234567"
    disp = {"GITHUB_EVENT_NAME": DISPATCH_EVENT, "GITHUB_RUN_ATTEMPT": "1", "GITHUB_REF": ROUND_REF}
    cases = [(["q", "--event", "pull_request"], {}), (["q", "--event", "push"], {}),
             (["q", "--event", "fixture"], {}), (["q", "--event", "fixture"], disp),
             (["q", "--event", "closed-or-other", "--dispatch-sha", hexsha], disp),
             (["q", "--event", DISPATCH_EVENT], dict(disp, GITHUB_EVENT_NAME="pull_request")),
             (["q", "--event", "pull_request"], disp),
             (["q", "--event", DISPATCH_EVENT], dict(disp, GITHUB_RUN_ATTEMPT="2")),
             (["q", "--event", DISPATCH_EVENT], dict(disp, GITHUB_REF="refs/heads/main"))]
    for argv, env in cases:
        before = REFUSAL_CALLS
        code, text = s_entry(argv, env)
        m = json.loads(text) if code in (0, 3) else {}
        t_check("M-GUARD fixture %s %s" % (argv[1:], sorted(env.items())),
                code in (0, 3) and m.get("mode") == "fixture" and m.get("P") == PLACEHOLDER
                and REFUSAL_CALLS == before)
        if "--dispatch-sha" in argv:
            t_check("M-GUARD B4 argv records dispatch_sha", m.get("parameters", {}).get("dispatch_sha") == hexsha)
    code, _ = s_entry(["q"], disp)
    t_check("M-GUARD missing --event exits 4", code == 4)
    for bad in ("0123", "0123456789ABCDEF0123456789abcdef01234567", "-" + hexsha[1:], hexsha + "0"):
        code, _ = s_entry(["q", "--event", "fixture", "--dispatch-sha", bad], {})
        t_check("M-GUARD malformed --dispatch-sha exits 4 (%s)" % bad[:6], code == 4)
    t_check("M-GUARD s_mode decisive iff all four keys", s_mode(["q", "--event", DISPATCH_EVENT], disp) == "decisive")
    for k in disp:
        t_check("M-GUARD s_mode single-key failure " + k,
                s_mode(["q", "--event", DISPATCH_EVENT], dict(disp, **{k: "x"})) == "fixture")
    t_check("M-GUARD s_mode first key", s_mode(["q", "--event", "fixture"], disp) == "fixture")
    before = REFUSAL_CALLS
    t_builder_refuses()
    t_check("one direct refusal accounted for", REFUSAL_CALLS == before + 1)


def t_decide_paths():
    def arm(v, d, k=KER_ID, nonabs=True, spi=True):
        return {"V": v, "D": d, "K": k, "NONABS": nonabs, "SPI": spi}
    base = {"adm": ["off", "on", "a", "shk"], "off": "off", "on": "on", "controls_red": [],
            "arms": {"off": arm(1, 0), "on": arm(0, 1, KER_UNIF), "a": arm(0, 1, KER_UNIF),
                     "shk": arm(0, 0, KER_UNIF)}}
    t_check("decide-p COMPLEMENTARITY", k_decide_p(base)["token"] == "P-COMPLEMENTARITY")
    r = json.loads(canonical(base))
    r["arms"]["a"]["V"] = "1"
    t_check("decide-p RECORD-WITHOUT-SUPPRESSION", k_decide_p(r)["token"] == "P-RECORD-WITHOUT-SUPPRESSION")
    r = json.loads(canonical(base))
    r["arms"]["on"]["D"] = "0"
    t_check("decide-p NO-RECORD", k_decide_p(r)["token"] == "P-NO-RECORD")
    r = json.loads(canonical(base))
    r["arms"]["off"]["V"] = "0"
    t_check("decide-p NO-FRINGES", k_decide_p(r)["token"] == "P-NO-FRINGES")
    for mut in ("red", "missing", "nonabs", "spi", "missing-off"):
        r = json.loads(canonical(base))
        if mut == "red":
            r["controls_red"] = ["PL-SHARP"]
        elif mut == "missing":
            del r["arms"]["a"]["D"]
        elif mut == "nonabs":
            r["arms"]["a"]["NONABS"] = False
        elif mut == "spi":
            r["arms"]["shk"]["SPI"] = False
        else:
            del r["arms"]["off"]
        t_check("decide-p VOID " + mut, k_decide_p(r)["token"] == "P-VOID")
    fr = lambda lp, role="B-P", eq=True, ver=True: {"name": "f", "role": role, "lp": lp, "verified": ver,
                                                    "lp_reads_equal_acc": eq, "preps": 32, "lp_settings": list(ACC_BP), "acc": list(ACC_BP)}
    t_check("decide-b CONTEXTUAL", k_decide_b({"controls_red": [], "fragments": [fr("infeasible")]})["token"] ==
            "B-CONTEXTUAL")
    t_check("decide-b IMITABLE", k_decide_b({"controls_red": [], "fragments": [fr("feasible")]})["token"] ==
            "B-CLASSICALLY-IMITABLE")
    for name, rec in (("red", {"controls_red": ["B-POS"], "fragments": [fr("feasible")]}),
                      ("undecided", {"controls_red": [], "fragments": [fr("undecided")]}),
                      ("out_of_scope", {"controls_red": [], "fragments": [fr("out_of_scope")]}),
                      ("unverified", {"controls_red": [], "fragments": [fr("feasible", ver=False)]}),
                      ("lp_reads", {"controls_red": [], "fragments": [fr("infeasible", eq=False)]}),
                      ("missing", {"fragments": []})):
        t_check("decide-b VOID " + name, k_decide_b(rec)["token"] == "B-VOID")
    for role in ("A-of-B", "B-C", "completion"):
        for outcome in ("undecided", "out_of_scope"):
            record = {"controls_red": [], "fragments": [fr("feasible"), fr(outcome, role, ver=False)]}
            t_check("decide-b report-only "+role+" "+outcome, k_decide_b(record)["token"] == "B-CLASSICALLY-IMITABLE")
    small = fr("infeasible")
    small["preps"] = 16
    t_check("SG-1 refuses sixteen preparations", k_decide_b({"controls_red": [], "fragments": [small]})["token"] == "B-VOID")
    yes = {"6": True, "12": True}
    no = {"6": False, "12": False}
    six = {"6": True, "12": False}
    inst = lambda **kw: dict({"id": "i", "HC": yes, "CONS": yes, "VAL": yes, "WOCT": no, "WCL": True, "ABL": True,
                              "EMB": True}, **kw)
    c = lambda insts, **kw: dict({"controls_red": [], "complete": True, "flags_agree": True, "instances": insts}, **kw)
    t_check("decide-c EXPOSURE", k_decide_c(c([inst()]))["token"] == "C-EXPOSURE")
    t_check("decide-c SIZE-DEPENDENT", k_decide_c(c([inst(CONS=six)]))["token"] == "C-SIZE-DEPENDENT")
    t_check("decide-c NONSTABILIZER", k_decide_c(c([inst(WCL=False, WOCT=yes)]))["token"] == "C-NONSTABILIZER")
    t_check("decide-c SURVIVAL", k_decide_c(c([inst(WCL=False)]))["token"] == "C-SURVIVAL")
    t_check("decide-c ABL blocks", k_decide_c(c([inst(ABL=False)]))["token"] == "C-SURVIVAL")
    for name, rec in (("red", c([inst()], controls_red=["C-DET"])), ("incomplete", c([inst()], complete=False)),
                      ("flags", c([inst()], flags_agree=False)), ("missing", {"controls_red": []})):
        t_check("decide-c VOID " + name, k_decide_c(rec)["token"] == "C-VOID")
    bp_ok = {"contextual": True, "lp_reads_equal_acc": True, "acc_owner_typed": True, "acc_typing": "t"}
    L = lambda **kw: k_decide_levels(dict({"P": "P-COMPLEMENTARITY", "B_P": bp_ok, "C": "C-EXPOSURE"}, **kw))
    t_check("levels 3", L()["level"] == 3)
    t_check("levels 2", L(C="C-SURVIVAL")["level"] == 2)
    t_check("levels 1", L(B_P=dict(bp_ok, contextual=False))["level"] == 1)
    t_check("levels none", L(P="P-NO-RECORD")["level"] == "none")
    t_check("levels no 3 without 2", L(B_P=dict(bp_ok, lp_reads_equal_acc=False))["level"] == 1)
    t_check("levels design-chosen Acc", L(B_P=dict(bp_ok, acc_owner_typed=False), C="C-SURVIVAL")["level"] == 1)
    t_check("levels representation rule L-PORT", L(imported=["L-PORT"])["level"] == "none")
    t_check("levels representation rule L-CAL", L(imported=["L-CAL"])["level"] == 2)
    t_check("levels Level-1 sentence printed", LEVEL1_SENTENCE in L()["lines"])
    ab = k_ab_p(base, base)
    t_check("ab-p both succeed", ab["existence_case"] == "both succeed" and ab["universality_case"] == "both succeed")
    r = json.loads(canonical(base))
    r["arms"]["a"]["V"] = "1"
    ab = k_ab_p(r, base)
    t_check("ab-p A fails, B succeeds", ab["universality_case"] == "A fails and B succeeds"
            and ab["A_P"]["record_without_suppression"] == ["a"])
    t_check("ab-p B fails", k_ab_p(base, r)["universality_case"] == "B fails")
    dec = k_decompose_p(base["arms"], "off", "on", "off", "shk")
    t_check("decompose-p validity flags", dec["valid_K_SHK_eq_K_on"] and dec["valid_D_SHK_zero"])


def t_mutations():
    """M-FACET, M-W, M-MODEL, M-SOLVER, M-FACTOR, M-BUDGET (C.4, through the adaptation table)."""
    step4_infeasible = {"B-POS": fx_b_pos(), "B-REG": fx_b_reg()}

    def drop_facet(c):
        c = dict(c)
        c["facets"] = c["facets"][1:]
        return c

    def neg_w(c):
        c = dict(c)
        c["W"] = [[-x for x in r] for r in c["W"]]
        return c

    def shift_w(c):
        c = dict(c)
        d = len(c["W"])
        tr = sum(c["W"][i][i] for i in range(d))
        cc = 1 - q_div(tr, d)
        c["W"] = [[c["W"][i][j] + (cc if i == j else 0) for j in range(d)] for i in range(d)]
        return c

    for name, fr in step4_infeasible.items():
        for mname, mut in (("M-FACET", drop_facet), ("M-W neg", neg_w), ("M-W shift", shift_w)):
            r = s_decide(fr, mutate=mut)
            t_check("%s fails C-CERT on %s" % (mname, name), r["verified"] is False and r["lp"] == "undecided")

    def bump_model(c):
        c = dict(c)
        mu, xi = [list(r) for r in c["mu"]], [list(r) for r in c["xi"]]
        for e in range(len(xi)):
            for j in range(len(xi[e])):
                if any(m[j] > 0 for m in mu):
                    xi[e][j] = xi[e][j] + 1
                    c["xi"] = xi
                    return c
        return c

    for name, fr, step in (("B-CLASS", fx_b_class(), 2), ("ZPT", fx_zpt(), 3), ("F10", fx_f10(), 4), ("B-S4F", fx_b_s4f(), 4)):
        r0 = s_decide(fr)
        r = s_decide(fr, mutate=bump_model)
        t_check("M-MODEL fails C-CERT on a step-%d certificate (%s)" % (step, name),
                r0["decided_by"] == step and r["verified"] is False)
    r = s_decide(fx_b_class(), mutate=lambda c: None)
    t_check("M-SOLVER no certificate", r["verified"] is False and r["lp"] == "undecided")
    other = s_decide(fx_b_pos())

    def swap_cert(c):
        c2 = json.loads(other["cert"])
        c2["A"], c2["B"], c2["d"] = c["A"], c["B"], c["d"]
        return c2

    r = s_decide(fx_b_class(), mutate=swap_cert)
    t_check("M-SOLVER other verdict's certificate", r["verified"] is False)
    case = dict(strip_bytes(r), role="B-P", preps=32, lp_settings=list(ACC_BP), acc=list(ACC_BP),
                lp_reads_equal_acc=True, lp="feasible", verified=False)
    token_bad = k_decide_b({"controls_red": [], "fragments": [case]})["token"]
    token_good = k_decide_b({"controls_red": [], "fragments": [dict(case, verified=True)]})["token"]
    t_check("M-SOLVER invalid certificate, not SG-1, gives VOID",
            r["verified"] is False and token_bad == "B-VOID" and token_good == "B-CLASSICALLY-IMITABLE")

    def bump_a(c):
        c = dict(c)
        a = [list(x) for x in c["A"]]
        a[0][0] = a[0][0] + 1
        c["A"] = a
        return c

    r = s_decide(fx_b_pos(), mutate=bump_a)
    t_check("M-FACTOR fails A B^T = N", r["verified"] is False)
    ray = fx_b_ray(fx_b_pos(), "B-RAY-P")

    def ray_weight(c):
        c = json.loads(canonical(c))
        c["prep_removals"][0]["weights"][0] = parse_q(c["prep_removals"][0]["weights"][0])+1
        return c

    def ray_extreme(c):
        c = json.loads(canonical(c))
        c["prep_removals"] = [{"row": 0, "sources": [1], "weights": [1]}]+c["prep_removals"]
        c["prep_kept"] = [i for i in c["prep_kept"] if i != 0]
        return c

    for label, mutation in (("multiplier", ray_weight), ("fabricated extreme removal", ray_extreme)):
        record = s_decide(ray, mutate=mutation)
        t_check("M-RAY "+label, record["verified"] is False and record["lp"] == "undecided")

    def drop_removed_model_row(c):
        c = dict(c)
        c["mu"] = list(c["mu"][:-1])
        return c

    ray_model = s_decide(fx_b_ray(fx_b_s4f(), "B-RAY-F"), mutate=drop_removed_model_row)
    t_check("B-RAY-F model must include the removed preparation", ray_model["verified"] is False and ray_model["lp"] == "undecided")

    for name, fr in (("B-REG", fx_b_reg()), ("ZPT", fx_zpt())):
        for which, bv in (("P_max", (1, None, None)), ("B_max", (None, 1, None)), ("W_max", (None, None, 1))):
            r = s_decide(fr, bv)
            ok = r["lp"] == "out_of_scope"
            free = s_decide(fr)
            if which == "P_max":
                ok = ok and r["pivots"] <= 2
            if which == "W_max":
                ok = ok and r["work"] <= 1 + free["work"]
            limited = dict(strip_bytes(r), role="B-P", preps=32, lp_settings=list(ACC_BP),
                           acc=list(ACC_BP), lp_reads_equal_acc=True)
            # The valid B-P is the same fragment decided without a budget, so it is within its own limits.
            valid = dict(strip_bytes(free), role="B-P", name="B-P-valid", preps=32, lp_settings=list(ACC_BP),
                         acc=list(ACC_BP), lp_reads_equal_acc=True, lp="feasible", verified=True)
            reported = dict(limited, role="A-of-B")
            void = k_decide_b({"controls_red": [], "fragments": [limited]})["token"]
            still_valid = k_decide_b({"controls_red": [], "fragments": [valid, reported]})["token"]
            monitored = k_fragment_controls([valid, reported])
            t_check("M-BUDGET %s on %s" % (which, name),
                    ok and void == "B-VOID" and still_valid == "B-CLASSICALLY-IMITABLE"
                    and monitored["C-BUDGET"]["green"] and monitored["C-CERT"]["green"])


def t_misc():
    t_check("sha256 test vector", h_sha256(b"abc") ==
            "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")
    t_check("sha256 empty", h_sha256(b"") ==
            "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855")
    t_check("sha256 448-bit vector", h_sha256(b"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq") ==
            "248d6a61d20638b8e5c026930c3e6039a33ce45964ff2167f6ecedd419db06c1")
    t_check("native step on supplied states", native_step({"a": (1, 0), "b": (1, 1)}, ordered_unique([ordered_key(("a", "b"))]))
            == {"a": (1, 1), "b": (0, 1)} and native_step({"a": (1, 0)}, ordered_unique()) == {"a": (0, 1)})
    laws = [{(0, 1, 1): Fraction(1, 2), (1, 1, 0): Fraction(1, 2)}, {(0, 0, 0): Fraction(1)}]
    fr = frag_from_laws("eval", laws, (0, 2), [("b0", _bit(0)), ("b2", _bit(1))])
    tab = frag_outcome_table(fr)
    direct = [[sum(p for c, p in l.items() if c[i] == v) for i, v in ((0, 0), (0, 1), (2, 0), (2, 1))] for l in laws]
    t_check("fragment builder against the definition (C-EVAL)", tab == direct)
    t_check("C-STEP transport mutation turns it red", c_step_control(True)["green"] is False)
    adm_b, adm_a = p_classes()
    t_check("|Adm_A| = 12 and |Adm_B| = 6", len(adm_a) == 12 and len(adm_b) == 6)
    t_check("Adm_B names", [n for n, _ in adm_b] == ["off", "(0,w')", "(1,w')", "(w,0)", "(w,1)", "(w,w')"])
    t_check("rational roots", rational_roots([1, -2, 1])[0] == [1, 1])
    t_check("r12a STAB-TRUE: the supplied identity map gives STAB true at K = 1, 2, 6, 12",
            stab_true_control()["green"])
    t_check("r12a STAB-TRUE builds nothing decisive", REFUSAL_CALLS == 0)
    t_check("W-CL R60 fires, signed permutation does not", wcl_spectrum_fires(R60)
            and not wcl_spectrum_fires(_fm(P_SWAP)))


def self_test():
    del SELFTEST_LOG[:]
    t_misc()
    t_decide_paths()
    t_mutations()
    t_mguard_checker()
    sec = fixture_section()
    for n, c in sec["controls"].items():
        t_check("fixture control " + n, c["green"])
    for n, r in sec["fixtures"].items():
        if "as_expected" in r:
            t_check("fixture expectation " + n, r["as_expected"])
    fm = fixture_measurements()
    t_check("M-MODE fixture output is decision-invalid", fm["mode"] == "fixture" and fm["complete"] is False
            and fm["B"]["fragments"][0]["lp"] == PLACEHOLDER)
    t_check("only the direct refusal counted in self-tests", REFUSAL_CALLS == 1)
    bad = [n for n, okv in SELFTEST_LOG if not okv]
    lines = ["%s %s" % ("PASS" if okv else "FAIL", n) for n, okv in SELFTEST_LOG]
    return (0 if not bad else 1), "\n".join(lines) + "\n%d checks, %d failed\n" % (len(SELFTEST_LOG), len(bad))


# ------------------------------------------------------------------------------------------------------------
# The entry
# ------------------------------------------------------------------------------------------------------------
def s_entry(argv, environ):
    """The default entry: (exit status, output text)."""
    if "--self-test" in argv:
        return self_test()
    if "--stress" in argv:
        if not isinstance(S_MAX, int) or S_MAX < 1:
            return 4, ""
        return 0, canonical(stress_output())
    dsha = None
    if "--dispatch-sha" in argv:
        i = argv.index("--dispatch-sha")
        dsha = argv[i + 1] if i + 1 < len(argv) else ""
        if len(dsha) != 40 or any(ch not in HEX for ch in dsha):
            return 4, "refused: --dispatch-sha is not 40 lowercase hex\n"
    mode = s_mode(argv, environ)
    if mode == "refuse":
        return 4, "refused: --event is required\n"
    if mode == "fixture":
        m = fixture_measurements(dsha)
        return (3 if m["flags"]["fixture_mismatches"] else 0), canonical(m)
    m = s_decisive()
    m["parameters"]["dispatch_sha"] = dsha
    return 0, canonical(m)  # D21: complete scientific outcomes, including VOID, are evidence.


if __name__ == "__main__":
    status, text = s_entry(sys.argv, os.environ)
    sys.stdout.write(text)
    sys.exit(status)
