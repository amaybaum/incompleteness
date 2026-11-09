"""Reviewer probe R2 (exact sympy). Countercontrol for BRIDGE-UNIT1 §10.

Claim under test: a same-sublattice (NNB-type) coupling breaks {D, eps} = 0.
That is trivially true when the coupling is ADDED TO the first-order operator D.
This probe checks the cross-level version: does an NNB-type same-sublattice
coupling in the SECOND-ORDER scalar operator force a chirality-breaking term in a
first-order factor D' with D'^2 = -(1/4) Box'?

Construction (1D ring of N fermion sites): D' = (T - T^-1)/2 + mu (T^3 - T^-3)/2,
eps = diag((-1)^x).  Box' := -4 D'^2.  Box' is eps-even, so it splits into two
scalar lattices (even / odd fermion sites) of spacing 2.  On one scalar lattice,
with its own bipartition chi(s) = (-1)^s, we test whether Box' has same-chi
(NNB-type) off-diagonal couplings.
"""
import sympy as sp
N = 16
mu = sp.Rational(1, 3)
def shift(k):
    M = sp.zeros(N, N)
    for x in range(N):
        M[(x + k) % N, x] = 1
    return M
D = (shift(1) - shift(-1)) / 2 + mu * (shift(3) - shift(-3)) / 2
eps = sp.diag(*[(-1) ** x for x in range(N)])
print('{D\', eps} == 0 exactly:', (D * eps + eps * D) == sp.zeros(N, N))
Box = -4 * D * D
print('Box\' eps-even (commutes with eps):', (Box * eps - eps * Box) == sp.zeros(N, N))
even = [x for x in range(0, N, 2)]
Bs = Box.extract(even, even)          # scalar operator on the even scalar lattice (8 sites)
n = len(even)
chi = sp.diag(*[(-1) ** s for s in range(n)])
off = Bs - sp.diag(*[Bs[i, i] for i in range(n)])
same = (off + chi * off * chi) / 2    # chi-even (same-sublattice) part of the off-diagonal couplings
opp = (off - chi * off * chi) / 2
print('scalar-lattice opposite-sublattice couplings nonzero:', opp != sp.zeros(n, n))
print('scalar-lattice SAME-sublattice (NNB-type) couplings nonzero:', same != sp.zeros(n, n))
print('row 0 of scalar operator:', list(Bs.row(0)))
# control: mu = 0 gives the pure staggered case; its scalar operator is NN only on the scalar lattice
D0 = (shift(1) - shift(-1)) / 2
B0 = (-4 * D0 * D0).extract(even, even)
off0 = B0 - sp.diag(*[B0[i, i] for i in range(n)])
print('control mu=0: same-sublattice part zero:', (off0 + chi * off0 * chi) / 2 == sp.zeros(n, n))
# control: adding an eps-even term h directly to D breaks the anticommutator (the writer's check)
h = (shift(2) + shift(-2)) / 10
print('control: {D0 + h, eps} nonzero:', (D0 + h) * eps + eps * (D0 + h) != sp.zeros(N, N))
