#!/usr/bin/env python3
"""Collect the batch's expected results from the shard job logs as the session's job-log tool served them.

  python3 -I collect.py --runs batchx/runs.json --run-jobs JOBS.json --head SHA --served FILE [--served FILE ...] \
      --out DIR
  python3 -I collect.py --self-test [--work DIR]

Run in the session, after the launch, never in CI. Nothing here downloads anything. The trust boundary this file
implements is TRUST-BOUNDARY.md; the section numbers cited below are its own.
  --served FILE   one answer of the job-log tool for one shard job, saved as the tool returned it (the tool's own
                  file, or from_transcript.py's extraction of it): exactly one JSON object whose keys are job_id,
                  logs_content and original_length, plus optionally message, which must be the tool's success
                  message. Every served file passes the strict grammar of section 2.2 or is rejected.
  --run-jobs      the jobs list of the extraction's workflow run, from the JSON endpoint
                  repos/amaybaum/incompleteness/actions/runs/<run>/jobs?per_page=100, merged over its pages.
  --head          the commit the owner launched.
  --out DIR       a new path, which must not exist. The collection is written into a fresh staging directory beside
                  it and published by one atomic rename (section 4).
From --run-jobs it builds the job index: exactly one job named "Extract shard K" for each shard K, every job of
one run, at --head, on the launch branch, of this workflow, and the shard jobs' ids distinct.

Exit codes (section 3). 0: published, COLLECT HOLDS. 1: published, quarantined, COLLECT FAILS. 2: published,
quarantined, COLLECT UNVERIFIED. 3: refused (an argument error, or --out exists): nothing read, nothing written.
4: aborted (a host failure, an interrupt, or an error while staging or publishing): nothing published by
this invocation. 5: published, but its
durability not confirmed. Exit 0 always follows a COLLECT PUBLISHED line and ends with COLLECT HOLDS. Every output
line goes through emit(): printable ASCII only, with every input-derived value JSON-escaped. A reader takes a
collection as current only after the check of section 4 (the nonce and digest printed by this invocation, the
pinned run set, the input digests, the exact listing, every run usable).

Governing invariant. A run may be marked usable only when the complete collection succeeds (COLLECT HOLDS) and every
relevant served file has been identified, validated and reconciled. Under any other verdict the collection is
quarantined: collected.json marks no run usable, no result file is written and no ci/ directory exists; this is
decided in one place, write_collection(). Each run's own result is recorded as `eligible`, which is diagnostic only
and licenses nothing.

The intake (section 2.5). Each served file is read once; its sha256 and size are recorded before anything else, so
every file that can be read is traceable. Its bytes are then scanned for every shard they name, unanchored and
independent of timestamps, ANSI codes, whitespace, case, JSON escapes and line position (see raw_named). Then the
strict grammar: duplicate keys at any depth, unknown keys, wrong types, non-standard constants, a BOM, non-UTF-8,
anything before or after the one object, and a message other than the tool's success message are all rejected. An
accepted answer's decoded logs_content is scanned the same way, so the names a file carries do not depend on how
they are spelled in JSON. A scan's conversion error (ValueError, e.g. int() refusing more than 4,300 digits)
rejects only that file, as byte, decoded or parsed scan failed, with names_shards null, and the intake goes on; a
host failure (MemoryError, or an OSError other than a path that names nothing or the file's own refused access)
or an interrupt aborts the run (exit 4) and publishes nothing. A rejected file, an answer of a job outside the run
that names no shard, and a missing
expected answer (the log of job "Extract shard K" in the extraction run's jobs list, for every shard of the plan)
quarantine the whole collection: no run is eligible or usable, the verdict is FAILS, and the file is recorded by
name, size and sha256, or the missing answer by its expected name. A file that fails validation makes the
collection FAILS and is recorded by name and sha256 in failed_files. collected.json also records every served
argument (files), every expected answer with all its copies' digests (expected), and the collection's nonce, input
digests and manifest (collection).

Identity. An answer belongs to the shard the job index gives its job id: trusted collection metadata (the tool's
job id and the extraction run's jobs list), never the log's own text. Every file is read before anything is decided,
and the answers are grouped by that trusted job id. For each job the shards it is involved with are its trusted
shard and every shard its answers name anywhere: every RUNSET line, the assembler banner, the end-of-output marker,
the verdict line, the runs.json shard of every RESULT line and block, and everything the raw scan finds. A job involved with two or more
shards voids every one of them; a job whose answers differ, or with an answer that has no single readable RUNSET
banner, voids its shard (UNVERIFIED, none of its runs usable); an answer of a job outside the run FAILS and voids
every shard its log names. Byte-identical copies are taken once. So neither file order, nor shard numbering, nor
a damaged or reordered banner can decide which runs are usable.

For the one answer of each surviving shard it checks, fail closed:
  - the answer's job id is the index's job for that shard, and the log's banner names that shard;
  - the log was served whole, its line count equal to original_length, and is under 5,000 lines;
  - one assembler banner, naming the pinned assembler, host-reader and extractor blobs, the extractor's commit and
    runs.json's digest; one `BATCH SHARD K/N RUNSET <sha256> RUNS n` line whose N and digest are shard K's in the
    pinned runs.json;
  - one RESULT line for each of shard K's runs and for no other run;
  - one block, BEGIN/END/SHA256, for each run whose RESULT line is HOLDS, and none for any other run; the block's
    text (timestamps stripped, lines joined with newlines, ending with one) is canonical ASCII JSON whose sha256
    equals its SHA256 line, naming that run, its pinned bridge job and head, kind cited-bridge, and in `source`
    the pinned extractor blob and commit, assembler blob, host-reader blob and runs.json digest;
  - the assembler's output is bounded: exactly one start marker (its banner) and exactly one end-of-output marker
    (`BATCH END shard K/N: assembler <blob prefix>`), in that order, every RESULT line and block between them, and no
    `CHECK all ...` line between them (the assembler's own report that it stopped or that its run set is wrong);
  - exactly one `EXTRACT SHARD K/N <verdict>` line in the whole log, the line just before the end-of-output marker,
    and that verdict is the one the RESULT lines imply.
A file that fails any check contributes no result, and the collection FAILS.

A run is eligible when its RESULT is HOLDS and its shard passed every check. The verdict is COLLECT HOLDS (exit 0)
when every run of runs.json is eligible and nothing failed, COLLECT FAILS (exit 1) when a run FAILS, a file fails a
check or the collection is quarantined, and COLLECT UNVERIFIED (exit 2) otherwise. Only under HOLDS are the runs
usable: each block is then written to DIR/ci/<run>/results.json and listed in DIR/collected.json with its digest,
shard, source job id and served-text sha256. collected.json always records the verdict, the quarantine, each run's
eligibility and the reason it is not usable. Python 3 stdlib.
"""
import argparse
import collections
import contextlib
import errno
import hashlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time

sys.dont_write_bytecode = True
RUNS_SHA256 = "5436c5b6325e5efca8b9d9a737ba832b6556ae9ffc15524b33774f701f672edb"
# The launched tree's blobs of the two CI scripts; controls.py's plan check requires them to equal the files' blobs.
ASSEMBLER_BLOB = "d0a794835a22f1cdb94a8419fb6ec4c3aaaf2151"
HOST_BLOB = "2b1e6e01517b71f5d2ef9792676f1ca23fccbcd6"
EXTRACT_RESULT_BLOB = "05c41bce610b8d02ccbaca8e69377b771bef4a35"
MAIN_COMMIT = "b96662e6be4f537502c772db369ea32a35b213a8"
BRANCH = "tmp/ci-batch-extract-design-20261017"
WORKFLOW_NAME = "Cited CI runs, bridge-output batch extraction (read-only)"
JOB_NAME = "Extract shard %d"
MAX_LINES = 5000           # the job-log tool serves at most this many lines; a shard log must be under it
TS = re.compile(r"^\ufeff?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ")
ABANNER = re.compile(r"^BATCH ci-batch-extract shard (\d+)/(\d+): assembler ([0-9a-f]{12}), host reader ([0-9a-f]{12}), "
                     r"extract_result ([0-9a-f]{12}) at ([0-9a-f]{12}), runs\.json ([0-9a-f]{12})$")
BANNER = re.compile(r"^BATCH SHARD (\d+)/(\d+) RUNSET ([0-9a-f]{64}) RUNS (\d+)$")
AEND = re.compile(r"^BATCH END shard (\d+)/(\d+): assembler ([0-9a-f]{12})$")
RESULT = re.compile(r"^RESULT (\d+) (HOLDS|FAILS|UNVERIFIED) (\S+) \(")
BEGIN = re.compile(r"^===== BEGIN EXPECTED RESULT ci/(\d+)/results\.json =====$")
END = "===== END EXPECTED RESULT ci/%s/results.json ====="
SHA = re.compile(r"^SHA256 ci/(\d+)/results\.json ([0-9a-f]{64})$")
VERDICT = re.compile(r"^EXTRACT SHARD (\d+)/(\d+) (HOLDS|FAILS|UNVERIFIED)$")


def runset_digest(ids):
    return hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()


def strip(l):
    return TS.sub("", l, count=1)


def build_job_index(jobsd, head, nshards):
    """{shard: job id} from the extraction run's jobs list; (index, run id, problems)."""
    probs = []
    if not re.fullmatch(r"[0-9a-f]{40}", str(head)):
        return {}, None, ["the launched commit %s is not a full 40-hex sha" % json.dumps(str(head)[:100])]
    try:
        jobs = jobsd["jobs"]
        if len(jobs) != jobsd["total_count"]:
            probs.append("the jobs list holds %d of %d jobs" % (len(jobs), jobsd["total_count"]))
        runs = {j["run_id"] for j in jobs}
        if len(runs) != 1:
            probs.append("the jobs list spans %d runs" % len(runs))
        for j in jobs:
            if j["head_sha"] != head or j.get("head_branch") != BRANCH or j.get("workflow_name") != WORKFLOW_NAME:
                probs.append("job %s is not of this workflow at %s on %s" % (json.dumps(j.get("id")), head[:12], BRANCH))
        index = {}
        for k in range(1, nshards + 1):
            ids = [j["id"] for j in jobs if j["name"] == JOB_NAME % k]
            if len(ids) != 1 or not isinstance(ids[0], int) or isinstance(ids[0], bool):
                probs.append("%d jobs named %r" % (len(ids), JOB_NAME % k))
            else:
                index[k] = ids[0]
        if len(set(index.values())) != len(index):   # one id under two shard names (TRUST-BOUNDARY.md 1, J1)
            probs.append("the shard jobs' ids are not distinct")
        return index, (sorted(runs)[0] if len(runs) == 1 else None), probs
    except (KeyError, TypeError, AttributeError):
        return {}, None, ["the jobs list is malformed"]


def identity(obj):
    return hashlib.sha256(json.dumps([obj.get("job_id"), obj.get("logs_content"), obj.get("original_length")],
                                     sort_keys=True).encode("utf-8")).hexdigest()


# ------------------------------------------------------------------ the strict grammar (TRUST-BOUNDARY.md 2.2-2.3)
SUCCESS_MESSAGE = "Job logs content retrieved successfully"   # the tool's success response, in every real answer
MAX_SERVED_BYTES = 16 * 1024 * 1024                            # the largest saved answer seen is 812 KB
REQUIRED_KEYS = frozenset(("job_id", "logs_content", "original_length"))


class Rejected(ValueError):
    """A rejection by a strict decoder's hook; its text is the recorded reason."""


def _no_duplicates(pairs):
    """object_pairs_hook: any key twice in one object is refused. Python calls it for every object, nested ones
    included, as each one closes, so it covers every depth; keys are compared after unescaping."""
    counts = collections.Counter(k for k, _ in pairs)
    dup = sorted(k for k, c in counts.items() if c > 1)
    if dup:
        raise Rejected("duplicate key %s" % ", ".join(repr(k) for k in dup))
    return dict(pairs)


def _no_constant(c):
    raise Rejected("non-standard constant %s" % c)


def _no_float(s):
    raise Rejected("non-integer number")


def _served_int(s):
    if not re.fullmatch(r"0|[1-9][0-9]{0,15}", s):
        raise Rejected("integer out of range")
    return int(s)


def _jobs_int(s):
    if not re.fullmatch(r"-?(?:0|[1-9][0-9]{0,19})", s):
        raise Rejected("integer out of range")
    return int(s)


SERVED_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates, parse_constant=_no_constant,
                                  parse_float=_no_float, parse_int=_served_int)
JOBS_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates, parse_constant=_no_constant,
                                parse_int=_jobs_int)
BLOCK_DECODER = json.JSONDecoder(strict=True, object_pairs_hook=_no_duplicates, parse_constant=_no_constant)


def _decode_strict(data, decoder, served):
    """Steps 2-5 of 2.2 for a served file (served=True), or the jobs-list form of 2.3 (whitespace allowed around
    the value): (value, None) or (None, the rejection reason)."""
    if data[:3] == b"\xef\xbb\xbf":
        return None, "byte-order mark before the object"
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None, "not UTF-8"
    start = 0 if served else len(text) - len(text.lstrip(" \t\n\r"))
    if served and not text.startswith("{"):
        return None, "does not begin with '{'"
    try:
        obj, end = decoder.raw_decode(text, start)
    except Rejected as e:
        return None, str(e)
    except RecursionError:
        return None, "nested too deeply"
    except ValueError as e:
        return None, "not JSON: %s" % getattr(e, "msg", str(e))
    if end != len(text) and (served or text[end:].strip(" \t\n\r")):
        return None, "data after the object"
    return obj, None


def _served_answer(data):
    obj, why = _decode_strict(data, SERVED_DECODER, True)
    if obj is None:
        return None, why
    keys = set(obj)
    if keys != REQUIRED_KEYS and keys != REQUIRED_KEYS | {"message"}:
        return None, "key set %s" % sorted(keys)
    if type(obj["job_id"]) is not int or obj["job_id"] < 1:
        return None, "job_id has the wrong type"
    if type(obj["original_length"]) is not int:
        return None, "original_length has the wrong type"
    if type(obj["logs_content"]) is not str:
        return None, "logs_content has the wrong type"
    if "message" in obj and obj["message"] != SUCCESS_MESSAGE:
        return None, "message is not the tool's success message"
    try:
        obj["logs_content"].encode("utf-8")
    except UnicodeEncodeError:
        return None, "lone surrogate in logs_content"
    return obj, None


def parse_served(data):
    """A served file's bytes: (the tool's answer, None), or (None, the reason it is rejected) (2.2)."""
    return _served_answer(data)


def _errname(e):
    return errno.errorcode.get(getattr(e, "errno", None) or 0, type(e).__name__)


def _read_fd(fd, cap):
    """(size, sha256, bytes or None when over the cap), reading the descriptor once, to its end."""
    h, chunks, n = hashlib.sha256(), [], 0
    while True:
        b = os.read(fd, 1 << 20)
        if not b:
            break
        h.update(b)
        n += len(b)
        if chunks is not None:
            chunks.append(b)
            if n > cap:
                chunks = None
    return n, h.hexdigest(), (b"".join(chunks) if chunks is not None else None)


# The boundary of TRUST-BOUNDARY.md 2.5, by error kind, for a file being read: a path that names nothing, and the
# file's own refused access, are the file's conditions (attributed rejections). Every other OSError (EIO, ENOSPC,
# ENOMEM, EMFILE, ENFILE, ...) is a host failure: it propagates, and the run is ABORTED (exit 4), never published.
NAMES_NOTHING = (errno.ENOENT, errno.ENOTDIR, errno.ENAMETOOLONG)
OWN_ACCESS = (errno.EACCES, errno.EPERM)


def read_input(path, cap=MAX_SERVED_BYTES):
    """Steps 1-2 of 2.5: (record, bytes or None). The record names the file by basename and gives its kind, size,
    sha256 and, when it is not one regular file within the cap, the reason. The bytes are read once; every later
    step uses that one buffer. A symbolic link is never followed for parsing: the regular file it points to is hashed
    for the record only. "_id" is (st_dev, st_ino), for the same-file rule; it is not recorded. A host failure
    raises."""
    rec = {"name": os.path.basename(path), "kind": "unreadable", "size": None, "sha256": None, "reason": None,
           "_id": None}
    try:
        st = os.lstat(path)
    except OSError as e:
        if e.errno in NAMES_NOTHING:   # a missing, mistyped or mangled path
            rec.update(kind="missing", reason="not a regular file (missing)")
            return rec, None
        if e.errno not in OWN_ACCESS:
            raise
        rec["reason"] = "not a regular file (unreadable: %s)" % _errname(e)
        return rec, None
    if stat.S_ISLNK(st.st_mode):
        rec.update(kind="symlink", reason="not a regular file (symlink)")
        try:   # the target is hashed for the record only, when it is a regular file within the cap
            tst = os.stat(path)
            if stat.S_ISREG(tst.st_mode) and tst.st_size <= cap:
                fd = os.open(path, os.O_RDONLY | os.O_NONBLOCK)
                try:
                    if stat.S_ISREG(os.fstat(fd).st_mode):
                        size, digest, _ = _read_fd(fd, cap)
                        rec.update(size=size, sha256=digest)
                finally:
                    os.close(fd)
        except OSError as e:
            if e.errno not in NAMES_NOTHING + OWN_ACCESS + (errno.ELOOP,):   # a dangling or looping link: no digest
                raise
        return rec, None
    if not stat.S_ISREG(st.st_mode):
        kind = "directory" if stat.S_ISDIR(st.st_mode) else "other"
        rec.update(kind=kind, reason="not a regular file (%s)" % kind)
        return rec, None
    try:
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    except OSError as e:
        if e.errno not in OWN_ACCESS + (errno.ELOOP,):   # ELOOP: it became a link between lstat and open
            raise
        rec["reason"] = "not a regular file (unreadable: %s)" % _errname(e)
        return rec, None
    try:
        fst = os.fstat(fd)
        if not stat.S_ISREG(fst.st_mode):
            rec.update(kind="other", reason="not a regular file (other)")
            return rec, None
        size, digest, data = _read_fd(fd, cap)
        rec.update(kind="regular", size=size, sha256=digest, _id=(fst.st_dev, fst.st_ino))
        if data is None:
            rec["reason"] = "over the size cap"
        return rec, data
    except OSError as e:
        if e.errno not in OWN_ACCESS:   # the read: EIO and every other host failure propagate (2.5)
            raise
        rec["reason"] = "not a regular file (unreadable: %s)" % _errname(e)
        return rec, None
    finally:
        os.close(fd)


def esc(v):
    """An input-derived value as any output line carries it: JSON-escaped (TRUST-BOUNDARY.md 3)."""
    return json.dumps(v, ensure_ascii=True)


def emit(outp, line):
    """The one writer of the collector's output lines: one call, one line, printable ASCII only. A character outside
    U+0020-U+007E that still reaches it is written as its JSON escape, so no value can end a line."""
    out = []
    for c in line:
        if " " <= c <= "~":
            out.append(c)
        else:
            e = json.dumps(c)[1:-1]
            out.append(e if e != c else "\\" + "u%04x" % ord(c))
    print("".join(out), file=outp)


def shard_of(obj):
    """The shard of the answer's RUNSET banner when it has exactly one readable one, else None (no readable banner)."""
    ms = [m for m in (BANNER.match(strip(l)) for l in obj["logs_content"].split("\n")) if m]
    return int(ms[0].group(1)) if len(ms) == 1 else None


NAMES_SHARD = re.compile(r"^(?:BATCH SHARD|BATCH ci-batch-extract shard|BATCH END shard|EXTRACT SHARD) (\d+)\b")
NAMES_RUN = re.compile(r"^(?:RESULT (\d+) |===== BEGIN EXPECTED RESULT ci/(\d+)/)")


def shards_named(obj, doc):
    """Every shard the log names anywhere, read loosely so that a damaged line still counts: every RUNSET line, the
    assembler banner, the end-of-output marker and the verdict line, and the runs.json shard of every RESULT line and
    block. Used only to widen the shards a job is involved with, never to choose one."""
    L = [strip(l) for l in obj["logs_content"].split("\n")]
    shard_of_run = {r["run_id"]: r["shard"] for r in doc["runs"]}
    named = set()
    for l in L:
        m = NAMES_SHARD.match(l)
        if m:
            named.add(int(m.group(1)))
        m = NAMES_RUN.match(l)
        if m and (m.group(1) or m.group(2)) in shard_of_run:
            named.add(shard_of_run[m.group(1) or m.group(2)])
    return named  # every shard the log names


# The raw scan. It reads the bytes of a served file as they are, before and independent of any parsing, so a file
# that does not parse, or parses into something else, still names what it names. ANSI escape sequences (raw, or
# JSON-escaped as \u001b) are removed first; separators may be any whitespace or a JSON-escaped one; case is ignored;
# nothing is anchored to a line start or a timestamp. Shard names: "BATCH SHARD K/", "ci-batch-extract shard K/",
# "BATCH END shard K/", "EXTRACT SHARD K/". Run and job ids: a runs.json run id or bridge job id written after
# "ci/", "RESULT", "CHECK", "run", "job" or as the value of an "id", "job_id" or "run_id" key, or written anywhere as
# a bare number of 9 or more digits (every id in runs.json has 11 or 12); each names its run's shard. And the value
# of any "job_id" key that the job index knows names that job's shard.
ANSI = re.compile(r"(?:\x1b|\\u001[bB]|\\x1[bB]|\\033|\\e)\[[0-9;?]*[ -/]*[@-~]")
_SP = r"(?:\s|\\[ntr]|\\u0020|\\u00[aA]0)+"
RAW_SHARD = re.compile(r"(?:BATCH{0}SHARD|ci-batch-extract{0}shard|BATCH{0}END{0}shard|EXTRACT{0}SHARD){0}(\d+)"
                       r"(?:\s|\\[ntr])*/".format(_SP), re.I)
RAW_ID = re.compile(r"(?:ci/|RESULT{0}|CHECK{0}|run{0}|job{0}|\\*\"(?:id|job_id|run_id)\\*\"\s*:\s*\\*\"?\s*)"
                    r"(\d+)(?!\d)".format(_SP), re.I)
RAW_LONG = re.compile(r"(?<!\d)(\d{9,})(?!\d)")
RAW_JOB = re.compile(r"\\*\"job_id\\*\"\s*:\s*\\*\"?\s*(\d+)", re.I)


def raw_named(data, doc, inv):
    """Every shard the raw bytes of a served file name (see above). Only ever widens what a file is involved with."""
    text = ANSI.sub("", data.decode("utf-8", "replace"))
    shard_of_id = {}
    for r in doc["runs"]:
        shard_of_id[str(r["run_id"])] = r["shard"]
        shard_of_id[str(r["bridge_job_id"])] = r["shard"]
    named = {int(m.group(1)) for m in RAW_SHARD.finditer(text)}
    for rx in (RAW_ID, RAW_LONG):
        named |= {shard_of_id[m.group(1)] for m in rx.finditer(text) if m.group(1) in shard_of_id}
    named |= {inv[int(m.group(1))] for m in RAW_JOB.finditer(text) if int(m.group(1)) in inv}
    return named  # the raw scan


def read_shard(obj, doc, job_index, shard=None):
    """Returns (shard or None, problems, {run: (verdict, block text or None)}). shard is the one the job index gives
    the answer's job id (trusted metadata); the log's own banner must agree with it but never chooses it."""
    probs = []
    text, orig, job = obj["logs_content"], obj["original_length"], obj["job_id"]
    raw = text.split("\n")   # a whole answer: original_length == count("\n") + 1, no trailing "\n" (2.4)
    if len(raw) != orig:
        return None, ["job %s served %d of %d lines: not whole" % (job, len(raw), orig)], {}
    if orig >= MAX_LINES:
        return None, ["job %s has %d lines: not under %d" % (job, orig, MAX_LINES)], {}
    L = [strip(l) for l in raw]
    ban = [m for m in (BANNER.match(l) for l in L) if m]
    if len(ban) != 1:
        return None, ["job %s: %d RUNSET lines" % (job, len(ban))], {}
    k, nsh, rs, nr = int(ban[0].group(1)), int(ban[0].group(2)), ban[0].group(3), int(ban[0].group(4))
    if shard is not None and k != shard:
        probs.append("job %s is shard %d's job, but its banner names shard %d" % (job, shard, k))
        k = shard
    if job_index.get(k) != job:
        probs.append("shard %d: served job %s is not the run's job %s for this shard" % (k, job, job_index.get(k)))
    ab = [m for m in (ABANNER.match(l) for l in L) if m]
    if not ab or any(m.groups() != (str(k), str(nsh), ASSEMBLER_BLOB[:12], HOST_BLOB[:12], EXTRACT_RESULT_BLOB[:12],
                                    MAIN_COMMIT[:12], RUNS_SHA256[:12]) for m in ab):
        probs.append("shard %d: the assembler banner is absent or names other blobs" % k)
    exp = [r for r in doc["runs"] if r["shard"] == k]
    byid = {r["run_id"]: r for r in exp}
    if nsh != doc["shards"] or rs != runset_digest(byid) or nr != len(exp) or not exp:
        probs.append("shard %d: banner does not match runs.json (N %d, %d runs)" % (k, nsh, nr))
    res, last, first = {}, -1, None
    for i, l in enumerate(L):
        m = RESULT.match(l) or BEGIN.match(l)
        if m and first is None:
            first = i
        m = RESULT.match(l)
        if m:
            if m.group(1) in res:
                probs.append("shard %d: run %s has two RESULT lines" % (k, m.group(1)))
            res[m.group(1)] = m.group(2)
            last = max(last, i)
    if set(res) != set(byid):
        probs.append("shard %d: RESULT lines for %s, runs.json %s" % (k, sorted(res), sorted(byid)))
    blocks = {}
    i = 0
    while i < len(L):
        m = BEGIN.match(L[i])
        if m:
            rid = m.group(1)
            try:
                j = L.index(END % rid, i + 1)
            except ValueError:
                probs.append("shard %d: run %s's block never ends" % (k, rid))
                last = len(L)
                break
            body = "\n".join(L[i + 1:j]) + "\n"
            sm = SHA.match(L[j + 1]) if j + 1 < len(L) else None
            if rid in blocks:
                probs.append("shard %d: run %s has two blocks" % (k, rid))
            if not sm or sm.group(1) != rid or sm.group(2) != hashlib.sha256(body.encode("utf-8")).hexdigest():
                probs.append("shard %d: run %s's block does not match its SHA256 line" % (k, rid))
            blocks[rid] = body
            last = max(last, j + 1)
            i = j + 1
        i += 1
    for rid, body in blocks.items():
        if res.get(rid) != "HOLDS":
            probs.append("shard %d: a block for run %s, whose RESULT is %s" % (k, rid, res.get(rid)))
            continue
        try:
            r = BLOCK_DECODER.decode(body)   # duplicates at any depth and non-standard constants are refused (2.3)
            cfg, src = byid[rid], r["source"]
            ok = (body.isascii() and body == json.dumps(r, indent=1, sort_keys=True) + "\n"
                  and r.get("kind") == "cited-bridge" and r["run"]["id"] == rid and r["run"]["job_id"] == cfg["bridge_job_id"]
                  and r["commit"] == r["run"]["head_sha"] == cfg["head_sha"])
            ok = ok and isinstance(r.get("expected"), dict) and isinstance(r["expected"].get("outcome"), str)
            pins = (src.get("extractor_blob") == EXTRACT_RESULT_BLOB and src.get("extractor_commit") == MAIN_COMMIT
                    and src.get("assembler_blob") == ASSEMBLER_BLOB and src.get("host_reader_blob") == HOST_BLOB
                    and src.get("runs_sha256") == RUNS_SHA256)
        except (ValueError, KeyError, TypeError, AttributeError):
            ok = pins = False
        if not ok:
            probs.append("shard %d: run %s's block is not a canonical result of that run" % (k, rid))
        elif not pins:
            probs.append("shard %d: run %s's block names another extractor, assembler, host reader or runs.json" % (k, rid))
    for rid, v in res.items():
        if v == "HOLDS" and rid not in blocks:
            probs.append("shard %d: run %s holds but has no block" % (k, rid))
    # The assembler's output runs from its banner (the start marker) to its end-of-output marker, which it prints
    # right after its verdict. There must be exactly one of each, in that order; every RESULT line and block must lie
    # between them; and there must be exactly one verdict line in the whole log, the line before the end marker.
    starts = [i for i, l in enumerate(L) if ABANNER.match(l)]
    ends = [i for i, l in enumerate(L) if AEND.match(l)]
    span = None
    if len(starts) != 1:
        probs.append("shard %d: %d start markers (assembler banners), not one" % (k, len(starts)))
    if len(ends) != 1:
        probs.append("shard %d: %d end-of-output markers, not one: the assembler did not finish, or its output is "
                     "ambiguous" % (k, len(ends)))
    if len(starts) == 1 and len(ends) == 1:
        span = (starts[0], ends[0])
        if span[1] < span[0]:
            probs.append("shard %d: the end-of-output marker comes before the start marker" % k)
            span = None
        elif AEND.match(L[span[1]]).groups() != (str(k), str(nsh), ASSEMBLER_BLOB[:12]):
            probs.append("shard %d: the end-of-output marker names another shard or assembler" % k)
            span = None
    if span is not None and first is not None and (first < span[0] or last > span[1]):
        probs.append("shard %d: a RESULT line or block lies outside the assembler's output" % k)
    if span is not None and any(L[i].startswith("CHECK all ") for i in range(span[0], span[1])):
        probs.append("shard %d: the assembler reported a CHECK all line (it stopped, or its run set is wrong)" % k)
    vs = [(i, m) for i, m in ((i, VERDICT.match(l)) for i, l in enumerate(L)) if m]
    want = "FAILS" if "FAILS" in res.values() else "HOLDS" if res and all(v == "HOLDS" for v in res.values()) \
        and set(res) == set(byid) else "UNVERIFIED"
    if len(vs) != 1:
        probs.append("shard %d: %d verdict lines, not one" % (k, len(vs)))
    elif span is not None and vs[0][0] != span[1] - 1:
        probs.append("shard %d: the verdict line is not the assembler's last line before its end-of-output marker" % k)
    elif (int(vs[0][1].group(1)), int(vs[0][1].group(2))) != (k, nsh) or vs[0][1].group(3) != want:
        probs.append("shard %d: the verdict line is not the one its RESULT lines imply (%s)" % (k, want))
    return k, probs, {rid: (v, blocks.get(rid)) for rid, v in res.items()}


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def collector_identity(path=None):
    """The collector as executed and as committed: the sha256 and git blob of the bytes executed, the commit of the
    checkout they were run from, that commit's blob of this file, and whether the two blobs are equal."""
    path = os.path.abspath(path or __file__)
    with open(path, "rb") as f:
        data = f.read()
    executed = git_blob_id(data)
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")

    def git(*args):
        p = subprocess.run(["git", "-C", os.path.dirname(path)] + list(args), capture_output=True, text=True, env=env,
                           timeout=60)
        return p.stdout.strip() if p.returncode == 0 else None
    commit = git("rev-parse", "--verify", "HEAD")
    rel = git("ls-files", "--full-name", "--", os.path.basename(path))
    committed = git("rev-parse", "--verify", "HEAD:%s" % rel) if commit and rel else None
    return {"path": rel, "commit": commit, "committed_blob": committed, "executed_blob": executed,
            "executed_sha256": hashlib.sha256(data).hexdigest(),
            "executed_matches_committed_blob": committed is not None and committed == executed}


_IDENTITY = []


def _collector_identity_once():
    """collector_identity() of the executing file, computed once per process: the bytes executed and the checkout they
    run from do not change during one run, and each call costs three git subprocesses."""
    if not _IDENTITY:
        _IDENTITY.append(collector_identity())
    return dict(_IDENTITY[0])


def _sync(fd, durable):
    if durable:
        os.fsync(fd)


def _sync_dir(path, durable):
    if durable:
        fd = os.open(path, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)


def _utc():
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def write_collection(out, table, verdict, quarantine, shards, run_id, head, failed=(), voids=(), extra=None,
                     durable=False):
    """The one place collected.json and the result files are written, and the one place a run becomes usable: it is
    usable only when it is eligible and the whole collection's verdict is HOLDS. Under any other verdict no run is
    usable, no result file is written and no ci/ directory is made, and the run entries carry no result content.
    out is the staging directory (TRUST-BOUNDARY.md 4): the result files are written first and collected.json last,
    with the manifest of every other file. Returns (the number of usable runs, collected.json's sha256)."""
    extra = dict(extra or {})
    n, manifest = 0, []
    for e in table:
        e["usable"] = bool(e["eligible"] and verdict == "HOLDS")
        body = e.pop("_body", None)
        if verdict != "HOLDS":   # a quarantined record carries no result content (section 5)
            e.pop("sha256", None)
            e.pop("outcome", None)
        if e["usable"]:
            d = os.path.join(out, "ci", e["run_id"])
            os.makedirs(d, exist_ok=True)
            with open(os.path.join(d, "results.json"), "x", encoding="ascii") as f:
                f.write(body)
                f.flush()
                _sync(f.fileno(), durable)
            _sync_dir(d, durable)
            data = body.encode("ascii")
            manifest.append({"path": "ci/%s/results.json" % e["run_id"], "size": len(data),
                             "sha256": hashlib.sha256(data).hexdigest()})
            n += 1
    if n:
        _sync_dir(os.path.join(out, "ci"), durable)
    coll = dict(extra.get("collection") or {}, manifest=manifest, written_utc=_utc())
    record = {"runs_sha256": extra.get("runs_sha256"), "extraction_run": run_id, "verdict": verdict,
              "usable_rule": "a run is usable only when it is eligible and the whole collection's verdict is HOLDS",
              "quarantine": quarantine,
              "failed_files": list(failed), "voided_shards": list(voids),
              # what was launched: the --head commit, which the job index required of every job of the run
              "launched_commit": head,
              "launched_commit_check": "every job of extraction_run's jobs list is at launched_commit, on %s, of "
                                       "workflow %r" % (BRANCH, WORKFLOW_NAME),
              # what collected it: this file as executed and as committed, and the values it pins
              "collector": dict(_collector_identity_once(), pins={"assembler_blob": ASSEMBLER_BLOB, "host_reader_blob": HOST_BLOB,
                                     "extractor_blob": EXTRACT_RESULT_BLOB, "extractor_commit": MAIN_COMMIT,
                                     "runs_sha256": RUNS_SHA256}),
              "shards": {str(k): (v and {"file": v["file"], "files": v["files"], "served_sha256": v["served_sha256"],
                                         "sha256s": v["sha256s"], "job_id": v["job_id"], "copies": v["copies"]})
                         for k, v in sorted(shards.items())}, "runs": table,
              "schema": "batchx-collected/2", "quarantined": verdict != "HOLDS", "collection": coll,
              "files": extra.get("files", []), "expected": extra.get("expected")}
    text = json.dumps(record, indent=1, sort_keys=True) + "\n"
    with open(os.path.join(out, "collected.json"), "x", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        _sync(f.fileno(), durable)
    _sync_dir(out, durable)
    return n, hashlib.sha256(text.encode("utf-8")).hexdigest()


def _q_label(q):
    if q["kind"] == "missing":
        return "missing shard %d" % q["shard"]
    if q["kind"] == "input":
        return "%s %s" % (q["input"], esc(q.get("name")))
    if q["kind"] == "internal":
        return "internal error at %s" % q["stage"]
    return esc(q.get("file"))


FILE_FIELDS = ("arg", "name", "kind", "size", "sha256", "status", "reason")
SCAN_ERRORS = (ValueError,)   # the per-file catch (TRUST-BOUNDARY.md 2.5): a scan's conversion error, and nothing else


def _file_lines(P, files):
    for e in files:
        P("COLLECT FILE %s" % json.dumps({k: e[k] for k in FILE_FIELDS}, sort_keys=True, ensure_ascii=True))


def _take_in(i, path, doc, inv, known):
    """Steps 1-5 of 2.5 for one served argument: (its files entry, (answer, names, parsed readings) when accepted,
    else None, its file id). A ValueError raised by the byte scan, the decoded scan or the parsed readings rejects
    this file with names_shards null, and nothing after the failed scan runs on it. Every other exception propagates
    (a host failure: ABORTED; a bug: S10's internal quarantine)."""
    rec, data = read_input(path)
    fid = rec.pop("_id")
    entry = {"arg": i, "name": rec["name"], "kind": rec["kind"], "size": rec["size"], "sha256": rec["sha256"],
             "status": "rejected", "reason": rec["reason"], "job_id": None, "shard": None, "names_shards": None,
             "same_file_as": None}
    if data is None:
        return entry, None, fid
    try:
        raw = raw_named(data, doc, inv) if known else None          # the byte scan, before any parsing
    except SCAN_ERRORS as e:
        entry["reason"] = "byte scan failed (%s)" % type(e).__name__   # never reaches the grammar
        return entry, None, fid
    obj, why = parse_served(data)
    if obj is None:
        entry.update(reason=why, names_shards=sorted(raw) if raw is not None else None)
        return entry, None, fid
    try:
        raw = raw if raw is None else raw | raw_named(obj["logs_content"].encode("utf-8"), doc, inv)  # the decoded scan
    except SCAN_ERRORS as e:
        entry["reason"] = "decoded scan failed (%s)" % type(e).__name__
        return entry, None, fid
    try:
        parsed = (shard_of(obj), shards_named(obj, doc)) if known else (None, set())   # the parsed readings
    except SCAN_ERRORS as e:
        entry["reason"] = "parsed scan failed (%s)" % type(e).__name__
        return entry, None, fid
    entry.update(status="accepted", reason=None, job_id=obj["job_id"], shard=inv.get(obj["job_id"]),
                 names_shards=sorted(raw) if raw is not None else None)
    return entry, (obj, raw, parsed), fid


def evaluate(load, served_files, outp, head):
    """S3-S10 (TRUST-BOUNDARY.md 3): read every input, decide, write nothing. An exception that no check foresaw
    becomes an internal quarantine (S10). A host failure (MemoryError, an OSError that is not a file's own
    condition) and an interrupt are not caught here: the run is ABORTED (2.5, the boundary)."""
    P = lambda s: emit(outp, s)  # noqa: E731
    st = {"stage": "S3", "doc": None, "job_index": None, "run_id": None,
          "inputs": {"runs_json": None, "jobs_list": None}, "runs_sha256": None, "files": [], "expected": None,
          "quarantine": [], "failed": [], "voids": [], "shards": {}, "table": [], "verdict": "FAILS",
          "eligible": 0}
    try:
        _evaluate(load, served_files, P, st)
    except (MemoryError, OSError):   # a host failure is never an internal quarantine: ABORTED (2.5)
        raise
    except Exception as e:  # noqa: BLE001 - S10: quarantine, never a traceback
        st["quarantine"].append({"kind": "internal", "stage": st["stage"], "exception": type(e).__name__})
        P("COLLECT FAIL internal error at %s: %s; the whole collection is quarantined" % (st["stage"], type(e).__name__))
        st.update(verdict="FAILS", shards={}, eligible=0)
        try:
            st["table"] = [{"run_id": c["run_id"], "shard": c["shard"], "expires": c["expires"], "eligible": False,
                            "verdict": None, "reason": "the collection is quarantined (internal error at %s)"
                            % st["stage"]} for c in (st["doc"]["runs"] if st["doc"] is not None else [])]
        except Exception:  # noqa: BLE001 - a run set too malformed to list
            st["table"] = []
    return st


def _evaluate(load, served_files, P, st):
    doc, job_index, run_id, inputs, runs_sha256, input_q = load()
    st.update(doc=doc, job_index=job_index, run_id=run_id, inputs=inputs, runs_sha256=runs_sha256)
    known = doc is not None and job_index is not None   # the run set and the index: attribution can run
    inv = {j: k for k, j in job_index.items()} if job_index is not None else {}
    bad, answers = False, []
    voided, quarantine, failed = {}, st["quarantine"], st["failed"]
    quarantine.extend(input_q)
    # S5, the intake (2.5): every served argument, in argument order, whatever S3 and S4 gave. Every file is read
    # before anything is decided; the decisions below depend only on the set of answers. A scan's ValueError rejects
    # its file (the per-file catch); a host failure, an interrupt or a bug propagates, after the COLLECT FILE lines
    # of the files already taken in.
    st["stage"] = "S5"
    files, objs, ids, fids = st["files"], {}, {}, {}
    try:
        for i, path in enumerate(served_files):
            entry, got, fid = _take_in(i, path, doc, inv, known)
            entry["same_file_as"] = ids.get(fid) if fid is not None else None
            if fid is not None:
                ids.setdefault(fid, i)
            fids[i] = fid
            files.append(entry)
            if got is not None:
                objs[i] = got
    except BaseException:
        _file_lines(P, files)
        raise
    by_name = {}
    for e in files:
        by_name.setdefault(e["name"], []).append(e)
    for es in by_name.values():   # the record names files by basename, so two different files may not share one
        if len(es) > 1 and (len({fids[e["arg"]] for e in es}) > 1 or fids[es[0]["arg"]] is None):
            for e in es:
                e.update(status="rejected", reason="another served file has the same name", job_id=None, shard=None)
                objs.pop(e["arg"], None)
    for e in files:
        if e["status"] == "rejected":
            # It cannot be attributed reliably, so the whole collection is quarantined, whatever it seems to name.
            quarantine.append({"kind": "unattributable", "file": e["name"], "sha256": e["sha256"], "size": e["size"],
                               "reason": e["reason"], "names_shards": e["names_shards"]})
    _file_lines(P, files)
    st["stage"] = "S6"
    for i in sorted(objs) if known else []:
        obj, raw, (so, sn) = objs[i]
        answers.append((files[i]["name"], obj, files[i]["sha256"], so, sn, raw, i))
    # The job rule. An answer belongs to the shard the job index gives its job id: trusted metadata (the extraction
    # run's jobs list and the tool's job id), never the log's own banner. A banner can only add a shard to the
    # shards a job is involved with, never choose one. A job involved with two or more shards voids every one of
    # them; a job whose answers differ, or one of whose answers has no readable banner, voids its shard; an answer
    # of a job outside the run voids the shard its banner names.
    by_job = {}
    for a in answers:
        by_job.setdefault(a[1]["job_id"], []).append(a)
    for job in sorted(by_job):
        ans = by_job[job]
        named = set().union(*(a[4] for a in ans))
        named |= set().union(*(a[5] for a in ans))  # the raw scan of every answer
        if job not in inv and not named:
            for a in ans:   # no trusted job and no recoverable shard identifier: it cannot be attributed
                quarantine.append({"kind": "unattributable", "file": a[0], "sha256": a[2], "size": files[a[6]]["size"],
                                   "reason": "job %s is no job of the run and the file "
                                   "names no shard" % job, "names_shards": []})
            continue
        if job not in inv:
            P("COLLECT FAIL job %s (%s) is no job of the extraction run; shard %s is void"
              % (job, ", ".join(sorted(esc(a[0]) for a in ans)), sorted(named)))
            bad = True  # an answer of a job outside the run
            for s_ in sorted(named):
                voided.setdefault(s_, set()).add("an answer of job %s, which is no job of the run, names it" % job)
            continue
        involved = named | {inv[job]}
        if len(involved) > 1:
            P("COLLECT FAIL job %s answers for shards %s: every one of them is void" % (job, sorted(involved)))
            bad = True
            for s_ in sorted(involved):  # every shard involved
                voided.setdefault(s_, set()).add("job %s answers for shards %s" % (job, sorted(involved)))
        elif len({identity(a[1]) for a in ans}) > 1:
            P("COLLECT UNVERIFIED job %s: %d answers that differ (%s); shard %d is void"
              % (job, len(ans), ", ".join(sorted(esc(a[0]) for a in ans)), inv[job]))
            voided.setdefault(inv[job], set()).add("answers of job %s differ" % job)
        elif any(a[3] is None for a in ans):
            P("COLLECT UNVERIFIED job %s: an answer with no readable banner (%s); shard %d is void"
              % (job, ", ".join(sorted(esc(a[0]) for a in ans)), inv[job]))
            voided.setdefault(inv[job], set()).add("an answer of job %s has no readable banner" % job)
    st["stage"] = "S8"
    shards, why, runs_seen = st["shards"], {}, {}
    for k in sorted({inv[j] for j in by_job if j in inv} | set(voided)):
        if k in voided:
            shards[k], why[k] = None, "; ".join(sorted(voided[k]))
            continue
        copies = by_job[job_index[k]]
        name, obj, dig = sorted(copies, key=lambda c: c[0])[0][:3]
        digests = sorted({c[2] for c in copies})   # every copy's digest (N3)
        if len(copies) > 1:
            P("COLLECT NOTE shard %d: %d identical copies of job %s, taken once" % (k, len(copies), job_index[k]))
        kk, probs, res = read_shard(obj, doc, job_index, k)
        for p in probs:
            P("COLLECT FAIL %s: %s" % (esc(name), p))
        if probs:
            bad = True
            failed.append({"file": name, "sha256": dig, "sha256s": digests, "shard": k, "problems": probs})  # traceability
            shards[k], why[k] = None, "failed a check"
            continue
        shards[k] = {"file": name, "files": sorted(c[0] for c in copies), "served_sha256": dig, "sha256s": digests,
                     "job_id": obj["job_id"], "copies": len(copies), "runs": res}
        for rid in res:
            runs_seen.setdefault(rid, []).append(k)
    st["stage"] = "S7"
    nsh = doc["shards"] if doc is not None else 0
    for k in range(1, (nsh if job_index is not None else 0) + 1):
        if job_index.get(k) not in by_job:   # the expected answer of shard k was not served
            quarantine.append({"kind": "missing", "shard": k, "job_id": job_index.get(k),
                               "expected": "the job-log answer of job %s (%s)" % (job_index.get(k), JOB_NAME % k)})
    if doc is not None:
        expected = []
        for k in range(1, nsh + 1):
            j = job_index.get(k) if job_index is not None else None
            cps = sorted(({"arg": a[6], "name": a[0], "size": files[a[6]]["size"], "sha256": a[2]}
                          for a in by_job.get(j, [])), key=lambda c: c["arg"]) if j is not None else []
            expected.append({"shard": k, "job_name": JOB_NAME % k, "job_id": j,
                             "status": "undetermined" if job_index is None else "present" if cps else "missing",
                             "copies": cps, "candidates": [e["arg"] for e in files if e["status"] == "rejected"
                                                           and k in (e["names_shards"] or [])]})
        st["expected"] = expected
    for q in quarantine:
        if q["kind"] == "missing":
            P("COLLECT FAIL missing: %s; the whole collection is quarantined" % q["expected"])
        elif q["kind"] == "input":
            P("COLLECT FAIL %s %s (sha256 %s): %s; the whole collection is quarantined"
              % (q["input"], esc(q["name"]), q["sha256"], esc(q["reason"])))
        else:
            P("COLLECT FAIL %s (sha256 %s): %s; the whole collection is quarantined" % (esc(q["file"]), q["sha256"], esc(q["reason"])))
    # Each run's own result: eligible when its shard passed every check and its RESULT is HOLDS. This is diagnostic
    # only. Whether any run is usable is decided once, in write_collection, from the verdict of the whole collection.
    st["stage"] = "S9"
    runs_cfg = doc["runs"] if doc is not None else []
    table = st["table"]
    for cfg in runs_cfg:
        rid, k = cfg["run_id"], cfg["shard"]
        sh = shards.get(k)
        entry = {"run_id": rid, "shard": k, "expires": cfg["expires"], "eligible": False}
        if quarantine:
            entry.update(verdict=None, reason="the collection is quarantined (%s)" % ", ".join(
                _q_label(q) for q in quarantine))
        elif sh is None:
            entry.update(verdict=None, reason="shard %d %s" % (k, why.get(k, "not collected")))
        elif len(runs_seen.get(rid, [])) != 1:
            entry.update(verdict=None, reason="run seen in shards %s" % runs_seen.get(rid))
        else:
            v_, body = sh["runs"][rid]
            entry.update(verdict=v_, served_sha256=sh["served_sha256"], file=sh["file"], job_id=sh["job_id"])
            if v_ == "HOLDS":
                entry.update(eligible=True, sha256=hashlib.sha256(body.encode()).hexdigest(),
                             outcome=BLOCK_DECODER.decode(body)["expected"]["outcome"], _body=body)
            else:
                entry.update(reason="the run's verdict is %s" % v_)
        table.append(entry)
    extra = sorted(set(runs_seen) - {r["run_id"] for r in runs_cfg})
    for rid in extra:
        P("COLLECT FAIL run %s is not in runs.json" % rid)
    missing = sorted(set(range(1, nsh + 1)) - set(shards))
    if missing and not quarantine:
        P("COLLECT UNVERIFIED shards not collected: %s" % missing)
    st["stage"] = "S10"
    eligible = sum(1 for e in table if e["eligible"])
    fails = bad or extra or quarantine or any(e.get("verdict") == "FAILS" for e in table)
    v = "FAILS" if fails else "HOLDS" if runs_cfg and eligible == len(runs_cfg) and not missing else "UNVERIFIED"
    st["voids"] = [{"shard": k_, "reasons": sorted(r_)} for k_, r_ in sorted(voided.items())]
    st.update(verdict=v, eligible=eligible)


def run_collection(load, served_files, out, outp=None, head=None, durable=True):
    """S1-S12 (TRUST-BOUNDARY.md 3-4); returns the exit code, 0 to 5, and never raises."""
    outp = outp or sys.stdout
    P = lambda s: emit(outp, s)  # noqa: E731
    phase, said, v = "S1", False, "FAILS"
    try:
        out = os.path.abspath(out)
        parent = os.path.dirname(out)
        if not os.path.isdir(parent):
            P("COLLECT REFUSED the output location's parent is not a directory; --out is not a result of this invocation")
            return 3
        if os.path.lexists(out):
            P("COLLECT REFUSED the output location exists; --out is not a result of this invocation")
            return 3
        phase = "S2"
        nonce = os.urandom(16).hex()
        staging = os.path.join(parent, ".%s.staging-%s" % (os.path.basename(out), nonce))
        os.mkdir(staging, 0o700)
        started = _utc()
        phase = "S3"
        st = evaluate(load, served_files, outp, head)
        phase = "S11"
        v = st["verdict"]
        extra = {"runs_sha256": st["runs_sha256"], "files": st["files"], "expected": st["expected"],
                 "collection": {"nonce": nonce, "started_utc": started, "out_name": os.path.basename(out),
                                "inputs": dict(st["inputs"], head=None if head is None else str(head)[:100])}}
        target = staging
        usable, digest = write_collection(target, st["table"], v, st["quarantine"], st["shards"], st["run_id"], head,
                                          st["failed"], st["voids"], extra=extra, durable=durable)
        phase = "S12"
        os.rename(staging, out)  # the commit point: out appears whole, or not at all
        phase = "published"
        nruns = len(st["table"])
        for e in st["table"]:
            P("RUN %s shard %d expires %s %s%s" % (e["run_id"], e["shard"], e["expires"], e.get("verdict"),
                                                   (" " + e.get("outcome", "")) if e["usable"] else
                                                   " not usable: " + (e.get("reason") or "the collection's verdict is %s" % v)))
        P("COLLECT %d of %d runs passed every check of their shard" % (st["eligible"], nruns))
        P("COLLECT %d of %d runs usable" % (usable, nruns))
        P("COLLECT PUBLISHED %s nonce %s collected.json sha256 %s" % (esc(out), nonce, digest))
        said = True
        _sync_dir(parent, durable)
        P("COLLECT %s" % v)
        return {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[v]
    except BaseException as e:  # noqa: BLE001 - every path gets a code; nothing leaves uncaught
        try:
            if phase == "S1":
                P("COLLECT REFUSED %s; --out is not a result of this invocation" % _errname(e))
                return 3
            if phase != "published":
                P("COLLECT ABORTED %s" % _errname(e))
                return 4
            if not said:
                P("COLLECT PUBLISHED %s nonce %s collected.json sha256 %s" % (esc(out), nonce, digest))
            P("COLLECT NOT DURABLE %s" % _errname(e))
            P("COLLECT %s" % v)
        except BaseException:  # noqa: BLE001 - the output itself failed; the code still stands
            pass
        return 3 if phase == "S1" else 4 if phase != "published" else 5


def collect(doc, served_files, out, job_index, run_id=None, outp=None, head=None, durable=True):
    """A collection from a run set and job index given directly (the self-test's entry): S1-S12, with
    collection.inputs.runs_json, inputs.jobs_list and the top-level runs_sha256 recorded as null (section 4, A2).
    Returns the exit code."""
    return run_collection(lambda: (doc, job_index, run_id, {"runs_json": None, "jobs_list": None}, None, []),
                          served_files, out, outp, head, durable)


def load_inputs(runs_path, jobs_path, head):
    """S3-S4: the run set and the job index, each file read once (2.5 steps 1-2) and parsed strictly (2.3)."""
    q = []
    rrec, data = read_input(runs_path)
    rrec.pop("_id")
    runs_meta = {"name": rrec["name"], "size": rrec["size"], "sha256": rrec["sha256"],
                 "pinned": rrec["sha256"] == RUNS_SHA256}
    doc, runs_sha, why = None, None, rrec["reason"]
    if why is None:
        if not runs_meta["pinned"]:
            why = "runs.json is not the pinned file"
        else:
            doc, why = _decode_strict(data, JOBS_DECODER, False)
            runs_sha = rrec["sha256"] if doc is not None else None
    if why is not None:
        q.append({"kind": "input", "input": "runs.json", "name": rrec["name"], "file_kind": rrec["kind"],
                  "size": rrec["size"], "sha256": rrec["sha256"], "pinned": runs_meta["pinned"], "reason": why})
    jrec, jdata = read_input(jobs_path)
    jrec.pop("_id")
    jobs_meta = {"name": jrec["name"], "size": jrec["size"], "sha256": jrec["sha256"]}
    index, run_id = None, None
    probs = [jrec["reason"]] if jrec["reason"] is not None else []
    if not probs:
        jobsd, jwhy = _decode_strict(jdata, JOBS_DECODER, False)
        if jobsd is None:
            probs = [jwhy]
        elif doc is not None:
            index, run_id, probs = build_job_index(jobsd, head, doc["shards"])
    if probs:
        q.append({"kind": "input", "input": "jobs list", "name": jrec["name"], "file_kind": jrec["kind"],
                  "size": jrec["size"], "sha256": jrec["sha256"], "problems": probs, "reason": "; ".join(probs)})
        index = None
    return doc, index, run_id, {"runs_json": runs_meta, "jobs_list": jobs_meta}, runs_sha, q


# ------------------------------------------------------------------------------------------------ self-test

def _result(cfg):
    return {"kind": "cited-bridge", "commit": cfg["head_sha"], "expected": {"outcome": "gate-verdict"},
            "run": {"id": cfg["run_id"], "job_id": cfg["bridge_job_id"], "head_sha": cfg["head_sha"]},
            "source": {"extractor_blob": EXTRACT_RESULT_BLOB, "extractor_commit": MAIN_COMMIT,
                       "assembler_blob": ASSEMBLER_BLOB, "host_reader_blob": HOST_BLOB, "runs_sha256": RUNS_SHA256}}


def _shard_text(doc, k, verdicts=None, mut=None):
    """A shard log as assemble.py prints it, inside runner lines, timestamped, as the job-log tool serves it."""
    mut = mut or {}
    exp = [r for r in doc["runs"] if r["shard"] == k]
    verdicts = verdicts or {}
    L = ["Current runner version: '2.337.0'", "##[group]Run python3 -I batchx/assemble.py", "##[endgroup]",
         "BATCH ci-batch-extract shard %d/%d: assembler %s, host reader %s, extract_result %s at %s, runs.json %s"
         % (k, doc["shards"], ASSEMBLER_BLOB[:12], mut.get("host_prefix", HOST_BLOB[:12]), EXTRACT_RESULT_BLOB[:12],
            MAIN_COMMIT[:12], RUNS_SHA256[:12]),
         ("BATCH SHARD %d/%d RUNSET not-a-digest RUNS %d" % (k, doc["shards"], len(exp))) if mut.get("malformed_banner") else
         "BATCH SHARD %d/%d RUNSET %s RUNS %d" % (k, doc["shards"], mut.get("runset", runset_digest([r["run_id"] for r in exp])), len(exp))]
    endl = mut.get("end_line", "BATCH END shard %d/%d: assembler %s" % (k, doc["shards"], ASSEMBLER_BLOB[:12]))
    vline0 = "EXTRACT SHARD %d/%d %s" % (k, doc["shards"], mut.get("outside_verdict", "HOLDS"))
    if mut.get("dup_start"):
        L.insert(4, L[3])
    if mut.get("end_first"):
        L.insert(3, endl)
    if mut.get("verdict_before_start"):
        L.insert(3, vline0)
    rs = exp + mut.get("extra_runs", [])
    for r in rs:
        if r["run_id"] in mut.get("drop_result", []):
            continue
        L.append("RESULT %s %s gate-verdict (15 checks, 0 failed, 0 unverified)" % (r["run_id"], verdicts.get(r["run_id"], "HOLDS")))
    L += mut.get("extra_lines", [])
    vs = [verdicts.get(r["run_id"], "HOLDS") for r in exp]
    v = mut.get("verdict") or ("FAILS" if "FAILS" in vs else "HOLDS" if all(x == "HOLDS" for x in vs) else "UNVERIFIED")
    vline = "EXTRACT SHARD %d/%d %s" % (k, doc["shards"], v)
    if mut.get("verdict_early"):
        L.append(vline)
    for r in rs:
        rv = verdicts.get(r["run_id"], "HOLDS")
        if rv != "HOLDS" and r["run_id"] not in mut.get("block_for", []):
            continue
        res = _result(r)
        res.update(mut.get("edit_result", {}).get(r["run_id"], {}))
        for key, val in mut.get("edit_source", {}).get(r["run_id"], {}).items():
            res["source"][key] = val
        body = json.dumps(res, indent=1, sort_keys=True) + "\n"
        sha = hashlib.sha256(body.encode()).hexdigest()
        if r["run_id"] in mut.get("tamper", []):
            body = body.replace('"gate-verdict"', '"build-failed"')
        L.append("===== BEGIN EXPECTED RESULT ci/%s/results.json =====" % r["run_id"])
        L += body.rstrip("\n").split("\n")
        L.append("===== END EXPECTED RESULT ci/%s/results.json =====" % r["run_id"])
        L.append("SHA256 ci/%s/results.json %s" % (r["run_id"], sha))
    if mut.get("stopped"):
        L.append("CHECK all UNVERIFIED stopped: OSError: [Errno 28] No space left on device")
    if not mut.get("verdict_early") and not mut.get("no_verdict") and not mut.get("died"):
        L.append(vline)
        if mut.get("two_inside"):
            L.append(vline)
    if not mut.get("died") and not mut.get("no_end") and not mut.get("end_first"):
        L.append(endl)
        if mut.get("dup_end"):
            L.append(endl)
    if mut.get("second_verdict"):
        L.append(vline)
    if mut.get("verdict_after_end"):
        L.append(vline0)
    L += ["##[error]Process completed with exit code 1."] if v != "HOLDS" or mut.get("died") else []
    L += ["Post job cleanup."] + mut.get("extra_trailer", []) + (["EXTRACT SHARD %d/%d %s" % (k, doc["shards"], v)] if mut.get("verdict_in_trailer") else []) \
        + ["[command]/usr/bin/git config --local --unset-all x"] * mut.get("trailer", 2) + ["Cleaning up orphan processes"]
    if mut.get("pad_to"):
        L += ["##[warning]padding"] * (mut["pad_to"] - len(L))
    if mut.get("tool"):   # a runner line with <, >, &, raw non-ASCII and ANSI codes, as real logs have them
        L.insert(1, "##[group]Run echo 'a < b > c & d' " + chr(0xe9) + chr(0x2014) + " " + chr(27) + "[36;1mx"
                 + chr(27) + "[0m")
    text = "\n".join("2026-12-01T10:00:%02d.0000000Z %s" % (i % 60, l) for i, l in enumerate(L))
    orig = len(L) + mut.get("orig_delta", 0)
    if mut.get("tail"):
        text = "\n".join(text.split("\n")[mut["tail"]:])
    if mut.get("tool"):   # the real tool's byte format: U+FEFF first, the success message (TRUST-BOUNDARY.md 2.1)
        return _tool_json({"job_id": mut.get("job_id", 77000 + k), "logs_content": chr(0xfeff) + text,
                           "message": SUCCESS_MESSAGE, "original_length": orig})
    return json.dumps({"job_id": mut.get("job_id", 77000 + k), "logs_content": text, "original_length": orig})


def _tool_json(obj):
    """obj in the job-log tool's byte format (TRUST-BOUNDARY.md 2.1): compact, sorted keys, raw UTF-8, and <, >, &,
    U+2028 and U+2029 written as JSON escapes."""
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    for c in "<>&" + chr(0x2028) + chr(0x2029):
        s = s.replace(c, "\\" + "u%04x" % ord(c))
    return s


def self_test(work=None):
    base = tempfile.mkdtemp(prefix="collect-selftest-", dir=work)
    fails, n = 0, 0
    runs = [{"run_id": str(800 + i), "bridge_job_id": str(8800 + i), "head_sha": "%040x" % i, "shard": 1 + i // 2,
             "expires": "2026-12-2%d" % (i // 2)} for i in range(6)]
    doc = {"shards": 3, "runs": runs}
    index = {k: 77000 + k for k in (1, 2, 3)}
    HEAD = "c" * 40
    print("collect self-test (synthetic served shard logs, no network):")
    try:
        FILE_KEYS = ("arg", "name", "kind", "size", "sha256", "status", "reason")

        def harness(d, out, written, text, err):
            """The harness rules of TRUST-BOUNDARY.md 6, checked on what is on disk: (ok, collected.json, problems).
            written maps an argument number to the bytes the test itself wrote there."""
            hp = []
            try:
                with open(os.path.join(out, "collected.json"), encoding="utf-8") as f_:
                    cj_ = json.load(f_)
            except (OSError, ValueError):
                return False, None, ["1: no collected.json on disk"]
            nu = sum(1 for e in cj_["runs"] if e["usable"])
            if cj_.get("quarantined") is not (cj_["verdict"] != "HOLDS"):
                hp.append("2: quarantined is not verdict != HOLDS")
            if nu != (len(cj_["runs"]) if cj_["verdict"] == "HOLDS" else 0):
                hp.append("2: usable count")
            man = (cj_.get("collection") or {}).get("manifest", [])
            listing = sorted(os.path.relpath(os.path.join(r_, f_), out) for r_, _, fs_ in os.walk(out) for f_ in fs_)
            if listing != sorted(["collected.json"] + [m["path"] for m in man]):
                hp.append("3: listing %s" % listing)
            for m in man:
                with open(os.path.join(out, m["path"]), "rb") as f_:
                    b_ = f_.read()
                if (len(b_), hashlib.sha256(b_).hexdigest()) != (m["size"], m["sha256"]):
                    hp.append("3: manifest digest")
            if not nu and os.path.exists(os.path.join(out, "ci")):
                hp.append("3: a ci/ directory without a usable run")
            if any(x.startswith(".%s.staging-" % os.path.basename(out)) for x in os.listdir(d)):
                hp.append("4: a staging directory remains")
            for i, b_ in written.items():
                fe = cj_["files"][i] if i < len(cj_["files"]) else {}
                if (fe.get("size"), fe.get("sha256")) != (len(b_), hashlib.sha256(b_).hexdigest()):
                    hp.append("5: file %d's size and sha256" % i)
            fl = [json.loads(l[len("COLLECT FILE "):]) for l in text.split("\n") if l.startswith("COLLECT FILE ")]
            if fl != [{k: fe[k] for k in FILE_KEYS} for fe in cj_["files"]]:
                hp.append("6: the COLLECT FILE lines")
            if any(not all(" " <= c <= "~" for c in l) for l in text.split("\n")):
                hp.append("7: a stdout line that is not printable ASCII")
            if err:
                hp.append("7: stderr is not empty")
            return not hp, cj_, hp

        def write_items(d, items):
            """items: [(name relative to d, payload)]. A payload is bytes, a str (written as UTF-8), or ("dir",),
            ("missing",), ("fifo",), ("same", j) (item j's path again), ("hardlink", j), ("symlink_to", bytes)
            (a link to a file the test writes outside the served set), ("sparse", size) or ("rawpath",) (the name
            as a path, nothing created: e.g. a path through a regular file)."""
            paths, written = [], {}
            for i, (nm, pl) in enumerate(items):
                p = os.path.join(d, nm)
                if not (isinstance(pl, tuple) and pl[0] in ("rawpath", "missing")):
                    os.makedirs(os.path.dirname(p), exist_ok=True)
                if isinstance(pl, (bytes, str)):
                    b_ = pl if isinstance(pl, bytes) else pl.encode("utf-8")
                    with open(p, "wb") as f_:
                        f_.write(b_)
                    written[i] = b_
                elif pl[0] == "dir":
                    os.mkdir(p)
                elif pl[0] == "fifo":
                    os.mkfifo(p)
                elif pl[0] == "same":
                    p = paths[pl[1]]
                    written[i] = written[pl[1]]
                elif pl[0] == "hardlink":
                    os.link(paths[pl[1]], p)
                    written[i] = written[pl[1]]
                elif pl[0] == "symlink_to":
                    tp = os.path.abspath(os.path.join(d, "targets", "target-%d" % i))
                    os.makedirs(os.path.dirname(tp), exist_ok=True)
                    with open(tp, "wb") as f_:
                        f_.write(pl[1])
                    os.symlink(tp, p)
                elif pl[0] == "sparse":
                    with open(p, "wb") as f_:
                        f_.truncate(pl[1])
                paths.append(p)   # ("missing",) is a path the test never creates
            return paths, written

        def coll(items, ix=None, dc=None, durable=False, pre=None, setup=None, out_name="out"):
            """One collection of items through collect(), with stdout and stderr captured, read back from disk
            under the harness rules (not for the refused and aborted outcomes, which publish nothing)."""
            d = tempfile.mkdtemp(dir=base)
            paths, written = write_items(d, items)
            out = os.path.join(d, out_name)
            if pre:
                pre(out)
            undo = setup(d) if setup else None
            buf, err = io.StringIO(), io.StringIO()
            try:
                with contextlib.redirect_stderr(err):
                    code = collect(dc or doc, paths, out, index if ix is None else ix, 42, buf, head=HEAD,
                                   durable=durable)
            finally:
                if undo:
                    undo()
            t = buf.getvalue()
            hok, cj, hp = harness(d, out, written, t, err.getvalue()) if code not in (3, 4) else (None, None, [])
            return {"code": code, "t": t, "err": err.getvalue(), "cj": cj, "hok": hok, "hp": hp, "d": d, "out": out,
                    "paths": paths, "written": written}

        def case(name, texts, want, needle=None, usable=None, absent=None, bytes_=False, extra=None):
            nonlocal fails, n
            n += 1
            R = coll([("served-%d.json" % i, t.encode("latin-1") if bytes_ and i == len(texts) - 1 else t)
                      for i, t in enumerate(texts)])
            d, code, t = R["d"], R["code"], R["t"]
            ok = t.rstrip("\n").split("\n")[-1] == "COLLECT " + want and code == {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[want]
            ok = ok and bool(R["hok"]) and (extra is None or extra(R["cj"]))
            ok = ok and (needle is None or needle in t) and (absent is None or absent not in t)
            # usable= is the number of runs that pass their own shard's checks (eligible); the governing invariant,
            # checked in every case: runs are usable, and result files written, only under a HOLDS verdict
            if usable is not None:
                ok = ok and ("COLLECT %d of 6 runs passed every check of their shard" % usable) in t
            cj_ = json.load(open(os.path.join(d, "out", "collected.json")))
            n_use = sum(1 for e in cj_["runs"] if e["usable"])
            n_elig = sum(1 for e in cj_["runs"] if e["eligible"])
            written = sorted(os.listdir(os.path.join(d, "out", "ci"))) if os.path.isdir(os.path.join(d, "out", "ci")) else []
            ok = ok and cj_["verdict"] == want and n_use == (n_elig if want == "HOLDS" else 0) == len(written) \
                and ("COLLECT %d of 6 runs usable" % n_use) in t
            print("  %s  %s -> COLLECT %s" % ("ok  " if ok else "FAIL", name, t.rstrip("\n").split("\n")[-1].split()[-1]))
            if not ok:
                fails += 1
                print("\n".join("        | " + l for l in t.split("\n") if l.startswith("COLLECT")
                                and not l.startswith("COLLECT FILE ")))
                if R["hp"]:
                    print("        | harness: %s" % R["hp"])
            return d, t

        def chk(name, cond):
            nonlocal fails, n
            n += 1
            print("  %s  %s" % ("ok  " if cond else "FAIL", name))
            fails += not cond

        S = lambda k, verdicts=None, **mut: _shard_text(doc, k, verdicts, mut)  # noqa: E731
        d, _ = case("three whole shards, every run holding", [S(1), S(2), S(3)], "HOLDS", usable=6)
        f800 = os.path.join(d, "out", "ci", "800", "results.json")
        got = open(f800).read() if os.path.exists(f800) else None
        chk("the written file is byte-identical to the canonical block",
            got == json.dumps(_result(runs[0]), indent=1, sort_keys=True) + "\n")
        cj = json.load(open(os.path.join(d, "out", "collected.json")))
        chk("collected.json records each shard's job id, the extraction run and the pinned blobs",
            {k: v["job_id"] for k, v in cj["shards"].items()} == {"1": 77001, "2": 77002, "3": 77003}
            and cj["extraction_run"] == 42 and cj["collector"]["pins"]["assembler_blob"] == ASSEMBLER_BLOB
            and all(e["job_id"] == 77000 + e["shard"] for e in cj["runs"]))
        # R4: exact identities, in separate fields
        chk("[R4a] collected.json records the full 40-hex launched commit, the --head value the job index required",
            cj.get("launched_commit") == HEAD and re.fullmatch(r"[0-9a-f]{40}", cj["launched_commit"])
            and "every job of extraction_run's jobs list is at launched_commit" in cj.get("launched_commit_check", ""))
        # the expected identity is computed here, independently of collector_identity(): git asked directly, and the
        # executed bytes hashed directly
        here = os.path.abspath(__file__)
        genv0 = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")

        def g(*args):
            p_ = subprocess.run(["git", "-C", os.path.dirname(here)] + list(args), capture_output=True, text=True,
                                env=genv0, timeout=60)
            return p_.stdout.strip() if p_.returncode == 0 else None
        exp_commit = g("rev-parse", "--verify", "HEAD")
        exp_rel = g("ls-files", "--full-name", "--", os.path.basename(here))
        exp_blob = g("rev-parse", "--verify", "HEAD:%s" % exp_rel) if exp_commit and exp_rel else None
        data_ = open(here, "rb").read()
        exp_exec = hashlib.sha1(("blob %d\0" % len(data_)).encode() + data_).hexdigest()
        c_ = cj["collector"]
        chk("[R4b] collected.json's collector fields equal git's own answers and the executed bytes' digests",
            c_.get("commit") == exp_commit and c_.get("committed_blob") == exp_blob and c_.get("path") == exp_rel
            and c_.get("executed_sha256") == hashlib.sha256(data_).hexdigest() and c_.get("executed_blob") == exp_exec
            and c_.get("executed_matches_committed_blob") == (exp_blob is not None and exp_blob == exp_exec)
            and c_.get("pins", {}).get("extractor_blob") == EXTRACT_RESULT_BLOB
            and "launched_commit" not in c_ and cj.get("launched_commit") not in (c_.get("commit"), c_.get("committed_blob")))
        n += 1
        gd = os.path.join(base, "repo")
        os.makedirs(os.path.join(gd, "batchx"))
        src = open(os.path.abspath(__file__), "rb").read()
        gp = os.path.join(gd, "batchx", "collect.py")
        with open(gp, "wb") as f:
            f.write(src)
        genv = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        for args in (["init", "-q"], ["add", "-A"], ["-c", "user.name=t", "-c", "user.email=t@example.invalid",
                                                       "-c", "commit.gpgsign=false", "commit", "-q", "-m", "c"]):
            subprocess.run(["git", "-C", gd] + args, check=True, capture_output=True, env=genv, timeout=60)
        head_c = subprocess.run(["git", "-C", gd, "rev-parse", "HEAD"], capture_output=True, text=True, env=genv).stdout.strip()
        id1 = collector_identity(gp)
        with open(gp, "ab") as f:
            f.write(b"# a local, uncommitted change\n")
        id2 = collector_identity(gp)
        ok = (id1["commit"] == head_c and id1["path"] == "batchx/collect.py" and id1["committed_blob"] == git_blob_id(src)
              and id1["executed_blob"] == git_blob_id(src) and id1["executed_matches_committed_blob"] is True
              and id1["executed_sha256"] == hashlib.sha256(src).hexdigest() and id1["commit"] != HEAD
              and id2["commit"] == head_c and id2["committed_blob"] == git_blob_id(src)
              and id2["executed_matches_committed_blob"] is False and id2["executed_sha256"] != id1["executed_sha256"])
        print("  %s  [R4c] the collector's commit and committed blob come from git, and local uncommitted changes are "
              "recorded by the executed bytes' sha256 and a false match flag" % ("ok  " if ok else "FAIL"))
        fails += not ok
        n += 1
        _, _, pr4 = build_job_index({"total_count": 0, "jobs": []}, "c" * 12, 3)
        ok = bool(pr4) and "not a full 40-hex sha" in pr4[0]
        print("  %s  [R4d] a launched commit that is not a full 40-hex sha is refused" % ("ok  " if ok else "FAIL"))
        fails += not ok
        case("the same shards in another order", [S(3), S(1), S(2)], "HOLDS", usable=6)
        case("a shard served as a tail is refused", [S(1, tail=2), S(2), S(3)], "FAILS", "not whole", usable=4)
        case("a served line count other than original_length is refused", [S(1, orig_delta=1), S(2), S(3)], "FAILS",
             "not whole", usable=4)
        case("a shard missing quarantines the whole collection", [S(1), S(2)], "FAILS",
             "missing: the job-log answer of job 77003 (Extract shard 3)", usable=0)
        case("a RUNSET digest other than runs.json's", [S(1, runset="0" * 64), S(2), S(3)], "FAILS", "banner does not match",
             usable=4)
        case("a run's RESULT line missing", [S(1, drop_result=["800"]), S(2), S(3)], "FAILS", "RESULT lines for", usable=4)
        case("an extra run of shard 2 in shard 1's log voids shards 1 and 2", [S(1, extra_runs=[dict(runs[2])]), S(2), S(3)],
             "FAILS", "job 77001 answers for shards [1, 2]", usable=2)
        case("a tampered block (its SHA256 line no longer matches)", [S(1, tamper=["801"]), S(2), S(3)], "FAILS",
             "does not match its SHA256 line", usable=4)
        case("a block for a run that does not hold", [S(1, verdicts={"800": "UNVERIFIED"}, block_for=["800"]), S(2), S(3)],
             "FAILS", "a block for run 800", usable=4)
        case("a block naming another head", [S(1, edit_result={"800": {"commit": "f" * 40}}), S(2), S(3)], "FAILS",
             "not a canonical result of that run", usable=4)
        case("a verdict line at odds with the RESULT lines", [S(1, verdict="HOLDS", verdicts={"800": "FAILS"}), S(2), S(3)],
             "FAILS", "not the one its RESULT lines imply", usable=4)
        case("one run UNVERIFIED: the others are eligible, none usable", [S(1, verdicts={"801": "UNVERIFIED"}), S(2), S(3)],
             "UNVERIFIED", "RUN 801 shard 1 expires 2026-12-20 UNVERIFIED not usable", usable=5)
        case("one run FAILS: the batch FAILS, the others are eligible, none usable", [S(1, verdicts={"801": "FAILS"}), S(2), S(3)],
             "FAILS", "RUN 801 shard 1 expires 2026-12-20 FAILS not usable", usable=5)
        case("a file that is not a job-log answer quarantines the whole collection", ["not json", S(1), S(2), S(3)], "FAILS",
             "the whole collection is quarantined", usable=0)
        # N1: the verdict line
        case("a verdict line followed by 40 runner lines is found", [S(1, trailer=40), S(2, trailer=40), S(3)], "HOLDS",
             usable=6)
        case("a red shard's verdict line with 40 runner lines after it is found and checked",
             [S(1, verdicts={"801": "UNVERIFIED"}, trailer=40), S(2), S(3)], "UNVERIFIED", usable=5, absent="COLLECT FAIL")
        case("no verdict line", [S(1, no_verdict=True), S(2), S(3)], "FAILS", "0 verdict lines, not one", usable=4)
        case("two verdict lines", [S(1, second_verdict=True), S(2), S(3)], "FAILS", "2 verdict lines, not one", usable=4)
        case("a verdict line before the last block", [S(1, verdict_early=True), S(2), S(3)], "FAILS",
             "not the assembler's last line before its end-of-output marker", usable=4)
        # N2: copies
        case("a shard collected twice, byte-identical, is taken once", [S(1), S(1), S(2), S(3)], "HOLDS",
             "2 identical copies of job 77001, taken once", usable=6)
        _, ta = case("a shard collected twice with contradicting content: UNVERIFIED, none taken (good copy first)",
                     [S(1), S(1, verdicts={"800": "UNVERIFIED"}), S(2), S(3)], "UNVERIFIED", "answers that differ", usable=4)
        _, tb = case("  ... and the same with the contradicting copy first",
                     [S(1, verdicts={"800": "UNVERIFIED"}), S(1), S(2), S(3)], "UNVERIFIED", "answers that differ", usable=4)
        chk("  ... and the argument order changes no RUN line", [l for l in ta.split("\n") if l.startswith("RUN ")]
            == [l for l in tb.split("\n") if l.startswith("RUN ")])
        case("copies differing only in a tampered block are UNVERIFIED, whichever comes first",
             [S(1, tamper=["801"]), S(1), S(2), S(3)], "UNVERIFIED", "answers that differ", usable=4)
        # N3: provenance and pins
        case("a log from another job (another push of this branch) is refused and voids the shard it names",
             [S(1), S(1, job_id=99999), S(2), S(3)], "FAILS", 'job 99999 ("served-1.json") is no job of the extraction run', usable=4)
        case("one job serving two shards is refused", [S(1), S(2), S(2, job_id=77001), S(3)], "FAILS",
             "job 77001 answers for shards [1, 2]", usable=2)
        # R1: a job id under two shards voids every shard involved, whatever the shard numbers
        case("[R1a] shard 3's job serving shard 1's content, beside genuine shards 1 and 3, voids both",
             [S(1), S(2), S(3), S(1, job_id=77003)], "FAILS", "job 77003 answers for shards [1, 3]: every one of them is void",
             usable=2)
        case("[R1a] the same with the mislabelled copy first by name", [S(1, job_id=77003), S(1), S(2), S(3)], "FAILS",
             "job 77003 answers for shards [1, 3]: every one of them is void", usable=2)
        # F1: every place a log names a shard counts, so a damaged or reordered banner cannot hide a mislabelled copy
        s1, s3 = json.loads(S(1)), json.loads(S(3))

        def answer(job, *parts):
            text = "\n".join(p_["logs_content"] for p_ in parts)
            return json.dumps({"job_id": job, "logs_content": text, "original_length": len(text.split("\n"))})

        def drop_runset(js):
            o = json.loads(js)
            L_ = [l for l in o["logs_content"].split("\n") if " BATCH SHARD " not in l]
            return json.dumps({"job_id": o["job_id"], "logs_content": "\n".join(L_), "original_length": len(L_)})
        for tag, nm, copy in (
                ("F1a", "with its banner intact", S(1, job_id=77003)),
                ("F1b", "with its RUNSET line malformed", S(1, job_id=77003, malformed_banner=True)),
                ("F1c", "with its RUNSET line deleted", drop_runset(S(1, job_id=77003))),
                ("F1d", "as shard 3's log followed by shard 1's in one answer", answer(77003, s3, s1)),
                ("F1e", "as shard 1's log followed by shard 3's in one answer", answer(77003, s1, s3))):
            case("[%s] shard 3's job serving shard 1's log %s voids shards 1 and 3, only shard 2's runs eligible, none usable"
                 % (tag, nm), [S(1), S(2), S(3), copy], "FAILS", "job 77003 answers for shards [1, 3]", usable=2)
        # G1/G2: the raw scan, before any parsing. Shard 3's job saves shard 1's log, damaged in each way below,
        # beside genuine shards 1, 2 and 3: both shards void, only shard 2's runs usable.
        mis = S(1, job_id=77003)

        def lines_edit(js, f):
            o = json.loads(js)
            L_ = f(o["logs_content"].split("\n"))
            return json.dumps({"job_id": o["job_id"], "logs_content": "\n".join(L_), "original_length": len(L_)})
        TSRE = re.compile(r"^(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d)\.\d+Z ")
        only = lambda line: lines_edit(mis, lambda L: [L[0], "2026-12-01T10:00:01.0000000Z " + line, L[-1]])  # noqa: E731
        o_ = json.loads(mis)
        G = (
            ("G1a", "cut off halfway (not JSON)", mis[: len(mis) // 2]),
            ("G1b", "with its job_id written as a string", json.dumps(dict(o_, job_id="77003"))),
            ("G1c", "wrapped in a tool envelope", json.dumps({"result": o_})),
            ("G1d", "with a byte that is not UTF-8", None),
            ("G2a", "with timestamps without fractional seconds", lines_edit(mis, lambda L: [TSRE.sub(r"\1Z ", l) for l in L])),
            ("G2b", "with an ANSI code after each timestamp",
             lines_edit(mis, lambda L: [TSRE.sub(lambda m: m.group(0) + "\x1b[0m", l) for l in L])),
            ("G2c", "with each line indented by one space", lines_edit(mis, lambda L: [TSRE.sub(lambda m: m.group(0) + " ", l) for l in L])),
            ("G2d", "reduced to its block bodies, END and SHA256 lines",
             lines_edit(mis, lambda L: [l for l in L if not re.search(r"Z (BATCH|RESULT|EXTRACT|===== BEGIN)", l)])),
            ("G2e", "reduced to one RUNSET line with an ANSI code inside the name",
             only("BATCH\x1b[0m SHARD 1/3 RUNSET %s RUNS 2" % ("0" * 64))),
            ("G2f", "reduced to one RUNSET line with a tab and doubled spaces", only("BATCH\tSHARD  1 /3 RUNSET x RUNS 2")),
            ("G2g", "reduced to one RUNSET line in lower case", only("batch shard 1/3 runset x runs 2")),
        )
        for tag, nm, copy in G:
            if copy is None:
                copy = mis.replace('"logs_content": "', '"logs_content": "\udcff', 1)
                copy = copy.encode("utf-8", "surrogateescape").decode("latin-1")   # one raw 0xff byte
            if tag.startswith("G1"):
                case("[%s] shard 3's job saving shard 1's log %s quarantines the whole collection: no run eligible or usable"
                     % (tag, nm), [S(1), S(2), S(3), copy], "FAILS", "the whole collection is quarantined", usable=0,
                     bytes_=(tag == "G1d"),
                     # G1a also: the rejected file records what it names, its banner's shard and its job's (N4)
                     extra=(lambda cj_: cj_["files"][3]["names_shards"] == [1, 3]) if tag == "G1a" else None)
            else:
                case("[%s] shard 3's job saving shard 1's log %s voids shards 1 and 3, only shard 2's runs eligible, none usable" % (tag, nm),
                     [S(1), S(2), S(3), copy], "FAILS", "every one of them", usable=2)
        doc_long = {"runs": [{"run_id": "38808914622", "bridge_job_id": "116676857951", "shard": 3}]}
        chk("[G2h] a bare 11-digit run id or 12-digit bridge job id anywhere names its shard",
            raw_named(b"x" + b"a38808914622b", doc_long, {}) == {3} and raw_named(b"=116676857951;", doc_long, {}) == {3}
            and raw_named(b"388089146221", doc_long, {}) == set())
        case("[G2i] a job_id of another shard's job written inside an answer's log voids both shards",
             [S(1, extra_trailer=['{"job_id": 77002}']), S(2), S(3)], "FAILS", "job 77001 answers for shards [1, 2]", usable=2)
        # The governing invariant: a run is usable only when the whole collection succeeds
        import gzip
        gz = gzip.compress(b"opaque bytes with no shard identifier").decode("latin-1")
        d_, _ = case("[I1] an unreadable (compressed) served file with no recoverable shard identifier quarantines the whole "
                     "collection: no run eligible or usable", [S(1), S(2), S(3), gz], "FAILS",
                     "the whole collection is quarantined", usable=0, bytes_=True)
        cjq = json.load(open(os.path.join(d_, "out", "collected.json")))
        chk("[I1] the quarantined file is recorded by name and digest",
            cjq["quarantine"] == [{"kind": "unattributable", "file": "served-3.json",
                                   "sha256": hashlib.sha256(gz.encode("latin-1")).hexdigest(),
                                   "size": len(gz.encode("latin-1")), "reason": "not UTF-8", "names_shards": []}])
        d_, _ = case("[I4] an answer of a job outside the run that names no shard quarantines the whole collection",
                     [json.dumps({"job_id": 99999, "logs_content": "x", "original_length": 1}), S(1), S(2), S(3)], "FAILS",
                     "is no job of the run and the file names no shard", usable=0)

        def outcome_of(texts, bytes_last=False):
            """(exit code, collected.json, the ci/ listing), all read back from disk; the code is replaced by a
            marker that no test accepts when a harness rule fails."""
            R = coll([("served-%d.json" % i, t_.encode("latin-1") if bytes_last and i == len(texts) - 1 else t_)
                      for i, t_ in enumerate(texts)])
            ci = os.path.join(R["out"], "ci")
            return (R["code"] if R["hok"] else ("harness", R["hp"])), R["cj"], sorted(os.listdir(ci)) if os.path.isdir(ci) else []
        c2, cj2, w2 = outcome_of([S(1), S(2), S(3), mis[: len(mis) // 2]])
        c2x, cj2x, w2x = outcome_of([S(1), S(2), S(3), lines_edit(mis, lambda L: [TSRE.sub(r"\1Z ", l) for l in L])])
        chk("[I2] a COLLECT FAILS outcome marks zero runs usable and writes no result file, read back from disk: a "
            "truncated mislabelled copy (quarantined) and a reformatted one (two runs still eligible)",
            c2 == 1 and cj2["verdict"] == "FAILS" and not any(e["usable"] for e in cj2["runs"]) and w2 == []
            and c2x == 1 and cj2x["verdict"] == "FAILS" and not any(e["usable"] for e in cj2x["runs"]) and w2x == []
            and sum(e["eligible"] for e in cj2x["runs"]) == 2)
        c2b, cj2b, w2b = outcome_of([S(1, verdicts={"801": "UNVERIFIED"}), S(2), S(3)])
        chk("[I2b] an UNVERIFIED outcome (one run UNVERIFIED) marks zero runs usable and writes no result file, though "
            "five runs are eligible", c2b == 2 and cj2b["verdict"] == "UNVERIFIED" and not any(e["usable"] for e in cj2b["runs"])
            and sum(e["eligible"] for e in cj2b["runs"]) == 5 and w2b == [])
        c5, cj5, w5 = outcome_of([S(1), S(3)])
        chk("[I5] one shard's answer missing quarantines the whole collection, recorded by its expected name: zero runs "
            "eligible or usable, read back from disk",
            c5 == 1 and cj5["verdict"] == "FAILS" and w5 == [] and not any(e["usable"] or e["eligible"] for e in cj5["runs"])
            and cj5["quarantine"] == [{"kind": "missing", "shard": 2, "job_id": 77002,
                                        "expected": "the job-log answer of job 77002 (Extract shard 2)"}])
        tam = S(1, tamper=["801"])
        c6, cj6, w6 = outcome_of([tam, S(2), S(3)])
        chk("[I6] a file that fails validation is recorded by name and digest, read back from disk",
            c6 == 1 and w6 == [] and [(f_["file"], f_["sha256"], f_["shard"]) for f_ in cj6["failed_files"]]
            == [("served-0.json", hashlib.sha256(tam.encode()).hexdigest(), 1)] and cj6["failed_files"][0]["problems"])
        c3, cj3, w3 = outcome_of([S(1), S(2), S(3)])
        chk("[I3] positive control: a clean collection marks all six runs usable and writes all six result files",
            c3 == 0 and cj3["verdict"] == "HOLDS" and all(e["usable"] and e["eligible"] for e in cj3["runs"])
            and w3 == ["800", "801", "802", "803", "804", "805"])
        # N1: a genuine log's own lines name no other shard; a crafted line would (fail closed, by design)
        runner = ["Current runner version: '2.337.0'", "Complete job name: Extract shard 1", "env:", "  SHARD: 1",
                  "  GH_TOKEN: ***", "##[group]Run python3 -I batchx/host.py --runs batchx/runs.json --shard \"$SHARD\" --out x",
                  "##[group]Run python3 -I batchx/assemble.py \\", "##[endgroup]", "##[error]Process completed with exit code 2.",
                  "Post job cleanup.", "[command]/usr/bin/git version", "Cleaning up orphan processes",
                  "##[warning]Node.js 20 is deprecated.", "Terminate orphan process: pid (2899) (python3)"]
        chk("[N1a] the runner's own line shapes name no shard",
            raw_named(json.dumps({"job_id": 0, "logs_content": "\n".join(runner)}).encode(), doc,
                      {j: k for k, j in index.items()}) == set())
        case("[N1b] a crafted 'EXTRACT SHARD 2/3' runner line in genuine shard 1's log voids shards 1 and 2 (fail closed)",
             [S(1, extra_trailer=["EXTRACT SHARD 2/3 x"]), S(2), S(3)], "FAILS", "job 77001 answers for shards [1, 2]",
             usable=2)
        # N2: a RESULT line for a run outside runs.json
        case("[N2] a RESULT line for a run outside runs.json is refused",
             [S(1, extra_lines=["RESULT 999 UNVERIFIED - (1 checks, 0 failed, 1 unverified)"], verdict="UNVERIFIED"),
              S(2), S(3)], "FAILS", "RESULT lines for", usable=4)
        # N3: a job outside the run with a damaged banner
        case("[N3] a job outside the run saving shard 1's log with its RUNSET line deleted voids shard 1",
             [S(1), S(2), S(3), drop_runset(S(1, job_id=99999))], "FAILS", "is no job of the extraction run", usable=4)
        # F2: the assembler's own CHECK all line inside its output voids the shard
        case("[F2] a 'CHECK all UNVERIFIED stopped' line inside the assembler's output voids the shard",
             [S(1, verdicts={"801": "UNVERIFIED"}, stopped=True), S(2), S(3)], "FAILS", "reported a CHECK all line",
             usable=4)
        case("[R1b] the mirror, shard 1's job serving shard 3's content, voids the same two shards",
             [S(1), S(2), S(3), S(3, job_id=77001)], "FAILS", "job 77001 answers for shards [1, 3]: every one of them is void",
             usable=2)
        # R2: a duplicate cannot escape by its banner: copies are grouped by the trusted job id
        t = json.loads(S(1, trailer=40))
        lines = t["logs_content"].split("\n")
        bannerless = json.dumps({"job_id": 77001, "logs_content": "\n".join(lines[6:]), "original_length": t["original_length"]})
        contra = json.dumps({"job_id": 77001, "logs_content": "\n".join(l.replace("HOLDS", "FAILS") for l in lines[6:]),
                             "original_length": t["original_length"]})
        malformed = S(1, trailer=40, malformed_banner=True)
        for tag, nm, extra in (("R2a", "a bannerless duplicate", bannerless),
                               ("R2b", "a contradicting bannerless duplicate", contra),
                               ("R2c", "a malformed-banner duplicate", malformed)):
            _, ta = case("[%s] a whole shard 1, then %s of the same job: shard 1 UNVERIFIED, none of its runs usable"
                         % (tag, nm), [S(1, trailer=40), extra, S(2), S(3)], "UNVERIFIED", "shard 1 is void", usable=4)
            _, tb = case("[%s] %s, then the whole shard 1: the same" % (tag, nm), [extra, S(1, trailer=40), S(2), S(3)],
                         "UNVERIFIED", "shard 1 is void", usable=4)
            chk("[%s] the order changes no RUN line" % tag, [l for l in ta.split("\n") if l.startswith("RUN ")]
                == [l for l in tb.split("\n") if l.startswith("RUN ")])
        case("[R2d] a clean shard 1, then a conflicting copy of the same job arriving after it: shard 1 UNVERIFIED",
             [S(1), S(1, verdicts={"801": "FAILS"}), S(2), S(3)], "UNVERIFIED", "answers of job 77001 differ", usable=4)
        case("[R2e] a lone bannerless answer of an indexed job leaves its shard void, never usable",
             [bannerless, S(2), S(3)], "UNVERIFIED", "an answer with no readable banner", usable=4)
        case("[R2f] an identical duplicate stays accepted once", [S(1), S(1), S(2), S(3)], "HOLDS",
             "2 identical copies of job 77001, taken once", usable=6)
        # R3: an unambiguous output boundary
        R3 = (
            ("R3a", "the assembler died before its verdict; a verdict-shaped line appears later in the trailer",
             dict(died=True, verdict_in_trailer=True), "0 end-of-output markers, not one"),
            ("R3b", "a missing end-of-output marker (truncated output)", dict(no_end=True), "0 end-of-output markers, not one"),
            ("R3c", "two start markers", dict(dup_start=True), "2 start markers (assembler banners), not one"),
            ("R3d", "two end-of-output markers", dict(dup_end=True), "2 end-of-output markers, not one"),
            ("R3e", "the end-of-output marker before the start marker", dict(end_first=True),
             "the end-of-output marker comes before the start marker"),
            ("R3f", "two verdict lines inside the output", dict(two_inside=True), "2 verdict lines, not one"),
            ("R3g", "a verdict-like line before the start, with a real verdict inside", dict(verdict_before_start=True),
             "2 verdict lines, not one"),
            ("R3h", "a verdict-like line before the start, with no verdict inside",
             dict(verdict_before_start=True, no_verdict=True),
             "the verdict line is not the assembler's last line before its end-of-output marker"),
            ("R3i", "a verdict-like line after the end, with a real verdict inside", dict(verdict_after_end=True),
             "2 verdict lines, not one"),
            ("R3j", "a verdict-like line after the end, with no verdict inside", dict(verdict_after_end=True, no_verdict=True),
             "the verdict line is not the assembler's last line before its end-of-output marker"),
            ("R3k", "an end-of-output marker naming another assembler blob",
             dict(end_line="BATCH END shard 1/3: assembler " + "0" * 12), "names another shard or assembler"),
            ("R3l", "an end-of-output marker of another shard (it names shard 2, so the job rule voids 1 and 2)",
             dict(end_line="BATCH END shard 2/3: assembler %s" % ASSEMBLER_BLOB[:12]), "job 77001 answers for shards [1, 2]"),
        )
        for tag, nm, mut, needle in R3:
            case("[%s] %s is refused" % (tag, nm), [S(1, **mut), S(2), S(3)], "FAILS", needle,
                 usable=2 if tag == "R3l" else 4)
        # R1, R2: the result is the same under every numbering of the shards and every order of the files
        import itertools

        def outcome(perm, order, scenario):
            """order is a permutation of the scenario's answers: answer order[i] is written as served-<i>.json, so
            both the order and the name each answer is paired with vary."""
            pd = {"shards": 3, "runs": [dict(r, shard=perm[r["shard"] - 1]) for r in runs]}
            pix = {perm[k - 1]: 77000 + perm[k - 1] for k in (1, 2, 3)}
            PS = lambda k, verdicts=None, **mut: _shard_text(pd, perm[k - 1], verdicts, dict(mut, **(  # noqa: E731
                {"job_id": pix[perm[mut.pop("job_of") - 1]]} if "job_of" in mut else {})))
            texts = scenario(PS)
            idx = [i for i in order if i < len(texts)] + [i for i in range(len(texts)) if i not in order]
            R = coll([("served-%d.json" % pos, texts[i]) for pos, i in enumerate(idx)], ix=pix, dc=pd)
            code, cjp = R["code"], R["cj"] or {"runs": []}
            n_use = sum(1 for e in cjp["runs"] if e["usable"])
            n_el = sum(1 for e in cjp["runs"] if e["eligible"])
            return code, frozenset((e["run_id"], e["eligible"], e["usable"], e["verdict"]) for e in cjp["runs"]), \
                n_el, n_use == (n_el if code == 0 else 0) and bool(R["hok"])

        def bl(PS):
            t_ = json.loads(PS(1, trailer=40))
            ls = t_["logs_content"].split("\n")
            return json.dumps({"job_id": t_["job_id"], "logs_content": "\n".join(ls[6:]), "original_length": t_["original_length"]})
        # each scenario: (name, answers, the exit code and the number of usable runs it must give everywhere)
        scenarios = [
            ("clean", lambda PS: [PS(1), PS(2), PS(3)], 0, 6),
            ("shard 3's job with shard 1's content", lambda PS: [PS(1), PS(1, job_of=3), PS(2), PS(3)], 1, 2),
            ("shard 1's job with shard 3's content", lambda PS: [PS(1), PS(2), PS(3), PS(3, job_of=1)], 1, 2),
            ("shard 2's job with shard 1's content, shard 1 also whole", lambda PS: [PS(1), PS(1, job_of=2), PS(2), PS(3)],
             1, 2),
            ("a bannerless copy of shard 1's job", lambda PS: [PS(1, trailer=40), bl(PS), PS(2), PS(3)], 2, 4),
            ("contradicting copies of shard 2", lambda PS: [PS(1), PS(2), PS(2, verdicts={"802": "FAILS"}), PS(3)], 2, 4),
            ("an identical duplicate of shard 3", lambda PS: [PS(1), PS(2), PS(3), PS(3)], 0, 6),
            ("a malformed-banner duplicate of shard 2", lambda PS: [PS(1), PS(2), PS(2, malformed_banner=True), PS(3)], 2, 4),
            ("a conflicting copy of shard 1 after a clean one",
             lambda PS: [PS(1), PS(2), PS(3), PS(1, verdicts={"801": "FAILS"})], 2, 4),
            ("shard 2 missing", lambda PS: [PS(1), PS(3)], 1, 0),
        ]
        for nm, sc, want_code, want_usable in scenarios:
            res_ = {(perm, order): outcome(perm, order, sc)
                    for perm in itertools.permutations((1, 2, 3)) for order in ((0, 1, 2, 3), (3, 2, 1, 0), (2, 0, 3, 1), (1, 3, 0, 2))}
            outs = set(res_.values())
            chk("[RP] permutation: %s gives exit %d and %d eligible runs, none usable unless it holds, under all 6 shard "
                "numberings and 4 orders and name pairings of the answers" % (nm, want_code, want_usable),
                len(outs) == 1 and all(o[0] == want_code and o[2] == want_usable and o[3] for o in outs))
        for key, val in (("assembler_blob", "0" * 40), ("host_reader_blob", "0" * 40), ("extractor_blob", "0" * 40),
                         ("extractor_commit", "0" * 40), ("runs_sha256", "0" * 64)):
            case("a block naming another %s is refused" % key, [S(1, edit_source={"800": {key: val}}), S(2), S(3)], "FAILS",
                 "names another extractor, assembler, host reader or runs.json", usable=4)
        case("a banner naming another host-reader blob is refused", [S(1, host_prefix="0" * 12), S(2), S(3)], "FAILS",
             "assembler banner is absent or names other blobs", usable=4)
        # N9: under 5,000 lines
        case("a whole answer of 4,999 lines is accepted", [S(1, pad_to=4999), S(2), S(3)], "HOLDS", usable=6)
        case("a whole answer of 5,000 lines is refused: not under 5,000", [S(1, pad_to=5000), S(2), S(3)], "FAILS",
             "has 5000 lines: not under 5000", usable=4)
        # the job index
        n += 1
        jobsd = {"total_count": 4, "jobs": [{"id": 70, "name": "Self-tests and controls"}] + [
            {"id": 70 + k, "name": JOB_NAME % k} for k in (1, 2, 3)]}
        for j in jobsd["jobs"]:
            j.update(run_id=5, head_sha="a" * 40, head_branch=BRANCH, workflow_name=WORKFLOW_NAME)
        ix, rid, pr = build_job_index(jobsd, "a" * 40, 3)
        ix2, _, pr2 = build_job_index(jobsd, "b" * 40, 3)
        jd3 = json.loads(json.dumps(jobsd))
        jd3["jobs"][2]["name"] = JOB_NAME % 1
        _, _, pr3 = build_job_index(jd3, "a" * 40, 3)
        ok = ix == {1: 71, 2: 72, 3: 73} and rid == 5 and not pr and pr2 and pr3
        print("  %s  the job index maps each shard to its one job, and refuses another head or a doubled name"
              % ("ok  " if ok else "FAIL"))
        fails += not ok
        # ------------------------------------------------ TRUST-BOUNDARY.md 6: the trust-boundary tests, read from disk
        U = lambda cp: "\\" + "u%04x" % cp  # noqa: E731 - a JSON escape, built so that this source holds none
        S1, S2, S3 = S(1), S(2), S(3)
        CLEAN = [("served-0.json", S1), ("served-1.json", S2), ("served-2.json", S3)]
        s1o, bad1 = json.loads(S1), json.loads(S(1, {"800": "FAILS"}))
        body1 = S1[1:]   # '"job_id": 77001, "logs_content": ...'

        def ansx(job, text, orig, **more):
            o = {"job_id": job, "logs_content": text, "original_length": orig}
            o.update(more)
            return json.dumps(o)

        def rej(R, which, prefix):
            """R is published quarantined (exit 1, FAILS; zero usable runs and no ci/ by the harness rules), and the
            file at argument `which` is rejected for a reason starting with prefix, and quarantined by name."""
            cj_ = R["cj"]
            if not (R["hok"] and cj_ and R["code"] == 1 and cj_["verdict"] == "FAILS" and cj_["quarantined"] is True):
                return False
            fe = cj_["files"][which]
            return (fe["status"] == "rejected" and (fe["reason"] or "").startswith(prefix)
                    and any(q_.get("kind") == "unattributable" and q_.get("file") == fe["name"] for q_ in cj_["quarantine"]))

        def as_only(payload, k=1):
            items = list(CLEAN)
            items[k - 1] = ("served-%d.json" % (k - 1), payload)
            return coll(items)

        def extra_file(payload):
            return coll(CLEAN + [("served-3.json", payload)])

        # strict grammar (I-PARSE)
        dup5 = '{"job_id": 77001, "logs_content": %s, "original_length": %d, "logs_content": %s, "original_length": %d}' % (
            json.dumps(bad1["logs_content"]), bad1["original_length"], json.dumps(s1o["logs_content"]), s1o["original_length"])
        dup5r = '{"job_id": 77001, "logs_content": %s, "original_length": %d, "logs_content": %s, "original_length": %d}' % (
            json.dumps(s1o["logs_content"]), s1o["original_length"], json.dumps(bad1["logs_content"]), bad1["original_length"])
        ok = True
        for x in (dup5, dup5r):
            R = as_only(x)
            ok = ok and rej(R, 0, "duplicate key 'logs_content', 'original_length'") \
                and R["cj"]["files"][0]["reason"] == "duplicate key 'logs_content', 'original_length'" \
                and R["cj"]["expected"][0]["status"] == "missing" and R["cj"]["expected"][0]["candidates"] == [0]
        chk("[TB-D5] two logs_content keys in shard 1's only file are refused in either order, shard 1 missing with the file "
            "as its candidate", ok)
        D1 = '{"job_id": 99999, ' + body1
        D2 = '{"job_id": 77003, ' + body1
        D3 = '{"logs_content": %s, ' % json.dumps(json.loads(S3)["logs_content"]) + body1
        chk("[TB-D1] a duplicated job_id (a foreign id or another shard's first) or an earlier logs_content holding shard "
            "3's log is refused (D1, D2, D3)", rej(as_only(D1), 0, "duplicate key 'job_id'")
            and rej(as_only(D2), 0, "duplicate key 'job_id'") and rej(as_only(D3), 0, "duplicate key 'logs_content'"))
        D1b = '{"job_id": 99999, "logs_content": %s, "original_length": %d, "job_id": 77001}' % (
            json.dumps(s1o["logs_content"]), s1o["original_length"])
        chk("[TB-D1b] a foreign job's answer with a trailing job_id 77001 is refused, as shard 1's only file and beside "
            "genuine shard 1 (D1b, D1c)", rej(as_only(D1b), 0, "duplicate key 'job_id'")
            and rej(extra_file(D1b), 3, "duplicate key 'job_id'"))
        D4 = '{"logs_content": %s, ' % json.dumps("x\n" * 10) + body1
        chk("[TB-D4] an earlier logs_content naming no shard is refused", rej(as_only(D4), 0, "duplicate key 'logs_content'"))
        msgs = [bad1["logs_content"], "BATCH SHARD 3/3 RUNSET x RUNS 2", SUCCESS_MESSAGE[:-1] + "X", SUCCESS_MESSAGE.lower(),
                SUCCESS_MESSAGE + " ", 5, None]
        ok = all(rej(as_only(ansx(77001, s1o["logs_content"], s1o["original_length"], message=m_)), 0,
                     "message is not the tool's success message") for m_ in msgs)
        ok = ok and rej(extra_file(ansx(77001, s1o["logs_content"], s1o["original_length"], message="m")), 3,
                        "message is not the tool's success message")
        chk("[TB-X3] a message other than the tool's success message is refused: a contradicting log (X3), a RUNSET line "
            "(X1), 'm' beside genuine S1 (C4), one character, case, a trailing space, a non-string", ok)
        chk("[TB-DEEP2a] a duplicate key inside a nested value is refused as a duplicate, before any type check",
            rej(extra_file('{"job_id": 77001, "logs_content": {"a": 1, "a": 2}, "original_length": 1}'), 3,
                "duplicate key 'a'"))
        RUNS_REAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs.json")
        HEADM = "a" * 40

        def jobs_list(nsh, drop=()):
            jobs = [{"id": 70, "name": "Self-tests and controls"}] + [
                {"id": 100 + k, "name": JOB_NAME % k} for k in range(1, nsh + 1) if k not in drop]
            for j in jobs:
                j.update(run_id=5, head_sha=HEADM, head_branch=BRANCH, workflow_name=WORKFLOW_NAME)
            return {"total_count": len(jobs), "jobs": jobs}

        def via_main(items, jobs_bytes, runs_path=None, head=HEADM):
            """One collection through main(), in-process, with stdout and stderr captured, read back from disk."""
            d = tempfile.mkdtemp(dir=base)
            paths, written = write_items(d, items)
            jp, out = os.path.join(d, "jobs.json"), os.path.join(d, "out")
            with open(jp, "wb") as f_:
                f_.write(jobs_bytes)
            argv = ["--runs", runs_path or RUNS_REAL, "--run-jobs", jp, "--head", head, "--out", out] + [
                x for p in paths for x in ("--served", p)]
            buf, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
                code = main(argv, durable=False)
            t = buf.getvalue()
            hok, cj, hp = harness(d, out, written, t, err.getvalue()) if code not in (3, 4) else (None, None, [])
            return {"code": code, "t": t, "err": err.getvalue(), "cj": cj, "hok": hok, "hp": hp, "d": d, "out": out}

        def input_entry(R, which):
            return [q_ for q_ in (R["cj"] or {}).get("quarantine", []) if q_.get("kind") == "input" and q_.get("input") == which]

        def published_quarantined(R):
            return bool(R["hok"]) and R["code"] == 1 and R["cj"]["verdict"] == "FAILS" and R["cj"]["quarantined"] is True

        jl = json.dumps(jobs_list(32))
        jl2 = jl.replace('"id": 101,', '"id": 101, "id": 9999,', 1)
        R = via_main([("served-0.json", S1)], jl2.encode())
        e_ = input_entry(R, "jobs list")
        chk("[TB-DEEP2b] a jobs list with a duplicated id inside a job object is refused, through main and read from disk",
            jl2 != jl and published_quarantined(R) and len(e_) == 1
            and e_[0]["sha256"] == hashlib.sha256(jl2.encode()).hexdigest() and e_[0]["reason"].startswith("duplicate key 'id'"))

        def reblock(js, rid, f):
            """js with run rid's block body replaced by f(its lines), and the SHA256 line made to match."""
            o = json.loads(js)
            L_ = o["logs_content"].split("\n")
            i = next(i for i, l in enumerate(L_) if l.endswith("===== BEGIN EXPECTED RESULT ci/%s/results.json =====" % rid))
            j = next(j for j, l in enumerate(L_) if l.endswith("===== END EXPECTED RESULT ci/%s/results.json =====" % rid))
            body = f([strip(l) for l in L_[i + 1:j]])
            sha = hashlib.sha256(("\n".join(body) + "\n").encode()).hexdigest()
            L_ = L_[:i + 1] + ["2026-12-01T10:00:00.0000000Z " + x for x in body] + [
                L_[j], "2026-12-01T10:00:00.0000000Z SHA256 ci/%s/results.json %s" % (rid, sha)] + L_[j + 2:]
            return json.dumps({"job_id": o["job_id"], "logs_content": "\n".join(L_), "original_length": len(L_)})
        R = as_only(reblock(S1, "800", lambda B: [x for b in B for x in ([b, b] if b.strip().startswith('"id": "800"') else [b])]))
        chk("[TB-DEEP2c] a result block with a duplicated key inside run and a matching SHA256 line fails validation "
            "(defence in depth)", bool(R["hok"]) and R["code"] == 1 and [f_["shard"] for f_ in R["cj"]["failed_files"]] == [1])
        R = as_only(json.dumps({"job_id": 77001, "logs_content": s1o["logs_content"] + "\n",
                                "original_length": s1o["original_length"]}))
        chk("[TB-NL] a whole answer ending in a newline is refused as not whole", bool(R["hok"]) and R["code"] == 1
            and any("not whole" in p_ for f_ in R["cj"]["failed_files"] for p_ in f_["problems"]))
        keyx = [ansx(77001, s1o["logs_content"], s1o["original_length"], result={"a": 1}),
                json.dumps({"job_id": 77001, "logs_content": s1o["logs_content"], "original_length": s1o["original_length"],
                            "Message": SUCCESS_MESSAGE}),
                json.dumps({"result": s1o}),
                json.dumps({"failed_jobs": 1, "logs": [], "message": "Retrieved logs for 12 failed jobs",
                            "return_format": "x", "run_id": 5, "total_jobs": 2})]
        chk("[TB-KEY] unknown keys are refused: an extra key (X2), Message, a tool envelope (G1c), the failed-jobs answer",
            all(rej(extra_file(x), 3, "key set") for x in keyx))
        T = lambda j, l='"x"', o="1": '{"job_id": %s, "logs_content": %s, "original_length": %s}' % (j, l, o)  # noqa: E731
        types_ = [(T("77001.0"), "non-integer number"), (T("7e4"), "non-integer number"), (T("true"), "job_id has the wrong type"),
                  (T('"77001"'), "job_id has the wrong type"), (T("0"), "job_id has the wrong type"),
                  (T("-77001"), "integer out of range"), (T("1" * 17), "integer out of range"),
                  (T("null"), "job_id has the wrong type"),
                  (T("77001", o="1.5"), "non-integer number"), (T("77001", o="-1"), "integer out of range"),
                  (T("77001", o="null"), "original_length has the wrong type"),
                  (T("77001", l='["x"]'), "logs_content has the wrong type"), (T("77001", l="null"), "logs_content has the wrong type")]
        # (a 5,000-digit job_id is [TB-SCAN]'s: the byte scan raises on it before the grammar sees it)
        chk("[TB-TYPE] wrong types and ranges are refused (T1-T3, null values)", all(rej(extra_file(x), 3, w) for x, w in types_))
        ok = all(rej(extra_file(T("77001", o=c_)), 3, "non-standard constant") for c_ in ("NaN", "Infinity", "-Infinity"))
        for val in (float("nan"), float("inf")):
            R = as_only(S(1, edit_result={"800": {"x": val}}))
            ok = ok and bool(R["hok"]) and R["code"] == 1 and [f_["shard"] for f_ in R["cj"]["failed_files"]] == [1]
        chk("[TB-NAN] NaN, Infinity and -Infinity are refused in a served file and in a result block (B1)", ok)
        chk("[TB-BOM] a byte-order mark before the object is refused (E7)",
            rej(as_only(b"\xef\xbb\xbf" + S1.encode()), 0, "byte-order mark before the object"))
        g1d = mis.encode().replace(b'"logs_content": "', b'"logs_content": "\xff', 1)
        utf = [(g1d, "not UTF-8"), (mis.encode("utf-16"), "not UTF-8"), (mis.encode("utf-16-le"), "not JSON"),
               (mis.encode("utf-16-be"), "does not begin with '{'"), (mis.encode("utf-32"), "not UTF-8"),
               (('{"job_id": 77001, "logs_content": "' + U(0xd800) + '", "original_length": 1}').encode(),
                "lone surrogate in logs_content")]
        chk("[TB-UTF8] bytes that are not strict UTF-8 JSON text (G1d, E1, E2) and a lone surrogate escape are refused",
            all(rej(extra_file(x), 3, w) for x, w in utf) and rej(as_only(S2.encode("utf-16"), 2), 1, "not UTF-8"))
        trail = [(S1 + "\n" + mis, "data after the object"), (S1 + "x", "data after the object"),
                 (S1 + "\n", "data after the object"), (" " + S1, "does not begin with '{'")]
        chk("[TB-TRAIL] exactly one object and nothing before or after it: E8, a trailing payload, a trailing newline, a "
            "leading space", all(rej(extra_file(x), 3, w) for x, w in trail))
        empt = [b"", b"  \n\t ", b"null", ("[" + ",".join((S1, S2, S3)) + "]").encode()]
        chk("[TB-EMPTY] an empty file, whitespace, null and an array are refused with their digests (E3, E9-E11)",
            all(rej(extra_file(x), 3, "does not begin with '{'") for x in empt))
        R = extra_file('{"job_id":' + "[" * 100000 + "]" * 100000 + "}")
        chk("[TB-NEST] 100,000-deep nesting is refused with a reason and no traceback", rej(R, 3, "nested too deeply") and not R["err"])
        R = extra_file(("sparse", MAX_SERVED_BYTES + 1))
        h_ = hashlib.sha256()
        with open(R["paths"][3], "rb") as f_:
            for b_ in iter(lambda: f_.read(1 << 20), b""):
                h_.update(b_)
        fe = R["cj"]["files"][3] if R["cj"] else {}
        chk("[TB-CAP] a regular file one byte over the cap is refused and never parsed, its streamed digest recorded",
            rej(R, 3, "over the size cap") and fe["size"] == MAX_SERVED_BYTES + 1 and fe["sha256"] == h_.hexdigest())
        os.remove(R["paths"][3])
        plain = S(3, extra_trailer=[" BATCH SHARD 1/3 RUNSET x RUNS 2"])
        escd = plain.replace(" BATCH SHARD 1/3", " " + U(0x42) + "ATCH SHARD 1/3")
        ok = escd != plain and json.loads(escd)["logs_content"] == json.loads(plain)["logs_content"]
        for x in (plain, escd):
            R = as_only(x, 3)
            ok = ok and bool(R["hok"]) and R["code"] == 1 and [v_["shard"] for v_ in R["cj"]["voided_shards"]] == [1, 3]
        chk("[TB-ESC] a trailer line naming shard 1 in genuine S3 voids shards 1 and 3, spelled plainly or with a JSON "
            "escape (E-esc)", ok)
        # paths and copies (I-PARSE, I-PUB)
        R = extra_file(("dir",))
        fe = R["cj"]["files"][3] if R["cj"] else {}
        chk("[TB-DIR] a served directory is refused by kind with no digest, and the collection published quarantined (E12)",
            rej(R, 3, "not a regular file (directory)") and fe["kind"] == "directory" and fe["sha256"] is None and fe["size"] is None)
        ok = True
        for item in (("served-3.json", ("missing",)), ("served-0.json/x", ("rawpath",)), ("a" * 300, ("rawpath",))):
            R = coll(CLEAN + [item])   # ENOENT; ENOTDIR (a path through a regular file); ENAMETOOLONG
            cj_ = R["cj"] or {}
            ok = ok and rej(R, 3, "not a regular file (missing)") and cj_["files"][3]["kind"] == "missing" \
                and not any(q_["kind"] == "missing" for q_ in cj_["quarantine"]) and all(x["status"] == "present" for x in cj_["expected"])
        chk("[TB-MISS] a missing, mistyped (ENOTDIR) or mangled (ENAMETOOLONG) served path is refused as missing, never a "
            "host failure, told apart from a missing expected answer (E13)", ok)
        R = as_only(("symlink_to", S1.encode()))
        fe = R["cj"]["files"][0] if R["cj"] else {}
        chk("[TB-LINK] a symbolic link to genuine S1, as shard 1's only file, is refused, its target's digest recorded",
            rej(R, 0, "not a regular file (symlink)") and fe["kind"] == "symlink" and fe["size"] == len(S1.encode())
            and fe["sha256"] == hashlib.sha256(S1.encode()).hexdigest() and R["cj"]["expected"][0]["status"] == "missing")
        R = extra_file(("fifo",))
        chk("[TB-FIFO] a FIFO is refused without blocking", rej(R, 3, "not a regular file (other)")
            and R["cj"]["files"][3]["kind"] == "other")
        R = coll(CLEAN + [("served-0.json", ("same", 0)), ("served-hl.json", ("hardlink", 0))])
        fs_ = (R["cj"] or {}).get("files", [])
        chk("[TB-SAME] the same path twice and a hard link hold with 6 usable runs, both recorded as the same file (C2)",
            bool(R["hok"]) and R["code"] == 0 and sum(e["usable"] for e in R["cj"]["runs"]) == 6 and len(fs_) == 5
            and fs_[3]["same_file_as"] == 0 and fs_[4]["same_file_as"] == 0 and all(x["status"] == "accepted" for x in fs_))
        R = coll(CLEAN + [("sub/served-0.json", json.dumps(s1o, indent=2))])
        chk("[TB-NAME] two different files with one basename in two directories quarantine the collection",
            bool(R["hok"]) and R["code"] == 1 and R["cj"]["quarantined"] is True
            and [x["reason"] for x in R["cj"]["files"] if x["name"] == "served-0.json"] == ["another served file has the same name"] * 2)
        c4s = ansx(77001, s1o["logs_content"], s1o["original_length"], message=SUCCESS_MESSAGE)
        ind = json.dumps(s1o, indent=2)
        three = (("served-0.json", S1), ("served-0b.json", ind), ("served-0c.json", c4s))
        R = coll(list(three) + [("served-1.json", S2), ("served-2.json", S3)])
        dg = sorted(hashlib.sha256(x.encode()).hexdigest() for _, x in three)
        cj_ = R["cj"] or {}
        chk("[TB-N3] byte-distinct copies with one identity (C3, C4s) hold, and every copy's name and digest is recorded",
            bool(R["hok"]) and R["code"] == 0 and len(set(dg)) == 3
            and [(c_["name"], c_["sha256"]) for c_ in cj_["expected"][0]["copies"]]
            == [(n_, hashlib.sha256(x.encode()).hexdigest()) for n_, x in three]
            and cj_["shards"]["1"]["sha256s"] == dg and sorted(f_["sha256"] for f_ in cj_["files"][:3]) == dg)
        # early failures and traceability (I-QUAR, N2)
        fake_runs = os.path.join(tempfile.mkdtemp(dir=base), "runs.json")
        with open(fake_runs, "wb") as f_:
            f_.write(b'{"shards": 1, "runs": []}\n')
        R = via_main([("served-0.json", S1), ("served-1.json", S2)], jl.encode(), runs_path=fake_runs)
        e_ = input_entry(R, "runs.json")
        chk("[TB-RUNS] a runs.json other than the pinned file is published quarantined (exit 1), its digest recorded with "
            "pinned false, every served file recorded", published_quarantined(R) and len(e_) == 1 and e_[0]["pinned"] is False
            and e_[0]["sha256"] == hashlib.sha256(b'{"shards": 1, "runs": []}\n').hexdigest() and R["cj"]["runs"] == []
            and R["cj"]["expected"] is None and len(R["cj"]["files"]) == 2
            and R["cj"]["collection"]["inputs"]["runs_json"]["pinned"] is False)
        ok = True
        for jb in (json.dumps(jobs_list(32, drop=(32,))).encode(), b"not json", b'{"jobs": "\xff"}',
                   b"\xef\xbb\xbf" + jl.encode()):
            R = via_main([("served-0.json", S1)], jb)
            e_ = input_entry(R, "jobs list")
            ok = ok and published_quarantined(R) and len(e_) == 1 and e_[0]["sha256"] == hashlib.sha256(jb).hexdigest() \
                and len(R["cj"]["expected"]) == 32 and all(x["status"] == "undetermined" for x in R["cj"]["expected"])
        chk("[TB-JOBS] a jobs list omitting shard 32, not JSON, not UTF-8 or with a BOM is published quarantined (exit 1), "
            "recorded by digest, every expected answer undetermined", ok)
        jl3 = jobs_list(32)
        jl3["jobs"][2]["id"] = jl3["jobs"][1]["id"]   # Extract shard 2 gets Extract shard 1's job id
        R = via_main([("served-0.json", S1)], json.dumps(jl3).encode())
        e_ = input_entry(R, "jobs list")
        chk("[TB-JOBID] one job id under two shard names is refused, through main and read from disk",
            published_quarantined(R) and len(e_) == 1 and "not distinct" in e_[0]["reason"])
        R = coll(CLEAN)
        chk("[TB-SYNTH] a direct collect() call records inputs.runs_json, inputs.jobs_list and runs_sha256 as null, never "
            "the pin", bool(R["hok"]) and R["code"] == 0 and R["cj"]["collection"]["inputs"]["runs_json"] is None
            and R["cj"]["collection"]["inputs"]["jobs_list"] is None and R["cj"]["runs_sha256"] is None)
        R = via_main([("served-0.json", S1)], jl.encode(), head="c" * 12)
        chk("[TB-HEAD] a --head that is not 40 hex digits is published quarantined", published_quarantined(R)
            and "not a full 40-hex sha" in (input_entry(R, "jobs list") or [{"reason": ""}])[0]["reason"])
        ok = True
        for args in (["--runs", RUNS_REAL, "--run-jobs", "j", "--head", HEADM, "--served", "s"],
                     ["--runs", RUNS_REAL, "--run-jobs", "j", "--head", HEADM, "--out", "OUT"], ["-h"], ["--help"]):
            d_ = tempfile.mkdtemp(dir=base)
            args = [os.path.join(d_, "out") if a_ == "OUT" else a_ for a_ in args]
            buf, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
                code_ = main(args, durable=False)
            L_ = buf.getvalue().rstrip("\n").split("\n")
            ok = ok and code_ == 3 and os.listdir(d_) == [] and not err.getvalue() and L_[-1].startswith("COLLECT REFUSED ") \
                and not any(l.startswith("COLLECT PUBLISHED") for l in L_)
        chk("[TB-ARGS] a missing --out, no --served, -h and --help are refused (exit 3), nothing created", ok)

        def kcase(expected_):
            R_ = as_only(S(1, edit_result={"800": {"expected": expected_}}))
            return bool(R_["hok"]) and R_["code"] == 1 and [(f_["shard"], f_["sha256"]) for f_ in R_["cj"]["failed_files"]] \
                == [(1, R_["cj"]["files"][0]["sha256"])]
        chk("[TB-K1] a canonical block whose expected is null is a validation failure, recorded with its digest", kcase(None))
        chk("[TB-K2] a canonical block whose expected is a string is a validation failure, recorded with its digest", kcase("x"))
        chk("[TB-K3] a canonical block whose expected.outcome is absent or not a string is a validation failure",
            kcase({}) and kcase({"outcome": 5}))
        real_read_shard = read_shard

        def boom(*a_, **k_):
            raise RuntimeError("test")
        globals()["read_shard"] = boom
        try:
            R = coll(CLEAN)
        finally:
            globals()["read_shard"] = real_read_shard
        chk("[TB-INT] an exception no check foresaw is an internal quarantine, published (exit 1)", bool(R["hok"])
            and R["code"] == 1 and any(q_["kind"] == "internal" for q_ in R["cj"]["quarantine"]))
        Ra = coll([("served-0.json", S1), ("served-2.json", S3)])
        Rb = coll([("served-0.json", S1), ("served-1.json", S2[: len(S2) // 2]), ("served-2.json", S3)])
        chk("[TB-CAND] a shard not served and a shard whose only file is rejected are both missing; only the second names a "
            "candidate", bool(Ra["hok"]) and bool(Rb["hok"]) and Ra["cj"]["expected"][1]["status"] == "missing"
            and Ra["cj"]["expected"][1]["candidates"] == [] and Rb["cj"]["expected"][1]["status"] == "missing"
            and Rb["cj"]["expected"][1]["candidates"] == [1])
        # stale output and publication (I-PUB, N1)

        def snapshot(path):
            """What is at path: a link's target, a file's bytes and mtime, or every file and directory under it."""
            if os.path.islink(path):
                return ("link", os.readlink(path))
            if os.path.isfile(path):
                with open(path, "rb") as f_:
                    return ("file", f_.read(), os.stat(path).st_mtime_ns)
            fl_ = []
            for r_, ds, fs2 in os.walk(path):
                fl_ += [("dir", os.path.relpath(os.path.join(r_, x), path)) for x in ds]
                for x in fs2:
                    p_ = os.path.join(r_, x)
                    with open(p_, "rb") as f_:
                        fl_.append((os.path.relpath(p_, path), f_.read(), os.stat(p_).st_mtime_ns))
            return sorted(fl_, key=repr)

        def refused(make):
            snap = {}

            def pre(out):
                make(out)
                snap["before"] = snapshot(out)
            R_ = coll([("served-0.json", S1), ("served-2.json", S3)], pre=pre)
            L_ = R_["t"].rstrip("\n").split("\n")
            return (R_["code"] == 3 and snapshot(R_["out"]) == snap["before"] and not R_["err"]
                    and L_[-1].startswith("COLLECT REFUSED ") and not any(".staging-" in x for x in os.listdir(R_["d"])))

        def stale_ci(out):
            os.makedirs(os.path.join(out, "ci", "800"))
            with open(os.path.join(out, "ci", "800", "results.json"), "w") as f_:
                f_.write("{}\n")

        def stale_cj(out):
            os.makedirs(out)
            with open(os.path.join(out, "collected.json"), "w") as f_:
                json.dump({"verdict": "HOLDS", "quarantined": False, "quarantine": [],
                           "runs": [{"run_id": r["run_id"], "usable": True, "eligible": True} for r in runs]}, f_)

        def a_file(out):
            with open(out, "w") as f_:
                f_.write("x\n")
        chk("[TB-O1] a collection into an existing --out holding a stale ci/800/results.json is refused (exit 3), the "
            "stale file untouched", refused(stale_ci))
        chk("[TB-O2] a collection into an existing --out holding a stale HOLDS collected.json is refused (exit 3), "
            "untouched", refused(stale_cj))
        chk("[TB-O3] an --out that is an empty directory, a file, a symbolic link or a dangling link is refused (exit 3), "
            "untouched", refused(os.makedirs) and refused(a_file)
            and refused(lambda out: os.symlink(os.path.dirname(out), out))
            and refused(lambda out: os.symlink(os.path.join(os.path.dirname(out), "nowhere"), out)))

        def patch(obj, name, fn):
            orig = getattr(obj, name)
            setattr(obj, name, fn)
            return lambda: setattr(obj, name, orig)

        def raising(exc):
            def f(*a_, **k_):
                raise exc
            return f
        R = coll(CLEAN, setup=lambda d: patch(os, "rename", raising(OSError(errno.EXDEV, "test"))))
        L_ = R["t"].rstrip("\n").split("\n")
        chk("[TB-O5] a failed rename after a complete staging is ABORTED (exit 4), --out absent, no COLLECT PUBLISHED line",
            R["code"] == 4 and not os.path.lexists(R["out"]) and not R["err"] and L_[-1].startswith("COLLECT ABORTED ")
            and not any(l.startswith("COLLECT PUBLISHED") for l in L_))

        def fault_open(exc, nth):
            """A setup that makes the nth result-file open in a staging directory raise exc."""
            real, cnt = open, [0]

            def fake(p, *a_, **k_):
                if str(p).endswith("results.json") and ".staging-" in str(p):
                    cnt[0] += 1
                    if cnt[0] == nth:
                        raise exc
                return real(p, *a_, **k_)

            def setup(d):
                globals()["open"] = fake
                return lambda: globals().pop("open", None)
            return setup
        R = coll(CLEAN, setup=fault_open(OSError(errno.ENOSPC, "test"), 3))
        fl = [json.loads(l[len("COLLECT FILE "):]) for l in R["t"].split("\n") if l.startswith("COLLECT FILE ")]
        want_fl = [{"arg": i, "name": "served-%d.json" % i, "kind": "regular", "size": len(b_),
                    "sha256": hashlib.sha256(b_).hexdigest(), "status": "accepted", "reason": None}
                   for i, b_ in sorted(R["written"].items())]
        chk("[TB-O6] a failed result write is ABORTED (exit 4), --out absent, and the COLLECT FILE lines trace every served "
            "file", R["code"] == 4 and not os.path.lexists(R["out"]) and fl == want_fl and not R["err"]
            and R["t"].rstrip("\n").split("\n")[-1].startswith("COLLECT ABORTED "))
        ok = True
        for exc in (UnicodeEncodeError("ascii", "x", 0, 1, "test"), KeyboardInterrupt()):
            R = coll(CLEAN, setup=fault_open(exc, 3))
            ok = ok and R["code"] == 4 and not os.path.lexists(R["out"]) and not R["err"]
        chk("[TB-O6x] a non-OSError or an interrupt during the result write is ABORTED (exit 4), never uncaught", ok)

        def fsync_hook(on_parent=None, seen=None):
            def setup(d):
                pst, real = os.stat(d), os.fsync

                def fake(fd):
                    s_ = os.fstat(fd)
                    if seen is not None:
                        seen.append((s_.st_dev, s_.st_ino))
                    if on_parent is not None and (s_.st_dev, s_.st_ino) == (pst.st_dev, pst.st_ino):
                        raise on_parent
                    return real(fd)
                return patch(os, "fsync", fake)
            return setup
        R = coll(CLEAN, durable=True, setup=fsync_hook(on_parent=OSError(errno.EIO, "test")))
        L_ = R["t"].rstrip("\n").split("\n")
        pub = [l for l in L_ if l.startswith("COLLECT PUBLISHED ")]
        cjp_ = os.path.join(R["out"], "collected.json")
        cjb = open(cjp_, "rb").read() if os.path.exists(cjp_) else b""
        chk("[TB-NDUR] a failed parent fsync after the rename is exit 5: --out present and complete, the PUBLISHED line's "
            "nonce and digest those of the file on disk, then COLLECT NOT DURABLE", R["code"] == 5 and bool(R["hok"])
            and len(pub) == 1 and pub[0].endswith(" nonce %s collected.json sha256 %s" % (
                R["cj"]["collection"]["nonce"], hashlib.sha256(cjb).hexdigest()))
            and L_[-3] == pub[0] and L_[-2].startswith("COLLECT NOT DURABLE ") and L_[-1] == "COLLECT HOLDS")
        ok = True
        for nm in ("a\nCOLLECT HOLDS\nb", "a\nCOLLECT PUBLISHED x nonce y\nb"):
            R = coll(CLEAN + [(nm, "not json")])
            cj_ = R["cj"] or {"runs": [{"usable": True}], "files": [{}] * 4, "collection": {}}
            L_ = R["t"].rstrip("\n").split("\n")
            pub = [l for l in L_ if l.startswith("COLLECT PUBLISHED")]
            cjb = open(os.path.join(R["out"], "collected.json"), "rb").read() if R["cj"] else b""
            e_, runl = esc(nm), [l for l in L_ if l.startswith("RUN ")]
            ok = (ok and R["code"] == 1 and bool(R["hok"]) and cj_["verdict"] == "FAILS" and cj_["quarantined"] is True
                  and not any(e["usable"] for e in cj_["runs"]) and not os.path.exists(os.path.join(R["out"], "ci"))
                  and cj_["files"][3]["status"] == "rejected" and cj_["files"][3]["name"] == nm
                  and "COLLECT HOLDS" not in L_[:-1] and L_[-1] == "COLLECT FAILS"
                  and len(pub) == 1 and pub[0].endswith(" nonce %s collected.json sha256 %s" % (
                      cj_["collection"]["nonce"], hashlib.sha256(cjb).hexdigest()))
                  and all(all(" " <= c <= "~" for c in l) for l in L_)
                  and len(runl) == 6 and all(e_ in l for l in runl)
                  and any(l.startswith("COLLECT FAIL " + e_) for l in L_)
                  and any(l.startswith("COLLECT FILE ") and e_ in l for l in L_) and not R["err"])
        chk("[TB-INJ] a rejected file whose name embeds newlines and COLLECT lines injects no line: quarantined on disk, "
            "one PUBLISHED line matching the file, the name JSON-escaped in every line, the RUN lines included", ok)
        R = coll([("served-0.json", S1), ("served-2.json", S3)])
        chk("[TB-O7] a quarantined collection publishes exactly collected.json", bool(R["hok"]) and R["code"] == 1
            and sorted(os.listdir(R["out"])) == ["collected.json"])
        d_ = tempfile.mkdtemp(dir=base)
        paths, written = write_items(d_, CLEAN)
        outs = []
        for o_ in ("out1", "out2"):
            buf, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stderr(err):
                code_ = collect(doc, paths, os.path.join(d_, o_), index, 42, buf, head=HEAD, durable=False)
            outs.append((code_,) + harness(d_, os.path.join(d_, o_), written, buf.getvalue(), err.getvalue())[:2])
        chk("[TB-O8] two collections of the same inputs into two fresh locations have distinct nonces and record the "
            "on-disk digests", all(c_ == 0 and h_ for c_, h_, _ in outs)
            and outs[0][2]["collection"]["nonce"] != outs[1][2]["collection"]["nonce"]
            and [f_["sha256"] for f_ in outs[0][2]["files"]] == [f_["sha256"] for f_ in outs[1][2]["files"]]
            == [hashlib.sha256(written[i]).hexdigest() for i in range(3)])
        seen = []
        R = coll(CLEAN, durable=True, setup=fsync_hook(seen=seen))
        man = (R["cj"] or {}).get("collection", {}).get("manifest", [])
        ino = lambda p: (os.stat(p).st_dev, os.stat(p).st_ino)  # noqa: E731
        want_sync = [ino(os.path.join(R["out"], "collected.json"))] + [ino(os.path.join(R["out"], m["path"])) for m in man] \
            + [ino(R["out"]), ino(R["d"])] if R["cj"] else [None]
        chk("[TB-SYNC] with durable=True each published file, the staging directory and the parent are synced",
            R["code"] == 0 and bool(R["hok"]) and len(man) == 6 and set(want_sync) <= set(seen))
        # [TB-SCAN]: a scan's conversion error rejects only its file; [TB-SCANX]: a host failure is never a rejection

        def stdout_ok(R_):
            """The [TB-INJ] stdout checks: no COLLECT HOLDS before the last line, the last COLLECT FAILS, exactly one
            PUBLISHED line whose nonce and digest are those of collected.json on disk, printable ASCII, no stderr."""
            L2 = R_["t"].rstrip("\n").split("\n")
            pub_ = [l for l in L2 if l.startswith("COLLECT PUBLISHED")]
            cjp2 = os.path.join(R_["out"], "collected.json")
            if not (R_["cj"] and os.path.exists(cjp2)):
                return False
            with open(cjp2, "rb") as f_:
                dig = hashlib.sha256(f_.read()).hexdigest()
            return ("COLLECT HOLDS" not in L2[:-1] and L2[-1] == "COLLECT FAILS" and len(pub_) == 1
                    and pub_[0].endswith(" nonce %s collected.json sha256 %s" % (R_["cj"]["collection"]["nonce"], dig))
                    and all(all(" " <= c <= "~" for c in l) for l in L2) and not R_["err"])
        D5k = "9" * 5000
        scan_cases = [
            ("a", '{"job_id": %s, "logs_content": "x", "original_length": 1}' % D5k, "byte scan failed (ValueError)"),
            ("b", json.dumps({"job_id": 77001, "logs_content": "BATCH SHARD %s/3 x" % D5k, "original_length": 1}),
             "byte scan failed (ValueError)"),
            ("c", '{"job_id": 77001, "logs_content": "\\"job_id\\": ' + U(0x31) * 5000 + '", "original_length": 1}',
             "decoded scan failed (ValueError)"),
            ("d", json.dumps({"job_id": 77001, "logs_content": "EXTRACT SHARD " + "1" * 5000, "original_length": 1}),
             "parsed scan failed (ValueError)")]
        ok = True
        for tag, x, why in scan_cases:
            R = extra_file(x)
            cj_ = R["cj"] or {"files": [{}] * 4, "quarantine": [{"kind": "internal"}]}
            ok = ok and rej(R, 3, why) and cj_["files"][3]["reason"] == why and cj_["files"][3]["names_shards"] is None \
                and len(cj_["files"]) == 4 and not any(q_["kind"] == "internal" for q_ in cj_["quarantine"]) and stdout_ok(R)
        chk("[TB-SCAN] a scan's conversion error (a 5,000-digit job_id, shard number, escaped job_id digits, or EXTRACT "
            "SHARD number) rejects only that file, with all 4 files recorded and the collection published quarantined", ok)

        def scan_fault(exc):
            """A setup in which raw_named raises exc when it scans the marked file."""
            def setup(d):
                real = globals()["raw_named"]

                def fake(data, *a_, **k_):
                    if b"scanx-marker" in data:
                        raise exc
                    return real(data, *a_, **k_)
                globals()["raw_named"] = fake
                return lambda: globals().__setitem__("raw_named", real)
            return setup

        def read_fault(exc):
            """A setup in which the read (os.read) of served-3.json raises exc."""
            def setup(d):
                pst, real = os.stat(os.path.join(d, "served-3.json")), os.read

                def fake(fd, n_):
                    s_ = os.fstat(fd)
                    if (s_.st_dev, s_.st_ino) == (pst.st_dev, pst.st_ino):
                        raise exc
                    return real(fd, n_)
                return patch(os, "read", fake)
            return setup
        ok = True
        for setup_ in (scan_fault(MemoryError()), scan_fault(OSError(errno.ENOSPC, "test")),
                       scan_fault(OSError(errno.EIO, "test")), read_fault(OSError(errno.EIO, "test")),
                       read_fault(MemoryError()), scan_fault(KeyboardInterrupt())):
            R = coll(CLEAN + [("served-3.json", ansx(77001, "scanx-marker", 1))], setup=setup_)
            L_ = R["t"].rstrip("\n").split("\n")
            fl = [json.loads(l[len("COLLECT FILE "):]) for l in L_ if l.startswith("COLLECT FILE ")]
            ok = ok and R["code"] == 4 and not os.path.lexists(R["out"]) and not R["err"] \
                and not any(l.startswith("COLLECT PUBLISHED") for l in L_) and L_[-1].startswith("COLLECT ABORTED ") \
                and [f_["arg"] for f_ in fl] == [0, 1, 2] \
                and not any(w_ in l for l in L_ for w_ in ("scan failed", "unreadable"))
        chk("[TB-SCANX] a host failure at intake (MemoryError, ENOSPC or EIO in the byte scan, EIO or MemoryError in the "
            "read, an interrupt) is ABORTED (exit 4), nothing published, never a file's rejection", ok)
        # positive controls (non-vacuity)
        R = coll([("served-%d.json" % (k - 1), ansx(77000 + k, json.loads(S(k))["logs_content"],
                                                   json.loads(S(k))["original_length"], message=SUCCESS_MESSAGE))
                  for k in (1, 2, 3)])
        chk("[TB-P0m] every answer with the success message holds with 6 usable runs", bool(R["hok"]) and R["code"] == 0
            and sum(e["usable"] for e in R["cj"]["runs"]) == 6)
        LAYOUT = re.compile(rb'\A\{"job_id":(0|[1-9][0-9]*),"logs_content":"(?:[^"\\\x00-\x1f]|\\.)*",'
                            rb'"message":"Job logs content retrieved successfully","original_length":(0|[1-9][0-9]*)\}\Z')
        reals = [S(k, tool=True).encode("utf-8") for k in (1, 2, 3)]
        R = coll([("served-%d.json" % i, b_) for i, b_ in enumerate(reals)])
        f800 = os.path.join(R["out"], "ci", "800", "results.json")
        chk("[TB-REAL] the real tool's byte format (compact, sorted keys, the success message, raw UTF-8, HTML escapes, "
            "U+FEFF first) holds with 6 usable runs", all(LAYOUT.match(b_) for b_ in reals)
            and all(b'"logs_content":"' + chr(0xfeff).encode() in b_ and ("\\" + "u003c").encode() in b_
                    and ("\\" + "u0026").encode() in b_ and ("\\" + "u001b").encode() in b_ and chr(0xe9).encode() in b_
                    and b"<" not in b_ for b_ in reals)
            and bool(R["hok"]) and R["code"] == 0 and sum(e["usable"] for e in R["cj"]["runs"]) == 6
            and os.path.exists(f800) and open(f800).read() == json.dumps(_result(runs[0]), indent=1, sort_keys=True) + "\n")
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("collect self-test: %d of %d cases ok" % (n - fails, n))
    return fails


class _ArgError(Exception):
    pass


class _Parser(argparse.ArgumentParser):
    def error(self, message):   # an argument error is REFUSED (exit 3), never argparse's exit 2
        raise _ArgError(message)


def main(argv=None, durable=True):
    """S0, then S1-S12 through run_collection. Returns the exit code (TRUST-BOUNDARY.md 3); never raises in
    collection mode. The self-test passes durable=False."""
    try:
        ap = _Parser(description=__doc__.splitlines()[0], add_help=False)   # -h and --help are refused, never exit 0
        ap.add_argument("--runs")
        ap.add_argument("--run-jobs")
        ap.add_argument("--head")
        ap.add_argument("--served", action="append", default=[])
        ap.add_argument("--out")
        ap.add_argument("--self-test", action="store_true")
        ap.add_argument("--work")
        a = ap.parse_args(argv)
        if not a.self_test and not (a.runs and a.run_jobs and a.head and a.served and a.out):
            raise _ArgError("--runs, --run-jobs, --head, --served and --out are required")
    except BaseException as e:  # noqa: BLE001 - before S2 every failure is REFUSED
        try:
            emit(sys.stdout, "COLLECT REFUSED %s; --out is not a result of this invocation"
                 % (esc(str(e)) if isinstance(e, _ArgError) else _errname(e)))
        except BaseException:  # noqa: BLE001
            pass
        return 3
    if a.self_test:
        return 1 if self_test(a.work) else 0
    return run_collection(lambda: load_inputs(a.runs, a.run_jobs, a.head), a.served, a.out, head=a.head, durable=durable)


if __name__ == "__main__":
    sys.exit(main())
