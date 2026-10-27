"""Named exact examples for the recurrence/readback review.  Imports only the probe's helpers."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from recur_probe import (order, rooted, is_perm, overlap_pairs, inverse,
                         has_stochastic_right_inverse, c4_gap, path_law)

def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]

def stoch(M):
    return all(v >= 0 for r in M for v in r) and all(sum(r) == 1 for r in M)

def show(name, phi, nV, nH, mu, pV):
    L = order(phi)
    G = [rooted(phi, nV, nH, mu, t) for t in range(L + 1)]
    print(f"== {name}: order L={L}")
    for t, g in enumerate(G):
        print(f"   Gamma_{t} =", [[str(v) for v in r] for r in g], "perm" if is_perm(g) else "NONPERM")
    c4 = [(k, c4_gap(phi, nV, nH, mu, pV, k)) for k in range(1, L + 1)]
    c4 = [(k, w) for k, w in c4 if w]
    print("   C4 gap orders <= L:", [k for k, _ in c4], " first witness:", c4[0] if c4 else None)
    for s in range(1, L):
        if not is_perm(G[s]):
            print(f"   pair (s={s}, L={L}): stochastic right inverse exists? {has_stochastic_right_inverse(G[s])}",
                  " overlaps:", overlap_pairs(G[s]))
            break
    return L, G

def enc(x, h, nH):
    return x * nH + h

# 1. Main 2.4 minimal model: x in {0,1}, h in {1..6} (indexed 0..5)
nV, nH = 2, 6
phi = list(range(12))
def swap(a, b):
    phi[a], phi[b] = b, a
for (p, q) in [((0, 1), (1, 1)), ((0, 2), (1, 2)), ((0, 3), (0, 4)), ((0, 5), (0, 6)),
               ((1, 3), (1, 4)), ((1, 5), (1, 6))]:
    swap(enc(p[0], p[1] - 1, nH), enc(q[0], q[1] - 1, nH))
show("Main 2.4 six-hidden model", phi, nV, nH, [F(1, 6)] * 6, [F(1, 2)] * 2)
law = path_law(phi, nV, nH, [F(1, 6)] * 6, [F(1, 2)] * 2, 2)
p_110 = sum(v for k, v in law.items() if k[:2] == (0, 1))
p_0_110 = sum(v for k, v in law.items() if k == (0, 1, 0))
p_x1 = sum(v for k, v in law.items() if k[1] == 1)
p_0_x1 = sum(v for k, v in law.items() if k[1] == 1 and k[2] == 0)
print("   control (Main 2.4 text): P(x2=0|x1=1,x0=0) =", p_0_110 / p_110, " P(x2=0|x1=1) =", p_0_x1 / p_x1)

# 2. Short-window control: phi(x,u) = (u, x xor u), order 3, uniform u.
nV, nH = 2, 2
phi = [0] * 4
for x in range(2):
    for u in range(2):
        phi[enc(x, u, nH)] = enc(u, x ^ u, nH)
L, G = show("short-window XOR control phi(x,u)=(u,x^u)", phi, nV, nH, [F(1, 2)] * 2, [F(1, 2)] * 2)
J = [[F(1, 2)] * 2] * 2
I = [[F(1), F(0)], [F(0), F(1)]]
wit = {(0, 1): J, (0, 2): J, (1, 2): I}
ok = all(stoch(Lm) and matmul(G[s], Lm) == G[t] for (s, t), Lm in wit.items())
print("   P-divisible on {0,1,2} by exhibited stochastic witnesses:", ok)
print("   C4 at order 1 lies inside {0,1,2}:", bool(c4_gap(phi, nV, nH, [F(1, 2)] * 2, [F(1, 2)] * 2, 1)))

# 3. Zero-probability root: visible prior delta_0. Same phi as 2.
pV = [F(1), F(0)]
print("== single supported root (pV = delta_0), phi as in 2")
gaps = [k for k in range(1, L + 1) if c4_gap(phi, nV, nH, [F(1, 2)] * 2, pV, k)]
print("   C4 gap orders with pV=delta_0:", gaps, " witness:", c4_gap(phi, nV, nH, [F(1, 2)] * 2, pV, gaps[0]) if gaps else None)
# restricted family: row 0 only; Lambda_{s,t} = all rows equal to row_t is stochastic, gives row_s Lambda = row_t
rows = [[G[t][0]] for t in range(L + 1)]
okR = True
for s in range(L + 1):
    for t in range(s + 1, L + 1):
        Lm = [list(G[t][0]) for _ in range(nV)]
        okR &= stoch(Lm) and matmul(rows[s], Lm) == rows[t]
print("   restricted (supported-root rows only) family P-divisible on {0..L}:", okR)
print("   full-row family: pair (1,L) has stochastic right inverse?", has_stochastic_right_inverse(G[1]),
      "; overlap at s=1 uses rows", overlap_pairs(G[1]), "(row 1 has visible prior 0)")

# 4. Negative control: decoupled phi(x,h) = (1-x, h+x mod 2): all Gamma perm, no C4.
phi = [0] * 4
for x in range(2):
    for h in range(2):
        phi[enc(x, h, 2)] = enc(1 - x, (h + x) % 2, 2)
show("decoupled negative control", phi, 2, 2, [F(1, 2)] * 2, [F(1, 2)] * 2)

# 5. Hidden influence without readback: phi(v,(h,m)) writes nothing back: coin x' = h_t from a tape
#    that rotates; ledger absent.  V={0,1}, H = tape of 2 bits rotating: (x,(a,b)) -> (a,(b,x)).
nV, nH = 2, 4
phi = [0] * 8
for x in range(2):
    for a in range(2):
        for b in range(2):
            phi[enc(x, 2 * a + b, nH)] = enc(a, 2 * b + x, nH)
show("tape shift (x,(a,b))->(a,(b,x)), uniform tape", phi, nV, nH, [F(1, 4)] * 4, [F(1, 2)] * 2)

# 6. Lemma countercontrols: non-square stochastic pair with AB = I; square with nonneg non-stochastic inverse
A = [[F(1, 2), F(1, 2)]]; B = [[F(1)], [F(1)]]
print("== Lemma scope: 1x2 A=[1/2,1/2], 2x1 B=[1;1] stochastic, AB =", matmul(A, B), "(non-square: lemma needs square)")
M = [[F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]]
print("   inverse of [[2/3,1/3],[1/3,2/3]] =", [[str(v) for v in r] for r in inverse(M)], "(Main 2.4 Lambda(2,1))")
