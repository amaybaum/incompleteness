"""Offline tests for write_canon.py: python3 -I -m unittest discover -s tools/write_canon"""
import fcntl, json, os, re, subprocess, tempfile, unittest
from pathlib import Path

import write_canon as W

FX = Path(__file__).resolve().parent / "fixtures"
F, TAIL = W.F, W.TAIL
LOCAL = "https://github.com/amaybaum/incompleteness/blob/413b0bb88f39cad901befcf4684355c7ee39480b/AGENTS.md"
OK_BODY = "**Test** per [#1169](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7080958038)\n\n- item with `code`\n  - nested\n- link: " + LOCAL + "\n\n| a | b |\n|---|---|\n| `x` | **y** |\n"


def fx(name):
    return (FX / name).read_bytes().decode("utf-8")


def unsupported(body):
    return W.check(body)["constructs"]["unsupported"]


class Normalization(unittest.TestCase):
    CASES = ["x", "x\n", "x\n\n\n\n", "x\n---\n" + F, "x\n\n---\n" + F + "\n", "x" + TAIL, "x" + TAIL + TAIL,
             "x\n" + F, "x\n---\n", "x\n---\n" + F + "\ntrailing text", "x\n---\n" + F + "\n\n---\n" + F + "\n",
             "x\n---\n" + F[:-1], "---\n" + F, "x---\n" + F, "x\t\n\n", "\n\n---\n" + F, "Title\n---\n" + F,
             "Values x---\n" + F, "x\n\n---\n" + F + "\n\n---\n" + F]

    def all_inputs(self):
        return self.CASES + [fx(p.name) for p in sorted(FX.iterdir())]

    def test_idempotent(self):
        for s in self.all_inputs():
            self.assertEqual(W.normalize(W.normalize(s)), W.normalize(s), repr(s[-80:]))

    def test_identity_outside_footer(self):
        for s in self.all_inputs():
            c = W.core(s)
            self.assertTrue(s.startswith(c))
            rest, foot = s[len(c):], re.escape(F)
            self.assertTrue(re.fullmatch(r"\n*", rest) or re.fullmatch(r"\n\n+---\n%s\n*" % foot, rest)
                            or (c == "" and re.fullmatch(r"---\n%s\n*" % foot, rest)), repr(rest))
            self.assertEqual(W.normalize(s), c + TAIL)

    def test_footer_variants(self):
        n = W.normalize
        self.assertEqual(n("x"), "x" + TAIL)                                # missing
        self.assertEqual(n("x\n\n---\n" + F + "\n"), "x" + TAIL)            # one blank line
        self.assertEqual(n("x\n\n\n\n"), "x" + TAIL)                        # trailing newlines
        self.assertEqual(n("x" + TAIL + TAIL), "x" + TAIL + TAIL)           # repeated: one is body
        self.assertEqual(n("x\n" + F), "x\n" + F + TAIL)                    # footer missing its rule
        self.assertEqual(n("x\n---\n"), "x\n---" + TAIL)                    # rule with no footer
        self.assertEqual(n("x\n---\n" + F + "\nmore"), "x\n---\n" + F + "\nmore" + TAIL)
        for body in ("x" + TAIL + TAIL, "x\n" + F, "x\n---\n", "x\n---\n" + F + "\nmore"):
            self.assertFalse(W.check(body)["ok"], body)                     # leftover footer parts fail closed

    def test_footer_boundaries(self):
        n = W.normalize
        self.assertEqual(n("Values x---\n" + F), "Values x---\n" + F + TAIL)     # mid-line rule keeps its bytes
        self.assertEqual(n("Title\n---\n" + F), "Title\n---\n" + F + TAIL)     # setext H2 is not a footer
        self.assertEqual(n("x\n---\n" + F), "x\n---\n" + F + TAIL)             # no blank line before the rule
        self.assertEqual(n("x\n\n---\n" + F), "x" + TAIL)                       # blank line: footer
        self.assertEqual(n("---\n" + F + "\n"), TAIL)                            # footer is the whole body
        self.assertEqual(n("\n\n---\n" + F), TAIL)
        self.assertTrue(W.check("x\n\n---\n" + F)["ok"])
        for body in ("Values x---\n" + F, "Title\n---\n" + F, "x\n---\n" + F, "---\n" + F):
            self.assertFalse(W.check(body)["ok"], body)

    def test_non_ascii_whitespace(self):
        for ws in ("\u00a0", "\u2003", "\u3000", "\u1680", "\u202f", "\u2028", "\u0085"):
            r = W.check("- " + LOCAL + ws + "x")
            self.assertFalse(r["ok"] or r["integrity"]["ok"] or r["links"]["ok"], repr(ws))
            self.assertEqual(r["links"]["links"], [])

    def test_forbidden_characters(self):
        for bad in ("a\rb", "a\r\n", "a\0", "a\x1b[0m", "a\x7f", "a\x85"):
            r = W.check(bad)
            self.assertFalse(r["integrity"]["ok"], repr(bad))
        self.assertTrue(W.check("a\tb")["integrity"]["ok"])
        self.assertFalse(W.check("- " + LOCAL + "\r")["links"]["ok"])      # not reported as checked


class Fixtures(unittest.TestCase):
    def test_bloblink_round_trip(self):
        r = W.check(fx("bloblink-source.md"), fx("bloblink-stored.md"))
        self.assertTrue(r["ok"], r)
        self.assertEqual(r["integrity"]["expected_sha256"],
                         "6f2ac910e3b423a26234a903806ab4e2471c4fbfd8d18bac307b8399da261a60")
        self.assertEqual(r["links"]["links"][0]["status"], "verified-local")

    def test_receipt_1548(self):
        src, st = fx("receipt1548-source.md"), fx("receipt1548-stored.md")
        self.assertIn("8dd58694…/README.md".encode("utf-8"), (FX / "receipt1548-source.md").read_bytes())
        self.assertIn(b"8dd58694\xe2\x80\xa6/README.md", W.normalize(src).encode("utf-8"))
        r = W.check(src, st)
        self.assertTrue(r["integrity"]["ok"] and r["integrity"]["stored_matches_expected"])
        self.assertEqual(r["integrity"]["source_sha256"],
                         "1b138061b739cfb22f9f9ffb80874ae0a069437963a2bcbd355b2185d682bd81")
        self.assertTrue(r["links"]["ok"])                         # ellipsis URL is inside a code span
        self.assertEqual(r["constructs"]["inventory"]["bracket-code-literal"], 1)
        # the byte match does not certify rendering: "body=@file" outside code is a mention
        self.assertEqual(r["constructs"]["unsupported"], ["line 23: mention or e-mail autolink"])
        self.assertFalse(r["ok"])

    def test_issue_1169_corruption(self):
        sub, st = fx("issue1169-submitted.md"), fx("issue1169-stored.md")
        r = W.check(sub, st)
        self.assertFalse(r["integrity"]["stored_matches_expected"])
        self.assertFalse(r["links"]["ok"])
        self.assertFalse(r["constructs"]["ok"])                  # headings, HTML, block quotes
        # Apart from the capture's final newline, the stored body is N(submitted) with backtick runs
        # (and one adjacent space) inserted around link destinations, and nothing else.
        exp, got, i, j, ins = W.normalize(sub), st[:-1], 0, 0, 0
        self.assertTrue(st.endswith(TAIL + "\n"))
        while i < len(exp) or j < len(got):
            if i < len(exp) and j < len(got) and exp[i] == got[j]:
                i, j = i + 1, j + 1
                continue
            k = j + (got[j:j + 2] == " `")
            while k < len(got) and got[k] == "`":
                k += 1
            self.assertGreater(k, j + (got[j] == " "), "non-backtick difference at %d" % j)
            if got[j] != " " and k < len(got) and got[k] == " " and (i >= len(exp) or exp[i] != " "):
                k += 1
            ins, j = ins + 1, k
        self.assertEqual(ins, 38)                         # 19 links, opened and closed


class Scanner(unittest.TestCase):
    def test_allowed_constructs(self):
        r = W.check(OK_BODY)
        self.assertTrue(r["ok"], r)
        inv = r["constructs"]["inventory"]
        for k in ("bold", "bullet-list", "nested-list", "table", "code-span", "bare-blob-link", "issue-link"):
            self.assertIn(k, inv)

    def test_code_spans(self):
        self.assertEqual(W.code_spans("a ``b ` c`` d")[1], [(2, 11, "b ` c")])
        self.assertEqual(len(W.code_spans("`a` and ```b``c```")[1]), 2)
        self.assertTrue(W.check("x ``with ` inside`` y")["ok"])
        self.assertTrue(W.check("x `" + LOCAL[:60] + "…/AGENTS.md` y")["ok"])

    def test_adversarial_backticks(self):
        for body in ("a `b", "a ``b`", "a `b``", "`a\nb`", "a ```b`` c", "a \\`b`", "[a `b` c](https://github.com/o/r/issues/1)",
                     "a `b` `c", "```\ncode\n```", "~~~\ncode\n~~~", "```\nunclosed"):
            self.assertTrue(unsupported(body), repr(body))

    def test_unsupported_fail_closed(self):
        bodies = ["# h", "## h", "Title\n===", "Title\n---", "***", "> quote", "<b>x</b>", "a <br> b", "a &amp; b",
                  "![i](https://x.y/i.png)", "[ref][r]\n\n[r]: https://x.y", "[^1]", "[sic]", "*em*", "_em_",
                  "a ~~s~~", "1. one", "+ plus", "* star", "    code", "  lead", "@someone", "a :smile: b",
                  "a\\*b", "line  ", "line\\", "a | b", "| a |", "| a |\n|---|\n| b | c |", "- x\n  continued",
                  "- x\ncontinued", "- - x", "-", "- ", "  - jump", "- a\n    - jump", "https://example.com",
                  "see " + LOCAL + ".", "(" + LOCAL + ")", "[a](https://example.com)", "[a](https://github.com/other/repo/issues/1)", "a​b", "a b",
                  "x\n\n---\n\ny", "- | a | b |", "| - a | b |\n|---|---|\n| c | d |", "| `a|b` | c |\n|---|---|",
                  "| a | b |\n|---|---|\ntext", "**a\nb**", "a**b**c", "**a"]
        for body in bodies:
            r = W.check(body)
            self.assertFalse(r["ok"], repr(body))

    def test_review_bypasses(self):
        for body in ("where $a_1$ is", "$$\nx\n$$", "math $`x`$ here", "fetch ftp://example.com/a", "FTP://x.y/a",
                     "see foo://bar", "- " + LOCAL + "<x", "see owner/repo#5", "see owner/repo@abc1234", "see GH-12",
                     "see gh-12", "[#12](https://github.com/amaybaum/incompleteness/issues/13)"):
            self.assertFalse(W.check(body)["ok"], repr(body))
        self.assertTrue(W.check("[#12](https://github.com/amaybaum/incompleteness/issues/12)")["ok"])
        self.assertTrue(W.check("a `$x$ ftp://x owner/repo#5` b")["ok"])            # literals inside code

    def test_unsupported_does_not_rewrite(self):
        body = "# h\n\n<b>x</b>"
        self.assertEqual(W.normalize(body), body + TAIL)


class Links(unittest.TestCase):
    def test_full_local(self):
        r = W.check("- " + LOCAL)
        self.assertEqual(r["links"]["links"][0]["status"], "verified-local")

    def test_nonexistent(self):
        for url in (LOCAL.replace("413b0bb8", "00000000"), LOCAL.replace("AGENTS.md", "NO-SUCH-FILE.md"),
                    LOCAL.replace("AGENTS.md", "tools")):
            r = W.check("- " + url)
            self.assertFalse(r["links"]["ok"], url)

    def test_foreign_repo_unverified_offline(self):
        url = LOCAL.replace("amaybaum/incompleteness", "other/repo")
        r = W.check("- " + url)
        self.assertFalse(r["ok"])
        self.assertTrue(r["links"]["links"][0]["status"].startswith("unverified"))

    def test_shortened(self):
        short = "https://github.com/amaybaum/incompleteness/blob/413b0bb8…/AGENTS.md"
        self.assertFalse(W.check("- " + short)["links"]["ok"])
        self.assertFalse(W.check("- " + LOCAL.replace("413b0bb88f39cad901befcf4684355c7ee39480b", "413b0bb"))["links"]["ok"])
        self.assertTrue(W.check("- `" + short + "`")["ok"])

    def test_reachability_from_origin_refs(self):
        env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        env.update(GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t", GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t")
        with tempfile.TemporaryDirectory() as d:
            def g(*a):
                return subprocess.run(["git", "-C", d] + list(a), env=env, check=True, capture_output=True,
                                      text=True).stdout.strip()
            g("init", "-q")
            Path(d, "f").write_text("x\n")
            g("add", "f")
            g("commit", "-q", "-m", "a")
            pushed = g("rev-parse", "HEAD")
            g("update-ref", "refs/remotes/origin/main", pushed)
            g("commit", "-q", "--allow-empty", "-m", "b")
            local = g("rev-parse", "HEAD")
            dangling = g("commit-tree", pushed + "^{tree}", "-m", "c")
            fork = g("commit-tree", pushed + "^{tree}", "-m", "d")
            g("update-ref", "refs/remotes/upstream/x", fork)
            old, W.REPO_ROOT = W.REPO_ROOT, Path(d)
            try:
                url = "https://github.com/amaybaum/incompleteness/blob/%s/f"
                self.assertEqual(W.check("- " + url % pushed)["links"]["links"][0]["status"], "verified-local")
                for sha in (local, dangling, fork):
                    st = W.check("- " + url % sha)["links"]["links"][0]["status"]
                    self.assertTrue(st.startswith("unverified"), st)
            finally:
                W.REPO_ROOT = old
            saved = {k: os.environ.get(k) for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_OBJECT_DIRECTORY")}
            os.environ.update(GIT_DIR=str(Path(d, ".git")), GIT_WORK_TREE=d, GIT_OBJECT_DIRECTORY=str(Path(d, "x")))
            try:                                                  # GIT_* from the environment is ignored
                self.assertEqual(W.check("- " + LOCAL)["links"]["links"][0]["status"], "verified-local")
            finally:
                for k, v in saved.items():
                    os.environ.pop(k, None) if v is None else os.environ.__setitem__(k, v)

    def test_inline_blob_link_rejected(self):
        r = W.check("[guide](" + LOCAL + ")")
        self.assertFalse(r["links"]["ok"])

    def test_nothing_expanded(self):
        body = "- `https://github.com/amaybaum/incompleteness/blob/413b0bb8…/AGENTS.md`"
        self.assertEqual(W.normalize(body), body + TAIL)


class Mutants(unittest.TestCase):
    """Corruptions seen in practice: each must fail the stored-body check."""

    def test_mutants(self):
        src = fx("bloblink-source.md")
        good = W.normalize(src)
        self.assertTrue(W.check(src, good)["ok"])
        mutants = {
            "backtick-wrapped link": good.replace(LOCAL, "` " + LOCAL + " `"),
            "appended footer": good + "\n\n---\n" + F,
            "CR insertion": good.replace("\n", "\r\n", 1),
            "trailing whitespace": good.replace("unchanged.", "unchanged. ", 1),
            "dropped bytes": good.replace("bullet ", "", 1),
            "dropped final byte": good[:-1],
            "footer missing": W.core(src),
        }
        for name, m in mutants.items():
            r = W.check(src, m)
            self.assertFalse(r["ok"], name)
            self.assertFalse(r["integrity"]["stored_matches_expected"], name)
        self.assertFalse(W.check(src, mutants["backtick-wrapped link"])["links"]["ok"])


class Stub:
    """Injectable gh runner. Records every argv; no network."""

    def __init__(self, stored=None, post="ok", issue=None, created="2026-11-22T00:00:00Z", updated=None, recent=()):
        self.calls, self.stored, self.post, self.created, self.recent = [], stored, post, created, recent
        self.updated = updated or created
        self.issue = issue if issue is not None else {"number": 7}

    def __call__(self, argv):
        self.calls.append(argv)
        if argv[2:4] == ["-X", "POST"]:
            if self.post == "neterr":
                raise TimeoutError("connection reset after send")
            if self.post == "empty":
                return 0, "", ""
            if self.post == "nonjson":
                return 0, "<html>", ""
            self.body = Path(argv[6][len("body=@"):]).read_text(encoding="utf-8")
            return 0, json.dumps({"id": 123}), ""
        if "/comments?since=" in argv[2]:
            return (1, "", "HTTP 500") if self.recent == "fail" else (0, json.dumps(list(self.recent)), "")
        if "/issues/comments/" in argv[2]:
            if self.stored == "missing":
                return 1, "", "HTTP 404"
            body = W.normalize(self.body) if self.stored is None else self.stored
            return 0, json.dumps({"id": 123, "body": body, "created_at": self.created, "updated_at": self.updated,
                                  "issue_url": "https://api.github.com/repos/amaybaum/incompleteness/issues/7"}), ""
        return 0, json.dumps(self.issue), ""


class Post(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = Path(self.tmp.name)
        self.state = self.d / "state"
        self.src = self.d / "src.md"
        self.src.write_text(OK_BODY, encoding="utf-8")
        self.rcpt = self.d / "receipt.json"

    def tearDown(self):
        self.tmp.cleanup()

    def run_post(self, stub, issue="7", src=None, rcpt=None):
        return W.post(issue, str(src or self.src), str(rcpt or self.rcpt), runner=stub, state_dir=self.state)

    def posts(self, stub):
        return [c for c in stub.calls if c[2:4] == ["-X", "POST"]]

    def test_match(self):
        stub = Stub()
        code, msg = self.run_post(stub)
        self.assertEqual(code, 0, msg)
        rec = json.loads(self.rcpt.read_text())
        self.assertTrue(rec["match"] and rec["links_survived"] and rec["created_equals_updated"])
        self.assertIn("does not", rec["note"])
        self.assertIn("gh", rec["executables"])
        self.assertFalse((self.state / "PENDING").exists() or (self.state / "HALT").exists())
        self.assertEqual(self.posts(stub), [["gh", "api", "-X", "POST", "repos/amaybaum/incompleteness/issues/7/comments",
                                             "-F", "body=@%s" % (self.state / "submit.md")]])

    def assert_halted(self, stub, code):
        self.assertEqual(code, 4)
        self.assertTrue((self.state / "HALT").exists() and (self.state / "PENDING").exists())
        self.assertEqual(len(self.posts(stub)), 1)                       # never retried
        self.assertEqual(self.run_post(Stub(), rcpt=self.d / "r2.json")[0], 3)   # sticky

    def test_modified_store(self):
        stub = Stub(stored=W.normalize(OK_BODY).replace(LOCAL, "` " + LOCAL + " `"))
        code, _ = self.run_post(stub)
        self.assert_halted(stub, code)
        rec = json.loads(self.rcpt.read_text())
        self.assertFalse(rec["match"] or rec["links_survived"])

    def test_edited_after_post(self):
        stub = Stub(updated="2026-11-22T00:00:09Z")
        self.assert_halted(stub, self.run_post(stub)[0])

    def test_missing_response(self):
        for kind in ("empty", "nonjson"):
            self.tearDown()
            self.setUp()
            stub = Stub(post=kind)
            self.assert_halted(stub, self.run_post(stub)[0])

    def test_missing_verification(self):
        stub = Stub(stored="missing")
        self.assert_halted(stub, self.run_post(stub)[0])

    def test_network_error_after_submit(self):
        stub = Stub(post="neterr")
        self.assert_halted(stub, self.run_post(stub)[0])

    def test_interrupted_verification_is_sticky(self):
        stub = Stub()
        orig = stub.__call__

        def interrupt(argv):
            if "/issues/comments/" in argv[2]:
                raise KeyboardInterrupt
            return orig(argv)
        with self.assertRaises(KeyboardInterrupt):
            self.run_post(interrupt)
        self.assertTrue((self.state / "PENDING").exists())
        later = Stub()
        self.assertEqual(self.run_post(later, rcpt=self.d / "r2.json")[0], 3)
        self.assertEqual(later.calls, [])

    def test_state_location_not_an_argument(self):
        for opt in ("--halt", "--state-dir", "--pending"):
            with self.assertRaises(SystemExit):
                W.main(["post", "7", str(self.src), "--receipt", str(self.rcpt), opt, str(self.d)])

    def test_existing_halt_and_pending(self):
        for marker in ("HALT", "PENDING"):
            self.tearDown()
            self.setUp()
            self.state.mkdir(mode=0o700)
            (self.state / marker).write_text("x")
            stub = Stub()
            self.assertEqual(self.run_post(stub)[0], 3)
            self.assertEqual(stub.calls, [])

    def test_check_failure_refuses(self):
        self.src.write_text("# heading\n", encoding="utf-8")
        stub = Stub()
        self.assertEqual(self.run_post(stub)[0], 1)
        self.assertEqual(stub.calls, [])

    def test_duplicate_and_unlistable_recent_comments(self):
        for recent in ([{"body": W.normalize(OK_BODY)}], [{"body": "x"}] * 100, "fail"):
            stub = Stub(recent=recent)
            self.assertEqual(self.run_post(stub)[0], 3)
            self.assertEqual(self.posts(stub), [])

    def test_state_dir_permissions(self):
        self.state.mkdir(mode=0o700)
        os.chmod(self.state, 0o750)
        stub = Stub()
        self.assertEqual(self.run_post(stub)[0], 3)
        self.assertEqual(stub.calls, [])

    def test_foreign_link_refused_and_no_online_post(self):
        self.src.write_text("- " + LOCAL.replace("amaybaum/incompleteness", "other/repo") + "\n", encoding="utf-8")
        stub = Stub()
        self.assertEqual(self.run_post(stub)[0], 1)
        self.assertEqual(stub.calls, [])
        with self.assertRaises(SystemExit):
            W.main(["post", "7", str(self.src), "--receipt", str(self.rcpt), "--online"])

    def test_exclusive_receipt_write(self):
        self.rcpt.write_text("old")
        with self.assertRaises(FileExistsError):
            W.write_atomic(self.rcpt, "new", exclusive=True)
        self.assertEqual(self.rcpt.read_text(), "old")
        self.assertEqual([p.name for p in self.d.iterdir() if p.name.endswith(".tmp")], [])

    def test_pull_request_refused(self):
        stub = Stub(issue={"number": 7, "pull_request": {}})
        self.assertEqual(self.run_post(stub)[0], 3)
        self.assertEqual(self.posts(stub), [])

    def test_symlinks_refused(self):
        link = self.d / "link.md"
        link.symlink_to(self.src)
        stub = Stub()
        self.assertEqual(self.run_post(stub, src=link)[0], 3)
        target = self.d / "elsewhere.json"
        rlink = self.d / "rlink.json"
        rlink.symlink_to(target)
        self.assertEqual(self.run_post(stub, rcpt=rlink)[0], 3)
        self.assertFalse(target.exists())
        self.state.mkdir(mode=0o700, exist_ok=True)
        (self.state / "HALT").symlink_to(self.d / "nowhere")
        self.assertEqual(self.run_post(stub)[0], 3)
        self.assertEqual(self.posts(stub), [])
        os.unlink(self.state / "HALT")
        (self.d / "real").mkdir()
        sdir = self.d / "slink"
        sdir.symlink_to(self.d / "real")
        self.assertEqual(W.post("7", str(self.src), str(self.rcpt), runner=stub, state_dir=sdir)[0], 3)

    def test_lock(self):
        self.state.mkdir(mode=0o700)
        fd = os.open(self.state / "lock", os.O_RDWR | os.O_CREAT, 0o600)
        fcntl.flock(fd, fcntl.LOCK_EX)
        try:
            stub = Stub()
            self.assertEqual(self.run_post(stub)[0], 3)
            self.assertEqual(stub.calls, [])
        finally:
            os.close(fd)

    def test_receipt_atomic_and_not_overwritten(self):
        self.rcpt.write_text("old")
        self.assertEqual(self.run_post(Stub())[0], 3)
        self.assertEqual(self.rcpt.read_text(), "old")
        self.assertEqual(self.run_post(Stub(), rcpt=self.d / "new.json")[0], 0)
        self.assertEqual([p.name for p in self.d.iterdir() if p.name.endswith(".tmp")], [])

    def test_issue_number_validation(self):
        for bad in ("0", "-1", "01", "7 ", "7/comments", "7/../../pulls/1", "７", "1e3", "", "7?x=1"):
            stub = Stub()
            self.assertEqual(self.run_post(stub, issue=bad)[0], 2, repr(bad))
            self.assertEqual(stub.calls, [])

    def test_only_issue_comment_commands(self):
        r = "repos/amaybaum/incompleteness/"
        bad = [["gh", "api", "-X", "PATCH", r + "issues/7", "-F", "body=@/s/submit.md"],
               ["gh", "api", "-X", "POST", r + "pulls/7/comments", "-F", "body=@/s/submit.md"],
               ["gh", "api", "-X", "POST", r + "issues/7", "-F", "body=@/s/submit.md"],
               ["gh", "api", "-X", "PATCH", r + "issues/comments/1", "-F", "body=@/s/submit.md"],
               ["gh", "api", "-X", "POST", r + "pulls/7/reviews", "-F", "body=@/s/submit.md"],
               ["gh", "api", "-X", "POST", "repos/other/repo/issues/7/comments", "-F", "body=@/s/submit.md"],
               ["gh", "api", "-X", "POST", r + "issues/7/comments", "-F", "title=x"],
               ["gh", "api", "-X", "POST", r + "issues/7/comments", "-f", "body=@/s/submit.md"],
               ["gh", "api", r + "issues/7", "-f", "body=x"], ["gh", "api", "graphql"],
               ["gh", "pr", "comment", "7"], ["gh", "issue", "edit", "7"], ["gh", "api", r + "pulls/7"],
               ["gh", "api", r + "issues/7/comments?per_page=100"],
               ["gh", "api", r + "issues/7/comments?since=2026-11-15T00:00:00Z&per_page=100&body=x"]]
        for argv in bad:
            with self.assertRaises(ValueError, msg=argv):
                W.gh(lambda a: self.fail("runner reached"), argv)


if __name__ == "__main__":
    unittest.main()
