#!/usr/bin/env python3
# intervention_probes.py — b76B (2026-08-12)
# The intervention dilation, classical comb: for a finite-horizon,
# finite-action-labeled kernel family {P(x_{k+1} | x_{<=k}, a_{<=k})},
# construct (S, phi, mu_H, {I_a}) with phi and every I_a bijections such
# that the protocol (I_{a_k}, then phi) reproduces the conditional law for
# EVERY action sequence — exact Fractions, all histories checked.
from fractions import Fraction as F
import itertools

nV, nA = 2, 2
BLANK = -1
import sys
K = int(sys.argv[1]) if len(sys.argv) > 1 else 2
def kern(ctx):
    """Target kernel P(x_{k+1}=1 | ctx). K=1: all contexts binary (fully
    generic). K=2: six designated binary contexts (action- and history-
    dependent), the rest deterministic — keeps |U| = 64 while the test
    still spans every action sequence and history."""
    xs, as_ = ctx
    v = 1 + sum(xs) + 2*sum(as_) + 3*len(xs) + (xs[-1]^as_[-1])
    p1 = F(v % 7 + 1, 9)
    if K == 1: return {0: 1 - p1, 1: p1}
    binary = (len(xs) == 1) or (len(xs) == 2 and as_[0] == 0 and xs[1] == as_[1])
    if binary: return {0: 1 - p1, 1: p1}
    d = (sum(xs) + sum(as_)) % 2
    return {d: F(1), 1-d: F(0)}

# contexts: (x_0..x_k, a_0..a_k) for k = 0..K-1
ctxs = []
for k in range(K):
    for xs in itertools.product(range(nV), repeat=k+1):
        for as_ in itertools.product(range(nA), repeat=k+1):
            ctxs.append((xs, as_))
# hidden tables u: one value per context, weight = prod of kernel probs
tables = [{}]
for c in ctxs:
    new = []
    for tb in tables:
        for y in range(nV):
            if kern(c)[y] > 0:
                t2 = dict(tb); t2[c] = y; new.append(t2)
    tables = new
U = [tuple(sorted(tb.items())) for tb in tables]
mu = {}
for ui, tb in enumerate(U):
    w = F(1)
    for c, y in tb: w *= kern(c)[y]
    mu[ui] = w
assert sum(mu.values()) == F(1)

# state: (x, xhist, ahist, u, clock); ledgers length K, BLANK-padded
xh = list(itertools.product(list(range(nV)) + [BLANK], repeat=K))
ah = list(itertools.product(list(range(nA)) + [BLANK], repeat=K))
states = [(x, h, a, u, c) for x in range(nV) for h in xh for a in ah
          for u in range(len(U)) for c in range(K+1)]
sidx = {s: i for i, s in enumerate(states)}

def wf_x(h, c): return all(h[i] != BLANK for i in range(c)) and all(h[i] == BLANK for i in range(c, K))
def wf_a(a, c, wrote):  # after I_{a_c} acted: slots < c filled, slot c filled iff wrote
    n = c + (1 if wrote else 0)
    return all(a[i] != BLANK for i in range(n)) and all(a[i] == BLANK for i in range(n, K))

# instruments: I_act = involution swapping BLANK <-> act at the clock-indexed slot
def instr(act):
    m = {}
    for s in states:
        x, h, a, u, c = s
        if c < K:
            al = list(a)
            if al[c] == BLANK: al[c] = act
            elif al[c] == act: al[c] = BLANK
            m[s] = (x, h, tuple(al), u, c)
        else:
            m[s] = s
    assert sorted(m.values()) == sorted(states), "instrument not a bijection"
    return m
INSTR = {act: instr(act) for act in range(nA)}

# step bijection phi: on protocol-shaped states (clock c, xhist filled to c,
# ahist filled to c+1 i.e. action just written), read context, write u_ctx,
# append x to xhist, clock+1; complete leftovers to a bijection.
phi = {}
for s in states:
    x, h, a, u, c = s
    if c < K and wf_x(h, c) and wf_a(a, c, wrote=True):
        ctx = (tuple(list(h[:c]) + [x]), tuple(a[:c+1]))
        y = dict(U[u])[ctx]
        h2 = tuple(list(h[:c]) + [x] + [BLANK]*(K-c-1))
        phi[s] = (y, h2, a, u, c+1)
undef = sorted(set(states) - set(phi.keys()))
unhit = sorted(set(states) - set(phi.values()))
for a_, b_ in zip(undef, unhit): phi[a_] = b_
assert sorted(phi.values()) == sorted(states), "phi not a bijection"

# verify: every action sequence, every step, every positive-mass history
def run(u, x0, aseq):
    s = (x0, tuple([BLANK]*K), tuple([BLANK]*K), u, 0)
    traj = [x0]
    for k in range(K):
        s = INSTR[aseq[k]][s]
        s = phi[s]
        traj.append(s[0])
    return tuple(traj)

checked = 0
for aseq in itertools.product(range(nA), repeat=K):
    for x0 in range(nV):
        # joint over trajectories under uniform x0 slice (fix x0, weight mu)
        joint = {}
        for ui, w in mu.items():
            tr = run(ui, x0, aseq)
            joint[tr] = joint.get(tr, F(0)) + w
        # conditionals at each step vs target
        for k in range(K):
            for prefix in itertools.product(range(nV), repeat=k+1):
                if prefix[0] != x0: continue
                mass = sum(w for tr, w in joint.items() if tr[:k+1] == prefix)
                if mass == 0: continue
                for y in range(nV):
                    got = sum(w for tr, w in joint.items()
                              if tr[:k+1] == prefix and tr[k+1] == y) / mass
                    want = kern((prefix, tuple(aseq[:k+1])))[y]
                    assert got == want, (aseq, prefix, k, y, got, want)
                    checked += 1
print(f"intervention dilation: EXACT for all {nA**K} action sequences x all")
print(f"    positive-mass histories ({checked} conditionals, Fractions);")
print(f"    phi and both instruments certified bijections on |S| = {len(states)}.")
print(f"intervention probe (K={K}): COMPLETE — CLASSICAL COMB REPRODUCED")
