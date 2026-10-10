import sympy as sp, itertools
src=open('k20_part2.py').read().split('# 5. which gates')[0]
src=src.replace("print('(0)","_=('(0)").replace("    print('(1)","    _=('(1)")
exec(src)
exec(open('k20_part2.py').read().split('# 5. which gates are quantum (unitary conjugations in the standard embedding)? Choi rank-1 PSD test')[1].split('R=sp.diag(1,1,-1,1)')[0])
U_=set(c for c in cands if is_unitary_channel(Gs[c]))
print('(4) candidates that are unitary conjugations in the standard embedding:',len(U_))
for c in sorted(U_): print('     ',c)
# O-class: is some member unitary?
for i,cl in enumerate(co):
    print('    O-class',i,'members unitary:',[c in U_ for c in cl])
for i,cl in enumerate(cs):
    print('    SO-class',i,cl,'unitary' if cl[0] in U_ else 'not unitary', '(consistent)' if all((c in U_)==(cl[0] in U_) for c in cl) else '(MIXED)')
