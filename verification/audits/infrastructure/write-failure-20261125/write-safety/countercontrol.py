"""Countercontrols. Run: python3 -I countercontrol.py

C1  the real edit.py (evidence copy), its gh() replaced by the mock transport, under the D1
    behaviour: the no-subsequent-write predicate must report a violation.
C2  the near-miss shell sequence with an empty commit id, against a fake git that only records
    its arguments: the refspec produced must be a deletion, and the gate must refuse it.
C3  mutations of the gate (halt that prints and continues, as edit.py did; halt check removed;
    refspec check removed): the control suite must fail under each.
"""
import io, json, os, shutil, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gate as G
from mock import MockGitHub, MockGit

EV = os.path.join(HERE, "ev")
ORDER = [1558, 1565, 1062, 1245, 1556]
results = {}


def read(p):
    return open(p, encoding="utf-8", newline="").read()


def writes_after_first_mismatch(events):
    """Predicate used by the controls: number of writes after the first read-back mismatch."""
    seen = None
    for i, e in enumerate(events):
        if e == "mismatch" and seen is None:
            seen = i
    if seen is None:
        return 0
    return sum(1 for e in events[seen + 1:] if e.startswith("write"))


def c1():
    before = {n: {"number": n, "title": "t", "labels": [], "state": "open",
                  "body": read(os.path.join(EV, "bodies", "%d.before.md" % n))} for n in ORDER}
    sent = {n: read(os.path.join(EV, "bodies", "%d.sent.md" % n)) for n in ORDER}
    mock = MockGitHub(before, mode="append_if_absent")
    events = []

    def gh(*a, inp=None):          # replaces edit.py's subprocess call to gh api
        method, path = "GET", a[-1]
        if "-X" in a:
            method = a[a.index("-X") + 1]
            path = a[a.index("-X") + 2]
        payload = json.loads(inp) if inp else None
        if method != "GET":
            events.append("write %s %s" % (method, path))
        status, obj = mock.request(method, path.replace("%20", " ").replace("%3A", ":"), payload)
        if isinstance(obj, dict) and "number" in obj and method == "GET":
            obj = dict(obj)
        return json.dumps(obj)

    ns = {"__name__": "edit_under_mock"}
    src = read(os.path.join(EV, "edit.py"))
    exec(compile(src, "edit.py", "exec"), ns)
    ns["gh"] = gh
    work = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
    os.makedirs(os.path.join(work, "<scratch>", "blocks"))
    cwd = os.getcwd(); os.chdir(work)
    out = io.StringIO(); real = sys.stdout; sys.stdout = out
    try:
        for n in ORDER:            # the driver called edit() once per Issue, in this order
            ns["edit"](n, [(before[n]["body"], sent[n])], add=("label-x",))
    finally:
        sys.stdout = real; os.chdir(cwd)
    for line in out.getvalue().splitlines():
        if "body match False" in line:
            events.insert(_index_after_write(events, int(line.split()[0])), "mismatch")
    v = writes_after_first_mismatch(events)
    results["C1"] = {"edit_py_writes_total": sum(e.startswith("write") for e in events),
                     "writes_after_first_mismatch": v,
                     "printed": out.getvalue().splitlines()[:2],
                     "predicate_reports_violation": v > 0}
    # Same scenario through the gate: one write, then halt.
    mock2 = MockGitHub(before, mode="append_if_absent")
    d = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
    g = G.Gate(mock2, MockGit(), os.path.join(d, "HALT"), "o/r",
               {"issue.edit_body": {"validated": True, "send_form": None}})
    try:
        G.run_plan(g, [("w", "issue.edit_body", n, {"body": sent[n]}) for n in ORDER])
    except G.Halted:
        pass
    results["C1_gate"] = {"writes": len(mock2.writes)}
    return v > 0 and len(mock2.writes) == 1


def _index_after_write(events, n):
    for i, e in enumerate(events):
        if e.startswith("write PATCH") and e.endswith("/issues/%d" % n):
            return i + 1
    raise AssertionError("no PATCH for %d" % n)


def c2():
    d = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
    fake = os.path.join(d, "bin"); os.makedirs(fake)
    log = os.path.join(d, "argv.log")
    with open(os.path.join(fake, "git"), "w") as f:
        f.write("#!/bin/sh\nfor a in \"$@\"; do printf '%%s\\n' \"$a\"; done > %s\nexit 0\n" % log)
    os.chmod(os.path.join(fake, "git"), 0o755)
    sh = 'c=$(false); git push origin "$c:refs/heads/evidence/x"'   # earlier step failed
    subprocess.run(["sh", "-c", sh], env={"PATH": fake + ":/usr/bin:/bin"}, check=True)
    argv = open(log).read().splitlines()
    refspec = argv[-1]
    viol = G.check_refspec(refspec, ("refs/heads/evidence/x",))
    git = MockGit()
    g = G.Gate(MockGitHub(), git, os.path.join(d, "HALT"), "o/r", {}, ("refs/heads/evidence/x",))
    try:
        g.push("origin", "", "refs/heads/evidence/x"); refused = False
    except G.Halted:
        refused = True
    results["C2"] = {"naive_argv": argv, "refspec_is_deletion": refspec.startswith(":"),
                     "check_refspec": viol, "gate_refused": refused, "gate_git_runs": git.runs}
    return refspec == ":refs/heads/evidence/x" and viol and refused and git.runs == []


def run_suite():
    import test_gate
    for p in os.listdir(os.path.join(HERE, "runs")):
        pass
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_gate)
    r = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    return r.testsRun, len(r.failures) + len(r.errors), \
        sorted(t.id().split(".")[-1] for t, _ in r.failures + r.errors)


def c3():
    out = {}
    baseline = run_suite()
    out["baseline"] = baseline
    orig_halt, orig_clear, orig_ref = G.Gate._halt, G.Gate._check_clear, G.check_refspec

    def print_and_continue(self, reason, **ev):
        print("MISMATCH (continuing):", reason, file=io.StringIO())
    mutants = {
        "halt_prints_and_continues": ("_halt", print_and_continue),
        "halt_check_removed": ("_check_clear", lambda self: None),
        "refspec_check_removed": ("check_refspec", lambda r, a: []),
    }
    for name, (attr, fn) in mutants.items():
        if attr == "check_refspec":
            G.check_refspec = fn
        else:
            setattr(G.Gate, attr, fn)
        try:
            out[name] = run_suite()
        finally:
            G.Gate._halt, G.Gate._check_clear, G.check_refspec = orig_halt, orig_clear, orig_ref
    results["C3"] = {k: {"run": v[0], "failed": v[1], "failing": v[2]} for k, v in out.items()}
    return baseline[1] == 0 and all(out[k][1] > 0 for k in mutants)


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    ok = {"C1": c1(), "C2": c2(), "C3": c3()}
    print(json.dumps({"pass": ok, "detail": results}, indent=1))
    sys.exit(0 if all(ok.values()) else 1)
