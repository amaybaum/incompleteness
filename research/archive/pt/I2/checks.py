#!/usr/bin/env python3
"""I2 integrity checks on the inventory (stage 6, Q-EX-FULL, step 1).

DECISION RULE (fixed before the first run):
Q (quote check): every line of INVENTORY.md of the form `- statement [<path>:<line>]: ...` is parsed; every
  fragment between « and » must be a substring of line <line> of pt/base/<path>. PASS iff every fragment matches.
  Countercontrol Q-neg: a deliberately altered copy of the first fragment (one character appended) must FAIL to
  match; the check is void if the countercontrol matches.
X (cross-reference check): every token I2.<n> in INVENTORY.md and CENSUS.md must name a record header
  `### I2.<n> — ` of INVENTORY.md. PASS iff no dangling reference. Record ids must be 1..N without gaps.
B (bridge check): for each I2 kernel module listed by kernel_census.out (owner=I2), the source must not contain
  any of the pair-cone identifiers PAIR (word match) nor import a K-programme module. PASS iff no hit.
  Countercontrol B-neg: the same test on CompositeDimension.lean must report hits; the check is void otherwise.
Verdict lines print only when the countercontrols behave as stated. Output is deterministic.
"""
import os, re, sys

ROOT = "../base"
INV = "INVENTORY.md"
CEN = "CENSUS.md"
LEAN = os.path.join(ROOT, "verification", "lean-mathlib", "OIBridge")
PAIR = ["CompositeDimension", "K2Guard", "KInfFoundations", "maxCone", "cnot", "prodState", "dualW", "NativeGate",
        "eball"]
PAIR_RE = re.compile(r"(?<![A-Za-z0-9_])(" + "|".join(PAIR) + r")(?![A-Za-z0-9_])|\bW 3\b")
IMPORT_RE = re.compile(r"^import OIBridge\.(CompositeDimension|K2Guard|KInfFoundations|OrbitGeneration|TransitiveBody)")


def lines_of(p):
    with open(p, encoding="utf-8") as f:
        return f.read().split("\n")


def main():
    inv = lines_of(INV)
    # --- Q
    stmt_re = re.compile(r"^- statement \[([^\]:]+):(\d+)\]: (.*)$")
    frag_re = re.compile(r"«(.*?)»")
    nq = 0
    bad = []
    first = None
    cache = {}
    for i, l in enumerate(inv, 1):
        m = stmt_re.match(l)
        if not m:
            continue
        path, ln, rest = m.group(1), int(m.group(2)), m.group(3)
        if path not in cache:
            cache[path] = lines_of(os.path.join(ROOT, path))
        src = cache[path][ln - 1] if 0 < ln <= len(cache[path]) else ""
        for fr in frag_re.findall(rest):
            nq += 1
            if first is None:
                first = (fr, src)
            if fr not in src:
                bad.append((i, path, ln, fr[:80]))
    print("Q: fragments checked %d, mismatches %d" % (nq, len(bad)))
    for b in bad:
        print("Q-MISMATCH inventory:%d %s:%d «%s»" % b)
    qneg_ok = first is not None and (first[0] + "⁂") not in first[1]
    print("Q-neg countercontrol (altered fragment must not match): %s" % ("behaves" if qneg_ok else "VOID"))
    # --- X
    heads = []
    for l in inv:
        m = re.match(r"^### I2\.(\d+) — ", l)
        if m:
            heads.append(int(m.group(1)))
    ids = set(heads)
    texts = "\n".join(inv)
    if os.path.exists(CEN):
        texts += "\n" + "\n".join(lines_of(CEN))
    refs = set(int(x) for x in re.findall(r"I2\.(\d+)", texts))
    dangling = sorted(r for r in refs if r not in ids)
    dup = sorted(set(h for h in heads if heads.count(h) > 1))
    gaps = sorted(set(range(1, max(heads) + 1)) - ids) if heads else []
    print("X: records %d (max id %d), references %d, dangling %s, duplicates %s, gaps %s" % (
        len(heads), max(heads) if heads else 0, len(refs), dangling or "none", dup or "none", gaps or "none"))
    # --- B
    mods = []
    for l in lines_of("kernel_census.out"):
        m = re.match(r"^MODULE (\S+)\s+owner=I2\b", l)
        if m:
            mods.append(m.group(1))
    hits = []
    for m in mods:
        for j, l in enumerate(lines_of(os.path.join(LEAN, m + ".lean")), 1):
            if PAIR_RE.search(l) or IMPORT_RE.match(l):
                hits.append("%s:%d" % (m, j))
    neg = sum(1 for l in lines_of(os.path.join(LEAN, "CompositeDimension.lean")) if PAIR_RE.search(l))
    print("B: I2 modules scanned %d, pair-cone hits %d %s" % (len(mods), len(hits), " ".join(hits[:20])))
    print("B-neg countercontrol (CompositeDimension.lean must hit): %d hits -> %s" % (neg, "behaves" if neg > 0 else "VOID"))
    if qneg_ok and neg > 0:
        print("VERDICT Q %s; X %s; B %s" % ("PASS" if not bad else "FAIL",
                                             "PASS" if not dangling and not dup and not gaps else "FAIL",
                                             "PASS" if not hits else "FAIL"))
    else:
        print("NO VERDICT (countercontrol void)")


if __name__ == "__main__":
    main()
