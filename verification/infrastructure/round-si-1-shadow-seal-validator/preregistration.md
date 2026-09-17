# Seal infrastructure round 1 — the shadow validator and the equivalence census: CONTROL PLANE

Preregistration only. No execution object exists when this merges, and this merge commit becomes
the round's mandated execution base under `AGENTS.md` `§A.37`.

This is the first of **two** rounds. `SI-1` builds a generic seal validator and a per-round seal
manifest **alongside** the machinery now in `verification/lean/edge_rigidity_probe.py`, runs the two
side by side, and delivers a census of their agreement. `SI-2`, a separate round begun only from a
certified `SI-1`, moves authority to the manifest and removes the duplicated per-round state. The
boundary is drawn at authority and nowhere else.

## The round's shape, declared first, in `§A.37`'s terms

**`SI-1` is NON-SEALING.** It lands `E` → `L`. There is no pin commit `P`, no
`_SI1_SEALED_HEAD` and no `_SI1_MERGE`.

The guard is the fresh tag **`R7-SI1`**, stem **`_SI1_`**, and it carries:

- content contracts over this round's own artifacts, and
- a `_SI1_BASE` with the strengthened ancestry check of act 10's form — the question asked of the
  real `pull_request.head.sha`, never of the synthetic merge commit, every commit of
  `git rev-list H ^B` required to descend from the base, recovery included, **fail-closed**.

It carries **no seal triple of its own**, which is the `R7-ABR` / `R7-CLG` / `R7-RBR` / `R7-TSG`
shape and not the `R7-HBS` shape. The ancestry check is wanted because the census this round
delivers must be produced *after* the freeze that says what would count as agreement; the seal
triple is not wanted because the round seals nothing.

Both `R7-SI1` and `_SI1_` are verified free at the base: the guard file at the base contains **zero**
occurrences of either string.

### Why NON-SEALING, stated narrowly, because the narrowness is the point

`SI-1` is non-sealing **because it does not alter which mechanism gates or interprets repository
history.** The old machinery remains authoritative for every check that gates. The new validator
runs, reports, and is compared; it decides nothing.

This is stated narrowly and deliberately. It is **not** a claim that shadow code is inert, nor a
licence to read "non-sealing" as "ordinary tooling". The instant the new validator becomes
authoritative, that is `SI-2`. No later reading may hold that the certification semantics were
already changed by `SI-1` merely because the new code was present in the tree: presence is not
authority, and this freeze fixes the distinction in advance so that it cannot be relitigated from
the artifact afterwards.

### What this round would own, and what it would not

It would own: the manifest record schema; the generic validator and its three-state model; the
transcription of all twenty-two existing records; the negative-test suite; and the agreement census.

It would not own: which validator gates anything; the removal of any existing constant, clause or
comparison; any change to a historical `B`, `E`, `L` or `P`; any change to a preregistration, result
note or scientific claim; and Act 21, which stays closed through both rounds.

## What this round is not, stated before anything else

1. **It is not the cutover.** Authority does not move in `SI-1`. A result note claiming the manifest
   is authoritative, or that the old machinery has been replaced, is outside this round whatever the
   census shows.
2. **It removes nothing.** Not one `_XYZ_BASE`, `_XYZ_SEALED_HEAD` or `_XYZ_MERGE` constant is
   deleted, and not one hand-written prior-seal comparison is deleted or weakened. The diff against
   the base **adds**; the only edits to existing lines permitted anywhere in the guard file are those
   required to *call* the shadow validator and print its report, and those edits may not change the
   verdict of any existing check.
3. **It is not a retrofit.** Every historical commit stays exactly where it is. The migration changes
   how the seal record is *represented and checked*, never what happened.
4. **It decides no mathematics.** No target of this round bears on any programme's content. No
   manuscript file is read for content or written.
5. **It does not amend any seal.** Transcription is exact. A transcription that "corrects" a value is
   a failure of this round, not a repair.
6. **It is not Act 21's control plane** and states nothing about Act 21's targets.

## The directory is fixed here and does not move afterwards

This round and `SI-2` live at

```
verification/infrastructure/round-si-1-shadow-seal-validator/
verification/infrastructure/round-si-2-authority-cutover/        (SI-2, not created here)
```

and the manifest at

```
verification/seals/<STEM>.json                                   (one record per round)
```

`verification/infrastructure/` is created by this round. The reason it is not a fifth entry under
`verification/programmes/` is that `programmes/` holds research programmes — `hydrodynamics`,
`oi-qm`, `physical-realization`, `substratum` — each owning scientific targets, and this round owns
none. It is also not an entry under `verification/audits/`, which holds audits of the corpus rather
than changes to the verification instrument.

**This had to be a pre-merge decision.** `R7-SI1` pins this preregistration by path **and** by blob,
so a later rename would break the pin rather than tidy it. The path above is the settled one and the
execution reads the freeze from its own base at exactly that path.

## Start state, pinned by blob

The execution's first act, before any target is executed, is to verify each of these at its own
mandated base `B`. A mismatch stops the round.

| path | blob at `B` |
|---|---|
| `verification/infrastructure/round-si-1-shadow-seal-validator/preregistration.md` | fixed by this merge; the execution reads it and checks its own copy against `git show B:` |
| `verification/lean/edge_rigidity_probe.py` | `033081ea01608a1a31cf78293e84168e675b359a` |
| `AGENTS.md` | `3e3f00454db033b4fc519fd1123cd3f9b7f7cf24` |
| `.github/workflows/verify.yml` | `5e16a4b24636f997ce4076eb56159923dfd62a31` |
| `verification/ROADMAP.md` | `4eb3a6502e65b54b77d4f3488fa8e105cdf0e8da` |
| `verification/README.md` | `9983b0781e565e9f9a01b4b3152c30842307a406` |

### Files this round reads AND writes

- `verification/lean/edge_rigidity_probe.py` — **adds** the `R7-SI1` clause and the shadow-validator
  call; alters no existing check's verdict; removes nothing.
- `verification/seals/*.json` — **created**, twenty-two records.
- `verification/infrastructure/round-si-1-shadow-seal-validator/result.md` — **created**.
- `verification/infrastructure/round-si-1-shadow-seal-validator/census.json` — **created**, the
  machine-readable agreement census.
- `verification/README.md`, `verification/ROADMAP.md` — ledger and queue rows only.

### Files this round reads and MUST NOT write

Every `preregistration.md` and `result.md` under `verification/programmes/`; every file under
`papers/` and `book/`; every `.lean` file. The guard checks the last two mechanically: the
execution's diff against `B` touches no path matching `papers/`, `book/` or `*.lean`.

## The census, frozen as data

These are the twenty-two records as the guard file carries them at `B`. They are frozen here so that
"transcribed exactly" is a checkable claim against this document and not against the execution's own
reading of the source.

| stem | kind | `base` | `sealed_head` | `merge` |
|---|---|---|---|---|
| `A12P` | SEALED | `999f1b5b3c9d6960233a12698d83c1a56a16fe10` | `2792a7836d70e10b7f085f4e35fb8a92d77eb133` | `2706a3aa7b87e481df17e3ceab88cd3244ce780d` |
| `A6D` | SEALED | `8792801beeeccbf0673db137cae83e6663d21fba` | `d0b8c6e83c32a01a586f947c0dfd9618a8b42a91` | `4fb0a6052d33193d442dd2a2cb72f64937177291` |
| `A6I` | SEALED | `3e5d6a8f75166581213b6c5b7c0dbca1671b030e` | `93405f3ff7eb4818a2895b5f5e2861094d9fe757` | `ae0baf8ad5b8ef0daa473f2b772d4217a210f520` |
| `A6P` | SEALED | `07ab3657c2c78b48e4c11e0c3ceb30c82ac0b484` | `58100aea15eea8f5808b351d64163f55c9fed1bf` | `98d0c894c96b81e9138b97d92b4635356751e194` |
| `ABR` | BASE-ONLY | `93c2ca63c6cd7a61388d577b8baf22c3c1fdb41f` | — | — |
| `CLG` | BASE-ONLY | `6cff07cc0655124f1f29e04b156cc05a3d717a48` | — | — |
| `CTI` | SEALED | `d019718696fd12e4719b5ed5b7d8dfab45544a8c` | `9ea94f9ca52f12e8cd4215be7e039d1f86d81fc7` | `292848b3c908d33ac432a5360effe0c259e3ce16` |
| `HYA` | SEALED | `ae81459372887cfbe27b427b30bbdad1b564f2b7` | `6a8675efca5e5ceeab0195036af1a658b49ace80` | `d2314f5edc33fbeb4f75642ec87f9d302ee734f4` |
| `HYB` | SEALED | `8de0478ef31fe4cabcf89fc5787f80f38376a957` | `54b33c4304bdbda52a09dfe0a06f3e7ff350d832` | `2ac870f0b7f04df35f32e80f7717d67667b5df83` |
| `HYE` | SEALED | `0975bbab380b26cd2bb06ec65ed68f8bcc23937f` | `fe8060bd934c874356f7ba4778e414108d6fc36a` | `d98d690bdd2634299862282ac5ed3da4c015e7e1` |
| `PC4` | SEALED | `ebc3951dc581d558373f720a90f1ba7deb2a8ed8` | `6c1acdd28f03f614f71a7ce15c6efc141906e080` | `e82755cafdbc0314890ad3809bc48e72e5995311` |
| `PC4S` | SEALED | `0ef074104cee3957d3aee9422888859b88fc0ebf` | `81b78484a0abf39ac2a23a6a8e4afcd003b79e23` | `8f4934136bae62a57a0744dbf93d3ee485404198` |
| `PQT` | SEALED | `bc76a88dbe300a35715d5ce8196002f31aa62493` | `5008a47bf7e67edc502120f9269c4a4661ef7342` | `c50dd22457bfd4812761cb56e7ca1a559af33c5e` |
| `RBR` | BASE-ONLY | `79872cbbb0e26188f619b8c6a99b379bb46b7b0c` | — | — |
| `RNC` | SEALED | `d05399020d05d4a7b6f662d2e069062452e7d6b4` | `31db7c1082b012c00c43f3fda35ce44c5653e123` | `eb70bbb9b2b3311095945ec3ce2418962f3b741a` |
| `RNT` | SEALED | `84f27b50198ee31c224e31284905ff6c284ea9db` | `0f8b4e06a1cc31ab0c01f2edb5011f1efe545e1b` | `6a6d62e97518600bf2de51cf1d39146d1adbdff9` |
| `SGT` | SEALED | `c46e1606d4cafe2720afd69dc06c667eb0f1acff` | `57103e9ddf430c538094fed48358c4d1b050ce4d` | `11a8a59d22793a10182f853fe3c05edf5415d724` |
| `TCF` | SEALED | `e4501bfff4e80533a5440c67d032f1ad401bdbe1` | `c622461495c6b2db4e09c8084f404bd5ca2c5192` | `9e0cc3834538b7bdcb742fcaa046194cfa9526fb` |
| `TRJ` | SEALED | `02cfc9be141a44aaebf847d8e7d9fdd0d0a18f08` | `94d41561114b2aee5939dcfa976ce98b8f141093` | `e8b12a433ebc0e5047504d2c95664a85ca65d1e8` |
| `TSG` | BASE-ONLY | `b821d69ae86f7d76020383735b3161e77c064ccc` | — | — |
| `WTS` | SEALED | `baadea2638019b335d96c892590491a6fb420936` | `c31fe45d28d6aa37782902f67aba404ef721a59e` | `6a6f206f830f5b44e1b19a6912b823d545207126` |
| `XTS` | SEALED | `d7a9931befeb942db8ebc7b07014f9020c6663d0` | `730a518c173460d7bed525da10a95ee6bd32c7de` | `0b893d75cca344faeb9a9e434b5b8537f8b45dac` |

Eighteen `SEALED`, four `BASE-ONLY`. **The schema must admit `BASE-ONLY` as a first-class record
kind, not as a triple with two nulls**: `ABR`, `CLG`, `RBR` and `TSG` are non-sealing rounds that
never had a seal, and a schema that represents them as incomplete seals would misdescribe four
rounds' history in the act of transcribing it. The owner settles this below, and the kind is named
`sealed` rather than `archived` on purpose — see the next paragraph.

### `kind` is not a state, and the two must never be spelled the same

`kind` describes **history**: whether the round ever had a seal. `SEALED` and `BASE-ONLY` are the two
kinds, and a round's kind does not change once its history is what it is.

`EXECUTION`, `LANDED-PENDING-PIN` and `ARCHIVED` are **lifecycle states**, computed per event from
the record plus the repository. They are not stored.

A `sealed` record is normally in state `ARCHIVED`, but the two words answer different questions, and
using one spelling for both is how a reader comes to believe that a record carries its own verdict.
The freeze therefore uses `sealed` for the kind and `ARCHIVED` for the state throughout, and the
guard checks that no stored record carries any state name as a value.

### The rebinding hazard, which is part of this round's motivation and is regression-tested

`_RNT_SEALED_HEAD` and `_RNT_MERGE` are each assigned **twice** at module level in the guard file at
`B`: once as the pin, and once at lines 23602–23603 as the clause-9 self-test rebinding to
`('f' * 40, 'e' * 40)`. No other stem has a repeated assignment.

A transcription that reads the source for the *last* assignment of each name therefore returns the
probe values and not the seal, and the resulting manifest would be wrong for exactly one round while
looking well-formed. The freeze fixes two consequences:

- the transcription is checked against **this document's table**, not against the execution's own
  parse of the source; and
- the negative-test suite carries a case in which a stem's constant is assigned twice with different
  values, and the test requires the transcriber either to take the first assignment or to **refuse**.
  Silently taking the last is a failure.

This is also the standing argument for target `SI1-1`: seal data should have **one canonical
representation**, and executable tests should *consume* it rather than redefine it at module scope.

## The derivation rule, FROZEN, with its scope

For a `sealed` record the validator derives `L` and compares it to the pinned value.

> **The derived `L` is the unique merge commit in the resolved target's reachable history whose
> non-first parent is exactly `E`.**

**Reachable history, not the first-parent spine.** This is frozen with its evidence, because the
narrower rule is wrong for this repository and would have failed twelve of eighteen rounds:

| derivation scope | agrees with the pin, at `B` |
|---|---|
| main's **first-parent** history | **6 of 18** — and **zero** candidates for the other twelve |
| **all merges** in the target's reachable history | **18 of 18**, exactly one candidate each |

The mechanism is two historical landing shapes, and **both are preserved in the frozen test
corpus**:

- **Shape A, `L` on the first-parent spine — six rounds:** `A12P`, `A6D`, `HYA`, `RNT`, `SGT`, `XTS`.
  `L` was merged into main directly and `P`, where the round had one, arrived as a later separate
  pull request. Act 20 is the worked example: `L` `6a6d62e9` landed by #665, `P` `e602ebfd` by #666.
- **Shape B, `L` one step off the spine — twelve rounds:** `A6I`, `A6P`, `CTI`, `HYB`, `HYE`, `PC4`,
  `PC4S`, `PQT`, `RNC`, `TCF`, `TRJ`, `WTS`. `L` and `P` landed **together** through one pull
  request: `P` was committed on top of `L` on a branch, and that branch entered main as the pull
  request merge's second parent. `CTI` is the worked example: `L` `292848b3c908` is the **first
  parent** of `P` `762c06f6`, which entered main inside #612.

Neither shape is a defect and neither is corrected. A validator that handles only Shape A is the
defect.

Hard failures, each a distinct condition and each named separately in the report:

1. **zero candidates** — no merge in reachable history has `E` as a non-first parent;
2. **multiple candidates** — more than one does;
3. **disagreement** — exactly one does and it is not the pinned value.

Pinning `L` as data *and* deriving it is not redundancy. Derivation alone is self-healing in the
wrong direction: rewrite the landing merge and a deriving validator finds the new one and reports
success, which is the event the seal exists to detect. The pin is the tamper-evidence; the
derivation is the independent check; equality is the claim.

## The three states, FROZEN

**The three states are the lifecycle of a seal-producing round, not the lifecycle of every manifest
record.** A `base-only` record does not enter the state machine at all.

This is stated first because the obvious wording gets it wrong, and did. Defining `EXECUTION` as
"no record, or a record with no `sealed_head`" captures all four `base-only` records and classifies
`ABR`, `CLG`, `RBR` and `TSG` — completed historical non-sealing rounds — as permanently *executing*,
after which the validator would go on applying execution ancestry semantics to them on every future
repository state. That is precisely the category mistake the `base-only` kind exists to eliminate: a
round for which no seal exists is not a round whose seal has not arrived yet.

So the classification is:

| record | lifecycle |
|---|---|
| `kind = "base-only"` — a historical non-sealing record | **not applicable.** Its schema, its pinned `base` and its record integrity are validated, along with whatever generic invariants apply, and it is **not** classified `EXECUTION`, `LANDED-PENDING-PIN` or `ARCHIVED` |
| a prospective round with **no** manifest record | `EXECUTION` |
| a sealing round whose exact `L` is the resolved target, with no sealed record yet | `LANDED-PENDING-PIN` |
| `kind = "sealed"` | `ARCHIVED`, once the complete `base`/`E`/`L` record exists and all archive checks pass |

`BASE-ONLY` is **not** a fourth lifecycle state, and none is invented. The kind/state distinction
holds: the validator reports `kind = base-only` with `lifecycle = not-applicable`, and stores no
lifecycle value for any record.

**`EXECUTION`.** No manifest record for this round at all. The prospective execution is validated:
the strengthened ancestry check against `base`, asked of the resolved target, fail-closed. A record
that exists but lacks `sealed_head` is **not** this state — under the schema the only such record is
a `base-only` one, and it is out of the machine.

**`LANDED-PENDING-PIN`.** Permitted **only when the resolved target is itself `L`** — a merge whose
first parent is a certified main, whose non-first parent is an `E` that passes the strengthened
ancestry check against `base`, and for which no manifest record yet exists. That one commit
validates.

> **A descendant of an unpinned `L` FAILS, with the reason `seal pending`.**

This is the condition that removes the deliberately red window without weakening fail-closed: `L`'s
own push run is green, the pin moves the record to `ARCHIVED`, and anything that lands in between is
red. A forgotten pin blocks the next change instead of drifting indefinitely.

**`ARCHIVED`.** A manifest record carrying `base`, `sealed_head` and `merge`. All of: pinned `L`
equals derived `L`; `L`'s non-first parent is exactly `E`; `E` passes the strengthened ancestry
check against `base`; and `L` and `E` are both reachable from the resolved target — the existing
archive conditions, unchanged in content.

### Event resolution stays explicit

- On `pull_request`, the resolved target is the **real `pull_request.head.sha`** wherever the
  question is about the execution or the landing, and the base-branch tip is
  `refs/remotes/origin/<base ref>` and nothing else, `pull_request.base.sha` being read and printed
  as a non-gating diagnostic only.
- On `push`, the resolved target is `HEAD`.
- **The synthetic merge `HEAD` of a pull-request build must never be the object of an ancestry
  question**, because it has both the base and the head as parents and makes the question vacuous.
  The negative-test suite carries a case in which a reading that consulted the synthetic merge would
  pass a case that must fail.

## Manifest integrity, FROZEN

Against the record set as it stood at the execution's own base `B`, the validator distinguishes
**three** conditions, reported separately and never merged into one:

1. **mutated** — a record present at `B` and now present with different contents;
2. **removed** — a record present at `B` and now absent;
3. **added** — a record absent at `B` and now present.

With one file per round, a record can be deleted as easily as edited, and a rule checking only
contents would let a deletion pass invisibly. An amendment of an existing record must be
**prospectively authorized by a control plane naming that record**; `SI-1` authorizes none, so for
`SI-1` the rule is: **no mutations, no removals, and the only additions are the twenty-two
transcriptions this round makes.**

### Why one file per round

A single shared manifest file is a merge-conflict hotspot the moment two sibling rounds seal
concurrently — which this repository does routinely; five rounds landed in one afternoon on
2026-09-17. One record per round means each round's pin touches only its own file. The validator
loads `verification/seals/` as **one logical manifest**; the storage is per-record and the semantics
are whole-manifest.

## The objects, FROZEN

**`O1` — the record schema, a discriminated union on `kind`.** A JSON object with `round` (the stem,
matching the filename), `kind`, and the fields that kind requires:

| `kind` | requires | forbids |
|---|---|---|
| `"base-only"` | `base` | `sealed_head`, `merge` |
| `"sealed"` | `base`, `sealed_head`, `merge` | — |

`forbids` means a hard failure, not a tolerated null: a `base-only` record carrying `sealed_head` or
`merge` — **including as `null`** — is rejected. Unknown keys are a hard failure, not ignored. Every
hash is checked as 40 lowercase hex before it is used, and a malformed or missing hash fails closed
rather than being coerced.

The union is the whole point of the modelling. `ABR`, `CLG`, `RBR` and `TSG` are not seals waiting
for fields; they are rounds for which **no seal exists**, and the schema says so structurally rather
than by convention about nulls. Any other representation requires an **explicit prospective schema
amendment**, and may not reinterpret these four records merely to make the data structure
cosmetically uniform.

**`O2` — the generic validator.** One function taking the manifest, the event environment and the
repository, and returning, per record, a verdict with a reason string, together with **either** a
lifecycle state — for a `sealed` record or a round with no record — **or** `lifecycle =
not-applicable`, for a `base-only` record. It does not return a state for every record, because not
every record has one. It contains **no round-specific branch**: no stem appears in its logic, and
the `SI1` guard checks that mechanically against the validator's own source.

**`O3` — the shadow harness.** Runs `O2` over all twenty-two records in the same process and on the
same repository state as the existing checks, and emits `census.json`. It gates nothing.

**`O4` — the negative-test suite**, on synthetic repositories built in temporary directories, in the
manner of the existing `R7-VIS` and `R7-ARCH` regressions.

## The targets, FROZEN

**`SI1-0` — locating controls.** `R7-SI1` and `_SI1_` are free at `B`; `verification/seals/` and
`verification/infrastructure/` do not exist at `B`; the twenty-two records in this freeze's table
are exactly the seal constants the guard file carries at `B`, with the double-assignment of
`_RNT_SEALED_HEAD` and `_RNT_MERGE` recorded as found. Cheap and certain; a bounded check, reported
per item.

**`SI1-1` — the schema, `O1`.** Twenty-two records written, one per stem, each validating against
the schema; `base-only` represented as its own kind; every value byte-identical to this freeze's
table. Outcome `SCHEMA-BUILT` or `SCHEMA-INCOMPLETE`.

**`SI1-2` — the validator, `O2`.** Built, with the three states, with `base-only` records held OUT
of the state machine and reported `lifecycle = not-applicable`, and with no round-specific branch.
Outcome `VALIDATOR-BUILT` or `VALIDATOR-PARTIAL`, the latter naming which state is unimplemented. A
validator that assigns any of the three states to a `base-only` record is `VALIDATOR-PARTIAL`
whatever else it gets right.

**`SI1-3` — the derivation rule.** Implemented at reachable-history scope; run over all eighteen
`sealed` records; the six Shape-A and twelve Shape-B rounds both covered; and the first-parent-only
scope **retained as a regression** that must report 6 agreements and 12 zero-candidate failures, so
that a future narrowing of the scope is caught. Outcome `DERIVE-EXACT` if all eighteen agree with
their pins with exactly one candidate each, `DERIVE-PARTIAL` otherwise, with every disagreement
named. The four `base-only` records are not derived over: there is no sealed head to derive from, and
attempting a derivation for them is a failure of this target.

**`SI1-4` — the negative-test suite, `O4`.** One case per condition, each required to **fail** and
each required to fail for the *named* reason rather than merely to fail:

| # | case | required verdict |
|---|---|---|
| 1 | malformed hash — not 40 hex | FAIL, malformed |
| 2 | missing required key | FAIL, schema |
| 3 | unknown extra key | FAIL, schema |
| 4 | `base-only` record carrying a `sealed_head`, and separately one carrying `sealed_head: null` | FAIL, schema, both |
| 5 | rewritten `E` — the sealed head no longer exists | FAIL, unreachable |
| 6 | wrong `L` — pinned `L` is a real merge but not `E`'s landing | FAIL, disagreement |
| 7 | two candidate landings for one `E` | FAIL, multiple candidates |
| 8 | zero candidate landings | FAIL, zero candidates |
| 9 | sibling history — a commit reachable from the target that post-dates `base` but does not descend from it, in `EXECUTION` state | FAIL, pre-freeze side history |
| 10 | stale `pull_request.base.sha` disagreeing with the live base-branch tip, base branch carrying the landing | PASS via the branch tip |
| 11 | the same, base branch **rewound** off the landing while `base.sha` still carries it | FAIL, failing closed |
| 12 | unresolved base ref — `refs/remotes/origin/<ref>` absent, a local `refs/heads/<ref>` present and carrying the landing | FAIL, not accepted in its place |
| 13 | a descendant of an unpinned `L` | FAIL, seal pending |
| 14 | `L` itself, unpinned | PASS, `LANDED-PENDING-PIN` |
| 15 | mutation of a record present at the base | FAIL, mutated |
| 16 | removal of a record present at the base | FAIL, removed |
| 17 | unauthorized addition of a record | FAIL, added |
| 18 | a stem whose constant is assigned twice with different values, in the transcription path | FAIL or first-assignment, never last |
| 19 | a reading that consults the synthetic merge `HEAD` instead of the resolved target | the case FAILS, so such a reading would wrongly pass |
| 20 | a `base-only` record on a repository state where an `EXECUTION`-style ancestry check would fail | PASS, `lifecycle = not-applicable`; a validator that classifies it `EXECUTION` FAILS the case |

Outcome `NEGATIVES-COMPLETE` if all twenty behave as the table requires, `NEGATIVES-PARTIAL`
otherwise, naming each case that does not.

Case 20 is the one this freeze was amended to add. It is the direct test of the correction: it fails
any validator that treats an absent seal as a pending one.

**`SI1-5` — the agreement census.** For all twenty-two records, on the repository state at the
execution head and on every synthetic control of `O4`, the old machinery's verdict and `O2`'s verdict
are recorded side by side in `census.json`. Outcome `CENSUS-EXACT` if they agree on every record and
every control, `CENSUS-DIVERGENT` otherwise.

**The twenty-two records are not compared on the same axis, and the census says which axis each is
on.** The **eighteen** `sealed` records exercise LIFECYCLE equivalence: the state and the verdict.
The **four** `base-only` records exercise SCHEMA, PINNED-`base` and RECORD-INTEGRITY equivalence
only, because they have no lifecycle to agree about. A census that reported a lifecycle agreement for
a `base-only` record would be claiming agreement on a question neither implementation should be
answering, so `census.json` carries the axis per record and the frozen sentence names both counts. **A divergence is reported, not repaired**, and it does
not become a licence to change the old machinery in this round.

**`SI1-6` — non-authority, checked mechanically.** The execution's diff against `B` deletes no seal
constant and no prior-seal comparison; every check that existed at `B` returns the same verdict at
the execution head as at `B`, on the same inputs; and no existing check consults `O2`. Outcome
`SHADOW-ONLY` or `AUTHORITY-LEAKED`, the latter being a failure of the round.

**`SI1-7` — what `SI-2` would have to do.** A specification, not an implementation: the ordered
cutover steps, what evidence each needs, and which of this round's artifacts each consumes. No
`SI-2` code, no `SI-2` freeze.

**`SI1-8` — the record-level statement of `#140` and `#141`.** `#140` — every round's `base` equals
its historically mandated base — is restated as a **schema/global invariant over the manifest**, and
this round says whether the twenty-two records satisfy it as transcribed, reporting any that do not
**without changing them**. `#141` — prior seals evaluated against the landing topology rather than
the pull-request head — is restated as a property of the three-state model, and the round says
whether the model as built has it. Outcomes `RESTATED-AND-HOLDS`, `RESTATED-AND-FAILS` (naming
which), or `RESTATED-ONLY` where the round can state the invariant but not decide it.

## The preregistered predictions, with signs, strengths and recorded reasons

| target | prediction | strength | recorded reason |
|---|---|---|---|
| `SI1-0` | all locating controls hold | HIGH | each was checked at `ff0d5a29` while this freeze was written |
| `SI1-1` | `SCHEMA-BUILT` | HIGH | the data is in hand and frozen in this document |
| `SI1-2` | `VALIDATOR-BUILT` | MEDIUM | the three states are specified here, but `LANDED-PENDING-PIN` has never been implemented and its descendant rule is the delicate part |
| `SI1-3` | `DERIVE-EXACT` | HIGH | measured at `ff0d5a29`: 18 of 18 with exactly one candidate each. This is the one prediction resting on a measurement already taken, and it is recorded as such rather than as a forecast |
| `SI1-4` | `NEGATIVES-COMPLETE` | MEDIUM | twenty cases is a large suite, and cases 18, 19 and 20 are the ones most likely to be got wrong: the first two are about how the checker reads rather than what it checks, and the third is the category error this freeze was amended to forbid |
| `SI1-5` | `CENSUS-EXACT` | MEDIUM | the two implementations are independent, and independence is the point; a divergence is a live possibility and would be a finding rather than a defeat |
| `SI1-6` | `SHADOW-ONLY` | MEDIUM | the hazard is accidental, not deliberate: a shared helper edited for the new path can change an old verdict |
| `SI1-7` | delivered | HIGH | it is a specification and its inputs are all named here |
| `SI1-8` | `RESTATED-AND-HOLDS` for `#141`; **NOT PREDICTED** for `#140` | — | `#141` follows from the state model as specified. `#140` is genuinely open: nobody has checked all twenty-two bases against their mandated bases, and this freeze does not guess the answer |

`#140` is left **NOT PREDICTED** deliberately. It is the one place this round could turn up something
about the existing record, and a freeze that predicted it would be scoring a question it has not
asked.

## The STATUS RULE, FROZEN

- A target is **decided** only by the artifact it names: a record by its bytes, a validator property
  by an executed test, an agreement by the census.
- `CENSUS-EXACT` is **not** a claim that the new validator is correct. It is a claim that two
  implementations agree on the states the repository and the controls present. Both could be wrong
  together, and the frozen sentence for this outcome says so.
- A divergence in `SI1-5` is recorded with both verdicts and the round **stops short of adjudicating
  which is right**. Adjudication is the owner's, and if the old machinery is the one in error that is
  a finding about the existing record which `SI-1` has no authority to act on.
- `AUTHORITY-LEAKED` on `SI1-6` **fails the round**. It is not a discrepancy to record; it means the
  round did the thing it promised not to do.
- No outcome of this round licenses any sentence about which mechanism gates.

## The frozen post-round sentences, one per outcome

**`SI1-3`, `DERIVE-EXACT`:** "For all eighteen sealed rounds the landing merge derived from the
sealed head — as the unique merge in reachable history whose non-first parent is exactly that head —
is the merge the record already pinned. Six of those landings lie on main's first-parent spine and
twelve lie one step off it, and both shapes are in the test corpus."

**`SI1-3`, `DERIVE-PARTIAL`:** "Derivation disagreed with the pin for the rounds named below. The
disagreement is recorded; no pinned value was changed, and no historical commit was moved."

**`SI1-5`, `CENSUS-EXACT`:** "On every one of the twenty-two records and on every synthetic control,
the existing per-round machinery and the generic validator returned the same verdict: the eighteen
`sealed` records agreeing on lifecycle and verdict, the four `base-only` records agreeing on schema,
pinned `base` and record integrity, those four having no lifecycle to agree about. This is an
agreement census and not a proof of correctness: it shows the two implementations do not differ on
the cases presented, and it would not detect an error both share."

**`SI1-5`, `CENSUS-DIVERGENT`:** "The two implementations disagreed on the records named below. Both
verdicts are recorded. This round does not adjudicate which is correct and changed neither
implementation to remove the disagreement."

**`SI1-6`, `SHADOW-ONLY`:** "Authority did not move. Every check that existed at the base returns the
same verdict at the execution head, no seal constant and no prior-seal comparison was removed, and no
existing check consults the new validator. The new validator is present in the tree and gates
nothing; presence is not authority."

**`SI1-8`, `#140` outcomes:** "`RESTATED-AND-HOLDS`: every transcribed base equals the base its round
was mandated to use." / "`RESTATED-AND-FAILS`: the records named below carry a base that does not
equal the base the round was mandated to use. This is recorded as found. No record was changed, and
whether it is a transcription question or a question about the round's own history is the owner's to
adjudicate." / "`RESTATED-ONLY`: the invariant is stated in the schema and this round could not
decide it, for the reason given."

## What no outcome of this round licenses

1. Any sentence that the manifest is, or should now be treated as, authoritative.
2. Any removal, weakening or bypass of an existing check.
3. Any change to a historical `B`, `E`, `L` or `P`, or to any preregistration or result note.
4. Any claim that the new validator is *correct*, as distinct from *in agreement*.
5. Any statement about Act 21's targets, or that Act 21 may open.
6. Any adjudication of a census divergence, or of a `#140` failure, in this round.
7. Any claim that `SI-2` is safe because `SI-1` was green: `SI-2` carries its own evidence
   obligations and this freeze does not discharge them in advance.

## Named hazards

**`H1` — self-certification.** The temptation is to let the new validator certify the round that
introduces it. The split exists to prevent exactly that: in `SI-1` the old machinery is
authoritative, and `SI-2`'s bootstrap evidence is `SI-1`'s **already-certified independent
agreement**, not a special case invented during cutover. A freeze for `SI-2` that invents a
self-certification path is the failure this round's structure is designed to make unnecessary.

**`H2` — "shadow code already changed the semantics".** Addressed by `SI1-6` and by the narrow
statement above: presence is not authority, and the round proves it mechanically rather than
asserting it.

**`H3` — agreement mistaken for correctness.** Two implementations written in one round, by one
author, from one specification, can share a misreading. The frozen `CENSUS-EXACT` sentence says this
in terms, and the twenty negative cases exist because agreement on the positive cases is the weaker
half of the evidence.

**`H4` — the transcription reading the wrong assignment.** Live and measured: `_RNT_SEALED_HEAD` and
`_RNT_MERGE` are each assigned twice at module level, so a last-assignment parse yields `'f' * 40`
and `'e' * 40`. Addressed by checking the transcription against this freeze's table and by negative
case 18.

**`H5` — first-parent derivation.** Would have failed twelve of eighteen. Addressed by freezing the
reachable-history scope *and* keeping the first-parent scope as a regression with its expected 6/12
split, so a later narrowing is caught rather than silently accepted.

**`H6` — the `base-only` records represented as broken seals, OR classified as executing.** Four
rounds never had a seal.
Representing them as triples with nulls would misdescribe their history while claiming to transcribe
it. Addressed by making `base-only` its own kind, with a schema failure if such a record carries a
seal field; and by holding those records OUT of the state machine, since the natural wording of
`EXECUTION` — "no record, or a record with no `sealed_head`" — captures all four and would classify
completed historical rounds as permanently executing, applying execution ancestry semantics to them
forever. That wording was in the first draft of this freeze and was corrected before it merged;
negative case 20 exists to keep it corrected.

**`H7` — a deletion passing as no-change.** Addressed by making added, removed and mutated three
distinct conditions over the record *set*.

**`H8` — scope creep into `SI-2`.** Every target above stops at specification where `SI-2` begins.
`SI1-7` is a document, and the guard checks that no file under
`verification/infrastructure/round-si-2-authority-cutover/` exists at the execution head.

**`H9` — the manifest as a new single point of failure.** Mitigated by per-record files, by the
schema's refusal of unknown keys and malformed hashes, and by the pinned-and-derived `L` rule; and
bounded by the fact that in `SI-1` nothing depends on the manifest.

**`H10` — an unrelated repair smuggled in.** The round's diff is confined to the paths listed under
*Files this round reads AND writes*. Anything else, however tempting, is a separate change.

## Definition budget

**Four** slots, and the execution may fire no more:

1. the record schema `O1`;
2. the generic validator `O2` with its three states;
3. the derivation function;
4. the shadow harness `O3`.

The negative-test suite is not a definition slot; it is test code. No slot may introduce a
round-specific branch, and no slot may be a rewrite of an existing check.

## Evidence level

Level 2 — executed code with recorded output — for `SI1-1` through `SI1-6` and for `SI1-8`'s decision
where it is decided. `SI1-0` is a bounded mechanical check. `SI1-7` is a specification and is
reported as type P: it is not evidence about the repository and is **out** of any table of certified
results.

## The chronology control

The property certified is: **no commit reachable from the execution head lies outside `B`'s
descendants.** Asked of the real `pull_request.head.sha`, never of the synthetic merge commit; every
commit of `git rev-list H ^B` required to descend from `B`; recovery of missing objects included;
**fail-closed**.

This round is **NON-SEALING**. It lands `E` → `L`. There is no pin commit, and
`_SI1_SEALED_HEAD` / `_SI1_MERGE` do not exist — not as `None`, not at all. The seal-integrity
obligation this round bears is the data-driven one over the manifest, stated above: the twenty-two
additions are the only permitted change to the record set, and every seal constant in the guard file
is left exactly as `B` carries it.

This preregistration is pinned by path **and** by blob, with a drift control that fails the guard if
one byte is appended.

### What must have merged before the execution begins, checkable mechanically

| # | precondition | check at `B` |
|---|---|---|
| 1 | this freeze is at its settled path | `git show B:verification/infrastructure/round-si-1-shadow-seal-validator/preregistration.md` has the blob `R7-SI1` names |
| 2 | Act 20 is sealed | `git show B:verification/lean/edge_rigidity_probe.py` contains `_RNT_SEALED_HEAD = '0f8b4e06a1cc31ab0c01f2edb5011f1efe545e1b'` and `_RNT_MERGE = '6a6d62e97518600bf2de51cf1d39146d1adbdff9'` |
| 3 | the tag and stem are free | that file contains no `R7-SI1` and no `_SI1` |
| 4 | the manifest does not yet exist | `git ls-tree -r B --name-only` contains no path under `verification/seals/` |
| 5 | `SI-2` does not exist | the same listing contains no path under `verification/infrastructure/round-si-2-authority-cutover/` |
| 6 | the eighteen sealed triples are as frozen | each `sealed_head` and `merge` in this freeze's table appears in that file as a first module-level assignment |
| 7 | the four base-only records carry no seal | that file contains no `_ABR_SEALED_HEAD`, `_CLG_SEALED_HEAD`, `_RBR_SEALED_HEAD` or `_TSG_SEALED_HEAD` |
| 8 | Act 21 has not begun | `git ls-tree -r B --name-only` contains no `act-21-*` path |

## Non-doings

No manuscript edit. No Lean module. No change to `.github/workflows/verify.yml`. No change to
`AGENTS.md` — the lifecycle rule is `SI-2`'s to amend if anything, and only once authority has
actually moved. No deletion of any file. No change to any existing `R7-*` clause's verdict. No new
top-level directory beyond `verification/infrastructure/` and `verification/seals/`.

## Execution discipline

The execution branches from this merge commit and from nothing else, and verifies the start state
before any target. It never absorbs later main before certification: no merge from main, no rebase,
no amend, no force-push. Its head is the object the guard certifies.

## Allowed final report

The result note reports, per target, the outcome and the artifact that decided it; the census in
full, as a table and as `census.json`; every negative case with its verdict and its reason string;
each of the twenty cases marked as behaving or not behaving as the table requires; the four
definition slots with what each contains; every discrepancy recorded and not repaired; and every
prediction against its outcome, with `#140` recorded as **not predicted** rather than as a
confirmation either way.

It carries the narrow non-sealing statement verbatim at each place where the round's status could be
read as a claim about authority.

## Points at which this freeze chose a reading, recorded rather than resolved

1. **`verification/infrastructure/` rather than a programme or an audit directory.** Reason given
   above. The alternative — putting the round under `verification/audits/` — was rejected because
   this round changes the instrument rather than auditing the corpus.
2. **`base-only` as a record kind rather than a nullable triple — SETTLED BY THE OWNER, see below,
   and no longer a reading this freeze chose.** It is recorded here because it is a modelling
   choice with consequences for `SI-2`: a later round wanting one uniform shape would have to amend
   the schema, and this freeze would rather that be explicit than have four rounds' history
   misdescribed now.
3. **The ancestry check without a seal triple.** `R7-HBS` took content contracts only; the
   `ABR`/`CLG`/`RBR`/`TSG` shape takes a base and an ancestry check. This round takes the latter
   because the census must demonstrably post-date the freeze, and records that the choice is about
   chronology and not about sealing.
4. **Nineteen negative cases, not fewer.** Cases 18 and 19 are about how the checker *reads* rather
   than what it checks, and are the two most likely to be thought unnecessary. They are the two the
   existing machinery has actually got wrong — the double assignment, and the synthetic-merge
   reading — so they stay.

## Settled by the owner before this freeze merges

The following are prospective design decisions, fixed before `SI-1` executes. They are not findings
of `SI-1`, and `SI-1` does not score itself for rediscovering them.

- The migration is split at the authority boundary. `SI-1` is a non-authoritative shadow round: it
  may add the manifest representation, generic validator, census and controls, but the existing
  sealing machinery remains authoritative throughout the round. `SI-2` is a separate later round,
  begun only from a certified `SI-1`, in which authority may move to the new mechanism. Presence of
  the new mechanism in the tree is not authority.

- Landing derivation ranges over reachable history, not only first-parent history. For a sealed
  execution `E`, the derived landing `L` is the unique reachable merge whose non-first parent is
  exactly `E`. Both historical landing shapes are part of the required regression corpus. The pinned
  `L` and independently derived `L` must agree; zero candidates, multiple candidates, or disagreement
  are hard failures.

- The generic lifecycle has three distinct states: `EXECUTION`, `LANDED-PENDING-PIN`, and `ARCHIVED`.
  `LANDED-PENDING-PIN` is permitted only when the resolved target itself is the landing merge `L`.
  Any descendant of an unpinned `L` fails with `seal pending`. Synthetic merge `HEAD` is never
  substituted for the resolved target when doing ancestry or lifecycle classification.

- Manifest integrity covers the entry set as well as entry contents. Mutation of an existing record,
  removal of an existing record, and addition of a record are distinct conditions. A change to
  previously certified seal data requires prospective authorization by the round that intends to
  change it; it may not arise incidentally from another round.

- Storage is one record per round, loaded as one logical manifest. This avoids making a single shared
  manifest file a serialization point for otherwise independent sibling rounds. The validator reasons
  over the logical set of records, not over file layout as a source of semantics.

- No historical object is retrofitted. Existing `B`, `E`, `L`, `P`, preregistration, result and
  landing objects remain exactly where and as they are. `SI-1` may transcribe and independently
  validate their identities; it does not rewrite their history or reinterpret a past landing into a
  new shape.

- Act 21 remains closed through both infrastructure rounds. Its sealing mechanics are not defined
  under the old per-round-constant scheme and are not frozen until `SI-1` is certified and `SI-2` has
  completed and certified the authority cutover.

### `base-only` as a first-class record kind, settled explicitly

`base-only` is settled as a first-class record kind. `ABR`, `CLG`, `RBR` and `TSG` are **not** to be
modelled as sealed records with `sealed_head: null` and `merge: null`.

The clean schema is a discriminated union conceptually:

- `kind = "base-only"` → requires `base`, forbids `sealed_head` and `merge`.
- `kind = "sealed"` → requires `base`, `sealed_head`, and `merge`.

That distinction describes history rather than implementation state: those four rounds are not "seals
waiting for fields"; they are rounds for which no seal exists. If a future design wants another
representation, that requires an explicit prospective schema amendment. It must not reinterpret these
four records merely to make the data structure cosmetically uniform.

### Two preregistration disciplines confirmed

`#140` stays **NOT PREDICTED**, and the explicit limitation on `CENSUS-EXACT` — that it is an
agreement census and not a proof of correctness, and would not detect an error both implementations
share — stands as written.
