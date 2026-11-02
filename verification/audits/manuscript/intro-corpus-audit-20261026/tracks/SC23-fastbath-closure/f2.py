#!/usr/bin/env python3
"""sc23 F2 — one-step thermalization vs window-wide Markovianity. Implements PREREG.txt F2.
python3 -I f2.py  (exit 0 iff all controls green)"""
import sys, itertools, random
from fractions import Fraction as F
from collections import defaultdict

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][l] * B[l][j] for l in range(n)) for j in range(n)] for i in range(n)]
def matpow(T, k):
    n = len(T); R = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for _ in range(k): R = matmul(R, T)
    return R
def tvnorm(A, B):
    return max(sum(abs(A[i][j] - B[i][j]) for j in range(len(A))) / 2 for i in range(len(A)))

class Model:
    """phi: dict (x,h)->(x',h'); B: None (id) | dict h->h (bijection) | 'reset'"""
    def __init__(s, name, nV, H, phi, B=None, bijective=True):
        s.name, s.nV, s.H, s.phi, s.B, s.bij = name, nV, list(H), phi, B, bijective
        s.m = len(s.H)
    def step_dist(s, x, h):
        x2, h2 = s.phi[(x, h)]
        if s.B is None: return [((x2, h2), F(1))]
        if s.B == 'reset': return [((x2, hh), F(1, s.m)) for hh in s.H]
        return [((x2, s.B[h2]), F(1))]

def ensembles(M, K):
    """ens[t]: dict (record x_0..x_t, h_pre_t) -> prob, x0 uniform, h0 ~ pi_H uniform."""
    ens = [defaultdict(F)]
    for x in range(M.nV):
        for h in M.H: ens[0][((x,), h)] += F(1, M.nV * M.m)
    for t in range(K):
        new = defaultdict(F)
        for (rec, h), p in ens[t].items():
            for (x2, h2), q in M.step_dist(rec[-1], h):
                new[(rec + (x2,), h2)] += p * q
        ens.append(new)
    return ens

def rooted_T(ens, M, k):
    num = [[F(0)] * M.nV for _ in range(M.nV)]
    for (rec, h), p in ens[k].items(): num[rec[0]][rec[-1]] += p
    return [[num[i][j] / sum(num[i]) for j in range(M.nV)] for i in range(M.nV)]

def cond_hidden(ens_t, keyf):
    groups = defaultdict(lambda: defaultdict(F))
    for (rec, h), p in ens_t.items(): groups[keyf(rec)][h] += p
    return groups

def tv_pi(dist, M):
    tot = sum(dist.values())
    return sum(abs(dist.get(h, F(0)) / tot - F(1, M.m)) for h in M.H) / 2

def gap(ens, M, k):
    """delta_k from the law of x_0..x_{k+1}"""
    Pk1 = defaultdict(F)
    for (rec, h), p in ens[k + 1].items(): Pk1[rec] += p
    Pk = defaultdict(F)
    for rec, p in Pk1.items(): Pk[rec[:-1]] += p
    best = F(0)
    for c in range(M.nV):
        hs = [r for r in Pk if Pk[r] > 0 and r[-1] == c]
        cond = {r: [Pk1.get(r + (j,), F(0)) / Pk[r] for j in range(M.nV)] for r in hs}
        for a, b in itertools.combinations(hs, 2):
            best = max(best, sum(abs(u - v) for u, v in zip(cond[a], cond[b])) / 2)
    return best

def analyse(M, K, extra_k=()):
    ens = ensembles(M, K + 1)
    T = rooted_T(ens, M, 1)
    out = {'T': T, 'Dk': {}, 'OST': True, 'CL': True, 'epsFR': {}, 'delta': {}, 'ident': True}
    for t in range(K):
        for d in cond_hidden(ens[t], lambda r: r[-1]).values():
            if tv_pi(d, M) != 0: out['OST'] = False
        for d in cond_hidden(ens[t], lambda r: (r[0], r[-1])).values():
            if tv_pi(d, M) != 0: out['CL'] = False
        fr = cond_hidden(ens[t], lambda r: r)
        out['epsFR'][t] = max(tv_pi(d, M) for d in fr.values())
        if M.bij:  # CF2-d identity
            for rec, d in fr.items():
                tot = sum(d.values())  # = P(record) = P(x0) P(x1..xt|x0)
                if tv_pi(d, M) != 1 - tot * M.nV:
                    out['ident'] = False
    for k in range(1, K + 1):
        Tk = rooted_T(ens, M, k)
        out['Dk'][k] = tvnorm(Tk, matpow(T, k))
    for k in range(1, K):
        out['delta'][k] = gap(ens, M, k)
    out['extra'] = {}
    for k in extra_k:  # direct rooted maps for long k
        cnt = [[F(0)] * M.nV for _ in range(M.nV)]
        for x in range(M.nV):
            for h in M.H:
                s = (x, h)
                for _ in range(k): s = M.phi[s]
                cnt[x][s[0]] += F(1, M.m)
        out['extra'][k] = (cnt, tvnorm(cnt, matpow(T, k)))
    return out, ens

def is_bij(phi, space):
    return sorted(phi[s] for s in space) == sorted(space)

fail = 0
def check(n, ok, info=""):
    global fail
    print(f"  [{'PASS' if ok else 'FAIL'}] {n} {info}"); fail += (not ok)

K = 6
models = {}
# M1 Main §2.4 sigma; hidden 1..6
H6 = list(range(1, 7)); phi1 = {(x, h): (x, h) for x in (0, 1) for h in H6}
for a, b in [((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (0, 4)), ((0, 5), (0, 6)), ((1, 3), (1, 4)), ((1, 5), (1, 6))]:
    phi1[a] = b; phi1[b] = a
models['M1'] = Model('M1 Main 2.4 sigma', 2, H6, phi1)
# M2
models['M2'] = Model('M2 (x^h, x)', 2, [0, 1], {(x, h): (x ^ h, x) for x in (0, 1) for h in (0, 1)})
# M3 rotation bath
b = (1, 1, 0)
models['M3'] = Model('M3 rotation z->z+1 mod 3', 2, [0, 1, 2], {(x, z): (x ^ b[z], (z + 1) % 3) for x in (0, 1) for z in range(3)})
# M4 random
rng = random.Random(2310)
space4 = [(x, h) for x in (0, 1) for h in range(16)]
img = space4[:]; rng.shuffle(img); phi4 = dict(zip(space4, img))
perm = list(range(16)); rng.shuffle(perm)
B4 = {h: h for h in range(16)}
for _ in range(5): B4 = {h: perm[B4[h]] for h in range(16)}
models['M4'] = Model('M4 random phi on Z2xZ16, B=perm^5', 2, range(16), phi4, B4)
# N1 tape
tapes = list(itertools.product((0, 1, 2), repeat=5))
models['N1'] = Model('N1 tape {0,1,2}^5 (closure holds)', 2, tapes,
                     {(x, s): (x ^ int(s[0] == 0), s[1:] + s[:1]) for x in (0, 1) for s in tapes})
# N2 reset
models['N2'] = Model('N2 M1 sigma + hidden reset', 2, H6, phi1, 'reset', bijective=False)

print("== CF2-a bijectivity ==")
for key, M in models.items():
    sp = [(x, h) for x in range(M.nV) for h in M.H]
    ok = is_bij(M.phi, sp) and (not isinstance(M.B, dict) or sorted(M.B.values()) == sorted(M.H))
    check(f"CF2-a {key} coupling map (and B) bijective", ok)

res = {}
for key, M in models.items():
    res[key], _ = analyse(M, K, extra_k=(10,) if key == 'N1' else ())

print("== controls ==")
check("CF2-b N1 Dk == 0 exactly for k=1..5", all(res['N1']['Dk'][k] == 0 for k in range(1, 6)), str({k: str(v) for k, v in res['N1']['Dk'].items()}))
check("CF2-b N2 Dk == 0 exactly for k=1..6", all(v == 0 for v in res['N2']['Dk'].values()))
for key in models:
    r = res[key]
    ok = all(r['Dk'][k] <= (k - 1) * max([r['epsFR'][t] for t in range(1, k)] or [F(0)]) for k in range(1, K + 1))
    check(f"CF2-c {key} ||T^(k)-T^k|| <= (k-1) max eps_FR", ok)
for key in ('M1', 'M2', 'M3', 'M4', 'N1'):
    check(f"CF2-d {key} TV(P(H_t|X_0..X_t), pi_H) == 1 - P(X_1..X_t|X_0) on every record", res[key]['ident'])
# CF2-e
M1 = models['M1']; e1 = ensembles(M1, 3)
T1 = res['M1']['T']; T2 = rooted_T(e1, M1, 2)
P = defaultdict(F)
for (rec, h), p in e1[2].items(): P[rec] += p
p_010 = P[(0, 1, 0)] / (P[(0, 1, 0)] + P[(0, 1, 1)])
num = P[(0, 1, 0)] + P[(1, 1, 0)]; den = num + P[(0, 1, 1)] + P[(1, 1, 1)]
check("CF2-e M1 reproduces Main 2.4 numbers",
      T1 == [[F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]] and T2 == [[1, 0], [0, 1]] and p_010 == 1 and num / den == F(1, 3),
      f"(T={T1}, T2={T2}, P(x2=0|x1=1,x0=0)={p_010}, P(x2=0|x1=1)={num/den})")

print("== data ==")
for key, M in models.items():
    r = res[key]
    print(f" {M.name}: OST(all t<{K})={r['OST']}  CL(all t)={r['CL']}  T={[[str(v) for v in row] for row in r['T']]}")
    print(f"    Dk=||T^(k)-T^k||: {[str(r['Dk'][k]) for k in range(1, K + 1)]}")
    print(f"    eps_FR(t), t=0..{K-1}: {[str(r['epsFR'][t]) for t in range(K)]}")
    print(f"    delta_k, k=1..{K-1}: {[str(r['delta'][k]) for k in range(1, K)]}")
    for k, (cnt, dk) in r['extra'].items():
        print(f"    k={k}: T^(k)={[[str(v) for v in row] for row in cnt]}  ||T^(k)-T^k||={dk}")

# V2-3 exhaustive
print("== exhaustive: all bijections of Z2xZ2 and Z2xZ3 (B=id) ==")
ex = {}
for m in (2, 3):
    sp = [(x, h) for x in (0, 1) for h in range(m)]
    n_ost = n_dev = n_tot = n_mem = 0
    for img in itertools.permutations(sp):
        M = Model('ex', 2, range(m), dict(zip(sp, img)))
        r, _ = analyse(M, K)
        n_tot += 1; n_ost += r['OST']
        n_dev += any(v != 0 for v in r['Dk'].values())
        n_mem += any(v != 0 for v in r['delta'].values())
    ex[m] = (n_tot, n_ost, n_dev, n_mem)
    print(f"  m={m}: bijections={n_tot}  OST holds at all t<{K}: {n_ost}  with T^(k)!=T^k for some k<={K}: {n_dev}  with a gap (delta_k>0, k<{K}): {n_mem}")

print("== verdicts ==")
if fail:
    print("  VOID: a control failed")
else:
    w = [k for k in ('M1', 'M2', 'M3', 'M4') if res[k]['OST'] and any(res[k]['Dk'][kk] != 0 for kk in range(2, K + 1))]
    print(f"  V2-1: {'PRINT' if w else 'no'} — models with exact OST and T^(k)!=T^k: {w}")
    w2 = [k for k in ('M1', 'M2', 'M3', 'M4') if res[k]['OST'] and any(v > 0 for v in res[k]['delta'].values())]
    print(f"  V2-2: {'PRINT' if w2 else 'no'} — models with exact OST and a positive gap: {w2}")
    allost = all(ex[m][0] == ex[m][1] for m in ex)
    print(f"  V2-3: {'PRINT' if allost else 'no'} — OST holds for every bijection tested ({ {m: ex[m] for m in ex} })")
print("f2:", "ALL CONTROLS GREEN" if not fail else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
