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

Continuation, 2026-11-08: independent Codex agent k1p1_impl_a_revision,
writer-k1p1-impl-a under the root coordinator; not the original Claude session.
Common inputs: AGENTS.md, the original draft above, preregistration and all A1
files at d92e0882e7609e91e3458193391e89610fffa777, K at the pin above,
and the coordinator's common/role briefs. A1 is a disclosed behavior-only
cross-writer channel. No B/controls code, output or checkpoint was read.
Shared dependencies: those common specifications and Python 3.11 stdlib;
no shared implementation, formatter or library. WIP / UNVERIFIED, pre-F.

Exit statuses (A1 section 4): 0 files written; 2 refusal; 3 exactness guard;
1 other failure. Nothing is written on a nonzero exit.

Usage (the instance route requires separate scientific authorization):
  python3 -I verification/lean/k1p1_enum_a.py --stage {members|rows|final}
      --record <rec> --out <out> [--members-sha256 <hex>]
  python3 -I verification/lean/k1p1_enum_a.py --fixture <id>
      --input <file> --out <out>

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


class Failure(Exception):
    """Exit 1: an internal check of stage M fails."""


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


def state_space(width, q):
    """All tuples of cells, in the declared lexicographic order (M1)."""
    return [tuple(s) for s in itertools.product(range(q), repeat=width)]


class CellMap:
    """A cell-by-cell map: each output cell is an explicit linear form.

    A form is the tuple of its coefficients in the declared cell order.
    Applying it uses cell sums; symbolic propagation substitutes forms into
    forms, preserving A's method on both admitted routes.
    """

    def __init__(self, cells, q, forward, backward):
        self.cells = list(cells)
        self.q = q
        self.forward = tuple(forward)
        self.backward = tuple(backward)

    def apply(self, state, inverse=False):
        rules = self.backward if inverse else self.forward
        return tuple(sum(c * state[j] for j, c in enumerate(form)) % self.q
                     for form in rules)

    def evolve(self, state, ticks):
        for _ in range(abs(ticks)):
            state = self.apply(state, inverse=ticks < 0)
        return state

    def propagate(self, forms):
        width = len(self.cells)
        return tuple(tuple(sum(coef * forms[j][k] for j, coef in enumerate(rule)) % self.q
                           for k in range(width)) for rule in self.forward)


def instance_map(n, q):
    """Build K's coordinate formulas as cell forms, only on the instance path.

    phi(x,y)=(y,Ay-x); phi^-1(x,y)=(Ax-y,x), with periodic neighbours.
    Multiple occurrences are added mod q, also when neighbour sites coincide.
    """
    width = 2 * n
    identity = [tuple(int(i == j) for j in range(width)) for i in range(width)]
    forward, backward = list(identity[n:]), []
    for i in range(n):
        forward.append(tuple((int(j == n + (i - 1) % n)
                              + int(j == n + (i + 1) % n) - int(j == i)) % q
                             for j in range(width)))
        backward.append(tuple((int(j == (i - 1) % n) + int(j == (i + 1) % n)
                               - int(j == n + i)) % q for j in range(width)))
    backward.extend(identity[:n])
    return CellMap(cell_names(n), q, forward, backward)


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

def region_e(mapping, t_window, v_cell, sigma_cells):
    """R0: substitute symbolic forms through the supplied cell rules."""
    names = mapping.cells
    width = len(names)
    forms = tuple(tuple(int(j == i) for j in range(width)) for i in range(width))
    v = names.index(v_cell)
    hit = set()
    for tick in range(t_window + 1):
        for j, coefficient in enumerate(forms[v]):
            if coefficient % mapping.q:
                hit.add(j)
        if tick < t_window:
            forms = mapping.propagate(forms)
    return [names[j] for j in sorted(hit) if names[j] not in sigma_cells]


def region_w_eq(names, v_cell):
    """W_eq: V's site set, both slices, in the supplied cell order."""
    site = v_cell.split("_")[1]
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

def stage_m(mapping, image=None):
    names, q = mapping.cells, mapping.q
    S = state_space(len(names), q)  # M1
    size_s = len(S)
    distinct = (len(set(S)) == size_s) and (size_s == q ** len(names))
    fwd = ({s: mapping.apply(s) for s in S} if image is None else image)  # M2
    bwd = {s: mapping.apply(s, inverse=True) for s in S} if image is None else None
    bijection = set(fwd.values()) == set(S)
    if bwd is not None:
        bijection = (bijection and all(bwd.get(fwd[s]) == s for s in S)
                     and all(fwd.get(bwd[s]) == s for s in S))
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
    return {
        "S": S, "fwd": fwd, "bwd": bwd, "cycles": cycles,
        "members_obj": members_obj,
        "completeness": {
            "states": size_s, "length_sum": length_sum, "cycles": len(cycles),
            "distinct": distinct, "bijection": bijection, "partition": partition,
            "mass_sums": None,
        },
    }


def instance_preserved(m):
    """Instance-only preserved measurements; fixtures never call this."""
    S, fwd = m["S"], m["fwd"]
    order, cur = 0, list(S)
    while True:
        cur = [fwd[t] for t in cur]
        order += 1
        if cur == S:
            break
        if order > len(S):
            raise Failure("phi order exceeds |S|")
    shells = {str(v): 0 for v in range(Q)}
    for state in S:
        shells[str(energy(state, N, Q))] += 1
    return {"energy_conserved": all(energy(fwd[s], N, Q) == energy(s, N, Q) for s in S),
            "shell_sizes": shells, "phi_order": order}


# ---------------------------------------------------------------------------
# Readiness, NB and usefulness for a weighted law (R2, R3, R4)
# ---------------------------------------------------------------------------

class Frame:
    """Per-(W, t_u) data over all of S at instance (n, q)."""

    def __init__(self, S, mapping, w_cells, shift, e_cells, sigma, readout, window):
        self.q = mapping.q
        self.w_idx = [mapping.cells.index(c) for c in w_cells]
        self.e_idx = [mapping.cells.index(c) for c in e_cells]
        self.sig_idx = [mapping.cells.index(c) for c in sigma]
        self.v = mapping.cells.index(readout)
        self.shift = shift
        self.wval = {s: restrict(mapping.evolve(s, shift), self.w_idx) for s in S}
        self.evalue = {s: restrict(s, self.e_idx) for s in S}
        self.zero = {s: all(s[i] == 0 for i in self.e_idx) for s in S}
        self.sigma = {s: restrict(s, self.sig_idx) for s in S}
        self.readout = {}
        for s in S:
            r, t = [], s
            for _ in range(window + 1):
                r.append(str(t[self.v]))
                t = mapping.apply(t)
            self.readout[s] = "".join(r)
        self.all_w = values_of(self.w_idx, mapping.q)
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


def unique_object(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise Refusal("duplicate JSON object key")
        obj[key] = value
    return obj


def parse_json(data):
    try:
        return json.loads(data.decode("utf-8"), object_pairs_hook=unique_object)
    except (ValueError, UnicodeError) as exc:
        raise Refusal("input is not UTF-8 JSON: %s" % exc)


def read_bytes(path):
    try:
        with open(path, "rb") as fh:
            return fh.read()
    except OSError as exc:
        raise Refusal("input unreadable: %s" % exc)


def read_json(path):
    return parse_json(read_bytes(path))


def exact_keys(obj, keys):
    return isinstance(obj, dict) and set(obj) == set(keys)


def valid_decisions(cd):
    if not isinstance(cd, dict) or cd.get("g1") not in ("pass", "undecided"):
        return False
    for key in ("class_rule", "support_restriction"):
        part = cd.get(key)
        if not exact_keys(part, ("a", "t1")):
            return False
        if any(v not in ("pass", "flag", "undecided") for v in part.values()):
            return False
    return True


def load_class_decisions(rec):
    cd = read_json(os.path.join(rec, "class-decisions.json"))
    keys = ("schema", "version", "derivations", "g1", "class_rule",
            "support_restriction", "s0_paper")
    ok = (exact_keys(cd, keys) and cd["schema"] == "k1p1-class-decisions"
          and type(cd["version"]) is int and cd["version"] == 1
          and cd["derivations"] == ["derivations/P1-class-paper.md", "derivations/S0-paper.md"]
          and valid_decisions(cd) and exact_keys(cd["s0_paper"], S0_PAPER_KEYS)
          and all(v in ("pass", "fail", "undecided") for v in cd["s0_paper"].values()))
    if not ok:
        raise Refusal("class-decisions.json does not match A1 Q11")
    return cd


def check_members_file(rec, pinned, computed_bytes):
    path = os.path.join(rec, "members.json")
    if pinned is None:
        raise Refusal("--members-sha256 is required at this stage")
    if len(pinned) != 64 or any(c not in "0123456789abcdef" for c in pinned):
        raise Refusal("--members-sha256 is not 64 lowercase hexadecimal characters")
    if not os.path.isfile(path):
        raise Refusal("members.json absent")
    data = read_bytes(path)
    if hashlib.sha256(data).hexdigest() != pinned:
        raise Refusal("members.json differs from its pinned digest")
    if data != computed_bytes:
        raise Refusal("members.json differs from the members.json computed here")


def adversarial_entries(entries, with_note):
    if not isinstance(entries, list):
        raise Refusal("adversarial rows must be a list")
    keys = ("branch", "member", "token", "note") if with_note else ("branch", "member", "token")
    table = {}
    for entry in entries:
        if not exact_keys(entry, keys) or any(not isinstance(v, str) for v in entry.values()):
            raise Refusal("adversarial entry malformed")
        key = (entry["branch"], entry["member"])
        if key in table:
            raise Refusal("adversarial record lists a row twice")
        table[key] = entry["token"]
    return table


def load_adversarial(rec):
    path = os.path.join(rec, "adversarial.json")
    if not os.path.exists(path):
        return None
    adv = read_json(path)
    if not (exact_keys(adv, ("schema", "version", "rows"))
            and adv["schema"] == "k1p1-adversarial"
            and type(adv["version"]) is int and adv["version"] == 1):
        raise Refusal("adversarial.json does not match A1 Q10")
    return adversarial_entries(adv["rows"], with_note=True)


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

def build_context(m, mapping, window, readout, sigma):
    S = m["S"]
    e_cells = region_e(mapping, window, readout, sigma)
    w_eq = region_w_eq(mapping.cells, readout)
    w_by_branch = {"B-pl": [], "B-eq": w_eq, "B-ct": w_eq}
    frames = {b: Frame(S, mapping, w_by_branch[b], TU_SHIFT[b], e_cells,
                       sigma, readout, window) for b in BRANCHES}
    overlap = {"B-eq": [c for c in w_eq if c in e_cells], "B-ct": []}
    region = {
        "E": e_cells, "W_eq": w_eq,
        "q_pow_minus_E": ratio(1, mapping.q ** len(e_cells)),
        "overlap": overlap,
        "overlap_tautological": {b: bool(overlap[b]) for b in ("B-eq", "B-ct")},
    }
    return {"S": S, "E": e_cells, "W": w_by_branch, "frames": frames, "region": region,
            "map": mapping, "window": window, "readout": readout, "sigma": sigma,
            "q": mapping.q}


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
    frame = Frame(S, ctx["map"], w_cells, -1, ctx["E"],
                  ctx["sigma"], ctx["readout"], ctx["window"])
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
    f_abs = Frame(S, ctx["map"], ["x_3", "y_3"], 0, e_cells,
                  ctx["sigma"], ctx["readout"], ctx["window"])
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
    S6 = state_space(2 * n6, Q)
    map6 = instance_map(n6, Q)
    w6 = [cell_index(c, n6) for c in ("x_0", "x_1", "y_0", "y_1")]
    x2 = cell_index("x_2", n6)
    event = [s for s in S6
             if all(s[i] == 0 for i in w6) and all(map6.apply(s, inverse=True)[i] == 0 for i in w6)]
    computed["CC-IMP″"] = {"fixes_x2_zero": bool(event) and all(s[x2] == 0 for s in event)}

    # CC-PASS and CC-T2: O_1 = "W_eq identical at t_u - 1 and t_u", t_u = t_0.
    weq_idx = [cell_index(c, N) for c in ctx["W"]["B-eq"]]
    image = {s for s in S if restrict(ctx["map"].apply(s, inverse=True), weq_idx) == restrict(s, weq_idx)}
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
    q = ctx["q"]
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
        bound_ok = q ** len(e_cells) * size <= len(S)
        verdict = "holds" if bound_ok else "breaks"
        ledger = "D=log(%s); (c1) |E|=%d: %s" % (rat(d_ratio), len(e_cells), verdict)
        breaks = (not bound_ok) and bool(r["sharp"])
    elif branch == "B-eq":
        bound_ok = {}
        items = []
        for w in r["sharp"]:
            a, b = parts(r["mass"][w])
            bound_ok[w] = q ** (a * k) * size ** b <= len(S) ** b
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
                gates["G7"] = "pending"
                token = "pending"
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
            uc[b] = False
            continue
        if all(is_positive(t) for t in toks):
            uc[b] = True
            ct[b] = None
            continue
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
    out = ([table["region"]["q_pow_minus_E"]] if "region" in table else [])
    for c in table.get("controls", []):
        for side in ("computed", "expected"):
            obj = c[side]
            for f in RATIONAL_CONTROL_FIELDS.get(c["id"], ()):
                v = obj.get(f) if isinstance(obj, dict) else None
                out.extend(v.values() if isinstance(v, dict) else [v])
    for rw in table.get("rows", []):
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


# A1 section 5.2: ids and SHA-256 of admitted raw canonical input bytes.
# These are admission pins, never expected computational answers.
FIXTURE_INPUTS = {
    "SF-1a": "0e0d87f8b6ca82646134383abc08158fc5546a133b25d60ee513890ed7350bf1",
    "SF-1b": "c15b30da87758d7d7d762f6cf3b282c0490f9243e7f88d7b97db800811689dc9",
    "SF-1c": "d44e2700ddb8e50e1061c8846d6a8ee82092583af59ac44df0bbac361448643c",
    "SF-2p": "f7d444061e8c2bfa427f66e5df7ff43ae80bf7b22548391ee340b67b66b845a7",
    "SF-2pb": "b8048192ccffc506f9e18981045048633ce9af1ceba1ac5f29c76fc1add20630",
    "SF-3": "9f6fd0a2bb09127350b1b4a8edc323c3989f95fc1097064ecfe96d31740af36a",
    "SF-3f": "80319c62df77dc8a95a16d4e640fc0c44cf4a2c9aafa6f30006ba39b2271a8af",
    "SF-3g": "03dae8724f09cbbe68e983a6dd1717f370ddf4bf2ea194c4a7716f1ca02c8064",
}


def parse_args(argv):
    opts = {}
    allowed = ("--stage", "--record", "--out", "--members-sha256", "--fixture", "--input")
    i = 0
    while i < len(argv):
        key = argv[i]
        if (key not in allowed or key in opts or i + 1 >= len(argv)
                or argv[i + 1].startswith("--")):
            raise Refusal("unknown/repeated flag or missing value")
        opts[key] = argv[i + 1]
        i += 2
    if "--fixture" in opts:
        if set(opts) != {"--fixture", "--input", "--out"}:
            raise Refusal("fixture mode requires --fixture --input --out exclusively")
    else:
        if not {"--stage", "--record", "--out"} <= set(opts):
            raise Refusal("instance mode requires --stage --record --out")
        if set(opts) - {"--stage", "--record", "--out", "--members-sha256"}:
            raise Refusal("fixture and instance flags are mutually exclusive")
        if opts["--stage"] not in STAGE_TABLE:
            raise Refusal("unknown stage")
        if opts["--stage"] in ("rows", "final") and "--members-sha256" not in opts:
            raise Refusal("--members-sha256 is required at this stage")
        if "--members-sha256" in opts:
            pin = opts["--members-sha256"]
            if len(pin) != 64 or any(c not in "0123456789abcdef" for c in pin):
                raise Refusal("--members-sha256 is not a lowercase SHA-256")
    return opts


def fresh_out(out):
    try:
        ok = os.path.isdir(out) and not os.listdir(out)
    except OSError as exc:
        raise Refusal("--out unreadable: %s" % exc)
    if not ok:
        raise Refusal("--out is not an existing empty directory")


def write_payload(out, payload):
    """All checks precede this transaction; undo owned files on an I/O failure."""
    staged, installed = [], []
    try:
        for name in sorted(payload):
            temp = os.path.join(out, ".k1p1-" + name)
            with open(temp, "xb") as fh:
                staged.append(temp)
                fh.write(payload[name])
        for name, temp in zip(sorted(payload), staged):
            target = os.path.join(out, name)
            os.replace(temp, target)
            installed.append(target)
    except Exception:
        for path in staged + installed:
            if os.path.exists(path):
                os.unlink(path)
        raise


def fill_rows(table, ctx, m, cd, stage, adversarial):
    """The same complete R1-R10 and CLASS pipeline for both routes."""
    if not m["completeness"]["partition"]:
        raise Refusal("CT-INC: CC-PART does not hold")
    supports = member_supports(m)
    member_keys = [key for key, _ in supports]
    if member_keys != [mm["key"] for mm in m["members_obj"]["members"]]:
        raise Refusal("CT-INC: member list differs from M5")
    needed = []
    if stage == "final":
        needed = [(b, key) for b in BRANCHES for key, support in supports
                  if g5_passing(ctx, m, cd, b, key, support)]
        if needed and adversarial is None:
            raise Refusal("adversarial record absent while rows pass G5")
        if any(key not in (adversarial or {}) for key in needed):
            raise Refusal("adversarial record does not cover every G5 row")
    by_branch, all_sums = {}, True
    for branch in BRANCHES:
        by_branch[branch] = []
        for key, support in supports:
            row, sums = evaluate_row(ctx, m, cd, branch, key, support,
                                     stage, adversarial or {})
            by_branch[branch].append(row)
            all_sums = all_sums and sums
    table["rows"] = [row for b in BRANCHES for row in by_branch[b]]
    table["completeness"]["mass_sums"] = all_sums
    table["class_tokens"], table["union_clause_reached"] = class_tokens(ctx, by_branch, member_keys)


def fixture_map(data):
    cells, q = data["cells"], data["q"]
    forms = []
    for key in ("phi", "phi_inv"):
        rules = data[key]
        if not exact_keys(rules, cells):
            raise Refusal("cell-form keys differ from cells")
        ordered = []
        for cell in cells:
            terms = rules[cell]
            if (not isinstance(terms, list) or any(c not in cells for c in terms)
                    or terms != sorted(set(terms), key=cells.index)):
                raise Refusal("invalid cell form")
            ordered.append(tuple(int(c in terms) for c in cells))
        forms.append(ordered)
    return CellMap(cells, q, forms[0], forms[1])


def fixture_payload(fixture_id, input_path):
    # Admission is deliberately before parsing, constructing a map or walking states.
    if fixture_id not in FIXTURE_INPUTS:
        raise Refusal("fixture id is not admitted for A")
    raw = read_bytes(input_path)
    if hashlib.sha256(raw).hexdigest() != FIXTURE_INPUTS[fixture_id]:
        raise Refusal("fixture input differs from its frozen digest")
    data = parse_json(raw)
    if not isinstance(data, dict) or data.get("id") != fixture_id:
        raise Refusal("fixture id mismatch")
    kind = data.get("kind")
    keys = {"id", "kind", "cells", "image"} if kind == "perm" else {
        "id", "kind", "q", "kmax", "cells", "phi", "phi_inv"}
    if kind == "system":
        keys |= {"T", "stage", "sigma", "readout", "class_decisions", "adversarial"}
    if kind not in ("perm", "linear", "system") or not exact_keys(data, keys):
        raise Refusal("fixture schema mismatch")
    cells = data["cells"]
    if (not isinstance(cells, list) or not cells or any(not isinstance(c, str) for c in cells)
            or len(set(cells)) != len(cells)):
        raise Refusal("invalid fixture cells")
    image = None
    if kind == "perm":
        # No inverse is required for an explicit permutation (A1 section 5.3).
        width = len(cells)
        identity = [tuple(int(i == j) for j in range(width)) for i in range(width)]
        mapping = CellMap(cells, 2, identity, identity)
        states = state_space(width, mapping.q)
        state_names = {sstr(s) for s in states}
        if (not exact_keys(data["image"], state_names)
                or any(t not in state_names for t in data["image"].values())):
            raise Refusal("permutation image is outside the state space")
        image = {s: tuple(int(c) for c in data["image"][sstr(s)]) for s in states}
    else:
        if (type(data["q"]) is not int or data["q"] != 2
                or type(data["kmax"]) is not int or data["kmax"] <= 0):
            raise Refusal("invalid fixture field/range")
        mapping = fixture_map(data)
    m = stage_m(mapping, image)
    obj = {"schema": "k1p1-fixture-output", "version": 1, "fixture": fixture_id, "kind": kind,
           "cell_order": cells, "members": m["members_obj"]["members"],
           "histogram": m["members_obj"]["histogram"],
           "completeness": dict(m["completeness"])}
    if kind == "system":
        if (type(data["T"]) is not int or data["T"] < 0
                or data["stage"] not in ("rows", "final")
                or len(cells) % 2 or cells != cell_names(len(cells) // 2)
                or not isinstance(data["sigma"], list)
                or any(c not in cells for c in data["sigma"])
                or data["readout"] not in cells
                or not exact_keys(data["class_decisions"],
                                  ("g1", "class_rule", "support_restriction"))
                or not valid_decisions(data["class_decisions"])):
            raise Refusal("invalid toy system")
        adversarial = adversarial_entries(data["adversarial"], with_note=False)
        if data["stage"] == "rows" and adversarial:
            raise Refusal("rows fixture must have no adversarial entries")
        ctx = build_context(m, mapping, data["T"], data["readout"], data["sigma"])
        obj.update({"stage": data["stage"],
                    "region": dict(ctx["region"], q_pow_minus_E=rat(ctx["region"]["q_pow_minus_E"]))})
        fill_rows(obj, ctx, m, data["class_decisions"], data["stage"], adversarial)
    guard(m["members_obj"], obj)
    return {"fixture.json": dump(obj)}


def instance_payload(opts):
    """Only the explicit --stage route can read instance inputs/build K's map."""
    stage, rec = opts["--stage"], opts["--record"]
    pinned = opts.get("--members-sha256")
    cd = load_class_decisions(rec)
    mapping = instance_map(N, Q)
    m = stage_m(mapping)
    members_bytes = dump(m["members_obj"])
    if stage in ("rows", "final"):
        check_members_file(rec, pinned, members_bytes)
    ctx = build_context(m, mapping, T, V_CELL, SIGMA_CELLS)
    controls = compute_controls(ctx, cd)
    table = {
        "schema": "k1p1-gate-table", "version": 1, "stage": stage,
        "instance": {"N": N, "a": A_COUP, "d": D_DIM, "q": Q},
        "region": dict(ctx["region"], q_pow_minus_E=rat(ctx["region"]["q_pow_minus_E"])),
        "preserved": instance_preserved(m), "completeness": dict(m["completeness"]),
        "controls": controls, "rows": [], "class_tokens": {}, "union_clause_reached": {},
    }
    if walk_floats(controls) or not is_rational_string(table["region"]["q_pow_minus_E"]):
        raise InexactValue("a float in the region or S0 controls")
    if stage != "members":
        if any(c["outcome"] != "pass" for c in controls):
            raise Refusal("S0 control failed at stage %s" % stage)
        adv = load_adversarial(rec) if stage == "final" else None
        fill_rows(table, ctx, m, cd, stage, adv)
    guard(m["members_obj"], table)
    return {"members.json": members_bytes, STAGE_TABLE[stage]: dump(table)}


def run(argv):
    opts = parse_args(argv)
    out = opts["--out"]
    fresh_out(out)
    if "--fixture" in opts:
        payload = fixture_payload(opts["--fixture"], opts["--input"])
    else:
        payload = instance_payload(opts)
    write_payload(out, payload)
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
    except Exception as exc:
        sys.stderr.write("failure: %s\n" % exc)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
