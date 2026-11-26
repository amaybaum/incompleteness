#!/usr/bin/env python3
"""claims_check_test.py - controls on tools/claims_check.py that its own self-test cannot run.

  records    the exit-code, licence and review-record controls of the adopted design (DESIGN-r4
             section 3, 73 controls, ported from work/run_r4.py exitcodes), run on synthetic trees
             against a synthetic git repository built in a temporary directory, so that they need
             no network, no particular checkout and no history of this repository;
  sources    every item of tools/claims_check_controls.json against the control file it was copied
             from, batch W against its published SHA-256, and every pinned verdict against the
             reference prototype work/proto.r4.py of the design directory;
  previous   the withdrawn-claim patterns of the checker this one replaced, kept below verbatim as a
             fixture: every control text they flagged is flagged here, every match of them in this
             repository's Markdown that its marker lists did not excuse lies in a flagged sentence,
             and inserting its markers into a must-not-pass control never produces PASS (the
             design's M2 segmentation check);
  gate       tools/release_gate.py runs the checker with --repo and the main ref, and runs this file.

Usage:  python3 tools/claims_check_test.py [records|sources|previous|gate ...]
Exit 0 when every control holds, 1 otherwise.  Writes nothing outside a temporary directory.
"""
import hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHECKER = os.path.join(HERE, "claims_check.py")
DESIGN = os.path.join(ROOT, "verification", "audits", "infrastructure", "claims-check-redesign-20261125", "work")
W_SHA = "6317946b6fae4d58c2c78be5e718b06fd002c1edc6d37280f6821c9876d6b9a9"


def load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


CC = load("claims_check", CHECKER)
RESULTS = []


def check(section, name, ok, detail=""):
    RESULTS.append(ok)
    print(("ok   " if ok else "BAD  ") + section.ljust(10) + name + (("  | " + detail) if detail else ""))


# ------------------------------------------------------------------ records
def git(repo, *args):
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError("git %s: %s" % (" ".join(args), p.stderr.strip()))
    return p.stdout.strip()


ANCHOR = "a preferred-frame dispersive lattice theory satisfies it only under the H-Hawking conditions of §8.5"


def synthetic_repo(d):
    """A repository whose main and origin/main hold one commit with papers/GR.md (the licence anchor
    and review-record path), and whose branch 'research' holds a commit that is not on main."""
    repo = os.path.join(d, "repo")
    os.makedirs(os.path.join(repo, "papers"))
    env_git = ["-c", "user.name=test", "-c", "user.email=test.invalid", "-c", "commit.gpgsign=false"]
    git(d, "init", "-q", "-b", "main", repo)
    with open(os.path.join(repo, "papers", "GR.md"), "w", encoding="utf-8") as fh:
        fh.write("Synthetic anchor: " + ANCHOR + ".\n")
    git(repo, "add", "-A")
    git(repo, *env_git, "commit", "-q", "-m", "main")
    rev = git(repo, "rev-parse", "HEAD")
    git(repo, "update-ref", "refs/remotes/origin/main", rev)
    git(repo, "checkout", "-q", "-b", "research")
    with open(os.path.join(repo, "papers", "side.md"), "w", encoding="utf-8") as fh:
        fh.write("side\n")
    git(repo, "add", "-A")
    git(repo, *env_git, "commit", "-q", "-m", "research")
    branch_rev = git(repo, "rev-parse", "HEAD")
    git(repo, "checkout", "-q", "main")
    return repo, rev, branch_rev


def records():
    d0 = tempfile.mkdtemp()
    repo, REV, BRANCH_REV = synthetic_repo(d0)
    R = ("--repo", repo, "--main", "main")
    section = ["records"]

    def run(args):
        p = subprocess.run([sys.executable, "-I", CHECKER] + args, capture_output=True, text=True)
        return p.returncode, (p.stdout.strip().splitlines() or [""])[-1]

    def write(root, rel, text):
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(text)

    def case(name, files, expect, licences=None, reviews=None, extra=R):
        with tempfile.TemporaryDirectory() as d:
            t = os.path.join(d, "t")
            os.makedirs(t)
            for rel, text in files.items():
                write(t, rel, text)
            args = ["--root", t, "--json", os.path.join(d, "o.json")]
            write(d, "lic.json", json.dumps(licences if licences is not None else {"schema": "claims-licences/3", "entries": []}))
            args += ["--licences", os.path.join(d, "lic.json")]
            write(d, "rev.json", json.dumps({"records": []}) if reviews is None else
                  (reviews if isinstance(reviews, str) else json.dumps(reviews)))
            args += ["--reviews", os.path.join(d, "rev.json")]
            code, last = run(args + list(extra))
        check(section[0], "%s: expect %d, got %d" % (name, expect, code), code == expect, last[:100])

    FAILS = "The Hawking temperature $T_Q$ is state-independent.\n"
    neg = "The Hawking temperature $T_Q$ is not state-independent."
    hs = "Quantum mechanics requires observational incompleteness only if H-slope holds."
    hh = "Any QFT on this background is periodic in imaginary time only under the H-Hawking conditions."
    flip = "If H-balance fails, the Hawking temperature $T_Q$ is still state-independent."
    anap_prev, anap = "The calibration fixes $T_Q$ on the de Sitter horizon.", "It is state-independent."

    def rec(sent, rule, code, decision, **kw):
        r = {"rule": rule, "path": "papers/x.md", "sentence": sent, "sentence_sha256": CC.norm_hash(sent), "code": code,
             "decision": decision, "reason": "test", "reviewer": "test-reviewer", "revision": REV, "date": "2026-11-25",
             "authority": "test authority"}
        r.update(kw)
        return {"records": [r]}

    lic_ok = {"schema": "claims-licences/3", "entries": [{
        "id": "LIC-KMS-1", "rule": "W-GR-KMS", "qualifier": r"H-Hawking", "proposer": "proposer-a",
        "anchor": {"path": "papers/GR.md", "revision": REV, "quote": ANCHOR},
        "review": {"reviewer": "reviewer-b", "record": "papers/GR.md", "date": "2026-11-25", "revision": REV},
        "adoption": {"author": "owner", "time": "2026-11-25T00:00:00Z", "quote": "synthetic test entry"}}]}

    def lic_with(**kw):
        L = json.loads(json.dumps(lic_ok))
        e = L["entries"][0]
        for k, v in kw.items():
            if v is None:
                e.pop(k, None)
            elif isinstance(v, dict):
                e[k].update(v)
            else:
                e[k] = v
        return L

    # ---- the r3 controls (one expectation reversed by correction 2)
    case("clean active tree", {"papers/x.md": "Nothing here.\n"}, 0)
    case("bare FAIL in papers/", {"papers/x.md": FAILS}, 1)
    case("REVIEW only in papers/", {"papers/x.md": neg + "\n"}, 2)
    case("FAIL and REVIEW in papers/ (FAIL wins)", {"papers/x.md": FAILS + "\n" + neg + "\n"}, 1)
    case("FAIL in a verification record (reported, exit 0)", {"verification/a/b.md": FAILS}, 0)
    case("FAIL in verification/README.md (active)", {"verification/README.md": FAILS}, 1)
    case("FAIL in a README under verification/a/ (record)", {"verification/a/README.md": FAILS}, 0)
    case("FAIL in tools/README.md (active)", {"tools/README.md": FAILS}, 1)
    case("FAIL in AGENTS.md record section", {"AGENTS.md": "## §A.1 Rule\n\nText.\n\n## §A.37 Old lifecycle (record)\n\n" + FAILS}, 0)
    case("FAIL in AGENTS.md ordinary section", {"AGENTS.md": "## §A.37 Old (record)\n\nText.\n\n## §A.38 Rule\n\n" + FAILS}, 1)
    good = rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent")
    case("negated REVIEW resolved by a valid unrelated record", {"papers/x.md": neg + "\n"}, 0, reviews=good)
    case("valid record but no --repo", {"papers/x.md": neg + "\n"}, 3, reviews=good, extra=())
    case("record revision not on main", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent", revision="0" * 40))
    case("record revision abbreviated", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent", revision=REV[:12]))
    case("record missing reviewer", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent", reviewer=""))
    case("stale record (sentence edited)", {"papers/x.md": "The Hawking temperature $T_Q$ is not state-independent at all.\n"}, 3, reviews=good)
    case("record with a wrong code (code is matched exactly)", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "A", "unrelated", basis="negated", evidence="is not state-independent", window_sha256="x"))
    case("record cannot resolve a FAIL", {"papers/x.md": FAILS}, 3, reviews=rec(FAILS.strip(), "W-GR-TQ-STATE", "B", "unrelated", basis="other-subject", evidence="The"))
    case("unreadable review file", {"papers/x.md": "Nothing.\n"}, 3, reviews="{not json")
    case("governed on unlicensed H-slope (no licence cited)", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "governed", evidence="only if H-slope holds"))
    case("governed citing a licence id absent from the (empty) list", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "governed", licence="LIC-OI-1", evidence="only if H-slope holds"))
    case("unrelated resting on the qualifier itself", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="negated", evidence="only if H-slope holds"))
    case("unrelated 'other-subject' citing the rule's own subject", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="other-subject", evidence="Quantum mechanics"))
    case("'negated' basis on a polarity-flipped qualifier", {"papers/x.md": flip + "\n"}, 3, reviews=rec(flip, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="fails, the Hawking temperature $T_Q$ is still state-independent"))
    dn = "It is not false that the free-level cone is exact per channel."
    case("double negation cannot be recorded as negated", {"papers/x.md": dn + "\n"}, 3, reviews=rec(dn, "W-GR-CONE", "C", "unrelated", basis="negated", evidence="not false that the free-level cone is exact"))
    case("mention basis outside any quotation", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="mention", evidence="requires observational incompleteness"))
    qs = "Is the Hawking temperature $T_Q$ state-independent?"
    case("question record whose evidence lacks the cue (correction 2)", {"papers/x.md": qs + "\n"}, 3, reviews=rec(qs, "W-GR-TQ-STATE", "C", "unrelated", basis="question", evidence="Is the Hawking temperature"))
    case("anaphora REVIEW (code A) unresolved", {"papers/x.md": anap_prev + " " + anap + "\n"}, 2)
    win = CC.norm_hash("" + "\n\n" + anap_prev + " " + anap + "\n")
    case("anaphora record without window hash", {"papers/x.md": anap_prev + " " + anap + "\n"}, 3, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is"))
    case("anaphora record with its window hash", {"papers/x.md": anap_prev + " " + anap + "\n"}, 0, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is", window_sha256=win))
    case("anaphora record with a stale window hash", {"papers/x.md": "Context. " + anap_prev + " " + anap + "\n"}, 3, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is", window_sha256=win))
    case("governed with a valid licence entry (synthetic)", {"papers/x.md": hh + "\n"}, 0, licences=lic_ok, reviews=rec(hh, "W-GR-KMS", "C", "governed", licence="LIC-KMS-1", evidence="only under the H-Hawking conditions"))
    case("governed with a licence for another rule", {"papers/x.md": hs + "\n"}, 3, licences=lic_ok, reviews=rec(hs, "W-OI-REQ", "C", "governed", licence="LIC-KMS-1", evidence="only if H-slope holds"))
    case("licence without proposer", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(proposer=None))
    case("licence reviewed by its proposer", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(review={"reviewer": "proposer-a"}))
    case("licence without quoted owner adoption", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(adoption=None))
    case("licence review record path absent on main", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(review={"record": "verification/no/such/record.md"}))
    case("licence anchor quotation absent at its revision", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(anchor={"quote": "a sentence that is not in GR.md"}))
    case("licence entries but no --repo", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_ok, extra=())
    case("licence file with the r2 schema", {"papers/x.md": "Nothing.\n"}, 3, licences={"schema": "claims-licences/1", "fixture": True, "entries": []})
    code, _ = run(["--bogus"])
    check(section[0], "usage error: expect 4, got %d" % code, code == 4)

    # ---- the r3 review's record-loophole probes; each exits 3
    section[0] = "loophole"
    s1 = 'Under H-slope, the Hawking temperature $T_Q$ is state-independent in the "standard" sense.'
    case("mention: unrelated quoted word, H-slope sentence", {"papers/x.md": s1 + "\n"}, 3, reviews=rec(s1, "W-GR-TQ-STATE", "C", "unrelated", basis="mention", evidence="standard"))
    s2 = "The Hawking temperature $T_Q$ is state-independent, as one would expect from H-slope."
    case("supposition: incidental 'would', H-slope sentence", {"papers/x.md": s2 + "\n"}, 3, reviews=rec(s2, "W-GR-TQ-STATE", "C", "unrelated", basis="supposition", evidence="as one would expect"))
    s3 = "Why else would the Hawking temperature $T_Q$ be state-independent under H-slope?"
    case("question: rhetorical question under H-slope", {"papers/x.md": s3 + "\n"}, 3, reviews=rec(s3, "W-GR-TQ-STATE", "C", "unrelated", basis="question", evidence="Why else"))
    s5 = "Coupling-degree minimization, on this reading, singles out six components."
    case("other-subject: W-KDEG citing its own subject", {"papers/x.md": s5 + "\n"}, 3, reviews=rec(s5, "W-KDEG", "C", "unrelated", basis="other-subject", evidence="Coupling-degree minimization"))
    s6 = "Under H-Hawking, any QFT on this background is periodic in imaginary time."
    case("governed, empty list, licence=''", {"papers/x.md": s6 + "\n"}, 3, reviews=rec(s6, "W-GR-KMS", "C", "governed", licence="", evidence="Under H-Hawking"))
    case("governed, empty list, no licence key", {"papers/x.md": s6 + "\n"}, 3, reviews=rec(s6, "W-GR-KMS", "C", "governed", evidence="Under H-Hawking"))
    case("record for another path", {"papers/x.md": neg + "\n"}, 3, reviews={"records": [dict(good["records"][0], path="book/y.md")]})
    case("revision on the research branch, not on main", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent", revision=BRANCH_REV))
    case("--repo names a directory that does not exist", {"papers/x.md": neg + "\n"}, 3, reviews=good, extra=("--repo", os.path.join(d0, "no-such-repo"), "--main", "main"))

    # ---- correction 1: hypothesis token
    section[0] = "corr-1"
    hneg = "Under H-slope the Hawking temperature $T_Q$ is not state-independent."
    case("negated record on a sentence with an H-token (evidence clean)", {"papers/x.md": hneg + "\n"}, 3, reviews=rec(hneg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent"))
    hchi = "Quantum mechanics does not require observational incompleteness, which H-χ concerns."
    case("other-subject record on a sentence with a non-ASCII H-token (H-χ)", {"papers/x.md": hchi + "\n"}, 3, reviews=rec(hchi, "W-OI-REQ", "C", "unrelated", basis="other-subject", evidence="which"))
    hs0 = "Quantum mechanics requires observational incompleteness only if the bound holds."
    case("unmasked: unrelated resting on a qualifier (no H-token)", {"papers/x.md": hs0 + "\n"}, 3, reviews=rec(hs0, "W-OI-REQ", "C", "unrelated", basis="negated", evidence="only if the bound holds"))
    case("unmasked: other-subject citing the rule's own subject (no H-token)", {"papers/x.md": hs0 + "\n"}, 3, reviews=rec(hs0, "W-OI-REQ", "C", "unrelated", basis="other-subject", evidence="Quantum mechanics"))
    case("unmasked: mention outside any quotation (no H-token)", {"papers/x.md": hs0 + "\n"}, 3, reviews=rec(hs0, "W-OI-REQ", "C", "unrelated", basis="mention", evidence="requires observational incompleteness"))
    flip0 = "Even at the bound, the Hawking temperature $T_Q$ is not state-independent."
    case("unmasked: negated on a concessive sentence (no H-token)", {"papers/x.md": flip0 + "\n"}, 3, reviews=rec(flip0, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent"))
    case("governed record with a valid licence still resolves an H-token sentence", {"papers/x.md": hh + "\n"}, 0, licences=lic_ok, reviews=rec(hh, "W-GR-KMS", "C", "governed", licence="LIC-KMS-1", evidence="only under the H-Hawking conditions"))

    # ---- correction 2: the evidence carries the rule's own match
    section[0] = "corr-2"
    m1 = 'The Hawking temperature $T_Q$ is state-independent in the "standard" sense.'
    case("mention: quoted evidence lacks the rule's match (no H-token)", {"papers/x.md": m1 + "\n"}, 3, reviews=rec(m1, "W-GR-TQ-STATE", "C", "unrelated", basis="mention", evidence="standard"))
    m2 = 'The withdrawn draft wrote "the Hawking temperature $T_Q$ is state-independent", which this paper does not assert.'
    case("mention: quoted evidence carries the rule's match", {"papers/x.md": m2 + "\n"}, 0, reviews=rec(m2, "W-GR-TQ-STATE", "C", "unrelated", basis="mention", evidence="the Hawking temperature $T_Q$ is state-independent"))
    sp1 = "The Hawking temperature $T_Q$ is state-independent, as one would expect."
    case("supposition: evidence lacks the rule's match (no H-token)", {"papers/x.md": sp1 + "\n"}, 3, reviews=rec(sp1, "W-GR-TQ-STATE", "C", "unrelated", basis="supposition", evidence="as one would expect"))
    sp2 = "Suppose the Hawking temperature $T_Q$ were state-independent; the bound of §4 would then fail."
    case("supposition: clause carries the rule's match", {"papers/x.md": sp2 + "\n"}, 0, reviews=rec(sp2, "W-GR-TQ-STATE", "C", "unrelated", basis="supposition", evidence="Suppose the Hawking temperature $T_Q$ were state-independent"))
    q2 = "Why else would the Hawking temperature $T_Q$ be state-independent?"
    case("question: evidence lacks the rule's match (no H-token)", {"papers/x.md": q2 + "\n"}, 3, reviews=rec(q2, "W-GR-TQ-STATE", "C", "unrelated", basis="question", evidence="Why else"))
    case("question: evidence carries the rule's match", {"papers/x.md": qs + "\n"}, 0, reviews=rec(qs, "W-GR-TQ-STATE", "C", "unrelated", basis="question", evidence="Is the Hawking temperature $T_Q$ state-independent"))
    aq = "Is it state-independent?"
    winq = CC.norm_hash("" + "\n\n" + anap_prev + " " + aq + "\n")
    case("question, code A: evidence carries cue and anaphor", {"papers/x.md": anap_prev + " " + aq + "\n"}, 0, reviews=rec(aq, "W-GR-TQ-STATE", "A", "unrelated", basis="question", evidence="Is it state-independent", window_sha256=winq))
    case("question, code A: evidence lacks the anaphor", {"papers/x.md": anap_prev + " " + aq + "\n"}, 3, reviews=rec(aq, "W-GR-TQ-STATE", "A", "unrelated", basis="question", evidence="state-independent", window_sha256=winq))
    pp = 'The words "state-independent" and "draft" recur in the earlier note.'
    case("mention, code P: quoted evidence carries the strong cue", {"papers/x.md": pp + "\n"}, 0, reviews=rec(pp, "W-GR-TQ-STATE", "P", "unrelated", basis="mention", evidence="state-independent"))
    case("mention, code P: quoted evidence lacks the strong cue", {"papers/x.md": pp + "\n"}, 3, reviews=rec(pp, "W-GR-TQ-STATE", "P", "unrelated", basis="mention", evidence="draft"))

    # ---- correction 3: W-KDEG-ANSWER
    section[0] = "corr-3"
    ka = "Is the framework's answer $K = 2d$ here?"
    case("record citing rule W-KDEG for a W-KDEG-ANSWER finding is stale", {"papers/x.md": ka + "\n"}, 3, reviews=rec(ka, "W-KDEG", "C", "unrelated", basis="question", evidence="Is the framework's answer $K = 2d$ here"))
    case("record citing W-KDEG-ANSWER resolves it", {"papers/x.md": ka + "\n"}, 0, reviews=rec(ka, "W-KDEG-ANSWER", "C", "unrelated", basis="question", evidence="Is the framework's answer $K = 2d$ here"))
    case("other-subject citing the W-KDEG-ANSWER argument", {"papers/x.md": "The framework's answer, it seems, is $K = 2d$.\n"}, 3, reviews=rec("The framework's answer, it seems, is $K = 2d$.", "W-KDEG-ANSWER", "C", "unrelated", basis="other-subject", evidence="The framework's answer"))

    # ---- --main defaults to origin/main
    section[0] = "main-ref"
    case("valid record, --repo, no --main: revision on origin/main", {"papers/x.md": neg + "\n"}, 0, reviews=good, extra=("--repo", repo))
    case("record at a research-branch revision, --repo, no --main", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent", revision=BRANCH_REV), extra=("--repo", repo))

    # ---- documented residual (DESIGN-r4 section 5): correction 1 reads the sentence, not the window
    section[0] = "residual"
    hp = "Under H-slope, the calibration fixes $T_Q$ on the de Sitter horizon."
    winh = CC.norm_hash("" + "\n\n" + hp + " " + anap + "\n")
    case("code A: H-token only in the window; other-subject record accepted", {"papers/x.md": hp + " " + anap + "\n"}, 0, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is", window_sha256=winh))

    # ---- deployed files
    section[0] = "deployed"
    code, last = run(["--self-test"])
    check(section[0], "self-test with the deployed licence file: expect 0, got %d" % code, code == 0, last[:100])
    with tempfile.TemporaryDirectory() as d:
        with open(os.path.join(d, "lic.json"), "w", encoding="utf-8") as fh:
            json.dump(lic_ok, fh)
        code, last = run(["--self-test", "--licences", os.path.join(d, "lic.json")])
    check(section[0], "self-test with a non-empty licence list: expect 3, got %d" % code, code == 3, last[:100])
    code, last = run(["--root", d0, "--reviews", os.path.join(d0, "absent.json")])
    check(section[0], "missing review file: expect 3, got %d" % code, code == 3, last[:100])


# ------------------------------------------------------------------ sources
SOURCE_KEYS = ("id", "rule", "expect", "text", "context")


def sources():
    if not os.path.isdir(DESIGN):
        check("sources", "design directory present", False, "missing; the copies cannot be checked")
        return
    suite = json.load(open(os.path.join(HERE, "claims_check_controls.json"), encoding="utf-8"))["controls"]
    by_src = {}
    for c in suite:
        by_src.setdefault(c["source"], []).append(c)
    for src, items in sorted(by_src.items()):
        data = json.load(open(os.path.join(DESIGN, src), encoding="utf-8"))
        if src == "design-example-sentences.json":
            orig = [{"id": e["id"], "rule": e["rule"], "expect": "FAIL", "text": e["text"]} for e in data["examples"]]
        else:
            orig = data
        a = [{k: c[k] for k in SOURCE_KEYS if k in c} for c in items]
        b = [{k: c[k] for k in SOURCE_KEYS if k in c} for c in orig]
        check("sources", "%s: %d items copied verbatim" % (src, len(b)), a == b)
    h = hashlib.sha256(open(os.path.join(DESIGN, "reviewer-heldout-W.json"), "rb").read()).hexdigest()
    check("sources", "batch W SHA-256 is the published one", h == W_SHA, h[:16])
    proto = load("proto_r4", os.path.join(DESIGN, "proto.r4.py"))
    order = {"FAIL": 2, "REVIEW": 1, "PASS": 0}
    diff = []
    for c in suite:
        v, fs = proto.verdict_for(c["text"], c["rule"], c.get("context", ""))
        a = max([x["verdict"] for x in proto.check_paragraph(c["text"], c.get("context", ""))], key=order.get, default="PASS")
        if c["pinned"] != {"verdict": v, "codes": ",".join(x["code"] for x in fs), "any": a}:
            diff.append(c["id"])
    check("sources", "every pinned verdict is the prototype's (%d items)" % len(suite), not diff, " ".join(diff[:10]))
    rules = lambda m: [(r["id"], r.get("family"), r.get("args"), r.get("cues"), r.get("strong"), r.get("literal"))
                       for r in m.RULES]
    same = [(x == y) or (x[0] == "W-OI-NOEXIST" and x[:4] == y[:4] and x[5:] == y[5:]) for x, y in zip(rules(CC), rules(proto))]
    check("sources", "rule data equal the prototype's (W-OI-NOEXIST strong cue rewritten equivalently)",
          len(CC.RULES) == len(proto.RULES) and all(same) and CC.BARE == proto.BARE)
    probe = ["Quantum mechanics cannot exist without it.", "QM could not exist without OI.",
             "Quantum theory would not exist without that.", "It cannot  exist without it.", "cannot exist withoutx"]
    s_cc = [r for r in CC.RULES if r["id"] == "W-OI-NOEXIST"][0]["strong"]
    s_pr = [r for r in proto.RULES if r["id"] == "W-OI-NOEXIST"][0]["strong"]
    check("sources", "W-OI-NOEXIST strong cue agrees with the prototype's on its probes",
          all(bool(re.search(s_cc, p, re.I)) == bool(re.search(s_pr, p, re.I)) for p in probe))


# ------------------------------------------------------------------ previous
# Fixture: the patterns and marker lists of tools/claims_check.py before this design was implemented
# (blob at commit 5ebba1a27f2ce5d02cadb75ee5fb3393e6f88e80), verbatim.  They are not used to decide
# anything in the gate; they test that no claim the previous checker caught passes silently here.
PREV_MARKERS = ('H-link', 'H-spin', 'H-balance', 'H-Hawking', 'H-spectrum', 'H-cust', 'H-blind',
                'H-frame', 'H-scramble', 'H-shell', 'H-slope', 'kinematic in its parameter', 'conditional', 'CONDITIONAL', 'not establish',
                'does not answer', 'does not close', 'premise', 'withdrawn',
                'is not a proof', 'No framework derives', 'no framework derives',
                'definition*', 'assumption', 'does not', 'cannot', 'not a proof',
                'link count', 'rather than facts')
PREV_CLAIMS = [
    re.compile(r'coupling-degree minimi\w*'),
    re.compile(r"framework's answer is \$K = 2d"),
    re.compile(r'forcing an Euclidean|forces an Euclidean'),
    re.compile(r'leading scalar propagation geometry is Euclidean'),
    re.compile(r'state-independent'),
    re.compile(r'purely kinematic'),
    re.compile(r'must therefore be periodic|must be KMS|any QFT on this background'),
    re.compile(r'any QFT on a bifurcate|exact free-level cone per channel'),
    re.compile(r'free-level cone is exact'),
    re.compile(r'(\\v?arepsilon|\\epsilon)\s*\\kappa\s*/\s*c\b(?!\^)'),
]
PREV_OI_MARKERS = ('core-containment', 'core containment', 'containment', 'qm_implies_oiCore',
                   'completedOI_iff_physical', 'forward redundancy', 'forward-redundancy',
                   'redundant', 'does no work', 'not explanatory', 'not an explanatory',
                   'in the narrow', 'unsupported', 'is not proved', 'not a theorem')
PREV_OI_CLAIMS = [
    re.compile(r'(?i)\b(QM|quantum mechanics) (requires|needs|presupposes) '
               r'(bare )?(OI\b|observation(al)? incompleteness)'),
    re.compile(r'(?i)\b(QM|quantum mechanics) cannot exist without'),
    re.compile(r'(?i)\b(QM|quantum mechanics) (requires|needs) hidden '
               r'(information|variables?|states?|ontology)'),
    re.compile(r'(?i)\b(OI|observation(al)? incompleteness|ignorance) '
               r'(causes|produces|explains|generates|gives rise to) '
               r'(QM|quantum|quantum mechanics)'),
    re.compile(r'(?i)\bwithout (OI|observation(al)? incompleteness) there (is|would be) no '
               r'(QM|quantum)'),
]
PREV = [(rx, PREV_MARKERS) for rx in PREV_CLAIMS] + [(rx, PREV_OI_MARKERS) for rx in PREV_OI_CLAIMS]


def prev_hits(par):
    """The previous checker's verdict on one paragraph: the matches it reported."""
    return [m for rx, marks in PREV for m in rx.finditer(par) if not any(k in par for k in marks)]


def previous():
    suite = json.load(open(os.path.join(HERE, "claims_check_controls.json"), encoding="utf-8"))["controls"]
    flagged = [c for c in suite if prev_hits(c["text"])]
    lost = [c["id"] for c in flagged if CC.any_verdict(c["text"], c.get("context", "")) == "PASS"]
    # EX-2 is the one exception, and it is not an assertion: it lists the forms of the subject
    # "coupling-degree minimization" with no selection cue (K, 2d, six, fixes, ...), which the previous
    # checker flagged as a bare mention.  Any other loss fails.
    check("previous", "every control the previous checker flagged is flagged, except the mention EX-2 (%d of %d)"
          % (len(flagged), len(suite)), lost == ["EX-2"], " ".join(lost[:10]))
    n, lost = 0, []
    for dp, dn, fs in os.walk(ROOT):
        dn[:] = sorted(x for x in dn if x != ".git")
        for fn in sorted(fs):
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dp, fn)
            text = open(p, encoding="utf-8", errors="replace").read()
            prev = ""
            for par in text.split("\n\n"):
                ms = prev_hits(par)
                if ms:
                    found = CC.check_paragraph(par, prev)
                    starts = [a for a, _ in CC.sentences(par)]
                    for m in ms:
                        n += 1
                        unit = max(a for a in starts if a <= m.start()) if any(a <= m.start() for a in starts) else None
                        if not any(x["offset"] == unit for x in found):
                            lost.append("%s: %s" % (os.path.relpath(p, ROOT), m.group(0)))
                prev = par
    check("previous", "every unexcused match of the previous patterns in this tree lies in a flagged sentence (%d)" % n,
          not lost, "; ".join(lost[:5]))
    ins, passed = 0, []
    for c in suite:
        if c["category"] != "acceptance" or c["expect"] != "FAIL":
            continue
        t = c["text"].rstrip()
        for m in PREV_MARKERS + PREV_OI_MARKERS:
            for txt in (t + " The text notes " + m + ".", (t[:-1] if t.endswith(".") else t) + ", and the text notes " + m + ".",
                        m[:1].upper() + m[1:] + ": " + t, "Under " + m + ", " + t[:1].lower() + t[1:]):
                ins += 1
                if CC.verdict_for(txt, c["rule"], c.get("context", ""))[0] == "PASS":
                    passed.append(c["id"])
    check("previous", "marker insertion into must-not-pass controls never passes (%d insertions)" % ins,
          not passed, " ".join(sorted(set(passed))[:10]))


# ------------------------------------------------------------------ gate
def gate():
    g = open(os.path.join(HERE, "release_gate.py"), encoding="utf-8").read()
    m = re.search(r'\("claims",\s*\[([^\]]*)\]\)', g)
    argv = m.group(1) if m else ""
    check("gate", "the claims step runs tools/claims_check.py with --repo and --main origin/main",
          "tools/claims_check.py" in argv and '"--repo"' in argv and '"--main", "origin/main"' in argv, argv.strip()[:100])
    check("gate", "the gate runs this file", '"tools/claims_check_test.py"' in g)


def main(argv):
    parts = {"records": records, "sources": sources, "previous": previous, "gate": gate}
    want = argv[1:] or list(parts)
    bad = [w for w in want if w not in parts]
    if bad:
        print(__doc__)
        return 1
    for w in want:
        parts[w]()
    n_bad = RESULTS.count(False)
    print("claims_check_test: %s (%d controls, %d failed)" % ("OK" if not n_bad else "FAILED", len(RESULTS), n_bad))
    return 1 if n_bad else 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except SystemExit:
        raise
    except Exception as e:                     # noqa: BLE001 -- a crash is a failed control, never a pass
        print("claims_check_test: internal error:", repr(e))
        sys.exit(1)
