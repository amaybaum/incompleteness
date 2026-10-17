#!/usr/bin/env python3
"""layer_images.py -- audit check A (exact, q = 3, N = 1). Decides nothing for any round.

Question: under E1's dictionary (F2-5 RULES section 2), what are the images of the kernel's two
layers of the one-step map, `shear` and `swapLayer` (SecondOrderCircuit.lean:59, :64; the leap
factors as swapLayer o shear, :85), and of E1-L's two layers (F2-2 RULES: coupling shear and the
free map J')?  Kernel coordinates per site are (p, c) = (previous, current); F2-5's are
z = (x, xi) = (current, previous). Translation: kernel shear (p,c) -> (m c - p, c) is
(x, xi) -> (x, m x - xi); kernel swap (p,c) -> (c,p) is (x, xi) -> (xi, x).

Reuses F2-5's exact definitions (Q(omega) arithmetic, phase-point operators, Choi, two PSD tests)
by executing f2_5_dict.py up to its K-order section, pinned by sha256, as its own supplementary
check does.
"""
import contextlib, hashlib, io, os, sys
MAIN = sys.argv[1]
PIN = '211ce708440e3f6fd02558113dcb1aea2ca3723da780f0c32c838b3a454f6b04'
src = open(MAIN, encoding='utf-8').read()
assert hashlib.sha256(src.encode('utf-8')).hexdigest() == PIN, 'pin'
ns = {'__name__': 'f2_5_defs'}
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:src.index('# ---------------------------------------------------------------- K-order')], MAIN, 'exec'), ns)
PTS1, phi_from_T, choi, psd, psd_ldl, psd_charpoly = (ns[k] for k in
    ('PTS1', 'phi_from_T', 'choi', 'psd', 'psd_ldl', 'psd_charpoly'))
q = 3

def classify(f):
    perm = {z: f(z) for z in PTS1}
    assert sorted(perm.values()) == sorted(PTS1), 'not a bijection'
    T = {z: [(perm[z], 1)] for z in PTS1}
    ph = phi_from_T(T)
    C = choi(ph); Ct = choi(ph, transpose_input=True)
    cp = psd_ldl(C); cp2 = psd_charpoly(C)
    pos = psd_ldl(Ct); pos2 = psd_charpoly(Ct)
    assert cp == cp2 and pos == pos2, 'PSD tests disagree'
    return cp, pos

def lin_det(f):
    # linear part from images of basis vectors (all maps here are linear: f(0) = 0)
    a, c = f((1, 0)); b, d = f((0, 1))
    return (a * d - b * c) % q

rows = []
for m in range(q):
    rows.append(('kernel shear  m=%d' % m, lambda z, m=m: (z[0], (m * z[0] - z[1]) % q)))
rows.append(('kernel swap        ', lambda z: (z[1], z[0])))
for m in range(q):
    rows.append(('leap = swap.shear m=%d' % m, lambda z, m=m: ((m * z[0] - z[1]) % q, z[0])))
for m in range(q):
    rows.append(('E1-L coupling shear m=%d' % m, lambda z, m=m: (z[0], (z[1] - m * z[0]) % q)))
rows.append(("E1-L free J'       ", lambda z: ((-z[1]) % q, z[0])))
ok = True
for name, f in rows:
    cp, pos = classify(f)
    det = lin_det(f)
    print('%-26s det %d  CP %-5s  positive(Phi o transpose CP) %-5s' % (name, det, cp, pos))
    ok &= (cp == (det == 1)) and (cp or pos)
# control: the leap factors as swap after shear (kernel :85) and as J' after the coupling shear (F2-2 L0)
for m in range(q):
    for z in PTS1:
        sh = (z[0], (m * z[0] - z[1]) % q); lp = (sh[1], sh[0])
        cs = (z[0], (z[1] - m * z[0]) % q); lp2 = ((-cs[1]) % q, cs[0])
        ok &= lp == ((m * z[0] - z[1]) % q, z[0]) == lp2
print('CHECK-A', 'PASS' if ok else 'FAIL',
      ': kernel shear and swap layers are det -1 (anti-symplectic), positive and not CP; both factorizations multiply to the leap, which is CP')
