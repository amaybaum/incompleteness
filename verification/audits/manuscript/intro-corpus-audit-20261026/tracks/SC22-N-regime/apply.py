import sys, os, runpy
tree = sys.argv[1]
src = open(sys.argv[2], encoding="utf-8").read()
ns = {}
code = src.split("full_path =")[0]
exec(compile(code.replace("wt = sys.argv[1]; outdir = sys.argv[2]", ""), "p", "exec"), ns)
E = ns["E"]
fullp = os.path.join(tree, "book/The-Incompleteness-of-Observation-FULL.md")
for eid, f, old, new, disp in E:
    for p in (os.path.join(tree, f), fullp):
        t = open(p, encoding="utf-8").read(); assert t.count(old) == 1, (eid, p)
        open(p, "w", encoding="utf-8").write(t.replace(old, new))
print("applied", len(E))
