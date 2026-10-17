"""LOC-1 preflight, leg T: sizes of the identification scopes I0 (ambient) and I1 (sigma_V in the declared
class, sigma_A free).  Pure counting: no matrix, lift or law is read.

An identification of V x A is sigma = (sigma_V, sigma_A), bijections of V and A with their factor grids;
part k of the cut is V_k x A_k.  Two quotients are counted:
  Q-part  (relabellings only): post-composition with S_{|V1|} x S_{|V2|} x S_{|A1|} x S_{|A2|}, and, when
          the parts have equal shapes, the PART swap, which exchanges V1<->V2 and A1<->A2 together;
  Q-set   (thread B's D(C), sizes.py): each set quotiented separately, with its own factor swap, so the
          V-swap and the A-swap act independently.  Q-set identifies (sigma_V, sigma_A) with
          (swap o sigma_V, sigma_A), which pairs V1 with A2: a different cut, not a relabelling.
Orbits are counted by brute force (canonical minimum over the group) and cross-checked by |X| / |G|
(the actions are free).  C21 and the Fin 8 engine control are counted by formula.
Run:  python3 -I scope_T.py
"""
import itertools
from math import factorial


def grid_perms(s1, s2):
    """Group elements acting on a grid Fin s1 x Fin s2 (index a s2 + b): (p1, p2, swap?)."""
    out = []
    for p1 in itertools.permutations(range(s1)):
        for p2 in itertools.permutations(range(s2)):
            out.append(lambda g, p1=p1, p2=p2, s2=s2: p1[g // s2] * s2 + p2[g % s2])
    return out


def swap_map(s):
    return lambda g, s=s: (g % s) * s + g // s


def dedupe(G, nv, na):
    """Group elements as permutation tuples of (V grid, A grid); duplicates (e.g. the swap of a 1 x 1 grid)
    removed, so that |G| is the order of the acting group."""
    seen, out = set(), []
    for g in G:
        key = g((tuple(range(nv)), tuple(range(na))))
        if key not in seen:
            seen.add(key)
            out.append(g)
    return out


def orbit_count(X, G):
    reps = set()
    for x in X:
        reps.add(min(g(x) for g in G))
    return len(reps)


def act(fv, fa):
    return lambda x: (tuple(fv(g) for g in x[0]), tuple(fa(g) for g in x[1]))


def groups(v, a):
    """v = (|V1|, |V2|), a = (|A1|, |A2|); return (Q-part group, Q-set group) as lists of maps on pairs."""
    Vp, Ap = grid_perms(*v), grid_perms(*a)
    ident = lambda g: g
    part = [act(fv, fa) for fv in Vp for fa in Ap]
    same_shape = v[0] == v[1] and a[0] == a[1]
    if same_shape:
        sv, sa = swap_map(v[0]), swap_map(a[0])
        part += [act(lambda g, f=fv: f(sv(g)), lambda g, f=fa: f(sa(g))) for fv in Vp for fa in Ap]
    Vs = Vp + ([lambda g, f=fv: f(swap_map(v[0])(g)) for fv in Vp] if v[0] == v[1] else [])
    As = Ap + ([lambda g, f=fa: f(swap_map(a[0])(g)) for fa in Ap] if a[0] == a[1] else [])
    setq = [act(fv, fa) for fv in Vs for fa in As]
    return part, setq


def count_case(name, v, a):
    nv, na = v[0] * v[1], a[0] * a[1]
    X = [(sv, sa) for sv in itertools.permutations(range(nv)) for sa in itertools.permutations(range(na))]
    part, setq = groups(v, a)
    # declared class of sigma_V under V's own relabellings (with V's factor swap when square)
    Vs = grid_perms(*v) + ([lambda g, f=fv: f(swap_map(v[0])(g)) for fv in grid_perms(*v)] if v[0] == v[1] else [])
    decl = {tuple(f(g) for g in range(nv)) for f in Vs}
    X1 = [x for x in X if x[0] in decl]
    res = {}
    part, setq = dedupe(part, nv, na), dedupe(setq, nv, na)
    for qn, G in (("Q-part", part), ("Q-set", setq)):
        o0, o1 = orbit_count(X, G), orbit_count(X1, G)
        assert len(X) % len(G) == 0 and o0 == len(X) // len(G), (name, qn)
        assert len(X1) % len(G) == 0 and o1 == len(X1) // len(G), (name, qn)
        res[qn] = (o0, o1, len(G))
    return res


def main():
    rows = [("CCT4", (2, 2), (2, 2)), ("CCC", (2, 2), (2, 2)), ("CENT", (2, 2), (1, 1))]
    print("%-6s %-22s %-8s %10s %10s %8s" % ("case", "shape", "quotient", "I0 ambient", "I1 ambient", "|G|"))
    for name, v, a in rows:
        res = count_case(name, v, a)
        for qn in ("Q-part", "Q-set"):
            o0, o1, g = res[qn]
            print("%-6s V %dx%d, A %dx%d %9s %10d %10d %8d" % (name, v[0], v[1], a[0], a[1], qn, o0, o1, g))
    c21 = factorial(16) // (factorial(4) ** 2 * 2)
    print("%-6s V 4x4,  A 1x1        both    %10d %10d %8d" % ("C21", c21, 1, factorial(4) ** 2 * 2))
    print("%-6s Fin 8 as 2x4         both    %10d %10s %8d" % ("K-srch", factorial(8) // (2 * 24), "-", 48))
    # formula controls (free actions): |X| / |G|
    assert count_case("CCT4", (2, 2), (2, 2))["Q-part"][:2] == (24 * 24 // 32, 8 * 24 // 32)
    assert count_case("CCT4", (2, 2), (2, 2))["Q-set"][:2] == (24 * 24 // 64, 8 * 24 // 64)
    assert c21 == 18162144000
    print("orbit counts equal |X|/|G| in every case (free actions): OK")


if __name__ == "__main__":
    main()
