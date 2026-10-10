import subprocess
L = "9f9f8257a980a1819fbbc1dc0019917cf8678626"; P = "verification/lean-mathlib/OIBridge/"
cites = [
 ("CompositionOrder.lean", 378, "not_stagePreserving_of_infiniteOrderOn"), ("CompositionOrder.lean", 348, "finiteOrderOn_of_stagePreserving"),
 ("CompositionOrder.lean", 149, "exists_return"), ("CompositionOrder.lean", 171, "exists_common_period"),
 ("TransitiveBody.lean", 109, "chartBody_isCompact"), ("TransitiveBody.lean", 80, "chartBody_convex"),
 ("CompletionAction.lean", 352, "preservesBody_inducedEquiv"),
 ("OperationalAssembly.lean", 658, "readout_is_localLuders"), ("OperationalAssembly.lean", 675, "pureSeedPrep_available_of_swap"),
 ("OperationalAssembly.lean", 492, None), ("OperationalAssembly.lean", 515, None), ("OperationalAssembly.lean", 649, None),
 ("InternalObserver.lean", 249, "recordInstr"), ("InternalObserver.lean", 290, "recordInstr_not_passive"),
 ("StateMixingCoupling.lean", 56, None), ("StateMixingCoupling.lean", 59, None), ("LieRankSource.lean", 209, None),
 ("DiscreteCompletion.lean", 1926, None), ("DiscreteCompletion.lean", 1522, None), ("DiscreteCompletion.lean", 1948, None),
 ("SubstratumSource.lean", 103, "genTheory_avail_conj"), ("KInfFoundations.lean", 425, "cyc3"), ("KInfFoundations.lean", 427, "cyc3_apply"),
]
cache = {}
def lines(f):
    if f not in cache:
        cache[f] = subprocess.run(["git", "-C", "/home/user/incompleteness", "show", f"{L}:{P}{f}"], capture_output=True, text=True, check=True).stdout.split("\n")
    return cache[f]
miss = 0
for f, n, ident in cites:
    ls = lines(f); window = "\n".join(ls[max(0, n - 2):n + 1]); text = ls[n - 1].strip() if n - 1 < len(ls) else "<EOF>"
    ok = (ident is None) or (ident in window)
    if not ok: miss += 1
    print(("OK   " if ok else "MISS ") + f"{f}:{n} [{ident}] " + text[:110])
print("MISSING", miss, "of", len(cites))
