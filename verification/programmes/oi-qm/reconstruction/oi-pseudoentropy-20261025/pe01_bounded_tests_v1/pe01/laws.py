"""Record laws by full enumeration through the bijection, and class U (PLAN.md §2, §3).

The record law at horizon K is the count multiset of X_{0:K} over the prior's seeds. Prefix classes
are tracked incrementally: label_{K+1} = class of (label_K, X_{K+1}). All arithmetic is in Python
ints and Fractions; numpy only on integer arrays.
"""
from fractions import Fraction

import numpy as np


def prefix_labels(X, kcap):
    """labels[K] = int64 array of prefix-class ids of X[:, 0:K+1], ids in first-appearance order."""
    rows = X.shape[0]
    out = []
    lab = np.zeros(rows, dtype=np.int64)
    for K in range(kcap + 1):
        key = lab * 2 + X[:, K].astype(np.int64)
        _, inv = np.unique(key, return_inverse=True)
        lab = inv.astype(np.int64).reshape(-1)
        out.append(lab)
    return out


class Law:
    """Record law of one generator, at every K <= kcap."""

    def __init__(self, gen, kcap):
        self.gen = gen
        self.kcap = kcap
        self.X = gen.records(kcap)
        self.w = gen.seed_w
        self.M = gen.M
        self.labels = prefix_labels(self.X, kcap)

    def counts(self, K):
        return _wcount(self.labels[K], self.w)

    def support(self, K):
        return int(self.labels[K].max()) + 1

    def max_prob(self, K):
        c = self.counts(K)
        return Fraction(int(c.max()), self.M)


def _wcount(lab, w):
    n = int(lab.max()) + 1
    out = np.zeros(n, dtype=np.int64)
    np.add.at(out, lab, w)
    return out


def tv_uniform_from_counts(c, M, N):
    """TV(P, uniform on {0,1}^N) for a law given by integer counts c (total M) on its support."""
    twoN = 1 << N
    s = len(c)
    num = sum(abs(int(ci) * twoN - M) for ci in c.tolist()) + (twoN - s) * M
    return Fraction(num, 2 * M * twoN)


def u_k1_curve(law):
    """U at K1: exact TV against Q, and the exact K1 Bayes next-symbol predictor advantage."""
    tv, bayes = {}, {}
    for K in range(law.kcap + 1):
        c = law.counts(K)
        tv[K] = tv_uniform_from_counts(c, law.M, K + 1)
        if K == 0:
            c0 = int(law.w[law.X[:, 0] == 0].sum())
            bayes[K] = Fraction(max(c0, law.M - c0), law.M) - Fraction(1, 2)
        else:
            pre = law.labels[K - 1]
            nxt = law.X[:, K].astype(np.int64)
            n = int(pre.max()) + 1
            tab = np.zeros((n, 2), dtype=np.int64)
            np.add.at(tab, (pre, nxt), law.w)
            bayes[K] = Fraction(int(tab.max(axis=1).sum()), law.M) - Fraction(1, 2)
    return tv, bayes


def complement_invariant(gen, kcap):
    """SY: the record law is complement-invariant at every K <= kcap (c(r) = c(r-bar) on the support)."""
    X = gen.records(kcap)
    S = X.shape[0]
    XX = np.concatenate([X, 1 - X], axis=0)
    labs = prefix_labels(XX, kcap)
    w = gen.seed_w
    bad = []
    for K in range(kcap + 1):
        lab = labs[K]
        n = int(lab.max()) + 1
        cnt = np.zeros(n, dtype=np.int64)
        np.add.at(cnt, lab[:S], w)
        if not np.array_equal(cnt[lab[:S]], cnt[lab[S:]]):
            bad.append(K)
    return {"pass": not bad, "K_cap": kcap, "failing_K": bad[:10]}


def u_k0(laws, tvs):
    """U K0 intervals (PLAN.md §3): worst [1 - |union| 2^-N, min TV], average [TV(mix, Q), mean TV]."""
    F = len(laws)
    M = laws[0].M
    kcap = min(l.kcap for l in laws)
    worst, avg = {}, {}
    # incremental stacked labelling
    X = np.concatenate([l.X for l in laws], axis=0)
    w = np.concatenate([l.w for l in laws])
    lab = np.zeros(X.shape[0], dtype=np.int64)
    for K in range(kcap + 1):
        _, inv = np.unique(lab * 2 + X[:, K].astype(np.int64), return_inverse=True)
        lab = inv.reshape(-1).astype(np.int64)
        n = int(lab.max()) + 1
        cnt = np.zeros(n, dtype=np.int64)
        np.add.at(cnt, lab, w)
        N = K + 1
        # the explicit test D_union: its exact advantage on each phi, from phi's own counts
        per = []
        off = 0
        for i, l in enumerate(laws):
            inU = np.zeros(n, dtype=bool)
            inU[lab[off:off + len(l.w)]] = True
            pP = Fraction(int(l.w[inU[lab[off:off + len(l.w)]]].sum()), l.M)
            per.append(abs(pP - Fraction(n, 1 << N)))
            off += len(l.w)
        lo = min(per)
        hi = min(tvs[i][K] for i in range(F))
        worst[K] = (lo, hi, per)
        mix = tv_uniform_from_counts(cnt, F * M, N)
        mean = sum(tvs[i][K] for i in range(F)) / F
        avg[K] = (mix, mean, None)
    return worst, avg
