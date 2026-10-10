def Q(v, u):
    out = []
    for (i, j) in PAIRS:
        re = 0; im = 0; ci = i * 16; cj = j * 16
        for k, (a, b) in enumerate(C_SIG[(i, j)]):
            p = (v[ci + k] - v[cj + k]) * (u[ci + k] - u[cj + k])
            if p: re += a * p; im += b * p
        out.append(re); out.append(im)
    return out
z240 = [0] * 240
IN_KER = {}
def in_ker_df(v):
    """v in ker DF, exact; memoized on the vector, since the hulls share most of their tangent vectors"""
    t = tuple(v)
    if t not in IN_KER:
        nz = [i for i, x in enumerate(v) if x]
        IN_KER[t] = all(sum(r[i] * v[i] for i in nz) == 0 for r in DF)
    return IN_KER[t]
Q_ZERO = {}
def q_zero(u, v):
    """Q(u, v) == 0, exact; Q is symmetric, so memoized on the unordered pair"""
    a, b = tuple(u), tuple(v)
    k = (a, b) if a <= b else (b, a)
    if k not in Q_ZERO: Q_ZERO[k] = Q(u, v) == z240
    return Q_ZERO[k]
