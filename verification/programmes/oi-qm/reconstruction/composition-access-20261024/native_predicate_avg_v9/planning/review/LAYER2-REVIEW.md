# Independent review: NP-AVG-1 Stage 0, Layer 2 draft

**Object.**
- PR #935 at `99a9797e`: `stage0/layer2/`. The plan is `LAYER2-PLAN.md` (SHA-256
  `9dfa0e11…ff9b`, 647 lines), alongside `README.md`, `code/` (22 files) and `design/`.
- Read against the frozen Layer 1: `r5/STAGE0-PLAN-r5.md`, SHA-256 `1a30188e…847e`, at
  `f33d8d63`.

**Read-only.** Nothing was edited, committed or pushed.

**No v8 computation.** Nothing ran on v8's configuration class. On v8, I did only three things:
- I re-ran the drafter's own design-evidence steps, which are combinatorics and refusals;
- I ran the dry run under an import trap that makes the engine unimportable;
- I made guard calls that construct no `Context`.

My outputs are in `S/npavg/review-l2/`. `replay/` is a scratch copy of `code-r5/` and `layer2/`
with `l2run.py` re-run. The comparison is in `replay_compare.txt`. The probes are in `probe/`.

## Verdict: ACCEPT WITH CHANGES. Layer 2 is not ready to freeze

**What is sound.**
- **Architecture.** The production, reference and native paths are kept apart. The merge reads
  structured files only, and no closure is computable on v8 without an artifact.
- **Bounded evidence.** It replays exactly, apart from the recorded commit and the timing steps.
- **Proof obligations.** Most are valid.
- **Rule T.** Its L_A = L_G = 0 consequence follows from the frozen assumptions under Layer 2's
  readings (§2).

**What blocks a freeze.**
- **Nine required changes.** L2-R1 to L2-R9 cover three silent truncations of the minimal witness
  and the residue, gates run on survivor representatives where Layer 1 says every survivor, a
  certificate that does not bind commits, and an over-stated v8-lock claim.
- **Four owner decisions.** Rule T's readings (T1, T2, T5), the C7 scope (F3), the launch and
  budget rule, and the degeneracy cross-tabulation (F6).

None of this changes the masking law, the domain or the labels.

## 1. Replay (task 5)

`l2run.py` was re-run on a scratch copy at the same code hashes. The `RUN-MANIFEST` code hashes
are equal.

| step | result |
| --- | --- |
| manifest, self-test, both dry runs, pre-flight, quick mutants, S1a, merge, certificate, cross-check, code-r5 equivalence, planted survivor path, v8 refusal probe | stdout **byte-identical**; exits 0; `-O` identity as recorded |
| `calibration_planted`, `dryrun_v8_estimate` | timing-dependent, as declared |
| `shard_toy_0`…`3` stdout; `s1a`, `shard-*`, `result`, `certificate` JSON | equal **modulo `commit`** and the self-digests that hash it |

**The commit caveat.** The committed files record HEAD `217f7a40`. My scratch copy is not a
repository, so it records `null`. Every other field is equal.

**The quick campaign** (`toyrun/mutant-campaign.json`, identical on replay):
- **30 of 30 killed at their named cases.** That is 17 rule mutants, each at its Layer-1 case, and
  13 machinery mutants, each at its L2 self-test case.
- **The unmodified suite** passed first.
- **The demonstrations** fail C11 only.

**The counts cross-check holds.** All 54 merged counts equal code-r5's full per-record
computation (`crosscheck_toy_counts`, identical on replay).

## 2. Rule T, for the owner (task 2)

**Is the consequence true?** I checked PO-L2-7 step by step; U = {(x, 23) : x ∈ Reg}.
1. **Nesting.** Ctx(R) ⊆ Ctx(U) for every finite set R of items in Reg × {−1, …, 23}. The samples
   of (x, t) are those of (x, 23) at slices up to t. The fixed quantities and port samples are in
   every context (L1 §1).
2. **Monotonicity.** ret(R) ⊆ ret(U) under A and G, for L3′ (L1 PO4). This holds because the
   closure is the greatest self-supporting subset, and G-eligibility depends only on the frame,
   which is record-independent (L1 §2).
3. **Under A.** S_A(R) consists of non-fixed quantities in ret_A(U). A Φ-linked survivor puts a Φ
   cell in the cone of some such quantity, so L_A ≥ 1.
4. **Under G.** Whether a quantity has a seed tip is intrinsic to it (L1 PO7). So S_G(R) lies inside
   {q ∈ ret_G(U) : q has a seed tip}, and a G-linked survivor makes L_G ≥ 1.

**The consequence follows.** "No record over Reg × {−1, …, 23}, of any size, has a linked
survivor" follows from L1 §1, §2, PO4 and PO7. The scope "geometric fact only; no law beyond
k ≤ 2" is right: PO8 covers at most two Φ triples in clear.

**Is the text unambiguous? No.** Three readings must be fixed. One clause is inert, and one
citation is incomplete.

| finding | my verdict | needs a Layer-1 amendment before the Layer-2 freeze? |
| --- | --- | --- |
| **T1**, which rule's bound | Genuinely open in the text. The consequence is true under both readings, because ret_L3′ ⊆ ret_L3. They differ only in *when* S1b is proposed: L3 triggers at least as often. L3′ is the reading S2 supports ("labels use L3′"), and a linked survivor is a label-level object. | **Yes, an owner ruling** before any S1a result. This is a trigger parameter of a preregistered rule (O-b), so Layer 2 must not choose it. I recommend L3′, with L3 reported. |
| **T2**, S1a status undefined | A real gap. Layer 2's definition (VOID, MISMATCH or INCOMPLETE from S1a's own reference checks, C10 (i), L3′ ⊆ L3 on the bound, and any shard's C9 against the bound) is admissible under neutrality. Its inputs are validity facts, not the k ≤ 2 label or its direction. | **Yes, an owner ruling.** It defines when a preregistered rule is evaluated. I recommend Layer 2's definition. |
| **T3**, cost clause | Not vacuous in principle. In Stage 0 it is inert: S1b's dry run exists only inside S1b's own future preregistration. "Not evaluable in Stage 0" is the correct record. | No. An optional erratum could add "S1b's own dry run, in its preregistration". |
| **T4**, citations | The argument is complete, but rule T cites only PO4. It also rests on L1 §1 (Ctx), §2 (frame and eligibility) and PO7 (seed tips). | No. Cite them in the same erratum. |
| **T5**, "seed tip whose cone" | Ambiguous, and the alternative reading is degenerate. A tip is a depth-0 quantity whose cone is itself. Read as the tip's cone, the clause would require a seed (outside the frame) to be a source cell (inside the frame), which is impossible, so L_G ≡ 0 for every record class. Only the quantity's-cone reading is meaningful, and it matches G-linkage. | **Yes, an owner ruling or erratum.** I recommend "a quantity with a seed tip, whose cone contains a source cell". |

**Recommended vehicle.** A single append-only, owner-approved Layer-1 erratum fixing T1, T2 and
T5 (with T3 and T4 as notes). It must be recorded before the Layer-2 freeze, and in any case before
any S1a output exists, with its own short independent review. The Layer-2 freeze would also
precede the results, but rule T is Layer-1 text, so the authority should stay there.

**Neutrality** (the plan's question 3) is admissible as implemented. `rule_T` takes only
(status, L_A, L_G); L2-RT checks that the label is not an input, and M_ruleT_or is killed.

## 3. Proof obligations (task 1)

| id | verdict |
| --- | --- |
| PO-L2-1 | **Valid.** The ranges are standard unranking and ⌊sN/S⌋ is a cover. For v8 it is checked indirectly by the merge's recount: weights sum to N and representatives number Burnside's count. |
| PO-L2-2 | **Valid.** The canonical image is a function of the orbit and a member of it. |
| PO-L2-3 | **Valid** for the true closure. C4v fixes the slices, q9, Φ's site set, the port and Reg, and preserves ℓ¹ parity. With L1 PO4 (greatest self-supporting subset), equivariance follows. |
| PO-L2-4 | **Valid as code identity.** `post_closure` reproduces `analyse` after the closure: I compared them line by line. It is checked by L2-POST and by in-run C8. |
| PO-L2-5 | **Valid.** The distinct public sets are the union of the orbits of the representatives' sets, and the merge dedups canonical keys across shards. |
| PO-L2-6 | **Valid.** An item's non-fixed, non-port sample set is determined by (x, m), and sites are disjoint. |
| PO-L2-7 | **Valid under the T1, T2 and T5 readings** (§2). |
| PO-L2-8 | **Valid.** The cache key (pair, frame sources) determines eligibility. Frame sources include the rule's port filter, so the mutants are keyed correctly. |
| PO-L2-9 | **Valid.** "Cone inside the frame" is a property of the quantity, and every context lies within the universe plus the fixed quantities. |
| PO-L2-10 | **Claimed, not proved; false as stated** (L2-R1). See below. |
| PO-L2-11 | Honestly marked as checked, not proved. |
| PO-L2-12 | **Valid** (PO4 and nesting). |
| PO-L2-13 | Honestly marked toy-only. N and Burnside on v8 are independently confirmed by `s0symcheck`. |

**Why PO-L2-10 fails.** It claims "follows from PO-L2-3", but:
- **It assumes the computation is correct.** PO-L2-3 is about the *true* closure, and MISMATCH
  exists precisely to detect a computation that disagrees with it.
- **Members are not computed directly.** Their MISMATCH conditions come from *carried* results,
  except on orbits flagged by a representative or sampled at 1 in 100. A non-equivariant fault can
  therefore give a member a MISMATCH that is never seen.
- **Candidates are capped.** `l2enum` keeps only the first 100 candidates per shard
  (`WITNESS_CAP`), by index, not by the C16 key. Minimality fails even for the carried computation.

**Missing obligations** (the table is incomplete):
- **Reference gates on survivor members.** The gates run on survivor *representatives* only. That
  is valid only if the reference is equivariant, and no obligation states it (L2-R2).
- **Completeness of the residue output.** Survivor detail is truncated at 10,000 per shard, and the
  merge ignores the flag (L2-R3).

## 4. Implementation (task 4)

**§A.41 mapping.** Every Layer-1 control has a Layer-2 home:
- the full `s0controls` suite in pre-flight;
- C6's execution instances, C10 (ii) and C12 on the universe in the authorized pre-flight;
- C11 (iii) and both direction mutants in pre-flight;
- the in-run gates as in §3.3.

The expected values for C6 (base: A retains nothing, G retains N[1], N[3], N[5]; (q9, 9): A has p
and V in clear, G truncates to q9@0, 2, 4) match L1 §3's hand derivations. Exceptions:
- **"Every survivor".** L1 requires C7 to "agree on every survivor", and C11 (i) to run "on every
  survivor". `l2enum` runs C7, C11 (i), C17, C18 and the C0 context check on the *representative*
  record only (L2-R2). Survivor orbits are fully re-closed directly for C8, so running the reference
  gates on every member costs little.
- **The S1a L3 bound** feeds C9 but is never reference-checked; only the L3′ bound is (L2-R8,
  minor).

**Independence holds.**
- `l2refcheck` imports only `s0ref`.
- `l2plan` imports only `l2config`. I ran it under an import trap that makes `s0geom`, `s0ref`,
  `s0native`, `l2analysis`, `l2refcheck`, `l2enum` and `l2s1a` unimportable. It completed with
  output byte-identical to `runs/dryrun_v8_plan_no_closure.out`, so **no closure or context can
  occur in the v8 dry run.**
- The engine copy differs from code-r5 only in the guard and the memo. The geometry and the closure
  are byte-identical.

**The v8 lock** (`probe/lock_probe.{py,out}`; no `Context` is built).
- **Default refusals hold.** These are refused:
  - the default;
  - `authorized_v8=True`;
  - a `V8Grant` subclass;
  - a duck-typed grant;
  - a malformed `V8Grant`.

  The drafter's `refusal_probe` (9 of 9) replays identically.
- **A grant can be forged in-process.**
  - `G.V8Grant('0'*40, '0'*64, '0'*64, 'forged')`, built directly without `l2auth`, is accepted by
    the guard. `num_records(v8)` and `record_at(v8, 0)` run; I constructed nothing further.
  - `REF.RefGrant('0'*40)` passes `_ref_granted`.
  - `l2auth.decide()` returns `ok` on a fabricated artifact plus a fabricated owner-check JSON.

  The owner check's authenticity is not verifiable in-process, since the JSON is just a file. The
  lock prevents *accidental* v8 runs. It is not proof against a deliberate local forger.
- **The plan over-claims.** §7 says "Only `l2auth.issue_grant` constructs a grant". That holds as a
  static property of the repository's files (L2-S1), not at run time. The real gate is the CI
  owner-check job, together with a post-hoc check of the designation (L2-R4).

## 5. Layer-1 findings F1–F11 (task 3)

| finding | verdict | action |
| --- | --- | --- |
| **F1**, BASE_RESIDUE unreachable | Correct. A non-collapsed base disagrees with C6's hand derivation, which is MISMATCH and comes first. It fails closed. BASE_RESIDUE becomes reachable after the MISMATCH-resolution amendment L1 §5 already requires, if that amendment corrects C6's derivation. | No amendment before the Layer-2 freeze. Record this reading in Layer 2. |
| **F2**, base-relative survivors under G | Correct: the literal text counts truncated in-frame samples. Moot while F1 holds. | Fix in any future BASE_RESIDUE amendment, as "a record whose S_A or S_G contains a quantity outside ret(∅)". |
| **F3**, C7 scope | Correct. The literal initial-context reading is well defined but very common: 739 of 976 on the toy class. Any two quantities on a common axis line whose separation equals their depth difference share a tip, for example a z-axis item and a port sample; I did not measure the v8 fraction. At the reference cost it may exceed S7. The retained-set reading is cheap but nearly vacuous under A, where retained sets are almost always empty. | **Owner decision with an append-only amendment** (§7 has my recommendation). The v8 count comes from `l2plan --shared-tips`, which is combinatorics and needs no grant; it should be run in the dry run before the decision. |
| **F4**, residual support undefined | Reported only; no label depends on it. | Layer 2's definition is acceptable as a Layer-2 reading. |
| **F5**, masking equivalence | L1's text ("equal even-class contexts") governs, since code-r5 was unfrozen design evidence. Layer 2 implements the text and reports code-r5's reading beside it. | No amendment. |
| **F6**, degeneracy cross-tabs | Correct. §3 says *each* degeneracy is cross-tabulated with survivors, but C8's closed list gives the masking-equivalent and nontrivial-stabilizer counts plain. **I missed this in the r4 and r5 re-checks**, where I accepted "closed against §3". | **Owner decision:** either C8's list governs (the later, more specific clause), or a 4-count erratum adds the two cross-tabs (58 counts). I recommend the erratum, in the rule-T bundle. |
| **F7**, C12 per record | PO-L2-9 is valid. | Accept. |
| **F8**, sample rates | L1 N6 makes these Layer-2 configuration constants. | Accept 1 in 1,000. |
| **F9**, budget | See §6. | Owner decision. |
| **F10**, "s0geom's frozen engine" | Layer 1 freezes no code (§5b). The phrase means the engine implementing the frozen rule. The guard and memo edits leave geometry and closure byte-identical, and PO-L2-8 holds. | Accept. |
| **F11**, C12 and C6 on v8 need the grant | Correct, and implemented in the authorized pre-flight. | Accept. |

## 6. Budget and the launch rule (task 6)

**The half-budget threshold is not in Layer 1.** Layer 1 has only S7, "24 runner-hours over at
most 32 shards, with a stop rule", and rule T's cost clause. "At most half the budget, and half the
shard timeout" is a Layer-2 invention, the configuration constant `launch_if_estimate_at_most
1/2`.

**The estimate is consistent with Layer 1.** The 17.5 h figure:
- equals L1 §10's own figures: 4 (convention, rule) pairs × 5–10 h ÷ 6.3, × 2 for `-O`, × 2 for
  overhead, which is about 13–25 h;
- **excludes** C7 on shared-tip records, which under the literal F3 reading is the dominant term.
  The estimate is therefore an underestimate, and launching on it would be unsound.

**A sound launch rule:**
1. **The estimate includes every cost term:**
   - C7 under the chosen F3 scope, using the dry run's `--shared-tips` count;
   - the survivor gates, bounded by a stated survivor cap beyond which the run is INCOMPLETE rather
     than over budget;
   - pre-flight;
   - S1a;
   - the merge.
2. **Launch** iff κ · (total estimate) ≤ S7's budget, and κ · (per-job estimate) ≤ the job timeout.
   κ is a margin fixed by the owner *before* the corrected estimate is computed, set from the
   measured spread of the calibration (two runs differ by about 12%) plus the planted-to-v8 model
   error. The current κ = 2 has no stated basis.
3. **Normal and `-O` replicas** may run as separate jobs. They are replicas of one shard, not
   additional shards, which halves the per-job time without changing total runner time.
4. **The in-run stop rule is kept:** a timeout gives INCOMPLETE and nothing is retried
   automatically.
5. **Fixing the margin.** The margin or budget is a resource decision, not an experimental
   acceptance criterion. It is still decided by the owner and recorded with its reason, so that it
   is not adjusted to fit the estimate.

## Required changes

**L2-R1. PO-L2-10 and the witness cap.**
- **Code.** Replace the first-100 candidate cap in `l2enum` with a per-shard running minimum by the
  C16 key, plus a bounded overflow count.
- **Plan.** Restate PO-L2-10 as:
  > the witness is minimal among records whose computed (carried, or directly recomputed on flagged
  > and sampled orbits) results meet a MISMATCH condition
- **Unproved part.** Strike "follows from PO-L2-3".

**L2-R2. Reference gates on every survivor record.** Run C0 (context), C7, C11 (i), C17 and C18
on every member of every survivor orbit, with each member's reference context. The members'
closures are already computed directly for C8. This meets L1's "every survivor" literally and needs
no reference-equivariance obligation.

**L2-R3. No silent truncation.** Either write all survivor details (to a sharded residue file if
large), or make `survivors_truncated` an INCOMPLETE reason in the merge. The owner's rule is that no
counterexample is excluded.

**L2-R4. The v8 lock: claims and post-hoc verifiability.**
- **(a) Wording.** In §7 and the `s0geom` docstring, replace "only `l2auth.issue_grant` constructs
  a grant" with:
  > no file in the repository other than `l2auth` constructs a grant (static check L2-S1); a grant
  > can be forged in-process, so the lock prevents accidental runs, and the authoritative gate is
  > the CI owner-check job and the post-hoc verification below
- **(b) Echo the owner check.** Shards and `result.json` echo the full owner-check object
  (comment URL, author, `body_sha256`, commit) and the workflow run id.
- **(c) Verify at landing.** The evidence-retention or landing step re-fetches the designation
  comment from the host and checks author and body SHA-256 against the echo. The certificate's
  item 6 records that this check is required.
- **(d) Defence in depth.** `_granted` also requires `manifest_sha256` and `config_sha256` to equal
  the running manifest's `code_digest` and configuration digest.

**L2-R5. The certificate binds commits.** Items 2 and 7 require `preflight.json`, `s1a.json`,
every shard and `result.json` to record one and the same commit, equal to the authorization
artifact's commit (v8 profile). The toy certificate now "holds" with pre-flight at `217f7a40` while
the files sit in `99a9797e`, which shows the gap. At the freeze, regenerate the design evidence at a
recorded commit. The caveat is acceptable for design evidence, but it should be stated in `design/`.

**L2-R6. Cost estimate completeness.**
- `dryrun.json` must include the C7 term under the chosen F3 scope, from `--shared-tips` (no
  grant), and a survivor-gate bound.
- `launch_within_budget` must be computed from the complete estimate.

**L2-R7. The launch-rule constant.** Mark `launch_if_estimate_at_most` as an owner-set resource
margin, not a Layer-1 requirement, and record its basis (§6).

**L2-R8. Reference check on the S1a L3 bound.** Extend S1a's C17 and C18 stream checks to the L3
bound as well, since C9 compares members with it.

**L2-R9. Record the readings.** Record in Layer 2 the readings this review accepts:
- F1: BASE_RESIDUE becomes reachable only after a MISMATCH amendment;
- F4, F5, F7, F8, F10, F11 as accepted above.

Then mirror the owner's rulings on T1, T2, T5, F3 and F6 once they exist.

## Owner decisions (only the owner can make these)

1. **Rule T: an append-only Layer-1 erratum before the Layer-2 freeze.** I recommend it fix:
   - T1: the L3′ bound, with L3 reported;
   - T2: S1a's status as Layer 2 §4 defines it;
   - T5: "a quantity with a seed tip, whose cone contains a source cell".

   T3 and T4 can be notes. It needs a short independent review. The wording "geometric fact only"
   can then be confirmed. The consequence is mathematically sound under these readings.
2. **F3, C7's scope** (an amendment to C7's pass condition). My recommendation:
   - every survivor record;
   - every record whose *production* closure retains a quantity with a shared near tip (cheap,
     non-vacuous wherever ties are retained);
   - a deterministic 1-in-100 sample of records whose initial context has a shared tip;
   - the 1-in-1,000 base sample.

   Individual eliminations are already independently re-checked by C11 (i) and C18. Alternatively,
   keep the literal reading if the v8 `--shared-tips` count shows it fits the budget.
3. **The budget and launch margin** (S7). Either raise S7's 24 runner-hours, or accept a margin κ
   fixed with its basis before the corrected estimate is computed. Normal and `-O` replicas may run
   as separate jobs.
4. **F6.** Either C8's closed list governs, or a 4-count erratum adds the two survivor cross-tabs.
   I recommend the erratum.
5. **Unchanged:**
   - the v8 enumeration, the workflow edit and the full mutant campaign each need separate
     approval;
   - Layer 2 is not proved until reviewed again after these changes.
