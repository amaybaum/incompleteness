"""Assemble the A37 probe from act 36's probe head (verbatim, from D) and the A37 body."""
import json, os
S = os.path.dirname(os.path.abspath(__file__))
p36 = open(os.path.join(S, 'probe36.py'), encoding='utf-8').read()
body = open(os.path.join(S, 'probe37_body.py'), encoding='utf-8').read()
wit = json.load(open(os.path.join(S, 'witness37.json')))
DOC = '''"""Track B act 37 -- the exact-computation probe of the arc-exclusivity round (frozen with the control plane).

Everything asserted is exact arithmetic: Gaussian rationals in Python integers and fractions for the numeric
searches, and an exact monomial calculus for the symbolic ones, in which every entry of SIG o u^W is a monomial
i^p z^q w^r u^k and every point of the unit circle that the analysis singles out is named canonically as
zeta z^s w^t. The probe asserts the preregistered values and exits 1 on any mismatch; it certifies nothing on its
own beyond the arithmetic it replays. Its first part is act 36's probe head, verbatim, for the shared objects and
act 36's exhaustive structure search.

Objects (acts 24-36, numbers as in the landed Lean):
  F4(z)      (1/2) [[1,1,1,1],[1,z,-1,-z],[1,-1,1,-1],[1,-z,-1,z]]           (scaled by 2 here)
  SIG        F4(z) ⊗ F4(w), z = (3+4i)/5, w = (5+12i)/13, index (a,b) -> 4a+b (scaled by 4: unimodular entries)
  W          [a even][c even]·([b = 1] + [d = 1]) on the entry ((a,b),(c,d))
  Pu(u)      SIG ∘ u^W; P = Pu(u60), u60 = (60+i)/(60-i) = (3599+120i)/3601; the second point Pu(u5), u5 = (3+4i)/5
"""
'''
head = p36[p36.index('import itertools, json, sys, time'):p36.index('fails = []')]
objs = p36[p36.index('N16 = 16'):p36.index('# ---- exact linear algebra')]
search = p36[p36.index('def is_unitary_s'):p36.index('PT = [list(c)')]
sym = p36[p36.index('S4 = list(itertools.permutations(range(4)))'):p36.index('G4 = []')]
stab = p36[p36.index('X4, Y4 = F4(z), F4(w)'):p36.index('def apply(e, v):')]
CHK = '''fails = []
def check(name, got, want):
    ok = got == want
    print('  %s  %-70s %s' % ('PASS' if ok else 'FAIL', name, got if ok else '%s (expected %s)' % (got, want)))
    if not ok: fails.append(name)
t0 = time.time()
'''
E_CAND = json.load(open(os.path.join(S, 'e_cand37.json')))
body = body.replace('@@WITNESSES@@', json.dumps(wit, sort_keys=True)).replace('@@E_CAND@@', json.dumps(E_CAND, ensure_ascii=False))
BANNER = 'print("== 0. act 36\'s stabilizer of SIG in G_ext, replayed for the census ==")\n'
text = DOC + head + CHK + objs + search + sym + BANNER + stab + body
open(os.path.join(S, 'dita_arc_exclusivity_probe.py'), 'w', encoding='utf-8').write(text)
print('probe written', len(text.encode()), 'bytes')
