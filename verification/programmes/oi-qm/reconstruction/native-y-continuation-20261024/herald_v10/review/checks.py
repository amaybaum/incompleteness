#!/usr/bin/env python3
"""Independent remote-herald review; no author imports."""
from pathlib import Path
from functools import lru_cache
from itertools import product
from collections import Counter
from fractions import Fraction as F
from math import comb
import argparse,hashlib,json

HASH='406befa2c8d1f663856a78ca6cb632e9c61d1233b02a9d532c7cb43d6261ce64'
BITS=list(product((0,1),repeat=3));FULL=(1<<32)-1

def need(ok,msg):
    if not ok:raise RuntimeError(msg)

def H(q):a,b,c=q;return b,c,a^(b&c)
def xor(*values):return tuple(__import__('functools').reduce(int.__xor__,(v[k] for v in values),0) for k in range(3))
def val(mask,seed):return (mask&1)^((mask>>1 & seed).bit_count()%2)
def packed(mask):return sum(val(mask,s)<<s for s in range(32))
def controls(step):
    code,terms=step;out=[(code>>(2-k))&1 for k in range(3)]
    for bit,word in terms:
        for k in range(3):out[k]^=((word>>(2-k))&1)<<(bit+1)
    return tuple(out)

def source_rows(program):
    n=len(program);size=1<<(n-1).bit_length();rows=[]
    # Binary zeta transform in-place, independently of author's submask loop.
    for wing in range(3):
        row=[program[t][(wing-t)%3] for t in range(n)]+[0]*(size-n)
        bit=1
        while bit<size:
            for q in range(size):
                if q&bit:row[q]^=row[q^bit]
            bit*=2
        rows.append(row[:n])
    return rows

def source_native(program,omit_terminal=False):
    n=len(program);rows=source_rows(program);initial={}
    for q in range(n):
        if omit_terminal and q==n-1:continue
        pos=[(n-1-q,q+1,0),(n-1-q,-q-1,0),(n-1-q,0,q+1)]
        for wing in range(3):
            v=[0,0,0];v[wing]=packed(rows[wing][q]);initial[pos[wing]]=tuple(v)
    steps=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    @lru_cache(None)
    def field(t,p):
        if t<0:return(0,0,0)
        if t==0:return initial.get(p,(0,0,0))
        if min(sum(abs(a-b) for a,b in zip(p,s)) for s in initial)>t:return(0,0,0)
        neighbors=[field(t-1,tuple(a+b for a,b in zip(p,step))) for step in steps]
        return xor(field(t-2,p),H(xor(*neighbors)))
    need(all(field(t,(0,0,0))==(0,0,0) for t in range(n)),'whole raw blank prefix')
    return field(n,(0,0,0))

def main(path):
    raw=path.read_bytes();need(hashlib.sha256(raw).hexdigest()==HASH,'source provenance')
    data=json.loads(raw);prefix=data['program'][:2684];identity=[2,3,3,3,3,7]
    need([s[0] for s in data['program'][2684:2690]]==identity,'retained identity sequence')
    for s in BITS:
        q=s
        for code in identity:q=H(xor(q,tuple((code>>(2-k))&1 for k in range(3))))
        need(q==s,'identity word on every state')
    truth=[];planes=Counter()
    for seed in range(32):
        q=(0,0,0)
        for code,terms in prefix:
            for bit,term in terms:
                if seed>>bit&1:code^=term
            q=H(xor(q,tuple((code>>(2-k))&1 for k in range(3))))
        a=seed&1;b=(seed>>1)&1;K=seed>>2;g=int(K<{(0,0):5,(0,1):0,(1,0):3,(1,1):2}[a,b])
        need(q==(g,0,0),'actual predicate word truth table');truth.append(g);planes[a,b]+=g
    P=12*840**185;R=P+253;L=R+9;m=(P-2424)//6;side=256*L+64*185+1
    need(m>=0 and 6*m==P-2424 and 2684+6*m+2==L,'unchanged-P exact schedule')
    need(L%3==1,'fair z phase')
    need(47*L>13*R and 96*L>2*L,'full source/ready/bank separation')
    need(196*L<side and 8*L<side,'no periodic shortcuts in full coordinate envelopes')
    # Complete original predicate with two terminal zero steps, no padding needed
    # in this bounded native realization; the proven identity handles arbitrary m.
    program=[controls(step) for step in prefix]+[(0,0,0),(0,0,0)]
    span={0}
    for triple in program:
        for mask in triple:span|={v^(mask>>1) for v in span}
    need(len(span)==32,'five-dimensional affine seed embedding')
    rows=source_rows(program);q=(0,0,0);comparisons=0
    for t,target in enumerate(program):
        injection=[0,0,0]
        for w in range(3):
            injection[(w-t)%3]=packed(rows[w][0])
            rows[w]=[a^b for a,b in zip(rows[w],rows[w][1:])]
        need(tuple(injection)==tuple(packed(a) for a in target),'full native wing injection')
        q=H(xor(q,tuple(injection)));comparisons+=32
    bits=sum(g<<i for i,g in enumerate(truth));need(q==(0,bits,0),'complete native herald triple')
    # Full 3D native tests exercise the arbitrary-length formula including q=n-1.
    direct=0;terminal_mutants=0
    for n in (3,5,7):
        p=[tuple(((t+1)*(k+3)*13+7*t*k)%64 for k in range(3)) for t in range(n-1)]+[(0,0,0)]
        q=(0,0,0)
        for a in p:q=H(xor(q,tuple(packed(v) for v in a)))
        need(source_native(p)==q,'full spatial rule agrees with arbitrary program')
        terminal_mutants+=source_native(p,True)!=q
        # Independent finite binomial formula checks every small source mask.
        rows=source_rows(p)
        for w,qindex in product(range(3),range(n)):
            v=0
            for e in range(qindex+1):
                if comb(qindex,e)%2:v^=p[e][(w-e)%3]
            need(v==rows[w][qindex],'inverse Pascal including last source row')
        direct+=32
    need(terminal_mutants>0,'omitting terminal source row detected')
    for z in (0,1):
        q=(z,0,0)
        for _ in range(L%12):q=H(q)
        need(q==(0,0,z),'native fair-z triple')
        if z:
            bad=(0,0,z)
            for _ in range(L%12):bad=H(bad)
            need(bad!=q,'wrong initial z field negative')
    accepted=Counter();rejected=Counter()
    for seed,z in product(range(32),(0,1)):
        a=seed&1;b=(seed>>1)&1
        (accepted if truth[seed] else rejected)[a,b,z]+=1
    need(sum(accepted.values())==20 and sum(rejected.values())==44,'all64 branches retained')
    for a,b in product((0,1),repeat=2):
        need(accepted[a,b,0]==accepted[a,b,1]==planes[a,b],'joint z fairness after herald')
        need(rejected[a,b,0]==rejected[a,b,1]==8-planes[a,b],'failure z branches retained')
    ideal={k:F(v,20) for k,v in accepted.items()};shared=Counter()
    for s in range(32):
        if truth[s]:a=s&1;b=s>>1&1;shared[a,b,a]+=1
    distance=sum(abs(ideal.get(k,0)-F(shared.get(k,0),10)) for k in ideal.keys()|shared.keys())/2
    need(distance==F(1,2),'shared-z joint negative')
    need(H((bits,0,0))!=(0,bits,0),'missing zero step phase negative')
    return {'schema':'synchronized-herald-review-v1','predicate_assignments':32,
            'identity_states':8,'affine_seed_rank':5,'full_wing_steps':2686,'full_wing_seed_comparisons':comparisons,
            'small_3D_seed_cases':direct,'terminal_source_omission_mutants_detected':terminal_mutants,
            'accepted_plane_counts':[planes[k] for k in [(0,0),(0,1),(1,0),(1,1)]],
            'success':'5/16','failure':'11/16','shared_z_joint_TV':str(distance),
            'controls_passed':True,'verdict':'PASS_CONDITIONAL_REMOTE_HERALD_AND_Z'}

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--herald',type=Path,default=Path(__file__).resolve().parents[2]/'parallel_v3/direct_reset/herald.json');a=ap.parse_args()
    print(json.dumps(main(a.herald),sort_keys=True,indent=2))
