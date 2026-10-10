"""bridge_check2.py -- thread I1, stage 6: can a two-step route H -> M -> P exist at L?

Run from pt/I1/ as:  python3 -I -B bridge_check2.py > bridge_check2.out 2> bridge_check2.err
Read-only on ../base/. Deterministic.

QUESTION. bridge_check.py found no module importing both an I1 module and a pair-cone module.
A two-step route would need some module that imports the M-level carrier (OperationalAssembly,
where `FiniteOperationalTheory` is defined) together with a pair-cone module (CompositeDimension
or K2Guard): only there could a theorem relate a matrix-level theory to `W 3`.

DECISION RULE (fixed before the first run). Build the OIBridge import closure as in
bridge_check.py. List every module whose closure-or-self contains OperationalAssembly AND
contains CompositeDimension or K2Guard. Verdict `NO-MODULE` if the list is empty, else
`MODULES n` with the list (whether any of their theorems is a bridge is thread I4's scope and is
not decided here). Countercontrol: OperationalAssembly must lie in the closure of
OIRealization (an I1 module that consumes FiniteOperationalTheory); if not, VOID.
"""
import os
import re
import sys

ROOT = os.path.join("..", "base", "verification", "lean-mathlib", "OIBridge")


def main():
    mods = sorted(f[:-5] for f in os.listdir(ROOT) if f.endswith(".lean"))
    direct = {}
    for m in mods:
        with open(os.path.join(ROOT, m + ".lean"), encoding="utf-8") as fh:
            direct[m] = [x for x in re.findall(r"^import\s+OIBridge\.(\S+)", fh.read(), re.M)
                         if x + ".lean" in os.listdir(ROOT)]
    closure = {}

    def clo(m):
        if m not in closure:
            acc = set()
            for x in direct[m]:
                acc.add(x)
                acc |= clo(x)
            closure[m] = acc
        return closure[m]

    for m in mods:
        clo(m)
    ctrl = "OperationalAssembly" in closure["OIRealization"]
    print("control (OperationalAssembly in closure(OIRealization)): %s" % ctrl)
    hits = [m for m in mods
            if "OperationalAssembly" in (closure[m] | {m})
            and ({"CompositeDimension", "K2Guard"} & (closure[m] | {m}))]
    for m in hits:
        print("  %s" % m)
    if not ctrl:
        print("VERDICT: VOID (control failed)")
    elif not hits:
        print("VERDICT: NO-MODULE")
    else:
        print("VERDICT: MODULES %d" % len(hits))
    return 0


if __name__ == "__main__":
    sys.exit(main())
