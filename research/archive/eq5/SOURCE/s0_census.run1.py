"""EQ4-SOURCE s0 — exact census of the certified base for multi-copy carriers and composite structure (Q1, Q2).

Usage:  python3 -I -B s0_census.py <base>/verification/lean-mathlib/OIBridge <eq5>/inputs
Read-only text processing of the base Lean sources; no Lean toolchain is used or claimed.

DECISION RULE (fixed before the first run; rules, not expected numbers):
  C  controls (all must pass, otherwise no verdict):
     C1 every OIBridge module file parses at least one import line or is a leaf with Mathlib-only imports; the
        aggregator OIBridge.lean is excluded from path checks;
     C2 the import-path finder finds the known landed paths K2Guard ->* CompositeInterface and
        RegionTower ->* TypedCompletion (positive controls), and finds no path CompositeInterface ->* K2Guard
        (an importer is not reachable from its import: countercontrol);
     C3 the carrier scanner (real-valued function types with >= 3 chained `Fin _ ->` binders before `ℝ`) finds the
        four-copy carrier W4 in the preflight input FourCopyPackage.lean (positive control), does not count the
        two-copy carriers `W d` (CompositeDimension) and `Model.Carrier` (CompositeInterface), and does not count the
        index map `pc : Fin 4 -> Fin 4 -> Fin 4` (no ℝ codomain) (countercontrols);
     C4 the identifier scanner finds `PreComposite` in CompositeInterface.lean and `TokenCoherent` in the preflight
        input (positive controls).
  Q  census questions (each reported PASS when the stated condition holds on the base, FAIL otherwise):
     Q1a no import path, in either direction, between any module of the field-neutral composite core
         {CompositeInterface, CompositeDimension, K2Guard, K1Bridge, EffectSpace, RelcSelectBlock, NativeGateBall,
          TransitiveBody, KInfFoundations, StageCompletion, CompletionAction} and any module of the complex region /
         operational core {RegionTower, RegionLimit, QuasilocalAlgebra, TypedCompletion, OperationalAssembly,
          MonoidalCompletion};
     Q1b the COMP-1 structure names (`PreComposite`, `ProductData`, `LocallyTomographic`, `SharpReadout`) occur in no
         base module other than CompositeInterface.lean;
     Q1c no module of the field-neutral side (the core above together with every module that imports, directly or
         transitively, CompositeInterface or CompositeDimension) contains a real-valued carrier type with >= 3
         chained `Fin _ ->` binders; hits in other modules are listed as notes and not judged;
     Q1d every `def` of CompositeInterface whose declared type (the text between the declaration name and the first
         `:=` or ` where`) ends in `Composite A B C` or `PreComposite A B C` has factor-body arguments A, B of
         one-copy type (`ball3`, `(simplex 2)`, or the generic parameters `ΩA`, `ΩB`), i.e. no value takes a
         composite body as a factor; at least four such values exist (listed);
     Q1e none of the stage-product / joint-tower / local-extension names (`FiniteStage.prod`, `DirectedStages.prod`,
         `stageProd`, `LocalExt`, `JointTower`, `jointTower`) and none of the package names (`TokenCoherent`,
         `FourCopyCoherent`, `NClass`, `ctrlGate_classification`, `PairAdm`) occurs in the base;
     Q2a every `DirectedStages` value defined in the base is listed (record only; reported, not judged);
     Q2b the region tower's observable and state types are complex-matrix types (`Matrix (Conf ..) (Conf ..) ℂ` in
         the signatures of `inclObs` and `restrict`).
VERDICT S0-CENSUS-NO-MULTICOPY-STRUCTURE iff every C check and every Q check passes; otherwise VERDICT NOT RENDERED.
Deterministic output (sorted listings); no timing in stdout.
"""
import os
import re
import sys

BASE = sys.argv[1]
INPUTS = sys.argv[2]
CHECKS = []


def check(name, cond, detail=None):
    ok = bool(cond)
    CHECKS.append((name, ok))
    line = ("PASS " if ok else "FAIL ") + name
    if detail is not None:
        line += "  [" + str(detail) + "]"
    print(line)
    sys.stdout.flush()
    return ok


def note(text):
    print("NOTE " + text)
    sys.stdout.flush()


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


# ---------------------------------------------------------------- module graph
files = sorted(f for f in os.listdir(BASE) if f.endswith(".lean"))
mods = [f[:-5] for f in files]
text = {m: read(os.path.join(BASE, m + ".lean")) for m in mods}
imports = {}
for m in mods:
    imps = re.findall(r"^import\s+(\S+)", text[m], flags=re.M)
    imports[m] = sorted(set(i[len("OIBridge."):] for i in imps if i.startswith("OIBridge.")))
root_text = read(os.path.join(os.path.dirname(BASE), "OIBridge.lean"))
root_imports = re.findall(r"^import\s+OIBridge\.(\S+)", root_text, flags=re.M)
note("modules in OIBridge/: %d; aggregator OIBridge.lean imports %d of them" % (len(mods), len(root_imports)))

parse_ok = all(re.search(r"^import\s+\S+", text[m], flags=re.M) for m in mods)
check("C1 every module file has at least one import line (Mathlib or OIBridge); aggregator excluded from paths",
      parse_ok)


def reach(src):
    seen, stack = set(), [src]
    while stack:
        cur = stack.pop()
        for nxt in imports.get(cur, []):
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


R = {m: reach(m) for m in mods}
check("C2 positive controls: K2Guard ->* CompositeInterface and RegionTower ->* TypedCompletion; countercontrol: "
      "no path CompositeInterface ->* K2Guard",
      "CompositeInterface" in R["K2Guard"] and "TypedCompletion" in R["RegionTower"]
      and "K2Guard" not in R["CompositeInterface"])

BALL = ["CompositeInterface", "CompositeDimension", "K2Guard", "K1Bridge", "EffectSpace", "RelcSelectBlock",
        "NativeGateBall", "TransitiveBody", "KInfFoundations", "StageCompletion", "CompletionAction"]
CX = ["RegionTower", "RegionLimit", "QuasilocalAlgebra", "TypedCompletion", "OperationalAssembly",
      "MonoidalCompletion"]
missing = [m for m in BALL + CX if m not in mods]
paths = []
for b in BALL:
    for c in CX:
        if c in R[b]:
            paths.append(b + "->" + c)
        if b in R[c]:
            paths.append(c + "->" + b)
common = sorted(m for m in mods if any(b in R[m] or b == m for b in BALL) and any(c in R[m] or c == m for c in CX))
note("modules (other than the aggregator) reaching both a ball-core and a complex-core module: "
     + (", ".join(common) if common else "none"))
check("Q1a no import path in either direction between the field-neutral composite core and the complex region core",
      not missing and not paths, "missing=%s paths=%s" % (missing, paths))

# ---------------------------------------------------------------- COMP-1 names
names = ["PreComposite", "ProductData", "LocallyTomographic", "SharpReadout"]
users = sorted(m for m in mods if any(re.search(r"\b" + n + r"\b", text[m]) for n in names))
check("C4a identifier scanner finds PreComposite in CompositeInterface.lean (positive control)",
      re.search(r"\bPreComposite\b", text["CompositeInterface"]))
pkg = read(os.path.join(INPUTS, "FourCopyPackage.lean"))
check("C4b identifier scanner finds TokenCoherent in the preflight input FourCopyPackage.lean (positive control)",
      re.search(r"\bTokenCoherent\b", pkg))
check("Q1b the COMP-1 structure names occur only in CompositeInterface.lean", users == ["CompositeInterface"],
      "users=%s" % users)

# ---------------------------------------------------------------- carriers with >= 3 copies
CARRIER = re.compile(r"(?:Fin\s*(?:\([^()]*\)|[\w']+)\s*→\s*){3,}ℝ")
TWO = re.compile(r"(?:Fin\s*(?:\([^()]*\)|[\w']+)\s*→\s*){2}ℝ")
w4_hits = CARRIER.findall(pkg)
cd_two = TWO.findall(text["CompositeDimension"])
ci_two = TWO.findall(text["CompositeInterface"])
cd_three = CARRIER.findall(text["CompositeDimension"])
ci_three = CARRIER.findall(text["CompositeInterface"])
pc_line = re.search(r"def pc : Fin 4 → Fin 4 → Fin 4", text["CompositeDimension"])
check("C3 carrier scanner: finds W4 in FourCopyPackage.lean; counts no >=3-copy carrier in CompositeDimension or "
      "CompositeInterface although both contain two-copy carriers; does not count `pc : Fin 4 -> Fin 4 -> Fin 4`",
      len(w4_hits) >= 1 and len(cd_two) >= 1 and len(ci_two) >= 1 and not cd_three and not ci_three
      and pc_line is not None,
      "W4 hits=%d, two-copy hits CD=%d CI=%d" % (len(w4_hits), len(cd_two), len(ci_two)))
FN = set(BALL) | {m for m in mods if "CompositeInterface" in R[m] or "CompositeDimension" in R[m]}
three_fn = sorted((m, h) for m in sorted(FN) for h in CARRIER.findall(text[m]))
three_other = sorted((m, h) for m in mods if m not in FN for h in CARRIER.findall(text[m]))
note("field-neutral side scanned for Q1c: %d modules" % len(FN))
note("three-binder real-valued types outside the field-neutral side (not judged): "
     + (", ".join("%s: %s" % x for x in three_other) if three_other else "none"))
check("Q1c no field-neutral module contains a real-valued carrier with >= 3 chained Fin binders", not three_fn,
      "hits=%s" % three_fn[:5])

# ---------------------------------------------------------------- values of the COMP-1 structures
ci = text["CompositeInterface"]
lines = ci.split("\n")
decl_start = re.compile(r"^(?:noncomputable\s+)?(?:def|theorem|structure|abbrev|instance|lemma)\s")
chunks = []
cur = None
for ln in lines:
    if decl_start.match(ln):
        if cur is not None:
            chunks.append(cur)
        cur = [ln]
    elif cur is not None:
        cur.append(ln)
if cur is not None:
    chunks.append(cur)


def split_args(s, k):
    """The first k arguments of a type application: parenthesised groups or single tokens."""
    out, i = [], 0
    while len(out) < k and i < len(s):
        while i < len(s) and s[i] == " ":
            i += 1
        if i >= len(s):
            break
        if s[i] == "(":
            depth, j = 0, i
            while j < len(s):
                if s[j] == "(":
                    depth += 1
                elif s[j] == ")":
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            out.append(s[i:j + 1])
            i = j + 1
        else:
            j = i
            while j < len(s) and s[j] != " ":
                j += 1
            out.append(s[i:j])
            i = j
    return out


ONE_COPY = {"ball3", "(simplex 2)", "ΩA", "ΩB"}
values = []
factors_ok = True
for ch in chunks:
    head = " ".join(x.strip() for x in ch)
    m = re.match(r"(?:noncomputable\s+)?def\s+([\w.']+)\s*(.*)", head)
    if not m:
        continue
    nm, rest = m.group(1), m.group(2)
    cut = len(rest)
    for tok in [":=", " where"]:
        k = rest.find(tok)
        if k != -1:
            cut = min(cut, k)
    sig = rest[:cut]
    mm = re.search(r":\s*(PreComposite|Composite)\s+(.*)$", sig)
    if not mm:
        continue
    args = split_args(mm.group(2).strip(), 3)
    ok = len(args) == 3 and args[0] in ONE_COPY and args[1] in ONE_COPY
    values.append((nm, mm.group(1), tuple(args)))
    if not ok:
        factors_ok = False
for nm, kind, args in sorted(values):
    note("COMP-1 value: %s : %s %s" % (nm, kind, " ".join(args)))
check("Q1d every Composite/PreComposite value of CompositeInterface has one-copy factor bodies "
      "(ball3, simplex 2, or generic ΩA ΩB), and at least four such values exist", factors_ok and len(values) >= 4,
      "values=%d" % len(values))

# ---------------------------------------------------------------- stage products, package names
absent = ["FiniteStage.prod", "DirectedStages.prod", "stageProd", "LocalExt", "JointTower", "jointTower",
          "TokenCoherent", "FourCopyCoherent", "NClass", "ctrlGate_classification", "PairAdm"]
found = sorted((n, m) for n in absent for m in mods if re.search(r"(?<![\w.])" + re.escape(n) + r"(?![\w'])",
                                                                  text[m]))
check("Q1e no stage-product, joint-tower, local-extension or four-copy package name occurs in the base", not found,
      "found=%s" % found)

# ---------------------------------------------------------------- protocol towers
ds = sorted((m, nm) for m in mods for nm in re.findall(r"^(?:noncomputable\s+)?def\s+([\w.']+)\s*:\s*"
                                                         r"(?:[\w.]+\.)?DirectedStages\b", text[m], flags=re.M))
note("DirectedStages values defined in the base: " + (", ".join("%s.%s" % x for x in ds) if ds else "none"))
check("Q2a DirectedStages values listed (record only)", True, "count=%d" % len(ds))
rt = text["RegionTower"]
incl = re.search(r"def inclObs[^\n]*\n?[^\n]*Matrix \(Conf Λ Q\) \(Conf Λ Q\) ℂ", rt)
restr = re.search(r"def restrict[^\n]*\n?[^\n]*Matrix \(Conf Λ' Q\) \(Conf Λ' Q\) ℂ", rt)
check("Q2b the region tower's inclObs and restrict act on complex matrices over configurations",
      incl is not None and restr is not None)

nfail = sum(1 for _, ok in CHECKS if not ok)
print("--- s0_census: %d/%d checks pass" % (len(CHECKS) - nfail, len(CHECKS)))
ctrl_ok = all(ok for nm, ok in CHECKS if nm.startswith("C"))
if nfail == 0 and ctrl_ok:
    print("VERDICT S0-CENSUS-NO-MULTICOPY-STRUCTURE")
else:
    print("VERDICT NOT RENDERED")
