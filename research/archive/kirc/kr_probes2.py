"""K/R second pass -- read-only, exact arithmetic. Nothing here touches the repository.

P7  the native coupling in the real completion: CNOT is a permutation matrix (the kind of reversible coupling the OI
    substratum supplies natively). In real QM on two rebits, CNOT conjugation does not preserve the locally
    accessible subspace L = span{real-symmetric products}: it maps X(x)Z in L to -Y(x)Y, the locally invisible
    direction. So the real completion's own permutation coupling mixes the invisible direction with the visible ones.
P8  the native experiment class is not tomographically complete for any coherent completion: with only fixed-basis
    readout and permutation interventions, |+><+| and |-><-| (qubit, and the rebit versions) give identical statistics
    for every experiment; also for D = 3 with a coherent vs a dephased state. Exhaustive over all permutations.
P9  C does not imply purification -- two countermodels:
    (a) classical simplex: closure under attach-uniform / stochastic map / discard holds, and every pure (vertex) joint
        state has pure (vertex) marginals, so no mixed state has a pure dilation;
    (b) the diagonal (dephased) class, the kinematic content of the census cell with control failing: the diagonal
        states are closed under uniform attachment, diagonal-preserving maps and partial trace; a pure diagonal joint
        state is a basis state, whose marginal is pure; so the maximally mixed qubit has no purification among
        reachable states.
P10 local tomography plus local reversible pair mixing does not by itself force an enlargement: the minimal tensor
    product of two discs (rebits) is locally tomographic by construction (the joint space is spanned by products) and
    local rotations act reversibly on it, mapping product pure states to product pure states; no entangling reversible
    map is claimed or needed.
"""
import itertools, random
from fractions import Fraction as Fr
import sympy as sp

OUT = []


def rep(name, ok, detail=''):
    OUT.append(ok)
    print(('PASS ' if ok else 'FAIL ') + name + ('  ' + detail if detail else ''))


I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]]); Z = sp.Matrix([[1, 0], [0, -1]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
kron = sp.kronecker_product

# ---- P7 --------------------------------------------------------------------------------------------------------
CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
rep('P7 CNOT is a 0/1 permutation matrix', all(x in (0, 1) for x in CNOT) and CNOT * CNOT.T == sp.eye(4))
img = CNOT * kron(X, Z) * CNOT.T
rep('P7 CNOT (X(x)Z) CNOT^T = -(Y(x)Y)', sp.simplify(img + kron(Y, Y)) == sp.zeros(4))
L = [kron(a, b) for a in (I2, X, Z) for b in (I2, X, Z)]         # real-symmetric products: the local span (9-dim)
YY = kron(Y, Y)
rep('P7 Y(x)Y is Hilbert-Schmidt orthogonal to the whole local span L', all((M * YY).trace() == 0 for M in L))
# L is not CNOT-invariant: some element of L is sent to something with a nonzero Y(x)Y component
comp = [sp.simplify((CNOT * M * CNOT.T * YY).trace() / 4) for M in L]
rep('P7 L is not CNOT-invariant (an element of L acquires a Y(x)Y component)', any(c != 0 for c in comp),
    'components: %s' % comp)
# control: over C the full 16-dim operator space is spanned by products, so invariance is automatic
P = [I2, X, Y, Z]
basis16 = sp.Matrix([list(kron(a, b)) for a in P for b in P])
rep('P7 control: over C, products of {I,X,Y,Z} span all 16 dimensions', basis16.rank() == 16)

# ---- P8 --------------------------------------------------------------------------------------------------------
def fixed_basis_stats(rho, D):
    """all statistics available to permutation interventions followed by fixed-basis readout"""
    stats = []
    for p in itertools.permutations(range(D)):
        Pm = sp.zeros(D)
        for j in range(D): Pm[p[j], j] = 1
        r = Pm * rho * Pm.T
        stats.append(tuple(sp.nsimplify(r[k, k]) for k in range(D)))
    return stats


plus = sp.Matrix([[1, 1], [1, 1]]) / 2; minus = sp.Matrix([[1, -1], [-1, 1]]) / 2
rep('P8 D=2: |+> and |-> distinct, identical under every permutation + fixed-basis readout',
    plus != minus and fixed_basis_stats(plus, 2) == fixed_basis_stats(minus, 2))
v = sp.Matrix([1, 1, 1]) / sp.sqrt(3); coh = v * v.T; deph = sp.eye(3) / 3
rep('P8 D=3: coherent uniform superposition vs maximally mixed: identical native statistics',
    coh != deph and fixed_basis_stats(coh, 3) == fixed_basis_stats(deph, 3))
rep('P8 control: a non-permutation local operation (Hadamard) separates |+> and |->',
    ((sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)) * plus * (sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)))[0, 0] !=
    ((sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)) * minus * (sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)))[0, 0])

# ---- P9 --------------------------------------------------------------------------------------------------------
random.seed(9)


def rand_stoch(n):
    cols = []
    for _ in range(n):
        w = [Fr(random.randint(0, 5)) for _ in range(n)]
        if sum(w) == 0: w[0] = Fr(1)
        s = sum(w); cols.append([x / s for x in w])
    return [[cols[j][i] for j in range(n)] for i in range(n)]      # column-stochastic


def apply(M, p): return [sum(M[i][j] * p[j] for j in range(len(p))) for i in range(len(M))]


# (a) classical: closure under attach uniform (2 states) / stochastic map on 4 states / discard  => stochastic on 2
ok_closure = True
for _ in range(50):
    M = rand_stoch(4)
    # induced map on the system: p -> discard(M (p (x) u)), u uniform on 2
    induced = [[sum(M[2 * i + a][2 * j + b] * Fr(1, 2) for a in range(2) for b in range(2)) for j in range(2)]
               for i in range(2)]
    ok_closure &= all(x >= 0 for r in induced for x in r) and all(sum(induced[i][j] for i in range(2)) == 1
                                                                      for j in range(2))
rep('P9a classical: attach-uniform / stochastic / discard stays stochastic (C-type closure, 50 random rational maps)',
    ok_closure)
vertices = [[Fr(1) if k == m else Fr(0) for k in range(4)] for m in range(4)]      # pure joint states on 2x2
marg_pure = all(max(sum(vx[2 * i + b] for b in range(2)) for i in range(2)) == 1 for vx in vertices)
rep('P9a classical: every pure joint state has a pure marginal => the uniform state has no pure dilation', marg_pure)


# (b) diagonal class: closure and no purification
def is_diag(M): return all(M[i, j] == 0 for i in range(M.rows) for j in range(M.cols) if i != j)


def ptrace2(M, d1, d2):
    R = sp.zeros(d1)
    for i in range(d1):
        for j in range(d1):
            R[i, j] = sum(M[i * d2 + b, j * d2 + b] for b in range(d2))
    return R


ok_b = True
for _ in range(20):
    rho = sp.diag(*[sp.Rational(random.randint(1, 5)) for _ in range(2)]); rho = rho / rho.trace()
    joint = kron(rho, sp.eye(2) / 2)
    M = rand_stoch(4)
    joint2 = sp.diag(*apply(M, [joint[k, k] for k in range(4)]))                    # a diagonal-preserving channel
    ok_b &= is_diag(joint) and is_diag(joint2) and is_diag(ptrace2(joint2, 2, 2))
rep('P9b diagonal class closed under uniform attach, diagonal-preserving channel, partial trace (20 random)', ok_b)
pure_diag = [sp.diag(*[1 if k == m else 0 for k in range(4)]) for m in range(4)]
rep('P9b every pure diagonal joint state has a pure marginal => maximally mixed qubit has no reachable purification',
    all(ptrace2(Pd, 2, 2) ** 2 == ptrace2(Pd, 2, 2) for Pd in pure_diag))
# control: in full (complex or real) QM the Bell state purifies the maximally mixed qubit
bell = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2); B = bell * bell.T
rep('P9 control: the Bell state (real, non-diagonal) purifies I/2', ptrace2(B, 2, 2) == sp.eye(2) / 2 and B ** 2 == B)

# ---- P10 -------------------------------------------------------------------------------------------------------
def disc_state(c, s): return sp.Matrix([1, c, s])                  # rebit (1, x, z), pure on the unit circle


def rot(c, s): return sp.Matrix([[1, 0, 0], [0, c, -s], [0, s, c]])


pts = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(5, 13), sp.Rational(12, 13)), (1, 0), (0, 1)]
ok10 = True
for (c1, s1), (c2, s2), (ca, sa), (cb, sb) in itertools.product(pts, repeat=4):
    prod = kron(disc_state(c1, s1), disc_state(c2, s2))
    Rl = kron(rot(ca, sa), rot(cb, sb))
    out = Rl * prod
    # the image is again a product of pure disc states
    a = rot(ca, sa) * disc_state(c1, s1); b = rot(cb, sb) * disc_state(c2, s2)
    ok10 &= out == kron(a, b) and sp.simplify(a[1] ** 2 + a[2] ** 2) == 1 and sp.simplify(b[1] ** 2 + b[2] ** 2) == 1
rep('P10 local rotations act reversibly on the min tensor product of two discs, products -> pure products (256 cases)',
    ok10)
rep('P10 the min tensor product of discs spans R^3 (x) R^3 (9-dim): locally tomographic by construction',
    sp.Matrix([list(kron(disc_state(*p), disc_state(*q))) for p in pts for q in pts]).rank() == 9)

print('\nSUMMARY: %d PASS, %d FAIL' % (sum(OUT), len(OUT) - sum(OUT)))
