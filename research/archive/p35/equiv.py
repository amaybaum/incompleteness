"""Equivalence control for the act-35 profile fast path: on every fourth-root matrix that sections 3 and 4 of
dita_defect_probe.py pass to profile2 or pvalues, the exponent-count profile equals the Gaussian-rational profile
of the probe as landed at 8ae3522c, value for value and type for type; the non-fourth-root matrices of the probe
(Σ, the Diţă point with nine rational twists) are refused by the fast path."""
import time, sys, itertools
from fractions import Fraction as Fr
new = open('wt-probe35/verification/lean/dita_defect_probe.py', encoding='utf-8').read()
old = open('p35/old_probe.py', encoding='utf-8').read()
exec(new[:new.index("print('== 1.")])                       # the new definitions, including the fast path
exec(old[old.index('def profile(H)'):old.index('def profile2')].replace('def profile(', 'def profile_gauss('))  # the landed G path
# the matrices of sections 1-4, built exactly as the probe builds them
exec(new[new.index("z = G(Fr(3, 5)"):new.index("for name, H, want in")])
exec(new[new.index("CENSUS = ["):new.index("kron_inv = {}")])
mats = {}
for nm, X, Ys in (('H4⊗H4', circle(0, ONE), [circle(0, ONE)] * 4), ('H4⊗F4', circle(0, ONE), [circle(0, I_)] * 4),
                  ('F4⊗H4', circle(0, I_), [circle(0, ONE)] * 4), ('F4⊗F4', circle(0, I_), [circle(0, I_)] * 4)):
    mats[nm] = dita(X, Ys, unitD())
for n_, c in enumerate(CENSUS):
    X = circle(c['X'][0], ROOTS[c['X'][1]]); Ys = [circle(r, ROOTS[zz]) for r, zz in c['Y']]
    D = [[ROOTS[c['D'][cc][b]] for b in range(4)] for cc in range(4)]
    mats['census %d' % n_] = dita(X, Ys, D)
mats['H34'] = H34; mats['HW'] = HW; mats['F4F4'] = F4F4; mats['H4H4'] = H4H4; mats['HR'] = HR
X = circle(CENSUS[0]['X'][0], ROOTS[CENSUS[0]['X'][1]]); Ys = [circle(r, ROOTS[zz]) for r, zz in CENSUS[0]['Y']]
D = [[ROOTS[CENSUS[0]['D'][cc][b]] for b in range(4)] for cc in range(4)]
H0 = dita(X, Ys, D); mats['H0'] = H0
pi = [4 * ((a + 1) % 4) + ((b + 2) % 4) for a in range(4) for b in range(4)]; tau = [4 * ((c + 3) % 4) + ((d + 1) % 4) for c in range(4) for d in range(4)]
mats['H1'] = relabel(H0, pi, tau, cj=True, tr=True)
bad = []; tg = tn = 0.0
for nm, H in mats.items():
    HT = [[H[j][i] for j in range(16)] for i in range(16)]
    for lab, M in ((nm, H), (nm + '^T', HT)):
        E = fourth_root_exponents(M)
        if E is None: bad.append(lab + ': not recognized as fourth-root'); continue
        t = time.time(); pg = profile_gauss(M); tg += time.time() - t
        t = time.time(); pe = profile_of_exponents(E); tn += time.time() - t
        if pg != pe: bad.append(lab + ': profile differs')
        if repr(pg) != repr(pe): bad.append(lab + ': repr differs')
        if any(type(x) is not Fr for trip in pe for x in trip): bad.append(lab + ': non-Fraction value')
    if profile2(H) != tuple(sorted((profile_gauss(H), profile_gauss(HT)))): bad.append(nm + ': profile2 differs')
    if repr(pvalues(H)) != repr(set(x for trip in profile_gauss(H) for x in trip)): bad.append(nm + ': pvalues repr differs')
refused = [nm for nm, M in (('Σ', SIG), ('DIT', DIT)) if fourth_root_exponents(M) is None]
print('matrices compared (row and column profiles each):', len(mats), '; disagreements:', len(bad), bad)
print('non-fourth-root matrices refused by the fast path:', refused)
print('Gaussian-rational path %.0f s, exponent-count path %.1f s over %d profiles' % (tg, tn, 2 * len(mats)))
sys.exit(1 if bad or len(refused) != 2 else 0)
