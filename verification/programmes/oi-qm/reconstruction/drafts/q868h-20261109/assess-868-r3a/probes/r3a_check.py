"""ASSESS-868 r3a: exact checks for nits n2 and n6 of REVIEW-868-r3 (WIP / UNVERIFIED).

Generic matrices only. No OI update rule, encoding, record law or mechanism is simulated or
enumerated. Imports nothing from earlier probes; every definition is re-typed here. Kernel
definitions re-typed by hand from fd539e15:
  unit g t = 1 + (exp(i pi t) - 1) (1 - g)/2            SecondOrderCircuit.lean:356 (gateFlow, LiftAudit.lean:47)
  phaseFun tau t z = 1 if tau z = z else exp(-i pi t)    LiftAudit.lean:586
  signFun tau e a z = -1 on the lower member of a moved orbit outside {a, tau a}, else 1   LiftAudit.lean:582
  flow H t = exp(-i t H), transition a b = E_ab + E_ba   ReachabilitySeam.lean:95, LieRankSource.lean:199
Run: python3 -I r3a_check.py

n2  On three states with tau = (01) the sign conjugation of `gateFlow_isolation` (LiftAudit.lean:660)
    is trivial and G(t)^2 = G(2t), so the kernel identity reads
    diag(phaseFun) G(2t) = exp(-i pi t X_01), which at th = pi t is r3 W10's
    exp(-i th X_ab) = exp(-i th) G(2 th/pi) diag(1, 1, exp(i th)). Control: the conjugate phase fails.
n6  Four states, index 2*first + second (r3 W8's convention). The second drive of W8's x+ (x) z+
    preparation, at pi/2 on the pair (|10>, |11>), followed by the exchange of that pair, equals
    S^dagger (x) I exactly (S = diag(1, i), the quarter phase), hence as a channel. It takes the first
    drive's output y+ (x) z+ to x+ (x) z+. Controls: S (x) I gives a different channel, and the drive at
    pi/2 alone is not S^dagger (x) I as a channel.
"""
import sympy as sp

I = sp.I; pi = sp.pi
t, s = sp.symbols('t s', real=True)
res = []


def chk(name, cond):
    res.append((name, bool(cond)))


def z(M):
    return (M.applyfunc(lambda x: sp.simplify(sp.expand_complex(sp.expand(x))))) == sp.zeros(*M.shape)


def nz(M, subs):
    """Exact nonzero witness: some entry is nonzero after exact substitution."""
    N = M.subs(subs).applyfunc(lambda x: sp.nsimplify(sp.simplify(sp.expand_complex(x))))
    return any(e != 0 for e in N)


def perm(p):
    n = len(p); M = sp.zeros(n, n)
    for j in range(n):
        M[p[j], j] = 1
    return M


def unit(g, tt):
    n = g.shape[0]
    return sp.eye(n) + (sp.exp(pi * I * tt) - 1) * (sp.eye(n) - g) / 2


def transition(a, b, n):
    M = sp.zeros(n, n); M[a, b] = 1; M[b, a] = 1
    return M


def drive(a, b, ss, n):
    """Closed form of exp(-i ss X_ab); checked against the generator below."""
    M = sp.eye(n); M[a, a] = sp.cos(ss); M[b, b] = sp.cos(ss)
    M[a, b] = -I * sp.sin(ss); M[b, a] = -I * sp.sin(ss)
    return M


# ---- closed form of the drive: solves U' = -i X_ab U, U(0) = 1 (3 and 4 states) ----
for n, (a, b) in ((3, (0, 1)), (4, (2, 3)), (4, (0, 2))):
    D = drive(a, b, s, n)
    chk(f'drive closed form solves U\' = -i X_ab U, U(0)=1 (n={n}, pair {a},{b})',
        z(D.diff(s) + I * transition(a, b, n) * D) and z(D.subs(s, 0) - sp.eye(n)))

# ---- n2 ----
P01 = perm([1, 0, 2])
G = lambda tt: unit(P01, tt)
chk('n2 gate flow group law on 3 states: G(t) G(t) = G(2t)', z(G(t) * G(t) - G(2 * t)))
# signFun for tau = (01), a = 0: the only moved orbit is {0, 1} = {a, tau a}, so every value is 1
def signFun(tau, a, zz):  # enumeration e = identity
    return -1 if (tau[zz] != zz and not (zz == a or zz == tau[a]) and zz < tau[zz]) else 1
tau3 = [1, 0, 2]
sign3 = [signFun(tau3, 0, zz) for zz in range(3)]
chk('n2 signFun control: active on 4 states with tau = (01)(23), a = 0', [signFun([1, 0, 3, 2], 0, q) for q in range(4)] == [1, 1, -1, 1])
chk('n2 signFun is identically 1 for tau = (01) on three states', sign3 == [1, 1, 1])
Sg = sp.diag(*sign3)
phase = sp.diag(sp.exp(-I * pi * t), sp.exp(-I * pi * t), 1)
lhs = phase * G(t) * (Sg * G(t) * Sg)
chk('n2 kernel lhs (tau = (01), 3 states) = exp(-i pi t X_01)', z(lhs - drive(0, 1, pi * t, 3)))
th = sp.symbols('th', real=True)
w10_rhs = sp.exp(-I * th) * G(2 * th / pi) * sp.diag(1, 1, sp.exp(I * th))
chk('n2 W10 right side at th = pi t equals the kernel lhs', z(w10_rhs.subs(th, pi * t) - lhs))
bad = sp.diag(sp.exp(I * pi * t), sp.exp(I * pi * t), 1) * G(t) * G(t)
chk('n2 control: conjugate phase fails (exact nonzero witness at t = 1/3)',
    nz(bad - drive(0, 1, pi * t, 3), {t: sp.Rational(1, 3)}))

# ---- n6 ----
kron = sp.kronecker_product
S = sp.diag(1, I); Sd = sp.diag(1, -I); I2 = sp.eye(2)
i00, i10, i11 = 0, 2, 3
E = perm([0, 1, 3, 2]) * drive(i10, i11, pi / 2, 4)   # exchange (|10>,|11>) after the drive at pi/2
chk('n6 exchange * drive(pi/2) on (|10>,|11>) = S^dagger (x) I exactly', z(E - kron(Sd, I2)))
hs = sp.symbols('h0:16', real=True)
rho = sp.zeros(4, 4); k = 0
for i in range(4):
    rho[i, i] = hs[k]; k += 1
for i in range(4):
    for j in range(i + 1, 4):
        rho[i, j] = hs[k] + I * hs[k + 1]; rho[j, i] = hs[k] - I * hs[k + 1]; k += 2
SdI = kron(Sd, I2); SI = kron(S, I2)
chk('n6 as channels on a generic Hermitian rho: E rho E^H = (S^dagger x I) rho (S^dagger x I)^H',
    z(E * rho * E.H - SdI * rho * SdI.H))
wit = {hs[q]: q + 1 for q in range(16)}
chk('n6 control: S (x) I is a different channel (exact nonzero witness)',
    nz(E * rho * E.H - SI * rho * SI.H, wit))
D2 = drive(i10, i11, pi / 2, 4)
chk('n6 control: the drive at pi/2 alone is not S^dagger (x) I as a channel (exact nonzero witness)',
    nz(D2 * rho * D2.H - SdI * rho * SdI.H, wit))
k10 = sp.zeros(4, 1); k10[i10] = 1
yplus = sp.Matrix([1, I]) / sp.sqrt(2); xplus = sp.Matrix([1, 1]) / sp.sqrt(2); zplus = sp.Matrix([1, 0])
psi1 = drive(i00, i10, pi / 4, 4) * k10
proj = lambda v: v * v.H
chk('n6 first drive at pi/4 takes |10> to y+ (x) z+ (projectors)', z(proj(psi1) - proj(kron(yplus, zplus))))
chk('n6 S^dagger takes y+ to x+ exactly', z(Sd * yplus - xplus))
chk('n6 full preparation E * drive(pi/4) |10> = x+ (x) z+ (projectors)',
    z(proj(E * psi1) - proj(kron(xplus, zplus))))

fails = [n for n, ok in res if not ok]
for n, ok in res:
    print(('PASS ' if ok else 'FAIL ') + n)
print(f'{len(res)} checks, {len(fails)} failures')
raise SystemExit(1 if fails else 0)
