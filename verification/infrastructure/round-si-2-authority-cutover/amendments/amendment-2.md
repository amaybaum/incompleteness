# SI-2 preregistration — Amendment 2: the `_SI2_BASE` allowance in `R7-SI1`'s seal-constant containment contract, and the readings Amendment 1 left open

This is an **execution-affecting control-plane amendment** to
`verification/infrastructure/round-si-2-authority-cutover/preregistration.md`, made **before
execution began**, in the repository's append-only amendment form (§A.36). It follows Amendment 1
and touches neither the frozen preregistration nor Amendment 1: this file is the whole of the
change.

Frozen provenance:

- freeze commit: `71745dbe26c526e24e72dc370f6ec1813fa41ed4` (#669); authoritative frozen
  preregistration blob: `bfcd43831d887c006eab64c9a4b8b5f35ff41c9a`; preregistration merge
  commit on `main`: `da9d69d60b19482abfeb27b16af5aaebebba0e83`, certified by push run 35321848352;
- Amendment 1 head: `37f573896c94510bcbe8c7d469ab8fa467c65e98` (#671); authoritative frozen
  Amendment 1 blob: `9d05509d8fb84d9007c73b40a062bbdb7b6c36ea`; Amendment 1 merge commit on `main`:
  `9ca82958cfaa3ff926d8a80baf2ee22eb468a917`, certified by push run 35340667434.

**Both frozen documents remain byte-for-byte unchanged**, historical and authoritative for
everything this amendment does not name. No stage of `SI-2` was executed, no guard clause was
written, no manifest record was committed, no census was regenerated, and nothing was pushed between
the Amendment 1 merge and this amendment. Three uncommitted measurements were taken and are recorded
below; their artifacts were discarded and nothing from them was kept.

## What was measured, at `9ca82958`, uncommitted

An execution worktree was cut from exactly `9ca82958` and both frozen blobs were verified there.
The eight frozen preconditions and Amendment 1's two held at that base, with precondition 6 read as
stated in point 6 below. Three runs of the guard file were then taken, none committed:

| run | tree | result |
|---|---|---|
| 1, the frozen one-verdict dry run | `SI1.json` present, `R7-SI1` scoped per Amendment 1 point 1, nothing else | **`ALL CHECKS PASS`**, 91 tags, `R7-SI1` `PASS`, scope line reporting 22 transcribed records, 1 authorized addition, 0 unauthorized; SI-1's census reconstructs identically |
| 2 | run 1's tree plus **one line**, `_SI2_BASE = '9ca82958cfaa3ff926d8a80baf2ee22eb468a917'` | **`FAILURE`**: 91 tags, 90 `PASS`, **`R7-SI1` `FAIL`**, the only failing tag |
| 3 | the pristine base | `ALL CHECKS PASS`, 91 tags, `R7-SI1` `PASS` |

Runs 1 and 2 differ by that single line, so the failing contract is isolated by construction. It is
`R7-SI1`'s **N13**, `_si1_seal_constants_intact`, at lines 24696–24713 of the guard file as of
`9ca82958`: it parses every module-level `_<STEM>_(BASE|SEALED_HEAD|MERGE) = '<40 hex>'` statement
at the head and at SI-1's mandated base `99ab6370`, requires the base's set to be contained in the
head's, and requires the difference to be **exactly** `{('SI1', 'BASE', _SI1_BASE)}`. A replica of
that predicate over the same two sources gives the difference
`{('SI1', 'BASE', 99ab6370…), ('SI2', 'BASE', 9ca82958…)}` once `_SI2_BASE` is present, and the
equality is false.

Run 1 is the dry run Amendment 1's superseded clause 2 requires, and it passed: the one-verdict
allowance was used and nothing else changed. Run 2 is the next frozen requirement after it.

## Why this is an adjudication and not a repair

Two frozen requirements cannot hold at once on any execution head:

- the frozen preregistration's guard section requires `R7-SI2` to carry `_SI2_BASE` — "It carries
  `_SI2_BASE`, act 10's strengthened ancestry check … and no seal triple of its own" — and its
  chronology section requires that constant to be what the bootstrap guard certifies against;
- `R7-SI1`'s N13, frozen at SI-1's landing, admits exactly one addition to the seal-constant set,
  SI-1's own base, and fails any second one.

Amendment 1 scoped SI-1's **manifest** cardinality and integrity surface. It did not touch N13,
which is a **seal-constant** containment contract, so relaxing N13 under Amendment 1 would have been
an unrecorded guard relaxation, which the owner's path-D adjudication forbids. The owner adjudicated
a second append-only amendment, analogous to the first, with the scope fixed as the points below.
Paths **rejected**: any form of `_SI2_BASE` that evades N13's parser, any change to N13 not recorded
here, and any restart of execution from `9ca82958`.

## The adjudication

1. **Exactly the N13 delta.** For `SI-2`, N13's exact allowed-addition set becomes
   **`{_SI1_BASE, _SI2_BASE}`** rather than `{_SI1_BASE}`. Everything else in N13 stands: every
   assignment inherited from SI-1's mandated base `99ab6370` must still be present and
   value-identical (containment); `_SI2_BASE` must equal **SI-2's newly mandated execution base**,
   which is this amendment's certified merge commit under point 7; **no `_SI2_SEALED_HEAD` and no
   `_SI2_MERGE` may exist**, not as `None`, not at all; and **any third new legacy-style assignment
   still fails**. This does not make `SI-2` sealing: `_SI2_BASE` is its required chronology base,
   and `SI-2` still creates no sealed-head or merge state. **This amendment does not authorize the
   retirement round's future deletions**: that round removes the sixty-one legacy statements, which
   N13's containment half refuses, and it must prospectively own and supersede N13 itself under
   the protocol `SI2-7` writes.

2. **Amendment 1's point 1 is extensional.** It scopes SI-1's twenty-two-record cardinality
   contracts as a class, not only the lines its measurement narrative enumerated. Therefore
   **N11**'s `len(stems) == 22` (the stem list the no-stem check reads, line 24676) and the **#140
   probe**'s 22-record / 22-merge-base observation (lines 25058–25060) are evaluated over the
   original twenty-two SI-1 transcriptions, exactly as the contracts Amendment 1 named. Their
   substantive contracts do not change: N11 still proves the generic region carries no round stem,
   and #140 remains `RESTATED-ONLY`; the `SI1.json` row is simply outside those historical SI-1
   measurements. Recorded here so there is no future ambiguity; run 1 above passed with both scoped
   this way.

3. **`SI2-3` includes SI-1's own chronology clause.** The frozen language is explicit: every
   ancestry and archive clause of a round represented in the manifest moves to `U3`, with only
   `R7-SI2` excluded. After `SI2-1`, SI-1 is represented. Amendment 1's "no other clause of `R7-SI1`
   changes" bounds the scoping edit and creates no SI-1 exemption from `SI2-3`, because Amendment 1
   separately preserves `SI2-3` untouched. So `_si1_execution_ancestry` becomes a call to `U3` keyed
   on the `SI1` record; its old implementation — the strengthened execution check against
   `_SI1_BASE` — remains alongside it as the **shadow `SI2-4` relies on** and gates nothing.

4. **The validator relocation and the derivation hook are permitted** as implementation of the
   already-frozen `U3` requirement. The marker-bounded `SI1-VALIDATOR` region (`SI1-VALIDATOR-BEGIN`
   to `SI1-VALIDATOR-END`) may be moved early enough in the guard file that prior-round clauses can
   invoke it, and is preserved unchanged except for **the narrow O2 hook needed to inject the
   derivation implementation**: O2's default behaviour remains the original target-only
   `_si1_derive`, and `U3` invokes that same validator with `U2`. That is the most literal
   implementation of "SI-1's O2 with U2 in place of the target-only derivation". SI-1's existing
   negative suite and default O2 route must still reproduce their old behaviour, so SI-1's
   `census.json` still reconstructs identically; the marker and no-stem contract remain active after
   the relocation.

5. **The nested subprocess cost is accepted.** `SI2-6`(a) runs the base's guard file, which itself
   runs its base's guard file; each infrastructure round nests one level deeper. These are
   evidence-bearing checks and are **not optimized away** to shorten CI. If runtime itself becomes a
   CI failure, the round stops on that actual result rather than weakening the measurements.

6. **Frozen precondition 6 is a provenance fact, not a live-tip requirement.** It preserves that
   `B0` is `66eea646fcbf242df89b168bcce3336ff1b77802` and that its second parent is
   `d75427aece402e1629d56d1ca96fbc8d3c8101e8`; it does not require live `main` to remain there,
   which Amendment 1 necessarily moved it past. Checked at the mandated base as: `66eea646` has
   that second parent and lies on the mandated base's first-parent spine.

7. **The bases.** `9ca82958cfaa3ff926d8a80baf2ee22eb468a917` becomes the **certified
   pre-Amendment-2 base from which nothing resumes**. The **certified merge commit of this
   amendment on `main`** becomes the new mandated `SI-2` execution base, superseding `9ca82958` for
   execution-base purposes only, exactly as Amendment 1 superseded `da9d69d6`. `da9d69d6` remains
   the certified preregistration merge; `9ca82958` remains the certified Amendment 1 merge.

8. **Three blobs, three drift controls.** Execution's first act verifies **three** frozen blobs at
   the new mandated base — the original preregistration `bfcd4383…`, Amendment 1 `9d05509d…`, and
   this amendment's blob — and `R7-SI2` pins and enforces all three, each independently, each with
   its own one-byte drift control.

## Superseded clauses

For `SI-2` execution only. Everything not named here stands as frozen or as amended by Amendment 1.

1. **Amendment 1, superseded clause 3 (the mandated execution base)** and **Amendment 1,
   precondition 10**: superseded by point 7 above. The mandated base is this amendment's certified
   merge commit; `9ca82958` is the certified pre-Amendment-2 base from which nothing resumes.
2. **Amendment 1, superseded clause 4 (the first act, two blobs)**: extended by point 8 to three
   blobs.
3. **Amendment 1, superseded clause 5 (`R7-SI2` pins both blobs)**: extended by point 8 to three,
   each with its own drift control.
4. **Frozen precondition 6**: read per point 6.
5. **`SI2-1`, as extended by Amendment 1**: stage 1 additionally carries the N13 delta of point 1,
   as the second and last authorized edit to a prior round's guard. `MANIFEST-DEVIATED` also covers
   an N13 allowance wider than `{_SI1_BASE, _SI2_BASE}` or any N13 change beyond the allowed-addition
   set.
6. **`SI2-6`(a), as extended by Amendment 1**: the first post-Amendment-2 dry run is part of the
   target. It includes `SI1.json`, all of Amendment 1's scoping, the exact N13 `_SI2_BASE` allowance,
   and `_SI2_BASE` itself, and **all 91 pre-existing tags must remain `PASS`, `R7-SI1` included**.
   Any further pre-existing verdict change is `MAP-CHANGED` and stops the round.

## Negative suite: one case added

Numbered in continuation of the frozen eleven and Amendment 1's twelfth:

13. A **third** new legacy-style assignment at the head beyond `_SI1_BASE` and `_SI2_BASE` — a
    `_SI2_SEALED_HEAD`, a `_SI2_MERGE`, or any `_<STEM>_(BASE|SEALED_HEAD|MERGE)` for a stem not
    present at `99ab6370` — **fails N13 as amended**, as does any inherited assignment removed or
    re-valued. This is the mutation control that proves the allowance is a set of exactly two and
    not a blanket exemption.

## Preconditions: two added

Numbered in continuation of the frozen eight and Amendment 1's ninth and tenth:

11. N13 is **unamended** at the mandated base: `_si1_seal_constants_intact` still reads
    `now - was == {('SI1', 'BASE', _SI1_BASE)}`, so the allowance is this round's own recorded edit
    and not something already present. Verified at `9ca82958` (line 24713); `SI2-0` re-verifies it
    at the new base.
12. The mandated base is the certified merge commit of this amendment and not `9ca82958`, and its
    second parent is this amendment's reviewed head. `9ca82958` is recorded as the certified
    pre-Amendment-2 base from which nothing resumes.

## What this amendment does not touch

- No pin in the frozen start-state table changes; all six were re-verified at `9ca82958`.
- The derivation rule, the four adjudicated divergences, `U1`–`U5`, the stage order, targets
  `SI2-0` and `SI2-2` to `SI2-8` except as named above, the predictions, the non-licences, the
  hazards, the legacy inventory, and the retirement round are untouched.
- Amendment 1's six points stand in full; its scoping is confirmed, not widened, by point 2.
- SI-1's `census.json` is not regenerated and not repinned. `#141` at `RESTATED-AND-FAILS` is not
  rewritten.
- No seal constant is altered, added or removed by this amendment. `SI-2` remains NON-SEALING.
- Act 21 remains closed.

## Execution discipline after this amendment

This amendment is frozen by exact commit SHA and blob SHA at its own review, and merged to `main`
with a merge commit on explicit owner direction naming the exact head. After that merge and its
`main` push run are certified, `9ca82958` is discarded as an execution base, `claude/si2-execution`
is restarted from **that** merge commit and from no other, and its first act is the three-blob
verification of point 8. Its first pre-commit dry run is the one in superseded clause 6. If it
reports anything other than all 91 pre-existing tags `PASS`, `SI2-6`(a) is `MAP-CHANGED`, the
cutover stops, and this amendment authorizes nothing further.
