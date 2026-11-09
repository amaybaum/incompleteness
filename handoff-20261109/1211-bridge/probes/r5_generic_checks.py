"""EXACT GENERIC CHECKS FOR BRIDGE-UNIT1 r5 (generic mathematical objects only).

Run under the owner's permission in #1211 c.6739843458 ("Allow generic checks (as #1210)").
Labelled controls on algebra stated in the r5 text (R4-B1, R4-B2, r4-n6); not evidence for any
physical result. No OI mechanism is run: no cubic lattice, no ring rule of the corpus, no
encoding of the corpus, no kernel object is imported or executed. The matrices below are the
textbook objects the kernel definitions name (transition generator E_ab + E_ba; gate flow
1 + (e^{i pi t} - 1)(1 - P)/2 of a permutation matrix P with P^2 = 1), rebuilt here by hand.
Imports no earlier script. Exact arithmetic only (sympy, symbolic real angle).

The drive is written in closed form U(th) = I + (cos th - 1) X^2 - i sin th X. It is certified
as exp(-i th X) exactly: U(0) = I and dU/dth = -i X U symbolically (uniqueness of the linear
ODE solution), with X^3 = X asserted.

I   Isolation form (R4-B1), symbolic th, on 3 and 4 states, X = X_ab:
    (a) exp(-i th X_ab) = e^{-i th} G_(ab)(2 th/pi) diag(1, 1, e^{i th}[, e^{i th}]);
    (b) the kernel-shaped identity for a single transposition (sign function trivially 1):
        diag(phase(t)) G(t) G(t) = exp(-i pi t X_ab), phase(t) = e^{-i pi t} on a, b, 1 elsewhere;
    (c) group law G(t) G(s) = G(t + s);
    countercontrol: without the relative phase the identity (a) fails.
Y   Ray and monomiality (r4-n6), symbolic th:
    (a) on 3 and 4 states the drive sends 1 to e^{-i th}(e_a + e_b) + rest; it is proportional
        to 1 iff e^{-i th} = 1 (entry a / entry c = e^{-i th});
    (b) the drive is monomial iff sin th cos th = 0 (pair block entries cos th, -i sin th);
    (c) control: on 2 states the drive keeps 1 on its ray for all th;
    (d) control: the gate flow keeps 1 fixed for all t.
Q   Quarter turn (R4-B1):
    (a) exp(-i pi/2 X_ab) swap(a b) = -i diag(1, 1, i) on 3 states;
    (b) its conjugation channel equals the quarter phase's on c (all nine matrix units);
    (c) with permutation transport, the quarter-phase channel on every state of the 3-state level;
    (d) at th = pi/2 the drive is monomial and moves the all-ones ray;
    countercontrols: the exchange alone does not act as the quarter phase; on two states the
    quarter-turn drive times the exchange is a scalar (no third state, no relative phase).
R  Real-rotation countercontrol (R4-B1, R4-B2), R(th) = exp(th (E_ab - E_ba)):
    (a) real orthogonal for all th; at th = pi/4 non-monomial, moves the all-ones ray, and does
        not preserve a diagonal state;
    (b) Lie algebras with permutation transport, as real vector spaces: rotation generators
        close on dimension 3 (so(3)); drive generators i X close on dimension 8 (su(3));
    (c) every conjugation channel of a real matrix sends the real matrix E_ac + E_ca to a real
        matrix; the quarter phase on c sends it to a non-real one; so no word in real
        rotations and permutations acts as the quarter phase.
H   r4-n3 (reviewer-supplied CHSH witness, closed form): for the maximally entangled two-qubit
    state, observables in the x-z plane at 0, 2 al (one wing) and al, -al (other wing),
    CHSH = 6 cos al - 4 cos^3 al for every al, = 344/125 at cos al = 4/5.
"""
import itertools
import sympy as sp

ok = True


def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


th, s, t = sp.symbols("theta s t", real=True)
I = sp.I
pi = sp.pi


def zero(M):
    return all(sp.simplify(sp.expand_complex(sp.expand(e.rewrite(sp.exp)))) == 0 for e in M)


def E(n, i, j):
    M = sp.zeros(n)
    M[i, j] = 1
    return M


def Xab(n, a=0, b=1):
    return E(n, a, b) + E(n, b, a)


def drive(n, ang, a=0, b=1):
    X = Xab(n, a, b)
    assert X ** 3 == X
    return sp.eye(n) + (sp.cos(ang) - 1) * X ** 2 - I * sp.sin(ang) * X


def perm_matrix(n, p):
    M = sp.zeros(n)
    for i in range(n):
        M[p[i], i] = 1
    return M


def swap(n, a=0, b=1):
    p = list(range(n))
    p[a], p[b] = b, a
    return perm_matrix(n, p)


def G(n, tt, a=0, b=1):
    P = swap(n, a, b)
    return sp.eye(n) + (sp.exp(I * pi * tt) - 1) * (sp.eye(n) - P) / 2


def is_monomial(M):
    n = M.shape[0]
    rows = all(sum(1 for j in range(n) if sp.simplify(M[i, j]) != 0) == 1 for i in range(n))
    cols = all(sum(1 for i in range(n) if sp.simplify(M[i, j]) != 0) == 1 for j in range(n))
    return rows and cols


def on_ray_ones(v):
    n = v.shape[0]
    return all(sp.simplify(v[i] - v[0]) == 0 for i in range(n)) and sp.simplify(v[0]) != 0


def channel(V, Xm):
    return V * Xm * V.H


# certification of the closed form as the exponential
for n in (2, 3, 4):
    U = drive(n, th)
    X = Xab(n)
    check(f"exp n={n}: U(0) = I", U.subs(th, 0) == sp.eye(n))
    check(f"exp n={n}: dU/dth = -i X U (symbolic)", zero(U.diff(th) + I * X * U))

# ---------------- I ----------------
for n in (3, 4):
    U = drive(n, th)
    D = sp.diag(1, 1, *([sp.exp(I * th)] * (n - 2)))
    check(f"I(a) n={n}: exp(-i th X_ab) = e^(-i th) G(2th/pi) diag(1,1,e^(i th),..) (all th)",
          zero(U - sp.exp(-I * th) * G(n, 2 * th / pi) * D))
    ph = sp.diag(sp.exp(-I * pi * t), sp.exp(-I * pi * t), *([1] * (n - 2)))
    check(f"I(b) n={n}: diag(phase(t)) G(t) G(t) = exp(-i pi t X_ab) (all t)",
          zero(ph * G(n, t) * G(n, t) - drive(n, pi * t)))
    check(f"I(c) n={n}: G(t) G(s) = G(t+s)", zero(G(n, t) * G(n, s) - G(n, t + s)))
    check(f"I countercontrol n={n}: without the relative phase diag(1,1,e^(i th)) the identity fails",
          not zero(U - sp.exp(-I * th) * G(n, 2 * th / pi)))
check("zero() rejects a nonzero matrix (sanity)", not zero(sp.Matrix([[sp.exp(I * th) - 1]])))

# ---------------- Y ----------------
for n in (3, 4):
    U = drive(n, th)
    one = sp.ones(n, 1)
    target = sp.exp(-I * th) * (E(n, 0, 0) + E(n, 1, 1)) * one + sum(
        (E(n, c, c) * one for c in range(2, n)), sp.zeros(n, 1))
    check(f"Y(a) n={n}: drive sends 1 to e^(-i th)(e_a+e_b) + rest (all th)", zero(U * one - target))
    w = U * one
    check(f"Y(a) n={n}: entry a / entry c = e^(-i th), so on the ray iff e^(-i th) = 1",
          zero(sp.Matrix([w[0] / w[2] - sp.exp(-I * th)])))
blk = drive(3, th)[0:2, 0:2]
check("Y(b) pair block entries are cos th (diagonal) and -i sin th (off-diagonal)",
      zero(blk - sp.Matrix([[sp.cos(th), -I * sp.sin(th)], [-I * sp.sin(th), sp.cos(th)]])))
mono_pts = [0, pi / 2, pi, 3 * pi / 2]
non_pts = [pi / 4, pi / 3, 2 * pi / 3, sp.Rational(1, 2)]
check("Y(b) monomial at th in {0, pi/2, pi, 3pi/2}", all(is_monomial(drive(3, a)) for a in mono_pts))
check("Y(b) non-monomial at th in {pi/4, pi/3, 2pi/3, 1/2}",
      all(not is_monomial(drive(3, a)) for a in non_pts))
moves = [pi / 4, pi / 2, pi, 3 * pi / 2, sp.Rational(1, 2)]
check("Y(a) n=3: moves the ray at th in {pi/4, pi/2, pi, 3pi/2, 1/2}; keeps it at th = 2pi",
      all(not on_ray_ones(drive(3, a) * sp.ones(3, 1)) for a in moves)
      and on_ray_ones(drive(3, 2 * pi) * sp.ones(3, 1)))
v2 = drive(2, th) * sp.ones(2, 1)
check("Y(c) control n=2: drive keeps 1 on its ray (all th)",
      zero(v2 - sp.exp(-I * th) * sp.ones(2, 1)))
check("Y(d) control: gate flow fixes 1 (n=3, all t)", zero(G(3, t) * sp.ones(3, 1) - sp.ones(3, 1)))

# ---------------- Q ----------------
Uq = drive(3, pi / 2)
Sc = sp.diag(1, 1, I)
check("Q(a) exp(-i pi/2 X_ab) swap(a b) = -i diag(1,1,i)", zero(Uq * swap(3) - (-I) * Sc))
units = [E(3, i, j) for i in range(3) for j in range(3)]
W = Uq * swap(3)
check("Q(b) its conjugation channel equals the quarter phase's on c (all matrix units)",
      all(zero(channel(W, M) - channel(Sc, M)) for M in units))
allstates = True
for p in itertools.permutations(range(3)):
    Pm = perm_matrix(3, p)
    Wp = Pm * W * Pm.T
    target_state = p[2]
    St = sp.diag(*[I if k == target_state else 1 for k in range(3)])
    allstates = allstates and all(zero(channel(Wp, M) - channel(St, M)) for M in units)
check("Q(c) with permutation transport: quarter-phase channel on every state of the level",
      allstates)
check("Q countercontrol: the exchange alone does not act as the quarter phase on c",
      not all(zero(channel(swap(3), M) - channel(Sc, M)) for M in units))
check("Q countercontrol: on two states drive(pi/2) swap is the scalar -i (no relative phase)",
      zero(drive(2, pi / 2) * swap(2) - (-I) * sp.eye(2)))
check("Q(d) at th = pi/2 the drive is monomial and moves the all-ones ray",
      is_monomial(Uq) and not on_ray_ones(Uq * sp.ones(3, 1)))

# ---------------- R ----------------
def rot(n, ang, a=0, b=1):
    A = E(n, a, b) - E(n, b, a)
    assert A ** 3 == -A
    return sp.eye(n) + sp.sin(ang) * A + (1 - sp.cos(ang)) * A ** 2


R = rot(3, th)
A = E(3, 0, 1) - E(3, 1, 0)
check("R exp: R(0) = I and dR/dth = A R (symbolic)", R.subs(th, 0) == sp.eye(3) and zero(R.diff(th) - A * R))
check("R(a) real orthogonal for all th", zero(R.T * R - sp.eye(3)) and all(sp.im(e) == 0 for e in R))
R4 = rot(3, pi / 4)
diag_state = sp.diag(1, 0, 0)
out = channel(R4, diag_state)
check("R(a) at pi/4: non-monomial, moves the all-ones ray, does not preserve a diagonal state",
      not is_monomial(R4) and not on_ray_ones(R4 * sp.ones(3, 1))
      and any(sp.simplify(out[i, j]) != 0 for i in range(3) for j in range(3) if i != j))


def realvec(M):
    v = []
    for e in M:
        e = sp.expand_complex(sp.nsimplify(e))
        v += [sp.re(e), sp.im(e)]
    return v


def lie_closure_dim(gens):
    basis = []

    def rank(ms):
        return sp.Matrix([realvec(m) for m in ms]).rank() if ms else 0

    for g in gens:
        if rank(basis + [g]) > len(basis):
            basis.append(g)
    changed = True
    while changed:
        changed = False
        for x, y in itertools.product(list(basis), repeat=2):
            c = sp.expand(x * y - y * x)
            if rank(basis + [c]) > len(basis):
                basis.append(c)
                changed = True
    return len(basis)


def transported(M):
    out = []
    for p in itertools.permutations(range(3)):
        Pm = perm_matrix(3, p)
        out.append(Pm * M * Pm.T)
    return out


d_rot = lie_closure_dim(transported(A))
d_drv = lie_closure_dim(transported(I * Xab(3)))
check(f"R(b) rotation generators with permutation transport close on dim {d_rot} (so(3) = 3)", d_rot == 3)
check(f"R(b) drive generators i X with permutation transport close on dim {d_drv} (su(3) = 8)", d_drv == 8)
M = E(3, 0, 2) + E(3, 2, 0)
img_q = channel(Sc, M)
check("R(c) quarter phase on c sends E_ac + E_ca to a non-real matrix",
      any(sp.im(sp.expand_complex(e)) != 0 for e in img_q))
check("R(c) control: real rotation and a permutation send it to real matrices",
      all(sp.im(sp.expand_complex(e)) == 0 for e in channel(R4 * swap(3), M)))

# ---------------- H ----------------
# r4-n3: maximally entangled state |Phi+>, observables cos(x) Z + sin(x) X on each wing,
# wing 1 at angles 0, 2 al; wing 2 at al, -al. CHSH = E00 + E01 + E10 - E11.
al = sp.symbols("alpha", real=True)
Z = sp.Matrix([[1, 0], [0, -1]])
Xp = sp.Matrix([[0, 1], [1, 0]])
phi = sp.Matrix([1, 0, 0, 1]) / sp.sqrt(2)


def obs(x):
    return sp.cos(x) * Z + sp.sin(x) * Xp


def corr(x, y):
    return sp.simplify((phi.T * sp.kronecker_product(obs(x), obs(y)) * phi)[0, 0])


chsh = corr(0, al) + corr(0, -al) + corr(2 * al, al) - corr(2 * al, -al)
check("H CHSH = 6 cos(al) - 4 cos(al)^3 for every al (closed form)",
      sp.simplify(sp.expand_trig(chsh - (6 * sp.cos(al) - 4 * sp.cos(al) ** 3))) == 0)
c = sp.Rational(4, 5)
check("H at cos(al) = 4/5: CHSH = 344/125 > 2", 6 * c - 4 * c ** 3 == sp.Rational(344, 125) > 2)

print("ALL PASS" if ok else "SOME FAIL")
