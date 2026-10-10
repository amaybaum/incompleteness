import subprocess, sys
L = "9f9f8257a980a1819fbbc1dc0019917cf8678626"
P = "verification/lean-mathlib/OIBridge/"
cites = [
 # bridge
 ("CompositeDimension.lean", 1220, None), ("CompositeDimension.lean", 1222, None),
 ("ImplementationLocality.lean", 207, "redundancy_fails"), ("CompositeInterface.lean", 245, "lt"),
 ("StructuralClosure.lean", 261, "substratumClass_contextStable"), ("SubstratumInterface.lean", 75, None),
 ("KInfFoundations.lean", 264, "ElementaryDrivability"),
 # origin
 ("SubstratumInterface.lean", 126, "preservesDiag_conj_of_monomial"), ("ImplementationLocality.lean", 530, None),
 ("StructuralClosure.lean", 231, None), ("SubstratumInterfaceAudit.lean", 350, None),
 ("InstrumentRealization.lean", 628, "onesClass_arch"), ("InstrumentRealization.lean", 833, "isometry_fixes_ones"),
 ("InstrumentRealization.lean", 508, "onesClass_gateFlow"), ("SubstratumSource.lean", 103, "genTheory_avail_conj"),
 ("LiftAudit.lean", 138, "gateFlow_half_entries"), ("PhaseSource.lean", 79, None),
 ("InstrumentRealization.lean", 398, "instAvail_unitary_fixes_ones"), ("SubstratumInterface.lean", 91, None),
 ("ReadWriteControl.lean", 96, None), ("CoherentContinuumSource.lean", 292, None), ("InternalObserver.lean", 249, None),
 ("InternalObserver.lean", 290, None), ("AncillaInterference.lean", 161, None), ("AncillaInterference.lean", 163, None),
 ("LiftAudit.lean", 47, None), ("LiftAudit.lean", 200, None), ("StateMixingCoupling.lean", 45, None), ("StateMixingCoupling.lean", 50, None),
 ("DiscreteCompletion.lean", 1929, None), ("DiscreteCompletion.lean", 1933, None), ("DiscreteCompletion.lean", 1948, None),
 ("DiscreteCompletion.lean", 1522, None), ("BarandesTuple.lean", 430, None), ("OperationalAssembly.lean", 658, None),
 ("LiftAudit.lean", 812, "derivedOI_qm_iff_layerFlowExecutable"), ("LiftAudit.lean", 783, None), ("RouteB.lean", 161, "derivedOI_qm_iff_phaseFree"),
 ("RouteB.lean", 290, None), ("LiftAudit.lean", 750, None), ("LiftAudit.lean", 754, None), ("LiftAudit.lean", 770, None),
 ("MinimalRepertoire.lean", 569, "oiPlusMin_iff_qm"), ("KInfFoundations.lean", 449, "ball3Drive"),
 ("SubstratumInterfaceAudit.lean", 654, None), ("SubstratumInterfaceAudit.lean", 660, None), ("ImplementationLocality.lean", 904, None),
 ("StateMixingCoupling.lean", 511, None), ("KInfFoundations.lean", 425, "cyc3"), ("KInfFoundations.lean", 427, "cyc3_apply"),
 # equivalence
 ("CarrierGeneralOIPlus.lean", 207, "oiPlus_iff_qm"), ("TypedCompletion.lean", 850, "typed_determined_iff"),
 ("SubstratumSource.lean", 136, "genTheory_qm_of_quantumArchitecture"), ("TransitiveBody.lean", 602, None),
 ("DenseOrbit.lean", 174, None), ("DenseOrbit.lean", 398, None), ("DenseOrbit.lean", 403, None),
 ("KInfFoundations.lean", 590, None), ("KInfFoundations.lean", 632, None),
 ("ImplementationLocality.lean", 506, "Architecture"), ("ImplementationLocality.lean", 359, "ContextStable"), ("ImplementationLocality.lean", 364, "LabelInvariant"),
 ("SubstratumSource.lean", 77, "DrivesElementary"), ("K2Guard.lean", 143, "no_candidateCone_cnot_reflY"),
 ("K2Guard.lean", 106, None), ("K2Guard.lean", 110, None), ("K2Guard.lean", 134, None),
 ("QuasilocalCharacterization.lean", 359, "canon_unique"), ("QuasilocalCharacterization.lean", 497, "systemEquiv_dyn"),
]
cache = {}
def lines(f):
    if f not in cache:
        cache[f] = subprocess.run(["git", "-C", "/home/user/incompleteness", "show", f"{L}:{P}{f}"], capture_output=True, text=True, check=True).stdout.split("\n")
    return cache[f]
miss = 0
for f, n, ident in cites:
    ls = lines(f); window = "\n".join(ls[max(0, n - 2):n + 1])
    text = ls[n - 1].strip() if n - 1 < len(ls) else "<EOF>"
    ok = (ident is None) or (ident in window)
    if not ok: miss += 1
    print(("OK   " if ok else "MISS ") + f"{f}:{n} [{ident}] " + text[:110])
print("MISSING", miss, "of", len(cites))
