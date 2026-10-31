"""Exact check: on a finite bijection with full-support visible prior,
(some Gamma_s, 0<s<L, non-permutation)  <=>  (C4 gap at some order k <= L-1).
Also records the least C4 order relative to L (readback at recurrence scale)."""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from collections import Counter
from recur_probe import order, rooted, is_perm, c4_gap
st = Counter()
for nV, nH, mus in [(2,2,[[F(1,2)]*2,[F(2,3),F(1,3)]]),(2,3,[[F(1,3)]*3,[F(1,2),F(1,2),F(0)]]),(3,2,[[F(1,2)]*2,[F(3,4),F(1,4)]])]:
    pV = [F(1,nV)]*nV
    for perm in itertools.permutations(range(nV*nH)):
        phi = list(perm); L = order(phi)
        for mu in mus:
            G = [rooted(phi,nV,nH,mu,t) for t in range(L+1)]
            np_ = any(not is_perm(G[s]) for s in range(1,L))
            ks = [k for k in range(1,L) if c4_gap(phi,nV,nH,mu,pV,k)]
            st[(nV,nH,'nonperm' if np_ else 'allperm','C4<=L-1' if ks else 'noC4')] += 1
            if ks and np_:
                st[(nV,nH,'least_C4_order_minus_L', ks[0]-L)] += 1
for k,v in sorted(st.items(), key=str): print(k, v)
