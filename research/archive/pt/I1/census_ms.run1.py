"""census_ms.py -- thread I1, stage 6: manuscript census (coverage control (b)).

Run from pt/I1/ as:  python3 -I -B census_ms.py > census_ms.out 2> census_ms.err
Read-only on ../base/. Deterministic.

DECISION RULE (fixed before the first run).
SECTIONS (I1's assignment, with two declared extensions):
  M  papers/Main.md lines 24-659 (Sec. 1-3);
  T  papers/Methodology.md lines 239-286 (Sec. 6); extension: 160-163 (Sec. 4.6) and 216-238
     (Sec. 5.4-5.5), which state the axioms and the conditions;
  S  papers/Substratum.md lines 88-130 (structural assumptions A1-A6, Stage 1 with C1-C4) and
     204-219 (the A1-A6 remarks);
  E  papers/Explainer.md, whole file, only sentences that mention a condition or an axiom
     ("Explainer where it states a condition");
  B1 book/ch01-observation.md, whole chapter;
  BX every other book/*.md except the FULL file: only RESTATEMENT sentences (pattern RESTATE).
  FULL book/The-Incompleteness-of-Observation-FULL.md: mirror check of every B1/BX sentence
     (exact sentence match after whitespace normalization) and a list of FULL-only RESTATE
     sentences.
UNIT: a sentence = a piece of a nonblank line split at `(?<=[.!?])\s+(?=[A-Z*(\[$])`.
COUNTED: in M, T, S, B1 every sentence matching KEYS (axiom, condition, C1-C4, (i)-(v), H-,
  K-programme labels, A1-A6, theorem, lemma, principle, assumption, hypothesis, definition,
  corollary, proposition, posit, postulate, boxed); in E and BX the sentences matching RESTATE
  (E: also any C1-C4 or axiom mention).
MAPPING (first rule that fires; the rules are the table below, applied in order):
  1. line-anchored rules (LINE_RULES) for Main Sec. 1 and the condition theorems of Sec. 2-3,
     for ch01 Sec. 1.2-1.4, Methodology, Substratum;
  2. keyword rules: axioms -> I1.1/I1.2/I1.3; Definition of observation -> I1.6;
     partition-relativity -> I1.15; conditions -> I1.20 (C1), I1.21 (C2), I1.22 (C2-slow / the
     slow timescale), I1.23 (C3), I1.24 (C4), "C1-C4" -> all four; A1..A6 -> I1.63..I1.68,
     "A1-A6" -> I1.69; M1-T -> I1.36;
  3. section defaults: Main lines 111-659 and ch01 lines 87-296 -> OOS:I2 (finite-horizon
     equivalence, P-indivisibility, dilation, Bell, characterization theorem, structural limits);
     Substratum E1-E7 / Theorem 23 / H-Bell / M1-B -> OOS:I2 (physical layer); named physical
     hypotheses H-* -> OOS:I2 (physical layer); Methodology Sec. 6.3-6.4 -> I1.3;
  4. anything else -> UNMAPPED (reported; a non-zero count is an incomplete census).
Each output line: `<file>:<line>#<k>  <ids or OOS:reason or UNMAPPED>  [mirror=...]  | text[:150]`.
"""
import os
import re
import sys

BASE = os.path.join("..", "base")
SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z*(\[$])")
KEYS = re.compile(r"Axiom|axiom|Condition|condition|\bC[1-4]\b|\((?:i|ii|iii|iv|v)\)|\bH-[A-Za-z]|"
                  r"\bK(?:1|2|3|∞|ₙ)\b|\bA[1-6]\b|Theorem|theorem|Lemma|lemma|Principle|principle|"
                  r"Assumption|assumption|Hypothesis|hypothesis|Definition|Corollary|Proposition|"
                  r"posit|postulate|boxed")
RESTATE = re.compile(r"Axiom 1|Axiom 2|two-axiom|tokened differentiation|first axiom|second axiom|"
                     r"\*\*\(?C[1-4]\)?[ :*]|\(C[1-4]\)\s|Condition C[1-4]|"
                     r"\bC[1-4] \((?:[Nn]on|[Rr]ecord|[Mm]emory|[Ss]ufficient|[Hh]istory|[Ss]low|"
                     r"[Cc]oupling)")
CMENTION = re.compile(r"\bC[1-4]\b|Axiom|axiom|tokened")


def lines_of(rel):
    with open(os.path.join(BASE, rel), encoding="utf-8") as fh:
        return fh.read().split("\n")


def sentences(text):
    return [s.strip() for s in SPLIT.split(text) if s.strip()]


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


# line-anchored rules: (file tag, first line, last line, ids)
LINE_RULES = [
    ("M", 28, 30, ["OOS:I2 (finite-horizon equivalence; problem statement)"]),
    ("M", 34, 36, None), ("M", 38, 38, None), ("M", 40, 40, ["I1.4"]),
    ("M", 44, 44, ["I1.6"]), ("M", 46, 46, ["I1.7"]), ("M", 48, 48, ["I1.8"]),
    ("M", 50, 54, ["I1.9"]), ("M", 56, 56, ["I1.10", "I1.12"]), ("M", 58, 58, ["I1.12"]),
    ("M", 60, 60, ["I1.13"]), ("M", 62, 62, ["I1.10", "I1.11"]), ("M", 64, 64, ["I1.12"]),
    ("M", 66, 66, ["I1.14"]), ("M", 68, 68, ["I1.6"]), ("M", 72, 72, ["I1.19"]),
    ("M", 74, 74, ["I1.20"]), ("M", 76, 76, ["I1.21", "I1.22"]), ("M", 78, 78, ["I1.23"]),
    ("M", 80, 80, ["I1.24"]), ("M", 82, 82, ["I1.17"]), ("M", 86, 92, ["I1.15"]),
    ("M", 97, 99, ["I1.16"]), ("M", 137, 141, ["I1.27"]), ("M", 159, 165, ["I1.28"]),
    ("M", 167, 172, ["I1.29"]), ("M", 286, 286, ["I1.34"]), ("M", 433, 445, ["I1.30"]),
    ("M", 447, 456, ["I1.31"]), ("M", 484, 494, ["I1.32"]), ("M", 594, 594, ["I1.19"]),
    ("M", 602, 602, ["I1.25"]), ("M", 612, 614, ["I1.33"]),
    ("B1", 20, 22, None), ("B1", 24, 24, ["I1.4"]), ("B1", 26, 26, ["I1.6"]),
    ("B1", 28, 28, ["I1.7"]), ("B1", 30, 32, ["I1.8"]), ("B1", 34, 36, ["I1.9"]),
    ("B1", 38, 41, ["I1.10", "I1.12"]), ("B1", 53, 53, ["I1.20"]), ("B1", 55, 55, ["I1.22"]),
    ("B1", 57, 57, ["I1.23"]), ("B1", 59, 59, ["I1.24"]), ("B1", 61, 71, ["I1.26"]),
    ("B1", 79, 85, ["I1.15"]),
    ("T", 160, 163, ["I1.18"]), ("T", 249, 253, ["I1.3"]),
    ("S", 104, 104, ["I1.69"]), ("S", 122, 122, ["I1.36"]), ("S", 124, 128, ["I1.35"]),
    ("S", 204, 219, None),
]


def keyword_ids(t):
    ids = []
    a1 = re.search(r"Axiom 1|first axiom|[Tt]okened differentiation occurs", t)
    a2 = re.search(r"Axiom 2|second axiom|[Dd]ifferentiation recurs|recurrence of differentiation", t)
    if re.search(r"two-axiom|non-derivab|not derivable|no-go|cannot be squeezed", t) and (a1 or a2 or "two-axiom" in t):
        ids.append("I1.3")
    else:
        if a1:
            ids.append("I1.1")
        if a2:
            ids.append("I1.2")
    if not ids and re.search(r"[Tt]okened differentiation|evidential floor", t):
        ids.append("I1.1")
    if re.search(r"\*\*Definition\.\*\*.*observation", t):
        ids.append("I1.6")
    if re.search(r"[Pp]artition-relativity", t):
        ids.append("I1.15")
    if re.search(r"selection condition|observer-admitting", t):
        ids.append("I1.5")
    cs = []
    if re.search(r"C1[–-]C4|C1–C3|\(C1\)–\(C4\)|\(C1\)–\(C3\)", t):
        cs += ["I1.20", "I1.21", "I1.23", "I1.24"]
    if re.search(r"\bC1\b", t):
        cs.append("I1.20")
    if re.search(r"\bC2\b", t):
        cs.append("I1.21")
    if re.search(r"C2-slow|\\tau_S \\ll \\tau_B|τ_S ≪ τ_B|[Ss]low-bath|slow bath", t):
        cs.append("I1.22")
    if re.search(r"\bC3\b", t):
        cs.append("I1.23")
    if re.search(r"\bC4\b", t):
        cs.append("I1.24")
    for c in cs:
        if c not in ids:
            ids.append(c)
    if re.search(r"A1[–-]A6", t):
        ids.append("I1.69")
    for k in range(1, 7):
        if re.search(r"\(A%d\)|\bA%d\b" % (k, k), t) and "I1.%d" % (62 + k) not in ids:
            ids.append("I1.%d" % (62 + k))
    if "M1-T" in t and "I1.36" not in ids:
        ids.append("I1.36")
    return ids


def map_sentence(tag, ln, t):
    for (ft, a, b, ids) in LINE_RULES:
        if ft == tag and a <= ln <= b:
            if ids is not None:
                return ids
            kid = keyword_ids(t)
            if kid:
                return kid
            if tag == "M" and ln in (34, 36):
                return ["I1.5"]
            if tag == "M" and ln == 38:
                return ["I1.1", "I1.2"]
            if tag == "B1":
                return ["I1.1", "I1.2"]
            if tag == "S":
                return ["I1.69"]
    kid = keyword_ids(t)
    if kid:
        return kid
    if re.search(r"\bH-[A-Za-z]|\bE[1-7]\b|Theorem 23|Lemma 23|M1-B|Bell", t):
        return ["OOS:I2 (physical layer: named hypotheses H-*, empirical inputs E1-E7, Theorem 23, Bell)"]
    if tag == "M" and 101 <= ln <= 659:
        return ["OOS:I2 (Main Sec. 2-3: P-indivisibility, dilation, Bell, finite-horizon equivalence, characterization)"]
    if tag == "B1" and 87 <= ln <= 296:
        return ["OOS:I2 (ch01 Sec. 1.5-1.11: P-indivisibility, routes to QM, Bell, characterization, limits)"]
    if tag == "B1" and ln < 20:
        return ["OOS:I2 (ch01 Sec. 1.1: the theorem announced)"]
    if tag == "T" and 255 <= ln <= 286:
        if re.search(r"observer-selection|selection principle is a theorem", t):
            return ["OOS:I2 (structural observer-selection theorem, Main Sec. 4.6)"]
        return ["I1.3"]
    if tag == "T" and 216 <= ln <= 238:
        return ["I1.3"]
    return ["UNMAPPED"]


def main():
    full = lines_of("book/The-Incompleteness-of-Observation-FULL.md")
    full_sents = set()
    for ln in full:
        for s in sentences(ln):
            full_sents.add(norm(s))
    plan = [("M", "papers/Main.md", [(24, 659)], "keys"),
            ("T", "papers/Methodology.md", [(160, 163), (216, 238), (239, 286)], "keys"),
            ("S", "papers/Substratum.md", [(88, 130), (204, 219)], "keys"),
            ("E", "papers/Explainer.md", None, "explainer"),
            ("B1", "book/ch01-observation.md", None, "keys")]
    bx = sorted(f for f in os.listdir(os.path.join(BASE, "book"))
                if f.endswith(".md") and f not in ("ch01-observation.md",
                                                   "The-Incompleteness-of-Observation-FULL.md"))
    for f in bx:
        plan.append(("BX", "book/" + f, None, "restate"))
    counts, per_id, oos, unm = {}, {}, {}, []
    book_counted = set()
    total = 0
    for tag, rel, ranges, mode in plan:
        ls = lines_of(rel)
        rng = ranges or [(1, len(ls))]
        n_here = 0
        for (a, b) in rng:
            for ln in range(a, min(b, len(ls)) + 1):
                for k, s in enumerate(sentences(ls[ln - 1])):
                    if mode == "keys":
                        hit = KEYS.search(s)
                    elif mode == "explainer":
                        hit = RESTATE.search(s) or CMENTION.search(s)
                    else:
                        hit = RESTATE.search(s)
                    if not hit:
                        continue
                    ids = map_sentence(tag, ln, s)
                    mirror = ""
                    if tag in ("B1", "BX"):
                        book_counted.add(norm(s))
                        mirror = " [mirror=%s]" % ("FULL" if norm(s) in full_sents else "none")
                    print("%s:%d#%d  %s%s  | %s" % (rel, ln, k + 1, ",".join(ids), mirror, s[:150]))
                    n_here += 1
                    total += 1
                    for i in ids:
                        if i.startswith("OOS"):
                            oos[i] = oos.get(i, 0) + 1
                        elif i == "UNMAPPED":
                            unm.append("%s:%d#%d" % (rel, ln, k + 1))
                        else:
                            per_id[i] = per_id.get(i, 0) + 1
        counts[rel] = n_here
    print()
    print("== FULL-only restatement sentences (no identical sentence in the chapter files counted)")
    fo = 0
    for ln_i, ln in enumerate(full, 1):
        for s in sentences(ln):
            if RESTATE.search(s) and norm(s) not in book_counted:
                fo += 1
                print("FULL:%d  %s  | %s" % (ln_i, ",".join(map_sentence("BX", ln_i, s)), s[:150]))
    print()
    print("== COUNTS")
    for rel in sorted(counts):
        print("  sentences counted %-55s %d" % (rel, counts[rel]))
    print("  TOTAL sentences counted: %d; FULL-only restatements: %d" % (total, fo))
    for i in sorted(per_id, key=lambda x: (len(x), x)):
        print("  mapped %s %d" % (i, per_id[i]))
    for r in sorted(oos):
        print("  %s %d" % (r, oos[r]))
    print("  UNMAPPED %d %s" % (len(unm), " ".join(unm[:40])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
