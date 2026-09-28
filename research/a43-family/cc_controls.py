"""Countercontrols for the alignment-free harness and the flip-symmetry mechanism.
CC1 gauge atom: H3 plus a full-row atom (gauge-trivial): the relaxed union must be H3's five faces times a free fourth coordinate;
    the strict union is expected to differ (strict Dita form is not invariant under row phases).
CC2 act 40's perturbed pieces (one entry of C cleared), alignment-free: realizability and union reported (a classifier control).
CC3 a hull family (B, C): identically Dita, so the union must be the whole 2-torus.
CC4 the flip symmetry as a matrix identity at exact points: H3(-u1,u2,u3) = rows 7<->15 of H3(u1,u2,u3); H3(u1,u2,-u3) = columns
    2<->8 of H3(u1,u2,u3); negative control: H3(u1,-u2,u3) is no row permutation and no column permutation of H3(u1,u2,u3)."""
import time
from align import *
t0 = time.time()
fails = []
def chk(name, got, want):
    ok = got == want; print('  %s  %-100s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)), flush=True)
    if not ok: fails.append(name)
GROW = mat(lambda i, j: 1 if i == 5 else 0)
S = summarize_alignfree([PA, PB, PC, GROW])
five = ['u1 = -1', 'u1 = 1', 'u2 = 1', 'u3 = -1', 'u3 = 1']
chk('CC1 joint realizability of (A, B, C, row-5 gauge atom)', joint_realizable([PA, PB, PC, GROW])[1], 0)
chk('CC1 relaxed union = five faces x free u4', show_union(S['union_relaxed']), five)
print('  CC1 strict union:', show_union(S['union_strict']), '  (sorted notion strict: %s)' % show_union(S['union_sorted_strict']))
chk('CC1 strict union differs from relaxed', show_union(S['union_strict']) != five, True)
print('  (%.0fs)' % (time.time() - t0), flush=True)
Cp = [r[:] for r in PC]; Cp[1][2] = 0
jr = joint_realizable([PA, PB, Cp])
print('  CC2 perturbed family joint realizability (level sets, failing):', jr)
S2 = summarize_alignfree([PA, PB, Cp])
print('  CC2 candidates %d; alignment-free strict union %s; sorted-notion union %s' % (S2['ncand'], show_union(S2['union_strict']), show_union(S2['union_sorted_strict'])))
chk('CC2 sorted-notion union reproduces the frozen countercontrol (the one face u3 = 1), candidates 30', (S2['ncand'], show_union(S2['union_sorted_strict'])), (30, ['u3 = 1']))
S3 = summarize_alignfree([PB, PC])
chk('CC3 hull family (B, C): union is the whole torus (strict and relaxed)', (show_union(S3['union_strict']), show_union(S3['union_relaxed'])), (['T^2'], ['T^2']))
print('  (%.0fs)' % (time.time() - t0), flush=True)
def gp(u, k):
    out = ONE
    for _ in range(k): out = out * u
    return out
def H3f(u1, u2, u3): return [[SIG[i][j] * gp(u1, PA[i][j]) * gp(u2, PB[i][j]) * gp(u3, PC[i][j]) for j in range(16)] for i in range(16)]
U = [G(Fr(3, 5), Fr(4, 5)), G(Fr(8, 17), Fr(15, 17)), G(Fr(20, 29), Fr(21, 29)), I_, G(Fr(7, 25), Fr(24, 25)), z.conj() * z.conj()]
ok1 = ok3 = neg = 0; n = 0
import itertools
for u1, u2, u3 in itertools.permutations(U, 3):
    n += 1
    H = H3f(u1, u2, u3)
    Hm1 = H3f(-u1, u2, u3); ok1 += all(Hm1[i] == H[15 if i == 7 else 7 if i == 15 else i] for i in range(16))
    Hm3 = H3f(u1, u2, -u3); ok3 += all(Hm3[i][j] == H[i][8 if j == 2 else 2 if j == 8 else j] for i in range(16) for j in range(16))
    Hm2 = H3f(u1, -u2, u3)
    rows = {tuple(x.key() for x in H[i]) for i in range(16)}; cols = {tuple(H[i][j].key() for i in range(16)) for j in range(16)}
    neg += (all(tuple(x.key() for x in Hm2[i]) in rows for i in range(16)) or all(tuple(Hm2[i][j].key() for i in range(16)) in cols for j in range(16)))
chk('CC4 at %d exact points: u1 -> -u1 is rows 7<->15, u3 -> -u3 is columns 2<->8; u2 -> -u2 is neither a row nor a column permutation' % n, (ok1, ok3, neg), (n, n, 0))
print('  (%.0fs)' % (time.time() - t0))
print('cc:', 'FAILED %s' % fails if fails else 'OK')
