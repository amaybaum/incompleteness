"""For each of the 9 census classes at SIG (column form): the monomial conditions the class imposes on u
(proportionality on blocks, rank-one), the exponents k that occur, and one witness quadruple whose condition is
u^k = 1 with k odd (so that it forces u = 1 alone), if any."""
import itertools
from fractions import Fraction as Fr
exec(open('a37/measure37.py', encoding='utf-8').read().split("E_cand = {}")[0])   # symbolic setup, gen_entry, cond
# census at u = 1: the numeric search
def census():
    out = []
    for (m, n) in ((4, 4), (8, 2), (2, 8)):
        for cp, rows, ok, X, Y in dita_orientations(SIG, m, n):
            if ok: out.append((m, n, tuple(cp), tuple(rows)))
    return out
CEN = census(); print('census classes (column form):', len(CEN))
FROZEN = ((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15))
for (m, n, cp, rows) in CEN:
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    conds = []   # (kind, indices, monomial)
    for c in range(m):
        for b in range(n):
            for a in range(m):
                i, i2 = row[(a, b)], row[(0, b)]
                for d in range(1, n):
                    conds.append(('prop', (i, i2, col[(c, d)], col[(c, 0)]), cond(i, i2, col[(c, d)], col[(c, 0)])))
    lam = {(a, b, c): gen_div(gen_entry(row[(a, b)], col[(c, 0)]), gen_entry(row[(0, b)], col[(c, 0)])) for a in range(m) for b in range(n) for c in range(m)}
    for a in range(m):
        for b in range(n):
            for c in range(m):
                conds.append(('rank1', (a, b, c), gen_div(lam[(a, b, c)], gen_mul(lam[(a, 0, c)], lam[(0, b, c)]))))
    nonid = [(k_, idx, mm) for k_, idx, mm in conds if mm != GEN_ONE]
    ks = sorted(set(mm[0] for _, _, mm in nonid)); cs = set(mm[1:] for _, _, mm in nonid)
    odd = [(k_, idx, mm) for k_, idx, mm in nonid if mm[0] % 2 == 1]
    tag = 'FROZEN' if (m, n) == (2, 8) and cp == FROZEN else 'other'
    print('%dx%d %s blocks %s: %d conditions, %d non-identities, u-exponents %s, constant parts %s' % (m, n, tag, cp[:2], len(conds), len(nonid), ks, sorted(cs)))
    if odd:
        k_, idx, mm = odd[0]; print('     witness (%s %s): u^%d * i^%d z^%d w^%d = 1  -> u = 1 only' % (k_, idx, mm[0], mm[1], mm[2], mm[3]))
    elif nonid:
        k_, idx, mm = nonid[0]; print('     no odd exponent; first non-identity (%s %s): u^%d * i^%d z^%d w^%d = 1' % (k_, idx, mm[0], mm[1], mm[2], mm[3]))
