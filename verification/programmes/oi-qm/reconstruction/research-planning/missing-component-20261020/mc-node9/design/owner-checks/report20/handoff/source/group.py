"""The register group: steps g_v = H o T_v on F2^3 (state s = 4a+2b+d). Words, leaf blocks, Barrington programs."""
import itertools
def Hs(s):
    a,b,d=(s>>2)&1,(s>>1)&1,s&1
    return (b<<2)|(d<<1)|(a^(b&d))
GEN={v:tuple(Hs(s^v) for s in range(8)) for v in range(8)}
I=tuple(range(8))
def comp(p,q): return tuple(p[q[i]] for i in range(8))   # p after q
def inv(p):
    r=[0]*8
    for i,x in enumerate(p): r[x]=i
    return tuple(r)
def layers(maxm):
    """layer[m]: dict element -> (prev element, v) with element = GEN[v] o prev."""
    L=[{I:None}]
    for m in range(1,maxm+1):
        nxt={}
        for g in L[-1]:
            for v,h in GEN.items():
                e=comp(h,g)
                if e not in nxt: nxt[e]=(g,v)
        L.append(nxt)
    return L
LAY=layers(10)
def word(e,m):
    """translations (v_1..v_m), step 1 applied first, with GEN[v_m] o ... o GEN[v_1] = e."""
    w=[]
    for k in range(m,0,-1):
        prev,v=LAY[k][e]; w.append(v); e=prev
    assert e==I
    return w[::-1]
def block_len(g):
    for m in (6,8,10):
        if g in LAY[m] and I in LAY[m]: return m
    return None
def cycle(points):
    p=list(range(8))
    for i,a in enumerate(points): p[a]=points[(i+1)%len(points)]
    return tuple(p)
def is5(p):
    moved=[i for i in range(8) if p[i]!=i]
    return len(moved)==5 and all(p[i]!=i for i in moved) and (lambda: (lambda c: c==5)(cyclen(p,moved[0])))()
def cyclen(p,i):
    j=p[i]; L=1
    while j!=i: j=p[j]; L+=1
    return L
