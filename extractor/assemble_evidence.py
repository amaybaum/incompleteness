#!/usr/bin/env python3
"""Assemble KTOKEN-MAXCONE-1's two retained expected results (AGENTS §A.42 item 1, form `derived`) from the
four design-run job logs and the host's JSON records, and print them. Read-only; Python 3 stdlib.

  python3 -I assemble_evidence.py --extractor main-src/verification/audits/evidence-retention/extract_result.py \
      --extractor-repo main-src --host HOSTDIR --logs LOGDIR --download-record download-record.json \
      --src run1=SRC1 --src run2=SRC2
  python3 -I assemble_evidence.py --self-test --extractor PATH

Inputs:
  --extractor        extract_result.py, verified against EXTRACT_RESULT_BLOB (its git blob id at MAIN_COMMIT)
                     and, with --extractor-repo, against that checkout's HEAD and tree; the verified bytes are the
                     ones executed (they are read once, hashed, then compiled).
  --host             run-<id>.json and jobs-<id>.json from fetch_records.py.
  --logs, --download-record
                     <job>.log and the record from download_job_logs.py; each log's length, sha256 and line count
                     must equal the record's.
  --src runN=DIR     a checkout of run N's head holding verification/lean-mathlib/OIBridge.lean and
                     OIBridge/KTokenMaxCone.lean; HEAD and each file's blob are checked with git. The governed
                     modules' `#print axioms` lines are read there, as compare_result.py reads them.

For each run it reads, from the logs, with the pinned extract_result.extract on each step's section: the build
line, every `#print axioms` report of the two governed modules, the release-gate block and verdict, and the
failure markers (counted over the Build and Release gate sections, the scope compare_result.py compares); and,
with this file's parsers: the absence line, check A3's cases and final line, the probe's lines, and (run 2) the
controls self-test's lines. From the API records: the run's identity and every job's name and conclusion.

Fail closed. A run's result is printed only if every check below holds for it. Otherwise the run FAILS (the
evidence is present and contradicts or lacks a required item) or is UNVERIFIED (an input is absent or does not
match its record). Each failed check is printed by name. The verdict line is the last line printed:
  EXTRACT HOLDS       both results printed (exit 0)
  EXTRACT FAILS       at least one run FAILS (exit 1)
  EXTRACT UNVERIFIED  no run FAILS, at least one is UNVERIFIED (exit 2)

Each result is printed exactly as it would be committed, canonical json.dumps(obj, indent=1, sort_keys=True)
plus a newline (ASCII only), between the lines
  ===== BEGIN EXPECTED RESULT <path> =====
  ===== END EXPECTED RESULT <path> =====
followed by `SHA256 <path> <hex>`, the sha256 of that text. In a served job log each line carries a timestamp
prefix; strip it (`^\\d{4}-\\d\\d-\\d\\dT\\d\\d:\\d\\d:\\d\\d\\.\\d+Z `) and join the lines between the markers
with newlines, ending with one, to recover the file. Before printing, the text is scanned for credentials,
signed-URL query strings, IP and e-mail addresses; a hit FAILS the run.

Nothing that varies between runs of the same commit goes under `expected`: no timestamps, durations, build-job
counts, cache lines, temporary paths or output order (sets are recorded as sorted lists or as dicts). Source line
numbers, which are provenance of this log, are kept under `observed`.
"""
import argparse
import contextlib
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import types

sys.dont_write_bytecode = True  # never leave bytecode beside the sources

REPO = "amaybaum/incompleteness"
MAIN_COMMIT = "b96662e6be4f537502c772db369ea32a35b213a8"
EXTRACT_RESULT_PATH = "verification/audits/evidence-retention/extract_result.py"
EXTRACT_RESULT_BLOB = "05c41bce610b8d02ccbaca8e69377b771bef4a35"
RECORD_DIR = "verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/"
LEAN_DIR = "verification/lean-mathlib/"
GOVERNED = ("OIBridge.lean", "OIBridge/KTokenMaxCone.lean")   # the governed paths' .lean files, from LEAN_DIR
MODULE = "OIBridge/KTokenMaxCone.lean"
PERMITTED = ["propext", "Classical.choice", "Quot.sound"]
MARKER_KEYS = ("sorryAx", "Lean.ofReduceBool", "declaration uses 'sorry'", "error:")
ABSENCE = re.compile(r"^info: OIBridge/KTokenMaxCone\.lean:(\d+):(\d+): "
                     r"OIBridge\.EqvK2MaxCone\.pairCone_eq_Q3_of_drive_maxCone is not in the environment$")
PRESENT = "OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone is in the environment"

JOB_BRIDGE = "Mathlib bridge"
JOB_PROBE = "Numerical probes / KTOKEN-MAXCONE-1 k = 3 exact layer"
STEP_BUILD, STEP_GATE = "Build", "Release gate"
STEP_A3 = "KTOKEN-MAXCONE-1 check A3 (k = 2 statement identity and dependency walk, with mutations)"
STEP_PROBE, STEP_CONTROLS = "k = 3 exact witnesses and probe mutations", "Native control mutation tests"
HDR_BUILD = "##[group]Run lean --version"
HDR_GATE = "##[group]Run python3 tools/release_gate.py"
HDR_A3 = ("##[group]Run lake env python3 -I -B ../programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/checks/"
          "run_checks.py run")
HDR_PROBE = "##[group]Run python3 -I -B verification/lean/ktoken_maxcone1_probe.py --self-test"
HDR_CONTROLS = ("##[group]Run python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/"
                "controls.py --self-test")

# What the preregistration (wip/ktoken-maxcone-run2-draft at 2dc8b580) states: the checks compare with these.
PROBE_CODES = ("DICT3", "PRODUCT3", "REACH3", "DEMUX3", "ADJOINT3", "QUANTUM3", "ZERO3", "SCALE3", "ADD3",
               "SHIFT3", "SEP3", "ORBIT3", "CUT3", "SLICE3")
PROBE_REJECTION_CODES = ("ADJOINT3", "CUT3", "DICT3", "ORBIT3", "SHIFT3")
PROBE_N = 3196
PROBE_VERDICT = "KTOKEN-K3-EXACT"
A3_CASES, A3_MUTATIONS = 13, 11
PRINTS = 68
FROZEN_MODULE_BLOB = "14bb9fc07bf65e59e3f412ac7270ffb734a30069"

# The release gate's steps, in the order it prints them, read from its source and never from a run's output:
# tools/release_gate.py, blob d40e2acc9783704dcaf5793bb2228e96252dc6e8, which is the blob at both 1ab0fd9d (run 1)
# and 6959ced4 (run 2), checked separately for each head: the 21 entries of `checks = [...]` (lines 103-187) with
# `checks.insert(2, ("baseline-label", lab))` (line 195), and no other change to the list: 22 steps at each head.
GATE_STEPS = ("toolchain", "staleness", "baseline-label", "voice", "voice-scope", "ci-gate-presence",
              "artifact-placement", "manifest-drift", "claims", "duplicate", "mirror", "citation", "architecture",
              "dependency-label", "coverage", "lean-axioms", "lean-manuscript", "legacy-records", "v3-self-test",
              "v3-corpus", "v3-receipts", "evidence-retention")
GATE_STEPS_RUN1 = GATE_STEPS   # tools/release_gate.py at 1ab0fd9d: blob d40e2acc, 22 steps
GATE_STEPS_RUN2 = GATE_STEPS   # tools/release_gate.py at 6959ced4: blob d40e2acc, 22 steps

RUNS = {
    "run1": {"path": "evidence/run1-39043849411.json", "design_run": 1, "run_id": "39043849411",
             "head": "1ab0fd9dd2c6701197f2e0ab18401cafb76a090d", "bridge_job": "117428550018",
             "probe_job": "117428550439", "controls": False, "gate_steps": GATE_STEPS_RUN1},
    "run2": {"path": "evidence/run2.json", "design_run": 2, "run_id": "39056982958",
             "head": "6959ced4c327ebb800cf6d463a049e4066e37288", "bridge_job": "117466847042",
             "probe_job": "117466847062", "controls": True, "gate_steps": GATE_STEPS_RUN2},
}
# Session observations (2026-10-17), for the printed cross-check only; never in a result. original_length is the
# line count the job-log connector reported; the tail digest is sha256 of the text it served (its last 5000 lines,
# joined with newlines, no final newline; the whole log for the two probe jobs).
CONNECTOR = {
    "117428550018": (41715, 5000, "4c567ef7f3411d57f4206b29d096c88b1f419f7f4ab06f7c510dabfbdfa375a1"),
    "117428550439": (173, 173, "c0c472e147cadeaaba54f42d889bd06b29fdbfcd0537090f9f5b5773c2a606b7"),
    "117466847042": (41728, 5000, "a96872536987cad624a4ed7c28f5afdbd970c12c214a54d9870e19042fafb694"),
    "117466847062": (223, 223, "ffaac76ec9fdcef1dbb6479e49f29535ecfa734d0f58d7e381a598572efaed6e"),
}

# check_retention.py's R5 pattern (main at b96662e6), with signed-URL parameters of the log storage hosts added.
SECRET = re.compile(
    r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
    r'|x-access-toke[n]|[?&](sig|signature|sv|se|sp|sr|st|skoid|sktid|skt|ske|sks|skv|token|x-amz-[a-z-]+)='
    r'|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]|private[_-]?key|https?://[^\s"]*\?'
    r'|blob\.core\.windows\.net|actions\.githubusercontent\.com'
    r'|(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.I)

BEGIN = "===== BEGIN EXPECTED RESULT %s ====="
END = "===== END EXPECTED RESULT %s ====="


class Unverified(Exception):
    pass


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def git(repo, *args):
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, env=env, timeout=60)
    return p.stdout.strip() if p.returncode == 0 else None


def load_extractor(path, repo=None):
    """Read once, check the blob id (and, with repo, the checkout's HEAD and tree), then execute those bytes."""
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        raise Unverified("extractor unreadable: %s" % type(e).__name__)
    if git_blob_id(data) != EXTRACT_RESULT_BLOB:
        raise Unverified("extractor blob %s is not the pinned %s" % (git_blob_id(data), EXTRACT_RESULT_BLOB))
    if repo is not None:
        if git(repo, "rev-parse", "HEAD") != MAIN_COMMIT:
            raise Unverified("extractor checkout HEAD is not %s" % MAIN_COMMIT)
        if git(repo, "rev-parse", "HEAD:" + EXTRACT_RESULT_PATH) != EXTRACT_RESULT_BLOB:
            raise Unverified("extractor checkout tree does not hold the pinned blob")
    mod = types.ModuleType("extract_result")
    mod.__file__ = path
    exec(compile(data, path, "exec"), mod.__dict__)  # noqa: S102 - the pinned, verified bytes
    for name in ("extract", "strip", "MARKERS", "TS"):
        if not hasattr(mod, name):
            raise Unverified("extractor lacks %s" % name)
    if tuple(mod.MARKERS) != MARKER_KEYS:
        raise Unverified("extractor markers are not the expected four")
    return mod


def own_blob(name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), "rb") as f:
        return git_blob_id(f.read())


def spans(nums):
    out = []
    for n in sorted(nums):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


# ------------------------------------------------------------------------------------------------ reading

class Log:
    """One job log: its bytes checked against the download record, decoded, split as extract_result splits."""

    def __init__(self, path, rec, ex):
        try:
            with open(path, "rb") as f:
                data = f.read()
        except OSError as e:
            raise Unverified("log %s unreadable: %s" % (os.path.basename(path), type(e).__name__))
        if rec is None or rec.get("outcome") != "ok":
            raise Unverified("log %s has no successful download record" % os.path.basename(path))
        nl = data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
        self.sha256 = hashlib.sha256(data).hexdigest()
        if (len(data), self.sha256, nl) != (rec.get("bytes"), rec.get("sha256"), rec.get("lines")):
            raise Unverified("log %s does not match its download record" % os.path.basename(path))
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            raise Unverified("log %s is not UTF-8" % os.path.basename(path))
        self.bytes, self.lines_n = len(data), nl
        self.bom = text.startswith("\ufeff")
        self.cr = text.count("\r")
        whole = text.split("\n")
        if whole and whole[-1] == "":
            whole.pop()
        self.tail_text = "\n".join(whole[-5000:])
        body = (text[1:] if self.bom else text).replace("\r\n", "\n")
        raw = body.split("\n")
        if raw and raw[-1] == "":
            raw.pop()
        self.raw = raw
        self.s = [ex.strip(l) for l in raw]

    def find(self, header):
        return [i for i, l in enumerate(self.s) if l == header]

    def section(self, start):
        """[start, end): from a step's header to the next step header or the post-job cleanup."""
        for j in range(start + 1, len(self.s)):
            if self.s[j].startswith("##[group]Run ") or self.s[j] == "Post job cleanup.":
                return start, j
        return start, len(self.s)

    def body(self, a, b):
        """The lines of a section after its header group (the echoed command), as (index, text)."""
        k = a + 1
        while k < b and self.s[k] != "##[endgroup]":
            k += 1
        return [(i, self.s[i]) for i in range(k + 1, b)] if k < b else []


class Checks:
    def __init__(self, label):
        self.label, self.items, self.unverified = label, [], []

    def __call__(self, name, ok, detail=""):
        self.items.append((name, bool(ok), detail))
        return bool(ok)

    @property
    def failed(self):
        return [x for x in self.items if not x[1]]

    def verdict(self):
        return "FAILS" if self.failed else "UNVERIFIED" if self.unverified else "HOLDS"


def markers(ex, lines):
    return {k: sum(1 for l in lines if rx.search(l)) for k, rx in ex.MARKERS.items()}


def first_hits(lines_idx, rx, n=3):
    return [(i + 1, l[:160]) for i, l in lines_idx if rx.search(l)][:n]


# ------------------------------------------------------------------------------------------------ parsers

A3_OPEN = re.compile(r"^##\[group\](\S+) \(exit (-?\d+)\)$")
A3_JUDGED = re.compile(r"^(OK  |BAD ) (\S+) expected (pass|fail)$")
A3_FINAL = re.compile(r"^A3-CHECK-NONVACUOUS: (\d+) cases as expected$")
A3_BAD = re.compile(r"^(A3 FAIL|A3-CHECK-NOT-ESTABLISHED|RUN FAIL)")
A3_ERROR = re.compile(r"^(?:\S*/)?([A-Za-z0-9_]+\.lean):(\d+):(\d+): error: (.*)$")
A3_CODE = re.compile(r"^(STMT-IDENTITY\b.*|DEPCHECK (?:PASS|FAIL|closure|watched)\b|DEPCHECK-[A-Z-]+)")


def parse_a3(body):
    cases, order, final, bad, cur, stray = {}, [], None, [], None, []
    for i, l in body:
        if cur is not None:
            if l == "##[endgroup]":
                cur = None
                continue
            m = A3_ERROR.match(l)
            if m:
                c["errors"].append("%s:%s:%s: error: %s" % m.groups())
                continue
            m = A3_CODE.match(l)
            if m:
                k = m.group(1) if m.group(1).startswith("STMT-IDENTITY") else m.group(1).rstrip()
                c["codes"][k] = c["codes"].get(k, 0) + 1
            if A3_BAD.match(l):
                bad.append((i, l))
            continue
        m = A3_OPEN.match(l)
        if m:
            c = {"exit": int(m.group(2)), "codes": {}, "errors": [], "judged": None, "expected": None,
                 "_lines": [i + 1]}
            if m.group(1) in cases:
                bad.append((i, "duplicate case " + m.group(1)))
            cases[m.group(1)] = c
            order.append(m.group(1))
            cur = m.group(1)
            continue
        m = A3_JUDGED.match(l)
        if m:
            name = m.group(2)
            if name not in cases or cases[name]["judged"] is not None:
                bad.append((i, l))
            else:
                cases[name]["judged"], cases[name]["expected"] = m.group(1).strip(), m.group(3)
                cases[name]["_lines"].append(i + 1)
            continue
        m = A3_FINAL.match(l)
        if m:
            if final is not None:
                bad.append((i, "second final line"))
            final = (i + 1, l, int(m.group(1)))
            continue
        if A3_BAD.match(l):
            bad.append((i, l))
            continue
        if l.strip():
            stray.append((i, l))
    if cur is not None:
        bad.append((-1, "case %s never closed" % cur))
    for c in cases.values():
        c["errors"].sort()
    return cases, order, final, bad, stray


PROBE_PASS = re.compile(r"^PASS ([A-Z0-9]+) \((\d+)\)$")
PROBE_CHECKS = re.compile(r"^checks: (\d+), failures: (\d+)$")
PROBE_REJ = re.compile(r"^REJECTED ([A-Za-z0-9-]+): ([A-Z0-9]+)$")
PROBE_MUT = re.compile(r"^mutations: (\d+) rejected, (\d+) accepted$")
PROBE_VERD = re.compile(r"^VERDICT (\S+)$")


def parse_probe(body):
    p = {"codes": {}, "checks": None, "rejected": {}, "mutations": None, "verdicts": [], "other": [], "lines": {}}
    for i, l in body:
        if not l.strip():
            continue
        m = PROBE_PASS.match(l)
        if m:
            # a code seen twice is recorded as -1, which the "once each" check rejects
            p["codes"][m.group(1)] = -1 if m.group(1) in p["codes"] else int(m.group(2))
            p["lines"]["PASS " + m.group(1)] = i + 1
            continue
        m = PROBE_CHECKS.match(l)
        if m and p["checks"] is None:
            p["checks"] = (int(m.group(1)), int(m.group(2)))
            p["lines"]["checks"] = i + 1
            continue
        m = PROBE_REJ.match(l)
        if m and m.group(1) not in p["rejected"]:
            p["rejected"][m.group(1)] = m.group(2)
            p["lines"]["REJECTED " + m.group(1)] = i + 1
            continue
        m = PROBE_MUT.match(l)
        if m and p["mutations"] is None:
            p["mutations"] = (int(m.group(1)), int(m.group(2)))
            p["lines"]["mutations"] = i + 1
            continue
        m = PROBE_VERD.match(l)
        if m:
            p["verdicts"].append(m.group(1))
            p["lines"]["VERDICT"] = i + 1
            continue
        p["other"].append((i, l))
    return p


CTRL_PASS = re.compile(r"^PASS self: (.+)$")
CTRL_FINAL = re.compile(r"^controls: (\S+) \((\d+) failure\(s\)\)$")


def parse_controls(body):
    c = {"passes": [], "final": [], "other": [], "lines": {}}
    for i, l in body:
        if not l.strip():
            continue
        m = CTRL_PASS.match(l)
        if m:
            c["passes"].append(m.group(1))
            c["lines"].setdefault(m.group(1), i + 1)
            continue
        m = CTRL_FINAL.match(l)
        if m:
            c["final"].append((i + 1, l))
            continue
        c["other"].append((i, l))
    return c


# ------------------------------------------------------------------------------------------------ assembly

def load_json(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as e:
        raise Unverified("%s unreadable: %s" % (os.path.basename(path), type(e).__name__))


def _need(cond, what):
    if not cond:
        raise Unverified("malformed record: " + what)


def _typed(obj, where, fields):
    """Each (key, types) must be present and of one of the types (a bool is never an int; null is never allowed)."""
    for k, t in fields:
        _need(k in obj, "%s lacks %s" % (where, k))
        v = obj[k]
        _need(isinstance(v, t) and not (isinstance(v, bool) and bool not in (t if isinstance(t, tuple) else (t,))),
              "%s field %s is %s" % (where, k, "null" if v is None else type(v).__name__))


def check_run_record(run, rid):
    where = "run-%s.json" % rid
    _need(isinstance(run, dict), "%s is not a JSON object" % where)
    _typed(run, where, (("id", int), ("head_sha", str), ("run_attempt", int), ("event", str),
                        ("conclusion", str), ("path", str)))


def check_jobs_record(jobsd, rid):
    where = "jobs-%s.json" % rid
    _need(isinstance(jobsd, dict), "%s is not a JSON object" % where)
    _typed(jobsd, where, (("total_count", int), ("jobs", list)))
    for n, j in enumerate(jobsd["jobs"]):
        w = "%s job %d" % (where, n)
        _need(isinstance(j, dict), "%s is not a JSON object" % w)
        _typed(j, w, (("id", int), ("run_id", int), ("run_attempt", int), ("name", str), ("conclusion", str),
                      ("head_sha", str), ("steps", list)))
        for m, st in enumerate(j["steps"]):
            ws = "%s step %d" % (w, m)
            _need(isinstance(st, dict), "%s is not a JSON object" % ws)
            _typed(st, ws, (("number", int), ("name", str), ("conclusion", str)))


def check_download_record(d):
    """{job id: record}; a record whose outcome is ok must carry its length, digest and line count."""
    _need(isinstance(d, dict), "the download record is not a JSON object")
    _typed(d, "the download record", (("logs", list),))
    out = {}
    for n, r in enumerate(d["logs"]):
        w = "download record entry %d" % n
        _need(isinstance(r, dict), "%s is not a JSON object" % w)
        _typed(r, w, (("job_id", (str, int)), ("outcome", str)))
        if r["outcome"] == "ok":
            _typed(r, w, (("bytes", int), ("sha256", str), ("lines", int)))
        _need(str(r["job_id"]) not in out, "%s repeats job %s" % (w, r["job_id"]))
        out[str(r["job_id"])] = r
    return out


def module_sources(src, head, C):
    """{module: (text, blob)} from a checkout of the run's head, each checked with git."""
    if git(src, "rev-parse", "HEAD") != head:
        raise Unverified("source checkout HEAD is not %s" % head)
    out = {}
    for mod in GOVERNED:
        p = os.path.join(src, LEAN_DIR, mod)
        try:
            with open(p, "rb") as f:
                data = f.read()
        except OSError:
            raise Unverified("source %s absent from the checkout" % mod)
        blob = git_blob_id(data)
        if git(src, "rev-parse", "HEAD:" + LEAN_DIR + mod) != blob:
            raise Unverified("source %s differs from HEAD's blob" % mod)
        out[mod] = (data.decode("utf-8"), blob)
    return out


def assemble_run(key, cfg, ex, inputs):
    """Returns (Checks, result dict or None)."""
    C = Checks(key)
    head, rid = cfg["head"], cfg["run_id"]
    try:
        run = load_json(os.path.join(inputs["host"], "run-%s.json" % rid))
        check_run_record(run, rid)
        jobsd = load_json(os.path.join(inputs["host"], "jobs-%s.json" % rid))
        check_jobs_record(jobsd, rid)
        recs = check_download_record(load_json(inputs["download_record"]))
        blog = Log(os.path.join(inputs["logs"], cfg["bridge_job"] + ".log"), recs.get(cfg["bridge_job"]), ex)
        plog = Log(os.path.join(inputs["logs"], cfg["probe_job"] + ".log"), recs.get(cfg["probe_job"]), ex)
        srcs = module_sources(inputs["src"][key], head, C)
    except Unverified as e:
        C.unverified.append(str(e))
        return C, None
    except Exception as e:  # noqa: BLE001 - any other failure while reading the inputs is an unverified run
        C.unverified.append("malformed input: %s: %s" % (type(e).__name__, str(e)[:200]))
        return C, None

    # --- run identity and jobs (API)
    C("run: id, head, attempt 1, event workflow_dispatch, conclusion success",
      str(run.get("id")) == rid and run.get("head_sha") == head and run.get("run_attempt") == 1
      and run.get("event") == "workflow_dispatch" and run.get("conclusion") == "success"
      and run.get("path") == ".github/workflows/verify.yml",
      "id=%s head=%s attempt=%s event=%s conclusion=%s" % (run.get("id"), str(run.get("head_sha"))[:12],
                                                          run.get("run_attempt"), run.get("event"), run.get("conclusion")))
    jobs = jobsd.get("jobs") or []
    C("jobs: the list is complete", jobs and len(jobs) == jobsd.get("total_count")
      and len({j.get("id") for j in jobs}) == len(jobs), "%d of %s" % (len(jobs), jobsd.get("total_count")))
    notok = [j.get("name") for j in jobs if j.get("conclusion") != "success"]
    C("jobs: every job success", jobs and not notok, "; ".join(map(str, notok))[:300])
    C("jobs: every job at the run's head, attempt 1",
      jobs and all(j.get("head_sha") == head and str(j.get("run_id")) == rid and j.get("run_attempt") == 1 for j in jobs))
    C("jobs: every job name distinct (the result maps names to conclusions)",
      len({j.get("name") for j in jobs}) == len(jobs))
    byid = {str(j.get("id")): j for j in jobs}
    bj, pj = byid.get(cfg["bridge_job"]), byid.get(cfg["probe_job"])
    C("jobs: the bridge job is %s %r" % (cfg["bridge_job"], JOB_BRIDGE), bj and bj.get("name") == JOB_BRIDGE)
    C("jobs: the probe job is %s %r" % (cfg["probe_job"], JOB_PROBE), pj and pj.get("name") == JOB_PROBE)
    bj, pj = bj or {}, pj or {}

    def steps(j):
        return {s.get("name"): s.get("conclusion") for s in j.get("steps") or []}
    bs, ps = steps(bj), steps(pj)
    for st in (STEP_BUILD, STEP_GATE, STEP_A3):
        C("bridge step %r success" % st[:40], bs.get(st) == "success", str(bs.get(st)))
    C("probe step %r success" % STEP_PROBE, ps.get(STEP_PROBE) == "success", str(ps.get(STEP_PROBE)))
    if cfg["controls"]:
        C("probe job step %r success" % STEP_CONTROLS, ps.get(STEP_CONTROLS) == "success", str(ps.get(STEP_CONTROLS)))
    else:
        C("run 1: no controls step in the probe job (not applicable)", STEP_CONTROLS not in ps)

    # --- the logs: complete, of this job, at this head
    for lg, name in ((blog, JOB_BRIDGE), (plog, JOB_PROBE)):
        tag = "bridge" if lg is blog else "probe"
        C("%s log: complete (runner header on line 1, cleanup at the end)" % tag,
          lg.s and lg.s[0].startswith("Current runner version: ") and "Cleaning up orphan processes" in lg.s[-8:],
          "line 1: %r" % (lg.s[0][:60] if lg.s else ""))
        C("%s log: job name line" % tag, ("Complete job name: " + name) in lg.s)
        k = [i for i, l in enumerate(lg.s) if l == "[command]/usr/bin/git log -1 --format=%H"]
        C("%s log: checked-out head is the run's head" % tag,
          len(k) == 1 and k[0] + 1 < len(lg.s) and lg.s[k[0] + 1] == head)

    # --- bridge sections: each found on its own, so a missing one is named and the others are still read
    hb, hg, ha = blog.find(HDR_BUILD), blog.find(HDR_GATE), blog.find(HDR_A3)
    for nm, h in (("Build", hb), ("Release gate", hg), ("A3", ha)):
        C("bridge log: one %s section" % nm, len(h) == 1, "%d found" % len(h))
    sec = {nm: blog.section(h[0]) for nm, h in (("build", hb), ("gate", hg), ("a3", ha)) if len(h) == 1}
    have = len(sec) == 3
    C("bridge log: the sections in step order, each ending at the next step",
      have and sec["build"][1] == hg[0] and sec["gate"][1] == ha[0])
    empty = (0, 0)
    b0, b1 = sec.get("build", empty)
    g0, g1 = sec.get("gate", empty)
    a0, a1 = sec.get("a3", empty)
    bx = ex.extract("\n".join(blog.raw[b0:b1])) if "build" in sec else {"build": None, "reports": {}, "markers": {}}
    gx = ex.extract("\n".join(blog.raw[g0:g1])) if "gate" in sec else {"gate": None, "markers": {}}
    # sorryAx, Lean.ofReduceBool and "declaration uses 'sorry'" may not appear in any step this result reads. The
    # controls self-test is excluded: its own test names mention sorryAx ("a sorryAx report on the recovery ...").
    hp = plog.find(HDR_PROBE)
    scopes = [("bridge Build, Release gate and A3 sections", [(i, blog.s[i]) for a, b in sec.values() for i in range(a, b)]),
              ("probe section", [(i, plog.s[i]) for i in range(*plog.section(hp[0]))] if len(hp) == 1 else [])]
    for where, idx in scopes:
        for mk in ("sorryAx", "Lean.ofReduceBool", "declaration uses 'sorry'"):
            hits = first_hits(idx, ex.MARKERS[mk])
            C("no %s in the %s" % (mk, where), idx and not hits, str(hits) if hits else "" if idx else "section absent")
    bline = bx.get("build")
    C("build: 'Build completed successfully' line in the Build section", bline and bline.get("success"))
    gate = gx.get("gate")
    gv = (gate or {}).get("verdict")
    C("gate: a release-gate block with steps and a verdict", gate and gate.get("steps") and gv)
    C("gate: verdict PASS and every step PASS", gv and gv.get("pass")
      and all(s["status"] == "PASS" for s in gate["steps"]),
      "" if not gate else "; ".join("%s %s" % (s["status"], s["name"]) for s in gate["steps"] if s["status"] != "PASS"))
    got_steps = [s["name"] for s in gate["steps"]] if gate and gate.get("steps") else []
    want_steps = list(cfg["gate_steps"])
    C("gate: exactly the %d steps of tools/release_gate.py at the head, in its order" % len(want_steps),
      gate is not None and len(got_steps) == len(want_steps) and got_steps == want_steps
      and sum(1 for s in gate["steps"] if s["status"] == "PASS") == len(want_steps),
      "%d steps; missing %s; unexpected %s" % (len(got_steps), [x for x in want_steps if x not in got_steps][:4],
                                               [x for x in got_steps if x not in want_steps][:4]))
    exp_markers = {k: (bx.get("markers") or {}).get(k, 0) + (gx.get("markers") or {}).get(k, 0) for k in MARKER_KEYS}
    C("markers: none in the Build and Release gate sections", "build" in sec and "gate" in sec
      and not any(exp_markers.values()),
      str(first_hits([(i, blog.s[i]) for i in range(b0, g1)], re.compile(r"error:|sorryAx|ofReduceBool|declaration uses")))
      if any(exp_markers.values()) else "")

    # --- modules
    modules, report_lines = {}, {}
    for mod in GOVERNED:
        text, blob = srcs[mod]
        pl = {i + 1 for i, l in enumerate(text.split("\n")) if re.match(r"^#print axioms\b", l)}
        reps = (bx.get("reports") or {}).get(mod, [])
        lines = [r["line"] for r in reps]
        names = [r["name"] for r in reps]
        complete = set(lines) == pl and len(lines) == len(pl) and len(set(names)) == len(names) and pl
        C("%s: one report per #print axioms line of the source at the head (%d prints)" % (mod, len(pl)), complete,
          "%d reports at %d distinct lines" % (len(reps), len(set(lines))))
        C("%s: no unclosed axiom list" % mod, not any(r.get("unclosed") for r in reps))
        out = [n for n, r in zip(names, reps) if r["axioms"] is not None and not set(r["axioms"]) <= set(PERMITTED)]
        C("%s: every axiom within propext, Classical.choice, Quot.sound" % mod, not out, ", ".join(out)[:300])
        modules[mod] = {"status": "complete" if complete else "partial" if lines else "none", "prints": len(pl),
                        "print_lines": spans(pl),
                        "reports": sorted(({"line": r["line"], "name": r["name"], "axioms": r["axioms"]} for r in reps),
                                          key=lambda r: (r["line"], r["name"]))}
        report_lines[mod] = {r["name"]: b0 + r["served_line"] for r in reps}
    C("%s: %d prints, as the preregistration freezes" % (MODULE, PRINTS), modules[MODULE]["prints"] == PRINTS,
      str(modules[MODULE]["prints"]))
    C("%s: the frozen blob %s" % (MODULE, FROZEN_MODULE_BLOB[:12]), srcs[MODULE][1] == FROZEN_MODULE_BLOB,
      srcs[MODULE][1])

    # --- absence line
    ab = [(i, l) for i, l in enumerate(blog.s[b0:b1], b0) if ABSENCE.match(l)]
    mtext = srcs[MODULE][0].split("\n")
    absence_ok = len(ab) == 1
    src_line = int(ABSENCE.match(ab[0][1]).group(1)) if absence_ok else None
    if absence_ok:
        absence_ok = 0 < src_line <= len(mtext) and mtext[src_line - 1].startswith("#eval")
    C("absence: one absence line in the Build section, at the source's #eval", absence_ok, "%d found" % len(ab))
    C("absence: the pair theorem is never reported present", not any(PRESENT in l for l in blog.s))

    # --- A3
    cases, order, final, bad, stray = parse_a3(blog.body(a0, a1)) if "a3" in sec else ({}, [], None, [], [])
    C("A3: final line 'A3-CHECK-NONVACUOUS: N cases as expected'", final is not None)
    C("A3: no failure line", not bad, str([(i + 1, l[:120]) for i, l in bad][:3]))
    C("A3: no unrecognized line between cases", not stray, str([(i + 1, l[:120]) for i, l in stray][:3]))
    C("A3: %d cases, each judged OK, and the final line counts them" % A3_CASES,
      len(cases) == A3_CASES and final is not None and final[2] == len(cases)
      and all(c["judged"] == "OK" for c in cases.values()), "%d cases" % len(cases))
    C("A3: expected-pass cases exit 0, expected-fail cases exit non-zero",
      cases and all((c["exit"] == 0) == (c["expected"] == "pass") for c in cases.values()))
    nmut = sum(1 for c in cases.values() if c["expected"] == "fail")
    C("A3: %d mutations fail" % A3_MUTATIONS, nmut == A3_MUTATIONS, str(nmut))
    a3_markers = markers(ex, blog.s[a0:a1]) if "a3" in sec else {}

    # --- probe
    hc = plog.find(HDR_CONTROLS)
    pp = parse_probe(plog.body(*plog.section(hp[0]))) if len(hp) == 1 else parse_probe([])
    C("probe: one probe section", len(hp) == 1, str(len(hp)))
    C("probe: final verdict line 'VERDICT %s'" % PROBE_VERDICT, pp["verdicts"] == [PROBE_VERDICT], str(pp["verdicts"]))
    C("probe: the 14 codes PASS, once each", sorted(pp["codes"]) == sorted(PROBE_CODES)
      and all(v > 0 for v in pp["codes"].values()), str(sorted(set(pp["codes"]) ^ set(PROBE_CODES))))
    C("probe: 'checks: %d, failures: 0'" % PROBE_N, pp["checks"] == (PROBE_N, 0), str(pp["checks"]))
    C("probe: five mutations rejected with the frozen codes, none accepted",
      pp["mutations"] == (5, 0) and sorted(pp["rejected"].values()) == sorted(PROBE_REJECTION_CODES),
      "%s %s" % (pp["mutations"], sorted(pp["rejected"].values())))
    C("probe: no other output (no FAIL, nothing on standard error)", not pp["other"],
      str([(i + 1, l[:120]) for i, l in pp["other"]][:3]))
    probe_markers = markers(ex, [l for _, l in plog.body(*plog.section(hp[0]))]) if len(hp) == 1 else {}

    # --- controls
    if cfg["controls"]:
        cc = parse_controls(plog.body(*plog.section(hc[0]))) if len(hc) == 1 else parse_controls([])
        C("controls: one controls section", len(hc) == 1, str(len(hc)))
        C("controls: final line 'controls: OK (0 failure(s))'",
          len(cc["final"]) == 1 and cc["final"][0][1] == "controls: OK (0 failure(s))", str(cc["final"])[:200])
        C("controls: PASS lines present, no other output", cc["passes"] and not cc["other"],
          "%d PASS; other %s" % (len(cc["passes"]), [(i + 1, l[:100]) for i, l in cc["other"]][:3]))
        C("controls: no PASS line repeated", len(set(cc["passes"])) == len(cc["passes"]))
        controls = {"applicable": True, "pass_lines": sorted(cc["passes"]),
                    "final": cc["final"][0][1] if cc["final"] else None}
        controls_obs = {"final": cc["final"][0][0] if cc["final"] else None, "pass_lines": cc["lines"],
                        "section": [hc[0] + 1, plog.section(hc[0])[1]] if hc else None}
    else:
        C("run 1: no controls section in the probe log (not applicable)", not hc)
        controls = {"applicable": False,
                    "reason": "run 1's tree has no controls.py and its probe job no controls self-test step"}
        controls_obs = None

    if C.failed or C.unverified:
        return C, None

    # --- the result
    expected = {
        "build_success": True,
        "gate": {"steps": [{"name": s["name"], "status": s["status"], "summary": s["summary"]} for s in gate["steps"]],
                 "steps_pass": sum(1 for s in gate["steps"] if s["status"] == "PASS"),
                 "steps_total": len(gate["steps"]), "verdict": gv["text"]},
        "markers": exp_markers,
        "modules": modules,
        "permitted_axioms": PERMITTED,
        "absence_check": {"module": MODULE, "source_line": src_line,
                          "text": ab[0][1][len("info: "):]},
        "a3_check": {"cases": {n: {"expected": c["expected"], "exit": c["exit"], "judged": c["judged"],
                                   "codes": c["codes"], "errors": c["errors"]} for n, c in cases.items()},
                     "final": final[1], "mutations_failing": nmut, "markers": a3_markers},
        "probe": {"codes": pp["codes"], "checks": pp["checks"][0], "failures": pp["checks"][1],
                  "rejected": pp["rejected"], "mutations_rejected": pp["mutations"][0],
                  "mutations_accepted": pp["mutations"][1], "verdict": pp["verdicts"][0], "markers": probe_markers},
        "controls": controls,
    }

    def job_steps(j):
        return [{"number": s.get("number"), "name": s.get("name"), "conclusion": s.get("conclusion")}
                for s in j.get("steps") or []]
    result = {
        "schema": "oi-evidence-result", "version": 1, "kind": "bridge", "form": "derived",
        "round": "KTOKEN-MAXCONE-1", "design_run": cfg["design_run"], "commit": head,
        "run": {"id": rid, "head_sha": head, "event": run["event"], "attempt": run["run_attempt"],
                "conclusion": run["conclusion"], "workflow": os.path.basename(run["path"]),
                "job_id": cfg["bridge_job"], "job_name": JOB_BRIDGE},
        "probe_job": {"id": cfg["probe_job"], "name": JOB_PROBE, "conclusion": pj.get("conclusion"),
                      "steps": job_steps(pj)},
        "bridge_job": {"id": cfg["bridge_job"], "name": JOB_BRIDGE, "conclusion": bj.get("conclusion"),
                       "steps": job_steps(bj)},
        "jobs": {"total": len(jobs), "conclusions": {j["name"]: j["conclusion"] for j in jobs}},
        "expected": expected,
        "observed": {
            "note": "1-based lines of the job log named in source.logs, after the byte-order mark; provenance of "
                    "this log, not compared",
            "build_line": {"line": b0 + bline["line"], "text": "Build completed successfully"},
            "gate_served_lines": {"start": g0 + gate["start_line"], "verdict": g0 + gv["served_line"]},
            "report_served_lines": report_lines,
            "reports_in_build_section": sum(len(v) for v in (bx.get("reports") or {}).values()),
            "absence_line": ab[0][0] + 1,
            "a3_lines": {"final": final[0], "cases": {n: c["_lines"] for n, c in cases.items()}},
            "probe_lines": pp["lines"],
            "controls_lines": controls_obs,
            "sections": {"bridge": {"build": [b0 + 1, b1], "gate": [g0 + 1, g1], "a3": [a0 + 1, a1]},
                         "probe": [hp[0] + 1, plog.section(hp[0])[1]]},
        },
        "source": {
            "extractor": EXTRACT_RESULT_PATH, "extractor_blob": EXTRACT_RESULT_BLOB, "extractor_commit": MAIN_COMMIT,
            "assembler": "extractor/assemble_evidence.py", "assembler_blob": own_blob("assemble_evidence.py"),
            "downloader": "extractor/download_job_logs.py", "downloader_blob": own_blob("download_job_logs.py"),
            "kind": "GitHub Actions job logs, each downloaded in full from the jobs/<id>/logs endpoint by a read-only "
                    "workflow, with the run and job records from the Actions runs and jobs API",
            "note": "the digests identify the bytes this result was read from: provenance of the extraction, not "
                    "independent proof of the result, which reproduction at the commit supplies",
            "logs": {r: {"job_id": lg_id, "bytes": lg.bytes, "lines": lg.lines_n, "source_sha256": lg.sha256,
                         "byte_order_mark": lg.bom, "carriage_returns": lg.cr}
                     for r, lg_id, lg in (("bridge", cfg["bridge_job"], blog), ("probe", cfg["probe_job"], plog))},
            "source_sha256": blog.sha256,
            "module_sources": {m: srcs[m][1] for m in GOVERNED},
        },
        "reproduce": {
            "compared": "build success; the gate's steps and verdict; each governed module's reports and axioms; "
                        "the markers (compare_result.py); then, by reading, check A3's cases and final line, the "
                        "probe's codes, counts and verdict" + (", and the controls self-test's lines" if cfg["controls"] else ""),
            "not_compared": "timestamps, durations, cache behaviour, build-job counts, output order, source lines",
            "recipe": [
                "run from the root of a full-history clone at a commit that carries "
                "verification/audits/evidence-retention (the verifier), with the object %s available; <dir> is a "
                "new directory and <log> a file outside it" % head,
                "git worktree add --detach <dir> %s" % head,
                "(cd <dir>/verification/lean-mathlib && lean --version && lake exe cache get && lake --rehash build) "
                "> <log> 2>&1",
                "(cd <dir> && python3 tools/release_gate.py) >> <log> 2>&1",
                "python3 -I verification/audits/evidence-retention/extract_result.py <log> > reproduced.json",
                "python3 -I verification/audits/evidence-retention/compare_result.py <this file> reproduced.json "
                "--tree <dir>",
                "(cd <dir>/verification/lean-mathlib && lake env python3 -I -B ../programmes/oi-qm/reconstruction/"
                "round-ktoken-maxcone-1/checks/run_checks.py run): every case and the final line as expected.a3_check",
                "(cd <dir> && python3 -I -B verification/lean/ktoken_maxcone1_probe.py --self-test): as expected.probe",
            ] + (["(cd <dir> && python3 -I -B verification/programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/"
                  "controls.py --self-test): as expected.controls"] if cfg["controls"] else []),
        },
    }
    return C, result


def overall(verdicts, runs):
    """HOLDS only when every run carries an explicit verdict and every verdict is HOLDS."""
    known = ("HOLDS", "FAILS", "UNVERIFIED")
    if any(verdicts.get(k) == "FAILS" for k in runs):
        return "FAILS"
    if set(verdicts) != set(runs) or any(verdicts.get(k) not in known for k in runs):
        return "UNVERIFIED"
    return "HOLDS" if all(verdicts[k] == "HOLDS" for k in runs) else "UNVERIFIED"


def canonical(obj):
    return json.dumps(obj, indent=1, sort_keys=True) + "\n"


def scan(text):
    return [(n + 1, m.group(0)[:6] + "...") for n, l in enumerate(text.split("\n")) for m in [SECRET.search(l)] if m]


def redact(s):
    return SECRET.sub("<redacted>", s)


def assemble(ex, inputs, runs=RUNS, out=None):
    """Prints the checks, the results and the verdict line; returns the exit code."""
    out = out or sys.stdout
    P = lambda s="": print(s, file=out)  # noqa: E731
    P("KTOKEN-MAXCONE-1 expected-result extraction (assembler blob %s, extract_result blob %s at %s)"
      % (own_blob("assemble_evidence.py")[:12], EXTRACT_RESULT_BLOB[:12], MAIN_COMMIT[:12]))
    verdicts, texts = {}, {}
    for key, cfg in runs.items():
        try:
            C, res = assemble_run(key, cfg, ex, inputs)
            if res is not None:
                text = canonical(res)
                hits = scan(text)
                C("output: credential, signed-URL, IP and e-mail scan of the result", not hits, str(hits[:3]))
                if not hits:
                    texts[key] = text
        except Exception as e:  # noqa: BLE001 - a run whose assembly stopped is unverified, never held
            C = Checks(key)
            C.unverified.append("assembly stopped: %s: %s" % (type(e).__name__, str(e)[:200]))
            texts.pop(key, None)
        for name, ok, detail in C.items:
            P("CHECK %s %s %s%s" % (key, "ok  " if ok else "FAIL", name, (" -- " + redact(detail)) if detail and not ok else ""))
        for u in C.unverified:
            P("CHECK %s UNVERIFIED %s" % (key, redact(u)))
        verdicts[key] = C.verdict()
        P("RESULT %s %s %s (%d checks, %d failed)" % (key, cfg["path"], verdicts[key], len(C.items), len(C.failed)))
    for key, cfg in runs.items():
        if key in texts and verdicts[key] == "HOLDS":
            P(BEGIN % cfg["path"])
            out.write(texts[key])
            P(END % cfg["path"])
            P("SHA256 %s %s" % (cfg["path"], hashlib.sha256(texts[key].encode("ascii")).hexdigest()))
    v = overall(verdicts, runs)
    P("EXTRACT %s" % v)
    return {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[v]


def crosscheck(inputs, ex, out=None):
    """Printed, never decisive: each downloaded log against the session's connector observation."""
    out = out or sys.stdout
    try:
        recs = check_download_record(load_json(inputs["download_record"]))
    except Exception as e:  # noqa: BLE001 - the cross-check is never decisive
        print("CROSSCHECK unavailable: %s" % redact(str(e))[:200], file=out)
        return
    for jid, (orig, served, tail_sha) in CONNECTOR.items():
        try:
            lg = Log(os.path.join(inputs["logs"], jid + ".log"), recs.get(jid), ex)
        except Exception as e:  # noqa: BLE001
            print("CROSSCHECK job %s unavailable: %s" % (jid, redact(str(e))[:200]), file=out)
            continue
        same_tail = hashlib.sha256(lg.tail_text.encode("utf-8")).hexdigest() == tail_sha
        print("CROSSCHECK job %s lines=%d connector_original_length=%d %s; last %d lines %s the session's served text"
              % (jid, lg.lines_n, orig, "equal" if lg.lines_n == orig else "DIFFERS", served,
                 "equal" if same_tail else "DIFFER FROM"), file=out)


def run_all(ex, inputs, runs=RUNS, out=None):
    """The cross-check, then the assembly; a verdict line is printed whatever is raised."""
    out = out or sys.stdout
    try:
        crosscheck(inputs, ex, out)
        return assemble(ex, inputs, runs, out)
    except Exception as e:  # noqa: BLE001
        print("CHECK all UNVERIFIED stopped: %s: %s" % (type(e).__name__, redact(str(e))[:200]), file=out)
        print("EXTRACT UNVERIFIED", file=out)
        return 2


# ------------------------------------------------------------------------------------------------ self-test

def _ts(i):
    return "2026-10-17T15:%02d:%02d.%07dZ " % (i // 3600 % 60, i // 60 % 60, i * 7919 % 10000000)


def _fixture_module(prints=PRINTS):
    """A synthetic module: `prints` #print axioms lines in two blocks and the absence #eval between them."""
    lines = ["import Mathlib", "", "namespace OIBridge.KTokenMaxCone", ""]
    names = ["d%02d" % i for i in range(prints)]
    first = prints // 2
    lines += ["theorem %s : True := trivial" % n for n in names] + [""]
    lines += ["#print axioms %s" % n for n in names[:first]] + [""]
    lines += ["#eval show MetaM Unit from do", "  logInfo \"absent\"", ""]
    lines += ["#print axioms %s" % n for n in names[first:]] + ["", "end OIBridge.KTokenMaxCone", ""]
    return "\n".join(lines)


def _fixture_root():
    return "\n".join(["import OIBridge.KTokenMaxCone", "", "#print axioms r0", "#print axioms r1", "#print axioms r2", ""])


A3_FIXTURE = [("Positive", "pass"), ("M_real", "pass"), ("M_direct", "fail"), ("M_iff", "fail"),
              ("M_inline", "fail"), ("M_deadref", "fail"), ("M_sibling", "fail"), ("M_required", "fail"),
              ("M_vac_target", "fail"), ("M_vac_sibling", "fail"), ("M_vac_module", "fail"),
              ("M_stmt_binder", "fail"), ("M_stmt_hyp", "fail")]


def _bridge_lines(head, module_text, root_text, variant=0, mut=None):
    """Stripped lines of a synthetic bridge log; variant changes only run-varying content."""
    mut = mut or {}
    L = ["Current runner version: '2.337.0'", "Worker ID: {%d}" % variant, "Complete job name: " + JOB_BRIDGE,
         "##[group]Run actions/checkout@v4", "##[endgroup]", "[command]/usr/bin/git log -1 --format=%H",
         mut.get("head", head), "##[group]Run lean --version", "\x1b[36;1mlean --version\x1b[0m",
         "shell: /usr/bin/bash -e {0}", "##[endgroup]", "Lean (version 4.0.0, x86_64-unknown-linux-gnu, Release)"]
    if variant:
        L += ["Cache restored from key: oibridge-Linux-%d" % variant]
    L += ["\u26a0 [%d/3653] Built OIBridge.KTokenMaxCone (%d.%ds)" % (3651 - variant, 6 + variant, variant)]
    mlines = module_text.split("\n")
    evl = next(i + 1 for i, l in enumerate(mlines) if l.startswith("#eval"))
    reps = []
    for i, l in enumerate(mlines):
        m = re.match(r"^#print axioms (\S+)$", l)
        if m:
            ax = mut.get("axioms", "propext, Classical.choice, Quot.sound") if m.group(1) == "d05" else \
                "propext, Classical.choice, Quot.sound"
            reps.append((i + 1, "info: OIBridge/KTokenMaxCone.lean:%d:0: 'OIBridge.KTokenMaxCone.%s' depends on "
                                "axioms: [%s]" % (i + 1, m.group(1), ax)))
    if mut.get("drop_one_report"):
        reps = reps[1:]
    if mut.get("drop_reports"):
        reps = []
    for ln, r in reps:
        if ln > evl and not mut.get("drop_absence") and not any(x.startswith("info: OIBridge/KTokenMaxCone.lean:%d:" % evl) for x in L):
            L.append("info: OIBridge/KTokenMaxCone.lean:%d:0: OIBridge.EqvK2MaxCone.pairCone_eq_Q3_of_drive_maxCone "
                     "is not in the environment" % evl)
        if r.endswith("'OIBridge.KTokenMaxCone.d10' depends on axioms: [propext, Classical.choice, Quot.sound]"):
            L += [r.replace(" Quot.sound]", ""), "  Quot.sound]"]   # a list wrapped over two lines
        else:
            L.append(r)
    for i, l in enumerate(root_text.split("\n")):
        m = re.match(r"^#print axioms (\S+)$", l)
        if m:
            L.append("info: OIBridge.lean:%d:0: 'OIBridge.X.%s' depends on axioms: [propext]" % (i + 1, m.group(1)))
    L += mut.get("build_extra", [])
    if not mut.get("drop_build"):
        L.append("Build completed successfully (%d jobs)." % (3653 + variant))
    L += ["TIMING lake-exe-cache-get %ds" % (86 + variant), "TIMING lake-rehash-build %ds" % (23 + variant)]
    L += [HDR_GATE, "\x1b[36;1mpython3 tools/release_gate.py\x1b[0m", "shell: /usr/bin/bash -e {0}", "##[endgroup]"]
    if not mut.get("drop_gate"):
        steps = [x for x in GATE_STEPS if x != mut.get("gate_drop_step")] + mut.get("gate_extra_steps", [])
        L += ["release gate", "=" * 20]
        for x in steps:
            st = mut.get("gate_status", "PASS") if x == "evidence-retention" else "PASS"
            summ = "EVIDENCE-RETENTION  HOLDS" + mut.get("gate_summary_extra", "") if x == "evidence-retention" \
                else "%s_check: OK (fixture)" % x
            L.append("  %s  %-16s %s" % (st, x, summ))
        L += ["=" * 20, "release gate: %s  (note: --label bNNN not given)" % mut.get("gate_verdict", "PASS")]
    L += [HDR_A3, "\x1b[36;1mlake env python3 ...\x1b[0m", "shell: /usr/bin/bash -e {0}", "##[endgroup]"]
    tmp = "/tmp/tmp%06d/" % (variant * 7 + 3)
    for name, exp in A3_FIXTURE:
        code = 0 if exp == "pass" else 1
        if mut.get("a3_exit0") == name:
            code = 0
        L.append("##[group]%s (exit %d)" % (name, code))
        if exp == "pass":
            L += ["STMT-IDENTITY ok", "DEPCHECK closure of X: %d constants" % 35179, "DEPCHECK watched A (B)",
                  "DEPCHECK PASS X"]
        else:
            L += ["DEPCHECK closure of X: 34756 constants", "%s%s.lean:30:0: error: DEPCHECK FAIL" % (tmp, name),
                  "DEPCHECK-MODULE OIBridge.EqvK2MaxCone.x (OIBridge.EqvK2MaxCone)"]
        L += mut.get("a3_inside", []) if name == "M_direct" else []
        L.append("##[endgroup]")
        L.append("%s %s expected %s" % ("BAD " if mut.get("a3_bad") == name else "OK  ", name, exp))
    if not mut.get("drop_a3_final"):
        L.append("A3-CHECK-NONVACUOUS: 13 cases as expected")
    L += ["Post job cleanup.", "[command]/usr/bin/git version", "Cleaning up orphan processes",
          "##[warning]Node.js 20 is deprecated."]
    if mut.get("truncate"):
        L = L[mut["truncate"]:]
    return L


def _probe_lines(head, controls, variant=0, mut=None):
    mut = mut or {}
    L = ["Current runner version: '2.337.0'", "Region: r%d" % variant, "Complete job name: " + JOB_PROBE,
         "##[group]Run actions/checkout@v4", "##[endgroup]", "[command]/usr/bin/git log -1 --format=%H", head,
         HDR_PROBE, "\x1b[36;1mpython3 -I -B verification/lean/ktoken_maxcone1_probe.py --self-test\x1b[0m",
         "shell: /usr/bin/bash -e {0}", "env:", "  pythonLocation: /opt/hostedtoolcache/Python/3.11.17/x64",
         "##[endgroup]"]
    counts = [2082, 4, 40, 2, 2, 914, 1, 1, 1, 2, 1, 3, 1, 142]
    L += ["PASS %s (%d)" % (c, n) for c, n in zip(PROBE_CODES, counts)]
    L += mut.get("probe_extra", [])
    L.append("checks: %d, failures: 0" % mut.get("probe_n", PROBE_N))
    L += ["REJECTED trace-factor: DICT3", "REJECTED adjoint: ADJOINT3", "REJECTED shift-sign: SHIFT3",
          "REJECTED group-below-168: ORBIT3", "REJECTED cut-direction: CUT3", "mutations: 5 rejected, 0 accepted"]
    if not mut.get("drop_probe_verdict"):
        L.append("VERDICT KTOKEN-K3-EXACT")
    if controls or mut.get("controls_in_run1"):
        L += [HDR_CONTROLS, "\x1b[36;1mpython3 -I -B .../controls.py --self-test\x1b[0m", "shell: /usr/bin/bash -e {0}",
              "##[endgroup]", "PASS self: D agrees with the preregistration",
              "PASS self: S1 rejects the mutation: i < j replaced by i \u2260 j",
              "PASS self: a sorryAx report on the recovery fails Q-PAIR alone",   # the real run 2 prints this line
              "PASS self: 38 self-checks ran, as frozen (38)"]
        if not mut.get("drop_controls_final"):
            L.append("controls: OK (0 failure(s))")
    L += ["Post job cleanup.", "Cleaning up orphan processes", "##[warning]Node.js 20 is deprecated."]
    return L


def _write_log(path, lines, variant):
    text = "\ufeff" + "\n".join(_ts(i + 1000 * variant) + l for i, l in enumerate(lines)) + "\n"
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return {"job_id": os.path.basename(path)[:-4], "outcome": "ok", "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest(), "lines": data.count(b"\n")}


def _git_repo(d, files):
    os.makedirs(d)
    for rel, text in files.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
    for args in (["init", "-q"], ["add", "-A"],
                 ["-c", "user.name=selftest", "-c", "user.email=selftest@example.invalid", "-c", "commit.gpgsign=false",
                  "commit", "-q", "-m", "fixture"]):
        subprocess.run(["git", "-C", d] + args, check=True, capture_output=True, env=env, timeout=60)
    return git(d, "rev-parse", "HEAD")


def _fixture(base, variant=0, mut=None):
    """Writes a complete synthetic input set under base; returns (inputs, runs)."""
    mut = mut or {}
    os.makedirs(base)
    module, root = mut.get("module_text", _fixture_module()), _fixture_root()
    srcs, heads = {}, {}
    for k in ("run1", "run2"):
        srcs[k] = os.path.join(base, "src-" + k)
        heads[k] = _git_repo(srcs[k], {LEAN_DIR + MODULE: mut.get("source_text", module), LEAN_DIR + "OIBridge.lean": root,
                                       "marker-%s" % k: k})
    blob = git_blob_id(_fixture_module().encode())
    runs = {}
    for n, k in ((1, "run1"), (2, "run2")):
        runs[k] = dict(RUNS[k], head=heads[k], run_id=str(900 + n), bridge_job=str(9100 + n), probe_job=str(9200 + n))
    host, logs = os.path.join(base, "host"), os.path.join(base, "logs")
    os.makedirs(host)
    os.makedirs(logs)
    recs = []
    for k, cfg in runs.items():
        mk = mut.get(k, {})
        run = {"id": int(cfg["run_id"]), "head_sha": cfg["head"], "run_attempt": 1, "event": "workflow_dispatch",
               "conclusion": mk.get("run_conclusion", "success"), "path": ".github/workflows/verify.yml"}
        psteps = [STEP_PROBE] + ([STEP_CONTROLS] if cfg["controls"] and not mk.get("no_controls_step") else [])
        jobs = [{"id": int(cfg["bridge_job"]), "name": JOB_BRIDGE, "conclusion": "success", "head_sha": cfg["head"],
                 "run_id": int(cfg["run_id"]), "run_attempt": 1,
                 "steps": [{"number": i + 1, "name": s, "conclusion": "success", "started_at": _ts(i)}
                           for i, s in enumerate(["Set up job", STEP_BUILD, STEP_GATE, STEP_A3])]},
                {"id": int(cfg["probe_job"]), "name": JOB_PROBE, "conclusion": "success", "head_sha": cfg["head"],
                 "run_id": int(cfg["run_id"]), "run_attempt": 1,
                 "steps": [{"number": i + 1, "name": s, "conclusion": "success"} for i, s in enumerate(psteps)]},
                {"id": 9300 + cfg["design_run"], "name": "Numerical probes", "conclusion": mk.get("other_job", "success"),
                 "head_sha": cfg["head"], "run_id": int(cfg["run_id"]), "run_attempt": 1, "steps": []}]
        for edit in mk.get("run_edits", []):
            edit(run)
        jobsd = {"total_count": len(jobs), "jobs": jobs}
        for edit in mk.get("jobs_edits", []):
            edit(jobsd)
        with open(os.path.join(host, "run-%s.json" % cfg["run_id"]), "wb") as f:
            f.write(mk["run_raw"](json.dumps(run).encode()) if "run_raw" in mk else json.dumps(run).encode())
        if not mk.get("drop_jobs_json"):
            with open(os.path.join(host, "jobs-%s.json" % cfg["run_id"]), "wb") as f:
                f.write(mk["jobs_raw"](json.dumps(jobsd).encode()) if "jobs_raw" in mk else json.dumps(jobsd).encode())
        recs.append(_write_log(os.path.join(logs, cfg["bridge_job"] + ".log"),
                               _bridge_lines(cfg["head"], module, root, variant, mk.get("bridge")), variant))
        recs.append(_write_log(os.path.join(logs, cfg["probe_job"] + ".log"),
                               _probe_lines(cfg["head"], cfg["controls"], variant, mk.get("probe")), variant))
    for r in recs:
        if mut.get("bad_record") == r["job_id"]:
            r["sha256"] = "0" * 64
    for edit in mut.get("record_edits", []):
        edit(recs)
    rec_path = os.path.join(base, "download-record.json")
    body = json.dumps({"logs": recs}).encode()
    with open(rec_path, "wb") as f:
        f.write(mut["record_raw"](body) if "record_raw" in mut else body)
    return {"host": host, "logs": logs, "download_record": rec_path, "src": srcs}, runs, blob


def self_test(extractor_path, work=None):
    global FROZEN_MODULE_BLOB
    base = tempfile.mkdtemp(prefix="assemble-selftest-", dir=work)
    saved = FROZEN_MODULE_BLOB
    fails, n = 0, 0
    try:
        ex = load_extractor(extractor_path)

        def run_case(name, mut, want, needle=None, variant=0):
            nonlocal fails, n
            n += 1
            d = os.path.join(base, "c%03d" % n)
            inputs, runs, blob = _fixture(d, variant, mut)
            globals()["FROZEN_MODULE_BLOB"] = blob
            buf = io.StringIO()
            code = run_all(ex, inputs, runs, out=buf)
            text = buf.getvalue()
            verdict = text.strip().split("\n")[-1]
            ok = verdict == "EXTRACT " + want and (needle is None or needle in text)
            if want != "HOLDS":
                failing = [k for k in runs if ("RESULT %s %s HOLDS" % (k, runs[k]["path"])) not in text]
                ok = ok and all((BEGIN % runs[k]["path"]) not in text for k in failing)
            ok = ok and code == {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[want]
            print("  %s  %s -> %s" % ("ok  " if ok else "FAIL", name, verdict))
            if not ok:
                fails += 1
                print("\n".join("        | " + l for l in text.split("\n")
                                if re.match(r"^(CHECK \S+ (FAIL|UNVERIFIED)|RESULT )", l))[:3000])
            return text

        print("assemble self-test (synthetic fixtures, local git repositories, no network):")
        t0 = run_case("clean fixtures for both runs hold (run 2's controls lines mention sorryAx, as the real ones do)",
                      {}, "HOLDS")
        t1 = run_case("the same evidence with other timestamps, tmp paths, durations, cache lines and job counts "
                      "holds", {}, "HOLDS", variant=3)

        def blocks(t):
            return re.findall(r"===== BEGIN EXPECTED RESULT (\S+) =====\n(.*?)===== END", t, re.S)
        b0, b1 = blocks(t0), blocks(t1)
        n += 1
        same = len(b0) == 2 and [p for p, _ in b0] == [p for p, _ in b1] and all(
            json.loads(x)["expected"] == json.loads(y)["expected"] for (_, x), (_, y) in zip(b0, b1))
        print("  %s  the expected sections are identical across the two variants" % ("ok  " if same else "FAIL"))
        fails += not same
        n += 1
        ok = len(b0) == 2 and all(x == canonical(json.loads(x)) and x.isascii() for _, x in b0)
        sha_ok = all(("SHA256 %s %s" % (p, hashlib.sha256(x.encode()).hexdigest())) in t0 for p, x in b0)
        print("  %s  each printed block is canonical ASCII JSON and its SHA256 line matches" %
              ("ok  " if ok and sha_ok else "FAIL"))
        fails += not (ok and sha_ok)
        n += 1
        r1 = json.loads(b0[0][1]) if b0 else {}
        na = r1.get("expected", {}).get("controls", {}).get("applicable") is False and b0[0][0].startswith("evidence/run1")
        print("  %s  run 1 records the controls self-test as not applicable, not as a pass" % ("ok  " if na else "FAIL"))
        fails += not na
        n += 1
        tv = "2026-10-17T" not in "".join(x for _, x in b0) and "/tmp/" not in "".join(x for _, x in b0) \
            and "Cache" not in "".join(x for _, x in b0) and "(3653 jobs)" not in "".join(x for _, x in b0)
        print("  %s  no timestamp, temporary path, cache line or build-job count in a result" % ("ok  " if tv else "FAIL"))
        fails += not tv

        R2 = "run2"
        run_case("no build line", {R2: {"bridge": {"drop_build": True}}}, "FAILS", "FAIL build: 'Build completed successfully'")
        run_case("no gate block", {R2: {"bridge": {"drop_gate": True}}}, "FAILS", "FAIL gate: a release-gate block")
        run_case("a failing gate verdict", {R2: {"bridge": {"gate_verdict": "FAIL", "gate_status": "FAIL"}}}, "FAILS",
                 "FAIL gate: verdict PASS")
        run_case("no KTokenMaxCone reports", {R2: {"bridge": {"drop_reports": True}}}, "FAILS",
                 "FAIL OIBridge/KTokenMaxCone.lean: one report per")
        run_case("one KTokenMaxCone report missing", {R2: {"bridge": {"drop_one_report": True}}}, "FAILS",
                 "FAIL OIBridge/KTokenMaxCone.lean: one report per")
        run_case("an axiom outside the permitted three", {R2: {"bridge": {"axioms": "propext, Lean.trustCompiler"}}},
                 "FAILS", "FAIL OIBridge/KTokenMaxCone.lean: every axiom")
        run_case("a sorryAx report", {R2: {"bridge": {"axioms": "propext, sorryAx"}}}, "FAILS", "FAIL no sorryAx in the bridge")
        run_case("a sorryAx line in check A3's output", {R2: {"bridge": {"a3_inside": ["DEPCHECK-MODULE sorryAx (X)"]}}},
                 "FAILS", "FAIL no sorryAx in the bridge")
        run_case("an error line in the Build section", {R2: {"bridge": {"build_extra": ["error: OIBridge/X.lean:1:0: boom"]}}},
                 "FAILS", "FAIL markers: none in the Build")
        run_case("no absence line", {R2: {"bridge": {"drop_absence": True}}}, "FAILS", "FAIL absence: one absence line")
        run_case("no A3 final line", {R2: {"bridge": {"drop_a3_final": True}}}, "FAILS", "FAIL A3: final line")
        run_case("an A3 case judged BAD", {R2: {"bridge": {"a3_bad": "M_iff"}}}, "FAILS", "FAIL A3: 13 cases, each judged OK")
        run_case("an A3 mutation that compiled", {R2: {"bridge": {"a3_exit0": "M_sibling"}}}, "FAILS",
                 "FAIL A3: expected-pass cases exit 0")
        run_case("a sorryAx line in the probe section", {R2: {"probe": {"probe_extra": ["sorryAx"]}}}, "FAILS",
                 "FAIL no sorryAx in the probe section")
        run_case("no probe verdict", {R2: {"probe": {"drop_probe_verdict": True}}}, "FAILS", "FAIL probe: final verdict")
        run_case("a probe FAIL line", {R2: {"probe": {"probe_extra": ["FAIL SEP3 (1)"]}}}, "FAILS", "FAIL probe: no other output")
        run_case("a probe check count other than the frozen N", {R2: {"probe": {"probe_n": 3195}}}, "FAILS",
                 "FAIL probe: 'checks: 3196")
        run_case("run 2 without the controls OK line", {R2: {"probe": {"drop_controls_final": True}}}, "FAILS",
                 "FAIL controls: final line")
        run_case("run 2 without the controls step in the jobs API", {R2: {"no_controls_step": True}}, "FAILS",
                 "FAIL probe job step 'Native control mutation tests' success")
        run_case("run 1 with a controls section", {"run1": {"probe": {"controls_in_run1": True}}}, "FAILS",
                 "FAIL run 1: no controls section")
        run_case("a job that did not succeed", {R2: {"other_job": "failure"}}, "FAILS", "FAIL jobs: every job success")
        run_case("a run that did not succeed", {R2: {"run_conclusion": "failure"}}, "FAILS", "FAIL run: id, head")
        run_case("a log checked out at another head", {R2: {"bridge": {"head": "f" * 40}}}, "FAILS",
                 "FAIL bridge log: checked-out head")
        run_case("a truncated log (a served tail)", {R2: {"bridge": {"truncate": 9}}}, "FAILS", "FAIL bridge log: complete")
        run_case("a credential-shaped string in the result",
                 {R2: {"bridge": {"gate_summary_extra": " (contact someone@example.com)"}}}, "FAILS",
                 "FAIL output: credential")
        run_case("a module source other than the frozen blob",
                 {"module_text": _fixture_module() + "\n-- edited\n"}, "FAILS", "FAIL OIBridge/KTokenMaxCone.lean: the frozen blob")
        run_case("a #print axioms line in the source at the head with no report in the log",
                 {"source_text": _fixture_module() + "#print axioms extra\n"}, "FAILS",
                 "FAIL OIBridge/KTokenMaxCone.lean: one report per")
        run_case("a log that does not match its download record", {"bad_record": "9102"}, "UNVERIFIED",
                 "UNVERIFIED log 9102.log does not match its download record")
        run_case("a missing jobs record", {R2: {"drop_jobs_json": True}}, "UNVERIFIED", "UNVERIFIED jobs-902.json unreadable")
        # N1: the gate's step lines against the 22 steps of tools/release_gate.py at the head
        G = "FAIL gate: exactly the 22 steps of tools/release_gate.py"
        run_case("a gate block with one step line deleted", {R2: {"bridge": {"gate_drop_step": "voice"}}}, "FAILS", G)
        run_case("a gate block with an extra step line", {R2: {"bridge": {"gate_extra_steps": ["extra-step"]}}},
                 "FAILS", G)
        run_case("a gate block with a step line repeated", {R2: {"bridge": {"gate_extra_steps": ["voice"]}}},
                 "FAILS", G)
        # N2: malformed records are unverified, with a reason, and never crash or hold
        U = "UNVERIFIED "
        run_case("a truncated run record", {R2: {"run_raw": lambda b: b[:len(b) // 2]}}, "UNVERIFIED",
                 U + "run-902.json unreadable: JSONDecodeError")
        run_case("a truncated jobs record", {R2: {"jobs_raw": lambda b: b[:-7]}}, "UNVERIFIED",
                 U + "jobs-902.json unreadable: JSONDecodeError")
        run_case("a truncated download record", {"record_raw": lambda b: b[:-5]}, "UNVERIFIED",
                 U + "download-record.json unreadable: JSONDecodeError")
        run_case("a run record that is not an object", {R2: {"run_raw": lambda b: b'"run"'}}, "UNVERIFIED",
                 U + "malformed record: run-902.json is not a JSON object")
        run_case("a jobs record that is a list", {R2: {"jobs_raw": lambda b: b"[1, 2]"}}, "UNVERIFIED",
                 U + "malformed record: jobs-902.json is not a JSON object")
        run_case("a download record that is a list", {"record_raw": lambda b: b"[]"}, "UNVERIFIED",
                 U + "malformed record: the download record is not a JSON object")
        run_case("a jobs list holding null", {R2: {"jobs_edits": [lambda d: d["jobs"].insert(0, None)]}}, "UNVERIFIED",
                 U + "malformed record: jobs-902.json job 0 is not a JSON object")
        run_case("a run record without head_sha", {R2: {"run_edits": [lambda r: r.pop("head_sha")]}}, "UNVERIFIED",
                 U + "malformed record: run-902.json lacks head_sha")
        run_case("a jobs record without total_count", {R2: {"jobs_edits": [lambda d: d.pop("total_count")]}},
                 "UNVERIFIED", U + "malformed record: jobs-902.json lacks total_count")
        run_case("a job without a name", {R2: {"jobs_edits": [lambda d: d["jobs"][0].pop("name")]}}, "UNVERIFIED",
                 U + "malformed record: jobs-902.json job 0 lacks name")
        run_case("a download entry without sha256", {"record_edits": [lambda r: r[2].pop("sha256")]}, "UNVERIFIED",
                 U + "malformed record: download record entry 2 lacks sha256")
        run_case("a run record with a null conclusion", {R2: {"run_edits": [lambda r: r.update(conclusion=None)]}},
                 "UNVERIFIED", U + "malformed record: run-902.json field conclusion is null")
        run_case("a job with a null name", {R2: {"jobs_edits": [lambda d: d["jobs"][1].update(name=None)]}},
                 "UNVERIFIED", U + "malformed record: jobs-902.json job 1 field name is null")
        run_case("a step with a null conclusion",
                 {R2: {"jobs_edits": [lambda d: d["jobs"][0]["steps"][1].update(conclusion=None)]}}, "UNVERIFIED",
                 U + "malformed record: jobs-902.json job 0 step 1 field conclusion is null")
        run_case("a download entry with null bytes", {"record_edits": [lambda r: r[2].update(bytes=None)]},
                 "UNVERIFIED", U + "malformed record: download record entry 2 field bytes is null")
        run_case("a run attempt given as true", {R2: {"run_edits": [lambda r: r.update(run_attempt=True)]}},
                 "UNVERIFIED", U + "malformed record: run-902.json field run_attempt is bool")
        run_case("a run record with a non-UTF-8 byte", {R2: {"run_raw": lambda b: b[:10] + b"\xff" + b[10:]}},
                 "UNVERIFIED", U + "run-902.json unreadable: UnicodeDecodeError")
        run_case("a download record with a non-UTF-8 byte", {"record_raw": lambda b: b[:10] + b"\xff" + b[10:]},
                 "UNVERIFIED", U + "download-record.json unreadable: UnicodeDecodeError")
        # N2: every run must carry an explicit verdict before the whole can hold
        real = globals()["assemble_run"]

        def stopping(key, cfg, ex_, inputs_):
            if key == "run2":
                raise RuntimeError("fixture stop")
            return real(key, cfg, ex_, inputs_)
        globals()["assemble_run"] = stopping
        try:
            run_case("a run whose assembly raises", {}, "UNVERIFIED", U + "assembly stopped: RuntimeError: fixture stop")
        finally:
            globals()["assemble_run"] = real
        n += 1
        two = {"run1": {}, "run2": {}}
        ok = (overall({"run1": "HOLDS", "run2": "HOLDS"}, two) == "HOLDS"
              and overall({"run1": "HOLDS"}, two) == "UNVERIFIED"
              and overall({"run1": "HOLDS", "run2": None}, two) == "UNVERIFIED"
              and overall({"run1": "HOLDS", "run2": "MAYBE"}, two) == "UNVERIFIED"
              and overall({}, two) == "UNVERIFIED"
              and overall({"run1": "HOLDS", "run2": "FAILS"}, two) == "FAILS"
              and overall({"run1": "UNVERIFIED", "run2": "HOLDS"}, two) == "UNVERIFIED")
        print("  %s  the whole holds only when both runs carry an explicit HOLDS" % ("ok  " if ok else "FAIL"))
        fails += not ok
        n += 1
        bad = os.path.join(base, "extract_result.py")
        with open(extractor_path, "rb") as f, open(bad, "wb") as g:
            g.write(f.read().replace(b"sorryAx", b"sorryAX"))
        try:
            load_extractor(bad)
            ok = False
        except Unverified:
            ok = True
        print("  %s  an extractor other than the pinned blob is refused before it runs" % ("ok  " if ok else "FAIL"))
        fails += not ok
        n += 1
        hits = scan('{\n "a": "ghp_' + "a" * 30 + '",\n "b": "https://x.blob.core.windows.net/c?sv=1&sig=2",\n'
                    ' "c": "10.1.2.3"\n}\n')
        ok = [h[0] for h in hits] == [2, 3, 4] and not scan(canonical({"v": "4.21.0", "h": "0" * 64, "p": "a/b.lean:3:0"}))
        print("  %s  the scan finds a token, a signed URL and an IP address, and passes versions, digests and paths"
              % ("ok  " if ok else "FAIL"))
        fails += not ok
    finally:
        FROZEN_MODULE_BLOB = saved
        shutil.rmtree(base, ignore_errors=True)
    print("assemble self-test: %d of %d cases ok" % (n - fails, n))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--extractor", required=True)
    ap.add_argument("--extractor-repo")
    ap.add_argument("--host")
    ap.add_argument("--logs")
    ap.add_argument("--download-record")
    ap.add_argument("--src", action="append", default=[], help="runN=DIR")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    if a.self_test:
        try:
            return 1 if self_test(a.extractor, a.work) else 0
        except Unverified as e:
            print("assemble self-test: extractor refused: %s" % e)
            return 1
    if not (a.extractor_repo and a.host and a.logs and a.download_record and a.src):
        ap.error("--extractor-repo, --host, --logs, --download-record and --src are required")
    src = dict(s.split("=", 1) for s in a.src)
    try:
        ex = load_extractor(a.extractor, a.extractor_repo)
    except Unverified as e:
        print("CHECK all UNVERIFIED %s" % e)
        print("EXTRACT UNVERIFIED")
        return 2
    inputs = {"host": a.host, "logs": a.logs, "download_record": a.download_record, "src": src}
    for k in RUNS:
        inputs["src"].setdefault(k, os.path.join(os.devnull, "absent"))
    return run_all(ex, inputs)


if __name__ == "__main__":
    sys.exit(main())
