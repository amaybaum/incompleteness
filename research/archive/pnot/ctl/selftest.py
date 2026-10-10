REL_RELC = '  relC : ∀ ω, actC N (G (actC N ω)) = actT N (G ω)\n'
PAR_HEAD = ('    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) :\n'
            '    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by')
EVEN_HEAD = '    {G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) (hR : GateRel N G) : ¬ Even d :='
PI_HEAD = ('    {G : W 3 ≃ₗ[ℝ] W 3} (hN : IsNot (eball 3) z N) (hR : GateRel N G) :\n'
           '    ∃ u : Fin 3 → ℝ, ∑ j, u j ^ 2 = 1 ∧ ∀ x, N x = (2 * ∑ j, u j * x j) • u - x := by')
DET_HEAD = ('    (hN : IsNot (eball 3) z N) (hR : GateRel N G) : LinearMap.det N = 1 := by\n'
            '  obtain ⟨u, hu, hform⟩ := piRotation_three hN hR')
COR_PROOF = '  det_three hN (gateRel_of_nativeGate hG)\n'
REFL_DEF = 'def refl3 : (Fin 3 → ℝ) →ₗ[ℝ] (Fin 3 → ℝ) := diagSign ![1, 1, -1]'
CNOT_PROOF = 'theorem gateRel_cnot : GateRel nflip cnot := ⟨cnot_relT, cnot_relC⟩'
W5_DEF = 'noncomputable def w5 : Fin 5 → ℝ := fun i => if i = 2 then -3 / 5 else if i = 4 then -4 / 5 else 0'
V5_HEAD = ('theorem gJ5_value :\n'
           '    prodEffVal (sharpEff w5) (sharpEff z5) (gJ5 (prodState x5 z5)) = -1 / 10 := by')
V3_HEAD = ('theorem gJ3_value :\n'
           '    prodEffVal (sharpEff w3) (sharpEff z3) (gJ3 (prodState xplus z3)) = -1 / 10 := by')
PF5 = ('theorem not_posFwd_gJ5 :\n'
       '    ¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gJ5 (prodState x y) ∈ maxCone (eball 5) :=\n'
       '  fun h => gJ5_not_mem_maxCone (h _ x5_mem _ z5_mem)')
FR5 = ('theorem gJ5_frame (a b : Fin 2) :\n'
       '    gJ5 (prodState (corner z5 a) (corner z5 b)) = prodState (corner z5 a) (corner z5 (a + b)) := by')
G5_DEF = 'def gJ5 : W 5 ≃ₗ[ℝ] W 5 := sgateEquiv odd5 perm5 perm5_perm5'
NG5 = 'theorem not_nativeGate_gJ5 : ¬ NativeGate (eball 5) z5 n5 gJ5 :=\n  fun hG => not_posFwd_gJ5 hG.posFwd'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    landed = landed_at_d()
    check('T', 'the landed texts read from D are the frozen ones', landed == LANDED and len(LANDED) == 8)
    module_checks(mod, ' [reference]')
    a, b, c = verdict_of(mod)
    check('T', 'the reference module reads %s, %s and %s' % (a, b, c),
          a == [REL_TOKENS[0]] and b == [NOT_TOKENS[0]] and c == [SEP_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem w3_unit :', '\ntheorem w3_unit\' :'))
    must_fail('N2', 'a changed binder context', replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {k : ℕ}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, 'NativeGateBall CompositeDimension EffectSpace Finset',
                                                       'NativeGateBall CompositeDimension Finset'))
    must_fail('N3', 'a sorry', append_end(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.ParityNot.det_three\n', ''))
    # S1 -- the relations
    must_fail('S1', 'the frame added to GateRel',
              replace_once(mod, REL_RELC, REL_RELC + '  frame : ∀ ω, G ω = G ω\n'))
    must_fail('S1', 'the control relation changed',
              replace_once(mod, REL_RELC, '  relC : ∀ ω, actC N (G (actC N ω)) = G ω\n'))
    lm = dict(LANDED)
    lm['NativeGate#relC'] = lm['NativeGate#relC'].replace('actT N (G ω)', 'G ω')
    check('M', 'relations: a landed relC that differs fails S1 and all three cells',
          not rel_ok(mod, lm) and verdict_of(mod, lm) == ([REL_TOKENS[1]], [NOT_TOKENS[1]], [SEP_TOKENS[1]]))
    # S2 -- the parity pairing
    must_fail('S2', 'the parity theorem with the native gate kept',
              replace_once(mod, PAR_HEAD, PAR_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball d) z N G)')))
    must_fail('S2', 'the parity theorem with positivity added',
              replace_once(mod, PAR_HEAD, PAR_HEAD.replace(
                  '(hR : GateRel N G)', '(hR : GateRel N G)\n    (hP : ∀ x ∈ eball d, ∀ y ∈ eball d, G (prodState x y) ∈ maxCone (eball d))')))
    must_fail('S2', 'the parity conclusion weakened to an inequality',
              replace_once(mod, PAR_HEAD, PAR_HEAD.replace('Module.finrank ℝ (plusSpace N) = Module', 'Module.finrank ℝ (plusSpace N) ≤ Module')))
    must_fail('S2', 'the oddness theorem with the frame added',
              replace_once(mod, EVEN_HEAD, EVEN_HEAD.replace(
                  '(hR : GateRel N G)', '(hR : GateRel N G)\n    (hF : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)))')))
    must_fail('S2', 'a §A proof reading positivity',
              replace_once(mod, '  apply LinearMap.ext; intro u\n  rw [LinearMap.neg_apply, Lop_apply, Pop_apply, Lop_apply]',
                           '  have _hp : maxCone (eball d) = maxCone (eball d) := rfl\n'
                           '  apply LinearMap.ext; intro u\n  rw [LinearMap.neg_apply, Lop_apply, Pop_apply, Lop_apply]'))
    must_fail('S2', 'a local declaration shadowing a landed object of a paired statement (eball)',
              insert_in_section(mod, '/-! ### §A', 'def eball (d : ℕ) : Set (Fin d → ℝ) := Set.univ'))
    lm = dict(LANDED)
    lm['finrank_plus_eq_finrank_minus'] = lm['finrank_plus_eq_finrank_minus'].replace('= Module.finrank', '≤ Module.finrank')
    check('M', 'pairing: a landed parity statement that differs fails the pair and only the relation cell',
          verdict_of(mod, lm) == ([REL_TOKENS[1]], [NOT_TOKENS[0]], [SEP_TOKENS[0]]))
    # S3 -- the NOT at d = 3
    must_fail('S3', 'the π-rotation with the native gate in place of GateRel',
              replace_once(mod, PI_HEAD, PI_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball 3) z N G)')))
    must_fail('S3', 'the π-rotation with the frame added',
              replace_once(mod, PI_HEAD, PI_HEAD.replace(
                  '(hR : GateRel N G)', '(hR : GateRel N G)\n    (hF : ∀ a b : Fin 2, G (prodState (corner z a) (corner z b)) = prodState (corner z a) (corner z (a + b)))')))
    must_fail('S3', 'the π-rotation conclusion weakened (unit axis dropped)',
              replace_once(mod, PI_HEAD, PI_HEAD.replace('∑ j, u j ^ 2 = 1 ∧ ', '')))
    must_fail('S3', 'the determinant conclusion changed to ±1',
              replace_once(mod, DET_HEAD, DET_HEAD.replace('LinearMap.det N = 1 :=', 'LinearMap.det N = 1 ∨ LinearMap.det N = -1 :=')))
    must_fail('S3', 'a §B proof reading positivity',
              replace_once(mod, '  have ht : Module.finrank ℝ (tangentSpace N) = 1 := by',
                           '  have _hp : maxCone (eball 3) = maxCone (eball 3) := rfl\n'
                           '  have ht : Module.finrank ℝ (tangentSpace N) = 1 := by'))
    must_fail('S3', 'a corollary proved without gateRel_of_nativeGate',
              replace_once(mod, COR_PROOF, '  det_three hN ⟨hG.relT, hG.relC⟩\n'))
    m = replace_once(mod, PI_HEAD, PI_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball 3) z N G)'))
    check('M', 'decision rule: a broken π-rotation reads D3-NOT-PI-ROTATION-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([REL_TOKENS[0]], [NOT_TOKENS[1]], [SEP_TOKENS[0]]))
    # S4 -- the controls
    must_fail('S4', 'the reflection control replaced by a rotation',
              replace_once(mod, REFL_DEF, REFL_DEF.replace('![1, 1, -1]', '![-1, -1, 1]')))
    must_fail('S4', 'the positive control proved without the landed cnot relations',
              replace_once(mod, CNOT_PROOF, 'theorem gateRel_cnot : GateRel nflip cnot := gateRel_of_nativeGate nativeGate_cnot'))
    lm = dict(LANDED)
    lm['cnot_relC'] = lm['cnot_relC'].replace('actT nflip (cnot ω)', 'cnot ω')
    check('M', 'controls: a different landed cnot relation fails only the NOT cell',
          verdict_of(mod, lm) == ([REL_TOKENS[0]], [NOT_TOKENS[1]], [SEP_TOKENS[0]]))
    # S5 -- the separation witnesses, both dimensions, the d = 5 witness load-bearing
    must_fail('S5', 'the d = 5 witness replaced by the landed dimension exclusion',
              replace_once(mod, NG5, 'theorem not_nativeGate_gJ5 : ¬ NativeGate (eball 5) z5 n5 gJ5 :=\n'
                                     '  fun hG => ne_five_of_nativeGate isNot_n5 hG rfl'))
    must_fail('S5', 'the d = 5 value changed', replace_once(mod, V5_HEAD, V5_HEAD.replace('= -1 / 10', '< 0')))
    must_fail('S5', 'the d = 3 value changed', replace_once(mod, V3_HEAD, V3_HEAD.replace('= -1 / 10', '= -1 / 5')))
    must_fail('S5', 'the d = 5 witness direction changed',
              replace_once(mod, W5_DEF, W5_DEF.replace('-4 / 5', '4 / 5')))
    must_fail('S5', 'the d = 5 positivity failure weakened to one input',
              replace_once(mod, PF5, PF5.replace('¬ ∀ x ∈ eball 5, ∀ y ∈ eball 5, gJ5 (prodState x y) ∈ maxCone (eball 5)',
                                                  '¬ gJ5 (prodState x5 z5) ∈ maxCone (eball 5)')
                           .replace('fun h => gJ5_not_mem_maxCone (h _ x5_mem _ z5_mem)', 'gJ5_not_mem_maxCone')))
    must_fail('S5', 'the d = 5 frame changed', replace_once(mod, FR5, FR5.replace('(corner z5 (a + b))', '(corner z5 b)')))
    must_fail('S5', 'the d = 5 gate changed', replace_once(mod, G5_DEF, G5_DEF.replace('sgateEquiv odd5 perm5', 'sgateEquiv odd5 (perm5 ∘ perm5)')))
    lm = dict(LANDED)
    lm['NativeGate#posFwd'] = lm['NativeGate#posFwd'].replace('maxCone Ω', 'jointStates Ω')
    check('M', 'separation: a landed posFwd that differs fails only the separation cell',
          verdict_of(mod, lm) == ([REL_TOKENS[0]], [NOT_TOKENS[0]], [SEP_TOKENS[1]]))
    m = replace_once(mod, V5_HEAD, V5_HEAD.replace('= -1 / 10', '< 0'))
    check('M', 'decision rule: a broken d = 5 witness reads POSITIVITY-SEPARATION-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([REL_TOKENS[0]], [NOT_TOKENS[0]], [SEP_TOKENS[1]]))
    m = replace_once(mod, REL_RELC, REL_RELC + '  frame : ∀ ω, G ω = G ω\n')
    check('M', 'decision rule: GateRel broken reads NOT-ESTABLISHED in all three cells',
          verdict_of(m) == ([REL_TOKENS[1]], [NOT_TOKENS[1]], [SEP_TOKENS[1]]))
    # S6 -- scope
    must_fail('S6', 'a dimension conclusion', append_end(mod, 'theorem d_sel {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} '
                                                           '{G : W d ≃ₗ[ℝ] W d} (h : GateRel N G) : d ≠ 2 := sorry'))
    must_fail('S6', 'a complex field', append_end(mod, 'theorem cplx : (Complex.I : ℂ) = Complex.I := rfl'))
    must_fail('S6', 'the landed d = 1 gate', append_end(mod, 'theorem c1 : GateRel neg1 cnot1 := sorry'))
    # S7 -- reuse
    must_fail('S7', 'a landed definition re-declared', append_end(mod, 'def nflip : ℕ := 0'))
    must_fail('S7', 'a second import',
              replace_once(mod, 'import OIBridge.EffectSpace\n', 'import OIBridge.EffectSpace\nimport OIBridge.K2Guard\n'))
    # S8 -- phrases
    must_fail('S8', 'a forbidden phrase in the header',
              replace_once(mod, '  (A) Parity.', '  The relations select d = 3. (A) Parity.'))
    must_fail('S8', 'the design header', replace_once(mod, 'round PARITY-NOT-1:', 'design (round PARITY-NOT-1, not for landing):'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('The two relations give parity; gJ5 satisfies the frame and the relations and fails forward '
                          'positivity at an explicit product state.')
          and phrase_hits('Hence J² = −1\nholds.') == ['J² = −1'])
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.ParityNot.not_posFwd_gJ5\n',
                           '#print axioms OIBridge.ParityNot.not_posFwd_gJ5\n'
                           '#print axioms OIBridge.ParityNot.w5_unit\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.ParityNot.det_three\n',
                           '#print axioms OIBridge.ParityNot.det_three\n#print axioms OIBridge.ParityNot.det_three\n'))
    # V
    m = replace_once(mod, PAR_HEAD, PAR_HEAD.replace('(hR : GateRel N G)', '(hR : NativeGate (eball d) z N G)'))
    check('M', 'decision rule: a broken parity pair reads PARITY-FROM-RELATIONS-NOT-ESTABLISHED and leaves the other '
               'cells unchanged', verdict_of(m) == ([REL_TOKENS[1]], [NOT_TOKENS[0]], [SEP_TOKENS[0]]))
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('PARITY-FROM-RELATIONS-PROVED, D3-NOT-PI-ROTATION-PROVED and POSITIVITY-SEPARATION-PROVED.')
          == ['PARITY-FROM-RELATIONS-PROVED', 'D3-NOT-PI-ROTATION-PROVED', 'POSITIVITY-SEPARATION-PROVED']
          and note_tokens('POSITIVITY-SEPARATION-NOT-ESTABLISHED') == ['POSITIVITY-SEPARATION-NOT-ESTABLISHED'])
    # I, C
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORT, 1)
    check('M', 'imports: the frozen edit passes and a dropped line fails',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp))
    d_cen = show(D, CENSUS)
    good = census_want(d_cen)
    dd = json.loads(d_cen)
    k = [i for i, f in enumerate(dd['families']) if f['modules'] == PREV_FAMILY_MODULES][0]
    bad_status = json.loads(good)
    bad_status['families'][k + 1]['status'] = 'carried'
    bad_status = json.dumps(bad_status, indent=2, ensure_ascii=False) + '\n'
    moved = json.loads(good)
    moved['families'].insert(k, moved['families'].pop(k + 1))
    moved = json.dumps(moved, indent=2, ensure_ascii=False) + '\n'
    check('M', 'census: the frozen edit passes; a changed status, a moved family, a whitespace change and the '
               'unchanged file fail',
          census_ok(d_cen, good) and not census_ok(d_cen, bad_status) and moved != good
          and not census_ok(d_cen, moved) and not census_ok(d_cen, good.replace('\n', '\n ', 1))
          and not census_ok(d_cen, d_cen))


def main(argv):
    if argv == ['--self-test']:
        self_test()
    elif len(argv) == 2 and argv[0] == 'verdict':
        print_verdicts(argv[1])
    elif len(argv) >= 2 and argv[0] == 'check':
        freeze = argv[3] if len(argv) == 4 and argv[2] == '--freeze' else None
        run_check(argv[1], freeze)
    else:
        print(__doc__)
        return 2
    if FAILS:
        print('controls: FAILED (%d of %d): %s' % (len(FAILS), COUNT[0], ' '.join(FAILS)))
        return 1
    print('controls: OK -- %d checks' % COUNT[0])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
