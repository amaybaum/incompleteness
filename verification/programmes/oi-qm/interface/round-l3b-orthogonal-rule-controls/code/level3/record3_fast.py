"""Level 3A fast evaluator: RECORD's record_fast.py (sealed; int64 counts, prefix-sharing trie) plus the letter 'c'.

St, initial, leap, pair_map, kfn are imported unchanged; step3 is record_fast.step with the 'c' branch; run_all3 is
record_fast.run_all with step3. Output is checked equal to record3_sim.run3 (validate3_fast.py).
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'record'))
from record_fast import St, initial, leap, pair_map, kfn, LEAPS   # noqa: E402,F401
from record_sim import PASSIVE                                    # noqa: E402
from record3_sim import c_perm                                    # noqa: E402


def step3(st, s, rule, kappa, left_after):
    if s in 'om':
        st = pair_map(st, kfn(kappa), s == 'o')
    elif s == 'p':
        st = pair_map(st, kfn(PASSIVE), True)
    elif s == 'f':
        st = pair_map(st, lambda q: (q ^ 2, None), False)
    elif s == 's':
        st = pair_map(st, lambda q: (((q & 1) << 1) | (q >> 1), None), False)
    elif s == 'c':
        st = pair_map(st, lambda q: (c_perm(q), None), False)
    elif s != 'i':
        raise ValueError(s)
    if s in LEAPS:
        st = leap(st, min(st.a + 1, left_after), rule)
    return st


def run_all3(protocols, rule, kappa, step=None):
    """dict protocol -> (counts per record string, total mass); identical to record3_sim.run3 per protocol."""
    step = step or step3
    out = {}
    groups = {}
    for pr in set(protocols):
        groups.setdefault(sum(1 for s in pr if s in LEAPS), []).append(pr)
    for T, prs in groups.items():
        trie = {}
        for pr in prs:
            node = trie
            for s in pr:
                node = node.setdefault(s, {})
            node[None] = pr

        def walk(node, st, left):
            if None in node:
                out[node[None]] = ([int(x) for x in st.P.sum(axis=0)], 4 ** st.m)
            for s, ch in node.items():
                if s is None:
                    continue
                la = left - (1 if s in LEAPS else 0)
                walk(ch, step(st, s, rule, kappa, la), la)
        walk(trie, initial(), T)
    return out
