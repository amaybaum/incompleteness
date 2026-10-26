"""Reviewer: independent FD(B,m) chains and comparison lists for fb05dea8.

Usage: python3 -I -B fd_and_lists.py <new result.json> <reviewer indep.out from the first round>
FD rule written from the REPORT's prose (not the author's code): register r of m bits; v = r*2^B + u;
x = v / 2^(m+B) in [0,1); agree iff x < 4/5 rounded as 'v < ceil(4*2^(m+B)/5)'; new register is the m-bit floor of
the rescaled left end: agree -> (5/4)x, disagree -> 5(x - 4/5).
Stationary laws by cofactors of I-P (Markov chain tree theorem), determinants by exact Fraction elimination.
"""
import ast
import json
import sys
from fractions import Fraction as F

Q45 = F(4, 5)


def det(M):
    M = [r[:] for r in M]
    n = len(M)
    d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        inv = 1 / M[c][c]
        for r in range(c + 1, n):
            if M[r][c]:
                f = M[r][c] * inv
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return d


def fd(B, m):
    n = 1 << m
    K = 1 << (m + B)
    D = [[[F(0)] * n for _ in range(n)] for _ in range(2)]
    for r in range(n):
        for u in range(1 << B):
            v = r * (1 << B) + u
            x = F(v, K)
            if v < -((-4 * K) // 5):
                g, y = 1, x * F(5, 4)
            else:
                g, y = 0, (x - Q45) * 5
            r2 = (y * n).numerator // (y * n).denominator
            assert 0 <= r2 < n
            D[g][r][r2] += F(1, 1 << B)
    return n, D


def classes(n, P):
    reach = []
    for i in range(n):
        s, st = {i}, [i]
        while st:
            a = st.pop()
            for b in range(n):
                if P[a][b] and b not in s:
                    s.add(b)
                    st.append(b)
        reach.append(s)
    out = set()
    for i in range(n):
        c = frozenset(j for j in reach[i] if i in reach[j])
        if c == reach[i]:
            out.add(tuple(sorted(c)))
    return sorted(out)


def analyse(n, D, N):
    P = [[D[0][i][j] + D[1][i][j] for j in range(n)] for i in range(n)]
    res = []
    for C in classes(n, P):
        m = len(C)
        L = [[(1 if a == b else 0) - P[C[a]][C[b]] for b in range(m)] for a in range(m)]
        w = [det([[L[r][s] for s in range(m) if s != i] for r in range(m) if r != i]) if m > 1 else F(1)
             for i in range(m)]
        pi = [x / sum(w) for x in w]
        for b in range(m):
            assert sum(pi[a] * P[C[a]][C[b]] for a in range(m)) == pi[b]
        v = pi[:]
        first = None
        freq = None
        for t in range(1, m + 1):
            v = [sum(v[a] * D[1][C[a]][C[b]] for a in range(m)) for b in range(m)]
            s = sum(v)
            if t == 1:
                freq = s
            if first is None and s != Q45 ** t:
                first = t
        # chi(lambda) = det(lambda I - N D1|C)
        lam = Q45 * N
        chi = det([[(lam if a == b else 0) - N * D[1][C[a]][C[b]] for b in range(m)] for a in range(m)])
        assert first is not None and chi != 0
        res.append((m, first, str(freq)))
    return res


def main():
    new = json.load(open(sys.argv[1]))
    fdres = new['floor_truncated_decoder_member_post_review']
    ok = True
    ncls = 0
    for B in (2, 3, 4):
        for m in range(1, 6):
            n, D = fd(B, m)
            r = analyse(n, D, 1 << B)
            ncls += len(r)
            e = fdres[f'B{B}_m{m}']
            mine = {'states': n, 'class_sizes': [x[0] for x in r], 'least_mismatch': [x[1] for x in r],
                    'stationary_agreement_frequency': [x[2] for x in r]}
            # author's class order may differ: compare as multisets of tuples
            a = sorted(zip(e['class_sizes'], e['least_mismatch'], e['stationary_agreement_frequency']))
            b = sorted(zip(mine['class_sizes'], mine['least_mismatch'], mine['stationary_agreement_frequency']))
            same = e['states'] == n and a == b
            ok &= same
            print(f'FD({B},{m}) states={n} classes={b} match={same}')
    print('FD total classes', ncls, 'all match', ok)
    # comparison lists against reviewer rows from round 1
    rows = {}
    for line in open(sys.argv[2]):
        if line.startswith('('):
            t = ast.literal_eval(line.strip())
            rows[(t[0], t[1])] = (t[4], t[5])     # (power-rule lower depth, power-rule upper depth)
    fam = new['family_RS']
    bad = 0
    for B in (2, 3, 4):
        near = fam[f'B{B}_memoryless_comparators_post_plan']['nearest_dyadic_reset']
        cross = {2: 127, 3: 127, 4: 1819}[B]
        assert near['exact_first_depth_T_above_half'] == cross, (B, near)
        for k in range(2, 17):
            hp, lp = rows[(B, k)]
            pp = fam[f'B{B}_k{k}']['post_plan']
            exp_before, exp_out = hp < cross, lp >= cross
            if (pp['certified_fails_before_nearest_dyadic_reset'], pp['certified_outlasts_nearest_dyadic_reset']) != (exp_before, exp_out):
                bad += 1
                print('LIST MISMATCH', B, k)
        print(f'B={B} nearest agreement {near["agreement"]} crossing {near["exact_first_depth_T_above_half"]}; '
              f'fails-before {[k for k in range(2, 17) if rows[(B, k)][0] < cross]}; '
              f'outlast {[k for k in range(2, 17) if rows[(B, k)][1] >= cross]}')
    print('list mismatches', bad)


if __name__ == '__main__':
    main()
