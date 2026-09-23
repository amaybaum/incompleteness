# Verifier protocol 3 (V3) — architecture specification

> **A round certifies the objects and state it owns. Unrelated mutable repository or hosting state
> cannot invalidate a historical round.**

This document specifies protocol 3 of the repository's round verification. Protocol 1 is the guard
(`V1`) and protocol 2 the round certificate (`V2`). This specification was produced by round `V3-1`
under the frozen preregistration
`verification/infrastructure/round-v3-1-architecture/preregistration.md`, whose settlements `S1` to
`S13` it states as normative text. It is not operative: until a later round activates it, every
round is governed by `AGENTS.md` §A.37, and no `V1` or `V2` state is changed or migrated by it.

The words **must**, **must not** and **may** are normative. Anything this document leaves
undefined is invalid, not permitted.

***

## Objects

| symbol | object |
|---|---|
| `D` | the drafting snapshot: the commit of `main` from which the round's pull request begins |
| `F` | the freeze anchor: the exact control-plane commit the owner designates |
| `E` | the certified execution head: the last execution commit, fixed by certification |
| `W` | the withdrawal commit a halted round appends after its last execution commit |
| `R₁ … Rₖ` | the reconciliation commits, merges whose first parent is the tip of `main` when each is built |
| `Λ` | the landing object: the last reconciliation, `Rₖ` |
| `LB` | the landing base: `Λ`'s first parent |
| `Q` | the final receipt commit: a single-parent child of `Λ`, which publication makes the tip of `main` |

Every other object named below is defined where it is named.

**The round's record directory** is one repository directory the control plane names. It holds the
round's **control-plane files**, `preregistration.md` and the files under `amendments/`, and its
result note `result.md`. **The receipt path** is `verification/receipts/<round id>.json`, where the
round id matches `[A-Z0-9]+(-[A-Z0-9]+)*`.

**A path's state at a commit** is either the pair (mode, object id) of the path's entry in that
commit's tree, or its absence from that tree.

***

## Traceability

| settlement | subject | section |
|---|---|---|
| `S1` | predicates are commit-local | `S1` below, and every predicate of the lifecycle |
| `S2` | one pull request per round, anchored at `F` | `S2`; lifecycle transitions T1 and T2 |
| `S3` | `E` is immutable | `S3`; lifecycle transitions T3 and T4 |
| `S4` | every round has one receipt | `S4`; the receipt field table and the canonical example receipts |
| `S5` | repository facts and attestations are separate | `S5`; the receipt's `attestations` field |
| `S6` | historical assertions are evaluated at their named subject | `S6`; every predicate names its subjects |
| `S7` | governed paths, in two classes, canonical and hashed | `S7`; worked examples |
| `S8` | canonical deltas | `S8`; worked examples |
| `S9` | reconciliation on the pull request, after `E` | `S9`; lifecycle transition T6 |
| `S10` | publication is a fast-forward to `Q` | `S10`; lifecycle transitions T7 and T8 |
| `S11` | sealing is receipt state | `S11`; the receipt's `seal` field |
| `S12` | halted rounds are first-class | `S12`; lifecycle transition T5; the halted example receipts |
| `S13` | no migration | `S13` |

***

## `S1` — predicates are commit-local

A V3 predicate **may** take as input only:

- the commits `D`, `F`, the commits of `F..E`, `E`, `W`, the reconciliation commits, the receipt
  commits of the round, `Λ`, `LB` and `Q`;
- the trees and blobs those commits reach;
- the round's own receipt, read from a named commit.

A V3 predicate **must not** take as input: the existence or tip of any branch (`main`, `dev` or any
other); any remote-tracking ref; any ref under `refs/pull/`; a synthetic merge commit a host
constructs; any field of a host event payload; the working tree; the result of a network fetch; or
the time.

A mutable ref or host state **may** enter a predicate only when the round's control plane at `F`
declares, prospectively and by name, that the round owns it. Such a predicate is evaluated only
inside the round's execution window, between the designation of `F` and publication; no historical
verdict on the round depends on it afterwards.

Locating a commit is not a predicate. A verifier **may** be handed `E` or `Q` by any means — an
argument, a ref, a search of history — but whether the round holds is decided from the commits
alone. The one operation that reads the live tip of `main` is publication (`S10`), which either
succeeds atomically or leaves `main` untouched; it is never an input to the round's validity.

## `S2` — one pull request per round, anchored at `F`

A V3 round is one pull request. It begins from `D` with control-plane-only commits: the
preregistration and, before `F` exists, append-only amendments. Each of these commits has exactly
one parent and changes only control-plane files of the round's record directory.

`F` is the exact commit the owner approves and designates. Before `F` is designated, amendments are
appended; after it, no commit **may** change a control-plane file. Execution begins only after the
required checks have passed on exactly `F` and the owner has designated `F`.

`F`, and not a merge commit on `main`, is the execution's ancestry anchor. `delta(D, F)` touches only
control-plane files of the round's record directory.

## `S3` — `E` is immutable

Execution starts from `F` and nothing else. Every commit of `rev-list E ^F` has exactly one parent,
and that parent is `F` or another commit of `rev-list E ^F`: no merge and no rebase absorbs later
`main` before certification. Certification fixes `E`: the required checks pass on exactly `E`, and
the owner designates `E`. Nothing after certification rewrites `F..E`; later objects only append.

`delta(F, E)` **must** be authorized under `S7`, and no commit of `F..E` changes a control-plane
file.

## `S4` — every round has one receipt

Every V3 round, sealing or not, complete or halted, commits one final receipt at its receipt path in
its final receipt commit `Q`. The receipt is the round's durable state. It does not record the
object id of the commit that carries it.

### Encoding

The receipt is a single JSON object, UTF-8, with no byte-order mark. Keys are unique at every
level. A key not listed in the field table is invalid, at every level. Object ids are strings of
lowercase hexadecimal digits of the width `object_format` fixes (40 for `sha1`, 64 for `sha256`).
Digests are 64 lowercase hexadecimal digits. Paths are strings holding the repository-relative path;
a path that is not valid UTF-8 cannot be written in a receipt and is therefore never authorized.

### The field table

The subject of a field is the commit from whose objects its value is re-derived (`S6`). In the
status columns, `R` is required, `—` is forbidden, and `A` is absent with a reason listed in
`absent`.

| field | type and encoding | subject | complete | halted, execution commits exist | halted, none exist |
|---|---|---|---|---|---|
| `schema` | the string `"v3-receipt"` | — | `R` | `R` | `R` |
| `version` | the integer `1` | — | `R` | `R` | `R` |
| `round` | the round id | `F` | `R` | `R` | `R` |
| `status` | `"complete"` or `"halted"` | — | `R` | `R` | `R` |
| `kind` | `"sealing"` or `"non-sealing"` | `F` | `R` | `R` | `R` |
| `object_format` | `"sha1"` or `"sha256"` | the repository | `R` | `R` | `R` |
| `d` | object id of `D` | `D` | `R` | `R` | `R` |
| `f` | object id of `F` | `F` | `R` | `R` | `R` |
| `control_plane_blobs` | array of `{"path", "blob"}`, one per control-plane file at `F`, sorted by path bytes | `F` | `R` | `R` | `R` |
| `governed_paths_digest` | `S7`'s digest of the block at `F` | `F` | `R` | `R` | `R` |
| `e` | object id of `E` | `E` | `R` | `A` | `A` |
| `tree_e` | object id of `E`'s tree | `E` | `R` | `A` | `A` |
| `execution_delta_digest` | `S8`'s digest of `delta(F, E)` | `F`, `E` | `R` | `A` | `A` |
| `withdrawal` | object id of `W` | `W` | `—` | `R` | `A` |
| `candidates` | array of `{"commit", "tree", "measured"}`, `measured` a string stating what was measured on it | each commit | `R`, possibly empty | `R`, non-empty | `R`, empty |
| `landing` | object `{"base", "object", "reconciliations", "resolved_paths", "delta_digest"}`: `base` the object id of `LB`; `object` that of `Λ`; `reconciliations` the object ids of every reconciliation of the round in order, at least one, the last equal to `object`; `resolved_paths` an array of paths sorted by bytes; `delta_digest` `S8`'s digest of `delta(LB, Λ)` | `Λ`, `LB`, each reconciliation | `R` | `R` | `R` |
| `seal` | object `{"records"}`: `records` an array of `{"path", "blob"}`, the seal records `Q` publishes, sorted by path bytes, non-empty | `Q` | `R` if `kind` is `"sealing"`, `—` otherwise | `—` | `—` |
| `attestations` | array of attestation objects (below) | — | `R` | `R` | `R` |
| `absent` | object mapping each `A` field's name to one reason code | — | `—` | `R` | `R` |

A field marked `A` in a column is absent from the receipt and listed in `absent` with its reason; a
field not marked `A` never appears in `absent`. The reason codes form a closed list:

| reason code | admitted for |
|---|---|
| `halted-before-certification` | `e`, `tree_e`, `execution_delta_digest` in a halted receipt |
| `no-execution-commits` | `withdrawal` in a halted receipt with no execution commits |

Any other code, or an admitted code on any other field, is invalid.

### Attestation objects

Each attestation object has exactly the keys `kind`, `subject`, `commit` and `record`:

- `kind` is `"owner-designation"` (a human attestation) or `"check-run"` (a host attestation);
- `subject` is `"F"` or `"E"`;
- `commit` is the object id of the subject;
- `record` is a string naming where the attestation can be inspected on the host — a comment, a
  review or a run — and is never parsed by a verifier as proof of anything.

A complete receipt carries at least one `owner-designation` and one `check-run` for each of `F` and
`E`. A halted receipt carries at least one of each for `F`, and none for `E`.

## `S5` — repository facts and attestations are separate

Ancestry, trees, blobs, deltas, digests and frozen subjects are **repository facts**: a verifier
re-derives every one of them from the repository alone. The owner's designation of `F` and of `E` is
a **human attestation**; check-run and workflow-run identities and their recorded conclusions are
**host attestations**. Attestations are stored in `attestations`, reported by an offline verifier as
recorded and unverified, and never treated as proved because an identifier parses.

What the offline verifier proves is that the subjects the receipt records exist, have the recorded
trees, blobs and deltas, and stand in the recorded ancestry.

The checks on the final receipt commit `Q` cannot be recorded in the receipt `Q` carries; they are
host state outside the receipt.

## `S6` — historical assertions are evaluated at their named subject

Every assertion names its subject: `D`, `F`, `E`, `W`, a reconciliation commit, `Λ`, `LB` or `Q`. It
is reconstructed from that commit's objects and never from the tree a verifier runs on.

An assertion that a tool produced an outcome at a subject is a host attestation (`S5`). A verifier
**may** reproduce it only by running the tool on the subject's own tree in isolation, and never by
running the current tool over the current tree. An assertion of the form "the census at the
certified subject equals the committed census" is therefore evaluated by reading both from the
subject, and it is unchanged by any later change to the files it counts.

## `S7` — the governed-path set is declared at `F`, in two classes, canonical and hashed

### Declaration

The control plane declares every path the round may change in exactly one fenced block with info
string `v3-governed-paths`. Each line of the block that is not blank and does not start with `#` is
`<class> <ops> <path>`, fields separated by one space:

- `<class>` is `execution` or `record`. **Record paths** carry the round's own record: its record
  directory, its receipt path and, for a sealing round, the seal records its receipt names.
  **Execution paths** are everything else the round may change. The `record` class **must** contain
  the round's record directory and its receipt path.
- `<ops>` is a non-empty subset of `A`, `M`, `D`, written in that order (`A`, `M`, `D`, `AM`, `AD`,
  `MD`, `AMD`).
- `<path>` is a repository-relative path, or a directory prefix ending in `/`.

A path **must not** be empty, contain CR, LF or TAB, start with `/`, contain `//`, or have a `.` or
`..` segment, and no path may appear twice across both classes. A block that violates any of these,
a control plane with no such block, or one with two, is invalid.

### Canonical bytes

The canonical bytes are the fields `v3-governed-paths` and `v1`, then, for each entry in ascending
order of the UTF-8 bytes of `<path>`, the fields `<class>`, `<ops>` and `<path>`. Every field is its
UTF-8 bytes followed by one NUL byte (0x00), and nothing else is emitted. The digest is the SHA-256
of those bytes, written as 64 lowercase hexadecimal digits.

### Authorization

A changed path is **governed** by the entry of greatest length whose `<path>` equals it or is a
directory prefix of it. The change is **authorized** when the delta record's status letter is in
that entry's `<ops>`, with the status `T` counting as `M`. A path no entry governs is unauthorized;
this includes every path the text block cannot express.

The set in force is the set at `F`, re-derived from `F` by the verifier; no later policy redefines
it.

## `S8` — deltas are canonical

### Parsing

For commits `X` and `Y`, `delta(X, Y)` is parsed from the output of

```
git diff-tree -r --raw --no-renames --no-abbrev -z X Y
```

in which no path is quoted or escaped. Each record is the bytes
`:<old_mode> <new_mode> <old_oid> <new_oid> <status>`, one NUL byte, the path bytes, and one NUL
byte. No configuration of the repository changes this output.

### Canonical bytes

The canonical bytes are the fields `v3-delta`, `v1` and the object format name (`sha1` or
`sha256`), then, for each record in ascending order of its path bytes, the fields `<status>`,
`<path>`, `<old_mode>`, `<old_oid>`, `<new_mode>`, `<new_oid>`. Every field is followed by one NUL
byte, and nothing else is emitted.

- `<status>` is one of `A`, `D`, `M`, `T`.
- Modes are six octal digits.
- Object ids are lowercase hexadecimal of the width the object format fixes, with the mode `000000`
  and an all-zero object id on the absent side.

A delta carrying any other status, or the same path twice, is invalid. The digest is the SHA-256 of
the canonical bytes, written as 64 lowercase hexadecimal digits.

### The round's deltas

| delta | from | to | meaning |
|---|---|---|---|
| control plane | `D` | `F` | control-plane files only (`S2`) |
| execution | `F` | `E` | authorized under `S7` (`S3`) |
| landing | `LB` | `Λ` | authorized under `S9` or `S12` |
| receipt | `Λ` | `Q` | the receipt path, plus the seal records of a sealing receipt (`S10`) |

Each is between fixed commits the receipt records or that are derived from them, and never between
a commit and the current tip of `main`.

## `S9` — reconciliation happens on the pull request, after `E`

Later `main` enters the round only through reconciliation commits appended to the pull request's
branch after `E`, or after `W` (`S12`). Each reconciliation `Rᵢ` is a merge with exactly two parents:

- the **first parent** is the tip of `main` when `Rᵢ` is built;
- the **second parent** is the round's branch head before it: `E` (or `W`) for `R₁`, and the
  previous receipt commit for each later reconciliation.

The first reconciliation is always built, with `--no-ff` when `main` has not moved since `D`, so that
`Λ` is always a reconciliation and `LB` is always its first parent. `E` and every earlier commit are
unchanged by reconciliation. `Λ` is the last reconciliation and `LB` is its first parent. `D` lies on
`LB`'s first-parent chain; this, and not the tip of any branch, is how a verifier knows `LB` is later
`main` than `D`.

With `Δ = delta(LB, Λ)`, the landing is authorized when:

1. every path of `Δ` is governed, and its change authorized, under `S7`;
2. for every path of `Δ` other than the receipt path, its state at `Λ` equals its state at `E`,
   unless the path is listed in `landing.resolved_paths`, each of which is governed;
3. every path of `delta(D, E)` either appears in `Δ` with its state at `E`, has at `LB` the same
   state as at `E`, or is listed in `landing.resolved_paths`.

For a halted round `S12` replaces conditions 2 and 3. No branch name and no live ref enters these
conditions.

## `S10` — publication is a fast-forward to `Q`, and nothing else

`Q` is a single-parent child of `Λ`, and `delta(Λ, Q)` is exactly the receipt path, plus the seal
records a sealing receipt names. The required checks pass on exactly `Q`. Publication is a non-force
update of `main` from `LB` to `Q`: a fast-forward, because `Q` descends from `LB` through `Λ`'s first
parent. After publication the tip of `main` is `Q`; there is no publication commit distinct from
`Q`.

If `main` has moved past `LB` when publication is attempted, the non-force update fails atomically
and `main` is untouched. The round then:

1. appends a further reconciliation, whose first parent is the new tip of `main` and whose second
   parent is `Q`;
2. appends a new final receipt commit on it, whose receipt names the new `LB` and `Λ` and lists every
   reconciliation;
3. reruns the required checks on the new `Q`;
4. retries publication.

`F`, `E` and every earlier commit stay as they are. A superseded receipt commit remains in the
history as the second parent of the next reconciliation.

A `main` that reaches the round's commits through any commit other than `Q` itself — a merge
created on the host, a squash or a rebase — is not a publication of the round.

## `S11` — sealing is receipt state, not topology

Sealing and non-sealing rounds use the same lifecycle, commits and receipt position. A sealing
receipt carries `seal`, and `Q` publishes the seal state it owns; a non-sealing receipt carries no
`seal`, and `Q` publishes none. The V3 lifecycle has no separate pin commit.

## `S12` — halted rounds are first-class

A halted round publishes its receipt and its result through the same pull request, and never
manufactures an `E`. The receipt says `status: halted`; `e`, `tree_e` and `execution_delta_digest`
are absent with their reason; and every head that was measured but not certified is listed in
`candidates` and nowhere else.

When execution commits exist, the round appends a withdrawal commit `W`, a single-parent child of
the last of them. The **withdrawal invariant**: for every path governed by an `execution` entry, its
state at `W` equals its state at `F`. If the path is present at `F`, it is present at `W` with the
identical mode and object id; if it is absent at `F`, it is absent at `W`, so a file created during
execution is removed by `W`. `record` paths keep their content, so the result note survives: the
round's `result.md` **must** be present at `W` and at `Λ`.

Reconciliation (`S9`, with `W` in place of `E`) and publication (`S10`) then proceed as for a
complete round. When no execution commits exist, the round appends to `F` a single-parent commit
that changes only `record` paths and carries the result note, and that commit takes the place of
`W`.
The halted landing is authorized when every path of `delta(LB, Λ)` is a `record` path and its change
is authorized.

The semantics, stated exactly:

- **The halted execution's effects do not survive in the published tree.** No `execution` path
  differs between `LB` and `Λ`.
- **The execution commits do remain reachable from `main`**, through `W`, as historical evidence.
- **The receipt names them only as `candidates`**, never as `E`.

## `S13` — no migration

This specification changes no `V1` or `V2` state and does not specify their migration, which later
rounds own. `CV-2`'s unfinished retirement is not touched by it.

***

## The lifecycle

The lifecycle is a sequence of states with one transition each. Every transition is admitted by a
predicate whose inputs are listed; each input is one of those `S1` admits. Attestations accompany
transitions but are never predicate inputs.

| state | reached by |
|---|---|
| `DRAFTING` | the pull request's first control-plane commit on `D` |
| `FROZEN` | T1 |
| `EXECUTING` | T2 |
| `CERTIFIED` | T3 |
| `HALTED` | T5 (from `FROZEN` or `EXECUTING`) |
| `RECONCILED` | T6 (from `CERTIFIED` or `HALTED`) |
| `RECEIPTED` | T7 |
| `PUBLISHED` | T8 |

| transition | predicate | inputs |
|---|---|---|
| T1: `DRAFTING` → `FROZEN` | every commit of `rev-list F ^D` has one parent and changes only control-plane files; the governed-path block at `F` is valid (`S7`) | `D`, `F`, the commits between them, their trees |
| T2: `FROZEN` → `EXECUTING` | the first execution commit is a single-parent child of `F` | `F`, that commit |
| T3: `EXECUTING` → `CERTIFIED` | `S3`: `rev-list E ^F` linear from `F`; `delta(F, E)` authorized; no control-plane file changed after `F` | `F`, `E`, the commits between them, their trees, the block at `F` |
| T4: `CERTIFIED` fixes `E` | nothing that follows changes `F..E`; every later commit descends from `E` | `E` and the later commits |
| T5: → `HALTED` | when execution commits exist: `W` is a single-parent child of the last, listed in `candidates`, and satisfies the withdrawal invariant; the result note is present at `W` (`S12`) | `F`, `W`, the commits between them, their trees, the block at `F` |
| T6: → `RECONCILED` | `S9`: each reconciliation's parents as specified; `D` on `LB`'s first-parent chain; the landing authorized (`S9` or `S12`) | `D`, `E` or `W`, each reconciliation and receipt commit, `LB`, `Λ`, their trees, the block at `F` |
| T7: `RECONCILED` → `RECEIPTED` | `Q` a single-parent child of `Λ`; `delta(Λ, Q)` exactly the receipt path and the seal records; the receipt at `Q` valid under `S4` and consistent with every subject it records | `Q`, `Λ`, the receipt at `Q`, every commit it names |
| T8: `RECEIPTED` → `PUBLISHED` | none: publication is the non-force update of `main` to `Q` (`S10`), which the host performs or refuses | — |

A verifier asked whether a round holds evaluates T1, T3 (or T5), T6 and T7 from `Q` and the commits
its receipt names. Whether `Q` is the tip of `main` is not part of the answer.

***

## Canonical example receipts

The object ids below are illustrative: each role uses a repeated pattern so that the examples cannot
be mistaken for real objects. Everything else is as a verifier would require it.

### Complete, non-sealing

```json
{
  "schema": "v3-receipt",
  "version": 1,
  "round": "EX-1",
  "status": "complete",
  "kind": "non-sealing",
  "object_format": "sha1",
  "d": "dddddddddddddddddddddddddddddddddddddddd",
  "f": "ffffffffffffffffffffffffffffffffffffffff",
  "control_plane_blobs": [
    {"path": "verification/infrastructure/round-ex-1/preregistration.md", "blob": "0101010101010101010101010101010101010101"}
  ],
  "governed_paths_digest": "9999999999999999999999999999999999999999999999999999999999999999",
  "e": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
  "tree_e": "e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0",
  "execution_delta_digest": "8888888888888888888888888888888888888888888888888888888888888888",
  "candidates": [],
  "landing": {
    "base": "babababababababababababababababababababa",
    "object": "c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1",
    "reconciliations": ["c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1"],
    "resolved_paths": [],
    "delta_digest": "7777777777777777777777777777777777777777777777777777777777777777"
  },
  "attestations": [
    {"kind": "owner-designation", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "pull request review designating F"},
    {"kind": "check-run", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "workflow run on F"},
    {"kind": "owner-designation", "subject": "E", "commit": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "record": "pull request comment designating E"},
    {"kind": "check-run", "subject": "E", "commit": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "record": "workflow run on E"}
  ]
}
```

### Complete, sealing, after one base movement

`main` moved once after the first receipt commit was built, so the landing lists two
reconciliations; the first receipt commit is the second parent of the second reconciliation.

```json
{
  "schema": "v3-receipt",
  "version": 1,
  "round": "EX-2",
  "status": "complete",
  "kind": "sealing",
  "object_format": "sha1",
  "d": "dddddddddddddddddddddddddddddddddddddddd",
  "f": "ffffffffffffffffffffffffffffffffffffffff",
  "control_plane_blobs": [
    {"path": "verification/infrastructure/round-ex-2/amendments/amendment-1.md", "blob": "0202020202020202020202020202020202020202"},
    {"path": "verification/infrastructure/round-ex-2/preregistration.md", "blob": "0101010101010101010101010101010101010101"}
  ],
  "governed_paths_digest": "9999999999999999999999999999999999999999999999999999999999999999",
  "e": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
  "tree_e": "e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0e0",
  "execution_delta_digest": "8888888888888888888888888888888888888888888888888888888888888888",
  "candidates": [],
  "landing": {
    "base": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "object": "c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2",
    "reconciliations": [
      "c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1",
      "c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2c2"
    ],
    "resolved_paths": ["verification/ROADMAP.md"],
    "delta_digest": "7777777777777777777777777777777777777777777777777777777777777777"
  },
  "seal": {
    "records": [
      {"path": "verification/seals/EX2.json", "blob": "5555555555555555555555555555555555555555"}
    ]
  },
  "attestations": [
    {"kind": "owner-designation", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "pull request review designating F"},
    {"kind": "check-run", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "workflow run on F"},
    {"kind": "owner-designation", "subject": "E", "commit": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "record": "pull request comment designating E"},
    {"kind": "check-run", "subject": "E", "commit": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", "record": "workflow run on E"}
  ]
}
```

### Halted, with execution commits

```json
{
  "schema": "v3-receipt",
  "version": 1,
  "round": "EX-3",
  "status": "halted",
  "kind": "non-sealing",
  "object_format": "sha1",
  "d": "dddddddddddddddddddddddddddddddddddddddd",
  "f": "ffffffffffffffffffffffffffffffffffffffff",
  "control_plane_blobs": [
    {"path": "verification/infrastructure/round-ex-3/preregistration.md", "blob": "0101010101010101010101010101010101010101"}
  ],
  "governed_paths_digest": "9999999999999999999999999999999999999999999999999999999999999999",
  "withdrawal": "a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0a0",
  "candidates": [
    {"commit": "cacacacacacacacacacacacacacacacacacacaca", "tree": "cbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb", "measured": "the closing checks; one frozen predicate false"}
  ],
  "landing": {
    "base": "babababababababababababababababababababa",
    "object": "c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1",
    "reconciliations": ["c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1"],
    "resolved_paths": [],
    "delta_digest": "7777777777777777777777777777777777777777777777777777777777777777"
  },
  "attestations": [
    {"kind": "owner-designation", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "pull request review designating F"},
    {"kind": "check-run", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "workflow run on F"}
  ],
  "absent": {
    "e": "halted-before-certification",
    "tree_e": "halted-before-certification",
    "execution_delta_digest": "halted-before-certification"
  }
}
```

### Halted, without execution commits

```json
{
  "schema": "v3-receipt",
  "version": 1,
  "round": "EX-4",
  "status": "halted",
  "kind": "sealing",
  "object_format": "sha1",
  "d": "dddddddddddddddddddddddddddddddddddddddd",
  "f": "ffffffffffffffffffffffffffffffffffffffff",
  "control_plane_blobs": [
    {"path": "verification/infrastructure/round-ex-4/preregistration.md", "blob": "0101010101010101010101010101010101010101"}
  ],
  "governed_paths_digest": "9999999999999999999999999999999999999999999999999999999999999999",
  "candidates": [],
  "landing": {
    "base": "babababababababababababababababababababa",
    "object": "c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1",
    "reconciliations": ["c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1c1"],
    "resolved_paths": [],
    "delta_digest": "7777777777777777777777777777777777777777777777777777777777777777"
  },
  "attestations": [
    {"kind": "owner-designation", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "pull request review designating F"},
    {"kind": "check-run", "subject": "F", "commit": "ffffffffffffffffffffffffffffffffffffffff", "record": "workflow run on F"}
  ],
  "absent": {
    "e": "halted-before-certification",
    "tree_e": "halted-before-certification",
    "execution_delta_digest": "halted-before-certification",
    "withdrawal": "no-execution-commits"
  }
}
```
