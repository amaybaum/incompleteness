"""A40 builder: the frozen propositions from shared components (single source).
Writes props40.json and elab40.lean."""
import importlib.util, json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('build37', os.path.join(S, '..', 'a37', 'build37.py')); B37 = importlib.util.module_from_spec(spec); spec.loader.exec_module(B37)
P39 = json.load(open(os.path.join(S, '..', 'a39', 'props39.json')))
HEAD39 = P39['COMPONENTS']['HEAD']          # act 39's frozen head: act 38's head, then Ea, Eb, Ec, H3
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
def MAT(n): return 'Matrix (Fin %d) (Fin %d) ℂ' % (n, n)
M_COL = (((0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)), ((0, 2), (1, 3), (4, 6), (5, 15), (7, 13), (8, 10), (9, 11), (12, 14)))
M_ROW = (((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)), ((0, 2), (1, 9), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 10)))
# act 38's two exceptional index maps, as lookup tables in act 37's form
HEAD40 = B37.maps('mc', 2, 8, *M_COL) + B37.maps('mr', 2, 8, *M_ROW)
HEAD = HEAD39 + HEAD40
CLASSES = list(B37.CLASSES[:6]) + [B37.FROZEN] + list(B37.CLASSES[6:])     # k1 k2 k3 k4 e1 e2 t1 t2 t3
FORM = {nm: ('dita28' if nm == 't1' else 'dita' + nm) for nm, *_ in CLASSES}
FORM.update({'mc': 'ditamc', 'mr': 'ditamr'})
SHAPE = {nm: (m, n) for nm, m, n, _, _ in CLASSES}; SHAPE.update({'mc': (2, 8), 'mr': (2, 8)})
U = {1: 'u₁', 2: 'u₂', 3: 'u₃'}
def EX(nm, form, h3):
    m, n = SHAPE[nm]
    return ('(∃ (X : %s) (Y : Fin %d → %s) (D : Fin %d → Fin %d → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ %s = %s)'
            % (MAT(m), m, MAT(n), m, n, h3, form))
def FORMOF(nm, orient): return ('%s X Y D' if orient == 'c' else '(%s X Y D)ᵀ') % FORM[nm]
# the five faces: (key, coordinate, value, structure, orientation)
FACES = [('FACE_1p', 1, '1', 't2', 'c'), ('FACE_1m', 1, '(-1)', 'mc', 'c'), ('FACE_2p', 2, '1', 't1', 'c'),
         ('FACE_3p', 3, '1', 't1', 'r'), ('FACE_3m', 3, '(-1)', 'mr', 'r')]
def FACE(coord, val, nm, orient):
    free = [k for k in (1, 2, 3) if k != coord]
    args = ' '.join(val if k == coord else U[k] for k in (1, 2, 3))
    return ('∀ %s %s : ℂ, star %s * %s = 1 → star %s * %s = 1 →\n    ' % (U[free[0]], U[free[1]], U[free[0]], U[free[0]], U[free[1]], U[free[1]])
            + EX(nm, FORMOF(nm, orient), 'H3 ' + args)[1:-1])
# the twenty named maps and the proportionality equations each forces (measured: every equation has a single witness)
EQS = {('k1', 'c'): [(2, '1'), (3, '1')], ('k1', 'r'): [(1, '1'), (3, '1')], ('k2', 'c'): [(2, '1')], ('k2', 'r'): [(2, '1')],
       ('k3', 'c'): [(2, '1'), (3, '1')], ('k3', 'r'): [(1, '1'), (2, '1'), (3, '1')], ('k4', 'c'): [(1, '1'), (3, '1')],
       ('k4', 'r'): [(2, '1'), (3, '1')], ('e1', 'c'): [(2, '1'), (3, '1')], ('e1', 'r'): [(1, '1')], ('e2', 'c'): [(3, '1')],
       ('e2', 'r'): [(2, '1')], ('t1', 'c'): [(2, '1')], ('t1', 'r'): [(3, '1')], ('t2', 'c'): [(1, '1')],
       ('t2', 'r'): [(2, '1'), (3, '1')], ('t3', 'c'): [(1, '1'), (2, '1')], ('t3', 'r'): [(2, '1')],
       ('mc', 'c'): [(1, '-1')], ('mr', 'r'): [(3, '-1')]}
NAMED = [(nm, o) for nm, *_ in CLASSES for o in ('c', 'r')] + [('mc', 'c'), ('mr', 'r')]
def EQTEXT(eqs): return ' ∧ '.join('%s = %s' % (U[k], v) for k, v in eqs)
def EXCL(nm, orient):
    return ('∀ u₁ u₂ u₃ : ℂ, star u₁ * u₁ = 1 → star u₂ * u₂ = 1 → star u₃ * u₃ = 1 →\n    '
            + EX(nm, FORMOF(nm, orient), 'H3 u₁ u₂ u₃') + ' → ' + EQTEXT(EQS[(nm, orient)]))
COMP = {'HEAD': HEAD, 'HEAD39': HEAD39, 'HEAD40': HEAD40}
for key, coord, val, nm, o in FACES: COMP[key] = FACE(coord, val, nm, o)
for nm, o in NAMED: COMP['EXCL_%s_%s' % (nm, o)] = EXCL(nm, o)
PARTS = [f[0] for f in FACES] + ['EXCL_%s_%s' % x for x in NAMED]
PKG = '\n  ∧ '.join('(' + COMP[k] + ')' for k in PARTS)
COMP['PKG'] = PKG
P_R = HEAD + '  ' + PKG
P_N = HEAD + '  ' + '\n  ∨ '.join('¬ (' + COMP[k] + ')' for k in PARTS)
PROPS = {'P_R': P_R, 'P_N': P_N}
PROPS.update({k: HEAD + '  ' + COMP[k] for k in PARTS})
THEOREMS = ([('A40-LOCUS-CLASSIFIED', 'a40_locus_kernel', 'P_R'), ('A40-LOCUS-FAILS', 'a40_not_locus_kernel', 'P_N')]
            + [('A40-1', 'a40_shared_' + k.lower(), k) for k in PARTS[:5]]
            + [('A40-2', 'a40_shared_' + k.lower(), k) for k in PARTS[5:]])
COROLLARY = ('a40_c_exclusive', ['P_N'], 'P_R')
OPEN = P39['OPEN'].rstrip('\n') + ' DitaTorus\n'
IMPORT = 'import OIBridge.DitaTorus\n'
DOC = '''/-!
# Act 40 — the Diţă locus of the three-parameter family: the kernel layer

Act 39 proved the family `H3 u₁ u₂ u₃ = SIG ∘ u₁^A u₂^B u₃^C` through the certified rational stratum point
`SIG = F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, realizable at every point of the three-torus. This
module states the kernel layer of act 40's classification of the points of the torus at which `H3` admits a
Diţă structure. On each of the five coordinate faces `u₁ = 1`, `u₁ = −1`, `u₂ = 1`, `u₃ = 1`, `u₃ = −1`, and at
every point of the face, `H3` (or its transpose) is an explicit strict Diţă product `dita X Y D` of a named shape
and index map, with `X` and every `Y c` flat unitary and `‖D c b‖ = 1`. For each of twenty named index maps — act
37's nine classes in both orientations and act 38's two maps `M_COL` and `M_ROW` — a strict Diţă form of `H3` at
that map forces the named coordinate equations. The module does not state that the five faces exhaust the
points admitting a Diţă structure: that converse, over every shape, index map and orientation and up to
diagonal equivalence, is certified by the round's exact-computation probe, not by the kernel.

The module carries no definition. Every theorem prints its axioms.
-/
'''
def elab_module(ns='DitaTorusLocus'):
    parts = [IMPORT, '\n', DOC, '\nnamespace OIBridge\nnamespace %s\n\n' % ns, OPEN, '\n']
    for role, nm, key in THEOREMS:
        parts.append('-- %s, `%s`\n#check (%s)\n\n' % (role, nm, PROPS[key]))
    parts.append('-- corollary\n#check ((%s) → ¬ (%s))\n\n' % (PROPS['P_N'], PROPS['P_R']))
    parts.append('end %s\nend OIBridge\n' % ns)
    return ''.join(parts)
if __name__ == '__main__':
    json.dump({'COMPONENTS': COMP, 'PROPS': PROPS, 'THEOREMS': THEOREMS, 'COROLLARY': COROLLARY, 'PARTS': PARTS, 'OPEN': OPEN,
               'IMPORT': IMPORT, 'DOC': DOC, 'EQS': {'%s_%s' % k: v for k, v in EQS.items()}},
              open(os.path.join(S, 'props40.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(S, 'elab40.lean'), 'w', encoding='utf-8').write(elab_module())
    print('props', len(PROPS), 'theorems', len(THEOREMS), 'parts', len(PARTS), 'P_R chars', len(P_R))
    print(COMP['FACE_1m']); print(COMP['EXCL_k1_c'][-200:])
