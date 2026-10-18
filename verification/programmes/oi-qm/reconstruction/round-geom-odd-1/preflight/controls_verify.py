"""GEOM-ODD-1 controls preflight: the exact verifier.

Standard library only; every quantity is a `fractions.Fraction`. It imports nothing from the generator and reads a
candidate only as data. For a control body it rebuilds, from the definitions and the kernel source, the body's corner
`z`, its NOT `N`, the generation pool `A` and the disjoint holdout pool `B`, and checks a candidate gate `G` (a rational
matrix on the joint carrier `W D`, tables indexed `mu * (D + 1) + nu`, control `mu`, target `nu`):

  VS  every pooled state lies in the body (exact membership);
  VE  every pooled effect is an effect on the whole body (exact certificate, below);
  VL  the frame on the four corner products, relT and relC as matrix identities (equivalently on every basis table);
  VI  an exact inverse, with G Ginv = 1;
  VP  posFwd and posInv: (e (x) f)(G (hom x (x) hom y)) >= 0 and the same for Ginv, for every pair of pooled states
      and every pair of pooled effects, pools A and B together (pool-relative positivity, not positivity on the body).

PASS for a control iff VS, VE, VL, VI and VP hold. Whether the candidate equals the reference gate exactly is recorded
and decides nothing.

Bodies.
  eball3  the unit ball of R^3, z = z3 = e_3, N = nflip, both parsed from CompositeDimension.lean; the reference gate is
          the kernel's cnot (pc, pt, sgn parsed).  States: rational unit vectors (pure states).  Effects (1 + u.x)/2.
          Certificate: (e0, e) is an effect on the ball iff 0 <= e0 - |e| and e0 + |e| <= 1, checked as e0 >= 0,
          e0 <= 1, |e|^2 <= e0^2 and |e|^2 <= (1 - e0)^2.
  omegah  E16b's hybrid body in R^7, chart (w, a, b): t0 = (1 + w)/2, t1 = (1 - w)/2, r0 = (a + b)/2, r1 = (a - b)/2,
          Omega_h = {t0, t1 >= 0, |r0| <= t0, |r1| <= t1}; z = (0, e_3, 0); N = 1 (+) nflip (+) nflip; the reference
          gate (Phi (x) Phi)(cnot on every sector block)(Phi (x) Phi)^-1.  Omega_h is the convex hull of the two sector
          balls {t_i = 1, |r_i| <= 1}, so an affine functional alpha0 t0 + beta0.r0 + alpha1 t1 + beta1.r1 is an effect
          on Omega_h iff (alpha_i, beta_i) is an effect on the unit ball for i = 0, 1 (the certificate checked).  States:
          the pure sector states (w, a, b) = (1, u, u) and (-1, u, -u), u a rational unit vector.
"""
import json
import os
import random
import re
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..', '..'))
KERNEL_CD = os.path.join(ROOT, 'verification', 'lean-mathlib', 'OIBridge', 'CompositeDimension.lean')

SEEDS = {'A': 20261018, 'B': 20261019}
POOL_SIZE = {'eball3': 24, 'omegah': 6}            # unit vectors drawn per pool
PYTHAG = [(1, 0, 0), (3, 4, 0), (1, 2, 2), (2, 3, 6), (2, 6, 9), (1, 4, 8), (4, 4, 7), (1, 12, 12)]


# ------------------------------------------------------------------ the kernel's data, parsed
def kernel_data():
    src = open(KERNEL_CD, encoding='utf-8').read()

    def table(name):
        m = re.search(r'def %s : Fin 4 → Fin 4 → Fin 4\n((?:  \|.*\n)+)' % name, src)
        t = {(int(a), int(b)): int(c) for a, b, c in re.findall(r'(\d), (\d) => (\d)', m.group(1))}
        assert len(t) == 16, name
        return t
    ms = re.search(r'def sgn \(μ ν : Fin 4\) : ℝ := if \(μ = (\d) ∧ ν = (\d)\) ∨ \(μ = (\d) ∧ ν = (\d)\) then -1 else 1',
                   src)
    neg = {(int(ms.group(1)), int(ms.group(2))), (int(ms.group(3)), int(ms.group(4)))}
    sgn = {(a, b): (-1 if (a, b) in neg else 1) for a in range(4) for b in range(4)}
    mn = re.search(r'def nflip : \(Fin 3 → ℝ\) →ₗ\[ℝ\] \(Fin 3 → ℝ\) where\n  toFun x := fun i => '
                   r'\(!\[(-?1), (-?1), (-?1)\] : Fin 3 → ℝ\) i \* x i', src)
    nflip = [int(mn.group(k)) for k in (1, 2, 3)]
    mz = re.search(r'def z3 : Fin 3 → ℝ := !\[(-?\d), (-?\d), (-?\d)\]', src)
    z3 = [int(mz.group(k)) for k in (1, 2, 3)]
    return table('pc'), table('pt'), sgn, nflip, z3


# ------------------------------------------------------------------ exact matrices
def eye(n):
    return [[Fr(int(i == j)) for j in range(n)] for i in range(n)]


def mat_mul(A, B):
    Bt = list(zip(*B))
    out = []
    for row in A:
        nz = [(k, v) for k, v in enumerate(row) if v]
        out.append([sum((v * col[k] for k, v in nz), Fr(0)) for col in Bt])
    return out


def mat_vec(A, v):
    return [sum((a * b for a, b in zip(row, v) if a and b), Fr(0)) for row in A]


def kron(A, B):
    return [[a * b for a in ra for b in rb] for ra in A for rb in B]


def inverse(A):
    n = len(A)
    M = [list(A[i]) + [Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return None
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]


def diag(v):
    return [[Fr(v[i]) if i == j else Fr(0) for j in range(len(v))] for i in range(len(v))]


# ------------------------------------------------------------------ the bodies
def units3():
    out = set()
    import itertools
    for t in PYTHAG:
        n2 = sum(a * a for a in t)
        n = int(round(n2 ** 0.5))
        assert n * n == n2
        for p in set(itertools.permutations(t)):
            for s in itertools.product((1, -1), repeat=3):
                out.add(tuple(Fr(si * ai, n) for si, ai in zip(s, p)))
    return sorted(out)


def pick_units(control):
    """pools A and B: disjoint seeded draws from the sorted rational unit vectors of R^3"""
    u = units3()
    rest = list(u)
    pools = {}
    for name in ('A', 'B'):
        rng = random.Random(SEEDS[name])
        chosen = rng.sample(rest, POOL_SIZE[control])
        pools[name] = chosen
        rest = [x for x in rest if x not in set(chosen)]
    return pools


class Body:
    def __init__(self, control):
        pc, pt, sgn, nflip, z3 = kernel_data()
        self.control = control
        self.nflip = nflip
        units = pick_units(control)
        if control == 'eball3':
            self.D = 3
            self.z = [Fr(t) for t in z3]
            self.N = diag(nflip)
            self.pools = {k: {'states': [list(u) for u in v], 'effects': [[Fr(1, 2)] + [c / 2 for c in u] for u in v]}
                          for k, v in units.items()}
            self.reference = cnot16(pc, pt, sgn)
        elif control == 'omegah':
            self.D = 7
            self.z = [Fr(0), Fr(0), Fr(0), Fr(1), Fr(0), Fr(0), Fr(0)]
            self.N = diag([1] + nflip + nflip)
            self.pools = {}
            for k, v in units.items():
                states, effects = [], []
                for u in v:
                    states.append([Fr(1)] + list(u) + list(u))                    # sector 0, r0 = u
                    states.append([Fr(-1)] + list(u) + [-c for c in u])           # sector 1, r1 = u
                h = [Fr(1, 2)]
                for i, u in enumerate(v):
                    w = v[(i + 1) % len(v)]
                    for (al0, be0, al1, be1) in (
                            (h[0], [c / 2 for c in u], h[0], [c / 2 for c in w]),
                            (h[0], [c / 2 for c in u], Fr(0), [Fr(0)] * 3),
                            (h[0], [c / 2 for c in u], Fr(1), [Fr(0)] * 3),
                            (Fr(0), [Fr(0)] * 3, h[0], [c / 2 for c in u]),
                            (Fr(1), [Fr(0)] * 3, h[0], [c / 2 for c in u])):
                        effects.append(sector_to_hom(al0, be0, al1, be1))
                effects.append(sector_to_hom(Fr(1), [Fr(0)] * 3, Fr(0), [Fr(0)] * 3))
                effects.append(sector_to_hom(Fr(0), [Fr(0)] * 3, Fr(1), [Fr(0)] * 3))
                self.pools[k] = {'states': states, 'effects': effects}
            self.reference = omega_gate(pc, pt, sgn)
        else:
            raise SystemExit('unknown control %r' % control)
        self.n = self.D + 1
        self.H = [[Fr(1) if (i == 0 and j == 0) else Fr(0) for j in range(self.n)] for i in range(self.n)]
        for i in range(self.D):
            for j in range(self.D):
                self.H[i + 1][j + 1] = self.N[i][j]

    def member(self, x):
        if self.control == 'eball3':
            return sum(c * c for c in x) <= 1
        w, a, b = x[0], x[1:4], x[4:7]
        t0, t1 = (1 + w) / 2, (1 - w) / 2
        r0 = [(p + q) / 2 for p, q in zip(a, b)]
        r1 = [(p - q) / 2 for p, q in zip(a, b)]
        return t0 >= 0 and t1 >= 0 and sum(c * c for c in r0) <= t0 * t0 and sum(c * c for c in r1) <= t1 * t1

    def effect_ok(self, e):
        if self.control == 'eball3':
            return ball_effect(e[0], e[1:])
        e0, ew, ea, eb = e[0], e[1], e[2:5], e[5:8]
        return (ball_effect(e0 + ew, [p + q for p, q in zip(ea, eb)])
                and ball_effect(e0 - ew, [p - q for p, q in zip(ea, eb)]))


def ball_effect(a, b):
    nb = sum(c * c for c in b)
    return 0 <= a <= 1 and nb <= a * a and nb <= (1 - a) * (1 - a)


def sector_to_hom(al0, be0, al1, be1):
    """alpha0 t0 + beta0.r0 + alpha1 t1 + beta1.r1 in the hom coordinates (1, w, a, b)"""
    return ([(al0 + al1) / 2, (al0 - al1) / 2] + [(p + q) / 2 for p, q in zip(be0, be1)]
            + [(p - q) / 2 for p, q in zip(be0, be1)])


def cnot16(pc, pt, sgn):
    M = [[Fr(0)] * 16 for _ in range(16)]
    for m in range(4):
        for n in range(4):
            M[4 * m + n][4 * pc[(m, n)] + pt[(m, n)]] = Fr(sgn[(m, n)])
    return M


def omega_gate(pc, pt, sgn):
    """E16b's gate as a 64 x 64 matrix: chart tables -> V_q (x) V_b tables, cnot on every sector block, back"""
    idx = lambda mu, i: 2 * mu + i
    PHI = [[Fr(0)] * 8 for _ in range(8)]                  # rows (T, w, a0, a1, a2, b0, b1, b2); columns (mu, i)
    PHI[0][idx(0, 0)] = PHI[1][idx(0, 0)] = PHI[0][idx(0, 1)] = Fr(1)
    PHI[1][idx(0, 1)] = Fr(-1)
    for k in range(3):
        PHI[2 + k][idx(k + 1, 0)] = PHI[5 + k][idx(k + 1, 0)] = PHI[2 + k][idx(k + 1, 1)] = Fr(1)
        PHI[5 + k][idx(k + 1, 1)] = Fr(-1)
    PHIinv = inverse(PHI)
    C = cnot16(pc, pt, sgn)
    # on V_q (x) V_b tables, index (mu, i) (x) (nu, j) -> (idx(mu, i)) * 8 + idx(nu, j); cnot acts on (mu, nu) per (i, j)
    Q = [[Fr(0)] * 64 for _ in range(64)]
    for i in range(2):
        for j in range(2):
            for m in range(4):
                for n in range(4):
                    for m2 in range(4):
                        for n2 in range(4):
                            c = C[4 * m + n][4 * m2 + n2]
                            if c:
                                Q[idx(m, i) * 8 + idx(n, j)][idx(m2, i) * 8 + idx(n2, j)] = c
    P = kron(PHI, PHI)
    Pinv = kron(PHIinv, PHIinv)
    return mat_mul(mat_mul(P, Q), Pinv)


# ------------------------------------------------------------------ the checks
def hom(x):
    return [Fr(1)] + list(x)


def prod(x, y):
    hx, hy = hom(x), hom(y)
    return [a * b for a in hx for b in hy]


def check_VL(body, G):
    z = body.z
    corner = {0: z, 1: [-c for c in z]}
    frame = all(mat_vec(G, prod(corner[a], corner[b])) == prod(corner[a], corner[(a + b) % 2])
                for a in (0, 1) for b in (0, 1))
    T = kron(eye(body.n), body.H)
    C = kron(body.H, eye(body.n))
    relT = mat_mul(mat_mul(T, G), T) == G
    relC = mat_mul(mat_mul(C, G), C) == mat_mul(T, G)
    return frame, relT, relC


def _lcm(a, b):
    from math import gcd
    return a * b // gcd(a, b)


def _scaled(vec):
    """a positive integer multiple of a rational vector, and the multiplier"""
    L = 1
    for c in vec:
        L = _lcm(L, c.denominator)
    return [int(c * L) for c in vec], L


def positivity(body, M, pools=('A', 'B')):
    """over every pooled quadruple, (e (x) f)(M (hom x (x) hom y)): the number of negative values and the minimum.
    Integer arithmetic on positive rescalings (signs are unchanged); the minimum is returned as an exact Fraction."""
    n = body.n
    states = [s for p in pools for s in body.pools[p]['states']]
    effects = [e for p in pools for e in body.pools[p]['effects']]
    LM = 1
    for row in M:
        for c in row:
            LM = _lcm(LM, c.denominator)
    Mi = [[int(c * LM) for c in row] for row in M]
    S = [_scaled(hom(x)) for x in states]
    E = [_scaled(e) for e in effects]
    neg, mn = 0, None
    for hy, sy in S:
        # A[p][k] = sum_l M[p][k n + l] hy[l]
        A = [[sum(row[k * n + l] * hy[l] for l in range(n) if hy[l]) for k in range(n)] for row in Mi]
        for hx, sx in S:
            Wv = [sum(a[k] * hx[k] for k in range(n) if hx[k]) for a in A]
            Wm = [Wv[mu * n:(mu + 1) * n] for mu in range(n)]
            for f, sf in E:
                wf = [sum(r[nu] * f[nu] for nu in range(n) if f[nu]) for r in Wm]
                bv, bs = None, 1
                for e, se in E:
                    val = sum(e[mu] * wf[mu] for mu in range(n) if e[mu])
                    if val < 0:
                        neg += 1
                    if bv is None or val * bs < bv * se:
                        bv, bs = val, se
                tv = Fr(bv, bs * LM * sx * sy * sf)
                if mn is None or tv < mn:
                    mn = tv
    return mn, neg


def verify(body, G, pools=('A', 'B')):
    n2 = body.n * body.n
    out = {'control': body.control}
    shape = isinstance(G, list) and len(G) == n2 and all(isinstance(r, list) and len(r) == n2 for r in G)
    out['shape'] = shape
    if not shape:
        out['verdict'] = 'FAIL'
        return out
    out['VS'] = all(body.member(x) for p in pools for x in body.pools[p]['states'])
    out['VE'] = all(body.effect_ok(e) for p in pools for e in body.pools[p]['effects'])
    frame, relT, relC = check_VL(body, G)
    out['VL'] = {'frame': frame, 'relT': relT, 'relC': relC}
    Ginv = inverse(G)
    out['VI'] = Ginv is not None and mat_mul(G, Ginv) == eye(n2)
    if out['VI'] and frame and relT and relC:
        mf, nf = positivity(body, G, pools)
        mi, ni = positivity(body, Ginv, pools)
        out['VP'] = {'posFwd_min': str(mf), 'posFwd_negative': nf, 'posInv_min': str(mi), 'posInv_negative': ni,
                     'posFwd': nf == 0, 'posInv': ni == 0}
    else:
        out['VP'] = {'posFwd': False, 'posInv': False, 'evaluated': False}
    out['pool_sizes'] = {p: [len(body.pools[p]['states']), len(body.pools[p]['effects'])] for p in pools}
    out['equals_reference'] = G == body.reference
    ok = out['VS'] and out['VE'] and frame and relT and relC and out['VI'] and out['VP']['posFwd'] and out['VP']['posInv']
    out['verdict'] = 'PASS' if ok else 'FAIL'
    return out


# ------------------------------------------------------------------ candidates as data
def to_json_matrix(G):
    return [[str(v) for v in row] for row in G]


def from_json_matrix(rows):
    return [[Fr(v) for v in row] for row in rows]


def squeeze(body, s):
    """1 (x) K_s with K_s = s on the chart coordinates moved by no corner and orthogonal to z's line and fixing hom z"""
    if body.control == 'eball3':
        k = [Fr(1), Fr(s), Fr(s), Fr(1)]
    else:
        k = [Fr(1), Fr(1), Fr(s), Fr(s), Fr(1), Fr(s), Fr(s), Fr(1)]
    return kron(eye(body.n), diag(k))


def self_test():
    """the verifier's own controls: the reference gate passes; the identity fails the frame; ref o (1 (x) K_2) fails
    posFwd; ref o (1 (x) K_1/2) passes VL and posFwd and fails posInv; an invalid effect fails VE; an outside state
    fails VS"""
    lines, ok = [], True
    for control in ('eball3', 'omegah'):
        body = Body(control)
        R = body.reference
        r = verify(body, R)
        c1 = r['verdict'] == 'PASS' and r['equals_reference']
        r = verify(body, eye(body.n * body.n))
        c2 = r['verdict'] == 'FAIL' and not r['VL']['frame']
        r = verify(body, mat_mul(R, squeeze(body, 2)))
        c3 = r['verdict'] == 'FAIL' and all(r['VL'].values()) and not r['VP']['posFwd'] and r['VP']['posInv']
        r = verify(body, mat_mul(R, squeeze(body, Fr(1, 2))))
        c4 = (r['verdict'] == 'FAIL' and all(r['VL'].values()) and r['VP']['posFwd'] and not r['VP']['posInv'])
        saved = body.pools['A']['effects'][0]
        body.pools['A']['effects'][0] = [Fr(1)] + [Fr(1)] * body.D
        c5 = not verify(body, R)['VE']
        body.pools['A']['effects'][0] = saved
        saved = body.pools['A']['states'][0]
        body.pools['A']['states'][0] = [Fr(2)] * body.D
        c6 = not verify(body, R)['VS']
        body.pools['A']['states'][0] = saved
        c7 = verify(body, [[Fr(0)]])['verdict'] == 'FAIL'
        res = [c1, c2, c3, c4, c5, c6, c7]
        lines.append('%s: reference PASS %s; identity fails frame %s; squeeze 2 fails posFwd only %s; squeeze 1/2 '
                     'fails posInv only %s; bad effect fails VE %s; outside state fails VS %s; bad shape fails %s'
                     % (control, *res))
        ok = ok and all(res)
    for ln in lines:
        print(ln)
    print('self-test: %s' % ('OK' if ok else 'FAILED'))
    return ok


def main(argv):
    if argv[1:] == ['--self-test']:
        return 0 if self_test() else 1
    if len(argv) == 4 and argv[1] == '--emit-pool':
        body = Body(argv[2])
        p = body.pools['A']
        json.dump({'control': body.control, 'D': body.D, 'z': [str(c) for c in body.z],
                   'N': to_json_matrix(body.N), 'states': [[str(c) for c in s] for s in p['states']],
                   'effects': [[str(c) for c in e] for e in p['effects']]}, open(argv[3], 'w'), indent=0)
        return 0
    if len(argv) == 5 and argv[1] == '--verify':
        body = Body(argv[2])
        cand = json.load(open(argv[3]))
        if cand.get('control') != body.control or cand.get('G') is None:
            out = {'control': body.control, 'verdict': 'FAIL', 'reason': 'no candidate'}
        else:
            out = verify(body, from_json_matrix(cand['G']))
        json.dump(out, open(argv[4], 'w'), indent=1, sort_keys=True)
        print(json.dumps(out, sort_keys=True))
        return 0 if out['verdict'] == 'PASS' else 1
    print('usage: controls_verify.py --self-test | --emit-pool <control> <out.json> | '
          '--verify <control> <candidate.json> <out.json>')
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
