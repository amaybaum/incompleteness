"""Level 3B rule extension: the two new radius-1 second-order leap rules of the 3B matrix, added WITHOUT modifying
the sealed modules. record_sim.State.leap and record_fast.leap look up F_bits at call time in their own module
namespace, so installing the extended function there is enough; the three sealed rules are delegated unchanged.

    'linear'    F = l ^ r                 (3A / RECORD; A5 kept, A4-S kept)         edge-permutive (both edges)
    'LS'        F = l ^ c ^ r             (R_LS: A5 kept, A4-S violated)            edge-permutive (both edges)
    'nonlinear' F = (l & r) ^ c           (RECORD's nonlinear; R_NS-n)              centre-permutive only
    'majority'  F = maj(l, c, r)          (RECORD's majority;  R_NS-m)              not permutive
    'NL'        F = l & r                 (R_NL: A5 violated, A4-S kept)            not permutive (necessarily)
    'R5'        F = l ^ (c & r)           (R_5:  A5 violated, A4-S violated)        edge-permutive (left edge)

permutive(rule) returns the set of arguments in which F is permutive (exact, by enumeration of all 8 inputs).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
for sub in ('record', 'level3', 'quotient'):
    p = os.path.join(HERE, '..', sub)
    if p not in sys.path:
        sys.path.insert(0, p)
import record_sim    # noqa: E402
import record_fast   # noqa: E402

_SEALED = record_sim.F_bits
RULES = ('linear', 'LS', 'nonlinear', 'majority', 'NL', 'R5')
CELLS = {'R_LL': 'linear', 'R_LS': 'LS', 'R_NL': 'NL', 'R_NS-n': 'nonlinear', 'R_NS-m': 'majority', 'R_5': 'R5'}


def F3B(l, c, r, rule):
    if rule == 'LS':
        return l ^ c ^ r
    if rule == 'NL':
        return l & r
    if rule == 'R5':
        return l ^ (c & r)
    return _SEALED(l, c, r, rule)


def install():
    record_sim.F_bits = F3B
    record_fast.F_bits = F3B


def permutive(rule):
    """Arguments ('l', 'c', 'r') in which F(rule) is permutive: flipping that bit always flips F."""
    out = set()
    for name, mask in (('l', (1, 0, 0)), ('c', (0, 1, 0)), ('r', (0, 0, 1))):
        ok = True
        for l in (0, 1):
            for c in (0, 1):
                for r in (0, 1):
                    a = F3B(l, c, r, rule)
                    b = F3B(l ^ mask[0], c ^ mask[1], r ^ mask[2], rule)
                    ok &= (a != b)
        if ok:
            out.add(name)
    return out


def uses_centre(rule):
    return any(F3B(l, 0, r, rule) != F3B(l, 1, r, rule) for l in (0, 1) for r in (0, 1))


def is_affine(rule):
    f = [F3B(l, c, r, rule) for l in (0, 1) for c in (0, 1) for r in (0, 1)]
    # affine iff f(x) ^ f(y) ^ f(z) == f(x ^ y ^ z) for all x, y, z
    idx = lambda l, c, r: (l << 2) | (c << 1) | r
    for x in range(8):
        for y in range(8):
            for z in range(8):
                if f[x] ^ f[y] ^ f[z] != f[x ^ y ^ z]:
                    return False
    return True


install()

if __name__ == '__main__':
    print('rule       A5(affine)  uses-centre(A4-S violated)  permutive-in')
    for rule in RULES:
        print(f'{rule:10s} {str(is_affine(rule)):11s} {str(uses_centre(rule)):27s} {sorted(permutive(rule))}')
    # the design lemma: a two-variable Boolean function permutive in one argument is affine
    aff = 0
    for bits in range(16):
        g = lambda l, r: (bits >> ((l << 1) | r)) & 1
        pl = all(g(0, r) != g(1, r) for r in (0, 1))
        pr = all(g(l, 0) != g(l, 1) for l in (0, 1))
        if pl or pr:
            lin = all(g(a, b) ^ g(c, d) ^ g(e, f) == g(a ^ c ^ e, b ^ d ^ f)
                      for a in (0, 1) for b in (0, 1) for c in (0, 1) for d in (0, 1) for e in (0, 1) for f in (0, 1))
            aff += lin
            assert lin, bits
    print(f'two-variable functions permutive in some argument: {aff}, all affine')
