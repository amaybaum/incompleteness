"""P3 — the composite cone of two 3-balls between min and max, under the kernel's d = 3 native gate, exact.

All objects in W 3 coordinates (CompositeDimension.lean), cnot parsed from the Lean file; quantum states enter only
as models through the P1 dictionary (verified there).

Preregistered decision rules.
  (a) min is not cnot-invariant: phiW = cnot(prodState xplus z3) is separated from min by an exact block-positive
      functional.  [block-positivity of the functional is written; its value at phiW is exact]
  (b) max is not cnot-invariant: some omega in max has cnot(omega) outside max, shown by an exact product-effect
      pair (two Lorentz vectors) with negative pairVal.  Membership of omega in max: written (Lorentz pairing).
  (c) the finite native group H = <cnot, actC nflip, actT nflip> (enumerated exactly as signed permutations) does not
      pin the cone: an exact pure entangled state psi has no h in H with h^{-1}(psi) a product (operator-Schmidt
      rank of the W-matrix > 1 for all h), so psi lies in Q but not in the orbit hull C_H = conv(H min); by
      self-duality of Q and orthogonality of H, M_H = C_H^* strictly contains Q.  Both are H-invariant, contain
      cnot(min), lie in max.  An explicit element X of M_H \\ Q is exhibited with a rational certificate.
      (Run 1 used the bound 19/20, which P3.c2 refuted and the control P3.c5 caught; kept in p3_cones.run1.out.)
  (d) local reflections: no closed convex cone C with min <= C <= max is invariant under cnot and the one-copy
      reflection R_B = actT diag(1,-1,1) (a body automorphism of eball 3, in EffectSpace.fullAut 3): an exact chain
      prodState -> cnot -> R_B -> cnot leaves max (negative product-effect value).
  Controls: (b') the countercontrol omega' = phiW (in Q) stays in max after cnot; (d') with R_B replaced by the
  orientation-preserving rotation actT diag(1,-1,-1) = actT nflip the same chain stays in max.
"""
import sys
import itertools
import sympy as sp
from k2lib import *

LEAN = sys.argv[1]
K = kernel_cnot_matrix(LEAN)
NT = actT_matrix(sp.diag(1, -1, -1))
NC = actC_matrix(sp.diag(1, -1, -1))


def lor(v):
    return v[0] >= 0 and v[1] ** 2 + v[2] ** 2 + v[3] ** 2 <= v[0] ** 2


# a finite family of product-effect Lorentz vectors: (1, +-e_i)/2 and (1, unit rational directions)/2
dirs = []
for i in range(3):
    for s in (1, -1):
        e = [0, 0, 0]
        e[i] = s
        dirs.append(e)
pyth = [(sp.Rational(3, 5), sp.Rational(4, 5)), (sp.Rational(4, 5), sp.Rational(3, 5))]
for (p, r) in pyth:
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        for s1 in (1, -1):
            for s2 in (1, -1):
                e = [0, 0, 0]
                e[i] = s1 * p
                e[j] = s2 * r
                dirs.append(e)
effs = [sp.Matrix([1] + d) / 2 for d in dirs]
assert all(lor(e) for e in effs)


def min_pair(om):
    best = None
    for a in effs:
        for b in effs:
            v = pairval(a, b, om)
            if best is None or v < best[0]:
                best = (v, a.T, b.T)
    return best


# (a)
phiW = unvec(K * vec(prod_W([1, 0, 0], [0, 0, 1])))
Fw = sp.diag(1, -1, 1, -1)
val = sum(Fw[m, v] * phiW[m, v] for m in range(4) for v in range(4))
check('P3.a phiW separated from min: F = diag(1,-1,1,-1) has F(phiW) = -2 '
      '[F >= 0 on products: 1 + x.Dy with D = diag(-1,1,-1) orthogonal, written]', val == -2, val)
# sanity of F on a few products (exact)
check('P3.a\' control: F >= 0 on the 36x36 rational product grid',
      all(sum(Fw[m, v] * prod_W(a[1:, 0] * 2, b[1:, 0] * 2)[m, v] for m in range(4) for v in range(4)) >= 0
          for a in effs for b in effs))

# (b)
I4 = sp.eye(4)   # = W(SWAP/2) = W(PT_B Phi+) ; in max since sum_mu a_mu b_mu >= a0 b0 - |a||b| >= 0
check('P3.b0 omega = I4 is W(SWAP/2) (= PT_B of Phi+, not PSD)', W_of(sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]]) / 2) == I4)
img = unvec(K * vec(I4))
mb = min_pair(img)
check('P3.b cnot(I4) leaves max: exact negative product-effect value', mb[0] < 0, mb)
mb2 = min_pair(unvec(K * vec(phiW)))
check('P3.b\' countercontrol: cnot(phiW) = prodState xplus z3 stays nonneg on the family', mb2[0] >= 0, mb2[0])

# (c) the finite group H
gens = [K, NT, NC]
elems = [sp.eye(16)]
frontier = [sp.eye(16)]
seen = {tuple(sp.eye(16))}
while frontier:
    nxt = []
    for g in frontier:
        for s in gens:
            h = s * g
            t = tuple(h)
            if t not in seen:
                seen.add(t)
                elems.append(h)
                nxt.append(h)
    frontier = nxt
check('P3.c0 |H| = 8 (exact BFS over signed permutations)', len(elems) == 8, len(elems))
# psi = (|00> + |01> + |10> + 2|11>)/sqrt 7 ; rho rational
c = sp.Matrix([1, 1, 1, 2])
rho_psi = c * c.T / 7
Wpsi = W_of(rho_psi)
ranks = [unvec(h.inv() * vec(Wpsi)).rank() for h in elems]
check('P3.c psi has operator-Schmidt rank > 1 after every h^{-1}, h in H (psi not in C_H)', min(ranks) > 1, ranks)
check('P3.c\' countercontrol: the same test finds Phi+ = cnot(product) inside C_H (some rank 1)',
      min(unvec(h.inv() * vec(phiW)).rank() for h in elems) == 1)
# explicit X in M_H \ Q : X = Id - lam psi psi^T with lam = 1/u, u a rational upper bound of
# max_{h, phi product} |<psi|h phi>|^2 = max_h smax^2(h^{-1} psi), smax^2 = (1 + sqrt(1 - C^2))/2, C = 2|det|.
# h are unitary conjugations (P1 dictionary + group of Paulis/CNOT), so pure products go to pure states.
U_CN = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0]])
XI = kron(SX, I2)
IX = kron(I2, SX)
ugens = [U_CN, IX, XI]
uel = [sp.eye(4)]
fr = [sp.eye(4)]
seenu = {tuple(sp.eye(4))}
while fr:
    nx = []
    for g in fr:
        for s in ugens:
            h = s * g
            if tuple(h) not in seenu:
                seenu.add(tuple(h))
                uel.append(h)
                nx.append(h)
    fr = nx
check('P3.c1 the unitary lift group <CNOT, X(x)I, I(x)X> has 8 elements and its Pauli transfer set equals H',
      len(uel) == 8 and {tuple(ptm(u)) for u in uel} == {tuple(h) for h in elems})
psi = c / sp.sqrt(7)
Ds = []
for u in uel:
    v = u.H * psi
    det = sp.nsimplify(v[0] * v[3] - v[1] * v[2])
    Ds.append(sp.nsimplify(1 - 4 * det * sp.conjugate(det)))   # smax^2 = (1 + sqrt(D))/2, D rational
ubound = sp.Rational(99, 100)
c2 = all(D.is_Rational and 0 <= D <= (2 * ubound - 1) ** 2 for D in Ds)
check('P3.c2 every smax^2 = (1+sqrt D)/2 <= 99/100: D rational and D <= (2u-1)^2 (exact rational test)', c2, Ds)
lam = 1 / ubound
X = sp.eye(4) - lam * psi * psi.T
check('P3.c3 X = Id - (100/99) psi psi^T is not PSD (<psi|X|psi> = 1 - 100/99 < 0): X not in Q',
      sp.simplify((psi.T * X * psi)[0]) < 0)
check('P3.c4 X in M_H = C_H^*: <h(phi phi^*), X> = 1 - (100/99)|<psi|h phi>|^2 >= 0 for every pure product phi '
      '[written: |<psi|h phi>|^2 <= smax^2(h^{-1} psi) <= 99/100 by P3.c2]', c2)
WX = W_of(X)
mx = min_pair(WX)
check('P3.c5 control: W(X) is nonneg on the finite product-effect family (consistent with X in max)', mx[0] >= 0, mx[0])

# (d) local reflection on copy B
RB = actT_matrix(sp.diag(1, -1, 1))
tau = unvec(RB * vec(phiW))
chain = unvec(K * vec(tau))
md = min_pair(chain)
check('P3.d cnot(R_B(cnot(prodState xplus z3))) leaves max: exact negative product-effect value', md[0] < 0, md)
chain2 = unvec(K * NT * vec(phiW))
md2 = min_pair(chain2)
check('P3.d\' control: with the rotation actT nflip in place of R_B the chain stays nonneg', md2[0] >= 0, md2[0])
check('P3.d\'\' R_B is a body automorphism of eball 3 (orthogonal, det -1)',
      sp.diag(1, -1, 1).T * sp.diag(1, -1, 1) == sp.eye(3) and sp.diag(1, -1, 1).det() == -1)
print('VERDICT:', ('min and max are not cnot-invariant; the finite native group leaves C_H < Q < M_H all admissible; '
                   'no admissible cone is invariant under cnot and a one-copy reflection')
      if all(c for _, c in CHECKS) else 'NOT RENDERED (a check failed)')
sys.exit(summary())
