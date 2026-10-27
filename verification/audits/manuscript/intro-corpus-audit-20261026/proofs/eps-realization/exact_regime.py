# Independent exact-rational check of clause (1), exact-arithmetic regime (Main.md:546/558),
# with a 3-outcome instrument, a two-Kraus (mixed-conditional) outcome, rational rotations,
# random ADAPTIVE protocols, horizons K = 1..3, grids G = 1..9 and 16, 64.
# Realized conditional per step: seed r uniform on {0..G-1}; outcome o chosen iff
#   G*F_{o-1} <= r*S < G*F_o   (F cumulative unnormalized weights, S total)  -- exact thresholds.
from fractions import Fraction as F
import itertools, random

def mat(a): return [[F(x) for x in row] for row in a]
def mul(A, B): return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def T(A): return [[A[j][i] for j in range(2)] for i in range(2)]
def add(A, B): return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
def apply(Ks, rho):
    out = mat([[0, 0], [0, 0]])
    for K in Ks: out = add(out, mul(mul(K, rho), T(K)))
    return out
tr = lambda A: A[0][0] + A[1][1]
R345 = mat([[F(3,5), F(-4,5)], [F(4,5), F(3,5)]]); R51213 = mat([[F(5,13), F(-12,13)], [F(12,13), F(5,13)]])
P0 = mat([[1, 0], [0, 0]]); P1 = mat([[0, 0], [0, 1]])
def conj(U, A): return mul(mul(U, A), T(U))
INSTR = {
  "Z":   [[P0], [P1]],
  "X":   [[conj(R345, P0)], [conj(R345, P1)]],                          # rotated projective, non-dyadic
  "T3":  [[[[F(3,5), 0], [0, 0]]], [[[F(4,5), 0], [0, 0]]], [P1]],        # 3 outcomes
  "MIX": [[[[F(3,5), 0], [0, 0]], [[0, 0], [F(4,5), 0]]], [P1]],          # 2 Kraus in outcome 0 -> mixed
  "U":   [[R51213]],                                                       # outcome-free
}
INSTR = {k: [[mat(K) if not isinstance(K[0][0], F) else K for K in Ks] for Ks in v] for k, v in INSTR.items()}
# check trace preservation exactly
for k, v in INSTR.items():
    S = mat([[0, 0], [0, 0]])
    for Ks in v:
        for K in Ks: S = add(S, mul(T(K), K))
    assert S == mat([[1, 0], [0, 1]]), k
OMAX = max(len(v) for v in INSTR.values())

def laws(policy, K, G, rho0):
    q, r = {}, {}
    def rec(rho_q, rho_r, h, wq, wr):
        if len(h) == K:
            q[h] = q.get(h, 0) + wq; r[h] = r.get(h, 0) + wr; return
        a = policy(h)
        bq = [apply(Ks, rho_q) for Ks in INSTR[a]]
        br = [apply(Ks, rho_r) for Ks in INSTR[a]]     # exact ring: same update (unnormalized)
        w = [tr(B) for B in br]; S = sum(w)
        cum = [sum(w[:i + 1]) for i in range(len(w))]
        cnt = [0] * len(w)
        for s in range(G):
            for i in range(len(w)):
                if s * S < G * cum[i]: cnt[i] += 1; break
        Sq = sum(tr(B) for B in bq)
        for i in range(len(w)):
            pq = tr(bq[i]) / Sq if Sq else F(0)
            if wq * pq == 0 and wr * F(cnt[i], G) == 0: continue
            rec(bq[i], br[i], h + ((a, i),), wq * pq, wr * F(cnt[i], G))
    rec(rho0, rho0, (), F(1), F(1))
    keys = set(q) | set(r)
    return sum(abs(q.get(k, 0) - r.get(k, 0)) for k in keys) / 2

random.seed(3)
rho0 = mat([[F(1, 3), F(1, 5)], [F(1, 5), F(2, 3)]])
worst = F(0); viol = 0; n = 0
for K in (1, 2, 3):
    for _ in range(60):
        table = {}
        def pol(h):
            if h not in table: table[h] = random.choice(list(INSTR))
            return table[h]
        for G in list(range(1, 10)) + [16, 64]:
            tv = laws(pol, K, G, rho0); n += 1
            bound = F(K * (OMAX - 1), G)
            if tv > bound: viol += 1
            worst = max(worst, tv / bound)
print(f"runs {n}; violations of TV <= K(|O|max-1)/G: {viol}; worst TV/bound = {float(worst):.4f}")
# per-step grid lemma, exhaustive over rational distributions with denominators <= 8, |O| <= 4
wr = F(0)
for nO in (2, 3, 4):
    for G in range(1, 13):
        for den in range(1, 9):
            for nums in itertools.product(range(den + 1), repeat=nO - 1):
                if sum(nums) > den: continue
                p = [F(x, den) for x in nums] + [1 - F(sum(nums), den)]
                cum = 0; cnt = []
                prev = 0
                for x in p:
                    cum += x
                    c = sum(1 for s in range(G) if s < G * cum) - prev; prev += c; cnt.append(c)
                tvs = sum(abs(F(c, G) - x) for c, x in zip(cnt, p)) / 2
                assert tvs < F(nO - 1, G) or tvs == 0, (p, G)
                wr = max(wr, tvs * G / (nO - 1))
print(f"per-step grid bound exhaustive check passed; worst TV / ((|O|-1)/G) = {float(wr):.4f}")
