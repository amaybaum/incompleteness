"""R0 exact check: dim aff{prepVec x} = rank(conditional table) - 1 = rank(joint table) - 1,
on the PT toy tower (stages 2, 3) and on the lattice passive tables (n <= 4)."""
import sys
sys.path.insert(0, '../oistage'); sys.path.insert(0, '.')
from fractions import Fraction as Fr
import oistage_checks as T            # runs the OI-STAGE checks once (prints)
from lattice_rank import record_counts, hankel, rank_Q
ok = True
for n in (2, 3):
    P, E = T.stagesP[n], T.stagesE[n]
    rows = [[T.p(T.S, e, x) for e in E] for x in P]
    diffs = [[a - b for a, b in zip(r, rows[0])] for r in rows[1:]]
    joint = [[T.p(T.S, e, x) * sum((T.S.mu[w] for w in range(T.S.N) if T.S.run(w, x[0])[0] == x[1]), Fr(0))
              for e in E] for x in P]
    a, r, j = T.rank(diffs), T.rank(rows), T.rank(joint)
    print(f'R0 toy stage {n}: dim aff = {a}, rank(conditional) = {r}, rank(joint) = {j}')
    ok = ok and a == r - 1 and r == j
for rule in ('nonlinear',):
    cnt = record_counts(4, rule)
    for L in (1, 2, 3, 4):
        H = hankel(cnt, 4, L)
        cond = [[Fr(x, row[0]) for x in row] for row in H if row[0] != 0]
        diffs = [[a - b for a, b in zip(rw, cond[0])] for rw in cond[1:]]
        a, r, j = rank_Q(diffs) if diffs else 0, rank_Q(cond), rank_Q(H)
        print(f'R0 lattice {rule} n={L}: dim aff = {a}, rank(conditional) = {r}, rank(joint) = {j}')
        ok = ok and a == r - 1 and r == j
print('R0', 'OK' if ok else 'FAILED')
