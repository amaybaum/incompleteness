"""(3) Alternative principles, same hard-to-vary count.
 Alt-1  'records compose associatively (cocycle) and covariantly under the card dynamics (a lift exists), with
         minimal phase group'; the commutator is NOT prescribed.
 Alt-2  'the lifted dynamics is a faithful copy of the card dynamics group' (lifts form a group isomorphic to the
         card group: no new identities, no new operations), on top of the commutator-omega principle."""
from g1lib import *
from a_classify import reps
from itertools import product
from collections import Counter
n = 2; R = card_relmaps(n); card = CardTheory(n); qm = QMTheory(n)
def compose(a, b): return {u: a[b[u]] for u in b}      # a after b
idm = {u: u for u in range(16)}
# card group on V
G = {tuple(idm[u] for u in range(16))}; fr = [idm]
while fr:
    nf = []
    for g in fr:
        for S in R.values():
            h = compose(S, g); k = tuple(h[u] for u in range(16))
            if k not in G: G.add(k); nf.append(h)
    fr = nf
print("card dynamics group <swap_A, swap_B, couple> acting on relation labels: order", len(G))
w = idm
for op in W7: w = compose(R[op], w)
print("card word W7 = swap_A (couple swap_A)^3 ... acts on V as identity:", all(w[u] == u for u in range(16)))
w6 = idm
for op in W6: w6 = compose(R[op], w6)
print("card word W6 acts on V as identity:", all(w6[u] == u for u in range(16)), "; W6 maps Z_B ->", w6[ZB(1)], "(ZA*ZB =", ZB(0) | ZB(1), ")")
# invariant alternating forms
forms = []
for c in range(1 << 6):
    pairs = [(i, k) for i in range(4) for k in range(i+1, 4)]
    def f(u, v, c=c): return sum(((c >> t) & 1) * ((((u >> i) & 1) & ((v >> k) & 1)) ^ (((u >> k) & 1) & ((v >> i) & 1)))
                                 for t, (i, k) in enumerate(pairs)) & 1
    if all(f(S[u], S[v]) == f(u, v) for S in R.values() for u in range(16) for v in range(16)):
        forms.append(c)
print("alternating forms on V invariant under the card group:", len(forms),
      "(omega among them:", any(all(omega(u, v, 2) == (lambda u, v, c=c: sum(((c >> t) & 1) * ((((u >> i) & 1) & ((v >> k) & 1)) ^ (((u >> k) & 1) & ((v >> i) & 1))) for t, (i, k) in enumerate([(i, k) for i in range(4) for k in range(i+1, 4)])) & 1)(u, v) for u in range(16) for v in range(16)) for c in forms), ")")

def tally(E, d, L, label):
    cnt = Counter(); wit = Counter()
    for p0, p1, pc in product(L["swap0"], L["swap1"], L["couple"]):
        T = ExtTheory(E, d, ext_theory_ops(E, d, {"swap0": p0, "swap1": p1, "couple": pc}))
        o6 = run_word(T, W6, "read1"); o7 = run_word(T, W7, "read1")
        wit[(str(dict(o6)), str(dict(o7)))] += 1
        if equivalent(T, qm, ALPH_FULL)[0]: cnt["= QM"] += 1
        elif equivalent(T, card, ALPH_FULL)[0]: cnt["= cards"] += 1
        else: cnt["other"] += 1
    print("  %s: %d choices; full table %s" % (label, sum(cnt.values()), dict(cnt)))
    for k, v in sorted(wit.items()): print("      (W6, W7) = %s : %d" % (k, v))

print("== Alt-1, commutator 0 (abelian), C = Z2: classes = squares map q linear; lifts must preserve q")
for eps, b in reps(n, 2):
    pass
for eps in product((0, 1), repeat=4):
    c = [[0]*4 for _ in range(4)]
    for i in range(4): c[i][i] = eps[i]
    E = Ext(n, 2, bilinear_beta(n, 2, c)); assert E.is_cocycle() and E.commutator_is(lambda u, v: 0)
    L = {nm: E.lifts(S, 1) for nm, S in R.items()}
    if all(L.values()):
        d = default_dict(E)
        print("  class q|gens=%s admits all three; lifts %s; inner automorphisms trivial: %s" % (
            "".join(map(str, eps)), {k: len(v) for k, v in L.items()}, all(E.inner(g) == tuple(range(E.size)) for g in range(E.size))))
        tally(E, d, L, "Alt-1 abelian branch")
print("== Alt-1, commutator omega: the classes/lifts of b_lifts.py / d_witness.py (C = Z2: 1 class x 16^3 lifts)")
print("   minimal C: the trivial group C = 1 admits only commutator 0 => V itself, i.e. the cards; the minimal C")
print("   admitting commutator omega is Z2 (no odd-order C: Hom(Z2, C) = 0).")

print("== Alt-2: faithful (split) lifts of the card group, commutator omega")
for m in (2, 4):
    E = Ext(n, m, bilinear_beta(n, m, real_pauli_coeff(n, m//2))); d = default_dict(E)
    L = {nm: E.lifts(S, 1) for nm, S in R.items()}
    nsplit = 0; split = []
    for p0, p1, pc in product(L["swap0"], L["swap1"], L["couple"]):
        H = {tuple(range(E.size))}; fr = list(H); big = False
        while fr and not big:
            nf = []
            for g in fr:
                for h in (p0, p1, pc):
                    k = tuple(h[g[x]] for x in range(E.size))
                    if k not in H:
                        H.add(k); nf.append(k)
                        if len(H) > len(G): big = True; break
                if big: break
            fr = nf
        if not big and len(H) == len(G): nsplit += 1; split.append((p0, p1, pc))
    print("  C=Z%d: lift triples whose generated group has the card group's order %d (a splitting): %d of %d"
          % (m, len(G), nsplit, len(L["swap0"])*len(L["swap1"])*len(L["couple"])))
    if split:
        Lsp = None
        cnt = Counter(); wit = Counter()
        for p0, p1, pc in split:
            T = ExtTheory(E, d, ext_theory_ops(E, d, {"swap0": p0, "swap1": p1, "couple": pc}))
            wit[(str(dict(run_word(T, W6, "read1"))), str(dict(run_word(T, W7, "read1"))))] += 1
            cnt["= QM" if equivalent(T, qm, ALPH_FULL)[0] else ("= cards" if equivalent(T, card, ALPH_FULL)[0] else "other")] += 1
        print("    full table:", dict(cnt))
        for k, v in sorted(wit.items()): print("      (W6, W7) = %s : %d" % (k, v))
    ert = [ert_lift(E, S, d)[0] for S in (R["swap0"], R["swap1"], R["couple"])]
    Hq = {tuple(range(E.size))}; fr = list(Hq)
    while fr:
        nf = []
        for g in fr:
            for h in ert:
                k = tuple(h[g[x]] for x in range(E.size))
                if k not in Hq: Hq.add(k); nf.append(k)
        fr = nf
    print("    group generated by the ERT (QM-calibration) lifts alone: order %d (card group %d) -> QM's lift is %s"
          % (len(Hq), len(G), "a splitting" if len(Hq) == len(G) else "NOT a splitting"))
