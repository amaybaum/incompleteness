"""Controls for the write gate. Mock transport only. Run: python3 -I test_gate.py"""
import json, os, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gate as G
from gate import FOOTER, Gate, Halted, run_plan
from mock import MockGitHub, MockGit

EV = os.path.join(HERE, "ev", "bodies")
REPO = "owner/repo"
SHA = "a" * 40
SHA2 = "b" * 40
ALLOWED = ("refs/heads/evidence/x",)


def registry(validated=True, form="footer"):
    return {op: {"validated": validated, "send_form": (form if spec["text"] else None)}
            for op, spec in G.OPERATIONS.items()}


def issues():
    return {n: {"number": n, "title": "T%d" % n, "body": "old %d" % n + FOOTER,
                "labels": [{"name": "a"}], "state": "open"} for n in (1, 2, 3, 4, 5)}


class Base(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
        self.marker = os.path.join(self.dir, "HALT")

    def gate(self, gh, git=None, reg=None):
        return Gate(gh, git or MockGit(), self.marker, REPO, reg or registry(), ALLOWED)

    def assertNoFurtherWrites(self, g, gh, git):
        """After a halt: every later write and push attempt raises and reaches no transport."""
        w, r = len(gh.writes), len(git.runs)
        self.assertTrue(os.path.exists(self.marker), "halt marker not written")
        with self.assertRaises(Halted):
            g.write("comment.create", 1, {"body": "x" + FOOTER})
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 2, {"body": "y" + FOOTER})
        with self.assertRaises(Halted):
            g.push("origin", SHA, ALLOWED[0])
        g2 = self.gate(gh, git)        # a fresh gate: a later process or session on this host
        with self.assertRaises(Halted):
            g2.write("labels.add", 3, {}, labels=["b"])
        self.assertEqual(len(gh.writes), w, "a write reached the transport after the halt")
        self.assertEqual(len(git.runs), r, "a push ran after the halt")


class Writes(Base):
    def test_01_verbatim_success(self):
        gh = MockGitHub(issues()); g = self.gate(gh)
        g.write("issue.edit_body", 1, {"body": "new" + FOOTER})
        g.write("comment.create", 1, {"body": "c" + FOOTER})
        self.assertEqual(len(gh.writes), 2)
        self.assertFalse(os.path.exists(self.marker))

    def test_02_mismatch_halts(self):
        gh = MockGitHub(issues(), mode="append_if_absent"); git = MockGit()
        g = self.gate(gh, git, registry(form="nofooter"))
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "no footer here"})
        self.assertEqual(len(gh.writes), 1)
        rec = json.load(open(self.marker))
        self.assertIn("read-back mismatch", rec["reason"])
        self.assertEqual(set(rec["evidence"]), {"sent", "stored"})
        self.assertNoFurtherWrites(g, gh, git)

    def test_03_d1_replay_stops_after_first(self):
        """Replay the five sent bodies of the evidence in edit.py's order under D1 behaviour."""
        order = [1558, 1565, 1062, 1245, 1556]
        sent = {n: open(os.path.join(EV, "%d.sent.md" % n), encoding="utf-8", newline="").read()
                for n in order}
        before = {n: {"number": n, "title": "t", "labels": [], "state": "open",
                      "body": open(os.path.join(EV, "%d.before.md" % n), encoding="utf-8",
                                   newline="").read()} for n in order}
        gh = MockGitHub(before, mode="append_if_absent"); git = MockGit()
        g = self.gate(gh, git, registry(form=None))   # no send-form rule: pure read-back test
        steps = [("w", "issue.edit_body", n, {"body": sent[n]}) for n in order]
        with self.assertRaises(Halted):
            run_plan(g, steps)
        self.assertEqual([p for _, p, _ in gh.writes], ["repos/%s/issues/1558" % REPO])
        stored = gh.issues[1558]["body"]
        self.assertEqual(stored, open(os.path.join(EV, "1558.stored.md"), encoding="utf-8",
                                      newline="").read(), "mock does not reproduce D1 bytes")
        self.assertNoFurtherWrites(g, gh, git)

    def test_04_readback_failure_halts(self):
        for mode in ("readback_fail_after_write", "readback_404"):
            self.setUp()
            gh = MockGitHub(issues(), mode=mode); git = MockGit(); g = self.gate(gh, git)
            with self.assertRaises(Halted):
                g.write("comment.create", 1, {"body": "c" + FOOTER})
            self.assertIn("read-back failed", json.load(open(self.marker))["reason"])
            self.assertNoFurtherWrites(g, gh, git)

    def test_05_exception_unknown_outcome_halts(self):
        gh = MockGitHub(issues(), mode="raise_on_write"); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.create", None, {"title": "t", "body": "b" + FOOTER})
        self.assertIn("unknown outcome", json.load(open(self.marker))["reason"])
        self.assertNoFurtherWrites(g, gh, git)

    def test_06_bad_status_halts(self):
        gh = MockGitHub(issues(), mode="status_500"); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "b" + FOOTER})
        self.assertNoFurtherWrites(g, gh, git)

    def test_07_existing_marker_blocks_everything(self):
        open(self.marker, "w").write('{"reason": "set elsewhere"}')
        gh = MockGitHub(issues()); git = MockGit(); g = self.gate(gh, git)
        for call in (lambda: g.write("comment.create", 1, {"body": "c" + FOOTER}),
                     lambda: g.write("issue.close", 1, {}),
                     lambda: g.push("origin", SHA, ALLOWED[0])):
            with self.assertRaises(Halted):
                call()
        self.assertEqual((len(gh.writes), len(git.runs), gh.gets), (0, 0, 0))
        self.assertEqual(open(self.marker).read(), '{"reason": "set elsewhere"}',
                         "an earlier marker was overwritten")

    def test_08_marker_blocks_other_process(self):
        open(self.marker, "w").write("{}")
        code = ("import sys; sys.path.insert(0, %r)\n"
                "from gate import *; from mock import *\n"
                "gh = MockGitHub({1: {'number': 1, 'title': 't', 'body': 'b', 'labels': [], "
                "'state': 'open'}}); g = Gate(gh, MockGit(), %r, 'o/r', "
                "{'comment.create': {'validated': True, 'send_form': 'footer'}})\n"
                "rc = main([lambda: g.write('comment.create', 1, {'body': 'x' + FOOTER})])\n"
                "print(len(gh.writes)); sys.exit(rc)\n") % (HERE, self.marker)
        p = subprocess.run([sys.executable, "-I", "-c", code], capture_output=True, text=True)
        self.assertEqual(p.returncode, 3)
        self.assertEqual(p.stdout.strip(), "0")
        self.assertIn("HALTED", p.stderr)

    def test_09_prechecks_refuse_before_write(self):
        long = "https://github.com/o/r/blob/" + "f" * 40 + "/" + "p" * 60
        cases = ["a\r\nb", "zero​width", "nb sp", "﻿bom", "see " + long,
                 "  OI-form comment\nx", "no footer"]
        for t in cases:
            self.setUp()
            gh = MockGitHub(issues()); git = MockGit(); g = self.gate(gh, git)
            body = t if t == "no footer" else t + FOOTER
            with self.assertRaises(Halted, msg=repr(t)):
                g.write("comment.create", 1, {"body": body})
            self.assertEqual(len(gh.writes), 0, repr(t))
            self.assertNoFurtherWrites(g, gh, git)
        ok = "https://github.com/o/r/blob/" + "f" * 40 + "/p#L1"
        self.assertEqual(G.precheck_text(ok + " " + "x" * 200), [])

    def test_10_unvalidated_needs_single_grant(self):
        gh = MockGitHub(issues()); git = MockGit(); g = self.gate(gh, git, registry(False))
        g.grant_single_write("issue.edit_body", 1)
        g.write("issue.edit_body", 1, {"body": "one" + FOOTER})
        with self.assertRaises(Halted):          # the grant was for one write only
            g.write("issue.edit_body", 1, {"body": "two" + FOOTER})
        self.assertEqual(len(gh.writes), 1)
        self.assertNoFurtherWrites(g, gh, git)

    def test_11_unsent_field_changed_halts(self):
        bodies = issues(); bodies[1]["body"] = "no footer"
        gh = MockGitHub(bodies, mode="append_on_close"); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.close", 1, {})
        self.assertIn("unsent field body changed", json.load(open(self.marker))["reason"])
        self.assertNoFurtherWrites(g, gh, git)

    def test_12_labels_and_close_verbatim(self):
        gh = MockGitHub(issues()); g = self.gate(gh)
        g.write("labels.add", 1, {}, labels=["b"])
        g.write("labels.remove", 1, {}, label="a")
        g.write("issue.close", 1, {})
        self.assertEqual([x["name"] for x in gh.issues[1]["labels"]], ["b"])
        self.assertFalse(os.path.exists(self.marker))


    def test_15_canonical_footer_body(self):
        cases = {
            "extra newlines": ("text\n\n\n\n---\n_Generated by [Claude Code](https://claude.ai/code)_",
                               "text" + FOOTER),
            "one extra newline (#1505)": ("Parent: #1169\n" + FOOTER, "Parent: #1169" + FOOTER),
            "trailing spaces, no footer": ("text   \n  ", "text" + FOOTER),
            "trailing spaces before footer": ("text  " + FOOTER, "text" + FOOTER),
            "already canonical": ("text" + FOOTER, "text" + FOOTER),
            "footer then newline": ("text" + FOOTER + "\n", "text" + FOOTER),
            "no footer": ("text", "text" + FOOTER),
        }
        for name, (raw, want) in cases.items():
            got = G.canonical_footer_body(raw)
            self.assertEqual(got, want, name)
            self.assertEqual(G.canonical_footer_body(got), got, name + ": idempotent")

    def test_16_noncanonical_refused_before_write(self):
        for raw in ("x\n" + FOOTER, "x  " + FOOTER, "x" + FOOTER + "\n"):
            self.setUp()
            gh = MockGitHub(issues()); git = MockGit(); g = self.gate(gh, git)
            with self.assertRaises(Halted):
                g.write("issue.edit_body", 1, {"body": raw})
            self.assertEqual(len(gh.writes), 0, "a non-canonical body reached the transport")
            self.assertIn("pre-check", json.load(open(self.marker))["reason"])
            self.assertNoFurtherWrites(g, gh, git)

    def test_17_canonical_passes_separator_normalization(self):
        with open(os.path.join(EV, "..", "issue-1505", "sent.md"), encoding="utf-8", newline="") as f:
            raw1505 = f.read()          # the body sent to #1505, three newlines before "---"
        self.assertNotEqual(G.canonical_footer_body(raw1505), raw1505)
        for raw in ("text\n\n\n" + FOOTER[2:], raw1505, "t  \n", "t" + FOOTER):
            self.setUp()
            gh = MockGitHub(issues(), mode="canonicalize_separator"); g = self.gate(gh)
            g.write("issue.edit_body", 1, {"body": G.canonical_footer_body(raw)})
            self.assertEqual(len(gh.writes), 1)
            self.assertFalse(os.path.exists(self.marker))

    def test_18_countercontrol_mock_reproduces_1505(self):
        """Without canonicalization (no send form) the mock reproduces the #1505 mismatch."""
        gh = MockGitHub(issues(), mode="canonicalize_separator"); git = MockGit()
        g = self.gate(gh, git, registry(form=None))
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "Parent: #1169\n" + FOOTER})
        self.assertIn("read-back mismatch", json.load(open(self.marker))["reason"])
        self.assertNoFurtherWrites(g, gh, git)


class Pushes(Base):
    def test_13_refused_refspecs(self):
        bad = [("", ALLOWED[0]), ("abc", ALLOWED[0]), ("A" * 40, ALLOWED[0]),
               ("a" * 39, ALLOWED[0]), ("+" + SHA, ALLOWED[0]), (SHA, "refs/heads/main"),
               (SHA, "refs/heads/other"), (SHA, ""), (SHA, "refs/tags/v1"),
               (SHA + ":refs/heads/x", ALLOWED[0]), ("--delete", ALLOWED[0])]
        for sha, ref in bad:
            self.setUp()
            gh = MockGitHub(issues()); git = MockGit(); g = self.gate(gh, git)
            with self.assertRaises(Halted, msg=(sha, ref)):
                g.push("origin", sha, ref)
            self.assertEqual(git.runs, [], (sha, ref))
            self.assertNoFurtherWrites(g, gh, git)
        for r in (":refs/heads/x", "+%s:refs/heads/evidence/x" % SHA, "%s:" % SHA, SHA):
            self.assertTrue(G.check_refspec(r, ALLOWED), r)
        self.assertEqual(G.check_refspec("%s:%s" % (SHA, ALLOWED[0]), ALLOWED), [])
        self.assertIn("deletes", " ".join(G.check_refspec(":refs/heads/evidence/x", ALLOWED)))
        self.setUp(); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(MockGitHub(), git).push("--force", SHA, ALLOWED[0])
        self.assertEqual(git.runs, [])
        self.assertIn("plain remote name", json.load(open(self.marker))["reason"])

    def test_14_push_paths(self):
        git = MockGit(); g = self.gate(MockGitHub(issues()), git)
        self.assertEqual(g.push("origin", SHA, ALLOWED[0]), SHA)             # create
        git.ancestors.add((SHA, SHA2))
        self.assertEqual(g.push("origin", SHA2, ALLOWED[0]), SHA2)           # fast-forward
        self.assertEqual(git.runs[0], ["git", "push", "--porcelain", "--", "origin",
                                       "%s:%s" % (SHA, ALLOWED[0])])
        for kw, refs in ((dict(rc=1), {}), (dict(raise_on_run=True), {}), (dict(lie=True), {}),
                         (dict(), {ALLOWED[0]: SHA2})):                        # non-ff
            self.setUp()
            gh = MockGitHub(issues()); git = MockGit(refs=refs, **kw); g = self.gate(gh, git)
            with self.assertRaises(Halted, msg=kw):
                g.push("origin", SHA, ALLOWED[0])
            self.assertNoFurtherWrites(g, gh, git)


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    unittest.main(verbosity=2)
