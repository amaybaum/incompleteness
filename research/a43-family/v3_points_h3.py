"""Verification 3: explicit exact factorizations of H3 at exact points, over all 46 candidates and all alignments (v1's independent
search), compared with the frozen probe's section-7 counts (sorted notion). Points: the frozen probe's seventeen, plus the
non-coordinate points (+-z^-2, 1, 1) found by the alignment-free locus."""
import time
from v1_explicit import *
t0 = time.time()
def gp(u, k):
    out = ONE
    for _ in range(k): out = out * u
    return out
def H3f(u1, u2, u3): return [[SIG[i][j] * gp(u1, PA[i][j]) * gp(u2, PB[i][j]) * gp(u3, PC[i][j]) for j in range(16)] for i in range(16)]   # verbatim from the frozen probe, section 6
TESTU = [G(Fr(3, 5), Fr(4, 5)), G(Fr(8, 17), Fr(15, 17)), G(Fr(20, 29), Fr(21, 29)), I_, G(Fr(7, 25), Fr(24, 25))]
OR, CANDS, _, _ = P40['classify'](PA, PB, PC)
zi2 = z.conj() * z.conj()
PTS = [('generic', (TESTU[0], TESTU[1], TESTU[2])), ('generic', (TESTU[4], I_, TESTU[0])), ('u1 = 1', (ONE, TESTU[0], TESTU[1])),
       ('u1 = -1', (G(-1), TESTU[0], TESTU[1])), ('u2 = 1', (TESTU[0], ONE, TESTU[1])), ('u2 = -1, absent', (TESTU[0], G(-1), TESTU[1])),
       ('u3 = 1', (TESTU[0], TESTU[1], ONE)), ('u3 = -1', (TESTU[0], TESTU[1], G(-1))), ('u1 = i, absent', (I_, TESTU[0], TESTU[1])),
       ('(1, u, -1)', (ONE, TESTU[2], G(-1))), ('(u, 1, 1)', (TESTU[2], ONE, ONE)), ('(-1, 1, u)', (G(-1), ONE, TESTU[4])),
       ('(1, 1, 1)', (ONE, ONE, ONE)), ('(-1, -1, -1)', (G(-1), G(-1), G(-1))), ('(-1, 1, 1)', (G(-1), ONE, ONE)),
       ('(1, 1, -1)', (ONE, ONE, G(-1))), ('(1, -1, 1)', (ONE, G(-1), ONE)),
       ('(z^-2, 1, 1)', (zi2, ONE, ONE)), ('(-z^-2, 1, 1)', (-zi2, ONE, ONE)), ('(z^-2, 1, -1)', (zi2, ONE, G(-1))),
       ('(z^2, 1, 1) control', (z * z, ONE, ONE)), ('(z^-1, 1, 1) control', (z.conj(), ONE, ONE))]
FROZEN_COUNTS = [0, 0, 1, 1, 2, 0, 1, 1, 0, 3, 7, 4, 18, 2, 12, 12, 4]
counts = []
for idx, (nm, u) in enumerate(PTS):
    H = H3f(*u); HT = [list(c) for c in zip(*H)]
    assert is_unitary16(H)
    n_any = 0; n_sorted = 0
    for (f, mn, cp, rows) in CANDS:
        M = H if f == 'column' else HT
        ex = explicit_factorizations(M, mn, cp, rows, limit=10 ** 6)
        ok = [s for s, i, u_ in ex if i and u_]
        n_any += bool(ok)
        n_sorted += any(all(tuple(s[b]) == tuple(rows[b]) for b in range(len(rows))) for s in ok)
    counts.append((n_any, n_sorted))
    fr = FROZEN_COUNTS[idx] if idx < len(FROZEN_COUNTS) else None
    print('%-24s structures (any alignment) %2d   sorted alignment %2d   frozen section-7 count %s   %.0fs' % (nm, n_any, n_sorted, fr, time.time() - t0), flush=True)
print('sorted-alignment counts equal the frozen section-7 counts:', [c[1] for c in counts[:17]] == FROZEN_COUNTS)
print('points off the five faces with a structure (any alignment):', [nm for (nm, u), c in zip(PTS, counts) if c[0] and not (u[0] in (ONE, G(-1)) or u[1] == ONE or u[2] in (ONE, G(-1)))])
