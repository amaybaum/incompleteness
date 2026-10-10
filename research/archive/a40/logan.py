import re, collections, sys
t=open(sys.argv[1]).read().replace('\\n','\n')
src=open(sys.argv[2],encoding='utf-8').read().split('\n')
def thm(n):
    for i in range(n-1,-1,-1):
        if src[i].startswith('theorem '): return src[i].split()[1]
print('log starts', t[40:100])
errs=[(int(m.group(1)),int(m.group(2)),m.group(3)) for m in re.finditer(r'error: OIBridge/DitaTorusLocus.lean:(\d+):(\d+): ([^\n]*)',t)]
print('errors in window', len(errs))
c=collections.Counter()
for n,col,e in errs: c[(thm(n), e[:80])]+=1
for k,v in sorted(c.items()): print(v, k)
sor=sorted(set(re.findall(r"'OIBridge\.DitaTorusLocus\.([^']+)' depends on axioms: \[[^\]]*sorryAx",t)))
ok=sorted(set(re.findall(r"'OIBridge\.DitaTorusLocus\.([^']+)' depends on axioms: \[propext, Classical.choice, Quot.sound\]",t)))
print('sorry', len(sor), sor); print('clean', len(ok), ok)
