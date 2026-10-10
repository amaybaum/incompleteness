"""o3_density.py -- research/origin, node O3, skeptical pass on O3-T3 ("Discrete =/=> Continuous with the
quarter phase only"), which o3_continuous checked on the single-qubit level only (C5).

QUESTION. Does one balanced mixer, together with the exchanges available at every level, generate elements of
infinite order at levels whose carrier is not a power of two? If so, the closure of the generated group contains
a one-parameter subgroup (a compact infinite group has positive dimension), and the quarter-phase finiteness of C5
is a single-qubit statement only.

METHOD (exact): the matrices have entries in Q(sqrt2). Write the characteristic polynomial as A + sqrt2 B with A,
B in Q[lam]; its norm N = A^2 - 2 B^2 lies in Q[lam] and has as roots the spectrum of U and of its Galois
conjugate, which has finite order exactly when U does. So U has finite order iff every irreducible factor of N over
Q is cyclotomic; a factor that is not monic over Z, or monic but not cyclotomic, certifies an eigenvalue that is
not a root of unity, hence infinite order. (Run 1 tested the characteristic polynomial itself with a defective
cyclotomic comparison and was VOID by its countercontrols; kept as o3_density.run1.*.)
  E1  three states: H_01 H_12 (H on a pair, identity elsewhere; the second a permutation conjugate of the first).
  E2  the kernel's carrier at level n = 3 (Fin 2 x Fin 3, six states): M1 = rot(pi/4) (x) 1_3 (StateMixingCoupling
      `mixImage 3 (pi/4)`, the fixed-gate datum at the balanced angle), M2 = P M1 P^-1 for the permutation P that
      shifts the ancilla index of the second site value by one (an exchange product, available at every level).
  E3  level n = 2 (four states): M1 = rot(pi/4) (x) 1_2 and its conjugate by the same kind of shift: the product's
      factors are expected cyclotomic (two qubits: Clifford), reported as measured.
DECISION RULE (fixed before the first run): the verdict line is generated from the measured factorizations;
VERDICT DENSITY printed iff E1 and E2 are both certified infinite-order and the countercontrols return their
expected-false values; VERDICT FINITE iff neither is; otherwise VERDICT MIXED. Countercontrols (must be False):
  CC1  the single-qubit product rot(pi/4) . X has an infinite-order certificate (it must not: dihedral, finite);
  CC2  the identity matrix has a non-cyclotomic factor.

Run: python3 -I -B o3_density.py > o3_density.out 2> o3_density.err; echo "exit $?" >> o3_density.err
"""

import sympy as sp

lam = sp.symbols("lam")
r = sp.sqrt(2) / 2


def pair_mixer(n, a, b, real_rot=True):
    """balanced real mixer rot(pi/4) on the pair (a, b) of n states, identity elsewhere."""
    M = sp.eye(n)
    M[a, a], M[a, b], M[b, a], M[b, b] = r, -r, r, r
    return M


SQ = sp.symbols("SQ")  # stands for sqrt(2); reduced modulo SQ^2 - 2


def certificate(U):
    """Norm of the characteristic polynomial from Q(sqrt2) down to Q, factored over Q.
    P(lam) = A(lam) + sqrt2 B(lam) with A, B in Q[lam]; N = A^2 - 2 B^2 has the eigenvalues of U and of its
    Galois conjugate as roots; U has finite order iff its conjugate does, iff every irreducible factor of N is
    cyclotomic. Returns (factors, infinite_order_certified)."""
    n = U.shape[0]
    Us = U.subs(sp.sqrt(2), SQ)
    P = sp.expand((lam * sp.eye(n) - Us).det())
    red = sp.rem(sp.Poly(P, SQ), sp.Poly(SQ ** 2 - 2, SQ))
    A = red.coeff_monomial(1)
    B = red.coeff_monomial(SQ)
    N = sp.expand(A ** 2 - 2 * B ** 2)
    fl = sp.factor_list(N, lam)
    factors = []
    certified = False
    for f, mult in fl[1]:
        pf = sp.Poly(f, lam)
        monic = pf.monic()
        mc = [sp.Rational(c) for c in monic.all_coeffs()]
        coeffs_int = all(c.q == 1 for c in mc)
        cyclo = False
        if coeffs_int:
            d = pf.degree()
            for k in range(1, 400):
                if sp.totient(k) == d:
                    ck = [sp.Rational(c) for c in sp.Poly(sp.cyclotomic_poly(k, lam), lam).all_coeffs()]
                    if ck == mc:
                        cyclo = True
                        break
        if not cyclo:
            certified = True
        kind = "cyclotomic" if cyclo else ("not monic over Z" if not coeffs_int else "monic, not cyclotomic")
        factors.append((str(monic.as_expr()), mult, kind))
    return factors, certified


RES = []


def report(cid, U, expect_label):
    U = sp.simplify(U)
    unitary = sp.simplify(U.T * U - sp.eye(U.shape[0])) == sp.zeros(U.shape[0])
    factors, cert = certificate(U)
    print(f"{cid}: unitary={unitary}; factors over Q of the norm of the characteristic polynomial:")
    for f, m, kind in factors:
        print(f"     ({f})^{m}   [{kind}]")
    print(f"     infinite order certified: {cert}  ({expect_label})")
    return unitary, cert


print("== o3_density ==")
print()
# E1: three states
H01 = pair_mixer(3, 0, 1)
H12 = pair_mixer(3, 1, 2)
u1, c1 = report("E1", H01 * H12, "three states, overlapping pairs")


# E2: level 3 of the fixed-gate datum: carrier Fin 2 x Fin 3, index (s, k) -> 3 s + k
def idx(s, k, n):
    return n * s + k


def mix_image(n):
    M = sp.zeros(2 * n)
    for k in range(n):
        a, b = idx(0, k, n), idx(1, k, n)
        M[a, a], M[a, b], M[b, a], M[b, b] = r, -r, r, r
    return M


def shift_perm(n):
    """permutation matrix of (s, k) -> (s, k + s mod n): shifts the ancilla index of s = 1."""
    P = sp.zeros(2 * n)
    for s in range(2):
        for k in range(n):
            P[idx(s, (k + s) % n, n), idx(s, k, n)] = 1
    return P


M1 = mix_image(3)
P3 = shift_perm(3)
M2 = P3 * M1 * P3.T
u2, c2 = report("E2", M1 * M2, "level n = 3 of fixedGateTheory(pi/4)")
M1b = mix_image(2)
P2 = shift_perm(2)
M2b = P2 * M1b * P2.T
u3, c3 = report("E3", M1b * M2b, "level n = 2 (four states)")

print()
print("-- countercontrols")
X = sp.Matrix([[0, 1], [1, 0]])
R = sp.Matrix([[r, -r], [r, r]])
_, cc1 = certificate(R * X)
_, cc2 = certificate(sp.eye(3))
print(f"CC1  {'CC-OK (False as required)' if not cc1 else 'CC-FAIL (True)'}  rot(pi/4).X infinite-order certificate")
print(f"CC2  {'CC-OK (False as required)' if not cc2 else 'CC-FAIL (True)'}  identity has a non-cyclotomic factor")
print()
ok = u1 and u2 and u3 and not cc1 and not cc2
if not ok:
    print("VERDICT VOID")
elif c1 and c2:
    print("VERDICT DENSITY: a balanced mixer and its exchange conjugates generate elements of infinite order on three")
    print(f"  states and at level 3 of the fixed-gate datum (level 2 certified infinite: {c3}); the closure of the generated")
    print("  group then contains a one-parameter subgroup, so the quarter-phase finiteness of o3_continuous C5 is a")
    print("  single-qubit statement only; exactness is a separate matter (kernel: fixedGateTheory_not_qm).")
elif not c1 and not c2:
    print("VERDICT FINITE: no infinite-order certificate at three states or at level 3.")
else:
    print(f"VERDICT MIXED: three states {c1}, level 3 {c2}.")
