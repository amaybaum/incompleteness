# Independent re-review: Q-C2-1 r10 (ARP-2-QC21), with Appendix C and the D12 revision

**Reviewer.** The same independent model reviewer as r6–r9, 2026-11-09. Read-only, with `gh api` GETs only.

**Probes and checks** (in `review/probes-r10/`):
- One exact probe of supplied matrices only (C-R60-ODD's fixture).
- A line-by-line diff of Appendix C against QC22 r13.
- A sentence-level verbatim check of the authority fills against the comments.
- A read-only re-run of `--verify-round` for ARP-1.

**Owner inputs read:**
- c.6735014875 (the freeze decisions, 07:52:50Z);
- c.6735159962 (D12 waived for Q-C2-1, 08:02:29Z);
- the coordinator's relay of the owner's three acceptance conditions for removing D12.

## Verdict: **REVISE**

**Correct in r10:**
- The fills are correct.
- The owner decisions are applied faithfully.
- `ATTR` and `access_only` are sound in substance.
- The Lemma P and cone-argument withholding table is right.
- Appendix C is verbatim apart from the five declared renames.

**Blockers.** Five, and three of them concern the gated execution design:
- **R10-B1.** Appendix C is incomplete. The copied sections depend on controls, scripts, preconditions and gate tests
  that were not copied, so the frozen control plane is not self-contained (§A.42 item 8).
- **R10-B2.** QC22's guards assume one decisive builder. This round has many decisive families, and several P and C
  controls that evaluate them have no frozen job or mode, so they could run in ordinary PR CI.
- **R10-B3.** REP-INV cannot detect a resource supplied by an identification, because every alternative is a symmetry.
  The owner's D18 condition is unmet for L-UPRIME's effect on B-C contextuality.
- **R10-B4.** REP-INV's L-CAL variation falsely loses W-CL in 8 of 48 recalibrations unless the encoded transposition is
  transported (probe). That would reclassify a genuine C-EXPOSURE as a benchmark result.
- **R10-B5 (D12).** With the Environment waived, decisive computation after the final capture is neither prevented nor
  detected. The owner's condition 1 explicitly includes post-landing runs. Every claim of "prevented" that rested on the
  Environment must become "detected".

## Inputs verified

| file | sha256 | status |
| --- | --- | --- |
| `preregistration.draft.md` r10 | `656d2202a6fd9380356fd335931b1d02ca5709ffd58028e51f0b0abf1bfcde94` | matches |
| `PLAN.md` r10 | `d090cc6b304a49e8c3c791662e319bad0de3d38adba257cc89a28c52d160ad1d` | as given (`d090cc6b…`) |
| `DESIGN-DS.md` r10 | `81e102cc75039a3c0dab914cf5f51c8c9e2413918b69965c48b8728cf311f646` | matches |
| QC22 r13 source | `15d90b24496a733d87079256f4a3efb06f426bfaba775aa77e7bc2adda2f4dd2` | matches Appendix C's statement |
| `review/probes-r10/repinv_frame.py` | `213cff5fc73b47293219a74f2f74c7eb90cc0cff4d73be6e5a2133e3e22c5d6f` | reviewer probe (supplied matrices only) |

**Fills checked:**
- **ARP-1 blobs.** All six match `git rev-parse fd539e15:<path>`.
- **The verifier.** `tools/v3_verifier.py` at `fd539e15` has sha256 `fc6545f5…`. Re-run read-only (`is-shallow: false`),
  `--verify-round e064e766…` prints four `ATTESTATION … recorded, unverified` lines, then `VERDICT  HOLDS`, exit 0.
- **The authority passages.** r5's five passages (c.6723277401, …329527, …491138, …571280, …585151) and c.6733796760
  are verbatim at sentence level against the comments. So is the c.6735014875 block. Each comment's time and author
  association, `amaybaum OWNER`, is as stated.
- **`D`.** `fd539e15` is `main`'s head.

**Appendix C, verbatim check.**
- Method: the source is lines 297–486 and Appendix C carries them at 1121–1310.
- Workflow: 1099–1326 against 1314–1541.
- Runs: 1328–1475 against 1545–1692.
- After applying exactly the five declared renames, all three are **byte-identical**. The source has 47 renamed hits.
- The stated source span "297–486" is right; the appendix copy begins one line lower, after a blank line.

***

## Blockers

### R10-B1. Appendix C is not self-contained

The copied sections reference definitions that live in QC22 sections **not copied**:
- *The controls*, at source 487–628: M-GUARD, M-MODE, the control-B name rules and route allowlist, C-INDEP, C-EXACT,
  C-STATELESS and C-BUDGET.
- *Scripts*, at 849–1096: the checker's modes and keys, the builder's refusal, `derive-run`, `order`, `stress-check`,
  `approval-check`, `check --freeze`, and A11.
- QC22's *Stop rule*, at 1476–1513: the definition of a host VOID.
- QC22's preconditions 2a, 2b, 6, 6′ and 6″: E-ID, E-READ, E-BIND, GT-1 to GT-7, GT-2b, the design run, the confirmation
  run and the timeout test.

The adaptation table says these are "carried". But no row of r10 defines controls B, W, T, P or N, M-GUARD, A11 or the
gate tests, and r5 does not define them either. Counts in the appendix: "precondition 6" ×6, "E-ID" ×5, "timeout test"
×4, "control N" ×3, "precondition 2b" ×3, "stress-check" ×3, "check --freeze" ×3, "A11" ×2, "host VOID" ×2, and others.

This has two consequences:
- The frozen control plane would rest on a scratch file off `main`, a §A.42 item 8 gap.
- The safeguards the brief asks about cannot be verified from r10. The allowlist is one, the name rules another.

**Fix.** Copy the remaining QC22 sections by the same method: verbatim, with declared renames and an adaptation table.
Apply D12's removals (R10-B5) in the copy, and re-review it.

### R10-B2. The single-builder guard does not fit this round's decisive families; controls lack a frozen mode

QC22's guards are built around **one** builder: an instrumented count of F1-builder calls, "a second self-test function
that references the builder", and `t_builder_refuses`. The adaptation table maps F1 to many families:
- P's `Adm_A`, `Adm_B` and the ablations;
- REP-INV;
- B-P, construction A of B, and B-C;
- C's test-rule orbits, ablations and C-A.

r10 does not say how one builder guard covers them.

Several P and C **controls** evaluate exactly those families, and none has a frozen mode:
- **P controls:** AB-P-FIX, MECH-FIX, ACC-ONLY-FIX, PL-SHARP, PL-CONFOUND, PL-NOREC, PL-ABSORB, PL-SPI and PL-NOFR
  (construction B's arms and supply variants), and REP-PLANT (REP-INV on P's arms).
- **C controls:** CC-NAT (affine-rule orbits, the same computation as ABL), CC-DYAD ("all eight rules, rounds with
  `reg = none`", that is, test-rule C-A data), C-XB (test-rule propagation for every `S_0` law and round), C-AFFB,
  C-FRAME, C-SCOPE and C-EMB.

Meanwhile:
- r10's header reads "*The controls* (frozen; each decided before any decisive computation)";
- QC22's copied text says controls are "evaluated in the decisive run";
- the adaptation table puts "every self-test fixture and every B control" in fixture mode.

Read as fixtures, the controls above would compute decisive families in job A on every pull request and push. The
"no self-test evaluates P's construction B, a test rule's orbit …" sentence would then be false.

**Fix.**
- Freeze a per-control table giving the mode and job: fixture/A or decisive/B.
- Route every decisive family through one gated entry point, with one refusal and one call counter, or give each
  builder its own refusal and a counted registry.
- Extend M-GUARD and control B's name rules to every decisive builder.
- Correct the controls header.

### R10-B3. The owner's D18 condition: REP-INV cannot detect a resource supplied by an identification

**The paper claim holds.** Every ledger alternative is a symmetry: relabellings and frame shifts commute with the
reciprocal step; signed-permutation recalibrations preserve O_h compatibility, ℓ1 and the ball; RC2's relabellings
induce signed permutations.

**That is also why REP-INV cannot detect what the owner asked about.** Varying an identification within its symmetry
class can only show outcome-neutrality inside the class. It catches implementation errors (REP-PLANT gives it teeth
there). It cannot show whether the class itself supplies "coherent mixing, quantum probabilities, or contextuality".

**Confirmation per entry:**
- **L-PATH, L-PORT and L-CAL.** Confirmed on paper. Each names native registered records or affine coordinates, and
  supplies no dynamics, probability or contextuality.
- **L-UPRIME. Not confirmed for contextuality.**
  - U′'s three functionals are B-C's entire access class.
  - The carrier has four bits, and meters on cell 1 exist. That read set is the source of B-C's fragment
    incompleteness (r6 B7).
  - A B-C contextuality can therefore be supplied by L-UPRIME's read set, which is exactly the owner's "If an
    identification supplies a quantum-specific resource, it must instead be classified as an imported assumption".
  - Under D17(a), B-C does not count toward Level 2, so no Level is affected. But the condition is unmet, and B-C's
    printed result could carry the resource unlabelled.

**Fix.**
- State REP-INV's scope as "outcome-neutrality within each identification's symmetry class".
- Add a non-symmetric test for L-UPRIME. If B-C is contextual and decide-b's completion "every slot of every cell"
  (which reads beyond U′'s functionals) restores a model, reclassify L-UPRIME as imported **for B-C**, mechanically,
  in `decide-levels` and in the note.

### R10-B4. REP-INV's L-CAL variation must transport the encoded transposition

- W-CL fires on `β` or on `P^k β`, with `P = (x ↔ z)` in the calibrated frame.
- Under a recalibration `S` (one of the 48 signed permutations), `β ↦ SβS⁻¹`. The encoded transposition must become
  `SPS⁻¹`.
- With `P` kept fixed, the either-frame verdict changes.
- **Probe** (`repinv_frame.py`, C-R60-ODD's supplied `β = P·R60`): with `P` fixed, W-CL is lost in **8 of 48**
  recalibrations. With `P` transported, it is lost in 0 of 48.
- REP-INV as drafted would therefore report L-CAL "changed". The reclassification rule would then turn a genuine
  C-EXPOSURE into a benchmark result and withhold Level 3.

The same applies to L-UPRIME's RC2 relabellings, which act on the frame as signed permutations.

**Fix.**
- Freeze "under recalibration `S`, the encoded transposition is `SPS⁻¹`; `det_enc` is computed in the transported
  frame".
- Add a REP-INV self-test: C-R60-ODD under all 48 recalibrations must stay invariant.

### R10-B5. D12: what the Environment did, what remains, and the post-landing gap

This blocker is detailed in the D12 section below. In brief:
- Every Environment element must be removed.
- Three claims must be downgraded from "prevented" to "detected".
- The audit window ends at the final capture, but the owner's condition 1 includes post-landing runs. Without the
  Environment, a first-attempt dispatch with `arp2qc21_decisive: true` on any ref whose head carries the checker and no
  receipt would compute decisive output after the final capture, unseen. Those refs are the design, confirmation and
  gate-test branches, S1, `E`, a `Λ`, or a new branch cut from any of them.
- **Fix:** add a ref key, so that decisive mode requires `GITHUB_REF == refs/heads/research/arp2-qc21-20261108` in B3,
  in B4's workflow expression and among the checker's keys. After landing, the round branch head carries the receipt, so
  B3 and the receipt key refuse.
- The remaining residual is a force-move of the round branch, a destructive ref movement that §A.43 bars without owner
  authorization. It is visible in `GET repos/{o}/{r}/activity`, so state it as a residual.

***

## D12 (owner c.6735159962): Environment-dependent elements, removal, and what remains

### Elements to remove

| # | element (where) | remove |
| --- | --- | --- |
| E1 | job B's `environment: arp2-qc21-decisive` (C.2, Job B); "It names the Environment …" | the line and its paragraph |
| E2 | *Enforcement* item 1, "Primary: the Environment gate", including "This holds before `F`, during execution, before landing and after it" and the "reach in identity" (E-ID options) (C.2) | the whole item. The in-tree keys become the only preventive layer for the frozen splice, and detection becomes the authorization check |
| E3 | B3b (E-BIND) `approval-check` and job B's `permissions:` for it; `approval-check` in controls (C.2) | B3b, its permissions and the route |
| E4 | A11 (E-READ (a)), job A's `permissions:` and `GH_TOKEN`; A11 in the *Common* interpreter list (C.2) | A11 and the token |
| E5 | the approval entry's `review` field (`GET actions/runs/{id}/approvals`: state, `user.login`, `environments`, `comment`) (C.3) | the field. Re-anchor the binding: the run's `head_sha` equals the commit **in the owner's quoted words**; B3 success; `parameters.dispatch_sha`; the decisive input; attempt 1 |
| E6 | the deployment record (`GET deployments?environment=…`) and its mapping (C.3) | the whole bullet |
| E7 | **Order (r11 N5)**: the review time bounded by the deployment statuses (C.3) | the bullet. The order rule is now "the owner's approval comment precedes the run's `created_at`, and no comment is reused" (already in *the prior authorization*) |
| E8 | control N (Environment settings read at S1, `E` and `verdict`); `verdict`'s "control N included" (C.3) | control N, and its `verdict` condition. Delete rather than leave a vacuous pass |
| E9 | E-ID, E-READ, E-BIND (precondition 2b); precondition 2a (frozen Environment settings) | all of them |
| E10 | GT-1 to GT-7 and GT-2b (precondition 6″) | the Environment tests: reviewer identity, branch policy, the approvals endpoint (GT-2, GT-2b), the session credential's approval (GT-7). **Keep or add** non-Environment gate tests: job B is `skipped` on `pull_request`, `push` and attempt 2; B3 fails on an input that does not match (B4 `skipped`); the ref key (R10-B5) fails off the round branch |
| E11 | the call budget's "a few calls for the Environment, approvals and deployments" (C.3) | those calls |
| E12 | r10 body: "owner-approved, Environment-gated dispatch" (*The objects*, S1); "job B gated by `environment:`…" (*The workflow edit*); D12 rows in the decisions table and preconditions 2 and 7; the adaptation-table rows for control N, E-ID, E-READ, E-BIND, B3b, GT-*, 2a, 2b and 6″ | replace with c.6735159962's wording |
| E13 | wording only: "skipped before the Environment is consulted" (C.2 *Common*, C.3 *Re-runs*) | "skipped by the job-level `if:`" |

### Claims to downgrade from "prevented" to "detected"

- **"Scope of this guarantee".** "unless … an owner-approved, first-attempt, gated dispatch" should read: "unless it is a
  first-attempt dispatch with the decisive input, on the round branch (R10-B5), whose commit equals the input and whose
  tree has no receipt. Whether such a dispatch was owner-approved is **detected** by the enumeration against the
  approval entries, within the audit window; it is not prevented."
- **"After merging to `main`".**
  - "refused by the Environment" should read "refused by B3's receipt key and the ref key".
  - "A gated dispatch on the round branch waits for the owner's approval" should read "an unapproved dispatch on the
    round branch before `Q` runs and is **detected** (VOID)".
  - "both are closed by prevention" should be deleted.
- **"The window between `E`'s capture and `Q`'s push".** "A gated dispatch on one waits for the owner's approval, which
  is not given" should read "a dispatch on a `Λ` runs, and is detected by the final capture (VOID)".
- **"A latent route (`workflow_call`)".** "The Environment would still gate that route" should be deleted: it is now
  ungated, so state it as a guard on any later change.

### What remains after removal

| property | holds? | by what |
| --- | --- | --- |
| decisive steps only on dispatch, attempt 1, keyed to the receipt | **yes, for runs of the frozen splice** | job B's `if:` (event, attempt, input); B3 (`GITHUB_SHA = input`; no receipt); B4's and B6's workflow keys (event, attempt, receipt); the checker's three keys and the builder's refusal; plus the ref key (R10-B5) |
| the repository-wide enumeration rejects any unapproved run as VOID | **yes, within the audit window** | rules (a)–(d) need no Environment. An unapproved checker-bearing dispatch matches no entry and is a violation |
| the allowlist holds | **cannot be confirmed from r10** | the allowlist (control B's routes) is in QC22's uncopied *Scripts* and controls (R10-B1). After removal it must also drop the `approvals`, `deployments` and Environment templates and add no write route |
| the approval entry and the order rule alone detect any unapproved decisive run | **yes, within the window and limits below** | the prior owner comment (exact commit and stage, before the run's `created_at`, not reused); the run's binding to that commit; one entry per `(run_id, attempt)` |

### The owner's three conditions

**1. Complete detection within the audit scope.**
- **Re-runs.** Covered:
  - every attempt is read;
  - job B is skipped at attempt 2 or later by the in-tree `if:`, so a re-run of the frozen splice cannot compute;
  - an attempt 2 or later whose job B ran is a violation.
- **Post-landing runs. Not covered by r10.** No capture runs after the final capture.
  - With the Environment waived, a dispatch at a no-receipt ref that carries the checker computes unseen.
  - R10-B5's ref key turns this into prevention for the frozen splice, because the round branch's head carries the
    receipt after `Q`.
  - The residual (a force-moved round branch) is visible in the repository activity API. State it.
- With that fix, condition 1 holds within the scope stated under *Limits* below.

**2. Fail-closed.** r10's rules are fail-closed:
- a failed or rate-limited capture is retried and is never a pass;
- an unreadable tree halts the stage;
- a missing artifact without its `order-s1.json` record is VOID;
- `verdict` prints VOID unless every listed condition holds.

Removing E5–E8 must **delete** their conditions. If they are left in place, `verdict` would demand Environment
evidence that no longer exists: that fails closed but blocks every legitimate run, or, worse, is coded as an absent
field read as a pass. Two pieces of evidence are ambiguous by construction and must be stated:
- The approval comment is posted under `amaybaum`, the credential the session also holds. Host records cannot tell the
  owner's comment from the session's. This was so under the Environment's option (iii) too.
- **Recommended:** the `E` designation request lists every checker-bearing run and every approval entry from
  `order.json`. The owner then ratifies them when designating `E`, which closes the ambiguity by the owner's act rather
  than by host records.

**3. No residual dependencies.** **Not confirmable on r10.** The dependent definitions (E3–E10) sit in QC22 sections that
Appendix C does not copy (R10-B1). r11 must copy them with the removals applied. The re-review then checks the full
list E1–E13 and confirms that no control, `verdict` condition, gate test, allowlist template or adaptation row still
refers to an Environment, `approvals` or `deployments`.

### Limits of detection (the owner's qualification, stated concretely)

r11's text must claim no more than this:

- **Deleted runs.** A deleted run cannot be enumerated. The protection is the owner's commitment, c.6726548830 item 1,
  "No CI run deletion until Q-C2-2 closes". It should be restated for this round, and the session's credential can
  break it.
- **Retention.**
  - Artifacts and logs expire after 90 days. `order-s1.json` freezes the fixture-mode records at S1, and `verdict` reads
    attempt and job records, which persist until deleted.
  - Logs are never evidence (§A.44).
  - After expiry only structured run and job records and the committed captures remain.
- **API visibility.**
  - Runs of a workflow whose file was later deleted are still listed by the repository runs API; this holds as long as
    the runs themselves are not deleted, and should be confirmed in a gate test.
  - **Runs in forks are invisible.** A fork's own workflow runs are not in this repository's API. Pull-request runs from
    a fork run in this repository and are enumerated; job B is skipped there.
- **Local runs of the public code.** These are undetectable. The code is public from S1's push.
- **Modified workflows on other branches.** These are detected only if they carry the pinned checker blob or the frozen
  job or step names. A modified checker with renamed jobs is undetectable (r10's own scope statement, which should be
  kept).
- **The session's own credential.** As `amaybaum`, the session can do all of the following, and none of it is prevented:
  - dispatch;
  - post an approval comment;
  - re-run;
  - push branches;
  - force-move refs;
  - delete runs.

  Detection covers its dispatches and re-runs, within the window and the blob/name identification. Ref force-moves are
  visible in the activity API. Run deletion is not detectable. Authorization integrity therefore rests on the owner's
  procedural commitments and on the `E`-designation ratification recommended above.
- **The audit window.** `[T_repo, final capture]` for dispatches and `[T0, final capture]` for other events. After that,
  only the in-tree keys hold, together with the ref key once it is added.

### Unauthorized executions, classified three ways (the owner's refinement)

| execution | class | why |
| --- | --- | --- |
| unapproved dispatch of the frozen splice or the pinned checker, on any branch of this repository, within the window | **detectable** (VOID) | rule (a)–(d): no matching entry. The checker is identified by blob or name, and conclusions are not consulted |
| a dispatch made before the owner's comment, a reused comment, or a run whose `head_sha` differs from the quoted commit | **detectable** | the order rule and the binding (after the E5 re-anchoring) |
| a cancelled checker-bearing dispatch | **detectable** | identification ignores conclusions. A cancelled approved run at S1 or `E` fails `verdict`, and the host-VOID rule applies (that rule is in QC22's uncopied stop rule; R10-B1) |
| a re-run attempt 2 or later of an approved run | **detectable** if job B ran; **prevented** for the frozen splice | the `if:` skips job B; every attempt is read |
| a run at a commit outside the recorded branches, for example a new branch cut from S1 | **detectable** within the window | rule (d) and the closing violation clause |
| a non-dispatch run in which B4 ran or `fixtures_mode` is not `"fixture"` | **detectable** | the no-unapproved-F1 rule |
| a force-move or deletion of the round branch | **detectable only if the captures read it** (they do not in r10) | `GET repos/{o}/{r}/activity` records force-pushes and branch deletions. **Add it to every capture**, with a hit on a recorded branch as a violation |
| a dispatch after the final capture at a no-receipt ref | **unobservable** in r10. **Prevented** once the ref key is added (R10-B5) | no capture runs after the final one |
| a deleted run | **unobservable** | it cannot be enumerated, and run ids are not contiguous per repository, so a gap is not visible. It rests on the no-deletion commitment |
| a local run, or a run in a fork | **unobservable** | outside this repository's API |
| a modified checker with a different blob and renamed jobs and steps, on any branch | **unobservable** | outside identification (r10's own scope statement) |
| a non-dispatch run before `T0` on an unrecorded branch carrying the checker | **unobservable** (residual; empty per the writer's record) | outside set (2)'s window |
| a capture that failed, was rate-limited or was truncated; an unreadable tree; a `total_count` mismatch | **evidence-incomplete** → fail-closed | retried, never a pass. A persistent failure halts the stage |
| a missing artifact (expired, or deleted through the artifacts API) | **evidence-incomplete** → fail-closed | VOID, unless `order-s1.json` holds the record (S1's measurements are committed at `E`) |
| deleted logs only | not evidence (§A.44) | run and job records persist |
| an approval comment under `amaybaum` whose author (owner or session) cannot be told apart, or which was edited after the run (`updated_at`) | **evidence-incomplete** → fail-closed **only if r11 adds** the owner's ratification at the `E` designation and a rule that a comment edited after its run is a violation | host records cannot attribute the comment's authorship |

### What the session's credential can do, and whether each control is independent of it

| capability (as `amaybaum`) | the control that catches it | independent of the executor holding the credential? |
| --- | --- | --- |
| dispatch | enumeration, entries, order rule | **No at execution time:** the session runs the captures (`order`, `verdict`). **Yes after the fact:** the captures re-query host records, so an independent reviewer can re-run them read-only, as ARP-1's results review re-derived its counts. Recommended: the results review re-runs the enumeration with its own read |
| re-run | the job-level `if:` (in-tree), and enumeration of every attempt | the in-tree key is independent unless the workflow is edited. The enumeration is as above |
| cancel | identification ignores conclusions | as above |
| delete runs | none | **not independent.** Unobservable; it rests on the no-deletion commitment |
| delete logs or artifacts | logs are not evidence; a missing artifact is VOID or covered by `order-s1.json` | fail-closed, so independent in effect |
| edit workflows | control W (uncopied, R10-B1) and V3's governed paths on the round branch; on other branches, blob or name identification only | partial. A renamed, modified copy is unobservable |
| push to any branch; create a branch from S1 | rule (d) and the closing violation within the window; the ref key afterwards | the in-tree key is independent. The detection is as for dispatch |
| force-move or delete refs | the activity API (to be added) | host-recorded, so independent once the captures read it |
| post or edit approval comments; record designations | none mechanical: designations are "recorded, unverified" in V3 receipts | **not independent.** It rests on the owner's direct confirmation. Recommended: owner ratification of the run list and entries when designating `E` |

### The owner's rule applied

- **Condition 1 (complete detection within the documented limits): fails in r10.**
  - Post-landing runs at no-receipt refs are neither prevented nor detected.
  - Ref moves are not read.
  - It passes once the ref key and the activity check are added, within the limits above.
- **Condition 2 (fail-closed): passes for capture and artifact evidence.**
  - It fails for authorization evidence until the `E`-designation ratification and the edited-comment rule are added.
  - The E5–E8 conditions must be deleted, not left vacuous.
- **Condition 3 (no residual dependencies): cannot pass on r10.** The dependent controls are in uncopied QC22 text
  (R10-B1).

So, by the owner's rule, **the D12 removal stays a blocker (R10-B5)** until r11 corrects the controls as listed. With
those corrections and the limits stated as above, I expect all three conditions to pass.

***

## Other checks

**D14 (`ATTR`).**
- `ATTR` is mechanical. It reads `V` (observer layer) and `D`, `K` (validation layer). "Computed from the validation
  layer" in PLAN §14 is imprecise.
- No sham-specific condition enters the token. But SH-0 and SH-K are members of `Adm_B`, so their `D` and `V` are read
  by the class predicate and by step 1's NONABS/SPI. "No sham quantity enters it" is literally false.
- Fix (r10-N1):
  - Reword to "no sham-specific gate".
  - Add a C-IFACE static rule that `decide-p` references neither `ATTR` nor the SH-0/SH-K fields except through the
    `Adm_B` loop.
  - Add an ATTR-FIX mutation that flips the sham-specific fields and must leave the token unchanged.
- "Attributable" is unreachable whenever screen statistics are a function of the arm's system channel. This is
  disclosed correctly.

**`access_only`.**
- It is correct, read as the identity of the full world laws. It is true exactly when the ablation changes only which
  records are registered or held unread.
- It holds for ABL-SA1b because registration is modelled as a read with no meter cells. State that modelling, since a
  physical read by meters would change the world laws (r10-N2).
- For `A_P` against B, the arm classes differ. Define the comparison: arms present in both are compared; an arm present
  in only one makes `access_only` false (r10-N3).

**Withholding table.**
- Correct and mechanical.
- "Pending at `F` counts as failed" is the right fail-closed rule.
- If Lemma P fails, CC-NAT becomes a reported comparison while ABL still gates C. That is consistent.

**Owner decisions.**
- Applied faithfully: L(i), D4(a), D15(a) typed candidate strengthened, and the A/B typing.
- The Level-1 presentation sentence is frozen and printed with every Level-1 award. It meets "must not be presented as a
  new derivation".
- PLAN §14's "D1/D9 `PENDING`" is stale, as the coordinator noted. c.6735014875 covers both (r10-N4).

**Regressions.** Against r9a, the diff is confined to the listed r10 additions and fills. I found no regression in P,
B or C's rules.

## Nits

- **r10-N1.** `ATTR`: wording, the C-IFACE rule and the ATTR-FIX mutation (above).
- **r10-N2.** `access_only`: state that registration is modelled without meter cells.
- **r10-N3.** `access_only` for `A_P` against B: define the arm matching.
- **r10-N4.** PLAN §14: remove the stale D1/D9 `PENDING`.
- **r10-N5.** Appendix C header: the copy begins at line 1121, not 1120, after one blank line. This is cosmetic.

## What remains before `F`

1. **r11 must resolve R10-B1 to R10-B5:**
   - copy the rest of QC22's guard machinery, with the D12 removals E1–E13;
   - a per-control mode table and a builder guard covering every decisive family;
   - REP-INV's scope statement, and the L-UPRIME/B-C test;
   - frame transport in REP-INV;
   - the ref key, the claim downgrades and the *Limits* text.
2. **Independent review of r11**, covering the newly copied text (precondition 5).
3. **The two sketch reviews** (Lemma P and the cone argument). Their verdicts are quoted, or the withholding rows apply.
4. **The `PENDING` fields:**
   - the record-directory date and digest;
   - the REACHABLE path and blob (D9(a));
   - the benchmark;
   - the design-run anchors and records;
   - the stress generator and seeds;
   - the timeout-test term count;
   - `T0`.
5. **D9(a).** Land REACHABLE r3 and DESIGN-DS as paper records before `D`.
6. **Scripts with self-tests**, the design run, and the non-Environment gate tests (E10's kept set and the ref key).
7. **The restated no-deletion commitment**, and the **`E`-designation ratification** of the run list (condition 2).
8. **The freeze.** The `F` dispatch with its approval entry, and the designation request.
