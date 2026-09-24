# Verifier protocol 3 (V3) — architecture specification

> **A round certifies the objects and state it owns. Unrelated mutable repository or hosting state
> cannot invalidate a historical round.**

This document specifies protocol 3 of the repository's round verification. Protocol 1 is the guard
(`V1`) and protocol 2 the round certificate (`V2`). This specification was produced by round `V3-1`
under the frozen preregistration
`verification/infrastructure/round-v3-1-architecture/preregistration.md`, whose settlements `S1` to
`S13` it states as normative text. Round `V3-3`, under the frozen preregistration
`verification/infrastructure/round-v3-3-specification-resolution/preregistration.md`, settled the
seven gaps round `V3-2` recorded, `K1` to `K4` and `G5` to `G7`. Round `V3-5`, under the frozen
preregistration
`verification/infrastructure/round-v3-5-specification-completion/preregistration.md`, settled the
five gaps round `V3-3` recorded, `G8` to `G12`. Each settlement is normative text under its
identifier. The specification is not operative: until a later round activates it, every round is
governed by `AGENTS.md` §A.37, and no `V1` or `V2` state is changed or migrated by it.

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
| `R₁ … Rₖ` | the reconciliation commits of the round (`G11`), merges whose first parent is the tip of `main` when each is built |
| `Λ` | the landing object: the last reconciliation, `Rₖ` |
| `LB` | the landing base: `Λ`'s first parent |
| `Q` | the final receipt commit: a single-parent child of `Λ`, which publication makes the tip of `main` |

Every other object named below is defined where it is named.

**The round's record directory** is one repository directory the round declaration names (`K1`).
It holds the round's **control-plane files**, `preregistration.md` and the files under
`amendments/`, and its result note `result.md`. **The receipt path** is
`verification/receipts/<round id>.json`, where the round id matches `[A-Z0-9]+(-[A-Z0-9]+)*`.

**A path's state at a commit** is either the pair (mode, object id) of the path's entry in that
commit's tree, or its absence from that tree.

### `K1` — the round declaration

The preregistration declares the round in one fenced block with info string `v3-round`; `K2` fixes
where the block lies. Each line of the block that is not blank and does not start with `#` is
`<key> <value>`, the two separated by one space. `<key>` is `round`, `kind` or `record-directory`,
and each of the three appears exactly once, in any order:

- `round` is the round id, matching `[A-Z0-9]+(-[A-Z0-9]+)*`;
- `kind` is `sealing` or `non-sealing`;
- `record-directory` is a path `S7` accepts, ending in `/`: the directory that holds the
  preregistration carrying the block.

A block that breaks any of these rules is invalid, and so is a control plane without one. The
receipt's `round` and `kind`, whose subject is `F`, are re-derived from the declaration at `F` and
must equal it. The declaration names the round's record directory, whose control-plane files are
the only paths `delta(D, F)` may touch (`S2`), and it fixes the receipt path,
`verification/receipts/<round>.json`. Neither the round id nor the kind is derived from a path.

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
| `K1` | the round declaration | `K1`, under the objects; lifecycle transitions T1 and T7 |
| `K2` | the declarations lie in the preregistration | `K2`, under `S7`; lifecycle transition T1 |
| `K3` | the first parent of every reconciliation | `K3`, under `S9`; lifecycle transition T6 |
| `K4` | every receipt commit | `K4`, under `S10`; lifecycle transitions T6 and T7 |
| `G5` | the halted execution is linear | `G5`, under `S12`; lifecycle transition T5 |
| `G6` | the record class is the round's own record | `G6`, under `S7`; lifecycle transitions T1, T5 and T6 |
| `G7` | no commit after `F` changes the control plane | `G7`, under `S2`; lifecycle transitions T3, T5, T6 and T7 |
| `G8` | mutable state is never a predicate input | `G8`, under `S1`; every predicate of the lifecycle |
| `G9` | before `F` the control plane is a draft | `G9`, under `S2`; lifecycle transition T1 |
| `G10` | declaration blocks are recognized by exact lines | `G10`, under `S7`; lifecycle transition T1 |
| `G11` | the round's later objects are those its final receipt commit reaches | `G11`, under `S3`; lifecycle transitions T6 and T7 |
| `G12` | the seal record | `G12`, under `S7`; lifecycle transitions T1, T3, T6 and T7 |

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

A mutable ref or host state **must not** enter a V3 predicate, whatever the round's control plane
declares (`G8`).

Locating a commit is not a predicate. A verifier **may** be handed `E` or `Q` by any means — an
argument, a ref, a search of history — but whether the round holds is decided from the commits
alone. The one operation that reads the live tip of `main` is publication (`S10`), which either
succeeds atomically or leaves `main` untouched; it is never an input to the round's validity.

### `G8` — mutable state is never a predicate input

No control-plane declaration makes a mutable ref or host state an input to a predicate. The
specification defines no form for such a declaration, and a control plane that names a ref, a
branch or a host setting changes no predicate by doing so. Host facts enter a round in two ways
only. An owner's designation and a check run's conclusion are attestations (`S5`), recorded and
never read by a predicate. Anything else the executor observes on the host — the state of a branch,
a deletion it performs, a setting it changes — is the executor's evidence, recorded in the round's
result note and read by no predicate. Publication (`S10`) inspects the live tip of `main` as an
operation, and the outcome of that operation is not an input to the round's validity.

## `S2` — one pull request per round, anchored at `F`

A V3 round is one pull request. It begins from `D` with control-plane-only commits, which create
the preregistration and may add amendments. Each of these commits has exactly one parent and
changes only control-plane files of the round's record directory.

`F` is the exact commit the owner approves and designates. Before `F` is designated, the control
plane is a draft, which a commit may revise (`G9`); after it, no commit **may** change a
control-plane file. Execution begins only after the required checks have passed on exactly `F` and
the owner has designated `F`.

`F`, and not a merge commit on `main`, is the execution's ancestry anchor. `delta(D, F)` touches only
control-plane files of the round's record directory.

### `G9` — before `F` the control plane is a draft

The commits of `rev-list F ^D` may add, modify and delete the round's control-plane files: the
preregistration may be rewritten, and an amendment revised or removed. Nothing before `F` is
append-only. The constraints on those commits are T1's: each has exactly one parent, `D` is an
ancestor of `F`, and each changes only control-plane files of the round's record directory. The
declarations in force are those `K2` reads at `F`, and no predicate reads the content of a
control-plane file at a commit before `F`. Every earlier state stays in `F`'s history.

### `G7` — no commit after `F` changes the control plane

The rule that no commit after `F` changes a control-plane file binds every commit of the round after
`F`: each execution commit, `W` or the commit that takes its place (`S12`), and each reconciliation
and receipt commit of the round (`G11`), superseded or final. At each of them the round's
control-plane files are exactly those at `F`, each with its state at `F`: none is changed, removed
or added. A control-plane file listed in `landing.resolved_paths` is no exception.

## `S3` — `E` is immutable

Execution starts from `F` and nothing else. Every commit of `rev-list E ^F` has exactly one parent,
and that parent is `F` or another commit of `rev-list E ^F`: no merge and no rebase absorbs later
`main` before certification. Certification fixes `E`: the required checks pass on exactly `E`, and
the owner designates `E`. Nothing after certification rewrites `F..E`, and every later object of
the round descends from `E` (`G11`).

`delta(F, E)` **must** be authorized under `S7`, and no commit of `F..E` changes a control-plane
file.

### `G11` — the round's later objects are those its final receipt commit reaches

The reconciliations and receipt commits of the round are exactly those of one chain, which `Q`
fixes. `Λ`, `Q`'s parent, is the last reconciliation. Each reconciliation's second parent is either
a receipt commit, whose parent is the reconciliation before it in the chain, or, for `R₁`, `E`, `W`
or the commit in `W`'s place (`S12`). `landing.reconciliations` lists the chain's reconciliations,
in order, and nothing else. A reconciliation or receipt commit that `Q` does not reach through that
chain is not an object of the round, whether or not it exists in the repository or was once the
head of the pull request, and no predicate reads it.

Before publication a round may therefore abandon a reconciliation or receipt commit and build again
from `E`, from `W` or the commit in its place, or from a receipt commit it keeps. `F`, `E` and the
commits of `F..E` are never replaced. The result note may record abandoned objects as provenance;
they are not predicate inputs.

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
| `seal` | object `{"records"}`: `records` an array of exactly one `{"path", "blob"}`, the round's seal record path and the object id of its file at `Q` (`G12`) | `Q` | `R` if `kind` is `"sealing"`, `—` otherwise | `—` | `—` |
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
  **Execution paths** are everything else the round may change. The `record` class is exactly the
  round's own record (`G6`).
- `<ops>` is a non-empty subset of `A`, `M`, `D`, written in that order (`A`, `M`, `D`, `AM`, `AD`,
  `MD`, `AMD`).
- `<path>` is a repository-relative path, or a directory prefix ending in `/`.

A path **must not** be empty, contain CR, LF or TAB, start with `/`, contain `//`, or have a `.` or
`..` segment, and no path may appear twice across both classes. A block that violates any of these,
a control plane with no such block, or one with two, is invalid.

### Canonical bytes of a governed-path set

The canonical bytes are the fields `v3-governed-paths` and `v1`, then, for each entry in ascending
order of the UTF-8 bytes of `<path>`, the fields `<class>`, `<ops>` and `<path>`. Every field is its
UTF-8 bytes followed by one NUL byte (0x00), and nothing else is emitted. The digest is the SHA-256
of those bytes, written as 64 lowercase hexadecimal digits.

### Authorization

A changed path is **governed** by the entry of greatest length whose `<path>` equals it or is a
directory prefix of it. The change is **authorized** when the delta record's status letter is in
that entry's `<ops>`, with the status `T` counting as `M`. A path no entry governs is unauthorized;
this includes every path the text block cannot express. A change `G12` excludes is unauthorized,
whichever entry governs it.

The set in force is the set at `F`, re-derived from `F` by the verifier; no later policy redefines
it.

### `K2` — the declarations lie in the preregistration

At `F`, the preregistration carries exactly one `v3-governed-paths` block and exactly one
`v3-round` block (`K1`), which are the declarations in force, and no amendment carries a block with
either info string. Blocks are recognized as `G10` states. An opener that is not closed, or a near
miss, in any control-plane file at `F`, makes the control plane invalid. This fixes where the
declarations lie at `F`; how control-plane files may change before it is `G9`'s.

### `G10` — declaration blocks are recognized by exact lines

The declaration blocks are recognized in the bytes of each control-plane file, line by line and
without Markdown semantics. A line is the bytes between two LF bytes (0x0A), or between the start
or the end of the file and an LF; every other byte, a CR (0x0D) included, belongs to the line. With
`I` either reserved info string, `v3-round` or `v3-governed-paths`:

1. An **opener** for `I` is a line that is exactly three backticks (0x60) followed by `I`.
2. A **closer** is a line that is exactly three backticks.
3. A block for `I` begins at an opener for `I`. Its body is the lines after the opener up to, and
   not including, the first closer after it, where the block ends. An opener after which no closer
   occurs is **not closed**.
4. A **near miss** for `I` is a line that is not an opener and that consists of, in order: zero or
   more spaces (0x20) and TABs (0x09); a run of three or more backticks, or of three or more
   tildes (0x7E); zero or more spaces and TABs; `I`; and then either nothing, or a space, a TAB or
   a CR followed by any bytes.

Nesting has no meaning. An opener is an opener wherever it lies, inside another fenced block, an
HTML comment or any other Markdown construct, and every line of the file, the lines of a block's
body included, is examined for a near miss. A tilde fence, a fence of four or more backticks, an
indented fence and an opener followed by further text are near misses, never declarations. A line
whose info string only begins with `I`, such as `v3-roundtrip`, is neither an opener nor a near
miss. A fenced block with any other info string is not a declaration and is not read.

### `G6` — the record class is the round's own record

With `R` the record directory and `P` the receipt path that the round declaration fixes (`K1`), the
block at `F` is valid for the round only if:

1. it has a `record` entry whose `<path>` is `R` and a `record` entry whose `<path>` is `P`;
2. no `execution` entry's `<path>` lies within `R`, that is, equals `R` or begins with it;
3. every other `record` entry's `<path>` lies within `R`, except one: the block of a sealing round
   has the entry `record A S`, where `S` is the round's seal record path (`G12`).

These conditions are checked against the round, at `F`. A **record path** of the round is a path
that lies within `R`, the path `P`, or a seal record that the round's final receipt names; a path is
not a record path merely because a `record` entry governs it. A halted receipt names no seal record
(`S4`), so the record paths of a halted round are `P` and the paths within `R`. `S12`'s record
commit and halted landing admit record paths in this sense and no others.

### `G12` — the seal record

A sealing round has exactly one seal record, at its **seal record path**
`verification/v3-seals/<round>.json`, where `<round>` is its round id (`K1`). Its block at `F`
carries `record A` of that path (`G6`), so the round may add the file and may never modify or
delete it: if a file already lies at the path, the round's change to it is not an addition, and is
unauthorized. The receipt of a complete sealing round names exactly that path and the object id of
its file at `Q` (`S4`); a non-sealing receipt and a halted receipt name none.

V3 assigns the seal record no field and no format. Its protocol meaning is exactly this: the
durable blob the round owns at its fixed seal record path, whose object id the final receipt pins.
The `.json` extension is conventional. No V3 predicate parses the file or derives any validity from
its content; a consumer of a round's seal record may impose its own format on it, and the V3
verifier does not.

No round changes another round's receipt or seal state. A change is unauthorized, whichever entry
governs it, when it is to a path under `verification/receipts/` other than the round's receipt
path, to a path under `verification/v3-seals/` other than its seal record path, or to any path
under `verification/seals/`, which holds the seal state of protocol 2 and is no V3 round's.

## `S8` — deltas are canonical

### Parsing

For commits `X` and `Y`, `delta(X, Y)` is parsed from the output of

```
git diff-tree -r --raw --no-renames --no-abbrev -z X Y
```

in which no path is quoted or escaped. Each record is the bytes
`:<old_mode> <new_mode> <old_oid> <new_oid> <status>`, one NUL byte, the path bytes, and one NUL
byte. No configuration of the repository changes this output.

### Canonical bytes of a delta

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

### `K3` — the first parent of every reconciliation

The requirement that `D` lie on `LB`'s first-parent chain binds every reconciliation of the round
(`G11`), not only the last. `D` lies on the first-parent chain of `R₁`'s first parent, and for each
`i > 1` the first parent of `Rᵢ₋₁` lies on the first-parent chain of `Rᵢ`'s first parent. The first
parents of the reconciliations therefore lie, in order, on one first-parent chain, which is `LB`'s.
Two consecutive reconciliations may have the same first parent, when `main` has not moved between
them. A round in which one reconciliation's first parent lies behind an earlier one's is invalid,
even when a later reconciliation's first parent lies ahead of both.

## `S10` — publication is a fast-forward to `Q`, and nothing else

`Q` is a single-parent child of `Λ`, and `delta(Λ, Q)` is exactly the receipt path, plus the seal
records a sealing receipt names. The required checks pass on exactly `Q`. Publication is a non-force
update of `main` from `LB` to `Q`: a fast-forward, because `Q` descends from `LB` through `Λ`'s first
parent. After publication the tip of `main` is `Q`; there is no publication commit distinct from
`Q`.

If `main` has moved past `LB` when publication is attempted, the non-force update fails atomically
and `main` is untouched. The round then:

1. builds a further reconciliation, whose first parent is the new tip of `main` and whose second
   parent is either `Q`, which then remains in the round as a superseded receipt commit, or an
   object from which the round builds again (`G11`);
2. builds a new final receipt commit on it, whose receipt names the new `LB` and `Λ` and lists
   every reconciliation of the chain the new `Q` reaches;
3. reruns the required checks on the new `Q`;
4. retries publication.

`F`, `E` and the commits of `F..E` stay as they are.

A `main` that reaches the round's commits through any commit other than `Q` itself — a merge
created on the host, a squash or a rebase — is not a publication of the round.

### `K4` — every receipt commit

`S10`'s rule for `Q` binds every receipt commit of the round (`G11`), superseded or final. Each
receipt commit `Qᵢ` is a single-parent child of the reconciliation `Rᵢ` before it, and
`delta(Rᵢ, Qᵢ)` is exactly the receipt path plus the seal record that the round's final receipt
names, each change authorized (`G12`). The content of a superseded receipt is not read: the final
receipt is the round's durable state (`S4`), and it alone fixes which seal record any receipt
commit carries.

## `S11` — sealing is receipt state, not topology

Sealing and non-sealing rounds use the same lifecycle, commits and receipt position. A sealing
receipt carries `seal`, and `Q` publishes the seal state it owns, which is its one seal record
(`G12`); a non-sealing receipt carries no `seal`, and `Q` publishes none. The V3 lifecycle has no
separate pin commit.

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
that changes only record paths (`G6`) and carries the result note, and that commit takes the place
of `W`.
The halted landing is authorized when every path of `delta(LB, Λ)` is a record path (`G6`) and its
change is authorized.

The semantics, stated exactly:

- **The halted execution's effects do not survive in the published tree.** No `execution` path
  differs between `LB` and `Λ`.
- **The execution commits do remain reachable from `main`**, through `W`, as historical evidence.
- **The receipt names them only as `candidates`**, never as `E`.

### `G5` — the halted execution

The execution commits of a halted round are the commits of `rev-list W ^F` other than `W`. `S3`'s
form binds each of them as it binds the commits of `F..E`: each has exactly one parent, which is `F`
or another of them, so that none absorbs later `main`; and, by `G7`, none changes a control-plane
file. Their delta from `F` is not required to be authorized under `S7`: a halt may follow a change
outside the governed paths, and what of the halted execution reaches the published tree is decided
by the withdrawal invariant and the halted landing.

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
| T1: `DRAFTING` → `FROZEN` | every commit of `rev-list F ^D` has one parent and changes only control-plane files, which it may add, modify or delete (`G9`); the round declaration and the governed-path block at `F` are valid, recognized by exact lines with no near miss (`G10`), and lie in the preregistration (`K1`, `S7`, `K2`); the record class is the round's own record, with a sealing round's seal record path (`G6`, `G12`) | `D`, `F`, the commits between them, their trees |
| T2: `FROZEN` → `EXECUTING` | the first execution commit is a single-parent child of `F` | `F`, that commit |
| T3: `EXECUTING` → `CERTIFIED` | `S3`: `rev-list E ^F` linear from `F`; `delta(F, E)` authorized; no control-plane file changed after `F` | `F`, `E`, the commits between them, their trees, the block at `F` |
| T4: `CERTIFIED` fixes `E` | nothing that follows changes `F..E`; every later commit descends from `E` | `E` and the later commits |
| T5: → `HALTED` | when execution commits exist: they are linear from `F` (`G5`); `W` is a single-parent child of the last, listed in `candidates`, and satisfies the withdrawal invariant; the result note is present at `W` (`S12`); when none exist, the commit that takes `W`'s place changes only record paths (`G6`); no control-plane file changes after `F` (`G7`) | `F`, `W` or the commit in its place, the commits between them, their trees, the block at `F` |
| T6: → `RECONCILED` | `S9`: each reconciliation of the chain `Q` reaches (`G11`) with its parents as specified, and its first parent as `K3` requires; each superseded receipt commit of that chain as `K4` requires; no control-plane file changes at any of them (`G7`); the landing authorized (`S9`, or `S12` with `G6`'s record paths) | `D`, `E` or `W`, each reconciliation and receipt commit of that chain, `LB`, `Λ`, their trees, the block at `F`, the seal record the final receipt names |
| T7: `RECONCILED` → `RECEIPTED` | `Q` a single-parent child of `Λ`; `delta(Λ, Q)` exactly the receipt path and the seal record, each change authorized (`K4`, `G12`); no control-plane file changed at `Q` (`G7`); the receipt at `Q` valid under `S4` and consistent with every subject it records, its `round` and `kind` those of the declaration at `F` (`K1`), and its seal record the round's own (`G12`) | `Q`, `Λ`, the receipt at `Q`, every commit it names |
| T8: `RECEIPTED` → `PUBLISHED` | none: publication is the non-force update of `main` to `Q` (`S10`), which the host performs or refuses | — |

A verifier asked whether a round holds evaluates T1, T3 (or T5), T6 and T7 from `Q` and the commits
its receipt names. Whether `Q` is the tip of `main` is not part of the answer.

***

## Worked examples

Every digest below was derived twice and the derivations agreed byte for byte: once by parsing
`git diff-tree -r --raw --no-renames --no-abbrev -z` as `S8` prescribes, and once independently
from `git ls-tree -r -z` of the two trees, comparing entries. Canonical bytes are shown as lowercase
hexadecimal, wrapped at 64 digits; the lines concatenate.

### `S8` — three deltas between commits of this repository

| from | to | statuses | records | digest |
|---|---|---|---|---|
| `2c6a4373e7a6b5c6faa0b3981f0a8813bc5a5701` | `56b253976e116a7fe547b806f66a12ff6ae76daa` | `A` | 1 | `1a89deb9f260da4bbf53a91b959acbb4ab8bbc99740a7d949c6133c55e815f4e` |
| `f9a99fdf4b3bfeb2d3e830c8d6980ced74d52d23` | `14b9d991c3253d741e6faceea0a81adbfc2ef968` | `A`, `M` | 2 | `6b3b05a0bba80ccb325e7a9fd875ecb9392d2ad3642edb538c2eab34b8f7b2be` |
| `d3212b0ea09ba6b29a060a314ce487d27b3f26da` | `50938dffc32075d9ce3f58ba9c5712716b5c843c` | `D` | 1 | `54e4a5f90e6eb789f88be9f4d8ccb6c8d6de6ebc5946dcde5f12b1e0351b0eee` |

`delta(2c6a4373e7a6, 56b253976e11)`:

```
76332d64656c74610076310073686131004100766572696669636174696f6e2f
696e6672617374727563747572652f726f756e642d67682d312d7265662d6879
6769656e652f726573756c742e6d640030303030303000303030303030303030
3030303030303030303030303030303030303030303030303030303030303000
3130303634340033626365326232623438613532616365326438373364616635
33613435396533316337343633386600
```

`delta(f9a99fdf4b3b, 14b9d991c325)`:

```
76332d64656c74610076310073686131004d00766572696669636174696f6e2f
524541444d452e6d640031303036343400346435636265653832626661633661
3165613739363365633762376233353738306464616431353100313030363434
0062353835643932316562383562383461666230313438323636383438626334
663064663433323730004100766572696669636174696f6e2f696e6672617374
727563747572652f726f756e642d63762d322d76312d7265746972656d656e74
2f726573756c742e6d6400303030303030003030303030303030303030303030
3030303030303030303030303030303030303030303030303030003130303634
3400356333333137306535393064643036383437666139343033666361626534
3661323535333934343300
```

`delta(d3212b0ea09b, 50938dffc320)`:

```
76332d64656c746100763100736861310044002e6769746875622f776f726b66
6c6f77732f636f6465782d676174652e796d6c00313030363434006636643735
6337313339653962323733343136376231626362616166633163366631633339
6565390030303030303000303030303030303030303030303030303030303030
3030303030303030303030303030303030303000
```

### `S8` — a path carrying a newline and non-ASCII bytes

In a scratch repository: a first commit holding `base.txt` with the content `a` and a newline; a
second commit changing `base.txt` to `b` and a newline and adding a file whose path is the bytes
`dir/new`, LF, `line-`, `c3 a9` (UTF-8 `é`), `.txt`, with the one-byte content `x`. The delta between
the two commits has statuses `M` and `A`; its canonical bytes are identical under `core.quotePath` true
and false, and by both derivations. Its digest depends only on the file contents and modes:

`61e4a51182e953b8cd90fe5b95031af5f531744fa5c7a75e865d460da87c36cd`

```
76332d64656c74610076310073686131004d00626173652e7478740031303036
3434003738393831393232363133623261666236303235303432666636626438
3738616331393934653835003130303634340036313738303739383232386431
3761663264333466636534636662646633353535363833323437320041006469
722f6e65770a6c696e652dc3a92e747874003030303030300030303030303030
3030303030303030303030303030303030303030303030303030303030303030
3000313030363434006331623037333065303133333434376261646366643437
666431343465323534383037623036653100
```

### `S7` — governed-path sets

Set G1, given in two orders; both declarations have one digest.

```
record AM verification/infrastructure/round-ex-1/
record AM verification/receipts/EX-1.json
execution AMD tools/ex/
execution M verification/README.md
```

```
# the same set, another order
execution M verification/README.md
execution AMD tools/ex/
record AM verification/receipts/EX-1.json
record AM verification/infrastructure/round-ex-1/
```

Digest of G1: `e8bbfdef7908f026af80b86520349aa377d6963d98a995799aaf83d36251e946`. Canonical bytes:

```
76332d676f7665726e65642d706174687300763100657865637574696f6e0041
4d4400746f6f6c732f65782f00657865637574696f6e004d0076657269666963
6174696f6e2f524541444d452e6d64007265636f726400414d00766572696669
636174696f6e2f696e6672617374727563747572652f726f756e642d65782d31
2f007265636f726400414d00766572696669636174696f6e2f72656365697074
732f45582d312e6a736f6e00
```

Set G2, a sealing round with nested directory entries:

```
record AM verification/infrastructure/round-ex-2/
record AM verification/receipts/EX-2.json
record A verification/v3-seals/EX-2.json
execution AM verification/lean-mathlib/OIBridge/
execution M verification/lean-mathlib/OIBridge.lean
execution AMD verification/lean-mathlib/OIBridge/Scratch/
```

Digest of G2: `0053d9c8bb76392786d52bd9f0da71dcd44455e51833bde01ec15b1ab2942d85`. Under G2, a change to a path is governed as follows:

| path | governing entry | ops |
|---|---|---|
| `verification/lean-mathlib/OIBridge/Scratch/X.lean` | `verification/lean-mathlib/OIBridge/Scratch/` | `AMD` |
| `verification/lean-mathlib/OIBridge/Y.lean` | `verification/lean-mathlib/OIBridge/` | `AM` |
| `verification/lean-mathlib/OIBridge.lean` | `verification/lean-mathlib/OIBridge.lean` | `M` |
| `verification/README.md` | none: unauthorized | — |

Each of these blocks is invalid, and the rule it breaks:

| block content | rule broken |
|---|---|
| `record verification/receipts/X.json` | a line of two fields |
| `recorded AM a/` | an unknown class |
| `record MA a/` | `<ops>` not written in the order `A`, `M`, `D` |
| `record  a/` (two spaces) | empty `<ops>` |
| `record AM ` (trailing space) | an empty path |
| a path ending in CR | a path containing CR |
| `record AM a/b<TAB>c` | a path containing TAB |
| `record AM /a/` | a path starting with `/` |
| `record AM a//b` | a path containing `//` |
| `record AM a/./b` | a `.` segment |
| `record AM a/../b` | a `..` segment |
| `record AM a/` and `execution M a/` | a path appearing twice across classes |
| no `v3-governed-paths` block | exactly one block required |
| two such blocks | exactly one block required |

A valid block that breaks one of `G6`'s three conditions for its round is also invalid; those
conditions are checked against the round, at `F`.

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
      {"path": "verification/v3-seals/EX-2.json", "blob": "5555555555555555555555555555555555555555"}
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
