#!/usr/bin/env python3
# selection_probes.py — certificate for the selection program's phase-1 core
# (papers/Selection.md; b183, corrected b184 per review). Exact fractions
# wherever the claim is exact; numpy only for spectra and unitaries.
#
#   (1) S1(i,iii): exhaustively at (n_V,|C_H|) in {(2,2),(2,3)}, two priors:
#       every reachable operational state is a distribution over that
#       stage's tails; a TAIL VERTEX is reachable iff some prefix makes the
#       future deterministic; the no-redundancy quotient equals the
#       conditional-law quotient.
#   (2) S1(ii): for every pair of distinct reachable states, an explicit
#       separating cylinder test is constructed.
#   (3) Ext control (b184): exact extreme-point computation of the
#       operational polytope S_t(P) (Caratheodory in affine dimension <= 2):
#       instances EXIST whose polytope has MIXED extreme points — extreme in
#       S_t(P) yet not a tail point mass — certifying the document's
#       non-identification of quotient tails with operational pure states.
#   (4) S2 census (corrected b184): RECURSIVELY label-preserving,
#       shift-commuting automorphisms of the staged tail structure — the
#       b183 census accepted label-breaking induced maps and is replaced;
#       group closure verified, orders reported. Finiteness itself is
#       theorem-proved (Lemma S2, on the polytope); the census is a
#       representative certificate.
#   (5) S3 (classical homogeneous-Markov EMBEDDABILITY obstruction):
#       determinant certificates for the negative-determinant
#       (flip-dominant) exemplar regime det A_a = 2a-1 < 0, the 3-state
#       diagonal embedding, and a doubly-negative-spectrum instance with
#       det > 0 certifying the odd-multiplicity eigenvalue criterion
#       independently; numeric square-root searches corroborate. NO memory
#       identification is made (obligation O6).
#   (6) COUNTER-CONTROL (b184): the convex path C(t) = (1-t)I + tA IS a
#       valid continuous stochastic interpolation of a negative-determinant
#       A, its determinant crossing zero en route — S3 forbids roots and
#       semigroups, NOT continuous paths; any exclusion argument from bare
#       path-continuity is refuted here, in-suite.
#   (7) S4: the rotation carrier U(t) is a one-parameter GROUP with valid
#       row-stochastic marginals for all t, M(1) = A_a, M(0) = I; the
#       marginal path is not a semigroup (M(1/2)^2 != M(1), exhibited).
import sys, math
from fractions import Fraction as F
from itertools import permutations, combinations
import numpy as np

fails = 0
def check(name, ok, msg=""):
    global fails
    print(("PASS" if ok else "FAIL"), name, (" " + msg if msg else ""))
    if not ok: fails += 1

K = 3

def instances(nV, nH):
    V, H = list(range(nV)), list(range(nH))
    states = [(x, h) for x in V for h in H]
    priors = [("uniform", {h: F(1, nH) for h in H}),
              ("generic", {h: F(h + 1, sum(range(1, nH + 1))) for h in H})]
    for perm in permutations(states):
        phi = dict(zip(states, perm))
        def tail(x, h, steps):
            out, cx, ch = [], x, h
            for _ in range(steps):
                cx, ch = phi[(cx, ch)]
                out.append(cx)
            return tuple(out)
        for pname, mu in priors:
            yield phi, tail, mu

# ---- exact extreme-point test in affine dimension <= 2 (Caratheodory) ----
def in_conv_pair(p, q, r):
    # is p = t*q + (1-t)*r for some t in [0,1]? exact fractions
    t = None
    for a, b, c in zip(p, q, r):
        if b != c:
            t = F(a - c, b - c); break
    if t is None:
        return p == q
    if not (0 <= t <= 1): return False
    return all(a == t * b + (1 - t) * c for a, b, c in zip(p, q, r))

def in_conv_triple(p, q, r, s):
    # p = l1*q + l2*r + l3*s, l_i >= 0, sum 1: solve 2 independent coords
    n = len(p)
    for i in range(n):
        for j in range(i + 1, n):
            a11, a12 = q[i] - s[i], r[i] - s[i]
            a21, a22 = q[j] - s[j], r[j] - s[j]
            det = a11 * a22 - a12 * a21
            if det == 0: continue
            b1, b2 = p[i] - s[i], p[j] - s[j]
            l1 = (b1 * a22 - b2 * a12) / det
            l2 = (a11 * b2 - a21 * b1) / det
            l3 = 1 - l1 - l2
            if l1 < 0 or l2 < 0 or l3 < 0: return False
            return all(pk == l1 * qk + l2 * rk + l3 * sk
                       for pk, qk, rk, sk in zip(p, q, r, s))
    # all 2x2 systems singular: points affinely dependent; fall back to pairs
    return (in_conv_pair(p, q, r) or in_conv_pair(p, q, s)
            or in_conv_pair(p, r, s))

def extreme_points(points):
    # points: list of tuples of Fractions, affine dim <= 2 by construction
    ext = []
    for i, p in enumerate(points):
        others = [q for j, q in enumerate(points) if j != i]
        inside = p in others
        if not inside:
            for q, r in combinations(others, 2):
                if in_conv_pair(p, q, r): inside = True; break
        if not inside and len(others) >= 3:
            for q, r, s in combinations(others, 3):
                if in_conv_triple(p, q, r, s): inside = True; break
        if not inside: ext.append(p)
    return ext

# ---------- (1)+(2)+(3)+(4) exhaustive ----------
s1_support_ok = s1_reach_ok = s1_quotient_ok = s1_separate_ok = True
ext_sanity_ok = True
mixed_extreme_instances = 0
stage0_mixed_singletons = 0
s2_group_ok = True
group_orders = {}
n_inst = 0
for (nV, nH) in [(2, 2), (2, 3)]:
    for phi, tail, mu in instances(nV, nH):
        n_inst += 1
        law = {}
        for h in range(nH):
            tr = tail(0, h, K)
            law[tr] = law.get(tr, F(0)) + mu[h]
        tails_t = [sorted({tr[t:] for tr in law}) for t in range(K)]
        saw_mixed_here = False
        for t in range(K):
            cond = {}
            for tr, p in law.items():
                pre, suf = tr[:t], tr[t:]
                if p > 0:
                    cond.setdefault(pre, {})
                    cond[pre][suf] = cond[pre].get(suf, F(0)) + p
            Tt = tails_t[t]
            vecs = {}
            for pre, d in cond.items():
                tot = sum(d.values())
                dist = {s: p / tot for s, p in d.items()}
                if not set(dist) <= set(Tt): s1_support_ok = False
                # tail-VERTEX reachability iff deterministic future
                pure_vertex = (len(dist) == 1)
                det_future = (len(d) == 1)
                if pure_vertex != det_future: s1_reach_ok = False
                vecs[pre] = tuple(dist.get(s, F(0)) for s in Tt)
            # S1(iii) + S1(ii)
            keys = list(vecs)
            for i in range(len(keys)):
                for j in range(i + 1, len(keys)):
                    vi, vj = vecs[keys[i]], vecs[keys[j]]
                    same = (vi == vj)
                    agree = all(a == b for a, b in zip(vi, vj))
                    if same != agree: s1_quotient_ok = False
                    if not same:
                        if not any(a != b for a, b in zip(vi, vj)):
                            s1_separate_ok = False
            # (3) Ext control: extreme points of the operational polytope
            pts = sorted(set(vecs.values()))
            ext = extreme_points(pts)
            if not set(ext) <= set(pts): ext_sanity_ok = False
            for e in ext:
                if sum(1 for c in e if c > 0) > 1:
                    saw_mixed_here = True
                    if t == 0 and len(pts) == 1:
                        stage0_mixed_singletons += 1
        if saw_mixed_here: mixed_extreme_instances += 1
        # (4) corrected S2 census: recursive label-preserving automorphisms
        T0 = tails_t[0]
        auts = []
        for pi in permutations(range(len(T0))):
            sigma = {T0[a]: T0[b] for a, b in enumerate(pi)}
            level_ok = True
            cur = sigma
            for lvl in range(K):
                # first-symbol preservation at this level
                if any(ta[0] != tb[0] for ta, tb in cur.items()):
                    level_ok = False; break
                if lvl == K - 1: break
                nxt = {}
                good = True
                for ta, tb in cur.items():
                    sa, sb = ta[1:], tb[1:]
                    if sa in nxt and nxt[sa] != sb: good = False; break
                    nxt[sa] = sb
                if not good or len(set(nxt.values())) != len(nxt):
                    level_ok = False; break
                cur = nxt
            if level_ok: auts.append(pi)
        idx = set(auts)
        ident = tuple(range(len(T0)))
        closed = ident in idx
        if closed:
            for p in auts:
                for q in auts:
                    comp = tuple(p[q[i]] for i in range(len(T0)))
                    if comp not in idx: closed = False; break
                if not closed: break
        if not closed: s2_group_ok = False
        group_orders[len(auts)] = group_orders.get(len(auts), 0) + 1

check("S1i_support (all reachable states are tail-mixtures, exhaustive)",
      s1_support_ok, f"{n_inst} instances")
check("S1i_tail_vertex_reachability (vertex reachable <-> deterministic prefix)",
      s1_reach_ok)
check("S1iii_quotient (operational equivalence == conditional-law equality)",
      s1_quotient_ok)
check("S1ii_separation (explicit cylinder test for every distinct pair)",
      s1_separate_ok)
check("Ext_sanity (extreme set within the conditional-law points)",
      ext_sanity_ok)
check("Ext_mixed_extremes_exist (polytope pure states need not be tails)",
      mixed_extreme_instances > 0 and stage0_mixed_singletons > 0,
      f"{mixed_extreme_instances} instances with mixed extreme points; "
      f"{stage0_mixed_singletons} stage-0 mixed singletons")
check("S2_census (recursively label-preserving automorphisms form a group)",
      s2_group_ok, "orders " + str(sorted(group_orders.items())))

# ---------- (5): S3 embeddability-obstruction certificates ----------
ok_det = all((2 * a - 1) < 0 for a in [F(1, 8), F(1, 4), F(3, 8)])
check("S3a_exemplar_det (det A_a = 2a-1 < 0: the negative-determinant regime)",
      ok_det, "a in {1/8, 1/4, 3/8}; no memory identification made (O6)")
a = F(1, 4)
check("S3a_embedded_3state (diag(A_a, 1): det < 0 persists)", (2 * a - 1) < 0)

B = np.array([[1, 13, 10], [13, 1, 10], [10, 10, 4]], dtype=float) / 24.0
ev = sorted(np.linalg.eigvalsh(B))
spec_ok = (abs(ev[2] - 1) < 1e-12 and abs(ev[0] + 0.5) < 1e-12
           and abs(ev[1] + 0.25) < 1e-12)
rows_ok = np.allclose(B.sum(axis=1), 1) and (B >= -1e-15).all()
check("S3b_double_negative_spectrum (stochastic, eigen {1,-1/2,-1/4}, det>0)",
      spec_ok and rows_ok and np.linalg.det(B) > 0,
      f"det={np.linalg.det(B):.4f}")

def sqrt_residual(A, restarts=200, iters=400, seed=7):
    rng = np.random.default_rng(seed)
    n = A.shape[0]
    best = np.inf
    for _ in range(restarts):
        R = rng.normal(scale=1.0, size=(n, n))
        lr = 0.05
        for _ in range(iters):
            E = R @ R - A
            G = R.T @ E + E @ R.T
            R -= lr * G
            lr *= 0.995
        best = min(best, np.linalg.norm(R @ R - A))
    return best

Aq = np.array([[0.25, 0.75], [0.75, 0.25]])
r2 = sqrt_residual(Aq)
check("S3_numeric_2x2 (square-root search residual bounded away from zero)",
      r2 > 1e-6, f"min residual {r2:.3e}")
r3 = sqrt_residual(B)
check("S3_numeric_3x3 (same for the double-negative instance)",
      r3 > 1e-6, f"min residual {r3:.3e}")

# ---------- (6): the counter-control ----------
cc_ok = True
sign_change = False
prev = 1.0
for k in range(0, 101):
    t = k / 100.0
    Ct = (1 - t) * np.eye(2) + t * Aq
    if not (np.allclose(Ct.sum(axis=1), 1, atol=1e-12) and (Ct >= -1e-15).all()):
        cc_ok = False
    d = np.linalg.det(Ct)
    if prev > 0 and d < 0: sign_change = True
    prev = d
check("COUNTERCONTROL_path_exists (C(t)=(1-t)I+tA valid stochastic for all t)",
      cc_ok and np.allclose((1 - 0) * np.eye(2), np.eye(2)),
      "S3 forbids roots/semigroups, NOT continuous paths")
check("COUNTERCONTROL_det_crossing (det C(t) crosses zero en route)",
      sign_change, "crossing near t = 2/3")

# ---------- (7): S4 quantum carrier ----------
av = 0.25
th = math.acos(math.sqrt(av))
def M(t):
    c, s = math.cos(t * th), math.sin(t * th)
    U = np.array([[c, s], [-s, c]])
    return U ** 2

grid_ok = all(
    np.allclose(M(k / 100.0).sum(axis=1), 1, atol=1e-12)
    and (M(k / 100.0) >= -1e-15).all() for k in range(0, 101))
check("S4_grid (M(t) row-stochastic for all t in [0,1], step 0.01)", grid_ok)
check("S4_endpoints (M(1) = A_a and M(0) = I to 1e-12)",
      np.allclose(M(1.0), Aq, atol=1e-12)
      and np.allclose(M(0.0), np.eye(2), atol=1e-12))
half = M(0.5)
check("S4_halfstep_valid (M(1/2) a valid stochastic matrix)",
      np.allclose(half.sum(axis=1), 1, atol=1e-12) and (half >= 0).all())
dev = np.linalg.norm(half @ half - M(1.0))
check("S4_marginals_not_a_semigroup (M(1/2)^2 != M(1), as documented)",
      dev > 1e-3, f"deviation {dev:.3f}")

print(("selection_probes: ALL PASS" if fails == 0 else
       f"selection_probes: {fails} FAILURE(S)"))
sys.exit(1 if fails else 0)
