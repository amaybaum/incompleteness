#!/usr/bin/env python3
"""SC-41 exact check: the Pauli-twirl classical-memory decomposition of the uniform-hidden swap.

Run with `python3 -I pauli_twirl_check.py`. Uses sympy exact arithmetic (Gaussian rationals);
no floating point anywhere. Every map is compared through its Choi matrix
J(L) = sum_{ij} |i><j| (x) L(|i><j|), which determines a linear map on 2x2 matrices exactly.

Object (Main §4.5, §3.2): visible qubit V, hidden qubit H, the swap bijection phi(x,h) = (h,x) as the
permutation unitary U on V (x) H, hidden slot in the uniform diagonal state I/2 (the uniform-burn
card game). Two-step process: L_k(rho) = tr_H[U^k (rho (x) I/2) U^k^dag], k = 1, 2.

Checks.
 (A) L_1(rho) = tr(rho) I/2 and L_2(rho) = rho: the process is the one the decomposition targets.
 (B) Classical-memory form of Main §4.5 ([28]): an instrument {I_o} realizing the first step
     (each I_o completely positive, sum_o I_o = L_1), followed by channels Phi_o conditioned on the
     outcome (each completely positive and trace preserving), with sum_o Phi_o o I_o = L_2.
     Here I_o(rho) = sigma_o rho sigma_o / 4 and Phi_o = Ad sigma_o, o in {0, x, y, z}.
 (C) Controls.
     C1 (non-vacuity): with Phi_o = id for every o the composite is L_1, not L_2.
     C2 (countercontrol, fixed card): with the hidden slot in |0><0| the same swap gives
        L_1(rho) = tr(rho)|0><0| and L_2 = id. J(L_1) = I (x) |0><0|, so every CP I_o <= L_1 has
        Choi A_o (x) |0><0| (measure-and-prepare) and every feed-forward composite has a separable
        Choi matrix; J(id) has a negative partial-transpose eigenvalue, so no classical-memory
        decomposition exists. The script checks the two exact facts the argument uses.
     C3 (definition sensitivity): the Pauli instrument does not realize the fixed-card L_1.
"""
import sympy as sp

fails = 0
def check(cond, msg):
    global fails
    print(('PASS  ' if cond else 'FAIL  ') + msg)
    if not cond:
        fails += 1

I2 = sp.eye(2)
sx = sp.Matrix([[0, 1], [1, 0]])
sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
sz = sp.Matrix([[1, 0], [0, -1]])
paulis = {'0': I2, 'x': sx, 'y': sy, 'z': sz}

def ket(i, n=2):
    v = sp.zeros(n, 1); v[i] = 1; return v
def E(i, j):
    return ket(i) * ket(j).T
def kron(A, B):
    return sp.kronecker_product(A, B)
def ptrace_H(M):
    """trace out the second qubit of a 4x4 matrix on V (x) H."""
    out = sp.zeros(2, 2)
    for a in range(2):
        for b in range(2):
            out[a, b] = sum(M[2 * a + h, 2 * b + h] for h in range(2))
    return out
def choi(L):
    J = sp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            J += kron(E(i, j), L(E(i, j)))
    return sp.simplify(J)
def is_zero(M):
    return sp.simplify(M) == sp.zeros(*M.shape)

# swap permutation unitary: U |x, h> = |h, x>, basis index 2x + h
U = sp.zeros(4, 4)
for x in range(2):
    for h in range(2):
        U[2 * h + x, 2 * x + h] = 1
check(U * U.H == sp.eye(4) and all(sum(U[r, c] for c in range(4)) == 1 for r in range(4)),
      'U is the permutation unitary of phi(x,h) = (h,x)')

def process(rhoH, k):
    Uk = U ** k
    return lambda rho: ptrace_H(Uk * kron(rho, rhoH) * Uk.H)

uniform = I2 / 2
L1, L2 = process(uniform, 1), process(uniform, 2)
J1, J2 = choi(L1), choi(L2)
J_dep = choi(lambda r: r.trace() * I2 / 2)
J_id = choi(lambda r: r)
# (A)
check(is_zero(J1 - J_dep), '(A) uniform hidden slot: L_1(rho) = tr(rho) I/2 exactly')
check(is_zero(J2 - J_id), '(A) uniform hidden slot: L_2(rho) = rho exactly')

# (B) instrument and feed-forward
inst = {o: (lambda s: (lambda r: s * r * s.H / 4))(s) for o, s in paulis.items()}
ff = {o: (lambda s: (lambda r: s * r * s.H))(s) for o, s in paulis.items()}
for o, s in paulis.items():
    Jo = choi(inst[o])
    check(all(ev >= 0 for ev in Jo.eigenvals()), f'(B) I_{o} completely positive (Choi eigenvalues {sorted(Jo.eigenvals())})')
    check(s.H * s == I2, f'(B) Phi_{o} = Ad sigma_{o} is unitary, hence CPTP')
J_sumI = sum((choi(inst[o]) for o in paulis), sp.zeros(4, 4))
check(is_zero(J_sumI - J1), '(B) sum_o I_o = L_1 (the Pauli twirl realizes the first step)')
J_comp = sum((choi(lambda r, o=o: ff[o](inst[o](r))) for o in paulis), sp.zeros(4, 4))
check(is_zero(J_comp - J2), '(B) sum_o Ad sigma_o o (sigma_o . sigma_o / 4) = L_2 = id')

# (C) controls
J_noff = sum((choi(inst[o]) for o in paulis), sp.zeros(4, 4))
check(not is_zero(J_noff - J2), 'C1 without the conditioned correction the composite is L_1, not L_2')
fixed = E(0, 0)
F1, F2 = process(fixed, 1), process(fixed, 2)
JF1, JF2 = choi(F1), choi(F2)
check(is_zero(JF1 - kron(I2, E(0, 0))), 'C2 fixed card: J(L_1) = I (x) |0><0| (output support one-dimensional)')
check(is_zero(JF2 - J_id), 'C2 fixed card: L_2 = id')
def ptranspose_in(J):
    out = sp.zeros(4, 4)
    for i in range(2):
        for j in range(2):
            for a in range(2):
                for b in range(2):
                    out[2 * j + a, 2 * i + b] = J[2 * i + a, 2 * j + b]
    return out
evs = ptranspose_in(J_id).eigenvals()
check(min(evs) < 0, f'C2 J(id) has partial-transpose eigenvalues {sorted(evs)}: entangled, so id is not a sum of measure-and-prepare maps')
check(not is_zero(J_sumI - JF1), 'C3 the Pauli instrument does not realize the fixed-card L_1')

print('\nSC-41 checks:', 'ALL PASS' if fails == 0 else f'{fails} FAILED')
raise SystemExit(1 if fails else 0)
