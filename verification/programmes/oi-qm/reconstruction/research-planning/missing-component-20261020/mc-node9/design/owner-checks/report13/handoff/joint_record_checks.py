#!/usr/bin/env python3
"""Exploratory exact joint-record diagnostics; standard library, no file writes.

This checks a conditional kinematic model, NOT a native OI apparatus.
No randomness, network, repository imports, or acceptance tolerance.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import comb


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def depth_size(n):
    return 1 << (9*n-1).bit_length()


def old_rates(n):
    # Original fixed-laboratory velocity law, independently summed.
    sx = sr = 0
    for i in range(n+1):
        x = 2*i-n
        for j in range(n+1):
            y = 2*j-n
            weight = comb(n, i)*comb(n, j)
            sx += weight*max(5*x, 0)
            sr += weight*max(4*x+3*y, 0)
    denominator = depth_size(n)*4**n
    return F(sx, denominator), F(sr, denominator)


def geometric_tv(p, q, m):
    # Independent formula: monotone likelihood ratio gives a prefix event.
    require(p >= q > 0, 'rate ordering')
    fp, fq = 1-p, 1-q
    prefix = max(fq**j-fp**j for j in range(1, m+1))
    direct = (abs(fp**m-fq**m) + sum(
        abs(p*fp**j-q*fq**j) for j in range(m)))/2
    require(prefix == direct, 'geometric prefix/sum disagreement')
    return prefix


def rotated_counts(n):
    # S_z is integrated out. Normal projection is 5*S_x at every station.
    # h[t] counts successful (S_x,S_y,D); k[t] also requires R's X read = +.
    h, k = Counter(), Counter()
    for i in range(n+1):
        x = 2*i-n
        if x <= 0:
            continue
        wx = comb(n, i)
        positive_y = sum(comb(n, j) for j in range(n+1)
                         if 4*x-3*(2*j-n) > 0)
        for d in range(1, 5*x+1):
            t = F(d, 5*x)
            h[t] += wx*2**n
            k[t] += wx*positive_y
    return h, k


LABELS = ('X+', 'X-', 'Y+', 'Y-', 'Z+', 'Z-', 'R+', 'R-')
AXES5 = {'X': (5, 0, 0), 'Y': (0, 5, 0), 'Z': (0, 0, 5),
         'R': (4, 3, 0)}


def direct_microstates(n):
    # Separate path: all 3*n bits, all depths, actual lab components,
    # direct dot product with the oriented plane, and a terminal X read.
    laws = {s: Counter() for s in LABELS}
    for bits in product((-1, 1), repeat=3*n):
        x, y, z = (sum(bits[i*n:(i+1)*n]) for i in range(3))
        base = {'X': (5*x, 5*y, 5*z), 'Y': (-5*y, 5*x, 5*z),
                'Z': (-5*z, 5*y, 5*x), 'R': (4*x-3*y, 3*x+4*y, 5*z)}
        for label in LABELS:
            sign = 1 if label[-1] == '+' else -1
            axis = tuple(sign*a for a in AXES5[label[0]])
            velocity = tuple(sign*v for v in base[label[0]])
            dot = sum(a*v for a, v in zip(axis, velocity))
            require(dot % 5 == 0, 'noninteger normal projection')
            normal = dot//5
            require(normal == 5*x, 'rotation failed to preserve normal speed')
            for depth in range(1, depth_size(n)+1):
                if 0 < depth <= normal:
                    require(velocity[0] != 0, 'readout tie')
                    key = (F(depth, normal), velocity[0] > 0)
                else:
                    key = None
                laws[label][key] += 1
    return laws


def mix(laws, weights):
    result = Counter()
    for label, weight in weights.items():
        for record, count in laws[label].items():
            result[record] += weight*count
    return result


A = {'R+': F(13, 16), 'R-': F(3, 16)}
B = {'X+': F(1, 2), 'Y+': F(3, 8), 'Z+': F(1, 16), 'Z-': F(1, 16)}


def rank(rows):
    a = [[F(x) for x in row] for row in rows]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][c]
        a[r] = [x/d for x in a[r]]
        for i in range(len(a)):
            if i != r:
                d = a[i][c]
                a[i] = [x-d*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


RELATIONS = (
    (1, 1, -1, -1, 0, 0, 0, 0),
    (1, 1, 0, 0, -1, -1, 0, 0),
    (1, 1, 0, 0, 0, 0, -1, -1),
    (-4, 4, -3, 3, 0, 0, 5, -5),
)


def affine_checks(laws):
    coords = []
    for label in LABELS:
        sign = 1 if label[-1] == '+' else -1
        coords.append((F(1),)+tuple(F(sign*v, 5) for v in AXES5[label[0]]))
    matrix = list(zip(*coords))
    require(rank(matrix) == rank(RELATIONS) == 4, 'affine ranks')
    for row in RELATIONS:
        require(all(sum(c*x for c, x in zip(row, coordinate)) == 0
                    for coordinate in matrix), 'relation outside nullspace')
    ar = tuple(sum(A.get(s, 0)*coords[i][j] for i, s in enumerate(LABELS))
               for j in range(4))
    br = tuple(sum(B.get(s, 0)*coords[i][j] for i, s in enumerate(LABELS))
               for j in range(4))
    require(ar == br == (1, F(1, 2), F(3, 8), 0), 'reference states differ')
    require(all(16*v == int(16*v) for weights in (A, B) for v in weights.values()),
            'preparation coin is not four fair bits')
    # Positive control: every exact quantum menu effect satisfies all rows.
    for axis in AXES5.values():
        for sign in (-1, 1):
            probabilities = [(1+sign*sum(F(a, 5)*v for a, v in
                                         zip(axis, c[1:])))/2 for c in coords]
            require(all(sum(a*p for a, p in zip(row, probabilities)) == 0
                        for row in RELATIONS), 'quantum positive control')
    keys = set().union(*(set(law) for law in laws.values()))
    for row in RELATIONS[:3]:
        require(all(sum(c*laws[s][key] for c, s in zip(row, LABELS)) == 0
                    for key in keys), 'antipodal mixture equality failed')
    require(any(sum(c*laws[s][key] for c, s in zip(RELATIONS[3], LABELS)) != 0
                for key in keys), 'missing fourth-relation countercontrol')


def clock_bound_checks():
    cases = 0
    for n in (1, 3, 15, 63):
        for bins in (1, 2, 16):
            norm = direct = residue = positive = 0
            for i in range(n+1):
                x = 2*i-n
                if x <= 0:
                    continue
                weight, p = comb(n, i), 5*x
                norm += weight*p
                positive += weight
                counts = Counter((bins*d+p-1)//p for d in range(1, p+1))
                direct += weight*sum(abs(F(counts[j])-F(p, bins))
                                     for j in range(1, bins+1))
                r = p % bins
                residue += weight*F(r*(bins-r), bins)
            actual, formula = direct/(2*norm), residue/norm
            upper = F(bins*positive, 4*norm)
            require(actual == formula <= upper, 'finite-clock joint bound')
            require(positive == 2**(n-1), 'central symmetry count')
            if bins == 1:
                require(actual == 0, 'one-bin clock is not independent')
            cases += 1
    print('Finite-bin joint clock/velocity TV: direct depth counts = residue formula <= bound, %d cases PASS' % cases)


def main():
    print('Joint-record diagnostic v1: exploratory exact arithmetic; NOT apparatus acceptance')
    print('Original candidate: censored geometric TV, prefix event = direct sum (m=256)')
    for n in (7, 15, 31, 63, 127):
        p, q = old_rates(n)
        tv = geometric_tv(p, q, 256)
        print('n=%d pX=%.12f pR=%.12f TV=%.12f' % (n, float(p), float(q), float(tv)))
    for n in (1, 3):
        laws = direct_microstates(n)
        denominator = depth_size(n)*8**n
        require(all(sum(law.values()) == denominator for law in laws.values()), 'normalization')
        heralds = []
        for law in laws.values():
            herald = Counter()
            for record, count in law.items():
                herald[None if record is None else record[0]] += count
            heralds.append(herald)
        require(all(h == heralds[0] for h in heralds), 'herald marginals differ')
        h, k = rotated_counts(n)
        require({t: laws['R+'][(t, True)] for t in h} ==
                {t: count*2**n for t, count in k.items()}, 'R plus count mismatch')
        require({t: heralds[0][t] for t in h} ==
                {t: count*2**n for t, count in h.items()}, 'herald count mismatch')
        la, lb = mix(laws, A), mix(laws, B)
        actual = sum(abs(la[key]-lb[key]) for key in set(la)|set(lb))/(2*denominator)
        formula = F(sum(abs(10*k[t]-9*h[t]) for t in h), 16*depth_size(n)*4**n)
        require(actual == formula, 'direct/aggregated joint TV differs')
        affine_checks(laws)
    print('Direct 3D bit/depth enumeration n=1,3: normalization, rotations, herald equality, joint TV PASS')
    print('Menu state matrix rank=4; four null relations rank=4; equal-state pair PASS')
    print('Quantum positive control PASS; all three antipodal relations PASS; fourth relation fails as expected')
    print('Rotated candidate: same heralds; equivalent-state pair A vs B; m=256; terminal X read')
    print('n | joint TV | time-blind TV | simple joint-event gap | completion')
    for n in (3, 7, 15, 31, 63, 127):
        h, k = rotated_counts(n)
        total = sum(h.values())
        total_plus = sum(k.values())
        p = F(total, depth_size(n)*4**n)
        completion = 1-(1-p)**256
        tv = completion*F(sum(abs(10*k[t]-9*h[t]) for t in h), 16*total)
        blind = completion*F(abs(10*total_plus-9*total), 16*total)
        # Fixed explicit event: success by 256, den(T)^2 > 25*n, X read +.
        eh = sum(h[t] for t in h if t.denominator**2 > 25*n)
        ek = sum(k[t] for t in h if t.denominator**2 > 25*n)
        gap = completion*F(10*ek-9*eh, 16*total)
        require(0 <= blind <= tv <= completion <= 1, 'TV range/data processing')
        require(abs(gap) <= tv, 'event exceeds TV')
        # Independent-clock countercontrol preserves both marginals exactly.
        # Replacing k[t] by h[t]*sum(k)/total yields precisely the blind TV.
        decorrelated = completion*F(5, 8)*sum(abs(F(h[t]*total_plus, total)-F(9*h[t], 10))
                                              for t in h)/total
        require(decorrelated == blind, 'decorrelation countercontrol')
        if n == 63:
            require(tv > F(7, 160) and gap > F(1, 64), 'exploratory finite witness absent')
        print('%d | %.12f | %.12f | %.12f | %.12f' %
              (n, float(tv), float(blind), float(gap), float(completion)))
    clock_bound_checks()
    print('PASS: exact identities and scoped witnesses; no native clock or detector derivation claimed')


if __name__ == '__main__':
    main()
