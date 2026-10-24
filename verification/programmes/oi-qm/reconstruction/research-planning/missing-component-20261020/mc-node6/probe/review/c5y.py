"""Reviewer check: C5 is the toy bit's Z/X dynamics with sharp preparations and the toy's Y readout removed.
Adding the toy Y step (p ^= b0^b1; b0 ^= r; b1 ^= r) to C5's accessible set breaks parity obliviousness for w > 0."""
from fractions import Fraction as F
from itertools import product
def run(bits, seq, rs):
    b = list(bits); rec = []
    for t, y in enumerate(seq):
        if y == 2:
            rec.append(b[0] ^ b[1]); b[0] ^= rs[t]; b[1] ^= rs[t]
        else:
            rec.append(b[y]); b[1 - y] ^= rs[t]
    return tuple(rec)
def law(mix, seq):
    L = {}
    for bits, w in mix.items():
        for rs in product((0, 1), repeat=len(seq)):
            k = run(bits, seq, rs); L[k] = L.get(k, 0) + w * F(1, 2 ** len(seq))
    return L
def prep(x, w):
    m = {l: (1 - w) * F(1, 4) for l in product((0, 1), repeat=2)}; m[x] += w; return m
for w in (F(1), F(7, 10), F(1, 2)):
    p0 = {}; p1 = {}
    for x in ((0, 0), (1, 1)):
        for k, v in prep(x, w).items(): p0[k] = p0.get(k, 0) + v / 2
    for x in ((0, 1), (1, 0)):
        for k, v in prep(x, w).items(): p1[k] = p1.get(k, 0) + v / 2
    print(f'w={w}: Y-readout law parity-0 {law(p0,(2,))} vs parity-1 {law(p1,(2,))}')
# toy-bit Z/X steps equal C5 steps (identity of dynamics) on all 2^4 states
def toy(s, k):
    a, b, p, r = s
    if k == 'Z': return (a, b ^ r, p ^ a, r)
    return (a ^ r, b, p ^ b, r)
def c5(s, y):
    b = [s[0], s[1]]; p = s[2] ^ b[y]; b[1 - y] ^= s[3]; return (b[0], b[1], p, s[3])
print('toy Z == C5 y=0 and toy X == C5 y=1 on all states:',
      all(toy(s, 'Z') == c5(s, 0) and toy(s, 'X') == c5(s, 1) for s in product((0, 1), repeat=4)))
