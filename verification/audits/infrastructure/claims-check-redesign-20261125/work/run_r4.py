#!/usr/bin/env python3
"""Measurement harness for DESIGN-r4 (paper-only). Usage, from this directory:
  run_r4.py compare                       r3 vs r4 on every control file, batch W, the earlier probes and the
                                          author diagnostics: per-rule verdicts and, for W and D, any rule firing
  run_r4.py exitcodes REPO MAINREF        exit-code, licence and review-record controls on synthetic trees, run
                                          under r3 and r4; expectations are r4's.  Includes the r3 review's
                                          record-loophole probes, each of which must exit 3 under r4
  run_r4.py inject TREEM [r3]             corpus injection of every positive and ambiguous control and probe
  run_r4.py m2 CURRENT_CHECKER            marker insertion into every positive control (segmentation check only)
  run_r4.py scan TREEM OUTDIR             scan tree M with r3 and r4; per-rule and per-code review load
Writes nothing outside a temporary directory, except scan's OUTDIR."""
import sys, os, json, subprocess, tempfile, importlib.util, hashlib
from multiprocessing import Pool
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m

P4 = load("p4", os.path.join(HERE, "proto.r4.py"))
P3 = load("p3", os.path.join(HERE, "proto.r3.py"))
REV = "e2e2a623265187a28ebec604ab8bcc672742888f"
BRANCH_REV = "29b21374f33a08d6ec131b43d9cfbbc5bcadf684"   # research branch commit, not on main
W_SHA = "6317946b6fae4d58c2c78be5e718b06fd002c1edc6d37280f6821c9876d6b9a9"

CONTROL_FILES = [("batch 1 (63)", "controls.json"), ("batch H (20)", "heldout.json"), ("batch C (5)", "controls_c.json"),
                 ("batch D (4)", "controls_d.json"), ("batch X (34)", "reviewer-heldout.json"),
                 ("batch R2 (26)", "controls_r2.json"), ("batch Y (43)", "reviewer-heldout-Y.json")]
PROBES = [("probe (13)", "reviewer-probes/probe.json"), ("probe2 (9)", "reviewer-probes/probe2.json"),
          ("probe3 (2)", "reviewer-probes/probe3.json"), ("probe4 (6)", "reviewer-probes/probe4.json"),
          ("Z post-hoc (10)", "reviewer-probes-Y/posthoc-probes.json"), ("M1 diag (8)", "reviewer-probes-Y/m1-diag.json")]
WBATCH = [("batch W (38)", "reviewer-heldout-W.json")]
DIAG = [("author diagnostics D (12)", "r3-author-diagnostics.json")]
O = {"FAIL": 2, "REVIEW": 1, "PASS": 0}

def jload(fn):
    return json.load(open(os.path.join(HERE, fn), encoding="utf-8"))

def anyv(P, c):
    fs = P.check_paragraph(c["text"], c.get("context", ""))
    return max([x["verdict"] for x in fs], key=O.get, default="PASS")

def compare():
    h = hashlib.sha256(open(os.path.join(HERE, "reviewer-heldout-W.json"), "rb").read()).hexdigest()
    print("batch W SHA-256", h, "matches published" if h == W_SHA else "MISMATCH")
    tot = {k: Counter() for k in ("r3", "r4")}
    for label, fn in CONTROL_FILES + PROBES + WBATCH + DIAG:
        cs = jload(fn)
        if isinstance(cs, dict):
            cs = cs.get("controls") or cs.get("items") or cs.get("sentences")
        print(label)
        for name, P in (("r3", P3), ("r4", P4)):
            cnt = Counter(); ms = []; anymiss = 0
            for c in cs:
                exp = c.get("expect", "FAIL")
                o = P.outcome(exp, P.verdict_for(c["text"], c["rule"], c.get("context", ""))[0])
                cnt[o] += 1
                if o in ("MISS", "FPFAIL"):
                    ms.append(c["id"] + ":" + o)
                if exp != "PASS" and anyv(P, c) == "PASS":
                    anymiss += 1
            if fn in dict(CONTROL_FILES).values():
                tot[name] += cnt
            extra = ("   any-rule silent PASS %d" % anymiss) if label.startswith(("batch W", "author")) else ""
            print("   %-3s exact %2d  blocked %2d  load %2d  MISS %2d  FPFAIL %2d%s   %s" % (
                name, cnt["exact"], cnt["blocked"], cnt["load"], cnt["MISS"], cnt["FPFAIL"], extra, " ".join(ms)))
    print("ALL CONTROL FILES (195)")
    for name, c in tot.items():
        print("   %-3s exact %3d  blocked %3d  load %3d  MISS %2d  FPFAIL %2d" % (name, c["exact"], c["blocked"], c["load"], c["MISS"], c["FPFAIL"]))
    print("per-item changes r3 -> r4 (per-rule verdict):")
    for label, fn in CONTROL_FILES + PROBES + WBATCH + DIAG:
        for c in jload(fn):
            a = P3.verdict_for(c["text"], c["rule"], c.get("context", ""))[0]
            b = P4.verdict_for(c["text"], c["rule"], c.get("context", ""))[0]
            if a != b:
                print("   %-14s %-14s expect %-6s r3 %-6s r4 %-6s" % (c["id"], c["rule"], c.get("expect", "?"), a, b))

# ------------------------------------------------------------------ exit codes and records
def run(proto, args):
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, proto)] + args, capture_output=True, text=True)
    return p.returncode, p.stdout

def write(root, rel, text):
    p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text)

def exitcodes(repo, mainref):
    rows = []
    R = ("--repo", repo, "--main", mainref)
    section = ["r3 controls"]
    def case(name, files, expect, licences=None, reviews=None, extra=R):
        got = {}
        for tag, proto in (("r3", "proto.r3.py"), ("r4", "proto.r4.py")):
            with tempfile.TemporaryDirectory() as d:
                t = os.path.join(d, "t"); os.makedirs(t)
                for rel, text in files.items():
                    write(t, rel, text)
                args = ["--scan", t, "--json", os.path.join(d, "o.json")]
                write(d, "lic.json", json.dumps(licences if licences is not None else {"schema": "claims-licences/3", "entries": []}))
                args += ["--licences", os.path.join(d, "lic.json")]
                if reviews is not None:
                    write(d, "rev.json", reviews if isinstance(reviews, str) else json.dumps(reviews)); args += ["--reviews", os.path.join(d, "rev.json")]
                code, out = run(proto, args + list(extra))
                got[tag] = (code, out.strip().splitlines()[-1] if out.strip() else "")
        rows.append((got["r4"][0] == expect, section[0], name, expect, got["r3"][0], got["r4"][0], got["r4"][1]))
    FAILS = "The Hawking temperature $T_Q$ is state-independent.\n"
    neg = "The Hawking temperature $T_Q$ is not state-independent."
    hs = "Quantum mechanics requires observational incompleteness only if H-slope holds."
    hh = "Any QFT on this background is periodic in imaginary time only under the H-Hawking conditions."
    flip = "If H-balance fails, the Hawking temperature $T_Q$ is still state-independent."
    anap_prev, anap = "The calibration fixes $T_Q$ on the de Sitter horizon.", "It is state-independent."
    def rec(sent, rule, code, decision, **kw):
        r = {"rule": rule, "path": "papers/x.md", "sentence": sent, "sentence_sha256": P4.norm_hash(sent), "code": code,
             "decision": decision, "reason": "test", "reviewer": "test-reviewer", "revision": REV, "date": "2026-11-25",
             "authority": "test authority"}
        r.update(kw); return {"records": [r]}
    lic_ok = {"schema": "claims-licences/3", "entries": [{
        "id": "LIC-KMS-1", "rule": "W-GR-KMS", "qualifier": r"H-Hawking", "proposer": "proposer-a",
        "anchor": {"path": "papers/GR.md", "revision": REV,
                   "quote": "a preferred-frame dispersive lattice theory satisfies it only under the H-Hawking conditions of §8.5"},
        "review": {"reviewer": "reviewer-b", "record": "papers/GR.md", "date": "2026-11-25", "revision": REV},
        "adoption": {"author": "owner", "time": "2026-11-25T00:00:00Z", "quote": "synthetic test entry"}}]}
    def lic_with(**kw):
        L = json.loads(json.dumps(lic_ok)); e = L["entries"][0]
        for k, v in kw.items():
            if v is None:
                e.pop(k, None)
            elif isinstance(v, dict):
                e[k].update(v)
            else:
                e[k] = v
        return L
    # ---- the 41 r3 controls, unchanged except the one whose expectation correction (2) reverses
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
    case("record with a wrong code (F5: code is matched exactly)", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "A", "unrelated", basis="negated", evidence="is not state-independent", window_sha256="x"))
    case("record cannot resolve a FAIL", {"papers/x.md": FAILS}, 3, reviews=rec(FAILS.strip(), "W-GR-TQ-STATE", "B", "unrelated", basis="other-subject", evidence="The"))
    case("unreadable review file", {"papers/x.md": "Nothing.\n"}, 3, reviews="{not json")
    case("F2: governed on unlicensed H-slope (no licence cited)", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "governed", evidence="only if H-slope holds"))
    case("F2: governed citing a licence id absent from the (empty) list", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "governed", licence="LIC-OI-1", evidence="only if H-slope holds"))
    case("F2: unrelated resting on the qualifier itself", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="negated", evidence="only if H-slope holds"))
    case("F2: unrelated 'other-subject' citing the rule's own subject", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="other-subject", evidence="Quantum mechanics"))
    case("F1/F3: 'negated' basis on a polarity-flipped qualifier", {"papers/x.md": flip + "\n"}, 3, reviews=rec(flip, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="fails, the Hawking temperature $T_Q$ is still state-independent"))
    dn = "It is not false that the free-level cone is exact per channel."
    case("double negation cannot be recorded as negated", {"papers/x.md": dn + "\n"}, 3, reviews=rec(dn, "W-GR-CONE", "C", "unrelated", basis="negated", evidence="not false that the free-level cone is exact"))
    case("mention basis outside any quotation", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="mention", evidence="requires observational incompleteness"))
    qs = "Is the Hawking temperature $T_Q$ state-independent?"
    case("question record whose evidence lacks the cue (r3 expected 0; reversed by correction 2)", {"papers/x.md": qs + "\n"}, 3, reviews=rec(qs, "W-GR-TQ-STATE", "C", "unrelated", basis="question", evidence="Is the Hawking temperature"))
    case("anaphora REVIEW (code A) unresolved", {"papers/x.md": anap_prev + " " + anap + "\n"}, 2)
    win = P4.norm_hash("" + "\n\n" + anap_prev + " " + anap + "\n")
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
    c3, _ = run("proto.r3.py", ["--bogus"]); c4, _ = run("proto.r4.py", ["--bogus"])
    rows.append((c4 == 4, section[0], "usage error", 4, c3, c4, ""))

    # ---- the r3 review's record-loophole probes (finding 2, finding 3); each must exit 3 under r4
    section[0] = "review loophole probes"
    s1 = 'Under H-slope, the Hawking temperature $T_Q$ is state-independent in the "standard" sense.'
    case("mention: unrelated quoted word, H-slope sentence", {"papers/x.md": s1 + "\n"}, 3, reviews=rec(s1, "W-GR-TQ-STATE", "C", "unrelated", basis="mention", evidence="standard"))
    s2 = "The Hawking temperature $T_Q$ is state-independent, as one would expect from H-slope."
    case("supposition: incidental 'would', H-slope sentence", {"papers/x.md": s2 + "\n"}, 3, reviews=rec(s2, "W-GR-TQ-STATE", "C", "unrelated", basis="supposition", evidence="as one would expect"))
    s3 = "Why else would the Hawking temperature $T_Q$ be state-independent under H-slope?"
    case("question: rhetorical question under H-slope", {"papers/x.md": s3 + "\n"}, 3, reviews=rec(s3, "W-GR-TQ-STATE", "C", "unrelated", basis="question", evidence="Why else"))
    s5 = "Coupling-degree minimization, on this reading, singles out six components."
    case("other-subject: W-KDEG citing its own subject (duplicate id)", {"papers/x.md": s5 + "\n"}, 3, reviews=rec(s5, "W-KDEG", "C", "unrelated", basis="other-subject", evidence="Coupling-degree minimization"))
    s6 = "Under H-Hawking, any QFT on this background is periodic in imaginary time."
    case("governed, empty list, licence=''", {"papers/x.md": s6 + "\n"}, 3, reviews=rec(s6, "W-GR-KMS", "C", "governed", licence="", evidence="Under H-Hawking"))
    case("governed, empty list, no licence key", {"papers/x.md": s6 + "\n"}, 3, reviews=rec(s6, "W-GR-KMS", "C", "governed", evidence="Under H-Hawking"))
    case("record for another path", {"papers/x.md": neg + "\n"}, 3, reviews={"records": [dict(good["records"][0], path="book/y.md")]})
    case("revision on the research branch, not on main", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent", revision=BRANCH_REV))
    case("--repo bogus directory", {"papers/x.md": neg + "\n"}, 3, reviews=good, extra=("--repo", "/nonexistent", "--main", mainref))

    # ---- r4 corrections, each isolated
    section[0] = "r4 correction (1) H-token"
    hneg = "Under H-slope the Hawking temperature $T_Q$ is not state-independent."
    case("negated record on a sentence with an H-token (evidence clean)", {"papers/x.md": hneg + "\n"}, 3, reviews=rec(hneg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent"))
    hchi = "Quantum mechanics does not require observational incompleteness, which H-χ concerns."
    case("other-subject record on a sentence with a non-ASCII H-token (H-χ)", {"papers/x.md": hchi + "\n"}, 3, reviews=rec(hchi, "W-OI-REQ", "C", "unrelated", basis="other-subject", evidence="which"))
    # correction (1) is checked first, so it would mask the r3 checks on H-token sentences; each masked
    # r3 check is re-exercised here on a sentence without an H-token, so that none becomes vacuous
    hs0 = "Quantum mechanics requires observational incompleteness only if the bound holds."
    case("unmasked: unrelated resting on a qualifier (no H-token)", {"papers/x.md": hs0 + "\n"}, 3, reviews=rec(hs0, "W-OI-REQ", "C", "unrelated", basis="negated", evidence="only if the bound holds"))
    case("unmasked: other-subject citing the rule's own subject (no H-token)", {"papers/x.md": hs0 + "\n"}, 3, reviews=rec(hs0, "W-OI-REQ", "C", "unrelated", basis="other-subject", evidence="Quantum mechanics"))
    case("unmasked: mention outside any quotation (no H-token)", {"papers/x.md": hs0 + "\n"}, 3, reviews=rec(hs0, "W-OI-REQ", "C", "unrelated", basis="mention", evidence="requires observational incompleteness"))
    flip0 = "Even at the bound, the Hawking temperature $T_Q$ is not state-independent."
    case("unmasked: negated on a concessive sentence (no H-token)", {"papers/x.md": flip0 + "\n"}, 3, reviews=rec(flip0, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent"))
    case("governed record with a valid licence still resolves an H-token sentence", {"papers/x.md": hh + "\n"}, 0, licences=lic_ok, reviews=rec(hh, "W-GR-KMS", "C", "governed", licence="LIC-KMS-1", evidence="only under the H-Hawking conditions"))
    section[0] = "r4 correction (2) own match"
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
    winq = P4.norm_hash("" + "\n\n" + anap_prev + " " + aq + "\n")
    case("question, code A: evidence carries cue and anaphor", {"papers/x.md": anap_prev + " " + aq + "\n"}, 0, reviews=rec(aq, "W-GR-TQ-STATE", "A", "unrelated", basis="question", evidence="Is it state-independent", window_sha256=winq))
    case("question, code A: evidence lacks the anaphor", {"papers/x.md": anap_prev + " " + aq + "\n"}, 3, reviews=rec(aq, "W-GR-TQ-STATE", "A", "unrelated", basis="question", evidence="state-independent", window_sha256=winq))
    pp = 'The words "state-independent" and "draft" recur in the earlier note.'
    case("mention, code P: quoted evidence carries the strong cue", {"papers/x.md": pp + "\n"}, 0, reviews=rec(pp, "W-GR-TQ-STATE", "P", "unrelated", basis="mention", evidence="state-independent"))
    case("mention, code P: quoted evidence lacks the strong cue", {"papers/x.md": pp + "\n"}, 3, reviews=rec(pp, "W-GR-TQ-STATE", "P", "unrelated", basis="mention", evidence="draft"))
    section[0] = "r4 correction (3) W-KDEG-ANSWER"
    ka = "Is the framework's answer $K = 2d$ here?"
    case("record citing rule W-KDEG for a W-KDEG-ANSWER finding is stale", {"papers/x.md": ka + "\n"}, 3, reviews=rec(ka, "W-KDEG", "C", "unrelated", basis="question", evidence="Is the framework's answer $K = 2d$ here"))
    case("record citing W-KDEG-ANSWER resolves it", {"papers/x.md": ka + "\n"}, 0, reviews=rec(ka, "W-KDEG-ANSWER", "C", "unrelated", basis="question", evidence="Is the framework's answer $K = 2d$ here"))
    case("other-subject citing the W-KDEG-ANSWER argument", {"papers/x.md": "The framework's answer, it seems, is $K = 2d$.\n"}, 3, reviews=rec("The framework's answer, it seems, is $K = 2d$.", "W-KDEG-ANSWER", "C", "unrelated", basis="other-subject", evidence="The framework's answer"))
    section[0] = "r4 --main default"
    case("valid record, --repo, no --main: revision on origin/main", {"papers/x.md": neg + "\n"}, 0, reviews=good, extra=("--repo", repo))
    case("record at a research-branch revision, --repo, no --main", {"papers/x.md": neg + "\n"}, 3, reviews=rec(neg, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="is not state-independent", revision=BRANCH_REV), extra=("--repo", repo))
    # ---- residual left by the corrections as stated, measured and reported to the owner, not corrected:
    # correction (1) reads the sentence, so an H-token in the anaphora window of a code-A finding is not seen
    section[0] = "documented residual (not corrected in r4)"
    hp = "Under H-slope, the calibration fixes $T_Q$ on the de Sitter horizon."
    winh = P4.norm_hash("" + "\n\n" + hp + " " + anap + "\n")
    case("code A: H-token only in the window; other-subject record accepted", {"papers/x.md": hp + " " + anap + "\n"}, 0, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is", window_sha256=winh))
    bad = 0
    cur = None
    for ok, sec, name, exp, r3c, r4c, last in rows:
        if sec != cur:
            print("--", sec); cur = sec
        bad += not ok
        print(("ok  " if ok else "BAD ") + name.ljust(84), "expect", exp, "r3", r3c, "r4", r4c, "|", last[:80])
    by = Counter(r[1] for r in rows)
    print("controls:", len(rows), dict(by), "mismatches under r4:", bad,
          "| r3 differs from expectation on:", sum(1 for r in rows if r[4] != r[3]))

# ------------------------------------------------------------------ injection
PARAS = []
WHICH = ["r4"]

def init(paras, which):
    global PARAS
    PARAS = paras; WHICH[0] = which

def one(args):
    i, c = args
    t = PARAS[i].rstrip() + " " + ((c.get("context", "") + " ") if c.get("context") else "") + c["text"]
    P = P3 if WHICH[0] == "r3" else P4
    return P.verdict_for(t, c["rule"])[0]

def inject(treem, which="r4"):
    paras = []
    for sub in ("papers", "book"):
        for dp, dn, fs in os.walk(os.path.join(treem, sub)):
            dn.sort()
            for f in sorted(fs):
                if f.endswith(".md"):
                    for p in open(os.path.join(dp, f), encoding="utf-8").read().split("\n\n"):
                        if len(p) > 200:
                            paras.append(p)
    print("paragraphs:", len(paras))
    sents = []
    for label, fn in CONTROL_FILES + PROBES + WBATCH:
        for c in jload(fn):
            if c["expect"] in ("FAIL", "REVIEW"):
                sents.append((label, c))
    print("injected sentences (every control, probe and batch-W item expected FAIL or REVIEW):", len(sents))
    tot = Counter(); worst = []; perbatch = Counter()
    print("checker:", which)
    with Pool(initializer=init, initargs=(paras, which)) as pool:
        for label, c in sents:
            res = Counter(pool.map(one, [(i, c) for i in range(len(paras))], chunksize=200))
            tot.update(res)
            if res["PASS"]:
                worst.append((c["id"], res["PASS"])); perbatch[label] += res["PASS"]
    print("total verdicts:", dict(tot))
    print("silent PASS by batch:", dict(perbatch) if perbatch else "none")
    print("sentences with any silent PASS:", worst if worst else "none")

# ------------------------------------------------------------------ M2
def m2(ccpath):
    cc = load("cc", ccpath)
    marks = list(cc.MARKERS) + list(cc.OI_MARKERS)
    res = {"r3": Counter(), "r4": Counter()}; n = 0
    for label, fn in CONTROL_FILES:
        for c in jload(fn):
            if c["expect"] != "FAIL":
                continue
            t = c["text"].rstrip()
            for m in marks:
                for txt in (t + " The text notes " + m + ".", (t[:-1] if t.endswith(".") else t) + ", and the text notes " + m + ".",
                            m[:1].upper() + m[1:] + ": " + t, "Under " + m + ", " + t[:1].lower() + t[1:]):
                    n += 1
                    for k, P in (("r3", P3), ("r4", P4)):
                        res[k][P.verdict_for(txt, c["rule"], c.get("context", ""))[0]] += 1
    print("markers", len(marks), "insertions", n, "r3", dict(res["r3"]), "r4", dict(res["r4"]))

# ------------------------------------------------------------------ tree-M scan
def scan(treem, outdir):
    os.makedirs(outdir, exist_ok=True)
    summ = {}
    for tag, proto in (("r3", "proto.r3.py"), ("r4", "proto.r4.py")):
        j = os.path.join(outdir, "treeM-scan-%s.json" % tag)
        code, out = run(proto, ["--scan", treem, "--json", j])
        d = json.load(open(j))
        act = [x for x in d["findings"] if x["active"] and x["verdict"] != "PASS"]
        summ[tag] = {
            "exit": code, "counts": d["counts"],
            "active_FAIL": sum(x["verdict"] == "FAIL" for x in act),
            "active_REVIEW": sum(x["verdict"] == "REVIEW" for x in act),
            "active_REVIEW_by_code": dict(sorted(Counter(x["code"] for x in act if x["verdict"] == "REVIEW").items())),
            "active_REVIEW_by_rule": dict(sorted(Counter(x["rule"] for x in act if x["verdict"] == "REVIEW").items())),
            "distinct_path_sentence": len({(x["path"], x["sentence_sha256"]) for x in act}),
            "distinct_sentence_texts": len({x["sentence_sha256"] for x in act}),
            "files": len({x["path"] for x in act}),
            "record_REVIEW": sum(1 for x in d["findings"] if not x["active"] and x["verdict"] == "REVIEW"),
        }
        os.remove(j)
        summ[tag]["_keys"] = sorted({(x["rule"], x["path"], x["sentence_sha256"], x["code"]) for x in act})
    k3, k4 = set(map(tuple, summ["r3"].pop("_keys"))), set(map(tuple, summ["r4"].pop("_keys")))
    summ["delta"] = {"active_findings_only_r3": sorted(k3 - k4), "active_findings_only_r4": sorted(k4 - k3)}
    print(json.dumps({k: v for k, v in summ.items() if k != "delta"}, indent=1))
    print("findings only under r3:", len(k3 - k4), " only under r4:", len(k4 - k3))
    for k in sorted(k3 - k4):
        print("   -", k[0], k[1], k[3])
    for k in sorted(k4 - k3):
        print("   +", k[0], k[1], k[3])
    return summ

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "compare":
        compare()
    elif cmd == "exitcodes":
        exitcodes(sys.argv[2], sys.argv[3])
    elif cmd == "inject":
        inject(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "r4")
    elif cmd == "m2":
        m2(sys.argv[2])
    elif cmd == "scan":
        s = scan(sys.argv[2], sys.argv[3])
        json.dump(s, open(os.path.join(sys.argv[3], "treeM-scan-summary-r4.json"), "w"), indent=1)
    else:
        print(__doc__)
