# SI-2 preregistration — Amendment 1: scope `R7-SI1`'s frozen manifest contracts to the records `SI-1` transcribed

This is an **execution-affecting control-plane amendment** to
`verification/infrastructure/round-si-2-authority-cutover/preregistration.md`, made **before
execution began**. It follows the repository's append-only amendment form (§A.36): the frozen
preregistration is not edited, and this file is the whole of the change.

Frozen preregistration provenance:

- freeze commit: `71745dbe26c526e24e72dc370f6ec1813fa41ed4` (#669);
- authoritative frozen blob: `bfcd43831d887c006eab64c9a4b8b5f35ff41c9a`;
- preregistration merge commit on `main`: `da9d69d60b19482abfeb27b16af5aaebebba0e83`, certified by
  push run 35321848352.

**The frozen preregistration remains byte-for-byte unchanged**, historical and authoritative for
everything this amendment does not name. No stage of `SI-2` was executed, no guard clause was
written, no manifest record was committed, and no census was regenerated between the preregistration
merge and this amendment. One uncommitted dry run was taken and is recorded below; its artifact was
removed and nothing from it was kept.

## What was measured, at `da9d69d6`, uncommitted

`SI1.json` was written in the base-only record format `SI2-1` authorizes — `kind: "base-only"`,
`base` = `99ab6370470ed9d9e4005551581c6c8c18e54bd2` — and the guard file was run once, at
`da9d69d6`, with no other change.

`R7-SI1` **failed**, with `edge_rigidity_probe: FAILURE`, while every validator agreed. The `SI-1`
census reported 23 of 23 records agreeing — 18 `sealed` on lifecycle, 5 `base-only` on schema,
pinned base and record integrity — and the four control divergences (7, 13, 20 and control 10) were
unchanged in direction. What failed were `SI-1`'s **frozen manifest-cardinality contracts in its own
guard**, at `verification/lean/edge_rigidity_probe.py` as of `da9d69d6`:

- `len(_si1_recs) == 22` (line 24873);
- `sealed == 18` and `base-only == 4` over the whole manifest (lines 24874–24875);
- the record-axis counts, 18 `lifecycle` and 4 `schema+base+integrity` (lines 24905–24906);
- the integrity rule that treats any record beyond `SI-1`'s twenty-two transcriptions as an
  unauthorized addition;
- the census-artifact equality, which saw 23 measured rows against the recorded 22 and, correctly,
  reported the recorded `census.json` as stale.

The file was removed. Nothing was committed. `main` did not move.

## Why this is an adjudication and not a repair

Three frozen contracts interact, and none of them is wrong on its own terms:

- `SI2-1` requires the record: exactly one, `SI1`, added first and then fixed.
- `R7-SI1` as frozen at `SI-1`'s landing refuses any twenty-third record, because at `SI-1`'s
  landing there were twenty-two and an unauthorized addition was exactly what its integrity rule
  existed to catch.
- `SI2-6`(a) says a changed verdict on any pre-existing tag is a **result requiring adjudication**
  that stops the cutover — and `R7-SI1` turning from `PASS` to `FAIL` is such a verdict.

So the first stage of `SI-2`, executed exactly as frozen, stops itself at `SI2-6`(a). The
preregistration named no path through this because it did not foresee it: precondition 4 checked
`R7-SI1` passing **at the base**, with twenty-two records, and did not ask what `R7-SI1` would say
with the twenty-third present.

The owner adjudicated **path D** — amend the control plane before executing, rather than adjudicate
inside the execution record, relax a prior round's guard without a record, or regenerate `SI-1`'s
artifact — and fixed the amendment's scope as the six points that follow. Paths explicitly
**rejected**: path B in any form, regeneration or repinning of `SI-1`'s `census.json`, and any guard
relaxation not recorded here in advance.

## The six points of the authorization

1. **Scope, not removal.** `R7-SI1`'s twenty-two-record, eighteen-`sealed`, four-`base-only`
   cardinality contracts, its 18/4 record-axis counts, and its integrity contract are **scoped to
   the twenty-two records `SI-1` transcribed**. They keep their values; they stop being evaluated
   over the whole manifest.
2. **`SI-1`'s census is untouched.** `SI-1`'s existing twenty-two-row `census.json` stays
   **byte-for-byte unchanged** — not regenerated, not repinned. Its blob
   `7a3e6288c5f532a849a07beb9a8e5757cdf79d04` remains pinned in the frozen preregistration's start
   state, and `R7-SI1`'s artifact check keeps comparing its twenty-two-row measured census against
   that recorded file.
3. **One addition, and where it lives.** `SI1.json` is **the single addition authorized by
   `SI2-1`**. It is outside `SI-1`'s frozen census and inside `SI-2`'s `U4` census, where its
   shadow comparator — the twenty-third comparator — is already frozen under `SI2-4`.
4. **`R7-SI1` is not otherwise weakened.** All twenty-two original records, their contents, the
   four divergences, the census-artifact equality against the pinned blob, and the resulting `PASS`
   verdict remain frozen. No other clause of `R7-SI1` changes.
5. **A new certified base, and only that base.** After this amendment lands, its `main` merge
   commit is certified through the normal exact-head gates — the merge itself and its `main` push
   run — and **`SI-2` resumes only from that newly certified base**, not from `da9d69d6`.
6. **The allowance is one verdict wide.** On the first post-amendment dry run, `R7-SI1` must be
   `PASS` on the scoped twenty-two-record set with `SI1.json` present, and `SI-2`'s `U4` comparator
   must account for the twenty-third row. **Any other changed pre-existing verdict is still
   `MAP-CHANGED` and stops execution**, this amendment notwithstanding.

The scoping edit is permitted to a non-sealing round by §A.37 — it modifies a contract inside an
existing guard and touches no seal constant — and it is permitted to *this* round only because this
amendment says so in advance of execution.

## Superseded frozen clauses

The following clauses of the frozen preregistration are superseded **for `SI-2` execution only**.
Everything not named here stands as frozen.

1. **`SI2-1` — the authorized manifest addition, first and then fixed.** The clause is *extended*,
   not replaced: its record, its ordering and its outcomes are unchanged, and stage 1 **also carries
   the one authorized edit to a prior round's guard**, per points 1–4 above. `R7-SI1` continues to
   validate exactly the manifest `SI-1` created and reports `SI1.json` as *the addition `SI2-1`
   authorizes* rather than as unauthorized. `MANIFEST-DEVIATED` additionally covers a scoping that
   reaches beyond the contracts named in point 1.
2. **`SI2-6`(a) — the verdict map is preserved.** The clause is *extended*, not replaced: **the
   first post-amendment dry run is part of this target**. With `SI1.json` present and `R7-SI1`
   scoped as `SI2-1` now authorizes, `R7-SI1` must be `PASS` on its twenty-two-record set and
   `SI-2`'s comparator must account for the twenty-third row. That one verdict — `R7-SI1` at the
   head, with the record present, against `R7-SI1` at the base, without it — is the amendment's
   whole allowance, and **any other changed pre-existing verdict is `MAP-CHANGED` and stops
   execution**. `SI2-6`(b) is untouched.
3. **The mandated execution base.** The frozen sentence "The mandated execution base is the merge
   commit of this pull request" is superseded **for execution-base purposes only**: the mandated
   execution base is **the certified merge commit of this amendment on `main`**. `da9d69d6` remains
   the certified preregistration merge and the base at which every pin and precondition was
   re-verified; it is recorded as the pre-amendment base **from which nothing resumes**.
4. **The first act of execution.** The frozen sentence "its first act is to verify this
   preregistration's blob at that base" is extended: the first act verifies **both** the frozen
   preregistration blob `bfcd43831d887c006eab64c9a4b8b5f35ff41c9a` **and** this amendment's frozen
   blob, at the new mandated base.
5. **The guard `R7-SI2`.** The clause "this preregistration pinned **by blob** with a one-byte
   drift control" is extended: `R7-SI2` pins and enforces **both** blobs — the frozen
   preregistration and this amendment — each with its own one-byte drift control. Its content
   contracts additionally hold the result note to **the `R7-SI1` scoping recorded as this
   amendment's single allowance and bounded to the contracts named in point 1**.

## Negative suite: one case added

`SI-1`'s twenty cases and the frozen eleven remain in force. Added, numbered in continuation:

12. A **twenty-fourth** record present beyond `SI1.json` — **fails both** the scoped `R7-SI1`
    integrity contract and `U5`, as an unauthorized addition. The scoping admits the one record
    `SI2-1` authorizes and nothing else; that is what "not otherwise weakened" means mechanically,
    and this case is the mutation control that proves the scoping did not become a blanket
    exemption.

## Preconditions: two added

The frozen eight remain in force and are re-checked at the new mandated base. Added, numbered in
continuation:

9. `R7-SI1`'s cardinality and integrity contracts are **unscoped** at the mandated base — they
   still read `== 22`, `== 18`, `== 4` over the whole manifest — so that the scoping is this round's
   own recorded edit and not something already present. Verified at `da9d69d6` (guard lines
   24873–24875 and 24905–24906); `SI2-0` re-verifies it at the new base.
10. The mandated base is the certified merge commit of this amendment and not `da9d69d6`, and its
    second parent is this amendment's reviewed execution head. `da9d69d6` is recorded as the
    certified pre-amendment base from which nothing resumes.

## What this amendment does not touch

- No pin in the frozen start-state table changes. Every pin and every one of the eight frozen
  preconditions was re-verified at `da9d69d6` and is unchanged from `B0`.
- The derivation rule, the four adjudicated divergences, the objects `U1`–`U5`, the stage order,
  targets `SI2-0`, `SI2-2` to `SI2-5`, `SI2-6`(b), `SI2-7` and `SI2-8`, the predictions, the
  non-licences, the hazards, the legacy inventory, and the retirement round are untouched.
- `SI-1`'s result — `#141` at `RESTATED-AND-FAILS` — is not rewritten.
- No seal constant is altered, added or removed. `SI-2` remains NON-SEALING.
- Act 21 remains closed.

## Execution discipline after this amendment

This amendment is frozen by exact commit SHA and blob SHA at its own review, and merged to `main`
with a merge commit on explicit owner direction naming the exact head. After that merge and its
`main` push run are certified, `SI-2` execution branches from **that** merge commit and from no other,
and its first act is the two-blob verification in superseded clause 4. Its first dry run is the
one-verdict allowance in superseded clause 2: `R7-SI1` `PASS` on the scoped twenty-two with
`SI1.json` present. If that dry run reports anything other than that one verdict changing,
`SI2-6`(a) is `MAP-CHANGED`, the cutover stops, and this amendment authorizes nothing further.
