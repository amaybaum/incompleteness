"""I3 exact-quote extractor for the inventory's theorem and definition records.

DECISION RULE (fixed before the first run):
- For each (module, name) in WANT, find the column-0 declaration `(theorem|lemma|def|abbrev|structure|instance)`,
  optionally preceded by `noncomputable`/`private`/`protected` and attributes, whose name is exactly `name`.
- Print `module:line`, the docstring (the `/-- ... -/` block ending on the preceding line, attribute lines skipped)
  and the header: the declaration line and the following lines up to the first line that contains `:=` or ends in
  ` by`, ` where` (at most 30 lines); the text after `:=` on that line is cut.
- A name not found prints `NOT FOUND` (it is a control on the list, not an error).
- Design modules (pt/inputs/fourcopy/) are searched only for names listed with module prefix `D:`.
- Deterministic output, no timestamps.
"""
import os
import re
import sys

KB = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
DB = os.path.join("..", "inputs", "fourcopy")

WANT = [
    ("CompositeDimension", ["W", "hom", "prodState", "pairVal", "prodEffVal", "maxCone", "jointStates", "actT",
                            "actC", "corner", "IsNot", "NativeGate", "Entangling", "sgn", "pc", "pt", "cnot", "z3",
                            "nflip", "xplus", "phiW", "isNot_nflip", "cnot_frame", "cnot_relT", "cnot_relC",
                            "nativeGate_cnot", "entangling_cnot", "finrank_plus_eq_finrank_minus",
                            "not_even_of_nativeGate", "blockData_of_nativeGate", "dim_of_nativeGate",
                            "three_of_nativeGate", "not_entangling_one", "nativeGate_cnot1", "not_entangling_cnot1",
                            "no_gate_four", "dim1_core", "lor_ehom", "isEffectOn_affOf", "lor_toOp_of_maxCone"]),
    ("KInfFoundations", ["FiniteStage", "IsEffectOn", "ElementaryDrivability", "CopyNatural", "ball3", "rot3",
                         "cyc3", "ball3Drive", "ball3_drivable", "not_drivable_Icc", "KInf1", "SingletonFaces",
                         "SupportingEffectComplete", "RelStrictConvex", "kinf2_kernel_core"]),
    ("OrbitGeneration", ["SharpSeed", "PreservesBody", "SeedOrbitAvailable", "BoundaryTransitive",
                         "preservesBody_drive", "seedOrbit_ball3_eq", "fullAut3", "boundaryTransitive_fullAut3",
                         "not_boundaryTransitive_flow", "orbit_generation_core"]),
    ("OrbitNormalization", ["driveWords3", "boundaryTransitive_ball3Drive", "isEmpty_drivability_of_finite_orbits",
                            "boundaryTransitive_ball4", "flow_zero_of_add"]),
    ("TransitiveBody", ["IsBodyGroup", "TransBody", "eball", "eq_qBall_of_boundaryTransitive",
                        "exists_affine_image_eq_eball", "extreme_of_isBoundaryState_of_transitive"]),
    ("StageCompletion", ["DirectedStages", "SCInf", "BinaryVisible", "FiniteRank", "body", "body_isClosed",
                         "sharpSeed_completion", "exists_chart_of_finiteRank"]),
    ("CompletionAction", ["OpDatum", "AffineRespect", "StateRespect", "preservesBody_inducedEquiv"]),
    ("CompositionOrder", ["OrdInf", "finiteOrderOn_of_stagePreserving", "not_ordInf_of_finite_of_mulClosed",
                          "ord1_core"]),
    ("InvariantInnerProduct", ["invariant_inner_product", "centroid_fixed"]),
    ("CompositeInterface", ["ProductData", "PreComposite", "LocallyTomographic", "Composite", "JointReversible",
                            "condA_prodState", "not_locallyTomographic_paddedPre", "no_composite_over_paddedPre"]),
    ("EffectSpace", ["EffectsOn", "MixingClosed", "maxConeOf", "sharpFamily_subset_avail", "maxConeOf_avail_eq",
                     "fullEffects_subset_avail", "not_fullEffects_of_orbit"]),
    ("K1Bridge", ["NativeGateOf", "EntanglingOf", "dim_of_nativeGateOf", "three_of_nativeGateOf"]),
    ("SharpTests", ["HasTwoSharpTests", "hasTwoSharpTests_iff", "two_le_not_implied"]),
    ("K2Guard", ["CandidateCone", "reflY", "prodState_mem_maxCone", "no_candidateCone_cnot_reflY",
                 "three_of_nativeGate_of_two_le", "two_le_of_entangling", "three_of_nativeGateOf_of_two_le"]),
    ("DenseOrbit", ["DenseBoundaryOrbit", "denseBoundaryOrbit_of_boundaryTransitive", "maxConeOf_avail_eq_of_dense"]),
    ("NativeGateBall", ["parity", "p_le_one", "dim_of_bounds", "lorentz_of_effects", "nb1_kernel_core"]),
    ("ParityNot", ["GateRel", "not_even_of_gateRel", "piRotation_three", "not_gateRel_refl3", "not_posFwd_gJ3",
                   "not_posFwd_gJ5"]),
    ("OddChar", ["exists_frame_gateRel_iff_odd", "not_posFwd_gRev"]),
    ("RelcSelectParity", ["not_even_of_relC"]),
    ("RelcSelectBlock", ["CtrlGate", "ctrlGate_of_nativeGate", "dim_of_ctrlGate", "three_of_ctrlGate"]),
    ("RelcSelectSqueeze", ["gSq_sep", "gSqInv_sep"]),
    ("RelcSelectC5", ["relT_not_dimension_selecting"]),
    ("D:FourCopyDefs", ["ipW", "dualW", "PairAdm", "FourCopyCoherent"]),
    ("D:FourCopyCore", ["NClass", "IE1", "KT4Core", "TokenCoherent", "EvenCycle"]),
    ("D:FourCopyPackage", ["Q3", "twin", "IE1Drive", "ie1Drive_of_ie1"]),
    ("D:FourCopyHeadline", ["kt4_forward_ie1"]),
    ("D:FourCopyBridge", ["fourCopyCoherent_of_kt4Core"]),
]

DECL = r"^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected)\s+)*(?:theorem|lemma|def|abbrev|structure|instance)\s+{}(?=[\s:({{\[]|$)"


def doc_of(lines, i):
    j = i - 1
    while j >= 0 and lines[j].strip().startswith("@["):
        j -= 1
    if j < 0 or not lines[j].rstrip().endswith("-/"):
        return None
    end = j
    while j >= 0 and "/--" not in lines[j]:
        j -= 1
    if j < 0:
        return None
    return (j + 1, [l.rstrip("\n") for l in lines[j:end + 1]])


def main():
    found = missing = 0
    for mod, names in WANT:
        if mod.startswith("D:"):
            path, tag = os.path.join(DB, mod[2:] + ".lean"), "D"
        else:
            path, tag = os.path.join(KB, mod + ".lean"), "K"
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        base = os.path.basename(path)
        for name in names:
            rx = re.compile(DECL.format(re.escape(name)))
            hit = [i for i, l in enumerate(lines) if rx.match(l)]
            if not hit:
                missing += 1
                print(f"### [{tag}] {base} {name}: NOT FOUND")
                print()
                continue
            found += 1
            i = hit[0]
            print(f"### [{tag}] {base}:{i + 1} {name}" + (f" (also at {[h + 1 for h in hit[1:]]})" if len(hit) > 1 else ""))
            d = doc_of(lines, i)
            if d:
                print(f"doc {base}:{d[0]}-{d[0] + len(d[1]) - 1}:")
                for x in d[1]:
                    print("  | " + x)
            for j in range(i, min(i + 30, len(lines))):
                s = lines[j].rstrip("\n")
                if ":=" in s:
                    print("  > " + s[: s.index(":=") + 2])
                    break
                print("  > " + s)
                if s.rstrip().endswith(" by") or s.rstrip().endswith(" where"):
                    break
            print()
    print(f"found = {found}, not found = {missing}")
    print("END")


if __name__ == "__main__":
    sys.exit(main())
