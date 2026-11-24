import sys,re,collections
def tables(path):
    L=open(path,encoding='utf-8').read().split('\n')
    sec=None;out=[];i=0
    while i<len(L):
        l=L[i]
        if l.startswith('#'): sec=l.strip('# ').strip()
        if l.startswith('|') and i+1<len(L) and re.match(r'^\|[-:| ]+\|$',L[i+1]):
            hdr=l;rows=[];j=i+2
            while j<len(L) and L[j].startswith('|'):
                rows.append((j+1,L[j]));j+=1
            out.append((sec,hdr,i+1,rows));i=j;continue
        i+=1
    return out
def key(row):
    c=[x.strip() for x in row.strip().strip('|').split('|')]
    return c[0]
a=tables(sys.argv[1]);b=tables(sys.argv[2])
# map rows by (header, firstcell)
def idx(t):
    d=collections.OrderedDict()
    for sec,h,ln,rows in t:
        for n,r in rows:
            d.setdefault((h,key(r)),[]).append((sec,n,r))
    return d
A=idx(a);B=idx(b)
print('tables v5.5.9:',len(a),'rows',sum(len(t[3]) for t in a))
print('tables v6.0:',len(b),'rows',sum(len(t[3]) for t in b))
rem=[k for k in A if k not in B]; add=[k for k in B if k not in A]
mod=[k for k in A if k in B and [x[2] for x in A[k]]!=[x[2] for x in B[k]]]
same=[k for k in A if k in B and k not in mod]
print('unchanged',len(same),'removed',len(rem),'modified',len(mod),'added',len(add))
def show(tag,ks,D):
    for k in ks:
        for sec,n,r in D[k]: print(tag,n,'|',sec[:40],'|',r[:230])
show('REM',rem,A); show('ADD',add,B)
for k in mod:
    for sec,n,r in A[k]: print('MOD-OLD',n,'|',sec[:40],'|',r[:400])
    for sec,n,r in B[k]: print('MOD-NEW',n,'|',sec[:40],'|',r[:400])
