#!/usr/bin/env python3
"""Exact product-section diagnostic; no predecessor-code imports."""
from fractions import Fraction as F
from itertools import product
import argparse
import json


OMEGA=tuple(product((-1,1),repeat=3))


def need(value,message):
    if not value:
        raise RuntimeError(message)


def prior(r):
    return tuple(F(1,8)*(1+r[0]*v[0])*(1+r[1]*v[1])*(1+r[2]*v[2]) for v in OMEGA)


def moment(p,axes):
    total=F()
    for v,w in zip(OMEGA,p):
        factor=1
        for a in axes:
            factor*=v[a]
        total+=w*factor
    return total


def means(p):
    return tuple(moment(p,(a,)) for a in range(3))


def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F())/2


def determinant_and_rank(matrix):
    rows=[list(row) for row in matrix]
    det=F(1)
    rank=0
    for col in range(len(rows[0])):
        k=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if k is None:
            det=F()
            continue
        if k!=rank:
            rows[k],rows[rank]=rows[rank],rows[k]
            det=-det
        pivot=rows[rank][col]
        det*=pivot
        rows[rank]=[v/pivot for v in rows[rank]]
        for i in range(len(rows)):
            if i!=rank:
                factor=rows[i][col]
                rows[i]=[x-factor*y for x,y in zip(rows[i],rows[rank])]
        rank+=1
    return det,rank


def cc(real=0,imag=0):
    return F(real),F(imag)


def add(a,b):
    return a[0]+b[0],a[1]+b[1]


def mul(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def star(a):
    return a[0],-a[1]


def multiply(a,b):
    return tuple(tuple(add(mul(a[i][0],b[0][j]),mul(a[i][1],b[1][j])) for j in range(2)) for i in range(2))


def decode(r):
    x,y,z=r
    return ((cc((1+z)/2),cc(x/2,-y/2)),(cc(x/2,y/2),cc((1-z)/2)))


def rational_rotation_conjugation(r):
    raw=((cc(2,-1),cc()),(cc(),cc(2,1)))
    adjoint=tuple(tuple(star(raw[j][i]) for j in range(2)) for i in range(2))
    out=multiply(multiply(raw,decode(r)),adjoint)
    return tuple(tuple((v[0]/5,v[1]/5) for v in row) for row in out)


def rotated(r):
    return F(3,5)*r[0]-F(4,5)*r[1],F(4,5)*r[0]+F(3,5)*r[1],r[2]


def main():
    epsilon=F(1,3)
    vectors=[tuple(epsilon*s for s in v) for v in OMEGA]
    priors=[prior(r) for r in vectors]
    need(min(min(p) for p in priors)==F(1,27),'minimum spanning prior atom')
    fourier_checks=0
    for r,p in zip(vectors,priors):
        need(min(p)>0 and sum(p)==1,'finite rank prior positivity')
        need(sum(x*x for x in r)==F(1,3),'finite rank prior Bloch validity')
        need(means(p)==r,'finite rank prior decoding')
        need(rational_rotation_conjugation(r)==decode(rotated(r)),'matrix rotation rank controls')
        for subsetmask in range(8):
            axes=tuple(a for a in range(3) if subsetmask&(1<<a))
            target=F(1)
            for a in axes:
                target*=r[a]
            need(moment(p,axes)==target,'independent Fourier product moment')
            fourier_checks+=1
    # Columns are the eight allowed product preparations, in sign order.
    matrix=tuple(tuple(p[j] for p in priors) for j in range(8))
    det,rank=determinant_and_rank(matrix)
    need(rank==8 and det==F(1,3**12),'finite product-section span')
    # Verify the interpolation basis directly without invoking point priors as inputs.
    inverse_1d=lambda lam,sign:(F(1)+F(lam*sign)/epsilon)/2
    interpolation_cases=0
    for vertex in OMEGA:
        weights=[]
        for signs in OMEGA:
            w=F(1)
            for a in range(3):
                w*=inverse_1d(vertex[a],signs[a])
            weights.append(w)
        reconstructed=tuple(sum((w*p[j] for w,p in zip(weights,priors)),F()) for j in range(8))
        need(reconstructed==tuple(F(v==vertex) for v in OMEGA),'exact affine interpolation')
        need(sum(weights)==1,'affine weights total')
        interpolation_cases+=1
    need(rotated((1,-1,1))[0]==F(7,5),'cube escape after span')

    rplus=(F(2,3),F(-2,3),F())
    rminus=tuple(-v for v in rplus)
    pplus,pminus=prior(rplus),prior(rminus)
    for r,p in ((rplus,pplus),(rminus,pminus)):
        need(sum(x*x for x in r)==F(8,9),'pair Bloch validity')
        need(min(p)==F(1,72) and sum(p)==1,'pair positive normalized')
        need(means(p)==r,'pair product decoding')
        need(rational_rotation_conjugation(r)==decode(rotated(r)),'pair matrix rotation')
    source_distance=tv(pplus,pminus)
    target_records=[]
    for r in (rplus,rminus):
        # Matrix X expectation is the sum of the offdiagonal entries.
        rho=rational_rotation_conjugation(r)
        x=add(rho[0][1],rho[1][0])
        need(x[1]==0,'X expectation reality')
        target_records.append(((1+x[0])/2,(1-x[0])/2))
    need(target_records==[(F(29,30),F(1,30)),(F(1,30),F(29,30))],'target pair law')
    target_distance=tv(*target_records)
    lower=(target_distance-source_distance)/2
    need(source_distance==F(2,3) and target_distance==F(14,15),'pair distinguishability')
    need(lower==F(2,15),'pair triangle lower bound')
    extreme_count=0
    best_error=None
    maximal_distance=F()
    for mask in range(256):
        outcomes=[]
        for p in (pplus,pminus):
            q=sum((p[j] for j in range(8) if mask&(1<<j)),F())
            outcomes.append((q,1-q))
        d=tv(*outcomes)
        need(d<=source_distance,'response data processing')
        maximal_distance=max(maximal_distance,d)
        err=max(tv(a,b) for a,b in zip(outcomes,target_records))
        need(err>=lower,'response pair error bound')
        best_error=err if best_error is None else min(best_error,err)
        extreme_count+=1
    need(maximal_distance==source_distance and best_error==lower,'tight response control')
    ordinary_X=[]
    for p in (pplus,pminus):
        q=sum((w for v,w in zip(OMEGA,p) if v[0]==1),F())
        ordinary_X.append((q,1-q))
    need(ordinary_X==[(F(5,6),F(1,6)),(F(1,6),F(5,6))],'explicit tight X response')
    need(max(tv(a,b) for a,b in zip(ordinary_X,target_records))==lower,'explicit pair tightness')

    # Physical mixing creates additional fibres but is not needed by the span proof.
    mixed=tuple((a+b)/2 for a,b in zip(pplus,pminus))
    uniform=prior((F(),F(),F()))
    need(means(mixed)==means(uniform)==(0,0,0),'mixture same decoder')
    need(mixed!=uniform,'product section nonconvex')
    need(moment(mixed,(0,1))==F(-4,9) and moment(uniform,(0,1))==0,'retained mixture correlation')

    # Positive controls retained by the changed source domain.
    clifford_cases=0
    for r in vectors+[rplus,rminus]:
        for action in (lambda v:(v[2],-v[1],v[0]),lambda v:(-v[1],v[0],v[2])):
            p=prior(r)
            outgoing={action(v):w for v,w in zip(OMEGA,p)}
            transformed=tuple(outgoing[v] for v in OMEGA)
            need(transformed==prior(action(r)),'product section Clifford closure')
            clifford_cases+=1

    # A preparation-dependent external controller can supply either target law.
    # This labels the input, enlarging the distinguishability resource to one.
    controller_laws=[]
    for accept in (29,1):
        yes=sum(int(seed<accept) for seed in range(30))
        controller_laws.append((F(yes,30),1-F(yes,30)))
    need(controller_laws==target_records,'preparation-dependent controller control')
    joint_input_plus=tuple(w/30 if label==0 else F() for label in range(2) for w in pplus for seed in range(30))
    joint_input_minus=tuple(w/30 if label==1 else F() for label in range(2) for w in pminus for seed in range(30))
    need(tv(joint_input_plus,joint_input_minus)==1,'input label changes resource premise')

    return {
        'schema':'oi-product-section-v4.1',
        'verdict':'PASS',
        'scope':'fixed eight-sign moment map, product preparation section, independent apparatus',
        'finite_spanning_product_priors':8,
        'minimum_spanning_prior_atom':'1/27',
        'spanning_prior_bloch_norm_squared':'1/3',
        'preparation_matrix_rank':rank,
        'preparation_matrix_determinant':str(det),
        'fourier_moment_controls':fourier_checks,
        'affine_interpolation_cases':interpolation_cases,
        'rational_rotation_matrix_cases':10,
        'cube_escape_coordinate':'7/5',
        'pair_r_plus':['2/3','-2/3','0'],
        'pair_bloch_norm_squared':'8/9',
        'pair_minimum_atom':'1/72',
        'source_pair_tv':str(source_distance),
        'target_rotated_X_pair_tv':str(target_distance),
        'worst_pair_record_error_floor':str(lower),
        'best_deterministic_pair_response_error':str(best_error),
        'deterministic_response_controls':extreme_count,
        'tight_response':'ordinary X sign read',
        'mixture_zero_mean_xy_correlation':'-4/9',
        'Clifford_product_closure_controls':clifford_cases,
        'prep_dependent_controller_target_laws':'exact using supplied input label and uniform30seed',
        'prep_label_joint_input_tv':'1',
        'full_channel_minimax_claimed':False,
        'native_implementation_claimed':False,
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output')
    args=parser.parse_args()
    output=json.dumps(main(),indent=2,sort_keys=True)+'\n'
    if args.output:
        with open(args.output,'w',encoding='utf-8') as stream:
            stream.write(output)
    else:
        print(output,end='')
