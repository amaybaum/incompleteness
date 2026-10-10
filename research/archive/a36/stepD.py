"""Step D: every relabelled column-Diţă orientation through the point: column 4-blocks S on which the rows fall into
four proportionality classes of four, compatible across a partition of the 16 columns into four blocks."""
import time, itertools
from lib36 import *
t0 = time.time()
H = SIG
cols = range(16)
def prop_partition(S):
    """rows partitioned by proportionality on the column set S (exact: ratios H[i][s]/H[i][S0] equal)"""
    keys = {}
    for i in range(16):
        base = H[i][S[0]]
        k = tuple((H[i][s] * base.conj()).key() for s in S)      # unimodular: division = multiplication by the conjugate
        keys.setdefault(k, []).append(i)
    return sorted(tuple(v) for v in keys.values())
good = {}
for S in itertools.combinations(cols, 4):
    P = prop_partition(S)
    if all(len(cl) % 4 == 0 for cl in P) and all(len(cl) >= 4 for cl in P):
        good[S] = P
print('4-column sets on which rows fall into classes of size a multiple of 4:', len(good), 'of 1820; class-size profiles:', sorted(set(tuple(len(c) for c in P) for P in good.values())))
# column partitions into four good blocks
blocks = list(good)
partitions = []
def rec(rem, chosen):
    if not rem:
        partitions.append(tuple(chosen)); return
    first = min(rem)
    for S in blocks:
        if first in S and set(S) <= rem:
            rec(rem - set(S), chosen + [S])
rec(set(cols), [])
print('column partitions into four admissible blocks:', len(partitions))
# common row partitions: a 4x4 row partition refining every block's proportionality partition
def refinements(parts):
    # the finest common refinement of the block partitions; then it must consist of classes of size 4 (exactly the row classes) or admit 4-splittings
    cls = {i: [] for i in range(16)}
    for P in parts:
        for ci, cl in enumerate(P):
            for i in cl: cls[i].append(ci)
    groups = {}
    for i in range(16): groups.setdefault(tuple(cls[i]), []).append(i)
    return sorted(tuple(v) for v in groups.values())
orientations = []
for cp in partitions:
    common = refinements([good[S] for S in cp])
    sizes = tuple(len(g) for g in common)
    if all(s % 4 == 0 for s in sizes):
        orientations.append((cp, common))
print('column partitions admitting a common row partition into classes of size a multiple of 4:', len(orientations))
for cp, common in orientations[:12]:
    print('  blocks', cp, '| common row classes', tuple(len(g) for g in common))
print('(%.0fs)' % (time.time() - t0))
import pickle; pickle.dump({'good': good, 'orientations': orientations}, open('stepD.pkl', 'wb'))
