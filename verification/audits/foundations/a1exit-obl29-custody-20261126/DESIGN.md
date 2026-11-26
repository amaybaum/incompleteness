# OBL-29 custody: format, bootstrap inventory and mapping to admitted inputs (paper design c6)

## 0. Status, authority, scope and goal link

**Status.** Paper design c6, pending an owner decision on the context source (§4.2, decision D-1), independent review and adoption. The proposed
requirements (ids `R6.CUST.n`) have no force until adoption. Adoption of this design does not
discharge OBL-29, does not authorize implementing custody-dependent discharge, and changes no
schema, admission rule or release-gate step by itself (§7).

**Authority.** Owner decision (amaybaum, received 2026-11-26T19:52Z, coordinating session; recorded
at #1169 comment 7202075726), item 5, quoted:

> Authorize a bounded paper-only design and independent review of the OBL-29 custody format, bootstrap inventory and mapping to admitted inputs. Prefer existing Git objects and verification mechanisms. Bring the reviewed design for adoption before implementing custody-dependent discharge.

The decision closes: "All existing correctness, independent review, staging, freeze, trial and
landing gates remain in force."

**Revision.** c1 at `dc2b344c91c04979570ad58c5a554b3b7585008f` received REVISE from an independent
review, relayed by the coordinating session; c2 at `b61467e9efecc435798861130a5ace5e40c18a91`
received REVISE from the independent re-review posted on PR #1616 (comment 7202652276). c3 answers
findings 2 to 6 of that re-review and drafts both variants of finding 1, which awaits the owner's
decision (D-1); c3 at `ca82d23ef4b604b040660515e486fe6fdfdf1f9d` received a small REVISE (PR #1616
comment 7202781537), which c4 answers, keeping both variants; c4 at
`3658ed49f210f83f633a47cf2546ea5606b005b2` received a REVISE with two targeted fixes (PR #1616
comment 7202860517), which c5 answers; c5 at `9fe63de3402f444420ef3e6cc7c912fb28d31c82` received a
confirmatory REVISE (PR #1616 comment 7202923040), which c6 answers. §9 maps findings to changes and records each choice made where a finding offered one.

**Source requirements.** The adopted OBL-29 remedy r9: `DESIGN.md` and `CONTROLS.json` under
`verification/audits/foundations/a1exit-obl29-remedy-20261126/` at
`77a73c022091f598cf807fcf89d66c3cf43208de` (branch `design/a1-obl29-remedy-20261126`), adopted by
owner amaybaum at #1601 comment 7197486426 (2026-11-26T16:19:17Z) with the token convention
`<blob>#<item>`. Its §2.2 "Custody and lookup" states the requirements this design serves and leaves
"the custody format, bootstrap record and mapping to admitted inputs" to be fixed and independently
verified before implementation relies on them. Section numbers prefixed "r9" refer to that text;
requirement ids `R6.*` refer to it or to the Amendment 6 r13 contract at
`5ad8837521de0a26734266a64f91548fd3dcff1e` that it amends.

**Implementation reference.** PR #1577 at `e88ca375c35a278371f8bc1c70ba963ea61fef05`
(`tools/a1-ledger-coverage-r6`): `tools/ledger_coverage/engine/obl29.py` (the predicates of r9 §2.2
over explicit witnesses, not yet called by a run) and `engine/category3.py`, whose
`reassessment_problems` appends `custody_unverified` to every cited discharge, so every cited
discharge fails closed. This design states what replaces that unconditional failure; it changes no
code.

**Goal link (AGENTS.md §A.47).** Serves A1 retirement (#1169) through its blocker OBL-29 (#1598):
it would decide whether the custody that r9 §2.2 requires can be stated as a checkable record built
from existing Git objects, and which parts remain review. A finding that some part cannot be made
mechanical is an equally valid result; §6 records where that is so.

**Scope.** The custody record of r9 §2.2: its schema and location, the bootstrap inventory, the
successor rule, the mapping of r9's historical inputs to admitted inputs and Git objects, the
fail-closed rules, the split between mechanical checks and review, and preregistered controls
(`CONTROLS.json`). Outside scope: route 2 adjudication (r9 §5.6, a separate design), the squash and
rebase gap (r9 §6, R-1), and any change to the witness predicates of r9 §2.2.

***

## 1. What custody has to establish

r9 computes a run's findings over `R*`, every tree reachable through any parent from the run's roots
(R6.OBL29.1, .7). That set is monotone under ancestry extension (r9 §2.3) and needs no custody. What
`R*` does not carry is **which discharge checks were operative, and under which inputs**. r9 §2.2
retains a witness only where "R6.OBL29.3 qualifies it for an existing discharge check", qualified
"under the configuration and admitted lineage inputs under which [it] is found", including "the exact
`M`/source tree" and, where qualification depends on it, "the exact `REV` and its admission
evidence"; and "the existence of an eligible pair in history alone gives no witness for a frozen
discharge that never made the lineage check operative". A later run's own inputs "cannot serve as the
list of negative witnesses". Custody supplies that list and lets a run show it is complete.

**Discharge-bearing.** A configuration is discharge-bearing when it is a regular file (mode `100644`
or `100755`) of schema `oi-retirement-config/1` whose `admission.mode` is `"chain"` and whose
`records` (R6.CFG.4) include at least one reference of kind `reassessment`. A **discharge-bearing
context** is a freeze that admits such a configuration under R6.CUST.5 (c1), whose wording depends
on decision D-1 (§4.2). Only such a freeze can
make a reassessment discharge operative under an authorized freeze (R6.RECON.27), and so only it can
qualify a witness. Harness-admitted runs have no freeze (R6.RECON.21) and form no context (OQ-10).
The no-edit route of R6.RECON.26 uses no repair and no custody (R6.CUST.7).

**Drafting measurement.** At `origin/main` `84e927b9b7c2bcc8cb9624cb036167dae233e408` (6,076
commits by all-parent ancestry) no discharge-bearing configuration and no receipt of a
discharge-bearing freeze is reachable from `main`: no blob that ever stood under
`verification/audits/` has schema `oi-reassessment/1`, `oi-reconciliation/2` or
`oi-review-record/1`, and the nine `oi-retirement-config/1` blobs (all at
`verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json`) cite
no record of kind `reassessment`. The independent review of c1 confirmed this measurement by its own
method. It is a drafting fact; the bootstrap re-establishes it at `B0` (§3).

***

## 2. The custody record

### 2.1 Location

**R6.CUST.1 Location.** The custody record is the regular file (mode `100644` or `100755`) at the
single path `verification/audits/foundations/a1exit-obl29-custody/custody.json`. The path, and the
git blob id of the bootstrap version (§3), are constants of `tools/ledger_coverage/record_authority.py`,
the tool file that already holds the admitted record directories (R6.A1CFG.1). That file is listed in
`tool.files` and pinned at `F` (R6.REC.18), so neither constant can be changed by a configuration, a
record or an argument; changing either is a tool revision. The directory is not a reconciliation
directory (R6.RECON.1), not a plan record directory, and lies outside every tool-landing prefix. The
run reads the record from the tree of effective `M` and its versions from every tree reachable from
`M` (R6.CUST.4), through the verified reader (R6.REC.17).

A custody successor, or a review record of one, that lands on `M` after `F` is a side change of the
run (R6.TREE.5): the configuration's side-change class record must classify the custody directory, or
the run reports REVIEW_REQUIRED `side-change-unclassified` as for any other path (control CU-N24).
This is an existing mechanism and needs no new rule.

### 2.2 Schema

**R6.CUST.2 Schema `oi-obl29-custody/1`.** The file's bytes are exactly the canonical JSON
(R6.RECON.29) of one object, with no trailing newline, and pass strict parsing (R6.RECON.29). The
object has exactly these keys:

| Key | Type | Meaning |
|---|---|---|
| `schema` | `"oi-obl29-custody/1"` | |
| `predecessor` | blob id or null | the git blob id of the version this one extends; null only for the bootstrap version |
| `author` | identity string (R6.RECON.29) | the writer of this version, for review independence (R6.CUST.8) |
| `entries` | array of entry objects, at least one | the append-only inventory |

Each entry has a `type` and exactly the keys its row lists:

| `type` | Further keys | Meaning |
|---|---|---|
| `"bootstrap"` | `base`: commit id | the inventory starts at `base` (§3). Exactly one, and it is `entries[0]` |
| `"freeze"` (variant (ii) of D-1 only) | `f`: commit id; `config`: reference; `landing`: commit id | a reviewed statement that `f` is an owner-designated freeze of the discharge-bearing configuration `config`, landed on `main` by the merge `landing` |
| `"close"` | `f`: commit id; `runs`: array of `{m, rev}`, `m` a commit id, `rev` a commit id or null | a reviewed statement that the authorized op C runs of the freeze `f` (R6.CUST.5 (c3)) are exactly these, each with its exact `M` and the record commit `REV` it admitted, if any (R6.RECON.2 (c)); an empty `runs` states that the freeze made no authorized run |
| `"unfrozen"` | `config`: reference | an acknowledgement that a discharge-bearing configuration in `R*` was not frozen when the entry was written; a later freeze of the same configuration makes it a context without contradicting the entry |
| `"void"` | `blob`: blob id | a version of the custody path in `Vers(M)` that fails R6.CUST.2, acknowledged as carrying nothing custody must retain |

Commit id, blob id, reference and identity string are the encodings of R6.RECON.29. There is no other
key and no free-text field. A key, entry type or value outside these tables is a schema failure. No
entry clears, adjudicates, accepts or withdraws anything: an entry type that would is not in the
table.

**Why these entries.** Under variant (i) of D-1, discharge-bearing freezes are derived from V3
receipts and are not listed, because a list in bijection with receipts would repeat Git; under
variant (ii) no structured Git record of a retirement freeze exists, so a reviewed `freeze` entry
supplies it. What Git cannot express in either variant is: where the inventory starts (`bootstrap`), which runs each freeze actually made and with which
`M` and `REV` (`close`), that a discharge-bearing configuration on `main` was never frozen
(`unfrozen`), and that a malformed version of the record is acknowledged (`void`). Several `close`
entries may name the same `f`; their `runs` are united, so an omitted run is added by a further
`close`.

**Detection.** The custody record's schema is not a reconciliation or review schema, so category-3
detection keeps no finding from it. No key or literal value of the schema contains an invalidation
token, so it can meet the class (b) or (c) heuristics only through a path value copied from a record
path (r9 R-3). Review records of custody versions (R6.CUST.8) are ordinary `oi-review-record/1`
files in `R*`: detection treats them as it treats every review record (R6.OBL29.2, .3). An accepting
custody review carries no finding. A custody review whose verdicts carry `invalidates` or
`invalidated` names no reconciliation record entry, so its items are not items of one; it counts as a
finding only through R6.RECON.26's Form (i) clause that "a review whose `reviewed` names no record
the scan finds, so that its independence cannot be established, counts, as a form failure". It then
binds as any form-failed finding does; that is the fail-closed outcome. Control CU-B4 covers both.

### 2.3 Size

One `close` entry is under 120 bytes plus about 100 bytes per run. The record carries no witness,
review, record content, verdict or list of freezes.

***

## 3. The bootstrap inventory

**R6.CUST.3 Bootstrap.** The bootstrap version is the version whose git blob id equals the constant
of R6.CUST.1. Its `predecessor` is null, its `entries[0]` is `{"base": B0, "type": "bootstrap"}`, and
its remaining entries are the output of the builder below at `B0`. `B0` is a commit on `main`
designated in the owner decision that adopts the implementing tool revision (OQ-11).

**What it lists.** An `unfrozen` entry for every discharge-bearing configuration in `R*(B0)` that no
discharge-bearing context reachable from `B0` admits, a `close` entry for every discharge-bearing
context reachable from `B0`, and, under variant (ii) of D-1, a `freeze` entry for each such context. On the drafting measurement both sets are empty, and
the bootstrap version would be the canonical JSON of

    {"author": <writer>, "entries": [{"base": B0, "type": "bootstrap"}], "predecessor": null,
     "schema": "oi-obl29-custody/1"}

**Deterministic builder (specification).** Inputs: `B0`, read through the verified reader, and the
writer's identity string for `author`; the output depends on nothing else.
1. Walk every commit reachable from `B0` through any parent (R6.OBL29.7). Collect every regular entry
   (mode `100644` or `100755`) under `verification/audits/` that is a discharge-bearing configuration
   (§1), and every regular entry `verification/receipts/<name>.json` with schema `v3-receipt`.
2. Derive the discharge-bearing contexts by R6.CUST.5 (c1): under variant (i), from the receipts;
   under variant (ii), none is derivable, and every discharge-bearing configuration of step 1 is a
   candidate for a reviewed `freeze` or `unfrozen` entry.
3. For each discharge-bearing configuration of step 1 that no context of step 2 admits, emit
   `{"config": ref, "type": "unfrozen"}` as a candidate.
4. If step 2 finds any context, or under variant (ii) step 1 finds any discharge-bearing
   configuration, stop: its `close` entry needs the runs, which the builder cannot
   discover, and the bootstrap then needs the review of §5 item 2 before it is pinned. Otherwise emit
   `bootstrap` first, then the `unfrozen` candidates sorted by `(config.path, config.blob_sha256)`,
   in canonical JSON.

**Independent verification of the bootstrap.** Before the blob id is pinned:
- (a) a non-author reviewer re-runs the builder at `B0` and obtains the same bytes;
- (b) the reviewer confirms the two sets of step 1 and step 2 by a method that shares no code with the
  builder, for example `git rev-list --objects B0` filtered to `verification/audits/` and
  `verification/receipts/` with a separate JSON parse of every blob;
- (c) the reviewer checks the owner's recorded designations of `F` for retirement rounds up to `B0`
  against the receipts reachable from `B0` (variant (i)) or the `freeze` entries (variant (ii)),
  records that no designated discharge-bearing freeze is missing, and confirms each `unfrozen`
  candidate;
- (d) the tool revision that adds the pin is independently reviewed under the existing tool-revision
  route (R6.REC.18).

Items (a), (b) and (d) are reproducible from `main`; item (c) is review. Every later run and every
gate check re-applies the mechanical rules of R6.CUST.4 and R6.CUST.5 at its own commit, which covers
everything reachable from `B0`.

***

## 4. Successor binding, completeness and the mapping

### 4.1 Successor binding

**R6.CUST.4 Successor rule.** Let `V_M` be the custody record in the tree of effective `M`. Let
`Vers(M)` be every distinct blob that stands at the custody path at a regular mode (`100644` or
`100755`) in any tree reachable from `M` through any parent (the walk of R6.OBL29.7, with the custody
path added to its fixed selection; removing or rewriting the file on a later commit removes nothing
from `Vers(M)`). A version is *well-formed* when it meets R6.CUST.2.
- (s1) **Chain.** Starting at `V_M` and following `predecessor`, every named blob is in `Vers(M)` and
  well-formed, no blob repeats, and the chain ends at the bootstrap blob of R6.CUST.1. A cycle, or a
  predecessor-null version other than the bootstrap, breaks the chain.
- (s2) **Prefix.** For each version `V` on the chain with predecessor `P`, `P.entries` equals the
  first `len(P.entries)` elements of `V.entries` element for element, and `V` adds at least one entry.
- (s3) **Inclusion.** For every well-formed version in `Vers(M)`, on the chain or not, and whatever its
  own predecessor, every entry other than its `bootstrap` entry is an entry of `V_M`. A fork is
  resolved by a successor that names one side as `predecessor` and appends the other side's entries; a
  revert, a merge keeping one side's file, or a new bootstrap pinned by a later tool revision cannot
  drop an entry, because every earlier well-formed version stays in `Vers(M)`.
- (s4) **Malformed versions.** Every version in `Vers(M)` that is not well-formed is named by a `void`
  entry of `V_M`; every `void` entry names a blob in `Vers(M)` that is not well-formed.
- (s5) **Duplicates.** No two entries of `V_M` are equal.

The predecessor binding is by git blob id, so a successor binds the exact bytes of its predecessor,
which is itself a Git object reachable from `M`. The record does not repeat the history of the path:
`Vers(M)` is read from Git, and the record adds only which version extends which.

**Liveness.** An entry, once in a well-formed version on `main`, can never be removed (s2, s3). An
entry that fails a mechanical check of R6.CUST.5 therefore keeps custody unestablished for every
later run. The release-gate check of R6.CUST.10 refuses such an entry before it lands. If one lands
anyway (the gate bypassed or changed), custody stays unestablished and every cited discharge stays
inapplicable; this design gives no recovery route (OQ-15). A `close` entry that is mechanically
valid but lists a run that did not happen only adds witnesses, and an omitted run is added by a
further `close`.

### 4.2 Contexts and completeness

**R6.CUST.5 Completeness.** At effective `M`:
- (c1) **Contexts. This clause depends on decision D-1; exactly one variant is adopted.**

  *Variant (i): native V3 rounds only.* Every discharge-bearing freeze is the `F` of a native V3
  round (AGENTS.md §A.39). The receipts are the regular entries `verification/receipts/<name>.json`
  with schema `v3-receipt` in any tree reachable from `M`, read by the walk of R6.OBL29.7 with that
  prefix added to its fixed selection, so deletion removes nothing. For a receipt with freeze commit
  `f` (its key `f`), let `R` be the directory of the member of its `control_plane_blobs` whose path
  ends in `/preregistration.md` (the round's record directory, V3 `K1`). Every member of
  `control_plane_blobs` must stand in `f`'s tree at its path, at a regular mode, with its listed git
  blob id; a member that is absent there, or present with another blob or mode, is a custody failure
  (`custody-receipt-mismatch`). A configuration is admitted from the receipt when it and the
  `PREREG.md` beside it (R6.CFG.1) lie under `R` in `f`'s tree and that `PREREG.md`'s last `Record
  pins` subsection lists the configuration's SHA-256. Each admitted configuration that is
  discharge-bearing makes `(f, config)` a discharge-bearing context; a configuration elsewhere in `f`'s
  tree, including one that an unrelated receipt's `f` happens to contain, is not admitted from that
  receipt. The receipts' validity is decided by `tools/v3_verifier.py --receipts` in the release gate,
  not by this tool. *Realizability:* V3 `S2` lets `delta(D, F)` touch only `R/preregistration.md` and
  files under `R/amendments/`, so the configuration and its `PREREG.md` stand in `f`'s tree under `R`
  only if they were already under `R` at `D` or lie under `R/amendments/`; and R6.A1CFG.1 admits
  configurations only from its fixed record directories. Adopting variant (i) therefore also needs a
  plan layout in which the A1 record directory and the V3 record directory agree (OQ-18). The A1
  retirement plan of `a1exit-r6-20261120` is not a native V3 round and has no receipt.

  *Variant (ii): reviewed `freeze` entries.* The discharge-bearing contexts are the `freeze` entries.
  For each, `f`'s tree holds `config` at its path at a regular mode, the configuration is
  discharge-bearing and is admitted by R6.CFG.1–.2 at `f` (the `PREREG.md` beside it lists its
  SHA-256), and `landing` is the merge that landed `f`: a commit on `M`'s first-parent chain with at
  least two parents, whose first parent is not a descendant-or-self of `f`, and one of whose other parents is a
  descendant-or-self of `f`. `landing = f`, a commit off `M`'s first-parent chain,
  or a descendant of `f` that is not that merge, fails (`custody-unsupported`). A later foxtrot
  fast-forward that took the landing merge off the first-parent chain would make the entry fail at
  every later `M`; that is fail-closed and is a liveness hazard of variant (ii) (R-C4). Whether the entries list every owner-designated
  freeze of a discharge-bearing configuration is review (§5 item 1); the owner's designations are
  GitHub comments, not structured Git data, and the R6.CUST.8 review records which designations
  were compared.
- (c2) **Closing statements.** Every discharge-bearing context has at least one `close` entry naming
  its `f`, and every `close` entry names the `f` of a discharge-bearing context. Until a context has a
  `close` entry, custody is not established. A `close` is written after the context's landing: every
  commit reachable from `M` whose custody version contains a `close` entry for `f` has the context's
  landing commit as an ancestor (variant (i): the receipt's `landing.object`; variant (ii): the
  `freeze` entry's `landing`).
- (c3) **Runs.** The runs of a context are its *authorized op C runs*: the op C execution runs under
  the frozen configuration with `F = f`, made between the designation of `f` and the context's
  landing (R6.EVID.7 kind 4). No run under `f` after the landing is authorized, and a run whose own
  `F` is the `f` of a closed context fails custody (R6.CUST.7). Mechanically, in every `close` entry
  each `m` is reachable from `M`, and each non-null `rev` has the shape of R6.RECON.2 (c): exactly one
  parent, equal to its run's `m`, and a tree equal to that parent's except for regular files added
  inside reconciliation directories, at least one an `oi-reconciliation/2` record naming `m` as its
  `M`.

  *Run results.* A run result of context `f` is a regular file named `result.json` anywhere under
  `<dir>/op-c-runs/` in the landing commit's tree, where `<dir>` is the directory of the context's
  configuration, that strict-parses with schema `oi-ledger-coverage/5` (R6.OUT.11) and records, in
  fields the tool at `e88ca375` emits: top-level `operation` equal to `"execution"`; `config.commit`
  equal to `f` (in a chain run the tool refuses unless the configuration's commit equals `--freeze`);
  `config.blob_sha256` equal to the configuration's SHA-256; `config.admission.mode` equal to
  `"chain"`; and no `harness` field. A result whose `outcome` is USAGE, ERROR, VOID or INTERNAL did
  not evaluate and is not a run; it is ignored by the equality below. The run's `REV` is the common
  `rev` of the admitted classify records, the members of `inputs.classify_records` (R6.RECON.2 (c)
  requires one `REV` per run; refused records become items, not members), or null when none was
  admitted. A run whose named `REV` admitted no record made no check operative through it, so null is
  its correct `REV` for r9. The run's `M` must come from a named result field that a
  verdict may read: `roles.M` is a declared diagnostic that R6.OUT forbids a verdict to read, so the
  check depends on either adopting `roles.M` as a named field or emitting `inputs.main` under OBL-28
  C-24. That is an r6 and tool change that the owner adopts with this design (OQ-19); until it is
  made, the run results cannot supply `M`: the equality below cannot be computed, and the completeness
  and attribution of `runs` rest on the R6.CUST.8 review whichever form OQ-17 fixes, while the
  conditions of this paragraph and the `REV`s of evaluating results (each must equal the `rev` of a
  listed run of `f`) are still checked. A `result.json`
  under that directory that fails these conditions, other than by a non-evaluating outcome, is a
  custody failure (`custody-runs-mismatch`). The location `op-c-runs/` is
  this design's proposal (OQ-17). The check takes one of two forms, fixed by OQ-17:
  - *OQ-17 adopted (recommended).* Every discharge-bearing round lands its run results. The union of
    the `close` runs for `f` equals, as a set of `(m, rev)`, the runs of its results: a listed run
    without a result (missing results included), a result without a listed run, and a run filed under
    another context's `close` all fail (`custody-runs-mismatch`). An empty `runs` with no results is
    consistent, and whether the freeze truly made no run rests on the R6.CUST.8 review (R-C2).
  - *OQ-17 not adopted.* Where the landing tree holds run results for `f`, the same equality is
    checked; where it holds none, the completeness and attribution of `runs`, including an empty
    `runs`, rest on the R6.CUST.8 review (§5 item 2, R-C2).
- (c4) **Configurations.** Every discharge-bearing configuration in `R*(M)` is admitted by some
  discharge-bearing context or named by an `unfrozen` entry, and every `unfrozen` entry names a
  discharge-bearing configuration in `R*(M)`. An `unfrozen` entry whose configuration a later context
  admits is not a failure: it only acknowledges, and the context then needs its own `close` (c2).
  **Pin rule.** A *pinning commit* of a discharge-bearing configuration is a commit reachable from
  `M` whose tree lists the configuration's SHA-256 in the last `Record pins` subsection of the
  `PREREG.md` beside it, while none of its parents' trees does (the commit that introduces the pin,
  on a branch or in a merge resolution; a root commit that lists it is one). A later merge of a branch
  forked before the pin has one parent that lists the pin, so it is not a pinning commit. An `unfrozen` entry covers such a
  configuration only when every commit reachable from `M` whose custody version contains that entry
  descends from every pinning commit; the pin remaining present at later commits, `M` included, does
  not by itself defeat a cover written after the pin was introduced. Otherwise the configuration must
  be admitted by a context: under variant (i) a receipt, under variant (ii) a `freeze` entry. An acknowledgement written before
  a configuration was pinned for a freeze therefore cannot stand in for that freeze, and a writer who
  asserts `unfrozen` after the pin does so knowingly, under the R6.CUST.8 review. An `unfrozen` entry
  is `{config, type}`, so re-asserting it after a pin gives an entry equal to the existing one, which
  (s3) keeps and (s5) forbids repeating, and the stale version stays in `Vers(M)`. A stale `unfrozen`
  entry is therefore recovered only by a context (a receipt under variant (i), a `freeze` entry under
  variant (ii)), where the configuration was in fact frozen. A configuration that was pinned but never
  frozen, and whose `unfrozen` entry predates the pin, has no recovery: custody stays unestablished at
  every later `M` (R-C4; OQ-20).
- (c5) **Reachability.** Every commit an entry names (`base`, `f`, `landing`, `m`, `rev`) is
  reachable from `M` through any parent.

### 4.3 Mapping from r9's historical inputs to admitted inputs and Git objects

**R6.CUST.6 Replay.** For each discharge-bearing context `(f, config)` and each run `(m, rev)` in the
union of its `close` entries, the run re-establishes that run's operative discharge checks and
qualifies their witnesses under R6.OBL29.3 exactly as a run with roots `m`, `f` and `rev` would have,
with these inputs and no others:

| r9 §2.2 input (a retained witness "names" or custody "preserves") | Source in this design | Admission and verification in the replay |
|---|---|---|
| the original configuration, by exact reference | (c1): derived from the receipt (variant (i)) or the `freeze` entry (variant (ii)) | admitted from `f` as in (c1) and by R6.CFG.1–.2; a failure is a custody failure (R6.CUST.9) |
| the original freeze, by verified commit | the receipt's or the `freeze` entry's `f` | (c1) and (c5); read through the verified reader |
| the applicable mode | the configuration's `admission.mode` | `chain` by definition (§1) |
| the original selector | the side-change class record named by `roles.side_change_classes` | resolved from anchor `f` (R6.RECON.33); its prefixes and pins apply to that context only |
| the proposed reassessment | each `records` member of kind `reassessment` | resolved from anchor `f` (R6.RECON.33) and linted as at that freeze |
| the original finding reference and `item` | the reassessment's `finding` | looked up in `R*(m)` (R6.OBL29.3) |
| the exact repair record and entry path; the repair commits | the reassessment's `repair.entry` and `repair.commits` | the record by exact reference; the repair entry in the scanned set of `m` (R6.OBL29.4) |
| the exact operative edge `U → P` | derived | R6.REC.7 for the repair record under the context's admission route and anchor (`f`, or `rev` for a record that `REV` admitted) |
| the exact adverse review or competing successor `S` | derived | R6.OBL29.3 qualification over `R*(m)` (and `rev`'s tree), with the context's selector |
| the exact `M`/source tree | the run's `m` | every `M`-dependent condition is evaluated at `m`: the first-parent chain of `m` for the repair commits (R6.RECON.27), R6.RECON.2 (b) for `rev`, the R6.RECON.26 applicability test, and the scanned set at `m` |
| the exact `REV` and its admission evidence | the run's `rev` | R6.RECON.2 (a)–(g) replayed with that `REV`, `m` and the context's configuration |
| full Git objects | none copied | every object reachable from `M`, read and hash-checked by the verified reader |
| authorization provenance | the receipt (variant (i)); the reviewed `freeze` entry and its R6.CUST.8 review (variant (ii)) | owner designations are provenance (AGENTS.md §A.42 item 2); the tool does not read them (R6.STAT.4) |
| reviews, corrections and later dispositions | `R*` and later contexts | every review in `R*(m)` qualifies witnesses for that run; a correction is evaluated only for the current run's candidate discharge `D` by r9's `decide`; no adjudication route exists (r9 §5.6), so `Adjudicated(W)` is false |
| original bytes, paths and lineage | none copied | exact references resolve in `R*`; lineage resolves under R6.RECON.33 from the context's anchor |

Replaying at each run's exact `m` reproduces r9's qualification: `R*(m)` is what that run's scan read
(r9 §2.3), and the positive-route conditions that depend on `M` hold at `m` exactly when they held for
the run. A replay at a later `M` could fail them, for example after a foxtrot fast-forward moves a
repair commit off the first-parent chain (r9 P-FOXTROT, N-FOXTROT-SIDE-COMMIT), and so lose a witness;
control CU-N20 pins this.

The witnesses of every replayed run, with the current run's own live witnesses, are the set over which
r9's `blocked(D, W)` is evaluated for each candidate discharge `D`. **Custody only adds witnesses.**
No replayed context is an admission of the current freeze: it cannot supply NR-2's admission of a
replacement `R`, a positive review, a lineage anchor or any other positive input, and it never clears
a witness. Clearance is decided only by r9's `Cleared(D, W)` over the current freeze's own admitted
records. A witness is identified by its context `f`, its run `m`, its kind and the exact references
r9 §2.2 lists, and is reported in the result (OQ-12). The replay applies the rules of the tool
revision pinned at the current `F` (OQ-3).

`Inapplicable(W)` is defined in r9 as failure of `W`'s original qualification to reproduce from
retained custody. Here every witness is obtained by reproduction from immutable objects, so a witness
that does not reproduce is not in the set and no recorded witness exists to be reported as
inapplicable. A witness can stop reproducing only through a tool revision that narrows the predicates
(r9 P-4, R6.STAT.5).

### 4.4 What custody gates

**R6.CUST.7 Gate on discharge.** Custody is established at effective `M` exactly when R6.CUST.2,
R6.CUST.4, R6.CUST.5 and R6.CUST.8 hold and every run of every context replays (R6.CUST.6) without a
custody failure, and the run's own `F` is not the `f` of a context that has a `close` entry (c3; a
run after the close is not authorized). Before a run returns an applying reassessment discharge,
custody must be established; the check replaces `custody_unverified` in `reassessment_problems`. The R6.RECON.26
route by which a configuration carries no edit the finding binds needs no repair and no custody and is
unaffected (OQ-13).

**R6.CUST.8 Review evidence (a condition of the `close` design).** Every well-formed version in `Vers(M)` that chains to
the bootstrap and adds entries relative to its predecessor has, in the custody directory, an
`oi-review-record/1` whose `reviewed` is that version's exact `{path, blob_sha256}`, whose `reviewer`
differs as an identity string from the version's `author`, and which accepts every item, the items
being `entry:<i>` for each index `i` the version adds. No eligible review in `R*` of that version
dissents (the R6.OBL29.3 rule; a non-empty `dissent` counts). The bootstrap version is verified
instead by §3. Identity strings are not authenticated (r9 R-8). R6.CUST.8 is not optional: a `close`,
`freeze` or `unfrozen` entry states facts the tool cannot fully check, and without a review record on
`main` a writer could establish custody with an empty or wrong `runs`. Adopting the `close` design
therefore adopts R6.CUST.8, including the item ids `entry:<i>` it adds to the review lint, a schema
change that the owner's adoption must cover.

**R6.CUST.10 Release-gate check.** A release-gate step evaluates, at the commit under check as `M`,
R6.CUST.2 for the version in its tree, R6.CUST.4, the mechanical parts of R6.CUST.5 (c1) for
`freeze` entries and receipt members, (c3), (c4)'s second clause and (c5), the second and third
clauses of (c2), and R6.CUST.8, and fails on any failure. It does not require a `close` for every
context, since a round lands before its closing statement can. A later commit can falsify one of the
clauses it checks only by adding a dissenting review under R6.CUST.8, which is meant to block; no
clause it checks becomes false through a later admission or landing. It
establishes nothing for a run, which re-checks everything at its own `M`. It is a new step in the
existing release gate (OQ-9).

***

## 5. Fail-closed rules and the mechanical/review split

**R6.CUST.9 Failure outcomes.** For every cited reassessment discharge of the run:

| Condition | Outcome |
|---|---|
| no regular file at the custody path in effective `M`'s tree | FAIL `record-invalid` naming `custody-missing`, and `retirement-blocked` for the finding |
| `V_M` fails R6.CUST.2 | FAIL `record-invalid`, `custody-schema` |
| (s1) fails | FAIL `record-invalid`, `custody-chain` |
| (s2) fails | FAIL `record-invalid`, `custody-prefix` |
| (s3) fails | FAIL `record-invalid`, `custody-regressed` |
| (s4) fails | FAIL `record-invalid`, `custody-stray` |
| (s5) fails | FAIL `record-invalid`, `custody-duplicate` |
| a discharge-bearing context has no `close` (c2) | FAIL `record-invalid`, `custody-unclosed` |
| a `close` names an `f` that is no discharge-bearing context (c2) | FAIL `record-invalid`, `custody-unsupported` |
| a `close` is contained in a version at a commit that does not descend from the context's landing (c2) | FAIL `record-invalid`, `custody-early-close` |
| a receipt's `control_plane_blobs` member is absent from `f`'s tree or differs there (c1, variant (i)) | FAIL `record-invalid`, `custody-receipt-mismatch` |
| a `freeze` entry fails (c1, variant (ii)) | FAIL `record-invalid`, `custody-unsupported` |
| the `close` runs for `f` differ from the landed run results for `f` (c3) | FAIL `record-invalid`, `custody-runs-mismatch` |
| an `unfrozen` entry is the only cover of a configuration pinned after it (c4, pin rule) | FAIL `record-invalid`, `custody-incomplete` |
| the run's own `F` is the `f` of a closed context (c3, R6.CUST.7) | FAIL `record-invalid`, `custody-closed-freeze` |
| (c3) shape fails | FAIL `record-invalid`, `custody-run-shape` |
| (c4) fails: a discharge-bearing configuration unaccounted for, or an `unfrozen` entry naming none | FAIL `record-invalid`, `custody-incomplete` or `custody-unsupported` |
| (c5) fails for a commit present in the store | FAIL `record-invalid`, `custody-unreachable` |
| R6.CUST.8 fails | FAIL `record-invalid`, `custody-unreviewed` |
| a run does not replay because a required record or reference does not resolve, or eligibility is undecidable | FAIL `record-invalid`, `custody-replay` |
| a commit, tree or blob that custody, `Vers(M)`, the receipts or a replay needs is missing or does not hash to its id | ERROR, no verdict (R6.REC.17) |

Every custody failure makes each cited discharge inapplicable; none lifts a finding, none is a
warning, and none depends on a commit message, pull request, Issue, run log or earlier verdict (r9
§2.2, "Decision"). An empty witness set is evidence of no dispute only when custody is established.
The failure is global to the run's cited discharges (OQ-14).

**What the tool checks mechanically.** R6.CUST.2, R6.CUST.4, R6.CUST.5 except the completeness of
`runs`, R6.CUST.6, R6.CUST.8's form, the bootstrap blob id, the presence and hash of every object, and
the decision `blocked(D, W)`. The gate step R6.CUST.10 checks the same rules that do not depend on a
closing statement existing.

**What is left to review.**
1. The bootstrap's item (c) of §3; under variant (i) of D-1, the precondition that every
   discharge-bearing freeze is the `F` of a native V3 round, which the tool cannot enforce: a freeze
   made outside V3 forms no context and is caught only by review of the `unfrozen` entry its pinned
   configuration then needs, which the pin rule of (c4) forces to be written after the pin; and under
   variant (ii), that the `freeze` entries list every owner-designated freeze of a discharge-bearing
   configuration.
2. Where no run results landed (c3), the completeness and attribution of each `close` entry's
   `runs`: every authorized op C run of the freeze, with its exact `M` and the `REV` it admitted, and
   no run filed under another context; an empty `runs` is a statement that rests on this review. A run
   whose `REV` never landed on `main` cannot be listed (c5), so a correct `close` for that freeze
   cannot exist and custody stays unestablished (R-C2).
3. The truth of each `unfrozen` and `void` entry.
4. The procedural preconditions (OQ-7): each discharge-bearing round lands with its ancestry, each
   admitted `REV` lands on `main` by a merge that keeps its id, and the freeze's `close` lands, before
   a later discharge-bearing freeze is designated.
5. The tool revision that adds the constants of R6.CUST.1 and implements this design.

Review is recorded by R6.CUST.8 review records for items 1 (variant (ii)), 2 and 3, and otherwise by
ordinary independent review of the pull requests.

**Controls.** `CONTROLS.json` preregisters the controls: positive (CU-P*), negative and boundary
(CU-N*), adversarial countercases (CU-X*) and residual or boundary rows (CU-B*). Each control other
than a residual one names the implementation mutation it must detect, in both directions: a tool that
keeps failing every discharge is killed by the positive rows, and a tool that relaxes any rule of
R6.CUST.2 to R6.CUST.10 by the negative and countercase rows. Residual rows document limits and kill
nothing. The decision rule is preregistered, not the expected numbers: a control holds when the run's
outcome and named items match its `expected`, over the r9 fixture as amended in the row.

***

## 6. Assumptions and limits

- **R-C1. A freeze that never reaches `main`, or one made outside V3 under variant (i).** A
  designated freeze whose round has not landed, or never lands, has no receipt or `freeze` entry
  reachable from `M`, and its configuration is not in `R*(M)`. Under variant (i), a freeze made outside
  a native V3 round lands without a receipt; the pin rule of (c4) then demands either a context or an
  `unfrozen` entry written after the pin, so the omission surfaces at review rather than silently,
  but the tool cannot establish that the freeze happened. The tool
  cannot see it. The preconditions of §5 item 4 and the bootstrap's item (c) are review. AGENTS.md
  §A.39 requires a halted round to land with a halted receipt, which narrows but does not close the
  gap before landing.
- **R-C2. A `REV` that never lands.** A `REV` that never becomes reachable from `main` cannot be
  listed in a `close` entry (c5). A correct closing statement for that freeze then cannot exist, and
  custody stays unestablished for every later run (fail closed). Where the run results did not land
  on `main` (c3), a `close` that omits a run, lists none although runs were made, or files a run under
  another context loses the witnesses of that run or replays it under the wrong configuration and
  selector; each of these rests on the R6.CUST.8 review. Where the results landed, each is a
  mechanical failure.
- **R-C3. Squash or rebase landing.** A discharge-bearing round landed by squash or rebase has a
  receipt or `freeze` entry reachable from `main` and an `f` that is not, so its context cannot replay and every cited
  discharge stays inapplicable. This is the fail-closed outcome r9 §2.2 and R-1 require; no custody
  entry repairs it, and this design does not accept the squash and rebase gap.
- **R-C4. Liveness.** An entry that fails a mechanical check and lands despite R6.CUST.10 keeps
  custody unestablished permanently (§4.1; OQ-15). Under variant (ii), a later foxtrot fast-forward
  that moves a landing merge off the first-parent chain has the same effect. So does a configuration
  that was pinned but never frozen while its only `unfrozen` entry predates the pin (pin rule of (c4);
  OQ-20).
- **R-C5. Identity strings.** `author` and `reviewer` are not authenticated (r9 R-8).
- **R-C6. Tool revisions.** A later tool revision that narrows the replayed predicates can forget a
  witness (r9 P-4, R6.STAT.5).
- **P-1 to P-5 of r9 §6** apply unchanged; a rewrite of `main` history (r9 R-2) defeats `Vers(M)` and
  the receipt walk as it defeats `R*`.

***

## 7. What this design deliberately does not do

- It confers no authority. No entry approves, clears, adjudicates, accepts, withdraws or discharges
  anything; a custody context never supplies a positive input to a discharge (§4.3, R6.STAT.4).
- It copies no evidence and lists nothing Git already establishes: under variant (i) of D-1 freezes
  come from receipts, under variant (ii) a `freeze` entry lists only what no structured Git record
  holds, and no record, review, configuration, tree, verdict or witness is duplicated.
- It adds no admitted record kind for runs: the custody record is read by a fixed tool path, not
  through a configuration's `records` (R6.RECON.33's table is unchanged). R6.CUST.8, a condition of
  the `close` design, gives item ids to one new reviewed kind in the review lint, a schema change
  requiring the owner's decision. R6.CUST.10, if adopted, adds a release-gate step (OQ-16).
- It does not design route 2, accept the squash or rebase gap, recover evidence that never reached
  `main`, or change any witness predicate, reliance clause or clearance condition of r9.
- It adds no outcome class: every failure uses `record-invalid`, `retirement-blocked` or ERROR.
- It authorizes no implementation, freeze, trial, dispatch or merge.

***

## 8. Requirement trace

| r9 §2.2 or owner requirement | Clause of this design |
|---|---|
| discover witnesses and dispositions from verified custody reachable from protected `main`, starting at effective `M` | R6.CUST.1, R6.CUST.4 (`Vers(M)`), R6.CUST.5 (c1), (c5), R6.CUST.6 |
| verify completeness from an independently verified starting inventory | R6.CUST.3 and §3 (a)–(d) |
| the retained sequence of authorized freezes | R6.CUST.5 (c1), variant (i) receipts or variant (ii) `freeze` entries (D-1); (c4) |
| operative repair inputs | R6.CUST.6 rows: configuration, reassessment, repair entry, commits; `close` runs |
| original witness sources | R6.CUST.6: `R*(m)` and each `rev`, reachable from `M` (c5) |
| later dispositions | R6.CUST.6 last rows: later contexts, reviews in `R*`; `Adjudicated(W)` false |
| each successor carries all earlier evidence | R6.CUST.4 (s2), (s3) |
| each successor accounts for each newly authorized context | R6.CUST.5 (c1), (c2) at every `M` |
| historic configuration and original selector for each older witness | R6.CUST.6 rows "configuration" and "selector" |
| a current run's positive inputs cannot serve as the negative-witness list | R6.CUST.6: witnesses from every run of every context |
| verify custody starting point and coverage before an applying discharge | R6.CUST.7 |
| an empty result from incomplete custody is no evidence | R6.CUST.9 closing paragraph |
| missing custody or unresolved eligibility: FAIL `record-invalid` and `retirement-blocked` | R6.CUST.9 table |
| unreadable or unverifiable required object: ERROR | R6.CUST.9 last row |
| preserve bytes, paths, objects, lineage, authorization provenance, reviews, corrections, adjudications | R6.CUST.6 mapping, by reference to Git objects reachable from `M`; receipt as provenance |
| evidence only, no positive repair authority | R6.CUST.2, §4.3 "Custody only adds witnesses", §7 |
| format, bootstrap and mapping fixed and independently verified before reliance | R6.CUST.2, R6.CUST.3, R6.CUST.6; this design's review and adoption |
| a retained witness names config, freeze, mode, selector, reassessment, finding, repair, edge, `S`, objects, exact `M`, `REV` | R6.CUST.6 mapping table, row by row; `close` runs give the exact `M` and `REV` |
| `Inapplicable(W)` from retained custody | §4.3 closing paragraph |
| terms read through the verified reader; messages, PR text, logs, verdicts are not inputs | R6.CUST.1, R6.CUST.9 |
| r9 §2.3: a later freeze reusing the disputed repair consults custody | R6.CUST.6, R6.CUST.7 |
| r9 R-1: custody of a prior scope not established leaves discharge inapplicable | R6.CUST.5 (c2), R6.CUST.9; R-C1 to R-C3 |
| owner: bootstrap is an independently verified starting inventory | R6.CUST.3, §3 |
| owner: evidence identity by exact paths, Git object ids and finding references | R6.CUST.2 encodings; R6.CUST.6 |
| owner: each successor binds its predecessor | R6.CUST.4 (s1), (s2) |
| owner: retain operative repair inputs, witnesses and later dispositions | R6.CUST.6 (witnesses by reproduction; OQ-2) |
| owner: completeness and object integrity independently verifiable | R6.CUST.5, R6.CUST.9 ERROR row, R6.CUST.10, §3 (b) |
| owner: missing evidence fails closed | R6.CUST.5 (c2), R6.CUST.9; (s3), (s4), (c4); R-C2 |
| owner: custody supplies evidence, never authorization | §4.3, §7, R6.CUST.2 |
| owner: minimalism, not a second history | §2.2 "Why these four", §2.3, §4.1 closing paragraph, §7 |
| owner: prefer existing Git objects and verification mechanisms | receipts and `v3_verifier` (c1, variant (i)); verified reader; `record_authority.py` pin; `oi-review-record/1` (R6.CUST.8); side-change classes (R6.CUST.1); release gate (R6.CUST.10) |

***

## 9. Review of c1: findings and changes

| Finding | Change in c2 |
|---|---|
| 1. Admission from `f` not tied to the freezing round | R6.CUST.5 (c1): a configuration is admitted from a receipt only beside a `PREREG.md` listed, by path and blob, in that receipt's `control_plane_blobs`; controls CU-P8, CU-N21 |
| 2. A discharge can apply on incomplete custody (`rev` completeness by review; a never-landed `REV` cannot be listed) | **Choice (b):** a reviewed per-freeze closing statement (`close`) on `main`; custody is not established for a context without one (c2). Reason: (a) treats every `REV`-shaped commit as a context, which over-qualifies witnesses r9 does not retain ("the existence of an eligible pair in history alone gives no witness") and still lets a discharge apply when an admitted `REV` never lands; (b) fails closed in that case (R-C2) and records exactly what r9 asks for. R-C2 states that a never-landed `REV` cannot be listed; §5 item 4 adds the landing precondition |
| 3. Replay at the current `M` can drop a witness | **Choice (b):** each run's exact `m` (former OQ-1 (b)), carried in the same `close` entry as finding 2's `REV`s. Reason: (a) would hold positive-route conditions true in replay, a rule stricter than r9 that blocks discharges r9 permits; (b) is r9's own requirement ("the exact `M`/source tree") and, combined with finding 2, adds no further entry type. R6.CUST.6 evaluates every `M`-dependent condition at `m`; controls CU-N20 (foxtrot) and CU-P9 |
| 4. `freeze` entries duplicate Git | `freeze` removed; contexts derived from receipts (c1); `close` names its `f` directly; entry types are `bootstrap`, `close`, `unfrozen`, `void` |
| 5. Chained wrong entries fatal; re-bootstrap allows truncation | (s3) applies to every well-formed version, chained or not, so a new bootstrap cannot truncate; (s4) requires each `void` to name a non-well-formed blob in `Vers(M)`; multiple `close` per `f` let an omitted run be added; OQ-9 adopted as R6.CUST.10; the remaining liveness hazard is stated (§4.1, R-C4, OQ-15) |
| 6. Mode | §1 defines discharge-bearing with regular mode and `admission.mode` `chain`; builder step 1 and (c1) use it; controls CU-N22, CU-N23 |
| 7. Custody contexts only add witnesses | §4.3 "Custody only adds witnesses", including NR-2; control CU-X4 |
| 8. Detection of custody review records | §2.2 "Detection"; CU-B4 extended |
| 9. Controls | added CU-N19 (cycle), CU-N8b (`void` outside `Vers(M)`), CU-N4b (bootstrap constant changed), CU-N25 (chained wrong entry), CU-P8/CU-N21 (unrelated receipt), CU-N20 (foxtrot), CU-N22/N23 (mode), CU-N24 (side change); CU-B3 recast as positive CU-P9 under exact-`m` replay; CU-X2 marked as a paired run |
| 10. Nits | implementation cited at `e88ca375`; "regular mode (`100644` or `100755`)" throughout; measurement reworded in §1 |

The table above records c2's changes; where c3 changes them again, the table below says so.

**Re-review of c2 (PR #1616 comment 7202652276):**

| Finding | Change in c3 |
|---|---|
| 1. (c1) admits no configuration, since receipts list only `preregistration.md` and amendments (critical) | Not chosen: decision D-1 is the owner's. (c1) carries variant (i), native V3 rounds keyed on the record directory of the receipt's `preregistration.md`, with its realizability constraint (OQ-18), and variant (ii), reviewed `freeze` entries with `landing`. The schema, builder, mapping, gate and failure table mark what each variant adds. Controls are tagged by variant; positive variant (i) controls use a receipt that `tools/v3_receipt.py` builds |
| 2. `close` runs undefined | (c3) defines runs as the authorized op C runs with `F = f` between designation and landing; (c2) requires the `close` after the landing (`custody-early-close`); a run under a closed `f` fails (`custody-closed-freeze`, R6.CUST.7); runs are checked against landed run results where they exist (`custody-runs-mismatch`, OQ-17); otherwise empty and misattributed runs are review-resting residuals in R-C2 and §5 item 2 |
| 3. R6.CUST.8 optional | R6.CUST.8 is a condition of the `close` design; former OQ-5 removed |
| 4. `unfrozen` converse blocks forever | (c4) drops "no context admits it"; a later admission only creates a context needing its own `close`; the gate checks only clauses no later commit can falsify |
| 5. A listed control-plane member missing from `f`'s tree is skipped | (c1) variant (i): `custody-receipt-mismatch` |
| 6. Cite Form (i) for custody reviews | §2.2 "Detection" quotes R6.RECON.26 Form (i) |
| Controls | added CU-N26 (empty `close`), CU-N27 (run under the wrong context), CU-N28 (run after the `close`), CU-N29 (early `close`), CU-N30 (receipt member mismatch), CU-P10 (`unfrozen` later admitted); receipt-based controls rebuilt on the real receipt shape and tagged `variant` |

**Re-review of c3 (PR #1616 comment 7202781537):**

| Finding | Change in c4 |
|---|---|
| 1. Variant (ii), stale `unfrozen` entries | (c4) pin rule: an `unfrozen` entry covers a configuration pinned in any reachable `Record pins` table only when introduced after every pinning commit; otherwise a context is required (a `freeze` entry under (ii), a receipt under (i)); `custody-incomplete`. Control CU-N32 |
| 2. Variant (ii), `landing` barely checked | (c1) variant (ii): `landing` is a merge on `M`'s first-parent chain whose first parent lacks `f` and another parent contains it; the foxtrot liveness hazard is stated in R-C4. Controls CU-N33 (`landing = f`) and CU-N34 (an early descendant) |
| 3. Runs check avoidable and unspecified | (c3) names the run results: `result.json` under `<dir>/op-c-runs/`, schema `oi-ledger-coverage/5`, with `inputs.operation`, `inputs.freeze`, `inputs.config.blob_sha256`, `roles.M` and `inputs.classify_records[].rev`; both forms stated, with missing results a custody failure if OQ-17 is adopted. Control CU-N35 |
| 4. Variant (i) precondition | §5 item 1 and R-C1 list "every discharge-bearing freeze is a native round's `F`" as review-resting, and note that the pin rule makes that review effective |
| 5. Nits | CU-N2 split into CU-N2 (both) and CU-N2i (variant (i): an entry type `freeze`); CU-N30 worded as built by `tools/v3_receipt.py`, then mutated; CU-P2's `expected` completed |

**Re-review of c4 (PR #1616 comment 7202860517):**

| Finding | Change in c5 |
|---|---|
| 1. Result fields do not exist; `roles.M` is a diagnostic | (c3) reads top-level `operation` = `"execution"`, `config.commit` = `f`, `config.blob_sha256`, `config.admission.mode` = `"chain"`, no `harness`, and `REV` from `inputs.classify_records[].rev`; non-evaluating outcomes (USAGE, ERROR, VOID, INTERNAL) are not runs; `M` needs a named field (`roles.M` adopted as named, or `inputs.main` under OBL-28 C-24), listed as dependency OQ-19. CU-N35 rebuilt, with an errored-result variant |
| 2. Pinning commit undefined | (c4) defines a pinning commit as one that introduces the pin (listed in its tree, absent from at least one parent's). Control CU-P11: an `unfrozen` entry written after that commit passes while the pin is still present at `M` |
| 3. Landing wording | "first parent is not a descendant-or-self of `f`" |

**Confirmatory re-review of c5 (PR #1616 comment 7202923040):**

| Finding | Change in c6 |
|---|---|
| 1. Ordinary merges count as pinning commits | (c4): a pinning commit lists the pin while none of its parents does. CU-P11 variant b: a later merge of a branch based before the pin still passes |
| 2. CU-N32's re-assertion variant cannot pass | Option (a) taken: re-assertion variant dropped; (c4) states that a stale `unfrozen` entry is recovered only by a context, and the no-recovery case is stated in (c4) and R-C4. Option (b) recorded as OQ-20 |
| 3. REV of admitted records | (c3): "the common `rev` of the admitted classify records, or null when none was admitted" |
| Adoption list | new §12, from the reviewer's ten items |

***

## 10. Open questions for the owner

Each point below is one the r9 text does not settle. The recommended default is what this draft
assumes; none is decided by this draft. Former OQ-1 and OQ-4 are settled by the choices of §9
(c1 findings 3 and 2), former OQ-9 is adopted as R6.CUST.10, and former OQ-5 is settled by making
R6.CUST.8 a condition of the `close` design (c2 finding 3), each subject to the owner's adoption of
this design; their ids are not reused.

| Id | Question | Recommended default | Alternatives and consequences |
|---|---|---|---|
| D-1 | The source of discharge-bearing contexts (R6.CUST.5 (c1)); put to the owner by the coordinating session | none: this draft carries both variants and does not choose | (i) native V3 rounds only: contexts derived from receipts, no listed freezes, but retirement freezes must become V3 rounds with a plan layout V3 `S2` and R6.A1CFG.1 both accept (OQ-18); (ii) reviewed `freeze` entries: works with the existing A1 plan layout, but completeness of the freeze list rests on review of owner designations |
| OQ-2 | Does the record list derived witnesses? | no; witnesses are reproduced each run and reported in the result | a checked cache of witnesses: readable without the tool, but duplicates derived data and must change with any predicate change |
| OQ-3 | Under which rules is a prior run replayed? | the tool revision pinned at the current `F` | the revision pinned at the context's `f`: faithful, but needs a second execution environment per context |
| OQ-6 | Are discharge-bearing configurations without a context accounted for by `unfrozen` (R6.CUST.5 (c4))? | yes | drop (c4) and `unfrozen`: smaller, but a configuration landed outside a receipted round goes unaccounted |
| OQ-7 | What procedural preconditions order freezes? | every earlier discharge-bearing round, of any retirement, has landed with ancestry, its admitted `REV`s have landed on `main` by merges keeping their ids, and its `close` has landed, before a later discharge-bearing freeze is designated (any retirement, because reliance (r1) crosses retirements) | the same retirement only; or none, accepting R-C1 and the fail-closed outcome of R-C2 |
| OQ-8 | Path and constants | `verification/audits/foundations/a1exit-obl29-custody/custody.json`; path and bootstrap blob id in `record_authority.py` | another directory under `verification/audits/`; a path outside it needs a second selector in the walk |
| OQ-10 | Do harness-admitted runs form contexts? | no; discharge-bearing requires `admission.mode` `chain` and a freeze under (c1) | include harness runs: they have no authorized freeze to derive |
| OQ-11 | Which commit is `B0`? | the `main` commit designated in the decision adopting the implementing tool revision | the current `main` at adoption of this design |
| OQ-12 | Result fields for custody | add `category3.custody` with the status, `V_M`'s blob id, the contexts, runs and each witness with its route; a result-schema change beside R6.OBL29.8 | report custody failures only through the existing `record-invalid` items |
| OQ-13 | Does a custody failure affect the R6.RECON.26 no-edit route? | no (r9 ties custody to "the repair under consideration") | yes: simpler, but blocks retirements that drop the bound edit |
| OQ-14 | Is a custody failure global or per repair? | global to the run's cited discharges | per repair: needs a relevance test that itself depends on the failed replay |
| OQ-15 | Recovery when a mechanically invalid entry lands despite R6.CUST.10 | none: custody stays unestablished (fail closed) | an owner-authorized correction route, for example a tool revision listing the offending entries as excluded; a new mechanism needing its own design |
| OQ-16 | Adopt R6.CUST.10 as a release-gate step? | yes (review finding 5) | no: run-time checks only, accepting that a malformed or invalid entry is found only at the next run and cannot then be removed |
| OQ-17 | Must a discharge-bearing round land the `result.json` of each op C run under `<dir>/op-c-runs/` of its configuration's directory, so that (c3) checks `runs` mechanically and a missing result is a custody failure? | yes, at that location | no: the equality is checked only where results landed, and otherwise completeness and attribution rest on review (R-C2); or another location fixed by the same rule |
| OQ-20 | May a stale `unfrozen` entry be re-asserted after a pin? | (a) no: a stale entry is recovered only by a context; a configuration pinned but never frozen whose `unfrozen` entry predates the pin has no recovery (R-C4) | (b) an exception to (s5) for re-asserted `unfrozen` entries, with the pin rule judged by the version that last adds the entry: recovers that case, at the cost of a small schema and rule change the owner must adopt |
| OQ-19 | Which named result field carries a run's `M` for (c3)? A dependency: an r6 and tool change adopted with this design | adopt `roles.M` as a named field a verdict may read (R6.OUT) | emit `inputs.main` under OBL-28 C-24; until either is made, (c3) cannot read `M` from results and takes its review form |
| OQ-18 | Under variant (i) of D-1, which plan layout reconciles the V3 record directory with R6.CFG.1 and R6.A1CFG.1? | the configuration and its `PREREG.md` under `R/amendments/` of the round, with the admitted record directory of R6.A1CFG.1 set to that round's record directory by a tool revision | the configuration landed under `R` on `main` before `D`; either needs an r6 amendment |

***

## 11. Provenance and references (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7202075726, item 5 | authority, quoted with author and time in §0 | provenance |
| r9 at `77a73c022091f598cf807fcf89d66c3cf43208de` | the source requirements of §2.2 and their definitions | support off `main`: the adopted design is on `design/a1-obl29-remedy-20261126`; it must reach `main` no later than this design |
| #1601 comment 7197486426 | r9's adoption and the token convention | provenance |
| Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e` | R6.CFG.*, R6.RECON.*, R6.REC.* cited here | support off `main` (PR #1593 open) |
| PR #1577 at `e88ca375c35a278371f8bc1c70ba963ea61fef05` | the current fail-closed behaviour this design replaces | provenance |
| c1 at `dc2b344c91c04979570ad58c5a554b3b7585008f` and its independent review (relayed by the coordinating session) | the findings answered in §9 | provenance |
| c2 at `b61467e9efecc435798861130a5ace5e40c18a91` and its re-review, PR #1616 comment 7202652276 | the findings answered in §9 | provenance |
| c4 at `3658ed49f210f83f633a47cf2546ea5606b005b2` and its re-review, PR #1616 comment 7202860517 (result fields at `e88ca375`, `cli.py` freeze check) | the findings answered in §9 | provenance |
| c3 at `ca82d23ef4b604b040660515e486fe6fdfdf1f9d` and its re-review, PR #1616 comment 7202781537 | the findings answered in §9; the reviewer's build of a variant (i) receipt with `tools/v3_receipt.py` | provenance |
| `tools/v3_verifier.py` (control-plane pattern) and `verification/infrastructure/v3/architecture.md` (`K1`, `S2`) on `main` | variant (i) of (c1) and its realizability | support on `main` |
| `origin/main` at `84e927b9b7c2bcc8cb9624cb036167dae233e408` | the drafting measurement of §1; receipts under `verification/receipts/`; `tools/v3_verifier.py` as an existing mechanism | support on `main`; the measurement is re-established at `B0` (§3 (b)) |

***

## 12. What the owner adopts with this design

Adopting the design adopts nothing by itself (§0, §7). Taken from the confirmatory review of c5
(PR #1616 comment 7202923040), the decisions and changes that must be adopted with it, for D-1 = (ii)
with OQ-17, R6.CUST.8 and R6.CUST.10, are:

1. **D-1.** The context source: variant (ii), the `freeze` entry type with its `landing` rule, or
   variant (i) with OQ-18's plan layout and r6 amendment.
2. **OQ-19 (r6 and tool).** A named result field for a run's `M`: `roles.M` moved from declared
   diagnostics to named fields in R6.OUT, or `inputs.main` emitted under OBL-28 C-24.
3. **OQ-17 (r6 and plan rule).** Every discharge-bearing round lands each op C run's `result.json`
   under `<dir>/op-c-runs/` beside its configuration.
4. **R6.CUST.8 (review-lint schema).** Item ids `entry:<i>` for `oi-review-record/1` reviews of
   custody versions.
5. **R6.CUST.10.** A new release-gate step.
6. **The record schema `oi-obl29-custody/1`** at the fixed path, with the path and bootstrap blob-id
   constants in `tools/ledger_coverage/record_authority.py` (a tool revision), and in
   `engine/purity.py`'s schema list if that list must name every schema.
7. **A tool revision implementing R6.CUST.1–10:** replacing `custody_unverified` in
   `engine/category3.py`, adding the custody path (and, under variant (i), `verification/receipts/`)
   to the R6.OBL29.7 walk's fixed selection, and adding the `custody-*` item names under the existing
   `record-invalid` class.
8. **OQ-12, if its default is kept.** A `category3.custody` result field, a change to the
   `oi-ledger-coverage/5` schema file.
9. **The procedural preconditions of OQ-7 and §5 item 4:** admitted `REV`s land by merges that keep
   their ids, each `close` comes after its landing, and freezes are ordered as OQ-7 states.
10. **OQ-20, if option (b) is chosen.** The (s5) exception for re-asserted `unfrozen` entries.

The remaining open questions of §10 keep their recommended defaults unless the owner decides
otherwise. None of these items authorizes implementation, a freeze, a trial, a dispatch or a merge
(AGENTS.md §A.50).
