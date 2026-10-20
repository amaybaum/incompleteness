"""K-10 (PREREG section 4.3 and section 5): under counting-type priors, membership of A_CHSH(n) (uniform mixtures of n
deterministic two-wing response pairs, no-signalling required) equals the set of no-signalling boxes with every entry
in (1/n)Z, and the eight-coordinate program equals the 256-count program. Exhaustive at n <= 3 locally; n = 4
(about 1.8e8 multisets) is for CI with owner approval (amendment A-2). Exact integer arithmetic (boxes as counts).
Run: python3 -I -B k10.py
"""
from itertools import combinations_with_replacement, product

SETTINGS = list(product((0, 1), repeat=2))
CELLS = [(a, b, q, r) for a, b in SETTINGS for q, r in product((0, 1), repeat=2)]


def pair_vectors():
    vecs = []
    for f in range(16):
        for g in range(16):
            v = [0] * 16
            for si, (a, b) in enumerate(SETTINGS):
                q = (f >> si) & 1
                r = (g >> si) & 1
                v[CELLS.index((a, b, q, r))] = 1
            vecs.append(tuple(v))
    return vecs


def nosig(c):
    def p(a, b, q, r):
        return c[CELLS.index((a, b, q, r))]
    for a in (0, 1):
        for q in (0, 1):
            if p(a, 0, q, 0) + p(a, 0, q, 1) != p(a, 1, q, 0) + p(a, 1, q, 1):
                return False
    for b in (0, 1):
        for r in (0, 1):
            if p(0, b, 0, r) + p(0, b, 1, r) != p(1, b, 0, r) + p(1, b, 1, r):
                return False
    return True


def by_mixtures(n, vecs):
    out = set()
    for combo in combinations_with_replacement(range(256), n):
        c = [0] * 16
        for i in combo:
            v = vecs[i]
            for t in range(16):
                c[t] += v[t]
        c = tuple(c)
        if nosig(c):
            out.add(c)
    return out


def by_coordinates(n):
    """eight free coordinates (in units of 1/n): pA(a) = P(q=0|a), pB(b) = P(r=0|b), j(a,b) = P(q=0,r=0|a,b)"""
    out = set()
    rng = range(n + 1)
    for pA0, pA1, pB0, pB1 in product(rng, repeat=4):
        pA = (pA0, pA1)
        pB = (pB0, pB1)
        for js in product(rng, repeat=4):
            c = [0] * 16
            ok = True
            for si, (a, b) in enumerate(SETTINGS):
                j = js[si]
                e = (j, pA[a] - j, pB[b] - j, n - pA[a] - pB[b] + j)
                if min(e) < 0:
                    ok = False
                    break
                for (q, r), val in zip(((0, 0), (0, 1), (1, 0), (1, 1)), e):
                    c[CELLS.index((a, b, q, r))] = val
            if ok:
                out.add(tuple(c))
    return out


def main():
    vecs = pair_vectors()
    allok = True
    for n in (1, 2, 3):
        m = by_mixtures(n, vecs)
        c = by_coordinates(n)
        eq = m == c
        allok &= eq
        print(f'n={n}: mixtures of n response pairs that are no-signalling: {len(m)}; no-signalling boxes with entries '
              f'in (1/n)Z by eight coordinates: {len(c)}; equal: {eq}')
    print(f'[{"PASS" if allok else "FAIL"}] K-10 (n <= 3): the two forms define the same set at n = 1, 2, 3, so every '
          f'objective has the same optimum over both; n = 4 pending (CI); written argument for all n in NODE.md')


if __name__ == '__main__':
    main()
