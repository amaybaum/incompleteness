# Review: ARP-3 (Q-C2-2) preregistration r14a, an independent review

**Standing.** WIP / UNVERIFIED review note. Model-written. Read-only.
- **Authorization.** #1169 c.6740747027 (amaybaum, 2026-11-09T13:04:10Z), as the coordinator applies it to this
  review: "Fix B1–B6 and the nits, reusing Q-C2-1's repaired wording, then run a further independent review.
  Paper-only. No F, design run, gate tests or Environment changes. Q-C2-2 stays behind Q-C2-1."
- **What was not done.**
  - No repository, git or GitHub write. Two owner comments (c.6740593434, c.6740747027) were read through the API.
  - No LP or simplex was run on any object, the round's fixtures included. No script self-test was run.
  - No computation was made on F1, `G_SM` or any OI construction.
  - Q-C2-1's files were read only. Its draft's sha256 is unchanged.
- **Probes.** The probes in `review/probes-r14a/` are text checks, plus exact ranks, counts and certificate
  identities on generic synthetic fixtures (§7).

## Objects (hashes verified)

| object | sha256 |
| --- | --- |
| `preregistration.draft.md` r14a | `d751a127582748093491da416cfb024ac8db319f72b8f3206334abe7d35447ae` ✓ |
| `r14/preregistration.draft.md` | `9e3ef0c9ddea2876d86bb097e68dc5939487a5a7625333a26167469044c641ba` ✓ |
| `ACCESS.md` r14a / `r14/ACCESS.md` | `8fb9016e…6b0b` ✓ / `e45339ba…e157` ✓ |
| `DISPOSITIONS-r14a.md` | `595dd2c8…1338` ✓ |
| `IMPL-DELTA-r14a.md` | `76a21032…0418` ✓ |
| `DECISIONS-QC22-preF.md` (r14a) | `545ce34c…f571` ✓ |
| `review/REVIEW-QC22-r14.md` | `d344e277…92b3` ✓ |
| `r14awork/make_r14a.py` | `8208d4cb86e959d8bcc5021398de6efe66794e8dd611338c5e71287921ee1d81` |
| Q-C2-1 `preregistration.draft.md` r14b | `57053e08a18f3357b86ea3956e88bbb1fb7a34c1d14fbd6b169ebbff8d1b65e1` ✓ (read only) |

**Reproduction.**
- `python3 -I r14awork/make_r14a.py r14/preregistration.draft.md <out> r14/ACCESS.md <out>` applies 78 + 4 edits.
- Both outputs are byte-identical to the installed r14a files (`cmp`).
- The script only applies exact, counted replacements; it reads and writes nothing else.

**V3 blocks.** The `v3-round` and `v3-governed-paths` blocks are byte-identical in r14 and r14a (`p01`). The
governed-paths digest is therefore unchanged.

## Verdict: **REVISE** (one blocker, cheap)

- **Rb1–Rb3 are fixed.** Each fix compares the right object (§1).
  - **Rb1.** My own construction reproduces every count, all four removal certificates and the effect-side identities
    exactly (`p03`).
  - **Rb2.** The per-reference table is sound. The six narrowings each remove the off-`main` content from the
    claim.
  - **Rb3.** The three new `PENDING` items are well formed and block `F`.
- **The nits N1–N11 and the §3/§5 points are applied.** Small residuals are noted in §2.
- **The fourth new `PENDING` item is legitimate and correctly placed.** One of its options is worded so that it
  would not close the gap it names (N3).
- **One blocker found on the full re-read (Rc1).** It was pre-existing in r14, and it survives the N10 fix. The
  frozen no-unapproved-F1 rule makes any recorded-branch run whose A3 leaves no fixture output a violation. That
  includes an A3 timeout, which precondition 6 explicitly provides for as "revise before `F`", and any pre-A3
  infrastructure failure on the round PR's own S1 or `E` push. Either one voids the round after `F`, with no
  retake.
- **Unchanged.** The mathematics, the decision rule, the tokens and the frozen expectations. The S4 screen of the
  printed sections is clean (`p05`).

## Blocker

**Rc1. An A3 that leaves no fixture output voids the round, including in a case the text itself provides for.**
- **The rule** (lines 1727–1739). For every non-dispatch checker-bearing attempt at a recorded-branch commit,
  A3b must be `success`. "A non-dispatch checker-bearing attempt at a recorded-branch commit whose A3b is not
  `success`, because A3's output is missing or not fixture mode, is therefore a violation." A violation is VOID
  (rule (d), 1697–1707).
- **What `always()` does and does not fix.** With `if: ${{ always() }}` (1359), a red A3 with complete fixture
  output is no longer a violation, so N10's case is fixed. But the rule still voids the round in these cases:
  - **an A3 timeout or crash.** The output is then empty or partial, so A3b is `failure` (or `cancelled`);
  - **a failure before A3.** If checkout, `setup-python` or the runner fails, A3 is `skipped`, and A3b runs on a
    missing file and fails. A job that never starts has no A3b at all.
- **Where this bites.**
  - **Precondition 6 (2083–2085)** says: "If such a fixture is undecided within the job timeout … the fixture set
    is revised before `F`". The design run uses no budget (588), so an undecided fixture *is* an A3 timeout.
    - The design branch is a recorded branch, and its runs postdate `T0`.
    - So that design run is a violation, found at `check --stage S1`'s capture after `F`, and the round is VOID.
    - The text prescribes revision for a case that its own rule turns into a VOID.
  - **The round PR's `pull_request` runs at S1's and `E`'s pushes** (226), and 6′. A transient `setup-python` or
    runner failure there is a VOID of the round. 6′'s "must be green on every step" implies a repeat after such a
    failure, but the failed attempt stays a violation (rule (c) excuses attempts `≥ 2` only for (a)/(b) entries).
- **Why it matters.** The failure is fail-closed, so no wrong token can result. But the risk per run is not
  negligible, the loss is irreversible after `F`, and one of its triggers is a contingency the text explicitly
  plans for.
- **Fix (cheap; any one of these, plus the precondition 6 sentence).**
  - **(a) Exempt an A3 that never started.** The rule holds when job B and B4 are absent or `skipped`, and either A3
    is absent or `skipped` or A3b is `success`. `order.json` already records `A3_conclusion`.
    - This is safe on the frozen splice: if A3 is skipped, every later step with a default `if:` is skipped too,
      A11 included, so no checker process runs in job A.
    - Then state the remaining case, an A3 that started and left no fixture output, as a named residual. Back it
      with a frozen executor precondition (§A.41): no push to a recorded branch unless A3's command, run locally on
      that tree, completes with fixture-mode output.
  - **(b) Rely on the pinned checker at pinned trees.** At commits whose tree carries the pinned blob and the frozen
    splice (control W), A3's literal `--event fixture` and the builder's own refusal already exclude F1, so an
    incomplete A3 there cannot have computed it. Restrict the A3b requirement to other trees.
  - **In either case, correct precondition 6's "undecided within the job timeout" clause.** Either a design-run A3
    timeout is a violation (so the fixtures' run time is established locally first), or the rule exempts it.
- **The same trap is in Q-C2-1.** Its C.8 item 7 has no `always()` at all (DISPOSITIONS-r14a §7). Noted, not
  changed.

## 1. The r14 blockers

| r14 finding | fixed? | what was checked |
| --- | --- | --- |
| **Rb1** caps, completions, C-SYM | ✓ | **Construction frozen** (619–627): F1's formulas per preparation, `η` = the other coordinates, equal laws once, H3 from block B, SW on its carrier. Built independently from the text in `p03`. Every count in *Every frozen fragment is within the caps* (503–531) holds: largest listed `n` 13 outside GX+R-Y, largest `d` 10, largest effect count 27 (GX+RG), largest listed `C(n, d − 1)` 1,716. **GX+R-Y:** 18 rows, `d = 10`. The four certificates `¾·(δ_0 ⊗ U_{Y±}) + ¼·(δ_1 ⊗ U_{Y±})` and their reverses are exact on all 25 columns of `N`. The four endpoints are extreme by the support test (no other listed law's support is inside theirs), so `n ≤ 14`. The bound `C(14, 7) = 3,432` is a valid maximum; the actual value is `C(14, 9) = 2,002` if all 14 are extreme. **Step 1b** (356–367). The greedy removal in any order leaves exactly one row per extreme ray: a retained row is outside the cone of the rows retained at its turn, hence outside that of the final set, and the cone is pointed. So the retained count is order-independent and equals the counted quantity. The text's claim holds. **Verifier** (475–478): in-order check of `λ ≥ 0`, `Σ λ_q a_q = a_p` and `q` retained; then the induction gives cone(retained) = cone(all) ✓. **C-SYM** (658): only GX+R-Y exceeds `C(E, d − 1) ≤ 10^5` (`C(25, 9) = 2,042,975`). Every effect column there is an exact 0/1 sum of the 12 point-indicator columns, so at most 12 effect rows are retained, with `C(12, 9) = 220`. Every other completion's listed `C(E, d − 1)` is at most 27,132 (H3+RG; the writer's script omits the +RG rows, which do not change the conclusion). **Timeout bullet** (451–455) ✓; step 6 covers 1b ✓; C-CERT, C-INDEP and the invariant rows ✓ |
| **Rb2** provenance label | ✓ (nits N4, N5) | The group label is gone. The table (189–216) gives one row per reference with the claim it attaches to. Each classification follows from reading the claim. **H3** (637), **X's order** (639), **GX's restriction argument** (641) and the **moment convention** (621–623) are restated. The restriction argument as written is the §6.4 support condition, which r14's review verified on both the preparation and effect sides. **Line 131's clause is removed. The ledger cites this file or `main`, and E-CTX is "unsupported in this round" ✓.** **Six narrowings**: F0 (175–180, 51–52, 1876–1877) ✓; (a) and ¬X1 as predictions (267–271) ✓; the git reason (1187–1189) ✓, now resting on the self-test; the pre-`D` draft residual (1664–1666) ✓, wording N7; the call estimate (1717–1719) ✓; SW's reviewer-probe clause (642) ✓. `ACCESS.md` r14a's four edits are correct, and its new citation `review/probes-full/p02.out` does show H3, block B and X+RY infeasible |
| **Rb3** owner choices | ✓ (nit N2) | (a) 1908–1912, fail-closed as the labelled draft default (1748–1750, 1780–1781); (b) 2048; (c) 2032–2035. Each is an unbackticked `PENDING` (`p02`: 34 fields), and so blocks `F` through control P |

## 2. The nits and review points

- **Fixed and checked:**
  - N1 (1604–1606, 1993–1994; H22's row 211 scoped too);
  - N2 (1591–1594, 1615–1625, 1760–1761; APPROVALS 783–788);
  - N3 (names at A4, A6, B5 and A11, and every reader);
  - N4 (2108–2113);
  - N5 (2156–2160), N6 (1775–1778, 1083–1088, 1208–1209, 777–782), N7 (1307–1309), N8 (`ACCESS.md`) and N9 (886);
  - N10 (1357–1361, 1737–1739, 722), but see Rc1;
  - N11 (2119–2121);
  - §3's C-SYM facet sentence (658); §5's rows (1234–1235, 1836, 1846, 1851, 1861; BYP-22 is indeed absent).
- **N6's wording** matches Q-C2-1 r14b C.8 item 3 (its 3133–3138), including N11's "run on S1's run before `E` is
  committed".
- **Small residuals.**
  - Invariant row 1865 still says "the `E` entry in `verdict`", in the singular. N2 made it one entry per `E`-stage
    comment id.
  - The stop rule's "a failed S1 binding" (1814) and S1-BIND's "no artifact" case (780) carry the R6-type default
    without its label. Q-C2-1 r14b labels every such site (its N2).

## 3. The fourth new `PENDING` item (§A.42 item 8 dispositions; 1913–1918)

**It is legitimate, and correctly placed.**
- **The classification is right.** The final capture's record, the `E`-stage Environment reads, and the approval
  entries built for the dispatches at `E` exist only after `E`.
  - Nothing can be added to the record directory after `E`: `Q` adds only the receipt, and `G13` freezes the
    directory.
  - A dispatch at `E` does not re-create them: it would read the Environment and approvals as they are later, not
    as they were.
  - So each is a gap under item 8. The only closures are narrowing, in a record still mutable before `F`, or a
    recorded owner exception.
- **It is the owner's choice.** Only the owner can grant the exception, and the two options change what the landed
  record claims.
- **The form is right.** It sits in precondition 2, it is unbackticked, so control P refuses `F` until it is filled,
  and the decision sheet has a row for it. No option is chosen in the text: 1301–1302 and 1549–1551 say only that the
  disposition is the owner's.
- **The list is complete.** Row 216 ("the `E` run's other records … re-established … by a dispatch at `E`") covers
  the computational remainder. `verdict`'s own enumeration window is subsumed by the final capture, which enumerates
  to landing.

**Defects in its wording (N3).**
- **(i) The narrowing option, as written, does not close the gap.** It says "the landed record states those checks
  as halt conditions met before landing". To state that the checks were *met* is itself a claim that uses the
  off-`main` records. It contradicts the option's own "makes no claim that rests on their content".
  - The narrowing should state them only as conditions of landing: the round lands only if they pass. It should not
    state that they passed.
- **(ii) Filling the record id alone changes no text.** Under either option, the passages that now assert these
  properties must be revised before `F` and reviewed under precondition 4:
  - control N (1299–1303) and *Its record* (1549–1552);
  - the approval entries (1591–1594);
  - invariant rows 1846–1849, 1854 and 1865;
  - the table's row 215.

  Say so in the item, and name these sites. Otherwise a record id could satisfy control P while the text still
  carries the unsupported claims.
- **(iii) Say what each option leaves of the token.** The token's scientific content (F1's verdict, replay-matched)
  is re-established by a dispatch at `E` under either option. The governance claims (approved dispatches at `E`, the
  Environment at `E`, no unapproved run after `E`'s capture) are what the exception leaves unestablished (§A.46
  item 1). Stating this lets the owner choose knowingly.

**Its divergences from Q-C2-1, and the writer's other three.**
- **Q-C2-1 does not raise this question.** Its final capture and its `E`-entry ratification (R8) are equally
  host-time. A designation that quotes a sha256 does not retain content (§A.42 item 2). So the same item 8 gap exists
  there, unclassified. QC22 is the more careful of the two. This is noted, not a QC22 defect.
- **`S_max` not imported:** correct. QC22 has no ST-BP and no owner budget; every enumeration is bounded by the frozen
  `10^5`.
- **N13's incomplete-output relabel not imported:** correct. QC22 has one round-level VOID, and a crash or timeout
  is already a "checker outcome". There is no test-level VOID to separate it from.
- **R8's ratification not imported:** an intended divergence, as before. QC22 verifies the `E` entries against the
  host through the Environment's approvals and deployments. Their item 8 status is this `PENDING`.
- **Conditional step 1b (Q-C2-1 runs it always):** justified, and safe.
  - It changes nothing for any fragment within the caps as listed, and F1's family never triggers it (at most 16
    listed rows).
  - Because only GX+R-Y triggers it, and GX+R-Y's preparation-side and C-SYM verdicts are both "infeasible", no
    feasible-after-removal path is ever used in this round. So Q-C2-1's positive control B-RAY is not needed here.
- **The caps' counting** mirrors an owner decision in Q-C2-1 (D19 (0)(c)). In QC22 it is not owner-reserved: it
  changes no decision, no scope and no expectation, and it only keeps one fixture decidable. That is a method choice
  for review, not a scope choice.

## 4. Re-read: other findings

**Nits (fix in the same revision).**
- **N1 (governance: authorization of r14a).**
  - Line 43 says "r14a applies them under the same authorization", and DISPOSITIONS says "The same scope covers this
    review's findings".
  - c.6740747027 records the owner's choice "Fix B1–B6 and the nits … then run a further independent review". The
    question it answered distinguished explicitly: "Your authorization covered the review and the decision sheet,
    not a revision".
  - A second revision is therefore a reading of the record, not its text (§A.45 rule 3).
  - **Fix:** record the owner's confirmation, or word line 43 as the coordinator's reading, as precondition 4 does.
- **N2 (R6 alternative; Q-C2-1 r14b's fix not taken).**
  - The alternative (1911) omits the clause that Q-C2-1 r14b added (its 1653–1657): "the committed measurements are
    then bound to the approved computation by B6's replay at `E` only, not to S1's output."
  - The decision sheet's row also states this wrongly: "bound to S1 only by B6 at `E` and the binding's record at
    `E`". B6 at `E` binds to `E`'s recomputation, and the record at `E` holds S1's archive digest, not a content
    comparison.
  - The alternative also needs a frozen rendering for "the limitation printed". No frozen text exists for it, so
    choosing the alternative needs a reviewed revision. Mark it **[R]** on the sheet.
- **N3.** The fourth `PENDING`'s wording, (i)–(iii) of §3.
- **N4 (off-`main` table completeness).**
  - Line 827 asserts "`r_S ≤ 6` against 36 reads" unqualified. This is `ACCESS.md` §5's paper prediction. Mark it
    as predicted, or add the site to row 204. The same applies to 273's "In F1 the conjunction reduces to (c)",
    which needs (a).
  - S1's measurements artifact (`verdict`'s S1-binding read) is classified inline (1751–1752) but has no row.
- **N5 (row 216's re-establishment route).** "A dispatch at `E`" with `arp3qc22_decisive` true needs a ref at `E`
  that the deployment-branch policy admits. That means the round or gate-test branch moved to `E`, or a policy edit
  after Q-C2-2 closes. Say which, or the classification has no executable route.
- **N6 (M-RAY, 677–679).** "Its first row removed under a fabricated certificate" is invalid by construction on the
  preparation side, where the first row is extreme (`p03`). On the effect side, the first effect in frozen order is
  `[e = 0]` of a point read, which may be a complement, a removable row; so a "fabricated" certificate is not
  invalid by construction unless its form is fixed. Use Q-C2-1's wording, "an extreme row removed under a fabricated
  certificate", on both sides.
- **N7 (1664–1666).** "Which is the writer's statement" reads as a present assertion of a fact about pushes before
  `D`, which is still in the future. Write "this round does not check it" only, or make it an executor commitment
  with a checkpoint (§A.41).
- **N8 (2034).** "Under (iv), the session's identity, which the dispatcher rule and the authorship condition use."
  Under (iv), B3b and the review check use `amaybaum`, authorship requires `amaybaum`, and `prevent_self_review`
  enforces the dispatcher rule on the host. No mechanical condition reads the session's identity. Say what it is
  recorded for. IMPL-DELTA A8 lists B3b and the review check as its users, which is true under (i) only.
- **N9 (drafting records).**
  - DISPOSITIONS says "four rows added" to the decision sheet. The diff adds three; precondition 4's row was already
    in r14's sheet.
  - The sheet's §0 still presents ENV-CREATE as an open conflict and says it rests on r13. c.6740593434 resolved it
    (2a stands), as DISPOSITIONS-r14 recorded.

**Optional.**
- The common clause's "(reproduced in this round as CC-F0 …)" (840). Since F0 is now a paper prediction, "decided in
  this round as CC-F0" matches the narrowing.
- G's configuration space: the row says "`η = 1`", so G may live on 4 or 8 points. Verdicts are the same either way
  (`p03`: G and G4), but the effect counts differ.
- Line 886 is 152 characters wide (re-wrap).

## 5. Owner decisions: complete, and none decided implicitly

- **All owner items are unbackticked `PENDING` fields.**
  - precondition 1's records and disposition;
  - precondition 2's record (O-7, O-1–O-3, audit, F1+R-S, floating point, paired completions), Q12, the expired
    artifact and the §A.42 item 8 dispositions;
  - 2a's commitments and branch names;
  - 2b's record and the E-ID identity;
  - precondition 3;
  - precondition 4's confirmation.

  Control P refuses `F` while any of them remains (`p02`: 34).
- **Owner acts at execution time are not pre-`F` fields, correctly.** These are retake decisions (1800), GT-6b
  (optional) and launch authorizations.
- **Checked for implicit decisions.**
  - The conditional step 1b, the C-SYM cap, `always()` on A3b and N2's host-VOID entry rule are method choices
    within review. None is owner-reserved, and none changes a scope or an expectation.
  - The R6-type fail-closed default is labelled at its main sites (residual in §2).
  - Nothing reads an owner option as chosen.

## 6. §A.41, §A.42 item 8, §A.44, register, authorization

- **§A.41.** Every new mechanism has a checkpoint: step 1b with C-CERT, C-SYM and M-RAY; the C-SYM cap with a
  recorded `out_of_scope`; the binding's record with S1-BIND; the re-derivation with `check --freeze`. Gaps:
  - Rc1's hazard has no mitigation;
  - N7's residual has none either.
- **§A.42 item 8.** The table answers Rb2. Residuals are in N3–N5.
- **§A.44.** No condition reads log text. A3b's `always()` keeps the mode in a step conclusion, and C-SYM's
  `out_of_scope` is a recorded field.
- **Register.**
  - The printed sections contain no S4 phrase (`p05`). The writer's `s4_screen.py` hits only the S4 list itself.
  - The new identifiers (M-RAY, GX+R-Y, R14-…) are code names or tags.
- **Authorization.** Nothing in the text authorizes a run, `F` or an Environment change. The one implied
  authorization is the r14a status line (N1).

## 7. Probe files (`review/probes-r14a/`; reviewer checks, not evidence)

| file | what |
| --- | --- |
| `r14a.rebuilt.md`, `ACCESS-r14a.rebuilt.md` | `make_r14a.py`'s outputs; `cmp`-equal to the installed files |
| `p01.out` | `review/probes-r14/p01_v3blocks.py` on r14 against r14a: both blocks equal |
| `p02.out` | `review/probes-r14/p02_pending.py` on r14a: 34 unbackticked `PENDING` |
| `p03_caps.py` / `p03.out` | Every fixture and completion is built independently from r14a's text, with exact `Fraction`s. The script reports listed `n`, `d`, the effects before reduction, `E` after step 1, `C(n, d − 1)` and `C(E, d − 1)`. It checks GX+R-Y's four certificates exactly on `N`, extremeness by support, and the effect-side 0/1 sums. Ranks only: no LP and no simplex |
| `p05_s4.py` / `p05.out` | S4 screen of the printed sections (829–905, 913–1011), with the S4 list itself skipped: 0 hits |
