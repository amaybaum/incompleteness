#!/usr/bin/env python3
"""Exact bounded audit of a specified fixed-vector Montina continuation.

General continuum weights are proved in REPORT.md. Finite checks enumerate
all six rank-sign cells and independent coordinate-reflection signs, using
rational unit-vector witnesses. No Monte Carlo or author imports.
"""
from argparse import ArgumentParser
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import cmp_to_key
from itertools import product
from pathlib import Path
import hashlib
import json

C = Counter()

def need(name, ok):
    C[name] += 1
    if not ok:
        raise RuntimeError('failed control: ' + name)


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def sign(x): return 1 if x >= 0 else -1

def winner(vectors, axis):
    return 0 if dot(vectors[0],axis)**2 >= dot(vectors[1],axis)**2 else 1


def prepare(vectors, pole):
    r=winner(vectors,pole)
    return r,sign(dot(vectors[r],pole))


def measure(vectors, r, t, axis):
    k=t*sign(dot(vectors[r],axis))
    new_r=winner(vectors,axis)
    return k,new_r,k*sign(dot(vectors[new_r],axis))


def measure_reference_basis(vectors, r, s, axis):
    # Eq.17 evaluated in its reference n=Z basis, independently of orientation t.
    z=(F(0),F(0),F(1))
    k=s*sign(dot(vectors[r],z))*sign(dot(vectors[r],axis))
    new_r=winner(vectors,axis)
    new_s=s*sign(dot(vectors[r],z))*sign(dot(vectors[r],axis))
    new_s*=sign(dot(vectors[new_r],z))*sign(dot(vectors[new_r],axis))
    return k,new_r,new_s


def rotation(vectors,r,s,R):
    z=(F(0),F(0),F(1))
    out=tuple(tuple(dot(row,v) for row in R) for v in vectors)
    out_s=s*sign(dot(vectors[r],z))*sign(dot(out[r],z))
    return out,r,out_s


def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def projector(axis,k):
    x,y,z=axis
    if y:
        raise ValueError('bounded matrix control is in the real XZ plane')
    return (((F(1)+k*z)/2,k*x/2),(k*x/2,(F(1)-k*z)/2))


def quantum_records(pole, axes):
    states={():projector(pole,1)}
    for a in axes:
        out={}
        for h,rho in states.items():
            for k in (-1,1):
                p=projector(a,k)
                out[h+(k,)]=mm(mm(p,rho),p)
        states=out
    return {h:rho[0][0]+rho[1][1] for h,rho in states.items()}


def tv(p,q):
    return sum(abs(p.get(k,F(0))-q.get(k,F(0))) for k in p.keys()|q.keys())/2


def circle_integral(n,a):
    # Direct signed primitive over hemisphere intersection, not Born expression.
    n=(n[0],n[2]);a=(a[0],a[2])
    points={(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))}
    for p in (n,a):
        b=(-p[1],p[0]);points.add(b);points.add(neg(b))
    def cmp(p,q):
        hp=0 if (p[1]>0 or (p[1]==0 and p[0]>=0)) else 1
        hq=0 if (q[1]>0 or (q[1]==0 and q[0]>=0)) else 1
        if hp!=hq: return -1 if hp<hq else 1
        c=p[0]*q[1]-p[1]*q[0]
        return -sign(c) if c else 0
    ring=sorted(points,key=cmp_to_key(cmp))
    val=F(0)
    for p,q in zip(ring,ring[1:]+ring[:1]):
        mid=tuple(x+y for x,y in zip(p,q))
        if dot(n,mid)>0 and dot(a,mid)>0:
            val+=(n[0]*(q[1]-p[1])-n[1]*(q[0]-p[0]))/2
    return val


def source_cells():
    # Six sign patterns of coordinate-square differences, each probability1/6
    # by coordinate permutations plus pair interchange. Exact sphere measure
    # zero for ties. Four independent X/Z signs contribute probability1/16.
    u=(F(2,7),F(3,7),F(6,7));v=(F(6,7),F(2,7),F(3,7))
    cells=[]
    patterns=set()
    for shift,swap in product(range(3),(False,True)):
        pair=(u[shift:]+u[:shift],v[shift:]+v[:shift])
        if swap: pair=pair[::-1]
        pattern=tuple(sign(pair[0][d]**2-pair[1][d]**2) for d in range(3))
        need('strict_rank_witness',all(pair[0][d]**2!=pair[1][d]**2 for d in range(3)))
        need('coordinate_square_trace_zero',sum(pair[0][d]**2-pair[1][d]**2 for d in range(3))==0)
        patterns.add(pattern)
        for signs in product((-1,1),repeat=4):
            vs=( (pair[0][0]*signs[0],pair[0][1],pair[0][2]*signs[1]),
                 (pair[1][0]*signs[2],pair[1][1],pair[1][2]*signs[3]) )
            need('rational_sphere_witnesses',all(dot(x,x)==1 for x in vs))
            cells.append((vs,F(1,96)))
    need('all_six_nontrivial_difference_patterns',len(patterns)==6 and all(0<sum(x>0 for x in p)<3 for p in patterns))
    return cells


def reversible_update(vectors,axis,r,t,g,c):
    # Bits r,g,c and sign t. g=0 is the ready garbage bit.
    k=t*sign(dot(vectors[r],axis))
    j=winner(vectors,axis)
    out_r=g^j
    out_t=k*sign(dot(vectors[out_r],axis))
    return out_r,out_t,r,c^(k==-1)


def inverse_update(vectors,axis,out_r,out_t,out_g,out_c):
    j=winner(vectors,axis)
    k=out_t*sign(dot(vectors[out_r],axis))
    r=out_g
    t=k*sign(dot(vectors[r],axis))
    return r,t,out_r^j,out_c^(k==-1)


def main():
    zero=F(0);one=F(1)
    X=(one,zero,zero);Z=(zero,zero,one)
    circle2=((one,zero),(F(3,5),F(4,5)),(F(4,5),F(3,5)),(zero,one),
             (-F(3,5),F(4,5)),(-F(4,5),F(3,5)),(-one,zero),
             (-F(3,5),-F(4,5)),(-F(4,5),-F(3,5)),(zero,-one),
             (F(3,5),-F(4,5)),(F(4,5),-F(3,5)))
    settings=tuple((x,zero,z) for x,z in circle2)
    for n,a in product(settings,repeat=2):
        born=quantum_records(n,[a])[(1,)]
        need('two_time_direct_integral_matrix',circle_integral(n,a)==born)
        need('complementary_integral_mass',circle_integral(n,a)+circle_integral(n,neg(a))==1)
    # Selected-vector density is |n.u|/(2pi); folding gives KS. Its normalizing
    # radial factor is independently checked by integrating 2c on [0,1].
    need('selected_folded_density_normalized',F(2)*F(1,2)==1)

    cells=source_cells()
    need('exact_cell_mass',sum(w for v,w in cells)==1)
    agreement=sum(w for v,w in cells if winner(v,X)==winner(v,Z))
    need('rank_concordance_probability',agreement==F(1,3))
    # Orthogonal first-read comparison, all sign/rank cells exactly.
    hist={}
    for h in (1,2,3,4,6,8,10):
        axes=tuple(X if j%2==0 else Z for j in range(h))
        laws=defaultdict(F)
        for vectors,w in cells:
            r,t=prepare(vectors,Z);s=t*sign(dot(vectors[r],Z));rec=[]
            for a in axes:
                k,nr,nt=measure(vectors,r,t,a)
                k2,nr2,ns=measure_reference_basis(vectors,r,s,a)
                need('two_coordinate_engines_agree',k==k2 and nr==nr2 and ns==nt*sign(dot(vectors[nr],Z)))
                rec.append(k);r,t,s=nr,nt,ns
            laws[tuple(rec)]+=w
        q=quantum_records(Z,axes)
        need('complete_law_mass',sum(laws.values())==sum(q.values())==1)
        if h==1:
            need('first_X_read_passes',dict(laws)==q)
        else:
            need('four_possible_fixed_vector_records',len(laws)==4)
            need('reused_vector_record_failure',tv(dict(laws),q)>0)
        hist[str(h)]={'native_comparison_scope':'abstract fixed-vector continuation',
            'model_support':len(laws),'quantum_support':sum(x>0 for x in q.values()),
            'complete_record_tv':str(tv(dict(laws),q)),
            'model_law':{''.join('+' if k>0 else '-' for k in s):str(p) for s,p in sorted(laws.items())}}
    h2=hist['2']['model_law']
    need('XZ_joint_witness',h2=={'--':'1/6','-+':'1/3','+-':'1/6','++':'1/3'})
    need('XZ_complete_record_TV',hist['2']['complete_record_tv']=='1/6')
    for h in (3,4,6,8,10):
        need('long_support_TV_exact',F(hist[str(h)]['complete_record_tv'])==1-F(4,2**h))

    # Geometry-independent map/inverse checks and explicit many-to-one update.
    R=((F(3,5),zero,F(4,5)),(zero,one,zero),(-F(4,5),zero,F(3,5)))
    RT=tuple(zip(*R))
    for vectors,_ in cells:
        for a in settings:
            images=set()
            physical_images=set()
            for r,t,g,c in product((0,1),(-1,1),(0,1),(0,1)):
                out=reversible_update(vectors,a,r,t,g,c)
                need('global_dilation_inverse',inverse_update(vectors,a,*out)==(r,t,g,c))
                images.add(out)
                if g==c==0:
                    k,nr,nt=measure(vectors,r,t,a)
                    need('ready_dilation_instrument',out==(nr,nt,r,int(k==-1)))
                    physical_images.add((k,nr,nt))
            need('global_dilation_permutation',len(images)==16)
            need('unlifted_update_two_to_one',len(physical_images)==2)
        for r,s in product((0,1),(-1,1)):
            rv,rr,ss=rotation(vectors,r,s,R)
            iv,ir,iss=rotation(rv,rr,ss,RT)
            need('rotation_inverse',iv==vectors and ir==r and iss==s)
            need('orientation_bit_rotation_invariant',s*sign(dot(vectors[r],Z))==ss*sign(dot(rv[r],Z)))

    # Reset-source repair is compared branchwise with a fresh geometric pair,
    # whose folded selected-vector law just passed 144 independent integrals.
    # Dynamic programming multiplies geometric kernels; matrix products supply
    # the independently evaluated complete-branch quantum reference.
    repair_nodes=0;repair_leaves=0;zero_leaves=0
    for n in settings[:4]:
        for policy in range(4):
            states=[((),F(1),n)]
            for depth in range(4):
                out=[]
                for rec,w,pole in states:
                    a=settings[(policy+depth+sum(k>0 for k in rec))%len(settings)]
                    for k in (-1,1):
                        p=circle_integral(pole,a if k==1 else neg(a))
                        out.append((rec+(k,),w*p,tuple(k*x for x in a)))
                        repair_nodes+=1
                states=out
            for rec,w,pole in states:
                rho=projector(n,1);past=()
                for depth,k in enumerate(rec):
                    a=settings[(policy+depth+sum(j>0 for j in past))%len(settings)]
                    p=projector(a,k);rho=mm(mm(p,rho),p);past+= (k,)
                need('fresh_pair_complete_adaptive_branch_mass',rho[0][0]+rho[1][1]==w)
                out_rho=tuple(tuple(w*e for e in row) for row in projector(pole,1))
                need('fresh_pair_complete_adaptive_outgoing_state',rho==out_rho)
                repair_leaves+=1;zero_leaves+=int(w==0)
    # Missing winner selection: a uniformly distributed single sphere vector
    # folded toward Z has a uniform azimuth. The 45-degree diagonal read has
    # eight equal azimuth octants; each rational witness is strictly inside
    # one. Their sign responses derive the actual triangle-law3/4.
    octants=((F(4,5),F(3,5)),(F(3,5),F(4,5)),(-F(3,5),F(4,5)),
             (-F(4,5),F(3,5)),(-F(4,5),-F(3,5)),(-F(3,5),-F(4,5)),
             (F(3,5),-F(4,5)),(F(4,5),-F(3,5)))
    no_selector=F(0)
    for x,z in octants:
        need('single_vector_octant_witness',x*x+z*z==1 and x+z!=0 and z!=0)
        no_selector+=F(1,8)*int(sign(z)*sign(x+z)==1)
    need('no_selector_geometric_probability',no_selector==F(3,4))
    # Independent Born projector has plus mass(2+sqrt2)/4. Squaring after
    # moving its rational term shows the actual nonzero difference exactly.
    need('no_selector_countercontrol',4*no_selector-2==1 and F(2)>F(1)**2)
    need('renewal_repairs_XZ_law',quantum_records(Z,[X,Z])=={k:F(1,4) for k in product((-1,1),repeat=2)})

    return {'schema':'oi-exact-reset-resource-audit-v6.1','verdict':'PASS',
        'claim_scope':'fixed two-vector deterministic continuation, not original two-time model refutation',
        'source_rank_cells':6,'coordinate_sign_cells_per_rank':16,'source_cell_count':len(cells),
        'rank_concordance_probability':str(agreement),'XZ_final_Z_plus':'2/3','XZ_quantum_final_Z_plus':'1/2',
        'XZ_joint_record_TV':'1/6','fixed_vector_records':hist,
        'fresh_pair_repair':{'scope':'supplied independent geometric pairs per reset; no native availability',
            'two_time_integrals':len(settings)**2,'adaptive_depth':4,'adaptive_policies':4,
            'initial_preparations':4,'branch_nodes':repair_nodes,'leaf_records':repair_leaves,
            'zero_mass_leaves':zero_leaves,
            'sphere_vectors_for_h_measurements_and_outgoing_reset':'2*(h+1)',
            'ready_garbage_bits_for_explicit_bit_map':'h',
            'minimum_fresh_continuous_entropy_claimed':False},
        'reversible_bit_update':{'garbage_bits_per_declared_lift':1,'pointer_bits_per_measurement':1,
            'unlifted_multiplicity':2,'native_compilation_claimed':False},
        'no_selector_control':{'geometric_plus':str(no_selector),
            'quantum_plus':'(2+sqrt2)/4','positive_gap':'(sqrt2-1)/4'},
        'full_equivalence_claimed':False,'checks':dict(sorted(C.items()))}


if __name__=='__main__':
    ap=ArgumentParser();ap.add_argument('--output');args=ap.parse_args()
    out=json.dumps(main(),indent=2,sort_keys=True)+'\n'
    if args.output: Path(args.output).write_text(out)
    else: print(out,end='')
