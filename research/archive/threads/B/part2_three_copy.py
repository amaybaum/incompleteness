"""Thread B, part 2 -- three-copy consistency of mismatched NOT splits (exact; Fractions only).

THE RELATIONS, stated before any computation.  Copies A, B, C of the d-ball; a used ordered pair (X -> Y) carries a
native CNOT G_XY on X (x) Y (X control, Y target), embedded in the three-copy space with the identity on the third copy.
  R2  (pairwise, every used ordered pair X -> Y):  F, P+-, Rt with the target NOT of Y, Rc with (control NOT of X,
      target NOT of Y)  -- NB-1's hypotheses in their two-NOT reading.
  T1  common control:  G_XY G_XZ = G_XZ G_XY.
  T2  common target:   G_XZ G_YZ = G_YZ G_XZ.
  T3  the chain identity (CNOT truth-table identity, extended off the frame as an operator identity):
          G_BC G_AB G_BC G_AB = G_AC         (composition right to left)
  T4  composite positivity: every product of used gates maps product states into the maximal tensor cone
      (checked as: value on product effects >= 0).  Exact here only through a reduction identity plus the written
      disc argument; floating point only as labelled exploration.
  NOT assumed anywhere: SWAP, any exchange relation, G_YX determined by G_XY, any continuous local group.

Two NOT models.
  MODEL I  (per copy, role-independent): copy X carries ONE NOT N_X, used both when X is a control and a target.
           Different copies may carry different NOTs (that is the mismatch).
  MODEL II (per type, role-dependent): every copy carries the same pair (N^c, N^t): N^c when it is a control,
           N^t when it is a target; the same gate matrix for every ordered pair.  The NB-1 two-NOT countermodel is
           exactly this data with N^c = N_A, N^t = N_B.

Sections.
  2.1  Model I, necessary conditions (two-NOT reading of NB-1: target p <= 1, control p = q), exhaustive over the
       63 non-empty sets of used ordered pairs on {A, B, C} and all split assignments, d = 5 and d = 7.
  2.2  Model I, existence for the role-pure patterns (out-star, in-star) with J/K gates, d = 5 and d = 7: R2, T1, T2,
       G^2 = I exactly; the generated group with the local NOTs, by exact BFS; T4 through the reduction identity: the
       composite's value tensor equals F(invariants) with the SAME coefficient tensor as the d = 3 quantum composite.
       Countercontrol (matched case): d = 3 complex CNOT with one N on every copy: R2, T1, T2, T3 all hold.
  2.3  The two-NOT reading's preconditions on the J/K models: S1/S2 structure with the TARGET NOT holds and with the
       control NOT fails; G maps T (x) V-(N_B) into itself and anticommutes there with N_A (x) I.
  2.4  Model II and T3: the corner-sector lemma (T3 => Rc(N_B^t, N_C^t) for G_BC) checked exactly on positive and
       negative controls; the J/K Model II at d = 5, 7: R2, T1, T2 hold, T3 fails, the defect identity
       D1 = G D2 holds; a T4 witness for the two-copy composite G_BA G_AB of the J/K Model II gate.
"""
import sys
from itertools import product, combinations
from fractions import Fraction as Fr
from blib import *

OUT = []


def check(name, ok, detail=''):
    print(('PASS ' if ok else 'FAIL ') + name + (('  ' + detail) if detail else ''), flush=True)
    OUT.append(ok)
    if not ok:
        print('part2: FAILED')
        sys.exit(1)


print(__doc__.split('Two NOT models.')[0])

# ------------------------------------------------------------------ models
MODELS = {}
# d = 3 quantum: N = diag(1, 1, -1, -1) on u, x, y, z; J: x -> y, y -> -x; K: y -> z, z -> -y
G3 = sp_from_dense(complex_cnot_d3())
MODELS[3] = dict(n=4, G=G3, NA=diag([1, 1, -1, -1]), NB=diag([1, 1, -1, -1]),
                 J={1: (1, 2), 2: (-1, 1)}, K={2: (1, 3), 3: (-1, 2)}, x=1)
MODELS[5] = dict(n=6, G=jk_gate(5, [1, 1, -1, -1, -1, -1], {1: (1, 2), 2: (-1, 1), 3: (1, 4), 4: (-1, 3)},
                                 {2: (1, 5), 5: (-1, 2), 3: (1, 4), 4: (-1, 3)}),
                 NA=diag([1, 1, -1, 1, -1, -1]), NB=diag([1, 1, -1, -1, -1, -1]),
                 J={1: (1, 2), 2: (-1, 1), 3: (1, 4), 4: (-1, 3)}, K={2: (1, 5), 5: (-1, 2), 3: (1, 4), 4: (-1, 3)}, x=1)
MODELS[7] = dict(n=8, G=jk_gate(7, [1, 1, -1, -1, -1, -1, -1, -1],
                                 {1: (1, 4), 4: (-1, 1), 2: (1, 5), 5: (-1, 2), 3: (1, 6), 6: (-1, 3)},
                                 {2: (1, 3), 3: (-1, 2), 4: (1, 5), 5: (-1, 4), 6: (1, 7), 7: (-1, 6)}),
                 NA=diag([1, 1, 1, 1, -1, -1, -1, -1]), NB=diag([1, 1, -1, -1, -1, -1, -1, -1]),
                 J={1: (1, 4), 4: (-1, 1), 2: (1, 5), 5: (-1, 2), 3: (1, 6), 6: (-1, 3)},
                 K={2: (1, 3), 3: (-1, 2), 4: (1, 5), 5: (-1, 4), 6: (1, 7), 7: (-1, 6)}, x=1)

COP = 'ABC'


def gates3(G, n, pairs):
    sp = Space(n, 3)
    return sp, {pr: embed_two(G, n, pr, sp) for pr in pairs}


# ------------------------------------------------------------------ 2.1 Model I necessary conditions
ALL_PAIRS = [(X, Y) for X in range(3) for Y in range(3) if X != Y]
for d in (5, 7):
    surv_total = 0; surv_mism = 0; conflict_mism = 0; patterns = set()
    for mask in range(1, 64):
        used = [ALL_PAIRS[i] for i in range(6) if (mask >> i) & 1]
        ctrl = {X for X, Y in used}; targ = {Y for X, Y in used}
        involved = sorted(ctrl | targ)
        for ps in product(range(d), repeat=3):
            ok = all(ps[Y] <= 1 for Y in targ) and all(ps[X] == d - 1 - ps[X] for X in ctrl)
            mism = len({ps[X] for X in involved}) > 1
            if ok:
                surv_total += 1
                if mism:
                    surv_mism += 1
                    patterns.add((tuple(sorted(used)), tuple(ps[X] for X in range(3))))
                    if ctrl & targ:
                        conflict_mism += 1
    # every surviving pattern is role-pure (no copy both control and target)
    role_pure = all(not ({X for X, Y in u} & {Y for X, Y in u}) for u, _ in patterns)
    shapes = sorted({('out-star' if len({X for X, Y in u}) == 1 and len(u) == 2 else
                      'in-star' if len({Y for X, Y in u}) == 1 and len(u) == 2 else
                      'single edge' if len(u) == 1 else 'other') for u, _ in patterns})
    check('2.1 d=%d Model I: of all (used-pair set, split assignment) configurations meeting the necessary conditions, '
          '%d have mismatched splits; every one is role-pure (no copy both control and target); shapes %s; '
          'control splits forced to (%d,%d), target p in {0,1}'
          % (d, surv_mism, shapes, (d - 1) // 2, (d - 1) // 2),
          surv_mism > 0 and conflict_mism == 0 and role_pure and shapes == ['in-star', 'out-star', 'single edge'])
    # with a role conflict, the necessary conditions leave only d in {1, 3}: p <= 1 and p = d - 1 - p
    check('2.1 d=%d Model I: a copy in both roles needs p <= 1 and p = d - 1 - p, impossible for d = %d '
          '(possible only for d in {1, 3})' % (d, d),
          not any(p <= 1 and p == d - 1 - p for p in range(d)) and any(p <= 1 and p == 3 - 1 - p for p in range(3)))

# ------------------------------------------------------------------ 2.2 Model I existence (role-pure)
for d in (5, 7):
    M = MODELS[d]; n = M['n']; G = M['G']; NA = M['NA']; NB = M['NB']
    for shape, used, nots in (('out-star', [(0, 1), (0, 2)], [NA, NB, NB]),
                              ('in-star', [(0, 2), (1, 2)], [NA, NA, NB])):
        sp, g = gates3(G, n, used)
        sp2 = Space(n, 2)
        # R2 for every used pair, with the per-copy NOTs (pairwise objects: two-copy checks)
        r2 = all(frame_ok(G, n) and rel_t(G, n, nots[Y]) and rel_c(G, n, nots[X], nots[Y]) for X, Y in used)
        # the same relations as three-copy operator identities (embedded)
        r2e = True
        for X, Y in used:
            NX = embed_local(nots[X], X, sp); NY = embed_local(nots[Y], Y, sp)
            r2e &= sp_eq(sp_compose(NY, sp_compose(g[(X, Y)], NY)), g[(X, Y)], sp.dim)
            r2e &= sp_eq(sp_compose(NX, sp_compose(g[(X, Y)], NX)), sp_compose(NY, g[(X, Y)]), sp.dim)
        a, b = used
        comm = sp_eq(sp_compose(g[a], g[b]), sp_compose(g[b], g[a]), sp.dim)
        invol = all(sp_eq(sp_compose(g[e], g[e]), sp_identity(sp.dim), sp.dim) for e in used)
        check('2.2 d=%d Model I %s, NOTs (A, B, C) splits %s: R2 for both used pairs (two-copy and embedded), %s, '
              'G^2 = I' % (d, shape, [split_of(N_)[:2] for N_ in nots], 'T1' if shape == 'out-star' else 'T2'),
              r2 and r2e and comm and invol)
        # the group generated with the three local NOTs: exact BFS
        gens = [g[e] for e in used] + [embed_local(nots[X], X, sp) for X in range(3)]
        key = lambda A: tuple(sorted((j, tuple(sorted(c.items()))) for j, c in A.items()))
        seen = {key(sp_identity(sp.dim)): sp_identity(sp.dim)}
        frontier = [sp_identity(sp.dim)]
        while frontier:
            new = []
            for A in frontier:
                for Gn in gens:
                    B = sp_compose(Gn, A)
                    kB = key(B)
                    if kB not in seen:
                        seen[kB] = B; new.append(B)
            frontier = new
        # every element is L * (gate word) with L a product of local NOTs and gate word in {I, g_a, g_b, g_a g_b}
        locs = []
        for e in product((0, 1), repeat=3):
            L = sp_identity(sp.dim)
            for X in range(3):
                if e[X]:
                    L = sp_compose(embed_local(nots[X], X, sp), L)
            locs.append(L)
        words = [sp_identity(sp.dim), g[a], g[b], sp_compose(g[a], g[b])]
        normal = {key(sp_compose(L, W)) for L in locs for W in words}
        check('2.2 d=%d Model I %s: the group generated by the used gates and the local NOTs has order %d, and every '
              'element is (local NOTs) x (I, G1, G2 or G1 G2)' % (d, shape, len(seen)),
              len(seen) == 32 and set(seen) == normal)


# T4 through the reduction identity.  Per-copy bilinear forms (matrices B with value f^T B s):
def forms(M, role):
    n = M['n']; d = n - 1
    E = lambda i, j: [[Fr(int((a, b) == (i, j))) for b in range(n)] for a in range(n)]
    if role == 'c':
        T = list(range(1, d)); Jm = as_mat(M['J'], n)
        P1 = [[Fr(int(a == b and a in T)) for b in range(n)] for a in range(n)]
        P2 = [[Jm[a][b] if (a in T and b in T) else Fr(0) for b in range(n)] for a in range(n)]
        return [E(0, 0), E(0, d), E(d, 0), E(d, d), P1, P2]          # 1, s_z, f_z, f_z s_z, f.s, f.Js
    x = M['x']; Vm = [i for i in range(1, n) if M['NB'][i][i] == -1]; Km = as_mat(M['K'], n)
    Q1 = [[Fr(int(a == b and a in Vm)) for b in range(n)] for a in range(n)]
    Q2 = [[Km[a][b] if (a in Vm and b in Vm) else Fr(0) for b in range(n)] for a in range(n)]
    return [E(0, 0), E(0, x), E(x, 0), E(x, x), Q1, Q2]              # 1, t_x, g_x, g_x t_x, g-.t-, g-.Kt-


def frob(A, B):
    return sum(A[i][j] * B[i][j] for i in range(len(A)) for j in range(len(A)))


def dual(Bs):
    Gm = [[frob(a, b) for b in Bs] for a in Bs]
    Gi = inv(Gm)
    n = len(Bs[0])
    return [[[sum(Gi[k][l] * Bs[l][i][j] for l in range(len(Bs))) for j in range(n)] for i in range(n)]
            for k in range(len(Bs))]


def decompose(W, sp, F3):
    """W (sparse map on the 3-copy space; W[out][in]) against products of per-copy forms; returns (coeffs, exact?)"""
    n = sp.n
    D = [dual(F) for F in F3]
    coeff = {}
    for al in range(6):
        for be in range(6):
            for ga in range(6):
                c = Fr(0)
                for j, col in W.items():
                    l, m, o = sp.digits(j)
                    for i, x in col.items():
                        a, b, cc = sp.digits(i)
                        c += x * D[0][al][a][l] * D[1][be][b][m] * D[2][ga][cc][o]
                if c != 0:
                    coeff[(al, be, ga)] = c
    # reconstruct and compare
    R = {}
    for (al, be, ga), c in coeff.items():
        A_, B_, C_ = F3[0][al], F3[1][be], F3[2][ga]
        for a in range(n):
            for l in range(n):
                if A_[a][l] == 0: continue
                for b in range(n):
                    for m in range(n):
                        if B_[b][m] == 0: continue
                        for cc in range(n):
                            for o in range(n):
                                if C_[cc][o] == 0: continue
                                j = sp.idx([l, m, o]); i = sp.idx([a, b, cc])
                                R.setdefault(j, {})
                                R[j][i] = R[j].get(i, Fr(0)) + c * A_[a][l] * B_[b][m] * C_[cc][o]
    R = {j: {i: x for i, x in col.items() if x != 0} for j, col in R.items()}
    return coeff, sp_eq(R, W, sp.dim)


for shape, used, roles in (('out-star', [(0, 1), (0, 2)], 'ctt'), ('in-star', [(0, 2), (1, 2)], 'cct')):
    coeffs = {}
    for d in (3, 5, 7):
        M = MODELS[d]; n = M['n']
        sp, g = gates3(M['G'], n, used)
        F3 = [forms(M, r) for r in roles]
        res = {}
        for lab, W in (('G1', g[used[0]]), ('G2', g[used[1]]), ('G2 G1', sp_compose(g[used[1]], g[used[0]]))):
            c, exact = decompose(W, sp, F3)
            if not exact:
                check('2.2 %s d=%d %s: value tensor lies in the span of the invariant forms' % (shape, d, lab), False)
            res[lab] = c
        coeffs[d] = res
    same = all(coeffs[d] == coeffs[3] for d in (5, 7))
    check('2.2 T4 %s: for G1, G2 and G2 G1 the value tensor equals F(invariants) EXACTLY at d = 3, 5, 7 '
          '(invariants per control copy: s_z, f_z, f.s, f.Js; per target copy: t_x, g_x, g-.t-, g-.Kt-), and the '
          'coefficient tensor F is the same at d = 5 and 7 as for the d = 3 quantum composite (%d, %d, %d nonzero '
          'coefficients)' % (shape, len(coeffs[3]['G1']), len(coeffs[3]['G2']), len(coeffs[3]['G2 G1'])), same)

# matched countercontrol: d = 3 quantum, one N on every copy, all relations including T3
M = MODELS[3]; n = 4; N = M['NA']
sp, g = gates3(M['G'], n, ALL_PAIRS)
ok = all(rel_t(M['G'], n, N) and rel_c(M['G'], n, N, N) for _ in [0])
t1 = all(sp_eq(sp_compose(g[(X, Y)], g[(X, Z)]), sp_compose(g[(X, Z)], g[(X, Y)]), sp.dim)
         for X in range(3) for Y in range(3) for Z in range(3) if len({X, Y, Z}) == 3)
t2 = all(sp_eq(sp_compose(g[(X, Z)], g[(Y, Z)]), sp_compose(g[(Y, Z)], g[(X, Z)]), sp.dim)
         for X in range(3) for Y in range(3) for Z in range(3) if len({X, Y, Z}) == 3)
t3 = all(sp_eq(sp_compose(g[(Y, Z)], sp_compose(g[(X, Y)], sp_compose(g[(Y, Z)], g[(X, Y)]))), g[(X, Z)], sp.dim)
         for X in range(3) for Y in range(3) for Z in range(3) if len({X, Y, Z}) == 3)
check('2.2 countercontrol (matched): d = 3 complex CNOT, one N on every copy, all six ordered pairs: R2, T1, T2 and '
      'T3 (all six labelings) hold exactly; T4 holds by quantum theory (the gates are unitary channels)',
      ok and t1 and t2 and t3)

# ------------------------------------------------------------------ 2.3 two-NOT reading: preconditions on J/K models
def s1_s2_structure(G, n, nu):
    """NB-1 probe's S1/S2 structure test (copied), nu = eigenvalues of the TARGET NOT on 1..d"""
    d = n - 1; k = corners(n); e = eye(n); sp2 = Space(n, 2)
    full = {}
    for j in range(n * n):
        full[j] = G.get(j, {})
    Gd = [[full[j].get(i, Fr(0)) for j in range(n * n)] for i in range(n * n)]
    def matvec(A, v): return [sum(A[i][j] * v[j] for j in range(len(v)) if v[j] != 0) for i in range(len(A))]
    def kron(a, b): return [x * y for x in a for y in b]
    Ms = []
    for a in (0, 1):
        Ma = zeros(n)
        for j in range(n):
            img = matvec(Gd, kron(k[a], e[j]))
            row_u = img[0:n]
            if [img[i * n + jj] for i in range(n) for jj in range(n)] != [k[a][i] * row_u[jj] for i in range(n) for jj in range(n)]:
                return False
            for i in range(n): Ma[i][j] = row_u[i]
        Ms.append(Ma)
    iso = all(mm(tr(Ma), Ma) == eye(n) for Ma in Ms)
    Nm = diag([1] + nu)
    if mm(Nm, Ms[0]) != Ms[1]:
        return False
    Vp = [i for i in range(1, d) if nu[i - 1] == 1]; Vm = [i for i in range(1, n) if nu[i - 1] == -1]
    M0inv = tr(Ms[0])
    Gt = [[sum(Gd[r][c * n + l] * M0inv[l][tj] for l in range(n)) for c in range(n) for tj in range(n)] for r in range(n * n)]
    col = lambda ci, tj: [Gt[r][ci * n + tj] for r in range(n * n)]
    ok = True
    for c in range(1, d):
        cu = col(c, 0)
        ok &= all(cu[i * n + j] == 0 for i in range(n) for j in [0] + Vm)
        ok &= all(cu[i * n + j] == 0 for i in [0, d] for j in range(n))
        for r_ in Vp:
            cr = col(c, r_)
            ok &= all(cr[i * n + 0] == cu[i * n + r_] for i in range(n))
            ok &= all(cr[i * n + j] == 0 for i in range(n) for j in Vm)
            for s_ in Vp:
                cs = col(c, s_)
                ok &= all(cr[i * n + s_] == -cs[i * n + r_] for i in range(n))
        for j_ in Vm:
            cj = col(c, j_)
            ok &= all(cj[i * n + jj] == 0 for i in range(n) for jj in [0] + Vp)
            for l_ in Vm:
                cl = col(c, l_)
                ok &= all(cj[i * n + l_] == -cl[i * n + j_] for i in range(n))
    return iso and ok


for d in (5, 7):
    M = MODELS[d]; n = M['n']; G = M['G']; NA = M['NA']; NB = M['NB']
    nuB = [NB[i][i] for i in range(1, n)]; nuA = [NA[i][i] for i in range(1, n)]
    T = list(range(1, d)); VmB = [i for i in range(1, n) if NB[i][i] == -1]
    sub = [c * n + t for c in T for t in VmB]
    inv_ok = all(set(G.get(j, {})) <= set(sub) for j in sub)
    anti = all(all(G[j].get(i, 0) * NA[i // n][i // n] == -NA[j // n][j // n] * G[j].get(i, 0) for i in G[j]) for j in sub)
    rk = rank([[G[j].get(i, Fr(0)) for j in sub] for i in sub]) == len(sub)
    check('2.3 d=%d two-NOT J/K model: S1/S2 structure holds with the TARGET NOT N_B and FAILS with the control NOT '
          'N_A; G maps T (x) V-(N_B) into itself, injectively, anticommuting with N_A (x) I there (S5 in its two-NOT '
          'reading: p_A = q_A = %d)' % (d, (d - 1) // 2),
          s1_s2_structure(G, n, nuB) and not s1_s2_structure(G, n, nuA) and inv_ok and anti and rk)

# ------------------------------------------------------------------ 2.4 Model II and T3
def t3_holds(gAB, gBC, gAC, dim):
    return sp_eq(sp_compose(gBC, sp_compose(gAB, sp_compose(gBC, gAB))), gAC, dim)


# lemma controls at d = 3: frames conjugated on copy B
n = 4; sp = Space(n, 3); sp2 = Space(n, 2); N = MODELS[3]['NA']
gB = frame_preserving(cayley([[Fr(0), Fr(1, 2)], [Fr(-1, 2), Fr(0)]]))
gBi = inv(gB); NBc = mm(mm(gB, N), gBi)
CN = MODELS[3]['G']
G_AB = sp_compose(embed_local(gB, 1, sp2), sp_compose(CN, embed_local(gBi, 1, sp2)))   # target NOT on B: g N g^-1
G_BCc = sp_compose(embed_local(gB, 0, sp2), sp_compose(CN, embed_local(gBi, 0, sp2)))  # Rc(gNg^-1, N), Rt(N)
eAB = embed_two(G_AB, n, (0, 1), sp); eAC = embed_two(CN, n, (0, 2), sp)
eBCc = embed_two(G_BCc, n, (1, 2), sp); eBCp = embed_two(CN, n, (1, 2), sp)
check('2.4 lemma positive control (d=3): G_AB with target NOT N_B = g N g^-1 != N, G_AC = CNOT, G_BC = (g(x)I) CNOT '
      '(g^-1(x)I): T3 holds, and G_BC meets Rc(N_B, N_C) with N_C = N (the lemma\'s conclusion)',
      rel_t(G_AB, n, NBc) and t3_holds(eAB, eBCc, eAC, sp.dim) and rel_c(G_BCc, n, NBc, N) and rel_t(G_BCc, n, N))
# Note: the complex CNOT meets Rc(N', N) for EVERY corner-swapping N' of split (1, 1) (a pi-rotation about any axis
# of the xy-plane), so a control-frame relabelling is invisible at d = 3; the negative control therefore uses a G_BC
# that meets F, P+- and Rt(N) but Rc with NO ball NOT: G_BC = CNOT (R (x) I), R a rational rotation of B's T.
R = frame_preserving(cayley([[Fr(0), Fr(1, 3)], [Fr(-1, 3), Fr(0)]]))
G_BCn = sp_compose(CN, embed_local(R, 0, sp2))
eBCn = embed_two(G_BCn, n, (1, 2), sp)
check('2.4 lemma control (d=3): the complex CNOT meets Rc(N_B, N) as well as Rc(N, N) (its control NOT is not '
      'unique), and with G_BC = CNOT T3 also holds', rel_c(CN, n, NBc, N) and rel_c(CN, n, N, N)
      and t3_holds(eAB, eBCp, eAC, sp.dim))
noRc = not any(rel_c(G_BCn, n, diag([1, s1, s2, -1]), N) for s1 in (1, -1) for s2 in (1, -1)) \
    and not rel_c(G_BCn, n, NBc, N)
check('2.4 lemma negative control (d=3): G_BC = CNOT (R (x) I) meets F, P+- (local automorphism after CNOT), Rt(N), and fails Rc(N\', N) '
      'for N\' in {coordinate NOTs, N_B}; T3 FAILS, as the lemma\'s contrapositive requires',
      frame_ok(G_BCn, n) and rel_t(G_BCn, n, N) and noRc and not rel_c(G_BCn, n, NBc, N)
      and not t3_holds(eAB, eBCn, eAC, sp.dim) and not t3_holds(embed_two(CN, n, (0, 1), sp), eBCn, eAC, sp.dim))

sp3all, g3all = gates3(MODELS[3]['G'], 4, ALL_PAIRS)
for d in (5, 7):
    M = MODELS[d]; n = M['n']; G = M['G']; Nc = M['NA']; Nt = M['NB']
    sp, g = gates3(G, n, ALL_PAIRS); sp2 = Space(n, 2)
    r2 = frame_ok(G, n) and rel_t(G, n, Nt) and rel_c(G, n, Nc, Nt)
    t1 = all(sp_eq(sp_compose(g[(X, Y)], g[(X, Z)]), sp_compose(g[(X, Z)], g[(X, Y)]), sp.dim)
             for X in range(3) for Y in range(3) for Z in range(3) if len({X, Y, Z}) == 3)
    t2 = all(sp_eq(sp_compose(g[(X, Z)], g[(Y, Z)]), sp_compose(g[(Y, Z)], g[(X, Z)]), sp.dim)
             for X in range(3) for Y in range(3) for Z in range(3) if len({X, Y, Z}) == 3)
    t3 = [t3_holds(g[(X, Y)], g[(Y, Z)], g[(X, Z)], sp.dim)
          for X in range(3) for Y in range(3) for Z in range(3) if len({X, Y, Z}) == 3]
    t3b = [sp_eq(sp_compose(g[(X, Y)], sp_compose(g[(Y, Z)], sp_compose(g[(X, Y)], g[(Y, Z)]))), g[(X, Z)], sp.dim)
           for X in range(3) for Y in range(3) for Z in range(3) if len({X, Y, Z}) == 3]
    check('2.4 d=%d Model II: the other ordering of the chain identity, G_AB G_BC G_AB G_BC = G_AC, also FAILS for all '
          'six labelings (it holds for the d = 3 complex CNOT)' % d,
          not any(t3b) and sp_eq(sp_compose(g3all[(0, 1)], sp_compose(g3all[(1, 2)], sp_compose(g3all[(0, 1)],
                                 g3all[(1, 2)]))), g3all[(0, 2)], sp3all.dim))
    check('2.4 d=%d Model II (N^c split %s, N^t split %s, the J/K gate on all six ordered pairs): R2 holds for every '
          'pair, T1 and T2 hold, T3 FAILS for all six labelings' % (d, split_of(Nc)[:2], split_of(Nt)[:2]),
          r2 and t1 and t2 and not any(t3))
    # corner sector of T3: with A in corner k_a the T3 defect is k_a (x) [G (m_a (x) I) G (m_a (x) I) - I (x) m_a]
    k = corners(n)
    INt = embed_local(Nt, 1, sp2); NtI = embed_local(Nt, 0, sp2)
    m = [eye(n), Nt]                                       # M_0 = I for the J/K map, so m_1 = N^t
    L = sp_compose(g[(1, 2)], sp_compose(g[(0, 1)], sp_compose(g[(1, 2)], g[(0, 1)])))
    sec_ok = True
    for a in (0, 1):
        ma = embed_local(m[a], 0, sp2)
        star = sp_sub(sp_compose(G, sp_compose(ma, sp_compose(G, ma))), embed_local(m[a], 1, sp2), sp2.dim)
        for jb in range(n):
            for jc in range(n):
                v = tensor_vec([k[a], eye(n)[jb], eye(n)[jc]], sp)
                lhs = sp_apply(L, v)
                rhs = sp_apply(g[(0, 2)], v)
                diff = {i: lhs.get(i, 0) - rhs.get(i, 0) for i in set(lhs) | set(rhs)}
                diff = {i: x for i, x in diff.items() if x != 0}
                want = {}
                for i2, x in star[jb * n + jc].items():
                    for ia in range(n):
                        if k[a][ia] != 0:
                            want[sp.idx([ia, i2 // n, i2 % n])] = k[a][ia] * x
                sec_ok &= diff == want
    D2 = sp_sub(sp_compose(NtI, sp_compose(G, NtI)), sp_compose(INt, G), sp2.dim)          # Rc(N^t, N^t) defect
    D1 = sp_sub(sp_compose(G, sp_compose(NtI, sp_compose(G, NtI))), INt, sp2.dim)           # (*1) defect
    check('2.4 d=%d: on the corner sector A = k_a the T3 defect equals k_a (x) [G(m_a (x) I)G(m_a (x) I) - I (x) m_a] '
          'exactly; (*0) holds (G^2 = I) and the (*1) defect D1 equals G D2 with D2 the defect of Rc(N^t, N^t), '
          'which is nonzero' % d,
          sec_ok and sp_eq(D1, sp_compose(G, D2), sp2.dim) and not sp_is_zero(D2)
          and sp_eq(sp_compose(G, G), sp_identity(sp2.dim), sp2.dim))

# T4 for the two-copy composite G_BA G_AB of the J/K Model II gate (the exchange below is bookkeeping of which factor
# is which, not an operation): exact rational witness
for d, (s_, t_, f_, g_) in ((5, ((2, -1), (3, -1), (2, -1), (4, 1))), (7, (None, None, None, None))):
    M = MODELS[d]; n = M['n']; G = M['G']; sp2 = Space(n, 2)
    S = {j: {sp2.idx(sp2.digits(j)[::-1]): Fr(1)} for j in range(sp2.dim)}
    W = sp_compose(sp_compose(S, sp_compose(G, S)), G)

    def ax(i, sg):
        v = [Fr(0)] * n; v[0] = Fr(1); v[i] = Fr(sg); return v
    if s_ is None:
        best = None
        for (i1, s1), (i2, s2), (i3, s3), (i4, s4) in product([(i, sg) for i in range(1, n) for sg in (1, -1)], repeat=4):
            v = value(W, [ax(i1, s1), ax(i2, s2)], [ax(i3, s3), ax(i4, s4)], sp2)
            if best is None or v < best[0]:
                best = (v, (i1, s1), (i2, s2), (i3, s3), (i4, s4))
        val = best[0]; s_, t_, f_, g_ = best[1:]
    else:
        val = value(W, [ax(*s_), ax(*t_)], [ax(*f_), ax(*g_)], sp2)
    check('2.4 d=%d Model II J/K gate: the two-copy composite G_BA G_AB sends the pure product state '
          '(u %+d e%d) (x) (u %+d e%d) outside the maximal tensor cone: product effect (u %+d e%d) (x) (u %+d e%d) has '
          'value %s' % (d, s_[1], s_[0], t_[1], t_[0], f_[1], f_[0], g_[1], g_[0], val), val < 0)

print('part2: OK -- %d checks' % len(OUT))
