"""EQ3-P probe p2 -- Amendments 1-2 audit of the four-copy instance, twisted configurations, general charts, and the
exact foils (independent content of KT at four copies).  Research only; base bcbc516f.  Usage (from scratchpad/eq3/P):
  python3 -I -B p2_audit_twists_foils.py <base>/.../OIBridge/CompositeDimension.lean <base>/.../OIBridge/K2Guard.lean

Instance KT(4; 01|23, 02|13): one four-copy body is a COMP-1 composite of (01)|(23) and of (02)|(13); each pair body
is the group's full body, its effects every IsEffectOn functional (KInfFoundations:116).  Table calculus of p1:
family (i) <X, E.Y.F^T> >= 0 (states on 01, 23; effects on 02, 13); family (ii) L.f.L'^T in cl K_01 (states on 02,
13; effect on 23; conditioning on 01|23).

CHECKS (exact; symbolic unless stated):
  P  link provenance (Amendment 1(b), Amendment 2):
     P1 sharpVec b = hom(b)/2 (EffectSpace:57) and the product effect table sharp(xplus) (x) sharp(z3) =
        prodState(xplus, z3)/4 pairs with every table as pairVal (sharpVec xplus) (sharpVec z3)   [product effect]
     P2 dual action: <cnot E, w> = <E, cnot w> (symbolic) and cnot(sharp (x) sharp) = Delta/4: the Bell EFFECT is
        the dual image of a product effect; cnot fixes the unit effect table and the unit coordinate
     P3 twisted orientation: R_B = actT reflY and cnot' = R_B cnot R_B are Euclidean-self-adjoint involutions;
        cnot'(prodState xplus z3) = idW (twin Bell STATE) and cnot'(sharp (x) sharp) = idW/4 (twin Bell EFFECT)
     P4 link-induced maps: Bell links (Delta, Delta) induce T; twin links (idW, idW) induce the identity; mixed links
        (Delta on 02, idW on 13) induce reflY on copy 0 only, i.e. PT on the first token (operator check)
     P5 the other link family (03)(12): conditioning L(03) L'(12) on f(23) leaves L.f^T.L'^T on (0,1); with Bell
        links this is T(swap f)
  N  non-uniform pair cones (Amendment 1(a)): with arbitrary pair cones K_01, K_23 and Bell links on 02, 13,
     (I) needs only the link STATES and gives T(K_23*) <= K_01; (II) needs only the link EFFECTS and gives
     K_01 <= T(K_23*) -- recorded as the symbolic identities of families (ii) and (i) with distinct tables
  U  general token charts (no alignment): for exact rational orthogonal A, B, A', B' (proper and improper),
     post-local l1 = (A, B) on pair (0,2) and (A', B') on (1,3), Theta(g) = H_R02 g H_R13^T with R = A reflY B^T:
     U1 Bell links l1(Delta) induce Theta; U2 with f = Theta^-1(X), the filter-link conditional equals
        4 (H_A M_D H_A^T) X (H_A' M_D' H_A'^T)^T (symbolic X, u, u'): conjugated local filters on K_01
  Z  twisted configurations: for every twist assignment tau on the four pairs (01, 23, 02, 13), with Bell_tau =
     Delta (tau = 0) or idW (tau = 1): Z1 the derived relation K_01 = Theta_tau(K_23*) with K_ij = R_B^tau_ij Q3 is
     consistent iff tau_01 + tau_13 + tau_23 + tau_02 is even (sign-map algebra, witness Delta in Q3 \ Tw);
     Z2 own recomputation of the four-copy test: over the 4 Bell-type tables and their twists, a negative family-(i)
     value exists iff the parity is odd (16 assignments); Z3 even parity is realized by K4 = PT_S(PSD_16): the pair
     marginals of PT_S(rho) are PT_{S cap pair}(marginal) (one exact random 16x16 instance per S, all four pairs)
  F  foils:
     F1 K_F = cone(<octahedral locals, cnot> . products): own BFS, order 11520; every generator is Ad of an explicit
        unitary (Pauli-dictionary identity); psi = (1,1,1,2): max |r_A|^2 over its orbit = 45/49 <= (24/25)^2, so
        w = effect table of (49/50) 1 - psi psi^dag is in K_F*; f = effect table of psi psi^dag is in K_F*; Delta in
        K_F; four-copy value <w (x) f, Delta(02) (x) Delta(13)> = -1/200 < 0: K_F violates the instance
     F2 gate-free foils SEP and max satisfy the instance (product-table identities) and fail the gate:
        <coordsW(1 - 2 Phi+)/4, Delta> = -1 with that table in max (value on products (1 - x.Delta y)/2 >= 0), and
        cnot(idW) = chainW with pairVal(sharp(-e1), sharp(-e3), chainW) = -1/2 while idW is in max
     F3 restricted effects: w is in K_F* but not PSD (eigenvalue -1/50 on psi): the effect set Q3 is a strict
        restriction of K_F*; K_F's generators are PSD (so K_F with effects Q3 satisfies the restricted instance)
     F4 non-closed: psi psi^dag is not in conv(SEP u cnot SEP) (it is outside K_F, witness w)
  Q  converse: K = Q3, K4 = PSD_16 (p1 F1); twin configurations by Z3
DECISION RULE (fixed before the first run): verdict `P2-AUDIT-TWISTS-FOILS-EXACT` iff every check passes, including the
landed controls (cnot(prodState xplus z3) = phiW, cnot(idW) = chainW), the transcription controls and the
countercontrols (Z2 even cases nonnegative over the candidates; F1 control: a pure product's orbit reaches |r_A|^2 = 1;
F2 controls).  Otherwise VERDICT NOT RENDERED.  Exact arithmetic only.
"""
import itertools
import os
import random
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp  # noqa: E402
from sympy import I, Matrix, Rational as R, eye, zeros  # noqa: E402

import eq3_lib as L  # noqa: E402

check, note = L.check, L.note
cd_path, k2_path = sys.argv[1], sys.argv[2]
rng = random.Random(77)

tabs = L.parse_cnot(cd_path)
sgn, pc, pt = tabs
phiW = L.parse_phiW(cd_path)
idW, chainW, refl = L.parse_k2guard(k2_path)
check("T0 transcription controls: parsed cnot tables, phiW, idW, chainW, reflY equal the hand transcriptions",
      {(i, j) for i in range(4) for j in range(4) if sgn[i][j] == -1} == L.HAND_SGN_NEG and pc == L.HAND_PC
      and pt == L.HAND_PT and phiW == L.HAND_PHIW and idW == L.HAND_IDW and chainW == L.HAND_CHAINW
      and refl == [1, -1, 1])
cnot = L.cnot_from(tabs)
DEL = L.DELTA
check("T1 landed controls: cnot(prodState xplus z3) = phiW (CD:1222), cnot(idW) = chainW (K2G:110)",
      cnot(L.prod_state(L.XPLUS, L.Z3)) == phiW and cnot(idW) == chainW)


def symtab(name):
    return Matrix(4, 4, lambda m, n: sp.Symbol(f"{name}{m}{n}", real=True))


Wv, Wu = symtab("w"), symtab("v")


def sharp(b):
    return [R(1, 2)] + [sp.sympify(t) / 2 for t in b]


def outer(a, b):
    return Matrix(4, 4, lambda m, n: a[m] * b[n])


# ---------------------------------------------------------------- P link provenance
xs = sp.symbols("x0:3", real=True)
check("P1 sharpVec b = hom(b)/2 (EffectSpace:57) and the product effect table sharp(xplus) (x) sharp(z3) = "
      "prodState(xplus, z3)/4, with <that table, w> = pairVal (sharpVec xplus) (sharpVec z3) w (symbolic w)",
      sharp(xs) == [sp.Integer(1) / 2] + [t / 2 for t in xs]
      and L.zero(outer(sharp(L.XPLUS), sharp(L.Z3)) - L.prod_state(L.XPLUS, L.Z3) / 4)
      and sp.expand(L.eucl(outer(sharp(L.XPLUS), sharp(L.Z3)), Wv) - L.pair_val(sharp(L.XPLUS), sharp(L.Z3), Wv)) == 0)
U = Matrix(4, 4, lambda m, n: 1 if (m, n) == (0, 0) else 0)       # the unit effect table: <U, w> = w_00
check("P2 dual action: <cnot E, w> = <E, cnot w> (symbolic); cnot(sharp(xplus) (x) sharp(z3)) = Delta/4 (the Bell "
      "EFFECT is the dual image of a product effect); cnot fixes the unit effect table and the unit coordinate",
      sp.expand(L.eucl(cnot(Wu), Wv) - L.eucl(Wu, cnot(Wv))) == 0
      and L.zero(cnot(outer(sharp(L.XPLUS), sharp(L.Z3))) - DEL / 4) and cnot(U) == U
      and sp.expand(cnot(Wv)[0, 0] - Wv[0, 0]) == 0)


def RB(w):
    return L.actT(L.REFLY, w)


def cnotp(w):
    return RB(cnot(RB(w)))


check("P3 twisted orientation: R_B and cnot' = R_B cnot R_B are involutions and Euclidean-self-adjoint (symbolic); "
      "cnot'(prodState xplus z3) = idW (twin Bell STATE) and cnot'(sharp (x) sharp) = idW/4 (twin Bell EFFECT); "
      "cnot' fixes the unit",
      L.zero(RB(RB(Wv)) - Wv) and L.zero(cnotp(cnotp(Wv)) - Wv)
      and sp.expand(L.eucl(RB(Wu), Wv) - L.eucl(Wu, RB(Wv))) == 0
      and sp.expand(L.eucl(cnotp(Wu), Wv) - L.eucl(Wu, cnotp(Wv))) == 0
      and cnotp(L.prod_state(L.XPLUS, L.Z3)) == idW and L.zero(cnotp(outer(sharp(L.XPLUS), sharp(L.Z3))) - idW / 4)
      and cnotp(U) == U)
f = symtab("f")
mixed = DEL * f * idW.T
check("P4 link-induced maps (symbolic f): Bell links give Delta.f.Delta = T f; twin links give idW.f.idW^T = f; mixed "
      "links (Delta on 02, idW on 13) give Delta.f, whose operator is PT on the first token: pauliW(Delta.f) = "
      "PT_1(pauliW f) -- so Phi+ induces T, R_B Phi+ induces no transpose, a mixed pair induces one partial transpose",
      L.zero(DEL * f * DEL - L.transposeW(f)) and L.zero(idW * f * idW.T - f)
      and L.zero(L.pauliW(mixed) - L.pt_copy(L.pauliW(f), 0, 2)))
Lm, Lp = symtab("l"), symtab("k")
cond0312 = Matrix(4, 4, lambda a, b: sp.expand(sum(Lm[a, d] * Lp[b, c] * f[c, d] for c in range(4) for d in range(4))))
check("P5 links on (0,3), (1,2): conditioning L(03) L'(12) on f(23) leaves L.f^T.L'^T on (0,1) (symbolic); with Bell "
      "links it is T(swap f) = Delta.f^T.Delta",
      L.zero(cond0312 - Lm * f.T * Lp.T) and L.zero(DEL * f.T * DEL - L.transposeW(L.swapW(f))))

# ---------------------------------------------------------------- N non-uniform pair cones
X1, Y1, E1, F1 = symtab("X"), symtab("Y"), symtab("E"), symtab("F")
val_i = sp.expand(sum(E1[a, c] * F1[b, d] * X1[a, b] * Y1[c, d] for a, b, c, d in itertools.product(range(4), repeat=4)))
cond_ii = Matrix(4, 4, lambda a, b: sp.expand(sum(Lm[a, c] * Lp[b, d] * f[c, d] for c in range(4) for d in range(4))))
check("N1 inclusion (I) [states on 02|13, effect products on 01|23, conditioning on 01|23, Bell link as STATE]: with "
      "L = L' = Delta the conditional of f(23) on (0,1) is T f, so T(K_23*) <= cl K_01 -- no identification of "
      "K_01 with K_23 is used (symbolic)", L.zero(cond_ii.subs({**{Lm[i, j]: DEL[i, j] for i in range(4)
                                                                     for j in range(4)},
                                                                  **{Lp[i, j]: DEL[i, j] for i in range(4)
                                                                     for j in range(4)}}) - L.transposeW(f)))
check("N2 inclusion (II) [states on 01|23, effect products on 02|13, no conditioning, Bell link as EFFECT]: with "
      "E = F = Delta the value is <X, T Y>, so T(K_23) <= K_01*, i.e. K_01 <= T(K_23*) (symbolic)",
      sp.expand(val_i.subs({**{E1[i, j]: DEL[i, j] for i in range(4) for j in range(4)},
                            **{F1[i, j]: DEL[i, j] for i in range(4) for j in range(4)}})
                - L.eucl(X1, L.transposeW(Y1))) == 0)

# ---------------------------------------------------------------- U general token charts
def rat_rot(seed):
    r2 = random.Random(seed)
    a, b, c = (R(r2.randint(-4, 4), r2.randint(1, 3)) for _ in range(3))
    S = Matrix([[0, -a, -b], [a, 0, -c], [b, c, 0]])
    return ((eye(3) - S) * (eye(3) + S).inv()).applyfunc(sp.expand)


A, B = rat_rot(1), rat_rot(2) * L.REFLY          # B improper
Ap, Bp = rat_rot(3) * L.REFLY, rat_rot(4)        # A' improper
okorth = all(L.zero(M.T * M - eye(3)) for M in (A, B, Ap, Bp)) and A.det() == 1 and B.det() == -1 \
    and Ap.det() == -1 and Bp.det() == 1
H = L.hom_map
R02, R13 = A * L.REFLY * B.T, Ap * L.REFLY * Bp.T


def Theta(g):
    return H(R02) * g * H(R13).T


def Theta_inv(g):
    return H(R02).T * g * H(R13)


check("U1 general charts: exact rational orthogonal A, B (det -1), A' (det -1), B'; the Bell links l1(Delta) = "
      "H_A Delta H_B^T = H_R02 and H_A' Delta H_B'^T = H_R13, so the Bell-link conditional is Theta(f) = "
      "H_R02 f H_R13^T with R = A reflY B^T in O(3) (symbolic f)",
      okorth and L.zero(H(A) * DEL * H(B).T - H(R02)) and L.zero(H(Ap) * DEL * H(Bp).T - H(R13))
      and L.zero(H(A) * DEL * H(B).T * f * (H(Ap) * DEL * H(Bp).T).T - Theta(f)))
ur, ui, vr, vi = sp.symbols("ur ui vr vi", real=True)
u, up = ur + I * ui, vr + I * vi


def proj(v):
    return (v * v.H).applyfunc(sp.expand)


def P_a(z):
    ca = L.coords1(proj(Matrix([1, z])))
    hz = L.hom(L.Z3)
    return Matrix(4, 4, lambda m, n: ca[m] * hz[n])


La, Lap = cnot(P_a(u)), cnot(P_a(up))
MD, MDp = La * DEL / 2, Lap * DEL / 2
Xs = symtab("y")
lhs_U2 = (H(A) * La * H(B).T * Theta_inv(Xs) * (H(Ap) * Lap * H(Bp).T).T).applyfunc(sp.expand)
rhs_U2 = (4 * (H(A) * MD * H(A).T) * Xs * (H(Ap) * MDp * H(Ap).T).T).applyfunc(sp.expand)
check("U2 general charts: with links l1(cnot(P_a)) on (0,2), (1,3) and f = Theta^-1(X), the conditional is "
      "4 (H_A M_D H_A^T) X (H_A' M_D' H_A'^T)^T: K_01 is invariant under the A-conjugated local filters (symbolic X, u, "
      "u'; no chart alignment used)", L.zero(lhs_U2 - rhs_U2))

# ---------------------------------------------------------------- Z twisted configurations
BELL = [sp.diag(1, 1, -1, 1), sp.diag(1, -1, 1, 1), sp.diag(1, 1, 1, -1), sp.diag(1, -1, -1, -1)]


def bell_tau(t):
    return DEL if t == 0 else idW


ok_z1 = True
for tau in itertools.product((0, 1), repeat=4):           # (t01, t23, t02, t13)
    t01, t23, t02, t13 = tau
    # Theta_tau(g) = Bell_t02 . g . Bell_t13^T ; K_ij = R_B^t_ij Q3 (Q3* = Q3, Tw* = Tw in tables)
    # the composite sign map S = R_B^t01 . Theta_tau . R_B^t23 is diagonal; Q3 is preserved iff it is 1 or T,
    # tested on the witness Delta (in Q3, not in Tw): S(Delta) must be Delta.
    S_img = bell_tau(t02) * (DEL * (DEL if t23 else eye(4))) * bell_tau(t13).T
    S_img = S_img * (DEL if t01 else eye(4))
    consistent = (S_img == DEL)            # the composite map is g -> Delta^a g Delta^b; Q3-preserving iff a = b
    ok_z1 = ok_z1 and (consistent == ((t01 + t23 + t02 + t13) % 2 == 0))
check("Z1 for all 16 twist assignments on (01, 23, 02, 13): K_01 = Theta_tau(K_23*) with K_ij = R_B^tau_ij Q3 is "
      "consistent iff tau_01 + tau_13 + tau_23 + tau_02 is even (image of the Bell table under the composite sign "
      "map; Delta is in Q3 and not in Tw)", ok_z1)


def val_i_num(Xt, Yt, Et, Ft):
    return L.eucl(Xt, Et * Yt * Ft.T)


ok_z2, mins = True, []
for tau in itertools.product((0, 1), repeat=4):
    t01, t23, t02, t13 = tau
    cand = lambda t: [Bm * DEL if t else Bm for Bm in BELL]  # noqa: E731
    mval = min(val_i_num(Xb, Yb, Eb, Fb) for Xb in cand(t01) for Yb in cand(t23) for Eb in cand(t02)
               for Fb in cand(t13))
    mins.append(("".join(map(str, tau)), mval))
    ok_z2 = ok_z2 and ((mval < 0) == ((t01 + t23 + t02 + t13) % 2 == 1))
check("Z2 own recomputation of the four-copy test: over the Bell-type tables and their twists, a negative family-(i) "
      "value exists iff the 4-cycle parity is odd (16 assignments; even cases nonnegative over the candidates)", ok_z2,
      " ".join(f"{k}:{v}" for k, v in mins))


def ptrace_pair(M, pair):
    return L.ptrace_keep(M, list(pair), 4)


ok_z3 = True
rho16 = L.rand_herm(random.Random(5), 16)
for Sset in itertools.chain.from_iterable(itertools.combinations(range(4), k) for k in range(5)):
    Mt = rho16
    for q in Sset:
        Mt = L.pt_copy(Mt, q, 4)
    for pair in ((0, 1), (2, 3), (0, 2), (1, 3)):
        lhs = ptrace_pair(Mt, pair)
        rhs = ptrace_pair(rho16, pair)
        for t_, q in enumerate(pair):
            if q in Sset:
                rhs = L.pt_copy(rhs, t_, 2)
        ok_z3 = ok_z3 and L.zero(lhs - rhs)
check("Z3 even parity is realized: for every S in {0,1,2,3}, the pair marginals of PT_S(rho) are PT_{S cap pair} of "
      "the marginals (exact random 16x16 instance, pairs 01, 23, 02, 13), so K4 = PT_S(PSD_16) has pair cones "
      "R_B^([i in S] + [j in S]) Q3 (Tw = PT_1 Q3 = PT_2 Q3): every coboundary twist pattern has a quantum K4", ok_z3)

# ---------------------------------------------------------------- F1 the Clifford cone K_F violates the instance
def rot(axis):
    if axis == "z":
        return Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])      # (x,y,z) -> (-y, x, z)
    return Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])          # (x,y,z) -> (x, -z, y)


Uz = sp.diag(1, I)                       # Ad(Uz): X -> Y, Y -> -X
Ux = Matrix([[1, -I], [-I, 1]])          # 1 - iX (unnormalized): Ad: Y -> -Z... checked below
gens = [("C z", lambda w: L.actC(rot("z"), w), L.kron(Uz, L.S0)), ("C x", lambda w: L.actC(rot("x"), w), L.kron(Ux, L.S0)),
        ("T z", lambda w: L.actT(rot("z"), w), L.kron(L.S0, Uz)), ("T x", lambda w: L.actT(rot("x"), w), L.kron(L.S0, Ux)),
        ("cnot", cnot, L.CNOT_U)]
okad = True
for name, g, Uop in gens:
    lhs = L.pauliW(g(Wv))
    rhs = (Uop * L.pauliW(Wv) * Uop.H).applyfunc(sp.expand)
    nrm = sp.expand((Uop.H * Uop)[0, 0])
    okad = okad and L.zero(lhs * nrm - rhs) and L.zero(Uop.H * Uop - nrm * eye(4))
check("F1 every generator of <octahedral locals, cnot> is Ad of an explicit unitary (up to a positive scalar): "
      "pauliW(g w) = U pauliW(w) U^dag (symbolic w); hence every group element preserves PSD and products' images "
      "are pure states", okad)


def to_vec(M):
    return tuple(Fr(int(sp.numer(M[m, n])), int(sp.denom(M[m, n]))) for m in range(4) for n in range(4))


def signed_perm(g):
    """16x16 signed permutation of table entries, read off from the images of the basis tables."""
    cols = []
    for k in range(16):
        Eb = zeros(4, 4)
        Eb[k // 4, k % 4] = 1
        img = g(Eb)
        nz = [(i, img[i // 4, i % 4]) for i in range(16) if img[i // 4, i % 4] != 0]
        assert len(nz) == 1 and nz[0][1] in (1, -1)
        cols.append((nz[0][0], int(nz[0][1])))
    return tuple(cols)                    # basis k -> sign * basis cols[k][0]


def compose(p, q):                        # (p o q)
    return tuple((p[i][0], p[i][1] * s) for (i, s) in q)


IDP = tuple((k, 1) for k in range(16))
gen_perms = [signed_perm(g) for _, g, _ in gens]
seen = {IDP}
frontier = [IDP]
while frontier:
    new = []
    for h in frontier:
        for gp in gen_perms:
            c = compose(gp, h)
            if c not in seen:
                seen.add(c)
                new.append(c)
    frontier = new
group = list(seen)


def act(p, vec):
    out = [Fr(0)] * 16
    for k in range(16):
        if vec[k] != 0:
            i, s = p[k]
            out[i] += s * vec[k]
    return out


psi = Matrix([1, 1, 1, 2])
rho_psi = psi * psi.T / 7
f_state = L.coordsW(rho_psi)                     # state table of psi psi^dag (w_00 = 1)
fv = to_vec(f_state)
orbit_r2 = []
for p in group:
    img = act(p, fv)
    orbit_r2.append(sum(img[4 * k] ** 2 for k in (1, 2, 3)) / img[0] ** 2)
prod_v = to_vec(L.prod_state([1, 0, 0], [0, 0, 1]))
prod_r2 = max(sum(act(p, prod_v)[4 * k] ** 2 for k in (1, 2, 3)) for p in group)
check("F1 the group generated by the local octahedral rotations and cnot has order 11520 (own BFS on signed "
      "permutations of the 16 table entries)", len(group) == 11520, len(group))
check("F1 psi = (1,1,1,2)/sqrt7: every orbit element has marginal Bloch norm^2 <= 45/49 < (24/25)^2 = 576/625, so the "
      "largest Schmidt weight is <= 49/50 on the whole orbit; control: a pure product's orbit reaches 1",
      max(orbit_r2) == Fr(45, 49) and max(orbit_r2) <= Fr(576, 625) and prod_r2 == 1, f"max = {max(orbit_r2)}")
W_op = R(49, 50) * eye(4) - rho_psi
w_eff = L.coordsW(W_op) / 4                      # effect table of W_op
f_eff = L.coordsW(rho_psi) / 4                   # effect table of psi psi^dag
val4 = L.eucl(w_eff, DEL * f_eff * DEL)          # family (ii): states Delta(02) Delta(13), effects w(01) f(23)
check("F1 four-copy witness: states Delta on (0,2) and (1,3) (Delta = cnot(prodState xplus z3) is in K_F), effects w "
      "on (0,1) and f on (2,3) (both in K_F*: w by the orbit bound, f is PSD and K_F <= Q3): the value <w, Delta.f.Delta> "
      "= tr(W_op (psi psi^dag)^T)/4 = -1/200 < 0, so K_F violates KT(4; 01|23, 02|13)",
      val4 == R(-1, 200) and sp.expand((W_op * rho_psi.T).trace() / 4 - val4) == 0, val4)

# ---------------------------------------------------------------- F2 gate-free foils
a_, b_, c_, d_ = (Matrix(sp.symbols(f"{s}0:4", real=True)) for s in "abcd")
Es, Fs = symtab("e"), symtab("g")
check("F2 SEP and max satisfy the instance without a gate (symbolic product-table identities): "
      "<a b^T, E (c d^T) F^T> = (a^T E c)(b^T F d) and <p r^T, Lm (q s^T) Lp^T> = (p^T Lm q)(r^T Lp s), so with "
      "product states and block-positive effects (SEP) or block-positive states and product effects (max) every "
      "family value is a product of two nonnegative numbers",
      sp.expand(L.eucl(a_ * b_.T, Es * (c_ * d_.T) * Fs.T) - (a_.T * Es * c_)[0] * (b_.T * Fs * d_)[0]) == 0
      and sp.expand(L.eucl(a_ * c_.T, Lm * (b_ * d_.T) * Lp.T) - (a_.T * Lm * b_)[0] * (c_.T * Lp * d_)[0]) == 0)
phip = Matrix([1, 0, 0, 1]) * Matrix([1, 0, 0, 1]).T / 2
wit = L.coordsW(eye(4) - 2 * phip) / 4
ys = sp.symbols("y0:3", real=True)
onprod = sp.expand(L.eucl(wit, L.prod_state(xs, ys)) - (1 - sum(xs[k] * DEL[k + 1, k + 1] * ys[k] for k in range(3))) / 2)
check("F2 SEP fails the gate: the effect table of 1 - 2 Phi+ takes the value (1 - x.Delta y)/2 >= 0 on every product "
      "(so it is in max = SEP*) and the value -1 on Delta = cnot(prodState xplus z3): cnot(SEP) is not in SEP",
      onprod == 0 and L.eucl(wit, DEL) == -1)
check("F2 max fails the gate: idW is in max (its value on products is |<a|b>|^2-type: pairVal(hom x, hom y, idW) = "
      "1 + x.y >= 0) and cnot(idW) = chainW with pairVal(sharp(-e1), sharp(-e3), chainW) = -1/2 (K2Guard's chain)",
      sp.expand(L.pair_val(L.hom(xs), L.hom(ys), idW) - (1 + sum(xs[k] * ys[k] for k in range(3)))) == 0
      and L.pair_val(sharp([-1, 0, 0]), sharp([0, 0, -1]), chainW) == R(-1, 2))

# ---------------------------------------------------------------- F3 / F4
ev = (W_op * psi)[0] / psi[0]
check("F3 restricted effects: w (in K_F*) is not PSD: W_op psi = (-1/50) psi, so the effect set Q3 is a strict "
      "restriction of K_F*; K_F's generators g(products) are PSD (F1), so K_F with effect set Q3 satisfies the "
      "instance with K4 = conv of the two product sets (written; PSD_16 bounds it)",
      L.zero(W_op * psi - R(-1, 50) * psi) and ev == R(-1, 50))
check("F4 non-closed foil ingredient: psi psi^dag is outside K_F (the witness w is nonnegative on K_F and "
      "<w, coordsW(psi psi^dag)> = 49/50 - 1 = -1/50), hence outside conv(SEP u cnot SEP) <= K_F",
      L.eucl(w_eff, f_state) == R(-1, 50))

ok = L.summary("p2_audit_twists_foils")
print("VERDICT " + ("P2-AUDIT-TWISTS-FOILS-EXACT" if ok else "NOT RENDERED"))
sys.exit(0 if ok else 1)
