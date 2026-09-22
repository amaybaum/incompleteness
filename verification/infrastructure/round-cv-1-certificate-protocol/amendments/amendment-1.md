# CV-1 preregistration — Amendment 1: the landing's push certification, and this round's terminal sequence

This is a **post-landing control-plane amendment** to
`verification/infrastructure/round-cv-1-certificate-protocol/preregistration.md`. It follows the
repository's append-only amendment form (§A.36): the frozen preregistration is not edited, and
this file is the whole of the change.

## What kind of artifact this is

This is a **post-`E` terminal-procedure amendment**, and it is **not an execution control-plane
artifact**. It is **not execution-affecting** in the sense of §A.37: it defines no execution base,
it does not repeat the control-plane lifecycle, no execution resumes from its merge, and it names
no new target, prediction or status rule. `CV-1`'s execution is complete: `E` is sealed and
landed, every target is decided, and every outcome the result note records stands unchanged. What
this amendment changes is the **terminal segment alone** — what must happen between `L` and `A` —
because the frozen segment cannot be completed as written.

It therefore **changes nothing retrospectively**, and in particular:

- `B_CV1`, `E_CV1`, `L_CV1` and `tree(E_CV1)` are what they already are. This amendment does not
  move them and cannot be read as moving them.
- Both censuses keep their frozen outcomes and their committed measurements; `census.json` is not
  recomputed, and neither is `cv1-tagmap.json`.
- The blob of `verification/certificates/CV1.json` **at `E`** is historical and final. It is what
  the attestation row's `certificate` field names, and it is not reissued.
- **`CV1.json` at `E` does not acquire this amendment in its `control_plane` list**, and no later
  commit adds it there. A certificate sealed at `E` cannot carry the landing identity of an
  artifact that did not exist at `E`; requiring it would be an impossible self-reference, since
  this amendment's own `merge` field could only be known after the certificate was sealed. The
  `control_plane` list of `CV1` remains exactly the preregistration, as sealed.

The amendment is evidence about the round, not an input to it. It is read by people and by the
round's record; no verifier derivation consumes it.

Frozen preregistration provenance:

- freeze commit: `0ff5ea0e27abbba24f65213c28df764ca1444d40` (#713);
- authoritative frozen blob: `45509fdf6271687034bc83c4fd86ca44098f58cd`;
- preregistration merge commit on `main`, the mandated execution base: `395d953faa5a2bd4d33c5b642e063f355453cba0`,
  certified by push run 35702332294;
- drafting snapshot: `effd5c865dfcc207624712a6711a54b712642f48`.

**The frozen preregistration remains byte-for-byte unchanged**, historical and authoritative for
everything this amendment does not name.

## 1. What was certified

- `E_CV1` = `9332019aed34e33e83adc5e8740f1ef7c38742da`. Exact-head run 35716484185, all five jobs
  success.
- `L_CV1` = `5fe921ce10e68a2496b9797b0ab2b0b08ae02cdb`, first parent
  `395d953faa5a2bd4d33c5b642e063f355453cba0`, second parent exactly `E_CV1`, tree
  `05b915584230d1dcbb5f272d7c3746db642fcaa6`, identical to `tree(E_CV1)`; it writes nothing.
- Exact-`L` run 35718385581, `pull_request` event, **all five jobs success**: Lean kernel check,
  the standalone `Certificate verifier` job in shadow, `Mathlib bridge` with the release gate
  carrying the authoritative verifier, `Numerical probes` with `R7-CV1` reporting
  `LANDED-UNATTESTED` over 101 checks and no failure, and the control-plane base check.

`L_CV1` was then fast-forwarded onto `main`. That is where the frozen terminal sequence stops.

## 2. What the landing's `main` push run did

Push run 35719492395, at `head_sha` `5fe921ce10e68a2496b9797b0ab2b0b08ae02cdb`, **failed**. Four
of its five jobs succeeded — Lean kernel check, the standalone `Certificate verifier` in shadow,
`Control-plane base check` with its preconditions evaluated at the merge commit, and `Numerical
probes`, in which `R7-CV1` again reported `LANDED-UNATTESTED`, both censuses at their frozen
outcomes, the bridge simulated, and no failure.

The `Mathlib bridge` job failed, at the release gate, on one step:

```
FAIL  certificate-verifier     legacy-owned:base:PRA
```

Every other gate step passed. The gate prints one code; the verifier reports thirty. Reproduced in
a depth-1, single-branch checkout of `L_CV1` under a `push` event, the authoritative verifier
reports `legacy-owned:base:PRA` together with `<STEM>:base:unreachable` for each of the
twenty-nine rounds whose certificate carries topology.

## 3. The cause

The environment, not a disagreement between `V1` and `V2`.

- `V7` names one legacy-owned round, `PRA`, whose pinned base is
  `0bedff07fc1ad2675ecab205c8836e7a90a113d4`. That commit is real and is in this repository's
  history on `main`.
- The `Mathlib bridge` job, which is where the release gate runs, checks out with the default
  `actions/checkout` depth of one commit and a single branch. `Lean kernel check` does the same;
  the other three jobs check out at `fetch-depth: 0`.
- On a `push` event the verifier's visibility target is the reachable history of `HEAD`, which is
  correct, and it then asks git for the recorded bases. In a depth-1 clone those objects are
  absent, so every such question fails closed.
- On a `pull_request` event the verifier materializes the one prescribed remote-tracking ref,
  `refs/remotes/origin/<base ref>`, and that fetch incidentally unshallows the checkout. This is
  why the identical tree passed at `E` and at `L` under pull-request builds, and why the
  standalone shadow job, at `fetch-depth: 0`, is green on the same commit.

Stated as a defect: **the verifier conflates absence from this shallow clone with absence from the
prescribed repository history.** It is the stage-7 finding one layer deeper. The stage-7
correction repaired the pull-request path and was verified on the pull-request path only; the push
path had never been exercised, because the authoritative step entered the gate at this round's
stage 5 and no `main` push run had yet carried it.

## 4. The semantic repair, frozen here

> On a `push` event, if the repository is shallow, materialize the history reachable from the
> already-prescribed visibility target `HEAD`, and then evaluate exactly the same push visibility
> rule.

Bounds, all of them part of this freeze:

- Exactly the history of a commit the verifier is already required to consult is fetched, from
  `origin`. No ref is created; no other commit is named; no local branch and no worktree file
  changes.
- **No fallback**, on any event: not `pull_request.base.sha`, not a local `refs/heads/<ref>`, not
  the synthetic merge commit, not any other ref or SHA.
- If a pinned object still does not exist after that recovery, the check **fails closed**, exactly
  as before.
- The four frozen visibility refusals in the conformance corpus keep failing as frozen, including
  `visibility-unresolvable-base-ref` and `visibility-local-branch-refused`.
- The workflow's checkout configuration is not changed, and neither is the release gate's wiring.

## 5. The recovery commit `R`, and what it may not touch

`R` is a single commit on `main`, whose diff is **exactly one modified file**,
`tools/certificate_verifier.py`, carrying the repair of section 4 and nothing else.

`R7-CV1` pins four artifacts, after landing, to their blobs at `E`: the preregistration, the
result note, `census.json` and `cv1-tagmap.json`. `R` therefore **does not touch the result note**,
and the record of this failure lives in this amendment instead. `R` also touches nothing under
`verification/certificates/`, so the conformance corpus stays at its eighty-nine vectors and both
censuses stay byte-equal to the committed `census.json`.

`R` is certified by the `main` push run of the head that carries it, on all five jobs, before `A`
is constructed. Its
build must show the authoritative verifier passing inside the release gate, the standalone shadow
verifier passing, `R7-CV1` still `LANDED-UNATTESTED` with no failure, both censuses equal to the
committed census, and every tag verdict in the map unchanged.

## 6. The amended terminal sequence

The frozen preregistration requires that "nothing else lands between `L` and `A`". That clause is
amended, for this round only, to:

> Exactly two commits land between `L` and `A`: this amendment, and `R`, in that order. Nothing
> else lands between them.

They land on **one pull request**, this amendment as its first commit and `R` as its second, and
that pull request reaches `main` as a fast-forward, so `main` gains exactly those two commits and
no merge commit. The ordering is what makes the repair a frozen instruction rather than a
description of work already done: section 4 states the repair in full, and `R` implements exactly
that and nothing else.

They are not split into two pull requests. Merging this amendment by itself would put `main` at a
commit whose `push` build runs the unrepaired verifier in the same shallow checkout, which fails
for the reason section 3 gives, deterministically. A second red `main` would record nothing that
this amendment does not already record.

Everything else about `A` is unchanged: a pull request from certified `main`, one commit whose
diff is exactly one created file, `verification/certificates/attestations/CV1.json`, validated
against git by `V6` through the release gate on `A`'s own build, and merged only after that build
is green. `R7-CV1` moves to `ATTESTED` on it.

### The recovery pull request's contract

Every clause below is part of this freeze, and each is checked before the pull request is opened
and again on its exact-head build:

1. its base is exactly `L_CV1` = `5fe921ce10e68a2496b9797b0ab2b0b08ae02cdb`;
2. exactly two commits, this amendment first, the recovery second;
3. no other files than this amendment and `tools/certificate_verifier.py`;
4. the amendment moves `B_CV1`, `E_CV1` and `L_CV1` not at all;
5. the recovery teaches push mode to deepen the ancestry of its already-prescribed `HEAD`, and
   nothing else;
6. no new ref, no alternate SHA, no local-branch fallback, no synthetic-merge fallback;
7. all eighty-nine conformance vectors remain exact;
8. full-history behaviour is unchanged, verdict for verdict;
9. a shallow `push` checkout goes from the measured thirty failures to zero;
10. a genuinely unavailable historical object still fails closed.

Exact-head continuous integration on that pull request must then be green on all five jobs.
`main` is fast-forwarded to exactly that head, and its push run must be green on all five jobs.
Only then is `A` created.

## 7. What `A` records

The attestation row's `ci` block carries exactly three run identities, and this amendment does not
widen that schema: a fourth key would be a post-landing change to `V2`'s frozen row format,
untested by any vector, and adding a vector for it would change the corpus count and break two of
this round's own frozen contracts. The three keys are therefore fixed as:

| key | run | `head_sha` | `conclusion` |
|---|---|---|---|
| `exact_e` | 35716484185 | `9332019aed34e33e83adc5e8740f1ef7c38742da` | `success` |
| `exact_l` | 35718385581 | `5fe921ce10e68a2496b9797b0ab2b0b08ae02cdb` | `success` |
| `main_push` | the push run certifying `R` | `R` | `success` |

**`main_push`, for the `CV-1` bootstrap row and for it alone, is redefined** as: *the successful
`main` push certification that authorizes `A`, after the frozen landing push failed.* It is **not**
the original push of `L`, and it is not to be represented as the original push of `L`. Its
`head_sha` is `R`, not `L_CV1`, and the two are distinguishable from the row itself: `exact_l`
names `L_CV1`, `main_push` names a later commit.

The alternative, writing the failed run into the row with `conclusion: "failure"`, was rejected:
it would leave the certification that actually permitted `A` with no machine-readable place in the
ledger at all.

The landing's own push run, 35719492395 at `5fe921ce10e68a2496b9797b0ab2b0b08ae02cdb`, **failed**.
This amendment is the durable, permanent record of that fact and of its cause, and nothing in the
row is to be read as a claim that `L_CV1`'s push run was green; it was not.

This redefinition is **bootstrap-only**. It governs the one `bootstrap-v1` row the ledger will
ever carry, and it extends to no `native-v2` row, for which `main_push` keeps its frozen meaning:
the push run of that round's own landing.

## 8. The failed run stays in the record

Run 35719492395 is not re-run and not hidden. It is a historical fact about `L_CV1`, and no later
code change can make it green — a rerun on the unchanged workflow would deterministically reach
the same shallow-history failure. `L_CV1` stays on `main`, unchanged, as the landing merge whose
second parent is `E_CV1`.

## 9. Recorded, not resolved

1. This is the class of defect the round exists to expose, found in the round's own bootstrap:
   the first protocol object that gates on repository history, failing on the first event whose
   execution environment does not supply it.
2. The frozen terminal sequence requires an attestation appended **after** a continuous-integration
   verdict that does not yet exist when the objects it attests are written. That makes
   infrastructure availability into protocol state, and it is the same temporal edge the
   two-pull-request lifecycle was adopted to remove elsewhere. Whether `A` should exist at all, or
   whether a round's continuous-integration identities belong somewhere that no later commit has
   to carry, is `CV-2`'s to settle; this amendment does not settle it.
3. The execution's own verification covered a depth-1 checkout under the pull-request event and did
   not cover the push event. The gap was in the coverage, not in the frozen protocol.
