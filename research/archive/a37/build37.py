"""A37 builder: the frozen propositions from shared components (single source).
Writes props37.json and elab37.lean. controls.py and the preregistration embed the same texts."""
import json, os, sys
S = os.path.dirname(os.path.abspath(__file__))
P36 = json.load(open(os.path.join(S, '..', 'a36', 'props36.json')))
HEAD36 = P36['COMPONENTS']['HEAD']          # act 35's head + act 36's objects, verbatim
M16 = 'Matrix (Fin 4 × Fin 4) (Fin 4 × Fin 4) ℂ'
def MAT(n): return 'Matrix (Fin %d) (Fin %d) ℂ' % (n, n)

# the eight other factorization classes of SIG, column form, as measured at D: (name, m, n, column blocks, row classes)
CLASSES = [
 ('k1', 4, 4, ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15)), ((0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15))),
 ('k2', 4, 4, ((0, 2, 8, 10), (1, 3, 9, 11), (4, 6, 12, 14), (5, 7, 13, 15)), ((0, 2, 8, 10), (1, 3, 9, 11), (4, 6, 12, 14), (5, 7, 13, 15))),
 ('k3', 4, 4, ((0, 2, 9, 11), (1, 3, 8, 10), (4, 6, 13, 15), (5, 7, 12, 14)), ((0, 6, 8, 14), (1, 7, 9, 15), (2, 4, 10, 12), (3, 5, 11, 13))),
 ('k4', 4, 4, ((0, 4, 8, 12), (1, 5, 9, 13), (2, 6, 10, 14), (3, 7, 11, 15)), ((0, 1, 2, 3), (4, 5, 6, 7), (8, 9, 10, 11), (12, 13, 14, 15))),
 ('e1', 8, 2, ((0, 2), (1, 3), (4, 6), (5, 7), (8, 10), (9, 11), (12, 14), (13, 15)), ((0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15))),
 ('e2', 8, 2, ((0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)), ((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15))),
 ('t2', 2, 8, ((0, 2, 4, 6, 8, 10, 12, 14), (1, 3, 5, 7, 9, 11, 13, 15)), ((0, 2), (1, 3), (4, 6), (5, 7), (8, 10), (9, 11), (12, 14), (13, 15))),
 ('t3', 2, 8, ((0, 2, 5, 7, 8, 10, 13, 15), (1, 3, 4, 6, 9, 11, 12, 14)), ((0, 10), (1, 11), (2, 8), (3, 9), (4, 14), (5, 15), (6, 12), (7, 13))),
]
FROZEN = ('t1', 2, 8, ((0, 1, 2, 3, 8, 9, 10, 11), (4, 5, 6, 7, 12, 13, 14, 15)), ((0, 8), (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15)))

def table(vals):
    """a 4 x 4 lookup table over the row/column index (i.1, i.2) with i = 4 i.1 + i.2, as a nested vector literal"""
    return '![' + ', '.join('![' + ', '.join(str(vals[4 * a + b]) for b in range(4)) + ']' for a in range(4)) + ']'
def maps(name, m, n, cp, rows):
    # column j = cp[c][d] -> (c, d); row i = rows[b][a] -> (a, b)
    cblk = [None] * 16; cpos = [None] * 16; ra = [None] * 16; rb = [None] * 16
    for c in range(m):
        for d in range(n): cblk[cp[c][d]] = c; cpos[cp[c][d]] = d
    for b in range(n):
        for a in range(m): ra[rows[b][a]] = a; rb[rows[b][a]] = b
    assert None not in cblk + cpos + ra + rb
    r = '  let r%s : Fin 4 × Fin 4 → Fin %d × Fin %d := fun i => (%s i.1 i.2, %s i.1 i.2)\n' % (name, m, n, table(ra), table(rb))
    c = '  let c%s : Fin 4 × Fin 4 → Fin %d × Fin %d := fun j => (%s j.1 j.2, %s j.1 j.2)\n' % (name, m, n, table(cblk), table(cpos))
    d = '  let dita%s : %s → (Fin %d → %s) → (Fin %d → Fin %d → ℂ) → %s := fun X Y D => Matrix.of fun i j => dg X Y D (r%s i) (c%s j)\n' % (name, MAT(m), m, MAT(n), m, n, M16, name, name)
    return r + c + d
HEAD37 = ''.join(maps(*cl) for cl in CLASSES)
HEAD = HEAD36 + HEAD37

def EXCL(name, m, n):
    ex = '(∃ (X : %s) (Y : Fin %d → %s) (D : Fin %d → Fin %d → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = %s)' % (MAT(m), m, MAT(n), m, n, '%s')
    return ('∀ u : ℂ, star u * u = 1 →\n    (' + ex % ('dita%s X Y D' % name) + ' → u = 1)\n    ∧ (' + ex % ('(dita%s X Y D)ᵀ' % name) + ' → u = 1)')
SYM = '∀ u : ℂ, (Pu u)ᵀ = Pu u'
PERSIST = ('∀ u : ℂ, star u * u = 1 →\n'
           '    (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = dita28 X Y D)\n'
           '    ∧ (∃ (X : Matrix (Fin 2) (Fin 2) ℂ) (Y : Fin 2 → Matrix (Fin 8) (Fin 8) ℂ) (D : Fin 2 → Fin 8 → ℂ), flg X ∧ (∀ c, flg (Y c)) ∧ (∀ c b, ‖D c b‖ = 1) ∧ Pu u = (dita28 X Y D)ᵀ)')
BASE = 'Pu 1 = SIG ∧ flg (F4 z) ∧ (∀ c : Fin 4, flg (F4 w)) ∧ SIG = ditak1 (F4 z) (fun _ => F4 w) (fun _ _ => (1 : ℂ))'
EXCLS = {'EXCL_' + nm: EXCL(nm, m, n) for nm, m, n, _, _ in CLASSES}
PARTS = ['SYM', 'PERSIST'] + list(EXCLS)
COMP = {'HEAD': HEAD, 'HEAD36': HEAD36, 'HEAD37': HEAD37, 'SYM': SYM, 'PERSIST': PERSIST, 'BASE': BASE}
COMP.update(EXCLS)
PKG = '\n  ∧ '.join('(' + COMP[k] + ')' for k in PARTS)
COMP['PKG'] = PKG
P_R = HEAD + '  ' + PKG
P_N = HEAD + '  ' + '\n  ∨ '.join('¬ (' + COMP[k] + ')' for k in PARTS)
PROPS = {'P_R': P_R, 'P_N': P_N, 'SYM': HEAD + '  ' + SYM, 'PERSIST': HEAD + '  ' + PERSIST, 'BASE': HEAD + '  ' + BASE}
PROPS.update({k: HEAD + '  ' + v for k, v in EXCLS.items()})
THEOREMS = [
 ('A37-EXCLUSIVITY-PROVED', 'a37_exclusivity', 'P_R'),
 ('A37-EXCLUSIVITY-FAILS', 'a37_not_exclusivity', 'P_N'),
 ('A37-1', 'a37_shared_symmetric', 'SYM'),
 ('A37-2', 'a37_shared_persistence', 'PERSIST'),
] + [('A37-3', 'a37_shared_excl_' + nm, 'EXCL_' + nm) for nm, _, _, _, _ in CLASSES] + [
 ('control', 'a37_control_base', 'BASE'),
]
COROLLARY = ('a37_c_exclusive', ['P_N'], 'P_R')
OPEN = P36['OPEN'].rstrip('\n') + ' DitaHierarchy\n'
IMPORT = 'import OIBridge.DitaHierarchy\n'
DOC = '''/-!
# Act 37 — the exclusivity of the `2 × 8` arc through the product-embedded stratum point

Act 36 ran an exact one-parameter family `Pu u = SIG ∘ u^W` of realizable classes through the
certified rational stratum point `SIG = F₄(z) ⊗ F₄(w)`, `z = (3+4i)/5`, `w = (5+12i)/13`, every member
a `2 × 8` column Diţă matrix at the frozen index maps, and its named point admitted no other
factorization. This module states the arc symmetric, so that its column and row Diţă forms coincide
entry for entry; the frozen `2 × 8` factorization persistent along the whole arc in both orientations;
and, for each of the eight other factorization classes of `SIG` — four `4 × 4`, two `8 × 2` and two
`2 × 8`, the complete census of the stratum point's Diţă structures modulo its stabilizer — that a
Diţă form of `Pu u` at that class's index maps, in either orientation, forces `u = 1`. The
exact-computation layer carries the exhaustive complement: at every unit `u ≠ 1`, no index maps
whatever admit a Diţă form of `Pu u` but the frozen class's.

The module carries no definition. Every theorem prints its axioms.
-/
'''
def elab_module():
    parts = [IMPORT, '\n', DOC, '\nnamespace OIBridge\nnamespace DitaArcExclusivity\n\n', OPEN, '\n']
    for role, nm, key in THEOREMS:
        parts.append('-- %s, `%s`\n#check (%s)\n\n' % (role, nm, PROPS[key]))
    parts.append('-- corollary, `a37_c_exclusive`\n#check ((%s) → ¬ (%s))\n\n' % (PROPS['P_N'], PROPS['P_R']))
    parts.append('end DitaArcExclusivity\nend OIBridge\n')
    return ''.join(parts)
if __name__ == '__main__':
    json.dump({'COMPONENTS': COMP, 'PROPS': PROPS, 'THEOREMS': THEOREMS, 'COROLLARY': COROLLARY, 'PARTS': PARTS, 'CLASSES': [list(c[:3]) for c in CLASSES],
               'OPEN': OPEN, 'IMPORT': IMPORT, 'DOC': DOC}, open(os.path.join(S, 'props37.json'), 'w'), ensure_ascii=False, indent=1)
    open(os.path.join(S, 'elab37.lean'), 'w', encoding='utf-8').write(elab_module())
    print('props', len(PROPS), 'theorems', len(THEOREMS), 'P_R chars', len(P_R), 'HEAD37 lines', HEAD37.count('\n'))
