# Extension of neg_parent.py: an instrument with |O| outcomes, r diagonal Kraus per outcome
# (r <= d^2 = 4, i.e. within the minimal-Kraus count the paper assumes, R = |O| r <= |O| d^2).
# Exact output blocks B_o = diag(P_o rho00, Q_o rho11) are rational. Everything exact.
from fractions import Fraction as F
import random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from neg_parent import rnd, rnd_sqrt

def run(b, nO, r, trials, seed):
    random.seed(seed)
    d = 2; R = nO * r
    eta = F(48 * R * d**4, 2**b)
    best = None
    for _ in range(trials):
        ws = [random.randint(1, 10**6) for _ in range(R)]; vs = [random.randint(1, 10**6) for _ in range(R)]
        p = [F(w, sum(ws)) for w in ws]; q = [F(v, sum(vs)) for v in vs]
        ah = [rnd_sqrt(x, b) for x in p]; ch = [rnd_sqrt(x, b) for x in q]
        for m in range(1, 80):
            s = F(m, 2**b); r00, r11 = F(1, 2) + s, F(-1, 2)
            blocks_hat, blocks_ex = [], []
            for o in range(nO):
                c00 = F(0); c11 = F(0); e00 = F(0); e11 = F(0)
                for k in range(o * r, (o + 1) * r):
                    c00 = rnd(c00 + rnd(rnd(ah[k] * r00, b) * ah[k], b), b)
                    c11 = rnd(c11 + rnd(rnd(ch[k] * r11, b) * ch[k], b), b)
                    e00 += p[k] * r00; e11 += q[k] * r11
                blocks_hat.append((c00, c11)); blocks_ex.append((e00, e11))
            clipped = [(c if c[0] + c[1] > 0 else (F(0), F(0))) for c in blocks_hat]
            Q = sum(c[0] + c[1] for c in clipped)
            if Q <= 0: continue
            sx = sum(e[0] + e[1] for e in blocks_ex)
            assert sx == s
            k = s / Q
            err = sum(abs(k * c[0] - e[0]) + abs(k * c[1] - e[1]) for c, e in zip(clipped, blocks_ex))
            E = sum(abs(c[0] - e[0]) + abs(c[1] - e[1]) for c, e in zip(blocks_hat, blocks_ex))
            N = 1 + s; nu = F(1, 2)
            claimed = 4 * eta * s + 8 * nu
            nu_out = k * sum((-c[0] if c[0] < 0 else 0) + (-c[1] if c[1] < 0 else 0) for c in clipped)
            rec = (err / claimed, m, Q * 2**b, k, err, claimed, E, eta * N, nu_out)
            if best is None or rec[0] > best[0]: best = rec
    return best

if __name__ == "__main__":
    for (b, nO, r) in ((16, 2, 4), (16, 3, 4), (20, 3, 4)):
        ratio, m, Qn, k, err, claimed, E, etaN, nu_out = run(b, nO, r, 300, seed=7 * b + nO)
        print(f"b={b} |O|={nO} r={r} (R={nO*r}): Tr rho = {m}*2^-b, Q = {Qn}*2^-b, s/Q = {k}")
        print(f"   E = {float(E):.3e} <= eta||rho||_1 = {float(etaN):.3e}: {E <= etaN}")
        print(f"   ||K~(rho) - I(rho)||_1 = {float(err):.4f}  vs claimed 4 eta s + 8 nu = {float(claimed):.4f}:  EXCEEDED = {err > claimed}")
        print(f"   output negativity = {float(nu_out):.4f}  (input negativity 0.5)")
