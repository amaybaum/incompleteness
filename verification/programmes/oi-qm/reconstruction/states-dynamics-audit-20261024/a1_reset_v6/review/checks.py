"""Independent exact review of the pushed fixed-vector reset-resource audit.
No author engine imports. Response written in the primary reference bits.
"""
from collections import defaultdict,Counter
from fractions import Fraction as F
from itertools import product,permutations
from math import isqrt
import json
import hashlib
from pathlib import Path
from argparse import ArgumentParser

C=Counter()
def require(ok,label):
    C[label]+=1
    if not ok:raise RuntimeError(label)
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def sgn(x):return 1 if x>=0 else -1
def neg(a):return tuple(-x for x in a)
X=(F(1),F(0),F(0));Z=(F(0),F(0),F(1))


def primary_prepare(pair,n):
    idx=0 if dot(pair[0],n)**2>=dot(pair[1],n)**2 else 1
    refbit=sgn(dot(pair[idx],n)*dot(pair[idx],Z))
    return idx,refbit

def primary_step(pair,idx,refbit,a):
    # Eq17 directly, keeping its fixed Z reference coordinate.
    out=refbit*sgn(dot(pair[idx],Z)*dot(pair[idx],a))
    nxt=0 if dot(pair[0],a)**2>=dot(pair[1],a)**2 else 1
    rb=refbit*sgn(dot(pair[idx],Z)*dot(pair[idx],a)*dot(pair[nxt],Z)*dot(pair[nxt],a))
    return out,nxt,rb


def cells():
    # Different strict interior unit vectors than the author; all S3 images
    # and pair interchange classified independently by sign differences.
    p=(F(2,3),F(2,3),F(1,3));q=(F(6,7),F(3,7),F(2,7))
    classes={}
    for perm in permutations(range(3)):
        a=tuple(p[k] for k in perm);b=tuple(q[k] for k in perm)
        for pair in ((a,b),(b,a)):
            dif=tuple(pair[0][k]**2-pair[1][k]**2 for k in range(3))
            require(sum(dif)==0 and all(dif),'strict zero-sum difference witness')
            pattern=tuple(sgn(x) for x in dif)
            classes.setdefault(pattern,pair)
    require(len(classes)==6,'all six geometric rank-sign classes')
    # S3 and exchange are transitive on these six sign patterns. Reflection
    # symmetry makes four independent X/Z signs uniform conditional on rank.
    result=[]
    for pattern,pair in sorted(classes.items()):
        for signs in product((-1,1),repeat=4):
            u=(pair[0][0]*signs[0],pair[0][1],pair[0][2]*signs[1])
            v=(pair[1][0]*signs[2],pair[1][1],pair[1][2]*signs[3])
            require(dot(u,u)==dot(v,v)==1,'rational spherical interior witnesses')
            result.append(((u,v),F(1,96)))
    require(sum(w for p,w in result)==1,'complete exact cell mass')
    return result


def record_law(source,h):
    law=defaultdict(F)
    for pair,w in source:
        idx,bit=primary_prepare(pair,Z);rec=[]
        for t in range(h):
            k,idx,bit=primary_step(pair,idx,bit,X if t%2==0 else Z);rec.append(k)
        law[tuple(rec)]+=w
    return dict(law)

def matrix_product(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def projector(a,s):
    x,y,z=a;require(y==0,'independent real XZ projector scope')
    return (((1+s*z)/2,s*x/2),(s*x/2,(1-s*z)/2))
def quantum_tree(n,axes):
    a={():projector(n,1)}
    for axis in axes:
        nxt={}
        for rec,rho in a.items():
            for s in (-1,1):
                p=projector(axis,s);nxt[rec+(s,)]=matrix_product(matrix_product(p,rho),p)
        a=nxt
    return {k:v[0][0]+v[1][1] for k,v in a.items()}
def distance(a,b):return sum((abs(a.get(k,F(0))-b.get(k,F(0))) for k in a.keys()|b.keys()),F(0))/2


def selected_source_integral(n,a):
    # Condition on n's winner. |n.u| is uniform before selection; the winning
    # absolute projection has density2v. Folding gives cosine density.
    # Rotate the XZ plane so n=(1,0). Hemisphere intersection has endpoint
    # sin(theta)=-(n dot a), and primitive sin(theta)/2. Reflection handles
    # either sign of the perpendicular component without angle evaluation.
    c=n[0]*a[0]+n[2]*a[2]
    d=n[0]*a[2]-n[2]*a[0]
    require(c*c+d*d==1,'exact rotated hemisphere endpoints')
    upper=F(1);lower=-c
    return (upper-lower)/2


def total_lift(idx,orient,g,c,m,j):
    # Independent formulation as a table of signs on the selected pair.
    k=orient*m[idx]
    nr=g^j
    return nr,k*m[nr],idx,c^int(k<0)


def pinned_inputs(author_root=None):
    here=Path(__file__).resolve().parent
    record=json.loads((here/'INPUT-HASHES.json').read_text())
    if author_root is None:
        options=[here.parent,here.parent/'a1_reset_v6']
        author_root=next((p for p in options if (p/'PLAN.md').is_file()),None)
    else:author_root=Path(author_root)
    require(author_root is not None,'author package present')
    for name,pin in record['files'].items():
        b=(author_root/name).read_bytes()
        require(hashlib.sha256(b).hexdigest()==pin['sha256'],'immutable author SHA256')
        require(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()==pin['git_blob_sha1'],'immutable pushed author Git blob')
    return record['author_commit']


def main(author_root=None):
    author=pinned_inputs(author_root)
    source=cells();law2=record_law(source,2)
    require(law2=={(-1,-1):F(1,6),(-1,1):F(1,3),(1,-1):F(1,6),(1,1):F(1,3)},'independent XZ complete law')
    q2=quantum_tree(Z,(X,Z));require(set(q2.values())=={F(1,4)},'quantum orthogonal records')
    require(distance(law2,q2)==F(1,6),'XZ discrepancy')
    agree=F(0)
    for pair,w in source:
        a=primary_prepare(pair,X)[0];b=primary_prepare(pair,Z)[0]
        if a==b:agree+=w
    require(agree==F(1,3),'same winning vector event')
    histories=[]
    for h in (1,2,3,4,5,6,8,10,12):
        p=record_law(source,h);q=quantum_tree(Z,tuple(X if i%2==0 else Z for i in range(h)))
        require(sum(p.values())==sum(q.values())==1,'complete finite record mass')
        e=distance(p,q)
        require(e==(F(0) if h==1 else F(1,6) if h==2 else 1-F(4,2**h)),'four-record recurrence versus matrix reference')
        if h>=2:
            require(sorted(p.values())==[F(1,6),F(1,6),F(1,3),F(1,3)],'four exact persistent path masses')
        histories.append({'h':h,'support':len(p),'TV':str(e)})

    # Every possible projection-sign/winner configuration, including abstract
    # tie-convention cases, independently proves the proposed total bit lift.
    lift_cases=0
    for m in product((-1,1),repeat=2):
        for j in (0,1):
            outputs={}
            ready={}
            for state in product((0,1),(-1,1),(0,1),(0,1)):
                i,t,g,c=state;out=total_lift(i,t,g,c,m,j)
                require(out not in outputs,'global lifted map injective')
                outputs[out]=state;lift_cases+=1
                if g==c==0:
                    k=t*m[i]
                    require(out==(j,k*m[j],i,int(k<0)),'ready lifted logical action')
                    ready[(k,j,k*m[j])]=1
            require(len(outputs)==16 and len(ready)==2,'total permutation and literal logical multiplicity')
            for out,state in outputs.items():
                nr,nt,ng,nc=out;k=nt*m[nr]
                restored=(ng,k*m[ng],nr^j,nc^int(k<0))
                require(restored==state,'independent lifted inverse')

    # Rotation invariance of the orientation coordinate, checked using only
    # the reference-basis sign-crossing rule read from the primary source.
    R=((F(5,13),F(0),F(12,13)),(F(0),F(1),F(0)),(-F(12,13),F(0),F(5,13)))
    RT=tuple(zip(*R));rotations=0
    def move(pair,idx,bit,A):
        out=tuple(tuple(dot(row,v) for row in A) for v in pair)
        rb=bit*sgn(dot(pair[idx],Z)*dot(out[idx],Z))
        return out,idx,rb
    for pair,w in source:
        for idx,bit in product((0,1),(-1,1)):
            p,j,b=move(pair,idx,bit,R);back,i,c=move(p,j,b,RT)
            require(back==pair and i==idx and c==bit,'rational rotation inverse')
            require(bit*sgn(dot(pair[idx],Z))==b*sgn(dot(p[j],Z)),'orientation coordinate preserved')
            rotations+=1

    circle=((F(1),F(0)),(F(5,13),F(12,13)),(F(12,13),F(5,13)),(F(0),F(1)),
            (-F(5,13),F(12,13)),(-F(12,13),F(5,13)),(-F(1),F(0)),
            (-F(5,13),-F(12,13)),(-F(12,13),-F(5,13)),(F(0),-F(1)),
            (F(5,13),-F(12,13)),(F(12,13),-F(5,13)))
    directions=tuple((x,F(0),z) for x,z in circle)
    integral_cases=0
    for n,a in product(directions,repeat=2):
        p=selected_source_integral(n,a)
        require(p==quantum_tree(n,(a,))[(1,)],'folded winner hemisphere versus independent matrix')
        integral_cases+=1
    repair_cases=0;repair_leaves=0;zero=0
    for n in directions[:4]:
        for policy in range(4):
            branches=[((),F(1),n,projector(n,1))]
            for depth in range(4):
                nxt=[]
                for rec,p,pole,rho in branches:
                    axis=directions[(2*policy+depth+sum(i<0 for i in rec))%len(directions)]
                    for s in (-1,1):
                        v=p*selected_source_integral(pole,axis if s>0 else neg(axis))
                        P=projector(axis,s);quant=matrix_product(matrix_product(P,rho),P)
                        newpole=tuple(s*x for x in axis)
                        require(quant[0][0]+quant[1][1]==v,'renewed adaptive branch probability')
                        expected=tuple(tuple(v*x for x in row) for row in projector(newpole,1))
                        require(expected==quant,'renewed adaptive outgoing operator')
                        nxt.append((rec+(s,),v,newpole,quant));repair_cases+=1
                branches=nxt
            repair_leaves+=len(branches);zero+=sum(p==0 for rec,p,pole,rho in branches)

    # Uniform sphere azimuth: exact equal octants, with different rational
    # interior witnesses than author. No winning-vector selection is used.
    octants=((F(12,13),F(5,13)),(F(5,13),F(12,13)),(-F(5,13),F(12,13)),
      (-F(12,13),F(5,13)),(-F(12,13),-F(5,13)),(-F(5,13),-F(12,13)),
      (F(5,13),-F(12,13)),(F(12,13),-F(5,13)))
    plus=0
    for x,z in octants:
        require(x*x+z*z==1 and z and x+z,'strict no-selector angular interior')
        plus+=int(sgn(z)*sgn(x+z)>0)
    require(plus==6,'no-selector source yields six of eight octants')
    # q=(2+sqrt2)/4 exceeds3/4 because sqrt2>1, certified by squares.
    lo=F(isqrt(2*(1<<64)**2),1<<64)
    require(lo>1 and lo*lo<=2,'strict symbolic quantum/no-selector gap')
    return {'schema':'oi.a1-reset-v6.independent-review.v1','author_commit':author,'verdict':'ACCEPT_WITHIN_STATED_SCOPE',
      'rank_sign_cells':6,'response_cells':len(source),'rank_concordance':str(agree),
      'XZ_law':{''.join('+' if x>0 else '-' for x in k):str(v) for k,v in sorted(law2.items())},
      'XZ_TV':str(distance(law2,q2)),'longer_records':histories,
      'global_bit_lift_inputs':lift_cases,'rotation_inverse_cases':rotations,
      'independent_two_time_integrals':integral_cases,'renewed_adaptive_branch_nodes':repair_cases,
      'renewed_adaptive_leaf_records':repair_leaves,'renewed_zero_mass_leaves':zero,
      'no_selector_plus':str(F(plus,8)),'quantum_no_selector_plus':'(2+sqrt2)/4',
      'scope':'Literal fixed-vector iteration only; original two-time theorem preserved. Fresh independent-pair repair is sufficient and supplied, not native or minimal.',
      'checks':dict(sorted(C.items()))}


if __name__=='__main__':
    ap=ArgumentParser();ap.add_argument('--author-root');args=ap.parse_args()
    print(json.dumps(main(args.author_root),sort_keys=True,separators=(',',':')))
