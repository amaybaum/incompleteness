"""qe2_graph -- QE2: locate every route declaration at the base (read-only), print its header (hypotheses) and the
modules that mention it, so the dependency graph and its seams are replayable.  Reads only scratchpad/eq/base."""
import os, re, sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "base", "verification", "lean-mathlib", "OIBridge")
NAMES = """
oiPlus_iff_qm qm_of_oiPlus oiPlus_of_qm OIPlus carrier_general_oiPlus
typed_determined_iff ShadowQuantum TypedOperationalTheory IsTypedKrausInstrument
genTheory_qm_of_quantumArchitecture QuantumArchitecture DrivesElementary fullClass_quantumArchitecture
qm_generated_by_quantumArchitecture quantumArchitecture_supplies_all qm_of_oiPlusElem
control_of_lieRank LieRankRichness lieRank_of_elementary fullInstruments_of_control finiteIsometryExtensionSF_discharged
W IsNot NativeGate Entangling maxCone jointStates dim_of_nativeGate three_of_nativeGate isNot_nflip nativeGate_cnot entangling_cnot
CtrlGate dim_of_ctrlGate three_of_ctrlGate GateRel piRotation_three
EffectsOn maxConeOf maxConeOf_avail_eq sharpFamily_subset_avail seedOrbit_eq_sharpFamily
NativeGateOf EntanglingOf dim_of_nativeGateOf three_of_nativeGateOf
HasTwoSharpTests hasTwoSharpTests_iff two_le_load_bearing_relative two_le_not_implied
three_of_nativeGateOf_of_two_le two_le_of_entangling no_candidateCone_cnot_reflY CandidateCone
DenseBoundaryOrbit maxConeOf_avail_eq_of_dense dim_of_nativeGateOf_dense three_of_nativeGateOf_dense chartBody_eq_eball_of_dense
eball exists_affine_image_eq_eball chartBody_eq_eball eball_three not_boundaryTransitive_of_nonextreme_boundary
SharpSeed PreservesBody SeedOrbitAvailable BoundaryTransitive seedOrbit_ball3_eq ballEffect_mem_avail
hypotheses_tr hypotheses_restrict preservesBody_drive preservesBody_driveWords boundaryTransitive_ball3Drive
FiniteStage DirectedStages SCInf BinaryVisible FiniteRank sharpSeed_completion exists_chart_of_finiteRank
OpDatum AffineRespect preservesBody_inducedEquiv CompletionChart chartBody exists_completionChart
ElementaryDrivability SingletonFaces RelStrictConvex CopyNatural card_le_two_of_centrallySymmetric ball3Drive
Composite LocallyTomographic local_tomography_physical qm_implies_oiCore realizesSealedOICore_of_control
""".split()

files = sorted(f for f in os.listdir(BASE) if f.endswith(".lean"))
text = {f: open(os.path.join(BASE, f), encoding="utf-8").read().split("\n") for f in files}
decl = re.compile(r"^(?:noncomputable )?(?:private )?(theorem|lemma|def|structure|abbrev|class)\s+(\S+)")

for name in NAMES:
    hits = []
    for f in files:
        for i, line in enumerate(text[f]):
            m = decl.match(line)
            if m and m.group(2) == name:
                hits.append((f, i + 1))
    if not hits:
        print("== %-40s NOT FOUND" % name)
        continue
    for f, ln in hits:
        hdr = []
        for j in range(ln - 1, min(ln + 12, len(text[f]))):
            hdr.append(text[f][j].rstrip())
            if text[f][j].rstrip().endswith(":=") or text[f][j].rstrip().endswith(":= by") or \
               text[f][j].rstrip().endswith("where") or " := " in text[f][j]:
                break
        users = sorted({g for g in files if g != f and re.search(r"\b%s\b" % re.escape(name), "\n".join(text[g]))})
        print("== %s  %s:%d" % (name, f, ln))
        for h in hdr:
            print("     " + h)
        print("   used outside its module in: %s" % (", ".join(users) if users else "(none)"))
