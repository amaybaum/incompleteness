# Witness check for PREMISE-MEMO.md §2 ("Collapse under local rotations"), the K(Z_F) defect witness.
# A verification written from the memo's definitions and the construction in dc_premise.py; it does not import or
# read dc_premise.py and is not a probe of any screen. Exact arithmetic only (SymPy integers, Rational, sqrt(2));
# no floating point. Prints measured eigenvalues, PASS/FAIL lines and a verdict generated from them.
#
# Objects (memo §1 notation and §2 witness convention):
#   |ij> = |i>(x)|j>, token 1 first, basis index 2i+j.
#   CN = P0(x)I + P1(x)X, CNOT with control token 1 (as in dc_premise.py).
#   cond_k(Y) = Tr_2[(I(x)P_k) CN Y CN], token 1's conditional after the coupling and native readout k of token 2.
#   Defects z = I/2 - P_m, m = (|00> + b|01> - bd|10> + d|11>)/2, b, d = +-1 (as in dc_premise.py).
#   C is m's coefficient matrix: convention "ji": C_ij = <ji|m>; convention "ij": C_ij = <ij|m>.
#   V = sqrt(2) C^T; I(x)V acts by z -> (I(x)V) z (I(x)V)^dagger.
#
# Claims checked (memo §2, the witness bullets):
#   W1  convention "ji": the outcome-0 conditional has eigenvalue -1/2 for all four defects.
#   W2  convention "ij": eigenvalue -1/2 at outcome 0 exactly for the d = -1 defects.
#   W3  either convention: some outcome's conditional has a negative eigenvalue for all four defects (UPD excludes).
#   W4  mutation V = I: no outcome's conditional has a negative eigenvalue for any defect.
# Decision rule: each claim HOLDS iff its predicate is true on the measured eigenvalues; the verdict is printed only
# if every control K1-K4 passes, otherwise VOID.
import sympy as sp
from sympy import Matrix, Rational as R, eye, sqrt, zeros

res = []
def ok(name, c):
    c = bool(c); res.append(c); print(("PASS " if c else "FAIL ") + name); return c
def kron(A, B): return sp.kronecker_product(A, B)

P0 = Matrix([[1, 0], [0, 0]]); P1 = Matrix([[0, 0], [0, 1]]); X = Matrix([[0, 1], [1, 0]])
CN = kron(P0, eye(2)) + kron(P1, X)
DEFECTS = [(b, d) for b in (1, -1) for d in (1, -1)]

def mvec(b, d): return Matrix([1, b, -b * d, d]) / 2
def defect(b, d, c=1):            # c = 1: the defect I/2 - P_m; other c: the perturbation I/2 - c P_m
    m = mvec(b, d); return eye(4) / 2 - c * (m * m.H)
def coeff(m, conv):
    if conv == "ji": return Matrix(2, 2, lambda i, j: m[2 * j + i])
    if conv == "ij": return Matrix(2, 2, lambda i, j: m[2 * i + j])
    raise ValueError(conv)
def Vmat(b, d, conv): return sqrt(2) * coeff(mvec(b, d), conv).T
def tr2(A): return Matrix(2, 2, lambda i, j: sum(A[2 * i + t, 2 * j + t] for t in range(2)))
def cond(Y, k): return tr2(kron(eye(2), [P0, P1][k]) * CN * Y * CN.H)
def spectrum(M):
    ev = []
    for v, mult in M.eigenvals().items():
        v = sp.nsimplify(sp.simplify(v)); ev += [v] * mult
    if not all(v.is_rational for v in ev): raise SystemExit("non-rational eigenvalue: %r" % (ev,))
    return sorted(ev)
def rotated(z, V): L = kron(eye(2), V); return L * z * L.H
def spectra(z, V): Y = rotated(z, V); return spectrum(cond(Y, 0)), spectrum(cond(Y, 1))
def has_half_neg(ev): return R(-1, 2) in ev
def has_neg(ev): return any(v < 0 for v in ev)

print("# controls")
# K1 the objects are the memo's: m normalized, P_m a projector, z not PSD (eigenvalue -1/2), CN an involution,
#    V unitary in both conventions.
ok("K1 objects: m unit, P_m projector, z has eigenvalue -1/2, CN^2 = I, V unitary (both conventions)",
   all((mvec(b, d).H * mvec(b, d))[0] == 1
       and (mvec(b, d) * mvec(b, d).H) ** 2 == mvec(b, d) * mvec(b, d).H
       and R(-1, 2) in spectrum(defect(b, d))
       and all(sp.simplify(Vmat(b, d, cv) * Vmat(b, d, cv).H - eye(2)) == zeros(2, 2) for cv in ("ji", "ij"))
       for b, d in DEFECTS) and CN * CN == eye(4))
# K2 cond_k is the memo's definition, cross-checked on a generic symbolic Y against the parity blocks it must equal
Ys = Matrix(4, 4, lambda r, c: sp.Symbol("y%d%d" % (r, c)))
ok("K2 cond_0(Y) = even block {00,11} and cond_1(Y) = odd block {01,10} of Y (symbolic Y)",
   sp.simplify(cond(Ys, 0) - Matrix([[Ys[0, 0], Ys[0, 3]], [Ys[3, 0], Ys[3, 3]]])) == zeros(2, 2)
   and sp.simplify(cond(Ys, 1) - Matrix([[Ys[1, 1], Ys[1, 2]], [Ys[2, 1], Ys[2, 2]]])) == zeros(2, 2))
# K3 the predicates can fail: fixed matrices with known spectra
ok("K3 predicates: diag(1/2,-1/2) flagged, diag(1/2,1/2) and diag(1,0) not flagged",
   has_half_neg(spectrum(sp.diag(R(1, 2), R(-1, 2)))) and has_neg(spectrum(sp.diag(R(1, 2), R(-1, 2))))
   and not has_neg(spectrum(sp.diag(R(1, 2), R(1, 2)))) and not has_neg(spectrum(sp.diag(1, 0))))
# K4 countercontrol: the perturbed defects I/2 - (1/4)P_m are PSD, so the same pipeline must report no violation
#    at either outcome, in either convention, for every defect (the witness claims W1-W3 must fail on them)
pert = {(b, d, cv): spectra(defect(b, d, R(1, 4)), Vmat(b, d, cv)) for b, d in DEFECTS for cv in ("ji", "ij")}
ok("K4 countercontrol: perturbed defects I/2 - P_m/4 give no negative eigenvalue (W1-W3 fail on them)",
   not any(has_neg(e0) or has_neg(e1) for e0, e1 in pert.values()))

print("# measured spectra of the outcome-0 and outcome-1 conditionals")
meas = {}
for b, d in DEFECTS:
    for cv, V in (("ji", None), ("ij", None), ("V=I", eye(2))):
        e0, e1 = spectra(defect(b, d), V if V is not None else Vmat(b, d, cv))
        meas[(b, d, cv)] = (e0, e1)
        print("b=%+d d=%+d %-4s outcome0 %s outcome1 %s" % (b, d, cv, e0, e1))

print("# claims")
w1 = ok("W1 convention ji: eigenvalue -1/2 at outcome 0 for all four defects",
        all(has_half_neg(meas[(b, d, "ji")][0]) for b, d in DEFECTS))
w2 = ok("W2 convention ij: eigenvalue -1/2 at outcome 0 exactly for the d = -1 defects",
        all(has_half_neg(meas[(b, d, "ij")][0]) == (d == -1) for b, d in DEFECTS))
w3 = ok("W3 either convention: a negative eigenvalue at some outcome for all four defects (UPD excludes)",
        all(has_neg(meas[(b, d, cv)][0]) or has_neg(meas[(b, d, cv)][1]) for b, d in DEFECTS for cv in ("ji", "ij")))
w4 = ok("W4 mutation V = I: no negative eigenvalue at either outcome for any defect",
        not any(has_neg(e) for b, d in DEFECTS for e in meas[(b, d, "V=I")]))

controls = res[:4]
print("TOTAL %d PASS %d FAIL" % (sum(res), len(res) - sum(res)))
if all(controls):
    print("VERDICT " + "; ".join("%s %s" % (n, "HOLDS" if v else "FAILS")
                                 for n, v in (("W1", w1), ("W2", w2), ("W3", w3), ("W4", w4))))
else:
    print("VERDICT VOID: a control failed")
