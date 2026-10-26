# Re-check: NP-AVG-1 Stage 0 r5 (diff-only freeze gate under O-a)

**Reviewed.**
- `stage0/r5/STAGE0-PLAN-r5.md` (SHA-256
  `1a30188e70804644a6ff65b3114ab82f8be40a2b056d0e2862ce595a8982847e`) and
  `STAGE0-CHANGES-r5.md` (`247859ac…1a00`), on PR #935 at `f33d8d63`.
- Diffed against `stage0/r4/` and `stage0/code-r4/`, and checked against
  `review/STAGE0-RECHECK-r4.md`. The committed copy is byte-identical to mine.
- `stage0/design-r5/`:
  - `RUN-MANIFEST.json` (`3f821cc5…308f`): every code hash, and every retained stdout hash,
    equals the manifest;
  - all ten steps exit 0, and every deterministic step is `-O`-identical.

**Read-only.** Nothing was edited, committed or pushed. No closure ran on anything derived from
v8: v8 setups were constructed only, to be refused. My outputs are in `S/npavg/review-r5/rerun/`
and `S/npavg/review-r5/probe/`.

## Verdict: ACCEPT. Layer 1 is ready to freeze, with no required changes

Every R4 item and nit is applied with the review's text. The six departures are sound, and the
disclosed change in observed failures is correct, with every kill still at its named case. My
probes and the whole cheap suite replay byte for byte, and the owner's five standing checks are
met.

The open item is rule T's consequence, which awaits the owner. The plan records it as pending
owner, and its text already states the geometric fact only (§5).

## 1. Reproduction (my runs, against `code-r5`)

| step | my result | against `runs/` |
| --- | --- | --- |
| `s0controls.py` (full), normal and `-O` | exit 0, `failed: []`; 54 counts; refusal 36/36; C11 (iii) 96 sets, 0 failures | byte-identical; `-O` identical |
| `s0s6.py`, `s0symcheck.py`, normal and `-O` | exit 0 | byte-identical; `-O` identical |
| `rerun.py`, `planted.py`, `radius_mutants.py`, `exact_small.py`, normal and `-O` | exit 0 | byte-identical; `-O` identical |
| `s0mutants.py` (QUICK) | exit 0 | byte-identical (`85ddb4f1…`) |
| my guard probe (`guard_probe.py`, the r4 file unchanged) | 15 of 15 refused | byte-identical to `runs/review_guard_probe.out` |
| my frame-adjacent probe (only the mutant renamed) | as below | byte-identical to `runs/review_frame_adjacent.out` |

**The full mutant campaign** is not run, as §A.40 requires. It belongs in CI, on the owner's
dispatch approval.

## 2. R4-1 to R4-7 and the nits

**R4-1: applied.**
- **Text.** The §6 C11 (ii) text is verbatim. The G adjacent family is now planted without
  ((n+2, 0, 0), 0). Assertions check that the removed cell is that family's −x tip, that it is
  ineligible, and that it lies in a fixed or port cone.
- **Mutant.** The mutant is mine: the decision ignores frame and fixed cover on −x, with the table
  truthful. It is named at C11 (iii), "frame-adjacent G family eliminated", and is killed there.
  It also fails C7, C8, C11 (i) and C18.
- **My probe on r5.**

  | rule | family without its in-frame tip | r4's family |
  | --- | --- | --- |
  | frozen | 7/7 and 12/12 retained | — |
  | the mutant | 0/7 and 0/12 | intact, 8/8 and 13/13 |

  The blind-G and ignore-fixed −y mutants leave the r5 family intact, as they should.

**R4-2: applied.**
- **Keying.** The refusal is keyed on (dim, n, port), compared against a literal, with the port
  compared as a tuple. Its 36 attempts are all refused.
- **My r4 guard probe:** 15 of 15 refused, including the five r4 bypasses (sources changed,
  sources empty, ρ = 5, t_last = 24, `record_at` on a superset) and both rebindings.
- **New attempts** (`probe/guard_probe2.{py,out}`):

  | attempt | result |
  | --- | --- |
  | float port | refused |
  | n = 6.0 | refused |
  | port as a generator | refused |
  | ρ = 10, t_last = 40, no sources | refused |
  | `record_samples` on a superset | refused |
  | `ref_context` with a float port | refused |
  | `ref_retained` | refused, before any closure |
  | a `Setup` subclass that overrides `key()` | not refused |
  | port `None`, or a port moved to (0, 0, −2) | not refused |

  The two not refused are not findings:
  - **Subclass override:** deliberate tampering inside the process, of the same kind as the
    rebinding noted in r4. The Layer-2 manifest and certificate items 1 and 6 cover it.
  - **Port `None` or moved:** a different configuration. Its contexts lack, or move, v8's port
    samples, so it is not v8's class.

**R4-3: applied.**
- **PO6 (G)** is verbatim, and now holds. S_G is a function of the frame's non-source cells and
  the seeds. Given the non-source frame, the seeds are independent of G and of every in-frame
  quantity, and PO4 (G) completes the reduction to Law_P.
- **PO7 and P_G** carry the slice −1 seed condition, |c| > 7.
- **Citations.** C_A, C_G and PO6 (A and G) cite PO4.
- **P_G for slice −1 elements.** The only new wording is "|c| > 7 if it is at slice −1".
  A ρ-maximal slice −1 element cannot be retained, since an F cover would need reach ρ + 1. So P_G
  holds vacuously there, and the statement is correct.

**R4-4: applied.**
- The text is verbatim.
- The change of the G observer classes from 173 to 24 is reproduced in r5's own run.

**R4-5: applied.**
- **Consequence.** The text is: "The report states this geometric fact only; law failure beyond
  k ≤ 2 is not claimed, since PO8 covers at most two Φ triples in clear." It is marked
  pending owner confirmation.
- **Invalid S1a.** "If S1a is VOID, MISMATCH or INCOMPLETE, rule T is not evaluated."
- **Checkpoint.** A §7 row records L_A, L_G and rule T's outcome in `result.json`, and Layer-2
  item 5 writes them.

**R4-6: applied.**
- G-linked and G-unlinked survivor counts are computed per record in the orbit-reduced path
  (`_g_linked_per_record`), never transferred.
- That makes 54 counts. The list is stated as closed against §3, and I confirm it is.
- 32 of the 54 counts are identically zero.

**R4-7: applied.**
- `blind_B_minus_y` requires a violation on an `A_B` or `adjPhi_A_B` set, and
  `blind_G_minus_y` one on a `G_F` or `adjFrame_G_F` set. Both are killed so.

**Nits: all applied.**
- "review R5", "review R8" and "review R1–R9";
- C11 (i) and (iii) added to §4's over-elimination guards;
- the `s0symcheck` docstring;
- the §7 complete-statement row marked as checked by independent review.

## 3. The drafter's six departures: all accepted

1. **PO7's middle sentence** is restricted to t ≥ 0. This is correct: a slice −1 quantity with
   |c| = 9 is a seed. For t ≥ 0 the cone reaches |c| + t ≤ 8 on slice 0 and ≤ 7 on slice −1, with
   matching parity.
2. **The PO6 joins** are grammatical, and the PO4 citations are in the right places. Nothing
   changes in substance.
3. **Literal-keyed guards** close the rebinding route. Both rebindings are refused in the suite
   and in my probe.
4. **Retained probes.** `guard_probe.py` is byte-identical to the committed r4 probe and to my
   copy. `frame_adjacent.py` differs only by its provenance header and the mutant's name. Both
   replay byte for byte.
5. **Tag placement** changes no wording.
6. **§A.44** is present on `origin/main`, at AGENTS.md line 1016, so the citation is valid.

## 4. The disclosed change in observed failures

In `runs/mutants_quick.out`, which my re-run reproduces byte for byte, four mutants no longer fail
`C11_props`:
- off-axis (all), named at C2;
- wrong-far, named at C15;
- far-cone-deleted, named at C1;
- radius −2, named at C1.

**All four are still killed at their named cases.** The cause is as disclosed. r4's G frame family
kept its in-frame tip quantity, survived these mutants, and produced the P_G hits. r5's family is
eliminated by them, which C11 (iii) reports.

**Campaign totals.**
- All 17 mutants are killed at their named cases, and the frozen suite is clean.
- The demonstrations fail C11 only, with counts equal to the frozen rule's:
  - blind −y fails parts i–iii;
  - ignore-fixed −y fails parts i and iii.
- The equivalent mutants behave as stated.
- Every bracketed cell of the §6 table matches the run, including the new
  `decide_frame_ignore_minus_x` row: C7, C8, C11 i and iii, C18.

## 5. The owner's five standing checks: all met

1. **The planted families are detected:**
   - B type: `blind_B_minus_y`, at C11 (ii), on an `A_B` set;
   - G: `blind_G_minus_y`, at C11 (ii), on a `G_F` set;
   - Φ-adjacent: `ignore_fixed_minus_y`, at C11 (iii);
   - G frame-adjacent: `decide_frame_ignore_minus_x`, at C11 (iii).
2. **Decision-level mutants are caught:**
   - `decide_blind_minus_y` and `decide_ignore_fixed_minus_y`, by the decision–table check of
     C11 (i);
   - `decide_frame_ignore_minus_x`, at C11 (iii).

   My `rv_decide_ignore_fixed_y` was caught in r4, and r5 does not change that path.
3. **The v8 refusal cannot be bypassed** by constructing a fresh object, by a larger region or
   slice range, by changed sources, by type variants of the port or n, or by rebinding the
   constants. See §2, R4-2.
4. **The PO statements are complete.** PO3 and PO5–PO8 are each stated in full and correct, and
   every proof-dependent rule cites its POs.
5. **The disclosure is accurate.** §9 gives 0 toy survivors and 32 of 54 counts zero, both
   correct. The over-elimination sentence is now accurate, and the two r4 limits are stated.

## Required changes

None.

## Notes, non-blocking (for Layer 2, not Layer 1)

- **The guard is a design-evidence safeguard, not a security boundary.** A `Setup` subclass that
  overrides `key()` bypasses it, as rebinding constants did in r4, and direct calls to the
  geometry primitives take no setup. The Layer-2 frozen manifest and certificate items 1 and 6
  remain the real gate.

## Owner decisions

- **Rule T's consequence (pending owner).** The plan's text states the geometric fact only. I
  recommend confirming it as written.
- **Then freeze Layer 1** (`STAGE0-PLAN-r5.md`, SHA-256 `1a30188e…847e`) under O-a.
- **Unchanged:**
  - Layer 2 follows the freeze, with its own review;
  - the full mutant campaign runs in CI on the owner's dispatch approval;
  - the v8 enumeration is not authorized.
