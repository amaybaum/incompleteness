# Independent preparation review: Q-C2-1 r14a (ARP-2-QC21)

**Verdict: REVISE (minor).** There is one blocker: the port of Q-C2-2's R13-B4 fix is incomplete, so the `E` entry
check cannot be implemented as frozen. There is a set of nits, most of them labelling gaps for R1–R8. R14-B1, R14-B2
and N1–N21 are otherwise fixed or soundly disposed of. No owner decision needs to be reopened.

**Authority.** #1169 c.6740078002 (amaybaum, OWNER, 2026-11-09T12:29:10Z) authorizes "r14, bringing the scripts up to
date, ordinary non-scientific self-tests, and independent preparation review". It does not authorize the design run,
the gate tests, `F` or dispatch, or any scientific computation.

What this review did and did not do:
- It ran no LP, no stress test, no script self-test and no computation on a round instance.
- It made no repo, git or GitHub writes.
- It changed no Q-C2-2 file.
- Its only writes are this file and `review/probes-r14a/`.

## Inputs (verified)

| file | sha256 | check |
| --- | --- | --- |
| r14a `preregistration.draft.md` | `1dd595d30eafb65dce341b1c6306ef85b4876ce008f5e45639f893247daad708` | matches the brief |
| r14 `r14/preregistration.draft.md` | `ae6f0e26e3eefc5060dddd8b7fc8a3a4958f689cf99bcc699c18821225b477fd` | matches |
| `DISPOSITIONS-r14a.md` | `680f13419d3d07c110fa18235424cfcf10cb841927bd64e527aba4bcfabc5e2b` | matches |
| `IMPL-DELTA-r14a.md` | `cb9f0c4ea7d99d698f9885f067e7e6b39064138b8642d176d05743284d95c0f5` | matches |
| `review/REVIEW-QC21-r14.md` | `e11f466836eb0e92d7a5f7a99753d61b63082fcd51267cc75b883f8ae192d1e6` | matches |
| `../qc22/preregistration.draft.md` (Q-C2-2 r14) | `9e3ef0c9ddea2876d86bb097e68dc5939487a5a7625333a26167469044c641ba` | matches |
| `wt-impl` `qc21_check.py` / `controls.py` at `d87547a4a` | `1f928334…` / `ce343d6f…` | match IMPL-DELTA |

**The build reproduces.**
- `r14awork/make_r14a.py`, with its output redirected, applies 90 edits to r14.
- Its output is byte-identical to r14a (`probes-r14a/rebuild-r14a.md`, `1dd595d3…`).
- `r14awork/r14-r14a.diff` matches a freshly generated diff apart from its header (`probes-r14a/r14-r14a.fresh.diff`).

**The V3 blocks are unchanged.** The `v3-round` and `v3-governed-paths` blocks are byte-identical in r13a, r14 and
r14a (`probes-r14a/v3_blocks.out`).

**Edit-log rows.** For rows 73, 82 and 86–98, each row's copied-text fragments occur in r14, and each "becomes"
fragment occurs in r14a (`probes-r14a/editlog_rows_r14a.out`). There are two expected exceptions:
- row 73's old cell is r13a's copied text;
- row 93's "C-INDEP:" is a label.

## Blocker

**R14A-B1. R13-B4 is only partly ported: as frozen, `verdict` has no way to read the `E` approval comment.**

**What C.8 item 9 now requires.** `verdict` builds the `E` dispatch's own entry "from the `E` approval comment's id,
given as an argument". It then verifies that entry "as C.3 states". C.3's checks need the comment's
- author and author association,
- `created_at` and `updated_at`,
- quoted words.

R8's draft default adds a second read: `verdict` must read the owner's ratification comment and check that it quotes
the entry's sha256.

**Why that cannot be implemented.** Rule (g)'s frozen `gh` templates (C.5, lines 2728–2738) contain no comment
endpoint, and `GH_TEMPLATES` (`controls.py` line 90) has none either. Under control B, `verdict` can read neither
comment. Q-C2-2 r14 closes the same gap in two places:
- the template `issues/comments/{DEC}` (R13-B4; its line 1113);
- the `verdict` condition "every approval entry holds, the `E` dispatch's included" (its line 1644).

r14a has neither. Its C.3 condition list (lines 2410–2423) never states what happens when `E`'s entry fails its checks.

**IMPL-DELTA.** D20 omits the template.

**Fix.**
- Add `issues/comments/{DEC}` to rule (g)'s templates as an edit row, using Q-C2-2's wording.
- Add the `verdict` condition, also as an edit row.
- Under R8's default, read the ratification comment through the same template.
- Update D20.

## Nits (one line each)

- **N1 (R8 sites).** Seven sites still say that the designation of `E` ratifies "every approval entry": 1385, 1420,
  1474, 1489, the PENDING owner commitment at 1494, 2296 and 2414. C.8 item 9 says it cannot cover `E`'s entry. Restate
  them as "every entry in `approvals.json`; `E`'s entry per R8", and label them.
- **N2 (other unlabelled default sites).**
  - R2: C.6 at 2844 ("at `E`, a red fixture-mode control"). The default is also implicit in C.6's S1 checker-outcome
    line and in `verdict`'s "every step of job A is `success`".
  - R1: invariant row 1557 states "at least `10^5`" without the label.
  - R3 and R5: adaptation row 1861.
  - R6: C.3 at 2421–2422 ("A missing or unreadable artifact fails it").
- **N3 (R8 framing).** C.8 item 9 and R8 say "the designation of `E` precedes that entry".
  - Under §A.39, `E` is designated after its exact-head run, which here is the approved `E` dispatch. The designation
    could therefore quote the entry's sha256. What precedes the entry is `order.json` in `E`'s tree.
  - Narrow the sentence, and offer the designation itself as an R8 option.
  - Also name the mode that builds the entry before `verdict`'s capture. The default has the executor post it first.
- **N4 (R1 boundary).** The default requires `S_max ≥ 10^5`, and after a red design run it allows only a smaller
  `S_max`. A red design run at `S_max = 10^5` therefore leaves no admissible value. State this in R1. R1 also states no
  alternative, only a default form and a missing value.
- **N5 (R4 and R5).** R4's alternative presupposes R3's alternative. R5's alternative does not say which budget the
  other B fragments take, or how it changes the `1203 · W_max` term.
- **N6 (control P coverage, residue).**
  - The DSN (`DESIGN-DS.md`) blob must be filled before `F`, but it carries no PENDING marker (Inputs row DSN at 654;
    precondition 3), so control P cannot catch its omission. This is pre-existing.
  - Precondition 2's D18 and D14 review items are unmarked, while the sketch-review item is marked. Make the three
    consistent.
- **N7 (cap values).** `check --freeze` now compares `S_max` in the file, in the checker and in `stress.json`. B-P's cap
  values as written in C.8 item 1 and D19 (i)(a) are still not compared with the checker (the second half of R14-B1).
  Either parse them, or state that the checker's constants govern.
- **N8 (sketch-review item).**
  - In content it is met: the quotes in *Proof reviews* match `review/proofs/REVIEW-LEMMA-P.md` (`07170453…`) and
    `REVIEW-CONE.md` (`07bc8fd7…`), apart from bold markers, and both sha256s verify.
  - But both review files exist only in session-local working files, and CC-NAT's gating rests on Lemma P's verdict. §A.42 items 2
    and 8 therefore need both files on `main` before the item is discharged, either with precondition 3's paper records
    or in the record directory. That is the coordinator's and owner's call.
- **N9 (status bullet).** Line 6 calls R1–R8 "owner-reserved choices that r14 made". R8, R3's SF-2 part and R7 are new
  defaults where r14 was silent.
- **N10 (typography).**
  - Line 63 is 130 characters long.
  - The wrap breaks at 3167–3168 ("M-RAY (row 76): in B-RAY's").
- **N11 (wording).** Row 82 and the template list say `derive-run` reads the archive "at `E`". C.8 item 3 says
  `derive-run` is "run on S1's run before `E` is committed". Use one wording.
- **N12 (provenance).** The QC22 Inputs row (652) cites r13 (`15d90b24…`) only. Rows 92–98 take their wording from
  Q-C2-2 r14 (`9e3ef0c9…`); cite it as provenance.
- **N13 (UPR-BC).** DISPOSITIONS §7 flags UPR-BC with an `out_of_scope` completion as an owner scope question. The file
  does not mention it. Either add it as a ruling (R9), or record the current rule as frozen behaviour: no label, and the
  completion's status printed.

**IMPL-DELTA Part D** (read-only, against `wt-impl` `d87547a4a`):
- **I1 (B1).** D20 omits adding `issues/comments/{DEC}` to `GH_TEMPLATES`.
- **I2 (D16).**
  - Lines 3316–3342 are in `fixture_section`, not `assemble_decisive`.
  - State what is missing:
    - `s_decide_effect_facet` discards its certificate (`verdict, _ = s_step4(…)`);
    - it uses a fresh `Budget()`;
    - no verifier exists with the roles exchanged.
- **I3 (D2).** The `C-CERT` in `b_red` at 3201 is the fixture section's (`fx["controls"]`). The decisive-mode C-CERT
  over B-P and the reported-only fragments does not yet exist; say so.
- **I4 (D17).** By AST count, `qc21_check.py` has 38 `set`/`frozenset` calls, 4 set displays and 6 set comprehensions,
  not "26 `set(` calls" (`probes-r14a/script_facts.out`). This is the same in DISPOSITIONS §3.
- **I5 (pre-existing).** `controls.py` `INPUTS` (52–66) lacks QA, FB, M2D, MI-R, SUB, RCH and DSN, and skips
  `tools/v3_verifier.py` (`None`). DS therefore does not re-check rows that the file says it re-checks.

These Part D items were confirmed against the scripts:
- **D1.** `pending_unbackticked` is at 1433–1440.
- **D3.** The token line is already `"%s %s %s level %s"` (1772). It prints `None`, not `none`.
- **D5.** No `ada_*` functions exist yet.
- **D6.** The line references are right.
- **D7.** The defect is real: `upload()` names both A4 and A6 `arp2-qc21-output`, and B5 `arp2-qc21-measurements`.
- **D9.** `evidence/s1-run/results.json` is already in `E_FILES`.
- **D18.** The `JoinedStr` handling is at 429–438.
- **D19.** The line references are right.

## Scope item 1: R14-B1, R14-B2 and N1–N21

**R14-B1. Fixed.**
- **Control P's rule** was re-run on r14a with the review's text probe (`probes-r14a/control_p_coverage_r14a.out`). It
  now catches 31 of the 40 lines that carry the word. Among them:
  - every r14 placeholder: `S_max`, B-P's three caps and their triple, the D19 (i)(a) values, C.7's lines, the stress
    pin, the design-run and gate-test pins;
  - the inherited placeholders: the sketch review, the owner commitments, `T0`, RCH, the digest date, the anchors and
    the activity retention;
  - R1–R8.
- **The 9 lines it skips** only name the word: status lines 6 and 11, discipline 55–56, SG-2 552, invariant 1555,
  precondition 6, C.2 2271 and C.5 2791.
- **The 2198/2789 contradiction is resolved.** C.2 (2271) and C.7 (2875) now agree.
- **What remains:** N6 (DSN pin, D18/D14 items) and N7 (cap values).

**The new `check --freeze` rule for `S_max`. Sound.**
- The single line `- **`S_max`** = PENDING` (2969) is caught by control P.
- `check --freeze` then requires:
  - the line occurs exactly once;
  - its value is a decimal integer `≥ 10^5`;
  - the value equals the checker's `S_MAX` (read by AST from the pinned blob) and the single `S_max` in the pinned
    `stress.json`.
- SG-2 (551–556), the invariant row (1557) and IMPL D1, with its self-test cases, agree with it.
- `≥ 10^5` is R1's draft default (N2, N4).

**R14-B2. Fixed, with labelling gaps.**
- R1–R8 are unbackticked PENDING items of precondition 2 (1595–1629), each with a draft default and an alternative
  (R1 has none; N4).
- Control P and precondition 6 block `F` on any of them.
- The invariant row (1555) names them.
- Labels are missing at some sites: N1, N2.

**Nits N1–N21.**
- **Correct:** N1, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, N13, N14, N15, N16, N17, N18, N19 and N20.
- **N4 checked exactly.** B-RAY-F's expectations hold: 5 distinct rows, `d = 3`, `r_S = 4`, the mixture in the cone,
  each point-law row extreme, `m = 4` and `T = 3`. They hold with the mixture on an edge or on the diagonal
  (`probes-r14a/bray_f.out`). The *Models cover removed rows* reading is right: `μ_p(j) = (g_j · a_p) s_j` is linear,
  and `g_j · a_p ≥ 0` for a removed row in `cone(R)`.
- **N13 checked against r13a.** Its D21 options section lists "a crash or a timeout" under "Under either option the
  round halts on". So the relabelling, without a PENDING marker, is right.
- **N21** is process only. It still applies: nothing is pushed and no guiding PR exists (§A.43 items 1–2). Inspect
  the push-triggered workflows before any push. `wt-impl` changes no `.github` file.

## Scope item 2: the six fixes found via Q-C2-2 r14

| item | finding |
| --- | --- |
| **"the sum covers both"** (R13-N8) | Correct, and it agrees with Q-C2-2 401: job B's bound is `σ(W^BP + 1203 W + W_fix)`; job A's is `σ(2W_fix + W_stress) + t_810`; each is at most the left side; the sum, with `3·W_fix`, is not what the test bounds |
| **C-SYM** (R13-N10) | Byte-identical to Q-C2-2's row 570 apart from the provenance tag. The algebra checks: transposing `Σ h_k κ′_kᵀ = I_d` gives `a_p · b_e = Σ_k (κ′_k · a_p)(h_k · b_e)`, so the model reproduces `N`; `h_k · b_u > 0` and `ξ ≤ 1` hold when the complements and unit are present (as the row says); the Farkas soundness is `tr W = Σ y_{kp} κ′_k · a_p ≥ 0`. Counting C-SYM in `W_fix` and the maxima raises `W_max`, and so the `1203 · W_max` term (R3, R4) |
| **rule (e) vs (g)** (R13-N6) | The row 98 wording and the M-GUARD variant (row 95) match Q-C2-2 1074 and 678. `controls.py` already implements the rule (429–438) |
| **no sets** (R13-N17) | The wording matches Q-C2-2 935–937 and 1022, and `set` is removed from C-INDEP's whitelist as in Q-C2-2 566. The invariant row is real |
| **synthetic merges** (R13-N9) | Matches Q-C2-2 1468–1473, apart from the record name. The C.7 check list and the invariant row are added. The tree argument is right: the base is an ancestor of the head, so the merge tree equals the head's tree |
| **`approvals.json` and `E`'s entry** (R13-B4) | The "Where the entries are" wording matches Q-C2-2 1485–1488. The template and the `verdict` condition are missing (**R14A-B1**). R8, the new ruling for the authorship of `E`'s entry, is a legitimate owner question, because Q-C2-1 has no Environment review. Its premise is too strong (N3) |

## Scope item 3: the partial dispositions

- **N2's alternative route. Accept.** Under the copied M-SOLVER, `unverified` must stay a count of failed certificates.
  Moving the red condition instead has the same effect: a failed reported-only certificate cannot turn a B control
  red. A failed fixture certificate still exits 3 in fixture mode. In decisive mode, C-CERT becomes an
  implementation-invariant check, as C-BUDGET is. A failed B-P certificate gives B-VOID through `decide-b`, not through
  C-CERT.
- **The sketch-review item in precondition 2.** It is met in substance: the verdicts are quoted verbatim apart from
  emphasis, and both sha256s match. It should be discharged only once the two review files have a home on `main`
  (N8). Until then, keeping it PENDING is correct.

## Scope item 4: owner rulings R1–R8

- **PENDING and blocking `F`.** All eight are unbackticked PENDING (1595, 1600, 1603, 1609, 1613, 1615, 1619 and
  1624). Control P and precondition 6 block `F` on each.
- **Labels.** Not all labelled (N1, N2).
- **No other owner choice is unmarked,** except UPR-BC (N13). The crash and timeout halts were adopted with D21 (N13).

**One-line descriptions for the owner's decision sheet.**

- **R1, `S_max`.**
  - Default: the owner fixes a maximum number of `(d − 1)`-subsets per facet enumeration, in the solver and again in
    the verifier. It is at least `10^5`, time is capped by the 1200 s test and the 60-minute job, and only a smaller
    value is allowed after a red design run.
  - A larger value lets ST-BP raise B-P's caps further, but lengthens A5 and so risks a red design run.
  - A value of exactly `10^5` cannot raise the binomial cap, and if that design run is red no admissible value remains
    (N4).
  - The file states no alternative to the form.
- **R2, a red fixture-mode control at S1 or `E`.**
  - Default: the round halts and every result is void, read as a reproducibility failure.
  - Alternative: only the tokens in that control's `for` column are void, and the other tokens stand. This needs
    edits to C.1's fixture exit rule, C.6's checker-outcome and halt lines, and `verdict`'s job-A condition.
- **R3, reported-only volume in the timeout test.**
  - Default: all 1203 reported-only fragments are charged at `W_max`, and SF-2 is decided uncapped and enters the
    general maxima. A failed test means `F` is not requested.
  - Alternative: an aggregate work budget for reported-only fragments, beyond which they are recorded `out_of_scope`.
    This makes the test easier to pass, but some B-C results become `out_of_scope` (a scope change).
- **R4, priority between B-P's caps and the reported-only volume.**
  - Default: the reported-only term counts when the reference is chosen. It can lower B-P's caps or leave the copied
    caps, which raises the chance of B-VOID.
  - Alternative: B-P's reference is chosen first. This requires R3's alternative to bound the reported-only work.
- **R5, which fragments the raised caps cover.**
  - Default: B-P only. The other B fragments use the general caps, and more of them may be `out_of_scope`.
  - Alternative: every B fragment gets the raised caps. More reported-only fragments are decided, at greater timeout
    exposure, and the budget and timeout term are unspecified (N5).
- **R6, the S1 artifact expired at `verdict`'s capture.**
  - Default: the binding fails and the round is void, so `verdict` at `E` must fall within 90 days of S1.
  - Alternative: the binding is reported as not checkable, and the tokens stand with the limitation printed. The
    committed measurements are then bound only by B6's replay at `E`.
- **R7, a REP-INV alternative whose B table differs beyond relabelling.**
  - Default: it is not re-decided. It is read as a change, so the identification is reclassified as imported. This is
    conservative and adds no LP time.
  - Alternative: it is re-decided under its role's caps and counted in the timeout test. A native classification can
    then survive, at the cost of added job-B time and a possibly lower B-P reference under R4's default.
- **R8, authorship of `E`'s own approval entry.**
  - Default: after the `E` run, the owner posts a comment quoting the entry's canonical sha256, and `verdict` is VOID
    without it. That is one extra owner act, and it needs the comment-read template (R14A-B1).
  - Alternative: some other recorded owner act before the capture. One concrete form is the designation of `E` quoting
    the entry's sha256 alongside `order.json`'s (N3).

## Scope item 5: a re-read for new errors

New errors are R14A-B1 and N1, N3, N9, N10 and N11. Otherwise the added text is consistent:
- The token line, C.8 item 14 and rows 89–90 agree.
- The B-RAY-F row matches C.8 item 15.
- SG-2 and SG-3, the invariant rows and D21's list use "incomplete-output halt" consistently.
- The added text is in a neutral register.

## Scope item 7: authorization

Nothing in r14a implies authorization of the design run, the gate tests, `F` or computation:
- lines 357–366 and precondition 7 say so;
- N10's guards (`--stress` exits 4 while `S_MAX` is unset; no splice-bearing push before the design run is
  authorized) lean the same way.

## Probes (`review/probes-r14a/`)

All probes are generic or text-only.

| file | sha256 | what |
| --- | --- | --- |
| `make_r14a_redirected.py` → `rebuild-r14a.md` | `e4b6d407…` → `1dd595d3…` | the build, redirected; byte-identical to r14a |
| `r14-r14a.fresh.diff` | `302cfa27…` | fresh diff; equal to `r14awork/r14-r14a.diff` apart from its header |
| `v3_blocks.py` / `.out` | `6b6e4f39…` / `18e1d167…` | the V3 blocks are unchanged (r13a, r14, r14a) |
| `control_p_coverage.py` / `control_p_coverage_r14a.out` | `fc3f8b2f…` / `5b0eccb8…` | control P's rule on r14a: 31 of 40 lines caught |
| `editlog_rows_r14a.py` / `.out` | `328f6264…` / `0fa18fdd…` | rows 73, 82 and 86–98 located |
| `bray_f.py` / `.out` | `a004c557…` / `9c963d65…` | B-RAY-F exact checks (generic fixture; exact 3×3 solves, no LP) |
| `script_facts.py` / `.out` | `199e503c…` / `0c4b72b1…` | AST and text facts about `wt-impl`: set counts, templates, `upload()` names, `INPUTS`; Q-C2-2's template and `verdict` line |
