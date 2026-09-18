# SI-3 preregistration — Amendment 1: three internal contradictions of the freeze, resolved prospectively, and execution attempt 1 recorded as non-certifying

This is an **execution-affecting control-plane amendment** to
`verification/infrastructure/round-si-3-legacy-seal-retirement/preregistration.md`, made in the
repository's append-only amendment form (§A.36). The frozen preregistration is not edited: this
file is the whole of the change.

Frozen provenance:

- freeze pull request: #675, reviewed head `333735a8e5efb9f3cafbc396b99d18ec954cf3cc` (the first
  draft `4378ae36` plus one corrective commit, appended and not rewritten); authoritative frozen
  preregistration blob:
  `e8e9be66de3a63963418a40189accfbb2c046a92`; preregistration merge commit on `main`:
  `220827b89c038d98dbe643a53c72a8fd00ed8480`, certified by push run 35377254073, and mandated as
  the execution base by the owner on that certification;
- the base the freeze was measured against: `B0` = `d89fff8abb20e2c63a33949b79947650bf47df6a`,
  `SI-2`'s landing; the guard file is the same blob, `163d3e1b6bd859d5c4eebafcbf37d4eaa9005b46`,
  at `B0` and at `220827b8`.

**The frozen preregistration remains byte-for-byte unchanged**, historical and authoritative for
everything this amendment does not name.

## What happened: execution attempt 1, and why it does not certify

An execution was run from exactly `220827b8` on `claude/si3-execution`, in the frozen stage order,
one commit per stage, each stage's dry run taken before the next stage's commit existed, with a
final component adding `R7-SI3`, the result note, the tag map and the ledger entry:

| commit | content |
|---|---|
| `bbf68e495b3362c1f9bbfced96dc77239a9505b8` | stage 1 |
| `124ccc66810e1728915f18be49e79f3c8dbe23c4` | stage 2 |
| `e08bf0f0550af19ee48435c9d58bd3b330ff871e` | stage 3 |
| `a10a6cfd58e92379a0748500a16058b4cd4b1d4d` | stage 4 |
| `03e94be29c911fcd1a0408b7236dd043a5de8e79` | stage 5 |
| `962fdce606335605da2aaf7c117586166f7e0d8c` | stage 6 |
| `76bf328a19c7354cbb0a120b4a374c16369aa1a1` | final component; the head |

At that head the guard file ends `ALL CHECKS PASS` with 93 tags, `R7-SI3` reporting every target's
predicted outcome and `SI3-7` `MAP-PRESERVED` over the base's 92 tags, and the release gate passes
17 of 17. The head was pushed for review and **no execution pull request was opened**.

**That head is `SI-3` execution attempt 1: informative, and not certifiable.** A green guard at the
final head does not prove conformity to the frozen control plane when the freeze contains
contradictions the execution resolved implicitly. Three were exposed by the attempt and confirmed
independently by the owner. Nothing from attempt 1 becomes `SI-3` result evidence except the
observations below, which motivate this amendment. Its branch is preserved as it is — not
force-pushed, not rewritten, not repurposed — and nothing resumes from it.

### The three contradictions, as observed

1. **`SI3-2` was mis-scored at its own stage.** The frozen target says that after stage 2 no
   genuine identifier read of any of the sixty names exists outside the shadow and comparator
   functions that stage 3 deletes. At the stage-2 commit `124ccc66` the frozen tokenization counts
   182 genuine reads: the 116 shadow-ancestry and 60 comparator reads still inside the functions
   stage 3 deletes, **plus six** inside `R7-RNT`'s clause-9 self-test block — which the freeze's
   reads table lists in the *other* class and disposes of as "deleted above" with the comparator,
   at stage 3. Those six were neither rebound nor retired at stage 2, so the stage-2 target as
   written did not hold at the stage-2 commit; the head reaches zero, and attempt 1's result note
   reported `REBOUND` on the head's count. The frozen stage-2 outcome cannot honestly be reported
   as `REBOUND` under the frozen language.
2. **The shadow-recorder deletion conflicts with negative case 14.** The freeze's function
   inventory says `_si2_shadow_integrity` and `_SI2_SHADOW_INTEGRITY` are deleted. Both are defined
   inside the `SI2-AUTHORITY` region, and negative case 14 permits exactly the two `R2`/`R3` wiring
   edits there and nothing else. Attempt 1's stage 3 kept the bound and retained the function and
   the list with zero callers, reporting it as a discrepancy. The two frozen rules cannot both be
   satisfied.
3. **The stage-3 deletion of the clause-9 block is incompatible with the stage-3 all-`PASS` gate.**
   The stage table says the clause-9 block is deleted at stage 3, and stage 4 may not begin until
   stage 3's dry run has every pre-existing tag `PASS`; but two statements of that block are two
   of the sixty-one in `SI2-6`(b)'s frozen inventory, which is retired only at stage 4 and holds
   until then. Attempt 1's first stage-3 dry run deleted the block whole and `SI2-6`(b) reported
   `LEGACY-ALTERED` at 59 statements; restoring the two rebindings with their probe and restore
   lines gave 61 and every tag `PASS`, and the residue was deleted at stage 4. The freeze's stage
   table and its gating condition cannot both be met by a stage-3 deletion of the whole block.

Attempt 1's result note stated two discrepancies and every prediction held. Under the frozen
target language that statement is not correct: the third issue is the stage-2 target itself, and
a target whose frozen wording did not hold at its own stage is not "as predicted".

### Observations from attempt 1 that this amendment records and does not act on

- `SI1-5` still reproduced at attempt 1's stage 4, after every legacy constant was gone: `SI-1`'s
  census harness ran the generic archive-mode and quiet-ancestry helpers on each record's own
  fields and never read a constant, and its control census ran on synthetic repositories. The
  freeze's stated reason for retiring `SI1-5` — that its old side reads the constants — is wrong
  in mechanism for `SI-1` (it is right for `SI-2`'s `U4`, which transcribes the head's guard text).
  The **disposition stands unchanged**: the pinned-artifact design was adjudicated on its own terms
  and is what the owner agreed to; the re-execution's result note records the mechanism as a
  finding about the freeze's reasoning.
- The freeze's non-gating count of seventy-eight `(STRING, name)` pairs over twenty-five names at
  `B0` reproduces exactly by attempt 1's tokenization; counting every legacy-shaped name rather
  than the sixty gives 87. Neither gates, as frozen.
- Two implementation defects of attempt 1 that were not control-plane matters: the stage-1 patch
  scoped `R7-SI2`'s record-count contracts but not `SI2-4`'s census input or `SI2-8`'s `#140`
  probe, both inside the table's twenty-three-record row, caught by the stage's first dry run and
  fixed in the same uncommitted stage; and the `R7-SI3` guard's negative case 2 wrote the shadowed
  keyed-call form as one string literal, which the whole-file `shadow=` check then matched in the
  guard's own source — `SI-2`'s defect 7 in a new place — fixed by assembling the literal from
  fragments. The re-execution carries both fixes from the start and records neither as new.

## The adjudication

For `SI-3` execution only. Everything not named here stands as frozen.

1. **The `SI2-AUTHORITY` bound admits exactly two named dead-object deletions.** Inside the region,
   this amendment authorizes, in addition to the two `R2`/`R3` wiring edits, exactly two deletions:
   the declaration `_SI2_SHADOW_INTEGRITY = []` (the list) and the definition
   `def _si2_shadow_integrity(...)` with its body (the recorder). Both are dead objects once the
   eight recording call sites go: nothing in `U1`–`U5` reads them, and no verdict depends on them.
   They are deleted at stage 3, with the eight call sites and the comparators. **Negative case 14
   becomes:** the region's text at the head, with exactly the two wiring edits reverted, must equal
   the region's text at the mandated base with exactly those two definitions excised, and must
   differ from the base's region before reverting; any other difference fails, and a round stem in
   the region fails `_si2_region_no_stem` as before. All other region text is frozen. The function
   inventory's row "shadow-integrity recording — 1 function, 1 list, 8 call sites" is now
   executable as written.

2. **The clause-9 retirement is split across stages 3 and 4, explicitly.** Stage 3 removes the
   comparator-bearing logic and calls of `R7-RNT`'s clause-9 block — `_rnt_prior_seals`, the
   `_si2_shadow_integrity('R7-RNT', …)` recording lines, the comparison loop that exercised the
   comparator under the rebinding — and **leaves the legacy residue** that `SI2-6`(b) needs to
   remain 61 of 61 as text and in order: the pin probe, the two rebindings, the restore, and the
   restore checks. That residue is these lines, exactly, in this order, and nothing else:

   ```
   _rnt_pin_probe = (_RNT_SEALED_HEAD, _RNT_MERGE)
   _RNT_SEALED_HEAD = 'f' * 40
   _RNT_MERGE = 'e' * 40
   ok_rnt &= _rnt_execution_ancestry.__doc__ is not None
   _RNT_SEALED_HEAD, _RNT_MERGE = _rnt_pin_probe
   ok_rnt &= (_RNT_SEALED_HEAD, _RNT_MERGE) == _rnt_pin_probe
   ok_rnt &= ('f' * 40, 'e' * 40) != _rnt_pin_probe
   ```

   The `ok_rnt &= _si2_integrity_ok()` lines around it are among the eight `U5` gates and stay in
   text throughout. Stage 4 removes the residue together with the sixty-two legacy assignment
   statements, of which the residue's two rebindings are two. The freeze no longer says the whole
   block disappears at stage 3. Hazard H1's mirror trap is restated for the split: at no commit of
   the round may a rebinding of `_RNT_SEALED_HEAD` or `_RNT_MERGE` be present without its pin, and
   the statement count is 62 at every commit before stage 4 and 0 from stage 4 on.

3. **`SI3-2` covers the reads whose disposition at stage 2 is rebinding or retirement.** After
   stage 2, no genuine identifier read of any of the sixty names exists outside (a) the shadow and
   comparator functions stage 3 deletes and (b) the **enumerated deletion-scheduled residue** of
   point 2. The residue's six reads — two in the pin probe, two in the tuple restore, two in the
   restore check — are permitted until their staged retirement at stage 4, and are **not counted as
   rebound**. The mechanical bound: at the stage-2 commit and at the stage-3 commit, the genuine
   reads outside the shadow and comparator functions number **exactly six** and lie on the residue's
   lines and nowhere else; at the stage-4 commit and every commit after, they number zero. The
   re-execution measures the bound at each of those commits by the frozen tokenization and records
   the counts with the commit SHAs in the result note; `R7-SI3` enforces zero at the head, and the
   negative case below keeps the exception from growing. `REBOUND` means the bound held at every
   commit; `REBOUND-PARTIAL` means it did not.

4. **`76bf328a19c7354cbb0a120b4a374c16369aa1a1` is recorded as the non-certifying first execution
   attempt** that exposed the three control-plane inconsistencies above. Its seven commits are
   listed above for the record. Nothing from it becomes `SI-3` result evidence except the
   observations in this amendment; its guard verdicts, its tag map, its result note and its ledger
   entry are not carried forward, and the re-execution rebuilds each from its own base. The branch
   `claude/si3-execution` is preserved unmodified and is not the re-execution's branch.

5. **The bases.** `220827b89c038d98dbe643a53c72a8fd00ed8480` becomes the **certified
   preregistration merge from which nothing resumes**. The **certified merge commit of this
   amendment on `main`** becomes the new mandated `SI-3` execution base, superseding `220827b8` for
   execution-base purposes only, exactly as `SI-2`'s amendments superseded their predecessors. `R2`
   declares that commit; `R3`'s baseline is the seals tree at that commit, which is the same
   twenty-three records, `verification/seals/` still at tree `e4fb69db…`.

6. **Two blobs, two drift controls.** The re-execution's first act verifies **two** frozen blobs at
   the new mandated base — the original preregistration `e8e9be66…` and this amendment's blob — and
   `R7-SI3` pins and enforces both, each independently, each with its own one-byte drift control.

## Superseded clauses

For `SI-3` execution only. Everything not named here stands as frozen.

1. **Negative case 14**: superseded by point 1. The region at the head with the two wiring edits
   reverted equals the base's region with the two named definitions excised.
2. **The function inventory's third row** ("shadow-integrity recording") and **the stage-3 row of
   the stage table** ("the shadow-integrity recording … deleted"): now executable under point 1;
   the function and the list are deleted at stage 3.
3. **The stage-3 row of the stage table** ("… and `R7-RNT`'s self-test block deleted"), **the
   reads table's comparator row** ("together with `R7-RNT`'s clause-9 self-test block"), **the
   supersession table's `R7-RNT` row** ("deleted with the comparator"), and **hazard H1**'s last
   sentence ("the self-test block is deleted as a block"): superseded by point 2. The comparator-
   bearing lines go at stage 3; the enumerated residue goes at stage 4.
4. **`SI3-2`**: superseded by point 3, with the reads table's *other*-class disposition read
   accordingly — the six `R7-RNT` reads are "deleted at stage 4", not "deleted above" at stage 3.
5. **The mandated execution base** (the freeze's opening paragraph and precondition 6's reading):
   superseded by point 5.
6. **The first act and the guard's pins** ("its first act is to verify this preregistration's blob";
   "It carries this preregistration pinned by blob"): extended by point 6 to two blobs, each with
   its own drift control.

## Negative suite: two cases added

Numbered in continuation of the frozen fourteen:

15. The `SI2-AUTHORITY` region at the head differing from the mandated base's by anything other
    than the two wiring edits and the two named deletions — one more line deleted, one line added,
    one of the two definitions retained — **fails** case 14 as amended. The mutation control
    reinstates one of the two definitions and requires the amended check to fail on it.
16. A seventh genuine read outside the shadow and comparator functions at the stage-2 or stage-3
    commit, any such read off the residue's lines, or any residue read surviving the stage-4 commit
    — **fails `SI3-2`** (`REBOUND-PARTIAL`), and a surviving residue statement **fails `SI3-4`**.

## Preconditions: three added

Numbered in continuation of the frozen nine:

10. The mandated base is the certified merge commit of this amendment and not `220827b8`, and its
    second parent is this amendment's reviewed head. `220827b8` is recorded as the certified
    preregistration merge from which nothing resumes.
11. At the mandated base, `_SI2_SHADOW_INTEGRITY` and `def _si2_shadow_integrity` are present inside
    the `SI2-AUTHORITY` region, so their deletion is this round's own recorded edit; `R7-RNT`'s
    clause-9 block is present with its residue lines exactly as enumerated in point 2; and the guard
    file is still blob `163d3e1b…`.
12. The re-execution branch is a fresh branch cut from the mandated base — not `claude/si3-execution`
    — and no commit of attempt 1 is reachable from it.

## What this amendment does not touch

- No pin in the frozen start-state table changes; `verification/seals/` is still the twenty-three
  records at tree `e4fb69db…`, and the guard file is still `163d3e1b…` at `220827b8`.
- `R1`, `R2`, `R3`, `U1`–`U5`, the stage order and its gating conditions, targets `SI3-0`, `SI3-1`
  and `SI3-3` to `SI3-7`, the predictions and their strengths, the supersession table except its
  `R7-RNT` row, the non-licences, hazards H2–H8, the legacy inventory's counts, and the landing
  shape `E` → `L` → `P` are untouched.
- The `SI1-5` and `SI2-4` dispositions stand; the `SI1-5` mechanism is recorded above as an
  observation and changes nothing.
- No frozen `SI-1` or `SI-2` document is edited. `SI-1`'s and `SI-2`'s `census.json` are not
  regenerated and not repinned.
- No seal constant is altered, added or removed by this amendment. No manifest record is added or
  changed. `SI-3` remains SEALING.
- `SI-3` is not Act 21, and Act 21 is unaffected.

## Execution discipline after this amendment

This amendment is frozen by exact commit SHA and blob SHA at its own review, and merged to `main`
with a merge commit on explicit owner direction naming the exact head. After that merge and its
`main` push run are certified, `220827b8` is discarded as an execution base, the re-execution is
started on a fresh branch from **that** merge commit and from no other, its first act is the
two-blob verification of point 6, and it runs the six stages in the frozen order under the stage
table as amended by points 1–3, taking each stage's dry run before the next stage's commit exists.
Its result note reports the residue bound at each stage commit by SHA, reports `SI3-2` under point
3, and records attempt 1 under point 4 as history and not as evidence. If any pre-existing tag's
verdict differs from the base's at any stage, `SI3-7` is `MAP-CHANGED`, the round stops, and this
amendment authorizes nothing further.
