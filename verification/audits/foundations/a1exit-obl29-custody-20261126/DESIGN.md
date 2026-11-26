# OBL-29 custody: format, bootstrap inventory and mapping to admitted inputs (paper design c1)

## 0. Status, authority, scope and goal link

**Status.** Paper design c1, pending independent review and an owner decision. The proposed
requirements (ids `R6.CUST.n`) have no force until adoption. Adoption of this design does not
discharge OBL-29, does not authorize implementing custody-dependent discharge, and changes no
schema or admission rule by itself (§7).

**Authority.** Owner decision (amaybaum, received 2026-11-26T19:52Z, coordinating session; recorded
at #1169 comment 7202075726), item 5, quoted:

> Authorize a bounded paper-only design and independent review of the OBL-29 custody format, bootstrap inventory and mapping to admitted inputs. Prefer existing Git objects and verification mechanisms. Bring the reviewed design for adoption before implementing custody-dependent discharge.

The decision closes: "All existing correctness, independent review, staging, freeze, trial and
landing gates remain in force."

**Source requirements.** The adopted OBL-29 remedy r9: `DESIGN.md` and `CONTROLS.json` under
`verification/audits/foundations/a1exit-obl29-remedy-20261126/` at
`77a73c022091f598cf807fcf89d66c3cf43208de` (branch `design/a1-obl29-remedy-20261126`), adopted by
owner amaybaum at #1601 comment 7197486426 (2026-11-26T16:19:17Z) with the token convention
`<blob>#<item>`. Its §2.2 "Custody and lookup" states the requirements this design serves and leaves
"the custody format, bootstrap record and mapping to admitted inputs" to be fixed and independently
verified before implementation relies on them. Section numbers prefixed "r9" refer to that text;
requirement ids `R6.*` refer to it or to the Amendment 6 r13 contract at
`5ad8837521de0a26734266a64f91548fd3dcff1e` that it amends.

**Implementation reference.** PR #1577, head `aafb052580ea2d07e1b14bfbd00c543417e89206`,
`tools/ledger_coverage/engine/obl29.py` (the predicates of r9 §2.2 over explicit witnesses, not yet
called by a run) and `engine/category3.py`, whose `reassessment_problems` appends
`custody_unverified` to every cited discharge, so every cited discharge fails closed. This design
states what replaces that unconditional failure; it changes no code.

**Goal link (AGENTS.md §A.47).** Serves A1 retirement (#1169) through its blocker OBL-29 (#1598):
it would decide whether the custody that r9 §2.2 requires can be stated as a mechanically checkable
record built from existing Git objects, and what remains to review. Not the outcome expected: a
finding that some requirement cannot be met mechanically is an equally valid result, and §6 records
the points where that is so.

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
"under the configuration and admitted lineage inputs under which [it] is found", and states that "the
existence of an eligible pair in history alone gives no witness for a frozen discharge that never
made the lineage check operative". The set of operative discharge checks is decided by frozen
configurations and the record commits their runs admitted. A later run's own inputs "cannot serve as
the list of negative witnesses" (r9 §2.2). Custody supplies that list, and lets a run show the list
is complete.

Write a **discharge-bearing context** for a frozen configuration whose `records` (R6.CFG.4) include
at least one reference of kind `reassessment`: only such a freeze can make a reassessment discharge
operative (R6.RECON.27), and so only such a freeze can qualify a witness. A freeze whose configuration
cites no reassessment qualifies no witness, and the no-edit route of R6.RECON.26 uses no repair and no
custody (§4.4).

**Drafting measurement (not verification).** At `origin/main`
`84e927b9b7c2bcc8cb9624cb036167dae233e408` (6,076 commits by all-parent ancestry), every blob that
ever stood at a path under `verification/audits/` was parsed as JSON. None has schema
`oi-reassessment/1`, `oi-reconciliation/2` or `oi-review-record/1`. Nine blobs have schema
`oi-retirement-config/1`, all at
`verification/audits/foundations/ledger-coverage-tool-20261123/a1exit-retirement-config.json`, and
none cites a record of kind `reassessment` or `reconciliation` (their kinds are `hit-classification`,
`scope` and `side-change-classes`). If an independent check confirms this at the bootstrap base, no
discharge check has yet been operative on `main`, and the bootstrap inventory lists no context (§3).

***

## 2. The custody record

### 2.1 Location

**R6.CUST.1 Location.** The custody record is the regular file at the single path
`verification/audits/foundations/a1exit-obl29-custody/custody.json`. The path, and the git blob id
of the bootstrap version (§3), are constants of `tools/ledger_coverage/record_authority.py`, the tool
file that already holds the admitted record directories (R6.A1CFG.1). That file is listed in
`tool.files` and pinned at `F` (R6.REC.18), so neither constant can be changed by a configuration, a
record or an argument; changing either is a tool revision. The directory is not a reconciliation
directory (R6.RECON.1), not a plan record directory, and lies outside every tool-landing prefix. The
run reads the record from the tree of effective `M` and its versions from every tree reachable from
`M` (R6.CUST.4), through the verified reader (R6.REC.17).

A custody successor that lands on `M` after `F` is a side change of the run (R6.TREE.5). The
configuration's side-change class record must classify the custody path, or the run reports
REVIEW_REQUIRED `side-change-unclassified` as for any other path. This is an existing mechanism and
needs no new rule.

### 2.2 Schema

**R6.CUST.2 Schema `oi-obl29-custody/1`.** The file's bytes are exactly the canonical JSON
(R6.RECON.29) of one object, with no trailing newline, and pass strict parsing (R6.RECON.29). The
object has exactly these keys:

| Key | Type | Meaning |
|---|---|---|
| `schema` | `"oi-obl29-custody/1"` | |
| `predecessor` | blob id or null | the git blob id of the version this one extends; null only for the bootstrap version |
| `author` | identity string (R6.RECON.29) | the writer of this version, for review independence (R6.CUST.7) |
| `entries` | array of entry objects, at least one | the append-only inventory |

Each entry has a `type` and exactly the keys its row lists:

| `type` | Further keys | Meaning |
|---|---|---|
| `"bootstrap"` | `base`: commit id | the inventory is complete for every discharge-bearing context reachable from `base` (§3). Exactly one, and it is `entries[0]` |
| `"freeze"` | `f`: commit id; `config`: reference | a discharge-bearing freeze: the configuration `config` admitted from `f` |
| `"rev"` | `f`: commit id; `rev`: commit id | a record commit `REV` (R6.RECON.2 (c)) admitted by a run under the freeze `f` |
| `"unfrozen"` | `config`: reference | a discharge-bearing configuration present in `R*` that no freeze has admitted |
| `"void"` | `blob`: blob id | a version of the custody path in `R*` that does not meet R6.CUST.2 or does not chain to the bootstrap (R6.CUST.4), acknowledged as carrying nothing that custody must retain |

Commit id, blob id, reference and identity string are the encodings of R6.RECON.29. There is no other
key and no free-text field. No key or literal value of the schema contains an invalidation token, so
the record cannot meet the category-3 heuristics of classes (b) or (c) except through a path value
copied from a record path (r9 R-3); control CU-B4 pins this. A key, entry type or value outside these
tables is a schema failure (R6.CUST.9). In particular no entry clears, adjudicates, accepts or
withdraws anything: an entry type that would is not in the table.

**Why these five.** `freeze` and `rev` are the operative repair inputs that `R*` cannot reveal
(§1). `bootstrap` anchors completeness. `unfrozen` and `void` exist only so that the completeness
rules of R6.CUST.5 and the stray rule of R6.CUST.4 can fail closed without making a single historical
mistake on `main` permanently fatal. Everything else the witness predicates need is already a Git
object reachable from `M` and is derived, not copied (§4).

### 2.3 Size

One entry is under 250 bytes. The record grows by one `freeze` entry per discharge-bearing freeze,
one `rev` entry per admitted record commit, and rarely by `unfrozen` or `void`. It carries no
witness, review, record content or verdict.

***

## 3. The bootstrap inventory

**R6.CUST.3 Bootstrap.** The bootstrap version is the version whose git blob id equals the constant
of R6.CUST.1. Its `predecessor` is null, its `entries[0]` is `{"base": B0, "type": "bootstrap"}`, and
its remaining entries are the output of the builder below at `B0`. `B0` is a commit on `main`
designated in the owner decision that adopts the implementing tool revision (open question OQ-11).

**What it lists.** Exactly the entries that R6.CUST.5 requires of an inventory at `B0`: a `freeze`
entry for every discharge-bearing freeze with a receipt reachable from `B0`, and an `unfrozen` entry
for every discharge-bearing configuration in `R*(B0)` that no such freeze admits. On the drafting
measurement of §1 both sets are empty, and the bootstrap version would be the canonical JSON of

    {"author": <writer>, "entries": [{"base": B0, "type": "bootstrap"}], "predecessor": null,
     "schema": "oi-obl29-custody/1"}

**Deterministic builder (specification).** Input: `B0`, read through the verified reader, and the
writer's identity string for `author`; the output depends on nothing else.
1. Walk every commit reachable from `B0` through any parent (R6.OBL29.7). Collect every regular entry
   under `verification/audits/` that strict-parses with schema `oi-retirement-config/1` and whose
   `records` includes a member of kind `reassessment` (the discharge-bearing configurations), and
   every regular entry `verification/receipts/<name>.json` with schema `v3-receipt`.
2. For each receipt, read its `f` and the tree of that commit. A configuration is admitted from `f`
   when R6.CFG.1–.2 admit it there: a regular file under `verification/audits/` with schema
   `oi-retirement-config/1` whose SHA-256 is listed in the last `Record pins` subsection of the
   `PREREG.md` beside it. Emit `{"config": ref, "f": f, "type": "freeze"}` for each admitted
   discharge-bearing configuration.
3. For each discharge-bearing configuration from step 1 that step 2 did not emit, emit
   `{"config": ref, "type": "unfrozen"}` as a candidate. A candidate is retained only on the
   reviewer's confirmation (§5); otherwise the builder's output is not a valid bootstrap.
4. Emit `bootstrap` first, then `freeze` entries sorted by `(f, config.path, config.blob_sha256)`,
   then `unfrozen` entries sorted by `(config.path, config.blob_sha256)`. Write canonical JSON.

The builder emits no `rev` entry: a `REV` admits only a reconciliation record, and with no
discharge-bearing freeze at `B0` there is no run to have admitted one. If the builder emits any
`freeze` entry, the bootstrap must also carry every `rev` of every run under it, which the builder
cannot discover (§6, R-C2), and the bootstrap then needs the review of §5 item 3 before it is pinned.

**Independent verification of the bootstrap.** Before the blob id is pinned:
- (a) a non-author reviewer re-runs the builder at `B0` and obtains the same bytes (deterministic
  replay);
- (b) the reviewer confirms the two sets by a method that shares no code with the builder, for example
  `git rev-list --objects B0` filtered to `verification/audits/` and `verification/receipts/` and a
  separate JSON parse of every blob, as in the drafting measurement of §1;
- (c) the reviewer checks the owner's recorded designations of `F` for retirement rounds up to `B0`
  against the receipts reachable from `B0`, and records that no designated discharge-bearing freeze
  lacks a receipt (the part a tool cannot see, §6 R-C1);
- (d) the tool revision that adds the pin is independently reviewed under the existing tool-revision
  route (R6.REC.18), and every later run re-checks the bootstrap's mechanical content through
  R6.CUST.5, which applies at every `M` and therefore at least to everything reachable from `B0`.

Items (a), (b) and (d) are mechanical or reproducible from `main`; item (c) is review.

***

## 4. Successor binding, completeness and the mapping

### 4.1 Successor binding

**R6.CUST.4 Successor rule.** Let `V_M` be the custody record in the tree of effective `M`. Let
`Vers(M)` be every distinct blob that stands at the custody path, at a regular mode, in any tree
reachable from `M` through any parent (the walk of R6.OBL29.7, with the custody path added to its
fixed selection; removing or rewriting the file on a later commit removes nothing from `Vers(M)`).
- (s1) **Chain.** Starting at `V_M` and following `predecessor`, every named blob is in `Vers(M)` and
  meets R6.CUST.2, and the chain ends at the bootstrap blob of R6.CUST.1. A version on that chain is a
  *chained version*. A cycle, or a predecessor-null version other than the bootstrap, breaks the chain.
- (s2) **Prefix.** For each chained version `V` with predecessor `P`, `P.entries` equals the first
  `len(P.entries)` elements of `V.entries` element for element, and `V` adds at least one entry. No
  entry is removed, reordered or changed.
- (s3) **Union.** Every other version in `Vers(M)` that meets R6.CUST.2 and whose own predecessor
  chain reaches the bootstrap contributes every one of its entries to `V_M.entries`. A fork is
  therefore resolved by a successor that names one side as `predecessor` and appends the other side's
  entries; a merge that keeps one side's file loses nothing silently.
- (s4) **Strays.** Every version in `Vers(M)` that fails R6.CUST.2, or whose chain does not reach the
  bootstrap, is named by a `void` entry of `V_M`.
- (s5) **Duplicates.** No two entries of `V_M` are equal, and each `freeze` names a distinct
  `(f, config)`.

The predecessor binding is by git blob id, so a successor binds the exact bytes of its predecessor,
and the predecessor is itself a Git object reachable from `M`. The record does not repeat the history
of the path: `Vers(M)` is read from Git, and the record adds only the binding Git cannot express,
which version extends which.

### 4.2 Completeness

**R6.CUST.5 Completeness.** At effective `M`:
- (c1) **Receipted freezes.** For every receipt in a tree reachable from `M` (path
  `verification/receipts/<name>.json`, schema `v3-receipt`, read by the walk of R6.OBL29.7 with that
  prefix added to its fixed selection, so deletion removes nothing), every
  discharge-bearing configuration admitted from the receipt's `f` (builder step 2) has a `freeze`
  entry with that `f` and that `config`. Conversely every `freeze` entry has such a receipt, and its
  configuration is admitted from its `f` and is discharge-bearing. The receipts are the existing V3
  protocol records (AGENTS.md §A.39); their validity is decided by `tools/v3_verifier.py --receipts`
  in the release gate, not by this tool. Over-inclusion of a freeze could only add witnesses; the
  exact bijection keeps the record honest in both directions.
- (c2) **Configurations.** Every discharge-bearing configuration in `R*(M)` has a `freeze` or an
  `unfrozen` entry.
- (c3) **Record commits.** Every `rev` entry names a `f` that has a `freeze` entry, and a commit with
  the shape of R6.RECON.2 (c): exactly one parent, a tree equal to that parent's except for regular
  files added inside reconciliation directories, at least one of them an `oi-reconciliation/2` record
  naming that parent as `M`. Whether the list of `rev` entries is complete is review (§5 item 2;
  OQ-4).
- (c4) **Reachability.** Every commit an entry names (`base`, `f`, `rev`) is reachable from `M`
  through any parent.

### 4.3 Mapping from r9's historical inputs to admitted inputs and Git objects

**R6.CUST.6 Replay of a context.** For each `freeze` entry `c = (f, config)`, the run re-establishes
the context's operative discharge checks and qualifies its witnesses under R6.OBL29.3, with these
inputs and no others:

| r9 §2.2 input (a retained witness "names" or custody "preserves") | Source in this design | Admission and verification in the replay |
|---|---|---|
| the original configuration, by exact reference | `freeze.config` | read at its path in `f`'s tree and admitted by R6.CFG.1–.2 from `f`'s pin table; failure is a custody failure (R6.CUST.9) |
| the original freeze, by verified commit | `freeze.f` | the receipt bijection (c1) and reachability (c4); `f` read through the verified reader |
| the applicable mode | the configuration's `admission.mode` | as recorded; a context whose mode is not `chain` is not discharge-bearing for custody (OQ-10) |
| the original selector | the side-change class record named by the configuration's `roles.side_change_classes` | resolved from anchor `f` (R6.RECON.33); its tool-landing prefixes and pins apply to that context only |
| the proposed reassessment | each `records` member of kind `reassessment` | resolved from anchor `f` (R6.RECON.33) and linted as at that freeze |
| the original finding reference and `item` | the reassessment's `finding` | looked up in `R*` (R6.OBL29.3) |
| the exact repair record and entry path; the repair commits | the reassessment's `repair.entry` and `repair.commits` | the record by exact reference in `R*`; for a pinned repair, read at `f` |
| the exact operative edge `U → P` | derived | R6.REC.7 for the repair record under the context's own admission route and anchor (`f`, or `REV` for a record a `rev` entry admitted) |
| the exact adverse review or competing successor `S` | derived | R6.OBL29.3 qualification over `R*` at the replay commit, with the context's selector |
| the exact `M`/source tree | the replay commit | effective `M` for every context (OQ-1); for a record admitted through a `rev` entry, the single parent of that `REV` |
| the exact `REV` and its admission evidence | `rev` entries | R6.RECON.2 (a)–(g) replayed with that `REV` and the context's configuration |
| full Git objects | none copied | every object reachable from `M`, read and hash-checked by the verified reader |
| authorization provenance | the receipt | the receipt's owner-designation attestation is provenance (AGENTS.md §A.42 item 2); the tool does not read it (R6.STAT.4) |
| reviews, corrections and later dispositions | `R*` and later `freeze` entries | every review in `R*`; a correction is a later context whose configuration cites a replacement `R` and review `Z`, judged by r9's `decide`; no adjudication route exists (r9 §5.6), so `Adjudicated(W)` is false |
| original bytes, paths and lineage | none copied | exact references resolve in `R*`; lineage resolves under R6.RECON.33 from the context's anchor |

The witnesses of all contexts, together with the run's own live witnesses, are the set over which r9's
`blocked(D, W)` is evaluated for each candidate discharge `D` of the run. A witness is identified by
its context `f`, its kind and the exact references r9 §2.2 lists, and is reported in the result
(OQ-12). The replay applies the rules of the tool revision pinned at the current `F` (OQ-3).

`Inapplicable(W)` is defined in r9 as failure of `W`'s original qualification to reproduce from
retained custody. Here every witness is obtained by reproduction from immutable objects and the
monotone `R*`, so a witness that does not reproduce is not in the set, and no recorded witness exists
to be reported as inapplicable. A witness can stop reproducing only through a tool revision that
narrows the predicates, which r9 P-4 and R6.STAT.5 govern.

### 4.4 What custody gates

**R6.CUST.7 Gate on discharge.** Custody is established at effective `M` exactly when R6.CUST.2,
R6.CUST.4, R6.CUST.5 and R6.CUST.8 hold and every context replays (R6.CUST.6) without a custody
failure. Before a run returns an applying reassessment discharge, custody must be established; the
check replaces `custody_unverified` in `reassessment_problems`. The R6.RECON.26 route by which a
configuration carries no edit the finding binds needs no repair and no custody, and is unaffected
(OQ-13).

**R6.CUST.8 Review evidence for non-mechanical entries (proposed; OQ-5).** Every version in `Vers(M)`
that meets R6.CUST.2, chains to the bootstrap and adds a `rev`, `unfrozen` or `void` entry relative to
its predecessor has, in the custody directory, an `oi-review-record/1` whose
`reviewed` is that version's exact `{path, blob_sha256}`, whose `reviewer` differs as an identity
string from the version's `author`, and which accepts every item, the items being `entry:<i>` for
each index `i` the version adds. No eligible review in `R*` of that version dissents (the R6.OBL29.3
rule, applied to custody). A version that adds only `freeze` entries needs no review: (c1) checks
them completely. Identity strings are not authenticated (r9 R-8).

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
| (c1) fails in either direction | FAIL `record-invalid`, `custody-incomplete` or `custody-unsupported` |
| (c2) fails | FAIL `record-invalid`, `custody-incomplete` |
| (c3) shape fails | FAIL `record-invalid`, `custody-rev-shape` |
| (c4) fails for a commit present in the store | FAIL `record-invalid`, `custody-unreachable` |
| R6.CUST.8 fails | FAIL `record-invalid`, `custody-unreviewed` |
| a context does not replay because a required record or reference does not resolve, or eligibility is undecidable | FAIL `record-invalid`, `custody-replay` |
| a commit, tree or blob that custody, `Vers(M)`, the receipts or a replay needs is missing or does not hash to its id | ERROR, no verdict (R6.REC.17) |

Every custody failure makes each cited discharge inapplicable; none lifts a finding, none is
downgraded to a warning, and none depends on the content of a commit message, pull request, Issue,
run log or earlier verdict (r9 §2.2, "Decision"). An empty witness set is evidence of no dispute only
when custody is established. The failure is global to the run's cited discharges, not per repair,
because a context that does not replay cannot be shown irrelevant to any repair (OQ-14).

**What the tool checks mechanically.** Everything in R6.CUST.2, R6.CUST.4, R6.CUST.5 (c1), (c2), (c4)
and the shape part of (c3), R6.CUST.6 and R6.CUST.8's form; the bootstrap blob id; the presence and
hash of every object; the replay of every context and the decision `blocked(D, W)` over the result.

**What is left to review.**
1. The bootstrap's item (c) of §3: no designated discharge-bearing freeze up to `B0` lacks a receipt.
2. Completeness of `rev` entries: every `REV` admitted by any run under a listed freeze is listed. The
   reviewer compares the record commits named in the runs' results with the `rev` entries.
3. The truth of each `unfrozen` entry (no freeze admitted that configuration) and of each `void`
   entry (the stray carries no entry that the record does not otherwise retain).
4. That each freeze of a discharge-bearing configuration lands with its receipt and ancestry before
   any later discharge-bearing freeze is designated, and that a custody successor recording it lands
   before the later freeze's runs (procedural precondition; OQ-7).
5. The tool revision that adds the constants of R6.CUST.1 and implements this design.

Review is recorded through existing mechanisms: R6.CUST.8 review records for items 2 and 3 where the
owner adopts OQ-5, and ordinary independent review of the pull requests otherwise.

**Controls.** `CONTROLS.json` preregisters 32 controls: 7 positive (CU-P1 to CU-P7), 18 negative
and boundary (CU-N1 to CU-N18), 3 adversarial countercases (CU-X1 to CU-X3) and 4 residual or
boundary rows (CU-B1 to CU-B4). Each non-residual control names the implementation mutation it must
detect. The mutation set covers both directions: a tool that keeps failing every discharge (killed by
CU-P1 to CU-P7) and a tool that relaxes any rule of R6.CUST.2 to R6.CUST.9 (killed by the negative and
countercase rows). Residual rows document R-C1, R-C2 and R-C4 and kill nothing. The decision rule, not
the expected numbers, is preregistered: a control holds when the run's outcome and named items match
its `expected`, over the r9 fixture as amended in the row.

***

## 6. Assumptions and limits

- **R-C1. A freeze that never reaches `main`.** A designated freeze whose round has not landed, or
  never lands, has no receipt reachable from `M`, and its configuration is not in `R*(M)`. The tool
  cannot see it. The precondition of §5 item 4 and the bootstrap's item (c) are review. AGENTS.md
  §A.39 requires a halted round to land with a halted receipt, which narrows but does not close the
  gap in the interval before landing.
- **R-C2. An unlisted `REV`.** An omitted `rev` entry loses a witness that only that admission made
  operative. The omission adds no entry, so R6.CUST.8 cannot detect it; it rests on review (§5 item 2)
  unless OQ-4's mechanical alternative is adopted.
- **R-C3. Squash or rebase landing of a discharge-bearing round.** Its `f` is then not reachable from
  `main` while its receipt is, so (c1) and (c4) fail and every cited discharge stays inapplicable from
  then on. This is the fail-closed outcome r9 §2.2 and R-1 require. No custody entry can repair it,
  and this design does not accept the squash and rebase gap.
- **R-C4. Conservative replay.** With OQ-1's default every context is replayed at the current `M`.
  A sibling that landed after all of a freeze's runs can then count as that freeze's witness, which r9
  would not retain. The effect is additional blocking, never a lost witness.
- **R-C5. Identity strings.** `author` and `reviewer` are not authenticated (r9 R-8).
- **R-C6. Tool revisions.** A later tool revision that narrows the replayed predicates can forget a
  witness (r9 P-4, R6.STAT.5).
- **P-1 to P-5 of r9 §6** apply unchanged; in particular a rewrite of `main` history (r9 R-2) defeats
  `Vers(M)` and the receipt walk as it defeats `R*`.

***

## 7. What this design deliberately does not do

- It confers no authority. No entry approves, clears, adjudicates, accepts, withdraws or discharges
  anything, and a custody record never supplies a positive input to a discharge (r9 §2.2, R6.STAT.4).
  An established custody only allows the existing predicates to be evaluated.
- It copies no evidence. No record, review, configuration, tree, verdict or witness is duplicated;
  custody names Git objects reachable from `main` and adds only the facts Git cannot express.
- It adds no admitted record kind for runs: the custody record is read by a fixed tool path, not
  through a configuration's `records` (R6.RECON.33's table is unchanged). R6.CUST.8, if adopted, adds
  item ids for one new reviewed kind to the review lint, which is a schema change requiring the owner's
  decision (OQ-5).
- It does not design route 2, accept the squash or rebase gap, recover evidence that never reached
  `main`, or change any witness predicate, reliance clause or clearance condition of r9.
- It adds no release-gate step (OQ-9) and no new outcome class: every failure uses `record-invalid`,
  `retirement-blocked` or ERROR.
- It authorizes no implementation, freeze, trial, dispatch or merge.

***

## 8. Requirement trace

| r9 §2.2 or owner requirement | Clause of this design |
|---|---|
| discover witnesses and dispositions from verified custody reachable from protected `main`, starting at effective `M` | R6.CUST.1 (read at `M`), R6.CUST.4 (`Vers(M)`), R6.CUST.5 (c4), R6.CUST.6 |
| verify completeness from an independently verified starting inventory | R6.CUST.3 and §3 items (a)–(d) |
| the retained sequence of authorized freezes | `freeze` entries, R6.CUST.5 (c1), (c2) |
| operative repair inputs | R6.CUST.6 rows: configuration, reassessment, repair entry, commits, `rev` |
| original witness sources | R6.CUST.6: `R*` and `REV`s reachable from `M` (c4) |
| later dispositions | R6.CUST.6 last rows: later contexts, `R*` reviews; `Adjudicated(W)` false |
| each successor carries all earlier evidence | R6.CUST.4 (s2), (s3) |
| each successor accounts for each newly authorized context | R6.CUST.5 (c1), (c2) at every `M` |
| historic configuration and original selector for each older witness | R6.CUST.6 rows "configuration" and "selector" |
| a current run's positive inputs cannot serve as the negative-witness list | R6.CUST.6: witnesses come from every context, independent of the run's own pins and `REV` |
| verify custody starting point and coverage before returning an applying discharge | R6.CUST.7 |
| an empty result from incomplete custody is no evidence | R6.CUST.9, closing paragraph |
| missing custody or unresolved eligibility: FAIL `record-invalid` and `retirement-blocked` | R6.CUST.9 table |
| unreadable or unverifiable required object: ERROR | R6.CUST.9 last row |
| preserve original bytes, paths, objects, lineage, authorization provenance, reviews, corrections, adjudications | R6.CUST.6 mapping (by reference to Git objects reachable from `M`; receipt as provenance) |
| evidence only, no positive repair authority | R6.CUST.2 (no clearing entry type), §7 |
| format, bootstrap and mapping fixed and independently verified before reliance | R6.CUST.2, R6.CUST.3, R6.CUST.6; this design's review and adoption |
| a retained witness names config, freeze, mode, selector, reassessment, finding, repair, edge, `S`, objects, `M`, `REV` | R6.CUST.6 mapping table, row by row |
| `Inapplicable(W)` from retained custody | §4.3 closing paragraph |
| terms read through the verified reader; messages, PR text, logs, verdicts are not inputs | R6.CUST.1, R6.CUST.9 |
| r9 §2.3: a later freeze reusing the disputed repair consults custody | R6.CUST.6, R6.CUST.7 |
| r9 R-1: custody of a prior scope not established leaves discharge inapplicable | R6.CUST.9; R-C1 to R-C3 |
| owner: bootstrap is an independently verified starting inventory | R6.CUST.3, §3 |
| owner: evidence identity by exact paths, Git object ids and finding references | R6.CUST.2 encodings; R6.CUST.6 |
| owner: each successor binds its predecessor | R6.CUST.4 (s1), (s2) |
| owner: retain operative repair inputs, witnesses and later dispositions | R6.CUST.6 (witnesses by reproduction; OQ-2) |
| owner: completeness and object integrity independently verifiable | R6.CUST.5, R6.CUST.9 ERROR row, §3 (b) |
| owner: missing evidence fails closed | R6.CUST.9; (s3), (s4), (c2) |
| owner: custody supplies evidence, never authorization | §7, R6.CUST.2 |
| owner: minimalism, not a second history | §2.3, §4.1 closing paragraph, §7 |
| owner: prefer existing Git objects and verification mechanisms | receipts and `v3_verifier` (c1); verified reader; `record_authority.py` pin; `oi-review-record/1` (R6.CUST.8); side-change classes (R6.CUST.1) |

***

## 9. Open questions for the owner

Each point below is one the r9 text does not settle. The recommended default is what this draft
assumes; none is decided by this draft.

| Id | Question | Recommended default | Alternatives and consequences |
|---|---|---|---|
| OQ-1 | At which `M` is a prior context's qualification replayed? r9 asks for "the exact `M`/source tree" but a freeze may have several runs | the current effective `M` (R-C4) | (a) a reviewed per-context `close` entry fixing the latest run's `M`: closer to r9, but an early bound loses witnesses and is review only; (b) a `run` entry per run with its exact `M`: exact, but run completeness becomes review |
| OQ-2 | Does the record list derived witnesses? | no; witnesses are reproduced each run and reported in the result | a checked cache of witnesses in the record: readable without the tool, but duplicates derived data and must change with any predicate change |
| OQ-3 | Under which rules is a prior context replayed? | the tool revision pinned at the current `F` | the revision pinned at the context's `f`: faithful, but needs a second execution environment per context |
| OQ-4 | How is `rev` completeness established? | review (§5 item 2) | require every op C execution result to land on `main` with its inputs, then check a bijection between results and `rev` entries mechanically; needs a rule outside this design |
| OQ-5 | Is review of `rev`, `unfrozen` and `void` entries evidenced by a review record the tool checks (R6.CUST.8)? | yes | ordinary pull-request review only: no schema change, but item 2 and 3 of §5 become unverifiable from `main` |
| OQ-6 | Are discharge-bearing configurations without a freeze accounted for by `unfrozen` (R6.CUST.5 (c2))? | yes | drop (c2) and `unfrozen`: smaller, but a configuration landed outside a receipted round then goes unaccounted |
| OQ-7 | What procedural precondition orders freezes? | every earlier discharge-bearing freeze, of any retirement, has landed with ancestry and a custody successor before a later one is designated (any retirement, because reliance (r1) crosses retirements) | the same retirement only; or none, accepting R-C1 |
| OQ-8 | Path and constants | `verification/audits/foundations/a1exit-obl29-custody/custody.json`; path and bootstrap blob id in `record_authority.py` | another directory under `verification/audits/`; a path outside it would need a second selector in the walk |
| OQ-9 | Add a release-gate step that checks R6.CUST.2 and R6.CUST.4 on every commit? | no | yes: catches a malformed or regressing successor before it lands rather than at the next run, at the cost of a new gate step |
| OQ-10 | Do harness-admitted runs (no `F`, R6.RECON.21) form contexts? | no; only receipted `chain` freezes | include harness runs: they have no authorized freeze to list |
| OQ-11 | Which commit is `B0`? | the `main` commit designated in the decision adopting the implementing tool revision | the current `main` at adoption of this design |
| OQ-12 | Result fields for custody | add `category3.custody` with the status, `V_M`'s blob id, the contexts and each witness with its route; this is a result-schema change beside R6.OBL29.8 | report custody failures only through the existing `record-invalid` items |
| OQ-13 | Does a custody failure affect the R6.RECON.26 no-edit route? | no (r9 ties custody to "the repair under consideration") | yes: simpler, but blocks retirements that drop the bound edit |
| OQ-14 | Is a custody failure global or per repair? | global to the run's cited discharges | per repair: needs a relevance test that itself depends on the failed replay |

***

## 10. Provenance and references (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7202075726, item 5 | authority, quoted with author and time in §0 | provenance |
| r9 at `77a73c022091f598cf807fcf89d66c3cf43208de` | the source requirements of §2.2 and their definitions | support off `main`: the adopted design is on `design/a1-obl29-remedy-20261126`; it must reach `main` no later than this design |
| #1601 comment 7197486426 | r9's adoption and the token convention | provenance |
| Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e` | R6.CFG.*, R6.RECON.*, R6.REC.* cited here | support off `main` (PR #1593 open) |
| PR #1577 at `aafb052580ea2d07e1b14bfbd00c543417e89206` | the current fail-closed behaviour this design replaces | provenance |
| `origin/main` at `84e927b9b7c2bcc8cb9624cb036167dae233e408` | the drafting measurement of §1; receipts under `verification/receipts/`; `tools/legacy_records_check.py` and `tools/v3_verifier.py` as existing mechanisms | support on `main`; the measurement is a drafting fact to be re-established at `B0` (§3 (b)) |
