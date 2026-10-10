def append_control(text, decl):
    """Insert a declaration just before the verdict section (inside §D)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


DIM_HEAD = ('theorem dim_of_nativeGateOf (hd : 0 < d) (hE : EffectsOn (eball d) avail)\n'
            '    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r)\n'
            '    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n'
            '    {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} {T : W d ≃ₗ[ℝ] W d}\n'
            '    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 1 ∨ d = 3 :=\n'
            '  dim_of_nativeGate hN (nativeGate_of_avail hd hE hG hP1 hK hV4 hT)')
GENERIC = ('theorem %s {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
           '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} %s : %s := by\n'
           '  exact absurd %s (by simp)')


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    check('T', 'the reference module reads %s' % verdict_of(mod), verdict_of(mod) == [TOKENS[0]])
    check('T', 'DIM-1\'s NativeGate, Entangling and jointStates at D are the embedded texts',
          decl_chunks(show(D, 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'))['NativeGate'][1]
          == DIM1_NATIVEGATE
          and decl_chunks(show(D, 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'))['Entangling'][1]
          == DIM1_ENTANGLING
          and decl_chunks(show(D, 'verification/lean-mathlib/OIBridge/CompositeDimension.lean'))['jointStates'][1]
          == DIM1_JOINTSTATES)
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem k1b_core :', '\ntheorem k1b_core\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {Ω : Set (Fin d → ℝ)}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace\n', '\n'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, '(h : maxConeOf avail = maxCone Ω) : jointStatesOf avail = jointStates Ω := by',
                           '(h : maxConeOf avail ⊆ maxCone Ω) : jointStatesOf avail = jointStates Ω := by'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed',
              replace_once(mod, '#print axioms OIBridge.K1Bridge.jointStatesOf_eq\n', ''))
    # S1
    must_fail('S1', 'a positivity clause returned to DIM-1\'s cone',
              replace_once(mod, '  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxConeOf avail',
                           '  posFwd : ∀ x ∈ Ω, ∀ y ∈ Ω, T (prodState x y) ∈ maxCone Ω'))
    must_fail('S1', 'the frame weakened',
              replace_once(mod, '  frame : ∀ a b : Fin 2,\n    T (prodState',
                           '  frame : ∀ a : Fin 2, ∀ b : Fin 1,\n    T (prodState'))
    must_fail('S1', 'a NOT relation dropped',
              replace_once(mod, '  relC : ∀ ω, actC N (T (actC N ω)) = actT N (T ω)\n', ''))
    must_fail('S1', 'the entangling clause on DIM-1\'s joint states',
              replace_once(mod, 'T (prodState x y) ∈ (jointStatesOf avail).extremePoints ℝ ∧',
                           'T (prodState x y) ∈ (jointStates Ω).extremePoints ℝ ∧'))
    # S2
    must_fail('S2', 'the mixing closure added to the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hN : IsNot (eball d) z N)',
                                                           '(hM : MixingClosed avail) (hN : IsNot (eball d) z N)')))
    must_fail('S2', '`0 < d` dropped from the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hd : 0 < d) ', '')
                           .replace('nativeGate_of_avail hd', 'nativeGate_of_avail (by omega)')))
    must_fail('S2', 'effect soundness dropped from the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace(' (hE : EffectsOn (eball d) avail)', '')))
    must_fail('S2', 'DIM-1\'s NOT dropped from the dimension selector',
              replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hN : IsNot (eball d) z N) ', '')))
    must_fail('S2', 'the entangling clause dropped from the three selector',
              replace_once(mod, '    (hEnt : EntanglingOf (eball d) avail T) : d = 3 :=',
                           '    : d = 3 :='))
    # S3
    must_fail('S3', 'the dimension selector proved without DIM-1\'s selector',
              replace_once(mod, '  dim_of_nativeGate hN (nativeGate_of_avail hd hE hG hP1 hK hV4 hT)',
                           '  by exact absurd hd (by simp)'))
    must_fail('S3', 'a dimension-argument token',
              append_control(mod, 'theorem extra_rank : finrank ℝ (Fin 1 → ℝ) = 1 := by simp'))
    # S4
    must_fail('S4', 'the relative native-gate hypotheses concluded from the seed orbit',
              append_control(mod, GENERIC % ('gate_of_orbit', '{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}'
                                             ' {T : W d ≃ₗ[ℝ] W d} (hV4 : SeedOrbitAvailable G r avail)',
                                             'NativeGateOf (eball d) avail z N T', 'hV4')))
    must_fail('S4', 'effect soundness concluded for a hypothesis-bound family',
              append_control(mod, GENERIC % ('effects_of_orbit', '(hV4 : SeedOrbitAvailable G r avail)',
                                             'EffectsOn (eball d) avail', 'hV4')))
    must_fail('S4', 'DIM-1\'s native-gate hypotheses concluded without the relative form',
              append_control(mod, GENERIC % ('gate_free', '{z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}'
                                             ' {T : W d ≃ₗ[ℝ] W d} (hd : 0 < d)',
                                             'NativeGate (eball d) z N T', 'hd')))
    # S5
    must_fail('S5', 'a landed definition re-declared', append_control(mod, 'def maxCone : ℕ := 0'))
    must_fail('S5', 'a second import',
              replace_once(mod, 'import OIBridge.EffectSpace\n',
                           'import OIBridge.EffectSpace\nimport OIBridge.SubstratumSource\n'))
    # S6
    must_fail('S6', 'a complex scalar', append_control(mod, 'def cvec (z : Fin d → ℂ) : Fin d → ℂ := z'))
    must_fail('S6', 'a mixing-closure token',
              append_control(mod, 'def mixed (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop := MixingClosed A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  Round DIM-1 states', '  OI supplies the effects. Round DIM-1 states'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('The relative selectors remove the full effect set from K1; the four hypotheses are '
                          'named premises.')
          and phrase_hits('Hence local tomography\nis derived.') == ['local tomography is derived'])
    # S8
    must_fail('S8', '`0 < d` added to the cone-equality transport',
              replace_once(mod, 'theorem nativeGate_of_cone_eq {Ω : Set (Fin d → ℝ)}',
                           'theorem nativeGate_of_cone_eq (hd : 0 < d) {Ω : Set (Fin d → ℝ)}'))
    must_fail('S8', 'a dimension-three object in the bridge section',
              replace_once(mod, '/-! ### §C', 'theorem three_ball : eball 3 = eball 3 := rfl\n\n/-! ### §C'))
    must_fail('S8', 'the control family in the bridge section',
              replace_once(mod, '/-! ### §C', 'theorem axis_self : axisFamily = axisFamily := rfl\n\n/-! ### §C'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.K1Bridge.k1b_core\n',
                           '#print axioms OIBridge.K1Bridge.k1b_core\n'
                           '#print axioms OIBridge.K1Bridge.NativeGateOf\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.K1Bridge.dim_of_nativeGateOf\n',
                           '#print axioms OIBridge.K1Bridge.dim_of_nativeGateOf\n'
                           '#print axioms OIBridge.K1Bridge.dim_of_nativeGateOf\n'))
    # V -- the decision rule reads the alternatives
    m_mix = replace_once(mod, DIM_HEAD, DIM_HEAD.replace('(hN : IsNot (eball d) z N)',
                                                         '(hM : MixingClosed avail) (hN : IsNot (eball d) z N)'))
    check('M', 'decision rule: the dimension selector with the mixing closure reads NOT-ESTABLISHED',
          verdict_of(m_mix) == [TOKENS[1]])
    m_zero = replace_once(mod, 'theorem cone_eq_fails_zero : maxConeOf (sharpFamily 0) ≠ maxCone (eball 0) :=',
                          'theorem cone_eq_fails_zero : maxConeOf (sharpFamily 0) = maxConeOf (sharpFamily 0) :=')
    check('M', 'decision rule: the d = 0 control weakened reads NOT-ESTABLISHED', verdict_of(m_zero) == [TOKENS[1]])
    m_axis = replace_once(mod, 'theorem cone_eq_fails_axis : EffectsOn (eball 3) axisFamily ∧ maxConeOf axisFamily '
                               '≠ maxCone (eball 3) :=',
                          'theorem cone_eq_fails_axis : EffectsOn (eball 3) axisFamily :=')
    check('M', 'decision rule: the one-axis control weakened reads NOT-ESTABLISHED',
          verdict_of(m_axis) == [TOKENS[1]])
    m_rel = replace_once(mod, '  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxConeOf avail',
                         '  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, T.symm (prodState x y) ∈ maxCone Ω')
    check('M', 'decision rule: a relative form that is not DIM-1\'s with the family\'s cone reads NOT-ESTABLISHED',
          verdict_of(m_rel) == [TOKENS[1]])
    check('M', 'note tokens: exactly the stated verdict is found',
          note_tokens('Outcome: K1-EFFECT-AVAILABILITY-DISCHARGED.') == [TOKENS[0]]
          and note_tokens('K1-EFFECT-AVAILABILITY-DISCHARGED, not K1-BRIDGE-NOT-ESTABLISHED.') == list(TOKENS)
          and note_tokens('nothing') == [])
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
