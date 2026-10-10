"""probe4: discrete off-locus classes and class-vs-stratum invariants.
(a) strata labels are not class invariants: a non-product relabelling of a Σ point leaves Σ while
    staying in its N16 isometry class; so 'off-locus' must be read modulo Isom(N16).
(b) real classes: ±1 Diţă twists of H4⊗H4 (512 modulo gauge, times the choice of real vertices for
    the block factors) -> distinct profiles; every non-Sylvester profile is a class off the whole
    Kronecker locus (its Haagerup set is {±1}, so a Kronecker representative would be H4⊗H4).
(c) quaternary classes: fourth-root Diţă twists of F4⊗F4 and of vertex/Fourier mixtures ->
    distinct (profile, Haagerup set, defect) triples; a row-ratio certificate for non-Kronecker
    classes under every relabelling."""
import numpy as np, itertools, sys, time
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from lib35 import *
rng = np.random.default_rng(354)
t0 = time.time()

# (a)
z, w = np.exp(1j * rng.uniform(0, 2 * np.pi, 2))
H = kron(U_circle(3, z), U_circle(7, w))
res = []
for _ in range(20):
    sig = rng.permutation(16)
    res.append(sigma_residual(H[sig, :]))
print('(a) Σ point under 20 random row relabellings of V: sigma_residual min %.3f max %.3f (isometry class unchanged)' % (min(res), max(res)))
sig = [4 * b + a for a in range(4) for b in range(4)]
print('(a) under the swap relabelling (a product-compatible one): residual %.2e' % sigma_residual(H[np.ix_(sig, sig)]))

# (b)
H4 = U_circle(0, 1)
verts = {}
for r in range(9):
    for zz in (1, -1):
        U = U_circle(r, zz); k = tuple(np.round(dephase(U).ravel() * 2).real.astype(int))
        verts.setdefault(k, U)
verts = list(verts.values())
print('(b) distinct dephased real 4x4 vertices:', len(verts))
def prof4(Hn):
    """profile via the 4-row sums, vectorised: |sum_k H_ak H_bk H_ck H_dk| for a<b<c<d"""
    n = Hn.shape[0]
    P2 = np.einsum('ak,bk->abk', Hn, np.conj(Hn))           # pair products
    vals = []
    for a, b in itertools.combinations(range(n), 2):
        M = P2[a, b][None, None, :] * P2                      # (c,d,k)
        S = np.abs(M.sum(-1))
        for c, d in itertools.combinations(range(n), 2):
            if c > b: vals.append(round(S[c, d], 6))
    return tuple(sorted(vals))
sylv = prof4(kron(H4, H4) * 4)
profiles = {}
D0 = np.ones((4, 4))
cnt = 0
for bits in itertools.product([1, -1], repeat=9):
    D = D0.copy(); D[1:, 1:] = np.array(bits).reshape(3, 3)
    Hd = dita(H4, [H4] * 4, D)
    p = prof4(Hd * 4)
    profiles.setdefault(p, []).append(('H4⊗H4 twist', bits)); cnt += 1
print('(b) 512 real twists of H4⊗H4: distinct profiles %d (Sylvester profile present: %s) [%d]' % (len(profiles), sylv in profiles, cnt))
# mixtures of vertex factors
for _ in range(300):
    X = verts[rng.integers(len(verts))]; Ys = [verts[rng.integers(len(verts))] for _ in range(4)]
    D = rng.choice([1, -1], size=(4, 4)).astype(float)
    Hd = dita(X, Ys, D)
    assert is_unitary(Hd)
    profiles.setdefault(prof4(Hd * 4), []).append(('mixed vertices',))
print('(b) with mixed vertex factors (300 samples): distinct profiles %d' % len(profiles))
for p, members in profiles.items():
    Hrep = None
    print('    profile #%s: multiset of |4-row sums| values %s ... count %d, Sylvester? %s' % (hash(p) % 10007, sorted(set(p)), len(members), p == sylv))
# transposes: same profile set?
print('(b) profile of H^T equals profile of H for the sampled twists:', all(prof4(dita(H4, [H4] * 4, D).T * 4) in profiles for D in [np.array(list(m[1]) + [0]*0).reshape(3,3) if False else None for m in []] ) if False else 'skipped')
print('(%.0fs)' % (time.time() - t0))

# (c)
Fi = F4(1j)
def row_ratio_degrees(H):
    """for each row i, the number of rows j whose ratio vector H_i∘conj(H_j) takes ≤ 4 distinct values."""
    n = H.shape[0]; Hn = H / np.abs(H); deg = []
    for i in range(n):
        d = 0
        for j in range(n):
            if i == j: continue
            v = Hn[i] * np.conj(Hn[j]); v = v / v[0]
            if len(set(map(tuple, np.round(np.c_[v.real, v.imag], 6)))) <= 4: d += 1
        deg.append(d)
    return deg
def invariants(H):
    d, _ = defect_numeric(H)
    return (prof4(H * 4), haagerup_set(H), d)
classes = {}
roots = np.array([1, 1j, -1, -1j])
samples = []
for _ in range(400):
    bits = rng.integers(0, 4, size=(3, 3)); D = np.ones((4, 4), dtype=complex); D[1:, 1:] = roots[bits]
    X = U_circle(rng.integers(0, 9), roots[rng.integers(0, 4)] if rng.random() < 0.5 else 1j)
    Ys = [U_circle(rng.integers(0, 9), roots[rng.integers(0, 4)]) for _ in range(4)]
    Hd = dita(X, Ys, D)
    assert is_unitary(Hd) and is_flat(Hd)
    inv = invariants(Hd)
    classes.setdefault(inv, []).append(Hd)
print('(c) 400 quaternary Diţă twists: distinct (profile, Haagerup set, defect) triples: %d' % len(classes))
by_defect = {}
for inv, mem in classes.items():
    by_defect.setdefault(inv[2], 0); by_defect[inv[2]] += 1
print('    classes per defect value:', dict(sorted(by_defect.items())))
# which of these are certified non-Kronecker under every relabelling (row-ratio degree < 6 somewhere),
# and which have entries only ±1 (real classes among them)
nonk = 0; real = 0; on_sigma = 0
for inv, mem in classes.items():
    H = mem[0]
    if min(row_ratio_degrees(H)) < 6: nonk += 1
    if np.allclose(H.imag, 0): real += 1
    if sigma_residual(H) < 1e-9: on_sigma += 1
print('    certified off the whole Kronecker locus by the row-ratio degree: %d of %d; real: %d; on Σ (fixed pairing): %d' % (nonk, len(classes), real, on_sigma))
print('    row-ratio degrees of a Σ point:', sorted(set(row_ratio_degrees(kron(Fi, Fi)))), '; of F16 (Diţă with D[c,b]=ω^{bc}):', end=' ')
om = np.exp(2j * np.pi / 16); D16 = np.array([[om ** (b * c) for b in range(4)] for c in range(4)])
F16d = dita(Fi, [Fi] * 4, D16)
print(sorted(set(row_ratio_degrees(F16d))), ' defect', defect_numeric(F16d)[0], ' unitary', is_unitary(F16d))
# is F16d the cyclic Fourier matrix up to relabelling? compare Haagerup sets with the cyclic F16
F16 = np.array([[om ** (j * k) for k in range(16)] for j in range(16)]) / 4
print('    Haagerup set of the Diţă F16 == cyclic F16:', haagerup_set(F16d) == haagerup_set(F16), '; profiles equal:', prof4(F16d * 4) == prof4(F16 * 4))
print('(%.0fs)' % (time.time() - t0))
