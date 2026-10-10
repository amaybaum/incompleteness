"""bridge_check.py -- thread I1, stage 6: mechanical search for bridge declarations at L.

Run from pt/I1/ as:  python3 -I -B bridge_check.py > bridge_check.out 2> bridge_check.err
Read-only on ../base/. Deterministic (sorted traversal; no clock; no randomness).

QUESTION. Is there, at L, a kernel declaration whose statement connects an I1 object (the sealed
core, C1-C4, the axiom images, the substratum interface, the C3/C4 forms, the internal observer)
to the pair-cone level P (`W 3`, `maxCone`, `prodState`, `cnot`, ...) or to the single-system
operational level O of the K programme (K-infinity: `Stage`, `ElementaryDrivability`, ...)?

DECISION RULE (fixed before the first run).
  1. Build the OIBridge import graph from the `import OIBridge.X` lines; close it transitively.
  2. CORE = the I1 modules (list below). PAIR = {CompositeDimension, K2Guard}.
     OPER = {KInfFoundations, OrbitGeneration, TransitiveBody, StageCompletion}.
  3. Report every module that imports (transitively, or is) a CORE module AND a PAIR module;
     likewise CORE and OPER. If a list is empty, no declaration at L can mention both, and the
     verdict line for that level is `NO-MODULE`.
  4. For every module in a non-empty list, report every declaration (any keyword) whose
     signature (keyword .. first `:=` / trailing `where`) contains a CORE token AND a PAIR
     (resp. OPER) token. Verdict per level: `NONE-FOUND` if no such declaration, else `FOUND n`.
  5. Countercontrol (must succeed, else the run is void): the same signature search with
     CORE tokens replaced by the PAIR tokens themselves must find declarations in
     CompositeDimension.lean (the search can see pair statements), and the import closure of
     OIRealization must contain IndependenceCensus (the graph closure works).
  The verdict lines print only if both controls are green.
"""
import os
import re
import sys

ROOT = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
CORE = ["OIRealization", "IndependenceCensus", "ManuscriptAxioms", "RouteB",
        "SubstratumInterfaceAudit", "BackgroundIndependence", "A6Instantiation", "C3Necessity",
        "CausalReadback", "PhysicalC4Discharge", "PhysicalC4StorageReadback", "InternalObserver"]
PAIR = ["CompositeDimension", "K2Guard"]
OPER = ["KInfFoundations", "OrbitGeneration", "TransitiveBody", "StageCompletion"]
CORE_TOK = ["OICore", "RealizesSealedOICore", "CoreC1C4", "SealedCoreIsFiniteOI", "DerivedOICore",
            "DerivedOI", "A1Realized", "A2Realized", "Substratum", "obsTheory", "C4e", "C4r",
            "RoutedReadback", "RoutedReadbackAtStorage", "IsInternalObserver", "c3_necessity",
            "Realization", "RootedRealization", "A6Cov", "A6Inv", "Core"]
PAIR_TOK = ["maxCone", "prodState", "cnot", "dualW", "pauliW", "ipW", "eball", "NativeGate",
            "IsNot", "Entangling", "actC", "actT", "W 3", "W d"]
OPER_TOK = ["ElementaryDrivability", "BoundaryTransitive", "DirectedStages", "StageCompletion",
            "cyc3", "CopyNatural", "OpDatum", "Drive", "Stage"]

HEAD = re.compile(r"^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected|partial|unsafe)\s+)*"
                  r"(axiom|opaque|class|structure|def|abbrev|inductive|theorem|lemma|instance)\b\s*"
                  r"([^\s:({\[]*)")


def read(mod):
    with open(os.path.join(ROOT, mod + ".lean"), encoding="utf-8") as fh:
        return fh.read().split("\n")


def imports(lines):
    out = []
    for ln in lines:
        m = re.match(r"^import\s+OIBridge\.(\S+)", ln)
        if m:
            out.append(m.group(1))
    return out


def signature(lines, i):
    parts = []
    for j in range(i, min(len(lines), i + 40)):
        ln = lines[j]
        if j > i and (ln.lstrip().startswith("|") or HEAD.match(ln) or ln.startswith("/--")):
            break
        if ":=" in ln:
            parts.append(ln.split(":=")[0])
            break
        s = ln.rstrip()
        if re.search(r"\bwhere\s*$", s):
            parts.append(re.sub(r"\bwhere\s*$", "", s))
            break
        parts.append(s)
    return " ".join(p.strip() for p in parts)


def decls(lines):
    depth = 0
    for i, ln in enumerate(lines):
        if depth == 0:
            m = HEAD.match(ln)
            if m:
                yield i + 1, m.group(1), m.group(2), signature(lines, i)
        depth = max(0, depth + ln.count("/-") - ln.count("-/"))


def has(sig, toks):
    return [t for t in toks if re.search(r"(?<![A-Za-z0-9_'])" + re.escape(t) + r"(?![A-Za-z0-9_'])", sig)]


def main():
    mods = sorted(f[:-5] for f in os.listdir(ROOT) if f.endswith(".lean"))
    src = {m: read(m) for m in mods}
    direct = {m: [x for x in imports(src[m]) if x in src] for m in mods}
    closure = {}

    def clo(m, seen=None):
        if m in closure:
            return closure[m]
        acc = set()
        for x in direct[m]:
            acc.add(x)
            acc |= clo(x)
        closure[m] = acc
        return acc

    for m in mods:
        clo(m)
    print("modules: %d" % len(mods))
    ctrl_graph = "IndependenceCensus" in closure["OIRealization"]
    ctrl_search = sum(1 for (_, _, _, s) in decls(src["CompositeDimension"]) if has(s, PAIR_TOK))
    print("control graph (IndependenceCensus in closure(OIRealization)): %s" % ctrl_graph)
    print("control search (CompositeDimension declarations with a PAIR token): %d" % ctrl_search)
    green = ctrl_graph and ctrl_search > 0
    for label, LEV, TOK in (("PAIR (level P)", PAIR, PAIR_TOK), ("OPER (level O)", OPER, OPER_TOK)):
        both = [m for m in mods
                if (m in CORE or closure[m] & set(CORE)) and (m in LEV or closure[m] & set(LEV))]
        print()
        print("== %s: modules importing (or being) a CORE module and a %s module: %d"
              % (label, label.split()[0], len(both)))
        found = 0
        for m in both:
            print("  module %s  (core via: %s; level via: %s)" % (
                m, ",".join(sorted((closure[m] | {m}) & set(CORE))),
                ",".join(sorted((closure[m] | {m}) & set(LEV)))))
            for (ln, kw, name, sig) in decls(src[m]):
                c, p = has(sig, CORE_TOK), has(sig, TOK)
                if c and p:
                    found += 1
                    print("    %s.lean:%d %s %s  core=%s level=%s" % (m, ln, kw, name, c, p))
        if not green:
            print("VERDICT %s: VOID (control failed)" % label)
        elif not both:
            print("VERDICT %s: NO-MODULE" % label)
        elif found == 0:
            print("VERDICT %s: NONE-FOUND" % label)
        else:
            print("VERDICT %s: FOUND %d" % (label, found))
    print()
    print("== reverse direction: modules importing a PAIR module, listed with their CORE imports")
    for m in mods:
        if m in PAIR or closure[m] & set(PAIR):
            cs = sorted((closure[m] | {m}) & set(CORE))
            print("  %s  core-imports=%s" % (m, ",".join(cs) if cs else "-"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
