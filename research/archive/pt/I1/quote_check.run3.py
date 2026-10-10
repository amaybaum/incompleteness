"""quote_check.py -- thread I1, stage 6: are INVENTORY.md's quotations exact?

Run from pt/I1/ as:  python3 -I -B quote_check.py > quote_check.out 2> quote_check.err
Read-only on ../base/ and on INVENTORY.md. Deterministic.

DECISION RULE (fixed before the first run).
  1. In INVENTORY.md (line wraps joined: newline plus indentation -> one space), find every
     citation immediately followed by a double-quoted string, of the forms
     `<Paper>.md:<a>[–<b>] "<q>"`, `ch01(-observation.md)?:<a> "<q>"`, `ROADMAP.md:<a>[–<b>] "<q>"`,
     `README.md:<a>[–<b>] "<q>"`, `<Module>.lean:<a>[–<b>] "<q>"`; `<q>` ends at the next `"`.
  2. Split `<q>` at the ellipsis `…`; every fragment of length >= 12 after stripping must occur in
     the whitespace-normalized concatenation of the cited source lines a .. max(a, b) + 3 (Lean:
     a .. max(a, b) + 12, docstrings run on), after removing Lean comment leaders.
  3. Report each check PASS/FAIL with its location. VERDICT ALL-EXACT iff every fragment passes;
     otherwise FAILURES n (each failure is to be corrected in INVENTORY.md, never in the source).
  Countercontrol (must hold or the run is VOID): a deliberately altered fragment (one character
  changed in the first checked fragment) must FAIL against its own source window.

RUN 3 AMENDMENT (pre-run edit, recorded in NOTES.md; runs 1-2 kept as quote_check.run1.*/run2.*):
run 2 checked only quotations whose citation names its file. Run 3 also checks the relative form
`:<a>[–<b>] "<q>"` (a line citation with no file name), resolving the file to the last file named
explicitly earlier in the same record (a record is the text from one `**I1.` heading to the next).
Nothing else changes; a relative citation with no earlier file in its record is skipped.
"""
import os
import re
import sys

BASE = os.path.join("..", "base")
OIB = os.path.join(BASE, "verification", "lean-mathlib", "OIBridge")
PAPERS = {"Main": "papers/Main.md", "Methodology": "papers/Methodology.md",
          "Substratum": "papers/Substratum.md", "Explainer": "papers/Explainer.md"}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def src_lines(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read().split("\n")


def window(path, a, b, extra, lean):
    ls = src_lines(path)
    hi = min(len(ls), max(a, b or a) + extra)
    seg = []
    for ln in ls[a - 1:hi]:
        t = ln
        if lean:
            t = re.sub(r"^\s*/--\s?", "", t)
            t = re.sub(r"\s?-/\s*$", "", t)
        seg.append(t)
    return norm(" ".join(seg))


def main():
    with open("INVENTORY.md", encoding="utf-8") as fh:
        inv = fh.read()
    inv = re.sub(r"\n\s+", " ", inv)
    pat = re.compile(r"(?:(Main|Methodology|Substratum|Explainer)\.md|(ch01)(?:-observation\.md)?|"
                     r"(ROADMAP)\.md|(README)\.md|([A-Za-z0-9]+)\.lean):(\d+)(?:[–-](\d+))?:?\s+\"([^\"]+)\"")
    checks = fails = 0
    first = None
    found = list(pat.finditer(inv))
    rel = re.compile(r"(?<![A-Za-z0-9_.)])\s:(\d+)(?:[–-](\d+))?:?\s+\"([^\"]+)\"")
    starts = [mm.start() for mm in re.finditer(r"\*\*I1\.", inv)] + [len(inv)]
    for r in rel.finditer(inv):
        rs = max([x for x in starts if x <= r.start()] or [0])
        prev = [m for m in found if rs <= m.start() < r.start()]
        if not prev:
            continue
        pm = prev[-1]
        g = list(pm.groups())
        g[5], g[6], g[7] = r.group(1), r.group(2), r.group(3)
        found.append(type("M", (), {"groups": (lambda gg: (lambda self=None: tuple(gg)))(g),
                                    "start": (lambda st: (lambda self=None: st))(r.start())})())
    found.sort(key=lambda m: m.start())
    for m in found:
        paper, ch, rm, rd, mod, a, b, q = m.groups()
        a = int(a)
        b = int(b) if b else None
        if paper:
            path, extra, lean = os.path.join(BASE, PAPERS[paper]), 3, False
        elif ch:
            path, extra, lean = os.path.join(BASE, "book", "ch01-observation.md"), 3, False
        elif rm:
            path, extra, lean = os.path.join(BASE, "verification", "ROADMAP.md"), 3, False
        elif rd:
            path, extra, lean = os.path.join(BASE, "verification", "README.md"), 3, False
        else:
            path, extra, lean = os.path.join(OIB, mod + ".lean"), 12, True
            if not os.path.exists(path):
                continue
        w = window(path, a, b, extra, lean)
        for frag in q.split("…"):
            f = norm(frag)
            if len(f) < 12:
                continue
            checks += 1
            ok = f in w
            if first is None:
                first = (f, w)
            if not ok:
                fails += 1
            print("%s  %s:%d%s  | %s" % ("PASS" if ok else "FAIL", os.path.relpath(path, BASE), a,
                                         ("-%d" % b) if b else "", f[:110]))
    ctrl_ok = False
    if first is not None:
        f, w = first
        altered = f[:5] + ("X" if f[5] != "X" else "Y") + f[6:]
        ctrl_ok = altered not in w
    print("countercontrol (altered fragment fails): %s" % ctrl_ok)
    print("checks %d  failures %d" % (checks, fails))
    if not ctrl_ok:
        print("VERDICT VOID")
    elif fails == 0:
        print("VERDICT ALL-EXACT")
    else:
        print("VERDICT FAILURES %d" % fails)
    return 0


if __name__ == "__main__":
    sys.exit(main())
