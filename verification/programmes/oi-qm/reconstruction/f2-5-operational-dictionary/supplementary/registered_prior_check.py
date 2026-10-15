#!/usr/bin/env python3
"""registered_prior_check.py -- supplementary to F2-5; decides no cell.

At N = 2, q = 3: the dictionary image of a registered preparation (c1, c2) = (a, b) with hidden prior nu on (p1, p2)
is rho = sum nu(xi1, xi2) A((a, xi1), (b, xi2)). Tested priors: p1 = p2 (P0 locality sources' E-pri), p1 = -p2, and
uniform; all nine registered values. Reuses the definitions of ../f2_5_dict.py, pinned by hash, by executing its
definitional part up to the K-order section.
"""
import contextlib
import hashlib
import io
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.join(HERE, '..', 'f2_5_dict.py')
PIN = '211ce708440e3f6fd02558113dcb1aea2ca3723da780f0c32c838b3a454f6b04'
src = open(MAIN, encoding='utf-8').read()
if hashlib.sha256(src.encode('utf-8')).hexdigest() != PIN:
    print('FAIL pin: f2_5_dict.py is not the pinned blob')
    sys.exit(1)
ns = {'__name__': 'f2_5_defs'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:src.index('# ---------------------------------------------------------------- K-order')], MAIN,
                 'exec'), ns)
A2, K, zeros, add, scal = ns['A2'], ns['K'], ns['zeros'], ns['add'], ns['scal']
psd_ldl, psd_charpoly = ns['psd_ldl'], ns['psd_charpoly']


def rho(a, b, nu):
    M = zeros(9)
    for (x1, x2), w in nu.items():
        M = add(M, scal(K(w), A2[((a, x1), (b, x2))]))
    return M


priors = [('p1 = p2', {(x, x): Fraction(1, 3) for x in range(3)}),
          ('p1 = -p2', {(x, (-x) % 3): Fraction(1, 3) for x in range(3)}),
          ('uniform', {(x, y): Fraction(1, 9) for x in range(3) for y in range(3)})]
ok = True
for name, nu in priors:
    r1 = [psd_ldl(rho(a, b, nu)) for a in range(3) for b in range(3)]
    r2 = [psd_charpoly(rho(a, b, nu)) for a in range(3) for b in range(3)]
    agree = r1 == r2
    ok &= agree and (all(r1) if name == 'uniform' else not any(r1))
    print('%-9s a state at %d of 9 registered values; the two PSD tests agree: %s' % (name, sum(r1), agree))
print('SUPPLEMENTARY ' + ('AS-EXPECTED' if ok else 'NOT-AS-EXPECTED')
      + ': correlated hidden priors on registered sites have no physical image; the uniform prior does')
