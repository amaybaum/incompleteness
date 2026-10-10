"""kernel_census.py -- thread I1 (foundations), stage 6, kernel census (coverage control (a)).

Run from pt/I1/ as:  python3 -I -B kernel_census.py > kernel_census.out 2> kernel_census.err
Read-only on ../base/. Deterministic: sorted traversal, no clock, no randomness.

DECISION RULE (fixed before the first run; what is counted, not what is expected):
  Part A -- whole-module census over the I1 module set MODS_A below (paths under
    ../base/verification/lean-mathlib/OIBridge/). A declaration is a CENSUS ENTRY iff its
    head line (after optional attributes `@[...]` and modifiers noncomputable/private/
    protected/partial/unsafe) starts with one of
      axiom | opaque | class                      (any type), or
      structure | def | abbrev | inductive        whose signature ends in `Prop`
    (`: Prop` or `-> Prop`), the signature being the text from the keyword up to the first
    `:=`, a trailing `where`, or a line opening with `|`. `abbrev`/`inductive` are an I1
    extension of the protocol's grep pattern and are reported in their own count.
    Every theorem/lemma of the module is also listed (name, line) as material for the
    records; theorems are not census entries.
  Part A' -- the single declaration `OICore` in CompletedOI.lean (the rest of that module
    belongs to thread I4).
  Part B -- cross-tree core-token census: every declaration of any keyword (including
    theorem/lemma/instance) anywhere in OIBridge/*.lean whose SIGNATURE (not its proof)
    contains one of the tokens in TOKENS_B. These are the statements in which the sealed
    core, its realization, or the internal-observer predicate enters.
  Part C -- the non-Mathlib kernel ../base/verification/lean/*.lean: every axiom/opaque/class/
    structure head line, listed (scope decision recorded in CENSUS.md).
  Output: one line per entry, `file:line  keyword  name  [PROP]  | first signature line`,
  plus counts. Nothing is printed that depends on the environment except relative paths.
"""
import os
import re
import sys

ROOT = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
CORE_LEAN = os.path.join("..", "base", "verification", "lean")

MODS_A = [
    "OIRealization.lean",
    "IndependenceCensus.lean",
    "ManuscriptAxioms.lean",
    "RouteB.lean",
    "SubstratumInterfaceAudit.lean",
    "BackgroundIndependence.lean",
    "A6Instantiation.lean",
    "C3Necessity.lean",
    "CausalReadback.lean",
    "PhysicalC4Discharge.lean",
    "PhysicalC4StorageReadback.lean",
    "InternalObserver.lean",
]

TOKENS_B = [
    "OICore", "RealizesSealedOICore", "CoreC1C4", "SealedCoreIsFiniteOI",
    "DerivedOICore", "IsInternalObserver", "A1Realized", "A2Realized", "A1A2Realized",
]

MODS_RE = r"(?:(?:noncomputable|private|protected|partial|unsafe)\s+)*"
HEAD = re.compile(r"^(?:@\[[^\]]*\]\s*)*" + MODS_RE +
                  r"(axiom|opaque|class|structure|def|abbrev|inductive|theorem|lemma|instance)\b\s*([^\s:({\[]*)")


def signature(lines, i):
    """Text from line i up to the first ':=' / trailing 'where' / a line opening with '|'."""
    parts = []
    j = i
    while j < len(lines) and j < i + 40:
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
        j += 1
    return " ".join(p.strip() for p in parts).strip()


def is_prop(sig):
    return re.search(r"(?::|→|->)\s*Prop\s*$", sig) is not None


def scan(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    out = []
    depth = 0  # block-comment depth; declarations inside comments are skipped
    for i, ln in enumerate(lines):
        if depth == 0:
            m = HEAD.match(ln)
            if m:
                kw, name = m.group(1), m.group(2)
                sig = signature(lines, i)
                out.append((i + 1, kw, name, sig, ln.rstrip()))
        depth += ln.count("/-") - ln.count("-/")
        if depth < 0:
            depth = 0
    return out


def census_entry(kw, sig):
    if kw in ("axiom", "opaque", "class"):
        return True
    if kw in ("structure", "def", "abbrev", "inductive"):
        return is_prop(sig)
    return False


def main():
    total_census = 0
    total_ext = 0
    print("== PART A: whole-module census, I1 module set (%d modules)" % len(MODS_A))
    for mod in MODS_A:
        decls = scan(os.path.join(ROOT, mod))
        ents = [d for d in decls if census_entry(d[1], d[3])]
        thms = [d for d in decls if d[1] in ("theorem", "lemma")]
        print("-- %s : %d census entries, %d theorems/lemmas, %d declarations scanned"
              % (mod, len(ents), len(thms), len(decls)))
        for (ln, kw, name, sig, raw) in ents:
            tag = "EXT" if kw in ("abbrev", "inductive") else "CEN"
            if tag == "EXT":
                total_ext += 1
            else:
                total_census += 1
            print("  %s:%d  %s  %s  %s  | %s" % (mod, ln, tag, kw, name, sig[:150]))
        for (ln, kw, name, sig, raw) in thms:
            print("  %s:%d  THM  %s  %s" % (mod, ln, kw, name))
    print("PART A totals: census entries (axiom/opaque/class/structure:Prop/def:Prop) = %d; "
          "extension entries (abbrev/inductive :Prop) = %d" % (total_census, total_ext))
    print()
    print("== PART A': OICore in CompletedOI.lean")
    for (ln, kw, name, sig, raw) in scan(os.path.join(ROOT, "CompletedOI.lean")):
        if name == "OICore":
            print("  CompletedOI.lean:%d  CEN  %s  %s  | %s" % (ln, kw, name, sig[:150]))
    print()
    print("== PART B: cross-tree core-token census, tokens = %s" % ",".join(TOKENS_B))
    nb = 0
    files = sorted(f for f in os.listdir(ROOT) if f.endswith(".lean"))
    per = {}
    for f in files:
        for (ln, kw, name, sig, raw) in scan(os.path.join(ROOT, f)):
            toks = [t for t in TOKENS_B if re.search(r"\b" + t + r"\b", sig)]
            if toks:
                nb += 1
                per[f] = per.get(f, 0) + 1
                print("  %s:%d  %s  %s  [%s]" % (f, ln, kw, name, ",".join(toks)))
    print("PART B total: %d declarations in %d modules" % (nb, len(per)))
    for f in sorted(per):
        print("  per-module %s %d" % (f, per[f]))
    print()
    print("== PART C: non-Mathlib kernel verification/lean/*.lean, axiom/opaque/class/structure heads")
    nc = 0
    for f in sorted(x for x in os.listdir(CORE_LEAN) if x.endswith(".lean")):
        for (ln, kw, name, sig, raw) in scan(os.path.join(CORE_LEAN, f)):
            if kw in ("axiom", "opaque", "class", "structure"):
                nc += 1
                print("  lean/%s:%d  %s  %s" % (f, ln, kw, name))
    print("PART C total: %d" % nc)
    return 0


if __name__ == "__main__":
    sys.exit(main())
