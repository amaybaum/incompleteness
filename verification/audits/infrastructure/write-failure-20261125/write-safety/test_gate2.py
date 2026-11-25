"""Controls for gate2 and transport_rules. Mock transport only. Run: python3 -I -B test_gate2.py

Negative controls are the test methods named test_neg_*; countercontrol2.py requires that every
mutation of the rule or of the gate's outcome handling makes at least one of them fail.

Containment (AGENTS.md section A.49 rule 3 as amended in PR #1566): after any halt or refusal,
the plan's latch (HALT-PLAN.<plan_id>) and the process's copy of the halt store refuse every write
and push of the plan, in this and every later process (run level); a later sequence, simulated here
by new_sequence(), which empties the process copy as a fresh process would start and runs under a
new plan id, meets the global marker unless the halt was a read-back mismatch with a footer-shaped
tail meeting every condition of rule 3, in which case only that operation's marker exists, and it
writes nothing until the marker's .notified companion exists. Tests q10 and q11 run the same plan
id in a separate process (a restart) and find it refused. The plan id is fixed in the plan record
(PLAN in the halt store) before the run; new_sequence() replaces that record by hand, as a person
does when a plan has ended, and test q16 finds a caller-supplied id that differs from it refused."""
import dataclasses, hashlib, json, os, subprocess, sys, tempfile, unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gate as G
import gate2 as G2
import transport_rules as TR
from gate2 import Gate2, Halted, run_plan
from mock2 import MockGitHub2, MockGit

EV = os.path.join(HERE, "ev")
REPO = "owner/repo"
SHA, SHA2 = "a" * 40, "b" * 40
ALLOWED = ("refs/heads/evidence/x",)
CORE = TR.FOOTER_CORE
F = TR.FOOTER_SEND_FORM          # "\n\n" + CORE


def DROP(b):
    """A rejected, footer-shaped transformation with at most one footer copy (operation level):
    a footer at the end is removed; a body without one gets two newlines."""
    return b[: -len(F)] if b.endswith(F) else b + "\n\n"


def read(*p):
    with open(os.path.join(EV, *p), encoding="utf-8", newline="") as f:
        return f.read()


def registry(validated=True, form=None, allowlist=True):
    """allowlist True: validated under the allowlist (section A.51 item 2); False: validated by
    exact read-back only, and so held to exact read-back."""
    return {op: {"validated": validated, "send_form": (form if spec["text"] else None),
                 "allowlist": allowlist} for op, spec in G.OPERATIONS.items()}


def issues():
    return {n: {"number": n, "title": "T%d" % n, "body": "old %d" % n + F,
                "labels": [{"name": "a"}], "state": "open"} for n in (1, 2, 3, 4, 5)}


def rep(s, a, b):
    assert s.count(a) == 1, (a, s.count(a))
    return s.replace(a, b)


BASE = ("## Planning status\n\n"
        "- Tier: foundational\n"
        "- Authorization: execution (owner `amaybaum`, #1169 comment 7164587230, "
        "2026-11-25T09:12:00Z)\n\n"
        "Owner decision (amaybaum, 2026-11-25): \"Proceed with the bounded transport-difference "
        "policy now.\"\n\n"
        "The bound is m < 3.2 GeV at 95% CL; see "
        "[the proof](https://github.com/o/r/blob/abc/papers/Main.md#L10) and "
        "[the record](https://github.com/o/r/issues/1548).\n\n"
        "1. first item\n"
        "2. second item\n\n"
        "Parent: #1169")


def variants(mutated):
    """Every content mutation is tried with the footer appended, with the footer on both sides,
    and with no footer at all."""
    return [(BASE, mutated + F), (BASE + F, mutated + F), (BASE, mutated)]


SAMPLE = {   # one further write per mechanism, for the no-further-write checks
    "comment.create": lambda g: g.write("comment.create", 1, {"body": "x" + F}),
    "issue.edit_body": lambda g: g.write("issue.edit_body", 2, {"body": "y" + F}),
    "issue.create": lambda g: g.write("issue.create", None, {"title": "t", "body": "b" + F}),
    "issue.close": lambda g: g.write("issue.close", 4, {}),
    "labels.add": lambda g: g.write("labels.add", 3, {}, labels=["b"]),
    "labels.remove": lambda g: g.write("labels.remove", 3, {}, label="a"),
    "pr.edit": lambda g: g.write("pr.edit", 5, {"body": "p" + F}),
    "push": lambda g: g.push("origin", SHA, ALLOWED[0]),
}


def expect_footer_shaped(sent, stored):
    """Independent restatement of rule 3's third condition, for the expected scope of a halt:
    the sent content (sent less trailing newlines and a footer recognised as rule 2 states it)
    is not empty, the stored text starts with it, and what follows is only newlines and at most
    one exact copy of the footer core."""
    c = sent
    while c.endswith("\n"):
        c = c[:-1]
    if c.endswith(CORE):
        b = c[: len(c) - len(CORE)]
        cc = b
        while cc.endswith("\n"):
            cc = cc[:-1]
        if cc and len(b) - len(cc) >= 2 and not cc.endswith(CORE):
            c = cc
    if not (isinstance(stored, str) and c != "" and stored[: len(c)] == c):
        return False
    rest = stored[len(c):]
    copies = 0
    while rest:
        if rest[0] == "\n":
            rest = rest[1:]
        elif rest[: len(CORE)] == CORE:
            rest = rest[len(CORE):]
            copies += 1
        else:
            return False
    return copies <= 1


class Base(unittest.TestCase):
    plans = 0

    def setUp(self):
        self.dir = tempfile.mkdtemp(dir=os.path.join(HERE, "runs"))
        self.new_sequence()

    def new_sequence(self):
        """A later sequence: a fresh writer process, with an empty copy of the halt store in
        memory, running a new plan (a new plan id)."""
        del G2._HALTED[:]
        Base.plans += 1
        self.plan = "plan-%d" % Base.plans
        record = os.path.join(self.dir, G2.PLAN_RECORD)
        if os.path.exists(record):                   # by hand: the previous plan has ended
            os.remove(record)
        G2.record_plan(self.dir, self.plan)

    def notify(self, mech):
        """By hand, after the evidence is kept and the owner told (rule 3)."""
        open(self.marker(mech) + ".notified", "w").close()

    def marker(self, mech=None):
        return os.path.join(self.dir, "HALT" if mech is None else "HALT." + mech)

    def gate(self, gh, git=None, reg=None, rules=None):
        return Gate2(gh, git or MockGit(), self.dir, REPO, reg or registry(), ALLOWED, rules=rules,
                     plan_id=self.plan)

    def halt_record(self, mech=None):
        with open(self.marker(mech)) as f:
            return json.load(f)

    def assertNoFurtherWrites(self, g, gh, git, mech, scope="global"):
        """After a halt of mech: the marker of the expected scope exists (and only it); the same
        gate and any other gate in the process refuse every mechanism (run level); in a later
        sequence a fresh gate refuses mech. None of it reaches the transport."""
        w, r, n = len(gh.writes), len(git.runs), gh.gets
        if scope == "global":
            self.assertTrue(os.path.exists(self.marker()), "global marker not written for " + mech)
            self.assertFalse(os.path.exists(self.marker(mech)), "operation marker for " + mech)
        else:
            self.assertTrue(os.path.exists(self.marker(mech)), "halt marker not written for " + mech)
            self.assertFalse(os.path.exists(self.marker()), "global marker written for " + mech)
        for gg in (g, self.gate(gh, git)):           # same sequence: everything refused
            for m, call in SAMPLE.items():
                with self.assertRaises(Halted, msg="%s after halt of %s" % (m, mech)):
                    call(gg)
        self.new_sequence()
        with self.assertRaises(Halted):
            SAMPLE[mech](self.gate(gh, git))
        self.assertEqual((len(gh.writes), len(git.runs), gh.gets), (w, r, n),
                         "a request reached the transport after the halt of " + mech)
        self.new_sequence()

    def assertOtherMechanismOpen(self, gh, git, mech):
        """Operation-level containment: a later sequence writes nothing until the owner has been
        told (.notified), then another mechanism writes, through a fresh gate."""
        other = "issue.edit_body" if mech != "issue.edit_body" else "comment.create"
        w = len(gh.writes)
        gh2 = MockGitHub2(issues())                  # same halt directory, new transport
        self.new_sequence()
        with self.assertRaises(Halted) as cm:
            SAMPLE[other](self.gate(gh2, git))
        self.assertIn("owner not yet told", str(cm.exception))
        self.assertEqual((len(gh2.writes), gh2.gets), (0, 0))
        self.notify(mech)
        self.new_sequence()
        res = SAMPLE[other](self.gate(gh2, git))
        self.assertEqual(res.outcomes["body"][0], "exact")
        self.assertEqual(len(gh.writes), w)
        self.assertFalse(os.path.exists(self.marker(other)))

    def assertGlobalStop(self, git, mech):
        """A later sequence writes through no mechanism, even with every notification present."""
        for n in os.listdir(self.dir):
            if n.startswith("HALT.") and not n.endswith(".notified"):
                open(os.path.join(self.dir, n + ".notified"), "w").close()
        gh2 = MockGitHub2(issues())
        for m, call in SAMPLE.items():
            self.new_sequence()
            with self.assertRaises(Halted, msg="%s after global halt of %s" % (m, mech)):
                call(self.gate(gh2, git))
        self.assertEqual((len(gh2.writes), gh2.gets), (0, 0))
        self.new_sequence()

    def check_rejected_through_gate(self, sent, stored, name):
        """The negative-control pattern: rejected by classify; through the gate, one write, a halt
        of that mechanism with sent, stored and diff kept, no further write, others open."""
        self.assertEqual(TR.classify(sent, stored), ("rejected", None), name)
        self.setUp()
        gh = MockGitHub2(issues(), transforms={"patch": lambda b, s=stored: s}); git = MockGit()
        g = self.gate(gh, git)
        with self.assertRaises(Halted, msg=name):
            g.write("issue.edit_body", 1, {"body": sent})
        self.assertEqual(len(gh.writes), 1, name)
        scope = "operation" if expect_footer_shaped(sent, stored) else "global"
        rec = self.halt_record("issue.edit_body" if scope == "operation" else None)
        self.assertEqual(rec["scope"], scope, name)
        self.assertIn("rejected", rec["reason"], name)
        self.assertEqual(set(rec["evidence"]), {"body.sent", "body.stored", "body.diff"}, name)
        for k, v in (("body.sent", sent), ("body.stored", stored)):
            with open(os.path.join(self.dir, rec["evidence"][k]["file"]), encoding="utf-8",
                      newline="") as f:
                self.assertEqual(f.read(), v, name)
            self.assertEqual(rec["evidence"][k]["text"], v, name)
            self.assertEqual(rec["evidence"][k]["sha256"], G2.sha256(v), name)
        self.assertFalse([p for p in os.listdir(self.dir) if p.startswith("discrepancy")], name)
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", scope)
        if scope == "operation":
            self.assertOtherMechanismOpen(gh, git, "issue.edit_body")
        else:
            self.assertGlobalStop(git, "issue.edit_body")
        return scope


# --------------------------------------------------------------------------------------------
class Registry(Base):
    def test_r1_registry_closed(self):
        self.assertIsInstance(TR.REGISTRY, tuple)
        self.assertEqual([(r.id, r.version) for r in TR.REGISTRY], [("footer-attribution-1", "1")])
        self.assertEqual(TR.REGISTRY[0].fields, ("body",))
        with self.assertRaises(dataclasses.FrozenInstanceError):
            TR.REGISTRY[0].id = "x"
        self.assertFalse([n for n in dir(TR) if n.lower().startswith(("register", "learn", "add"))])
        self.assertEqual(TR.FOOTER_SEND_FORM, G.FOOTER)
        self.assertEqual(TR.FOOTER_CORE, G.FOOTER_CORE)

    def test_r2_gate2_carries_no_footer_formatting(self):
        with open(os.path.join(HERE, "gate2.py"), encoding="utf-8") as f:
            src = f.read()
        for s in ("Generated", "claude.ai", "FOOTER", "rstrip", "strip(", "lower("):
            self.assertNotIn(s, src, s)

    def test_r3_registry_validation(self):
        for bad in ([TR.FOOTER_ATTRIBUTION_1], (TR.FOOTER_ATTRIBUTION_1, TR.FOOTER_ATTRIBUTION_1),
                    ("not a rule",)):
            with self.assertRaises((TypeError, ValueError)):
                TR.classify("a", "b", bad)

    def test_r4_classification_failure_halts(self):
        gh = MockGitHub2(issues(), transforms={"patch": lambda b: b + F}); git = MockGit()
        g = self.gate(gh, git, rules=[TR.FOOTER_ATTRIBUTION_1])       # a list: not a registry
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "x"})
        self.assertIn("classification failed", self.halt_record()["reason"])
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "global")

    def test_r5_ambiguity_rejected(self):
        twin = dataclasses.replace(TR.FOOTER_ATTRIBUTION_1, id="footer-attribution-twin")
        rules = (TR.FOOTER_ATTRIBUTION_1, twin)
        self.assertEqual(TR.classify("x", "x" + F, rules), ("rejected", None))
        self.assertEqual(TR.classify("x", "x", rules), ("exact", None))
        gh = MockGitHub2(issues(), transforms={"patch": lambda b: b + F}); git = MockGit()
        g = self.gate(gh, git, rules=rules)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "x"})
        self.assertIn("rejected", self.halt_record("issue.edit_body")["reason"])
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "operation")


# --------------------------------------------------------------------------------------------
class Positive(Base):
    PAIRS = {
        "exact": ("x" + F, "x" + F),
        "footer appended": ("text", "text" + F),
        "footer appended after trailing newline": ("text\n", "text" + F),
        "footer in both, more newlines sent": ("text\n\n\n\n" + CORE, "text" + F),
        "footer in both, more newlines stored": ("text" + F, "text\n\n\n" + CORE),
        "newlines after footer": ("text" + F, "text" + F + "\n"),
        "newlines after footer, footer appended": ("text\n\n", "text" + F + "\n\n"),
        "hard break kept byte-identical": ("line one  \nline two  ", "line one  \nline two  " + F),
        "indented last line kept": ("Code:\n\n    x = 1", "Code:\n\n    x = 1" + F),
        "footer quoted earlier in content": ("q:\n\n" + CORE + "\n\nend", "q:\n\n" + CORE
                                             + "\n\nend" + F),
    }

    def test_p1_classify_synthetic(self):
        for name, (s, t) in self.PAIRS.items():
            want = ("exact", None) if s == t else ("permitted", "footer-attribution-1")
            self.assertEqual(TR.classify(s, t), want, name)

    def test_p2_classify_real_pairs(self):
        for n in (1558, 1062, 1245, 1556):
            self.assertEqual(TR.classify(read("bodies", "%d.sent.md" % n),
                                         read("bodies", "%d.stored.md" % n)),
                             ("permitted", "footer-attribution-1"), n)
        self.assertEqual(TR.classify(read("bodies", "1565.sent.md"), read("bodies", "1565.stored.md")),
                         ("exact", None))
        self.assertEqual(TR.classify(read("issue-1505", "sent.md"), read("issue-1505", "stored.md")),
                         ("permitted", "footer-attribution-1"))
        for v in ("validation", "validation-2"):
            self.assertEqual(TR.classify(read("issue-1548", v, "expected-body.md"),
                                         read("issue-1548", v, "stored-body.md")), ("exact", None))

    def test_p3_real_pairs_through_gate_with_records(self):
        cases = {"1505": (read("issue-1505", "sent.md"), read("issue-1505", "stored.md")),
                 "1558": (read("bodies", "1558.sent.md"), read("bodies", "1558.stored.md"))}
        for name, (sent, stored) in cases.items():
            self.setUp()
            gh = MockGitHub2(issues(), transforms={"patch": lambda b, s=stored: s}); git = MockGit()
            g = self.gate(gh, git)
            res = g.write("issue.edit_body", 1, {"body": sent})
            self.assertEqual(res.outcomes, {"body": ["permitted", "footer-attribution-1"]}, name)
            self.assertEqual(len(res.records), 1, name)
            self.check_record(res.records[0], "issue.edit_body", 1, sent, stored)
            self.assertFalse([p for p in os.listdir(self.dir) if p.startswith("HALT")], name)
            res2 = g.write("comment.create", 1, {"body": "next" + F})   # writing continues
            self.assertEqual(res2.outcomes["body"][0], "exact")

    def check_record(self, path, op, target, sent, stored):
        self.assertEqual(os.path.dirname(path), self.dir)
        with open(path, encoding="utf-8") as f:
            rec = json.load(f)
        self.assertEqual(rec["kind"], "permitted-transport-difference")
        self.assertEqual((rec["operation"], rec["target"], rec["field"]), (op, target, "body"))
        self.assertEqual((rec["rule_id"], rec["rule_version"]), ("footer-attribution-1", "1"))
        self.assertEqual(rec["sent"], sent)
        self.assertEqual(rec["stored"], stored)
        self.assertEqual(rec["sent_sha256"], hashlib.sha256(sent.encode()).hexdigest())
        self.assertEqual(rec["stored_sha256"], hashlib.sha256(stored.encode()).hexdigest())
        self.assertTrue(rec["unified_diff"].startswith("--- sent\n+++ stored\n"))
        self.assertRegex(rec["time"], r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$")
        out, pos = [], 0                       # the char diff reproduces stored from sent exactly
        for tag, i1, i2, j1, j2, a, b in rec["char_opcodes"]:
            self.assertEqual(sent[i1:i2], a)
            out.append(sent[pos:i1]); out.append(b); pos = i2
        out.append(sent[pos:])
        self.assertEqual("".join(out), stored)

    def test_p4_d1_replay_all_accepted_with_records(self):
        """The five evidence bodies, in edit.py's order, under append-if-absent: all five accepted,
        four with records (#1565 exact), stored bytes equal to the evidence."""
        order = [1558, 1565, 1062, 1245, 1556]
        before = {n: {"number": n, "title": "t", "labels": [], "state": "open",
                      "body": read("bodies", "%d.before.md" % n)} for n in order}
        gh = MockGitHub2(before, mode="append_if_absent"); git = MockGit()
        g = self.gate(gh, git)
        results = [g.write("issue.edit_body", n, {"body": read("bodies", "%d.sent.md" % n)})
                   for n in order]
        self.assertEqual(len(gh.writes), 5)
        self.assertEqual([r.outcomes["body"][0] for r in results],
                         ["permitted", "exact", "permitted", "permitted", "permitted"])
        self.assertEqual(sum(len(r.records) for r in results), 4)
        for n in order:
            self.assertEqual(gh.issues[n]["body"], read("bodies", "%d.stored.md" % n), n)

    def test_p5_send_form_without_footer_then_appended(self):
        gh = MockGitHub2(issues(), mode="append_if_absent"); g = self.gate(gh, reg=registry(form="nofooter"))
        res = g.write("comment.create", 1, {"body": "plain"})
        self.assertEqual(res.outcomes["body"], ["permitted", "footer-attribution-1"])


# --------------------------------------------------------------------------------------------
class Negative(Base):
    def run_cases(self, cases):
        scopes = []
        for name, mutated in cases:
            self.assertNotEqual(mutated, BASE, name)
            for i, (s, t) in enumerate(variants(mutated)):
                scopes.append(self.check_rejected_through_gate(s, t, "%s/v%d" % (name, i)))
        return scopes

    def test_neg_content_changes_stop_globally(self):
        """Every content change before the tail stops every text write (rule 3), whichever
        footer handling surrounds it."""
        for name, mutated in [("digit", rep(BASE, "3.2 GeV", "3.3 GeV")),
                              ("link", rep(BASE, "#L10", "#L11")),
                              ("leading space", " " + BASE),
                              ("truncated", BASE[:-1])]:
            self.assertEqual(set(self.run_cases([(name, mutated)])), {"global"}, name)

    def test_neg_scientific_content(self):
        self.run_cases([
            ("changed word", rep(BASE, "The bound is", "The limit is")),
            ("changed digit", rep(BASE, "3.2 GeV", "3.3 GeV")),
            ("changed percent", rep(BASE, "95%", "90%")),
            ("changed relation", rep(BASE, "m < 3.2", "m > 3.2")),
            ("last word changed", rep(BASE, "Parent: #1169", "Parent: #1170")),
        ])

    def test_neg_links(self):
        self.run_cases([
            ("link URL path", rep(BASE, "papers/Main.md", "papers/SM.md")),
            ("link host", rep(BASE, "https://github.com/o/r/issues", "https://gitlab.com/o/r/issues")),
            ("fragment removed", rep(BASE, "Main.md#L10", "Main.md")),
            ("fragment added", rep(BASE, "issues/1548)", "issues/1548#issuecomment-1)")),
            ("fragment changed", rep(BASE, "#L10", "#L11")),
            ("link text", rep(BASE, "[the proof]", "[a proof]")),
        ])

    def test_neg_internal_whitespace(self):
        self.run_cases([
            ("internal blank line removed", rep(BASE, "\n\n1. first", "\n1. first")),
            ("internal blank line added", rep(BASE, "\n\nParent", "\n\n\nParent")),
            ("internal space run", rep(BASE, "m < 3.2", "m  < 3.2")),
            ("internal trailing spaces", rep(BASE, "first item\n", "first item  \n")),
            ("internal tab", rep(BASE, "m < 3.2", "m\t< 3.2")),
            ("whitespace before non-footer ending", rep(BASE, "Parent: #1169", "Parent:  #1169")),
            ("leading blank line", "\n" + BASE),
            ("leading space", " " + BASE),
        ])

    def test_neg_markdown_structure(self):
        self.run_cases([
            ("bullet marker", rep(BASE, "- Tier", "* Tier")),
            ("ordered marker", rep(BASE, "1. first", "1) first")),
            ("heading level", rep(BASE, "## Planning", "### Planning")),
            ("heading to text", rep(BASE, "## Planning", "Planning")),
            ("code span removed", rep(BASE, "`amaybaum`", "amaybaum")),
        ])

    def test_neg_authorization_record(self):
        self.run_cases([
            ("quoted decision word", rep(BASE, "policy now.", "policy soon.")),
            ("quoted decision punctuation", rep(BASE, "now.\"", "now\"")),
            ("comment id", rep(BASE, "7164587230", "7164587231")),
            ("decision author", rep(BASE, "(amaybaum, 2026", "(someone, 2026")),
            ("decision time", rep(BASE, "09:12:00Z", "09:12:01Z")),
            ("authorization level", rep(BASE, "execution (owner", "paper-only (owner")),
        ])

    def test_neg_footer_variants(self):
        x = BASE
        cases = {
            "nbsp before footer": (x, x + "\u00a0" + F),
            "nbsp inside separator": (x, x + "\n\u00a0\n" + CORE),
            "nbsp after footer": (x, x + F + "\u00a0"),
            "form feed before footer": (x, x + "\x0c" + F),
            "carriage returns in separator": (x, x + "\r\n\r\n" + CORE),
            "vertical tab after footer": (x, x + F + "\x0b"),
            "zero-width space before footer": (x, x + "\u200b" + F),
            "footer one char: case": (x, x + F.replace("Claude Code", "Claude code")),
            "footer one char: rule": (x, x + "\n\n-" + CORE),
            "footer one char: url": (x, x + F.replace("claude.ai/code", "claude.ai/codex")),
            "footer one char: lookalike": (x, x + F.replace("Generated", "G\u0435nerated")),
            "footer one char: underscore": (x, x + F[:-1]),
            "footer other attribution": (x, x + "\n\n---\n_Generated by Codex_"),
            "doubled footer": (x, x + F + F),
            "doubled footer, sent has one": (x + F, x + F + F),
            "doubled footer, separator between": (x, x + F + "\n\n\n" + CORE),
            "footer moved off end": (x, x + F + "\n\nmore"),
            "footer in middle": (x, rep(x, "\n\nParent", F + "\n\nParent")),
            "footer removed": (x + F, x),
            "footer one newline before": (x, x + "\n" + CORE),
            "footer no newline before": (x, x + CORE),
            "footer indented": (x, x + "\n\n    " + CORE),
            "footer indented one space": (x, x + "\n\n " + CORE),
            "spaces after footer": (x, x + F + "  "),
            "tab after footer": (x, x + F + "\t"),
            "spaces between newlines before footer": (x, x + "\n \n" + CORE),
            "tab in separator": (x, x + "\n\t\n" + CORE),
            "empty body gets footer": ("", F),
            "malformed sent footer plus appended": (x + "\n" + CORE, x + "\n" + CORE + F),
        }
        for name, (s, t) in cases.items():
            if "\r" in s or "\u00a0" in s:
                raise AssertionError("sent must pass the pre-checks: " + name)
            self.check_rejected_through_gate(s, t, name)

    def test_neg_markdown_whitespace_boundary(self):
        """Owner clarification: meaningful Markdown whitespace at the end of the content is
        content. Spaces and tabs never differ anywhere."""
        cases = {
            "hard break removed": ("para\nlast line  ", "para\nlast line" + F),
            "hard break removed, footer both": ("para\nlast line  " + F, "para\nlast line" + F),
            "hard break added": ("para\nlast line", "para\nlast line  " + F),
            "hard break internal removed": ("a  \nb", "a\nb" + F),
            "backslash break removed": ("para\nlast\\", "para\nlast" + F),
            "backslash break doubled": ("para\nlast\\", "para\nlast\\\\" + F),
            "backslash break added": ("para\nlast", "para\nlast\\" + F),
            "indented code dedented": ("Code:\n\n    x = 1", "Code:\n\n  x = 1" + F),
            "indented code to text": ("Code:\n\n    x = 1", "Code:\n\nx = 1" + F),
            "indented code trailing line": ("Code:\n\n    x = 1\n    ", "Code:\n\n    x = 1" + F),
            "nested list item outdented": ("- a\n  - b", "- a\n- b" + F),
            "nested list item reindented": ("- a\n  - b", "- a\n    - b" + F),
            "tab to spaces, last line": ("- a\n\t- b", "- a\n    - b" + F),
            "tab to spaces, trailing": ("last\t", "last    " + F),
            "trailing tab removed": ("last\t", "last" + F),
            "trailing single space removed": ("last ", "last" + F),
            "space-only line before footer removed": ("para\n\n   \n\n" + CORE, "para" + F),
            "space-only line before footer added": ("para" + F, "para\n\n   \n\n" + CORE),
            "space-only line internal emptied": ("a\n \nb", "a\n\nb" + F),
            "space-only line internal changed": ("a\n \nb", "a\n  \nb" + F),
            "space-only trailing line removed": ("para\n  ", "para" + F),
        }
        for name, (s, t) in cases.items():
            self.check_rejected_through_gate(s, t, name)

    def test_neg_truncation_extension(self):
        self.run_cases([
            ("stored truncated by one", BASE[:-1]),
            ("stored truncated by a line", BASE.rsplit("\n", 1)[0]),
            ("trailer added", BASE + "\n\nSigned-off-by: x"),
            ("trailer after rule", BASE + "\n\n---\n"),
        ])
        for name, (s, t) in {"extended after footer": (BASE, BASE + F + "\nx"),
                             "empty stored": (BASE, ""),
                             "trailing newline only, no footer": (BASE, BASE + "\n"),
                             "trailing newline removed, no footer": (BASE + "\n", BASE)}.items():
            self.check_rejected_through_gate(s, t, name)

    def test_neg_title_never_permitted(self):
        gh = MockGitHub2(issues(), title_transform=lambda t: t + F); git = MockGit()
        g = self.gate(gh, git)
        self.assertEqual(TR.classify("t", "t" + F, field="title"), ("rejected", None))
        with self.assertRaises(Halted):
            g.write("issue.create", None, {"title": "t", "body": "b" + F})
        self.assertIn("title", self.halt_record("issue.create")["reason"])   # footer-shaped
        self.assertNoFurtherWrites(g, gh, git, "issue.create", "operation")

    def test_neg_unsent_field_gets_footer(self):
        """A footer appended to a body the write did not send is not permitted (no allowlist for
        unsent fields)."""
        bodies = issues(); bodies[1]["body"] = "no footer"
        gh = MockGitHub2(bodies, mode="append_on_close"); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.close", 1, {})
        self.assertIn("body read-back differs", self.halt_record()["reason"])
        self.assertNoFurtherWrites(g, gh, git, "issue.close", "global")


# --------------------------------------------------------------------------------------------
class Containment(Base):
    def test_c1_run_level_latch_after_operation_level_halt(self):
        """A footer-shaped mismatch halts the operation only; the same gate, and every other gate in
        the process, still refuse every mechanism, even after the owner has been told. A later
        sequence may write a comment only once the .notified file exists."""
        gh = MockGitHub2(issues(), transforms={"patch": DROP}); git = MockGit()
        g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "x" + F})          # footer removed: rejected
        self.assertEqual(self.halt_record("issue.edit_body")["scope"], "operation")
        self.assertFalse(os.path.exists(self.marker()))
        self.notify("issue.edit_body")
        for gg in (g, self.gate(gh, git)):
            for mech, call in SAMPLE.items():
                with self.assertRaises(Halted, msg=mech):
                    call(gg)
        self.assertEqual((len(gh.writes), len(git.runs)), (1, 0))
        self.new_sequence()
        g2 = self.gate(gh, git)
        self.assertEqual(g2.write("comment.create", 1, {"body": "c" + F}).outcomes["body"][0],
                         "exact")
        g2.write("labels.add", 2, {}, labels=["b"])
        self.assertEqual(g2.push("origin", SHA, ALLOWED[0]), SHA)
        with self.assertRaises(Halted):
            g2.write("issue.edit_body", 3, {"body": "z" + F})
        with self.assertRaises(Halted):                               # and g2 is now latched
            g2.write("comment.create", 1, {"body": "d" + F})
        self.assertEqual(len(gh.writes), 3)

    def test_c1b_later_sequence_waits_for_notification(self):
        gh = MockGitHub2(issues(), transforms={"patch": DROP}); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(gh, git).write("issue.edit_body", 1, {"body": "x" + F})
        self.new_sequence()
        with self.assertRaises(Halted) as cm:
            self.gate(gh, git).write("comment.create", 1, {"body": "c" + F})
        self.assertIn("owner not yet told", str(cm.exception))
        self.assertEqual(len(gh.writes), 1)
        self.assertFalse(os.path.exists(self.marker()))               # a refusal writes no marker

    def test_c2_global_marker_blocks_every_mechanism(self):
        with open(self.marker(), "w") as f:
            f.write('{"reason": "set elsewhere"}')
        gh = MockGitHub2(issues()); git = MockGit()
        for mech, call in SAMPLE.items():
            self.new_sequence()
            with self.assertRaises(Halted, msg=mech):
                call(self.gate(gh, git))
        self.assertEqual((len(gh.writes), len(git.runs), gh.gets), (0, 0, 0))
        with open(self.marker()) as f:
            self.assertEqual(f.read(), '{"reason": "set elsewhere"}')

    def test_c3_existing_op_marker_blocks_and_is_kept(self):
        with open(self.marker("comment.create"), "w") as f:
            f.write("{}")
        self.notify("comment.create")
        gh = MockGitHub2(issues()); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            SAMPLE["comment.create"](g)
        self.assertEqual((len(gh.writes), gh.gets), (0, 0))
        with self.assertRaises(Halted):                               # the sequence has ended
            SAMPLE["issue.edit_body"](g)
        self.new_sequence()
        SAMPLE["issue.edit_body"](self.gate(gh, git))
        self.assertEqual(len(gh.writes), 1)
        with open(self.marker("comment.create")) as f:
            self.assertEqual(f.read(), "{}")

    def test_c4_unknown_operation_halts_globally(self):
        gh = MockGitHub2(issues()); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.delete", 1, {})
        self.assertTrue(os.path.exists(self.marker()))
        for mech, call in SAMPLE.items():
            self.new_sequence()
            with self.assertRaises(Halted, msg=mech):
                call(self.gate(gh, git))
        self.assertEqual((len(gh.writes), len(git.runs)), (0, 0))

    def test_c5_marker_blocks_other_process(self):
        with open(self.marker("comment.create"), "w") as f:
            f.write("{}")
        code = ("import sys; sys.path.insert(0, %r)\n"
                "from gate2 import *; from mock2 import *; import transport_rules as TR\n"
                "gh = MockGitHub2({1: {'number': 1, 'title': 't', 'body': 'b', 'labels': [], "
                "'state': 'open'}}); g = Gate2(gh, MockGit(), %r, 'o/r', "
                "{'comment.create': {'validated': True, 'send_form': None}}, plan_id=%r)\n"
                "rc = main([lambda: g.write('comment.create', 1, {'body': 'x'})])\n"
                "print(len(gh.writes), gh.gets); sys.exit(rc)\n") % (HERE, self.dir, self.plan)
        p = subprocess.run([sys.executable, "-I", "-B", "-c", code], capture_output=True, text=True)
        self.assertEqual(p.returncode, 3, p.stderr)
        self.assertEqual(p.stdout.strip(), "0 0")
        self.assertIn("HALTED", p.stderr)

    def test_c6_second_halt_with_outstanding_marker_is_global(self):
        """Two halts in one process (two sequences) keep separate evidence; the second, although
        footer-shaped, is global because another operation's mismatch is outstanding."""
        gh = MockGitHub2(issues(), transforms={"patch": DROP, "comment": DROP})
        git = MockGit()
        with self.assertRaises(Halted):
            SAMPLE["issue.edit_body"](self.gate(gh, git))
        self.notify("issue.edit_body")
        self.new_sequence()
        with self.assertRaises(Halted):
            SAMPLE["comment.create"](self.gate(gh, git))
        a, b = self.halt_record("issue.edit_body"), self.halt_record()
        self.assertEqual((a["scope"], b["scope"]), ("operation", "global"))
        self.assertFalse(os.path.exists(self.marker("comment.create")))
        self.assertNotEqual(a["evidence"]["body.sent"]["file"], b["evidence"]["body.sent"]["file"])
        for rec in (a, b):
            for k in ("body.sent", "body.stored", "body.diff"):
                self.assertTrue(os.path.exists(os.path.join(self.dir, rec["evidence"][k]["file"])))


# --------------------------------------------------------------------------------------------
class Probes(Base):
    """The independent review's probes of PR #1566 and gate v2 (R2, R3, R8) and rule 3's
    conditions, each with a fixed expected scope."""

    def test_q1_timeout_is_global(self):
        gh = MockGitHub2(issues(), mode="raise_on_write"); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "b" + F})
        self.assertIn("unknown outcome: TimeoutError", self.halt_record()["reason"])
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "global")
        self.assertGlobalStop(git, "issue.edit_body")

    def test_q2_content_change_is_global(self):
        body = "The measured value is 0.3 at 95% CL." + F
        gh = MockGitHub2(issues(), transforms={"patch": lambda b: b.replace("0.3", "0.4")})
        git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": body})
        self.assertEqual(self.halt_record()["scope"], "global")
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "global")
        self.assertGlobalStop(git, "issue.edit_body")

    def plan_steps(self):
        return [("issue.edit_body", 1, {"body": "edit one" + F}),
                ("comment.create", 1, {"body": "comment one" + F}),
                ("comment.create", 2, {"body": "comment two" + F}),
                ("issue.edit_body", 2, {"body": "edit two" + F})]

    def test_q3_caller_catching_halted_writes_nothing_further(self):
        """edit.py's shape: a loop that catches Halted per item. After the first halt, zero
        further writes, whether the halt was operation-level or global, whether the loop reuses
        the gate or builds a new one per item, and even if .notified appears meanwhile."""
        transforms = {"footer-shaped": DROP,
                      "content change": lambda b: b.replace("one", "One")}
        for tname, tf in transforms.items():
            for per_item in (False, True):
                self.setUp()
                gh = MockGitHub2(issues(), transforms={"patch": tf}); git = MockGit()
                g = self.gate(gh, git)
                halts = 0
                for i, (op, n, fields) in enumerate(self.plan_steps()):
                    if i == 1:
                        for m in os.listdir(self.dir):
                            if m.startswith("HALT."):
                                self.notify(m[len("HALT."):])
                    try:
                        (self.gate(gh, git) if per_item else g).write(op, n, fields)
                    except Halted:
                        halts += 1
                        continue
                self.assertEqual(len(gh.writes), 1, (tname, per_item))
                self.assertEqual(halts, 4, (tname, per_item))
                with self.assertRaises(Halted):
                    g.push("origin", SHA, ALLOWED[0])
                self.assertEqual(git.runs, [])

    def test_q4_no_orphaned_record_when_a_later_field_fails(self):
        """R8: issue.create with the body footer appended (permitted) and the title altered:
        no discrepancy record is written for the body."""
        for title_tf, scope in ((lambda t: "X" + t, "global"), (lambda t: t + "!", "global"),
                                (lambda t: t + F, "operation")):
            self.setUp()
            gh = MockGitHub2(issues(), mode="append_if_absent", title_transform=title_tf)
            git = MockGit(); g = self.gate(gh, git)
            with self.assertRaises(Halted):
                g.write("issue.create", None, {"title": "t", "body": "b"})
            self.assertFalse([p for p in os.listdir(self.dir) if p.startswith("discrepancy")])
            rec = self.halt_record("issue.create" if scope == "operation" else None)
            self.assertEqual(rec["scope"], scope)
            self.assertEqual(set(rec["evidence"]), {"title.sent", "title.stored", "title.diff"})
            self.assertNoFurtherWrites(g, gh, git, "issue.create", scope)

    def test_q5_narrowing_conditions(self):
        x = "Some content."
        cases = [   # (sent, stored, expected scope)
            (x + F, x + F + F, "global"),                  # doubled footer
            (x + F, x, "operation"),                       # footer removed
            (x, x + "\n" + CORE, "operation"),             # one newline before the footer
            (x, x + F + F, "global"),                      # doubled footer appended
            (x, x + "\n\n\n", "operation"),               # newlines only
            (x, x + F + "  ", "global"),                   # spaces after the footer
            (x, x + "\n\nSigned-off-by: someone", "global"),     # appended text
            (x, x + "\n\n---\n_Generated by Claude Code_", "global"),   # footer-like, not exact
            (x + "  ", x + F, "global"),                   # hard break removed: inside content
            (x, x[:-1] + F, "global"),                     # last content character changed
            (x, "Same content." + F, "global"),            # content change
            ("", "anything", "global"),                    # empty sent content
        ]
        for sent, stored, scope in cases:
            self.setUp()
            self.assertEqual(expect_footer_shaped(sent, stored), scope == "operation")
            self.assertEqual(TR.footer_shaped_tail(sent, stored), scope == "operation",
                             (sent, stored))
            gh = MockGitHub2(issues(), transforms={"patch": lambda b, t=stored: t}); git = MockGit()
            g = self.gate(gh, git)
            with self.assertRaises(Halted):
                g.write("issue.edit_body", 1, {"body": sent})
            mech = "issue.edit_body" if scope == "operation" else None
            self.assertEqual(self.halt_record(mech)["scope"], scope, (sent, stored))
            self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", scope)

    def test_q6_outstanding_marker_of_another_operation_makes_it_global(self):
        with open(self.marker("comment.create"), "w") as f:
            f.write("{}")
        self.notify("comment.create")
        gh = MockGitHub2(issues(), transforms={"patch": DROP}); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(gh, git).write("issue.edit_body", 1, {"body": "x" + F})
        self.assertEqual(self.halt_record()["scope"], "global")
        self.assertFalse(os.path.exists(self.marker("issue.edit_body")))

    def test_q7_internal_exception_latches_and_is_global(self):
        gh = MockGitHub2(issues()); git = MockGit()
        g = self.gate(gh, git, reg={"comment.create": "not a dict", "issue.edit_body":
                                    {"validated": True, "send_form": None}})
        with self.assertRaises(Halted):
            g.write("comment.create", 1, {"body": "c"})
        self.assertIn("exception during write", self.halt_record()["reason"])
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "e"})
        self.assertEqual(len(gh.writes), 0)

    def test_q8_marker_embeds_texts_when_evidence_files_fail(self):
        gh = MockGitHub2(issues(), transforms={"patch": lambda b: "?" + b}); git = MockGit()
        g = Gate2(gh, git, self.dir, REPO, registry(), ALLOWED,
                  evidence_dir=os.path.join(self.dir, "missing", "dir"), plan_id=self.plan)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "body text"})
        ev = self.halt_record()["evidence"]
        self.assertEqual(ev["body.sent"]["text"], "body text")
        self.assertEqual(ev["body.stored"]["text"], "?body text")
        self.assertIsNone(ev["body.sent"]["file"])
        self.assertIn("error", ev["body.sent"])


# --------------------------------------------------------------------------------------------
class Revision3(Base):
    """Revision r3: owner decisions Q2-Q4 of 2026-11-25 and review findings G1-G3."""

    def subprocess_write(self, plan):
        """A separate writer process (a restart) running plan, writing one comment."""
        code = ("import sys; sys.path.insert(0, %r)\n"
                "from gate2 import *; from mock2 import *\n"
                "gh = MockGitHub2({1: {'number': 1, 'title': 't', 'body': 'b', 'labels': [], "
                "'state': 'open'}}); mk = lambda: Gate2(gh, MockGit(), %r, 'o/r', "
                "{'comment.create': {'validated': True, 'send_form': None, 'allowlist': True}}, "
                "plan_id=%r)\n"
                "rc = main([lambda: mk().write('comment.create', 1, {'body': 'x'})])\n"
                "print(len(gh.writes), gh.gets); sys.exit(rc)\n") % (HERE, self.dir, plan)
        p = subprocess.run([sys.executable, "-I", "-B", "-c", code], capture_output=True, text=True)
        return p.returncode, p.stdout.strip(), p.stderr

    def test_q9_appended_text_stops_globally(self):
        """Q2: only newlines and exact footers appended may confine a stop to the operation; any
        other appended text is global. Recognizing the shape is not acceptance."""
        x = "Some content."
        cases = {
            "injected link": (x, x + "\n\nSee [evil](https://x.example)", "global"),
            "forged owner line": (x, x + F + "\n\nOwner decision (amaybaum, 2026-11-25): "
                                  "\"Approved.\"", "global"),
            "spaces after footer": (x, x + F + "  ", "global"),
            "look-alike footer": (x, x + F.replace("Generated", "G\u0435nerated"), "global"),
            "bot tag": (x, x + " [bot]", "global"),
            "doubled footer": (x, x + F + F, "global"),
            "one newline before footer": (x, x + "\n" + CORE, "operation"),
            "footer removed": (x + F, x, "operation"),
        }
        for name, (sent, stored, scope) in cases.items():
            self.assertEqual(TR.classify(sent, stored), ("rejected", None), name)
            self.assertEqual(TR.footer_shaped_tail(sent, stored), scope == "operation", name)
            self.assertEqual(self.check_rejected_through_gate(sent, stored, name), scope, name)
        self.assertTrue(TR.footer_shaped_tail(x, x + F))            # accepted case: same shape,
        self.assertEqual(TR.classify(x, x + F)[0], "permitted")     # acceptance by the rule only
        self.setUp()                                                # titles likewise
        gh = MockGitHub2(issues(), title_transform=lambda t: t + " [bot]"); git = MockGit()
        g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.create", None, {"title": "t", "body": "b" + F})
        self.assertEqual(self.halt_record()["scope"], "global")
        self.assertNoFurtherWrites(g, gh, git, "issue.create", "global")

    def test_q10_plan_latch_survives_restart(self):
        """Q3: after an operation-level halt and the owner told, the same plan writes nothing in a
        restarted process or a new gate; a new plan writes another operation."""
        gh = MockGitHub2(issues(), transforms={"patch": DROP}); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(gh, git).write("issue.edit_body", 1, {"body": "x" + F})
        self.assertEqual(self.halt_record("issue.edit_body")["scope"], "operation")
        latch = os.path.join(self.dir, G2.PLAN_PREFIX + self.plan)
        with open(latch) as f:
            self.assertEqual(json.load(f)["plan_id"], self.plan)
        self.notify("issue.edit_body")
        del G2._HALTED[:]                              # restart in this process: memory empty
        with self.assertRaises(Halted) as cm:
            SAMPLE["comment.create"](self.gate(gh, git))
        self.assertIn(G2.PLAN_PREFIX, str(cm.exception))
        with self.assertRaises(Halted):
            SAMPLE["push"](self.gate(gh, git))
        self.assertEqual((len(gh.writes), len(git.runs)), (1, 0))
        rc, out, err = self.subprocess_write(self.plan)          # restart in another process
        self.assertEqual((rc, out), (3, "0 0"), err)
        self.assertIn(G2.PLAN_PREFIX, err)
        os.remove(os.path.join(self.dir, G2.PLAN_RECORD))         # by hand: the plan has ended
        G2.record_plan(self.dir, "later-plan")
        rc, out, err = self.subprocess_write("later-plan")       # a later sequence
        self.assertEqual((rc, out), (0, "1 1"), err)

    def test_q11_plan_id_required_and_checked(self):
        gh = MockGitHub2(issues())
        with self.assertRaises(TypeError):
            Gate2(gh, MockGit(), self.dir, REPO, registry(), ALLOWED)
        for bad in ("", ".hidden", "../x", "a/b", "x" * 101, None, 7):
            with self.assertRaises(ValueError, msg=repr(bad)):
                Gate2(gh, MockGit(), self.dir, REPO, registry(), ALLOWED, plan_id=bad)
        self.assertEqual(len(gh.writes), 0)

    def test_q12_permitted_difference_and_validation(self):
        """Q4: a permitted difference validates under the allowlist (single-write grant) and is
        accepted on an operation validated under it; an operation validated by exact read-back
        only is held to byte identity until revalidated."""
        gh = MockGitHub2(issues(), mode="append_if_absent"); git = MockGit()
        g = self.gate(gh, git, reg=registry(validated=False))
        g.grant_single_write("issue.edit_body", 1)
        res = g.write("issue.edit_body", 1, {"body": "plain"})
        self.assertEqual(res.outcomes["body"], ["permitted", "footer-attribution-1"])
        self.assertEqual(len(res.records), 1)
        res = self.gate(gh, git, reg=registry(allowlist=True)).write(
            "issue.edit_body", 2, {"body": "plain two"})
        self.assertEqual(res.outcomes["body"][0], "permitted")
        held = registry(allowlist=False)
        self.assertEqual(self.gate(gh, git, reg=held).write(
            "issue.edit_body", 3, {"body": "exact" + F}).outcomes["body"][0], "exact")
        w = len(gh.writes)
        g = self.gate(gh, git, reg=held)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 4, {"body": "plain four"})
        self.assertEqual(len(gh.writes), w + 1)
        rec = self.halt_record("issue.edit_body")
        self.assertIn("held to exact read-back", rec["reason"])
        self.assertEqual(rec["scope"], "operation")
        self.assertEqual(len([p for p in os.listdir(self.dir) if p.startswith("discrepancy")]), 2)
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "operation")

    def test_q13_labels_and_state_checked_on_every_write(self):
        """G1: labels and state are compared on every write, against the pre-write read or the
        values a new object has; any difference is global."""
        def empty_labels(iss, n): iss[n]["labels"] = []
        def close(iss, n): iss[n]["state"] = "closed"
        def add_label(iss, n): iss[n]["labels"].append({"name": "z"})
        def retitle(iss, n): iss[n]["title"] = "changed"
        cases = [
            ("issue.edit_body", lambda g: g.write("issue.edit_body", 1, {"body": "x" + F}),
             empty_labels, {"patch": DROP}, "labels"),     # reviewer's probe
            ("issue.edit_body", lambda g: g.write("issue.edit_body", 1, {"body": "x" + F}),
             empty_labels, {}, "labels"),
            ("issue.edit_body", lambda g: g.write("issue.edit_body", 1, {"body": "x" + F}),
             close, {}, "state"),
            ("issue.create", lambda g: g.write("issue.create", None, {"title": "t", "body": "b"}),
             add_label, {}, "labels"),
            ("pr.edit", lambda g: g.write("pr.edit", 5, {"body": "p" + F}), retitle, {}, "title"),
            ("issue.close", lambda g: g.write("issue.close", 4, {}), add_label, {}, "labels"),
            ("labels.add", lambda g: g.write("labels.add", 3, {}, labels=["b"]), close, {},
             "state"),
        ]
        for op, call, side, tf, key in cases:
            self.setUp()
            gh = MockGitHub2(issues(), transforms=tf, after_write=side); git = MockGit()
            g = self.gate(gh, git)
            with self.assertRaises(Halted, msg=(op, key)):
                call(g)
            rec = self.halt_record()
            self.assertEqual(rec["scope"], "global", (op, key))
            self.assertIn("%s read-back differs" % key, rec["reason"])
            self.assertIn("unsent-%s.stored" % key, rec["evidence"])
            self.assertNoFurtherWrites(g, gh, git, op, "global")

    def test_q14_stale_or_existing_operation_marker_makes_it_global(self):
        """G2: a .notified companion left from an earlier incident, or an operation marker that
        appears meanwhile, makes a footer-shaped halt global."""
        open(self.marker("issue.edit_body") + ".notified", "w").close()
        gh = MockGitHub2(issues(), transforms={"patch": DROP}); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(gh, git).write("issue.edit_body", 1, {"body": "x" + F})
        self.assertEqual(self.halt_record()["scope"], "global")
        self.assertFalse(os.path.exists(self.marker("issue.edit_body")))
        self.assertGlobalStop(git, "issue.edit_body")
        self.setUp()
        gets = []

        def other_process_halts():
            gets.append(1)
            if len(gets) == 2:                      # during the read-back
                with open(self.marker("issue.edit_body"), "w") as f:
                    f.write("{}")
        gh = MockGitHub2(issues(), transforms={"patch": DROP},
                         before_get=other_process_halts)
        with self.assertRaises(Halted) as cm:
            self.gate(gh, git).write("issue.edit_body", 1, {"body": "x" + F})
        self.assertIn("halt made global", str(cm.exception))
        rec = self.halt_record()
        self.assertEqual((rec["scope"], rec["escalated_from"]), ("global", "issue.edit_body"))
        with open(self.marker("issue.edit_body")) as f:
            self.assertEqual(f.read(), "{}")

    def test_q15_store_rechecked_before_the_write_request(self):
        """G3: a halt recorded during the pre-write read stops the write request itself."""
        def halt_elsewhere():
            with open(self.marker(), "w") as f:
                f.write("{}")
        gh = MockGitHub2(issues(), before_get=halt_elsewhere); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(gh, git).write("issue.edit_body", 1, {"body": "x" + F})
        self.assertEqual((len(gh.writes), gh.gets), (0, 1))
        self.assertTrue(os.path.exists(os.path.join(self.dir, G2.PLAN_PREFIX + self.plan)))


class Revision4(Base):
    """Revision r4: owner decision of 2026-11-25 (#1169 comment 7170157100), items 1 and 2."""
    subprocess_write = Revision3.subprocess_write

    def test_q16_plan_id_only_from_the_plan_record(self):
        """Item 1: the plan id is fixed in the plan record before the run; a caller cannot
        substitute another, in this process, after a restart or in a separate process."""
        record = os.path.join(self.dir, G2.PLAN_RECORD)
        gh = MockGitHub2(issues()); git = MockGit()
        with self.assertRaises(FileExistsError):             # never rewritten while it exists
            G2.record_plan(self.dir, "another-plan")
        with open(record) as f:
            self.assertEqual(json.load(f)["plan_id"], self.plan)
        with self.assertRaises(Halted) as cm:                # substituted id, before any halt
            Gate2(gh, git, self.dir, REPO, registry(), ALLOWED, plan_id="another-plan")
        self.assertIn("differs from the plan record", str(cm.exception))
        del G2._HALTED[:]
        os.remove(record)                                    # no record: refused
        with self.assertRaises(Halted) as cm:
            self.gate(gh, git)
        self.assertIn("no readable plan record", str(cm.exception))
        del G2._HALTED[:]
        G2.record_plan(self.dir, self.plan)
        g = self.gate(gh, git)                               # the record swapped mid-run
        os.remove(record); G2.record_plan(self.dir, "swapped-plan")
        with self.assertRaises(Halted) as cm:
            SAMPLE["comment.create"](g)
        self.assertIn("differs from the plan record", str(cm.exception))
        self.assertEqual((len(gh.writes), gh.gets, len(git.runs)), (0, 0, 0))
        rc, out, err = self.subprocess_write("another-plan")  # separate process, substituted id
        self.assertEqual((rc, out), (3, "0 0"), err)
        self.assertIn("differs from the plan record", err)

    def test_q17_restart_after_halt_same_or_substituted_id(self):
        """Item 1: after an operation-level halt and the owner told, neither the same id nor a
        substituted one continues the plan, in this process or in a separate one."""
        gh = MockGitHub2(issues(), transforms={"patch": lambda b: b + "\n"}); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(gh, git).write("issue.edit_body", 1, {"body": "x"})
        self.assertEqual(self.halt_record("issue.edit_body")["scope"], "operation")
        self.notify("issue.edit_body")
        for plan in (self.plan, "substituted-%d" % os.getpid()):
            del G2._HALTED[:]                                # restart in this process
            with self.assertRaises(Halted, msg=plan):
                Gate2(gh, git, self.dir, REPO, registry(), ALLOWED,
                      plan_id=plan).write("comment.create", 1, {"body": "y"})
            rc, out, err = self.subprocess_write(plan)       # restart in a separate process
            self.assertEqual((rc, out), (3, "0 0"), (plan, err))
        self.assertEqual((len(gh.writes), len(git.runs)), (1, 0))

    def test_q18_at_most_one_footer_copy_narrows(self):
        """Item 2: one appended footer copy (plus newlines) narrows to the operation; two or more
        copies are global."""
        x = "Some content."
        cases = [(x, x + "\n" + CORE + "\n\n", "operation"),          # one copy, newlines
                 (x + F, x + "\n", "operation"),                      # no copy, newlines
                 (x, x + F + F, "global"),                            # two copies
                 (x, x + F * 50, "global"),                           # fifty copies
                 (x + F, x + F + "\n" + CORE, "global")]              # two, joined
        for sent, stored, scope in cases:
            self.assertEqual(TR.classify(sent, stored), ("rejected", None), (sent, stored))
            self.assertEqual(TR.footer_shaped_tail(sent, stored), scope == "operation",
                             (sent, stored))
            self.assertEqual(self.check_rejected_through_gate(sent, stored, repr(stored[-40:])),
                             scope)


# --------------------------------------------------------------------------------------------
class PortedGuarantees(Base):
    """gate.py's guarantees, under v2's containment: every failure but a footer-shaped read-back
    mismatch meeting rule 3's conditions is global."""

    def test_g01_verbatim_success(self):
        gh = MockGitHub2(issues()); g = self.gate(gh)
        r1 = g.write("issue.edit_body", 1, {"body": "new" + F})
        r2 = g.write("comment.create", 1, {"body": "c" + F})
        self.assertEqual((r1.records, r2.records), ([], []))
        self.assertEqual(len(gh.writes), 2)
        self.assertEqual(os.listdir(self.dir), [G2.PLAN_RECORD])

    def test_g04_readback_failure_halts(self):
        for mode in ("readback_fail_after_write", "readback_404"):
            self.setUp()
            gh = MockGitHub2(issues(), mode=mode); git = MockGit(); g = self.gate(gh, git)
            with self.assertRaises(Halted):
                g.write("comment.create", 1, {"body": "c" + F})
            self.assertIn("read-back failed", self.halt_record()["reason"])
            self.assertNoFurtherWrites(g, gh, git, "comment.create", "global")

    def test_g05_exception_unknown_outcome_halts(self):
        gh = MockGitHub2(issues(), mode="raise_on_write"); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.create", None, {"title": "t", "body": "b" + F})
        self.assertIn("unknown outcome", self.halt_record()["reason"])
        self.assertNoFurtherWrites(g, gh, git, "issue.create", "global")

    def test_g06_bad_status_halts(self):
        gh = MockGitHub2(issues(), mode="status_500"); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "b" + F})
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "global")

    def test_g09_prechecks_refuse_before_write(self):
        long = "https://github.com/o/r/blob/" + "f" * 40 + "/" + "p" * 60
        for t in ["a\r\nb", "zero\u200bwidth", "nb\u00a0sp", "\ufeffbom", "see " + long,
                  "  OI-form comment\nx"]:
            self.setUp()
            gh = MockGitHub2(issues()); git = MockGit(); g = self.gate(gh, git)
            with self.assertRaises(Halted, msg=repr(t)):
                g.write("comment.create", 1, {"body": t + F})
            self.assertEqual(len(gh.writes), 0, repr(t))
            self.assertIn("pre-check", self.halt_record()["reason"])
            self.assertNoFurtherWrites(g, gh, git, "comment.create", "global")

    def test_g10_unvalidated_needs_single_grant(self):
        gh = MockGitHub2(issues()); git = MockGit(); g = self.gate(gh, git, registry(False))
        g.grant_single_write("issue.edit_body", 1)
        g.write("issue.edit_body", 1, {"body": "one" + F})
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "two" + F})
        self.assertEqual(len(gh.writes), 1)
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "global")

    def test_g11_fields_mismatch_halts(self):
        gh = MockGitHub2(issues()); git = MockGit(); g = self.gate(gh, git)
        with self.assertRaises(Halted):
            g.write("issue.edit_body", 1, {"body": "b", "title": "t"})
        self.assertEqual(len(gh.writes), 0)
        self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "global")

    def test_g12_labels_and_close_verbatim(self):
        gh = MockGitHub2(issues()); g = self.gate(gh)
        g.write("labels.add", 1, {}, labels=["b"])
        g.write("labels.remove", 1, {}, label="a")
        g.write("issue.close", 1, {})
        self.assertEqual([x["name"] for x in gh.issues[1]["labels"]], ["b"])
        self.assertEqual(os.listdir(self.dir), [G2.PLAN_RECORD])

    def test_g15_canonical_footer_body_matches_gate(self):
        for raw in ("text\n\n\n\n" + CORE, "Parent: #1169\n" + F, "text   \n  ", "text  " + F,
                    "text" + F, "text" + F + "\n", "text"):
            self.assertEqual(TR.canonical_footer_body(raw), G.canonical_footer_body(raw), repr(raw))

    def test_g16_noncanonical_refused_before_write(self):
        for raw in ("x\n" + F, "x  " + F, "x" + F + "\n", "no footer"):
            self.setUp()
            gh = MockGitHub2(issues()); git = MockGit(); g = self.gate(gh, git, registry(form="footer"))
            with self.assertRaises(Halted):
                g.write("issue.edit_body", 1, {"body": raw})
            self.assertEqual(len(gh.writes), 0)
            self.assertIn("pre-check", self.halt_record()["reason"])
            self.assertNoFurtherWrites(g, gh, git, "issue.edit_body", "global")

    def test_g17_canonical_send_form_exact_under_separator_canonicalization(self):
        for raw in ("text\n\n\n" + CORE, read("issue-1505", "sent.md"), "t  \n", "t" + F):
            self.setUp()
            gh = MockGitHub2(issues(), mode="canonicalize_separator")
            g = self.gate(gh, reg=registry(form="footer"))
            res = g.write("issue.edit_body", 1, {"body": TR.canonical_footer_body(raw)})
            self.assertEqual(res.outcomes["body"][0], "exact")

    def test_g13_refused_refspecs(self):
        bad = [("", ALLOWED[0]), ("abc", ALLOWED[0]), ("A" * 40, ALLOWED[0]), ("a" * 39, ALLOWED[0]),
               ("+" + SHA, ALLOWED[0]), (SHA, "refs/heads/main"), (SHA, "refs/heads/other"),
               (SHA, ""), (SHA, "refs/tags/v1"), (SHA + ":refs/heads/x", ALLOWED[0]),
               ("--delete", ALLOWED[0])]
        for sha, ref in bad:
            self.setUp()
            gh = MockGitHub2(issues()); git = MockGit(); g = self.gate(gh, git)
            with self.assertRaises(Halted, msg=(sha, ref)):
                g.push("origin", sha, ref)
            self.assertEqual(git.runs, [], (sha, ref))
            self.assertNoFurtherWrites(g, gh, git, "push", "global")
            self.assertGlobalStop(git, "push")
        self.setUp(); git = MockGit()
        with self.assertRaises(Halted):
            self.gate(MockGitHub2(), git).push("--force", SHA, ALLOWED[0])
        self.assertEqual(git.runs, [])
        self.assertIn("plain remote name", self.halt_record()["reason"])

    def test_g14_push_paths(self):
        git = MockGit(); g = self.gate(MockGitHub2(issues()), git)
        self.assertEqual(g.push("origin", SHA, ALLOWED[0]), SHA)
        git.ancestors.add((SHA, SHA2))
        self.assertEqual(g.push("origin", SHA2, ALLOWED[0]), SHA2)
        self.assertEqual(git.runs[0], ["git", "push", "--porcelain", "--", "origin",
                                       "%s:%s" % (SHA, ALLOWED[0])])
        for kw, refs in ((dict(rc=1), {}), (dict(raise_on_run=True), {}), (dict(lie=True), {}),
                         (dict(), {ALLOWED[0]: SHA2})):
            self.setUp()
            gh = MockGitHub2(issues()); git = MockGit(refs=refs, **kw); g = self.gate(gh, git)
            with self.assertRaises(Halted, msg=kw):
                g.push("origin", SHA, ALLOWED[0])
            self.assertNoFurtherWrites(g, gh, git, "push", "global")


if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    unittest.main(verbosity=2)
