"""SC-22 exact probes: classical BLP-type revival of the rooted family vs conditional memory,
capacity, and bath persistence, on finite bijective realizations (Main §2.3 objects).

Objects (Main §2.3 :137, Lean OIBridge/CausalReadback.lean):
  Gamma_t(a, j) = mu_H{h : pi_V phi^t(a,h) = j}, mu_H uniform, shared by every root.
  d_t(a,b) = tv(Gamma_t a, Gamma_t b) = 1/2 sum |.|          (point roots)
  R_K      = max_{a != b, s < t <= K} (d_t - d_s)^+            (peak revival, in [0,1])
  B_K      = max_{a != b} sum_{t=1..K} (d_t - d_{t-1})^+       (BLP-type cumulative revival, point roots)
  R_K > 0  <=>  B_K > 0  <=>  Lean C4r K Gamma.
Memory: an order-k gap = two positive-probability histories (x_0..x_k), (x'_0..x'_k) with x_k = x'_k and
different next-step laws (Main §1.3 C4); decided exactly with Fractions. CMI values printed as floats
(log of exact rationals); only their positivity is used, and it is decided by the exact gap test.
P-divisibility on {0..K}: decided only by exact witnesses (unique inverse when Gamma_s is invertible;
Lambda = I when Gamma_s = Gamma_t; Lambda = Gamma_t when Gamma_s = I; rank-one Gamma_s); otherwise 'undecided'.
"""
from fractions import Fraction as Fr
from itertools import product
from math import log2
import sys

def rooted(phi, nV, nH, K):
    """phi: dict (x,h)->(x',h'). Returns list Gamma_0..Gamma_K (uniform mu_H)."""
    G = []
    for t in range(K + 1):
        M = [[Fr(0)] * nV for _ in range(nV)]
        for a in range(nV):
            for h in range(nH):
                s = (a, h)
                for _ in range(t):
                    s = phi[s]
                M[a][s[0]] += Fr(1, nH)
        G.append(M)
    return G

def tv(p, q):
    return sum(abs(x - y) for x, y in zip(p, q)) / 2

def revival(G, K):
    nV = len(G[0]); R = Fr(0); B = Fr(0)
    for a in range(nV):
        for b in range(a + 1, nV):
            d = [tv(G[t][a], G[t][b]) for t in range(K + 1)]
            for s in range(K + 1):
                for t in range(s + 1, K + 1):
                    R = max(R, d[t] - d[s])
            B = max(B, sum(max(Fr(0), d[t] - d[t - 1]) for t in range(1, K + 1)))
    return R, B

def law(phi, nV, nH, K):
    """joint law of (X_0..X_K), uniform visible prior and uniform hidden prior, independent."""
    P = {}
    for x in range(nV):
        for h in range(nH):
            s = (x, h); path = [x]
            for _ in range(K):
                s = phi[s]; path.append(s[0])
            P[tuple(path)] = P.get(tuple(path), Fr(0)) + Fr(1, nV * nH)
    return P

def marg(P, idx):
    out = {}
    for k, v in P.items():
        kk = tuple(k[i] for i in idx); out[kk] = out.get(kk, Fr(0)) + v
    return out

def gap_orders(P, K):
    """orders k (1..K-1) with two positive-probability histories of length k+1 sharing x_k, different next-step laws."""
    res = []
    for k in range(1, K):
        H = marg(P, range(k + 1)); H1 = marg(P, range(k + 2))
        nxt = {}
        for hist, ph in H.items():
            if ph == 0: continue
            lawn = tuple(sorted((y[-1], v / ph) for y, v in H1.items() if y[:-1] == hist))
            nxt.setdefault(hist[-1], set()).add(lawn)
        if any(len(v) > 1 for v in nxt.values()):
            res.append(k)
    return res

def H_(d):
    return -sum(float(v) * log2(float(v)) for v in d.values() if v > 0)

def cmi_past_future(P, t, K):
    """I(X_<t ; X_>t | X_t) in bits from the exact law on {0..K}."""
    past = list(range(t)); now = [t]; fut = list(range(t + 1, K + 1))
    return (H_(marg(P, past + now)) + H_(marg(P, now + fut)) - H_(marg(P, now)) - H_(marg(P, past + now + fut)))

def matmul(A, B):
    n = len(A); return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def inv(A):
    n = len(A); M = [row[:] + [Fr(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None: return None
        M[c], M[p] = M[p], M[c]; pv = M[c][c]; M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]; M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]

def stoch(L):
    return all(x >= 0 for row in L for x in row) and all(sum(row) == 1 for row in L)

def pdiv(G, K):
    n = len(G[0]); I = [[Fr(int(i == j)) for j in range(n)] for i in range(n)]
    for s in range(K + 1):
        for t in range(s + 1, K + 1):
            Gs, Gt = G[s], G[t]
            if Gs == Gt or Gs == I: continue
            Gi = inv(Gs)
            if Gi is not None:
                L = matmul(Gi, Gt)
                if not stoch(L): return f"P-indivisible (unique divisor {s}->{t} has a negative entry)"
                continue
            if all(Gs[i] == Gs[0] for i in range(n)):  # rank one: Gs*L has rows uL; need Gt rows equal
                if all(Gt[i] == Gt[0] for i in range(n)): continue  # L = Gt works
                return f"P-indivisible (rank-one Gamma_{s}, Gamma_{t} rows differ)"
            return f"undecided at {s}->{t}"
    return "P-divisible (exact witnesses)"

def perm_model(perm, nV, nH):
    # index s = x*nH + h (Track B convention)
    return {(s // nH, s % nH): (perm[s] // nH, perm[s] % nH) for s in range(nV * nH)}

def order(phi):
    keys = list(phi); s0 = {k: k for k in keys}; t = 0; cur = dict(s0)
    while True:
        cur = {k: phi[v] for k, v in cur.items()}; t += 1
        if all(cur[k] == k for k in keys): return t

def report(name, phi, nV, nH, windows, note=""):
    L = order(phi); Kmax = max(max(windows), L)
    G = rooted(phi, nV, nH, Kmax); P = law(phi, nV, nH, Kmax)
    gaps = gap_orders(P, Kmax)
    print(f"== {name}  (n_V={nV}, n_H={nH}, log2 n_H={log2(nH):.4g}, order L={L}) {note}")
    print(f"   gap orders on {{0..{Kmax}}}: {gaps}")
    for K in windows + [L]:
        R, B = revival(G, K)
        print(f"   window {{0..{K}}}: peak revival R={R}, BLP-type B={B}, {pdiv(G, K)}")
    Is = [round(cmi_past_future(P, t, Kmax), 6) for t in range(1, Kmax)]
    print(f"   I(X_<t;X_>t|X_t), t=1..{Kmax-1} on horizon {Kmax}: {Is}")
    return G

if __name__ == "__main__":
    # (A) Main §2.4 minimal model, V={0,1}, H={1..6} -> h index 0..5
    sw = {}
    for x in (0, 1):
        for h in range(6): sw[(x, h)] = (x, h)
    for h in (0, 1): sw[(0, h)], sw[(1, h)] = (1, h), (0, h)
    for x in (0, 1):
        sw[(x, 2)], sw[(x, 3)] = (x, 3), (x, 2); sw[(x, 4)], sw[(x, 5)] = (x, 5), (x, 4)
    report("A Main 2.4 minimal model", sw, 2, 6, [1, 2])
    # (B) XOR (2,2) [0,3,1,2]
    report("B XOR", perm_model([0, 3, 1, 2], 2, 2), 2, 2, [2])
    # (C) XOR x idle ledger of size M: capacity margin log2(2M) - 1 bits
    for M in (2, 8):
        phi = {}
        base = perm_model([0, 3, 1, 2], 2, 2)
        for x in (0, 1):
            for h in range(2):
                for l in range(M):
                    x2, h2 = base[(x, h)]; phi[(x, h * M + l)] = (x2, h2 * M + l)
        report(f"C XOR + idle ledger M={M}", phi, 2, 2 * M, [2], note=f"(C3 margin log2(2M)-I* = {log2(2*M)-1:g} bits if I*=1)")
    # (D) block-XOR, n_V = 2k, n_H = 2: capacity ratio n_H/n_V = 1/k
    for k in (1, 3, 8):
        phi = {}
        base = perm_model([0, 3, 1, 2], 2, 2)
        for b in range(k):
            for x in (0, 1):
                for h in (0, 1):
                    x2, h2 = base[(x, h)]; phi[(2 * b + x, h)] = (2 * b + x2, h2)
        report(f"D block-XOR k={k}", phi, 2 * k, 2, [2], note=f"(n_H/n_V = 1/{k}, log2 n_H/log2 n_V = {1/log2(2*k) if k>1 else 1:.4g})")
    # (E) static bath p = 3: phi(x,h) = (x+h mod 3, h); tau_B = infinity literally
    phi = {(x, h): ((x + h) % 3, h) for x in range(3) for h in range(3)}
    report("E static bath p=3", phi, 3, 3, [2])
    # (F) Track B (2,3) [0,3,4,1,5,2]
    report("F (2,3) [0,3,4,1,5,2]", perm_model([0, 3, 4, 1, 5, 2], 2, 3), 2, 3, [5])
    # Controls
    print("== controls")
    # K1: P-divisible family must have zero revival (Lean not_c4e_and_not_c4r_of_pDivisible): Markov powers of T
    T = [[Fr(2, 3), Fr(1, 3)], [Fr(1, 3), Fr(2, 3)]]
    Gm = [[[Fr(1), Fr(0)], [Fr(0), Fr(1)]]]
    for _ in range(6): Gm.append(matmul(Gm[-1], T))
    print("   K1 Markov powers T^t, t<=6:", pdiv(Gm, 6), "R =", revival(Gm, 6)[0])
    # K2: the swap (Track B K1) revives and is P-indivisible on {0,1,2}
    Gs = [[[Fr(1), Fr(0)], [Fr(0), Fr(1)]], [[Fr(1, 2), Fr(1, 2)], [Fr(1, 2), Fr(1, 2)]], [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]]
    print("   K2 I, J/2, I:", pdiv(Gs, 2), "R =", revival(Gs, 2)[0])
    # K3: gap detector on an i.i.d. fair coin (no memory): static ledger that never influences
    coin = {(x, h): (h % 2, (h + 1) % 4 if False else h) for x in range(2) for h in range(4)}
    coin = {(x, h): ((h >> 0) & 1, h) for x in range(2) for h in range(4)}  # X_t = h bit for t>=1: not iid; replaced below
    # i.i.d. coin via tape: hidden tape of 3 bits shifted, visible reads fresh bit; horizon 2 only
    tape = {}
    for x in range(2):
        for h in range(8):
            b0 = h & 1; rest = h >> 1
            tape[(x, h)] = (b0, (rest | (x << 2)))  # ledger stores old x at top bit; read bit consumed
    Pt = law(tape, 2, 8, 3)
    print("   K3 tape-and-ledger coin, gap orders on {0..3}:", gap_orders(Pt, 3), "(expected [])")
    # F(r) = 2r - r^2 monotonicity on [0,1] at exact grid and continuity with limit 1
    grid = [Fr(i, 8) for i in range(9)]
    vals = [2 * r - r * r for r in grid]
    print("== F(r)=2r-r^2 on r=0..1 step 1/8:", [str(v) for v in vals],
          "strictly increasing:", all(vals[i] < vals[i + 1] for i in range(8)), "F(1) =", vals[-1])
