"""b17_tower.py — research/bridge, round 4, node B17: HO-24's explicit cone along B10-5's tower G_n.

S0 (written 2026-10-11T05:39:54Z, NOTES-B17, before this script's first run). Decision rules fixed there: n passes
iff G_n lies in G384 modulo phases (invariance by construction); n fails iff an exact certificate exists: a defect
d_j = I - c P_{h_j} of the orbit and a projector P_{h'} (h' = V h_j, V a generator of G_n) with |<h_k|h'>|^2 <= 1/c for
every orbit ray h_k (so P_{h'} lies in the dual of K = (Q3 cap Z*) + cone Z) and <P_{h'}, V d_j V*> = 1 - c < 0.
Controls: K1 (order 384, orbit 192), K2 (no certificate at n = 2), K3 (no certificate for V = 1).
Exact: Gaussian rationals; the eighth root of unity only through p + q*sqrt(2) compared by integer arithmetic.
Run from experiments/:  python3 -I -B b17_tower.py > b17_tower.out 2> b17_tower.err
"""
from fractions import Fraction as Fr

Z = (Fr(0), Fr(0))
ONE = (Fr(1), Fr(0))
I = (Fr(0), Fr(1))
C_STAR = Fr(401, 400)


def cadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


def cinv(a):
    d = a[0] * a[0] + a[1] * a[1]
    return (a[0] / d, -a[1] / d)


def cabs2(a):
    return a[0] * a[0] + a[1] * a[1]


def mmul(A, B):
    return [[sum_c([cmul(A[i][k], B[k][j]) for k in range(4)]) for j in range(4)] for i in range(4)]


def mvec(A, v):
    return [sum_c([cmul(A[i][k], v[k]) for k in range(4)]) for i in range(4)]


def sum_c(xs):
    s = Z
    for x in xs:
        s = cadd(s, x)
    return s


def canon_mat(A):  # canonical representative modulo the phases {1, i, -1, -i}
    first = next(x for row in A for x in row if x != Z)
    for mu in (ONE, I, (Fr(-1), Fr(0)), (Fr(0), Fr(-1))):
        y = cmul(mu, first)
        if y[0] > 0 and y[1] >= 0:
            return tuple(tuple(cmul(mu, x) for x in row) for row in A)
    raise ValueError


def canon_ray(v):  # canonical representative of the ray: divide by the first nonzero coordinate
    f = next(x for x in v if x != Z)
    fi = cinv(f)
    return tuple(cmul(x, fi) for x in v)


def block(U):  # I (x) U, index 2a + b, b the target
    M = [[Z] * 4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            for b2 in range(2):
                M[2 * a + b][2 * a + b2] = U[b][b2]
    return M


h = Fr(1, 2)
UJ = [[(h, -h), (-h, -h)], [(h, -h), (h, h)]]
S1 = [[ONE, Z], [Z, I]]
Z1 = [[ONE, Z], [Z, (Fr(-1), Fr(0))]]
X1 = [[Z, ONE], [ONE, Z]]
CNOT = [[ONE if j == p else Z for j in range(4)] for p in (0, 1, 3, 2)]
GENS384 = [CNOT, block(S1), block(UJ)]
HSTAR = [(Fr(10), Fr(0)), (Fr(2), Fr(-2)), (Fr(-1), Fr(-3)), (Fr(3), Fr(-1))]


def le_p_q_sqrt2(p, q, r):  # decide p + q*sqrt(2) <= r exactly
    f = r - p
    if q <= 0:
        return f >= 0 or 2 * q * q >= f * f
    return f >= 0 and 2 * q * q <= f * f


def main():
    checks = []
    # G384 modulo phases
    seen = {canon_mat(g): g for g in GENS384}
    fr = list(GENS384)
    while fr:
        nx = []
        for A in fr:
            for g in GENS384:
                B = mmul(A, g)
                k = canon_mat(B)
                if k not in seen:
                    seen[k] = B
                    nx.append(B)
        fr = nx
    grp = list(seen.values())
    print('G384 modulo phases: order', len(grp))
    orbit = {}
    for g in grp:
        v = mvec(g, HSTAR)
        orbit.setdefault(canon_ray(v), v)
    rays = list(orbit.values())
    print('orbit of h*: rays', len(rays))
    checks.append(('K1 order 384 modulo phases and an orbit of 192 rays (HO-24 items 1, 4, re-derived)',
                   len(grp) == 384 and len(rays) == 192))
    # pairwise overlaps (HO-24 item 4's window, for the record)
    n2 = [sum(cabs2(x) for x in v) for v in rays]
    ov = []
    for i in range(len(rays)):
        for j in range(i + 1, len(rays)):
            ip = sum_c([cmul(cconj(rays[i][k]), rays[j][k]) for k in range(4)])
            ov.append(cabs2(ip) / (n2[i] * n2[j]))
    print('pairwise squared overlaps: pairs', len(ov), 'min', min(ov), 'max', max(ov))
    checks.append(('K1b pairwise squared overlaps in [25/2048, 13/16] over 18336 pairs (HO-24 item 4)',
                   len(ov) == 18336 and min(ov) >= Fr(25, 2048) and max(ov) <= Fr(13, 16)))
    # stages n = 1, 2: membership modulo phases
    for nm, U in (('1 (x) Z', block(Z1)), ('1 (x) S', block(S1)), ('1 (x) X', block(X1)), ('CNOT', CNOT)):
        print('member of G384 modulo phases:', nm, canon_mat(U) in seen)
    mem12 = all(canon_mat(U) in seen for U in (block(Z1), block(S1), block(X1), CNOT))
    checks.append(('S0-2 G_1 and G_2 generators (CNOT, 1(x)Z, 1(x)S, 1(x)X) lie in G384 modulo phases', mem12))

    # the certificate search for a target phase diag(1, omega) with omega = e^{i pi/4}, or a rational phase
    def overlap_parts(hk, hj, kind):
        # <h_k | V h_j> with V = 1 (x) diag(1, w); split by the target index
        A = cadd(cmul(cconj(hk[0]), hj[0]), cmul(cconj(hk[2]), hj[2]))
        B = cadd(cmul(cconj(hk[1]), hj[1]), cmul(cconj(hk[3]), hj[3]))
        if kind == 'T':          # w = (1 + i)/sqrt 2: |A + wB|^2 = |A|^2 + |B|^2 + sqrt2 * Re(conj(A) B (1 + i))
            t = cmul(cmul(cconj(A), B), (Fr(1), Fr(1)))
            return cabs2(A) + cabs2(B), t[0]
        w = {'S': I, 'one': ONE}[kind]
        return cabs2(cadd(A, cmul(w, B))), Fr(0)

    def certificates(kind):
        found = []
        for j, hj in enumerate(rays):
            ok = True
            for k, hk in enumerate(rays):
                p, q = overlap_parts(hk, hj, kind)
                nrm = n2[k] * n2[j]
                # overlap = (p + q sqrt2)/nrm <= 1/c*  <=>  p + q sqrt2 <= nrm / c*
                if not le_p_q_sqrt2(p, q, nrm / C_STAR):
                    ok = False
                    break
            if ok:
                found.append(j)
        return found

    cert_T = certificates('T')
    cert_S = certificates('S')
    cert_1 = certificates('one')
    print('certificates at n = 3 (V = 1 (x) diag(1, e^{i pi/4})): defects certified', len(cert_T), 'of', len(rays))
    print('certificates at n = 2 (V = 1 (x) S):', len(cert_S), '; for V = 1:', len(cert_1))
    if cert_T:
        j = cert_T[0]
        print('first certified defect: orbit ray', [tuple(map(str, x)) for x in rays[j]])
        print('pairing <P_{h\'}, V d_j V*> = 1 - c* =', 1 - C_STAR)
    # the stage n = 3 generator is not a phase multiple of a Gaussian-rational matrix: the ratio of two of its
    # nonzero entries is (1 + i)/sqrt(2), whose square i is in Q(i) while it is not (|.| = 1, argument pi/4)
    checks.append(('S0-3 an exact certificate exists at n = 3 for V = 1 (x) diag(1, e^{i pi/4})', len(cert_T) > 0))
    checks.append(('K2 positive control: no certificate at n = 2', len(cert_S) == 0))
    checks.append(('K3 countercontrol: no certificate for V = 1', len(cert_1) == 0))
    print('\nCHECKS')
    for nm, ok in checks:
        print(('PASS ' if ok else 'FAIL ') + nm)
    if all(ok for _, ok in checks):
        print('VERDICT B17-TOWER: K is invariant under G_1 and G_2; the first failing stage is n = 3 '
              '(%d of %d defects certified out of K under 1 (x) diag(1, e^{i pi/4})); every n >= 3 fails'
              % (len(cert_T), len(rays)))
    else:
        print('VERDICT VOID: a check failed')


main()
