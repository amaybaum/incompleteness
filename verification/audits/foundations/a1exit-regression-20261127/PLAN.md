# A1-EXIT final regression audit (#1468): plan

**Status.** Writer's plan, committed before the report. Paper-only. It edits no manuscript, Lean module,
registry, ledger or plan file.

**Authorization.** Owner `amaybaum`, #1169 comment 7214186738, 2026-11-27T09:01:16Z (DP-1): "Authorize
the #1468 regression audit with a designated writer. Reuse existing accepted evidence and limit the audit
to its necessary scope." The standing policy of #1169 comment 7213780573 (`amaybaum`,
2026-11-27T08:39:51Z) applies: "Minimize the remaining A1 retirement requirements to those strictly
necessary for correctness and scientific integrity."

**Goal link (§A.47).** A1 retirement (#1477, #1169), through #1468: decides whether the integrated A1-exit
changes weaken, strengthen or alter any physical prediction or empirical comparison without explicit
justification (owner requirement 6, #1169 comment 7048255658). The audit is listed as necessary by r6
Amendment 8 §3, adopted at `f10195d4`.

## 1. What is audited

The **integrated A1-exit changes** are the composition of two layers, measured against the accepted
before-baseline of `../a1exit-regression-20261121/` (pin `1c7eedc4`, the state before any Step-2 change):

- **Layer S (Step 2, landed).** `1c7eedc4..53c6601a` on `papers/*.md` and `book/*.md`. Every manuscript
  commit in that range belongs to the A1-exit merges #1470, #1472, #1473, #1474, #1475 and #1494.
- **Layer R (retirement, planned).** The manuscript edits (`papers/`, `book/`) of the retirement plan's
  edit list, `a1exit-deletion-20261121/edits.json` at PR #1477 head `4c79be64` (blob `ec384fdf`), applied
  with the plan's own rule (`old` exact and unique, else `old_step2`) by the plan's `edits_check.py`.

Layer R is evaluated at the plan's base H = `53c6601a`, where every edit applies, and at current `main`
`d7794dc9`. Changes on `main` after H that are not A1-exit changes (#979, #924, #1558/#1560, #1588) are
outside the audit; where they touch a site an edit targets, the edit's re-cut form is a re-check item.

## 2. Evidence reused

- The baseline extractor `../a1exit-regression-20261121/baseline.py` (accepted on #1471) and its
  `--compare` / `--compare-tree` modes, number tokens (`parse_numbers`) and label vocabulary
  (`labels_of`). No new extractor or inventory rule is introduced.
- The A1-EXIT ledger (`../a1exit-ledger-20261120/`): rows X-47, X-48, X-11, X-71 and their correction
  cells, which are the justification cited for a change where a ledger row prescribes it.
- The plan's edit list: each edit's `row`, `disposition` and `reason` fields, which are the justification
  cited for a Layer-R change.

## 3. Classification rule (fixed before the report)

Each changed item that the baseline inventory or a per-file token comparison reports is classified:

- **unchanged** — no number token, unit, uncertainty or prediction/status table cell changes, and the
  statement's comparison with data is the same;
- **changed, justified** — a change whose explicit justification is cited: a ledger row correction, an
  edit's recorded reason, or an owner record. A scope qualifier that restates the same condition (for
  example "under A1" replaced by "for a finite total system", A1 being finiteness of the total
  configuration space) is classified here, as a renaming of a carried condition;
- **changed without justification** — a finding.

**What counts as a finding.** Any of:
1. a number, unit or uncertainty of a prediction or empirical comparison that changes, or a comparison
   that is removed, without a cited justification;
2. a status label of a prediction or empirical row (appendix-a rows, SM §7.6, GR §7.4, book status
   tables) that changes without a cited justification;
3. a result presented as unconditional whose support needed A1, after A1's deletion (owner condition on
   R1 and C1; ledger "What may not remain");
4. a finite-lattice value presented as an approximation of ℤ^d, or an L → ∞ value presented as more than
   numerical evidence, without an established convergence result (owner rule, #1169 comment
   7048255658).

Prose that changes no prediction, number or comparison is not re-reviewed for wording: that is the
scientific delta review (7.1), not this audit.

## 4. Steps

1. Layer S: `baseline.py --compare 53c6601a`; read every non-unchanged entry in a prediction or status
   table and every entry in C-CDO, C-FINL, C-CAL, C-OBS and C-OPEN; per-file number-token loss.
2. Layer R: build the after-tree from H (and from `main`) with the plan's edits; per-file number-token
   loss; per-edit number change and table class; read every edit on a C-FINL, C-CAL, C-OPEN, C-OBS or
   C-PROSE entry and every edit that changes a number.
3. Integrated: `baseline.py --compare-tree` of the after-tree against the pin.
4. X-48 reading with and without A1; X-47 values whose reading depends on L → ∞; R1 and C1 premises.
5. A delta script and recipe for the final H.

## 5. Out of scope

New controls, schemas or inventories; wording review; Lean, registry and verification-file edits of the
plan (they carry no physical prediction); changes on `main` that are not A1-exit changes.
