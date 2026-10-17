#!/usr/bin/env python3
"""Download one workflow artifact's original zip, as an explicit two-step, and hash it.

  python3 -I download_artifact_zip.py --repo amaybaum/incompleteness --artifact-id 12090461970 \
      --metadata artifact-12090461970.json --out artifact.zip --record download-record.json
  python3 -I download_artifact_zip.py --self-test [--work DIR]

Step 1 sends GET to the artifact's zip endpoint on api.github.com with `Authorization: Bearer $GH_TOKEN` and no
redirect handling. Before anything is sent, the endpoint is checked: scheme, host and full path must equal
PINNED_ENDPOINT exactly, or the request is refused and the token is never used. The answer must be a redirect.
Step 2 sends GET to the redirect target with no Authorization header. It must be https, carry no user info, and
answer 200 itself: any further redirect is refused. The body is read in chunks under a size cap
(min(2 x the metadata's size_in_bytes, 64 MiB)), checked against Content-Length when one is sent, under a
connect/read timeout and an overall deadline, and written to a new file while it is hashed.

The redirect target is never printed, logged or recorded, nor is its path or query. A failure records only the stage,
the exception type and the host. The record (JSON) holds the outcome, the hosts, the endpoint of step 1, and on
success the size and sha256 of the bytes written. Exit 0 when the zip was written, 3 otherwise. Python 3.12 stdlib.
"""
import argparse
import contextlib
import hashlib
import http.server
import io
import json
import os
import shutil
import socket
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
PINNED_ENDPOINT = "https://api.github.com/repos/amaybaum/incompleteness/actions/artifacts/12090461970/zip"
API_BASE = "https://api.github.com"
TOKEN_HOST = "api.github.com"
FIXED_CAP = 64 * 1024 * 1024
TIMEOUT_S = 60.0
DEADLINE_S = 300.0
CHUNK = 64 * 1024
UA = "artifact-validator/1 (read-only)"


class Refused(Exception):
    """A policy refusal; the class name is the reason."""


class RefusedEndpoint(Refused): pass
class RefusedScheme(Refused): pass
class RefusedNoToken(Refused): pass
class RefusedNoRedirect(Refused): pass
class RefusedLocation(Refused): pass
class RefusedRedirect(Refused): pass
class RefusedStatus(Refused): pass
class RefusedTooLarge(Refused): pass
class RefusedLengthMismatch(Refused): pass
class RefusedNoMetadata(Refused): pass
class RefusedExists(Refused): pass
class DeadlineExceeded(Refused): pass


class Transport:
    """Production transport. Only the self-test builds a different one."""
    def __init__(self, api_base=API_BASE, pinned_endpoint=PINNED_ENDPOINT, token_host=TOKEN_HOST,
                 allow_http_api=False, allow_http_link=False, proxies=None, timeout=TIMEOUT_S,
                 deadline=DEADLINE_S, fixed_cap=FIXED_CAP):
        self.api_base = api_base
        self.pinned_endpoint = pinned_endpoint
        self.token_host = token_host
        self.allow_http_api = allow_http_api
        self.allow_http_link = allow_http_link
        self.proxies = proxies          # None: the environment's proxy settings; {}: none
        self.timeout = timeout
        self.deadline = deadline
        self.fixed_cap = fixed_cap


def _opener(t):
    # No redirect handler at all: a 3xx reaches HTTPDefaultErrorHandler and is raised as HTTPError, never followed.
    # No cookie, auth, file, ftp or data handler.
    op = urllib.request.OpenerDirector()
    for h in (urllib.request.ProxyHandler(t.proxies), urllib.request.UnknownHandler(),
              urllib.request.HTTPHandler(), urllib.request.HTTPSHandler(),
              urllib.request.HTTPDefaultErrorHandler(), urllib.request.HTTPErrorProcessor()):
        op.add_handler(h)
    return op


def size_cap(metadata_path, fixed_cap=FIXED_CAP):
    try:
        with open(metadata_path, encoding="utf-8") as f:
            n = int(json.load(f)["size_in_bytes"])
    except Exception:
        raise RefusedNoMetadata()
    if n <= 0:
        raise RefusedNoMetadata()
    return min(2 * n, fixed_cap)


def _check_endpoint(url, t):
    u, p = urllib.parse.urlsplit(url), urllib.parse.urlsplit(t.pinned_endpoint)
    ok_scheme = u.scheme == "https" or (t.allow_http_api and u.scheme == "http")
    if not (url == t.pinned_endpoint and ok_scheme and u.scheme == p.scheme and u.hostname == p.hostname
            and u.port == p.port and u.path == p.path and u.query == "" and u.fragment == ""
            and u.username is None and u.password is None):
        raise RefusedEndpoint()
    return u


def download(repo, artifact_id, token, out_path, cap, t=None):
    """Returns a record dict. It never contains the redirect target, its path or its query."""
    t = t or Transport()
    url = f"{t.api_base}/repos/{repo}/actions/artifacts/{artifact_id}/zip"
    rec = {"artifact_id": str(artifact_id), "repo": repo, "api_endpoint": None, "outcome": "failed",
           "stage": "endpoint", "error_type": None, "error_host": urllib.parse.urlsplit(url).hostname,
           "storage_host": None, "bytes": None, "sha256": None, "size_cap": cap}
    wrote = False
    try:
        u = _check_endpoint(url, t)
        rec["api_endpoint"] = url
        if u.hostname != t.token_host:
            raise RefusedEndpoint()
        if not token:
            raise RefusedNoToken()
        if os.path.lexists(out_path):
            raise RefusedExists()
        op = _opener(t)
        start = time.monotonic()
        rec["stage"], rec["error_host"] = "api", u.hostname
        req = urllib.request.Request(url, method="GET", headers={
            "User-Agent": UA, "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28", "Authorization": f"Bearer {token}"})
        loc = None
        try:
            resp = op.open(req, timeout=t.timeout)
        except urllib.error.HTTPError as e:
            code, loc = e.code, e.headers.get("Location")
            e.close()
            if code not in (301, 302, 303, 307, 308):
                raise
        else:
            resp.close()
            raise RefusedNoRedirect()
        if not loc:
            raise RefusedLocation()
        v = urllib.parse.urlsplit(loc)
        rec["stage"], rec["error_host"] = "storage", v.hostname
        if not (v.scheme == "https" or (t.allow_http_link and v.scheme == "http")):
            raise RefusedScheme()
        if not v.hostname or v.username is not None or v.password is not None:
            raise RefusedLocation()
        rec["storage_host"] = v.hostname
        req2 = urllib.request.Request(loc, method="GET", headers={"User-Agent": UA})
        try:
            resp = op.open(req2, timeout=t.timeout)
        except urllib.error.HTTPError as e:
            code = e.code
            e.close()
            if 300 <= code < 400:
                raise RefusedRedirect()
            raise
        h = hashlib.sha256()
        total = 0
        with resp:
            if resp.status != 200:
                raise RefusedStatus()
            clen = resp.headers.get("Content-Length")
            if clen is not None:
                if not clen.strip().isdigit():
                    raise RefusedLengthMismatch()
                if int(clen) > cap:
                    raise RefusedTooLarge()
            with open(out_path, "xb") as f:
                wrote = True
                while True:
                    if time.monotonic() - start > t.deadline:
                        raise DeadlineExceeded()
                    # read1 returns as soon as any bytes arrive, so the deadline is checked between arrivals
                    # (a plain read(n) would block until n bytes came, however slowly they dribbled in).
                    chunk = resp.read1(min(CHUNK, cap + 1 - total))
                    if not chunk:
                        break
                    total += len(chunk)
                    if total > cap:
                        raise RefusedTooLarge()
                    h.update(chunk)
                    f.write(chunk)
            if clen is not None and int(clen) != total:
                raise RefusedLengthMismatch()
        rec.update(outcome="ok", stage="done", error_type=None, error_host=None, bytes=total, sha256=h.hexdigest())
    except BaseException as e:  # noqa: BLE001 - only the type name is ever kept
        if isinstance(e, KeyboardInterrupt):
            raise
        rec["error_type"] = type(e).__name__
        if wrote:
            with contextlib.suppress(OSError):
                os.unlink(out_path)
    return rec


def print_record(rec, out=None):
    out = out or sys.stdout
    if rec["outcome"] == "ok":
        print(f"download  ok  endpoint={rec['api_endpoint']} storage_host={rec['storage_host']} "
              f"bytes={rec['bytes']} sha256={rec['sha256']} cap={rec['size_cap']}", file=out)
    else:
        print(f"download  failed  stage={rec['stage']} error_type={rec['error_type']} host={rec['error_host']}",
              file=out)


def write_record(path, rec):
    with open(path, "x", encoding="utf-8") as f:
        json.dump(rec, f, indent=1, sort_keys=True)
        f.write("\n")


# ----------------------------------------------------------------------------------------------- self-test

class _Server:
    """A local HTTP server whose GET handler is a function of (handler, state)."""
    def __init__(self, fn):
        self.state = {"requests": []}
        self.stop = threading.Event()
        state, stop = self.state, self.stop

        class H(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def do_GET(self):
                state["requests"].append({"path": self.path, "headers": {k.lower(): v for k, v in self.headers.items()}})
                fn(self, state, stop)

            def log_message(self, *a):  # the request line would carry the link
                pass

        class S(http.server.ThreadingHTTPServer):
            daemon_threads = True

            def handle_error(self, request, client_address):  # a client that gave up is expected here
                pass

        self.srv = S(("127.0.0.1", 0), H)
        self.port = self.srv.server_address[1]
        self.base = f"http://127.0.0.1:{self.port}"
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


def test_transport(api, allow_http_link=True, timeout=5.0, deadline=10.0, fixed_cap=FIXED_CAP):
    return Transport(api_base=api.base, pinned_endpoint=f"{api.base}/repos/o/r/actions/artifacts/7/zip",
                     token_host="127.0.0.1", allow_http_api=True, allow_http_link=allow_http_link, proxies={},
                     timeout=timeout, deadline=deadline, fixed_cap=fixed_cap)


def self_test(work=None):
    """Transport checks. Returns the number of failed cases."""
    base = tempfile.mkdtemp(prefix="dl-selftest-", dir=work)
    try:
        return _self_test(base)
    finally:
        shutil.rmtree(base, ignore_errors=True)


def _self_test(base):
    import secrets
    token = "tok-" + secrets.token_hex(16)
    secret_path = "/blob/" + secrets.token_hex(12) + "/artifact.zip"
    secret_query = "".join(["s", "v=2025-01-05&s", "e=2030-01-01T00%3A00%3A00Z&s", "ig=", secrets.token_hex(20)])
    body = os.urandom(5000)
    fails = 0
    results = []

    def case(name, cond):
        nonlocal fails
        results.append((name, bool(cond)))
        print(f"  {'ok  ' if cond else 'FAIL'}  {name}")
        if not cond:
            fails += 1

    def run(api_fn, storage_fn, *, repo="o/r", aid="7", allow_http_link=True, timeout=5.0, deadline=10.0,
            cap=None, fixed_cap=FIXED_CAP, use_token=token, pinned=None):
        storage = _Server(storage_fn)
        link = storage.base + secret_path + "?" + secret_query

        def api_handler(h, st, stop):
            api_fn(h, st, stop, link)
        api = _Server(api_handler)
        t = test_transport(api, allow_http_link, timeout, deadline, fixed_cap)
        if pinned is not None:
            t.pinned_endpoint = pinned(api)
        d = tempfile.mkdtemp(dir=base)
        out = os.path.join(d, "artifact.zip")
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            rec = download(repo, aid, use_token, out, cap if cap is not None else 2 * len(body), t)
            print_record(rec)
            write_record(os.path.join(d, "record.json"), rec)
        api.close()
        storage.close()
        files = b""
        for root, _, names in os.walk(d):
            for n in names:
                with open(os.path.join(root, n), "rb") as f:
                    files += f.read()
        text = buf.getvalue()
        leaked = any(s in text or s.encode() in files for s in (link, secret_path, secret_query))
        tok_leak = token in text or token.encode() in files
        return rec, api.state, storage.state, out, leaked or tok_leak, text

    def redirect(h, st, stop, link):
        _send(h, 302, headers={"Location": link})

    def serve(h, st, stop):
        _send(h, 200, body, {"Content-Type": "application/zip"})

    print("download self-test (local API and storage servers, no network):")
    rec, a, s, out, leak, _ = run(redirect, serve)
    case("clean two-step download writes the bytes and their sha256",
         rec["outcome"] == "ok" and rec["sha256"] == hashlib.sha256(body).hexdigest() and rec["bytes"] == len(body)
         and open(out, "rb").read() == body)
    case("the token reaches the API server, as Bearer",
         len(a["requests"]) == 1 and a["requests"][0]["headers"].get("authorization") == f"Bearer {token}")
    case("the storage server receives no Authorization header and never the token",
         len(s["requests"]) == 1 and "authorization" not in s["requests"][0]["headers"]
         and not any(token in v for v in s["requests"][0]["headers"].values()))
    case("the link, its path and its query appear in neither the output nor the recorded files", not leak)

    def second_redirect(h, st, stop):
        _send(h, 302, headers={"Location": "http://127.0.0.1:9/elsewhere"})
    rec, a, s, out, leak, _ = run(redirect, second_redirect)
    case("a second redirect is refused (RefusedRedirect), no file kept",
         rec["outcome"] == "failed" and rec["error_type"] == "RefusedRedirect" and not os.path.exists(out) and not leak)

    rec, a, s, out, leak, _ = run(redirect, serve, allow_http_link=False)
    case("a non-https link is refused without the test-only flag, storage never contacted",
         rec["error_type"] == "RefusedScheme" and rec["stage"] == "storage" and not s["requests"] and not leak)

    rec, a, s, out, leak, _ = run(redirect, serve, repo="o/other")
    case("a different repo is refused before sending: RefusedEndpoint, API never contacted",
         rec["error_type"] == "RefusedEndpoint" and not a["requests"] and not s["requests"])
    rec, a, s, out, leak, _ = run(redirect, serve, aid="8")
    case("a different artifact id is refused before sending",
         rec["error_type"] == "RefusedEndpoint" and not a["requests"])
    rec, a, s, out, leak, _ = run(redirect, serve, pinned=lambda api: "http://localhost:%d/repos/o/r/actions/artifacts/7/zip" % api.port)
    case("a different host than the pinned one is refused before sending",
         rec["error_type"] == "RefusedEndpoint" and not a["requests"])
    for bad in ("o/r/../r", "o/r?x=1"):
        rec, a, s, out, leak, _ = run(redirect, serve, repo=bad)
        case(f"a path-shaped repo {bad!r} is refused before sending",
             rec["error_type"] == "RefusedEndpoint" and not a["requests"])
    t = Transport()
    for repo, aid, ok in (("amaybaum/incompleteness", "12090461970", True), ("amaybaum/other", "12090461970", False),
                          ("amaybaum/incompleteness", "12090461971", False)):
        url = f"{t.api_base}/repos/{repo}/actions/artifacts/{aid}/zip"
        try:
            _check_endpoint(url, t)
            got = True
        except RefusedEndpoint:
            got = False
        case(f"production pin: {repo} artifact {aid} {'accepted' if ok else 'refused'}", got == ok)
    for host_base in ("https://api.github.com.example.org", "https://uploads.github.com", "http://api.github.com"):
        t2 = Transport(api_base=host_base, proxies={}, timeout=1.0)
        rec = download("amaybaum/incompleteness", "12090461970", token, os.path.join(base, "never.zip"), 100, t2)
        case(f"production pin: base {host_base} refused before sending", rec["error_type"] == "RefusedEndpoint")

    rec, a, s, out, leak, _ = run(redirect, serve, use_token="")
    case("no token: refused before sending", rec["error_type"] == "RefusedNoToken" and not a["requests"])

    def no_redirect(h, st, stop, link):
        _send(h, 200, b"{}")
    rec, *_ = run(no_redirect, serve)
    case("an API answer without a redirect is refused", rec["error_type"] == "RefusedNoRedirect")

    def userinfo(h, st, stop, link):
        _send(h, 302, headers={"Location": link.replace("http://", "http://u:p@")})
    rec, a, s, *_ = run(userinfo, serve)
    case("a link with user info is refused", rec["error_type"] == "RefusedLocation" and not s["requests"])

    def relative(h, st, stop, link):
        _send(h, 302, headers={"Location": "/relative/path"})
    rec, *_ = run(relative, serve)
    case("a relative link is refused", rec["error_type"] in ("RefusedLocation", "RefusedScheme"))

    def oversized(h, st, stop):
        _send(h, 200, os.urandom(3 * len(body)))
    rec, a, s, out, leak, _ = run(redirect, oversized)
    case("an oversized body (Content-Length over the cap) is refused: RefusedTooLarge, no file kept",
         rec["error_type"] == "RefusedTooLarge" and not os.path.exists(out) and not leak)

    def oversized_nolen(h, st, stop):
        _send(h, 200, os.urandom(3 * len(body)), clen=False)
    rec, a, s, out, leak, _ = run(redirect, oversized_nolen)
    case("an oversized body without Content-Length stops at the cap: RefusedTooLarge",
         rec["error_type"] == "RefusedTooLarge" and not os.path.exists(out))
    case("the cap is min(2 x size_in_bytes, fixed cap); missing or zero size refuses", size_cap_check(base))

    def short(h, st, stop):
        h.send_response(200)
        h.send_header("Content-Length", str(len(body) + 10))
        h.send_header("Connection", "close")
        h.end_headers()
        h.wfile.write(body)
    rec, *_ = run(redirect, short)
    case("a body shorter than its Content-Length fails", rec["outcome"] == "failed")

    def slow_header(h, st, stop):
        if not stop.wait(3.0):
            _send(h, 200, body)
    rec, a, s, out, leak, _ = run(redirect, slow_header, timeout=0.5, deadline=2.0)
    case("a slow server (no answer within the read timeout) fails with a timeout type",
         rec["outcome"] == "failed" and rec["error_type"] in ("TimeoutError", "URLError") and not leak)

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
    rec, a, s, out, leak, _ = run(redirect, dribble, timeout=1.0, deadline=1.5)
    case("a dribbling server is stopped by the overall deadline: DeadlineExceeded, no file kept",
         rec["error_type"] == "DeadlineExceeded" and not os.path.exists(out))

    def err500(h, st, stop):
        _send(h, 500, b"x")
    rec, a, s, out, leak, text = run(redirect, err500)
    case("a storage error records only stage, type and host",
         rec["outcome"] == "failed" and rec["error_type"] == "HTTPError" and rec["error_host"] == "127.0.0.1"
         and rec["stage"] == "storage" and not leak)
    print(f"download self-test: {len(results) - fails} of {len(results)} cases ok")
    return fails


def size_cap_check(base):
    p = os.path.join(base, "meta-cap.json")
    with open(p, "w") as f:
        json.dump({"size_in_bytes": 1000}, f)
    a = size_cap(p) == 2000 and size_cap(p, fixed_cap=1500) == 1500
    with open(p, "w") as f:
        json.dump({"size_in_bytes": 0}, f)
    try:
        size_cap(p)
        b = False
    except RefusedNoMetadata:
        b = True
    try:
        size_cap(os.path.join(base, "absent.json"))
        c = False
    except RefusedNoMetadata:
        c = True
    return a and b and c


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--repo")
    ap.add_argument("--artifact-id")
    ap.add_argument("--metadata", help="the artifact's API metadata (JSON); bounds the download")
    ap.add_argument("--out")
    ap.add_argument("--record")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work", help="parent directory for self-test scratch files")
    a = ap.parse_args(argv)
    if a.self_test:
        return 1 if self_test(a.work) else 0
    if not (a.repo and a.artifact_id and a.metadata and a.out and a.record):
        ap.error("--repo, --artifact-id, --metadata, --out and --record are required")
    try:
        cap = size_cap(a.metadata)
    except RefusedNoMetadata:
        rec = {"artifact_id": a.artifact_id, "repo": a.repo, "api_endpoint": None, "outcome": "failed",
               "stage": "metadata", "error_type": "RefusedNoMetadata", "error_host": None, "storage_host": None,
               "bytes": None, "sha256": None, "size_cap": None}
    else:
        rec = download(a.repo, a.artifact_id, os.environ.get("GH_TOKEN", ""), a.out, cap)
    print_record(rec)
    write_record(a.record, rec)
    return 0 if rec["outcome"] == "ok" else 3


if __name__ == "__main__":
    sys.exit(main())
