import sys; sys.path.insert(0, '.')
from det_solver import *
MINUS = (ONE, neg(ONE)); PLUSI = (ONE, I_); PLUS = (ONE, ONE)
fails = 0
def row(label, n, bases, tgt, mode, na, expect, ms=60000):
    global fails
    s0, win, ns, tr = solve(n, bases, tgt, mode, na, max_states=ms)
    got = s0 in win
    ok = (got == expect)
    if expect is False and tr: ok = ok  # a loss on a truncated graph is relative to the bound; reported as such
    fails += 0 if ok else 1
    print('%s %-52s states=%-6d truncated=%-5s deterministic=%s' % ('PASS' if ok else 'FAIL', label, ns, tr, got), flush=True)
row('NEG  n=2 configuration tests only, target |->', 2, 'Z', MINUS, 'luders', False, False)
row('NEG  n=1 Pauli Lueders, target |->', 1, 'XYZ', MINUS, 'luders', False, False)
row('POS  n=2 Pauli Lueders, target |+i>', 2, 'XYZ', PLUSI, 'luders', False, True)
row('POS  n=2 Pauli Lueders, target |+>', 2, 'XYZ', PLUS, 'luders', False, True)
row('MAIN n=2 Pauli Lueders, target |->', 2, 'XYZ', MINUS, 'luders', False, False)
row('MAIN n=3 Pauli Lueders, affine perms, target |->', 3, 'XYZ', MINUS, 'luders', False, False)
row('DES  n=3 Pauli destructive (test, reset), target |+i>', 3, 'XYZ', PLUSI, 'destructive', True, False)
row('MAIN n=3 Pauli Lueders, + Toffoli/Fredkin, target |-> (bounded)', 3, 'XYZ', MINUS, 'luders', True, False, ms=30000)
print('SUMMARY fails', fails)
