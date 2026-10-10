"""I3 manuscript census (coverage control (b)) and roadmap census (coverage control (c)).

DECISION RULE (fixed before the first run):
(b) Manuscripts: every line of pt/base/papers/*.md and pt/base/book/*.md matching the K-programme vocabulary regex
    VOCAB below is a census hit; the output lists file:line, the matched terms (deduplicated, in order) and the first
    240 characters of the line. Hits are mapped by hand in CENSUS.md to a record id or to an out-of-scope thread with a
    reason; a pure word coincidence (e.g. a gene name) is listed as "no statement (vocabulary coincidence)".
(c) Roadmap: (i) every line of pt/base/verification/ROADMAP.md in the K section, lines 971-1102 (from the heading
    "### P1 — K: pre-quantum kinematics" to the line before "### P2 — Bekir–Golomb"), that begins a unit: a heading,
    a top-level bullet "- **", a sub-bullet "  - **", a bold paragraph start "**", an indented paragraph start (two
    spaces then a capital letter, after a blank line), a code fence, or a link line "→ "; (ii) every line outside that
    section matching ROADMAP_K. Each unit is mapped by hand in CENSUS.md.
The section bounds are checked: line 971 must start with "### P1 — K" and line 1104 with "### P2"; a mismatch prints
BOUNDS-MISMATCH and the section is still scanned from the heading found by search.
Deterministic output, no timestamps.
"""
import glob
import os
import re
import sys

BASE = os.path.join("..", "base")
VOCAB = re.compile(
    r"K∞|Kₙ|\bK1\b|\bK2\b|pre-quantum|field-neutral|native gate|NativeGate|native-gate|dimension selector|DIM-1|"
    r"drivab|ElementaryDrivability|local tomograph|locally tomographic|tomographic[- ]locality|copy natural|"
    r"boundary[- ]transitiv|continuous[- ]transitiv|sharp seed|four-copy|KT\(4\)|Bloch ball|elementary system|"
    r"reconstruction theorem|operational axiom|Masanes|Chiribella|Hardy|self-dual|Barnum|Wilce"
)
ROADMAP_K = re.compile(r"K∞|Kₙ|\bK1\b|\bK2\b|\bK3\b|pre-quantum|DIM-1|NB-1|EFF-1|OG-1|TRB-1|CMP-1|OPACT|COMP-1|ORD-1|"
                       r"KINF|K1-|K2-|KTRANS|PARITY-NOT|ODD-CHAR|RELC|KT4|IIP-1|drivab|NativeGate")


def manuscripts():
    files = sorted(glob.glob(os.path.join(BASE, "papers", "*.md"))) + sorted(glob.glob(os.path.join(BASE, "book", "*.md")))
    print("## (b) manuscript census")
    print(f"files scanned: {len(files)}")
    n = 0
    for f in files:
        with open(f, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                terms = []
                for m in VOCAB.finditer(line):
                    if m.group(0) not in terms:
                        terms.append(m.group(0))
                if terms:
                    n += 1
                    rel = os.path.relpath(f, BASE)
                    print(f"M{n:03d} {rel}:{i} [{', '.join(terms)}] {line.strip()[:240]}")
    print(f"manuscript hits: {n}")


def roadmap():
    path = os.path.join(BASE, "verification", "ROADMAP.md")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    print()
    print("## (c) roadmap census")
    start = next(i for i, l in enumerate(lines) if l.startswith("### P1 — K"))
    end = next(i for i, l in enumerate(lines) if l.startswith("### P2 — Bekir"))
    ok = lines[970].startswith("### P1 — K") and lines[1103].startswith("### P2")
    print(f"K section: lines {start + 1}-{end} ; bounds check {'OK' if ok else 'BOUNDS-MISMATCH'}")
    n = 0
    prev_blank = True
    for i in range(start, end):
        l = lines[i]
        unit = (l.startswith("### ") or l.startswith("- **") or l.startswith("  - **") or l.startswith("**")
                or l.startswith("```") or l.startswith("→ ")
                or (prev_blank and re.match(r"^  [A-Z]", l) is not None)
                or (prev_blank and re.match(r"^[A-Z]", l) is not None))
        if unit:
            n += 1
            print(f"R{n:03d} ROADMAP.md:{i + 1} {l.strip()[:200]}")
        prev_blank = (l.strip() == "")
    print(f"K-section units: {n}")
    m = 0
    for i, l in enumerate(lines):
        if start <= i < end:
            continue
        if ROADMAP_K.search(l):
            m += 1
            terms = []
            for mm in ROADMAP_K.finditer(l):
                if mm.group(0) not in terms:
                    terms.append(mm.group(0))
            print(f"X{m:03d} ROADMAP.md:{i + 1} [{', '.join(terms)}] {l.strip()[:200]}")
    print(f"outside-section hits: {m}")
    print("END")


if __name__ == "__main__":
    manuscripts()
    roadmap()
    sys.exit(0)
