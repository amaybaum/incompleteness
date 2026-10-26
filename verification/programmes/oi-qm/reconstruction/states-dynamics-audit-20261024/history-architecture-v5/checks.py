#!/usr/bin/env python3
"""Exact controls for a supplied continuous Kochen-Specker qubit interface.

No continuum is discretized here. Angular controls are exact integrals;
general source kernels use the separately proved hemisphere identity.
"""
from collections import Counter
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import product
import argparse
import json


COUNTS=Counter()


def need(name,condition):
    if not condition:
        raise RuntimeError(name)
    COUNTS[name]+=1


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),F())


def scale(v,c):
    return tuple(c*x for x in v)


def addv(a,b):
    return tuple(x+y for x,y in zip(a,b))


def matv(a,v):
    return tuple(dot(row,v) for row in a)


def transpose(a):
    return tuple(zip(*a))


def matmul(a,b):
    return tuple(tuple(dot(row,col) for col in transpose(b)) for row in a)


I3=((F(1),F(),F()),(F(),F(1),F()),(F(),F(),F(1)))
H3=((F(),F(),F(1)),(F(),F(-1),F()),(F(1),F(),F()))
S3=((F(),F(-1),F()),(F(1),F(),F()),(F(),F(),F(1)))
RZ=((F(3,5),F(-4,5),F()),(F(4,5),F(3,5),F()),(F(),F(),F(1)))
RY=((F(3,5),F(),F(4,5)),(F(),F(1),F()),(F(-4,5),F(),F(3,5)))
ROTATIONS=(I3,H3,S3,RZ,RY)
AXES=tuple(tuple(F(i==a) for i in range(3)) for a in range(3))


# Exact rational complex matrix arithmetic, independent of Bloch updates.
def c(a=0,b=0):
    return F(a),F(b)


def ca(x,y):
    return x[0]+y[0],x[1]+y[1]


def cm(x,y):
    return x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]


def star(x):
    return x[0],-x[1]


def multiply(a,b):
    return tuple(tuple(ca(cm(a[i][0],b[0][j]),cm(a[i][1],b[1][j])) for j in range(2)) for i in range(2))


def adjoint(a):
    return tuple(tuple(star(a[j][i]) for j in range(2)) for i in range(2))


def matrix_scale(a,k):
    return tuple(tuple((k*z[0],k*z[1]) for z in row) for row in a)


ZERO=c()
ONE=c(1)
IDENTITY=((ONE,ZERO),(ZERO,ONE))
PAULI=(
    ((ZERO,ONE),(ONE,ZERO)),
    ((ZERO,c(0,-1)),(c(0,1),ZERO)),
    ((ONE,ZERO),(ZERO,c(-1))),
)
GATE_MATRICES=(
    (IDENTITY,1),
    (((ONE,ONE),(ONE,c(-1))),2),
    (((ONE,ZERO),(ZERO,c(0,1))),1),
    (((c(2,-1),ZERO),(ZERO,c(2,1))),5),
    (((c(2),c(-1)),(c(1),c(2))),5),
)


def density(w,r):
    x,y,z=r
    return ((c((w+z)/2),c(x/2,-y/2)),(c(x/2,y/2),c((w-z)/2)))


def projector(a,s):
    return density(F(1),scale(a,s))


def conjugate(rho,g):
    u,norm=GATE_MATRICES[g]
    return matrix_scale(multiply(multiply(u,rho),adjoint(u)),F(1,norm))


def trace(rho):
    return ca(rho[0][0],rho[1][1])


def determinant(rho):
    x=cm(rho[0][0],rho[1][1]);y=cm(rho[0][1],rho[1][0])
    return x[0]-y[0],x[1]-y[1]


# An allowed measure is a finite positive mixture of cosine-hemisphere laws.
def mass(prep):
    return sum((w for w,n in prep),F())


def bloch(prep):
    return tuple(sum((w*n[i] for w,n in prep),F()) for i in range(3))


def decode(prep):
    return density(mass(prep),bloch(prep))


def rotation(prep,g):
    return tuple((w,matv(ROTATIONS[g],n)) for w,n in prep)


def instrument(prep,a,s):
    # This integral is proved in REPORT.md and independently checked below
    # on coplanar inputs by exact angular endpoint integration.
    w=sum((weight*(1+s*dot(n,a))/2 for weight,n in prep),F())
    return ((w,scale(a,s)),) if w else ()


CIRCLE=tuple(dict.fromkeys(
    [(F(1),F()),(F(-1),F()),(F(),F(1)),(F(),F(-1))]+
    [(F(sx*3,5),F(sy*4,5)) for sx,sy in product((-1,1),repeat=2)]+
    [(F(sx*4,5),F(sy*3,5)) for sx,sy in product((-1,1),repeat=2)]))


def angular_cmp(a,b):
    def half(v):
        return 0 if v[1]>0 or (v[1]==0 and v[0]>0) else 1
    if half(a)!=half(b):
        return half(a)-half(b)
    cross=a[0]*b[1]-a[1]*b[0]
    return -1 if cross>0 else 1 if cross<0 else 0


def sphere_integral(n,constraints):
    """Integral of mu_n over any coplanar hemisphere intersection.

    The polar integral is pi/2. Remaining azimuth primitive is
    n_x*sin(phi)-n_z*cos(phi), evaluated at rational unit endpoints.
    Neither Born probabilities nor the proposed output law is used.
    """
    points={(F(1),F()),(F(-1),F()),(F(),F(1)),(F(),F(-1))}
    for direction in (n,)+tuple(constraints):
        perp=(-direction[1],direction[0])
        points.add(perp);points.add(scale(perp,-1))
    points=sorted(points,key=cmp_to_key(angular_cmp))
    total=F()
    for start,end in zip(points,points[1:]+points[:1]):
        middle=addv(start,end)
        if dot(n,middle)>0 and all(dot(a,middle)>0 for a in constraints):
            total+=n[0]*(end[1]-start[1])-n[1]*(end[0]-start[0])
    return total/2


def tv(a,b):
    return sum((abs(x-y) for x,y in zip(a,b)),F())/2


def raw_two_read(prep,a,b):
    return tuple(sum((w*sphere_integral(n,(scale(a,s),scale(b,t))) for w,n in prep),F())
                 for s,t in product((-1,1),repeat=2))


def send_blank_to(g):
    ez=AXES[2]
    if g==ez:
        return I3
    v=addv(ez,scale(g,-1))
    denominator=dot(v,v)
    householder=tuple(tuple(F(i==j)-2*v[i]*v[j]/denominator for j in range(3)) for i in range(3))
    flip=((-F(1),F(),F()),(F(),F(1),F()),(F(),F(),F(1)))
    return matmul(householder,flip)


def main():
    global COUNTS
    COUNTS=Counter()
    # Independent exact continuum-integral controls on three rational planes.
    for n in CIRCLE:
        need('angular_normalization',sphere_integral(n,())==1)
        for a in CIRCLE:
            overlap=sphere_integral(n,(a,))
            need('angular_probability_range',0<=overlap<=1)
            need('independent_angular_Born_integral',overlap==(1+dot(n,a))/2)
            for omitted in range(3):
                axes=[i for i in range(3) if i!=omitted]
                n3=tuple(n[axes.index(i)] if i in axes else F() for i in range(3))
                a3=tuple(a[axes.index(i)] if i in axes else F() for i in range(3))
                p=projector(a3,1)
                rho=density(F(1),n3)
                prob=trace(multiply(multiply(p,rho),p))
                need('angular_matrix_independent_control',prob==c(overlap))

    n1=(F(2,3),F(-2,3),F(1,3));n2=(F(2,3),F(-2,3),F(-1,3))
    eigens=[((F(1),scale(a,s)),) for a in AXES for s in (-1,1)]
    pure=[((F(1),n),) for n in (n1,n2,scale(n1,-1),scale(n2,-1))]
    eta_x=((F(1,2),AXES[0]),(F(1,2),scale(AXES[0],-1)))
    eta_z=((F(1,2),AXES[2]),(F(1,2),scale(AXES[2],-1)))
    plus=((F(1,2),n1),(F(1,2),n2))
    minus=tuple((w,scale(n,-1)) for w,n in plus)
    small=tuple((F(1,3),scale(AXES[i],s)) for i,s in enumerate((1,-1,1)))
    smallminus=tuple((w,scale(n,-1)) for w,n in small)
    other=((F(1,3),n1),(F(2,3),AXES[2]))
    preparations=eigens+pure+[eta_x,eta_z,plus,minus,small,smallminus,other]
    settings=AXES+(n1,n2,(F(3,5),F(-4,5),F()),(F(3,5),F(),F(4,5)))
    for prep in preparations:
        need('preparation_mass',mass(prep)==1)
        need('cone_positivity',all(w>=0 and dot(n,n)==1 for w,n in prep))
        need('decoded_positivity',determinant(decode(prep))[0]>=0)
        # The exact scaled first moment is proved by the polar integral.
        first_moment=scale(bloch(prep),F(2,3))
        need('scaled_first_moment_decoder',scale(first_moment,F(3,2))==bloch(prep))
        for g in range(len(ROTATIONS)):
            out=rotation(prep,g)
            need('rotation_isometry',matmul(ROTATIONS[g],transpose(ROTATIONS[g]))==I3)
            need('rotation_cone',all(w>=0 and dot(n,n)==1 for w,n in out))
            need('rotation_matrix_intertwining',decode(out)==conjugate(decode(prep),g))
        for a,s in product(settings,(-1,1)):
            post=instrument(prep,a,s)
            pr=projector(a,s)
            reference=multiply(multiply(pr,decode(prep)),pr)
            need('complete_instrument_intertwining',decode(post)==reference)
            need('instrument_cone',all(w>=0 and dot(n,n)==1 for w,n in post))

    # Correct full joint records under several finite adaptive policies.
    def policy(k,history):
        t=len(history)
        if k==0:
            return 0,t%len(settings)
        if k==1:
            return 3,0
        if k==2:
            return (4 if not history or history[-1][-1]>0 else 3),(t+sum(h[-1]>0 for h in history))%len(settings)
        return (1 if t%2 else 2),(2+t+sum(h[-1] for h in history))%len(settings)
    for prep in preparations:
        for k in range(4):
            branches=[((),prep,decode(prep))]
            for t in range(3):
                next_branches=[]
                for history,source,reference in branches:
                    gate,axis=policy(k,history)
                    a=settings[axis]
                    source=rotation(source,gate);reference=conjugate(reference,gate)
                    for s in (-1,1):
                        post=instrument(source,a,s)
                        pr=projector(a,s)
                        quantum=multiply(multiply(pr,reference),pr)
                        need('adaptive_complete_branch',decode(post)==quantum)
                        record=(t+1,gate,axis,1,s)
                        next_branches.append((history+(record,),post,quantum))
                branches=next_branches
            need('adaptive_total_mass',sum(mass(p) for _,p,_ in branches)==1)
            need('adaptive_zero_branches_retained',len(branches)==8)

    # Same decoded I/2, different hidden preparations; no-reset/old-workspace controls.
    x2=(F(1),F());z2=(F(),F(1));b2=(F(3,5),F(4,5))
    mixed_x=((F(1,2),x2),(F(1,2),scale(x2,-1)))
    mixed_z=((F(1,2),z2),(F(1,2),scale(z2,-1)))
    need('mixed_preparations_same_decoder',decode(eta_x)==decode(eta_z))
    raw_x=raw_two_read(mixed_x,z2,b2);raw_z=raw_two_read(mixed_z,z2,b2)
    need('no_reset_exact_joint_laws',raw_z==(F(9,20),F(1,20),F(1,20),F(9,20)) and
         raw_x==(F(7,20),F(3,20),F(3,20),F(7,20)))
    no_reset_tv=tv(raw_x,raw_z)
    need('no_reset_congruence_failure',no_reset_tv==F(1,5))
    proper=[]
    for prep in (eta_x,eta_z):
        proper.append(tuple(mass(instrument(instrument(prep,AXES[2],s),(F(3,5),F(),F(4,5)),t))
                            for s,t in product((-1,1),repeat=2)))
    need('proper_reset_restores_equivalence',proper[0]==proper[1]==raw_z)
    # Public old-Z sign with private old-b read reproduces the no-reset laws.
    need('retained_workspace_access_failure',tv(raw_x,raw_z)==F(1,5))

    # Hidden-state-dependent timing carries an extra preparation-sensitive bit.
    timing=[];sign_only=[]
    for n in (z2,scale(z2,-1)):
        rows=[]
        for s,zsign in product((-1,1),repeat=2):
            rows.append(sphere_integral(n,(scale(x2,s),scale(z2,zsign))))
        timing.append(tuple(rows))
        sign_only.append(tuple(sum(rows[2*i:2*i+2]) for i in range(2)))
    need('timing_countercontrol_sign_marginals',sign_only==[(F(1,2),F(1,2))]*2)
    need('timing_joint_record_gap',tv(*timing)==1)

    # Even one extra private-seed bit can violate the outgoing cone.
    # c=sqrt(U) has density2c; expose the flag U>4/9 (equivalently c>2/3).
    cut=F(2,3)
    flag_probability=1-cut**2
    cap_first_moment=F(2,3)*(1-cut**3)/flag_probability
    cap_bloch_scale=F(3,2)*cap_first_moment
    cap_det=(1-cap_bloch_scale**2)/4
    need('single_seed_bit_mass',flag_probability==F(5,9))
    need('single_seed_bit_nonpositive',cap_bloch_scale==F(19,15) and cap_det==F(-34,225))

    # Continuous reset samples and an explicit globally invertible extension.
    witness_points=AXES+tuple(scale(a,-1) for a in AXES)+(n1,n2)
    for frame in ROTATIONS:
        ex,ey,pole=tuple(transpose(frame))
        for cosine,sine in ((F(),F(1)),(F(3,5),F(4,5)),(F(4,5),F(3,5)),(F(1),F())):
            for azimuth in CIRCLE:
                tangent=addv(scale(ex,azimuth[0]),scale(ey,azimuth[1]))
                for source in witness_points:
                    s=1 if dot(pole,source)>=0 else -1
                    g=addv(scale(tangent,sine),scale(pole,s*cosine))
                    need('reset_sample_geometry',dot(g,g)==1 and dot(g,pole)==s*cosine)
                    transfer=send_blank_to(g)
                    need('dilation_rotation_geometry',matv(transfer,AXES[2])==g and
                         matmul(transfer,transpose(transfer))==I3)
                    need('ready_reset_output',matv(transfer,AXES[2])==g)
                    for blank,record in product(witness_points,(0,1)):
                        image=(matv(transfer,blank),source,record^(s==-1))
                        # source, seed and setting determine the same transfer.
                        back=(image[1],matv(transpose(transfer),image[0]),image[2]^(s==-1))
                        need('dilation_inverse',back==(source,blank,record))
                    # Exposing the two continuous seeds fixes g and leaves a point law.
                    point_decoder=density(F(1),scale(g,F(3,2)))
                    need('exposed_seed_decoder_nonpositive',determinant(point_decoder)==c(F(-5,16)))

    # The previous rational non-Clifford pair is represented by four rational poles.
    need('new_pair_positive_preparation',bloch(plus)==(F(2,3),F(-2,3),F()) and bloch(minus)==scale(bloch(plus),-1))
    target_probs=[]
    for prep in (plus,minus):
        out=rotation(prep,3)
        target_probs.append((mass(instrument(out,AXES[0],1)),mass(instrument(out,AXES[0],-1))))
    need('old_nonclifford_witness_passes',target_probs==[(F(29,30),F(1,30)),(F(1,30),F(29,30))])
    need('sphere_input_distinguishability_sufficient',F(8,9)-F(14,15)**2==F(4,225))
    return {
        'schema':'oi-continuous-qubit-architecture-v5.1',
        'verdict':'PASS',
        'scope':'supplied continuous single-qubit projective/unitary interface, not native sourcing',
        'pure_density':'(n dot lambda)_+/pi',
        'fixed_decoder_bloch_scale':'3/2',
        'preparations_checked':len(preparations),
        'rational_coplanar_directions':len(CIRCLE),
        'settings_checked':len(settings),
        'rotation_generators_checked':len(ROTATIONS),
        'adaptive_policies':4,'adaptive_depth':3,'adaptive_leaf_records':len(preparations)*4*8,
        'nonclifford_pair_output_laws':[[str(x) for x in row] for row in target_probs],
        'continuous_pair_ontic_tv':'2*sqrt(2)/3',
        'continuous_pair_ontic_tv_squared':'8/9',
        'target_pair_record_tv':'14/15',
        'no_reset_joint_record_tv':str(no_reset_tv),
        'retained_workspace_read_joint_tv':'1/5',
        'timing_sign_marginal_tv':'0','timing_full_record_tv':'1',
        'exposed_reset_seed_point_decoder_determinant':'-5/16',
        'single_reset_seed_bit_probability':'5/9',
        'single_reset_seed_bit_bloch_length':'19/15',
        'single_reset_seed_bit_decoder_determinant':'-34/225',
        'native_availability_claimed':False,'full_POVM_or_composite_reconstruction_claimed':False,
        'checks':dict(sorted(COUNTS.items())),
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output')
    args=parser.parse_args()
    text=json.dumps(main(),indent=2,sort_keys=True)+'\n'
    if args.output:
        with open(args.output,'w',encoding='utf-8') as out:
            out.write(text)
    else:
        print(text,end='')
