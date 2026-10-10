"""EQ2-C, C1: mechanical check of every kernel citation (file:line identifier) used in RESULT.md.

For each entry the base file is read (path given as argv[1], the OIBridge directory of the read-only base tree) and the
cited line must contain the identifier as a whole token. DECISION RULE (fixed before the first run): the verdict prints
only if every citation is found at its line; a countercontrol (a deliberately wrong line) must NOT be found.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from c_common import Checks  # noqa: E402

BASE = sys.argv[1]
ABBR = {"SC": "StageCompletion", "CA": "CompletionAction", "KF": "KInfFoundations", "OG": "OrbitGeneration",
        "ON": "OrbitNormalization", "TB": "TransitiveBody", "IIP": "InvariantInnerProduct", "ES": "EffectSpace",
        "DO": "DenseOrbit", "K1B": "K1Bridge", "CD": "CompositeDimension", "RSB": "RelcSelectBlock",
        "RSP": "RelcSelectParity", "RC5": "RelcSelectC5", "OC": "OddChar", "PN": "ParityNot", "K2G": "K2Guard",
        "ST": "SharpTests", "IL": "ImplementationLocality", "SS": "SubstratumSource", "SCl": "StructuralClosure",
        "MR": "MinimalRepertoire", "LRS": "LieRankSource", "RS": "ReachabilitySeam", "AC": "AncillaClosure",
        "CL": "CoherentLift", "MC": "MonoidalCompletion", "SI": "SubstratumInterface",
        "MRv": "MicroscopicReversibility", "LOS": "LevelOneSeam", "TC": "TypedCompletion",
        "CGOP": "CarrierGeneralOIPlus", "CI": "CompositeInterface", "OA": "OperationalAssembly",
        "NGB": "NativeGateBall"}
CITES = """
SC:63 DirectedStages; SC:78 SCInf; SC:224 sharpSeed_completion; SC:244 BinaryVisible; SC:299 FiniteRank;
SC:304 exists_chart_of_finiteRank; CA:46 OpDatum; CA:58 AffineRespect; CA:144 CompletionChart;
CA:154 exists_completionChart; CA:166 chartBody; CA:325 Undoes; CA:333 inducedEquiv; CA:352 preservesBody_inducedEquiv;
CA:461 midOp_not_affineRespect; KF:116 IsEffectOn; KF:130 IsBoundaryState; KF:135 SupportingEffectComplete;
KF:139 SingletonFaces; KF:144 RelStrictConvex; KF:154 PerfectlyDistinguishable; KF:160 CentrallySymmetric;
KF:227 isBoundaryState_of_certain_proper; KF:264 ElementaryDrivability; KF:284 CopyNatural;
KF:575 relStrictConvex_of_supporting_singleton; KF:590 singletonFaces_of_relStrictConvex;
KF:601 not_isBoundaryState_of_mem_interior; KF:632 card_le_two_of_centrallySymmetric; KF:658 singletonFaces_closedBall;
OG:65 SharpSeed; OG:69 PreservesBody; OG:74 SeedOrbitAvailable; OG:79 BoundaryTransitive;
OG:620 not_boundaryTransitive_flow; ON:159 effTr; ON:177 conjTr; ON:217 isEffectOn_tr; ON:295 hypotheses_tr;
ON:427 sharpSeed_restrict; ON:529 hypotheses_restrict; ON:571 driveWords3; ON:667 boundaryTransitive_ball3Drive;
TB:223 IsBodyGroup; TB:284 isBoundaryState_of_extreme; TB:290 extreme_of_isBoundaryState_of_transitive;
TB:301 not_boundaryTransitive_of_nonextreme_boundary; TB:356 centroid_fixed_of_preservesBody; TB:388 centroid_mem;
TB:427 centroid_mem_interior; TB:602 exists_affine_image_eq_eball; TB:651 chartBody_eq_eball; TB:671 eball_three;
TB:772 not_boundaryTransitive_square2; IIP:152 centroid_fixed; IIP:336 invariant_inner_product; ES:567 EffectsOn;
ES:572 maxConeOf_avail_eq; ES:858 not_boundaryTransitive_of_countable; DO:53 DenseBoundaryOrbit;
DO:209 chartBody_eq_eball_of_dense; DO:243 maxConeOf_avail_eq_of_dense; DO:299 dim_of_nativeGateOf_dense;
DO:307 three_of_nativeGateOf_dense; K1B:49 NativeGateOf; K1B:64 EntanglingOf; K1B:73 nativeGate_of_cone_eq;
K1B:108 nativeGate_of_avail; K1B:128 dim_of_nativeGateOf; K1B:138 three_of_nativeGateOf; CD:97 W; CD:112 homMap;
CD:161 prodState; CD:186 maxCone; CD:198 actT; CD:201 actC; CD:210 IsNot; CD:218 NativeGate; CD:229 Entangling;
CD:471 actT_actT; CD:503 opGate_homMap_comp; CD:682 finrank_plus_eq_finrank_minus; CD:775 cnot; CD:797 nflip;
CD:860 cnot_relC; CD:1160 nativeGate_cnot; CD:1380 entangling_cnot; CD:1639 lift; CD:1805 corner_form; CD:1878 Mfwd;
CD:1923 actT_tens; CD:1930 actC_tens; CD:1945 gate_actC; CD:1965 gate_corner_neg; CD:2723 dim_of_nativeGate;
CD:2748 three_of_nativeGate; CD:2765 cnot1; CD:2869 not_entangling_cnot1; RSB:45 CtrlGate;
RSB:53 ctrlGate_of_nativeGate; RSB:92 gate_actC_ctrl; RSB:99 gate_corner_neg_ctrl; RSB:113 gt_corner_neg_ctrl;
RSB:716 blockData_of_ctrlGate; RSB:725 not_entangling_one_ctrl; RSB:739 dim_of_ctrlGate; RSB:753 three_of_ctrlGate;
RSP:329 finrank_plus_eq_finrank_minus_relC; RSP:354 not_even_of_relC; RC5:51 nC5; RC5:68 isNot_nC5; RC5:89 sgnC5;
RC5:94 pcC5; RC5:104 ptC5; RC5:134 gC5; RC5:154 gC5_frame; RC5:161 gC5_relT; RC5:179 gC5_not_relC;
RC5:242 selC5_target; RC5:303 selC5_core; RC5:333 prodEffVal_gC5_prodState; RC5:360 gC5_posFwd; RC5:369 gC5_posInv;
RC5:393 relT_not_dimension_selecting; OC:56 nK; OC:59 zK; OC:102 isNot_nK; OC:176 finrank_plus_eq_finrank_minus_nK;
OC:238 entW; PN:292 diagSign; PN:299 homMap_diagSign; K2G:46 reflY; K2G:95 CandidateCone;
K2G:143 no_candidateCone_cnot_reflY; K2G:173 actT_prodState; K2G:234 three_of_nativeGate_of_two_le;
K2G:253 three_of_nativeGateOf_of_two_le; ST:41 HasTwoSharpTests; ST:137 hasTwoSharpTests_of_two_le;
ST:155 hasTwoSharpTests_iff; ST:185 two_le_load_bearing_relative; IL:244 ImplementationClass; IL:268 InstAvail;
IL:352 ImplementationGenerated; IL:359 ContextStable; IL:364 LabelInvariant; IL:374 fullClass; IL:506 Architecture;
IL:530 realized_of_instAvail; IL:852 genTheory; SS:77 DrivesElementary; SS:86 QuantumArchitecture;
SS:136 genTheory_qm_of_quantumArchitecture; SCl:180 substratumClass; SCl:183 StructurallyClosed;
SCl:231 substratumClass_arch; SCl:261 substratumClass_contextStable; SCl:275 substratumClass_labelInvariant;
SCl:289 substratumClass_daggerStable; SCl:364 quantumArchitecture_iff_drives_of_closed; SCl:401 ExtendsSubstratum;
SCl:408 substratum_extension_quantum_iff_drives; MR:488 ancBlock_tensorOf_one; LRS:199 transition; LRS:209 phaseGate;
LRS:228 permMatrix_one'; RS:95 flow; AC:457 ancBlock; CL:92 permMatrix; MC:193 tensorOf; SI:75 IsMonomial;
SI:126 preservesDiag_conj_of_monomial; MRv:216 DaggerStable; LOS:186 ExactAllFiniteEndomorphicQuantumOps;
TC:165 TypedOperationalTheory; TC:291 ShadowQuantum; TC:838 shadowQuantum_of_typed; TC:850 typed_determined_iff;
TC:916 typedDiag; CGOP:207 oiPlus_iff_qm; CI:445 JointReversible; OA:594 FiniteOperationalTheory;
NGB:176 p_le_one; NGB:194 parity; NGB:248 dim_of_bounds; CD:257 plusSpace; CD:261 minusSpace;
CD:274 finrank_plus_add_finrank_minus; CD:722 p_le_one_of_blockData; CD:2712 pos_of_isNot;
SC:193 stageEffects_isEffectOn; ON:423 isEffectOn_restrict; ES:337 boundaryTransitive_fullAut;
KF:617 relStrictConvex_of_strictConvex; ES:374 sharpFamily_subset_avail; K1B:88 jointStatesOf_eq;
DO:284 nativeGate_of_avail_dense; ON:674 preservesBody_driveWords3
"""
C = Checks("c1_cite")
cache = {}


def line_of(abbr, n):
    f = ABBR[abbr]
    if f not in cache:
        with open(os.path.join(BASE, f + ".lean"), encoding="utf-8") as fh:
            cache[f] = fh.read().split("\n")
    lines = cache[f]
    return lines[n - 1] if 0 < n <= len(lines) else ""


def found(abbr, n, name):
    ln = line_of(abbr, n)
    return re.search(r"(^|[\s(.{])" + re.escape(name) + r"($|[\s:(}])", ln) is not None


entries = [e.strip() for e in CITES.replace("\n", " ").split(";") if e.strip()]
missing = []
for e in entries:
    loc, name = e.split()
    abbr, n = loc.split(":")
    if not found(abbr, int(n), name):
        missing.append(e)
C.check(f"CITE every one of the {len(entries)} kernel citations is at its stated line (missing: {missing})",
        missing == [])
C.check("CITE countercontrol: deliberately wrong lines are not accepted (dim_of_ctrlGate at RSB:740, CtrlGate at "
        "RSB:46, nK at OC:57)", not found("RSB", 740, "dim_of_ctrlGate") and not found("RSB", 46, "CtrlGate")
        and not found("OC", 57, "nK"))
sys.exit(C.finish(f"CITATIONS-VERIFIED: {len(entries)} file:line citations at bcbc516f"))
