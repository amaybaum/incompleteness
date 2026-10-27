import json,shutil,os,sys,collections
out=json.load(open('out.json',encoding='utf-8'))
REC={'O1A','O2a','O3b','O3x','O4a','O5a','O6A','O7a'}
sel={i:v for i,v in out.items() if v[0] in ('H','T','M') or v[0] in REC}
src='../snap'; dst='../sim'
if os.path.exists(dst): shutil.rmtree(dst)
shutil.copytree(src,dst)
FULLp=dst+'/book/The-Incompleteness-of-Observation-FULL.md'
F=open(FULLp,encoding='utf-8').read().split('\n')
files=collections.defaultdict(list)
for i,(g,f,n,full,o,nw) in sel.items(): files[f].append((n,full,o,nw,i))
for f,lst in files.items():
    L=open(dst+'/'+f,encoding='utf-8').read().split('\n')
    for n,full,o,nw,i in lst:
        assert L[n-1].count(o)==1,(i,f,n)
        L[n-1]=L[n-1].replace(o,nw)
        if full and full!='NONE':
            k=int(full)-1; assert F[k].count(o)==1,(i,'FULL'); F[k]=F[k].replace(o,nw)
    open(dst+'/'+f,'w',encoding='utf-8').write('\n'.join(L))
open(FULLp,'w',encoding='utf-8').write('\n'.join(F))
# mirror check: every non-empty chapter line present in FULL
Fs=set(F); miss=0
import glob
for f in glob.glob(dst+'/book/*.md'):
    b=os.path.basename(f)
    if b in ('README.md','The-Incompleteness-of-Observation-FULL.md'): continue
    for l in open(f,encoding='utf-8').read().split('\n'):
        if l.strip() and l not in Fs: miss+=1
print('applied',len(sel),'edits; chapter lines missing from FULL:',miss)
