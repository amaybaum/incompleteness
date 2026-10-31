"""Explicit countermodel families.  python3 -I -B run_families.py"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as F
from oi_exact import analyze, divisor, identity, is_perm
from families import xor22, static_shift, lfsr, swap22

def show(M, nmax=None, quiet_windows=False):
    recs, gaps = analyze(M, nmax=nmax)
    print(f'== {M.name}: nV={M.nV} nH={M.nH} L={M.L} r={M.r} static_bath={M.static_bath()} '
          f'T=Gamma_1 perm={is_perm(M.Gamma(1))}')
    for k, (g, wit, c2s) in gaps.items():
        if g > 0:
            p1, p2, l1, l2 = wit
            print(f'   gap at order k={k}: TV={g}  histories {p1} vs {p2}  next laws {[str(v) for v in l1]} vs {[str(v) for v in l2]}  C2s={c2s}')
            break
    cm = []
    for rec in recs:
        is_cm = rec['C1'] and rec['C2s'] and rec['C3'] and rec['C4']
        line = (f"   n={rec['n']:3d}: C1={rec['C1']} C1hist={rec['C1hist']} C2s={rec['C2s']} C3={rec['C3']}"
                f"(sat={rec['C3sat']}) C4={rec['C4']} orders={rec['c4_orders'][:3]} | R1={rec['R1']} R2={rec['R2']} R3={rec['R3']} R4={rec['R4']}")
        if not quiet_windows or rec is recs[0] or rec is recs[-1]:
            print(line)
        if is_cm:
            cm.append((rec['n'], [R for R in ('R1', 'R2', 'R3', 'R4') if rec[R]]))
    if cm:
        print(f'   countermodel windows: n in [{cm[0][0]}..{cm[-1][0]}] ; readings divisible at largest n: {cm[-1][1]}')
    # recurrence-cycle control: R1 must fail on {0..r}
    nonperm = any(not is_perm(M.Gamma(s)) for s in range(1, M.r))
    fail_r = any(not divisor(M.Gamma(s), M.Gamma(M.r))[0] for s in range(1, M.r))
    print(f'   control: some Gamma_s (0<s<r) non-permutation = {nonperm}; R1 fails on {{0..r}} = {fail_r}  '
          f'[{"GREEN" if nonperm == fail_r else "RED"}]')
    return cm

print('--- XOR (2,2): write-then-read, period 3')
show(xor22())
print('--- swap (2,2): indivisibility control (no accessible window: r = 2)')
M = swap22(); print(f'   r = {M.r}; windows 2 <= n < r: none')
print('--- static bath Z_3 with shifts {1,2} (nV=3, nH=2)')
show(static_shift(3, [1, 2]))
for m in (3, 5, 7, 11):
    print(f'--- static bath Z_{m}, all shifts (nV=nH={m}), tau_B = infinity')
    show(static_shift(m), quiet_windows=True)
for mb in (1, 2, 3, 5, 6):
    print(f'--- LFSR x^{mb+1}+x+1, (2, {2**mb})')
    show(lfsr(mb), nmax=None if mb < 5 else 2 * mb + 4, quiet_windows=True)
    if mb >= 5:
        M = lfsr(mb)
        allJ = all(M.Gamma(t) == [[F(1, 2)] * 2] * 2 for t in range(1, M.r))
        print(f'   all Gamma_t = J/2 for 1 <= t < r={M.r}: {allJ}  (=> R1 holds on every window n < r, Lambda = J/2)')
