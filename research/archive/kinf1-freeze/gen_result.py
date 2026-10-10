"""gen_result.py <F> <F_run> <S1_sha> <S1_run> <S2_sha> <S2_run> <S3_sha> <S3_run> <module_blob_at_E> <lean_axioms_count>
Writes result.md for the FOUNDATIONS-PROVED outcome; every run must have concluded success with no job cancelled."""
import sys, json
sys.path.insert(0, '.')
import texts
fr = json.load(open('frozen.json'))
F, F_RUN, S1, S1_RUN, S2, S2_RUN, S3, S3_RUN, MOD, NAX = sys.argv[1:11]
REF = fr['REFERENCE_BLOB']
PROBE = fr['PROBE_BLOB']
dep = ('the reference implementation `%s`: no departure.' % REF) if MOD == REF else \
      ('the reference implementation is `%s`; the departure from the reference implementation is a proof-only repair, stated below.' % REF)
L = []
L += ['# Reconstruction round KINF-1 — the field-neutral foundations of the pre-quantum completion: RESULT', '',
      '**Outcome:** `KINF-1-FOUNDATIONS-PROVED`', '',
      '> ' + texts.SENTENCES['KINF-1-FOUNDATIONS-PROVED'], '',
      texts.CLAUSE_MENTION, '',
      '> ' + texts.CLAUSE, '',
      '## The layers at `E`', '',
      '| layer | what it certifies | where |',
      '| --- | --- | --- |',
      '| kernel, evidence level 2 | the frozen definitions; `states_isCompact`, `states_unit`; Lemma C `strictConvex_of_supporting_singleton`; Lemma D `card_le_two_of_centrallySymmetric` and its full-effects corollary; Lemma B `eq_closedBall_of_frontier_subset_sphere`; `exposed_mem_range`, `exposed_ncard_le`; Theorem F2 `classical_exposed_ncard_le` with `response_eq_one_forces` and `exists_zero_of_classicallyExposed`; `copyNatural_iff_apply`; `qubit_certain_face` (imported kinematics); `KInf1` as a definition with `strictConvex_of_kInf1`; the verdict `kinf1_kernel_core` | `verification/lean-mathlib/OIBridge/KInfFoundations.lean` |',
      '| exact computation, replayed in CI | the SIC-embedded ball on four ontic states; the Carathéodory capacity-three triple; the torus and Stiefel flat faces with central symmetry; the 3-ball control | `verification/lean/kinf_foundations_probe.py` |',
      '| written remark | that strict convexity relative to the affine span gives the facet condition of Theorem F2 | the preregistration, *The mathematics* |', '',
      '## The kernel layer', '',
      'The module at `E` is blob `%s`, %s It carries the frozen header, the frozen' % (MOD, dep),
      'declarations (three structures, fifteen definitions, twenty-four theorems), each theorem followed by its `#print axioms`',
      'line. In the run at `E`\'s predecessor, every theorem reports axioms within `[propext, Classical.choice, Quot.sound]`,',
      'and `lean-axioms` reports %s named results and no sorry.' % NAX, '',
      '## The exact-computation layer', '',
      'The probe has its frozen blob `%s`. Its summary line in run %s, on `%s`:' % (PROBE, S3_RUN, S3), '',
      '`' + texts.PROBE_OK_PREFIX + '`', '',
      '## The execution', '',
      '| commit | content | run on that commit | conclusion |',
      '| --- | --- | --- | --- |',
      '| `F` = `%s` | the preregistration | %s | `success`, every job |' % (F[:8], F_RUN),
      '| `%s` | stage 1: `controls.py`, the probe, the workflow shard | %s | `success`, every job |' % (S1[:8], S1_RUN),
      '| `%s` | stage 2: the module without its verdict, the import, the census family | %s | `success`, every job |' % (S2[:8], S2_RUN),
      '| `%s` | stage 3: the verdict; the module is `%s` | %s | `success`, every job; `lean-axioms` %s |' % (S3[:8], MOD[:8], S3_RUN, NAX), '',
      'No run was cancelled. The paths changed from `D` are exactly the governed ones; no manuscript, built artifact or',
      '`verification/ROADMAP.md` changed.', '',
      '## What stays open', '',
      '- Field-neutral drivability (K∞-R), sharp supporting effects beyond the matrix level (K∞-1), singleton faces (SF) and',
      '  copy naturality: named here as definitions, discharged by nothing.',
      '- Whether the completion\'s available effects are the full effects.',
      '- The passage from strict convexity relative to the affine span to the facet condition of Theorem F2, in the kernel.', '']
open('result.md', 'w', encoding='utf-8').write('\n'.join(L))
print('written', len(L), 'lines')
