"""Coordinator addendum checks A1-A3 (own code; imports only trackB/oi_exact.py and families.py).
python3 -I -B addendum.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from itertools import product
from oi_exact import Model, divisor, is_perm, identity, matmul, tv_monotone_all

def mat(G):
    return [[str(v) for v in r] for r in G]

def R1_window(M, n):
    return all(divisor(M.Gamma(s), M.Gamma(t))[0] for t in range(1, n + 1) for s in range(0, t))

def routed_at_storage(M, K):
    """Lean PhysicalC4StorageReadback.RoutedReadbackAtStorage K R, transcribed for a finite bijection."""
    nV, nH = M.nV, M.nH
    def it(st, n):
        for _ in range(n):
            st = M.phi[st]
        return st
    def post(a, s, x):  # Law(H_s | X_s = x, X_0 = a): k -> weight
        d = {}
        for h in range(nH):
            if M.muH[h]:
                st = it(a * nH + h, s)
                if st // nH == x:
                    d[st % nH] = d.get(st % nH, F(0)) + M.muH[h]
        tot = M.Gamma(s)[a][x]
        return {k: v / tot for k, v in d.items()} if tot else {}
    def push(p, x, n):
        out = [F(0)] * nV
        for k, v in p.items():
            out[it(x * nH + k, n) // nH] += v
        return out
    wits = []
    for a, b in product(range(nV), repeat=2):
        if a == b:
            continue
        for w in range(1, K):
            W = any(M.muH[h] and it(a * nH + h, w) % nH != it(b * nH + h, w) % nH for h in range(nH))
            if not W:
                continue
            for s in range(w, K):
                for t in range(s + 1, K + 1):
                    for x in range(nV):
                        if not (M.Gamma(s)[a][x] > 0 and M.Gamma(s)[b][x] > 0):
                            continue
                        pa, pb = post(a, s, x), post(b, s, x)
                        if pa == pb:
                            continue
                        if push(pa, x, t - s) == push(pb, x, t - s):
                            continue
                        if M.Gamma(t)[a] == M.Gamma(t)[b]:
                            continue
                        wits.append((a, b, w, s, t, x))
    return wits

# ---------------- A1: candidate (2,3) countermodel
print('A1  V={0,1}, H={0,1,2}, index 3x+h, phi=[0,3,4,1,5,2], uniform mu_H')
M = Model(2, 3, [0, 3, 4, 1, 5, 2], [F(1, 3)] * 3)
print('    L =', M.L, ' r =', M.r)
for t in range(0, 7):
    print(f'    Gamma_{t} =', mat(M.Gamma(t)))
B13 = [[F(1, 3), F(2, 3)], [F(2, 3), F(1, 3)]]; B23 = [[F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]]
claimG = (M.Gamma(1) == B13 == M.Gamma(5) and M.Gamma(2) == M.Gamma(3) == M.Gamma(4) == B23 and M.Gamma(6) == identity(2))
print('    claimed Gamma family reproduced:', claimG)
print('    R1 on {0..5}:', R1_window(M, 5), '  R1 on {0..6}:', R1_window(M, 6))
for s in range(1, 6):
    ok, cert = divisor(M.Gamma(s), M.Gamma(s + 1))
    print(f'      Lambda_{{{s},{s+1}}} =', mat(cert) if ok else 'none (Farkas ' + str([str(v) for v in cert]) + ')')
print('    gaps (order k: TV):', {k: str(M.gap(k)[0]) for k in range(1, 7)})
print('    T = Gamma_1 non-permutation:', not is_perm(M.Gamma(1)), '; literal C1 (n=2):', M.c1(2), '; C1-hist:', M.c1_hist(2))
print('    C3 exact (log2 nH >= I*): ', M.c3())
print('    TV-monotone (all p,q) on {0..5}:', tv_monotone_all([M.Gamma(t) for t in range(6)])[0])
w2 = routed_at_storage(M, 2)
print('    RoutedReadbackAtStorage K=2 witnesses:', w2, '; claimed (0,1,1,1,2,0) present:', (0, 1, 1, 1, 2, 0) in w2)
print('    RoutedReadbackAtStorage K=1:', bool(routed_at_storage(M, 1)))

# ---------------- A2(c): LFSR, general primitive polynomial (degree m+1), all orders
from families import lfsr
def lfsr_general(taps):
    """Sequence X_{t+m+1} = sum_{i in taps} X_{t+i} (mod 2), taps subset of {0..m}, 0 in taps.
    State (X_t, ..., X_{t+m}) with x = X_t, register b_i = X_{t+i}."""
    m = max(max(taps), 1) if False else None
    return None
def lfsr_poly(coeffs):
    """coeffs c_0..c_m (c_0 = 1): X_{t+m+1} = sum_i c_i X_{t+i}.  nV = 2, nH = 2^m."""
    m = len(coeffs) - 1
    nH = 2 ** m
    phi = [0] * (2 * nH)
    for x in range(2):
        for h in range(nH):
            w = [x] + [(h >> i) & 1 for i in range(m)]
            nxt = sum(c * v for c, v in zip(coeffs, w)) % 2
            nw = w[1:] + [nxt]
            phi[x * nH + h] = nw[0] * nH + sum(v << i for i, v in enumerate(nw[1:]))
    return Model(2, nH, phi, [F(1, nH)] * nH)
print()
print('A2(c) LFSR: Gamma_t = J/2 for 1<=t<L, R1 on {0..L-1}, gaps by order')
J2 = [[F(1, 2)] * 2 for _ in range(2)]
polys = {1: [1, 1], 2: [1, 1, 0], 3: [1, 1, 0, 0], 4: [1, 0, 1, 0, 0], 5: [1, 1, 0, 0, 0, 0],
         '3b': [1, 0, 0, 1]}  # x^2+x+1, x^3+x+1, x^4+x+1, x^5+x^2+1, x^6+x+1, x^4+x^3+1
for key, co in polys.items():
    M = lfsr_poly(co)
    m = len(co) - 1
    allJ = all(M.Gamma(t) == J2 for t in range(1, M.L))
    gaps = [M.gap(k)[0] for k in range(1, M.L)]
    below = all(g == 0 for g in gaps[:m - 1])
    atm = all(g == 1 for g in gaps[m - 1:])
    print(f'    coeffs={co} (m={m}): L={M.L} r={M.r} 2^(m+1)-1={2**(m+1)-1}  Gamma_t=J/2 all 1<=t<L: {allJ}  '
          f'R1 on {{0..L-1}}: {"by Lambda=J/2" if allJ else R1_window(M, M.L - 1)}  no gap below m: {below}  gap=1 at every order m..L-1: {atm}')

# ---------------- A2(d): hidden bit g ~ BSC(1/50), flip prob p_g, ledger
print()
print('A2(d) HMM: g_{t+1} = g_t xor Bern(1/50), X_{t+1} = X_t xor Bern(p_{g_t}), p_0=1/5, p_1=2/5, g_0 uniform, ledger l_{t+1} = l_t xor X_t')
eps = F(1, 50); pg = [F(1, 5), F(2, 5)]
T = 9
def path_law(x0):
    """dict over (x_0..x_T) -> prob, given X_0 = x0, g_0 uniform."""
    st = {((x0,), 0): F(1, 2), ((x0,), 1): F(1, 2)}
    for _ in range(T):
        nst = {}
        for (xs, g), p in st.items():
            for fl in (0, 1):
                pf = pg[g] if fl else 1 - pg[g]
                for gf in (0, 1):
                    pgf = eps if gf else 1 - eps
                    k = (xs + (xs[-1] ^ fl,), g ^ gf)
                    nst[k] = nst.get(k, F(0)) + p * pf * pgf
        st = nst
    out = {}
    for (xs, g), p in st.items():
        out[xs] = out.get(xs, F(0)) + p
    return out
laws = {a: path_law(a) for a in (0, 1)}
def Gam(t):
    G = [[F(0)] * 2 for _ in range(2)]
    for a in (0, 1):
        for xs, p in laws[a].items():
            G[a][xs[t]] += p
    return G
# lambda_t by its own formula: E[prod_{i<t}(1 - 2 p_{g_i})] over the g-chain
def lam(t):
    d = {0: F(1, 2), 1: F(1, 2)}
    for _ in range(t):
        nd = {}
        for g, v in d.items():
            v2 = v * (1 - 2 * pg[g])
            nd[g] = nd.get(g, F(0)) + v2 * (1 - eps)
            nd[1 - g] = nd.get(1 - g, F(0)) + v2 * eps
        d = nd
    return sum(d.values())
ok_formula = all(Gam(t) == [[(1 + lam(t)) / 2, (1 - lam(t)) / 2], [(1 - lam(t)) / 2, (1 + lam(t)) / 2]] for t in range(T + 1))
lams = [lam(t) for t in range(T + 1)]
print('    Gamma_t = B((1+lambda_t)/2) with lambda_t = E[prod(1-2p_g)] for t<=9:', ok_formula)
print('    lambda_t positive and strictly decreasing for t<=9:', all(l > 0 for l in lams) and all(lams[i + 1] < lams[i] for i in range(T)))
print('    lambda_1..4 =', [str(l) for l in lams[1:5]])
print('    R1 on {0..9} by exact LP:', all(divisor(Gam(s), Gam(t))[0] for t in range(1, T + 1) for s in range(0, t)))
# gaps: histories (x_0..x_k) under uniform root, next-step laws
def gap_order(k):
    joint = {}
    for a in (0, 1):
        for xs, p in laws[a].items():
            key = xs[:k + 1]
            joint.setdefault(key, [F(0), F(0)])
            joint[key][xs[k + 1]] += p / 2
    best = F(0)
    keys = list(joint)
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            h1, h2 = keys[i], keys[j]
            if h1[-1] != h2[-1]:
                continue
            l1 = [v / sum(joint[h1]) for v in joint[h1]]; l2 = [v / sum(joint[h2]) for v in joint[h2]]
            best = max(best, abs(l1[0] - l2[0]))
    return best
print('    max gap TV at orders 1..5:', [str(gap_order(k)) for k in range(1, 6)])
# Routed readback at storage, K=2, witness (a,b,w,s,t,x) = (0,1,1,1,2,x): clauses W and S hold through the
# ledger (l_1 = X_0 differs between roots for the same seed); R(1) is Law(X_t | X_s = x, X_0 = a), Lean CS1
# identity; R(2) rows of Gamma_t differ since lambda_t != 0.
def cond(a, s, x, t):
    num = [F(0), F(0)]
    for xs, p in laws[a].items():
        if xs[s] == x:
            num[xs[t]] += p
    tot = sum(num)
    return [v / tot for v in num]
for (s, t) in ((1, 2), (1, 4), (3, 4)):
    for x in (0, 1):
        print(f'    R(1) at s={s}, t={t}, x={x}: Law(X_t|X_s=x,X_0=0)={[str(v) for v in cond(0, s, x, t)]} '
              f'vs X_0=1: {[str(v) for v in cond(1, s, x, t)]}  differ: {cond(0, s, x, t) != cond(1, s, x, t)}')
