"""Exhaustive exact search (PREREG R3/R4): bijections at (n_V,n_H) in {(2,2),(2,3),(3,2),(2,4)},
uniform prior on V x H (time-homogeneous, stationary). For each: order L, rooted family, gap orders,
n_div, and the forms C4-alone, F2, F2max, F3. Controls C-2x2 and C-rec run inline.
Usage: python3 -I -B sc16_search.py [sizes...]   e.g. 2x2 2x3 3x2 2x4"""
import importlib.util, sys, os, json
from fractions import Fraction as Fr
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('trackd_lib', os.path.join(HERE, 'trackd_lib.py'))
L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)

sizes = sys.argv[1:] or ['2x2', '2x3', '3x2', '2x4']
summary = {}
stats = {'cf_checked': 0, 'cf_disagree': 0}
all_green = True
for sz in sizes:
    nV, nH = map(int, sz.split('x'))
    N = nV * nH
    S = dict(total=0, with_gap=0, crec_violations=0, f3_neq_f2=0, kbar_mismatch=0,
             c4_counter=0, f2_counter=0, f2max_counter=0, best_excess=None,
             best_f2_window=0, first=dict())
    for perm in L.all_perms(N):
        perm = list(perm)
        S['total'] += 1
        Lo = L.perm_order(perm)
        G = L.rooted_family(perm, nV, nH, Lo)
        trajs = L.trajectories(perm, nV, nH, Lo + 1)
        P = L.law_from_trajs(trajs)
        gaps = {}
        for k in range(1, Lo + 1):
            g, d, _ = L.gap_at(P, k, nV)
            gaps[k] = (g, d)
        # F3 check: K-bar_x vs P(X_{t+1} | X_t = x), and F3 <=> gap
        Kbar = []
        for x in range(nV):
            row = [Fr(0)] * nV
            for h in range(nH):
                row[perm[x * nH + h] // nH] += Fr(1, nH)
            Kbar.append(row)
        for t in range(1, Lo + 1):
            Mt1 = L.marginal(P, t + 2); Mt = L.marginal(P, t + 1)
            px = defaultdict(Fr); pxy = defaultdict(Fr)
            for s, w in Mt1.items():
                pxy[(s[t], s[t + 1])] += w
            for s, w in Mt.items():
                px[s[t]] += w
            for x in range(nV):
                if px[x] > 0 and [pxy[(x, y)] / px[x] for y in range(nV)] != Kbar[x]:
                    S['kbar_mismatch'] += 1
            # F3 at t: some history-conditional differs from Kbar_{x_t}
            f3 = False
            for s, w in Mt.items():
                if w > 0:
                    cond = [Mt1.get(s + (y,), Fr(0)) / w for y in range(nV)]
                    if cond != Kbar[s[-1]]:
                        f3 = True; break
            if f3 != gaps[t][0]:
                S['f3_neq_f2'] += 1
        any_gap = any(g for g, _ in gaps.values())
        if not any_gap:
            continue
        S['with_gap'] += 1
        nd, fail = L.n_div(G, Lo, closed_form_check=(nV == 2), stats=stats)
        if nd >= Lo:
            S['crec_violations'] += 1
        kmin = min(k for k, (g, _) in gaps.items() if g)
        excess = nd - (kmin + 1)
        if S['best_excess'] is None or excess > S['best_excess']:
            S['best_excess'] = excess
        rec = dict(perm=perm, L=Lo, kmin=kmin, n_div=nd, first_fail=fail,
                   gaps={k: [g, str(d)] for k, (g, d) in gaps.items()},
                   Gamma=[[[str(v) for v in r] for r in G[t]] for t in range(min(Lo, nd + 1) + 1)])
        # C4 alone: gap at order k with k+1 <= n_div (and k+1 <= L-1 automatically since n_div < L)
        if excess >= 0:
            S['c4_counter'] += 1
            S['first'].setdefault('C4', rec)
        # F2: largest n <= n_div with gaps at every order 1..n-1, n >= 2
        n2 = 0
        for n in range(2, nd + 1):
            if all(gaps[t][0] for t in range(1, n)):
                n2 = n
        if n2 >= 2:
            S['f2_counter'] += 1
            S['first'].setdefault('F2', rec)
            if n2 > S['best_f2_window']:
                S['best_f2_window'] = n2
                S['first']['F2_best'] = dict(rec, window=n2)
        n2m = 0
        for n in range(2, nd + 1):
            if all(gaps[t][0] and gaps[t][1] == 1 for t in range(1, n)):
                n2m = n
        if n2m >= 2:
            S['f2max_counter'] += 1
            S['first'].setdefault('F2max', dict(rec, window=n2m))
    green = (S['crec_violations'] == 0 and S['kbar_mismatch'] == 0 and S['f3_neq_f2'] == 0)
    all_green &= green
    summary[sz] = S
    print(f"{sz}: total={S['total']} with_gap={S['with_gap']} C-rec_violations={S['crec_violations']} "
          f"Kbar_mismatch={S['kbar_mismatch']} F3!=gap={S['f3_neq_f2']} | C4-alone countermodels={S['c4_counter']} "
          f"best n_div-(kmin+1)={S['best_excess']} | F2 countermodels={S['f2_counter']} best F2 window n={S['best_f2_window']} "
          f"| F2max countermodels={S['f2max_counter']}")
print(f"C-2x2 closed-form cross-checks: {stats['cf_checked']} pairs, disagreements={stats['cf_disagree']}")
all_green &= stats['cf_disagree'] == 0
print('INLINE CONTROLS', 'ALL GREEN' if all_green else 'FAILED')
with open(os.path.join(HERE, 'out_sc16_' + '_'.join(sizes) + '.json'), 'w') as f:
    json.dump(summary, f, indent=1)
