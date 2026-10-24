"""Review check on the section 1.3 table, row C: Sum h = 0 is neither sufficient for a ray-moving unitary
nor needed for breaking reality. Exact Fractions; uses this reviewer's own helpers in rev_mc4.py."""
import sys; sys.path.insert(0, sys.argv[1])
from itertools import permutations
from rev_mc4 import c, Z, nz, kraus_indep, rank1_rep, ad, channel_K, units, check, RES
# (i) complex prior, Sum h = 0, pairwise distinct moduli: no ray-moving unitary channel (m = 3, exhaustive)
h = [c(3), c(-1, 1), c(-2, -1)]
assert sum(e[0] for e in h) == 0 and sum(e[1] for e in h) == 0
mov = 0; nr = 0; nonreal = False
for p in permutations(range(6)):
    Ks = kraus_indep(p, 2, 3, h)
    V = rank1_rep(Ks)
    if V is not None and all(any(nz(e) for e in r) for r in V):
        nr += 1
        if ad(V[0][0], V[0][1]) != ad(V[1][0], V[1][1]): mov += 1
    if not nonreal:
        for U in units(2):
            if any(e[1] != 0 for r in channel_K(Ks, h, U) for e in r): nonreal = True; break
check("C1", mov == 0 and nr > 0, f"h = (3, -1+i, -2-i), Sum h = 0: {nr} rank-one channels, ray-moving {mov}")
check("C1b", nonreal, "same prior: some channel maps a matrix unit to a non-real matrix (reality broken without a phase)")
# (ii) complex prior with Sum h != 0 breaks reality as well
h2 = [c(1), c(0, 1), c(1)]
nonreal2 = any(any(e[1] != 0 for r in channel_K(kraus_indep(p, 2, 3, h2), h2, U) for e in r)
               for p in permutations(range(6)) for U in units(2))
check("C2", nonreal2, "h = (1, i, 1), Sum h != 0: reality is broken too, so 'broken when Sum h = 0' is not the condition")
print(f"SUMMARY {sum(RES)} PASS, {len(RES)-sum(RES)} FAIL")
