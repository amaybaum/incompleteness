#!/usr/bin/env python3
# fastbath_probes.py — b100 (2026-08-13)
# Two exact certifications about what (C2) does and does not supply to (C4):
#  (A) COUNTEREXAMPLE to the slow-evolution reading: a shift-register bath rotating
#      M=5 cells per visible step (fast autonomous evolution) with deterministic
#      circulation (zero forgetting) and timely return (R=10: the written bit is at
#      the read position two steps later) produces a MAXIMAL order-2 readback gap
#      (delta = 1, TV between the two induced next-step laws): C4 holds while the
#      evolution reading of C2 fails.
#  (B) INSUFFICIENCY of bare persistence: the same construction at R=12, M=5
#      (return time 12, outside the 4-step window) is exactly i.i.d. in-window —
#      no gap at any tested order. Persistence without timely return gives no C4.
# All conclusions are computed from the enumeration; nothing is asserted a priori.
import sys
from fractions import Fraction as F
from itertools import product
from collections import defaultdict

def run(R, M, STEPS=4):
    def step(x, reg):
        reg = list(reg)
        x, reg[0] = reg[0], x
        reg = reg[-M:] + reg[:-M]
        return x, tuple(reg)
    space = [(x, r) for x in (0, 1) for r in product((0, 1), repeat=R)]
    bij = len(set(step(x, r) for x, r in space)) == len(space)
    ens = defaultdict(lambda: F(0))
    for x0 in (0, 1):
        for r in product((0, 1), repeat=R):
            ens[(x0, r, (x0,))] += F(1, 2 ** (R + 1))
    hist_next = defaultdict(lambda: defaultdict(lambda: F(0)))
    for _ in range(STEPS):
        new = defaultdict(lambda: F(0))
        for (x, r, h), p in ens.items():
            x2, r2 = step(x, r)
            hist_next[h][x2] += p
            new[(x2, r2, h + (x2,))] += p
        ens = new
    gaps = []
    hs = sorted(h for h in hist_next if len(h) in (2, 3))
    for i in range(len(hs)):
        for j in range(i + 1, len(hs)):
            a, b = hs[i], hs[j]
            if len(a) == len(b) and a[-1] == b[-1] and a != b:
                Pa, Pb = hist_next[a], hist_next[b]
                na, nb = sum(Pa.values()), sum(Pb.values())
                if na == 0 or nb == 0: continue
                tv = abs(Pa[0] / na - Pb[0] / nb)
                if tv > 0: gaps.append(tv)
    return bij, gaps

fail = 0
print("== (A) fast bath, timely return (R=10, M=5): the slow-evolution reading is not necessary ==")
bij, gaps = run(10, 5)
dmax = max(gaps) if gaps else F(0)
print(f"  bijective: {bij}   in-window gaps found: {len(gaps)}   max delta = {dmax}")
if not (bij and gaps and dmax == 1): fail += 1; print("  FAIL: expected a maximal (delta=1) readback gap")
else: print("  => C4 holds maximally while hidden evolution is FAST (5 rotations per visible step).")

print("== (B) fast bath, late return (R=12, M=5): bare persistence is not sufficient ==")
bij, gaps = run(12, 5)
print(f"  bijective: {bij}   in-window gaps found: {len(gaps)}")
if not (bij and len(gaps) == 0): fail += 1; print("  FAIL: expected zero in-window gaps")
else: print("  => zero forgetting, yet no C4: the record returns at step 12, outside the window.")

print()
print("fastbath_probes:", "ALL CHECKS PASS" if fail == 0 else f"{fail} FAILURE(S)")
sys.exit(1 if fail else 0)
