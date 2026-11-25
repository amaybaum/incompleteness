"""Countercontrols for gate2. Mock transport only. Run: python3 -I -B countercontrol2.py

C1  gate.py (exact only) halts on the real #1505 and #1558 pairs; gate2 accepts each as
    "permitted footer-attribution-1" with a discrepancy record. Same for the five-body D1 replay.
C2  mutations of the rule (looser variants of footer-attribution-1): under each, the control suite
    must fail, and at least one negative control (test_neg_*) must be among the failures.
C3  mutations of gate2's outcome handling and containment: accept "rejected"; skip the
    discrepancy record; a single global marker for every halt; no run-level latch (a caller that
    catches Halted continues the sequence); every halt confined to its operation (the containment
    of gate v2 before revision r2); narrowing without the tail-confinement condition. The control
    suite must fail under each, and under the latch mutant the run-level tests must be among the
    failures.
"""
import dataclasses, io, json, os, re, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gate as G
import gate2 as G2
import transport_rules as TR
from mock2 import MockGitHub2, MockGit

EV = os.path.join(HERE, "ev")
CORE = TR.FOOTER_CORE
results = {}


def read(*p):
    with open(os.path.join(EV, *p), encoding="utf-8", newline="") as f:
        return f.read()


def reg():
    return {"issue.edit_body": {"validated": True, "send_form": None}}


def c1():
    pairs = {"1505": (read("issue-1505", "sent.md"), read("issue-1505", "stored.md")),
             "1558": (read("bodies", "1558.sent.md"), read("bodies", "1558.stored.md"))}
    out, ok = {}, True
    for name, (sent, stored) in pairs.items():
        issues = {1: {"number": 1, "title": "t", "body": "b", "labels": [], "state": "open"}}
        d = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
        gh1 = MockGitHub2(issues, transforms={"patch": lambda b, s=stored: s})
        g1 = G.Gate(gh1, MockGit(), os.path.join(d, "HALT"), "o/r", reg())
        try:
            g1.write("issue.edit_body", 1, {"body": sent}); v1 = "accepted"
        except G.Halted as e:
            v1 = "halted: " + str(e)
        d2 = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
        gh2 = MockGitHub2(issues, transforms={"patch": lambda b, s=stored: s})
        g2 = G2.Gate2(gh2, MockGit(), d2, "o/r", reg())
        try:
            r = g2.write("issue.edit_body", 1, {"body": sent})
            with open(r.records[0], encoding="utf-8") as f:
                rec = json.load(f)
            v2 = {"outcome": r.outcomes["body"], "records": len(r.records),
                  "record_rule": [rec["rule_id"], rec["rule_version"]],
                  "record_sent_sha256": rec["sent_sha256"],
                  "record_stored_sha256": rec["stored_sha256"],
                  "record_texts_complete": rec["sent"] == sent and rec["stored"] == stored,
                  "unified_diff": rec["unified_diff"]}
        except G.Halted as e:
            v2 = "halted: " + str(e)
        out[name] = {"gate_v1": v1, "gate_v2": v2}
        ok &= v1.startswith("halted: read-back mismatch") and isinstance(v2, dict) \
            and v2["outcome"] == ["permitted", "footer-attribution-1"] and v2["records"] == 1 \
            and v2["record_texts_complete"]
    # D1 replay of the five evidence bodies under append-if-absent
    order = [1558, 1565, 1062, 1245, 1556]
    before = {n: {"number": n, "title": "t", "labels": [], "state": "open",
                  "body": read("bodies", "%d.before.md" % n)} for n in order}
    steps = [("w", "issue.edit_body", n, {"body": read("bodies", "%d.sent.md" % n)}) for n in order]
    m1 = MockGitHub2(before, mode="append_if_absent")
    g1 = G.Gate(m1, MockGit(), os.path.join(tempfile.mkdtemp(dir=os.path.join(HERE, "runs")),
                                            "HALT"), "o/r", reg())
    try:
        G.run_plan(g1, steps)
    except G.Halted:
        pass
    m2 = MockGitHub2(before, mode="append_if_absent")
    d = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
    g2 = G2.Gate2(m2, MockGit(), d, "o/r", reg())
    G2.run_plan(g2, steps)
    recs = sorted(p for p in os.listdir(d) if p.startswith("discrepancy"))
    out["D1_replay"] = {"gate_v1_writes": len(m1.writes), "gate_v2_writes": len(m2.writes),
                        "gate_v2_records": len(recs)}
    ok &= len(m1.writes) == 1 and len(m2.writes) == 5 and len(recs) == 4
    results["C1"] = out
    return ok


def run_suite():
    import importlib, test_gate2
    importlib.reload(test_gate2)
    suite = unittest.defaultTestLoader.loadTestsFromModule(test_gate2)
    r = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
    failing = sorted(set(t.id().split(".")[-1].split(" ")[0] for t, _ in r.failures + r.errors))
    return {"run": r.testsRun, "failed": len(failing), "failing": failing}


# -- rule mutants (each keeps the id and version, so only behaviour differs) -------------------
def _strip_footer_any(t, count=None):
    t = t.rstrip()
    n = 0
    while t.endswith(CORE) and (count is None or n < count):
        t = t[: -len(CORE)].rstrip(); n += 1
    return t, n


def m_strip_all_whitespace(s, t):
    cs, _ = _strip_footer_any(s, 1); ct, n = _strip_footer_any(t, 1)
    return n == 1 and re.sub(r"\s+", "", cs) == re.sub(r"\s+", "", ct)


def m_whole_text_strip(s, t):
    cs, _ = _strip_footer_any(s.strip(), 1); ct, n = _strip_footer_any(t.strip(), 1)
    return n == 1 and cs.strip() == ct.strip()


def m_ignore_footer_text(s, t):
    pat = re.compile(r"[ \t\n]*---\n_[^\n]*_[ \t\n]*\Z")
    ms, mt = pat.search(s), pat.search(t)
    cs = s[: ms.start()] if ms else s.rstrip(" \t\n")
    return bool(mt) and cs == t[: mt.start()]


def m_doubled_footer(s, t):
    cs, _ = _strip_footer_any(s); ct, n = _strip_footer_any(t)
    return n >= 1 and cs == ct


def m_ascii_whitespace_tail(s, t):
    """The first draft of the rule: spaces and tabs in the tail may differ too."""
    def split(x):
        t1 = x.rstrip(" \t\n")
        if t1.endswith(CORE):
            c = t1[: -len(CORE)].rstrip(" \t\n")
            if c and not c.endswith(CORE):
                return c, 1
        return t1, 0
    (cs, _), (ct, n) = split(s), split(t)
    return n == 1 and cs == ct


def m_no_separator_check(s, t):
    def split(x):
        t1 = x.rstrip("\n")
        if t1.endswith(CORE):
            c = t1[: -len(CORE)].rstrip("\n")
            if not c.endswith(CORE):
                return c, 1
        return t1, 0
    (cs, _), (ct, n) = split(s), split(t)
    return n == 1 and cs == ct


RULE_MUTANTS = {
    "strip_all_whitespace": m_strip_all_whitespace,
    "whole_text_strip": m_whole_text_strip,
    "ignore_footer_text": m_ignore_footer_text,
    "accept_doubled_footer": m_doubled_footer,
    "ascii_whitespace_tail": m_ascii_whitespace_tail,
    "no_separator_check": m_no_separator_check,
}


def c2():
    out = {"baseline": run_suite()}
    orig = TR.REGISTRY
    for name, fn in RULE_MUTANTS.items():
        TR.REGISTRY = (dataclasses.replace(orig[0], permits=fn),)
        try:
            out[name] = run_suite()
        finally:
            TR.REGISTRY = orig
    for name in RULE_MUTANTS:
        out[name]["negative_controls_failing"] = [t for t in out[name]["failing"]
                                                  if t.startswith("test_neg_")]
    results["C2"] = out
    return out["baseline"]["failed"] == 0 and all(out[n]["negative_controls_failing"]
                                                  for n in RULE_MUTANTS)


def c3():
    out = {}
    saved = {k: getattr(G2.Gate2, k) for k in
             ("_classify", "_record", "marker_path", "_check_sequence", "_halt",
              "_containment_scope")}

    def accept_rejected(self, op, field, sent, stored):
        cls, rid = TR.classify(sent, stored, self.rules, field)
        return ("exact", None) if cls == "rejected" else (cls, rid)

    def skip_record(self, *a):
        return None

    def global_only(self, mech):
        return self.halt_path

    def no_latch(self):
        return None

    def operation_scope_always(self, reason, scope=None, **ev):
        mech = self._mech if self._mech in G2.OPERATIONS else scope
        return saved["_halt"](self, reason, scope=mech, **ev)

    def narrow_without_tail_check(self, op, expected, stored, failures, other):
        if other or any(kind != "rejected" for _, kind in failures):
            return None
        outstanding = [n for n in self._operation_markers() if n != "HALT." + op]
        return None if outstanding else op

    mutants = {"accept_rejected": ("_classify", accept_rejected),
               "skip_discrepancy_record": ("_record", skip_record),
               "single_global_marker": ("marker_path", global_only),
               "no_run_level_latch": ("_check_sequence", no_latch),
               "operation_scope_always": ("_halt", operation_scope_always),
               "narrow_without_tail_check": ("_containment_scope", narrow_without_tail_check)}
    for name, (attr, fn) in mutants.items():
        setattr(G2.Gate2, attr, fn)
        try:
            out[name] = run_suite()
        finally:
            for k, v in saved.items():
                setattr(G2.Gate2, k, v)
            del G2._SEQUENCE_STOP[:]
    out["accept_rejected"]["negative_controls_failing"] = [
        t for t in out["accept_rejected"]["failing"] if t.startswith("test_neg_")]
    latch_tests = {"test_c1_run_level_latch_after_operation_level_halt",
                   "test_q3_caller_catching_halted_writes_nothing_further"}
    out["no_run_level_latch"]["run_level_tests_failing"] = sorted(
        latch_tests & set(out["no_run_level_latch"]["failing"]))
    results["C3"] = out
    return all(out[n]["failed"] > 0 for n in mutants) and \
        out["accept_rejected"]["negative_controls_failing"] and \
        out["no_run_level_latch"]["run_level_tests_failing"] == sorted(latch_tests)


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    ok = {"C1": bool(c1()), "C2": bool(c2()), "C3": bool(c3())}
    print(json.dumps({"pass": ok, "detail": results}, indent=1, ensure_ascii=False))
    sys.exit(0 if all(ok.values()) else 1)
