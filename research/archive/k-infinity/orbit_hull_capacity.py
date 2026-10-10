"""Side probe: with FULL effects (all affine 0 <= e <= u), can a connected orbit-generated body have capacity 2 and a
flat boundary?  Answer: yes, and a lemma explains it.

Lemma (central symmetry bounds capacity).  Let Omega be a compact convex body, centrally symmetric about c
(Omega - c = c - Omega), with full effects.  If omega_1..omega_k are perfectly distinguishable (affine e_i >= 0,
sum e_i = u, e_i(omega_j) = delta_ij) then k <= 2.
Proof.  Write e_i = a_i + <B_i, x - c>.  e_i >= 0 on Omega and e_i has a zero on Omega force a_i = h(-B_i) = h(B_i),
h the support function (symmetric by central symmetry).  Then 1 = e_i(omega_i) = a_i + <B_i, omega_i - c> <= 2 a_i, so
a_i >= 1/2.  Summing, sum e_i = u gives sum a_i = 1, hence k <= 2.  QED

Instances (numerical LP as a control; each 'capacity-3 feasibility' LP relaxes nonnegativity to a sample of extreme
points, so infeasibility of the relaxation is a certificate of infeasibility):
  T  torus orbitope  = conv S^1 x S^1 in R^4  (connected abelian group SO(2)^2, transitive on the orbit; centrally
     symmetric; boundary contains the flat 2-face {s = 0} x disk)                      -> capacity 2, NOT strictly convex
  S  Stiefel orbitope = conv V_2(R^3) in R^{3x2} (connected NON-abelian SO(3), transitive; centrally symmetric; the
     face exposed by a rank-1 functional is a flat disk)                                -> capacity 2, NOT strictly convex
  C  Caratheodory orbitope C_2 = conv{(cos t, sin t, cos 2t, sin 2t)} (SO(2), transitive; NOT centrally symmetric)
                                                                                         -> capacity 3 (positive control)
  B  the 3-ball (SO(3), centrally symmetric, strictly convex)                             -> capacity 2 (control)
"""
import numpy as np
from scipy.optimize import linprog
rng=np.random.default_rng(11)
def torus(n):  s,t=rng.uniform(0,2*np.pi,(2,n)); return np.c_[np.cos(s),np.sin(s),np.cos(t),np.sin(t)]
def torus_pt(s,t): return np.array([np.cos(s),np.sin(s),np.cos(t),np.sin(t)])
def stiefel(n):
    out=[]
    for _ in range(n):
        Q,_=np.linalg.qr(rng.normal(size=(3,3))); out.append(Q[:,:2].reshape(-1))
    return np.array(out)
def cara(n):  t=rng.uniform(0,2*np.pi,n); return np.c_[np.cos(t),np.sin(t),np.cos(2*t),np.sin(2*t)]
def cara_pt(t): return np.array([np.cos(t),np.sin(t),np.cos(2*t),np.sin(2*t)])
def ball(n):  v=rng.normal(size=(n,3)); return v/np.linalg.norm(v,axis=1)[:,None]
def cap3_feasible(samples, triple):
    """LP: affine e_i = c_i0 + c_i.x, i=1..3; e_i(x_m) >= 0 on samples; e_i(w_j) = delta_ij; sum_i e_i = 1."""
    d=samples.shape[1]; nv=3*(d+1)
    def row(i,x):
        r=np.zeros(nv); r[i*(d+1)]=1; r[i*(d+1)+1:(i+1)*(d+1)]=x; return r
    A_ub=[]; b_ub=[]
    for i in range(3):
        for x in samples: A_ub.append(-row(i,x)); b_ub.append(0)
    A_eq=[]; b_eq=[]
    for i in range(3):
        for j,w in enumerate(triple): A_eq.append(row(i,w)); b_eq.append(1.0 if i==j else 0.0)
    for k in range(d+1):
        r=np.zeros(nv); r[[i*(d+1)+k for i in range(3)]]=1; A_eq.append(r); b_eq.append(1.0 if k==0 else 0.0)
    res=linprog(np.zeros(nv),A_ub=np.array(A_ub),b_ub=np.array(b_ub),A_eq=np.array(A_eq),b_eq=np.array(b_eq),bounds=[(None,None)]*nv,method='highs')
    return res.status==0
bodies={'T torus':(torus(4000),[np.array([torus_pt(*p) for p in rng.uniform(0,2*np.pi,(3,2))]) for _ in range(30)]),
        'S Stiefel':(stiefel(6000),[stiefel(3) for _ in range(30)]),
        'C Caratheodory':(cara(4000),[np.array([cara_pt(0),cara_pt(2*np.pi/3),cara_pt(4*np.pi/3)])]+[np.array([cara_pt(t) for t in rng.uniform(0,2*np.pi,3)]) for _ in range(10)]),
        'B ball':(ball(4000),[ball(3) for _ in range(30)])}
for name,(S,triples) in bodies.items():
    feas=[cap3_feasible(S,tr) for tr in triples]
    print('%-16s capacity-3 LP feasible for %d of %d triples' % (name,sum(feas),len(feas)))
# flat boundary certificates
e=lambda x:(1+x[0])/2                                    # torus: e = (1 + cos s)/2, a valid effect (0..1 on the body)
p1,p2=torus_pt(0,0),torus_pt(0,np.pi/2); m=(p1+p2)/2
print('torus: e(p1)=%.3f e(p2)=%.3f e(mid)=%.3f -> the midpoint is a boundary point (e = 1) and not extreme: flat face' % (e(p1),e(p2),e(m)))
u=np.array([1,0,0.]); v=np.array([1,0.]); A1=np.array([[1,0],[0,1],[0,0.]]); A2=np.array([[1,0],[0,0],[0,1.]])
eS=lambda A:(1+u@A@v)/2                                  # Stiefel: rank-1 exposing functional, valid (nuclear norm 1/2)
print('Stiefel: e(A1)=%.3f e(A2)=%.3f e(mid)=%.3f, mid has singular values %s -> boundary, not extreme: flat face' % (eS(A1),eS(A2),eS((A1+A2)/2),np.round(np.linalg.svd((A1+A2)/2,compute_uv=False),3)))
