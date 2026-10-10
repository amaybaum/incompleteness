"""A33 research: every intersection of two of the nine circles, exactly.
f_r(w) = f_s(w') coordinatewise: sg1 w^e1 = sg2 w'^e2, i.e. w^e1 w'^(-e2) = sg1 sg2, an integer congruence
in the angles; solved by structural.snf, so no parameter grid is assumed."""
import itertools
from fractions import Fraction
from circles import C, N
from structural import snf

def solve2(rows):
    A = [list(r) for r, _ in rows]; c = [x for _, x in rows]
    if not A:
        return ('continuous', 2)
    U, D, V = snf(A)
    Uc = [sum(Fraction(u) * x for u, x in zip(row, c)) for row in U]
    d = [D[i][i] if i < len(D) else 0 for i in range(2)]
    for i in range(len(D)):
        if (D[i][i] if i < 2 else 0) == 0 and Uc[i] % 1:
            return ('none',)
    if 0 in d:
        return ('continuous', d.count(0))
    sols = set()
    for ks in itertools.product(*[range(x) for x in d]):
        psi = [(Uc[i] + ks[i]) / d[i] for i in range(2)]
        sols.add(tuple(sum(Fraction(V[j][i]) * psi[i] for i in range(2)) % 1 for j in range(2)))
    return ('finite', sorted(sols))

def meet(r, s):
    rows = []
    for (s1, e1), (s2, e2) in zip(C[r], C[s]):
        row = [e1, -e2]; rhs = Fraction(0) if s1 * s2 == 1 else Fraction(1, 2)
        if any(row):
            rows.append((row, rhs))
        elif rhs:
            return ('none',)
    return solve2(sorted(set((tuple(r), c) for r, c in rows)))

if __name__ == '__main__':
    tot = 0
    for r in range(N):
        for s in range(r + 1, N):
            res = meet(r, s)
            if res[0] == 'continuous':
                print('CONTINUOUS', r, s); continue
            if res[0] == 'finite':
                tot += len(res[1])
                print(r, s, [(str(a), str(b)) for a, b in res[1]])
    print('intersection incidences (pairs of circle-points):', tot)
