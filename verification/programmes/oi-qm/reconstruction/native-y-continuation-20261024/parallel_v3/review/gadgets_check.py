"""Independent finite native extractor and clean-cone fanout audit."""
from functools import lru_cache
from itertools import product
from checks import H, hp, parity, need, R, S, P, T, steps, add, norm, distance, x, u, my, mr, ONE, ZERO, variable, xor, mul, px, ph, constant
from sidecar_check import native_eval

def scalar(src,old=None):
    old=old or {}
    @lru_cache(None)
    def at(t,v):
        if t==-1:return old.get(v,0)
        if t==0:return src.get(v,0)
        if min((distance(v,s) for s in src),default=10**6)>t and min((distance(v,s) for s in old),default=10**6)>t+1:return 0
        z=0
        for e in steps:z ^= at(t-1,add(v,e))
        return at(t-2,v)^H[z]
    return at

fixed={(0,1,-1):2,(1,1,-2):7,(8,2,0):2}
for q in range(8):
    src=dict(fixed);src[(0,0,0)]=q
    at=scalar(src)
    need([at(t,(3,2,0)) for t in range(6)]==[0]*5+[2*(q&1)],'five-tick arbitrary-A extractor')
need(all(distance(s,(3,2,0))==5 for s in list(fixed)+[(0,0,0)]),'extractor boundary')
need(native_eval(R+1,(1,0,2))==(ZERO,xor(ONE,u,my),my),'actual dirty neighbor')
src=dict(fixed);src[(0,0,0)]=4
need(scalar(src)(5,(3,2,0))==0,'clean countercontrol base')
need(scalar(src,{(1,0,0):2})(5,(3,2,0))==2,'dirty countercontrol flip')
print('AUX1: independent integer-coded 5tick recursion extracts A on all8 raw triples, with blank target prefix: PASS')
print('AUX2: actual translated previous-slice neighbor is (0,1 XOR u XOR mY,mY); supplied dirty old value flips gadget: PASS')

# Native two-ended mixer: sole overlap in receiver cones is the input origin.
for q,a,b in product(range(8),(0,1),(0,1)):
    src={(0,0,0):q,(24,0,0):a,(-24,0,0):b}
    at=scalar(src)
    for sign,seed in ((1,a),(-1,b)):
        v=(sign*12,0,0)
        A=q&1;B=(q>>1)&1;D=(q>>2)&1
        expected=(A^seed)+2*B+4*(D^(seed&B))
        need(at(12,v)==expected,'two-ended fanout exact')
        need(all(at(t,v)==0 for t in range(12)),'fanout prefixes blank')
print('RESET1: direct3D clean-cone fanout at L=12,all32 Q/a/b cases, both full outputs and prefixes: PASS')
for q,a in product(range(8),(0,1)):
    # General L multiple12 proof reduces to this local first-arrival identity.
    out=H[hp(q,11)^hp(a,11)]
    A=q&1;B=(q>>1)&1;D=(q>>2)&1
    need(out==(A^a)+2*B+4*(D^(a&B)),'general mixer algebra')
print('RESET2: first-arrival identity gives M_a(Q)=(A XOR a,B,D XOR aB) for every L=0mod12: PASS')
print('SCOPE: native conditional clean-cone gadgets accepted; embedding into actual populated q2 phase is NOT proved.')
