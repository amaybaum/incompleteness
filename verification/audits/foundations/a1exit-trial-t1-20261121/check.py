#!/usr/bin/env python3
"""Verify the retained T1 trial evidence against expected.json.

  python3 -I -B check.py                 integrity and outcome checks (standard library only)
  python3 -I -B check.py --self-test     the same checks on mutated copies; each must report its target finding
  python3 -I -B check.py --github        also compare both runs and the artifact with what the host reports (needs gh)
  python3 -I -B check.py --extract DIR   after the checks pass, write the artifact's members to DIR, byte for byte
  python3 -I -B check.py --trial-commit  also check the trial commit's tree, parent and PDF blobs (needs the commit)

The checks:
- artifact.zip (dispatch 1) has the recorded sha256 and size, and exactly the recorded members, each
  with the recorded sha256;
- every file under artifact/ is byte-identical to the member of the same name, and every out/ member
  is present there;
- result.json carries the recorded trial, plan, workflow and run, every step outcome `success`,
  `verdict: pass`, no TeX difference and the recorded page counts;
- each structured report (preserve_check.py and guards_check.py, schema a1exit-checker-result-v1)
  carries the recorded schema, plan, ledger digest, mode and check list, passes every check with no
  discrepancy, and has `verdict: pass`;
- ci-record.json (the run, job and step conclusions of both runs, read from the host's API) has the
  recorded sha256: dispatch 1 has one job, conclusion `success`; dispatch 2 ran on the trial branch at
  the trial commit, concluded `success`, and its 41 jobs all concluded `success`, with no step other
  than the recorded marker step concluding anything but `success`;
- the recorded digests of the trial commit's eight PDFs equal the CI-built PDFs retained for T0 in
  ../a1exit-trial-t0-20261121/expected.json. From main this compares two records; the trial commit is off
  main. `--trial-commit`, where the commit is present locally, checks the commit itself: its tree, its single
  parent, and the sha256 of its eight PDF blobs against those digests.
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
T0_EXPECTED = os.path.join(HERE, "..", "a1exit-trial-t0-20261121", "expected.json")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def check(zb, retained, ci_bytes, exp, t0exp):
    f = []
    d1 = exp["dispatch_1"]
    a = d1["artifact"]
    if sha(zb) != a["sha256"]:
        f.append("artifact.zip sha256 differs from the recorded digest")
    if len(zb) != a["size_in_bytes"]:
        f.append("artifact.zip size differs from the recorded size")
    try:
        z = zipfile.ZipFile(io.BytesIO(zb))
        members = {i.filename: z.read(i) for i in z.infolist()}
    except Exception as e:
        return f + [f"artifact.zip does not open: {e}"]
    if sorted(members) != sorted(a["members"]):
        f.append("artifact members differ from the recorded list")
    for name, digest in sorted(a["members"].items()):
        if name in members and sha(members[name]) != digest:
            f.append(f"member {name}: sha256 differs")
    for name, b in sorted(retained.items()):
        if members.get(name) != b:
            f.append(f"artifact/{name}: not byte-identical to the artifact member")
    for name in sorted(members):
        if name.startswith("out/") and name not in retained:
            f.append(f"artifact/{name}: missing")
    # result.json
    try:
        r = json.loads(members["out/result.json"])
    except Exception as e:
        return f + [f"result.json unreadable: {e}"]
    want = {"trial_sha": exp["trial_sha"], "plan_sha": exp["plan_sha"], "workflow_sha": d1["workflow_sha"],
            "run_id": str(d1["run_id"]), "run_attempt": str(d1["run_attempt"]), "verdict": "pass",
            "tex_files_differing": [], "pdf_pages": d1["pdf_pages_built"]}
    for k, v in want.items():
        if r.get(k) != v:
            f.append(f"result.json {k}: {r.get(k)!r}, expected {v!r}")
    got = {k: v.get("outcome") for k, v in r.get("steps", {}).items()}
    if got != d1["step_outcomes"] or set(got.values()) != {"success"}:
        f.append(f"result.json step outcomes differ from all-success: {got}")
    # structured reports
    for name, w in d1["structured_reports"].items():
        try:
            rep = json.loads(members[f"out/{name}"])
        except Exception as e:
            f.append(f"report {name} unreadable: {e}")
            continue
        for k in ("schema", "plan", "ledger_sha256", "mode", "verdict"):
            if rep.get(k) != w[k]:
                f.append(f"report {name} {k}: {rep.get(k)!r}, expected {w[k]!r}")
        if rep.get("verdict") != "pass":
            f.append(f"report {name}: verdict is not pass")
        checks = rep.get("checks", [])
        if [c.get("name") for c in checks] != w["check_names"]:
            f.append(f"report {name}: check list differs from the recorded one")
        for c in checks:
            if c.get("status") != "pass" or c.get("discrepancies"):
                f.append(f"report {name}: check {c.get('name')!r} is not a clean pass")
    # CI record of both runs
    if sha(ci_bytes) != exp["ci_record"]["sha256"]:
        f.append("ci-record.json sha256 differs from the recorded digest")
    try:
        ci = json.loads(ci_bytes)
        runs = {x["run_id"]: x for x in ci["runs"]}
        f += check_runs(runs, exp)
    except Exception as e:
        f.append(f"ci-record.json unreadable: {e}")
    # the trial commit's PDFs are T0's retained CI-built PDFs
    t0pdfs = {k[len("build/"):]: v for k, v in t0exp["artifact"]["members"].items() if k.startswith("build/")}
    if exp["trial_pdfs_sha256"] != t0pdfs or len(t0pdfs) != 8:
        f.append("the trial commit's PDF digests differ from T0's retained CI-built PDFs")
    return f


def check_runs(runs, exp):
    f = []
    d1, d2 = exp["dispatch_1"], exp["dispatch_2"]
    r1, r2 = runs.get(d1["run_id"]), runs.get(d2["run_id"])
    if not r1 or not r2:
        return ["ci-record.json lacks one of the two runs"]
    for r, d, ref, sha_ in ((r1, d1, "main", d1["workflow_sha"]), (r2, d2, exp["trial_branch"], exp["trial_sha"])):
        for k, v in (("path", d["workflow"]), ("event", "workflow_dispatch"), ("run_attempt", d["run_attempt"]),
                     ("head_branch", ref), ("head_sha", sha_), ("conclusion", "success")):
            if r.get(k) != v:
                f.append(f"run {r.get('run_id')} {k}: {r.get(k)!r}, expected {v!r}")
    if len(r1["jobs"]) != 1 or r1["jobs"][0]["conclusion"] != d1["job_conclusion"]:
        f.append("dispatch 1: job inventory differs from one successful job")
    if len(r2["jobs"]) != d2["jobs"]:
        f.append(f"dispatch 2: {len(r2['jobs'])} jobs, expected {d2['jobs']}")
    bad = [j["name"] for j in r2["jobs"] if j["conclusion"] != "success"]
    if bad:
        f.append(f"dispatch 2: jobs not successful: {bad}")
    steps = [{"job": j["name"], "step": s["name"], "conclusion": s["conclusion"]}
             for r in (r1, r2) for j in r["jobs"] for s in j["steps"] if s["conclusion"] != "success"]
    if steps != d2["non_success_steps"]:
        f.append(f"non-success steps differ from the recorded marker step: {steps}")
    return f


def load():
    exp = json.load(open(os.path.join(HERE, "expected.json")))
    t0exp = json.load(open(T0_EXPECTED))
    zb = open(os.path.join(HERE, "artifact.zip"), "rb").read()
    ci = open(os.path.join(HERE, exp["ci_record"]["file"]), "rb").read()
    retained = {}
    root = os.path.join(HERE, "artifact")
    for dp, _, fs in os.walk(root):
        for n in fs:
            p = os.path.join(dp, n)
            retained[os.path.relpath(p, root).replace(os.sep, "/")] = open(p, "rb").read()
    return zb, retained, ci, exp, t0exp


def rezip(zb, edit):
    src = zipfile.ZipFile(io.BytesIO(zb))
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as dst:
        for i in src.infolist():
            b = edit(i.filename, src.read(i))
            if b is not None:
                dst.writestr(i, b)
    return out.getvalue()


def self_test():
    """Each mutant must be caught by the check it targets: its expected finding must be reported."""
    base = load()
    zb, ret, ci, exp, t0 = base
    if check(*base):
        print("self-test: the unmodified evidence does not pass; mutants not run")
        return 1

    def flip(b):
        return bytes([b[0] ^ 1]) + b[1:] if b else b"x"

    def forge(zb2):
        """Consistent forgery: the recorded digests and retained copies follow zb2."""
        e = json.loads(json.dumps(exp))
        z = zipfile.ZipFile(io.BytesIO(zb2))
        e["dispatch_1"]["artifact"].update(sha256=sha(zb2), size_in_bytes=len(zb2),
                                           members={i.filename: sha(z.read(i)) for i in z.infolist()})
        return zb2, {k: z.read(k) for k in ret if k in z.namelist()}, ci, e, t0

    def member(name, edit):
        d = json.loads(zipfile.ZipFile(io.BytesIO(zb)).read(name))
        edit(d)
        return forge(rezip(zb, lambda n, b: json.dumps(d).encode() if n == name else b))

    def cirec(edit):
        d = json.loads(ci)
        edit(d)
        b = json.dumps(d).encode()
        e = json.loads(json.dumps(exp))
        e["ci_record"]["sha256"] = sha(b)
        return zb, ret, b, e, t0

    def run2(d):
        return next(r for r in d["runs"] if r["run_id"] == exp["dispatch_2"]["run_id"])

    def t0edit(edit):
        e = json.loads(json.dumps(t0))
        edit(e)
        return zb, ret, ci, exp, e

    def w(i, v):
        t = list(base)
        t[i] = v
        return tuple(t)

    tree = "out/preserve_check-tree.json"
    mutants = {
        "one byte of the zip": (w(0, flip(zb)), "artifact.zip sha256 differs"),
        "one byte of a retained file": (w(1, {**ret, "out/preserve.log": flip(ret["out/preserve.log"])}),
                                        "artifact/out/preserve.log: not byte-identical"),
        "a retained file missing": (w(1, {k: v for k, v in ret.items() if k != "out/result.json"}),
                                    "artifact/out/result.json: missing"),
        "verdict fail in result.json": (member("out/result.json", lambda r: r.update(verdict="fail")), "result.json verdict"),
        "guards step skipped": (member("out/result.json", lambda r: r["steps"]["guards"].update(outcome="skipped")),
                                "step outcomes differ from all-success"),
        "a TeX difference": (member("out/result.json", lambda r: r.update(tex_files_differing=["papers/GR.tex"])),
                             "result.json tex_files_differing"),
        "a PDF-compare discrepancy in the tree report":
            (member(tree, lambda d: d["checks"][3]["discrepancies"].append("papers/GR.pdf: text differs")),
             "is not a clean pass"),
        "the guards report failing":
            (member("out/guards_check-mutants.json", lambda d: d.update(verdict="fail")),
             "report guards_check-mutants.json verdict"),
        "a CI job failed": (cirec(lambda d: run2(d)["jobs"][0].update(conclusion="failure")), "jobs not successful"),
        "a CI job missing": (cirec(lambda d: run2(d)["jobs"].pop()), "jobs, expected 41"),
        "a CI step skipped": (cirec(lambda d: run2(d)["jobs"][0]["steps"][1].update(conclusion="skipped")),
                              "non-success steps differ"),
        "dispatch 2 on another commit": (cirec(lambda d: run2(d).update(head_sha="0" * 40)), "head_sha"),
        "one byte of the CI record": (w(2, flip(ci)), "ci-record.json sha256 differs"),
        "trial PDFs not T0's": (t0edit(lambda e: e["artifact"]["members"].update({"build/papers/GR.pdf": "0" * 64})),
                                "differ from T0's retained CI-built PDFs"),
    }
    bad = 0
    for name, (args, want) in mutants.items():
        f = check(*args)
        hit = any(want in x for x in f)
        print(f"  {'ok  ' if hit else 'MISS'} mutant {name}: "
              f"{next((x for x in f if want in x), 'expected finding not reported: ' + want)}")
        bad += not hit
    print(f"self-test: {len(mutants) - bad}/{len(mutants)} mutants caught by their target check; "
          f"RESULT {'PASS' if not bad else 'FAIL'}")
    return 1 if bad else 0


def github(exp):
    f = []

    def api(path):
        q = subprocess.run(["gh", "api", f"repos/amaybaum/incompleteness/{path}"], capture_output=True, text=True)
        return json.loads(q.stdout) if q.returncode == 0 else {}
    a = exp["dispatch_1"]["artifact"]
    art = api(f"actions/artifacts/{a['id']}")
    if art.get("digest") != "sha256:" + a["sha256"]:
        f.append(f"host artifact digest {art.get('digest')!r} differs from the recorded digest")
    runs = {}
    for d in (exp["dispatch_1"], exp["dispatch_2"]):
        r = api(f"actions/runs/{d['run_id']}")
        jobs, page = [], 1
        while True:
            j = api(f"actions/runs/{d['run_id']}/jobs?per_page=100&page={page}")
            jobs += j.get("jobs", [])
            if not j.get("jobs") or len(jobs) >= j.get("total_count", 0):
                break
            page += 1
        runs[d["run_id"]] = {"run_id": r.get("id"), "path": r.get("path"), "event": r.get("event"),
                             "run_attempt": r.get("run_attempt"), "head_branch": r.get("head_branch"),
                             "head_sha": r.get("head_sha"), "conclusion": r.get("conclusion"),
                             "jobs": sorted([{"name": x["name"], "conclusion": x["conclusion"],
                                              "steps": [{"name": s["name"], "conclusion": s["conclusion"]}
                                                        for s in x["steps"]]} for x in jobs], key=lambda x: x["name"])}
    f += [f"host: {x}" for x in check_runs(runs, exp)]
    rec = json.load(open(os.path.join(HERE, exp["ci_record"]["file"])))
    for r in rec["runs"]:
        h = runs[r["run_id"]]
        strip = lambda js: [{"name": j["name"], "conclusion": j["conclusion"],
                             "steps": [{"name": s["name"], "conclusion": s["conclusion"]} for s in j["steps"]]} for j in js]
        if strip(r["jobs"]) != h["jobs"]:
            f.append(f"host: run {r['run_id']} jobs and steps differ from ci-record.json")
    return f


def trial_commit(exp):
    def git(*a):
        return subprocess.run(["git", "-C", HERE, *a], capture_output=True)
    t = exp["trial_sha"]
    if git("cat-file", "-e", t + "^{commit}").returncode:
        return [f"--trial-commit: {t[:8]} not present; fetch {exp['trial_branch']}"]
    f = []
    obj = git("cat-file", "-p", t).stdout.decode().splitlines()
    tree = [l.split()[1] for l in obj if l.startswith("tree ")]
    parents = [l.split()[1] for l in obj if l.startswith("parent ")]
    if tree != [exp["trial_tree"]]:
        f.append(f"trial commit tree {tree}, expected {exp['trial_tree']}")
    if parents != [exp["trial_parent"]]:
        f.append(f"trial commit parents {parents}, expected [{exp['trial_parent']}]")
    for path, digest in sorted(exp["trial_pdfs_sha256"].items()):
        b = git("cat-file", "blob", f"{t}:{path}").stdout
        if sha(b) != digest:
            f.append(f"trial commit {path}: sha256 differs from the recorded digest")
    if not f:
        print(f"trial commit {t[:8]}: tree, single parent and eight PDF blobs match the record")
    return f


def main(argv):
    if "--self-test" in argv:
        return self_test()
    zb, ret, ci, exp, t0 = load()
    f = check(zb, ret, ci, exp, t0)
    if "--trial-commit" in argv:
        f += trial_commit(exp)
    if "--github" in argv:
        g = github(exp)
        f += g
        if not g:
            print("host: artifact digest, both runs, and every job and step conclusion match the record")
    if "--extract" in argv:
        d = argv[argv.index("--extract") + 1]
        if f:
            f.append("--extract refused: the evidence does not match expected.json")
        else:
            z = zipfile.ZipFile(io.BytesIO(zb))
            root = os.path.realpath(d)
            names = [i.filename for i in z.infolist()]
            unsafe = [n for n in names if n.startswith("/") or ".." in n.split("/")
                      or not os.path.realpath(os.path.join(root, n)).startswith(root + os.sep)]
            if unsafe:
                f.append(f"--extract refused: unsafe member name {unsafe[0]!r}")
            else:
                for i in z.infolist():
                    p = os.path.join(root, i.filename)
                    os.makedirs(os.path.dirname(p), exist_ok=True)
                    open(p, "wb").write(z.read(i))
                print(f"extracted {len(names)} members to {d}")
    for x in f:
        print("  FAIL", x)
    print(f"T1 evidence: {len(exp['dispatch_1']['artifact']['members'])} artifact members, "
          f"{exp['dispatch_2']['jobs']} CI jobs; {len(f)} findings; RESULT {'PASS' if not f else 'FAIL'}")
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
