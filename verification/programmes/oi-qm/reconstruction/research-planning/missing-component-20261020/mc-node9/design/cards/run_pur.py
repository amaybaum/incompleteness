"""Task 4: Pur-E and Pur-U in the base card theory (Pi_B), per realization (one shared deck), exact.
Pure = extreme in conv(Prep(AB)) (the strongest reading; extreme implies pure at budget and across the model).
Pur-E: every preparable A-state (heralded marginals, plus the named coarse-herald mixtures) has a pure AB state
with that A-marginal. Pur-U: two pure AB states with the same A-marginal are related by a B-local reversible
operation (permutations of B's slots; content-dependent B-local bijections act trivially on exchangeable states)."""
import itertools
from fractions import Fraction as F
from collections import defaultdict
from cardtheory import *

def coarse_herald_same_colour(deck):
    """exact protocol: burn (reveal) the top two deck cards, keep the run iff they have the same colour,
    then deal a1, a2; discard the rest of the deck. Returns the A-state (a1, a2) or None if impossible."""
    m = Model([deck], {"a": ["a1", "a2"], "b": []})
    dist = m.initial(); keep = defaultdict(F)
    for st, p in dist.items():
        o1, s1 = m.apply(("peekdeck", 0), st); o2, s2 = m.apply(("peekdeck", 0), s1)
        if o1 != o2: continue
        _, s3 = m.apply(("deal", "a1", 0), s2); _, s4 = m.apply(("deal", "a2", 0), s3)
        keep[(s4[0][0], s4[0][1])] += p
    tot = sum(keep.values())
    return ({k: v / tot for k, v in keep.items()}, tot) if tot else (None, 0)

print("== exact obstruction check: 2-slot marginal of E(M), |M| = n, r red: P(RR) <= P(a1=R)^2, equality iff r in {0,n} ==")
ok = True
for n in range(2, 13):
    for r in range(0, n + 1):
        prr = F(r * (r - 1), n * (n - 1)); pr = F(r, n)
        if not (prr <= pr * pr and ((prr == pr * pr) == (r in (0, n)))): ok = False
        # brute force against the formula for n <= 7
        if n <= 7:
            seqs = set(itertools.permutations([0] * r + [1] * (n - r)))
            bf = F(sum(1 for s in seqs if s[0] == 0 and s[1] == 0), len(seqs))
            assert bf == prr, (n, r)
print("  holds for n = 2..12:", ok, "(formula brute-forced for n <= 7)")

print("\n== Pur-E / Pur-U, base theory, decks n = 2..6 (two colours), A in {1,2} slots, B in {1,2} slots ==")
REASONS = defaultdict(int); tot_rows = 0; purE_fail_rows = 0; purU_fail_rows = 0
summary = []
for n in range(2, 7):
    for r in range(1, n):
        for na in (1, 2):
            for nb in (1, 2, 3):
                if n < na + nb: continue
                if nb == 3 and na == 2: continue
                A = [f"a{i+1}" for i in range(na)]; B = [f"b{i+1}" for i in range(nb)]
                m = Model([(r, n - r)], {"a": A, "b": B})
                nodes, depth, bp, st = closure(m)
                extra = []
                if na == 2 and n >= 4:
                    s, pr = coarse_herald_same_colour((r, n - r))
                    if s: extra.append(s)
                print(f"  deck={r}R{n-r}B A={na} B={nb}{' (beyond bound)' if nb == 3 else ''}: {st['status']}@{st['depth']}")
                res = pur_analysis(m, A, B, nodes, depth, extra_states=extra)
                tot_rows += 1
                purE_fail_rows += res["purE_have"] < res["purE_total"]
                purU_fail_rows += res["purU_unconnected"] > 0
                summary.append((f"{r}R{n-r}B", na, nb, res["purE_have"], res["purE_total"], res["purU_pairs"], res["purU_unconnected"]))
                for k, v in res["reasons"].items(): REASONS[k] += v
allreasons = defaultdict(int)
for s in summary: pass
print(f"\n  SUMMARY: realizations={tot_rows}; with a Pur-E failure={purE_fail_rows}; with an unconnected Pur-U pair={purU_fail_rows}")
print("  same-type purifier (A=1,B=1 and A=2,B=2) Pur-E failures:",
      sum(1 for s in summary if s[1] == s[2] and s[3] < s[4]), "of", sum(1 for s in summary if s[1] == s[2]))
print("  total Pur-U pairs tested:", sum(s[5] for s in summary))

print("  obstruction classes over all realizations:"); [print(f"    {k}: {v}") for k, v in sorted(REASONS.items())]
