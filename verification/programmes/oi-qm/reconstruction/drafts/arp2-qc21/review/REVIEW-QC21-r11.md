# Independent re-review: Q-C2-1 r11 (ARP-2-QC21)

**Reviewer.** The same independent model reviewer as r6–r10, 2026-11-09. Read-only, with `gh api` GETs only. I ran
`r11parts/build_c.py` in my own directory (`review/probes-r11/run/`), with only its source path made absolute. Nothing
was written to the writer's files.

## Verdict: **REVISE (minor)**: one small blocker, otherwise ready

**What r11 achieves:**
- Appendix C is now self-contained, and it is verbatim apart from the declared renames and the 44 logged edits. Each
  edit is necessary and correct, and no Environment-free safeguard was removed.
- The single gated entry `s_decisive` and the control-mode table close R10-B2. All 37 control codes are assigned to
  exactly one mode, and no fixture-mode control builds a decisive family.
- UPR-BC and REP-FRAME are correct.
- The r10 nits are applied.
- The three-way classification and the credential table are accurate.

**One blocker remains (R11-B1).** The post-landing prevention claim omits two routes that reopen decisive mode on the
round branch after the final capture, so a documented limit is missing. By the owner's rule, condition 1 does not pass
until it is stated. The fix is a text change and one owner commitment.

## Inputs verified

| file | sha256 | status |
| --- | --- | --- |
| `preregistration.draft.md` r11 | `6d7b88afd1d0e77f731274fe6a38c23d1b46f1690f9c1e74b6ebb20785c203e9` | matches |
| `PLAN.md` r11 | `65288c2c1f399010e1278f113e0d563e0955e5ed5e8c24e77107bf3a984e6a13` | matches |
| `DESIGN-DS.md` r11 | `f0cb090e06d68bddb4241b319ad480cc90603d590b5186847c10517df4f59b84` | matches |
| `r11parts/build_c.py` | `5b06b439237baf21c537b23dc510a580ff828ba7786090ac17c4a091f7a7b25f` | matches. My local copy, with only `SRC` made absolute, is `6a30d846…` |

The D12 quote of c.6735159962 is verbatim at sentence level (13 of 13 sentences).

## 1. Appendix C

**Rebuild.**
- `build_c.py` asserts the QC22 source hash `15d90b24…` and applies 44 logged edits.
- Its outputs `c1`, `c3`, `c4_rows`, `c4_st`, `c5`, `c6` and `editlog` are byte-identical to `r11parts/`.
- `c2` differs from `r11parts/c2.md` by one re-wrapped sentence, whitespace only.

**Against the preregistration.**
- `r11parts/appendixC.md` equals the preregistration's Appendix C (1078 lines).
- C.1, C.3, C.4's rows and C.4's self-test block appear verbatim.
- C.2, C.5 and C.6 differ only in heading level. "### Job A/B" became "####", and the "## Scripts" and
  "## Stop rule" headings were dropped under C.5 and C.6.
- C.5a (the schema) and C.7 (the design and confirmation runs and the gate tests) are declared **adapted, not
  verbatim**. I read them as new text.

**The 44 edits.** Each is necessary and correct:
- **E1, E3, E4, E8, E12, E13 (removal and wording).**
  - The `environment:` line, B3b, `approval-check`, A11 and `env-read` are removed.
  - Control N is removed. The text it removed was Environment-only: settings pins, the E-READ channels and the residual
    on `updated_at`.
  - The Environment endpoints are removed from the allowlist.
  - The "skipped before the Environment is consulted" wording is fixed.
- **E2 (enforcement, rewritten).** It now says "detected and rejected, not prevented". The in-tree keys are scoped as
  prevention for the frozen splice only.
- **E5–E7 (approval entries).**
  - The binding is re-anchored on the quoted commit.
  - Authorship must be `amaybaum` with association `OWNER`.
  - The edited-comment rule is added.
  - The order rule is "the comment precedes the run's `created_at`; no reuse".
- **Ref-key rows.** B3, B4's expression, B6's `if:`, the checker's fourth key, control W's list, M-GUARD's
  single-key-failure list and `s_mode` all add `GITHUB_REF == refs/heads/research/arp2-qc21-20261108`.
- **Downgrade rows.** "Scope of this guarantee", "After merging to `main`", the `Λ` window and `workflow_call`.
- **Activity, deletion and ratification rows.** Every capture reads the activity API; deletion and force-push are
  violations; `verdict` requires the owner's ratification at `E`. The `activity?ref=refs/heads/...` template is already
  in control B's frozen GET allowlist.
- **ARP-4 to ARP-3** (row 44). This is correct for this programme's order.

**Was a needed safeguard removed?** No.
- The removed "Who approves" paragraph was Environment-specific: the deployment-review endpoint and E-ID option
  (iii). Its replacement points to *Scope of authorization and detection*.
- `pending_deployments` stays as a **forbidden** `POST` route in M-GUARD and control B. That is correct defence.
- The header's claim is confirmed by the build script's own scan. The residual mentions are: the waiver statements, the
  section title "Runs, evidence, approvals", "No `environment:`" for job A, and the forbidden `pending_deployments`
  route.

## 2. The guard

**Builders.**
- `s_decisive` is the only gated entry. `DECISIVE_BUILDERS` lists one builder per family: P's arm classes and
  ablations, REP-INV, B-P, construction A of B, B-C, and C's orbits, ABL and C-A.
- Each builder carries the refusal as its first statement.
- The name rules confine each builder name to its `def`, the list and `s_decisive`, and confine `s_decisive` to the
  entry and `t_builder_refuses`.
- M-GUARD's counter counts every registered builder and must read zero in every fixture-mode case.
- The adaptation table maps "the F1 builder" to this guard. **Sound.**

**Control modes.**
- All 37 control codes in the controls table and Appendix B are assigned to exactly one mode (exact check).
- The fixture-mode controls evaluate only supplied or synthetic objects:
  - QM-P and CW-P (non-OI data);
  - C-DET (native-`XOR` detectors on supplied laws);
  - C-STEP (the step map against its inverse; no orbit and no law);
  - REP-FRAME and C-R60-ODD (supplied matrices);
  - ATTR-FIX (synthetic records).
- No fixture-mode control evaluates a decisive family.
- The decisive list covers every P control on construction B, REP-PLANT, CC-NAT, CC-DYAD, C-XB, C-AFFB, C-FRAME,
  C-SCOPE, C-EMB, C-BUDGET and C-CERT on decisive fragments.
- Nit r11-N1: UPR-BC's fixture is synthetic `decide-levels` records, yet it is listed as decisive. That over-gates a
  check that could run on every event. Either is safe; make the table consistent.

**The ref key.**
- **Sound against a same-named ref while the round branch exists.** Branch names are unique, and a tag dispatch gives
  `refs/tags/…`, which fails the key.
- **Sound for gate tests.** GT-REF puts B3, B4's expression and the checker's key in triple redundancy, so if B3's
  implementation were wrong, B4 and the checker would still select fixture mode.
- **Not sound after the final capture** against two routes on the round branch (R11-B1).

## 3. The owner's three D12 conditions

**Condition 1, complete detection within scope: passes within the window; the post-landing limit is incomplete.**
- **Re-runs.** Prevented by the `if:`, and every attempt is read.
- **In-window events.** Unapproved dispatches, early or reused comments, wrong commits, edited comments, cancelled runs,
  new branches, non-dispatch decisive runs and ref moves are all detected (VOID).

**R11-B1 (blocker).** After `Q`, two routes reopen decisive mode on the round branch, and neither is prevented or
detected once the final capture has run:
- **(a) a fast-forward push** to the round branch of a commit that deletes `verification/receipts/ARP-2-QC21.json`.
  This is not a force-move, so neither the activity rule nor §A.43's ref-move bar covers it.
- **(b) a deletion and re-creation** of the round branch at a pre-`Q` commit. The table names deletion only "within the
  window", and names only force-moves after it.

The text "Post-landing runs. The ref key … turns them into prevention for the frozen splice. The residual, a
force-move …" therefore overclaims.

**Fix:**
- State (a) and (b) in *Limits* and in the three-way table: **unobservable after the final capture**.
- Extend the owner's commitment at the freeze to "no push to, deletion or re-creation of the round branch after `Q`
  without a recorded owner authorization".
- In the scope section, change "turns them into prevention" to "prevents them for the frozen splice, except through
  (a), (b) or a force-move, which this round does not observe after the final capture".

Since the decisive output is public from `E`, these routes threaten attestation hygiene, not blindness. State that too.

**Condition 2, fail-closed: passes.**
- Failed, truncated or rate-limited captures, unreadable trees, `total_count` mismatches and missing artifacts fail
  closed.
- So do edited comments and approval entries the owner has not ratified at `E`.
- The deleted Environment conditions are deleted, not left vacuous, in `verdict` (*every check at `E` passes*) and in
  the stage records (R).

**Condition 3, no residual dependencies: passes.**
- The build script's scan, the body grep and my reading of every E1–E13 location find no control, `verdict` condition,
  gate test, allowlist template or adaptation row that depends on an Environment, `approvals` or `deployments`.
- C.7's gate tests are Environment-free: GT-B3, GT-REF, GT-RERUN, GT-PLAIN, GT-PR, GT-LIST.

**The three-way classification** is correct, and complete apart from (a) and (b) above.

**The credential table** is accurate in its independence statements:
- the captures are not independent at execution time, but can be re-checked independently afterwards;
- run deletion and comment authorship are not independent;
- ref moves are host-recorded.

Add one row: "push to the round branch after `Q`" → unobservable after the final capture, under the commitment.

**Downgrades.** Every "prevented" claim that rested on the Environment is downgraded. That covers C.2's enforcement,
scope, after-merge, `Λ` window and `workflow_call` passages, and the body text (*The objects*, D12 row, preconditions).
The only remaining over-strong sentence is the post-landing one in R11-B1.

## 4. UPR-BC, REP-FRAME and the nits

- **REP-FRAME.** It requires W-CL to fire in all 48 recalibrations of C-R60-ODD's map with `SPS⁻¹`, matching my r10
  probe (0 of 48 lost when transported). The rule text also transports `det_enc`. **Correct.**
- **UPR-BC.**
  - The rule is mechanical: if B-C is contextual and the completion "every slot of every cell, registered jointly"
    restores a model, the result is "imported for B-C", printed as a benchmark, with no Level effect under D17(a).
  - If the completion does not restore a model, the contextuality is not attributed to U′'s read set. That is the
    right reading.
  - **Correct**, apart from r11-N1.
- **REP-INV's scope sentence** and the paper confirmation for L-PATH, L-PORT and L-CAL are as recommended.
- **r10-N1.** "no sham-specific gate", the C-IFACE `Adm_B`-loop rule and the ATTR-FIX mutation are all present.
- **r10-N2 and r10-N3.** The registration modelling and the arm matching are present.
- **r10-N4.** PLAN is current.
- **r10-N5.** The header now gives the spans correctly.

## Nits

- **r11-N1.** UPR-BC's mode (above).
- **r11-N2.** Add the `c2` re-wrap and the heading-level changes to the edit log, or say "with heading levels adjusted"
  in the header.
- **r11-N3.** Add GT-ACT: a force-push on the gate-test branch appears in `GET activity?ref=…` within the capture.
  Also record the activity API's retention horizon, so that "detectable within the window" for ref moves is verified,
  not assumed.

## What remains before `F`

1. **R11-B1.** Add the two post-landing routes to *Limits*, the three-way table and the credential table. Extend the
   owner commitment. Re-word the post-landing sentence. A confirming check of that edit is sufficient.
2. **r11-N1 to N3**, including GT-ACT.
3. **The two sketch reviews** (Lemma P and the cone argument). Their verdicts are quoted, or the withholding rows apply.
4. **The `PENDING` fields:**
   - the record-directory date and digest;
   - the REACHABLE path and blob;
   - the benchmark;
   - the design-run anchors and records, the stress seeds, the budgets and the timeout-test count;
   - `T0`;
   - the pins of `design-run.json`, `stress.json` and `gate-tests.json`.
5. **D9(a).** Land REACHABLE r3 and DESIGN-DS as paper records before `D`.
6. **The scripts** (`qc21_check.py`, `controls.py`) with self-tests; the design run, the confirmation run and the gate
   tests of C.7.
7. **The owner's commitments at the freeze, recorded:**
   - no run, log or artifact is deleted until `Q`;
   - ratification at `E`;
   - no force-move, deletion or re-creation of, or push to, the round branch after `Q` without authorization (R11-B1).
8. **The freeze.** The `F` dispatch with its approval entry, and the designation request.
