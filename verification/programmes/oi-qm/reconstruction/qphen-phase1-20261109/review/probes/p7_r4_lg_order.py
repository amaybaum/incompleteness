"""Probe P7 (QPHEN Phase 1 r4, writer's check). Exact (sympy). Imports no earlier probe.

The Leggett-Garg counterexample of QX-4 A4.1(c), in one fixed configuration:
- tensor order: carrier (x) mediator, basis |c m>;
- G1 = (I (x) H) . CNOT_{m->c}: CNOT with control the mediator and target the carrier, then H on the mediator
  (the rightmost factor acts first);
- G2 = (I (x) H) . SWAP . CNOT_{m->c}: the same, with a SWAP between the CNOT and the H;
- reads: Lueders reads of Z on the carrier, projectors P_q (x) I;
- the protocol: Q read at t1 < t2 < t3, one application of G between consecutive times, C_ij from runs that read only
  at t_i and t_j, K3 = C12 + C23 - C13.

Configurations checked:
(a) G1, carrier |+>, mediator with Bloch vector (sin b, 0, cos b): expect K3 = cos b + sin b.
(b) G2, carrier with Bloch vector (sin b, 0, cos b), mediator |0>: expect K3 = cos b + sin b.
(c) The other placement of H, on the carrier, (H (x) I) . CNOT_{m->c} and (H (x) I) . SWAP . CNOT_{m->c}, with the
    same preparations: reported separately.
Also: G1 and G2 are Clifford (they map each two-qubit Pauli to a signed Pauli under conjugation), and the values at
b = pi/4 and at (cos b, sin b) = (4/5, 3/5).
"""
import itertools
import sympy as sp

b = sp.symbols('b', real=True)
I2 = sp.eye(2)
H = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
P = (sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 0], [0, 1]]))          # Z = +1, Z = -1
kron = sp.kronecker_product

# basis index 2*c + m (carrier first)
CNOT_m_to_c = sp.zeros(4, 4)
for c, m in itertools.product((0, 1), repeat=2):
    CNOT_m_to_c[2 * ((c + m) % 2) + m, 2 * c + m] = 1                       # |c, m> -> |c + m, m>
SWAP = sp.zeros(4, 4)
for c, m in itertools.product((0, 1), repeat=2):
    SWAP[2 * m + c, 2 * c + m] = 1

G1 = kron(I2, H) * CNOT_m_to_c
G2 = kron(I2, H) * SWAP * CNOT_m_to_c
G1c = kron(H, I2) * CNOT_m_to_c
G2c = kron(H, I2) * SWAP * CNOT_m_to_c
PROJ = (kron(P[0], I2), kron(P[1], I2))

def is_clifford(U):
    paulis = [I2, X, Y, Z]
    basis = [kron(A, B) for A in paulis for B in paulis]
    for Pm in basis[1:]:
        V = sp.simplify(U * Pm * U.H)
        if not any(sp.simplify(V - s * Q) == sp.zeros(4, 4) for Q in basis for s in (1, -1, sp.I, -sp.I)):
            return False
    return True

def correlators(rho0, G):
    ev = lambda r: G * r * G.H
    val = (1, -1)
    def C(i, j):
        r = rho0
        for _ in range(i - 1):
            r = ev(r)
        tot = 0
        for q1 in (0, 1):
            r1 = PROJ[q1] * r * PROJ[q1]
            for _ in range(j - i):
                r1 = ev(r1)
            for q2 in (0, 1):
                tot += val[q1] * val[q2] * (PROJ[q2] * r1 * PROJ[q2]).trace()
        return sp.simplify(sp.trigsimp(tot))
    return C(1, 2), C(2, 3), C(1, 3)

def bloch_xz(beta):           # pure state with Bloch vector (sin beta, 0, cos beta)
    return sp.Matrix([sp.cos(beta / 2), sp.sin(beta / 2)])

plus = sp.Matrix([1, 1]) / sp.sqrt(2)
zero = sp.Matrix([1, 0])
def rho(car, med):
    v = kron(car, med); return v * v.H

cases = [
    ('(a) G1 = (I x H).CNOT_{m->c}; carrier |+>, mediator (sin b,0,cos b)', G1, rho(plus, bloch_xz(b))),
    ('(b) G2 = (I x H).SWAP.CNOT_{m->c}; carrier (sin b,0,cos b), mediator |0>', G2, rho(bloch_xz(b), zero)),
    ('(c1) H on the carrier: (H x I).CNOT_{m->c}; carrier |+>, mediator (sin b,0,cos b)', G1c, rho(plus, bloch_xz(b))),
    ('(c2) H on the carrier: (H x I).SWAP.CNOT_{m->c}; carrier (sin b,0,cos b), mediator |0>', G2c, rho(bloch_xz(b), zero)),
]

if __name__ == '__main__':
    print('G1 Clifford:', is_clifford(G1), '| G2 Clifford:', is_clifford(G2))
    print('G1 unitary:', sp.simplify(G1 * G1.H) == sp.eye(4), '| G2 unitary:', sp.simplify(G2 * G2.H) == sp.eye(4))
    for name, G, r in cases:
        c12, c23, c13 = correlators(r, G)
        K3 = sp.simplify(sp.trigsimp(c12 + c23 - c13))
        v1 = sp.nsimplify(sp.simplify(K3.subs(b, sp.pi / 4)))
        v2 = sp.simplify(K3.subs(b, sp.atan2(sp.Rational(3, 5), sp.Rational(4, 5))))
        target = sp.simplify(K3 - (sp.cos(b) + sp.sin(b))) == 0
        print(name)
        print('    (C12, C23, C13) =', (c12, c23, c13), '; K3 =', K3, '; equals cos b + sin b:', target,
              '; K3(pi/4) =', v1, '; K3 at (4/5, 3/5) =', v2)
