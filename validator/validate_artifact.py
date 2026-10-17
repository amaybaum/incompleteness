#!/usr/bin/env python3
"""Independent validator for one log-archive workflow artifact (ci-logs-<sha>).

Written from the artifact's format specification only; it shares no code with the archiver.

  python3 -I validate_artifact.py --zip artifact.zip --extract-to DIR --metadata artifact-<id>.json \
      --batch batch.json --inventory-runs inventory-runs.csv --inventory-jobs inventory-jobs.csv \
      --host HOSTDIR [--download-record download-record.json] \
      --expect-input-sha256 batch.json=<hex> --expect-input-sha256 inventory-runs.csv=<hex> ...
  python3 -I validate_artifact.py --dir EXTRACTED ...      (no zip: the digest is UNVERIFIED)
  python3 -I validate_artifact.py --self-test [--work DIR]

Every check prints one PASS, FAIL or UNVERIFIED line (FAIL: the evidence contradicts; UNVERIFIED: the evidence is
unavailable). INFO lines are not gating. The last line is `VALIDATE  HOLDS` (exit 0), `VALIDATE  FAILS (<n>)`
(exit 1) or `VALIDATE  UNVERIFIED (<n>)` (exit 2). Output holds names, sizes, hashes and counts only, never log
content. Python 3.12 stdlib only; run with `python3 -I`.
"""
import argparse
import contextlib
import csv
import datetime as dt
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import stat
import sys
import tempfile
import traceback
import zipfile
import zlib

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
HERE = os.path.dirname(os.path.abspath(__file__))
KEY_FIELD = "key"  # the spec: "the last line for a key wins"; each fetch-log object names its key in this field
META_FILES = ("completeness.json", "fetch-log.jsonl", "manifest.json", "scan.json")
JOB_FIELDS = ("id", "name", "status", "conclusion", "head_sha", "started_at", "completed_at", "runner_id")
PILOT = {"repo": "amaybaum/incompleteness", "artifact_id": "12090461970", "source_run_id": "39005152534",
         "source_head_sha": "05df8cc18e0103ae9f3ffbf52b1ecb6a6aedf64b"}
EXPIRY_TOLERANCE_S = 60
DEFAULT_RETENTION_DAYS = 14
MAX_EXTRACT_BYTES = 2 * 1024 ** 3
MAX_MEMBERS = 200000
ZIP_ERRORS = (zipfile.BadZipFile, OSError, ValueError, EOFError, NotImplementedError, zlib.error)
TOP_RE = re.compile(r"^-?(\d+)_(.+)\.txt$")
KEY_RES = {
    "run": re.compile(r"^run:(\d+)$"),
    "jobs": re.compile(r"^jobs:(\d+):(\d+)$"),
    "zip": re.compile(r"^zip:(\d+):(\d+)$"),
    "joblog": re.compile(r"^joblog:(\d+)$"),
}
OUTCOME = {"run": "ok", "jobs": "ok", "zip": "archived", "joblog": "archived"}

# Credential-shaped patterns. Masked values (***) never match. Report locations only, never the match.
SCAN_PATTERNS = [
    ("github-token", rb"(?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9]{36,255}(?![A-Za-z0-9])"),
    ("github-app-token-jwt", rb"(?<![A-Za-z0-9_])ghs_[A-Za-z0-9]{1,64}_[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]*"),
    ("github-token-generic", rb"(?<![A-Za-z0-9_])gh[pousr]_[A-Za-z0-9_.\-]{20,}"),
    ("github-fine-grained-pat", rb"github_pat_[A-Za-z0-9_]{20,}"),
    ("github-installation-v1", rb"(?<![A-Za-z0-9.])v1\.[0-9a-f]{40}(?![0-9a-f])"),
    ("jwt", rb"eyJ[A-Za-z0-9_-]{6,}\.eyJ[A-Za-z0-9_-]{6,}\.[A-Za-z0-9_-]*"),
    ("azure-sas-sig", rb"(?i)[?&]sig=(?!\*\*\*)[A-Za-z0-9%+/=_-]{10,}"),
    ("azure-sas-se", rb"(?i)[?&]se=\d{4}-\d{2}-\d{2}"),
    ("azure-sas-sv", rb"(?i)[?&]sv=\d{4}-\d{2}-\d{2}"),
    ("authorization-header", rb"(?i)authorization\s*[:=]\s*\"?(?:bearer|token|basic)\s+(?!\*\*\*)[A-Za-z0-9+/=._~-]{8,}"),
    ("x-access-token-url", rb"x-access-token" rb":(?!\*\*\*)[^@\s/]{8,}@"),
    ("url-credentials", rb"[a-z][a-z0-9+.-]*://[^/\s:@]+:(?!\*\*\*)[^/\s@]{8,}@"),
    ("aws-access-key-id", rb"(?<![A-Z0-9])(?:AKIA|ASIA|AGPA|AIDA|AROA|ANPA|ANVA|AIPA)[0-9A-Z]{16}(?![A-Z0-9])"),
    ("aws-secret-access-key", rb"(?i)aws_secret_access_key\s*[=:]\s*\"?[A-Za-z0-9/+=]{40}"),
    ("private-key", rb"-----BEGIN (?:[A-Z0-9]+ )*PRIVATE KEY(?: BLOCK)?-----"),
]
SCAN_RES = [(n, re.compile(p)) for n, p in SCAN_PATTERNS]


# ----------------------------------------------------------------------------------------------- utilities

def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def sha256_file(path):
    h, n = hashlib.sha256(), 0
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
            n += len(chunk)
    return n, h.hexdigest()


def load_json(path):
    if not path:
        return None, "not given"
    if not os.path.isfile(path):
        return None, "absent"
    try:
        with open(path, "rb") as f:
            return json.loads(f.read()), None
    except (OSError, ValueError) as e:
        return None, f"unreadable ({type(e).__name__})"


def safe(s, n=120):
    """A printable form of a name for output (names only, never content)."""
    s = ascii(str(s))[1:-1]
    return s if len(s) <= n else s[:n] + "..."


def parse_time(s):
    return dt.datetime.fromisoformat(str(s).replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def norm_name(s):
    return "".join(ch for ch in str(s).casefold() if ch.isalnum())


def sid(x):
    return None if x is None else str(x)


def project(job):
    p = {f: job.get(f) for f in JOB_FIELDS}
    p["id"], p["runner_id"] = sid(p["id"]), sid(p["runner_id"])
    return p


def ran(job):
    """A job that ran and so has a log: completed, not skipped, and taken by a runner."""
    return job.get("status") == "completed" and job.get("conclusion") != "skipped" and bool(job.get("runner_id")) \
        and str(job.get("runner_id")) != "0"


class Report:
    def __init__(self, out=None):
        self.out = out if out is not None else sys.stdout
        self.rows = []

    def _emit(self, status, cid, msg):
        self.rows.append((status, cid, msg))
        print(f"{status:<10} {cid:<18} {msg}".rstrip(), file=self.out)

    def ok(self, cid, msg=""):
        self._emit("PASS", cid, msg)

    def fail(self, cid, msg=""):
        self._emit("FAIL", cid, msg)

    def unv(self, cid, msg=""):
        self._emit("UNVERIFIED", cid, msg)

    def info(self, cid, msg=""):
        self._emit("INFO", cid, msg)

    def check(self, cid, cond, msg_pass, msg_fail=None):
        (self.ok if cond else self.fail)(cid, msg_pass if cond else (msg_fail or msg_pass))
        return cond

    def head(self, label, value):
        print(f"{label:<20}{value}", file=self.out)

    def failed_ids(self):
        return [c for s, c, _ in self.rows if s == "FAIL"]

    def unverified_ids(self):
        return [c for s, c, _ in self.rows if s == "UNVERIFIED"]

    def verdict(self):
        f, u = len(self.failed_ids()), len(self.unverified_ids())
        if f:
            return f"VALIDATE  FAILS ({f})", 1
        if u:
            return f"VALIDATE  UNVERIFIED ({u})", 2
        if not any(s == "PASS" for s, _, _ in self.rows):
            return "VALIDATE  UNVERIFIED (0)", 2
        return "VALIDATE  HOLDS", 0


class Ctx:
    pass


# ----------------------------------------------------------------------------------------------- 0, 1: inputs and artifact

def check_inputs(a, rep, c):
    pins = {}
    for item in a.expect_input_sha256 or []:
        name, _, hexd = item.partition("=")
        pins[name] = hexd.lower()
    c.inputs_ok = True
    c.batch = c.inv_runs = c.inv_jobs = None
    status = []
    for label, path in (("batch.json", a.batch), ("inventory-runs.csv", a.inventory_runs),
                        ("inventory-jobs.csv", a.inventory_jobs)):
        if not path or not os.path.isfile(path):
            rep.unv("0.inputs", f"{label}: {'not given' if not path else 'absent'}")
            c.inputs_ok = False
            continue
        size, h = sha256_file(path)
        name = os.path.basename(path)
        if name not in pins:
            rep.unv("0.inputs", f"{label}: sha256 {h} ({size} bytes) has no pinned value to check")
            c.inputs_ok = False
        elif pins[name] != h:
            rep.fail("0.inputs", f"{label}: sha256 {h} differs from the pin {pins[name]}")
            c.inputs_ok = False
        else:
            status.append(f"{label}={h[:16]}")
    if not a.batch or not os.path.isfile(a.batch):
        return
    batch, err = load_json(a.batch)
    if err or not isinstance(batch, dict) or not isinstance(batch.get("run_ids"), list):
        rep.unv("0.inputs", f"batch.json unusable ({err or 'no run_ids list'})")
        c.inputs_ok = False
        return
    c.batch = batch
    try:
        if a.inventory_runs and os.path.isfile(a.inventory_runs):
            with open(a.inventory_runs, newline="", encoding="utf-8") as f:
                c.inv_runs = {r["run_id"]: r for r in csv.DictReader(f)}
        if a.inventory_jobs and os.path.isfile(a.inventory_jobs):
            with open(a.inventory_jobs, newline="", encoding="utf-8") as f:
                c.inv_jobs = list(csv.DictReader(f))
    except (OSError, KeyError, csv.Error, UnicodeDecodeError) as e:
        rep.unv("0.inputs", f"inventory unreadable ({type(e).__name__})")
        c.inputs_ok = False
    if c.inputs_ok:
        rep.ok("0.inputs", "inputs match their pins: " + ", ".join(status))


def check_artifact(a, rep, c):
    """Artifact level. Sets c.root to the directory that the content checks read, or None."""
    c.root = None
    meta = c.meta
    if meta is None:
        rep.unv("1.metadata", f"artifact metadata {c.meta_err}")
    # download record
    if a.download_record:
        drec, err = load_json(a.download_record)
        if err or not isinstance(drec, dict):
            rep.unv("1.download", f"download record {err or 'not an object'}")
        elif drec.get("outcome") != "ok":
            rep.unv("1.download", f"download failed: stage={safe(drec.get('stage'))} "
                                  f"error_type={safe(drec.get('error_type'))} host={safe(drec.get('error_host'))}")
        else:
            exp_ep = getattr(a, "expected_endpoint", None) or \
                f"https://api.github.com/repos/{a.repo}/actions/artifacts/{a.artifact_id}/zip"
            ok = drec.get("api_endpoint") == exp_ep and c.zip_hash is not None and \
                drec.get("sha256") == c.zip_hash[1] and drec.get("bytes") == c.zip_hash[0]
            rep.check("1.download", ok,
                      f"downloaded from the pinned endpoint; storage host {safe(drec.get('storage_host'))}; "
                      f"record size and sha256 equal the file",
                      "download record disagrees with the pinned endpoint or with the file's size/sha256")
    # digest and size
    exp_digest = (meta or {}).get("digest") if meta else None
    exp_size = (meta or {}).get("size_in_bytes") if meta else None
    if c.zip_hash is None or meta is None:
        why = "no artifact zip" if c.zip_hash is None else "no metadata"
        rep.unv("1.digest", f"cannot compare: {why}")
        rep.unv("1.size", f"cannot compare: {why}")
    elif not (isinstance(exp_digest, str) and re.fullmatch(r"sha256:[0-9a-f]{64}", exp_digest)) or \
            isinstance(exp_size, bool) or not isinstance(exp_size, int):
        rep.unv("1.digest", "the metadata carries no usable sha256 digest or size to compare with")
        rep.unv("1.size", "the metadata carries no usable sha256 digest or size to compare with")
    else:
        rep.check("1.digest", exp_digest == f"sha256:{c.zip_hash[1]}",
                  f"sha256 of the zip equals the metadata digest",
                  f"sha256 of the zip differs from the metadata digest")
        rep.check("1.size", exp_size == c.zip_hash[0], f"{c.zip_hash[0]} bytes, as the metadata says",
                  f"{c.zip_hash[0]} bytes, metadata says {safe(exp_size)}")
    if meta is not None:
        wr = meta.get("workflow_run") or {}
        ident = (str(meta.get("id")) == str(a.artifact_id), meta.get("name") == f"ci-logs-{a.source_head_sha}",
                 str(wr.get("id")) == str(a.source_run_id), wr.get("head_sha") == a.source_head_sha)
        rep.check("1.identity", all(ident),
                  f"artifact {safe(meta.get('id'))} name {safe(meta.get('name'))} from run {safe(wr.get('id'))} "
                  f"at {safe(wr.get('head_sha'))}",
                  f"metadata identity differs (id, name, run, head: {['ok' if x else 'differs' for x in ident]})")
        try:
            retention = int((c.batch or {}).get("retention_days", DEFAULT_RETENTION_DAYS))
            created, expires = parse_time(meta["created_at"]), parse_time(meta["expires_at"])
            delta = (expires - created).total_seconds()
            off = delta - retention * 86400
            ok = meta.get("expired") is False and abs(off) <= EXPIRY_TOLERANCE_S
            rep.check("1.expiry", ok,
                      f"expired=false; staged {meta['created_at']}, expires {meta['expires_at']}: "
                      f"{retention} days {off:+.0f} s (tolerance {EXPIRY_TOLERANCE_S} s)",
                      f"expired={safe(meta.get('expired'))}; staged {safe(meta.get('created_at'))}, expires "
                      f"{safe(meta.get('expires_at'))}: {delta / 86400:.4f} days, {retention} expected")
            left = (expires - dt.datetime.now(dt.timezone.utc)).total_seconds()
            rep.info("1.expiry", f"time to expiry at validation: {left / 3600:.1f} h")
        except (KeyError, ValueError, TypeError) as e:
            rep.unv("1.expiry", f"staging/expiry times unreadable ({type(e).__name__})")
    # outer zip: testzip, names, fresh extraction
    if c.zip_hash is not None:
        if extract_zip(a.zip, a.extract_to, rep):
            c.root = a.extract_to
    elif a.dir:
        rep.unv("1.testzip", "no artifact zip given; the content checks read a pre-extracted directory")
        if os.path.isdir(a.dir):
            c.root = a.dir
        else:
            rep.unv("1.extract", "directory absent")


def unsafe_reason(info):
    n = info.filename
    if not n or "\x00" in n or "\\" in n or n.startswith("/") or re.match(r"^[A-Za-z]:", n):
        return "absolute or malformed path"
    parts = n[:-1].split("/") if n.endswith("/") else n.split("/")
    if any(p in ("", ".", "..") for p in parts):
        return "'..', '.' or empty component"
    mode = (info.external_attr >> 16) & 0o170000
    if mode and mode not in (stat.S_IFREG, stat.S_IFDIR):
        return "not a regular file or directory"
    return None


def extract_zip(zpath, dest, rep):
    try:
        z = zipfile.ZipFile(zpath)
    except (zipfile.BadZipFile, OSError, ValueError) as e:
        rep.fail("1.testzip", f"not a readable zip ({type(e).__name__})")
        return False
    with z:
        infos = z.infolist()
        try:
            bad = z.testzip()
        except ZIP_ERRORS as e:
            bad = f"#{type(e).__name__}"
        if bad is not None:
            rep.fail("1.testzip", f"testzip reports a bad member ({len(infos)} members)")
            return False
        rep.ok("1.testzip", f"{len(infos)} members, every CRC ok")
        problems = [(i, r) for i, r in ((i, unsafe_reason(x)) for i, x in enumerate(infos)) if r]
        names = [x.filename for x in infos]
        dups = len(names) - len(set(names))
        if problems or dups or len(infos) > MAX_MEMBERS:
            rep.fail("1.names", f"{len(problems)} unsafe member names (first: member #{problems[0][0]}, "
                                f"{problems[0][1]}); {dups} duplicates" if problems else
                     f"{dups} duplicate member names; {len(infos)} members")
            return False
        rep.ok("1.names", "no absolute path, '..', link or duplicate among the member names")
        if not dest:
            rep.unv("1.extract", "no --extract-to directory given")
            return False
        if os.path.lexists(dest) and (not os.path.isdir(dest) or os.listdir(dest)):
            rep.unv("1.extract", "the extraction directory is not fresh (exists and is not empty)")
            return False
        os.makedirs(dest, exist_ok=True)
        real = os.path.realpath(dest)
        total = files = 0
        try:
            for info in infos:
                rel = info.filename[:-1] if info.is_dir() else info.filename
                target = os.path.join(dest, *rel.split("/"))
                if not os.path.realpath(target).startswith(real + os.sep):
                    raise ValueError("escape")
                if info.is_dir():
                    os.makedirs(target, exist_ok=True)
                    continue
                total += info.file_size
                if total > MAX_EXTRACT_BYTES:
                    raise ValueError("too large")
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with z.open(info) as src, open(target, "xb") as dst:
                    shutil.copyfileobj(src, dst, 1 << 20)
                files += 1
        except ZIP_ERRORS as e:
            rep.fail("1.extract", f"extraction failed ({type(e).__name__})")
            return False
        rep.ok("1.extract", f"{files} files, {total} bytes, extracted into a fresh directory")
        return True


# ----------------------------------------------------------------------------------------------- records

def read_fetch_log(path):
    """Returns (last records by key, number of lines, superseded count, problems)."""
    with open(path, "rb") as f:
        data = f.read()
    last, problems, n, superseded = {}, [], 0, 0
    lines = data.split(b"\n")
    if lines and lines[-1] == b"":
        lines.pop()
    for i, raw in enumerate(lines, 1):
        n += 1
        try:
            obj = json.loads(raw)
        except ValueError:
            problems.append(f"line {i}: not JSON")
            continue
        if not isinstance(obj, dict) or not isinstance(obj.get(KEY_FIELD), str):
            fields = sorted(obj)[:12] if isinstance(obj, dict) else type(obj).__name__
            problems.append(f"line {i}: no '{KEY_FIELD}' field (fields: {safe(fields, 200)})")
            continue
        if obj[KEY_FIELD] in last:
            superseded += 1
        last[obj[KEY_FIELD]] = obj
    return last, n, superseded, problems


def strip_key(rec):
    return {k: v for k, v in rec.items() if k != KEY_FIELD}


def load_records(rep, c):
    root = c.root
    c.records = c.manifest = c.completeness = c.scanjson = None
    c.fetch_problems = []
    p = os.path.join(root, "fetch-log.jsonl")
    if os.path.isfile(p):
        try:
            c.records, c.fetch_lines, c.fetch_superseded, c.fetch_problems = read_fetch_log(p)
        except OSError as e:
            c.fetch_problems = [f"unreadable ({type(e).__name__})"]
    for attr, name in (("manifest", "manifest.json"), ("completeness", "completeness.json"),
                       ("scanjson", "scan.json")):
        obj, err = load_json(os.path.join(root, name))
        setattr(c, attr, obj)
        setattr(c, attr + "_err", err)


# ----------------------------------------------------------------------------------------------- 2: expected sets

def derive_expected(a, rep, c):
    """Fills c.attempts {run: n}, c.jobs {(run, n): [projected jobs]}, c.host_runs, c.exp_* sets."""
    c.expected_ok = False
    c.source = None
    if c.batch is None or c.inv_runs is None or c.inv_jobs is None:
        rep.unv("2.expected", "batch.json or the inventory is unavailable")
        return
    run_ids = [str(r) for r in c.batch["run_ids"]]
    mode = c.batch.get("job_logs")
    missing_inv = [r for r in run_ids if r not in c.inv_runs]
    if missing_inv:
        rep.fail("2.expected", f"batch runs absent from the inventory: {missing_inv}")
        return
    c.run_ids, c.attempts, c.jobs, c.host_runs, c.host_attempts = run_ids, {}, {}, {}, {}
    if a.host:
        c.source = "host"
        for r in run_ids:
            run, err = load_json(os.path.join(a.host, f"run-{r}.json"))
            if err or not isinstance(run, dict) or "run_attempt" not in run:
                rep.unv("2.expected", f"host run record for {r}: {err or 'malformed'}")
                return
            c.host_runs[r] = run
            n = int(run["run_attempt"])
            c.attempts[r] = n
            for k in range(1, n + 1):
                att, err = load_json(os.path.join(a.host, f"run-{r}-attempt-{k}.json"))
                if err or not isinstance(att, dict) or str(att.get("run_attempt")) != str(k):
                    rep.unv("2.expected", f"host attempt record for {r} attempt {k}: "
                                          f"{err or 'malformed or for another attempt'}")
                    return
                c.host_attempts[(r, k)] = att
                jl, err = load_json(os.path.join(a.host, f"jobs-{r}-attempt-{k}.json"))
                if err or not isinstance(jl, dict) or not isinstance(jl.get("jobs"), list):
                    rep.unv("2.expected", f"host job list for {r} attempt {k}: {err or 'malformed'}")
                    return
                ids = [sid(j.get("id")) for j in jl["jobs"]]
                if len(ids) != jl.get("total_count") or len(set(ids)) != len(ids):
                    rep.unv("2.expected", f"host job list for {r} attempt {k} is incomplete: {len(ids)} jobs "
                                          f"(unique {len(set(ids))}) vs total_count {safe(jl.get('total_count'))}")
                    return
                c.jobs[(r, k)] = [project(j) for j in jl["jobs"]]
    else:
        c.source = "records"
        rep.unv("2.expected", "no host job lists: the expected sets below come from the archiver's own records, "
                              "which cannot verify themselves")
        if c.records is None:
            return
        for r in run_ids:
            rr = c.records.get(f"run:{r}")
            if not rr or not str(rr.get("run_attempt", "")).isdigit():
                rep.unv("2.expected", f"no usable run record for {r}")
                return
            c.attempts[r] = int(rr["run_attempt"])
            for k in range(1, c.attempts[r] + 1):
                jr = c.records.get(f"jobs:{r}:{k}")
                if not jr or not isinstance(jr.get("jobs"), list):
                    rep.unv("2.expected", f"no usable job record for {r} attempt {k}")
                    return
                c.jobs[(r, k)] = [project(j) for j in jr["jobs"]]
    # classification
    unsettled = [(r, k, j["id"]) for (r, k), js in c.jobs.items() for j in js if j["status"] != "completed"]
    if unsettled:
        rep.fail("2.expected", f"{len(unsettled)} jobs not completed (first: run {unsettled[0][0]} attempt "
                               f"{unsettled[0][1]} job {unsettled[0][2]})")
        return
    c.copies, c.exp_top, c.exp_joblogs, c.job_attempt = {}, {}, set(), {}
    for r in run_ids:
        first_seen = {}
        for k in range(1, c.attempts[r] + 1):
            js = c.jobs[(r, k)]
            for j in js:
                c.job_attempt.setdefault(j["id"], (r, k))
                sig = (j["name"], j["started_at"], j["completed_at"], j["runner_id"])
                if k > 1 and sig in first_seen and first_seen[sig] != j["id"]:
                    c.copies[j["id"]] = first_seen[sig]
            for j in js:
                first_seen.setdefault((j["name"], j["started_at"], j["completed_at"], j["runner_id"]), j["id"])
            c.exp_top[(r, k)] = [j for j in js if ran(j) and j["id"] not in c.copies]
            for j in js:
                if ran(j):
                    c.exp_joblogs.add(j["id"])
            nr = sum(ran(j) for j in js)
            rep.info("2.expected", f"run {r} attempt {k}: {len(js)} jobs, {nr} ran, "
                                   f"{sum(j['conclusion'] == 'skipped' for j in js)} skipped, "
                                   f"{sum(not ran(j) and j['conclusion'] != 'skipped' for j in js)} without a runner, "
                                   f"{sum(j['id'] in c.copies for j in js)} copies of an earlier attempt; "
                                   f"{len(c.exp_top[(r, k)])} expected in the zip")
    cited = {r["job_id"] for r in c.inv_jobs if r.get("run_id") in set(run_ids)}
    if mode == "all":
        bad = sorted(cited - c.exp_joblogs)
        if bad:
            rep.fail("2.expected", f"inventory cites jobs of these runs that did not run: {bad[:10]}")
            return
    elif mode == "cited":
        bad = sorted(cited - c.exp_joblogs)
        if bad:
            rep.fail("2.expected", f"cited jobs that did not run: {bad[:10]}")
            return
        c.exp_joblogs = cited
    else:
        rep.fail("2.expected", f"unsupported job_logs mode {safe(mode)}")
        return
    c.exp_files = set(META_FILES)
    c.exp_files |= {f"runs/{r}/attempt-{k}.zip" for r in run_ids for k in range(1, c.attempts[r] + 1)}
    c.exp_files |= {f"jobs/{j}.txt" for j in c.exp_joblogs}
    c.exp_keys = {f"run:{r}" for r in run_ids}
    c.exp_keys |= {f"{kind}:{r}:{k}" for kind in ("jobs", "zip") for r in run_ids for k in range(1, c.attempts[r] + 1)}
    c.exp_keys |= {f"joblog:{j}" for j in c.exp_joblogs}
    nz = sum(c.attempts.values())
    if c.source == "host":
        rep.ok("2.expected", f"from batch ({len(run_ids)} runs, job_logs={mode}), inventory and host job lists: "
                             f"{len(c.exp_files)} files = {nz} zips + {len(c.exp_joblogs)} job logs + "
                             f"{len(META_FILES)} metadata; {sum(len(v) for v in c.exp_top.values())} top-level zip logs")
    else:
        rep.info("2.expected", f"from the records: {len(c.exp_files)} files = {nz} zips + {len(c.exp_joblogs)} "
                               f"job logs + {len(META_FILES)} metadata")
    c.expected_ok = True


def check_fileset(rep, c):
    actual, odd = set(), 0
    for dirpath, dirnames, filenames in os.walk(c.root):
        for n in filenames + [d for d in dirnames if os.path.islink(os.path.join(dirpath, d))]:
            p = os.path.join(dirpath, n)
            rel = os.path.relpath(p, c.root).replace(os.sep, "/")
            if os.path.islink(p) or not os.path.isfile(p):
                odd += 1
            actual.add(rel)
    c.actual_files = actual
    if not c.expected_ok:
        rep.unv("2.files", f"{len(actual)} files present; no verified expected set to compare with")
        return
    missing, extra = sorted(c.exp_files - actual), sorted(actual - c.exp_files)
    nz = sum(1 for f in actual if f.startswith("runs/"))
    nj = sum(1 for f in actual if f.startswith("jobs/"))
    ok = not missing and not extra and not odd
    rep.check("2.files", ok,
              f"exactly the {len(actual)} expected files: {nz} zips, {nj} job logs, "
              f"{len(actual) - nz - nj} metadata",
              f"{len(missing)} missing, {len(extra)} extra, {odd} not regular; missing: "
              f"{[safe(x, 60) for x in missing[:8]]} extra: {[safe(x, 60) for x in extra[:8]]}")


# ----------------------------------------------------------------------------------------------- 3: records

def check_records(rep, c):
    root = c.root
    # fetch log
    if c.records is None:
        rep.fail("3.fetchlog", "fetch-log.jsonl absent or unreadable"
                 if not c.fetch_problems else f"fetch-log.jsonl: {c.fetch_problems[0]}")
        return
    probs = list(c.fetch_problems)
    for k, rec in c.records.items():
        kind = k.split(":", 1)[0]
        if kind not in KEY_RES or not KEY_RES[kind].match(k):
            probs.append(f"unknown key form {safe(k, 40)}")
        elif rec.get("outcome") != OUTCOME[kind]:
            probs.append(f"{safe(k, 40)}: outcome {safe(rec.get('outcome'), 20)}, spec says {OUTCOME[kind]}")
    if c.expected_ok:
        miss, extra = sorted(c.exp_keys - set(c.records)), sorted(set(c.records) - c.exp_keys)
        if miss:
            probs.append(f"{len(miss)} expected keys without a record (first {safe(miss[0], 40)})")
        if extra:
            probs.append(f"{len(extra)} records for unexpected keys (first {safe(extra[0], 40)})")
    rep.check("3.fetchlog", not probs,
              f"{c.fetch_lines} lines, {len(c.records)} keys ({c.fetch_superseded} superseded lines); "
              f"every key and outcome as specified" + ("; key set = expected" if c.expected_ok else ""),
              f"{len(probs)} problems; first: {probs[0] if probs else ''}")
    if not c.expected_ok:
        rep.unv("3.fetchlog", "key set not compared: no verified expected set")
    # manifest
    m = c.manifest
    man_items = None
    if not isinstance(m, dict) or "items" not in m:
        rep.fail("3.manifest", f"manifest.json {c.manifest_err or 'has no items'}")
    else:
        items = m["items"]
        man_items, bad = {}, 0
        if isinstance(items, dict):
            for k, v in items.items():
                if not isinstance(v, dict) or (KEY_FIELD in v and v[KEY_FIELD] != k):
                    bad += 1
                else:
                    man_items[k] = strip_key(v)
        elif isinstance(items, list):
            for v in items:
                if not isinstance(v, dict) or not isinstance(v.get(KEY_FIELD), str) or v[KEY_FIELD] in man_items:
                    bad += 1
                else:
                    man_items[v[KEY_FIELD]] = strip_key(v)
        else:
            bad = 1
        fl = {k: strip_key(v) for k, v in c.records.items()}
        diff_keys = sorted(set(fl) ^ set(man_items))
        diff_vals = sorted(k for k in set(fl) & set(man_items) if fl[k] != man_items[k])
        fields = sorted({f for k in diff_vals for f in set(fl[k]) | set(man_items[k])
                         if fl[k].get(f) != man_items[k].get(f)})
        rep.check("3.manifest", not bad and not diff_keys and not diff_vals,
                  f"{len(man_items)} items equal the fetch log's last records",
                  f"{bad} malformed items, {len(diff_keys)} keys in one only, {len(diff_vals)} records differ "
                  f"(fields: {fields[:10]})")
        rm = m.get("rehash_mismatches")
        rep.check("3.rehash", rm == [], "rehash_mismatches is empty",
                  f"rehash_mismatches is {'non-empty (' + str(len(rm)) + ')' if isinstance(rm, list) else 'absent or not a list'}")
        counts = m.get("counts")
        if isinstance(counts, dict):
            flat = {k: v for k, v in counts.items() if isinstance(v, (int, str, bool)) or v is None}
            rep.info("3.manifest", f"counts: {safe(json.dumps(flat, sort_keys=True), 300)}")
    # completeness and scan
    cp = c.completeness
    if not isinstance(cp, dict):
        rep.fail("3.completeness", f"completeness.json {c.completeness_err or 'not an object'}")
    else:
        mi = cp.get("missing_or_incomplete")
        rep.check("3.completeness", cp.get("complete") is True and mi in ([], {}, 0),
                  "complete is true and missing_or_incomplete is empty",
                  f"complete={safe(cp.get('complete'))}, missing_or_incomplete has "
                  f"{len(mi) if isinstance(mi, (list, dict)) else safe(mi)} entries")
        req, its = cp.get("required"), cp.get("items")
        rep.info("3.completeness", f"required: {len(req) if isinstance(req, (list, dict)) else safe(req)}; "
                                   f"items: {len(its) if isinstance(its, (list, dict)) else safe(its)}")
    rep.check("3.scanjson", c.scanjson == [] and c.scanjson_err is None, "scan.json is []",
              f"scan.json is {'unreadable' if c.scanjson_err else 'not []'}"
              + (f" ({len(c.scanjson)} entries)" if isinstance(c.scanjson, list) else ""))
    # files against their records
    mism, empty, checked, sized = [], [], 0, {}
    for k, rec in sorted(c.records.items()):
        kind = k.split(":", 1)[0]
        if kind not in ("zip", "joblog") or not KEY_RES[kind].match(k):
            continue
        g = KEY_RES[kind].match(k).groups()
        want = f"runs/{g[0]}/attempt-{g[1]}.zip" if kind == "zip" else f"jobs/{g[0]}.txt"
        p = os.path.join(root, *want.split("/"))
        if rec.get("path") != want:
            mism.append(f"{safe(k, 40)}: path {safe(rec.get('path'), 60)}")
            continue
        if not os.path.isfile(p):
            mism.append(f"{want}: recorded but absent")
            continue
        size, h = sha256_file(p)
        sized[want] = (size, h)
        checked += 1
        mrec = (man_items or {}).get(k, {})
        if rec.get("bytes") != size or rec.get("sha256") != h:
            mism.append(f"{want}: fetch-log record {'size' if rec.get('bytes') != size else 'sha256'} differs")
        if man_items is not None and (mrec.get("bytes") != size or mrec.get("sha256") != h):
            mism.append(f"{want}: manifest item differs")
        if size == 0:
            empty.append(want)
    unrecorded = sorted(f for f in c.actual_files if f not in META_FILES and f not in sized)
    rep.check("3.files", not mism and not empty and not unrecorded,
              f"{checked} archived files: size and sha256 equal their fetch-log record and manifest item; none empty",
              f"{len(mism)} mismatches, {len(empty)} empty, {len(unrecorded)} without a record; first: "
              f"{(mism + [e + ': empty' for e in empty] + [u + ': no record' for u in unrecorded] + [''])[0]}")
    c.sized = sized
    # job log line counts: one definition must fit every job log
    defs = {"count of LF": lambda d: d.count(b"\n"),
            "LF-terminated lines + unterminated tail": lambda d: d.count(b"\n") + (1 if d and not d.endswith(b"\n") else 0),
            "bytes.splitlines": lambda d: len(d.splitlines()),
            "str.splitlines (UTF-8)": lambda d: len(d.decode("utf-8", "replace").splitlines())}
    # The spec does not define `lines`. A log on which the candidate definitions agree checks the record exactly;
    # the logs on which they disagree must all fit one definition, and pin it only when there are two or more.
    fits = {n: 0 for n in defs}
    total = distinguishing = 0
    for k, rec in c.records.items():
        if not k.startswith("joblog:") or rec.get("path") not in sized:
            continue
        with open(os.path.join(root, *rec["path"].split("/")), "rb") as f:
            d = f.read()
        total += 1
        vals = {n: fn(d) for n, fn in defs.items()}
        distinguishing += len(set(vals.values())) > 1
        for n, v in vals.items():
            fits[n] += v == rec.get("lines")
    good = [n for n, v in fits.items() if v == total]
    rep.check("3.lines", total > 0 and bool(good),
              f"{total} job-log line counts all fit: {', '.join(good)} "
              f"({distinguishing} logs distinguish the candidate definitions)",
              f"no single line-count definition fits all {total} job logs (best fits {max(fits.values() or [0])}; "
              f"{distinguishing} logs distinguish the definitions)")
    if distinguishing < 2:
        rep.info("3.lines", f"only {distinguishing} log(s) distinguish the definitions: a count off by exactly that "
                            f"ambiguity on such a log would not be detected")
    # run and job records against the host
    if not c.expected_ok:
        rep.unv("3.run-records", "no verified host records to compare")
        rep.unv("3.jobs-records", "no verified host job lists to compare")
        return
    for r in c.run_ids:
        rr = c.records.get(f"run:{r}") or {}
        if c.source != "host":
            rep.unv("3.run-records", f"run {r}: no host run record to compare")
        else:
            rep.check("3.run-records", str(rr.get("run_attempt")) == str(c.attempts[r]),
                      f"run {r}: run_attempt {safe(rr.get('run_attempt'))} as the host says",
                      f"run {r}: record run_attempt {safe(rr.get('run_attempt'))}, host {c.attempts[r]}")
        for k in range(1, c.attempts.get(r, 0) + 1):
            jr = c.records.get(f"jobs:{r}:{k}") or {}
            if c.source != "host":
                rep.unv("3.jobs-records", f"run {r} attempt {k}: no host job list to compare")
                continue
            got = jr.get("jobs")
            if not isinstance(got, list):
                rep.fail("3.jobs-records", f"run {r} attempt {k}: no job list in the record")
                continue
            gp = {}
            dup = 0
            for j in got:
                if not isinstance(j, dict):
                    dup += 1
                    continue
                pj = project(j)
                dup += pj["id"] in gp
                gp[pj["id"]] = pj
            hp = {j["id"]: j for j in c.jobs[(r, k)]}
            diff = sorted(i for i in set(gp) | set(hp) if gp.get(i) != hp.get(i))
            fields = sorted({f for i in diff if i in gp and i in hp for f in JOB_FIELDS if gp[i][f] != hp[i][f]})
            rep.check("3.jobs-records", not diff and not dup,
                      f"run {r} attempt {k}: {len(gp)} jobs equal the host list on {len(JOB_FIELDS)} fields",
                      f"run {r} attempt {k}: {len(diff)} jobs differ from the host list (fields {fields}; "
                      f"{len(set(gp) - set(hp))} only in record, {len(set(hp) - set(gp))} only on host), {dup} malformed")


# ----------------------------------------------------------------------------------------------- 4: zips

def inner_zip(data):
    z = zipfile.ZipFile(io.BytesIO(data))
    out = {"bad": None, "members": [], "names": [], "blobs": {}}
    with z:
        infos = z.infolist()
        out["names"] = [i.filename for i in infos]
        try:
            out["bad"] = z.testzip()
        except ZIP_ERRORS as e:
            out["bad"] = f"#{type(e).__name__}"
        for i in infos:
            if i.is_dir():
                continue
            try:
                b = z.read(i)
            except ZIP_ERRORS:
                out["members"].append((i.filename, i.file_size, None))
                continue
            out["blobs"][i.filename] = b
            out["members"].append((i.filename, len(b), sha256_bytes(b)))
    out["members"].sort()
    return out


def as_count(v):
    if isinstance(v, bool):
        return None
    if isinstance(v, int):
        return v
    if isinstance(v, (list, dict)):
        return len(v)
    return None


def check_zips(rep, c):
    c.inner = {}
    if not c.expected_ok:
        rep.unv("4.zips", "no verified expected set")
        return
    for r in c.run_ids:
        for k in range(1, c.attempts[r] + 1):
            rel = f"runs/{r}/attempt-{k}.zip"
            p = os.path.join(c.root, "runs", r, f"attempt-{k}.zip")
            if not os.path.isfile(p):
                rep.info("4.zips", f"{rel}: absent (see 2.files)")
                continue
            with open(p, "rb") as f:
                data = f.read()
            try:
                iz = inner_zip(data)
            except ZIP_ERRORS as e:
                rep.fail("4.testzip", f"{rel}: not a readable zip ({type(e).__name__})")
                continue
            c.inner[(r, k)] = iz
            names = iz["names"]
            rep.check("4.testzip", iz["bad"] is None and len(names) == len(set(names)),
                      f"{rel}: testzip ok, no duplicate names",
                      f"{rel}: testzip reports a bad member" if iz["bad"] is not None else f"{rel}: duplicate names")
            rec = (c.records or {}).get(f"zip:{r}:{k}") or {}
            recm = rec.get("members")
            try:
                recm_t = sorted((m["name"], m["size"], m["sha256"]) for m in recm)
            except (TypeError, KeyError):
                recm_t = None
            if recm_t is None:
                rep.fail("4.members", f"{rel}: the record has no usable member list")
            else:
                d = sorted(set(recm_t) ^ set(iz["members"]))
                rep.check("4.members", recm_t == iz["members"],
                          f"{rel}: {len(iz['members'])} members (name, size, sha256) equal the record",
                          f"{rel}: {len(d)} member entries differ (first {safe(d[0][0], 80) if d else ''}); "
                          f"zip {len(iz['members'])}, record {len(recm_t)}")
            top = [n for n in names if "/" not in n and TOP_RE.match(n)]
            other = [n for n in names if "/" not in n and not TOP_RE.match(n) and not n.endswith("/")]
            steps = [n for n in names if "/" in n and not n.endswith("/")]
            exp = len(c.exp_top[(r, k)])
            iz["top"] = top
            rep.info("4.zips", f"{rel}: members {len(iz['members'])}, top-level job logs {len(top)}, expected {exp}, "
                               f"step logs {len(steps)}, other top-level {len(other)}")
            rep.check("4.toplevel", len(top) == exp, f"{rel}: {len(top)} top-level job logs = {exp} jobs that ran "
                                                      f"in this attempt (not copies)",
                      f"{rel}: {len(top)} top-level job logs, {exp} expected")
            tl, le = as_count(rec.get("top_level_job_logs")), as_count(rec.get("logs_expected"))
            ok = rec.get("crc_ok") is True and rec.get("complete") is True and tl == len(top) and le == exp
            rep.check("4.record", ok, f"{rel}: record crc_ok, complete, top_level_job_logs {tl}, logs_expected {le}",
                      f"{rel}: record crc_ok={safe(rec.get('crc_ok'))} complete={safe(rec.get('complete'))} "
                      f"top_level_job_logs={tl} (zip {len(top)}) logs_expected={le} (validator {exp})")


# ----------------------------------------------------------------------------------------------- 5: heads

def check_heads(rep, c):
    if not c.expected_ok:
        rep.unv("5.heads", "no verified run and job records to compare")
        return
    for r in c.run_ids:
        src = {"inventory": c.inv_runs[r].get("head_sha")}
        rr = (c.records or {}).get(f"run:{r}") or {}
        src["fetch-log run"] = rr.get("head_sha")
        src["fetch-log inventory_head_sha"] = rr.get("inventory_head_sha")
        recjobs = {j.get("head_sha") for k in range(1, c.attempts.get(r, 0) + 1)
                   for j in (((c.records or {}).get(f"jobs:{r}:{k}") or {}).get("jobs") or []) if isinstance(j, dict)}
        for i, h in enumerate(sorted(recjobs, key=str)):
            src[f"fetch-log jobs #{i}"] = h
        if c.source == "host":
            src["host run"] = c.host_runs[r].get("head_sha")
            for k in range(1, c.attempts[r] + 1):
                src[f"host attempt {k}"] = c.host_attempts[(r, k)].get("head_sha")
            for i, h in enumerate(sorted({j["head_sha"] for k in range(1, c.attempts[r] + 1)
                                          for j in c.jobs[(r, k)]}, key=str)):
                src[f"host jobs #{i}"] = h
        vals = set(src.values())
        flag = rr.get("head_matches_inventory")
        ok = len(vals) == 1 and None not in vals and flag is True
        rep.check("5.heads", ok, f"run {r}: {next(iter(vals))} in all {len(src)} sources; head_matches_inventory true",
                  f"run {r}: {len(vals)} distinct heads across {len(src)} sources "
                  f"({', '.join(f'{k}={safe(v)[:12]}' for k, v in src.items())}); head_matches_inventory={safe(flag)}")
        if c.source != "host":
            rep.unv("5.heads", f"run {r}: no host run record")


# ----------------------------------------------------------------------------------------------- 6: cross-representation

def check_cross(rep, c):
    if not c.expected_ok or not c.inner:
        rep.unv("6.map", "no verified expected set or no zips")
        return
    ident = differ = unmapped = ambiguous = 0
    for (r, k), iz in sorted(c.inner.items()):
        rel = f"runs/{r}/attempt-{k}.zip"
        by = {}
        for j in c.jobs[(r, k)]:
            by.setdefault(norm_name(j["name"]), []).append(j)
        exp_ids = {j["id"] for j in c.exp_top[(r, k)]}
        mapped, bad, um, amb = {}, [], 0, 0
        for m in iz.get("top", []):
            cands = by.get(norm_name(TOP_RE.match(m).group(2)), [])
            if len(cands) == 1:
                mapped[m] = cands[0]["id"]
            elif cands:
                amb += 1
            else:
                um += 1
        # two logs naming one job is a naming question, not an exact identification: ambiguous, not gating
        hits = {}
        for m, jid in mapped.items():
            hits.setdefault(jid, []).append(m)
        for jid, ms in hits.items():
            if len(ms) > 1:
                amb += len(ms)
                for m in ms:
                    del mapped[m]
        # a log whose name identifies exactly one job, and that job is not expected here, is exact: gating
        for m, jid in sorted(mapped.items()):
            if jid not in exp_ids:
                bad.append(f"{safe(m, 60)} -> job {jid} ({'copy' if jid in c.copies else 'did not run'})")
        unmapped += um
        ambiguous += amb
        rep.check("6.map", not bad,
                  f"{rel}: {len(mapped)} top-level logs map by name to {len(set(mapped.values()))} expected jobs; "
                  f"{um} unmatched, {amb} ambiguous (not gating)",
                  f"{rel}: {len(bad)} top-level logs identify a job not expected in this zip; first: "
                  f"{bad[0] if bad else ''}")
        for m, jid in sorted(mapped.items()):
            p = os.path.join(c.root, "jobs", f"{jid}.txt")
            if jid not in exp_ids or not os.path.isfile(p):
                continue
            with open(p, "rb") as f:
                per = f.read()
            zb = iz["blobs"].get(m)
            if zb is None:
                continue
            if zb == per:
                ident += 1
            else:
                differ += 1
                rel_ = "zip is a prefix of the per-job log" if per.startswith(zb) else \
                    "per-job log is a prefix of the zip" if zb.startswith(per) else "neither is a prefix of the other"
                rep.info("6.bytes", f"job {jid}: zip {len(zb)} bytes, per-job {len(per)} bytes "
                                    f"(diff {len(zb) - len(per):+d}); {rel_}")
    rep.info("6.bytes", f"top-level zip logs vs per-job logs: {ident} byte-identical, {differ} differ, "
                        f"{unmapped} unmatched, {ambiguous} ambiguous")
    same, diff = [], []
    for cid, oid in sorted(c.copies.items()):
        pc, po = os.path.join(c.root, "jobs", f"{cid}.txt"), os.path.join(c.root, "jobs", f"{oid}.txt")
        if not (os.path.isfile(pc) and os.path.isfile(po)):
            continue
        with open(pc, "rb") as f1, open(po, "rb") as f2:
            a_, b_ = f1.read(), f2.read()
        if a_ == b_:
            same.append(f"{cid}={oid}")
        else:
            diff.append(f"{cid} vs {oid}: {len(a_) - len(b_):+d} bytes, "
                        f"{'prefix' if a_.startswith(b_) or b_.startswith(a_) else 'not a prefix'}")
    rep.info("6.copies", f"per-job logs of copied jobs: {len(same)} byte-identical to their originals, "
                         f"{len(diff)} differ")
    for i in range(0, len(same), 4):
        rep.info("6.copies", "identical (copy=original): " + " ".join(same[i:i + 4]))
    for d in diff:
        rep.info("6.copies", "differs: " + d)


# ----------------------------------------------------------------------------------------------- 7: scan

def scan_bytes(data):
    hits = []
    for name, rx in SCAN_RES:
        for m in rx.finditer(data):
            hits.append((name, m.start(), data.count(b"\n", 0, m.start()) + 1))
    return hits


def check_scan(rep, c):
    hits, nfiles, nmembers, nbytes = [], 0, 0, 0
    for dirpath, _, filenames in os.walk(c.root):
        for n in sorted(filenames):
            p = os.path.join(dirpath, n)
            rel = os.path.relpath(p, c.root).replace(os.sep, "/")
            if os.path.islink(p):
                continue
            with open(p, "rb") as f:
                data = f.read()
            nfiles += 1
            nbytes += len(data)
            hits += [(rel, None, *h) for h in scan_bytes(data)]
            hits += [(rel, "(path)", *h) for h in scan_bytes(rel.encode())]
            if n.endswith(".zip"):
                try:
                    with zipfile.ZipFile(io.BytesIO(data)) as z:
                        names = z.namelist()
                        hits += [(rel, "(member names)", *h) for h in scan_bytes("\n".join(names).encode())]
                        for i in z.infolist():
                            if i.is_dir():
                                continue
                            try:
                                b = z.read(i)
                            except ZIP_ERRORS:
                                rep.unv("7.scan", f"{rel}: a member could not be decompressed for the scan")
                                continue
                            nmembers += 1
                            nbytes += len(b)
                            hits += [(rel, i.filename, *h) for h in scan_bytes(b)]
                except ZIP_ERRORS:
                    rep.unv("7.scan", f"{rel}: not a readable zip; its members were not scanned")
    rep.check("7.scan", not hits,
              f"{nfiles} files and {nmembers} zip members ({nbytes} bytes) against {len(SCAN_RES)} patterns: no hits",
              f"{len(hits)} credential-shaped hits (locations below, content not shown)")
    for f, m, name, off, line in hits[:50]:
        rep.info("7.scan", f"hit pattern={name} file={safe(f, 80)}" + (f" member={safe(m, 80)}" if m else "")
                 + f" line={line} offset={off}")
    if len(hits) > 50:
        rep.info("7.scan", f"... {len(hits) - 50} more hits")


# ----------------------------------------------------------------------------------------------- driver

CONTENT_CHECKS = ("2.files", "3.records", "4.zips", "5.heads", "6.map", "7.scan")


def validate(a, out=None):
    rep = Report(out)
    c = Ctx()
    c.meta, c.meta_err = load_json(a.metadata)
    if c.meta is not None and not isinstance(c.meta, dict):
        c.meta, c.meta_err = None, "not an object"
    c.zip_hash = None
    zip_note = "no zip given"
    if a.zip:
        if os.path.isfile(a.zip):
            c.zip_hash = sha256_file(a.zip)
        else:
            zip_note = "zip absent (download failed or not run)"
    env = os.environ
    rep.head("validator commit", a.validator_commit or env.get("GITHUB_SHA") or "(not in GitHub Actions)")
    rep.head("workflow run", f"{a.workflow_run or env.get('GITHUB_RUN_ID') or '-'} attempt "
                             f"{a.workflow_attempt or env.get('GITHUB_RUN_ATTEMPT') or '-'}")
    rep.head("source run", a.source_run_id)
    rep.head("artifact id", a.artifact_id)
    rep.head("expected digest", (c.meta or {}).get("digest") or f"unavailable (metadata {c.meta_err})")
    rep.head("computed digest", f"sha256:{c.zip_hash[1]}" if c.zip_hash else f"unavailable ({zip_note})")
    rep.head("expected size", (c.meta or {}).get("size_in_bytes", f"unavailable (metadata {c.meta_err})"))
    rep.head("computed size", c.zip_hash[0] if c.zip_hash else f"unavailable ({zip_note})")
    for n in ("validate_artifact.py", "download_artifact_zip.py", "fetch_host_records.py"):
        p = os.path.join(HERE, n)
        rep.head("validator file", f"{n} sha256={sha256_file(p)[1] if os.path.isfile(p) else 'absent'}")
    for label, p in (("batch.json", a.batch), ("inventory-runs.csv", a.inventory_runs),
                     ("inventory-jobs.csv", a.inventory_jobs)):
        rep.head("input", f"{label} sha256={sha256_file(p)[1] if p and os.path.isfile(p) else 'unavailable'}")
    rep.head("expected-set source", "host job lists and run records (independent of the archiver)" if a.host
             else "the archiver's own records (not independent)")
    print("", file=rep.out)
    try:
        check_inputs(a, rep, c)
        check_artifact(a, rep, c)
        if c.root is None:
            for cid in CONTENT_CHECKS:
                rep.unv(cid, "no verified artifact content to check")
        else:
            load_records(rep, c)
            derive_expected(a, rep, c)
            check_fileset(rep, c)
            check_records(rep, c)
            check_zips(rep, c)
            check_heads(rep, c)
            check_cross(rep, c)
            check_scan(rep, c)
    except Exception as e:  # fail closed: an unexpected state is unverified, never a pass
        tb = traceback.extract_tb(e.__traceback__)
        rep.unv("internal", f"validator stopped on {type(e).__name__} at line {tb[-1].lineno if tb else '?'}")
    line, code = rep.verdict()
    print("", file=rep.out)
    print(f"summary: {sum(s == 'PASS' for s, _, _ in rep.rows)} PASS, {len(rep.failed_ids())} FAIL, "
          f"{len(rep.unverified_ids())} UNVERIFIED", file=rep.out)
    print(line, file=rep.out)
    return rep, code


def parser():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--zip", help="the artifact zip as downloaded")
    ap.add_argument("--extract-to", help="a fresh directory to extract the zip into")
    ap.add_argument("--dir", help="a pre-extracted artifact directory (when no zip is available)")
    ap.add_argument("--download-record", help="the downloader's record (JSON)")
    ap.add_argument("--metadata", help="the artifact's API metadata (JSON)")
    ap.add_argument("--batch")
    ap.add_argument("--inventory-runs")
    ap.add_argument("--inventory-jobs")
    ap.add_argument("--host", help="directory of host run records and job lists (fetch_host_records.py)")
    ap.add_argument("--expect-input-sha256", action="append", metavar="NAME=HEX")
    ap.add_argument("--repo", default=PILOT["repo"])
    ap.add_argument("--artifact-id", default=PILOT["artifact_id"])
    ap.add_argument("--source-run-id", default=PILOT["source_run_id"])
    ap.add_argument("--source-head-sha", default=PILOT["source_head_sha"])
    ap.add_argument("--validator-commit")
    ap.add_argument("--workflow-run")
    ap.add_argument("--workflow-attempt")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work", help="parent directory for self-test scratch files")
    return ap


def main(argv=None):
    a = parser().parse_args(argv)
    if a.self_test:
        return 1 if self_test(a.work) else 0
    if a.zip and a.dir:
        parser().error("give --zip (with --extract-to) or --dir, not both")
    _, code = validate(a)
    return code


# ----------------------------------------------------------------------------------------------- self-test

MARKER = "SYNTHETIC-LOG-CONTENT-7f3a"
SRC_SHA = "a" * 40
AID, SRC_RUN = "77", "900"
H1, H2 = "1" * 40, "2" * 40


def _t(m, s):
    return f"2026-01-01T00:{m:02d}:{s:02d}Z"


def _job(i, name, concl, runner, start, end, attempt, run, head):
    return {"id": i, "name": name, "status": "completed", "conclusion": concl, "head_sha": head, "started_at": start,
            "completed_at": end, "runner_id": runner, "run_attempt": attempt, "run_id": int(run),
            "runner_name": None if not runner else f"GitHub Actions {runner}", "steps": [], "labels": []}


def _fixture_jobs():
    j = {}
    j[("1001", 1)] = [_job(11, "Build", "success", 501, _t(0, 1), _t(0, 30), 1, "1001", H1),
                      _job(12, "Test / unit (a:1)", "failure", 502, _t(0, 2), _t(0, 40), 1, "1001", H1),
                      _job(13, "Deploy", "skipped", None, _t(0, 41), _t(0, 41), 1, "1001", H1),
                      _job(14, "Lint", "cancelled", 0, _t(0, 3), _t(0, 5), 1, "1001", H1)]
    j[("1002", 1)] = [_job(21, "Lean", "failure", 601, _t(1, 0), _t(1, 30), 1, "1002", H2),
                      _job(22, "Probe / A", "success", 602, _t(1, 1), _t(1, 31), 1, "1002", H2),
                      _job(23, "Probe / B", "success", 603, _t(1, 2), _t(1, 32), 1, "1002", H2),
                      _job(24, "Bridge", "failure", 604, _t(1, 3), _t(1, 33), 1, "1002", H2)]
    j[("1002", 2)] = [_job(31, "Lean", "success", 611, _t(5, 0), _t(5, 30), 2, "1002", H2),
                      _job(32, "Probe / A", "success", 602, _t(1, 1), _t(1, 31), 2, "1002", H2),
                      _job(33, "Probe / B", "success", 603, _t(1, 2), _t(1, 32), 2, "1002", H2),
                      _job(34, "Bridge", "success", 614, _t(5, 3), _t(5, 33), 2, "1002", H2)]
    return j


def _log(i, n=4, tail=True):
    s = "".join(f"2026-01-01T00:00:{k:02d}.0000000Z {MARKER} job {i} line {k}\n" for k in range(n))
    return (s if tail else s[:-1]).encode()


def _sanitize(name):
    return name.replace("/", "").replace(":", "")


def _zipbytes(members, method=zipfile.ZIP_DEFLATED):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", method) as z:
        for name, data in members:
            zi = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
            zi.compress_type = method
            zi.external_attr = 0o644 << 16
            z.writestr(zi, data)
    return buf.getvalue()


def _flip_member_data(zb, member):
    """Flip one byte inside a member's stored data (so the CRC check, not the parse, fails)."""
    with zipfile.ZipFile(io.BytesIO(zb)) as z:
        info = z.getinfo(member)
    b = bytearray(zb)
    off = info.header_offset
    nlen, xlen = int.from_bytes(b[off + 26:off + 28], "little"), int.from_bytes(b[off + 28:off + 30], "little")
    pos = off + 30 + nlen + xlen + info.compress_size // 2
    b[pos] ^= 0x01
    return bytes(b)


def build_fixture(base, mut=None):
    """Writes a synthetic artifact, its inputs and host records under base. Returns validator arguments."""
    M = mut or {}
    jobs = _fixture_jobs()
    copies = {32: 22, 33: 23}
    joblogs = {}
    for (r, k), js in jobs.items():
        for j in js:
            if j["runner_id"] and j["conclusion"] != "skipped":
                joblogs[j["id"]] = _log(copies.get(j["id"], j["id"]), tail=(j["id"] not in (22, 24)))
    zips = {}
    for (r, k), js in jobs.items():
        members = []
        for idx, j in enumerate(js):
            if not j["runner_id"] or j["conclusion"] == "skipped" or j["id"] in copies:
                continue
            nm = _sanitize(j["name"])
            whole = joblogs[j["id"]]
            if j["id"] == 12:  # the zip's copy of this log stops one line early (a prefix): informative only
                whole = whole[:whole.rstrip(b"\n").rfind(b"\n") + 1]
            members.append((f"{idx}_{nm}.txt", whole))
            members.append((f"{nm}/1_Set up job.txt", _log(f"{j['id']}-s1", 2)))
            members.append((f"{nm}/2_Run.txt", _log(f"{j['id']}-s2", 3)))
        zips[(r, k)] = members
    exp_top = {("1001", 1): 2, ("1002", 1): 4, ("1002", 2): 2}
    if "content" in M:
        M["content"](jobs, joblogs, zips, exp_top)
    art = os.path.join(base, "artifact")
    os.makedirs(os.path.join(art, "jobs"))
    for jid, data in joblogs.items():
        with open(os.path.join(art, "jobs", f"{jid}.txt"), "wb") as f:
            f.write(data)
    zipdata = {}
    for (r, k), members in zips.items():
        os.makedirs(os.path.join(art, "runs", r), exist_ok=True)
        zb = _zipbytes(members)
        if "zipbytes" in M:
            zb = M["zipbytes"](r, k, zb)
        zipdata[(r, k)] = zb
        with open(os.path.join(art, "runs", r, f"attempt-{k}.zip"), "wb") as f:
            f.write(zb)
    recs = []
    attempts = {"1001": 1, "1002": 2}
    heads = {"1001": H1, "1002": H2}
    for r in ("1001", "1002"):
        recs.append({"key": f"run:{r}", "outcome": "ok", "head_sha": heads[r], "run_attempt": attempts[r],
                     "inventory_head_sha": heads[r], "head_matches_inventory": True})
        for k in range(1, attempts[r] + 1):
            recs.append({"key": f"jobs:{r}:{k}", "outcome": "ok",
                         "jobs": [{f: j[f] for f in JOB_FIELDS} for j in jobs[(r, k)]]})
            zb = zipdata[(r, k)]
            # the archiver's member list, as recorded from what it wrote (a later corruption is not reflected)
            mem = [{"name": n, "size": len(d), "sha256": sha256_bytes(d)} for n, d in zips[(r, k)]]
            ntop = sum(1 for n, _ in zips[(r, k)] if "/" not in n)
            recs.append({"key": f"zip:{r}:{k}", "outcome": "archived", "path": f"runs/{r}/attempt-{k}.zip",
                         "bytes": len(zb), "sha256": sha256_bytes(zb), "crc_ok": True, "members": mem,
                         "top_level_job_logs": ntop, "logs_expected": exp_top[(r, k)], "complete": True})
    for jid, data in sorted(joblogs.items()):
        recs.append({"key": f"joblog:{jid}", "outcome": "archived", "path": f"jobs/{jid}.txt", "bytes": len(data),
                     "sha256": sha256_bytes(data), "lines": data.count(b"\n")})
    rec_by = {x["key"]: x for x in recs}
    if "records" in M:
        M["records"](rec_by)
    lines = [json.dumps({"key": "joblog:11", "outcome": "error"})]  # superseded by a later line
    lines += [json.dumps(v, sort_keys=True) for v in rec_by.values()]
    manifest = {"items": [rec_by[k] for k in sorted(rec_by)], "rehash_mismatches": [],
                "counts": {"records": len(rec_by), "zips": 3, "job_logs": len(joblogs)}}
    completeness = {"complete": True, "required": sorted(k for k in rec_by if k.startswith(("zip:", "joblog:"))),
                    "missing_or_incomplete": [], "items": {k: "ok" for k in rec_by}}
    scan = []
    if "fetchlog" in M:
        M["fetchlog"](lines, manifest)
    if "manifest" in M:
        M["manifest"](manifest)
    if "completeness" in M:
        M["completeness"](completeness)
    if "scan" in M:
        scan = M["scan"](scan)
    for name, obj in (("manifest.json", manifest), ("completeness.json", completeness), ("scan.json", scan)):
        with open(os.path.join(art, name), "w") as f:
            json.dump(obj, f, indent=1, sort_keys=True)
    with open(os.path.join(art, "fetch-log.jsonl"), "w") as f:
        f.write("\n".join(lines) + "\n")
    if "files" in M:
        M["files"](art)
    # outer zip, as upload-artifact would stage it
    members = []
    for dirpath, _, fns in os.walk(art):
        for n in sorted(fns):
            p = os.path.join(dirpath, n)
            with open(p, "rb") as f:
                members.append((os.path.relpath(p, art).replace(os.sep, "/"), f.read()))
    members.sort()
    if "outer_members" in M:
        M["outer_members"](members)
    outer = _zipbytes(members)
    meta = {"id": int(AID), "name": f"ci-logs-{SRC_SHA}", "size_in_bytes": len(outer),
            "digest": "sha256:" + sha256_bytes(outer), "expired": False, "created_at": "2026-10-17T05:09:37Z",
            "expires_at": "2026-10-31T05:09:33Z",
            "workflow_run": {"id": int(SRC_RUN), "head_sha": SRC_SHA, "head_branch": "tmp/log-archive-test"}}
    if "outer" in M:
        outer, recompute = M["outer"](outer)
        if recompute:
            meta["size_in_bytes"], meta["digest"] = len(outer), "sha256:" + sha256_bytes(outer)
    if "meta" in M:
        M["meta"](meta)
    zp = os.path.join(base, "artifact.zip")
    with open(zp, "wb") as f:
        f.write(outer)
    mp = os.path.join(base, "metadata.json")
    with open(mp, "w") as f:
        json.dump(meta, f)
    # host records
    host = os.path.join(base, "host")
    os.makedirs(host)
    hjobs = {k: [dict(j) for j in v] for k, v in _fixture_jobs().items()}
    hruns = {r: {"id": int(r), "head_sha": heads[r], "run_attempt": attempts[r], "status": "completed"}
             for r in attempts}
    hatt = {(r, k): {"id": int(r), "run_attempt": k, "head_sha": heads[r]} for r in attempts
            for k in range(1, attempts[r] + 1)}
    if "host" in M:
        M["host"](hruns, hatt, hjobs)
    for r, v in hruns.items():
        with open(os.path.join(host, f"run-{r}.json"), "w") as f:
            json.dump(v, f)
    for (r, k), v in hatt.items():
        with open(os.path.join(host, f"run-{r}-attempt-{k}.json"), "w") as f:
            json.dump(v, f)
    for (r, k), v in hjobs.items():
        with open(os.path.join(host, f"jobs-{r}-attempt-{k}.json"), "w") as f:
            json.dump({"total_count": len(v), "jobs": v}, f)
    if "hostfiles" in M:
        M["hostfiles"](host)
    # inputs
    inp = os.path.join(base, "inputs")
    os.makedirs(inp)
    with open(os.path.join(inp, "batch.json"), "w") as f:
        json.dump({"source": "inventory-runs.csv", "run_ids": ["1001", "1002"], "job_logs": "all",
                   "retention_days": 14}, f)
    with open(os.path.join(inp, "inventory-runs.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["run_id", "tier", "head_sha", "workflow", "event", "conclusion"])
        w.writerow(["1001", "A", H1, "verify.yml", "push", "failure"])
        w.writerow(["1002", "A", H2, "verify.yml", "workflow_dispatch", "success"])
        w.writerow(["1003", "A", "3" * 40, "verify.yml", "push", "success"])
    with open(os.path.join(inp, "inventory-jobs.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["job_id", "cited_by", "run_id", "name", "conclusion"])
        w.writerow(["12", "rule-R", "1001", "Test / unit (a:1)", "failure"])
        w.writerow(["5", "rule-R", "999", "Other", "success"])
    pins = [f"{n}={sha256_file(os.path.join(inp, n))[1]}" for n in
            ("batch.json", "inventory-runs.csv", "inventory-jobs.csv")]
    args = ["--zip", zp, "--extract-to", os.path.join(base, "extracted"), "--metadata", mp,
            "--batch", os.path.join(inp, "batch.json"), "--inventory-runs", os.path.join(inp, "inventory-runs.csv"),
            "--inventory-jobs", os.path.join(inp, "inventory-jobs.csv"), "--host", host,
            "--artifact-id", AID, "--source-run-id", SRC_RUN, "--source-head-sha", SRC_SHA,
            "--validator-commit", "selftest", "--workflow-run", "0", "--workflow-attempt", "0"]
    for p in pins:
        args += ["--expect-input-sha256", p]
    if "args" in M:
        args = M["args"](args, base)
    return args


def _drop_arg(args, flag):
    i = args.index(flag)
    return args[:i] + args[i + 2:]


def _set_arg(args, flag, value):
    i = args.index(flag)
    return args[:i + 1] + [value] + args[i + 2:]


def _j(*parts):
    """Joined at run time (a call, so the compiler cannot fold the parts into one constant)."""
    return "".join(parts)


def _fake_token(kind):
    """Credential-shaped samples, assembled at run time so neither this file nor its bytecode holds one."""
    a36 = _j(*("abcdefghijklmnopqrstuvwxyzABCDEFGHIJ"[i % 36] for i in range(36)))
    hdr = _j("ey", "JhbGciOiJSUzI1NiJ9")
    pay = _j("ey", "Jpc3MiOiJ0ZXN0In0")
    sig = "c2lnbmF0dXJlc2lnbmF0dXJl"
    blob = _j("https://x.blob.core.", "windows.net/c/b.zip?")
    return {
        "github-token": _j("gh", "p_", a36),
        "github-app-token-jwt": _j("gh", "s_", "123456_", hdr, ".", pay, ".", sig),
        "github-fine-grained-pat": _j("github", "_pat_", "11ABCDEFG0123456789_abcdefghijklmnop"),
        "github-installation-v1": _j("v1", ".", "0123456789abcdef", "0123456789abcdef", "01234567"),
        "jwt": _j(hdr, ".", pay, ".", sig),
        "azure-sas-sig": _j(blob, "sp=r&s", "ig=", "AbCdEfGhIjKlMnOp%2Bq%3D"),
        "azure-sas-se": _j(blob, "s", "e=2026-10-17T06%3A00%3A00Z"),
        "azure-sas-sv": _j(blob, "s", "v=2025-01-05"),
        "authorization-header": _j("Author", "ization: Bearer ", "abcdEFGH1234ijkl5678"),
        "x-access-token-url": _j("https://x-access-", "token:", "abcdEFGH1234ijkl", "@github.com/o/r"),
        "url-credentials": _j("https://user:", "s3cretpassw0rd", "@example.com/"),
        "aws-access-key-id": _j("AK", "IA", "QWERTYUIOPASDFGH"),
        "aws-secret-access-key": _j("aws_secret_", "access_key = ", "A" * 20, "b" * 20),
        "private-key": _j("-----BEGIN ", "OPENSSH PRIVATE ", "KEY-----"),
    }[kind]


NEGATIVE_SAMPLES = [
    "[command]/usr/bin/git config --local http.https://github.com/.extraheader AUTHORIZATION: basic ***",
    "https://x.blob.core.windows.net/c/b.zip?sig=***",
    "https://x-access-token:***@github.com/o/r",
    "Authorization: Bearer $GH_TOKEN",
    "sha 05df8cc18e0103ae9f3ffbf52b1ecb6a6aedf64b and ghp_short",
    "-----BEGIN PUBLIC KEY-----",
]


def _run(args, out=None):
    a = parser().parse_args(args)
    buf = io.StringIO()
    rep, code = validate(a, buf)
    return rep, code, buf.getvalue()


def _load_downloader():
    p = os.path.join(HERE, "download_artifact_zip.py")
    spec = importlib.util.spec_from_file_location("download_artifact_zip", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def self_test(work=None):
    base = tempfile.mkdtemp(prefix="validate-selftest-", dir=work)
    try:
        return _self_test(base)
    finally:
        shutil.rmtree(base, ignore_errors=True)


def _self_test(base):
    failures = []
    counter = [0]

    def fresh():
        counter[0] += 1
        d = os.path.join(base, f"case-{counter[0]:03d}")
        os.makedirs(d)
        return d

    def expect(name, mut, verdict, intended=None, show=False, args_hook=None):
        d = fresh()
        args = build_fixture(d, mut)
        if args_hook:
            args = args_hook(args, d)
        rep, code, text = _run(args)
        fails, unv = rep.failed_ids(), rep.unverified_ids()
        got = "HOLDS" if code == 0 else "FAILS" if code == 1 else "UNVERIFIED"
        ok = got == verdict and (intended is None or intended in (fails if verdict == "FAILS" else unv))
        ok = ok and MARKER not in text
        for kind in ("github-token",):
            ok = ok and _fake_token(kind) not in text
        if show:
            print(text.rstrip())
        ids = sorted(set(fails if got == "FAILS" else unv))
        print(f"  {'ok  ' if ok else 'FAIL'}  {name:<52} -> {got:<10} {' '.join(ids)}")
        if not ok:
            failures.append(name)
            if not show:
                print(text)
        return ok

    print("validator self-test (synthetic artifact; no network)")
    print("== clean copy, full report ==")
    expect("clean synthetic artifact", None, "HOLDS", show=True)

    print("== targeted mutations (each must fail with its intended check) ==")

    def flip_file(rel):
        def f(art):
            p = os.path.join(art, *rel.split("/"))
            with open(p, "r+b") as fh:
                b = bytearray(fh.read())
                b[len(b) // 2] ^= 0x01
                fh.seek(0)
                fh.write(b)
        return f

    def rec_edit(fn):
        return {"records": fn}

    cases = [
        ("flipped byte in a zip (records stale)", {"files": flip_file("runs/1002/attempt-1.zip")}, "3.files"),
        ("flipped byte in a job log (records stale)", {"files": flip_file("jobs/22.txt")}, "3.files"),
        ("extra file", {"files": lambda art: open(os.path.join(art, "jobs", "999.txt"), "wb").write(b"x\n")},
         "2.files"),
        ("missing file", {"files": lambda art: os.unlink(os.path.join(art, "jobs", "23.txt"))}, "2.files"),
        ("member list differs from the zip",
         rec_edit(lambda R: R["zip:1002:1"]["members"][0].__setitem__("size", R["zip:1002:1"]["members"][0]["size"] + 1)),
         "4.members"),
        ("re-run job's log missing from the zip (records agree)",
         {"content": lambda J, L, Z, E: (Z.__setitem__(("1002", 2), [m for m in Z[("1002", 2)]
                                                                       if not m[0].startswith("0_")]),
                                         E.__setitem__(("1002", 2), 1))}, "4.toplevel"),
        ("copied job wrongly expected in the zip (log included)",
         {"content": lambda J, L, Z, E: (Z[("1002", 2)].append(("1_Probe  A.txt", L[32])),
                                         E.__setitem__(("1002", 2), 3))}, "4.toplevel"),
        ("copy no longer a copy on the host (runner differs)",
         {"host": lambda R, A, J: J[("1002", 2)][1].__setitem__("runner_id", 999)}, "4.toplevel"),
        ("digest mismatch with the metadata",
         {"meta": lambda m: m.__setitem__("digest", "sha256:" + "0" * 64)}, "1.digest"),
        ("size mismatch with the metadata",
         {"meta": lambda m: m.__setitem__("size_in_bytes", m["size_in_bytes"] + 1)}, "1.size"),
        ("wrong expiry (7 days)", {"meta": lambda m: m.__setitem__("expires_at", "2026-10-24T05:09:37Z")},
         "1.expiry"),
        ("wrong expiry (14 days + 2 min)", {"meta": lambda m: m.__setitem__("expires_at", "2026-10-31T05:11:37Z")},
         "1.expiry"),
        ("metadata says expired", {"meta": lambda m: m.__setitem__("expired", True)}, "1.expiry"),
        ("artifact identity (name) differs", {"meta": lambda m: m.__setitem__("name", "ci-logs-other")},
         "1.identity"),
        ("head mismatch: host run record", {"host": lambda R, A, J: R["1002"].__setitem__("head_sha", "3" * 40)},
         "5.heads"),
        ("head mismatch: fetch-log run record",
         rec_edit(lambda R: R["run:1001"].__setitem__("head_sha", "4" * 40)), "5.heads"),
        ("token in a compressed zip member (scan.json still [])",
         {"content": lambda J, L, Z, E: Z[("1001", 1)].append(
             ("Build/3_Leak.txt", (MARKER + " " + _fake_token("github-token") + "\n").encode() * 3))}, "7.scan"),
        ("app token (ghs_<app>_<jwt>) in a job log",
         {"content": lambda J, L, Z, E: L.__setitem__(24, L[24] + (_fake_token("github-app-token-jwt") + "\n").encode())},
         "7.scan"),
        ("non-empty scan.json", {"scan": lambda s: [{"path": "jobs/11.txt", "line": 1, "pattern": "x"}]},
         "3.scanjson"),
        ("manifest item differs from the fetch log",
         {"manifest": lambda m: [i for i in m["items"] if i["key"] == "joblog:21"][0].__setitem__("sha256", "0" * 64)},
         "3.manifest"),
        ("rehash_mismatches non-empty", {"manifest": lambda m: m.__setitem__("rehash_mismatches", ["jobs/11.txt"])},
         "3.rehash"),
        ("completeness false", {"completeness": lambda cp: cp.__setitem__("complete", False)}, "3.completeness"),
        ("skipped job given a log", {"content": lambda J, L, Z, E: L.__setitem__(13, _log(13))}, "2.files"),
        ("empty job log (records agree)", {"content": lambda J, L, Z, E: L.__setitem__(21, b"")}, "3.files"),
        ("CRC-corrupt zip member, records rehashed",
         {"zipbytes": lambda r, k, zb: _flip_member_data(zb, "Lean/2_Run.txt") if (r, k) == ("1002", 1) else zb},
         "4.testzip"),
        ("job-log line count wrong", rec_edit(lambda R: R["joblog:22"].__setitem__("lines", R["joblog:22"]["lines"] + 1)),
         "3.lines"),
        ("job record differs from the host list",
         rec_edit(lambda R: R["jobs:1001:1"]["jobs"][0].__setitem__("conclusion", "failure")), "3.jobs-records"),
        ("last fetch-log line wins (a later wrong line)",
         {"fetchlog": lambda lines, man: (
             lines.append(json.dumps(dict([i for i in man["items"] if i["key"] == "joblog:23"][0], sha256="f" * 64))),
             [i for i in man["items"] if i["key"] == "joblog:23"][0].__setitem__("sha256", "f" * 64))},
         "3.files"),
        ("record outcome not as specified", rec_edit(lambda R: R["joblog:24"].__setitem__("outcome", "missing")),
         "3.fetchlog"),
        ("unknown record key", rec_edit(lambda R: R.__setitem__("misc:1", {"key": "misc:1", "outcome": "ok"})),
         "3.fetchlog"),
        ("unsafe member name ('..') in the artifact zip",
         {"outer_members": lambda ms: ms.append(("../evil.txt", b"x"))}, "1.names"),
        ("CRC-corrupt artifact zip, metadata matches it",
         {"outer": lambda zb: (_flip_member_data(zb, "fetch-log.jsonl"), True)}, "1.testzip"),
    ]
    for name, mut, intended in cases:
        expect(name, mut, "FAILS", intended)
    expect("input pin mismatch", None, "FAILS", "0.inputs",
           args_hook=lambda a, d: _set_arg(a, "--expect-input-sha256", "batch.json=" + "0" * 64))

    print("== missing evidence (each must be UNVERIFIED, never HOLDS) ==")
    expect("no host job lists", None, "UNVERIFIED", "2.expected", args_hook=lambda a, d: _drop_arg(a, "--host"))
    expect("host job list of one attempt missing", {"hostfiles": lambda h: os.unlink(
        os.path.join(h, "jobs-1002-attempt-2.json"))}, "UNVERIFIED", "2.expected")
    expect("no artifact zip (pre-extracted directory only)", None, "UNVERIFIED", "1.digest",
           args_hook=lambda a, d: _drop_arg(_drop_arg(a, "--zip"), "--extract-to") + ["--dir", os.path.join(d, "artifact")])
    expect("metadata without a digest", {"meta": lambda m: m.pop("digest")}, "UNVERIFIED", "1.digest")
    expect("metadata absent", None, "UNVERIFIED", "1.digest",
           args_hook=lambda a, d: _set_arg(a, "--metadata", os.path.join(d, "absent.json")))
    expect("no input pins", None, "UNVERIFIED", "0.inputs",
           args_hook=lambda a, d: [x for i, x in enumerate(a) if x != "--expect-input-sha256"
                                   and (i == 0 or a[i - 1] != "--expect-input-sha256")])
    expect("batch.json absent", None, "UNVERIFIED", "0.inputs",
           args_hook=lambda a, d: _set_arg(a, "--batch", os.path.join(d, "absent.json")))
    expect("extraction directory not fresh", None, "UNVERIFIED", "1.extract",
           args_hook=lambda a, d: (os.makedirs(os.path.join(d, "extracted")),
                                   open(os.path.join(d, "extracted", "x"), "w").close(), a)[2])

    print("== download path, end to end (local API and storage servers) ==")
    try:
        dl = _load_downloader()
    except Exception as e:  # noqa: BLE001
        print(f"  FAIL  downloader module not loadable ({type(e).__name__})")
        failures.append("downloader")
        dl = None
    if dl is not None:
        def e2e(name, storage_kind, verdict, intended, transport_kw=None, aid="7"):
            d = fresh()
            args = build_fixture(d)
            with open(_arg(args, "--zip"), "rb") as f:
                outer = f.read()
            served = {"clean": outer, "flipped": outer[:100] + bytes([outer[100] ^ 1]) + outer[101:],
                      "oversized": outer * 3}.get(storage_kind, outer)

            def storage_fn(h, st, stop):
                if storage_kind == "error":
                    dl._send(h, 500, b"x")
                elif storage_kind == "slow":
                    if not stop.wait(3.0):
                        dl._send(h, 200, served)
                else:
                    dl._send(h, 200, served)
            storage = dl._Server(storage_fn)
            link = _j(storage.base, "/blob/secret-path-0123/artifact.zip?", "s", "v=2025-01-05&s", "ig=SECRETSIG0123456789")

            def api_fn(h, st, stop):
                dl._send(h, 302, headers={"Location": link})
            api = dl._Server(api_fn)
            t = dl.test_transport(api, **(transport_kw or {}))
            out, recp = os.path.join(d, "dl.zip"), os.path.join(d, "dl-record.json")
            cap = dl.size_cap(_arg(args, "--metadata"))
            rec = dl.download("o/r", aid, "tok-e2e", out, cap, t)
            dl.write_record(recp, rec)
            api.close()
            storage.close()
            args = _set_arg(args, "--zip", out) + ["--download-record", recp]
            a = parser().parse_args(args)
            a.expected_endpoint = t.pinned_endpoint
            buf = io.StringIO()
            rep, code = validate(a, buf)
            text = buf.getvalue()
            got = "HOLDS" if code == 0 else "FAILS" if code == 1 else "UNVERIFIED"
            ids = rep.failed_ids() if got == "FAILS" else rep.unverified_ids()
            leaked = any(s in text for s in ("secret-path-0123", "SECRETSIG0123456789", link, "tok-e2e"))
            with open(recp) as f:
                leaked = leaked or "secret-path" in f.read()
            ok = got == verdict and (intended is None or intended in ids) and not leaked and MARKER not in text
            print(f"  {'ok  ' if ok else 'FAIL'}  {name:<52} -> {got:<10} {' '.join(sorted(set(ids)))}"
                  f"  [download {rec['outcome']}{'' if rec['outcome'] == 'ok' else ' ' + str(rec['error_type'])}]")
            for st_, cid_, msg_ in rep.rows:
                if cid_ == "1.download":
                    print(f"          {st_} {cid_}: {msg_}")
            if not ok:
                failures.append(name)
                print(text)
        e2e("clean download, validated", "clean", "HOLDS", None)
        e2e("byte-flipped zip served: digest check fails", "flipped", "FAILS", "1.digest")
        e2e("failed download (storage 500)", "error", "UNVERIFIED", "1.download")
        e2e("oversized body (3 x size_in_bytes)", "oversized", "UNVERIFIED", "1.download")
        e2e("slow storage server (0.5 s read timeout)", "slow", "UNVERIFIED", "1.download",
            {"timeout": 0.5, "deadline": 2.0})
        e2e("endpoint refused (another artifact id)", "clean", "UNVERIFIED", "1.download", aid="8")

    print("== credential patterns ==")
    for name, _ in SCAN_PATTERNS:
        if name == "github-token-generic":
            continue
        hits = {h[0] for h in scan_bytes(("x " + _fake_token(name) + " y\n").encode())}
        ok = name in hits
        print(f"  {'ok  ' if ok else 'FAIL'}  positive sample matches {name}")
        if not ok:
            failures.append(f"pattern {name}")
    for i, s in enumerate(NEGATIVE_SAMPLES):
        hits = scan_bytes(s.encode())
        ok = not hits
        print(f"  {'ok  ' if ok else 'FAIL'}  masked/benign sample #{i} has no hit")
        if not ok:
            failures.append(f"negative {i}")
    tok = _fake_token("github-token").encode()
    zb = _zipbytes([("a/1_x.txt", b"pad " * 50 + tok + b"\n" + b"pad " * 50)])
    ok = tok not in zb and any(h[0] == "github-token" for h in
                               scan_bytes(zipfile.ZipFile(io.BytesIO(zb)).read("a/1_x.txt")))
    print(f"  {'ok  ' if ok else 'FAIL'}  control: a token in a deflated member is absent from the raw zip bytes "
          f"and found after decompression")
    if not ok:
        failures.append("compressed control")

    print(f"validator self-test: {'all cases ok' if not failures else str(len(failures)) + ' FAILED: ' + ', '.join(failures)}")
    return len(failures)


def _arg(args, flag):
    return args[args.index(flag) + 1]


if __name__ == "__main__":
    sys.exit(main())
