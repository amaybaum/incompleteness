"""Probe P5-LG (QPHEN Phase 1 r3, writer's checks). No import from p1-p4.

Leggett-Garg protocol: Q = +-1 read at t1 < t2 < t3, one fixed unitary G between consecutive times;
C_ij from runs that read only at t_i and t_j; K3 = C12 + C23 - C13 (and the other three sign forms).

(1) R4.9 couplings over F_2 on (c, x, m, m'): copy m <- m + c is affine; reciprocal (copy plus
    unconditional kick x <- x + m') is affine; occupation-conditional kick x <- x + c*m' is not.
(2) R2-N1 counterexample, exact (sympy): carrier |0>, ancilla cos t|0> + sin t|1>, G = CNOT
    (ancilla control, carrier target), Lueders Z reads on the carrier: C12 = cos 2t.
(3) Two-mode Clifford G with a non-stabilizer carrier preparation, exact (sympy): K3 = cos b + sin b,
    = sqrt2 at b = pi/4 and 7/5 at (cos b, sin b) = (4/5, 3/5).  Lueders Z reads on the carrier.
    The factorization G = (I x H) . SWAP . CNOT_{m->c} is checked.
(3') Stabilizer carrier |+>, non-stabilizer ancilla with Bloch vector (sin b, 0, cos b), and a two-qubit Clifford
    G = (I x H) . CNOT_{m->c} (checked), with G^dag Zc G = Zc Zm and G^dag (Zc Zm) G = -Yc Ym, exact:
    K3 = cos b + sin b (sqrt2 at b = pi/4).
    Plus an enumeration of all 11520 two-qubit Cliffords (mod phase):
      (a) stabilizer product preparations: every correlator in {0, +-1}, max K3 = 1;
      (b) stabilizer carrier, ancilla on a 7x6 Bloch grid: grid maximum of K3 (a lower bound on the supremum).
(4) Measure-and-reprepare instruments (same instrument at every time), exact: the flip instrument with G = X gives
    K3 = 3; the mixture reprepare-flipped (weight w) / reprepare-read-eigenstate (weight 1 - w), G = X, gives
    K3 = 6w - 3, so K3 = 2 at w = 5/6.
(5) Lueders reads, numeric evidence only: random-search max of K3 for a qubit and for a qubit plus a
    mediator (Q = Z x I, Lueders projectors), compared with 3/2.
"""
import itertools, cmath, math, random
import numpy as np
import sympy as sp

# ---------- (1) ----------
def is_affine(F, n):
    V = list(itertools.product((0, 1), repeat=n))
    for x, y, z in itertools.product(V, repeat=3):
        w = tuple((p + q + r) % 2 for p, q, r in zip(x, y, z))
        if any((F(x)[i] + F(y)[i] + F(z)[i] + F(w)[i]) % 2 for i in range(n)):
            return False
    return True
copy = lambda v: (v[0], v[1], (v[2] + v[0]) % 2, v[3])
recip = lambda v: (v[0], (v[1] + v[3]) % 2, (v[2] + v[0]) % 2, v[3])
condk = lambda v: (v[0], (v[1] + v[0] * v[3]) % 2, (v[2] + v[0]) % 2, v[3])

# ---------- generic exact LG engine ----------
def lg_correlators(rho0, G, projs, instrument=None):
    """rho0 density matrix; G unitary; projs = (P+, P-) Lueders projectors for Q;
    instrument(q, rho) -> post-measurement unnormalized state for outcome q (default Lueders)."""
    if instrument is None:
        instrument = lambda q, r: projs[q] * r * projs[q]
    Gd = G.H if hasattr(G, 'H') else G.conj().T
    evolve = lambda r: G * r * Gd
    tr = lambda M: sp.simplify(M.trace()) if isinstance(M, sp.MatrixBase) else np.trace(M)
    val = {0: 1, 1: -1}
    def corr(i, j):
        tot = 0
        r = rho0
        for _ in range(i - 1):
            r = evolve(r)
        for q1 in (0, 1):
            r1 = instrument(q1, r)
            for _ in range(j - i):
                r1 = evolve(r1)
            for q2 in (0, 1):
                tot += val[q1] * val[q2] * tr(projs[q2] * r1 * projs[q2])
        return sp.simplify(tot) if isinstance(rho0, sp.MatrixBase) else tot.real
    return corr(1, 2), corr(2, 3), corr(1, 3)

def K3forms(c12, c23, c13):
    return [s1 * c12 + s2 * c23 + s3 * c13 for s1, s2, s3 in itertools.product((1, -1), repeat=3) if s1 * s2 * s3 == -1]

# ---------- (2) ----------
def part2():
    t = sp.symbols('t', real=True)
    k0, k1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    anc = sp.cos(t) * k0 + sp.sin(t) * k1
    psi = sp.kronecker_product(k0, anc)             # carrier (x) ancilla
    rho = psi * psi.T
    I2 = sp.eye(2); X = sp.Matrix([[0, 1], [1, 0]])
    P0, P1 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]])
    CNOT_ac = sp.kronecker_product(I2, P0) + sp.kronecker_product(X, P1)   # ancilla control, carrier target
    projs = (sp.kronecker_product(P0, I2), sp.kronecker_product(P1, I2))
    c12, c23, c13 = lg_correlators(rho, CNOT_ac, projs)
    return sp.simplify(sp.trigsimp(c12 - sp.cos(2 * t))) == 0, sp.trigsimp(c12)

# ---------- Clifford group (numeric, mod phase) ----------
def clifford2():
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2); S = np.diag([1, 1j]); I = np.eye(2)
    CX = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
    gens = [np.kron(H, I), np.kron(I, H), np.kron(S, I), np.kron(I, S), CX]
    def key(U):
        idx = np.flatnonzero(np.abs(U.ravel()) > 1e-9)[0]
        ph = U.ravel()[idx] / abs(U.ravel()[idx])
        return tuple(np.round(U.ravel() / ph, 6).tolist())
    seen = {key(np.eye(4)): np.eye(4)}; fr = [np.eye(4)]
    while fr:
        nf = []
        for U in fr:
            for g in gens:
                V = g @ U; k = key(V)
                if k not in seen:
                    seen[k] = V; nf.append(V)
        fr = nf
    return list(seen.values())

PAULI = {'I': np.eye(2), 'X': np.array([[0, 1], [1, 0]]), 'Y': np.array([[0, -1j], [1j, 0]]), 'Z': np.diag([1, -1])}

def part3_exact():
    """find a two-qubit Clifford with G^dag Zc G = Za and G^dag Za G = Xc; then exact K3."""
    Zc, Za, Xc = np.kron(PAULI['Z'], PAULI['I']), np.kron(PAULI['I'], PAULI['Z']), np.kron(PAULI['X'], PAULI['I'])
    cl = clifford2()
    found = None
    for U in cl:
        if np.allclose(U.conj().T @ Zc @ U, Za) and np.allclose(U.conj().T @ Za @ U, Xc):
            found = U; break
    assert found is not None
    # exact form: round to the {0, +-1, +-i}/sqrt2^k lattice via sympy nsimplify
    Gs = sp.Matrix(4, 4, lambda i, j: sp.nsimplify(complex(np.round(found[i, j], 12)), [sp.sqrt(2)]))
    assert all(sp.simplify(e) == 0 for e in (Gs.H * Gs - sp.eye(4)))
    Hs = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    SW = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])
    CNmc = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])   # |c, m> -> |c + m, m>
    assert sp.simplify(sp.kronecker_product(sp.eye(2), Hs) * SW * CNmc - Gs) == sp.zeros(4, 4)
    b = sp.symbols('b', real=True)
    car = sp.Matrix([sp.cos(b / 2), sp.sin(b / 2)])          # Bloch vector (sin b, 0, cos b)
    psi = sp.kronecker_product(car, sp.Matrix([1, 0]))
    rho = psi * psi.T
    P0, P1, I2 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]]), sp.eye(2)
    projs = (sp.kronecker_product(P0, I2), sp.kronecker_product(P1, I2))
    c12, c23, c13 = lg_correlators(rho, Gs, projs)
    K3 = sp.simplify(sp.trigsimp(c12 + c23 - c13))
    v1 = sp.nsimplify(sp.simplify(K3.subs(b, sp.pi / 4)))
    v2 = sp.simplify(K3.subs(b, sp.atan2(sp.Rational(3, 5), sp.Rational(4, 5))))
    return Gs, (sp.trigsimp(c12), sp.trigsimp(c23), sp.trigsimp(c13)), K3, v1, v2

def part3b_exact():
    Zc, Zm = np.kron(PAULI['Z'], PAULI['I']), np.kron(PAULI['I'], PAULI['Z'])
    YY = np.kron(PAULI['Y'], PAULI['Y'])
    found = None
    for U in clifford2():
        if np.allclose(U.conj().T @ Zc @ U, Zc @ Zm) and np.allclose(U.conj().T @ (Zc @ Zm) @ U, -YY):
            found = U; break
    assert found is not None
    Gs = sp.Matrix(4, 4, lambda i, j: sp.nsimplify(complex(np.round(found[i, j], 12)), [sp.sqrt(2)]))
    assert all(sp.simplify(e) == 0 for e in (Gs.H * Gs - sp.eye(4)))
    Hs = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    CNmc = sp.Matrix([[1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0]])   # |c, m> -> |c + m, m>
    assert sp.simplify(sp.kronecker_product(sp.eye(2), Hs) * CNmc - Gs) == sp.zeros(4, 4)
    b = sp.symbols('b', real=True)
    car = sp.Matrix([1, 1]) / sp.sqrt(2)
    anc = sp.Matrix([sp.cos(b / 2), sp.sin(b / 2)])
    psi = sp.kronecker_product(car, anc); rho = psi * psi.T
    P0, P1, I2 = sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]]), sp.eye(2)
    projs = (sp.kronecker_product(P0, I2), sp.kronecker_product(P1, I2))
    c = lg_correlators(rho, Gs, projs)
    K3 = sp.simplify(sp.trigsimp(c[0] + c[1] - c[2]))
    return Gs, tuple(sp.trigsimp(x) for x in c), K3, sp.nsimplify(sp.simplify(K3.subs(b, sp.pi / 4)))

def part3_enum():
    cl = clifford2()
    Zc = np.kron(PAULI['Z'], PAULI['I'])
    Pp, Pm = (np.eye(4) + Zc) / 2, (np.eye(4) - Zc) / 2
    stab1 = [np.array(v, dtype=complex) / np.linalg.norm(v) for v in
             ([1, 0], [0, 1], [1, 1], [1, -1], [1, 1j], [1, -1j])]
    def corrs(U, psi):
        rho = np.outer(psi, psi.conj())
        out = []
        for (i, j) in ((1, 2), (2, 3), (1, 3)):
            r = rho
            for _ in range(i - 1):
                r = U @ r @ U.conj().T
            tot = 0
            for q1, P in ((1, Pp), (-1, Pm)):
                r1 = P @ r @ P
                for _ in range(j - i):
                    r1 = U @ r1 @ U.conj().T
                tot += q1 * (np.trace(Pp @ r1).real - np.trace(Pm @ r1).real)
            out.append(tot)
        return out
    # (a) stabilizer product preparations
    integral, maxa = True, -9
    for U in cl:
        for c, a in itertools.product(stab1, stab1):
            cs = corrs(U, np.kron(c, a))
            integral &= all(min(abs(x), abs(abs(x) - 1)) < 1e-9 for x in cs)
            maxa = max(maxa, max(K3forms(*cs)))
    # (b) stabilizer carrier, non-stabilizer ancilla on a Bloch grid
    grid = []
    for th in np.linspace(0, np.pi, 7):
        for ph in np.linspace(0, 2 * np.pi, 6, endpoint=False):
            grid.append(np.array([np.cos(th / 2), np.exp(1j * ph) * np.sin(th / 2)]))
    maxb, arg = -9, None
    for U in cl:
        for c in stab1:
            for a in grid:
                k = max(K3forms(*corrs(U, np.kron(c, a))))
                if k > maxb + 1e-12:
                    maxb, arg = k, None
    return len(cl), integral, maxa, maxb

# ---------- (4) measure-and-reprepare ----------
def part4():
    k0, k1 = sp.Matrix([1, 0]), sp.Matrix([0, 1])
    P = (k0 * k0.T, k1 * k1.T)
    X = sp.Matrix([[0, 1], [1, 0]])
    # instrument: read Z with outcome q, reprepare the flipped eigenstate (Lueders followed by X)
    flip = lambda q, r: (P[q] * r * P[q]).trace() * P[1 - q]
    res3 = lg_correlators(k0 * k0.T, X, P, flip)
    # instrument: read Z, reprepare |0> whatever the outcome; G = X
    reset = lambda q, r: (P[q] * r * P[q]).trace() * P[0]
    sqX = sp.Matrix([[1, -sp.I], [-sp.I, 1]]) / sp.sqrt(2)
    found2 = []
    for name, G in (('X', X), ('sqrtX', sqX), ('I', sp.eye(2))):
        for iname, ins in (('flip', flip), ('reset0', reset), ('lueders', None)):
            for pname, rho in (('|0>', k0 * k0.T), ('|1>', k1 * k1.T)):
                c = lg_correlators(rho, G, P, ins)
                ks = [sp.nsimplify(sp.simplify(k)) for k in K3forms(*c)]
                if 2 in ks:
                    found2.append((name, iname, pname, [sp.nsimplify(sp.simplify(x)) for x in c]))
    wv = sp.symbols('w', real=True)
    mix = lambda q, r: (P[q] * r * P[q]).trace() * (wv * P[1 - q] + (1 - wv) * P[q])
    cm = lg_correlators(k0 * k0.T, X, P, mix)
    Kmix = sp.expand(cm[0] + cm[1] - cm[2])
    return res3, found2, cm, Kmix, sp.solve(sp.Eq(Kmix, 2), wv)

# ---------- (5) Lueders numeric ----------
def haar(d, rng):
    Z = (rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z); return Q * (np.diag(R) / np.abs(np.diag(R)))

def part5(seed=7):
    rng = np.random.default_rng(seed)
    out = {}
    for d, Zq in ((2, np.diag([1, -1])), (4, np.kron(np.diag([1, -1]), np.eye(2)))):
        Pp, Pm = (np.eye(d) + Zq) / 2, (np.eye(d) - Zq) / 2
        def K(U, psi):
            rho = np.outer(psi, psi.conj()); cs = []
            for (i, j) in ((1, 2), (2, 3), (1, 3)):
                r = rho
                for _ in range(i - 1):
                    r = U @ r @ U.conj().T
                tot = 0
                for q1, P in ((1, Pp), (-1, Pm)):
                    r1 = P @ r @ P
                    for _ in range(j - i):
                        r1 = U @ r1 @ U.conj().T
                    tot += q1 * (np.trace(Pp @ r1).real - np.trace(Pm @ r1).real)
                cs.append(tot)
            return max(K3forms(*cs))
        best = -9
        for _ in range(600):
            U = haar(d, rng); v = rng.standard_normal(d) + 1j * rng.standard_normal(d); v /= np.linalg.norm(v)
            k = K(U, v)
            # local hill-climb
            step = 0.3
            for _ in range(60):
                H = rng.standard_normal((d, d)) + 1j * rng.standard_normal((d, d)); H = (H + H.conj().T) / 2
                w, Vv = np.linalg.eigh(H); dU = Vv @ np.diag(np.exp(1j * step * w)) @ Vv.conj().T
                v2 = v + step * (rng.standard_normal(d) + 1j * rng.standard_normal(d)); v2 /= np.linalg.norm(v2)
                k2 = K(dU @ U, v2)
                if k2 > k:
                    U, v, k = dU @ U, v2, k2
                else:
                    step *= 0.97
            best = max(best, k)
        out[d] = best
    return out

if __name__ == '__main__':
    print('(1) copy affine:', is_affine(copy, 4), '| reciprocal affine:', is_affine(recip, 4),
          '| occupation-conditional kick affine:', is_affine(condk, 4))
    ok, c12 = part2()
    print('(2) CNOT from ancilla cos t|0>+sin t|1>: C12 =', c12, '; equals cos 2t:', ok)
    Gs, cs, K3, v1, v2 = part3_exact()
    print('(3) two-mode Clifford G (G^dag Zc G = Za, G^dag Za G = Xc) = (I x H).SWAP.CNOT_{m->c} [asserted]:', Gs.tolist())
    print('    carrier Bloch (sin b, 0, cos b), ancilla |0>: (C12, C23, C13) =', cs, '; K3 =', K3)
    print('    K3(b = pi/4) =', v1, '; K3(cos b = 4/5, sin b = 3/5) =', v2)
    Gb, cb, K3b, vb = part3b_exact()
    print("(3') G = (I x H).CNOT_{m->c} [asserted]; G^dag Zc G = Zc Zm, G^dag (Zc Zm) G = -Yc Ym:", Gb.tolist())
    print('    carrier |+>, ancilla Bloch (sin b, 0, cos b): (C12, C23, C13) =', cb, '; K3 =', K3b, '; at b = pi/4:', vb)
    n, integral, maxa, maxb = part3_enum()
    print('    enumeration over', n, 'two-qubit Cliffords: stabilizer product preps -> correlators in {0,+-1}:',
          integral, ', max K3 =', round(maxa, 9))
    print('    stabilizer carrier x ancilla on a 7x6 Bloch grid: grid max K3 (lower bound) =', round(maxb, 9))
    res3, found2, cm, Kmix, w2 = part4()
    print('(4) flip instrument (read Z, reprepare the other eigenstate), G = X, prep |0>: (C12, C23, C13) =',
          res3, '-> K3 =', res3[0] + res3[1] - res3[2])
    print('    small search for K3 = 2 among {X, sqrtX, I} x {flip, reset0, Lueders} x {|0>, |1>}:', found2[:3])
    print('    mixture (flip with weight w, else reprepare the read eigenstate), G = X, prep |0>: (C12, C23, C13) =',
          cm, '-> K3 =', Kmix, '; K3 = 2 at w =', w2)
    print('(5) Lueders reads, random search + hill-climb (numeric evidence only):', part5())
