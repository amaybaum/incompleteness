"""The 4x4 candidate of SIG that the sorted-matching search reports as not exact: verify, with Gaussian rationals, that
under a valid label matching SIG is exactly X_{ac} Y_c[b][d] with X and every Y_c unitary (a Dita decomposition)."""
import itertools, json
from lib41 import *
from matchlib import valid_per_group, n_matchings
def mdiv(x, y): return ((x[0] - y[0]) % 4, x[1] - y[1], x[2] - y[2])
def gdiv(x, y):
    n2 = y.norm2(); q = x * y.conj(); return G(q.a / n2, q.b / n2)
out = []
for tr in (False, True):
    M = SIGT if tr else SIG
    H = (lambda i, j: SIGE[j][i]) if tr else (lambda i, j: SIGE[i][j])
    ratio = [[[mdiv(H(i, s), H(i, s0)) for s in range(16)] for s0 in range(16)] for i in range(16)]
    cands, exact = structures(H, mdiv, lambda a, b: ((a[0] + b[0]) % 4, a[1] + b[1], a[2] + b[2]), lambda x: x == (0, 0, 0), 4, 4, ratio)
    for cp, rows in cands:
        if (cp, rows) in exact: continue
        V = valid_per_group(H, cp, rows, False, mdiv)
        print('form', 'row' if tr else 'column', 'blocks', cp, 'groups', rows, 'valid s_b per group', V[1:])
        for sig in itertools.product(*V[1:]):
            s = (tuple(range(4)),) + sig
            row = {(a, b): rows[b][s[b][a]] for a in range(4) for b in range(4)}; col = {(c, d): cp[c][d] for c in range(4) for d in range(4)}
            # X[a][c] = H[row(a,0)][col(c,0)] / H[row(0,0)][col(c,0)];  Y_c[b][d] = H[row(0,b)][col(c,d)] * (normalization)
            X = [[gdiv(M[row[(a, 0)]][col[(c, 0)]], M[row[(0, 0)]][col[(c, 0)]]) for c in range(4)] for a in range(4)]
            Y = [[[M[row[(0, b)]][col[(c, d)]] for d in range(4)] for b in range(4)] for c in range(4)]
            recon = all(M[row[(a, b)]][col[(c, d)]] == X[a][c] * Y[c][b][d] for a in range(4) for b in range(4) for c in range(4) for d in range(4))
            uX = is_unitary_s(X, 4); uY = all(is_unitary_s(Y[c], 4) for c in range(4))   # X entries unimodular, Y scaled by 4
            print('   matching', s, 'exact reconstruction', recon, 'X unitary (x4)', uX, 'Y_c unitary (x4)', uY)
            out.append({'form': 'row' if tr else 'column', 'blocks': cp, 'groups': rows, 'matching': s, 'recon': recon, 'X_unitary': uX, 'Y_unitary': uY})
            break
json.dump(out, open('fifth.json', 'w'), default=list, indent=1)
