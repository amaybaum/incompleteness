"""Amendment 1 (R5, C-F4): RoutedReadbackAtStorage(K), transcribed from
verification/lean-mathlib/OIBridge/PhysicalC4StorageReadback.lean, tested for accessible-window
P-divisibility.
  (1) controls: Lean core carrier (positive at K=2), decoupled bijection (negative), LFSR m=2 (R(2)
      negative for K <= L-1);
  (2) exhaustive search under the uniform prior at (2,2),(2,3),(3,2),(2,4): bijections with F4(K) and
      P-divisible on {0..K}, K <= L-1 (smallest K with F4);
  (3) explicit (EM)/(C2-slow) bijection: hidden-modulated flip rate with a ledger write, K = 4.
"""
import importlib.util, sys, os
from fractions import Fraction as Fr
from itertools import permutations, product
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('trackd_lib', os.path.join(HERE, 'trackd_lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)


class Real:
    """Rooted realization: states are (v, h) index pairs; step: dict/list on state ids; prior on h."""
    def __init__(self, nV, nH, step, prior):
        self.nV, self.nH, self.step, self.prior = nV, nH, step, prior  # step: list over v*nH+h
        self.cache = {}
    def it(self, z, n):
        key = (z, n)
        if key not in self.cache:
            y = z
            for _ in range(n):
                y = self.step[y]
            self.cache[key] = y
        return self.cache[key]
    def rooted(self, t):
        M = [[Fr(0)] * self.nV for _ in range(self.nV)]
        for a in range(self.nV):
            for h in range(self.nH):
                if self.prior[h]:
                    M[a][self.it(a * self.nH + h, t) // self.nH] += self.prior[h]
        return M
    def state_post(self, a, s, x):
        w = defaultdict(Fr)
        for h in range(self.nH):
            if self.prior[h]:
                y = self.it(a * self.nH + h, s)
                if y // self.nH == x:
                    w[y % self.nH] += self.prior[h]
        Z = sum(w.values())
        return {k: v / Z for k, v in w.items()} if Z else None


def F4(R, K):
    """Exact transcription of RoutedReadbackAtStorage K R. Returns witness tuple or None."""
    nV, nH = R.nV, R.nH
    G = [R.rooted(t) for t in range(K + 1)]
    for a in range(nV):
        for b in range(nV):
            if a == b:
                continue
            for w in range(1, K):
                Wok = any(R.prior[h] and R.it(a * nH + h, w) % nH != R.it(b * nH + h, w) % nH for h in range(nH))
                if not Wok:
                    continue
                for s in range(w, K):
                    for t in range(s + 1, K + 1):
                        if G[t][a] == G[t][b]:
                            continue
                        for x in range(nV):
                            if G[s][a][x] > 0 and G[s][b][x] > 0:
                                pa, pb = R.state_post(a, s, x), R.state_post(b, s, x)
                                if pa == pb:
                                    continue
                                ma = defaultdict(Fr); mb = defaultdict(Fr)
                                for k, v in pa.items(): ma[R.it(x * nH + k, t - s) // nH] += v
                                for k, v in pb.items(): mb[R.it(x * nH + k, t - s) // nH] += v
                                if dict(ma) != dict(mb):
                                    return (a, b, w, s, t, x)
    return None


green = True
# ---- controls
# Lean core: V = Bool x Bool encoded v*2+b, H = Bool; step ((v,b),h) = ((h,b),v); uniform prior
step = [0] * 8
for v in (0, 1):
    for b in (0, 1):
        for h in (0, 1):
            step[(v * 2 + b) * 2 + h] = (h * 2 + b) * 2 + v
core = Real(4, 2, step, [Fr(1, 2)] * 2)
c_core = F4(core, 2) is not None and F4(core, 1) is None
# decoupled bijection (2,3): phi(x,h) = (1-x, (h+x+1) mod 3)
step = [(1 - x) * 3 + (h + x + 1) % 3 for x in range(2) for h in range(3)]
dec = Real(2, 3, step, [Fr(1, 3)] * 3)
c_dec = all(F4(dec, K) is None for K in range(1, 7))
# LFSR m=2 (x^3+x+1): state (s0,s1,s2), visible s0
def enc(bits): return bits[0] * 4 + bits[1] + 2 * bits[2]
step = [0] * 8
for z in range(8):
    x, h = divmod(z, 4); s = [x, h & 1, (h >> 1) & 1]
    step[z] = enc(s[1:] + [(s[0] + s[1]) % 2])
lf = Real(2, 4, step, [Fr(1, 4)] * 4)
c_lfsr = all(F4(lf, K) is None for K in range(1, 7))
print(f'C-F4: core F4(2) true and F4(1) false: {c_core}; decoupled F4 false K<=6: {c_dec}; LFSR(m=2) F4 false K<=6 (R(2) control): {c_lfsr}')
green &= c_core and c_dec and c_lfsr

# ---- exhaustive search, uniform prior
first = {}
for (nV, nH) in [(2, 2), (2, 3), (3, 2), (2, 4)]:
    N = nV * nH
    n_f4 = n_counter = 0
    best = None
    for perm in permutations(range(N)):
        perm = list(perm)
        Lo = L.perm_order(perm)
        R = Real(nV, nH, perm, [Fr(1, nH)] * nH)
        Kf = None
        for K in range(2, Lo):
            if F4(R, K) is not None:
                Kf = K; break
        if Kf is None:
            continue
        n_f4 += 1
        G = [R.rooted(t) for t in range(Lo + 1)]
        nd, _ = L.n_div(G, Lo - 1)
        if nd >= Kf:
            n_counter += 1
            if best is None or nd - Kf > best[0]:
                best = (nd - Kf, perm, Lo, Kf, nd, F4(R, Kf))
    first[(nV, nH)] = best
    print(f'({nV},{nH}): bijections with F4 at some K <= L-1: {n_f4}; of these P-divisible on {{0..K_F4}}: {n_counter}; '
          f'best (n_div - K_F4, perm, L, K_F4, n_div, witness (a,b,w,s,t,x)) = {best}')

# ---- explicit (EM)/(C2-slow) bijection: modulated flip rate + ledger write, window K = 4
K = 4
eta = Fr(1, 50)
U = 5  # u uniform on {0..4}; flip iff u < thr[g]; thr = (1, 2) -> p0 = 1/5, p1 = 2/5
thr = (1, 2)
hid = list(product((0, 1), (0, 1), product(range(U), repeat=K), product((0, 1), repeat=K)))  # (g, l, u, f)
hidx = {h: i for i, h in enumerate(hid)}
nH = len(hid)
step = [0] * (2 * nH)
for x in (0, 1):
    for hi, (g, l, u, f) in enumerate(hid):
        e = 1 if u[0] < thr[g] else 0
        x2 = x ^ e
        h2 = (g ^ f[0], l ^ x, tuple(u[1:]) + (u[0],), tuple(f[1:]) + (f[0],))
        step[x * nH + hi] = x2 * nH + hidx[h2]
bij = sorted(step) == list(range(2 * nH))
prior = []
for (g, l, u, f) in hid:
    w = Fr(1, 2) if l == 0 else Fr(0)       # g uniform, ledger blank
    w *= Fr(1, U ** K)
    for b in f:
        w *= eta if b else 1 - eta
    prior.append(w)
assert sum(prior) == 1
R = Real(2, nH, step, prior)
G = [R.rooted(t) for t in range(K + 1)]
div, bad = L.p_divisible_window(G, K, closed_form_check=True)
wit = F4(R, K)
# gaps under a uniform root
P = defaultdict(Fr)
for x0 in (0, 1):
    for hi in range(nH):
        if prior[hi]:
            z = x0 * nH + hi; xs = [x0]
            for _ in range(K):
                z = step[z]; xs.append(z // nH)
            P[tuple(xs)] += prior[hi] / 2
P = dict(P)
gaps = {k: L.gap_at(P, k, 2)[:2] for k in range(1, K)}
lam = [G[t][0][0] - G[t][1][0] for t in range(K + 1)]
ok = bij and div and wit is not None and all(g for g, _ in gaps.values())
print(f'EM/C2-slow modulated-flip bijection: |S|={2*nH}, bijective={bij}; eigenvalues of Gamma_t: {[str(v) for v in lam]}; '
      f'P-divisible on {{0..{K}}}: {div}; F4({K}) witness (a,b,w,s,t,x): {wit}; gaps: { {k: (g, str(d)) for k, (g, d) in gaps.items()} } -> {"OK" if ok else "FAIL"}')
green &= ok
print('F4 RUN', 'CONTROLS GREEN' if green else 'FAILED')
