"""NP-AVG-1 Stage 0, S6: exact proof-check of PO8 (the Phi-in-clear lemma) on the
21-bit reference structure of Phi only. No native record of the class is involved.

Under the fair prior the seven Phi triples (q8, q10, m, o1, o2, o3 at slice n+1 and V
at n+2) are i.i.d. uniform (L2). p = V ^ H(q8^q10^m^o1^o2^o3) (backward rule).
J = (Y, R, Z) = (q8.B, q10.D, q10.B); s = p.B; t1(s)_j = n(y^s, r^s), t0 = 8 - t1.
For every subset of at most two of the six slice-(n+1) triples read in clear, and every
public value (p, V, read triples) with p.A = 0, the J-law must be neither t1/20 nor
t0/44 (PO8). Positive control: adding v6's flag A = [K < n(Y^s, R^s)] to the record,
with K = q8.A + 2 q8.D + 4 q10.A, makes every class target-law (the statistic can pass).
Negative control: the flag with permuted thresholds (5,4,0,1) fails.
Standard library, exact integers. Prints JSON; exit 0 iff all hold."""
import json
import sys
from collections import defaultdict
from itertools import combinations

HT = tuple(4*((v >> 1) & 1) + 2*(v & 1) + (((v >> 2) & 1) ^ ((v >> 1) & (v & 1) & 1)) for v in range(8))
NT = {(0, 0): 5, (0, 1): 0, (1, 0): 4, (1, 1): 1}
NBAD = {(0, 0): 5, (0, 1): 4, (1, 0): 0, (1, 1): 1}
NAMES = ('q8', 'q10', 'm', 'o1', 'o2', 'o3')


def comp(v, i):          # 0 = A, 1 = B, 2 = D
    return (v >> (2 - i)) & 1


def targets(s):
    t1 = [NT[y ^ s, r ^ s] for y in (0, 1) for r in (0, 1) for z in (0, 1)]
    return t1, [8 - c for c in t1]


def prop(counts, target):
    tot, tt = sum(counts), sum(target)
    return tot > 0 and all(c*tt == t*tot for c, t in zip(counts, target))


def main():
    subsets = [()] + [(i,) for i in range(6)] + list(combinations(range(6), 2))
    assert len(subsets) == 22
    classes = {k: defaultdict(lambda: [0]*8) for k in range(len(subsets))}
    pos = defaultdict(lambda: [0]*8)
    neg = defaultdict(lambda: [0]*8)
    for w in range(1 << 21):
        t = [(w >> (3*i)) & 7 for i in range(7)]
        six, V = t[:6], t[6]
        x = 0
        for v in six:
            x ^= v
        p = V ^ HT[x]
        if comp(p, 0) != 0:
            continue
        s = comp(p, 1)
        q8, q10 = six[0], six[1]
        Y, R, Z = comp(q8, 1), comp(q10, 2), comp(q10, 1)
        j = 4*Y + 2*R + Z
        K = comp(q8, 0) + 2*comp(q8, 2) + 4*comp(q10, 0)
        for k, S in enumerate(subsets):
            classes[k][(p, V) + tuple(six[i] for i in S)][j] += 1
        A = int(K < NT[Y ^ s, R ^ s])
        Ab = int(K < NBAD[Y ^ s, R ^ s])
        pos[(p, V, A)][j] += 1
        neg[(p, V, Ab)][j] += 1
    res = {'label': 'proof-check of PO8; not a result', 'worlds': 1 << 21, 'subsets': len(subsets), 'per_subset': {}}
    ok = True
    for k, S in enumerate(subsets):
        target_classes = 0
        for key, c in classes[k].items():
            s = comp(key[0], 1)
            t1, t0 = targets(s)
            target_classes += prop(c, t1) or prop(c, t0)
        res['per_subset']['+'.join(NAMES[i] for i in S) or 'none'] = {
            'classes': len(classes[k]), 'target_law_classes': target_classes}
        ok &= target_classes == 0
    pos_ok = all(prop(c, targets(comp(key[0], 1))[1 - key[2]]) for key, c in pos.items())
    neg_bad = sum(not (prop(c, targets(comp(key[0], 1))[0]) or prop(c, targets(comp(key[0], 1))[1]))
                  for key, c in neg.items())
    res['positive_control_flag_A_all_target'] = pos_ok
    res['negative_control_permuted_flag_nontarget_classes'] = neg_bad
    res['pass'] = ok and pos_ok and neg_bad > 0
    print(json.dumps(res, sort_keys=True))
    sys.exit(0 if res['pass'] else 2)


if __name__ == '__main__':
    main()
