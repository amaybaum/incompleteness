#!/usr/bin/env python3
"""Measurement harness for DESIGN-r3 (paper-only). Usage, from this directory:
  run_r3.py compare                       r2 (fixture and deployed empty licences) vs r3 on every control
                                          file and on the review's diagnostic probes
  run_r3.py exitcodes REPO MAINREF        exit-code, licence and review-record controls on synthetic trees
  run_r3.py inject TREEM [r2]             corpus injection of every positive and ambiguous control and probe
  run_r3.py m1                            deletion mutants of every control expected PASS or REVIEW (M1)
  run_r3.py m2 CURRENT_CHECKER            marker insertion into every positive control (M2)
Writes nothing outside a temporary directory."""
import sys, os, json, subprocess, tempfile, importlib.util
from multiprocessing import Pool
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))

def load(name, path):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m

P3 = load("p3", os.path.join(HERE, "proto.r3.py"))
P2 = load("p2", os.path.join(HERE, "proto.r2.py"))
FIX2 = json.load(open(os.path.join(HERE, "licences-fixture.json")))
EMPTY2 = {"fixture": False, "entries": []}
REV = "e2e2a623265187a28ebec604ab8bcc672742888f"

CONTROL_FILES = [("batch 1 (63)", "controls.json"), ("batch H (20)", "heldout.json"), ("batch C (5)", "controls_c.json"),
                 ("batch D (4)", "controls_d.json"), ("batch X (34)", "reviewer-heldout.json"),
                 ("batch R2 (26)", "controls_r2.json"), ("batch Y (43)", "reviewer-heldout-Y.json")]
PROBES = [("probe (13)", "reviewer-probes/probe.json"), ("probe2 (9)", "reviewer-probes/probe2.json"),
          ("probe3 (2)", "reviewer-probes/probe3.json"), ("probe4 (6)", "reviewer-probes/probe4.json"),
          ("Z post-hoc (10)", "reviewer-probes-Y/posthoc-probes.json"), ("M1 diag (8)", "reviewer-probes-Y/m1-diag.json")]

def r2v(c, L):
    v, _ = P2.verdict_for(c["text"], c["rule"], c.get("context", ""), L)
    return v

def compare():
    tot = {k: Counter() for k in ("r2-fixture", "r2-empty", "r3")}
    for label, fn in CONTROL_FILES + PROBES:
        cs = json.load(open(os.path.join(HERE, fn), encoding="utf-8"))
        row = {}
        misses = {}
        for name, f in (("r2-fixture", lambda c: r2v(c, FIX2)), ("r2-empty", lambda c: r2v(c, EMPTY2)),
                        ("r3", lambda c: P3.verdict_for(c["text"], c["rule"], c.get("context", ""))[0])):
            cnt = Counter(); ms = []
            for c in cs:
                o = P3.outcome(c["expect"], f(c))
                cnt[o] += 1
                if o in ("MISS", "FPFAIL"):
                    ms.append(c["id"] + ":" + o)
            row[name] = cnt; misses[name] = ms
            if not label.startswith(("probe", "Z", "M1")):
                tot[name] += cnt
        print(label)
        for name in row:
            c = row[name]
            print("   %-10s exact %2d  blocked %2d  load %2d  MISS %2d  FPFAIL %2d   %s" % (
                name, c["exact"], c["blocked"], c["load"], c["MISS"], c["FPFAIL"], " ".join(misses[name])))
    print("ALL CONTROL FILES (195)")
    for name, c in tot.items():
        print("   %-10s exact %3d  blocked %3d  load %3d  MISS %2d  FPFAIL %2d" % (name, c["exact"], c["blocked"], c["load"], c["MISS"], c["FPFAIL"]))

# ------------------------------------------------------------------ exit codes and records
def run(args):
    p = subprocess.run([sys.executable, os.path.join(HERE, "proto.r3.py")] + args, capture_output=True, text=True)
    return p.returncode, p.stdout

def write(root, rel, text):
    p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text)

def exitcodes(repo, mainref):
    rows = []
    R = ("--repo", repo, "--main", mainref)
    def case(name, files, expect, licences=None, reviews=None, extra=R):
        with tempfile.TemporaryDirectory() as d:
            t = os.path.join(d, "t"); os.makedirs(t)
            for rel, text in files.items():
                write(t, rel, text)
            args = ["--scan", t, "--json", os.path.join(d, "o.json")]
            write(d, "lic.json", json.dumps(licences if licences is not None else {"schema": "claims-licences/3", "entries": []}))
            args += ["--licences", os.path.join(d, "lic.json")]
            if reviews is not None:
                write(d, "rev.json", reviews if isinstance(reviews, str) else json.dumps(reviews)); args += ["--reviews", os.path.join(d, "rev.json")]
            code, out = run(args + list(extra))
            rows.append((code == expect, name, expect, code, out.strip().splitlines()[-1] if out.strip() else ""))
    FAILS = "The Hawking temperature $T_Q$ is state-independent.\n"
    neg = "The Hawking temperature $T_Q$ is not state-independent."
    hs = "Quantum mechanics requires observational incompleteness only if H-slope holds."
    hh = "Any QFT on this background is periodic in imaginary time only under the H-Hawking conditions."
    flip = "If H-balance fails, the Hawking temperature $T_Q$ is still state-independent."
    anap_prev, anap = "The calibration fixes $T_Q$ on the de Sitter horizon.", "It is state-independent."
    def rec(sent, rule, code, decision, **kw):
        r = {"rule": rule, "path": "papers/x.md", "sentence": sent, "sentence_sha256": P3.norm_hash(sent), "code": code,
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
    # F2: licensing enforced in records
    case("F2: governed on unlicensed H-slope (no licence cited)", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "governed", evidence="only if H-slope holds"))
    case("F2: governed citing a licence id absent from the (empty) list", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "governed", licence="LIC-OI-1", evidence="only if H-slope holds"))
    case("F2: unrelated resting on the qualifier itself", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="negated", evidence="only if H-slope holds"))
    case("F2: unrelated 'other-subject' citing the rule's own subject", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="other-subject", evidence="Quantum mechanics"))
    case("F1/F3: 'negated' basis on a polarity-flipped qualifier", {"papers/x.md": flip + "\n"}, 3, reviews=rec(flip, "W-GR-TQ-STATE", "C", "unrelated", basis="negated", evidence="fails, the Hawking temperature $T_Q$ is still state-independent"))
    dn = "It is not false that the free-level cone is exact per channel."
    case("double negation cannot be recorded as negated", {"papers/x.md": dn + "\n"}, 3, reviews=rec(dn, "W-GR-CONE", "C", "unrelated", basis="negated", evidence="not false that the free-level cone is exact"))
    case("mention basis outside any quotation", {"papers/x.md": hs + "\n"}, 3, reviews=rec(hs, "W-OI-REQ", "C", "unrelated", basis="mention", evidence="requires observational incompleteness"))
    qs = "Is the Hawking temperature $T_Q$ state-independent?"
    case("question resolved by a valid question record", {"papers/x.md": qs + "\n"}, 0, reviews=rec(qs, "W-GR-TQ-STATE", "C", "unrelated", basis="question", evidence="Is the Hawking temperature"))
    case("anaphora REVIEW (code A) unresolved", {"papers/x.md": anap_prev + " " + anap + "\n"}, 2)
    win = P3.norm_hash("" + "\n\n" + anap_prev + " " + anap + "\n")
    case("anaphora record without window hash", {"papers/x.md": anap_prev + " " + anap + "\n"}, 3, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is"))
    case("anaphora record with its window hash", {"papers/x.md": anap_prev + " " + anap + "\n"}, 0, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is", window_sha256=win))
    case("anaphora record with a stale window hash", {"papers/x.md": "Context. " + anap_prev + " " + anap + "\n"}, 3, reviews=rec(anap, "W-GR-TQ-STATE", "A", "unrelated", basis="other-subject", evidence="It is", window_sha256=win))
    # licences: a governed record works only with an owner-adopted, reviewed, validated licence
    case("governed with a valid licence entry (synthetic)", {"papers/x.md": hh + "\n"}, 0, licences=lic_ok, reviews=rec(hh, "W-GR-KMS", "C", "governed", licence="LIC-KMS-1", evidence="only under the H-Hawking conditions"))
    case("governed with a licence for another rule", {"papers/x.md": hs + "\n"}, 3, licences=lic_ok, reviews=rec(hs, "W-OI-REQ", "C", "governed", licence="LIC-KMS-1", evidence="only if H-slope holds"))
    case("licence without proposer", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(proposer=None))
    case("licence reviewed by its proposer", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(review={"reviewer": "proposer-a"}))
    case("licence without quoted owner adoption", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(adoption=None))
    case("licence review record path absent on main", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(review={"record": "verification/no/such/record.md"}))
    case("licence anchor quotation absent at its revision", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_with(anchor={"quote": "a sentence that is not in GR.md"}))
    case("licence entries but no --repo", {"papers/x.md": "Nothing.\n"}, 3, licences=lic_ok, extra=())
    case("licence file with the r2 schema", {"papers/x.md": "Nothing.\n"}, 3, licences={"schema": "claims-licences/1", "fixture": True, "entries": []})
    code, out = run(["--bogus"])
    rows.append((code == 4, "usage error", 4, code, ""))
    bad = 0
    for ok, name, exp, got, last in rows:
        bad += not ok
        print(("ok  " if ok else "BAD ") + name.ljust(64), "expect", exp, "got", got, "|", last[:90])
    print("exit-code controls:", len(rows), "mismatches:", bad)

# ------------------------------------------------------------------ injection
PARAS = []
WHICH = ["r3"]

def init(paras, which):
    global PARAS
    PARAS = paras; WHICH[0] = which

def one(args):
    i, c = args
    t = PARAS[i].rstrip() + " " + ((c.get("context", "") + " ") if c.get("context") else "") + c["text"]
    if WHICH[0] == "r2":
        return P2.verdict_for(t, c["rule"], "", EMPTY2)[0]
    return P3.verdict_for(t, c["rule"])[0]

def inject(treem, which="r3"):
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
    for label, fn in CONTROL_FILES + PROBES:
        for c in json.load(open(os.path.join(HERE, fn), encoding="utf-8")):
            if c["expect"] in ("FAIL", "REVIEW"):
                sents.append((label, c))
    print("injected sentences (every control and probe expected FAIL or REVIEW):", len(sents))
    tot = Counter(); worst = []
    print("checker:", which, "(r2 under the deployed empty licence file)" if which == "r2" else "")
    with Pool(initializer=init, initargs=(paras, which)) as pool:
        for label, c in sents:
            res = Counter(pool.map(one, [(i, c) for i in range(len(paras))], chunksize=200))
            tot.update(res)
            if res["PASS"]:
                worst.append((c["id"], res["PASS"]))
    print("total verdicts:", dict(tot))
    print("sentences with any silent PASS:", worst if worst else "none")

# ------------------------------------------------------------------ M1
def m1():
    """Deletion mutants of every control expected PASS or REVIEW: every single-word and two-adjacent-word
    deletion.  A mutant one of whose sentence units still contains every argument and cue match of its rule
    must not PASS."""
    import re
    rules = {}
    for r in P3.RULES:
        rules.setdefault(r["id"], []).append(r)
    n = keep = bad = 0; res = Counter()
    for label, fn in CONTROL_FILES:
        for c in json.load(open(os.path.join(HERE, fn), encoding="utf-8")):
            if c["expect"] == "FAIL":
                continue
            w = c["text"].split(" ")
            for k in (1, 2):
                for i in range(len(w) - k + 1):
                    t = " ".join(w[:i] + w[i + k:])
                    n += 1
                    units = [t[a:b] for a, b in P3.sentences(t)]
                    if not any("literal" not in r and P3._all(r["args"] + r["cues"], u) for r in rules[c["rule"]] for u in units):
                        continue
                    keep += 1
                    v = P3.verdict_for(t, c["rule"], c.get("context", ""))[0]
                    res[v] += 1
                    bad += v == "PASS"
    print("mutants", n, "keeping every argument and cue", keep, dict(res), "PASS among them:", bad)

# ------------------------------------------------------------------ M2
def m2(ccpath):
    cc = load("cc", ccpath)
    marks = list(cc.MARKERS) + list(cc.OI_MARKERS)
    res = Counter(); n = 0
    for label, fn in CONTROL_FILES:
        for c in json.load(open(os.path.join(HERE, fn), encoding="utf-8")):
            if c["expect"] != "FAIL":
                continue
            t = c["text"].rstrip()
            for m in marks:
                for txt in (t + " The text notes " + m + ".", (t[:-1] if t.endswith(".") else t) + ", and the text notes " + m + ".",
                            m[:1].upper() + m[1:] + ": " + t, "Under " + m + ", " + t[:1].lower() + t[1:]):
                    res[P3.verdict_for(txt, c["rule"], c.get("context", ""))[0]] += 1; n += 1
    print("markers", len(marks), "insertions", n, dict(res))

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "compare":
        compare()
    elif cmd == "exitcodes":
        exitcodes(sys.argv[2], sys.argv[3])
    elif cmd == "inject":
        inject(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "r3")
    elif cmd == "m1":
        m1()
    elif cmd == "m2":
        m2(sys.argv[2])
    else:
        print(__doc__)
