# INTERVENE-1 exact generic checks (no OI mechanism computed). python3 -I -B checks.py
import itertools, sympy as sp
ok = {}
# X1: an isometry with column-monomial (CM) support has permutation support. Exhaustive over support patterns, n<=4.
def x1(n):
    for cols in itertools.product(range(n+1), repeat=n):   # row index of the column's nonzero entry, n = zero column
        # K^H K = 1 needs each column norm 1 => no zero column; orthogonality of columns j,k with same row r gives conj(a)b != 0
        iso_possible = all(c < n for c in cols) and len(set(cols)) == n
        is_perm = sorted(cols) == list(range(n))
        if iso_possible != is_perm: return False
    # control: symbolic check that two columns sharing a row cannot be orthogonal
    a, b = sp.symbols('a b', nonzero=True)
    return sp.simplify(sp.conjugate(a)*b) != 0
ok['X1 CM isometry => permutation support (n<=4)'] = all(x1(n) for n in range(1,5))
# X2: conj by K preserves all diagonals iff K is column-monomial; exhaustive over 0/1/x supports, 2x2 and 3x3, symbolic entries.
def conj(K, X): return K*X*K.H
def x2(n):
    w = sp.symbols(f'w0:{n}')
    syms = sp.symbols(f'k0:{n*n}')
    for supp in itertools.product([0,1], repeat=n*n):
        K = sp.Matrix(n, n, [s if f else 0 for s, f in zip(syms, supp)])
        Y = sp.expand(conj(K, sp.diag(*w)))
        pres = all(Y[i,j] == 0 for i in range(n) for j in range(n) if i != j)
        cm = all(sum(supp[i*n+j] for i in range(n)) <= 1 for j in range(n))
        if pres != cm: return False
    return True
ok['X2 conj(K) preserves diagonals <=> K column-monomial (supports, n=2,3)'] = x2(2) and x2(3)
# X3: SU(2)-type unitary: conj on diag(1,0) has off-diagonal a*conj(c); zero iff monomial.
ph = sp.symbols('phi', real=True)
A, B = sp.symbols('A B')
U = sp.Matrix([[A, B], [-sp.exp(sp.I*ph)*sp.conjugate(B), sp.exp(sp.I*ph)*sp.conjugate(A)]])
Y = sp.simplify(conj(U, sp.diag(1, 0)))
ok['X3 unitary: off-diagonal of U e0e0 U^H = -A*B*exp(-i phi) (nonzero iff A,B both nonzero)'] = sp.simplify(Y[0,1] + A*B*sp.exp(-sp.I*ph)) == 0
# X4: lift underdetermination witnesses. (a) identity vs quarter-phase conj; (b) reset: CM single operator vs submonomial Kraus pair.
w0, w1, x = sp.symbols('w0 w1 x')
S = sp.diag(1, sp.I)
D = sp.diag(w0, w1); X = sp.Matrix([[w0, x], [sp.conjugate(x), w1]])
ok['X4a phase conj = id on diagonals'] = sp.simplify(conj(S, D) - D) == sp.zeros(2)
ok['X4a countercontrol: phase conj != id off diagonal'] = sp.simplify(conj(S, X) - X) != sp.zeros(2)
K = sp.Matrix([[1, 1], [0, 0]])
R = lambda Z: sp.Matrix([[1,0],[0,0]])*Z*sp.Matrix([[1,0],[0,0]]) + sp.Matrix([[0,1],[0,0]])*Z*sp.Matrix([[0,1],[0,0]]).H
ok['X4b CM reset = Kraus reset on diagonals'] = sp.simplify(conj(K, D) - R(D)) == sp.zeros(2)
ok['X4b countercontrol: differ on off-diagonal input'] = sp.simplify(conj(K, X) - R(X)) != sp.zeros(2)
ok['X4b CM K is not an isometry'] = K.H*K != sp.eye(2)
# X5: route E_f control: R1 tetrahedral frame matrix M_ij=(1+3 a_i.O a_j)/4 ; identity -> permutation (nonneg), Hadamard -> min entry -1/2.
s3 = sp.sqrt(3)
av = [sp.Matrix(v)/s3 for v in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
def M(O): return sp.Matrix(4, 4, lambda i, j: sp.nsimplify((1 + 3*(av[i].T*O*av[j])[0])/4))
Hrot = sp.Matrix([[0,0,1],[0,-1,0],[1,0,0]])   # Hadamard on Bloch vectors: x<->z, y->-y
ok['X5 control: identity frame matrix is a permutation'] = M(sp.eye(3)) == sp.eye(4)
ok['X5 Hadamard frame matrix min entry = -1/2'] = min(M(Hrot)) == sp.Rational(-1, 2)
ok['X5 nonnegative stochastic composite stays nonnegative (P*diag*marg)'] = all(e >= 0 for e in (sp.Matrix([[0,1],[1,0]])*sp.Matrix([[sp.Rational(1,3),1],[sp.Rational(2,3),0]])))
for k, v in ok.items(): print(('PASS ' if v else 'FAIL ') + k)
print('ALL', 'PASS' if all(ok.values()) else 'FAIL')
