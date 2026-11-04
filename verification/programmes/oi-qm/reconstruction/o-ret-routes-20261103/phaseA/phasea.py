#!/usr/bin/env python3
"""O-RET Phase A: exact replay of the pulse-design controls.

Implements PREREG-PHASE-A.md (frozen at F, together with DESIGN-PULSE.md, PHASEA-TUPLES.json and
PHASEA-EXPECTED.json in the parent directory). Standard library only. Every probability is a
fractions.Fraction built from exact integer counts or exact rational weights; a float anywhere in the
verdict path is a schema violation (exit 2).

Modes
  --verify-inputs        hash-check the four frozen inputs against their git blob ids at F (exit 0 or 3)
  --run --out DIR        the preregistered run: DIR/phase-a/<tuple_id>.json and DIR/phase-a/summary.json
  --check-summary DIR    regenerate verdict_text from summary.json, re-apply section 4 to every per-tuple
                         record and check the halt bookkeeping; writes DIR/phase-a/check.json
  --self-test            synthetic cases only; no frozen tuple is evaluated

Exit codes of --run (PREREG section 5)
  0 all tuples match; 1 row or value mismatch; 2 schema violation or floating-point value;
  3 frozen input does not match its git blob id at F, or F is not in the checkout;
  4 G* undetermined at step 6; 5 enumeration-method check failed;
  other nonzero: error (6 re-application of section 4 disagrees, 7 internal error).
"""

import argparse
import hashlib
import itertools
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from fractions import Fraction

# ----------------------------------------------------------------------------------------------
# Frozen constants
# ----------------------------------------------------------------------------------------------

F_COMMIT = "49f0bd41c5323d2191b580460c8703740dd01b30"
PKG = "verification/programmes/oi-qm/reconstruction/o-ret-routes-20261103"
FROZEN_NAMES = ("PREREG-PHASE-A.md", "DESIGN-PULSE.md", "PHASEA-TUPLES.json", "PHASEA-EXPECTED.json")
FROZEN_PATHS = tuple(PKG + "/" + name for name in FROZEN_NAMES)
TUPLES_PATH = PKG + "/PHASEA-TUPLES.json"
EXPECTED_PATH = PKG + "/PHASEA-EXPECTED.json"

EPS_STAR = Fraction(1, 20)
TUPLES_FROZEN = 49
FULL_MAX_BITS = 16
RECORD_SCHEMA = "oret-phase-a/1"
SUMMARY_SCHEMA = "oret-phase-a-summary/1"
TUPLES_SCHEMA = "oret-phase-a-tuples/1"
EXPECTED_SCHEMA = "oret-phase-a-expected/1"
INF = "inf"
CLOCK_DECODER = False  # PREREG section 4 step 5: a declared constant in Phase A
RAT_RE = re.compile(r"^(0|[1-9][0-9]*)(/[1-9][0-9]*)?$")
ROW_CODES = ("1", "2a", "2b", "3", "4", "5", "6", "7", "8", "I-3", "I-9")
PROB_MAP_FIELDS = ("eps_max", "tv", "eta", "lemma_h_bound")
PROB_SCALAR_FIELDS = ("write_min_eps", "w", "w_chg", "sweep_min_max_eps")
KNOWN_FIELDS = (
    "row", "eps_max", "tv", "Ra", "Rb", "dil_exact_T", "tau", "T_prime", "J1", "SCH",
    "Q_missing_T", "G_star_out_T", "G_status_T", "Q_missing_Tprime", "G_star_out_Tprime",
    "G_status_Tprime", "eta", "lemma_h_bound", "recurrence_flags", "D_bits", "method", "g",
    "write_min_eps", "w", "w_chg", "sweep_min_max_eps",
)
FIXED_STRINGS = {
    "eps_star": "1/20",
    "kappa": "sigma",
    "independence_law": "mu_t(.|sigma in P)",
    "support_conditioning": "mu_t(.|sigma in P)",
    "B_def": "Par(A)\\A on S",
    "rd_test": "J-1, Q7-narrowed",
    "access": "H-cur (declared)",
}
EXIT_REAPPLY = 6
EXIT_INTERNAL = 7


# ----------------------------------------------------------------------------------------------
# Halts and the exactness guard
# ----------------------------------------------------------------------------------------------

class Halt(Exception):
    """A halt of the run with a PREREG section 5 exit code."""

    def __init__(self, code, field=None, detail=None, expected=None, computed=None, tuple_id=None):
        super().__init__("exit %s: field=%s detail=%s" % (code, field, detail))
        self.code = code
        self.field = field
        self.detail = detail
        self.expected = expected
        self.computed = computed
        self.tuple_id = tuple_id
        self.frozen_inputs = None

    def failure(self):
        return {"exit": self.code, "tuple_id": self.tuple_id, "field": self.field,
                "expected": self.expected, "computed": self.computed, "detail": self.detail}


def exact(x, where):
    """Return x as a Fraction; anything but an int or a Fraction (a float above all) halts with exit 2."""
    if type(x) is Fraction:
        return x
    if type(x) is int:
        return Fraction(x)
    raise Halt(2, field=where, detail="inexact value of type %s in the verdict path" % type(x).__name__)


def gt_eps(x, where):
    return exact(x, where) > EPS_STAR


def rat(x, where):
    """Serialize a probability as a lowest-terms rational string (PREREG section 5 encodings)."""
    v = exact(x, where)
    if v < 0:  # a Lemma H bound may exceed 1; the regex admits every nonnegative rational
        raise Halt(2, field=where, detail="negative value")
    s = str(v)
    if not RAT_RE.match(s):
        raise Halt(2, field=where, detail="probability does not match the rational regex")
    return s


def parse_rat(s, where):
    if type(s) is not str or not RAT_RE.match(s):
        raise Halt(2, field=where, detail="not a rational string")
    v = Fraction(s)
    if str(v) != s:
        raise Halt(2, field=where, detail="rational not in lowest terms")
    return v


def no_float(obj, path):
    """Reject any value that is not a JSON type; floats above all (exit 2)."""
    if obj is None or type(obj) in (bool, int, str):
        return
    if type(obj) is dict:
        for k, v in obj.items():
            if type(k) is not str:
                raise Halt(2, field=path, detail="non-string key")
            no_float(v, path + "." + k)
        return
    if type(obj) is list:
        for i, v in enumerate(obj):
            no_float(v, "%s[%d]" % (path, i))
        return
    raise Halt(2, field=path, detail="value of type %s is not exact JSON" % type(obj).__name__)


def _reject_float(s):
    raise Halt(2, field="json", detail="floating-point literal %s" % s)


def _reject_constant(s):
    raise Halt(2, field="json", detail="non-finite literal %s" % s)


def _no_duplicates(pairs):
    out = {}
    for k, v in pairs:
        if k in out:
            raise Halt(2, field=k, detail="duplicate JSON key")
        out[k] = v
    return out


def load_json_bytes(data, where):
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        raise Halt(2, field=where, detail="not UTF-8")
    try:
        return json.loads(text, parse_float=_reject_float, parse_constant=_reject_constant,
                          object_pairs_hook=_no_duplicates)
    except json.JSONDecodeError:
        raise Halt(2, field=where, detail="invalid JSON")


def dumps_canonical(v):
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


# ----------------------------------------------------------------------------------------------
# Git and the frozen-input check (PREREG section 5, "F and the frozen-input check")
# ----------------------------------------------------------------------------------------------

def git_run(repo, args):
    p = subprocess.run(["git", "-C", repo] + list(args), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout.decode("utf-8", "replace").strip()


def blob_id(data):
    """The git blob id (SHA-1 object format) of exactly these bytes."""
    return hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()


def repo_root(git=git_run):
    here = os.path.dirname(os.path.abspath(__file__))
    rc, out = git(here, ["rev-parse", "--show-toplevel"])
    if rc != 0 or not out:
        raise Halt(3, detail="the tool is not inside a git checkout")
    return out


def check_frozen_inputs(repo, F=F_COMMIT, git=git_run, read=None):
    """Compare each frozen file's blob id at F with the blob id of the bytes loaded. Returns
    (frozen_inputs, {path: bytes}); the bytes returned are the bytes hashed. Exit 3 on any failure."""
    if read is None:
        def read(path):
            with open(os.path.join(repo, path), "rb") as fh:
                return fh.read()
    meta = []
    rc, _ = git(repo, ["cat-file", "-e", F + "^{commit}"])
    if rc != 0:
        h = Halt(3, detail="F %s (absent from the checkout)" % F)
        h.frozen_inputs = meta
        raise h
    rc, out = git(repo, ["log", "--format=%H", "HEAD"])
    if rc != 0 or F not in out.split():
        h = Halt(3, detail="F %s (not in the history of HEAD)" % F)
        h.frozen_inputs = meta
        raise h
    data = {}
    for path in FROZEN_PATHS:
        rc, at_f = git(repo, ["rev-parse", "--verify", "--quiet", F + ":" + path])
        if rc != 0 or not re.fullmatch(r"[0-9a-f]{40}", at_f):
            h = Halt(3, detail=path + " (absent at F)")
            h.frozen_inputs = meta
            raise h
        try:
            b = read(path)
        except OSError:
            meta.append({"path": path, "blob_at_F": at_f, "blob_read": None})
            h = Halt(3, detail=path + " (unreadable)")
            h.frozen_inputs = meta
            raise h
        bid = blob_id(b)
        meta.append({"path": path, "blob_at_F": at_f, "blob_read": bid})
        if bid != at_f:
            h = Halt(3, detail=path)
            h.frozen_inputs = meta
            raise h
        data[path] = b
    return meta, data


def run_info(repo, git=git_run):
    rc, head = git(repo, ["rev-parse", "HEAD"])
    att = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    return {"F": F_COMMIT, "commit": head if rc == 0 else None,
            "run_attempt": int(att) if att.isdigit() else None}


# ----------------------------------------------------------------------------------------------
# Index templates and the expression grammar (PHASEA-TUPLES.json conventions)
# ----------------------------------------------------------------------------------------------

_ATOK = re.compile(r"\s*(?:(\d+)|(mod)\b|([A-Za-z_][A-Za-z0-9_]*)|([-+()]))")


def arith(text, env, where):
    """Integer index arithmetic: integers, names, + and -, parentheses, and 'mod' (lowest precedence)."""
    toks, pos = [], 0
    text = text.strip()
    while pos < len(text):
        m = _ATOK.match(text, pos)
        if not m or m.end() == pos:
            raise Halt(2, field=where, detail="cannot parse index expression %r" % text)
        pos = m.end()
        if m.group(1):
            toks.append(("int", int(m.group(1))))
        elif m.group(2):
            toks.append(("op", "mod"))
        elif m.group(3):
            toks.append(("name", m.group(3)))
        else:
            toks.append(("op", m.group(4)))
    i = [0]

    def peek():
        return toks[i[0]] if i[0] < len(toks) else (None, None)

    def take():
        t = peek()
        i[0] += 1
        return t

    def atom():
        k, v = take()
        if k == "int":
            return v
        if k == "name":
            if v not in env or type(env[v]) is not int:
                raise Halt(2, field=where, detail="unknown index name %r" % v)
            return env[v]
        if (k, v) == ("op", "("):
            r = mexpr()
            if take() != ("op", ")"):
                raise Halt(2, field=where, detail="unbalanced parentheses in %r" % text)
            return r
        raise Halt(2, field=where, detail="bad index expression %r" % text)

    def add():
        r = atom()
        while peek() in (("op", "+"), ("op", "-")):
            _, o = take()
            r = r + atom() if o == "+" else r - atom()
        return r

    def mexpr():
        r = add()
        if peek() == ("op", "mod"):
            take()
            b = add()
            if b <= 0:
                raise Halt(2, field=where, detail="nonpositive modulus")
            r = r % b
        return r

    r = mexpr()
    if i[0] != len(toks):
        raise Halt(2, field=where, detail="trailing tokens in %r" % text)
    return r


def subst(text, env, where):
    out = re.sub(r"\{([^{}]*)\}", lambda m: str(arith(m.group(1), env, where)), text)
    if "{" in out or "}" in out:
        raise Halt(2, field=where, detail="unbalanced braces in %r" % text)
    return out


_CONJ = re.compile(r"([A-Za-z_][A-Za-z0-9]*)_1\s*&\s*\.\.\s*&\s*\1_k")


def expand_conj(text, env, where):
    """'x_1 & .. & x_k' is the conjunction of x_i over i = 1 .. k; for k = 1 it is x_1."""
    def rep(m):
        k = env.get("k")
        if type(k) is not int or k < 1:
            raise Halt(2, field=where, detail="conjunction template without a positive k")
        return "(" + " & ".join("%s_%d" % (m.group(1), j) for j in range(1, k + 1)) + ")"
    out = _CONJ.sub(rep, text)
    if ".." in out:
        raise Halt(2, field=where, detail="unexpanded '..' in %r" % text)
    return out


def parse_ranges(spec, env, where):
    out = []
    for part in spec.split(","):
        m = re.fullmatch(r"\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+?)\s*\.\.\s*(.+?)\s*", part)
        if not m:
            raise Halt(2, field=where, detail="cannot parse range %r" % spec)
        name = m.group(1)
        if name in env:
            raise Halt(2, field=where, detail="range variable %r shadows a parameter" % name)
        out.append((name, list(range(arith(m.group(2), env, where), arith(m.group(3), env, where) + 1))))
    return out


_ETOK = re.compile(r"\s*(?:(ite)(?=\s*\()|([A-Za-z_][A-Za-z0-9_]*)|([01])(?![A-Za-z0-9_])|(\^|&|\(|\)|,))")


def parse_expr(text, index, where):
    """Grammar: cell names; 0; 1; a ^ b; a & b; ite(c, a, b); parentheses. A chain mixing ^ and &
    without parentheses has no stated precedence and is rejected (exit 2)."""
    toks, pos = [], 0
    text = text.strip()
    while pos < len(text):
        m = _ETOK.match(text, pos)
        if not m or m.end() == pos:
            raise Halt(2, field=where, detail="cannot parse expression %r" % text)
        pos = m.end()
        if m.group(1):
            toks.append(("ite", None))
        elif m.group(2):
            toks.append(("name", m.group(2)))
        elif m.group(3):
            toks.append(("const", int(m.group(3))))
        else:
            toks.append(("op", m.group(4)))
    i = [0]

    def peek():
        return toks[i[0]] if i[0] < len(toks) else (None, None)

    def take():
        t = peek()
        i[0] += 1
        return t

    def expect(op):
        if take() != ("op", op):
            raise Halt(2, field=where, detail="expected %r in %r" % (op, text))

    def operand():
        k, v = take()
        if k == "ite":
            expect("(")
            c = expr()
            expect(",")
            a = expr()
            expect(",")
            b = expr()
            expect(")")
            return ("ite", c, a, b)
        if k == "name":
            if v not in index:
                raise Halt(2, field=where, detail="unknown cell %r in %r" % (v, text))
            return ("var", index[v])
        if k == "const":
            return ("const", v)
        if (k, v) == ("op", "("):
            e = expr()
            expect(")")
            return e
        raise Halt(2, field=where, detail="bad operand in %r" % text)

    def expr():
        terms, op = [operand()], None
        while peek() in (("op", "^"), ("op", "&")):
            _, o = take()
            if op is None:
                op = o
            elif op != o:
                raise Halt(2, field=where, detail="^ and & mixed without parentheses in %r" % text)
            terms.append(operand())
        if op is None:
            return terms[0]
        return ("xor" if op == "^" else "and", terms)

    e = expr()
    if i[0] != len(toks):
        raise Halt(2, field=where, detail="trailing tokens in %r" % text)
    return e


def compile_expr(node):
    kind = node[0]
    if kind == "var":
        i = node[1]
        return lambda s: (s >> i) & 1
    if kind == "const":
        v = node[1]
        return lambda s: v
    if kind == "xor":
        fs = [compile_expr(x) for x in node[1]]

        def fx(s):
            r = 0
            for h in fs:
                r ^= h(s)
            return r
        return fx
    if kind == "and":
        fs = [compile_expr(x) for x in node[1]]

        def fa(s):
            for h in fs:
                if not h(s):
                    return 0
            return 1
        return fa
    if kind == "ite":
        c, a, b = (compile_expr(x) for x in node[1:])
        return lambda s: a(s) if c(s) else b(s)
    raise Halt(EXIT_INTERNAL, detail="unknown expression node")


def expr_cells(node):
    if node[0] == "var":
        return {node[1]}
    if node[0] == "const":
        return set()
    if node[0] in ("xor", "and"):
        return set().union(*(expr_cells(x) for x in node[1]))
    return expr_cells(node[1]) | expr_cells(node[2]) | expr_cells(node[3])


# ----------------------------------------------------------------------------------------------
# Models
# ----------------------------------------------------------------------------------------------

def _need(env, name, where):
    v = env.get(name)
    if type(v) is not int or v < 1:
        raise Halt(2, field=where, detail="parameter %s missing or not a positive integer" % name)
    return v


def _check_eq(cond, where, what):
    if not cond:
        raise Halt(2, field=where, detail="parameter constraint %s fails" % what)


def _cells_ring(env, where):
    return ["u%d" % j for j in range(_need(env, "L", where))]


def _cells_closed_ring(env, where):
    _check_eq(_need(env, "L", where) == _need(env, "m", where) + 3, where, "L = m+3")
    return _cells_ring(env, where)


def _cells_channel(env, where):
    return [c for j in range(_need(env, "L", where)) for c in ("p%d" % j, "v%d" % j)] + ["r"]


def _cells_pair(env, where):
    _check_eq(_need(env, "L", where) == 3, where, "L = 3")
    return ["p0", "v0", "p1", "v1", "p2", "v2", "r1", "r2"]


def _cells_trigger(env, where):
    L, k = _need(env, "L", where), _need(env, "k", where)
    _check_eq(L == _need(env, "T", where) + 1, where, "L = T+1")
    return [c for j in range(L) for c in ["p%d_%d" % (j, i) for i in range(1, k + 1)] + ["v%d" % j]] + ["r"]


# The cell lists of PHASEA-TUPLES.json are prose; each recognized description maps to one constructor.
CELL_SPECS = {
    "u0 .. u{L-1}": _cells_ring,
    "u0 .. u{L-1}, with L = m+3": _cells_closed_ring,
    "a, z0, z1, z2": lambda env, where: ["a", "z0", "z1", "z2"],
    "p0, v0, p1, v1, .., p{L-1}, v{L-1}, r": _cells_channel,
    "p0, v0, p1, v1, p2, v2, r1, r2 (L = 3)": _cells_pair,
    "for j = 0 .. L-1: p{j}_1, .., p{j}_k, v{j}; then r (L = T+1)": _cells_trigger,
    "c, w0, w1, w2, w3": lambda env, where: ["c", "w0", "w1", "w2", "w3"],
    "r, s, y0, y1, z0, z1": lambda env, where: ["r", "s", "y0", "y1", "z0", "z1"],
}


class Model:
    """A finite product of F2 cells and a rule of steps; within a step every assignment is
    simultaneous (it reads the state before the step); an unassigned cell keeps its value.
    A state is an int whose bit i is the cell with index i in the model's cell order."""

    def __init__(self, mdef, env, where):
        if type(mdef) is not dict or set(mdef) - {"cells", "rule", "source"} or "rule" not in mdef:
            raise Halt(2, field=where, detail="model keys")
        cells = mdef.get("cells")
        if type(cells) is list:
            self.cells = list(cells)
        elif type(cells) is str and cells in CELL_SPECS:
            self.cells = CELL_SPECS[cells](env, where + ".cells")
        else:
            raise Halt(2, field=where + ".cells", detail="unrecognized cell specification")
        if (len(set(self.cells)) != len(self.cells) or not self.cells
                or not all(type(c) is str and re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", c) for c in self.cells)):
            raise Halt(2, field=where + ".cells", detail="cell names")
        self.index = {c: i for i, c in enumerate(self.cells)}
        self.n = len(self.cells)
        self.steps = []
        if type(mdef["rule"]) is not list:
            raise Halt(2, field=where + ".rule", detail="rule is not a list of steps")
        for si, step in enumerate(mdef["rule"]):
            sw = "%s.rule[%d]" % (where, si)
            if type(step) is not list:
                raise Halt(2, field=sw, detail="step is not a list")
            assigns, seen = [], set()
            for a in step:
                if type(a) is not dict or set(a) - {"lhs", "rhs", "range"} or not {"lhs", "rhs"} <= set(a):
                    raise Halt(2, field=sw, detail="assignment keys")
                combos = [{}]
                if "range" in a:
                    ranges = parse_ranges(a["range"], env, sw)
                    combos = [dict(zip([r[0] for r in ranges], vals))
                              for vals in itertools.product(*[r[1] for r in ranges])]
                for combo in combos:
                    e = dict(env)
                    e.update(combo)
                    lhs = subst(a["lhs"], e, sw)
                    rhs = expand_conj(subst(a["rhs"], e, sw), e, sw)
                    if lhs not in self.index:
                        raise Halt(2, field=sw, detail="assignment to unknown cell %r" % lhs)
                    li = self.index[lhs]
                    if li in seen:
                        raise Halt(2, field=sw, detail="cell %r assigned twice in one step" % lhs)
                    seen.add(li)
                    node = parse_expr(rhs, self.index, sw)
                    bare = node[1] if node[0] == "var" else None
                    assigns.append((li, compile_expr(node), frozenset(expr_cells(node)), bare))
            self.steps.append(assigns)
        self.step_fns = [self._mk_step(a) for a in self.steps]

    def _mk_step(self, assigns):
        keep = ((1 << self.n) - 1) & ~sum(1 << li for li, _, _, _ in assigns)
        pairs = [(li, fn) for li, fn, _, _ in assigns]

        def step(s):
            new = s & keep
            for li, fn in pairs:
                new |= fn(s) << li
            return new
        return step

    def phi(self, s):
        for f in self.step_fns:
            s = f(s)
        return s

    def syntactic_deps(self, deps):
        """One application of phi to per-cell dependency sets (syntactic superset)."""
        for assigns in self.steps:
            new = list(deps)
            for li, _, rc, _ in assigns:
                new[li] = frozenset().union(*[deps[x] for x in rc]) if rc else frozenset()
            deps = new
        return deps

    def provenance_step(self, deps, orig):
        """As syntactic_deps, also tracking whether a cell is an unmodified copy of a t0 cell."""
        for assigns in self.steps:
            nd, no = list(deps), list(orig)
            for li, _, rc, bare in assigns:
                nd[li] = frozenset().union(*[deps[x] for x in rc]) if rc else frozenset()
                no[li] = orig[bare] if bare is not None else None
            deps, orig = nd, no
        return deps, orig


def proj(s, idxs):
    return "".join("1" if (s >> i) & 1 else "0" for i in idxs)


def place(cfg, idxs):
    s = 0
    for ch, i in zip(cfg, idxs):
        if ch == "1":
            s |= 1 << i
    return s


def all_cfgs(m):
    return ["".join(b) for b in itertools.product("01", repeat=m)]


# ----------------------------------------------------------------------------------------------
# Laws
# ----------------------------------------------------------------------------------------------

def _law_eqs(law, model, where):
    eqs = law.get("equalities")
    if type(eqs) is not dict or not eqs:
        raise Halt(2, field=where, detail="equalities")
    out = {}
    for c, v in eqs.items():
        if c not in model.index or type(v) is not int or v not in (0, 1):
            raise Halt(2, field=where, detail="equality %r" % c)
        out[model.index[c]] = v
    return out


def _law_states(law, model, where):
    st = law.get("states")
    if type(st) is not dict or not st:
        raise Halt(2, field=where, detail="states")
    out = {}
    for cfg, p in st.items():
        if type(cfg) is not str or len(cfg) != model.n or set(cfg) - {"0", "1"}:
            raise Halt(2, field=where, detail="state %r" % cfg)
        out[place(cfg, range(model.n))] = parse_rat(p, where + "." + cfg)
    if sum(out.values()) != 1:
        raise Halt(2, field=where, detail="explicit law does not sum to 1")
    return out


def validate_law(law, model, where):
    if type(law) is not dict or law.get("type") not in ("uniform", "uniform_conditioned", "explicit"):
        raise Halt(2, field=where, detail="law type")
    allowed = {"uniform": {"type"}, "uniform_conditioned": {"type", "equalities"},
               "explicit": {"type", "states"}}[law["type"]]
    if set(law) != allowed:
        raise Halt(2, field=where, detail="law keys")
    if law["type"] == "uniform_conditioned":
        _law_eqs(law, model, where)
    if law["type"] == "explicit":
        _law_states(law, model, where)


def law_support(law, model, where):
    """[(state, integer weight)] over the support of mu at t0, and the total weight."""
    n, t = model.n, law["type"]
    if t == "uniform":
        sup = [(s, 1) for s in range(1 << n)]
    elif t == "uniform_conditioned":
        eqs = _law_eqs(law, model, where)
        mask = sum(1 << i for i in eqs)
        val = sum(v << i for i, v in eqs.items())
        sup = [(s, 1) for s in range(1 << n) if s & mask == val]
    else:
        st = _law_states(law, model, where)
        den = math.lcm(*[p.denominator for p in st.values()])
        sup = [(s, int(p * den)) for s, p in sorted(st.items()) if p > 0]
    if not sup:
        raise Halt(2, field=where, detail="empty support")
    return sup, sum(w for _, w in sup)


def law_multiset(law, model, where):
    """{probability: number of states} for mu at t0, without enumeration."""
    n, t = model.n, law["type"]
    if t == "uniform":
        return {Fraction(1, 1 << n): 1 << n}
    if t == "uniform_conditioned":
        e = len(_law_eqs(law, model, where))
        return {Fraction(1, 1 << (n - e)): 1 << (n - e)}
    out = {}
    for p in _law_states(law, model, where).values():
        if p > 0:
            out[p] = out.get(p, 0) + 1
    return out


def d_bits(law, model, where):
    """D = log2|S| - H(mu) at t0 as an integer, or None when D is not an integer. Decided exactly:
    with e_v = c_v * v * M integer, H is an integer h iff prod (1/v)^(e_v) = 2^(h*M)."""
    ms = law_multiset(law, model, where)
    ex = {v: Fraction(c) * v for v, c in ms.items()}
    M = math.lcm(*[e.denominator for e in ex.values()])
    X = Fraction(1)
    for v, e in ex.items():
        X *= (1 / v) ** int(e * M)
    if X.denominator != 1:
        return None
    num = X.numerator
    if num & (num - 1):
        return None
    e2 = num.bit_length() - 1
    if e2 % M:
        return None
    return model.n - e2 // M


def product_marginals(law, model, where):
    """Per-cell marginals of mu at t0, which the sequential method requires to be a product over
    cells (exit 5 otherwise)."""
    n, t = model.n, law["type"]
    half = Fraction(1, 2)
    if t == "uniform":
        return [{0: half, 1: half} for _ in range(n)]
    if t == "uniform_conditioned":
        eqs = _law_eqs(law, model, where)
        return [({eqs[i]: Fraction(1)} if i in eqs else {0: half, 1: half}) for i in range(n)]
    st = {s: p for s, p in _law_states(law, model, where).items() if p > 0}
    marg = [{0: Fraction(0), 1: Fraction(0)} for _ in range(n)]
    for s, p in st.items():
        for i in range(n):
            marg[i][(s >> i) & 1] += p
    marg = [{b: p for b, p in m.items() if p > 0} for m in marg]
    free = [i for i in range(n) if len(marg[i]) == 2]
    if len(free) > FULL_MAX_BITS:
        raise Halt(5, field="law", detail="explicit law too large to verify as a product over cells")
    base = sum(1 << i for i in range(n) if 1 in marg[i] and len(marg[i]) == 1)
    count = 0
    for bits in itertools.product((0, 1), repeat=len(free)):
        s = base | sum(b << i for b, i in zip(bits, free))
        p = Fraction(1)
        for i in range(n):
            p *= marg[i][(s >> i) & 1]
        if st.get(s, Fraction(0)) != p:
            raise Halt(5, field="law", detail="law at t0 is not a product over cells")
        count += 1
    if count != len(st):
        raise Halt(5, field="law", detail="law at t0 is not a product over cells")
    return marg


# ----------------------------------------------------------------------------------------------
# A tuple's context
# ----------------------------------------------------------------------------------------------

def parse_tick(label, where):
    m = re.fullmatch(r"t0\+([1-9][0-9]*)", label) if type(label) is str else None
    if not m:
        raise Halt(2, field=where, detail="tick label %r" % (label,))
    return int(m.group(1))


def tick(n):
    return "t0+%d" % n


class TupleCtx:
    KEYS = {"order", "id", "model", "params", "mode", "T", "Sigma", "P", "f", "law", "A", "read_cells",
            "g", "method"}

    def __init__(self, tup, models):
        where = "tuple"
        if type(tup) is not dict:
            raise Halt(2, field=where, detail="tuple is not an object")
        self.id = tup.get("id")
        where = "tuple " + str(self.id)
        keys = set(tup)
        if keys - self.KEYS - {"readback_ticks"} or not self.KEYS <= keys:
            raise Halt(2, field=where, detail="tuple keys")
        self.tup = tup
        self.mode = tup["mode"]
        if self.mode not in ("window", "noext", "readback"):
            raise Halt(2, field="mode", detail="unknown mode")
        if (self.mode == "readback") != ("readback_ticks" in tup):
            raise Halt(2, field="readback_ticks", detail="readback ticks iff readback mode")
        self.T = tup["T"]
        if self.mode == "readback":
            if self.T is not None:
                raise Halt(2, field="T", detail="readback tuples have T = null")
            rb = tup["readback_ticks"]
            if type(rb) is not list or not rb:
                raise Halt(2, field="readback_ticks", detail="not a list")
            self.readback = [parse_tick(x, "readback_ticks") for x in rb]
            if self.readback != sorted(set(self.readback)):
                raise Halt(2, field="readback_ticks", detail="not strictly increasing")
        elif type(self.T) is not int or self.T < 1:
            raise Halt(2, field="T", detail="T must be a positive integer")
        params = tup["params"]
        if type(params) is not dict or not all(type(v) is int for v in params.values()):
            raise Halt(2, field="params", detail="params must map names to integers")
        env = dict(params)
        if self.T is not None:
            if "T" in env and env["T"] != self.T:
                raise Halt(2, field="params", detail="params.T differs from T")
            env["T"] = self.T
        self.params = params
        if tup["model"] not in models:
            raise Halt(2, field="model", detail="unknown model %r" % tup["model"])
        self.model_name = tup["model"]
        self.model = Model(models[tup["model"]], env, "models." + tup["model"])
        m = self.model

        def idx_list(name):
            v = tup[name]
            if type(v) is not list or not v or not all(type(c) is str and c in m.index for c in v):
                raise Halt(2, field=name, detail="cell list")
            ix = [m.index[c] for c in v]
            if ix != sorted(set(ix)):
                raise Halt(2, field=name, detail="cells not distinct and in cell order")
            return ix
        self.Sigma = idx_list("Sigma")
        self.A = idx_list("A")
        self.read = idx_list("read_cells")
        if not set(self.read) <= set(self.A):
            raise Halt(2, field="read_cells", detail="read cells must lie in A")
        P, f = tup["P"], tup["f"]
        if (type(P) is not list or type(f) is not list or len(P) != len(f) or len(P) < 2
                or len(set(P)) != len(P)
                or not all(type(c) is str and len(c) == len(self.Sigma) and not set(c) - {"0", "1"} for c in P)
                or not all(type(v) is int and v in (0, 1) for v in f)):
            raise Halt(2, field="P", detail="P and f")
        self.P = list(P)
        self.Pset = set(P)
        self.fval = dict(zip(P, f))
        g = tup["g"]
        if type(g) is not str or len(g) != 1 << len(self.A) or set(g) - {"0", "1"}:
            raise Halt(2, field="g", detail="decoder truth table")
        self.g = g
        validate_law(tup["law"], m, "law")
        self.law = tup["law"]
        if tup["method"] not in ("full", "sequential", "full+sequential"):
            raise Halt(2, field="method", detail="unknown method")
        self.is_sk = self.model_name == "trigger-channel"
        self.is_mdxor = type(self.id) is str and self.id.startswith("MD-xor")

    def decode(self, cfg):
        return int(self.g[int(cfg, 2)])


def method_for(ctx):
    """PREREG section 2.0: full for |S| <= 2^16; HC-SK tuples with |S| <= 2^16 by both methods;
    sequential only for HC-SK tuples with |S| > 2^16."""
    n = ctx.model.n
    if ctx.is_sk:
        return "full+sequential" if n <= FULL_MAX_BITS else "sequential"
    if n > FULL_MAX_BITS:
        raise Halt(5, field="method", detail="no frozen method for a non-HC-SK tuple with |S| > 2^16")
    return "full"


# ----------------------------------------------------------------------------------------------
# Enumeration methods. Each supplies Par, Q (= Par(A) minus A, from phi on all of S), f_R and
# table(n, need_q): the exact law of (sigma, R_t, Q_t) at t = t0+n under mu (all sigma, unconditioned).
# ----------------------------------------------------------------------------------------------

def build_fR(phi, A, Q):
    out = {}
    for l in all_cfgs(len(A)):
        for q in all_cfgs(len(Q)):
            out[(l, q)] = proj(phi(place(l, A) | place(q, Q)), A)
    return out


class FullMethod:
    name = "full"

    def __init__(self, ctx):
        m = ctx.model
        n = m.n
        if n > FULL_MAX_BITS:
            raise Halt(5, field="method", detail="full enumeration of |S| = 2^%d" % n)
        size = 1 << n
        tab = [m.phi(s) for s in range(size)]
        self.injective = len(set(tab)) == size
        if not self.injective:
            raise Halt(5, field="injective", detail="phi is not injective on S")
        self.tab = tab
        self.par = {}
        for i in ctx.A:
            deps = set()
            for j in range(n):
                bj = 1 << j
                for s in range(size):
                    if not s & bj and ((tab[s] ^ tab[s | bj]) >> i) & 1:
                        deps.add(j)
                        break
            self.par[i] = deps
        parR = set().union(*self.par.values())
        self.Q = [c for c in range(n) if c in parR and c not in ctx.A]
        self.f_R = build_fR(lambda s: tab[s], ctx.A, self.Q)
        for s in range(size):  # f_R is the R-part of phi: check that it is well defined on all of S
            if proj(tab[s], ctx.A) != self.f_R[(proj(s, ctx.A), proj(s, self.Q))]:
                raise Halt(EXIT_INTERNAL, field="f_R", detail="R-part of phi does not factor through R and Q")
        sup, self.total = law_support(ctx.law, m, "law")
        self.w = [w for _, w in sup]
        self.sig = [proj(s, ctx.Sigma) for s, _ in sup]
        self.states = {0: [s for s, _ in sup]}
        self.A = ctx.A
        self.cache = {}

    def _at(self, n):
        k = max(self.states)
        while k < n:
            self.states[k + 1] = [self.tab[s] for s in self.states[k]]
            k += 1
        return self.states[n]

    def table(self, n, need_q):
        key = (n, need_q)
        if key not in self.cache:
            agg = {}
            for i, s in enumerate(self._at(n)):
                k = (self.sig[i], proj(s, self.A), proj(s, self.Q) if need_q else None)
                agg[k] = agg.get(k, 0) + self.w[i]
            self.cache[key] = {k: Fraction(v, self.total) for k, v in agg.items()}
        return self.cache[key]


def par_restricted(model, i):
    """Par(i) from phi on all of S, evaluated on the syntactic support of phi_i: phi_i is constant in
    every other cell, so the essential cells are found by enumerating that support alone."""
    deps = model.syntactic_deps([frozenset([c]) for c in range(model.n)])[i]
    cells = sorted(deps)
    if len(cells) > 20:
        raise Halt(5, field="Par", detail="syntactic support too large for the sequential method")
    out = set()
    for pj, j in enumerate(cells):
        for bits in range(1 << len(cells)):
            if (bits >> pj) & 1:
                continue
            s = sum(1 << c for k, c in enumerate(cells) if (bits >> k) & 1)
            if ((model.phi(s) ^ model.phi(s | (1 << j))) >> i) & 1:
                out.add(j)
                break
    return out


class SequentialMethod:
    """Exact sequential marginalization (PREREG section 2.0). The law of (sigma, R) is updated at each
    tick by the exact law of the arriving Q cells, which must be unmodified copies of t0 cells that
    are fresh (never in Sigma, A or Q before, and outside the dependency set of R) under a law that is
    a product over cells. Both conditions are checked from phi and the law; failure exits 5."""
    name = "sequential"

    def __init__(self, ctx):
        if ctx.mode == "readback":
            raise Halt(5, field="method", detail="the sequential method has no readback mode")
        m = ctx.model
        self.m = m
        self.A = ctx.A
        self.par = {i: par_restricted(m, i) for i in ctx.A}
        parR = set().union(*self.par.values())
        self.Q = [c for c in range(m.n) if c in parR and c not in ctx.A]
        self.f_R = build_fR(m.phi, ctx.A, self.Q)
        self.injective = None
        self.marg = product_marginals(ctx.law, m, "law")
        U = sorted(set(ctx.Sigma) | set(ctx.A) | set(self.Q))
        self.forbidden = set(ctx.Sigma) | set(U)
        t0 = {}
        for bits in itertools.product((0, 1), repeat=len(U)):
            p = Fraction(1)
            for b, c in zip(bits, U):
                p *= self.marg[c].get(b, Fraction(0))
            if p == 0:
                continue
            s = sum(b << c for b, c in zip(bits, U))
            k = (proj(s, ctx.Sigma), proj(s, ctx.A), proj(s, self.Q))
            t0[k] = t0.get(k, Fraction(0)) + p
        self.cache = {(0, True): t0}
        self.J = {}
        self.prov = [([frozenset([c]) for c in range(m.n)], list(range(m.n)))]
        self.checked = {}
        self.used = set()

    def _prov(self, n):
        while len(self.prov) <= n:
            self.prov.append(self.m.provenance_step(*self.prov[-1]))
        return self.prov[n]

    def _origins(self, n):
        """Check the sequential conditions at hold tick t0+n and return the t0 origins of Q_t."""
        if n in self.checked:
            return self.checked[n]
        for k in range(1, n):
            self._origins(k)
        deps, orig = self._prov(n)
        origins = [orig[c] for c in self.Q]
        if any(o is None for o in origins):
            raise Halt(5, field="sequential", detail="a cell of Q at %s is not an unmodified t0 cell" % tick(n))
        if len(set(origins)) != len(origins):
            raise Halt(5, field="sequential", detail="two cells of Q at %s share a t0 origin" % tick(n))
        rdeps = frozenset().union(*[deps[c] for c in self.A])
        bad = set(origins) & (self.forbidden | self.used | rdeps)
        if bad:
            raise Halt(5, field="sequential",
                       detail="cells %s enter Q at %s more than once or are not fresh"
                       % (",".join(self.m.cells[c] for c in sorted(bad)), tick(n)))
        self.used |= set(origins)
        self.checked[n] = origins
        return origins

    def _joint(self, n):
        if n not in self.J:
            J = {}
            for (sg, r, q), p in self.table(n - 1, True).items():
                k = (sg, self.f_R[(r, q)])
                J[k] = J.get(k, Fraction(0)) + p
            self.J[n] = J
        return self.J[n]

    def table(self, n, need_q):
        key = (n, need_q)
        if key in self.cache:
            return self.cache[key]
        if n == 0:
            out = {}
            for (sg, r, _), p in self.cache[(0, True)].items():
                out[(sg, r, None)] = out.get((sg, r, None), Fraction(0)) + p
        elif not need_q:
            out = {(sg, r, None): p for (sg, r), p in self._joint(n).items()}
        else:
            J = self._joint(n)
            origins = self._origins(n)
            qlaw = {}
            for bits in itertools.product((0, 1), repeat=len(origins)):
                p = Fraction(1)
                for b, o in zip(bits, origins):
                    p *= self.marg[o].get(b, Fraction(0))
                if p:
                    qlaw["".join(map(str, bits))] = p
            out = {(sg, r, q): p * pq for (sg, r), p in J.items() for q, pq in qlaw.items()}
        self.cache[key] = out
        return out


# ----------------------------------------------------------------------------------------------
# Exact criteria
# ----------------------------------------------------------------------------------------------

def indep(pairs):
    """x independent of y under the (unnormalized) joint table {(x, y): p}."""
    tot = sum(pairs.values())
    px, py = {}, {}
    for (x, y), p in pairs.items():
        px[x] = px.get(x, 0) + p
        py[y] = py.get(y, 0) + p
    for x, a in px.items():
        for y, b in py.items():
            if pairs.get((x, y), 0) * tot != a * b:
                return False
    return True


def cond_indep(triples):
    """x independent of y given z under {(z, x, y): p}."""
    by_z = {}
    for (z, x, y), p in triples.items():
        d = by_z.setdefault(z, {})
        d[(x, y)] = d.get((x, y), 0) + p
    return all(indep(d) for d in by_z.values())


def classes_of(G, cfgR, fR):
    parent = {l: l for l in cfgR}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for q in sorted(G):
        for l in cfgR:
            a, b = find(l), find(fR[(l, q)])
            if a != b:
                parent[max(a, b)] = min(a, b)
    groups = {}
    for l in cfgR:
        groups.setdefault(find(l), []).append(l)
    return sorted(sorted(v) for v in groups.values())


def consistent(classes, Lset, dec):
    return all(len({dec(l) for l in c if l in Lset}) <= 1 for c in classes)


def g_star(Qset, Lset, cfgR, fR, dec):
    """PREREG section 4, the G-rule: G*_W and G_status_W."""
    G = {q for q in Qset if consistent(classes_of({q}, cfgR, fR), Lset, dec)}
    if not G:
        return G, "empty"
    return G, ("consistent" if consistent(classes_of(G, cfgR, fR), Lset, dec) else "inconsistent")


def compute_tau(starts, Qset, Lset, fR, dec):
    """PREREG section 2.4: the least k >= 1 with a hit; 'inf' when the family repeats first."""
    starts = sorted(starts)
    fam = tuple(frozenset([l]) for l in starts)
    seen = {fam}
    k = 0
    while True:
        k += 1
        fam = tuple(frozenset(fR[(x, q)] for x in F for q in Qset) for F in fam)
        for l, F in zip(starts, fam):
            if any(lk in Lset and dec(lk) != dec(l) for lk in F):
                return k
        if fam in seen:
            return INF
        seen.add(fam)


def recurrence(ticks, eps):
    flags, failed = [], False
    for n in sorted(ticks):
        if gt_eps(eps[n], "eps_max"):
            failed = True
        elif failed:
            flags.append(n)
    return flags


def assign_row(mode, T, tau, J1, eps, Ra, Rb, dil, G_status_T, G_T_empty, G_Tp_empty, bound, sch):
    """PREREG section 4 steps 1-8 for window and noext tuples (step 0's readback case is handled by
    the caller). Returns (row, step, T_prime); exit 4 at step 6 only."""
    finite = tau != INF

    def jfail(ns):
        return any(not (J1[n][0] and J1[n][1]) for n in ns)

    def fails(ns):
        return any(gt_eps(eps[n], "eps_max") for n in ns)
    if mode == "noext":
        if jfail(range(1, T + 1)):
            return "1", 1, T
        if finite and T < tau:
            return "I-9", 1, None
        Tp = T
    else:
        Tp = max(T, tau) if finite else T
    if jfail(range(1, Tp + 1)):
        return "1", 2, Tp
    if finite and fails(range(1, Tp + 2)):
        return ("2a" if G_Tp_empty else "2b"), 3, Tp
    if not Ra or not Rb or fails(range(1, T + 2)):
        return "3", 4, Tp
    if CLOCK_DECODER:
        return "4", 5, Tp
    if G_status_T == "inconsistent":
        raise Halt(4, field="G_status_T", detail="G* undetermined on W_T at the storage step")
    st = (not fails(range(1, T + 2))) and (
        dil or (not G_T_empty and all(not gt_eps(bound[n], "lemma_h_bound") for n in range(1, T + 2))))
    if st:
        return ("5" if all(sch[n] for n in range(1, T + 1)) else "6"), 6, Tp
    if all(exact(eps[n], "eps_max") == 0 for n in range(1, T + 2)):
        return "7", 7, Tp
    return "8", 8, Tp


def compute_record(ctx, M):
    """Every field of PREREG section 4 'Computed objects' for one tuple and one method. Returns
    (record, pending_halt), where pending_halt is the exit-4 halt of step 6 if it occurred."""
    A, read, P, Pset = ctx.A, ctx.read, ctx.P, ctx.Pset
    Q, par, fR, dec = M.Q, M.par, M.f_R, ctx.decode
    cfgR, cfgQ = all_cfgs(len(A)), all_cfgs(len(Q))

    def cond_R(n):
        out, ps = {s: {} for s in P}, {s: Fraction(0) for s in P}
        for (sg, r, _), p in M.table(n, False).items():
            if sg in Pset:
                out[sg][r] = out[sg].get(r, Fraction(0)) + p
                ps[sg] += p
        for s in P:
            if ps[s] == 0:
                raise Halt(2, field="P", detail="mu(sigma) = 0 for sigma = %s" % s)
            out[s] = {r: p / ps[s] for r, p in out[s].items()}
        return out

    def eps_with(n, d):
        cs = cond_R(n)
        return max(sum((p for r, p in cs[s].items() if d(r) != ctx.fval[s]), Fraction(0)) for s in P)

    def tv(n):
        cs = cond_R(n)
        best = Fraction(0)
        for a, b in itertools.combinations(P, 2):
            keys = set(cs[a]) | set(cs[b])
            best = max(best, sum((abs(cs[a].get(k, 0) - cs[b].get(k, 0)) for k in keys), Fraction(0)) / 2)
        return best

    def tabP(n, need_q):
        return {k: p for k, p in M.table(n, need_q).items() if k[0] in Pset and p > 0}

    def suppR(n):
        return {r for (_, r, _) in tabP(n, False)}

    def suppQ(n):
        return {q for (_, _, q) in tabP(n, True)}

    def J1(n):
        t = tabP(n, True)
        ji = {}
        jii = {}
        for (sg, r, q), p in t.items():
            ji[(sg, q)] = ji.get((sg, q), 0) + p
            jii[(r, sg, q)] = jii.get((r, sg, q), 0) + p
        return (indep(ji), cond_indep(jii))

    need_c = sorted(set().union(*[par[i] for i in read]))

    def C_cells(n):
        t = tabP(n, True)
        out = set()
        for c in need_c:
            if c in A:
                pos, part = A.index(c), 1
            elif c in Q:
                pos, part = Q.index(c), 2
            else:
                raise Halt(EXIT_INTERNAL, field="SCH", detail="Par of a read cell outside A and Q")
            d = {}
            for k, p in t.items():
                key = (k[0], k[part][pos])
                d[key] = d.get(key, 0) + p
            if not indep(d):
                out.add(c)
        return out

    def SCH(n):
        C = C_cells(n)
        return all((par[i] & C) <= {i} for i in read)

    def failures(ticks):
        out = []
        for n in ticks:
            cs = cond_R(n)
            for s in P:
                for r in sorted(cs[s]):
                    if cs[s][r] > 0 and dec(r) != ctx.fval[s]:
                        out.append({"sigma": s, "t": tick(n), "config": r, "prob": rat(cs[s][r], "failures")})
        return out

    rec = {}
    extra = {"Q_cells": [ctx.model.cells[c] for c in Q], "Wr": None, "classes_T": None}
    if ctx.mode == "readback":
        ticks = ctx.readback
        e = {n: eps_with(n, dec) for n in ticks}
        rec["row"] = "I-3"
        rec["eps_max"] = {tick(n): rat(e[n], "eps_max") for n in ticks}
        rec["tv"] = {tick(n): rat(tv(n), "tv") for n in ticks}
        rec["recurrence_flags"] = [tick(n) for n in recurrence(ticks, e)]
        rec["g"] = ctx.g
        extra.update({"ticks": [tick(n) for n in ticks], "failures": failures(ticks), "row_step": 0,
                      "Q_cells": None})
        return rec, extra, None

    T = ctx.T
    hold, win = list(range(1, T + 1)), list(range(1, T + 2))
    QsetT = set().union(*[suppQ(n) for n in hold])
    LsetT = set().union(*[suppR(n) for n in win])
    clsT = classes_of(QsetT, cfgR, fR)
    dil = consistent(clsT, LsetT, dec)
    tau = compute_tau(suppR(1), QsetT, LsetT, fR, dec)
    GT, stT = g_star(QsetT, LsetT, cfgR, fR, dec)
    Tp = (T if tau == INF else max(T, tau)) if ctx.mode == "window" else T
    holdp, winp = list(range(1, Tp + 1)), list(range(1, Tp + 2))
    e = {n: eps_with(n, dec) for n in winp}
    tvs = {n: tv(n) for n in winp}
    J = {n: J1(n) for n in holdp}
    sch = {n: SCH(n) for n in hold}
    if stT == "inconsistent":
        eta = bound = None
    else:
        eta = {}
        for n in hold:
            t, ps, out = M.table(n, True), {s: Fraction(0) for s in P}, {s: Fraction(0) for s in P}
            for (sg, r, q), p in t.items():
                if sg in Pset:
                    ps[sg] += p
                    if q not in GT:
                        out[sg] += p
            eta[n] = max(out[s] / ps[s] for s in P)
        bound = {t: e[1] + sum((eta[s] for s in hold if s < t), Fraction(0)) for t in win}
    if ctx.mode == "window":
        QsetTp = set().union(*[suppQ(n) for n in holdp])
        LsetTp = set().union(*[suppR(n) for n in winp])
        GTp, stTp = g_star(QsetTp, LsetTp, cfgR, fR, dec)
    else:
        GTp, stTp = GT, stT
    flags = recurrence(winp, e)
    t0 = {k: p for k, p in M.table(0, False).items() if k[0] in Pset and p > 0}
    Ra = (not set(A) & set(ctx.Sigma)) and indep({(sg, r): p for (sg, r, _), p in t0.items()})
    glaw = {}
    for (sg, r, _), p in t0.items():
        glaw.setdefault(sg, {})
        glaw[sg][dec(r)] = glaw[sg].get(dec(r), Fraction(0)) + p
    for sg in glaw:
        tot = sum(glaw[sg].values())
        glaw[sg] = {k: v / tot for k, v in glaw[sg].items()}
    Rb = all(glaw.get(s) == glaw.get(P[0]) for s in P)
    decoders = ["".join(b) for b in itertools.product("01", repeat=len(cfgR))]

    def dec_of(tt):
        return lambda r: int(tt[int(r, 2)])
    wme = min(eps_with(1, dec_of(tt)) for tt in decoders)
    sweep = None
    if ctx.is_mdxor:
        sweep = min(max(eps_with(n, dec_of(tt)) for n in win) for tt in decoders)
    w = w_chg = None
    if ctx.is_sk:
        pres = [k for k, c in enumerate(ctx.Sigma) if re.fullmatch(r"p0_[1-9][0-9]*", ctx.model.cells[c])]
        if not pres:
            raise Halt(EXIT_INTERNAL, field="w", detail="no presence bits in Sigma")
        t00 = M.table(0, True)
        w = sum((p for (sg, _, _), p in t00.items() if all(sg[k] == "1" for k in pres)), Fraction(0))
        w_chg = sum((p for (_, r, q), p in t00.items() if fR[(r, q)] != r), Fraction(0))

    pending = None
    try:
        row, step, Tp_out = assign_row(ctx.mode, T, tau, J, e, Ra, Rb, dil, stT, not GT, not GTp, bound, sch)
    except Halt as h:
        if h.code != 4:
            raise
        row, step, Tp_out, pending = None, 6, Tp, h

    rec["row"] = row
    rec["eps_max"] = {tick(n): rat(e[n], "eps_max." + tick(n)) for n in winp}
    rec["tv"] = {tick(n): rat(tvs[n], "tv." + tick(n)) for n in winp}
    rec["Ra"] = bool(Ra)
    rec["Rb"] = bool(Rb)
    rec["dil_exact_T"] = bool(dil)
    rec["tau"] = tau
    rec["T_prime"] = Tp_out
    rec["J1"] = {tick(n): {"Ji": J[n][0], "Jii": J[n][1]} for n in holdp}
    rec["SCH"] = {tick(n): sch[n] for n in hold}
    rec["Q_missing_T"] = sorted(set(cfgQ) - QsetT)
    rec["G_star_out_T"] = sorted(QsetT - GT)
    rec["G_status_T"] = stT
    if ctx.mode == "window":
        rec["Q_missing_Tprime"] = sorted(set(cfgQ) - QsetTp)
        rec["G_star_out_Tprime"] = sorted(QsetTp - GTp)
        rec["G_status_Tprime"] = stTp
    rec["eta"] = None if eta is None else {tick(n): rat(eta[n], "eta." + tick(n)) for n in hold}
    rec["lemma_h_bound"] = (None if bound is None else
                            {tick(n): rat(bound[n], "lemma_h_bound." + tick(n)) for n in win})
    rec["recurrence_flags"] = [tick(n) for n in flags]
    rec["D_bits"] = d_bits(ctx.law, ctx.model, "law")
    rec["g"] = ctx.g
    rec["write_min_eps"] = rat(wme, "write_min_eps")
    rec["w"] = None if w is None else rat(w, "w")
    rec["w_chg"] = None if w_chg is None else rat(w_chg, "w_chg")
    rec["sweep_min_max_eps"] = None if sweep is None else rat(sweep, "sweep_min_max_eps")
    extra.update({
        "ticks": [tick(n) for n in winp],
        "failures": failures(winp),
        "classes_T": clsT,
        "Wr": [q for q in cfgQ if any(dec(fR[(l, q)]) != dec(l) for l in cfgR)],
        "row_step": step,
    })
    return rec, extra, pending


# ----------------------------------------------------------------------------------------------
# Comparison and re-application of section 4 to the JSON fields
# ----------------------------------------------------------------------------------------------

def strict_eq(a, b):
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return set(a) == set(b) and all(strict_eq(a[k], b[k]) for k in a)
    if type(a) is list:
        return len(a) == len(b) and all(strict_eq(x, y) for x, y in zip(a, b))
    return a == b


def field_equal(field, exp, comp):
    """Exact equality; probabilities compare as rationals; null must be computed as null."""
    if exp is None or comp is None:
        return exp is None and comp is None
    if field in PROB_MAP_FIELDS:
        if type(exp) is not dict or type(comp) is not dict or set(exp) != set(comp):
            return False
        return all(parse_rat(exp[k], field) == parse_rat(comp[k], field) for k in exp)
    if field in PROB_SCALAR_FIELDS:
        return parse_rat(exp, field) == parse_rat(comp, field)
    return strict_eq(exp, comp)


def reapply(rec):
    """Re-apply section 4 to a serialized record and check the properties PREREG section 6 names.
    Independent of the internal objects: it reads only the JSON fields. Returns (row, problems)."""
    problems = []
    mode, row = rec.get("mode"), rec.get("row")

    def epsmap(field):
        return {parse_tick(k, field): parse_rat(v, field) for k, v in rec[field].items()}
    eps = epsmap("eps_max")
    ticks = sorted(eps)
    flags, failed = [], False
    for n in ticks:
        if eps[n] > EPS_STAR:
            failed = True
        elif failed:
            flags.append(tick(n))
    if flags != rec["recurrence_flags"]:
        problems.append("recurrence_flags differ from the rule applied to eps_max")
    if mode == "readback":
        if row != "I-3":
            problems.append("readback row is not I-3")
        return "I-3", problems
    T, tau, Tp_rec = rec["T"], rec["tau"], rec["T_prime"]
    finite = tau != INF
    if finite and (type(tau) is not int or tau < 1):
        problems.append("tau is neither a positive integer nor inf")
        return None, problems
    J = {parse_tick(k, "J1"): v for k, v in rec["J1"].items()}

    def jfail(ns):
        return any(not (J[n]["Ji"] and J[n]["Jii"]) for n in ns)

    def fails(ns):
        return any(eps[n] > EPS_STAR for n in ns)
    if mode == "window":
        Tp = max(T, tau) if finite else T
        if Tp_rec != Tp:
            problems.append("T_prime differs from max(T, tau)")
        if not finite and Tp_rec != T:
            problems.append("tau = inf without T_prime = T")
        g_empty_tp = rec["G_status_Tprime"] == "empty"
    else:
        Tp = T
        g_empty_tp = rec["G_status_T"] == "empty"
    if ticks != list(range(1, Tp + 2)):
        problems.append("eps_max keys are not the evaluated window")
    if sorted(J) != list(range(1, Tp + 1)):
        problems.append("J1 keys are not the evaluated hold ticks")
    sch = {parse_tick(k, "SCH"): v for k, v in rec["SCH"].items()}
    if sorted(sch) != list(range(1, T + 1)):
        problems.append("SCH keys are not H_T")
    bound = None
    if rec["lemma_h_bound"] is not None:
        bound = epsmap("lemma_h_bound")
        if sorted(bound) != list(range(1, T + 2)):
            problems.append("lemma_h_bound keys are not W_T")
    if (rec["eta"] is None) != (rec["G_status_T"] == "inconsistent") or (bound is None) != (rec["eta"] is None):
        problems.append("eta and the bound must be null exactly when G_status_T is inconsistent")
    rr = None
    if mode == "noext" and jfail(range(1, T + 1)):
        rr = "1"
    elif mode == "noext" and finite and T < tau:
        rr = "I-9"
    elif jfail(range(1, Tp + 1)):
        rr = "1"
    elif finite and fails(range(1, Tp + 2)):
        rr = "2a" if g_empty_tp else "2b"
    elif not rec["Ra"] or not rec["Rb"] or fails(range(1, T + 2)):
        rr = "3"
    elif CLOCK_DECODER:
        rr = "4"
    elif rec["G_status_T"] == "inconsistent":
        rr = None
    elif rec["dil_exact_T"] or (rec["G_status_T"] != "empty" and bound is not None
                                and all(bound[n] <= EPS_STAR for n in range(1, T + 2))):
        rr = "5" if all(sch[n] for n in range(1, T + 1)) else "6"
    elif all(eps[n] == 0 for n in range(1, T + 2)):
        rr = "7"
    else:
        rr = "8"
    if mode == "noext" and (Tp_rec is None) != (rr == "I-9"):
        problems.append("noext T_prime must be null exactly for I-9")
    if mode == "noext" and Tp_rec is not None and Tp_rec != T:
        problems.append("noext T_prime differs from T")
    if row in ("2a", "2b") and not fails(range(1, Tp + 2)):
        problems.append("a 2a/2b row without an observed eps_max > eps* on W_T'")
    if rec["recurrence_flags"] and row in ("5", "6"):
        problems.append("a flagged tuple in row 5 or 6")
    if rr != row:
        problems.append("re-applied row %s differs from recorded row %s" % (rr, row))
    return rr, problems


def check_record_schema(rec, where):
    no_float(rec, where)
    for f in PROB_MAP_FIELDS:
        if f in rec and rec[f] is not None:
            if type(rec[f]) is not dict:
                raise Halt(2, field=f, detail="not a map")
            for k, v in rec[f].items():
                parse_tick(k, f)
                parse_rat(v, f + "." + k)
    for f in PROB_SCALAR_FIELDS:
        if f in rec and rec[f] is not None:
            parse_rat(rec[f], f)
    for item in rec.get("failures") or []:
        parse_rat(item["prob"], "failures")
    for k, v in FIXED_STRINGS.items():
        if rec.get(k) != v:
            raise Halt(2, field=k, detail="fixed string")
    if rec.get("w_star") is not None or rec.get("T_star") is not None:
        raise Halt(2, field="w_star", detail="w* and T* must be null")
    if "row" in rec and rec["row"] is not None and rec["row"] not in ROW_CODES:
        raise Halt(2, field="row", detail="row code")


# ----------------------------------------------------------------------------------------------
# One tuple
# ----------------------------------------------------------------------------------------------

def evaluate_tuple(ctx, method, seq_hook=None):
    """Compute one tuple's record by its frozen method. For full+sequential, both methods run and
    every compared field (and Q) must agree exactly (exit 5 otherwise)."""
    if method == "full":
        M = FullMethod(ctx)
        rec, extra, pending = compute_record(ctx, M)
        extra["injective"] = True
        return rec, extra, pending, None
    if method == "sequential":
        M = SequentialMethod(ctx)
        rec, extra, pending = compute_record(ctx, M)
        extra["injective"] = None
        return rec, extra, pending, None
    Mf = FullMethod(ctx)
    rec, extra, pending = compute_record(ctx, Mf)
    if pending is not None:
        extra["injective"] = True
        return rec, extra, pending, None
    Ms = SequentialMethod(ctx)
    rec_s, extra_s, pending_s = compute_record(ctx, Ms)
    if seq_hook is not None:
        seq_hook(rec_s, extra_s)
    if pending_s is not None:
        raise Halt(5, field="method", detail="full and sequential disagree on the exit-4 condition")
    fields = [f for f in rec if f != "method"] + ["Q_cells"]
    for f in fields:
        a = rec.get(f) if f != "Q_cells" else extra["Q_cells"]
        b = rec_s.get(f) if f != "Q_cells" else extra_s["Q_cells"]
        if not strict_eq(a, b):
            raise Halt(5, field=f, detail="full and sequential disagree on %s" % f,
                       expected=a, computed=b)
    extra["injective"] = True
    extra["sequential_check"] = {"fields_compared": fields, "agree": True}
    return rec, extra, None, None


def build_output(ctx, method, rec, extra, compared, frozen_inputs, run):
    rec = dict(rec)
    rec["method"] = method
    out = {"schema": RECORD_SCHEMA, "tuple_id": ctx.id, "order": ctx.tup["order"], "mode": ctx.mode,
           "params": ctx.params}
    for f in compared:
        if f not in rec:
            raise Halt(2, field=f, detail="compared field not computed for this mode")
        out[f] = rec[f]
    for f, v in rec.items():
        if f not in out:
            out[f] = v
    out.update({
        "eps_star": FIXED_STRINGS["eps_star"], "w_star": None, "T_star": None,
        "kappa": FIXED_STRINGS["kappa"], "independence_law": FIXED_STRINGS["independence_law"],
        "support_conditioning": FIXED_STRINGS["support_conditioning"], "B_def": FIXED_STRINGS["B_def"],
        "Q_cells": extra["Q_cells"], "read_cells": list(ctx.tup["read_cells"]),
        "injective": extra.get("injective"), "law": ctx.law, "P": ctx.P, "f": list(ctx.tup["f"]),
        "T": ctx.T, "ticks": extra["ticks"], "failures": extra["failures"],
        "classes_T": extra["classes_T"], "Wr": extra["Wr"], "row_step": extra["row_step"],
        "rd_test": FIXED_STRINGS["rd_test"], "access": FIXED_STRINGS["access"],
    })
    if "sequential_check" in extra:
        out["sequential_check"] = extra["sequential_check"]
    out["frozen_inputs"] = frozen_inputs
    out["run"] = run
    return out


# ----------------------------------------------------------------------------------------------
# Input validation and the run
# ----------------------------------------------------------------------------------------------

def validate_docs(tdoc, edoc, expect_count, frozen_order_rule):
    if type(tdoc) is not dict or tdoc.get("schema") != TUPLES_SCHEMA:
        raise Halt(2, field="tuples.schema", detail="tuples schema")
    if type(edoc) is not dict or edoc.get("schema") != EXPECTED_SCHEMA:
        raise Halt(2, field="expected.schema", detail="expected schema")
    conv = tdoc.get("conventions")
    if type(conv) is not dict or conv.get("eps_star") != "1/20":
        raise Halt(2, field="conventions.eps_star", detail="eps_star must be 1/20")
    cf = tdoc.get("compared_fields")
    if type(cf) is not dict or set(cf) != {"window", "noext", "readback"}:
        raise Halt(2, field="compared_fields", detail="modes")
    for mode, lst in cf.items():
        if type(lst) is not list or len(set(lst)) != len(lst) or not set(lst) <= set(KNOWN_FIELDS) or "row" not in lst:
            raise Halt(2, field="compared_fields." + mode, detail="field list")
    if type(tdoc.get("models")) is not dict:
        raise Halt(2, field="models", detail="models")
    tuples = tdoc.get("tuples")
    if type(tuples) is not list or len(tuples) != expect_count:
        raise Halt(2, field="tuples", detail="tuples_frozen must be %d" % expect_count)
    ids = [t.get("id") if type(t) is dict else None for t in tuples]
    if not all(type(i) is str and i for i in ids) or len(set(ids)) != len(ids):
        raise Halt(2, field="tuples.id", detail="ids")
    if [t.get("order") for t in tuples] != list(range(1, len(tuples) + 1)):
        raise Halt(2, field="order", detail="orders are not 1..N in the listed sequence")
    if frozen_order_rule:
        sk = [t for t in tuples if t.get("model") == "trigger-channel"]
        if [t.get("order") for t in sk] != list(range(len(tuples) - len(sk) + 1, len(tuples) + 1)):
            raise Halt(2, field="order", detail="HC-SK tuples do not follow the non-HC-SK tuples")
        try:
            keys = [((t["T"] + 1) * (t["params"]["k"] + 1) + 1, t["params"]["k"]) for t in sk]
        except (KeyError, TypeError):
            raise Halt(2, field="order", detail="HC-SK params")
        if keys != sorted(keys) or len(set(keys)) != len(keys):
            raise Halt(2, field="order", detail="HC-SK tuples not sorted by (n_bits, k)")
    exp = edoc.get("expected")
    if type(exp) is not dict or set(exp) != set(ids):
        raise Halt(2, field="expected", detail="expected entries must match the tuple ids")
    for t in tuples:
        e = exp[t["id"]]
        mode = t.get("mode")
        if mode not in cf:
            raise Halt(2, field="mode", detail="unknown mode", tuple_id=t["id"])
        if type(e) is not dict or set(e) != set(cf[mode]):
            raise Halt(2, field="expected." + t["id"], detail="expected fields differ from the mode's list")
        if e["row"] not in ROW_CODES:
            raise Halt(2, field="expected.%s.row" % t["id"], detail="row code")
        for f in PROB_MAP_FIELDS:
            if f in e and e[f] is not None:
                if type(e[f]) is not dict:
                    raise Halt(2, field="expected.%s.%s" % (t["id"], f), detail="not a map")
                for k, v in e[f].items():
                    parse_tick(k, "expected.%s.%s" % (t["id"], f))
                    parse_rat(v, "expected.%s.%s.%s" % (t["id"], f, k))
        for f in PROB_SCALAR_FIELDS:
            if f in e and e[f] is not None:
                parse_rat(e[f], "expected.%s.%s" % (t["id"], f))
    return tuples, cf, exp


def render_verdict(summary):
    """verdict_text from summary.json fields only (PREREG section 5)."""
    if summary["verdict"] == "PASS":
        return "Phase A: all %d frozen tuples reproduced their expected rows and values." % summary["tuples_frozen"]
    ff = summary["first_failure"] or {}
    code = ff.get("exit")
    tid = ff.get("tuple_id")
    if code == 1:
        return "Phase A halted at %s: %s expected %s, computed %s. The run is void." % (
            tid, ff.get("field"), dumps_canonical(ff.get("expected")), dumps_canonical(ff.get("computed")))
    if code == 2:
        return "Phase A halted at %s: schema violation in %s. The run is void." % (
            tid if tid is not None else "start", ff.get("field"))
    if code == 3:
        return ("Phase A halted at start: frozen input %s does not match its git blob id at F. The run is void."
                % ff.get("detail"))
    if code == 4:
        return "Phase A halted at %s: G* undetermined on W_T at storage step. The run is void." % tid
    if code == 5:
        return "Phase A halted at %s: enumeration-method check failed (%s). The run is void." % (tid, ff.get("detail"))
    return "Phase A halted with exit %s. The run is void." % code


def write_json(path, obj):
    no_float(obj, os.path.basename(path))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=1, ensure_ascii=True)
        fh.write("\n")


def run(out_dir, tdoc_bytes, edoc_bytes, frozen_inputs, run_meta, expect_count=TUPLES_FROZEN,
        frozen_order_rule=True, seq_hook=None):
    """The preregistered run over already hash-checked input bytes. Returns the exit code; writes
    out_dir/phase-a/<tuple_id>.json and out_dir/phase-a/summary.json."""
    pa = os.path.join(out_dir, "phase-a")
    evaluated, rows = [], []
    state = {"halt": None, "n": expect_count}

    def finish(h):
        summary = {
            "schema": SUMMARY_SCHEMA, "tuples_frozen": state["n"], "tuples_evaluated": evaluated,
            "first_failure": None if h is None else h.failure(),
            "verdict": "PASS" if h is None else "HALT", "exit": 0 if h is None else h.code,
            "eps_star": "1/20", "w_star": None, "T_star": None,
            "run": run_meta, "frozen_inputs": frozen_inputs, "tuples": rows,
        }
        summary["verdict_text"] = render_verdict(summary)
        try:
            write_json(os.path.join(pa, "summary.json"), summary)
        except Halt as h2:  # a non-JSON value in a failure detail: record the schema violation
            summary["first_failure"] = h2.failure()
            summary["exit"], summary["verdict"] = 2, "HALT"
            summary["first_failure"]["expected"] = summary["first_failure"]["computed"] = None
            summary["verdict_text"] = render_verdict(summary)
            write_json(os.path.join(pa, "summary.json"), summary)
            return 2
        return summary["exit"]

    try:
        tdoc = load_json_bytes(tdoc_bytes, "PHASEA-TUPLES.json")
        edoc = load_json_bytes(edoc_bytes, "PHASEA-EXPECTED.json")
        tuples, cf, exp = validate_docs(tdoc, edoc, expect_count, frozen_order_rule)
    except Halt as h:
        h.tuple_id = None
        return finish(h)
    for tup in tuples:
        tid = tup["id"]
        evaluated.append(tid)
        try:
            ctx = TupleCtx(tup, tdoc["models"])
            method = method_for(ctx)
            if method != tup["method"]:
                raise Halt(5, field="method", detail="declared method %s differs from the section 2.0 rule (%s)"
                           % (tup["method"], method))
            rec, extra, pending, _ = evaluate_tuple(ctx, method, seq_hook=seq_hook)
            out = build_output(ctx, method, rec, extra, cf[ctx.mode], frozen_inputs, run_meta)
            out["expected"] = exp[tid]
            check_record_schema(out, tid)
            if pending is not None:
                out["comparisons"], out["match"] = [], False
                write_json(os.path.join(pa, tid + ".json"), out)
                rows.append({"tuple_id": tid, "order": tup["order"], "mode": ctx.mode, "row": None,
                             "match": False, "computed": {f: out.get(f) for f in cf[ctx.mode]}})
                raise pending
            rerow, problems = reapply(json.loads(json.dumps(out)))
            comps = [{"field": f, "expected": exp[tid][f], "computed": out[f],
                      "match": field_equal(f, exp[tid][f], out[f])} for f in cf[ctx.mode]]
            out["comparisons"] = comps
            out["match"] = all(c["match"] for c in comps) and not problems
            out["reapplied_row"] = rerow
            out["reapply_problems"] = problems
            write_json(os.path.join(pa, tid + ".json"), out)
            rows.append({"tuple_id": tid, "order": tup["order"], "mode": ctx.mode, "row": out["row"],
                         "match": out["match"], "computed": {f: out[f] for f in cf[ctx.mode]}})
            if problems:
                raise Halt(EXIT_REAPPLY, field="row", detail="; ".join(problems))
            bad = [c for c in comps if not c["match"]]
            if bad:
                raise Halt(1, field=bad[0]["field"], expected=bad[0]["expected"], computed=bad[0]["computed"])
        except Halt as h:
            if h.tuple_id is None:
                h.tuple_id = tid
            return finish(h)
        except Exception as ex:  # an unexpected error is a red, never a pass
            return finish(Halt(EXIT_INTERNAL, tuple_id=tid, detail="%s: %s" % (type(ex).__name__, ex)))
    return finish(None)


def check_summary(out_dir, order_ids, expect_count=TUPLES_FROZEN):
    """The in-job regeneration step: verdict_text regenerated byte for byte, section 4 re-applied to
    every per-tuple record, and the halt bookkeeping. Returns (ok, report)."""
    pa = os.path.join(out_dir, "phase-a")
    report = {"schema": "oret-phase-a-check/1", "checks": {}, "reapply": []}
    c = report["checks"]
    try:
        with open(os.path.join(pa, "summary.json"), "rb") as fh:
            s = load_json_bytes(fh.read(), "summary.json")
    except (OSError, Halt):
        c["summary_readable"] = False
        return False, report
    c["summary_readable"] = True
    try:
        c["verdict_text_regenerated_equal"] = (render_verdict(s).encode("utf-8") == s["verdict_text"].encode("utf-8"))
    except (KeyError, TypeError, AttributeError):
        c["verdict_text_regenerated_equal"] = False
    ev = s.get("tuples_evaluated") or []
    ff = s.get("first_failure")
    c["tuples_frozen"] = s.get("tuples_frozen") == expect_count
    c["prefix_of_frozen_order"] = ev == order_ids[:len(ev)]
    if s.get("verdict") == "PASS":
        c["verdict_consistent"] = ff is None and s.get("exit") == 0 and ev == order_ids
    else:
        c["verdict_consistent"] = (s.get("verdict") == "HALT" and ff is not None and s.get("exit") == ff.get("exit")
                                   and s.get("exit") not in (0, None))
        if ff is not None and ff.get("tuple_id") is not None:
            c["halt_at_last_evaluated"] = bool(ev) and ev[-1] == ff["tuple_id"]
    ok_records = True
    for tid in ev:
        path = os.path.join(pa, tid + ".json")
        if not os.path.exists(path):
            if s.get("verdict") == "PASS":
                ok_records = False
            continue
        try:
            with open(path, "rb") as fh:
                rec = load_json_bytes(fh.read(), tid)
            check_record_schema(rec, tid)
            rr, problems = reapply(rec)
            entry = {"tuple_id": tid, "row": rec.get("row"), "reapplied_row": rr, "problems": problems}
            if rec.get("row") is not None and problems:
                ok_records = False
            if s.get("verdict") == "PASS" and not rec.get("match"):
                ok_records = False
        except (Halt, KeyError, TypeError, ValueError) as ex:
            entry = {"tuple_id": tid, "row": None, "reapplied_row": None, "problems": ["unreadable: %s" % ex]}
            ok_records = False
        report["reapply"].append(entry)
    c["records_reapply"] = ok_records
    report["pass"] = all(c.values())
    return report["pass"], report


# ----------------------------------------------------------------------------------------------
# Self-test (synthetic inputs only; no frozen tuple is evaluated)
# ----------------------------------------------------------------------------------------------

ST_MODELS = {
    "st-gated-hold": {"cells": ["k", "x", "r"], "rule": [
        [{"lhs": "x", "rhs": "ite(k, r, x)"}, {"lhs": "r", "rhs": "ite(k, x, r)"}],
        [{"lhs": "k", "rhs": "k ^ 1"}]]},
    "st-gated-swap": {"cells": ["k", "x", "r1", "r2"], "rule": [
        [{"lhs": "x", "rhs": "ite(k, r1, x)"}, {"lhs": "r1", "rhs": "ite(k, x, r1)"}],
        [{"lhs": "r1", "rhs": "r2"}, {"lhs": "r2", "rhs": "r1"}],
        [{"lhs": "k", "rhs": "k ^ 1"}]]},
    "st-shift": {"cells": "u0 .. u{L-1}", "rule": [
        [{"lhs": "u{j}", "rhs": "u{(j-1) mod L}", "range": "j = 0 .. L-1"}]]},
    "st-collapse": {"cells": ["a", "b"], "rule": [[{"lhs": "a", "rhs": "b"}], [{"lhs": "b", "rhs": "a"}]]},
    "st-swap1": {"cells": ["a", "b"], "rule": [[{"lhs": "a", "rhs": "b"}, {"lhs": "b", "rhs": "a"}]]},
    "st-toffoli-channel": {"cells": "p0, v0, p1, v1, .., p{L-1}, v{L-1}, r", "rule": [
        [{"lhs": "r", "rhs": "r ^ (p0 & v0)"}],
        [{"lhs": "p{j}", "rhs": "p{(j-1) mod L}", "range": "j = 0 .. L-1"},
         {"lhs": "v{j}", "rhs": "v{(j-1) mod L}", "range": "j = 0 .. L-1"}]]},
    "st-conj": {"cells": ["p0_1", "p0_2", "v0", "r"], "rule": [
        [{"lhs": "v0", "rhs": "ite(p0_1 & .. & p0_k, r, v0)"}, {"lhs": "r", "rhs": "ite(p0_1 & .. & p0_k, v0, r)"}]]},
}


def _st_tuple(order, tid, model, mode, T, Sigma, law, A, g, params=None, P=("0", "1"), read=None):
    return {"order": order, "id": tid, "model": model, "params": params or {}, "mode": mode, "T": T,
            "Sigma": list(Sigma), "P": list(P), "f": [0, 1], "law": law, "A": list(A),
            "read_cells": list(read or A), "g": g, "method": "full"}


def _J(*ns):
    return {tick(n): {"Ji": True, "Jii": True} for n in ns}


def _st_docs():
    """Five synthetic tuples with hand-derived expected values (none is a frozen tuple)."""
    cf_w = list(KNOWN_FIELDS)
    cf_n = [f for f in KNOWN_FIELDS if not f.endswith("_Tprime") and f not in ("w", "w_chg", "sweep_min_max_eps")]
    hold = _st_tuple(1, "st-hold", "st-gated-hold", "window", 1, ["x"],
                     {"type": "uniform_conditioned", "equalities": {"k": 1, "r": 0}}, ["r"], "01")
    swap = _st_tuple(2, "st-swap", "st-gated-swap", "window", 1, ["x"],
                     {"type": "uniform_conditioned", "equalities": {"k": 1, "r1": 0, "r2": 0}}, ["r1", "r2"], "0110")
    shift = _st_tuple(3, "st-shift1", "st-shift", "window", 1, ["u0"],
                      {"type": "uniform_conditioned", "equalities": {"u1": 0}}, ["u1"], "01", params={"L": 3})
    plaw = {"type": "uniform_conditioned", "equalities": {"u1": 0, "u2": 0, "u3": 0, "u4": 0}}
    pn = _st_tuple(4, "st-pulse-noext", "st-shift", "noext", 1, ["u0"], plaw, ["u1", "u2", "u3"], "01101001",
                   params={"L": 5})
    pw = _st_tuple(5, "st-pulse-window", "st-shift", "window", 1, ["u0"], plaw, ["u1", "u2", "u3"], "01101001",
                   params={"L": 5})
    nul = {"w": None, "w_chg": None, "sweep_min_max_eps": None}
    e_hold = dict(row="5", eps_max={"t0+1": "0", "t0+2": "0"}, tv={"t0+1": "1", "t0+2": "1"}, Ra=True, Rb=True,
                  dil_exact_T=True, tau=INF, T_prime=1, J1=_J(1), SCH={"t0+1": True},
                  Q_missing_T=["01", "10", "11"], G_star_out_T=[], G_status_T="consistent",
                  Q_missing_Tprime=["01", "10", "11"], G_star_out_Tprime=[], G_status_Tprime="consistent",
                  eta={"t0+1": "0"}, lemma_h_bound={"t0+1": "0", "t0+2": "0"}, recurrence_flags=[], D_bits=2,
                  method="full", g="01", write_min_eps="0", **nul)
    e_swap = dict(e_hold, row="6", SCH={"t0+1": False}, D_bits=3, g="0110")
    e_shift = dict(row="2a", eps_max={"t0+1": "0", "t0+2": "1/2"}, tv={"t0+1": "1", "t0+2": "0"}, Ra=True,
                   Rb=True, dil_exact_T=False, tau=1, T_prime=1, J1=_J(1), SCH={"t0+1": True}, Q_missing_T=[],
                   G_star_out_T=["0", "1"], G_status_T="empty", Q_missing_Tprime=[], G_star_out_Tprime=["0", "1"],
                   G_status_Tprime="empty", eta={"t0+1": "1"}, lemma_h_bound={"t0+1": "0", "t0+2": "1"},
                   recurrence_flags=[], D_bits=1, method="full", g="01", write_min_eps="0", **nul)
    e_pn = dict(row="I-9", eps_max={"t0+1": "0", "t0+2": "0"}, tv={"t0+1": "1", "t0+2": "1"}, Ra=True, Rb=True,
                dil_exact_T=False, tau=3, T_prime=None, J1=_J(1), SCH={"t0+1": False}, Q_missing_T=["1"],
                G_star_out_T=["0"], G_status_T="empty", eta={"t0+1": "1"},
                lemma_h_bound={"t0+1": "0", "t0+2": "1"}, recurrence_flags=[], D_bits=4, method="full",
                g="01101001", write_min_eps="0")
    e_pw = dict(e_pn, row="2a", eps_max={"t0+1": "0", "t0+2": "0", "t0+3": "0", "t0+4": "1"},
                tv={"t0+1": "1", "t0+2": "1", "t0+3": "1", "t0+4": "0"}, T_prime=3, J1=_J(1, 2, 3),
                Q_missing_Tprime=["1"], G_star_out_Tprime=["0"], G_status_Tprime="empty", **nul)
    tdoc = {"schema": TUPLES_SCHEMA, "conventions": {"eps_star": "1/20"},
            "compared_fields": {"window": cf_w, "noext": cf_n, "readback": ["row", "eps_max", "tv",
                                                                             "recurrence_flags", "method", "g"]},
            "models": ST_MODELS, "tuples": [hold, swap, shift, pn, pw]}
    edoc = {"schema": EXPECTED_SCHEMA, "expected": {"st-hold": e_hold, "st-swap": e_swap, "st-shift1": e_shift,
                                                    "st-pulse-noext": e_pn, "st-pulse-window": e_pw}}
    return tdoc, edoc


def _b(obj):
    return json.dumps(obj).encode("utf-8")


def _expect_halt(code, fn):
    try:
        fn()
    except Halt as h:
        assert h.code == code, "expected exit %d, got %d (%s)" % (code, h.code, h)
        return h
    raise AssertionError("expected exit %d, no halt" % code)


def _ctx(tup, models=None):
    return TupleCtx(tup, models or ST_MODELS)


def self_test():
    checks = []

    def check(name):
        def deco(fn):
            try:
                fn()
                checks.append({"name": name, "ok": True})
            except Exception as ex:  # report, do not stop
                checks.append({"name": name, "ok": False, "detail": "%s: %s" % (type(ex).__name__, ex)})
            return fn
        return deco

    meta = [{"path": "synthetic", "blob_at_F": None, "blob_read": None}]
    runm = {"F": F_COMMIT, "commit": None, "run_attempt": None}

    @check("blob ids of known byte strings")
    def _():
        assert blob_id(b"") == "e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
        assert blob_id(b"hello\n") == "ce013625030ba8dba906f756967f9e9ca394464a"

    @check("frozen-input check: match, mismatch, F absent, F not an ancestor (exit 3)")
    def _():
        files = {p: ("content of %s\n" % p).encode() for p in FROZEN_PATHS}

        def fake_git(at_f, has_f=True, ancestor=True):
            def g(repo, args):
                if args[0] == "cat-file":
                    return (0, "") if has_f else (1, "")
                if args[0] == "log":
                    return 0, (F_COMMIT if ancestor else "0" * 40)
                if args[0] == "rev-parse":
                    return 0, at_f[args[-1].split(":", 1)[1]]
                return 1, ""
            return g
        good = {p: blob_id(b) for p, b in files.items()}
        meta_ok, data = check_frozen_inputs("/nonexistent", git=fake_git(good), read=lambda p: files[p])
        assert [m["blob_read"] for m in meta_ok] == [good[p] for p in FROZEN_PATHS] and data == files
        bad = dict(good)
        bad[FROZEN_PATHS[2]] = "0" * 40
        h = _expect_halt(3, lambda: check_frozen_inputs("/x", git=fake_git(bad), read=lambda p: files[p]))
        assert h.detail == FROZEN_PATHS[2]
        s = {"verdict": "HALT", "tuples_frozen": 49, "first_failure": h.failure()}
        assert render_verdict(s) == ("Phase A halted at start: frozen input %s does not match its git blob id at F. "
                                     "The run is void." % FROZEN_PATHS[2])
        _expect_halt(3, lambda: check_frozen_inputs("/x", git=fake_git(good, has_f=False), read=lambda p: files[p]))
        _expect_halt(3, lambda: check_frozen_inputs("/x", git=fake_git(good, ancestor=False), read=lambda p: files[p]))

    @check("exactness guard: floats rejected in JSON input, records, serialization and comparisons (exit 2)")
    def _():
        _expect_halt(2, lambda: load_json_bytes(b'{"p": 0.05}', "x"))
        _expect_halt(2, lambda: load_json_bytes(b'{"p": NaN}', "x"))
        _expect_halt(2, lambda: load_json_bytes(b'{"p": 1, "p": 2}', "x"))
        _expect_halt(2, lambda: no_float({"eps_max": {"t0+1": 0.5}}, "rec"))
        _expect_halt(2, lambda: no_float({"x": Fraction(1, 2)}, "rec"))
        _expect_halt(2, lambda: rat(0.5, "eps"))
        _expect_halt(2, lambda: gt_eps(0.06, "eps"))
        _expect_halt(2, lambda: exact(True, "eps"))
        for s in ("2/4", "0.5", "01", "1/1", "0/3", "-1/2", "1/0"):
            _expect_halt(2, lambda s=s: parse_rat(s, "p"))
        assert parse_rat("37/128", "p") == Fraction(37, 128) and rat(Fraction(2, 4), "p") == "1/2"
        assert not gt_eps(Fraction(1, 20), "e") and gt_eps(Fraction(51, 1000), "e")
        rec = {"eps_max": {"t0+1": "1/2"}, "w_star": None, "T_star": None}
        rec.update(FIXED_STRINGS)
        check_record_schema(rec, "r")
        rec["eps_max"]["t0+1"] = 0.5
        _expect_halt(2, lambda: check_record_schema(rec, "r"))

    @check("expression grammar, templates and simultaneous steps")
    def _():
        env = {"L": 4}
        assert arith("(j-1) mod L", dict(env, j=0), "w") == 3 and arith("m+2", {"m": 3}, "w") == 5
        assert subst("p{(j-1) mod L}_{i}", dict(env, j=0, i=2), "w") == "p3_2"
        assert expand_conj("ite(p0_1 & .. & p0_k, r, v0)", {"k": 3}, "w") == "ite((p0_1 & p0_2 & p0_3), r, v0)"
        assert expand_conj("p0_1 & .. & p0_k", {"k": 1}, "w") == "(p0_1)"
        idx = {"a": 0, "b": 1, "c": 2}
        _expect_halt(2, lambda: parse_expr("a ^ b & c", idx, "w"))
        _expect_halt(2, lambda: parse_expr("a ^ d", idx, "w"))
        f = compile_expr(parse_expr("a ^ (b & c) ^ 1", idx, "w"))
        assert [f(s) for s in range(8)] == [1 ^ (s & 1) ^ ((s >> 1) & (s >> 2) & 1) for s in range(8)]
        g = compile_expr(parse_expr("ite(a, b, c)", idx, "w"))
        assert [g(s) for s in range(8)] == [((s >> 1) & 1) if s & 1 else ((s >> 2) & 1) for s in range(8)]
        m = Model(ST_MODELS["st-conj"], {"k": 2}, "m")
        # fired (p0_1 = p0_2 = 1): v0 <-> r swap; otherwise identity
        for s in range(16):
            fired = (s & 3) == 3
            v, r = (s >> 2) & 1, (s >> 3) & 1
            want = (s & 3) | ((r if fired else v) << 2) | ((v if fired else r) << 3)
            assert m.phi(s) == want
        dead = Model({"cells": ["a", "b", "c"], "rule": [[{"lhs": "a", "rhs": "ite(b, c, c) ^ a"}]]}, {}, "m")
        assert par_restricted(dead, 0) == {0, 2}  # b is a syntactic, not a semantic, dependence
        dt = _st_tuple(1, "st-dead", "st-dead", "window", 1, ["c"], {"type": "uniform"}, ["a"], "01")
        dm = {"st-dead": {"cells": ["a", "b", "c"], "rule": [[{"lhs": "a", "rhs": "ite(b, c, c) ^ a"}]]}}
        assert FullMethod(TupleCtx(dt, dm)).par == {0: {0, 2}} and FullMethod(TupleCtx(dt, dm)).Q == [2]
        assert SequentialMethod(TupleCtx(dt, dm)).Q == [2]
        sw = Model(ST_MODELS["st-swap1"], {}, "m")
        assert [sw.phi(s) for s in range(4)] == [0, 2, 1, 3]
        ring = Model(ST_MODELS["st-shift"], {"L": 3}, "m")
        assert ring.cells == ["u0", "u1", "u2"] and ring.phi(0b001) == 0b010 and ring.phi(0b100) == 0b001
        _expect_halt(2, lambda: Model({"cells": ["a"], "rule": [[{"lhs": "a", "rhs": "a"}, {"lhs": "a", "rhs": "1"}]]},
                                      {}, "m"))
        _expect_halt(2, lambda: Model({"cells": "x0 .. x{L-1}", "rule": []}, {"L": 2}, "m"))

    @check("non-injective map exits 5 (sequential reading of a 2-cycle); the simultaneous swap passes")
    def _():
        t = _st_tuple(1, "st-collapse", "st-collapse", "window", 1, ["a"], {"type": "uniform"}, ["b"], "01")
        h = _expect_halt(5, lambda: FullMethod(_ctx(t)))
        assert h.field == "injective"
        t2 = dict(t, model="st-swap1")
        assert FullMethod(_ctx(t2)).injective is True

    @check("hand-derived synthetic tuples: rows 5, 6, 2a, I-9 and all fields")
    def _():
        tdoc, edoc = _st_docs()
        for tup in tdoc["tuples"]:
            ctx = _ctx(tup)
            rec, extra, pending, _ = evaluate_tuple(ctx, "full")
            assert pending is None
            rec["method"] = "full"
            exp = edoc["expected"][tup["id"]]
            for f in tdoc["compared_fields"][tup["mode"]]:
                assert field_equal(f, exp[f], rec[f]), "%s %s: expected %r computed %r" % (tup["id"], f, exp[f], rec[f])
            rr, problems = reapply(dict(rec, mode=tup["mode"], T=tup["T"]))
            assert rr == exp["row"] and not problems, (tup["id"], rr, problems)

    @check("window extension: the pooled Q-set over W_T' differs from W_T and decides the T' fields")
    def _():
        # ring of 5, A = (u1, u2, u3), parity, u3 free at t0: u0 is 0, n, 0 at t0+1, t0+2, t0+3
        t = _st_tuple(1, "st-pulse-free", "st-shift", "window", 1, ["u0"],
                      {"type": "uniform_conditioned", "equalities": {"u1": 0, "u2": 0, "u4": 0}},
                      ["u1", "u2", "u3"], "01101001", params={"L": 5})
        rec, _, _, _ = evaluate_tuple(_ctx(t), "full")
        assert rec["tau"] == 3 and rec["T_prime"] == 3 and rec["row"] == "2a", rec
        assert rec["eps_max"] == {"t0+1": "0", "t0+2": "0", "t0+3": "1/2", "t0+4": "1/2"}
        assert rec["Q_missing_T"] == ["1"] and rec["G_star_out_T"] == ["0"]
        assert rec["Q_missing_Tprime"] == [] and rec["G_star_out_Tprime"] == ["0", "1"]
        assert rec["G_status_Tprime"] == "empty" and rec["J1"] == _J(1, 2, 3)
        # a hit needs l_k in L_{W_T}: with g = u1 ^ u2, 100 -> 010 -> 001 decodes 0 at k = 2, but 001 is
        # unsupported on W_1, so the first hit is 000 at k = 3
        t2 = _st_tuple(1, "st-pulse-xor12", "st-shift", "noext", 1, ["u0"],
                       {"type": "uniform_conditioned", "equalities": {"u1": 0, "u2": 0, "u3": 0, "u4": 0}},
                       ["u1", "u2", "u3"], "00111100", params={"L": 5})
        rec, _, _, _ = evaluate_tuple(_ctx(t2), "full")
        assert rec["tau"] == 3 and rec["row"] == "I-9" and rec["T_prime"] is None, rec

    @check("G* on W_T' differs from G* on W_T: a gated conveyor is EX (2b), not TR")
    def _():
        models = dict(ST_MODELS)
        models["st-gated-conveyor"] = {"cells": ["x0", "h0", "x1", "h1", "x2", "h2", "r1", "r2"], "rule": [
            [{"lhs": "x0", "rhs": "ite(h0, x0, r2)"}, {"lhs": "r1", "rhs": "ite(h0, r1, x0)"},
             {"lhs": "r2", "rhs": "ite(h0, r2, r1)"}],
            [{"lhs": "x{j}", "rhs": "x{(j-1) mod 3}", "range": "j = 0 .. 2"},
             {"lhs": "h{j}", "rhs": "h{(j-1) mod 3}", "range": "j = 0 .. 2"}]]}
        t = _st_tuple(1, "st-gated-conveyor", "st-gated-conveyor", "window", 1, ["x0"],
                      {"type": "uniform_conditioned",
                       "equalities": {"h0": 0, "r1": 0, "r2": 0, "x2": 0, "h2": 0, "x1": 0}},
                      ["r1", "r2"], "0110")
        rec, extra, _, _ = evaluate_tuple(_ctx(t, models), "full")
        assert extra["Q_cells"] == ["x0", "h0"] and rec["tau"] == 2 and rec["T_prime"] == 2, (rec, extra)
        assert rec["eps_max"] == {"t0+1": "0", "t0+2": "0", "t0+3": "1/2"}
        assert rec["G_star_out_T"] == ["00"] and rec["G_status_T"] == "empty"
        assert rec["Q_missing_T"] == ["01", "10", "11"] and rec["Q_missing_Tprime"] == ["10", "11"]
        assert rec["G_star_out_Tprime"] == ["00"] and rec["G_status_Tprime"] == "consistent"
        assert rec["row"] == "2b" and rec["J1"] == _J(1, 2)

    @check("support conditioning on P, Q from A as a whole, and (R-a)/(R-b) failures")
    def _():
        models = dict(ST_MODELS)
        models["st-static2"] = {"cells": ["s", "v", "r"], "rule": [[{"lhs": "r", "rhs": "r ^ (s & v)"}]]}
        t = _st_tuple(1, "st-static2", "st-static2", "window", 1, ["s", "v"],
                      {"type": "uniform_conditioned", "equalities": {"r": 0}}, ["r"], "01", P=("10", "11"))
        rec, _, _, _ = evaluate_tuple(_ctx(t, models), "full")
        assert rec["Q_missing_T"] == ["00", "01"] and rec["G_star_out_T"] == ["11"], rec
        assert rec["J1"] == {"t0+1": {"Ji": False, "Jii": True}} and rec["row"] == "1"
        assert rec["eps_max"] == {"t0+1": "0", "t0+2": "1"}  # c = 1: r = 1 ^ 1 = 0 at t0+2 with certainty
        sw = _st_tuple(1, "st-swap-r2", "st-gated-swap", "window", 1, ["x"],
                       {"type": "uniform_conditioned", "equalities": {"k": 1, "r1": 0, "r2": 0}},
                       ["r1", "r2"], "0101", read=["r2"])
        rec, extra, _, _ = evaluate_tuple(_ctx(sw), "full")
        assert extra["Q_cells"] == ["k", "x"] and rec["SCH"] == {"t0+1": True}, (rec["SCH"], extra["Q_cells"])
        bad = _st_tuple(1, "st-hold-ab", "st-gated-hold", "window", 1, ["x"],
                        {"type": "explicit", "states": {"100": "1/2", "111": "1/2"}}, ["r"], "01")
        rec, _, _, _ = evaluate_tuple(_ctx(bad), "full")
        assert rec["Ra"] is False and rec["Rb"] is False

    @check("J-1: an unbiased-pad completion fails J-ii only; a static carrier input fails J-i only (row 1)")
    def _():
        pad = _st_tuple(1, "st-pad", "st-pad-ring", "window", 1, ["z0"],
                        {"type": "explicit", "states": {"000": "1/4", "010": "1/4", "101": "1/4", "111": "1/4"}},
                        ["a"], "01")
        models = dict(ST_MODELS)
        models["st-pad-ring"] = {"cells": ["a", "z0", "z1"], "rule": [
            [{"lhs": "a", "rhs": "a ^ z0"}], [{"lhs": "z0", "rhs": "z1"}, {"lhs": "z1", "rhs": "z0"}]]}
        models["st-static"] = {"cells": ["c", "a"], "rule": [[{"lhs": "a", "rhs": "a ^ c"}]]}
        rec, _, _, _ = evaluate_tuple(_ctx(pad, models), "full")
        assert rec["J1"] == {"t0+1": {"Ji": True, "Jii": False}} and rec["row"] == "1", rec
        assert rec["eps_max"] == {"t0+1": "1/2", "t0+2": "0"}
        st = _st_tuple(1, "st-static", "st-static", "window", 1, ["c"],
                       {"type": "uniform_conditioned", "equalities": {"a": 0}}, ["a"], "01")
        rec, _, _, _ = evaluate_tuple(_ctx(st, models), "full")
        assert rec["J1"] == {"t0+1": {"Ji": False, "Jii": True}} and rec["row"] == "1", rec

    @check("sequential method: hand values and agreement with full enumeration (Toffoli channel)")
    def _():
        t = _st_tuple(1, "st-toffoli", "st-toffoli-channel", "window", 2, ["p0", "v0"],
                      {"type": "uniform_conditioned", "equalities": {"r": 0}}, ["r"], "01", params={"L": 3},
                      P=("10", "11"))
        ctx = _ctx(t)
        rf, ef, _, _ = evaluate_tuple(ctx, "full")
        rs, es, _, _ = evaluate_tuple(ctx, "sequential")
        rb, eb, _, _ = evaluate_tuple(ctx, "full+sequential")
        for rec in (rf, rs, rb):
            assert rec["row"] == "2b" and rec["tau"] == 1 and rec["T_prime"] == 2
            assert rec["eps_max"] == {"t0+1": "0", "t0+2": "1/4", "t0+3": "3/8"}
            assert rec["tv"] == {"t0+1": "1", "t0+2": "1/2", "t0+3": "1/4"}
            assert rec["eta"] == {"t0+1": "1/4", "t0+2": "1/4"}
            assert rec["lemma_h_bound"] == {"t0+1": "0", "t0+2": "1/4", "t0+3": "1/2"}
            assert rec["G_star_out_T"] == ["11"] and rec["G_status_T"] == "consistent" and rec["Q_missing_T"] == []
            assert rec["dil_exact_T"] is False and rec["SCH"] == {"t0+1": True, "t0+2": True} and rec["D_bits"] == 1
        assert eb["sequential_check"]["agree"] and es["injective"] is None and ef["injective"] is True

    @check("sequential conditions: a re-entering cell and a non-product law exit 5; disagreement exits 5")
    def _():
        t = _st_tuple(1, "st-toffoli-L2", "st-toffoli-channel", "window", 2, ["p0", "v0"],
                      {"type": "uniform_conditioned", "equalities": {"r": 0}}, ["r"], "01", params={"L": 2},
                      P=("10", "11"))
        h = _expect_halt(5, lambda: evaluate_tuple(_ctx(t), "sequential"))
        assert "more than once" in h.detail
        t3 = _st_tuple(1, "st-toffoli-corr", "st-toffoli-channel", "window", 2, ["p0", "v0"],
                       {"type": "explicit", "states": {"1000000": "1/2", "1100001": "1/2"}}, ["r"], "01",
                       params={"L": 3}, P=("10", "11"))
        h = _expect_halt(5, lambda: evaluate_tuple(_ctx(t3), "sequential"))
        assert "product" in h.detail
        t4 = dict(t3, law={"type": "uniform"})

        def corrupt(rec, extra):
            rec["eps_max"] = dict(rec["eps_max"], **{"t0+2": "1/3"})
        h = _expect_halt(5, lambda: evaluate_tuple(_ctx(t4), "full+sequential", seq_hook=corrupt))
        assert h.field == "eps_max"
        st = dict(t4, model="st-swap1", Sigma=["a"], A=["b"], P=["0", "1"])
        st["read_cells"] = ["b"]
        _expect_halt(5, lambda: evaluate_tuple(_ctx(dict(st, mode="readback", T=None, readback_ticks=["t0+1"])),
                                               "sequential"))

    @check("D_bits: exact integer test of log2|S| - H(mu)")
    def _():
        m = Model({"cells": ["a", "b", "c", "d"], "rule": []}, {}, "m")
        assert d_bits({"type": "uniform"}, m, "l") == 0
        assert d_bits({"type": "uniform_conditioned", "equalities": {"a": 0, "c": 1}}, m, "l") == 2
        assert d_bits({"type": "explicit", "states": {"0000": "1/4", "1000": "1/4", "0100": "1/2"}}, m, "l") is None
        assert d_bits({"type": "explicit", "states": {"0000": "1/8", "1000": "1/8", "0100": "1/4", "1100": "1/2"}},
                      m, "l") is None
        assert d_bits({"type": "explicit", "states": {"0000": "1/2", "1000": "1/4", "0100": "1/8",
                                                      "1100": "1/16", "0010": "1/16"}}, m, "l") is None
        assert d_bits({"type": "explicit", "states": {"0000": "1/4", "1000": "1/4", "0100": "1/4", "1100": "1/4"}},
                      m, "l") == 2
        # a nonuniform law with H = 1/2 + 4 * 3/8 = 2 bits exactly
        assert d_bits({"type": "explicit", "states": {"0000": "1/2", "1000": "1/8", "0100": "1/8", "1100": "1/8",
                                                      "0010": "1/8"}}, m, "l") == 2

    @check("row precedence: steps 1-8 in order, exact <= at eps*, exit 4 only at step 6")
    def _():
        ok, no = (True, True), (False, True)
        z, h, big = Fraction(0), Fraction(1, 20), Fraction(1, 2)
        base = dict(mode="window", T=1, tau=INF, J1={1: ok}, eps={1: z, 2: z}, Ra=True, Rb=True, dil=True,
                    G_status_T="consistent", G_T_empty=False, G_Tp_empty=False, bound={1: z, 2: z}, sch={1: True})

        def row(**kw):
            a = dict(base)
            a.update(kw)
            return assign_row(**a)[0]
        assert row() == "5" and row(sch={1: False}) == "6"
        assert row(J1={1: no, 2: ok}, tau=1, eps={1: z, 2: big}) == "1"           # step 2 before step 3
        assert row(J1={1: ok, 2: no}, tau=2, eps={1: z, 2: z, 3: z}) == "1"       # row 1 on H_T' \ H_T
        assert row(tau=1, eps={1: z, 2: big}, Ra=False, G_Tp_empty=True) == "2a"  # step 3 before step 4
        assert row(tau=1, eps={1: z, 2: big}, Rb=False) == "2b"
        assert row(eps={1: z, 2: big}) == "3" and row(Ra=False) == "3" and row(Rb=False) == "3"
        assert row(eps={1: h, 2: h}, bound={1: h, 2: h}) == "5"                    # eps = eps* is not a failure
        assert row(dil=False, bound={1: z, 2: h}) == "5"                           # DIL-eta storage at the boundary
        assert row(dil=False, bound={1: z, 2: Fraction(1, 10)}) == "7"
        assert row(dil=False, eps={1: h, 2: z}, bound={1: h, 2: Fraction(1, 10)}) == "8"
        assert row(dil=False, G_T_empty=True, G_status_T="empty", bound={1: z, 2: Fraction(1)}) == "7"
        _expect_halt(4, lambda: row(dil=False, G_status_T="inconsistent", bound=None))
        assert row(G_status_T="inconsistent", bound=None, tau=1, eps={1: z, 2: big}) == "2b"  # no exit 4 before 6
        assert row(G_status_T="inconsistent", bound=None, Ra=False) == "3"
        nx = dict(mode="noext", tau=3, eps={1: z, 2: z})
        assert row(**nx) == "I-9" and assign_row(**dict(base, **nx))[2] is None
        assert row(J1={1: no}, **nx) == "1"                                        # noext row 1 before I-9
        assert row(mode="noext", tau=1, eps={1: z, 2: big}, G_Tp_empty=True) == "2a"

    @check("re-application detects an altered row, a bad flag set and T_prime errors")
    def _():
        tdoc, edoc = _st_docs()
        ctx = _ctx(tdoc["tuples"][0])
        rec, _, _, _ = evaluate_tuple(ctx, "full")
        rec = dict(rec, mode="window", T=1)
        assert reapply(rec)[1] == []
        assert reapply(dict(rec, row="6"))[1]
        assert reapply(dict(rec, recurrence_flags=["t0+2"]))[1]
        assert reapply(dict(rec, T_prime=2))[1]
        flagged = dict(rec, eps_max={"t0+1": "1/2", "t0+2": "0"}, recurrence_flags=["t0+2"])
        assert any("row 5 or 6" in p for p in reapply(flagged)[1])

    @check("end-to-end run on synthetic docs: PASS, exit 1, exit 2, exit 5; verdict text regenerates")
    def _():
        tdoc, edoc = _st_docs()
        ids = [t["id"] for t in tdoc["tuples"]]
        with tempfile.TemporaryDirectory() as d:
            code = run(d, _b(tdoc), _b(edoc), meta, runm, expect_count=5, frozen_order_rule=False)
            s = json.load(open(os.path.join(d, "phase-a", "summary.json")))
            assert code == 0 and s["verdict"] == "PASS" and s["tuples_evaluated"] == ids, s["first_failure"]
            assert s["verdict_text"] == "Phase A: all 5 frozen tuples reproduced their expected rows and values."
            ok, rep = check_summary(d, ids, expect_count=5)
            assert ok, rep
            s["verdict_text"] += " "
            write_json(os.path.join(d, "phase-a", "summary.json"), s)
            assert not check_summary(d, ids, expect_count=5)[0]
        e2 = json.loads(json.dumps(edoc))
        e2["expected"]["st-shift1"]["eps_max"]["t0+2"] = "1/4"
        with tempfile.TemporaryDirectory() as d:
            code = run(d, _b(tdoc), _b(e2), meta, runm, expect_count=5, frozen_order_rule=False)
            s = json.load(open(os.path.join(d, "phase-a", "summary.json")))
            assert code == 1 and s["tuples_evaluated"] == ids[:3] and s["first_failure"]["field"] == "eps_max"
            assert s["verdict_text"] == ('Phase A halted at st-shift1: eps_max expected {"t0+1":"0","t0+2":"1/4"}, '
                                         'computed {"t0+1":"0","t0+2":"1/2"}. The run is void.')
            assert check_summary(d, ids, expect_count=5)[0]
        e3 = json.loads(json.dumps(edoc))
        del e3["expected"]["st-swap"]["tau"]
        with tempfile.TemporaryDirectory() as d:
            assert run(d, _b(tdoc), _b(e3), meta, runm, expect_count=5, frozen_order_rule=False) == 2
            s = json.load(open(os.path.join(d, "phase-a", "summary.json")))
            assert s["tuples_evaluated"] == [] and s["verdict_text"].startswith("Phase A halted at start: schema")
        e4 = json.loads(json.dumps(edoc))
        e4["expected"]["st-hold"]["eps_max"]["t0+1"] = 0.0
        with tempfile.TemporaryDirectory() as d:
            assert run(d, _b(tdoc), json.dumps(e4).encode(), meta, runm, expect_count=5, frozen_order_rule=False) == 2
        t5 = json.loads(json.dumps(tdoc))
        t5["tuples"][1]["model"] = "st-collapse"
        t5["tuples"][1].update({"Sigma": ["a"], "A": ["b"], "read_cells": ["b"], "g": "01",
                                "law": {"type": "uniform"}})
        with tempfile.TemporaryDirectory() as d:
            assert run(d, _b(t5), _b(edoc), meta, runm, expect_count=5, frozen_order_rule=False) == 5
            s = json.load(open(os.path.join(d, "phase-a", "summary.json")))
            assert s["tuples_evaluated"] == ids[:2] and s["first_failure"]["tuple_id"] == "st-swap"
            assert s["verdict_text"] == ("Phase A halted at st-swap: enumeration-method check failed "
                                         "(phi is not injective on S). The run is void.")
        with tempfile.TemporaryDirectory() as d:
            assert run(d, _b(tdoc), _b(edoc), meta, runm, expect_count=49) == 2

    @check("verdict text templates for exits 2, 4 and other")
    def _():
        mk = lambda **ff: {"verdict": "HALT", "tuples_frozen": 49, "first_failure": ff}
        assert render_verdict(mk(exit=2, tuple_id=None, field="eps_max")) == \
            "Phase A halted at start: schema violation in eps_max. The run is void."
        assert render_verdict(mk(exit=4, tuple_id="x")) == \
            "Phase A halted at x: G* undetermined on W_T at storage step. The run is void."
        assert render_verdict(mk(exit=7, tuple_id="x")) == "Phase A halted with exit 7. The run is void."

    ok = all(c["ok"] for c in checks)
    print(json.dumps({"self_test": "pass" if ok else "fail", "checks": checks}, indent=1))
    return 0 if ok else 1


# ----------------------------------------------------------------------------------------------
# Command line
# ----------------------------------------------------------------------------------------------

def _verify(expect_f):
    if expect_f is not None and expect_f != F_COMMIT:
        raise Halt(3, detail="F given to the tool (%s) differs from its constant" % expect_f)
    repo = repo_root()
    return repo, check_frozen_inputs(repo)


def main(argv=None):
    ap = argparse.ArgumentParser(description="O-RET Phase A: exact replay of the pulse-design controls "
                                             "(PREREG-PHASE-A.md, frozen at F = %s)." % F_COMMIT)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--self-test", action="store_true", help="synthetic cases only; exit 0 iff all pass")
    g.add_argument("--verify-inputs", action="store_true",
                   help="hash-check the four frozen inputs against their git blob ids at F (exit 0 or 3)")
    g.add_argument("--run", action="store_true", help="the preregistered run (CI only, PREREG section 7)")
    g.add_argument("--check-summary", metavar="DIR",
                   help="regenerate verdict_text from DIR/phase-a/summary.json and re-apply section 4")
    ap.add_argument("--out", metavar="DIR", help="output directory for --run (files under DIR/phase-a/)")
    ap.add_argument("--expect-F", metavar="SHA", help="the F constant carried by the workflow; must equal the tool's")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test()
    if a.verify_inputs:
        try:
            _, (meta, _) = _verify(a.expect_F)
            print(json.dumps({"verify_inputs": "match", "F": F_COMMIT, "frozen_inputs": meta}, indent=1))
            return 0
        except Halt as h:
            print(json.dumps({"verify_inputs": "mismatch", "F": F_COMMIT, "detail": h.detail,
                              "frozen_inputs": h.frozen_inputs}, indent=1))
            return 3
    if a.check_summary:
        try:
            repo, (meta, data) = _verify(a.expect_F)
            tdoc = load_json_bytes(data[TUPLES_PATH], "PHASEA-TUPLES.json")
            order_ids = [t["id"] for t in sorted(tdoc["tuples"], key=lambda t: t["order"])]
        except (Halt, KeyError, TypeError) as ex:
            print(json.dumps({"check_summary": "fail", "detail": str(ex)}))
            return 1
        ok, report = check_summary(a.check_summary, order_ids)
        try:
            write_json(os.path.join(a.check_summary, "phase-a", "check.json"), report)
        except (OSError, Halt):
            ok = False
        print(json.dumps(report, indent=1))
        return 0 if ok else 1
    if not a.out:
        ap.error("--run needs --out DIR")
    repo = None
    try:
        repo, (meta, data) = _verify(a.expect_F)
    except Halt as h:
        runm = run_info(repo) if repo else {"F": F_COMMIT, "commit": None, "run_attempt": None}
        summary = {"schema": SUMMARY_SCHEMA, "tuples_frozen": TUPLES_FROZEN, "tuples_evaluated": [],
                   "first_failure": h.failure(), "verdict": "HALT", "exit": 3, "eps_star": "1/20",
                   "w_star": None, "T_star": None, "run": runm, "frozen_inputs": h.frozen_inputs or [],
                   "tuples": []}
        summary["verdict_text"] = render_verdict(summary)
        write_json(os.path.join(a.out, "phase-a", "summary.json"), summary)
        return 3
    return run(a.out, data[TUPLES_PATH], data[EXPECTED_PATH], meta, run_info(repo))


if __name__ == "__main__":
    sys.exit(main())
