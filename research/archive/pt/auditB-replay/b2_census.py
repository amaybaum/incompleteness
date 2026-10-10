#!/usr/bin/env python3
"""
b2_census.py -- thread B (PAIR-ACT), research only: census of the landed declarations that can bear on the pair data.

Run:  python3 -I -B b2_census.py <pt-root>        (pt-root = the directory holding base/)

Purpose.  The INDEPENDENT label for hgate (RESULT section 0) needs countermodels that satisfy every certified
observer-native premise bearing on the pair data (K, N).  b2_sources S3 checks a 13-item checklist for M_max and
M_D13.  This script checks, by a scan of every landed Lean source at L, that the checklist was not a hand selection:
every landed declaration that can bear on the pair data is classified, and every one that mentions the pair carrier
is covered by a checklist item.  It is a text census: it certifies the classification relative to the scan rules
below, not the semantics of any declaration (the dispositions are written judgements, recorded here verbatim).

Decision rules (fixed before the first run; rules, not expected numbers):
  R0  The scanned set is every file base/verification/lean-mathlib/OIBridge/*.lean plus
      base/verification/lean-mathlib/OIBridge.lean, found by glob (no hand list of files).  The script prints the
      file count and the sha256 of the concatenation (sorted path, NUL, content, NUL per file).
  R1  A declaration is a line matching  ^(@[...])? (private|protected)? (noncomputable)? (def|structure|class|abbrev|
      inductive) NAME.  Its signature is the text from that line up to (not including) the first ':=' or ' where',
      within at most 15 lines and stopping at a blank line.
  R2  A declaration is SELECTED iff
        (a) its signature contains 'Prop' and matches CARRIER (the pair carrier and pair gates:
            'W 3', 'W d', 'W (', '≃ₗ[ℝ] W', 'Set (W', '→ₗ[ℝ] W'), in any module; or
        (b) it is declared in a module of IFACE (the interface modules that the checklist's sources live in) and its
            signature contains 'Prop' or it is a structure, class or inductive.
  R3  Every SELECTED declaration (module.name) has an entry in the frozen map COVER, and every COVER entry is SELECTED
      (no stale entries).  PASS iff both.
  R4  Every SELECTED declaration matched by R2(a) has a COVER kind 'item' or 'ingredient' (a checklist item covers it);
      none of them is excluded.  PASS iff so.
  R5  The pair-touching modules -- every scanned module whose text matches PAIR -- are exactly the keys of the frozen
      map MODS, each with a disposition.  PASS iff the two sets are equal.
  R6  Countercontrols, each must be DETECTED (the R3 or R5 comparison must fail on the planted input):
        (i)  a declaration 'def PlantedPairPremise (G : W 3 ≃ₗ[ℝ] W 3) : Prop := True' appended in memory to
             CompositeDimension's text is SELECTED by R2(a) and unclassified by R3;
        (ii) a planted module 'PlantedModule' whose text is 'theorem t : cnot = cnot := rfl' is reported by R5;
        (iii) a planted declaration 'def PlantedLocal (x : Fin 3 → ℝ) : Prop := True' in CompositeDimension is
             SELECTED by R2(b) (CompositeDimension is in IFACE) and unclassified by R3.
  VERDICT B2-CENSUS prints only if R0-R6 all pass.  No timing in stdout.
"""
import glob
import hashlib
import os
import re
import sys

PASS_COUNT = 0
FAILS = []


def check(cid, kind, ok, text, detail=""):
    global PASS_COUNT
    tag = "PASS" if ok else "FAIL"
    line = f"{tag} {cid}  [{kind}] {text}"
    if detail:
        line += " -- " + detail
    print(line)
    if ok:
        PASS_COUNT += 1
    else:
        FAILS.append(cid)


DECL = re.compile(r"^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(?:noncomputable\s+)?"
                  r"(def|structure|class|abbrev|inductive)\s+(\S+)")
CARRIER = re.compile(r"W 3|W d\b|W \(|≃ₗ\[ℝ\] W|Set \(W|→ₗ\[ℝ\] W")
PAIR = re.compile(r"\bW 3\b|\bW d\b|\bcnot\b|NativeGate|maxCone|CandidateCone|jointStates|prodState|\bactT\b|\bactC\b")

IFACE = {"CompositeInterface", "OrbitGeneration", "CompletionAction", "StageCompletion", "DenseOrbit", "EffectSpace",
         "K1Bridge", "K2Guard", "CompositeDimension", "RelcSelectBlock", "ParityNot", "KInfFoundations",
         "TransitiveBody", "SharpTests"}

SINGLE = ("single-copy", "reads one copy's body, effects or automorphisms only; M_Q, M_max and M_D13 share the copies "
          "(landed eball 3 with its landed families), so it takes the same value in all three and does not read (K, N)")
OPLAYER = ("operation layer", "a directed system / operation datum; no pair DirectedStages value exists at L "
           "(b2_sources S0.opd), so it asserts nothing of (K, N): checklist item 12")

# Frozen coverage map: "Module.Name" -> (kind, disposition).  kind in {item, ingredient, single-copy, operation layer,
# candidate source, derived, description}.
COVER = {
    "CompositeDimension.IsProduct": ("ingredient", "of Entangling and EntanglingOf (items 5, 6)"),
    "CompositeDimension.IsNot": ("item", "1"),
    "CompositeDimension.NativeGate": ("item", "2"),
    "CompositeDimension.Entangling": ("item", "5"),
    "CompositeDimension.BlockData": ("derived", "a consequence of NativeGate (blockData_of_nativeGate), not a premise"),
    "CompositeDimension.Lor": ("description", "the Lorentz cone of homogenized effect vectors; a description"),
    "RelcSelectBlock.CtrlGate": ("item", "3"),
    "ParityNot.GateRel": ("item", "4"),
    "K1Bridge.NativeGateOf": ("item", "6"),
    "K1Bridge.EntanglingOf": ("item", "6"),
    "K2Guard.CandidateCone": ("item", "8"),
    "CompositeInterface.BoundedAffine": SINGLE,
    "CompositeInterface.ProductData": ("item", "10 (the product data of the coordinate model)"),
    "CompositeInterface.PreComposite": ("item", "10"),
    "CompositeInterface.LocallyTomographic": ("item", "10 (the lt field of Composite)"),
    "CompositeInterface.Composite": ("item", "10"),
    "CompositeInterface.SharpReadout": ("description", "register readout data of a composite; no constraint on N"),
    "CompositeInterface.JointReversible": ("candidate source", "asserted of no pair gate at L (S0.jr); as a premise "
                                          "for the native gate it restates hgate (S4.jr): RESULT section 3"),
    "OrbitGeneration.SharpSeed": SINGLE,
    "OrbitGeneration.PreservesBody": ("candidate source", "generic body preservation; for one copy single-copy, for "
                                      "the pair it is JointReversible (above)"),
    "OrbitGeneration.SeedOrbitAvailable": SINGLE,
    "OrbitGeneration.BoundaryTransitive": SINGLE,
    "OrbitGeneration.CoversBoundaryFrom": SINGLE,
    "CompletionAction.OpDatum": OPLAYER,
    "CompletionAction.StateRespect": OPLAYER,
    "CompletionAction.AffineRespect": OPLAYER,
    "CompletionAction.CompletionChart": OPLAYER,
    "CompletionAction.Undoes": OPLAYER,
    "StageCompletion.StageMap": OPLAYER,
    "StageCompletion.StageMap.Consistent": OPLAYER,
    "StageCompletion.DirectedStages": OPLAYER,
    "StageCompletion.SCInf": OPLAYER,
    "StageCompletion.BinaryVisible": OPLAYER,
    "StageCompletion.FiniteRank": SINGLE,
    "KInfFoundations.FiniteStage": OPLAYER,
    "KInfFoundations.IsEffectOn": SINGLE,
    "KInfFoundations.IsProperOn": SINGLE,
    "KInfFoundations.IsBoundaryState": SINGLE,
    "KInfFoundations.SupportingEffectComplete": SINGLE,
    "KInfFoundations.SingletonFaces": SINGLE,
    "KInfFoundations.RelStrictConvex": SINGLE,
    "KInfFoundations.PerfectlyDistinguishable": SINGLE,
    "KInfFoundations.CentrallySymmetric": SINGLE,
    "KInfFoundations.ElementaryDrivability": SINGLE,
    "KInfFoundations.CopyNatural": ("item", "7 (copy naturality of the NOT; the identity identification)"),
    "KInfFoundations.ClassicallyExposed": SINGLE,
    "KInfFoundations.KInf1": SINGLE,
    "DenseOrbit.DenseBoundaryOrbit": SINGLE,
    "EffectSpace.EffectsOn": SINGLE,
    "EffectSpace.MixingClosed": SINGLE,
    "SharpTests.HasTwoSharpTests": SINGLE,
    "TransitiveBody.IsBodyGroup": SINGLE,
    "TransitiveBody.TransBody": SINGLE,
}

# Frozen map of the pair-touching modules (PAIR matches) with a disposition.
MODS = {
    "CompositeDimension": "DIM-1: IsNot, NativeGate, Entangling, cnot, maxCone, phiW (items 1, 2, 5)",
    "CompositeInterface": "COMP-1: the composite interface and the landed min/max composites (item 10)",
    "DenseOrbit": "EFF-1 / K1-BRIDGE-1 under a dense boundary orbit: the same cone maxCone (item 6)",
    "EffectSpace": "EFF-1: the available family's cone equals maxCone (item 6)",
    "K1Bridge": "NativeGateOf, EntanglingOf (item 6)",
    "K2Guard": "CandidateCone and the orientation theorem (items 8, 11)",
    "NativeGateBall": "theorems of the dimension selector's core; no premise on (K, N) beyond NativeGate",
    "OddChar": "odd dimensions d = 2k+1: theorems and witnesses at d >= 5; no premise at d = 3 beyond items 1, 2, 4",
    "OrbitGeneration": "PreservesBody (single-copy; JointReversible for the pair)",
    "ParityNot": "GateRel (item 4); gJ3, gJ5 are witnesses, not premises",
    "RelcSelectBlock": "CtrlGate (item 3)",
    "RelcSelectC5": "a d = 5 witness gate; no premise at d = 3",
    "RelcSelectParity": "theorems: parity counts from the control relation; no new premise",
    "RelcSelectSqueeze": "d = 5 witnesses for the positivity clauses; no premise at d = 3",
    "SharpTests": "a single-copy premise (two sharp tests) and a d = 1 witness",
    "OIBridge(root)": "the import list; it matches PAIR only through 'import OIBridge.NativeGateBall'",
}


def scan(texts):
    """texts: dict module -> text.  Returns list of (module, line, name, keyword, via_carrier)."""
    out = []
    for mod in sorted(texts):
        lines = texts[mod].split("\n")
        for i, l in enumerate(lines):
            m = DECL.match(l)
            if not m:
                continue
            kw, name = m.group(1), m.group(2)
            parts = []
            for j in range(i, min(i + 15, len(lines))):
                if j > i and lines[j].strip() == "":
                    break
                parts.append(lines[j])
            sig = " ".join(parts)
            cut = len(sig)
            for stop in (":=", " where"):
                k = sig.find(stop)
                if k != -1:
                    cut = min(cut, k)
            sig = sig[:cut]
            via_a = ("Prop" in sig) and bool(CARRIER.search(sig))
            via_b = (mod in IFACE) and (("Prop" in sig) or kw in ("structure", "class", "inductive"))
            if via_a or via_b:
                out.append((mod, i + 1, name, kw, via_a))
    return out


def r3(selected):
    names = {f"{m}.{n}" for (m, _, n, _, _) in selected}
    missing = sorted(names - set(COVER))
    stale = sorted(set(COVER) - names)
    return missing, stale


def pair_modules(texts):
    return sorted(m for m, t in texts.items() if PAIR.search(t))


def main():
    if len(sys.argv) != 2:
        print("usage: python3 -I -B b2_census.py <pt-root>")
        sys.exit(2)
    root = sys.argv[1]
    lm = os.path.join(root, "base", "verification", "lean-mathlib")
    paths = sorted(glob.glob(os.path.join(lm, "OIBridge", "*.lean"))) + [os.path.join(lm, "OIBridge.lean")]
    texts = {}
    h = hashlib.sha256()
    for p in paths:
        with open(p, encoding="utf-8") as f:
            t = f.read()
        rel = os.path.relpath(p, root)
        h.update(rel.encode() + b"\0" + t.encode("utf-8") + b"\0")
        mod = "OIBridge(root)" if p.endswith(os.path.join("lean-mathlib", "OIBridge.lean")) else \
            os.path.basename(p)[:-5]
        texts[mod] = t

    print("== R0  the scanned set")
    check("R0", "source", len(paths) == len(texts) and len(paths) > 1,
          "every landed OIBridge source at L, by glob, read",
          f"{len(paths)} files, sha256 of the concatenation {h.hexdigest()}")

    selected = scan(texts)
    print("\n== R1-R3  the selected declarations and their dispositions")
    for (m, ln, n, kw, via_a) in selected:
        key = f"{m}.{n}"
        kind, disp = COVER.get(key, ("UNCLASSIFIED", ""))
        route = "a" if via_a else "b"
        print(f"  {m}.lean:{ln}  {kw} {n}  [R2({route})]  {kind}: {disp}")
    missing, stale = r3(selected)
    check("R3", "source", not missing and not stale,
          "every selected declaration is classified in COVER and every COVER entry is selected",
          f"{len(selected)} selected; unclassified {missing}; stale {stale}")

    carrier_sel = [(m, n) for (m, _, n, _, a) in selected if a]
    bad = [f"{m}.{n}" for (m, n) in carrier_sel if COVER.get(f"{m}.{n}", ("", ""))[0] not in ("item", "ingredient")]
    check("R4", "source", not bad and len(carrier_sel) > 0,
          "every declaration over the pair carrier (R2(a)) is covered by a checklist item",
          f"{len(carrier_sel)} over the pair carrier: {sorted(f'{m}.{n}' for (m, n) in carrier_sel)}; not covered {bad}")

    pm = pair_modules(texts)
    print("\n== R5  the pair-touching modules")
    for m in pm:
        print(f"  {m}: {MODS.get(m, 'UNCLASSIFIED')}")
    check("R5", "source", set(pm) == set(MODS),
          "the modules whose text touches the pair carrier are exactly the classified list",
          f"{len(pm)} modules; unclassified {sorted(set(pm) - set(MODS))}; stale {sorted(set(MODS) - set(pm))}")

    print("\n== R6  countercontrols")
    t1 = dict(texts)
    t1["CompositeDimension"] = t1["CompositeDimension"] + \
        "\n\ndef PlantedPairPremise (G : W 3 ≃ₗ[ℝ] W 3) : Prop := True\n"
    s1 = scan(t1)
    m1, _ = r3(s1)
    hit1 = any(n == "PlantedPairPremise" and a for (_, _, n, _, a) in s1)
    check("R6.i", "countercontrol", hit1 and m1 == ["CompositeDimension.PlantedPairPremise"],
          "countercontrol: a planted Prop over the pair carrier is selected by R2(a) and reported unclassified by R3")
    t2 = dict(texts)
    t2["PlantedModule"] = "theorem t : cnot = cnot := rfl\n"
    p2 = pair_modules(t2)
    check("R6.ii", "countercontrol", sorted(set(p2) - set(MODS)) == ["PlantedModule"],
          "countercontrol: a planted module touching cnot is reported by R5")
    t3 = dict(texts)
    t3["CompositeDimension"] = t3["CompositeDimension"] + "\n\ndef PlantedLocal (x : Fin 3 → ℝ) : Prop := True\n"
    s3 = scan(t3)
    m3, _ = r3(s3)
    hit3 = any(n == "PlantedLocal" and not a for (_, _, n, _, a) in s3)
    check("R6.iii", "countercontrol", hit3 and m3 == ["CompositeDimension.PlantedLocal"],
          "countercontrol: a planted Prop in an interface module is selected by R2(b) and reported unclassified by R3")

    print()
    total = PASS_COUNT + len(FAILS)
    if FAILS:
        print(f"b2_census: NO VERDICT -- {len(FAILS)} of {total} checks failed: {', '.join(FAILS)}")
        sys.exit(1)
    kinds = {}
    for (m, _, n, _, _) in selected:
        k = COVER[f"{m}.{n}"][0]
        kinds[k] = kinds.get(k, 0) + 1
    print("dispositions: " + ", ".join(f"{k} {kinds[k]}" for k in sorted(kinds)))
    print("VERDICT B2-CENSUS: every landed declaration at L selected by R2 is classified; every Prop over the pair "
          "carrier is covered by a checklist item (b2_sources S3); the pair-touching modules are exactly the "
          "classified list -- a text census relative to rules R1-R2, not a semantic proof of completeness")
    print(f"b2_census: OK -- {total} checks")


if __name__ == "__main__":
    main()
