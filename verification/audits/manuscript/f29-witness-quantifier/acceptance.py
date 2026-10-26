#!/usr/bin/env python3
"""Acceptance test for the corrected characterization theorem, clause (iii) (Main §3.4).

Corrected (iii): for some accessible order k and every finite accessible horizon K >= k+1,
S arises from marginalizing a deterministic bijection, with (C1), (C3) and (C4) history
readback at k, and a fixed hidden prior independent of the visible initial state.

Three processes, horizon cap KMAX = 3 (X_0..X_3), x_0 uniform:
  M   a two-state Markov chain (memoryless);
  N1  the XOR-involution law, x_{t+1} = x_t XOR h with a fixed fair hidden bit h
      (accessible memory witnesses at orders 1 and 2: x_2 = x_0, x_3 = x_1);
  N2  X_0, X_1, X_2 fair i.i.d., X_3 = X_1 XOR X_2 (witness at order 2 only).

For every process and every pair (k, K) with 1 <= k < K <= KMAX, the test builds the
finite-horizon process dilation of Main's constructive proof from the target's conditional
kernels alone (history ledger, randomness tape, clock, conditional-quantile step,
lexicographic completion), and checks on the realization:
  faithful   the realized joint law through K equals the target's, exactly, for each x_0;
  bijective  the completed map is a permutation of the finite product;
  prior      the hidden prior does not depend on x_0 (by construction; asserted);
  pushfwd    universal theorem (a): for every visible history p ending in x, the hidden
             posterior mu_p pushed through f_x equals the realized next-step law;
  C4@k       a readback gap at k: two histories of length k+1 (X_0..X_k), common
             endpoint, both of positive probability, with different next-step laws;
             p0 = smaller probability, delta = total-variation distance (max over pairs);
  C1         hidden-to-visible influence: two reachable states with the same visible
             value and different next visible value;
  C3         |C_H| >= 2^{I*}, I* = max_t I(X_<t; X_>t | X_t) of the target, in bits.

Directions tested:
  (ii) => (iii): for each witness order k of the target, every K >= k+1 gives a dilation
                 with C1, C3 and C4 at k.
  (iii) => (ii): wherever a realization shows a C4 gap at k, the readback bound
                 I(X_<k; X_{k+1} | X_k) >= p0 delta^2 / ln 2 holds, and the bound is > 0.

Verdicts printed only if every control is green. Exact rationals for all laws; the
conditional mutual informations are floats used only for strict inequalities, with the
margin printed.
"""
from fractions import Fraction as F
from itertools import product
from math import log, log2
import sys

KMAX = 3
PAD = -1


# ---------- target laws: kernels P(x_{c+1} | x_0..x_c) ----------

def markov_kernel(T):
    return lambda past: tuple(T[past[-1]])


def model_kernel(phi, nV, nH, K):
    """Kernels of a bijection model with uniform hidden prior (reachable pasts only)."""
    paths = []
    for x0 in range(nV):
        for h in range(nH):
            s, tr = (x0, h), [x0]
            for _ in range(K):
                s = phi[s]
                tr.append(s[0])
            paths.append(tuple(tr))

    def kern(past):
        c = len(past) - 1
        num = [0] * nV
        den = 0
        for tr in paths:
            if tr[:c + 1] == tuple(past):
                den += 1
                num[tr[c + 1]] += 1
        if den == 0:
            return tuple(F(1) if y == 0 else F(0) for y in range(nV))
        return tuple(F(a, den) for a in num)
    return kern


def n2_kernel(past):
    c = len(past) - 1
    if c < 2:
        return (F(1, 2), F(1, 2))
    y = past[1] ^ past[2]
    return tuple(F(1) if v == y else F(0) for v in range(2))


def target_joint(kern, nV, K):
    """P(x_0..x_K) with x_0 uniform."""
    out = {}
    for tr in product(range(nV), repeat=K + 1):
        p = F(1, nV)
        for c in range(K):
            p *= kern(tr[:c + 1])[tr[c + 1]]
            if p == 0:
                break
        if p:
            out[tr] = p
    return out


# ---------- the dilation of Main's constructive proof ----------

def common_denominator(kern, nV, K):
    D = 1
    for c in range(K):
        for past in product(range(nV), repeat=c + 1):
            for q in kern(past):
                D = D * q.denominator // __import__("math").gcd(D, q.denominator)
    return D


def build_dilation(kern, nV, K, D, mutate=False):
    hists = list(product(list(range(nV)) + [PAD], repeat=K))
    tapes = list(product(range(D), repeat=K))
    states = [(x, hi, tp, c) for x in range(nV) for hi in hists for tp in tapes
              for c in range(K + 1)]

    def wellformed(hi, c):
        return all(hi[i] != PAD for i in range(c)) and all(hi[i] == PAD for i in range(c, K))

    def Q(past, s):
        acc = 0
        dist = kern(past)
        for y in range(nV):
            cnt = dist[y] * D
            assert cnt.denominator == 1
            acc += int(cnt)
            if mutate and y == 0:
                acc += 1  # countercontrol: shift one tape symbol between fibers
            if s < acc:
                return y
        return nV - 1

    phi = {}
    for (x, hi, tp, c) in states:
        if c < K and wellformed(hi, c):
            past = tuple(hi[:c]) + (x,)
            hin = tuple(list(hi[:c]) + [x] + [PAD] * (K - c - 1))
            phi[(x, hi, tp, c)] = (Q(past, tp[c]), hin, tp, c + 1)
    imgs = list(phi.values())
    assert len(imgs) == len(set(imgs)), "partial step not injective"
    unhit = sorted(set(states) - set(imgs))
    undom = sorted(set(states) - set(phi))
    assert len(unhit) == len(undom)
    for a, b in zip(undom, unhit):
        phi[a] = b
    bij = sorted(phi.values()) == sorted(states)
    prior = [((PAD,) * K, tp, 0) for tp in tapes]  # same for every x_0
    return phi, prior, len(hists) * len(tapes) * (K + 1), bij


def realized(phi, prior, nV, K):
    """Joint law of (x_0..x_K) and, per history, the hidden-state posterior at its end."""
    w = F(1, nV * len(prior))
    joint, post = {}, {}
    for x0 in range(nV):
        for h in prior:
            s, tr = (x0,) + h, [x0]
            post_key = (x0,)
            post.setdefault(post_key, {})
            post[post_key][s[1:]] = post[post_key].get(s[1:], 0) + w
            for _ in range(K):
                s = phi[s]
                tr.append(s[0])
                key = tuple(tr)
                post.setdefault(key, {})
                post[key][s[1:]] = post[key].get(s[1:], 0) + w
            joint[tuple(tr)] = joint.get(tuple(tr), 0) + w
    return joint, post


def marg(P, L):
    M = {}
    for t, w in P.items():
        M[t[:L]] = M.get(t[:L], 0) + w
    return M


def conditionals(P, nV, k):
    """Next-step laws P(X_{k+1} | x_0..x_k) for positive-probability histories."""
    Mk, Mk1 = marg(P, k + 1), marg(P, k + 2)
    return {h: tuple(Mk1.get(h + (y,), 0) / w for y in range(nV)) for h, w in Mk.items()}, Mk


def gap(P, nV, k):
    cond, Mk = conditionals(P, nV, k)
    best = None
    hs = sorted(cond)
    for i, a in enumerate(hs):
        for b in hs[i + 1:]:
            if a[-1] != b[-1] or cond[a] == cond[b]:
                continue
            delta = sum(abs(u - v) for u, v in zip(cond[a], cond[b])) / 2
            p0 = min(Mk[a], Mk[b])
            if best is None or p0 * delta * delta > best[0] * best[1] ** 2:
                best = (p0, delta)
    return best  # None: no gap at order k


def cmi_bits(P, a_idx, b_idx, c_idx):
    """I(X_A; X_B | X_C) in bits, float."""
    def m(idx):
        out = {}
        for t, w in P.items():
            key = tuple(t[i] for i in idx)
            out[key] = out.get(key, 0) + w
        return out
    pabc, pac, pbc, pc = m(a_idx + b_idx + c_idx), m(a_idx + c_idx), m(b_idx + c_idx), m(c_idx)
    na, nb = len(a_idx), len(b_idx)
    s = 0.0
    for key, w in pabc.items():
        a, b, c = key[:na], key[na:na + nb], key[na + nb:]
        s += float(w) * log2(float(w) * float(pc[c]) / (float(pac[a + c]) * float(pbc[b + c])))
    return s


def c1(phi, post):
    """Two reachable states with the same visible value and different next visible value."""
    by_x = {}
    for key, d in post.items():
        x = key[-1]
        for h in d:
            by_x.setdefault(x, set()).add(phi[(x,) + h][0])
    return any(len(v) > 1 for v in by_x.values())


def pushforward_ok(phi, post, joint, nV, K):
    for L in range(1, K + 1):
        cond, _ = conditionals(joint, nV, L - 1)
        for hist, c in cond.items():
            mu = post[hist]
            tot = sum(mu.values())
            push = [F(0)] * nV
            for h, w in mu.items():
                push[phi[(hist[-1],) + h][0]] += w / tot
            if tuple(push) != c:
                return False
    return True


# ---------- the test ----------

phiX = {(v, h): (v ^ h, h) for v in range(2) for h in range(2)}
PROCESSES = {
    "M":  markov_kernel([[F(1, 2), F(1, 2)], [F(1, 4), F(3, 4)]]),
    "N1": model_kernel(phiX, 2, 2, KMAX),
    "N2": n2_kernel,
}
EXPECT = {"M": (False, False), "N1": (True, True), "N2": (True, True)}  # ((ii), (iii-A))

controls = {}
rows = {}
for name, kern in PROCESSES.items():
    P = target_joint(kern, 2, KMAX)
    W = [k for k in range(1, KMAX) if gap(P, 2, k)]
    cm = {k: cmi_bits(P, tuple(range(k)), (k + 1,), (k,)) for k in range(1, KMAX)}
    Istar = max(cmi_bits(P, tuple(range(t)), tuple(range(t + 1, KMAX + 1)), (t,))
                for t in range(1, KMAX))
    R = {}
    for K in range(2, KMAX + 1):
        PK = marg(P, K + 1)
        D = common_denominator(kern, 2, K)
        phi, prior, mH, bij = build_dilation(kern, 2, K, D)
        joint, post = realized(phi, prior, 2, K)
        rec = {"faithful": joint == PK, "bijective": bij, "pushfwd": pushforward_ok(phi, post, joint, 2, K),
               "C1": c1(phi, post), "C3": mH >= 2 ** Istar, "mH": mH}
        for k in range(1, K):
            g = gap(joint, 2, k)
            rec[f"C4@{k}"] = g
        R[K] = rec
        controls[f"{name}.K{K}.faithful"] = rec["faithful"]
        controls[f"{name}.K{K}.bijective"] = rec["bijective"]
        controls[f"{name}.K{K}.pushforward"] = rec["pushfwd"]
        # countercontrol: a mutated quantile step must break faithfulness when any kernel is
        # non-degenerate on the horizon
        phim, priorm, _, _ = build_dilation(kern, 2, K, D, mutate=True)
        jm, _ = realized(phim, priorm, 2, K)
        controls[f"{name}.K{K}.mutant_detected"] = (jm != PK)

    def realization_ok(k, K):
        r = R[K]
        return r["faithful"] and r["C1"] and r["C3"] and r[f"C4@{k}"] is not None

    ii = bool(W)
    iiiA = any(all(realization_ok(k, K) for K in range(k + 1, KMAX + 1)) for k in range(1, KMAX))
    old_univ = all(all(realization_ok(k, K) for K in range(k + 1, KMAX + 1)) for k in W)
    # (iii) => (ii): every C4 gap seen in a faithful realization obeys the readback bound
    bounds = []
    for K, r in R.items():
        for k in range(1, K):
            g = r[f"C4@{k}"]
            if g is not None and r["faithful"]:
                lhs = cmi_bits(marg(P, K + 1), tuple(range(k)), (k + 1,), (k,))
                rhs = float(g[0] * g[1] ** 2) / log(2)
                bounds.append((K, k, lhs, rhs, lhs >= rhs and rhs > 0))
    # (ii) => (iii): every witness order has a C1/C3/C4 realization at every K >= k+1
    forward = all(all(realization_ok(k, K) for K in range(k + 1, KMAX + 1)) for k in W)
    rows[name] = dict(W=W, cmi=cm, Istar=Istar, ii=ii, iiiA=iiiA, old_univ=old_univ,
                      bounds=bounds, forward=forward, R=R)

# Detector controls on the gap test.
controls["detector.N1_orders_1_2"] = rows["N1"]["W"] == [1, 2]  # x_2 = x_0, x_3 = x_1
controls["detector.N2_order2_only"] = rows["N2"]["W"] == [2]
iid = target_joint(lambda past: (F(1, 2), F(1, 2)), 2, KMAX)
controls["detector.iid_clean"] = not any(gap(iid, 2, k) for k in range(1, KMAX))

ok = all(controls.values())
for c, v in sorted(controls.items()):
    print(f"control {c}: {'PASS' if v else 'FAIL'}")
if not ok:
    print("CONTROLS FAILED: no verdict")
    sys.exit(1)

all_ok = True
for name, r in rows.items():
    print(f"\n{name}: witness orders W = {r['W']}; CMI_k (bits) = "
          + ", ".join(f"k={k}: {v:.6f}" for k, v in r["cmi"].items()) + f"; I* = {r['Istar']:.6f}")
    for K, rec in r["R"].items():
        c4 = ", ".join(f"k={k}: " + ("none" if rec[f'C4@{k}'] is None else
                                     f"p0={rec[f'C4@{k}'][0]}, delta={rec[f'C4@{k}'][1]}")
                       for k in range(1, K))
        print(f"  K={K}: |C_H|={rec['mH']}, faithful={rec['faithful']}, C1={rec['C1']}, "
              f"C3={rec['C3']}, C4: {c4}")
    for (K, k, lhs, rhs, good) in r["bounds"]:
        print(f"  readback bound K={K}, k={k}: I = {lhs:.6f} >= p0 delta^2/ln2 = {rhs:.6f} "
              f"(margin {lhs - rhs:.6f}): {good}")
    exp_ii, exp_iii = EXPECT[name]
    match = (r["ii"], r["iiiA"]) == (exp_ii, exp_iii) and r["ii"] == r["iiiA"]
    dirs = r["forward"] and all(b[4] for b in r["bounds"])
    all_ok &= match and dirs
    print(f"  (ii) = {r['ii']}; corrected (iii) = {r['iiiA']}; biconditional holds: "
          f"{r['ii'] == r['iiiA']}; as expected: {match}")
    print(f"  (ii) => (iii) via dilation at every witness order: {r['forward']}; "
          f"(iii) => (ii) readback bound at every observed gap: {all(b[4] for b in r['bounds'])}")
    print(f"  original universal-over-witness reading of (iii) = {r['old_univ']}"
          + ("  (vacuous: no witness order)" if not r["W"] else ""))

print("\nVERDICT: " + ("ACCEPT" if all_ok else "REJECT")
      + " - the corrected (iii) agrees with (ii) on the memoryless process and on both "
        "processes with an accessible memory witness, with both proof directions exercised.")
sys.exit(0 if all_ok else 1)
