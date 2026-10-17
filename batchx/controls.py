#!/usr/bin/env python3
"""Controls for the batch extractor: an end-to-end pass, and code mutations each self-test must catch.

  python3 -I controls.py --extractor PATH [--work DIR]

1. End to end. assemble.py's own fixture shard is assembled with the given extractor, its output is timestamped and
   wrapped as the job-log tool serves a log, and collect.py's reader must accept it whole: every run usable, each
   collected block byte-identical to the block assemble.py printed. Served as a tail, it must be refused. This ties
   the collector to the assembler's real output rather than to the collector's own synthetic writer.
2. Mutations. Each entry changes one decisive line of assemble.py, host.py or collect.py in a copy of batchx/; the
   copy's self-test must then fail (the mutant is killed). The unmutated copy's self-tests must pass first, so a
   kill is not an artefact of the copy. A mutation whose text is not found exactly once is itself a failure.
3. Plan and pins (with --plan WORKFLOW). runs.json is the 223 runs, each once, in expiry order, in contiguous
   shards of at most shard_size; the three scripts pin its sha256 and assemble.py pins crosscheck.json's; the
   workflow's matrix lists exactly shards 1..N; it triggers only on a push to its own branch; its permissions are
   actions: read and contents: read and nothing else; every `uses:` is pinned by a full SHA and is actions/checkout;
   every checkout sets persist-credentials: false; GH_TOKEN is set once, on the host step, from github.token, and
   no other secret, artifact, cache or summary is named; every job and every step has timeout-minutes. Each rule has
   a negative control that edits the workflow text and must be caught.
Exit 0 when every part holds and every mutant is killed, 1 otherwise. Local and CI; no network.
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
import types

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ("assemble.py", "host.py", "collect.py", "runs.json", "crosscheck.json")

MUTANTS = [
    ("assemble.py", 'logged == head, logged[:12])', 'True, logged[:12])', "the head check is skipped"),
    ("assemble.py", 'm.group(2) == head\n                  and', 'True\n                  and',
     "a pull-request merge of any head is accepted"),
    ("assemble.py", 'and any(l == "Cleaning up orphan processes" for l in lg.s[-12:]),', 'and True,',
     "a log cut before its cleanup is accepted"),
    ("assemble.py", 'if run_set_problem(verdicts, runs, expected_ids) is not None:\n        return "UNVERIFIED"',
     'if False:\n        return "UNVERIFIED"', "the run-set rule is skipped"),
    ("assemble.py", "if fixed + used + n + 1 > budget:", "if False:", "the line budget is ignored"),
    ("assemble.py", 'C("gate: a PASS verdict under a successful Release gate step", gv and gv["pass"],',
     'C("gate: a PASS verdict under a successful Release gate step", True,', "a red verdict under a green step passes"),
    ("assemble.py", "    if unparsed:\n        gaps.append(", "    if False:\n        gaps.append(",
     "an unparsed report line is dropped silently"),
    ("assemble.py", "hits = scan(text)", "hits = []", "the credential scan is skipped"),
    ("assemble.py", 'C("build: no \'Build completed successfully\' line under a failed Build step", not built)',
     'C("build: no \'Build completed successfully\' line under a failed Build step", True)',
     "a build line under a failed step passes"),
    ("assemble.py", "if pinned and git_blob_id(data) != EXTRACT_RESULT_BLOB:", "if False:",
     "the extractor's blob is not checked"),
    ("assemble.py", 'C.need("format: one %s section for a step that ran" % nm,',
     'C("format: one %s section for a step that ran" % nm,', "an unknown format reads as FAILS (review note N3)"),
    ("assemble.py", 'return RUNNER_PATH.sub("", text).rstrip()', "return text.rstrip()",
     "runner paths stay in the error lines"),
    ("assemble.py", 'if bconc == "cancelled" and not gv:\n        outcome = "cancelled"',
     'if bconc == "cancelled" and not gv:\n        outcome = "gate-verdict"', "a cancelled run is labelled as reaching a verdict"),
    ("host.py", 'if kind == "log" and not u.query and u.path in t.log_paths:', 'if kind == "log":',
     "the log allow-list admits any job"),
    ("host.py", 'req2 = urllib.request.Request(loc, method="GET", headers={"User-Agent": UA})',
     'req2 = urllib.request.Request(loc, method="GET", headers={"User-Agent": UA, "Authorization": "Bearer " + token})',
     "the token is sent to the storage host"),
    ("host.py", 'if kind != "rate" and t.remaining is not None and t.remaining < t.reserve:', "if False:",
     "the rate-limit reserve is ignored for JSON reads"),
    ("host.py", "            if len(jobs) != total:", "            if False:", "a short jobs list is accepted"),
    ("collect.py", "    if len(raw) != orig:", "    if False:", "a served tail is accepted"),
    ("collect.py", 'sm.group(2) != hashlib.sha256(body.encode("utf-8")).hexdigest()', "False",
     "a block's digest is not checked"),
    ("collect.py", "if k is not None and k in shards:", "if False:", "a shard is collected twice"),
    ("collect.py", 'if res.get(rid) != "HOLDS":', "if False:", "a block of a run that does not hold is taken"),
]


def selftests(d, extractor, work):
    cmds = [[sys.executable, "-I", os.path.join(d, "assemble.py"), "--self-test", "--extractor", extractor, "--work", work],
            [sys.executable, "-I", os.path.join(d, "host.py"), "--self-test", "--work", work],
            [sys.executable, "-I", os.path.join(d, "collect.py"), "--self-test", "--work", work]]
    return [subprocess.run(c, capture_output=True, text=True, timeout=900).returncode for c in cmds]


def load(path, name):
    mod = types.ModuleType(name)
    mod.__file__ = path
    with open(path, "rb") as f:
        exec(compile(f.read(), path, "exec"), mod.__dict__)  # noqa: S102 - this directory's own sources
    return mod


def end_to_end(extractor, work):
    A = load(os.path.join(HERE, "assemble.py"), "assemble")
    K = load(os.path.join(HERE, "collect.py"), "collect")
    ex = A.load_extractor(extractor)
    base = tempfile.mkdtemp(prefix="controls-e2e-", dir=work)
    try:
        inputs, doc, xc = A._fixture(os.path.join(base, "f"), 0, {})
        buf = io.StringIO()
        code = A.run_all(ex, doc, 1, inputs, xc, out=buf)
        out = buf.getvalue()
        printed = dict(A._blocks(out))
        lines = ["Current runner version: '2.337.0'", "##[group]Run python3 -I batchx/assemble.py", "##[endgroup]"] \
            + out.rstrip("\n").split("\n") + ["Post job cleanup.", "Cleaning up orphan processes"]
        text = "\n".join("2026-12-01T10:%02d:%02d.1234567Z %s" % (i // 60 % 60, i % 60, l) for i, l in enumerate(lines))
        served = json.dumps({"job_id": 1, "logs_content": text, "original_length": len(lines)})
        k, probs, res = K.read_shard(served, doc)
        ok = code == 0 and k == 1 and not probs and sorted(res) == ["901", "902", "903"] and all(
            v == "HOLDS" and body == printed[rid] for rid, (v, body) in res.items())
        print("  %s  assemble.py's real output, served whole, is collected: 3 runs, blocks byte-identical%s"
              % ("ok  " if ok else "FAIL", "" if ok else " -- %s %s" % (code, probs[:3])))
        tail = json.dumps({"job_id": 1, "logs_content": "\n".join(text.split("\n")[5:]), "original_length": len(lines)})
        k2, probs2, _ = K.read_shard(tail, doc)
        ok2 = k2 is None and probs2 and "not whole" in probs2[0]
        print("  %s  the same output served as a tail is refused" % ("ok  " if ok2 else "FAIL"))
        return int(not ok) + int(not ok2)
    finally:
        shutil.rmtree(base, ignore_errors=True)


BRANCH = "tmp/ci-batch-extract-design-20261017"


def plan_problems(wf, runs_text, scripts, xc_text):
    """The static checks of part 3; returns a list of problems (empty when the plan holds)."""
    P = []
    # comment lines are prose; only the workflow's code lines are checked (an inline "# v4" after a pin is dropped)
    wf = "\n".join(re.sub(r"\s+#.*$", "", l) for l in wf.split("\n") if not l.lstrip().startswith("#")) + "\n"
    doc = json.loads(runs_text)
    rs = doc["runs"]
    ids = [r["run_id"] for r in rs]
    if len(rs) != 223 or len(set(ids)) != len(ids) or len({r["bridge_job_id"] for r in rs}) != len(rs):
        P.append("runs.json: not 223 distinct runs and jobs")
    if [r["expires"] for r in rs] != sorted(r["expires"] for r in rs):
        P.append("runs.json: not in expiry order")
    sh = [r["shard"] for r in rs]
    if sh != sorted(sh) or set(sh) != set(range(1, doc["shards"] + 1)) or \
            max(sh.count(k) for k in set(sh)) > doc["shard_size"]:
        P.append("runs.json: shards not contiguous 1..%s of at most %s" % (doc["shards"], doc["shard_size"]))
    digest = hashlib.sha256(runs_text.encode()).hexdigest()
    for name, text in scripts.items():
        if not re.search(r'^RUNS_SHA256 = "%s"$' % digest, text, re.M):
            P.append("%s does not pin runs.json's sha256" % name)
    if not re.search(r'^CROSSCHECK_SHA256 = "%s"$' % hashlib.sha256(xc_text.encode()).hexdigest(), scripts["assemble.py"], re.M):
        P.append("assemble.py does not pin crosscheck.json's sha256")
    m = re.findall(r"^\s+shard: \[([0-9, ]+)\]$", wf, re.M)
    if len(m) != 1 or [int(x) for x in m[0].split(",")] != list(range(1, doc["shards"] + 1)):
        P.append("workflow: the matrix does not list exactly shards 1..%d" % doc["shards"])
    on = re.search(r"^on:\n((?:  .*\n)+)", wf, re.M)
    if not on or on.group(1) != "  push:\n    branches: ['%s']\n" % BRANCH:
        P.append("workflow: the trigger is not a push to %s alone" % BRANCH)
    if wf.count("if: github.ref == 'refs/heads/%s'" % BRANCH) != 2:
        P.append("workflow: a job lacks the branch guard")
    perm = re.search(r"^permissions:\n((?:  .*\n)+)", wf, re.M)
    if not perm or perm.group(1) != "  actions: read\n  contents: read\n" or wf.count("permissions:") != 1:
        P.append("workflow: permissions are not exactly actions: read and contents: read")
    uses = re.findall(r"^\s+(?:- )?uses: (\S+)", wf, re.M)
    if not uses or any(not re.fullmatch(r"actions/checkout@[0-9a-f]{40}", u) for u in uses):
        P.append("workflow: an action is not actions/checkout pinned by a full SHA")
    if wf.count("persist-credentials: false") != len(uses):
        P.append("workflow: a checkout does not set persist-credentials: false")
    if wf.count("GH_TOKEN") != 1 or wf.count("${{ github.token }}") != 1 or "secrets." in wf:
        P.append("workflow: GH_TOKEN is not set exactly once from github.token, or a secret is named")
    tok = wf.find("GH_TOKEN: ${{ github.token }}")
    step = wf.rfind("- name:", 0, tok)
    if tok < 0 or "batchx/host.py" not in wf[step:wf.find("- name:", tok)]:
        P.append("workflow: GH_TOKEN is not on the host step")
    for bad in ("upload-artifact", "actions/cache", "GITHUB_STEP_SUMMARY", "GITHUB_OUTPUT", "GITHUB_ENV", "git push",
                "workflow_dispatch", "pull_request", "schedule:", "contents: write", "actions: write"):
        if bad in wf:
            P.append("workflow: names %s" % bad)
    jobs = re.split(r"^  (?=[a-z]+:\n    name:)", wf.split("\njobs:\n", 1)[1], flags=re.M)
    jobs = [j for j in jobs if j.strip()]
    for j in jobs:
        if "\n    timeout-minutes:" not in j:
            P.append("workflow: a job has no timeout-minutes")
        for st in re.split(r"^      - name:", j, flags=re.M)[1:]:
            if "timeout-minutes:" not in st:
                P.append("workflow: step %r has no timeout-minutes" % st.split("\n", 1)[0].strip()[:50])
    return P


def plan(path):
    fails = 0
    wf = open(path, encoding="utf-8").read()
    runs_text = open(os.path.join(HERE, "runs.json"), encoding="utf-8").read()
    xc_text = open(os.path.join(HERE, "crosscheck.json"), encoding="utf-8").read()
    scripts = {n: open(os.path.join(HERE, n), encoding="utf-8").read() for n in ("assemble.py", "host.py", "collect.py")}
    p = plan_problems(wf, runs_text, scripts, xc_text)
    print("  %s  the plan and pins hold%s" % ("ok  " if not p else "FAIL", "" if not p else ": " + "; ".join(p)))
    fails += bool(p)
    negs = [
        ("a shard dropped from the matrix", lambda w: w.replace(", 32]", "]")),
        ("a second trigger", lambda w: w.replace("on:\n  push:", "on:\n  workflow_dispatch:\n  push:")),
        ("a write permission", lambda w: w.replace("  contents: read\n", "  contents: write\n")),
        ("an action pinned by tag", lambda w: w.replace("actions/checkout@11d5960a326750d5838078e36cf38b85af677262", "actions/checkout@v4", 1)),
        ("a checkout keeping credentials", lambda w: w.replace("          persist-credentials: false", "          persist-credentials: true", 1)),
        ("the token on the assemble step", lambda w: w.replace("        if: ${{ !cancelled() }}\n        timeout-minutes: 8\n",
                                                             "        if: ${{ !cancelled() }}\n        timeout-minutes: 8\n"
                                                             "        env:\n          GH_TOKEN: ${{ github.token }}\n")),
        ("an artifact upload", lambda w: w + "      - name: up\n        timeout-minutes: 1\n        uses: actions/upload-artifact@"
                                         + "0" * 40 + "\n"),
        ("a step without a timeout", lambda w: w.replace("        timeout-minutes: 8\n", "", 1)),
        ("a job without a timeout", lambda w: w.replace("    timeout-minutes: 25\n", "", 1)),
        ("a job without the branch guard", lambda w: w.replace("    if: github.ref == 'refs/heads/%s'\n" % BRANCH, "", 1)),
    ]
    for name, edit in negs:
        w2 = edit(wf)
        caught = w2 != wf and bool(plan_problems(w2, runs_text, scripts, xc_text))
        print("  %s  plan negative control: %s is caught" % ("ok  " if caught else "FAIL", name))
        fails += not caught
    s2 = dict(scripts, **{"collect.py": scripts["collect.py"].replace("RUNS_SHA256 = \"", "RUNS_SHA256 = \"0", 1)})
    caught = bool(plan_problems(wf, runs_text, s2, xc_text))
    print("  %s  plan negative control: a script pinning another runs.json is caught" % ("ok  " if caught else "FAIL"))
    fails += not caught
    r2 = json.loads(runs_text)
    r2["runs"] = r2["runs"][1:]
    caught = bool(plan_problems(wf, json.dumps(r2, indent=1, sort_keys=True) + "\n", scripts, xc_text))
    print("  %s  plan negative control: a run dropped from runs.json is caught" % ("ok  " if caught else "FAIL"))
    fails += not caught
    return fails


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--extractor", required=True)
    ap.add_argument("--plan", help="the workflow file, for part 3")
    ap.add_argument("--work")
    a = ap.parse_args(argv)
    extractor = os.path.abspath(a.extractor)
    work = tempfile.mkdtemp(prefix="controls-", dir=a.work)
    fails = 0
    try:
        print("controls (local, no network):")
        if a.plan:
            fails += plan(a.plan)
        fails += end_to_end(extractor, work)
        base = os.path.join(work, "pristine")
        os.makedirs(base)
        for f in FILES:
            shutil.copy(os.path.join(HERE, f), base)
        rc = selftests(base, extractor, work)
        ok = rc == [0, 0, 0]
        print("  %s  the unmutated copy's three self-tests pass (exit codes %s)" % ("ok  " if ok else "FAIL", rc))
        fails += not ok
        killed = 0
        for i, (fname, old, new, what) in enumerate(MUTANTS):
            d = os.path.join(work, "m%02d" % i)
            shutil.copytree(base, d)
            p = os.path.join(d, fname)
            src = open(p, encoding="utf-8").read()
            if src.count(old) != 1:
                print("  FAIL  mutant %02d (%s): its text occurs %d times" % (i, what, src.count(old)))
                fails += 1
                continue
            with open(p, "w", encoding="utf-8") as f:
                f.write(src.replace(old, new))
            rc = selftests(d, extractor, work)
            k = any(rc)
            killed += k
            print("  %s  mutant %02d %s: %s (exit codes %s)" % ("ok  " if k else "FAIL", i, fname, what, rc))
            fails += not k
            shutil.rmtree(d, ignore_errors=True)
        print("controls: %d of %d mutants killed" % (killed, len(MUTANTS)))
    finally:
        shutil.rmtree(work, ignore_errors=True)
    print("controls: %s" % ("OK" if not fails else "%d failure(s)" % fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
