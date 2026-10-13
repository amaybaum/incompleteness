#!/usr/bin/env python3
"""Exact certificates for the written spectrality screen, not a universal probe.

Exploratory, post-source design evidence. No native freeze or blind prediction.
Universal effect and decomposition arguments are in spectrality.md.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import sympy as s

R = s.Rational
I4 = s.eye(4)
checks = []


def clean(a):
    return a.applyfunc(s.simplify) if isinstance(a, s.MatrixBase) else s.simplify(a)


def check(name, statement):
    if not bool(statement):
        raise AssertionError(name)
    checks.append(name)


def projector(name, a, rank=1):
    check(name + ' Hermitian', a == a.H)
    check(name + ' idempotent', clean(a*a) == a)
    check(name + ' trace', s.trace(a) == rank)


def pairing(a, b):
    return s.simplify(s.trace(a*b))


def partial_transpose(a):
    return s.Matrix(4, 4, lambda i, j: a[2*(i//2)+j%2, 2*(j//2)+i%2])


def calculate(mutation):
    zero = s.Matrix([1, 0])
    u = s.Matrix([R(12, 13), R(5, 13)])
    if mutation == 'kb-distinguishable':
        u = s.Matrix([0, 1])
    p = s.kronecker_product(zero, zero)
    q = s.kronecker_product(u, u)
    pp, pq = p*p.H, q*q.H
    projector('KB first product', pp)
    projector('KB second product', pq)
    local_diff = u*u.H-zero*zero.H
    delta = s.sqrt(1-(zero.H*u)[0]**2)
    check('local trace-distance certificate', clean(local_diff**2) == delta**2*s.eye(2))
    check('local difference trace', s.trace(local_diff) == 0)
    check('KB distinguishability gap', 2*delta < 1)
    a, b = s.symbols('a b')
    product_matrix = s.Matrix(2, 2, list(a*p+b*q))
    check('only two product rays in support', s.factor(product_matrix.det()) == a*b*u[1]**2)
    support = s.Matrix.hstack(p, q)
    fkb = clean(I4-support*(support.H*support).inv()*support.H)
    projector('KB support complement', fkb, 2)
    bell = s.Matrix([1, 0, 0, 1])/s.sqrt(2)
    B = bell*bell.H
    check('Bell excluded from support', pairing(fkb, B) > 0)
    xkb = (pp+pq)/2
    check('KB witness rank two', xkb.rank() == 2)
    check('KB witness in support face', pairing(fkb, xkb) == 0)
    overlap = (p.H*q)[0]
    plus = (p+q)*(p+q).H/(2+2*overlap)
    minus = (p-q)*(p-q).H/(2-2*overlap)
    projector('quantum KB plus eigenstate', plus)
    projector('quantum KB minus eigenstate', minus)
    check('quantum KB eigenstates orthogonal', plus*minus == s.zeros(4))
    check('quantum KB spectral decomposition',
          clean((1+overlap)/2*plus+(1-overlap)/2*minus) == xkb)
    projector('quantum KB complement effect', clean(I4-plus-minus), 2)

    x, y, z = s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)
    defects = [(I4+sgn*s.kronecker_product(x, z)+t*s.kronecker_product(y, y)
                -sgn*t*s.kronecker_product(z, x))/16
               for sgn in (-1, 1) for t in (-1, 1)]
    normalized = [4*e for e in defects]
    pis = [I4/2-e for e in normalized]
    if mutation == 'zf-wrong-defect':
        pis[0] = I4/2+normalized[0]
    for j, pi in enumerate(pis):
        projector('ZF Bell projector '+str(j), pi)
    check('ZF Bell frame', sum(pis, s.zeros(4)) == I4)
    U = s.Matrix.hstack(*(2*pi[:, 0] for pi in pis))
    check('ZF actual Pauli-to-Bell coordinates', U.H*U == I4)
    v = s.Matrix([s.sqrt(3)/2, 1/(2*s.sqrt(3)), 1/(2*s.sqrt(3)), 1/(2*s.sqrt(3))])
    if mutation == 'zf-wrong-cap':
        v = s.Matrix([R(1, 2)]*4)
    w = s.sqrt(R(5, 14))*s.Matrix([0, 1, R(-3, 5)+R(4, 5)*s.I, R(-2, 5)-R(4, 5)*s.I])
    pv, pw = clean(U*v*v.H*U.H), clean(U*w*w.H*U.H)
    projector('ZF first support vector', pv)
    projector('ZF second support vector', pw)
    check('ZF support vectors orthogonal', pv*pw == s.zeros(4))
    support_projection = pv+pw
    fzf = I4-support_projection
    projector('ZF support complement', fzf, 2)
    rs = [pairing(pi, support_projection) for pi in pis]
    check('ZF strict one-cap inequalities', R(1, 2) < rs[0] < 1 and
          all(0 < r < R(1, 2) for r in rs[1:]))
    for j, (pi, defect) in enumerate(zip(pis, normalized)):
        check('ZF face excludes defect '+str(j), pairing(fzf, defect) == rs[j] > 0)
        compressed = clean(support_projection*pi*support_projection)
        check('ZF compressed Bell rank-one identity '+str(j), clean(compressed**2) == rs[j]*compressed)
    zfirst = clean(support_projection*normalized[0]*support_projection)
    check('ZF distinguished compression', zfirst == (R(1, 2)-rs[0])*pv+pw/2)
    weight = 1/(2*rs[0])
    xzf = clean(weight*pv+(1-weight)*pw)
    check('ZF witness normalization', s.trace(xzf) == 1)
    check('ZF witness rank two', xzf.rank() == 2)
    pairings = [pairing(e, xzf) for e in normalized]
    check('ZF witness in cut PSD base', pairings[0] == 0 and all(r > 0 for r in pairings[1:]))
    check('ZF witness exposed by two dual faces', pairing(fzf+normalized[0], xzf) == 0)
    t = s.symbols('t', nonnegative=True)
    lower = s.expand(weight*(1+t*(rs[0]-R(1, 2)))-(1-weight)*(1-t/2))
    check('ZF universal weighted-overlap gap', lower == (1+t)/3)
    projector('quantum ZF complement test', fzf, 2)
    quantum_input = normalized[0] if mutation == 'quantum-not-PSD' else xzf
    check('quantum positive comparison', all(r >= 0 for r in quantum_input.eigenvals()))
    check('quantum ZF measurement is complete', pv+pw+fzf == I4)

    classical = s.diag(R(1, 2), R(1, 3), R(1, 6), 0)
    coordinates = [s.diag(*(1 if k == j else 0 for k in range(4))) for j in range(4)]
    check('classical spectral preparation', sum((classical[j, j]*e for j, e in enumerate(coordinates)), s.zeros(4)) == classical)
    check('classical distinguishing measurement', all(pairing(e, f) == int(j == k)
          for j, e in enumerate(coordinates) for k, f in enumerate(coordinates)))
    check('co-quantum involution', partial_transpose(partial_transpose(B)) == B)
    check('co-quantum excludes quantum Bell state', partial_transpose(B).eigenvals().get(R(-1, 2)) == 1)
    check('co-quantum spectral measurement pairing', pairing(partial_transpose(plus), partial_transpose(minus)) == 0)
    check('co-quantum spectral decomposition', clean((1+overlap)/2*partial_transpose(plus)+
          (1-overlap)/2*partial_transpose(minus)) == partial_transpose(xkb))
    return {'controls': len(checks), 'kb_distance_bound': str(2*delta),
            'kb_Bell_support_gap': str(pairing(fkb, B)), 'zf_projection_weights': list(map(str, rs)),
            'zf_cut_pairings': list(map(str, pairings)), 'zf_weighted_overlap_lower': str(lower),
            'scope': 'exact certificates for written fixture exclusions; sourcing and preservation implication unresolved'}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mutation', choices=['kb-distinguishable', 'zf-wrong-defect', 'zf-wrong-cap', 'quantum-not-PSD'])
    args = ap.parse_args()
    result = calculate(args.mutation)
    if args.mutation:
        raise AssertionError('mutation unexpectedly survived')
    mutations = [('kb-distinguishable', 'KB distinguishability gap'),
                 ('zf-wrong-defect', 'ZF Bell projector 0 trace'),
                 ('zf-wrong-cap', 'ZF strict one-cap inequalities'),
                 ('quantum-not-PSD', 'quantum positive comparison')]
    for mode, failure in mutations:
        child = subprocess.run([sys.executable, '-I', '-B', str(Path(__file__).resolve()), '--mutation', mode], capture_output=True, text=True)
        if child.returncode == 0 or child.stdout or failure not in child.stderr:
            raise AssertionError('mutation control: '+mode)
    result['mutations_rejected'] = len(mutations)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
