#!/usr/bin/env python3
"""Thread D, route 2 (purification with essential uniqueness) against the corpus's fiber freedom.
Exact (Fractions).  Same grid as papers/oi_lattice_code/foundations/purification_probes.py:
every bijection phi on C_V x C_H, (nV,nH) in {(2,2),(2,3),(3,2)}, priors uniform and generic 1:2[:3],
x0 = 0, horizon K = 3.  (Read-only re-enumeration; the corpus probe is not modified or imported.)

Questions:
 Q1  Where does fiber freedom live?  For each same-law group, split members into TAIL-INJECTIVE
     (distinct prior-supported hidden states h have distinct visible tails) and non-injective.
     Is every fiber-freedom witness (two members with different fiber profiles) carried by a
     non-injective member?
 Q2  Weaker uniqueness: for two tail-injective members of the same law group, is there a
     realization isomorphism on the stage-indexed reachable part (visible-preserving,
     dynamics-intertwining, prior-preserving)?  Built explicitly through the ledgered tail object.
 Q3  Is that isomorphism a reversible transformation of the purifier ALONE (one permutation sigma
     of C_H used at every stage and every visible value), as CDP's essential uniqueness requires?
"""
from fractions import Fraction as F
from itertools import permutations

K = 3
def run(nV, nH):
    V, H = range(nV), range(nH)
    states = [(x, h) for x in V for h in H]
    priors = [("uniform", {h: F(1, nH) for h in H}),
              ("generic", {h: F(h + 1, sum(range(1, nH + 1))) for h in H})]
    groups = {}
    for perm in permutations(states):
        phi = dict(zip(states, perm))
        def traj(h):
            s = (0, h); seq = [s]
            for _ in range(K):
                s = phi[s]; seq.append(s)
            return seq                               # stage-indexed configurations s_0..s_K
        trajs = {h: traj(h) for h in H}
        tails = {h: tuple(s[0] for s in trajs[h][1:]) for h in H}
        for pname, mu in priors:
            law = {}
            for h in H: law[tails[h]] = law.get(tails[h], F(0)) + mu[h]
            key = tuple(sorted(law.items()))
            inj = len(set(tails.values())) == nH
            mult = {}
            for h in H: mult[tails[h]] = mult.get(tails[h], 0) + 1
            profile = (tuple(sorted(mult.values())), tuple(sorted(mu.values())))
            groups.setdefault(key, []).append(dict(phi=phi, mu=mu, trajs=trajs, tails=tails,
                                                   inj=inj, profile=profile))
    n_inst = sum(len(g) for g in groups.values())
    witness_groups = [g for g in groups.values() if len({m['profile'] for m in g}) >= 2]
    # Q1: within each witness group, do the tail-injective members alone already disagree?
    inj_disagree = sum(1 for g in witness_groups if len({m['profile'] for m in g if m['inj']}) >= 2)
    witness_needs_noninj = all(any(not m['inj'] for m in g) for g in witness_groups)
    # Q2/Q3: pairs of tail-injective members of one law group
    pairs = iso_ok = single_sigma = 0
    for g in groups.values():
        inj = [m for m in g if m['inj']]
        for a in range(len(inj)):
            for b in range(a + 1, len(inj)):
                A, B = inj[a], inj[b]; pairs += 1
                # match hidden initial states by tail (bijection since both tail-injective, same law)
                byt = {B['tails'][h]: h for h in B['tails']}
                match = {h: byt.get(A['tails'][h]) for h in A['tails']}
                ok = all(v is not None for v in match.values())
                # prior preserved
                ok = ok and all(A['mu'][h] == B['mu'][match[h]] for h in match)
                # stage-indexed iso psi(t, s) = B-trajectory(match h)[t]; well-defined & injective,
                # visible-preserving, intertwining (psi(t+1, phi_A s) = phi_B psi(t, s))
                psi = {}
                for h, hp in match.items():
                    for t in range(K + 1):
                        sA, sB = A['trajs'][h][t], B['trajs'][hp][t]
                        if (t, sA) in psi and psi[(t, sA)] != (t, sB): ok = False
                        psi[(t, sA)] = (t, sB)
                        if sA[0] != sB[0]: ok = False
                        if t < K and B['phi'][sB] != B['trajs'][hp][t + 1]: ok = False
                ok = ok and len(set(psi.values())) == len(psi)
                iso_ok += ok
                # Q3: a single permutation sigma of C_H with psi(t,(x,h)) = (x, sigma(h)) everywhere?
                sig = {}
                good = True
                for (t, sA), (_, sB) in psi.items():
                    if sig.get(sA[1], sB[1]) != sB[1]: good = False
                    sig[sA[1]] = sB[1]
                good = good and len(set(sig.values())) == len(sig)
                single_sigma += good
    return dict(grid=f"{nV}x{nH}", instances=n_inst, laws=len(groups),
                witness_groups=len(witness_groups), witness_groups_where_injective_members_disagree=inj_disagree,
                every_witness_group_has_noninjective_member=witness_needs_noninj,
                injective_same_law_pairs=pairs, pairs_isomorphic=iso_ok, pairs_related_by_one_hidden_permutation=single_sigma)

lines = []
for nV, nH in [(2, 2), (2, 3), (3, 2)]:
    r = run(nV, nH); s = "  ".join(f"{k}={v}" for k, v in r.items()); print(s); lines.append(s)
open('d2_route2_fibers.out', 'w').write("\n".join(lines) + "\n")
