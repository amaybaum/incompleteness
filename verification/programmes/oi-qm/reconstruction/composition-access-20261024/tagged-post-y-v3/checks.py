#!/usr/bin/env python3
"""Exact tagged-interface controls; no native geometric splice is simulated."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json

PLANES=((0,0,0),(1,1,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1))
WEIGHTS={'X':(5,5,4,1,1,4),'Y':(5,5,2,3,3,2),'R':(7,7,2,1,1,2)}
INDEX={'X':0,'Y':1,'R':2,'Z':3}
DIR={'X':(F(1),F(0),F(0)),'Y':(F(0),F(1),F(0)),
     'R':(F(4,5),F(3,5),F(0)),'Z':(F(0),F(0),F(1))}

def need(ok,label):
    if not ok: raise RuntimeError(label)

def preparation(a,s):
    out={}
    for i,p in enumerate(PLANES):
        for z in (0,1):
            j=p+(z,)
            if j[INDEX[a]]==s:
                out[j]=F(1,6) if a=='Z' else F(WEIGHTS[a][i],20)
    return out

def encode(g,j):
    X,Y,R,Z=j
    return ((X,Y,1^g^(X&Y)^Y),(Y,Y,1^g),(R,Y,1^g^(R&Y)^Y),(0,0,Z))

def extract(raw):
    a,b,c,d=raw
    j=(a[0],b[0],c[0],d[2]); g=1^b[2]
    need(raw==encode(g,j),'valid global raw code')
    return j,g

def source_raw(x,y,u,v,z):
    q=(y,y,1^(x&y))
    def mix(q,a): A,B,D=q; return A^a,B,D^(a&B)
    return mix(q,u),q,mix(q,v),(0,0,z)

def bloch(mu):
    return (sum(mu.values(),F(0)),)+tuple(sum(w*(1-2*j[i]) for j,w in mu.items()) for i in (0,1,3))

def tv(a,b):
    return sum(abs(a.get(k,F(0))-b.get(k,F(0))) for k in a.keys()|b.keys())/2

def marginal(mu,fn):
    out=defaultdict(F)
    for j,w in mu.items(): out[fn(j)]+=w
    return dict(out)

def run():
    for a,s in product(INDEX,(0,1)):
        t,*b=bloch(preparation(a,s))
        need(t==1 and tuple(b)==tuple((1-2*s)*c for c in DIR[a]),'eight decoder preparations')
        need(sum(c*c for c in b)==1,'decoder positivity on generators')
    source_cases=0; positive_branches=0; posteriors=[]; raw_laws={}
    # Before averaging histories: all four conditional histories checked.
    for x,y in product((0,1),repeat=2):
        law=defaultdict(F); fail=F(0)
        for u,v,k,z in product((0,1),(0,1),range(8),(0,1)):
            source_cases+=1
            raw=source_raw(x,y,u,v,z)
            j,g=extract(raw)
            need(j==(y^u,y,y^v,z) and g==x*y,'fixed global extraction')
            if k < {(0,0):5,(1,0):3,(1,1):2,(0,1):0}[u,v]: law[raw]+=F(1,64)
            else: fail+=F(1,64)
        target={encode(x*y,j):F(5,16)*w for j,w in preparation('Y',y).items()}
        need(dict(law)==target and fail==F(11,16),'full raw source kernel and failure')
        raw_laws[x,y]={r:w*F(16,5) for r,w in law.items()}
        mu=preparation('Y',y)
        for axis in INDEX:
            port={'X':0,'Y':1,'R':2,'Z':3}[axis]
            records=marginal(mu,lambda j:encode(x*y,j)[port])
            for rec,prob in records.items():
                outcome=rec[2] if axis=='Z' else rec[0]
                expected_prob=(1+(1-2*outcome)*(1-2*y)*DIR[axis][1])/2
                need(prob==expected_prob,'whole-port quantum probability')
                # Every extra field is fixed by known x,y and selected outcome.
                template={'X':(outcome,y,1^(x*y)^((outcome^y)&y)),
                          'R':(outcome,y,1^(x*y)^((outcome^y)&y)),
                          'Y':(y,y,1^(x*y)), 'Z':(0,0,outcome)}[axis]
                need(rec==template,'whole-port metadata redundancy')
                post={j:w/prob for j,w in mu.items() if encode(x*y,j)[port]==rec}
                t,*b=bloch(post)
                determinant=(t*t-sum(v*v for v in b))/4
                posteriors.append({'x':x,'y':y,'axis':axis,'outcome':outcome,'mass':str(prob),'unchanged_determinant':str(determinant)})
                # Positive control: explicit independent resampling kernel.
                joint=defaultdict(F)
                for old,w in mu.items():
                    if encode(x*y,old)[port]!=rec: continue
                    for fresh,fw in preparation(axis,outcome).items():
                        joint[encode(x*y,fresh)]+=w*fw
                expected={encode(x*y,j):prob*w for j,w in preparation(axis,outcome).items()}
                need(dict(joint)==expected,'entire port-record/fresh-carrier law')
                dec=marginal(dict(joint),lambda r:extract(r)[0])
                need(bloch(dec)==(prob,)+tuple(prob*(1-2*outcome)*v for v in DIR[axis]),'quantum rank-one reset branch')
                positive_branches+=1
    need(tv(raw_laws[0,1],raw_laws[1,1])==1,'strict untagged raw obstruction retained')
    # The tag is observable if old x is omitted; it is redundant if x,y retained.
    need(extract(next(iter(raw_laws[0,1])))[1]==0 and extract(next(iter(raw_laws[1,1])))[1]==1,'hidden-history metadata detected')
    for row in posteriors:
        axis=row['axis']; y=row['y']; s=row['outcome']; d=F(row['unchanged_determinant'])
        want=F(0) if axis=='Y' else F(-1,64) if axis=='R' and s==y else F(-1,4)
        need(d==want,'conditional determinant countercontrol')
    correct=preparation('Y',0)
    wrong={(u,0,v,z):F(n,20) for u,v,n in [(0,0,5),(1,0,2),(1,1,3)] for z in (0,1)}
    need(tv(correct,wrong)==F(1,10),'wrong calibrated law rejected')
    need(marginal(correct,lambda j:j[0])==marginal(wrong,lambda j:j[0]),'X-blind calibration control')
    need(tv(marginal(correct,lambda j:j[2]),marginal(wrong,lambda j:j[2]))==F(1,10),'R calibration control')
    # Fresh law is required jointly; reusing first X-reset seed forces Xnew=x.
    need(all(y^(x^y)==x for x,y in product((0,1),repeat=2)),'old seed reuse control')
    return {'schema':'oi-tagged-post-y-contract-v1','source_seed_cases':source_cases,
            'fixed_decoder_preparations':8,'positive_record_reset_branches':positive_branches,
            'strict_raw_history_tv':'1','source_success':'5/16','source_terminal_failure':'11/16',
            'unchanged_carrier_posteriors':posteriors,'wrong_Y_calibration_tv':'1/10',
            'native_splice':'NOT_CONSTRUCTED','tagged_extension':'NOT_ADOPTED',
            'controls_passed':True,'verdict':'FIXED_TAGGED_COMPARISON_POSSIBLE; UNCHANGED_CARRIER_REUSE_FAILS'}

if __name__=='__main__': print(json.dumps(run(),indent=2,sort_keys=True))
