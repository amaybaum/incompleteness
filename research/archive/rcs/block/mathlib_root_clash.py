"""Root-level Mathlib v4.33.0 declarations whose name equals a short name that RelcSelectBlock.lean
resolves through `open` (an equal root name would make the reference ambiguous)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_block as vb
ML = "/tmp/claude-0/-home-user-incompleteness/727ddb71-72ba-5388-a9a1-1413a0433ac0/scratchpad/ml-v433-src/m/Mathlib"
HEAD = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(?:private\s+|protected\s+)?(?:nonrec\s+)?"
                  r"(theorem|lemma|def|abbrev|structure|instance|class|inductive|opaque)\s+([^\s(:{\[]+)")
root = {}
for dp, _, fs in os.walk(ML):
    for fn in fs:
        if not fn.endswith(".lean"):
            continue
        p = os.path.join(dp, fn)
        stack = []
        try:
            txt = vb.strip_comments(open(p, encoding="utf-8").read())
        except Exception:
            continue
        for l in txt.split("\n"):
            m = re.match(r"^\s*namespace\s+(\S+)", l)
            if m: stack.append(("ns", m.group(1))); continue
            m = re.match(r"^\s*(?:noncomputable\s+)?section\b\s*(\S*)", l)
            if m: stack.append(("sec", m.group(1))); continue
            m = re.match(r"^\s*end\b\s*(\S*)\s*$", l)
            if m and stack: stack.pop(); continue
            m = HEAD.match(l)
            if m:
                n = m.group(2)
                ns = [x for k, x in stack if k == "ns"]
                if n.startswith("_root_."):
                    q = n[len("_root_."):]
                elif ns:
                    q = ".".join(ns) + "." + n
                else:
                    q = n
                if "." not in q:
                    root.setdefault(q, []).append(os.path.relpath(p, ML))
code = vb.strip_comments(open(vb.MODULE, encoding="utf-8").read())
md = vb.decls(open(vb.MODULE, encoding="utf-8").read())
full = vb.ns_decls()
short = {}
for q in full:
    short.setdefault(q.split(".")[-1], []).append(q)
visible = ["OIBridge." + o for o in vb.OPENED]
toks = sorted(t for t in set(vb.IDENT.findall(code)) - set(md)
              if any(q.rsplit(".", 1)[0] in visible for q in short.get(t, [])))
print(f"Mathlib root-level declarations parsed: {len(root)}")
print(f"opened-namespace names used by the module: {len(toks)}")
cl = [(t, root[t][:3]) for t in toks if t in root]
print("root-level clashes:", cl if cl else "none")
# own new names vs Mathlib root
cl2 = [(t, root[t][:3]) for t in md if t in root]
print("module's own names equal to a Mathlib root name:", cl2 if cl2 else "none")
# control: a known root-level Mathlib name must be found
for ctl in ("mul_comm", "sq_nonneg", "two_ne_zero"):
    print(f"control {ctl}: {'found' if ctl in root else 'MISSING'}")
