# Seal infrastructure round SI-3 — the legacy seal retirement: PREREGISTRATION

**Control plane only.** This document fixes what `SI-3` will do, what would count as each outcome,
and what no outcome licenses, before any of it is implemented. One file, added. No Lean, no guard
clause, no manifest change, no ROADMAP edit, no manuscript edit.

**The mandated execution base is the merge commit of this pull request**, once that merge and its
`main` push run are themselves certified. The execution branches from exactly that commit and from
nothing else, and its first act is to verify this preregistration's blob at that base.

The base this freeze is written against is `B0` = `d89fff8abb20e2c63a33949b79947650bf47df6a`, the
landing merge `L` of `SI-2` (#673), whose second parent is `SI-2`'s certified execution head
`E` = `df2fab5770085d7e83543c50c00ffc6a3c2a37d0`, certified as the state of `main` by push run
35371369465.

## What `SI-3` is, and what it deliberately is not

`SI-1` built a generic seal validator and a per-round seal manifest and proved they agreed with the
existing machinery. `SI-2` made the adjudicated derivation rule executable, moved every prior
round's authority to that validator while keeping the old machinery as a **shadow**, made the
data-driven integrity rule authoritative while keeping the per-round comparisons as a shadow, and
rewrote §A.37 so that rounds seal through the manifest. `SI-2` deleted nothing, and said why: a
round that deletes protected seal state while calling itself non-sealing contradicts §A.37, and a
round that deletes it while installing the mechanism that certifies the deletion is circular.

**`SI-3` is the retirement round `SI-2` named.** It begins from a world in which the generic
validator and the manifest protocol are already authoritative, and it removes the representation
they replaced: the legacy seal constants, the shadow copies of every cut-over clause, and the
per-round seal-integrity comparisons the data-driven rule shadows. It installs no new authority. It
is certified by the validator `SI-2` made authoritative, and by nothing it builds itself.

**`SI-3` is SEALING, `E` → `L` → `P`.** §A.37 as amended by `SI2-7` says so in terms: the legacy
constants are protected historical seal state until the retirement round, altering or removing any
of them is taking ownership of existing seal state, and the round that does it is sealing and its
`P` writes its own `sealed` manifest record. This preregistration takes that ownership
**prospectively, here, and for exactly the inventory below**. `P` writes `verification/seals/SI3.json`
with `kind: "sealed"`, `base` = the mandated execution base, `sealed_head` = `E`, `merge` = `L`, and
**no legacy constant**: no `_SI3_BASE`, no `_SI3_SEALED_HEAD`, no `_SI3_MERGE`, not as `None`, not at
all, at any point in the round.

**`SI-3` owns and supersedes what its deletions break, and says so before executing.** Amendment 2
of `SI-2` recorded that `R7-SI1`'s seal-constant containment contract, N13, refuses the very
deletions this round performs, and that this round "must prospectively own and supersede N13 itself"
rather than treat the resulting failure as an implementation repair. N13 is one of a class. Every
frozen `SI-1` and `SI-2` contract that this round's deletions would fail is named in *The contracts
this round supersedes* below, with what replaces it; a failure of a contract **not** named there is a
result requiring adjudication and stops the round. The frozen `SI-1` and `SI-2` preregistrations,
amendments and result notes are not edited: their recorded outcomes stand as history, and this
document is where their live re-measurement is retired.

**What it is not.** Track B's act 20 freeze and result reserve **Act 21** for a fresh rigidity
round written after act 20 lands, carrying an attestation-span instruction and a naturality-rung
choice that go into that round's own preregistration. `SI-3` is not Act 21 and is not a Track B
round: it is the third seal-infrastructure round, after `SI-1` and `SI-2`, and it states nothing
about Act 21's targets, attestation span, ladder or rungs. Act 21 is neither opened, closed nor
otherwise affected by any outcome here; its status is the owner's. A first draft of this control
plane carried the Act 21 name and is preserved unmerged as #674; nothing from it is freeze evidence
for `SI-3`.

## What `SI-3` inherits, and only this

1. `SI-2`'s **certified measurements and artifacts**, at the blobs pinned below, including the
   frozen legacy inventory — fifty-nine names, sixty-one statements at `SI-2`'s `B0` — which this
   round consumes as its deletion target, extended by exactly one name as stated in the inventory
   section: `SI-2`'s own `_SI2_BASE`, which `SI-2` excluded from its inventory by stem because it
   was `SI-2`'s required chronology base while `SI-2` ran, and which `SI2.json` makes redundant.
2. `U1`–`U5` as `SI-2` left them, **authoritative and unchanged in semantics**. The union rule and
   the four adjudicated divergences are not reopened.
3. §A.37's *Sealing through the manifest* subsection, as the protocol this round lands under, and
   the one it amends where the retirement leaves it out of date.
4. Amendment 2 point 1's instruction about N13, taken up as stated above.
5. The validator's **prospective path** — `_si1_validate(prospective={stem: base})`, built by
   `SI-1`, reachable through `U3`, and never yet exercised in vivo — as the form in which a sealing
   round with no record is classified `EXECUTION` and then `LANDED-PENDING-PIN`. `SI-1`'s freeze
   called its descendant rule "the delicate part"; this round is where it is first used for a live
   round, and hazard H5 exists for that.

It inherits **no** claim that `U3` is correct, as distinct from authoritative; **no** statement about
Track B; and **no** licence to touch any historical `B`, `E`, `L` or `P`.

## The retirement, stated as an inventory and not as prose

Measured at `B0` from `verification/lean/edge_rigidity_probe.py`, blob
`163d3e1b6bd859d5c4eebafcbf37d4eaa9005b46`. The execution reports against these tables.

### The statements to delete: 62 statements over 60 names

`SI-2`'s frozen inventory, plus `SI-2`'s own base:

| stems | shape | names | statements |
|---|---|---|---|
| `A12P` `A6D` `A6I` `A6P` `CTI` `HYA` `HYB` `HYE` `PC4` `PC4S` `PQT` `RNC` `SGT` `TCF` `TRJ` `WTS` `XTS` | `BASE` + `SEALED_HEAD` + `MERGE` | 51 | 51 |
| `RNT` | `BASE` + `SEALED_HEAD` ×2 + `MERGE` ×2 | 3 | 5 |
| `ABR` `CLG` `RBR` `TSG` | `BASE` only | 4 | 4 |
| `SI1` | `BASE` only | 1 | 1 |
| *(`SI-2`'s frozen inventory)* | | **59** | **61** |
| `SI2` | `BASE` only | 1 | 1 |
| **total at `B0`** | | **60** | **62** |

The `RNT` double assignment — the pin, and the clause-9 self-test rebinding to `('f' * 40,
'e' * 40)` — is two statements per name and is deleted as two statements. **After the round the
guard file carries zero module-level `_<STEM>_(BASE|SEALED_HEAD|MERGE)` statements**, measured by the
same extraction `SI2-6`(b) used, and that zero is a standing contract from this round on.

### The reads to remove or rebind: 228 genuine identifier reads, in three classes

Counted by tokenizing the file with Python's `tokenize` module and keeping `NAME` tokens equal to
one of the sixty names outside their own assignment lines. **That count, 228, and its three-class
partition are what `SI3-2` and `SI3-4` gate on.** Mentions inside string literals are **not
reads**, need no name to exist, and are left exactly as they are; for the record, the same
tokenization counts seventy-eight `(STRING token, name)` pairs — a `STRING` token, docstrings
included, paired once with each of the sixty names it contains as a whole word, a name repeated
inside one token counting once — over twenty-five names, all of them quotations of frozen
result-note phrases inside content contracts. A broader lexical scan counting every occurrence
gives a larger number. **Neither string count gates anything**: they are explanatory, and the
execution reports whatever its own tokenization finds without a bound.

| class | where | reads | disposition |
|---|---|---|---|
| shadow ancestry | the 23 `_<stem>_legacy_ancestry` functions, one per manifested round, each handed to `_si2_authority` as `shadow=` | 116 | **deleted with the functions**; each keyed clause loses its `shadow=` argument and nothing else |
| comparator | the 5 `_<stem>_prior_seals` functions (`TCF`, `RNC`, `TRJ`, `XTS`, `RNT`) and their 8 `_si2_shadow_integrity` recordings | 60 | **deleted with the functions and the recordings**, together with `R7-RNT`'s clause-9 self-test block, which exists only to exercise `_rnt_prior_seals` under a module-level rebinding of the two `RNT` pins |
| other | `R7-HYE` (16: `_hye_seal_state`, `_hye_seals_untouched`, two mutation controls), `R7-PC4S` (3: `_pc4s_round1_seal`), `R7-RNT` (6: the self-test block, deleted above), `R7-SI1` (6), `R7-SI2` (21) | 52 | **rebound to the manifest through one accessor**, field for field, or **retired with the contract that read them** where that contract is named as superseded below; no predicate changes otherwise |

The rebinding rule, frozen: a contract that read `_<STEM>_BASE`, `_<STEM>_SEALED_HEAD` or
`_<STEM>_MERGE` reads instead the `base`, `sealed_head` or `merge` field of `<STEM>.json` through the
accessor `R1` below, compares it to the **same literal or the same other value** it compared the
constant to, and produces the **same verdict** at `B0`'s state of the world. A rebinding that changes
a verdict is not a rebinding; it is a result requiring adjudication, and `SI3-7` catches it.

### The functions to delete

| kind | count | names |
|---|---|---|
| shadow ancestry | 23 | `_rbr_legacy_ancestry`, `_abr_legacy_ancestry`, `_hya_legacy_ancestry`, `_clg_legacy_ancestry`, `_tsg_legacy_ancestry`, `_sgt_legacy_ancestry`, `_a12p_legacy_ancestry`, `_cti_legacy_ancestry`, `_pqt_legacy_ancestry`, `_hyb_legacy_ancestry`, `_a6p_legacy_ancestry`, `_wts_legacy_ancestry`, `_pc4_legacy_ancestry`, `_pc4s_legacy_ancestry`, `_a6d_legacy_ancestry`, `_a6i_legacy_ancestry`, `_hye_legacy_ancestry`, `_tcf_legacy_ancestry`, `_rnc_legacy_ancestry`, `_trj_legacy_ancestry`, `_xts_legacy_ancestry`, `_rnt_legacy_ancestry`, `_si1_legacy_ancestry` |
| comparators | 5 | `_tcf_prior_seals`, `_rnc_prior_seals`, `_trj_prior_seals`, `_xts_prior_seals`, `_rnt_prior_seals` |
| shadow-integrity recording | 1 function, 1 list, 8 call sites | `_si2_shadow_integrity`, `_SI2_SHADOW_INTEGRITY`, and the eight `_si2_shadow_integrity('R7-…', _…_prior_seals())` lines |

The twenty-three keyed clause wrappers — `_rbr_base_ancestry`, twenty-one `_<stem>_execution_ancestry`
and `_si1_execution_ancestry` — **stay**, and after the round each body is exactly
`return _si2_authority('<STEM>', tag='R7-<STEM>')`. `_si2_authority` keeps its `shadow` parameter
with default `None` so that the entry point's signature is not a frozen-region edit, and the
`_SI2_LEDGER` row's `shadow_ok` is `None` for every clause from this round on. The generic helpers
the deleted functions called — `_rbr_archive_ancestry`, `_rbr_strong_ancestry`, `_si1_quiet_ancestry`
— are `U3`'s own and stay.

## The objects `SI-3` builds

**`R1` — the manifest accessor.** One function returning a named field of one round's manifest
record, read through `_si1_load` and nothing else, failing closed on a missing record, a missing
field or a schema failure. It is the **only** replacement for a legacy read anywhere in the file.
Every rebound read in the table above goes through it, so that "where does this guard get that
round's sealed head from" has one answer.

**`R2` — the prospective declaration.** A module-level mapping from stem to mandated base,
**declared outside both marker-bounded regions**, before the first keyed clause runs, and handed to
`U3` as its `prospective` argument by `_si2_manifest_verdicts`. That function lives inside
`SI2-AUTHORITY` and today calls `_si2_validate(_recs, errors=_errs)` with no prospective argument,
and no hook outside the region reaches it; so **this freeze authorizes, in advance, the minimal
generic wiring edit inside the region** — `_si2_manifest_verdicts` reads the declaration and passes
it as `prospective` — as a wiring supersession of `SI-2`'s object and not a new authority. The edit
names no round stem, so `_si2_region_no_stem` keeps passing; it changes nothing in `U1`, `U2`, `U3`
or `U5`'s semantics; and it is bounded by negative case 14. While `SI-3` executes the declaration holds
exactly `{'SI3': <mandated base>}`; `U3` classifies `SI3` as `EXECUTION` and certifies its head by
act 10's strengthened check, and at `L` as `LANDED-PENDING-PIN`. **`P` removes the entry when it
writes the record**, so that from `P` on the round is classified from `SI3.json` alone; a stem that
is both declared and recorded is a failure. This is the bootstrap form §A.37 names — act 10's
strengthened check against the mandated base — reached through the validator's own prospective
path instead of through a per-round constant, which is what makes it possible to carry a base
without writing the representation this round retires. The name is generic and carries no round
stem, and the mapping is the single place a future sealing round declares its base while it runs.

**`R3` — the round-declared integrity baseline.** `U5` today fixes its record set by reading the
seals tree at `_SI2_BASE` and adding `SI-2`'s one authorized record, in `_si2_manifest_at_stage1`,
which lives inside `SI2-AUTHORITY`. That reads a constant this round deletes and hard-codes one
round's authorization. `R3` replaces it with a declaration, beside `R2` and likewise stem-free in
its name, of **the mandated base whose seals tree is the baseline** and **the additions the current
round's preregistration authorizes**; and **this freeze authorizes, in advance, the second minimal
generic wiring edit inside the region** — `U5`'s baseline path consumes `R3` instead of reading
`_SI2_BASE` and `_SI2_STAGE1_ADDITIONS` — on the same terms as `R2`'s: stem-free, no change to
`U5`'s semantics, bounded by negative case 14. `U5`'s semantics are unchanged:
mutated, removed and added are three distinct conditions against that baseline; the only permitted
change is an authorized addition; the current round's own `sealed` record, written at `P`, is
authorized **by stem** here and validated **by content** by `U3`, which must classify it `ARCHIVED`
with the derived landing equal to the pinned one. For `SI-3` the baseline is the twenty-three
records at the mandated base and the authorized additions are exactly `SI2` (at stage 1) and `SI3`
(at `P`).

**Three definition slots** are budgeted, one per object. Test code, the negative suite and the
regression harnesses are not definition slots. Unused slots are recorded as unused.

## THE ORDER IS PART OF THE CONTRACT, AND THE FINAL HEAD IS THE CHECKPOINT

| stage | target | what it does | may not begin until |
|---|---|---|---|
| 1 | `SI3-1` | **one commit, atomically:** `SI2.json` added, `kind: "base-only"`, `base` = `df54b99dba99dc043b11752163d8d348c9e54472`; `R3` declared with that addition and `U5`'s baseline path wired to it; `R7-SI1`'s scoped-integrity contract generalized to the closed-round rule and `R7-SI2`'s twenty-three-record contracts scoped to `_SI2_MANIFESTED`, both per the supersession table, because a twenty-fourth record fails each of them as written; `_si2_guard_edits_bounded`'s "exactly one addition" assertion retired in the same commit; `R7-SI2`'s chronology clause becomes a keyed call to `U3` on that record; the record set is **fixed** at twenty-four from here until `P`. The stage's dry run has every pre-existing tag `PASS` | — |
| 2 | `SI3-2` | `R1` built; every read in the *other* class rebound or retired per the table; `R2` declared with `SI-3`'s base | stage 1 |
| 3 | `SI3-3` | the twenty-three shadow functions, the five comparators, the shadow-integrity recording and `R7-RNT`'s self-test block deleted; the twenty-three keyed calls lose `shadow=` | stage 2's dry run: every pre-existing tag `PASS` |
| 4 | `SI3-4` | the sixty-two statements deleted; zero remain | stage 3's dry run: every pre-existing tag `PASS` |
| 5 | `SI3-5` | the `SI-1` and `SI-2` live re-measurements that consumed the deleted machinery are converted to pinned historical artifacts, per the supersession table | stage 4 |
| 6 | `SI3-6` | §A.37 amended: the legacy representation is retired, the prospective declaration and its removal at `P` stated, the standing prohibition stated, closed rounds' manifest-cardinality contracts read over the records they manifested | stage 4 |
| — | `SI3-7` | the verdict map: the base's guard file is run and every one of its ninety-two tags returns the same verdict at the final head | everything above |

**Each stage is one commit, in this order, and the dry run named in the "may not begin until"
column is taken before the next stage's commit exists.** The final head `E` is the checkpoint:
`SI3-7` is measured at the commit that carries the whole retirement, and `P` adds a record and
removes a declaration and touches nothing the measurement covered.

## The targets, FROZEN

Each target names the artifact that decides it. A target is decided only by that artifact.

**`SI3-0` — locating controls.** The pinned blobs and the preconditions below hold at the mandated
base. Outcomes: `HOLD` / `DRIFTED`. `DRIFTED` stops the round.

**`SI3-1` — `SI-2`'s record, first and then fixed.** Exactly one record is added before any other
stage: `SI2`, `kind: "base-only"`, `base` = `df54b99dba99dc043b11752163d8d348c9e54472`, `SI-2`'s
mandated execution base. The record set is twenty-four at `E` — eighteen `sealed`, six `base-only`
— and nothing else is added, mutated or removed before `P`. `R7-SI2`'s chronology clause, the one
clause `SI-2` kept out of the cutover because `SI-2` had no record, is from this stage a keyed call
to `U3` on `SI2.json`, classified `not-applicable` with the pinned base reachable, exactly as the
five other `base-only` rounds are. **The addition and the scoping it requires land in one commit**:
as written at `B0`, `R7-SI1` fails any record beyond its twenty-two transcriptions and the one
addition `SI-2` authorized, and `R7-SI2` requires exactly twenty-three records with an empty `U5`
delta against `SI-2`'s stage-1 set, so a commit that added the record alone would fail both guards
by construction and prove nothing. Stage 1 therefore also carries the two scoping supersessions
named in the table — `R7-SI1`'s scoped-integrity contract generalized to the closed-round rule,
`R7-SI2`'s record-count contracts scoped to `_SI2_MANIFESTED` — with `_si2_guard_edits_bounded`'s
"exactly one addition" assertion retired alongside, and `U5` reading `R3`. Outcomes:
`RECORD-AS-AUTHORIZED` / `RECORD-DEVIATED`.

**`SI3-2` — every remaining read goes through the accessor.** After this stage, no genuine
identifier read of any of the sixty names exists outside the shadow and comparator functions that
stage 3 deletes: the fifty-two *other*-class reads are rebound through `R1` or retired with their
superseded contract, per the table. Measured by the same tokenization that produced the inventory.
Outcomes: `REBOUND` / `REBOUND-PARTIAL`.

**`SI3-3` — the shadows are gone and nothing gated on them.** Zero `_<stem>_legacy_ancestry`
functions, zero `_<stem>_prior_seals` functions, zero `_si2_shadow_integrity` calls, zero `shadow=`
arguments at the twenty-three keyed calls, and every keyed wrapper body exactly the shadowless form
above. **And the verdict map is unchanged by their removal**, which is what proves `SI2-3`'s claim
that they gated nothing: the stage's dry run has every pre-existing tag `PASS`. Outcomes:
`SHADOWS-RETIRED` / `SHADOWS-PARTIAL` / **`SHADOW-GATED`** — a tag whose verdict changes when a
shadow is removed was gating on it, and that is a finding about `SI-2`'s measurement, reported and
not repaired.

**`SI3-4` — the representation is gone.** Zero module-level `_<STEM>_(BASE|SEALED_HEAD|MERGE)`
statements in the guard file, by `SI2-6`(b)'s extraction; zero genuine identifier reads of any of
the sixty names anywhere; the detector kept as a standing contract so that a future round writing
one fails this tag forever. Outcomes: `RETIRED` / `RETIRED-PARTIAL`.

**`SI3-5` — the archived measurements.** The `SI-1` and `SI-2` contracts named in the supersession
table as *live re-measurement retired* are **replaced, not silently deleted**: each becomes an
artifact-integrity check at the final head — a pin of the artifact the contract produced, `SI-1`'s
`census.json` at `7a3e6288c5f532a849a07beb9a8e5757cdf79d04` and `SI-2`'s at
`d6b2e505da8bb816179a822258d6672b79670155`, by their existing blob identities, each with a one-byte
drift control, each labelled in its guard as **a certified historical measurement of that round's
checkpoint under that round's rule, whose retired side no longer exists and which is not
re-measured**. The mechanical distinction is: the authoritative validator and `U5` remain live and
executable, and every `U3`-side measurement those guards make — the schema, the three states, the
negative suites that exercise the validator, the tag-map comparisons that run historical guard files
from git, `#140` and `#141`'s restatements — keeps running; **only the retired-side comparison
ceases to be reproducible**, and a pinned census is never read as a statement about the current
head. Outcomes: `ARCHIVED-AS-PINNED` / `ARCHIVE-PARTIAL`.

**`SI3-6` — the protocol.** §A.37's *Sealing through the manifest* subsection is amended,
prospectively, so that it states: that the legacy representation is **retired** from `SI-3`'s
landing — the guard file carries no legacy seal constant, no shadow of a manifest verdict and no
per-round seal-integrity comparison, and a round that writes any of them fails the standing contract
`SI3-4` keeps; how a sealing round carries its base while it executes — the prospective declaration
`R2`, and its removal at `P`; how `U5`'s baseline is declared — `R3`; and that **a closed round's
manifest-cardinality and integrity contracts are read over the records that round manifested**, so
that a later round's authorized additions are outside them without a per-round amendment — the rule
Amendment 1 applied to `SI-1` and stage 1 of this round applies to both `R7-SI1` and `R7-SI2`,
stated here once for every round after.
The two halves `SI2-7` wrote about the legacy constants are replaced by the one that now holds: they
are gone. Outcomes: `PROTOCOL-UPDATED` / `PROTOCOL-PARTIAL` / `PROTOCOL-ABSENT`.

**`SI3-7` — the verdict map is preserved.** The base's guard file — `B0`'s, at blob
`163d3e1b…` — is run at the mandated base in a detached temporary worktree with every git and
pull-request environment variable removed, exactly as `SI2-6`(a) runs its base, and its ninety-two
tags and verdicts are compared in process with the head's. Every pre-existing tag returns the same
verdict at the final head. This is the round's sharpest evidence: a deletion round is right exactly
when nothing that was measured before it changes. Outcomes: `MAP-PRESERVED` / `MAP-CHANGED`.
`MAP-CHANGED` stops the round and reports; a changed verdict is never adopted as an improvement.

**The nested cost, accepted and counted.** Each infrastructure guard runs its base's guard file. At
`SI-3`'s head one run of the file executes the guard file **eight** times: the head; `R7-SI1`'s
base; `R7-SI2`'s base and, inside it, its own `SI-1` base; and `R7-SI3`'s base and, inside it, that
base's `SI-1` run and its `SI-2` run with its own `SI-1` run. Amendment 2 point 5 stands: these are
evidence-bearing and are not optimized away. The wall-clock cost is recorded in the result note.

## The contracts this round supersedes, named in advance

Under §A.37's ownership rule this section is the authorization. Each entry names the frozen contract,
why the retirement fails it, and what stands in its place. **Nothing outside this table is touched
in `R7-SI1`, `R7-SI2` or the `SI2-AUTHORITY` region**, and a failure outside it is a result
requiring adjudication.

| guard | contract | why the retirement fails it | disposition |
|---|---|---|---|
| `R7-SI1` | N2, the chronology clause with `_si1_legacy_ancestry` as its shadow | the shadow reads `_SI1_BASE` | shadow deleted; the keyed call to `U3` on `SI1.json` is unchanged and still gates |
| `R7-SI1` | N13, `_si1_seal_constants_intact`, as amended by `SI-2` Amendment 2 | its containment half requires every statement at `99ab6370` to survive; its allowance half requires `_SI1_BASE` and `_SI2_BASE` | **retired**, as Amendment 2 said this round must own; its subject ceases to exist; `SI3-4`'s zero is what holds from here |
| `R7-SI1` | `SI1-5`'s live census reconstruction: `_si1_census` and `_si1_control_census` run the legacy machinery as the old side through `_si1_transcribe` of the guard text | the old side reads the constants | **live re-measurement retired and replaced, not silently deleted**: the clause becomes an artifact-integrity check, `census.json` pinned by its existing blob `7a3e6288…` with a drift control, labelled a certified historical measurement of `SI-1`'s checkpoint; the `U3`-side negatives, including case 18 which calls `_si1_transcribe` on a synthetic string, keep running |
| `R7-SI1` | `SI1-6`'s tag-map comparison and `_si1_no_forbidden_paths`, which name `_SI1_BASE` as a revision | the constant is deleted | rebound to `SI1.json`'s `base` through `R1`; both keep running |
| `R7-SI1` | the `SI1` record literal built from `_SI1_BASE` | the constant is deleted | the literal `99ab6370470ed9d9e4005551581c6c8c18e54bd2`, which is what the record holds |
| `R7-SI2` | the bootstrap chronology clause, and negative case 11 which required it to stay out of the cutover "because `SI-2` has none" | `SI2.json` exists from stage 1; `_SI2_BASE` is deleted | a keyed call to `U3` on `SI2.json`; case 11's reason no longer holds and the case is **retired** |
| `R7-SI1` | the scoped-integrity contract (`SI-2` Amendment 1, point 1): `_SI1_AUTHORIZED_ADDITIONS = {'SI1'}`, and `ok_si1 &= not _si1_unauthorized` failing any record beyond the twenty-two transcriptions and that one addition | stage 1 adds `SI2.json`, a twenty-fourth record | **generalized at stage 1** to the closed-round rule `SI3-6` later writes into §A.37: `R7-SI1`'s cardinality and integrity contracts are evaluated over `_si1_scoped(records)`, the twenty-two it transcribed, and a later round's authorized additions are outside that historical scope; the unauthorized-addition check is retired here because `U5` under `R3` is what polices additions from this round on; `_SI1_TRANSCRIBED <= set(records)` keeps running |
| `R7-SI2` | `SI2-1`'s `_si2_guard_edits_bounded` — `_SI1_AUTHORIZED_ADDITIONS == {'SI1'}`, the two-element N13 allowance present once, `_SI2_BASE` assigned once | the first assertion fails at stage 1; N13 and `_SI2_BASE` are gone by stage 4 | **retired at stage 1** in the same commit as the record addition, not deferred |
| `R7-SI2` | `SI2-1`'s record-count contracts: twenty-three records, `U5` delta empty against `SI-2`'s stage-1 set | `SI-3` adds `SI2` and then `SI3` | **scoped to the twenty-three records `SI-2` manifested**, `_SI2_MANIFESTED`, exactly as Amendment 1 scoped `SI-1`'s to its twenty-two; `U5` moves to `R3`'s baseline |
| `R7-SI2` | `SI2-2`'s negative case 13, the N13 mutation control | N13 is gone | **retired** with N13; with case 11 retired above, `SI-2`'s cases 1–8 and 12 keep running |
| `SI2-AUTHORITY` region | `_si2_manifest_verdicts` calling `_si2_validate` without `prospective`; `_si2_manifest_at_stage1` reading `_SI2_BASE` and `_SI2_STAGE1_ADDITIONS` | no hook outside the region reaches either | **two minimal generic wiring edits authorized**, per `R2` and `R3`: the first passes the declaration as `prospective`, the second reads `R3`'s baseline; no round stem enters the region, `U1`–`U5`'s semantics do not change, and the region's text at the head equals the base's after reverting exactly those two edits (negative case 14) |
| `R7-SI2` | `SI2-3`'s measurement, `_si2_authority_measured` and `_si2_clause_gates_on_u3`: the `shadow=` form required, shadow-forced controls, the in-vivo rebinding that flips eighteen shadows | there are no shadows | **replaced** by `SI3-3`'s shadowless form, measured statically the same way; the static count of clauses gating on `U3` stays twenty-three and the count gating on a legacy constant stays zero |
| `R7-SI2` | `SI2-4`'s live census reconstruction, `_si2_census` and `_si2_control_census` | the old side reads the constants | **live re-measurement retired and replaced, not silently deleted**: the clause becomes an artifact-integrity check, `census.json` pinned by its existing blob `d6b2e505…` with a drift control, labelled a certified historical measurement of `SI-2`'s checkpoint |
| `R7-SI2` | `SI2-5`'s "eight comparator verdicts recorded as shadows" | the comparators are gone | **retired**; `U5` gating with zero live per-round gates keeps running |
| `R7-SI2` | `SI2-6`(b), `LEGACY-INTACT` | the round deletes the inventory it protects | **retired**; `SI3-4`'s zero is the successor contract; the extraction it used is kept as the detector |
| `R7-SI2` | every read of `_SI2_BASE` as a revision: locating controls, base provenance, the base tag map, the region check, the stage-1 baseline | the constant is deleted | rebound to `SI2.json`'s `base` through `R1`, or to `R3` for the baseline; all keep running |
| `R7-RNT` | the clause-9 self-test block | it exercises `_rnt_prior_seals` under a rebinding of the two `RNT` pins | **deleted** with the comparator; the landability it tested is `U3`'s `LANDED-PENDING-PIN` → `ARCHIVED` path, and `RNT` is `ARCHIVED` |
| `R7-HYE`, `R7-PC4S` | the seal-state contracts over `HYA`/`HYB`/`HYE` and `PC4` | they read the triples from constants | rebound through `R1`, same literals, same verdicts |
| all 8 gates | `ok_<x> &= _si2_integrity_ok()` | `U5`'s baseline read `_SI2_BASE` | unchanged in text; `U5` reads `R3` |

What this table does **not** do: it does not edit any frozen document, does not change what `SI-1`
or `SI-2` recorded as their outcomes, does not touch `SI-1`'s scoping or its twenty transcribed-case
suite, and does not reopen anything adjudicated.

## Predictions, with strength

| target | predicted | strength |
|---|---|---|
| `SI3-0` | `HOLD` | HIGH |
| `SI3-1` | `RECORD-AS-AUTHORIZED` | HIGH |
| `SI3-2` | `REBOUND` | HIGH |
| `SI3-3` | `SHADOWS-RETIRED` | MEDIUM |
| `SI3-4` | `RETIRED` | HIGH |
| `SI3-5` | `ARCHIVED-AS-PINNED` | HIGH |
| `SI3-6` | `PROTOCOL-UPDATED` | HIGH |
| `SI3-7` | `MAP-PRESERVED` | MEDIUM |

`SI3-3` and `SI3-7` are MEDIUM for the same reason: `SI-2` measured that the shadows gate nothing
and that the map is preserved, and this round removes them. If a verdict moves, `SI-2`'s measurement
missed a read, and that is the informative outcome. `SI3-4` is HIGH because it is a count.

## The negative suite

`SI-1`'s twenty cases and `SI-2`'s cases 1–8 and 12 remain in force; `SI-2`'s cases 11 and 13 are
retired, per the supersession table, because each asserts a fact this round makes false — that
`SI-2` has no record, and that N13 exists. These are added, and each must satisfy its named outcome
for its named reason:

1. One legacy statement of any shape re-added at the final head — **fails `SI3-4`**.
2. One `_<stem>_legacy_ancestry` function retained, or one keyed call still carrying `shadow=` —
   **fails `SI3-3`**.
3. One `_<stem>_prior_seals` comparator retained, or one `_si2_shadow_integrity` call — **fails
   `SI3-3`**.
4. A genuine identifier read of any of the sixty names surviving outside the deleted functions —
   **fails `SI3-2`**; the same name inside a string literal does not.
5. `SI2.json` absent, or carrying `sealed_head` or `merge` even as null — **fails `SI3-1`**.
6. A twenty-fifth record before `P`, or any record other than `SI3` at `P` — **fails `U5` under
   `R3`** as an unauthorized addition.
7. The prospective declaration present at the same time as `SI3.json` — **fails** as
   declared-and-recorded.
8. A head descending from `SI-3`'s landing `L` before `P` — **fails as seal pending** under `U3`'s
   prospective path; the resolved target being `L` itself — **`LANDED-PENDING-PIN`, permitted**.
9. At `P`: `SI3.json` with `sealed_head` ≠ `L`'s second parent, or `merge` ≠ the unique landing
   `U2` derives — **fails on the second-parent or pin-versus-derived check**.
10. A rebinding through `R1` that changes any pre-existing tag's verdict — **`MAP-CHANGED`**.
11. One byte changed in a pinned archived census — **fails `SI3-5`'s drift control**.
12. §A.37 still saying the legacy constants remain "PROTECTED HISTORICAL SEAL STATE" — **fails
    `SI3-6`**.
13. `R1` asked for a field of a record that does not exist, or a `base-only` record's
    `sealed_head` — **fails closed**, never returns a default.
14. The `SI2-AUTHORITY` region at the head differing from the base's by anything other than the
    two authorized wiring edits — measured as `SI-2` measured its relocation: the region text with
    exactly those two edits reverted must equal the base's, and must differ before reverting —
    **fails**; a round stem appearing in the region **fails** `_si2_region_no_stem` as before.

## What no outcome of this round licenses

1. Any change to a historical `B`, `E`, `L` or `P`, or to any preregistration, amendment or result
   note of any round, `SI-1`'s and `SI-2`'s included.
2. Any claim that the generic validator is *correct*, as distinct from authoritative. The retirement
   removes the old machinery; it does not vindicate the new.
3. Any re-opening of the adjudicated derivation rule or the four adjudicated divergences.
4. Any re-measurement of `SI-1`'s or `SI-2`'s census: their old side no longer exists after this
   round, and the pinned artifacts are history, not live evidence.
5. Any statement about Act 21, the Track B rigidity round act 20 reserved: its attestation span,
   ladder, rungs or classification, or whether it is open.
9. Any reading of a pinned `SI-1` or `SI-2` census as **current** evidence, and any claim of
   old/new **equivalence** made after retirement: the pinned artifacts are evidence of what `SI-1`
   and `SI-2` measured at their own checkpoints under their own rules, and the retired side can no
   longer be run to say anything about a later head.
6. Any claim that a `MAP-CHANGED` or `SHADOW-GATED` verdict is acceptable because the new mechanism
   is better.
7. Any retrofit. Every historical `B`, `E`, `L`, `P` stays exactly where it is.
8. Any writing of a legacy seal constant, by this round or any later one.

## Hazards

**H1 — the parser trap, now on deletion.** `SI-1` recorded that a parser keeping the *last*
assignment of `_RNT_SEALED_HEAD` returns the self-test's synthetic value. Deletion has the mirror
trap: a deletion that removes the pin and keeps the rebinding leaves a legacy statement in the file
with a fake value. `SI3-4` counts statements, and the self-test block is deleted as a block.

**H2 — the rebinding that moves a verdict.** A contract that compared a constant to a literal now
compares a manifest field to the same literal, and the two should agree at `B0`. A transcription
error in a record would surface here as a changed verdict. `SI3-7` catches it and the round stops;
it is not repaired by editing the record.

**H3 — self-certification, the second time.** `SI-2`'s H3 kept `SI-2` from being certified by the
validator it installed. `SI-3` installs no validator; it is certified by `U3` as `SI-2` left it,
through the prospective path `SI-1` built. What `SI-3` does touch is the wiring — `R2` handed to
`U3`, `R3` read by `U5` — and the two functions that must consume them, `_si2_manifest_verdicts`
and `_si2_manifest_at_stage1`, live inside `SI2-AUTHORITY`. So the region **is** edited, and the
hazard is that a wiring edit becomes a semantic one. The edit is bounded three ways: the
declarations themselves stay outside both regions; the two edits are named in the supersession
table and are the only ones, which negative case 14 measures by reverting exactly them and
requiring equality with the base's region; and `_si2_region_no_stem` keeps running, so no round
stem enters. The `SI1-VALIDATOR` region is not edited at all, and `_si2_region_relocated_verbatim`
keeps running against it. Any other edit inside either region is out of scope.

**H4 — the nested run.** Eight executions per run. If runtime becomes a CI failure the round stops
on that actual result.

**H5 — the delicate part.** `LANDED-PENDING-PIN` has never classified a live round. Its descendant
rule — a head descending from the unpinned landing fails, the landing itself is permitted — is
exercised on synthetic repositories by `SI-1`'s suite and will be exercised in vivo for the first
time at `SI-3`'s own `L`. Negative cases 8 and 9 exist for this, and the result note records what the
live classification said at `L` and at `P`.

**H6 — the name.** A first draft of this round was written as Act 21, which act 20 had already
reserved for a different round. The paragraph *What it is not* is the whole of what `SI-3` says
about Act 21, and `SI-1`'s locating control that no `act-21-*` path exists is respected by this
round's directory name.

**H7 — the archive read as live.** A pinned census is a certified statement about a past head under
a past rule. `SI3-5` labels each pin as such in the guard, and non-licence 4 exists so that no later
round quotes it as a current measurement.

**H8 — a stage skipped.** Stages 3 and 4 each require the previous stage's dry run to be all-`PASS`
before the commit exists. A deletion committed on top of a stage whose dry run was never taken
cannot say which stage moved a verdict.

## Start state, pinned

| path | blob at `B0` |
|---|---|
| `verification/infrastructure/round-si-2-authority-cutover/preregistration.md` | `bfcd43831d887c006eab64c9a4b8b5f35ff41c9a` |
| `verification/infrastructure/round-si-2-authority-cutover/amendments/amendment-1.md` | `9d05509d8fb84d9007c73b40a062bbdb7b6c36ea` |
| `verification/infrastructure/round-si-2-authority-cutover/amendments/amendment-2.md` | `c57d1dc9a3b370c86a91fcb01f7209ef5da782d5` |
| `verification/infrastructure/round-si-2-authority-cutover/result.md` | `9b42ff9b2cfc47b66136e0513eb8bff756566db4` |
| `verification/infrastructure/round-si-2-authority-cutover/census.json` | `d6b2e505da8bb816179a822258d6672b79670155` |
| `verification/infrastructure/round-si-2-authority-cutover/si2-tagmap.json` | `2b07e27bc873147239fda8f103ef4ce9407ff52c` |
| `verification/infrastructure/round-si-1-shadow-seal-validator/preregistration.md` | `4a5f183a52b2720e0714049ecf34911c55c1ef61` |
| `verification/infrastructure/round-si-1-shadow-seal-validator/result.md` | `3e034dfd4b74978adf8b9a8e4bc4339885a4b65d` |
| `verification/infrastructure/round-si-1-shadow-seal-validator/census.json` | `7a3e6288c5f532a849a07beb9a8e5757cdf79d04` |
| `verification/infrastructure/round-si-1-shadow-seal-validator/si1-tagmap.json` | `057cdf90ed9d9f0e129a076a327dcc6f089f53df` |
| `verification/lean/edge_rigidity_probe.py` | `163d3e1b6bd859d5c4eebafcbf37d4eaa9005b46` |
| `AGENTS.md` | `a28449d11371b529bf346e3b0dcb625c54a9f900` |
| `verification/seals/SI1.json` | `9cefa2001d2ebb8d7f0e67212f9fa9c5eece6a63` |
| `verification/seals/` (tree) | `e4fb69dbf6796462b00b075f192e2d85e2e29031` |

**Preconditions, each checkable mechanically at the mandated base:**

1. `R7-SI3` does not appear in `verification/lean/edge_rigidity_probe.py`. Verified at `B0`: 0
   occurrences.
2. `_SI3` does not appear in that file. Verified at `B0`: 0 occurrences.
3. `verification/seals/` holds exactly 23 records, 18 `sealed` and 5 `base-only`, and no `SI2` and no
   `SI3` record.
4. The guard file carries exactly 62 legacy assignment statements over 60 distinct names, per the
   inventory; 23 `_<stem>_legacy_ancestry` definitions; 5 `_<stem>_prior_seals` definitions; 23
   keyed calls carrying `shadow=`; 8 `_si2_shadow_integrity` call sites. Verified at `B0`.
5. The guard file at `B0` passes: 92 tags, all `PASS`, `R7-SI1` and `R7-SI2` included. Verified by
   push run 35371369465 and by a local run at `L`.
6. `B0` is `d89fff8abb20e2c63a33949b79947650bf47df6a`, its first parent is
   `df54b99dba99dc043b11752163d8d348c9e54472` and its second parent is
   `df2fab5770085d7e83543c50c00ffc6a3c2a37d0`. A provenance fact about `B0`, read as Amendment 2
   point 6 reads `SI-2`'s: checked as `B0` having those parents and lying on the mandated base's
   first-parent spine, not as a requirement that live `main` remain there.
7. `AGENTS.md` §A.37 at `B0` still says the legacy constants "remain **PROTECTED HISTORICAL SEAL
   STATE**" until the retirement round — the sentence `SI3-6` supersedes prospectively.
8. `_si1_validate` at `B0` accepts `prospective`, and `_si2_validate` passes it through; neither is
   edited by this round.
9. `SI2.json` is not present at `B0`, and `_SI2_BASE` at `B0` is exactly
   `df54b99dba99dc043b11752163d8d348c9e54472`, so the record stage 1 writes transcribes the constant
   it retires.

## The guard

Fresh tag **`R7-SI3`**, stem **`_SI3_`** for its own helpers and **no legacy-shaped name**: nothing
matching `_SI3_(BASE|SEALED_HEAD|MERGE)` exists at any commit of the round. It carries this
preregistration pinned **by blob** with a one-byte drift control; its chronology clause is a keyed
call to `U3` on stem `SI3`, which `R2` makes `EXECUTION` while the round runs, `LANDED-PENDING-PIN`
at `L`, and `SI3.json` makes `ARCHIVED` at `P`; the locating controls; the inventory measurements of
`SI3-2`, `SI3-3` and `SI3-4` by tokenization and extraction; the pins of `SI3-5`; the protocol
contract of `SI3-6`; the base run of `SI3-7`; and content contracts holding the result note to the
distinctions this freeze makes — sealing and `E` → `L` → `P`; the inventory as counts; the
supersession table as the authorization; the archived censuses as evidence of `SI-1`'s and
`SI-2`'s checkpoints and never as current evidence, with no claim of old/new equivalence after
retirement; `SI-1`'s and `SI-2`'s recorded outcomes not edited; `SI-3` not being Act 21. Each
contract is mutation-tested against the exact failure it exists to catch.

## The landing shape

`E` → `L` → `P`, on the execution pull request, under §A.37 as amended by `SI2-7`:

- **`E`** is the final head after stage 6 and `SI3-7`, certified by exact-head CI.
- **`L`** has current green `main` as its first parent and exactly `E` as its second. At `L` the
  guard classifies `SI3` as `LANDED-PENDING-PIN`, permitted, "the seal record is still owed".
- **`P`** writes `verification/seals/SI3.json` — `{"round": "SI3", "kind": "sealed", "base":
  <the mandated execution base>, "sealed_head": <E>, "merge": <L>}` — removes the `SI3` entry from
  `R2`, and touches nothing else. From `P` the guard classifies `SI3` as `ARCHIVED`, re-derives `L`
  from `E` over the union of the event's visibility targets, and requires the derived landing to
  equal the pinned one. `P` writes no legacy constant and the guard file's legacy-statement count
  stays zero.
- Full CI must pass again on exact `P` before the pull request merges, and the resulting `main`
  push run must be green before any later round's landing is constructed.

## Chronology

The execution branches from the mandated base and from no other commit, and certifies that
ancestry in act 10's strengthened form — the base an ancestor of the head, and every commit of
`rev-list HEAD ^base` a descendant of the base, recovery included, fail-closed, asked of the real
pull-request head — reached through `U3`'s prospective path and never through a per-round constant.
