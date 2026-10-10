# messages1 — deletion notes per tag

General conventions applied to every tag:
- Deleted every closing tally ("N named contracts, M mutation controls, seal controls, drift control"), because the retained predicates no longer match those counts. Recomputing them would add new claims.
- Deleted any per-clause mutation count that no longer matches the retained mutations. Kept a count only where it still matches exactly.
- Deleted "still" before OPEN/UNDECIDED so no revision-history wording is left.
- Deleted SEALING / "under A.37" / MANIFEST PROTOCOL / landing descriptors from the leading phrase, and kept the rest of the guard descriptor.

## R7-TRJ
Retained predicates: anticonflation (result.md + module + ROADMAP), lean_defs, roadmap; mutations m26-29, m37-40, m53-56.
Deleted:
- "SEALING ... under A.37" from the descriptor.
- The whole AXIS 1 (TJ1) block, including "RULES LINE 3 OUT ...", its four mutation controls, and the |A| rank-bound POINTWISE sentence. These are checked by _trj_tj1 against the result note, which is not retained.
- The whole AXIS 2 (TJ3) block: line 4, EXISTS C FORALL S, the reversed order refused, exhibited countermodel, six mutation controls.
- "THE TWO AXES ARE CHECKED NOT MERGED ... two mutation controls". This is _trj_two_axis on the note. The ROADMAP's not-merged sentence is still covered by the descriptor "kept APART" and by "both axes recorded".
- Line 1 / line 2 / unrefuted-candidate sentence.
- TJ0 sentence (type P, bounded search, five mutation controls).
- TJ2 six parts sentence.
- Scope-boundary sentence (the GL2 pair as one trajectory, uniform-phase not adopted).
- Twenty forbidden sentences.
- "The frozen FOUR-slot budget ... slots 1 and 2 FIRED ... conditional slots UNUSED", and the "five mutation controls". The module clause is kept with 4 retained mutations, so the count was dropped.
- Axiom table (twenty-three lines).
- Discrepancies / observations / configurations.
- Predictions.
- Chronology, freeze-pin drift, archive pins, seal-integrity clause, acts 13-16 seals unmoved.
- Final tally.
Kept: the anti-conflation clause with "four mutation controls" (m26-29 = 4). The ROADMAP P0 clause with "four mutation controls" (m53-56 = 4). The module two-defs / no sorry-axiom-native_decide clause.
Uncertain:
- _trj_lean_defs also checks docstring phrases: no candidate endorsed, reversed quantifier order not the statement, merged existential not enlarged, GL2 pair one trajectory. The old message states these as result-note checks ("checked refused as a TJ2 finding", scope boundary), so I deleted them rather than re-scope them to the docstring.
- _trj_roadmap also checks "Line 3 is ruled out by TJ1" and the ∃C∀S quantifiers in the ROADMAP. These are covered only by the kept phrase "both axes recorded".

## R7-TCF
Retained predicates: seam, act14_untouched, cf1, anticonflation, status_rule, axiom_table, lean_defs (several read result.md, so the note clauses they test are kept); mutations m3-7, m11, m19-22, m25-28.
Deleted:
- "SEALING ... under A.37" and "AGAINST the freeze's own central prediction". The outcome/reversal is _tcf_outcome, not retained.
- The freeze-rating / line-1 exhibition sentence and the "reversal is checked reported" sentence (_tcf_outcome / _tcf_cf5).
- The seam's "four mutation controls": only 3 are retained (m3-5).
- The CF0 sentence.
- The three necessary-conditions sentence (_tcf_cf2_cf3_cf4).
- "act 14's PQ3 (b) on O_1 above all".
- "as a block quote" in the anti-conflation clause. _TCF1/_TCFROADQ strip the '>' markers, so block-quote form is not tested.
- Budget ("frozen TWO-slot budget ... slot 1 fired ... conditional slot UNUSED") and its "four mutation controls". The module clause has 2 retained mutations (m25-26).
- Chronology, archive pins, "no later main absorbed", acts 13/14 seals, tally.
Kept counts: anti-conflation two (m19-20), P0 two (m21-22), axiom table two (m27-28), "both mutation-tested" for act 14 (m6-7).
Uncertain:
- "THE ANSWER IS CHECKED SCOPED TO O_2 and untransferred to any other carrier" is kept. It rests on _tcf_lean_defs requiring "**travels to no other carrier**" in the module docstring, which sits in the sentence "`cf5_cancelling_triple_exists` is a statement about `𝒪₂` and travels to no other carrier". The result-note version (_tcf_cf5) is removed. The claim is tested, but only in the docstring.

## R7-A6D
Retained predicates: d2_kernel, d3_kernel, d4_kernel, lean_defs (module), roadmap_row (ROADMAP + result.md), axiom_table (module + result.md); mutations m14, m18, m21, m25, m28-31.
Deleted:
- "so what can go wrong is the READING of four readings ... in the freeze's own terms".
- The readings-never-identified sentence.
- The adoption-decision-named-OPEN clause and its mutations.
- D1 entirely.
- D2-iii entirely.
- "in the note and" from the D2-i witness clause, plus "the substitution of a witness" (m13 not retained).
- D3 one-directional sentence.
- D3-a bounded / not "local gauge invariance is trivial".
- The D4 connected-corollary-as-ANALYSIS clause and its mutations.
- Non-licences.
- Unsettled points.
- "No manuscript edit".
- Seven of nine slots / conditional slots / no tenth.
- Chronology and ARCHIVE MODE.
- Tally.
- "still" before "recording".
Joining edits: "the identity theorem checked universal" became "D3-a's identity theorem is checked universal". Lower-case "the module" became "The module".
Uncertain:
- "a DEFINITION round, not a proof round" is kept as the leading descriptor, although _a6d_outcome, which checked that sentence in the note, is removed.
- "No reading is checked adopted" is kept on the strength of _a6d_lean_defs requiring the module docstring's "it adopts no reading".
- "A6-cov not a predicate of a Substratum" is also checked in the docstring by lean_defs. I still deleted the readings sentence, because its umbrella claim ("never silently identified", A6-sd not the covariant coupling) is not tested.
- "D4 is checked single-edge" is kept because _a6d_d4_kernel pins the single-edge theorem d4a_single_edge (hypothesis `hj : j ∈ N i`). The note-side bounded reading (_a6d_d4_single_edge) is removed. Delete this phrase if you want only the symmetric-point clause.

## R7-RCL
Deleted only "and its amendment as append-only and superseding". Those checks read C4-CAUSAL-READBACK-AUDIT-AMENDMENT-1.md and are not retained. Everything else is tested by the retained predicates (prints-complete, reachability plus 3 mutations, 2 axiom-reporting mutations, counts, hygiene, capstone/finite-visible/control-13 kernel strings, manuscripts, registry/census, README).

## R7-SOI
Deleted the whole round-note clause: "the note keeps the question, ..., the scope amendment before the outcome, names all three commits, records outcome A ... no divisibility verdict and no correspondence claim". It reads STOCHASTIC-OBSERVER-INTERFACE-AUDIT.md, the round's own record, and is not retained. Everything else is kept verbatim. The frozen-sourcing note clause and the older-notes clause are kept because they read live audit files that are not the round's own records.

## R7-CTI
Retained predicates: ct2b_kernel (which also pins the CT1 and CT2 (a) iffs), ct4_kernel, lean_defs; mutations m13, m14, m20, m21, m27.
Deleted:
- The boxed outcome.
- The structural-point sentences.
- CT1's forward/backward provenance and "constant NOT restricted to a gauge class".
- CT2 (a)'s conjugation/sufficiency/CT4-certificate tail.
- "the phase-quotiented corollary recorded not attempted".
- The ladder sentence.
- CT3 (G), (a), (b), (c), (d).
- CL1.
- Case A sentence and non-licences.
- Shape remark.
- GL2/GL3/... consumed.
- "Four of six definition slots fire ... no seventh".
- Chronology / archive scaffolding.
- "No manuscript edit, no discrepancy".
- Tally.
Joining edit: "those four top-level definitions" became "EXACTLY four top-level definitions".
Uncertain: "CT3 (G) is checked universal" was deleted. _cti_ct4_kernel only checks that the name `theorem ct3g_fibreCrossGram_strong_right` exists, not that it is universal. The same applies to the CL1 theorem name. The descriptor's "bounded from below by a universal theorem" is kept as descriptor text.

## R7-C4R
Deleted:
- "the note keeps its frozen sections in order before the outcome, names both commits, and the amendment is binding, additions-only and carries all five of its clauses".
- The whole "the outcome records M-A and S-B separately, ... interface gap remains binding" clause.
- "no architecture-refuted, no OI-sources-it, no A6-filled, no fifth-condition, no necessity and no correspondence claim".
All of these are checks on the round's own note and amendment, which are not retained.
Uncertain: the README-forbidden-phrase checks (retained, `_bad not in _rd1`) cover some of the deleted "no architecture-refuted ..." list, but only for the README. The old message placed that list under the note, so I deleted it rather than re-scope it.

## R7-HYE
Retained predicates: lean_defs (module docstring), lean_statements, programme_line, roadmap; mutations m21-24, m29, m30.
Deleted:
- "SEALING" and "so what can go wrong is the READING rather than the landing".
- The chronology sentence.
- "in the freeze's own words".
- "and the crossing is routed through HE2-f alone".
- "and not surjectivity".
- "carried twice, once as H3-ident ... once as H3-prop ..., either carriage dropped mutation-tested".
- "in the note and" (site-independent).
- The HE4-a/HE4-b bounds clause.
- HE5-unstatable.
- The frozen gates sentence (HE6, lane D, H-B guardrail).
- HE0/HE1/HE5 type P.
- "with the conditional slot recorded fired".
- H-A/H-B seal constants, the pins, start-state discrepancies, "no sibling result consumed".
- Tally.
Uncertain:
- The "two characteristic errors" sentence is kept in trimmed form. It rests on the module docstring (lean_defs: the propagation clause not stated or proved; the variable is the parameter triple, not the coarse charges) and the ROADMAP (roadmap: "The clause that would supply closure is the propagation clause, and it is neither stated nor proved here"; the flux is a function of the parameters). It is no longer checked against the note in the freeze's words.
- The injectivity / image-uncharacterized / im Ψ clause is kept. It rests on the kernel hexMeanCharge_injective, the docstring's im Ψ and image-not-characterized strings, and the ROADMAP image-HO string (m22, m30).

## R7-OLG
Retained predicates: _olg_lean (zero defs, both imports, twelve results with axiom lines, witnesses pinned), _olg_wired, _olg_p0 (reads ROADMAP, preregistration.md, result.md); mutations m11-m14, m13b.
Deleted:
- "a SEALING round under A.37 through the MANIFEST PROTOCOL".
- "executed in the order G1, G2, G3, G4 with one verdict commit per target".
- "act 21's ladder and act 22's verdicts consumed UNCHANGED".
- Control-plane blob / drift.
- The chronology verdict.
- The whole ordering obligation: stage-A commit, module commit, verdict commits, "at any commit from the module commit to the certified object", "at every such commit".
- "a fabricated SHA, an out-of-order chain", "a verdict theorem in the module commit".
- The entire "note held to the freeze's distinctions" list, except the P0 sentence.
- Twenty-one mutation controls / locating controls / seal state read mode-aware.
Uncertain: "with a synthetic definition, a reassigned witness and a substituted witness each checked to FAIL on synthetic data" is kept. In the old message these were the ordering negatives, but the retained head-level mutations test the same three failures on synthetic text: m12 (a def added), m13 (witness equation substituted) and m13b (another target's witness named in a section). The P0 clause is kept because _olg_p0 is retained, and it reads the preregistration for the frozen sentence.

## R7-HYB
Deleted:
- "not the landing".
- The chronology sentence.
- The "Each target's frozen reading is checked in terms: ..." sentence (_hyb_h*_status / reading / not_licensed on the note).
- Tally.
Uncertain: the status-rule four-parts sentence is kept. _hyb_status_rule (note) is removed, but each part is still tested elsewhere:
- the module docstring via lean_defs: not reported closed, no label "for OI", the A1–A4, ¬A5 class; mutation m23;
- PROGRAMME.md via programme_line: "OI-compatibility of the class open", no "H-B is closed"; mutation m25.
