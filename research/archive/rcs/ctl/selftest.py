RELC = 'actC N (G (actC N ω)) = actT N (G ω)'
RELT = 'actT N (G (actT N ω)) = G ω'
P = (PAR_TOKENS[0], SEL_TOKENS[0], POS_TOKENS[0], REL_TOKENS[0])
NP = (PAR_TOKENS[1], SEL_TOKENS[1], POS_TOKENS[1], REL_TOKENS[1])


def cells(*which):
    """The four verdicts with the named cells (0..3) not established."""
    return tuple([NP[k] if k in which else P[k]] for k in range(4))


def self_test():
    mods = {m: git('cat-file', '-p', MOD_REFERENCE_BLOBS[m]).stdout for m in MODULES}
    check('T', 'the four reference module blobs are readable', all(mods.values()))
    landed = landed_at_d()
    check('T', 'the landed texts read from D are the frozen ones', landed == LANDED)
    module_checks(mods, ' [reference]')
    check('T', 'the reference modules read %s' % ', '.join(x[0] for x in verdict_of(mods)), verdict_of(mods) == cells())
    check('T', 'the copy check passes on the reference block module', copy_bad(mods[BLK], LANDED) == [])
    # N1-N3
    must_fail('N1', 'a renamed declaration', mutate(mods, SQZ, '\ntheorem x5_unit ', '\ntheorem x5_unit\' '))
    must_fail('N2', 'a changed binder context', mutate(mods, PAR, '\nvariable {d : ℕ}\n', '\nvariable {d : ℕ} {m : ℕ}\n'))
    must_fail('N2', 'a changed open line', mutate(mods, BLK, 'CompositeDimension EffectSpace ParityNot\n',
                                                  'CompositeDimension EffectSpace\n'))
    must_fail('N2', 'a restated conclusion', mutate(mods, SQZ, '      ∧ GateRel n5 gSq\n', '      ∧ True\n'))
    must_fail('N3', 'a sorry', append_decl(mods, C5, 'theorem extra_sorry : (1 : ℕ) = 1 := sorry'))
    must_fail('N3', 'a print removed', mutate(mods, SQZ, '#print axioms OIBridge.RelcSelect.gSqInv_sep\n', ''))
    # S1 -- parity from the control relation
    head1 = '    Module.finrank ℝ (plusSpace N) = Module.finrank ℝ (minusSpace N) := by'
    must_fail('S1', 'the control relation replaced by GateRel',
              mutate(mods, PAR, '    (hC : ∀ ω, %s) :\n%s' % (RELC, head1), '    (hC : GateRel N G) :\n%s' % head1))
    must_fail('S1', 'the target relation added to the parity corollary',
              mutate(mods, PAR, '    (hC : ∀ ω, %s) : ¬ Even d :=' % RELC,
                     '    (hT : ∀ ω, %s) (hC : ∀ ω, %s) : ¬ Even d :=' % (RELT, RELC)))
    must_fail('S1', 'the count weakened to an inequality', mutate(mods, PAR, head1, head1.replace(' = Module', ' ≤ Module')))
    must_fail('S1', 'a parity proof reading a landed relT lemma',
              mutate(mods, PAR, ' : P = Q := by\n  subst hn\n',
                     ' : P = Q := by\n  have _x := @gateRel_of_nativeGate\n  subst hn\n'))
    m = mutate(mods, PAR, head1, head1.replace(' = Module', ' ≤ Module'))
    check('M', 'decision rule: a broken parity theorem reads RELC-PARITY-NOT-ESTABLISHED and '
               'CTRL-SELECTOR-NOT-ESTABLISHED, whose parity step it is, and leaves the other two cells',
          verdict_of(m) == cells(0, 1))
    check('M', 'landed: a landed relC field that differs fails all four cells',
          verdict_of(mods, landed_with('NativeGate#relC', 'actT N (G ω)', 'G ω')) == cells(0, 1, 2, 3))
    check('M', 'landed: a landed balance lemma that differs fails the parity cell alone',
          verdict_of(mods, landed_with('not_even_of_balanced', '¬ Even d', 'Odd d')) == cells(0))
    check('M', 'landed: a landed relT field that differs fails the positivity and relation cells and leaves the '
               'parity and selector cells, which do not read relT',
          verdict_of(mods, landed_with('NativeGate#relT', '= G ω', '= -G ω')) == cells(2, 3))
    # S2 -- the selector without the target relation
    relc_f = '  relC : ∀ ω, %s\n' % RELC
    must_fail('S2', 'relT restored to CtrlGate', mutate(mods, BLK, relc_f, '  relT : ∀ ω, %s\n%s' % (RELT, relc_f)))
    must_fail('S2', 'posInv dropped from CtrlGate',
              mutate(mods, BLK, '  posInv : ∀ x ∈ Ω, ∀ y ∈ Ω, G.symm (prodState x y) ∈ maxCone Ω\n', ''))
    must_fail('S2', 'the selector strengthened to d = 3', mutate(mods, BLK, '    d = 1 ∨ d = 3 := by\n  have hpos',
                                                                   '    d = 3 := by\n  have hpos'))
    must_fail('S2', 'the landed parity line restored',
              mutate(mods, BLK, '    have hbal := finrank_plus_eq_finrank_minus_relC hN hG.relC',
                     '    have hbal := finrank_plus_eq_finrank_minus hN hG'))
    must_fail('S2', 'the relT step restored in the block reduction',
              mutate(mods, BLK, '            rw [hω]; exact actT_slice_ctrl hN hG hcl hzl',
                     '            rw [hω, ← gate_actT hN hG, actT_tens, ← Minv_homMap hN hG, homMap_hom, map_zero]'))
    must_fail('S2', 'a copied proof token changed', mutate(mods, BLK, '  rw [gate_corner_ctrl hN hG, Mfwd_Minv_ctrl hN hG]\n',
                                                          '  rw [gate_corner_ctrl hN hG, Mfwd_Minv_ctrl hN hG, add_zero]\n'))
    must_fail('S2', 'a landed native-gate lemma referenced',
              mutate(mods, BLK, '    exact Phi_hom_zero_eq_zero_ctrl hN hG hc hzc u (hom 0)',
                     '    exact Phi_hom_zero_eq_zero hN hG hc hzc u (hom 0)'))
    must_fail('S2', 'the entangling clause dropped', mutate(mods, BLK, '\n    (hE : Entangling (eball d) G) : d = 3 := by',
                                                            ' : d = 3 := by'))
    check('M', 'reuse: a relT reader named through its namespace is found',
          mentions('theorem x : True := by\n  have := CompositeDimension.gate_actT\n  trivial', RELT_READERS)
          == ['gate_actT'])
    check('M', 'reuse: a landed native-gate lemma named through its namespace is found',
          nativegate_names_bad('theorem x : True := by\n  have := CompositeDimension.gate_corner\n  trivial', LANDED)
          == ['x'])
    m = mutate(mods, BLK, '    d = 1 ∨ d = 3 := by\n  have hpos', '    d = 3 := by\n  have hpos')
    check('M', 'decision rule: a broken selector reads CTRL-SELECTOR-NOT-ESTABLISHED and leaves the other cells',
          verdict_of(m) == cells(1))
    check('M', 'landed: a landed selector that differs fails the selector cell alone',
          verdict_of(mods, landed_with('dim_of_nativeGate', '(hN : IsNot (eball d) z N)',
                                       '(hN : IsNot (eball d) z N) (h2 : 2 ≤ d)')) == cells(1))
    check('M', 'landed: a landed d = 3 native gate that differs fails the selector cell alone',
          verdict_of(mods, landed_with('nativeGate_cnot', 'eball 3', 'eball 5')) == cells(1))
    check('M', 'landed: a landed copied declaration that differs fails the selector cell alone',
          verdict_of(mods, landed_with('copy#gt_corner', 'Mfwd_Minv hN hG]', 'Mfwd_Minv hN hG, add_zero]')) == cells(1))
    check('M', 'landed: a landed posInv field that differs fails every cell but parity',
          verdict_of(mods, landed_with('NativeGate#posInv', 'maxCone Ω', 'jointStates Ω')) == cells(1, 2, 3))
    # S3 -- the positivity clauses one at a time
    sep_tail = ('      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)) :=\n'
                '  ⟨isNot_n5, gSq_frame, gateRel_gSq, gSq_posFwd, gSq_not_posInv⟩')
    must_fail('S3', 'the failure of inverse positivity dropped from gSq_sep',
              mutate(mods, SQZ, '\n' + sep_tail, ' :=\n  ⟨isNot_n5, gSq_frame, gateRel_gSq, gSq_posFwd⟩'))
    inv4 = ('      ∧ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq (prodState x y) ∈ maxCone (eball 5))\n'
            '      ∧ ¬ (∀ x ∈ eball 5, ∀ y ∈ eball 5, gSq.symm (prodState x y) ∈ maxCone (eball 5)) :=\n'
            '  ⟨isNot_n5, frame_symm')
    must_fail('S3', 'the inverse positivity of gSq.symm restated as its forward positivity',
              mutate(mods, SQZ, inv4, inv4.replace('gSq (prodState', 'gSq.symm (prodState', 1)))
    must_fail('S3', 'the transfer of relC to the inverse without relT',
              mutate(mods, SQZ, '(hN : IsNot Ω z N) (hT : ∀ ω, %s)\n    (hC :' % RELT, '(hN : IsNot Ω z N)\n    (hC :'))
    must_fail('S3', 'the value changed to a sign', mutate(mods, SQZ, '(gSq.symm (prodState z5 x5)) = -1 / 2 := by',
                                                          '(gSq.symm (prodState z5 x5)) < 0 := by'))
    must_fail('S3', 'the squeeze removed', mutate(mods, SQZ, 'if sqCls n then 1 else 1 / 2', 'if sqCls n then 1 else 1'))
    must_fail('S3', 'GateRel weakened to the control relation in gSq_sep',
              mutate(mods, SQZ, '      ∧ GateRel n5 gSq\n', '      ∧ (∀ ω, actC n5 (gSq (actC n5 ω)) = actT n5 (gSq ω))\n'))
    m = mutate(mods, SQZ, '(gSq.symm (prodState z5 x5)) = -1 / 2 := by', '(gSq.symm (prodState z5 x5)) < 0 := by')
    check('M', 'decision rule: a broken positivity witness reads POSITIVITY-SEPARATION-NOT-ESTABLISHED and leaves the '
               'other cells', verdict_of(m) == cells(2))
    check('M', 'landed: a landed n5 that differs fails the positivity cell alone',
          verdict_of(mods, landed_with('odd5', '2 => false', '2 => true')) == cells(2))
    check('M', 'landed: a landed GateRel that differs from the landed relations fails the positivity cell alone',
          verdict_of(mods, landed_with('GateRel#relC', 'actT N (G ω)', 'G ω')) == cells(2))
    # S4 -- the control relation is not replaced by the target relation
    must_fail('S4', 'the failure of relC dropped from c5_sep',
              mutate(mods, C5, ' ∧\n      ¬ (∀ ω, actC nC5 (gC5 (actC nC5 ω)) = actT nC5 (gC5 ω)) :=\n'
                               '  ⟨isNot_nC5, gC5_frame, gC5_relT, gC5_posFwd, gC5_posInv, gC5_not_relC⟩',
                     ' :=\n  ⟨isNot_nC5, gC5_frame, gC5_relT, gC5_posFwd, gC5_posInv⟩'))
    must_fail('S4', 'relC in place of relT in the non-selection statement',
              mutate(mods, C5, '      (∀ ω, %s) →\n      d = 1 ∨ d = 3 := by' % RELT,
                     '      (∀ ω, %s) →\n      d = 1 ∨ d = 3 := by' % RELC))
    must_fail('S4', 'inverse positivity dropped from the non-selection statement',
              mutate(mods, C5, '      (∀ x ∈ eball d, ∀ y ∈ eball d, G.symm (prodState x y) ∈ maxCone (eball d)) →\n', ''))
    must_fail('S4', 'a sign of the gate changed', mutate(mods, C5, '(ν = 2 ∨ ν = 3)) then -1 else 1',
                                                         '(ν = 2 ∨ ν = 3)) then 1 else -1'))
    must_fail('S4', 'the witness NOT replaced by the landed n5',
              mutate(mods, C5, 'def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := diagSign cC5',
                     'def nC5 : (Fin 5 → ℝ) →ₗ[ℝ] (Fin 5 → ℝ) := n5'))
    must_fail('S4', 'the non-selection conclusion changed', mutate(mods, C5, '      d = 1 ∨ d = 3 := by\n  intro h',
                                                                   '      d = 3 := by\n  intro h'))
    m = mutate(mods, C5, '(ν = 2 ∨ ν = 3)) then -1 else 1', '(ν = 2 ∨ ν = 3)) then 1 else -1')
    check('M', 'decision rule: a broken relation witness reads RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED and leaves '
               'the other cells', verdict_of(m) == cells(3))
    check('M', 'landed: a landed z5 that differs fails the positivity and relation cells',
          verdict_of(mods, landed_with('z5', 'i = 4', 'i = 3')) == cells(2, 3))
    # S6 -- scope
    must_fail('S6', 'a complex field', append_decl(mods, SQZ, 'theorem cplx : (Complex.I : ℂ) = Complex.I := rfl'))
    must_fail('S6', 'a positive native gate', append_decl(mods, C5, 'theorem pos_gate : NativeGate (eball 5) z5 nC5 gC5 '
                                                                     ':= sorry'))
    must_fail('S6', 'a conclusion on d outside the selector',
              append_decl(mods, BLK, 'theorem d_sel {z : Fin d → ℝ} {N : (Fin d → ℝ) →ₗ[ℝ] (Fin d → ℝ)} '
                                     '{G : W d ≃ₗ[ℝ] W d} (hN : IsNot (eball d) z N) '
                                     '(hG : CtrlGate (eball d) z N G) : d ≠ 5 := sorry'))
    must_fail('S6', 'the landed selector read', mutate(mods, BLK, '  rcases dim_of_ctrlGate hN hG with hone | hthree',
                                                       '  rcases dim_of_nativeGate hN hG with hone | hthree'))
    # S7 -- reuse
    must_fail('S7', 'a landed definition re-declared', append_decl(mods, C5, 'def odd5 : ℕ := 0'))
    must_fail('S7', 'a declaration of another module of the round re-declared',
              append_decl(mods, C5, 'theorem lor_five : True := trivial'))
    must_fail('S7', 'a second import', mutate(mods, PAR, 'import OIBridge.OddChar\n',
                                              'import OIBridge.OddChar\nimport OIBridge.K2Guard\n'))
    # S8 -- phrases
    must_fail('S8', 'a global redundancy claim in a header',
              mutate(mods, BLK, '  remains a field of both.\n', '  remains a field of both; relT is redundant.\n'))
    must_fail('S8', 'an implication between the positivity clauses in a docstring',
              mutate(mods, SQZ, '/-- **Forward positivity does not imply inverse positivity**',
                     '/-- **Forward positivity implies inverse positivity**'))
    must_fail('S8', 'the design header', mutate(mods, C5, 'OIBridge/RelcSelectC5.lean — round RELC-SELECT-1:',
                                                'OIBridge/RelcSelectC5.lean — design module for round RELC-SELECT-1:'))
    frozen = EARNED + NONINF
    check('M', 'phrases: the frozen earned reading and non-inference rule pass when stated; each passes nowhere else',
          not phrase_hits('\n\n'.join(frozen), frozen) and all(phrase_hits(f) for f in frozen))
    check('M', 'phrases: unqualified or global claims fail',
          phrase_hits('relT is unnecessary.') == ['relT is unnecessary']
          and phrase_hits('Hence `relC` is inverse-stable.') == ['inverse-stable']
          and 'redundan' in phrase_hits('relT is globally redundant')
          and phrase_hits('a physical gate') == ['physical gate']
          and phrase_hits('a globally minimal set') == ['globally minimal']
          and phrase_hits('> ' + EARNED[0] + ' Hence relT is unnecessary.', frozen) == ['relT is unnecessary'])
    # S9
    must_fail('S9', 'an extra print', mutate(mods, SQZ, '#print axioms OIBridge.RelcSelect.gSqInv_sep\n',
                                             '#print axioms OIBridge.RelcSelect.gSqInv_sep\n'
                                             '#print axioms OIBridge.RelcSelect.x5_unit\n'))
    must_fail('S9', 'a duplicated print', mutate(mods, C5, '#print axioms OIBridge.RelcSelect.c5_sep\n',
                                                 '#print axioms OIBridge.RelcSelect.c5_sep\n'
                                                 '#print axioms OIBridge.RelcSelect.c5_sep\n'))
    # V
    allp = ', '.join(P)
    check('M', 'note tokens: exactly the stated tokens are found',
          note_tokens(allp + '.') == list(P)
          and note_tokens('RELT-NOT-DIMENSION-SELECTING-NOT-ESTABLISHED') == [REL_TOKENS[1]])
    quoted = '\n'.join('> ' + l for l in '\n\n'.join(EARNED).split('\n'))
    check('M', 'earned reading: found when quoted across lines, not found when one sentence is changed',
          all(earned_stated(quoted)) and
          not all(earned_stated(quoted.replace('the dimension is 1 or 3', 'the dimension is 3'))))
    # I, C
    d_imp = show(D, IMPORTS)
    good_imp = d_imp.replace(ANCHOR_IMPORT, ANCHOR_IMPORT + NEW_IMPORTS, 1)
    check('M', 'imports: the frozen edit passes; a dropped line and a reordered pair fail',
          imports_ok(d_imp, good_imp) and not imports_ok(d_imp, d_imp)
          and not imports_ok(d_imp, good_imp.replace('import OIBridge.RelcSelectParity\nimport OIBridge.RelcSelectBlock\n',
                                                     'import OIBridge.RelcSelectBlock\nimport OIBridge.RelcSelectParity\n')))
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
