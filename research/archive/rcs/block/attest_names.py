"""Which opened-namespace short names used by RelcSelectBlock.lean are already used, via `open`,
in a landed module outside their own namespace (evidence they resolve without ambiguity)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_block as vb
full = vb.ns_decls()
short = {}
for q in full:
    short.setdefault(q.split(".")[-1], []).append(q)
code = vb.strip_comments(open(vb.MODULE, encoding="utf-8").read())
md = vb.decls(open(vb.MODULE, encoding="utf-8").read())
toks = sorted(set(vb.IDENT.findall(code)) - set(md))
visible = ["OIBridge." + o for o in vb.OPENED]
used = {}
for t in toks:
    c = [q for q in short.get(t, []) if q.rsplit(".", 1)[0] in visible]
    if c:
        used[t] = c[0]
# landed modules that open CompositeDimension (not inside it)
openers = []
for fn in sorted(os.listdir(vb.ROOT)):
    if fn.endswith(".lean") and fn != "CompositeDimension.lean":
        s = open(os.path.join(vb.ROOT, fn), encoding="utf-8").read()
        if re.search(r"^open .*\bCompositeDimension\b", s, re.M):
            openers.append((fn, set(vb.IDENT.findall(vb.strip_comments(s)))))
print("modules opening CompositeDimension:", [f for f, _ in openers])
unattested = []
for t, q in sorted(used.items()):
    att = [f for f, ids in openers if t in ids]
    if not att and not q.startswith("OIBridge.CompositeDimension") is False:
        pass
    if not att:
        unattested.append((t, q))
print(f"opened-namespace names used: {len(used)}; attested via open elsewhere: {len(used)-len(unattested)}")
print("unattested:", unattested)
