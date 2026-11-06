"""K1-P1-1 implementation A: exact enumeration of the P1 stage of K1-RDY-1.

Round K1-P1-1 (native V3, non-sealing).  Control plane: PR #1135,
verification/programmes/oi-qm/reconstruction/round-k1-p1-1/preregistration.md
at 4ca431afb1bfee0cdf301f0917c73068fdf09b58 ("the preregistration", cited by
section).  Adopted rule text "K": K1-RDY-1's control plane at
d9b3de012e393262adb20f91ad49627bad48de43 (preregistration section 2).

Provenance (preregistration section 8.1)
- Author session: writer-k1p1-impl-a (coordinator label writer-k1p1-implA),
  Claude Code session session_011zDyUSyEszk3JJx83uXKKq, 2026-11-06.
- Access to another implementation: none.  This writer received the
  preregistration and the adopted text of its section 2 only, and did not read
  implementation B, controls.py or their branches.
- Shared dependency: none (Python 3.11 standard library only).
- Status: WIP / UNVERIFIED pre-F draft.  Never run on the K1 instance.

Method A (preregistration section 8.2): states are tuples of cells; phi and
phi^-1 are applied from the coordinate formulas; E is found by propagating
symbolic linear forms over Z/q through phi; orbits are walked as in M3.

Exactness (section 7): int and fractions.Fraction only.  Every exact quotient
goes through ratio(); a non-Fraction quotient reaching serialization or the
bound computation exits with status 3.

Exit status (section 10.1): 0 files written; 2 refusal (a stage precondition,
or CT-INC); 3 exactness guard; 4 a case the preregistration leaves
undetermined (OPEN QUESTIONS below; a failure status); any other nonzero
status is a failure.  Nothing is written on a nonzero exit.

OPEN QUESTIONS (not resolved here; each such case exits 4 naming its id)
- OQ-A1: the G7 entry of a row that passes G5 while its G6 is "pending"
  (stage rows): "pending" or "not-reached".
- OQ-A2: the G7 entry of a row whose G6 issues UNDECIDED(G6) (stage final).
- OQ-A3: union_clause_reached for a branch whose class token is "pending".
- OQ-A4: the class_tokens entry of a branch that reaches the union clause
  ("no class token").
- OQ-A5: what is written at stages rows and final when a computed S0 control
  outcome is "fail" (VOID[stage]: "no row or class token is issued").

Usage, from the repository root (section 10.1):
  python3 -I verification/lean/k1p1_enum_a.py --stage {members|rows|final}
      --record <rec> --out <out> [--members-sha256 <hex>]
"""

import hashlib
import itertools
import json
import os
import sys
from fractions import Fraction

# ---------------------------------------------------------------------------
# Exit statuses and their exceptions
# ---------------------------------------------------------------------------


class Refusal(Exception):
    """Exit 2: a stage precondition fails, or CT-INC."""


class InexactValue(Exception):
    """Exit 3: the exactness guard of section 7."""


class Undetermined(Exception):
    """Exit 4: a case the preregistration leaves undetermined."""


class Failure(Exception):
    """Exit 1: an internal check of stage M fails."""


def undetermined(qid, text):
    raise Undetermined(qid + ": " + text)


# ---------------------------------------------------------------------------
# Instance (K lines 31-35; preregistration section 5)
# ---------------------------------------------------------------------------

D_DIM = 1
N = 5
Q = 2
A_COUP = 1
T = 1
SIGMA_CELLS = ("x_0", "y_0")
V_CELL = "y_1"
BRANCHES = ("B-pl", "B-eq", "B-ct")
TU_SHIFT = {"B-pl": 0, "B-eq": 0, "B-ct": -1}  # t_u - t_0 by branch rule

LBL_CUR = "H-cur (declared)"
LBL_2S = "H-2s (declared)"
LBL_RET = "H-ret"
LBL_INV = "H-inv[K-17(a)]"
LBL_LAW = "H-law"
LBL_SEL = "H-sel"

W_RULE = {
    "B-pl": "W trivial; t_u = t_0",
    "B-eq": "W_eq: site set of V, both slices; t_u = t_0",
    "B-ct": "W_eq: site set of V, both slices; t_u = t_0 - 1",
}
W_INPUTS = {"B-pl": [], "B-eq": ["V"], "B-ct": ["V"]}


def ratio(num, den):
    """The exact quotient num/den.  The single division point (section 7)."""
    return Fraction(num, den)


def rat(x):
    """Serialize an exact rational as "p/q"; anything else passes through
    unchanged so that the guard of section 7 sees it."""
    if isinstance(x, Fraction):
        return "%d/%d" % (x.numerator, x.denominator)
    return x


def parts(x):
    """Numerator and denominator of an exact rational, or exit 3."""
    if not isinstance(x, Fraction):
        raise InexactValue("non-Fraction quotient %r" % (x,))
    return x.numerator, x.denominator


# ---------------------------------------------------------------------------
# Cells, states and the coordinate formulas
# ---------------------------------------------------------------------------

def cell_names(n):
    return ["x_%d" % i for i in range(n)] + ["y_%d" % i for i in range(n)]


def cell_index(name, n):
    slab, site = name.split("_")
    return (0 if slab == "x" else n) + int(site)


def is_previous_slice(name):
    return name.startswith("x_")


def all_states(n, q):
    """All states as tuples of cells, in A2's lexicographic order."""
    return [tuple(s) for s in itertools.product(range(q), repeat=2 * n)]


def phi(s, n, q):
    """phi(x, y) = (y, Ay - x), (Ay)_i = y_{i-1} + y_{i+1}."""
    x, y = s[:n], s[n:]
    new_y = tuple((y[(i - 1) % n] + y[(i + 1) % n] - x[i]) % q for i in range(n))
    return tuple(y) + new_y


def phi_inv(s, n, q):
    """phi^-1(x, y) = (Ax - y, x)."""
    x, y = s[:n], s[n:]
    new_x = tuple((x[(i - 1) % n] + x[(i + 1) % n] - y[i]) % q for i in range(n))
    return new_x + tuple(x)


def evolve(s, k, n, q):
    """phi^k(s) for an integer k."""
    for _ in range(max(0, k)):
        s = phi(s, n, q)
    for _ in range(max(0, -k)):
        s = phi_inv(s, n, q)
    return s


def restrict(s, idx):
    return "".join(str(s[i]) for i in idx)


def sstr(s):
    return "".join(str(c) for c in s)


def values_of(idx, q):
    """All values of a cell set, as strings, in lexicographic order."""
    return ["".join(str(c) for c in v) for v in itertools.product(range(q), repeat=len(idx))]


# ---------------------------------------------------------------------------
# R0: E by symbolic linear forms propagated through phi (method A)
# ---------------------------------------------------------------------------

def form_add(f, g, q):
    return tuple((a + b) % q for a, b in zip(f, g))


def form_neg(f, q):
    return tuple((-a) % q for a in f)


def phi_forms(forms, n, q):
    """phi applied to a state whose cells are linear forms in s(t_0)."""
    x, y = forms[:n], forms[n:]
    new_y = tuple(form_add(form_add(y[(i - 1) % n], y[(i + 1) % n], q), form_neg(x[i], q), q)
                  for i in range(n))
    return tuple(y) + new_y


def region_e(n, q, t_window, v_cell, sigma_cells):
    """Cells outside Sigma with a nonzero coefficient in V(t_0 + t), as a
    linear form in s(t_0), for some 0 <= t <= T (K lines 36-38)."""
    names = cell_names(n)
    width = 2 * n
    forms = tuple(tuple(1 if j == i else 0 for j in range(width)) for i in range(width))
    v = cell_index(v_cell, n)
    hit = set()
    for _ in range(t_window + 1):
        for j, c in enumerate(forms[v]):
            if c % q != 0:
                hit.add(j)
        forms = phi_forms(forms, n, q)
    sig = {cell_index(c, n) for c in sigma_cells}
    return [names[j] for j in sorted(hit) if j not in sig]


def region_w_eq(n, v_cell):
    """W_eq: the site set of V, both slices (K line 43)."""
    site = v_cell.split("_")[1]
    names = cell_names(n)
    return [c for c in names if c.split("_")[1] == site]


def energy(s, n, q):
    """E(x, y) = <x, x> + <y, y> - <x, Ay> mod q (preregistration section 5)."""
    x, y = s[:n], s[n:]
    xx = sum(x[i] * x[i] for i in range(n))
    yy = sum(y[i] * y[i] for i in range(n))
    xay = sum(x[i] * (y[(i - 1) % n] + y[(i + 1) % n]) for i in range(n))
    return (xx + yy - xay) % q


# ---------------------------------------------------------------------------
# Stage M
# ---------------------------------------------------------------------------

def stage_m():
    names = cell_names(N)
    S = all_states(N, Q)  # M1
    size_s = len(S)
    distinct = (len(set(S)) == size_s) and (size_s == Q ** (2 * N))
    fwd = {s: phi(s, N, Q) for s in S}  # M2
    bwd = {s: phi_inv(s, N, Q) for s in S}
    bijection = (all(bwd[fwd[s]] == s for s in S)
                 and all(fwd[bwd[s]] == s for s in S)
                 and set(fwd.values()) == set(S))
    visited = set()  # M3
    cycles = []
    for s in S:
        if s in visited:
            continue
        c = [s]
        t = fwd[s]
        steps = 0
        while t != s:
            c.append(t)
            t = fwd[t]
            steps += 1
            if steps > size_s:
                raise Failure("orbit walk from %s exceeds |S| steps" % sstr(s))
        visited.update(c)
        cycles.append((s, sorted(c)))
    owner = {}  # M4
    for key, c in cycles:
        for t in c:
            owner[t] = owner.get(t, 0) + 1
    length_sum = sum(len(c) for _, c in cycles)
    partition = (set(owner) == set(S) and all(v == 1 for v in owner.values())
                 and length_sum == size_s)
    for key, c in cycles:
        cs = set(c)
        if {fwd[t] for t in c} != cs or min(c) != key:
            partition = False
        t, seen = key, set()
        for _ in range(len(c)):
            seen.add(t)
            t = fwd[t]
        if t != key or seen != cs:
            partition = False
    histogram = {}
    for _, c in cycles:
        histogram[str(len(c))] = histogram.get(str(len(c)), 0) + 1
    members = [{"key": "pi0", "size": size_s}]  # M5
    for key, c in cycles:
        members.append({"key": sstr(key), "size": len(c), "states": [sstr(t) for t in c]})
    members_obj = {
        "schema": "k1p1-members",
        "version": 1,
        "cell_order": names,
        "members": members,
        "histogram": histogram,
    }
    order, cur = 0, list(S)
    while True:
        cur = [fwd[t] for t in cur]
        order += 1
        if cur == S:
            break
        if order > size_s:
            raise Failure("phi order exceeds |S|")
    energy_conserved = all(energy(fwd[s], N, Q) == energy(s, N, Q) for s in S)
    shells = {str(v): 0 for v in range(Q)}
    for s in S:
        shells[str(energy(s, N, Q))] += 1
    return {
        "S": S, "fwd": fwd, "bwd": bwd, "cycles": cycles,
        "members_obj": members_obj,
        "completeness": {
            "states": size_s, "length_sum": length_sum, "cycles": len(cycles),
            "distinct": distinct, "bijection": bijection, "partition": partition,
            "mass_sums": None,
        },
        "preserved": {"energy_conserved": energy_conserved, "shell_sizes": shells,
                      "phi_order": order},
    }


# ---------------------------------------------------------------------------
# Readiness, NB and usefulness for a weighted law (R2, R3, R4)
# ---------------------------------------------------------------------------

class Frame:
    """Per-(W, t_u) data over all of S at instance (n, q)."""

    def __init__(self, S, n, q, w_cells, shift, e_cells):
        self.n, self.q = n, q
        self.w_idx = [cell_index(c, n) for c in w_cells]
        self.e_idx = [cell_index(c, n) for c in e_cells]
        self.sig_idx = [cell_index(c, n) for c in SIGMA_CELLS]
        self.v = cell_index(V_CELL, n)
        self.shift = shift
        self.wval = {s: restrict(evolve(s, shift, n, q), self.w_idx) for s in S}
        self.evalue = {s: restrict(s, self.e_idx) for s in S}
        self.zero = {s: all(s[i] == 0 for i in self.e_idx) for s in S}
        self.sigma = {s: restrict(s, self.sig_idx) for s in S}
        self.readout = {}
        for s in S:
            r, t = [], s
            for _ in range(T + 1):
                r.append(str(t[self.v]))
                t = phi(t, n, q)
            self.readout[s] = "".join(r)
        self.all_w = values_of(self.w_idx, q)
        self.block = {w: [] for w in self.all_w}
        for s in S:
            self.block[self.wval[s]].append(s)

    def certified(self):
        """R4: for every w, B_w within Z or B_w disjoint from Z."""
        for w in self.all_w:
            z = [self.zero[s] for s in self.block[w]]
            if any(z) and not all(z):
                return False
        return True


def law_split(frame, weighted):
    """For nu given as [(state, weight > 0)]: nu(sigma) and L_sigma."""
    total = sum(wt for _, wt in weighted)
    by_sigma = {}
    for s, wt in weighted:
        by_sigma.setdefault(frame.sigma[s], []).append((s, wt))
    nu_sigma, laws = {}, {}
    for sig in sorted(by_sigma):
        part = by_sigma[sig]
        msig = sum(wt for _, wt in part)
        nu_sigma[sig] = ratio(msig, total)
        acc = {}
        for s, wt in part:
            acc[frame.readout[s]] = acc.get(frame.readout[s], 0) + wt
        laws[sig] = {r: ratio(acc[r], msig) for r in sorted(acc)}
    return nu_sigma, laws


def nb_of(laws):
    sigs = sorted(laws)
    return any(laws[a] != laws[b] for a, b in itertools.combinations(sigs, 2))


def sums_ok(nu_sigma, laws):
    if sum(nu_sigma.values()) != 1:
        return False
    return all(sum(law.values()) == 1 for law in laws.values())


def usefulness_at(laws):
    disjoint, law_only = [], []
    for a, b in itertools.combinations(sorted(laws), 2):
        sa, sb = set(laws[a]), set(laws[b])
        if not (sa & sb):
            disjoint.append([a, b])
        elif laws[a] != laws[b]:
            law_only.append([a, b])
    return {"disjoint": disjoint, "law_only": law_only}


def readiness(frame, weighted):
    """R2 and R3 for the law given as [(state, weight > 0)]."""
    total = sum(wt for _, wt in weighted)
    groups = {}
    for s, wt in weighted:
        groups.setdefault(frame.wval[s], []).append((s, wt))
    out = {"mass": {}, "weak": {}, "pi0_ref": {}, "sharp": [], "nb": {},
           "laws": {}, "sums_ok": True, "parts": {}}
    for w in frame.all_w:
        part = groups.get(w, [])
        mw = sum(wt for _, wt in part)
        if not part:
            continue
        out["parts"][w] = part
        out["mass"][w] = ratio(mw, total)
        ready = sum(wt for s, wt in part if frame.zero[s])
        out["weak"][w] = ratio(ready, mw)
        blk = frame.block[w]
        out["pi0_ref"][w] = ratio(sum(1 for s in blk if frame.zero[s]), len(blk))
        if out["weak"][w] == 1:
            out["sharp"].append(w)
            nu_sigma, laws = law_split(frame, part)
            out["nb"][w] = nb_of(laws)
            out["laws"][w] = laws
            out["sums_ok"] = out["sums_ok"] and sums_ok(nu_sigma, laws)
    if sum(out["mass"].values()) != 1:
        out["sums_ok"] = False
    return out


def hsel_content(frame, support):
    """R5 (RD-5): I_w strictly inside J_w, per positive-mass w, in w order."""
    sup = set(support)
    content = []
    for w in frame.all_w:
        inside = [s for s in frame.block[w] if s in sup]
        if not inside:
            continue
        i_w = sorted({frame.evalue[s] for s in inside})
        j_w = {frame.evalue[s] for s in frame.block[w]}
        if set(i_w) < j_w:
            content.append({"values": i_w, "w": w})
    return content


# ---------------------------------------------------------------------------
# Inputs
# ---------------------------------------------------------------------------

S0_PAPER_KEYS = ("CC-LEDGER", "CC-IMP", "CC-IMP′", "CC-IMP″", "CC-PASS", "CC-T2")


def read_json(path):
    with open(path, "rb") as fh:
        return json.loads(fh.read().decode("utf-8"))


def load_class_decisions(rec):
    path = os.path.join(rec, "class-decisions.json")
    if not os.path.isfile(path):
        raise Refusal("class-decisions.json absent")
    try:
        cd = read_json(path)
    except ValueError as exc:
        raise Refusal("class-decisions.json unreadable: %s" % exc)
    tri = ("pass", "flag", "undecided")
    ok = (isinstance(cd, dict)
          and cd.get("schema") == "k1p1-class-decisions"
          and cd.get("version") == 1
          and cd.get("derivations") == ["derivations/P1-class-paper.md",
                                        "derivations/S0-paper.md"]
          and cd.get("g1") in ("pass", "undecided"))
    for k in ("class_rule", "support_restriction"):
        v = cd.get(k) if isinstance(cd, dict) else None
        ok = ok and isinstance(v, dict) and v.get("a") in tri and v.get("t1") in tri
    sp = cd.get("s0_paper") if isinstance(cd, dict) else None
    ok = ok and isinstance(sp, dict) and all(sp.get(k) in ("pass", "fail", "undecided")
                                             for k in S0_PAPER_KEYS)
    if not ok:
        raise Refusal("class-decisions.json does not match the schema of section 10.2")
    return cd


def check_members_file(rec, pinned, computed_bytes):
    path = os.path.join(rec, "members.json")
    if pinned is None:
        raise Refusal("--members-sha256 is required at this stage")
    if len(pinned) != 64 or any(c not in "0123456789abcdef" for c in pinned):
        raise Refusal("--members-sha256 is not 64 lowercase hexadecimal characters")
    if not os.path.isfile(path):
        raise Refusal("members.json absent")
    with open(path, "rb") as fh:
        data = fh.read()
    if hashlib.sha256(data).hexdigest() != pinned:
        raise Refusal("members.json differs from its pinned digest")
    if data != computed_bytes:
        raise Refusal("members.json differs from the members.json computed here")


def load_adversarial(rec):
    path = os.path.join(rec, "adversarial.json")
    if not os.path.isfile(path):
        return None
    try:
        adv = read_json(path)
    except ValueError as exc:
        raise Refusal("adversarial.json unreadable: %s" % exc)
    if not (isinstance(adv, dict) and adv.get("schema") == "k1p1-adversarial"
            and adv.get("version") == 1 and isinstance(adv.get("rows"), list)):
        raise Refusal("adversarial.json does not match the schema of section 10.2")
    table = {}
    for e in adv["rows"]:
        if not (isinstance(e, dict) and isinstance(e.get("branch"), str)
                and isinstance(e.get("member"), str) and isinstance(e.get("token"), str)):
            raise Refusal("adversarial.json entry malformed")
        k = (e["branch"], e["member"])
        if k in table:
            raise Refusal("adversarial.json lists a row twice")
        table[k] = e["token"]
    return table


# ---------------------------------------------------------------------------
# Tokens and labels
# ---------------------------------------------------------------------------

def member_name(key):
    return "π_0" if key == "pi0" else "u_c[%s]" % key


def access_labels(branch, w_cells):
    """Section 2 access labels in token order: H-cur, H-2s, H-ret."""
    labels = [LBL_CUR]
    if any(is_previous_slice(c) for c in w_cells):
        labels.append(LBL_2S)
    if TU_SHIFT[branch] != 0:
        labels.append(LBL_RET)
    return labels


def is_positive(token):
    return token.startswith(("CONDITIONAL[", "AVAILABLE[H-sel]("))


def positive_token(lam):
    joined = ", ".join(sorted(lam))
    if LBL_SEL in lam:
        return "AVAILABLE[H-sel](%s)" % joined
    return "CONDITIONAL[%s]" % joined


# ---------------------------------------------------------------------------
# Context at the instance
# ---------------------------------------------------------------------------

def build_context(m):
    S = m["S"]
    e_cells = region_e(N, Q, T, V_CELL, SIGMA_CELLS)
    w_eq = region_w_eq(N, V_CELL)
    w_by_branch = {"B-pl": [], "B-eq": w_eq, "B-ct": w_eq}
    frames = {b: Frame(S, N, Q, w_by_branch[b], TU_SHIFT[b], e_cells) for b in BRANCHES}
    overlap = {"B-eq": [c for c in w_eq if c in e_cells], "B-ct": []}
    region = {
        "E": e_cells,
        "W_eq": w_eq,
        "q_pow_minus_E": ratio(1, Q ** len(e_cells)),
        "overlap": overlap,
        "overlap_tautological": {b: bool(overlap[b]) for b in ("B-eq", "B-ct")},
    }
    return {"S": S, "E": e_cells, "W": w_by_branch, "frames": frames, "region": region}


# ---------------------------------------------------------------------------
# S0 controls (K section 6; preregistration sections 10.2 and 11.1)
# ---------------------------------------------------------------------------

CONTROL_IDS = ["CC-ABS", "CC-EXACT", "CC-SCOPE", "CC-LEDGER", "CC-IMP", "CC-IMP′",
               "CC-IMP″", "CC-PASS", "CC-T2", "POS-X", "CC-BLIND"]
CONTROL_GATES = ["G4", "G4", "G4", "G3/G4", "G2, G3", "G2(a)",
                 "G2(a); T1; T2's no-image disjunct", "G2(b)", "G2(b) T2", "G3, G4, G7", "G4"]
_SAME = {"nb_all_false": True, "sharp": True}
CONTROL_EXPECTED = {
    "CC-ABS": {"sharp_w": [], "weak": {"00": "1/8", "01": "1/8", "10": "1/8", "11": "1/8"}},
    "CC-EXACT": {"sharp_w": [], "weak": {"": "153/160"}},
    "CC-SCOPE": {"B-ct": dict(_SAME), "B-eq": dict(_SAME), "B-pl": dict(_SAME)},
    "CC-LEDGER": {"c1": False, "d_ratio": "2/1", "shell_size": 512},
    "CC-IMP": {"d_ratio": "8/1", "support_size": 128},
    "CC-IMP′": None,
    "CC-IMP″": {"fixes_x2_zero": True},
    "CC-PASS": {"hsel_content": {"B-eq": [], "B-pl": [{"values": ["000", "001", "110", "111"],
                                                       "w": ""}]},
                "image_equals_stated": True},
    "CC-T2": {"image_equals_stated": False},
    "POS-X": {"g3_void": False, "mass_w0": "1/64", "nb_w0": True, "sharp_w0": True,
              "token": "CONDITIONAL[H-2s (declared), H-cur (declared), H-ret, H-μ, "
                       "finite-S posit]",
              "w_certified": True},
    "CC-BLIND": {"mass_w0": "1/256", "nb_w0": False, "sharp_w0": True},
}
W_CT = ["x_1", "x_2", "y_0", "y_1", "y_2", "y_3"]  # K line 199, in A2 order
W_BLIND = ["x_0", "x_1", "x_2", "y_0", "y_1", "y_2", "y_3", "y_4"]  # W_ct and {y_4, x_0}


def linear_set(S, equations, n, q):
    """States satisfying every equation sum of cells = 0 mod q."""
    idx = [[cell_index(c, n) for c in eq] for eq in equations]
    return {s for s in S if all(sum(s[i] for i in eq) % q == 0 for eq in idx)}


def ctl_cross_fixture(S, ctx, w_cells):
    frame = Frame(S, N, Q, w_cells, -1, ctx["E"])
    r = readiness(frame, [(s, 1) for s in S])
    w0 = "0" * len(w_cells)
    mass_w0 = r["mass"].get(w0, ratio(0, 1))
    if w0 in r["parts"]:
        _, laws = law_split(frame, r["parts"][w0])
        nb_w0 = nb_of(laws)
    else:
        nb_w0 = False
    cert = frame.certified()
    return r, w0, mass_w0, nb_w0, cert


def compute_controls(ctx, cd):
    S = ctx["S"]
    e_cells = ctx["E"]
    fr = ctx["frames"]
    zero_set = [s for s in S if fr["B-pl"].zero[s]]
    computed = {}

    # CC-ABS: pi_0, W = {x_3, y_3}, equal time.
    f_abs = Frame(S, N, Q, ["x_3", "y_3"], 0, e_cells)
    r = readiness(f_abs, [(s, 1) for s in S])
    computed["CC-ABS"] = {"sharp_w": list(r["sharp"]),
                          "weak": {w: rat(v) for w, v in r["weak"].items()}}

    # CC-EXACT: (1 - eps) mu_Q + eps pi_0, eps = 1/20, B-pl.
    eps = ratio(1, 20)
    mq = ratio(1, len(zero_set))
    zs = set(zero_set)
    weighted = [(s, (1 - eps) * (mq if s in zs else 0) + eps * ratio(1, len(S))) for s in S]
    r = readiness(fr["B-pl"], weighted)
    computed["CC-EXACT"] = {"sharp_w": list(r["sharp"]),
                            "weak": {w: rat(v) for w, v in r["weak"].items()}}

    # CC-SCOPE: delta_0 in each branch.
    origin = tuple(0 for _ in range(2 * N))
    scope = {}
    for b in BRANCHES:
        r = readiness(fr[b], [(origin, 1)])
        scope[b] = {"nb_all_false": all(not r["nb"][w] for w in r["sharp"]),
                    "sharp": bool(r["sharp"])}
    computed["CC-SCOPE"] = scope

    # CC-LEDGER: pi_0( . | energy = 0).
    shell = [s for s in S if energy(s, N, Q) == 0]
    computed["CC-LEDGER"] = {"c1": Q ** len(e_cells) * len(shell) <= len(S),
                             "d_ratio": rat(ratio(len(S), len(shell))),
                             "shell_size": len(shell)}

    # CC-IMP: mu_Q = delta_0 on E's cells x pi_0 elsewhere.
    computed["CC-IMP"] = {"d_ratio": rat(ratio(len(S), len(zero_set))),
                          "support_size": len(zero_set)}

    # CC-IMP': paper only.
    computed["CC-IMP′"] = None

    # CC-IMP'': N = 6; W = sites {0, 1}, both slices; O = "W = 0 over [t_u - 1, t_u]".
    n6 = 6
    S6 = all_states(n6, Q)
    w6 = [cell_index(c, n6) for c in ("x_0", "x_1", "y_0", "y_1")]
    x2 = cell_index("x_2", n6)
    event = [s for s in S6
             if all(s[i] == 0 for i in w6) and all(phi_inv(s, n6, Q)[i] == 0 for i in w6)]
    computed["CC-IMP″"] = {"fixes_x2_zero": bool(event) and all(s[x2] == 0 for s in event)}

    # CC-PASS and CC-T2: O_1 = "W_eq identical at t_u - 1 and t_u", t_u = t_0.
    weq_idx = [cell_index(c, N) for c in ctx["W"]["B-eq"]]
    image = {s for s in S if restrict(phi_inv(s, N, Q), weq_idx) == restrict(s, weq_idx)}
    stated_pass = linear_set(S, [("x_1", "y_1"), ("x_0", "x_2")], N, Q)
    stated_t2 = linear_set(S, [("x_1", "y_1")], N, Q)
    pass_ok = image == stated_pass
    support = sorted(image)
    hsel = {}
    for b in ("B-pl", "B-eq"):
        hsel[b] = hsel_content(fr[b], support) if pass_ok else []
    computed["CC-PASS"] = {"hsel_content": hsel, "image_equals_stated": pass_ok}
    computed["CC-T2"] = {"image_equals_stated": image == stated_t2}

    # POS-X: pi_0, cross time, W = W_ct.
    r, w0, mass_w0, nb_w0, cert = ctl_cross_fixture(S, ctx, W_CT)
    labels = access_labels("B-ct", W_CT)
    if not r["sharp"]:
        token = "ABSENT[π_0; B-ct; %s]" % ", ".join(labels)
    elif all(not r["nb"][w] for w in r["sharp"]):
        token = "BLIND[π_0; B-ct; %s]" % ", ".join(labels)
    else:
        lam = {"H-μ", "finite-S posit"} | set(labels)
        if not cert:
            lam.add(LBL_LAW)
        token = positive_token(lam)
    computed["POS-X"] = {"g3_void": False, "mass_w0": rat(mass_w0), "nb_w0": nb_w0,
                         "sharp_w0": w0 in r["sharp"], "token": token, "w_certified": cert}

    # CC-BLIND: W_ct and {y_4, x_0} at t_u.
    r, w0, mass_w0, nb_w0, cert = ctl_cross_fixture(S, ctx, W_BLIND)
    computed["CC-BLIND"] = {"mass_w0": rat(mass_w0), "nb_w0": nb_w0,
                            "sharp_w0": w0 in r["sharp"]}

    controls = []
    for cid, gate in zip(CONTROL_IDS, CONTROL_GATES):
        paper = cd["s0_paper"][cid] if cid in S0_PAPER_KEYS else None
        exp = CONTROL_EXPECTED[cid]
        ok = computed[cid] == exp and paper in (None, "pass")
        controls.append({"id": cid, "gate": gate, "computed": computed[cid], "expected": exp,
                         "paper": paper, "outcome": "pass" if ok else "fail"})
    return controls


# ---------------------------------------------------------------------------
# Stage R: member rows (R1-R10)
# ---------------------------------------------------------------------------

def member_supports(m):
    out = [("pi0", list(m["S"]))]
    for key, c in m["cycles"]:
        out.append((sstr(key), list(c)))
    return out


def early_token(cd, is_pi0, t2):
    """R5a: G1 and G2 entries and the token they issue, if any."""
    cr, sr = cd["class_rule"], cd["support_restriction"]
    imported = cr["a"] == "flag" or (not is_pi0 and sr["a"] == "flag")
    t1 = cr["t1"] == "flag" or (not is_pi0 and sr["t1"] == "flag")
    dyn = t1 or t2
    und2 = ("undecided" in (cr["a"], cr["t1"])
            or (not is_pi0 and "undecided" in (sr["a"], sr["t1"])))
    g1_und = cd["g1"] == "undecided"
    z1 = "Z1-VOID[IMPORTED]" if imported else ("Z1-VOID[DYN]" if dyn else None)
    g1 = "UNDECIDED(G1)" if g1_und else "pass"
    g2 = z1 if z1 else ("UNDECIDED(G2)" if und2 else "pass")
    if z1:
        tok = z1
    elif g1_und:
        tok = "UNDECIDED(G1)"
    elif und2:
        tok = "UNDECIDED(G2)"
    else:
        tok = None
    return {"a": imported, "t1": t1}, g1, g2, tok


def evaluate_row(ctx, m, cd, branch, key, support, stage, adversarial):
    S = ctx["S"]
    frame = ctx["frames"][branch]
    w_cells = ctx["W"][branch]
    e_cells = ctx["E"]
    size = len(support)
    is_pi0 = key == "pi0"
    fwd = m["fwd"]
    weighted = [(s, 1) for s in support]  # R1: uniform on supp(m), as counts
    r = readiness(frame, weighted)  # R2, R3 at sharp w
    sums = r["sums_ok"]
    nb_g1 = None
    if branch == "B-pl":
        nu_sigma, laws = law_split(frame, weighted)
        nb_g1 = nb_of(laws)
        sums = sums and sums_ok(nu_sigma, laws)
    supp_set = set(support)
    t2 = {fwd[s] for s in support} != supp_set  # R5, RD-6
    g2flags, g1, g2, tok = early_token(cd, is_pi0, t2)
    hsel = [] if (g2flags["t1"] or t2) else hsel_content(frame, support)
    d_ratio = ratio(len(S), size)  # R6
    labels = access_labels(branch, w_cells)
    k = len([c for c in e_cells if c not in w_cells])
    if branch == "B-pl":
        bound_ok = Q ** len(e_cells) * size <= len(S)
        verdict = "holds" if bound_ok else "breaks"
        ledger = "D=log(%s); (c1) |E|=%d: %s" % (rat(d_ratio), len(e_cells), verdict)
        breaks = (not bound_ok) and bool(r["sharp"])
    elif branch == "B-eq":
        bound_ok = {}
        items = []
        for w in r["sharp"]:
            a, b = parts(r["mass"][w])
            bound_ok[w] = Q ** (a * k) * size ** b <= len(S) ** b
            items.append("w=%s p=%s k=%d: %s" % (w, rat(r["mass"][w]), k,
                                                 "holds" if bound_ok[w] else "breaks"))
        if items:
            ledger = "D=log(%s); (c2) " % rat(d_ratio) + "; ".join(items)
        else:
            ledger = "D=log(%s); (c2) no sharp w" % rat(d_ratio)
        breaks = any(not v for v in bound_ok.values())
    else:
        bound_ok = None
        ledger = "D=log(%s); cross time, no D bound; H-ret" % rat(d_ratio)
        breaks = False
    certified = frame.certified()  # R4
    gates = {"G1": g1, "G2": g2, "G3": "not-reached", "G4": "not-reached",
             "G5": "not-reached", "G6": "not-reached", "G7": "not-reached"}
    usefulness = None
    hyps = {LBL_INV}
    name = member_name(key)
    if tok is not None:
        token = tok
    else:
        gates["G3"] = "pass"
        if not r["sharp"]:  # R7
            token = "ABSENT[%s; %s; %s]" % (name, branch, ", ".join(labels))
            gates["G4"] = token
            hyps |= set(labels)
        elif breaks:
            token = "VOID[row]"
            gates["G4"] = token
        elif all(not r["nb"][w] for w in r["sharp"]):
            token = "BLIND[%s; %s; %s]" % (name, branch, ", ".join(labels))
            gates["G4"] = token
            hyps |= set(labels)
        else:
            gates["G4"] = "pass"
            lam = {LBL_INV} | set(labels)  # R8
            if not certified:
                lam.add(LBL_LAW)
            if hsel:
                lam.add(LBL_SEL)
            gates["G5"] = "pass"
            hyps = lam
            pos = positive_token(lam)  # R10
            usefulness = {w: usefulness_at(r["laws"][w]) for w in r["sharp"]}
            if stage == "probe":
                token = "pending"
            elif stage == "rows":  # R9
                gates["G6"] = "pending"
                token = "pending"
                undetermined("OQ-A1", "G7 entry of a row whose G6 is pending (%s, %s)"
                             % (branch, key))
            else:
                if (branch, key) not in adversarial:
                    raise Refusal("adversarial.json does not list row (%s, %s), which passes G5"
                                  % (branch, key))
                if adversarial[(branch, key)] == pos:
                    gates["G6"] = "pass"
                    gates["G7"] = pos
                    token = pos
                else:
                    gates["G6"] = "UNDECIDED(G6)"
                    token = "UNDECIDED(G6)"
                    usefulness = None
                    undetermined("OQ-A2", "G7 entry of a row whose G6 issues UNDECIDED(G6) "
                                 "(%s, %s)" % (branch, key))
    row = {
        "candidate": "P1",
        "member": key,
        "branch": branch,
        "gates": gates,
        "w_rule": W_RULE[branch],
        "w_inputs": list(W_INPUTS[branch]),
        "g2": {"a": g2flags["a"], "t1": g2flags["t1"], "t2": t2, "hsel_content": hsel},
        "sharp_w": list(r["sharp"]),
        "weak": {w: rat(v) for w, v in r["weak"].items()},
        "mass": {w: rat(v) for w, v in r["mass"].items()},
        "pi0_ref": {w: rat(v) for w, v in r["pi0_ref"].items()},
        "nb": dict(r["nb"]),
        "nb_g1": nb_g1,
        "w_certified": certified,
        "usefulness": usefulness,
        "hypotheses": sorted(hyps),
        "token": token,
        "support_size": size,
        "d_ratio": rat(d_ratio),
        "bound_ok": bound_ok,
        "ledger": ledger,
    }
    return row, sums


def g5_passing(ctx, m, cd, branch, key, support):
    """Whether the row reaches G5 (used to check adversarial coverage)."""
    row, _ = evaluate_row(ctx, m, cd, branch, key, support, "probe", None)
    return row["gates"]["G5"] == "pass"


def class_tokens(ctx, rows_by_branch, member_keys):
    """CLASS (A2) per branch.  Returns (class_tokens, union_clause_reached)."""
    ct, uc = {}, {}
    for b in BRANCHES:
        rows = rows_by_branch[b]
        if [rw["member"] for rw in rows] != member_keys:
            raise Refusal("CT-INC: the row set of %s is incomplete" % b)
        toks = [rw["token"] for rw in rows]
        if any(t == "pending" for t in toks):
            ct[b] = "pending"
            undetermined("OQ-A3", "union_clause_reached for a pending branch (%s)" % b)
        if all(is_positive(t) for t in toks):
            uc[b] = True
            undetermined("OQ-A4", "class_tokens entry of a branch at the union clause (%s)" % b)
        uc[b] = False
        labels = access_labels(b, ctx["W"][b])
        voided = [rw["member"] for rw in rows if rw["token"] == "VOID[row]"]
        z1 = [s for s in ("IMPORTED", "DYN") if ("Z1-VOID[%s]" % s) in toks]
        und = sorted({int(t[len("UNDECIDED(G"):-1]) for t in toks if t.startswith("UNDECIDED(G")})
        if voided:
            ct[b] = "VOID[row](%s)" % ", ".join(member_name(k) for k in voided)
        elif z1:
            ct[b] = "Z1-VOID[%s]" % ", ".join(z1)
        elif und:
            ct[b] = "UNDECIDED(%s)" % ", ".join("G%d" % k for k in und)
        elif any(t.startswith("ABSENT[") for t in toks):
            ct[b] = "ABSENT[\U0001d4d8; %s; %s]" % (b, ", ".join(labels))
        elif any(t.startswith("BLIND[") for t in toks):
            ct[b] = "BLIND[\U0001d4d8; %s; %s]" % (b, ", ".join(labels))
        else:
            raise Failure("non-positive row token of no listed type in %s" % b)
    return ct, uc


# ---------------------------------------------------------------------------
# Exactness guard (section 7) and serialization (section 10.2)
# ---------------------------------------------------------------------------

def walk_floats(obj):
    if isinstance(obj, float):
        return True
    if isinstance(obj, dict):
        return any(walk_floats(v) for v in obj.values())
    if isinstance(obj, list):
        return any(walk_floats(v) for v in obj)
    return False


def is_rational_string(x):
    if not isinstance(x, str) or x.count("/") != 1:
        return False
    p, q = x.split("/")
    try:
        pi, qi = int(p), int(q)
    except ValueError:
        return False
    if str(pi) != p or str(qi) != q or qi <= 0:
        return False
    f = Fraction(pi, qi)
    return f.numerator == pi and f.denominator == qi


RATIONAL_CONTROL_FIELDS = {
    "CC-ABS": ("weak",), "CC-EXACT": ("weak",), "CC-LEDGER": ("d_ratio",),
    "CC-IMP": ("d_ratio",), "POS-X": ("mass_w0",), "CC-BLIND": ("mass_w0",),
}


def rational_fields(table):
    out = [table["region"]["q_pow_minus_E"]]
    for c in table["controls"]:
        for side in ("computed", "expected"):
            obj = c[side]
            for f in RATIONAL_CONTROL_FIELDS.get(c["id"], ()):
                v = obj.get(f) if isinstance(obj, dict) else None
                out.extend(v.values() if isinstance(v, dict) else [v])
    for rw in table["rows"]:
        for f in ("weak", "mass", "pi0_ref"):
            out.extend(rw[f].values())
        out.append(rw["d_ratio"])
    return out


def guard(members_obj, table):
    if walk_floats(members_obj) or walk_floats(table):
        raise InexactValue("a float in the output")
    for v in rational_fields(table):
        if not is_rational_string(v):
            raise InexactValue("not a rational p/q in lowest terms: %r" % (v,))


def dump(obj):
    text = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return text.encode("utf-8") + b"\n"


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

STAGE_TABLE = {"members": "gate-table.members.json", "rows": "gate-table.rows.json",
               "final": "gate-table.json"}


def parse_args(argv):
    opts = {}
    allowed = ("--stage", "--record", "--out", "--members-sha256")
    i = 0
    while i < len(argv):
        k = argv[i]
        if k not in allowed or i + 1 >= len(argv) or k in opts:
            raise Failure("usage: --stage {members|rows|final} --record <rec> --out <out> "
                          "[--members-sha256 <hex>]")
        opts[k] = argv[i + 1]
        i += 2
    for k in ("--stage", "--record", "--out"):
        if k not in opts:
            raise Failure("missing %s" % k)
    if opts["--stage"] not in STAGE_TABLE:
        raise Failure("unknown stage %r" % opts["--stage"])
    return opts["--stage"], opts["--record"], opts["--out"], opts.get("--members-sha256")


def run(argv):
    stage, rec, out, pinned = parse_args(argv)
    if not os.path.isdir(out) or os.listdir(out):
        raise Refusal("--out is not an existing empty directory")
    cd = load_class_decisions(rec)
    m = stage_m()
    members_bytes = dump(m["members_obj"])
    if stage in ("rows", "final"):
        check_members_file(rec, pinned, members_bytes)
    ctx = build_context(m)
    controls = compute_controls(ctx, cd)
    table = {
        "schema": "k1p1-gate-table",
        "version": 1,
        "stage": stage,
        "instance": {"N": N, "a": A_COUP, "d": D_DIM, "q": Q},
        "region": dict(ctx["region"], q_pow_minus_E=rat(ctx["region"]["q_pow_minus_E"])),
        "preserved": m["preserved"],
        "completeness": dict(m["completeness"]),
        "controls": controls,
        "rows": [],
        "class_tokens": {},
        "union_clause_reached": {},
    }
    if walk_floats(controls) or not is_rational_string(table["region"]["q_pow_minus_E"]):
        raise InexactValue("a float in the region or the S0 controls")
    if stage != "members":
        if any(c["outcome"] != "pass" for c in controls):
            undetermined("OQ-A5", "output at stage %s when an S0 control fails" % stage)
        if not m["completeness"]["partition"]:
            raise Refusal("CT-INC: CC-PART does not hold")
        supports = member_supports(m)
        member_keys = [k for k, _ in supports]
        if member_keys != [mm["key"] for mm in m["members_obj"]["members"]]:
            raise Refusal("CT-INC: member list differs from M5")
        adversarial = {}
        if stage == "final":
            adv = load_adversarial(rec)
            needed = [(b, k) for b in BRANCHES for k, sup in supports
                      if g5_passing(ctx, m, cd, b, k, sup)]
            if needed and adv is None:
                raise Refusal("adversarial.json absent while rows pass G5")
            adversarial = adv or {}
            missing = [x for x in needed if x not in adversarial]
            if missing:
                raise Refusal("adversarial.json does not list %d row(s) that pass G5"
                              % len(missing))
        rows_by_branch = {}
        all_sums = True
        for b in BRANCHES:
            rows_by_branch[b] = []
            for k, sup in supports:
                row, sums = evaluate_row(ctx, m, cd, b, k, sup, stage, adversarial)
                rows_by_branch[b].append(row)
                all_sums = all_sums and sums
        if stage == "final":
            for b in BRANCHES:
                for row in rows_by_branch[b]:
                    if not is_positive(row["token"]):
                        row["usefulness"] = None
        table["rows"] = [row for b in BRANCHES for row in rows_by_branch[b]]
        table["completeness"]["mass_sums"] = all_sums
        ct, uc = class_tokens(ctx, rows_by_branch, member_keys)
        table["class_tokens"] = ct
        table["union_clause_reached"] = uc
    guard(m["members_obj"], table)
    payload = {"members.json": members_bytes, STAGE_TABLE[stage]: dump(table)}
    for fname in sorted(payload):
        with open(os.path.join(out, fname), "wb") as fh:
            fh.write(payload[fname])
    return 0


def main(argv):
    try:
        return run(argv)
    except Refusal as exc:
        sys.stderr.write("refused: %s\n" % exc)
        return 2
    except InexactValue as exc:
        sys.stderr.write("exactness guard: %s\n" % exc)
        return 3
    except Undetermined as exc:
        sys.stderr.write("undetermined by the preregistration: %s\n" % exc)
        return 4
    except Failure as exc:
        sys.stderr.write("failure: %s\n" % exc)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
