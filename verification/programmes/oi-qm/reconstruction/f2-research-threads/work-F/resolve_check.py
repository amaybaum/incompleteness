import re, sys, glob
draft, tree, design = sys.argv[1], sys.argv[2], sys.argv[3]
text = open(draft, encoding="utf-8").read()
# strip comments
body = re.sub(r"/-.*?-/", "", text, flags=re.S)
body = re.sub(r"--[^\n]*", "", body)
decl = {}
for f in glob.glob(tree + "/OIBridge/*.lean") + [design, draft]:
    s = open(f, encoding="utf-8").read()
    for m in re.finditer(r"^(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(theorem|def|structure|abbrev|lemma)\s+([^\s({:]+)", s, re.M):
        decl.setdefault(m.group(2), set()).add(f.split("/")[-1])
names = set(re.findall(r"(?<![\w.'])([A-Za-z_][\w']*(?:\.[A-Za-z_][\w']*)*)", body))
lean_kw = set("""import namespace open variable section end theorem def structure where fun by have exact
rw rwa at intro calc obtain example show refine Prop Type Set Fin ℝ ℕ x y z a b e f g h r N d ω hx hy he hp
hT hE hG hK hN hP1 hV4 hd hcone hcov hgh hhg hgΩ hhΩ hgz hC hg hnat eC eT eg NC NT T G Ω avail Ω
omega norm_num simp only noncomputable LinearMap.comp_apply hsub hω""".split())
used = sorted(n for n in names if n not in lean_kw)
for n in used:
    base = n.split(".")[-1]
    hit = decl.get(n) or decl.get(base)
    print(("OK   " if hit else "??   ") + n + ("  <- " + ",".join(sorted(hit)) if hit else ""))
