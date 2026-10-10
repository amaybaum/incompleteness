"""Coordinator's independent check of the core identity of EQ-D's Theorem A (my construction, not EQ-D's code).
On the carrier R x Fin 2 (tensorOf (1_R) K, kernel convention (r, i)), with X = transition 0 1 at Fin 2:
  M = reindex sigma (1_R (x) flow X s),   sigma swaps (a, 1) <-> (b, 0) and fixes the rest (an involution);
  D = 1_R (x) (phaseGate 0)^2 = 1_R (x) diag(-1, 1)            (no relabelling needed);
  then M D M D = tensorOf (flow (transition a b) (2s)) (1_{Fin 2}), and ancBlock (.) 0 0 = flow (transition a b) (2s).
Also: phaseGate a * phaseGate b * flow (transition a b) (pi/2) = permMatrix (swap a b).
Exact symbolic in s (cos, sin); every ordered pair a != b at |R| = 3, 4."""
import sys
from sympy import Matrix, I, cos, sin, symbols, zeros, eye, pi, simplify, trigsimp, expand
s = symbols('s', real=True)
checks = []
def check(name, cond):
    checks.append((name, bool(cond))); print(("PASS " if cond else "FAIL ") + name)
def flow_transition(n, a, b, t):
    # exp(-i t (E_ab + E_ba)) = identity off {a,b}; cos t on the diagonal of {a,b}, -i sin t off-diagonal
    F = eye(n)
    F[a, a] = cos(t); F[b, b] = cos(t); F[a, b] = -I * sin(t); F[b, a] = -I * sin(t)
    return F
def tensorOf(XA, XB):
    na, nb = XA.shape[0], XB.shape[0]
    T = zeros(na * nb, na * nb)
    for p1 in range(na):
        for p2 in range(nb):
            for q1 in range(na):
                for q2 in range(nb):
                    T[p1 * nb + p2, q1 * nb + q2] = XA[p1, q1] * XB[p2, q2]
    return T
def reindex(K, perm):
    # (reindex e e K)(i, j) = K(e^-1 i, e^-1 j); perm is an involution so e^-1 = e
    n = K.shape[0]
    return Matrix(n, n, lambda i, j: K[perm[i], perm[j]])
for n in (3, 4):
    idx = lambda r, i: r * 2 + i
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            perm = list(range(2 * n))
            perm[idx(a, 1)], perm[idx(b, 0)] = idx(b, 0), idx(a, 1)
            M = reindex(tensorOf(eye(n), flow_transition(2, 0, 1, s)), perm)
            D = tensorOf(eye(n), Matrix([[-1, 0], [0, 1]]))
            lhs = (M * D * M * D).applyfunc(lambda e: trigsimp(expand(e)))
            rhs = tensorOf(flow_transition(n, a, b, 2 * s), eye(2)).applyfunc(lambda e: trigsimp(expand(e)))
            diff = (lhs - rhs).applyfunc(lambda e: simplify(e))
            blk = Matrix(n, n, lambda x, y: lhs[idx(x, 0), idx(y, 0)])
            check(f"|R|={n} (a,b)=({a},{b}): M D M D = flow(transition a b)(2s) (x) 1, block (0,0) extracts it",
                  diff.is_zero_matrix and (blk - flow_transition(n, a, b, 2 * s)).applyfunc(simplify).is_zero_matrix)
            P = Matrix.diag(*[I if r in (a, b) else 1 for r in range(n)])
            Sw = P * flow_transition(n, a, b, pi / 2)
            perm_sw = eye(n); perm_sw[a, a] = 0; perm_sw[b, b] = 0; perm_sw[a, b] = 1; perm_sw[b, a] = 1
            check(f"|R|={n} (a,b)=({a},{b}): phaseGate a * phaseGate b * flow(transition a b)(pi/2) = swap",
                  (Sw - perm_sw).applyfunc(simplify).is_zero_matrix)
# countercontrol: without D (or with D = identity) the product is not a pure system flow
n, a, b = 3, 0, 2
perm = list(range(6)); perm[1], perm[4] = 4, 1
M = reindex(tensorOf(eye(3), flow_transition(2, 0, 1, s)), perm)
lhs = (M * M).applyfunc(lambda e: trigsimp(expand(e)))
check("countercontrol: M*M (no sign conjugation) is not flow(transition a b)(2s) (x) 1 at |R| = 3",
      not (lhs - tensorOf(flow_transition(3, a, b, 2 * s), eye(2))).applyfunc(simplify).is_zero_matrix)
npass = sum(1 for _, c in checks if c)
print(f"review_eqD: {npass}/{len(checks)} checks pass")
sys.exit(0 if npass == len(checks) else 1)
