ACCEPT WITH CHANGES — `S3-PLAN-r4.md` at `5001331a208155e13027d1465652d29f219d9b5a` (`research/ro1-sector-c-1169-20261114`, PR #1294).

# Focused confirmation of the S3 plan, r4

**Reviewer.** Independent reviewer; not the writer. Read-only and paper-only: no computation, no
Lean build, no edit, no commit, no post.

**What was read.**
- `S3-PLAN-r4.md` and `RESPONSE-S3-PLAN-r3.md`. The copies supplied to me are identical to the
  committed files.
- `S3-PLAN-r3.md` is unchanged, and `REVIEW-S3-PLAN-r3.md` is preserved as delivered.
- The full diff from r3 to r4.

**Line numbers** are r4's.

## 1. The four fixes

- **R3: resolved (ll. 687–693).**
  - The new wording: "no restriction is *proposed, or reported as passing*, if it excludes PR by
    disabling …".
  - A restriction found to do so is "reported as failing AC-1", which is "an admissible finding", in
    line with H-RR's refutation route (§4.1).
  - The stop is narrowed correctly, to a unit "that cannot test a restriction against both coverage
    and soundness on one interface".
  - §6's row is unchanged, as advised.
- **R4: resolved (ll. 513–516).**
  - The sentence now reads: "Whether a which-path marker lies in the reference class depends on OB-b0
    … open under #1234. If the marker does not lie in it, D-1 does not apply under the scoped
    reading."
  - The statement is conditional, and nothing is decided.
- **N1: resolved (ll. 530–536)**, labelled [A-inf]. It carries the coupling, the masking, the joint
  survival with whatever retains `s_A`, "may be empty", and the joint decision of (β) and (δ). There
  is one consequence to make explicit (R5, below).
- **N2: resolved (ll. 285–287, 552–553).**
  - "At the rate" is removed.
  - The new clause, "A rate counts only where the rate limit is itself structural, that is, where it
    differs between PR and the quantum references on the shared interface", does not bring back a
    resource count. It admits a rate only where it discriminates, and the paragraph's prohibition
    stands: "It cannot be a resource count … 'Scarcity alone is not a separator'".
  - SEL-DISC-1 P5 records that fair quantum outputs need comparable entropy. So a discriminating rate
    would have to overcome P5, and AC-1 would still apply. No change is needed.
  - The falsification sentence now names both directions:
    - a miss falsifies the K1 reading together with the identifications;
    - a match falsifies the reading that native K1 recording misses complementarity.

## 2. Nothing else changed

- The diff touches only the title, the revision header, and the lines above.
- The "Revision r3" note is moved into the past tense.
- No other line differs.

## 3. Does "may be empty" quietly close route M?

**Not by itself.** Route M still needs (b′), the observer-level lift, and (c′), the σ12 screen, and
both lie outside U4. The plan keeps "U4 alone cannot close route M negatively" (§8.6). The
native-marker *miss* branch is what "may be empty"; that is not the same as route M closing.

**One gap does open (R5, required, one sentence).**
- The outcome "Empty on K1" is defined as "(β) fails under the global reading" (l. 540), and (a′)
  counts it towards a negative closure.
- After N1, for the native marker, (β) fails "unless `s_A` is held elsewhere".
- Whether `s_A` can be held elsewhere is the ready-region / history-record sourcing question. The
  plan itself carries the MR-1 GAP caveat on it (l. 660): "the absence of a proved ready supply is an
  open sourcing problem, not a proof that no ready supply can exist".
- So a failure of (β) that rests only on unsourced retention of `s_A` is an open sourcing gap, not a
  failure. Left implicit, it would let U4 record "empty on K1" for (a′) on the strength of an open
  question.
- **Fix:** add one sentence to the N1 bullet or the "Empty on K1" outcome:
  > Where (β) fails only because retention of `s_A` is not sourced, D-1 is reported as unsourced at
  > (β)–(δ), not as "empty on K1", and does not count toward (a′).

## 4. Verdict

**ACCEPT WITH CHANGES.**
- R3, R4, N1 and N2 are resolved.
- The diff is limited to them.
- R5 is a one-sentence clarification that keeps N1 from feeding an open sourcing gap into the
  negative-closure count.
- With R5 applied, the plan is acceptable without another review round. A diff check of that sentence
  suffices.
