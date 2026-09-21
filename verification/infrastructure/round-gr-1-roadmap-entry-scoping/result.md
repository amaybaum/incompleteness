# Guard repair round GR-1 — scoping act 28's ROADMAP contract to act 28's own entry: RESULT

**Outcome vector: `GR1-0-HOLD` · `GR1-1-INSTALLED-AS-FROZEN` · `GR1-2-SUITE-AS-FROZEN` ·
`GR1-3-MAP-PRESERVED`.** Every preregistered prediction met.

Executed under the frozen control plane at
`verification/infrastructure/round-gr-1-roadmap-entry-scoping/preregistration.md`, blob
`013ca3d75c65fd884974e7e6350b7c78924bb22b`, from the mandated execution base
`B = 15d08103a9c214395a0cc7948dfda3bc6858f30e`. **The first recorded execution act was the
base-blob check**, which matched before any stage was begun.

The base is that commit because Amendment 1,
`verification/infrastructure/round-gr-1-roadmap-entry-scoping/amendments/amendment-1.md`, blob
`631439af8682eec66a1f9ec3aaacece76d50dfb4`, corrected one mutation control and moved the
mandated base to its own certified merge, after the execution attempted from the preceding base
failed its checkpoint at candidate `2a67dfcab4ba443ec3b980335ce0a59e1b3e4a3b`, which is history
and is neither this round's `E` nor ancestry of it.

## 1 — The round's shape

**Non-sealing, `E` → `L`, no `P`.** The round writes no manifest record, no prospective
declaration and no baseline change.

The `base-only` record `verification/seals/GR1.json` is owed to a later round, which names it as
an authorized manifest addition in its own preregistration. It is not written here, and writing it
during the round would have classified the round `not-applicable` and switched off its own
chronology check.

**The baseline exception, owned by the freeze and exercised here.** `_MANIFEST_BASELINE` remains
act 28's declaration at every commit of the round. Under that declaration `U5` holds the
thirty-two records at act 28's base against mutation, removal and any addition other than `PFR`;
it does **not** hold `PFR.json`'s content, because it reads the current record of an authorized
stem into its own expectation. What protects every record at `B` while this round runs is
`R7-GR1`'s own whole-seals-tree contract, which requires the set of name-and-content pairs under
`verification/seals/` to equal the set at `B` byte for byte, with nothing authorized. That
contract passed at every checkpoint.

## 2 — The one contract this round owns

One leg is retired: the document-wide count of act 28's standing clause. Every other leg, the
adjacency leg included, is retained verbatim, and nothing is restated.

The installed text is the frozen replacement read out of the preregistration rather than retyped:
the frozen old block was required to occur exactly once in the guard file, the bytes before and
after it were required to be unchanged, and the result is compared on every run against the
frozen block the freeze carries.

| leg | disposition |
| --- | --- |
| the actual `P0` cell, read through `_pfr_p0_cell` | retained verbatim |
| the frozen sentence unique in that cell | retained verbatim |
| the position after act 27's anchor | retained verbatim |
| the complete standing clause following the sentence | retained verbatim |
| the frozen sentence nowhere else in the document | retained verbatim |
| the standing clause exactly once in the whole document | **retired** |

## 3 — The stages, and what each checkpoint measured

| stage | commit | dry run |
| --- | --- | --- |
| `GR1-1` | `c511b9b95f01ee8fa93687cfaeb1be93c38da67b` | 92 of 92 pre-existing tags PASS, `R7-PFR` included; no `R7-GR1` |
| `GR1-2` | `7498df5e2215030348fc7efc482ae2032ff2c43d` | 93 tags: the 92 pre-existing all PASS and identical to the stage-1 verdicts; `R7-GR1` the sole failure |
| `GR1-3` | this commit, `E` | 93 of 93 PASS |

Stage 2's dry run was red on exactly two contracts, `artifact-result-note` and `artifact-tag-map`,
and green on every pre-existing tag. That red was the frozen expectation of that checkpoint and
not a defect: the two artifacts named are the ones this stage creates. No third contract failed,
and the failure set was printed by name.

Each checkpoint was taken with `HEAD` fixed at the stage's own commit for the whole run, with a
clean worktree at launch, and the run's own log records the head at start and at exit.

## 4 — The differential acceptance suite

The differential suite is twenty-nine rows over the old predicate and the new one, and the seven
reject-then-accept rows are `RD2` reproduced from the pinned text.

The old column is executed from the base's own guard text, extracted and hashed to
`882077268e15a62b795f0f182d624769fd5fa726a11ca19c9140ce9df44f6472`, so it is the base's code and
not a retyping. The fixtures are built from the ROADMAP at `B`, read from git.

| rows | old | new |
| --- | --- | --- |
| act 28's entry alone | accept | accept |
| act 29's five frozen `P0` sentences, a generic successor, two successors | **reject** | accept |
| the clause adjoining the sentence with no whitespace | accept | accept |
| ten mutations of act 28's entry, each also on top of a successor | reject | reject |

Act 29's five sentences are provenanced: each quoted fragment is required to occur in act 29's
preregistration at `B`, so they are that freeze's and are not asserted here.

## 5 — What this round does not do

`RD2` stands as act 29 recorded it. It is history, neither repaired nor withdrawn, and this round
does not make the recorded failure not have happened. What changes is what holds from this round's
landing on.

Act 28's verdicts, frozen artifacts and seal record are unchanged at the blobs this round pins.

No ROADMAP, Lean, census or manuscript file is edited, and no seal record is written.

Act 29's verdicts are not read and not reported by this round.

## 6 — The verdict map

`gr1-tagmap.json` carries two columns over the ninety-two pre-existing tags and no others.

The **head column** is the ninety-two inherited verdict lines of the accepted stage-2 checkpoint
run at `7498df5e2215030348fc7efc482ae2032ff2c43d`, taken verbatim from that run and neither
regenerated nor normalized from another run.

The **base column** is the tag-to-verdict map of the base's own guard file, run once at `B` in a
detached temporary worktree with `GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE` and the
pull-request environment variables removed, so the base's guard resolves `HEAD` to the base
commit and its own regressions build their synthetic repositories without an environment leak.
That single base run took **144 seconds**. It is taken once and persisted; this clause does
not re-run the base's file on every build, because the evidence it gives is a fact about `E` and
is fixed once `E` is fixed.

Both columns hold the same ninety-two tags, every verdict `PASS`, and neither carries `R7-GR1`.

## 7 — Definition budget

Three definition slots were budgeted and three were used.

| slot | object |
| --- | --- |
| `R1` | the replaced predicate `_pfr_road_ok`, same name, same call sites |
| `R2` | the guard clause `R7-GR1`, one appended block |
| `R3` | the result note and `gr1-tagmap.json` |

## 8 — The targets, decided

| target | outcome |
| --- | --- |
| `GR1-0` | `HOLD` — the pinned blobs and the preconditions hold at the mandated base |
| `GR1-1` | `INSTALLED-AS-FROZEN` — the predicate equals the frozen replacement and the change budget is the two owned regions |
| `GR1-2` | `SUITE-AS-FROZEN` — all twenty-nine rows returned the expected pair |
| `GR1-3` | `MAP-PRESERVED` — the ninety-two pre-existing tags return the same verdict at `E` as at `B` |

No expectation was edited to fit, and no deviation from the freeze was found.

## 9 — The landing shape

`E` → `L`, with no `P`. `L` takes current green `main` as its first parent and exactly `E` as its
second, and writes nothing. From the landing the clause classifies the round `LANDED-UNRECORDED`,
recovering `E` as the landing's non-first parent, until a later round writes the record.
