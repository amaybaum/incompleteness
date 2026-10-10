"""Assemble the A40 probe: act 38's landed probe head (to its section 1) + the A40 body."""
import os
S = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(S, 'probe38_landed.py'), encoding='utf-8').read()
head = src[:src.index("print('== 1. realizability")]
doc_end = head.index('"""', 3) + 3
doc = '''"""Track B act 40 -- the exact-computation probe of the Dita-locus round (frozen with the control plane).

Everything asserted is exact arithmetic: Gaussian rationals in Python integers and fractions, an exact monomial calculus for the
entries of H3(u1, u2, u3) = SIG o u1^A u2^B u3^C, and an exact calculus of flats in the three-torus (solution sets of character
equations u^k = i^p z^q w^r, stored in canonical Hermite normal form), embedded below and self-tested. Its first part is act 38's
probe head, verbatim: act 36's objects, exhaustive structure search and stabilizer, act 37's monomial calculus and act 38's
pieces. It asserts the preregistered values and exits 1 on any mismatch; it certifies nothing beyond the arithmetic it replays.
"""'''
body = open(os.path.join(S, 'probe40_body.py'), encoding='utf-8').read()
open(os.path.join(S, 'dita_torus_locus_probe.py'), 'w', encoding='utf-8').write(doc + head[doc_end:] + body)
print('written')
