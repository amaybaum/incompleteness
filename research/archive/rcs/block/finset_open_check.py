"""Short identifiers in RelcSelectBlock.lean that are neither module-local, nor OIBridge (opened),
nor Mathlib root-level, nor local hypothesis names: candidates that would need `open Finset`."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_block as vb
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "mathlib_root_clash.py")).read().split("code = vb.strip_comments")[0])
code = vb.strip_comments(open(vb.MODULE, encoding="utf-8").read())
md = vb.decls(open(vb.MODULE, encoding="utf-8").read())
full = vb.ns_decls()
short = {}
for q in full:
    short.setdefault(q.split(".")[-1], []).append(q)
visible = ["OIBridge"] + ["OIBridge." + o for o in vb.OPENED]
# identifiers appearing as bare tokens (not after a dot, not qualified)
toks = set(re.findall(r"(?<![A-Za-z0-9_'.])([A-Za-z_][A-Za-z0-9_']*)(?![A-Za-z0-9_'.])", code))
finset = set()
for dp, _, fs in os.walk(os.path.join(ML, "Algebra/BigOperators")):
    for fn in fs:
        if fn.endswith(".lean"):
            finset |= set(re.findall(r"^\s*(?:@\[[^\]]*\]\s*)?(?:protected\s+)?(?:theorem|lemma)\s+([A-Za-z_][A-Za-z0-9_']*)", open(os.path.join(dp, fn), encoding="utf-8").read(), re.M))
hits = sorted(t for t in toks if t in finset and t not in root and t not in md
              and not any(q.rsplit(".", 1)[0] in visible for q in short.get(t, [])))
print("bare tokens that are BigOperators lemma names but not root/OIBridge-visible:", hits or "none")
