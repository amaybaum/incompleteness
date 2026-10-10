"""P1 -- SC-inf in the lattice cone-tower form (CT): protocol probabilities computed on the region [-R, R] under
the uniform measure do not depend on R once R >= protocol length (cone dependence, RegionTower:283, plus uniform
fibres, RegionTower:398).  Countercontrols: region measures whose finite marginals are not consistent: (i) uniform conditioned on even
total parity of the region; (ii) boundary sites +-R pinned to 1.  R is the exact cone radius #reads - 1.  Exact integer counts.

Second-order rule on Z, two layers (u, v):  (u, v) -> (v, F(v) + u) mod 2, reversible.  Visible bit v_0.
Letters: 'o' record v_0 then step; 'f' flip v_0; 's' swap (u_0, v_0).
"""
from fractions import Fraction as F
from itertools import product
import sys

RULE = sys.argv[1] if len(sys.argv) > 1 else 'nonlinear'
def Fv(v, i):   # v is a dict site -> bit on the current window
    if RULE == 'linear':
        return (v[i - 1] + v[i + 1]) % 2
    return (v[i - 1] * v[i + 1] + v[i]) % 2

def run(sigma, u, v, lo, hi):
    rec = []
    for a in sigma:
        if a == 'o':
            rec.append(v[0])
            nu = {i: v[i] for i in range(lo + 1, hi)}
            nv = {i: (Fv(v, i) + u[i]) % 2 for i in range(lo + 1, hi)}
            u, v, lo, hi = nu, nv, lo + 1, hi - 1
        elif 0 not in v:
            continue                 # an action after the window closed cannot affect the record
        elif a == 'f':
            v = dict(v); v[0] ^= 1
        elif a == 's':
            u, v = dict(u), dict(v); u[0], v[0] = v[0], u[0]
    return tuple(rec)

def law(R, sigma, measure):
    sites = list(range(-R, R + 1))
    counts, Z = {}, 0
    for bits in product((0, 1), repeat=2 * len(sites)):
        if measure == 'parity' and sum(bits) % 2:
            continue
        if measure == 'pinned' and not (bits[0] == bits[len(sites) - 1] == bits[len(sites)] == bits[-1] == 1):
            continue                 # boundary sites +-R pinned to 1 in both layers (an inconsistent family)
        u = dict(zip(sites, bits[:len(sites)]))
        v = dict(zip(sites, bits[len(sites):]))
        r = run(sigma, u, v, -R, R)
        counts[r] = counts.get(r, 0) + 1
        Z += 1
    return {r: F(c, Z) for r, c in counts.items()}

T = 3
protos = [s for L in range(1, T + 1) for s in product('ofs', repeat=L) if s.count('o') >= 1]
agree_u, agree_p, n = 0, 0, 0
for s in protos:
    nobs = s.count('o')
    R0 = nobs - 1                    # exact cone radius of the record: v_0 at read t depends on radius t
    lu0, lu1 = law(R0, s, 'uniform'), law(R0 + 1, s, 'uniform')
    lp0, lp1 = law(R0, s, 'parity'), law(R0 + 1, s, 'parity')
    lq0, lq1 = law(R0, s, 'pinned'), law(R0 + 1, s, 'pinned')
    agree_q = globals().get('agree_q', 0) + (lq0 == lq1); globals()['agree_q'] = agree_q
    n += 1
    agree_u += (lu0 == lu1)
    agree_p += (lp0 == lp1)
print(f'rule {RULE}: {n} protocols of length <= {T} with >= 1 read')
print(f'uniform measure: law at R = cone radius equals law at R+1 for {agree_u}/{n} protocols')
print(f'parity-conditioned (inconsistent) measure: equal for {agree_p}/{n} protocols')
print(f'boundary-pinned (inconsistent) measure: equal for {agree_q}/{n} protocols')
print('OK' if agree_u == n and agree_q < n else 'UNEXPECTED')
