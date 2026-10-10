"""bridge_check3.py -- thread I1, stage 6: what can the pair-cone modules see at all?

Run from pt/I1/ as:  python3 -I -B bridge_check3.py > bridge_check3.out 2> bridge_check3.err
Read-only on ../base/. Deterministic.

QUESTION. bridge_check.py / bridge_check2.py showed no module importing both an I1 module (or
the M-level carrier) and a pair-cone module. Which OIBridge modules are inside the import closure
of the pair-cone modules at all? A kernel statement at level P can mention only objects defined in
that closure.

DECISION RULE (fixed before the first run). Print the transitive OIBridge import closure of
CompositeDimension and of K2Guard (the pair-cone modules), and the closure's intersection with a
fixed list HLEV of modules whose subject is hidden histories / substratum / the sealed core / the
stochastic-level results (I1's twelve modules plus HiddenMemory, RecurrenceHorizon,
RootedClassification, StochasticInterface, SemigroupTransfer, Equivalence, EquivalenceChain,
Finiteness, CanonicalMeasure, SubstratumInterface, SubstratumSource, StructuralClosure,
OperationalAssembly). Verdict `DISJOINT` if the intersection is empty, else `MEETS n` with the
list. Countercontrol: the closure of K2Guard must contain CompositeDimension (else VOID).
"""
import os
import re
import sys

ROOT = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
HLEV = ["OIRealization", "IndependenceCensus", "ManuscriptAxioms", "RouteB", "SubstratumInterfaceAudit",
        "BackgroundIndependence", "A6Instantiation", "C3Necessity", "CausalReadback",
        "PhysicalC4Discharge", "PhysicalC4StorageReadback", "InternalObserver", "HiddenMemory",
        "RecurrenceHorizon", "RootedClassification", "StochasticInterface", "SemigroupTransfer",
        "Equivalence", "EquivalenceChain", "Finiteness", "CanonicalMeasure", "SubstratumInterface",
        "SubstratumSource", "StructuralClosure", "OperationalAssembly"]


def main():
    files = sorted(f[:-5] for f in os.listdir(ROOT) if f.endswith(".lean"))
    direct = {}
    for m in files:
        with open(os.path.join(ROOT, m + ".lean"), encoding="utf-8") as fh:
            direct[m] = [x for x in re.findall(r"^import\s+OIBridge\.(\S+)", fh.read(), re.M) if x in files]
    memo = {}

    def clo(m):
        if m not in memo:
            acc = set()
            for x in direct[m]:
                acc.add(x)
                acc |= clo(x)
            memo[m] = acc
        return memo[m]

    missing = [h for h in HLEV if h not in files]
    print("HLEV modules absent from the tree: %s" % (",".join(missing) if missing else "-"))
    ctrl = "CompositeDimension" in clo("K2Guard")
    print("control (CompositeDimension in closure(K2Guard)): %s" % ctrl)
    meet = set()
    for p in ("CompositeDimension", "K2Guard"):
        c = sorted(clo(p))
        print("closure(%s) [%d]: %s" % (p, len(c), " ".join(c)))
        meet |= set(c) & set(HLEV)
    if not ctrl:
        print("VERDICT VOID")
    elif not meet:
        print("VERDICT DISJOINT")
    else:
        print("VERDICT MEETS %d: %s" % (len(meet), " ".join(sorted(meet))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
