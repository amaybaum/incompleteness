"""p6_r3rev_aw3 -- cheap gem-finding probe (sec. A.16/A.31) for AW-QX4-1 beyond two modes (no p1-p5 imports).
Random affine-symplectic maps with translations on m = 3 F_2 modes (products of random symplectic transvections),
read model of QX-4 A4.1 (Z read on the carrier records z, adds a fresh uniform kick to the carrier x).
Supplies: every mode half-known (one known linear functional, other slot uniform: SA-1(c)) or environment
(both unknown); a sharp-supply countercontrol. Exact correlators (affine functionals of uniform bits).
This is a finite random sample, not a proof: it can refute the 3-mode bound, it cannot establish it.
"""
import random, itertools

def transvection(v, d):
    # T(x) = x + omega(x, v) v ; omega pairs coordinates (2m, 2m+1)
    M = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
    # column j of T = e_j + omega(e_j, v) v ; omega(e_j, v) = v[j^1]
    for j in range(d):
        if v[j ^ 1]:
            for i in range(d): M[i][j] ^= v[i]
    return M
def mul(A, B):
    d = len(A)
    return [[sum(A[i][k] & B[k][j] for k in range(d)) & 1 for j in range(d)] for i in range(d)]

def corr(Mrows, t, prep, i, j, kickbit):
    d = len(Mrows)
    st = list(prep)
    def apply(st):
        out = []
        for r in range(d):
            m, c = 0, t[r]
            for k in Mrows[r]:
                m ^= st[k][0]; c ^= st[k][1]
            out.append((m, c))
        return out
    for _ in range(i - 1): st = apply(st)
    zi = st[0]
    st = [st[0], (st[1][0] ^ (1 << kickbit), st[1][1])] + st[2:]
    for _ in range(j - i): st = apply(st)
    zj = st[0]
    if zi[0] ^ zj[0]: return 0
    return 1 - 2 * (zi[1] ^ zj[1])

def mode_preps(ubit, kind):
    out = []
    if kind == 'half':
        for v in (0, 1):
            out += [((0, v), (1 << ubit, 0)), ((1 << ubit, 0), (0, v)), ((1 << ubit, 0), (1 << ubit, v))]
    elif kind == 'env':
        out.append(((1 << ubit, 0), (1 << (ubit + 1), 0)))
    elif kind == 'sharp':
        for v in (0, 1):
            for u in (0, 1): out.append(((0, v), (0, u)))
    return out

def main(m=3, samples=20000, seed=7):
    rng = random.Random(seed); d = 2 * m
    supplies = {
        'all half-known': [mode_preps(0, 'half'), mode_preps(2, 'half'), mode_preps(4, 'half')],
        'carrier half, others env': [mode_preps(0, 'half'), mode_preps(2, 'env'), mode_preps(4, 'env')],
        'carrier half, one sharp (countercontrol)': [mode_preps(0, 'half'), mode_preps(2, 'sharp'), mode_preps(4, 'half')],
    }
    best = {k: (-9, None) for k in supplies}
    for s in range(samples):
        M = [[1 if i == j else 0 for j in range(d)] for i in range(d)]
        for _ in range(rng.randint(1, 8)):
            v = [rng.randint(0, 1) for _ in range(d)]
            M = mul(transvection(v, d), M)
        rows = [[k for k in range(d) if M[r][k]] for r in range(d)]
        t = [rng.randint(0, 1) for _ in range(d)]
        for name, per_mode in supplies.items():
            for combo in itertools.product(*per_mode):
                prep = [x for mode in combo for x in mode]
                c12 = corr(rows, t, prep, 1, 2, 10); c23 = corr(rows, t, prep, 2, 3, 10); c13 = corr(rows, t, prep, 1, 3, 10)
                for s1, s2 in itertools.product((1, -1), repeat=2):
                    K = s1 * c12 + s2 * c23 - s1 * s2 * c13
                    if K > best[name][0]: best[name] = (K, (c12, c23, c13))
    for k, v in best.items(): print(f'm={m}, {samples} random symplectic maps, supplies {k}: max K3 = {v[0]} {v[1]}')
    return best

if __name__ == '__main__':
    b = main()
