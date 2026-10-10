def append_control(text, decl):
    """Insert a declaration just before the verdict section."""
    i = text.index('\n/-! ### The verdicts')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_in_section(text, marker, decl):
    """Insert a declaration just before the section marker `marker`."""
    i = text.index(marker)
    return text[:i] + decl + '\n\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


CTL_TAIL = ('      IsNot (eball 1) z1 neg1 ∧ NativeGateOf (eball 1) (fullEffects (eball 1)) z1 neg1 cnot1 ∧\n'
            '      ¬ (2 ≤ 1) :=\n  ⟨fun _ he')
NI_TAIL = 'IsNot (eball d) z N →\n          NativeGateOf (eball d) avail z N T → 2 ≤ d) := by'
NI_PROOF = '  obtain ⟨hE, hG, hP1, hK, hV4, hN, hT, h2⟩ := two_le_load_bearing_relative\n'
PRED_TAIL = '    (∃ x ∈ Ω, f x ≠ e x) ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)\n'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    a, b = verdict_of(mod)
    check('T', 'the reference module reads %s and %s' % (a, b), a == [CLASS_TOKENS[0]] and b == [NI_TOKENS[0]])
    sel = show(D, SELECTOR_SRC)
    check('T', 'the landed relative selector at D yields the frozen hypothesis types', selector_types(sel) == SEL_TYPES)
    # N1-N3
    must_fail('N1', 'a renamed declaration',
              replace_once(mod, '\ntheorem k1sharp_classified :', '\ntheorem k1sharp_classified\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ}\n',
                           '\nvariable {V : Type} [NormedAddCommGroup V] [NormedSpace ℝ V] {d : ℕ} {Ω : Set V}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace K1Bridge\n', '\nopen EffectSpace\n'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem z1_sq : ∑ j, z1 j ^ 2 = 1 := by', 'theorem z1_sq : ∑ j, z1 j ^ 2 ≤ 1 := by'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.SharpTests.eq_or_compl_one\n', ''))
    # S1
    must_fail('S1', 'the predicate without the complement clause',
              replace_once(mod, PRED_TAIL, '    (∃ x ∈ Ω, f x ≠ e x)\n'))
    must_fail('S1', 'test identity as equality of maps',
              replace_once(mod, PRED_TAIL, '    f ≠ e ∧ (∃ x ∈ Ω, f x ≠ 1 - e x)\n'))
    # S2
    must_fail('S2', 'the witness requiring 3 ≤ d',
              replace_once(mod, 'theorem hasTwoSharpTests_of_two_le (hd : 2 ≤ d)',
                           'theorem hasTwoSharpTests_of_two_le (hd : 3 ≤ d)'))
    must_fail('S2', 'the equivalence weakened to one direction',
              replace_once(mod, 'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) ↔ 2 ≤ d := by',
                           'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) → 2 ≤ d := by'))
    must_fail('S2', 'the complement identity changed',
              replace_once(mod, 'sharpEff (-b) x = 1 - sharpEff b x := by', 'sharpEff (-b) x = sharpEff b x := by'))
    must_fail('S2', 'the equivalence proved without the d = 1 case',
              replace_once(mod, '    · exact not_hasTwoSharpTests_one h\n', '    · exact absurd h (by simp)\n'))
    must_fail('S2', 'the seed classification without sharp_eq_of_certain',
              replace_once(mod, '  exact ⟨u, sharp_eq_of_certain he hu hw h1 h0⟩', '  exact ⟨u, by simpa using he⟩'))
    # S3
    must_fail('S3', 'a hypothesis dropped from the d = 1 control',
              replace_once(mod, CTL_TAIL, CTL_TAIL.replace('IsNot (eball 1) z1 neg1 ∧ ', '')))
    must_fail('S3', 'a hypothesis dropped from the non-implication',
              replace_once(mod, NI_TAIL, NI_TAIL.replace('IsNot (eball d) z N →\n          ', '')))
    must_fail('S3', 'the non-implication proved without the control',
              replace_once(mod, NI_PROOF, NI_PROOF.replace('two_le_load_bearing_relative', 'k1sharp_aux')))
    sel_m = replace_once(sel, '    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3 := by',
                         '    (hT : NativeGateOf (eball d) avail z N T) : d = 3 := by')
    check('M', 'selector types: a landed selector with a hypothesis dropped does not yield the frozen types',
          selector_types(sel_m) != SEL_TYPES)
    # S4
    must_fail('S4', 'an entangling object mentioned',
              append_control(mod, 'theorem ent_free : True := by\n  have := @Entangling\n  trivial'))
    must_fail('S4', 'the predicate concluded of a general body',
              append_control(mod, 'theorem pred_general (Ω : Set (Fin 2 → ℝ)) (h : HasTwoSharpTests Ω) : '
                                  'HasTwoSharpTests Ω := h'))
    must_fail('S4', 'a theorem concluding 2 ≤ d',
              append_control(mod, 'theorem two_le_free (hd : 3 ≤ d) : 2 ≤ d := by omega'))
    # S5
    must_fail('S5', 'a landed definition re-declared', append_control(mod, 'def fullAut : ℕ := 0'))
    must_fail('S5', 'a second import',
              replace_once(mod, 'import OIBridge.K1Bridge\n', 'import OIBridge.K1Bridge\nimport OIBridge.K2Guard\n'))
    # S6
    must_fail('S6', 'a complex scalar', append_control(mod, 'def cvec (z : Fin 3 → ℂ) : Fin 3 → ℂ := z'))
    must_fail('S6', 'a closure token',
              append_control(mod, 'def closedFamily (A : Set (Fin 2 → ℝ)) : Prop := closure A ⊆ A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  (B) At `d = 1`', '  This is quantumness. (B) At `d = 1`'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('Two sharp binary tests distinct modulo complementation exist exactly when 2 ≤ d; '
                          'the round does not show that OI provides them.')
          and phrase_hits('Hence OI\nsupplies two tests.') == ['OI supplies'])
    # S8
    must_fail('S8', 'a selector object in the classification sections',
              insert_in_section(mod, '/-! ### §C', 'theorem fa_one : fullAut 1 = fullAut 1 := rfl'))
    must_fail('S8', 'the predicate in the selector section',
              append_control(mod, 'theorem pred_d : ¬ HasTwoSharpTests (eball 1) := not_hasTwoSharpTests_one'))
    must_fail('S8', '2 ≤ d in §A',
              insert_in_section(mod, '/-! ### §B', 'theorem two_le_A (hd : 2 ≤ d) : 1 ≤ d := by omega'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.SharpTests.k1sharp_two_le_not_implied\n',
                           '#print axioms OIBridge.SharpTests.k1sharp_two_le_not_implied\n'
                           '#print axioms OIBridge.SharpTests.z1_sq\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.SharpTests.sharpSeed_iff\n',
                           '#print axioms OIBridge.SharpTests.sharpSeed_iff\n'
                           '#print axioms OIBridge.SharpTests.sharpSeed_iff\n'))
    # V -- each cell reads its alternative, independently of the other
    m_pred = replace_once(mod, PRED_TAIL, '    (∃ x ∈ Ω, f x ≠ e x)\n')
    check('M', 'decision rule: the predicate without the complement clause reads MULTIPLICITY-NOT-CLASSIFIED and '
               'leaves the other cell unchanged', verdict_of(m_pred) == ([CLASS_TOKENS[1]], [NI_TOKENS[0]]))
    m_ctl = replace_once(mod, CTL_TAIL, CTL_TAIL.replace('IsNot (eball 1) z1 neg1 ∧ ', ''))
    check('M', 'decision rule: a hypothesis dropped from the control reads NON-IMPLICATION-NOT-ESTABLISHED and leaves '
               'the other cell unchanged', verdict_of(m_ctl) == ([CLASS_TOKENS[0]], [NI_TOKENS[1]]))
    m_iff = replace_once(mod, 'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) ↔ 2 ≤ d := by',
                         'theorem hasTwoSharpTests_iff : HasTwoSharpTests (eball d) → 2 ≤ d := by')
    check('M', 'decision rule: the equivalence weakened to one direction reads MULTIPLICITY-NOT-CLASSIFIED',
          verdict_of(m_iff)[0] == [CLASS_TOKENS[1]])
    m_ni = replace_once(mod, NI_PROOF, NI_PROOF.replace('two_le_load_bearing_relative', 'k1sharp_aux'))
    check('M', 'decision rule: the non-implication proved without the control reads NON-IMPLICATION-NOT-ESTABLISHED',
          verdict_of(m_ni)[1] == [NI_TOKENS[1]])
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED and K1-TWO-LE-NOT-IMPLIED.')
          == ['K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED', 'K1-TWO-LE-NOT-IMPLIED']
          and note_tokens('K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED, not K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED.')
          == ['K1-SHARP-TEST-MULTIPLICITY-CLASSIFIED', 'K1-SHARP-TEST-MULTIPLICITY-NOT-CLASSIFIED'])
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
