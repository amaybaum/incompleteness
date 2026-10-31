"""Rigorous (interval) conditional mutual information and the Pinsker readback bound.

Joint laws are dicts (a, c, b) -> Fraction.  All decisions use mpmath.iv
(outward-rounded interval arithmetic) against exact rational bounds; no plain
float enters a decision.  Comparison is done in nats: the claim
    I_bits >= p0 delta^2 / ln 2      is equivalent to      I_nats >= p0 delta^2,
so the bound side is an exact rational.
"""
from fractions import Fraction as F
from mpmath import iv

iv.prec = 80
_logcache = {}


def ivq(q):
    q = F(q)
    return iv.mpf(q.numerator) / iv.mpf(q.denominator)


def ivlog(q):
    q = F(q)
    key = (q.numerator, q.denominator)
    r = _logcache.get(key)
    if r is None:
        r = iv.log(ivq(q))
        _logcache[key] = r
    return r


def marginals(tab):
    pc, pac, pcb = {}, {}, {}
    for (a, c, b), p in tab.items():
        if not p:
            continue
        pc[c] = pc.get(c, F(0)) + p
        pac[(a, c)] = pac.get((a, c), F(0)) + p
        pcb[(c, b)] = pcb.get((c, b), F(0)) + p
    return pc, pac, pcb


def cmi_nats(tab):
    """Formula 1: sum p ln( p p(c) / (p(a,c) p(c,b)) )."""
    pc, pac, pcb = marginals(tab)
    s = iv.mpf(0)
    for (a, c, b), p in tab.items():
        if p:
            s += ivq(p) * ivlog(p * pc[c] / (pac[(a, c)] * pcb[(c, b)]))
    return s


def _H(masses):
    s = iv.mpf(0)
    for p in masses:
        if p:
            s -= ivq(p) * ivlog(p)
    return s


def cmi_nats_entropy(tab):
    """Formula 2 (independent control): H(AC)+H(CB)-H(C)-H(ACB)."""
    pc, pac, pcb = marginals(tab)
    return _H(pac.values()) + _H(pcb.values()) - _H(pc.values()) - _H(tab.values())


def cond_entropy_B_given_C_nats(tab):
    pc, pac, pcb = marginals(tab)
    return _H(pcb.values()) - _H(pc.values())


def laws(tab):
    """(a,c) -> (joint mass P(a,c), next-step law dict)."""
    m = {}
    for (a, c, b), p in tab.items():
        if p:
            m.setdefault((a, c), {})
            m[(a, c)][b] = m[(a, c)].get(b, F(0)) + p
    out = {}
    for key, d in m.items():
        w = sum(d.values())
        out[key] = (w, {b: v / w for b, v in d.items()})
    return out


def tv(P, Q):
    sup = set(P) | set(Q)
    return sum(abs(P.get(b, F(0)) - Q.get(b, F(0))) for b in sup) / 2


def hypothesis_pairs(tab):
    """All admissible (p0, delta, extra) for pairs of distinct pasts at a common present.
    p0 = min of the two JOINT probabilities (the largest admissible p0), delta = exact TV."""
    L = laws(tab)
    pc, _, _ = marginals(tab)
    keys = sorted(L, key=repr)
    out = []
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            (a1, c1), (a2, c2) = keys[i], keys[j]
            if c1 != c2:
                continue
            w1, P1 = L[keys[i]]
            w2, P2 = L[keys[j]]
            out.append(dict(c=c1, w1=w1, w2=w2, pc=pc[c1], p0=min(w1, w2), delta=tv(P1, P2)))
    return out


def decide(I, bound):
    """I: iv interval (nats); bound: Fraction (nats). Returns 'holds'/'VIOLATION'/'tie0'/'undecided'."""
    B = ivq(bound)
    if bound == 0:
        return 'tie0' if I.b >= 0 else 'VIOLATION'
    if I.a > B.b:
        return 'holds'
    if I.b < B.a:
        return 'VIOLATION'
    return 'undecided'


def compositions(n, k):
    """All k-tuples of nonnegative ints summing to n."""
    if k == 1:
        yield (n,)
        return
    for i in range(n + 1):
        for rest in compositions(n - i, k - 1):
            yield (i,) + rest
