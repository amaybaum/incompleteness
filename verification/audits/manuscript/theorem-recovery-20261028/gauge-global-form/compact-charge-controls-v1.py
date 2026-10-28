#!/usr/bin/env python3
"""Exact compact-vs-unquantized controls; no imports from author candidates.

The general compact theorem uses the credited classical exponent-3 Fermat
theorem. These coefficient/finite checks are not a substitute for it.
"""
from itertools import product
from pathlib import Path
import hashlib
import json

def anomalies(a,u,d,l,e):
    return (2*a-u-d,3*a+l,6*a-3*u-3*d+2*l-e,
            6*a**3-3*u**3-3*d**3+2*l**3-e**3)

def polynomial_multiply(p,q):
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):out[i+j]+=x*y
    return out
def cube(p):return polynomial_multiply(polynomial_multiply(p,p),p)

plus,minus=cube([3,1]),cube([3,-1])
curve_coefficients=[x+y for x,y in zip(plus,minus)]
if curve_coefficients != [54,0,18,0]:
    raise RuntimeError('Fermat coordinate coefficient identity failed')

# Original integer gauge-anomaly equations ONLY: deliberately do not assume G.
assignments=0
solutions=[]
for a,u,d,l,e in product(range(-6,7),repeat=5):
    C,W,G,A=anomalies(a,u,d,l,e)
    actual=(C==W==A==0)
    expected=((a==0 and d==-u and l==e==0) or
              (a!=0 and l==-3*a and e==-6*a and
               (u,d) in ((4*a,-2*a),(-2*a,4*a))))
    if actual!=expected:
        raise RuntimeError('compact finite classification mismatch')
    if actual:
        if G!=0:raise RuntimeError('integer gauge solution has nonzero G')
        solutions.append((a,u,d,l,e))
    assignments+=1
if assignments!=371293 or len(solutions)!=17:
    raise RuntimeError('compact finite grid coverage mismatch')

# Exact Q[r]/(r^3-2), represented in basis (1,r,r^2), with no floating point.
def alg_add(*vectors):return tuple(sum(v[i] for v in vectors) for i in range(3))
def alg_scale(k,v):return tuple(k*x for x in v)
def alg_mul(v,w):
    out=[0,0,0]
    for i,x in enumerate(v):
        for j,y in enumerate(w):
            power=i+j
            out[power if power<3 else power-3]+=x*y*(1 if power<3 else 2)
    return tuple(out)
def alg_cube(v):return alg_mul(alg_mul(v,v),v)
one=(1,0,0);r=(0,1,0)
a=u=d=one;l=alg_scale(-3,one);e=alg_scale(-3,r)
C=alg_add(alg_scale(2,a),alg_scale(-1,u),alg_scale(-1,d))
W=alg_add(alg_scale(3,a),l)
G=alg_add(alg_scale(6,a),alg_scale(-3,u),alg_scale(-3,d),alg_scale(2,l),alg_scale(-1,e))
A=alg_add(alg_scale(6,alg_cube(a)),alg_scale(-3,alg_cube(u)),
          alg_scale(-3,alg_cube(d)),alg_scale(2,alg_cube(l)),alg_scale(-1,alg_cube(e)))
if C!=W or C!=A or C!=(0,0,0) or G!=(-6,3,0):
    raise RuntimeError('unquantized algebraic countercontrol failed')
if alg_cube(r)!=(2,0,0):raise RuntimeError('algebraic arithmetic setup failed')

report={
    'schema':1,'status':'PASS','arithmetic':'exact integer coefficients and algebraic reduction; no floats',
    'Fermat_transform_sum_cube_coefficients':curve_coefficients,
    'compact_gauge_only_grid':{'bound':6,'assignments':assignments,'solutions':solutions,
                              'solution_count':len(solutions),'all_have_G_zero':True,
                              'G_was_not_assumed':True},
    'unquantized_real_countercontrol':{'r_relation':'r^3=2, r positive real',
                                      'charges':['1','1','1','-3','-3r'],
                                      'CWA_coefficients':[list(C),list(W),list(A)],
                                      'G_coefficients':list(G),'G_nonzero_argument':'G=0 would force r=2, contradicting r^3=2'},
    'universal_proof_dependency':'Classical exponent-3 Fermat theorem, credited in the frozen supplement; not proved by the finite grid or claimed Lean-proved',
    'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({'status':'PASS','output':str(out),'assignments':assignments,'solutions':len(solutions)}))
