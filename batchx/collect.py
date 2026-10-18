#!/usr/bin/env python3
"""Collect the batch's expected results from the shard job logs as the session's job-log tool served them.

  python3 -I collect.py --runs batchx/runs.json --run-jobs JOBS.json --head SHA --served FILE [--served FILE ...] \
      --out DIR
  python3 -I collect.py --self-test [--work DIR]

Run in the session, after the launch, never in CI. Nothing here downloads anything.
  --served FILE   one answer of the job-log tool for one shard job, saved as the tool returned it: a JSON object
                  with job_id, logs_content and original_length (the tool's own file, or from_transcript.py's
                  extraction of it).
  --run-jobs      the jobs list of the extraction's workflow run, from the JSON endpoint
                  repos/amaybaum/incompleteness/actions/runs/<run>/jobs?per_page=100, merged over its pages.
  --head          the commit the owner launched.
From --run-jobs it builds the job index: exactly one job named "Extract shard K" for each shard K, every job of
one run, at --head, on the launch branch, of this workflow.

For each served file it checks, fail closed:
  - the answer names a job id, and that id is the index's job for the shard its banner names;
  - the log was served whole, its line count equal to original_length, and is under 5,000 lines;
  - one assembler banner, naming the pinned assembler, host-reader and extractor blobs, the extractor's commit and
    runs.json's digest; one `BATCH SHARD K/N RUNSET <sha256> RUNS n` line whose N and digest are shard K's in the
    pinned runs.json;
  - one RESULT line for each of shard K's runs and for no other run;
  - one block, BEGIN/END/SHA256, for each run whose RESULT line is HOLDS, and none for any other run; the block's
    text (timestamps stripped, lines joined with newlines, ending with one) is canonical ASCII JSON whose sha256
    equals its SHA256 line, naming that run, its pinned bridge job and head, kind cited-bridge, and in `source`
    the pinned extractor blob and commit, assembler blob, host-reader blob and runs.json digest;
  - exactly one `EXTRACT SHARD K/N <verdict>` line in the whole log, after the last RESULT line and the last block,
    and that verdict is the one the RESULT lines imply.
A file that fails any check contributes no result, and the collection FAILS.

Copies. Files are grouped by the shard their banner names before anything is decided, so the order of --served
never matters. Byte-identical copies (the same job id, text and original_length) are taken once. Copies that differ
in anything make that shard UNVERIFIED: none of its runs is usable.

A run is usable when its RESULT is HOLDS and its shard passed every check. Its block is written to
DIR/ci/<run>/results.json and listed in DIR/collected.json with its digest, shard, source job id and served-text
sha256. Every other run is listed with its verdict and the reason it is not usable. The last line is COLLECT HOLDS
(exit 0) when every run of runs.json is usable, COLLECT FAILS (exit 1) when a run FAILS or a file fails a check,
and COLLECT UNVERIFIED (exit 2) otherwise. Python 3 stdlib.
"""
import argparse
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

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
        return {}, None, ["the launched commit %r is not a full 40-hex sha" % (head,)]
    try:
        jobs = jobsd["jobs"]
        if len(jobs) != jobsd["total_count"]:
            probs.append("the jobs list holds %d of %d jobs" % (len(jobs), jobsd["total_count"]))
        runs = {j["run_id"] for j in jobs}
        if len(runs) != 1:
            probs.append("the jobs list spans %d runs" % len(runs))
        for j in jobs:
            if j["head_sha"] != head or j.get("head_branch") != BRANCH or j.get("workflow_name") != WORKFLOW_NAME:
                probs.append("job %s is not of this workflow at %s on %s" % (j.get("id"), head[:12], BRANCH))
        index = {}
        for k in range(1, nshards + 1):
            ids = [j["id"] for j in jobs if j["name"] == JOB_NAME % k]
            if len(ids) != 1 or not isinstance(ids[0], int) or isinstance(ids[0], bool):
                probs.append("%d jobs named %r" % (len(ids), JOB_NAME % k))
            else:
                index[k] = ids[0]
        return index, (sorted(runs)[0] if len(runs) == 1 else None), probs
    except (KeyError, TypeError, AttributeError):
        return {}, None, ["the jobs list is malformed"]


def identity(obj):
    return hashlib.sha256(json.dumps([obj.get("job_id"), obj.get("logs_content"), obj.get("original_length")],
                                     sort_keys=True).encode("utf-8")).hexdigest()


def parse_served(served):
    """The tool's answer, or None."""
    try:
        obj = json.loads(served)
        if not (isinstance(obj, dict) and isinstance(obj.get("logs_content"), str)
                and isinstance(obj.get("original_length"), int) and not isinstance(obj.get("original_length"), bool)
                and isinstance(obj.get("job_id"), int) and not isinstance(obj.get("job_id"), bool)):
            return None
        return obj
    except ValueError:
        return None


def shard_of(obj):
    """The shard the answer's RUNSET banner names, read loosely (for grouping only), or None."""
    for l in obj["logs_content"].split("\n"):
        m = BANNER.match(strip(l))
        if m:
            return int(m.group(1))
    return None


def read_shard(obj, doc, job_index, shard=None):
    """Returns (shard or None, problems, {run: (verdict, block text or None)}). shard is the one the job index gives
    the answer's job id (trusted metadata); the log's own banner must agree with it but never chooses it."""
    probs = []
    text, orig, job = obj["logs_content"], obj["original_length"], obj["job_id"]
    raw = text.split("\n")
    if raw and raw[-1] == "":
        raw.pop()
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
            r = json.loads(body)
            cfg, src = byid[rid], r["source"]
            ok = (body.isascii() and body == json.dumps(r, indent=1, sort_keys=True) + "\n"
                  and r.get("kind") == "cited-bridge" and r["run"]["id"] == rid and r["run"]["job_id"] == cfg["bridge_job_id"]
                  and r["commit"] == r["run"]["head_sha"] == cfg["head_sha"])
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


def collect(doc, served_files, out, job_index, run_id=None, outp=None, head=None):
    outp = outp or sys.stdout
    P = lambda s: print(s, file=outp)  # noqa: E731
    inv = {j: k for k, j in job_index.items()}
    bad, answers = False, []
    # Every file is read before anything is decided; the decisions below depend only on the set of answers.
    for path in sorted(served_files, key=os.path.basename):
        with open(path, encoding="utf-8") as f:
            served = f.read()
        obj = parse_served(served)
        if obj is None:
            P("COLLECT FAIL %s: the served file is not a job-log answer" % os.path.basename(path))
            bad = True
            continue
        answers.append((os.path.basename(path), obj, hashlib.sha256(served.encode("utf-8")).hexdigest(), shard_of(obj)))
    # The job rule. An answer belongs to the shard the job index gives its job id: trusted metadata (the extraction
    # run's jobs list and the tool's job id), never the log's own banner. A banner can only add a shard to the
    # shards a job is involved with, never choose one. A job involved with two or more shards voids every one of
    # them; a job whose answers differ, or one of whose answers has no readable banner, voids its shard; an answer
    # of a job outside the run voids the shard its banner names.
    voided, by_job = {}, {}
    for a in answers:
        by_job.setdefault(a[1]["job_id"], []).append(a)
    for job in sorted(by_job):
        ans = by_job[job]
        named = {a[3] for a in ans if a[3] is not None}
        if job not in inv:
            P("COLLECT FAIL job %s (%s) is no job of the extraction run; shard %s is void"
              % (job, ", ".join(sorted(a[0] for a in ans)), sorted(named)))
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
              % (job, len(ans), ", ".join(sorted(a[0] for a in ans)), inv[job]))
            voided.setdefault(inv[job], set()).add("answers of job %s differ" % job)
        elif any(a[3] is None for a in ans):
            P("COLLECT UNVERIFIED job %s: an answer with no readable banner (%s); shard %d is void"
              % (job, ", ".join(sorted(a[0] for a in ans)), inv[job]))
            voided.setdefault(inv[job], set()).add("an answer of job %s has no readable banner" % job)
    shards, why, runs_seen = {}, {}, {}
    for k in sorted({inv[j] for j in by_job if j in inv} | set(voided)):
        if k in voided:
            shards[k], why[k] = None, "; ".join(sorted(voided[k]))
            continue
        copies = by_job[job_index[k]]
        name, obj, dig, _ = sorted(copies, key=lambda c: c[0])[0]
        if len(copies) > 1:
            P("COLLECT NOTE shard %d: %d identical copies of job %s, taken once" % (k, len(copies), job_index[k]))
        kk, probs, res = read_shard(obj, doc, job_index, k)
        for p in probs:
            P("COLLECT FAIL %s: %s" % (name, p))
        if probs:
            bad = True
            shards[k], why[k] = None, "failed a check"
            continue
        shards[k] = {"file": name, "files": sorted(n for n, _, _, _ in copies), "served_sha256": dig,
                     "job_id": obj["job_id"], "copies": len(copies), "runs": res}
        for rid in res:
            runs_seen.setdefault(rid, []).append(k)
    table, usable = [], 0
    os.makedirs(out, exist_ok=True)
    for cfg in doc["runs"]:
        rid, k = cfg["run_id"], cfg["shard"]
        sh = shards.get(k)
        entry = {"run_id": rid, "shard": k, "expires": cfg["expires"]}
        if sh is None:
            entry.update(verdict=None, usable=False, reason="shard %d %s" % (k, why.get(k, "not collected")))
        elif len(runs_seen.get(rid, [])) != 1:
            entry.update(verdict=None, usable=False, reason="run seen in shards %s" % runs_seen.get(rid))
        else:
            v, body = sh["runs"][rid]
            entry.update(verdict=v, served_sha256=sh["served_sha256"], file=sh["file"], job_id=sh["job_id"])
            if v == "HOLDS":
                d = os.path.join(out, "ci", rid)
                os.makedirs(d, exist_ok=True)
                with open(os.path.join(d, "results.json"), "x", encoding="ascii") as f:
                    f.write(body)
                entry.update(usable=True, sha256=hashlib.sha256(body.encode()).hexdigest(),
                             outcome=json.loads(body)["expected"]["outcome"])
                usable += 1
            else:
                entry.update(usable=False, reason="the run's verdict is %s" % v)
        table.append(entry)
        P("RUN %s shard %d expires %s %s%s" % (rid, k, cfg["expires"], entry.get("verdict"),
                                               (" " + entry.get("outcome", "")) if entry["usable"] else
                                               " not usable: " + entry["reason"]))
    extra = sorted(set(runs_seen) - {r["run_id"] for r in doc["runs"]})
    for rid in extra:
        P("COLLECT FAIL run %s is not in runs.json" % rid)
    missing = sorted(set(range(1, doc["shards"] + 1)) - set(shards))
    if missing:
        P("COLLECT UNVERIFIED shards not collected: %s" % missing)
    with open(os.path.join(out, "collected.json"), "x", encoding="utf-8") as f:
        json.dump({"runs_sha256": RUNS_SHA256, "extraction_run": run_id,
                   # what was launched: the --head commit, which the job index required of every job of the run
                   "launched_commit": head,
                   "launched_commit_check": "every job of extraction_run's jobs list is at launched_commit, on %s, of "
                                            "workflow %r" % (BRANCH, WORKFLOW_NAME),
                   # what collected it: this file as executed and as committed, and the values it pins
                   "collector": dict(collector_identity(), pins={"assembler_blob": ASSEMBLER_BLOB, "host_reader_blob": HOST_BLOB,
                                          "extractor_blob": EXTRACT_RESULT_BLOB, "extractor_commit": MAIN_COMMIT,
                                          "runs_sha256": RUNS_SHA256}),
                   "shards": {str(k): (v and {"file": v["file"], "files": v["files"], "served_sha256": v["served_sha256"],
                                              "job_id": v["job_id"], "copies": v["copies"]})
                              for k, v in sorted(shards.items())}, "runs": table},
                  f, indent=1, sort_keys=True)
        f.write("\n")
    fails = bad or extra or any(e.get("verdict") == "FAILS" for e in table)
    v = "FAILS" if fails else "HOLDS" if usable == len(doc["runs"]) and not missing else "UNVERIFIED"
    P("COLLECT %d of %d runs usable" % (usable, len(doc["runs"])))
    P("COLLECT %s" % v)
    return {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[v]


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
    L += ["Post job cleanup."] + (["EXTRACT SHARD %d/%d %s" % (k, doc["shards"], v)] if mut.get("verdict_in_trailer") else []) \
        + ["[command]/usr/bin/git config --local --unset-all x"] * mut.get("trailer", 2) + ["Cleaning up orphan processes"]
    if mut.get("pad_to"):
        L += ["##[warning]padding"] * (mut["pad_to"] - len(L))
    text = "\n".join("2026-12-01T10:00:%02d.0000000Z %s" % (i % 60, l) for i, l in enumerate(L))
    orig = len(L) + mut.get("orig_delta", 0)
    if mut.get("tail"):
        text = "\n".join(text.split("\n")[mut["tail"]:])
    return json.dumps({"job_id": mut.get("job_id", 77000 + k), "logs_content": text, "original_length": orig})


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
        def case(name, texts, want, needle=None, usable=None, absent=None):
            nonlocal fails, n
            n += 1
            d = os.path.join(base, "c%03d" % n)
            os.makedirs(d)
            files = []
            for i, t in enumerate(texts):
                p = os.path.join(d, "served-%d.json" % i)
                with open(p, "w", encoding="utf-8") as f:
                    f.write(t)
                files.append(p)
            buf = io.StringIO()
            code = collect(doc, files, os.path.join(d, "out"), index, 42, buf, head=HEAD)
            t = buf.getvalue()
            ok = t.rstrip("\n").split("\n")[-1] == "COLLECT " + want and code == {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[want]
            ok = ok and (needle is None or needle in t) and (absent is None or absent not in t)
            if usable is not None:
                ok = ok and ("COLLECT %d of 6 runs usable" % usable) in t
                written = sorted(os.listdir(os.path.join(d, "out", "ci"))) if os.path.isdir(os.path.join(d, "out", "ci")) else []
                ok = ok and len(written) == usable
            print("  %s  %s -> COLLECT %s" % ("ok  " if ok else "FAIL", name, t.rstrip("\n").split("\n")[-1].split()[-1]))
            if not ok:
                fails += 1
                print("\n".join("        | " + l for l in t.split("\n") if l.startswith("COLLECT")))
            return d, t

        def chk(name, cond):
            nonlocal fails, n
            n += 1
            print("  %s  %s" % ("ok  " if cond else "FAIL", name))
            fails += not cond

        S = lambda k, verdicts=None, **mut: _shard_text(doc, k, verdicts, mut)  # noqa: E731
        d, _ = case("three whole shards, every run holding", [S(1), S(2), S(3)], "HOLDS", usable=6)
        got = open(os.path.join(d, "out", "ci", "800", "results.json")).read()
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
        ident = collector_identity()
        chk("[R4b] collected.json records the collector's identity apart from the launched commit",
            all(k_ in cj["collector"] for k_ in ("commit", "committed_blob", "executed_blob", "executed_sha256",
                                                 "executed_matches_committed_blob", "path", "pins"))
            and cj["collector"]["executed_sha256"] == ident["executed_sha256"]
            and cj["collector"]["executed_blob"] == git_blob_id(open(os.path.abspath(__file__), "rb").read())
            and "launched_commit" not in cj["collector"] and "collector" not in cj["shards"])
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
        case("a shard missing", [S(1), S(2)], "UNVERIFIED", "shards not collected: [3]", usable=4)
        case("a RUNSET digest other than runs.json's", [S(1, runset="0" * 64), S(2), S(3)], "FAILS", "banner does not match",
             usable=4)
        case("a run's RESULT line missing", [S(1, drop_result=["800"]), S(2), S(3)], "FAILS", "RESULT lines for", usable=4)
        case("an extra run in a shard", [S(1, extra_runs=[dict(runs[2])]), S(2), S(3)], "FAILS", "RESULT lines for",
             usable=4)
        case("a tampered block (its SHA256 line no longer matches)", [S(1, tamper=["801"]), S(2), S(3)], "FAILS",
             "does not match its SHA256 line", usable=4)
        case("a block for a run that does not hold", [S(1, verdicts={"800": "UNVERIFIED"}, block_for=["800"]), S(2), S(3)],
             "FAILS", "a block for run 800", usable=4)
        case("a block naming another head", [S(1, edit_result={"800": {"commit": "f" * 40}}), S(2), S(3)], "FAILS",
             "not a canonical result of that run", usable=4)
        case("a verdict line at odds with the RESULT lines", [S(1, verdict="HOLDS", verdicts={"800": "FAILS"}), S(2), S(3)],
             "FAILS", "not the one its RESULT lines imply", usable=4)
        case("one run UNVERIFIED: the others are usable, the batch is not", [S(1, verdicts={"801": "UNVERIFIED"}), S(2), S(3)],
             "UNVERIFIED", "RUN 801 shard 1 expires 2026-12-20 UNVERIFIED not usable", usable=5)
        case("one run FAILS: the batch FAILS, the others are usable", [S(1, verdicts={"801": "FAILS"}), S(2), S(3)],
             "FAILS", "RUN 801 shard 1 expires 2026-12-20 FAILS not usable", usable=5)
        case("a file that is not a job-log answer", ["not json", S(1), S(2), S(3)], "FAILS", "not a job-log answer",
             usable=6)
        # note 1: the verdict line, found wherever it is after the last result
        case("a verdict line followed by 40 runner lines is found", [S(1, trailer=40), S(2, trailer=40), S(3)], "HOLDS",
             usable=6)
        case("a red shard's verdict line with 40 runner lines after it is found and checked",
             [S(1, verdicts={"801": "UNVERIFIED"}, trailer=40), S(2), S(3)], "UNVERIFIED", usable=5, absent="COLLECT FAIL")
        case("no verdict line", [S(1, no_verdict=True), S(2), S(3)], "FAILS", "0 verdict lines, not one", usable=4)
        case("two verdict lines", [S(1, second_verdict=True), S(2), S(3)], "FAILS", "2 verdict lines, not one", usable=4)
        case("a verdict line before the last block", [S(1, verdict_early=True), S(2), S(3)], "FAILS",
             "not the assembler's last line before its end-of-output marker", usable=4)
        # note 2: copies
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
        # note 3: provenance and pins
        case("a log from another job (another push of this branch) is refused and voids the shard it names",
             [S(1, job_id=99999), S(2), S(3)], "FAILS", "job 99999 (served-0.json) is no job of the extraction run", usable=4)
        case("one job serving two shards is refused", [S(1), S(2, job_id=77001), S(3)], "FAILS", "usable", usable=2)
        # R1: a job id under two shards voids every shard involved, whatever the shard numbers
        case("[R1a] shard 3's job serving shard 1's content voids shards 1 and 3", [S(1, job_id=77003), S(2), S(3)], "FAILS",
             "job 77003 answers for shards [1, 3]: every one of them is void", usable=2)
        case("[R1b] the mirror, shard 1's job serving shard 3's content, voids the same two shards",
             [S(1), S(2), S(3, job_id=77001)], "FAILS", "job 77001 answers for shards [1, 3]: every one of them is void",
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
            ("R3l", "an end-of-output marker of another shard",
             dict(end_line="BATCH END shard 2/3: assembler %s" % ASSEMBLER_BLOB[:12]), "names another shard or assembler"),
        )
        for tag, nm, mut, needle in R3:
            case("[%s] %s is refused" % (tag, nm), [S(1, **mut), S(2), S(3)], "FAILS", needle, usable=4)
        # R1, R2: the result is the same under every numbering of the shards and every order of the files
        import itertools

        def outcome(perm, order, scenario):
            pd = {"shards": 3, "runs": [dict(r, shard=perm[r["shard"] - 1]) for r in runs]}
            pix = {perm[k - 1]: 77000 + perm[k - 1] for k in (1, 2, 3)}
            PS = lambda k, **mut: _shard_text(pd, perm[k - 1], None, dict(mut, **(  # noqa: E731
                {"job_id": pix[perm[mut.pop("job_of") - 1]]} if "job_of" in mut else {})))
            texts = scenario(PS)
            d = tempfile.mkdtemp(dir=base)
            files = []
            for label, t in sorted(zip("abcdefgh", texts), key=lambda x: order.index(x[0]) if x[0] in order else 9):
                p = os.path.join(d, "served-%s.json" % label)
                with open(p, "w", encoding="utf-8") as f:
                    f.write(t)
                files.append(p)
            buf = io.StringIO()
            code = collect(pd, files, os.path.join(d, "out"), pix, 42, buf, head=HEAD)
            cjp = json.load(open(os.path.join(d, "out", "collected.json")))
            return code, frozenset((e["run_id"], e["usable"], e["verdict"]) for e in cjp["runs"])

        def bl(PS):
            t_ = json.loads(PS(1, trailer=40))
            ls = t_["logs_content"].split("\n")
            return json.dumps({"job_id": t_["job_id"], "logs_content": "\n".join(ls[6:]), "original_length": t_["original_length"]})
        scenarios = [
            ("clean", lambda PS: [PS(1), PS(2), PS(3)]),
            ("shard 3's job with shard 1's content", lambda PS: [PS(1, job_of=3), PS(2), PS(3)]),
            ("shard 1's job with shard 3's content", lambda PS: [PS(1), PS(2), PS(3, job_of=1)]),
            ("shard 2's job with shard 1's content, shard 1 also whole", lambda PS: [PS(1), PS(1, job_of=2), PS(2), PS(3)]),
            ("a bannerless copy of shard 1's job", lambda PS: [PS(1, trailer=40), bl(PS), PS(2), PS(3)]),
            ("contradicting copies of shard 2", lambda PS: [PS(1), PS(2), PS(2, verdicts={"802": "FAILS"}), PS(3)]),
            ("an identical duplicate of shard 3", lambda PS: [PS(1), PS(2), PS(3), PS(3)]),
            ("a malformed-banner duplicate of shard 2", lambda PS: [PS(1), PS(2), PS(2, malformed_banner=True), PS(3)]),
            ("a conflicting copy of shard 1 after a clean one", lambda PS: [PS(1), PS(2), PS(3), PS(1, verdicts={"801": "FAILS"})]),
            ("shard 2 missing", lambda PS: [PS(1), PS(3)]),
        ]
        for nm, sc in scenarios:
            res_ = {(perm, order): outcome(perm, order, sc)
                    for perm in itertools.permutations((1, 2, 3)) for order in ("abcd", "dcba", "cadb", "bdac")}
            chk("[RP] permutation: %s gives one result under all 6 shard numberings and 4 file orders (%s)"
                % (nm, ["HOLDS", "FAILS", "UNVERIFIED"][next(iter(res_.values()))[0]]), len(set(res_.values())) == 1)
        for key, val in (("assembler_blob", "0" * 40), ("host_reader_blob", "0" * 40), ("extractor_blob", "0" * 40),
                         ("extractor_commit", "0" * 40), ("runs_sha256", "0" * 64)):
            case("a block naming another %s is refused" % key, [S(1, edit_source={"800": {key: val}}), S(2), S(3)], "FAILS",
                 "names another extractor, assembler, host reader or runs.json", usable=4)
        case("a banner naming another host-reader blob is refused", [S(1, host_prefix="0" * 12), S(2), S(3)], "FAILS",
             "assembler banner is absent or names other blobs", usable=4)
        # note 4: under 5,000 lines
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
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("collect self-test: %d of %d cases ok" % (n - fails, n))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--runs")
    ap.add_argument("--run-jobs")
    ap.add_argument("--head")
    ap.add_argument("--served", action="append", default=[])
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    if a.self_test:
        return 1 if self_test(a.work) else 0
    if not (a.runs and a.run_jobs and a.head and a.served and a.out):
        ap.error("--runs, --run-jobs, --head, --served and --out are required")
    with open(a.runs, "rb") as f:
        data = f.read()
    if hashlib.sha256(data).hexdigest() != RUNS_SHA256:
        print("COLLECT FAIL runs.json is not the pinned file")
        print("COLLECT FAILS")
        return 1
    doc = json.loads(data)
    with open(a.run_jobs, encoding="utf-8") as f:
        index, run_id, probs = build_job_index(json.load(f), a.head, doc["shards"])
    if probs:
        for p in probs:
            print("COLLECT FAIL job index: %s" % p)
        print("COLLECT FAILS")
        return 1
    return collect(doc, a.served, a.out, index, run_id, head=a.head)


if __name__ == "__main__":
    sys.exit(main())
