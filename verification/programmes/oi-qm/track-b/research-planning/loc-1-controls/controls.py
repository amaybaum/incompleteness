"""LOC-1 controls that do not evaluate a target configuration (research development for PR #853).

    K-obj      objects/ holds exactly the files of §2.1's table; each file's size, sha256 and git blob id, computed
               from its bytes, equal its row.
    K-design   design/ holds exactly the files of §9's table; size and sha256 equal the row.
    K-prior    prior/ holds exactly the files of §13's table that are copied (a row whose form is "derived source"
               is provenance of an expected result and is not copied); size and sha256 equal the row.
    K-ret-F    retained/F/ holds check-run.json, jobs.json and designation.json, each well formed and naming F;
               check-run.json in the form of the evidence-retention archive's ci/<run>/results.json (schema
               oi-evidence-result, kind bridge), naming the run, the job, the recipe and the sha256 of the text it was
               read from; jobs.json every job with name, attempt and conclusion, at F; designation.json the
               designation's text, author, time and host object.
    SC-CLQ     clq.py --self-test.
    round trip p0_roundtrip.py --self-test (K-arith-16's round-trip clause, on synthetic elements).

The tables are read from the preregistration in the record directory, so the pins are the frozen ones.  Every check
reads bytes and parses JSON; nothing here imports or executes a file of objects/, design/ or prior/.

Run:  python3 -I -B controls.py --self-test [--p0 PATH_TO_PINNED_p0_exact.py]
      python3 -I -B controls.py --check-record RECORD_DIR [--F <sha>]     K-obj, K-design, K-prior (and K-ret-F)
      python3 -I -B controls.py --registry                               every §8 control and where it stands
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
ROW_OBJ = re.compile(r"^\| `([^`]+)` \| `([0-9a-f]{40})` \| `([0-9a-f]{40})` \| (\d+) \| `([0-9a-f]{64})` \|\s*$")
ROW_PIN = re.compile(r"^\| `([^`]+)` \| ([^|]*) \| ([^|]*) \| (\d+) \| `([0-9a-f]{64})` \|\s*$")


def blob_id(data):
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def sections(text):
    """Split the preregistration at its '## ' and '### ' headings."""
    out, cur, buf = {}, "", []
    for line in text.split("\n"):
        m = re.match(r"^(##+) (\d+(?:\.\d+)?)\.? ", line)
        if m:
            out[cur] = buf
            cur, buf = m.group(2), []
        buf.append(line)
    out[cur] = buf
    return out


def tables(prereg_text):
    s = sections(prereg_text)
    obj = [dict(zip(("file", "commit", "blob", "bytes", "sha256"), m.groups()))
           for m in (ROW_OBJ.match(l) for l in s.get("2.1", [])) if m]
    design = [dict(zip(("file", "role", "form", "bytes", "sha256"), m.groups()))
              for m in (ROW_PIN.match(l) for l in s.get("9", [])) if m]
    prior = [dict(zip(("file", "what", "form", "bytes", "sha256"), m.groups()))
             for m in (ROW_PIN.match(l) for l in s.get("13", [])) if m]
    for rows in (obj, design, prior):
        for r in rows:
            r["bytes"] = int(r["bytes"])
            for k in ("role", "form", "what"):
                if k in r:
                    r[k] = r[k].strip()
    return obj, design, prior


def files_under(d):
    out = []
    for root, _, fs in os.walk(d):
        for f in fs:
            out.append(os.path.relpath(os.path.join(root, f), d).replace(os.sep, "/"))
    return sorted(out)


def check_dir(d, rows, name, with_blob=False):
    fails = []
    if not os.path.isdir(d):
        return ["%s: %s is missing" % (name, d)]
    want = {r["file"]: r for r in rows}
    have = set(files_under(d))
    for f in sorted(have - set(want)):
        fails.append("%s: unlisted file %s" % (name, f))
    for f in sorted(set(want) - have):
        fails.append("%s: missing file %s" % (name, f))
    for f in sorted(set(want) & have):
        data = open(os.path.join(d, f), "rb").read()
        r = want[f]
        if len(data) != r["bytes"]:
            fails.append("%s: %s has %d bytes, pinned %d" % (name, f, len(data), r["bytes"]))
        if hashlib.sha256(data).hexdigest() != r["sha256"]:
            fails.append("%s: %s sha256 differs from its row" % (name, f))
        if with_blob and blob_id(data) != r["blob"]:
            fails.append("%s: %s git blob id %s, pinned %s" % (name, f, blob_id(data), r["blob"]))
    return fails


def copied_prior(rows):
    return [r for r in rows if not r["form"].startswith("derived source")]


def check_record(rec, F=None):
    text = open(os.path.join(rec, "preregistration.md"), encoding="utf-8").read()
    obj, design, prior = tables(text)
    res = []
    for name, d, rows, wb, n in (("K-obj", "objects", obj, True, 6), ("K-design", "design", design, False, None),
                                 ("K-prior", "prior", copied_prior(prior), False, None)):
        fails = check_dir(os.path.join(rec, d), rows, name, with_blob=wb)
        if n is not None and len(rows) != n:
            fails.append("%s: the table has %d rows, not %d" % (name, len(rows), n))
        res.append((name, not fails, fails or ["%d files equal their rows" % len(rows)]))
    if F is not None:
        fails = check_ret(os.path.join(rec, "retained", "F"), F, "F")
        res.append(("K-ret-F", not fails, fails or ["retained/F/ well formed and naming %s" % F[:12]]))
    return res


# ------------------------------------------------------------------- K-ret-F (and the per-commit part of K-ret-E)

def check_ret(d, commit, label):
    fails = []
    need = ("check-run.json", "jobs.json", "designation.json")
    if not os.path.isdir(d):
        return ["retained/%s/ is missing" % label]
    have = set(os.listdir(d))
    for f in need:
        if f not in have:
            fails.append("retained/%s/%s is missing" % (label, f))
    for f in sorted(have - set(need)):
        fails.append("retained/%s/ holds an unlisted file %s" % (label, f))
    if fails:
        return fails
    try:
        cr, jobs, des = (json.load(open(os.path.join(d, f), encoding="utf-8")) for f in need)
    except ValueError as e:
        return ["retained/%s: a file is not JSON (%s)" % (label, e)]
    # check-run.json: the archive's results.json form
    if cr.get("schema") != "oi-evidence-result" or cr.get("version") != 1 or cr.get("kind") != "bridge":
        fails.append("check-run.json is not an oi-evidence-result v1 of kind bridge")
    run = cr.get("run") or {}
    if run.get("head_sha") != commit:
        fails.append("check-run.json names %s, not %s" % (str(run.get("head_sha"))[:12], commit[:12]))
    for k in ("id", "job_id", "job_name", "attempt", "event", "workflow", "conclusion"):
        if k not in run:
            fails.append("check-run.json run lacks %s" % k)
    if run.get("event") != "workflow_dispatch":
        fails.append("check-run.json: the run is not a workflow_dispatch exact-head run")
    if run.get("job_name") != "Mathlib bridge":
        fails.append("check-run.json: the job is not the Mathlib bridge job")
    src = cr.get("source") or {}
    if not HEX64.match(str(src.get("served_sha256", ""))) or not src.get("extractor", "").endswith("extract_result.py"):
        fails.append("check-run.json source lacks the served text's sha256 or the extractor")
    rec = (cr.get("reproduce") or {}).get("recipe")
    # main's reproduce.py --run finds an expected result only through an archive entry ci-<run>; a run retained in
    # the record directory has none, so its recipe is the manual one ending in compare_result.py on this file
    by_archive = rec and any(("reproduce.py --run %s" % run.get("id")) in str(x) for x in rec)
    by_hand = rec and any("compare_result.py" in str(x) and ("retained/%s/check-run.json" % label) in str(x)
                          for x in rec) and any(("worktree add --detach <dir> %s" % commit) in str(x) for x in rec)
    if not (by_archive or by_hand):
        fails.append("check-run.json names no recipe that regenerates and compares it")
    exp = cr.get("expected") or {}
    if exp.get("build_success") is not True or not (exp.get("gate") or {}).get("steps") or \
            "verdict" not in (exp.get("gate") or {}) or "modules" not in exp or "markers" not in exp:
        fails.append("check-run.json expected lacks build success, the gate's steps and verdict, modules or markers")
    # jobs.json
    js = jobs.get("jobs") if isinstance(jobs, dict) else None
    if not js:
        fails.append("jobs.json lists no jobs")
    else:
        for j in js:
            for k in ("name", "run_attempt", "conclusion", "head_sha"):
                if k not in j:
                    fails.append("jobs.json: a job lacks %s" % k)
            if j.get("head_sha") != commit:
                fails.append("jobs.json: job %s is at %s" % (j.get("name"), str(j.get("head_sha"))[:12]))
        if not any(j.get("name") == run.get("job_name") and str(j.get("id")) == str(run.get("job_id")) for j in js):
            fails.append("jobs.json does not hold check-run.json's job")
        if any(j.get("conclusion") != "success" for j in js):
            fails.append("jobs.json: not every job succeeded")
    # designation.json
    for k in ("subject", "commit", "text", "author", "time", "host_object"):
        if k not in des:
            fails.append("designation.json lacks %s" % k)
    if des.get("commit") != commit or des.get("subject") != label:
        fails.append("designation.json does not designate %s as %s" % (commit[:12], label))
    if not re.match(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ$", str(des.get("time", ""))):
        fails.append("designation.json time is not an ISO-8601 UTC instant")
    if commit not in str(des.get("text", "")) and commit[:12] not in str(des.get("text", "")):
        fails.append("designation.json text does not name the commit")
    return fails


# ------------------------------------------------------------------- the §8 registry

REGISTRY = [
    # id, where it is implemented, whether it can run before F without a target configuration
    ("K-C21", "not yet: needs the run script; reads C21's targets", "no"),
    ("K-repro", "not yet: needs the run script; reproduces P0/P2 lines at sigma_0", "no"),
    ("K-obj", "controls.py", "yes, on the predicted stage-1 tree"),
    ("K-design", "controls.py", "yes, on the predicted stage-1 tree"),
    ("K-prior", "controls.py", "yes, on the predicted stage-1 tree"),
    ("K-arith-16", "loc-1-arith/s16_layer.py, cyclo16.py; round-trip clause p0_roundtrip.py; target clause "
                   "check_entries() at stage 2", "yes, synthetic; the target clauses at stage 2"),
    ("K-ring", "not yet: S-ring(3) is a target configuration", "no"),
    ("SC-nest", "not yet: needs the run script", "no"),
    ("SC-I0", "not yet: CENT and CCC are target configurations", "no"),
    ("SC-I1", "not yet: needs K-hid", "no"),
    ("SC-I2", "not yet: the constructed leg-T lifts are synthetic, the leg-S rules are targets", "partly"),
    ("SC-W-I2T", "not yet: needs the run script", "no"),
    ("SC-CLQ", "clq.py", "yes"),
    ("K0", "two byte-identical runs: run_controls.py in CI (fast suite twice)", "yes, for the controls"),
    ("K-cls", "W-CLS counts: indep_arith_check.py (class enumeration); W-CLS-S at stage 2", "partly"),
    ("K-adm", "not yet", "no"),
    ("K-hid", "not yet", "no"),
    ("K-prod", "not yet: F16 and H1 (x) H1 are P0 objects", "no"),
    ("K-rep", "not yet: constructed instances", "yes, once written"),
    ("K-rel-pos", "not yet: CCC is a target configuration", "no"),
    ("K-search", "design/c21_search.py (preflight)", "rerun at stage 2 (K-engine)"),
    ("K-sample", "design/c21_sampler.py (preflight); the I1 sampler not yet", "partly"),
    ("K-engine", "design/ preflight suite, rerun at stage 2", "stage 2"),
    ("K-leap, K-dep", "design/f34_enum.py (preflight) for F_3^4; F_3^8, F_5^8 not yet", "partly"),
    ("K-eig, K-same", "not yet", "no"),
    ("K-obs", "not yet: S-free and S-deep are target configurations", "no"),
    ("K-replay-arith", "loc-1-arith/replay_cyclo16.py; independent check indep_arith_check.py", "yes"),
    ("K-replay-lifts", "not yet: rebuilding the frozen lifts is a computation on targets", "no"),
    ("K-ret-F", "controls.py (form check)", "self-test only; the files exist after F"),
    ("K-ret-E", "controls.py check_ret for retained/E/; the archive and receipt clauses not yet", "after E"),
]


# ------------------------------------------------------------------- self-test

def _fixture(root):
    """A miniature record: a preregistration with the three tables and a matching tree."""
    files = {"objects/a/x.md": b"x\n", "objects/a/y.py": b"y = 1\n", "objects/b/z.txt": b"z\n",
             "objects/b/u.md": b"u\n", "objects/b/v.py": b"v = 2\n", "objects/b/w.txt": b"w\n",
             "design/e.py": b"e = 3\n", "prior/p.py": b"p = 4\n", "prior/p-expected.json": b"{}\n"}
    for p, b in files.items():
        os.makedirs(os.path.dirname(os.path.join(root, p)), exist_ok=True)
        open(os.path.join(root, p), "wb").write(b)
    h = lambda b: hashlib.sha256(b).hexdigest()
    lines = ["# fixture", "## 2. Records", "### 2.1 Frozen objects copied at stage 1", "",
             "| copy | source commit | blob | bytes | sha256 |", "| --- | --- | --- | --- | --- |"]
    for p, b in files.items():
        if p.startswith("objects/"):
            lines.append("| `%s` | `%s` | `%s` | %d | `%s` |" % (p[8:], "0" * 40, blob_id(b), len(b), h(b)))
    lines += ["", "## 9. Budget", "", "| file | role | form | bytes | sha256 |", "| --- | --- | --- | --- | --- |",
              "| `e.py` | engine | complete | %d | `%s` |" % (len(files["design/e.py"]), h(files["design/e.py"])),
              "", "## 13. Prior", "", "| file | what | form | bytes | sha256 |", "| --- | --- | --- | --- | --- |",
              "| `p.py` | script | complete-as-cited | %d | `%s` |" % (len(files["prior/p.py"]), h(files["prior/p.py"])),
              "| `p.out` | its output; not copied | derived source | 3 | `%s` |" % ("1" * 64),
              "| `p-expected.json` | expected result | derived | %d | `%s` |" % (
                  len(files["prior/p-expected.json"]), h(files["prior/p-expected.json"])),
              "", "## 14. Owner decisions", ""]
    open(os.path.join(root, "preregistration.md"), "w", encoding="utf-8").write("\n".join(lines))


def _ret_fixture(d, F):
    os.makedirs(d, exist_ok=True)
    cr = {"schema": "oi-evidence-result", "version": 1, "kind": "bridge",
          "run": {"id": "1", "job_id": "2", "job_name": "Mathlib bridge", "attempt": 1, "event": "workflow_dispatch",
                  "workflow": "verify.yml", "conclusion": "success", "head_sha": F},
          "source": {"extractor": "verification/audits/evidence-retention/extract_result.py", "served_sha256": "a" * 64},
          "reproduce": {"recipe": ["python3 -I verification/audits/evidence-retention/reproduce.py --run 1 --work <d>"]},
          "expected": {"build_success": True, "gate": {"steps": [{"name": "x", "status": "PASS", "summary": ""}],
                                                       "verdict": "PASS"}, "modules": {}, "markers": {}}}
    jobs = {"jobs": [{"id": 2, "name": "Mathlib bridge", "run_attempt": 1, "conclusion": "success", "head_sha": F},
                     {"id": 3, "name": "Lean kernel check", "run_attempt": 1, "conclusion": "success", "head_sha": F}]}
    des = {"subject": "F", "commit": F, "text": "I designate %s as F." % F, "author": "owner",
           "time": "2026-01-01T00:00:00Z", "host_object": "issue comment 1"}
    for name, doc in (("check-run.json", cr), ("jobs.json", jobs), ("designation.json", des)):
        json.dump(doc, open(os.path.join(d, name), "w"), indent=1, sort_keys=True)


def self_test(p0=None):
    lines, ok = [], True

    def rep(name, passed, detail=""):
        nonlocal ok
        ok &= bool(passed)
        lines.append("%s %-66s %s" % ("PASS" if passed else "FAIL", name, detail))

    tmp = tempfile.mkdtemp(prefix="loc1-controls-")
    try:
        rec = os.path.join(tmp, "rec")
        _fixture(rec)
        F = "f" * 40
        _ret_fixture(os.path.join(rec, "retained", "F"), F)
        res = check_record(rec, F)
        rep("K-obj, K-design, K-prior, K-ret-F pass on a matching record", all(r[1] for r in res),
            "; ".join("%s %s" % (r[0], "ok" if r[1] else r[2][0]) for r in res))

        def neg(name, mutate, control):
            shutil.rmtree(rec)
            _fixture(rec)
            _ret_fixture(os.path.join(rec, "retained", "F"), F)
            mutate()
            r = {x[0]: x for x in check_record(rec, F)}[control]
            rep("NEG " + name, not r[1], r[2][0] if not r[1] else "NOT detected")

        o = lambda p: os.path.join(rec, p)
        neg("K-obj: a one-byte change", lambda: open(o("objects/a/x.md"), "wb").write(b"X\n"), "K-obj")
        neg("K-obj: an unlisted file", lambda: open(o("objects/a/extra"), "wb").write(b""), "K-obj")
        neg("K-obj: a missing file", lambda: os.remove(o("objects/b/w.txt")), "K-obj")
        neg("K-design: a file appended to", lambda: open(o("design/e.py"), "ab").write(b"#"), "K-design")
        neg("K-design: an unpinned design run", lambda: (os.makedirs(o("design/runs")),
                                                         open(o("design/runs/1.json"), "wb").write(b"{}")), "K-design")
        neg("K-prior: the uncopied output copied", lambda: open(o("prior/p.out"), "wb").write(b"p\n\n"), "K-prior")

        def wrong_head():
            p = o("retained/F/check-run.json")
            d = json.load(open(p))
            d["run"]["head_sha"] = "e" * 40
            json.dump(d, open(p, "w"))
        neg("K-ret-F: check-run.json at another commit", wrong_head, "K-ret-F")

        def pr_run():
            p = o("retained/F/check-run.json")
            d = json.load(open(p))
            d["run"]["event"] = "pull_request"
            json.dump(d, open(p, "w"))
        neg("K-ret-F: a pull-request run (a synthetic merge, not F)", pr_run, "K-ret-F")

        def red_job():
            p = o("retained/F/jobs.json")
            d = json.load(open(p))
            d["jobs"][1]["conclusion"] = "failure"
            json.dump(d, open(p, "w"))
        neg("K-ret-F: a job not green", red_job, "K-ret-F")
        neg("K-ret-F: designation.json missing", lambda: os.remove(o("retained/F/designation.json")), "K-ret-F")
        # the real archive's form, read-only, if this checkout has it
        arch = _find_archive()
        if arch:
            rs = sorted(os.listdir(os.path.join(arch, "ci")))
            sample = None
            for r in rs:
                p = os.path.join(arch, "ci", r, "results.json")
                if os.path.isfile(p):
                    d = json.load(open(p))
                    if d.get("run", {}).get("event") == "workflow_dispatch" and d.get("kind") == "bridge":
                        sample = d
                        break
            if sample:
                dd = os.path.join(tmp, "arch", "retained", "F")
                os.makedirs(dd)
                head = sample["run"]["head_sha"]
                json.dump(sample, open(os.path.join(dd, "check-run.json"), "w"))
                _ret_fixture(os.path.join(tmp, "arch-j"), head)
                shutil.copy(os.path.join(tmp, "arch-j", "designation.json"), dd)
                jj = {"jobs": [{"id": int(sample["run"]["job_id"]), "name": "Mathlib bridge", "run_attempt": 1,
                                "conclusion": "success", "head_sha": head}]}
                json.dump(jj, open(os.path.join(dd, "jobs.json"), "w"))
                f = check_ret(dd, head, "F")
                rep("K-ret-F accepts the archive's own results.json form (run %s)" % sample["run"]["id"], not f,
                    "; ".join(f[:2]))
        else:
            lines.append("--   the evidence-retention archive is not in this checkout; the form check used the fixture")
    finally:
        shutil.rmtree(tmp)
    for sub, extra in (("clq.py", []), ("p0_roundtrip.py", [p0] if p0 else [])):
        r = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, sub), "--self-test"] + extra,
                           capture_output=True, text=True)
        last = (r.stdout.strip().split("\n") or [""])[-1]
        rep("%s --self-test" % sub, r.returncode == 0, last)
    lines.append("controls self-test: %s" % ("ALL PASS" if ok else "FAILURE"))
    return ok, lines


def _find_archive():
    d = HERE
    for _ in range(8):
        p = os.path.join(d, "verification", "audits", "evidence-retention")
        if os.path.isdir(os.path.join(p, "ci")):
            return p
        d = os.path.dirname(d)
    return None


def main(argv):
    if argv[:1] == ["--self-test"]:
        p0 = argv[2] if len(argv) == 3 and argv[1] == "--p0" else os.environ.get("LOC1_P0_EXACT")
        ok, lines = self_test(p0)
        print("\n".join(lines))
        return 0 if ok else 1
    if argv[:1] == ["--check-record"] and len(argv) in (2, 4):
        F = argv[3] if len(argv) == 4 and argv[2] == "--F" else None
        res = check_record(argv[1], F)
        for name, passed, det in res:
            print("%s %-10s %s" % ("PASS" if passed else "FAIL", name, "; ".join(det[:6])))
        return 0 if all(r[1] for r in res) else 1
    if argv[:1] == ["--registry"]:
        for cid, where, pre in REGISTRY:
            print("%-16s pre-F: %-36s %s" % (cid, pre, where))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
