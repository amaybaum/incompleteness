#!/usr/bin/env python3
"""claims_check_r4_test.py - controls on tools/claims_check_r4.py that its own self-test cannot run.

  records    the exit-code, licence and review-record controls of the adopted design (DESIGN-r4
             section 3, 73 controls, ported from work/run_r4.py exitcodes), run on synthetic trees
             against a synthetic git repository built in a temporary directory, so that they need
             no network, no particular checkout and no history of this repository;
  sources    every item of tools/claims_check_r4_controls.json copied from a file of the design
             directory against that file, batch W against its published SHA-256, and every pinned
             verdict against the reference prototype work/proto.r4.py;
  previous   comparison with the blocking checker, tools/claims_check.py, on three specific sets:
             the controls (those it flags and this checker passes must be exactly the pinned
             losses); a finite set of sentences generated from the alternatives of each of its
             patterns (the old-only ones and the per-pattern counts must equal the pinned file
             tools/claims_check_r4_gap.json; they are known, unresolved coverage gaps); and the
             current corpus (n reported, not coverage evidence).  Plus marker insertion into the
             must-not-pass acceptance controls (the design's M2 segmentation check).  None of these
             finite sets proves that coverage of the old patterns is preserved;
  gate       tools/release_gate.py keeps the blocking claims step unchanged, runs this checker
             report-only, and runs this file.

Usage:  python3 tools/claims_check_r4_test.py [records|sources|previous|gate ...]
        python3 tools/claims_check_r4_test.py report [--json OUT]   the report-only gate step
        python3 tools/claims_check_r4_test.py write-gap-pin         regenerate the pinned gap file
Exit 0 when every control holds, 1 otherwise.  report: 0 whatever it finds, 1 when
tools/claims_check_r4.py fails (self-test, record, usage or internal error) or the report crashes;
its output and OUT have three sections: findings in the current corpus, generated test cases
covering the old checker's patterns, and known coverage gaps, unresolved.  Writes nothing outside a
temporary directory, except OUT and write-gap-pin's file.
"""
import hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CHECKER = os.path.join(HERE, "claims_check_r4.py")
DESIGN = os.path.join(ROOT, "verification", "audits", "infrastructure", "claims-check-redesign-20261125", "work")
W_SHA = "6317946b6fae4d58c2c78be5e718b06fd002c1edc6d37280f6821c9876d6b9a9"


def load(name, path):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


CC = load("claims_check_r4", CHECKER)
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
    suite = json.load(open(os.path.join(HERE, "claims_check_r4_controls.json"), encoding="utf-8"))["controls"]
    by_src = {}
    for c in suite:
        by_src.setdefault(c["source"], []).append(c)
    for src, items in sorted(by_src.items()):
        if not os.path.exists(os.path.join(DESIGN, src)):
            continue                                   # items not copied from a design file
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
# The blocking checker, tools/claims_check.py, read as it is: its patterns and marker lists decide
# here only what it flags, to compare with this checker.
OLD = load("claims_check_previous", os.path.join(HERE, "claims_check.py"))
PREV = ([(rx, why, OLD.MARKERS) for rx, why in OLD.CLAIMS]
        + [(rx, why, OLD.OI_MARKERS) for rx, why in OLD.OI_CLAIMS])


def prev_matches(par):
    """The blocking checker's findings on one paragraph: (match, reason) for each rule it reports."""
    out = []
    for rx, why, marks in PREV:
        m = rx.search(par)
        if m and not any(k in par for k in marks):
            out.append((m, why))
    return out


def prev_hits(par):
    return [m for m, _ in prev_matches(par)]


# ---- generated forms: what the blocking checker's patterns can match
# Each pattern of tools/claims_check.py is expanded from its own alternatives (subjects, verbs,
# objects, case) into sentence frames that state the withdrawn result; the frames carry no marker
# of the blocking checker, so it flags each sentence that contains a match.  The list is fixed in
# this file, not chosen from the outcome, and every sentence it yields is compared.
def _cap(s):
    return s[:1].upper() + s[1:]


def generated_forms():
    forms = []

    def add(label, sents):
        for s in sents:
            forms.append((label, s))
    kdeg = ["coupling-degree minimization", "coupling-degree minimisation", "coupling-degree minimizing",
            "coupling-degree minimum"]
    kfr = ["{} fixes the component count.", "{} fixes $K = 2d$.", "{} selects six components per site.",
           "The component count follows from {}.", "{} determines the internal structure of a site.",
           "{} gives the single-copy clause.", "The lattice is chosen by {}.", "{} is why each site carries six links."]
    add("coupling-degree minimi", [(f.format(_cap(k)) if f.startswith("{}") else f.format(k)) for k in kdeg for f in kfr]
        + ["In this framework, " + f.format(k) for k in kdeg for f in kfr if f.startswith("{}")])
    add("framework's answer is $K = 2d", ["The framework's answer is $K = 2d$.", "The framework's answer is $K = 2d$ components per site.",
                                          "In three dimensions the framework's answer is $K = 2d$, six."])
    eu_s = ["cubic equivariance", "cubic symmetry", "the lattice symmetry", "finite observation", "equivariant projection",
            "the substratum", "projected memory", "the observer interface"]
    eu_o = ["quadratic symbol", "metric", "propagation geometry", "observer symbol", "dispersion relation"]
    add("forces an Euclidean", ["%s forces an Euclidean %s." % (_cap(s), o) for s in eu_s for o in eu_o])
    add("forcing an Euclidean", ["The lattice is cubic, forcing an Euclidean %s." % o for o in eu_o]
        + ["%s acts on the projection, forcing an Euclidean %s." % (_cap(s), o) for s in eu_s[:4] for o in eu_o[:2]])
    add("leading scalar propagation geometry is Euclidean",
        ["The leading scalar propagation geometry is Euclidean.", "At long wavelength the leading scalar propagation geometry is Euclidean.",
         "On the lattice the leading scalar propagation geometry is Euclidean in every direction."])
    ts = ["$T_Q$", "the Hawking temperature", "the horizon temperature", "the de Sitter temperature", "the temperature",
          "the vacuum energy", "the thermal ratio", "the Unruh temperature", "the calibration", "the entropy"]
    add("state-independent", ["%s is state-independent." % _cap(s) for s in ts]
        + ["The state-independent %s fixes the scale." % s.replace("the ", "") for s in ts[1:5]])
    ks = ["horizon thermality", "the Hawking temperature", "the thermal spectrum", "the Unruh effect", "the thermality of the horizon",
          "$T_Q$"]
    add("purely kinematic", ["%s is purely kinematic." % _cap(s) for s in ks]
        + ["The effect is purely kinematic in origin.", "Its origin is purely kinematic."])
    pf = ["the field", "the state", "every correlator", "the two-point function", "each mode", "the restricted state"]
    add("must therefore be periodic", ["%s must therefore be periodic in imaginary time." % _cap(s) for s in pf]
        + ["%s must therefore be periodic with period $2\\pi/\\kappa$." % _cap(s) for s in pf]
        + ["So %s must therefore be periodic with period 2π/κ." % s for s in pf])
    add("must be KMS", ["%s must be KMS." % _cap(s) for s in pf] + ["%s must be KMS at the horizon temperature." % _cap(s) for s in pf])
    qb = ["is thermal", "is in equilibrium", "has a thermal spectrum", "is KMS", "is periodic in imaginary time",
          "radiates at $T_Q$"]
    add("any QFT on this background", ["Any QFT on this background %s." % p for p in qb]
        + ["In this model, any QFT on this background %s." % p for p in qb])
    add("any QFT on a bifurcate", ["Any QFT on a bifurcate Killing horizon %s." % p for p in qb]
        + ["In this model, any QFT on a bifurcate Killing horizon %s." % p for p in qb])
    add("exact free-level cone per channel", ["The exact free-level cone per channel bounds every signal.",
                                              "Each mode obeys an exact free-level cone per channel.",
                                              "There is an exact free-level cone per channel."])
    add("free-level cone is exact", ["The free-level cone is exact.", "The free-level cone is exact per channel.",
                                     "On the normalized branch the free-level cone is exact.",
                                     "In $d = 3$ the free-level cone is exact for every mode."])
    add("epsilon kappa over c", ["The shift is $\\varepsilon\\kappa/c$.", "The shift is $\\epsilon \\kappa / c$.",
                                 "It equals $2\\varepsilon\\kappa/c$ at leading order."])
    qm = ["QM", "quantum mechanics", "Quantum mechanics"]
    oi = ["OI", "observational incompleteness", "observation incompleteness", "bare OI", "bare observational incompleteness"]
    add("QM requires OI", ["%s %s %s." % (q, v, o) for q in qm for v in ("requires", "needs", "presupposes") for o in oi]
        + ["In this framework, %s requires %s." % (q.lower() if q != "QM" else q, o) for q in qm[:2] for o in oi[:3]])
    add("QM cannot exist without", ["%s cannot exist without %s." % (q, o) for q in qm
                                    for o in ("OI", "observational incompleteness", "hidden information", "ignorance",
                                              "an observer", "a substratum", "the trace-out")])
    add("QM requires hidden", ["%s %s hidden %s." % (q, v, o) for q in qm for v in ("requires", "needs")
                               for o in ("information", "variables", "variable", "states", "state", "ontology")])
    oi_s = ["OI", "observational incompleteness", "observation incompleteness", "ignorance", "Observational incompleteness",
            "Ignorance"]
    oi_v = ["causes", "produces", "explains", "generates", "gives rise to"]
    oi_o = ["QM", "quantum mechanics", "quantum interference", "quantum randomness", "quantum entanglement",
            "quantum probabilities", "quantum indeterminacy", "quantum behaviour", "quantum statistics", "quantum theory",
            "quantum structure", "quantum phenomena", "quantum superposition", "quantum uncertainty"]
    add("OI explains quantum", ["%s %s %s." % (_cap(s), v, o) for s in oi_s for v in oi_v for o in oi_o])
    add("without OI there is no quantum", ["%s %s there %s no %s." % (w, o, b, q)
                                           for w in ("Without", "without")[:1]
                                           for o in ("OI", "observational incompleteness", "observation incompleteness")
                                           for b in ("is", "would be")
                                           for q in ("QM", "quantum mechanics", "quantum behaviour", "quantum interference",
                                                     "quantum theory")])
    return forms


def gap():
    """Over the generated forms: per pattern label, the number generated, flagged by the blocking
    checker, flagged by both checkers, and flagged by the blocking checker only (old-only); and the
    old-only sentences themselves."""
    rows, tot = [], {}
    for label, s in generated_forms():
        pm = prev_matches(s)
        t = tot.setdefault(label, {"generated": 0, "old_flags": 0, "caught_by_both": 0, "old_only": 0})
        t["generated"] += 1
        if not pm:
            continue
        t["old_flags"] += 1
        if CC.any_verdict(s) == "PASS":
            t["old_only"] += 1
            rows.append({"pattern": label, "old_rule": pm[0][1], "sentence": s})
        else:
            t["caught_by_both"] += 1
    return rows, tot


def tree_comparison():
    """Every match of the blocking checker's patterns, in a paragraph its marker lists do not excuse,
    in this repository's Markdown, and those of them that lie in a sentence this checker passes."""
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
                            lost.append({"path": os.path.relpath(p, ROOT).replace(os.sep, "/"), "match": m.group(0)})
                prev = par
    return n, lost


def control_losses(suite):
    """Controls the blocking checker flags and this checker passes (over every rule)."""
    flagged = [c for c in suite if prev_hits(c["text"])]
    return flagged, sorted(c["id"] for c in flagged if CC.any_verdict(c["text"], c.get("context", "")) == "PASS")


def coverage(suite):
    rows, tot = gap()
    n, lost = tree_comparison()
    flagged, losses = control_losses(suite)
    return {
        "generated_test_cases": {
            "about": ("Sentences generated from the alternatives of each pattern of tools/claims_check.py "
                      "(generated_forms in tools/claims_check_r4_test.py). A finite set: it shows which of these "
                      "sentences each checker flags, not that every sentence the old patterns match is covered."),
            "generated": sum(t["generated"] for t in tot.values()),
            "old_flags": sum(t["old_flags"] for t in tot.values()),
            "caught_by_both": sum(t["caught_by_both"] for t in tot.values()),
            "old_only": sum(t["old_only"] for t in tot.values()),
            "by_pattern": tot},
        "known_coverage_gaps": {
            "about": ("Sentences and controls that tools/claims_check.py flags and tools/claims_check_r4.py passes. "
                      "Unresolved; no switch to the new checker as the blocking check while they remain."),
            "generated_old_only": rows,
            "controls_old_only": losses,
            "corpus_old_only": lost},
        "corpus_comparison": {"old_unexcused_matches": n, "of_which_new_passes": len(lost),
                              "controls_old_flags": len(flagged), "controls": len(suite)},
    }


GAP_PIN = os.path.join(HERE, "claims_check_r4_gap.json")
SUITE = os.path.join(HERE, "claims_check_r4_controls.json")


def report(out):
    """The report-only gate step: the r4 scan of the current corpus (its own failures fail the step),
    then the comparison with the blocking checker, in three sections."""
    with tempfile.TemporaryDirectory() as d:
        j = os.path.join(d, "findings.json")
        p = subprocess.run([sys.executable, "-I", CHECKER, "--report-only", "--repo", ROOT, "--main", "origin/main",
                            "--json", j], capture_output=True, text=True, cwd=ROOT)
        print(p.stdout.rstrip())
        if p.returncode != 0:
            print("claims_check_r4_test report: FAILED (tools/claims_check_r4.py exit %d)" % p.returncode)
            return 1
        scan = json.load(open(j, encoding="utf-8"))
    suite = json.load(open(SUITE, encoding="utf-8"))["controls"]
    cov = coverage(suite)
    act = [x for x in scan["findings"] if x["active"] and "resolved_by" not in x]
    doc = {
        "schema": "claims-r4-report/1",
        "findings_in_current_corpus": {
            "about": ("tools/claims_check_r4.py on this tree, report-only. findings: one per (rule, sentence unit); "
                      "sentences: distinct (path, sentence hash); texts: distinct sentence hashes; records needed: "
                      "distinct (rule, path, sentence hash, code, window hash for code A)."),
            "workload": scan["workload"], "counts": scan["counts"], "record_problems": scan["record_problems"],
            "active_findings": [{k: x[k] for k in ("path", "line", "rule", "code", "verdict", "sentence_sha256",
                                                    "window_sha256", "sentence")} for x in act],
            "comparison_with_blocking_checker": cov["corpus_comparison"]},
        "generated_test_cases": cov["generated_test_cases"],
        "known_coverage_gaps": cov["known_coverage_gaps"],
    }
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, indent=1, ensure_ascii=False)
            fh.write("\n")
    w, cc, g, k = scan["workload"], cov["corpus_comparison"], cov["generated_test_cases"], cov["known_coverage_gaps"]
    print("== 1. findings in the current corpus (report-only; not gating)")
    print("   " + ", ".join("%s %d" % kv for kv in w.items()))
    print("   blocking-checker patterns: %d unexcused match(es) in this tree, %d in a sentence the new checker passes"
          % (cc["old_unexcused_matches"], cc["of_which_new_passes"]))
    print("== 2. generated test cases covering the old checker's patterns (a finite set, not a proof of coverage)")
    print("   %d generated, %d flagged by the old checker, %d by both, %d by the old checker only"
          % (g["generated"], g["old_flags"], g["caught_by_both"], g["old_only"]))
    for label, t in g["by_pattern"].items():
        print("   %-48s generated %3d  old %3d  both %3d  old-only %3d"
              % (label, t["generated"], t["old_flags"], t["caught_by_both"], t["old_only"]))
    print("== 3. known coverage gaps, unresolved")
    print("   controls flagged by the old checker only: %s" % (" ".join(k["controls_old_only"]) or "none"))
    for r in k["corpus_old_only"]:
        print("   CORPUS %s: %s" % (r["path"], r["match"]))
    for r in k["generated_old_only"]:
        print("   GAP [%s] %s" % (r["pattern"], r["sentence"]))
    print("claims_check_r4_test report: OK (report-only; %d active findings, %d records needed; %d known gap(s) in "
          "generated cases, %d in controls)%s" % (w["findings"], w["records needed"], len(k["generated_old_only"]),
                                                   len(k["controls_old_only"]), ("; report " + out) if out else ""))
    return 0


def previous():
    suite = json.load(open(SUITE, encoding="utf-8"))["controls"]
    known = {c["id"] for c in suite if c.get("category") == "previous-gap"} | {"EX-2"}
    flagged, lost = control_losses(suite)
    # The known losses are pinned: EX-2 (a listing of forms of "coupling-degree minimization" with no
    # selection cue) and the previous-gap controls (the independent review's examples).  Any other
    # control the blocking checker flags and this one passes fails the test.
    check("previous", "controls flagged by the old checker and passed by the new are exactly the pinned losses "
          "(%d of %d controls flagged by the old)" % (len(flagged), len(suite)), lost == sorted(known), " ".join(lost[:12]))
    for c in suite:
        if c.get("category") == "previous-gap":
            check("previous", "%s: the old checker's verdict is as pinned" % c["id"], bool(prev_hits(c["text"])) == c["old_flags"])
    # Generated test cases: the old-only list and the per-pattern counts must equal the pinned file, so
    # that a change in either direction is visible.  This records the gaps; it does not resolve them.
    rows, tot = gap()
    try:
        pin = json.load(open(GAP_PIN, encoding="utf-8"))
    except (OSError, ValueError) as e:
        check("previous", "pinned gap file readable", False, str(e))
        pin = {}
    check("previous", "generated test cases: old-only list and per-pattern counts equal the pinned file "
          "(%d generated, %d old-only)" % (sum(t["generated"] for t in tot.values()), len(rows)),
          pin.get("generated_old_only") == rows and pin.get("by_pattern") == tot)
    # Current corpus: n is reported, and is not coverage evidence (the old checker passes this tree).
    n, lost = tree_comparison()
    check("previous", "current corpus: old-pattern matches in sentences the new checker passes: %d of n = %d (n is not coverage)"
          % (len(lost), n), not lost, "; ".join("%s: %s" % (r["path"], r["match"]) for r in lost[:5]))
    ins, passed = 0, []
    for c in suite:
        if c["category"] != "acceptance" or c["expect"] != "FAIL":
            continue
        t = c["text"].rstrip()
        for m in OLD.MARKERS + OLD.OI_MARKERS:
            for txt in (t + " The text notes " + m + ".", (t[:-1] if t.endswith(".") else t) + ", and the text notes " + m + ".",
                        m[:1].upper() + m[1:] + ": " + t, "Under " + m + ", " + t[:1].lower() + t[1:]):
                ins += 1
                if CC.verdict_for(txt, c["rule"], c.get("context", ""))[0] == "PASS":
                    passed.append(c["id"])
    check("previous", "marker insertion into the must-not-pass acceptance controls never passes (%d insertions)" % ins,
          not passed, " ".join(sorted(set(passed))[:10]))


def write_gap_pin():
    """Regenerates the pinned file from the current outcome (used when a deliberate change moves it)."""
    rows, tot = gap()
    with open(GAP_PIN, "w", encoding="utf-8") as fh:
        json.dump({"schema": "claims-r4-previous-gap/1",
                   "about": ("Generated test cases from the patterns of tools/claims_check.py that it flags and "
                             "tools/claims_check_r4.py passes, and the per-pattern counts. Known, unresolved coverage "
                             "gaps of a finite generated set; tools/claims_check_r4_test.py previous fails when the "
                             "outcome differs from this file."),
                   "by_pattern": tot, "generated_old_only": rows}, fh, indent=1, ensure_ascii=False)
        fh.write("\n")


# ------------------------------------------------------------------ gate
def gate():
    g = open(os.path.join(HERE, "release_gate.py"), encoding="utf-8").read()
    m = re.search(r'\("claims",\s*\[([^\]]*)\]\)', g)
    check("gate", "the blocking claims step runs tools/claims_check.py unchanged",
          bool(m) and m.group(1).strip() == 'sys.executable, "tools/claims_check.py"', m.group(1).strip()[:100] if m else "")
    m = re.search(r'\("claims-r4-report",\s*\[([^\]]*)\]', g)
    argv = m.group(1) if m else ""
    check("gate", "the report-only step runs this file's report", '"tools/claims_check_r4_test.py", "report"' in argv,
          argv.strip()[:120])
    src = open(os.path.abspath(__file__), encoding="utf-8").read()
    check("gate", "the report runs tools/claims_check_r4.py with --report-only, --repo and --main origin/main",
          '[sys.executable, "-I", CHECKER, "--report-only", "--repo", ROOT, "--main", "origin/main"' in src)
    m = re.search(r'\("claims-controls",\s*\[([^\]]*)\]\)', g)
    check("gate", "the blocking claims-controls step runs this file's controls",
          bool(m) and m.group(1).strip() == 'sys.executable, "tools/claims_check_r4_test.py"')


def main(argv):
    if argv[1:2] == ["report"]:
        return report(argv[argv.index("--json") + 1] if "--json" in argv else None)
    if argv[1:2] == ["write-gap-pin"]:
        write_gap_pin()
        return 0
    parts = {"records": records, "sources": sources, "previous": previous, "gate": gate}
    want = argv[1:] or list(parts)
    bad = [w for w in want if w not in parts]
    if bad:
        print(__doc__)
        return 1
    for w in want:
        parts[w]()
    n_bad = RESULTS.count(False)
    print("claims_check_r4_test: %s (%d controls, %d failed)" % ("OK" if not n_bad else "FAILED", len(RESULTS), n_bad))
    return 1 if n_bad else 0


if __name__ == "__main__":
    try:
        sys.exit(main(sys.argv))
    except SystemExit:
        raise
    except Exception as e:                     # noqa: BLE001 -- a crash is a failed control, never a pass
        print("claims_check_r4_test: internal error:", repr(e))
        sys.exit(1)
