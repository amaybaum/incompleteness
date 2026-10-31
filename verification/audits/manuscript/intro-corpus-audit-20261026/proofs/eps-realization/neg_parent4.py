# Single-outcome (outcome-free) channel in dimension d with R <= d^2 diagonal Kraus operators
# M_k = diag(sqrt(p_{k,1}), ..., sqrt(p_{k,d})), sum_k p_{k,i} = 1 for every i (trace preserving).
# Hermitian dyadic register rho = diag(1/2 + s, -1/(2(d-1)), ..., -1/(2(d-1))): trace s,
# negativity nu = 1/2, ||rho||_1 = 1 + s (inside the window [1/2, 4]).
# Exact output I(rho) = rho. Compare the clipped/normalized digitized kernel with I(rho).
from fractions import Fraction as F
import random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from neg_parent import rnd, rnd_sqrt

def search(d, R, b, trials, seed):
    random.seed(seed)
    eta = F(48 * R * d**4, 2**b)
    best = None
    for _ in range(trials):
        cols = []
        for i in range(d):
            ws = [random.randint(1, 10**7) for _ in range(R)]
            cols.append([F(w, sum(ws)) for w in ws])
        hat = [[rnd_sqrt(cols[i][k], b) for i in range(d)] for k in range(R)]
        for m in range(1, 60):
            s = F(m, 2**b)
            rho = [F(1, 2) + s] + [F(-1, 2 * (d - 1))] * (d - 1)
            C = [F(0)] * d
            for k in range(R):
                for i in range(d):
                    C[i] = rnd(C[i] + rnd(rnd(hat[k][i] * rho[i], b) * hat[k][i], b), b)
            Q = sum(C)
            if Q <= 0: continue
            kf = s / Q
            err = sum(abs(kf * C[i] - rho[i]) for i in range(d))
            E = sum(abs(C[i] - rho[i]) for i in range(d))
            claimed = 4 * eta * s + 8 * F(1, 2)
            rec = (err / claimed, m, Q * 2**b, kf, err, claimed, E, eta * (1 + s))
            if best is None or rec[0] > best[0]: best = rec
    return best

if __name__ == "__main__":
    for (d, R, b, T) in ((2, 4, 16, 3000), (3, 9, 16, 1500), (4, 16, 16, 600)):
        ratio, m, Qn, kf, err, claimed, E, etaN = search(d, R, b, T, seed=d * 100 + R)
        print(f"d={d} R={R} b={b}: Tr rho={m}*2^-b, Q={Qn}*2^-b, s/Q={kf}; raw drift E={float(E):.2e} "
              f"(<= eta||rho||_1={float(etaN):.2e}: {E <= etaN}); ||K~(rho)-I(rho)||_1={float(err):.4f} "
              f"vs claimed 4 eta s + 8 nu = {float(claimed):.4f}: EXCEEDED={err > claimed}")
