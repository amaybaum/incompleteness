#!/usr/bin/env python3
"""I2 manuscript and roadmap census (stage 6, Q-EX-FULL, step 1, coverage controls (b) and (c)).

DECISION RULE (fixed before the first run; the script decides no item's status):
1. Sections: the fixed list SECTIONS (I2's manuscript sections) and RM_SECTIONS (I2's ROADMAP rows/sections).
2. A manuscript line (paragraph) is split into sentences at [.?!] followed by whitespace and an upper-case
   letter, '*', '$', '(' or '['. A sentence is a census entry iff it matches KEY (the protocol's list:
   Axiom, Condition, C1-C4, (i)-(v), H-, K, A1-A6, Theorem, Lemma, Principle, Assumption, boxed statements;
   added for theorem kinds: Proposition, Corollary, lower-case hypothesis).
3. A ROADMAP entry is every queue-table row and every bullet ('- ' or '* ' at line start) and every bold-led
   paragraph ('**' at line start) inside RM_SECTIONS.
4. Each entry is joined with census_map.tsv (file, first line, last line, mapping text); the first matching
   range wins. An entry with no matching range is printed as UNMAPPED. Counts are printed per section and in
   total. Output is deterministic; no time stamp.
AMENDMENT before run 2 (run 1 = the listing pass without a map, kept as manuscript_census.run1.*):
5. (d) book mirrors: for each phrase of BOOK_PHRASES, every book/*.md line containing it is listed with the
   record it mirrors. The book is censused by mirror, not sentence by sentence.
AMENDMENT before run 3 (run 2 kept as manuscript_census.run2.*, superseded, not failed):
6. (e) residual screen: lines of Main, GR, SM, Substratum outside SECTIONS matching SCREEN are listed by line
   number; CENSUS.md classifies them by section. The screen is a coverage control, not a census of sentences.
AMENDMENT before run 4 (run 3 kept as manuscript_census.run3.*, superseded, not failed): SECTIONS extended,
identically in kernel_census.py, by GR 326-330, GR 753-866, Substratum 236-242, 414-416, 430 (found by (e)).
"""
import os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "../base"
MAP = sys.argv[2] if len(sys.argv) > 2 else "census_map.tsv"
SECTIONS = [
    ("papers/Main.md", 14, 22), ("papers/Main.md", 82, 82), ("papers/Main.md", 95, 99),
    ("papers/Main.md", 101, 196), ("papers/Main.md", 200, 656), ("papers/Main.md", 660, 678),
    ("papers/Main.md", 696, 720), ("papers/Main.md", 722, 740), ("papers/Main.md", 744, 756),
    ("papers/GR.md", 164, 296), ("papers/GR.md", 326, 330), ("papers/GR.md", 709, 866),
    ("papers/SM.md", 10, 16), ("papers/SM.md", 40, 95), ("papers/SM.md", 96, 165),
    ("papers/SM.md", 216, 279), ("papers/SM.md", 535, 566), ("papers/SM.md", 1354, 1369),
    ("papers/SM.md", 1576, 1635),
    ("papers/Substratum.md", 12, 40), ("papers/Substratum.md", 42, 65), ("papers/Substratum.md", 70, 173),
    ("papers/Substratum.md", 186, 195), ("papers/Substratum.md", 236, 242),
    ("papers/Substratum.md", 414, 416), ("papers/Substratum.md", 430, 430),
]
RM_SECTIONS = [("verification/ROADMAP.md", 63, 63), ("verification/ROADMAP.md", 67, 67),
               ("verification/ROADMAP.md", 70, 70), ("verification/ROADMAP.md", 75, 75),
               ("verification/ROADMAP.md", 77, 664), ("verification/ROADMAP.md", 936, 970),
               ("verification/ROADMAP.md", 1148, 1157)]
KEY = re.compile(r"(\bAxiom\b|\bCondition\b|\bC[1-4]\b|\((?:i|ii|iii|iv|v)\)|\bH-|\bK\b|\bA[1-6]\b|\bTheorem\b|"
                 r"\bLemma\b|\bPrinciple\b|\bAssumption\b|\\boxed|\bProposition\b|\bCorollary\b|\bhypothesis\b)")
SPLIT = re.compile(r"(?<=[.?!])\s+(?=[A-Z*$(\[])")


def load_map(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            raw = raw.rstrip("\n")
            if not raw or raw.startswith("#"):
                continue
            parts = raw.split("\t")
            rows.append((parts[0], int(parts[1]), int(parts[2]), parts[3] if len(parts) > 3 else ""))
    return rows


def lookup(rows, rel, ln):
    for (r, a, b, m) in rows:
        if r == rel and a <= ln <= b:
            return m
    return None


def main():
    rows = load_map(MAP) if os.path.exists(MAP) else []
    total = 0
    unmapped = 0
    lines_total = 0
    print("# I2 manuscript census (b)")
    for (rel, a, b) in SECTIONS:
        ls = open(os.path.join(ROOT, rel), encoding="utf-8").read().split("\n")
        sec_n = 0
        for ln in range(a, min(b, len(ls)) + 1):
            text = ls[ln - 1]
            if not text.strip():
                continue
            sents = SPLIT.split(text)
            hits = [s for s in sents if KEY.search(s)]
            if not hits:
                continue
            keys = sorted(set(k for s in hits for k in KEY.findall(s)))
            m = lookup(rows, rel, ln)
            sec_n += len(hits)
            lines_total += 1
            if m is None:
                unmapped += 1
            print("%s:%d sentences=%d/%d keys=%s map=%s" % (rel, ln, len(hits), len(sents), ",".join(keys),
                                                            m if m is not None else "UNMAPPED"))
        total += sec_n
        print("SECTION %s:%d-%d keyword-sentences=%d" % (rel, a, b, sec_n))
    print("MANUSCRIPT TOTAL keyword-sentences=%d lines=%d unmapped-lines=%d" % (total, lines_total, unmapped))
    print()
    print("# I2 roadmap census (c)")
    rtotal = 0
    runmapped = 0
    for (rel, a, b) in RM_SECTIONS:
        ls = open(os.path.join(ROOT, rel), encoding="utf-8").read().split("\n")
        n = 0
        for ln in range(a, min(b, len(ls)) + 1):
            text = ls[ln - 1]
            if re.match(r"^\| \*\*P[0-9]", text) or re.match(r"^\s*[-*] ", text) or text.startswith("**"):
                m = lookup(rows, rel, ln)
                n += 1
                if m is None:
                    runmapped += 1
                lead = re.sub(r"\s+", " ", text)[:90]
                print("%s:%d %s map=%s" % (rel, ln, lead, m if m is not None else "UNMAPPED"))
        rtotal += n
        print("SECTION %s:%d-%d entries=%d" % (rel, a, b, n))
    print("ROADMAP TOTAL entries=%d unmapped=%d" % (rtotal, runmapped))
    # (d) book mirrors — added before run 2: every line of book/*.md containing a phrase of BOOK_PHRASES,
    # reported per phrase with the record it mirrors (the book restates; it adds no record of its own here).
    print()
    print("# I2 book-mirror census (d)")
    bdir = os.path.join(ROOT, "book")
    files = sorted(f for f in os.listdir(bdir) if f.endswith(".md"))
    for phrase, rec in BOOK_PHRASES:
        hits = []
        for f in files:
            for i, t in enumerate(open(os.path.join(bdir, f), encoding="utf-8").read().split("\n"), 1):
                if phrase in t:
                    hits.append("%s:%d" % (f, i))
        print("PHRASE %r -> %s hits=%d %s" % (phrase, rec, len(hits), " ".join(hits)))
    # (e) residual screen — added before run 3: lines of Main, GR, SM, Substratum OUTSIDE SECTIONS that contain a
    # composition/locality/operation term of SCREEN; listed per file so CENSUS.md can classify each block.
    print()
    print("# I2 residual screen (e)")
    for rel in ("papers/Main.md", "papers/GR.md", "papers/SM.md", "papers/Substratum.md"):
        ls = open(os.path.join(ROOT, rel), encoding="utf-8").read().split("\n")
        out = []
        for i, t in enumerate(ls, 1):
            if any(r == rel and a <= i <= b for (r, a, b) in SECTIONS):
                continue
            if SCREEN.search(t):
                out.append(i)
        print("RESIDUAL %s lines=%d %s" % (rel, len(out), " ".join(str(x) for x in out)))


SCREEN = re.compile(r"composite|tensor product|no-signal|locality|causal cone|spectator|\bBell\b|subsystem|"
                    r"local tomography|operational|trace-out|bipartite|Kochen")


BOOK_PHRASES = [
    ("Q_{\\mathrm{fb}}", "I2.39"), ("hidden predictive memory", "I2.44"), ("predictive quotient", "I2.45"),
    ("process dilation", "I2.40"), ("Stinespring", "I2.19/I2.59"), ("P-indivisib", "I2.48/I2.50"),
    ("causal cone", "I2.1/I2.2"), ("Bell ceiling", "I2.5"), ("ontic parameter dependence", "I2.6"),
    ("no-signal", "I2.10"), ("H-Bell", "I2.102"), ("local tomography", "I2.2/I2.3/I2.63"),
    ("gluing", "I2.12"), ("Kochen", "I2.14"), ("inert spectators", "I2.29"), ("OI⁺", "I2.31"),
    ("operational-completion", "I2.29"), ("quasilocal", "I2.36"), ("tensor product", "I2.19/I2.2"),
]


if __name__ == "__main__":
    main()
