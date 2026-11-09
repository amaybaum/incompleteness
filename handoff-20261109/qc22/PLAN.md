# ARP-3 (Q-C2-2): plan for the native round ARP-3-QC22 (draft r13)

**Status.** WIP / UNVERIFIED. Model-written.
- **Review history.**
  - r1 was reviewed REVISE.
  - r2 was re-reviewed ACCEPT WITH CHANGES, with two blockers.
  - r3 was reviewed REVISE, with four blockers (`review/REVIEW-ACCESS-r3.md`, `86c6c8ad…`).
  - r4 applied that review and the owner's direction #1169 c.6724832474 (amaybaum, 2026-11-08T17:42:02Z).
  - r4 was reviewed REVISE, with three blockers (`review/REVIEW-ACCESS-r4.md`, `91934582…`).
  - r5 applied that review. It was reviewed ACCEPT WITH NITS, with no blocker (`review/REVIEW-ACCESS-r5.md`,
    `5fe0ec53…`).
  - r6 applied N1–N4. It was reviewed REVISE (`review/REVIEW-ACCESS-r6.md`, `d44ecc06…`), with one blocker present
    since r1.
  - r7 applied that blocker and N1–N2. It was reviewed REVISE (`review/REVIEW-ACCESS-r7.md`, `947bd3b0…`).
  - r8 applied B1, B2 and N1–N4. It was reviewed REVISE (`review/REVIEW-ACCESS-r8.md`, `553e90bb…`).
  - r9 applied B1, B2, N1 and N3, and the owner's restated requirements. A new reviewer reviewed it REVISE
    (`review/REVIEW-ACCESS-r9.md`, `d7e95d74…`).
  - r10 applied B1–B4 and N1–N7. It was reviewed REVISE (`review/REVIEW-ACCESS-r10.md`, `3431a98a…`), with three
    blockers.
  - r11 applies those blockers and N1–N5, on the owner's decisions #1169 c.6726548830 (amaybaum,
    2026-11-08T20:14:37Z). It was reviewed REVISE (`review/REVIEW-ACCESS-r11.md`, `22d9cda8…`), with two blockers.
  - r12 applied B1–B2 and N1–N9. Its independent review was ACCEPT WITH NITS (`review/REVIEW-ACCESS-r12.md`,
    `ba2ac209…`).
  - r13 applies those nits N1–N6 and changes nothing else. It is not yet reviewed. Earlier files are kept in `r1/`
    to `r12/`.
- **Snapshot.** `main@2cd49dc082ee7b2a026fd6d1fb4a6168f92fac51`.
- **Not done.** Nothing was pushed, committed, dispatched or designated, and there was no GitHub write. F1 was not
  built, and no `G_SM` census was computed.

**Sequencing.** ARP-3 executes after ARP-2, which follows ARP-1 (#1169 c.6723277401, c.6723329527, c.6724832474). The
owner's words: "neither the unfinished M-ARC CI nor Q-C2-2's draft status authorizes a freeze or scientific
execution." The owner wants the final reviewed preregistration and the resource evidence at the freeze gate.

## 1. The round in one table

| item | choice |
| --- | --- |
| round | `ARP-3-QC22`, non-sealing; digest `9f3808ac33d65a27dc363a88a0d0e7df16c77fa33f49d2c0f22b0df279b049b6` |
| tokens | `IMITABLE`, `CONTEXTUAL-{S}` (`S` ⊆ {RG, RUP, RY, RS}, or `NONE`; RS dropped if R-S is out of scope), `VOID` |
| derived fields | R-Uc's verdict; `g_specific := RY ∧ ¬RUc` and `g_eta := RU′ ∧ ¬RUc`, rendered as tests ("R-Y restores and R-Uc does not: yes/no") with a frozen caveat on "no". `decide` recomputes them; `verdict` prints a `DERIVED` line; they never change the token |
| method | (1) effect reduction; (2) rank fast path; (3) sufficient test; (4) reduced state-facet LP via its Farkas system; (5) Bareiss pivoting with frozen tie-breaks; (6) deterministic budgets `P_max`, `B_max` and `W_max` (work), with `out_of_scope` → VOID |
| verifier | the `v_*` namespace; C-INDEP (AST); it re-derives `N`, checks `A Bᵀ = N` and the ranks, re-enumerates the facets, and checks every certificate by definition |
| resources | `timeout-minutes: 60` on each job. `--stress` writes `stress.json` v2, covering every non-F1 fragment (stress fixtures, frozen fixtures with completions, CC-F0); it is uploaded on every event, and its sha256 is pinned and checked against the design run's artifact. The freeze rule is `3 × max` over all of these. The timeout test is `σ × (14·W_max + 2·W_fix + W_stress) + t_810 ≤ ⅓ × 3600 s`, which bounds each of the two jobs |
| pre-`F` runs | the design run (budgets measured) and the confirmation run 6′ (the exact S1 tree; `pull_request` runs, so job B is skipped and job A runs fixture mode by A3's literal; the final budgets and pin for 6′, pinned); the gate tests GT-1 to GT-6 (GT-2b and GT-7 when their options are adopted) on the gate-test branch. Fixture mode exits 3 on any mismatch with a frozen expectation |
| enforcement | **primary:** job B carries `environment: arp3-qc22-decisive` (one required reviewer, the identity fixed by owner decision E-ID; the Environment is read through the channel fixed by E-READ, since this session's proxy refuses the Environments API; optional preventive commit binding B3b under E-BIND; deployment branches: the round and gate-test branches only; `can_admins_bypass: false`), created by the owner before the splice is pushed, read by control N at S1, `E` and `verdict`, and tested by GT-1 to GT-6 (plus GT-2b and GT-7 when their options are adopted). **Defence in depth:** job B's `if:` (dispatch, attempt 1, input true); B3 (commit equals input, no receipt); the workflow keys in B4 and B6; the checker's three keys and the builder's refusal; W and B. **Detection:** every checker-bearing attempt (by name or pinned blob) of any workflow, under dispatch over the whole history and under any other event from `T0`, must be an approved entry, a gate-test entry, a non-computing re-run, or a fixture-mode run at a recorded-branch commit; otherwise VOID |
| approval | the owner's PR comment plus the deployment review (`GET actions/runs/{id}/approvals`: approved, amaybaum, the Environment, comment `ARP-3-QC22 <stage> <commit>`), bound to `head_sha`, B3, `parameters.dispatch_sha`, the input, and attempt 1; every deployment of the Environment maps to an entry |
| host VOID | B4 never ran in attempt 1 of an approved dispatch (job B absent, B4 absent or skipped: a rejection, an expiry, a policy refusal or a B3 failure). Any timeout, crash or `out_of_scope` after B4 started is a checker outcome: VOID, no retake. A re-run never attests |

## 2. What changed in r5

- **B1.**
  - Specificity is rendered as a test, with a frozen caveat that a "no" does not show independence from `g`'s law.
  - The NONE addendum no longer says where the degeneracy lies.
  - Fixture GX (two causes) is frozen as `CONTEXTUAL-NONE`, with both tests "no".
  - An ADA row marks "no" as not attributed.
  - Paired completions are an owner decision before `F`, and not adopted.
- **B2.**
  - The budget maxima are taken over every non-F1 fragment, and `--fixture-output` exits 3 on any mismatch.
  - Confirmation run 6′ runs the exact S1 tree with its one substitution, with the final budgets and pin. Its run id
    and record are pinned.
  - The writer's own code therefore reproduces every fixture expectation in CI before `F`, including the base
    infeasibilities, X+R-Y and GX. This removes the circularity.
- **B3.**
  - The hidden-law sentence has two frozen forms, and the RS-dropped form replaces the original rather than appending
    to it.
  - A-SWITCH has two entries.
  - The RS drop applies to F1's alphabet only, so SW and SW− keep R-S.
  - The RS-dropped note path is self-tested.
- **N1–N7.**
  - N1: `decide` recomputes the derived fields, and there is a `DERIVED` line.
  - N2: the C-INDEP whitelist, with certificates passed as canonical JSON.
  - N3: the mutations are invalid by construction (`W ← −W`, `W + cI`, +1 on a weighted `ξ`, +1 on `A[0][0]`), and
    M-BUDGET adds ZPT (step 3) with an in-loop bound.
  - N4: Q+RY is the step-4 feasible case with `T = 5`, and C-NCF's step-4 runs are verified.
  - N5: the timeout test adds `t_810`, and `W` is called a proxy.
  - N6: step 7 enforces the schema and certificates on every tree, and the pin is checked against the artifact.
  - N7: `PENDING` fields for the timeout inputs and the confirmation run.

## 2a. What changed in r4

- **B1 (owner: no misleading negative).**
  - R-Uc keeps the joint law of `(g, η)`; `g_specific := RY ∧ ¬RUc`; `g_eta := RU′ ∧ ¬RUc`.
  - Fixtures frozen: G → `CONTEXTUAL-RY` (specific); X → `CONTEXTUAL-RUP` (not specific); Q → `CONTEXTUAL-RUP+RY`
    (specific and `g_eta`).
  - H3 is unchanged.
  - ADA rows are re-attributed to A-SPLIT; A-P2 is not varied.
- **B2 (owner: independent certificate validation).**
  - C-INDEP.
  - The verifier's re-derivation of `N` and its factorization check.
  - Mutations M-W, M-MODEL (steps 2, 3 and 4), M-SOLVER, M-FACTOR and M-INDEP.
  - M-FACET retargeted to step-4 fragments (POS-1, GBIT, DUAL, H3).
  - New fixtures F10 (step 4 feasible), ZPT (step 3) and X+RU′.
- **B3.**
  - `--stress` is in the mode list and the frozen workflow. `stress.json` is uploaded on every event, and a marker step
    checks its pinned sha256.
  - The timeout is frozen. A deterministic work counter `W_max` is added.
  - The freeze rule is exactly 3 × the maximum, and the timeout test is mechanical.
  - The host VOID is defined, so a timeout cannot be retaken.
  - C-BUDGET is no longer circular, and M-BUDGET drives the `out_of_scope` path.
- **B4 (owner: R-S preference).**
  - Both options are kept for the owner's freeze decision, with the owner's preference recorded.
  - The RS-dropped forms of the common clause and of the NONE addendum are frozen, so a scope cut never reads as a
    result.
  - A narrowed R-S is a revision with SF-3n, its scope and its controls, reviewed under precondition 4.
  - After `F`: no narrowing, no budget change, no re-run.
- **N1–N7.**
  - N1: EXP's "equivalently" is restricted.
  - N2: the ADA attributions.
  - N3: the ladder is printed as its three rows only.
  - N4: SW is a decision-path check only.
  - N5: field hygiene. The herald is `u_{−1}(3)`, the ACCESS version is r4, descriptive mentions of `PENDING` are
    backticked, and control P matches unbackticked `PENDING`.
  - N6: the tie-breaks; step 3 shares the budget; `s_j` replaces `t_j`.
  - N7: the block rendering is any-branch, with L1 and EXP.

## 3. Controls run in preparation (scratch; controls, not evidence)

| file | sha256 | result |
| --- | --- | --- |
| `controls/ctl_pstar_table.py` | `71decb7e…a1e2` | P★ exact |
| `controls/ctl_paper_algebra.py` | `fec92403…6db0c` | Proposition F0; the dual-gbit facets; H3's rectangle |
| `controls/ctl_r2_fixtures.py` | `9c15f3d3…39f5` | not independent: imports the reviewer's `nclp.py` |
| `controls/ctl_r3_fixtures.py` | `0227e23b…8de33` | R-U′ hulls; H3 + R-Y rank; SW rank; F0 facts; F-10 |
| `controls/ctl_r11_allowlist.py` | `30d9f6825c8e63e36fd496fe9eaefaa817fa619193a63dd79cac614896cd3f82` | the writer's own AST reading of r11's control-B rules (no import of the reviewer's probe). It catches BYP-1 to BYP-18, `--textconv`, an `a_ok` before `--end-of-options`, a `POST …/pending_deployments` and a rebinding of `subprocess`. It admits the intended `git`, `gh` and read forms. `a_ok` rejects `--output=…`, a leading `-`, `=`, `..`, whitespace, `~` and `@{`, and admits HEX40, DEC, TIME, PATH and HEX40:PATH. Snippets are parsed, never run. **Also, local git 2.43.0:** every admitted subcommand accepts `--end-of-options`, but `rev-parse` without `--verify` echoes it literally, so the prereg requires `--verify` and output checks |
| `controls/ctl_r12_allowlist.py` | `dd4c200ef03c691664a9c147fec8d6b3a5d9338b630fbf33f98a093cfa05aefa` | extends the r11 control with the r11 review's N1: catches BYP-19 (`--filters`), BYP-20 (rebinding `a_ok`, a second `def w_path`, `a_ok` as a loop target) and BYP-21 (`help`), and still admits the intended forms. Parsed, never run |
| `controls/ctl_r13_allowlist.py` | `65a0696d526e2abcd164a5602174379eb6036b1c5253f6b2b7a6f80142c20fce` | extends the r12 control with the r12 review's N1. Helper names may appear only as `Load` names apart from their single top-level `def`. It catches BYP-23 (walrus), BYP-24 (`match` capture), BYP-25 (`except … as`), BYP-26 (`class`), a `match` as-pattern, and a `w_path` name that is non-literal or contains a `/`. It still admits the intended forms. Parsed, never run |
| `controls/ctl_r4_fixtures.py` | `19962f24e3c3ce7acd6be3c5cea116203803de8bdc7ef1af031a7b039f38c5b3` | G, X, Q: charged-point ranks and the first applicable step; R-Uc is the centroid in G and Q; Q's conditional law; F10 → step 4; ZPT → step 3. No LP and no reviewer code |

LP verdicts not derivable from ranks or hulls (X + R-Y infeasible, and every base infeasibility) rest on the reviewers'
independent exact probes (`review/probes3/`).

## 4. Cost

- **On paper.** F1 `d ≤ 6`; R-G `≤ 7`; R-U′/R-Uc `≤ 8`; R-Y `≤ 10`; R-S at most 16 generators.
- **The reviewer's r2 timings (`Fraction` tableau; synthetic).** F1-scale under 1 s; R-Y-scale 287–578 s; R-S-scale not
  finished in over 20 minutes.
- **What decides.** The frozen method (fast path, sufficient test, Bareiss) is measured on SF-1 to SF-3 in the design
  run. The mechanical rules then fix the budgets and test the 60-minute timeout. If SF-3 is out of reach, the owner's
  stated preference is out of scope.

## 5. Steps to `F` (none taken)

1. ARP-1 and ARP-2 complete and are reviewed; revise and re-review if ARP-2 bears on this round.
2. **Owner decisions, recorded on #1169:**
   - whether to run F1;
   - O-1, O-2 and O-3;
   - the gate's F-2 guard;
   - the audit package;
   - F1+R-S's scope: kept, out of scope (preferred if undecidable) or narrowed with review;
   - (named only) the floating-point basis option;
   - paired completions (for example R-Y+R-S, or R-Y+R-Uc): not adopted; frozen before `F` only by a reviewed
     revision, if wanted.
3. Independent review of the candidate revision, to an independent ACCEPT (c.6726548830, item 5), including any
   narrowing or paired completions.
3a. **Owner decisions E-READ, E-ID and E-BIND** (prereg precondition 2b), then the **owner action**: create the
   Environment `arp3-qc22-decisive` with the frozen settings (precondition 2a) before any ref carrying the splice is
   pushed. The session makes no settings write and cannot read the Environments API (r11 H17). The pin
   (`env-pin.json`, with `id`, `created_at` and `updated_at`) comes through the E-READ channel.
4. Write the scripts on a staging branch, run the self-tests and every mutation, then run the design run with
   `--stress` and step 3 in fixture mode, both of which must exit 0. Retrieve `stress.json` through the artifacts API, then apply
   the freeze rule (maxima over every non-F1 fragment) and the timeout test. Then run the confirmation run 6′ with the
   final budgets and pin, and pin its record. Then, with a recorded owner authorization for each launch, run the gate
   tests GT-1 to GT-6 (GT-2b under E-BIND, GT-6b optional, GT-7 under E-ID (ii)) on the gate-test branch (the input sha is forty zeros, so no gate test can reach B4), and pin
   `gate-tests.json`.
5. Open the round PR from `D` and the design branch. Pin the blobs, `design-run.json`, `stress.json`, the anchors and
   the drift extension.
6. Run precondition 7's command, obtain the `F` dispatch approval, then present the candidate `F` with its resource
   evidence for designation.

After `F`, the sequence follows M-ARC. Any failed gate halts, and ARP-4 does not start.

## 6. Open questions (left open as instructed)

- **Q1.** Whether to run F1.
- **Q2.** O-1, O-2 and O-3.
- **Q3.** F-2, the gate's preparation-side guard.
- **Q4.** F1+R-S's scope, following the owner's preference.
- **Q5.** The floating-point basis option.
- **Q5a.** Paired completions, to measure `g`'s contribution beside a second cause (re-review r4 B1).
- **Q6.** The correction to M2D's ledger (F-4).
- **Decided by the owner (c.6726548830; formerly Q7–Q11).**
  - No run deletion until Q-C2-2 closes.
  - The two landing gaps are not accepted; they are closed by the Environment gate for runs of the frozen splice.
  - A re-run never attests.
  - The Environment gate is adopted.
  - The freeze waits for an independent ACCEPT and for the verified gate.
- **Q12 (raised by the decisions; for the owner).** The gate covers runs of the frozen splice. It cannot cover a
  modified workflow on another branch that omits `environment:`; the enumeration detects such runs, by pinned blob or
  frozen names, only up to the final capture before landing. After landing nothing detects them. F1's output is
  public from `E`, and the landed record is protected by `G13`. Is that scope limit acceptable as the reading of "must
  remain blocked, including after landing", or does the owner want a further measure outside the round? One example
  is a repository rule restricting workflow-file changes. Whether a ruleset of that kind is available for this
  repository is **unverified** (r11 N9).
- **Q13 (the identity limit; neutral; prereg precondition 2b, E-ID).** The session acts as `amaybaum`. The options:
  - **(i)** A required reviewer whose credential the session does not hold: a second owner-controlled account added
    as a collaborator, with `prevent_self_review: true`.
    - A team is not available, because the repository is user-owned.
    - Whether a second personal account is consistent with GitHub's account terms is unverified, and the owner's to
      check.
    - The host then refuses approval by the session's credential.
    - Environment edits by the session's administrator credential stay procedural, and are detected if they persist.
    - The session can still dispatch with inputs, but such a dispatch only waits for a review.
  - **(ii)** A rule on the agent proxy refusing `POST …/pending_deployments`, the review endpoint and Environment
    writes for the session's credential.
    - It is unverified. GT-7 would test only its review half, by an owner-authorized rejection attempt, which is a
      harmless host write if the rule is absent.
    - It does not reach the GitHub MCP connector the session also holds. That connector has no review or
      Environment method today, but it can dispatch, re-run, cancel and delete logs.
  - **(iv)** Change the session's identity instead of the reviewer's: a GitHub App or machine-account credential for
    the session, with `amaybaum` as the sole reviewer and `prevent_self_review: true`.
    - Its effect on approval is the same as (i).
    - Edits depend on the permissions given to the session's identity.
  - **(iii)** Accept the procedural limit: reviewer `amaybaum`, `prevent_self_review: false`. The host cannot tell
    the owner's approval from the session's.
- **Q14 (E-READ; neutral).** Who reads the Environment's settings: (a) a CI step in job A (token scope unverified;
  GT-6), (b) the owner posting the canonical JSON and its sha256, or (c) the owner permitting the two `GET` paths for
  the session's proxy.
- **Q15 (E-BIND; neutral).** Whether to add B3b, an in-job check that the run's approval names its own commit
  (preventive; token permission unverified; GT-2 and GT-2b).
- **Stated consequences of the decisions.** The Environment stays unchanged until Q-C2-2 closes. With no re-run
  attestation, a flaky job anywhere in attempt 1 of the S1 or `E` dispatch halts the round VOID.

## 6h. Disposition of `REVIEW-ACCESS-r12.md` (r12 → r13; ACCEPT WITH NITS)

| finding | disposition | where |
| --- | --- | --- |
| N1 | (c″) is restated: apart from their single top-level `def`, helper names occur only as `Load` names, and no node binds them (walrus, `match` capture or as-pattern, `except … as`, `class`, comprehension target and the forms already listed). `w_path`'s file name must be a literal matching `[A-Za-z0-9_.-]+`. M-GUARD adds BYP-23 to BYP-26 and two `w_path` variants (writer's control `ctl_r13_allowlist.py`) | prereg control B (c″), (d), M-GUARD |
| N2 | Every splice interpreter (A3, A5, A7, A8, A9, A11, B3b, B4, B6) is `python3 -I -S -B` | prereg workflow steps, *Common* |
| N3 | Control N's timing is stated by channel. Under (b) and (c) the reads come before each dispatch. Under (a) the S1 and `E` reads are A11 artifacts of those runs, so they are detection after the fact at `check --stage E` and at `verdict`, with an optional extra read through (b) | prereg control N |
| N4 | GT-7 is the single owner-authorized exception to 2a's commitment, with a frozen request body. If the rule is absent, it is a harmless host write (a rejection review, a red gate-test job B, recorded, (ii) not verified). Its Environment-write half is untested. A proxy rule does not reach the MCP connector. 2a gains the MCP channel: no dispatch, re-run or cancellation without authorization; no run or log deletion (log deletion listed under the no-deletion commitment); and the enumeration and the order rule cover runs whoever initiates them | prereg 2a, 2b E-ID (ii), 6″ GT-7, *Enforcement* |
| N5 | E-ID (i) drops the team option (the repository is user-owned) and marks the account-terms question unverified and the owner's. A new option (iv) changes the session's identity (an App or machine account) and keeps `amaybaum` as reviewer with `prevent_self_review: true`. 2a's reviewer and `prevent_self_review` follow (iv) | prereg 2a, 2b, *Enforcement*; PLAN Q13 |
| N6 | Under (i), the session can still dispatch with inputs, but such a dispatch only waits for a review | prereg 2b E-ID (i); PLAN Q13 |

`PENDING`: unchanged, 29 markers carrying 37 values. Nothing else is changed.

## 6g. Disposition of `REVIEW-ACCESS-r11.md` (r11 → r12)

| finding | disposition | where |
| --- | --- | --- |
| **B1** (Environment unreadable here) | Control N no longer assumes a direct session read. A new neutral owner decision, E-READ, offers three channels, each specified exactly: (a) CI step A11 in job A (`controls.py env-read`, `GH_TOKEN`, job-A `permissions:` with the scope unverified, `env.json` artifact, skipped on receipt-carrying trees, pinned by W); (b) the owner posts the canonical JSON and its sha256 on the round PR, read through the issue-comments API; (c) the owner permits the two `GET` paths for the session's proxy. GT-6 verifies the chosen channel; under (a) by a one-time cross-check against an owner-posted read. The frozen fields gain `id`, `created_at` and `updated_at`; optional GT-6b tests whether `updated_at` moves | prereg control N, preconditions 2a, 2b, 6″; W; modes |
| **B2** (identity limit) | Both invariant rows (requirements 1 and 3), *Enforcement* item 1 and *After merging* now say "prevented for every account other than `amaybaum`", and that against the credential the session holds, approval and edits are held back by the owner's procedural commitment, not by the host. A new neutral decision E-ID offers (i) a reviewer the session does not hold, with `prevent_self_review: true`; (ii) a proxy rule (unverified; GT-7, a harmless reject attempt on an all-zero-input deployment, owner-authorized); (iii) accept the limit. Precondition 2a's reviewer and `prevent_self_review` follow E-ID. PLAN Q13 is rewritten neutrally | prereg control B identity paragraph, *Enforcement*, *After merging*, invariant rows, preconditions 2a, 2b, 6″; PLAN Q13 |
| N1 | `--filters` forbidden; (c″) `a_ok`, `w_path` and the root check bound once by a top-level `def`, never rebound, never a parameter or a target; `help` added to (c); BYP-19 to BYP-21 added to M-GUARD (writer's control `ctl_r12_allowlist.py`) | prereg control B, M-GUARD |
| N2 | `id`, `created_at` and `updated_at` are pinned and compared; `updated_at`'s behaviour is unverified until GT-6b | prereg control N, 2a, 6″ |
| N3 | A self-test drives the entry with B4's argument forms (`--event closed-or-other --dispatch-sha <hex>`), expecting fixture mode and the recorded sha; a malformed sha exits 4 by the checker's own check (not `a_ok`). It runs as A8 in the design run and in 6′. Residual stated: the host's evaluation of B4's expression is first exercised at S1 | prereg *Scripts*, M-GUARD |
| N4 | B3's sentence is reworded (it stops a mismatch with the input only). The preventive in-job check B3b is offered neutrally as E-BIND, with GT-2 and GT-2b | prereg B3, B3b, 2b, 6″ |
| N5 | The review is bounded between the deployment's `waiting` status and its next `queued` or `in_progress` | prereg approvals |
| N6 | B6 has no design-run step record, so its id is "none" and its term 0; `t_810` sums A8 and A9; the step-id field names A5, A8 and A9 | prereg *Method* timeout test, precondition 6 |
| N7 | Precondition 4 states that "ACCEPT of r10" is read as an ACCEPT of the candidate revision, as the coordinating session's interpretation, which the owner can correct | prereg precondition 4 |
| N8 | Set (2)'s bound is checked: each recorded-branch commit carrying the blob or the names descends from `D` (`merge-base --is-ancestor`). The residual is stated: a draft pushed before `D` elsewhere is outside set (2), and that is empty on the writer's record | prereg enumeration |
| N9 | Q12's ruleset example is marked unverified | PLAN Q12 |

`PENDING`: 29 unbackticked markers (37 values). The new marker is precondition 2b's record id. The step-id field now
carries three values (A5, A8, A9), not four. The frozen texts, method, fixtures, ADA, C-INDEP and decision rule are
unchanged.

## 6f. Disposition of `REVIEW-ACCESS-r10.md` (r10 → r11) and of the owner's decisions c.6726548830

| finding | disposition | where |
| --- | --- | --- |
| **c.6726548830 item 4** (Environment gate) | **Two jobs.** Job A (fixtures, stress, self-tests, marker) runs on every event, has no Environment, and A3 is hard-wired to `--event fixture`. Job B (`probes_arp3qc22_decisive`) carries `environment: arp3-qc22-decisive`, a job-level `if:` (dispatch, attempt 1, `inputs.arp3qc22_decisive == true`), the input `arp3qc22_sha` passed through `env:`, and B3 (`$GITHUB_SHA` equals the input; no receipt). Then come B4 (decisive) and B6 (replay). New `workflow_dispatch` inputs. The aggregate accepts job B `success` or `skipped`; `verdict` requires `success` at S1 and `E`. **Enforcement** is stated in order: the gate is primary, the in-tree keys are defence in depth, and enumeration with VOID is detection. **Environment settings** are frozen (precondition 2a): one required reviewer (amaybaum), `prevent_self_review: false` (with the reason), no wait timer, no custom rule, `can_admins_bypass: false`, and two exact branch policies. The owner creates it before the splice is pushed, because a missing Environment is auto-created unprotected. Control N re-reads it at S1, `E` and `verdict` against `env-pin.json`. **Approval evidence:** the approvals API record (approved, amaybaum, the Environment, frozen comment `ARP-3-QC22 <stage> <commit>`) is bound to `head_sha`, B3, `parameters.dispatch_sha`, the input and attempt 1; every deployment of the Environment maps to an entry; the order rule bounds the review between `created_at` and job B's start. **Identity:** the session never calls the review endpoint, and `POST …/pending_deployments` is a named M-GUARD variant; the host cannot tell owner from session, stated as a residual | prereg *The workflow edit*, *Enforcement*, control N, *Runs, evidence, approvals*, preconditions 2a, 6, 6′ |
| **item 2** (landing gaps) | Closed for runs of the frozen splice. On `main`, the branch policy refuses job B, and B3 and the receipt key also stop it. At pre-`Q` round commits the owner's approval is required. The two r10 residual paragraphs are replaced | prereg *After merging*, *The window*, invariant row 3 |
| **item 3** (re-runs) | A re-run never attests. Job B is skipped on attempt `≥ 2`, before the Environment is consulted (GT-4). An attempt `≥ 2` whose job B ran is VOID. `verdict` reads attempt 1 only. Q10 and its consequences are removed (r10 N5); the remaining consequence (a red job in attempt 1 halts) is stated | prereg approvals, `verdict`, invariant row 2; PLAN Q13 |
| **item 1** (no deletion) | Recorded as decided; it anchors the enumeration's completeness | prereg precondition 2, enumeration residual |
| **item 5** (freeze readiness) | Precondition 4 requires an independent ACCEPT. New precondition 6″ verifies the complete gate with GT-1 (rejection), GT-2 (approval with a wrong commit, B3 stops it), GT-3 (branch policy), GT-4 (re-run skipped) and GT-5 (ordinary dispatch). Every gate-test dispatch uses an all-zero input sha, so B4 is unreachable. `gate-tests.json` is pinned | prereg preconditions 4, 6″; invariant rows |
| **B1** (allowlist) | (c′) `subprocess.run` and `open` only as a call's `func`, and `subprocess` and `open` never rebound; no `cwd=` at all, with the entry refusing unless `git rev-parse --show-prefix` is empty; `--ext-diff` and `--textconv` forbidden; `--end-of-options` before the first `a_ok` element, with only `a_ok` elements after it; `rev-parse` with `--verify` (writer's control: git 2.43 echoes the option otherwise); `a_ok`'s five patterns stated, none admitting a leading `-`, `=`, whitespace or `..`; BYP-13 to BYP-18 added to M-GUARD. **B's claims are scoped to what it checks**, and the Environment, not B, is the primary enforcement | prereg control B (c′), (e), (f), (g), (h), M-GUARD; `controls/ctl_r11_allowlist.py` |
| **B2** (builder reference) | Exactly two `Name` references: the default entry and `t_builder_refuses`, in a frozen `try` form. It is safe because A8's real argv has no `--event`, so `s_mode` refuses and the builder raises at its first statement. M-GUARD adds a second self-test reference, and a changed `t_builder_refuses`, as variants that must fail B | prereg *Scripts*, control B, M-GUARD |
| **B3** (blob search) | Trees are read from the object store, else from `GET git/trees/{sha}?recursive=1` with `truncated == false`, walking subtrees on truncation. The source is recorded per `head_sha`. An unreadable tree is a failed capture, to be retried, never "not checker-bearing"; a persistently unreadable one halts the stage. Trees are read once per distinct `head_sha` | prereg enumeration |
| N1 | Every listed attempt is read; only checker-bearing attempts can be violations | prereg enumeration |
| N2 | The gate's reach is scoped to runs of the frozen splice everywhere it is claimed. Unverified host behaviour is named: administrator bypass with `can_admins_bypass: false`, pending-review expiry, and re-approval on re-run (not relied on) | prereg *Enforcement*, scope paragraph, precondition 2a, invariant rows |
| N3 | Jobs are read through `GET actions/runs/{id}/attempts/{n}/jobs?per_page=100`, every page; `filter=all` is not used | prereg enumeration |
| N4 | The call budget is stated (about 770 calls per capture for dispatches, plus set (2)'s runs since `T0`, at about 100 runs a day; three captures). A rate-limit or 5xx response is a failed capture, to be retried | prereg enumeration |
| N5 | Q10 is decided ("no"), and its consequences are dropped; `verdict` names the conclusions it reads | prereg `verdict`; PLAN §6 |
| overall design (coordinator) | **Detection now covers any event.** Set (2) lists every non-dispatch run of every workflow from `T0`. A checker-bearing attempt at a commit outside the recorded branches, under any event, is VOID. So a run that bypassed both the in-tree keys and the gate is still caught, up to the final capture, provided it carries the pinned blob or the frozen names | prereg enumeration rule (a)–(d) |

`PENDING`: 28 unbackticked markers (37 values). The 5 new ones are the two branch names, the `env-pin.json` sha256,
the owner-commitments record id and the `gate-tests.json` sha256. The frozen texts, method, fixtures, ADA, C-INDEP and
decision rule are unchanged, so the S4 screen's inputs are unchanged.

## 6e. Disposition of `REVIEW-ACCESS-r9.md` (r9 → r10)

| finding | disposition | where |
| --- | --- | --- |
| **B1** (regression in step 8) | Step 8's `if:` is now the same compound condition as step 3's decisive branch (event, attempt and receipt keys). W pins it, M-GUARD's splice variants remove each key from step 3 and from step 8, and the cost paragraph is corrected: a dispatch after landing is green and fixture-only | prereg workflow steps 3 and 8, control W, M-GUARD, cost paragraph |
| **B2** (whitelist not closed) | Control B is a node-form allowlist. `controls.py` uses only `import X` from a frozen list (no `as`, no `from`), with per-module attribute lists (so no `os.path.os`, `sys.modules`, `subprocess.os`). Reflective builtins and `__*__` names are banned except the single main-guard statement. Every read is a literal-mode `open`, and the only write is in the self-test, under a `TemporaryDirectory` through `w_path`. Every process start is `subprocess.run` with a list display of literals or `a_ok(...)` validator calls, and no `shell`, `env` or `executable`. `git` takes a frozen read-only subcommand list, with no `-c`, `--config-env`, `--exec-path`, `-C`, `--git-dir`, `--work-tree`, `--upload-pack` or `--output`, and `--no-textconv --no-ext-diff` on `show` and `diff-tree`. `gh` is exactly `api --method GET <templated path>` plus frozen options, so no `--input`, graphql, `-f`/`-F`, or other `-X` or `--method`. Control T runs `python3 -I -S`; an isolated `cwd` is impossible, as stated. In `qc22_check.py`, reflection and dunders are banned module-wide, the builder's name is referenced only in the default entry, and the builder refuses unless `s_mode` is decisive. M-GUARD adds BYP-1 to BYP-12 and the `qc22_check` alias, `globals` and `getattr` variants. The claims are restated as holding under these rules for the frozen blobs | prereg *Scripts*, control B, M-GUARD |
| **B3** (identification) | Display name frozen (`Numerical probes / ARP-3-QC22 exact noncontextuality LP`). Checker-bearing means a job with that name, a step "ARP-3-QC22 exact decision" in any job, or the pinned blob at any path in the tree, checked on every attempt, conservatively and whatever the conclusion. The host VOID is defined by conclusions (job or step 3 absent, or step 3 `skipped`), never `started_at`. Re-runs of old runs are covered by listing the whole history from the repository's creation. The enumeration covers all workflows (`/actions/runs?event=workflow_dispatch`) | prereg *Runs, evidence, approvals*, stop rule |
| **B4** (requirement scope) | (a) The attempt key in step 3 and step 8, plus a third checker key `GITHUB_RUN_ATTEMPT`, so a re-run is fixture-only; retakes are fresh dispatches with their own approval; any attempt ≥ 2 of an approved dispatch is VOID until the owner decides (Q10). (b) Invariant rows narrowed: requirement 1 by detection and VOID; requirement 2 prevented; requirement 3 on `main` and receipt-carrying trees, with the pre-`Q`-ref residual stated. (c) The Environment gate is offered neutrally (Q11) | prereg step 3, `s_mode`, approvals, invariants, precondition 2 |
| N1 | The stale `github.event_name` row is replaced | prereg invariants |
| N2 | `total_count` read from page 1, consistent across pages, equal to the listed count and below 1,000; slices disjoint at one second, union recorded, deduplicated by `id` | prereg enumeration |
| N3 | W checks `verify.yml` as a whole file at the design run, 6′, S1 and `E` | prereg control W |
| N4 | `T0` is the `timestamp` of the activity-API entry with `after = D`; it is now the anchor of the deletion commitment | prereg enumeration residual |
| N5 | New neutral owner decisions: the pre-landing residual, post-landing pre-`Q` dispatches, re-run attestation, and the Environment gate. The final capture is provenance; validity rests on `E`'s `order.json` and the receipt | prereg precondition 2, after-landing paragraphs |
| N6 | Marker step 11, "ARP-3-QC22 receipt absent", with `if: hashFiles(...) == ''`. It must be `success` in `design-run.json` and `confirmation-run.json` (`check --freeze`) | prereg workflow step 11 |
| N7 | Scope sentence narrowed to the frozen splice and the pinned checker; modified workflows elsewhere and local runs are named as outside, with only the dispatch case detected | prereg "Which steps" |

`PENDING`: 23 unbackticked markers (32 values); `T0` is kept as the deletion commitment's anchor.

## 6d. Disposition of `REVIEW-ACCESS-r8.md` (r8 → r9)

| finding | disposition | where |
| --- | --- | --- |
| **B1(a)** (runtime second key) | Decisive mode needs `--event workflow_dispatch` **and** `GITHUB_EVENT_NAME == "workflow_dispatch"`, decided by the pure function `s_mode(argv, environ)`. Child processes inherit the variable, so an indirect call from a non-dispatch run gets fixture mode. `qc22_check.py` imports `os` for that single read only | prereg *Scripts* modes, step 3, control B |
| **B1(b)** (whitelist for `controls.py`) | Imports come from a frozen list, and importlib, runpy, imp, pkgutil, multiprocessing and any `os` attribute other than `os.path` are forbidden. Every process start is `subprocess.run` with a literal list whose first element is `"git"` or `"gh"`; the one exception is control T's frozen precondition-7 `python3` argv, which imports only `tools/v3_verifier.py`. Also forbidden: `shell=True`, `env=`, `os.system`, `exec*`, `spawn*`, `popen`, writes to `os.environ` or `sys.path`, and `exec`, `eval`, `compile`, `__import__`. Every `gh` call is `gh api` with GET, with no `-X` or `--method` other than GET, no `-f`/`-F`, and no `gh workflow` or `gh run`. Stated in prose: no control can create a dispatch (N2). In `qc22_check.py`, the literal occurs once, as the constant `DISPATCH_EVENT` | prereg control B |
| **B1(c)** (M-GUARD) | New variants that must fail B: a computed-path `subprocess`, `os.system`, and a `gh` POST or `gh workflow run`. `s_mode` and the entry with `--event workflow_dispatch` plus `GITHUB_EVENT_NAME=pull_request` give fixture mode with zero builder calls, and so does the converse. A splice without the receipt key fails W | prereg self-tests |
| **B2** (complete enumeration) | Queries per `created` window, paginated to the end. Listed count equal to `total_count` is asserted per query, with windows split below the 1,000 cap. Every query and count is recorded in `order.json`. Every attempt is read, with its jobs. Decisive executions are identified from the jobs API (job `probes_arp3qc22`, step "ARP-3-QC22 exact decision" with `started_at` not null), cross-checked by the pinned blob at any path. The window starts at a frozen `T0` (at or before `D`'s host time; a `PENDING` field) | prereg *Runs, evidence, approvals* |
| **N1** (regression) | Fixture mode exits 0 unless one of its three exit-3 conditions holds, whatever `complete` says; the default exit rule applies in decisive mode only | prereg *Method*, fixture mode |
| **N3** | Deleted-run residual stated. The owner commitment "no `verify.yml` run is deleted before `Q`" is listed as an owner decision at the freeze (precondition 2) | prereg precondition 2 |
| **Owner's restated requirements** | Four invariant rows. For "after merging to `main` … neither a push nor a new dispatch can silently execute F1": r8 still let a dispatch on `main` compute F1, so r9 adds **the receipt key**. Step 3 passes `workflow_dispatch` only if the tree carries no `verification/receipts/ARP-3-QC22.json`, so after `Q` lands every run is fixture mode. Also added: a final enumeration capture before landing, which covers dispatches between `E`'s capture and `Q`, with the small residual stated | prereg step 3, after-landing paragraphs, invariants |

`PENDING`: 23 unbackticked markers (`T0` added), carrying 32 values.

## 6c. Disposition of `REVIEW-ACCESS-r7.md` (r7 → r8)

| finding | disposition | where |
| --- | --- | --- |
| **B1** (re-runs, other refs) | Approval entries and `order.json` keyed on `(run_id, run_attempt)`; `derive-run` reads every attempt; `run_attempt = 1` for `F`, S1 and `E`; any further attempt halts with VOID unless a recorded host-VOID retake names it. Repository-wide enumeration of every `workflow_dispatch` run of `verify.yml`, on any ref and at any attempt, whose `head_sha` tree carries the round's `qc22_check.py` (via the git object store); each must be an approved entry, otherwise VOID. The design and confirmation branches are never dispatched. A dispatch on `main` after landing computes F1 without approval but does not affect validity: the round closes at `Q` | prereg *Runs, evidence, approvals*, stop rule, invariants |
| **B2(a)** (guard measurement) | Control B's static rule covers both scripts. `"workflow_dispatch"` occurs once in `qc22_check.py`, in the `--event` guard, and in `controls.py` only in the run-classification functions. That refinement is needed because the order rule must classify events. `controls.py` neither imports nor executes `qc22_check`, and `replay` only compares files. M-GUARD adds three variants that must fail B: an import-and-call, a `subprocess` call, and a second string occurrence | prereg *Scripts* (B), self-tests |
| **B2(b)** (`mode`) | `mode` is in the schema. `decide` gives VOID unless `mode = "decisive"`. Fixture output has `complete: false` and `lp: "placeholder"`, so it is decision-invalid on three independent conditions. M-MODE tests each condition alone | prereg schema, decision rule, self-tests |
| N1 | `retention-days: 90` on both uploads. `check --stage S1` captures the order records in `evidence/order-s1.json`, committed at `E`. A missing artifact at `E` counts as compliant only if `order-s1.json` holds its record; otherwise VOID | prereg workflow steps 4 and 6, *Runs*, objects (`E`), control R |
| N2 | `replay` recomputes nothing; the decisive computation is step 3's, which `14·W_max` covers | prereg "No automatic replay" |
| N3 | Post-landing cost stated: every PR and push runs steps 3, 5, 7, 9 and 10 in fixture mode, and every dispatch on `main` runs the 60-minute decisive job. Gating belongs to a successor change | prereg *The workflow edit* |
| N4 | A `workflow_call` trigger would be a route into decisive mode; none exists now | prereg *The workflow edit* |

## 6b. Disposition of `REVIEW-ACCESS-r6.md` (r6 → r7)

| finding | disposition | where |
| --- | --- | --- |
| **B1** (F1 computed on pull-request CI before any approved dispatch; present since r1) | **Chosen design: the event guard.** Step 3 runs `qc22_check.py --event "${{ github.event_name }}"`. The checker computes the F1 family only when `--event` is `workflow_dispatch`; any other event runs fixture mode (`mode: "fixture"`, placeholders), and a missing `--event` refuses with exit 4. Step 8 (replay) carries `if: ${{ github.event_name == 'workflow_dispatch' }}`, so there is **no automatic replay**: at `E` the only replay is the owner-approved `E` dispatch, and `main`'s push runs after landing compute and replay nothing of F1. Steps 5, 7, 9 and 10 compute nothing of F1; control B's AST check makes the default entry the only caller of the F1 builder. **Frozen:** control W checks the splice byte for byte, including both guards, and its self-test shows that removing either fails. M-GUARD (`--event pull_request` and `push` give fixture mode and zero F1-builder calls; no `--event` exits 4). Invariant row: "F1 is computed only under an approved `workflow_dispatch`". **Order-rule check (§A.44):** `order.json` lists every non-dispatch run at S1, `E` or later, with its event, the conclusions of steps 3 and 8, and its `measurements.json` artifact's sha256 and `mode`, from the jobs and artifacts APIs. The rule requires `mode: "fixture"`, placeholders only and step 8 `skipped`, and `verdict` re-checks it. Consequence: the design run and 6′ are the exact S1 tree; 6′'s `verify.yml` must be byte-equal to the splice, and `--fixture-output` is retired | prereg workflow steps 3, 4 and 8, the "which steps" paragraph, *Scripts* modes, `order.json` rule, control W, M-GUARD, invariants, preconditions 6 and 6′, objects (S1) |
| **N1** | C-STATELESS is evaluated by `controls.py check --stage E`; a mismatch is a failed check at `E`, so the round halts with VOID | prereg controls, precondition 6′ |
| **N2** | `design-run.json` records each step's `started_at` and `completed_at`. `check --freeze` recomputes `t_5`, `t_810`, `W_fix`, `W_stress` and σ from the pinned records and fails if the recorded values differ. Edge cases frozen: `t_5 = 0` → 1; `W_stress + W_fix = 0` → the test fails | prereg precondition 6 |

`PENDING`: still 22 unbackticked markers carrying 31 values. They are now recorded for reading and checked against
`check --freeze`'s recomputation.

## 6a. Disposition of `REVIEW-ACCESS-r5.md` (r5 → r6)

| finding | disposition | where |
| --- | --- | --- |
| **N1** | (a) `check --freeze` verifies `confirmation-run.json`: its sha256 against the pin, every job and step `success` (steps 3 and 7 included), the `head_sha` tree carrying the pinned script blobs, `verify.yml` equal to the splice apart from `--fixture-output` on step 3, and the stress artifact sha256 against the pin. (b) Tree differences between 6′ and S1 stated; no workflow step reads the differing record files. (c) `evidence/confirmation-run.json` and `evidence/confirmation-measurements.json` added to S1 and to control R. (d) Statelessness stated; C-STATELESS requires S1's `fixtures` section to be byte-equal to 6′'s. Step 4 uploads `measurements.json` on every event, so 6′'s step-3 output is retrievable. The design and confirmation branches are retained until `E`'s receipt | prereg objects, *Scripts* (R), workflow step 4, precondition 6′, controls, invariants |
| **N2** | `σ := t_5 / (W_stress + W_fix)`, an exact `Fraction` of integer step seconds. Test: `σ × (14·W_max + 2·W_fix + W_stress) + t_810 ≤ 1200`, with `W_fix` counted twice (steps 3 and 5). `check --freeze` evaluates it. Field `t_5` added beside `σ` (same marker) | prereg *Method* step 6, precondition 6 |
| **N3** | `DERIVED RUc_restores=… RY_restores_and_RUc_not=… RUP_restores_and_RUc_not=…` | prereg decision rule |
| **N4** | C-INDEP covers the whole `FunctionDef`: body, defaults, decorators, nested functions and lambdas. A runtime type check accepts only plain `dict`, `list`, `tuple`, `Fraction` and `int` for the non-JSON inputs. M-INDEP adds default-argument and closure variants | prereg C-INDEP, self-tests, invariants |

`PENDING`: still 22 unbackticked markers, now carrying 31 values (`t_5` added beside `σ`).

## 7. Disposition of `REVIEW-ACCESS-r4.md` (r4 → r5)

| finding | disposition | where |
| --- | --- | --- |
| **B1** | Renderings: "R-Y restores and R-Uc does not: yes/no", and "R-U′ restores and R-Uc does not: yes/no", each with a frozen caveat on "no" ("does not show … independent …; when several independent directions are degenerate, no single supplied completion restores"). The NONE addendum (both RS forms) now reads "may lie in several of the completed directions at once, or in others". GX frozen: `CONTEXTUAL-NONE`, both tests "no", R-Uc infeasible. ADA "no single completion restores" row: not attributed. §A.41 rows updated. Paired completions listed in precondition 2, not adopted | prereg renderings, CONTEXTUAL text, addenda, controls, ADA, invariants, precondition 2; ACCESS §6.3, F-13 |
| **B2** | (a) Freeze-rule maxima over every non-F1 fragment (stress, frozen fixtures with completions, CC-F0, self-tests); fixtures not exempt. (b) `--fixture-output` exits 3 on a verdict, step, derived-field or token mismatch, a failed certificate, or `out_of_scope`. (c) Precondition 6′: the confirmation run of the exact S1 tree (only `--fixture-output` substituted, keeping F1 unbuilt), final budgets and pin in force, green on every step, `confirmation-run.json` and run id pinned. A frozen fixture the design run cannot decide forces a reviewed revision before `F` | prereg *Method* step 6, `--fixture-output` paragraph, workflow note, preconditions 6 and 6′, invariants |
| **B3** | Common clause: `{hidden-law sentence}` with two frozen forms, the RS-dropped one replacing the original. A-SWITCH: two entries. §A.41 row cites both. The RS drop applies to F1's token alphabet only, so SW and SW− keep R-S. The self-test drives the RS-dropped note path, with S4 | prereg decision rule, common clause, ledger, invariants |
| N1 | `decide` recomputes `g_specific` and `g_eta` and VOIDs on disagreement; `verdict` prints `DERIVED RUc=… g_specific=… g_eta=…` | prereg decision rule |
| N2 | C-INDEP: the call whitelist (`v_*`, `Fraction`, `json.loads`, `itertools.combinations`, listed builtins, attribute calls on locals); `globals`, `locals`, `vars`, `getattr`, `setattr`, `eval`, `exec`, `compile` and `__import__` forbidden; the certificate and the solver's facet list reach the verifier only as canonical-JSON bytes (`cert_sha256`) | prereg C-INDEP |
| N3 | M-W: `−W` and `W + (1 − tr W/d) I`. M-MODEL: +1 on `ξ_e(j)` with `μ_p(j) > 0`. M-FACTOR: +1 on `A[0][0]`. M-BUDGET on GBIT and ZPT, with counters at the abort at most one pivot past the budget | prereg self-tests |
| N4 | Q+RY (`m = 6`, `T = 5`) named as the step-4 feasible case with `T > 0`, and added to M-MODEL; C-NCF's step-4 runs certificate-verified | prereg controls, invariants |
| N5 | The timeout test adds `t_810` (steps 8–10, measured); `W` is a deterministic proxy for tableau work; `σ` is an estimate; a timeout stays a checker outcome | prereg *Method* step 6 |
| N6 | Step 7 enforces schema v2 and the certificates on every tree; `check --freeze` verifies the pin against the design run's and the confirmation run's stress `artifact_sha256` | prereg `--stress` paragraph, precondition 6′ |
| N7 | `PENDING` fields: the design run id; the step ids of steps 5 and 8–10; `σ`; `W_fix` and `W_stress`; `t_810`; the confirmation run id; `confirmation-run.json`'s sha256. 22 unbackticked markers, carrying 30 values | prereg preconditions 6 and 6′ |

The r3 → r4 disposition is in `r4/PLAN-r4.md` §7.
