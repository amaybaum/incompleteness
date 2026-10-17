#!/usr/bin/env python3
"""Cross-check of check D's entry formula against F2-5's own dictionary at q = 3 (exact, Q(omega)).
For sigma_d(x, xi) = (x, d xi), d in {1, 2}, compare Phi_sigma(E_ij) computed by F2-5's phi_from_T with
the entry-permutation formula M_d(rho)[u, v] = rho[al u + be v, be u + al v]."""
import contextlib, hashlib, io, sys
MAIN = sys.argv[1]
PIN = '211ce708440e3f6fd02558113dcb1aea2ca3723da780f0c32c838b3a454f6b04'
src = open(MAIN, encoding='utf-8').read()
assert hashlib.sha256(src.encode('utf-8')).hexdigest() == PIN
ns = {'__name__': 'f2_5_defs'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:src.index('# ---------------------------------------------------------------- K-order')], MAIN, 'exec'), ns)
PTS1, phi_from_T, E, meq = ns['PTS1'], ns['phi_from_T'], ns['E'], ns['meq']
q = 3; inv2 = 2
ok = True
for d in (1, 2):
    T = {z: [((z[0], d * z[1] % q), 1)] for z in PTS1}
    ph = phi_from_T(T)
    al = (1 + d) * inv2 % q; be = (1 - d) * inv2 % q
    for i in range(q):
        for j in range(q):
            rho = E(i, j)
            out = ph(rho)
            pred = [[rho[(al * u + be * v) % q][(be * u + al * v) % q] for v in range(q)] for u in range(q)]
            ok &= meq(out, pred)
print('XCHECK-D', 'PASS' if ok else 'FAIL', ': entry formula equals F2-5 dictionary image for d = 1, 2 at q = 3')
