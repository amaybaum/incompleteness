#!/usr/bin/env python3
"""Read one shard's host records and bridge-job logs, read-only, for the CI batch extraction.

  python3 -I host.py --runs batchx/runs.json --shard K --out DIR
  python3 -I host.py --self-test [--work DIR]

The run set is batchx/runs.json, whose sha256 must equal RUNS_SHA256 before anything is requested. For each run of
shard K, in the file's order, it saves into DIR:
  run-<id>.json    GET repos/amaybaum/incompleteness/actions/runs/<id>/attempts/1  (the run as of attempt 1)
  jobs-<id>.json   GET .../actions/runs/<id>/attempts/1/jobs?per_page=100&page=<n>, every page, merged as
                   {"total_count": N, "jobs": [...], "pages": k}
  logs/<job>.log   the pinned bridge job's log: GET .../actions/jobs/<job>/logs, then its redirect target
and one record, DIR/fetch-record.json, holding for every run of the shard the outcome of each of the three reads.
The record is written before the first read, every read pre-filled as "not-reached", and replaced atomically after
each read (a log's entry reads "started" while it downloads), so a step stopped by its timeout keeps every completed
read on disk and names every other one; the assembler reads a read that is not "ok" as UNVERIFIED.

Adapted from extractor/download_job_logs.py and extractor/fetch_records.py of tmp/ktoken-evidence-20261017 at
0d94937d. Every URL is checked before anything is sent: it must be one of the endpoints built from the shard's
pinned run and job ids (scheme, host and path exactly; for the jobs list only the page number varies), or the
request is refused and the token is never used. The token goes only to api.github.com, as `Authorization: Bearer`.
No redirect is followed for a JSON endpoint. A log endpoint must answer with a redirect; its target is fetched
without an Authorization header, must be https without user info, and must answer 200 itself. The body is read
under a size cap, checked against Content-Length, under a read timeout and an overall deadline, and written to a
new file while it is hashed. The redirect target is never printed, logged or recorded, nor its path or query; a
failure records only the stage, the exception type, the HTTP status when there is one, and the host.

Rate limit. Every API answer's X-RateLimit-Remaining is read. Once it is below RESERVE no further request is
sent: each read not made is recorded with stage "rate-limit-reserve", so the run is named as unread, never
dropped. GET /rate_limit, which does not count against the limit, is read once at the start and printed as a
number only.

It prints ids, counts, outcomes, byte lengths, line counts and digests only. Exit 0 when every read succeeded,
3 otherwise; the assembler names each unread run. Python 3 stdlib.
"""
import argparse
import contextlib
import hashlib
import http.server
import io
import json
import os
import re
import shutil
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
REPO = "amaybaum/incompleteness"
RUNS_SHA256 = "5436c5b6325e5efca8b9d9a737ba832b6556ae9ffc15524b33774f701f672edb"
API_BASE = "https://api.github.com"
TOKEN_HOST = "api.github.com"
FIXED_CAP = 64 * 1024 * 1024
TIMEOUT_S = 60.0
DEADLINE_S = 240.0
CHUNK = 64 * 1024
MAX_PAGES = 3
RESERVE = 150
UA = "ci-batch-extract/1 (read-only)"


class Refused(Exception):
    """A policy refusal; the class name is the reason."""


class RefusedEndpoint(Refused): pass
class RefusedScheme(Refused): pass
class RefusedNoToken(Refused): pass
class RefusedNoRedirect(Refused): pass
class RefusedRedirect(Refused): pass
class RefusedLocation(Refused): pass
class RefusedStatus(Refused): pass
class RefusedTooLarge(Refused): pass
class RefusedLengthMismatch(Refused): pass
class RefusedExists(Refused): pass
class RefusedReserve(Refused): pass
class DeadlineExceeded(Refused): pass


def load_runs(path, expect_sha=RUNS_SHA256):
    with open(path, "rb") as f:
        data = f.read()
    got = hashlib.sha256(data).hexdigest()
    if got != expect_sha:
        raise Refused("runs file sha256 %s is not the pinned %s" % (got, expect_sha))
    doc = json.loads(data)
    runs = doc["runs"]
    ids = [r["run_id"] for r in runs]
    jobs = [r["bridge_job_id"] for r in runs]
    if len(set(ids)) != len(ids) or len(set(jobs)) != len(jobs):
        raise Refused("runs file repeats a run or a job")
    for r in runs:
        if not (re.fullmatch(r"[1-9][0-9]{0,19}", r["run_id"]) and re.fullmatch(r"[1-9][0-9]{0,19}", r["bridge_job_id"])
                and re.fullmatch(r"[0-9a-f]{40}", r["head_sha"]) and isinstance(r["shard"], int)):
            raise Refused("runs file entry %r is malformed" % r.get("run_id"))
    return doc


class Transport:
    """Production transport. Only the self-test builds a different one."""
    def __init__(self, runs, api_base=API_BASE, token_host=TOKEN_HOST, allow_http_api=False, allow_http_link=False,
                 proxies=None, timeout=TIMEOUT_S, deadline=DEADLINE_S, cap=FIXED_CAP, reserve=RESERVE):
        self.api_base, self.token_host = api_base, token_host
        self.allow_http_api, self.allow_http_link = allow_http_api, allow_http_link
        self.proxies, self.timeout, self.deadline, self.cap, self.reserve = proxies, timeout, deadline, cap, reserve
        r = re.escape(REPO)
        ids = "|".join(re.escape(x["run_id"]) for x in runs) or "(?!)"
        self.json_rx = re.compile(r"^/repos/%s/actions/runs/(?:%s)/attempts/1(?:/jobs\?per_page=100&page=[1-%d])?\Z"
                                  % (r, ids, MAX_PAGES))
        self.log_paths = frozenset("/repos/%s/actions/jobs/%s/logs" % (REPO, x["bridge_job_id"]) for x in runs)
        self.rate_path = "/rate_limit"
        self.remaining = None   # the last X-RateLimit-Remaining seen


def _opener(t):
    # No redirect handler at all: a 3xx reaches HTTPDefaultErrorHandler and is raised, never followed.
    op = urllib.request.OpenerDirector()
    for h in (urllib.request.ProxyHandler(t.proxies), urllib.request.UnknownHandler(),
              urllib.request.HTTPHandler(), urllib.request.HTTPSHandler(),
              urllib.request.HTTPDefaultErrorHandler(), urllib.request.HTTPErrorProcessor()):
        op.add_handler(h)
    return op


def check_url(url, t, kind):
    """kind: 'json', 'log' or 'rate'. The full URL must be an allowed endpoint of that kind, or RefusedEndpoint."""
    u = urllib.parse.urlsplit(url)
    base = urllib.parse.urlsplit(t.api_base)
    ok_scheme = u.scheme == "https" or (t.allow_http_api and u.scheme == "http")
    if not ok_scheme or u.scheme != base.scheme or u.netloc != base.netloc or u.hostname != t.token_host:
        raise RefusedEndpoint()
    if u.username is not None or u.password is not None or u.fragment or "%" in url or "\n" in url or " " in url:
        raise RefusedEndpoint()
    pq = u.path + ("?" + u.query if u.query else "")
    if kind == "json" and t.json_rx.fullmatch(pq):
        return u
    if kind == "log" and not u.query and u.path in t.log_paths:
        return u
    if kind == "rate" and not u.query and u.path == t.rate_path:
        return u
    raise RefusedEndpoint()


def _note_rate(t, headers):
    v = headers.get("X-RateLimit-Remaining") if headers is not None else None
    if v is not None and str(v).strip().isdigit():
        t.remaining = int(v)


def _api_request(url, token, t):
    if not token:
        raise RefusedNoToken()
    return urllib.request.Request(url, method="GET", headers={
        "User-Agent": UA, "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": "Bearer %s" % token})


def get_json(path, token, t, kind="json"):
    """One JSON GET at an allowed endpoint, no redirect followed. Returns (obj, record)."""
    url = t.api_base + path
    rec = {"outcome": "failed", "stage": "endpoint", "error_type": None, "http_status": None}
    try:
        check_url(url, t, kind)
        if kind != "rate" and t.remaining is not None and t.remaining < t.reserve:
            rec["stage"] = "rate-limit-reserve"
            raise RefusedReserve()
        rec["stage"] = "api"
        req = _api_request(url, token, t)
        try:
            resp = _opener(t).open(req, timeout=t.timeout)
        except urllib.error.HTTPError as e:
            rec["http_status"] = e.code
            if kind != "rate":
                _note_rate(t, e.headers)
            e.close()
            raise RefusedRedirect() if 300 <= e.code < 400 else RefusedStatus()
        with resp:
            if kind != "rate":
                _note_rate(t, resp.headers)
            rec["http_status"] = resp.status
            if resp.status != 200:
                raise RefusedStatus()
            data = resp.read(16 * 1024 * 1024 + 1)
            if len(data) > 16 * 1024 * 1024:
                raise RefusedTooLarge()
        obj = json.loads(data)
        rec.update(outcome="ok", stage="done")
        return obj, rec
    except BaseException as e:  # noqa: BLE001 - only the type name is kept
        if isinstance(e, KeyboardInterrupt):
            raise
        rec["error_type"] = type(e).__name__
        return None, rec


def download_log(job_id, token, out_path, t):
    """The two-step log download. The record never contains the redirect target, its path or its query."""
    url = "%s/repos/%s/actions/jobs/%s/logs" % (t.api_base, REPO, job_id)
    rec = {"job_id": str(job_id), "outcome": "failed", "stage": "endpoint", "error_type": None, "http_status": None,
           "error_host": urllib.parse.urlsplit(url).hostname, "storage_host": None, "bytes": None, "sha256": None,
           "lines": None, "size_cap": t.cap}
    wrote = False
    try:
        u = check_url(url, t, "log")
        if t.remaining is not None and t.remaining < t.reserve:
            rec["stage"] = "rate-limit-reserve"
            raise RefusedReserve()
        if os.path.lexists(out_path):
            raise RefusedExists()
        op = _opener(t)
        start = time.monotonic()
        rec["stage"] = "api"
        req = _api_request(url, token, t)
        loc = None
        try:
            resp = op.open(req, timeout=t.timeout)
        except urllib.error.HTTPError as e:
            code, loc = e.code, e.headers.get("Location")
            rec["http_status"] = code
            _note_rate(t, e.headers)
            e.close()
            if code not in (301, 302, 303, 307, 308):
                raise RefusedStatus()
        else:
            _note_rate(t, resp.headers)
            rec["http_status"] = resp.status
            resp.close()
            raise RefusedNoRedirect()
        if not loc:
            raise RefusedLocation()
        v = urllib.parse.urlsplit(loc)
        rec["stage"], rec["error_host"], rec["http_status"] = "storage", v.hostname, None
        if not (v.scheme == "https" or (t.allow_http_link and v.scheme == "http")):
            raise RefusedScheme()
        if not v.hostname or v.username is not None or v.password is not None:
            raise RefusedLocation()
        rec["storage_host"] = v.hostname
        req2 = urllib.request.Request(loc, method="GET", headers={"User-Agent": UA})
        try:
            resp = op.open(req2, timeout=t.timeout)
        except urllib.error.HTTPError as e:
            rec["http_status"] = e.code
            e.close()
            raise RefusedRedirect() if 300 <= e.code < 400 else RefusedStatus()
        h = hashlib.sha256()
        total, nl, last = 0, 0, b""
        with resp:
            rec["http_status"] = resp.status
            if resp.status != 200:
                raise RefusedStatus()
            clen = resp.headers.get("Content-Length")
            if clen is not None:
                if not clen.strip().isdigit():
                    raise RefusedLengthMismatch()
                if int(clen) > t.cap:
                    raise RefusedTooLarge()
            with open(out_path, "xb") as f:
                wrote = True
                while True:
                    if time.monotonic() - start > t.deadline:
                        raise DeadlineExceeded()
                    chunk = resp.read1(min(CHUNK, t.cap + 1 - total))
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > t.cap:
                        raise RefusedTooLarge()
                    h.update(chunk)
                    nl += chunk.count(b"\n")
                    last = chunk[-1:]
                    f.write(chunk)
            if clen is not None and int(clen) != total:
                raise RefusedLengthMismatch()
        rec.update(outcome="ok", stage="done", error_type=None, error_host=None, bytes=total, sha256=h.hexdigest(),
                   lines=nl + (1 if total and last != b"\n" else 0))
    except BaseException as e:  # noqa: BLE001 - only the type name is kept
        if isinstance(e, KeyboardInterrupt):
            raise
        rec["error_type"] = type(e).__name__
        if wrote:
            with contextlib.suppress(OSError):
                os.unlink(out_path)
    return rec


def fetch_jobs(rid, token, t):
    jobs, total, recs = [], None, []
    for page in range(1, MAX_PAGES + 1):
        d, rec = get_json("/repos/%s/actions/runs/%s/attempts/1/jobs?per_page=100&page=%d" % (REPO, rid, page),
                          token, t)
        recs.append(rec)
        if d is None:
            return None, dict(rec, pages=page)
        if not isinstance(d, dict) or not isinstance(d.get("jobs"), list) or not isinstance(d.get("total_count"), int):
            return None, dict(rec, outcome="failed", stage="shape", error_type="Malformed", pages=page)
        if total is None:
            total = d["total_count"]
        elif d["total_count"] != total:
            return None, dict(rec, outcome="failed", stage="shape", error_type="TotalChanged", pages=page)
        jobs.extend(d["jobs"])
        if not d["jobs"] or len(jobs) >= total:
            if len(jobs) != total:
                return None, dict(rec, outcome="failed", stage="shape", error_type="CountMismatch", pages=page)
            return {"total_count": total, "jobs": jobs, "pages": page}, dict(rec, pages=page)
    return None, dict(recs[-1], outcome="failed", stage="shape", error_type="TooManyPages", pages=MAX_PAGES)


def save(out, name, obj):
    with open(os.path.join(out, name), "x", encoding="utf-8") as f:
        json.dump(obj, f, indent=1, sort_keys=True)
        f.write("\n")


def fetch_shard(doc, shard, out, token, t=None, outp=None):
    outp = outp or sys.stdout
    runs = [r for r in doc["runs"] if r["shard"] == shard]
    t = t or Transport(runs)
    os.makedirs(os.path.join(out, "logs"), exist_ok=True)
    rl, rrec = get_json("/rate_limit", token, t, kind="rate")
    core = ((rl or {}).get("resources") or {}).get("core") or {}
    print("host shard %d: %d runs; rate_limit remaining=%s limit=%s (%s)" % (
        shard, len(runs), core.get("remaining"), core.get("limit"), rrec["outcome"]), file=outp)
    if isinstance(core.get("remaining"), int):
        t.remaining = core["remaining"]
    # The record is on disk from the start, every read pre-filled as not reached, and rewritten (atomically) after
    # each read, so a step stopped by its timeout leaves every completed read recorded and every other one named.
    rec_path = os.path.join(out, "fetch-record.json")
    if os.path.lexists(rec_path):
        raise RefusedExists()
    nr = {"outcome": "failed", "stage": "not-reached", "error_type": None, "http_status": None}
    record = {"shard": shard, "runs": {r["run_id"]: {"run": dict(nr), "jobs": dict(nr),
                                                     "log": dict(nr, job_id=r["bridge_job_id"])} for r in runs}}
    write_record(rec_path, record)

    def note(rid, what, rec):
        record["runs"][rid][what] = rec
        write_record(rec_path, record)  # every read is on disk as soon as it is done

    for r in runs:
        rid, jid = r["run_id"], r["bridge_job_id"]
        run, rec_run = get_json("/repos/%s/actions/runs/%s/attempts/1" % (REPO, rid), token, t)
        if run is not None:
            save(out, "run-%s.json" % rid, run)
        note(rid, "run", rec_run)
        jobs, rec_jobs = fetch_jobs(rid, token, t)
        if jobs is not None:
            save(out, "jobs-%s.json" % rid, jobs)
        note(rid, "jobs", rec_jobs)
        note(rid, "log", dict(nr, job_id=jid, stage="started"))
        rec_log = download_log(jid, token, os.path.join(out, "logs", jid + ".log"), t)
        note(rid, "log", rec_log)
        print("host run %s job %s: run %s, jobs %s, log %s%s" % (
            rid, jid, _brief(rec_run), _brief(rec_jobs), _brief(rec_log),
            (" bytes=%d lines=%d sha256=%s" % (rec_log["bytes"], rec_log["lines"], rec_log["sha256"]))
            if rec_log["outcome"] == "ok" else ""), file=outp)
    print("host shard %d: rate_limit remaining after=%s" % (shard, t.remaining), file=outp)
    return all(all(x["outcome"] == "ok" for x in v.values()) for v in record["runs"].values())


def write_record(path, record):
    """Replace the record atomically: a reader, or a step killed mid-write, sees the old or the new, never a part."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=1, sort_keys=True)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def _brief(rec):
    if rec["outcome"] == "ok":
        return "ok"
    return "failed(stage=%s type=%s status=%s)" % (rec.get("stage"), rec.get("error_type"), rec.get("http_status"))


# ----------------------------------------------------------------------------------------------- self-test

class _Server:
    def __init__(self, fn):
        self.state = {"requests": []}
        self.stop = threading.Event()
        state, stop = self.state, self.stop

        class H(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self):
                state["requests"].append({"path": self.path, "headers": {k.lower(): v for k, v in self.headers.items()}})
                fn(self, state, stop)

            def log_message(self, *a):
                pass

        class S(http.server.ThreadingHTTPServer):
            daemon_threads = True

            def handle_error(self, request, client_address):
                pass

        self.srv = S(("127.0.0.1", 0), H)
        self.port = self.srv.server_address[1]
        self.base = "http://127.0.0.1:%d" % self.port
        threading.Thread(target=self.srv.serve_forever, kwargs={"poll_interval": 0.05}, daemon=True).start()

    def close(self):
        self.stop.set()
        self.srv.shutdown()
        self.srv.server_close()


def _send(h, code, body=b"", headers=None, clen=True):
    h.send_response(code)
    for k, v in (headers or {}).items():
        h.send_header(k, v)
    if clen:
        h.send_header("Content-Length", str(len(body)))
    h.send_header("Connection", "close")
    h.end_headers()
    if body:
        with contextlib.suppress(OSError):
            h.wfile.write(body)


def self_test(work=None):
    base = tempfile.mkdtemp(prefix="host-selftest-", dir=work)
    try:
        return _self_test(base)
    finally:
        shutil.rmtree(base, ignore_errors=True)


def _self_test(base):
    import secrets
    token = "tok-" + secrets.token_hex(16)
    secret_path = "/blob/" + secrets.token_hex(12) + "/job-logs.txt"
    secret_query = "".join(["s", "v=2025-01-05&s", "e=2030-01-01T00%3A00%3A00Z&s", "ig=", secrets.token_hex(20)])
    body = "".join("2026-10-17T00:00:%02d.0000000Z line %d\n" % (i % 60, i) for i in range(300)).encode()
    fx = [{"run_id": "9001", "bridge_job_id": "9101", "head_sha": "a" * 40, "shard": 1},
          {"run_id": "9002", "bridge_job_id": "9102", "head_sha": "b" * 40, "shard": 1},
          {"run_id": "9003", "bridge_job_id": "9103", "head_sha": "c" * 40, "shard": 2}]
    fails, results = 0, []

    def case(name, cond):
        nonlocal fails
        results.append(name)
        print("  %s  %s" % ("ok  " if cond else "FAIL", name))
        fails += not cond

    print("host self-test (local API and storage servers, no network):")
    # --- the allow-list, production transport, no request sent
    t = Transport(fx[:2])
    R = "%s/repos/%s/actions" % (API_BASE, REPO)
    good = [("json", R + "/runs/9001/attempts/1"), ("json", R + "/runs/9002/attempts/1/jobs?per_page=100&page=1"),
            ("json", R + "/runs/9001/attempts/1/jobs?per_page=100&page=3"), ("log", R + "/jobs/9101/logs"),
            ("log", R + "/jobs/9102/logs"), ("rate", API_BASE + "/rate_limit")]
    bad = [("json", R + "/runs/9003/attempts/1"), ("json", R + "/runs/9001"), ("json", R + "/runs/9001/attempts/2"),
           ("json", R + "/runs/9001/attempts/1/jobs?per_page=100&page=4"),
           ("json", R + "/runs/9001/attempts/1/jobs?per_page=100&page=1&x=1"), ("json", R + "/runs/9001/logs"),
           ("json", R + "/runs/9001/artifacts"), ("json", R + "/artifacts/1/zip"), ("log", R + "/jobs/9103/logs"),
           ("log", R + "/jobs/9101/logs?x=1"), ("log", R + "/jobs/9101"), ("json", R + "/jobs/9101/logs"),
           ("log", R + "/runs/9001/logs"), ("json", R + "/runs/9001/attempts/1/../../../jobs/9101/logs"),
           ("json", R + "/runs/9001/attempts/1%2F"), ("json", R + "/runs/9001/attempts/1\n"),
           ("log", "http://api.github.com/repos/%s/actions/jobs/9101/logs" % REPO),
           ("log", "https://api.github.com.example.org/repos/%s/actions/jobs/9101/logs" % REPO),
           ("log", "https://u:p@api.github.com/repos/%s/actions/jobs/9101/logs" % REPO),
           ("json", "https://uploads.github.com/repos/%s/actions/runs/9001/attempts/1" % REPO),
           ("json", "%s/repos/amaybaum/other/actions/runs/9001/attempts/1" % API_BASE),
           ("rate", API_BASE + "/rate_limit?x=1")]
    for kind, url in good:
        try:
            check_url(url, t, kind)
            got = True
        except RefusedEndpoint:
            got = False
        case("allowed %s: %s" % (kind, url[len(API_BASE):]), got)
    for kind, url in bad:
        try:
            check_url(url, t, kind)
            got = False
        except RefusedEndpoint:
            got = True
        case("refused %s: %r" % (kind, url[:110]), got)

    # --- the pinned runs file
    d = os.path.join(base, "runs")
    os.makedirs(d)
    p = os.path.join(d, "runs.json")
    with open(p, "w") as f:
        json.dump({"runs": fx}, f)
    sha = hashlib.sha256(open(p, "rb").read()).hexdigest()
    try:
        ok = len(load_runs(p, sha)["runs"]) == 3
    except Refused:
        ok = False
    case("a runs file with the pinned digest loads", ok)
    try:
        load_runs(p, "0" * 64)
        ok = False
    except Refused:
        ok = True
    case("a runs file with another digest is refused", ok)
    with open(p, "w") as f:
        json.dump({"runs": fx + [dict(fx[0], shard=3)]}, f)
    try:
        load_runs(p, hashlib.sha256(open(p, "rb").read()).hexdigest())
        ok = False
    except Refused:
        ok = True
    case("a runs file repeating a run is refused", ok)

    # --- a whole shard against local servers
    class _Killed(BaseException):
        """Stands in for the step's timeout: nothing in host.py catches it."""

    def run_shard(api_fn, storage_fn, runs=fx, shard=1, cap=None, reserve=10, timeout=5.0, deadline=10.0,
                  use_token=token, allow_http_link=True, kill_job=None):
        storage = _Server(storage_fn)
        link = storage.base + secret_path + "?" + secret_query
        api = _Server(lambda h, st, stop: api_fn(h, st, stop, link))
        sh = [r for r in runs if r["shard"] == shard]
        tt = Transport(sh, api_base=api.base, token_host="127.0.0.1", allow_http_api=True,
                       allow_http_link=allow_http_link, proxies={}, timeout=timeout, deadline=deadline,
                       cap=cap if cap is not None else 2 * len(body), reserve=reserve)
        out = tempfile.mkdtemp(dir=base)
        buf = io.StringIO()
        real = globals()["download_log"]

        def killing(job_id, *a, **k):
            if job_id == kill_job:
                raise _Killed()
            return real(job_id, *a, **k)
        globals()["download_log"] = killing
        try:
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
                ok = fetch_shard({"runs": runs}, shard, out, use_token, tt, outp=buf)
        except _Killed:
            ok = "killed"
        finally:
            globals()["download_log"] = real
        api.close()
        storage.close()
        blob = b""
        for root, _, names in os.walk(out):
            for n in names:
                with open(os.path.join(root, n), "rb") as f:
                    blob += f.read()
        text = buf.getvalue()
        leak = any(s in text or s.encode() in blob for s in (link, secret_path, secret_query, token))
        rec = json.load(open(os.path.join(out, "fetch-record.json")))
        return ok, rec, api.state, storage.state, out, leak, text

    def api_ok(remaining=4000, log_code=302, jobs_total=2):
        def fn(h, st, stop, link):
            path = h.path
            hdr = {"X-RateLimit-Remaining": str(remaining - len(st["requests"]))}
            if path == "/rate_limit":
                _send(h, 200, json.dumps({"resources": {"core": {"remaining": remaining, "limit": 1000}}}).encode())
            elif "/jobs?" in path:
                rid = int(path.split("/runs/")[1].split("/")[0])
                _send(h, 200, json.dumps({"total_count": jobs_total, "jobs": [{"id": rid + 100, "name": "Mathlib bridge"},
                                                                              {"id": rid + 200, "name": "x"}]}).encode(), hdr)
            elif path.endswith("/attempts/1"):
                rid = int(path.split("/runs/")[1].split("/")[0])
                _send(h, 200, json.dumps({"id": rid, "run_attempt": 1}).encode(), hdr)
            elif path.endswith("/logs"):
                if log_code in (301, 302, 303, 307, 308):
                    _send(h, log_code, headers=dict(hdr, Location=link))
                else:
                    _send(h, log_code, b'{"message":"gone"}', hdr)
            else:
                _send(h, 404, b"{}", hdr)
        return fn

    def serve(h, st, stop):
        _send(h, 200, body, {"Content-Type": "text/plain"})

    ok, rec, a, s, out, leak, text = run_shard(api_ok(), serve)
    logs = sorted(os.listdir(os.path.join(out, "logs")))
    case("a clean shard reads both runs' records and logs, nothing of shard 2",
         ok and logs == ["9101.log", "9102.log"] and sorted(rec["runs"]) == ["9001", "9002"]
         and all(not r["path"].startswith("/repos/%s/actions/runs/9003" % REPO) for r in a["requests"]))
    case("each log's bytes, sha256 and line count are recorded",
         all(rec["runs"][x]["log"]["sha256"] == hashlib.sha256(body).hexdigest() and rec["runs"][x]["log"]["lines"] == 300
             for x in ("9001", "9002")))
    case("the token reaches the API server only, as Bearer",
         all(r["headers"].get("authorization") == "Bearer " + token for r in a["requests"])
         and all("authorization" not in r["headers"] and not any(token in v for v in r["headers"].values())
                 for r in s["requests"]))
    case("the storage link, its path, its query and the token appear in no output and no file", not leak)
    case("the rate limit is read once and printed as numbers only",
         sum(1 for r in a["requests"] if r["path"] == "/rate_limit") == 1 and "remaining=4000 limit=1000" in text)

    ok, rec, a, s, out, leak, text = run_shard(api_ok(), serve, kill_job="9102")
    r1, r2 = rec["runs"]["9001"], rec["runs"]["9002"]
    case("a step stopped during run 9002's log keeps run 9001's reads and run 9002's run and jobs reads on disk",
         ok == "killed" and all(r1[k]["outcome"] == "ok" for k in ("run", "jobs", "log"))
         and r2["run"]["outcome"] == "ok" and r2["jobs"]["outcome"] == "ok"
         and os.path.exists(os.path.join(out, "logs", "9101.log")))
    case("  ... and names run 9002's log as started, not read, with no partial record file left",
         r2["log"]["outcome"] == "failed" and r2["log"]["stage"] == "started"
         and not os.path.exists(os.path.join(out, "fetch-record.json.tmp")))
    ok, rec, a, s, out, leak, text = run_shard(api_ok(), serve, runs=fx, kill_job="9101")
    case("a step stopped at the first log leaves the later run pre-filled as not reached",
         ok == "killed" and rec["runs"]["9002"]["run"]["stage"] == "not-reached"
         and rec["runs"]["9002"]["log"]["stage"] == "not-reached" and rec["runs"]["9002"]["log"]["job_id"] == "9102")
    ok, rec, a, s, out, leak, text = run_shard(api_ok(log_code=410), serve)
    case("an expired log (HTTP 410) is recorded with its status, the run named, no file kept",
         not ok and rec["runs"]["9001"]["log"]["http_status"] == 410 and rec["runs"]["9001"]["log"]["outcome"] == "failed"
         and rec["runs"]["9001"]["run"]["outcome"] == "ok" and not os.listdir(os.path.join(out, "logs")))
    ok, rec, *_ = run_shard(api_ok(log_code=404), serve)
    case("a missing log (HTTP 404) is recorded with its status", not ok and rec["runs"]["9002"]["log"]["http_status"] == 404)

    ok, rec, a, s, out, leak, text = run_shard(api_ok(remaining=153), serve, reserve=150)
    reserved = [(x, k) for x in ("9001", "9002") for k in ("run", "jobs", "log")
                if rec["runs"][x][k]["stage"] == "rate-limit-reserve"]
    case("below the reserve no further request is sent, JSON or log, and each unread item is named",
         not ok and reserved == [("9002", "run"), ("9002", "jobs"), ("9002", "log")] and len(a["requests"]) == 4)

    def second_redirect(h, st, stop):
        _send(h, 302, headers={"Location": "http://127.0.0.1:9/elsewhere"})
    ok, rec, a, s, out, leak, _ = run_shard(api_ok(), second_redirect)
    case("a second redirect is refused, no file kept, nothing leaked",
         not ok and rec["runs"]["9001"]["log"]["error_type"] == "RefusedRedirect" and not os.listdir(os.path.join(out, "logs"))
         and not leak)
    ok, rec, a, s, *_ = run_shard(api_ok(), serve, allow_http_link=False)
    case("a non-https link is refused, storage never contacted",
         rec["runs"]["9001"]["log"]["error_type"] == "RefusedScheme" and not s["requests"])

    def json_redirect(h, st, stop, link):
        if h.path.endswith("/attempts/1"):
            _send(h, 302, headers={"Location": link})
        else:
            api_ok()(h, st, stop, link)
    ok, rec, a, s, *_ = run_shard(json_redirect, serve)
    case("a JSON endpoint answering with a redirect is refused and not followed",
         rec["runs"]["9001"]["run"]["error_type"] == "RefusedRedirect" and rec["runs"]["9002"]["run"]["error_type"]
         == "RefusedRedirect" and len(s["requests"]) == 2)   # the storage server saw only the two log fetches

    def no_redirect(h, st, stop, link):
        if h.path.endswith("/logs"):
            _send(h, 200, b"not a redirect")
        else:
            api_ok()(h, st, stop, link)
    ok, rec, *_ = run_shard(no_redirect, serve)
    case("a log endpoint answering 200 itself is refused", rec["runs"]["9001"]["log"]["error_type"] == "RefusedNoRedirect")

    def oversized(h, st, stop):
        _send(h, 200, os.urandom(3 * len(body)), clen=False)
    ok, rec, a, s, out, *_ = run_shard(api_ok(), oversized)
    case("an oversized body stops at the cap, no file kept",
         rec["runs"]["9001"]["log"]["error_type"] == "RefusedTooLarge" and not os.listdir(os.path.join(out, "logs")))

    def short(h, st, stop):
        h.send_response(200)
        h.send_header("Content-Length", str(len(body) + 10))
        h.send_header("Connection", "close")
        h.end_headers()
        h.wfile.write(body)
    ok, rec, a, s, out, *_ = run_shard(api_ok(), short)
    case("a body shorter than its Content-Length fails, no file kept",
         rec["runs"]["9001"]["log"]["outcome"] == "failed" and not os.listdir(os.path.join(out, "logs")))

    def dribble(h, st, stop):
        h.send_response(200)
        h.send_header("Content-Length", str(len(body)))
        h.send_header("Connection", "close")
        h.end_headers()
        for i in range(len(body)):
            if stop.wait(0.2):
                return
            with contextlib.suppress(OSError):
                h.wfile.write(body[i:i + 1])
                h.wfile.flush()
    ok, rec, *_ = run_shard(api_ok(), dribble, runs=fx[2:], shard=2, timeout=1.0, deadline=1.5)
    case("a dribbling server is stopped by the deadline", rec["runs"]["9003"]["log"]["error_type"] == "DeadlineExceeded")

    ok, rec, a, *_ = run_shard(api_ok(), serve, use_token="")
    case("no token: nothing is sent to the API but the refusal is recorded",
         not ok and rec["runs"]["9001"]["run"]["error_type"] == "RefusedNoToken"
         and not any(r["path"] != "/rate_limit" for r in a["requests"]))

    ok, rec, *_ = run_shard(api_ok(jobs_total=5), serve)
    case("a jobs list whose length is not its total_count is refused",
         rec["runs"]["9001"]["jobs"]["error_type"] == "CountMismatch")
    print("host self-test: %d of %d cases ok" % (len(results) - fails, len(results)))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--runs")
    ap.add_argument("--shard", type=int)
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    if a.self_test:
        return 1 if self_test(a.work) else 0
    if not (a.runs and a.shard and a.out):
        ap.error("--runs, --shard and --out are required")
    try:
        doc = load_runs(a.runs)
    except (Refused, OSError, ValueError, KeyError) as e:
        print("host refused: %s" % str(e)[:300])
        return 3
    os.makedirs(a.out, exist_ok=True)
    return 0 if fetch_shard(doc, a.shard, a.out, os.environ.get("GH_TOKEN", "")) else 3


if __name__ == "__main__":
    sys.exit(main())
