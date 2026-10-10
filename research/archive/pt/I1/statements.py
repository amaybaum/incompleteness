"""statements.py -- thread I1, stage 6: exact-quote appendix for INVENTORY.md.

Run from pt/I1/ as:  python3 -I -B statements.py > statements.out 2> statements.err
Read-only on ../base/. Deterministic.

DECISION RULE (fixed before the first run). For every (module, name) in DECLS: locate the first
line `^(...modifiers...)(def|theorem|structure|abbrev|noncomputable abbrev) <name>\b` outside block
comments; print, byte for byte, the immediately preceding docstring (if the previous nonblank line
closes a `/-- ... -/` block, from its `/--` line) and the declaration lines up to and including
the first line containing `:=` or ending in `where` (at most 40 lines). Print `MISSING` if the
name is not found; any MISSING is reported in the final count line. For every (file, line) in
MLINES print that manuscript line verbatim. Every block is headed `[S:<key>] <path>:<a>-<b>`.
The output is the exact text the INVENTORY records quote or abridge (abridgements in INVENTORY
are marked with an ellipsis).

RUN 2 AMENDMENT (pre-run edit, recorded in NOTES.md; run 1 kept as statements.run1.*): the
MLINES list of run 1 held imprecise picks (Methodology.md:225 is blank, :243 a lead-in line) and
lacked lines INVENTORY quotes. The list is replaced by the lines INVENTORY cites; DECLS and the
extraction rule are unchanged.
"""
import os
import re
import sys

OIB = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
BASE = os.path.join("..", "base")

DECLS = [
    ("IndependenceCensus", "Core"), ("IndependenceCensus", "vis"), ("IndependenceCensus", "swapFn"),
    ("IndependenceCensus", "flipFn"), ("IndependenceCensus", "core_hidden_drives_visible"),
    ("IndependenceCensus", "core_visible_period_two"), ("IndependenceCensus", "core_observer_minimal"),
    ("IndependenceCensus", "core_capacity_saturates"), ("IndependenceCensus", "core_history_readback"),
    ("IndependenceCensus", "CoreC1C4"), ("IndependenceCensus", "core_isC1C4"),
    ("IndependenceCensus", "IsLocalOnB"), ("IndependenceCensus", "IsLocalOnVH"),
    ("IndependenceCensus", "oi_core_underdetermines_completion"),
    ("OIRealization", "coreIdx"), ("OIRealization", "readVisible"),
    ("OIRealization", "RealizesSealedOICore"), ("OIRealization", "realizesSealedOICore_of_control"),
    ("OIRealization", "SealedCoreIsFiniteOI"), ("OIRealization", "sealedCore_is_finiteOI"),
    ("OIRealization", "sameCore_both_sides"), ("OIRealization", "finiteOI_not_implies_inert"),
    ("OIRealization", "finiteOI_not_implies_closure"),
    ("CompletedOI", "OICore"), ("CompletedOI", "oiCore_not_completedOI"),
    ("CompletedOI", "qm_implies_oiCore"), ("CompletedOI", "oiCore_forward_redundancy"),
    ("RouteB", "DerivedOI"), ("RouteB", "DerivedOICore"), ("RouteB", "ExchangesAvailable"),
    ("RouteB", "PhasesAvailable"), ("RouteB", "ReadWriteAvailable"), ("RouteB", "FalsifierUnavailable"),
    ("RouteB", "RouteBTarget"), ("RouteB", "derivedOICore_of_qm"),
    ("RouteB", "substratumTheory_realizesSealedOICore"), ("RouteB", "routeB_target"),
    ("RouteB", "derivedOICore_not_phaseFree"),
    ("ManuscriptAxioms", "A1Realized"), ("ManuscriptAxioms", "A2Realized"),
    ("ManuscriptAxioms", "A1A2Realized"), ("ManuscriptAxioms", "a1_every_theory"),
    ("ManuscriptAxioms", "a2_of_control"), ("ManuscriptAxioms", "ConfigurationLevel"),
    ("ManuscriptAxioms", "configurationLevel_not_phaseFree"),
    ("ManuscriptAxioms", "configurationLevel_not_qm"),
    ("SubstratumInterfaceAudit", "Substratum"), ("SubstratumInterfaceAudit", "A1"),
    ("SubstratumInterfaceAudit", "A2"), ("SubstratumInterfaceAudit", "A3"),
    ("SubstratumInterfaceAudit", "A4Exact"), ("SubstratumInterfaceAudit", "A4"),
    ("SubstratumInterfaceAudit", "A5"), ("SubstratumInterfaceAudit", "A3Family"),
    ("SubstratumInterfaceAudit", "waveSubstratum_A1"), ("SubstratumInterfaceAudit", "SourcedOI"),
    ("SubstratumInterfaceAudit", "permTheory_realizesSealedOICore"),
    ("SubstratumInterfaceAudit", "permTheory_twoState"), ("SubstratumInterfaceAudit", "obsTheory"),
    ("SubstratumInterfaceAudit", "obsTheory_rule_independent"),
    ("SubstratumInterfaceAudit", "obs_embeddedObservation"), ("SubstratumInterfaceAudit", "obs_not_qm"),
    ("BackgroundIndependence", "A6Inv"), ("BackgroundIndependence", "A6Glob"),
    ("BackgroundIndependence", "A6Cov"), ("BackgroundIndependence", "a6cov_all"),
    ("BackgroundIndependence", "d3b_not_a6inv"),
    ("A6Instantiation", "pk2a_bridge"), ("A6Instantiation", "cx3b_complex_not_A1"),
    ("C3Necessity", "c3_necessity"), ("C3Necessity", "card_hidden_ge_two_pow_Istar"),
    ("CausalReadback", "C4e"), ("CausalReadback", "C4r"), ("CausalReadback", "PIndivisibleWithin"),
    ("CausalReadback", "causal_readback_verdict"), ("CausalReadback", "control_separation"),
    ("PhysicalC4Discharge", "RoutedReadback"), ("PhysicalC4Discharge", "core_not_routedReadback"),
    ("PhysicalC4Discharge", "routed_forces_return_indivisibility"),
    ("PhysicalC4Discharge", "routed_forces_indivisible_somewhere"),
    ("PhysicalC4Discharge", "LatticeCutReadback"), ("PhysicalC4Discharge", "latticeCutReadback_iff"),
    ("PhysicalC4StorageReadback", "RoutedReadbackAtStorage"),
    ("PhysicalC4StorageReadback", "core_routedReadbackAtStorage_two"),
    ("PhysicalC4StorageReadback", "storageReadback_not_implies_routedReadback"),
    ("PhysicalC4StorageReadback", "routedReadback_not_implies_storageReadback"),
    ("InternalObserver", "Records"), ("InternalObserver", "IsInternalObserver"),
    ("InternalObserver", "internal_complete_iff"), ("InternalObserver", "no_complete_internal_observer"),
    ("StochasticInterface", "ensemble_underdetermined"),
    ("StochasticInterface", "waveSubstratum_stochastic_interface_gap"),
    ("PassiveIndependence", "passive_not_implies_oiCore"), ("DiagonalTheory", "control_independent"),
    ("RankGapTheory", "five_way_minimality"), ("SubstantiveCensus", "substantive_census"),
    ("LevelOneSeam", "levelOne_independent"), ("LevelOneRecursion", "levelOne_independent_of_recursion"),
    ("PhysicalCharacterization", "inert_independent"), ("IsometryExtension", "operational_classification"),
    ("SpectatorBridge", "InertSpectatorCompositionality"), ("AncillaClosure", "IteratedAncillaClosure"),
    ("OperationalAssembly", "HasCompositeUnitaryControl"),
    ("KrausSoundness", "ExactFiniteEndomorphicQuantumOps"),
]

MLINES = [("papers/Main.md", n) for n in (22, 36, 38, 40, 44, 46, 48, 50, 52, 54, 56, 60, 62, 66, 68,
                                         72, 74, 76, 78, 80, 82, 86, 99, 137, 141, 159, 167, 286,
                                         433, 447, 456, 484, 486, 492, 594, 602, 612, 614)]
MLINES += [("papers/Methodology.md", n) for n in (160, 162, 226, 227, 235, 243, 245, 247, 249, 251)]
MLINES += [("papers/Substratum.md", n) for n in (92, 94, 96, 98, 100, 102, 104, 108, 122, 124, 126,
                                                 128, 204, 217)]
MLINES += [("papers/Explainer.md", n) for n in (47, 65, 67, 69, 905)]
MLINES += [("book/ch01-observation.md", n) for n in (22, 24, 26, 28, 30, 34, 38, 53, 55, 57, 59, 61,
                                                     71, 79)]
MLINES += [("verification/ROADMAP.md", n) for n in (44, 45, 46, 47, 48, 49, 65, 66, 69, 738, 739, 740,
                                                     741, 775, 776, 780, 781, 782, 783, 840, 841,
                                                     842, 852, 853, 861, 862, 888, 889, 890, 894,
                                                     895, 896, 903, 904, 905, 906, 907, 1455, 1456,
                                                     1457, 1458, 1459, 1460, 1461)]
MLINES += [("verification/README.md", n) for n in (73, 74, 75, 76, 77, 78, 79, 84, 85, 86, 87, 88, 89,
                                                    91, 92, 631, 632, 633, 634, 635, 636, 637, 638,
                                                    639, 640, 747, 748, 749)]

HEADRE = r"^(?:@\[[^\]]*\]\s*)*(?:(?:noncomputable|private|protected)\s+)*(?:def|theorem|structure|abbrev|inductive)\s+"


def block(mod, name):
    path = os.path.join(OIB, mod + ".lean")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    pat = re.compile(HEADRE + re.escape(name) + r"(?![A-Za-z0-9_'])")
    depth = 0
    for i, ln in enumerate(lines):
        if depth == 0 and pat.match(ln):
            start = i
            k = i - 1
            while k >= 0 and lines[k].strip() == "":
                k -= 1
            if k >= 0 and lines[k].rstrip().endswith("-/"):
                j = k
                while j >= 0 and "/--" not in lines[j]:
                    j -= 1
                if j >= 0:
                    start = j
            end = i
            for e in range(i, min(len(lines), i + 40)):
                end = e
                if ":=" in lines[e] or re.search(r"\bwhere\s*$", lines[e]):
                    break
            return path, start + 1, end + 1, lines[start:end + 1]
        depth = max(0, depth + ln.count("/-") - ln.count("-/"))
    return path, 0, 0, None


def main():
    missing = 0
    for mod, name in DECLS:
        path, a, b, txt = block(mod, name)
        rel = os.path.relpath(path, BASE)
        if txt is None:
            missing += 1
            print("[S:%s] %s  MISSING" % (name, rel))
            continue
        print("[S:%s] %s:%d-%d" % (name, rel, a, b))
        for t in txt:
            print("    " + t)
    for f, n in MLINES:
        with open(os.path.join(BASE, f), encoding="utf-8") as fh:
            ls = fh.read().split("\n")
        print("[S:%s:%d] %s:%d" % (os.path.basename(f), n, f, n))
        print("    " + ls[n - 1])
    print("COUNT declarations=%d missing=%d manuscript_lines=%d" % (len(DECLS), missing, len(MLINES)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
