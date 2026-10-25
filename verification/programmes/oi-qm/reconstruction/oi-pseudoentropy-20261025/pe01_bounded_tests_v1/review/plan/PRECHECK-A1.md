# Pre-freeze check of A1 (ced675cc) and the evidence commit (01eb7950)

## What was read

- **Amendment A1:** `pe01_bounded_tests_v1/amendments/A1-owner-decisions.md` at `ced675cc`, sha256
  `037253a4d08f5c1bd715f45b68b535bb38d494445e54c191fb093da36f05c86f`, recomputed from `git show` and matching yours.
- **The plan A1 names:** PLAN.md at `af38dc2d`, sha256 `bf7b0cb9…e091`. That matches A1:8–9.
- **Neither commit touches PLAN.md.** `git diff --name-status af38dc2d ced675cc` lists only additions under
  `amendments/` and `review/plan/`.
- **Revision 5 itself.** I had not reviewed it, so I checked it here. A whitespace-insensitive word diff of
  `1cbfba61..af38dc2d` changes only the N6 sentence of §6 item 4 ("θ and the m = 3 scope are the open owner
  decisions (§10); K_LP awaits confirmation"). Everything else is rewrapping. Revision 5 is therefore the accepted
  revision 4 with N6 applied.
- **Line numbers** below refer to A1. Read-only throughout: no commits, no pushes, no PE-01 runs.

## Verdict: BLOCK (narrowly), pending one owner answer and one sentence

A1 records the three decisions faithfully, and its caps are right. Two items must be settled before this commit becomes
the freeze:
- **P1:** the owner's "separate from the primary acceptance criterion" safeguard is ambiguous, and A1 implements one
  reading of it. It must go to the owner.
- **P2:** the incomplete-shard sentence changes the plan's reporting and stopping in substance.

Everything else is ACCEPT, apart from three nits.

## 1. Faithfulness and caps

- **θ = n+1 (:15–20).**
  - The rationale is quoted verbatim.
  - (f) becomes m + ⌈log₂(K+1)⌉ + 1 ≤ n+1.
  - The region is the plan's θ = n+1 table, recomputed by AR.
  - The horizon bound K < 2^{n−m} matches PLAN §7.
- **K_LP = 2^{n−1} − 1 (:21–24).** Verbatim, including "no post-result adjustment", and it matches the §8 LP row.
- **Passive m = 3, option (ii) through n = 8 (:25–32).**
  - Verbatim, and the sweep stays passive (a ≡ 0).
  - The caps are K ≤ 15 at n = 7 and K ≤ 31 at n = 8. These match the top of every m = 3 cell of my θ = n+1 table at
    n = 7 and n = 8: [11,15] | [9,15] | [8,15] and [12,31] | [10,31] | [9,31] for G_lin | G_filt | G_clk. The top is the
    same for all three generators.
  - n ≤ 6 runs uncapped, as already planned. That is consistent with (ii).
- **Safeguards.**
  - The decisions and rationale are recorded (:13–32).
  - Revision 5's content is preserved: PLAN.md is untouched, and :3–6 says so.
  - The checker uses exactly the preregistered parameters: the parameter block and refusal at :54–55.
  - No post-result change without a recorded amendment (:48–50).
  - θ = n is kept as an untested alternative (:42–47).
  - "Separate from the primary acceptance criterion" is the exception (P1).

## 2. Does A1 change plan content?

- **(a)–(f), thresholds, window, controls and classification:** unchanged. A1 only instantiates θ, K_LP and the m = 3
  scope.
- **P2 (required): ":40–41 A missing or incomplete m = 3 shard is reported as 'not run' for those cells."** This is a
  substantive addition, and it contradicts A1's own claim at :4–6 that it changes nothing else.
  - The plan has no partial-completion rule. Its only stopping provision is §8's factor-of-3 move to CI.
  - Labelling an *incomplete* shard "not run" discards measured cells. Without a rule for when a shard counts as
    incomplete, it opens an optional-stopping route: a shard can be stopped after something is seen and then reported
    as never run.
  - That conflicts with the governing principle (verdict text generated from the measurements) and with §8's "shard
    outputs are committed as structured JSON".
  - It does not conflict with VOID precedence, which :41 keeps, provided every checkpoint that ran inside the shard
    still counts.
  - *Fix, one sentence:* "A shard that was never started is reported as 'not run'. A shard that started and did not
    complete is reported as 'incomplete', with its reason and every completed cell's results, and its partial output is
    committed like any other. Neither status is a verdict. Any checkpoint failure inside an m = 3 shard makes the stage
    VOID (§6.1)."
  - If the owner intends m = 3 control failures to void only m = 3 cells, see P1(c). That would be a change to §6.1,
    and it needs its own explicit owner decision.
- **The θ = n paragraph (:42–47) does not overclaim.** It is conservative.
  - Within the enumerated scope, the absence of an admissible witness at θ = n+1 logically implies absence at θ = n,
    because the θ = n region is a subset of the θ = n+1 region.
  - :45–46 declines to report even that implication. This is faithful to the owner's "not automatically under
    θ = n" and is not an error.
  - A COUNTEREXAMPLE at θ = n+1 does not transfer to θ = n, and A1 does not claim that it does.
  - A witness's own footprint ≤ n is recorded as a measured fact (:43–44). That is correct.

## 3. "Keep the passive sweep separate from the primary acceptance criterion"

The phrase is ambiguous, and I recommend putting it to the owner. There are three readings, and they lead to different
freezes:
- **(a) Your reading, which A1 implements.** One decision rule. m = 3 passive witnesses can be COUNTEREXAMPLEs. The sweep
  is reported in its own cells and runs in its own shards.
- **(b) Secondary status.** m = 3 passive results are reported, including witnesses meeting (a)–(f), but they do not
  enter the stage's primary outcome (COUNTEREXAMPLE / bounded-resource claim). They would be labelled as secondary
  findings.
  - "Primary acceptance criterion" read literally as "the main decision rule" supports this.
  - The owner's rationale, "necessary to examine m = 3 where the relaxed cap makes witnesses admissible", cuts
    against it.
- **(c) Operational separation.** The sweep's completion or cost does not gate the stage's acceptance. A missing m = 3
  shard does not hold the stage. Under the strong form, an m = 3 control failure voids only the m = 3 cells.
  - A1's shard sentence fits the weak form.
  - The strong form changes §6.1's VOID precedence.

Your reasoning from (ii) over (i) is sound as far as it goes. It rules out "comparison-only at n ≤ 6", but it does not
rule out (b) or (c). Suggested question for the owner:

> "By 'separate from the primary acceptance criterion', do you mean (a) the same decision rule with separate reporting;
> (b) m = 3 passive witnesses reported but not counted toward the stage's COUNTEREXAMPLE outcome; or (c) the sweep's
> completion does not gate the stage — and if (c), should an m = 3 control failure void only its cells or the whole
> stage?"

A1 should record the answer verbatim, with the reading it implements.

## 4. Parameter block and TH wording

- **Consistent with the plan's TH row** (revision 5, §5). The TH row records θ, K_LP, the m = 3 scope decision and the
  amendment blob, and requires the amendment's commit to be an ancestor of every run commit.
- **A1 is stricter.** A run whose parameters differ from the block, or that cannot read it, refuses to start (:54–55).
  The caps sit in the block as part of the m = 3 scope decision.
- **N-a (nit):** `"theta": "n+1"` and `"K_LP": "2^(n-1)-1"` are formula strings that the checker must parse. To make
  "exactly the preregistered parameters" mechanical:
  - add explicit per-n values, `"theta_by_n": {"3":4, …, "8":9}` and `"K_LP_by_n": {"3":3, "4":7, "5":15, "6":31}`;
  - have TH compare against both the formula and the explicit values.
- **N-b (nit):** say that the K_LP values apply only at n ≤ 6, where the LP runs, so that the block cannot be read as
  defining K_LP at n = 7 or 8.

## 5. Evidence commit 01eb7950

- **Byte-identity.** All 13 retained records and scripts are byte-identical to my files: `REVIEW.md`, the two RECHECKs,
  `checks*.py` and `checks*.out`. I compared sha256 against `revpe01/` and `ppe/review/`, and `SHA256SUMS` lists the
  same values.
- **Independent replay.** I extracted the retained scripts with `git show` into a fresh directory and ran all five
  with `python3 -I -B` and the README's argument conventions. Each output is byte-identical to its retained `.out`.
- **README.** It is accurate: verdict table, commit-to-revision mapping, relative paths, working-path mapping, hash
  pairs and replay commands. One nit:
  - **N-c:** :3 says the records cover "from its first version to revision 5", but they end at revision 4. Revision 5
    is covered only by README :15–16 and by this pre-check.
  - *Fix:* "…to revision 4. Revision 5 and A1 are covered by `PRECHECK-A1.md`". Retain this file beside the others,
    with its sha256 added to `SHA256SUMS`.

## Summary

| # | Item | Class |
|---|---|---|
| P1 | Owner to choose reading (a), (b) or (c) of "separate from the primary acceptance criterion"; A1 records the answer | required (owner) |
| P2 | Replace "missing or incomplete → 'not run'" with the not-run / incomplete split and VOID scope | required |
| N-a | Explicit per-n θ and K_LP values in the parameter block | nit |
| N-b | K_LP scoped to n ≤ 6 in the block | nit |
| N-c | README coverage wording; retain PRECHECK-A1 | nit |

With P1 answered and recorded, and P2 applied, A1 is ACCEPT WITH NITS as the freeze.

***

## Addendum: re-check of 7b8ca727 (tree 8a8a1656, parent ced675cc)

Read: the `ced675cc..7b8ca727` diff. It changes three files: A1, `review/plan/README.md` and `review/plan/SHA256SUMS`.
PLAN.md is unchanged. A1's sha256 is `7f15d5afc02e4b66df925f2f99ef10cda2333c9beb58ee10e5f3e9d0cefce1b2`, recomputed
from `git show`, and it matches yours. Read-only.

### Verdict: ACCEPT WITH NITS (A1 at 7b8ca727 is acceptable as the freeze)

| Item | Status |
|---|---|
| **P1** | **Resolved.** :37–40 quotes the safeguard verbatim, and the owner's selection "(a) Same rule", dated 2026-10-25, with its option text. That text says there is one decision rule, that an m = 3 witness meeting (a)–(f) counts as a counterexample, that the sweep has its own cells and CI jobs, and that any control failure voids the whole stage. The bullets that follow (:41–50) implement exactly that. |
| **P2** | **Resolved.** :45–50 splits "not run" (never started) from "incomplete" (started, did not finish). An incomplete shard is reported with its reason and every completed cell, its partial output is committed (§8), neither status is a verdict, and a checkpoint failure in an m = 3 shard VOIDs the whole stage (§6 item 1). The header (:4–6) now says A1 adds reporting rules, replacing "changes nothing else". Nothing in it alters (a)–(f), thresholds, the window, controls, classification or stopping. |
| **N-a** | **Applied.** The block parses as JSON. `theta_by_n` = n+1 for n = 3..8, and `K_LP_by_n` = 2^{n−1} − 1 for n = 3..6, both checked here. The run refuses to start on any disagreement, any difference from the block, or an unreadable block (:63–68). |
| **N-b** | **Applied** (:24–25). |
| **N-c** | **Applied.** README :3–4 now covers revision 4 and points to `PRECHECK-A1.md`. The new README sha256 `ccb7a3f0…65c5` matches its `SHA256SUMS` line. |

The remaining nits need no re-review:
- **N-d.** :64 says "the checker evaluates each formula at every n". Read literally, it would also evaluate K_LP at
  n = 7 and 8, where `K_LP_by_n` has no entry, and then refuse to start. That error is fail-safe, never permissive, but
  it would be spurious.
  - *Fix:* "at every n with an explicit value (θ: 3..8; K_LP: 3..6)".
- **N-e (sequencing, not text).** At 7b8ca727 the README already points to `PRECHECK-A1.md`, which is not yet in the
  tree.
  - As you plan, the final commit should add it, including this addendum, with its sha256 in `SHA256SUMS`.
  - That commit should touch only `review/plan/`, so A1's blob and the TH ancestry are unaffected.
  - The run's TH ancestor is the commit that carries A1's current blob, 7b8ca727 or later. ced675cc carries the old
    blob.
