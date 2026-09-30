"""R3: the exact class support of an integer n x n exponent matrix, with no floating point.

Class support = min over (alpha, beta) of #{(i, j) : E_ij + alpha_i + beta_j != 0}, since act 36's stabilizer acts by
signed position permutations of product form (a row permutation and a column permutation, possibly with the
transpose), which map the gauge subspace onto itself and preserve support, and the sign preserves support too.
Equivalently n^2 minus the maximum number Z* of zeros.

Method. A lower bound Zb on Z* comes from an exhibited (alpha, beta) (local search). To prove Z* = Zb, suppose some
(alpha, beta) had Zb + 1 zeros. Then some row i* has k = ceil((Zb + 1) / n) zeros; fix a k-subset K of them and
normalize alpha_{i*} = 0 (gauge), so beta_K = -E_{i*,K}. The remaining columns F (|F| = n - k <= 2 is required) take
values beta_F, and for fixed beta the best alpha gives Z(beta) = sum_i max_v #{j : -E_ij - beta_j = v}. Z depends on
beta_F only through which of the values x_ij = -E_ij - beta_j (j in F) equal a value w in W = {-E_ij - beta_j : j in K}
and whether x_{i j1} = x_{i j2}; the enumeration below takes one beta_F from every such class (the values hitting W,
the values aligning the two free columns, and far values). If no enumerated beta reaches Zb + 1, then Z* = Zb.
Requires Zb + 1 > n (n - 3), so that |F| <= 2.
"""
import itertools, math, random
import numpy as np

def zeros_given_beta(E, beta):
    X = -E - beta[None, :]
    Xs = np.sort(X, axis=1)
    tot = 0
    for r in Xs:
        best = run = 1
        for t in range(1, len(r)):
            run = run + 1 if r[t] == r[t - 1] else 1
            if run > best: best = run
        tot += best
    return tot

def best_alpha(E, beta):
    X = -E - beta[None, :]
    al = []
    for r in X:
        vals, cnt = np.unique(r, return_counts=True); al.append(int(vals[np.argmax(cnt)]))
    return np.array(al)

def local_search(E, starts=64, seed=0):
    n = E.shape[0]; rng = random.Random(seed); best = (-1, None, None)
    inits = [np.zeros(n, dtype=np.int64)] + [np.array([rng.randint(-2, 2) for _ in range(n)]) for _ in range(starts)]
    for beta in inits:
        prev = -1
        for _ in range(50):
            al = best_alpha(E, beta)
            beta = best_alpha(E.T, al)
            z = int(np.sum(E + al[:, None] + beta[None, :] == 0))
            if z <= prev: break
            prev = z
        if prev > best[0]: best = (prev, best_alpha(E, beta), beta.copy())
    return best

def exact_max_zeros(E, Zb):
    """None if no (alpha, beta) has Zb + 1 zeros, else a beta reaching at least Zb + 1"""
    n = E.shape[0]; target = Zb + 1; k = math.ceil(target / n)
    assert n - k <= 2, 'the enumeration needs |F| <= 2'
    FAR = 10 ** 6
    for i in range(n):
        for K in itertools.combinations(range(n), k):
            F = [j for j in range(n) if j not in K]
            beta = np.zeros(n, dtype=np.int64)
            for j in K: beta[j] = -E[i, j]
            W = set(int(-E[r, j] - beta[j]) for r in range(n) for j in K)
            Bset = {j: sorted(set(int(-E[r, j] - w) for r in range(n) for w in W)) for j in F}
            if len(F) == 0: cands = [()]
            elif len(F) == 1: cands = [(b,) for b in Bset[F[0]] + [FAR]]
            else:
                j1, j2 = F; cands = []
                for b1 in Bset[j1] + [FAR]:
                    c2 = set(Bset[j2]) | set(b1 + int(E[r, j1] - E[r, j2]) for r in range(n)) | {b1 + 7 * FAR}
                    cands += [(b1, b2) for b2 in sorted(c2)]
            for vals in cands:
                for j, v in zip(F, vals): beta[j] = v
                if zeros_given_beta(E, beta) >= target: return beta.copy()
    return None

def class_support(E):
    """(support, alpha, beta, rounds): exact, with a representative E + alpha 1^T + 1 beta^T attaining it"""
    E = np.array(E, dtype=np.int64); n = E.shape[0]
    Zb, al, be = local_search(E)
    if Zb + 1 <= n * (n - 3): raise ValueError('outside the method: Zb + 1 <= n (n - 3)')
    rounds = 0
    while True:
        rounds += 1
        b = exact_max_zeros(E, Zb)
        if b is None: break
        al = best_alpha(E, b); be = b; Zb = int(np.sum(E + al[:, None] + be[None, :] == 0))
    rep = E + al[:, None] + be[None, :]
    assert int(np.sum(rep != 0)) == n * n - Zb
    return n * n - Zb, al.tolist(), be.tolist(), rounds

def brute(E, R):
    """control: the best over beta in [-R, R]^(n-1), beta_0 = 0, alpha optimal (a lower bound on Z*)"""
    E = np.array(E, dtype=np.int64); n = E.shape[0]; best = -1
    for tail in itertools.product(range(-R, R + 1), repeat=n - 1):
        beta = np.array((0,) + tail, dtype=np.int64)
        z = zeros_given_beta(E, beta)
        if z > best: best = z
    return n * n - best

if __name__ == '__main__':
    import json, sys, time
    t0 = time.time(); rng = random.Random(7); agree = 0; tried = 0; rows = []
    while tried < 150:
        n = 6; s = rng.randint(3, 16)
        E = np.zeros((n, n), dtype=np.int64)
        for p in rng.sample(range(n * n), s): E[p // n, p % n] = rng.choice([-1, 1])
        E = E + np.array([rng.randint(-2, 2) for _ in range(n)])[:, None] + np.array([rng.randint(-2, 2) for _ in range(n)])[None, :]
        try: sup, al, be, _ = class_support(E)
        except ValueError: continue                            # outside the method's range
        tried += 1
        bf = brute(E, 4)
        agree += (bf == sup); rows.append((sup, bf))
    print('C6 random 6x6 instances: %d of %d agree with brute force over [-4, 4]^5 (%.0fs)' % (agree, tried, time.time() - t0))
    print('  disagreements:', [r for r in rows if r[0] != r[1]][:10])
