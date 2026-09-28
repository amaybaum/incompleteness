"""The stabilizer closure of the census has 34 relaxed subspaces. Exhibit that an extra one is a genuine Dita structure
of SIG (exact relaxed check on SIG's entries) with the same partitions as a census structure and a different matching."""
from lib42 import *
def relaxed_ok(M, m, n, row, col):
    for c in range(m):
        for b in range(n):
            for a in range(m):
                for d in range(n):
                    i, i2, j, j0 = row[(a, b)], row[(0, b)], col[(c, d)], col[(c, 0)]
                    if M[i][j] * M[i2][j0] != M[i2][j] * M[i][j0]: return False
    lam = lambda a, b, c: M[row[(a, b)]][col[(c, 0)]] * M[row[(0, b)]][col[(c, 0)]].conj()
    for a in range(m):
        for b in range(n):
            for c in range(m):
                if lam(a, b, c) * lam(a, 0, 0) != lam(a, 0, c) * lam(a, b, 0): return False
    return True
found = 0
for (nm, tr, s) in STRUCTS:
    if tr: continue
    (m, n), cp, rows = s
    col = {(c, d): cp[c][d] for c in range(m) for d in range(n)}; row = {(a, b): rows[b][a] for a in range(m) for b in range(n)}
    assert relaxed_ok(SIG, m, n, row, col)
    seen = set()
    for p, s_ in elems:
        rr = [set(divmod(p[i * 16 + j], 16)[0] for j in range(16)) for i in range(16)]
        if not all(len(x) == 1 for x in rr): continue
        pi = [x.pop() for x in rr]; tau = [p[j] % 16 for j in range(16)]
        row2 = {k: pi[v] for k, v in row.items()}; col2 = {k: tau[v] for k, v in col.items()}
        parts = (frozenset(frozenset(col2[(c, d)] for d in range(n)) for c in range(m)), frozenset(frozenset(row2[(a, b)] for a in range(m)) for b in range(n)))
        same_parts = parts == (frozenset(frozenset(cp[c]) for c in range(m)), frozenset(frozenset(rows[b]) for b in range(n)))
        # matching: which rows share the index a across classes (as a partition of rows into m 'a-sets')
        match = frozenset(frozenset(row2[(a, b)] for b in range(n)) for a in range(m))
        match0 = frozenset(frozenset(row[(a, b)] for b in range(n)) for a in range(m))
        if same_parts and match != match0 and (parts, match) not in seen:
            seen.add((parts, match))
            print(nm, 'extra matching on identical partitions; relaxed-Dita at SIG exactly:', relaxed_ok(SIG, m, n, row2, col2))
            found += 1
print('extra (partition-identical, matching-different) structures exhibited:', found)
