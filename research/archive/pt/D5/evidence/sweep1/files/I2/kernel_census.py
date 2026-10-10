#!/usr/bin/env python3
"""I2 kernel census (stage 6, Q-EX-FULL, step 1, coverage control (a)).

DECISION RULE (fixed before the first run; the script decides nothing about any item's status):
1. The I2 section set is the fixed list SECTIONS below (manuscript sections and ROADMAP rows in I2's scope).
2. A kernel identifier is "cited" iff it appears in backticks inside an I2 section and is declared in
   pt/base/verification/lean-mathlib/OIBridge/*.lean (declaration keywords listed in DECL_RE), matched on the
   full name or on its last dot-component; a module is "named" iff the text `OIBridge/<M>.lean` or
   `<M>.lean` appears in an I2 section and the file exists.
3. The candidate module set is (modules declaring a cited identifier) U (named modules).
4. Each candidate module is assigned: I4 if listed in PROTOCOL-STAGE6 I4's module list (I4_LIST) or cited only
   from the operational-completion / OI-plus line ranges that the protocol gives to I4's kernel side
   (I4_RANGES); I1 if in I1_LIST; I3 if in I3_LIST; otherwise I2.
5. For every I2 module, every declaration of kind axiom / opaque / class (any type) and every structure / def /
   abbrev / inductive whose declared type is Prop is printed with module:line, kind, name, the protocol's literal
   pattern flag (P = matched by grep '^(axiom|opaque|structure|class|def) '), and the number of theorem/lemma
   signatures in the I2 module set that mention the name before ':=' (hypothesis-use count, a role indicator).
6. Output is deterministic (sorted); no time stamp; counts printed at the end. Exit 0 always unless I/O fails.
AMENDMENT before run 2 (run 1 kept as kernel_census.run1.*): run 1 resolved round labels and single letters
(`A`, `S`, `N`, `D3`, `G₁`, `a4`) to same-named Lean declarations, a harness error. From run 2 an identifier
is eligible for resolution only if it has length >= 5 and either contains an underscore or contains at least
two lowercase letters (Lean-name shape); labels of the form [A-Z]+[0-9]* are never eligible. The matched
identifiers are printed per module.
"""
import os, re, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "../base"
LEAN = os.path.join(ROOT, "verification", "lean-mathlib", "OIBridge")
PAP = os.path.join(ROOT, "papers")
RM = os.path.join(ROOT, "verification", "ROADMAP.md")

SECTIONS = [
    ("papers/Main.md", 14, 22), ("papers/Main.md", 82, 82), ("papers/Main.md", 95, 99),
    ("papers/Main.md", 101, 196), ("papers/Main.md", 200, 656), ("papers/Main.md", 660, 678),
    ("papers/Main.md", 696, 720), ("papers/Main.md", 722, 740), ("papers/Main.md", 744, 756),
    ("papers/GR.md", 164, 296), ("papers/GR.md", 709, 752),
    ("papers/SM.md", 10, 16), ("papers/SM.md", 40, 95), ("papers/SM.md", 96, 165),
    ("papers/SM.md", 216, 279), ("papers/SM.md", 535, 566), ("papers/SM.md", 1354, 1369),
    ("papers/SM.md", 1576, 1635),
    ("papers/Substratum.md", 12, 40), ("papers/Substratum.md", 42, 65), ("papers/Substratum.md", 70, 173),
    ("papers/Substratum.md", 186, 195),
    ("verification/ROADMAP.md", 63, 63), ("verification/ROADMAP.md", 67, 67), ("verification/ROADMAP.md", 70, 70),
    ("verification/ROADMAP.md", 75, 75), ("verification/ROADMAP.md", 77, 664),
    ("verification/ROADMAP.md", 936, 970), ("verification/ROADMAP.md", 1148, 1157),
]
# kernel side given to I4 by the protocol's scope sentence (operational-completion characterization, OI+,
# primitive-source, substratum-source, layer-flow, typed forms as manuscript statements)
I4_RANGES = [("papers/GR.md", 212, 276), ("papers/Main.md", 564, 568)]
I4_LIST = set("""GeneralCarrier CompletedOI CarrierGeneralOIPlus ImplementationLocality MinimalRepertoire
PositivePackage StructuralClosure SubstratumSource SubstratumInterface PhaseSource ReadWriteControl DerivedQ3
LiftAudit ExecSource LiftSource EmbeddedObservation ReferenceExtension SpectatorBridge MicroscopicReversibility
PositiveReachability TypedCompletion TypedPositive QuasilocalAlgebra QuasilocalCharacterization SecondOrderDrive
JordanClassification OperationalRigidity""".split())
I1_LIST = set("""OIRealization C1Necessity C2Necessity C3Necessity C4Necessity""".split())
I3_LIST = set("""KInfFoundations OrbitGeneration TransitiveBody K2Guard CompositeDimension EffectAvailability""".split())

DECL_RE = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|partial|unsafe|nonrec)\s+)*"
                     r"(theorem|lemma|def|abbrev|structure|class|instance|axiom|opaque|inductive)\s+([^\s(:{\[]+)")
LIT_RE = re.compile(r"^(axiom|opaque|structure|class|def) ")
TICK_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_'.₀-₉⁺]*)`")
MOD_RE = re.compile(r"(?:OIBridge/)?([A-Z][A-Za-z0-9]*)\.lean")


def read_lines(p):
    with open(p, encoding="utf-8") as f:
        return f.read().split("\n")


def section_text(spec):
    rel, a, b = spec
    ls = read_lines(os.path.join(ROOT, rel))
    return [(rel, i, ls[i - 1]) for i in range(a, min(b, len(ls)) + 1)]


def in_ranges(rel, ln, ranges):
    return any(rel == r and a <= ln <= b for (r, a, b) in ranges)


def main():
    mods = sorted(f[:-5] for f in os.listdir(LEAN) if f.endswith(".lean"))
    src = {m: read_lines(os.path.join(LEAN, m + ".lean")) for m in mods}
    decl_index = {}  # name -> set(modules)
    decls = {m: [] for m in mods}  # (line, kind, name)
    for m in mods:
        for i, line in enumerate(src[m], 1):
            mm = DECL_RE.match(line)
            if mm:
                kind, name = mm.group(1), mm.group(2)
                decls[m].append((i, kind, name))
                for key in {name, name.split(".")[-1]}:
                    decl_index.setdefault(key, set()).add(m)
    cited = {}   # module -> set of (rel, line) citing it
    idents = {}  # module -> set of matched identifiers
    unresolved = set()

    def eligible(t):
        if len(t) < 5 or re.match(r"^[A-Z]+[0-9₀-₉]*$", t):
            return False
        return "_" in t or len(re.findall(r"[a-z]", t)) >= 2

    for spec in SECTIONS:
        for rel, ln, text in section_text(spec):
            for t in TICK_RE.findall(text):
                if not eligible(t):
                    continue
                keys = [t, t.split(".")[-1]]
                hit = set()
                for k in keys:
                    hit |= decl_index.get(k, set())
                if hit:
                    for m in hit:
                        cited.setdefault(m, set()).add((rel, ln))
                        idents.setdefault(m, set()).add(t)
                elif re.match(r"^[a-z][A-Za-z0-9_']*_[A-Za-z0-9_']+$", t) or re.match(r"^[A-Z][a-z]+[A-Z]\w*$", t):
                    unresolved.add(t)
            for mname in MOD_RE.findall(text):
                if mname in src:
                    cited.setdefault(mname, set()).add((rel, ln))
                    idents.setdefault(mname, set()).add("<module " + mname + ".lean>")

    def owner(m):
        if m in I4_LIST:
            return "I4 (protocol module list)"
        if m in I1_LIST:
            return "I1 (C1-C4 / realization modules)"
        if m in I3_LIST:
            return "I3 (K programme modules)"
        if all(in_ranges(r, l, I4_RANGES) for (r, l) in cited[m]):
            return "I4 (cited only from the operational-completion/OI-plus ranges)"
        return "I2"

    print("# I2 kernel census — candidate module set")
    print("modules in OIBridge: %d" % len(mods))
    own = {m: owner(m) for m in sorted(cited)}
    for m in sorted(cited):
        sites = sorted(cited[m])
        print("MODULE %-34s owner=%s cited_at=%s" % (m, own[m], ";".join("%s:%d" % s for s in sites[:6])
              + (";+%d more" % (len(sites) - 6) if len(sites) > 6 else "")))
        print("  idents: " + " ".join(sorted(idents.get(m, set()))))
    print("unresolved backticked identifiers (no Lean declaration found): %d" % len(unresolved))
    for t in sorted(unresolved):
        print("UNRESOLVED %s" % t)
    mine = [m for m in sorted(cited) if own[m] == "I2"]
    # theorem signatures in the I2 module set, for the hypothesis-use count
    sigs = []
    for m in mine:
        ls = src[m]
        for (i, kind, name) in decls[m]:
            if kind in ("theorem", "lemma"):
                buf = []
                for j in range(i - 1, min(i + 40, len(ls))):
                    buf.append(ls[j])
                    if ":=" in ls[j] or re.search(r"\bwhere\b", ls[j]):
                        break
                sigs.append(" ".join(buf).split(":=")[0])
    print()
    print("# census of axiom / opaque / class / Prop-valued structure, def, abbrev, inductive in I2 modules")
    total = 0
    lit_total = 0
    kinds = {}
    for m in mine:
        ls = src[m]
        for (i, kind, name) in decls[m]:
            if kind in ("theorem", "lemma", "instance"):
                continue
            buf = []
            for j in range(i - 1, min(i + 40, len(ls))):
                buf.append(ls[j])
                if ":=" in ls[j] or re.search(r"\bwhere\b", ls[j]) or (j > i - 1 and ls[j].strip() == ""):
                    break
            head = " ".join(buf)
            head = re.split(r":=|\bwhere\b", head)[0].rstrip()
            is_prop = bool(re.search(r":\s*Prop\s*$", head))
            if kind in ("axiom", "opaque", "class") or (kind in ("structure", "def", "abbrev", "inductive") and is_prop):
                lit = "P" if LIT_RE.match(ls[i - 1]) else "-"
                short = name.split(".")[-1]
                uses = sum(1 for s in sigs if re.search(r"(?<![A-Za-z0-9_.])" + re.escape(short) + r"(?![A-Za-z0-9_'])", s))
                total += 1
                lit_total += lit == "P"
                kinds[kind] = kinds.get(kind, 0) + 1
                print("DECL %s:%d %s %s lit=%s prop=%s hyp_uses=%d" % (m, i, kind, name, lit, is_prop, uses))
    print()
    print("I2 modules: %d" % len(mine))
    print("census entries: %d (literal-pattern matches: %d)" % (total, lit_total))
    print("by kind: " + ", ".join("%s=%d" % (k, kinds[k]) for k in sorted(kinds)))
    print("out-of-scope modules: %d" % sum(1 for m in own if own[m] != "I2"))


if __name__ == "__main__":
    main()
