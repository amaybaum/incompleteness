# Pre-push check: MATH-CON-1-S1B-1 control-plane amendment, aeab48e3 → a44c0206

Independent checker, 2026-11-09. Read-only: no git writes in the worktree, no push, no GitHub writes.
Worktree `scratchpad/wt-mathcon1-round`; `git status` clean before and after; Python run with `-B`.

Authorization: #1169 comment 6742682753, by `amaybaum`, 2026-11-09T14:35:00Z. The quoted option text matches
the brief verbatim. PR #1215's remote head is `aeab48e3662f3eb1302ff590f037e8d68319d037` (draft, open).

## Verdict: PASS (all seven checks). Nothing blocks the push.

| # | check | result |
| --- | --- | --- |
| 1 | chain shape | PASS |
| 2 | diff scope | PASS |
| 3 | XC4 as amended; fixture 5 | PASS |
| 4 | `availExt n O F` signature | PASS |
| 5 | V3 blocks; precondition 7 | PASS |
| 6 | local checks | PASS |
| 7 | commit messages | PASS |

## 1. Chain shape: PASS
- `3004ca93` has parent `aeab48e3`, `adbc238f` has parent `3004ca93`, and `a44c0206` has parent `adbc238f`. Each
  has exactly one parent.
- Each of the three commits touches exactly one file,
  `verification/programmes/oi-qm/reconstruction/round-mathcon1-s1b-1/preregistration.md`.
- Over all of `fd539e15..a44c0206` there are 5 commits. All are single-parent, and all touch only that file.
- Final blob `65be2fc9fe2fb5bf6b1f9a11c0732e99881539b5`, sha256
  `7f5fb95515723c6587fb0931a928639e2f500cbd488a674ab583dec37d19fd83`. Both match the brief.

## 2. Diff scope: PASS
The full diff is 18 insertions and 8 deletions in one file. Each hunk maps to an owner-approved item:
- `:235`: `availExt n F` → `availExt n O F` (the frozen-line item).
- `:630–633`: XC4 rewritten (the XC4 item).
- `:662–665`: the fifth fixture (the "5th pre-F fixture" item).
- `:1293–1295` (self-test replay), `:1354` (§A.41 row) and `:1487–1490` (precondition 6): "four" becomes "five",
  with the fifth fixture named. These follow necessarily from the fifth fixture.
- `:694`: one line on where the XS table lives (the note item).

There is nothing else. The header (`draft r13`) and the status paragraph are unchanged, and no earlier commit on the
branch bumped the draft number. `git diff --check` is clean. The only added line over 120 characters is the
§A.41 table row, which keeps the table's existing form. The §A.32/§A.33 scan of added lines found no hit. A grep
of the final file finds no other count of fixtures or XC4 wording to update. PR #1215's body does not mention XC4,
fixtures or `availExt`.

## 3. XC4 as amended: PASS

**Faithful to the option text.**
- Per outcome, on outcomes 1–3: yes.
- Comparator `(1/8)·id`: yes.
- All four matrix units: yes.
- Depth ≥ 1: yes, on one attempt and never on the depth-0 stopped channel.
- Fifth pre-F fixture, `(1/8)·Ad(Z) ≠ (1/8)·id`: yes.

XC4 is still one line and one countercontrol, so the summary counts (8 checks, 4 countercontrols) and the exit table
are unchanged.

**Correctly scoped.** `conjugatedAttempt j = Ad(H) ∘ attempt balancedCircuit j ∘ Ad(H)` (frozen surface `:301–302`),
and `correction j` acts as `Z ⊗ 1` on `Token × Fin 4` for `j ≠ 0` (BFP:170). XS already covers every definition that
XC4 computes through. Outcome 0 is excluded for the stated reason: `correction 0 = 1`, and my exact check reproduces
the original defect, with outcome 0 unchanged when the correction is removed.

**Non-vacuous, in both directions.**
- *Exit 0 is now reachable (paper argument only; no O-3a–e object computed).* The partial trace over the ancilla
  commutes with `Ad(Z ⊗ 1)`. So for `j ≠ 0`, the uncorrected branch is `Ad(Z)` composed with the corrected branch.
  On the conjugated attempt, if X3b holds, each uncorrected branch is `(1/8)·Ad(HZH) = (1/8)·Ad(X) ≠ (1/8)·id`, so
  XC4 fails as stated.
- *XC4 can report "not failing".* My check runs the same comparator on the corrected branches of the fixture, which
  are X3b's object, and it reports not failing. So the comparator is not constant. It detects a checker whose
  correction-removal path is a no-op on any of outcomes 1–3. It also detects one that compares the diagonal units
  only: on the unconjugated fixture, those units agree with `(1/8)·id`.

**The quantifier (judgement call 2): "any one equals ⇒ not failing" is correct.**
- The preregistration says countercontrols "must fail as stated". As stated, XC4 fails exactly when for each of
  outcomes 1–3 the uncorrected branch differs from `(1/8)·id`. Its negation, "not failing", is exactly that some
  branch equals `(1/8)·id`. The amended text states both halves, and they are exact negations of each other.
- "All three equal ⇒ not failing" would be the wrong quantifier. It would be strictly weaker: a checker whose
  correction removal silently did nothing on one or two outcomes would still pass XC4. My check shows the contrast
  on a synthetic triple.
- "Each" is right as the quantifier of the fail-as-stated condition, and the text already uses it ("for each of
  outcomes 1–3").

**Fifth fixture, independent exact check.**
- Script: `verify2/fixture5_check.py`, sha256 `bd38aca8197c8755362291618b660bd47d2cef80cfe9e68448c09a6e70498d63`.
- It imports nothing from earlier work. It reconstructs from the BFP and OperationalAssembly text at `D = fd539e15`
  and computes over ℚ(i).
- Results: 20 of 20 pass, exit 0, the same under `-O`.
- Control C0: with the correction kept, the branches reproduce BFP:194 on all four units for outcomes 0–3.
- Control C1: `correction 0 = 1`, and `correction j = Z ⊗ 1` for `j = 1, 2, 3`.
- Fixture: with the correction removed, outcomes 1–3 each equal `(1/8)·Ad(Z)` on all four units. They differ from
  `(1/8)·id` exactly on `E01` and `E10`, so XC4 fails as stated.
- Countercontrols: the comparator on the corrected branches reports not failing; the diagonal units alone cannot
  detect the difference; outcome 0 is unchanged by removing the correction.
- No `hadamard`, `hdh`, O-3a word or conjugated attempt was computed.
- The writer's `xc4_verify.py` (sha256 `260a8b4b…3159`, matching the commit message) reran: 27 expectations, 0
  unexpected.

## 4. availExt: PASS
At `fd539e15`, `OperationalAssembly.lean:599` reads:

```
availExt : ∀ (n : ℕ) (O : Type) [Fintype O] [DecidableEq O], (O → Matrix (A × Fin n) (A × Fin n) ℂ →ₗ[ℂ] …) → Prop
```

`substratumTheory (A) : FiniteOperationalTheory A` (`RouteB.lean:284`). So with `A = Fin 2`, the expression
`(substratumTheory (Fin 2)).availExt n O F` has exactly the binder order and argument types of the theorem's own
`n`, `O` and `F`, and the instances are in scope. The old text passed `F` where `O : Type` is expected, so it could
not elaborate. The proposition is the one intended, and the hypotheses and conclusion are unchanged. I confirm this
as the preregistration's reviewer step (frozen-surface correction, `:205–207`).

## 5. V3 blocks and precondition 7: PASS
- The `v3-round` and `v3-governed-paths` blocks extracted at `aeab48e3` and at `a44c0206` are byte-identical
  (sha256 of the extraction `8efe8727…1c91` at both).
- Precondition 7's exact command, run from the worktree root with `<D> = fd539e15…` and `<candidate F> = a44c0206…`
  (with `-B` added, to keep the worktree clean), printed `MATH-CON-1-S1B-1 non-sealing b'…/round-mathcon1-s1b-1/'
  81897a90a068b0402e68393f82cffda8fd83f0bda5283316c38d8c58b28e5107 []` and exited 0.

## 6. Local checks: PASS
SC-42 integration, following `verify.yml:282–294`:
- normal `--verbose` exits 0 and `-O` exits 0; the two outputs are equal and equal the committed
  `sc42-integration-result.json`;
- `--self-test`, normal and `-O`, exits 0; the two outputs are equal and equal the committed
  `sc42-integration-controls.json`.

`v3_verifier`:
- `--self-test`: OK;
- `--corpus`: 140 vectors, exact and as expected;
- `--receipts a44c0206`: 54 receipts, all hold.

`legacy_records_check a44c0206`: self-test OK; 303 records in 75 closed namespaces, all intact.

## 7. Commit messages: PASS
- The committed messages equal `msg1.txt`, `msg2.txt` and `msg3.txt`, apart from git's trailing newline.
- Each cites #1169 comment 6742682753 with author and time. Each quotes its own sentence of the option text
  verbatim, and commit 2 quotes the full XC4 sentence.
- Each ends with the `Co-Authored-By: Claude Opus 5.5` and `Claude-Session` trailers.
- Commit 1 carries the before/after unified diff and states which restriction it falls under, as `:205–207`
  requires.
- The hunk headers in commit 2's message agree with the actual line positions.
- Each commit carries an SSH signature. It was not verified locally, because no allowed-signers file is set up.

## Judgement calls
1. **"depth ≥ 1" read as one attempt (depth 1).** Accepted. Per-outcome branches exist only within one attempt; the
   stopped channel at depth ≥ 1 sums over outcomes. The reading carries out the option text's intent of excluding
   the vacuous depth-0 identity.
2. **"any one equals ⇒ not failing".** Correct; see §3. "All three" would weaken the countercontrol. "Each" is the
   quantifier of the fail-as-stated side, and the text uses it there.
3. **availExt in its own commit, on the owner's decision.** Correct. An explicit argument is not one of the four
   allowed kinds (`:200–203`), and the owner decision explicitly names this line.
4. **"controls.py or the checker".** Acceptable. Precondition 3 pins both blobs at `F`, so the table is frozen
   whichever file holds it, and the owner asked only for a note on where it lives. *Observation, non-blocking:* staging
   should settle which file holds the table before `F`, so that the review at the exact head can find it.
5. **Fixture 5's expectation from BFP:194 + BFP:170 rather than a kernel theorem.** Accepted. The derivation is
   valid and is confirmed by two independent exact computations, and the text states its basis. *Observation,
   non-blocking:* the fixture preamble says fixtures run on "objects whose results are already proved on `main`".
   Here the object (B23's attempt) is proved, but the correction-removed branch is a one-step consequence rather
   than a kernel statement. The text says so honestly.
6. **No extra self-test mutation cases.** Acceptable as the minimum change. *Observation, non-blocking:* no recorded
   fixture exercises the "not failing" direction of the per-outcome `any`. The existing case "exit 4 (XC1 made to
   pass)" covers exit routing only. A replay of XC4's comparator on the corrected branches (expected: not failing)
   would cover that direction, if the owner wants it.
7. **Commit 2 amended once, locally.** No issue. It is unpushed and unreviewed, the committer time differs from the
   author time as expected, and commit 3's parent is the amended commit.
