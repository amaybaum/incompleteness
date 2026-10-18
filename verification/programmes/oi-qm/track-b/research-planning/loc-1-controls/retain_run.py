"""Builds retained/<F|E>/ for LOC-1 from an exact-head check run (AGENTS §A.42 items 1, 2 and 6; preregistration §12).

    check-run.json    the expected result of the run's Mathlib bridge job, in the form of the evidence-retention
                      archive's ci/<run>/results.json (schema oi-evidence-result, kind bridge), read from the served
                      job log by main's extract_result.py, loaded from ARCHIVE and checked against its blob id.
                      LOC-1 governs no Lean module (its v3-governed-paths block names its record directory and its
                      receipt), so the module table is empty, as for any round that governs none.
    jobs.json         every job of the run with its name, attempt, conclusion and steps, from the jobs API's answer.
    designation.json  the owner's designation: its text, author and time, and the host object it was posted on.

main's reproduce.py finds an expected result through an archive entry ci-<run>, which a run retained in a round's
record directory does not have, so the recipe written here is the manual one: build and gate at the commit in a
worktree, extract with extract_result.py, compare with compare_result.py EXPECTED REPRODUCED --tree DIR.

Inputs are the saved API answers and the served log text, which are working material and are not retained; their
digests are recorded.

Run:  python3 -I -B retain_run.py build --archive ARCHIVE --commit SHA --label F|E --run-json RUN.json
                                          --jobs-json JOBS.json --log LOG.txt --original-lines N
                                          --designation DESIG.json --out DIR
      python3 -I -B retain_run.py --self-test ARCHIVE
"""
import hashlib
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
EXTRACTOR = "verification/audits/evidence-retention/extract_result.py"
EXTRACTOR_BLOB = "05c41bce610b8d02ccbaca8e69377b771bef4a35"
PERMITTED = ["propext", "Classical.choice", "Quot.sound"]
RUN_FIELDS = ("conclusion", "created_at", "display_title", "event", "head_branch", "head_sha", "id", "path",
              "run_attempt", "run_number", "status", "updated_at")
JOB_FIELDS = ("completed_at", "conclusion", "head_branch", "head_sha", "id", "name", "run_attempt", "started_at",
              "status", "workflow_name")


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob_id(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def dump(obj):
    return (json.dumps(obj, indent=1, sort_keys=True) + "\n").encode("utf-8")


def load_extract(archive):
    path = os.path.join(archive, "extract_result.py")
    src = open(path, "rb").read()
    if blob_id(src) != EXTRACTOR_BLOB:
        raise SystemExit("extract_result.py at %s is not blob %s" % (path, EXTRACTOR_BLOB))
    ns = {"__name__": "extract_result"}
    exec(compile(src, path, "exec"), ns)
    return ns["extract"]


def build(archive, commit, label, run_raw, jobs_raw, log_raw, original_lines, desig, out):
    extract = load_extract(archive)
    a, jl = json.loads(run_raw), json.loads(jobs_raw)
    if a["head_sha"] != commit or a["event"] != "workflow_dispatch" or a["conclusion"] != "success":
        raise SystemExit("the run is not a green workflow_dispatch run at %s" % commit)
    jb = next((j for j in jl["jobs"] if j["name"] == "Mathlib bridge"), None)
    if jb is None or jl.get("total_count", len(jl["jobs"])) != len(jl["jobs"]):
        raise SystemExit("the jobs answer is incomplete or has no Mathlib bridge job")
    text = log_raw.decode("utf-8")
    lines = text.split("\n")
    x = extract(text)
    if not (x["build"] and x["build"]["success"]) or not x["gate"] or not x["gate"]["verdict"]:
        raise SystemExit("the served log holds no successful build or no release-gate block")
    steps = x["gate"]["steps"]
    run = {"attempt": a["run_attempt"], "conclusion": jb["conclusion"], "event": a["event"], "head_sha": commit,
           "id": str(a["id"]), "job_id": str(jb["id"]), "job_name": jb["name"], "workflow": os.path.basename(a["path"])}
    res = {"schema": "oi-evidence-result", "version": 1, "kind": "bridge", "run": run,
           "scope": "what this run logged at %s, its exact-head %s check run" % (commit[:12], label),
           "source": {"kind": "GitHub Actions job log, served text", "original_lines": original_lines,
                      "served_lines": len(lines), "served_sha256": sha(log_raw), "extractor": EXTRACTOR,
                      "extractor_blob": EXTRACTOR_BLOB,
                      "note": "the digest identifies the text this result was read from: it is provenance of the "
                              "extraction, not independent proof of the result, which reproduction at the commit "
                              "supplies; the text is not retained"},
           "expected": {"build_success": True,
                        "gate": {"steps": [{"name": s["name"], "status": s["status"], "summary": s["summary"]}
                                           for s in steps],
                                 "steps_pass": sum(1 for s in steps if s["status"] == "PASS"),
                                 "steps_total": len(steps), "verdict": x["gate"]["verdict"]["text"]},
                        "modules": {}, "markers": x["markers"], "permitted_axioms": PERMITTED},
           "observed": {"build_line": "Build completed successfully (%d jobs)." % x["build"]["jobs"],
                        "built": x["built"], "cache": x["cache"],
                        "gate_served_lines": [x["gate"]["start_line"], x["gate"]["verdict"]["served_line"]],
                        "reports_in_served_text": sum(len(v) for v in x["reports"].values())},
           "reproduce": {
               "recipe": ["run from the root of a full-history clone at a commit that carries "
                          "verification/audits/evidence-retention/ (the verifier); <dir> is a new directory and <log> "
                          "a file outside it",
                          "git worktree add --detach <dir> %s" % commit,
                          "(cd <dir>/verification/lean-mathlib && lean --version && lake exe cache get && "
                          "lake --rehash build) > <log> 2>&1",
                          "(cd <dir> && python3 tools/release_gate.py) >> <log> 2>&1",
                          "python3 -I %s <log> > reproduced.json" % EXTRACTOR,
                          "python3 -I verification/audits/evidence-retention/compare_result.py "
                          "<record>/retained/%s/check-run.json reproduced.json --tree <dir>" % label],
               "tool": None,
               "note": "reproduce.py --run %s needs an archive entry ci-%s, which a run retained in a round's record "
                       "directory does not have; the recipe is the same steps by hand" % (run["id"], run["id"]),
               "compared": "build success; the gate's steps and verdict; the markers",
               "not_compared": "timestamps, durations, cache behaviour, job counts, output order"}}
    runj = {k: a[k] for k in RUN_FIELDS if k in a}
    runj.update({"run_id": str(a["id"]), "source": "GitHub Actions runs API, GET runs/<run_id>; selected fields",
                 "source_sha256": sha(run_raw)})
    jobs = {"run_id": str(a["id"]), "source": "GitHub Actions jobs API, GET runs/<run_id>/jobs?filter=all; selected "
            "fields", "source_sha256": sha(jobs_raw), "run": runj,
            "jobs": [dict({k: j[k] for k in JOB_FIELDS if k in j},
                          steps=[{"number": s["number"], "name": s["name"], "conclusion": s["conclusion"]}
                                 for s in j.get("steps", [])]) for j in sorted(jl["jobs"], key=lambda j: j["id"])]}
    des = dict(desig)
    des.update({"subject": label, "commit": commit})
    os.makedirs(out, exist_ok=True)
    made = []
    for name, obj in (("check-run.json", res), ("jobs.json", jobs), ("designation.json", des)):
        b = dump(obj)
        open(os.path.join(out, name), "wb").write(b)
        made.append((name, len(b), sha(b)))
    return made


# ------------------------------------------------------------------- self-test on a synthetic run

def synthetic(commit):
    ts = "2026-01-01T00:00:%02d.0000000Z "
    body = ["Run lake --rehash build", "Build completed successfully (3597 jobs).", "release gate",
            "  PASS  toolchain       toolchain_check: OK", "  PASS  v3-receipts     v3_verifier --receipts: OK",
            "release gate: PASS  (synthetic)"]
    log = "\n".join(ts % (i % 60) + l for i, l in enumerate(body)).encode("utf-8")
    run = {"id": 1, "head_sha": commit, "event": "workflow_dispatch", "conclusion": "success", "run_attempt": 1,
           "path": ".github/workflows/verify.yml", "status": "completed", "created_at": "2026-01-01T00:00:00Z",
           "updated_at": "2026-01-01T00:10:00Z", "display_title": "synthetic", "head_branch": "draft/x",
           "run_number": 1}
    jobs = {"total_count": 2, "jobs": [
        {"id": 11, "name": "Lean kernel check", "run_attempt": 1, "conclusion": "success", "head_sha": commit,
         "status": "completed", "head_branch": "draft/x", "workflow_name": "verify", "started_at": "x",
         "completed_at": "y", "steps": [{"number": 1, "name": "s", "conclusion": "success"}]},
        {"id": 12, "name": "Mathlib bridge", "run_attempt": 1, "conclusion": "success", "head_sha": commit,
         "status": "completed", "head_branch": "draft/x", "workflow_name": "verify", "started_at": "x",
         "completed_at": "y", "steps": [{"number": 1, "name": "s", "conclusion": "success"}]}]}
    des = {"text": "F designated: %s" % commit, "author": "owner", "time": "2026-01-01T00:20:00Z",
           "host_object": "issue comment (synthetic)"}
    return log, dump(run), dump(jobs), des


def self_test(archive):
    lines, ok = [], True

    def rep(name, passed, detail=""):
        nonlocal ok
        ok &= bool(passed)
        lines.append("%s %-64s %s" % ("PASS" if passed else "FAIL", name, detail))

    sys.path.insert(0, HERE)
    import controls
    commit = "c" * 40
    log, run, jobs, des = synthetic(commit)
    with tempfile.TemporaryDirectory() as t:
        out = os.path.join(t, "retained", "F")
        made = build(archive, commit, "F", run, jobs, log, len(log.split(b"\n")), des, out)
        rep("built retained/F/ from a synthetic exact-head run with main's extractor", len(made) == 3,
            ", ".join("%s %d B" % (n, b) for n, b, _ in made))
        f = controls.check_ret(out, commit, "F")
        rep("K-ret-F accepts it", not f, "; ".join(f[:2]))
        # main's comparator on the expected result against the extraction of the same text
        ex = load_extract(archive)
        rp = os.path.join(t, "reproduced.json")
        open(rp, "w").write(json.dumps(ex(log.decode("utf-8"))))
        os.makedirs(os.path.join(t, "tree"))
        r = subprocess.run([sys.executable, "-I", os.path.join(archive, "compare_result.py"),
                            os.path.join(out, "check-run.json"), rp, "--tree", os.path.join(t, "tree")],
                           capture_output=True, text=True)
        rep("main's compare_result.py accepts check-run.json against its own extraction", r.returncode == 0,
            (r.stdout.strip().split("\n") or [""])[-1][:90])
        bad = log.replace(b"  PASS  v3-receipts", b"  FAIL  v3-receipts")
        open(rp, "w").write(json.dumps(ex(bad.decode("utf-8"))))
        r = subprocess.run([sys.executable, "-I", os.path.join(archive, "compare_result.py"),
                            os.path.join(out, "check-run.json"), rp, "--tree", os.path.join(t, "tree")],
                           capture_output=True, text=True)
        rep("NEG main's compare_result.py refuses a reproduction with a failed gate step", r.returncode != 0)
        try:
            build(archive, commit, "F", run.replace(b"workflow_dispatch", b"pull_request"), jobs, log, 6, des,
                  os.path.join(t, "x"))
            rep("NEG a pull-request run is refused", False)
        except SystemExit:
            rep("NEG a pull-request run is refused", True)
    lines.append("retain_run self-test: %s" % ("ALL PASS" if ok else "FAILURE"))
    return ok, lines


def main(argv):
    if argv[:1] == ["--self-test"] and len(argv) == 2:
        ok, lines = self_test(argv[1])
        print("\n".join(lines))
        return 0 if ok else 1
    if argv[:1] == ["build"]:
        o = dict(zip(argv[1::2], argv[2::2]))
        made = build(o["--archive"], o["--commit"], o["--label"], open(o["--run-json"], "rb").read(),
                     open(o["--jobs-json"], "rb").read(), open(o["--log"], "rb").read(), int(o["--original-lines"]),
                     json.load(open(o["--designation"])), o["--out"])
        for n, b, h in made:
            print("%s %d %s" % (n, b, h))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
