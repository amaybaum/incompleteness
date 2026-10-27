#!/usr/bin/env python3
"""Side check for book ch18 :187 ("for a generic permutation ... order bounded by lcm(1..|S|) (Landau's
function), which grows as approximately e^{|S|}").  Exact: Landau g(n) = max order of a permutation of n
points, by DP over prime powers; compare ln g(n) with ln lcm(1..n) and with sqrt(n ln n).
Control: g(n) for n<=12 against brute force over integer partitions (OEIS A000793 values)."""
import math
from functools import reduce

def primes(n):
    s = [True] * (n + 1); s[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i*i::i] = [False] * len(s[i*i::i])
    return [i for i in range(n + 1) if s[i]]

def landau(n):
    best = [1] * (n + 1)              # best[k] = max product of prime powers with sum <= k (distinct primes)
    for p in primes(n):
        new = best[:]
        pk = p
        while pk <= n:
            for k in range(pk, n + 1):
                new[k] = max(new[k], best[k - pk] * pk)
            pk *= p
        best = new
    return best[n]

def partitions(n, m=None):
    if m is None: m = n
    if n == 0: yield []; return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k): yield [k] + r

def brute(n):
    return max(reduce(lambda a, b: a * b // math.gcd(a, b), p, 1) for p in partitions(n))

ctrl = all(landau(n) == brute(n) for n in range(1, 13))
print(f"control: DP Landau g(n) == brute force over partitions for n<=12: {ctrl}")
for n in (10, 50, 100, 500, 1000, 3000):
    g = landau(n); l = reduce(lambda a, b: a * b // math.gcd(a, b), range(1, n + 1), 1)
    print(f"n={n:5d}: ln g(n) = {math.log(g):9.2f}   sqrt(n ln n) = {math.sqrt(n*math.log(n)):9.2f}   "
          f"ln lcm(1..n) = {math.log(l):9.2f}   n = {n}")
