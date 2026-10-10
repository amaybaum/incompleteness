"""Exploration only: same cover as cover.py but with every test class at the exact parameter z = i
(feature values S i^m / 64, Gaussian integers over 64); phi(F(i)) = F(-i)."""
import itertools
from collections import Counter
import cover as C
def val(sym):
    S, m = sym
    return S * (1j ** (m % 4))
for shape in (1, 2, 3, 4):
    miss = {}
    for pt in C.S_ALL:
        miss[pt] = set((r, n) for r in range(9) for n in range(4096)
                       if val(C.member_sym(shape, pt, r, n)) != val(C.phi_sym(r, n)))
    empty = [pt for pt in miss if not miss[pt]]
    uncovered = set(C.S_ALL) - set(empty); chosen = []
    while uncovered:
        cnt = Counter()
        for pt in uncovered:
            for key in miss[pt]: cnt[key] += 1
        best, c = cnt.most_common(1)[0]
        chosen.append((best[0], C.COORDS[best[1]], c))
        uncovered = {pt for pt in uncovered if best not in miss[pt]}
    print("shape", shape, "members NOT separable with all tests at z=i:", len(empty), "; cover", len(chosen), chosen)
