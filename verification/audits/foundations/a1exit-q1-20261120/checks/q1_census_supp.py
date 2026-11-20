#!/usr/bin/env python3
"""Q1 supplementary census (post-preregistration deviation, RESULT section 6a).

Added after the round-1 review found a consumer line (book ch05:154) that the preregistered pattern
families missed. Lists every line of papers/*.md and book/*.md that is NOT in q1_census.json and
matches one of three further families, and writes the hits as JSON:
  G5 blocking and sublattice vocabulary; G6 "taste"; G7 "corner".
Lines matching G6 or G7 only are further marked "screen" when they also contain a lattice-shape
word (lattice, sublattice, periodic, torus, site, hypercube), so that they get a line-by-line reading.
Run from the repository root:
    python3 -I verification/audits/foundations/a1exit-q1-20261120/checks/q1_census_supp.py [out.json]
Exit status 0 always: this is a census, not a verdict.
"""
import glob
import json
import re
import sys

D = "verification/audits/foundations/a1exit-q1-20261120/checks/"
FAMILIES = {
    "G5-blocking": (r"hypercube corner|[Ss]ublattice parity|[Bb]locked|sublattice grading|"
                    r"even sublattice|odd sublattice|[Ss]ublattices"),
    "G6-taste": r"[Tt]aste",
    "G7-corner": r"[Cc]orner",
}
SCREEN = r"lattice|periodic|torus|\bsite|hypercube"


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else None
    old = {(h["file"], h["line"]) for h in json.load(open(D + "q1_census.json", encoding="utf-8"))}
    files = sorted(glob.glob("papers/*.md")) + sorted(glob.glob("book/*.md"))
    hits = []
    for f in files:
        with open(f, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if (f, n) in old:
                    continue
                fams = [k for k, p in FAMILIES.items() if re.search(p, line)]
                if fams:
                    screen = "G5-blocking" in fams or bool(re.search(SCREEN, line))
                    hits.append({"file": f, "line": n, "families": fams, "screen": screen})
    counts = {}
    for h in hits:
        for k in h["families"]:
            counts[k] = counts.get(k, 0) + 1
    print("new lines:", len(hits), counts, "screened:", sum(h["screen"] for h in hits),
          "non-FULL screened:", sum(h["screen"] for h in hits if "FULL" not in h["file"]))
    if out:
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(hits, fh, indent=1)
            fh.write("\n")


if __name__ == "__main__":
    main()
