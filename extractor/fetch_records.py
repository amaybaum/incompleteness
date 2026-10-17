#!/usr/bin/env python3
"""Fetch the host's JSON records of KTOKEN-MAXCONE-1's two design runs, read-only, through `gh api`.

  python3 -I fetch_records.py --out DIR
  python3 -I fetch_records.py --self-test

For each of the two pinned runs it saves, into --out:
  run-<id>.json    repos/amaybaum/incompleteness/actions/runs/<id>
  jobs-<id>.json   repos/amaybaum/incompleteness/actions/runs/<id>/attempts/1/jobs?per_page=100&page=<n>, every
                   page, merged as {"total_count": N, "jobs": [...], "pages": k}

Only those JSON endpoints are called. Every path is checked against an allow-list built from the pinned run ids
before `gh` is run, so no log endpoint, no download and no redirect target is ever requested here (the logs are
fetched by download_job_logs.py). A run whose run_attempt is not 1 is refused: the pinned jobs are attempt 1's.
It prints ids, heads, counts and conclusions only. Exit 0 on success, 3 otherwise.
Python 3 stdlib; GH_TOKEN (or a gh login) supplies auth.
"""
import argparse
import json
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
REPO = "amaybaum/incompleteness"
RUN_IDS = ("39043849411", "39056982958")
_R = re.escape(REPO)
_IDS = "|".join(RUN_IDS)
ALLOWED = re.compile(
    rf"^repos/{_R}/actions/runs/(?:{_IDS})"
    rf"(?:/attempts/1/jobs\?per_page=100&page=[1-9])?\Z")
MAX_PAGES = 9
TIMEOUT_S = 120


class FetchError(Exception):
    pass


def gh_json(path, runner=None):
    if not ALLOWED.fullmatch(path):
        raise FetchError(f"refused: {path!r} is not an allowed JSON endpoint")
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github+json",
           "-H", "X-GitHub-Api-Version: 2022-11-28", path]
    p = (runner or subprocess.run)(cmd, capture_output=True, timeout=TIMEOUT_S)
    if p.returncode != 0:
        msg = p.stderr.decode("utf-8", "replace").strip().splitlines()
        raise FetchError(f"gh api {path} failed (exit {p.returncode}): {msg[-1][:200] if msg else ''}")
    return json.loads(p.stdout)


def fetch_jobs(run_id, runner=None):
    jobs, total, page = [], None, 0
    while True:
        page += 1
        if page > MAX_PAGES:
            raise FetchError(f"run {run_id}: more than {MAX_PAGES} pages")
        d = gh_json(f"repos/{REPO}/actions/runs/{run_id}/attempts/1/jobs?per_page=100&page={page}", runner)
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


def save(out, name, obj):
    with open(os.path.join(out, name), "x", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")


def fetch_all(out, runner=None):
    for rid in RUN_IDS:
        run = gh_json(f"repos/{REPO}/actions/runs/{rid}", runner)
        if str(run.get("id")) != rid:
            raise FetchError(f"run {rid}: the API answered for run {run.get('id')}")
        if int(run.get("run_attempt", 0)) != 1:
            raise FetchError(f"run {rid}: run_attempt {run.get('run_attempt')}, not 1")
        js = fetch_jobs(rid, runner)
        save(out, f"run-{rid}.json", run)
        save(out, f"jobs-{rid}.json", js)
        concl = {}
        for j in js["jobs"]:
            concl[str(j.get("conclusion"))] = concl.get(str(j.get("conclusion")), 0) + 1
        print(f"run {rid} head_sha={run.get('head_sha')} run_attempt={run.get('run_attempt')} "
              f"event={run.get('event')} conclusion={run.get('conclusion')} jobs={js['total_count']} "
              f"pages={js['pages']} conclusions={json.dumps(concl, sort_keys=True)}")


def self_test():
    """The allow-list and the refusal path, offline: no request is made."""
    r = f"repos/{REPO}/actions"
    good = [f"{r}/runs/39043849411", f"{r}/runs/39056982958",
            f"{r}/runs/39043849411/attempts/1/jobs?per_page=100&page=1",
            f"{r}/runs/39056982958/attempts/1/jobs?per_page=100&page=2"]
    bad = [f"{r}/runs/39043849412", f"{r}/runs/1", f"{r}/runs/39043849411/logs",
           f"{r}/runs/39043849411/attempts/1/logs", f"{r}/jobs/117428550018/logs", f"{r}/jobs/117428550018",
           f"{r}/runs/39043849411/attempts/2/jobs?per_page=100&page=1",
           f"{r}/runs/39043849411/attempts/1/jobs?per_page=100&page=1&x=1",
           f"{r}/runs/39043849411/attempts/1/jobs?per_page=100&page=10",
           f"{r}/runs/39043849411/artifacts", f"{r}/artifacts/1/zip", f"{r}/runs/39043849411/../../jobs/1/logs",
           f"https://api.github.com/{r}/runs/39043849411", f"{r}/runs/39043849411\n",
           "repos/amaybaum/other/actions/runs/39043849411", f"repos/{REPO}/contents/x"]
    fails = 0
    for p in good:
        ok = bool(ALLOWED.fullmatch(p))
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  allowed: {p}")
    for p in bad:
        ok = not ALLOWED.fullmatch(p)
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  refused: {p!r}")
    calls = []

    def runner(cmd, **kw):
        calls.append(cmd)
        raise AssertionError("no command may run for a refused path")
    try:
        gh_json(f"{r}/jobs/117428550018/logs", runner)
        refused = False
    except FetchError:
        refused = True
    ok = refused and not calls
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a refused path raises before any command runs")

    class P:
        def __init__(self, obj, rc=0):
            self.returncode, self.stdout, self.stderr = rc, json.dumps(obj).encode(), b"boom"

    def fake(attempt):
        def run(cmd, **kw):
            path = cmd[-1]
            if "/jobs?" in path:
                return P({"total_count": 1, "jobs": [{"id": 1, "conclusion": "success"}]})
            return P({"id": int(path.rsplit("/", 1)[1]), "run_attempt": attempt, "head_sha": "0" * 40})
        return run
    import contextlib
    import io
    import tempfile
    with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
        try:
            fetch_all(d, fake(1))
            ok = sorted(os.listdir(d)) == sorted([f"run-{x}.json" for x in RUN_IDS] + [f"jobs-{x}.json" for x in RUN_IDS])
        except FetchError:
            ok = False
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a clean fetch writes the run and job records of both runs")
    with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
        try:
            fetch_all(d, fake(2))
            ok = False
        except FetchError:
            ok = True
    fails += not ok
    print(f"  {'ok  ' if ok else 'FAIL'}  a run with run_attempt 2 is refused")
    n = len(good) + len(bad) + 3
    print(f"fetch self-test: {n - fails} of {n} cases ok")
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return 1 if self_test() else 0
    if not a.out:
        ap.error("--out is required")
    os.makedirs(a.out, exist_ok=True)
    try:
        fetch_all(a.out)
    except (FetchError, subprocess.TimeoutExpired, ValueError, KeyError) as e:
        print(f"fetch failed: {type(e).__name__}: {str(e)[:300]}")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
