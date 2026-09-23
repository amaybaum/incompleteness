# Act 29, Amendment 1: the terminal sequence, when the pin is correct and another round's guard cannot observe it

Append-only, and **post-`E`**: a terminal-procedure amendment, not an execution control-plane
artifact. It is not execution-affecting under the lifecycle rule — it defines no execution base,
repeats no control-plane lifecycle, and no execution resumes from its merge. The frozen
preregistration is not edited.

Nothing here changes a research result. `A29-P-HOLD`, `A29-N-UNDECIDED`, `A29-0-UNDECIDED` and
`A29-1-NOT-EXECUTED` stand exactly as executed and certified, and so do the recorded readings RD1
and RD2. No kernel file, result note or census changes.

## What stands

| object | commit |
| --- | --- |
| `B_PRA` | `0bedff07fc1ad2675ecab205c8836e7a90a113d4` |
| `E_PRA` | `bf7e96fef8135525e752fb0daba0a082cf10ed44` |
| `L_PRA` | `c03939c2341c7085f0a55bddb61be2d175264dba` |

`E` was certified by run 35740517543, all five jobs success at that exact head. `L` was certified
by exact-`L` run 35744698210 and then by main-push run 35747091969, both all five jobs success,
with `R7-PRA` reading `LANDED-PENDING-PIN` over 216 checks and 133 mutation controls with no
failure. None of these three commits changes, and none is rebased, amended or re-derived.

## The situation this amendment records

The pin commit `P` that the frozen protocol requires — writing `verification/seals/PRA.json` and
removing this round's entry from the prospective declaration — is correct and sufficient on its own
terms. On the tree carrying it, `R7-PRA` reads:

```
R7-PRA authority: U3 keyed on PRA.json -> PASS (ARCHIVED; pinned == derived c03939c2341c;
  second parent is the sealed head; ancestry and reachability hold)
R7-PRA contracts: 216 checks, 133 mutation controls; failures: none
```

The obstacle is in another round's guard. Two of `R7-CV1`'s historical controls read the live seals
directory rather than CV-1's own certified historical subject, so the authorized addition of this
round's record falsifies statements CV-1 makes about a head that predates it. CV-1's Amendment 2
freezes those two defects and their replacement.

This produces a deadlock that neither round can resolve alone. `P` cannot land while `R7-CV1`
fails; the CV-1 repair cannot land first as an ordinary round, because under this protocol every
ordinary descendant of an unpinned landing fails closed as seal pending, and `L_PRA` is exactly
such an unpinned landing on `main`. A repair commit landed on top of `L_PRA` without the pin would
itself be rejected.

## What this amendment authorizes

One atomic terminal sequence, on one pull request from `L_PRA`, in exactly three commits in this
order:

1. **Control plane.** CV-1's Amendment 2 and this amendment. It adds the two amendment files and
   nothing else.
2. **CV-1 repair.** The guard-logic change CV-1's Amendment 2 freezes, and nothing beyond it.
3. **`P`.** This round's pin, in the shape the frozen protocol fixes and no other: create
   `verification/seals/PRA.json` with `kind` `sealed`, `base` `0bedff07…`, `sealed_head`
   `bf7e96fe…` and `merge` `c03939c2…`; change the live prospective declaration from
   `{'PRA': '0bedff07…'}` to `{}`; nothing else, and no legacy constant.

`P` remains the terminal commit and remains exactly the two-file pin. The amendment widens the
*sequence*, not the pin.

The first two commits are staging commits. They exist so that the repair is preregistered before it
is applied and so that the pin itself stays conventional. **Neither may become the tip of `main` on
its own.** Only the final head — `P` — is required to certify, and the landing moves `main` from
`L_PRA` directly to that head in a single reference update.

## Why this shape and not another

- Putting the repair inside `P` would widen the pin beyond the shape the frozen protocol fixes,
  and would make the round's terminal commit carry another round's guard change unannounced.
- Landing the repair as a separate round before `P` is not available: it would place `main`, between
  the two landings, at an ordinary descendant of an unpinned landing, which the guard rejects. This
  is the same reason the protocol already gives for why a needed pin cannot be split into its own
  pull request after the merge.
- Leaving `P` unlanded is not available either: the round's landing is on `main` and owes its seal
  record.

The sequence is therefore the shortest one that keeps every frozen object fixed, preregisters the
repair before applying it, and never exposes a rejected state as the tip of `main`.

## Scope

- No `B`, `E` or `L` changes. `PRA.json` keeps the content already determined from them.
- No research verdict, kernel file, result note or census changes.
- The exception is this round's terminal sequence only. It licenses no general practice of bundling
  repairs with pins, and it is not a precedent for widening any other round's `P`.
- The underlying defect class is CV-1's to own; its Amendment 2 states the replacement rule in terms
  that name no round, so that this is the last instance rather than another exception.
