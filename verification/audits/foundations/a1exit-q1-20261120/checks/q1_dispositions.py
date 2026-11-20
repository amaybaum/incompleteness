#!/usr/bin/env python3
"""Q1 census dispositions (stdlib only, deterministic). Exit status 0 iff every census hit has
exactly one disposition, every disposition names a census hit, and every FULL hit is an exact
mirror of a chapter line that has a disposition.

Codes (PREREG section 2): P primary consumer; R restates (edit id if a correction is proposed);
I inherits; S stencil / abstract / O-A4-classified; N unrelated; A4 restates A4's finite class
(disposition belongs to the A1-EXIT ledger; no Q1 condition).
Run from the repository root:
    python3 -I verification/audits/foundations/a1exit-q1-20261120/checks/q1_dispositions.py
"""
import glob
import json
import sys

D = "verification/audits/foundations/a1exit-q1-20261120/checks/"

# (file stem, line) -> (code, edit, note)
T = {}


def put(stem, lines, code, edit="", note=""):
    for n in lines:
        T[(stem, n)] = (code, edit, note)


put("papers/Complexity.md", [63, 168], "I", "", "cites Theorem 13 with its conditions")
put("papers/GR.md", [162], "S", "", "SM 3.1 rotational protection; O-A4 row 16")
put("papers/Juno.md", [77, 301], "S", "", "abstract group O")
put("papers/Juno.md", [79], "I", "", "cites Theorem 10")
put("papers/Main.md", [218], "I", "", "describes an open step; asserts no lattice property")
put("papers/Main.md", [286], "N", "", "Nielsen-Chuang Theorem 8.1")
put("papers/Main.md", [674, 678], "S", "", "step kernel on Z^3 with increments n +- e_i; lattice-shape free")
put("papers/Main.md", [893], "N", "", "bibliography")
put("papers/SM.md", [12, 26, 130, 258, 264, 266, 268, 270, 338, 360, 376, 384, 416, 418, 944],
    "S", "", "observer-level isotropy, point-group algebra or stencil symmetry; O-A4 rows 13-17")
put("papers/SM.md", [134, 136], "I", "E1", "O_h-invariant checkerboard partition about the observer's centre; "
    "on a quotient needs P cubic-invariant and even-sum (E1)")
put("papers/SM.md", [202], "A4", "", "growth exponent under A4; O-A4 row 4")
put("papers/SM.md", [222], "R", "E1", "introduces the finite quotient of Lambda without the conditions on P")
put("papers/SM.md", [286], "P", "", "C2 Theorem 2")
put("papers/SM.md", [302], "P", "", "C3 Theorem 3 (self-conditioned)")
put("papers/SM.md", [434, 436], "P", "", "C8 Theorem 8 and proof")
put("papers/SM.md", [440], "P", "", "C8b Theorem 8b")
put("papers/SM.md", [446], "P", "E5", "C8b proof step 'related by cubic symmetry'; arithmetic suffices")
put("papers/SM.md", [456, 460], "P", "", "C10 Theorem 10 and proof")
put("papers/SM.md", [535, 537], "P", "", "C12 Theorem 12 and proof")
put("papers/SM.md", [539], "P", "E2", "C539 spin-taste sentence needs P in 2Z^3")
put("papers/SM.md", [543, 545], "P", "", "C13 Theorem 13 and proof")
put("papers/SM.md", [1506], "R", "E3", "same list as SM:1536")
put("papers/SM.md", [1536], "P", "E3", "C1536 bipartite checkerboard among exact symmetries")
put("papers/SM.md", [290, 306, 308, 452, 483, 485, 513, 527, 529, 531, 553, 555, 557, 565, 569, 611, 629,
                     659, 765, 853, 867, 907, 911, 915, 954, 967, 1006, 1086, 1108, 1170, 1184, 1193, 1225,
                     1233, 1241, 1253, 1320, 1446, 1452, 1512, 1532, 1554, 1568],
    "I", "", "uses a primary consumer's conclusion or the corners/tastes of Lambda; covered by E1")
put("papers/SM.md", [647, 649, 661], "S", "", "Proposition 20's abstract bipartite C_4 ring / coupling graph")
put("papers/Structure.md", [1044, 1058], "I", "", "cites SM 4.7 / summarizes SM 8.7's mapping")
put("papers/Substratum.md", [3], "S", "", "abstract: equivariant projection")
put("papers/Substratum.md", [98], "A4", "", "CA4: A4's finite clause (no Q1 consumer uses it)")
put("papers/Substratum.md", [157], "A4", "", "growth exponent under A4")
put("papers/Substratum.md", [165, 505], "I", "", "checkerboard trace-out / Theorem 2 measure reduction")
put("papers/Substratum.md", [304, 585], "N", "", "Theorem 2.4 of a cited monograph")
put("book/appendix-a-prediction-status.md", [54], "S", "", "classification vocabulary")
put("book/appendix-b-derivations.md", [50], "N", "", "Nielsen-Chuang Theorem 8.1")
put("book/appendix-b-derivations.md", [299, 301, 305, 344, 346, 364, 389, 395, 472], "S", "",
    "point-group algebra, Bravais comparison, verification recipe on abstract corners")
put("book/appendix-b-derivations.md", [330, 374, 380, 382], "I", "", "tastes of the simple cubic lattice")
put("book/appendix-b-derivations.md", [378], "R", "", "'on a d = 3 simple cubic lattice': the Bravais lattice Z^3, "
    "true as stated; no correction")
put("book/bibliography.md", [71], "N", "", "bibliography")
put("book/ch00-introduction.md", [97], "I", "", "checkerboard reduction under H-chi'")
put("book/ch01-observation.md", [284], "N", "", "NR-1 Theorem 3.3")
put("book/ch02-substratum.md", [82, 96], "A4", "", "A4 mirror / growth under A4")
put("book/ch02-substratum.md", [104, 226], "I", "", "checkerboard parity grading; chain summary")
put("book/ch04-methodology.md", [128], "S", "", "rotational anisotropy, operator mixing")
put("book/ch05-gauge-structure.md", [4, 85, 112], "S", "", "observer-level isotropy; cubic rotation group on links")
put("book/ch05-gauge-structure.md", [65], "A4", "", "growth exponent under A4")
put("book/ch05-gauge-structure.md", [95, 152, 191], "I", "", "Theorem 3; checkerboard branch")
put("book/ch05-gauge-structure.md", [160], "I", "", "already conditioned: 'for a cubic lattice with bipartite coupling'")
put("book/ch06-matter-content.md", [8, 26, 32, 58, 168], "I", "", "tastes / checkerboard of the cubic lattice")
put("book/ch06-matter-content.md", [22], "R", "E4", "eight corners 'on a d = 3 lattice' under the book's A4")
put("book/ch06-matter-content.md", [24, 30], "R", "E4", "triplet tastes related by cubic symmetry")
put("book/ch06-matter-content.md", [64], "S", "", "abstract C_4 example")
put("book/ch07-gravity.md", [126, 128], "N", "", "bipartite quantum system")
put("book/ch08-juno.md", [34, 36, 179], "S", "", "abstract group O")
put("book/ch09-universality.md", [155], "S", "", "breaking of cubic symmetry by phi")
put("book/ch18-beyond.md", [242], "A4", "", "'a compact identification can give a finite periodic lattice': true; "
    "no Q1 condition")
put("book/ch19-open-problems.md", [80], "S", "", "abstract C_4 ring")
put("book/ch19-open-problems.md", [106, 108, 150, 160, 252], "I", "", "generations / Theorem 10 / Theorem 13")
put("book/ch19-open-problems.md", [228, 232, 246], "S", "", "rotational protection (SM 3.1)")
put("book/glossary.md", [43], "I", "", "'staggered bipartite structure on the cubic lattice'")

FULL = "book/The-Incompleteness-of-Observation-FULL.md"


def main():
    hits = json.load(open(D + "q1_census.json", encoding="utf-8"))
    keys = {(h["file"], h["line"]) for h in hits}
    errors = []
    # chapter-line index for FULL mirrors
    chap = {}
    for f in sorted(glob.glob("book/*.md")):
        if f == FULL:
            continue
        for i, l in enumerate(open(f, encoding="utf-8").read().split("\n"), 1):
            if l.strip():
                chap.setdefault(l, []).append((f, i))
    full = open(FULL, encoding="utf-8").read().split("\n")
    out = []
    for h in hits:
        k = (h["file"], h["line"])
        if h["file"] == FULL:
            src = [s for s in chap.get(full[h["line"] - 1], []) if s in T]
            if len(src) != 1:
                errors.append(f"FULL:{h['line']} mirrors {chap.get(full[h['line'] - 1])}")
                continue
            code, edit, note = T[src[0]]
            out.append({**h, "code": code, "edit": edit, "note": f"mirror of {src[0][0]}:{src[0][1]}; {note}"})
        elif k in T:
            code, edit, note = T[k]
            out.append({**h, "code": code, "edit": edit, "note": note})
        else:
            errors.append(f"no disposition: {k}")
    for k in T:
        if k not in keys:
            errors.append(f"disposition without census hit: {k}")
    with open(D + "q1_dispositions.json", "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
        fh.write("\n")
    counts = {}
    for o in out:
        counts[o["code"]] = counts.get(o["code"], 0) + 1
    print("dispositions:", dict(sorted(counts.items())), "total", len(out), "of", len(hits))
    edits = {}
    for o in out:
        if o["edit"]:
            edits.setdefault(o["edit"], []).append(f"{o['file'].split('/')[-1]}:{o['line']}")
    for e in sorted(edits):
        print(f"  {e}: {', '.join(edits[e])}")
    if errors:
        print("ERRORS:")
        for e in errors:
            print("  ", e)
        sys.exit(1)
    print("COMPLETE")


if __name__ == "__main__":
    main()
