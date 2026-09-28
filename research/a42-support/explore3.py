from lib42 import *
# row permutations induced by stabilizer elements (non-transposing): element maps (i,j)->(i2,j2); rows map i->i2 consistently?
rowmaps=set(); trans=0
for p,s_ in elems:
    m={}
    ok=True
    for i in range(16):
        for j in range(16):
            i2,j2=divmod(p[i*16+j],16)
            m.setdefault(('r',i),set()).add(('r',i2)); 
    # determine whether rows map to rows
    rr=[set(divmod(p[i*16+j],16)[0] for j in range(16)) for i in range(16)]
    if all(len(x)==1 for x in rr): rowmaps.add(tuple(x.pop() for x in rr))
    else: trans+=1
print('elements mapping rows to rows', len(elems)-trans, 'transposing', trans, 'distinct row perms', len(rowmaps))
orb={0}
for rm in rowmaps: orb.add(rm[0])
print('orbit of row 0 under row-preserving elements', sorted(orb))
# sign distribution
import collections
print(collections.Counter(s_ for p,s_ in elems))
# check: stabilizer maps straight lines to straight lines and permutes census memberships (on A,B,C)
for E,nm in ((A38,'A'),(B38,'B'),(C38,'C')):
    ok=all(straight(stab_apply(e,E)) for e in elems[::37])
    print(nm,'images straight (sample)',ok)
