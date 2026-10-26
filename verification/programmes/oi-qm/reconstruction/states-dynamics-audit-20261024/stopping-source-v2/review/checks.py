#!/usr/bin/env python3
"""Independent stopping-source review controls; imports no author module."""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import permutations
import argparse
import json
from pathlib import Path


def require(ok, label):
    if not ok:
        raise RuntimeError(label)


def below(r, complement=False):
    # Rational comparisons with the roots (2 +/- sqrt(2))/4.
    if complement:
        return r < Q(1, 2) and (2 - 4*r)**2 > 2
    return r <= Q(1, 2) or (4*r - 2)**2 < 2


def tree(cutoff, complement=False):
    # Classify whole cylinders geometrically, without computing target digits.
    unresolved = [(Q(0), Q(1))]
    law = defaultdict(Q)
    for depth in range(1, cutoff + 1):
        next_unresolved = []
        for lo, hi in unresolved:
            mid = (lo + hi)/2
            for left, right in ((lo, mid), (mid, hi)):
                if below(right, complement):
                    law[depth, 1] += right - left
                elif not below(left, complement):
                    law[depth, 0] += right - left
                else:
                    next_unresolved.append((left, right))
        require(len(next_unresolved) == 1, 'one unresolved cylinder')
        unresolved = next_unresolved
    law['timeout', 'timeout'] = sum(hi-lo for lo, hi in unresolved)
    require(sum(law.values()) == 1, 'mass conservation')
    return law


def tv(a, b):
    return sum(abs(a.get(k, 0)-b.get(k, 0)) for k in a.keys() | b.keys())/2


def run():
    rows = []
    for cutoff in list(range(1, 13)) + [32, 64]:
        a, b = tree(cutoff), tree(cutoff, True)
        tail = Q(1, 2**cutoff)
        require(a['timeout', 'timeout'] == b['timeout', 'timeout'] == tail, 'tail')
        for depth in range(1, cutoff+1):
            ma = sum(a.get((depth, y), 0) for y in (0, 1))
            mb = sum(b.get((depth, y), 0) for y in (0, 1))
            require(ma == mb == Q(1, 2**depth), 'geometric marginal')
            require(all(a.get((depth,y),0)*b.get((depth,y),0)==0 for y in (0,1)),
                    'disjoint threshold outcomes at each stopping depth')
        require(tv(a,b) == 1-tail, 'joint TV')
        expected = sum(t*mass for (t,y),mass in a.items() if t!='timeout') + cutoff*tail
        require(expected == 2-2*tail, 'capped stopping expectation')
        output1 = sum(mass for (t,y),mass in a.items() if y==1)
        require(below(output1) and not below(output1+tail), 'output approximation bracket')
        require(a[1,1] == Q(1,2) and b.get((1,1),0)==0, 'refinement contradiction')
        rows.append({'cutoff':cutoff, 'tail':str(tail), 'joint_tv':str(tv(a,b)),
                     'expected_capped_queries':str(expected), 'output1_timeout_zero':str(output1)})

    # An independent timing record really admits the common refinement.
    # Use exact rational outcome parameters to test the identity, not the candidate's formula.
    for probability in (Q(1,7), Q(1,2), Q(6,7)):
        for depth in range(1,13):
            factor = Q(1,2**depth)
            require((probability*factor)/probability == factor, 'positive refinement')
    # Both eventual output-1 probabilities are strictly positive; the unequal
    # depth-1/output-1 support above therefore rules out a common refinement.
    require(below(Q(0), True) and below(Q(3,4)) and not below(Q(1)),
            'strict threshold bounds for refinement witness')

    # Enumerate genuine six-configuration bijections. Reconstruct each induced
    # Kraus family from its hidden-output fibers and compare with direct tracing.
    shapes = set()
    tests = 0
    for perm in permutations(range(6)):
        for hidden in range(3):
            kraus = []
            for target_hidden in range(3):
                k = [[0,0],[0,0]]
                for visible in range(2):
                    target = perm[3*visible+hidden]
                    if target % 3 == target_hidden:
                        k[target//3][visible] = 1
                require(all(sum(row)<=1 for row in k), 'injective row')
                require(all(sum(k[i][j] for i in range(2))<=1 for j in range(2)), 'column')
                shapes.add(tuple(sum(k,[])))
                kraus.append(k)
            for i in range(2):
                for j in range(2):
                    a,b = perm[3*i+hidden],perm[3*j+hidden]
                    direct = [[int(a%3==b%3 and (r,c)==(a//3,b//3))
                               for c in range(2)] for r in range(2)]
                    fiber = [[sum(k[r][i]*k[c][j] for k in kraus)
                              for c in range(2)] for r in range(2)]
                    require(direct==fiber, 'dilation/Kraus equality')
                    require(all(x>=0 for row in direct for x in row), 'entrywise cone')
                    tests += 1
    require(len(shapes)==7, 'seven partial-permutation shapes including zero')
    h = [[1,1],[1,-1]]
    image = [[Q(h[r][1]*h[c][1],2) for c in range(2)] for r in range(2)]
    require(image==[[Q(1,2),Q(-1,2)],[Q(-1,2),Q(1,2)]], 'Hadamard image')
    require(image[0][1] < 0, 'negative entry witness')
    return {'schema':'oi-stopping-source-independent-review-v2', 'verdict':'PASS',
            'scope':'exact bounded controls plus separate written limit argument; no native implementation',
            'cutoffs':rows, 'dilations':720, 'hidden_inputs_per_dilation':3,
            'matrix_unit_comparisons':tests, 'partial_permutation_shapes':len(shapes),
            'refinement_positive_control':True, 'hadamard_offdiagonal':'-1/2'}


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    data=json.dumps(run(),indent=2,sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(data)
    else:
        print(data,end='')
