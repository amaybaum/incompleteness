"""Node 1b (b), (c): heralded Z and repeat-until-success, exact (SymPy). Token order: data first, ancilla second.
Each attempt: attach a fresh configuration ancilla |0>, Lueders X-test on it; on outcome '-' apply the native
CNOT data->ancilla (kickback Z on the data); discard the ancilla with its configuration Kraus <0|, <1|."""
import sys
import sympy as sp
from sympy import Matrix, I, sqrt, eye, zeros, Rational, symbols
results = []
def check(name, cond):
    ok = bool(cond); results.append((name, ok)); print(('PASS ' if ok else 'FAIL ') + name)
def kron(A, B): return Matrix(sp.kronecker_product(A, B))
def z(M): return all(sp.simplify(sp.expand(x)) == 0 for x in M)
def eqm(A, B): return z(A - B)
k0 = Matrix([1, 0]); k1 = Matrix([0, 1]); I2 = eye(2); Zm = sp.diag(1, -1)
one2 = Matrix([1, 1]); plus = Matrix([1, 1])/sqrt(2); minus = Matrix([1, -1])/sqrt(2)
def proj(v): return v*v.H/(v.H*v)[0]
CN = Matrix([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]])   # control data, target ancilla
a, b, c, d = symbols('a b c d'); rho = Matrix([[a, b], [c, d]])
def anc_attach(v): return kron(I2, v)
def anc_bra(v): return kron(I2, v.H)
def on_anc(A): return kron(I2, A)
def prop(K, U):
    M = sp.simplify(K*U.H); return sp.simplify(M[0,1]) == 0 and sp.simplify(M[1,0]) == 0 and sp.simplify(M[0,0]-M[1,1]) == 0
def chan(Ks, r): return sp.simplify(sum((K*r*K.H for K in Ks), zeros(2, 2)))

# (b1) X-test on |0>: outcome '-' with probability 1/2, post-measurement state |->
pm = (k0.H*proj(minus)*k0)[0]
check('b1 Lueders X-test on |0>: p(-) = 1/2 and the heralded state is |->', pm == Rational(1, 2) and z(proj(minus)*k0 - minus/sqrt(2)))
# (b2) heralded-Z instrument: success = outcome '-', then CNOT; failure = outcome '+', no correction.
Ks = [anc_bra(cv)*CN*on_anc(proj(minus))*anc_attach(k0) for cv in (k0, k1)]
Kf = [anc_bra(cv)*on_anc(proj(plus))*anc_attach(k0) for cv in (k0, k1)]
check('b2 success branch channel is exactly (1/2) Z rho Z', eqm(chan(Ks, rho), Zm*rho*Zm/2))
check('b3 every success Kraus operator is proportional to Z (or zero)', all(z(K) or prop(K, Zm) for K in Ks))
check('b4 failure branch channel is exactly (1/2) rho', eqm(chan(Kf, rho), rho/2))
check('b5 the instrument is complete: sum K^H K = I', eqm(sum((K.H*K for K in Ks+Kf), zeros(2, 2)), I2))
check('b6 the instrument as a whole is OnesNormal: sum K^H 1 = 1 over its configuration Kraus list', z(sum((K.H*one2 for K in Ks+Kf), zeros(2, 1)) - one2))
check('b7 the success branch alone is not OnesNormal-compatible: Z^H 1 is not proportional to 1', not z(Zm*one2 - one2) and not z(Zm*one2 + one2))
# (b8) the coarse-grained (unheralded) channel is the dephasing (1/2)(rho + Z rho Z), not Z
check('b8 coarse-graining the herald gives dephasing, not the Z channel', eqm(chan(Ks+Kf, rho), (rho + Zm*rho*Zm)/2))

# (c) repeat-until-success: n attempts, stop at the first success; after n failures do nothing.
def rus(n):
    branches = []   # list of Kraus operators on the data (2x2), full configuration Kraus list
    prefix = [I2]   # Kraus operators of the 'all failures so far' branch
    for k in range(n):
        newprefix = []
        for P in prefix:
            for K in Ks: branches.append(K*P)
            for K in Kf: newprefix.append(K*P)
        prefix = newprefix
    return branches + prefix, branches, prefix
for n in (1, 2, 3, 4):
    allK, succ, fail = rus(n)
    eps = Rational(1, 2**n)
    check('c%d.1 n=%d: channel = (1-2^-n) Z rho Z + 2^-n rho' % (n, n), eqm(chan(allK, rho), (1-eps)*Zm*rho*Zm + eps*rho))
    check('c%d.2 n=%d: failure probability 2^-n on every input' % (n, n), eqm(sum((K.H*K for K in fail), zeros(2, 2)), eps*I2))
    check('c%d.3 n=%d: the protocol is OnesNormal (sum K^H 1 = 1)' % (n, n), z(sum((K.H*one2 for K in allK), zeros(2, 1)) - one2))
    # normalized Choi matrices; trace distance of Choi states = 2^-n (the channels id and Z-conj have orthogonal Choi vectors)
    Om = Matrix([1, 0, 0, 1])/sqrt(2); OmZ = Matrix([1, 0, 0, -1])/sqrt(2)
    JZ = OmZ*OmZ.H; Jn = (1-eps)*JZ + eps*Om*Om.H
    ev = (Jn - JZ).eigenvals()
    tn = sum(abs(k)*m for k, m in ev.items())/2
    check('c%d.4 n=%d: Choi trace distance to the Z channel is exactly 2^-n (> 0, so not the Z channel)' % (n, n), sp.simplify(tn - eps) == 0)
# (D1) no ones-fixing unitary V approximates Z within operator-norm distance 1: (Z - cV)1 = (1,-1) - w(1,1)
w = symbols('w')
nrm2 = sp.expand((1 - w)*sp.conjugate(1 - w) + (-1 - w)*sp.conjugate(-1 - w))
check('d1 |(Z - cV) 1|^2 = 2 + 2|w|^2 >= 2 = |1|^2, so ||Z - cV|| >= 1 for every ones-fixing V', sp.simplify(nrm2 - (2 + 2*w*sp.conjugate(w))) == 0)
fails = [n for n, ok in results if not ok]
print('SUMMARY', len(results) - len(fails), 'PASS', len(fails), 'FAIL')
sys.exit(1 if fails else 0)
