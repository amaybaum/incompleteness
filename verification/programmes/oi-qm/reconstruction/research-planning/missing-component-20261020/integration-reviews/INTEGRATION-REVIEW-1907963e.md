# Review of `1907963e` (PR #885): native-instrument corrections, INTEGRATION.md, PLAN pointer

Reviewer: independent and read-only. Nothing was committed, pushed, commented or dispatched. Worktree:
`…/scratchpad/review-885-integration/wt` (detached at `1907963e`). Python 3.13.16. Paths below are relative to
`verification/programmes/oi-qm/reconstruction/research-planning/missing-component-20261020/`, with `NI/` short for
`mc-node9/design/native-instrument/`.

## Verdict: ACCEPT WITH CORRECTIONS

The corrections to the native instrument are applied accurately and the checker change is correct. Every
identifier in INTEGRATION.md resolves. One factual detail in the open obligations has no source (B1). The other
findings are missing caveats or presentation issues.

## A. Corrections and checker

**Integrity and replay**
- `sha256sum -c` passes for `NI/SHA256SUMS` (6 files) and for `NI/review/SHA256SUMS` (12 files). `PREREG.md`
  hashes to `e92724ca…`.
- `python3 -I -B instrument_checks.py` and the same with `-O`, run from `NI/`: both outputs are byte-identical to
  `instrument_checks.out` (13 s, rc 0).
- Compared with `455eb092`'s output, exactly three lines change: Q5, Q6b and VERDICT.
- Review scripts, run with `python3 -I -B` from `NI/review/`:
  - `indep_register`, `indep_cher`, `indep_native` and `coordinator_weight20` all reproduce their saved outputs.
  - `indep_degree_qm` differs only by the missing last line, as `review/README.md` says.
    `coordinator_weight20.py` gives 524800 = 2⁹·1025, which is divisible by 50, by enumeration and in closed form.

**Each required correction (review/REVIEW.md:57–77)**

| # | Applied? | Notes |
|---|---|---|
| 1 Degree 12 | Yes: README.md:22–24, REPORT.md header (lines 10–11), §3.2 (REPORT.md:102–105), PR comment 6380960431 | The text matches the review: 12 is this sampler's degree, the lower bound is 2, and lower-degree flags suffice. The example flag 1⊕x₀x₁⊕x₂x₃ has weight 10 and degree 2 (`indep_degree_qm.out`). |
| 2 Q5 count | Yes: the checker string, REPORT Q5 row, PR comment | The checker loop gives 4 settings × (16 λ × 8 r) × 2 seeds = 1024 runs, as stated. The parenthetical "128 per setting" is dropped, which is harmless. |
| 3 Native scope | Yes: README.md:13–16, REPORT §3.1 | The scope is correct. Nit: README.md:14 says "the re-preparation registers there", which places them at the record receiver. They are the four outgoing receivers at tick 2. |
| 4 Q6(c) layout | Yes: REPORT.md:85 | The permuted-layout values match `indep_native.out`: R first fails at D = 8, TV@10 = 0.297938, and Z is None. The checker's VERDICT also says "for this layout". |
| 5 Generated verdict and Q6(b) closure | Yes | See below. |
| 6 Preregistration precedence | Partly: REPORT.md:4–6 | **NB-1:** README.md:7 still says "written before any code" with no qualification, which is the unverified claim the review flagged. |

**The checker change (instrument_checks.py:308–327, 365–367, 436–449)**
- **Q6(b).** For every setting, preparation, outcome o and fresh vector r with Pr(r) > 0, the checker builds the
  conditional law of λ′ given (o, r) and compares it cell by cell with `prepared_law(±AX[a])`. This is Q4's
  comparison with r also conditioned on, so it is the preregistered per-setting conditional-law test.
- **Why it fails.** λ′ is fully determined by (o, r), while every target has a non-degenerate component (a·c = 0 or
  4/5). The test therefore fails for all four settings, which is the expected result.
- **One-sided comparison.** The check is valid, because both laws sum to 1.
- **VERDICT.** The Q6(a)/(b) verbs and setting lists are now computed from `junk`, `fresh_id` and
  `fresh_closure_fails`.
- **Nit.** `nat_cases // 2` assumes the two hard-coded seeds; it is correct here.
- **`-O`.** The checker contains no `assert`, so `-O` cannot change its behaviour.

**Further non-blocking points in NI/**
- **NB-2.** REPORT.md:5–6 says every number is printed by `instrument_checks.py` "with two exceptions". The
  corrections add more numbers that the checker does not print:
  - TV ≈ 0.298 and the permuted layout, cited to the review;
  - 1⊕x₀x₁⊕x₂x₃;
  - "odd part divisible by 5 … or by 25" (REPORT.md:31–32), which cites nothing and comes from the review's scope
    note. It is correct by the product-law argument; 9/25 needs 25.

  Update the exception list, or attribute these values to `review/`.
- **NB-3.** review/REVIEW.md:8 cites `run_normal.out` and `run_O.out`, which are not in `review/`. Say they are not
  retained, or add them.
- **Minor review items, not required:**
  - the unchecked "non-dyadic … cannot give them" PASS line (`instrument_checks.out:4`);
  - Q5 being gated as a control.

  Neither is addressed; that is acceptable, since the review lists them as minor.

## B. INTEGRATION.md

**Identifiers.** Every sha256 matches its file:
- the uploads `3d18fe9c`, `286d9b1c`, `c204e6f6`, `9c2a5dcc`, `15af0674`, `e50b51f0`, `2a51fe2a`, `88f80567`, `977e8e33`;
- `3e47e54e`, which is the combined bundle's `START-HERE.md`;
- `529185bb`, which is `archives/OI_native_X_instrument_handoff_v1.zip` in the combined bundle.

All four full #910 commit ids exist and are ancestors of `1c8c9e5e`. #905 is KTRANS-SEP-2.

**BLOCKING**
- **B1 — INTEGRATION.md:69, "the required two-site outgoing encoding".** No source states this.
  - The native-X outgoing encoding is three sites: E = ((x,1,y) at q_Y, (x,1,r) at q_R, (0,0,z) at q_Z). See
    `workspace/oi_native_x_instrument_v1/REPORT.md:192` in the combined bundle, its `START-HERE.md` and the
    external review.
  - The native-Y and #910 records speak of a "common raw carrier" or "common usable carrier interface", with no site
    count.
  - Suggested fix: "an outgoing encoding the next instrument accepts (the native-X carrier uses
    (x,1,y)@q_Y, (x,1,r)@q_R, (0,0,z)@q_Z)", or drop "two-site".

**NON-BLOCKING (each row was checked against its source)**
- **NB-4 — line 46, native X.** "A conditional X instrument" drops the source's own word *candidate*. The report
  says "a conditional one-axis instrument candidate"; the external review says "conditional X read/reset candidate…
  provisional… pending a deeper proof audit… before formal certification".
  - Restore "candidate".
  - Optionally add that the native herald is checked finite-and-algebraically, not by a full-lattice simulation (the
    review's item 2).
  - The review-level cell is accurate.
- **NB-5 — line 44, native selector.** The row omits the review's main should-fix item (F1). The "selection" is a
  one-time pad: the unselected signs stay in the public record, encrypted under private control data, and the record
  law equals single-port access plus three fair coins.
  - "under supplied … access" only gestures at this.
  - F3 (the T=185 instance is conditional on the unreviewed transport theorem) is covered by obligation 1.
  - Also, "readout of a setting" should read "readout of the selected sign for a setting".
  - The "holds, with corrections to claim text" level is accurate. Those corrections are applied nowhere, which is
    why the index row should carry them.
- **NB-6 — line 45, read-reset.** The row omits SF1. Input-independent reversible permutations, a class that
  contains the XOR masks, reach minimax 7/30, including when validity is required. So "9/10 if validity is required"
  is specific to translations.
  - The row's "XOR-mask" prefix keeps the statement true, but the 7/30 boundary is the robust form.
  - SF2 is also missing: the shell collapse binds only if private payloads must be fair and independent.
- **NB-7 — line 43, selector record.** The positivity criterion's premise is missing (F1: the input is a qubit with
  no accessible correlate, and the apparatus is independent of it).
  - "No native selector" could be read as a no-go. The source means that none is constructed; say so.
  - The factorization is the review's recommended acceptance test (F2), not a result of the checkpoint. Present it as
    the adopted acceptance rule, for example in the Acceptance section.
- **NB-8 — line 47, combined handoff.** The review cell gives replay only. The radius-185 audit was reviewed inside
  the research effort, so in this index's terms it is internal. Its source scope is "concrete application audit, not
  all-formula compiler certification" and should be stated.
  - The replay claim is confirmed by `combined-review/replay.out`: all groups PASS, including the full native-X
    suite normally and with `-O`, rc 0.
  - That record does not itself print the Python version.
- **NB-9 — lines 37–38.** The legend defines *independent* and *internal* but not *external*, which line 46 uses.
- **NB-10 — line 48, native Y; obligation 1, lines 65–66.**
  - The row is faithful:
    - the triple (y, y, 1⊕xy);
    - the reachable codes 001/111/110;
    - "within one cell" keeps the source's scope: the obstruction does not exclude an ancilla, a larger gate or a
      history-carrying controller.
  - The row omits the source's caveat that the staged-disclosure contract is abstract: the recorder and reset are
    supplied, and no native masking device is built.
  - The internal reviews in that bundle and in the combined bundle's parallel audit did audit the general extrusion
    and frontier proof. Obligation 1 should say so. As written, it reads as if the proof had no review at all. What is
    missing is an *independent* review, which is correct.
  - "Replays reproduced" is confirmed by `native-y-review/replay.out`: 10 of 10 checkers, normal and `-O`.
- **NB-11 — line 49, #910.** The row is faithful to `junction_v4/REPORT.md` and its review: the bijective free-pivot
  obstruction, M1 and the old input untouched, M2 retained, six current sources, the output unevaluated.
  - #910 calls this review "independent". This index classes it as internal, which is conservative and consistent
    with the legend, since the review was commissioned by the research parent.
  - Say that the classification differs from #910's own label.
  - #910 has since advanced to `8daae9f6` (six-source computation, 06:42Z). The pin at `1c8c9e5e` is a correct
    snapshot, but the index is now behind.
- **NB-12 — §A.42 and evidence location.**
  - The review verdicts in lines 43–45 rest on review reports held only in a session scratchpad. They are not in the
    repository, not on #885 (no comment between `455eb092` and `1907963e`) and not identified by hash. A reader
    cannot check the review column.
  - Add their sha256s, or retain them as `NI/review/` is retained:

    | Review | sha256 |
    |---|---|
    | SELECTOR-RECORD-REVIEW | `e9bac228…0a06` |
    | NATIVE-SELECTOR-REVIEW | `9cdb61bf…b8df` |
    | READ-RESET-REVIEW | `6d6e121d…52dc` |

  - The #910 commit ids and the bundles are off `main`. That is acceptable for a draft research index, but it must be
    resolved before any landing (§A.42 items 2–3).
- **NB-13 — line 42.** The identifier is a path, not the exact commit that line 4 promises. Cite `455eb092` as the
  reviewed state.

**Faithful as written**
- The acceptance-rule bullets, lines 27–33:
  - joint and every branch;
  - conditional freshness and no overwriting of a reserved fair source;
  - the 5:2:3 versus 5:3:2 case, with terminal R as a diagnostic beside the joint rule;
  - TV 7/8 for identical uniform ports.
- The "supplied" list, lines 57–61: the menu, with reciprocity leaving both (4/5,3/5) and (3/5,4/5) on the
  sharp-qubit circle; readiness and resources; the clock and settings; access.
- Obligations 2–6, apart from B1.
- The closing scope sentence, lines 78–79.

## C. Hygiene

- No self-narration of revision history and no caps emphasis in the added prose.
- Status sits in README headers and the INTEGRATION table, which are status artifacts.
- No unreviewed result is labelled reviewed: NB-11 is conservative, and NB-12 concerns where the reviews are
  retained, not whether they happened.
- Every full commit id named in the diff exists in the repository: `1c8c9e5e`, `3fcaa271`, `5d36a3f6`, `4f240773`,
  and the short `455eb092`, `9283b435` and `a7b7cb72`.
- PLAN.md:75–76 is only a pointer.
