#!/usr/bin/env python3
"""Q1 consumer census (stdlib only, deterministic).

Lists every line of the manuscript corpus (papers/*.md, book/*.md) that matches one of the
preregistered lattice-shape pattern families, and writes the hits as JSON.
Run from the repository root:
    python3 -I verification/audits/foundations/a1exit-q1-20261120/checks/q1_census.py [out.json]
Exit status 0 always: this is a census, not a verdict. The hit list is the output.
"""
import glob
import json
import re
import sys

FAMILIES = {
    # G4: A4's finite class and its restatements
    "G4-finite-class": r"finite periodic lattice|periodic quotient|finite-index sublattice|period lattice",
    # G1: checkerboard / bipartite structure of the coupling graph
    "G1-bipartite": r"[Bb]ipartite|[Cc]heckerboard",
    # G2: Brillouin-zone corners, staggered phases and the staggered reconstruction on the lattice
    "G2-corners": (r"Brillouin[- ]zone corner|BZ corner|2\^3 ?= ?8|2\^d ?= ?8|eight corners|"
                   r"staggered phase|staggered-to-Dirac"),
    # G3: the cubic point group acting on the carrier
    "G3-cubic": r"O_h|by cubic symmetry|cubic group O\b|group \$O\$|cubic symmetry",
    # the theorem labels of the named consumers
    "L-labels": r"Theorem (2|3|8|8b|10|12|13)\b",
}


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else None
    files = sorted(glob.glob("papers/*.md")) + sorted(glob.glob("book/*.md"))
    hits = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                fams = [k for k, p in FAMILIES.items() if re.search(p, line)]
                if fams:
                    hits.append({"file": f, "line": n, "families": fams})
    counts = {}
    for h in hits:
        for k in h["families"]:
            counts.setdefault(k, {}).setdefault(h["file"], 0)
            counts[k][h["file"]] += 1
    for k in FAMILIES:
        tot = sum(counts.get(k, {}).values())
        print(f"{k}: {tot} lines")
        for f, c in sorted(counts.get(k, {}).items()):
            print(f"    {f}: {c}")
    print(f"total distinct lines: {len(hits)}")
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(hits, fh, indent=1)
            fh.write("\n")


if __name__ == "__main__":
    main()
