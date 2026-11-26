#!/usr/bin/env python3
"""Measurement harness for DESIGN-r2 (paper-only). Usage:
  run_r2.py exitcodes REPO MAINREF        exit-code, licence and review-record controls on synthetic trees
  run_r2.py inject TREEM CURRENT_CHECKER   corpus injection (papers/ and book/ of tree M)
Prints results; writes nothing outside a temporary directory."""
import sys, os, json, re, random, subprocess, tempfile, importlib.util, hashlib
from multiprocessing import Pool
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PROTO = os.path.join(HERE, "proto.r2.py")
spec = importlib.util.spec_from_file_location("pr", PROTO); pr = importlib.util.module_from_spec(spec); spec.loader.exec_module(pr)
REV = "e2e2a623265187a28ebec604ab8bcc672742888f"

def run(args):
    p = subprocess.run([sys.executable, PROTO] + args, capture_output=True, text=True)
    return p.returncode, p.stdout

def write(root, rel, text):
    p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w").write(text)

def exitcodes(repo, mainref):
    rows = []
    def case(name, files, expect, licences=None, reviews=None, extra=()):
        with tempfile.TemporaryDirectory() as d:
            t = os.path.join(d, "t"); os.makedirs(t)
            for rel, text in files.items():
                write(t, rel, text)
            args = ["--scan", t, "--json", os.path.join(d, "o.json")]
            if licences is not None:
                write(d, "lic.json", json.dumps(licences)); args += ["--licences", os.path.join(d, "lic.json")]
            if reviews is not None:
                write(d, "rev.json", reviews if isinstance(reviews, str) else json.dumps(reviews)); args += ["--reviews", os.path.join(d, "rev.json")]
            args += list(extra)
            code, out = run(args)
            rows.append((code == expect, name, expect, code))
    FAILS = "The Hawking temperature $T_Q$ is state-independent.\n"
    REVS = "Quantum mechanics rests on observational incompleteness.\n"
    sent = "Quantum mechanics rests on observational incompleteness."
    sha = pr.norm_hash(sent)
    good = {"rule": "W-OI-REQ", "path": "papers/x.md", "sentence_sha256": sha, "sentence": sent, "code": "N1",
            "window_sha256": pr.norm_hash("" + "\n\n" + REVS), "decision": "unrelated", "reason": "test",
            "reviewer": "test-reviewer", "revision": REV, "date": "2026-11-25", "authority": "test"}
    case("clean active tree", {"papers/x.md": "Nothing here.\n"}, 0)
    case("FAIL in papers/", {"papers/x.md": FAILS}, 1)
    case("REVIEW only in papers/", {"papers/x.md": REVS}, 2)
    case("FAIL and REVIEW in papers/ (FAIL wins)", {"papers/x.md": FAILS + "\n" + REVS}, 1)
    case("FAIL in a verification record (reported, exit 0)", {"verification/a/b.md": FAILS}, 0)
    case("FAIL in verification/README.md (active)", {"verification/README.md": FAILS}, 1)
    case("FAIL in a README under verification/a/ (record)", {"verification/a/README.md": FAILS}, 0)
    case("FAIL in tools/README.md (active)", {"tools/README.md": FAILS}, 1)
    case("FAIL in AGENTS.md record section", {"AGENTS.md": "## §A.1 Rule\n\nText.\n\n## §A.37 Old lifecycle (record)\n\n" + FAILS}, 0)
    case("FAIL in AGENTS.md ordinary section", {"AGENTS.md": "## §A.37 Old (record)\n\nText.\n\n## §A.38 Rule\n\n" + FAILS}, 1)
    case("REVIEW resolved by a valid record", {"papers/x.md": REVS}, 0, reviews={"records": [good]}, extra=("--repo", repo, "--main", mainref))
    case("record revision not on main", {"papers/x.md": REVS}, 3, reviews={"records": [dict(good, revision="0" * 40)]}, extra=("--repo", repo, "--main", mainref))
    case("record revision abbreviated", {"papers/x.md": REVS}, 3, reviews={"records": [dict(good, revision=REV[:12])]})
    case("record missing reviewer", {"papers/x.md": REVS}, 3, reviews={"records": [dict(good, reviewer="")]})
    case("stale record (sentence edited)", {"papers/x.md": "Quantum mechanics rests on observational incompleteness alone.\n"}, 3, reviews={"records": [good]})
    case("stale record (window changed for N1)", {"papers/x.md": "Context.\n\n" + REVS}, 3, reviews={"records": [good]})
    fs = "The Hawking temperature $T_Q$ is state-independent."
    case("record cannot resolve a FAIL", {"papers/x.md": FAILS}, 3, reviews={"records": [dict(good, rule="W-GR-TQ-STATE", sentence=fs, sentence_sha256=pr.norm_hash(fs), code="asserted")]})
    case("unreadable review file", {"papers/x.md": "Nothing.\n"}, 3, reviews="{not json")
    unrev = {"schema": "claims-licences/1", "fixture": False, "entries": [
        {"rule": "W-GR-TQ-STATE", "qualifier": "H-slope", "proposer": "a",
         "anchor": {"path": "papers/GR.md", "revision": REV, "quote": "H-slope: the minimal condition the calibration needs, and its status."}, "review": None}]}
    case("unreviewed licence entry (H-slope)", {"papers/x.md": "Nothing.\n"}, 3, licences=unrev)
    selfrev = json.loads(json.dumps(unrev)); selfrev["entries"][0]["review"] = {"reviewer": "a", "record": "x", "date": "2026-11-25", "revision": REV}
    case("licence reviewed by its proposer", {"papers/x.md": "Nothing.\n"}, 3, licences=selfrev)
    badq = json.loads(json.dumps(selfrev)); badq["entries"][0]["review"]["reviewer"] = "b"; badq["entries"][0]["anchor"]["quote"] = "a sentence that is not in GR.md"
    case("licence anchor quotation absent at its revision", {"papers/x.md": "Nothing.\n"}, 3, licences=badq, extra=("--repo", repo, "--main", mainref))
    case("fixture licence file refused for a scan", {"papers/x.md": "Nothing.\n"}, 3,
         licences=json.load(open(os.path.join(HERE, "licences-fixture.json"))))
    code, out = run(["--bogus"])
    rows.append((code == 4, "usage error", 4, code))
    bad = 0
    for ok, name, exp, got in rows:
        bad += not ok
        print(("ok  " if ok else "BAD ") + name.ljust(52), "expect", exp, "got", got)
    print("exit-code controls:", len(rows), "mismatches:", bad)

# ------------------------------------------------------------------ injection
INJ = [
 ("pos-TQ", "W-GR-TQ-STATE", "The Hawking temperature $T_Q$ is state-independent.", "notPASS"),
 ("pos-OI", "W-OI-REQ", "Quantum mechanics requires observational incompleteness.", "notPASS"),
 ("gov-TQ", "W-GR-TQ-STATE", "Under H-balance, the Hawking temperature $T_Q$ is state-independent.", "PASS-fixture"),
 ("gov-OI", "W-OI-REQ", "No theorem shows that quantum mechanics requires observational incompleteness.", "PASS"),
 ("flip-TQ-even-without", "W-GR-TQ-STATE", "Even without H-balance, the Hawking temperature $T_Q$ is state-independent.", "notPASS"),
 ("flip-TQ-fails", "W-GR-TQ-STATE", "If H-balance fails, the Hawking temperature $T_Q$ is still state-independent.", "notPASS"),
 ("flip-OI-stronger", "W-OI-REQ", "Quantum mechanics requires observational incompleteness in a sense stronger than the core-containment sense.", "notPASS"),
 ("xclause-OI-yet", "W-OI-REQ", "No theorem shows that hidden sectors are finite, yet quantum mechanics requires observational incompleteness.", "notPASS"),
 ("xclause-TQ-whether-or-not", "W-GR-TQ-STATE", "Whether or not the detector is inertial, the Hawking temperature $T_Q$ is state-independent.", "notPASS"),
 ("xclause-OI-reading", "W-OI-REQ", "On the necessity reading, which we adopt, quantum mechanics requires observational incompleteness.", "notPASS"),
 ("near-OI-rests", "W-OI-REQ", "Quantum mechanics rests on observational incompleteness.", "notPASS"),
]
PARAS = []
CC = None

def init(paras, ccpath):
    global PARAS, CC
    PARAS = paras
    if ccpath:
        s = importlib.util.spec_from_file_location("cc", ccpath); CC = importlib.util.module_from_spec(s); s.loader.exec_module(CC)

def cur(par):
    for rx, why, marks in [(a, b, CC.MARKERS) for a, b in CC.CLAIMS] + [(a, b, CC.OI_MARKERS) for a, b in CC.OI_CLAIMS]:
        if rx.search(par) and not any(k in par for k in marks):
            return "FAIL"
    return "PASS"

FIX = json.load(open(os.path.join(HERE, "licences-fixture.json")))
EMPTY = json.load(open(os.path.join(HERE, "licences.json")))

def one(args):
    i, rule, sent = args
    t = PARAS[i].rstrip() + " " + sent
    out = []
    for L in (FIX, EMPTY):
        fs = [x for x in pr.check_paragraph(t, "", "", L, only=rule) if x["rule"] == rule]
        out.append(max((x["verdict"] for x in fs), key=lambda z: pr.ORDER[z], default="PASS"))
    out.append(cur(t) if CC else "-")
    return out

def inject(treem, ccpath):
    paras = []
    for sub in ("papers", "book"):
        for dp, dn, fs in os.walk(os.path.join(treem, sub)):
            dn.sort()
            for f in sorted(fs):
                if f.endswith(".md"):
                    for p in open(os.path.join(dp, f), encoding="utf-8").read().split("\n\n"):
                        if len(p) > 200:
                            paras.append(p)
    print("paragraphs (papers/ and book/ .md, split on blank lines, longer than 200 characters):", len(paras))
    with Pool(initializer=init, initargs=(paras, ccpath)) as pool:
        for name, rule, sent, exp in INJ:
            res = pool.map(one, [(i, rule, sent) for i in range(len(paras))], chunksize=50)
            fx = Counter(r[0] for r in res); em = Counter(r[1] for r in res); cu = Counter(r[2] for r in res)
            print(name.ljust(28), "expect", exp.ljust(12), "fixture", dict(fx), "| empty licences", dict(em), "| current checker", dict(cu))

if __name__ == "__main__":
    if sys.argv[1] == "exitcodes":
        exitcodes(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "inject":
        inject(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
