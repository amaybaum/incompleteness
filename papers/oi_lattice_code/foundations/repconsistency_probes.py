#!/usr/bin/env python3
# b95: representation-consistency — the named remainder of the operational bridge.
# The classical comb theorem realizes ANY finite action-labelled family. The
# quantum demand is stronger: the SAME Hilbert space and the SAME Hat-H that
# represent the passive process must host the intervened statistics through CP
# instruments in the slots. Question: is that always possible?
# Method: exact parameter counting. If the comb family with a fixed passive
# marginal has more free directions than the instrument parameters available on
# the fixed representation, generic combs are unreachable there.
from math import comb as C

def comb_params(nV, K, nA):
    """free parameters in P(x_{k+1} | x_<=k, a_<=k), MINUS those fixed by the
    passive branch (the all-trivial action sequence)."""
    tot = 0; passive = 0
    for k in range(K):
        ctx_x = nV**(k+1)          # histories x_1..x_{k+1}? contexts at step k
        ctx_a = nA**(k+1)
        tot     += ctx_x * ctx_a * (nV-1)
        passive += ctx_x * 1      * (nV-1)     # the single trivial action sequence
    return tot - passive

def instrument_params(d, K, nA, n_out):
    """CP instruments in each slot on a FIXED d-dim representation with FIXED H:
    an instrument with n_out outcomes is a set of CP maps summing to CPTP;
    Choi dimension d^2 x d^2 Hermitian per branch, minus the TP constraints."""
    per_instrument = n_out * (d**4) - (d**2)   # Hermitian Choi params minus TP
    return K * nA * per_instrument

CHECKS=[]
print("=== does a FIXED passive representation have room for the intervened statistics? ===")
print(f"{'n_V':>4} {'d':>3} {'K':>3} {'|A|':>4} {'comb dof':>10} {'instrument dof':>15}   verdict")
for nV,d,nA in [(2,2,2),(2,2,3),(3,3,2)]:
    for K in range(2,9):
        cp = comb_params(nV,K,nA)
        ip = instrument_params(d,K,nA,nV)
        v = "REACHABLE (room)" if ip>=cp else "OBSTRUCTED — generic combs unreachable"
        CHECKS.append((K,ip>=cp))
        print(f"{nV:>4} {d:>3} {K:>3} {nA:>4} {cp:>10} {ip:>15}   {v}")
    print()
print("The comb degrees of freedom grow like (nV*nA)^K; the instrument budget on a")
print("fixed representation grows only linearly in K. Beyond a finite horizon the")
print("count inverts, and it inverts at small K for every case above.")
print()
print("PROPOSITION. Fix d, H, and the slot structure. The set of intervened")
print("statistics reachable by CP instruments on that fixed representation is the")
print("image of a polynomial map from a space of dimension linear in K, hence has")
print("measure zero in the comb family for K large enough. Since the classical comb")
print("theorem realizes ALL of that family, representation-consistency fails for")
print("generic action-labelled combs: the intervened description needs a larger")
print("Hilbert space or a different H than the passive one. []")

import sys
# the certified content: reachable at K=3, obstructed at K=4, for every case above
by_K={}
for K,ok in CHECKS: by_K.setdefault(K,[]).append(ok)
ok3 = all(by_K.get(3,[False]))
ok4 = not any(by_K.get(4,[True]))
print("\nrepconsistency_probes:", "ALL CHECKS PASS" if (ok3 and ok4) else "FAILURE")
sys.exit(0 if (ok3 and ok4) else 1)
