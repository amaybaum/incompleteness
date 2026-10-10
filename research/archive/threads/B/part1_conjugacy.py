"""Thread B, part 1 -- the NOT-conjugacy reduction (exact; Fractions, sympy for surds).

1a. The reduction identities, for ARBITRARY rational G (no hypothesis assumed), d = 3, 5, 7:
      G~ = (I (x) g^-1) G (I (x) g),  N_B = g N_A g^-1,  g = 1 (+) h (+) (+-1)  (frame-preserving, u fixed)
      Rt-defect(G~; N_A)        = (I (x) g^-1) Rt-defect(G; N_B) (I (x) g)
      Rc-defect(G~; N_A, N_A)   = (I (x) g^-1) Rc-defect(G; N_A, N_B) (I (x) g)
      F-defect(G~)_{a,b}        = (I (x) g^-1) F-defect(G)_{a, b xor eps}      (g k_b = k_{b xor eps})
    and g orthogonal with g u = u (so g(L) = L; I (x) g preserves min and max).
1b. Constructed conjugate pairs.
    d = 3: the complex CNOT G0 with one N; g a rational rotation of T (and a z-flipping variant);
           G = (I (x) g) G0 (I (x) g^-1) is a genuine two-NOT model (Rc fails for the common N_A, Rt fails for N_A)
           and the reduction returns G0, which meets every one-N relation.
    d = 5: no positive one-N model exists (NB-1), so the d = 5 conjugate pair is ALGEBRAIC: the one-N model
           G0 = E0 (x) I + E1 (x) N + Pi_T (x) Pi_E+ + J Pi_T (x) Pi_V-  (N of split (2,2)) meets F, Rt, Rc and is
           invertible; an exact product witness shows it fails P (as NB-1 requires).  Conjugated and reduced.
    d = 5, 7 positive two-NOT models: conjugating the target copy moves N_B inside its split class only.
1b'. Non-conjugacy of the countermodels' NOTs: exact eigenspace dimensions; similarity invariants differ, so no
    invertible linear map (frame-preserving or not, on either copy) conjugates one to the other.  Plus an exhaustive
    scan of coordinate-diagonal NOT pairs compatible (Rt and Rc) with each J/K gate.
1c. Completeness of the split under the frame stabiliser H = {g orthogonal, g u = u, g z = +-z}: exact sympy
    construction of the conjugator for every d = 2..7 and every p, between the coordinate NOT and a NOT whose +1 space
    is spanned by non-orthonormal rational vectors (the conjugator has surds); also with det g = +1 and g z = z.
    Countercontrol: under the smaller group of signed coordinate permutations the split is NOT complete.
"""
import sys, random
from fractions import Fraction as Fr
import sympy as sy
from blib import *

OUT = []


def check(name, ok, detail=''):
    line = ('PASS ' if ok else 'FAIL ') + name + (('  ' + detail) if detail else '')
    print(line, flush=True)
    OUT.append(ok)
    if not ok:
        print('part1: FAILED')
        sys.exit(1)


rng = random.Random(20261001)          # deterministic; exact arithmetic on the values it produces


def rand_antisym(m):
    A = zeros(m)
    for i in range(m):
        for j in range(i + 1, m):
            x = Fr(rng.randint(-3, 3), rng.randint(1, 4))
            A[i][j] = x; A[j][i] = -x
    return A


def rand_G(n):
    G = {}
    for j in range(n * n):
        G[j] = {i: Fr(rng.randint(-4, 4), rng.randint(1, 3)) for i in range(n * n) if rng.random() < 0.35}
    return G


def coord_not(d, p):
    """N = diag(u: 1; p transverse +1; q transverse -1; z: -1)"""
    return diag([1] + [1] * p + [-1] * (d - 1 - p) + [-1])


def conj(g, N):
    return mm(mm(g, N), inv(g))


# ------------------------------------------------------------------ 1a. the identities, arbitrary G
for d in (3, 5, 7):
    n = d + 1
    sp = Space(n, 2)
    for p in range(d):
        for flip in (False, True):
            NA = coord_not(d, p)
            h = cayley(rand_antisym(d - 1))
            g = frame_preserving(h, flip)
            gi = inv(g)
            NB = conj(g, NA)
            G = rand_G(n)
            Ig, Igi = embed_local(g, 1, sp), embed_local(gi, 1, sp)
            Gt = sp_compose(Igi, sp_compose(G, Ig))
            INA, INB = embed_local(NA, 1, sp), embed_local(NB, 1, sp)
            NAI = embed_local(NA, 0, sp)
            dt = lambda H, N_: sp_sub(sp_compose(N_, sp_compose(H, N_)), H, sp.dim)
            dc = lambda H, NA_, NB_: sp_sub(sp_compose(NA_, sp_compose(H, NA_)), sp_compose(NB_, H), sp.dim)
            lhs_t = dt(Gt, INA); rhs_t = sp_compose(Igi, sp_compose(dt(G, INB), Ig))
            lhs_c = dc(Gt, NAI, INA); rhs_c = sp_compose(Igi, sp_compose(dc(G, NAI, INB), Ig))
            k = corners(n); eps = 1 if flip else 0
            fdef = lambda H, a, b: sp_sub({0: sp_apply(H, tensor_vec([k[a], k[b]], sp))},
                                          {0: tensor_vec([k[a], k[a ^ b]], sp)}, 1)[0]
            f_ok = all(fdef(Gt, a, b) == sp_apply(Igi, fdef(G, a, b ^ eps)) for a in (0, 1) for b in (0, 1))
            gk_ok = all(mv(g, k[b]) == k[b ^ eps] for b in (0, 1))
            ok = (sp_eq(lhs_t, rhs_t, sp.dim) and sp_eq(lhs_c, rhs_c, sp.dim) and f_ok and gk_ok
                  and is_ball_automorphism_fixing_u(g) and is_ball_not(NB) and split_of(NB)[:2] == (p, d - 1 - p))
            if not ok:
                check('1a d=%d p=%d flip=%s' % (d, p, flip), False)
    check('1a d=%d: Rt-, Rc- and F-defects of G~ are the g-conjugates of those of G (random rational G, every p, '
          'g fixing and g flipping z); g orthogonal, g u = u' % d, True)

# a countercontrol for 1a: conjugating on the CONTROL copy by a z-flipping g breaks F (the target copy is the right one)
d = 3; n = 4; sp = Space(n, 2)
G3 = sp_from_dense(complex_cnot_d3())
gflip = frame_preserving(eye(2), True)
Gc = sp_compose(embed_local(inv(gflip), 0, sp), sp_compose(G3, embed_local(gflip, 0, sp)))
check('1a countercontrol: conjugating the CONTROL copy by a corner-swapping g breaks F (complex CNOT)',
      frame_ok(G3, n) and not frame_ok(Gc, n))

# ------------------------------------------------------------------ 1b. constructed conjugate pairs
N3 = coord_not(3, 1)
for flip in (False, True):
    h = cayley([[Fr(0), Fr(1, 2)], [Fr(-1, 2), Fr(0)]])            # rotation by 2 arctan(1/2), not a multiple of 90 deg
    g = frame_preserving(h, flip)
    gi = inv(g)
    NB = conj(g, N3)
    G = sp_compose(embed_local(g, 1, sp), sp_compose(G3, embed_local(gi, 1, sp)))
    Gt = sp_compose(embed_local(gi, 1, sp), sp_compose(G, embed_local(g, 1, sp)))
    GG = sp_compose(G, G)
    check('1b d=3 (g %s z): G = (I(x)g) CNOT (I(x)g^-1) meets F, G^2 = I, Rt(N_B), Rc(N_A, N_B); N_B != N_A, '
          'same split %s; Rt(N_A) and Rc(N_A, N_A) FAIL (a genuine two-NOT model)'
          % ('flipping' if flip else 'fixing', split_of(NB)[:2]),
          frame_ok(G, n) and sp_eq(GG, sp_identity(16), 16) and rel_t(G, n, NB) and rel_c(G, n, N3, NB)
          and NB != N3 and split_of(NB)[:2] == (1, 1) and not rel_t(G, n, N3) and not rel_c(G, n, N3, N3))
    check('1b d=3 (g %s z): the reduction G~ = (I(x)g^-1) G (I(x)g) is the complex CNOT, which meets F, Rt(N_A), '
          'Rc(N_A, N_A) with ONE N' % ('flipping' if flip else 'fixing'),
          sp_eq(Gt, G3, 16) and frame_ok(Gt, n) and rel_t(Gt, n, N3) and rel_c(Gt, n, N3, N3))
print('     NB_d3 (fixing z) =', [[str(x) for x in r] for r in conj(frame_preserving(cayley([[Fr(0), Fr(1, 2)], [Fr(-1, 2), Fr(0)]])), N3)])

# d = 5 algebraic one-N model, N split (2, 2): basis u, x1, x2, y1, y2, z
d = 5; n = 6; sp = Space(n, 2)
N5 = coord_not(5, 2)
J5 = as_mat({1: (1, 3), 3: (-1, 1), 2: (1, 4), 4: (-1, 2)}, n)    # x_i -> y_i, y_i -> -x_i ; anticommutes with N on T
k = corners(n)
E0 = [[k[0][i] * k[0][j] / 2 for j in range(n)] for i in range(n)]
E1 = [[k[1][i] * k[1][j] / 2 for j in range(n)] for i in range(n)]
PiT = diag([0, 1, 1, 1, 1, 0]); PiEp = diag([1, 1, 1, 0, 0, 0]); PiVm = diag([0, 0, 0, 1, 1, 1])
JPiT = mm(J5, PiT)


def kronM(A, B):
    m = len(B)
    return [[A[i // m][j // m] * B[i % m][j % m] for j in range(len(A) * m)] for i in range(len(A) * m)]


G0d = [[a + b + c + e for a, b, c, e in zip(r1, r2, r3, r4)] for r1, r2, r3, r4 in
       zip(kronM(E0, eye(n)), kronM(E1, N5), kronM(PiT, PiEp), kronM(JPiT, PiVm))]
G0 = sp_from_dense(G0d)
inv_ok = rank(G0d) == 36
check('1b d=5 algebraic one-N model G0 (N split (2,2)): F, Rt(N), Rc(N, N), invertible (rank 36), N J N = -J',
      frame_ok(G0, n) and rel_t(G0, n, N5) and rel_c(G0, n, N5, N5) and inv_ok and mm(mm(N5, J5), N5) == neg(J5))
# its positivity failure (NB-1 says it must fail).  Witness found by hand from the value formula
#   value = (1 - f_z)(1 - s_z) + f_T.(s_T - J s_T)   at t = u + y1, g = u - y1:
# s = u + 3/5 z + 4/5 x1, f = u + 3/5 z - 4/5 x1 (pure), giving 4/25 - 16/25 = -12/25.
s_ = [Fr(1), Fr(4, 5), Fr(0), Fr(0), Fr(0), Fr(3, 5)]
f_ = [Fr(1), Fr(-4, 5), Fr(0), Fr(0), Fr(0), Fr(3, 5)]
t_ = [Fr(1), Fr(0), Fr(0), Fr(1), Fr(0), Fr(0)]
g_ = [Fr(1), Fr(0), Fr(0), Fr(-1), Fr(0), Fr(0)]
pure = all(v[0] ** 2 == sum(x * x for x in v[1:]) for v in (s_, f_, t_, g_))
wv = value(G0, [s_, t_], [f_, g_], sp)
check('1b d=5 G0 fails P exactly: pure product state (u + 3/5 z + 4/5 x1) (x) (u + y1), product effect '
      '(u + 3/5 z - 4/5 x1) (x) (u - y1), value %s' % wv, pure and wv == Fr(-12, 25))
hT = cayley(rand_antisym(4))
for flip in (False, True):
    g = frame_preserving(hT, flip); gi = inv(g)
    NB = conj(g, N5)
    G = sp_compose(embed_local(g, 1, sp), sp_compose(G0, embed_local(gi, 1, sp)))
    Gt = sp_compose(embed_local(gi, 1, sp), sp_compose(G, embed_local(g, 1, sp)))
    check('1b d=5 (g %s z): conjugate pair (N_A, N_B = g N_A g^-1), split %s both: G meets F, Rt(N_B), Rc(N_A, N_B) '
          'and fails Rc(N_A, N_A); the reduction returns G0 (one N)' % ('flipping' if flip else 'fixing', split_of(NB)[:2]),
          frame_ok(G, n) and rel_t(G, n, NB) and rel_c(G, n, N5, NB) and not rel_c(G, n, N5, N5)
          and sp_eq(Gt, G0, 36) and rel_t(Gt, n, N5) and rel_c(Gt, n, N5, N5))

# d = 5 and d = 7 POSITIVE two-NOT J/K models: conjugation of the target copy stays inside N_B's split class
J5m = {1: (1, 2), 2: (-1, 1), 3: (1, 4), 4: (-1, 3)}               # x -> y, y -> -x, w1 -> w2, w2 -> -w1
K5m = {2: (1, 5), 5: (-1, 2), 3: (1, 4), 4: (-1, 3)}               # y -> z, z -> -y, w1 -> w2, w2 -> -w1
NA5 = diag([1, 1, -1, 1, -1, -1]); NB5 = diag([1, 1, -1, -1, -1, -1])
GJK5 = jk_gate(5, [1, 1, -1, -1, -1, -1], J5m, K5m)
J7m = {1: (1, 4), 4: (-1, 1), 2: (1, 5), 5: (-1, 2), 3: (1, 6), 6: (-1, 3)}
K7m = {2: (1, 3), 3: (-1, 2), 4: (1, 5), 5: (-1, 4), 6: (1, 7), 7: (-1, 6)}
NA7 = diag([1, 1, 1, 1, -1, -1, -1, -1]); NB7 = diag([1, 1, -1, -1, -1, -1, -1, -1])
GJK7 = jk_gate(7, [1, 1, -1, -1, -1, -1, -1, -1], J7m, K7m)
for (d, G, NA, NB) in ((5, GJK5, NA5, NB5), (7, GJK7, NA7, NB7)):
    n = d + 1; sp = Space(n, 2)
    check('1b\' d=%d J/K two-NOT model: F, G^2 = I, Rt(N_B), Rc(N_A, N_B); split(N_A) = %s, split(N_B) = %s'
          % (d, split_of(NA)[:2], split_of(NB)[:2]),
          frame_ok(G, n) and sp_eq(sp_compose(G, G), sp_identity(n * n), n * n) and rel_t(G, n, NB)
          and rel_c(G, n, NA, NB))
    pa, qa, plus_a, minus_a = split_of(NA); pb, qb, plus_b, minus_b = split_of(NB)
    check('1b\' d=%d: dim ker(N - I), dim ker(N + I) on R^n: N_A (%d, %d) vs N_B (%d, %d) -- different similarity '
          'invariants, so N_B != g N_A g^-1 for EVERY invertible g (in particular every frame-preserving g)'
          % (d, plus_a, minus_a, plus_b, minus_b), (plus_a, minus_a) != (plus_b, minus_b))
    # also no local relabelling (h (x) g) of the pair, and no exchange of roles, can match them: spectra are invariant
    g = frame_preserving(cayley(rand_antisym(d - 1)), False); gi = inv(g)
    Gg = sp_compose(embed_local(g, 1, sp), sp_compose(G, embed_local(gi, 1, sp)))
    NBg = conj(g, NB)
    check('1b\' d=%d: conjugating copy B gives a new valid two-NOT model with N_B\' = g N_B g^-1 of the SAME split %s; '
          'the reduction returns the original J/K map (with its mismatched N_A)' % (d, split_of(NBg)[:2]),
          frame_ok(Gg, n) and rel_t(Gg, n, NBg) and rel_c(Gg, n, NA, NBg)
          and sp_eq(sp_compose(embed_local(gi, 1, sp), sp_compose(Gg, embed_local(g, 1, sp))), G, n * n))
    # exhaustive scan: coordinate-diagonal ball NOTs (u: +1, z: -1, transverse signs free) compatible with G
    found = []
    for sb in range(2 ** (d - 1)):
        nb = [1] + [1 if (sb >> i) & 1 else -1 for i in range(d - 1)] + [-1]
        if not rel_t(G, n, diag(nb)):
            continue
        for sa in range(2 ** (d - 1)):
            na = [1] + [1 if (sa >> i) & 1 else -1 for i in range(d - 1)] + [-1]
            if rel_c(G, n, diag(na), diag(nb)):
                found.append((tuple(na), tuple(nb)))
    splits = sorted(set((split_of(diag(a))[:2], split_of(diag(b))[:2]) for a, b in found))
    check('1b\' d=%d: exhaustive scan of the %d coordinate-diagonal NOT pairs: %d pairs meet Rt and Rc with the J/K map, '
          'splits (N_A, N_B) = %s; none matched' % (d, 4 ** (d - 1), len(found), splits),
          len(found) >= 1 and all(a != b for a, b in splits))

# ------------------------------------------------------------------ 1c. completeness of the split under H
def sym_not_from_plus_space(vecs, m):
    """N_T = 2 P - I, P the orthogonal projector (exact, rational) onto span(vecs) in R^m"""
    if not vecs:
        return -sy.eye(m)
    V = sy.Matrix.hstack(*[sy.Matrix(v) for v in vecs])
    P = V * (V.T * V).inv() * V.T
    return 2 * P - sy.eye(m)


def onb(vecs):
    out = []
    for v in vecs:
        w = sy.Matrix(v)
        for e in out:
            w = w - (e.T * w)[0] * e
        w = sy.simplify(w / sy.sqrt((w.T * w)[0]))
        out.append(w)
    return out


def complement_basis(vecs, m):
    """rational basis of the orthogonal complement of span(vecs) in R^m"""
    if not vecs:
        return [list(sy.eye(m)[:, i]) for i in range(m)]
    V = sy.Matrix.hstack(*[sy.Matrix(v) for v in vecs])
    return [list(c) for c in V.T.nullspace()]


ncases = 0
nirr = 0
for d in range(2, 8):
    m = d - 1
    for p in range(0, m + 1):
        # target NOT: +1 space spanned by the non-orthonormal rational vectors w_i = e_i + e_{i+1} + ... (i < p)
        Wp = []
        for i in range(p):                               # w_i = e_i + (i + 1) e_{m-1}  (e_{m-1} itself if i = m-1)
            v = [0] * m
            v[i] = 1
            if i != m - 1:
                v[m - 1] = i + 1
            Wp.append(v)
        if p and sy.Matrix.hstack(*[sy.Matrix(v) for v in Wp]).rank() < p:
            raise SystemExit('bad +1 space')
        NT2 = sym_not_from_plus_space(Wp, m)
        NT1 = sy.diag(*([1] * p + [-1] * (m - p))) if m else sy.zeros(0, 0)
        # conjugator: map the standard adapted ONB to an ONB adapted to NT2
        Bplus = onb(Wp) if p else []
        Bminus = onb(complement_basis(Wp, m)) if m - p else []
        if m:
            h = sy.Matrix.hstack(*(Bplus + Bminus))
            if h.det().simplify() == -1:                  # make det +1: flip one adapted vector (commutes with NT1)
                h[:, 0] = -h[:, 0]
            ok_h = sy.simplify(h.T * h - sy.eye(m)) == sy.zeros(m, m) and sy.simplify(h.det() - 1) == 0
            ok_c = sy.simplify(h * NT1 * h.T - NT2) == sy.zeros(m, m)
        else:
            ok_h = ok_c = True
        # embed: g = 1 (+) h (+) 1, fixes u and z (so fixes both corners), det +1
        n = d + 1
        g = sy.zeros(n, n); g[0, 0] = 1; g[n - 1, n - 1] = 1
        for i in range(m):
            for j in range(m):
                g[i + 1, j + 1] = h[i, j]
        N1 = sy.diag(1, *([1] * p + [-1] * (m - p)), -1)
        N2 = sy.zeros(n, n); N2[0, 0] = 1; N2[n - 1, n - 1] = -1
        for i in range(m):
            for j in range(m):
                N2[i + 1, j + 1] = NT2[i, j]
        ok_g = sy.simplify(g.T * g - sy.eye(n)) == sy.zeros(n, n) and sy.simplify(g * N1 * g.T - N2) == sy.zeros(n, n)
        irr = any(not x.is_rational for x in g) if m else False
        if not (ok_h and ok_c and ok_g):
            check('1c d=%d p=%d' % (d, p), False)
        ncases += 1
        nirr += int(bool(irr))
check('1c every d = 2..7 and every p: an explicit g in H (orthogonal, g u = u, g z = z, det g = +1) conjugates the '
      'coordinate NOT of split (p, q) to the NOT whose +1 space is spanned by w_i = e_i + (i+1) e_last (non-orthonormal '
      'for p >= 2; exact sympy, %d cases, %d of them with an irrational conjugator)' % (ncases, nirr), ncases == sum(m_ + 1 for m_ in range(1, 7)))

# countercontrol for 1c: under the signed coordinate permutations (a finite subgroup of H) the split is NOT complete
m = 2; NT2 = sym_not_from_plus_space([[1, 1]], m)                 # +1 space spanned by x + y; split (1, 1)
orbit = set()
for perm in ((0, 1), (1, 0)):
    for s0 in (1, -1):
        for s1 in (1, -1):
            P = sy.zeros(2, 2); P[perm[0], 0] = s0; P[perm[1], 1] = s1
            orbit.add(tuple(P * sy.diag(1, -1) * P.T))
check('1c countercontrol: d = 3, N_T = reflection fixing x + y (split (1,1)) is NOT conjugate to diag(1,-1) under '
      'the 8 signed coordinate permutations (orbit %s); completeness needs the full O(T)' % sorted(orbit),
      tuple(NT2) not in orbit)

print('part1: OK -- %d checks' % len(OUT))
