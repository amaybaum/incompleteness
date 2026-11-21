#!/usr/bin/env python3
"""Verify the retained T0 trial evidence against expected.json.

  python3 -I -B check.py                 integrity checks (standard library only)
  python3 -I -B check.py --self-test     the same checks on mutated copies; each must fail
  python3 -I -B check.py --github        also compare the artifact digest, the run's event, workflow and head,
                                         and the job conclusion with what the host reports (needs gh)
  python3 -I -B check.py --extract DIR   after the checks pass, write the artifact's members to DIR, byte for byte
  python3 -I -B check.py --structure     Structure.pdf: committed (main) against CI-built; fails unless every
                                         recorded value is reproduced (needs git, pdftotext)

The integrity checks: artifact.zip has the recorded sha256 and size; its members are exactly the
recorded ones, each with the recorded sha256; the Structure.md patch has the recorded sha256;
the four preserve_check.py reports carry the recorded verdicts and checks, with the nine findings
exactly in the one failing check; every file under artifact/ is byte-identical to the
member of the same name, and every out/ member is present there; the job log has the recorded
sha256; result.json inside the artifact carries the recorded trial, plan, workflow and run ids,
step outcomes, preserve findings, page counts and verdict.
"""
import hashlib
import io
import json
import os
import subprocess
import sys
import tempfile
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def check(zip_bytes, retained, log_bytes, exp, patch_bytes):
    """Return a list of findings; empty means the evidence matches expected.json."""
    f = []
    if sha(patch_bytes) != exp["structure_patch"]["sha256"]:
        f.append("Structure.md patch sha256 differs from the recorded digest")
    a = exp["artifact"]
    if sha(zip_bytes) != a["sha256"]:
        f.append("artifact.zip sha256 differs from the recorded digest")
    if len(zip_bytes) != a["size_in_bytes"]:
        f.append("artifact.zip size differs from the recorded size")
    try:
        z = zipfile.ZipFile(io.BytesIO(zip_bytes))
        members = {i.filename: z.read(i) for i in z.infolist()}
    except Exception as e:  # a corrupt archive is a finding, not a crash
        return f + [f"artifact.zip does not open: {e}"]
    if sorted(members) != sorted(a["members"]):
        f.append("artifact members differ from the recorded list")
    for name, digest in sorted(a["members"].items()):
        if name in members and sha(members[name]) != digest:
            f.append(f"member {name}: sha256 differs")
    for name, b in sorted(retained.items()):
        if members.get(name) != b:
            f.append(f"artifact/{name}: not byte-identical to the artifact member")
    for name in sorted(members):
        if name.startswith("out/") and name not in retained:
            f.append(f"artifact/{name}: missing")
    if sha(log_bytes) != exp["job_log"]["sha256"]:
        f.append("job log sha256 differs from the recorded digest")
    try:
        r = json.loads(members["out/result.json"])
    except Exception as e:
        return f + [f"result.json unreadable: {e}"]
    want = {
        "trial_sha": exp["trial_sha"], "plan_sha": exp["plan_sha"],
        "workflow_sha": exp["workflow_sha"], "run_id": str(exp["run_id"]),
        "run_attempt": str(exp["run_attempt"]), "verdict": exp["verdict"],
        "tex_files_differing": exp["tex_files_differing"], "pdf_pages": exp["pdf_pages_built"],
    }
    for k, v in want.items():
        if r.get(k) != v:
            f.append(f"result.json {k}: {r.get(k)!r}, expected {v!r}")
    got = {k: v.get("outcome") for k, v in r.get("steps", {}).items()}
    if got != exp["step_outcomes"]:
        f.append(f"result.json step outcomes differ: {got}")
    if r.get("steps", {}).get("preserve", {}).get("log_lines_flagged") != exp["preserve_findings"]:
        f.append("result.json preserve findings differ from the recorded nine")
    plog = members.get("out/preserve.log", b"").decode("utf-8", "replace")
    for line in exp["preserve_findings"]:
        if line not in plog:
            f.append(f"preserve.log lacks: {line}")
    f += check_reports(members, exp)
    return f


def check_reports(members, exp):
    """The nine findings and the passing checks, read from preserve_check.py's structured reports
    (schema a1exit-checker-result-v1) rather than from log-derived fields."""
    f = []
    sr = exp["structured_reports"]
    for name, want in sr.items():
        try:
            rep = json.loads(members[f"out/{name}"])
        except Exception as e:
            f.append(f"report {name} unreadable: {e}")
            continue
        for k in ("schema", "plan", "ledger_sha256", "mode", "verdict"):
            if rep.get(k) != want[k]:
                f.append(f"report {name} {k}: {rep.get(k)!r}, expected {want[k]!r}")
        checks = rep.get("checks", [])
        if [c.get("name") for c in checks] != want["check_names"]:
            f.append(f"report {name}: check list differs from the recorded one")
        failing = [c for c in checks if c.get("status") != "pass"]
        if [c.get("name") for c in failing] != want["failing"]:
            f.append(f"report {name}: failing checks {[c.get('name') for c in failing]}, "
                     f"expected {want['failing']}")
        for c in checks:
            if c.get("status") == "pass" and c.get("discrepancies"):
                f.append(f"report {name}: passing check {c.get('name')!r} lists discrepancies")
        for c in failing:
            nine = [x[len("FAIL "):] if x.startswith("FAIL ") else x for x in exp["preserve_findings"]]
            if c.get("status") != "fail" or c.get("discrepancies") != nine:
                f.append(f"report {name}: check {c.get('name')!r} does not carry exactly the nine findings")
    return f


def load():
    exp = json.load(open(os.path.join(HERE, "expected.json")))
    zb = open(os.path.join(HERE, "artifact.zip"), "rb").read()
    lb = open(os.path.join(HERE, exp["job_log"]["file"]), "rb").read()
    pb = open(os.path.join(HERE, exp["structure_patch"]["file"]), "rb").read()
    retained = {}
    root = os.path.join(HERE, "artifact")
    for dp, _, fs in os.walk(root):
        for n in fs:
            p = os.path.join(dp, n)
            retained[os.path.relpath(p, root).replace(os.sep, "/")] = open(p, "rb").read()
    return zb, retained, lb, exp, pb


def rezip(zb, edit):
    """Rebuild the archive with edit(name, bytes) -> bytes | None (None drops the member)."""
    src = zipfile.ZipFile(io.BytesIO(zb))
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as dst:
        for i in src.infolist():
            b = edit(i.filename, src.read(i))
            if b is not None:
                dst.writestr(i, b)
    return out.getvalue()


def self_test():
    """Each mutant must be caught by the check it targets: its expected finding must be reported."""
    zb, ret, lb, exp, pb = load()
    if check(zb, ret, lb, exp, pb):
        print("self-test: the unmodified evidence does not pass; mutants not run")
        return 1
    def flip(b):
        return bytes([b[0] ^ 1]) + b[1:] if b else b"x"
    def forge(zb2, members_too):
        """A consistent forgery: the recorded digest and size follow zb2, so the deeper checks must
        catch it. With members_too the member list and digests, and the retained files, follow too."""
        e = json.loads(json.dumps(exp))
        e["artifact"].update(sha256=sha(zb2), size_in_bytes=len(zb2))
        r2 = dict(ret)
        if members_too:
            z = zipfile.ZipFile(io.BytesIO(zb2))
            e["artifact"]["members"] = {i.filename: sha(z.read(i)) for i in z.infolist()}
            r2 = {k: z.read(k) for k in ret if k in z.namelist()}
        return zb2, r2, lb, e, pb
    def res(edit):
        r = json.loads(zipfile.ZipFile(io.BytesIO(zb)).read("out/result.json"))
        edit(r)
        return forge(rezip(zb, lambda n, b: json.dumps(r).encode() if n == "out/result.json" else b), True)
    def slog(edit):
        return forge(rezip(zb, lambda n, b: edit(b) if n == "out/preserve.log" else b), True)
    def rpt(member, edit):
        d = json.loads(zipfile.ZipFile(io.BytesIO(zb)).read("out/" + member))
        edit(d)
        return forge(rezip(zb, lambda n, b: json.dumps(d).encode() if n == "out/" + member else b), True)
    finding = exp["preserve_findings"][6].encode()
    base = (zb, ret, lb, exp, pb)
    def with_(i, v):
        t = list(base)
        t[i] = v
        return tuple(t)
    mutants = {
        "one byte of the zip": (with_(0, flip(zb)), "artifact.zip sha256 differs"),
        "one byte of a retained log": (with_(1, {**ret, "out/preserve.log": flip(ret["out/preserve.log"])}),
                                       "artifact/out/preserve.log: not byte-identical"),
        "a retained file missing": (with_(1, {k: v for k, v in ret.items() if k != "out/result.json"}),
                                    "artifact/out/result.json: missing"),
        "an extra retained file": (with_(1, {**ret, "out/extra.txt": b"x"}), "artifact/out/extra.txt: not byte-identical"),
        "one byte of the job log": (with_(2, flip(lb)), "job log sha256 differs"),
        "one byte of the Structure.md patch": (with_(4, flip(pb)), "Structure.md patch sha256 differs"),
        "a PDF member dropped (digest forged)":
            (forge(rezip(zb, lambda n, b: None if n.endswith("Structure.pdf") else b), False), "artifact members differ"),
        "a PDF member altered (digest forged)":
            (forge(rezip(zb, lambda n, b: flip(b) if n.endswith("SM.pdf") else b), False), "member build/papers/SM.pdf: sha256 differs"),
        "a finding dropped from result.json":
            (res(lambda r: r["steps"]["preserve"]["log_lines_flagged"].pop(6)), "result.json preserve findings differ"),
        "a finding dropped from preserve.log": (slog(lambda b: b.replace(finding, b"")), "preserve.log lacks"),
        "guards outcome changed": (res(lambda r: r["steps"]["guards"].update(outcome="success")), "step outcomes differ"),
        "a TeX difference": (res(lambda r: r.update(tex_files_differing=["papers/GR.tex"])), "tex_files_differing"),
        "a page count changed": (res(lambda r: r["pdf_pages"].update({"papers/Structure.pdf": 94})), "result.json pdf_pages"),
        "wrong trial sha": (res(lambda r: r.update(trial_sha="0" * 40)), "result.json trial_sha"),
        "a finding dropped from the tree report":
            (rpt("preserve_check-tree.json", lambda d: next(c for c in d["checks"] if c["status"] == "fail")
                 ["discrepancies"].pop(6)), "does not carry exactly the nine findings"),
        "a passing tree check turned failing":
            (rpt("preserve_check-tree.json", lambda d: d["checks"][0].update(status="fail")),
             "report preserve_check-tree.json: failing checks"),
        "the commit report's verdict changed":
            (rpt("preserve_check-commit.json", lambda d: d.update(verdict="fail")),
             "report preserve_check-commit.json verdict"),
    }
    bad = 0
    for name, (args, want) in mutants.items():
        f = check(*args)
        hit = any(want in x for x in f)
        print(f"  {'ok  ' if hit else 'MISS'} mutant {name}: "
              f"{next((x for x in f if want in x), 'expected finding not reported: ' + want)}")
        bad += not hit
    print(f"self-test: {len(mutants) - bad}/{len(mutants)} mutants caught by their target check; "
          f"RESULT {'PASS' if not bad else 'FAIL'}")
    return 1 if bad else 0


def pages(pdf_bytes):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "x.pdf")
        open(p, "wb").write(pdf_bytes)
        t = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, check=True).stdout
    ps = t.decode("utf-8", "replace").split("\f")
    return [x for x in ps if x.strip()]


def git(*a):
    return subprocess.run(["git", "-C", HERE, *a], capture_output=True, check=True).stdout


def structure():
    """Committed papers/Structure.pdf (the main blob) against the CI-built one, and the attribution of
    their text differences to the papers/Structure.md edits. The edited source is rebuilt from the
    main blob and the retained patch, and checked against T0's blob id; no T0 objects are needed."""
    import re
    from collections import Counter
    zb, _, _, exp, pb = load()
    sp = exp["structure_patch"]
    if sha(pb) != sp["sha256"]:
        print("Structure.md patch sha256 differs from the recorded digest; RESULT FAIL")
        return 1
    built = zipfile.ZipFile(io.BytesIO(zb)).read("build/papers/Structure.pdf")
    committed = git("show", f"{exp['workflow_sha']}:papers/Structure.pdf")
    c, b = pages(committed), pages(built)
    first = next((i for i, (x, y) in enumerate(zip(c, b)) if x != y), None)
    lines = lambda p: [l.strip() for l in p.splitlines() if l.strip()]
    print(f"committed (main {exp['workflow_sha'][:8]}): {len(c)} pages; CI-built: {len(b)} pages")
    print(f"first page whose text differs: {first + 1 if first is not None else 'none'}")
    print(f"last line of committed page {len(c)}: {lines(c[-1])[-2]}")
    print(f"CI-built page {len(b)}, in full:")
    for l in lines(b[-1]):
        print(f"  | {l}")
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "papers"))
        src = os.path.join(d, "papers", "Structure.md")
        open(src, "wb").write(git("show", f"{exp['workflow_sha']}:papers/Structure.md"))
        old = os.path.join(d, "old.md")
        open(old, "wb").write(open(src, "rb").read())
        subprocess.run(["git", "apply", "--unsafe-paths", "--directory=.", os.path.join(HERE, sp["file"])],
                       cwd=d, capture_output=True, check=True)
        blob = subprocess.run(["git", "hash-object", src], capture_output=True, check=True, text=True).stdout.strip()
        if blob != sp["T0_blob"]:
            print(f"rebuilt Structure.md blob {blob} is not T0's {sp['T0_blob']}; RESULT FAIL")
            return 1
        print(f"Structure.md at T0 rebuilt from main and the patch: blob {blob}, equal to T0's")
        wd = subprocess.run(["git", "diff", "--no-index", "--word-diff=porcelain", "--word-diff-regex=[^[:space:]]+",
                             old, src], capture_output=True).stdout.decode()
    # Word multisets, so reflow and reordering cancel. Tokens are lower-cased with punctuation,
    # symbols and hyphens removed, and tokens of one to three digits (page numbers) are dropped:
    # the comparison does not resolve differences in symbols or short numbers.
    def norm(w):
        return re.sub(r"[^\w]", "", w.replace("-", "").replace("\u2013", "").replace("\u2014", "")).lower()
    def pdfwords(pdf):
        with tempfile.TemporaryDirectory() as d:
            q = os.path.join(d, "x.pdf")
            open(q, "wb").write(pdf)
            txt = subprocess.run(["pdftotext", q, "-"], capture_output=True, check=True).stdout.decode()
        txt = re.sub(r"-\n", "", txt).replace("\f", " ")
        return Counter(n for n in map(norm, txt.split()) if n and not re.fullmatch(r"\d{1,3}", n))
    add, rem = Counter(), Counter()
    for l in wd.splitlines():
        if l.startswith("+") and not l.startswith("+++"):
            add.update(n for n in map(norm, l[1:].split()) if n)
        elif l.startswith("-") and not l.startswith("---"):
            rem.update(n for n in map(norm, l[1:].split()) if n)
    pc, pbw = pdfwords(committed), pdfwords(built)
    md_add, md_rem, pdf_add, pdf_rem = add - rem, rem - add, pbw - pc, pc - pbw
    print(f"PDF words (normalized tokens): committed {sum(pc.values())}, CI-built {sum(pbw.values())}")
    print(f"attribution: source net words +{sum(md_add.values())} -{sum(md_rem.values())}; "
          f"PDF net words +{sum(pdf_add.values())} -{sum(pdf_rem.values())}")
    print(f"  source additions absent from the PDF additions: {dict(md_add - pdf_add)}")
    print(f"  source removals absent from the PDF removals:   {dict(md_rem - pdf_rem)}")
    print(f"  PDF additions not from the source: {dict(pdf_add - md_add)}")
    print(f"  PDF removals not from the source:  {dict(pdf_rem - md_rem)}")
    # Pass/fail: the retained evidence must reproduce the recorded comparison exactly. This checks
    # that the evidence is what the README describes; it does not establish why the page appeared.
    se = exp["structure_expected"]
    got = {
        "committed_pages": len(c), "built_pages": len(b),
        "first_differing_page": first + 1 if first is not None else None,
        "built_last_page_lines": lines(b[-1]),
        "tokens_committed": sum(pc.values()), "tokens_built": sum(pbw.values()),
        "source_net_added": sum(md_add.values()), "source_net_removed": sum(md_rem.values()),
        "pdf_net_added": sum(pdf_add.values()), "pdf_net_removed": sum(pdf_rem.values()),
        "source_additions_absent_from_pdf": dict(md_add - pdf_add),
        "source_removals_absent_from_pdf": dict(md_rem - pdf_rem),
        "pdf_additions_not_from_source": dict(pdf_add - md_add),
        "pdf_removals_not_from_source": dict(pdf_rem - md_rem),
    }
    bad = [k for k in se if k != "pdftotext" and got[k] != se[k]]
    for k in bad:
        print(f"  FAIL {k}: {got[k]!r}, expected {se[k]!r}")
    print(f"Structure comparison: {len(se) - 1 - len(bad)}/{len(se) - 1} recorded values reproduced "
          f"(recorded with {se['pdftotext']}); RESULT {'PASS' if not bad else 'FAIL'}")
    return 1 if bad else 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if "--structure" in argv:
        return structure()
    zb, ret, lb, exp, pb = load()
    f = check(zb, ret, lb, exp, pb)
    if "--github" in argv:
        a = exp["artifact"]
        def api(path, jq):
            q = subprocess.run(["gh", "api", f"repos/amaybaum/incompleteness/{path}", "--jq", jq],
                               capture_output=True, text=True)
            return q.stdout.strip() or q.stderr.strip()
        host = {
            "artifact digest": (api(f"actions/artifacts/{a['id']}", ".digest"), "sha256:" + a["sha256"]),
            "run event": (api(f"actions/runs/{exp['run_id']}", ".event"), exp["event"]),
            "run workflow path": (api(f"actions/runs/{exp['run_id']}", ".path"), exp["workflow"]),
            "run head sha": (api(f"actions/runs/{exp['run_id']}", ".head_sha"), exp["workflow_sha"]),
            "job conclusion": (api(f"actions/jobs/{exp['job_id']}", ".conclusion"), exp["job_conclusion"]),
        }
        for k, (got, want) in host.items():
            if got != want:
                f.append(f"host {k} {got!r} differs from the recorded {want!r}")
            else:
                print(f"host {k} matches the record")
    if "--extract" in argv:
        d = argv[argv.index("--extract") + 1]
        if f:
            f.append("--extract refused: the evidence does not match expected.json")
        else:
            z = zipfile.ZipFile(io.BytesIO(zb))
            root = os.path.realpath(d)
            for i in z.infolist():
                p = os.path.realpath(os.path.join(root, i.filename))
                if i.filename.startswith("/") or ".." in i.filename.split("/") or not p.startswith(root + os.sep):
                    f.append(f"--extract refused: unsafe member name {i.filename!r}")
                    break
            else:
                for i in z.infolist():
                    p = os.path.join(root, i.filename)
                    os.makedirs(os.path.dirname(p), exist_ok=True)
                    open(p, "wb").write(z.read(i))
                print(f"extracted {len(z.infolist())} members to {d}")
    for x in f:
        print("  FAIL", x)
    print(f"T0 evidence: {len(exp['artifact']['members'])} artifact members, "
          f"{len(exp['preserve_findings'])} preserve findings; {len(f)} findings; "
          f"RESULT {'PASS' if not f else 'FAIL'}")
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
