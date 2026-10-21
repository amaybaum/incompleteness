"""E1 / E2: the fixed global update on a fixed graph and region, nothing else (exact, F2).

Protocol class.  A protocol is (graph G on n sites, region R, toy site tau not in R, clean
declaration, elapsed time t).  The observer's memory is the visible configuration at time t and
nothing else (no external history); the observer knows the declared clean values and t.  In E2
the controller and memory are further visible sites of the same graph; because the update is
linear, the clean values (the controller's program) enter every cell as a known additive
constant and cannot change which hidden functionals reach memory (verified by check_core.py for
every clean-value assignment at n <= 3).  E2 is therefore E1 on the enlarged graph, and the
tables split by |R| (|R| = 1: the pointer alone; |R| >= 2: pointer plus memory/controller
sites).

Time.  M is a bijection of a finite set, so t -> M^t is periodic with period ord(M); every
quantity is computed for t = 1 .. ord(M) - 1, which is exact for every t >= 1.

Per case:
  minF   min over t of the toy's posterior support given the final visible configuration
  learn  some t has posterior support 1 while the prior support of the toy's current state is 4
         (the toy is not partly overwritten by clean inflow: genuine learning)
  minH   the same with the full visible history 0..t (K-EXTHIST)
Controls (each must be 0):
  NONE   with no clean coordinate, posterior == prior at every t (records carry nothing)
  SYMP   every final-memory reconstruction g_j = f_j + k_j (f_j in span F, k_j clean) has
         omega(k_1, g_2) = omega(k_2, g_1) = 1  (the known-displacement lemma of the report)
  CAP    posterior rank of all hidden cells == #unknown - rank(F_u)  (capacity identity)
persist: some t at which the final memory determines the toy's INITIAL state while its current
state keeps support >= 2 (old records retained while fresh uncertainty reaches the toy).
Also tabulated by the inner boundary |d^-R| (visible sites with a hidden neighbour): |d^-R| = 1
is the single-apparatus arrangement (one pointer touching the hidden sector, every other memory
or controller site behind it).  maxgain = max over t of prior rank - posterior rank (bits learnt
about the toy's current state); maxgain|prior4 the same over the t at which the toy's prior is
uniform on 4 states.
Background (B0: the same graph with every R-H edge removed, same initial state): at the first
learning-type reconstruction time the disturbance D = toy_t - toy_t^B0 is classified as
'none', 'known' (no unknown coordinate), 'in memory' (D_u in span F_u) or 'not in memory'.
"""
import sys
import time
from itertools import combinations
from collections import Counter, defaultdict
from emb_core import (lattice_update, vis_coords, clean_coords, mask_of, post_rank, prior_rank,
                      iso_graphs, toy_rows, order)
from f2 import compose, identity, rank, omega

NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6
DECLS = ("FULL", "U", "V", "NONE")


def solve_in_span(target, basis):
    """Return a combination mask c (bit i = basis[i] used) with xor = target, or None."""
    piv = {}  # highest bit -> (vector, combo)
    for i, b in enumerate(basis):
        v, c = b, 1 << i
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h][0]
                c ^= piv[h][1]
            else:
                piv[h] = (v, c)
                break
    v, c = target, 0
    while v:
        h = v.bit_length() - 1
        if h not in piv:
            return None
        v ^= piv[h][0]
        c ^= piv[h][1]
    return c


def comp_of(n, edges, x):
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen, st = {x}, [x]
    while st:
        y = st.pop()
        for z in adj[y]:
            if z not in seen:
                seen.add(z)
                st.append(z)
    return seen


def main():
    t0 = time.time()
    ctrl = Counter()
    for n in range(2, NMAX + 1):
        graphs = iso_graphs(n)
        tab = defaultdict(Counter)
        firstlearn = {}
        ords = Counter()
        wit = {}
        bt = defaultdict(Counter)
        sbw = {}
        for edges in graphs:
            M = lattice_update(n, edges)
            om = order(M)
            ords[om] += 1
            powers = [identity(2 * n)]
            for t in range(1, om):
                powers.append(compose(M, powers[-1]))
            for r in range(1, n):
                for R in combinations(range(n), r):
                    Rs = set(R)
                    cut = tuple(e for e in edges if (e[0] in Rs) == (e[1] in Rs))
                    M0 = lattice_update(n, cut)
                    om0 = order(M0)
                    p0 = [identity(2 * n)]
                    for t in range(1, om):
                        p0.append(compose(M0, p0[-1]))
                    bin_ = len({a for e in edges for a in e if a in Rs and (set(e) - Rs)})
                    vc = vis_coords(n, R)
                    hid = [c for c in range(2 * n) if c not in vc]
                    for decl in DECLS:
                        K = clean_coords(n, R, decl)
                        um = ((1 << (2 * n)) - 1) & ~mask_of(K)
                        nunk = 2 * n - len(K)
                        for toy in range(n):
                            if toy in Rs:
                                continue
                            conn = bool(comp_of(n, edges, toy) & Rs)
                            bath = any(((a == toy and b not in Rs) or (b == toy and a not in Rs)) for a, b in edges)
                            key = (decl, r, "conn" if conn else "disc")
                            minF = minH = 4
                            tF1 = tH1 = tL = None
                            gmax = gmax2 = 0
                            pers = None
                            T0 = [1 << toy, 1 << (n + toy)]
                            hist = [identity(2 * n)[c] for c in vc]
                            hstable = False
                            for t in range(1, om):
                                P = powers[t]
                                F = [P[c] for c in vc]
                                T = toy_rows(P, n, toy)
                                pf = post_rank(F, T, um)
                                pr = prior_rank(T, um)
                                if decl == "NONE" and pf != pr:
                                    ctrl["NONE"] += 1
                                sF = 2 ** pf
                                minF = min(minF, sF)
                                gmax = max(gmax, pr - pf)
                                if pers is None and pf > 0 and post_rank(F, T0, um) == 0:
                                    pers = t
                                if pr == 2:
                                    gmax2 = max(gmax2, pr - pf)
                                if sF == 1 and tF1 is None:
                                    tF1 = t
                                if sF == 1 and decl == "FULL":
                                    Fs = [f for f in F]
                                    Kb = [1 << c for c in K]
                                    ok = True
                                    ks = []
                                    for g in T:
                                        cmb = solve_in_span(g, Fs + Kb)
                                        if cmb is None:
                                            ok = False
                                            break
                                        k = 0
                                        for i in range(len(Kb)):
                                            if (cmb >> (len(Fs) + i)) & 1:
                                                k ^= Kb[i]
                                        ks.append(k)
                                    if not ok or omega(ks[0], T[1], n) != 1 or omega(ks[1], T[0], n) != 1:
                                        ctrl["SYMP"] += 1
                                    ctrl["SYMP_checked"] += 1
                                if decl == "FULL" and t <= 6:
                                    Hr = [P[c] for c in hid]
                                    if post_rank(F, Hr, um) != nunk - rank([f & um for f in F]):
                                        ctrl["CAP"] += 1
                                if sF == 1 and pr == 2 and tL is None:
                                    tL = t
                                    Tb = toy_rows(p0[t], n, toy)
                                    D = [a ^ b for a, b in zip(T, Tb)]
                                    if all(d == 0 for d in D):
                                        dcls = "none"
                                    elif all(d & um == 0 for d in D):
                                        dcls = "known"
                                    elif rank([f & um for f in F] + [d & um for d in D]) == rank([f & um for f in F]):
                                        dcls = "in memory"
                                    else:
                                        dcls = "not in memory"
                                    tab[key]["dist:" + dcls] += 1
                                if not hstable:
                                    old = rank([h & um for h in hist])
                                    hist = hist + F
                                    if rank([h & um for h in hist]) == old and t > 1:
                                        pass
                                    pH = post_rank(hist, T, um)
                                    if 2 ** pH < minH:
                                        minH = 2 ** pH
                                    if pH == 0 and tH1 is None:
                                        tH1 = t
                            tab[key]["cases"] += 1
                            if conn:
                                bk = (decl, r, bin_)
                                bt[bk]["cases"] += 1
                                bt[bk][f"maxgain={gmax}"] += 1
                                bt[bk][f"maxgain|prior4={gmax2}"] += 1
                                if tL is not None:
                                    bt[bk]["learn"] += 1
                                    if bin_ == 1 and ((decl, r) not in sbw or tL < sbw[(decl, r)][0]):
                                        sbw[(decl, r)] = (tL, edges, R, toy, bath)
                            tab[key][f"minF={minF}"] += 1
                            tab[key][f"minH={minH}"] += 1
                            if tL is not None:
                                tab[key]["learn"] += 1
                                if bath:
                                    tab[key]["learn&bath"] += 1
                                fk = (decl, r)
                                if fk not in firstlearn or (tL, n) < firstlearn[fk][0]:
                                    firstlearn[fk] = ((tL, n), edges, R, toy, bath)
                                if bath and ((decl, r, "bath") not in wit or tL < wit[(decl, r, "bath")][0]):
                                    wit[(decl, r, "bath")] = (tL, edges, R, toy)
                            if pers is not None:
                                tab[key]["persist"] += 1
                                if (decl, "persist") not in wit or (pers, r) < wit[(decl, "persist")][:2]:
                                    wit[(decl, "persist")] = (pers, r, edges, R, toy)
                            if conn and minF > 1:
                                tab[key]["never(conn)"] += 1
        print(f"=== n = {n}: {len(graphs)} graphs up to isomorphism; orders of M: {dict(sorted(ords.items()))}")
        for key in sorted(tab):
            c = tab[key]
            fields = " ".join(f"{k}:{c[k]}" for k in sorted(c))
            print(f"  decl={key[0]:4s} |R|={key[1]} toy {key[2]}: {fields}")
        for fk in sorted(firstlearn):
            (tL, nn), e, R, toy, bath = firstlearn[fk]
            print(f"  earliest learning reconstruction decl={fk[0]} |R|={fk[1]}: t={tL} edges={e} R={R} toy={toy} toy-has-hidden-neighbour={bath}")
        for k in sorted(wit, key=str):
            if k[1] == "persist":
                tp, rr, e, R, toy = wit[k]
                print(f"  earliest 'old record kept, current toy uncertain' (initial toy determined by final memory, current toy support >= 2) decl={k[0]}: t={tp} |R|={rr} edges={e} R={R} toy={toy}")
                continue
            tL, e, R, toy = wit[k]
            print(f"  earliest learning reconstruction with a hidden bath neighbour decl={k[0]} |R|={k[1]}: t={tL} edges={e} R={R} toy={toy}")
        for bk in sorted(bt):
            c = bt[bk]
            print(f"  by inner boundary: decl={bk[0]:4s} |R|={bk[1]} |inner boundary|={bk[2]}: " + " ".join(f"{k}:{c[k]}" for k in sorted(c)))
        for k in sorted(sbw):
            tL, e, R, toy, bath = sbw[k]
            print(f"  earliest learning reconstruction with ONE inner-boundary site (single apparatus) decl={k[0]} |R|={k[1]}: t={tL} edges={e} R={R} toy={toy} toy-has-hidden-neighbour={bath}")
        print(f"  [elapsed {time.time() - t0:.0f} s]", flush=True)
    print("controls:", dict(ctrl))
    green = ctrl["NONE"] == 0 and ctrl["SYMP"] == 0 and ctrl["CAP"] == 0 and ctrl["SYMP_checked"] > 0
    print("E1/E2 CONTROLS:", "GREEN" if green else "RED")


main()
