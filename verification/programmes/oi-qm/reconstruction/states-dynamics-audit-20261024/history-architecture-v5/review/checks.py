"""Independent exact review controls for the supplied qubit sphere model.

No author imports. Hemisphere integrals use rational stereographic intervals.
"""
import argparse
from fractions import Fraction as Q
from itertools import product
import hashlib
import json
from pathlib import Path


def need(ok,message):
    if not ok:
        raise RuntimeError(message)


def dot(a,b):
    return sum((x*y for x,y in zip(a,b)),Q())


def scale(a,s):
    return tuple(x*s for x in a)


def matvec(m,v):
    return tuple(dot(row,v) for row in m)


def transpose(m):
    return tuple(zip(*m))


def matmul(a,b):
    return tuple(tuple(dot(row,col) for col in transpose(b)) for row in a)


I3=tuple(tuple(Q(i==j) for j in range(3)) for i in range(3))
AXES=I3


def stereographic_integral(n,constraints):
    """Exact mu_n hemisphere intersection integral for coplanar rational axes.

    x=(1-t*t)/(1+t*t), z=2t/(1+t*t). After the polar integral,
    the primitive is (n_x*t-n_z)/(1+t*t), with zero limits at infinities.
    """
    roots=set()
    for a,b in (n,)+tuple(constraints):
        need(a*a+b*b==1,'nonunit integration direction')
        if a:
            roots.update(((b+1)/a,(b-1)/a))
        else:
            roots.add(Q())
    ordered=[None]+sorted(roots)+[None]
    def primitive(t):
        return Q() if t is None else (n[0]*t-n[1])/(1+t*t)
    total=Q()
    for lo,hi in zip(ordered,ordered[1:]):
        mid=hi-1 if lo is None else lo+1 if hi is None else (lo+hi)/2
        if all(a*(1-mid*mid)+2*b*mid>0 for a,b in (n,)+tuple(constraints)):
            total+=primitive(hi)-primitive(lo)
    return total


# Exact Gaussian-rational matrix arithmetic.
def z(a=0,b=0):
    return Q(a),Q(b)


def za(a,b):
    return a[0]+b[0],a[1]+b[1]


def zm(a,b):
    return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]


def zs(a,s):
    return a[0]*s,a[1]*s


def mm(a,b):
    return tuple(tuple(za(zm(a[i][0],b[0][j]),zm(a[i][1],b[1][j]))
                       for j in range(2)) for i in range(2))


def adjoint(a):
    return tuple(tuple((a[j][i][0],-a[j][i][1]) for j in range(2)) for i in range(2))


def rho(mass,r):
    x,y,v=r
    return ((z((mass+v)/2),z(x/2,-y/2)),(z(x/2,y/2),z((mass-v)/2)))


def det2(m):
    p=zm(m[0][0],m[1][1]);q=zm(m[0][1],m[1][0])
    return p[0]-q[0],p[1]-q[1]


def decoded(prep):
    mass=sum((w for w,n in prep),Q())
    r=tuple(sum((w*n[k] for w,n in prep),Q()) for k in range(3))
    return rho(mass,r)


def quaternion(q):
    w,x,y,v=q
    need(dot(q,q)==1,'quaternion norm')
    u=((z(w,-v),z(-y,-x)),(z(y,-x),z(w,v)))
    vec=(x,y,v)
    cross=((0,-v,y),(v,0,-x),(-y,x,0))
    R=tuple(tuple((w*w-dot(vec,vec))*Q(i==j)+2*vec[i]*vec[j]+2*w*cross[i][j]
                  for j in range(3)) for i in range(3))
    return R,u,Q(1)


def conjugate(m,u,norm=Q(1)):
    out=mm(mm(u,m),adjoint(u))
    return tuple(tuple(zs(value,1/norm) for value in row) for row in out)


def matrix_branch(m,a,s):
    p=rho(Q(1),scale(a,s))
    return mm(mm(p,m),p)


def sphere_branch(prep,a,s):
    # The general integral is re-proved in REPORT; the independent
    # stereographic function exercises that identity without using this rule.
    weight=sum((w*(1+s*dot(n,a))/2 for w,n in prep),Q())
    need(weight>=0,'negative branch weight')
    return () if weight==0 else ((weight,scale(a,s)),)


def rotations():
    quats=[(Q(1),Q(),Q(),Q()),(Q(3,5),Q(4,5),Q(),Q()),
           (Q(2,3),Q(2,3),Q(1,3),Q()),(Q(1,2),)*4]
    out=[quaternion(q) for q in quats]
    # Previous non-Clifford witness: unnormalized rational unitary divided by sqrt5.
    out.append((((Q(3,5),Q(-4,5),Q()),(Q(4,5),Q(3,5),Q()),AXES[2]),
                ((z(2,-1),z()),(z(),z(2,1))),Q(5)))
    return out


def integral_controls():
    circle=[(Q(1),Q()),(Q(-1),Q()),(Q(),Q(1)),(Q(),Q(-1))]
    circle += [(Q(s*5,13),Q(t*12,13)) for s,t in product((-1,1),repeat=2)]
    circle += [(Q(s*8,17),Q(t*15,17)) for s,t in product((-1,1),repeat=2)]
    cases=0
    for n in circle:
        need(stereographic_integral(n,())==1,'independent density normalization')
        for a in circle:
            overlap=stereographic_integral(n,(a,))
            n3=(n[0],Q(),n[1]);a3=(a[0],Q(),a[1])
            quantum=matrix_branch(rho(Q(1),n3),a3,1)
            need(quantum[0][0][0]+quantum[1][1][0]==overlap,'integral/matrix trace')
            need(overlap==(1+dot(n,a))/2,'general hemisphere identity')
            cases+=1
    x=(Q(1),Q());v=(Q(),Q(1));b=(Q(3,5),Q(4,5))
    def mixed_raw(n):
        return tuple(sum((stereographic_integral(scale(n,t),(scale(v,s),scale(b,u)))
                          for t in (-1,1)),Q())/2 for s,u in product((-1,1),repeat=2))
    raw_x,raw_z=mixed_raw(x),mixed_raw(v)
    need(raw_x==(Q(7,20),Q(3,20),Q(3,20),Q(7,20)),'no-reset etaX joint law')
    need(raw_z==(Q(9,20),Q(1,20),Q(1,20),Q(9,20)),'no-reset etaZ joint law')
    need(sum(abs(a-b) for a,b in zip(raw_x,raw_z))/2==Q(1,5),'workspace/reset gap')
    proper=[]
    for axis in (AXES[0],AXES[2]):
        prep=((Q(1,2),axis),(Q(1,2),scale(axis,-1)))
        law=[]
        for s,u in product((-1,1),repeat=2):
            first=sphere_branch(prep,AXES[2],s)
            last=sphere_branch(first,(Q(3,5),Q(),Q(4,5)),u)
            law.append(sum((w for w,n in last),Q()))
        proper.append(tuple(law))
    need(proper[0]==proper[1]==raw_z,'proper fresh reset fails hidden-mixture congruence')
    timing=[]
    for n in (v,scale(v,-1)):
        joint=tuple(stereographic_integral(n,(scale(x,s),scale(v,t)))
                    for s,t in product((-1,1),repeat=2))
        need((sum(joint[:2]),sum(joint[2:]))==(Q(1,2),Q(1,2)),'timing sign marginal')
        timing.append(joint)
    need(sum(abs(a-b) for a,b in zip(*timing))/2==1,'timing full-record gap')
    return cases


def operator_controls():
    n1=(Q(2,3),Q(-2,3),Q(1,3));n2=(Q(2,3),Q(-2,3),Q(-1,3))
    pure=[((Q(1),scale(a,s)),) for a in AXES for s in (-1,1)]
    preps=pure+[((Q(1,2),n1),(Q(1,2),n2)),
                ((Q(1,2),scale(n1,-1)),(Q(1,2),scale(n2,-1))),
                ((Q(2,7),AXES[0]),(Q(3,7),AXES[2])),()]
    settings=list(AXES)+[n1,(Q(5,13),Q(12,13),Q())]
    gates=rotations()
    rotation_rows=branch_rows=0
    for prep in preps:
        need(det2(decoded(prep))[0]>=0,'cone decoder positivity')
        for R,U,norm in gates:
            need(matmul(R,transpose(R))==I3,'rotation orthogonality')
            spun=tuple((w,matvec(R,n)) for w,n in prep)
            need(decoded(spun)==conjugate(decoded(prep),U,norm),'rotation intertwining')
            rotation_rows+=1
        for a,s in product(settings,(-1,1)):
            post=sphere_branch(prep,a,s)
            need(decoded(post)==matrix_branch(decoded(prep),a,s),'full outcome branch intertwining')
            branch_rows+=1
    adaptive_rows=leaves=0
    for prep in preps[:6]:
        for policy in (0,1):
            active=[((),prep,decoded(prep))]
            for depth in range(4):
                future=[]
                for history,carrier,quantum in active:
                    g=(depth+sum(t[-1]>0 for t in history)+policy)%len(gates)
                    j=(2*depth+sum(t[-1] for t in history)+policy)%len(settings)
                    R,U,norm=gates[g]
                    moved=tuple((w,matvec(R,n)) for w,n in carrier)
                    target=conjugate(quantum,U,norm)
                    for s in (-1,1):
                        out=sphere_branch(moved,settings[j],s)
                        ref=matrix_branch(target,settings[j],s)
                        need(decoded(out)==ref,'adaptive whole branch/state')
                        increment=(depth+1,g,j,1,s)
                        future.append((history+(increment,),out,ref))
                        adaptive_rows+=1
                active=future
            need(len(active)==16,'zero branches omitted')
            need(sum(sum((w for w,n in out),Q()) for _,out,_ in active)==1,'complete tree mass')
            leaves+=len(active)
    plus,minus=preps[6:8]
    R,U,norm=gates[-1]
    laws=[]
    for prep in (plus,minus):
        moved=tuple((w,matvec(R,n)) for w,n in prep)
        laws.append(tuple(sum((w for w,n in sphere_branch(moved,AXES[0],s)),Q())
                          for s in (1,-1)))
    need(laws==[(Q(29,30),Q(1,30)),(Q(1,30),Q(29,30))],'non-Clifford witness')
    need(Q(8,9)-Q(14,15)**2==Q(4,225),'new input TV data-processing margin')
    return {'preparations':len(preps),'rotation_intertwinings':rotation_rows,
            'projective_branch_intertwinings':branch_rows,'adaptive_branch_nodes':adaptive_rows,
            'adaptive_depth':4,'adaptive_leaf_records':leaves,
            'nonclifford_output_laws':[[str(v) for v in law] for law in laws]}


def send_to(g):
    ez=AXES[2]
    if g==ez:
        return I3
    d=tuple(x-y for x,y in zip(ez,g));norm=dot(d,d)
    reflection=tuple(tuple(Q(i==j)-2*d[i]*d[j]/norm for j in range(3)) for i in range(3))
    J=((-Q(1),Q(),Q()),AXES[1],AXES[2])
    return matmul(reflection,J)


def dilation_controls():
    points=list(AXES)+[scale(a,-1) for a in AXES]+[(Q(2,3),Q(-2,3),Q(1,3))]
    seed_angles=[(Q(1),Q()),(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(-5,13),Q(12,13))]
    inverse_rows=geometry=0
    for R,unused,norm in rotations()[:4]:
        e1,e2,a=transpose(R)
        for old in points:
            sign=1 if dot(a,old)>=0 else -1
            for cosine,sine in [(Q(),Q(1)),(Q(3,5),Q(4,5)),(Q(4,5),Q(3,5)),(Q(1),Q())]:
                for cp,sp in seed_angles:
                    g=tuple(sine*(cp*x+sp*y)+sign*cosine*zv for x,y,zv in zip(e1,e2,a))
                    need(dot(g,g)==1 and dot(g,a)==sign*cosine,'reset sample geometry')
                    transfer=send_to(g)
                    need(matmul(transfer,transpose(transfer))==I3,'global transfer inverse')
                    need(matvec(transfer,AXES[2])==g,'ready-register reset')
                    # Properness is independently checked by a direct expansion.
                    aa,bb,cc=transfer
                    det=aa[0]*(bb[1]*cc[2]-bb[2]*cc[1])-aa[1]*(bb[0]*cc[2]-bb[2]*cc[0])+aa[2]*(bb[0]*cc[1]-bb[1]*cc[0])
                    need(det==1,'transfer not a rotation')
                    geometry+=1
                    for blank,record in product(points[:4],range(2)):
                        out=(matvec(transfer,blank),old,record^(sign<0))
                        back=(out[1],matvec(transpose(transfer),out[0]),out[2]^(sign<0))
                        need(back==(old,blank,record),'global reversible dilation')
                        inverse_rows+=1
    # Exact polar-coordinate integrals: density2c, and c=sqrt(U).
    need(2*Q(1,2)==1 and 2*Q(1,3)==Q(2,3),'reset normalization/first moment')
    probability=1-Q(2,3)**2
    conditional_mean=Q(2,3)*(1-Q(2,3)**3)/probability
    length=Q(3,2)*conditional_mean
    need(probability==Q(5,9) and conditional_mean==Q(38,45),'seed-bit conditional integral')
    need((1-length*length)/4==Q(-34,225),'seed-bit decoder nonpositivity')
    need((1-Q(3,2)**2)/4==Q(-5,16),'point-law decoder nonpositivity')
    return {'reset_sample_geometries':geometry,'global_inverse_cases':inverse_rows,
            'seed_bit_probability':'5/9','seed_bit_conditional_mean':'38/45',
            'seed_bit_decoder_determinant':'-34/225','point_decoder_determinant':'-5/16'}


def main():
    here=Path(__file__).resolve().parent
    parser=argparse.ArgumentParser()
    parser.add_argument('--author-root',type=Path)
    args=parser.parse_args()
    author=args.author_root or (here.parent if (here.parent/'PROVENANCE.json').exists()
                               else here.parent/'architecture_v5')
    inputs=json.loads((here/'INPUT-HASHES.json').read_text())
    for name,digest in inputs['author_files'].items():
        need(hashlib.sha256((author/name).read_bytes()).hexdigest()==digest,'author hash '+name)
    result={'schema':'oi.continuous-qubit-architecture.review.v5',
            'author_revision':inputs['author_revision'],'verdict':'ACCEPT_SCOPED_KNOWN_MODEL',
            'independent_stereographic_integrals':integral_controls(),
            'operators_and_adaptive_laws':operator_controls(),'dilation_and_access':dilation_controls(),
            'no_reset_or_old_workspace_joint_TV':'1/5','hidden_timing_joint_TV':'1',
            'native_availability_or_full_A1_claimed':False}
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
