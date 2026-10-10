def append_control(text, decl):
    """Insert a declaration just before the verdict section (inside §F)."""
    i = text.index('\n/-! ### The verdict')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


CONE_HEAD = ('theorem cone_of_orbit (hd : 0 < d) (hG : PreservesBody (eball d) G)\n'
             '    (hP1 : SharpSeed (eball d) r) (hK : BoundaryTransitive (eball d) G)\n'
             '    (hV4 : SeedOrbitAvailable G r avail) :')
SET_HEAD = ('    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) (hM : MixingClosed avail) :\n'
            '    fullEffects (eball d) ⊆ avail := by')
DERIVED_SET = ('theorem fullEffects_of_orbit_alone {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
               '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)} (hd : 0 < d)\n'
               '    (hG : PreservesBody (eball d) G) (hP1 : SharpSeed (eball d) r) '
               '(hK : BoundaryTransitive (eball d) G)\n'
               '    (hV4 : SeedOrbitAvailable G r avail) : fullEffects (eball d) ⊆ avail := by\n'
               '  exact absurd hd (by simp)')
INSUFF_SET = ('theorem insufficient_with_mixing (hd : 0 < d) : ∃ (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))\n'
              '    (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), PreservesBody (eball d) G ∧\n'
              '    SharpSeed (eball d) r ∧ BoundaryTransitive (eball d) G ∧ SeedOrbitAvailable G r avail ∧\n'
              '    unitEff d ∈ avail ∧ MixingClosed avail ∧ ¬ fullEffects (eball d) ⊆ avail := by\n'
              '  exact absurd hd (by simp)')
INSUFF_CONE = ('theorem cone_insufficient (hd : 0 < d) : ∃ (G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ)))\n'
               '    (r : (Fin d → ℝ) →ᵃ[ℝ] ℝ) (avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)), PreservesBody (eball d) G ∧\n'
               '    SharpSeed (eball d) r ∧ BoundaryTransitive (eball d) G ∧ SeedOrbitAvailable G r avail ∧\n'
               '    unitEff d ∈ avail ∧ MixingClosed avail ∧ EffectsOn (eball d) avail ∧\n'
               '    maxConeOf avail ≠ maxCone (eball d) := by\n'
               '  exact absurd hd (by simp)')


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    st, cone = verdict_of(mod)
    check('T', 'the reference module reads Q-SET %s and Q-CONE %s' % (st, cone),
          st == ['CONDITIONAL-FULL-EFFECTS'] and cone == ['CONE-DERIVED'])
    # N1-N3
    must_fail('N1', 'a renamed declaration', replace_once(mod, '\ntheorem eff1_core :', '\ntheorem eff1_core\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {Ω : Set (Fin d → ℝ)}\n'))
    must_fail('N2', 'a changed preamble',
              replace_once(mod, 'open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension '
                                'CompositeInterface',
                           'open Set KInfFoundations OrbitGeneration TransitiveBody CompositeDimension'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem sharpEff_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 = 1) : sharpEff b b = 1',
                           'theorem sharpEff_self {b : Fin d → ℝ} (hb : ∑ j, b j ^ 2 ≤ 1) : sharpEff b b = 1'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed',
              replace_once(mod, '#print axioms OIBridge.EffectSpace.lor_decomp\n', ''))
    # S1
    must_fail('S1', 'the mixing closure added to the cone theorem',
              replace_once(mod, CONE_HEAD, CONE_HEAD[:-2] + ' (hU : unitEff d ∈ avail)\n'
                                                            '    (hM : MixingClosed avail) :'))
    must_fail('S1', 'one inclusion of the cone equality dropped from its proof',
              replace_once(mod, '  Set.Subset.antisymm (maxConeOf_sharp_subset_maxCone hd) '
                                'maxCone_subset_maxConeOf_sharp',
                           '  Set.Subset.antisymm (maxConeOf_sharp_subset_maxCone hd) (fun ω hω => by\n'
                           '    intro e he f hf\n    exact absurd he (by simp))'))
    must_fail('S1', 'an effect premise on the generation theorem',
              replace_once(mod, '    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail) :\n'
                                '    sharpFamily d ⊆ avail := by',
                           '    (hK : BoundaryTransitive (eball d) G) (hV4 : SeedOrbitAvailable G r avail)\n'
                           '    (hE : EffectsOn (eball d) avail) : sharpFamily d ⊆ avail := by'))
    must_fail('S1', '`0 < d` added to the free inclusion',
              replace_once(mod, 'theorem maxCone_subset_maxConeOf_sharp :',
                           'theorem maxCone_subset_maxConeOf_sharp (hd : 0 < d) :'))
    # S2
    must_fail('S2', 'the mixing closure dropped from the set generation',
              replace_once(mod, SET_HEAD, '    (hV4 : SeedOrbitAvailable G r avail) (hU : unitEff d ∈ avail) :\n'
                                          '    fullEffects (eball d) ⊆ avail := by'))
    must_fail('S2', 'the countermodel weakened to keep the mixing closure open',
              replace_once(mod, '      ¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d '
                                ':= by',
                           '      ¬ fullEffects (eball d) ⊆ sharpUnitFamily d := by'))
    must_fail('S2', 'the upper bound with a weaker radius',
              replace_once(mod, '    ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ min a (1 - a) ∧\n'
                                '      ∀ x, e x = a + ∑ j, v j * x j := by',
                           '    ∃ (a : ℝ) (v : Fin d → ℝ), Real.sqrt (∑ j, v j ^ 2) ≤ 1 ∧\n'
                           '      ∀ x, e x = a + ∑ j, v j * x j := by'))
    # S3
    must_fail('S3', 'the cone restricted to normalized effects',
              replace_once(mod, '  {ω | ∀ e ∈ A, ∀ f ∈ A, 0 ≤ prodEffVal e f ω}',
                           '  {ω | ∀ e ∈ A, ∀ f ∈ A, e 0 = 1 / 2 → 0 ≤ prodEffVal e f ω}'))
    must_fail('S3', 'the mixing closure made convex',
              replace_once(mod, '0 ≤ α → 0 ≤ β → α + β ≤ 1 → α • e + β • f ∈ A',
                           '0 ≤ α → 0 ≤ β → α + β = 1 → α • e + β • f ∈ A'))
    # S4
    must_fail('S4', 'the mixing closure concluded from the seed orbit',
              append_control(mod, 'theorem mixing_of_orbit {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
                                  '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n'
                                  '    (hV4 : SeedOrbitAvailable G r avail) : MixingClosed avail := by\n'
                                  '  exact absurd hV4 (by simp)'))
    must_fail('S4', 'seed-orbit availability concluded for a hypothesis-bound family',
              append_control(mod, 'theorem orbit_available {G : Set ((Fin d → ℝ) ≃ᵃ[ℝ] (Fin d → ℝ))}\n'
                                  '    {r : (Fin d → ℝ) →ᵃ[ℝ] ℝ} {avail : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)}\n'
                                  '    (hP1 : SharpSeed (eball d) r) : SeedOrbitAvailable G r avail := by\n'
                                  '  exact absurd hP1 (by simp)'))
    # S5
    must_fail('S5', 'a landed definition re-declared',
              append_control(mod, 'def maxCone : ℕ := 0'))
    must_fail('S5', 'an import outside the whitelist',
              replace_once(mod, 'import OIBridge.CompositeInterface\n',
                           'import OIBridge.CompositeInterface\nimport OIBridge.SubstratumSource\n'))
    # S6
    must_fail('S6', 'a complex scalar',
              append_control(mod, 'def cvec (z : Fin d → ℂ) : Fin d → ℂ := z'))
    must_fail('S6', 'a limit closure',
              append_control(mod, 'def LimitClosed (A : Set ((Fin d → ℝ) →ᵃ[ℝ] ℝ)) : Prop := '
                                  'closure A ⊆ A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  Two separate questions,', '  OI supplies the effects. Two separate questions,'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('The sharp family determines the cone; the mixing closure is a named premise.')
          and phrase_hits('Hence the mixing closure\nis derived.') == ['mixing closure is derived'])
    # S8
    must_fail('S8', '`0 < d` added to the generation theorem',
              replace_once(mod, 'theorem sharpFamily_subset_avail (hG',
                           'theorem sharpFamily_subset_avail (hd : 0 < d) (hG'))
    must_fail('S8', 'a dimension-three object in the generation section',
              replace_once(mod, '/-! ### §D', 'theorem three_ball : eball 3 = eball 3 := rfl\n\n/-! ### §D'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.EffectSpace.eff1_core\n',
                           '#print axioms OIBridge.EffectSpace.eff1_core\n'
                           '#print axioms OIBridge.EffectSpace.sharpVec_zero\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.EffectSpace.cone_of_orbit\n',
                           '#print axioms OIBridge.EffectSpace.cone_of_orbit\n'
                           '#print axioms OIBridge.EffectSpace.cone_of_orbit\n'))
    # V -- the decision rule reads each alternative
    m_cc = replace_once(mod, CONE_HEAD, CONE_HEAD[:-2] + ' (hU : unitEff d ∈ avail)\n    (hM : MixingClosed avail) :')
    check('M', 'decision rule: the cone theorem with the mixing closure reads CONE-CONDITIONAL',
          verdict_of(m_cc)[1] == ['CONE-CONDITIONAL'])
    m_ds = replace_once(mod, SET_HEAD, '    (hV4 : SeedOrbitAvailable G r avail) :\n    fullEffects (eball d) ⊆ avail '
                                       ':= by')
    check('M', 'decision rule: the set theorem without the unit and the mixing closure reads DERIVED-FULL-EFFECTS',
          verdict_of(m_ds)[0] == ['DERIVED-FULL-EFFECTS'])
    m_nc = replace_once(mod, '      ¬ MixingClosed (sharpUnitFamily d) ∧ ¬ fullEffects (eball d) ⊆ sharpUnitFamily d '
                             ':= by',
                        '      ¬ fullEffects (eball d) ⊆ sharpUnitFamily d := by')
    check('M', 'decision rule: without the frozen countermodel Q-SET has no verdict', verdict_of(m_nc)[0] == [])
    m_is = append_control(mod, INSUFF_SET)
    check('M', 'decision rule: a countermodel with the mixing closure reads INSUFFICIENT-EVEN-WITH-MIXING, and two '
               'outcomes fail V', verdict_of(m_is)[0] == ['CONDITIONAL-FULL-EFFECTS', 'INSUFFICIENT-EVEN-WITH-MIXING'])
    must_fail('V', 'two Q-SET outcomes at once', m_is)
    m_ic = append_control(mod, INSUFF_CONE)
    check('M', 'decision rule: a cone countermodel with the mixing closure reads CONE-INSUFFICIENT',
          'CONE-INSUFFICIENT' in verdict_of(m_ic)[1])
    m_dd = append_control(mod, DERIVED_SET)
    must_fail('V', 'a derived set theorem beside the conditional one', m_dd)
    check('M', 'note tokens: exactly the stated verdicts are found',
          note_tokens('Q-SET: CONDITIONAL-FULL-EFFECTS. Q-CONE: CONE-DERIVED.')
          == ['CONDITIONAL-FULL-EFFECTS', 'CONE-DERIVED']
          and note_tokens('Q-CONE: CONE-DERIVED, not CONE-CONDITIONAL.') == ['CONE-DERIVED', 'CONE-CONDITIONAL'])
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
