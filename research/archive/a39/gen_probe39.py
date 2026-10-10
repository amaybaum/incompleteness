"""Assemble the A39 probe from act 38's landed probe head (verbatim, from D) and the A39 body."""
import os
S = os.path.dirname(os.path.abspath(__file__))
p38 = open(os.path.join(S, 'probe38_landed.py'), encoding='utf-8').read()
body = open(os.path.join(S, 'probe39_body.py'), encoding='utf-8').read()
DOC = '''"""Track B act 39 -- the exact-computation probe of the three-parameter realizability round (frozen with the control plane).

Everything asserted is exact arithmetic: Gaussian rationals in Python integers and fractions, and, for the symbolic form of the
identity, integer counts of the monomials z^q w^r. The probe asserts the preregistered values and exits 1 on any mismatch; it
certifies nothing on its own beyond the arithmetic it replays. Its first part is act 38's probe head, verbatim: act 36's
objects and exhaustive structure search, act 36's stabilizer, act 37's monomial calculus, and act 38's pieces A, B, C and E.

Objects (acts 24-39, numbers as in the landed Lean):
  SIG        F4(z) ⊗ F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) -> 4a+b (scaled by 4: unimodular entries)
  A, B, C    [a odd][b = 3][c odd], [a = 2][d = 1], [a+b odd][(c,d) in {(0,2),(2,0)}] on the entry ((a,b),(c,d))
  H3         SIG o u1^A u2^B u3^C, the three-parameter family; its diagonal is act 38's arc SIG o u^(A+B+C)
"""
'''
head = p38[p38.index('import itertools, json, sys, time'):p38.index("print('== 1. realizability")]
text = DOC + head + body
open(os.path.join(S, 'dita_torus_probe.py'), 'w', encoding='utf-8').write(text)
print('probe written', len(text.encode()), 'bytes')
