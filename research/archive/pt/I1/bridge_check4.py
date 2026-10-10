"""bridge_check4.py -- thread I1, stage 6: do the K-programme / pair modules state anything about
the passive-observation layer they import?

Run from pt/I1/ as:  python3 -I -B bridge_check4.py > bridge_check4.out 2> bridge_check4.err
Read-only on ../base/. Deterministic.

QUESTION. bridge_check3.py found that the import closure of the pair-cone modules contains the
passive-observation modules ObservabilityQuotient and PassiveQuotient, whose subject is the
observer structure (a deterministic permutation `φ` of a carrier with a visible labelling `vis`;
itinerary classes; the minimal passive carrier; hidden-sector enlargement). Is there a declaration
at level O or P whose statement mentions that layer's objects (a candidate H -> O/P bridge)?

DECISION RULE (fixed before the first run).
  LEVEL_OP = KInfFoundations and every module whose import closure contains KInfFoundations
             (the K programme and the pair modules built on it).
  H_TOK    = identifiers defined in the passive-observation layer: itiRelInf, itiRelK, itiSetoid,
             MinimalCarrier, quotPerm, quotVis, hiddenExt, ClassicalBranchDomain,
             CompatibilityDomainGlue, BranchDomainK, PassivelyMinimal, ObservationCongruence,
             ItinerarySeparating, itinerarySeparating, realizationMap, passiveQuotient.
  Report every declaration in LEVEL_OP whose signature (keyword .. first `:=` / trailing `where`)
  contains an H_TOK token; then report, per LEVEL_OP module, whether its SOURCE TEXT mentions any
  H_TOK token at all (proof bodies included). Verdict `NONE-FOUND` if no signature hit, else
  `FOUND n`. Countercontrol: the same signature search over PassiveQuotient.lean itself must find
  hits (the tokens are spelled as the layer spells them), else VOID.
"""
import os
import re
import sys

ROOT = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
H_TOK = ["itiRelInf", "itiRelK", "itiSetoid", "MinimalCarrier", "quotPerm", "quotVis", "hiddenExt",
         "ClassicalBranchDomain", "CompatibilityDomainGlue", "BranchDomainK", "PassivelyMinimal",
         "ObservationCongruence", "ItinerarySeparating", "itinerarySeparating", "realizationMap",
         "passiveQuotient"]
HEAD = re.compile(r"^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected|partial|unsafe)\s+)*"
                  r"(axiom|opaque|class|structure|def|abbrev|inductive|theorem|lemma|instance)\b\s*"
                  r"([^\s:({\[]*)")


def sig(lines, i):
    out = []
    for j in range(i, min(len(lines), i + 40)):
        ln = lines[j]
        if j > i and (ln.lstrip().startswith("|") or HEAD.match(ln) or ln.startswith("/--")):
            break
        if ":=" in ln:
            out.append(ln.split(":=")[0])
            break
        if re.search(r"\bwhere\s*$", ln.rstrip()):
            out.append(re.sub(r"\bwhere\s*$", "", ln.rstrip()))
            break
        out.append(ln.rstrip())
    return " ".join(x.strip() for x in out)


def toks(text):
    return [t for t in H_TOK if re.search(r"(?<![A-Za-z0-9_'])" + t + r"(?![A-Za-z0-9_'])", text)]


def decl_hits(lines):
    depth, hits = 0, []
    for i, ln in enumerate(lines):
        if depth == 0:
            m = HEAD.match(ln)
            if m:
                t = toks(sig(lines, i))
                if t:
                    hits.append((i + 1, m.group(1), m.group(2), t))
        depth = max(0, depth + ln.count("/-") - ln.count("-/"))
    return hits


def main():
    mods = sorted(f[:-5] for f in os.listdir(ROOT) if f.endswith(".lean"))
    src, direct = {}, {}
    for m in mods:
        with open(os.path.join(ROOT, m + ".lean"), encoding="utf-8") as fh:
            src[m] = fh.read()
        direct[m] = [x for x in re.findall(r"^import\s+OIBridge\.(\S+)", src[m], re.M) if x in mods]
    memo = {}

    def clo(m):
        if m not in memo:
            acc = set()
            for x in direct[m]:
                acc.add(x)
                acc |= clo(x)
            memo[m] = acc
        return memo[m]

    level = [m for m in mods if m == "KInfFoundations" or "KInfFoundations" in clo(m)]
    ctrl = len(decl_hits(src["PassiveQuotient"].split("\n")))
    print("control (signature hits inside PassiveQuotient.lean): %d" % ctrl)
    print("LEVEL_OP modules: %d" % len(level))
    n = 0
    for m in level:
        hits = decl_hits(src[m].split("\n"))
        anywhere = toks(src[m])
        print("  %s  signature-hits=%d  source-mentions=%s" % (m, len(hits), ",".join(anywhere) if anywhere else "-"))
        for (ln, kw, name, t) in hits:
            n += 1
            print("    %s.lean:%d %s %s %s" % (m, ln, kw, name, t))
    if ctrl == 0:
        print("VERDICT VOID")
    elif n == 0:
        print("VERDICT NONE-FOUND")
    else:
        print("VERDICT FOUND %d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
