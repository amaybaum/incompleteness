"""(b) Lifting the card dynamics: which extensions admit a lift of each card map to an automorphism of E that
covers it (and acts trivially on C; inversion on C is reported separately for Z4), and are lifts unique up to
inner automorphisms?  Brute force over all generator images; compared with the class criterion
q o S = q (Z2) / qbar o S = qbar (Z4)."""
from g1lib import *
from itertools import product
from a_classify import reps
n = 2
R = card_relmaps(n); R["phase0"] = relpush(onticmap("phase0", n), n)
for m in (2, 4):
    print("== n=2, C=Z%d" % m)
    admissible = {}
    for eps, b in reps(n, m):
        E = Ext(n, m, b)
        Inn = set(E.inner(g) for g in range(E.size))
        row = {}
        for nm, S in R.items():
            L = E.lifts(S, 1)
            crit = all(E.cval(E.sq(E.el(0, S[u]))) % (2 if m == 4 else m) == E.cval(E.sq(E.el(0, u))) % (2 if m == 4 else m)
                       for u in range(E.N))
            if L:
                L0 = L[0]
                comp = set(tuple(L0[i[g]] for g in range(E.size)) for i in Inn)
                uniq = comp == set(L)
            else: uniq = None
            Linv = E.lifts(S, -1) if m == 4 else []
            row[nm] = (len(L), uniq, crit, len(Linv))
            assert (len(L) > 0) == crit
        tag = "".join(map(str, eps))
        print("  class [squares mod 2 on gens (xA,zA,xB,zB)]=%s |Inn|=%d  " % (tag, len(Inn)) +
              "  ".join("%s:%d lifts%s%s" % (nm, r[0], "" if r[1] is None else (" =L0*Inn" if r[1] else " NOT L0*Inn"),
                                               (" (+%d inverting C)" % r[3]) if m == 4 else "") for nm, r in row.items()))
        admissible[tag] = row
    for fam in (["swap0", "couple"], ["swap0", "swap1", "couple"], ["swap0", "swap1", "couple", "phase0"], ["swap0", "phase0"]):
        ok = [t for t, r in admissible.items() if all(r[nm][0] > 0 for nm in fam)]
        print("  classes admitting lifts of all of %s: %s" % (fam, ok))
