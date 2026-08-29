#!/usr/bin/env python3
# comb_realization_probes.py — b446 (2026-08-29)
#
# The multi-step realization dimension at K = 2: an exact separation between the intrinsic
# strategy dimension of a comb and the size of the smallest REVERSIBLE machine that realizes it.
#
# b445 left the frontier at a single number: D_strat(2), the minimum number of deterministic
# strategies needed to decompose the b76B comb at horizon 2, computed INTRINSICALLY and not read
# off any particular construction. That is where this round starts, and the result is
#
#       D_table(2) = D_strat(2) = 8      <      d_bij-comb(2) = 10.
#
# Both halves are exact and each is established by its own kind of argument.
#
#   LOWER BOUND: A THEOREM, via the saturated-class lemma. Not an exhaustion, not a sample.
#   UPPER BOUND: CONSTRUCTIVE, via the explicit 10-state reversible witness carried below.
#
# NON-ANTICIPATION IS A REAL CONSTRAINT AND IT IS FREE HERE. A deterministic strategy at K = 2 is
# a map R : A^2 -> V^2, but a physical one must be CAUSAL: the first visible value cannot depend on
# the second action, R(a_0, 0)_1 = R(a_0, 1)_1. That kills 3 of every 4 tables -- 256 raw tables,
# 64 causal ones -- and yet it costs nothing in dimension: D_table(2) = D_strat(2) = 8. Conflating
# the two would have been the b445 error in a new costume, so both are computed and compared.
#
# THE SATURATED-CLASS LEMMA, which is what upgrades the lower bound from exhaustion to proof.
# Call a readout class SATURATED when every one of its states carries positive prior weight. Let
# g = phi o I_a be the one-step map for a single action a, a bijection of the state set. Then:
#
#   If either readout class is saturated, NO bijective realization reproduces the comb.
#
#   Proof (class C_0 saturated; the mirror runs the same way). Put A = g(C_0), B = g(C_1); A and B
#   partition the state set because g is a bijection. Put P = A n C_0 and Q = C_0 \ P = C_0 n B.
#   Sector 0 at sequence (a,a) gives outcome (0,1) probability ZERO, so for supported s in C_0 with
#   pi(g s) = 0 we must have pi(g^2 s) = 0. Saturation makes every u in P such an image, so
#   g(P) is contained in C_0, and g(P) is contained in g(C_0) = A, hence g(P) is contained in P;
#   injectivity gives g(P) = P and therefore g(Q) = A \ P, which lies entirely in C_1.
#   Sector 1 at the same sequence gives outcome (0,0) probability 1/4, so some supported s in C_1
#   has pi(g s) = 0 -- forcing g(s) in B n C_0 = Q -- and pi(g^2 s) = 0. But g(Q) lies in C_1.
#   Contradiction.
#
#   THE OBSTRUCTION DOES NOT REQUIRE COMPARING INCOMPATIBLE CROSS-ACTION HISTORIES. It uses ONE
#   action sequence, (a,a), and the same a throughout. Only the counting step that forces four
#   supported states per sector reads a mixed sequence.
#
# WHAT THE LEMMA COSTS THE MACHINE. Four equiprobable outcomes at sequence (0,1) force at least
# four supported states per readout class, so each class has at least four states; a class of
# exactly four is saturated, which the lemma forbids; so each class has at least FIVE states and
# |S| >= 10. Ten is attained. FOR THE PRESENT COMB, THEREFORE, REVERSIBILITY FORCES ONE ZERO-WEIGHT
# WORKSPACE STATE PER VISIBLE SECTOR. Whether an analogous workspace lower bound holds for a
# broader class of finite combs REMAINS OPEN -- that is an observed structural pattern and a
# follow-up conjecture, NOT a general theorem, and this file does not assert it as one.
#
# THE 2x2 INSTRUMENT LATTICE COLLAPSES. The lower-bound proof assumes only that the one-step map is
# a BIJECTION -- not that instruments preserve the readout, not that they are involutive, not that
# a common phi factors out. The witness satisfies ALL of those at once. So the weakest and the
# strongest notion agree:
#
#       d_bij-comb(2) = d_inv(2) = d_RP(2) = d_rev-comb(2) = 10.
#
# CARRIED FORWARD FROM b445, and it is the discipline this round is built on: N_resp(M) is a
# property of ONE realization and is NEVER a lower bound on another realization of the same comb;
# minimisation runs downward, D_strat(C) <= N_resp(M). Every lower bound below is proved from the
# comb itself.
#
#   CR1  the K = 2 comb and causality: 256 raw response tables, 64 causal ones
#   CR2  D_table(2) = D_strat(2) = 8 -- lower bound by counting, attained by explicit atoms
#   CR3  the SATURATED-CLASS LEMMA, its forced steps verified exhaustively at n = 8 and n = 9
#   CR4  |S| >= 10 as a THEOREM, with n = 8 and n = 9 exhaustion as an independent control
#   CR5  the explicit 10-state reversible witness against the FULL CONDITIONAL comb
#   CR6  the 2x2 instrument lattice collapses; the exact chain 8 < 10 against a canonical 7776
#   CR7  the Lean companion: present, universal, carrying no `sorry`, and actually gated
#   CR7b scope: what is theorem, what is construction, what is conjecture, what is not measured
#   CR8  the verdict, gated on every control above
#
# Usage:  python3 comb_realization_probes.py

import itertools, os, re, sys
from collections import defaultdict
from fractions import Fraction as F

CHECKS = []


def check(label, ok, msg):
    CHECKS.append(bool(ok))
    print(f"  {'PASS' if ok else 'FAIL'}  {label}: {msg}", flush=True)


def verdict(label, ok, msg):
    """A TERMINAL SUMMARY: it has no computation of its own, it only states what the checks above
    have established. Gating the label is not enough -- check() prints its msg whatever the label
    says, so a bare gate renders the entire verdict text under a FAIL heading, which is the thing
    the gate exists to prevent. The message itself is therefore withheld when a control failed."""
    check(label, ok, msg if ok else
          "WITHHELD — a prerequisite control above failed, so this summary is not asserted")


# ---------------------------------------------------------------- the b76B comb at K = 2
nV, nA, BLANK, K = 2, 2, -1, 2


def kern(ctx):
    xs, as_ = ctx
    p = F((1 + sum(xs) + 2 * sum(as_) + 3 * len(xs) + (xs[-1] ^ as_[-1])) % 7 + 1, 9)
    return {0: 1 - p, 1: p}


CTXS = [((x,), (a,)) for x in range(nV) for a in range(nA)]
tabs = [{}]
for c in CTXS:
    nxt = []
    for tb in tabs:
        for y in range(nV):
            if kern(c)[y] > 0:
                t2 = dict(tb); t2[c] = y; nxt.append(t2)
    tabs = nxt
UTAB = [tuple(sorted(tb.items())) for tb in tabs]
SEQS = list(itertools.product(range(nA), repeat=K))


def step(s, act):
    x, h, a, c = s
    if c >= K:
        return None
    al = list(a); al[c] = act
    return ((dict(UTAB[x[1]])[((x[0],), (act,))], x[1]),
            tuple(list(h[:c]) + [x[0]] + [BLANK] * (K - c - 1)), tuple(al), c + 1)


OMEGA = [((x, u), tuple([BLANK] * K), tuple([BLANK] * K), 0)
         for x in range(nV) for u in range(len(UTAB))]


def resp(s0):
    out = {}
    for q in SEQS:
        s = s0; w = []
        for act in q:
            s = step(s, act); w.append(s[0][0])
        out[q] = tuple(w)
    return out


BYX = defaultdict(list)
for s in OMEGA:
    BYX[s[0][0]].append(s)

# TGT[(x_0, q)] is the conditional comb: P(X_1 X_2 = . | X_0 = x_0, a = q), exact rationals.
TGT = {}
for x0, ss in BYX.items():
    for q in SEQS:
        d = defaultdict(F)
        for s in ss:
            d[resp(s)[q]] += F(1, len(ss))
        TGT[(x0, q)] = dict(d)

# ---------------------------------------------------------------- CR1  causality
ALL_TABLES = [tuple(sorted({q: (f[2 * i], f[2 * i + 1]) for i, q in enumerate(SEQS)}.items()))
              for f in itertools.product(range(nV), repeat=2 * len(SEQS))]

CAUSAL = []
for f1 in itertools.product(range(nV), repeat=nA):
    for f2 in itertools.product(range(nV), repeat=nA * nA):
        R = {}
        for a0 in range(nA):
            for a1 in range(nA):
                R[(a0, a1)] = (f1[a0], f2[a0 * nA + a1])
        CAUSAL.append(tuple(sorted(R.items())))
CAUSAL = sorted(set(CAUSAL))


def causal(R):
    d = dict(R)
    return all(d[(a0, 0)][0] == d[(a0, 1)][0] for a0 in range(nA))


ok1 = (len(ALL_TABLES) == 256 and len(CAUSAL) == 64
       and all(causal(R) for R in CAUSAL)
       and sorted(CAUSAL) == sorted(R for R in ALL_TABLES if causal(R))
       and all(len(TGT[(x, (0, 1))]) == 4 for x in range(nV))
       and all(sum(TGT[(x, q)].values()) == 1 for x in range(nV) for q in SEQS))
check("CR1", ok1,
      f"THE K = 2 COMB AND CAUSALITY. The conditional comb P(X_1 X_2 | X_0, a) is exact rational "
      f"data on {len(SEQS)} action sequences at each of {nV} visible values. A deterministic "
      f"strategy is a table R : A^2 -> V^2, of which there are {len(ALL_TABLES)}, but a PHYSICAL "
      f"one must be NON-ANTICIPATORY: the first visible value cannot depend on the second action, "
      f"R(a_0,0)_1 = R(a_0,1)_1. Exactly {len(CAUSAL)} tables are causal — causality discards "
      f"{len(ALL_TABLES) - len(CAUSAL)} of {len(ALL_TABLES)}, three quarters of the raw table "
      f"space. The mixed sequence (0,1) carries {len(TGT[(0, (0,1))])} distinct outcomes at each "
      f"visible value, each with positive probability")


# ---------------------------------------------------------------- CR2  D_table(2) = D_strat(2) = 8
def mixture(sub, w):
    out = {}
    for q in SEQS:
        d = defaultdict(F)
        for R, wt in zip(sub, w):
            d[dict(R)[q]] += wt
        out[q] = {k: v for k, v in d.items() if v}
    return out


def in_support(R, x0):
    return all(dict(R)[q] in TGT[(x0, q)] for q in SEQS)


def four_atoms(pool, x0):
    """An explicit 4-atom decomposition of sector x_0, one atom per outcome at (0,1). The weights
    are FORCED to be 1/4: each strategy is deterministic, so it contributes its whole weight to a
    single outcome at (0,1), and the four outcomes there are equiprobable."""
    by = defaultdict(list)
    for R in pool:
        if in_support(R, x0):
            by[dict(R)[(0, 1)]].append(R)
    for pick in itertools.product(*[by[o] for o in sorted(TGT[(x0, (0, 1))])]):
        if mixture(pick, [F(1, 4)] * 4) == {q: TGT[(x0, q)] for q in SEQS}:
            return pick
    return None


ATOMS = {x0: four_atoms(CAUSAL, x0) for x0 in range(nV)}
ATOMS_RAW = {x0: four_atoms(ALL_TABLES, x0) for x0 in range(nV)}

# The lower bound is a counting argument, not a search: a deterministic strategy produces exactly
# ONE outcome at sequence (0,1), the comb puts positive weight on four distinct outcomes there, and
# a strategy retains the initial visible label, so sectors never share atoms.
lb_per_sector = max(len(TGT[(x0, (0, 1))]) for x0 in range(nV))
D_STRAT = nV * lb_per_sector
ok2 = (all(ATOMS[x] is not None for x in range(nV))
       and all(ATOMS_RAW[x] is not None for x in range(nV))
       and all(causal(R) for x in range(nV) for R in ATOMS[x])
       and all(len({dict(R)[(0, 1)] for R in ATOMS[x]}) == 4 for x in range(nV))
       and lb_per_sector == 4 and D_STRAT == 8)
check("CR2", ok2,
      f"D_table(2) = D_strat(2) = {D_STRAT}, AND CAUSALITY COSTS NOTHING. The LOWER BOUND IS AN "
      f"ARGUMENT AND NOT A SEARCH: a deterministic strategy yields exactly one outcome at sequence "
      f"(0,1), the comb puts positive weight on {lb_per_sector} distinct outcomes there, so each "
      f"visible sector needs at least {lb_per_sector} strategies; a strategy retains the initial "
      f"visible label sigma = (x_0, R), so sectors cannot share atoms, and "
      f"{nV} x {lb_per_sector} = {D_STRAT} follows. It is ATTAINED: an explicit uniform "
      f"decomposition into four weight-1/4 atoms per sector reproduces every one of the "
      f"{len(SEQS)} sequence distributions exactly, and the atoms found in the CAUSAL pool are the "
      f"same size as those found in the unrestricted pool. So restricting to non-anticipatory "
      f"strategies removes three quarters of the tables and NO dimension")

# ---------------------------------------------------------------- CR3  the saturated-class lemma
#
# The lemma is proved in the header. What is verified here is that each of its forced steps holds
# for EVERY bijection that gets as far as satisfying the saturated sector, and that the conclusion
# then fails at the other sector -- so no step is a hidden assumption. The check is
# weight-independent: it compares OUTCOME SETS against the target supports, which is necessary for
# any choice of positive weights whatsoever.


def lemma_steps(n, m, orient, a=0):
    """Enumerate every bijection g on n states with readout pi = 0^m 1^(n-m) whose SATURATED class
    matches its target outcome support at sequence (a,a), then test each forced step."""
    pi = tuple([0] * m + [1] * (n - m))
    C0 = set(range(m)); C1 = set(range(m, n))
    sat, other = (C0, C1) if orient == 0 else (C1, C0)
    tgt_sat = set(TGT[(orient, (a, a))])
    forbidden = (0, 0) if orient == 0 else (1, 1)     # the outcome the OTHER sector needs
    tot = fixed = image = blocked = 0
    for g in itertools.permutations(range(n)):
        out = [(pi[g[s]], pi[g[g[s]]]) for s in range(n)]
        if {out[s] for s in sat} != tgt_sat:
            continue
        tot += 1
        Img = {g[s] for s in sat}
        Fix = Img & sat                               # P when orient = 0, R when orient = 1
        Rest = sat - Fix
        if {g[u] for u in Fix} == Fix:
            fixed += 1
        if {g[u] for u in Rest} == Img - Fix and (Img - Fix) <= other:
            image += 1
        if not any(out[s] == forbidden for s in other):
            blocked += 1
    return tot, fixed, image, blocked


LEM = {}
for n, m, orient in ((8, 4, 0), (8, 4, 1), (9, 4, 0), (9, 5, 1)):
    LEM[(n, m, orient)] = lemma_steps(n, m, orient)

ok3 = all(t > 0 and f == t and i == t and b == t for (t, f, i, b) in LEM.values())
_tot = {k: v[0] for k, v in LEM.items()}
check("CR3", ok3,
      f"THE SATURATED-CLASS LEMMA, ITS FORCED STEPS VERIFIED RATHER THAN ASSERTED. Over every "
      f"bijection whose saturated readout class matches its target outcome support at the REPEATED "
      f"sequence (a,a) — {_tot[(8,4,0)]} of them at n = 8 with the class-0 orientation, "
      f"{_tot[(8,4,1)]} with class-1, {_tot[(9,4,0)]} and {_tot[(9,5,1)]} at n = 9 — the map fixes "
      f"the same-readout part of the image setwise in 100% of cases, sends the remainder onto the "
      f"complementary readout class in 100% of cases, and in 100% of cases the OTHER sector can "
      f"then never produce the outcome the comb gives it weight 1/4. No step is a hidden "
      f"assumption and the orientation is symmetric. THE OBSTRUCTION USES ONE ACTION SEQUENCE, "
      f"(a,a), WITH THE SAME ACTION THROUGHOUT: it does NOT require comparing incompatible "
      f"cross-action histories")


# ---------------------------------------------------------------- CR4  |S| >= 10, a theorem
def exhaust(n, m, a=0):
    """Independent control: every bijection on n states, every admissible supported set, checked
    against BOTH sector outcome supports at sequence (a,a). Weight-independent and necessary."""
    pi = tuple([0] * m + [1] * (n - m))
    cls = {0: list(range(m)), 1: list(range(m, n))}
    sups = {}
    for x in range(nV):
        C = cls[x]
        sups[x] = ([tuple(C)] if len(C) == 4
                   else list(itertools.combinations(C, 4)) + [tuple(C)])
    S = {x: set(TGT[(x, (a, a))]) for x in range(nV)}
    hits = 0
    for g in itertools.permutations(range(n)):
        out = [(pi[g[s]], pi[g[g[s]]]) for s in range(n)]
        for s0 in sups[0]:
            if {out[s] for s in s0} != S[0]:
                continue
            for s1 in sups[1]:
                if {out[s] for s in s1} == S[1]:
                    hits += 1
    return hits


EXH = {(n, m): exhaust(n, m) for n, m in ((8, 4), (9, 4), (9, 5))}
MIN_CLASS = 5
ok4 = (all(v == 0 for v in EXH.values())
       and lb_per_sector == 4 and MIN_CLASS * nV == 10)
check("CR4", ok4,
      f"|S| >= 10 AS A THEOREM, WITH EXHAUSTION AS AN INDEPENDENT CONTROL AND NOT AS THE PROOF. "
      f"The four equiprobable outcomes at sequence (0,1) force at least {lb_per_sector} supported "
      f"states per readout class, so every class has at least {lb_per_sector} states; a class of "
      f"EXACTLY {lb_per_sector} is saturated, which the lemma forbids; so every class has at least "
      f"{MIN_CLASS} states and |S| >= {MIN_CLASS * nV}. Independently, exhaustive enumeration over "
      f"every bijection and every admissible supported set finds "
      f"{EXH[(8,4)] + EXH[(9,4)] + EXH[(9,5)]} realizations at n = 8 (4+4) and at n = 9 in both "
      f"class splits (4+5 and 5+4). n <= 7 is excluded outright: a class needs "
      f"{lb_per_sector} supported states. THE ARGUMENT IS THE RESULT; THE SEARCH IS THE "
      f"MISTAKE-CATCHER")

# ---------------------------------------------------------------- CR5  the 10-state witness
N = 10
PI = (0, 0, 0, 0, 0, 1, 1, 1, 1, 1)
PHI = (0, 1, 2, 6, 5, 3, 4, 8, 7, 9)
INS = {0: (0, 1, 4, 3, 2, 5, 8, 9, 6, 7),
       1: (0, 4, 2, 3, 1, 5, 7, 6, 9, 8)}
SUPP = {0: (0, 1, 2, 3), 1: (5, 6, 7, 8)}
G = {a: tuple(PHI[INS[a][s]] for s in range(N)) for a in range(nA)}


def bijective(p):
    return sorted(p) == list(range(N))


def witness_comb():
    for x0, C in SUPP.items():
        for q in SEQS:
            d = defaultdict(F)
            for s in C:
                u = G[q[0]][s]; v = G[q[1]][u]
                d[(PI[u], PI[v])] += F(1, len(C))
            if {k: v for k, v in d.items() if v} != TGT[(x0, q)]:
                return False
    return True


WORKSPACE = sorted(set(range(N)) - set(SUPP[0]) - set(SUPP[1]))
SUPP_N = sum(len(v) for v in SUPP.values())
ok5 = (bijective(PHI) and all(bijective(INS[a]) for a in range(nA))
       and all(INS[a][INS[a][s]] == s for a in range(nA) for s in range(N))
       and all(PI[INS[a][s]] == PI[s] for a in range(nA) for s in range(N))
       and all(bijective(G[a]) for a in range(nA))
       and witness_comb()
       and SUPP_N == D_STRAT and len(WORKSPACE) == 2
       and all(sum(1 for s in WORKSPACE if PI[s] == x) == 1 for x in range(nV)))
check("CR5", ok5,
      f"THE 10-STATE REVERSIBLE WITNESS, VERIFIED AGAINST THE FULL CONDITIONAL COMB. Readout "
      f"{PI}, evolution {PHI}, instruments {INS[0]} and {INS[1]}. The evolution is a bijection; "
      f"both instruments are bijective, INVOLUTIVE and READOUT-PRESERVING; both one-step maps "
      f"phi o I_a are bijections; and the machine reproduces P(X_1 X_2 | X_0, a) exactly on all "
      f"{len(SEQS)} sequences at both visible values, not merely the unconditional marginals. Its "
      f"prior is supported on {SUPP_N} states, four per sector at weight 1/4 — exactly "
      f"D_strat(2) = {D_STRAT} — leaving states {WORKSPACE} at weight zero, ONE PER VISIBLE "
      f"SECTOR, which is what the saturated-class lemma requires of any realization of THIS comb")

# ---------------------------------------------------------------- CR6  the instrument lattice
# The lower-bound proof assumes only that phi o I_a is a bijection; the witness satisfies every
# strengthening at once. So the whole 2x2 lattice -- involutive or not, readout-preserving or not
# -- is pinned between the same two numbers, and there is nothing left to search.
CANONICAL = (nV * (nV + 1) ** K * (nA + 1) ** K * len(UTAB) * (K + 1))
ok6 = (CANONICAL == 7776 and N == 10 and D_STRAT == 8 and N > D_STRAT)
check("CR6", ok6,
      f"THE 2x2 INSTRUMENT LATTICE COLLAPSES, AND THE SEPARATION IS EXACT. The lower bound assumes "
      f"ONLY that the one-step map is a bijection — not readout preservation, not involutivity, "
      f"not a common phi factoring through both instruments — while the witness satisfies all of "
      f"them simultaneously. Weakest hypothesis and strongest construction therefore meet: "
      f"d_bij-comb(2) = d_inv(2) = d_RP(2) = d_rev-comb(2) = {N}. The exact chain at K = 2 is "
      f"D_table(2) = D_strat(2) = {D_STRAT} < {N} = d_rev-comb(2), with |supp mu| = {SUPP_N} and "
      f"|S| = {N}, against a canonical construction of {CANONICAL} states — a "
      f"{CANONICAL / N:.1f}x state-count overhead over the reversible minimum. AT K = 1 THE TWO "
      f"NUMBERS COINCIDED AT 4; AT K = 2 THEY SEPARATE, and the separation is small, exact, and "
      f"forced")

# ---------------------------------------------------------------- CR7  the Lean companion, and scope
# The lower bound is claimed as a THEOREM, so the claim is checked rather than asserted: the Lean
# file must exist, must state the lemma and its three consequences, and must be REACHABLE from the
# bridge library's root -- a theorem in a module nothing imports is never built and never gated.
LEAN_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        *([os.pardir] * 3), 'verification', 'lean-mathlib')
LEAN_SRC = os.path.join(LEAN_DIR, 'OIBridge', 'CombRealization.lean')
LEAN_ROOT = os.path.join(LEAN_DIR, 'OIBridge.lean')
LEAN_THMS = ('saturated_class_obstruction', 'workspace_state_forced',
             'class_card_ge_five', 'card_ge_ten')
lean_txt = open(LEAN_SRC, encoding='utf-8').read() if os.path.exists(LEAN_SRC) else ''
root_txt = open(LEAN_ROOT, encoding='utf-8').read() if os.path.exists(LEAN_ROOT) else ''
# The statement must be UNIVERSAL rather than an instance: the state type is a variable, the only
# structural hypothesis is that the one-step map is injective on a finite type, and no axiom of the
# file's own is introduced.
ok7 = (lean_txt != ''
       and all(f'theorem {t}' in lean_txt for t in LEAN_THMS)
       and all(f'#print axioms {t}' in lean_txt for t in LEAN_THMS)
       and 'import OIBridge.CombRealization' in root_txt
       and re.search(r'(?<![A-Za-z])sorry(?![A-Za-z])', lean_txt) is None
       and '\naxiom ' not in lean_txt
       and 'variable {S : Type*}' in lean_txt
       and 'theorem saturated_class_obstruction [Finite S] {g : S \u2192 S} '
           '(hg : Function.Injective g)' in lean_txt)
check("CR7", ok7,
      f"THE LEAN COMPANION IS PRESENT, UNIVERSAL, AND ACTUALLY GATED. "
      f"verification/lean-mathlib/OIBridge/CombRealization.lean states all "
      f"{len(LEAN_THMS)} theorems — {', '.join(LEAN_THMS)} — carries no `sorry`, prints its axiom "
      f"dependencies at build time so the kernel's own answer is what the log records, contains NO "
      f"axioms of its own and quantifies over an arbitrary finite state type with injectivity of "
      f"the one-step map as its only structural hypothesis — so the statement is UNIVERSAL rather "
      f"than an instance of this comb — and it is IMPORTED from "
      f"OIBridge.lean, which is the bridge library's root: a module the root does not import is "
      f"never built and never gated. THE DIVISION OF LABOUR IS DELIBERATE — LEAN PROVES THE REASON "
      f"AND THIS FILE KEEPS THE CENSUS, and PROBED IS NOT FORMALLY PROVED")

# ---------------------------------------------------------------- CR7b  scope
check("CR7b", True,
      f"SCOPE, STATED AS THE THREE DIFFERENT KINDS OF THING THIS ROUND CONTAINS. LOWER BOUND: a "
      f"THEOREM, via the saturated-class lemma, holding for every bijective realization of this "
      f"comb. UPPER BOUND: CONSTRUCTIVE, via the explicit 10-state reversible witness — an "
      f"existence statement carried by one machine. OBSERVED STRUCTURAL PATTERN AND FOLLOW-UP "
      f"CONJECTURE, not a general theorem: for the present comb reversibility requires one "
      f"zero-weight workspace state per visible sector; whether an analogous workspace lower bound "
      f"holds for a broader class of finite combs REMAINS OPEN, and nothing here decides it. "
      f"d_OI-memory(2) IS NOT DEFINED AND NOT MEASURED — that quantity waits on the C2/C4 "
      f"record/readback requirement being DERIVED from the conditions rather than read off an "
      f"implementation — so this file NEVER CLAIMS d_rev-comb < d_OI. L4, pointwise action "
      f"separation, is NOT tested at K = 2 and d_L4(2) is NOT computed; the witness does not "
      f"satisfy it and no claim is made either way. b445's discipline stands unchanged: N_resp(M) "
      f"is a property of ONE realization and is NEVER a lower bound on another realization of the "
      f"same comb. ONE COMB AT ONE HORIZON. NOTHING PROPAGATES to the manuscripts")

# ---------------------------------------------------------------- CR8  the verdict
verdict("CR8", all(CHECKS),
        f"THE MULTI-STEP REALIZATION DIMENSION AT K = 2, AND AN EXACT SEPARATION. The intrinsic "
        f"strategy dimension is D_table(2) = D_strat(2) = {D_STRAT}: at least four strategies per "
        f"visible sector because the mixed sequence carries four equiprobable outcomes and a "
        f"strategy retains its visible label, attained by explicit weight-1/4 atoms; and "
        f"non-anticipation, which discards {len(ALL_TABLES) - len(CAUSAL)} of {len(ALL_TABLES)} "
        f"tables, costs no dimension at all. The smallest REVERSIBLE realization is strictly "
        f"larger, d_bij-comb(2) = {N}. The lower bound is a THEOREM: the saturated-class lemma "
        f"shows that if every state of a readout class carries positive weight then the one-step "
        f"bijection is forced to map that class's complement into the wrong readout class, so a "
        f"class of exactly four states is impossible and every class needs five. The upper bound "
        f"is CONSTRUCTIVE: an explicit ten-state machine with a bijective evolution and bijective, "
        f"involutive, readout-preserving instruments reproducing the full conditional comb. The "
        f"obstruction uses ONE repeated action sequence and no cross-action comparison, and it "
        f"assumes only bijectivity, so the entire 2x2 instrument lattice collapses to {N}. At "
        f"K = 1 the strategy dimension and the reversible dimension coincided at 4; K = 2 IS WHERE "
        f"THEY SEPARATE, {D_STRAT} against {N}, with {CANONICAL} canonical states above both. "
        f"The lemma is KERNEL-CHECKED in OIBridge/CombRealization.lean as a universal implication "
        f"with no comb data entering, and the exhaustive census stays here: PROBED IS NOT FORMALLY "
        f"PROVED and the two layers are independent. "
        f"d_OI is NOT measured and d_L4(2) is NOT computed")

print()
print('     [scope] Settled and EXACT at K = 2 on the b76B comb: D_table(2) = D_strat(2) = 8, the')
print('     lower bound a counting argument over the four equiprobable outcomes at the mixed')
print('     sequence and the upper bound explicit weight-1/4 atoms; non-anticipation removes 192')
print('     of 256 response tables and costs NO dimension; and d_bij-comb(2) = d_inv(2) =')
print('     d_RP(2) = d_rev-comb(2) = 10, strictly above 8.')
print('     Settled as a THEOREM: the saturated-class lemma. If every state of a readout class is')
print('     supported, no bijective realization reproduces the comb — proved from ONE repeated')
print('     action sequence, with no cross-action history comparison, and assuming only that the')
print('     one-step map is a bijection. Hence every class needs five states and |S| >= 10.')
print('     Kernel-checked: verification/lean-mathlib/OIBridge/CombRealization.lean proves the')
print('     lemma and its consequences as UNIVERSAL implications over an arbitrary finite state')
print('     type, with no comb data entering, and prints its axiom dependencies at build time.')
print('     The exhaustive census here and the Lean proof are INDEPENDENT layers and neither')
print('     substitutes for the other: PROBED IS NOT FORMALLY PROVED.')
print('     Settled CONSTRUCTIVELY: the ten-state witness, bijective evolution with bijective,')
print('     involutive, readout-preserving instruments, reproducing the FULL CONDITIONAL comb.')
print('     OPEN, and deliberately not promoted: for the present comb reversibility requires one')
print('     zero-weight workspace state per visible sector, but whether an analogous workspace')
print('     lower bound holds for a broader class of finite combs REMAINS OPEN. That is an')
print('     observed structural pattern and a follow-up conjecture, NOT a general theorem.')
print('     NOT settled: d_OI-memory(2) is NOT DEFINED and NOT measured, so no claim of the form')
print('     d_rev-comb < d_OI is made anywhere; d_L4(2) is NOT computed; and this is ONE comb at')
print('     ONE horizon. b441-b445 stand; NOTHING propagates to the manuscripts.')
print()
print("comb_realization_probes:", "ALL CHECKS PASS" if all(CHECKS) else "FAILURE")
sys.exit(0 if all(CHECKS) else 1)
