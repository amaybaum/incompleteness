# Act 21 preregistration — Amendment 1: the drafting snapshot and the mandated execution base are distinct commits, and the preconditions are read accordingly

This is a **procedural control-plane amendment** to
`verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md`, made
**before any execution object exists**, in the repository's append-only amendment form (§A.36): the
frozen preregistration is not edited, and this file is the whole of the change. **It changes no
rung, no candidate, no quotient, no target, no headline rule, no prediction and no settlement.** It
corrects one thing: the frozen preregistration uses the name `B` both for the commit it was written
against and for the execution base its chronology control defines, and after the freeze merged those
are different commits, so two of its eleven mechanical preconditions cannot be satisfied as written
at the commit the chronology control names.

Frozen preregistration provenance:

- freeze pull request: #678, reviewed head `d9b97f4bf07cdc2d62cc5dc6dc422dbb30955868` (the first
  draft `7fb200cd…` plus one revision commit on owner review, appended and not rewritten);
  authoritative frozen preregistration blob: `316d635a31f91faebeeebef7688b30002d24b4ca`;
- preregistration merge commit on `main`: `aeb0b91d20b4e307c293c06afda9db64fe2a3b09`, first parent
  `63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`, second parent `d9b97f4b…`, certified by main-push run
  35418734887 with all three jobs green;
- the snapshot the freeze was written against and measured at: `63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`,
  `SI-3`'s landing, certified by main-push run 35412319426.

**The frozen preregistration remains byte-for-byte unchanged**, historical and authoritative for
everything this amendment does not name. **Nothing of act 21 was executed between the
preregistration merge and this amendment**: no execution branch was created, no prospective
declaration or declared baseline was set, no guard clause was written, no Lean module exists, no
manifest record exists, and no dry run of the round was taken. The tree at `aeb0b91d` differs from
the tree at `63d8ca08` by exactly the one added preregistration file.

## The inconsistency, stated exactly

The frozen preregistration's chronology control, item 2, defines the execution base correctly:

> **The execution pull request's base must be exactly the merge commit of this control-plane pull
> request**, `B`.

That merge commit is `aeb0b91d…`. But the same file uses `B` for the commit it was drafted against:
its freedom-check section opens "At **`63d8ca08…`**, the certified `main` this freeze is written
against"; its locating controls open "The base is `main` at **`63d8ca08…`**"; its start-state table is
"pinned by blob at this freeze's base, `main` at `63d8ca08…`"; and its precondition table, which an
auditor checks "at the execution's base commit `B`", carries two rows that are true only at
`63d8ca08…`:

- **precondition 10** says "`B` is `63d8ca08…`; its first parent is `b0ee87ba…` and its second parent
  is `bae13c9e…`", which names the drafting snapshot as the execution base in terms;
- **precondition 6** requires "`git grep -- 'OLT' B` returns nothing", which held at `63d8ca08…`
  and is necessarily false at `aeb0b91d…` and at every later commit, because the merged
  preregistration itself contains the stem forty-six times.

So the eleven preconditions cannot all pass at the commit item 2 names. **The frozen set is
inconsistent, not merely ambiguous**, and an execution that branched from `aeb0b91d…` would have to
record two discrepancies at its first act against a freeze that was simply written with one name for
two commits. That is what the append-only amendment mechanism exists for, and it is applied here
before any execution object exists.

## The correction, in five points

### 1. Two names for two commits

- **`D`, the drafting snapshot** — `63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed`. Every measurement the
  frozen preregistration reports as made "at this base", "at `B`" in its freedom-check section, its
  locating controls, its start-state table, its provenance section and its supersession-table
  simulation, was made at `D`, and is read as a statement about `D`. `D` is the first parent of the
  preregistration's landing merge `aeb0b91d…`. **`D` is never the execution base.**
- **`B`, the mandated execution base** — the certified merge commit of **this amendment** on
  `main`, per point 5. The chronology control's items 2, 4 and 5, the prospective declaration
  `_MANIFEST_PROSPECTIVE = {'OLT': B}`, the declared baseline `_MANIFEST_BASELINE = {'base': B,
  'authorized': ('OLT',)}`, the anti-contamination invariant's "the base is fixed the moment this
  file merges", the execution-discipline bullet "the execution branches from the merge commit of this
  control-plane pull request", and the precondition table's "checked at `B`" all read `B` in this
  sense.

The blob pins are unaffected by the distinction: every blob the start-state table names at `D` is
the same blob at `aeb0b91d…` (the diff between the two trees is the one added preregistration file),
and the execution's first act, point 5, checks each of them at `B` by blob exactly as the freeze
requires.

### 2. What is preserved

- `aeb0b91d20b4e307c293c06afda9db64fe2a3b09` remains the certified merge of the original freeze and
  stays on `main`'s first-parent spine.
- Preregistration blob `316d635a31f91faebeeebef7688b30002d24b4ca` remains unchanged and remains the
  blob the `R7-OLT` clause pins by content at its path, with the one-byte drift control the freeze
  specifies.
- The freeze's supersession-table simulation, its freedom checks, its locating-control coordinates
  and its start-state table stand as measurements at `D`, exactly as reported.

### 3. Precondition 10, corrected

Precondition 10 is superseded by this row:

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 10 | The drafting snapshot's provenance, and the freeze's landing | `D` = `63d8ca08cbea2e05e4f9fdc5a9b36006b9f104ed` has first parent `b0ee87bae34c6f8dcd3a4a75d958bb4e8a1cbca5` and second parent `bae13c9eec30f63e4b0e6644811e6d124ee08a30`, `SI-3`'s `P`; the freeze's landing merge `aeb0b91d20b4e307c293c06afda9db64fe2a3b09` has first parent `D` and second parent `d9b97f4bf07cdc2d62cc5dc6dc422dbb30955868`; and both lie on `B`'s first-parent spine, `git log --first-parent --format=%H B` listing each. Read as provenance facts about `D` and about the freeze's landing — never as a statement that `D` is `B`, and never as a requirement that live `main` remain anywhere |

### 4. Precondition 6, corrected

The name-freedom check has two halves that the frozen row ran together. The **freedom** half —
that the tag, the stem and the bare form collided with nothing when they were chosen — was measured
at `D` and holds there: `R7-OLT`, `_OLT`, bare `OLT` and `OrbitLawRigidityTwisted` each returned
nothing at `D`, as the freeze records. **That half is a fact about `D` and is not re-measured at
`B`**, where the frozen control-plane documents necessarily mention the names they reserve. The
**absence-of-execution-objects** half is what the execution base must satisfy, and it is stated
here so that the names the control plane itself carries do not fail it. Precondition 6 is superseded
by this row:

| # | precondition | mechanical check at `B` |
| --- | --- | --- |
| 6 | The names were free when chosen, and no act 21 execution object exists at `B` | Freedom at `D`: `git grep -- 'R7-OLT' D`, `git grep -- '_OLT' D`, `git grep -- 'OLT' D` and `git grep -- 'OrbitLawRigidityTwisted' D` each return nothing. Absence at `B`: `git show B:verification/lean/edge_rigidity_probe.py` contains no occurrence of `R7-OLT` and no occurrence of `_OLT`, and no name matching `_OLT_(BASE\|SEALED_HEAD\|MERGE)`; `git ls-tree B --name-only verification/seals/` contains no `OLT.json`; `git ls-tree -r B --name-only` contains no `verification/lean-mathlib/OIBridge/OrbitLawRigidityTwisted.lean`; and `git grep -l -- 'OLT' B` returns exactly the two frozen control-plane documents, `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/preregistration.md` and `verification/programmes/oi-qm/track-b/act-21-orbit-law-rigidity-twisted/amendments/amendment-1.md`, and no other path |

Measured at `aeb0b91d…`, before this amendment merges: `git grep -l -- 'OLT'` returns the
preregistration alone, with forty-six occurrences; the guard file contains no `R7-OLT` and no
`_OLT`; no `OLT.json` and no `OrbitLawRigidityTwisted.lean` exist; the round directory holds
`preregistration.md` alone; the seals tree is `1abe1c988b1cb0a5fd119bbae8bd7108933334a4`; and the
guard at `aeb0b91d…` still carries `_MANIFEST_PROSPECTIVE = {}` and `_MANIFEST_BASELINE =
{'base': 'b0ee87ba…', 'authorized': ('SI2', 'SI3')}`. At `B` the same holds with this amendment's
path added to the round directory and to the `OLT` file list, and with nothing else changed by this
pull request.

**Precondition 8 is read with the same addition**: `git ls-tree -r B --name-only` contains no path
under the round directory other than `preregistration.md` and `amendments/amendment-1.md`.
**Precondition 1 is read of the freeze and of this amendment together**: `B` has two parents, the
preregistration at its path has blob `316d635a…`, and this amendment at its path has the blob the
`R7-OLT` clause pins for it, per point 5. **Precondition 5's certifying run** is the main-push run
that certifies `B`, named in the result note, with the guard file at `B` the same blob
`8b999f7a86d95dbc6a2871c0fe4be3f0bbcd64c9` as at `D`. Preconditions 2, 3, 4, 7, 9 and 11 are
unchanged and hold at `aeb0b91d…` by the same blobs as at `D`.

### 5. The mandated execution base moves to this amendment's certified merge

Following the repository's amendment precedent — `SI-2`'s Amendment 2, point 7, under which the
certified merge of the latest amendment became the mandated base and the execution branched from
it rather than from the original preregistration merge — **the certified merge commit of this
amendment on `main` becomes act 21's mandated execution base `B`**, superseding `aeb0b91d…` for that
role. Concretely:

- the execution branches from exactly `B` and from nothing else, **after `B`'s own main-push run is
  fully green**, and not before;
- **its first act is to verify both frozen blobs at `B`** — the preregistration at
  `316d635a31f91faebeeebef7688b30002d24b4ca` and this amendment at the blob recorded in the
  amendment pull request's review — before any target is executed, and to record both
  verifications in the result note; if either differs, the execution records the discrepancy and
  does not repair the freeze;
- the `R7-OLT` clause pins **both** blobs by content at their paths, each with its own one-byte
  drift control, as `SI-3`'s guard pinned its preregistration and its Amendment 1;
- the prospective declaration and the declared baseline are set to `B` in this sense, so the seals
  tree the declared baseline reads from git is the tree at `B`, which is
  `1abe1c988b1cb0a5fd119bbae8bd7108933334a4` unless a sibling landing changes it before `B`, in
  which case the execution records the tree it found and the anti-contamination invariant governs;
- the chronology control's item 1 reads "this preregistration blob **and this amendment** are merged
  into `main` before any execution-specific act 21 object enters the repository tree".

## What this amendment does not do

It does not edit the frozen preregistration. It does not change `L4n`, the ladder, the candidates,
the quotient list, `SIOP`, the witness rule, the headlines, the status rule, the predictions, the
attestation set, the anti-expansion rule, the definition budget, the evidence level, the
supersession table or any settlement. It does not set the prospective declaration or the declared
baseline, does not write a guard clause, a Lean module or a manifest record, and does not open the
execution. It adds no name and reserves none: the tag, the stem, the module and the directory are
those the freeze reserved.

## Owner settlement

Recorded as a call made: the drafting snapshot and the mandated execution base are distinct commits,
named `D` and `B`; preconditions 6 and 10 are read as corrected above, precondition 8 with the
amendment path added, and precondition 1 of both frozen blobs; and the certified merge of this
amendment is the mandated execution base from which act 21's execution branches. The freeze's
mathematics is untouched.
