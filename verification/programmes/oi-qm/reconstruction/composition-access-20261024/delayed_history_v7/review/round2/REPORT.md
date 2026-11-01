BLOCK — candidate 74cdd24ee4f8750c03f73fe4fe52983682e9c472 (#912 `delayed_history_v7`, local, unpublished)

# Second review: `delayed_history_v7` after the review fixes

24 October 2026. Independent, read-only. Nothing was pushed, committed or posted, and the clone was not modified.
The candidate files were exported with `git show` into `c/`. All runs used `python3 -I -B` from empty
directories. Paths below are relative to the round directory
`verification/programmes/oi-qm/reconstruction/composition-access-20261024/delayed_history_v7/` or to this review
directory.

**Summary.**
- Both original blockers are resolved, and the substance reproduces byte for byte.
- Every required control and countercontrol fails or changes when the condition it tests is violated.
- The fix commits move no number, scope or calculation beyond the hunks listed below.
- The block is for one owner-required scope item. `REPORT.md` never states the access contract the result depends
  on: which records are public, that the q-cells are private, and that no observer-access rule is adopted. The plan,
  `PROVENANCE.json` and `result.json` all carry it. This gap was already present at `114ad502`. The fix is one or
  two bullets.

## Original findings

1. **x3 vacuous: resolved.**
   - `checks.py:489-490` now requires the duplicated-tail record/carrier TV to be positive in every family, and
     `checks.py:571-581` makes a failed control give `VOID` and exit status 2.
   - The support count (32,768) is reported only.
   - The first reviewer's M4 (pinned triple, my `X3_PIN`) now gives c2 = 0, x3 false, `VOID` and rc 2.
   - A blind TV statistic (`X3_TVZERO`, which always returns 0) also gives `VOID` and rc 2.
   - The change is labelled post-plan in `PROVENANCE.json`, `result.json` (`post_plan_rows`) and the `REPORT.md`
     x3 row.
2. **L+77 overclaim: resolved.** `REPORT.md:74-76` now reads "could therefore depend … Cone arrival makes that
   dependence possible, not certain. The only dependence actually shown is c3 in the scaled control." This is the
   requested wording.

The first review's nits are also addressed:
- the pad ×4 in the counts (131,072 cells and 4,096 records);
- post-plan labels on the c1 denominators;
- `all_required_controls_pass` computed rather than written as a literal;
- a carrier read-set control;
- the note that scaled bank t = 4, 5 lies in C0;
- the joint prior and the "depends only through the sign" step stated in the argument;
- the stale "no retained review" phrase.

## Diff 114ad502..74cdd24e, every hunk

- **`checks.py`**
  - Added `V6_PHASE_INPUT_BITS = 21`. It matches v6 `result.json:56`.
  - Added the actual-L read-set comparison (`:81-83`) and the scaled read-set `need` (`:206-207`).
  - s1 is now a boolean that enters `s_ok`. It was an exception before.
  - x2 is a boolean, with decoded-sign mismatches folded into it. It was an exception before.
  - x1 is a mismatch count. It was an exception before.
  - The s3 pad loop is removed, and so is `positive *= 4`.
  - x3 is the TV criterion.
  - The `required_controls` dict, the VOID verdict and exit 2, `post_plan_rows` and the schema bump to v7.2 are
    new.
  - No model, engine, geometry or statistic code changed.
- **`result.json`.** Comparing every leaf of 114ad502 against 74cdd24e (`cmpjson.py`):
  - Only these change: the new keys, the two renamed counts (524,288 → 131,072 and 16,384 → 4,096, both exactly
    the removed ×4) and the schema.
  - The other 201 leaves are identical, including every g1/g2/g3 value, every c1/c2/c3 TV and the three world-table
    digests.
- **`PROVENANCE.json`.** Five post-plan rows were added and the schema was bumped. Nothing else changed.
- **`REPORT.md`**
  - The header changes "published" to "committed". This is correct: `d72ea524` is a local commit whose parent is
    `588edce1`.
  - The argument is split into four steps, with the joint-prior sentence and the sign sentence added.
  - The L+77 wording is fixed.
  - A note on scaled bank t = 4, 5 is added.
  - Read-set, s1, s3 and x3 rows are added or changed.
  - The c1 denominators are labelled post-plan.
  - A paragraph on replay and VOID is added.
  - No scope list or claim was strengthened. The "Result and scope" lists (`:11-32`) are unchanged since
    114ad502.
- **`SHA256SUMS`.** Four hashes were updated. `PLAN.md` is unchanged since `d72ea524`: blob `927fba6a` at both
  commits.

## Owner check 1: complete record law

### What is computed and asserted

- **Scaled control** (n = 3, k = 2, one port (0,0,−3), H = 8, three dirty backgrounds, 2^18 worlds each):
  - `checks.py:443-453` builds the joint count table of (tail port record of 9 bits, whole V, A, selected J of 4
    bits) over all worlds. It requires every one of the 512·8·2·16 = 131,072 cells to equal
    `target_count(s,a,j)`, zero cells included. That is the claimed law: uniform tail ⊗ uniform V ⊗ v6 (A,J | s).
  - It also requires the exact TV from Pr(record) × v6 to be 0 (`:486-487`).
  - The pre-tail port stream t = 0..5, the old q9 record and the three other neighbours must be constant (s1).
  - Every accepted (record, V) posterior must have mass 20, determinant 0 and sign s.
- **Records and pads.** The record is therefore the full joint law of every public record in the scaled model, not
  marginals or pairwise statistics.
  - The pads are factored by product. That is valid: v6 `REPORT.md:114-120` defines the whole pointer prefix as
    (q_A, 0, q_D) through tick 44 and (q_A, A, q_D) after it. The prefix is a bijection of (A, pads), and the pads
    are fresh and off-lattice.

### What is computed exactly at actual L

These are integer facts with proof-grade exactness:
- **g1:** 64 port-family × carrier pairs, minimum slack 76, with the minimum taken over the convex piecewise-affine
  distance at endpoints and breakpoints.
- **g2:** offsets F8 77, 77, 447 and F10/F9 79, 79, 449.
- **g3:** both horizons lie within 2L.
- **Exposures:** the 14 pre-tail exposures.
- **Read set:** the read-set identity.

### What is argued, not computed, at actual L

The eight-port factorization Pr(N_L, N_tail, Φ | C0) = [N_L = N_L(C0)]·2^(−24(H−L))·Pr_v6(Φ | C0) rests on a
written argument:
- **Step 1, the pool is masked:** inherited from Native A.
- **Step 2, the tail record is a bijection of the tail with G in the complement:** history_v11's inversion. Its
  steps v → α ⊕ H(v ⊕ β) let α and β be any function of the complement, so G may be included.
- **Step 3, the carrier is a function of (C0, G, pads):** g1 plus v6's isolation.
- **Step 4, the tail is not seen early:** computed in history_v11's checker ("no arrival at another public port
  before t"), not recomputed by v7.
- **Pads:** the pad step relies on v6's pointer definition.

I checked each step and found no gap, and my reading agrees with the first review's proof notes (a)–(c).
Pr_v6(Φ | C0) depends on C0 only through s = p.B, which is a function of the public old-q9 record. So averaging over
C0 given the public past gives the stated public law. The law holds for every H ≤ 2L because a prefix of a
uniform-⊗-v6 law is again uniform-⊗-v6.

### What the scaled control supports

It is a finite exhaustive witness that the mechanism works under the full nonlinear two-slice rule. It exercises:
- the same-tick coincidence of a G front and an own-bank arrival (t = 6);
- dirty backgrounds;
- the same-site pool triangle.

It does **not** exercise:
- eight ports, or G reaching two ports at once. At actual L, F8 reaches both port 3 and port 5 at L+77, and F10/F9
  reach both at L+79. history_v11 also has equal-time cross-edges 2→5 and 3→5.
- tail bank t = L+1..L+76, whose scaled analogue t = 4, 5 is held in C0.
- the H ≤ 2L condition. The scaled H = 8 exceeds 2n = 6, which the direct s2 check makes harmless.

So the actual-L statement is a written conditional corollary resting on exact geometry and inherited theorems. It
is not established by the scaled computation. The plan says exactly this (`PLAN.md`: "A scaled control does not
establish the actual-L statement"), and so does `PROVENANCE.json` (`evidence_levels`). `REPORT.md` says only that it
does not establish "an actual-L simulation" (Finding 2).

## Owner check 2: non-vacuous controls (mutants in `mut/`, `mut2/`; outputs `mutants.out`, `mutants2.out`)

Every mutant adds one stderr line, which reports the s3 cell comparison separately from the TV. The `BASE` copy with
only that line reproduces `result.json` byte for byte.

| mutant | violated condition | outcome |
| --- | --- | --- |
| X3_PIN (= first review's M4) | duplicate replaced by a pinned triple | c2 = 0, x3 false → **VOID, rc 2** |
| X3_TVZERO | TV statistic blind | x3 false → **VOID, rc 2** |
| C1_NOG | tail record carries no G (record := raw tail bank) | c1 max = 0, `bank_load_bearing` false; x3 false → VOID |
| C3_FROZEN | c3 evaluated on frozen q8 | c3 = 0, `storage_load_bearing` false (reported only, verdict unchanged, as planned) |
| X1_SCALAR / X1_BIT | one engine's nonlinearity wrong | x1 mismatches 338–389 → **VOID** |
| X2_BOTH | both engines drop the old-local term | x2 false in two families → **VOID** (x2 is trivially true in a family with p = 0; the chosen families have p = 2, 6, 1) |
| READ_DROP (= M3) / READ_TIME | carrier list loses q9+y / old q9 read at L−1 | read-set control false → **VOID** (M3 previously survived) |
| S1_PRE | pre-tail bank cell t = 5 carries a tail variable (both engines) | s1 false → **NEGATIVE** |
| S3_J_TAIL | selected carrier depends on a tail bit | cells fail, TV 25/128, 13/64, 19/128 → **NEGATIVE** |
| ALIAS_BOTH | tail triple 2 aliased to triple 1, full enumeration, both engines | s2 support 32,768, cells fail, TV 131/256 … → **NEGATIVE** |
| NONUNIF_REC | tail record non-uniform but independent of the carrier | **TV 0**, cells fail, s2 131,072 → NEGATIVE |
| G1_SHIFT (= M2) | tail lower bound 77 ticks early | g1 slack −1 → NEGATIVE |
| M1 / M1b / M5 / M6 (first review) | bank mask dropped in the bit-slicer / in both / old-local term dropped in the bit-slicer / native q8 used | VOID (x1) / NEGATIVE (s2 512) / VOID / exception "triangular pool bijection" (fail-closed) |

**Countercontrols do not reproduce the formula.**
- c1 and c2 measure the departure from the claimed reference and are positive only because the record carries G.
  They go to 0 under C1_NOG and X3_PIN respectively.
- c3 uses a different statistic, the TV from the product of marginals. It is 0 two ticks before arrival and 0 on
  frozen q8.

**Residual (Finding 4).**
- The revised x3 guards only the TV statistic. NONUNIF_REC shows that this statistic cannot see a non-uniform tail.
  Tail uniformity is certified only by the s3 cell comparison and s2, and no in-checker control exercises either
  one.
- Both checks do fail when violated (ALIAS_BOTH, NONUNIF_REC), so they are not vacuous. However, the plan's own x3
  target, the s2 support, is now reported only, and as implemented on the subset it never moves: it stays at 32,768
  even under ALIAS_BOTH.

## Owner check 3: scope

These are explicit in `REPORT.md` and not strengthened:
- the supplied history_v11 bank and G priors (`:23`, `:29`, `:36`);
- v6's isolated logical storage (`:24-25`);
- the hypothetical serial alignment L+2..L+91 / L+361 (`:11-12`);
- H ≤ 2L (`:14`, `:31`);
- no native storage, compilation, clock, isolation or actual-L simulation (`:28-30`).

`PROVENANCE.json` and `result.json` keep `native_storage_or_compilation_established: false`,
`observer_access(_rule)_adopted: false` and `actual_astronomical_time_simulated: false`. No handoff or status file
changed in 588edce1..74cdd24e. `CURRENT-HANDOFF.md` still says that a new joint proof is required. That is
consistent while the round is under review, and it must be propagated with its scope on acceptance.

**Missing (Finding 1):**
- `REPORT.md` contains no statement of the access restriction: no "observer", "access", "private" or "permitted".
- The only related item is "new ports or reads" in the "does not establish" list.

This restriction is load-bearing:
- v6 (`REPORT.md:114-124`) calls these channels a "candidate access contract": internal phase and workspace wires
  "are not extra public channels".
- The handoff records that revealing the private M field gives negative posteriors, with determinant −1/18.

Without the restriction, "complete public law" can be read as unconditional with respect to access.

## Replay, hashes, hygiene

- Normal and `-O` runs (`run_n/`, `run_o/`, about 49 s each, rc 0) are byte-identical to `result.json`.
- `SHA256SUMS` passes for all five files.
- All eight `PROVENANCE.json` source hashes match at their stated commits.
- The added lines in 588edce1..74cdd24e contain no absolute paths, tokens, keys, e-mail or IP addresses. The commit
  metadata uses the noreply address only.

## Findings, ranked

1. **Blocking. The access contract is missing from `REPORT.md`** (owner check 3; already present at 114ad502).
   - Add to "The result is conditional on": the candidate access contract of v6 and Native A. The public records are
     exactly the eight raw port streams, the old whole-q9 record, the single whole-V record and the whole pointer
     prefix. Q8, Q10, M, the other neighbours, the pool and the phase and workspace wires are private.
   - Add "an observer-access rule or access closure" to "It does not establish".
   - If the authors wish, also cite the v6 private-M countercontrol as the reason the restriction is load-bearing.
2. **Should fix. Evidence level of the actual-L statement.** Add to "Result and scope" the plan's sentence: the
   actual-L statement is a written conditional corollary (Argument) resting on exact g1–g3 and the inherited Native
   A and history_v11 results, and the scaled control does not establish it. In the scaled section, state:
   - it uses one port of eight;
   - G reaches one port there, but ports 3 and 5 at actual L;
   - its H = 8 exceeds 2n;
   - step 4 is inherited from history_v11's checker, not recomputed.
3. **Nit. The s1 row is mislabelled.** `REPORT.md:90` says s1 in the verdict rule "goes beyond the plan", but
   `PLAN.md` item 2 lists s1 in the HOLDS/NEGATIVE rule. Only two things are post-plan: the change from exception to
   criterion, and the extra conjuncts (old q9 = p, three complement neighbours constant). Reword the row.
4. **Nit, recommended. No in-checker control for the uniformity checks.** Add a post-plan required control: an
   aliased full enumeration, as in ALIAS_BOTH, that must make s2 support < 262,144 and the cell comparison fail.
   That restores the plan's x3 intent (the s2 support) and covers the uniformity checks.
5. **Nit. The read-set control is internal.** It checks the hand-written list against a restatement of v6's read set
   in the same file, with 21 hard-coded. It catches coordinate errors (READ_DROP, READ_TIME), but it is not tied to
   v6's artifact. Say "matches v6's stated read set" or read `phase_input_bits` from v6 `result.json`.
6. **Nit. Provenance wording.**
   - `PROVENANCE.json` keys say `published_plan_commit`, but `d72ea524` is local and not pushed.
   - The preregistration rests on local commit order: plan at 15:21, implementation at 15:35.
   - Push the checkpoint (§A.43) or rename the key.
7. **Nit. The sign sentence.** `REPORT.md:53`: the offer also depends on p.A, success versus failure. Say "only
   through the public old-q9 record (its sign s)".
8. **Nit. Replay commands.** `REPORT.md:116-119`: write the commands with the explicit checks.py path. As written,
   they do not run from an empty directory.

***

# Re-check of 98cf4647

BLOCK — candidate 98cf4647e58e291de1a6181a8a8825694db61ff0 (parent 74cdd24e). This is a narrow block on the s2
half of the new control x4. Everything else is accepted.

Method: the six files were exported with `git show` into `c2/`, and the runs and mutants are in `run_n3/`,
`run_o3/` and `mut3/` (`make_mutants3.py`, output `mutants3.out`).

## 1. Access contract (Finding 1): resolved, and accurate

- **The public set is accurate.** The new condition bullet lists the eight raw port streams, the old whole-q9
  record, the single whole-V record and the pointer prefix. This matches:
  - v6 `REPORT.md:114-124`: the whole pointer triple at every tick, with internal s, a, b, f, scratch and
    phase/pool wires "not extra public channels under this candidate access contract";
  - v6 `REPORT.md:147-148`: old whole q9 and a single whole V;
  - history_v11's eight ports.
- **The private set is accurate.** Q8, Q10, M, the other neighbours, the pool and the phase/workspace wires are
  exactly v6's non-public phase inputs.
- **The −1/18 sentence is correctly scoped.** It reads "in v6's tested sectors … as low as −1/18" with the fixed
  decoder. This matches v6 `REPORT.md:163-167` and v6 `result.json` (`key_exposure_min_determinant` −1/18, 1,024
  negative posteriors). It claims no universal failure.
- **The not-established list** now includes "an observer-access rule or access closure".

## 2. Actual-L corollary and scaled limits (Finding 2): resolved, and accurate

- The paragraph states that the actual-L result is a written conditional corollary of g1–g3 and the inherited
  Native A and history_v11 results, and that the scaled control does not establish it.
- **Ports 3 and 5 at the same tick: confirmed** by exact recomputation:
  - F8 is at offset 77 to both port 3 and port 5;
  - F10 and F9 are at 79 to both;
  - the next offsets are 447 and 449, at port 2.
- **The horizon claim is correct.** `HS = n+k+3 = 8` and `2n = 6`.
- **One residual nit.** The paragraph does not say that step 4 (the tail is not seen early) is inherited from
  history_v11's checker. That is acceptable, because "inherited … history_v11 results" covers it.

## 3. New control x4

- **`cells_match` is a pure refactor.** It has the same loops and the same comparison, with `counts` passed as
  `cnt`. The unmutated run reproduces `result.json` byte for byte.
- **x4 is a required control.** It sits in `required_controls`, and its failure gives VOID with rc 2:
  - `X4_IDENT` (alias map replaced by the identity) gives VOID, rc 2;
  - `CELLS_TRUE` (the comparator always returns True) gives VOID, rc 2.
- **The s2 half is vacuous** (blocking, in the same class as the original x3 finding).
  - `alias` maps all 2^18 lanes onto the 2^15 lanes with tail₂ = tail₁. So `alias_support ≤ 32,768 < WORLDS` holds
    by counting, whatever the model does.
  - It is computed by an inline copy, not by the s2 code. Two mutants show this:
    - `S2_TRUE` (s2 forced True) still gives **HOLDS_WITHIN_SCOPE**, rc 0, with x4 green;
    - `S2_LEN` (support taken as the list length, always WORLDS) gives the same result.
  - So x4 never exercises the s2 statistic. Its REPORT row, "lowers the s2 support to 32,768", reports a counting
    bound as a detection.
  - **My nit 4 shares this flaw.** I proposed "must make s2 support < 262,144" on the basis of `ALIAS_BOTH`, and
    that 32,768 was the same counting bound.
- **The cells half is genuine, but only as a self-test of the comparator.**
  - It does not depend on the model. Every aliased count is a multiple of 8, while the targets include 5, 3, 1 and
    7. So the comparison must fail for any aliased multiset whenever the comparator is correct.
  - Two mutants confirm this. `C1_NOG` (the record carries no G) and `M1b_both` (bank mask dropped in both engines)
    both leave x4 green.
  - That makes it a valid control of the comparator, but it is not a model-level detection.
- **The non-uniform-record mutant no longer gives HOLDS.** `NONUNIF_REC` gives NEGATIVE: s2 = 131,072, the cells
  fail, x4 is green and rc is 0.
- **Fix.** Either option is enough:
  - Option (a): drop the support criterion from x4, keep the alias support as a reported count labelled a counting
    bound, and describe x4 in the REPORT as a self-test of the s3 cell comparator.
  - Option (b): route s2 and x4 through one shared `support()` function, so that the s2 code is exercised, and say
    in the REPORT that the reduction is guaranteed by counting and tests the statistic only.
  - Under either option, the stated purpose of x4 in PROVENANCE.json and the REPORT row should be adjusted to match.

## 4. result.json, replay and hashes

- **result.json.** Against 74cdd24e, only these changed: the nine x4 leaves (support, cells and detected, in each of
  three families), `required_controls.x4_aliased_tail_detected`, one inserted `post_plan_rows` entry (the later
  entries shift by one) and the schema bump to v7.3. The other 226 leaves are identical.
- **Replay.** Normal and `-O` runs are byte-identical to `result.json`, each with rc 0.
- **Hashes.** `SHA256SUMS` passes for all five files.

## 5. Nits

- **Applied:**
  - nit 3, the s1 row;
  - nit 7, "public old-q9 record (its sign)";
  - nit 8, the replay commands now name `$D/checks.py` with a `<repository root>` placeholder.
- **Nit 5, left as is: no objection.** The read-set control still catches coordinate errors.
- **Nit 6, left as is: no objection.** The v6 sibling `PROVENANCE.json:19` uses the same `published_plan_commit`
  key. The key becomes accurate once the chain is pushed, so push before citing it.

## 6. Hygiene

- 74cdd24e..98cf4647 touches only the five round files: PROVENANCE.json, REPORT.md, SHA256SUMS, checks.py and
  result.json.
- The added lines contain no absolute paths, secrets, e-mail or IP addresses.
- The commit message describes the change accurately, except that it also calls the s2 half of x4 a control
  (§3 above).

***

# Re-check of 65650298

ACCEPT WITH NITS — candidate 656502989dd34ef64ba63d54328e13966517444b (parent 98cf4647). The x4 finding is
resolved.

Method: the files were exported to `c3/`. The runs are in `run_n4/` and `run_o4/`, and the mutants are in `mut4/`
(`make_mutants4.py`, output `mutants4.out`).

## Diff 98cf4647..65650298

- **`checks.py`.** Two shared functions were introduced:
  - `support(sub) = len({(pool[l], w[l]) for l in sub})`, which also feeds the reported s2 support;
  - `bijective(sub) = support(sub) == WORLDS`.

  s2 is now `bijective(lanes)`, and x4 is `not bijective(alias) and not cells_match(alias counts)`, using the same
  `cells_match` as s3. The comment says x4 is a self-test of the statistics whose answer is fixed by counting. No
  other code changed.
- **The x4 text in `REPORT.md`, `PROVENANCE.json` and result.json's `post_plan_rows`** is reworded to "self-test of
  the s2 and s3 statistics … fixed by counting, not of the model". This is accurate:
  - the alias maps all 2^18 worlds onto 2^15, so the support is at most 32,768;
  - every aliased cell count is a multiple of 8, while the targets include 1, 3, 5 and 7.
- **The commit message** matches the diff.
- **Files touched:** only the five round files.
- **Hygiene:** the added lines contain no absolute paths, secrets, e-mail or IP addresses.

## result.json, replay and hashes

- **result.json.** Against 98cf4647, the only change is `post_plan_rows[2]`. The other 242 leaves are identical.
- **Replay.** Normal and `-O` runs are byte-identical to `result.json`, both with rc 0.
- **Hashes.** `SHA256SUMS` passes for all five files.

## Mutants against 65650298

| mutant | outcome |
| --- | --- |
| S2_TRUE_FN (`bijective` returns True) | **VOID**, rc 2 (x4) |
| S2_LEN_FN (`support` returns the list length) | **VOID**, rc 2 (x4) |
| CELLS_TRUE (`cells_match` always True) | **VOID**, rc 2 (x4) |
| X4_IDENT (alias replaced by the identity) | **VOID**, rc 2 (x4) |
| NONUNIF_REC (non-uniform record, still independent of the carrier) | NEGATIVE: s2 131,072, s3 false |
| C1_NOG (the record carries no G) | VOID through x3; c1 = 0; x4 green, as expected |
| M1b_both (bank mask dropped in both engines) | NEGATIVE: s2 512, s3 false; x4 green, as expected |
| X3_PIN / READ_DROP / S3_J_TAIL | VOID (x3) / VOID (read set) / NEGATIVE (s3) |
| S2_TRUE_CALLSITE (`s2 = True` at the call site) | HOLDS |

On the last row: this mutation is a no-op on the real run, because s2 is truly True there, so no self-test can
catch it. It is not a finding. x4 now covers defects inside the statistic functions, which is what its new
description claims.

## Remaining nits (non-blocking)

- **Push the chain before anything cites `published_plan_commit`.** Today the preregistration rests on local commit
  order: plan at 15:21, implementation at 15:35.
- **Propagate on acceptance.** `CURRENT-HANDOFF.md` still states that a joint public-history/carrier proof is
  required. On acceptance, propagate the v7 result there with its scope unchanged, per §A.25 and §A.27.
- **Step 4 is inherited.** "The tail is not seen early" comes from history_v11's checker, not v7's. The REPORT
  covers this under "inherited … results".

## Overall verdict, chain 588edce1..65650298

The chain is d72ea524 → f08390a3 → 114ad502 → 92800fc3 → 74cdd24e → 98cf4647 → 65650298. Verdict: **ACCEPT WITH
NITS**, judged against the owner's three checks.

1. **Complete record law: met, within its stated evidence levels.**
   - **Scaled control.** The checker asserts the full joint law of (pre-tail stream, tail port record, old q9, whole
     V, A, selected J) cell by cell, with zero cells included, and also requires an exact TV of 0. The pads factor
     by product through v6's pointer-prefix bijection. These are not marginals.
   - **Actual L.** The result is a written conditional corollary of exact g1–g3 and the inherited Native A and
     history_v11 results. The REPORT now says so, and it names the limits of the scaled control: one port, G arriving
     at one port whereas it reaches ports 3 and 5 at actual L, and H = 8 > 2n.
   - I found no gap in the argument.
2. **Non-vacuous controls: met.** Each control was violated by a mutant and caught:

   | control | violations that move the verdict |
   | --- | --- |
   | x1 | either engine wrong → VOID |
   | x2 | both engines drop the old-local term → VOID |
   | x3 | pinned triple, blind TV → VOID |
   | x4 | broken support, broken `bijective`, broken comparator, identity alias → VOID |
   | read set | site or time dropped → VOID |
   | s1 | a pre-tail variable → NEGATIVE |
   | s2 | bank mask dropped, non-uniform record → NEGATIVE |
   | s3 | carrier depends on a tail bit → NEGATIVE |
   | g1 | tail lower bound shifted → NEGATIVE |

   The countercontrols measure departures from the formula, and each goes to 0 when its condition is removed: c1
   under C1_NOG, c2 under X3_PIN, and c3 on frozen q8. Every post-plan change is labelled in PROVENANCE.json,
   result.json and REPORT.md.
3. **Explicit scope: met.** The REPORT states each of these:
   - the bank and G priors are supplied;
   - v6's isolated logical storage;
   - the serial alignment L+2..L+91 / L+361 is hypothetical;
   - H ≤ 2L;
   - v6's candidate access contract, with the public/private split and the scoped −1/18 witness;
   - no observer-access rule, access closure, native storage, compilation, clock or actual-L simulation.

   No claim is stronger than its evidence. Replay is byte-identical in both modes, all hashes verify, and the
   additions are clean.
