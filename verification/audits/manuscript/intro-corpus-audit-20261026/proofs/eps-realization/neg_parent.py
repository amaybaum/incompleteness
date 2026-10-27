# Exact-rational test of the Rounding Lemma's Hermitian-input step (Main.md:556).
# Fixed-point model as in the paper / opglue_probes.py check 14: b fractional bits,
# round-to-nearest-even per product and per addition, Kraus entries quantized to b bits.
# Instrument: ONE outcome (an outcome-free channel), R=4 diagonal Kraus operators
#   M_k = diag(sqrt(p_k), sqrt(q_k)),  sum p = sum q = 1  (exactly trace preserving).
# For diagonal input rho, the EXACT output is I(rho) = rho itself, so no irrational
# arithmetic is needed for the comparison; only the b-bit rounding of sqrt(p) is computed
# exactly (by comparing squares).
from fractions import Fraction as F
import random, sys

def rnd(x, b):                      # round-to-nearest-even at b fractional bits
    n = x * 2**b
    fl = n.numerator // n.denominator
    r = n - fl
    if r > F(1, 2) or (r == F(1, 2) and fl % 2 == 1): fl += 1
    return F(fl, 2**b)

def rnd_sqrt(p, b):                 # exact b-bit round-to-nearest of sqrt(p), p rational >= 0
    t = p * 4**b                    # want nearest integer to sqrt(t)
    k = 0
    lo, hi = 0, 1
    while F(hi * hi) <= t: hi *= 2
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if F(mid * mid) <= t: lo = mid
        else: hi = mid
    k = lo                          # floor(sqrt t)
    if F(2 * k + 1, 2) ** 2 < t: k += 1   # nearest (ties impossible for irrational; fine)
    return F(k, 2**b)

def digitized(ahat, chat, r00, r11, b):
    c00 = F(0); c11 = F(0)
    for a, c in zip(ahat, chat):
        c00 = rnd(c00 + rnd(rnd(a * r00, b) * a, b), b)
        c11 = rnd(c11 + rnd(rnd(c * r11, b) * c, b), b)
    return c00, c11

def run(b, seed, trials):
    random.seed(seed)
    d, R = 2, 4
    eta = F(48 * R * d**4, 2**b)
    best = None
    for _ in range(trials):
        ws = [random.randint(1, 10**6) for _ in range(R)]
        vs = [random.randint(1, 10**6) for _ in range(R)]
        p = [F(w, sum(ws)) for w in ws]; q = [F(v, sum(vs)) for v in vs]
        ahat = [rnd_sqrt(x, b) for x in p]; chat = [rnd_sqrt(x, b) for x in q]
        for m in range(1, 40):
            s = F(m, 2**b)
            r00, r11 = F(1, 2) + s, F(-1, 2)      # Hermitian dyadic register, ||.||_1 = 1+s (in window)
            c00, c11 = digitized(ahat, chat, r00, r11, b)
            Q = c00 + c11                          # digitized total trace
            if Q <= 0: continue                    # would be clipped -> fallback; skip
            nu_in = F(1, 2)
            N = 1 + s
            E = abs(c00 - r00) + abs(c11 - r11)   # raw drift, exact
            k = s / Q                              # normalization factor of the clipped/normalized kernel
            out00, out11 = k * c00, k * c11
            err = abs(out00 - r00) + abs(out11 - r11)   # || K~(rho) - I(rho) ||_1, exact
            nu_out = k * (-c11 if c11 < 0 else 0)
            claimed = 4 * eta * s + 8 * nu_in     # per-parent form of "4 eta s + 8 nu" (Main.md:556)
            rec = (err / claimed, m, s, Q, k, E, err, claimed, nu_out, nu_in + E, eta * N, p, q)
            if best is None or rec[0] > best[0]: best = rec
    return best

if __name__ == "__main__":
    for b in (12, 16, 20):
        best = run(b, seed=b, trials=400)
        ratio, m, s, Q, k, E, err, claimed, nu_out, nu_budget, etaN, p, q = best
        print(f"b={b}: s=Tr rho={m}*2^-b  Q=Tr C={Q*2**b}*2^-b  s/Q={k}")
        print(f"   raw drift E={float(E):.3e}  (Rounding-Lemma bound eta*||rho||_1={float(etaN):.3e}: holds={E <= etaN})")
        print(f"   normalized-kernel error ||K~(rho)-I(rho)||_1 = {float(err):.4f}")
        print(f"   claimed per-parent bound 4*eta*s + 8*nu = {float(claimed):.4f}   exceeded: {err > claimed}  (ratio {float(ratio):.3f})")
        print(f"   negativity out (s/Q)*||C_-||_1 = {float(nu_out):.4f}  vs nu_in + E = {float(nu_budget):.4f}: amplified={nu_out > nu_budget}")
        print(f"   p={[str(x) for x in p]}\n   q={[str(x) for x in q]}")
