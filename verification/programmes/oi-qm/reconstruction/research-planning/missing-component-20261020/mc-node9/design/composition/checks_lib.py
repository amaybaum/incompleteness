import numpy as np
from tri_fast import tt_vars
from builder import chains, realize, bits
def H(c): a,b,d=c; return (b,d,a^(b&d))
def machine_and(n):
    vs,full=tt_vars(n)
    def run(prog):
        c=(0,0,0)
        for cst,dd in prog:
            s=[full if b else 0 for b in bits(cst)]
            for j,v in dd.items():
                for k,bb in enumerate(bits(v)):
                    if bb: s[k]^=vs[j]
            c=H(tuple(x^y for x,y in zip(c,s)))
        return c
    p1,p2=chains(n); c1=run(p1); c2=run(p2)
    out=H(tuple(x^y for x,y in zip(c1,c2)))
    target=1<<((1<<n)-1)
    F1=full; F2=full
    for j in range((n+1)//2): F1&=vs[j]
    for j in range((n+1)//2,n): F2&=vs[j]
    return out[2]==target, c1==(0,F1,0), c2==(0,0,F2), len(p1)+1
