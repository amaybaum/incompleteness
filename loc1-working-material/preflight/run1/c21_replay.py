"""LOC-1 preflight: independent replay of the C21 search witnesses.  Shares no code with c21_engine.py or
c21_search.py; reads only the witness file they write.

  * every reported identification is re-checked as a product by a third method: the rank of the
    reshuffled matrix by fraction-free (Bareiss) elimination over the integers;
  * classes are keyed by the unordered pair {row partition, column partition} of Fin N that the
    identification induces (ordered pair when m != n), not by the engine's canonical form;
  * on every shape with N <= 9, ALL N! bijections are tested and the set of product classes is compared
    with the engine's list (completeness and no duplicates);
  * planted classes must appear in complete enumerations;
  * permutation matrices: admission is recomputed from the cycle type (lcm/gcd rule) and compared;
  * 4x4 instances reported as having no class get a seeded consistency sample (not a proof).
Run:  python3 -I c21_replay.py [WITNESS.json]   (default: c21_witness.json in this directory)
"""
import os
import sys
import json
import itertools
from math import gcd


def reshuffled(M, inv, m, n):
    """inv[g] = index sent to grid point g = a n + b.  Rows (a, a'), columns (b, b')."""
    return [[M[inv[a * n + b]][inv[a2 * n + b2]] for b in range(n) for b2 in range(n)]
            for a in range(m) for a2 in range(m)]


def bareiss_rank(A):
    A = [row[:] for row in A]
    rows, cols = len(A), len(A[0])
    r, prev = 0, 1
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(r + 1, rows):
            for j in range(c + 1, cols):
                A[i][j] = (A[i][j] * A[r][c] - A[i][c] * A[r][j]) // prev
            A[i][c] = 0
        prev = A[r][c]
        r += 1
        if r == rows or r >= 2:        # only rank <= 1 versus >= 2 is needed
            break
    return r


def is_product(M, inv, m, n):
    return bareiss_rank(reshuffled(M, inv, m, n)) <= 1


def inverse_of(sig):
    inv = [None] * len(sig)
    for i, g in enumerate(sig):
        inv[g] = i
    return inv


def class_key(sig, m, n):
    rows = frozenset(frozenset(i for i, g in enumerate(sig) if g // n == a) for a in range(m))
    cols = frozenset(frozenset(i for i, g in enumerate(sig) if g % n == b) for b in range(n))
    return frozenset((rows, cols)) if m == n else (rows, cols)


def perm_from_matrix(M):
    N = len(M)
    pi = [None] * N
    for j in range(N):
        nz = [i for i in range(N) if M[i][j] != 0]
        if len(nz) != 1 or M[nz[0]][j] != 1 or sum(1 for x in M[nz[0]] if x) != 1:
            return None
        pi[j] = nz[0]
    return pi


def ctype(pi):
    seen, out = set(), []
    for s in range(len(pi)):
        if s not in seen:
            L, x = 0, s
            while x not in seen:
                seen.add(x)
                x = pi[x]
                L += 1
            out.append(L)
    return tuple(sorted(out, reverse=True))


def parts(k, mx=None):
    mx = mx or k
    if k == 0:
        return [()]
    return [(p,) + r for p in range(min(k, mx), 0, -1) for r in parts(k - p, p)]


def admitted_types(m, n):
    out = set()
    for t1 in parts(m):
        for t2 in parts(n):
            c = []
            for k in t1:
                for l in t2:
                    c += [k * l // gcd(k, l)] * gcd(k, l)
            out.add(tuple(sorted(c, reverse=True)))
    return out


class LCG:
    def __init__(self, s):
        self.s = s % (1 << 63)

    def below(self, k):
        self.s = (self.s * 6364136223846793005 + 1442695040888963407) % (1 << 64)
        return (self.s >> 11) % k          # bias irrelevant: consistency sample only


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                               "c21_witness.json")
    with open(path) as fh:
        W = json.load(fh)
    fails = []
    stats = {"records": 0, "witnesses": 0, "bruteforce": 0, "planted": 0, "perm": 0, "sampled_none": 0, "truncated": 0}

    def fail(msg):
        fails.append(msg)
        print("REPLAY FAIL", msg)

    for rec in W:
        stats["records"] += 1
        m, n, mats, found = rec["m"], rec["n"], rec["mats"], rec["found"]
        N = m * n
        keys = []
        for sig in found:
            stats["witnesses"] += 1
            inv = inverse_of(sig)
            if not all(is_product(M, inv, m, n) for M in mats):
                fail("%s: reported identification is not a product" % rec["name"])
            keys.append(class_key(sig, m, n))
        if len(set(keys)) != len(keys):
            fail("%s: duplicate classes reported" % rec["name"])
        truncated = rec["found_total"] > len(found)
        if truncated:
            stats["truncated"] += 1
        if rec["planted"] is not None and rec["status"] == "ALL" and not truncated:
            stats["planted"] += 1
            if class_key(rec["planted"], m, n) not in set(keys):
                fail("%s: planted class missing from a complete enumeration" % rec["name"])
        if rec["status"] == "ALL" and N <= 9 and not truncated:
            stats["bruteforce"] += 1
            truth = set()
            for perm in itertools.permutations(range(N)):
                inv = list(perm)               # inv[g] = index at grid point g
                if all(is_product(M, inv, m, n) for M in mats):
                    truth.add(class_key(inverse_of(inv), m, n))
            if truth != set(keys):
                fail("%s: brute force finds %d classes, engine %d" % (rec["name"], len(truth), len(keys)))
        if len(mats) == 1:
            pi = perm_from_matrix(mats[0])
            if pi is not None and rec["status"] in ("FOUND", "NONE", "ALL"):
                stats["perm"] += 1
                adm = ctype(pi) in admitted_types(m, n)
                has = len(found) > 0
                if has != adm:                 # FOUND, or a complete search (NONE / ALL)
                    fail("%s: cycle type %s admitted=%s but engine found=%s"
                         % (rec["name"], ctype(pi), adm, has))
        if rec["status"] == "NONE" and N == 16:
            stats["sampled_none"] += 1
            rng = LCG(len(rec["name"]) * 7919 + 17)
            for _ in range(200):
                inv = list(range(N))
                for i in range(N - 1, 0, -1):
                    j = rng.below(i + 1)
                    inv[i], inv[j] = inv[j], inv[i]
                if all(is_product(M, inv, m, n) for M in mats):
                    fail("%s: engine reports no class but a sampled identification is a product" % rec["name"])
                    break
    print("REPLAY records %(records)d  witnesses re-verified %(witnesses)d  brute-forced shapes %(bruteforce)d  "
          "planted checks %(planted)d  permutation checks %(perm)d  no-class samples %(sampled_none)d  "
          "truncated witness lists %(truncated)d" % stats)
    print("REPLAY:", "AGREES" if not fails else "DISAGREES (%d)" % len(fails))


if __name__ == "__main__":
    main()
