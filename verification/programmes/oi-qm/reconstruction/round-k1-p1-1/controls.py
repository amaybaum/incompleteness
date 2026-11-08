#!/usr/bin/env python3
"""K1-P1-1 controls (preregistration §8.1, §9, §10, §11).

Header (preregistration §8.1)
  Author session: writer-k1p1-ctl, the controls writer of §8.1 (dispatched by the
    coordinator under the name "writer-k1p1-controls"); Claude Code session
    https://claude.ai/code/session_011zDyUSyEszk3JJx83uXKKq.
  Access to another implementation: none. The writer received the preregistration at
    4ca431afb1bfee0cdf301f0917c73068fdf09b58 and the adopted text K at
    d9b3de012e393262adb20f91ad49627bad48de43 (its section 2 table), and read neither
    implementation A nor implementation B.
  Shared dependency: none. Standard library only; imports limited to §8.1's list.
  Python: 3.11 (§8.1).

Status: DRAFT before F, written under the owner's Stage 2 authorization (#1031 comment
6677496553, amaybaum, 2026-11-06T05:11:18Z): pre-F code drafting, static analysis and
predeclared synthetic-fixture tests only. WIP / UNVERIFIED.

Continuation: writer-k1p1-ctl / independent agent k1p1_controls_revision, 2026-11-08,
  under the Codex coordinator. This is a distinct continuation context, not the original
  Claude session. Shared behavioral input: adopted A1 at d92e0882e7609e91e3458193391e89610fffa777,
  pinned companion fixtures, AGENTS.md and the coordinator's common/role briefs. No A/B
  source, output, revised checkpoint or provisional patch package read by this context.
  Static-only drafting initially; no scientific instance execution authorized.
Final patch bindings are a delivery dependency: absent bindings always refuse self-tests.

Command lines (§10.1), run from the repository root:
  python3 -I <rec>/controls.py run --stage {members|rows|final}
  python3 -I <rec>/controls.py check [--stage {members|rows|final}]
  python3 -I <rec>/controls.py self-test {--synthetic | --stage {members|rows|final}}
  python3 -I <rec>/controls.py render

Exit statuses: 0 every check and comparison holds; 1 a check, comparison or mutation
failed; 2 a refusal (a stage precondition, or an OPEN point).
"""

import ast
import hashlib
import itertools
import json
import os
import subprocess
import sys
import tempfile
from fractions import Fraction


class Refusal(Exception):
    """A precondition or missing pinned input (exit status 2)."""


CHECK_ID_EXACT = "EXACT"
CHECK_ID_TOKENS = "TOKENS"
FIXTURE_SHA256 = "691aedbf0c9e74fdcc64f4c9c35f5e07c8ffc362e74360d4e541df682c750e85"
# Filled only from root's final independently reviewed patch bytes, never guessed.
PATCH_SHA256 = {"MU-C1": None, "MU-C2": None, "MU-C3": None}


# ---------------------------------------------------------------------------
# Constants fixed by the preregistration
# ---------------------------------------------------------------------------

REC_REL = "verification/programmes/oi-qm/reconstruction/round-k1-p1-1"
IMPL = {
    "A": "verification/lean/k1p1_enum_a.py",
    "B": "verification/lean/k1p1_enum_b.py",
}
STAGES = ("members", "rows", "final")
GATE_TABLE = {
    "members": "gate-table.members.json",
    "rows": "gate-table.rows.json",
    "final": "gate-table.json",
}
CHECKS_FILE = {
    "members": "checks.members.json",
    "rows": "checks.rows.json",
    "final": "checks.json",
}
# Files each stage commits (§10.1), the checks file last.
STAGE_FILES = {
    "members": ("members.json", "cyc2.json", "gate-table.members.json", "checks.members.json"),
    "rows": ("gate-table.rows.json", "checks.rows.json"),
    "final": ("gate-table.json", "checks.json"),
}
BRANCHES = ("B-pl", "B-eq", "B-ct")

ALLOWED_IMPL_IMPORTS = frozenset(("fractions", "itertools", "json", "hashlib", "sys", "os"))
ALLOWED_CTL_IMPORTS = ALLOWED_IMPL_IMPORTS | frozenset(("subprocess", "tempfile", "ast"))

# Instance (§5; K lines 31-35).
N = 5
Q = 2
CELLS = tuple(["x_" + str(i) for i in range(N)] + ["y_" + str(i) for i in range(N)])
S_SIZE = Q ** (2 * N)

# Unicode (§10.2).
PI0_NAME = "π_0"
CLASS_SET = "\U0001D4D8"
PRIME = "′"
DPRIME = "″"

H_INV = "H-inv[K-17(a)]"
ACCESS = {
    "B-pl": ("H-cur (declared)",),
    "B-eq": ("H-cur (declared)", "H-2s (declared)"),
    "B-ct": ("H-cur (declared)", "H-2s (declared)", "H-ret"),
}
W_RULE = {
    "B-pl": "W trivial; t_u = t_0",
    "B-eq": "W_eq: site set of V, both slices; t_u = t_0",
    "B-ct": "W_eq: site set of V, both slices; t_u = t_0 - 1",
}
W_INPUTS = {"B-pl": [], "B-eq": ["V"], "B-ct": ["V"]}
ROW_KEYS = frozenset((
    "bound_ok", "branch", "candidate", "d_ratio", "g2", "gates", "hypotheses", "ledger",
    "mass", "member", "nb", "nb_g1", "pi0_ref", "sharp_w", "support_size", "token",
    "usefulness", "w_certified", "w_inputs", "w_rule", "weak",
))
GATES = ("G1", "G2", "G3", "G4", "G5", "G6", "G7")
NR = "not-reached"

MEMBERS_ROSTER = ("PRE-INPUTS", "IMPORTS", "AB-members", "AB-gate-table", "EXACT",
    "CC-ABS", "CC-EXACT", "CC-SCOPE", "CC-LEDGER", "CC-IMP", "CC-IMP′", "CC-IMP″",
    "CC-PASS", "CC-T2", "POS-X", "CC-BLIND", "PR-S0", "CC-COUNT", "CC-BIJ", "CC-PART",
    "CC-CYC2", "CT-INC", "PR-E", "PR-CYC", "PR-EN", "PR-P1c")
ROWS_ROSTER = (("PRE-INPUTS", "PRE-PREV", "PRE-CHECK") + MEMBERS_ROSTER[1:21] +
    ("CC-ROWS", "CC-MASS", "CT-INC", "PR-E", "PR-CYC", "PR-EN", "PR-P1c", "PR-IND",
     "PR-BLIND", "PR-LEDGER", "PR-CR6", "PR-P0", "TOKENS"))
FINAL_ROSTER = (("PRE-INPUTS", "PRE-PREV", "PRE-ADV", "PRE-CHECK") + ROWS_ROSTER[3:] + ("ADV-INDEX",))
ROSTERS = {"members": MEMBERS_ROSTER, "rows": ROWS_ROSTER, "final": FINAL_ROSTER}

# S0 controls (K §6 order; §10.2 table).
S0_ORDER = ("CC-ABS", "CC-EXACT", "CC-SCOPE", "CC-LEDGER", "CC-IMP", "CC-IMP" + PRIME,
            "CC-IMP" + DPRIME, "CC-PASS", "CC-T2", "POS-X", "CC-BLIND")
S0_GATE = dict(zip(S0_ORDER, (
    "G4", "G4", "G4", "G3/G4", "G2, G3", "G2(a)", "G2(a); T1; T2's no-image disjunct",
    "G2(b)", "G2(b) T2", "G3, G4, G7", "G4")))
S0_PAPER_IDS = ("CC-LEDGER", "CC-IMP", "CC-IMP" + PRIME, "CC-IMP" + DPRIME, "CC-PASS", "CC-T2")
S0_EXPECTED = {
    "CC-ABS": {"sharp_w": [], "weak": {"00": "1/8", "01": "1/8", "10": "1/8", "11": "1/8"}},
    "CC-EXACT": {"sharp_w": [], "weak": {"": "153/160"}},
    "CC-SCOPE": {b: {"nb_all_false": True, "sharp": True} for b in BRANCHES},
    "CC-LEDGER": {"c1": False, "d_ratio": "2/1", "shell_size": 512},
    "CC-IMP": {"d_ratio": "8/1", "support_size": 128},
    "CC-IMP" + PRIME: None,
    "CC-IMP" + DPRIME: {"fixes_x2_zero": True},
    "CC-PASS": {"hsel_content": {"B-eq": [], "B-pl": [{"values": ["000", "001", "110", "111"], "w": ""}]},
                "image_equals_stated": True},
    "CC-T2": {"image_equals_stated": False},
    "POS-X": {"g3_void": False, "mass_w0": "1/64", "nb_w0": True, "sharp_w0": True,
              "token": "CONDITIONAL[H-2s (declared), H-cur (declared), H-ret, H-μ, finite-S posit]",
              "w_certified": True},
    "CC-BLIND": {"mass_w0": "1/256", "nb_w0": False, "sharp_w0": True},
}
# Rational leaves of the S0 computed/expected objects (exactness guard).
S0_RATIONAL_PATHS = {
    "CC-ABS": (("weak", "*"),),
    "CC-EXACT": (("weak", "*"),),
    "CC-LEDGER": (("d_ratio",),),
    "CC-IMP": (("d_ratio",),),
    "POS-X": (("mass_w0",),),
    "CC-BLIND": (("mass_w0",),),
}

# Preserved results (§4).
PR_E_E = ["x_1", "y_1", "y_2"]
PR_E_WEQ = ["x_1", "y_1"]
PR_CYC_HIST = {"1": 2, "2": 1, "5": 102, "10": 51}
PR_CYC_FIXED = ["0000000000", "1111111111"]
PR_CYC_TWO = ["0000011111", "1111100000"]
PR_CYC_ORDER = 10
PR_EN_SHELLS = {"0": 512, "1": 512}
PR_P0_WEAK = {
    "B-pl": {"": "1/8"},
    "B-eq": {"00": "1/2", "01": "0/1", "10": "0/1", "11": "0/1"},
    "B-ct": {"00": "1/4", "01": "0/1", "10": "1/4", "11": "0/1"},
}
DELTA0 = "0" * (2 * N)


# ---------------------------------------------------------------------------
# Serialization and exact values (§7, §10.2)
# ---------------------------------------------------------------------------

def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def dumps(obj):
    return (canon(obj) + "\n").encode("utf-8")


def same(a, b):
    """Equality of JSON values with types kept apart (true is not 1)."""
    return canon(a) == canon(b)


def loads(data):
    def pairs(items):
        out = {}
        for k, v in items:
            if k in out:
                raise ValueError("duplicate key " + repr(k))
            out[k] = v
        return out

    def constant(name):
        raise ValueError("non-finite constant " + name)

    return json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant)


def _digits(t):
    return len(t) > 0 and all(c in "0123456789" for c in t)


def parse_rational(s):
    """Parse "p/q" in lowest terms with q > 0; zero is "0/1". Raises ValueError otherwise."""
    if not isinstance(s, str):
        raise ValueError("rational is not a string: " + repr(s))
    parts = s.split("/")
    if len(parts) != 2:
        raise ValueError("not p/q: " + repr(s))
    p, q = parts
    neg = p.startswith("-")
    pd = p[1:] if neg else p
    if not _digits(pd) or not _digits(q):
        raise ValueError("not p/q: " + repr(s))
    if (len(pd) > 1 and pd[0] == "0") or (len(q) > 1 and q[0] == "0"):
        raise ValueError("leading zero: " + repr(s))
    num, den = int(pd), int(q)
    if neg:
        if num == 0:
            raise ValueError("negative zero: " + repr(s))
        num = -num
    if den <= 0:
        raise ValueError("denominator not positive: " + repr(s))
    fr = Fraction(num, den)
    if fr.numerator != num or fr.denominator != den:
        raise ValueError("not in lowest terms: " + repr(s))
    return fr


def fmt_rational(fr):
    fr = Fraction(fr)
    return str(fr.numerator) + "/" + str(fr.denominator)


def is_int(x):
    return type(x) is int


def is_bool(x):
    return type(x) is bool


def is_state(s):
    return isinstance(s, str) and len(s) == 2 * N and all(c in "01" for c in s)


def is_bits(s, n):
    return isinstance(s, str) and len(s) == n and all(c in "01" for c in s)


def float_paths(obj, path="$"):
    out = []
    if isinstance(obj, float):
        out.append(path)
    elif isinstance(obj, dict):
        for k in sorted(obj):
            out.extend(float_paths(obj[k], path + "." + k))
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            out.extend(float_paths(v, path + "[" + str(i) + "]"))
    return out


# ---------------------------------------------------------------------------
# The instance map, used only by CC-PART (closure and single orbit) and PR-P1c.
# Nothing here runs at import; the state list is built on demand.
# ---------------------------------------------------------------------------

def phi(s):
    """phi(x, y) = (y, Ay - x), (Ay)_i = y_{i-1} + y_{i+1}, over Z/Q (§5)."""
    x = [int(c) for c in s[:N]]
    y = [int(c) for c in s[N:]]
    ay = [(y[(i - 1) % N] + y[(i + 1) % N]) % Q for i in range(N)]
    ny = [(ay[i] - x[i]) % Q for i in range(N)]
    return "".join(str(v) for v in y + ny)


def instance_states():
    return ["".join(p) for p in itertools.product("01", repeat=2 * N)]


def partition_findings(universe, step, cycles):
    """Generic CC-PART: `cycles` is a list of (key, size, states) in report order.

    Passes (returns []) iff the cycles are listed by increasing key, each key is the least
    state of its cycle, each size is its length, each state list is sorted and distinct,
    every element of `universe` lies in exactly one cycle, the sizes sum to |universe|, and
    each cycle is exactly the orbit of its key under `step` (closure and single orbit).
    """
    f = []
    uni = set(universe)
    seen = set()
    total = 0
    prev = None
    for idx, (key, size, states) in enumerate(cycles):
        tag = "cycle #" + str(idx) + " (" + str(key) + ")"
        states = list(states)
        if not states:
            f.append(tag + ": empty")
            continue
        if states != sorted(states):
            f.append(tag + ": states not sorted")
        if len(set(states)) != len(states):
            f.append(tag + ": repeated state")
        if key != min(states):
            f.append(tag + ": key is not the least state")
        if not is_int(size) or size != len(states):
            f.append(tag + ": size differs from its state count")
        if prev is not None and not key > prev:
            f.append(tag + ": keys not strictly increasing")
        prev = key
        total += size if is_int(size) else 0
        for s in states:
            if s not in uni:
                f.append(tag + ": state outside the universe")
            if s in seen:
                f.append(tag + ": state in two cycles")
            seen.add(s)
        if any(step(s) not in set(states) for s in states):
            f.append(tag + ": not closed under the map (p3)")
        orbit = [key]
        cur = key
        closed = False
        for _ in range(len(uni)):
            cur = step(cur)
            if cur == key:
                closed = True
                break
            orbit.append(cur)
        if not closed:
            f.append(tag + ": orbit of the key does not return within |universe| steps")
        elif sorted(orbit) != sorted(states):
            f.append(tag + ": not a single orbit closed under the map")
    if total != len(uni):
        f.append("sizes sum to " + str(total) + ", not " + str(len(uni)))
    if seen != uni:
        f.append("coverage: " + str(len(uni - seen)) + " states in no cycle")
    return f


def mobius(n):
    res = 1
    m = n
    p = 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res


# ---------------------------------------------------------------------------
# Repository context
# ---------------------------------------------------------------------------

class Ctx(object):
    def __init__(self, root):
        self.root = root
        self.rec = os.path.join(root, *REC_REL.split("/"))

    def rec_path(self, name):
        return os.path.join(self.rec, *name.split("/"))

    def read_rec(self, name):
        with open(self.rec_path(name), "rb") as fh:
            return fh.read()

    def has_rec(self, name):
        return os.path.isfile(self.rec_path(name))


def ctx_from_file():
    rec = os.path.dirname(os.path.abspath(__file__))
    norm = rec.replace(os.sep, "/")
    if not norm.endswith("/" + REC_REL):
        raise Refusal("controls.py is not at " + REC_REL + "/controls.py")
    root = rec[: len(rec) - len(REC_REL) - 1]
    return Ctx(root)


def git_env():
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    env.update({"GIT_CONFIG_GLOBAL": "/dev/null", "GIT_CONFIG_NOSYSTEM": "1"})
    return env


def git(ctx, args):
    return subprocess.run(["git", "-c", "core.hooksPath=/dev/null"] + list(args), cwd=ctx.root, env=git_env(),
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode


def tracked_and_unmodified(ctx, names):
    """§10.1: `git ls-files --error-unmatch` and `git diff --quiet HEAD --`."""
    rels = [REC_REL + "/" + n for n in names]
    for r in rels:
        if git(ctx, ["ls-files", "--error-unmatch", "--", r]) != 0:
            return False
    return git(ctx, ["diff", "--quiet", "HEAD", "--"] + rels) == 0


# ---------------------------------------------------------------------------
# IMPORTS (§8.1)
# ---------------------------------------------------------------------------

def import_findings(path, allowed):
    try:
        with open(path, "rb") as fh:
            src = fh.read()
        tree = ast.parse(src, filename=path)
    except (OSError, SyntaxError, ValueError) as exc:
        return [path + ": " + type(exc).__name__]
    f = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".")[0] not in allowed:
                    f.append(path + ":" + str(node.lineno) + ": import " + alias.name)
        elif isinstance(node, ast.ImportFrom):
            if node.level != 0 or node.module is None:
                f.append(path + ":" + str(node.lineno) + ": relative import")
            elif node.module.split(".")[0] not in allowed:
                f.append(path + ":" + str(node.lineno) + ": from " + node.module + " import")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "__import__":
            f.append(path + ":" + str(node.lineno) + ": __import__ call")
    return f


def chk_imports(ctx, impl_paths=None):
    paths = impl_paths or {k: os.path.join(ctx.root, *v.split("/")) for k, v in IMPL.items()}
    f = []
    f += import_findings(paths["A"], ALLOWED_IMPL_IMPORTS)
    f += import_findings(paths["B"], ALLOWED_IMPL_IMPORTS)
    f += import_findings(ctx.rec_path("controls.py"), ALLOWED_CTL_IMPORTS)
    return f


# ---------------------------------------------------------------------------
# Document readers
# ---------------------------------------------------------------------------

def members_cycles(mdoc, cells=None):
    cells = CELLS if cells is None else cells
    count = 2 ** len(cells)
    if set(mdoc) != {"schema", "version", "cell_order", "members", "histogram"}:
        raise ValueError("members.json keys")
    if mdoc["schema"] != "k1p1-members" or not same(mdoc["version"], 1):
        raise ValueError("members.json schema/version")
    if not same(mdoc["cell_order"], list(cells)):
        raise ValueError("members.json cell_order")
    ms = mdoc["members"]
    if not same(ms[0], {"key": "pi0", "size": count}):
        raise ValueError("members.json: first member is not pi0 of size " + str(S_SIZE))
    cycles = []
    for m in ms[1:]:
        if set(m) != {"key", "size", "states"}:
            raise ValueError("members.json: member keys")
        if not is_bits(m["key"], len(cells)) or not is_int(m["size"]) or not isinstance(m["states"], list):
            raise ValueError("members.json: member field types")
        if not all(is_bits(s, len(cells)) for s in m["states"]):
            raise ValueError("members.json: state strings")
        cycles.append((m["key"], m["size"], list(m["states"])))
    return cycles


def member_keys(mdoc, cells=None):
    return ["pi0"] + [c[0] for c in members_cycles(mdoc, cells)]


def member_name(key):
    return PI0_NAME if key == "pi0" else "u_c[" + key + "]"


def positive(token):
    return isinstance(token, str) and (token.startswith("CONDITIONAL[") or token.startswith("AVAILABLE[H-sel]("))


def class_decisions(ctx):
    cd = loads(ctx.read_rec("class-decisions.json"))
    ok = (set(cd) == {"schema", "version", "derivations", "g1", "class_rule", "support_restriction", "s0_paper"}
          and cd["schema"] == "k1p1-class-decisions" and same(cd["version"], 1)
          and same(cd["derivations"], ["derivations/P1-class-paper.md", "derivations/S0-paper.md"])
          and cd["g1"] in ("pass", "undecided"))
    for k in ("class_rule", "support_restriction"):
        ok = ok and isinstance(cd[k], dict) and set(cd[k]) == {"a", "t1"} and all(
            v in ("pass", "flag", "undecided") for v in cd[k].values())
    ok = ok and isinstance(cd["s0_paper"], dict) and set(cd["s0_paper"]) == set(S0_PAPER_IDS) and all(
        v in ("pass", "fail", "undecided") for v in cd["s0_paper"].values())
    if not ok:
        raise ValueError("class-decisions.json does not follow §10.2")
    return cd


# ---------------------------------------------------------------------------
# Checks. Each takes `env` (one implementation's documents) and returns findings;
# an empty list is a pass. CT-INC also returns "refused".
# ---------------------------------------------------------------------------

def chk_exact(env):
    """controls.py's own exactness guard (§7) on the outputs as written."""
    f = []
    for name in ("members", "gt", "cyc2"):
        doc = env.get(name)
        if doc is not None:
            f += [name + ": float at " + p for p in float_paths(doc)]
    gt = env["gt"]

    def rat(v, where):
        try:
            parse_rational(v)
        except ValueError as exc:
            f.append(where + ": " + str(exc))

    rat(gt["region"]["q_pow_minus_E"], "region.q_pow_minus_E")
    for i, r in enumerate(gt["rows"]):
        rat(r["d_ratio"], "rows[" + str(i) + "].d_ratio")
        for fld in ("weak", "mass", "pi0_ref"):
            for w, v in r[fld].items():
                rat(v, "rows[" + str(i) + "]." + fld + "." + w)
    for c in gt.get("controls", []):
        for paths in S0_RATIONAL_PATHS.get(c.get("id"), ()):
            for side in ("computed", "expected"):
                node = c.get(side)
                if node is None:
                    continue
                if paths[-1] == "*":
                    for w, v in node[paths[0]].items():
                        rat(v, c["id"] + "." + side + "." + paths[0] + "." + w)
                else:
                    rat(node[paths[0]], c["id"] + "." + side + "." + paths[0])
    return f


def chk_cc_count(env):
    f = []
    comp = env["gt"]["completeness"]
    if not same(comp["states"], S_SIZE):
        f.append("completeness.states != " + str(S_SIZE))
    if comp["distinct"] is not True:
        f.append("completeness.distinct is not true")
    cycles = members_cycles(env["members"], env.get("cells"))
    allst = [s for c in cycles for s in c[2]]
    if len(allst) != S_SIZE or len(set(allst)) != S_SIZE:
        f.append("members.json does not list " + str(S_SIZE) + " distinct states")
    return f


def chk_cc_bij(env):
    return [] if env["gt"]["completeness"]["bijection"] is True else ["completeness.bijection is not true"]


def chk_cc_part(env):
    cycles = members_cycles(env["members"], env.get("cells"))
    f = partition_findings(env["universe"] if "universe" in env else instance_states(),
                           env.get("step", phi), cycles)
    hist = {}
    for _, size, _ in cycles:
        hist[str(size)] = hist.get(str(size), 0) + 1
    if not same(env["members"]["histogram"], hist):
        f.append("histogram does not count the listed cycle lengths")
    comp = env["gt"]["completeness"]
    if comp["partition"] is not True:
        f.append("completeness.partition is not true")
    if not same(comp["length_sum"], env.get("state_count", S_SIZE)):
        f.append("completeness.length_sum != " + str(S_SIZE))
    if not same(comp["cycles"], len(cycles)):
        f.append("completeness.cycles != number of listed cycles")
    return f


def chk_cc_cyc2(env):
    f = []
    c = env["cyc2"]
    if set(c) != {"schema", "version", "fix", "period_states", "cycles", "m10_identity"}:
        return ["cyc2.json keys"]
    if c["schema"] != "k1p1-cyc2" or not same(c["version"], 1):
        f.append("cyc2.json schema/version")
    ks = [str(k) for k in range(1, 11)]
    for fld in ("fix", "period_states", "cycles"):
        if set(c[fld]) != set(ks) or not all(is_int(v) for v in c[fld].values()):
            return f + ["cyc2." + fld + " is not an integer object over k = 1..10"]
    for k in ks:
        v = c["fix"][k]
        if v < 1 or v > S_SIZE or (v & (v - 1)) != 0:
            f.append("cyc2.fix[" + k + "] is not a power of 2 in [1, |S|]")
    for d in range(1, 11):
        ps = sum(mobius(d // e) * c["fix"][str(e)] for e in range(1, d + 1) if d % e == 0)
        if ps != c["period_states"][str(d)]:
            f.append("period_states[" + str(d) + "] differs from the Moebius sum of fix")
        if ps % d != 0 or c["cycles"][str(d)] * d != ps:
            f.append("cycles[" + str(d) + "] * " + str(d) + " != period_states[" + str(d) + "]")
    if c["m10_identity"] is not True or c["fix"]["10"] != S_SIZE:
        f.append("M^10 is not recorded as the identity")
    hist = env["members"]["histogram"]
    if not set(hist) <= set(ks):
        f.append("histogram has a cycle length outside 1..10")
    for k in ks:
        if c["cycles"][k] != hist.get(k, 0):
            f.append("cycles of length " + k + ": cyc2 " + str(c["cycles"][k]) + ", histogram " + str(hist.get(k, 0)))
    return f


def chk_cc_rows(env):
    f = []
    keys = member_keys(env["members"], env.get("cells"))
    rows = env["gt"]["rows"]
    expect = [(b, k) for b in BRANCHES for k in keys]
    got = [(r.get("branch"), r.get("member")) for r in rows]
    if got != expect:
        f.append("rows are not each member once per branch in M5 order")
    if len(rows) != 3 * len(keys):
        f.append("row count " + str(len(rows)) + " != 3 * " + str(len(keys)))
    if any(r.get("candidate") != "P1" for r in rows):
        f.append("a row's candidate is not P1")
    return f


def chk_cc_mass(env):
    f = []
    if env["gt"]["completeness"]["mass_sums"] is not True:
        f.append("completeness.mass_sums is not true")
    for i, r in enumerate(env["gt"]["rows"]):
        total = sum((parse_rational(v) for v in r["mass"].values()), Fraction(0))
        if total != 1:
            f.append("rows[" + str(i) + "]: masses sum to " + fmt_rational(total))
    return f


def chk_ct_inc(env, part_ok, rows_ok):
    """CT-INC: no class token from an incomplete list. Returns ("pass"|"fail"|"refused", findings)."""
    gt = env["gt"]
    if not part_ok or (rows_ok is not None and not rows_ok):
        return "refused", ["row set incomplete (CC-PART or CC-ROWS fails)"]
    f = []
    if env["stage"] == "members":
        if not same(gt["class_tokens"], {}) or not same(gt["union_clause_reached"], {}) or not same(gt["rows"], []):
            f.append("members stage carries rows or class tokens")
        return ("fail" if f else "pass"), f
    for b in BRANCHES:
        pending = any(r["token"] == "pending" for r in gt["rows"] if r["branch"] == b)
        if b not in gt["class_tokens"]:
            f.append(b + ": no class token")
            continue
        if (gt["class_tokens"][b] == "pending") != pending:
            f.append(b + ": class token 'pending' iff a row is pending")
    return ("fail" if f else "pass"), f


def chk_s0(env, cid):
    f = []
    ctl = env["gt"]["controls"]
    ids = [c.get("id") for c in ctl]
    if ids != list(S0_ORDER):
        return ["controls are not the eleven S0 controls in K section 6's order"]
    c = ctl[S0_ORDER.index(cid)]
    if set(c) != {"id", "gate", "computed", "expected", "paper", "outcome"}:
        return [cid + ": keys"]
    if c["gate"] != S0_GATE[cid]:
        f.append(cid + ": gate text")
    if not same(c["expected"], S0_EXPECTED[cid]):
        f.append(cid + ": expected differs from §10.2")
    paper = env["cd"]["s0_paper"][cid] if cid in S0_PAPER_IDS else None
    if not same(c["paper"], paper):
        f.append(cid + ": paper differs from class-decisions.json")
    derived = "pass" if (same(c["computed"], c["expected"]) and paper in (None, "pass")) else "fail"
    if c["outcome"] != derived:
        f.append(cid + ": recorded outcome " + repr(c["outcome"]) + " but derived " + derived)
    if derived != "pass":
        f.append(cid + ": control fails (VOID[stage]; H10)")
    return f


def chk_pr_s0(env):
    ctl = env["gt"]["controls"]
    f = []
    for cid in S0_ORDER:
        sub = chk_s0(env, cid)
        if sub:
            f.append(cid + " does not pass")
    if len(ctl) != len(S0_ORDER) or any(c.get("outcome") != "pass" for c in ctl):
        f.append("a recorded S0 outcome is not pass")
    return f


def chk_pr_e(env):
    reg = env["gt"]["region"]
    f = []
    if not same(reg["E"], PR_E_E):
        f.append("region.E != " + canon(PR_E_E))
    if not same(reg["W_eq"], PR_E_WEQ):
        f.append("region.W_eq != " + canon(PR_E_WEQ))
    return f


def chk_pr_cyc(env):
    f = []
    cycles = members_cycles(env["members"], env.get("cells"))
    if not same(env["members"]["histogram"], PR_CYC_HIST):
        f.append("histogram != " + canon(PR_CYC_HIST))
    fixed = sorted(c[0] for c in cycles if c[1] == 1)
    if fixed != PR_CYC_FIXED:
        f.append("fixed points != " + canon(PR_CYC_FIXED))
    two = [c[2] for c in cycles if c[1] == 2]
    if two != [PR_CYC_TWO]:
        f.append("2-cycle != " + canon(PR_CYC_TWO))
    cyc2 = env["cyc2"]["cycles"]
    want = {str(k): PR_CYC_HIST.get(str(k), 0) for k in range(1, 11)}
    if not same(cyc2, want):
        f.append("cyc2.cycles != " + canon(want))
    if not same(env["gt"]["preserved"]["phi_order"], PR_CYC_ORDER):
        f.append("preserved.phi_order != 10")
    if env["cyc2"]["m10_identity"] is not True:
        f.append("cyc2.m10_identity is not true")
    if not same(env["gt"]["completeness"]["cycles"], sum(PR_CYC_HIST.values())):
        f.append("completeness.cycles != 156")
    return f


def chk_pr_en(env):
    p = env["gt"]["preserved"]
    f = []
    if p["energy_conserved"] is not True:
        f.append("preserved.energy_conserved is not true")
    if not same(p["shell_sizes"], PR_EN_SHELLS):
        f.append("preserved.shell_sizes != " + canon(PR_EN_SHELLS))
    return f


def ind_formula(E, W, w):
    """PR-IND: pi_0(E_t = 0 | W_t = w) = q^-|E\\W| if w is 0 on W cap E, else 0 (A3)."""
    for i, c in enumerate(W):
        if c in E and w[i] != "0":
            return Fraction(0)
    return Fraction(1, Q ** len([c for c in E if c not in W]))


def chk_pr_ind(env):
    f = []
    gt = env["gt"]
    E = list(gt["region"]["E"])
    W = list(gt["region"]["W_eq"])
    rows = [r for r in gt["rows"] if r["member"] == "pi0" and r["branch"] == "B-eq"]
    if len(rows) != 1:
        return ["no unique pi0 B-eq row"]
    allw = ["".join(p) for p in itertools.product("01", repeat=len(W))]
    weak = rows[0]["weak"]
    if sorted(weak) != allw:
        f.append("pi0 B-eq weak values do not cover every w")
    for w in allw:
        if w in weak and parse_rational(weak[w]) != ind_formula(E, W, w):
            f.append("pi0 B-eq weak[" + w + "] differs from the formula")
    abs_w = ["x_3", "y_3"]
    abs_ctl = [c for c in gt["controls"] if c.get("id") == "CC-ABS"]
    if len(abs_ctl) != 1 or abs_ctl[0]["computed"] is None:
        return f + ["CC-ABS computed part missing"]
    aweak = abs_ctl[0]["computed"]["weak"]
    if sorted(aweak) != allw:
        f.append("CC-ABS weak values do not cover every w")
    for w in allw:
        if w in aweak and parse_rational(aweak[w]) != ind_formula(E, abs_w, w):
            f.append("CC-ABS weak[" + w + "] differs from the formula")
    return f


def chk_pr_p1c(env):
    f = []
    cycles = members_cycles(env["members"], env.get("cells"))
    allst = instance_states()
    if set(phi(s) for s in allst) != set(allst):
        f.append("phi(supp pi0) != supp pi0")
    for key, _, states in cycles:
        if set(env.get("step", phi)(s) for s in states) != set(states):
            f.append("phi(supp u_c[" + key + "]) != supp")
    return f


def chk_pr_blind(env):
    f = []
    for r in env["gt"]["rows"]:
        if r["branch"] == "B-pl" and r["sharp_w"] and any(r["nb"][w] is not False for w in r["sharp_w"]):
            f.append("B-pl row " + r["member"] + " is sharp with NB true")
    return f


def chk_pr_ledger(env):
    f = []
    for r in env["gt"]["rows"]:
        if r["branch"] in ("B-pl", "B-eq") and ("VOID[row]" in (r["gates"]["G4"], r["token"])):
            f.append(r["branch"] + " row " + r["member"] + " reaches VOID[row]")
    return f


def chk_pr_cr6(env):
    f = []
    gt = env["gt"]
    for b in BRANCHES:
        rows = [r for r in gt["rows"] if r["branch"] == b and r["member"] == env.get("zero", DELTA0)]
        if len(rows) != 1:
            f.append(b + ": no unique delta_0 row")
        elif rows[0]["gates"]["G5"] == "pass":
            f.append(b + ": delta_0 row passes G5 (strict PR-CR6)")
        if gt["union_clause_reached"].get(b) is not False:
            f.append(b + ": union_clause_reached is not false (H3)")
    return f


def chk_pr_p0(env):
    f = []
    for b in BRANCHES:
        rows = [r for r in env["gt"]["rows"] if r["branch"] == b and r["member"] == "pi0"]
        if len(rows) != 1:
            f.append(b + ": no unique pi0 row")
            continue
        r = rows[0]
        if not same(r["sharp_w"], []):
            f.append(b + ": pi0 sharp_w is not []")
        if not same(r["weak"], PR_P0_WEAK[b]):
            f.append(b + ": pi0 weak != " + canon(PR_P0_WEAK[b]))
        if r["w_certified"] is not False:
            f.append(b + ": pi0 w_certified is not false")
    return f


# --- token recomputation (R5a-R10, CLASS; K section 5.2-5.4, A2) -----------------------

def expected_row(r, info):
    """Recompute a row's derived fields, gates, hypotheses and token. Returns findings."""
    f = []
    b, key = r["branch"], r["member"]
    tag = b + "/" + key
    if set(r) != ROW_KEYS:
        return [tag + ": row keys"]
    if r["candidate"] != "P1" or r["w_rule"] != W_RULE[b] or not same(r["w_inputs"], W_INPUTS[b]):
        f.append(tag + ": candidate, w_rule or w_inputs")
    E, Weq, cd, stage = info["E"], info["W_eq"], info["cd"], info["stage"]
    W = [] if b == "B-pl" else Weq
    size = info["sizes"][key]
    is_uc = key != "pi0"
    if not same(r["support_size"], size):
        f.append(tag + ": support_size")
    state_count, q = info["state_count"], info["q"]
    dr = fmt_rational(Fraction(state_count, size))
    if r["d_ratio"] != dr:
        f.append(tag + ": d_ratio")

    mass = {w: parse_rational(v) for w, v in r["mass"].items()}
    if not all(is_bits(w, len(W)) for w in mass) or not all(v > 0 for v in mass.values()):
        f.append(tag + ": mass keys or non-positive mass")
    weak = {w: parse_rational(v) for w, v in r["weak"].items()}
    ref = {w: parse_rational(v) for w, v in r["pi0_ref"].items()}
    if set(weak) != set(mass) or set(ref) != set(mass):
        f.append(tag + ": weak/pi0_ref keys differ from mass keys")
    if not all(0 <= v <= 1 for v in list(weak.values()) + list(ref.values())):
        f.append(tag + ": weak or pi0_ref outside [0, 1]")
    sharp = sorted(w for w in mass if weak.get(w) == 1)
    if not same(r["sharp_w"], sharp):
        f.append(tag + ": sharp_w is not the w with weak value 1")
    if set(r["nb"]) != set(sharp) or not all(is_bool(v) for v in r["nb"].values()):
        f.append(tag + ": nb keys or values")
    if (b == "B-pl") != is_bool(r["nb_g1"]) or (b != "B-pl" and r["nb_g1"] is not None):
        f.append(tag + ": nb_g1")
    if not is_bool(r["w_certified"]):
        f.append(tag + ": w_certified")
    if f:
        return f

    k = len([c for c in E if c not in W])
    if b == "B-pl":
        bound = q ** len(E) * size <= state_count
        ledger = "D=log(" + dr + "); (c1) |E|=" + str(len(E)) + ": " + ("holds" if bound else "breaks")
        broken = bool(sharp) and not bound
    elif b == "B-eq":
        bound = {}
        for w in sharp:
            a, d = mass[w].numerator, mass[w].denominator
            bound[w] = q ** (a * k) * size ** d <= state_count ** d
        if sharp:
            ledger = "D=log(" + dr + "); (c2) " + "; ".join(
                "w=" + w + " p=" + r["mass"][w] + " k=" + str(k) + ": " + ("holds" if bound[w] else "breaks")
                for w in sharp)
        else:
            ledger = "D=log(" + dr + "); (c2) no sharp w"
        broken = any(not bound[w] for w in sharp)
    else:
        bound = None
        ledger = "D=log(" + dr + "); cross time, no D bound; H-ret"
        broken = False
    if not same(r["bound_ok"], bound):
        f.append(tag + ": bound_ok")
    if r["ledger"] != ledger:
        f.append(tag + ": ledger")

    # G1, G2 (R5, R5a)
    cr, sr = cd["class_rule"], cd["support_restriction"]

    def applies(field, value):
        return cr[field] == value or (is_uc and sr[field] == value)

    a_flag, t1_flag = applies("a", "flag"), applies("t1", "flag")
    t2 = info["t2"][key]
    g2 = r["g2"]
    if set(g2) != {"a", "t1", "t2", "hsel_content"} or g2["a"] is not a_flag or g2["t1"] is not t1_flag \
            or g2["t2"] is not t2:
        f.append(tag + ": g2 flags")
    hsel = g2.get("hsel_content")
    if t1_flag or t2:
        if not same(hsel, []):
            f.append(tag + ": hsel_content must be [] when T1 or T2 fires")
    else:
        ws = [e.get("w") for e in hsel] if isinstance(hsel, list) else None
        if ws is None or ws != sorted(set(ws)) or not all(w in mass for w in ws) or not all(
                set(e) == {"values", "w"} and isinstance(e["values"], list) and e["values"]
                and e["values"] == sorted(set(e["values"])) and all(is_bits(v, len(E)) for v in e["values"])
                for e in hsel):
            f.append(tag + ": hsel_content form")
    hsel_present = bool(hsel) and not (t1_flag or t2)

    z1 = "Z1-VOID[IMPORTED]" if a_flag else ("Z1-VOID[DYN]" if (t1_flag or t2) else None)
    g1_und = cd["g1"] == "undecided"
    g2_und = applies("a", "undecided") or applies("t1", "undecided")
    access = ", ".join(ACCESS[b])
    gates = {g: NR for g in GATES}
    hyps = [H_INV]
    useful_expected = None
    if z1 is not None:
        gates["G1"] = "UNDECIDED(G1)" if g1_und else "pass"
        gates["G2"] = z1
        token = z1
    elif g1_und:
        gates["G1"] = "UNDECIDED(G1)"
        gates["G2"] = "UNDECIDED(G2)" if g2_und else "pass"
        token = "UNDECIDED(G1)"
    elif g2_und:
        gates["G1"], gates["G2"] = "pass", "UNDECIDED(G2)"
        token = "UNDECIDED(G2)"
    else:
        gates["G1"] = gates["G2"] = gates["G3"] = "pass"
        if not sharp:
            token = "ABSENT[" + member_name(key) + "; " + b + "; " + access + "]"
        elif b in ("B-pl", "B-eq") and broken:
            token = "VOID[row]"
        elif all(r["nb"][w] is False for w in sharp):
            token = "BLIND[" + member_name(key) + "; " + b + "; " + access + "]"
        else:
            token = None
        if token is not None:
            gates["G4"] = token
            if token != "VOID[row]":
                hyps = [H_INV] + list(ACCESS[b])
        else:
            gates["G4"] = gates["G5"] = "pass"
            lam = set([H_INV] + list(ACCESS[b]))
            if not r["w_certified"]:
                lam.add("H-law")
            if hsel_present:
                lam.add("H-sel")
            hyps = sorted(lam)
            lam_s = ", ".join(hyps)
            cand = ("AVAILABLE[H-sel](" + lam_s + ")") if "H-sel" in lam else ("CONDITIONAL[" + lam_s + "]")
            useful_expected = "object"
            if stage != "final":
                gates["G6"] = "pending"
                gates["G7"] = "pending"
                token = "pending"
            else:
                adv = info["adv"].get((b, key))
                if adv is None:
                    f.append(tag + ": passes G5 but adversarial.json has no entry")
                    token = "pending"
                elif adv == cand:
                    gates["G6"], gates["G7"] = "pass", cand
                    token = cand
                else:
                    gates["G6"] = "UNDECIDED(G6)"
                    token = "UNDECIDED(G6)"
    if not same(r["gates"], gates):
        f.append(tag + ": gates " + canon(r["gates"]) + " != recomputed " + canon(gates))
    if r["token"] != token:
        f.append(tag + ": token " + repr(r["token"]) + " != recomputed " + repr(token))
    if not same(r["hypotheses"], sorted(hyps)):
        f.append(tag + ": hypotheses")

    u = r["usefulness"]
    keep = useful_expected is not None and (stage != "final" or positive(token))
    if not keep:
        if u is not None:
            f.append(tag + ": usefulness must be null")
    else:
        if not isinstance(u, dict) or set(u) != set(sharp):
            f.append(tag + ": usefulness keys")
        else:
            for w in sharp:
                ent = u[w]
                if not isinstance(ent, dict) or set(ent) != {"disjoint", "law_only"}:
                    f.append(tag + ": usefulness[" + w + "] keys")
                    continue
                pairs = []
                for lst in (ent["disjoint"], ent["law_only"]):
                    if not isinstance(lst, list) or lst != sorted(lst) or not all(
                            isinstance(p, list) and len(p) == 2 and is_bits(p[0], 2) and is_bits(p[1], 2)
                            and p[0] < p[1] for p in lst):
                        f.append(tag + ": usefulness[" + w + "] pair form")
                    else:
                        pairs += [tuple(p) for p in lst]
                if len(set(pairs)) != len(pairs):
                    f.append(tag + ": usefulness[" + w + "] pair in both lists")
                if bool(pairs) != (r["nb"][w] is True):
                    f.append(tag + ": usefulness[" + w + "] nonempty exactly when NB holds")
    return f


def expected_class(rows_b, b):
    toks = [r["token"] for r in rows_b]
    if any(t == "pending" for t in toks):
        return "pending", False
    if all(positive(t) for t in toks):
        return None, True
    void = [member_name(r["member"]) for r in rows_b if r["token"] == "VOID[row]"]
    if void:
        return "VOID[row](" + ", ".join(void) + ")", False
    subs = [s for s in ("IMPORTED", "DYN") if ("Z1-VOID[" + s + "]") in toks]
    if subs:
        return "Z1-VOID[" + ", ".join(subs) + "]", False
    ks = sorted(set(int(t[len("UNDECIDED(G"):-1]) for t in toks if t.startswith("UNDECIDED(G")))
    if ks:
        return "UNDECIDED(" + ", ".join("G" + str(k) for k in ks) + ")", False
    access = ", ".join(ACCESS[b])
    if any(t.startswith("ABSENT[") for t in toks):
        return "ABSENT[" + CLASS_SET + "; " + b + "; " + access + "]", False
    if any(t.startswith("BLIND[") for t in toks):
        return "BLIND[" + CLASS_SET + "; " + b + "; " + access + "]", False
    return "<no non-positive type attained>", False


def chk_tokens(env):
    f = []
    gt = env["gt"]
    cycles = members_cycles(env["members"], env.get("cells"))
    sizes = {"pi0": env.get("state_count", S_SIZE)}
    t2 = {"pi0": False}
    for key, size, states in cycles:
        sizes[key] = size
        t2[key] = set(env.get("step", phi)(s) for s in states) != set(states)
    adv = {}
    if env["stage"] == "final" and env.get("adv") is not None:
        adv = {(e["branch"], e["member"]): e["token"] for e in env["adv"]["rows"]}
    info = {"E": list(gt["region"]["E"]), "W_eq": list(gt["region"]["W_eq"]), "cd": env["cd"],
            "stage": env["stage"], "sizes": sizes, "t2": t2, "adv": adv,
            "state_count": env.get("state_count", S_SIZE), "q": env.get("q", Q)}
    by_b = {b: [] for b in BRANCHES}
    for r in gt["rows"]:
        f += expected_row(r, info)
        by_b[r["branch"]].append(r)
    for b in BRANCHES:
        certs = set(r["w_certified"] for r in by_b[b])
        if len(certs) > 1:
            f.append(b + ": w_certified differs between rows of one branch (R4)")
        ct, union = expected_class(by_b[b], b)
        if gt["class_tokens"].get(b) != ct:
            f.append(b + ": class token " + repr(gt["class_tokens"].get(b)) + " != recomputed " + repr(ct))
        if gt["union_clause_reached"].get(b) is not union:
            f.append(b + ": union_clause_reached")
    return f


def valid_adversarial(adv):
    if not isinstance(adv, dict) or set(adv) != {"schema", "version", "rows"}:
        return False
    if adv["schema"] != "k1p1-adversarial" or not same(adv["version"], 1) or not isinstance(adv["rows"], list):
        return False
    seen = set()
    for e in adv["rows"]:
        if not isinstance(e, dict) or set(e) != {"branch", "member", "token", "note"}:
            return False
        if not all(isinstance(v, str) for v in e.values()):
            return False
        key = (e["branch"], e["member"])
        if key in seen:
            return False
        seen.add(key)
    return True


def adv_index_findings(rows, adv, notes):
    g5 = [(r["branch"], r["member"]) for r in rows if r["gates"]["G5"] == "pass"]
    if adv is None:
        entries = []
    elif not valid_adversarial(adv):
        return ["adversarial.json schema or duplicate entries"]
    else:
        entries = adv["rows"]
    f = []
    if [(e["branch"], e["member"]) for e in entries] != g5:
        f.append("adversarial entries differ from G5 inventory/order")
    for b in BRANCHES:
        keys = [k for branch, k in g5 if branch == b]
        if (b in notes) != bool(keys):
            f.append(b + ": note exists iff G5 inventory nonempty")
        if b in notes:
            lines = notes[b].split("\n")
            if "" not in lines:
                f.append(b + ": no empty index terminator")
            elif lines[:lines.index("")] != keys:
                f.append(b + ": note index differs from G5 inventory")
        path = "derivations/adversarial-" + b + ".md"
        if any(e["note"] != path for e in entries if e["branch"] == b):
            f.append(b + ": wrong note path")
    return f


def chk_adv_index(env):
    return adv_index_findings(env["rows_gt"]["rows"], env.get("adv"), env["notes"])


# ---------------------------------------------------------------------------
# Stage execution (§10.1)
# ---------------------------------------------------------------------------

def run_impl(ctx, which, stage, out, members_sha, impl_path=None):
    path = impl_path or IMPL[which]
    argv = [sys.executable, "-I", path, "--stage", stage, "--record", REC_REL, "--out", out]
    if stage != "members":
        argv += ["--members-sha256", members_sha]
    return subprocess.run(argv, cwd=ctx.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode


def read_dir(d):
    out = {}
    for name in sorted(os.listdir(d)):
        p = os.path.join(d, name)
        if os.path.isfile(p):
            with open(p, "rb") as fh:
                out[name] = fh.read()
    return out


def combine(outcomes):
    if "fail" in outcomes:
        return "fail"
    if "refused" in outcomes:
        return "refused"
    return "pass"


def execute_stage(ctx, stage, members_sha, mutate=None, impl_paths=None):
    """Run A and B into fresh directories and perform the stage's checks.

    Returns (checks, outputs, codes): `checks` is the §10.2 list in the order run,
    `outputs` maps "A"/"B" to {file name: bytes}. `mutate`, used only by self-test,
    edits the outputs before any comparison.
    """
    checks = []
    findings = {}

    def record(cid, outcome, fs=()):
        checks.append({"id": cid, "outcome": outcome})
        findings[cid] = list(fs)

    impl_abs = None
    if impl_paths:
        impl_abs = {k: os.path.join(ctx.root, *v.split("/")) for k, v in impl_paths.items()}
    fs = chk_imports(ctx, impl_abs)
    record("IMPORTS", "fail" if fs else "pass", fs)

    outputs, codes = {}, {}
    for which in ("A", "B"):
        with tempfile.TemporaryDirectory() as tmp:
            out = os.path.join(tmp, "out")
            os.mkdir(out)
            codes[which] = run_impl(ctx, which, stage, out, members_sha,
                                    impl_paths[which] if impl_paths else None)
            outputs[which] = read_dir(out) if codes[which] == 0 else {}
    if mutate is not None and codes["A"] == 0 and codes["B"] == 0:
        mutate(outputs)

    gtf = GATE_TABLE[stage]
    if codes["A"] != 0 or codes["B"] != 0:
        msg = ["exit A=" + str(codes["A"]) + " B=" + str(codes["B"])]
        record("AB-members", "fail", msg)
        record("AB-gate-table", "fail", msg)
        return checks, outputs, codes, findings
    for cid, fname in (("AB-members", "members.json"), ("AB-gate-table", gtf)):
        a, b = outputs["A"].get(fname), outputs["B"].get(fname)
        ok = a is not None and a == b
        record(cid, "pass" if ok else "fail", [] if ok else [fname + ": A and B differ (H1)"])

    cd = None
    try:
        cd = class_decisions(ctx)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        cd_error = "class-decisions.json: " + str(exc)
    adv = None
    if stage == "final" and ctx.has_rec("adversarial.json"):
        adv = loads(ctx.read_rec("adversarial.json"))
    notes = {}
    if stage == "final":
        for b in BRANCHES:
            name = "derivations/adversarial-" + b + ".md"
            if ctx.has_rec(name):
                notes[b] = ctx.read_rec(name).decode("utf-8")
    rows_gt = None
    if stage == "final":
        rows_gt = loads(ctx.read_rec("gate-table.rows.json"))

    envs = {}
    for which in ("A", "B"):
        env = {"stage": stage, "cd": cd, "adv": adv, "rows_gt": rows_gt, "notes": notes}
        try:
            env["members"] = loads(outputs[which]["members.json"])
            env["gt"] = loads(outputs[which][gtf])
            env["cyc2"] = loads(outputs["B"]["cyc2.json"])
        except (KeyError, ValueError, UnicodeDecodeError) as exc:
            env["error"] = which + ": unreadable output: " + str(exc)
        envs[which] = env

    def run_check(cid, fn, *extra):
        outs, fs = [], []
        for which in ("A", "B"):
            env = envs[which]
            if "error" in env:
                outs.append("fail")
                fs.append(env["error"])
                continue
            if cd is None and fn in (chk_s0, chk_pr_s0, chk_tokens):
                outs.append("fail")
                fs.append(cd_error)
                continue
            try:
                res = fn(env, *extra)
            except (KeyError, IndexError, TypeError, ValueError, AttributeError) as exc:
                res = ["exception " + type(exc).__name__ + ": " + str(exc)]
            if isinstance(res, tuple):
                outs.append(res[0])
                fs += [which + ": " + x for x in res[1]]
            else:
                outs.append("fail" if res else "pass")
                fs += [which + ": " + x for x in res]
        record(cid, combine(outs), fs)
        return outs

    run_check(CHECK_ID_EXACT, chk_exact)
    for cid in S0_ORDER:
        run_check(cid, chk_s0, cid)
    run_check("PR-S0", chk_pr_s0)
    run_check("CC-COUNT", chk_cc_count)
    run_check("CC-BIJ", chk_cc_bij)
    part = run_check("CC-PART", chk_cc_part)
    run_check("CC-CYC2", chk_cc_cyc2)
    rows_outs = None
    if stage != "members":
        rows_outs = run_check("CC-ROWS", chk_cc_rows)
        run_check("CC-MASS", chk_cc_mass)
    # CT-INC per implementation, against that implementation's own CC-PART and CC-ROWS.
    ct_outs, ct_fs = [], []
    for i, which in enumerate(("A", "B")):
        env = envs[which]
        if "error" in env:
            ct_outs.append("fail")
            continue
        try:
            o, fs = chk_ct_inc(env, part[i] == "pass", None if rows_outs is None else rows_outs[i] == "pass")
        except (KeyError, IndexError, TypeError, ValueError, AttributeError) as exc:
            o, fs = "fail", ["exception " + type(exc).__name__]
        ct_outs.append(o)
        ct_fs += [which + ": " + x for x in fs]
    record("CT-INC", combine(ct_outs), ct_fs)
    run_check("PR-E", chk_pr_e)
    run_check("PR-CYC", chk_pr_cyc)
    run_check("PR-EN", chk_pr_en)
    run_check("PR-P1c", chk_pr_p1c)
    if stage != "members":
        run_check("PR-IND", chk_pr_ind)
        run_check("PR-BLIND", chk_pr_blind)
        run_check("PR-LEDGER", chk_pr_ledger)
        run_check("PR-CR6", chk_pr_cr6)
        run_check("PR-P0", chk_pr_p0)
        run_check(CHECK_ID_TOKENS, chk_tokens)
    if stage == "final":
        run_check("ADV-INDEX", chk_adv_index)
    return checks, outputs, codes, findings


def checks_doc(stage, checks, outputs, codes=None):
    doc = {"schema": "k1p1-checks", "version": 1, "stage": stage, "checks": checks,
           "exit_status": codes if codes is not None else {"A": None, "B": None}}
    if stage == "final":
        gt = outputs.get("A", {}).get("gate-table.json")
        doc["gate_table_sha256"] = hashlib.sha256(gt).hexdigest() if gt is not None and all_pass(checks) else None
    if stage == "members":
        m = outputs.get("A", {}).get("members.json")
        doc["members_sha256"] = hashlib.sha256(m).hexdigest() if m is not None else None
    return doc


def stage_outputs(stage, checks, outputs, codes=None):
    """The stage's files as `run` would write them: {file name: bytes}."""
    files = {CHECKS_FILE[stage]: dumps(checks_doc(stage, checks, outputs, codes))}
    if stage == "members":
        if "members.json" in outputs.get("A", {}):
            files["members.json"] = outputs["A"]["members.json"]
        if "cyc2.json" in outputs.get("B", {}):
            files["cyc2.json"] = outputs["B"]["cyc2.json"]
    if GATE_TABLE[stage] in outputs.get("A", {}):
        files[GATE_TABLE[stage]] = outputs["A"][GATE_TABLE[stage]]
    return files


def all_pass(checks):
    return all(c["outcome"] == "pass" for c in checks)


def committed_members_sha(ctx):
    doc = loads(ctx.read_rec("checks.members.json"))
    sha = doc.get("members_sha256")
    if not (isinstance(sha, str) and len(sha) == 64 and all(c in "0123456789abcdef" for c in sha)):
        raise Refusal("checks.members.json carries no valid members_sha256")
    return sha


def print_checks(stage, checks, findings):
    for c in checks:
        print(stage + " " + c["id"] + " " + c["outcome"])
        for x in findings.get(c["id"], [])[:20]:
            print("    " + x)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def previous_stage_files(ctx, stage):
    return [n for s in STAGES[:STAGES.index(stage)] for n in STAGE_FILES[s]]


def precondition_ids(stage):
    return [c for c in ROSTERS[stage] if c.startswith("PRE-")]


def precondition_holds(ctx, stage, cid):
    if cid == "PRE-INPUTS":
        return tracked_and_unmodified(ctx, ("class-decisions.json", "derivations/P1-class-paper.md",
                                            "derivations/S0-paper.md"))
    if cid == "PRE-PREV":
        return tracked_and_unmodified(ctx, previous_stage_files(ctx, stage))
    if cid == "PRE-ADV":
        gt = loads(ctx.read_rec("gate-table.rows.json"))
        branches = [b for b in BRANCHES if any(r["branch"] == b and r["gates"]["G5"] == "pass" for r in gt["rows"])]
        names = ["adversarial.json"] + ["derivations/adversarial-" + b + ".md" for b in branches]
        return not branches or tracked_and_unmodified(ctx, names)
    if cid == "PRE-CHECK":
        return check_stage(ctx, STAGES[STAGES.index(stage) - 1])["status"] == 0
    raise ValueError("unknown precondition " + cid)


def cmd_run(ctx, stage):
    checks, outputs, codes, findings = [], {}, {"A": None, "B": None}, {}
    status = 1
    try:
        for cid in precondition_ids(stage):
            try:
                ok = precondition_holds(ctx, stage, cid)
            except (OSError, ValueError, KeyError, TypeError, Refusal):
                ok = False
            checks.append({"id": cid, "outcome": "pass" if ok else "refused"})
            if not ok:
                status = 2
                return status
        sha = None if stage == "members" else committed_members_sha(ctx)
        done, outputs, codes, findings = execute_stage(ctx, stage, sha)
        checks += done
        print_checks(stage, checks, findings)
        files = stage_outputs(stage, checks, outputs, codes)
        if not all_pass(checks):
            return 1
        if [c["id"] for c in checks] != list(ROSTERS[stage]):
            raise ValueError("internal roster differs from frozen roster")
        for name, data in files.items():
            if name != CHECKS_FILE[stage]:
                with open(ctx.rec_path(name), "wb") as fh:
                    fh.write(data)
        status = 0
        return status
    except Refusal:
        status = 2
        return status
    except (OSError, ValueError, KeyError, TypeError) as exc:
        sys.stderr.write("run failure: " + type(exc).__name__ + "\n")
        return 1
    finally:
        with open(ctx.rec_path(CHECKS_FILE[stage]), "wb") as fh:
            fh.write(dumps(checks_doc(stage, checks, outputs, codes)))


def last_committed_stage(ctx):
    last = None
    for s in STAGES:
        if all(ctx.has_rec(n) for n in STAGE_FILES[s]):
            last = s
    return last


def check_stage(ctx, stage, mutate=None, quiet=True):
    """`check --stage s`: regenerate every stage up to s and compare with the committed files.

    Returns {"status": 0|1, "stages": {t: {"checks", "findings", "replay"}}, "render": ...}.
    """
    report = {"status": 0, "stages": {}, "render": None}
    for t in STAGES[: STAGES.index(stage) + 1]:
        members_sha = None
        if t != "members":
            members_sha = committed_members_sha(ctx)
        hook = mutate.get(t) if mutate else None
        checks, outputs, codes, findings = execute_stage(ctx, t, members_sha, hook)
        checks = [{"id": cid, "outcome": "pass"} for cid in precondition_ids(t)] + checks
        files = stage_outputs(t, checks, outputs, codes)
        replay = {}
        for name in STAGE_FILES[t]:
            committed = ctx.read_rec(name) if ctx.has_rec(name) else None
            replay["REPLAY-" + name] = committed is not None and files.get(name) == committed
        report["stages"][t] = {"checks": checks, "findings": findings, "replay": replay}
        if not quiet:
            print_checks(t, checks, findings)
            for k in sorted(replay):
                print(t + " " + k + " " + ("pass" if replay[k] else "fail"))
        if not all_pass(checks) or not all(replay.values()):
            report["status"] = 1
    if stage == "final" and report["status"] == 0:
        reason, fragment = render_from_record(ctx)
        report["render"] = reason == "OK" and ctx.has_rec("result.md") and marker_matches(ctx.read_rec("result.md"), fragment)
        if not report["render"]:
            report["status"] = 1
    return report


def cmd_check(ctx, stage):
    if stage is None:
        stage = last_committed_stage(ctx)
        if stage is None:
            raise Refusal("no stage's files are committed")
    return check_stage(ctx, stage, quiet=False)["status"]


def cmd_render(ctx):
    open_question("OQ-C4", "render: the output destination and the token-table format of result.md")


# ---------------------------------------------------------------------------
# Self-test (§11.2, §11.3)
# ---------------------------------------------------------------------------

# SF-1 (§11.2): the permutation of {0, ..., 11} with cycles (0)(1 2)(3 4 5)(6 7 8 9 10 11);
# hand-derived answers: cycle lengths 1, 2, 3, 6; least elements 0, 1, 3, 6; coverage 12.
SF1_CYCLES = ((0,), (1, 2), (3, 4, 5), (6, 7, 8, 9, 10, 11))
SF1_LENGTHS = [1, 2, 3, 6]
SF1_LEAST = [0, 1, 3, 6]
SF1_COVERAGE = 12


def sf1():
    """SF-1 through controls.py's CC-PART checker (partition_findings). Returns findings."""
    perm = {}
    for c in SF1_CYCLES:
        for i, e in enumerate(c):
            perm[e] = c[(i + 1) % len(c)]
    universe = list(range(SF1_COVERAGE))
    claimed = [(min(c), len(c), sorted(c)) for c in sorted(SF1_CYCLES, key=min)]
    f = []
    if [c[1] for c in claimed] != SF1_LENGTHS:
        f.append("SF-1 lengths")
    if [c[0] for c in claimed] != SF1_LEAST:
        f.append("SF-1 least elements")
    if sum(c[1] for c in claimed) != SF1_COVERAGE:
        f.append("SF-1 coverage")
    f += ["SF-1 " + x for x in partition_findings(universe, lambda s: perm[s], claimed)]
    return f


def cmd_self_test_synthetic():
    f = sf1()
    print("SF-1 " + ("pass" if not f else "fail"))
    for x in f:
        print("    " + x)
    if f:
        return 1
    open_question("OQ-C1", "SF-2 has no counterpart in controls.py (it computes no rank); SF-3's toy system "
                           "and SF-M's analogues are to be fixed in the code-freeze amendment; how SF-1 to "
                           "SF-3 reach A and B, whose command line is instance-only, is not stated")


def sandbox_copy(ctx, dest, skip=()):
    names = [IMPL["A"], IMPL["B"]]
    for dirpath, _, files in os.walk(ctx.rec):
        for fn in files:
            rel = os.path.relpath(os.path.join(dirpath, fn), ctx.root).replace(os.sep, "/")
            names.append(rel)
    for rel in names:
        src = os.path.join(ctx.root, *rel.split("/"))
        dst = os.path.join(dest, *rel.split("/"))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(src, "rb") as fh:
            data = fh.read()
        with open(dst, "wb") as fh:
            fh.write(data)
    sb = Ctx(dest)
    base = ["-c", "user.name=k1p1-self-test", "-c", "user.email=self-test@invalid", "-c", "commit.gpgsign=false"]
    git(sb, ["init", "-q"])
    git(sb, ["add", "-A"])
    for rel in skip:
        git(sb, ["rm", "-q", "--cached", "--", rel])
    if git(sb, base + ["commit", "-q", "-m", "self-test sandbox"]) != 0:
        raise Refusal("self-test sandbox commit failed")
    return sb


def json_edit(outputs, which, fname, fn):
    doc = loads(outputs[which][fname])
    fn(doc)
    outputs[which][fname] = dumps(doc)


def outcome(report, stage, cid):
    for c in report["stages"][stage]["checks"]:
        if c["id"] == cid:
            return c["outcome"]
    return None


def flip_digit(data):
    b = bytearray(data)
    for i in range(len(b) // 2, len(b)):
        if 48 <= b[i] <= 57:
            b[i] = 48 + ((b[i] - 48 + 1) % 10)
            return bytes(b)
    raise ValueError("no digit to flip")


def mutations_for(stage):
    """§11.3 timing: the mutations each `self-test --stage` covers."""
    return {
        "members": ("MU-3", "MU-4", "MU-8", "MU-13", "MU-C1", "MU-C2"),
        "rows": ("MU-1", "MU-2", "MU-5", "MU-6", "MU-7", "MU-9", "MU-10", "MU-12", "MU-13",
                 "MU-14a", "MU-14b", "MU-14c", "MU-C3"),
        "final": ("MU-11", "MU-13"),
    }[stage]


def apply_mutation(ctx, stage, mu):
    """Apply one mutation in a fresh sandbox. Returns True when it is detected as §11.3 requires."""
    gtf = GATE_TABLE[stage]
    with tempfile.TemporaryDirectory() as tmp:
        sb = sandbox_copy(ctx, os.path.join(tmp, "repo"))

        def chk(edit):
            return check_stage(sb, stage, mutate={stage: edit})

        if mu == "MU-1":
            def edit(o):
                json_edit(o, "A", gtf, lambda d: d["rows"].pop([r["branch"] for r in d["rows"]].index("B-eq") + 1))
            rep = chk(edit)
            return outcome(rep, stage, "CC-ROWS") == "fail" and outcome(rep, stage, "CT-INC") == "refused"
        if mu == "MU-2":
            rep = chk(lambda o: json_edit(o, "A", gtf, lambda d: d["rows"].insert(1, d["rows"][1])))
            return outcome(rep, stage, "CC-ROWS") == "fail"
        if mu in ("MU-3", "MU-4"):
            def edit_members(d):
                tens = [m for m in d["members"][1:] if m["size"] == max(x["size"] for x in d["members"][1:])]
                s = tens[0]["states"].pop()
                tens[0]["size"] -= 1
                if mu == "MU-3":
                    tens[1]["states"] = sorted(tens[1]["states"] + [s])
                    tens[1]["size"] += 1
            rep = chk(lambda o: json_edit(o, "A", "members.json", edit_members))
            ok = outcome(rep, stage, "CC-PART") == "fail"
            if mu == "MU-4":
                ok = ok and outcome(rep, stage, "CT-INC") == "refused"
            return ok
        if mu == "MU-5":
            def edit5(d):
                r = d["rows"][0]
                r["weak"][sorted(r["weak"])[0]] = "0.5"
            return outcome(chk(lambda o: json_edit(o, "A", gtf, edit5)), stage, CHECK_ID_EXACT) == "fail"
        if mu == "MU-6":
            def edit6(d):
                r = d["rows"][0]
                w = sorted(r["weak"])[0]
                v = parse_rational(r["weak"][w])
                v = v + Fraction(1, 1024) if v + Fraction(1, 1024) <= 1 else v - Fraction(1, 1024)
                r["weak"][w] = fmt_rational(v)
            rep = chk(lambda o: json_edit(o, "A", gtf, edit6))
            return outcome(rep, stage, "AB-gate-table") == "fail" and \
                rep["stages"][stage]["replay"]["REPLAY-" + gtf] is False
        if mu == "MU-7":
            def edit7(d):
                d["rows"][1], d["rows"][2] = d["rows"][2], d["rows"][1]
            return outcome(chk(lambda o: json_edit(o, "A", gtf, edit7)), stage, "CC-ROWS") == "fail"
        if mu == "MU-8":
            rep = chk(lambda o: json_edit(o, "A", gtf, lambda d: d["region"]["E"].remove("y_2")))
            return outcome(rep, stage, "PR-E") == "fail"
        if mu == "MU-9":
            def edit9(d):
                for r in d["rows"]:
                    if r["token"].startswith("ABSENT[") or r["token"].startswith("BLIND["):
                        r["token"] = r["gates"]["G4"] = "VOID[row]"
                        return
                raise ValueError("no ABSENT or BLIND row to mutate")
            return outcome(chk(lambda o: json_edit(o, "A", gtf, edit9)), stage, CHECK_ID_TOKENS) == "fail"
        if mu == "MU-10":
            def edit10(d):
                d["union_clause_reached"]["B-pl"] = True
            return outcome(chk(lambda o: json_edit(o, "A", gtf, edit10)), stage, "PR-CR6") == "fail"
        if mu == "MU-12":
            def edit12(d):
                d["controls"][0]["outcome"] = "fail"
            rep = chk(lambda o: json_edit(o, "A", gtf, edit12))
            # VOID[stage]: PR-S0 fails, so `run` writes no gate table (no row token written).
            return outcome(rep, stage, "PR-S0") == "fail" and not all_pass(rep["stages"][stage]["checks"])
        if mu == "MU-13":
            target = {"members": "members.json", "rows": "gate-table.rows.json", "final": "gate-table.json"}[stage]
            p = sb.rec_path(target)
            with open(p, "rb") as fh:
                data = fh.read()
            with open(p, "wb") as fh:
                fh.write(flip_digit(data))
            rep = check_stage(sb, stage)
            return rep["status"] != 0 and rep["stages"][stage]["replay"]["REPLAY-" + target] is False
        if mu in ("MU-14a", "MU-14b", "MU-14c"):
            sha = committed_members_sha(sb)
            if mu == "MU-14c":
                sb = sandbox_copy(ctx, os.path.join(tmp, "repo-c"), skip=(REC_REL + "/members.json",))
            else:
                p = sb.rec_path("members.json")
                if mu == "MU-14a":
                    os.remove(p)
                else:
                    with open(p, "rb") as fh:
                        data = fh.read()
                    with open(p, "wb") as fh:
                        fh.write(flip_digit(data))
            ok = True
            if mu != "MU-14c":
                for which in ("A", "B"):
                    with tempfile.TemporaryDirectory() as t2:
                        ok = ok and run_impl(sb, which, "rows", t2, sha) == 2
            code = subprocess.run([sys.executable, "-I", sb.rec_path("controls.py"), "run", "--stage", "rows"],
                                  cwd=sb.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode
            return ok and code == 2
        if mu == "MU-11":
            if not sb.has_rec("adversarial.json"):
                open_question("OQ-C6", "MU-11 when no row passes G5 (no adversarial.json to mutate)")
            open_question("OQ-C6", "MU-11's mutated token and how the self-test confirms 'that row recorded "
                                   "UNDECIDED(G6)' (from A's and B's final outputs)")
        if mu in ("MU-C1", "MU-C2", "MU-C3"):
            open_question("OQ-C3", "location and format of the frozen patches for MU-C1 to MU-C3 and the "
                                   "tool that applies them")
    raise ValueError("unknown mutation " + mu)


def cmd_self_test_stage(ctx, stage):
    base = check_stage(ctx, stage)
    if base["status"] != 0:
        print("baseline check --stage " + stage + " does not exit 0")
        return 1
    failed = []
    for mu in mutations_for(stage):
        ok = apply_mutation(ctx, stage, mu)
        print(mu + " " + ("detected" if ok else "NOT detected"))
        if not ok:
            failed.append(mu)
    return 1 if failed else 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

USAGE = ("usage: controls.py run --stage {members|rows|final}\n"
         "       controls.py check [--stage {members|rows|final}]\n"
         "       controls.py self-test {--synthetic | --stage {members|rows|final}}\n"
         "       controls.py render\n")


def parse_stage(args):
    if len(args) == 2 and args[0] == "--stage" and args[1] in STAGES:
        return args[1]
    raise Refusal("bad arguments\n" + USAGE)


def main(argv):
    try:
        if not argv:
            raise Refusal(USAGE)
        cmd, rest = argv[0], argv[1:]
        if cmd == "self-test" and rest == ["--synthetic"]:
            return cmd_self_test_synthetic()
        ctx = ctx_from_file()
        if cmd == "run":
            return cmd_run(ctx, parse_stage(rest))
        if cmd == "check":
            return cmd_check(ctx, parse_stage(rest) if rest else None)
        if cmd == "self-test":
            return cmd_self_test_stage(ctx, parse_stage(rest))
        if cmd == "render" and not rest:
            return cmd_render(ctx)
        raise Refusal(USAGE)
    except OpenQuestion as exc:
        sys.stderr.write("refused: " + str(exc) + "\n")
        return 2
    except Refusal as exc:
        sys.stderr.write("refused: " + str(exc) + "\n")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
