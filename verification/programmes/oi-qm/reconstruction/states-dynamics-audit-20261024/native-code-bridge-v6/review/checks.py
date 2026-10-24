"""Independent angular-integration and stochastic-response bridge review."""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
from itertools import product
import json
from pathlib import Path


PLANES=((0,0,0),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,1))
CODES=tuple((*p,z) for p in PLANES for z in (0,1))
AXES=((Q(1),Q(0),Q(0)),(Q(0),Q(1),Q(0)),
      (Q(4,5),Q(3,5),Q(0)),(Q(0),Q(0),Q(1)))
NEW=(Q(3,5),Q(-4,5),Q(0))


def check(ok,label):
    if not ok:
        raise RuntimeError(label)


def dot(x,y):
    return sum(a*b for a,b in zip(x,y))


def native_measure(axis,negative):
    planes=((0,0,0),(0,1,0),(0,1,1)) if axis==0 else ((0,0,0),(1,0,0),(1,0,1))
    weights=(5,4,1) if axis==0 else (5,3,2)
    out={c:Q(0) for c in CODES}
    for plane,weight in zip(planes,weights):
        p=tuple(v^negative for v in plane)
        for z in (0,1):
            out[(*p,z)]=Q(weight,20)
    return out


def sector_mass(n,left,right):
    # Marginalizing the orthogonal spherical coordinate gives angular
    # density max(n_x cos(theta)+n_y sin(theta),0)/2. The cuts include
    # every density zero, so each open sector has a constant support sign.
    midpoint=tuple(a+b for a,b in zip(left,right))
    test=dot(n,midpoint)
    check(test!=0,'density support sector not resolved')
    if test<0:
        return Q(0)
    integral=(n[0]*(right[1]-left[1])-n[1]*(right[0]-left[0]))/2
    check(integral>=0,'negative angular sector mass')
    return integral


def sphere_code_measure(n):
    # Exact counterclockwise cuts for X,Y and R=(4/5,3/5).
    cuts=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-3,5),Q(4,5)),
          (Q(-1),Q(0)),(Q(0),Q(-1)),(Q(3,5),Q(-4,5)))
    out={c:Q(0) for c in CODES}
    for left,right in zip(cuts,cuts[1:]+cuts[:1]):
        point=tuple(a+b for a,b in zip(left,right))
        values=(point[0],point[1],4*point[0]+3*point[1])
        check(all(v!=0 for v in values),'unresolved old sign boundary')
        plane=tuple(int(v<0) for v in values)
        mass=sector_mass(n,left,right)
        for z in (0,1):out[(*plane,z)]+=mass/2
    check(sum(out.values())==1,'sphere-code normalization')
    return out


def sphere_new_read(n):
    # Density zeros and NEW-hemisphere zeros, independently of the old R cuts.
    cuts=((Q(1),Q(0)),(Q(4,5),Q(3,5)),(Q(0),Q(1)),
          (Q(-1),Q(0)),(Q(-4,5),Q(-3,5)),(Q(0),Q(-1)))
    total=Q(0)
    for left,right in zip(cuts,cuts[1:]+cuts[:1]):
        point=tuple(a+b for a,b in zip(left,right))
        response=dot(NEW[:2],point)
        check(response!=0,'unresolved new response boundary')
        mass=sector_mass(n,left,right)
        if response>0:total+=mass
    return total


def addz(a,b):return a[0]+b[0],a[1]+b[1]
def mulz(a,b):return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def sumz(xs):
    value=(Q(0),Q(0))
    for x in xs:value=addz(value,x)
    return value


def matrix(r):
    x,y,z=map(Q,r)
    return (((1+z)/2,Q(0)),(x/2,-y/2),(x/2,y/2),((1-z)/2,Q(0)))


def project(r,a):
    rho,p=matrix(r),matrix(a)
    check(dot(a,a)==1,'non-unit projector direction')
    for i,j in product(range(2),repeat=2):
        value=sumz(mulz(p[2*i+k],p[2*k+j]) for k in range(2))
        check(value==p[2*i+j],'projector not idempotent')
    trace=sumz(mulz(p[2*i+j],rho[2*j+i]) for i,j in product(range(2),repeat=2))
    check(trace[1]==0 and 0<=trace[0]<=1,'invalid exact matrix probability')
    return trace[0]


def tv(p,q):
    return sum(abs(p.get(k,Q(0))-q.get(k,Q(0))) for k in set(p)|set(q))/2


def verify():
    check(len(CODES)==12 and len(set(CODES))==12,'native code inventory')
    measures={};old_checks=new_checks=cells=0
    for axis,negative in product(range(2),repeat=2):
        r=tuple(Q((1-2*negative) if j==axis else 0) for j in range(3))
        direct=sphere_code_measure(r[:2])
        native=native_measure(axis,negative)
        check(direct==native,'independently integrated full sign-code pushforward')
        check(all(native[(*plane,0)]==native[(*plane,1)] for plane in PLANES),'joint Z reflection')
        measures[axis,negative]=native
        cells+=len(CODES)
        for j,a in enumerate(AXES):
            observed=sum(p for c,p in native.items() if c[j]==0)
            check(observed==project(r,a),'old menu versus matrix projector')
            old_checks+=1
        check(sphere_new_read(r[:2])==project(r,NEW),'new angular integral versus matrix')
        new_checks+=1

    px,py=measures[0,0],measures[1,0]
    source=tv(px,py)
    targets=(project((1,0,0),NEW),project((0,1,0),NEW))
    target=abs(targets[0]-targets[1])
    lower=(target-source)/2
    check((source,target,lower)==(Q(1,2),Q(7,10),Q(1,10)),'pair contraction lower bound')
    wx=tuple(int(px[c]*20) for c in CODES)
    wy=tuple(int(py[c]*20) for c in CODES)
    check(all(Q(w,20)==px[c] for c,w in zip(CODES,wx)) and
          all(Q(w,20)==py[c] for c,w in zip(CODES,wy)),'integer response weights')
    reachable=set();best=Q(1);count=0;max_gap=Q(0)
    for response in product((0,1),repeat=12):
        x=sum(a*b for a,b in zip(wx,response));y=sum(a*b for a,b in zip(wy,response))
        reachable.add((x,y))
        check(Q(abs(x-y),20)<=source,'deterministic data-processing control')
        max_gap=max(max_gap,Q(abs(x-y),20))
        best=min(best,max(abs(Q(x,20)-targets[0]),abs(Q(y,20)-targets[1])))
        count+=1
    # Separate reachable-response dynamic programming cross-checks the census.
    convolution={(0,0)}
    for x,y in zip(wx,wy):
        convolution|={(a+x,b+y) for a,b in convolution}
    check(convolution==reachable,'response census versus independent convolution')
    check(count==4096 and best==Q(3,20) and max_gap==source,'deterministic optimum')

    # Attaining common response is derived from the source signed difference.
    kernel={}
    for c in CODES:
        difference=px[c]-py[c]
        kernel[c]=Q(1) if difference>0 else Q(0) if difference<0 else Q(2,5) if px[c]>0 else Q(0)
    actual=(sum(px[c]*kernel[c] for c in CODES),sum(py[c]*kernel[c] for c in CODES))
    check(actual==(Q(7,10),Q(1,5)),'supplied stochastic pair response')
    check(all(abs(a-b)==lower for a,b in zip(actual,targets)),'stochastic pair bound attained')
    apparatus_x={(c,j):p/5 for c,p in px.items() for j in range(5)}
    apparatus_y={(c,j):p/5 for c,p in py.items() for j in range(5)}
    check(tv(apparatus_x,apparatus_y)==source,'independent apparatus changes distinguishability')
    inverses=0
    for c,j,bit in product(CODES,range(5),(0,1)):
        out=int(Q(j,5)<kernel[c])
        check(sum(Q(k,5)<kernel[c] for k in range(5))==5*kernel[c],'five-valued realization')
        output=(c,j,bit^out)
        check((output[0],output[1],output[2]^out)==(c,j,bit),'global retained-resource inverse')
        inverses+=1

    labelled_x={(0,c):p for c,p in px.items()};labelled_y={(1,c):p for c,p in py.items()}
    check(tv(labelled_x,labelled_y)==1 and source<1,'extra input memory changes negative contract')
    check((Q(sum(j<8 for j in range(10)),10),Q(sum(j<1 for j in range(10)),10))==targets,
          'preparation-label-dependent response control')
    points=((Q(2,3),Q(1,3),Q(2,3)),(Q(1,3),Q(2,3),Q(2,3)))
    signs=[];margins=[]
    for p in points:
        check(dot(p,p)==1,'independent unit-sphere witness')
        values=tuple(dot(p,a) for a in AXES)
        check(all(x>0 for x in values),'old coarse sign cell')
        new=dot(p,NEW)
        check(new!=0 and p[0]>0 and p[1]>0,'interior positive-density witness')
        signs.append(int(new<0));margins.append(min((*values,abs(new))))
    check(signs==[0,1] and min(margins)>Q(1,100),'new read does not split open sign cells')
    continuous_squared=Q(2,4)
    check(continuous_squared>target*target and continuous_squared>source*source,
          'continuous classical TV cannot support new measurement')
    # The monotonic positive-part identity used in the written continuous-TV
    # proof is independently exercised on rational sphere witnesses/cuts.
    monotonic=0
    directions=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1)),NEW[:2])
    tests=((Q(1),Q(0)),(Q(0),Q(1)),(Q(-1),Q(0)),(Q(0),Q(-1)),
           (Q(3,5),Q(4,5)),(Q(-3,5),Q(4,5)))
    for n,m,p in product(directions,directions,tests):
        u,v=dot(n,p),dot(m,p)
        difference=max(u,0)-max(v,0)
        check(difference==0 or difference*(u-v)>0,'positive-part sign identity')
        monotonic+=1
    return {'projected_preparations':4,'full_pushforward_cells':cells,
            'old_menu_matrix_reads':old_checks,'new_angular_matrix_reads':new_checks,
            'source_pair_tv':str(source),'target_pair_tv':str(target),
            'stochastic_sharp_pair_error':str(lower),'deterministic_responses':count,
            'reachable_response_pairs':len(reachable),'best_deterministic_error':str(best),
            'five_value_reversible_inputs':inverses,'labelled_full_input_tv':'1',
            'same_cell_independent_witnesses':2,'continuous_pair_tv_squared':str(continuous_squared),
            'positive_part_identity_cases':monotonic}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--author-root',type=Path)
    args=parser.parse_args();here=Path(__file__).resolve().parent
    author=args.author_root or (here.parent if (here.parent/'PROVENANCE.json').exists() else here.parent/'code_bridge_v6')
    inputs=json.loads((here/'INPUT-HASHES.json').read_text())
    for name,entry in inputs['author_files'].items():
        content=(author/name).read_bytes()
        check(hashlib.sha256(content).hexdigest()==entry['sha256'],'author SHA-256 '+name)
        check(hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()==entry['git_blob'],'author Git blob '+name)
    result={'schema':'oi.native-code-bridge-v6.independent-review.v1',
            'reviewed_author_revision':inputs['reviewed_author_revision'],
            'checks':verify(),'verdict':'ACCEPT_SCOPED_CALIBRATION_BRIDGE_AND_COMMON_CODE_PAIR_BOUND',
            'scope':'One autonomous common selected-code input and common independent apparatus; no bound asserted for the actual native full boundary/history/masked code or general OI/A2.'}
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__=='__main__':main()
