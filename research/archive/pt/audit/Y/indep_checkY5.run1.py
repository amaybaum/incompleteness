#!/usr/bin/env python3
"""Coordinator's independent check of Y5 (the finite extensions), written without Y's code.

DECISION RULE (fixed before the first run): every line CONFIRMED or MISMATCH; verdict INDEP-Y5-CONFIRMED iff all
CONFIRMED.  Method: the two-qubit Clifford group modulo global phase is enumerated by closure from the generators
H(x)I, I(x)H, S(x)I, I(x)S, CNOT.  Every Clifford unitary has, up to a global phase, entries of the form
zeta * 2^(-k/2) with zeta in {0, +-1, +-i} and one k per matrix; after dividing by the phase of the first nonzero
entry the representation (k, N) with N an integer matrix over Z[i] in {0, +-1, +-i} is exact, and the product of two
elements is renormalized exactly (every nonzero entry of the product has the same modulus 2^(j/2); the modulus is
read off exactly from the Gaussian integer).  Claims checked: |group| = 11520 (so 23040 with the global transpose,
which does not change |det Psi| since |det Psi(conj psi)| = |det Psi(psi)|); for phi0 = (1, 2, 3i, -1+i),
d_min = min over the group of |det Psi(g phi0)|^2 / |phi0|^4 equals 5/256 and is attained inside G16 (the even native
class); every image is entangled (d > 0); the seed c = 1 + 4 d_min / 8 = 517/512 is Y's value.
Countercontrol: the product |00> has d = 0 everywhere, and the Bell state (1,0,0,1) reaches a product (d = 0 somewhere).
Exact integer arithmetic throughout; no floats.
"""
import sys
from fractions import Fraction

# Gaussian integers as Python complex with integer parts (exact), matrices as tuples of 16 entries
def gmul(a, b): return complex(a.real*b.real - a.imag*b.imag, a.real*b.imag + a.imag*b.real)
def mat_mul(A, B):
    return tuple(sum((gmul(A[4*i+k], B[4*k+j]) for k in range(4)), 0j) for i in range(4) for j in range(4))
def norm2(z): return int(z.real)**2 + int(z.imag)**2
def canon(N, k):
    """Normalize (k, N): all nonzero entries have equal norm 2^j (j integer); divide by 2^(j/2) (k -> k - j) and by the
    phase of the first nonzero entry (a unit of Z[i] when the entries are units up to the common modulus)."""
    norms = {norm2(z) for z in N if z != 0}
    assert len(norms) == 1, norms
    n2 = norms.pop(); j = n2.bit_length() - 1; assert 1 << j == n2, n2
    # divide by a Gaussian integer of norm 2^j: for even j by 2^(j/2); for odd j by (1+i) 2^((j-1)/2)
    if j % 2 == 0:
        d = 2**(j//2); M = tuple(complex(z.real/d, z.imag/d) for z in N)
    else:
        d = 2**((j-1)//2); M = tuple(gmul(z, complex(1,-1)) for z in N); M = tuple(complex(z.real/(2*d), z.imag/(2*d)) for z in M)
    assert all(z.real == int(z.real) and z.imag == int(z.imag) for z in M)
    first = next(z for z in M if z != 0); assert norm2(first) == 1
    ph = complex(first.real, -first.imag)   # inverse of a unit
    M = tuple(gmul(z, ph) for z in M)
    return (k - j, tuple((int(z.real), int(z.imag)) for z in M))
def unpack(key): return key[0], tuple(complex(a, b) for a, b in key[1])
# generators as (k, N): H = (1/sqrt2) [[1,1],[1,-1]] -> k = 1; S = diag(1, i) -> k = 0; CNOT -> k = 0
def kron2(A, B): return tuple(gmul(A[2*(i//2)+(j//2)], B[2*(i%2)+(j%2)]) for i in range(4) for j in range(4))
Hm = (1+0j, 1+0j, 1+0j, -1+0j); Sm = (1+0j, 0j, 0j, 1j); Im = (1+0j, 0j, 0j, 1+0j)
CN = tuple(complex(1 if (i,j) in ((0,0),(1,1),(2,3),(3,2)) else 0, 0) for i in range(4) for j in range(4))
gens = [canon(kron2(Hm, Im), 1), canon(kron2(Im, Hm), 1), canon(kron2(Sm, Im), 0), canon(kron2(Im, Sm), 0), canon(CN, 0)]
ident = canon(tuple(complex(1 if i == j else 0, 0) for i in range(4) for j in range(4)), 0)
group = {ident}; frontier = [ident]
while frontier:
    new = []
    for key in frontier:
        k, N = unpack(key)
        for gk in gens:
            kg, Ng = unpack(gk)
            prod = canon(mat_mul(Ng, N), kg + k)
            if prod not in group: group.add(prod); new.append(prod)
    frontier = new
R = []
def rec(cid, ok, text, detail=""):
    ok = bool(ok); R.append(ok); print(f"{'CONFIRMED' if ok else 'MISMATCH'} {cid} {text}" + (f" -- {detail}" if detail else ""))
rec("F1", len(group) == 11520, "the two-qubit Clifford group modulo global phase has 11520 elements (23040 with the global transpose, Y's census)", str(len(group)))
def det_frac(key, phi):
    k, N = unpack(key); v = [sum((gmul(N[4*i+j], phi[j]) for j in range(4)), 0j) for i in range(4)]
    d = gmul(v[0], v[3]) - gmul(v[1], v[2])        # det of the 2x2 coefficient matrix, Gaussian integer
    return Fraction(norm2(d), 2**(2*k))             # |det|^2 exactly (the matrix carries 2^(-k/2) per entry, so 2^(-k) per det... squared: 2^(-2k))
phi0 = (1+0j, 2+0j, 3j, -1+1j); n4 = Fraction(sum(norm2(z) for z in phi0))**2
vals = [det_frac(g, phi0) / n4 for g in group]
dmin = min(vals)
rec("F2", dmin == Fraction(5, 256) and all(v > 0 for v in vals), "phi0 = (1, 2, 3i, -1+i) stays entangled under every Clifford element, with min |det Psi|^2/|phi0|^4 = 5/256 (Y's d_min)", str(dmin))
# G16 = <cnot, Ad(Z(x)I), Ad(I(x)Z), T>: the unitary part is <CNOT, Z(x)I, I(x)Z> (order 8 mod phase); d_min attained there?
Zm = (1+0j, 0j, 0j, -1+0j)
g16 = {ident}; fr = [ident]; gens16 = [canon(CN,0), canon(kron2(Zm, Im), 0), canon(kron2(Im, Zm), 0)]
while fr:
    new = []
    for key in fr:
        k, N = unpack(key)
        for gk in gens16:
            kg, Ng = unpack(gk); prod = canon(mat_mul(Ng, N), kg + k)
            if prod not in g16: g16.add(prod); new.append(prod)
    fr = new
rec("F3", len(g16) == 8 and min(det_frac(g, phi0)/n4 for g in g16) == Fraction(5,256), "the unitary part of G16 has 8 elements and already attains d_min = 5/256 (so the whole Clifford extension adds no lower value)", str(len(g16)))
c_seed = 1 + Fraction(4)*dmin/8
rec("F4", c_seed == Fraction(517, 512), "the seed c = 1 + 4 d_min/8 equals 517/512 (Y's value); with d_min > 0 every finite node's reachable set misses phi0 and the cap defect is admissible", str(c_seed))
# transpose: conjugation of phi0 does not change |det|^2 of any image's coefficient matrix (|det conj Psi| = |det Psi|)
phi0c = tuple(complex(z.real, -z.imag) for z in phi0)
rec("F5", min(det_frac(g, phi0c)/n4 for g in group) == dmin, "the global transpose (complex conjugation on states) leaves the minimum unchanged: the 23040-element group with T has the same d_min")
rec("F6c", all(det_frac(g, (1+0j, 0j, 0j, 0j)) == 0 for g in group) and min(det_frac(g, (1+0j, 0j, 0j, 1+0j)) for g in group) == 0,
    "countercontrol: the product |00> has |det Psi| = 0 under every element, and the Bell state (1,0,0,1) reaches a product (min 0): reachable states give no certificate")
n_ = sum(R); print(f"checks: {len(R)}, confirmed: {n_}"); print("VERDICT", "INDEP-Y5-CONFIRMED" if n_ == len(R) else "INDEP-Y5-MISMATCH"); sys.exit(0 if n_ == len(R) else 1)
