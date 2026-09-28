"""The 4x4 structure of H(-1) = SIG o (-1)^E (act-38 witness) missed by the sorted search: exact reconstruction
H = X_{ac} Y_c[b][d] with X, Y_c unitary, in Gaussian rationals, under a valid matching."""
import itertools, json
from lib41 import *
from matchlib import valid_per_group
def gdiv(x, y):
    n2 = y.norm2(); q = x * y.conj(); return G(q.a / n2, q.b / n2)
HM = Hu(G(-1)); HMT = [list(c) for c in zip(*HM)]
out = []
for form, M, blocks, groups in (('column', HM, ((0, 2, 4, 12), (1, 5, 9, 13), (3, 7, 11, 15), (6, 8, 10, 14)), ((0, 1, 2, 3), (4, 5, 6, 15), (7, 12, 13, 14), (8, 9, 10, 11))),
                                ('row', HMT, ((0, 1, 2, 3), (4, 5, 6, 15), (7, 12, 13, 14), (8, 9, 10, 11)), ((0, 2, 4, 12), (1, 5, 9, 13), (3, 7, 11, 15), (6, 8, 10, 14)))):
    H = lambda i, j: M[i][j]
    V = valid_per_group(H, blocks, groups, False, gdiv)
    sig = (tuple(range(4)),) + tuple(v[0] for v in V[1:])
    row = {(a, b): groups[b][sig[b][a]] for a in range(4) for b in range(4)}; col = {(c, d): blocks[c][d] for c in range(4) for d in range(4)}
    X = [[gdiv(M[row[(a, 0)]][col[(c, 0)]], M[row[(0, 0)]][col[(c, 0)]]) for c in range(4)] for a in range(4)]
    Y = [[[M[row[(0, b)]][col[(c, d)]] for d in range(4)] for b in range(4)] for c in range(4)]
    recon = all(M[row[(a, b)]][col[(c, d)]] == X[a][c] * Y[c][b][d] for a in range(4) for b in range(4) for c in range(4) for d in range(4))
    r = {'form': form, 'valid_per_group': [len(v) for v in V[1:]], 'identity_valid': [tuple(range(4)) in v for v in V[1:]], 'matching': sig,
         'recon': recon, 'X_unitary': is_unitary_s(X, 4), 'Y_unitary': all(is_unitary_s(Y[c], 4) for c in range(4)), 'H(-1) unitary': is_unitary16(M)}
    print(r); out.append(r)
json.dump(out, open('minus_one.json', 'w'), default=list, indent=1)
