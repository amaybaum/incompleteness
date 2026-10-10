#!/usr/bin/env python3
"""Generates the frozen controls.py of IIP-1 and CMP-1 from controls_base.py and the reference modules."""
import json, re, sys, os

W = os.path.dirname(os.path.abspath(__file__))
S = os.path.dirname(W)
base = open(os.path.join(W, 'controls_base.py')).read()
ns = {'re': re}
exec(base[base.index('DECL = re.compile'):base.index('FAILS, COUNT')], ns)
exec(base[base.index('def preamble'):base.index('def split_statement')], ns)

IIP_DOC = """  S1  span        `invariant_inner_product_span` is relative to the affine span: its hypotheses are the injective
                  chart of the span, its conclusion is about `bodyR L p0 Ω` (compactness, nonempty interior, and
                  `invMatrix` of the restricted body) and never about the ambient `Ω`'s moment
  S2  interior    every theorem other than the span theorem and the verdict that concludes positivity of `moment` or
                  `invMatrix` has a nonempty-interior hypothesis; the verdict states it before positivity
  S3  lower-dim   the ambient-nullity controls are present as kernel theorems with axiom prints:
                  `momentMatrix_eq_zero_of_subset` (a body in a proper affine subspace has zero ambient second
                  moment) and `segment2_moment`; no theorem concludes positivity of a form on `segment2`
  S4  scope       no declaration name, theorem conclusion or header claim of an ellipsoid, transitivity, a rotation
                  group, a drive or a dimension; the header disclaimer is present"""

IIP_CODE = r'''SPAN = 'invariant_inner_product_span'
VERDICT = 'iip1_core'
FORBIDDEN_NAME = re.compile(r'(llipsoid|ransitiv|ball3|finrank|SO3|otation|losureGen|rive|dim3|Dim3)')
FORBIDDEN_CONCL = ('BoundaryTransitive', 'ElementaryDrivability', 'ball3', 'finrank', 'driveWords')
FORBIDDEN_PROSE = re.compile(r'(is an ellipsoid|boundary[- ]transitive (on|under)|dimension (three|3) (is|follows)|'
                             r'generates SO)', re.I)
DISCLAIMER = 'No ellipsoid, no transitivity and no dimension is claimed.'
LOWDIM = ('momentMatrix_eq_zero_of_null', 'momentMatrix_eq_zero_of_subset', 'volume_segment2', 'segment2_moment')
PREFIX = 'OIBridge.InvariantInnerProduct.'


def semantic_checks(mod, texts, kinds, prints, tag):
    st = texts.get(SPAN, '')
    b, c = split_statement(st) if st else ('', '')
    check('S1', 'the span theorem is relative to the affine span' + tag,
          kinds.get(SPAN) == 'theorem' and 'LinearMap.ker L = ⊥' in b
          and 'x ∈ affineSpan ℝ Ω ↔ x ∈ Set.range (chart L p0)' in b
          and '(interior (bodyR L p0 Ω)).Nonempty' in c and 'invMatrix (bodyR L p0 Ω)' in c
          and not re.search(r'(invMatrix|momentMatrix|moment) Ω\b', c))
    bad = []
    for n, t in texts.items():
        if kinds.get(n) not in ('theorem', 'lemma') or n in (SPAN, VERDICT):
            continue
        bb, cc = split_statement(t)
        if '0 <' in cc and re.search(r'invMatrix|moment ', cc) and '(interior' not in bb:
            bad.append(n)
    vt = texts.get(VERDICT, '')
    check('S2', 'positivity only under a nonempty-interior hypothesis%s%s' % (tag, (' %s' % bad[:3]) if bad else ''),
          not bad and vt.count('IsCompact Ω → (interior Ω).Nonempty →') == 2)
    sub = texts.get('momentMatrix_eq_zero_of_subset', '')
    sb, sc = split_statement(sub) if sub else ('', '')
    check('S3', 'the ambient-nullity controls are kernel theorems with prints' + tag,
          all(kinds.get(n) == 'theorem' and PREFIX + n in prints for n in LOWDIM)
          and 's ≠ ⊤' in sb and 'Ω ⊆ (s : Set (Fin n → ℝ))' in sb and sc.strip() == 'momentMatrix Ω = 0'
          and 'momentMatrix segment2 = 0' in texts.get('segment2_moment', '')
          and 'momentMatrix segment2 = 0' in vt
          and not any(re.search(r'0 <[^∧→]*segment2', split_statement(t)[1])
                      for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')))
    hdr = header(mod)
    names = [n for _, n in decls(mod)]
    concl = [split_statement(t)[1] for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')]
    check('S4', 'no ellipsoid, transitivity, rotation, drive or dimension claim' + tag,
          not any(FORBIDDEN_NAME.search(n) for n in names)
          and not any(f in cc for cc in concl for f in FORBIDDEN_CONCL)
          and not FORBIDDEN_PROSE.search(hdr) and DISCLAIMER in norm(hdr))'''

IIP_MUT = r'''    must_fail('S1', 'the span theorem strengthened to the ambient body',
              replace_once(mod, '(invMatrix (bodyR L p0 Ω))ᵀ = invMatrix (bodyR L p0 Ω)', '(invMatrix Ω)ᵀ = invMatrix Ω'))
    must_fail('S2', 'positivity without interior',
              append_decl(mod, 'theorem ambient_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) {u : Fin n → ℝ}\n'
                               '    (hu : u ≠ 0) : 0 < moment Ω u u := by\n  exact absurd hu hu'))
    must_fail('S2', 'the interior hypothesis dropped from invMatrix_pos',
              replace_once(mod, 'theorem invMatrix_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω) (hi : (interior Ω).Nonempty)',
                           'theorem invMatrix_pos {Ω : Set (Fin n → ℝ)} (hc : IsCompact Ω)'))
    must_fail('S3', 'the segment control removed', replace_once(mod, 'theorem segment2_moment', 'theorem segment2_moment2'))
    must_fail('S3', 'positivity claimed for the segment',
              append_decl(mod, 'theorem segment2_pos : 0 < moment segment2 (Pi.single 1 1) (Pi.single 1 1) := by\n'
                               '  exact absurd rfl rfl'))
    must_fail('S4', 'an ellipsoid name', append_decl(mod, 'theorem ellipsoid_of_moment : True := trivial'))
    must_fail('S4', 'a transitivity conclusion',
              append_decl(mod, 'theorem bt_of_moment (Ω : Set (Fin 3 → ℝ)) : BoundaryTransitive Ω ∅ := by\n'
                               '  exact absurd rfl rfl'))'''

CMP_DOC = """  S1  no ELEM     no declaration is named bare `ELEM` (or `Elem`, `elem`)
  S2  ELEM-bin    `BinaryVisible` is a structure, the formal notion this round provides; its docstring and the module
                  header state that it is necessary, not sufficient, for the elementary-system scope; the header
                  states that the visible-factor requirement is not formalized here and that the name ELEM is
                  reserved
  S3  ELEM-vis    no declaration formalizes the visible-factor requirement (`ElemVis`, `VisibleFactor`, `NoAncilla`,
                  ...)
  S4  SC∞         `SCInf` is a named predicate (`def`), `DirectedStages` carries no consistency field, and no theorem
                  concludes `SCInf`, `BinaryVisible` or `FiniteRank` without it among its hypotheses, except the
                  named controls on `bitTower` and `badD`
  S5  scope       no declaration name, theorem conclusion or header claim of a ball, ellipsoid, transitivity, drive,
                  dimension or V4′; the header disclaimer is present"""

CMP_CODE = r'''VERDICT = 'cmp1_core'
CONTROLS_SC = {'bitTower_scInf', 'not_scInf_bad'}
FORBIDDEN_NAME = re.compile(r'(llipsoid|ransitiv|ball3|finrank|rive|dim3|Dim3|V4)')
FORBIDDEN_CONCL = ('BoundaryTransitive', 'ElementaryDrivability', 'ball3', 'finrank', 'SeedOrbitAvailable')
VIS_NAME = re.compile(r'(ElemVis|ELEM_vis|ElemVisible|VisibleFactor|visibleFactor|NoAncilla|noAncilla|ElemFull|ELEM_full)')
DISCLAIMER = 'nothing defines the full elementary-system scope'


def semantic_checks(mod, texts, kinds, prints, tag):
    names = [n for _, n in decls(mod)]
    check('S1', 'no declaration named bare ELEM' + tag,
          not any(re.fullmatch(r'(ELEM|Elem|elem)', n.split('.')[-1]) for n in names))
    hdr = norm(header(mod))
    i = mod.find('structure BinaryVisible')
    doc = norm(mod[mod.rindex('/--', 0, i):i]) if i != -1 else ''
    check('S2', 'BinaryVisible is the formal notion, necessary, not sufficient; ELEM reserved' + tag,
          kinds.get('BinaryVisible') == 'structure' and 'necessary, not sufficient' in doc
          and 'necessary, not sufficient' in hdr and 'not formalized here' in hdr
          and 'the name ELEM is reserved' in hdr)
    check('S3', 'the visible-factor requirement is not formalized' + tag, not any(VIS_NAME.search(n) for n in names))
    viol = []
    for n, t in texts.items():
        if kinds.get(n) not in ('theorem', 'lemma') or n == VERDICT or n in CONTROLS_SC:
            continue
        bb, cc = split_statement(t)
        for p in ('SCInf', 'BinaryVisible', 'FiniteRank'):
            if p in cc and p not in bb:
                viol.append((n, p))
    vt = texts.get(VERDICT, '')
    check('S4', 'SC∞ is a named predicate and is not sourced%s%s' % (tag, (' %s' % viol[:3]) if viol else ''),
          kinds.get('SCInf') == 'def' and 'Consistent' not in texts.get('DirectedStages', '') and not viol
          and set(re.findall(r'SCInf \w+', vt)) <= {'SCInf D', 'SCInf badD', 'SCInf bitTower'}
          and 'SCInf D →' in vt)
    concl = [split_statement(t)[1] for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma')]
    check('S5', 'no ball, ellipsoid, transitivity, drive, dimension or V4′ claim' + tag,
          not any(FORBIDDEN_NAME.search(n) for n in names)
          and not any(f in cc for cc in concl for f in FORBIDDEN_CONCL) and DISCLAIMER in hdr)'''

CMP_MUT = r'''    must_fail('S1', 'a bare ELEM declaration', append_decl(mod, 'def ELEM (D : DirectedStages) : Prop := SCInf D'))
    must_fail('S2', 'the not-sufficient qualifier dropped',
              replace_once(mod, 'necessary, not sufficient; it says nothing', 'sufficient; it says nothing'))
    must_fail('S3', 'a visible-factor definition', append_decl(mod, 'def ElemVis (D : DirectedStages) : Prop := True'))
    must_fail('S4', 'SC∞ made a structure field',
              replace_once(mod, '  comp_P : ∀ {i j k : ι}',
                           '  consistent : ∀ {i j : ι} (h : i ≤ j), (map h).Consistent\n  comp_P : ∀ {i j k : ι}'))
    must_fail('S4', 'SC∞ concluded for every system',
              append_decl(mod, 'theorem scInf_all (D : DirectedStages) : SCInf D := by\n  exact absurd rfl rfl'))
    must_fail('S5', 'a ball claim', append_decl(mod, 'theorem ball3_of_completion : True := trivial'))'''

ROUNDS = {
    'IIP-1': dict(rdir='verification/programmes/oi-qm/reconstruction/round-iip-1-invariant-inner-product/',
                  modpath='verification/lean-mathlib/OIBridge/InvariantInnerProduct.lean',
                  newimport='import OIBridge.InvariantInnerProduct\n', dev='wt-iip1dev',
                  famprefix='the common fixed point and invariant inner product', doc=IIP_DOC, code=IIP_CODE,
                  mut=IIP_MUT, out='iip1/controls.py'),
    'CMP-1': dict(rdir='verification/programmes/oi-qm/reconstruction/round-cmp-1-completion/',
                  modpath='verification/lean-mathlib/OIBridge/StageCompletion.lean',
                  newimport='import OIBridge.StageCompletion\n', dev='wt-cmp1dev',
                  famprefix='the stage completion', doc=CMP_DOC, code=CMP_CODE, mut=CMP_MUT, out='cmp1/controls.py'),
}


def j(x):
    s = json.dumps(x, ensure_ascii=False, indent=1)
    assert "'''" not in s
    return s


for rnd, cfg in ROUNDS.items():
    dev = os.path.join(S, cfg['dev'])
    mod = open(os.path.join(dev, cfg['modpath'])).read()
    import subprocess
    blob = subprocess.run(['git', '-C', dev, 'rev-parse', 'HEAD:' + cfg['modpath']], capture_output=True,
                          text=True).stdout.strip()
    cen = json.load(open(os.path.join(dev, 'verification/lean-manuscript-census.json')))
    fam = [f for f in cen['families'] if f['name'].startswith(cfg['famprefix'])]
    assert len(fam) == 1
    t = base
    rep = {'@@ROUND@@': rnd, '@@RDIR@@': cfg['rdir'], '@@MODPATH@@': cfg['modpath'], '@@MODBLOB@@': blob,
           '@@NEWIMPORT@@': cfg['newimport'].replace('\n', '\\n'), '@@CENSUS_FAMILY@@': j(fam[0]),
           '@@DECLS@@': j([list(x) for x in ns['decls'](mod)]), '@@TEXTS@@': j(ns['decl_texts'](mod)),
           '@@PRINTS@@': j(re.findall(r'^#print axioms (\S+)', mod, re.M)), '@@PREAMBLE@@': j(ns['preamble'](mod)),
           '@@CONTEXT@@': j(ns['context_lines'](mod)), '@@SEMANTIC_DOC@@': cfg['doc'],
           '@@SEMANTIC_CODE@@': cfg['code'], '@@SEMANTIC_MUTATIONS@@': cfg['mut']}
    for k, v in rep.items():
        assert k in t, k
        t = t.replace(k, v)
    assert '@@' not in t
    open(os.path.join(S, cfg['out']), 'w').write(t)
    print(rnd, blob, len(ns['decls'](mod)), 'decls', len(re.findall(r'^#print axioms', mod, re.M)), 'prints',
          len(ns['context_lines'](mod)), 'context lines')
