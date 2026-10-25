ACCEPT WITH NITS — a97c852a3a5305a8b4a69eac7173ea526f08624b (preregistered scope control for a2_memory_v8; single parent 19a33d6fff854deadb9cc4cdb4f20b144202d5e6)

Overall verdict on 1dfec979721336cc9f0ce703b544f9d6be8e906c..a97c852a3a5305a8b4a69eac7173ea526f08624b: ACCEPT WITH NITS.

- Both re-check-3 blockers are resolved: scope identification and attribution.
- The owner's wrong-depth-bound scenario is caught.
- A5 is a distinct limit, inherent to any second implementation, and it is disclosed.
- Replay is byte-identical.
- One propagation item stays open outside the package: `CURRENT-HANDOFF.md` lines 67–69. See section 5.

Read-only review; `python3 -I -B` runs from empty directories on files exported with `git show a97c852a:<path>`
into `tree/`.
- Following §A.40, I ran only three targeted mutants of my own (`mut6.py`; outputs in `work/m6/`), not the full
  sets.
- The leaf diff is in `leafdiff.out`.

## Changed-file inventory

| range | files | notes |
| --- | --- | --- |
| `19a33d6f..a97c852a` | 7 files modified (+119/−17): `PROVENANCE.json`, `REPORT.md`, `SHA256SUMS`, `checks.py`, `mutants/mutants.out`, `mutants/run_mutants.py`, `result.json` | `PLAN.md` byte-identical (b7f7eaae…a275) |
| `1dfec979..a97c852a` | 7 files added under `a2_memory_v8/` (1,900 insertions) | |
| `49e1a119..a97c852a` | 8 files | nothing outside `a2_memory_v8/` |

## 1. Owner's requirement: wrong depth bound, implementation and reported result changed consistently

| mutant | change | result |
| --- | --- | --- |
| T1 (mine) | every reported power-rule half depth edited one block early, directly in the reported family | exit 2, VOID "audit recomputed depth equals reported (power_rule_…)" |
| T2 (mine) | preregistered nc/(1+nc) depth one block early, in the rule and its own minimality check together | exit 2, VOID "audit recomputed depth equals reported (certified_T_above_half…)" |
| M15, M17, M18, M21–M25 (author's) | wrong-bound mutants of the same scenario | recorded as caught in `mutants/mutants.out`, which the author's runner regenerates; the earlier re-checks ran the W- and A-sets on predecessors of this code |

In this scenario the main rules and the reported values move together. The audit stays as written, and it detects
the change in three ways:
- it recomputes BC and every depth from the stated definitions;
- it checks the certificates against exact TV at the reported depths;
- it requires the 48-member scope.

**A5 is a different case.** A5 edits the control's own coding of the definition, the audit's formula, so that it
agrees with the wrong main rule. No independent implementation can survive an edit to itself. Only an exact
certificate inside the affected range could catch it, and there is none: ⌊n/20⌋ = 0 for every n ≤ 16, and the k=1
shifts remain true. So A5 is an inherent limit, not the owner's scenario. REPORT now states it, and says that
agreement of both codings with the definitions stated in REPORT rests on review. That is the correct disclosure.

## 2. Labels, omissions and parameter definitions

**The scope check.** `preregistered_scope()` does the following:
- checks PLAN.md's SHA-256 against the pinned value before parsing it;
- parses "The family RS(B,k), B in {2,3,4}, k = 1..16";
- requires both threshold sentences to be present;
- requires `HALF` = 1/2 and `TENTH` = 1/10;
- requires exactly 48 keys.

`run()` requires the reported member keys and the enclosure keys to each equal that set. It then requires the
audited keys, and the audit's member count, to equal it too. `independent_audit` VOIDs on a missing member.

**What is caught.**
- The author's M26–M30 (my L1, L2, L3b, L5, L6) are recorded as caught on the scope labels.
- From the earlier rounds, a swap (L3) is caught by the block-TV digest and a threshold change (L4, A1) by the
  depth recomputation and the exact crossing.
- My T3 remaps labels: member (B,k) carries the block law of k+1. It exits 2 VOID, but through the new fail-closed
  handler ("control failure from an internal inconsistency (KeyError)"), not a named control. That is acceptable,
  since the failure is closed, but it is the weakest catch (nit a).

**What remains.** The scope literal can be changed only by editing PLAN.md together with `PLAN_SHA256` in
`checks.py`. That edits the frozen preregistration, which is visible against `1dfec979`, against PROVENANCE's
`plan_sha256` and against `SHA256SUMS`. `checks.py` does not cross-check its pin against PROVENANCE or git
(nit b). This is inherent at the same level as A5.

## 3. Attribution

**What REPORT and `plan_commit_note` now state on the repository's authority:**
- PLAN.md was committed alone at 1dfec979, before any other file of the package. I verified this: 1dfec979 adds
  only PLAN.md.
- The execution code postdates it.

**What they attribute to the author.** Everything else is now introduced with "By the author's account (no
artifact of the exploration is retained, and the repository cannot corroborate it)":
- the exploration's parameters;
- its findings;
- the steer to RS(B,k);
- "did not compute on RS(B,k), on the census populations or on the decision rule".

The "did not compute on" bullet also carries "(author's account)". This matches what the provenance supports.

Nits (c):
- REPORT's "the following holds" under that heading asserts rather than reports. "The author reports the
  following" is more consistent.
- "The execution code postdates it" is established only for commit order. Say "was first committed after it".

## 4. Replay and hygiene

- Normal and `-O` replays from empty directories are byte-identical to `result.json` (about 4 min each on a shared
  machine).
- `SHA256SUMS` verifies all 7 files, and `PROVENANCE.json` parses.
- Leaf diff 19a33d6f→a97c852a:
  - 16 leaves added: the 7-member T>1/2 exact-TV list and the parsed scope block.
  - 1 changed: `schema` v4→v5.
  - 0 removed, and no value changed.
- No absolute paths, emails, IPs, tokens or `__pycache__`.
- `tools/duplicate_check.py`, `tools/voice_check.py` and `tools/artifact_placement_check.py` all pass.
- The clone's worktree is clean at a97c852a.
- The re-check-3 leftovers (`tmp_pack_*` and `gc.log.lock`) are no longer present.

## 5. CURRENT-HANDOFF propagation (open)

`CURRENT-HANDOFF.md` (`states-dynamics-audit-20261024/`) is unchanged in `49e1a119..a97c852a`. Its §"Depth
extension of the finite controller" (lines 52–69) ends with lines 67–69:

> Arbitrary depth / is therefore open for controllers that carry randomness across slots and for / growing
> per-slot blocks; the h=3 certificate above is unchanged.

That sentence is now partly answered. Once the package is accepted and its review evidence retained, replace lines
67–69 with a paragraph like this:

> `a2_memory_v8/`, author head `<accepted head>`, with internal reviews retained under `a2_memory_v8/review/`,
> proves that every controller whose whole persistent state is finite, with a time-independent update and B fair
> fresh bits per slot, also has T(h)→1 on this protocol. The obstruction is arithmetic: dyadic fresh randomness
> against a run law with ratio 4/5. It holds for resets that carry no private randomness across slots, whatever
> their record dependence, and for every finite-state controller. The retained-seed reset, granted the target
> cuts, escapes it with linearly growing private memory. Arbitrary depth remains open for bounded private memory
> with unbounded public state (an unbounded clock or full-record dependence), for time-dependent updates, growing
> per-slot blocks and non-dyadic sources, and for the least memory growth that keeps T bounded. The h=3
> certificate above is unchanged.

Lines 54–66 stay as they are. They state v7's result and remain correct.

The citation of internal reviews requires the review records to be retained on `main` beside the package, as
`a2_depth_v7/review/` is (§A.42). At present they exist only in reviewer scratch, so either retain them or drop
the clause. The audit root's `SHA256SUMS` does not list `CURRENT-HANDOFF.md`, so editing it breaks no hash.

## Nits

- (a) T3 (label remap) is caught by the generic fail-closed handler, not a named control. Consider a named check
  that each reported member's block-law record length equals its k.
- (b) `PLAN_SHA256` in `checks.py` is not cross-checked against PROVENANCE's `plan_sha256` or the 1dfec979 blob.
- (c) Attribution phrasing; see section 3.
- (d) `CURRENT-HANDOFF.md` lines 67–69, and retention of the review records; see section 5.
