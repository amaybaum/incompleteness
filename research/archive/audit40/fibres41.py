"""Every fibre of the projection pi(eR, eC) = (blocks, classes, threads) has |R(m, n)| = m! n! m! (n!)^m elements (small carriers)."""
import itertools, math
from collections import Counter
def pi_rows(eR, m, n):
    classes = frozenset(frozenset(eR[(a, b)] for a in range(m)) for b in range(n))
    threads = frozenset(frozenset(eR[(a, b)] for b in range(n)) for a in range(m))
    return classes, threads
def pi_cols(eC, m, n): return frozenset(frozenset(eC[(c, d)] for d in range(n)) for c in range(m))
for m, n in ((2, 2), (2, 3), (3, 2), (2, 4), (4, 2)):
    N = m * n; keys = [(a, b) for a in range(m) for b in range(n)]; ckeys = [(c, d) for c in range(m) for d in range(n)]
    if N > 8: continue
    rowf = Counter(); colf = Counter()
    for p in itertools.permutations(range(N)):
        rowf[pi_rows(dict(zip(keys, p)), m, n)] += 1
        colf[pi_cols(dict(zip(ckeys, p)), m, n)] += 1
    # a fibre of pi over (partition, alignment) is (row fibre) x (column fibre)
    sizes = {r * c for r in rowf.values() for c in colf.values()}
    R = math.factorial(m) * math.factorial(n) * math.factorial(m) * math.factorial(n) ** m
    nal = Counter(cl for cl, th in rowf)   # alignments per class partition
    print('shape %dx%d on %d points: row fibres %s, column fibres %s, index-map fibre sizes %s, |R| = %d, alignments per partition %s (formula (m!)^(n-1) = %d)'
          % (m, n, N, sorted(set(rowf.values())), sorted(set(colf.values())), sorted(sizes), R, sorted(set(nal.values())), math.factorial(m) ** (n - 1)))
