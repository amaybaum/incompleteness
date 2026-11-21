#!/usr/bin/env python3
"""Verify the retained T0 trial evidence against expected.json.

  python3 -I -B check.py                 integrity checks (standard library only)
  python3 -I -B check.py --self-test     the same checks on mutated copies; each must fail
  python3 -I -B check.py --github        also compare the artifact digest the host reports (needs gh)
  python3 -I -B check.py --extract DIR   write the artifact's members to DIR, byte for byte
  python3 -I -B check.py --structure     Structure.pdf: committed (main) against CI-built (needs git, pdftotext)

The integrity checks: artifact.zip has the recorded sha256 and size; its members are exactly the
recorded ones, each with the recorded sha256; every file under artifact/ is byte-identical to the
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


def check(zip_bytes, retained, log_bytes, exp):
    """Return a list of findings; empty means the evidence matches expected.json."""
    f = []
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
    return f


def load():
    exp = json.load(open(os.path.join(HERE, "expected.json")))
    zb = open(os.path.join(HERE, "artifact.zip"), "rb").read()
    lb = open(os.path.join(HERE, exp["job_log"]["file"]), "rb").read()
    retained = {}
    root = os.path.join(HERE, "artifact")
    for dp, _, fs in os.walk(root):
        for n in fs:
            p = os.path.join(dp, n)
            retained[os.path.relpath(p, root).replace(os.sep, "/")] = open(p, "rb").read()
    return zb, retained, lb, exp


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
    zb, ret, lb, exp = load()
    if check(zb, ret, lb, exp):
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
        return zb2, r2, lb, e
    def res(edit):
        r = json.loads(zipfile.ZipFile(io.BytesIO(zb)).read("out/result.json"))
        edit(r)
        return forge(rezip(zb, lambda n, b: json.dumps(r).encode() if n == "out/result.json" else b), True)
    def slog(edit):
        return forge(rezip(zb, lambda n, b: edit(b) if n == "out/preserve.log" else b), True)
    finding = exp["preserve_findings"][6].encode()
    mutants = {
        "one byte of the zip": (flip(zb), ret, lb, exp),
        "one byte of a retained log": (zb, {**ret, "out/preserve.log": flip(ret["out/preserve.log"])}, lb, exp),
        "a retained file missing": (zb, {k: v for k, v in ret.items() if k != "out/result.json"}, lb, exp),
        "an extra retained file": (zb, {**ret, "out/extra.txt": b"x"}, lb, exp),
        "one byte of the job log": (zb, ret, flip(lb), exp),
        "a PDF member dropped (digest forged)": forge(rezip(zb, lambda n, b: None if n.endswith("Structure.pdf") else b), False),
        "a PDF member altered (digest forged)": forge(rezip(zb, lambda n, b: flip(b) if n.endswith("SM.pdf") else b), False),
        "a finding dropped from result.json": res(lambda r: r["steps"]["preserve"]["log_lines_flagged"].pop(6)),
        "a finding dropped from preserve.log": slog(lambda b: b.replace(finding, b"")),
        "guards outcome changed": res(lambda r: r["steps"]["guards"].update(outcome="success")),
        "a TeX difference": res(lambda r: r.update(tex_files_differing=["papers/GR.tex"])),
        "a page count changed": res(lambda r: r["pdf_pages"].update({"papers/Structure.pdf": 94})),
        "wrong trial sha": res(lambda r: r.update(trial_sha="0" * 40)),
    }
    bad = 0
    for name, args in mutants.items():
        f = check(*args)
        print(f"  {'ok  ' if f else 'MISS'} mutant {name}: {f[0] if f else 'not caught'}")
        bad += not f
    print(f"self-test: {len(mutants) - bad}/{len(mutants)} mutants caught; RESULT {'PASS' if not bad else 'FAIL'}")
    return 1 if bad else 0


def pages(pdf_bytes):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "x.pdf")
        open(p, "wb").write(pdf_bytes)
        t = subprocess.run(["pdftotext", "-layout", p, "-"], capture_output=True, check=True).stdout
    ps = t.decode("utf-8", "replace").split("\f")
    return [x for x in ps if x.strip()]


def structure():
    zb, _, _, exp = load()
    built = zipfile.ZipFile(io.BytesIO(zb)).read("build/papers/Structure.pdf")
    committed = subprocess.run(["git", "-C", HERE, "show", f"{exp['workflow_sha']}:papers/Structure.pdf"],
                               capture_output=True, check=True).stdout
    c, b = pages(committed), pages(built)
    first = next((i for i, (x, y) in enumerate(zip(c, b)) if x != y), None)
    lines = lambda p: [l.strip() for l in p.splitlines() if l.strip()]
    print(f"committed (main {exp['workflow_sha'][:8]}): {len(c)} pages; CI-built: {len(b)} pages")
    print(f"first page whose text differs: {first + 1 if first is not None else 'none'}")
    print(f"last line of committed page {len(c)}: {lines(c[-1])[-2]}")
    print(f"CI-built page {len(b)}, in full:")
    for l in lines(b[-1]):
        print(f"  | {l}")
    # Attribution: compare the net word changes between the two PDFs with the net word changes of
    # papers/Structure.md between main and the trial commit (multisets, so reflow and reordering
    # cancel). Needs the trial commit's objects (branch trial/a1exit-T0-55544cc3).
    t = exp["trial_sha"]
    if subprocess.run(["git", "-C", HERE, "cat-file", "-e", t + "^{commit}"], capture_output=True).returncode:
        print(f"attribution: trial commit {t[:8]} not present; fetch it to run this part")
        return 0
    import re
    from collections import Counter
    def norm(w):
        return re.sub(r"[^\w]", "", w.replace("-", "").replace("\u2013", "").replace("\u2014", "")).lower()
    def pdfwords(pdf):
        with tempfile.TemporaryDirectory() as d:
            q = os.path.join(d, "x.pdf")
            open(q, "wb").write(pdf)
            txt = subprocess.run(["pdftotext", q, "-"], capture_output=True, check=True).stdout.decode()
        txt = re.sub(r"-\n", "", txt).replace("\f", " ")
        return Counter(n for n in map(norm, txt.split()) if n and not re.fullmatch(r"\d{1,3}", n))
    wd = subprocess.run(["git", "-C", HERE, "diff", "--word-diff=porcelain", "--word-diff-regex=[^[:space:]]+",
                         exp["workflow_sha"], t, "--", ":/papers/Structure.md"],
                        capture_output=True, check=True).stdout.decode()
    add, rem = Counter(), Counter()
    for l in wd.splitlines():
        if l.startswith("+") and not l.startswith("+++"):
            add.update(n for n in map(norm, l[1:].split()) if n)
        elif l.startswith("-") and not l.startswith("---"):
            rem.update(n for n in map(norm, l[1:].split()) if n)
    pc, pb = pdfwords(committed), pdfwords(built)
    md_add, md_rem, pdf_add, pdf_rem = add - rem, rem - add, pb - pc, pc - pb
    print(f"attribution: source net words +{sum(md_add.values())} -{sum(md_rem.values())}; "
          f"PDF net words +{sum(pdf_add.values())} -{sum(pdf_rem.values())}")
    print(f"  source additions absent from the PDF additions: {dict(md_add - pdf_add)}")
    print(f"  source removals absent from the PDF removals:   {dict(md_rem - pdf_rem)}")
    print(f"  PDF additions not from the source: {dict(pdf_add - md_add)}")
    print(f"  PDF removals not from the source:  {dict(pdf_rem - md_rem)}")
    return 0


def main(argv):
    if "--self-test" in argv:
        return self_test()
    if "--structure" in argv:
        return structure()
    zb, ret, lb, exp = load()
    if "--extract" in argv:
        d = argv[argv.index("--extract") + 1]
        z = zipfile.ZipFile(io.BytesIO(zb))
        for i in z.infolist():
            p = os.path.join(d, i.filename)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "wb").write(z.read(i))
        print(f"extracted {len(z.infolist())} members to {d}")
    f = check(zb, ret, lb, exp)
    if "--github" in argv:
        a = exp["artifact"]
        q = subprocess.run(["gh", "api", f"repos/amaybaum/incompleteness/actions/artifacts/{a['id']}",
                            "--jq", ".digest"], capture_output=True, text=True)
        host = q.stdout.strip()
        if host != "sha256:" + a["sha256"]:
            f.append(f"host artifact digest {host or q.stderr.strip()!r} differs from the recorded digest")
        else:
            print("host artifact digest matches the recorded digest")
    for x in f:
        print("  FAIL", x)
    print(f"T0 evidence: {len(exp['artifact']['members'])} artifact members, "
          f"{len(exp['preserve_findings'])} preserve findings; {len(f)} findings; "
          f"RESULT {'PASS' if not f else 'FAIL'}")
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
