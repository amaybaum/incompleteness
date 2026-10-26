import re,os,json,sys
ROOT=sys.argv[1]
A=re.compile(r"'([A-Za-z0-9_.'₀₁₂]+?)' depends on axioms: \[([^\]]*)\]")
N=re.compile(r"'([A-Za-z0-9_.'₀₁₂]+?)' does not depend on any axioms")
out={}
for dp,dn,fn in os.walk(ROOT):
    if '/.git' in dp or '/.lake' in dp: continue
    for f in fn:
        p=os.path.join(dp,f)
        if f.endswith(('.lean','.py','.yml')): continue
        try: s=open(p,encoding='utf-8').read()
        except Exception: continue
        if 'axioms' not in s: continue
        s=s.replace('\\n','\n').replace("\\'","'")
        for m in A.finditer(s):
            ax=sorted(set(re.findall(r"[A-Za-z][A-Za-z0-9_.]*", m.group(2))))
            out.setdefault(m.group(1),[]).append(dict(axioms=ax,source=os.path.relpath(p,ROOT)))
        for m in N.finditer(s):
            out.setdefault(m.group(1),[]).append(dict(axioms=[],source=os.path.relpath(p,ROOT)))
# dedupe
for k in out:
    seen=[];r=[]
    for x in out[k]:
        key=(tuple(x['axioms']),x['source'])
        if key not in seen: seen.append(key); r.append(x)
    out[k]=r
json.dump(out,open(sys.argv[2],'w'),indent=0)
srcs={}
for k,v in out.items():
    for x in v: srcs[x['source']]=srcs.get(x['source'],0)+1
print(len(out)); print(srcs)
bad={k:v for k,v in out.items() if any(set(x['axioms'])-{'propext','Classical.choice','Quot.sound'} for x in v)}
print('nonstandard:',list(bad.items())[:10])
