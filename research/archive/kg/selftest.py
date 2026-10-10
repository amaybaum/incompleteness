def append_control(text, decl):
    """Insert a declaration just before the verdict section."""
    i = text.index('\n/-! ### The verdicts')
    return text[:i] + '\n' + decl + '\n' + text[i:]


def insert_in_section(text, marker, decl):
    """Insert a declaration just before the section marker that follows `marker`."""
    i = text.index(marker)
    return text[:i] + decl + '\n\n' + text[i:]


def verdict_of(mod2):
    return verdicts(decl_chunks(mod2))


OBS_HEAD = ('theorem no_candidateCone_cnot_reflY {K : Set (W 3)} (hK : CandidateCone K)\n'
            '    (hC : ∀ ω ∈ K, cnot ω ∈ K) (hR : ∀ ω ∈ K, actT reflY ω ∈ K) : False := by')
SEL_HEAD = ('    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) (hN : IsNot (eball d) z N) (hG : NativeGate (eball d) z N G) :\n'
            '    d = 3 := by')
REL_TAIL = '    (hN : IsNot (eball d) z N) (hT : NativeGateOf (eball d) avail z N T) : d = 3 := by'


def self_test():
    mod = git('cat-file', '-p', MOD_REFERENCE_BLOB).stdout
    check('T', 'the reference module blob is readable', bool(mod))
    module_checks(mod, ' [reference]')
    o, e = verdict_of(mod)
    check('T', 'the reference module reads %s and %s' % (o, e), o == [ORIENT_TOKENS[0]] and e == [ENT_TOKENS[0]])
    # N1-N3
    must_fail('N1', 'a renamed declaration',
              replace_once(mod, '\ntheorem k2guard_entangling :', '\ntheorem k2guard_entangling\' :'))
    must_fail('N2', 'a changed binder context',
              replace_once(mod, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {Ω : Set (Fin d → ℝ)}\n'))
    must_fail('N2', 'a changed open line', replace_once(mod, '\nopen EffectSpace K1Bridge\n', '\nopen EffectSpace\n'))
    must_fail('N2', 'a changed statement',
              replace_once(mod, 'theorem reflY_reflY (x : Fin 3 → ℝ) : reflY (reflY x) = x := by',
                           'theorem reflY_reflY (x : Fin 3 → ℝ) : reflY (reflY (reflY x)) = reflY x := by'))
    must_fail('N3', 'a sorry', append_control(mod, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', replace_once(mod, '#print axioms OIBridge.K2Guard.chain_eq\n', ''))
    # S1
    must_fail('S1', 'the reflection replaced by a rotation',
              replace_once(mod, 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i',
                           'toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i'))
    must_fail('S1', 'the candidate family narrowed by an extra condition',
              replace_once(mod, '  (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3)\n',
                           '  (∀ x ∈ eball 3, ∀ y ∈ eball 3, prodState x y ∈ K) ∧ K ⊆ maxCone (eball 3) ∧ '
                           'K.Countable\n'))
    must_fail('S1', 'an extra hypothesis on the obstruction',
              replace_once(mod, OBS_HEAD, OBS_HEAD.replace('(hR : ∀ ω ∈ K, actT reflY ω ∈ K) : False',
                                                           '(hR : ∀ ω ∈ K, actT reflY ω ∈ K) (hP : K.Nonempty) : '
                                                           'False')))
    must_fail('S1', 'the obstruction proved without the chain',
              replace_once(replace_once(mod, '  rw [chain_value] at hv\n  norm_num at hv',
                                        '  exact absurd hv (by norm_num)'),
                           ':= by rw [← chain_eq]; exact hK.2 h2', ':= hK.2 (by simpa using h2)'))
    # S2
    must_fail('S2', 'the rotation control weakened',
              replace_once(mod, '      (cnot (actT nflip (cnot (prodState xplus z3)))) = 0 := by',
                           '      (cnot (actT nflip (cnot (prodState xplus z3)))) ≤ 0 := by'))
    must_fail('S2', 'the determinant control dropped from the verdict',
              replace_once(mod, '    (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det reflY = -1 ∧ '
                                'LinearMap.det nflip = 1 ∧\n',
                           '    (∀ x ∈ eball 3, reflY x ∈ eball 3) ∧ LinearMap.det nflip = 1 ∧\n'))
    # S3
    must_fail('S3', 'the entangling clause added to the selector',
              replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hG : NativeGate (eball d) z N G) :',
                                                           '(hG : NativeGate (eball d) z N G)\n'
                                                           '    (hE : Entangling (eball d) G) :')))
    must_fail('S3', '`2 ≤ d` dropped from the selector',
              replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hd : 2 ≤ d) ', '')))
    must_fail('S3', 'the relative selector with K1-BRIDGE-1\'s `0 < d` only',
              replace_once(mod, 'theorem three_of_nativeGateOf_of_two_le (hd : 2 ≤ d)',
                           'theorem three_of_nativeGateOf_of_two_le (hd : 0 < d)'))
    must_fail('S3', 'a second theorem concluding `2 ≤ d`',
              append_control(mod, 'theorem two_le_free (hd : 3 ≤ d) : 2 ≤ d := by omega'))
    # S4
    must_fail('S4', 'the entangling clause concluded from `2 ≤ d`',
              append_control(mod, 'theorem entangling_of_two_le {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) : '
                                  'Entangling (eball d) G := by\n  exact absurd hd (by omega)'))
    must_fail('S4', 'a native gate concluded for a hypothesis-bound gate',
              append_control(mod, 'theorem gate_free {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)}\n'
                                  '    {G : W d ≃ₗ[ℝ] W d} (hd : 2 ≤ d) : NativeGate (eball d) z N G := by\n'
                                  '  exact absurd hd (by omega)'))
    # S5
    must_fail('S5', 'a landed definition re-declared', append_control(mod, 'def maxCone : ℕ := 0'))
    must_fail('S5', 'a second import',
              replace_once(mod, 'import OIBridge.K1Bridge\n', 'import OIBridge.K1Bridge\nimport OIBridge.SubstratumSource\n'))
    # S6
    must_fail('S6', 'a complex scalar', append_control(mod, 'def cvec (z : Fin 3 → ℂ) : Fin 3 → ℂ := z'))
    must_fail('S6', 'a closure token',
              append_control(mod, 'def closedFamily (A : Set (W 3)) : Prop := closure A ⊆ A'))
    # S7
    must_fail('S7', 'a forbidden phrase in the header',
              replace_once(mod, '  (A) The candidate-cone family', '  The physical cone is identified. (A) The '
                                                                     'candidate-cone family'))
    check('M', 'the result-note phrase test passes a neutral note and fails one with a forbidden phrase',
          not phrase_hits('No candidate cone is invariant under cnot and the one-copy reflection; 2 ≤ d stays a '
                          'premise.')
          and phrase_hits('Hence reflections are\nphysically forbidden.') == ['reflections are physically forbidden'])
    # S8
    must_fail('S8', 'a dimension-three object in the selector section',
              insert_in_section(mod, '/-! ### §F', 'theorem three_ball_sel : eball 3 = eball 3 := rfl'))
    must_fail('S8', '`2 ≤ d` in the orientation section',
              insert_in_section(mod, '/-! ### §B', 'theorem two_le_A (hd : 2 ≤ d) : 1 ≤ d := by omega'))
    # S9
    must_fail('S9', 'an extra print',
              replace_once(mod, '#print axioms OIBridge.K2Guard.k2guard_entangling\n',
                           '#print axioms OIBridge.K2Guard.k2guard_entangling\n'
                           '#print axioms OIBridge.K2Guard.reflY_reflY\n'))
    must_fail('S9', 'a duplicated print',
              replace_once(mod, '#print axioms OIBridge.K2Guard.chain_value\n',
                           '#print axioms OIBridge.K2Guard.chain_value\n#print axioms OIBridge.K2Guard.chain_value\n'))
    # V -- each cell reads its alternative, independently of the other
    m_rot = replace_once(mod, 'toFun x := fun i => (![1, -1, 1] : Fin 3 → ℝ) i * x i',
                         'toFun x := fun i => (![1, -1, -1] : Fin 3 → ℝ) i * x i')
    check('M', 'decision rule: the reflection replaced by a rotation reads ORIENTATION-NOT-ESTABLISHED and leaves the '
               'entangling cell unchanged', verdict_of(m_rot) == ([ORIENT_TOKENS[1]], [ENT_TOKENS[0]]))
    m_ent = replace_once(mod, SEL_HEAD, SEL_HEAD.replace('(hG : NativeGate (eball d) z N G) :',
                                                         '(hG : NativeGate (eball d) z N G)\n'
                                                         '    (hE : Entangling (eball d) G) :'))
    check('M', 'decision rule: the entangling clause in the selector reads ENTANGLING-NOT-WEAKENED and leaves the '
               'orientation cell unchanged', verdict_of(m_ent) == ([ORIENT_TOKENS[0]], [ENT_TOKENS[1]]))
    m_rel = replace_once(mod, REL_TAIL, REL_TAIL.replace(' : d = 3 := by', ' : d = 1 ∨ d = 3 := by'))
    check('M', 'decision rule: the relative selector concluding only d ∈ {1, 3} reads ENTANGLING-NOT-WEAKENED',
          verdict_of(m_rel)[1] == [ENT_TOKENS[1]])
    m_ctl = replace_once(mod, 'theorem candidateCone_cnotOrbit : CandidateCone cnotOrbit := by',
                         'theorem candidateCone_cnotOrbit : CandidateCone productSet := by')
    check('M', 'decision rule: a weakened non-vacuity control reads ORIENTATION-NOT-ESTABLISHED',
          verdict_of(m_ctl)[0] == [ORIENT_TOKENS[1]])
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens('K2-ORIENTATION-OBSTRUCTION-PROVED and K1-ENTANGLING-WEAKENED.')
          == ['K2-ORIENTATION-OBSTRUCTION-PROVED', 'K1-ENTANGLING-WEAKENED']
          and note_tokens('K1-ENTANGLING-WEAKENED, not K1-ENTANGLING-NOT-WEAKENED.')
          == ['K1-ENTANGLING-WEAKENED', 'K1-ENTANGLING-NOT-WEAKENED'])
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
