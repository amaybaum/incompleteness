"""census_rm.py -- thread I1, stage 6: roadmap census (coverage control (c)).

Run from pt/I1/ as:  python3 -I -B census_rm.py > census_rm.out 2> census_rm.err
Read-only on ../base/verification/ROADMAP.md. Deterministic.

DECISION RULE (fixed before the first run).
ITEMS: every line of ROADMAP.md that is (a) a table row whose first cell is bold (`| **`), (b) a
bullet opening with a bold label (`- **`), (c) a `### ` heading, (d) a paragraph opening with
`**Executed`, or (e) one of the two unheaded accounting paragraphs in scope (the programme
interpretation boundary, line range 36-57, and the declared-inputs paragraph, 1452-1463), each
counted once at its first line.
MAPPING: by the section the item lies in (the enclosing `## `/`### ` heading) and, for queue rows,
by the obligation named in the row; in-scope items map to I1 record ids, others to
`OOS:<thread> (<reason>)`. The table SECTION_MAP below is the whole rule; an item no rule covers
is printed UNMAPPED and counted (a non-zero count is an incomplete census).
"""
import os
import re
import sys

PATH = os.path.join("..", "base", "verification", "ROADMAP.md")

QUEUE = [  # (substring of the obligation cell, mapping)
    ("What additional structure determines the relative quantum evolution", "OOS:I2 (P0: relative evolution inside the finite representation S<=>D<=>Q_fb, Track B)"),
    ("Substratum Lemma 24.1", "OOS:I2 (reconstruction: completeness of the substratum gauge group)"),
    ("A6 — background independence", "I1.61,I1.62,I1.68"),
    ("Physical C4 discharge", "I1.74"),
    ("H-Bell — composite and Bell closure", "OOS:I2 (Bell and composite closure)"),
    ("K — pre-quantum kinematics", "OOS:I3/I4 (K programme: K1, K2, K-infinity; K_n)"),
    ("Stochastic observer interface", "I1.76"),
    ("H-∞ — finite operational theory", "OOS:I2/I4 (continuum / Level III quasilocal completion)"),
    ("Bekir–Golomb", "OOS:I2 (reconstruction premise, physical layer)"),
    ("H-link", "OOS:I2 (SM physical layer)"),
    ("H-state / H-frame / H-slope", "OOS:I2 (GR physical layer)"),
    ("Covariant matter→boundary coupling", "OOS:I2 (GR physical layer)"),
    ("GR states → Level-III", "OOS:I2 (GR / Level III)"),
]

SECTION_MAP = [  # (heading substring, mapping) -- the enclosing heading decides non-queue items
    ("P0 — what fixes the relative evolution", "OOS:I2 (P0, Track B)"),
    ("Act 1", "OOS:I2 (P0, Track B acts)"),
    ("P1 — Substratum Lemma 24.1", "OOS:I2 (reconstruction: Lemma 24.1)"),
    ("P1 — A6", "I1.61,I1.62,I1.68"),
    ("P1 — physical C4 discharge", "I1.71,I1.72,I1.73,I1.74"),
    ("P1 — stochastic observer interface", "I1.76"),
    ("P1 — H-∞", "OOS:I2/I4 (continuum / Level III)"),
    ("P1 — H-Bell", "OOS:I2 (Bell and composite closure)"),
    ("P1 — K: pre-quantum kinematics", "OOS:I3/I4 (K programme)"),
    ("P2 —", "OOS:I2 (physical layer)"),
    ("P3 —", "OOS:I2 (GR / Level III)"),
    ("Hydrodynamics programme", "OOS:I2 (physical layer: hydrodynamics)"),
    ("Long-range conditional research directions", "OOS:I2 (P0 geometry / gauge-QFT directions)"),
    ("The 3×3", "OOS:I2 (P0 geometry)"), ("The residual deformation", "OOS:I2 (P0 geometry)"),
    ("The census of", "OOS:I2 (P0 geometry)"), ("Minimal support", "OOS:I2 (P0 geometry)"),
    ("The three-parameter family", "OOS:I2 (P0 geometry)"),
    ("Gauge/QFT extension", "OOS:I2 (physical layer: gauge/QFT)"),
    ("Settled negatively", "OOS:I4 (sourcing results: phases, dense control, layer flow, observer-level lift)"),
    ("Deliberately not prioritized", "OOS:I2 (not-prioritized items: instruments, representation, CT3, all-time, double slit)"),
    ("Declared inputs and conditional hypotheses", "I1.77"),
    ("Programme interpretation boundary", "I1.78"),
    ("Where new artifacts go", "OOS:none (repository placement rule; no premise)"),
    ("Status vocabulary", "OOS:none (vocabulary; fixes no premise)"),
    ("The queue", "QUEUE"),
    ("Verification roadmap", "OOS:none (preamble)"),
]


def main():
    with open(PATH, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    heading = ""
    items = []
    for i, ln in enumerate(lines, 1):
        if ln.startswith("## ") or ln.startswith("### ") or ln.startswith("# "):
            heading = ln.lstrip("# ").strip()
        kind = None
        if ln.startswith("| **"):
            kind = "row"
        elif ln.startswith("- **"):
            kind = "bullet"
        elif ln.startswith("### "):
            kind = "heading"
        elif ln.startswith("**Executed"):
            kind = "executed"
        elif i in (38, 1455):
            kind = "paragraph"
        if kind:
            items.append((i, kind, heading, ln))
    counts, unm = {}, []
    for (i, kind, heading, ln) in items:
        m = None
        for key, val in SECTION_MAP:
            if key in heading:
                m = val
                break
        if m == "QUEUE":
            m = None
            for key, val in QUEUE:
                if key in ln:
                    m = val
                    break
        if m is None:
            m = "UNMAPPED"
            unm.append(i)
        counts[m] = counts.get(m, 0) + 1
        print("ROADMAP.md:%d  %-9s  %s  | [%s] %s" % (i, kind, m, heading[:50], ln[:110]))
    print()
    print("== COUNTS: items %d" % len(items))
    for k in sorted(counts):
        print("  %4d  %s" % (counts[k], k))
    print("  UNMAPPED %d %s" % (len(unm), " ".join(str(u) for u in unm)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
