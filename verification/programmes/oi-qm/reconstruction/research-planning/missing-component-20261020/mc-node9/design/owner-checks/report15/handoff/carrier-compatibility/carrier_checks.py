"""Exact bounded carrier/source/gate compatibility checks; stdout only."""
from collections import Counter
from itertools import product, combinations

DIRS=((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))
O=(0,0,0)
def require(x,msg):
    if not x: raise RuntimeError(msg)
def shift(s,L):
    out=set()
    for x in s:
        for d in DIRS:
            y=tuple((a+b)%L for a,b in zip(x,d))
            if y in out: out.remove(y)
            else: out.add(y)
    return out
def majority(bits):
    p=[bits[2*j]^bits[2*j+1] for j in range(3)]
    return (p[0]&p[1])^(p[1]&p[2])^(p[2]&p[0])
def majority_next(p,c,L):
    candidates=p|c|{tuple((a+b)%L for a,b in zip(x,d)) for x in c for d in DIRS}
    out=set()
    for x in candidates:
        bits=[int(tuple((a+b)%L for a,b in zip(x,d)) in c) for d in DIRS]
        if int(x in p)^majority(bits):out.add(x)
    return out

def box_checks():
    # Every outside-box site can have active neighbors in at most one opposite pair.
    count=0
    for axis in range(3):
        for pair in product((0,1),repeat=2):
            bits=[0]*6;bits[2*axis:2*axis+2]=pair
            require(majority(bits)==0,'outside-box force')
            count+=1
    L=9;box=set(product((0,1),repeat=3));runs=0
    for k in (1,2,3):
        for ones in combinations(sorted(box),k):
            for old_equal in (False,True):
                c=set(ones);p=set(c) if old_equal else set()
                for _ in range(8):
                    p,c=c,majority_next(p,c,L)
                    require(c<=box,'actual box exit')
                runs+=1
    require(count==12 and runs==184,'box control count')
    # The old radial statistic alone does not imply box membership.
    x=(L-1,0,0)
    require(x not in box and sum(min(v,L-v) for v in x)==1,'radial counterexample')
    print('Majority rule: 12 boundary truth cases and 184 runs x 8 ticks confirm box confinement')
    print('Radial-metric control: (-1,0,0) is outside the box but has L1 distance 1')

def repaired_step(p,c,L):
    sa,sb,sd=(shift(c[f],L) for f in ('A','B','D'))
    return {'A':sa^p['A'],'B':sb^p['B'],
            'D':sd^p['D']^shift(c['A']&c['B'],L)^(sa&sb)^(sa&p['B'])^(sb&p['A'])}
def to_raw(a,b,c):return {'A':set(a),'B':set(b),'D':set(c)^(set(a)&set(b))}
def record(c,x):return tuple(int(x in c[f]) for f in ('A','B','D'))
def run(a,b,c,K,L,receiver=O,source=None):
    p=to_raw(set(),set(),set());cur=to_raw(a,b,c)
    out=[]
    for _ in range(K):
        p,cur=cur,repaired_step(p,cur,L)
        out.append((record(cur,receiver),record(cur,source) if source is not None else None))
    return out
def ball(r):
    return {x for x in product(range(-r,r+1),repeat=3) if sum(map(abs,x))<=r}

def joint_carrier_check():
    K=3;L=8*K+1;q=(4*K,0,0);pa=(K,0,0);pb=(0,K,0)
    seen=Counter();source_by_payload={z:Counter() for z in product((0,1),repeat=2)}
    # All 3K source-frontier bits and two payload bits; other initial bits fixed zero.
    for bits in product((0,1),repeat=3*K+2):
        a,b=bits[:2];fields={f:set() for f in ('A','B','C')}
        if a: fields['A'].add(pa)
        if b: fields['B'].add(pb)
        for fi,f in enumerate(('A','B','C')):
            for t in range(1,K+1):
                if bits[2+fi*K+t-1]:fields[f].add((q[0]+t,0,0))
        require(not (fields['A']&fields['B']&{pa,pb}),'precomputed endpoint product')
        rec=run(fields['A'],fields['B'],fields['C'],K,L,source=q)
        rr=tuple(r for r,s in rec);ss=tuple(s for r,s in rec)
        require(rr==((0,0,0),)*(K-1)+((a,b,a*b),),'meeting detector record')
        source_by_payload[a,b][ss]+=1
        seen[(a,b),ss,rr]+=1
    require(len(seen)==4*8**K and set(seen.values())=={1},'joint record count')
    for row in source_by_payload.values():
        require(len(row)==8**K and set(row.values())=={1},'source law conditional on payload')
    # Geometry and exact readiness budget for several horizons.
    for k in range(1,9):
        bk,bm=ball(k),ball(k-1)
        require(len(bk)==(4*k**3+6*k*k+8*k+3)//3,'ball count')
        qk=(4*k,0,0);Lk=8*k+1
        receiver_cone={tuple(v%Lk for v in x) for x in bk}
        source_cone={tuple((a+b)%Lk for a,b in zip(qk,x)) for x in bk}
        require(not(receiver_cone&source_cone),'cone overlap')
        for a,b in product((0,1),repeat=2):
            r=run({(k,0,0)} if a else set(),{(0,k,0)} if b else set(),set(),k,Lk)
            require([v for v,s in r]==[(0,0,0)]*(k-1)+[(a,b,a*b)],'horizon carrier witness')
    require(3*(len(ball(K))+len(ball(K-1)))+4==268,'readiness exponent')
    # The earlier detector rule cannot combine the separated arrivals at this tick.
    p=to_raw(set(),set(),set());cur=to_raw({pa},{pb},set())
    for _ in range(K):
        n={f:shift(cur[f],L)^p[f] for f in ('A','B','D')}
        n['D'] ^= shift(cur['A']&cur['B'],L)
        p,cur=cur,n
    require(record(cur,O)==(1,1,0),'original-rule countercontrol')
    # Freeing one background bit masks the chosen carrier read completely.
    noisy=[]
    for message in (0,1):
        law=Counter()
        for mask in (0,1):
            aa=({pa} if message else set())|({(L-K,0,0)} if mask else set())
            rr=tuple(r for r,s in run(aa,{pb},set(),K,L))
            law[rr]+=1
        noisy.append(law)
    require(noisy[0]==noisy[1],'missing-ready-bit countercontrol')
    print('Shared ensemble, K=3: all 2048 frontier/payload assignments match the exact joint record law')
    print('Source records: 512 equally likely three-tick words for each of four payloads')
    print('Receiver: silent at ticks 1,2; (a,b,ab) at tick 3; payload TV=1 on raw receiver inputs')
    print('Horizons 1..8: separated pulses meet with exact product; readiness exponent at K=3 is 268')
    print('Original-rule control: terminal (1,1,0); one freed background bit masks the carrier, TV=0')

def mask_control():
    # A binary uniform source flip is a permutation, not a distinguishable encoding.
    laws=[]
    for message in (0,1):
        law=Counter()
        for a,b in product((0,1),repeat=2):
            raw_d=a*b
            encoded_a=a^message
            encoded_d=raw_d^(message*b)
            require(encoded_d==encoded_a*b,'clean-field preservation')
            law[encoded_a,b,encoded_d]+=1
        laws.append(law)
    require(laws[0]==laws[1],'uniform-flip control')
    print('Uniform-background flip: preserves readiness and the entire ensemble; message-record TV=0')

def main():
    box_checks();joint_carrier_check();mask_control()
    print('PASS: conditional bit-carrier/source/gate compatibility; not an angular-emission or QM verdict')
if __name__=='__main__':main()
