"""probe4b: certification of off-Kronecker classes by the exact defect (an equivalence invariant),
for the quaternary Diţă twists and the second real class."""
import numpy as np, itertools, sys, time
sys.path.insert(0, '.')
from lib35 import *
exec(open('probe2.py').read().split('t0 = time.time()')[0].split('from sympy import QQ')[1])  # defect_exact
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
rng = np.random.default_rng(354)
roots = np.array([1, 1j, -1, -1j])
# the three Kronecker quaternary classes (modulo full equivalence, conj, transpose): H4⊗H4, H4⊗F4, F4⊗F4
def inv3(H): return (profile(H), haagerup_set(H), defect_exact(H))
K = {'H4⊗H4': kron(U_circle(0, 1), U_circle(0, 1)), 'H4⊗F4': kron(U_circle(0, 1), U_circle(0, 1j)), 'F4⊗H4': kron(U_circle(0, 1j), U_circle(0, 1)), 'F4⊗F4': kron(U_circle(0, 1j), U_circle(0, 1j))}
Kinv = {k: inv3(v) for k, v in K.items()}
print('Kronecker quaternary classes: defects', {k: v[2] for k, v in Kinv.items()}, '; H4⊗F4 and F4⊗H4 same invariants:', Kinv['H4⊗F4'] == Kinv['F4⊗H4'])
t0 = time.time()
classes = {}
for _ in range(400):
    bits = rng.integers(0, 4, size=(3, 3)); D = np.ones((4, 4), dtype=complex); D[1:, 1:] = roots[bits]
    X = U_circle(rng.integers(0, 9), roots[rng.integers(0, 4)] if rng.random() < 0.5 else 1j)
    Ys = [U_circle(rng.integers(0, 9), roots[rng.integers(0, 4)]) for _ in range(4)]
    Hd = dita(X, Ys, D)
    d = defect_exact(Hd)
    classes.setdefault((profile(Hd), haagerup_set(Hd), d), Hd)
print('400 quaternary twists -> %d distinct (profile, Haagerup, exact defect) classes (%.0fs)' % (len(classes), time.time() - t0))
kd = {v[2] for v in Kinv.values()}
off_by_defect = sum(1 for c in classes if c[2] not in kd)
off_by_triple = sum(1 for c in classes if c not in Kinv.values())
on_kron = [c for c in classes if c in Kinv.values()]
print('certified off the entire Kronecker locus: by exact defect alone %d, by the full triple %d, of %d; coinciding with a Kronecker class: %d' % (off_by_defect, off_by_triple, len(classes), len(on_kron)))
print('defect values present:', sorted({c[2] for c in classes}))
# the witness
Fi = F4(1j); Dw = np.ones((4, 4), dtype=complex); Dw[1, :] = [1, 1j, 1, -1j]
Hw = dita(Fi, [Fi] * 4, Dw)
print('A34 witness: exact defect %d; equals a Kronecker class triple: %s' % (defect_exact(Hw), inv3(Hw) in Kinv.values()))
# real classes: the second profile
H4 = U_circle(0, 1)
for bits in itertools.product([1, -1], repeat=9):
    D = np.ones((4, 4)); D[1:, 1:] = np.array(bits).reshape(3, 3)
    Hd = dita(H4, [H4] * 4, D)
    if profile(Hd) != profile(kron(H4, H4)):
        print('second real class: exact defect %d (Sylvester: %d); twist bits %s' % (defect_exact(Hd), defect_exact(kron(H4, H4)), bits)); break
