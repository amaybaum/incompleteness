#!/usr/bin/env python3
"""K1-P1-1, implementation B: exact enumeration of the P1 stage of K1-RDY-1.

Header (preregistration section 8.1)
- Round K1-P1-1. Control plane:
  verification/programmes/oi-qm/reconstruction/round-k1-p1-1/preregistration.md at
  4ca431afb1bfee0cdf301f0917c73068fdf09b58 (PR #1135). Adopted text: K1-RDY-1's control plane at
  d9b3de012e393262adb20f91ad49627bad48de43, the files of the preregistration's section 2 table.
- Author session: writer-k1p1-impl-b (hand-off name writer-k1p1-implB), Claude Code session
  https://claude.ai/code/session_011zDyUSyEszk3JJx83uXKKq. Drafted pre-F under owner
  authorization #1031 comment 6677496553 (Stage 2, pre-F code drafting).
- Access to another implementation: none. The writer read neither implementation A nor
  controls.py, nor any branch holding them, before this file was delivered.
- Shared dependency: none. Python 3.11 standard library only: fractions, json, hashlib, sys, os.

Method (section 8.2). A state is a 10-bit integer whose bits, most significant first, are the
cells x_0, ..., x_4, y_0, ..., y_4 (A2's order), so integer order is A2's lexicographic order.
phi and phi^-1 are 10x10 matrices over F_2, built from their definitions and applied by
matrix-vector products. E is read from the V-rows of the matrix powers M^t. S is partitioned
into orbits by minimum-label propagation along phi. The second cycle count (CC-CYC2) is
computed from the F_2 ranks of M^k - I and enumerates no state.

Arithmetic is on int and fractions.Fraction only; the code contains no true division operator
and no float (section 7).

Command line (section 10.1), from the repository root:
  python3 -I verification/lean/k1p1_enum_b.py --stage {members|rows|final} --record <rec>
      --out <out> [--members-sha256 <hex>]

Exit status: 0 the files are written; 2 a refusal (a stage precondition, or CT-INC);
3 the exactness guard; 4 a case the preregistration does not settle (stop condition H7);
any other nonzero status is a failure. Nothing is written on a nonzero exit.
"""

import hashlib
import json
import os
import sys
from fractions import Fraction

# ----------------------------------------------------------------------------------------------
# Instance and fixed constants (preregistration section 5; K lines 31-35 and section 6)

N = 5
Q = 2
A_PARAM = 1
D_PARAM = 1
T_WINDOW = 1
INSTANCE = {"N": N, "a": A_PARAM, "d": D_PARAM, "q": Q}
V_CELL = ("y", 1)                      # V = site 1, current slice: V_t = y_1(t)
SIGMA_CELLS = (("x", 0), ("y", 0))     # Sigma = site 0, both slices
N_CC_IMP2 = 6                          # CC-IMP'' alone uses (N, q, a) = (6, 2, 1)
K_MAX_CYC2 = 10                        # CC-CYC2: k = 1, ..., 10
M10_POWER = 10                         # CC-CYC2: M^10 = I
EPSILON_CC_EXACT = Fraction(1, 20)

BRANCHES = ("B-pl", "B-eq", "B-ct")
W_RULE = {
    "B-pl": "W trivial; t_u = t_0",
    "B-eq": "W_eq: site set of V, both slices; t_u = t_0",
    "B-ct": "W_eq: site set of V, both slices; t_u = t_0 - 1",
}
W_INPUTS = {"B-pl": [], "B-eq": ["V"], "B-ct": ["V"]}

H_INV = "H-inv[K-17(a)]"
H_CUR = "H-cur (declared)"
H_2S = "H-2s (declared)"
H_RET = "H-ret"
H_LAW = "H-law"
H_SEL = "H-sel"
H_MU = "H-μ"
FINITE_S = "finite-S posit"
PI0_NAME = "π_0"
CLASS_NAME = "\U0001d4d8"
NOT_REACHED = "not-reached"
PENDING = "pending"

CELL_ORDER_N5 = ["x_0", "x_1", "x_2", "x_3", "x_4", "y_0", "y_1", "y_2", "y_3", "y_4"]

S0_PAPER_IDS = ("CC-LEDGER", "CC-IMP", "CC-IMP′", "CC-IMP″", "CC-PASS", "CC-T2")
CLASS_DERIVATIONS = ["derivations/P1-class-paper.md", "derivations/S0-paper.md"]

# The eleven S0 controls in K section 6's order, with K section 6's "Gate under test" text.
CONTROL_GATES = (
    ("CC-ABS", "G4"),
    ("CC-EXACT", "G4"),
    ("CC-SCOPE", "G4"),
    ("CC-LEDGER", "G3/G4"),
    ("CC-IMP", "G2, G3"),
    ("CC-IMP′", "G2(a)"),
    ("CC-IMP″", "G2(a); T1; T2's no-image disjunct"),
    ("CC-PASS", "G2(b)"),
    ("CC-T2", "G2(b) T2"),
    ("POS-X", "G3, G4, G7"),
    ("CC-BLIND", "G4"),
)

# Expected values of the computed parts (preregistration section 10.2).
POS_X_TOKEN = ("CONDITIONAL[H-2s (declared), H-cur (declared), H-ret, H-μ, "
               "finite-S posit]")
CONTROL_EXPECTED = {
    "CC-ABS": {"sharp_w": [], "weak": {"00": "1/8", "01": "1/8", "10": "1/8", "11": "1/8"}},
    "CC-EXACT": {"sharp_w": [], "weak": {"": "153/160"}},
    "CC-SCOPE": {
        "B-ct": {"nb_all_false": True, "sharp": True},
        "B-eq": {"nb_all_false": True, "sharp": True},
        "B-pl": {"nb_all_false": True, "sharp": True},
    },
    "CC-LEDGER": {"c1": False, "d_ratio": "2/1", "shell_size": 512},
    "CC-IMP": {"d_ratio": "8/1", "support_size": 128},
    "CC-IMP′": None,
    "CC-IMP″": {"fixes_x2_zero": True},
    "CC-PASS": {
        "hsel_content": {"B-eq": [], "B-pl": [{"values": ["000", "001", "110", "111"], "w": ""}]},
        "image_equals_stated": True,
    },
    "CC-T2": {"image_equals_stated": False},
    "POS-X": {"g3_void": False, "mass_w0": "1/64", "nb_w0": True, "sharp_w0": True,
              "token": POS_X_TOKEN, "w_certified": True},
    "CC-BLIND": {"mass_w0": "1/256", "nb_w0": False, "sharp_w0": True},
}
# Positions of rationals inside each control's computed and expected objects (exactness guard).
CONTROL_RATIONAL_KEYS = {
    "CC-ABS": ("weak",), "CC-EXACT": ("weak",), "CC-LEDGER": ("d_ratio",),
    "CC-IMP": ("d_ratio",), "POS-X": ("mass_w0",), "CC-BLIND": ("mass_w0",),
}

EXIT_OK = 0
EXIT_REFUSE = 2
EXIT_EXACT = 3
EXIT_UNSETTLED = 4


class Refusal(Exception):
    """A stage precondition or CT-INC does not hold: exit 2, nothing written."""


class Unsettled(Exception):
    """A case the preregistration does not settle (H7): exit 4, nothing written."""


# ----------------------------------------------------------------------------------------------
# Exact helpers

def ratio(num, den):
    """The exact quotient num/den of ints or Fractions, as a Fraction (no true division)."""
    num = Fraction(num)
    den = Fraction(den)
    if den == 0:
        raise ZeroDivisionError("ratio with zero denominator")
    return Fraction(num.numerator * den.denominator, num.denominator * den.numerator)


def fmt(value):
    """Section 7: a rational as "p/q" in lowest terms with q > 0; zero is "0/1"."""
    f = Fraction(value)
    return "%d/%d" % (f.numerator, f.denominator)


def is_canonical_rational(text):
    """True iff text is "p/q" with q > 0, both decimal without leading zeros, in lowest terms."""
    if not isinstance(text, str) or text.count("/") != 1:
        return False
    p_text, q_text = text.split("/")
    digits = "0123456789"
    negative = p_text.startswith("-")
    p_digits = p_text[1:] if negative else p_text
    for part in (p_digits, q_text):
        if part == "" or any(ch not in digits for ch in part):
            return False
        if len(part) > 1 and part[0] == "0":
            return False
    if negative and p_digits == "0":
        return False
    p_val = int(p_text)
    q_val = int(q_text)
    if q_val <= 0:
        return False
    f = Fraction(p_val, q_val)
    return f.numerator == p_val and f.denominator == q_val


def frac_sum(values):
    total = Fraction(0)
    for v in values:
        total = total + v
    return total


def mobius(n):
    result = 1
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            m = m // p
            if m % p == 0:
                return 0
            result = -result
        p += 1
    if m > 1:
        result = -result
    return result


# ----------------------------------------------------------------------------------------------
# Cells, states and values (A2's cell order; a state is an integer, cell 0 the top bit)

def cell_index(n, slice_name, site):
    return (0 if slice_name == "x" else n) + (site % n)


def cell_name(n, index):
    return ("x_%d" % index) if index < n else ("y_%d" % (index - n))


def cell_mask(nc, index):
    return 1 << (nc - 1 - index)


def cell_bit(nc, v, index):
    return (v >> (nc - 1 - index)) & 1


def state_string(nc, v):
    return format(v, "0%db" % nc)


def value_string(nc, v, cells):
    """The value of cell set `cells` (in A2's order) at state v, as a string of 0 and 1."""
    return "".join("1" if cell_bit(nc, v, i) else "0" for i in cells)


def all_values(k):
    """All strings over {0,1} of length k, in lexicographic order ("" when k = 0)."""
    if k == 0:
        return [""]
    return [format(j, "0%db" % k) for j in range(2 ** k)]


# ----------------------------------------------------------------------------------------------
# Matrices over F_2: a matrix is the list of its rows, each row a bit mask over the cells

def _add_coefficient(coeffs, j, c):
    coeffs[j] = coeffs.get(j, 0) + c


def phi_coefficients(n):
    """phi(x, y) = (y, Ay - x), (Ay)_i = y_{i-1} + y_{i+1}: per output cell, its coefficients."""
    rows = []
    for i in range(n):                      # x'_i = y_i
        c = {}
        _add_coefficient(c, cell_index(n, "y", i), 1)
        rows.append(c)
    for i in range(n):                      # y'_i = y_{i-1} + y_{i+1} - x_i
        c = {}
        _add_coefficient(c, cell_index(n, "y", i - 1), 1)
        _add_coefficient(c, cell_index(n, "y", i + 1), 1)
        _add_coefficient(c, cell_index(n, "x", i), -1)
        rows.append(c)
    return rows


def phi_inverse_coefficients(n):
    """phi^-1(x, y) = (Ax - y, x): per output cell, its coefficients."""
    rows = []
    for i in range(n):                      # x''_i = x_{i-1} + x_{i+1} - y_i
        c = {}
        _add_coefficient(c, cell_index(n, "x", i - 1), 1)
        _add_coefficient(c, cell_index(n, "x", i + 1), 1)
        _add_coefficient(c, cell_index(n, "y", i), -1)
        rows.append(c)
    for i in range(n):                      # y''_i = x_i
        c = {}
        _add_coefficient(c, cell_index(n, "x", i), 1)
        rows.append(c)
    return rows


def f2_matrix(coeff_rows, nc, q):
    if q != 2:
        raise ValueError("implementation B represents matrices over F_2 only")
    m = []
    for row in coeff_rows:
        mask = 0
        for j, c in row.items():
            if c % q != 0:
                mask |= cell_mask(nc, j)
        m.append(mask)
    return m


def mat_identity(nc):
    return [cell_mask(nc, i) for i in range(nc)]


def mat_vec(m, v, nc):
    out = 0
    for i in range(nc):
        if (m[i] & v).bit_count() & 1:
            out |= cell_mask(nc, i)
    return out


def mat_mul(a, b, nc):
    """(a b): row i is the F_2 sum of the rows j of b with a_ij = 1."""
    c = []
    for i in range(nc):
        r = 0
        for j in range(nc):
            if a[i] & cell_mask(nc, j):
                r ^= b[j]
        c.append(r)
    return c


def mat_pow(m, k, nc):
    r = mat_identity(nc)
    for _ in range(k):
        r = mat_mul(m, r, nc)
    return r


def row_support(m, nc, i):
    return [j for j in range(nc) if m[i] & cell_mask(nc, j)]


def rank_f2(rows, ncols):
    """Rank over F_2 of the matrix whose rows are bit masks over ncols columns."""
    rows = list(rows)
    rank = 0
    for col in range(ncols):
        bit = 1 << (ncols - 1 - col)
        pivot = None
        for k in range(rank, len(rows)):
            if rows[k] & bit:
                pivot = k
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for k in range(len(rows)):
            if k != rank and rows[k] & bit:
                rows[k] ^= rows[rank]
        rank += 1
    return rank


# ----------------------------------------------------------------------------------------------
# Orbits: minimum-label propagation

def orbit_partition(perm):
    """Partition {0, ..., n-1} into the orbits of perm by minimum-label propagation.

    After k rounds label(s) = min{s, perm(s), ..., perm^k(s)}; the rounds stop when no label
    changes. States are grouped by label. Returns (cycles, ok): cycles lists (least, states)
    by least state, states increasing; ok holds iff every group contains its label as its least
    state, is closed under perm, and is a single orbit of length |group| from its least state.
    """
    n = len(perm)
    label = list(range(n))
    stable = False
    for _ in range(n + 1):
        new = [label[s] if label[s] <= label[perm[s]] else label[perm[s]] for s in range(n)]
        if new == label:
            stable = True
            break
        label = new
    if not stable:
        raise RuntimeError("orbit labels did not stabilize")
    groups = {}
    for s in range(n):
        groups.setdefault(label[s], []).append(s)
    cycles = []
    ok = True
    for least in sorted(groups):
        states = groups[least]
        members = set(states)
        if states[0] != least:
            ok = False
        if {perm[s] for s in states} != members:
            ok = False
        seen = []
        t = least
        for _ in range(len(states)):
            seen.append(t)
            t = perm[t]
        if t != least or len(set(seen)) != len(states) or set(seen) != members:
            ok = False
        cycles.append((least, states))
    return cycles, ok


# ----------------------------------------------------------------------------------------------
# The instance

def energy(n, nc, v, q):
    """E(x, y) = <x, x> + <y, y> - <x, Ay> mod q."""
    x = [cell_bit(nc, v, cell_index(n, "x", i)) for i in range(n)]
    y = [cell_bit(nc, v, cell_index(n, "y", i)) for i in range(n)]
    xx = sum(x[i] * x[i] for i in range(n))
    yy = sum(y[i] * y[i] for i in range(n))
    xay = sum(x[i] * (y[(i - 1) % n] + y[(i + 1) % n]) for i in range(n))
    return (xx + yy - xay) % q


def dependency_region(m, nc, n, window):
    """R0: cells outside Sigma with a nonzero coefficient in V(t_0 + t), 0 <= t <= T."""
    v = cell_index(n, V_CELL[0], V_CELL[1])
    sigma = {cell_index(n, sl, site) for sl, site in SIGMA_CELLS}
    cells = set()
    mt = mat_identity(nc)
    for _ in range(window + 1):
        cells.update(row_support(mt, nc, v))
        mt = mat_mul(m, mt, nc)
    return sorted(cells - sigma)


def access_labels(n, w_cells, tu):
    """Section 2's access labels for V and W, in the order of the token strings."""
    labels = [H_CUR]
    if any(c < n for c in w_cells):
        labels.append(H_2S)
    if tu < 0:
        labels.append(H_RET)
    return labels


def branch_tables(inst, cells, tu):
    """W_{t_u}(s) at every state, |B_w|, |B_w ∩ Z|, J_w, and W-certification (R0, R4)."""
    S = inst["S"]
    nc = inst["nc"]
    wv = []
    for s in S:
        t = s
        for _ in range(-tu):
            t = inst["phiinv"][t]
        wv.append(value_string(nc, t, cells))
    size, zsize, jset = {}, {}, {}
    for s in S:
        w = wv[s]
        size[w] = size.get(w, 0) + 1
        zsize[w] = zsize.get(w, 0) + (1 if inst["z"][s] else 0)
        jset.setdefault(w, set()).add(inst["e_val"][s])
    certified = all(zsize[w] == 0 or zsize[w] == size[w] for w in size)
    return {"cells": list(cells), "tu": tu, "wv": wv, "size": size, "zsize": zsize,
            "jset": jset, "certified": certified, "values": all_values(len(cells))}


def build_instance():
    nc = 2 * N
    S = list(range(2 ** nc))                                   # M1, lexicographic order
    m = f2_matrix(phi_coefficients(N), nc, Q)
    minv = f2_matrix(phi_inverse_coefficients(N), nc, Q)
    phi = [mat_vec(m, s, nc) for s in S]                       # M2
    phiinv = [mat_vec(minv, s, nc) for s in S]
    inst = {"nc": nc, "S": S, "M": m, "Minv": minv, "phi": phi, "phiinv": phiinv}
    inst["distinct"] = len({state_string(nc, s) for s in S}) == len(S)
    inst["bijection"] = (all(phiinv[phi[s]] == s for s in S)
                         and all(phi[phiinv[s]] == s for s in S)
                         and set(phi) == set(S))
    E = dependency_region(m, nc, N, T_WINDOW)                  # R0
    v_site = V_CELL[1]
    w_eq = sorted([cell_index(N, "x", v_site), cell_index(N, "y", v_site)])
    sigma_cells = sorted(cell_index(N, sl, site) for sl, site in SIGMA_CELLS)
    v_index = cell_index(N, V_CELL[0], V_CELL[1])
    inst["E"] = E
    inst["W_eq"] = w_eq
    inst["e_val"] = [value_string(nc, s, E) for s in S]
    inst["z"] = [all(cell_bit(nc, s, i) == 0 for i in E) for s in S]
    inst["sigma"] = [value_string(nc, s, sigma_cells) for s in S]
    readout = []
    for s in S:
        parts = []
        t = s
        for _ in range(T_WINDOW + 1):
            parts.append(value_string(nc, t, [v_index]))
            t = phi[t]
        readout.append("".join(parts))
    inst["readout"] = readout
    inst["readout_values"] = all_values(T_WINDOW + 1)
    inst["energy"] = [energy(N, nc, s, Q) for s in S]
    inst["branch"] = {}
    for b in BRANCHES:
        cells = [] if b == "B-pl" else w_eq
        tu = -1 if b == "B-ct" else 0
        bt = branch_tables(inst, cells, tu)
        bt["access"] = access_labels(N, cells, tu)
        inst["branch"][b] = bt
    return inst


# ----------------------------------------------------------------------------------------------
# Stage M: members

def compute_members(inst):
    S = inst["S"]
    nc = inst["nc"]
    cycles, cycles_ok = orbit_partition(inst["phi"])
    length_sum = sum(len(states) for _, states in cycles)
    assigned = sorted(s for _, states in cycles for s in states)
    partition = cycles_ok and length_sum == len(S) and assigned == S
    members = [{"key": "pi0", "name": PI0_NAME, "support": list(S), "is_uc": False}]
    for least, states in cycles:
        key = state_string(nc, least)
        members.append({"key": key, "name": "u_c[%s]" % key, "support": list(states),
                        "is_uc": True})
    histogram = {}
    for _, states in cycles:
        histogram[str(len(states))] = histogram.get(str(len(states)), 0) + 1
    out_members = [{"key": "pi0", "size": len(S)}]
    for mem in members[1:]:
        out_members.append({"key": mem["key"], "size": len(mem["support"]),
                            "states": [state_string(nc, s) for s in mem["support"]]})
    members_obj = {"schema": "k1p1-members", "version": 1, "cell_order": list(CELL_ORDER_N5),
                   "members": out_members, "histogram": histogram}
    completeness = {"states": len(S), "length_sum": length_sum, "cycles": len(cycles),
                    "distinct": inst["distinct"], "bijection": inst["bijection"],
                    "partition": partition, "mass_sums": None}
    return members, members_obj, completeness


def compute_cyc2(inst):
    """CC-CYC2 from F_2 ranks: |Fix(phi^k)| = 2^(10 - rank(M^k - I)); no state is enumerated."""
    nc = inst["nc"]
    m = inst["M"]
    ident = mat_identity(nc)
    fix = {}
    mk = ident
    for k in range(1, K_MAX_CYC2 + 1):
        mk = mat_mul(m, mk, nc)
        r = rank_f2([mk[i] ^ ident[i] for i in range(nc)], nc)
        fix[k] = Q ** (nc - r)
    period, cycles = {}, {}
    for d in range(1, K_MAX_CYC2 + 1):
        p = sum(mobius(d // e) * fix[e] for e in range(1, d + 1) if d % e == 0)
        if p % d != 0:
            raise RuntimeError("states of exact period %d not divisible by %d" % (d, d))
        period[d] = p
        cycles[d] = p // d
    return {"schema": "k1p1-cyc2", "version": 1,
            "fix": {str(k): fix[k] for k in fix},
            "period_states": {str(d): period[d] for d in period},
            "cycles": {str(d): cycles[d] for d in cycles},
            "m10_identity": mat_pow(m, M10_POWER, nc) == ident}


def compute_preserved(inst):
    S = inst["S"]
    nc = inst["nc"]
    en = inst["energy"]
    conserved = all(en[inst["phi"][s]] == en[s] for s in S)
    shells = {str(c): sum(1 for s in S if en[s] == c) for c in range(Q)}
    ident = mat_identity(nc)
    order = None
    mk = ident
    for k in range(1, 2 ** nc + 1):
        mk = mat_mul(inst["M"], mk, nc)
        if mk == ident:
            order = k
            break
    if order is None:
        raise RuntimeError("no k <= 2^(2N) with M^k = I")
    return {"energy_conserved": conserved, "shell_sizes": shells, "phi_order": order}


def compute_region(inst):
    nc = inst["nc"]
    E = inst["E"]
    overlap, tautological = {}, {}
    for b in ("B-eq", "B-ct"):
        bt = inst["branch"][b]
        cells = sorted(set(bt["cells"]) & set(E)) if bt["tu"] == 0 else []
        overlap[b] = [cell_name(N, i) for i in cells]
        tautological[b] = len(cells) > 0
    return {"E": [cell_name(N, i) for i in E], "W_eq": [cell_name(N, i) for i in inst["W_eq"]],
            "q_pow_minus_E": fmt(Fraction(1, Q ** len(E))), "overlap": overlap,
            "overlap_tautological": tautological}


# ----------------------------------------------------------------------------------------------
# Readiness, NB and H-sel content for a uniform measure on `support` (R1-R5)

def measure(inst, bt, support):
    """R2 for the uniform measure on support: mass, weak, pi_0 reference, sharp values."""
    n_m = len(support)
    states_by_w = {}
    for s in support:
        states_by_w.setdefault(bt["wv"][s], []).append(s)
    mass, weak, ref = {}, {}, {}
    for w in bt["values"]:
        states = states_by_w.get(w, [])
        if not states:
            continue
        mass[w] = Fraction(len(states), n_m)
        weak[w] = Fraction(sum(1 for s in states if inst["z"][s]), len(states))
        ref[w] = Fraction(bt["zsize"][w], bt["size"][w])
    sharp = sorted(w for w in mass if weak[w] == 1)
    return {"mass": mass, "weak": weak, "ref": ref, "sharp": sharp, "states_by_w": states_by_w,
            "mass_sum_ok": frac_sum(mass.values()) == 1}


def nb_record(inst, states):
    """R3 for nu uniform on `states`: NB(nu), the usefulness lists, and CC-MASS's sums for nu."""
    total = len(states)
    groups = {}
    for s in states:
        g = groups.setdefault(inst["sigma"][s], {})
        r = inst["readout"][s]
        g[r] = g.get(r, 0) + 1
    sigmas = sorted(groups)
    nu, laws = {}, {}
    for sg in sigmas:
        n_sg = sum(groups[sg].values())
        nu[sg] = Fraction(n_sg, total)
        laws[sg] = {r: Fraction(groups[sg].get(r, 0), n_sg) for r in inst["readout_values"]}
    sums_ok = (frac_sum(nu.values()) == 1
               and all(frac_sum(laws[sg].values()) == 1 for sg in sigmas))
    nb = False
    disjoint, law_only = [], []
    for i in range(len(sigmas)):
        for j in range(i + 1, len(sigmas)):
            s1, s2 = sigmas[i], sigmas[j]
            if laws[s1] == laws[s2]:
                continue
            nb = True
            supp1 = {r for r in laws[s1] if laws[s1][r] > 0}
            supp2 = {r for r in laws[s2] if laws[s2][r] > 0}
            if supp1 & supp2:
                law_only.append([s1, s2])
            else:
                disjoint.append([s1, s2])
    return nb, {"disjoint": sorted(disjoint), "law_only": sorted(law_only)}, sums_ok


def hsel_content(inst, bt, support):
    """R5 (RD-5): for each positive-mass w, I_w's E-values when I_w is a proper subset of J_w."""
    i_sets = {}
    for s in support:
        i_sets.setdefault(bt["wv"][s], set()).add(inst["e_val"][s])
    out = []
    for w in bt["values"]:
        if w not in i_sets:
            continue
        if i_sets[w] < bt["jset"][w]:
            out.append({"values": sorted(i_sets[w]), "w": w})
    return out


# ----------------------------------------------------------------------------------------------
# S0 controls (preregistration section 11.1; K section 6)

def control_token_cross_time_pi0(inst, bt, meas, declaration_hypotheses):
    """G4 to G7 for pi_0 under a cross-time fixture region (POS-X): no bound, no rule part."""
    access = bt["access"]
    if not meas["sharp"]:
        return "ABSENT[%s; B-ct; %s]" % (PI0_NAME, ", ".join(access))
    nbs = [nb_record(inst, meas["states_by_w"][w])[0] for w in meas["sharp"]]
    if not any(nbs):
        return "BLIND[%s; B-ct; %s]" % (PI0_NAME, ", ".join(access))
    lam = set(declaration_hypotheses) | set(access)
    if not bt["certified"]:
        lam.add(H_LAW)
    return "CONDITIONAL[%s]" % ", ".join(sorted(lam))


def compute_controls(inst, cd):
    S = inst["S"]
    nc = inst["nc"]
    E = inst["E"]
    z = inst["z"]
    computed = {}

    # CC-ABS: pi_0, W = {x_3, y_3}, equal time.
    bt_abs = branch_tables(inst, sorted([cell_index(N, "x", 3), cell_index(N, "y", 3)]), 0)
    meas = measure(inst, bt_abs, S)
    computed["CC-ABS"] = {"sharp_w": meas["sharp"],
                          "weak": {w: fmt(meas["weak"][w]) for w in meas["weak"]}}

    # CC-EXACT: (1 - eps) mu_Q + eps pi_0, mu_Q uniform on {E = 0}; B-pl.
    n_z = sum(1 for s in S if z[s])
    mu = [(1 - EPSILON_CC_EXACT) * (Fraction(1, n_z) if z[s] else Fraction(0))
          + EPSILON_CC_EXACT * Fraction(1, len(S)) for s in S]
    mass_all = frac_sum(mu)
    weak_exact = ratio(frac_sum(mu[s] for s in S if z[s]), mass_all)
    computed["CC-EXACT"] = {"sharp_w": [""] if weak_exact == 1 else [],
                            "weak": {"": fmt(weak_exact)}}

    # CC-SCOPE: delta_0 (the fixed point 0) in each branch.
    scope = {}
    for b in BRANCHES:
        meas = measure(inst, inst["branch"][b], [0])
        nbs = [nb_record(inst, meas["states_by_w"][w])[0] for w in meas["sharp"]]
        scope[b] = {"nb_all_false": all(not x for x in nbs), "sharp": len(meas["sharp"]) > 0}
    computed["CC-SCOPE"] = scope

    # CC-LEDGER: pi_0( . | E = 0), the energy shell; asserted B-pl readiness against (c1).
    shell = [s for s in S if inst["energy"][s] == 0]
    computed["CC-LEDGER"] = {"c1": Q ** len(E) * len(shell) <= len(S),
                             "d_ratio": fmt(Fraction(len(S), len(shell))),
                             "shell_size": len(shell)}

    # CC-IMP: mu_Q = delta_0 on E's cells (x) pi_0 elsewhere.
    computed["CC-IMP"] = {"d_ratio": fmt(Fraction(len(S), n_z)), "support_size": n_z}

    # CC-IMP': paper only.
    computed["CC-IMP′"] = None

    # CC-IMP'': N = 6; W = sites {0, 1}, both slices; O = "W = 0 over [t_u - 1, t_u]", t_u = t_0.
    n6 = N_CC_IMP2
    nc6 = 2 * n6
    minv6 = f2_matrix(phi_inverse_coefficients(n6), nc6, Q)
    w6_mask = 0
    for site in (0, 1):
        for sl in ("x", "y"):
            w6_mask |= cell_mask(nc6, cell_index(n6, sl, site))
    x2 = cell_index(n6, "x", 2)
    event = [s for s in range(2 ** nc6)
             if s & w6_mask == 0 and mat_vec(minv6, s, nc6) & w6_mask == 0]
    computed["CC-IMP″"] = {"fixes_x2_zero": len(event) > 0
                                and all(cell_bit(nc6, s, x2) == 0 for s in event)}

    # CC-PASS and CC-T2: O_1 = "W's configuration identical at t_u - 1 and t_u", W = W_eq.
    w_eq = inst["W_eq"]
    image = [s for s in S
             if value_string(nc, s, w_eq) == value_string(nc, inst["phiinv"][s], w_eq)]

    def parity_zero(s, cells):
        return sum(cell_bit(nc, s, i) for i in cells) % 2 == 0

    x0, x1, x2n = (cell_index(N, "x", i) for i in (0, 1, 2))
    y1 = cell_index(N, "y", 1)
    stated_pass = {s for s in S if parity_zero(s, [x1, y1]) and parity_zero(s, [x0, x2n])}
    stated_t2 = {s for s in S if parity_zero(s, [x1, y1])}
    pass_equal = set(image) == stated_pass
    if pass_equal:
        content = {"B-eq": hsel_content(inst, inst["branch"]["B-eq"], image),
                   "B-pl": hsel_content(inst, inst["branch"]["B-pl"], image)}
    else:
        content = {"B-eq": [], "B-pl": []}
    computed["CC-PASS"] = {"hsel_content": content, "image_equals_stated": pass_equal}
    computed["CC-T2"] = {"image_equals_stated": set(image) == stated_t2}

    # POS-X: pi_0, cross time, W = W_ct := E's one-tick dependency set, t_u = t_0 - 1.
    w_ct = sorted({j for e in E for j in row_support(inst["M"], nc, e)})
    bt_ct = branch_tables(inst, w_ct, -1)
    bt_ct["access"] = access_labels(N, w_ct, -1)
    meas = measure(inst, bt_ct, S)
    w0 = "0" * len(w_ct)
    states_w0 = meas["states_by_w"].get(w0, [])
    computed["POS-X"] = {
        "g3_void": False if bt_ct["tu"] < 0 else None,   # cross time: no D bound (K line 62)
        "mass_w0": fmt(Fraction(bt_ct["size"].get(w0, 0), len(S))),
        "nb_w0": nb_record(inst, states_w0)[0] if states_w0 else False,
        "sharp_w0": w0 in meas["sharp"],
        "token": control_token_cross_time_pi0(inst, bt_ct, meas, [H_MU, FINITE_S]),
        "w_certified": bt_ct["certified"],
    }

    # CC-BLIND: POS-X with W_ct ∪ {y_4, x_0} at t_u.
    w_bl = sorted(set(w_ct) | {cell_index(N, "y", 4), cell_index(N, "x", 0)})
    bt_bl = branch_tables(inst, w_bl, -1)
    meas = measure(inst, bt_bl, S)
    w0 = "0" * len(w_bl)
    states_w0 = meas["states_by_w"].get(w0, [])
    computed["CC-BLIND"] = {
        "mass_w0": fmt(Fraction(bt_bl["size"].get(w0, 0), len(S))),
        "nb_w0": nb_record(inst, states_w0)[0] if states_w0 else False,
        "sharp_w0": w0 in meas["sharp"],
    }

    controls = []
    for cid, gate in CONTROL_GATES:
        paper = cd["s0_paper"][cid] if cid in S0_PAPER_IDS else None
        comp = computed[cid]
        exp = CONTROL_EXPECTED[cid]
        same = canonical_json(comp) == canonical_json(exp)
        outcome = "pass" if same and (paper is None or paper == "pass") else "fail"
        controls.append({"id": cid, "gate": gate, "computed": comp, "expected": exp,
                         "paper": paper, "outcome": outcome})
    return controls


# ----------------------------------------------------------------------------------------------
# Stage R: rows (R1-R10)

def g2_decision(cd, is_uc):
    """G2(a) and T1 from class-decisions.json for a row (R5a). Returns (a_flag, t1_flag, undecided)."""
    sources = [cd["class_rule"]]
    if is_uc:
        sources.append(cd["support_restriction"])
    a_flag = any(src["a"] == "flag" for src in sources)
    t1_flag = any(src["t1"] == "flag" for src in sources)
    undecided = any(src["a"] == "undecided" or src["t1"] == "undecided" for src in sources)
    return a_flag, t1_flag, undecided


def rd3_hypotheses(token, access):
    """RD-3 (i): the declaration's hypotheses and the section 2 access labels the token names."""
    hyps = {H_INV}
    if token.startswith("ABSENT[") or token.startswith("BLIND["):
        hyps |= set(access)
    return sorted(hyps)


def evaluate_row(inst, b, member, cd):
    """All measured fields of one (member, branch) row, and its outcome up to G5."""
    S = inst["S"]
    E = inst["E"]
    bt = inst["branch"][b]
    support = member["support"]
    n_m = len(support)
    meas = measure(inst, bt, support)
    sums_ok = meas["mass_sum_ok"]

    nb, usefulness = {}, {}
    for w in meas["sharp"]:
        val, report, ok = nb_record(inst, meas["states_by_w"][w])
        nb[w] = val
        usefulness[w] = report
        sums_ok = sums_ok and ok
    nb_g1 = None
    if b == "B-pl":
        val, _, ok = nb_record(inst, support)
        nb_g1 = val
        sums_ok = sums_ok and ok

    # R5: T2 on the support restriction, then H-sel content.
    t2 = {inst["phi"][s] for s in support} != set(support)
    a_flag, t1_flag, g2_undecided = g2_decision(cd, member["is_uc"])
    content = [] if (t1_flag or t2) else hsel_content(inst, bt, support)

    # R6: G3.
    d_ratio = Fraction(len(S), n_m)
    d_text = "D=log(%s); " % fmt(d_ratio)
    equal_time = bt["tu"] == 0
    breaks = False
    if b == "B-pl":
        c1 = Q ** len(E) * n_m <= len(S)
        bound_ok = c1
        ledger = d_text + "(c1) |E|=%d: %s" % (len(E), "holds" if c1 else "breaks")
        breaks = len(meas["sharp"]) > 0 and not c1
    elif b == "B-eq":
        k = len(set(E) - set(bt["cells"]))
        bound_ok = {}
        parts = []
        for w in meas["sharp"]:
            p = meas["mass"][w]
            a_num, b_den = p.numerator, p.denominator
            holds = Q ** (a_num * k) * n_m ** b_den <= len(S) ** b_den
            bound_ok[w] = holds
            parts.append("w=%s p=%s k=%d: %s" % (w, fmt(p), k, "holds" if holds else "breaks"))
            breaks = breaks or not holds
        ledger = d_text + ("(c2) no sharp w" if not parts else "(c2) " + "; ".join(parts))
    else:
        bound_ok = None
        ledger = d_text + "cross time, no D bound; H-ret"

    access = bt["access"]
    gates = {"G1": None, "G2": None, "G3": NOT_REACHED, "G4": NOT_REACHED,
             "G5": NOT_REACHED, "G6": NOT_REACHED, "G7": NOT_REACHED}
    g1 = "pass" if cd["g1"] == "pass" else "UNDECIDED(G1)"
    if a_flag:
        g2 = "Z1-VOID[IMPORTED]"
    elif t1_flag or t2:
        g2 = "Z1-VOID[DYN]"
    elif g2_undecided:
        g2 = "UNDECIDED(G2)"
    else:
        g2 = "pass"
    gates["G1"] = g1
    gates["G2"] = g2
    lam = None
    candidate = None
    if g1 != "pass" or g2 != "pass":                       # R5a
        if g2.startswith("Z1-VOID"):
            token = g2
        elif g1 != "pass":
            token = g1
        else:
            token = g2
    else:
        gates["G3"] = "pass"
        name = member["name"]
        if not meas["sharp"]:                              # R7
            token = "ABSENT[%s; %s; %s]" % (name, b, ", ".join(access))
        elif equal_time and breaks:
            token = "VOID[row]"
        elif not any(nb[w] for w in meas["sharp"]):
            token = "BLIND[%s; %s; %s]" % (name, b, ", ".join(access))
        else:
            token = None
        if token is not None:
            gates["G4"] = token
        else:                                              # R8, R10
            gates["G4"] = "pass"
            gates["G5"] = "pass"
            lam = {H_INV} | set(access)
            if not bt["certified"]:
                lam.add(H_LAW)
            if content:
                lam.add(H_SEL)
            lam_text = ", ".join(sorted(lam))
            if H_SEL in lam:
                candidate = "AVAILABLE[H-sel](%s)" % lam_text
            else:
                candidate = "CONDITIONAL[%s]" % lam_text
    row = {
        "bound_ok": bound_ok,
        "branch": b,
        "candidate": "P1",
        "d_ratio": fmt(d_ratio),
        "g2": {"a": a_flag, "hsel_content": content, "t1": t1_flag, "t2": t2},
        "gates": gates,
        "hypotheses": sorted(lam) if lam is not None else rd3_hypotheses(token, access),
        "ledger": ledger,
        "mass": {w: fmt(meas["mass"][w]) for w in meas["mass"]},
        "member": member["key"],
        "nb": nb,
        "nb_g1": nb_g1,
        "pi0_ref": {w: fmt(meas["ref"][w]) for w in meas["ref"]},
        "sharp_w": meas["sharp"],
        "support_size": n_m,
        "token": token,
        "usefulness": None,
        "w_certified": bt["certified"],
        "w_inputs": list(W_INPUTS[b]),
        "w_rule": W_RULE[b],
        "weak": {w: fmt(meas["weak"][w]) for w in meas["weak"]},
    }
    return {"row": row, "g5": candidate is not None, "candidate": candidate,
            "usefulness": usefulness, "sums_ok": sums_ok}


def finalize_row(ev, stage, adversarial):
    """R9: G6 and the token of a row that passes G5, at the rows or the final stage."""
    row = ev["row"]
    if not ev["g5"]:
        return row
    if stage == "rows":
        row["gates"]["G6"] = PENDING
        row["gates"]["G7"] = PENDING
        row["token"] = PENDING
        row["usefulness"] = ev["usefulness"]
        return row
    note_token = adversarial[(row["branch"], row["member"])]
    if note_token == ev["candidate"]:
        row["gates"]["G6"] = "pass"
        row["gates"]["G7"] = ev["candidate"]
        row["token"] = ev["candidate"]
        row["usefulness"] = ev["usefulness"]
    else:
        row["gates"]["G6"] = "UNDECIDED(G6)"
        row["gates"]["G7"] = NOT_REACHED
        row["token"] = "UNDECIDED(G6)"
        row["usefulness"] = None
    return row


def is_positive(token):
    return token.startswith("CONDITIONAL[") or token.startswith("AVAILABLE[H-sel](")


def class_token(rows_b, names, b, access):
    """CLASS (A2): returns (class token or "pending" or None, union_clause_reached)."""
    tokens = [r["token"] for r in rows_b]
    if any(t == PENDING for t in tokens):
        return PENDING, False
    if all(is_positive(t) for t in tokens):
        return None, True
    void_rows = [names[r["member"]] for r in rows_b if r["token"] == "VOID[row]"]
    if void_rows:
        return "VOID[row](%s)" % ", ".join(void_rows), False
    subtypes = [st for st in ("IMPORTED", "DYN") if ("Z1-VOID[%s]" % st) in tokens]
    if subtypes:
        return "Z1-VOID[%s]" % ", ".join(subtypes), False
    ks = sorted({int(t[len("UNDECIDED(G"):-1]) for t in tokens if t.startswith("UNDECIDED(G")})
    if ks:
        return "UNDECIDED(%s)" % ", ".join("G%d" % k for k in ks), False
    if any(t.startswith("ABSENT[") for t in tokens):
        return "ABSENT[%s; %s; %s]" % (CLASS_NAME, b, ", ".join(access)), False
    if any(t.startswith("BLIND[") for t in tokens):
        return "BLIND[%s; %s; %s]" % (CLASS_NAME, b, ", ".join(access)), False
    raise RuntimeError("a non-positive member row of %s has no class-token type" % b)


# ----------------------------------------------------------------------------------------------
# Inputs

def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def serialize(obj):
    """Section 10.2: compact, sorted keys, UTF-8, one trailing LF."""
    return (canonical_json(obj) + "\n").encode("utf-8")


def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def load_class_decisions(rec):
    path = os.path.join(rec, "class-decisions.json")
    if not os.path.isfile(path):
        raise Refusal("class-decisions.json is absent")
    with open(path, "rb") as fh:
        raw = fh.read()
    try:
        cd = json.loads(raw.decode("utf-8"))
    except ValueError:
        raise Refusal("class-decisions.json is not valid UTF-8 JSON")
    expected_keys = {"schema", "version", "derivations", "g1", "class_rule",
                     "support_restriction", "s0_paper"}
    if not isinstance(cd, dict) or set(cd) != expected_keys:
        raise Refusal("class-decisions.json does not have the fields of section 10.2")
    if cd["schema"] != "k1p1-class-decisions" or not _is_int(cd["version"]) or cd["version"] != 1:
        raise Refusal("class-decisions.json: schema or version")
    if cd["derivations"] != CLASS_DERIVATIONS:
        raise Refusal("class-decisions.json: derivations")
    if cd["g1"] not in ("pass", "undecided"):
        raise Refusal("class-decisions.json: g1")
    for key in ("class_rule", "support_restriction"):
        v = cd[key]
        if not isinstance(v, dict) or set(v) != {"a", "t1"}:
            raise Refusal("class-decisions.json: %s" % key)
        if any(v[f] not in ("pass", "flag", "undecided") for f in ("a", "t1")):
            raise Refusal("class-decisions.json: %s values" % key)
    paper = cd["s0_paper"]
    if not isinstance(paper, dict) or set(paper) != set(S0_PAPER_IDS):
        raise Refusal("class-decisions.json: s0_paper")
    if any(paper[k] not in ("pass", "fail", "undecided") for k in S0_PAPER_IDS):
        raise Refusal("class-decisions.json: s0_paper values")
    return cd


def load_adversarial(rec, g5_keys):
    """adversarial.json at final: refused unless it lists every row that passes G5."""
    path = os.path.join(rec, "adversarial.json")
    if not os.path.isfile(path):
        if g5_keys:
            raise Refusal("adversarial.json is absent and a row passes G5")
        return {}
    with open(path, "rb") as fh:
        raw = fh.read()
    try:
        adv = json.loads(raw.decode("utf-8"))
    except ValueError:
        raise Refusal("adversarial.json is not valid UTF-8 JSON")
    if (not isinstance(adv, dict) or adv.get("schema") != "k1p1-adversarial"
            or not _is_int(adv.get("version")) or adv.get("version") != 1
            or not isinstance(adv.get("rows"), list)):
        raise Refusal("adversarial.json: schema, version or rows")
    index = {}
    for entry in adv["rows"]:
        if (not isinstance(entry, dict) or set(entry) != {"branch", "member", "token", "note"}
                or not all(isinstance(entry[f], str) for f in entry)):
            raise Refusal("adversarial.json: malformed entry")
        key = (entry["branch"], entry["member"])
        if key in index:
            raise Refusal("adversarial.json: duplicate entry")
        index[key] = entry["token"]
    for key in g5_keys:
        if key not in index:
            raise Refusal("adversarial.json does not list a row that passes G5")
    return index


# ----------------------------------------------------------------------------------------------
# Exactness guard (section 7)

def contains_float(obj):
    if isinstance(obj, float):
        return True
    if isinstance(obj, dict):
        return any(contains_float(k) or contains_float(v) for k, v in obj.items())
    if isinstance(obj, (list, tuple)):
        return any(contains_float(v) for v in obj)
    return False


def gate_table_rationals(gate):
    out = [gate["region"]["q_pow_minus_E"]]
    for row in gate["rows"]:
        out.append(row["d_ratio"])
        for key in ("weak", "mass", "pi0_ref"):
            out.extend(row[key].values())
    for c in gate["controls"]:
        for part in ("computed", "expected"):
            obj = c[part]
            if obj is None:
                continue
            for key in CONTROL_RATIONAL_KEYS.get(c["id"], ()):
                v = obj.get(key) if isinstance(obj, dict) else None
                if isinstance(v, dict):
                    out.extend(v.values())
                else:
                    out.append(v)
    return out


def exactness_ok(outputs, gate):
    if any(contains_float(obj) for obj in outputs):
        return False
    return all(is_canonical_rational(s) for s in gate_table_rationals(gate))


# ----------------------------------------------------------------------------------------------
# Command line and stages

STAGE_TABLE = {"members": "gate-table.members.json", "rows": "gate-table.rows.json",
               "final": "gate-table.json"}


def parse_args(argv):
    allowed = {"--stage", "--record", "--out", "--members-sha256"}
    args = {}
    i = 0
    while i < len(argv):
        flag = argv[i]
        if flag not in allowed or flag in args or i + 1 >= len(argv):
            raise Refusal("usage: --stage {members|rows|final} --record <rec> --out <out> "
                          "[--members-sha256 <hex>]")
        args[flag] = argv[i + 1]
        i += 2
    for flag in ("--stage", "--record", "--out"):
        if flag not in args:
            raise Refusal("missing %s" % flag)
    if args["--stage"] not in STAGE_TABLE:
        raise Refusal("unknown stage")
    return args


def is_sha256_hex(text):
    return len(text) == 64 and all(ch in "0123456789abcdef" for ch in text)


def write_outputs(out, files):
    written = []
    try:
        for name, data in files:
            tmp = os.path.join(out, name + ".tmp")
            with open(tmp, "wb") as fh:
                fh.write(data)
            written.append(tmp)
        for name, _ in files:
            os.replace(os.path.join(out, name + ".tmp"), os.path.join(out, name))
    except BaseException:
        for name, _ in files:
            for path in (os.path.join(out, name + ".tmp"), os.path.join(out, name)):
                if os.path.exists(path):
                    os.remove(path)
        raise


def run(argv):
    args = parse_args(argv)
    stage = args["--stage"]
    rec = args["--record"]
    out = args["--out"]
    if not os.path.isdir(out) or os.listdir(out):
        raise Refusal("--out must be an existing empty directory")
    cd = load_class_decisions(rec)

    pinned_bytes = None
    if stage != "members":
        pin = args.get("--members-sha256")
        if pin is None or not is_sha256_hex(pin):
            raise Refusal("--members-sha256 (64 lowercase hexadecimal characters) is required")
        path = os.path.join(rec, "members.json")
        if not os.path.isfile(path):
            raise Refusal("members.json is absent from the record directory")
        with open(path, "rb") as fh:
            pinned_bytes = fh.read()
        if hashlib.sha256(pinned_bytes).hexdigest() != pin:
            raise Refusal("members.json does not match the pinned SHA-256")

    inst = build_instance()
    members, members_obj, completeness = compute_members(inst)
    members_bytes = serialize(members_obj)
    if pinned_bytes is not None and pinned_bytes != members_bytes:
        raise Refusal("members.json differs from the members computed here")
    cyc2_obj = compute_cyc2(inst)

    gate = {
        "schema": "k1p1-gate-table",
        "version": 1,
        "stage": stage,
        "instance": dict(INSTANCE),
        "region": compute_region(inst),
        "preserved": compute_preserved(inst),
        "completeness": completeness,
        "controls": compute_controls(inst, cd),
        "rows": [],
        "class_tokens": {},
        "union_clause_reached": {},
    }

    if stage != "members":
        if any(c["outcome"] != "pass" for c in gate["controls"]):
            raise Unsettled("an S0 control does not pass: VOID[stage]; the representation of "
                            "a stage with no row token is not fixed by the preregistration")
        if not completeness["partition"]:
            raise Refusal("CT-INC: CC-PART does not hold")
        evaluations = []
        for b in BRANCHES:
            for mem in members:
                evaluations.append(evaluate_row(inst, b, mem, cd))
        adversarial = None
        if stage == "final":
            g5_keys = [(ev["row"]["branch"], ev["row"]["member"]) for ev in evaluations
                       if ev["g5"]]
            adversarial = load_adversarial(rec, g5_keys)
        rows = [finalize_row(ev, stage, adversarial) for ev in evaluations]
        expected_keys = [mem["key"] for mem in members]
        for b in BRANCHES:
            if [r["member"] for r in rows if r["branch"] == b] != expected_keys:
                raise Refusal("CT-INC: CC-ROWS does not hold in %s" % b)
        if len(rows) != len(BRANCHES) * len(members):
            raise Refusal("CT-INC: CC-ROWS row count")
        names = {mem["key"]: mem["name"] for mem in members}
        for b in BRANCHES:
            token, reached = class_token([r for r in rows if r["branch"] == b], names, b,
                                         inst["branch"][b]["access"])
            gate["class_tokens"][b] = token
            gate["union_clause_reached"][b] = reached
        gate["rows"] = rows
        completeness["mass_sums"] = all(ev["sums_ok"] for ev in evaluations)

    if not exactness_ok([members_obj, cyc2_obj, gate], gate):
        return EXIT_EXACT
    write_outputs(out, [("members.json", members_bytes),
                        (STAGE_TABLE[stage], serialize(gate)),
                        ("cyc2.json", serialize(cyc2_obj))])
    return EXIT_OK


def main(argv):
    try:
        return run(argv)
    except Refusal as exc:
        sys.stderr.write("k1p1_enum_b: refused: %s\n" % exc)
        return EXIT_REFUSE
    except Unsettled as exc:
        sys.stderr.write("k1p1_enum_b: stopped (H7): %s\n" % exc)
        return EXIT_UNSETTLED


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
