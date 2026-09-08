#!/usr/bin/env python3
"""Exact controls for target T3 of OI-ROOTED-CLASSIFICATION-AUDIT.md.

Frozen preregistration: commit 945aa89484badb0b4c064693fe5b2006d049b778, authoritative blob
1dd761349a9f319fc7e507814b7acdbb85c3eb78.  This probe carries the adversarial half of the round.
It is not a sufficiency proof and is not offered as one: the uniform T2 statement, if it lands, is
a kernel theorem, and the frozen standards forbid citing a failed adversarial search as support for
it.

Three things are checked, in exact rational arithmetic.

Section A stresses the response-table realization on families chosen to be hostile to it: total
collapse onto one visible value, deterministic rank-one steps, rank-one at every nonzero phase,
non-dyadic entries, visible swaps with no collapse, mixed-rank periods, and the same shapes on a
three-valued carrier.  Every realization is checked for a total, injective, surjective step on
V x H, a nonnegative normalized prior, and entrywise agreement with Gamma at every time up to
three periods.

Section B records why a response table must not store phase zero.  In a variant whose tables carry
a phase-zero entry, the step map is a permutation exactly when f(.,0) is injective — checked here
table by table, as an iff — because the closing arrows of two root-cycles otherwise land on the
same phase-zero state.  Gamma_0 = I rescues that only on tables of nonzero product weight, which
makes reversibility depend on a support invariant.  The kernel construction avoids the hazard
structurally instead, by indexing tables on nonzero phases alone and taking the root itself as the
phase-zero state.  This section is the negative control on the variant that was set aside, not an
audit of the kernel's own carrier.

Section C carries the round's first separation result:

  THEOREM.  If |V| >= 2 and Gamma_t(a,j) = Gamma_t(b,j) = 1 for distinct roots a, b, then Gamma has
  no inherited realization whose prior has full support.

  Full support gives prior h > 0 for every h, so Gamma_t(a,j) = 1 forces visible(step^t(a,h)) = j
  for every h, and likewise for b.  Then step^t carries the 2|H| states {a,b} x H into the |H|
  states {j} x H; injectivity gives 2|H| <= |H|, so |H| = 0, against sum_h prior h = 1.

The witness is in P_per and IS realizable at the inherited interface, so this separates the
inherited class from its full-support variant rather than refuting sufficiency.  Zero-prior padding
is therefore mathematically unavoidable on such a family, not an artifact of one construction.

Section D carries the carrier lower bound:

  LEMMA.  dim_Q span_Q { Gamma_t(a,j) } <= |H| for every inherited realization, since each entry is
  a subset sum of the |H| numbers prior h.

  COROLLARY.  No carrier bound is a function of |V| alone: at |V| = 2 there are period-M families
  in P_per forcing |H| >= M.

This is an existential worst-case lower bound, not a pointwise claim and not a Theta(M) claim, and
it does not cross the construction's upper bound |V|^(|V|M) (1 + |V|M) at any M.  The counting
attack therefore closes without an obstruction, for a proved reason rather than by exhaustion.

Section E is the frozen negative visible control: the P_per checker must reject families violating
row stochasticity, Gamma_0 = I, and temporal periodicity.
"""

import itertools
from fractions import Fraction as Q

PASS, FAIL = [], []
PAD = "pad"


def check(name, ok):
    (PASS if ok else FAIL).append(name)
    print(f"  {'PASS' if ok else 'FAIL'}  {name}")


# ------------------------------------------------------------------ visible layer

def ident(n):
    return [[Q(1) if a == j else Q(0) for j in range(n)] for a in range(n)]


def is_stochastic(G, n):
    return all(sum(G[a]) == 1 and all(G[a][j] >= 0 for j in range(n)) for a in range(n))


def in_PPer(gam, n, M):
    """The frozen visible candidate: Gamma_0 = I, every Gamma_t row-stochastic, period M > 0."""
    if M <= 0 or gam[0] != ident(n):
        return False
    return all(is_stochastic(G, n) for G in gam)


# ------------------------------------------- the response-table realization (T2's construction)

def supported_tables(gam, n, M):
    """Tables f : V x Z_M -> V of nonzero product weight, with their weights.

    f(a,0) = a is forced by Gamma_0 = I; for k >= 1 the value must lie in the support of row a of
    Gamma_k or the product weight vanishes.
    """
    slots = [(a, k) for a in range(n) for k in range(1, M)]
    choices = [[j for j in range(n) if gam[k][a][j] > 0] for (a, k) in slots]
    out = []
    for combo in itertools.product(*choices):
        f = {(a, 0): a for a in range(n)}
        f.update(dict(zip(slots, combo)))
        w = Q(1)
        for (a, k) in slots:
            w *= gam[k][a][f[(a, k)]]
        if w > 0:
            out.append((tuple(sorted(f.items())), f, w))
    return out


def all_tables(gam, n, M):
    """Every table, supported or not, with f(a,0) ranging freely. Used only by the Section B control."""
    slots = [(a, k) for a in range(n) for k in range(M)]
    out = []
    for combo in itertools.product(*[list(range(n)) for _ in slots]):
        f = dict(zip(slots, combo))
        out.append((tuple(sorted(f.items())), f, Q(1)))
    return out


def build(tabs, n, M):
    """Hidden carrier, prior and step for a given table set."""
    hidden = [("tab", key) for (key, _f, _w) in tabs]
    for (key, _f, _w) in tabs:
        for a in range(n):
            for k in range(1, M):
                hidden.append((PAD, key, a, k))

    prior = {h: Q(0) for h in hidden}
    for (key, _f, w) in tabs:
        prior[("tab", key)] = w

    step, collisions = {}, 0
    for (key, f, _w) in tabs:
        for a in range(n):
            if M == 1:
                arrows = [((a, ("tab", key)), (a, ("tab", key)))]
            else:
                arrows = [((a, ("tab", key)), (f[(a, 1)], (PAD, key, a, 1)))]
                for k in range(1, M - 1):
                    arrows.append(((f[(a, k)], (PAD, key, a, k)),
                                   (f[(a, k + 1)], (PAD, key, a, k + 1))))
                arrows.append(((f[(a, M - 1)], (PAD, key, a, M - 1)),
                               (f[(a, 0)], ("tab", key))))
            for src, dst in arrows:
                if src in step and step[src] != dst:
                    collisions += 1
                step[src] = dst

    for v in range(n):
        for h in hidden:
            step.setdefault((v, h), (v, h))

    return hidden, prior, step, collisions


def rooted_map(hidden, prior, step, n, t):
    G = [[Q(0)] * n for _ in range(n)]
    for a in range(n):
        for h in hidden:
            if prior[h] == 0:
                continue
            s = (a, h)
            for _ in range(t):
                s = step[s]
            G[a][s[0]] += prior[h]
    return G


def is_permutation(step, hidden, n):
    states = [(v, h) for v in range(n) for h in hidden]
    if len(step) != len(states):
        return False
    images = [step[s] for s in states]
    return len(set(images)) == len(states) and set(images) == set(states)


# ------------------------------------------------------------ Section A, adversarial families

J2 = [[Q(1, 2), Q(1, 2)], [Q(1, 2), Q(1, 2)]]
COLLAPSE2 = [[Q(1), Q(0)], [Q(1), Q(0)]]
COLLAPSE2B = [[Q(0), Q(1)], [Q(0), Q(1)]]
THIRD = [[Q(1, 3), Q(2, 3)], [Q(2, 3), Q(1, 3)]]
SWAP2 = [[Q(0), Q(1)], [Q(1), Q(0)]]
J3 = [[Q(1, 3)] * 3 for _ in range(3)]
A3 = [[Q(1, 2), Q(1, 2), Q(0)], [Q(0), Q(1, 2), Q(1, 2)], [Q(1, 3), Q(1, 3), Q(1, 3)]]
C3 = [[Q(1), Q(0), Q(0)] for _ in range(3)]

HOSTILE = [
    ("trivial period", [ident(2)], 2, 1),
    ("uniform collapse then revival", [ident(2), J2], 2, 2),
    ("deterministic rank-one collapse", [ident(2), COLLAPSE2], 2, 2),
    ("non-dyadic entries", [ident(2), THIRD], 2, 2),
    ("visible swap, no collapse", [ident(2), SWAP2], 2, 2),
    ("collapse, revive, collapse", [ident(2), J2, COLLAPSE2], 2, 3),
    ("mixed rank and zero entries", [ident(2), THIRD, COLLAPSE2, J2], 2, 4),
    ("rank-one at every nonzero phase", [ident(2), COLLAPSE2, COLLAPSE2B], 2, 3),
    ("three values, total collapse", [ident(3), J3], 3, 2),
    ("three values, asymmetric rows", [ident(3), A3], 3, 2),
    ("three values, rank-one then mixing", [ident(3), C3, J3], 3, 3),
]

print("Section A — response-table realization on adversarial families")
for name, gam, n, M in HOSTILE:
    tabs = supported_tables(gam, n, M)
    hidden, prior, step, _c = build(tabs, n, M)
    ok = in_PPer(gam, n, M)
    ok &= is_permutation(step, hidden, n)
    ok &= sum(prior.values()) == 1 and all(p >= 0 for p in prior.values())
    ok &= all(rooted_map(hidden, prior, step, n, t) == gam[t % M] for t in range(3 * M + 1))
    check(f"{name}: reversible, common prior, exact at all t <= 3M  (|H|={len(hidden)})", ok)

print("\nSection B — why the phase-zero-storing table variant was set aside")
gam, n, M = [ident(2), THIRD], 2, 2
h_s, _p, step_s, _c = build(supported_tables(gam, n, M), n, M)
check("supported tables: the step map is a permutation", is_permutation(step_s, h_s, n))
h_a, _p2, step_a, _c2 = build(all_tables(gam, n, M), n, M)
check("unrestricted tables: the step map is not a permutation",
      not is_permutation(step_a, h_a, n))

# The failure is on the target side, so a source-collision counter does not see it: for a table
# with f(a,0) = f(b,0), the closing arrows of the cycles for roots a and b both land on the
# phase-zero state of the cycle for f(a,0). Checked table by table, as an iff rather than by
# exhibiting one bad table.
iff_holds = True
for (key, f, _w) in all_tables(gam, n, M):
    h1, _p1, s1, _c1 = build([(key, f, Q(1))], n, M)
    if is_permutation(s1, h1, n) != (len({f[(a, 0)] for a in range(n)}) == n):
        iff_holds = False
check("table by table: the step is a permutation iff f(.,0) is injective", iff_holds)
check("Gamma_0 = I forces f(.,0) = id on every supported table",
      all(all(f[(a, 0)] == a for a in range(n))
          for (_k, f, _w) in supported_tables(gam, n, M)))

# ------------------------------------------------------ Section C, the full-support separation

print("\nSection C — inherited class strictly contains its full-support variant")
WITNESS, WN, WM = [ident(2), COLLAPSE2], 2, 2
check("witness lies in P_per", in_PPer(WITNESS, WN, WM))

collisions = [(t, a, b, j)
              for t in range(WM) for j in range(WN)
              for a in range(WN) for b in range(a + 1, WN)
              if WITNESS[t][a][j] == 1 and WITNESS[t][b][j] == 1]
check("witness drives distinct roots deterministically onto one value", collisions == [(1, 0, 1, 0)])

w_hidden, w_prior, w_step, _c = build(supported_tables(WITNESS, WN, WM), WN, WM)
inherited_ok = (is_permutation(w_step, w_hidden, WN)
                and all(rooted_map(w_hidden, w_prior, w_step, WN, t) == WITNESS[t % WM]
                        for t in range(3 * WM + 1)))
zero_mass = sum(1 for h in w_hidden if w_prior[h] == 0)
check(f"witness is realizable at the inherited interface (|H|={len(w_hidden)})", inherited_ok)
check(f"that realization needs zero-prior states ({zero_mass} of {len(w_hidden)})", zero_mass > 0)


def full_support_exists(gam, n, M, max_h=3, grid=6):
    """Bounded control for the Section C theorem, which itself covers every finite |H|."""
    for hsize in range(1, max_h + 1):
        states = [(v, h) for v in range(n) for h in range(hsize)]
        idx = {s: i for i, s in enumerate(states)}
        priors = [[Q(c, grid) for c in combo]
                  for combo in itertools.product(range(1, grid), repeat=hsize)
                  if sum(combo) == grid]
        for perm in itertools.permutations(range(len(states))):
            for w in priors:
                good = True
                for t in range(M + 1):
                    if not good:
                        break
                    for a in range(n):
                        row = [Q(0)] * n
                        for h in range(hsize):
                            s = idx[(a, h)]
                            for _ in range(t):
                                s = perm[s]
                            row[states[s][0]] += w[h]
                        if row != gam[t % M][a]:
                            good = False
                            break
                if good:
                    return True
    return False


check("no full-support realization at |H| <= 3 on a sixths grid (bounded control)",
      not full_support_exists(WITNESS, WN, WM))
check("a family without a deterministic collision is not excluded by the theorem",
      full_support_exists([ident(2), J2], 2, 2))

# ------------------------------------------------------------- Section D, carrier lower bound

print("\nSection D — no carrier bound is a function of |V| alone")

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def rank_Q(vectors):
    rows = [list(v) for v in vectors]
    n = len(rows[0]) if rows else 0
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, len(rows)) if rows[i][col] != 0), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        pv = rows[r][col]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][col] != 0:
                f = rows[i][col]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def radical_family(M):
    """|V| = 2, period M, Gamma_k = B(1/2 + sqrt(q_k)/100) on the basis {1, sqrt q_1, ...}.

    Square roots of distinct primes are Q-linearly independent, so the entries span a Q-space of
    dimension M. Coefficients stay rational; no floating point enters.
    """
    dim = 1 + len(PRIMES)
    one = [Q(1)] + [Q(0)] * (dim - 1)
    zero = [Q(0)] * dim
    gam = [[[one, zero], [zero, one]]]
    for k in range(1, M):
        p = [Q(1, 2)] + [Q(0)] * (dim - 1)
        p[k] = Q(1, 100)
        q = [a - b for a, b in zip(one, p)]
        gam.append([[p, q], [q, p]])
    return gam, one


def upper_bound(nV, M):
    return nV ** (nV * M) * (1 + nV * M)


crossed = False
for M in range(1, 10):
    gam, one = radical_family(M)
    rows_ok = all(all([sum(c) for c in zip(*row)] == one for row in G) for G in gam)
    dim = rank_Q([e for G in gam for row in G for e in row])
    if not (rows_ok and dim == M and dim <= upper_bound(2, M)):
        crossed = True
check("period-M families force |H| >= M at |V| = 2, for M = 1..9", not crossed)
check("the forced carrier never crosses the construction's upper bound", not crossed)

# ------------------------------------------------------- Section E, negative visible controls

print("\nSection E — the P_per checker rejects the frozen bad shapes")
check("rejects a family failing row stochasticity",
      not in_PPer([ident(2), [[Q(1, 2), Q(1, 4)], [Q(1, 2), Q(1, 2)]]], 2, 2))
check("rejects a family failing Gamma_0 = I", not in_PPer([J2, ident(2)], 2, 2))


def has_visible_period(seq, horizon):
    """Does some M in 1..horizon satisfy Gamma_(t+M) = Gamma_t for every t within the window?"""
    return any(all(seq(t + M) == seq(t) for t in range(horizon))
               for M in range(1, horizon + 1))


# The two frozen CausalReadback controls, as complete families rather than horizon realizations.
pdFamily = lambda t: ident(2) if t == 0 else J2
peFamily = lambda t: J2 if t == 2 else ident(2)
check("rejects the nonperiodic pdFamily control", not has_visible_period(pdFamily, 8))
check("rejects the nonperiodic peFamily control", not has_visible_period(peFamily, 8))
check("accepts a genuinely periodic family", has_visible_period(lambda t: [ident(2), J2][t % 2], 8))

print(f"\nrooted_classification_t3_probe: {len(PASS)} passed, {len(FAIL)} failed")
if FAIL:
    raise SystemExit("failed: " + "; ".join(FAIL))
print("Adversarial controls only. No counterexample to P_per subseteq C_OI has been found, and the "
      "frozen preregistration forbids reading that absence as support for sufficiency.")
