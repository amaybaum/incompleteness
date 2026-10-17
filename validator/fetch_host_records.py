#!/usr/bin/env python3
"""Fetch the host's own JSON records for a log-archive batch, read-only, through `gh api`.

For every run in batch.json it saves, into --out:
  run-<id>.json                  repos/<repo>/actions/runs/<id>
  run-<id>-attempt-<n>.json      repos/<repo>/actions/runs/<id>/attempts/<n>       (n = 1 .. run_attempt)
  jobs-<id>-attempt-<n>.json     repos/<repo>/actions/runs/<id>/attempts/<n>/jobs?per_page=100, every page,
                                 merged as {"total_count": N, "jobs": [...], "pages": k}
and, with --artifact-id, artifact-<id>.json (repos/<repo>/actions/artifacts/<id>).

It calls JSON endpoints only. Every path is checked against an allow-list before `gh` is run, so no log endpoint,
no artifact download and no redirect target is ever requested. It prints counts, ids and heads only.
Python 3.12 stdlib; run as `python3 -I fetch_host_records.py ...`. GH_TOKEN (or a gh login) supplies auth.
"""
import argparse
import json
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
ALLOWED = re.compile(
    r"^repos/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/actions/("
    r"runs/\d+"
    r"|runs/\d+/attempts/\d+"
    r"|runs/\d+/attempts/\d+/jobs\?per_page=100&page=\d+"
    r"|artifacts/\d+"
    r")\Z")
MAX_PAGES = 20


def gh_json(path):
    if not ALLOWED.fullmatch(path):
        raise SystemExit(f"refused: {path!r} is not an allowed JSON endpoint")
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github+json",
           "-H", "X-GitHub-Api-Version: 2022-11-28", path]
    p = subprocess.run(cmd, capture_output=True, timeout=120)
    if p.returncode != 0:
        msg = p.stderr.decode("utf-8", "replace").strip().splitlines()
        raise SystemExit(f"gh api {path} failed (exit {p.returncode}): {msg[-1] if msg else ''}")
    return json.loads(p.stdout)


def save(out, name, obj):
    path = os.path.join(out, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")
    return path


def fetch_jobs(repo, run_id, attempt):
    jobs, total, page = [], None, 0
    while True:
        page += 1
        if page > MAX_PAGES:
            raise SystemExit(f"run {run_id} attempt {attempt}: more than {MAX_PAGES} pages")
        d = gh_json(f"repos/{repo}/actions/runs/{run_id}/attempts/{attempt}/jobs?per_page=100&page={page}")
        if total is None:
            total = d["total_count"]
        elif d["total_count"] != total:
            raise SystemExit(f"run {run_id} attempt {attempt}: total_count changed between pages")
        jobs.extend(d["jobs"])
        if not d["jobs"] or len(jobs) >= total:
            break
    if len(jobs) != total or len({j["id"] for j in jobs}) != len(jobs):
        raise SystemExit(f"run {run_id} attempt {attempt}: {len(jobs)} jobs (unique "
                         f"{len({j['id'] for j in jobs})}) vs total_count {total}")
    return {"total_count": total, "jobs": jobs, "pages": page}


def self_test():
    """The allow-list, offline: JSON endpoints pass; logs, downloads and anything else are refused."""
    r = "repos/amaybaum/incompleteness/actions"
    good = [f"{r}/runs/1", f"{r}/runs/1/attempts/2", f"{r}/runs/1/attempts/2/jobs?per_page=100&page=3",
            f"{r}/artifacts/12090461970"]
    bad = [f"{r}/runs/1/logs", f"{r}/runs/1/attempts/2/logs", f"{r}/jobs/5/logs", f"{r}/artifacts/1/zip",
           f"{r}/runs/1/artifacts", f"{r}/runs/1/rerun", f"https://api.github.com/{r}/runs/1", f"{r}/runs/1/../logs",
           f"{r}/runs/1/attempts/2/jobs?per_page=100&page=3&x=1", f"{r}/runs/1\n", "repos/a/b/contents/x"]
    fails = 0
    for p in good:
        ok = bool(ALLOWED.fullmatch(p))
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  allowed: {p}")
    for p in bad:
        ok = not ALLOWED.fullmatch(p)
        fails += not ok
        print(f"  {'ok  ' if ok else 'FAIL'}  refused: {p!r}")
    print(f"helper self-test: {len(good) + len(bad) - fails} of {len(good) + len(bad)} cases ok")
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo")
    ap.add_argument("--batch")
    ap.add_argument("--out")
    ap.add_argument("--artifact-id")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return 1 if self_test() else 0
    if not (a.repo and a.batch and a.out):
        ap.error("--repo, --batch and --out are required")
    os.makedirs(a.out, exist_ok=True)
    with open(a.batch, encoding="utf-8") as f:
        run_ids = [str(r) for r in json.load(f)["run_ids"]]
    if a.artifact_id:
        meta = gh_json(f"repos/{a.repo}/actions/artifacts/{a.artifact_id}")
        save(a.out, f"artifact-{a.artifact_id}.json", meta)
        print(f"artifact {meta['id']} name={meta['name']} size_in_bytes={meta['size_in_bytes']} "
              f"digest={meta.get('digest')} expired={meta['expired']} created_at={meta['created_at']} "
              f"expires_at={meta['expires_at']} run={meta['workflow_run']['id']}")
    for rid in run_ids:
        run = gh_json(f"repos/{a.repo}/actions/runs/{rid}")
        save(a.out, f"run-{rid}.json", run)
        n = int(run["run_attempt"])
        print(f"run {rid} head_sha={run['head_sha']} run_attempt={n} status={run['status']} "
              f"conclusion={run['conclusion']} event={run['event']}")
        for k in range(1, n + 1):
            att = gh_json(f"repos/{a.repo}/actions/runs/{rid}/attempts/{k}")
            save(a.out, f"run-{rid}-attempt-{k}.json", att)
            js = fetch_jobs(a.repo, rid, k)
            save(a.out, f"jobs-{rid}-attempt-{k}.json", js)
            concl = {}
            for j in js["jobs"]:
                concl[str(j.get("conclusion"))] = concl.get(str(j.get("conclusion")), 0) + 1
            heads = sorted({j.get("head_sha") for j in js["jobs"]})
            print(f"  attempt {k}: head_sha={att['head_sha']} jobs={js['total_count']} pages={js['pages']} "
                  f"conclusions={json.dumps(concl, sort_keys=True)} job_heads={heads}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
