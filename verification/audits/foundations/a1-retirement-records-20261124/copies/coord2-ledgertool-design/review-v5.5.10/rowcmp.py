import re,sys
def rows(p):
    d={};dup=[]
    for i,l in enumerate(open(p,encoding='utf-8')):
        m=re.match(r'^\|\s*([A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*)\s*\|',l)
        if m:
            k=m.group(1)
            if k in ('Id','Step','Hunk','#'): continue
            if k in d: dup.append(k); d.setdefault(k+'#dup',[]).append(l)
            else: d[k]=l
    return d,dup
a,da=rows(sys.argv[1]); b,db=rows(sys.argv[2])
print('rows base',len(a),'draft',len(b),'dups base',len(da),'dups draft',len(db), 'dupsame', sorted(da)==sorted(db))
print('removed',[k for k in a if k not in b])
print('added',[k for k in b if k not in a])
print('changed',[k for k in a if k in b and a[k]!=b[k]])
