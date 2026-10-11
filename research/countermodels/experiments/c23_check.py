"""C23 — independent checker of the certificate `c23_certificate.json` (reads nothing else).

Node C23 (round 5, research/countermodels); decision rule in NOTES-C23 S0 (fixed 2026-10-11T10:32Z, before the first run
of either script): CHECK C23-CERTIFICATE-OK iff every item below passes.

Method (different from the construction `c23_torus.py`): its own exact complex arithmetic on pairs of Fractions; its own
characterization of the group G_T (modulo phase): a listed 4x4 matrix is accepted iff it is unitary, monomial with
permutation in V4 = {e, (23), (01)(23), (01)} and its phases phi_i = g[i][sigma^-1(i)] satisfy phi0*phi1 = phi2*phi3
(the condition for diag(phi) to lie in U(1)*T^2, T^2 = {diag(1, uv, u, v)}); no (u, v) parametrization is read. Every
inner product, defect, witness, pairing, principal minor, rank, nullspace and quadratic-form value is recomputed from
the listed vectors and matrices. The identities of Lemma C23-1 and the determinant identity are checked by expanding
polynomials in real coordinates (sympy expand of real and imaginary parts), with the modulus identity in the form
|beta + u alpha|^2 - |conj(alpha) + u conj(beta)|^2 = (|u|^2 - 1)(|alpha|^2 - |beta|^2).
Items: K1 group membership; K2 C23-1 instances and classes; K3 identities; K4 C23-2 (a); K5 C23-2 (b) (the transported
K_T pair, the circle map, the circle defects); K6 C23-2 (c) (mixture); K7 C23-3 (a); K8 C23-3 (b); K9 C23-3 (c).
Run from experiments/:  python3 -I -B c23_check.py > c23_check.out 2> c23_check.err
"""
from fractions import Fraction as Fr
import itertools
import json
import sympy as sp

with open("c23_certificate.json") as fh:
    C = json.load(fh)


def num(s):
    return Fr(s)


def cx(p):
    return (num(p[0]), num(p[1]))


def cv(lst):
    return [cx(p) for p in lst]


def cm(rows):
    return [[cx(p) for p in r] for r in rows]


Z0 = (Fr(0), Fr(0))
ONE = (Fr(1), Fr(0))


def ad(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sb(a, b):
    return (a[0] - b[0], a[1] - b[1])


def ml(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cj(a):
    return (a[0], -a[1])


def a2(a):
    return a[0] * a[0] + a[1] * a[1]


def dv(a, b):
    d = a2(b)
    q = ml(a, cj(b))
    return (q[0] / d, q[1] / d)


def rs(r):
    return (Fr(r), Fr(0))


def isz(a):
    return a[0] == 0 and a[1] == 0


def inner(x, y):
    s = Z0
    for p, q in zip(x, y):
        s = ad(s, ml(cj(p), q))
    return s


def nrm2(x):
    return inner(x, x)[0]


def mat_vec(M, x):
    out = []
    for i in range(len(M)):
        s = Z0
        for j in range(len(x)):
            s = ad(s, ml(M[i][j], x[j]))
        out.append(s)
    return out


def mat_mat(A, B):
    n = len(A)
    return [[_sum([ml(A[i][k], B[k][j]) for k in range(n)]) for j in range(n)] for i in range(n)]


def _sum(xs):
    s = Z0
    for x in xs:
        s = ad(s, x)
    return s


def dagger(A):
    n = len(A)
    return [[cj(A[j][i]) for j in range(n)] for i in range(n)]


def ident():
    return [[ONE if i == j else Z0 for j in range(4)] for i in range(4)]


def mat_sub(A, B):
    return [[sb(A[i][j], B[i][j]) for j in range(4)] for i in range(4)]


def mat_add(A, B):
    return [[ad(A[i][j], B[i][j]) for j in range(4)] for i in range(4)]


def mat_scale(s, A):
    return [[ml(s, A[i][j]) for j in range(4)] for i in range(4)]


def rank1(x):
    n = nrm2(x)
    return [[ml(rs(Fr(1) / n), ml(x[i], cj(x[j]))) for j in range(4)] for i in range(4)]


def dfct(c, x):
    return mat_sub(ident(), mat_scale(rs(c), rank1(x)))


def pair(A, B):
    return _sum([ml(A[i][k], B[k][i]) for i in range(4) for k in range(4)])[0]


def quad(M, x):
    return inner(x, mat_vec(M, x))[0]


def mat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(4) for j in range(4))


def parallel(x, y):
    return all(isz(sb(ml(x[i], y[j]), ml(x[j], y[i]))) for i in range(4) for j in range(4))


def detpsi(x):
    return sb(ml(x[0], x[3]), ml(x[1], x[2]))


GE = {name: cm(M) for name, M in C["group_elements"].items()}
V4P = {(0, 1, 2, 3), (0, 1, 3, 2), (1, 0, 3, 2), (1, 0, 2, 3)}


def in_GT(g):
    """unitary, monomial with permutation in V4, phases with phi0 phi1 = phi2 phi3"""
    if not mat_eq(mat_mat(g, dagger(g)), ident()):
        return False
    sigma = []
    for j in range(4):
        nz = [i for i in range(4) if not isz(g[i][j])]
        if len(nz) != 1:
            return False
        sigma.append(nz[0])
    if tuple(sigma) not in V4P:
        return False
    inv = {sigma[j]: j for j in range(4)}
    phi = [g[i][inv[i]] for i in range(4)]
    return ml(phi[0], phi[1]) == ml(phi[2], phi[3])


def is_torus(g):
    return in_GT(g) and all(isz(g[i][j]) for i in range(4) for j in range(4) if i != j)


results = []


def report(name, ok, detail):
    results.append(ok)
    print(f"{name}  {'PASS' if ok else 'FAIL'}  {detail}")


# K1
bad = [n for n, g in GE.items() if not in_GT(g)]
report("K1", len(bad) == 0, f"{len(GE)} listed group elements; rejected: {bad[:5]}")

# K2
cls_seen = set()
ok2 = True
for it in C["C23-1"]["instances"]:
    h = cv(it["h"])
    g = GE[it["g"]]
    gh = mat_vec(g, h)
    al, be = ml(cj(h[2]), h[3]), ml(cj(h[0]), h[1])
    if isz(al) and isz(be):
        cls = "v"
    elif isz(al):
        cls = "iii"
    elif isz(be):
        cls = "iv"
    elif a2(al) == a2(be):
        cls = "ii"
    else:
        cls = "i"
    ok2 = ok2 and cls == it["class"] and isz(inner(h, gh)) and not parallel(h, gh)
    cls_seen.add(cls)
report("K2", ok2 and cls_seen == {"i", "ii", "iii", "iv", "v"},
       f"every instance: class recomputed from (alpha, beta), g in G_T, <h|gh> = 0, gh not parallel to h; classes {sorted(cls_seen)}")

# K3 identities in real coordinates
re_ = sp.symbols("p0:4", real=True)
im_ = sp.symbols("q0:4", real=True)
u1, u2, v1, v2 = sp.symbols("u1 u2 v1 v2", real=True)
H = [re_[k] + sp.I * im_[k] for k in range(4)]
U, V = u1 + sp.I * u2, v1 + sp.I * v2
DXh = [H[1], U * V * H[0], U * H[3], V * H[2]]
lhs = sum(sp.conjugate(H[k]) * DXh[k] for k in range(4))
AL, BE = sp.conjugate(H[2]) * H[3], sp.conjugate(H[0]) * H[1]
rhs = BE + U * V * sp.conjugate(BE) + U * AL + V * sp.conjugate(AL)
e1 = sp.expand(lhs - rhs)
k1 = sp.expand(sp.re(e1)) == 0 and sp.expand(sp.im(e1)) == 0
mod = sp.expand((BE + U * AL) * sp.conjugate(BE + U * AL) - (sp.conjugate(AL) + U * sp.conjugate(BE)) *
                sp.conjugate(sp.conjugate(AL) + U * sp.conjugate(BE))
                - (U * sp.conjugate(U) - 1) * (AL * sp.conjugate(AL) - BE * sp.conjugate(BE)))
k2 = sp.expand(sp.re(mod)) == 0 and sp.expand(sp.im(mod)) == 0
Dh = [H[0], U * V * H[1], U * H[2], V * H[3]]
e3 = sp.expand(Dh[0] * Dh[3] - Dh[1] * Dh[2] - V * (H[0] * H[3] - U ** 2 * H[1] * H[2]))
k3 = sp.expand(sp.re(e3)) == 0 and sp.expand(sp.im(e3)) == 0
report("K3", k1 and k2 and k3, f"<h|D(u,v)X_B h> identity: {k1}; |beta+u alpha|^2 - |conj alpha + u conj beta|^2 = "
       f"(|u|^2-1)(|alpha|^2-|beta|^2): {k2}; det Psi(D(u,v)h) = v(h0h3 - u^2 h1h2): {k3} (real coordinates)")

# K4 C23-2 (a)
A = C["C23-2a"]
hs_, cs_ = cv(A["seed_star"]), num(A["c_star"])
h2_, c2_ = cv(A["seed_two"]), num(A["c_two"])
lam = num(A["lambda"])
ok4 = lam == (cs_ - 1) / (4 - 2 * cs_)
gp = GE[A["g_pair"]]
hp = mat_vec(gp, hs_)
ok4 = ok4 and isz(inner(hs_, hp))
y = mat_add(rank1(hs_), mat_scale(rs(lam), dfct(cs_, hp)))
dh = dfct(cs_, hs_)
ok4 = ok4 and pair(y, dh) == 0 and quad(y, hp) < 0
minp, cnt = None, 0
h1_all = True
for smp in A["samples"]:
    g = GE[smp["g"]]
    seed, c = (hs_, cs_) if smp["seed"] == "star" else (h2_, c2_)
    hl = mat_vec(g, seed)
    dl = dfct(c, hl)
    p = pair(y, dl)
    ok4 = ok4 and p >= 0 and pair(dl, dh) > 0
    D = a2(detpsi(hl)) / nrm2(hl) ** 2
    h1_all = h1_all and (1 - 4 * D) <= (Fr(2) / c - 1) ** 2
    minp = p if minp is None else min(minp, p)
    cnt += 1
lam2 = num(A["countercontrol"]["lambda_small"])
ok_cc = lam2 == (c2_ - 1) / (4 - 2 * c2_)
y2 = mat_add(rank1(hs_), mat_scale(rs(lam2), dfct(c2_, hp)))
cc = pair(y2, dh)
report("K4", ok4 and h1_all and ok_cc and cc < 0 and cnt == 200,
       f"lambda = (c*-1)/(4-2c*); <y,d_h> = 0; (gh)^+y(gh) = {quad(y, hp)} < 0; {cnt} samples: <y,d> >= 0 (min {minp}), "
       f"<d,d_h> > 0, H1 at each: {h1_all}; countercontrol <y_small, d_h> = {cc} < 0")

# K5 C23-2 (b)
B = C["C23-2b"]


def l1p(u, L):
    M = [[Z0] * 4 for _ in range(4)]
    M[0][3], M[3][0], M[1][1], M[2][2] = sb(Z0, u), sb(Z0, cj(u)), rs(L), rs(L)
    return M


def l2p(u, L):
    M = [[Z0] * 4 for _ in range(4)]
    M[1][2], M[2][1], M[0][0], M[3][3] = sb(Z0, u), sb(Z0, cj(u)), rs(L), rs(L)
    return M


def det_exact(M):
    n = len(M)
    M = [r[:] for r in M]
    d = ONE
    for col in range(n):
        piv = next((i for i in range(col, n) if not isz(M[i][col])), None)
        if piv is None:
            return Z0
        if piv != col:
            M[col], M[piv] = M[piv], M[col]
            d = sb(Z0, d)
        d = ml(d, M[col][col])
        for i in range(col + 1, n):
            f = dv(M[i][col], M[col][col])
            M[i] = [sb(M[i][j], ml(f, M[col][j])) for j in range(n)]
    return d


def psd_minors(M):
    for r in range(1, 5):
        for S in itertools.combinations(range(4), r):
            d = det_exact([[M[i][j] for j in S] for i in S])
            if d[1] != 0 or d[0] < 0:
                return False
    return True


def inL1d(Y):
    s = Y[1][1][0] + Y[2][2][0]
    return s >= 0 and 4 * a2(Y[0][3]) <= s * s


def inL2d(Y):
    s = Y[0][0][0] + Y[3][3][0]
    return s >= 0 and 4 * a2(Y[1][2]) <= s * s


yP, q0, u0, L0 = cm(B["y"]), cm(B["q0"]), cx(B["u0"]), num(B["L0"])
wP, vP, zeta, tau = cm(B["w"]), cv(B["v"]), cx(B["zeta"]), num(B["tau"])
hermitian = lambda M: mat_eq(M, dagger(M))
ok5 = hermitian(yP) and hermitian(wP) and mat_eq(mat_sub(yP, q0), l1p(u0, L0)) and psd_minors(q0) and a2(u0) <= L0 * L0
vvd = [[ml(vP[i], cj(vP[j])) for j in range(4)] for i in range(4)]
ok5 = ok5 and mat_eq(mat_sub(wP, vvd), l1p(zeta, tau)) and a2(zeta) <= tau * tau
ok5 = ok5 and inL1d(yP) and inL2d(yP) and inL1d(wP) and inL2d(wP)
tv = pair(yP, wP)
ok5 = ok5 and tv < 0 and str(tv) == B["value_tr_yw"]
IH = cm(B["IH_unnormalized"])
okm = True
okd = True
for p in B["circle_points"]:
    w_ = cx(p)
    c1 = [ONE, ONE, w_, sb(Z0, w_)]          # |0+> + w|1-> up to normalization
    c2 = [ONE, sb(Z0, ONE), w_, w_]          # |0-> + w|1+> up to normalization
    okm = okm and parallel(mat_vec(IH, c1), [ONE, Z0, Z0, w_]) and parallel(mat_vec(IH, c2), [Z0, ONE, w_, Z0])
    okd = okd and mat_eq(dfct(Fr(2), [ONE, Z0, Z0, w_]), l1p(cj(w_), 1)) and mat_eq(dfct(Fr(2), [Z0, ONE, w_, Z0]), l2p(cj(w_), 1))
okH = all(IH[2 * a + b][2 * a + b2] == ([[ONE, ONE], [ONE, sb(Z0, ONE)]][b][b2]) for a in range(2) for b in range(2) for b2 in range(2))
report("K5", ok5 and okm and okd and okH,
       f"y' = q0' + l1'(u0, L0), q0' PSD (all 15 principal minors), |u0| <= L0; w' = v'v'^+ + l1'(zeta, tau), |zeta| <= tau; "
       f"y', w' in L1'* n L2'*; tr(y'w') = {tv} < 0: {ok5}; IH = 1 (x) [[1,1],[1,-1]] maps the S2 circles onto C1', C2': "
       f"{okm and okH}; circle defects are l1'(conj w,1), l2'(conj w,1): {okd}")

# K6 C23-2 (c)
M6 = C["C23-2c"]
hm, cmx, lm = cv(M6["h"]), num(M6["c"]), num(M6["lambda"])
gm = GE[M6["g_pair"]]
hpm = mat_vec(gm, hm)
ym = mat_add(rank1(hm), mat_scale(rs(lm), dfct(cmx, hpm)))
dhm = dfct(cmx, hm)
ok6 = lm == (cmx - 1) / (4 - 2 * cmx) and isz(inner(hm, hpm)) and pair(ym, dhm) == 0 and quad(ym, hpm) < 0
for bb in M6["bell_samples"]:
    b_ = cv(bb)
    maxent = 4 * a2(detpsi(b_)) == nrm2(b_) ** 2
    db = dfct(Fr(2), b_)
    ok6 = ok6 and maxent and pair(ym, db) >= 0 and pair(db, dhm) > 0
for gname in M6["orbit_samples"]:
    dl = dfct(cmx, mat_vec(GE[gname], hm))
    ok6 = ok6 and pair(ym, dl) >= 0 and pair(dl, dhm) > 0


def isqrt_frac(q):
    n, d = q.numerator, q.denominator
    rn, rd = sp.integer_nthroot(n, 2), sp.integer_nthroot(d, 2)
    assert rn[1] and rd[1]
    return Fr(int(rn[0]), int(rd[0]))


mods = [isqrt_frac(a2(x)) for x in hm]
overlap = max((mods[0] + mods[3]) ** 2, (mods[1] + mods[2]) ** 2) <= nrm2(hm)
Dmin = min((mods[0] * mods[3] - mods[1] * mods[2]) ** 2, (mods[0] * mods[2] - mods[1] * mods[3]) ** 2) / nrm2(hm) ** 2
h1m = Dmin > 0 and (1 - 4 * Dmin) <= (Fr(2) / cmx - 1) ** 2 and str(Dmin) == M6["Dmin"]
report("K6", ok6 and overlap and h1m,
       f"mixture: lambda, <h|gh> = 0, <y,d_h> = 0, (gh)^+y(gh) < 0; {len(M6['bell_samples'])} Bell samples maximally entangled "
       f"with <y,d_b> >= 0 and <d_b,d_h> > 0; {len(M6['orbit_samples'])} orbit samples >= 0: {ok6}; overlap condition: {overlap}; "
       f"D_min = {Dmin} > 0 with H1 at c: {h1m}")


# K7 C23-3 (a)
def rank_of(vecs):
    M = [list(v) for v in vecs]
    rk = 0
    ncol = len(M[0])
    for col in range(ncol):
        piv = next((i for i in range(rk, len(M)) if not isz(M[i][col])), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and not isz(M[i][col]):
                f = dv(M[i][col], M[rk][col])
                M[i] = [sb(M[i][j], ml(f, M[rk][j])) for j in range(ncol)]
        rk += 1
    return rk


def null_dim_and_span(rows, cand):
    """dimension of {k : rows k = 0} (= 4 - rank) and whether cand lies in it"""
    d = 4 - rank_of(rows)
    inside = all(isz(_sum([ml(r[j], cand[j]) for j in range(4)])) for r in rows) if cand is not None else None
    return d, inside


A7 = C["C23-3a"]
ha = cv(A7["h"])
P7 = [mat_vec(GE[n], ha) for n in A7["partners_g"]]
ok7 = all(isz(inner(ha, p)) for p in P7) and rank_of(P7) == 3
rows7 = [[cj(x) for x in p] for p in P7]
d7, inside7 = null_dim_and_span(rows7, ha)
d7b, _ = null_dim_and_span(rows7 + [[cj(x) for x in ha]], None)
gb = GE[A7["countercontrol_g"]]
bimg = mat_vec(gb, ha)
cc7 = not isz(inner(ha, bimg)) and rank_of(P7[:3] + [bimg]) == 4
report("K7", ok7 and d7 == 1 and inside7 and d7b == 0 and cc7,
       f"partners orthogonal to h, rank {rank_of(P7)}; {{k perp partners}} has dimension {d7} and contains h: {inside7}; with "
       f"k perp h: dimension {d7b}; countercontrol (non-orthogonalizing image) rank {rank_of(P7[:3] + [bimg])}")

# K8 C23-3 (b)
ok8 = True
det8 = []
for ent in C["C23-3b"]:
    h, k0 = cv(ent["h"]), cv(ent["k0"])
    Ps = [GE[n] for n in ent["partners_g"]]
    imgs = [mat_vec(g, h) for g in Ps]
    okc = isz(inner(h, k0)) and all(isz(inner(h, p)) for p in imgs) and rank_of(imgs) == 2
    rows = [[cj(x) for x in p] for p in imgs] + [[cj(x) for x in h]]
    dd, inside = null_dim_and_span(rows, k0)
    okc = okc and dd == 1 and inside
    c0 = num(ent["zero_pairing_c"])
    d0 = mat_sub(mat_sub(ident(), mat_scale(rs(c0), rank1(h))), mat_scale(rs(2 - c0), rank1(k0)))
    okc = okc and all(pair(d0, mat_mat(mat_mat(g, d0), dagger(g))) == 0 for g in Ps)
    p = [ml(cj(h[i]), k0[i]) for i in range(4)]
    okc = okc and not isz(ad(p[1], p[2]))
    for t in ent["tight"]:
        c = num(t["c"])
        Um = GE[t["U"]]
        b = cx(t["b"])
        d = mat_sub(mat_sub(ident(), mat_scale(rs(c), rank1(h))), mat_scale(rs(2 - c), rank1(k0)))
        uc = [ad(h[i], ml(b, k0[i])) for i in range(4)]
        coef = dv(inner(uc, k0), rs(nrm2(uc)))
        x = [sb(k0[i], ml(coef, uc[i])) for i in range(4)]
        dU = mat_mat(mat_mat(Um, d), dagger(Um))
        okt = is_torus(Um) and uc == cv(t["u_cap"]) and x == cv(t["x"]) and isz(inner(uc, x))
        okt = okt and quad(d, uc) < 0 and quad(d, x) > 0 and pair(d, dU) > 0 and quad(dU, x) < 0
        okc = okc and okt
        det8.append(f"{ent['class']} c={c}: x'(UdU+)x/|x|^2 = {float(quad(dU, x) / nrm2(x)):.6f}")
    ok8 = ok8 and okc
report("K8", ok8, f"r = 2 classes: partners orthogonal to h, rank 2, k0 spans the solutions of k perp (partners, h), zero "
       f"pairing on every partner, p1 + p2 != 0, tightness instances (U a torus element, u in the cap, x perp u, x'dx > 0, "
       f"<d,UdU+> > 0, x'(UdU+)x < 0): {'; '.join(det8)}")

# K9 C23-3 (c)
A9 = C["C23-3c"]
g9 = GE[A9["g"]]
ok9 = in_GT(g9)
for s_ in A9["seeds"]:
    h = cv(s_)
    ok9 = ok9 and not isz(detpsi(h)) and isz(detpsi(mat_vec(g9, h)))
report("K9", ok9, f"two-vanishing-coordinate entangled seeds have a product in their orbit (g in G_T): {ok9}")

n_ok = sum(results)
print(f"CHECKS {n_ok}/{len(results)}")
print("CHECK C23-CERTIFICATE-OK" if n_ok == len(results) else "CHECK C23-CERTIFICATE-FAIL")
