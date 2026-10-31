# As neg_parent2.py, but each outcome is "balanced": sum_k p_ok = sum_k q_ok = P_o, so every exact
# block has trace P_o * Tr(rho) > 0 and nothing is clipped for the exact instrument. This is the
# configuration in which the normalization factor s/Q exceeds 1.
from fractions import Fraction as F
import random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from neg_parent import rnd, rnd_sqrt

def split(total, r):
    ws = [random.randint(1, 10**6) for _ in range(r)]
    return [total * F(w, sum(ws)) for w in ws]

def trial(b, nO, r):
    d = 2; R = nO * r
    eta = F(48 * R * d**4, 2**b)
    Ps = split(F(1), nO)
    p, q = [], []
    for P in Ps: p += split(P, r); q += split(P, r)
    ah = [rnd_sqrt(x, b) for x in p]; ch = [rnd_sqrt(x, b) for x in q]
    out = []
    for m in range(1, 200):
        s = F(m, 2**b); r00, r11 = F(1, 2) + s, F(-1, 2)
        bh, be = [], []
        for o in range(nO):
            c00 = c11 = e00 = e11 = F(0)
            for k in range(o * r, (o + 1) * r):
                c00 = rnd(c00 + rnd(rnd(ah[k] * r00, b) * ah[k], b), b)
                c11 = rnd(c11 + rnd(rnd(ch[k] * r11, b) * ch[k], b), b)
                e00 += p[k] * r00; e11 += q[k] * r11
            bh.append((c00, c11)); be.append((e00, e11))
        cl = [(c if c[0] + c[1] > 0 else (F(0), F(0))) for c in bh]
        Q = sum(c[0] + c[1] for c in cl)
        if Q <= 0: continue
        k = s / Q
        err = sum(abs(k * c[0] - e[0]) + abs(k * c[1] - e[1]) for c, e in zip(cl, be))
        E = sum(abs(c[0] - e[0]) + abs(c[1] - e[1]) for c, e in zip(bh, be))
        claimed = 4 * eta * s + 8 * F(1, 2)
        out.append((err / claimed, m, Q * 2**b, k, err, claimed, E, eta * (1 + s)))
    return max(out) if out else None

if __name__ == "__main__":
    for (b, nO, r, T) in ((16, 1, 4, 300), (16, 2, 4, 300), (16, 3, 4, 300), (16, 4, 4, 200)):
        random.seed(1000 + 10 * nO + b)
        best = max(x for x in (trial(b, nO, r) for _ in range(T)) if x)
        ratio, m, Qn, k, err, claimed, E, etaN = best
        print(f"b={b} |O|={nO} r={r} (R={nO*r} <= |O| d^2): Tr rho={m}*2^-b, Q={Qn}*2^-b, s/Q={k}; "
              f"E={float(E):.2e} <= eta||rho||={float(etaN):.2e}: {E <= etaN}; "
              f"||K~-I||_1={float(err):.4f} vs 4 eta s + 8 nu={float(claimed):.4f}: EXCEEDED={err > claimed}")
