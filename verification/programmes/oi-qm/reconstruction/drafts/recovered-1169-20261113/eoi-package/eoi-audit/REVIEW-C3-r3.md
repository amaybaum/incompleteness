# Re-review of AUDIT-C3 r3 (edited lines only) against REVIEW-C3-r2.md

- **File reviewed:** `AUDIT-C3.md` r3, sha256 `d143754b469a5f9eaa90b9b0db5f06d2ec85ffbf946c9f9de855d3a55e40e68b`.
- **Diff base:** `AUDIT-C3-r2.md`, sha256 `412b50a30a73a18a387905493eaad480c5dc948acab78d822a579bde9c8f9e22`. Both files were
  re-hashed before review.
- **Scope:** only the lines that `diff AUDIT-C3-r2.md AUDIT-C3.md` shows as changed. The diff touches nothing else.
- **Snapshot:** `origin/main` `5ce4f98e`.
- **Read-only.** No new computation.

## Verdict: **ACCEPT**

B1, B2 and N1–N4 of REVIEW-C3-r2 are closed. Three minor wording points remain (n1–n3). They are optional and do not affect
any outcome, classification or the follow-up's decidability.

## Closure check

| r2 ID | r3 location | Status |
| --- | --- | --- |
| B1 | §2 M-ARC (lines 184-209) | **Closed** (details below) |
| B2 | §9 (lines 407-414); AW-C3-2 (lines 567-571) | **Closed** (details below) |
| N1 | Central answer (lines 48-51) | **Closed** (details below) |
| N2 | §3 (lines 239-245, 259-265) | **Closed** (details below) |
| N3 | §0.3 (lines 95-97); §3 (line 244) | **Closed** (details below) |
| N4 | §0.3 (line 92); §9 (line 413) | **Closed** (details below) |

**B1. M-ARC is now specified.**
- *Parameters.* `w = 3`, `T = 4`, `|H| ∈ {4, 6}`, so `L ∈ {7, 9}`. `T ≤ |H|` holds at both sizes.
- *Method.* Exact span membership over `F_2`.
  - Enumerating fixed schedules covers adaptive ones: within a branch an adaptive schedule is a fixed schedule, and under a
    full-support law determination for a fixed schedule does not depend on the branch.
  - "N2 does not enter" agrees with §9.
  - The enumeration is small, so the check is cheap.
- *Decision rule.* It is to be preregistered and has four labels: exposure, survival, size-dependent and void. Exposure and
  survival both require green controls at both `|H|` values, so each outcome is reachable.
- *Horizon.* The horizon is now worded as no wrap-around through `H`. AP1:338-341 is cited only for budget-relative isolation.
  The text also notes that variant D's archived site couples back within one tick, which is the intended de-isolation.
- *Status.* It is still named only: "not adopted, not run" (line 165).

**B2. The Theorem W pointer is correct.**
- It is restated as an odd-`q` R-W positivity hypothesis, "every ancilla law has a quantum state as its R-W image"
  (M1D:473-474, verified).
- Full-support laws are explicitly included in the MECH-1 check.
- The `q = 2` sharp-cell argument is not transferred.
- The reviewer's `q = 3` control is cited only as provenance.

**N1.** "Pointwise" is now limited to `E_A` and `E_B`, and `E_A′` is described as a 1/16 branch (MI-R:283-285, verified).

**N2.** Outcome 2 now rests on QA:142-144 (P2 "fixes which functional is known, not its value"; the audit's quotation joins
lines 142-143 with an ellipsis, which is acceptable) and on QA:777. The counter-reading (QA:48-50, QA:780 → AP1:297-299) is
stated with its consequence.

**N3.** MI-R:374 (C-P2, verified) and QA:780 are cited as the record-level instance of the support condition under SA-1.

**N4.** The review note is marked "provenance only".

## Optional wording points (non-blocking)

- **n1 (lines 201-202).** C-SUPP's bias half refers to "a stated non-uniform law" but does not state one. Name it, for
  example the `P(w = b) = 3/4` pair of §0.3, so that the rule can be preregistered without a choice left open.
- **n2 (lines 182-183).** C-NV says "one carrier slot read through a meter". The M-ARC model has no separate meter cells;
  every read is a registration of a `V` ring cell. Rephrase, for example as "a `Q* = 0` functional on the current `V`
  determined by one registration".
- **n3 (lines 204-206).** The decision rule's "Exposure" and "Survival" do not name the variant. Add "in variant D", matching
  the Question at line 177.
