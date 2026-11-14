# Status note: SUBSTATE-BRIDGE-1 L3, a shared factor that no setting writes is a common cause

**Draft for the Bell landing package (`LANDING-PLAN.md` §5.2).** At landing this note becomes
`verification/programmes/oi-qm/reconstruction/substate-bridge-l3-<date>/STATUS.md`, beside the carried
record `SB-L3.md`. That record is written in the package; this note states the standing it will
have. It is drafted for landing form (B) of `NOTES-PLAN.md` OQ-3, a carried extract; under form (A),
the whole SB draft, a different note is needed.

## Source and the carried record

- **Source.** `verification/programmes/oi-qm/reconstruction/drafts/substate-bridge-1-20261111/SUBSTATE-BRIDGE-UNIT1.md`
  at `86a413c88cd14d344aa41b6f47885aeb24da6910` (PR #1232, r2; parent `b94b283a`, r1; base
  `cac5d264`), blob `9ff0f0774e403ed782354c0b10986a0fe5dc5ed8`, SHA-256
  `662b9cbaab4237a357174b675c7ee7734c4d4512ef68d530555111230bde48fd`, 356 lines. "S:n" is line n of
  that file. L3 is §3.2, S:167–171.
- **The carried record `SB-L3.md`** (to be written): S:167–171 copied verbatim; a pin block; the
  hypotheses below, stated from Bell-scope §3.1–3.2 (BS:139–196, landed in the same package); one
  marked change, `Main:364` → `Main:362` (the same line at `c3b5f37a`); one marked addition, the
  extension to Theorem N′ (below); and a support-layer paragraph. Its blob and SHA-256 are recorded
  here when it is written.
- **Scope at the accepted head.** S:169 names Theorem N only, whose hypotheses include (GI) and MI
  for Ω. The Bell ladder's controlling condition also uses the (MI\*) branch, Theorem N′
  (BELL-LADDER-r3:57–60). N′'s proof reuses step 1 unchanged ("Step 1 does not use (GI)", BS:190),
  so the directed reading carries to N′; that one-line composition is not in SB and enters
  `SB-L3.md` as a marked addition [A], reviewed with the record (`LANDING-PLAN.md` §2.5).
- **Why an extract.** The owner's option (c) for #1232 lands "only the results not already on
  `main`" in a minimal package (#1169 c.6854728636), and the carried set of #1169 c.6855167580
  excludes L3; #1274 lists L3 as not carried (`intervene-substate-results-20261113/NEW-RESULTS.md`:641
  at `fef94857`) and names "land #1232 L3 through its own gates" as the remediation of its gap D2
  (`STATUS.md`:162 there). The owner's package names "SB L3 (#1232)" (#868 c.6873193841). An extract
  lands L3 without landing the SB results outside the owner's sets.

## Reviews

- ChatGPT review 5858000929 (posted under `amaybaum`, 2026-11-11T11:26:44Z) at `b94b283a`: REVISE on
  other findings; it records "The classical common-cause observation is also correct under MI."
- ChatGPT review 5859960068 (posted under `amaybaum`, 2026-11-11T14:03:54Z) at `86a413c8`: ACCEPT
  WITH NITS for r2's bounded paper analysis; its nits do not concern L3.
- The re-review of Bell-scope r2, 5857981727 at `e1534b08`, records L3's point as a nonblocking note:
  "A shared mode read by both wings, without a **directed** remote-setting-to-record path, may violate
  the symmetrized Sep inequality yet still leave parameter independence intact."
- The non-author review of the Bell ladder r1 (`drafts/bell-ladder-20261113/REVIEW-r1.md`:138, :279–286)
  checked the ladder's citations of L3 and its use in check 4; it did not re-derive L3.
- **Nature of the reviews.** Model reviews; none is a human review, a GitHub approval or an owner
  decision, and none is verification (§A.46 item 7). No separate non-author review of L3 is recorded,
  and the carried text `SB-L3.md` is not yet reviewed.

## What the record supports, and at what strength

**Claim supported by this record:** "If no directed `G_φ` path of length at most `t − t_s` runs from
the remote wing's generator region into a wing's record region at any tick `t` of the record window,
step 1 of Theorem N holds with directed distance; a hidden factor that both wings read and no
setting writes then belongs to Ω, and the conclusion of Theorem N is unchanged: the factor is a
common cause, and (Sep) with the symmetrized distance is sufficient, not necessary, for parameter
independence; by the marked addition, the same holds for Theorem N′ under (MI\*), whose proof reuses
step 1 (paper argument [A] on Main's cone lemma [P] and Bell-scope Theorem N and N′ [A];
model-reviewed for Theorem N, the N′ addition not yet reviewed; not independently verified; not
adopted; no manuscript claim affected)."

Consequence stated with it (S:171): a shared static or autonomously evolving substate cannot by
itself produce a Bell violation; parameter independence fails only through a directed path
generator → factor → record (requirement N2 of route A, carried by #1274 conditional on L3).

## Hypotheses

- Every hypothesis of Bell-scope Theorem N, (D), (F), (Gen), (Rec), (GI), every-run outputs with a
  fixed local failure rule, a finite jointly admissible menu, no postselection and (MI) for Ω, or of
  Theorem N′ with (MI*) for λ*, with (Sep) read with the directed distance.
- The directed reading of Main's cone lemma: `(φ^k(s))_i` depends only on components with a directed
  path into `i` of length at most `k`. Main:362 states the lemma for the symmetrized graph; the
  directed form follows by the same induction and is part of L3's argument [A].
- The shared factor's content at the setting slice lies outside the generator regions, so it is part
  of Ω and (MI) or (MI*) applies to it.

## Limitations

- L3 is a one-paragraph argument; its step is the directed cone induction, not written out at length.
- The generic check S5 cited with it (`probes/generic_substate_checks.py`:241–259 at `86a413c8`) draws
  response tables that already factorize through the shared mode, with setting-independent weights;
  it checks the standard CHSH bound for local models and does not exercise the directed-cone step.
  It is provenance, not support.
- L3 says nothing about a factor that a setting writes (route A with N2), about routes B and C, or
  about the O2 window.
- The SB unit's own 2026-11-11 authorization was not located (`intervene-substate-results-20261113/PROVENANCE.md`
  §4 at `fef94857`); three out-of-brief native-rule scripts run in the r1 session are excluded from
  the unit's evidence (S:340–342) and are not used by L3.

## Verification status and remediation (§A.46 item 4)

The accountable Issue is #1169. Model acceptance is evidence of review, not independent mathematical
verification (#1169 comment 6865680499). This plan authorizes no work. The gap remains open until
the evidence or decision named for it is recorded on `main`.

Here "independently verified" means verified from `main` to the standard for its kind, for example
kernel-checked or independently verified mathematically (§A.46 item 1); "partially verified" means
reviewed by at least one separate AI-agent reviewer, or resting in part on kernel-checked statements,
without independent mathematical verification of the result; "exploratory" means a result not
reviewed by anyone but its writer, or a proposal that claims no result; "known-invalid" means refuted
on `main` by a counterexample or disproof.

- **Independently verified:** none.
- **Known-invalid:** none. No review reports an error in L3.

| Result | Status | Current evidence | Missing verification | Resolving evidence or decision |
| --- | --- | --- | --- | --- |
| L3 as written (Theorem N) | partially verified; conditional on Theorem N's hypotheses with directed (Sep) | [A] on Main:362 [P] and Bell-scope Theorem N [A]; ChatGPT reviews of SB; S5 provenance | independent mathematical verification of the directed-cone step and of L3 as stated; a review of the carried text | an independent mathematical verification recorded on `main` (for example a kernel formalization of the directed cone lemma, or a human review); the package's non-author and ChatGPT reviews of `SB-L3.md` |
| Extension to Theorem N′ (marked addition) | exploratory until the package's reviews; conditional on Theorem N′'s hypotheses with directed (Sep) | [A], one line from BS:190 | any review; then as for L3 | the package's non-author and ChatGPT reviews of `SB-L3.md`; then as for L3 |

Where the gap cannot be closed, the result is narrowed or withdrawn where it is stated (§A.46 item 5).

## Dependencies

| Reference | Classification at landing |
| --- | --- |
| Bell-scope Theorem N step 1 (BS:168–170) and Theorem N′ (BS:185–196), `e1534b08` | Support on `main`: lands in the same merge. |
| `papers/Main.md`:362 at `c3b5f37a` | Support on `main`. |
| `SUBSTATE-BRIDGE-UNIT1.md` at `86a413c8` | Provenance: the copied content is in `SB-L3.md`. |
| S5 in `generic_substate_checks.py` at `86a413c8` | Provenance (see Limitations). |
| #1271 reconciliation, R3:66 at `703ae20e` | Provenance: it reads L3 as the standard Bell argument; no claim rests on it. |
| Reviews 5858000929, 5859960068, 5857981727 | Review provenance. |
| #1169 c.6854728636, c.6855167580, c.6865177667; #868 c.6873193841 | Governance provenance. |
| #1283 at `f57e576a` | Provenance until adopted (see Landing). |

## Source drift from `cac5d264` to `main` (`c3b5f37a`)

S:169 cites Main:364 for the symmetrized definition of `G_φ`; at `c3b5f37a` that sentence is at
Main:362, with "symmetrized for the spatial graph" unchanged. Main:362 also now defines `G_φ^K` and the
linear-update clause, which L3 does not use.

## Superseded lines in the source

S:3 ("pending focused re-review") and S:356 ("r2 has not been re-reviewed"): r2 was re-reviewed at
`86a413c8` (5859960068). These lines are not carried.

## Landing

- **Together.** `SB-L3.md` lands in one merge with Bell-scope r2, on whose Theorem N it rests, and
  with the Bell ladder r3, which cites it for the directed form of (Sep) (BELL-LADDER-r3:57–59, :100,
  :156).
- **Mode.** The record is new text in the package; the package lands by merge commit.
- **Basis.** The proposed basis is §A.46 item 8 as drafted in #1283 at `f57e576a`, which is not
  adopted; the basis is open until #1283 is adopted. Record-specific check of the draft's conditions:
  - substantive, nonredundant result: met (the directed form of (Sep), not on `main` and not carried
    by #1274);
  - scope and limits documented: in this note; `SB-L3.md` is to state them;
  - independent non-author review and ChatGPT exact-head review: not met for the carried text; the
    source has two ChatGPT reviews and no separate non-author review (owner question OQ-2 of
    `NOTES-PLAN.md`);
  - accountable Issue, verification status, remediation plan: #1169, this note;
  - explicit rationale: the Bell ladder's directed (Sep) (stage 3, §0, check 4) and #1274's gap D2;
    owner merge decision: not recorded;
  - historical authorization: the 2026-11-11 approval of the SB unit was not located; #1169
    c.6854728636 step 5 asks for a current owner decision to replace it (owner question OQ-7).

  The record is preserved, not established (§A.46 item 1). Its removal is not automatic and is
  governed by §A.46 item 6.
- **Owner record.** #868 comment 6873193841 names "SB L3 (#1232)" in the package. No merge decision
  is recorded.
