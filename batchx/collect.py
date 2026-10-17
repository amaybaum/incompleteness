#!/usr/bin/env python3
"""Collect the batch's expected results from the shard job logs as the session's job-log tool served them.

  python3 -I collect.py --runs batchx/runs.json --served FILE [--served FILE ...] --out DIR
  python3 -I collect.py --self-test [--work DIR]

Run in the session, after the launch, never in CI. Each --served FILE is one answer of the job-log tool for one
shard job, saved as the tool returned it: a JSON object with job_id, logs_content and original_length (the tool's
own file, or from_transcript.py's extraction of it). Nothing here downloads anything.

For each file it checks, fail closed:
  - the log was served whole: the served text's line count equals original_length (a tail is refused);
  - the shard's banner line, `BATCH SHARD K/N RUNSET <sha256> RUNS n`, appears once; K is not already collected;
    N and the RUNSET digest equal those of shard K's runs in the pinned runs.json;
  - one RESULT line for each of shard K's runs and for no other run;
  - one block, BEGIN/END/SHA256, for each run whose RESULT line is HOLDS, and none for any other run; the block's
    text (timestamps stripped, lines joined with newlines, ending with one) is canonical ASCII JSON whose sha256
    equals its SHA256 line, and it names that run, its pinned bridge job and head, and kind cited-bridge;
  - the last line is `EXTRACT SHARD K/N <verdict>`, and that verdict is the one the RESULT lines imply.
A shard that fails any check contributes no result. Across files: each shard 1..N is collected once, and the runs
collected are exactly runs.json's, each once.

A run is usable when its RESULT is HOLDS and its shard passed every check; its block is written to
DIR/ci/<run>/results.json and listed in DIR/collected.json with its digest, shard, source job and served-text
sha256. Every other run is listed with its verdict and the reason it is not usable. The last line is
COLLECT HOLDS (exit 0) when every run of runs.json is usable, COLLECT FAILS (exit 1) when a run FAILS or a shard
fails a check, and COLLECT UNVERIFIED (exit 2) otherwise. Python 3 stdlib.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile

sys.dont_write_bytecode = True
RUNS_SHA256 = "5436c5b6325e5efca8b9d9a737ba832b6556ae9ffc15524b33774f701f672edb"
TS = re.compile(r"^\ufeff?\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ")
BANNER = re.compile(r"^BATCH SHARD (\d+)/(\d+) RUNSET ([0-9a-f]{64}) RUNS (\d+)$")
RESULT = re.compile(r"^RESULT (\d+) (HOLDS|FAILS|UNVERIFIED) (\S+) \(")
BEGIN = re.compile(r"^===== BEGIN EXPECTED RESULT ci/(\d+)/results\.json =====$")
END = "===== END EXPECTED RESULT ci/%s/results.json ====="
SHA = re.compile(r"^SHA256 ci/(\d+)/results\.json ([0-9a-f]{64})$")
VERDICT = re.compile(r"^EXTRACT SHARD (\d+)/(\d+) (HOLDS|FAILS|UNVERIFIED)$")


def runset_digest(ids):
    return hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()


def strip(l):
    return TS.sub("", l, count=1)


def read_shard(served, doc):
    """Returns (shard or None, problems, {run: (verdict, block text or None)})."""
    probs = []
    try:
        obj = json.loads(served)
        text, orig = obj["logs_content"], obj["original_length"]
        job = obj.get("job_id")
        if not isinstance(text, str) or not isinstance(orig, int):
            raise ValueError("fields")
    except (ValueError, KeyError, TypeError):
        return None, ["the served file is not a job-log answer"], {}
    raw = text.split("\n")
    if raw and raw[-1] == "":
        raw.pop()
    if len(raw) != orig:
        return None, ["job %s served %d of %d lines: not whole" % (job, len(raw), orig)], {}
    L = [strip(l) for l in raw]
    ban = [BANNER.match(l) for l in L]
    ban = [m for m in ban if m]
    if len(ban) != 1:
        return None, ["job %s: %d banner lines" % (job, len(ban))], {}
    k, nsh, rs, nr = int(ban[0].group(1)), int(ban[0].group(2)), ban[0].group(3), int(ban[0].group(4))
    exp = [r for r in doc["runs"] if r["shard"] == k]
    byid = {r["run_id"]: r for r in exp}
    if nsh != doc["shards"] or rs != runset_digest(byid) or nr != len(exp) or not exp:
        probs.append("shard %d: banner does not match runs.json (N %d, %d runs)" % (k, nsh, nr))
    res, order = {}, []
    for l in L:
        m = RESULT.match(l)
        if m:
            if m.group(1) in res:
                probs.append("shard %d: run %s has two RESULT lines" % (k, m.group(1)))
            res[m.group(1)] = m.group(2)
            order.append(m.group(1))
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
                break
            body = "\n".join(L[i + 1:j]) + "\n"
            sm = SHA.match(L[j + 1]) if j + 1 < len(L) else None
            if rid in blocks:
                probs.append("shard %d: run %s has two blocks" % (k, rid))
            if not sm or sm.group(1) != rid or sm.group(2) != hashlib.sha256(body.encode("utf-8")).hexdigest():
                probs.append("shard %d: run %s's block does not match its SHA256 line" % (k, rid))
            blocks[rid] = body
            i = j + 1
        i += 1
    for rid, body in blocks.items():
        if res.get(rid) != "HOLDS":
            probs.append("shard %d: a block for run %s, whose RESULT is %s" % (k, rid, res.get(rid)))
            continue
        try:
            r = json.loads(body)
            cfg = byid[rid]
            ok = (body.isascii() and body == json.dumps(r, indent=1, sort_keys=True) + "\n"
                  and r.get("kind") == "cited-bridge" and r["run"]["id"] == rid and r["run"]["job_id"] == cfg["bridge_job_id"]
                  and r["commit"] == r["run"]["head_sha"] == cfg["head_sha"])
        except (ValueError, KeyError, TypeError):
            ok = False
        if not ok:
            probs.append("shard %d: run %s's block is not a canonical result of that run" % (k, rid))
    for rid, v in res.items():
        if v == "HOLDS" and rid not in blocks:
            probs.append("shard %d: run %s holds but has no block" % (k, rid))
    last = L[-30:]
    vs = [VERDICT.match(l) for l in last]
    vs = [m for m in vs if m]
    want = "FAILS" if "FAILS" in res.values() else "HOLDS" if res and all(v == "HOLDS" for v in res.values()) \
        and set(res) == set(byid) else "UNVERIFIED"
    if len(vs) != 1 or int(vs[0].group(1)) != k or vs[0].group(3) != want:
        probs.append("shard %d: the verdict line is absent or is not the one its RESULT lines imply (%s)" % (k, want))
    return k, probs, {rid: (v, blocks.get(rid)) for rid, v in res.items()}


def collect(doc, served_files, out, outp=None):
    outp = outp or sys.stdout
    P = lambda s: print(s, file=outp)  # noqa: E731
    shards, bad, runs_seen = {}, False, {}
    for path in served_files:
        with open(path, encoding="utf-8") as f:
            served = f.read()
        k, probs, res = read_shard(served, doc)
        dig = hashlib.sha256(served.encode("utf-8")).hexdigest()
        if k is not None and k in shards:
            probs.append("shard %d collected twice" % k)
        for p in probs:
            P("COLLECT FAIL %s: %s" % (os.path.basename(path), p))
        if probs:
            bad = True
            if k is not None and k not in shards:
                shards[k] = None
            continue
        shards[k] = {"file": os.path.basename(path), "served_sha256": dig, "runs": res}
        for rid in res:
            runs_seen.setdefault(rid, []).append(k)
    table, usable = [], 0
    os.makedirs(out, exist_ok=True)
    for cfg in doc["runs"]:
        rid, k = cfg["run_id"], cfg["shard"]
        sh = shards.get(k)
        entry = {"run_id": rid, "shard": k, "expires": cfg["expires"]}
        if sh is None:
            entry.update(verdict=None, usable=False, reason="shard %d not collected or failed a check" % k)
        elif len(runs_seen.get(rid, [])) != 1:
            entry.update(verdict=None, usable=False, reason="run seen in shards %s" % runs_seen.get(rid))
        else:
            v, body = sh["runs"][rid]
            entry.update(verdict=v, served_sha256=sh["served_sha256"], file=sh["file"])
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
        json.dump({"runs_sha256": RUNS_SHA256, "shards": {str(k): (v and {"file": v["file"], "served_sha256": v["served_sha256"]})
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
            "run": {"id": cfg["run_id"], "job_id": cfg["bridge_job_id"], "head_sha": cfg["head_sha"]}}


def _shard_text(doc, k, verdicts=None, mut=None):
    """A shard log as assemble.py prints it, inside runner lines, timestamped."""
    mut = mut or {}
    exp = [r for r in doc["runs"] if r["shard"] == k]
    verdicts = verdicts or {}
    L = ["Current runner version: '2.337.0'", "##[group]Run python3 -I batchx/assemble.py", "##[endgroup]",
         "BATCH ci-batch-extract shard %d/%d: assembler x" % (k, doc["shards"]),
         "BATCH SHARD %d/%d RUNSET %s RUNS %d" % (k, doc["shards"], mut.get("runset", runset_digest([r["run_id"] for r in exp])), len(exp))]
    rs = exp + mut.get("extra_runs", [])
    for r in rs:
        if r["run_id"] in mut.get("drop_result", []):
            continue
        L.append("RESULT %s %s gate-verdict (15 checks, 0 failed, 0 unverified)" % (r["run_id"], verdicts.get(r["run_id"], "HOLDS")))
    for r in rs:
        v = verdicts.get(r["run_id"], "HOLDS")
        if v != "HOLDS" and r["run_id"] not in mut.get("block_for", []):
            continue
        res = _result(r)
        res.update(mut.get("edit_result", {}).get(r["run_id"], {}))
        body = json.dumps(res, indent=1, sort_keys=True) + "\n"
        sha = hashlib.sha256(body.encode()).hexdigest()
        if r["run_id"] in mut.get("tamper", []):
            body = body.replace('"gate-verdict"', '"build-failed"')
        L.append("===== BEGIN EXPECTED RESULT ci/%s/results.json =====" % r["run_id"])
        L += body.rstrip("\n").split("\n")
        L.append("===== END EXPECTED RESULT ci/%s/results.json =====" % r["run_id"])
        L.append("SHA256 ci/%s/results.json %s" % (r["run_id"], sha))
    vs = [verdicts.get(r["run_id"], "HOLDS") for r in exp]
    v = mut.get("verdict") or ("FAILS" if "FAILS" in vs else "HOLDS" if all(x == "HOLDS" for x in vs) else "UNVERIFIED")
    L.append("EXTRACT SHARD %d/%d %s" % (k, doc["shards"], v))
    L += ["Post job cleanup.", "Cleaning up orphan processes"]
    text = "\n".join("2026-12-01T10:00:%02d.0000000Z %s" % (i % 60, l) for i, l in enumerate(L))
    orig = len(L) + mut.get("orig_delta", 0)
    if mut.get("tail"):
        text = "\n".join(text.split("\n")[mut["tail"]:])
    return json.dumps({"job_id": 77000 + k, "logs_content": text, "original_length": orig})


def self_test(work=None):
    base = tempfile.mkdtemp(prefix="collect-selftest-", dir=work)
    fails, n = 0, 0
    runs = [{"run_id": str(800 + i), "bridge_job_id": str(8800 + i), "head_sha": "%040x" % i, "shard": 1 + i // 2,
             "expires": "2026-12-2%d" % (i // 2)} for i in range(6)]
    doc = {"shards": 3, "runs": runs}
    print("collect self-test (synthetic served shard logs, no network):")
    try:
        def case(name, texts, want, needle=None, usable=None):
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
            import io
            buf = io.StringIO()
            code = collect(doc, files, os.path.join(d, "out"), buf)
            t = buf.getvalue()
            ok = t.rstrip("\n").split("\n")[-1] == "COLLECT " + want and code == {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[want]
            ok = ok and (needle is None or needle in t)
            if usable is not None:
                ok = ok and ("COLLECT %d of 6 runs usable" % usable) in t
                written = sorted(os.listdir(os.path.join(d, "out", "ci"))) if os.path.isdir(os.path.join(d, "out", "ci")) else []
                ok = ok and len(written) == usable
            print("  %s  %s -> COLLECT %s" % ("ok  " if ok else "FAIL", name, t.rstrip("\n").split("\n")[-1].split()[-1]))
            if not ok:
                fails += 1
                print("\n".join("        | " + l for l in t.split("\n") if l.startswith("COLLECT")))
            return d

        S = lambda k, verdicts=None, **mut: _shard_text(doc, k, verdicts, mut)  # noqa: E731
        d = case("three whole shards, every run holding", [S(1), S(2), S(3)], "HOLDS", usable=6)
        n += 1
        got = open(os.path.join(d, "out", "ci", "800", "results.json")).read()
        ok = got == json.dumps(_result(runs[0]), indent=1, sort_keys=True) + "\n"
        print("  %s  the written file is byte-identical to the canonical block" % ("ok  " if ok else "FAIL"))
        fails += not ok
        case("the same shards in another order", [S(3), S(1), S(2)], "HOLDS", usable=6)
        case("a shard served as a tail is refused", [S(1, tail=2), S(2), S(3)], "FAILS", "not whole", usable=4)
        case("a served line count other than original_length is refused", [S(1, orig_delta=1), S(2), S(3)], "FAILS",
             "not whole", usable=4)
        case("a shard missing", [S(1), S(2)], "UNVERIFIED", "shards not collected: [3]", usable=4)
        case("a shard collected twice", [S(1), S(1), S(2), S(3)], "FAILS", "collected twice", usable=6)
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
             "FAILS", "the verdict line", usable=4)
        case("one run UNVERIFIED: the others are usable, the batch is not", [S(1, verdicts={"801": "UNVERIFIED"}), S(2), S(3)],
             "UNVERIFIED", "RUN 801 shard 1 expires 2026-12-20 UNVERIFIED not usable", usable=5)
        case("one run FAILS: the batch FAILS, the others are usable", [S(1, verdicts={"801": "FAILS"}), S(2), S(3)],
             "FAILS", "RUN 801 shard 1 expires 2026-12-20 FAILS not usable", usable=5)
        case("a file that is not a job-log answer", ["not json", S(1), S(2), S(3)], "FAILS", "not a job-log answer",
             usable=6)
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("collect self-test: %d of %d cases ok" % (n - fails, n))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--runs")
    ap.add_argument("--served", action="append", default=[])
    ap.add_argument("--out")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    if a.self_test:
        return 1 if self_test(a.work) else 0
    if not (a.runs and a.served and a.out):
        ap.error("--runs, --served and --out are required")
    with open(a.runs, "rb") as f:
        data = f.read()
    if hashlib.sha256(data).hexdigest() != RUNS_SHA256:
        print("COLLECT FAIL runs.json is not the pinned file")
        print("COLLECT FAILS")
        return 1
    return collect(json.loads(data), a.served, a.out)


if __name__ == "__main__":
    sys.exit(main())
