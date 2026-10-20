#!/usr/bin/env python3
"""Load and check extractor/targets.json, the one list of what this extraction reads. Python 3 stdlib.

  python3 -I targets.py              # prints the targets, the file's sha256 and git blob id
  python3 -I targets.py --self-test

The other three scripts load this file by its path (python3 -I puts no script directory on sys.path) and take
every run id, job id and commit from load(). Nothing else names a target: adding E's run is a commit that changes
targets.json alone.

targets.json is a JSON object with exactly these keys:
  schema "ktoken-evidence-targets", version 1, repo "amaybaum/incompleteness", round "KTOKEN-MAXCONE-1",
  targets  a list of 1 to 4 entries, each with exactly:
    label       "F", "E" or another short upper-case name (^[A-Z][A-Z0-9]{0,7}$)
    kind        "bridge": the entry's job is the run's Mathlib bridge job
    run_id      the exact-head run, decimal digits as a string
    commit      the run's head, 40 lower-case hex digits
    bridge_job  the run's Mathlib bridge job, decimal digits as a string
    path        where the result is committed in the record directory, ^evidence/[a-z0-9-]+/results\\.json$
  and optionally
    cells       {"probe_job": decimal digits, "path": ^evidence/[a-z0-9-]+/cells\\.json$}: the run's probe job, whose
                log is read with the bridge log into a second result (check A3's lines, the absence line, the lines
                the round's frozen verdict reads, the probe's output), and over which the frozen verdict is run
    session_observation  {"original_lines": int, "tail_lines": int, "tail_sha256": hex}: what a session's job-log
                tool reported for the job (its line count, and the sha256 of the last tail_lines lines it served,
                joined with newlines, no final newline). Printed as a cross-check only; never decisive.
Every label, run id, commit and path occurs once, and every job id (bridge and probe) once across all targets. Anything else is refused with TargetsError.
"""
import hashlib
import json
import os
import re
import sys

sys.dont_write_bytecode = True  # never leave bytecode beside the sources
REPO = "amaybaum/incompleteness"
ROUND = "KTOKEN-MAXCONE-1"
SCHEMA = "ktoken-evidence-targets"
DEFAULT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "targets.json")
MAX_TARGETS = 4
TOP_KEYS = {"schema", "version", "repo", "round", "targets"}
REQUIRED = {"label", "kind", "run_id", "commit", "bridge_job", "path"}
OPTIONAL = {"session_observation", "cells"}
CELLS_KEYS = {"probe_job", "path"}
CELLS_PATH = re.compile(r"evidence/[a-z0-9][a-z0-9-]{0,40}/cells\.json\Z")
OBS_KEYS = {"original_lines", "tail_lines", "tail_sha256"}
RX = {
    "label": re.compile(r"[A-Z][A-Z0-9]{0,7}\Z"),
    "run_id": re.compile(r"[1-9][0-9]{6,14}\Z"),
    "bridge_job": re.compile(r"[1-9][0-9]{6,14}\Z"),
    "commit": re.compile(r"[0-9a-f]{40}\Z"),
    "path": re.compile(r"evidence/[a-z0-9][a-z0-9-]{0,40}/results\.json\Z"),
}
HEX64 = re.compile(r"[0-9a-f]{64}\Z")


class TargetsError(Exception):
    pass


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def parse(data):
    """Bytes of targets.json -> {"repo", "round", "targets": [entry, ...], "sha256", "blob"}; TargetsError otherwise."""
    try:
        doc = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as e:
        raise TargetsError("targets.json is not UTF-8 JSON: %s" % type(e).__name__)
    if not isinstance(doc, dict) or set(doc) != TOP_KEYS:
        raise TargetsError("targets.json must be an object with exactly the keys %s" % sorted(TOP_KEYS))
    if doc["schema"] != SCHEMA or doc["version"] != 1 or isinstance(doc["version"], bool):
        raise TargetsError("targets.json schema/version is not %s/1" % SCHEMA)
    if doc["repo"] != REPO or doc["round"] != ROUND:
        raise TargetsError("targets.json names repo %r round %r" % (doc["repo"], doc["round"]))
    ts = doc["targets"]
    if not isinstance(ts, list) or not 1 <= len(ts) <= MAX_TARGETS:
        raise TargetsError("targets must be a list of 1 to %d entries" % MAX_TARGETS)
    seen = {k: set() for k in ("label", "run_id", "commit", "path")}
    jobs = set()
    out = []
    for n, t in enumerate(ts):
        if not isinstance(t, dict):
            raise TargetsError("target %d is not an object" % n)
        keys = set(t)
        if not REQUIRED <= keys or keys - REQUIRED - OPTIONAL:
            raise TargetsError("target %d keys %s: required %s, optional %s"
                               % (n, sorted(keys), sorted(REQUIRED), sorted(OPTIONAL)))
        if t["kind"] != "bridge":
            raise TargetsError("target %d kind %r is not 'bridge'" % (n, t["kind"]))
        for k, rx in RX.items():
            if not isinstance(t[k], str) or not rx.match(t[k]):
                raise TargetsError("target %d field %s is malformed" % (n, k))
        for k in seen:
            if t[k] in seen[k]:
                what = "run" if k == "run_id" else k
                raise TargetsError("%s %s is listed more than once" % (what, t[k]))
            seen[k].add(t[k])
        cl = t.get("cells")
        if cl is not None:
            if (not isinstance(cl, dict) or set(cl) != CELLS_KEYS or not isinstance(cl["probe_job"], str)
                    or not RX["bridge_job"].match(cl["probe_job"]) or not isinstance(cl["path"], str)
                    or not CELLS_PATH.match(cl["path"])):
                raise TargetsError("target %d cells is malformed" % n)
            if cl["path"] in seen["path"]:
                raise TargetsError("path %s is listed more than once" % cl["path"])
            seen["path"].add(cl["path"])
        for j in [t["bridge_job"]] + ([cl["probe_job"]] if cl else []):
            if j in jobs:
                raise TargetsError("job %s is listed more than once" % j)
            jobs.add(j)
        obs = t.get("session_observation")
        if obs is not None:
            if (not isinstance(obs, dict) or set(obs) != OBS_KEYS or not _is_int(obs["original_lines"])
                    or not _is_int(obs["tail_lines"]) or obs["original_lines"] < 1 or obs["tail_lines"] < 1
                    or not isinstance(obs["tail_sha256"], str) or not HEX64.match(obs["tail_sha256"])):
                raise TargetsError("target %d session_observation is malformed" % n)
        out.append(dict(t))
    return {"repo": doc["repo"], "round": doc["round"], "targets": out,
            "sha256": hashlib.sha256(data).hexdigest(), "blob": git_blob_id(data)}


def load(path=None):
    path = path or DEFAULT_PATH
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        raise TargetsError("targets.json unreadable: %s" % type(e).__name__)
    return parse(data)


def self_test():
    good = {"schema": SCHEMA, "version": 1, "repo": REPO, "round": ROUND, "targets": [
        {"label": "F", "kind": "bridge", "run_id": "39163559807", "commit": "e" * 40, "bridge_job": "117781736738",
         "path": "evidence/f-run/results.json",
         "session_observation": {"original_lines": 38627, "tail_lines": 5000, "tail_sha256": "8" * 64}}]}
    e_entry = {"label": "E", "kind": "bridge", "run_id": "39999999999", "commit": "a" * 40, "bridge_job": "118000000001",
               "path": "evidence/e-run/results.json"}

    def enc(d):
        return json.dumps(d).encode()

    def variant(fn):
        d = json.loads(json.dumps(good))
        fn(d)
        return enc(d)
    cases = [("the one-target file", enc(good), True),
             ("F and E together", variant(lambda d: d["targets"].append(dict(e_entry))), True),
             ("no targets", variant(lambda d: d.update(targets=[])), False),
             ("five targets", variant(lambda d: d.update(targets=[dict(e_entry, label="E%d" % i, run_id="3999999990%d" % i,
                                                                         bridge_job="11800000000%d" % i, commit="%d" % i * 40,
                                                                         path="evidence/e%d/results.json" % i)
                                                                    for i in range(5)])), False),
             ("a run listed twice", variant(lambda d: d["targets"].append(dict(e_entry, run_id="39163559807"))), False),
             ("a job listed twice", variant(lambda d: d["targets"].append(dict(e_entry, bridge_job="117781736738"))), False),
             ("a label listed twice", variant(lambda d: d["targets"].append(dict(e_entry, label="F"))), False),
             ("a path listed twice", variant(lambda d: d["targets"].append(dict(e_entry, path="evidence/f-run/results.json"))),
              False),
             ("a commit listed twice", variant(lambda d: d["targets"].append(dict(e_entry, commit="e" * 40))), False),
             ("a run id given as a number", variant(lambda d: d["targets"][0].update(run_id=39163559807)), False),
             ("a job id carrying a path", variant(lambda d: d["targets"][0].update(bridge_job="117781736738/../1")), False),
             ("a short commit", variant(lambda d: d["targets"][0].update(commit="e12c1573")), False),
             ("an upper-case commit", variant(lambda d: d["targets"][0].update(commit="E" * 40)), False),
             ("kind probe", variant(lambda d: d["targets"][0].update(kind="probe")), False),
             ("an unknown key", variant(lambda d: d["targets"][0].update(extra=1)), False),
             ("a missing key", variant(lambda d: d["targets"][0].pop("commit")), False),
             ("a path outside evidence/", variant(lambda d: d["targets"][0].update(path="../x/results.json")), False),
             ("another repo", variant(lambda d: d.update(repo="amaybaum/other")), False),
             ("another round", variant(lambda d: d.update(round="X")), False),
             ("version true", variant(lambda d: d.update(version=True)), False),
             ("an extra top-level key", variant(lambda d: d.update(note="x")), False),
             ("E with a cells block", variant(lambda d: d["targets"].append(dict(e_entry, cells={
                 "probe_job": "118000000002", "path": "evidence/e-run/cells.json"}))), True),
             ("a cells probe job equal to a bridge job", variant(lambda d: d["targets"].append(dict(e_entry, cells={
                 "probe_job": "117781736738", "path": "evidence/e-run/cells.json"}))), False),
             ("a cells probe job equal to its own bridge job", variant(lambda d: d["targets"].append(dict(e_entry, cells={
                 "probe_job": "118000000001", "path": "evidence/e-run/cells.json"}))), False),
             ("a cells path equal to a result path", variant(lambda d: d["targets"].append(dict(e_entry, cells={
                 "probe_job": "118000000002", "path": "evidence/f-run/results.json"}))), False),
             ("a cells path not named cells.json", variant(lambda d: d["targets"].append(dict(e_entry, cells={
                 "probe_job": "118000000002", "path": "evidence/e-run/x.json"}))), False),
             ("a cells block with an extra key", variant(lambda d: d["targets"].append(dict(e_entry, cells={
                 "probe_job": "118000000002", "path": "evidence/e-run/cells.json", "x": 1}))), False),
             ("a cells probe job given as a number", variant(lambda d: d["targets"].append(dict(e_entry, cells={
                 "probe_job": 118000000002, "path": "evidence/e-run/cells.json"}))), False),
             ("a malformed observation", variant(lambda d: d["targets"][0]["session_observation"].update(tail_lines=True)),
              False),
             ("not JSON", b"{", False), ("not UTF-8", b"\xff", False), ("a list", b"[]", False)]
    fails = 0
    for name, data, want in cases:
        try:
            parse(data)
            got = True
        except TargetsError:
            got = False
        ok = got == want
        fails += not ok
        print("  %s  %s %s" % ("ok  " if ok else "FAIL", name, "loads" if want else "is refused"))
    try:
        real = load()
        ts = real["targets"]
        ok = (ts[0]["label"] == "F" and ts[0]["run_id"] == "39163559807" and ts[0]["commit"].startswith("e12c1573")
              and [t["label"] for t in ts[1:]] in ([], ["E"]))
    except TargetsError:
        ok = False
    fails += not ok
    print("  %s  the committed targets.json loads, lists F's run 39163559807 first, and at most E besides" % ("ok  " if ok else "FAIL"))
    print("targets self-test: %d of %d cases ok" % (len(cases) + 1 - fails, len(cases) + 1))
    return fails


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if argv == ["--self-test"]:
        return 1 if self_test() else 0
    if argv:
        print(__doc__)
        return 2
    try:
        t = load()
    except TargetsError as e:
        print("targets refused: %s" % e)
        return 3
    print("targets sha256=%s blob=%s" % (t["sha256"], t["blob"]))
    for x in t["targets"]:
        print("target %s kind=%s run=%s commit=%s bridge_job=%s path=%s" % (x["label"], x["kind"], x["run_id"], x["commit"],
                                                                           x["bridge_job"], x["path"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
