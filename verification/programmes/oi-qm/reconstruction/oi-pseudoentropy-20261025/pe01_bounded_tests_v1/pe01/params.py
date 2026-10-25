"""Fixed parameters and the TH and PIN checkpoints (PLAN.md §5; amendment A1).

TH reads A1's machine-readable `pe01-parameters` block, cross-checks every formula against its
per-n values, compares the block with the parameters this code runs with, records A1's blob id and
checks that A1's commit is an ancestor of the run commit. PIN records PLAN.md's blob id and checks
that the plan commit is an ancestor of the run commit and of every commit that touches the code.
A run refuses to start on any failure.
"""
import json
import os
import re
import subprocess

PKG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REL = "verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe01_bounded_tests_v1"
PLAN_PATH = REL + "/PLAN.md"
A1_PATH = REL + "/amendments/A1-owner-decisions.md"
PLAN_COMMIT = "af38dc2dde0fbdd190a67debf700ab5c370f92d9"   # revision 5, the plan A1 amends
A1_COMMIT = "1e025b672bdeb56e52f32d668f46320e8c4be06e"     # carries A1's final blob
# Amendment A2 resolves the open items of pending.py. It does not exist yet; when it lands, the
# commit carrying its final blob is pinned here, exactly as A1 is.
A2_PATH = REL + "/amendments/A2-open-items.md"
A2_COMMIT = None
CODE_PATHS = [REL + "/pe01", REL + "/verdict.py", REL + "/run.py", ".github/workflows/pe01-bounded-tests.yml"]

# --- the parameters this code runs with (TH compares them with A1's block) ---
NS = (3, 4, 5, 6, 7, 8)
LP_NS = (3, 4, 5, 6)
RUN = {
    "amendment": "A1",
    "theta": "n+1",
    "K_LP": "2^(n-1)-1",
    "m3_passive_scope": "ii",
    "m3_passive_K_cap": {"7": 15, "8": 31},
}


def theta(n):
    return n + 1


def k_lp(n):
    assert n in LP_NS
    return (1 << (n - 1)) - 1


def m3_cap(n, kmax):
    return {7: 15, 8: 31}.get(n, kmax)


def k_max(n):
    return 4 * ((1 << n) - 1)


DELTAS = ("1/8", "1/4")
DELTA_CX = "1/8"
W = 3
K_TAPE = 20
K_TAPE_EMB = 12
K0_CAP_M2 = 255


# ---------------------------------------------------------------- formula evaluation

_TOK = re.compile(r"\s*(?:(\d+)|(n)|([-+^()]))")


def eval_formula(expr, n):
    """Evaluate an integer formula in n with + - ^ and parentheses (^ is exponentiation)."""
    toks = []
    pos = 0
    while pos < len(expr):
        mt = _TOK.match(expr, pos)
        if not mt or mt.end() == pos:
            raise ValueError("bad formula %r" % expr)
        toks.append(mt.group(1) or mt.group(2) or mt.group(3))
        pos = mt.end()
    toks = [t for t in toks if t]
    i = 0

    def atom():
        nonlocal i
        t = toks[i]
        if t == "(":
            i += 1
            v = add()
            assert toks[i] == ")"
            i += 1
            return v
        if t == "n":
            i += 1
            return n
        if t == "-":
            i += 1
            return -atom()
        i += 1
        return int(t)

    def power():
        nonlocal i
        b = atom()
        if i < len(toks) and toks[i] == "^":
            i += 1
            e = power()
            return b ** e
        return b

    def add():
        nonlocal i
        v = power()
        while i < len(toks) and toks[i] in "+-":
            op = toks[i]
            i += 1
            r = power()
            v = v + r if op == "+" else v - r
        return v

    v = add()
    if i != len(toks):
        raise ValueError("trailing tokens in %r" % expr)
    return v


# ---------------------------------------------------------------- git helpers

def git(*args, root=None):
    r = subprocess.run(["git"] + list(args), cwd=root or repo_root(), capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("git %s: %s" % (" ".join(args), r.stderr.strip()))
    return r.stdout.strip()


def git_ok(*args):
    r = subprocess.run(["git"] + list(args), cwd=repo_root(), capture_output=True, text=True)
    return r.returncode == 0


def repo_root():
    r = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=PKG, capture_output=True, text=True)
    return r.stdout.strip()


def head():
    return git("rev-parse", "HEAD")


def blob_at(commit, path):
    return git("rev-parse", "%s:%s" % (commit, path))


def worktree_blob(path):
    return git("hash-object", os.path.join(repo_root(), path))


def is_ancestor(a, b):
    return git_ok("merge-base", "--is-ancestor", a, b)


# ---------------------------------------------------------------- TH

BLOCK = re.compile(r"```json pe01-parameters\n(.*?)\n```", re.S)
RES_BLOCK = re.compile(r"```json pe01-resolutions\n(.*?)\n```", re.S)


def parse_block(text):
    m = BLOCK.search(text)
    if not m:
        raise ValueError("TH: the pe01-parameters block cannot be read")
    return json.loads(m.group(1))


def th_check(text=None):
    """TH. Returns (ok, record). text: A1's content (default: the working tree file)."""
    rec = {"checkpoint": "TH", "reasons": []}
    try:
        if text is None:
            text = open(os.path.join(repo_root(), A1_PATH), encoding="utf-8").read()
        blk = parse_block(text)
    except Exception as e:  # unreadable block refuses the run
        rec["reasons"].append("block unreadable: %s" % e)
        rec["pass"] = False
        return False, rec
    rec["block"] = blk
    bad = rec["reasons"]
    for n_s, v in sorted(blk.get("theta_by_n", {}).items()):
        if eval_formula(blk["theta"], int(n_s)) != v:
            bad.append("theta formula disagrees with theta_by_n at n=%s" % n_s)
    if sorted(int(k) for k in blk.get("theta_by_n", {})) != list(NS):
        bad.append("theta_by_n does not cover n = 3..8")
    for n_s, v in sorted(blk.get("K_LP_by_n", {}).items()):
        if eval_formula(blk["K_LP"], int(n_s)) != v:
            bad.append("K_LP formula disagrees with K_LP_by_n at n=%s" % n_s)
    if sorted(int(k) for k in blk.get("K_LP_by_n", {})) != list(LP_NS):
        bad.append("K_LP_by_n does not cover n = 3..6")
    # the parameters this code runs with must equal the block
    for k, v in RUN.items():
        if blk.get(k) != v:
            bad.append("run parameter %s=%r differs from the block (%r)" % (k, v, blk.get(k)))
    for n in NS:
        if blk["theta_by_n"].get(str(n)) != theta(n):
            bad.append("code theta(%d) differs from the block" % n)
    for n in LP_NS:
        if blk["K_LP_by_n"].get(str(n)) != k_lp(n):
            bad.append("code K_LP(%d) differs from the block" % n)
    for n_s, cap in blk.get("m3_passive_K_cap", {}).items():
        if m3_cap(int(n_s), None) != cap:
            bad.append("code m=3 cap at n=%s differs from the block" % n_s)
    rec["theta_by_n"] = blk.get("theta_by_n")
    rec["K_LP_by_n"] = blk.get("K_LP_by_n")
    rec["m3_passive_scope"] = blk.get("m3_passive_scope")
    rec["m3_passive_K_cap"] = blk.get("m3_passive_K_cap")
    rec["pass"] = not bad
    return not bad, rec


def th_git(rec):
    """TH's provenance part: A1's blob at HEAD equals its blob at A1_COMMIT, which is an ancestor."""
    h = head()
    b_head = blob_at(h, A1_PATH)
    b_frozen = blob_at(A1_COMMIT, A1_PATH)
    b_tree = worktree_blob(A1_PATH)
    rec["a1_blob"] = b_head
    rec["a1_commit"] = A1_COMMIT
    anc = is_ancestor(A1_COMMIT, h)
    rec["a1_commit_is_ancestor"] = anc
    if b_head != b_frozen or b_tree != b_head:
        rec["reasons"].append("A1 blob changed since %s" % A1_COMMIT[:8])
    if not anc:
        rec["reasons"].append("A1 commit is not an ancestor of the run commit")
    rec["pass"] = rec["pass"] and not rec["reasons"]
    return rec


def pin_check():
    """PIN: PLAN.md's blob is unchanged since the plan commit, which is an ancestor of the run
    commit and of every commit touching the code."""
    h = head()
    rec = {"checkpoint": "PIN", "reasons": [], "run_commit": h, "run_tree": git("rev-parse", "HEAD^{tree}")}
    b_head = blob_at(h, PLAN_PATH)
    b_plan = blob_at(PLAN_COMMIT, PLAN_PATH)
    rec["plan_blob"] = b_head
    rec["plan_commit"] = PLAN_COMMIT
    if b_head != b_plan or worktree_blob(PLAN_PATH) != b_head:
        rec["reasons"].append("PLAN.md changed since the plan commit")
    if not is_ancestor(PLAN_COMMIT, h):
        rec["reasons"].append("plan commit is not an ancestor of the run commit")
    code_commits = git("rev-list", "HEAD", "--", *CODE_PATHS).split()
    rec["code_commits"] = len(code_commits)
    for c in code_commits:
        if not is_ancestor(PLAN_COMMIT, c) or c == PLAN_COMMIT:
            rec["reasons"].append("code commit %s does not descend from the plan commit" % c[:8])
    dirty = git("status", "--porcelain", "--", *CODE_PATHS, PLAN_PATH, A1_PATH)
    rec["code_tree_clean"] = dirty == ""
    rec["pass"] = not rec["reasons"]
    return rec


def a2_check(mode):
    """A2's resolutions. result mode: only a pinned A2 (A2_COMMIT set, blob unchanged, an ancestor of
    the run commit, A1's commit an ancestor of it) resolves items. test mode: a local stub named by
    the environment variable PE01_TEST_A2, recorded as an unpinned stub (never a result)."""
    from . import pending
    rec = {"checkpoint": "TH-A2", "reasons": [], "resolutions": {}, "a2_blob": None, "a2_commit": A2_COMMIT}
    text = None
    if mode == "test":
        p = os.environ.get("PE01_TEST_A2")
        if not p:
            rec["reasons"].append("test mode needs PE01_TEST_A2")
        else:
            text = open(p, encoding="utf-8").read()
            rec["source"] = "unpinned local stub (test mode)"
            rec["a2_blob"] = git("hash-object", p)
    elif A2_COMMIT is not None:
        h = head()
        b_head = blob_at(h, A2_PATH)
        if b_head != blob_at(A2_COMMIT, A2_PATH) or worktree_blob(A2_PATH) != b_head:
            rec["reasons"].append("A2 blob changed since %s" % A2_COMMIT[:8])
        if not is_ancestor(A2_COMMIT, h) or not is_ancestor(A1_COMMIT, A2_COMMIT):
            rec["reasons"].append("A2 commit ancestry fails")
        rec["a2_blob"] = b_head
        rec["source"] = "pinned"
        text = open(os.path.join(repo_root(), A2_PATH), encoding="utf-8").read()
    elif os.path.exists(os.path.join(repo_root(), A2_PATH)):
        rec["reasons"].append("A2 exists but is not pinned in params.A2_COMMIT")
    if text is not None:
        m = RES_BLOCK.search(text)
        if not m:
            rec["reasons"].append("A2: the pe01-resolutions block cannot be read")
        else:
            blk = json.loads(m.group(1))
            if blk.get("amendment") != "A2":
                rec["reasons"].append("A2 block does not name amendment A2")
            rec["resolutions"] = blk.get("resolves", {})
    rec["open_items"] = pending.open_items(rec["resolutions"])
    rec["pass"] = not rec["reasons"]
    return rec


def preflight(mode):
    """TH (A1 and A2) and PIN together. Result and test modes also refuse on a dirty code tree."""
    ok, th = th_check()
    th = th_git(th)
    a2 = a2_check(mode)
    th["A2"] = a2
    pin = pin_check()
    reasons = list(th["reasons"]) + list(a2["reasons"]) + list(pin["reasons"])
    if mode in ("result", "test") and not pin["code_tree_clean"]:
        reasons.append("code tree not clean at the run commit")
    if mode in ("result", "test") and a2["open_items"]:
        reasons.append("open plan items without an amendment: %s" % ", ".join(a2["open_items"]))
    th["pass"] = th["pass"] and a2["pass"]
    return {"TH": th, "PIN": pin, "pass": not reasons, "reasons": reasons}
