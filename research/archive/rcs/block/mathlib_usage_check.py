"""Every identifier in the NEW declarations of RelcSelectBlock.lean that is not an OIBridge / local
name must already occur in some landed OIBridge module (so its Mathlib v4.33.0 name is exercised)."""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verify_block as vb
txt = open(vb.MODULE, encoding="utf-8").read()
md = vb.decls(txt)
new = [k for k in md if k not in set(vb.MAP.values())]
code = vb.strip_comments("\n".join("\n".join(md[k]) for k in new))
toks = set(re.findall(r"(?<![A-Za-z0-9_'.])([A-Za-z_][A-Za-z0-9_'.]*[A-Za-z0-9_'])", code))
full = vb.ns_decls()
short = {q.split(".")[-1] for q in full}
corpus = ""
for fn in os.listdir(vb.ROOT):
    if fn.endswith(".lean"):
        corpus += open(os.path.join(vb.ROOT, fn), encoding="utf-8").read()
keywords = {"theorem","have","by","fun","at","with","exact","rw","rwa","intro","show","change","apply",
            "refine","rcases","set","let","simp","only","using","linarith","ring","norm_num","funext",
            "calc","simpa","Type","Prop","structure","where","def","end","namespace","open","variable"}
unseen = []
for t in sorted(toks):
    base = t.split(".")[-1]
    if t in md or t in keywords or base in short or t in vb.EXTERNAL_OK:
        continue
    if re.fullmatch(r"h\w*|[a-zA-Zα-ω]'*|[a-z]\d*|hz'*|e|this|hk|hlz|hT|hX|hL|hs|hu\w*|hw\w*", t):
        continue
    if not re.search(r"(?<![A-Za-z0-9_'])" + re.escape(t) + r"(?![A-Za-z0-9_'])", corpus):
        unseen.append(t)
print("external names in new declarations not used anywhere in landed OIBridge:", unseen or "none")
