#!/usr/bin/env python3
"""Assemble KTOKEN-MAXCONE-1's exact-head bridge results (AGENTS §A.42 item 1, form `derived`), one per target in
extractor/targets.json, from each Mathlib bridge job's whole log, the host's JSON records and the target's commit,
and print them. Read-only; Python 3 stdlib and git.

  python3 -I assemble_evidence.py --objects OBJ --host HOSTDIR --logs LOGDIR --download-record download-record.json
  python3 -I assemble_evidence.py --self-test --objects OBJ [--work DIR]
  python3 -I assemble_evidence.py --reassemble SERVED_LOG --label F [--out FILE]

Inputs:
  --objects          the bare repository from fetch_sources.py: the two extractor commits and each target's commit.
                     extract_result.py is read there at main 809fa9d6 (blob e6f69713, the extractor) and at b96662e6
                     (blob 05c41bce, the cross-check); each is read once, its blob id checked, then those bytes are
                     executed. The target's sources are read there with their blob ids checked.
  --host             run-<run>.json and job-<job>.json (the API answers' bytes) and jobs-<run>.json from
                     fetch_records.py.
  --logs, --download-record
                     <job>.log and the record from download_job_logs.py; each log's length, sha256 and line count
                     must equal the record's.

The result has the schema of the round's evidence/f-run/results.json (oi-evidence-result, kind bridge): the same
keys at every level, with the whole log read, so `gaps` is empty and the window fields describe the whole log
(served_window [1, N]). Line numbers are 1-based lines of the whole log after any byte-order mark.

For each target it reads, with the extractor's extract on each step's section: the build line, every `#print
axioms` report, the release-gate block and verdict, and the failure markers (counted over the Build and Release
gate sections, the scope compare_result.py compares). The governed modules are verification/lean-mathlib's
OIBridge.lean and OIBridge/KTokenMaxCone.lean; a governed module absent from the commit must have no report. With
the extractor's check() it requires every `#print axioms` command of every .lean file under
verification/lean-mathlib at the commit to have exactly one report in the Build section, every report within
propext, Classical.choice and Quot.sound, and no failure and no gap. The cross-check extractor must read the same
build line, gate, governed modules' reports and markers. From the API records: the run's identity, every job's
conclusion, and the bridge job's steps.

Fail closed. A target's result is printed only if every check holds for it. Otherwise it FAILS (the evidence is
present and contradicts or lacks a required item) or is UNVERIFIED (an input is absent or does not match its
record). Each failed check is printed by name. The verdict line is the last line printed:
  EXTRACT HOLDS       every listed target's result printed (exit 0)
  EXTRACT FAILS       at least one target FAILS (exit 1)
  EXTRACT UNVERIFIED  no target FAILS, and a target is UNVERIFIED, the inputs are not exactly the listed runs,
                      each once, or targets.json is refused (exit 2)

Printed for each target, whatever its verdict, when the sections were found: the release-gate block (GATE lines)
and the axiom-report table of every .lean file at the commit (AXIOMS lines). Printed for a target that HOLDS: its
result, as compact JSON (sorted keys, separators "," and ":") cut into numbered lines between
  ===== BEGIN EXPECTED RESULT <label> <path> (compact JSON, <k> numbered lines) =====
  RJ <label> <nnnn> <text>
  ===== END EXPECTED RESULT <label> <path> =====
followed by `SHA256 <label> <path> canonical=<hex> bytes=<n> compact=<hex>`. The committed form is canonical:
json.dumps(obj, indent=1, sort_keys=True) plus a newline (ASCII). `--reassemble` rebuilds it from the job log as
served (timestamps stripped) and checks both digests. Before printing, the canonical text is scanned for
credentials, signed-URL query strings, IP and e-mail addresses; a hit FAILS the target.
"""
import argparse
import contextlib
import hashlib
import importlib.util
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
HERE = os.path.dirname(os.path.abspath(__file__))


def _load_targets_module():
    spec = importlib.util.spec_from_file_location("ktoken_targets", os.path.join(HERE, "targets.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


T = _load_targets_module()
REPO = T.REPO
ROUND = T.ROUND
EXTRACT_RESULT_PATH = "verification/audits/evidence-retention/extract_result.py"
# The extractor: main at 809fa9d6. It reads primed declaration names (29 #print axioms commands at e12c1573 name
# one) and joins only Lean's continuation lines; it carries the fail-closed report check.
EXTRACTOR = ("809fa9d6fc931d7a75027ad72d6d2d4b03b722a5", "e6f69713bfffd1f1f9aca3c27bf26a689c994167")
# The cross-check: main at b96662e6, the blob the round's earlier records name (05c41bce).
CROSS = ("b96662e6be4f537502c772db369ea32a35b213a8", "05c41bce610b8d02ccbaca8e69377b771bef4a35")
MARKER_KEYS = ("sorryAx", "Lean.ofReduceBool", "declaration uses 'sorry'", "error:")
LEAN_DIR = "verification/lean-mathlib/"
GOVERNED = ("OIBridge.lean", "OIBridge/KTokenMaxCone.lean")   # the round's governed .lean files, from LEAN_DIR
KTOKEN = "OIBridge/KTokenMaxCone.lean"
PERMITTED = ["propext", "Classical.choice", "Quot.sound"]
JOB_BRIDGE = "Mathlib bridge"
WORKFLOW = ".github/workflows/verify.yml"
STEP_BUILD, STEP_GATE = "Build", "Release gate"
HDR_BUILD = "##[group]Run lean --version"
HDR_GATE = "##[group]Run python3 tools/release_gate.py"
GATE_SOURCE = "tools/release_gate.py"

# The release gate's steps, in the order it prints them, read from its source and never from a run's output:
# tools/release_gate.py, blob d40e2acc9783704dcaf5793bb2228e96252dc6e8 (at D b96662e6, at F e12c1573 and on the
# round branch at 7ce49dd1): the 21 entries of `checks = [...]` with `checks.insert(2, ("baseline-label", lab))`.
# The blob is checked at each target's commit; any other blob leaves the target unverified.
GATE_STEPS = ("toolchain", "staleness", "baseline-label", "voice", "voice-scope", "ci-gate-presence",
              "artifact-placement", "manifest-drift", "claims", "duplicate", "mirror", "citation", "architecture",
              "dependency-label", "coverage", "lean-axioms", "lean-manuscript", "legacy-records", "v3-self-test",
              "v3-corpus", "v3-receipts", "evidence-retention")
GATE_STEPS_BY_BLOB = {"d40e2acc9783704dcaf5793bb2228e96252dc6e8": GATE_STEPS}

# check_retention.py's R5 pattern (main at b96662e6), with signed-URL parameters of the log storage hosts added.
SECRET = re.compile(
    r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat[_]|AKIA[0-9A-Z]{16}|-{5}BEGIN|bearer [a-z0-9]'
    r'|x-access-toke[n]|[?&](sig|signature|sv|se|sp|sr|st|skoid|sktid|skt|ske|sks|skv|token|x-amz-[a-z-]+)='
    r'|passw(or)?d\s*[:=]|api[_-]?key\s*[:=]|private[_-]?key|https?://[^\s"]*\?'
    r'|blob\.core\.windows\.net|actions\.githubusercontent\.com'
    r'|(?<![\w.])(?:\d{1,3}\.){3}\d{1,3}(?![\w.])|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', re.I)
TS = re.compile(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\.\d+Z ")
BEGIN = "===== BEGIN EXPECTED RESULT %s %s (compact JSON, %d numbered lines) ====="
BEGIN_RX = re.compile(r"^===== BEGIN EXPECTED RESULT (\S+) (\S+) \(compact JSON, (\d+) numbered lines\) =====$")
END = "===== END EXPECTED RESULT %s %s ====="
CHUNK = 180


class Unverified(Exception):
    pass


def git_blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def own_blob(name):
    with open(os.path.join(HERE, name), "rb") as f:
        return git_blob_id(f.read())


# ------------------------------------------------------------------------------------------------ objects

class Objects:
    """Read-only access to the bare repository fetch_sources.py wrote; every blob's id is recomputed."""

    def __init__(self, path):
        self.path = path

    def _git(self, *args, inp=None):
        env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull, GIT_TERMINAL_PROMPT="0",
                   GIT_NO_LAZY_FETCH="1")
        for k in ("GH_TOKEN", "GITHUB_TOKEN"):
            env.pop(k, None)
        p = subprocess.run(["git", "-C", self.path] + list(args), input=inp, capture_output=True, env=env, timeout=120)
        return p.returncode, p.stdout

    def has_commit(self, c):
        rc, out = self._git("cat-file", "-t", c)
        return rc == 0 and out.strip() == b"commit"

    def blob_id(self, c, path):
        rc, out = self._git("rev-parse", "--verify", "-q", "%s:%s" % (c, path))
        return out.decode().strip() if rc == 0 else None

    def read(self, c, paths):
        """{path: bytes or None (absent)} at commit c, each blob's id recomputed and compared."""
        if not paths:
            return {}
        rc, out = self._git("cat-file", "--batch", inp="".join("%s:%s\n" % (c, p) for p in paths).encode())
        if rc != 0:
            raise Unverified("cat-file --batch failed at %s" % c[:12])
        res, pos = {}, 0
        for p in paths:
            nl = out.index(b"\n", pos)
            head = out[pos:nl].decode()
            pos = nl + 1
            parts = head.split(" ")
            if len(parts) == 2 and parts[1] == "missing":
                res[p] = None
                continue
            if len(parts) != 3 or parts[1] != "blob":
                raise Unverified("%s at %s is not a blob (%s)" % (p, c[:12], head[:80]))
            n = int(parts[2])
            data = out[pos:pos + n]
            pos += n + 1
            if git_blob_id(data) != parts[0]:
                raise Unverified("%s at %s does not hash to its blob id" % (p, c[:12]))
            res[p] = data
        return res

    def lean_files(self, c):
        rc, out = self._git("ls-tree", "-r", "-z", "--name-only", c, "--", LEAN_DIR)
        if rc != 0:
            raise Unverified("ls-tree failed at %s" % c[:12])
        names = [x.decode("utf-8") for x in out.split(b"\0") if x]
        return sorted(n[len(LEAN_DIR):] for n in names if n.endswith(".lean") and "/.lake/" not in n)


def load_extractor(objects, pin, need):
    """Read extract_result.py at the pinned commit, check the blob id, then execute exactly those bytes."""
    commit, blob = pin
    if not objects.has_commit(commit):
        raise Unverified("extractor commit %s absent from the objects" % commit[:12])
    if objects.blob_id(commit, EXTRACT_RESULT_PATH) != blob:
        raise Unverified("extract_result.py at %s is not the pinned blob %s" % (commit[:12], blob[:12]))
    data = objects.read(commit, [EXTRACT_RESULT_PATH])[EXTRACT_RESULT_PATH]
    return exec_extractor(data, blob, need, "%s:%s" % (commit[:12], EXTRACT_RESULT_PATH))


def exec_extractor(data, blob, need, label):
    if data is None or git_blob_id(data) != blob:
        raise Unverified("extractor %s is not the pinned blob %s" % (label, blob[:12]))
    mod = types.ModuleType("extract_result_%s" % blob[:8])
    mod.__file__ = label
    exec(compile(data, label, "exec"), mod.__dict__)  # noqa: S102 - the pinned, verified bytes
    for name in need:
        if not hasattr(mod, name):
            raise Unverified("extractor %s lacks %s" % (label, name))
    if tuple(mod.MARKERS) != MARKER_KEYS:
        raise Unverified("extractor %s markers are not the expected four" % label)
    return mod


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
        self.sha256 = sha256(data)
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
        self.tail = lambda k: "\n".join(whole[-k:])
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

    def text(self, a, b):
        return "\n".join(self.raw[a:b])


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


def first_hits(lines_idx, rx, n=3):
    return [(i + 1, l[:160]) for i, l in lines_idx if rx.search(l)][:n]


def load_raw(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError as e:
        raise Unverified("%s unreadable: %s" % (os.path.basename(path), type(e).__name__))
    try:
        return data, json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as e:
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


def check_run_record(run, where):
    _need(isinstance(run, dict), "%s is not a JSON object" % where)
    _typed(run, where, (("id", int), ("head_sha", str), ("run_attempt", int), ("event", str),
                        ("conclusion", str), ("path", str), ("head_branch", str)))


def check_job(j, where):
    _need(isinstance(j, dict), "%s is not a JSON object" % where)
    _typed(j, where, (("id", int), ("run_id", int), ("run_attempt", int), ("name", str), ("conclusion", str),
                      ("head_sha", str), ("steps", list)))
    for m, st in enumerate(j["steps"]):
        ws = "%s step %d" % (where, m)
        _need(isinstance(st, dict), "%s is not a JSON object" % ws)
        _typed(st, ws, (("number", int), ("name", str), ("conclusion", str)))


def check_jobs_record(jobsd, where):
    _need(isinstance(jobsd, dict), "%s is not a JSON object" % where)
    _typed(jobsd, where, (("total_count", int), ("jobs", list)))
    for n, j in enumerate(jobsd["jobs"]):
        check_job(j, "%s job %d" % (where, n))


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


def axiom_key(r):
    return "none" if r.get("axioms") is None else ", ".join(r["axioms"])


# ------------------------------------------------------------------------------------------------ assembly

def assemble_target(t, exs, inputs, env=None):
    """Returns (Checks, result dict or None, printable dict)."""
    env = os.environ if env is None else env
    ex, cx = exs["main"], exs["cross"]
    C = Checks(t["label"])
    show = {}
    head, rid, jid, label = t["commit"], t["run_id"], t["bridge_job"], t["label"]
    objects = inputs["objects"]
    try:
        run_raw, run = load_raw(os.path.join(inputs["host"], "run-%s.json" % rid))
        check_run_record(run, "run-%s.json" % rid)
        job_raw, job = load_raw(os.path.join(inputs["host"], "job-%s.json" % jid))
        check_job(job, "job-%s.json" % jid)
        _, jobsd = load_raw(os.path.join(inputs["host"], "jobs-%s.json" % rid))
        check_jobs_record(jobsd, "jobs-%s.json" % rid)
        recs = check_download_record(load_raw(inputs["download_record"])[1])
        blog = Log(os.path.join(inputs["logs"], jid + ".log"), recs.get(jid), ex)
        if not objects.has_commit(head):
            raise Unverified("commit %s absent from the objects" % head[:12])
        gate_blob = objects.blob_id(head, GATE_SOURCE)
        if gate_blob not in GATE_STEPS_BY_BLOB:
            raise Unverified("%s at %s is blob %s, whose step list is not pinned here" % (GATE_SOURCE, head[:12], gate_blob))
        files = objects.lean_files(head)
        srcb = objects.read(head, [LEAN_DIR + f for f in files])
        srcs = {f: srcb[LEAN_DIR + f].decode("utf-8") for f in files}
        gov_blobs = {m: objects.blob_id(head, LEAN_DIR + m) for m in GOVERNED}
    except Unverified as e:
        C.unverified.append(str(e))
        return C, None, show
    except Exception as e:  # noqa: BLE001 - any other failure while reading the inputs is an unverified target
        C.unverified.append("malformed input: %s: %s" % (type(e).__name__, str(e)[:200]))
        return C, None, show

    # --- run identity, jobs and the bridge job (API)
    C("run: id, head, attempt 1, event workflow_dispatch, conclusion success, workflow verify.yml",
      str(run["id"]) == rid and run["head_sha"] == head and run["run_attempt"] == 1
      and run["event"] == "workflow_dispatch" and run["conclusion"] == "success" and run["path"] == WORKFLOW,
      "id=%s head=%s attempt=%s event=%s conclusion=%s path=%s" % (run["id"], run["head_sha"][:12], run["run_attempt"],
                                                                 run["event"], run["conclusion"], run["path"]))
    jobs = jobsd["jobs"]
    C("jobs: the list is complete", jobs and len(jobs) == jobsd["total_count"] and len({j["id"] for j in jobs}) == len(jobs),
      "%d of %s" % (len(jobs), jobsd["total_count"]))
    notok = [j["name"] for j in jobs if j["conclusion"] != "success"]
    C("jobs: every job success (%d jobs)" % len(jobs), jobs and not notok, "; ".join(notok)[:300])
    C("jobs: every job at the run's head, attempt 1",
      jobs and all(j["head_sha"] == head and str(j["run_id"]) == rid and j["run_attempt"] == 1 for j in jobs))
    byid = {str(j["id"]): j for j in jobs}
    lj = byid.get(jid)
    C("jobs: the bridge job %s is in the run's job list, named %r" % (jid, JOB_BRIDGE), lj and lj["name"] == JOB_BRIDGE)
    C("job record: id %s, %r, success, at the head, of the run, attempt 1" % (jid, JOB_BRIDGE),
      str(job["id"]) == jid and job["name"] == JOB_BRIDGE and job["conclusion"] == "success" and job["head_sha"] == head
      and str(job["run_id"]) == rid and job["run_attempt"] == 1)

    def steps(j):
        return [(s["number"], s["name"], s["conclusion"]) for s in j["steps"]]
    C("job record: its steps equal the job list's", lj is not None and steps(job) == steps(lj))
    bs = {s["name"]: s["conclusion"] for s in job["steps"]}
    for st in (STEP_BUILD, STEP_GATE):
        C("bridge step %r success" % st, bs.get(st) == "success", str(bs.get(st)))

    # --- the log: complete, of this job, at this head
    C("bridge log: complete (runner header on line 1, cleanup at the end)",
      blog.s and blog.s[0].startswith("Current runner version: ") and "Cleaning up orphan processes" in blog.s[-8:],
      "line 1: %r" % (blog.s[0][:60] if blog.s else ""))
    C("bridge log: job name line", ("Complete job name: " + JOB_BRIDGE) in blog.s)
    k = [i for i, l in enumerate(blog.s) if l == "[command]/usr/bin/git log -1 --format=%H"]
    C("bridge log: checked-out head is the run's head", len(k) == 1 and k[0] + 1 < len(blog.s) and blog.s[k[0] + 1] == head)

    # --- sections
    hb, hg = blog.find(HDR_BUILD), blog.find(HDR_GATE)
    for nm, h in (("Build", hb), ("Release gate", hg)):
        C("bridge log: one %s section" % nm, len(h) == 1, "%d found" % len(h))
    if len(hb) != 1 or len(hg) != 1:
        return C, None, show
    b0, b1 = blog.section(hb[0])
    g0, g1 = blog.section(hg[0])
    C("bridge log: the Build section ends where the Release gate section begins", b1 == g0, "%d vs %d" % (b1, g0))
    bx, gx = ex.extract(blog.text(b0, b1)), ex.extract(blog.text(g0, g1))
    wx = ex.extract("\n".join(blog.raw))
    bc, gc = cx.extract(blog.text(b0, b1)), cx.extract(blog.text(g0, g1))

    # --- build, gate, markers
    bline = bx.get("build")
    C("build: 'Build completed successfully' line in the Build section", bline and bline.get("success"))
    gate = gx.get("gate")
    gv = (gate or {}).get("verdict")
    C("gate: a release-gate block with steps and a verdict", gate and gate.get("steps") and gv)
    C("gate: verdict PASS and every step PASS", gv and gv.get("pass") and all(s["status"] == "PASS" for s in gate["steps"]),
      "" if not gate else "; ".join("%s %s" % (s["status"], s["name"]) for s in gate["steps"] if s["status"] != "PASS"))
    want_steps = list(GATE_STEPS_BY_BLOB[gate_blob])
    got_steps = [s["name"] for s in gate["steps"]] if gate and gate.get("steps") else []
    C("gate: exactly the %d steps of %s at the head (blob %s), in its order" % (len(want_steps), GATE_SOURCE, gate_blob[:12]),
      got_steps == want_steps, "%d steps; missing %s; unexpected %s" % (
          len(got_steps), [x for x in want_steps if x not in got_steps][:4], [x for x in got_steps if x not in want_steps][:4]))
    markers = {k: bx["markers"].get(k, 0) + gx["markers"].get(k, 0) for k in MARKER_KEYS}
    C("markers: none in the Build and Release gate sections", not any(markers.values()),
      str(first_hits([(i, blog.s[i]) for i in range(b0, g1)], re.compile(r"error:|sorryAx|ofReduceBool|declaration uses")))
      if any(markers.values()) else "")
    if gate and gv:
        show["gate"] = blog.s[g0 + gate["start_line"] - 1:g0 + gv["served_line"]]

    # --- every .lean file's reports (the extractor's fail-closed check over the Build section)
    with_prints = {f: s for f, s in srcs.items() if re.search(r"(?m)^#print axioms\b", s)}
    fails, gaps = ex.check(bx, with_prints)
    C("reports: extract_result.check over the Build section, every .lean file at the head with a #print axioms "
      "command (%d files), holds with no failure and no gap" % len(with_prints), with_prints and not fails and not gaps,
      "; ".join((fails + gaps)[:4])[:400])
    stray = sorted(set(bx.get("reports", {})) - set(with_prints))
    C("reports: every module reported in the Build section has #print axioms commands at the head", not stray,
      ", ".join(stray[:5]))
    C("reports: no direct (unprefixed) report in the Build section", not bx.get("direct"),
      "%d block(s)" % len(bx.get("direct") or []))
    table = []
    for f in sorted(with_prints):
        reps = bx.get("reports", {}).get(f, [])
        sets = {}
        for r in reps:
            sets[axiom_key(r)] = sets.get(axiom_key(r), 0) + 1
        npr = len(re.findall(r"(?m)^#print axioms\b", with_prints[f]))
        table.append({"module": f, "prints": npr, "reports": len(reps), "unclosed": sum(1 for r in reps if r.get("unclosed")),
                      "sets": sets})
    show["table"] = table

    # --- governed modules
    modules, report_lines = {}, {}
    for mod in GOVERNED:
        reps = bx.get("reports", {}).get(mod, [])
        whole = wx.get("reports", {}).get(mod, [])
        if mod not in srcs:
            C("%s: absent from the tree at the head, and no report of it anywhere in the log" % mod,
              gov_blobs[mod] is None and not whole, "%d report(s)" % len(whole))
            modules[mod] = {"note": "the module is not in the tree at %s" % head[:12], "print_lines": None, "prints": None,
                            "reports": [], "status": "absent"}
            report_lines[mod] = {}
            continue
        pl = {i + 1 for i, l in enumerate(srcs[mod].split("\n")) if re.match(r"^#print axioms\b", l)}
        lines = [r["line"] for r in reps]
        names = [r["name"] for r in reps]
        complete = bool(pl) and set(lines) == pl and len(lines) == len(pl) and len(set(names)) == len(names)
        C("%s: one report per #print axioms line of the source at the head (%d prints)" % (mod, len(pl)), complete,
          "%d reports at %d distinct lines" % (len(reps), len(set(lines))))
        out = [n for n, r in zip(names, reps) if r["axioms"] is not None and not set(r["axioms"]) <= set(PERMITTED)]
        C("%s: every axiom within propext, Classical.choice, Quot.sound" % mod, not out, ", ".join(out)[:300])
        C("%s: no report of it outside the Build section" % mod, len(whole) == len(reps), "%d vs %d" % (len(whole), len(reps)))
        modules[mod] = {"print_lines": spans(pl), "prints": len(pl),
                        "reports": sorted(({"axioms": r["axioms"], "line": r["line"], "name": r["name"]} for r in reps),
                                          key=lambda r: (r["line"], r["name"]))}
        modules[mod]["status"] = "complete" if complete else "partial" if reps else "none"
        report_lines[mod] = {r["name"]: b0 + r["served_line"] for r in reps}

    # --- the cross-check extractor reads the same expected content
    def gov(x):
        return {m: sorted((r["line"], r["name"], tuple(r["axioms"] or ()), r["axioms"] is None)
                          for r in x.get("reports", {}).get(m, [])) for m in GOVERNED}

    def gsum(x):
        g = x.get("gate") or {}
        return ([(s["name"], s["status"], s["summary"]) for s in g.get("steps") or []], (g.get("verdict") or {}).get("text"))
    cmark = {k: bc["markers"].get(k, 0) + gc["markers"].get(k, 0) for k in MARKER_KEYS}
    C("cross-check (%s at %s): the same build line, gate, governed modules' reports and markers" % (CROSS[1][:8], CROSS[0][:8]),
      (bc.get("build") or {}).get("success") == (bline or {}).get("success") and gsum(gc) == gsum(gx)
      and gov(bc) == gov(bx) and cmark == markers,
      "build %s/%s gate %s modules %s markers %s" % ((bc.get("build") or {}).get("success"), (bline or {}).get("success"),
                                                     gsum(gc) == gsum(gx), gov(bc) == gov(bx), cmark == markers))

    if C.failed or C.unverified:
        return C, None, show

    # --- the result, in the schema of evidence/f-run/results.json
    N = blog.lines_n
    whole_markers = wx["markers"]
    all_reports = [r for rs in wx.get("reports", {}).values() for r in rs]
    gstart, gverd = g0 + gate["start_line"], g0 + gv["served_line"]
    bl = b0 + bline["line"]
    nprints = sum(x["prints"] for x in table)
    nreps = sum(x["reports"] for x in table)
    obs = t.get("session_observation")
    if obs:
        tail_same = sha256(blog.tail(obs["tail_lines"]).encode("utf-8")) == obs["tail_sha256"]
        retr = ("one download in the extraction run; the log's %d lines %s the job-log tool's reported length %d, and "
                "its last %d lines %s the text that tool served (sha256 %s)"
                % (N, "equal" if N == obs["original_lines"] else "differ from", obs["original_lines"], obs["tail_lines"],
                   "equal" if tail_same else "differ from", obs["tail_sha256"]))
    else:
        retr = "one download in the extraction run"
    xrun = env.get("GITHUB_RUN_ID")
    where = ("extraction run %s attempt %s of the read-only workflow ktoken-f-evidence.yml" % (xrun, env.get("GITHUB_RUN_ATTEMPT"))
             if xrun else "a local run of the extractor (no GITHUB_RUN_ID)")
    gov_text = []
    for mod in GOVERNED:
        m = modules[mod]
        if m["status"] == "absent":
            gov_text.append("%s: absent from the tree at %s, with no report in the log" % (mod, label))
        else:
            gov_text.append("%s: its %d reports, in the Build section, against its %d #print axioms lines at %s"
                            % (mod, len(m["reports"]), m["prints"], label))
    result = {
        "basis": {
            "build_success": "the build-success line at line %d, in the Build step's section (lines %d-%d), and the Build "
                             "step's conclusion 'success' in the job's API answer (job_api_sha256)" % (bl, b0 + 1, b1),
            "gate": "the release-gate block, lines %d-%d, in the Release gate step's section (lines %d-%d)" % (gstart, gverd, g0 + 1, g1),
            "markers": "counted over the Build and Release gate sections (lines %d-%d), the scope compare_result.py (C4) "
                       "compares; over the whole log: %s" % (b0 + 1, g1, ", ".join("%s %d" % (k, whole_markers[k]) for k in MARKER_KEYS)),
            "modules": "; ".join(gov_text),
            "unserved_reports": "none: every line of the log was read. Each of the %d #print axioms commands in the %d .lean "
                                "files with one under verification/lean-mathlib at %s has exactly one report in the Build "
                                "section (%d reports), each within propext, Classical.choice and Quot.sound, with no "
                                "truncated list and no failure marker: extract_result.check (blob %s at %s) holds with no "
                                "failure and no gap" % (nprints, len(table), head[:12], nreps, EXTRACTOR[1][:8], EXTRACTOR[0][:8]),
        },
        "expected": {
            "build_success": True,
            "gate": {"steps": [{"name": s["name"], "status": s["status"], "summary": s["summary"]} for s in gate["steps"]],
                     "steps_pass": sum(1 for s in gate["steps"] if s["status"] == "PASS"),
                     "steps_total": len(gate["steps"]), "verdict": gv["text"]},
            "markers": markers,
            "modules": modules,
            "permitted_axioms": PERMITTED,
        },
        "form": "derived",
        "gaps": [],
        "kind": "bridge",
        "observed": {
            "build_line": blog.s[bl - 1],
            "build_served_line": bl,
            "built": wx.get("built", []),
            "cache": wx.get("cache", []),
            "first_report_served_line": min((r["served_line"] for r in all_reports), default=None),
            "gate_served_lines": {"start": gstart, "steps": [g0 + s["served_line"] for s in gate["steps"]], "verdict": gverd},
            "ktoken_lines_in_served_text": sum(1 for l in blog.s if "KTokenMaxCone" in l),
            "other_modules_in_served_text": {m: len(rs) for m, rs in sorted(wx.get("reports", {}).items()) if m not in GOVERNED},
            "report_served_lines": report_lines,
            "reports_in_served_text": len(all_reports),
        },
        "reproduce": {
            "compared": "build success; the gate's steps and verdict; each governed module's reports and axioms; the markers",
            "markers_note": "the expected zero marker counts were observed over the Build and Release gate sections of the "
                            "whole log; compare_result.py (C4) holds a reproduction to zero markers over its whole log",
            "not_compared": "timestamps, durations, cache behaviour, job counts, output order",
            "recipe": [
                "run from the root of a full-history clone at a commit that carries this record (the verifier); <dir> is a "
                "new directory and <log> a file outside it",
                "make %s present in the clone (this extraction fetched it by id from https://github.com/%s.git)" % (head, REPO),
                "git worktree add --detach <dir> %s" % head,
                "(cd <dir>/verification/lean-mathlib && lean --version && lake exe cache get && lake --rehash build) > <log> 2>&1",
                "(cd <dir> && python3 tools/release_gate.py) >> <log> 2>&1",
                "python3 -I verification/audits/evidence-retention/extract_result.py <log> > reproduced.json",
                "python3 -I verification/audits/evidence-retention/compare_result.py <this file> reproduced.json --tree <dir>",
            ],
            "tool": None,
        },
        "run": {
            "attempt": run["run_attempt"], "conclusion": run["conclusion"], "event": run["event"],
            "head_branch": run["head_branch"], "head_sha": run["head_sha"], "id": rid,
            "job_conclusion": job["conclusion"], "job_id": jid, "job_name": job["name"],
            "job_steps": [{"conclusion": s["conclusion"], "name": s["name"]} for s in job["steps"]],
            "workflow": os.path.basename(run["path"]),
        },
        "schema": "oi-evidence-result",
        "scope": "what %s's exact-head check run logged in its Mathlib bridge job, as read from the whole job log (%d lines), "
                 "and nothing about any later tree" % (label, N),
        "source": {
            "digest_form": "sha256 of the job log's bytes exactly as downloaded from the jobs/<id>/logs endpoint (%d bytes, "
                           "%d lines): the digest of the whole log" % (blog.bytes, N),
            "extractor": EXTRACT_RESULT_PATH,
            "extractor_blob": EXTRACTOR[1],
            "form_note": "derived: read from the whole job log (served_sha256) with extract_result.py at main %s, "
                         "cross-checked for the build line, the gate, the governed modules' reports and the markers "
                         "against blob %s at %s; and from the runs and jobs APIs (their answers' digests)"
                         % (EXTRACTOR[0], CROSS[1], CROSS[0]),
            "job_api_sha256": sha256(job_raw),
            "kind": "GitHub Actions job log, whole: downloaded from the jobs/<id>/logs endpoint (job_id %s) by %s, with "
                    "extractor/download_job_logs.py blob %s and extractor/assemble_evidence.py blob %s"
                    % (jid, where, own_blob("download_job_logs.py"), own_blob("assemble_evidence.py")),
            "markers_scope": "the failure markers are counted over the Build and Release gate sections of the whole log "
                             "(lines %d-%d)" % (b0 + 1, g1),
            "note": "the digest identifies the text this result was read from: it is provenance of the extraction, not "
                    "independent proof of the result, which reproduction at the commit supplies; the text is not retained",
            "original_lines": N,
            "retrievals": retr,
            "runs_api_sha256": sha256(run_raw),
            "served_bytes": blog.bytes,
            "served_lines": N,
            "served_sha256": blog.sha256,
            "served_window": [1, N],
            "window_coverage": "complete: original lines 1-%d of %d were downloaded and read" % (N, N),
            "window_rule": "the whole log was read: the Build section (lines %d-%d), the Release gate section (lines %d-%d) "
                           "and every report lie in it" % (b0 + 1, b1, g0 + 1, g1),
        },
        "version": 1,
    }
    show["cross"] = {"bom": blog.bom, "cr": blog.cr, "lines": N, "obs": obs,
                     "tail_same": (sha256(blog.tail(obs["tail_lines"]).encode("utf-8")) == obs["tail_sha256"]) if obs else None,
                     "short_names": len({r["name"].split(".")[-1] for rs in bx.get("reports", {}).values() for r in rs}),
                     "gate_axioms": next((s["summary"] for s in gate["steps"] if s["name"] == "lean-axioms"), "")}
    return C, result, show


def canonical(obj):
    return json.dumps(obj, indent=1, sort_keys=True) + "\n"


def compact(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"))


def chunks(text, width=CHUNK):
    """Cut text into pieces of at most width characters, none ending with a space (a log viewer may trim it)."""
    out, i = [], 0
    while i < len(text):
        j = min(i + width, len(text))
        while j < len(text) and j > i + 1 and text[j - 1] == " ":
            j -= 1
        out.append(text[i:j])
        i = j
    return out


def scan(text):
    return [(n + 1, m.group(0)[:6] + "...") for n, l in enumerate(text.split("\n")) for m in [SECRET.search(l)] if m]


def redact(s):
    return SECRET.sub("<redacted>", s)


def inventory_problem(targets, inputs):
    """None when the inputs hold exactly the listed runs' records and logs, each once; else why not."""
    want_host = sorted(["run-%s.json" % t["run_id"] for t in targets] + ["jobs-%s.json" % t["run_id"] for t in targets]
                       + ["job-%s.json" % t["bridge_job"] for t in targets])
    want_logs = sorted("%s.log" % t["bridge_job"] for t in targets)
    probs = []
    try:
        host = sorted(os.listdir(inputs["host"]))
    except OSError:
        host = []
    try:
        logs = sorted(os.listdir(inputs["logs"]))
    except OSError:
        logs = []
    for name, got, want in (("records", host, want_host), ("logs", logs, want_logs)):
        miss, extra = [x for x in want if x not in got], [x for x in got if x not in want]
        if miss or extra:
            probs.append("%s missing %s, unexpected %s" % (name, miss, extra))
    try:
        recs = load_raw(inputs["download_record"])[1]
        ids = [str(r.get("job_id")) for r in recs.get("logs", []) if isinstance(r, dict)]
    except Exception:  # noqa: BLE001 - an unreadable record is reported by the target's own checks too
        ids = None
    if ids is None:
        probs.append("download record unreadable")
    else:
        want = [t["bridge_job"] for t in targets]
        dup = sorted({i for i in ids if ids.count(i) > 1})
        if dup or sorted(ids) != sorted(want):
            probs.append("download record jobs %s, listed %s" % (sorted(ids), sorted(want)))
    return "; ".join(probs) or None


def run_set_problem(verdicts, runs, expected_ids):
    """None when the runs are exactly the expected run ids, each once, and each carries a verdict; else why not."""
    if not isinstance(runs, dict) or not isinstance(verdicts, dict) or not runs or not expected_ids:
        return "no runs"
    ids = [str(cfg.get("run_id")) if isinstance(cfg, dict) else None for cfg in runs.values()]
    dup = sorted({i for i in ids if ids.count(i) > 1}, key=str)
    if dup:
        return "run %s appears more than once" % ", ".join(map(str, dup))
    missing = [i for i in expected_ids if i not in ids]
    extra = [i for i in ids if i not in expected_ids]
    if missing or extra:
        return "runs missing %s, unexpected %s" % (missing, extra)
    if set(verdicts) != set(runs):
        return "verdicts for %s, runs %s" % (sorted(verdicts), sorted(runs))
    return None


def overall(verdicts, runs, expected_ids):
    """HOLDS only when the runs are exactly the expected ones, each once, each with an explicit HOLDS."""
    known = ("HOLDS", "FAILS", "UNVERIFIED")
    if run_set_problem(verdicts, runs, expected_ids) is not None:
        return "UNVERIFIED"
    if any(verdicts.get(k) == "FAILS" for k in runs):
        return "FAILS"
    if any(verdicts.get(k) not in known for k in runs):
        return "UNVERIFIED"
    return "HOLDS" if all(verdicts[k] == "HOLDS" for k in runs) else "UNVERIFIED"


def assemble(exs, inputs, tdoc, out=None, env=None):
    """Prints the checks, the tables, the results and the verdict line; returns the exit code."""
    out = out or sys.stdout
    P = lambda s="": print(s, file=out)  # noqa: E731
    targets = tdoc["targets"]
    runs = {t["label"]: t for t in targets}
    expected = [t["run_id"] for t in targets]
    P("KTOKEN-MAXCONE-1 exact-head bridge extraction (assembler blob %s; extractor %s at %s; cross-check %s at %s)"
      % (own_blob("assemble_evidence.py")[:12], EXTRACTOR[1][:12], EXTRACTOR[0][:12], CROSS[1][:12], CROSS[0][:12]))
    P("TARGETS sha256=%s blob=%s %s" % (tdoc["sha256"], tdoc["blob"], " ".join(
        "%s:run=%s,commit=%s,job=%s" % (t["label"], t["run_id"], t["commit"][:12], t["bridge_job"]) for t in targets)))
    verdicts, texts = {}, {}
    for t in targets:
        key = t["label"]
        show = {}
        try:
            C, res, show = assemble_target(t, exs, inputs, env)
            if res is not None:
                text = canonical(res)
                hits = scan(text)
                C("output: credential, signed-URL, IP and e-mail scan of the result", not hits, str(hits[:3]))
                if not hits:
                    texts[key] = (res, text)
        except Exception as e:  # noqa: BLE001 - a target whose assembly stopped is unverified, never held
            C = Checks(key)
            C.unverified.append("assembly stopped: %s: %s" % (type(e).__name__, str(e)[:200]))
            texts.pop(key, None)
        for name, ok, detail in C.items:
            P("CHECK %s %s %s%s" % (key, "ok  " if ok else "FAIL", name, (" -- " + redact(detail)) if detail and not ok else ""))
        for u in C.unverified:
            P("CHECK %s UNVERIFIED %s" % (key, redact(u)))
        verdicts[key] = C.verdict()
        P("RESULT %s %s %s (%d checks, %d failed)" % (key, t["path"], verdicts[key], len(C.items), len(C.failed)))
        cr = show.get("cross")
        if cr:
            o = cr["obs"]
            P("CROSSCHECK %s lines=%d byte_order_mark=%s carriage_returns=%d%s" % (
                key, cr["lines"], cr["bom"], cr["cr"],
                "" if not o else " session_original_length=%d %s; last %d lines %s the session's served text" % (
                    o["original_lines"], "equal" if cr["lines"] == o["original_lines"] else "DIFFERS", o["tail_lines"],
                    "equal to" if cr["tail_same"] else "DIFFER FROM")))
            P("CROSSCHECK %s distinct short names reported in the Build section: %d; the gate's lean-axioms summary: %r"
              % (key, cr["short_names"], redact(cr["gate_axioms"])))
        for l in show.get("gate", []):
            P("GATE %s | %s" % (key, redact(l)))
        if show.get("table"):
            tab = show["table"]
            P("AXIOMS %s files=%d prints=%d reports=%d unclosed=%d" % (
                key, len(tab), sum(x["prints"] for x in tab), sum(x["reports"] for x in tab), sum(x["unclosed"] for x in tab)))
            for x in tab:
                P("AXIOMS %s %s prints=%d reports=%d unclosed=%d sets=%s" % (
                    key, x["module"], x["prints"], x["reports"], x["unclosed"], json.dumps(x["sets"], sort_keys=True)))
    for t in targets:
        key = t["label"]
        if key in texts and verdicts[key] == "HOLDS":
            res, text = texts[key]
            c = compact(res)
            parts = chunks(c)
            P(BEGIN % (key, t["path"], len(parts)))
            for i, p in enumerate(parts, 1):
                P("RJ %s %04d %s" % (key, i, p))
            P(END % (key, t["path"]))
            P("SHA256 %s %s canonical=%s bytes=%d compact=%s" % (key, t["path"], sha256(text.encode("ascii")), len(text),
                                                                  sha256(c.encode("ascii"))))
    v = overall(verdicts, runs, expected)
    problem = run_set_problem(verdicts, runs, expected) or inventory_problem(targets, inputs)
    if problem is not None:
        P("CHECK all UNVERIFIED the run set: %s" % redact(problem))
        if v == "HOLDS":
            v = "UNVERIFIED"
    P("EXTRACT %s" % v)
    return {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[v]


def run_all(exs, inputs, tdoc, out=None, env=None):
    """The assembly; a verdict line is printed whatever is raised."""
    out = out or sys.stdout
    try:
        return assemble(exs, inputs, tdoc, out, env)
    except Exception as e:  # noqa: BLE001
        print("CHECK all UNVERIFIED stopped: %s: %s" % (type(e).__name__, redact(str(e))[:200]), file=out)
        print("EXTRACT UNVERIFIED", file=out)
        return 2


# ------------------------------------------------------------------------------------------------ reassembly

def reassemble(served_text, label):
    """From a job log as served (timestamps or not): (canonical text, path); Unverified on any mismatch."""
    lines = [TS.sub("", l, count=1) for l in served_text.replace("\r\n", "\n").split("\n")]
    begins = [(i, BEGIN_RX.match(l)) for i, l in enumerate(lines)]
    begins = [(i, m) for i, m in begins if m and m.group(1) == label]
    if len(begins) != 1:
        raise Unverified("%d BEGIN lines for %s" % (len(begins), label))
    i0, m = begins[0]
    path, k = m.group(2), int(m.group(3))
    pref = "RJ %s " % label
    payload, n = [], 0
    j = i0 + 1
    while j < len(lines) and lines[j].startswith(pref):
        n += 1
        num, _, piece = lines[j][len(pref):].partition(" ")
        if num != "%04d" % n:
            raise Unverified("line %d of the result is numbered %r" % (n, num))
        payload.append(piece)
        j += 1
    if n != k or j >= len(lines) or lines[j] != END % (label, path):
        raise Unverified("%d of %d numbered lines, then %r" % (n, k, lines[j][:80] if j < len(lines) else None))
    shas = [l for l in lines[j + 1:j + 2] if l.startswith("SHA256 %s %s " % (label, path))]
    sm = re.match(r"^SHA256 \S+ \S+ canonical=([0-9a-f]{64}) bytes=(\d+) compact=([0-9a-f]{64})$", shas[0]) if shas else None
    if not sm:
        raise Unverified("no SHA256 line after the result")
    c = "".join(payload)
    if sha256(c.encode("ascii")) != sm.group(3):
        raise Unverified("the compact text does not match its sha256")
    text = canonical(json.loads(c))
    if sha256(text.encode("ascii")) != sm.group(1) or len(text) != int(sm.group(2)):
        raise Unverified("the canonical text does not match its sha256")
    return text, path


# ------------------------------------------------------------------------------------------------ self-test

def _ts(i):
    return "2026-10-18T20:%02d:%02d.%07dZ " % (i // 3600 % 60, i // 60 % 60, i * 7919 % 10000000)


def _sources(kind, mut):
    """Synthetic sources: OIBridge.lean (3 prints), OIBridge/A.lean (3 prints, one primed), and for kind E the
    KTokenMaxCone module (4 prints)."""
    files = {
        "OIBridge.lean": "import OIBridge.A\n\n#print axioms r0\n#print axioms r1\n#print axioms r2\n",
        "OIBridge/A.lean": "namespace OIBridge.A\ntheorem a0 : True := trivial\n\n#print axioms a0\n#print axioms a1'\n"
                           "#print axioms a2\nend OIBridge.A\n",
        "OIBridge/NoPrints.lean": "namespace OIBridge.NoPrints\nend OIBridge.NoPrints\n",
    }
    if kind == "E":
        files[KTOKEN] = "namespace OIBridge.KTokenMaxCone\n\n#print axioms k0\n#print axioms k1\n\n#eval 0\n#print axioms k2\n" \
                        "#print axioms k3\nend OIBridge.KTokenMaxCone\n"
    files.update(mut.get("source_edit", {}))
    out = {LEAN_DIR + f: s for f, s in files.items() if s is not None}
    out[GATE_SOURCE] = mut.get("gate_source", "checks = [] # fixture gate\n")
    return out


def _report(mod, line, name, ax="propext, Classical.choice, Quot.sound"):
    tail = "does not depend on any axioms" if ax is None else "depends on axioms: [%s]" % ax
    return "info: %s:%d:0: '%s' %s" % (mod, line, name, tail)


def _bridge_lines(head, srcs, kind, variant=0, mut=None):
    mut = mut or {}
    L = ["Current runner version: '2.337.0'", "Worker ID: {%d}" % variant, "Complete job name: " + JOB_BRIDGE,
         "##[group]Run actions/checkout@v4", "##[endgroup]", "[command]/usr/bin/git log -1 --format=%H",
         mut.get("head", head), "##[group]Run actions/cache@v4", "##[endgroup]"]
    if variant:
        L += ["Cache restored from key: oibridge-Linux-%d" % variant]
    L += [HDR_BUILD, "\x1b[36;1mlean --version\x1b[0m", "shell: /usr/bin/bash -e {0}", "##[endgroup]",
          "Lean (version 4.0.0, x86_64-unknown-linux-gnu, Release)",
          "\u26a0 [%d/3653] Built OIBridge.A (%d.%ds)" % (3651 - variant, 6 + variant, variant)]
    for path in sorted(srcs):
        if not path.startswith(LEAN_DIR) or not path.endswith(".lean"):
            continue
        mod = path[len(LEAN_DIR):]
        ns = "OIBridge.X" if mod == "OIBridge.lean" else mod[:-5].replace("/", ".")
        for i, l in enumerate(srcs[path].split("\n")):
            m = re.match(r"^#print axioms (\S+)$", l)
            if not m:
                continue
            nm = "%s.%s" % (ns, m.group(1))
            if (mod, m.group(1)) in mut.get("drop", []):
                continue
            ax = mut.get("axioms", {}).get(m.group(1), "propext, Classical.choice, Quot.sound")
            if m.group(1) == "a2" and ax == "propext, Classical.choice, Quot.sound":
                # a list wrapped over three lines, as Lean prints a long one
                L += [_report(mod, i + 1, nm, "propext,")[:-1], " Classical.choice,", " Quot.sound]"]
            else:
                L.append(_report(mod, i + 1, nm, ax))
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
    if kind == "E" or mut.get("a3"):
        # check A3's step at E: its mutations print errors and direct reports, outside the sections read here
        L += ["##[group]Run lake env python3 -I -B ../programmes/oi-qm/reconstruction/round-ktoken-maxcone-1/checks/"
              "run_checks.py run", "\x1b[36;1mlake env python3 ...\x1b[0m", "##[endgroup]", "##[group]M_iff (exit 1)",
              "/tmp/x/M_iff.lean:3:0: error: DEPCHECK FAIL", "'OIBridge.KTokenPairCheck.x' depends on axioms: [propext]",
              "##[endgroup]", "OK   M_iff expected fail", "A3-CHECK-NONVACUOUS: 13 cases as expected"]
    L += mut.get("after_gate", [])
    L += ["Post job cleanup.", "Cache hit occurred on the primary key oibridge-Linux-abc%d, not saving cache." % variant,
          "Post job cleanup.", "[command]/usr/bin/git version", "Cleaning up orphan processes",
          "##[warning]Node.js 20 is deprecated."]
    if mut.get("truncate"):
        L = L[mut["truncate"]:]
    return L


def _write_log(path, lines, variant):
    text = "\ufeff" + "\n".join(_ts(i + 1000 * variant) + l for i, l in enumerate(lines)) + "\n"
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    return {"job_id": os.path.basename(path)[:-4], "outcome": "ok", "bytes": len(data), "sha256": sha256(data),
            "lines": data.count(b"\n")}


def _git_commit(repo, files):
    env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
    if not os.path.isdir(repo):
        os.makedirs(repo)
        subprocess.run(["git", "-C", repo, "init", "-q"], check=True, capture_output=True, env=env, timeout=60)
    subprocess.run(["git", "-C", repo, "rm", "-rq", "--ignore-unmatch", "."], check=True, capture_output=True, env=env)
    for rel, text in files.items():
        p = os.path.join(repo, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(text)
    for args in (["add", "-A"], ["-c", "user.name=selftest", "-c", "user.email=selftest@example.invalid",
                                 "-c", "commit.gpgsign=false", "commit", "-q", "--allow-empty", "-m", "fixture"]):
        subprocess.run(["git", "-C", repo] + args, check=True, capture_output=True, env=env, timeout=60)
    return subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], check=True, capture_output=True, text=True,
                          env=env).stdout.strip()


FIXTURE_KINDS = {"F": ("1000000901", "2000009101"), "E": ("1000000902", "2000009102")}


def _fixture(base, kinds=("F",), variant=0, mut=None):
    """A complete synthetic input set under base: (inputs, tdoc)."""
    mut = mut or {}
    os.makedirs(base)
    repo = os.path.join(base, "objects")
    host, logs = os.path.join(base, "host"), os.path.join(base, "logs")
    os.makedirs(host)
    os.makedirs(logs)
    targets, recs = [], []
    for kind in kinds:
        mk = mut.get(kind, {})
        srcs = _sources(kind, mk)
        head = _git_commit(repo, srcs)
        rid, jid = FIXTURE_KINDS[kind]
        t = {"label": kind, "kind": "bridge", "run_id": rid, "commit": head, "bridge_job": jid,
             "path": "evidence/%s-run/results.json" % kind.lower()}
        if kind == "F":
            t["session_observation"] = {"original_lines": 0, "tail_lines": 5, "tail_sha256": "0" * 64}
        targets.append(t)
        run = {"id": int(rid), "head_sha": head, "run_attempt": 1, "event": "workflow_dispatch", "head_branch": "draft/x",
               "conclusion": mk.get("run_conclusion", "success"), "path": WORKFLOW, "created_at": _ts(variant)}
        bsteps = [{"number": i + 1, "name": s, "conclusion": "success"}
                  for i, s in enumerate(["Set up job", "Run actions/checkout@v4", STEP_BUILD, STEP_GATE, "Complete job"])]
        job = {"id": int(jid), "name": JOB_BRIDGE, "conclusion": "success", "head_sha": head, "run_id": int(rid),
               "run_attempt": 1, "steps": bsteps}
        jobs = [json.loads(json.dumps(job)), {"id": int(jid) + 50, "name": "Numerical probes", "conclusion": mk.get("other_job", "success"),
                            "head_sha": head, "run_id": int(rid), "run_attempt": 1, "steps": []}]
        for edit in mk.get("run_edits", []):
            edit(run)
        for edit in mk.get("job_edits", []):
            edit(job)
        jobsd = {"total_count": len(jobs), "jobs": jobs}
        for edit in mk.get("jobs_edits", []):
            edit(jobsd)
        for name, obj, rawkey in (("run-%s.json" % rid, run, "run_raw"), ("job-%s.json" % jid, job, "job_raw"),
                                  ("jobs-%s.json" % rid, jobsd, "jobs_raw")):
            if name.startswith("jobs") and mk.get("drop_jobs_json"):
                continue
            b = json.dumps(obj).encode()
            with open(os.path.join(host, name), "wb") as f:
                f.write(mk[rawkey](b) if rawkey in mk else b)
        lines = _bridge_lines(head, srcs, kind, variant, mk.get("bridge"))
        rec = _write_log(os.path.join(logs, jid + ".log"), lines, variant)
        recs.append(rec)
        if kind == "F":
            with open(os.path.join(logs, jid + ".log"), "rb") as f:
                text = f.read().decode("utf-8")
            whole = text.split("\n")[:-1]
            t["session_observation"] = {"original_lines": len(whole), "tail_lines": 5,
                                        "tail_sha256": sha256("\n".join(whole[-5:]).encode())}
    for r in recs:
        if mut.get("bad_record") == r["job_id"]:
            r["sha256"] = "0" * 64
    for edit in mut.get("record_edits", []):
        edit(recs)
    rec_path = os.path.join(base, "download-record.json")
    body = json.dumps({"logs": recs}).encode()
    with open(rec_path, "wb") as f:
        f.write(mut["record_raw"](body) if "record_raw" in mut else body)
    for name, data in mut.get("extra_files", {}).items():
        with open(os.path.join(base, name), "wb") as f:
            f.write(data)
    doc = {"schema": T.SCHEMA, "version": 1, "repo": REPO, "round": ROUND, "targets": targets}
    for edit in mut.get("targets_edits", []):
        edit(doc)
    tdoc = T.parse(json.dumps(doc).encode())
    gate_blob = git_blob_id(_sources("F", {}).get(GATE_SOURCE).encode())
    return {"objects": Objects(repo), "host": host, "logs": logs, "download_record": rec_path}, tdoc, gate_blob


def self_test(objects_path, work=None):
    base = tempfile.mkdtemp(prefix="assemble-selftest-", dir=work)
    fails, n = 0, 0
    saved = dict(GATE_STEPS_BY_BLOB)
    try:
        objs = Objects(objects_path)
        exs = {"main": load_extractor(objs, EXTRACTOR, ("extract", "check", "strip", "MARKERS")),
               "cross": load_extractor(objs, CROSS, ("extract", "strip", "MARKERS"))}

        def run_case(name, mut, want, needle=None, variant=0, kinds=("F",), tdoc_edit=None):
            nonlocal fails, n
            n += 1
            d = os.path.join(base, "c%03d" % n)
            try:
                inputs, tdoc, gblob = _fixture(d, kinds, variant, mut)
            except T.TargetsError as e:
                text = "CHECK all UNVERIFIED targets refused: %s\nEXTRACT UNVERIFIED\n" % e
                code = 2
            else:
                GATE_STEPS_BY_BLOB[gblob] = GATE_STEPS
                if tdoc_edit:
                    tdoc = tdoc_edit(tdoc)
                buf = io.StringIO()
                code = run_all(exs, inputs, tdoc, out=buf, env={"GITHUB_RUN_ID": "1", "GITHUB_RUN_ATTEMPT": "1"})
                text = buf.getvalue()
            verdict = text.strip().split("\n")[-1]
            ok = verdict == "EXTRACT " + want and (needle is None or needle in text)
            # a target that does not hold never has its result printed
            for lab in ("F", "E", "G"):
                if not re.search(r"(?m)^RESULT %s \S+ HOLDS " % lab, text):
                    ok = ok and ("===== BEGIN EXPECTED RESULT %s " % lab) not in text
            ok = ok and code == {"HOLDS": 0, "FAILS": 1, "UNVERIFIED": 2}[want]
            print("  %s  %s -> %s" % ("ok  " if ok else "FAIL", name, verdict))
            if not ok:
                fails += 1
                print("\n".join("        | " + l for l in text.split("\n")
                                if re.match(r"^(CHECK \S+ (FAIL|UNVERIFIED)|RESULT )", l))[:3000])
            return text

        def blocks(t):
            res = {}
            for lab in ("F", "E"):
                try:
                    res[lab] = reassemble(t, lab)
                except Unverified:
                    pass
            return res

        def extra(name, ok):
            nonlocal fails, n
            n += 1
            fails += not ok
            print("  %s  %s" % ("ok  " if ok else "FAIL", name))

        print("assemble self-test (synthetic fixtures, local git repositories, no network):")
        t0 = run_case("a clean F-shape fixture holds (KTokenMaxCone absent, a primed and a wrapped report)", {}, "HOLDS")
        t1 = run_case("the same evidence with other timestamps, durations, cache lines and job counts holds", {}, "HOLDS",
                      variant=3)
        b0, b1 = blocks(t0), blocks(t1)
        r0 = json.loads(b0["F"][0]) if "F" in b0 else {}
        r1 = json.loads(b1["F"][0]) if "F" in b1 else {}
        extra("the expected sections are identical across the two variants", r0 and r0.get("expected") == r1.get("expected"))
        extra("each result reassembles from the served lines to canonical ASCII JSON matching both digests",
              "F" in b0 and b0["F"][0] == canonical(r0) and b0["F"][0].isascii() and b0["F"][1] == "evidence/f-run/results.json")
        extra("the result has the f-run schema: gaps empty, KTokenMaxCone absent, OIBridge.lean complete, window [1, N]",
              r0.get("gaps") == [] and r0["expected"]["modules"][KTOKEN]["status"] == "absent"
              and r0["expected"]["modules"]["OIBridge.lean"]["status"] == "complete"
              and r0["source"]["served_window"] == [1, r0["source"]["original_lines"]]
              and r0["expected"]["gate"]["steps_total"] == 22 and r0["schema"] == "oi-evidence-result")
        extra("no timestamp, cache line or build-job count in the expected section",
              r0 and "2026-10-18T" not in json.dumps(r0["expected"]) and "Cache" not in json.dumps(r0["expected"])
              and "3653" not in json.dumps(r0["expected"]))
        extra("the session cross-check line reports equal length and tail", "session_original_length=" in t0
              and "equal; last 5 lines equal to the session's served text" in t0)
        extra("the gate block and the axiom table are printed", "GATE F | release gate: PASS" in t0
              and "AXIOMS F OIBridge/A.lean prints=3 reports=3 unclosed=0" in t0)
        te = run_case("an E-shape fixture holds (KTokenMaxCone present, check A3's step after the gate)", {}, "HOLDS",
                      kinds=("E",))
        re_ = json.loads(blocks(te)["E"][0]) if "E" in blocks(te) else {}
        extra("E's result records KTokenMaxCone complete with its 4 reports",
              re_ and re_["expected"]["modules"][KTOKEN]["status"] == "complete" and len(re_["expected"]["modules"][KTOKEN]["reports"]) == 4)
        tfe = run_case("F and E listed together both hold", {}, "HOLDS", kinds=("F", "E"))
        extra("both results print, each once", tfe.count("===== BEGIN EXPECTED RESULT F ") == 1
              and tfe.count("===== BEGIN EXPECTED RESULT E ") == 1)

        run_case("no build line", {"F": {"bridge": {"drop_build": True}}}, "FAILS", "FAIL build: 'Build completed")
        run_case("no gate block", {"F": {"bridge": {"drop_gate": True}}}, "FAILS", "FAIL gate: a release-gate block")
        run_case("a failing gate verdict", {"F": {"bridge": {"gate_verdict": "FAIL", "gate_status": "FAIL"}}}, "FAILS",
                 "FAIL gate: verdict PASS")
        G = "FAIL gate: exactly the 22 steps"
        run_case("a gate block with one step line deleted", {"F": {"bridge": {"gate_drop_step": "voice"}}}, "FAILS", G)
        run_case("a gate block with an extra step line", {"F": {"bridge": {"gate_extra_steps": ["extra-step"]}}}, "FAILS", G)
        run_case("a gate block with a step line repeated", {"F": {"bridge": {"gate_extra_steps": ["voice"]}}}, "FAILS", G)
        run_case("a release gate source whose step list is not pinned", {"F": {"gate_source": "checks = [1]\n"}},
                 "UNVERIFIED", "whose step list is not pinned")
        run_case("a governed report missing", {"F": {"bridge": {"drop": [("OIBridge.lean", "r1")]}}}, "FAILS",
                 "FAIL OIBridge.lean: one report per")
        run_case("a non-governed report missing (the check over every file)", {"F": {"bridge": {"drop": [("OIBridge/A.lean", "a0")]}}},
                 "FAILS", "FAIL reports: extract_result.check")
        run_case("the primed report missing", {"F": {"bridge": {"drop": [("OIBridge/A.lean", "a1'")]}}}, "FAILS",
                 "missing-report: OIBridge/A.lean:5")
        run_case("an axiom outside the permitted three", {"F": {"bridge": {"axioms": {"r0": "propext, Lean.trustCompiler"}}}},
                 "FAILS", "FAIL OIBridge.lean: every axiom")
        run_case("a sorryAx report in a non-governed module", {"F": {"bridge": {"axioms": {"a0": "propext, sorryAx"}}}},
                 "FAILS", "FAIL markers: none in the Build")
        run_case("an error line in the Build section", {"F": {"bridge": {"build_extra": ["error: OIBridge/X.lean:1:0: boom"]}}},
                 "FAILS", "FAIL markers: none in the Build")
        run_case("a report of a file with no #print axioms command",
                 {"F": {"bridge": {"build_extra": [_report("OIBridge/NoPrints.lean", 1, "OIBridge.NoPrints.z")]}}},
                 "FAILS", "FAIL reports: every module reported")
        run_case("a direct report in the Build section", {"F": {"bridge": {"build_extra": ["'OIBridge.Z' depends on axioms: [propext]"]}}},
                 "FAILS", "FAIL reports: no direct")
        run_case("a KTokenMaxCone report while the module is absent",
                 {"F": {"bridge": {"after_gate": [_report(KTOKEN, 3, "OIBridge.KTokenMaxCone.k0")]}}}, "FAILS",
                 "FAIL OIBridge/KTokenMaxCone.lean: absent")
        run_case("a governed primed name the cross-check extractor cannot read",
                 {"F": {"source_edit": {"OIBridge.lean": "import OIBridge.A\n\n#print axioms r0\n#print axioms r1'\n"}}},
                 "FAILS", "FAIL cross-check")
        run_case("a job that did not succeed", {"F": {"other_job": "failure"}}, "FAILS", "FAIL jobs: every job success")
        run_case("a run that did not succeed", {"F": {"run_conclusion": "failure"}}, "FAILS", "FAIL run: id, head")
        run_case("a run of another workflow", {"F": {"run_edits": [lambda r: r.update(path=".github/workflows/x.yml")]}},
                 "FAILS", "FAIL run: id, head")
        run_case("a job record whose steps differ from the list's",
                 {"F": {"job_edits": [lambda j: j["steps"].pop(0)]}}, "FAILS", "FAIL job record: its steps")
        run_case("a Release gate step that did not succeed",
                 {"F": {"job_edits": [lambda j: j["steps"][3].update(conclusion="failure")],
                        "jobs_edits": [lambda d: d["jobs"][0]["steps"][3].update(conclusion="failure")]}}, "FAILS",
                 "FAIL bridge step 'Release gate' success")
        run_case("a log checked out at another head", {"F": {"bridge": {"head": "f" * 40}}}, "FAILS",
                 "FAIL bridge log: checked-out head")
        run_case("a truncated log (a served tail)", {"F": {"bridge": {"truncate": 9}}}, "FAILS", "FAIL bridge log: complete")
        run_case("a credential-shaped string in the result",
                 {"F": {"bridge": {"gate_summary_extra": " (contact someone@example.com)"}}}, "FAILS", "FAIL output: credential")
        U = "UNVERIFIED "
        run_case("a log that does not match its download record", {"bad_record": "2000009101"}, "UNVERIFIED",
                 U + "log 2000009101.log does not match its download record")
        run_case("a missing jobs record", {"F": {"drop_jobs_json": True}}, "UNVERIFIED", U + "jobs-1000000901.json unreadable")
        run_case("a truncated run record", {"F": {"run_raw": lambda b: b[:len(b) // 2]}}, "UNVERIFIED",
                 U + "run-1000000901.json unreadable: JSONDecodeError")
        run_case("a job record that is a list", {"F": {"job_raw": lambda b: b"[1]"}}, "UNVERIFIED",
                 U + "malformed record: job-2000009101.json is not a JSON object")
        run_case("a run record without head_sha", {"F": {"run_edits": [lambda r: r.pop("head_sha")]}}, "UNVERIFIED",
                 U + "malformed record: run-1000000901.json lacks head_sha")
        run_case("a run attempt given as true", {"F": {"run_edits": [lambda r: r.update(run_attempt=True)]}}, "UNVERIFIED",
                 U + "malformed record: run-1000000901.json field run_attempt is bool")
        run_case("a jobs list holding null", {"F": {"jobs_edits": [lambda d: d["jobs"].insert(0, None)]}}, "UNVERIFIED",
                 U + "malformed record: jobs-1000000901.json job 0 is not a JSON object")
        run_case("a download entry without sha256", {"record_edits": [lambda r: r[0].pop("sha256")]}, "UNVERIFIED",
                 U + "malformed record: download record entry 0 lacks sha256")
        run_case("a download record that is a list", {"record_raw": lambda b: b"[]"}, "UNVERIFIED",
                 U + "malformed record: the download record is not a JSON object")
        # the run set: exactly the listed runs, each once
        V = "CHECK all UNVERIFIED the run set: "
        run_case("an unlisted run's records among the inputs", {"extra_files": {"host/run-1000000903.json": b"{}"}}, "UNVERIFIED",
                 V + "records missing [], unexpected ['run-1000000903.json']")
        run_case("an unlisted job's log among the inputs", {"extra_files": {"logs/2000009103.log": b"x"}}, "UNVERIFIED",
                 V + "logs missing [], unexpected ['2000009103.log']")
        run_case("a download record naming an unlisted job",
                 {"record_edits": [lambda r: r.append(dict(r[0], job_id="2000009103"))]}, "UNVERIFIED",
                 V + "download record jobs ['2000009101', '2000009103'], listed ['2000009101']")
        run_case("a listed run whose records are missing", {"F": {"drop_jobs_json": True}}, "UNVERIFIED",
                 V + "records missing ['jobs-1000000901.json']")
        run_case("a run listed twice in targets.json",
                 {"targets_edits": [lambda d: d["targets"].append(dict(d["targets"][0], label="G"))]}, "UNVERIFIED",
                 "targets refused: run 1000000901 is listed more than once")
        run_case("an empty target list", {"targets_edits": [lambda d: d.update(targets=[])]}, "UNVERIFIED",
                 "targets refused")
        run_case("a listed run with no inputs at all (E listed, only F's inputs)", {}, "UNVERIFIED",
                 V + "records missing", tdoc_edit=lambda td: dict(td, targets=td["targets"] + [
                     {"label": "E", "kind": "bridge", "run_id": "1000000902", "commit": td["targets"][0]["commit"][::-1],
                      "bridge_job": "2000009102", "path": "evidence/e-run/results.json"}]))
        real = globals()["assemble_target"]

        def stopping(t, exs_, inputs_, env_=None):
            raise RuntimeError("fixture stop")
        globals()["assemble_target"] = stopping
        try:
            run_case("a target whose assembly raises", {}, "UNVERIFIED", U + "assembly stopped: RuntimeError: fixture stop")
        finally:
            globals()["assemble_target"] = real
        E2 = ["1", "2"]
        two = {"F": {"run_id": "1"}, "E": {"run_id": "2"}}
        h = {"F": "HOLDS", "E": "HOLDS"}
        extra("the verdict rule refuses an empty set, a missing run, an extra run and a duplicate, and holds on the listed two",
              overall({}, {}, E2) == "UNVERIFIED" and overall(h, two, []) == "UNVERIFIED"
              and overall({"F": "HOLDS"}, {"F": {"run_id": "1"}}, E2) == "UNVERIFIED"
              and overall(dict(h, G="HOLDS"), dict(two, G={"run_id": "3"}), E2) == "UNVERIFIED"
              and overall(dict(h, G="HOLDS"), dict(two, G={"run_id": "1"}), E2) == "UNVERIFIED"
              and overall(h, {"F": {"run_id": "1"}, "E": {"run_id": "1"}}, E2) == "UNVERIFIED"
              and overall(h, two, E2) == "HOLDS")
        extra("the whole holds only when every listed run carries an explicit HOLDS",
              overall({"F": "HOLDS"}, two, E2) == "UNVERIFIED" and overall({"F": "HOLDS", "E": None}, two, E2) == "UNVERIFIED"
              and overall({"F": "HOLDS", "E": "FAILS"}, two, E2) == "FAILS"
              and overall({"F": "UNVERIFIED", "E": "HOLDS"}, two, E2) == "UNVERIFIED")
        try:
            exec_extractor(b"MARKERS = {}\n", EXTRACTOR[1], ("extract",), "x")
            ok = False
        except Unverified:
            ok = True
        extra("an extractor other than the pinned blob is refused before it runs", ok)
        try:
            load_extractor(objs, (EXTRACTOR[0], CROSS[1]), ("extract",))
            ok = False
        except Unverified:
            ok = True
        extra("an extractor commit holding another blob than the pin is refused", ok)
        hits = scan('{\n "a": "ghp_' + "a" * 30 + '",\n "b": "https://x.blob.core.windows.net/c?sv=1&sig=2",\n'
                    ' "c": "10.1.2.3"\n}\n')
        extra("the scan finds a token, a signed URL and an IP address, and passes versions, digests and paths",
              [x[0] for x in hits] == [2, 3, 4] and not scan(canonical({"v": "4.21.0", "h": "0" * 64, "p": "a/b.lean:3:0"})))
        # reassembly: tampering, renumbering and truncation are refused
        if "F" in b0:
            served = t0
            ok = True
            for bad in (served.replace("RJ F 0002 ", "RJ F 0003 ", 1), served.replace("RJ F 0001 {", "RJ F 0001 [", 1),
                        "\n".join(l for l in served.split("\n") if not l.startswith("RJ F 0002 "))):
                try:
                    reassemble(bad, "F")
                    ok = False
                except (Unverified, ValueError):
                    pass
            stamped = "\n".join(_ts(i) + l for i, l in enumerate(served.split("\n")))
            ok = ok and reassemble(stamped, "F") == b0["F"]
        else:
            ok = False
        extra("reassembly refuses a renumbered, altered or missing line, and reads timestamped served lines", ok)
        pieces = chunks("ab   cd" * 60, 10)
        extra("no printed piece ends with a space and the pieces rejoin exactly",
              "".join(pieces) == "ab   cd" * 60 and all(not p.endswith(" ") for p in pieces[:-1]) and max(map(len, pieces)) <= 10)
    finally:
        GATE_STEPS_BY_BLOB.clear()
        GATE_STEPS_BY_BLOB.update(saved)
        shutil.rmtree(base, ignore_errors=True)
    print("assemble self-test: %d of %d cases ok" % (n - fails, n))
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--objects")
    ap.add_argument("--host")
    ap.add_argument("--logs")
    ap.add_argument("--download-record")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--work")
    ap.add_argument("--reassemble")
    ap.add_argument("--label")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    if a.reassemble:
        if not a.label:
            ap.error("--label is required with --reassemble")
        try:
            with open(a.reassemble, encoding="utf-8") as f:
                text, path = reassemble(f.read(), a.label)
        except (OSError, Unverified, ValueError) as e:
            print("reassembly failed: %s: %s" % (type(e).__name__, e), file=sys.stderr)
            return 2
        if a.out:
            with open(a.out, "x", encoding="ascii", newline="") as f:
                f.write(text)
        else:
            sys.stdout.write(text)
        print("reassembled %s %s sha256=%s" % (a.label, path, sha256(text.encode("ascii"))), file=sys.stderr)
        return 0
    if not a.objects:
        ap.error("--objects is required")
    if a.self_test:
        try:
            return 1 if self_test(a.objects, a.work) else 0
        except Unverified as e:
            print("assemble self-test: extractor refused: %s" % e)
            return 1
    if not (a.host and a.logs and a.download_record):
        ap.error("--host, --logs and --download-record are required")
    try:
        tdoc = T.load()
    except T.TargetsError as e:
        print("CHECK all UNVERIFIED targets refused: %s" % e)
        print("EXTRACT UNVERIFIED")
        return 2
    try:
        objs = Objects(a.objects)
        exs = {"main": load_extractor(objs, EXTRACTOR, ("extract", "check", "strip", "MARKERS")),
               "cross": load_extractor(objs, CROSS, ("extract", "strip", "MARKERS"))}
    except Exception as e:  # noqa: BLE001 - an extractor that cannot be read or verified leaves the run unverified
        print("CHECK all UNVERIFIED %s: %s" % (type(e).__name__, redact(str(e))[:200]))
        print("EXTRACT UNVERIFIED")
        return 2
    inputs = {"objects": objs, "host": a.host, "logs": a.logs, "download_record": a.download_record}
    return run_all(exs, inputs, tdoc)


if __name__ == "__main__":
    sys.exit(main())
