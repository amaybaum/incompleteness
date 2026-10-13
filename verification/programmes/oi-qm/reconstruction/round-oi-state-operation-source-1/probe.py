#!/usr/bin/env python3
"""Design probe: local test/update consistency versus pair-cone preservation.

Exact SymPy arithmetic. Universal cone and duality arguments are separately
written; finite controls do not certify those arguments. No physical source is
inferred from these computations. --mutation cases must fail a named control.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import argparse
import json
import sympy as s

parser = argparse.ArgumentParser()
parser.add_argument('--mutation', choices=['identity', 'phase', 'unnormalized', 'positive_control'])
args = parser.parse_args()
Q, I = s.Rational, s.I
checks = []


def check(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    checks.append(name)


def clean(m):
    return m.applyfunc(s.simplify)


def same(a, b):
    return clean(a-b) == s.zeros(*a.shape)


def pair(a, b):
    return s.simplify(s.trace(a*b))


def positive2(a):
    return same(a.H, a) and a[0,0].is_nonnegative and a[1,1].is_nonnegative and s.det(a).is_nonnegative


def projector(v):
    v = s.Matrix(v)
    return clean(v*v.H/(v.H*v)[0])


root = Path(__file__).resolve().parents[5]
source = root/'verification/lean-mathlib/OIBridge/BridgeFiniteProtocol.lean'
check('actual adopted circuit source', sha256(source.read_bytes()).hexdigest() ==
      '9ae957839f49f57222bb968741d04b17496d2d355a47ab7918b0b6149d8aaba8')
pauli = [s.eye(2), s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-I],[I,0]]), s.diag(1,-1)]
X,Y,Z = pauli[1:]
kron = s.kronecker_product
D = s.diag(1, Q(3,5)+Q(4,5)*I)
H = s.Matrix([[1,1],[1,-1]])
hh = kron(s.eye(2), H, H)/2
toffoli = s.zeros(8)
for j in range(8):
    toffoli[j ^ 4 if j % 4 == 3 else j,j] = 1
u = hh*toffoli*kron(s.diag(1,I),s.eye(4))*toffoli*hh
check('independently composed circuit isometry', same(u.H*u,s.eye(8)))
ks=[]
for j in range(4):
    correction = s.diag(1,1 if j==0 else -1)
    ks.append(correction*s.Matrix(2,2,lambda a,b:u[4*a+j,4*b]))
check('actual branch normalization', same(sum((k.H*k for k in ks),s.zeros(2)),s.eye(2)))
for a,b in product(range(2),repeat=2):
    e=s.zeros(2);e[a,b]=1
    check('success branch '+str((a,b)), same(ks[0]*e*ks[0].H,Q(5,8)*D*e*D.H))
    for j in range(1,4):
        check('failure branch '+str((j,a,b)), same(ks[j]*e*ks[j].H,e/8))


def phi(a):
    if args.mutation=='identity':
        return a
    return clean(sum((kron(s.eye(2),k)*a*kron(s.eye(2),k.H) for k in ks),s.zeros(4)))


B=s.zeros(4)
for a,b in product((0,3),repeat=2):B[a,b]=Q(1,2)
P=s.zeros(4);P[1,1]=P[2,2]=Q(1,2);P[1,2]=I/2;P[2,1]=-I/2
W=s.Matrix(4,4,lambda a,b:P[2*(a//2)+b%2,2*(b//2)+a%2])
if args.mutation=='phase':W=W.conjugate()
es=[(s.eye(4)+a*kron(X,Z)+b*kron(Y,Y)-a*b*kron(Z,X))/16
    for a,b in product((-1,1),repeat=2)]
T=projector((1,-I,1,I))
check('Bell generator and dual zero', same(B*B,B) and s.trace(B)==1 and pair(W,B)==0)
check('ZF dual PSD projector', same(T*T,T) and s.trace(T)==1)
check('ZF dual generator inequalities', [pair(T,e) for e in es]==[0,0,Q(1,8),Q(1,8)])
separators=[pair(W,phi(B)),pair(T,phi(es[1]))]
check('uniform protocol negative witnesses', all(x.is_negative for x in separators))

# Phi_1 is itself a one-token operation with the other token idle.
def token_phi(a):
    return clean(sum((k*a*k.H for k in ks),s.zeros(2)))
for r,c in product(range(4),repeat=2):
    left=s.zeros(2);left[r//2,c//2]=1
    right=s.zeros(2);right[r%2,c%2]=1
    check('single-token factorization '+str((r,c)),same(phi(kron(left,right)),kron(left,token_phi(right))))

# Symbolic identities supply the inputs to the universal Cauchy-Schwarz proof.
a=s.symbols('a1:4',real=True);b=s.symbols('b1:4',real=True)
rho=(s.eye(2)+sum((a[j]*pauli[j+1] for j in range(3)),s.zeros(2)))/2
tau=(s.eye(2)+sum((b[j]*pauli[j+1] for j in range(3)),s.zeros(2)))/2
check('KB symbolic whole-product identity', pair(W,kron(rho,tau)) ==
      s.expand((1-a[0]*b[1]-a[1]*b[0]-a[2]*b[2])/4))
for j,(c,d) in enumerate(product((-1,1),repeat=2)):
    check('ZF symbolic whole-product identity '+str(j), pair(es[j],kron(rho,tau)) ==
          s.expand((1+c*a[0]*b[2]+d*a[1]*b[1]-c*d*a[2]*b[0])/16))

frames=[projector(v) for v in [(1,0),(0,1),(1,1),(1,-1),(1,I),(1,-I),(3,4),(3,4*I)]]
if args.mutation=='unnormalized':frames[-1]*=2
for j,p in enumerate(frames):
    check('normalized sharp frame '+str(j), same(p*p,p) and s.trace(p)==1)

# Both cone generators are admitted states at their stated scaling. Every
# product readout remains valid although the protocol output leaves that cone.
fixtures=[B]+es
readout_cases=filter_cases=0
for j,a0 in enumerate(fixtures):
    for tag,a1 in [('input',a0),('protocol-output',phi(a0))]:
        for p,q in product(frames,repeat=2):
            val=pair(kron(p,q),a1)
            check('product probability '+str((j,tag,readout_cases)),val.is_nonnegative)
            readout_cases+=1
        for side in (0,1):
            for f,p in enumerate(frames):
                norms=[]
                for branch,pp in enumerate((p,s.eye(2)-p)):
                    op=kron(pp,s.eye(2)) if side==0 else kron(s.eye(2),pp)
                    out=clean(op*a1*op.H)
                    if side==0:
                        marginal=s.Matrix(2,2,lambda r,c:sum(out[2*h+r,2*h+c] for h in range(2)))
                        expected=kron(pp,marginal)
                    else:
                        marginal=s.Matrix(2,2,lambda r,c:sum(out[2*r+h,2*c+h] for h in range(2)))
                        expected=kron(marginal,pp)
                    check('conditional product '+str((j,tag,side,f,branch)),same(out,expected) and positive2(marginal))
                    norms.append(s.simplify(s.trace(out)))
                    filter_cases+=1
                check('conditional outcome normalization '+str((j,tag,side,f)),sum(norms)==s.trace(a1))

# Independently specified quantum PSD and classical diagonal comparisons.
quantum=[projector(v) for v in [(1,0,0,0),(0,1,0,0),(1,0,0,1),(1,-I,1,I)]]
if args.mutation=='positive_control':quantum.append(es[-1])
quantum_ok=all(same(q.H,q) and all(ev.is_nonnegative for ev in q.eigenvals()) and
               same(phi(q).H,phi(q)) and all(ev.is_nonnegative for ev in phi(q).eigenvals()) for q in quantum)
check('quantum PSD positive control',quantum_ok)
classical=[s.diag(*[int(j==k) for j in range(4)]) for k in range(4)]
classical_protocol=all(same(phi(q),q) for q in classical)
check('actual protocol fixes the classical diagonal basis',classical_protocol)
coordinate=[s.diag(1,0),s.diag(0,1)]
classical_filters=True
for side,p,q in product((0,1),coordinate,classical):
    op=kron(p,s.eye(2)) if side==0 else kron(s.eye(2),p)
    out=clean(op*q*op)
    classical_filters &= all(out[r,c]==0 for r in range(4) for c in range(4) if r!=c)
    classical_filters &= all(out[r,r].is_nonnegative for r in range(4))
check('classical native local filters preserve the diagonal cone',classical_filters)
classical_tests=[kron(p,q) for p,q in product(coordinate,repeat=2)]
coordinates=s.symbols('d0:4',real=True)
diagonal=s.diag(*coordinates)
classical_saturation=(classical_tests==classical and
                      [pair(t,diagonal) for t in classical_tests]==list(coordinates))
check('classical product tests saturate exactly to the nonnegative diagonal cone',classical_saturation)
classical_dual=all(same(clean(sum((kron(s.eye(2),k.H)*t*kron(s.eye(2),k) for k in ks),s.zeros(4))),t)
                  for t in classical_tests)
check('actual protocol fixes the classical complete dual-test basis',classical_dual)
classical_ok=classical_protocol and classical_filters and classical_saturation and classical_dual
check('classical comparisons bear on the candidate readings',classical_ok)

# Product-test saturation selects maxCone, which contains an indefinite defect
# and excludes the quantum PSD comparison as a saturation model.
indefinite=es[-1]
check('saturation countercontrol is not PSD',any(ev.is_negative for ev in indefinite.eigenvals()))
pure=(s.eye(4)-8*indefinite)/2
check('fullClass inclusion confound: omitted quantum projector',
      same(pure*pure,pure) and s.trace(pure)==1 and pair(indefinite,pure).is_negative)
check('defects pairwise nonnegative for universal confound proof',
      all(pair(e,f).is_nonnegative for e,f in product(es,repeat=2)))

print(json.dumps({
    'controls':len(checks),'readout_cases':readout_cases,'filter_cases':filter_cases,
    'uniform_phi1_separators':[str(x) for x in separators],
    'witness_operation':'Phi1',
    'availability_theorem':'finite_protocol_spectator',
    'P1_local_consistency':'INSUFFICIENT: restricted rank-one filter/readout consistency holds while cone preservation fails',
    'LO_available_local_operations':'Phi1 is a one-token operation; general local-operation preservation asserts the target directly',
    'P2_complete_dual_tests':'both fixture pullback clauses violated; universal disguise classification is written evidence',
    'P3_product_saturation':'fails the quantum PSD positive control; universal Q3-inclusion consequence is written evidence',
    'quantum_positive':bool(quantum_ok),'classical_positive':bool(classical_ok),
    'classical_protocol_fixed':bool(classical_protocol),
    'classical_filters':bool(classical_filters),
    'classical_product_saturation':bool(classical_saturation),
    'classical_dual_pullbacks':bool(classical_dual),
    'scope':'exact instances plus symbolic identities; universal arguments and physical source statuses remain separate'
},sort_keys=True,indent=2))
