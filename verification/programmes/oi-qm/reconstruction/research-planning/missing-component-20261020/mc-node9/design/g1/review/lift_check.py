from eng import *
from itertools import product
# signed real Pauli group: elements (s,k); automorphisms covering a fixed V-map that fix -1
G=[(s,k) for s in (1,-1) for k in range(16)]
def is_hom(phi):
    return all(phi[gmul(g,h)]==gmul(phi[g],phi[h]) for g in G for h in G) and len(set(phi.values()))==32
def all_lifts(base):  # base: table k->(s,k') of one lift; enumerate sign twists on generators XA,ZA,XB,ZB (idx 4,8,1,2)
    out=set()
    gens=[4,8,1,2]
    for sg in product((1,-1),repeat=4):
        img={}
        for k in range(16):
            # decompose k = XA^a ZA^b XB^c ZB^d with product order XA ZA XB ZB
            a,b=divmod(k,4); bits=[a in(1,3),a in(2,3),b in(1,3),b in(2,3)]
            acc=(1,0); pre=(1,0)
            for i,gi in enumerate(gens):
                if bits[i]:
                    pre=gmul(pre,(1,gi)); acc=gmul(acc,(sg[i]*base[gi][0],base[gi][1]))
            # pre = sign * PAULI[k]
            img[k]=(acc[0]*pre[0],acc[1])
        phi={(s,k):(s*img[k][0],img[k][1]) for s,k in G}
        if is_hom(phi): out.add(tuple(sorted(phi.items())))
    return out
for name,(M,c) in {'sA':(HA,2),'sB':(HB,2),'c':(CN,1)}.items():
    base=conj_table(M,c); L=all_lifts(base)
    mine=set()
    for p in range(16):
        t=conj_table(mm(PAULI[p],M),c); mine.add(tuple(sorted({(s,k):(s*t[k][0],t[k][1]) for s,k in G}.items())))
    print(name,': lifts of the V-map (trivial on C, brute force over generator signs):',len(L),
          '; distinct Ad(P.U), P in 16 Paulis:',len(mine),'; equal sets:',L==mine)
