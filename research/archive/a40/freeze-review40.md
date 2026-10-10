# A40 freeze draft — review notes (local only; no branch, no candidate F)

Prospective F contents: `rec/preregistration.md` (1145 lines) alone. Stage-1 file held beside it: `rec/controls.py`, blob
`a67a49d1a510db2a2a70d2fafb9b10f875d79d78`. D = `b271b1df`.

## Frozen objects

| object | blob | status |
| --- | --- | --- |
| module `DitaTorusLocus.lean` | `829146f6eff2b99aab54d7e5e9292b0ecfb33d8d` | = the green design module `0d42d28e` with only the docstring and the verdict's name changed; **not yet CI-run at this blob** |
| probe `dita_torus_locus_probe.py` | `4b718e79f3800369855b6a9f0fc734ed2d59df4b` | = CI-measured blob `3905ae21` with only the section-7 title changed; the repo's `probe_replay_check` against `3905ae21`: 23 lines compared, 0 differences; **not yet CI-run at this blob** |
| workflow | D's + one edit in five places | own shard `probes_a40`, `Numerical probes / A40 locus`, required by the aggregate; **not yet CI-run** |
| ROADMAP cells | `145251197b…` (classified), `c06b8078b9…` (fails) | guard at D against each: `ALL CHECKS PASS`, output byte-identical to D's |

## Local verification (no push)

- `controls.py --self-test`: 14 duality mutations rejected, 3 rows hold, 74 mutation controls fail with their named codes;
  the agreement check passes against the preregistration (head, every body, sentences, clause, P0 texts, blobs, names).
- Predicted execution built as local commits from D (F → stages 1–2 → stage 3 → synthetic result note):
  `controls.py check E` OK (label `A40-LOCUS-CLASSIFIED`, exactly the nine governed paths), `legacy_records_check` 303 intact,
  `artifact_placement_check` OK, `lean_manuscript_census` OK (19 families), `git diff --check` clean.

## Decisions for the owner

1. **Module frozen by blob, no proof repair.** Stronger than A39, which froze the statements only. A module that fails at E is a
   freeze failure and the round halts. This is reversible: freeze the statements only and allow repairs.
2. **Names.** The verdict theorem is `a40_locus_kernel` (dual `a40_not_locus_kernel`); the design name `a40_classified`
   claimed more than the kernel proves. The labels are `A40-LOCUS-CLASSIFIED`, `A40-LOCUS-FAILS` and `A40-UNDECIDED`.
   "Classified" appears only in the round label, which requires the kernel `P_R` **and** a green probe at E.
3. **Two layers, stated as such.** The kernel proves the if-direction on the whole of each face, plus 20 strict
   named-map exclusions. The only-if direction, over all maps and up to diagonal equivalence, is the probe's. The preregistration's
   question table gives each direction its own witness (§A.34), and the module's own docstring says the converse is not the
   kernel's.
4. **Correction to my earlier report.** The probe's control at (1, 1, 1) is act 37's census of the eighteen structures of the
   stratum point, not the {0, 1} exponent census. The latter is not used, computed or controlled for anywhere
   (Hazard 3). Likewise, the probe's section 7 is an exact search, not a numeric one.
5. **Kernel countercontrol** (exactly nine red) is recorded as pre-freeze design evidence; it is not rerun by the execution.
6. **No kernel control theorems** (A39 had BASE and DIAG). All controls are the probe's; the kernel exclusions include the
   eighteen census maps.

## Outstanding before F: one run, which needs your permission to push

The draft keeps one unfilled row, `@@PREDICTED_RUN@@`. Neither the frozen module blob, the frozen probe blob nor the frozen
workflow edit has been compiled or run in CI yet. The proposed run: push the locally built predicted execution tree less the
result note (commit T3, rebuilt by `rehearse40.py`) to a disposable branch `claude/a40-predicted` from D, never landed, and
dispatch it once. It must show all nine jobs green: the bridge with 5251 named results and no sorry, the A40 locus shard with
22 PASS and its OK line, and the aggregate requiring it. Its run id then fills the row, and the preregistration's text is
final.
