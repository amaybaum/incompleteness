"""E9 probe 2 -- the dynamical converse at one finite level: which stage automorphisms are OI-induced?  (exact)

QUESTION.  A Target A system (OISystem, QuasilocalCharacterization.lean:463) carries a star automorphism acting on each
stage as the transport of a reversible configuration map; on a finite lattice the top stage is all of M_N, N = |Q|^|iota|,
and the transport is conjugation by the permutation matrix of a configuration bijection.  Target B's phase automorphism
(phaseQ_ne_heisQ :792) shows locality preservation does not force this.  The repairing hypothesis proposed in NOTES-E9 is
H-DYN: the automorphism maps every stage matrix unit E_fg to a stage matrix unit.  Written argument: an automorphism of
M_N is conjugation by a unitary U (Skolem-Noether); H-DYN sends the minimal projections E_ff to diagonal matrix units, so
U is monomial, U = P D; and E_fg -> D_ff conj(D_gg) E_(pi f)(pi g) is a matrix unit iff all phases of D are equal; so
H-DYN holds iff the automorphism is conjugation by a permutation matrix.  This probe checks the monomial step exhaustively
at N = 4 over the phases {1, i, -1, -i}, and that a non-monomial rational orthogonal conjugation violates H-DYN.

CHECKS.
  M1  for every permutation P of 4 points and every diagonal D with entries in {1, i, -1, -i} (24 * 256 = 6144 cases),
      X -> (PD) X (PD)^* maps all 16 matrix units of M_4 to matrix units  iff  D is a scalar matrix; and in that case it
      equals X -> P X P^T.
  M2  the Householder reflection H = 1 - 2 v v^T / 25, v = (1, 2, 2, 4), conjugates some matrix unit to a non-matrix-unit.
  M3  count: exactly 24 distinct maps satisfy H-DYN among the 6144 cases (one per permutation).

DECISION RULE (fixed before run 1).  VERDICT FINITE-DYN-CONVERSE-INSTANCE iff M1, M2 and M3 pass; otherwise
"VERDICT NOT RENDERED" with the failing checks.  The verdict supports the written argument at N = 4 only; the restriction
to monomial unitaries with fourth-root phases is a finite sample of the monomial case, not the general statement.
"""
import itertools
import sys

import sympy as sp

RESULTS = []


def check(name, ok, detail=''):
    RESULTS.append((name, bool(ok)))
    print(('PASS ' if ok else 'FAIL ') + name + ((' -- ' + detail) if detail else ''))


N = 4
PH = [1, sp.I, -1, -sp.I]
UNITS = []
for i in range(N):
    for j in range(N):
        M = sp.zeros(N, N)
        M[i, j] = 1
        UNITS.append(M)


def is_unit(M):
    ent = list(M)
    return sum(1 for e in ent if e != 0) == 1 and all(e in (0, 1) for e in ent)


ok_m1 = True
maps = set()
for p in itertools.permutations(range(N)):
    P = sp.zeros(N, N)
    for c, r in enumerate(p):
        P[r, c] = 1
    for ph in itertools.product(range(4), repeat=N):
        D = sp.diag(*[PH[k] for k in ph])
        U = P * D
        Ustar = U.H
        imgs = [sp.expand(U * E * Ustar) for E in UNITS]
        hdyn = all(is_unit(M) for M in imgs)
        scalar = len(set(ph)) == 1
        if hdyn != scalar:
            ok_m1 = False
        if hdyn:
            if any(imgs[k] != P * UNITS[k] * P.T for k in range(len(UNITS))):
                ok_m1 = False
            maps.add(tuple(tuple(M) for M in imgs))
check('M1', ok_m1, 'H-DYN holds exactly for scalar D, and then the map is conjugation by P')
v = sp.Matrix([1, 2, 2, 4])
H = sp.eye(N) - 2 * (v * v.T) / 25
bad = [k for k, E in enumerate(UNITS) if not is_unit(sp.expand(H * E * H.T))]
check('M2', H * H.T == sp.eye(N) and len(bad) > 0, '%d of 16 matrix units leave the matrix units under H' % len(bad))
check('M3', len(maps) == 24, '%d distinct maps satisfy H-DYN' % len(maps))
fails = [n for n, ok in RESULTS if not ok]
print('checks: %d, failures: %d' % (len(RESULTS), len(fails)))
print('VERDICT NOT RENDERED -- failing: ' + ', '.join(fails) if fails else 'VERDICT FINITE-DYN-CONVERSE-INSTANCE')
sys.exit(0)
