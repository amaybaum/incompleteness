import re,sys
L=open(sys.argv[1],encoding='utf-8').read().split('\n')
pat=re.compile(r'SEALED|sealed head|ARCHIVE MODE|archive mode|chronolog|CHRONOLOG|mandated execution base|execution base|seal constant|pin-only|ancestry')
i=0;out=[]
while i<len(L):
    if L[i].lstrip().startswith('#'):
        j=i
        while j<len(L) and L[j].lstrip().startswith('#'): j+=1
        para=L[i:j]
        if any(pat.search(x) for x in para):
            nxt=L[j] if j<len(L) else ''
            out.append((i+1,j-i,nxt.strip()[:50],para[0].strip()[:90]))
        i=j
    else: i+=1
for o in out: print(o)
print(len(out))
