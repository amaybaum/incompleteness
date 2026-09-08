#!/usr/bin/env python3
"""Exact probe for the realization-level CausalReadback discovery round.

All arithmetic is Fraction-exact. The reversible realization constructor is the
b51 finite-horizon dilation pattern used by review4_probes.py: it realizes a
finite history kernel by a bijection on V x H, with H = ledger x tape x clock
and one common uniform hidden prior.

This probe executes the four frozen controls before any Lean definition:
  N1  XOR/history-memory: C4w yes, CausalReadback no (failure is R(2)).
  P1  delayed revival: CausalReadback yes.
  N2  uncoupled reversible product: recurrence yes, CausalReadback no (W fails).
  P/N same phi, two priors: uniform is P-indivisible, delta_0 is P-divisible.

It also gives exact finite reversible countermodels to:
  T2  CausalReadback -> C4e
  T3  CausalReadback -> C4r

No fallback C4cr is defined here.
"""

from fractions import Fraction as F
import itertools

PAD = -1


def build(kern, nV, K, D):
    """b51 finite-horizon reversible dilation, copied structurally from review4_probes.py."""
    hs = list(itertools.product(list(range(nV)) + [PAD], repeat=K))
    ts = list(itertools.product(range(D), repeat=K))
    states = [(x, h, t, c)
              for x in range(nV) for h in hs for t in ts for c in range(K + 1)]

    def wf(h, c):
        return (all(h[i] != PAD for i in range(c))
                and all(h[i] == PAD for i in range(c, K)))

    def Q(past, tape_symbol):
        acc = 0
        dist = kern(past)
        assert sum(dist, F(0)) == 1
        for y in range(nV):
            cnt = dist[y] * D
            assert cnt.denominator == 1, (past, dist, D)
            acc += int(cnt)
            if tape_symbol < acc:
                return y
        raise AssertionError("quantile table did not cover tape")

    phi = {}
    for x, h, tape, c in states:
        if c < K and wf(h, c):
            new_h = tuple(list(h[:c]) + [x] + [PAD] * (K - c - 1))
            phi[(x, h, tape, c)] = (
                Q(tuple(h[:c]) + (x,), tape[c]), new_h, tape, c + 1
            )

    # Complete the injective partial map to a permutation.
    unused_range = sorted(set(states) - set(phi.values()))
    unused_domain = sorted(set(states) - set(phi.keys()))
    assert len(unused_range) == len(unused_domain)
    for a, b in zip(unused_domain, unused_range):
        phi[a] = b

    assert len(phi) == len(states)
    assert len(set(phi.values())) == len(states)

    # Common hidden prior: blank ledger, uniform tape, clock 0.
    mu = [(tuple([PAD] * K), tape, 0) for tape in ts]
    return phi, mu


def stepn(phi, state, n):
    for _ in range(n):
        state = phi[state]
    return state


def rooted_family(phi, mu, nV, K):
    out = []
    wt = F(1, len(mu))
    for k in range(K + 1):
        T = [[F(0) for _ in range(nV)] for _ in range(nV)]
        for a in range(nV):
            for hidden0 in mu:
                state = stepn(phi, (a, *hidden0), k)
                T[a][state[0]] += wt
        out.append(T)
    return out


def hidden_after(phi, root, hidden0, k):
    return stepn(phi, (root, *hidden0), k)[1:]


def hidden_conditional(phi, mu, root, s, x):
    wt = F(1, len(mu))
    mass = F(0)
    raw = {}
    for hidden0 in mu:
        state = stepn(phi, (root, *hidden0), s)
        if state[0] == x:
            h = state[1:]
            raw[h] = raw.get(h, F(0)) + wt
            mass += wt
    if mass == 0:
        return None
    return {h: p / mass for h, p in raw.items()}


def propagate_hidden_conditional(phi, cond, x, delta, nV):
    out = [F(0)] * nV
    for h, p in cond.items():
        state = stepn(phi, (x, *h), delta)
        out[state[0]] += p
    return out


def causal_readback_witness(phi, mu, nV, K):
    """Search the frozen W/S/R clauses literally."""
    Ts = rooted_family(phi, mu, nV, K)
    for a in range(nV):
        for b in range(nV):
            if a == b:
                continue
            for w in range(1, K + 1):
                same_seed_writes = [
                    h0 for h0 in mu
                    if hidden_after(phi, a, h0, w) != hidden_after(phi, b, h0, w)
                ]
                if not same_seed_writes:
                    continue
                for s in range(w, K):
                    for x in range(nV):
                        ca = hidden_conditional(phi, mu, a, s, x)
                        cb = hidden_conditional(phi, mu, b, s, x)
                        if ca is None or cb is None or ca == cb:
                            continue
                        for t in range(s + 1, K + 1):
                            qa = propagate_hidden_conditional(phi, ca, x, t - s, nV)
                            qb = propagate_hidden_conditional(phi, cb, x, t - s, nV)
                            if qa == qb:
                                continue
                            if Ts[t][a] == Ts[t][b]:
                                continue
                            return {
                                "a": a, "b": b, "w": w, "s": s, "x": x, "t": t,
                                "seed": same_seed_writes[0],
                                "read_a": qa, "read_b": qb, "family": Ts,
                            }
    return None


def tv(p, q):
    return sum(abs(a - b) for a, b in zip(p, q)) / 2


def has_c4e(Ts):
    nV = len(Ts[0])
    K = len(Ts) - 1
    for a in range(nV):
        for b in range(a + 1, nV):
            for s in range(K):
                for t in range(s + 1, K + 1):
                    if Ts[s][a] == Ts[s][b] and Ts[t][a] != Ts[t][b]:
                        return (a, b, s, t)
    return None


def has_c4r(Ts):
    nV = len(Ts[0])
    K = len(Ts) - 1
    for a in range(nV):
        for b in range(a + 1, nV):
            for s in range(K):
                for t in range(s + 1, K + 1):
                    ds, dt = tv(Ts[s][a], Ts[s][b]), tv(Ts[t][a], Ts[t][b])
                    if ds < dt:
                        return (a, b, s, t, ds, dt)
    return None


I2 = [[F(1), F(0)], [F(0), F(1)]]
J2 = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]


# N1: XOR/history-memory control.
def k_xor(past):
    c = len(past) - 1
    if c == 0:
        return (F(1, 2), F(1, 2))
    if c == 1:
        y = past[0] ^ past[1]
        return (F(1), F(0)) if y == 0 else (F(0), F(1))
    return (F(1, 2), F(1, 2))


phi, mu = build(k_xor, 2, 2, 2)
Ts = rooted_family(phi, mu, 2, 2)
assert Ts == [I2, J2, J2]
assert causal_readback_witness(phi, mu, 2, 2) is None
assert k_xor((0, 0)) == (F(1), F(0))
assert k_xor((1, 0)) == (F(0), F(1))

a, b, w, s, x, t = 0, 1, 1, 1, 0, 2
assert any(hidden_after(phi, a, h0, w) != hidden_after(phi, b, h0, w) for h0 in mu)
ca = hidden_conditional(phi, mu, a, s, x)
cb = hidden_conditional(phi, mu, b, s, x)
assert ca is not None and cb is not None and ca != cb
assert propagate_hidden_conditional(phi, ca, x, 1, 2) != \
       propagate_hidden_conditional(phi, cb, x, 1, 2)
assert Ts[t][a] == Ts[t][b] == [F(1, 2), F(1, 2)]
print("N1 XOR: C4w YES; W/S/R(1) YES; R(2) NO; CausalReadback NO. PASS")


# P1: delayed visible revival.
def k_rev(past):
    c = len(past) - 1
    if c == 0:
        return (F(1), F(0)) if past[0] == 0 else (F(0), F(1))
    if c == 1:
        return (F(1, 2), F(1, 2))
    return (F(1), F(0)) if past[0] == 0 else (F(0), F(1))


phi, mu = build(k_rev, 2, 3, 2)
Ts = rooted_family(phi, mu, 2, 3)
assert Ts == [I2, I2, J2, I2]
wit = causal_readback_witness(phi, mu, 2, 3)
assert wit is not None
assert (wit["s"], wit["t"]) == (2, 3)
assert has_c4e(Ts) is not None
assert has_c4r(Ts) is not None
print("P1 delayed revival: CausalReadback YES; C4e YES; C4r YES. PASS")


# N2: uncoupled reversible product. Recurrence alone is not readback.
def product_step(v, h):
    return (v ^ 1, h ^ 1)


def product_stepn(v, h, n):
    for _ in range(n):
        v, h = product_step(v, h)
    return v, h


for v in range(2):
    for h in range(2):
        assert product_stepn(v, h, 2) == (v, h)
for h in range(2):
    for k in (1, 2):
        assert product_stepn(0, h, k)[1] == product_stepn(1, h, k)[1]
print("N2 product: recurrence YES; W NO; CausalReadback NO. PASS")


# P/N prior-dependence pair: same dynamics, opposite divisibility verdicts.
def xor_static_step(v, h):
    return (v ^ h, h)


def xor_static_stepn(v, h, n):
    for _ in range(n):
        v, h = xor_static_step(v, h)
    return v, h


for v in range(2):
    for h in range(2):
        assert xor_static_stepn(v, h, 2) == (v, h)


def direct_rooted(prior, K):
    Ts = []
    for k in range(K + 1):
        T = [[F(0), F(0)], [F(0), F(0)]]
        for a in range(2):
            for h, p in prior.items():
                v, _ = xor_static_stepn(a, h, k)
                T[a][v] += p
        Ts.append(T)
    return Ts


uniform = {0: F(1, 2), 1: F(1, 2)}
delta0 = {0: F(1), 1: F(0)}
Tu = direct_rooted(uniform, 2)
Td = direct_rooted(delta0, 2)
assert Tu == [I2, J2, I2]
assert Td == [I2, I2, I2]
assert Tu[1][0] == Tu[1][1] and Tu[2][0] != Tu[2][1]
assert all(Td[k] == I2 for k in range(3))
for h in range(2):
    assert xor_static_step(0, h)[1] == xor_static_step(1, h)[1]
print("Prior pair: same phi/partition; uniform P-INDIVISIBLE, delta_0 P-DIVISIBLE; "
      "CausalReadback NO for both (W fails). PASS")


# T2 countermodel: CausalReadback does NOT imply C4e.
def k_no_collision(past):
    c = len(past) - 1
    x0 = past[0]
    if c == 0:
        return (F(1), F(0)) if x0 == 0 else (F(0), F(1))
    if c == 1:
        return (F(3, 4), F(1, 4)) if x0 == 0 else (F(1, 4), F(3, 4))
    if c == 2:
        return (F(1), F(0)) if x0 == 0 else (F(0), F(1))
    raise AssertionError("outside horizon")


phi, mu = build(k_no_collision, 2, 3, 4)
Ts = rooted_family(phi, mu, 2, 3)
B34 = [[F(3, 4), F(1, 4)], [F(1, 4), F(3, 4)]]
assert Ts == [I2, I2, B34, I2]
wit = causal_readback_witness(phi, mu, 2, 3)
assert wit is not None and (wit["s"], wit["t"]) == (2, 3)
assert has_c4e(Ts) is None
assert has_c4r(Ts) is not None
print("T2: exact reversible countermodel found: CausalReadback YES, C4e NO. REFUTED.")


# T3 countermodel: CausalReadback does NOT imply C4r.
def k_no_revival(past):
    c = len(past) - 1
    x0 = past[0]
    if c == 0:
        return (F(3, 4), F(1, 4)) if x0 == 0 else (F(1, 4), F(3, 4))
    if c == 1:
        return (F(5, 8), F(3, 8)) if x0 == 0 else (F(3, 8), F(5, 8))
    raise AssertionError("outside horizon")


phi, mu = build(k_no_revival, 2, 2, 8)
Ts = rooted_family(phi, mu, 2, 2)
B58 = [[F(5, 8), F(3, 8)], [F(3, 8), F(5, 8)]]
assert Ts == [I2, B34, B58]
wit = causal_readback_witness(phi, mu, 2, 2)
assert wit is not None and (wit["s"], wit["t"]) == (1, 2)
assert [tv(T[0], T[1]) for T in Ts] == [F(1), F(1, 2), F(1, 4)]
assert has_c4e(Ts) is None
assert has_c4r(Ts) is None
print("T3: exact reversible countermodel found: CausalReadback YES, C4r NO "
      "(TV 1 -> 1/2 -> 1/4). REFUTED.")

print("CausalReadback calibration: ALL FOUR FROZEN CONTROLS PASS.")
print("Bridge status from exact probes: T2 FALSE; T3 FALSE; T1 remains theorem work.")
print("No C4cr predicate has been defined.")
