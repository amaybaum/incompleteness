"""PREREG-3A section 6 item 1: on the radius-0 state, every word over {f, s, c} of length <= 4 acts on the visible
pair as its abstract permutation (checked on each delta state); the generated group has 24 elements, {f, s} 8."""
from itertools import product
import numpy as np
from record3_sim import State, c_perm

ABSTRACT = {'f': lambda q: q ^ 2, 's': lambda q: ((q & 1) << 1) | (q >> 1), 'c': c_perm}
SIM = {'f': lambda q: (q ^ 2, None), 's': lambda q: (((q & 1) << 1) | (q >> 1), None), 'c': lambda q: (c_perm(q), None)}


def closure(letters):
    G = {(0, 1, 2, 3)}
    frontier = set(G)
    while frontier:
        new = set()
        for h in frontier:
            for g in letters:
                q = tuple(ABSTRACT[g](h[p]) for p in range(4))
                if q not in G:
                    new.add(q)
        G |= new
        frontier = new
    return G


bad = words = 0
for L in range(5):
    for w in product('fsc', repeat=L):
        words += 1
        for p in range(4):
            st = State()
            st.P = np.zeros((4, 1), dtype=object)
            st.P[p, 0] = 1
            q = p
            for g in w:
                st.pair_map(SIM[g], record=False)
                q = ABSTRACT[g](q)
            if not (st.P[q, 0] == 1 and st.P.sum() == 1):
                bad += 1
print(f'UNIT-LETTERS: {words} words x 4 delta states, mismatches {bad}; |<f,s,c>| = {len(closure("fsc"))}, '
      f'|<f,s>| = {len(closure("fs"))}; c = {tuple(c_perm(q) for q in range(4))}')
print('UNIT-LETTERS', 'OK' if bad == 0 and len(closure('fsc')) == 24 and len(closure('fs')) == 8 else 'FAILED')
