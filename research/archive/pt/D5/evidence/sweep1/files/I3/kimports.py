"""I3 import-graph check: which kernel modules can consume the K-programme pair carrier at L.

DECISION RULE (fixed before the first run):
- K set: the 22 modules governed by the K-programme rounds (as in kcensus.py).
- An import edge is a line `import OIBridge.<M>` in `<N>.lean`, N, M modules of `verification/lean-mathlib/OIBridge/`.
  The aggregator `verification/lean-mathlib/OIBridge.lean` is not a module of the tree and is excluded.
- Report (1) for each K module its importers and its OIBridge imports; (2) the non-K modules that import a K module
  (a Lean declaration outside K can use a K declaration only through such an edge, transitively); (3) the non-K
  modules a K module imports; (4) the transitive closure of importers of CompositeDimension (the pair carrier `W d`,
  `NativeGate`, `cnot`) and of KInfFoundations (`ElementaryDrivability`).
- A "bridge at L by import" from the pair carrier to a non-K module exists iff (4) for CompositeDimension contains a
  non-K module. The output states the set; no verdict word is printed beyond the set comparison.
"""
import os
import re
import sys

BASE = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")
K = [
    "KInfFoundations", "OrbitGeneration", "OrbitNormalization", "TransitiveBody", "StageCompletion",
    "InvariantInnerProduct", "CompletionAction", "CompositionOrder", "CompositeInterface", "CompositeDimension",
    "EffectSpace", "K1Bridge", "SharpTests", "K2Guard", "DenseOrbit", "NativeGateBall", "OddChar", "ParityNot",
    "RelcSelectParity", "RelcSelectBlock", "RelcSelectSqueeze", "RelcSelectC5",
]


def main():
    mods = sorted(f[:-5] for f in os.listdir(BASE) if f.endswith(".lean"))
    imports = {}
    for m in mods:
        with open(os.path.join(BASE, m + ".lean"), encoding="utf-8") as fh:
            imports[m] = sorted(set(re.findall(r"^import OIBridge\.([A-Za-z0-9_]+)\s*$", fh.read(), re.M)))
    importers = {m: sorted(n for n in mods if m in imports[n]) for m in mods}
    kset = set(K)
    print(f"modules in tree: {len(mods)}; K modules: {len(K)}; K modules present: {sum(1 for k in K if k in mods)}")
    print()
    print("## (1) K modules: importers / OIBridge imports")
    for k in K:
        print(f"{k}: importers = {importers[k]} ; imports = {imports[k]}")
    print()
    nonk_importing = sorted(n for n in mods if n not in kset and any(i in kset for i in imports[n]))
    print(f"## (2) non-K modules importing a K module: {nonk_importing}")
    nonk_imported = sorted({i for k in K for i in imports[k] if i not in kset})
    print(f"## (3) non-K modules imported by a K module: {nonk_imported}")
    for target in ("CompositeDimension", "KInfFoundations"):
        seen, frontier = set(), [target]
        while frontier:
            x = frontier.pop()
            for n in importers.get(x, []):
                if n not in seen:
                    seen.add(n)
                    frontier.append(n)
        closure = sorted(seen)
        outside = sorted(s for s in seen if s not in kset)
        print(f"## (4) transitive importers of {target}: {closure}")
        print(f"     of which outside K: {outside}")
    print("END")


if __name__ == "__main__":
    sys.exit(main())
