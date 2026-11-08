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
  python3 -I <rec>/controls.py render --out <fresh-empty-directory>

Exit statuses: 0 every check and comparison holds; 1 a check, comparison or mutation
failed; 2 a refusal (usage, a stage precondition or absent/mis-pinned self-test inputs).
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
PATCH_SHA256 = {
    "MU-C1": "5d96ab821dc56cb874b75c8c6482c0cd376b0a3ebc40892614ab2fa0fb4dba4d",
    "MU-C2": "bcbb8ad013aff79bae2fe1d4582791fb9bd434b04543c043600c142778e1c822",
    "MU-C3": "3f278c93a678c033bc39a8a596eb9da9cf6b14f95f1308acb35298abba09e411",
}


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


def partition_subtests(universe, step, cycles, histogram=None):
    """Structured p1-p7 findings; histogram, when supplied, is part of p2."""
    findings = {"p" + str(i): [] for i in range(1, 8)}
    uni, seen, total, previous, counted_histogram = set(universe), set(), 0, None, {}
    for index, (key, size, states) in enumerate(cycles):
        tag = "cycle #" + str(index) + " (" + str(key) + ")"
        states = list(states)
        state_set = set(states)
        if not is_int(size) or size != len(states):
            findings["p2"].append(tag + ": size differs from state count")
        if is_int(size):
            total += size
            counted_histogram[str(size)] = counted_histogram.get(str(size), 0) + 1
        if states != sorted(states):
            findings["p5"].append(tag + ": states not sorted")
        if not states or key != min(states):
            findings["p6"].append(tag + ": key is not the least state")
        if previous is not None and not key > previous:
            findings["p7"].append(tag + ": keys not strictly increasing")
        previous = key
        for state in states:
            if state not in uni:
                findings["p1"].append(tag + ": state outside universe")
            if state in seen:
                findings["p1"].append(tag + ": repeated state within or between cycles")
            seen.add(state)
        if not states:
            findings["p4"].append(tag + ": empty orbit")
            continue
        if any(step(state) not in state_set for state in states):
            findings["p3"].append(tag + ": not closed under the map")
        orbit, current, closed = [key], key, False
        for _ in range(len(uni)):
            current = step(current)
            if current == key:
                closed = True
                break
            orbit.append(current)
        if not closed or sorted(orbit) != sorted(states):
            findings["p4"].append(tag + ": not exactly one orbit of its key")
    if seen != uni:
        findings["p1"].append("coverage differs from universe")
    if total != len(uni):
        findings["p2"].append("sizes do not sum to universe size")
    if histogram is not None and not same(histogram, counted_histogram):
        findings["p2"].append("histogram differs from listed size counts")
    return findings


def partition_findings(universe, step, cycles, histogram=None):
    subtests = partition_subtests(universe, step, cycles, histogram)
    return [pid + ": " + finding for pid, findings in subtests.items() for finding in findings]


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
        raise ValueError("members.json: first member is not pi0 of size " + str(count))
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

    if "region" in gt:
        rat(gt["region"]["q_pow_minus_E"], "region.q_pow_minus_E")
    for i, r in enumerate(gt.get("rows", [])):
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
    cycles = members_cycles(env["members"], env["cells"])
    allst = [s for c in cycles for s in c[2]]
    if len(allst) != S_SIZE or len(set(allst)) != S_SIZE:
        f.append("members.json does not list " + str(S_SIZE) + " distinct states")
    return f


def chk_cc_bij(env):
    return [] if env["gt"]["completeness"]["bijection"] is True else ["completeness.bijection is not true"]


def chk_cc_part(env):
    cycles = members_cycles(env["members"], env["cells"])
    f = partition_findings(env["universe"], env["step"], cycles, env["members"]["histogram"])
    comp = env["gt"]["completeness"]
    if comp["partition"] is not True:
        f.append("completeness.partition is not true")
    if not same(comp["length_sum"], env["state_count"]):
        f.append("completeness.length_sum != " + str(S_SIZE))
    if not same(comp["cycles"], len(cycles)):
        f.append("completeness.cycles != number of listed cycles")
    return f


def chk_cc_cyc2(env):
    """One rank/fixed/period/cycle checker parameterized by the output profile."""
    c = env["cyc2"]
    fixture = env.get("fixture", False)
    kmax, count, n = env["kmax"], env["state_count"], len(env["cells"])
    fields = {"schema", "version", "fix", "period_states", "cycles"}
    fields |= {"fixture", "kmax", "ranks", "identity_at_kmax"} if fixture else {"m10_identity"}
    if not keys_are(c, fields) or c["schema"] != ("k1p1-fixture-cyc2" if fixture else "k1p1-cyc2") or not same(c["version"], 1):
        return ["cycle-count schema/version"]
    if fixture and (not same(c["kmax"], kmax) or c["fixture"] != env["gt"]["fixture"]):
        return ["rank-chain id/kmax"]
    ks = [str(k) for k in range(1, kmax + 1)]
    integer_fields = ("ranks", "fix", "period_states", "cycles") if fixture else ("fix", "period_states", "cycles")
    if any(not keys_are(c[fld], ks) or not all(is_int(v) for v in c[fld].values()) for fld in integer_fields):
        return ["cycle-count key/types"]
    f = []
    for k in ks:
        fix = c["fix"][k]
        if fix < 1 or fix > count or (fix & (fix - 1)) != 0:
            f.append("fixed count not a power of two in [1, |S|] at " + k)
        if fixture:
            rank = c["ranks"][k]
            if not 0 <= rank <= n or fix != 2 ** (n - rank):
                f.append("rank-to-fixed count differs at " + k)
    for d in range(1, kmax + 1):
        ps = sum(mobius(d // e) * c["fix"][str(e)] for e in range(1, d + 1) if d % e == 0)
        if ps < 0 or ps != c["period_states"][str(d)] or ps % d or c["cycles"][str(d)] * d != ps:
            f.append("Moebius/period/cycle chain differs at " + str(d))
        if c["cycles"][str(d)] != env["members"]["histogram"].get(str(d), 0):
            f.append("cycles differ from histogram at " + str(d))
    identity = c["identity_at_kmax"] if fixture else c["m10_identity"]
    if not set(env["members"]["histogram"]) <= set(ks) or identity is not True or c["fix"][str(kmax)] != count:
        f.append("identity or histogram range differs")
    return f


def chk_cc_rows(env):
    f = []
    keys = member_keys(env["members"], env["cells"])
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
    expected = env["expected_region"]
    if not same(reg["E"], expected["E"]):
        f.append("region.E differs from preserved value")
    if not same(reg["W_eq"], expected["W_eq"]):
        f.append("region.W_eq differs from preserved value")
    return f


def chk_pr_cyc(env):
    f = []
    cycles = members_cycles(env["members"], env["cells"])
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
    cycles = members_cycles(env["members"], env["cells"])
    allst = instance_states()
    if set(phi(s) for s in allst) != set(allst):
        f.append("phi(supp pi0) != supp pi0")
    for key, _, states in cycles:
        if set(env["step"](s) for s in states) != set(states):
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
        rows = [r for r in gt["rows"] if r["branch"] == b and r["member"] == env["zero"]]
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
    cycles = members_cycles(env["members"], env["cells"])
    sizes = {"pi0": env["state_count"]}
    t2 = {"pi0": False}
    for key, size, states in cycles:
        sizes[key] = size
        t2[key] = set(env["step"](s) for s in states) != set(states)
    adv = {}
    if env["stage"] == "final" and env.get("adv") is not None:
        adv = {(e["branch"], e["member"]): e["token"] for e in env["adv"]["rows"]}
    info = {"E": list(gt["region"]["E"]), "W_eq": list(gt["region"]["W_eq"]), "cd": env["cd"],
            "stage": env["stage"], "sizes": sizes, "t2": t2, "adv": adv,
            "state_count": env["state_count"], "q": env["q"]}
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
        if os.path.isfile(p) and not os.path.islink(p):
            with open(p, "rb") as fh:
                out[name] = fh.read()
    return out


def output_snapshot(directory):
    """Exact output tree: directories, regular-file bytes, links and other entry types.

    Symlinks are recorded without following them, and empty directories are retained.
    Normal schema readers continue to use read_dir's file dictionary separately.
    """
    snapshot = {}

    def visit(path, relative):
        if os.path.islink(path):
            snapshot[relative] = ("symlink", os.readlink(path))
        elif os.path.isdir(path):
            snapshot[relative] = ("directory",)
            for name in sorted(os.listdir(path)):
                visit(os.path.join(path, name), name if relative == "." else relative + "/" + name)
        elif os.path.isfile(path):
            with open(path, "rb") as fh:
                snapshot[relative] = ("file", fh.read())
        else:
            snapshot[relative] = ("other", os.stat(path, follow_symlinks=False).st_mode)

    visit(directory, ".")
    return snapshot


def flat_output_snapshot(files):
    return {".": ("directory",), **{name: ("file", data) for name, data in files.items()}}


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
        env = {"stage": stage, "cd": cd, "adv": adv, "rows_gt": rows_gt, "notes": notes,
               "cells": CELLS, "state_count": S_SIZE, "q": Q, "zero": DELTA0,
               "universe": instance_states(), "step": phi, "kmax": 10,
               "expected_region": {"E": PR_E_E, "W_eq": PR_E_WEQ}}
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


def cmd_run(ctx, stage, mutate=None, impl_paths=None):
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
        done, outputs, codes, findings = execute_stage(ctx, stage, sha, mutate, impl_paths)
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


def check_stage(ctx, stage, mutate=None, quiet=True, impl_paths=None):
    """`check --stage s`: regenerate every stage up to s and compare with the committed files.

    Returns {"status": 0|1, "stages": {t: {"checks", "findings", "replay"}}, "render": ...}.
    """
    report = {"status": 0, "stages": {}, "render": None}
    for t in STAGES[: STAGES.index(stage) + 1]:
        members_sha = None
        if t != "members":
            members_sha = committed_members_sha(ctx)
        hook = mutate.get(t) if mutate else None
        checks, outputs, codes, findings = execute_stage(ctx, t, members_sha, hook, impl_paths)
        checks = [{"id": cid, "outcome": "pass"} for cid in precondition_ids(t)] + checks
        files = stage_outputs(t, checks, outputs, codes)
        replay = {}
        for name in STAGE_FILES[t]:
            committed = ctx.read_rec(name) if ctx.has_rec(name) else None
            replay["REPLAY-" + name] = committed is not None and files.get(name) == committed
        report["stages"][t] = {"checks": checks, "findings": findings, "replay": replay, "exit_status": codes}
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
    try:
        return check_stage(ctx, stage, quiet=False)["status"]
    except (OSError, ValueError, KeyError, IndexError, TypeError, Refusal) as exc:
        sys.stderr.write("check failure: " + type(exc).__name__ + "\n")
        return 1


# ---------------------------------------------------------------------------
# Schema and deterministic projection (A1 section 9). No map is evaluated here.
# ---------------------------------------------------------------------------

LABELS = ("H-2s (declared)", "H-cur (declared)", H_INV, "H-law", "H-ret", "H-sel")
BEGIN_MARKER = "<!-- k1p1-token-tables:v1:begin -->"
END_MARKER = "<!-- k1p1-token-tables:v1:end -->"


def keys_are(obj, keys):
    return isinstance(obj, dict) and set(obj) == set(keys)


def hex_digest(v):
    return isinstance(v, str) and len(v) == 64 and all(c in "0123456789abcdef" for c in v)


def label_list(text):
    labels = text.split(", ")
    return bool(text) and labels == sorted(set(labels)) and all(x in LABELS for x in labels)


def row_token_valid(token, branch, key):
    if not isinstance(token, str):
        return False
    if token in ("pending", "VOID[row]", "Z1-VOID[IMPORTED]", "Z1-VOID[DYN]"):
        return True
    if token in ["UNDECIDED(G" + str(k) + ")" for k in range(1, 8)]:
        return True
    for typ in ("ABSENT", "BLIND"):
        if token == typ + "[" + member_name(key) + "; " + branch + "; " + ", ".join(ACCESS[branch]) + "]":
            return True
    if token.startswith("CONDITIONAL[") and token.endswith("]"):
        return label_list(token[len("CONDITIONAL["):-1])
    if token.startswith("AVAILABLE[H-sel](") and token.endswith(")"):
        return label_list(token[len("AVAILABLE[H-sel]("):-1])
    return False


def class_token_valid(token, branch, keys, union):
    if token is None:
        return union is True
    if union is not False or not isinstance(token, str):
        return False
    if token in ("pending", "Z1-VOID[IMPORTED]", "Z1-VOID[DYN]", "Z1-VOID[IMPORTED, DYN]"):
        return True
    for typ in ("ABSENT", "BLIND"):
        if token == typ + "[" + CLASS_SET + "; " + branch + "; " + ", ".join(ACCESS[branch]) + "]":
            return True
    if token.startswith("UNDECIDED(") and token.endswith(")"):
        parts = token[len("UNDECIDED("):-1].split(", ")
        return bool(parts) and parts == sorted(set(parts)) and all(x in ["G" + str(k) for k in range(1, 8)] for x in parts)
    if token.startswith("VOID[row](") and token.endswith(")"):
        names = token[len("VOID[row]("):-1].split(", ")
        expected = [member_name(k) for k in keys if member_name(k) in names]
        return bool(names) and names == expected
    return False


def members_shape(mdoc, cells):
    cycles = members_cycles(mdoc, cells)
    if not isinstance(mdoc["histogram"], dict) or not all(_digits(k) and str(int(k)) == k and int(k) > 0
            and is_int(v) and v > 0 for k, v in mdoc["histogram"].items()):
        return False
    keys = [c[0] for c in cycles]
    if keys != sorted(set(keys)):
        return False
    return all(size > 0 and states and size == len(states) and states == sorted(set(states)) and key == states[0]
               for key, size, states in cycles)


def typed_like(value, template):
    if isinstance(template, dict):
        return keys_are(value, template) and all(typed_like(value[k], v) for k, v in template.items())
    if isinstance(template, list):
        return isinstance(value, list) and all(typed_like(x, template[0]) for x in value) if template else value == []
    if template is None:
        return value is None
    if isinstance(template, str) and "/" in template and all(c in "0123456789-/" for c in template):
        parse_rational(value)
    return type(value) is type(template)


def region_shape(region, cells):
    if not keys_are(region, ("E", "W_eq", "q_pow_minus_E", "overlap", "overlap_tautological")):
        return False
    for k in ("E", "W_eq"):
        seq = region[k]
        if not isinstance(seq, list) or seq != [c for c in cells if c in seq]:
            return False
    parse_rational(region["q_pow_minus_E"])
    if not keys_are(region["overlap"], ("B-eq", "B-ct")) or not keys_are(region["overlap_tautological"], ("B-eq", "B-ct")):
        return False
    for b in ("B-eq", "B-ct"):
        seq = region["overlap"][b]
        if not isinstance(seq, list) or seq != [c for c in cells if c in seq] or not is_bool(region["overlap_tautological"][b]):
            return False
    return True


def completeness_shape(doc, stage):
    if not keys_are(doc, ("states", "length_sum", "cycles", "distinct", "bijection", "partition", "mass_sums")):
        return False
    if not all(is_int(doc[k]) and doc[k] >= 0 for k in ("states", "length_sum", "cycles")):
        return False
    if not all(is_bool(doc[k]) for k in ("distinct", "bijection", "partition")):
        return False
    return doc["mass_sums"] is None if stage == "members" else is_bool(doc["mass_sums"])


def row_shape(row, cells, region):
    if not keys_are(row, ROW_KEYS):
        return False
    b, key = row["branch"], row["member"]
    if b not in BRANCHES or not isinstance(key, str) or (key != "pi0" and not is_bits(key, len(cells))):
        return False
    if row["candidate"] != "P1" or row["w_rule"] != W_RULE[b] or row["w_inputs"] != W_INPUTS[b]:
        return False
    if not is_int(row["support_size"]) or row["support_size"] <= 0:
        return False
    parse_rational(row["d_ratio"])
    width = 0 if b == "B-pl" else len(region["W_eq"])
    for name in ("weak", "mass", "pi0_ref"):
        if not isinstance(row[name], dict):
            return False
        for w, value in row[name].items():
            if not is_bits(w, width) or not 0 <= parse_rational(value) <= 1:
                return False
    sharp = row["sharp_w"]
    if not isinstance(sharp, list) or sharp != sorted(set(sharp)) or not all(is_bits(w, width) for w in sharp):
        return False
    if not keys_are(row["nb"], sharp) or not all(is_bool(v) for v in row["nb"].values()):
        return False
    if not is_bool(row["w_certified"]) or not (is_bool(row["nb_g1"]) if b == "B-pl" else row["nb_g1"] is None):
        return False
    if b == "B-pl" and not is_bool(row["bound_ok"]):
        return False
    if b == "B-eq" and not (keys_are(row["bound_ok"], sharp) and all(is_bool(v) for v in row["bound_ok"].values())):
        return False
    if b == "B-ct" and row["bound_ok"] is not None:
        return False
    if not isinstance(row["ledger"], str) or not keys_are(row["g2"], ("a", "t1", "t2", "hsel_content")):
        return False
    if not all(is_bool(row["g2"][k]) for k in ("a", "t1", "t2")):
        return False
    content = row["g2"]["hsel_content"]
    if not isinstance(content, list):
        return False
    for e in content:
        if not keys_are(e, ("w", "values")) or not is_bits(e["w"], width) or not isinstance(e["values"], list):
            return False
        if e["values"] != sorted(set(e["values"])) or not all(is_bits(v, len(region["E"])) for v in e["values"]):
            return False
    hyps = row["hypotheses"]
    if not isinstance(hyps, list) or not hyps or hyps != sorted(set(hyps)) or not all(h in LABELS for h in hyps):
        return False
    if not keys_are(row["gates"], GATES) or not all(v in ("pass", NR, "pending") or row_token_valid(v, b, key)
                                                for v in row["gates"].values()):
        return False
    if not row_token_valid(row["token"], b, key):
        return False
    useful = row["usefulness"]
    if useful is not None:
        if not keys_are(useful, sharp):
            return False
        for entry in useful.values():
            if not keys_are(entry, ("disjoint", "law_only")):
                return False
            for seq in entry.values():
                if not isinstance(seq, list) or seq != sorted(seq):
                    return False
                if not all(isinstance(pair, list) and len(pair) == 2 and all(is_bits(x, 2) for x in pair)
                           and pair[0] < pair[1] for pair in seq):
                    return False
    return True


def checks_shape(doc, stage):
    fields = {"schema", "version", "stage", "checks", "exit_status"}
    if stage == "members":
        fields.add("members_sha256")
    if stage == "final":
        fields.add("gate_table_sha256")
    if not keys_are(doc, fields) or doc["schema"] != "k1p1-checks" or not same(doc["version"], 1) or doc["stage"] != stage:
        return False
    if not keys_are(doc["exit_status"], ("A", "B")) or not all(v is None or (is_int(v) and v in (0, 1, 2, 3))
                                                            for v in doc["exit_status"].values()):
        return False
    if not isinstance(doc["checks"], list):
        return False
    if not all(keys_are(c, ("id", "outcome")) and isinstance(c["id"], str)
               and c["outcome"] in ("pass", "fail", "refused") for c in doc["checks"]):
        return False
    digest = doc["members_sha256"] if stage == "members" else doc.get("gate_table_sha256")
    return digest is None or hex_digest(digest)


def projection_schema(gt, mdoc, synthetic=False):
    if float_paths(gt) or float_paths(mdoc):
        return False
    cells = gt["cell_order"] if synthetic else list(CELLS)
    if not isinstance(cells, list) or not cells or len(set(cells)) != len(cells) or not all(isinstance(c, str) for c in cells):
        return False
    if not members_shape(mdoc, cells):
        return False
    common = {"schema", "version", "stage", "region", "completeness", "rows", "class_tokens", "union_clause_reached"}
    fields = common | ({"fixture", "kind", "cell_order", "members", "histogram"} if synthetic else {"instance", "preserved", "controls"})
    if not keys_are(gt, fields) or gt["schema"] != ("k1p1-fixture-output" if synthetic else "k1p1-gate-table"):
        return False
    if not same(gt["version"], 1) or gt["stage"] != "final":
        return False
    if synthetic:
        if gt["kind"] != "system" or not isinstance(gt["fixture"], str):
            return False
    else:
        if not same(gt["instance"], {"N": 5, "a": 1, "d": 1, "q": 2}):
            return False
        preserved = gt["preserved"]
        if not keys_are(preserved, ("energy_conserved", "shell_sizes", "phi_order")) or not is_bool(preserved["energy_conserved"]):
            return False
        if not is_int(preserved["phi_order"]) or preserved["phi_order"] < 1 or not keys_are(preserved["shell_sizes"], ("0", "1")):
            return False
        if not all(is_int(v) and v >= 0 for v in preserved["shell_sizes"].values()):
            return False
        ctl = gt["controls"]
        if not isinstance(ctl, list) or [c.get("id") for c in ctl] != list(S0_ORDER):
            return False
        for c in ctl:
            cid = c["id"]
            if not keys_are(c, ("id", "gate", "computed", "expected", "paper", "outcome")) or c["gate"] != S0_GATE[cid]:
                return False
            if not typed_like(c["computed"], S0_EXPECTED[cid]) or not same(c["expected"], S0_EXPECTED[cid]):
                return False
            if c["paper"] not in (None, "pass", "fail", "undecided") or c["outcome"] not in ("pass", "fail"):
                return False
    if not region_shape(gt["region"], cells) or not completeness_shape(gt["completeness"], "final"):
        return False
    keys = member_keys(mdoc, cells)
    rows = gt["rows"]
    if not isinstance(rows, list) or [(r["branch"], r["member"]) for r in rows] != [(b, k) for b in BRANCHES for k in keys]:
        return False
    if not all(row_shape(r, cells, gt["region"]) for r in rows):
        return False
    if not keys_are(gt["class_tokens"], BRANCHES) or not keys_are(gt["union_clause_reached"], BRANCHES):
        return False
    return all(is_bool(gt["union_clause_reached"][b]) and
               class_token_valid(gt["class_tokens"][b], b, keys, gt["union_clause_reached"][b]) for b in BRANCHES)


def fixture_members(doc):
    return {"schema": "k1p1-members", "version": 1, "cell_order": doc["cell_order"],
            "members": doc["members"], "histogram": doc["histogram"]}


def project_tokens(gt, mdoc, synthetic=False, cm=None, cf=None, raw=None):
    try:
        if not projection_schema(gt, mdoc, synthetic):
            return "BAD_SCHEMA", None
        if not synthetic:
            if not checks_shape(cm, "members") or not checks_shape(cf, "final"):
                return "BAD_SCHEMA", None
            if any(dumps(doc) != data for doc, data in zip((gt, mdoc, cm, cf), raw)):
                return "BAD_SCHEMA", None
            if cm["members_sha256"] != hashlib.sha256(raw[1]).hexdigest() or cf["gate_table_sha256"] != hashlib.sha256(raw[0]).hexdigest():
                return "INPUT_MISMATCH", None
        if any(gt["union_clause_reached"].values()):
            return "UNION_REACHED", None
        if not synthetic:
            green = [{"id": cid, "outcome": "pass"} for cid in FINAL_ROSTER]
            if any(c["outcome"] != "pass" for c in gt["controls"]) or cf["checks"] != green:
                return "CONTROL_NOT_GREEN", None
        if any(r["token"] == "pending" for r in gt["rows"]) or any(t == "pending" for t in gt["class_tokens"].values()):
            return "INCOMPLETE_TOKENS", None
        lines = [BEGIN_MARKER, "", "| Branch | Member | Token |", "| --- | --- | --- |"]
        for r in gt["rows"]:
            lines.append("| " + r["branch"] + " | `" + member_name(r["member"]) + "` | `" + r["token"] + "` |")
        lines += ["", "| Branch | Class token |", "| --- | --- |"]
        lines += ["| " + b + " | `" + gt["class_tokens"][b] + "` |" for b in BRANCHES]
        lines += ["", END_MARKER]
        return "OK", ("\n".join(lines) + "\n").encode("utf-8")
    except (KeyError, TypeError, ValueError, IndexError, AttributeError):
        return "BAD_SCHEMA", None


def render_from_record(ctx):
    try:
        raw = [ctx.read_rec(n) for n in ("gate-table.json", "members.json", "checks.members.json", "checks.json")]
        docs = [loads(b) for b in raw]
    except (FileNotFoundError, ValueError, UnicodeError):
        return "MISSING_INPUT", None
    return project_tokens(*docs[:2], cm=docs[2], cf=docs[3], raw=raw)


def marker_matches(document, fragment):
    if fragment is None:
        return False
    begin, end = BEGIN_MARKER.encode("utf-8") + b"\n", END_MARKER.encode("utf-8") + b"\n"
    lines = document.splitlines(keepends=True)
    # Count marker spellings as well, so extra unterminated or CRLF markers cannot hide.
    if document.count(BEGIN_MARKER.encode()) != 1 or document.count(END_MARKER.encode()) != 1:
        return False
    starts = [i for i, line in enumerate(lines) if line == begin]
    ends = [i for i, line in enumerate(lines) if line == end]
    return len(starts) == len(ends) == 1 and starts[0] < ends[0] and b"".join(lines[starts[0]:ends[0] + 1]) == fragment


def cmd_render(ctx, out):
    if not os.path.isdir(out) or os.listdir(out):
        raise Refusal("render --out must name a fresh empty directory")
    digest = None
    try:
        if ctx.has_rec("gate-table.json"):
            digest = hashlib.sha256(ctx.read_rec("gate-table.json")).hexdigest()
        reason, fragment = render_from_record(ctx)
        outcome = "pass" if reason == "OK" else "refused"
        status = {"schema": "k1p1-render-status", "version": 1, "stage": "final", "outcome": outcome,
                  "reason": reason, "gate_table_sha256": digest,
                  "fragment_sha256": hashlib.sha256(fragment).hexdigest() if fragment is not None else None}
        files = {"render-status.json": dumps(status)}
        if fragment is not None:
            files["token-tables.md"] = fragment
        for name, data in files.items():
            with open(os.path.join(out, name + ".tmp"), "wb") as fh:
                fh.write(data)
        for name in files:
            os.replace(os.path.join(out, name + ".tmp"), os.path.join(out, name))
        return 0 if outcome == "pass" else 2
    except OSError:
        status = {"schema": "k1p1-render-status", "version": 1, "stage": "final", "outcome": "fail",
                  "reason": "IO_ERROR", "gate_table_sha256": digest, "fragment_sha256": None}
        try:
            if os.path.exists(os.path.join(out, "token-tables.md")):
                os.remove(os.path.join(out, "token-tables.md"))
            with open(os.path.join(out, "render-status.json.tmp"), "wb") as fh:
                fh.write(dumps(status))
            os.replace(os.path.join(out, "render-status.json.tmp"), os.path.join(out, "render-status.json"))
        except OSError:
            pass
        return 1
    finally:
        for name in ("render-status.json.tmp", "token-tables.md.tmp"):
            try:
                os.remove(os.path.join(out, name))
            except FileNotFoundError:
                pass


# ---------------------------------------------------------------------------
# Self-test (§11.2, §11.3)
# ---------------------------------------------------------------------------

def clone(value):
    return loads(dumps(value))


def path_set(doc, path, value):
    node = doc
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = clone(value)


def apply_ops(doc, ops):
    for op in ops:
        path = op["path"]
        node = doc
        for key in path[:-1]:
            node = node[key]
        last = path[-1]
        if op["op"] == "set":
            node[last] = clone(op["value"])
        elif op["op"] == "delete":
            del node[last]
        elif op["op"] == "duplicate":
            node.insert(last, clone(node[last]))
        elif op["op"] == "swap":
            seq = node[last]
            i, j = op["i"], op["j"]
            seq[i], seq[j] = seq[j], seq[i]
        else:
            raise ValueError("unknown fixture operation")
    return doc


def pinned_self_inputs(ctx):
    try:
        data = ctx.read_rec("amendments/A1-fixtures.json")
        if hashlib.sha256(data).hexdigest() != FIXTURE_SHA256:
            raise Refusal("A1-fixtures.json SHA256 differs")
        patches = {}
        for mu in ("MU-C1", "MU-C2", "MU-C3"):
            pin = PATCH_SHA256[mu]
            if not hex_digest(pin):
                raise Refusal(mu + " final patch binding absent")
            patch = ctx.read_rec("amendments/A1-patches/" + mu + ".patch")
            if hashlib.sha256(patch).hexdigest() != pin:
                raise Refusal(mu + " patch SHA256 differs")
            patches[mu] = patch
        return loads(data), patches
    except (OSError, ValueError, UnicodeError) as exc:
        raise Refusal("self-test input absent or malformed: " + type(exc).__name__)


def splice_patch(source, patch, expected_path):
    """Strict unified-diff splice: no fuzz, offset, external patch program or execution."""
    old = source.decode("utf-8").splitlines(keepends=True)
    diff = patch.decode("utf-8").splitlines(keepends=True)
    if not source.endswith(b"\n") or not patch.endswith(b"\n"):
        raise ValueError("patch and source must end with LF")
    if len(diff) < 3 or diff[0] != "--- a/" + expected_path + "\n" or diff[1] != "+++ b/" + expected_path + "\n":
        raise ValueError("patch must name one frozen source file")
    output, cursor, delta, i = [], 0, 0, 2
    while i < len(diff):
        header = diff[i]
        if not header.startswith("@@ -") or " @@" not in header:
            raise ValueError("invalid hunk header")
        coordinates = header[4:].split(" @@", 1)[0].split(" +")
        if len(coordinates) != 2:
            raise ValueError("invalid hunk coordinates")
        ranges = []
        for item in coordinates:
            pair = item.split(",")
            if len(pair) != 2 or not all(_digits(v) for v in pair):
                raise ValueError("hunk ranges require start,count")
            ranges.append(tuple(int(v) for v in pair))
        (start, old_count), (new_start, new_count) = ranges
        at = start - 1 if old_count else start
        expected_new = at + delta + (1 if new_count else 0)
        if at < cursor or at > len(old) or new_start != expected_new:
            raise ValueError("hunk order/start offset differs")
        i += 1
        before, after = [], []
        while i < len(diff) and not diff[i].startswith("@@ "):
            line = diff[i]
            if line[:1] not in (" ", "+", "-"):
                raise ValueError("unsupported patch line")
            if line[0] in " -":
                before.append(line[1:])
            if line[0] in " +":
                after.append(line[1:])
            i += 1
        if len(before) != old_count or len(after) != new_count or old[at:at + old_count] != before:
            raise ValueError("hunk old lines/counts differ at exact start")
        output += old[cursor:at] + after
        cursor = at + old_count
        delta += new_count - old_count
    output += old[cursor:]
    return "".join(output).encode("utf-8")


def fixture_expected(entries, fid, cyc2=False):
    entry = entries[fid]
    name = "expected_cyc2" if cyc2 else "expected"
    if name in entry:
        return clone(entry[name])
    origin = entry.get(name + "_from")
    if origin is None:
        return None
    doc = fixture_expected(entries, origin, cyc2)
    doc["fixture"] = fid
    if not cyc2:
        for change in entry.get("expected_set", []):
            path_set(doc, change["path"], change["value"])
    return doc


def run_fixture(ctx, which, fid, input_bytes, extra=(), nonempty=False, program=None):
    """Only fixture CLI; malformed combinations are confined to the frozen NF cases."""
    with tempfile.TemporaryDirectory() as tmp:
        inp, out = os.path.join(tmp, "input.json"), os.path.join(tmp, "out")
        os.mkdir(out)
        if input_bytes is not None:
            with open(inp, "wb") as fh:
                fh.write(input_bytes)
        if nonempty:
            with open(os.path.join(out, "sentinel"), "wb") as fh:
                fh.write(b"preserve fixture sentinel\n")
        before = output_snapshot(out)
        argv = [sys.executable, "-I", program or os.path.join(ctx.root, *IMPL[which].split("/")),
                "--fixture", fid, "--input", inp, "--out", out] + list(extra)
        code = subprocess.run(argv, cwd=ctx.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode
        after = output_snapshot(out)
        return code, read_dir(out), before, after


def fixture_env(entry, doc, cyc2):
    data = entry["input"]
    cells = data["cells"]
    universe = ["".join(bits) for bits in itertools.product("01", repeat=len(cells))]
    if data["kind"] == "perm":
        step = lambda state: data["image"][state]
    else:
        def step(state):
            values = dict(zip(cells, (int(v) for v in state)))
            return "".join(str(sum(values[c] for c in data["phi"][out]) % data["q"]) for out in cells)
    return {"stage": doc.get("stage", "members"), "members": fixture_members(doc), "gt": doc,
            "cyc2": cyc2, "cells": cells, "universe": universe, "step": step,
            "state_count": len(universe), "zero": "0" * len(cells), "q": data.get("q", 2),
            "cd": data.get("class_decisions"),
            "adv": {"rows": data.get("adversarial", [])}, "fixture": True}


def fixture_checks(entry, outputs, expected, expected_cyc2):
    result = {}
    if "A" in outputs and "B" in outputs:
        result["AB'"] = "pass" if outputs["A"].get("fixture.json") == outputs["B"].get("fixture.json") else "fail"
    result["EXPECTED'"] = "pass" if all(out.get("fixture.json") == dumps(expected) and
        (which != "B" or expected_cyc2 is None or out.get("fixture-cyc2.json") == dumps(expected_cyc2))
        for which, out in outputs.items()) else "fail"
    for which, out in outputs.items():
        doc = loads(out["fixture.json"])
        if entry["input"]["kind"] == "rank":
            vals = {"EXACT'": "fail" if float_paths(doc) else "pass"}
        else:
            cyc = loads(out["fixture-cyc2.json"]) if "fixture-cyc2.json" in out else None
            env = fixture_env(entry, doc, cyc)
            if entry["input"]["kind"] == "system":
                env["expected_region"] = expected["region"]
            vals = {}
            funcs = [("EXACT'", chk_exact), ("CC-PART'", chk_cc_part), ("CC-BIJ'", chk_cc_bij)]
            if which == "B" and entry["input"]["kind"] in ("linear", "system"):
                env["kmax"] = entry["input"]["kmax"]
                funcs.append(("CC-CYC2'", chk_cc_cyc2))
            if entry["input"]["kind"] == "system":
                funcs += [("CC-ROWS'", chk_cc_rows), ("CC-MASS'", chk_cc_mass), ("PR-CR6'", chk_pr_cr6), ("TOKENS'", chk_tokens), ("PR-E'", chk_pr_e)]
            for cid, fn in funcs:
                try:
                    vals[cid] = "fail" if fn(env) else "pass"
                except (ValueError, KeyError, TypeError, IndexError, AttributeError):
                    vals[cid] = "fail"
            if entry["input"]["kind"] == "system":
                vals["CT-INC'"] = chk_ct_inc(env, vals["CC-PART'"] == "pass", vals["CC-ROWS'"] == "pass")[0]
        for cid, value in vals.items():
            result[cid] = combine((result.get(cid, "pass"), value))
            # Keep per-program results so SF-2pb cannot pass from a combined failure alone.
            result[which + ":" + cid] = value
    return result


def synthetic_projection_tests(spec, entries):
    fragments, f = {}, []
    for entry in spec["render_fixtures"]:
        doc = apply_ops(fixture_expected(entries, entry["source"]), entry["ops"])
        reason, fragment = project_tokens(doc, fixture_members(doc), synthetic=True)
        ok = reason == entry["reason"] and (fragment is not None) == (entry["outcome"] == "pass")
        if "fragment" in entry:
            lines = entry["fragment"]
        elif "fragment_from" in entry:
            lines = fragments[entry["fragment_from"]].decode("utf-8").splitlines()
            for replacement in entry["fragment_replace"]:
                lines[replacement["line"]] = replacement["text"]
        else:
            lines = None
        if lines is not None:
            wanted = ("\n".join(lines) + "\n").encode("utf-8")
            ok = ok and fragment == wanted
            fragments[entry["id"]] = wanted
        if not ok:
            f.append(entry["id"] + ": projection differs (" + reason + ")")
    for entry in spec["marker_fixtures"]:
        fragment = fragments[entry["fragment"]]
        text = fragment.decode("utf-8")
        op = entry["op"]
        if op == "remove_begin":
            text = text.replace(BEGIN_MARKER + "\n", "")
        elif op == "duplicate_end":
            text += END_MARKER + "\n"
        elif op == "swap_markers":
            text = text.replace(BEGIN_MARKER, "MARKER_TEMP").replace(END_MARKER, BEGIN_MARKER).replace("MARKER_TEMP", END_MARKER)
        elif op == "crlf":
            text = text.replace("\n", "\r\n")
        elif op == "replace":
            text = text.replace(entry["old"], entry["new"])
        elif op != "none":
            raise ValueError("unknown marker fixture")
        document = ("# result\n\n" + text + "\nProse.\n").encode("utf-8")
        if marker_matches(document, fragment) is not entry["match"]:
            f.append(entry["id"] + ": marker comparison differs")
    adv_entries = {e["id"]: e for e in spec["adv_index_fixtures"]}
    for entry in spec["adv_index_fixtures"]:
        doc = fixture_expected(entries, entry["source"])
        adv = entry.get("adversarial", adv_entries.get(entry.get("adversarial_from"), {}).get("adversarial"))
        valid = not adv_index_findings(doc["rows"], adv, entry["notes"])
        if valid is not entry["pass"]:
            f.append(entry["id"] + ": adversarial index result differs")
    return f


def cmd_self_test_synthetic(ctx):
    spec, patches = pinned_self_inputs(ctx)
    entries = {e["id"]: e for e in spec["fixtures"]}
    outputs, failures = {}, []
    # Step 1: canonical input, subprocess-only independent implementations, exact bytes.
    for fid, entry in entries.items():
        expected, cyc = fixture_expected(entries, fid), fixture_expected(entries, fid, True)
        result = {}
        for which in entry["programs"]:
            code, files, _, after = run_fixture(ctx, which, fid, dumps(entry["input"]))
            wanted = {"fixture.json": dumps(expected)}
            if which == "B" and cyc is not None:
                wanted["fixture-cyc2.json"] = dumps(cyc)
            if code != entry["exit"] or files != wanted or after != flat_output_snapshot(wanted):
                failures.append(fid + "/" + which + ": exit/inventory/expected bytes differ")
            result[which] = files
        if len(result) == 2 and result["A"].get("fixture.json") != result["B"].get("fixture.json"):
            failures.append(fid + ": AB' differs")
        outputs[fid] = result
    if failures:
        for f in failures:
            print(f)
        return 1
    # Step 2: A1's specific SF-2pb negative overrides its general all-pass sentence:
    # both programs must exit 0 with bijection=false, and both own CC-BIJ' checks fail.
    # The preceding SF-2p is the paired passing good-inverse control.
    for fid, entry in entries.items():
        checks = fixture_checks(entry, outputs[fid], fixture_expected(entries, fid), fixture_expected(entries, fid, True))
        for cid, value in checks.items():
            want = "fail" if fid == "SF-2pb" and cid in ("CC-BIJ'", "A:CC-BIJ'", "B:CC-BIJ'") else "pass"
            if value != want:
                failures.append(fid + "/" + cid + ": " + value + ", expected " + want)
    # Step 3: paired controls must hold immediately before each analogue.
    for entry in spec["analogues"]:
        fid = entry["fixture"]
        source = entries[fid]
        expected, cyc = fixture_expected(entries, fid), fixture_expected(entries, fid, True)
        named = entry["must_fail"] + entry["must_refuse"]
        baseline = fixture_checks(source, outputs[fid], expected, cyc)
        if any(baseline.get(cid) != "pass" for cid in named):
            failures.append(entry["id"] + ": paired control fails")
            continue
        changed = clone_outputs(outputs[fid])
        targets = ("A", "B") if entry["target"] == "A+B" else (entry["target"],)
        for which in targets:
            name = entry["file"]
            changed[which][name] = dumps(apply_ops(loads(changed[which][name]), entry["ops"]))
        got = fixture_checks(source, changed, expected, cyc)
        if any(got.get(cid) != "fail" for cid in entry["must_fail"]) or any(got.get(cid) != "refused" for cid in entry["must_refuse"]):
            failures.append(entry["id"] + ": mutation not detected by named own check")
    # Step 4: each NF after its specified passing control; unchanged output on refusal.
    # NF-3 explicitly requires the invalid --fixture/--stage mixture. This is the only
    # exception to A1 5.6's general "never passes --stage" sentence: admission must
    # refuse the mixture before entering any instance code (independently reviewed).
    for negative in spec["interface_negatives"]:
        base_id = negative["input_from"] or "SF-1a"
        base = entries[base_id]
        for which in negative["control"]["programs"]:
            code, files, _, after = run_fixture(ctx, which, base_id, dumps(base["input"]))
            wanted = {"fixture.json": dumps(fixture_expected(entries, base_id))}
            cyc = fixture_expected(entries, base_id, True)
            if which == "B" and cyc is not None:
                wanted["fixture-cyc2.json"] = dumps(cyc)
            ok = code == negative["control"]["exit"] and files == wanted and after == flat_output_snapshot(wanted)
            if not ok:
                failures.append(negative["id"] + ": paired CLI control fails")
        inp = clone(base["input"])
        for edit in negative["input_set"]:
            path_set(inp, edit["path"], edit["value"])
        payload = dumps(inp) if negative["input_from"] is not None else None
        for which in negative["programs"]:
            code, files, before, after = run_fixture(ctx, which, negative["fixture_arg"], payload,
                negative["extra_args"], negative["out"] == "nonempty")
            if code != negative["exit"] or after != before:
                failures.append(negative["id"] + "/" + which + ": refusal/unchanged output differs")
    # Step 5: pinned MU-C3, applied by exact splice to a disposable A copy.
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "mutated-a.py")
        try:
            with open(os.path.join(ctx.root, *IMPL["A"].split("/")), "rb") as fh:
                patched = splice_patch(fh.read(), patches["MU-C3"], IMPL["A"])
            with open(path, "wb") as fh:
                fh.write(patched)
            code, files, before, after = run_fixture(ctx, "A", "SF-3", dumps(entries["SF-3"]["input"]), program=path)
            if code != 3 or after != before:
                failures.append("MU-C3': expected exactness exit 3 with no files")
        except (ValueError, UnicodeError):
            failures.append("MU-C3': patch does not apply exactly")
    # Step 6 uses only the same in-memory projection/index functions as production.
    failures += synthetic_projection_tests(spec, entries)
    for f in failures:
        print(f)
    print("synthetic self-test " + ("fail" if failures else "pass"))
    return 1 if failures else 0


def clone_outputs(outputs):
    return {which: dict(files) for which, files in outputs.items()}


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
    return {
        "members": ("MU-3", "MU-4", "MU-8", "MU-13", "MU-C1", "MU-C2"),
        "rows": ("MU-1", "MU-2", "MU-5", "MU-6", "MU-7", "MU-9", "MU-10", "MU-12", "MU-13",
                 "MU-14a", "MU-14b", "MU-14c", "MU-14d", "MU-16a", "MU-16b", "MU-17", "MU-C3"),
        "final": ("MU-11", "MU-13", "MU-15a", "MU-15b", "MU-15c", "MU-15d", "MU-16c"),
    }[stage]


def edit_both(outputs, filename, fn):
    for which in ("A", "B"):
        json_edit(outputs, which, filename, fn)


def subprocess_controls_run(ctx, stage):
    return subprocess.run([sys.executable, "-I", ctx.rec_path("controls.py"), "run", "--stage", stage],
                          cwd=ctx.root, stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode


def pre_outcome(ctx, stage, cid):
    doc = loads(ctx.read_rec(CHECKS_FILE[stage]))
    return next((c["outcome"] for c in doc["checks"] if c["id"] == cid), None)


def g5_keys(ctx):
    rows = loads(ctx.read_rec("gate-table.rows.json"))["rows"]
    return [(r["branch"], r["member"]) for r in rows if r["gates"]["G5"] == "pass"]


def isolated_ten_cycle_exchange(document, universe, step):
    """MU-3 only: exchange nonleast states with a proof obligation on each p1-p7.

    This helper is instance-only and is never called by the synthetic route. No
    eligible exchange is a self-test failure, rather than a skipped mutation.
    """
    original = clone(document)
    original_cycles = members_cycles(original)
    if any(partition_subtests(universe, step, original_cycles, original["histogram"]).values()):
        raise ValueError("MU-3 unmutated partition does not pass")
    tens = [i for i, member in enumerate(original["members"]) if member["size"] == 10 and "states" in member]
    for offset, ai in enumerate(tens):
        a = original["members"][ai]
        for bi in tens[offset + 1:]:
            b = original["members"][bi]
            for x in a["states"]:
                for y in b["states"]:
                    # Outgoing states are nonleast. Incoming states must remain above
                    # the destination's existing key, which is retained byte for byte.
                    if x == a["key"] or y == b["key"] or x <= b["key"] or y <= a["key"]:
                        continue
                    changed = clone(original)
                    changed["members"][ai]["states"] = sorted([s for s in a["states"] if s != x] + [y])
                    changed["members"][bi]["states"] = sorted([s for s in b["states"] if s != y] + [x])
                    subtests = partition_subtests(universe, step, members_cycles(changed), changed["histogram"])
                    preserved = all(not subtests[pid] for pid in ("p1", "p2", "p5", "p6", "p7"))
                    isolated_failure = bool(subtests["p3"] or subtests["p4"])
                    # Beyond the subtests, only these two state lists may differ:
                    # keys, sizes, pi0, member order, histogram and other fields stay exact.
                    restored = clone(changed)
                    for index in (ai, bi):
                        restored["members"][index]["states"] = original["members"][index]["states"]
                    if preserved and isolated_failure and same(restored, original):
                        document.clear()
                        document.update(changed)
                        return True
    raise ValueError("MU-3 has no eligible isolated exchange preserving p1/p2/p5/p6/p7")


def apply_mutation(ctx, stage, mu, patches):
    """Instance-only mutation paths; never reached by --synthetic."""
    gtf = GATE_TABLE[stage]
    with tempfile.TemporaryDirectory() as tmp:
        sb = sandbox_copy(ctx, os.path.join(tmp, "repo"))

        def chk(edit):
            return check_stage(sb, stage, mutate={stage: edit})

        if mu == "MU-1":
            rep = chk(lambda o: edit_both(o, gtf, lambda d: d["rows"].pop(1)))
            return outcome(rep, stage, "CC-ROWS") == "fail" and outcome(rep, stage, "CT-INC") == "refused"
        if mu == "MU-2":
            rep = chk(lambda o: edit_both(o, gtf, lambda d: d["rows"].insert(1, clone(d["rows"][1]))))
            return outcome(rep, stage, "CC-ROWS") == "fail"
        if mu in ("MU-3", "MU-4"):
            def edit_members(d):
                if mu == "MU-3":
                    if not isolated_ten_cycle_exchange(d, instance_states(), phi):
                        raise ValueError("MU-3 isolation not established")
                else:
                    cycle = next(m for m in d["members"][1:] if m["size"] > 1)
                    old = str(cycle["size"])
                    cycle["states"].pop()
                    cycle["size"] -= 1
                    d["histogram"][old] -= 1
                    if not d["histogram"][old]:
                        del d["histogram"][old]
                    new = str(cycle["size"])
                    d["histogram"][new] = d["histogram"].get(new, 0) + 1
            rep = chk(lambda o: edit_both(o, "members.json", edit_members))
            return outcome(rep, stage, "CC-PART") == "fail" and (mu != "MU-4" or outcome(rep, stage, "CT-INC") == "refused")
        if mu == "MU-5":
            def edit(d):
                r = d["rows"][0]
                r["weak"][sorted(r["weak"])[0]] = "0.5"
            return outcome(chk(lambda o: edit_both(o, gtf, edit)), stage, "EXACT") == "fail"
        if mu == "MU-6":
            def edit(d):
                r = d["rows"][0]
                w = sorted(r["weak"])[0]
                v = parse_rational(r["weak"][w])
                delta = Fraction(1, 1024)
                r["weak"][w] = fmt_rational(v + delta if v + delta <= 1 else v - delta)
            rep = chk(lambda o: json_edit(o, "A", gtf, edit))
            return outcome(rep, stage, "AB-gate-table") == "fail" and rep["stages"][stage]["replay"]["REPLAY-" + gtf] is False
        if mu == "MU-7":
            def edit(d):
                d["rows"][1], d["rows"][2] = d["rows"][2], d["rows"][1]
            return outcome(chk(lambda o: edit_both(o, gtf, edit)), stage, "CC-ROWS") == "fail"
        if mu == "MU-8":
            return outcome(chk(lambda o: edit_both(o, gtf, lambda d: d["region"]["E"].remove("y_2"))), stage, "PR-E") == "fail"
        if mu == "MU-9":
            def edit(d):
                r = next(r for r in d["rows"] if r["token"].startswith("ABSENT["))
                r["token"] = r["gates"]["G4"] = "BLIND[" + member_name(r["member"]) + "; " + r["branch"] + "; " + ", ".join(ACCESS[r["branch"]]) + "]"
            return outcome(chk(lambda o: edit_both(o, gtf, edit)), stage, "TOKENS") == "fail"
        if mu == "MU-10":
            return outcome(chk(lambda o: edit_both(o, gtf, lambda d: d["union_clause_reached"].__setitem__("B-pl", True))), stage, "PR-CR6") == "fail"
        if mu == "MU-12":
            def edit(d):
                c = next(c for c in d["controls"] if c["id"] == "CC-EXACT")
                c["computed"]["weak"][""] = "1/1"
                c["outcome"] = "fail"
            # Remove existing sandbox rows so absence measures what this run writes.
            os.remove(sb.rec_path(gtf))
            code = cmd_run(sb, stage, mutate=lambda o: edit_both(o, gtf, edit))
            return code == 1 and pre_outcome(sb, stage, "CC-EXACT") == "fail" and pre_outcome(sb, stage, "PR-S0") == "fail" and not sb.has_rec(gtf)
        if mu == "MU-13":
            target = "members.json" if stage == "members" else gtf
            with open(sb.rec_path(target), "wb") as fh:
                fh.write(flip_digit(ctx.read_rec(target)))
            rep = check_stage(sb, stage)
            return rep["status"] == 1 and rep["stages"][stage]["replay"]["REPLAY-" + target] is False
        if mu in ("MU-14a", "MU-14b", "MU-14c", "MU-14d"):
            cid = "PRE-INPUTS" if mu == "MU-14d" else "PRE-PREV"
            if subprocess_controls_run(sb, "rows") != 0 or pre_outcome(sb, "rows", cid) != "pass":
                return False
            sha = committed_members_sha(sb)
            if mu == "MU-14c":
                sb = sandbox_copy(ctx, os.path.join(tmp, "repo-c"), skip=(REC_REL + "/members.json",))
            elif mu == "MU-14a":
                os.remove(sb.rec_path("members.json"))
            elif mu == "MU-14b":
                with open(sb.rec_path("members.json"), "wb") as fh:
                    fh.write(flip_digit(ctx.read_rec("members.json")))
            else:
                cd = loads(sb.read_rec("class-decisions.json"))
                cd["g1"] = "undecided" if cd["g1"] == "pass" else "pass"
                with open(sb.rec_path("class-decisions.json"), "wb") as fh:
                    fh.write(dumps(cd))
            if mu in ("MU-14a", "MU-14b"):
                for which in ("A", "B"):
                    with tempfile.TemporaryDirectory() as out:
                        if run_impl(sb, which, "rows", out, sha) != 2 or output_snapshot(out) != flat_output_snapshot({}):
                            return False
            return subprocess_controls_run(sb, "rows") == 2 and pre_outcome(sb, "rows", cid) == "refused"
        if mu in ("MU-11", "MU-16c"):
            keys = g5_keys(sb)
            if not keys:
                print(mu + " not applicable: committed gate-table.rows.json has no G5 row")
                return True
            branch, key = keys[0]
            adv = loads(sb.read_rec("adversarial.json"))
            entry = next(e for e in adv["rows"] if (e["branch"], e["member"]) == (branch, key))
            if mu == "MU-11":
                entry["token"] = "BLIND[" + member_name(key) + "; " + branch + "; " + ", ".join(ACCESS[branch]) + "]"
            else:
                del entry["note"]
            with open(sb.rec_path("adversarial.json"), "wb") as fh:
                fh.write(dumps(adv))
            for which in ("A", "B"):
                with tempfile.TemporaryDirectory() as out:
                    code = run_impl(sb, which, "final", out, committed_members_sha(sb))
                    if mu == "MU-16c":
                        if code != 2 or output_snapshot(out) != flat_output_snapshot({}):
                            return False
                    else:
                        if code != 0:
                            return False
                        result = loads(read_dir(out)["gate-table.json"])
                        row = next(r for r in result["rows"] if (r["branch"], r["member"]) == (branch, key))
                        if row["gates"]["G6"] != "UNDECIDED(G6)" or row["token"] != "UNDECIDED(G6)":
                            return False
            return True
        if mu in ("MU-16a", "MU-16b"):
            cd = loads(sb.read_rec("class-decisions.json"))
            cd["extra" if mu == "MU-16a" else "version"] = True
            with open(sb.rec_path("class-decisions.json"), "wb") as fh:
                fh.write(dumps(cd))
            checks, outputs, codes, _ = execute_stage(sb, stage, committed_members_sha(sb))
            doc = checks_doc(stage, checks, outputs, codes)
            return doc["exit_status"] == {"A": 2, "B": 2} and not any(outputs.values())
        if mu == "MU-17":
            def edit(d):
                row = next(r for r in d["rows"] if r["member"] == DELTA0)
                row["gates"]["G4"] = row["gates"]["G5"] = "pass"
                row["gates"]["G6"] = row["gates"]["G7"] = row["token"] = "pending"
            return outcome(chk(lambda o: edit_both(o, gtf, edit)), stage, "PR-CR6") == "fail"
        if mu in ("MU-15a", "MU-15b", "MU-15c", "MU-15d"):
            if mu == "MU-15d":
                reason, fragment = render_from_record(sb)
                if reason != "OK" or not marker_matches(sb.read_rec("result.md"), fragment):
                    return False
                changed = fragment.replace(b"B-pl", b"B-pk", 1)
                with open(sb.rec_path("result.md"), "wb") as fh:
                    fh.write(ctx.read_rec("result.md").replace(fragment, changed, 1))
                rep = check_stage(sb, "final")
                return rep["status"] == 1 and rep["render"] is False
            if mu == "MU-15c":
                os.remove(sb.rec_path("gate-table.json"))
            else:
                name = "checks.members.json" if mu == "MU-15a" else "checks.json"
                doc = loads(sb.read_rec(name))
                if mu == "MU-15a":
                    doc["members_sha256"] = "0" * 64
                else:
                    doc["checks"][0]["outcome"] = "fail"
                with open(sb.rec_path(name), "wb") as fh:
                    fh.write(dumps(doc))
            with tempfile.TemporaryDirectory() as out:
                code = cmd_render(sb, out)
                status = loads(read_dir(out)["render-status.json"])
                reason = {"MU-15a": "INPUT_MISMATCH", "MU-15b": "CONTROL_NOT_GREEN", "MU-15c": "MISSING_INPUT"}[mu]
                return code == 2 and status["outcome"] == "refused" and status["reason"] == reason and output_snapshot(out) == flat_output_snapshot({"render-status.json": dumps(status)})
        if mu in ("MU-C1", "MU-C2", "MU-C3"):
            which = "B" if mu == "MU-C2" else "A"
            source_path = os.path.join(sb.root, *IMPL[which].split("/"))
            with open(source_path, "rb") as fh:
                data = splice_patch(fh.read(), patches[mu], IMPL[which])
            with open(source_path, "wb") as fh:
                fh.write(data)
            checks, outputs, codes, _ = execute_stage(sb, stage, None if stage == "members" else committed_members_sha(sb))
            doc = checks_doc(stage, checks, outputs, codes)
            if mu == "MU-C3":
                return doc["exit_status"]["A"] == 3
            cid = "PR-E" if mu == "MU-C1" else "CC-BIJ"
            return any(c["id"] == cid and c["outcome"] == "fail" for c in doc["checks"])
    raise ValueError("unknown mutation " + mu)


def cmd_self_test_stage(ctx, stage):
    _, patches = pinned_self_inputs(ctx)
    for mu in mutations_for(stage):
        # A fresh unmutated paired control for every mutation, never a single shared baseline.
        if check_stage(ctx, stage)["status"] != 0:
            print(mu + ": paired unmutated control fails")
            return 1
        try:
            ok = apply_mutation(ctx, stage, mu, patches)
        except (OSError, ValueError, KeyError, TypeError, Refusal) as exc:
            print(mu + ": " + type(exc).__name__)
            ok = False
        print(mu + " " + ("detected" if ok else "NOT detected"))
        if not ok:
            return 1
    return 0


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

USAGE = ("usage: controls.py run --stage {members|rows|final}\n"
         "       controls.py check [--stage {members|rows|final}]\n"
         "       controls.py self-test {--synthetic | --stage {members|rows|final}}\n"
         "       controls.py render --out <fresh-empty-directory>\n")


def parse_stage(args):
    if len(args) == 2 and args[0] == "--stage" and args[1] in STAGES:
        return args[1]
    raise Refusal("bad arguments\n" + USAGE)


def main(argv):
    try:
        if not argv:
            raise Refusal(USAGE)
        cmd, rest = argv[0], argv[1:]
        ctx = ctx_from_file()
        if cmd == "self-test" and rest == ["--synthetic"]:
            try:
                return cmd_self_test_synthetic(ctx)
            except Refusal:
                raise
            except (OSError, ValueError, KeyError, IndexError, TypeError, UnicodeError) as exc:
                sys.stderr.write("synthetic failure: " + type(exc).__name__ + "\n")
                return 1
        if cmd == "run":
            return cmd_run(ctx, parse_stage(rest))
        if cmd == "check":
            return cmd_check(ctx, parse_stage(rest) if rest else None)
        if cmd == "self-test":
            return cmd_self_test_stage(ctx, parse_stage(rest))
        if cmd == "render" and len(rest) == 2 and rest[0] == "--out":
            return cmd_render(ctx, rest[1])
        raise Refusal(USAGE)
    except Refusal as exc:
        sys.stderr.write("refused: " + str(exc) + "\n")
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
