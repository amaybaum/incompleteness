#!/usr/bin/env python3
"""Fetch the host's JSON records of the runs listed in extractor/targets.json, read-only, through `gh api`.

  python3 -I fetch_records.py --out DIR
  python3 -I fetch_records.py --self-test

For each target (run id R, bridge job J) it saves, into --out:
  run-R.json    repos/amaybaum/incompleteness/actions/runs/R, the API answer's bytes as gh printed them
  job-J.json    repos/amaybaum/incompleteness/actions/jobs/J, the API answer's bytes as gh printed them
  jobs-R.json   repos/amaybaum/incompleteness/actions/runs/R/attempts/1/jobs?per_page=100&page=<n>, every page,
                merged as {"total_count": N, "jobs": [...], "pages": k}
and, for a target with a cells block (probe job P):
  job-P.json    repos/amaybaum/incompleteness/actions/jobs/P, the API answer's bytes as gh printed them

Only those JSON endpoints are called. Every path is checked against an allow-list built from the targets' run and
job ids before `gh` is run, so no log endpoint, no download and no redirect target is ever requested here (the logs
are fetched by download_job_logs.py). A run whose run_attempt is not 1 is refused: the targets are attempt 1's.
It prints ids, heads, counts and conclusions only. Exit 0 on success, 3 otherwise.
Python 3 stdlib; GH_TOKEN (or a gh login) supplies auth.
"""
import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
HERE = os.path.dirname(os.path.abspath(__file__))


def _load_targets_module():
    spec = importlib.util.spec_from_file_location("ktoken_targets", os.path.join(HERE, "targets.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T = _load_targets_module()
REPO = T.REPO
MAX_PAGES = 9
TIMEOUT_S = 120


class FetchError(Exception):
    pass


def allow_list(targets):
    _R = re.escape(REPO)
    runs = "|".join(re.escape(t["run_id"]) for t in targets)
    jobs = "|".join(re.escape(j) for j in all_jobs(targets))
    return re.compile(rf"^repos/{_R}/actions/(?:runs/(?:{runs})(?:/attempts/1/jobs\?per_page=100&page=[1-9])?"
                      rf"|jobs/(?:{jobs}))\Z")


def all_jobs(targets):
    """Every listed job id: each target's bridge job, then its probe job when it has a cells block."""
    return [j for t in targets for j in [t["bridge_job"]] + ([t["cells"]["probe_job"]] if t.get("cells") else [])]


def gh_raw(path, allowed, runner=None):
    if not allowed.fullmatch(path):
        raise FetchError(f"refused: {path!r} is not an allowed JSON endpoint")
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github+json",
           "-H", "X-GitHub-Api-Version: 2022-11-28", path]
    p = (runner or subprocess.run)(cmd, capture_output=True, timeout=TIMEOUT_S)
    if p.returncode != 0:
        msg = p.stderr.decode("utf-8", "replace").strip().splitlines()
        raise FetchError(f"gh api {path} failed (exit {p.returncode}): {msg[-1][:200] if msg else ''}")
    return p.stdout


def gh_json(path, allowed, runner=None):
    return json.loads(gh_raw(path, allowed, runner))


def fetch_jobs(run_id, allowed, runner=None):
    jobs, total, page = [], None, 0
    while True:
        page += 1
        if page > MAX_PAGES:
            raise FetchError(f"run {run_id}: more than {MAX_PAGES} pages")
        d = gh_json(f"repos/{REPO}/actions/runs/{run_id}/attempts/1/jobs?per_page=100&page={page}", allowed, runner)
        if total is None:
            total = d["total_count"]
        elif d["total_count"] != total:
            raise FetchError(f"run {run_id}: total_count changed between pages")
        jobs.extend(d["jobs"])
        if not d["jobs"] or len(jobs) >= total:
            break
    if len(jobs) != total or len({j["id"] for j in jobs}) != len(jobs):
        raise FetchError(f"run {run_id}: {len(jobs)} jobs vs total_count {total}")
    return {"total_count": total, "jobs": jobs, "pages": page}


def save_bytes(out, name, data):
    with open(os.path.join(out, name), "xb") as f:
        f.write(data)


def save(out, name, obj):
    with open(os.path.join(out, name), "x", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")


def fetch_all(out, targets, runner=None):
    allowed = allow_list(targets)
    for t in targets:
        rid, jid = t["run_id"], t["bridge_job"]
        raw = gh_raw(f"repos/{REPO}/actions/runs/{rid}", allowed, runner)
        run = json.loads(raw)
        if str(run.get("id")) != rid:
            raise FetchError(f"run {rid}: the API answered for run {run.get('id')}")
        if int(run.get("run_attempt", 0)) != 1:
            raise FetchError(f"run {rid}: run_attempt {run.get('run_attempt')}, not 1")
        js = fetch_jobs(rid, allowed, runner)
        answers = {}
        for j in [jid] + ([t["cells"]["probe_job"]] if t.get("cells") else []):
            jraw = gh_raw(f"repos/{REPO}/actions/jobs/{j}", allowed, runner)
            if str(json.loads(jraw).get("id")) != j:
                raise FetchError(f"job {j}: the API answered for job {json.loads(jraw).get('id')}")
            answers[j] = jraw
        job = json.loads(answers[jid])
        save_bytes(out, f"run-{rid}.json", raw)
        save(out, f"jobs-{rid}.json", js)
        for j, jraw in answers.items():
            save_bytes(out, f"job-{j}.json", jraw)
        concl = {}
        for j in js["jobs"]:
            concl[str(j.get("conclusion"))] = concl.get(str(j.get("conclusion")), 0) + 1
        print(f"target {t['label']} run {rid} head_sha={run.get('head_sha')} run_attempt={run.get('run_attempt')} "
              f"event={run.get('event')} conclusion={run.get('conclusion')} jobs={js['total_count']} "
              f"pages={js['pages']} conclusions={json.dumps(concl, sort_keys=True)} "
              f"bridge_job={jid} name={job.get('name')!r} job_conclusion={job.get('conclusion')}"
              + "".join(f" probe_job={j} name={json.loads(a).get('name')!r} job_conclusion={json.loads(a).get('conclusion')}"
                        for j, a in answers.items() if j != jid))


def self_test():
    """The allow-list and the refusal path, offline: no request is made."""
    r = f"repos/{REPO}/actions"
    targets = T.load()["targets"]
    allowed = allow_list(targets)
    rid, jid = targets[0]["run_id"], targets[0]["bridge_job"]
    good = [f"{r}/runs/{rid}", f"{r}/runs/{rid}/attempts/1/jobs?per_page=100&page=1",
            f"{r}/runs/{rid}/attempts/1/jobs?per_page=100&page=2", f"{r}/jobs/{jid}"]
    bad = [f"{r}/runs/{int(rid) + 1}", f"{r}/runs/1", f"{r}/runs/{rid}/logs", f"{r}/runs/{rid}/attempts/1/logs",
           f"{r}/jobs/{jid}/logs", f"{r}/jobs/{int(jid) + 1}", f"{r}/jobs/{rid}", f"{r}/runs/{jid}",
           f"{r}/runs/{rid}/attempts/2/jobs?per_page=100&page=1",
           f"{r}/runs/{rid}/attempts/1/jobs?per_page=100&page=1&x=1",
           f"{r}/runs/{rid}/attempts/1/jobs?per_page=100&page=10",
           f"{r}/runs/{rid}/artifacts", f"{r}/artifacts/1/zip", f"{r}/runs/{rid}/../../jobs/1/logs",
           f"https://api.github.com/{r}/runs/{rid}", f"{r}/runs/{rid}\n", f"{r}/jobs/{jid}?x=1",
           f"repos/amaybaum/other/actions/runs/{rid}", f"repos/{REPO}/contents/x",
           # the two design runs of the earlier extraction are not targets here
           f"{r}/runs/39043849411", f"{r}/runs/39056982958", f"{r}/jobs/117428550018"]
    fails = 0
    for p in good:
        ok = bool(allowed.fullmatch(p))
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  allowed: {p}")
    for p in bad:
        ok = not allowed.fullmatch(p)
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  refused: {p!r}")
    targets = [t for t in targets if t["label"] == "F"]   # the cases below are written against F alone
    allowed = allow_list(targets)
    two = targets + [{"label": "E", "kind": "bridge", "run_id": "39999999999", "commit": "a" * 40,
                      "bridge_job": "118000000001", "path": "evidence/e-run/results.json"}]
    a2 = allow_list(two)
    ok = bool(a2.fullmatch(f"{r}/runs/39999999999")) and bool(a2.fullmatch(f"{r}/jobs/118000000001")) \
        and not a2.fullmatch(f"{r}/jobs/118000000001/logs") and not allowed.fullmatch(f"{r}/runs/39999999999")
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a second target widens the allow-list by exactly its run and job")
    three = targets + [dict(two[-1], cells={"probe_job": "118000000002", "path": "evidence/e-run/cells.json"})]
    a3 = allow_list(three)
    ok = bool(a3.fullmatch(f"{r}/jobs/118000000002")) and not a3.fullmatch(f"{r}/jobs/118000000002/logs") \
        and not a3.fullmatch(f"{r}/jobs/118000000003") and not a2.fullmatch(f"{r}/jobs/118000000002") \
        and all_jobs(three) == [jid, "118000000001", "118000000002"]
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a cells block widens the allow-list by exactly its probe job's JSON endpoint")
    real = T.load()["targets"]
    ok = all(allow_list(real).fullmatch(f"{r}/jobs/{j}") for j in all_jobs(real)) \
        and len(set(all_jobs(real))) == len(all_jobs(real))
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  the committed targets' jobs ({', '.join(all_jobs(real))}) are each allowed, once")
    calls = []

    def runner(cmd, **kw):
        calls.append(cmd)
        raise AssertionError("no command may run for a refused path")
    try:
        gh_json(f"{r}/jobs/{jid}/logs", allowed, runner)
        refused = False
    except FetchError:
        refused = True
    ok = refused and not calls
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a refused path raises before any command runs")

    class P:
        def __init__(self, obj, rc=0):
            self.returncode, self.stdout, self.stderr = rc, json.dumps(obj).encode(), b"boom"

    def fake(attempt, job_id=None):
        def run(cmd, **kw):
            path = cmd[-1]
            if "/jobs?" in path:
                return P({"total_count": 1, "jobs": [{"id": 1, "conclusion": "success"}]})
            if "/jobs/" in path:
                return P({"id": int(job_id or path.rsplit("/", 1)[1]), "name": "Mathlib bridge", "conclusion": "success"})
            return P({"id": int(path.rsplit("/", 1)[1]), "run_attempt": attempt, "head_sha": "0" * 40})
        return run
    import contextlib
    import io
    import tempfile
    want = sorted([f"run-{t['run_id']}.json" for t in targets] + [f"jobs-{t['run_id']}.json" for t in targets]
                  + [f"job-{t['bridge_job']}.json" for t in targets])
    with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
        try:
            fetch_all(d, targets, fake(1))
            ok = sorted(os.listdir(d)) == want
            with open(os.path.join(d, f"run-{rid}.json"), "rb") as f:
                ok = ok and f.read() == json.dumps({"id": int(rid), "run_attempt": 1, "head_sha": "0" * 40}).encode()
        except FetchError:
            ok = False
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a clean fetch writes exactly the run, job and jobs-list records of the "
          f"listed runs, the run record byte for byte")
    with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
        try:
            fetch_all(d, three, fake(1))
            ok = sorted(os.listdir(d)) == sorted(want + ["run-39999999999.json", "jobs-39999999999.json",
                                                        "job-118000000001.json", "job-118000000002.json"])
        except FetchError:
            ok = False
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a cells target's fetch adds exactly its probe job's record")
    for name, fk in (("a run with run_attempt 2 is refused", fake(2)),
                     ("a job answer for another job id is refused", fake(1, job_id="1"))):
        with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
            try:
                fetch_all(d, targets, fk)
                ok = False
            except FetchError:
                ok = True
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  {name}")
    n = len(good) + len(bad) + 8
    print(f"fetch self-test: {n - fails} of {n} cases ok")
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    try:
        targets = T.load()["targets"]
    except T.TargetsError as e:
        print(f"fetch refused: {e}")
        return 3
    if a.self_test:
        return 1 if self_test() else 0
    if not a.out:
        ap.error("--out is required")
    os.makedirs(a.out, exist_ok=True)
    try:
        fetch_all(a.out, targets)
    except (FetchError, subprocess.TimeoutExpired, ValueError, KeyError) as e:
        print(f"fetch failed: {type(e).__name__}: {str(e)[:300]}")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
