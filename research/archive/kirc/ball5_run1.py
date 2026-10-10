from ball5 import *
# --- the J/K construction: N = rotation (x fixed; y,z,w1,w2 flipped); J on T_A: x->y->-x, w1->w2->-w1;
#     K on E- = {y,z,w1,w2}: y->z->-y, w1->w2->-w1; S on E+ = {u,x}: u<->x
def JK_G():
    J = {X: (1, Y), Y: (-1, X), W1: (1, W2), W2: (-1, W1)}
    K = {Y: (1, Z), Z: (-1, Y), W1: (1, W2), W2: (-1, W1)}
    Sp = {U: (1, X), X: (1, U)}
    rules = {}
    for c in (X, Y, W1, W2):
        for j in (U, X): s2, l = Sp[j]; rules[(c, j)] = (s2, c, l)
        for j in (Y, Z, W1, W2):
            s1, k = J[c]; s2, l = K[j]; rules[(c, j)] = (s1 * s2, k, l)
    return controlled({Y, Z, W1, W2}, rules)
G = JK_G(); Gm = G.mat(); I = np.eye(D)
k0 = np.eye(n)[U] + np.eye(n)[Z]; k1 = np.eye(n)[U] - np.eye(n)[Z]; ks = [k0, k1]
print('frame:', all(np.allclose(Gm @ np.kron(ks[a], ks[b]), np.kron(ks[a], ks[a ^ b])) for a in (0, 1) for b in (0, 1)),
      ' involution:', np.allclose(Gm @ Gm, I), ' normalization:', np.allclose(Gm.T[:, 0], np.eye(D)[0]))
v, _ = min_value(Gm); print('d=5 JK construction: min (f(x)g)(G(s(x)t)) over unit vectors ~ %+.3e' % v)
N = diagN({Y, Z, W1, W2}); NI = loc_pair(N, ident); IN = loc_pair(ident, N)
print('target relation (I(x)N)G(I(x)N) == G:', ((IN * G) * IN).key() == G.key())
print('control relation (N(x)I)G(N(x)I) == (I(x)N)G:', ((NI * G) * NI).key() == (IN * G).key())
grp = group([G, NI, IN]); print('|<G, N(x)I, I(x)N>| =', len(grp))
worst = min((min_value(g.mat(), starts=60)[0], i) for i, g in enumerate(grp)); print('worst element min value ~ %+.3f' % worst[0])
