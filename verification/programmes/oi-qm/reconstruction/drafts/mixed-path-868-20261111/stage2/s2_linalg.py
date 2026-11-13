"""MIXED-PATH-1 Stage 2: affine rules by exact linear algebra over F_q (STAGE2-PREREG.md section 3).

Builds its neighbour operator from the site list.  Does not import the stepper.  Integers only.
"""
import itertools

import numpy as np
from scipy import sparse

ALPHA = {("R-lin", 2): 1, ("R-lin", 3): 1, ("R-lin", 5): 1, ("R-norm", 5): 2}


def alpha_table(rule, q):
    a = ALPHA[(rule, q)]
    return tuple((a * s) % q for s in range(6 * (q - 1) + 1))


def site_list(dims):
    return [s for s in itertools.product(range(dims[0]), range(dims[1]), range(dims[2]))]


def build_operator(dims):
    """Six-neighbour sum operator from the site list; repeated neighbours add (weights 2 on a side of 2)."""
    sites = site_list(dims)
    index = {s: i for i, s in enumerate(sites)}
    rows, cols = [], []
    for i, s in enumerate(sites):
        for axis in range(3):
            for d in (1, -1):
                t = list(s)
                t[axis] = (t[axis] + d) % dims[axis]
                rows.append(i)
                cols.append(index[tuple(t)])
    data = np.ones(len(rows), dtype=np.int64)
    n = len(sites)
    A = sparse.coo_matrix((data, (np.array(rows), np.array(cols))), shape=(n, n)).tocsr()
    A.sum_duplicates()
    return A, sites, index


def torus_dist(s, t, dims):
    tot = 0
    for i in range(3):
        d = abs(s[i] - t[i])
        tot += min(d, dims[i] - d)
    return tot


def solve_mod(rows, rhs, q):
    """Solve rows * x = rhs over F_q (q prime).  rows: list of lists (r x n).  Returns x or None."""
    r = len(rows)
    n = len(rows[0]) if r else 0
    M = [[v % q for v in rows[i]] + [rhs[i] % q] for i in range(r)]
    piv = []
    rr = 0
    for c in range(n):
        if rr >= r:
            break
        pr = None
        for i in range(rr, r):
            if M[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        M[rr], M[pr] = M[pr], M[rr]
        inv = pow(M[rr][c], q - 2, q)
        M[rr] = [(v * inv) % q for v in M[rr]]
        for i in range(r):
            if i != rr and M[i][c] != 0:
                f = M[i][c]
                M[i] = [(vi - f * vr) % q for vi, vr in zip(M[i], M[rr])]
        piv.append(c)
        rr += 1
    for i in range(rr, r):
        if M[i][n] != 0:
            return None
    x = [0] * n
    for i, c in enumerate(piv):
        x[c] = M[i][n]
    return x


def check_mod(rows, x, rhs, q):
    """Separate exact check of rows * x = rhs over F_q."""
    for i in range(len(rows)):
        if sum(a * b for a, b in zip(rows[i], x)) % q != rhs[i] % q:
            return False
    return True


def analyse(op, dims, q, alpha, gA, gB, partition, slice_, ks):
    """Wing type S (record at the generator site).  Returns per-window dependence, masking and
    Theorem-L data, and the cone-lemma counts of the full-field response (control C1)."""
    A, sites, index = op
    n = len(sites)
    At = A.T.tocsr()
    par = np.array([(s[0] + s[1] + s[2]) % 2 for s in sites], dtype=np.int64)
    p = 0 if slice_ == "u" else 1
    iA, iB = index[gA], index[gB]
    wing = np.zeros(n, dtype=bool)
    wing[iA] = True
    wing[iB] = True
    if partition == "cb3":
        hid_site = par == 1
    elif partition == "reg":
        hid_site = ~wing
    elif partition in ("cb4", "hor"):
        hid_site = np.zeros(n, dtype=bool)
    else:
        raise ValueError(partition)
    hid_u = np.flatnonzero(hid_site & (par == p))        # u_0 coordinates of the class, hidden
    hid_v = np.flatnonzero(hid_site & (par == 1 - p))    # v_0 coordinates of the class, hidden
    kmax = max(ks)

    def functionals(ir):
        w = [np.zeros(n, dtype=np.int64)]
        w[0][ir] = 1
        prev = np.zeros(n, dtype=np.int64)
        for t in range(kmax):
            nxt = (alpha * (At @ w[-1]) - prev) % q
            prev = w[-1]
            w.append(nxt)
        return w

    def coeff(w, t, sl, idx):
        if sl == "u":
            return w[t][idx] % q
        return (-w[t - 1][idx]) % q

    out = {"windows": [], "c1": {}}
    fn = {"A": functionals(iA), "B": functionals(iB)}
    remote = {"A": iB, "B": iA}
    for k in ks:
        ticks = [t for t in range(1, k + 1) if (t + p) % 2 == 0]
        ent = {"k": k, "ticks": ticks}
        for wname in ("A", "B"):
            w = fn[wname]
            col = [int(coeff(w, t, slice_, remote[wname])) for t in ticks]
            rows_u = [coeff(w, t, "u", hid_u) for t in ticks]
            rows_v = [coeff(w, t, "v", hid_v) for t in ticks]
            nzu = np.flatnonzero(np.any(np.array(rows_u) != 0, axis=0)) if len(hid_u) else np.array([], dtype=np.intp)
            nzv = np.flatnonzero(np.any(np.array(rows_v) != 0, axis=0)) if len(hid_v) else np.array([], dtype=np.intp)
            rows = [[int(x) for x in rows_u[i][nzu]] + [int(x) for x in rows_v[i][nzv]]
                    for i in range(len(ticks))]
            dep = any(c != 0 for c in col)
            sol1 = solve_mod(rows, col, q)
            sig = sol1 is None
            thm = None
            if not sig:
                thm = True
                for a in range(q):
                    delta = [(a * x) % q for x in sol1]
                    if not check_mod(rows, delta, [(a * c) % q for c in col], q):
                        thm = False
            canon = []
            g0 = sites[iA]
            for j, src in ((nzu, hid_u), (nzv, hid_v)):
                sl = "u" if src is hid_u else "v"
                for cnum, jj in enumerate(j):
                    s = sites[int(src[int(jj)])]
                    disp = tuple(((s[i] - g0[i] + dims[i] // 2) % dims[i]) - dims[i] // 2 for i in range(3))
                    off = 0 if sl == "u" else len(nzu)
                    canon.append([sl, list(disp), [rows[i][off + cnum] for i in range(len(ticks))]])
            canon.sort()
            ent["dep_" + wname] = bool(dep)
            ent["sig_" + wname] = bool(sig)
            ent["thmL_" + wname] = thm
            ent["col_" + wname] = col
            ent["hidden_columns_" + wname] = canon
        out["windows"].append(ent)
    # control C1: full-field response of each setting, forward recurrence with A
    for gname, ig in (("A", iA), ("B", iB)):
        g = sites[ig]
        dist = np.array([torus_dist(g, s, dims) for s in sites], dtype=np.int64)
        u = np.zeros(n, dtype=np.int64)
        v = np.zeros(n, dtype=np.int64)
        if slice_ == "u":
            u[ig] = 1
        else:
            v[ig] = 1
        pairs = 0
        viol = 0
        for t in range(1, kmax + 1):
            u, v = (alpha * (A @ u) - v) % q, u
            m = ((par + 0) % 2 == (t + p) % 2) & (dist > t)
            pairs += int(m.sum())
            viol += int(np.count_nonzero(u[m]))
        out["c1"][gname] = {"pairs": pairs, "violations": viol}
    out["hidden_dimension"] = int(len(hid_u) + len(hid_v))
    return out
