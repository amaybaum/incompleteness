#!/usr/bin/env python3
"""Exact instance controls for the S1 realization family of RECURRENCE-SCALING-AUDIT.md.

The uniform statements are proved in RECURRENCE-SCALING-RESULT.md; the kernel carries the
family-level half in OIBridge/ScalingFamily.lean.  This probe is the independent instance check:
it rebuilds the declared realization from its definition, in exact rational arithmetic, and
verifies every frozen per-member obligation at a range of horizons.

Per the frozen preregistration a finite table of tight realizations is NOT an unbounded family.
Nothing here is offered as the uniform result; these are controls on the uniform proof.

The realization R_N, for N >= 4:

  V = {0,1}
  H = { (j, t, c) : j in 1..N-1, t in Z_N, c in {0,1} }
  orbit word            w_j(t) = 1 iff t = j  (mod N)
  phi (v,(j,t,c))       = ( w_j(t+1)      if v = w_j(t) else 1 - w_j(t+1),
                            (j, t+1, c XOR (v if t = 0 else 0)) )
  prior                 mu(j,0,0) = mu_j,  zero elsewhere
  mu_j                  = (2m + j) / sum,  m = N - 1

The ledger bit c is what makes the write clause W hold: it records the initial visible value, so
the hidden state after one step differs between the two roots under a common seed.  Without it the
hidden component would evolve independently of the visible root and the realization would be the
uncoupled product that PR #542 already recorded as parent-negative.
"""

from fractions import Fraction as Q
from math import gcd

PASS, FAIL = [], []


def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")


# ---------------------------------------------------------------- construction

def weights(N):
    m = N - 1
    raw = [Q(2 * m + i) for i in range(1, m + 1)]
    tot = sum(raw)
    return {i: raw[i - 1] / tot for i in range(1, m + 1)}


def build(N, mu, ledger=True):
    J = list(range(1, N))
    Hs = [(j, t, c) for j in J for t in range(N) for c in (0, 1)]

    def w(j, t):
        return 1 if (t % N) == j else 0

    def step(state):
        v, (j, t, c) = state
        primary = (v == w(j, t))
        nxt = w(j, (t + 1) % N)
        v2 = nxt if primary else 1 - nxt
        c2 = c ^ (v if (t == 0 and ledger) else 0)
        return (v2, (j, (t + 1) % N, c2))

    states = [(v, h) for v in (0, 1) for h in Hs]
    phi = {s: step(s) for s in states}
    prior = {h: Q(0) for h in Hs}
    for j in J:
        prior[(j, 0, 0)] = mu[j]
    return phi, prior, states


def iterate(phi, s, n):
    for _ in range(n):
        s = phi[s]
    return s


def rooted(phi, prior, t):
    rows = []
    for a in (0, 1):
        row = [Q(0), Q(0)]
        for h, m in prior.items():
            if m:
                row[iterate(phi, (a, h), t)[0]] += m
        rows.append(tuple(row))
    return tuple(rows)


def B(p):
    return ((p, 1 - p), (1 - p, p))


def matmul(A, C):
    return tuple(tuple(sum(A[i][k] * C[k][j] for k in (0, 1)) for j in (0, 1)) for i in (0, 1))


def stochastic(A):
    return all(all(x >= 0 for x in r) and sum(r) == 1 for r in A)


def tv(A):
    return sum(abs(A[0][j] - A[1][j]) for j in (0, 1)) / 2


def order(phi, states):
    def lcm(a, b):
        return a * b // gcd(a, b)
    seen, o = set(), 1
    for s in states:
        if s in seen:
            continue
        cyc, cur = [], s
        while True:
            cyc.append(cur)
            cur = phi[cur]
            if cur == s:
                break
        seen.update(cyc)
        o = lcm(o, len(cyc))
    return o


# ------------------------------------------------------------- parent clauses

def hidden_conditional(phi, prior, root, s, x):
    mass, tot = {}, Q(0)
    for h, m in prior.items():
        if m:
            v, hh = iterate(phi, (root, h), s)
            if v == x:
                mass[hh] = mass.get(hh, Q(0)) + m
                tot += m
    return None if tot == 0 else {k: v / tot for k, v in mass.items()}


def propagate(phi, law, x, d):
    out = [Q(0), Q(0)]
    for h, m in law.items():
        out[iterate(phi, (x, h), d)[0]] += m
    return tuple(out)


def parent_witness(phi, prior, N):
    """The declared witness: a=0, b=1, w=s=1, x=0, t=2, seed (1,0,0)."""
    seed = (1, 0, 0)
    W = prior[seed] > 0 and iterate(phi, (0, seed), 1)[1] != iterate(phi, (1, seed), 1)[1]
    G1, G2 = rooted(phi, prior, 1), rooted(phi, prior, 2)
    c0 = hidden_conditional(phi, prior, 0, 1, 0)
    c1 = hidden_conditional(phi, prior, 1, 1, 0)
    S = (c0 is not None and c1 is not None and c0 != c1
         and G1[0][0] > 0 and G1[1][0] > 0)
    R1 = S and propagate(phi, c0, 0, 1) != propagate(phi, c1, 0, 1)
    R2 = G2[0] != G2[1]
    return W, S, R1, R2


# ------------------------------------------------------------ instance checks

HORIZONS = list(range(4, 13))
print(f"S1 realization family — exact instance controls at N = {HORIZONS[0]}..{HORIZONS[-1]}")

for N in HORIZONS:
    mu = weights(N)
    phi, prior, states = build(N, mu)
    G = [rooted(phi, prior, t) for t in range(N + 1)]
    p = [Q(1)] + [1 - mu[t] for t in range(1, N)] + [Q(1)]

    ok = True
    ok &= sorted(phi.values()) == sorted(states)                  # permutation
    ok &= sum(prior.values()) == 1 and all(m >= 0 for m in prior.values())
    ok &= all(mu[j] < mu[j + 1] for j in range(1, N - 1))         # strictly increasing
    ok &= all(mu[j] < Q(1, 2) for j in mu)                        # forces N >= 4
    check(f"N={N:2d} construction: permutation, prior, weight shape", ok)

    check(f"N={N:2d} rooted family equals B(p_t) with p_t = 1 - mu_t",
          all(G[t] == B(p[t]) for t in range(N + 1)))
    check(f"N={N:2d} strict decrease to p_(N-1) > 1/2",
          all(p[t] > p[t + 1] for t in range(N - 1)) and p[N - 1] > Q(1, 2))
    check(f"N={N:2d} N_CR = N is minimal (no earlier identity return, storage at s=1)",
          G[N] == B(Q(1)) and all(G[n] != B(Q(1)) for n in range(1, N))
          and G[1][0][0] > 0 and G[1][1][0] > 0)

    div = True
    for s in range(N):
        for t in range(s + 1, N):
            ds, dt = G[s][0][0] - Q(1, 2), G[t][0][0] - Q(1, 2)
            L = B(Q(1, 2) + dt / (2 * ds))
            div &= stochastic(L) and matmul(G[s], L) == G[t]
    check(f"N={N:2d} P-divisible on every K < N, all pairs s < t <= K", div)
    check(f"N={N:2d} revival at (N-1, N): TV {tv(G[N-1])} < {tv(G[N])}",
          tv(G[N - 1]) < tv(G[N]))

    W, S, R1, R2 = parent_witness(phi, prior, N)
    check(f"N={N:2d} parent W/S/R1/R2 at a=0,b=1,w=s=1,x=0,t=2", W and S and R1 and R2)
    check(f"N={N:2d} ord(phi) = 2N", order(phi, states) == 2 * N)

# --------------------------------------------------------- negative controls
print("\nNegative controls (each must break a frozen obligation):")

# 1. Drop the ledger: the hidden component then evolves independently of the visible root,
#    so the write clause fails and the realization is parent-negative.
N = 6
mu = weights(N)
phi_nl, prior_nl, _ = build(N, mu, ledger=False)
W_nl, S_nl, R1_nl, R2_nl = parent_witness(phi_nl, prior_nl, N)
check("no-ledger variant is parent-negative (W fails)", not W_nl)
check("no-ledger variant still has the same rooted family (isolates W)",
      [rooted(phi_nl, prior_nl, t) for t in range(N + 1)]
      == [rooted(*build(N, mu)[:2], t) for t in range(N + 1)])

# 2. Break monotonicity of the weights: divisibility below the horizon must fail.
mu_bad = dict(weights(N))
mu_bad[1], mu_bad[N - 1] = mu_bad[N - 1], mu_bad[1]        # now non-monotone
phi_b, prior_b, _ = build(N, mu_bad)
Gb = [rooted(phi_b, prior_b, t) for t in range(N + 1)]
broke = False
for s in range(N):
    for t in range(s + 1, N):
        ds, dt = Gb[s][0][0] - Q(1, 2), Gb[t][0][0] - Q(1, 2)
        if ds > 0:
            L = B(Q(1, 2) + dt / (2 * ds))
            if not (stochastic(L) and matmul(Gb[s], L) == Gb[t]):
                broke = True
check("non-monotone weights break P-divisibility below the horizon", broke)

print(f"\nscaling_family_probe: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    raise SystemExit("failed: " + "; ".join(FAIL))
print("Instance controls only. The uniform statements are proved in "
      "RECURRENCE-SCALING-RESULT.md; a finite table is not an unbounded family.")
