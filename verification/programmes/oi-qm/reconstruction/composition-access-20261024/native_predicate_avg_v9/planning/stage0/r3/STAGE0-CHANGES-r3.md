# Stage 0: changes from r2 to r3

r2 (`STAGE0-PLAN-r2.md`, SHA-256 `2aa16206…d38a`), `stage0-code/` and
`stage0-design-r2/` are unchanged. The re-check is `review/STAGE0-RECHECK-r2.md`
(SHA-256 `33c279ef…76e6`). The r3 design-evidence code is in `stage0-code-r3/`,
and its evidence and run manifest are in `stage0-design-r3/`.

## Owner decisions (2026-10-26), recorded in the plan with the owner's wording

**O1, two-layer freeze: approved.**
- "Layer 1, the scientific specification": freeze the masking law, the
  geometry, the equivalence rules, the search domain, the invariants and the
  acceptance criteria.
- "Layer 2, the implementation": only after Layer 1 passes independent review,
  finalize and freeze the production enumerator, the controls, the
  configuration hashes and the execution certificate.
- "Complete enumeration code now: No; defer until the design layer is frozen."

Where it lands in the plan: header, §5b, §12. r3 presents this plan as the Layer-1
object. The code is design evidence and is not frozen. Layer 2 is a stated plan
with its own later review: the production enumerator, the controls, the
configuration hashes, the execution certificate, and the re-check's
fail-closed items 1–8. The v8 enumeration is not authorized.

**S11, P_A-dir: adopted as a required control, not a diagnostic.** "It must
detect incorrect elimination in individual directions even when aggregate counts
appear correct."

Where it lands in the plan: §4, §5, §6 C11, §7, the mutant table and §9. C11 is
required, in two parts:
- **(i)** The closure's per-direction tip-status tables, at every elimination
  and at the fixed point, must equal the independent reference's tables. A
  failure is VOID.
- **(ii)** P_A-dir and P_G-dir, with the aggregate P_A and P_G, hold on every
  survivor and on the planted retained sets. A failure is MISMATCH.

**Non-vacuity.** The −y-blind mutant was chosen before the run, as a direction
used neither by C3's dropped tip (+x) nor by the port's axis (z). On toy and
planted instances only:
- it fails C11 (i) and C11 (ii), and no other control;
- all 44 reported counts are identical to the frozen rule's;
- P_A-dir finds violations and the aggregate P_A finds none.

`s0mutants.py` checks all of this as `direction_demo`.

## Re-check items

| item | where | how |
| --- | --- | --- |
| R1 | owner decision O1, above | Applied as decided by the owner, not under r3's earlier draft, which put the code in Layer 1. |
| R2, depth ranges | plan §6 C1–C3; `s0controls.py` (`depth_plan`, `c1_cones`, `c2_tips`, `c3_planted`); `s0native.Lanes` | C1 and C2 now run at A F 0–15 and B 0–8 (pair (7, 8)), and at G F 0–23 plus B 0 (pair (−1, 0)), lane-parallel on generic random backgrounds. C1 perturbs exhaustively to depth 8; beyond that it covers the shell d − 3 to d + 2 plus 1,000 sampled interior cells per depth, and the plan states this limit. C3 plants at A F 1–15, B 1–8 and G F 1–23. Nothing runs on v8's configuration class. |
| R3, count preservation | §6 C8; `c8_symmetry` | Every reported count is compared, orbit-reduced against full: 44 counts, with 0 mismatches. G-linkage stays per record. |
| R4, small fixes | §6 C10, refusal, S6; `s0geom.py`; `s0s6.py` | C10 has two parts: (i) a code invariant, which cannot fail; (ii) the port samples are in-frame under G, which can fail. The guard covers `Context`, `num_records`, `record_at` and `record_samples`, with the docstring corrected; refusals are 5 of 5. S6's JSON carries "proof-check of PO8; not a result". |
| R5, retention | §6 C13; `s0run.py`; `stage0-design-r3/runs/` | Every step's stdout and stderr is retained and named in the manifest. `rerun.py`'s timing goes to stderr. `-O` identity is checked for every deterministic step. |
| R6, §A.41 rows | §7 | Corrected rows: C11 (now required, with its non-vacuity row); the C1–C3 depths as run; C8; C10; C13 split into design evidence and Layer 2; refusal and the certificate. |
| S5 note | §6 C7 | On v8 contexts (about 29 non-fixed quantities), `s0ref` runs in synchronous mode, so C7 compares two fixed-point algorithms there. |

Nothing from the re-check is declined.
