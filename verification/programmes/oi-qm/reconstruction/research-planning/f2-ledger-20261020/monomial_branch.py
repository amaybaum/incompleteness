"""monomial_branch.py -- exhaustive instance of the monomial-branch lemma (research only).

Lemma [W]: let M be a scaled partial permutation on S x A (system S, ancilla register A), let the
ancilla start in ANY vector |alpha> (arbitrary complex amplitudes, e.g. a product of arbitrary token
states), and read the ancilla in the configuration basis with outcome c'. The Kraus branch
K[x,y] = sum_c alpha(c) <x,c'|M|y,c> has at most one nonzero entry per row, each a single term
(injectivity of the permutation: a fixed output (x,c') has at most one preimage), so an invertible
branch is monomial. A unitary channel has all its Kraus operators proportional to one unitary, so only
monomial unitaries are implementable this way. A finite protocol of native branches, configuration
readouts, attachments and discards reduces to this form by deferring measurements and attachments
(controlled permutations are permutations).

The scan computes every branch matrix explicitly, with distinct prime ancilla amplitudes, over every
permutation of the 8 configurations for (|S|,|A|) = (2,4) and (4,2). The control runs the SAME branch
computation with a non-native post-map (Hadamard on the system) and must be flagged.
"""
import itertools
import sys
from fractions import Fraction as F

FAILS = []
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19]


def check(label, cond):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAILS.append(label)


def branch(perm, nS, nA, cout, post=None):
    """Kraus branch K (nS x nS) of: attach ancilla alpha, apply perm on S x A, read ancilla = cout,
    then (optionally) apply the system matrix `post`."""
    K = [[F(0)] * nS for _ in range(nS)]
    for y in range(nS):
        for c in range(nA):
            x, cp = divmod(perm[y * nA + c], nA)
            if cp == cout:
                K[x][y] += PRIMES[c]
    if post is not None:
        K = [[sum(post[i][k] * K[k][j] for k in range(nS)) for j in range(nS)] for i in range(nS)]
    return K


def row_monomial(K):
    return all(sum(1 for e in row if e != 0) <= 1 for row in K)


def full_support(K):
    n = len(K)
    return all(any(e != 0 for e in K[i]) for i in range(n)) and all(any(K[i][j] != 0 for i in range(n)) for j in range(n))


def is_monomial(K):
    n = len(K)
    return row_monomial(K) and all(sum(1 for i in range(n) if K[i][j] != 0) == 1 for j in range(n))


def scan(nS, nA, post=None, perms=None):
    stats = {"rowmono_fail": 0, "full": 0, "full_nonmono": 0}
    for perm in (perms if perms is not None else itertools.permutations(range(nS * nA))):
        for cout in range(nA):
            K = branch(perm, nS, nA, cout, post)
            if not row_monomial(K):
                stats["rowmono_fail"] += 1
            if full_support(K):
                stats["full"] += 1
                if not is_monomial(K):
                    stats["full_nonmono"] += 1
    return stats


for nS, nA in [(2, 4), (4, 2)]:
    st = scan(nS, nA)
    check(f"split |S|={nS}, |A|={nA}, all 40320 permutations: every branch row-monomial ({st['rowmono_fail']} failures)", st["rowmono_fail"] == 0)
    check(f"split |S|={nS}, |A|={nA}: {st['full']} full-support branches, all monomial ({st['full_nonmono']} non-monomial)",
          st["full_nonmono"] == 0 and st["full"] > 0)

# control through the same computation: identity permutation, then a non-native Hadamard on the system
H = [[F(1), F(1)], [F(1), F(-1)]]
st = scan(2, 4, post=H, perms=[tuple(range(8))])
check(f"control: with a Hadamard post-map the same scan flags {st['full_nonmono']} full-support non-monomial branches (detector fires)",
      st["full_nonmono"] > 0 and st["rowmono_fail"] > 0)
sys.exit(1 if FAILS else 0)
