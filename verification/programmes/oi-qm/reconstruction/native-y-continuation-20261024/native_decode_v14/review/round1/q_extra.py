"""rev910b extra: planted-law representation check, explicit counterexample laws."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from native_table import q10_table
from review_checks import kernel, readout_sets, solve, FEAT, CTX, idx, law_value, field_coeffs
tab_hex, _, _ = q10_table(); tab = [int(c, 16) for c in tab_hex]; K = kernel(tab)
full = set(FEAT); QA = 0b11110000
def cols_from_fields(fc):
    return {FEAT[j]: sum(((fc[f] >> j) & 1) << (5 - f) for f in range(6)) for j in range(6)}
def plant(cols):
    t = list(tab)
    for k in CTX:
        v = law_value(cols, k)
        for s in (0, 1):
            t[idx(s ^ k[0] ^ k[3], k, v >> 3, v & 7)] = 5 if s else 2
    return t
out = {}
mine = {'1': 37, 'u': 12, 'mY': 55, 'mR': 41, 'a': 22, 'b': 7}
auth = cols_from_fields((37, 12, 55, 41, 22, 7))
out['author_planted_as_columns'] = auth
for name, cols in (('mine', mine), ('author', auth)):
    c, sols = solve(readout_sets(kernel(plant(cols)), QA), full, collect=True)
    out['planted_count_' + name] = [c, any(x == cols for x in sols)]
# laws where q10.A = x exactly (target f = 0) and fewest seeds
sets = {}
from review_checks import key_of
for k in CTX:
    sets[key_of(k)] = sum(1 << v for v in range(64) if all(((QA >> tab[idx(x, k, v >> 3, v & 7)]) & 1) == x for x in (0, 1)))
c, sols = solve(sets, full, collect=True)
best = min(sols, key=lambda col: (sum(1 for n, x in col.items() if n != '1' and x), field_coeffs(col)))
out['qA_equals_x_laws'] = c
out['qA_equals_x_fewest_seed_law_fields'] = field_coeffs(best)
# direct check of that law: A = x on all 48 rows
out['qA_equals_x_direct_ok'] = all(((tab[idx(x, k, law_value(best, k) >> 3, law_value(best, k) & 7)] >> 2) & 1) == x for k in CTX for x in (0, 1))
# B sign-free q10.A=s laws
c, sols = solve(readout_sets(K, QA), full, collect=True)
bfree = []
for col in sols:
    if all(((K[0][k][law_value(col, k)] >> 1) & 1) == ((K[1][k][law_value(col, k)] >> 1) & 1) for k in CTX):
        bfree.append(field_coeffs(col))
out['qA_laws_B_sign_free'] = sorted(bfree)
# mY-only law: q10 raw codes per context
law = next(col for col in sols if field_coeffs(col) == [1, 5, 1, 4, 1, 5])
out['mY_law_contexts_B_dep'] = sum(((K[0][k][law_value(law, k)] >> 1) & 1) != ((K[1][k][law_value(law, k)] >> 1) & 1) for k in CTX)
out['mY_law_contexts_D_dep'] = sum((K[0][k][law_value(law, k)] & 1) != (K[1][k][law_value(law, k)] & 1) for k in CTX)
out['mY_law_E_N_codes_mY0_mY1'] = [[law_value(law, (0, my, 0, 0, 0)) >> 3, law_value(law, (0, my, 0, 0, 0)) & 7] for my in (0, 1)]
# rejected contexts (a,b)=(0,1): does the mY law also give A = s there?
rej = [k for k in __import__('itertools').product((0, 1), repeat=5) if (k[3], k[4]) == (0, 1)]
out['mY_law_A_equals_s_on_rejected_contexts'] = sum(all(((tab[idx(s ^ k[0] ^ k[3], k, law_value(law, k) >> 3, law_value(law, k) & 7)] >> 2) & 1) == s for s in (0, 1)) for k in rej)
print(json.dumps(out, indent=1))
