import re,sys
def stmts(p):
    s=open(p).read()
    out={}
    for m in re.finditer(r'^(?:@\[simp\] )?(?:noncomputable )?(theorem|def|structure) (\S+)(.*?)(:=|where)', s, re.S|re.M):
        out[m.group(2)]=' '.join((m.group(3)).split())
    return out
a,b=stmts(sys.argv[1]),stmts(sys.argv[2])
print(len(a),len(b),'same names' if a.keys()==b.keys() else 'NAMES DIFFER')
print('changed:',[k for k in a if a[k]!=b.get(k)])
