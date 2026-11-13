# NOTES-BG-r4: working log for G3 unit 2(b), revision 4

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`, read from a read-only worktree.
  - Head at reading time: `651849ab6e943dc5fd49180a910e23c6003af17e`.
  - `git diff --name-status 27c409a0 651849ab` lists four added files: `G3-UNIT2B-BG-r3.md`,
    `NOTES-BG-r3.md` and `RESPONSE-BG-r2.md` (from `7fd16a5d`), and `CONFIRM-BG-r3.md` (from `651849ab`).
  - The committed r3 files are byte-identical to the writer's r3 (`cmp`). The committed
    `CONFIRM-BG-r3.md` is byte-identical to the copy read (`cmp`).

### Commit state, recorded as observed (CONFIRM-BG-r3 CF-7)

| Revision | Committed at | Committed by |
|---|---|---|
| r1 | `4acb3a49` | the coordinator |
| r2 | `8a3c43e1` | the coordinator |
| r3 | `7fd16a5d` | the coordinator |
| r4 | — | not committed at the time of writing |

- Earlier NOTES files stated that the writer did not commit, push or post. That was accurate when
  written, and it was read later as a statement about the head.
- **The convention from this revision on.** The writer does not commit, push or post. Commits are made
  by the coordinator, and the branch history records them. A NOTES file records only the commit state
  observed when it is written.

**Authority.** #873 c.6865179466, QU5. The coordinator's request for r4 is a session message, not an
owner record.

## 2. Reading log (additions in r4)

| Source | What was used |
|---|---|
| CONFIRM-BG-r3.md | in full |
| GR:573 | "there is a classical microstate difference corresponding to this energy difference"; "An electron at rest vs. no electron" |
| GR:577 | "corresponds to classical microstate differences, is determined by the visible data, and gravitates" |
| GR:374 | "the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume"; "boundary architecture requires some state dependence on cosmological geometry" |
| GR:581 | the full non-sourcing clause, with "on the geometry-first proposal of §6.2 and conditional on its open coupling step" |
| U2Ar3:690–693 | the witness's `R`-dependence is "the same kind of piece that Reading 1 feeds back" |
| U1r5:504–506 | §8.3 within the geometry-first proposal; the epoch-differential caveat |

## 3. Order of work

1. Read CONFIRM-BG-r3 in full and checked the committed files with `cmp`.
2. Assessed CF-1 to CF-4 before editing.
   - **CF-1** is correct. Under r3:220–222, holding the channel as a premise leaves F4-c deciding the
     outcome, so the result is (C) with K3 named, not (B).
   - **A clarification found while applying CF-1.** K3's wording ("without a stated difference … fails
     K3") would fail any specific carve already stated. F4-c is therefore stated as a schema whose
     candidate classes each fail, and whose K3 is undetermined because the candidates are not shown to
     be exhaustive (r4 §1.3). That reading gives the reviewer's "(B) only if no grounded carve-out
     exists".
   - **CF-2** is correct on all three grounds. In particular, my r3 admission of the running channel
     under §8.3 contradicted my own F4-7.
   - **CF-3** is correct: `g_μν k^μ k^ν = 0` on every route.
   - **CF-4** is correct.
3. Created r4 from r3 by scripted exact-string replacements. Each replacement had to match exactly once
   in the file.
4. Re-applied the rule. The outcome is (C), unchanged. The consequence of QB7(a) is restated as (C) with
   K3 named.

## 4. Decisions

1. **No CF is disputed.** RESPONSE-BG-r3 gives each disposition.
2. **The rule's clauses are unchanged at r4.** R-6 records r3's unrecorded edits. R-7 lists F4-c, which
   r3 already counted.
3. **The §8.3 branch is stated as undetermined**, leaning to exclusion for the running channel. The
   witness is excluded under F4 in either branch.
4. **No premise adopted, no manuscript change, no Lean build, no claim about Λ.**

## 5. Checks

- No computation, script or build was run apart from the three permitted checks.
- **The r3→r4 diff.** `diff G3-UNIT2B-BG-r3.md G3-UNIT2B-BG-r4.md` gives 37 hunks. r4 has 889 lines, of
  which 697 are unchanged from r3. RESPONSE-BG-r3 §3 maps the hunks.
- **Barred-string scan of the three r4 files.** It found no forbidden path prefix and none of the
  §A.32/§A.33 phrase families.

| Check (worktree at `651849ab`, `PYTHONDONTWRITEBYTECODE=1`) | Result |
|---|---|
| `tools/claims_check.py` | exit 0: "OK (no withdrawn result asserted unconditionally)" |
| `tools/staleness_check.py` | exit 0: "OK (13 matched, 0 unstamped)" |
| `tools/voice_check.py` | exit 0: "OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)" |

None of these scans the drafts. The worktree stayed clean (`git status --short` empty before and after).

## 6. Off-`main` references (§A.42 item 8)

These are as in NOTES-BG-r3 §7, with the following additions:

| Reference | Claim it is attached to | Class |
|---|---|---|
| `CONFIRM-BG-r3.md` at `651849ab` (branch) | the findings r4 answers | support off `main`; lands with #1275 |
| `G3-UNIT2B-BG-r3.md` at `7fd16a5d` (branch) | the statements r4 withdraws or restates | support off `main`; lands with #1275 |

## 7. Limits

- By hand. Scoped to Reading G, case β, and conditional on N5-G.
- F4 and F5 are readings [P].
- The rule was repaired at r2 and r3 after reviews that named the expected outcome.
- The §A.31 fixed point is not reached.
