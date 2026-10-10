"""Compare theorem/def statements (header up to ':=') between two versions of a Lean file."""
import re, subprocess, sys
def stmts(text):
    out = {}
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        m = re.match(r"^(theorem|def|lemma)\s+([^\s({:]+)", lines[i])
        if m:
            name = m.group(2)
            buf = []
            j = i
            while j < len(lines):
                buf.append(lines[j])
                if ":=" in lines[j] or re.search(r"\bwhere\s*$", lines[j]):
                    break
                j += 1
            s = "\n".join(buf)
            s = s.split(":=")[0]
            out[name] = s
            i = j + 1
        else:
            i += 1
    return out
base = subprocess.run(["git", "show", sys.argv[1] + ":" + sys.argv[2]], capture_output=True, text=True, check=True).stdout
new = open(sys.argv[3]).read()
b, n = stmts(base), stmts(new)
changed = [k for k in b if k in n and b[k] != n[k]]
missing = [k for k in b if k not in n]
added = [k for k in n if k not in b]
print("base decls", len(b), "new decls", len(n))
print("changed statements:", changed)
print("missing:", missing)
print("added (%d):" % len(added), added)
prints = re.findall(r"^#print axioms OIBridge\.FourCopy\.(\S+)$", new, re.M)
print("prints", len(prints), "unprinted decls:", [k for k in n if k not in prints], "prints w/o decl:", [p for p in prints if p not in n])
print("duplicate prints:", sorted({p for p in prints if prints.count(p) > 1}))
