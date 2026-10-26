# Evidence part E1: Lean certificates and formal coverage

Scope: every kernel declaration the Introduction relies on. That is 65 declarations:

- the 28 of Appendix A;
- 27 more that `matrix.json` chains name with layer `kernel`;
- 10 more that FINDINGS.md's replacement texts, evidence lists or optional changes cite.

Each declaration was checked for five things: its name and line, its statement and premise structures, its axioms, its dependencies, and kernel acceptance at the exact commit. The items are in `part-E1.json`. The scripts are in `scripts/E1_*.py`.

## Counts

| | pass | partial | fail | total |
|---|---|---|---|---|
| ci-receipt | 3 | 0 | 0 | 3 |
| lean-certificate | 52 | 1 | 0 | 53 |
| formal-coverage | 56 | 9 | 0 | 65 |
| open-obligation | 0 | 1 | 0 | 1 |
| **total** | **111** | **11** | **0** | **122** |

| Evidence level | Items |
|---|---|
| reproduced | 0 |
| certificate-checked | 120 |
| traced-only | 2 (E1-55, E1-122) |
| failed | 0 |

The only possible local rebuild was ruled out: there is no Lean toolchain here (§A.40). So "certificate-checked" is the highest level any Lean item can reach.

## What the certificates are

- **E1-01, the retained result.** This is `papers/introduction_repro/results-121598983127.json` at `4a260ca9`.
  - I downloaded its source job log read-only: job 121598983127, run 40330683786, push to main at `17b830bc`. Both digests match the README:
    - the full log (43064 lines) hashes to `bc2291bc…`;
    - its first 38918 lines hash to `1a83921f…`.
  - Through the API, the job concluded success at head `17b830bc…`, and the Build and Release gate steps both succeeded.
  - `E1_crosscheck.py` compared all 286 retained reports with three job logs: this one, eae01647's and 02e73e56's. It also compared each module's `#print axioms` line numbers with the source. There were no differences. Two countercontrols were each caught on exactly the perturbed module: an axiom dropped from one report, and one print line shifted.
- **E1-02 and E1-03, main push CI.**
  - At `eae01647`: run 40395660130, job 121827872751.
  - At `02e73e56`: run 40399411290, job 121840956899.
  - At both:
    - The run concluded success, and so did the "Mathlib bridge" job and its Build and Release gate steps.
    - The gate passed all 22 steps. Its lean-axioms step reported "6082 named result(s)".
    - The toolchain was the same: Lean 4.33.0 (commit d8b18978) and Mathlib db584cd6.
    - The Build output has 0 `sorryAx`, 0 `Lean.ofReduceBool`, 0 "declaration uses 'sorry'" and 0 `error:`.
- **E1-04, identical sources.** The `verification/lean-mathlib` tree is `8624ba39` and `verification/lean` is `277d2822` at `17b830bc`, `eae01647`, `4a260ca9` and `02e73e56`. `git diff` is empty for each pair. `tools/lean_axiom_check.py`, `tools/release_gate.py` and `verify.yml` have the same blobs at all three main commits.
- **E1-05, no forbidden constructs; the allow-list.**
  - None of the 228 `.lean` files contains an `axiom`, `opaque` or `unsafe` declaration, or uses `sorry`, `admit`, `native_decide`, `implemented_by`, `extern` or `skipKernelTC`. The scan ran with comments stripped.
  - The allow-list is exactly `{propext, Classical.choice, Quot.sound}` (`tools/lean_axiom_check.py:47`).
- **Per-declaration axiom reports (E1-06 to E1-54).** These are the 49 declarations that have a `#print axioms` line.
  - Each has exactly one report, `[propext, Classical.choice, Quot.sound]`, at its print line in all three job logs.
  - The 28 Appendix A declarations also have it in the retained result.
  - The other 21 have no retained expected result. For them the structured certificate is the Release gate step's success under `lean_axiom_check`'s contract, which fails on any missing or non-allow-listed report. Their per-declaration report text is diagnostic log text (§A.44).
- **E1-56, definitions and structures.** 15 of them, which carry no `#print axioms` report. The kernel accepted them: their modules built in the successful Build step.

## Partial items

| Item | Declaration | What falls short |
|---|---|---|
| E1-55 | `cmi_nonneg` | It has no `#print axioms` line. Its axiom set is inferred from the tree scan and from `cmi3_nonneg`'s report, not printed (traced-only). It supports I-324 only negatively: FiniteEntropy's 21 theorems contain no CMI vanishing criterion, and a grep of the whole tree finds none. |
| E1-66, E1-67 | `c3_necessity`, `card_hidden_ge_two_pow_Istar` | The kernel bounds futures of finite length, and I* is a maximum over a finite nonempty family. L84 never defines I*, while Main.md:492 defines it as a supremum over t of the conditional information with the whole future. Both forms agree for a finite-horizon law (R-22). |
| E1-70 | `routed_forces_indivisible_somewhere` | Its `RoutedReadback` store clause uses the seed-posterior spelling, as PhysicalC4Discharge.lean:27–29 records. L96's gloss matches the storage-time declaration instead (R-13). **New observation:** both routed proofs take only the overlap clause (`routedReadback_overlap`, :88–92) plus finite recurrence. The write, store and read-effect clauses go unused, so the kernel derives indivisibility from a hypothesis weaker than readback. Also, no module uses `isPermMatrix_of_stochastic_inverse`. The kernel route is Theorem 3's route, and L96 says so. |
| E1-71 | `gl2_strong_gauge_moves_relative_candidate` | `CoherentLift` only requires pointwise admissibility at every time. It does not encode "compose exactly across times" (L124), and the declaration's docstring says the cocycle condition goes unused because it holds for every family. The theorem is one explicit witness: \|V\| = 2, a period-two family, one time pair. The existential reading of L124 is matched. |
| E1-85 | `PDivisible` | Locator only. The matrix cites CausalReadback:52, which is the docstring; the definition is at :54. Its content matches L90 exactly. |
| E1-92 | `isDiag_Phi` | It covers I-128. For I-129, it covers only the diagonal-preservation premise; the implication itself is Main's written theorem. The Introduction does not call I-129 machine-checked. |
| E1-98 | `rootedMap_periodic` | It states periodicity of the rooted one-time maps. I-088 speaks of the multi-time law's period. The declaration supports I-009 and I-120. |
| E1-99 | `responseRealization` | This is a rooted-family analogue. It does not cover I-071, the independent-prior realization of multi-time laws. R-08 correctly adds no "machine-checked". |
| E1-101 | `RoutedReadback` | Seed-posterior spelling (see E1-70). |
| E1-122 | open obligation | See the CI reproduction proposal below. |

## Formal coverage of FINDINGS.md's replacement texts

Every declaration that FINDINGS.md proposes to cite has the statement FINDINGS attributes to it:

- `realizesSealedOICore_of_control`, `permClass_onesFixing` and `onesFixing_not_phasesAvailable`;
- `monomialSource_not_control`, `readWriteSourced_not_control` and `substratumClass_not_drivesElementary`;
- `substratum_residual` and `substratum_plus_control_qm`;
- `routedAtStorage_forces_indivisible_somewhere`, `finiteRootedRealizable_iff_pper` and `pIndivisible_of_rooted_identity_return_of_overlap`.

The scope words in the replacement texts are the kernel's: "on the qubit" for the negative results, "every nonempty finite carrier" and "with the closure properties kept" for `substratum_plus_control_qm`, and "quarter phase".

Notes for R-06:

- **The "stated access" is a modelling choice.** The kernel takes the stated access to be the class `permClass`, the contractively scaled partial permutations. That bijective, read-write and gate-flow operators belong to it is shown by separate lemmas. Treating that class as the observer's whole access is not proved.
- **`substratumClass_not_onesFixing` shows something else.** FINDINGS lists it under "no phases from the stated access", but it does not show that phases are absent. It shows that the phase is the stipulated ingredient, which supports "with a phase intervention assumed".
- **`DrivesElementary` covers more than the flows.** It includes the transition flows at every real t, the swaps and the quarter phases. The substratum class already contains the swaps and phases, so the residual is the continuous flows, as R-06 says.

## Modelling premises (flagged, not defects)

- Every alphabet, hidden carrier, basis and operational carrier is finite.
- Reversible dynamics is an `Equiv` (a permutation) of V × H. `D_imp_Qfb` represents it by a permutation unitary.
- Q_K is fixed-basis with Born readout at every step.
- Theorem 4 is finite and endomorphic. Its outcome sets are `Fin m`; relabelling to any finite set follows from `avail_coarse`.
- Independence and OI-alone-not-QM are stated on the qubit, relative to one sealed C1–C4 core.
- Theorem 2 and the capacity bound are stated for a joint law. Their time-t identification is not formalized, as L80 says.
- No premise structure states its theorem's conclusion.

## Census status at eae01647 (FINDINGS OD-4)

| Status | Modules |
|---|---|
| kernel-only | CausalReadback, RecurrenceHorizon, PhysicalC4Discharge, PhysicalC4StorageReadback, RootedClassification, RootedClassificationAllTime, QuantumRepresentationT2, FrozenSourcing |
| verification-only | OperationalAssembly |
| current | all others cited here |

`papers/Introduction.md` is not among the census manuscripts.

## Needs owner authorization: CI reproduction proposal

**What the existing evidence is.** All three runs examined replayed the OIBridge build from an exact-key Actions cache hit, and `lake --rehash` validated byte-identical sources. No fresh elaboration was observed. Separately, 37 declarations have no retained expected result: 21 printed ones and the 16 definitions and lemmas without a print line.

**Why the existing workflow does not cover them.** The `reproduce evidence` workflow (`.github/workflows/reproduce-evidence.yml` and `verification/audits/evidence-retention/reproduce.py` at `48b18ac5`) does not reach these declarations, for three reasons:

1. It left `main` with the archive at `5c4e5087`.
2. It reproduces only manifest entries `ci-<run>`, and the manifest at `48b18ac5` has no entry `ci-40330683786`.
3. It compares only the modules an expected result lists. Of the declarations outside Appendix A, only the definitions in Equivalence, HiddenMemory, TrackBQfbBridge, PhysicalCharacterization and PhysicalC4Discharge, and the printed `isDiag_Phi` and `exactComposite_of_validity_general`, sit in those 14 modules.

**What a CI reproduction would add.** An owner-authorized run (`workflow_dispatch`, §A.40 and §A.43 item 4) would add:

1. **A fresh elaboration.** Run the README recipe at `17b830bc`, or at `eae01647`, whose sources are identical, starting from an empty `.lake/build`. No Actions cache restore; `lake exe cache get` fetches only Mathlib. Then extract with `extract_result.py` at `48b18ac5` and compare against `results-121598983127.json` with `compare_result.py --tree`. This turns the replayed reports into reports from a fresh elaboration.
2. **An extended expected result (OD-15).** Cover the modules of the declarations FINDINGS would add to Appendix A, with per-module completeness:
   - OIRealization, PhaseSource, SubstratumInterface and StructuralClosure (R-06);
   - PhysicalC4StorageReadback (R-13);
   - CanonicalMeasure, if O-5 is adopted.
   Cover also the kernel-only modules if OD-4 lands: RecurrenceHorizon and RootedClassificationAllTime.
3. **Optionally, an independent kernel replay** of the built `.olean` environment, for example `lean4checker` if a build exists for the pinned toolchain v4.33.0. This would re-typecheck every declaration outside the elaborator.

**What it needs.** A workflow on a branch that carries it, since `reproduce-evidence.yml` is not on main and its manifest has no entry for this run. It costs one uncached Mathlib bridge build and the gate; the old workflow's timeout was 120 minutes. Nothing here was dispatched.

## Commands

The scripts take paths as arguments and run read-only. Here `<lm>` is an extraction of `verification/lean-mathlib` at `eae01647`, and logs come from `gh api repos/amaybaum/incompleteness/actions/jobs/<job>/logs`.

```
python3 -I scripts/E1_decls.py <lm> --results results-121598983127.json > decls.json
python3 -I scripts/E1_logreports.py job-<job>.log decls.json > rep-<job>.json      # jobs 121598983127, 121827872751, 121840956899
python3 -I scripts/E1_crosscheck.py results-121598983127.json <lm> job-121598983127.log job-121827872751.log job-121840956899.log
python3 -I scripts/E1_build_part.py --decls decls.json --matrix matrix.json --rep17 rep-121598983127.json \
    --repeae rep-121827872751.json --rep02e rep-121840956899.json --cross crosscheck.json > part-E1.json
```

Local runtime is under one second in total. No raw logs are committed.
