"""Reviewer check: PNC is vacuous under eps parity leakage; POM bound 3/4 needs EXACT parity obliviousness.
Model: C5 ontology (b0,b1), preparations w*delta_x + (1-w)*U; accessible measurements
  y=0,1: read b_y, then XOR fresh r into the other bit (C5);
  'L'  : read b0^b1^n with n ~ Bernoulli(1/2 - e) from hidden uniform bits (k bits: e = 2^-k... here exact Fraction),
         then XOR fresh r into b0 and b1 (destructive).
Exact arithmetic."""
from fractions import Fraction as F
from itertools import product
import sympy as sp

def run(bits, seq, rs, ns):
    b = list(bits); rec = []
    for t, y in enumerate(seq):
        if y in (0, 1):
            rec.append(b[y]); b[1 - y] ^= rs[t]
        else:
            rec.append(b[0] ^ b[1] ^ ns[t]); b[0] ^= rs[t]; b[1] ^= rs[t] ^ 1 if False else rs[t]
    return tuple(rec)

def law(mix, seq, e):
    L = {}
    for bits, w in mix.items():
        for rs in product((0, 1), repeat=len(seq)):
            for ns in product((0, 1), repeat=len(seq)):
                pn = 1
                for t, y in enumerate(seq):
                    if y == 'L':
                        pn *= (F(1, 2) - e) if ns[t] else (F(1, 2) + e)
                    else:
                        pn *= F(1, 2)  # ns unused: uniform weight, sums to 1
                k = run(bits, seq, rs, ns)
                L[k] = L.get(k, 0) + w * pn * F(1, 2 ** len(seq))
    return L

def prep(x, w):
    m = {l: (1 - w) * F(1, 4) for l in product((0, 1), repeat=2)}; m[x] += w; return m

def tv(a, b):
    ks = set(a) | set(b); return sum(abs(a.get(k, 0) - b.get(k, 0)) for k in ks) / 2

seqs = [q for L in (1, 2, 3) for q in product((0, 1, 'L'), repeat=L)]
for e in (F(1, 100), F(1, 1000)):
    for w in (F(1), F(7, 10)):
        p0 = {}; p1 = {}
        for x in ((0, 0), (1, 1)):
            for k, v in prep(x, w).items(): p0[k] = p0.get(k, 0) + v / 2
        for x in ((0, 1), (1, 0)):
            for k, v in prep(x, w).items(): p1[k] = p1.get(k, 0) + v / 2
        maxtv = max(tv(law(p0, q, e), law(p1, q, e)) for q in seqs)
        # record map on ontic distributions (single measurements): rows P(out=0 | y) for y in 0,1,L, and normalization
        ab = list(product((0, 1), repeat=2))
        T = sp.Matrix([[1 if a == 0 else 0 for a, b in ab], [1 if b == 0 else 0 for a, b in ab],
                       [sp.Rational(1, 2) + (sp.Rational(e.numerator, e.denominator) if (a ^ b) == 0 else -sp.Rational(e.numerator, e.denominator)) for a, b in ab],
                       [1] * 4])
        succ = sum(F(1, 8) * sum(v for k, v in law(prep(x, w), (y,), e).items() if k[0] == x[y]) for x in ab for y in (0, 1))
        # distance of the L measurement on any prep from the trivial fair coin (a QM-admissible test)
        coin = max(tv(law(prep(x, w), ('L',), e), {(0,): F(1, 2), (1,): F(1, 2)}) for x in ab)
        print(f'e={e} w={w}: record-map rank {T.rank()}/4 (=> PNC holds vacuously), POM success {succ}, '
              f'max TV between parity mixtures over {len(seqs)} sequences {maxtv}, L vs fair coin TV {coin}')
