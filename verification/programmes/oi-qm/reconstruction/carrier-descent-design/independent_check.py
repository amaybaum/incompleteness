"""Independent finite controls for carrier descent; stdlib Gaussian rationals.

Written independently of source_e3_compress.py. No source import, SymPy or floats.
These finite controls supplement the universal Lean proof; they do not replace it.
"""
from dataclasses import dataclass
from fractions import Fraction as Q


@dataclass(frozen=True)
class G:
    re: Q = Q(0)
    im: Q = Q(0)

    def __add__(self, other):
        return G(self.re + other.re, self.im + other.im)

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other):
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    def conj(self):
        return G(self.re, -self.im)


ZERO, ONE, I = G(), G(Q(1)), G(Q(0), Q(1))
checks = 0


def check(ok, label):
    global checks
    if not ok:
        raise AssertionError(label)
    checks += 1


def identity(n):
    return [[ONE if r == s else ZERO for s in range(n)] for r in range(n)]


def flow(n, a, b, c, s):
    """exp(-it(E_ab+E_ba)), where c=cos(t), s=sin(t) are rational."""
    out = identity(n)
    if a == b:
        # transition a a = 2E_aa: exp(-2it)=(c-is)^2.
        out[a][a] = G(c, -s) * G(c, -s)
    else:
        out[a][a] = out[b][b] = G(c)
        out[a][b] = out[b][a] = G(Q(0), -s)
    return out


def swap(n, a, b):
    # Build from the permutation function, including a=b.
    f = list(range(n))
    f[a], f[b] = f[b], f[a]
    return [[ONE if r == f[s] else ZERO for s in range(n)] for r in range(n)]


def phase(n, a):
    out = identity(n)
    out[a][a] = I
    return out


def compression_plan(n, m, embedding, spectator):
    # Relabel onto S x Fin m, prescribing block k=m-1; complete in reverse order.
    e = dict((spectator * m + embedding[s], s * m + m - 1) for s in range(n))
    src = [p for p in range(n * m) if p not in e]
    dst = [p for p in range(n * m - 1, -1, -1) if p not in e.values()]
    e.update(zip(src, dst))
    check(set(e.values()) == set(range(n * m)), 'relabel is a bijection')
    check(all(e[spectator * m + embedding[s]] == s * m + m - 1
              for s in range(n)), 'prescribed relabel entries')
    return {v: k for k, v in e.items()}


def compress(matrix, n, m, inv):
    # Explicit full tensor and reindex, then extract the named block.
    tensor = [[matrix[r % m][s % m] if r // m == s // m else ZERO
               for s in range(n * m)] for r in range(n * m)]
    reindexed = [[tensor[inv[r]][inv[s]] for s in range(n * m)] for r in range(n * m)]
    return [[reindexed[r * m + m - 1][s * m + m - 1]
             for s in range(n)] for r in range(n)]


def isometry(matrix):
    n = len(matrix)
    return all(sum((matrix[k][r].conj() * matrix[k][s] for k in range(n)), ZERO)
               == (ONE if r == s else ZERO) for r in range(n) for s in range(n))


CASES = [(3, 4, (2, 0, 3)), (3, 8, (0, 3, 5)), (5, 8, (7, 1, 4, 2, 6))]
TIMES = [(Q(1), Q(0)), (Q(0), Q(1)), (Q(3, 5), Q(4, 5)), (Q(-5, 13), Q(12, 13))]
for n, m, embedding in CASES:
    for spectator in range(n):
        inv = compression_plan(n, m, embedding, spectator)
        arbitrary = [[G(Q(r + 2 * s + 1, 7), Q(3 * r - s, 11))
                      for s in range(m)] for r in range(m)]
        check(compress(arbitrary, n, m, inv) ==
              [[arbitrary[embedding[r]][embedding[s]] for s in range(n)] for r in range(n)],
              'arbitrary non-Hermitian operator compression')
        for a in range(n):
            check(compress(phase(m, embedding[a]), n, m, inv) == phase(n, a), 'phase compression')
            for b in range(n):
                check(compress(swap(m, embedding[a], embedding[b]), n, m, inv) == swap(n, a, b),
                      'swap compression including self-index')
                for c, s in TIMES:
                    check(c * c + s * s == 1, 'rational flow time is on the circle')
                    reduced = compress(flow(m, embedding[a], embedding[b], c, s), n, m, inv)
                    check(reduced == flow(n, a, b, c, s), 'flow compression including self-index')
                    check(isometry(reduced), 'compressed generator remains isometric')

# Generic compression need not preserve isometry when the image is not invariant.
inv = compression_plan(3, 4, (0, 1, 2), 2)
bad = compress(flow(4, 0, 3, Q(3, 5), Q(4, 5)), 3, 4, inv)
check(not isometry(bad), 'leaving the subspace loses isometry')
check(bad[0][0] * bad[0][0].conj() - ONE == G(Q(-16, 25)), 'exact negative Gram defect')
check(4 % 3 != 0, 'Fin4 has no factor Fin3 for block descent alone')
check(any(flow(3, 0, 1, Q(3, 5), Q(4, 5))[r][s] != ZERO
          for r in range(3) for s in range(3) if r != s), 'Fin3 transition is not diagonal')

# A relabel with the prescribed block moved is rejected by the arbitrary-operator test.
mutant = dict(inv)
mutant[3], mutant[7] = mutant[7], mutant[3]
arbitrary = [[G(Q(r * 4 + s + 1)) for s in range(4)] for r in range(4)]
check(compress(arbitrary, 3, 4, mutant) !=
      [[arbitrary[r][s] for s in range(3)] for r in range(3)], 'wrong relabel countercontrol')

print(f'PASS independent carrier controls: {checks}; failures: 0')
print('Includes self-index flows, all spectator choices, arbitrary matrices, and negative controls.')
