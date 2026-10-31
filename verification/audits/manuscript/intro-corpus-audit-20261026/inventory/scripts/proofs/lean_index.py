import re,glob,json,os,sys
ROOT=sys.argv[1]; OUT=sys.argv[2]
DECL=re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*(theorem|lemma|def|abbrev|structure|instance|class|inductive)\s+([^\s:({\[]+)")
NS=re.compile(r"^\s*(namespace|section|end)\b\s*([^\s-]*)")
PA=re.compile(r"^\s*#print\s+axioms\s+(\S+)")
files=sorted(glob.glob(os.path.join(ROOT,'verification/lean-mathlib/OIBridge/*.lean')))+[os.path.join(ROOT,'verification/lean-mathlib/OIBridge.lean')]+sorted(glob.glob(os.path.join(ROOT,'verification/lean/*.lean')))
decls=[]; prints=[]
for f in files:
    rel=os.path.relpath(f,ROOT)
    tree='OIBridge' if 'lean-mathlib' in rel else 'lean'
    mod=os.path.basename(f)[:-5]
    stack=[]; incomment=0
    for i,l in enumerate(open(f,encoding='utf-8'),1):
        # crude block-comment tracking
        s=l
        if incomment:
            if '-/' in s: incomment=0; s=s.split('-/',1)[1]
            else: continue
        if s.lstrip().startswith('/-') and '-/' not in s: incomment=1; continue
        m=NS.match(s)
        if m:
            k,n=m.groups()
            if k=='end':
                if stack: stack.pop()
            else: stack.append((k,n))
            continue
        m=DECL.match(s)
        if m:
            kind,name=m.groups()
            ns=[n for k,n in stack if k=='namespace' and n]
            full='.'.join(ns+[name]) if not name.startswith('_root_.') else name[7:]
            decls.append(dict(tree=tree,module=mod,path=rel,line=i,kind=kind,name=name,full=full,ns='.'.join(ns)))
            continue
        m=PA.match(s)
        if m:
            ns=[n for k,n in stack if k=='namespace' and n]
            prints.append(dict(path=rel,module=mod,line=i,target=m.group(1),ns='.'.join(ns)))
json.dump(dict(decls=decls,prints=prints),open(OUT,'w'))
from collections import Counter
print(len(decls),Counter((d['tree'],d['kind']) for d in decls),len(prints))
