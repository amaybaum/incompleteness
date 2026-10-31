import re,ast,sys,os
src=open(sys.argv[1]).read(); root=sys.argv[2]
def grab(name):
    i=src.index('\n'+name+' = (')+1
    j=src.index('=',i)+1
    # parse balanced parens
    k=src.index('(',j); d=0
    for p in range(k,len(src)):
        if src[p]=='(': d+=1
        elif src[p]==')':
            d-=1
            if d==0: break
    return ast.literal_eval(src[k:p+1])
for name in ('_qsum','_ssum','_pqual'):
    s=grab(name); tot=0
    for rel in ('papers/Main.md','papers/Explainer.md','book/ch01-observation.md','book/ch19-open-problems.md','book/The-Incompleteness-of-Observation-FULL.md'):
        t=re.sub(r'\s+',' ',open(os.path.join(root,rel),encoding='utf-8').read()); c=t.count(s); tot+=c
        print(name,rel,c)
    print(name,'TOTAL',tot)
