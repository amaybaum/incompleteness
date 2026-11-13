# NOTES-BG-r2: working log for G3 unit 2(b), revision 2

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`, read from a read-only worktree whose head was
  `1970a36aee2e86b10ea492e0515ade732cb9a02d`.
  - `git diff --name-status 3945940c 1970a36a` lists five added files: `G3-UNIT1-CORR-r2.md` and
    `RESPONSE-CORR-r1.md` (from `d4fe24be`), `G3-UNIT2B-BG-r1.md` and `NOTES-BG-r1.md` (from `4acb3a49`),
    and `REVIEW-BG-r1.md` (from `1970a36a`). Each is accounted for by the branch history.
  - The committed `G3-UNIT2B-BG-r1.md` and `NOTES-BG-r1.md` are byte-identical to the writer's r1
    (`cmp`). The committed `REVIEW-BG-r1.md` is byte-identical to the copy supplied for review (`cmp`).
- **Files.**
  - r1 (`G3-UNIT2B-BG-r1.md`, `NOTES-BG-r1.md`) was written in the working area by the writer and
    committed to the branch at `4acb3a49` by the coordinator. NOTES-BG-r1 §1 says the writer did not
    commit, push or post them, which was true when it was written and is inaccurate at the head
    (REVIEW-BG-r1 BG-7). r1 is not edited.
  - r2 (`G3-UNIT2B-BG-r2.md`, this file and `RESPONSE-BG-r1.md`) was written in the working area. The
    writer did not commit, push or post it.
- **Authority.** #873 c.6865179466 (`amaybaum`, 2026-11-13T21:19:37Z), QU5. The coordinator's request
  for r2 is a session message, not an owner record.

## 2. Reading log (additions in r2)

| Source | What was used |
|---|---|
| REVIEW-BG-r1.md | in full |
| G3-UNIT1-CORR-r2.md | lines 1–60 and every line containing "B_G" (row 2; X-1 to X-12) |
| GR:384 | "The total gravitating boundary energy tracks the critical density at every `H` as an identity, not a prediction." |
| GR:422–426 | `ρ_s = E_s/V_H = ρ_crit`, "a consequence of Jacobson's Clausius relation applied to the de Sitter horizon" |
| GR:462–482 | §7.3; Step 3, "The Jacobson mechanism converts the entropy gradient into curvature" |
| GR:695 | the Newtonian field from holographic equipartition with the classical horizon temperature |
| U1r5:158, :198–204, :352–355, :419–421, :589–606, :671 | W1-0; class 𝒞_div; K_cpl^free on shell; B1; R2a; F9 |
| U2Ar3:524–527, :535–536, :548–549 | Attempt 1; "That is G3"; "directly" |

**Search (§A.19).** I grepped GR.md at `c3b5f37a` for "gravitating" and for the §7.3 steps, to test F4
against the corpus's own partition-defined gravitational quantities (K3). Hits used: GR:384, GR:482 and
GR:695. GR:424's "grounds it in the Clausius relation" uses "grounds" in the sense of justification, and
I did not use it.

## 3. Order of work

1. Read REVIEW-BG-r1 in full and checked the committed files with `cmp`.
2. Assessed BG-1 before writing anything.
   - Item 1 (the rule is asymmetric) is correct. Given the premise base, Lemma U holds at every OI
     world, so r1's clause (A) could not be met by any per-world formalization.
   - Items 2, 3 and 5 are correct.
   - Item 4 (F4) is correct as a missing formalization. I pressure-tested it before accepting.
3. Repaired the rule (§1.6 of r2, R-1 to R-3). The repairs were written after the review named the
   outcome it expected. They are stated as repairs. The repaired rule decides by which kinds of
   formalization remain admissible, and it can return (A).
4. Added F4. Tested it depth-first as the branch favourable to decoupling: nodes F4-1 (presentation),
   F4-2 (feedback), F4-3 (relata), F4-4 (import), F4-5 (the corpus's partition-defined "gravitating"
   quantities) and F4-6 (the Jacobson route). Then tested CoC (C-1 to C-4) and re-evaluated r1's nodes.
5. Applied the repaired rule. Outcome (C).
6. Rewrote §0, §2.4, §4, §5, §7, §8, §9 and §11, and wrote RESPONSE-BG-r1.

## 4. Decisions

1. **BG-1 is accepted in full.** r1's (B) is withdrawn. The rule's defect is stated as a defect (r2
   §1.6 R-1).
2. **F4 is stated invariantly** (energy content, not the right-hand side; r2 §3.4). Otherwise it would
   classify a presentation.
3. **F4's exclusion carries three conditions found in testing:**
   - synchronic or whole-history relata (F4-3);
   - a divergence-free sourcing law (F4-6);
   - the classification of the corpus's partition-defined quantities as non-source (F4-5).

   These narrow the review's statement "Under F4 … excluded". They do not reverse it.
4. **BG-3 is applied** as an amendment to the excluded list (R-2). F3 rests on P-D alone.
5. **The consequences are conditional on the gap.** Forward notes are held (QB2).
6. **No premise adopted, no manuscript change, no Lean build, no claim about Λ.**

## 5. Checks

- No computation, script or build was run apart from the three permitted checks.
- **The r1→r2 diff.** `diff G3-UNIT2B-BG-r1.md G3-UNIT2B-BG-r2.md` gives 56 hunks. r2 has 701 lines, of
  which 179 are unchanged from r1. RESPONSE-BG-r1 §3 maps the hunks.
- **Barred-string scan of the three r2 files.** It found no forbidden path prefix and none of the
  §A.32/§A.33 phrase families.

| Check (worktree at `1970a36a`, `PYTHONDONTWRITEBYTECODE=1`) | Result |
|---|---|
| `tools/claims_check.py` | "OK (no withdrawn result asserted unconditionally)" |
| `tools/staleness_check.py` | "OK (13 matched, 0 unstamped)" |
| `tools/voice_check.py` | "OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)" |

None of these scans the drafts. The worktree stayed clean (`git status --short` empty before and after).

## 6. Off-`main` references (§A.42 item 8)

These are as in NOTES-BG-r1 §7, with the following additions:

| Reference | Claim it is attached to | Class |
|---|---|---|
| `REVIEW-BG-r1.md` at `1970a36a` (branch) | the findings r2 answers | support off `main`; lands with #1275 |
| `G3-UNIT1-CORR-r2.md` at `d4fe24be` (branch) | r2 §8.4 | support off `main`; lands with #1275 |
| `G3-UNIT2B-BG-r1.md` at `4acb3a49` (branch) | the withdrawn outcome; Lemma U and Corollary E as first stated | support off `main`; lands with #1275 |

## 7. Limits

- By hand. Scoped to Reading G, case β, and conditional on N5-G.
- F4 and CoC are readings [P].
- The rule was repaired after a review that named its expected outcome.
- The §A.31 fixed point is not reached.
