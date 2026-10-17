"""LOC-1 preflight, leg T at C21: a reproducible stratified sampler of identification classes
Fin 16 ~ Fin 4 x Fin 4 (mod S_4 x S_4 and the factor swap), and its cost.  SYNTHETIC targets only.

Stratum.  A class is the unordered pair {R, C} of orthogonal partitions of Fin 16 into four 4-blocks
(rows and columns of sigma).  Its stratum is k(sigma) = max over the eight blocks of R and C of
|block & {0,1,2,3}|, the most elements of the declared grid's first row kept together (k in 1..4).
k is a class function (S_4 x S_4 permutes blocks within R and within C; the swap exchanges R and C).
Population sizes are exact: k depends only on where 0..3 go, so (#placements in stratum) * 12! / 1152
classes lie in each stratum.

Sampling.  SplitMix64 from a fixed seed; Fisher-Yates bijections (uniform over bijections, hence over
classes, since every class has 1152 bijections); a draw is kept if its stratum quota is open and its
class is new (sampling without replacement), until each stratum holds QUOTA classes.
Run:  python3 -I c21_sampler.py [SAMPLES.json]   (default: c21_samples.json in this directory)
"""
import os
import sys
import json
import time
import hashlib
import itertools
from math import factorial

MASK = (1 << 64) - 1
SEED = 0x4C4F43312D535452          # "LOC1-STR"
QUOTA = 500                         # 4 strata x 500 = 2000
m = n = 4
N = 16
ROW0 = {0, 1, 2, 3}


class SM64:
    def __init__(self, seed):
        self.s = seed & MASK

    def next(self):
        self.s = (self.s + 0x9E3779B97F4A7C15) & MASK
        z = self.s
        z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK
        z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK
        return z ^ (z >> 31)

    def below(self, k):
        lim = (1 << 64) - ((1 << 64) % k)
        while True:
            x = self.next()
            if x < lim:
                return x % k


def stratum_of_points(pts):
    """pts: grid points (a, b) of the indices 0, 1, 2, 3."""
    rows, cols = {}, {}
    for a, b in pts:
        rows[a] = rows.get(a, 0) + 1
        cols[b] = cols.get(b, 0) + 1
    return max(max(rows.values()), max(cols.values()))


def canon(sig):
    """sig[i] = grid index; canonical class representative (RGS on both coordinates, rows <lex cols)."""
    def rgs(seq):
        lab, out = {}, []
        for x in seq:
            lab.setdefault(x, len(lab))
            out.append(lab[x])
        return out
    s1, s2 = rgs([g // n for g in sig]), rgs([g % n for g in sig])
    if s2 < s1:
        s1, s2 = s2, s1
    return tuple(a * n + b for a, b in zip(s1, s2))


def is_product(M, sig):
    """Exact PC on M^sig (integers): R[(a,a')][(b,b')] = M[i][j], sigma(i) = (a,b), sigma(j) = (a',b')."""
    R = [[0] * (n * n) for _ in range(m * m)]
    for i in range(N):
        a, b = divmod(sig[i], n)
        for j in range(N):
            a2, b2 = divmod(sig[j], n)
            R[a * m + a2][b * n + b2] = M[i][j]
    piv = next(((r, c) for r in range(m * m) for c in range(n * n) if R[r][c]), None)
    if piv is None:
        return True
    p, q = piv
    return all(R[p][q] * R[r][c] == R[r][q] * R[p][c] for r in range(m * m) for c in range(n * n))


def main():
    out = []
    # exact stratum populations
    cnt = {}
    for pl in itertools.permutations(range(N), 4):
        k = stratum_of_points([divmod(g, n) for g in pl])
        cnt[k] = cnt.get(k, 0) + 1
    total_classes = factorial(16) // (factorial(4) ** 2 * 2)
    pops = {}
    for k in sorted(cnt):
        b = cnt[k] * factorial(12)
        assert b % 1152 == 0
        pops[k] = b // 1152
    ok_pop = (sum(pops.values()) == total_classes and cnt.get(4) == 2 * 4 * 24 and cnt.get(1) == 16 * 9 * 4 * 1)
    out.append("ordered placements of 0..3 by stratum: %s (total %d)" % (sorted(cnt.items()), sum(cnt.values())))
    out.append("classes by stratum: %s  sum %d  (total classes %d)" % (sorted(pops.items()), sum(pops.values()),
                                                                       total_classes))
    out.append("CONTROL K-strata %s  (sums to 16!/1152; strata 4 and 1 match 2*4*4! and 16*9*4*1)"
               % ("PASS" if ok_pop else "FAIL"))
    # sampling
    t0 = time.perf_counter()
    rng = SM64(SEED)
    quota = {k: QUOTA for k in pops}
    seen, samples, draws, dups = set(), [], 0, 0
    per = {k: 0 for k in pops}
    while any(quota.values()):
        g = list(range(N))
        for i in range(N - 1, 0, -1):
            j = rng.below(i + 1)
            g[i], g[j] = g[j], g[i]
        sig = g                                    # sig[i] = grid point of index i
        draws += 1
        k = stratum_of_points([divmod(sig[i], n) for i in range(4)])
        per[k] += 1
        if not quota[k]:
            continue
        c = canon(sig)
        if c in seen:
            dups += 1
            continue
        seen.add(c)
        samples.append((k, c))
        quota[k] -= 1
    t1 = time.perf_counter()
    # controls on the sample
    ok_c = all(canon(list(c)) == c and sorted(c) == list(range(N)) for _, c in samples)
    ok_k = all(stratum_of_points([divmod(c[i], n) for i in range(4)]) == k for k, c in samples)
    out.append("draws %d to fill %d x %d; draws per stratum %s; duplicate classes rejected %d"
               % (draws, len(pops), QUOTA, sorted(per.items()), dups))
    out.append("CONTROL K-sample-canonical %s ; CONTROL K-sample-stratum %s ; distinct classes %d"
               % ("PASS" if ok_c else "FAIL", "PASS" if ok_k else "FAIL", len(set(c for _, c in samples))))
    blob = json.dumps([[k, list(c)] for k, c in samples], separators=(",", ":"))
    out.append("sample list sha256 %s" % hashlib.sha256(blob.encode()).hexdigest())
    spath = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                                "c21_samples.json")
    with open(spath, "w") as f:
        f.write(blob)
    # cost of classifying the sample on synthetic targets (two 16x16 integer matrices, jointly)
    r2 = SM64(0x434F5354)
    def rm(k, vals):
        return [[vals[r2.below(len(vals))] for _ in range(k)] for _ in range(k)]
    def kron(A, B):
        return [[A[a][a2] * B[b][b2] for a2 in range(4) for b2 in range(4)] for a in range(4) for b in range(4)]
    dense = [rm(16, list(range(-9, 10))), rm(16, list(range(-9, 10)))]
    prod = [kron(rm(4, [-2, -1, 1, 2]), rm(4, [-2, -1, 1, 2])), kron(rm(4, [-2, -1, 1, 2]), rm(4, [-2, -1, 1, 2]))]
    for nm, Ms in (("random dense pair", dense), ("declared-class product pair", prod)):
        t2 = time.perf_counter()
        hits = sum(1 for _, c in samples if all(is_product(M, c) for M in Ms))
        t3 = time.perf_counter()
        out.append("classified %d samples on %s: product classes among them %d" % (len(samples), nm, hits))
        print("TIMING classify %-28s %.3fs  %.1f us/sample" % (nm, t3 - t2, 1e6 * (t3 - t2) / len(samples)),
              file=sys.stderr)
    incl = {k: (QUOTA, pops[k]) for k in pops}
    out.append("power note: each class of stratum k enters the sample with probability %s; a target with r_k "
               "product classes in stratum k is hit with probability <= sum_k r_k * %d / pop_k"
               % (", ".join("k=%d: %d/%d" % (k, q, p) for k, (q, p) in sorted(incl.items())), QUOTA))
    for line in out:
        print(line)
    print("TIMING sampling_s %.3f  draws %d  us/draw %.1f" % (t1 - t0, draws, 1e6 * (t1 - t0) / draws),
          file=sys.stderr)


if __name__ == "__main__":
    main()
