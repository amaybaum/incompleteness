"""Exhaustive search over all bijections of V x H for given (nV, nH) and hidden priors.
python3 -I -B enumerate_all.py nV nH prior_label [workers]
prior_label in {uniform, skew, pure}.  Decision rule: PREREGISTRATION.txt."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from itertools import permutations
from multiprocessing import Pool
from oi_exact import Model, analyze, divisor, is_perm, identity

def prior(nH, label):
    if label == 'uniform':
        return [F(1, nH)] * nH
    if label == 'pure':
        return [F(1)] + [F(0)] * (nH - 1)
    if label == 'skew':
        return {2: [F(1, 3), F(2, 3)], 3: [F(1, 2), F(1, 3), F(1, 6)],
                4: [F(1, 2), F(1, 4), F(1, 8), F(1, 8)]}[nH]
    raise ValueError(label)

def one(args):
    nV, nH, phi, label = args
    M = Model(nV, nH, phi, prior(nH, label))
    res = dict(L=M.L, r=M.r, phi=phi)
    # K5 (Main Sec. 2.3 Scope equivalence) -- needs full-support visible prior (uniform here)
    gapL = any(M.gap(k)[0] > 0 for k in range(1, M.L))
    nonpermL = any(not is_perm(M.Gamma(s)) for s in range(1, M.L))
    failL = any(not divisor(M.Gamma(s), M.Gamma(t))[0] for t in range(2, M.L + 1) for s in range(1, t))
    res['K5'] = (gapL == nonpermL == failL)
    res['K5r'] = (not any(not is_perm(M.Gamma(s)) for s in range(1, M.r))) or \
        any(not divisor(M.Gamma(s), M.Gamma(M.r))[0] for s in range(1, M.r))
    recs, gaps = analyze(M, want_c3=False)
    cms = []
    acc_c4 = []
    for rec in recs:
        if rec['C1'] and rec['C2s'] and rec['C4']:
            acc_c4.append(rec)
            if any(rec[R] for R in ('R1', 'R2', 'R3', 'R4')):
                cms.append(rec)
    res['acc_c4'] = [(x['n'], x['c4_orders'][0], x['R1'], x['R2'], x['R3'], x['R4']) for x in acc_c4]
    res['C1hist_all'] = all(x['C1hist'] for x in acc_c4)
    if cms:
        ok, sat = M.c3()          # exact C3 on every countermodel candidate
        res['C3'] = ok; res['C3sat'] = sat
    res['static'] = M.static_bath()
    return res

def main():
    nV, nH, label = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    workers = int(sys.argv[4]) if len(sys.argv) > 4 else 1
    S = nV * nH
    jobs = ((nV, nH, list(p), label) for p in permutations(range(S)))
    tot = 0; k5bad = 0; k5rbad = 0
    nacc = 0; cnt = {R: 0 for R in ('R1', 'R2', 'R3', 'R4')}; nwin = 0
    win_div = {R: 0 for R in cnt}
    c3bad = 0; c1hist_bad = 0
    examples = {}
    best_ratio = None
    static_cm = 0
    with Pool(workers) as pool:
        for res in pool.imap_unordered(one, jobs, chunksize=256):
            tot += 1
            k5bad += (not res['K5']); k5rbad += (not res['K5r'])
            if res['acc_c4']:
                nacc += 1
                c1hist_bad += (not res['C1hist_all'])
                for (n, k, *Rs) in res['acc_c4']:
                    nwin += 1
                    for R, v in zip(('R1', 'R2', 'R3', 'R4'), Rs):
                        win_div[R] += v
                for R, i in zip(('R1', 'R2', 'R3', 'R4'), range(4)):
                    if any(w[2 + i] for w in res['acc_c4']):
                        cnt[R] += 1
                        if R not in examples:
                            w = next(w for w in res['acc_c4'] if w[2 + i])
                            examples[R] = (res['phi'], res['L'], res['r'], w)
                if any(w[2] for w in res['acc_c4']):
                    if 'C3' in res and not res['C3']:
                        c3bad += 1
                    static_cm += res['static']
                    w = max((w for w in res['acc_c4'] if w[2]), key=lambda w: w[0])
                    ratio = (F(w[1], res['r']), F(w[0], res['r']))
                    if best_ratio is None or (res['r'], w[0]) > (best_ratio[0], best_ratio[1]):
                        best_ratio = (res['r'], w[0], w[1], res['phi'])
    print(f'class (nV,nH)=({nV},{nH}) prior={label} {prior(nH, label)}: bijections={tot}')
    print(f'  K5 (Scope equivalence gap<L <=> nonperm Gamma_s <=> R1 fails on {{0..L}}) violations: {k5bad}  [{"GREEN" if k5bad == 0 else "RED"}]'
          + ('' if label != 'pure' and label != 'skew' else '  (full-support visible prior; equivalence asserted by Main for full support)'))
    print(f'  K5r (nonperm Gamma_s, s<r => R1 fails on {{0..r}}) violations: {k5rbad}  [{"GREEN" if k5rbad == 0 else "RED"}]')
    print(f'  bijections with an accessible window (2<=n<r) satisfying C1 & C2s & C4: {nacc}  (windows: {nwin})')
    print(f'  of those, C1-hist also holds in every such window: {nacc - c1hist_bad}/{nacc}')
    for R in cnt:
        print(f'  reading {R}: bijections with >=1 accessible C1&C2s&C4 window that is {R}-divisible: {cnt[R]};  windows: {win_div[R]}/{nwin}')
    print(f'  K7 C3 exact failures among R1-countermodels: {c3bad}  [{"GREEN" if c3bad == 0 else "RED"}]; static-bath R1-countermodels: {static_cm}')
    for R, (phi, L, r, w) in examples.items():
        print(f'  first {R} countermodel: phi={phi} L={L} r={r} window n={w[0]} gap order k={w[1]} (R1,R2,R3,R4)={w[2:]}')
    if best_ratio:
        print(f'  largest r among R1-countermodels: r={best_ratio[0]}, window n={best_ratio[1]}, gap order k={best_ratio[2]}, phi={best_ratio[3]}')

if __name__ == '__main__':
    main()
