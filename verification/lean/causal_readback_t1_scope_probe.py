#!/usr/bin/env python3
"""Exact control for the T1 preparation-scope correction on PR #542.

Reuses the exact finite reversible T3 realization from
causal_readback_discovery_probe.py.  The realization satisfies the full frozen
W/S/R parent.  With both witness roots supported in the standalone visible
initial law, C4w is present.  With either fixed-root initial law, C4w is absent
on the same two-step window.
"""

from fractions import Fraction as F
import causal_readback_discovery_probe as d


phi, mu = d.build(d.k_no_revival, 2, 2, 8)
wit = d.causal_readback_witness(phi, mu, 2, 2)
assert wit is not None
assert (wit["a"], wit["b"], wit["s"], wit["t"]) == (0, 1, 1, 2)


def trajectory_weights(p0):
    """Exact law of (X0,X1,X2) for a standalone visible initial law p0."""
    out = {}
    wh = F(1, len(mu))
    for root, pr in p0.items():
        if pr == 0:
            continue
        for hidden0 in mu:
            st0 = (root, *hidden0)
            st1 = d.stepn(phi, st0, 1)
            st2 = d.stepn(phi, st0, 2)
            tr = (root, st1[0], st2[0])
            out[tr] = out.get(tr, F(0)) + pr * wh
    assert sum(out.values(), F(0)) == 1
    return out


def next_law(tab, hist):
    """P(X2 | X0,X1 = hist), exactly."""
    den = sum(p for tr, p in tab.items() if tr[:2] == hist)
    assert den > 0
    return tuple(sum(p for tr, p in tab.items() if tr[:2] == hist and tr[2] == y) / den
                 for y in range(2))


def c4w_at_time1(tab):
    histories = sorted({tr[:2] for tr, p in tab.items() if p > 0})
    for h1 in histories:
        for h2 in histories:
            if h1 >= h2 or h1[-1] != h2[-1]:
                continue
            if next_law(tab, h1) != next_law(tab, h2):
                return h1, h2, next_law(tab, h1), next_law(tab, h2)
    return None


# Both parent witness roots have positive standalone preparation probability.
mixed = trajectory_weights({0: F(1, 2), 1: F(1, 2)})
wmix = c4w_at_time1(mixed)
assert wmix is not None
h0, h1, q0, q1 = wmix
assert h0 == (0, 0) and h1 == (1, 0)
assert q0 == (F(5, 8), F(3, 8))
assert q1 == (F(3, 8), F(5, 8))
print("T1 scope positive: mixed root support -> C4w YES. PASS")


# Same realization, same hidden prior and same rooted family, but fixed visible root.
for root in (0, 1):
    tab = trajectory_weights({root: F(1)})
    assert c4w_at_time1(tab) is None
    # At time 1, each current visible endpoint has only one positive visible history
    # because X0 is fixed.  Therefore no same-current, different-history witness exists.
    histories = sorted({tr[:2] for tr, p in tab.items() if p > 0})
    for x in (0, 1):
        assert len([h for h in histories if h[-1] == x]) <= 1
    print(f"T1 scope negative: delta_{root} root law -> C4w NO. PASS")

print("T1 preparation-scope control: COMPLETE")
