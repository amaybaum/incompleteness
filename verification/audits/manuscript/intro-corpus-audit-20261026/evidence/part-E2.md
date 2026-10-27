# Evidence verification, part E2: exhaustive computations and numerical results

Items are in `part-E2.json` (E2-01 to E2-20). Scripts are in `scripts/E2_*.py`. Each takes an
optional output path and uses no absolute paths. The corpus is read at `eae01647`. The probe files
and black-hole records are byte-identical at `b64919cd`, `eae01647` and `main` `02e73e56`.

## Counts

| Evidence level | Items |
|---|---|
| reproduced | 17 |
| failed | 2 |
| traced-only | 1 |

| Outcome | Items |
|---|---|
| pass | 15 |
| partial | 3 |
| fail | 2 |

Local compute was about 2 minutes in total. The largest item was the 53 s byte-for-byte replay of
BHa `checks.py`.

## Reproduced exactly (independent scripts)

- **§5 counts.** 1,376 of 40,320, the full delta histogram, 2,688, 60, the 24/60/172 split, 32 of
  256 (exactly the maps whose read register is constant), 14,496, 36,416 (36,368 and 36,032), and
  min P_succ = 1/2 attained by 2,368. Integer arithmetic, exhaustive (`E2_bh01_counts.py`). BHa
  `result.json` was also replayed byte-identical.
- **BHa item F.** Rational intervals (`E2_itemF.py`).
- **BHb C1.** The BHb `checks.py` replay (E3-18) reproduces `result.json` byte for byte, including the C1 sweeps at
  (2,2), (2,3) and (3,2) by exact Schmidt rank and the countercontrols CC1 = CC2 = 2. An independent exact-rank sweep
  at (2,2) and (2,3) (`E2_bh02.py`) agrees, and its countercontrols fire: an entangled start reaches rank 2 under the
  same evolution, non-permutation gates give rank 2, the orbits of length 1 number N! (so the permutation is
  applied), and mutant evolutions are caught.
- **BHb C6(c) shells.** Exact rationals and interval arithmetic (`E2_bh02.py`).
- **Appendix B.** Every number, the three-hidden-state model and the Theorem 3 census over every
  prior support (`E2_appendixB.py`).
- **c4_backflow instances.** Exact and rigorous-interval evaluation (`E2_c4_exact.py`).
- **Main:594 and B4.** `E2_memory_exact.py`, see below.
- **Small witnesses.** L94, L106 and L66 (`E2_small_exact.py`).
- **§4 numbers.** `E2_s4_numbers.py`.

## Failed

Both failures are of an evidence tag, not of the result it describes.

- **E2-10.** L84's "with exact probes" (and Main:170's "Certified exactly") is not met.
  `c4_backflow_probes.py` evaluates the conditional mutual information in floating point (:23) and
  decides with tolerances (:52, :63, :97), on five named instances, none exhaustive. The instance
  values do hold: E2-09 certifies them exactly. This confirms R-03 and CON-25.
- **E2-11.** L56's "with exact probes" fails L30's definition as the Introduction states it.
  `process_dilation_probes.py` and `review4_probes.py` P-G are exact, but they cover named instances and are not
  exhaustive. They meet R-03's narrowed definition. P-G builds no bijection and uses rational kernels only, so
  R-08's "for every law" rests on the paper Extension at Main:498.

## Partial

- **E2-15, opglue (R-07).** The final comparisons are in floating point, with large margins.
  Checks 8–9 compute in floating point throughout. This was a replay only.
- **E2-18, GR:366 convention range.** The range [1/(96π²), 8/3] holds only for a cutoff between
  M_Pl/2 and M_Pl together with the critical density. With ρ = H²/G it reaches 1/(256π³), and with
  Weinberg's cutoff 1/(384π⁴). This is a corpus wording item (GR:366, ch07:193, FULL:2072). The
  Introduction's L148 is unaffected.
- **E2-20, CI.** No CI job runs any cited probe or the black-hole checks. GitHub run history was
  not queried.

## New findings

- **CON-26 resolved, exactly.** "1 of 15" (memory_probes, grouped by the t=2 conditional
  signature) and "2 of 16" (B4, grouped by full law) are the same fact. The one merged signature
  group holds both attaining laws. Arbitrary priors attain nothing beyond the uniform prior: 2 of
  16 either way. So Main:594's counterexample holds over all priors. B4's `fixeddim.py` is
  unseeded and non-reproducible; `E2_memory_exact.py` supersedes it.
- **Defects in the audit's `b5_check.py`.** B.2's I(X0;X2|X1) was hard-coded as `1 - 0`, and the
  three-hidden variant's a/(2−a), which R-04 claims, was not computed. `E2_appendixB.py` computes
  both, and both hold. `b5_check.py` now computes both, with countercontrols.

## Needs owner authorization (CI)

- **BHb (bh02) `-O` replay and `mutants.py`.** The normal `checks.py` replay is done (E3-18, about
  30 s). `mutants.py` takes about 30 minutes.
- **BHa `mutants.py`.** 360–570 s on four cores (PROVENANCE.json); its retained output records
  12/12 mutants caught.
- **Foundations probes in CI (optional).** Add the eight cited probes (c4_backflow,
  process_dilation, review4, translation, c1_cp_scope, equivalence_recovery, memory, opglue,
  about 20 s together) to the `Numerical probes / foundations` job. This is a workflow change,
  so it is an owner decision.
