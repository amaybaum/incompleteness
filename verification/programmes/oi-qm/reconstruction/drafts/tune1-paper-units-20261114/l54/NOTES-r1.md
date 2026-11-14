# L5.4 r1: reading inventory and limits

Companion to `L54-r1.md`. Citation forms as defined there.

## Read

Worktree `wt-mainread` (`main` at `c3b5f37a`):

| File | Lines read | Used for |
|---|---|---|
| `TUNE-1-STEP2-PROPOSAL.md` | 60–600, 668–760, 800–812, 825–860 | rule and carrier classes, interface, modes, D1–D7, Q0–Q6, control table, proves-too-much check, L4 |
| `TUNE-1-STEP2-AMENDMENT-1-final.md` | 1–461 (whole file) | declared target, Lüders reads, credited assignments, `F`, Q3′, Q5′, Q6′, B3, B4, C-NULL, B6.3 |
| `…-final-addendum-1.md`, `-addendum-2.md` | whole files | C-POS-2 scope only; nothing used |
| `TUNE-1-STEP2-SESSION3.md` | 1–423 (whole file) | Lemma 0, Lemma A-T, FC-1, FC-2, nodes L5.1–L5.6, §4 row, tokens |
| `TUNE-1-STEP2-SESSION4.md` | 1–60, 240–520, 593–680 | Lemma I, transfer table, F-S3-1, NL-C, NL-C′, gaps, NL-C rows for R-lin |
| `TUNE-1-STEP2-SESSION2.md` | 263–290 | C-NULL derivation in both modes |
| `oa-2-20261112/OA-2-REPORT-r4.md` | 92–135, 176–200, 240–330, 490–612 | procedures, C-PM, H-AR, Proposition B, Theorem E, (SP), Corollary E1 |
| `mechanism-1-20261107/DESIGN.md` | 84–104, 398–450 | Lemma A, Corollary A′ |
| `papers/Main.md` | 556–602 (each paragraph, long lines truncated at about 2,600–4,500 characters), 724 (ledger) | classical-dimension proposition, extension-boundary remark, gluing theorem and corollary, 588, telescoping lemma, uniform continuum theorem, summary item 3 and 4, ledger items (vii), (xiii) |

Worktree `wt-3a` (`8228b3c2`, off `main`): `TUNE-1-STEP3A-r3.md` lines 1–140, 480–720, 778–900.

`AGENTS.md` as supplied with the task.

## Not read

- `TUNE-1-STEP1.md`; `TUNE-1-STEP2-SESSION1.md`; the remainder of Session 2 and its C-POS-2 rerun;
  amendment drafts r1–r3; Session 4 lines 61–239 (R-nl witnesses W-nl-1 to W-nl-4, Lemma NA's proof)
  and 521–592, 681–767.
- `OA-1-REPORT-r5.md`, `OA-3-REPORT-r4.md`, the OA reviews, `mechanism-2-20261108/DESIGN.md`.
- The remainder of the Step 3A report, its review and its r2.
- Any Lean module; `papers/SM.md`; the source records of C-POS-1 and C-POS-2
  (`history-architecture-v5`, `finite-a2-v5`).
- Issue #1236 and PR #1237 comments, including the owner's 2026-11-14 authorization, which is
  taken as relayed in the task.

## Could not check, or checked only partly

1. **Reading of `F` at `ℓ = 0`.** Theorem 1 uses the empty preparation. The texts read do not
   exclude it (AF:116, :134–135) and AF:389 names it, but no sentence states it as a definition.
   Corollary 1a is the fallback (`ℓ ≥ 1`, `K ≥ 3`, constant `1/128`).
2. **Lemma A-T (a), (b).** Its three proof steps (S3:79–85) were re-read and re-derived by hand for
   the two-sequence form of Lemma 1. Its Session 3 review record was not read.
3. **Lemma I.** Steps 2, 3 and 5 were re-derived by hand for both reads (Proposition 2, step 1).
   The Session 4 text was read; its review was not.
4. **Corollary 1a's continuity constant.** One derivation only (a two-step hybrid).
5. **Lemma 4 (c).** Rests on identifying OA-2's `Z₀`, preparations and effects with TUNE-1's
   objects; that identification is the unreviewed reading recorded at 3A:595–597.
6. **Controls K1 and K2.** The classifications of C-POS-1 and C-POS-2 are taken from the proposal's
   control table and the amendment, not from their source records. For the gluing realization only
   the construction paragraph and the corollary of Main (578, 580) were read; the certified probe
   files were not opened.
7. **Exchange mode.** Lemma 1 was checked for non-adaptive sequences from the description at
   P:155–171 and S3:65–68, :83–85. The statement for adaptive protocols in §7 item 6 of the main
   file is not derived.
8. **Prior art search (§A.19).** Searched the TUNE-1 directory for prior statements of the shift
   form applied to Q5′ (`grep` for "translate", "relabel"); found M1 Corollary A′ and Lemma A-T as
   the nearest. The wider corpus (other programme directories, audits, Lean) was not searched, so
   "new for TUNE-1" in the main file is relative to the files listed above.
9. **Line numbers.** `Main:n` at `c3b5f37a`; TUNE-1 files at `c3b5f37a`; `3A:n` at `8228b3c2`.
   Spot-checked after writing: P:72–77, P:206–209, S3:162–163, S3:199–200, 3A:595–597,
   3A:613–617, OA2:601–602, AF:88–91, :104, :116–123, :125–135, :153–175, :269, :274, :389.

## Disclosure

- Commands: `ls`, `wc`, `sed -n`, `cut`, `grep`, `fold`, `awk` (line lengths), `git rev-parse`,
  `mkdir`, and one short Python text substitution applied to `L54-r1.md` itself. No interpreter was
  run on any OI rule, model or record law; all arithmetic and the `ℤ/4` example of control K4 were
  done by hand.
- No repository check script was run: both documents are outside the repository tree.
- Nothing in either worktree or in the repository was edited, committed, pushed or posted.
