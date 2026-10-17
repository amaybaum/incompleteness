#!/usr/bin/env python3
"""Assemble one shard's expected results (AGENTS §A.42 item 1, form `derived`) from the Mathlib bridge job logs of
cited CI runs and the host's JSON records, and print them. Read-only; Python 3 stdlib.

  python3 -I assemble.py --extractor main-src/verification/audits/evidence-retention/extract_result.py \
      --extractor-repo main-src --runs batchx/runs.json --crosscheck batchx/crosscheck.json --shard K --host DIR
  python3 -I assemble.py --self-test --extractor PATH [--work DIR]

The extractor is main's extract_result.py, verified against EXTRACT_RESULT_BLOB (its blob at MAIN_COMMIT) and, with
--extractor-repo, against that checkout's HEAD and tree; the verified bytes are the ones executed. The run set is
batchx/runs.json, verified against RUNS_SHA256; shard K's runs are its entries with "shard": K, in file order.
--host holds what host.py wrote: run-<id>.json, jobs-<id>.json, logs/<job>.log and fetch-record.json.

What a result records, for every run, whatever the run's outcome: the run's identity and attempt-1 record; every
job's name and conclusion; the bridge job's steps and conclusions; how the job ended (expected.outcome); whether the
build completed, and if not, its `error:` lines, its failed targets and its error annotations; the release-gate
block, steps and verdict, when the gate ran to a verdict; the four failure markers over the Build and Release gate
sections; and, for every module with axiom reports in the log, its report count, its axiom sets and the sha256 of
its canonical report lines. What it cannot carry is named in `gaps`. The extraction judges the record, not the run:
a red run is recorded as red.

Per-run verdict, fail closed:
  HOLDS       every input present and matching its record; the log complete, of this job, at this head, in a
              known format; every step's conclusion consistent with its section of the log; the result printed.
  FAILS       the evidence is present and contradicts itself or the pinned run set: another head, a step that
              succeeded with no build line or gate verdict, a build line under a failed step, a gate verdict at odds
              with its steps, a job conclusion at odds with its steps, a credential-shaped string in the result.
  UNVERIFIED  an input is absent, unreadable or unread (expired or missing log, rate-limit reserve, malformed
              record, truncated log), the format is not recognized, a step failed without a located cause, or the
              block would pass the shard's line budget.
Shard verdict, the last line: EXTRACT SHARD K/N HOLDS (exit 0) only when the runs are exactly shard K's runs of the
pinned file, each once, each with an explicit HOLDS; FAILS (exit 1) when any run FAILS; UNVERIFIED (exit 2)
otherwise. A run's block is printed only when that run HOLDS, between
  ===== BEGIN EXPECTED RESULT ci/<run>/results.json =====
  ===== END EXPECTED RESULT ci/<run>/results.json =====
followed by `SHA256 ci/<run>/results.json <hex>`, the sha256 of the canonical text, json.dumps(obj, indent=1,
sort_keys=True) plus a newline, ASCII only. Strip the timestamp prefix from each served line and join the lines
between the markers with newlines, ending with one, to recover the file (collect.py does this and checks it).

Nothing that varies between runs of the same commit goes under `expected`: no timestamps, durations, build-job
counts, cache lines, runner paths or output order. Log line numbers, the set of modules that printed reports
(it depends on the build cache) and the synthetic merge commit of a pull-request run are kept under `observed`.
"""
import argparse
import contextlib
import copy
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
RUNS_SHA256 = "5436c5b6325e5efca8b9d9a737ba832b6556ae9ffc15524b33774f701f672edb"
CROSSCHECK_SHA256 = "5d71dd28415f60b68890da2059581d86a2204073db4fe5dd61b9fa9b3cf25890"
WORKFLOW = ".github/workflows/verify.yml"
JOB_BRIDGE = "Mathlib bridge"
STEP_BUILD, STEP_GATE = "Build", "Release gate"
HDR_BUILD = "##[group]Run lean --version"
HDR_GATE = "##[group]Run python3 tools/release_gate.py"
HEAD_LOG = "[command]/usr/bin/git log -1 --format=%H"
PERMITTED = ["propext", "Classical.choice", "Quot.sound"]
MARKER_KEYS = ("sorryAx", "Lean.ofReduceBool", "declaration uses 'sorry'", "error:")
STEP_CONCLUSIONS = ("success", "failure", "cancelled", "skipped")
LINE_BUDGET = 4200      # lines this script may print per shard; the runner adds about 300 around it
TRAILER = 4             # the run-set line, the verdict line and slack

HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEAD_NOW_PR = re.compile(r"^HEAD is now at ([0-9a-f]{7,40}) Merge ([0-9a-f]{40}) into ([0-9a-f]{40})$")
LOOSE_REPORT = re.compile(r"depends on axioms: \[|does not depend on any axioms")
LOC = re.compile(r"((?:OIBridge/)?[A-Za-z0-9_/]+\.lean):(\d+):\d+")
ERROR_LINE = re.compile(r"^error: (.*)$")
RUNNER_PATH = re.compile(r"/home/runner/work/[^\s:]*?/verification/lean-mathlib/|/tmp/[A-Za-z0-9_.-]+/")
FAILED_TARGETS = "Some required targets logged failures:"
FAILED_TARGET = re.compile(r"^- (\S+)$")

# check_retention.py's R5 pattern (main at b96662e6), with signed-URL parameters of the log storage hosts added.
SECRET = re.compile(
    r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
    r'|x-access-toke[n]|[?&](sig|signature|sv|se|sp|sr|st|skoid|sktid|skt|ske|sks|skv|token|x-amz-[a-z-]+)='
    r'|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]|private[_-]?key|https?://[^\s"]*\?'
    r'|blob\.core\.windows\.net|actions\.githubusercontent\.com'
    r'|(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.I)

BEGIN = "===== BEGIN EXPECTED RESULT %s ====="
END = "===== END EXPECTED RESULT %s ====="

GAP_UNATTESTED = ("no receipt or certificate attests this run, so it has no governed module set: expected.modules is "
                  "empty and every module's reports appear under expected.axiom_reports")
GAP_CACHE = ("which modules print axiom reports depends on the build cache: a module absent from "
             "expected.axiom_reports is not recorded, and is not recorded as having no reports")
GAP_DECLS = ("per-declaration reports are carried as each module's report count, axiom sets and the sha256 of its "
             "canonical report lines, not as a list")
GAP_GATE_SRC = "the gate's step list is not checked against tools/release_gate.py at the head"
AXIOM_FORMAT = ("<n> reports; <axiom set> x<count>; ...; sha256 <hex>. An axiom set is its axioms sorted and joined "
                "by commas, or (none) for 'does not depend on any axioms'. The digest is sha256 of the module's "
                "report lines '<source line>\\t<declaration>\\t<axioms as printed, joined by commas, or (none)>', "
                "sorted by line then name, each ending with a newline.")


class Unverified(Exception):
    pass


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def git(repo, *args):
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0")
    p = subprocess.run(["git", "-C", repo] + list(args), capture_output=True, text=True, env=env, timeout=60)
    return p.stdout.strip() if p.returncode == 0 else None


def _exec_extractor(data, path):
    mod = types.ModuleType("extract_result")
    mod.__file__ = path
    exec(compile(data, path, "exec"), mod.__dict__)  # noqa: S102 - the pinned, verified bytes
    return mod


def check_interface(mod):
    """The interface this script uses. A blob with another interface is refused, never guessed at."""
    for name in ("extract", "strip", "MARKERS", "TS"):
        if not hasattr(mod, name):
            raise Unverified("extractor lacks %s" % name)
    if tuple(mod.MARKERS) != MARKER_KEYS:
        raise Unverified("extractor markers are not the expected four")
    probe = mod.extract("info: OIBridge/A.lean:3:0: 'OIBridge.A.x' depends on axioms: [propext]\n"
                        "Build completed successfully (1 jobs).\nrelease gate\n  PASS  toolchain        ok\n"
                        "release gate: PASS\n")
    try:
        r = probe["reports"]["OIBridge/A.lean"][0]
        ok = (r["line"], r["name"], r["axioms"], r["served_line"]) == (3, "OIBridge.A.x", ["propext"], 1) \
            and probe["build"]["success"] is True and probe["gate"]["verdict"]["pass"] is True \
            and probe["gate"]["steps"][0]["name"] == "toolchain" and probe["markers"]["error:"] == 0
    except (KeyError, IndexError, TypeError):
        ok = False
    if not ok:
        raise Unverified("extractor output does not have the expected shape")
    return mod


def load_extractor(path, repo=None, pinned=True):
    """Read once, check the blob id (and, with repo, the checkout's HEAD and tree), then execute those bytes."""
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        raise Unverified("extractor unreadable: %s" % type(e).__name__)
    if pinned and git_blob_id(data) != EXTRACT_RESULT_BLOB:
        raise Unverified("extractor blob %s is not the pinned %s" % (git_blob_id(data), EXTRACT_RESULT_BLOB))
    if repo is not None:
        if git(repo, "rev-parse", "HEAD") != MAIN_COMMIT:
            raise Unverified("extractor checkout HEAD is not %s" % MAIN_COMMIT)
        if git(repo, "rev-parse", "HEAD:" + EXTRACT_RESULT_PATH) != EXTRACT_RESULT_BLOB:
            raise Unverified("extractor checkout tree does not hold the pinned blob")
    return check_interface(_exec_extractor(data, path))


def own_blob(name):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), name), "rb") as f:
        return git_blob_id(f.read())


def load_pinned(path, sha, what):
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        raise Unverified("%s unreadable: %s" % (what, type(e).__name__))
    if hashlib.sha256(data).hexdigest() != sha:
        raise Unverified("%s sha256 %s is not the pinned %s" % (what, hashlib.sha256(data).hexdigest(), sha))
    return json.loads(data)


# ------------------------------------------------------------------------------------------------ reading

class Log:
    """One job log: its bytes checked against the download record, decoded, split as extract_result splits."""

    def __init__(self, path, rec, ex):
        try:
            with open(path, "rb") as f:
                data = f.read()
        except OSError as e:
            raise Unverified("log %s unreadable: %s" % (os.path.basename(path), type(e).__name__))
        nl = data.count(b"\n") + (1 if data and not data.endswith(b"\n") else 0)
        self.sha256 = hashlib.sha256(data).hexdigest()
        if (len(data), self.sha256, nl) != (rec.get("bytes"), rec.get("sha256"), rec.get("lines")):
            raise Unverified("log %s does not match its download record" % os.path.basename(path))
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            raise Unverified("log %s is not UTF-8" % os.path.basename(path))
        self.bytes, self.lines_n = len(data), nl
        self.bom = text.startswith("﻿")
        self.cr = text.count("\r")
        whole = text.split("\n")
        if whole and whole[-1] == "":
            whole.pop()
        self.whole = whole
        body = (text[1:] if self.bom else text).replace("\r\n", "\n")
        raw = body.split("\n")
        if raw and raw[-1] == "":
            raw.pop()
        self.raw = raw
        self.s = [ex.strip(l) for l in raw]

    def tail_sha256(self, k):
        return hashlib.sha256("\n".join(self.whole[-k:]).encode("utf-8")).hexdigest()

    def find(self, header):
        return [i for i, l in enumerate(self.s) if l == header]

    def section(self, start):
        """[start, end): from a step's header to the next step header or the post-job cleanup."""
        for j in range(start + 1, len(self.s)):
            if self.s[j].startswith("##[group]Run ") or self.s[j] == "Post job cleanup.":
                return start, j
        return start, len(self.s)


class Checks:
    def __init__(self):
        self.items, self.unverified = [], []

    def __call__(self, name, ok, detail=""):
        """A check whose failure means the evidence contradicts itself: FAILS."""
        self.items.append((name, bool(ok), detail))
        return bool(ok)

    def need(self, name, ok, detail=""):
        """A check whose failure means the evidence cannot be read with confidence: UNVERIFIED."""
        if not ok:
            self.unverified.append("%s%s" % (name, (" -- " + detail) if detail else ""))
        return bool(ok)

    @property
    def failed(self):
        return [x for x in self.items if not x[1]]

    def verdict(self):
        return "FAILS" if self.failed else "UNVERIFIED" if self.unverified else "HOLDS"


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
    for k, t in fields:
        _need(k in obj, "%s lacks %s" % (where, k))
        v = obj[k]
        ts = t if isinstance(t, tuple) else (t,)
        _need(isinstance(v, ts) and not (isinstance(v, bool) and bool not in ts),
              "%s field %s is %s" % (where, k, "null" if v is None else type(v).__name__))


def check_run_record(run, rid):
    where = "run-%s.json" % rid
    _need(isinstance(run, dict), "%s is not a JSON object" % where)
    _typed(run, where, (("id", int), ("head_sha", str), ("run_attempt", int), ("event", str),
                        ("conclusion", str), ("path", str), ("created_at", str)))


def check_jobs_record(jobsd, rid):
    where = "jobs-%s.json" % rid
    _need(isinstance(jobsd, dict), "%s is not a JSON object" % where)
    _typed(jobsd, where, (("total_count", int), ("jobs", list)))
    for n, j in enumerate(jobsd["jobs"]):
        w = "%s job %d" % (where, n)
        _need(isinstance(j, dict), "%s is not a JSON object" % w)
        _typed(j, w, (("id", int), ("run_id", int), ("run_attempt", int), ("name", str), ("head_sha", str),
                      ("steps", list)))
        _need(j.get("conclusion") is None or isinstance(j.get("conclusion"), str), "%s conclusion is malformed" % w)
        for m, st in enumerate(j["steps"]):
            ws = "%s step %d" % (w, m)
            _need(isinstance(st, dict), "%s is not a JSON object" % ws)
            _typed(st, ws, (("number", int), ("name", str)))
            _need(st.get("conclusion") is None or isinstance(st.get("conclusion"), str), "%s conclusion is malformed" % ws)


def unread_reason(what, rec):
    st, status = rec.get("stage"), rec.get("http_status")
    if st == "rate-limit-reserve":
        return "%s not read: the rate-limit reserve was reached" % what
    if what == "log" and status in (404, 410):
        return "log not available (HTTP %d): expired or deleted" % status
    return "%s not read: stage %s, %s%s" % (what, st, rec.get("error_type"), (", HTTP %s" % status) if status else "")


# ------------------------------------------------------------------------------------------------ assembly

def norm_error(text):
    return RUNNER_PATH.sub("", text).rstrip()


def report_line(r):
    return "%d\t%s\t%s\n" % (r["line"], r["name"], ",".join(r["axioms"]) if r["axioms"] is not None else "(none)")


def module_summary(reps):
    sets = {}
    for r in reps:
        k = ",".join(sorted(r["axioms"])) if r["axioms"] is not None else "(none)"
        sets[k] = sets.get(k, 0) + 1
    lines = sorted((report_line(r) for r in reps), key=lambda l: (int(l.split("\t", 1)[0]), l))
    digest = hashlib.sha256("".join(lines).encode("utf-8")).hexdigest()
    return "%d reports; %s; sha256 %s" % (len(reps), "; ".join("%s x%d" % (k, sets[k]) for k in sorted(sets)), digest)


def assemble_run(cfg, ex, inputs, fetch):
    """Returns (Checks, result dict or None)."""
    C = Checks()
    rid, jid, head = cfg["run_id"], cfg["bridge_job_id"], cfg["head_sha"]
    try:
        fr = (fetch.get("runs") or {}).get(rid)
        _need(isinstance(fr, dict), "the fetch record has no entry for run %s" % rid)
        for what in ("run", "jobs", "log"):
            _need(isinstance(fr.get(what), dict), "fetch record of run %s lacks %s" % (rid, what))
            if fr[what].get("outcome") != "ok":
                raise Unverified(unread_reason(what, fr[what]))
        run = load_json(os.path.join(inputs["host"], "run-%s.json" % rid))
        check_run_record(run, rid)
        jobsd = load_json(os.path.join(inputs["host"], "jobs-%s.json" % rid))
        check_jobs_record(jobsd, rid)
        lrec = fr["log"]
        _typed(lrec, "fetch record of job %s" % jid, (("job_id", str), ("bytes", int), ("sha256", str), ("lines", int)))
        _need(lrec["job_id"] == jid, "fetch record names job %s, not %s" % (lrec["job_id"], jid))
        lg = Log(os.path.join(inputs["host"], "logs", jid + ".log"), lrec, ex)
    except Unverified as e:
        C.unverified.append(str(e))
        return C, None
    except Exception as e:  # noqa: BLE001 - any other failure while reading the inputs is an unverified run
        C.unverified.append("malformed input: %s: %s" % (type(e).__name__, str(e)[:200]))
        return C, None

    # --- identity (API) against the pinned run set
    event = run["event"]
    C("run: the pinned id, head and event; attempt 1; workflow verify.yml",
      str(run["id"]) == rid and run["head_sha"] == head and event == cfg["event"] and run["run_attempt"] == 1
      and run["path"] == WORKFLOW,
      "id=%s head=%s event=%s attempt=%s path=%s" % (run["id"], run["head_sha"][:12], event, run["run_attempt"],
                                                     run["path"]))
    jobs = jobsd["jobs"]
    C("jobs: the list is complete, each job once", jobs and len(jobs) == jobsd["total_count"]
      and len({j["id"] for j in jobs}) == len(jobs), "%d of %d" % (len(jobs), jobsd["total_count"]))
    C("jobs: every job of this run, attempt 1, at the run's head",
      all(str(j["run_id"]) == rid and j["run_attempt"] == 1 and j["head_sha"] == head for j in jobs))
    byid = {str(j["id"]): j for j in jobs}
    bj = byid.get(jid) or {}
    C("jobs: the pinned bridge job %s is %r" % (jid, JOB_BRIDGE), bj.get("name") == JOB_BRIDGE, str(bj.get("name")))
    bconc = bj.get("conclusion")
    C("jobs: the bridge job's conclusion is the pinned %s" % cfg["bridge_conclusion"], bconc == cfg["bridge_conclusion"],
      str(bconc))
    C.need("jobs: the bridge job's conclusion is success, failure or cancelled",
           bconc in ("success", "failure", "cancelled"), str(bconc))
    steps = bj.get("steps") or []
    named = {}
    for st in steps:
        named.setdefault(st["name"], []).append(st)
    sc = {}
    for nm in (STEP_BUILD, STEP_GATE):
        k = named.get(nm, [])
        C.need("format: one %r step in the bridge job" % nm, len(k) == 1, "%d found" % len(k))
        sc[nm] = k[0].get("conclusion") if len(k) == 1 else None
        C.need("format: step %r concluded %s" % (nm, "/".join(STEP_CONCLUSIONS)), sc[nm] in STEP_CONCLUSIONS, str(sc[nm]))
    concl = [st.get("conclusion") for st in steps]
    if bconc == "success":
        C("job: success, and no step failed or was cancelled", not any(c in ("failure", "cancelled") for c in concl))
    elif bconc == "failure":
        C("job: failure, and a step failed", any(c == "failure" for c in concl))

    # --- the log: complete, of this job, at this head
    C.need("log: complete (runner header on line 1, orphan cleanup at the end)",
           lg.s and lg.s[0].startswith("Current runner version: ")
           and any(l == "Cleaning up orphan processes" for l in lg.s[-12:]),
           "line 1: %r" % (lg.s[0][:60] if lg.s else ""))
    C.need("log: one job name line", lg.s.count("Complete job name: " + JOB_BRIDGE) == 1)
    k = [i for i, l in enumerate(lg.s) if l == HEAD_LOG]
    logged = lg.s[k[0] + 1] if len(k) == 1 and k[0] + 1 < len(lg.s) else None
    C.need("log: one checked-out commit line", logged is not None and HEX40.match(logged), "%d found" % len(k))
    checkout, merge = {"ref": "the run's head"}, None
    if logged is not None and HEX40.match(logged):
        if event == "pull_request":
            pm = [HEAD_NOW_PR.match(l) for l in lg.s]
            pm = [m for m in pm if m]
            if C.need("format: one synthetic-merge checkout line of a pull-request run", len(pm) == 1, "%d found" % len(pm)):
                m = pm[0]
                C("head: the synthetic merge checked out merges the run's head", m.group(2) == head
                  and logged.startswith(m.group(1)), "merge of %s into %s" % (m.group(2)[:12], m.group(3)[:12]))
                checkout = {"synthetic_merge_of": head, "base": m.group(3)}
                merge = logged
        else:
            C("head: the checked-out commit is the run's head", logged == head, logged[:12])

    # --- sections, each found on its own
    hb, hg = lg.find(HDR_BUILD), lg.find(HDR_GATE)
    sec = {}
    for nm, h in ((STEP_BUILD, hb), (STEP_GATE, hg)):
        c = sc.get(nm)
        if c in ("success", "failure"):
            C.need("format: one %s section for a step that ran" % nm, len(h) == 1, "%d found" % len(h))
        elif c == "skipped":
            C("log: no %s section for a skipped step" % nm, not h, "%d found" % len(h))
        elif c == "cancelled":
            C.need("format: at most one %s section" % nm, len(h) <= 1, "%d found" % len(h))
        if len(h) == 1:
            sec[nm] = lg.section(h[0])
    if STEP_BUILD in sec and STEP_GATE in sec:
        C("log: the Build section before the Release gate section", sec[STEP_BUILD][1] <= sec[STEP_GATE][0])
    b0, b1 = sec.get(STEP_BUILD, (0, 0))
    g0, g1 = sec.get(STEP_GATE, (0, 0))
    empty = {"build": None, "gate": None, "reports": {}, "markers": {k_: 0 for k_ in MARKER_KEYS}}
    bx = ex.extract("\n".join(lg.raw[b0:b1])) if STEP_BUILD in sec else empty
    gx = ex.extract("\n".join(lg.raw[g0:g1])) if STEP_GATE in sec else empty
    if any(r.get("unclosed") for x in (bx, gx) for reps in (x.get("reports") or {}).values() for r in reps):
        C.need("reports: every axiom list closes", False, "an unclosed list makes the section's reading unreliable")
        return C, None

    # --- build
    bline = bx.get("build")
    built = bool(bline and bline.get("success"))
    errors = sorted({norm_error(m.group(0)) for l in lg.s[b0:b1] for m in [ERROR_LINE.match(l)] if m})
    targets, annot = [], {}
    for i in range(b0, b1):
        if lg.s[i] == FAILED_TARGETS:
            j = i + 1
            while j < b1 and FAILED_TARGET.match(lg.s[j]):
                targets.append(FAILED_TARGET.match(lg.s[j]).group(1))
                j += 1
    for nm, (a, b) in sec.items():
        annot[nm] = sorted({lg.s[i] for i in range(a, b) if lg.s[i].startswith("##[error]")})
    cb = sc.get(STEP_BUILD)
    if cb in ("success", "failure") and STEP_BUILD not in sec:
        pass                                   # the format check above names the missing section: UNVERIFIED
    elif cb == "success":
        C("build: a 'Build completed successfully' line under a successful Build step", built)
    elif cb == "failure":
        C("build: no 'Build completed successfully' line under a failed Build step", not built)
        C.need("build: the failed Build step's cause is located (an error: line or an error annotation)",
               errors or annot.get(STEP_BUILD))
    elif cb == "skipped":
        C("build: no build line for a skipped Build step", not built)

    # --- gate
    gate = gx.get("gate")
    gv = (gate or {}).get("verdict")
    cg = sc.get(STEP_GATE)
    if cg in ("success", "failure") and STEP_GATE not in sec:
        cg = "unread"                          # the format check above names the missing section: UNVERIFIED
    if gate is not None:
        names = [s_["name"] for s_ in gate.get("steps") or []]
        C("gate: at least one step line, each step once", names and len(set(names)) == len(names),
          "%d steps, %d distinct" % (len(names), len(set(names))))
        if gv:
            nfail = sum(1 for s_ in gate["steps"] if s_["status"] == "FAIL")
            C("gate: a PASS verdict has no FAIL step and a failed verdict has one", bool(gv["pass"]) == (nfail == 0),
              "verdict %r, %d FAIL" % (gv["text"][:40], nfail))
    if cg == "success":
        C("gate: a PASS verdict under a successful Release gate step", gv and gv["pass"],
          "no verdict" if not gv else gv["text"][:60])
    elif cg == "failure":
        if gv:
            C("gate: no PASS verdict under a failed Release gate step", not gv["pass"])
        else:
            C.need("gate: the failed Release gate step printed a verdict", False, "no verdict line")
    elif cg == "skipped":
        C("gate: no gate block for a skipped Release gate step", gate is None)

    # --- outcome
    if bconc == "cancelled" and not gv:
        outcome = "cancelled"
    elif cb == "failure":
        outcome = "build-failed"
    elif cb == "skipped":
        outcome = "not-built"
    elif cb == "success" and gv:
        outcome = "gate-verdict"
    elif cb == "success" and cg == "skipped":
        outcome = "gate-not-run"
    else:
        outcome = None
    C.need("outcome: recognized", outcome is not None, "build %s, gate %s, job %s" % (cb, cg, bconc))

    # --- axiom reports
    reports = bx.get("reports") or {}
    parsed = {r["served_line"] for reps in reports.values() for r in reps}
    loose = [i for i in range(b0, b1) if LOOSE_REPORT.search(lg.s[i])]
    unparsed = []
    for i in loose:
        if i - b0 + 1 not in parsed:
            m = LOC.search(lg.s[i])
            unparsed.append("%s:%s" % (m.group(1), m.group(2)) if m else "unlocated")
    unparsed.sort()
    C("reports: every parsed report line is a report line", len(parsed) <= len(loose) and parsed <= {i - b0 + 1 for i in loose})
    axiom_reports, outside = {}, []
    for mod in sorted(reports):
        reps = reports[mod]
        axiom_reports[mod] = module_summary(reps)
        for r in reps:
            if r["axioms"] is not None and not set(r["axioms"]) <= set(PERMITTED):
                outside.append("%s:%d %s [%s]" % (mod, r["line"], r["name"], ", ".join(r["axioms"])))
    markers = {k_: (bx.get("markers") or {}).get(k_, 0) + (gx.get("markers") or {}).get(k_, 0) for k_ in MARKER_KEYS}

    if C.failed or C.unverified:
        return C, None

    gaps = [GAP_UNATTESTED, GAP_CACHE, GAP_DECLS]
    if gate is not None:
        gaps.append(GAP_GATE_SRC)
    if outcome != "gate-verdict":
        gaps.append("the job ended before the gate's verdict (%s): the result records no gate verdict" % outcome
                    if gv is None else "the job's outcome is %s" % outcome)
    if unparsed:
        gaps.append("%d axiom-report lines that the pinned extract_result.py does not parse, so their reports are "
                    "not recorded: %s" % (len(unparsed), ", ".join(unparsed)))
    gaps.sort()
    expected = {
        "outcome": outcome,
        "build_success": built,
        "build_errors": errors,
        "failed_targets": sorted(set(targets)),
        "error_annotations": annot,
        "gate": None if not gv else {
            "steps": [{"name": s_["name"], "status": s_["status"], "summary": s_["summary"]} for s_ in gate["steps"]],
            "steps_pass": sum(1 for s_ in gate["steps"] if s_["status"] == "PASS"),
            "steps_total": len(gate["steps"]), "verdict": gv["text"]},
        "markers": markers,
        "modules": {},
        "permitted_axioms": PERMITTED,
        "axiom_reports": axiom_reports,
        "axiom_reports_format": AXIOM_FORMAT,
        "outside_permitted": sorted(outside),
    }
    result = {
        "schema": "oi-evidence-result", "version": 1, "kind": "cited-bridge", "form": "derived",
        "commit": head,
        "run": {"id": rid, "head_sha": head, "event": event, "attempt": run["run_attempt"],
                "conclusion": run["conclusion"], "workflow": os.path.basename(run["path"]), "job_id": jid,
                "job_name": JOB_BRIDGE, "job_conclusion": bconc},
        "checkout": checkout,
        "jobs": {"total": len(jobs), "conclusions": sorted("%s: %s" % (j["name"], j.get("conclusion")) for j in jobs)},
        "bridge_steps": ["%d %s: %s" % (st["number"], st["name"], st.get("conclusion")) for st in steps],
        "expected": expected,
        "gaps": gaps,
        "observed": {
            "note": "1-based lines of the job log named in source.log, after the byte-order mark; provenance of this "
                    "log, not compared",
            "build_line": (b0 + bline["line"]) if built else None,
            "gate_lines": {"start": g0 + gate["start_line"], "verdict": g0 + gv["served_line"]} if gv else None,
            "sections": {nm: [a + 1, b] for nm, (a, b) in sorted(sec.items())},
            "modules_with_reports": len(reports),
            "reports_parsed": len(parsed),
            "report_lines_seen": len(loose),
            "synthetic_merge": merge,
        },
        "source": {
            "extractor": EXTRACT_RESULT_PATH, "extractor_blob": EXTRACT_RESULT_BLOB, "extractor_commit": MAIN_COMMIT,
            "assembler": "batchx/assemble.py", "assembler_blob": own_blob("assemble.py"),
            "host_reader": "batchx/host.py", "host_reader_blob": own_blob("host.py"),
            "kind": "a GitHub Actions job log, downloaded in full from the jobs/<id>/logs endpoint by a read-only "
                    "workflow, with the run (attempt 1) and job records from the Actions runs and jobs API",
            "note": "the digest identifies the bytes this result was read from: provenance of the extraction, not "
                    "independent proof of the result, which reproduction at the commit supplies",
            "log": {"job_id": jid, "bytes": lg.bytes, "lines": lg.lines_n, "byte_order_mark": lg.bom,
                    "carriage_returns": lg.cr},
            "source_sha256": lg.sha256,
        },
        "reproduce": {
            "compared": "for outcome gate-verdict, compare_result.py compares build success, the gate's steps and "
                        "verdict and the markers (expected.modules is empty); by reading, each module of "
                        "expected.axiom_reports must reproduce with the same count, axiom sets and sha256 from a "
                        "build at the commit; for build-failed, the build must fail with expected.build_errors and "
                        "expected.failed_targets",
            "not_compared": "timestamps, durations, cache behaviour, build-job counts, output order, log lines, which "
                            "modules printed reports",
            "recipe": [
                "run from the root of a full-history clone at a commit that carries "
                "verification/audits/evidence-retention (the verifier), with the object %s available; <dir> is a new "
                "directory and <log> a file outside it" % head,
                ("git worktree add --detach <dir> %s" % head) if event != "pull_request" else
                ("git worktree add --detach <dir> %s, then in <dir> git merge --no-ff --no-edit %s (GitHub's "
                 "synthetic merge, rebuilt under a new id)" % (checkout.get("base"), head)),
                "rm -rf <dir>/verification/lean-mathlib/.lake/build, so that every module prints its reports",
                "(cd <dir>/verification/lean-mathlib && lean --version && lake exe cache get && lake --rehash build) "
                "> <log> 2>&1",
                "(cd <dir> && python3 tools/release_gate.py) >> <log> 2>&1",
                "python3 -I verification/audits/evidence-retention/extract_result.py <log> > reproduced.json",
                "for outcome gate-verdict: python3 -I verification/audits/evidence-retention/compare_result.py "
                "<this file> reproduced.json --tree <dir>",
                "for each module of expected.axiom_reports: its reports in reproduced.json, summarized as "
                "expected.axiom_reports_format states, equal the recorded line",
            ],
        },
    }
    return C, result


# ------------------------------------------------------------------------------------------------ the shard

def runset_digest(ids):
    return hashlib.sha256(("\n".join(sorted(ids)) + "\n").encode()).hexdigest()


def run_set_problem(verdicts, runs, expected_ids):
    """None when the runs are exactly the expected ids, each once, each with a verdict; else why not."""
    if not isinstance(runs, list) or not isinstance(verdicts, dict) or not runs or not expected_ids:
        return "no runs"
    ids = [str(c.get("run_id")) if isinstance(c, dict) else None for c in runs]
    dup = sorted({i for i in ids if ids.count(i) > 1}, key=str)
    if dup:
        return "run %s appears more than once" % ", ".join(map(str, dup))
    missing = [i for i in expected_ids if i not in ids]
    extra = [i for i in ids if i not in expected_ids]
    if missing or extra:
        return "runs missing %s, unexpected %s" % (missing, extra)
    if set(verdicts) != set(ids):
        return "verdicts for %s, runs %s" % (sorted(verdicts), sorted(ids))
    return None


def overall(verdicts, runs, expected_ids):
    """HOLDS only when the runs are exactly the expected ids, each once, each with an explicit HOLDS."""
    if run_set_problem(verdicts, runs, expected_ids) is not None:
        return "UNVERIFIED"
    vs = [verdicts.get(str(c["run_id"])) for c in runs]
    if any(v == "FAILS" for v in vs):
        return "FAILS"
    return "HOLDS" if all(v == "HOLDS" for v in vs) else "UNVERIFIED"


def canonical(obj):
    return json.dumps(obj, indent=1, sort_keys=True) + "\n"


def scan(text):
    return [(n + 1, m.group(0)[:6] + "...") for n, l in enumerate(text.split("\n")) for m in [SECRET.search(l)] if m]


def redact(s):
    return SECRET.sub("<redacted>", s)


def crosscheck_lines(cfg, inputs, fetch, ex, xc):
    jid = cfg["bridge_job_id"]
    obs = (xc.get("jobs") or {}).get(jid)
    if not obs:
        return ["CROSSCHECK job %s not observed in session" % jid]
    try:
        lg = Log(os.path.join(inputs["host"], "logs", jid + ".log"), fetch["runs"][cfg["run_id"]]["log"], ex)
    except Exception as e:  # noqa: BLE001 - the cross-check is never decisive
        return ["CROSSCHECK job %s unavailable: %s" % (jid, redact(str(e))[:160])]
    same = lg.tail_sha256(obs["tail_lines"]) == obs["tail_sha256"]
    return ["CROSSCHECK job %s lines=%d session_original_length=%d %s; last %d lines %s the session's served text"
            % (jid, lg.lines_n, obs["original_length"], "equal" if lg.lines_n == obs["original_length"] else "DIFFERS",
               obs["tail_lines"], "equal to" if same else "DIFFER FROM")]


def assemble_shard(ex, doc, shard, inputs, xc, out=None, budget=LINE_BUDGET, runs=None, expected_ids=None):
    """Prints the shard's lines, ending with its verdict line; returns the exit code."""
    out = out or sys.stdout
    printed = [0]

    def P(s=""):
        out.write(s + "\n")
        printed[0] += s.count("\n") + 1
    nsh = doc.get("shards")
    exp = [r for r in doc["runs"] if r["shard"] == shard]
    expected_ids = [r["run_id"] for r in exp] if expected_ids is None else expected_ids
    runs = exp if runs is None else runs
    P("BATCH ci-batch-extract shard %d/%s: assembler %s, host reader %s, extract_result %s at %s"
      % (shard, nsh, own_blob("assemble.py")[:12], own_blob("host.py")[:12], EXTRACT_RESULT_BLOB[:12], MAIN_COMMIT[:12]))
    P("BATCH SHARD %d/%s RUNSET %s RUNS %d" % (shard, nsh, runset_digest(expected_ids), len(expected_ids)))
    try:
        fetch = load_json(inputs["fetch_record"])
        _need(isinstance(fetch, dict) and isinstance(fetch.get("runs"), dict) and fetch.get("shard") == shard,
              "the fetch record is not shard %d's" % shard)
    except Unverified as e:
        fetch = {"runs": {}}
        P("CHECK all UNVERIFIED %s" % redact(str(e)))
    for cfg in runs:
        for l in crosscheck_lines(cfg, inputs, fetch, ex, xc):
            P(l)
    verdicts, texts, checks = {}, {}, {}
    for cfg in runs:
        rid = str(cfg.get("run_id"))
        try:
            C, res = assemble_run(cfg, ex, inputs, fetch)
            if res is not None:
                text = canonical(res)
                hits = scan(text)
                C("output: credential, signed-URL, IP and e-mail scan of the result", not hits, str(hits[:3]))
                if not hits and text.isascii():
                    texts[rid] = (text, res["expected"]["outcome"])
                C("output: ASCII only", text.isascii())
        except Exception as e:  # noqa: BLE001 - a run whose assembly stopped is unverified, never held
            C = Checks()
            C.unverified.append("assembly stopped: %s: %s" % (type(e).__name__, str(e)[:200]))
        checks[rid] = C
    # the line budget: blocks in file order while they fit, after every CHECK and RESULT line is counted
    fixed = printed[0] + TRAILER + 1
    for rid, C in checks.items():
        fixed += len(C.failed) + len(C.unverified) + 1
    used = 0
    for cfg in runs:
        rid = str(cfg.get("run_id"))
        C = checks[rid]
        if rid in texts and C.verdict() == "HOLDS":
            n = texts[rid][0].count("\n") + 3
            if fixed + used + n + 1 > budget:
                C.need("output budget", False, "a block of %d lines would pass the shard's %d" % (n, budget))
                fixed += 1
            else:
                used += n
    for cfg in runs:
        rid = str(cfg.get("run_id"))
        C = checks[rid]
        for name, ok, detail in C.items:
            if not ok:
                P("CHECK %s FAIL %s%s" % (rid, name, (" -- " + redact(detail)) if detail else ""))
        for u in C.unverified:
            P("CHECK %s UNVERIFIED %s" % (rid, redact(u)))
        verdicts[rid] = C.verdict()
        kind = texts[rid][1] if rid in texts and verdicts[rid] == "HOLDS" else "-"
        P("RESULT %s %s %s (%d checks, %d failed, %d unverified)"
          % (rid, verdicts[rid], kind, len(C.items), len(C.failed), len(C.unverified)))
    for cfg in runs:
        rid = str(cfg.get("run_id"))
        if rid in texts and verdicts[rid] == "HOLDS":
            path = "ci/%s/results.json" % rid
            P(BEGIN % path)
            out.write(texts[rid][0])
            printed[0] += texts[rid][0].count("\n")
            P(END % path)
            P("SHA256 %s %s" % (path, hashlib.sha256(texts[rid][0].encode("ascii")).hexdigest()))
    problem = run_set_problem(verdicts, runs, expected_ids)
    if problem is not None:
        P("CHECK all UNVERIFIED the run set: %s" % problem)
    v = overall(verdicts, runs, expected_ids)
    P("EXTRACT SHARD %d/%s %s" % (shard, nsh, v))
    return {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[v]


def run_all(ex, doc, shard, inputs, xc, out=None, **kw):
    out = out or sys.stdout
    try:
        return assemble_shard(ex, doc, shard, inputs, xc, out, **kw)
    except Exception as e:  # noqa: BLE001
        print("CHECK all UNVERIFIED stopped: %s: %s" % (type(e).__name__, redact(str(e))[:200]), file=out)
        print("EXTRACT SHARD %d/%s UNVERIFIED" % (shard, doc.get("shards") if isinstance(doc, dict) else "?"), file=out)
        return 2


# ------------------------------------------------------------------------------------------------ self-test

def _ts(i):
    return "2026-10-17T15:%02d:%02d.%07dZ " % (i // 3600 % 60, i // 60 % 60, i * 7919 % 10000000)


GATE_FIXTURE = ["toolchain", "staleness", "voice", "claims", "lean-axioms", "lean-manuscript", "v3-receipts"]
STEPS_FIXTURE = ["Set up job", "Run actions/checkout@v4", "Install elan", "Restore the OIBridge build cache",
                 STEP_BUILD, STEP_GATE, "Post Restore the OIBridge build cache", "Post Run actions/checkout@v4",
                 "Complete job"]


def _bridge_lines(cfg, variant=0, mut=None):
    """Stripped lines of a synthetic bridge log. variant changes only run-varying content; mut injects defects."""
    mut = mut or {}
    head = cfg["head_sha"]
    L = ["Current runner version: '2.337.0'", "Runner Image Provisioner", "Worker ID: {%d}" % variant]
    if not mut.get("drop_job_name"):
        L.append("Complete job name: " + mut.get("job_name", JOB_BRIDGE))
    L += ["##[group]Run actions/checkout@v4", "with:", "  fetch-depth: 0", "##[endgroup]",
          "Syncing repository: amaybaum/incompleteness"]
    if cfg["event"] == "pull_request":
        merge = mut.get("merge_sha", "%040x" % (0xabc + variant))
        if not mut.get("drop_merge_line"):
            L.append("HEAD is now at %s Merge %s into %s" % (merge[:7], mut.get("merge_of", head), "e" * 40))
        L += [HEAD_LOG, merge]
    else:
        L.append("HEAD is now at %s a commit subject" % head[:7])
        L += [HEAD_LOG, mut.get("head", head)]
    L += ["##[group]Run curl -sSfL https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh \\",
          "\x1b[36;1mcurl -sSfL ...\x1b[0m", "##[endgroup]", "info: downloading installer",
          "##[group]Run actions/cache@v4", "##[endgroup]"]
    if variant:
        L.append("Cache restored from key: oibridge-Linux-%064x" % variant)
    else:
        L.append("Cache not found for input keys: oibridge-Linux-abc")
    if mut.get("build_section", True):
        L += [mut.get("hdr_build", HDR_BUILD), "\x1b[36;1mlean --version\x1b[0m", "shell: /usr/bin/bash -e {0}",
              "##[endgroup]", "Lean (version 4.21.0, x86_64-unknown-linux-gnu, Release)",
              "✔ [%d/3611] Built OIBridge.A (%d.%ds)" % (3600 - variant, 6 + variant, variant),
              "warning: OIBridge/A.lean:12:6: Variable name `x` is not explicitly referenced.", ""]
        L += ["info: OIBridge/A.lean:%d:0: 'OIBridge.A.t%d' depends on axioms: [propext, Classical.choice, Quot.sound]"
              % (20 + 3 * i, i) for i in range(3)]
        L += ["info: OIBridge/A.lean:40:0: 'OIBridge.A.w' depends on axioms: [propext,", "  Classical.choice,",
              "  Quot.sound]"]
        L += ["info: OIBridge/B.lean:7:0: 'OIBridge.B.u' depends on axioms: [%s]" % mut.get("b_axioms", "propext"),
              "info: OIBridge/B.lean:9:0: 'OIBridge.B.v' does not depend on any axioms",
              "info: OIBridge.lean:837:0: 'OIBridge.LinkJoin.act_op' depends on axioms: [propext, Classical.choice, "
              "Quot.sound]"]
        if mut.get("primed"):
            L.append("info: OIBridge/C.lean:5:0: 'OIBridge.C.foo'' depends on axioms: [propext]")
        if mut.get("unclosed"):
            L.append("info: OIBridge/C.lean:8:0: 'OIBridge.C.bar' depends on axioms: [propext,")
        L += mut.get("build_extra", [])
        if mut.get("build_fail"):
            L += ["error: /home/runner/work/incompleteness/incompleteness/verification/lean-mathlib/OIBridge/"
                  "ProductStratum.lean:37:61: Application type mismatch", "error: Lean exited with code 1",
                  "Some required targets logged failures:", "- OIBridge.ProductStratum", "error: build failed",
                  "##[error]Process completed with exit code 1."]
        elif mut.get("build_fail_silent"):
            L += ["something went wrong"]
        elif not mut.get("drop_build_line"):
            L.append("Build completed successfully (%d jobs)." % (3611 + variant))
        L += ["TIMING lake-exe-cache-get %ds" % (86 + variant), "TIMING lake-rehash-build %ds" % (23 + variant)]
    if mut.get("gate_section", True):
        L += [HDR_GATE, "\x1b[36;1mpython3 tools/release_gate.py\x1b[0m", "shell: /usr/bin/bash -e {0}", "##[endgroup]"]
        if mut.get("gate_block", True):
            L += ["release gate", "=" * 20]
            steps = list(GATE_FIXTURE) + mut.get("gate_extra_steps", [])
            for x in steps:
                st = mut.get("gate_fail_step") == x and "FAIL" or "PASS"
                summ = "lean_axiom_check: OK (5967 named result(s) reported, no sorr" if x == "lean-axioms" else \
                    "%s_check: OK (fixture)%s" % (x, mut.get("gate_summary_extra", "") if x == "claims" else "")
                L.append("  %s  %-16s %s" % (st, x, summ))
            L.append("=" * 20)
            if mut.get("gate_verdict"):
                L.append("release gate: %s" % mut["gate_verdict"])
            elif mut.get("gate_fail_step"):
                L += ["release gate: FAILED -> %s" % mut["gate_fail_step"], "(rerun the individual check for file/line "
                      "detail)", "##[error]Process completed with exit code 1."]
            else:
                L.append("release gate: PASS  (note: --label bNNN not given, so the baseline check ran in relative "
                         "mode only)")
        if mut.get("cancel"):
            L.append("##[error]The operation was canceled.")
    L += ["Post job cleanup.", "[command]/usr/bin/tar --posix -cf cache.tzst", "Cache saved with key: oibridge-Linux-%d"
          % variant, "Post job cleanup.", "[command]/usr/bin/git version", "Cleaning up orphan processes",
          "##[warning]Node.js 20 is deprecated."]
    if mut.get("truncate"):
        L = L[mut["truncate"]:]
    if mut.get("drop_tail"):
        L = L[:-mut["drop_tail"]]
    return L


FIXTURE_RUNS = [
    {"run_id": "901", "bridge_job_id": "9101", "head_sha": "1" * 40, "event": "workflow_dispatch", "shard": 1,
     "bridge_conclusion": "success", "expires": "2026-12-21"},
    {"run_id": "902", "bridge_job_id": "9102", "head_sha": "2" * 40, "event": "pull_request", "shard": 1,
     "bridge_conclusion": "success", "expires": "2026-12-22"},
    {"run_id": "903", "bridge_job_id": "9103", "head_sha": "3" * 40, "event": "workflow_dispatch", "shard": 1,
     "bridge_conclusion": "failure", "expires": "2026-12-22"},
    {"run_id": "904", "bridge_job_id": "9104", "head_sha": "4" * 40, "event": "push", "shard": 2,
     "bridge_conclusion": "success", "expires": "2026-12-23"},
]
# 903 is a build failure by default.
DEFAULT_MUT = {"903": {"build_fail": True, "gate_section": False}}


def _fixture(base, variant=0, mut=None, runs=FIXTURE_RUNS):
    """A complete synthetic input set for shard 1 under base. Returns (inputs, doc, xc)."""
    mut = dict(mut or {})
    os.makedirs(os.path.join(base, "host", "logs"))
    host = os.path.join(base, "host")
    fetch = {"shard": 1, "runs": {}}
    runs = copy.deepcopy(runs)
    for r in runs:
        r.update(mut.get("cfg", {}).get(r["run_id"], {}))
    xc = {"jobs": {}}
    for cfg in runs:
        if cfg["shard"] != 1:
            continue
        rid, jid = cfg["run_id"], cfg["bridge_job_id"]
        mk = dict(DEFAULT_MUT.get(rid, {}), **mut.get(rid, {}))
        bconc = mk.get("job_conclusion", cfg["bridge_conclusion"])
        sconc = {STEP_BUILD: "failure" if mk.get("build_fail") or mk.get("build_fail_silent") else "success",
                 STEP_GATE: "skipped" if not mk.get("gate_section", True) else
                 "failure" if mk.get("gate_fail_step") else "success"}
        if mk.get("cancel"):
            sconc[STEP_GATE] = "cancelled"
        sconc.update(mk.get("step_conclusions", {}))
        steps = [{"number": i + 1, "name": s, "conclusion": sconc.get(s, "success")} for i, s in enumerate(STEPS_FIXTURE)]
        run = {"id": int(rid), "head_sha": cfg["head_sha"], "run_attempt": mk.get("attempt", 1), "event": cfg["event"],
               "conclusion": mk.get("run_conclusion", bconc), "path": WORKFLOW, "created_at": "2026-09-22T10:00:00Z"}
        jobs = [{"id": int(jid), "run_id": int(rid), "run_attempt": 1, "name": JOB_BRIDGE, "conclusion": bconc,
                 "head_sha": cfg["head_sha"], "steps": steps},
                {"id": int(jid) + 50, "run_id": int(rid), "run_attempt": 1, "name": "Lean kernel check",
                 "conclusion": "success", "head_sha": cfg["head_sha"], "steps": []}]
        jobsd = {"total_count": len(jobs), "jobs": jobs, "pages": 1}
        for e in mk.get("run_edits", []):
            e(run)
        for e in mk.get("jobs_edits", []):
            e(jobsd)
        with open(os.path.join(host, "run-%s.json" % rid), "wb") as f:
            raw = json.dumps(run).encode()
            f.write(mk["run_raw"](raw) if "run_raw" in mk else raw)
        if not mk.get("drop_jobs"):
            with open(os.path.join(host, "jobs-%s.json" % rid), "w") as f:
                json.dump(jobsd, f)
        lines = _bridge_lines(cfg, variant, mk)
        text = "﻿" + "\n".join(_ts(i + 1000 * variant) + l for i, l in enumerate(lines)) + "\n"
        data = text.encode("utf-8")
        lrec = {"job_id": jid, "outcome": "ok", "stage": "done", "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                "lines": data.count(b"\n"), "http_status": 200}
        if not mk.get("drop_log"):
            with open(os.path.join(host, "logs", jid + ".log"), "wb") as f:
                f.write(data)
        ok = {"outcome": "ok", "stage": "done", "http_status": 200}
        fetch["runs"][rid] = {"run": dict(ok), "jobs": dict(ok), "log": lrec}
        for e in mk.get("fetch_edits", []):
            e(fetch["runs"][rid])
        whole = text.split("\n")[:-1]
        xc["jobs"][jid] = {"original_length": len(whole), "tail_lines": 5,
                           "tail_sha256": hashlib.sha256("\n".join(whole[-5:]).encode()).hexdigest()}
    for e in mut.get("fetch_top_edits", []):
        e(fetch)
    fr = os.path.join(base, "fetch-record.json")
    with open(fr, "w") as f:
        json.dump(fetch, f)
    return {"host": host, "fetch_record": fr}, {"shards": 2, "runs": runs}, xc


def _blocks(text):
    return re.findall(r"===== BEGIN EXPECTED RESULT ci/(\d+)/results.json =====\n(.*?)===== END", text, re.S)


def self_test(extractor_path, work=None, pinned=True):
    base = tempfile.mkdtemp(prefix="assemble-selftest-", dir=work)
    fails, n = 0, 0
    try:
        ex = load_extractor(extractor_path, pinned=pinned)
        print("assemble self-test (synthetic fixtures, no network):")

        def run_case(name, mut, want_shard, want_runs=None, needle=None, variant=0, budget=LINE_BUDGET, kw=None):
            nonlocal fails, n
            n += 1
            d = os.path.join(base, "c%03d" % n)
            inputs, doc, xc = _fixture(d, variant, mut)
            kw = dict(kw or {})
            if "runs_edit" in kw:
                kw["runs"] = kw.pop("runs_edit")([r for r in doc["runs"] if r["shard"] == 1])
            buf = io.StringIO()
            code = run_all(ex, doc, 1, inputs, xc, out=buf, budget=budget, **kw)
            text = buf.getvalue()
            last = text.rstrip("\n").split("\n")[-1]
            ok = last == "EXTRACT SHARD 1/2 " + want_shard and code == {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[want_shard]
            for rid, v in (want_runs or {}).items():
                ok = ok and re.search(r"^RESULT %s %s " % (rid, v), text, re.M) is not None
            ok = ok and (needle is None or needle in text)
            got = {b[0] for b in _blocks(text)}
            holds = set(re.findall(r"^RESULT (\d+) HOLDS ", text, re.M))
            ok = ok and got == holds          # a block exactly for each run that holds
            print("  %s  %s -> %s" % ("ok  " if ok else "FAIL", name, last))
            if not ok:
                fails += 1
                print("\n".join("        | " + l for l in text.split("\n") if re.match(r"^(CHECK|RESULT|EXTRACT)", l)))
            return text

        H3 = {"901": "HOLDS", "902": "HOLDS", "903": "HOLDS"}
        t0 = run_case("clean shard: a green dispatch run, a green pull-request run and a red build all hold", {},
                      "HOLDS", H3)
        t1 = run_case("the same evidence with other timestamps, cache lines, durations and job counts holds", {},
                      "HOLDS", H3, variant=3)
        b0, b1 = dict(_blocks(t0)), dict(_blocks(t1))

        def chk(name, cond):
            nonlocal fails, n
            n += 1
            print("  %s  %s" % ("ok  " if cond else "FAIL", name))
            fails += not cond
        chk("the expected sections, gaps and checkouts are identical across the two variants",
            set(b0) == set(b1) == {"901", "902", "903"} and all(
                json.loads(b0[k])["expected"] == json.loads(b1[k])["expected"]
                and json.loads(b0[k])["gaps"] == json.loads(b1[k])["gaps"]
                and json.loads(b0[k])["checkout"] == json.loads(b1[k])["checkout"] for k in b0))
        chk("each block is canonical ASCII JSON and its SHA256 line matches",
            all(x == canonical(json.loads(x)) and x.isascii() and
                ("SHA256 ci/%s/results.json %s" % (k, hashlib.sha256(x.encode()).hexdigest())) in t0 for k, x in b0.items()))
        allb = "".join(b0.values())
        chk("no timestamp, runner path, cache line, duration or build-job count in a result",
            "2026-10-17T" not in allb and "/home/runner" not in allb and "Cache" not in allb
            and "(3611 jobs)" not in allb and "TIMING" not in allb)
        r1, r2, r3 = (json.loads(b0[k]) for k in ("901", "902", "903"))
        chk("a green run records its gate, every step PASS, outcome gate-verdict, the markers and the module digests",
            r1["expected"]["outcome"] == "gate-verdict" and r1["expected"]["gate"]["steps_total"] == len(GATE_FIXTURE)
            and r1["expected"]["build_success"] is True and r1["expected"]["markers"]["error:"] == 0
            and sorted(r1["expected"]["axiom_reports"]) == ["OIBridge.lean", "OIBridge/A.lean", "OIBridge/B.lean"]
            and r1["expected"]["axiom_reports"]["OIBridge/A.lean"].startswith("4 reports; Classical.choice,Quot.sound,propext x4; sha256 "))
        chk("a report without axioms and a non-standard set are summarized, a wrapped list joined",
            r1["expected"]["axiom_reports"]["OIBridge/B.lean"].startswith("2 reports; (none) x1; propext x1; sha256 ")
            and r1["expected"]["outside_permitted"] == [])
        chk("a pull-request run records the merge's base, its head, and the synthetic merge under observed",
            r2["checkout"] == {"synthetic_merge_of": "2" * 40, "base": "e" * 40}
            and r2["observed"]["synthetic_merge"] == "%040x" % 0xabc and "git merge --no-ff" in r2["reproduce"]["recipe"][1])
        chk("a red build records outcome build-failed, its errors without runner paths, its failed target, no gate",
            r3["expected"]["outcome"] == "build-failed" and r3["expected"]["build_success"] is False
            and r3["expected"]["build_errors"] == ["error: Lean exited with code 1", "error: OIBridge/ProductStratum.lean:37:61: "
                                                   "Application type mismatch", "error: build failed"]
            and r3["expected"]["failed_targets"] == ["OIBridge.ProductStratum"] and r3["expected"]["gate"] is None
            and r3["expected"]["error_annotations"]["Build"] == ["##[error]Process completed with exit code 1."]
            and any("ended before the gate's verdict (build-failed)" in g for g in r3["gaps"]))
        chk("the module digest is sha256 of the canonical report lines",
            r1["expected"]["axiom_reports"]["OIBridge/B.lean"].endswith(hashlib.sha256(
                b"7\tOIBridge.B.u\tpropext\n9\tOIBridge.B.v\t(none)\n").hexdigest()))
        chk("CROSSCHECK lines say equal for logs matching the session's observation",
            t0.count("CROSSCHECK job") == 3 and "DIFFER" not in t0)

        A, U, F = "901", "UNVERIFIED", "FAILS"
        # --- a red gate is recorded, not judged
        t = run_case("a red gate (FAIL at lean-manuscript) holds with its FAIL step and verdict",
                     {A: {"gate_fail_step": "lean-manuscript", "job_conclusion": "failure"},
                      "cfg": {A: {"bridge_conclusion": "failure"}}}, "HOLDS", {A: "HOLDS"})
        r = json.loads(dict(_blocks(t))[A])
        chk("  ... and records the gate's verdict text and the FAIL", r["expected"]["gate"]["verdict"].startswith("FAILED -> ")
            and [s["status"] for s in r["expected"]["gate"]["steps"]].count("FAIL") == 1)
        t = run_case("a cancelled run holds as cancelled, with its annotation and no gate",
                     {A: {"cancel": True, "gate_block": False, "job_conclusion": "cancelled"},
                      "cfg": {A: {"bridge_conclusion": "cancelled"}}}, "HOLDS", {A: "HOLDS"})
        r = json.loads(dict(_blocks(t))[A])
        chk("  ... outcome cancelled, build success, the cancellation annotation",
            r["expected"]["outcome"] == "cancelled" and r["expected"]["build_success"] is True
            and r["expected"]["error_annotations"]["Release gate"] == ["##[error]The operation was canceled."])
        run_case("a run whose earlier step failed holds as not-built",
                 {A: {"build_section": False, "gate_section": False, "job_conclusion": "failure",
                      "step_conclusions": {"Install elan": "failure", STEP_BUILD: "skipped", STEP_GATE: "skipped"}},
                  "cfg": {A: {"bridge_conclusion": "failure"}}}, "HOLDS", {A: "HOLDS"}, needle="RESULT 901 HOLDS not-built")
        # --- the per-run fail-closed rules
        run_case("a log at another head FAILS", {A: {"head": "f" * 40}}, F, {A: F, "902": "HOLDS"},
                 "FAIL head: the checked-out commit is the run's head")
        run_case("a pull-request merge of another head FAILS", {"902": {"merge_of": "f" * 40}}, F, {"902": F},
                 "FAIL head: the synthetic merge")
        run_case("a pull-request log without its merge line is UNVERIFIED (unknown format)",
                 {"902": {"drop_merge_line": True}}, U, {"902": U}, "UNVERIFIED format: one synthetic-merge checkout line")
        run_case("a run record at another head FAILS", {A: {"run_edits": [lambda r: r.update(head_sha="f" * 40)]}}, F,
                 {A: F}, "FAIL run: the pinned id, head and event")
        run_case("a truncated log (a served tail) is UNVERIFIED", {A: {"truncate": 9}}, U, {A: U},
                 "UNVERIFIED log: complete")
        run_case("a log cut before its cleanup is UNVERIFIED", {A: {"drop_tail": 3}}, U, {A: U},
                 "UNVERIFIED log: complete")
        run_case("a renamed Build header (unknown format) is UNVERIFIED, not FAILS",
                 {A: {"hdr_build": "##[group]Run lake build"}}, U, {A: U}, "UNVERIFIED format: one Build section")
        run_case("a gate step that ran with no gate section found is UNVERIFIED, not FAILS",
                 {A: {"gate_section": False, "step_conclusions": {STEP_GATE: "success"}}}, U, {A: U},
                 "UNVERIFIED format: one Release gate section")
        run_case("a missing log (fetch failed) is UNVERIFIED",
                 {A: {"drop_log": True, "fetch_edits": [lambda r: r["log"].update(outcome="failed", stage="storage",
                                                                                   error_type="HTTPError")]}},
                 U, {A: U}, "UNVERIFIED log not read: stage storage")
        run_case("an expired log (HTTP 410) is UNVERIFIED and named as expired",
                 {A: {"drop_log": True, "fetch_edits": [lambda r: r["log"].update(outcome="failed", stage="api",
                                                                                   http_status=410)]}},
                 U, {A: U}, "UNVERIFIED log not available (HTTP 410): expired or deleted")
        run_case("a run left unread at the rate-limit reserve is UNVERIFIED and named",
                 {A: {"fetch_edits": [lambda r: r["run"].update(outcome="failed", stage="rate-limit-reserve")]}},
                 U, {A: U}, "the rate-limit reserve was reached")
        run_case("a log that does not match its record is UNVERIFIED",
                 {A: {"fetch_edits": [lambda r: r["log"].update(sha256="0" * 64)]}}, U, {A: U},
                 "does not match its download record")
        run_case("a successful Build step without a build line FAILS", {A: {"drop_build_line": True}}, F, {A: F},
                 "FAIL build: a 'Build completed successfully' line")
        run_case("a build line under a failed Build step FAILS",
                 {A: {"step_conclusions": {STEP_BUILD: "failure"}, "job_conclusion": "failure"},
                  "cfg": {A: {"bridge_conclusion": "failure"}}}, F, {A: F}, "FAIL build: no 'Build completed")
        run_case("a failed Build step with no located cause is UNVERIFIED",
                 {A: {"build_fail_silent": True, "gate_section": False, "job_conclusion": "failure"},
                  "cfg": {A: {"bridge_conclusion": "failure"}}}, U, {A: U}, "cause is located")
        run_case("a skipped Build step with a Build section FAILS",
                 {A: {"step_conclusions": {STEP_BUILD: "skipped"}}}, F, {A: F}, "FAIL log: no Build section")
        run_case("a successful gate step with a FAILED verdict FAILS", {A: {"gate_verdict": "FAILED -> voice"}}, F,
                 {A: F}, "FAIL gate: a PASS verdict under a successful")
        run_case("a failed gate step without a verdict is UNVERIFIED",
                 {A: {"gate_block": False, "step_conclusions": {STEP_GATE: "failure"}, "job_conclusion": "failure"},
                  "cfg": {A: {"bridge_conclusion": "failure"}}}, U, {A: U}, "printed a verdict")
        run_case("a PASS verdict with a FAIL step FAILS", {A: {"gate_fail_step": "voice", "gate_verdict": "PASS"}}, F,
                 {A: F}, "FAIL gate: a PASS verdict has no FAIL step")
        run_case("a gate step line repeated FAILS", {A: {"gate_extra_steps": ["voice"]}}, F, {A: F},
                 "FAIL gate: at least one step line, each step once")
        run_case("a successful job with a failed step FAILS",
                 {A: {"step_conclusions": {"Install elan": "failure"}}}, F, {A: F}, "FAIL job: success")
        run_case("a bridge job conclusion other than the pinned one FAILS",
                 {A: {"job_conclusion": "failure", "gate_fail_step": "voice"}}, F, {A: F},
                 "FAIL jobs: the bridge job's conclusion is the pinned success")
        run_case("a skipped bridge job (no steps run) is UNVERIFIED",
                 {A: {"job_conclusion": "skipped", "build_section": False, "gate_section": False,
                      "step_conclusions": {s: "skipped" for s in STEPS_FIXTURE}},
                  "cfg": {A: {"bridge_conclusion": "skipped"}}}, U, {A: U}, "conclusion is success, failure or cancelled")
        run_case("a job list naming another bridge job FAILS",
                 {A: {"jobs_edits": [lambda d: d["jobs"][0].update(name="Lean kernel check")]}}, F, {A: F},
                 "FAIL jobs: the pinned bridge job")
        run_case("an unclosed axiom list is UNVERIFIED", {A: {"unclosed": True}}, U, {A: U}, "every axiom list closes")
        run_case("a credential-shaped string in the result FAILS",
                 {A: {"gate_summary_extra": " (contact someone@example.com)"}}, F, {A: F}, "FAIL output: credential")
        run_case("an axiom outside the permitted three is recorded, not judged",
                 {A: {"b_axioms": "propext, Lean.trustCompiler"}}, "HOLDS", {A: "HOLDS"},
                 "OIBridge/B.lean:7 OIBridge.B.u [propext, Lean.trustCompiler]")
        run_case("a sorryAx report is recorded in the markers, not judged",
                 {A: {"b_axioms": "propext, sorryAx"}}, "HOLDS", {A: "HOLDS"}, '"sorryAx": 1')
        # --- the extractor blob: a primed name is parsed or named as a gap, never lost
        t = run_case("a primed declaration name holds and is either parsed or named as a gap", {A: {"primed": True}},
                     "HOLDS", {A: "HOLDS"})
        r = json.loads(dict(_blocks(t))[A])
        in_mod = "OIBridge/C.lean" in r["expected"]["axiom_reports"]
        in_gap = any("OIBridge/C.lean:5" in g for g in r["gaps"])
        chk("  ... with the pinned blob's REPORT pattern: exactly one of parsed and gap (%s)"
            % ("parsed" if in_mod else "gap"), in_mod != in_gap)
        ex2 = _exec_extractor(open(extractor_path, "rb").read(), extractor_path)
        ex2.REPORT = re.compile(r"^info: ((?:OIBridge/)?[A-Za-z0-9_/]+\.lean):(\d+):\d+: '(.+?)' "
                                r"(depends on axioms: \[(.*)|does not depend on any axioms)")
        check_interface(ex2)
        n += 1
        d = os.path.join(base, "c%03d" % n)
        inputs, doc, xc = _fixture(d, 0, {A: {"primed": True}})
        buf = io.StringIO()
        run_all(ex2, doc, 1, inputs, xc, out=buf)
        rr = json.loads(dict(_blocks(buf.getvalue())).get(A, "{}") or "{}")
        ok = rr.get("expected", {}).get("axiom_reports", {}).get("OIBridge/C.lean", "").startswith("1 reports; propext x1") \
            and not any("does not parse" in g for g in rr.get("gaps", []))
        print("  %s  under a repaired REPORT pattern (simulated in-process), the primed report is parsed and no gap "
              "remains" % ("ok  " if ok else "FAIL"))
        fails += not ok
        # --- malformed records
        run_case("a truncated run record is UNVERIFIED", {A: {"run_raw": lambda b: b[:len(b) // 2]}}, U, {A: U},
                 "run-901.json unreadable: JSONDecodeError")
        run_case("a missing jobs record is UNVERIFIED", {A: {"drop_jobs": True}}, U, {A: U}, "jobs-901.json unreadable")
        run_case("a run record without head_sha is UNVERIFIED", {A: {"run_edits": [lambda r: r.pop("head_sha")]}}, U,
                 {A: U}, "malformed record: run-901.json lacks head_sha")
        run_case("a run attempt given as true is UNVERIFIED", {A: {"run_edits": [lambda r: r.update(run_attempt=True)]}},
                 U, {A: U}, "field run_attempt is bool")
        run_case("a run of attempt 2 FAILS", {A: {"attempt": 2}}, F, {A: F}, "FAIL run: the pinned id")
        run_case("a jobs list holding null is UNVERIFIED", {A: {"jobs_edits": [lambda d: d["jobs"].insert(0, None)]}}, U,
                 {A: U}, "job 0 is not a JSON object")
        run_case("a jobs list shorter than total_count FAILS", {A: {"jobs_edits": [lambda d: d.update(total_count=3)]}}, F,
                 {A: F}, "FAIL jobs: the list is complete")
        run_case("a fetch record without the run is UNVERIFIED",
                 {"fetch_top_edits": [lambda f: f["runs"].pop(A)]}, U, {A: U}, "no entry for run 901")
        run_case("a fetch record of another shard leaves every run UNVERIFIED",
                 {"fetch_top_edits": [lambda f: f.update(shard=2)]}, U, H3 and {A: U, "902": U, "903": U},
                 "CHECK all UNVERIFIED malformed record: the fetch record is not shard 1's")
        # --- the run set and the shard verdict
        V = "CHECK all UNVERIFIED the run set: "
        run_case("one run FAILS: the shard FAILS, the other runs' blocks still print", {A: {"head": "f" * 40}}, F,
                 {A: F, "902": "HOLDS", "903": "HOLDS"})
        run_case("a run missing from the shard is UNVERIFIED", {}, U, None, V + "runs missing ['903']",
                 kw={"runs_edit": lambda rs: rs[:2]})
        run_case("a run of another shard is UNVERIFIED", {}, U, None, V + "runs missing [], unexpected ['904']",
                 kw={"runs_edit": lambda rs: rs + [dict(FIXTURE_RUNS[3])]})
        run_case("a run twice, both holding, is UNVERIFIED", {}, U, None, V + "run 901 appears more than once",
                 kw={"runs_edit": lambda rs: rs + [rs[0]]})
        run_case("no runs at all is UNVERIFIED", {}, U, None, V + "no runs", kw={"runs_edit": lambda rs: []})
        n += 1
        E = ["1", "2"]
        two = [{"run_id": "1"}, {"run_id": "2"}]
        ok = (overall({"1": "HOLDS", "2": "HOLDS"}, two, E) == "HOLDS"
              and overall({"1": "HOLDS"}, two, E) == "UNVERIFIED"
              and overall({"1": "HOLDS", "2": None}, two, E) == "UNVERIFIED"
              and overall({"1": "HOLDS", "2": "MAYBE"}, two, E) == "UNVERIFIED"
              and overall({"1": "HOLDS", "2": "FAILS"}, two, E) == "FAILS"
              and overall({"1": "UNVERIFIED", "2": "HOLDS"}, two, E) == "UNVERIFIED"
              and overall({}, [], E) == "UNVERIFIED" and overall({"1": "HOLDS"}, two[:1], []) == "UNVERIFIED"
              and overall({"1": "HOLDS", "2": "HOLDS"}, two, ["1", "2", "3"]) == "UNVERIFIED")
        print("  %s  the shard holds only when exactly its runs each carry an explicit HOLDS" % ("ok  " if ok else "FAIL"))
        fails += not ok
        # --- the line budget
        t = run_case("a block past the line budget is withheld and its run UNVERIFIED; earlier blocks print", {}, U,
                     {A: "HOLDS", "903": U}, "UNVERIFIED output budget", budget=len(t0.split("\n")) - 40)
        chk("  ... and the output stays within the budget", len(t.rstrip("\n").split("\n")) <= len(t0.split("\n")) - 40)
        # --- the cross-check is printed, never decisive
        n += 1
        d = os.path.join(base, "c%03d" % n)
        inputs, doc, xc = _fixture(d, 0, {})
        xc["jobs"]["9101"]["tail_sha256"] = "0" * 64
        xc["jobs"].pop("9102")
        buf = io.StringIO()
        code = run_all(ex, doc, 1, inputs, xc, out=buf)
        t = buf.getvalue()
        ok = code == 0 and "CROSSCHECK job 9101" in t and "DIFFER FROM" in t and "CROSSCHECK job 9102 not observed" in t
        print("  %s  a differing or absent session observation is printed and does not change the verdict"
              % ("ok  " if ok else "FAIL"))
        fails += not ok
        # --- pins
        n += 1
        bad = os.path.join(base, "extract_result.py")
        with open(extractor_path, "rb") as f, open(bad, "wb") as g:
            g.write(f.read() + b"\n# one more line: the same interface, another blob\n")
        try:
            load_extractor(bad)
            ok = False
        except Unverified:
            ok = True
        print("  %s  an extractor other than the pinned blob is refused before it runs" % ("ok  " if ok else "FAIL"))
        fails += not ok
        n += 1
        mod = _exec_extractor(open(extractor_path, "rb").read(), extractor_path)
        mod.MARKERS = dict(list(mod.MARKERS.items())[:3])
        try:
            check_interface(mod)
            ok = False
        except Unverified:
            ok = True
        print("  %s  an extractor with another interface is refused" % ("ok  " if ok else "FAIL"))
        fails += not ok
        n += 1
        hits = scan('{\n "a": "ghp_' + "a" * 30 + '",\n "b": "https://x.blob.core.windows.net/c?sv=1&sig=2",\n'
                    ' "c": "10.1.2.3"\n}\n')
        ok = [h[0] for h in hits] == [2, 3, 4] and not scan(canonical({"v": "4.21.0", "h": "0" * 64, "p": "a/b.lean:3:0"}))
        print("  %s  the scan finds a token, a signed URL and an IP address, and passes versions, digests and paths"
              % ("ok  " if ok else "FAIL"))
        fails += not ok
        n += 1
        try:
            hp = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "host.py")).read()
            ok = re.search(r'^RUNS_SHA256 = "%s"$' % RUNS_SHA256, hp, re.M) is not None
        except OSError:
            ok = False
        print("  %s  host.py pins the same runs.json digest" % ("ok  " if ok else "FAIL"))
        fails += not ok
    finally:
        shutil.rmtree(base, ignore_errors=True)
    print("assemble self-test: %d of %d cases ok" % (n - fails, n))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--extractor", required=True)
    ap.add_argument("--extractor-repo")
    ap.add_argument("--runs")
    ap.add_argument("--crosscheck")
    ap.add_argument("--shard", type=int)
    ap.add_argument("--host")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--unpinned", action="store_true", help="self-test only: accept an extractor of another blob")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    if a.self_test:
        try:
            return 1 if self_test(a.extractor, a.work, pinned=not a.unpinned) else 0
        except Unverified as e:
            print("assemble self-test: extractor refused: %s" % e)
            return 1
    if a.unpinned:
        ap.error("--unpinned is for the self-test only")
    if not (a.extractor_repo and a.runs and a.crosscheck and a.shard and a.host):
        ap.error("--extractor-repo, --runs, --crosscheck, --shard and --host are required")
    shard = a.shard
    try:
        doc = load_pinned(a.runs, RUNS_SHA256, "runs.json")
        xc = load_pinned(a.crosscheck, CROSSCHECK_SHA256, "crosscheck.json")
        ex = load_extractor(a.extractor, a.extractor_repo)
    except (Unverified, ValueError) as e:
        print("CHECK all UNVERIFIED %s" % e)
        print("EXTRACT SHARD %d/? UNVERIFIED" % shard)
        return 2
    inputs = {"host": a.host, "fetch_record": os.path.join(a.host, "fetch-record.json")}
    return run_all(ex, doc, shard, inputs, xc)


if __name__ == "__main__":
    sys.exit(main())
