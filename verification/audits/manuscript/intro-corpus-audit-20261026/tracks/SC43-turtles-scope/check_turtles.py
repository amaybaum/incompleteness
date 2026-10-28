"""SC-43 checks: the deep-sector generator and the turtles argument.

Part A runs exact finite computations (integers and Fractions; no floating point) on small
permutation substrata S = V x H with a uniform prior on the hidden factor. Two data are
compared:

  T_t[i][j]          = (1/|H|) #{h : vis(phi^t(i,h)) = j}            (classical transition law)
  Phi_t(E_ab)_cd     = (1/|H|) #{h : phi^t(a,h) = (c,k), phi^t(b,h) = (d,k), same k}
                                                                   (the uniform-prior channel family,
                                                                    block-trace form)

Both are periodic in t with the period of phi, so comparing t = 0 .. period-1 covers every t.

  A1 control      product enlargement phi x phi_new leaves T_t and Phi_t unchanged at every t,
                  for every phi_new on a 2- or 3-point adjoined factor (exhaustive);
  A2 control      Pair C of verification/lean-mathlib/OIBridge/SemigroupTransfer.lean is
                  replayed: equal Phi_t at every t, fixed-point counts 2 and 0, so no
                  relabelling relates the two (independent replay of a kernel-checked fact);
  A3 countercontrol  a two-way coupled extension changes T_t at some t (the check must fire);
  A4 probe        one-way-driven extensions (skew products (s,f) -> (phi(s), g_s(f))) of a
                  fixed phi by one adjoined bit: count those that leave T_t unchanged at every t,
                  those whose cycle type no product phi x phi_new of the SAME size has, and those
                  that change some Phi_t coherence entry. "Unreachable" here holds at equal size
                  only; A5 shows it disappears after a further enlargement.
  A5 probe        after a further decoupled enlargement of both sides by a cycle whose length N
                  is a common multiple of every cycle length, every skew product of A4 is
                  conjugate to (phi x id_2) x C_N by a visible-fibre-preserving relabelling. The
                  relabelling is built cycle by cycle (cycles grouped by the set of rotations of
                  their visible word) and verified pointwise; T_t equality is re-checked.
  A6 probe        visible-fibre-preserving relabellings of phi on the fixed carrier (3! x 3! = 36):
                  all preserve T_t; count those that change some Phi_t entry. So a fibre-wise
                  relabelling of the kind A5 uses preserves the classical law but not, in general,
                  the channel family.

Part B re-greps the corpus for the phrases this unit corrected.

Run:  python3 -I check_turtles.py <repo-root>
"""
import sys
import itertools
from fractions import Fraction
from math import gcd
from pathlib import Path


def lcm(a, b):
    return a * b // gcd(a, b)


def cycle_type(perm):
    seen, out = set(), []
    for s in range(len(perm)):
        if s in seen:
            continue
        n, x = 0, s
        while x not in seen:
            seen.add(x)
            x = perm[x]
            n += 1
        out.append(n)
    return tuple(sorted(out))


def period(perm):
    p = 1
    for c in cycle_type(perm):
        p = lcm(p, c)
    return p


def compose(p, q):  # p after q
    return [p[q[x]] for x in range(len(q))]


class Sub:
    """A permutation on V x H x ... with visible index vis(x) and hidden index hid(x)."""

    def __init__(self, nv, nh, perm):
        self.nv, self.nh, self.perm = nv, nh, perm

    def idx(self, v, h):
        return v * self.nh + h

    def vis(self, x):
        return x // self.nh

    def hid(self, x):
        return x % self.nh

    def power(self, t):
        p = list(range(len(self.perm)))
        for _ in range(t):
            p = compose(self.perm, p)
        return p

    def T(self, t):
        p = self.power(t)
        return tuple(tuple(Fraction(sum(1 for h in range(self.nh) if self.vis(p[self.idx(i, h)]) == j),
                                    self.nh) for j in range(self.nv)) for i in range(self.nv))

    def Phi(self, t):
        p = self.power(t)
        out = {}
        for a in range(self.nv):
            for b in range(self.nv):
                for c in range(self.nv):
                    for d in range(self.nv):
                        n = 0
                        for h in range(self.nh):
                            xa, xb = p[self.idx(a, h)], p[self.idx(b, h)]
                            if self.vis(xa) == c and self.vis(xb) == d and self.hid(xa) == self.hid(xb):
                                n += 1
                        out[(a, b, c, d)] = Fraction(n, self.nh)
        return out


def product_ext(s, fperm):
    nf = len(fperm)
    # hidden index of the enlarged system is (h, f) -> h * nf + f
    perm = [0] * (len(s.perm) * nf)
    for v in range(s.nv):
        for h in range(s.nh):
            y = s.perm[s.idx(v, h)]
            for f in range(nf):
                perm[(v * s.nh + h) * nf + f] = (s.vis(y) * s.nh + s.hid(y)) * nf + fperm[f]
    return Sub(s.nv, s.nh * nf, perm)


def skew_ext(s, gmaps):
    """(x, f) -> (phi(x), g_x(f)); gmaps[x] is a permutation of the adjoined factor."""
    nf = len(gmaps[0])
    perm = [0] * (len(s.perm) * nf)
    for x in range(len(s.perm)):
        y = s.perm[x]
        for f in range(nf):
            perm[x * nf + f] = y * nf + gmaps[x][f]
    return Sub(s.nv, s.nh * nf, perm)


def same_law(s1, s2, with_phi=True):
    P = lcm(period(s1.perm), period(s2.perm))
    for t in range(P):
        if s1.T(t) != s2.T(t):
            return False
        if with_phi and s1.Phi(t) != s2.Phi(t):
            return False
    return True


def all_perms(n):
    return [list(p) for p in itertools.permutations(range(n))]


def product_cycle_types(phi_ct, nf):
    out = set()
    for fp in all_perms(nf):
        ct = []
        for a in phi_ct:
            for b in cycle_type(fp):
                g = gcd(a, b)
                ct += [a * b // g] * g
        out.add(tuple(sorted(ct)))
    return out


def part_a():
    ok = True
    lines = []
    # A base substratum with non-trivial visible statistics: V = 2, H = 3.
    base = Sub(2, 3, [1, 3, 5, 0, 4, 2])  # an arbitrary 6-cycle-free permutation, fixed
    assert sorted(base.perm) == list(range(6))

    # A1: product enlargement, exhaustive over phi_new on 2 and 3 points.
    n1 = 0
    for nf in (2, 3):
        for fp in all_perms(nf):
            e = product_ext(base, fp)
            if not same_law(base, e):
                ok = False
                lines.append(f"A1 FAIL nf={nf} phi_new={fp}")
            n1 += 1
    lines.append(f"A1 control: product enlargements checked {n1}; all leave T_t and Phi_t unchanged: {ok}")

    # A2: Pair C replay (disjoint transpositions, so composition order is immaterial).
    def swaps(nv, nh, pairs):
        p = list(range(nv * nh))
        for (a, b) in pairs:
            i, j = a[0] * nh + a[1], b[0] * nh + b[1]
            p[i], p[j] = p[j], p[i]
        return Sub(nv, nh, p)
    C = swaps(2, 3, [((0, 2), (1, 0)), ((1, 1), (1, 2))])
    Cp = swaps(2, 3, [((0, 2), (1, 0)), ((1, 1), (1, 2)), ((0, 0), (0, 1))])
    a2_family = same_law(C, Cp)
    fixC = sum(1 for x in range(6) if C.perm[x] == x)
    fixCp = sum(1 for x in range(6) if Cp.perm[x] == x)
    t1 = C.T(1)
    a2 = a2_family and fixC == 2 and fixCp == 0 and t1[0] == (Fraction(2, 3), Fraction(1, 3))
    ok = ok and a2
    lines.append(f"A2 control (Pair C replay): equal family at every t: {a2_family}; fixed points "
                 f"{fixC} vs {fixCp}; T_1 row 0 = {[str(x) for x in t1[0]]}; pass: {a2}")

    # A3: two-way coupled extension must change the law.
    e = product_ext(base, [0, 1])  # identity on the adjoined bit
    p = list(e.perm)
    # after one step, swap the hidden pair (h=0,f=0) <-> (h=1,f=1) in visible state 0: the
    # adjoined bit now feeds back into the hidden coordinate the visible sector reads.
    i, j = (0 * 3 + 0) * 2 + 0, (0 * 3 + 1) * 2 + 1
    tr = list(range(len(p)))
    tr[i], tr[j] = tr[j], tr[i]
    coupled = Sub(e.nv, e.nh, compose(tr, p))
    a3 = not same_law(base, coupled, with_phi=False)
    ok = ok and a3
    lines.append(f"A3 countercontrol: two-way coupled extension changes T_t at some t: {a3}")

    # A4: one-way-driven (skew-product) extensions of `base` by one adjoined bit, exhaustive
    # over the 2^6 assignments g_x in {id, swap}.
    ids, sw = [0, 1], [1, 0]
    prod_cts = product_cycle_types(cycle_type(base.perm), 2)
    n_all = n_T = n_out = n_phi = 0
    witness = None
    for bits in itertools.product((0, 1), repeat=6):
        g = [sw if b else ids for b in bits]
        s = skew_ext(base, g)
        n_all += 1
        if same_law(base, s, with_phi=False):
            n_T += 1
            outside = cycle_type(s.perm) not in prod_cts
            phi_diff = not same_law(base, s, with_phi=True)
            n_out += outside
            n_phi += phi_diff
            if outside and witness is None:
                witness = (bits, cycle_type(s.perm), phi_diff)
    a4 = n_T == n_all  # every skew product preserves the classical law
    ok = ok and a4
    lines.append(f"A4 probe: skew products {n_all}; preserve T_t at every t: {n_T}; cycle type "
                 f"of no equal-size product phi x phi_new: {n_out}; change some Phi_t entry: {n_phi}")
    lines.append(f"A4 base cycle type {cycle_type(base.perm)}; product cycle types {sorted(prod_cts)}; "
                 f"first outside witness (bits, cycle type, Phi differs) {witness}")
    return ok, lines


def cycles_of(perm):
    seen, out = set(), []
    for s in range(len(perm)):
        if s in seen:
            continue
        c, x = [], s
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = perm[x]
        out.append(c)
    return out


def fibre_conjugacy(s1, s2):
    """A bijection pi with pi(s1(x)) = s2(pi(x)) and vis(pi(x)) = vis(x), or None."""
    if len(s1.perm) != len(s2.perm) or s1.nh != s2.nh:
        return None
    pool = {}
    for c in cycles_of(s2.perm):
        w = tuple(s2.vis(x) for x in c)
        key = (len(c), frozenset(w[i:] + w[:i] for i in range(len(w))))
        pool.setdefault(key, []).append(c)
    pi = [None] * len(s1.perm)
    for c in cycles_of(s1.perm):
        w = tuple(s1.vis(x) for x in c)
        key = (len(c), frozenset(w[i:] + w[:i] for i in range(len(w))))
        if not pool.get(key):
            return None
        d = pool[key].pop()
        wd = tuple(s2.vis(x) for x in d)
        r = next(i for i in range(len(w)) if wd[i:] + wd[:i] == w)  # align d's word to c's
        d = d[r:] + d[:r]
        for a, b in zip(c, d):
            pi[a] = b
    n = len(pi)
    if sorted(pi) != list(range(n)):
        return None
    if any(pi[s1.perm[x]] != s2.perm[pi[x]] for x in range(n)):
        return None
    if any(s1.vis(x) != s2.vis(pi[x]) for x in range(n)):
        return None
    return pi


def part_a2():
    lines = []
    base = Sub(2, 3, [1, 3, 5, 0, 4, 2])
    prod = product_ext(base, [0, 1])
    ids, sw = [0, 1], [1, 0]
    n_all = n_eq = n_after = n_phi_after = 0
    Ns = set()
    for bits in itertools.product((0, 1), repeat=6):
        s = skew_ext(base, [sw if b else ids for b in bits])
        n_all += 1
        if fibre_conjugacy(s, prod) is not None or fibre_conjugacy(s, product_ext(base, [1, 0])) is not None:
            n_eq += 1
        N = 1
        for L in cycle_type(s.perm) + cycle_type(prod.perm):
            N = lcm(N, L)
        Ns.add(N)
        cN = [(i + 1) % N for i in range(N)]
        se, pe = product_ext(s, cN), product_ext(prod, cN)
        pi = fibre_conjugacy(se, pe)
        if pi is not None and same_law(se, pe, with_phi=False):
            n_after += 1
            if not same_law(base, s, with_phi=True):
                n_phi_after += 1
    a5 = n_after == n_all
    lines.append(f"A5 probe: skew products {n_all}; fibre-conjugate to phi x id or phi x swap at equal "
                 f"size: {n_eq}; fibre-conjugate to (phi x id_2) x C_N after enlarging both by an "
                 f"N-cycle (pi verified, T re-checked): {n_after}; of these, Phi-changing: "
                 f"{n_phi_after}; N used {sorted(Ns)}")
    n_rel = n_T = n_phi = 0
    for r0 in itertools.permutations(range(3)):
        for r1 in itertools.permutations(range(3)):
            pi = list(r0) + [3 + x for x in r1]
            inv = [0] * 6
            for x in range(6):
                inv[pi[x]] = x
            q = Sub(2, 3, [pi[base.perm[inv[y]]] for y in range(6)])
            n_rel += 1
            n_T += same_law(base, q, with_phi=False)
            n_phi += not same_law(base, q, with_phi=True)
    a6 = n_T == n_rel
    lines.append(f"A6 probe: fibre-wise relabellings of phi on the fixed carrier {n_rel}; preserve T_t: "
                 f"{n_T}; change some Phi_t entry: {n_phi}")
    return a5 and a6, lines


PATTERNS = [
    "can prove that the question loses reference",
    "ends at a line the framework can state exactly",
    "ends where the framework can prove there is nothing left",
    "a proof that below a certain depth",
    "theorems for everything in between",
    "the framework proving where deduction runs out",
    "there is no physics question there to answer",
    "enters the transition probabilities at",
    "demonstrably, nothing of the matter",
    "This identification is recent",
    "a completeness theorem conditional",
    "The framework's claims are mathematical theorems rather than",
    "The exact extent of the hidden sector",
    "the name records the identification, which is a result and not a stipulation",
    "Different values of |C_D| produce the same transition data at leading order",
    "known to exhaust it only conditionally",
    "is not one of the four generator families, and that every such implementation",
    "Different deep-sector cardinalities — including infinite ones — produce the same visible transition data at leading order",
    "This gauge group has four generators",
    "The reconstruction theorem establishes this list",
    "the most recent addition to the paper and the least settled",
    "The deep hidden sector's cardinality is gauge",
    "The hidden sector beyond the boundary layer admits arbitrary cardinality",
]


def part_b(root):
    files = sorted(list((root / "papers").glob("*.md")) + list((root / "book").glob("*.md")))
    counts = {}
    for pat in PATTERNS:
        counts[pat] = sum(f.read_text(encoding="utf-8").count(pat) for f in files)
    keep = {
        "conditional on the semigroup-transfer completeness step": 0,
        "Lemma 24.1": 0,
        "turtle": 0,
    }
    for k in keep:
        keep[k] = sum(f.read_text(encoding="utf-8").count(k) for f in files)
    return counts, keep


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    ok, lines = part_a()
    ok2, lines2 = part_a2()
    ok = ok and ok2
    lines += lines2
    for l in lines:
        print(l)
    counts, keep = part_b(root)
    stale = sum(counts.values())
    print("B re-grep, corrected phrases (expect 0 each):")
    for k, v in counts.items():
        print(f"  {v}  {k}")
    print("B surviving occurrences (context, not targets):")
    for k, v in keep.items():
        print(f"  {v}  {k}")
    verdict = ok and stale == 0
    print("VERDICT", "PASS" if verdict else "FAIL")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
