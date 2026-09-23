# Verifier architecture round V3-1 — the one-pull-request lifecycle, commit-local chronology and the round receipt: PREREGISTRATION

**Status: control plane.** This file is the round's preregistration and nothing else. No
architecture document, receipt definition, model check or status correction exists at the time it
is written; each is an execution object and is created only after the certified merge of this
file.

> **A round certifies the objects and state it owns. Unrelated mutable repository or hosting state
> cannot invalidate a historical round.**

Everything below is subordinate to that sentence. A predicate that would let a branch move, a ref
deletion, a later tree or a host setting change the verdict on a closed round is a defect of the
design, whatever else it buys.

## The commit vocabulary this freeze uses, fixed first

`V3-1` itself is run under `AGENTS.md` §A.37 as it stands at `D`: two pull requests, this control
plane and then one execution pull request that carries its landing. It designs the successor
protocol and does not activate it.

This round's own objects, in §A.37's sense:

- `D` — the drafting snapshot: `b9388cfb5d05ac30349fe7e489c320979d9d135b`, the certified head of
  `main` after the `GH-1` halt record (push run 35898543975, all five jobs green). Every
  measurement in this file was taken at `D` unless it says otherwise.
- `B` — the mandated execution base: the certified merge commit on `main` of this file. It has no
  SHA until that merge exists and its push run is green.
- `M` — a candidate merge of this file into `main`, used only to evaluate `B`-scoped rows before
  the merge.
- `E` — the sealed execution commit, the last commit of the execution branch that branches from
  `B`.
- `L` — the landing merge, first parent current green `main`, second parent exactly `E`.

The objects the V3 protocol defines, which govern no part of this round:

- `D` and `E` keep the meanings above.
- `F` — the freeze anchor: the exact owner-designated control-plane commit of a V3 round.
- `W` — a withdrawal commit, appended by a halted round after its last execution commit.
- `R₁ … Rₖ` — reconciliation commits on the round's branch, each a merge whose first parent is the
  tip of `main` when it is built.
- `Λ` — the landing object: the last reconciliation, whose tree the round publishes.
- `LB` — the landing base: `Λ`'s first parent.
- `Q` — the final receipt commit, a single-parent child of `Λ`; publication makes it the tip of
  `main`.

**Protocol numbering.** Protocol 1 is the guard (`V1`), protocol 2 the round certificate
(`V2`, installed by `CV-1`), protocol 3 the architecture this round specifies (`V3`). The labels
`V1` to `V7` inside `CV-1`'s preregistration name that round's components (its `V3` is the
conformance corpus) and are unrelated to protocol numbers; this freeze never uses them.

## What `V3-1` is, and what it is not

`V3-1` is an **architecture round**. Its deliverable is a specification: one architecture document
that states the frozen settlements below as normative text, fixes the receipt's fields and
presence rules, fixes the byte serializations with worked examples computed from landed commits,
and records a model check of the settlements. It also corrects one status sentence that `GH-1` has
made false on `main`.

It is not an implementation round. It writes no verifier, guard, gate, workflow, seal record,
certificate, attestation, conformance vector, live-policy entry, receipt or `AGENTS.md` text. It
does not migrate `V1` or `V2` state, and it does not touch `CV-2`'s unfinished retirement. The
later sequence — shadow implementation, migration census, authoritative cutover, retirement of
`V1` and `V2` — is out of scope and is not constrained here beyond what the settlements say.

## Measurements at `D` that shape the round

### `F1` — name freedom

`V3-1`, `v3-1`, `round-v3`, `v3-architecture`, `verification/infrastructure/v3`, `§A.39`,
`execution_delta`, `landing_delta`, `governed_path`, `receipt.schema` and `freeze anchor` occur
nowhere in the tree at `D`. `V31` occurs only inside compiled PDF files. The bare symbol `V3`
occurs in text files in two senses: `GH-1`'s preregistration uses it for this architecture, and
`CV-1`'s preregistration and result use it as a component label (the conformance corpus).

### `F2` — where round state is reconstructed from live state at `D`

**The census, frozen as a procedure.** The scan set is every tracked file under `tools/` and
`.github/`, plus `verification/lean/edge_rigidity_probe.py`, whose extension is `.py`, `.yml`,
`.yaml` or `.sh`: 21 files at `D`. Each line is classed by these patterns (a line may carry several
classes):

| class | pattern | lines | files |
|---|---|---|---|
| `C1` remote and remote-tracking refs | `refs/remotes/`, `origin/`, `ls-remote`, a quoted `origin` | 69 | 4 |
| `C2` branch and ref enumeration | `for-each-ref`, `show-ref`, `symbolic-ref`, `--abbrev-ref`, `refs/heads/`, `git … branch` | 15 | 3 |
| `C3` host event context | `GITHUB_*`, `github.sha`/`ref`/`head_ref`/`base_ref`/`event`, `pull_request.head`/`base`, `event_name` | 90 | 3 |
| `C4` `HEAD`-relative queries | a quoted `HEAD`, `HEAD~`/`HEAD^`, `$REF`, `--ref` | 42 | 5 |
| `C5` working-tree reads | `open(`, `read_text(`, `os.walk(`, `glob.glob(` | 460 | 19 |
| `C6` object reads | `show`, `ls-tree`, `cat-file`, `rev-parse` | 135 | 4 |
| `C7` ancestry and reachability | `merge-base`, `is-ancestor`, `rev-list` | 70 | 4 |

Grouped by the function that contains them, the `C1`, `C2`, `C3` and `C7` lines fall in 45
functions of the guard, 13 of `tools/certificate_verifier.py`, 4 of `tools/control_plane_lint.py`
and 2 of `tools/control_plane_base_check.py`. The lexical classes are a superset; most `C5` reads
are a tool reading its own inputs. Read by what they decide, the live-state mechanisms at `D` are
eight:

| | mechanism | where at `D` | what the verdict depends on |
|---|---|---|---|
| `M1` | the certified object chosen from host context | the guard's `_rbr_target_commit` and the per-round ordering and chronology functions (26 defined, 7 reading the event directly); the verifier's `visibility_targets` | `pull_request.head.sha` from the event payload on a pull request, `HEAD` otherwise |
| `M2` | the live base-branch tip | the guard's `_rbr_base_branch_tip`, `_rbr_archive_visibility_targets`, `_si2_union_targets`; the verifier's `visibility_targets`; specified prospectively by the frozen control planes of `SI-1`, `SI-2`, `GR-1` and `CV-1` (with its Amendment 1) | the current `refs/remotes/origin/<base ref>` |
| `M3` | history recovered over the network | the guard's `_rbr_ensure_present` (including `refs/pull/<n>`); the verifier's `recover` and `deepen` | whether a fetch from the host succeeds |
| `M4` | execution-mode ancestry over the chosen target | the guard's `_rbr_strong_ancestry`; the verifier's `strong_ancestry` | `rev-list <target> ^base`, with the target from `M1` |
| `M5` | assertions about a closed round evaluated on a later tree | `R7-CV1`'s `census-equal-to-committed`, which halted `CV-2`; `GR-1`'s two live-tree assertions, which `GR-2` scoped to `GR-1`'s own history; the four `T1` live reads `CV-2` targeted | whatever tree the guard runs on |
| `M6` | change scope from a live ref | `tools/control_plane_lint.py`'s `changed_control_planes`, over `origin/main...HEAD` | the current remote tip of `main` |
| `M7` | a control-plane predicate over a ref the round does not own | `GH-1`'s `GH1-6` conjunct "`dev` at its `D` tip", the only one in the preconditions blocks and targets of the control planes at `D`. `GH1-2`'s check that `main` and `dev` kept their tips through the deletion has the same form but concerns the ref deletion `GH-1` declared it owned, the form `S1` admits | an unrelated branch; it halted `GH-1` |
| `M8` | a pinned unlanded object | `_SI3_ATTEMPT1`, read by one check that passes when the object is absent | nothing, by that check's construction |

`tools/control_plane_base_check.py` scopes its evaluation by the evaluated commit's first parent,
which is already commit-local; it is the one mechanism in the census of that form.

### `F3` — the `CV-1` status sentence is false at `D`

`verification/README.md`'s `CV-1` paragraph opens "A landed round is now also **data**:
`verification/certificates/` carries one certificate per round … and, under `attestations/`, one
record per round that has topology:". At `D` two rounds after the `CV-1` snapshot have landed
records and carry neither: `CV-2` (halted, #721) and `GH-1` (halted, #724). The universal reading is
false; the sentence is true of the `CV-1` migration snapshot.

### `F4` — tooling at `D`

No JSON Schema validator is installed in the drafting environment, and the workflow installs only
`numpy` and `scipy`. The repository's object format is `sha1`. With `-z`, `git diff-tree` emits
each path's bytes unquoted and unescaped, as `:<old_mode> <new_mode> <old_oid> <new_oid> <status>`
NUL `<path>` NUL; without it, paths are quoted according to `core.quotePath`, which is
configuration.

## The settlements, FROZEN

Each settlement below is binding on the architecture document. The document states each one as
normative text under its own identifier, `S1` to `S13`, and may add precision; it may not weaken,
omit or contradict one.

### `S1` — predicates are commit-local

A V3 predicate may take as input only: the commits `D`, `F`, the commits of `F..E`, `E`, the
withdrawal, reconciliation and receipt commits of the round, `Λ` and `LB`; the trees and blobs
those commits reach; and the round's own receipt read from a named commit. It may not take as input
the existence or tip of any branch (`main`, `dev` or any other), any remote-tracking ref,
`refs/pull/*` or a synthetic merge commit, any field of a host event payload, the working tree, the
result of a network fetch, or the time.

A mutable ref or host state may enter a predicate only when the round's control plane at `F`
declares, prospectively and by name, that the round owns it. Such a predicate is evaluated only
inside the round's execution window; no historical verdict on the round depends on it afterwards.

Locating a commit is not a predicate: a verifier may be handed `E` or `Q` by any means, but whether
the round holds is decided from the commits alone. The one step that reads the live tip of `main`
is publication (`S10`), an operation that either succeeds atomically or leaves `main` untouched;
it is never an input to the round's validity.

### `S2` — one pull request per round, anchored at `F`

A V3 round is one pull request. It begins from `D` with control-plane-only commits: the
preregistration and, before `F` exists, append-only amendments, each commit changing only files in
the round's record directory. `F` is the exact commit the owner approves and designates. Before `F`
is designated, amendments are appended; after it, no commit may change a control-plane file.
Execution begins only after the required checks have passed on exactly `F` and the owner has
designated `F`.

`F`, and not a merge commit on `main`, is the execution's ancestry anchor. `delta(D, F)` touches
only control-plane files of the round's record directory.

### `S3` — `E` is immutable

Execution starts from `F` and nothing else. Every commit of `rev-list E ^F` has exactly one parent,
and that parent is `F` or another commit of `rev-list E ^F`: no merge and no rebase absorbs later
`main` before certification. Certification fixes `E`: the required checks pass on exactly `E`, and
the owner designates `E`. Nothing after certification rewrites `F..E`; later objects only append.

### `S4` — every round has one receipt

Every V3 round, sealing or not, complete or halted, commits one final receipt, a JSON object at
`verification/receipts/<round id>.json`, in its final receipt commit `Q`. The receipt is the round's
durable state. It does not record the SHA of the commit that carries it. Its fields are frozen as
names and presence rules; the architecture document fixes each field's type and encoding and gives
one canonical example receipt for each column below.

`R` is required, `—` is forbidden, and `A` is absent with a reason listed in `absent`.

| field | content | complete | halted, execution commits exist | halted, none exist |
|---|---|---|---|---|
| `schema`, `version` | `"v3-receipt"`, `1` | `R` | `R` | `R` |
| `round` | the round id | `R` | `R` | `R` |
| `status` | `"complete"` or `"halted"` | `R` | `R` | `R` |
| `kind` | `"sealing"` or `"non-sealing"` | `R` | `R` | `R` |
| `object_format` | the repository's object format, `"sha1"` at `D` | `R` | `R` | `R` |
| `d`, `f` | the object ids of `D` and `F` | `R` | `R` | `R` |
| `control_plane_blobs` | each control-plane file with its blob at `F` | `R` | `R` | `R` |
| `governed_paths_digest` | `S7`'s digest of the set declared at `F` | `R` | `R` | `R` |
| `e`, `tree_e` | the object ids of `E` and of its tree | `R` | `A` | `A` |
| `execution_delta_digest` | `S8`'s digest of `delta(F, E)` | `R` | `A` | `A` |
| `withdrawal` | the object id of `W` | `—` | `R` | `A` |
| `candidates` | measured, uncertified heads, each with its tree and what was measured; a list, possibly empty | `R` | `R`, non-empty | `R`, empty |
| `landing` | `base` (`LB`), `object` (`Λ`), `reconciliations` (every reconciliation commit of the round, in order, at least one), `resolved_paths`, `delta_digest` (of `delta(LB, Λ)`) | `R` | `R` | `R` |
| `seal` | the seal state the round owns | `R` if sealing, `—` otherwise | `—` | `—` |
| `attestations` | the owner's designations and the check-run identities (`S5`) | `R` | `R` | `R` |
| `absent` | one reason code per `A` field, from a closed list the document fixes | `—` | `R` | `R` |

A field marked `A` is absent and listed in `absent` with its reason; a field not marked `A` never
appears in `absent`. The document's closed list of reason codes includes at least
`halted-before-certification` and `no-execution-commits`.

### `S5` — repository facts and attestations are separate

Ancestry, trees, blobs, deltas, digests and frozen subjects are **repository facts**: a verifier
re-derives every one of them from the repository alone. The owner's designation of `F` and of `E`
is a **human attestation**; check-run and workflow-run identities and their recorded conclusions are
**host attestations**. Attestations are stored in `attestations`, reported by an offline verifier as
recorded and unverified, and never treated as proved because an identifier parses. What the offline
verifier proves is that the subjects the receipt records exist, have the recorded trees, blobs and
deltas, and stand in the recorded ancestry.

The checks on the final receipt commit `Q` cannot be recorded in the receipt `Q` carries; they are
host state outside the receipt.

### `S6` — historical assertions are evaluated at their named subject

Every assertion names its subject: `D`, `F`, `E`, `W`, a reconciliation commit, `Λ`, `LB` or `Q`.
It is reconstructed from that commit's objects and never from the tree a verifier runs on. An
assertion that a tool produced an outcome at a subject is a host attestation (`S5`); a verifier may
reproduce it only by running the tool on the subject's own tree in isolation, and never by running
the current tool over the current tree. This excludes `F2`'s `M5` by construction.

### `S7` — the governed-path set is declared at `F`, in two classes, canonical and hashed

The control plane declares every path the round may change in one fenced block with info string
`v3-governed-paths`. Each non-blank line not starting with `#` is `<class> <ops> <path>`:

- `<class>` is `execution` or `record`. **Record paths** carry the round's own record: its record
  directory, which holds the preregistration, amendments and result note; its receipt path; and, for
  a sealing round, the seal records its receipt names. **Execution paths** are everything else the
  round may change. The record class must contain the round's record directory and its receipt path.
- `<ops>` is a non-empty subset of `A`, `M`, `D`, written in that order.
- `<path>` is a repository-relative path, or a directory prefix ending in `/`. It may not be empty,
  contain CR, LF or TAB, start with `/`, contain `//`, or have a `.` or `..` segment, and no path may
  appear twice across both classes.

A block that violates any of these is invalid.

The canonical bytes are the fields `v3-governed-paths` and `v1`, then, for each entry in ascending
order of the bytes of `<path>`, the fields `<class>`, `<ops>` and `<path>`; every field is its UTF-8
bytes followed by one NUL byte (0x00), and nothing else is emitted. The digest is the SHA-256 of
those bytes as 64 lowercase hex digits.

A changed path is governed by the entry of greatest length that equals it or is a directory prefix
of it; the change is authorized when its status letter is in that entry's `<ops>`. A path no entry
governs is unauthorized, which includes every path the text block cannot express. The set in force
is the set at `F`, re-derived from `F` by the verifier; no later policy redefines it.

### `S8` — deltas are canonical

For commits `X` and `Y`, `delta(X, Y)` is parsed from
`git diff-tree -r --raw --no-renames --no-abbrev -z X Y`, in which no path is quoted or escaped:
each record is `:<old_mode> <new_mode> <old_oid> <new_oid> <status>` followed by NUL, then the path
bytes followed by NUL. The canonical bytes are the fields `v3-delta`, `v1` and the object format
name (`sha1` at `D`), then, for each record in ascending order of the path bytes, the fields
`<status>`, `<path>`, `<old_mode>`, `<old_oid>`, `<new_mode>`, `<new_oid>`, every field followed by
one NUL byte, and nothing else. `<status>` is one of `A`, `D`, `M`, `T`; modes are six octal digits;
object ids are lowercase hex of the width the object format fixes, with the mode `000000` and an
all-zero id on the absent side. A delta carrying any other status, or a path twice, is invalid. The
digest is the SHA-256 of the canonical bytes as 64 lowercase hex digits.

The round's deltas are `delta(D, F)` (control plane), `delta(F, E)` (execution), `delta(LB, Λ)`
(landing) and `delta(Λ, Q)` (receipt), each between fixed commits the receipt records or that are
derived from them, and never between a commit and the current tip of `main`.

### `S9` — reconciliation happens on the pull request, after `E`

Later `main` enters the round only through reconciliation commits appended to the pull request's
branch after `E` (or after `W`, `S12`). Each reconciliation `Rᵢ` is a merge whose **first parent is
the tip of `main` when it is built** and whose second parent is the round's branch head before it:
`E` (or `W`) for the first, the previous receipt commit for each later one. The first reconciliation
is always built, with `--no-ff` when `main` has not moved since `D`. `E` and every earlier commit are
unchanged by reconciliation. `Λ` is the last reconciliation and `LB` is its first parent.

With `Δ = delta(LB, Λ)`, the landing is authorized when:

1. every path of `Δ` is governed, and its change authorized, under `S7`;
2. for every path of `Δ` other than the receipt path, its blob at `Λ` equals its blob at `E`,
   unless the path is listed in `landing.resolved_paths`, each of which is governed;
3. every path of `delta(D, E)` either appears in `Δ` with its blob at `E`, has at `LB` the same
   blob as at `E`, or is listed in `landing.resolved_paths`.

For a halted round `S12` replaces conditions 2 and 3. No branch name and no live ref enters these
conditions.

### `S10` — publication is a fast-forward to `Q`, and nothing else

`Q` is a single-parent child of `Λ`, and `delta(Λ, Q)` is exactly the receipt path, plus the seal
records a sealing receipt names. The required checks pass on exactly `Q`. Publication is a non-force
update of `main` from `LB` to `Q`: a fast-forward, because `Q` descends from `LB` through `Λ`'s first
parent. After publication the tip of `main` is `Q`; there is no publication commit distinct from `Q`.

If `main` has moved past `LB` when publication is attempted, the non-force update fails atomically
and `main` is untouched. The round then appends a further reconciliation, whose first parent is the
new tip of `main` and whose second parent is `Q`, and a new final receipt commit on it; reruns the
required checks on the new `Q`; and retries. `F`, `E` and every earlier commit stay as they are.

A `main` that reaches the round's commits through any commit other than `Q` itself — a merge
created on the host, a squash or a rebase — is not a publication of the round.

### `S11` — sealing is receipt state, not topology

Sealing and non-sealing rounds use the same lifecycle, commits and receipt position. A sealing
receipt carries `seal`, and `Q` publishes the seal state it owns; a non-sealing receipt carries no
`seal` and `Q` publishes none. The V3 lifecycle has no separate pin commit.

### `S12` — halted rounds are first-class

A halted round publishes its receipt and its result through the same pull request, and never
manufactures an `E`: the receipt says `status: halted`, `e`, `tree_e` and
`execution_delta_digest` are absent with their reason, and every head that was measured but not
certified is listed in `candidates` and nowhere else.

When execution commits exist, the round appends a withdrawal commit `W` to the last of them. A
path's **state** at a commit is either its mode and object id there, or its absence there. The
withdrawal invariant is: **for every path governed by an `execution` entry, its state at `W` equals
its state at `F`** — if the path is present at `F`, it is present at `W` with the identical mode and
object id; if it is absent at `F`, it is absent at `W`. A file created during execution is therefore
removed by `W`. `record` paths keep their content, so the result note survives. Reconciliation (`S9`, with `W`
in place of `E`) and publication (`S10`) then proceed as for a complete round. The halted landing is
authorized when every path of `delta(LB, Λ)` is a `record` path and its change is authorized.

The semantics, stated exactly:

- the halted execution's effects do not survive in the published tree: no `execution` path differs
  between `LB` and `Λ`;
- the execution commits do remain reachable from `main`, through `W`, as historical evidence;
- the receipt names them only as `candidates`, never as `E`.

### `S13` — no migration in `V3-1`

`V3-1` changes no `V1` or `V2` state and does not specify their migration, which later rounds own.
`CV-2`'s unfinished retirement stays as it is.

## The status correction, FROZEN as text

At `E`, in `verification/README.md`'s `CV-1` paragraph, the text from "A landed round is now also
**data**:" through "one record per round that has topology:", both located with whitespace
normalized, is replaced, reflowed to the paragraph's width, by

> `verification/certificates/` carries the `CV-1` migration snapshot: one certificate for each
> round represented in that snapshot, fifty-one translated from the guard's blocks and the seal
> manifest, plus `CV-1`'s own bootstrap certificate, issued by the `V1` guard that certifies the
> round and never by the verifier it installs; and, under `attestations/`, one record for each
> round in that snapshot that has topology:

and nothing else in the paragraph changes: whitespace-normalized, the paragraph at `E` equals the
paragraph at `B` with exactly that substitution. The text describes the snapshot and makes no claim
about any later round, V3 rounds included.

## The execution objects, FROZEN as a specification

- **`verification/infrastructure/v3/architecture.md`**, the specification. It carries:
  - the invariant at its head, verbatim;
  - one section per settlement `S1` to `S13`, headed with the identifier;
  - a traceability table mapping each settlement to its section;
  - the lifecycle as a state list, with the predicate that admits each transition, each predicate
    with an explicit list of its inputs;
  - the receipt: a field table giving, for every field of `S4`, its type and encoding, its subject,
    and its rule in each status column of `S4` (required, forbidden or absent with a reason); the
    closed list of `absent` reason codes;
  - worked examples of `S7` and `S8` (below);
  - four canonical example receipts, one per `S4` column and one sealing: complete non-sealing,
    complete sealing, halted with execution commits, halted without.
- **The worked examples.** For `S8`: at least three pairs of commits reachable from `D` whose deltas
  together carry the statuses `A`, `M` and `D`, each with its canonical bytes (as hex) and digest.
  The bytes are derived twice: once by parsing `git diff-tree -r --raw --no-renames --no-abbrev -z`
  as `S8` prescribes, and once independently from `git ls-tree -r -z` of the two trees. The two must
  be byte-identical. In addition, in a scratch repository, one delta whose paths include a newline
  and non-ASCII bytes, derived both ways, with the same result under `core.quotePath` true and
  false. For `S7`: at least two sets including both classes and directory entries, one given in two
  different orders to show a single digest, and one invalid block for each rejection rule, with its
  rejection.
- **The model check**, run in scratch and not landed. A throwaway model of the `S1`–`S12` predicates
  runs over temporary repositories, scenarios `MC1`–`MC9` below. Its outcomes are recorded in the
  result note; its code enters no tracked file.
- **`verification/infrastructure/round-v3-1-architecture/result.md`**, the result note.

### The model-check scenarios, FROZEN

Each scenario has a passing case and a failing countercase. The model must return the predicted
verdict on both.

| | scenario | passing case | countercase |
|---|---|---|---|
| `MC1` | unrelated ref churn | verdicts on a completed round byte-identical before and after branches, a `dev`-like ref and remote-tracking refs are created, moved and deleted | a predicate given a branch tip as input, which the model's input check rejects as outside `S1` |
| `MC2` | base drift | `main` advances after `Q` is built; the non-force update fails and leaves `main` untouched; a further reconciliation and receipt commit are appended; the retry fast-forwards `main` to the new `Q`; `E` and every earlier commit unchanged; the receipt names the final `LB` and `Λ` and every reconciliation | a `main` that reaches the round through a host merge commit, a squash or a rebase rather than through `Q` itself, rejected as no publication; a reconciliation whose first parent is not a commit of `main`, rejected |
| `MC3` | smuggled change | reconciliation resolving a governed path listed in `resolved_paths`: accepted | a reconciliation that adds an ungoverned path, or changes a governed path's blob without listing it, rejected |
| `MC4` | rewritten execution | linear `F..E`: accepted | a merge from later `main` inside `F..E`, or an `E` that does not descend from `F`, rejected |
| `MC5` | historical subject | an assertion certified at `E` unchanged after the live tree changes what it counts | the same assertion evaluated on the live tree changes: the `CV-2` failure mode reproduced |
| `MC6` | halted round | `W` satisfies `S12`'s withdrawal invariant — every `execution` path has at `W` its state at `F`, a path added during execution being absent at `W` — and keeps the `record` paths; `delta(LB, Λ)` carries only `record` paths; the execution commits are reachable from the published `Q` | a halted receipt carrying `e`; a `W` that leaves an `execution` path's state different from its state at `F`, including a file added during execution and left present; a `W` that also removes the result note; a landing that publishes an `execution` path: each rejected |
| `MC7` | sealing unified | sealing with `seal`, non-sealing without: both accepted through the same commit positions | `seal` in a non-sealing receipt, or missing from a sealing one, rejected |
| `MC8` | freeze anchor | amendments before `F`: accepted | a control-plane change after `F`, or execution from a commit other than `F`, rejected |
| `MC9` | receipt presence | each of the four canonical example receipts accepted under its `S4` column | a field required by the column missing; a forbidden field present; an `A` field absent without a reason or present with one; an unknown reason code; `execution_delta_digest` without `e`: each rejected |

A model that cannot return the failing verdict is not a control: for `MC2`, `MC3` and `MC4` the model
is also run with the corresponding check removed, and each countercase must then pass. If a
mutated model still rejects its countercase, the scenario's verdict is void.

## The targets, FROZEN

| target | passing outcome | stop outcome |
|---|---|---|
| `V31-0` | `BASE-HOLDS` — the execution branch starts at `B`; this file's blob at `B` is the frozen one; every `B` and `D->B` row and frozen blob holds at `B` | `BASE-BROKEN` — stop before any execution object |
| `V31-1` | `ARCHITECTURE-COMPLETE` — the architecture document carries the invariant verbatim, a section headed with each of `S1` to `S13` exactly once, the traceability table, the lifecycle, the receipt definition, the worked examples and the three example receipts; on review no settlement is weakened, omitted or contradicted | `ARCHITECTURE-INCOMPLETE` — stop |
| `V31-2` | `CHRONOLOGY-COMMIT-LOCAL` — every predicate in the lifecycle lists its inputs and none is outside `S1`'s admitted set; `MC1`, `MC4` and `MC8` pass on both cases | `CHRONOLOGY-LIVE` — stop |
| `V31-3` | `RECEIPT-COMPLETE` — every `S4` field defined with type, subject and its rule in each status column, the reason codes closed; the four canonical example receipts satisfy their columns; `MC9` passes on both cases | `RECEIPT-INCOMPLETE` — stop |
| `V31-4` | `SUBJECT-BOUND` — every assertion form in the document names its subject; `MC5` passes on both cases | `SUBJECT-UNBOUND` — stop |
| `V31-5` | `DETERMINISTIC` — the `S7` and `S8` worked examples are present with the coverage frozen above; each `S8` example's two derivations are byte-identical; each `S7` rejection fires; the order-invariance example yields one digest | `NONDETERMINISTIC` — stop |
| `V31-6` | `DRIFT-TOLERANT` — `MC2` and `MC3` pass on both cases, with the mutation controls | `DRIFT-FRAGILE` — stop |
| `V31-7` | `SEALING-UNIFIED` — sealing and non-sealing share lifecycle and commit positions and differ only in `seal`; the document defines no pin commit; `MC7` passes on both cases | `SEALING-DIVERGENT` — stop |
| `V31-8` | `HALT-REPRESENTED` — both halted example receipts satisfy their columns with no `e`; the document states `S12`'s three-part semantics; `MC6` passes on both cases | `HALT-UNREPRESENTED` — stop |
| `V31-9` | `STATUS-CORRECTED` — the frozen substitution made exactly, and nothing else in the paragraph changed | `STATUS-BLOCKED` — stop |
| `V31-10` | `SPECIFICATION-ONLY` — `git diff --name-status B E` adds exactly `verification/infrastructure/v3/architecture.md` and this round's `result.md`, modifies exactly `verification/README.md`, deletes nothing; the guard at `E` gives 105 PASS and 0 FAIL with `D`'s verdict map; the verifier is authoritative OK; the release gate passes | `SCOPE-EXCEEDED` — stop |

## Predictions, with strength

| target | predicted outcome | strength | reason |
|---|---|---|---|
| `V31-0` | `BASE-HOLDS` | strong | only this file lies between `D` and `B` |
| `V31-1` | `ARCHITECTURE-COMPLETE` | strong | the settlements are fixed here |
| `V31-2` | `CHRONOLOGY-COMMIT-LOCAL` | strong | `S1` excludes `M1`, `M2`, `M3`, `M6` and `M7` as inputs |
| `V31-3` | `RECEIPT-COMPLETE` | moderate | the presence rules have many interactions, and `MC9` may expose one the table above does not settle |
| `V31-4` | `SUBJECT-BOUND` | strong | `S6` |
| `V31-5` | `DETERMINISTIC` | strong | `F4`; both derivations read the same trees |
| `V31-6` | `DRIFT-TOLERANT` | moderate | `S9`'s third condition and `S10`'s retry loop are new, and `MC2` or `MC3` may find a shape they misjudge |
| `V31-7` | `SEALING-UNIFIED` | strong | `S11` |
| `V31-8` | `HALT-REPRESENTED` | moderate | `S12`'s withdrawal is new; `MC6` may find a delta it leaves behind |
| `V31-9` | `STATUS-CORRECTED` | strong | the span is `F3`'s and the text is `GH-1`'s validated reading |
| `V31-10` | `SPECIFICATION-ONLY` | strong | the budget writes no code |

**Status rule.** The round is COMPLETE iff every target reaches its passing outcome; it is HALTED at
the first stop outcome, with the targets not reached recorded as such.

## The order is part of the contract

| stage | targets | commit | checkpoint |
|---|---|---|---|
| 0 | `V31-0` | none | branch from `B`; blob check; rows at `B` |
| 1 | `V31-1`, `V31-3`, `V31-7` | one: the architecture document without the worked examples | structure checks, receipt rules on the example receipts |
| 2 | `V31-2`, `V31-4`, `V31-5`, `V31-6`, `V31-8` | one: the worked examples added to the document | the two derivations, the model check with its mutation controls |
| 3 | `V31-9` | one: the status correction | the substitution check |
| 4 | `V31-10` | one: the result note; its commit is `E` | the closing checks at `E`, then the exact-head pull request |

A finding at stage 2 that shows a settlement inconsistent is a stop outcome for the target it bears
on. It is recorded, and the settlement is not repaired within this round.

## The mutation budget

- **Added:** `verification/infrastructure/v3/architecture.md`,
  `verification/infrastructure/round-v3-1-architecture/result.md`.
- **Modified:** `verification/README.md` (the one frozen substitution).
- **Deleted:** nothing.
- **Never written:** `AGENTS.md`, everything under `tools/`, `.github/`, `verification/lean/`,
  `verification/lean-mathlib/`, `verification/seals/`, `verification/certificates/`,
  `verification/programmes/`, `verification/audits/`, any other round's directory, `papers/` and
  `book/`. No `verification/receipts/` directory is created.

## What no outcome of this round licenses

1. Treating any settlement as operative. Until a later round activates V3, §A.37 governs every
   round, this one included.
2. Any change to `V1` or `V2` state, or any claim about their migration beyond `S13`.
3. Reading the model check as an implementation, or its pass as evidence that a future verifier is
   correct.
4. Re-opening `GH-1` or `CV-2`.

## Hazards

- **`H1` — publication on the host.** The host's merge button creates a merge commit, a squash or a
  rebase, never a fast-forward to the head, and `S10` admits none of them as publication. A V3 round
  is therefore published by a non-force push of `Q` to `main`, or by a host mechanism that performs
  exactly that update. Whether the host's branch protection permits it, and for which actor, is a
  host configuration the implementation rounds must establish; it is out of this round's scope. The
  offline verifier decides from `Q` alone whether an object is a publication of the round.
- **`H2` — a landing with conflicts.** `S9`'s `resolved_paths` exists because reconciliation can
  change a governed file's content. The list is the only place such a change is admitted, and every
  entry must be governed.
- **`H3` — halted history.** Under `S12` a halted round's execution commits become reachable from
  `main` through `W`, while their effects do not survive in the published tree. This is by design: an
  append-only single pull request cannot publish a halt record without them. `MC6` checks that no
  `execution` path differs between `LB` and `Λ`, and that the `record` paths survive `W`.
- **`H4` — model versus specification.** The model check can only confirm the settlements as the
  model reads them. Where the model and the document disagree, the document is corrected before
  stage 2's commit, or the target stops.
- **`H5` — the object format.** `S8` names the object format in its canonical bytes and takes the
  object-id width from it, and the receipt records it. This repository is `sha1`; a change of object
  format changes every digest, is a later round's concern, and cannot be mistaken for an unchanged
  delta.

## Files

### Files this round reads AND writes

`verification/README.md` (the one substitution).

### Files this round reads and MUST NOT write

The guard, `tools/certificate_verifier.py`, `tools/control_plane_base_check.py`,
`tools/control_plane_lint.py`, `tools/release_gate.py`, `.github/workflows/verify.yml`,
`AGENTS.md`, and every file `F2`'s census names.

## Preconditions

```control-plane-preconditions
d: b9388cfb5d05ac30349fe7e489c320979d9d135b
frozen-blob: verification/README.md b585d921eb85b84afb0148266848bc4f0df43270
frozen-blob: AGENTS.md a9687b39c69973d35a2ff81c257687071fd35eca
frozen-blob: verification/infrastructure/round-gh-1-ref-hygiene/result.md 3bce2b2b48a52ace2d873daf53a459e31c74638f
# row 1: name freedom, drafting-time facts
{"id": "d1-round-free", "scope": "D", "check": "git grep -l -F -e 'V3-1' -e 'v3-1' -e 'round-v3' $D", "expect": "empty"}
{"id": "d1-spec-free", "scope": "D", "check": "git grep -l -F -e 'verification/infrastructure/v3' -e 'execution_delta' -e 'landing_delta' $D", "expect": "empty"}
{"id": "d1-section-free", "scope": "D", "check": "git grep -l -F -- '§A.39' $D", "expect": "empty"}
{"id": "d1-receipts-absent", "scope": "D", "check": "git ls-tree -d --name-only $D verification/receipts", "expect": "empty"}
# row 2: the status sentence at D, whitespace-normalized
{"id": "d2-sentence-present", "scope": "D", "check": "git show $D:verification/README.md | tr '\\n' ' ' | tr -s ' ' | grep -o -F 'A landed round is now also **data**: `verification/certificates/` carries one certificate per round'", "expect": "nonempty"}
# row 3: provenance, D to B: D an ancestor, and nothing but this file between them
{"id": "db3-ancestor", "scope": "D->B", "check": "git merge-base --is-ancestor $D $REF", "expect": "exit0"}
{"id": "db3-only-this-file", "scope": "D->B", "check": "git diff --name-only $D $REF | grep -v -x -F 'verification/infrastructure/round-v3-1-architecture/preregistration.md'", "expect": "empty"}
# row 4: no execution object at B; files are read directly, never through git grep
{"id": "b4-no-spec-dir", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/v3", "expect": "empty"}
{"id": "b4-round-dir-control-plane-only", "scope": "B", "check": "git ls-tree -r --name-only $REF verification/infrastructure/round-v3-1-architecture | grep -v -x -F 'verification/infrastructure/round-v3-1-architecture/preregistration.md'", "expect": "empty"}
{"id": "b4-no-receipts", "scope": "B", "check": "git ls-tree -d --name-only $REF verification/receipts", "expect": "empty"}
{"id": "b4-sentence-uncorrected", "scope": "B", "check": "git show $REF:verification/README.md | tr '\\n' ' ' | tr -s ' ' | grep -o -F 'A landed round is now also **data**: `verification/certificates/` carries one certificate per round'", "expect": "nonempty"}
{"id": "b4-agents-no-section", "scope": "B", "check": "git show $REF:AGENTS.md | grep -F -e '§A.39'", "expect": "empty"}
# row 5: this control plane at its path
{"id": "b5-present", "scope": "B", "check": "git cat-file -e $REF:verification/infrastructure/round-v3-1-architecture/preregistration.md", "expect": "exit0"}
```

## The landing shape

Non-sealing under §A.37, `E` → `L` on the execution pull request, no `P`. `L`'s first parent is
current green `main`, its second parent exactly `E`; conflicts, if any, are resolved in `L` by
merits. Full continuous integration passes on `L` before it merges, and the push run on `main` is
green before any later round's landing is built.

## Execution discipline

The execution branch is created from `B` and nothing else, after `B`'s push run is green including
the control-plane base check in mode `B`. Its first act is the blob check of this file at `B`. It
never absorbs later `main` before `E`; no rebase, amend or force-push. Each commit-bearing stage
commits before its checkpoint. A stop outcome halts the round; the halt is recorded in a result
note with the outcomes reached, and nothing else of the execution lands.

The round's chronology is the executor's check at `E` that every commit of `git rev-list E ^B`
descends from `B` and that the branch absorbed no later `main`, recorded in the result, followed by
exact-head review. `V3-1` carries no guard clause, manifest record or round certificate (reading
`R3`).

## Points at which this freeze chose a reading, recorded rather than resolved

- **`R1` — the receipt schema as normative text.** The receipt's schema is a section of the
  architecture document, not a JSON Schema file: no validator exists at `D` (`F4`), and a schema file
  nothing validates is an unexercised artifact. The declined option is a
  `verification/infrastructure/v3/receipt.schema.json` validated only by hand.
- **`R2` — no `§A.39` text.** `V3-1` writes no `AGENTS.md` text, not even marked as not yet
  operative. The operative rule belongs to the round that activates V3, and a non-operative rule in
  the rules document invites being read as operative. The declined option is a prospective `§A.39`
  marked inoperative.
- **`R3` — no protocol-2 certificate, no guard clause.** `V3-1` adds no `V1` guard clause and writes
  no `V2` certificate or attestation, for the reasons `GH-1` recorded as its `R1` and `R2`. The
  consequence is that `V3-1`, like `CV-2` and `GH-1`, is a landed round the `CV-1` snapshot does not
  represent, which the corrected sentence states correctly.
- **`R4` — the halted landing.** `S12` publishes a halt through a withdrawal commit on the same
  pull request. The halted execution's effects do not survive in the published tree, and its commits
  do remain reachable from `main` as historical evidence (`H3`); the receipt names them only as
  `candidates`. The distinction between `execution` and `record` paths in `S7` exists so that `W` can
  undo the one without erasing the other. The declined option publishes the halt record from `F` on
  a second branch, which breaks the one-pull-request lifecycle.
- **`R5` — owner designation of `F` and `E`.** `S2` and `S3` make the owner's designation, with the
  required checks, the act that fixes `F` and certifies `E`. The designation is a human attestation
  and the checks are host attestations (`S5`); neither is something the offline verifier can prove.
  What it proves is that the recorded subjects exist and that their trees, deltas and ancestry are
  consistent with the receipt. The declined option certifies `E` by checks alone.
- **`R6` — where the specification lives.** The architecture document lives at
  `verification/infrastructure/v3/`, outside the round's directory, because later rounds build on
  it and it outlives this round's record; the round's directory holds only its preregistration and
  result, per §A.36.
