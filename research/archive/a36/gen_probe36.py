"""Emit verification/lean/dita_hierarchy_probe.py: the A35 probe's exact head (Gaussian rationals, F4, circles, dita, kron,
unitarity, ranks) followed by this round's body (probe36_body.py). Single source for the frozen probe."""
import os
S = os.path.dirname(os.path.abspath(__file__))
src35 = open(os.path.join(S, 'probe_d36.py'), encoding='utf-8').read()
head35 = src35[src35.index('import itertools'):src35.index("print('== 1.")]
doc = '''"""Track B act 36 -- the exact-computation probe of the factorization-hierarchy round (frozen with the control plane).

Everything asserted is exact arithmetic over the Gaussian rationals in Python integers and fractions: ranks by exact
elimination, factorizations by exact proportionality and unitarity tests, the second-order form by exact cokernel
functionals. numpy appears only in the numerical eigenvalue guess that the exact eigenspace computation then verifies.
The probe asserts the preregistered values and exits 1 on any mismatch; it certifies nothing on its own beyond the
arithmetic it replays. Its first part is act 35's probe head, verbatim, for the shared objects.

Objects (acts 24-35, numbers as in the landed Lean):
  F4(z)      (1/2) [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]           (scaled by 2 here)
  SIG        F4(z) ⊗ F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) -> 4a+b (scaled by 4: unimodular entries)
  W          [a even][c even]·([b = 1] + [d = 1]) on the entry ((a,b),(c,d))
  P          SIG ∘ u^W with u = (60+i)/(60-i) = (3599+120i)/3601
  DF         the linearized unitarity constraints in the phase perturbations θ ∈ R^256 at SIG; defect = 256 − rank − 31
"""
'''
body = open(os.path.join(S, 'probe36_body.py'), encoding='utf-8').read()
text = doc + head35 + body
open(os.path.join(S, 'dita_hierarchy_probe.py'), 'w', encoding='utf-8').write(text)
import ast; ast.parse(text)
print('probe written', len(text))
