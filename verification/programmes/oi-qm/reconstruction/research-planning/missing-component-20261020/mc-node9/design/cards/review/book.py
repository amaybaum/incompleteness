from fractions import Fraction as F
import itertools
# swap core from a depleted two-colour deck of N cards (N/2 red): cards dealt v0, h0, fresh f (third card)
for N in (4, 6, 24):
    deck = ['R']*(N//2) + ['B']*(N//2)
    tot = 0; one = 0; ep = 0; burnvis = 0; burnhid = 0
    for i, j, k in itertools.permutations(range(N), 3):
        v0, h0, f = deck[i], deck[j], deck[k]; tot += 1
        v, h = h0, v0                    # swap 1
        one += (v == v0)
        # engine peek: look at v, replace h with f; swap 2 -> v = f
        ep += (f == v0)
        # literal rule 3 on the visible card: reveal v, burn it, replace v with f; swap2 -> v = h = v0
        burnvis += (h == v0)
        # literal rule 3 on the burn card: reveal h, burn it, replace h with f; swap2 -> v = f
        burnhid += (f == v0)
    print(N, 'one', F(one, tot), 'engine-peek', F(ep, tot), 'reveal+burn visible', F(burnvis, tot), 'reveal+burn hidden', F(burnhid, tot))
# Euchre line game
M = [(-v if s in (1, 2) else v) for v in range(1, 7) for s in range(4)]
from collections import Counter
bl = Counter(2*M[i] + 2*M[j] for i, j in itertools.permutations(range(24), 2))
pk = Counter(M[i]+M[j]+M[k]+M[l] for i, j, k, l in itertools.permutations(range(24), 4))
T = sum(pk.values()); odd = sum(c for d, c in pk.items() if d % 2)
print('blind total', sum(bl.values()), 'odd blind', sum(c for d, c in bl.items() if d % 2))
print('peek total', T, 'odd mass', F(odd, T), 'odd positions filled', sum(1 for d in range(-23, 24, 2) if pk[d]), 'of', len(range(-23, 24, 2)), 'max |d|', max(abs(d) for d in pk))
