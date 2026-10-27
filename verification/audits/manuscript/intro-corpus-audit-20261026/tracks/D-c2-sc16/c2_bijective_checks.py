"""Q1 exact checks (PREREG R1, R2, C-bij).

Class B: for every bijection at (2,2),(2,3),(3,2),(2,4) under the uniform initial law, every t = 1..L:
  C2s-full: each positive-probability time-t state (x_t, h_t) has exactly one visible past;
  C2s-supp: posteriors of distinct positive-probability histories with a common endpoint have
            disjoint supports (then TV = 1, the right side of clause (b)).
Also a correlated initial law (random-free: a fixed non-product law) at (2,3) for every bijection.
Countercontrol C-bij: a non-injective reset map must violate both.
Class N: canonical predictive quotient (hidden state = visible future tail) of three exact laws.
"""
import importlib.util, sys, os
from fractions import Fraction as Fr
from collections import defaultdict
from itertools import permutations, product
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('trackd_lib', os.path.join(HERE, 'trackd_lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)


def check_map(step, nV, nH, init, horizon):
    """step: list mapping state index -> state index (any map). init: dict state->weight.
    Returns (violations_full, violations_supp) over t = 1..horizon."""
    vf = vs = 0
    for t in range(1, horizon + 1):
        # past of each initial state up to t
        pasts = defaultdict(set)           # time-t state -> set of visible pasts (x_0..x_{t-1})
        post = defaultdict(lambda: defaultdict(Fr))  # (past, x_t) -> {h_t: weight}
        for z0, w in init.items():
            if w == 0:
                continue
            z = z0; xs = []
            for _ in range(t):
                xs.append(z // nH); z = step[z]
            pasts[z].add(tuple(xs))
            post[(tuple(xs), z // nH)][z % nH] += w
        vf += sum(1 for z, ps in pasts.items() if len(ps) > 1)
        byx = defaultdict(list)
        for (p, x), d in post.items():
            byx[x].append(set(h for h, w in d.items() if w > 0))
        for x, sups in byx.items():
            for i in range(len(sups)):
                for j in range(i + 1, len(sups)):
                    if sups[i] & sups[j]:
                        vs += 1
    return vf, vs


out = []
green = True
for (nV, nH) in [(2, 2), (2, 3), (3, 2), (2, 4)]:
    N = nV * nH
    init = {z: Fr(1, N) for z in range(N)}
    tot_f = tot_s = cnt = 0
    for perm in permutations(range(N)):
        perm = list(perm)
        Lo = L.perm_order(perm)
        vf, vs = check_map(perm, nV, nH, init, Lo)
        tot_f += vf; tot_s += vs; cnt += 1
    out.append(f'class B ({nV},{nH}) uniform init: bijections={cnt} C2s-full violations={tot_f} C2s-supp violations={tot_s}')
    green &= tot_f == 0 and tot_s == 0

# correlated initial law at (2,3): weight proportional to 1 + x*h + 2*[h==0] (not a product law)
nV, nH = 2, 3
raw = {x * nH + h: 1 + x * h + 2 * (h == 0) for x in range(nV) for h in range(nH)}
Z = sum(raw.values())
init = {z: Fr(v, Z) for z, v in raw.items()}
tot_f = tot_s = 0
for perm in permutations(range(6)):
    vf, vs = check_map(list(perm), nV, nH, init, L.perm_order(list(perm)))
    tot_f += vf; tot_s += vs
out.append(f'class B (2,3) correlated init: C2s-full violations={tot_f} C2s-supp violations={tot_s}')
green &= tot_f == 0 and tot_s == 0

# C-bij countercontrol: non-injective map at (2,2): (x,h) -> (x xor h, 0)  (hidden reset)
step = [0] * 4
for x in range(2):
    for h in range(2):
        step[x * 2 + h] = (x ^ h) * 2 + 0
vf, vs = check_map(step, 2, 2, {z: Fr(1, 4) for z in range(4)}, 3)
cbij = vf > 0 and vs > 0
out.append(f'C-bij countercontrol (hidden-reset map): C2s-full violations={vf} C2s-supp violations={vs} -> {"GREEN" if cbij else "RED"}')
green &= cbij

# ---------------- class N: canonical predictive quotient
def quotient_posteriors(P, t):
    """P: dict trajectory -> prob. Hidden state at t = future tail (x_{t+1}..x_K).
    Returns {(past, x_t): {tail: prob}} normalized."""
    post = defaultdict(lambda: defaultdict(Fr))
    for s, w in P.items():
        if w > 0:
            post[(s[:t], s[t])][s[t + 1:]] += w
    res = {}
    for k, d in post.items():
        Z = sum(d.values())
        res[k] = {tl: v / Z for tl, v in d.items()}
    return res

def tv(a, b):
    keys = set(a) | set(b)
    return sum(abs(a.get(k, 0) - b.get(k, 0)) for k in keys) / 2

laws = {}
# i.i.d. fair coin, K = 3
laws['iid coin'] = {s: Fr(1, 16) for s in product((0, 1), repeat=4)}
# XOR law: X0, X1 uniform, X2 = X0 xor X1
laws['XOR'] = {(a, b, a ^ b): Fr(1, 4) for a in (0, 1) for b in (0, 1)}
# ternary-root law: X0 uniform on {0,1,2}, X1 uniform bit, X2 = X1 xor [X0 == 0]
laws['ternary root'] = {(a, b, b ^ (a == 0)): Fr(1, 6) for a in (0, 1, 2) for b in (0, 1)}
for name, P in laws.items():
    q = quotient_posteriors(P, 1)
    byx = defaultdict(list)
    for (p, x), d in q.items():
        byx[x].append((p, d))
    identical = disjoint = partial = 0
    for x, lst in byx.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                d = tv(lst[i][1], lst[j][1])
                if d == 0: identical += 1
                elif d == 1: disjoint += 1
                else: partial += 1
    # clause (b) check: next-step TV <= posterior TV for every pair
    okb = True
    for x, lst in byx.items():
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                n1 = defaultdict(Fr); n2 = defaultdict(Fr)
                for tl, v in lst[i][1].items(): n1[tl[0]] += v
                for tl, v in lst[j][1].items(): n2[tl[0]] += v
                okb &= tv(n1, n2) <= tv(lst[i][1], lst[j][1])
    out.append(f'class N quotient, law={name!r}, t=1: history pairs with common endpoint: '
               f'identical posteriors={identical}, disjoint={disjoint}, partial={partial}; clause (b) holds={okb}')
    green &= okb
for line in out:
    print(line)
print('Q1 CHECKS', 'ALL GREEN' if green else 'FAILED')
