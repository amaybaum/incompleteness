#!/usr/bin/env python3
"""Builds OPACT-1's frozen controls.py, the census file and import file of the execution, from D and the reference
module blob. Off-repo tooling."""
import json, re, os, subprocess

H = os.path.dirname(os.path.abspath(__file__))
S = os.path.dirname(H)
REPO = os.path.join(S, 'wt-opact1dev')
D = '254ad0a7f19b3cf6f6ce28e1a7b955f18e4337e4'
REF = '4781824cf2d9aeda57a2782c6b22d457b411ff1b'
MODPATH = 'verification/lean-mathlib/OIBridge/CompletionAction.lean'
RDIR = 'verification/programmes/oi-qm/reconstruction/round-opact-1-completion-action/'

def git(*a):
    return subprocess.run(['git', '-C', REPO] + list(a), capture_output=True, text=True, check=True).stdout

base = open(os.path.join(H, 'controls_base_opact1.py')).read()
ns = {'re': re}
exec(base[base.index('DECL = re.compile'):base.index('FAILS, COUNT')], ns)
exec(base[base.index('def preamble'):base.index('def split_statement')], ns)

mod = git('show', REF + ':' + MODPATH)
blob = git('rev-parse', REF + ':' + MODPATH).strip()
assert blob == '8bcab4a5d1d98acdbc18bdba1fbddb43f370ed0c'

FAMILY = {
  "name": "completion-valued operation data and the affine automorphisms of the completed body they induce (round OPACT-1, reconstruction)",
  "modules": ["CompletionAction"],
  "status": "kernel-only",
  "manuscript": [],
  "note": ("Round OPACT-1, a native round under AGENTS.md §A.39, executed under the frozen control plane "
           "programmes/oi-qm/reconstruction/round-opact-1-completion-action/preregistration.md. The kernel layer "
           "defines a completion-valued operation datum, which carries each stage preparation to a point of the "
           "completed body, and the two respect conditions StateRespect and AffineRespect; AffineRespect implies "
           "StateRespect and not conversely (midOp_stateRespect, midOp_not_affineRespect). Under AffineRespect a datum "
           "induces exactly one affine map of the chart of a nonempty completed body of finite rank "
           "(existsUnique_induced), an affine extension forces AffineRespect (affineRespect_of_induced), the induced map "
           "preserves the completed body (induced_mem) and composes (induced_after), a datum with an inverse datum "
           "induces an affine equivalence that preserves the body (preservesBody_inducedEquiv), and stage effects read "
           "after the induced map are effects (isEffectOn_pullback). Carried by no manuscript. Nothing here supplies an "
           "operation, a flow, transitivity, an invariant inner product, a dimension or a ball, and nothing uses SC∞.")}

# the execution's census and import files: D's with exactly the one insertion
dcen = json.loads(git('show', D + ':verification/lean-manuscript-census.json'))
k = [i for i, f in enumerate(dcen['families']) if f['name'].startswith('the stage completion')]
assert len(k) == 1
ecen = dict(dcen); ecen['families'] = dcen['families'][:k[0] + 1] + [FAMILY] + dcen['families'][k[0] + 1:]
open(os.path.join(H, 'census.json'), 'w').write(json.dumps(ecen, indent=2, ensure_ascii=False) + '\n')
dimp = git('show', D + ':verification/lean-mathlib/OIBridge.lean')
a = 'import OIBridge.StageCompletion\n'
assert dimp.count(a) == 1
eimp = dimp.replace(a, a + 'import OIBridge.CompletionAction\n', 1)
open(os.path.join(H, 'OIBridge.lean'), 'w').write(eimp)
assert eimp == git('show', REF + ':verification/lean-mathlib/OIBridge.lean')

DOC = """  S1  premise     every load-bearing theorem and construction of the completion action carries `AffineRespect` among
                  its hypotheses and never `StateRespect`; the extension theorem carries its affine-relation
                  hypothesis; `StateRespect` occurs only in its definition, in `stateRespect_of_affineRespect`, in the
                  separation witness and twice in the verdict
  S2  separation  the witness `midOp_stateRespect : StateRespect midOp` and `midOp_not_affineRespect :
                  ¬ AffineRespect midOp` are kernel theorems with prints, stated exactly; the verdict carries
                  `StateRespect midOp ∧ ¬ AffineRespect midOp` and `AffineRespect T → StateRespect T`
  S3  structure   the inverse equivalence and its `PreservesBody` carry both inverse-availability hypotheses; the
                  chart exists only under `FiniteRank (body D)` and a nonempty body; every chart-level verdict
                  clause quantifies a `CompletionChart`; no theorem concludes `PreservesBody` without `Undoes`
  S4  neutrality  no declaration, conclusion or code mentions a drive, a flow, transitivity, an invariant inner
                  product, a dimension, a ball or ellipsoid, SC∞, countability, a concrete gate or phase, or
                  `stageEffects`; the only concrete `OpDatum` is the countermodel `midOp`
  S5  header      the header carries the downstream-neutrality disclaimer"""

CODE = r'''VERDICT = 'opact1_core'
LOAD = ('gen_relation', 'exists_induced', 'existsUnique_induced', 'induced', 'induced_gen', 'induced_mem', 'after',
        'comp_gen', 'affineRespect_after', 'induced_after', 'Undoes', 'comp_eq_id', 'inducedEquiv',
        'inducedEquiv_apply', 'inducedEquiv_symm_apply', 'preservesBody_inducedEquiv', 'isEffectOn_pullback')
STATE_OK = ('StateRespect', 'stateRespect_of_affineRespect', 'midOp_stateRespect', VERDICT)
REL_HYP = ('(h : ∀ (s : Finset ι) (c : ι → ℝ), ∑ i ∈ s, c i = 0 → ∑ i ∈ s, c i • v i = 0 → '
           '∑ i ∈ s, c i • u i = 0)')
INV = ('(hST : Undoes C S T hS)', '(hTS : Undoes C T S hT)')
FORBIDDEN_CODE = re.compile(r'(ElementaryDrivability|OperationalDrive|BoundaryTransitive|SCInf|invMatrix|momentMatrix|'
                            r'ball3|ball4|\bball\b|llipsoid|Countable|ountable|Clifford|Hadamard|gateFlow|rot3|'
                            r'stageEffects|ℝ → OpDatum|finrank)')
FORBIDDEN_NAME = re.compile(r'(rive|[Ff]low|ransitiv|llipsoid|[Bb]all|nnerProduct|[Dd]im3|[Gg]ate|[Pp]hase|lifford|'
                            r'ountab|SCInf|scInf)')
DISCLAIMER = ('Nothing here supplies an operation datum, a flow, transitivity, an invariant inner product, a '
              'dimension or a ball, and nothing uses SC∞.')


def semantic_checks(mod, texts, kinds, prints, tag):
    bad = []
    for n in LOAD:
        t = texts.get(n)
        if t is None:
            bad.append(n + '?')
            continue
        b = split_statement(t)[0] if kinds.get(n) in ('theorem', 'lemma') else t
        if 'AffineRespect' not in b or 'StateRespect' in b:
            bad.append(n)
    stray = sorted(n for n, t in texts.items() if 'StateRespect' in t and n not in STATE_OK)
    vt = texts.get(VERDICT, '')
    check('S1', 'every load-bearing statement requires AffineRespect, never StateRespect%s%s'
          % (tag, (' %s' % (bad + stray)[:4]) if bad or stray else ''),
          not bad and not stray and REL_HYP in norm(texts.get('exists_affine_of_relations', ''))
          and vt.count('StateRespect') == 2)
    check('S2', 'the separation witness StateRespect ∧ ¬ AffineRespect is proved and stated exactly' + tag,
          norm(texts.get('midOp_stateRespect', '')) == 'theorem midOp_stateRespect : StateRespect midOp'
          and norm(texts.get('midOp_not_affineRespect', '')) == 'theorem midOp_not_affineRespect : ¬ AffineRespect midOp'
          and all('OIBridge.CompletionAction.' + n in prints for n in ('midOp_stateRespect', 'midOp_not_affineRespect',
                                                                       'stateRespect_of_affineRespect'))
          and 'StateRespect midOp ∧ ¬ AffineRespect midOp' in norm(vt)
          and 'AffineRespect T → StateRespect T' in norm(vt)
          and split_statement(texts.get('stateRespect_of_affineRespect', 'x x'))[1].strip() == 'StateRespect T')
    cc = norm(texts.get('exists_completionChart', ''))
    pb_bad = [n for n, t in texts.items() if kinds.get(n) in ('theorem', 'lemma') and n != VERDICT
              and 'PreservesBody' in split_statement(t)[1] and not all(h in norm(t) for h in INV)]
    check('S3', 'inverse availability, FiniteRank and the chart are required where used%s%s'
          % (tag, (' %s' % pb_bad[:3]) if pb_bad else ''),
          all(h in norm(texts.get(n, '')) for n in ('inducedEquiv', 'inducedEquiv_symm_apply',
                                                    'preservesBody_inducedEquiv') for h in INV)
          and '(hfr : FiniteRank (body D))' in cc and '(hne : (body D).Nonempty)' in cc
          and 'Nonempty (CompletionChart D)' in cc and not pb_bad
          and '(body D).Nonempty → FiniteRank (body D) → Nonempty (CompletionChart D)' in norm(vt)
          and norm(vt).count('(C : CompletionChart D)') == 4 and all(h in norm(vt) for h in INV))
    code = code_only(mod)
    names = [n for _, n in decls(mod)]
    ops = [n for n, t in texts.items() if re.search(r':\s*OpDatum (?!D\b)\w+\s+where', t)]
    check('S4', 'no drive, flow, transitivity, inner product, dimension, ball, SC∞, gate or stageEffects closure%s'
          % tag, not FORBIDDEN_CODE.search(code) and not any(FORBIDDEN_NAME.search(n) for n in names)
          and ops == ['midOp'])
    check('S5', 'the header disclaimer is present' + tag, DISCLAIMER in norm(header(mod)))'''

MUT = r'''    must_fail('S1', 'AffineRespect replaced by StateRespect in body preservation',
              replace_once(mod, 'theorem induced_mem {T : OpDatum D} (hT : AffineRespect T)',
                           'theorem induced_mem {T : OpDatum D} (hT : StateRespect T)'))
    must_fail('S1', 'the affine-relation hypothesis removed from the extension theorem',
              replace_once(mod, """    (h : ∀ (s : Finset ι) (c : ι → ℝ), ∑ i ∈ s, c i = 0 → ∑ i ∈ s, c i • v i = 0 →
      ∑ i ∈ s, c i • u i = 0) :
    ∃ Φ""", """    :
    ∃ Φ"""))
    must_fail('S1', 'a load-bearing theorem stated under StateRespect',
              append_decl(mod, 'theorem induced_of_state {T : OpDatum D} (hT : StateRespect T) : True := trivial'))
    must_fail('S2', 'the separation witness weakened',
              replace_once(mod, 'theorem midOp_not_affineRespect : ¬ AffineRespect midOp',
                           'theorem midOp_not_affineRespect : ¬ StateRespect midOp'))
    must_fail('S3', 'inverse availability dropped from PreservesBody',
              replace_once(mod, '(hT : AffineRespect T) (hST : Undoes C S T hS) (hTS : Undoes C T S hT) :\n    PreservesBody',
                           '(hT : AffineRespect T) (hST : Undoes C S T hS) :\n    PreservesBody'))
    must_fail('S3', 'FiniteRank removed from the chart theorem',
              replace_once(mod, '(hne : (body D).Nonempty) (hfr : FiniteRank (body D)) :',
                           '(hne : (body D).Nonempty) :'))
    must_fail('S4', 'a one-parameter group of operations',
              append_decl(mod, 'noncomputable def phaseFlow (D : DirectedStages) : ℝ → OpDatum D := by\n'
                               '  exact absurd rfl rfl'))
    must_fail('S4', 'a stage-effect closure claim',
              append_decl(mod, 'theorem closed {T : OpDatum D} (hT : AffineRespect T) (a : Label D) :\n'
                               '    (coord D a).comp (chart C.L C.p0) ∈ stageEffects D := by\n  exact absurd rfl rfl'))
    must_fail('S4', 'a concrete operation datum',
              append_decl(mod, 'noncomputable def gateOp : OpDatum midD where\n'
                               '  τ x := prepVec midD x\n  mem_body x := prepVec_mem_body midD x'))
    must_fail('S5', 'the disclaimer dropped',
              replace_once(mod, 'and nothing uses SC∞.', 'and SC∞ is used.'))'''

def j(x):
    s = json.dumps(x, ensure_ascii=False, indent=1)
    assert "'''" not in s
    return s

t = base
rep = {'@@ROUND@@': 'OPACT-1', '@@RDIR@@': RDIR, '@@MODPATH@@': MODPATH, '@@MODBLOB@@': blob,
       '@@NEWIMPORT@@': 'import OIBridge.CompletionAction\\n', '@@CENSUS_FAMILY@@': j(FAMILY),
       '@@DECLS@@': j([list(x) for x in ns['decls'](mod)]), '@@TEXTS@@': j(ns['decl_texts'](mod)),
       '@@PRINTS@@': j(re.findall(r'^#print axioms (\S+)', mod, re.M)), '@@PREAMBLE@@': j(ns['preamble'](mod)),
       '@@CONTEXT@@': j(ns['context_lines'](mod)), '@@SEMANTIC_DOC@@': DOC, '@@SEMANTIC_CODE@@': CODE,
       '@@SEMANTIC_MUTATIONS@@': MUT}
for kk, v in rep.items():
    assert kk in t, kk
    t = t.replace(kk, v)
assert '@@' not in t
open(os.path.join(H, 'controls.py'), 'w').write(t)
print(blob, len(ns['decls'](mod)), 'decls', len(re.findall(r'^#print axioms', mod, re.M)), 'prints',
      len(ns['context_lines'](mod)), 'context lines')
