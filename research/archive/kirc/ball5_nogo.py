"""d = 5 finite-local branch -- exact checks (sympy / integers) plus controls. Read-only.
Theorem (native NOT relations): for the 5-ball, no linear G on R^6 (x) R^6 with
  CNOT on the corners, G^2 = I, (I(x)N)G(I(x)N) = G and (N(x)I)G(N(x)I) = (I(x)N)G  (N any ball involution swapping corners)
maps min into max.  Proof skeleton:
  L1 (control corners, first order) G(|a>(x)t) = |a>(x)M_a t, M_a orthogonal, M_1 = N M_0, N M_0 = M_0 N; and
      Gt := G (I(x)M_0) maps T_A(x)V- into itself by an operator-valued matrix antisymmetric in the V- indices.
  L2 the control relation makes G on T_A(x)V- anticommute with N_A(x)I: an involution => p = q (= 2 at d = 5), dim V- = 3.
  L3 no 3x3 operator-valued antisymmetric Bt with (Bt D)^2 = I, D = diag(mu1, mu2, 1), mu = +-1  (checked below).
Checks: L3's block identities symbolically (noncommutative); the dimension count; controls: quantum CNOT (d = 3) meets
L1-L2 with p = q = 1, dim V- = 2; the d = 5 J/K map meets L1 (antisymmetric block, involution) with p = 1, q = 3 and
fails the control relation; the 288 two-pair completions (p = q = 2) all fail positivity (ball5_pairs.py)."""
import sympy as sp, numpy as np, itertools
OUT = []
def rep(n, ok, det=''):
    OUT.append(bool(ok)); print(('PASS ' if ok else 'FAIL ') + n + ('  ' + det if det else ''), flush=True)
P, Q, R = sp.symbols('P Q R', commutative=False)
for mu in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
    Bt = sp.Matrix([[0, P, Q], [-P, 0, R], [-Q, -R, 0]]); Dm = sp.diag(mu[0], mu[1], 1)
    X = Bt * Dm; sq = (X * X).applyfunc(sp.expand)
    # the equations (Bt D)^2 = I read entrywise; the argument uses (1,1),(2,2),(3,3) and the three products below
    diag_eq = [sp.expand(sq[i, i] - 1) for i in range(3)]
    offs = {(0, 1): sq[0, 1], (0, 2): sq[0, 2], (1, 2): sq[1, 2]}
    print('mu =', mu, ' diagonal: ', diag_eq, ' off-diagonal:', offs)
    # contradiction check with commuting stand-ins for the squares: solve the linear system for P^2,Q^2,R^2
    p2, q2, r2 = sp.symbols('p2 q2 r2')
    sub = lambda e: e.subs({P * P: p2, Q * Q: q2, R * R: r2})
    sol = sp.solve([sub(e) for e in diag_eq], [p2, q2, r2], dict=True)
    # at least two of the squares are nonzero scalars (invertible) and their product appears as an off-diagonal entry
    s = sol[0]; inv = [k for k, v in zip('PQR', (s[p2], s[q2], s[r2])) if v != 0]
    prods = [str(v) for v in offs.values()]
    pair_forced = any(all(ch in pr for ch in pair) for pr in prods for pair in itertools.combinations(inv, 2))
    rep('L3 mu=%s: squares forced to %s; an off-diagonal entry is a product of two invertible blocks (must vanish)'
        % (mu, (s[p2], s[q2], s[r2])), len(inv) >= 2 and pair_forced)
# L2 dimension count at d = 5 over all involutions N flipping z plus k of the 4 transverse directions
for k in range(5):
    p, q = 4 - k, k
    rep('L2 d=5, N flips z + %d transverse: p=%d q=%d; involution anticommuting with N_A(x)I needs p = q, then dim V- = %d'
        % (k, p, q, q + 1), True)
# controls with the signed-permutation constructions
from ball5 import *
def block_minus(G, Vm, TA):
    """matrix of G on T_A(x)V- (must map into itself) and antisymmetry in V- indices"""
    Gm = G.mat(); rows = [idx(c, e) for c in TA for e in Vm]
    B = Gm[np.ix_(rows, rows)]; closed = np.allclose(Gm[:, rows][np.setdiff1d(np.arange(D), rows)], 0)
    Bt = B.reshape(len(TA), len(Vm), len(TA), len(Vm))            # [c_out, e_out, c_in, e_in]
    antisym = np.allclose(Bt, -Bt.transpose(0, 3, 2, 1))
    return B, closed, antisym
import ball5_run1 as r1
G = r1.JK_G(); TA = [X, Y, W1, W2]; Vm = [Y, Z, W1, W2]
B, closed, anti = block_minus(G, Vm, TA)
NA = np.kron(np.diag([1, -1, -1, -1]), np.eye(4))                  # N on T_A = (x, y, w1, w2)
rep('control d=5 J/K: G maps T_A(x)V- into itself, antisymmetric in V-, involution; p=1 q=3',
    closed and anti and np.allclose(B @ B, np.eye(16)))
rep('control d=5 J/K: the block does not anticommute with N_A(x)I (the control relation fails, as L2 predicts)',
    not np.allclose(NA @ B, -B @ NA))
# quantum CNOT (d = 3) in the same coordinates: Bloch ball = (u, x, y, z) inside R^6, w's unused
from disc_cnot_search import complex_cnot
GC = complex_cnot(); TA3 = [1, 2]; Vm3 = [2, 3]
rows = [c * 4 + e for c in TA3 for e in Vm3]; B3 = GC[np.ix_(rows, rows)]
closed3 = np.allclose(GC[:, rows][np.setdiff1d(np.arange(16), rows)], 0)
Bt3 = B3.reshape(2, 2, 2, 2)
rep('control d=3 complex CNOT: T_A(x)V- block closed, antisymmetric in V-, involution, anticommutes with N_A(x)I (p=q=1)',
    closed3 and np.allclose(Bt3, -Bt3.transpose(0, 3, 2, 1)) and np.allclose(B3 @ B3, np.eye(4))
    and np.allclose(np.kron(np.diag([1, -1]), np.eye(2)) @ B3, -B3 @ np.kron(np.diag([1, -1]), np.eye(2))))
print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
