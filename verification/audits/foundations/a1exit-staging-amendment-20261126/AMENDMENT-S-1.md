# A1 staging amendment r2, supplement S-1: recorded session identities (paper draft r5)

**Status.** Draft r5, for independent review and the owner's adoption of the exact reviewed text. r1
at `dae2468ee4ceb7c46df97dba529cc584e620f91a` received REVISE (PR #1620 comment 7208980804), and r2 at
`bfac322211b3e00303154e6cd96247ac1e48e9be` a narrow REVISE (PR #1620 comment 7209044224), and r3 at
`075d68515f5280bde3cc3bec58ce5bff71595278` a further REVISE (PR #1620 comment 7209091683); §9 maps the
reviews' findings to changes. It amends staging amendment r2 (`AMENDMENT.md` in this directory), the
Amendment 6 r13 identity rules, the identity comparisons of r9 and its Amendment 1, and the custody
design's R6.CUST.8, replacing GitHub-identity requirements with explicitly recorded session
identities. Adoption, implementation, staging, freeze and execution keep their separate gates.

**Authority.** Owner decision (amaybaum, received 2026-11-27, coordinating session; recorded at
#1169 comment 7208869709, 2026-11-27T03:17:51Z), item S-1, quoted:

> S-1: authorize drafting and independently reviewing the staging r2 amendment replacing GitHub-identity requirements with explicitly recorded session identities. Preserve reviewer independence, exact-revision binding and review-scope requirements. Missing or ambiguous identity evidence must disqualify the review. Return for adoption of the exact reviewed amendment.

**Goal link (AGENTS.md §A.47).** Serves A1 retirement (#1169): it would decide how the writer, ordinary
reviewer and widening reviewer of the staging records, and the parties of every identity comparison
the tool makes, can be told apart when every agent session commits and writes to GitHub through one
account.

## 1. The defect

Staging r2 §2 requires "the independently verified GitHub identity" of each root's actual author and
"distinct eligible identities" for the writer, ordinary reviewer and widening reviewer. r13 R6.RECON.29
defines an identity string as "a GitHub login", and R6.REC.6, R6.REC.13, R6.RECON.26 Form (i), the
`review.record` table, r9 NR-3 and NR-5, r9 Amendment 1 and R6.CUST.8 compare such strings. All agent
sessions use one GitHub account, so a login names no session. A rule that compares logins either
admits nothing or treats self-declared strings as verified.

## 2. The session registry

**S1.1 Location and form.** The session registry is the regular file `a1-staging-sessions.json` in the
admitted A1 plan record directory `D_rec`, pinned by the R6.REC.16 `PREREG.md` Record pins table of the
admitted `F`, beside the transition descriptor of staging r2 §2. Its bytes are canonical JSON
(R6.RECON.29). Closed keys, all required: `schema` (`"oi-a1-staging-sessions/1"`), `author` (the
writer's `id`, which must itself be an entry), `parties`, an array of entries, and `withdrawn`, an
array, possibly empty, of withdrawals `{id, designation}`. Each entry has these closed keys, all
required:

| Key | Type | Meaning |
|---|---|---|
| `id` | string matching `(session\|person)\.[a-z0-9][a-z0-9-]{1,62}`, prefix equal to `kind` | the party's identity string. A GitHub login holds no `.`, so no `id` equals one |
| `kind` | `"session"` or `"person"` | an agent session, or a person such as the owner |
| `platform_ref` | non-empty string | the platform's session or subagent identifier, which the owner can check against the platform's session list |
| `spawned_by` | an `id` or null | the session that started this one, if any |
| `same_party` | array of `id`, possibly empty | further parties that count as the same party |
| `scope` | non-empty array of paths | directories in which the party may author or review |
| `designation` | non-empty string | the URL of the owner's `oi-designate` form comment that designates this entry (S1.2) |

**S1.2 Root of trust: the owner's own acts.** The root of trust is the owner's own acts, not any
record a session can write. Every session writes to GitHub through the owner's account, so only a
form that an automated writer may not produce is attributable to the owner:
- **Designation.** Each entry's `designation` is the URL of an owner form comment, posted by hand, in
  an admitted thread (below), whose first line is exactly `oi-designate` and whose second line is the
  canonical JSON of the entry without its `designation` key, byte for byte (the comment's own URL
  cannot exist before it is posted). AGENTS.md §A.49 rule 4 bars any automated text whose first line
  begins with `oi-` in a governed thread, so such a comment is the owner's by rule.
- **Withdrawal.** A wrong entry is never edited (S1.5). The owner retires it with a form comment whose
  first line is exactly `oi-withdraw` and whose second line is the entry's `id` (which carries no
  self-reference), posted in an admitted thread; the registry records
  `{id, designation}` in `withdrawn`, with `designation` that comment's URL. A withdrawn `id` is not an
  identity string for any review or record at a freeze whose registry lists the withdrawal. Its links
  stay in the party relation, so withdrawal never makes two parties independent.
- **Admitted threads.** The owner's adoption of this supplement admits `oi-designate` and `oi-withdraw`
  form comments in #1169 and in the guiding pull request named in the owner's adoption record of this supplement, so both are governed threads for
  AGENTS.md §A.49 rule 4. A designation or withdrawal is accepted only from a thread that was admitted
  when the comment was posted.
- **Freeze approval.** The owner's approval of `F` quotes the registry's SHA-256 and states that the
  owner checked each entry's `id`, `platform_ref`, `spawned_by` and `same_party` against the
  platform's session list, and each designation and withdrawal against its form comment.

The registry also has an `oi-review-record/1` (S1.1), by a reviewer outside the party of the
registry's `author`, with items `party:<id>` for every entry and `withdrawn:<id>` for every withdrawal,
which checks each against its form comment before the owner's approval. That review is evidence of
review, not the root of trust: its reviewer and the writer are identified through the registry under
review. The tool checks mechanically that every `designation` is a comment URL in this repository and
that the registry's review exists, binds the registry's exact path and blob, meets §3 with root `F`
and scope over `D_rec`, has a reviewer outside the writer's party, and accepts every item. **One rule
applies:** a missing designation, a review that rejects or omits any item, or any other failure of
this paragraph fails the registry (S1.4); there is no partially usable registry. Whether a comment is
in the owner's form, and whether the owner's approval states the checks above, are procedural
(R6.REC.3) and are recorded in the record that relies on the approval (AGENTS.md §A.42 item 7).

**S1.3 Party.** The party of `x` is the closure of `{x}` under `same_party` and `spawned_by`, each read
in both directions. A spawning lineage is therefore one party unless the owner's `oi-designate`
comment for the spawned entry shows it as independent, by `spawned_by: null` or by omitting the link;
no other owner record shows independence (OQ-S1-3). Two identity strings are
the **same id** when byte-equal; they are in the **same party** when either is in the other's party.

**S1.4 Well-formed and unambiguous.** The registry fails, and with it every review and record whose
admission needs an identity, when: it is missing, unpinned, malformed, or lacks its review (S1.2); two
entries have equal `id`; an `id` breaks its grammar or its prefix differs from `kind`; a `spawned_by`
or `same_party` member, or the `id` of a `withdrawn` element, names no entry; or two entries share a
`platform_ref`. (The grammar admits only
lowercase ASCII, so case folding cannot make two distinct ids equal; no control is claimed for it.)

**S1.5 Append-only across freezes.** Where staging r2's `a1-staging-prior.json` names a non-null
`F_prev`, the registry admitted at `F_prev`, read from `F_prev`'s pin table, is the prior registry.
Every prior entry and withdrawal appears in the registry at `F` byte-identical as a canonical JSON
element; and the
party relation restricted to ids registered at `F_prev` is the same at `F`, so a new entry may join one
existing party but may not link two existing parties, and no existing entry gains a link. A failure
fails the registry (S1.4).

**S1.6 Scope.** A path is under a scope entry when the entry's components are a prefix of the path's
components, compared whole (`a/b` covers `a/b/c`, not `a/bc`); the repository root is not a valid scope
entry. A record's path is under its author's scope; a review's `reviewed.path` and the review file's
own path are under its reviewer's scope. Scope only narrows what a party may do. It never establishes
independence, which S1.7 decides. The owner's "review-scope requirements" are the item-coverage rules
of R6.REC.6 and R6.REC.13, which this supplement keeps.

**S1.7 Independence.** For a record with author `a`, ordinary reviews by `r`, and, where required, a
widening review by `w`: no `r` is in the party of `a`; `w` is in neither the party of `a` nor the party
of any ordinary reviewer of the superseding record; and for the configuration and the staging roots,
the three are in pairwise distinct parties. Each comparison is mechanical over the registry.

## 3. What a review binds

A review binds:
- its exact artifact: `reviewed` `{path, blob_sha256}`, as now;
- its revision: a required key `revision`, a commit id that is reachable, through any parent, from the
  root the review is read from, and whose tree holds `reviewed.path` at a regular mode with bytes
  hashing to `reviewed.blob_sha256`. The root is `F` in chain record lint; `REV` for a review read by
  the post-freeze route; effective `M` (or `F` and `REV` where the walk reaches them) for a review
  found in `R*` by detection and finding lookups (R6.OBL29.1–.3); and effective `M` for a custody
  review read from `Vers(M)` (R6.CUST.8). A review written after `F` is therefore bound to a commit it
  can name, and custody versions added after `F` stay reviewable;
- its reviewer: `reviewer`, an identity string (R6.RECON.29 as amended);
- a consistency check: a required key `platform_ref`, equal to the reviewer's registry entry's
  `platform_ref`;
- its authorized scope (S1.6).

The reviewing session also posts the review file's blob SHA-256 on the guiding pull request named in the owner's adoption record of this supplement; the tool
does not read it. The review-level `platform_ref` and the posted digest are consistency checks, not
identity evidence: any session can copy a registered `platform_ref`, and the post is written through
the shared account. Identity evidence is the entry-level `platform_ref` as checked by the owner against
the session list (S1.2). **Residual limit**, in
R6.REC.12's words: "The tool can check that the role fields differ, not who actually wrote the
records; identity rests on the writer's and the reviewer's own recorded statements." The owner's
designations and freeze approval fix which sessions exist and how they relate; they do not show which
session wrote a given review, and this supplement does not narrow that limit (OQ-S1-4).

## 4. Missing or ambiguous evidence

**S1.8 In record lint** (R6.REC.6, R6.REC.13, R6.CUST.8). A review is disqualified, and counts as no
review, when its `reviewer` is not an identity string, its `revision` or `platform_ref` fails §3, a
path is outside scope, its reviewer is in the party of the reviewed record's author, or the registry
fails. The reviewed record then lacks its required review and fails with FAIL `record-invalid`. A
record whose `author` is not an identity string fails record lint.

**S1.9 In detection** (R6.RECON.26 Form (i), r9 Amendment 1). A review carrying `invalidates` or
`invalidated` never lapses through doubt about identity:
- it is disqualified, carrying no finding, only when its `reviewer` is the same id as the `author` of
  the record its `reviewed` names, with that record in `R*`;
- when that record is absent from `R*`, it is a provisional block (Amendment 1);
- when that record is in `R*` and the reviewer is in the author's party but not the same id, or is not
  an identity string, or the registry fails, or `revision` or `platform_ref` fails, it is a genuine
  finding with a form failure: it binds, belongs to `Obl` under A1.1 where the record has a durable
  witness in `M`'s ancestry, and needs a repair to be discharged (Keys (b) does not apply, since the
  record is present).

**For the owner.** An invalidating review whose `reviewer` is not an identity string (unregistered,
withdrawn, or malformed) is a permanent block: no `Z` can meet r9 NR-5's resolver for it, route 2 does
not exist, and a repair-bearing reassessment still faces the review witness. Only dropping the bound
edit from the plan (R6.RECON.26) lifts it. This fails closed by design.

An unreadable required object stays ERROR (R6.REC.17, R6.OBL29.7).

## 5. Clauses that change

| Clause | Replacement text |
|---|---|
| staging r2 §2, "One-time transition" | "… and the registered identity (S-1 §2) of its actual author." in place of "and the independently verified GitHub identity of its actual author." |
| staging r2 §2, "Initial widening review" | "The writer, ordinary reviewer and widening reviewer are in pairwise distinct parties (S-1 S1.7)." in place of "… are distinct eligible identities." |
| staging r2 §2, "In a later, separately approved activation" | add: "The plan also pins `a1-staging-sessions.json` and its review (S-1 S1.1, S1.2) in `D_rec` by the same Record pins table, and the owner's approval of `F` quotes the registry's SHA-256." |
| staging r2 §2, "Prior-freeze continuity" | add: "The tool also checks S-1 S1.5 against the registry at `F_prev`." |
| r13 R6.RECON.29, row "identity string" | "`author` and `reviewer`: the `id` of exactly one entry of the session registry admitted at `F` (staging S-1), compared byte for byte (same id); not a GitHub login, run, check, Issue or URL. Party relations are those of S-1 S1.3." |
| r13 R6.RECON.29, conformance mutants | add near-miss mutants for an identity string: a bare GitHub login, an `id` whose prefix differs from the entry's `kind`, an upper-case `id`, and an `id` absent from the registry, beside the existing URL mutant. |
| r13 R6.REC.6 | "`reviewer` equal to `author`" reads "`reviewer` in the party of `author` (S-1 S1.3)"; "a `reviewer` value that points to a tool run, a CI run, a check run or an Issue" reads "an `author` or `reviewer` value that is not an identity string (R6.RECON.29), or a review disqualified under S-1 S1.8". |
| r13 R6.REC.13 | "by a non-author reviewer other than the record's own reviewer" reads "by a reviewer in neither the party of the record's author nor the party of any ordinary reviewer of the record (S-1 S1.7)". |
| r13 R6.RECON.26 Form (i) | "unless its independence fails: its `reviewer` equals the `author` of the record its `reviewed` names (R6.RECON.29), or is a run, check or Issue (R6.REC.6). Only such an independence failure disqualifies it" reads "unless its `reviewer` is the same id as the `author` of the record its `reviewed` names (S-1 S1.3). Only that disqualifies it. A reviewer in that author's party but not the same id, a reviewer that is not an identity string, or a failed registry, `revision` or `platform_ref`, is a form failure that still blocks (S-1 S1.9)." The provisional-block clause of r9 A1.5 follows. |
| r13 table `review.record` | add rows `revision` (commit id, required, the commit the reviewer read; acceptance as S-1 §3) and `platform_ref` (non-empty string, required; equals the reviewer's registry entry). The `reviewer` acceptance reads "not in the party of the reviewed record's `author`; for a widening review, also not in the party of any ordinary reviewer of the superseding record". |
| r13 R6.RECON.33, kind table | add the row `sessions` — `oi-a1-staging-sessions/1`. The registry is admitted from `F`'s pin table (S-1 S1.1); where the configuration's `records` also lists it, the reference must equal the pinned path and blob, as for `roles.side_change_classes`; otherwise ERROR `CONFIG_INVALID`. |
| r13 R6.RECON.31, item-id table | add the row for `oi-a1-staging-sessions/1`: item ids `party:<id>` for each entry of `parties` and `withdrawn:<id>` for each withdrawal. Its review meets S-1 §3 with root `F` and scope over `D_rec`. |
| r13 table `migration.approval`, `author` | acceptance: "the `id` of a registry entry of kind `"person"` designated as the owner" (a registry id in place of a login). |
| r9 Amendment 1, genuine finding (§1) and A1.1 | "whose `reviewer` differs, as an identity string (R6.RECON.29), from that record's `author` and is not a run, check or Issue" reads "whose `reviewer` is not the same id as that record's `author` (S-1 S1.3); a reviewer in the author's party, or one that is not an identity string, makes it a genuine finding with a form failure (S-1 S1.9)". |
| r9 Amendment 1, A1.2 | "shows `author` equal to `reviewer`" reads "shows `author` the same id as `reviewer`". |
| r9 Amendment 1, A1.5 | "is disqualified if its `reviewer` equals that record's `author`" reads "is disqualified if its `reviewer` is the same id as that record's `author` (S-1 S1.3)". |
| r9 NR-3 | "Its `reviewer` differs, as identity strings (R6.RECON.29), from the `author` of …, and from the `reviewer` of …" reads "Its `reviewer` is in none of the parties (S-1 S1.3) of the `author` of …, and of the `reviewer` of …". |
| r9 NR-5, Resolver | "`Z`'s `reviewer` equals `V`'s `reviewer` as identity strings (R6.RECON.29) and differs, as identity strings, from the `author` of `R`, of the disputed record and of the cited reassessment" reads "`Z`'s `reviewer` is the same id as `V`'s `reviewer` and is in none of the parties of the `author` of `R`, of the disputed record and of the cited reassessment (S-1 S1.3)". |
| custody R6.CUST.8 | "whose `reviewer` differs as an identity string from the version's `author`" reads "whose `reviewer` is in no party of the version's `author` (S-1 S1.3), and which meets S-1 §3 with root effective `M`". |

R6.REC.2's statement that a writer may not review its own record, and every item-coverage,
exact-blob and verdict rule of R6.REC.6 and R6.REC.13, are unchanged.

**Registry source for controls.** For an R6.EVID.8 representative control at a reviewed snapshot `S`,
the registry is read from `S`'s pin table under the same descriptor. An in-process harness control
(R6.RECON.21) reads the registry from the control-supplied configuration's directory at the commit the
configuration is read from; a synthetic fixture supplies its own registry among its test objects. In
no case is the registry taken from an argument, a commit author or a host record.

## 6. Effect on existing records (OQ-S1-1)

Inventory at `origin/main` `13c05b4fe666c2e128eed1213874be9b8208982d` and
`origin/tools/a1-ledger-coverage-r6` `27ee940c`: no file under `verification/audits/` has schema
`oi-review-record/1`, `oi-reconciliation/2` or `oi-reassessment/1`, so no review, finding or witness in
`R*` is disqualified, and no custody record exists yet. The records the tool reads that carry `author`
are, on the tool branch: `oi-side-change-classes/1` v1–v21, `oi-term-rules/2` (`dr-deny-v1`,
`register-infinity-params-v1`, `resid-v1`, `w1-w2-allow-v1` to `v3`), `oi-hit-classification/1` v1–v3,
`oi-scope/1` `repo-scope-v1`, `oi-delegation/1` and `oi-a1-controls/1`. Their `author` values are
`implementation-writer-20261123` or free text naming a replacement writer, none an identity string, and
none has an `oi-review-record/1`. Under the global default each fails record lint for its author as
well as for its missing review, which it already fails. Staging r2 already replaces the class and allow
lineages with new reviewed roots; the hit-classification, scope, delegation and controls records need
new reviewed versions written under the registry before any freeze uses them. No historical adverse
review witness exists, so none is stranded on route 2.

## 7. Tool and review-lint changes (not implemented)

- `engine/records.py`: replace `_person` with a registry lookup; the party closure (S1.3); S1.7 in
  record and widening-review lint (including "any ordinary reviewer", as `reviewers_of` reads); the
  `revision`, `platform_ref` and scope checks with the root of §3.
- Admission: read and validate the registry and its review from `F`'s pin table once per run, and
  S1.5 against `F_prev`.
- Detection (`category3.py`): S1.9's three outcomes, with lapse only on same id.
- Custody (`custody.py`) and the r9 predicates (`obl29.py`): the replacement comparisons of §5.
- Key tables, generator and conformance mutants (R6.RECON.29), and the generated schema.
- `record_authority.py`: the registry file name as a fixed selector.

## 8. Controls

Each is a specification until implemented.

| Id | Setup | Expected |
|---|---|---|
| S1-POS | Writer `w1`, ordinary reviewer `r1`, widening reviewer `x1` in distinct parties, each in scope, reviews with valid `revision` and `platform_ref`, registry reviewed | the root passes record lint |
| S1-UNREGISTERED | The reviewer `id` is in no registry entry | review disqualified; FAIL `record-invalid` |
| S1-LOGIN | `author` and `reviewer` are both the shared GitHub login | FAIL `record-invalid` (not identity strings) |
| S1-SAME-PARTY | `r1` lists `w1` in `same_party` | review disqualified |
| S1-SAME-PARTY-REVERSED | `w1` lists `r1` (the link only in the other direction) | review disqualified |
| S1-SAME-PARTY-CHAIN | `r1 → s → w1` through `same_party` | review disqualified |
| S1-SPAWNED | `r1.spawned_by` is `w1` | review disqualified |
| S1-MISSING-LINK | `r1` was spawned by `w1` but its entry has `spawned_by: null`; the registry review finds the mismatch against the owner's form comment | registry review rejects the item; registry fails; every dependent review disqualified |
| S1-WIDENING-SAME-PARTY | The widening reviewer is in an ordinary reviewer's party | widening review disqualified; FAIL `record-invalid` |
| S1-WIDENING-AUTHOR-PARTY | The widening reviewer is in the author's party | widening review disqualified; FAIL `record-invalid` |
| S1-DANGLING-LINK | A `same_party` or `spawned_by` member, or a `withdrawn` element's `id`, names no entry | registry fails |
| S1-DUP-ID | Two entries with equal `id`; variant: an `id` whose prefix differs from its `kind`; variant: two entries share `platform_ref` | registry fails; FAIL `record-invalid` for every record needing an identity |
| S1-NO-REGISTRY | The registry is absent from `F`'s pin table, differs from the pinned SHA-256, or lacks its accepting review | registry fails |
| S1-REGISTRY-BY-ARGUMENT | A registry is supplied by argument, or identities are derived from commit authors, with none pinned at `F` | ignored; registry fails |
| S1-DESIGNATION | An entry's `designation` is empty or not a comment URL in this repository; variant: the registry review rejects the item for a mismatch with the form comment | registry fails; every review and record needing an identity disqualified |
| S1-WITHDRAWN | The registry at `F` lists a withdrawal of `r2`; a review by `r2` | review disqualified; an invalidating review by `r2` blocks permanently (S1.9) |
| S1-WITHDRAWAL-KEEPS-LINKS | `r2` was in `w1`'s party and is withdrawn; a review by `r3`, linked to `w1` only through `r2` | still in `w1`'s party; review disqualified |
| S1-WITHDRAWAL-REMOVED | A withdrawal listed at `F_prev` is absent at `F` | registry fails (S1.5) |
| S1-REGISTRY-REVIEW-PARTIAL | The registry review accepts every `party:` item but omits a `withdrawn:` item | registry fails |
| S1-PLATFORM-REF | A review's `platform_ref` differs from its reviewer's entry, or is missing | review disqualified |
| S1-REGISTRY-CHANGED | Between `F_prev` and `F`: an entry removed, an entry edited, or a new entry linking two existing parties | registry fails (S1.5) |
| S1-REVISION-MISMATCH | `revision` holds `reviewed.path` with other bytes, is unreachable from the review's root, or is missing | review disqualified |
| S1-REVISION-POST-F | A custody review and a post-`F` finding review, each with `revision` a commit reachable from effective `M` holding the reviewed blob | both bind normally (custody review counts; finding detected) |
| S1-SCOPE-BOUNDARY | Scope `a/b`; reviewed path `a/bc/x.json` | review disqualified (out of scope) |
| S1-OUT-OF-SCOPE | The review file's own path lies outside the reviewer's scope | review disqualified |
| S1-INVALIDATING-SAME-ID | An invalidating review whose `reviewer` is the same id as the named record's `author`, record in `R*` | disqualified; no finding |
| S1-INVALIDATING-SAME-PARTY | As above, but the reviewer is in the author's party and not the same id | genuine finding with a form failure; FAIL `record-invalid` and `retirement-blocked` |
| S1-INVALIDATING-UNREGISTERED | As above, but the reviewer is not an identity string | genuine finding with a form failure; FAIL `record-invalid` and `retirement-blocked` |
| S1-RETRO-MERGE | A finding is genuine at `F_prev`; a later registry would link its reviewer and author | the later registry fails S1.5; the finding keeps binding |

## 9. Review of r1: findings and changes

| Finding | Change in r2 |
|---|---|
| 1. `revision` versus custody and detection | §3 anchors `revision` to the root the review is read from (`F`, `REV`, effective `M`, custody `Vers(M)`); S1.9 states the Amendment 1 state of each post-`F` finding review; S1-REVISION-POST-F |
| 2. Comparisons not restated | §5 restates Form (i), r9 A1 (§1, A1.1, A1.2, A1.5), NR-3, NR-5 and R6.CUST.8, each as same id or same party |
| 3. Retroactive merge | lapse only on same id (S1.9, Form (i)); registry append-only across freezes (S1.5); S1-RETRO-MERGE, S1-REGISTRY-CHANGED |
| 4. Bootstrap circularity | S1.2: the owner as root of trust, designations stating entries verbatim, a non-writer registry review before `F`, the `F` approval quoting the registry SHA-256; S1-DESIGNATION, S1-NO-REGISTRY |
| 5. Authorship evidence | `platform_ref` in entries and reviews; the posted digest; the R6.REC.12 residual quoted (§3); S1-PLATFORM-REF |
| 6. `same_party` | all keys required; `spawned_by` in the closure; spawning lineage one party by default (S1.3, OQ-S1-3); S1-SPAWNED, S1-MISSING-LINK |
| 7. Scope | whole-component matching, root excluded, review file path checked, scope never establishes independence (S1.6); S1-SCOPE-BOUNDARY |
| 8. Inventory | §6 |
| 9. Minor | case-folding claim withdrawn from controls (S1.4); near-miss mutants (§5); "any ordinary reviewer" (S1.7, §5); `migration.approval` acceptance as kind person (§5); registry source for snapshots and harness controls (§5) |
| 10. Controls | S1-REPLACEMENT-WRITER replaced by S1-SPAWNED and S1-MISSING-LINK; "provisional block" corrected (S1-INVALIDATING-*); the listed missing controls added |

**Re-review of r2 (PR #1620 comment 7209044224):**

| Finding | Change in r3 |
|---|---|
| N1. Designations not attributable | S1.2: designations and withdrawals are owner form comments posted by hand (`oi-designate`, `oi-withdraw`), attributable by AGENTS.md §A.49 rule 4; the `F` approval quotes the SHA-256 and states the owner's check of each entry against the platform's session list; the registry review is evidence of review, not the root of trust; OQ-S1-5 default changed |
| N2. `platform_ref` overstated | §3: the review-level `platform_ref` and the posted digest are consistency checks; the residual limit is not narrowed |
| N3. Entry unusable or registry fails | one rule: any rejected or omitted item fails the registry (S1.2, S1-DESIGNATION); a narrow append-only withdrawal (S1.2, S1.5); S1-WITHDRAWN, S1-WITHDRAWAL-KEEPS-LINKS, S1-WITHDRAWAL-REMOVED, S1-REGISTRY-REVIEW-PARTIAL |
| N4. Schema plumbing | §5 adds the R6.RECON.33 kind row and the R6.RECON.31 item-id row; the registry review meets §3 |
| N5. Permanent self-inflicted block | S1.9 states it for the owner |

**Re-review of r3 (PR #1620 comment 7209091683):**

| Finding | Change in r4 |
|---|---|
| R3-1. Self-referencing designation | S1.2: the `oi-designate` second line is the canonical JSON of the entry without its `designation` key; `oi-withdraw` carries only the `id`, with no self-reference, so it is unchanged; OQ-S1-5 aligned |
| R3-2. Governed threads | S1.2 "Admitted threads": adoption of S-1 admits the form comments in #1169 and the named guiding pull request; a comment is accepted only from a thread admitted when it was posted |
| R3-3. OQ-S1-4 | default aligned with §3: S-1 does not narrow the R6.REC.12 residual limit |
| R3-4. Independence from a spawning session | S1.3 and OQ-S1-3: shown only by the owner's `oi-designate` comment for that entry |
| R3-5. Dangling withdrawal | S1.4 and S1-DANGLING-LINK |

**The r4 delta re-review (PR #1620 comment 7209127764, accepted with nits):** r5 names the guiding pull request as the one named in the owner's adoption record of this supplement (S1.2, §3, OQ-S1-5) and adds the r3 and r4 reviews to §11.

## 10. Open questions for the owner

| Id | Question | Recommended default | Alternative |
|---|---|---|---|
| OQ-S1-1 | Scope of the identity change | every record the tool reads; §6 shows no review, finding or witness is lost, and the affected records already lack reviews | only the staging roots and their reviews, leaving other records on logins that cannot establish independence |
| OQ-S1-2 | Can a party registered after `F` review a post-freeze reconciliation record? | no: the registry is read from `F` only | admit a registry pinned at `REV`, which would let a post-freeze commit add identities |
| OQ-S1-3 | Which sessions count as one party? | a spawning lineage (`spawned_by`) and the owner's `same_party` links, unless the owner's `oi-designate` comment for the spawned entry shows it as independent (`spawned_by: null` or the link omitted) | `same_party` only, leaving undeclared spawning links undetected |
| OQ-S1-4 | Are identity strings authenticated? | no; S-1 does not narrow the residual limit of R6.REC.12 (§3) | a signed attestation per session, a new mechanism needing its own design |
| OQ-S1-5 | Which owner records count as designations and withdrawals? | owner form comments posted by hand, first line `oi-designate` (then the entry's canonical JSON without its `designation` key) or `oi-withdraw` (then the `id`), in #1169 or the guiding pull request named in the owner's adoption record of this supplement; attributable to the owner by AGENTS.md §A.49 rule 4 | any owner record linked from the guiding pull request, which a session could also write through the shared account |

## 11. References (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7208869709, item S-1 | authority, quoted above | provenance |
| PR #1620 comments 7208980804, 7209044224, 7209091683 and 7209127764 | the reviews answered in §9 | provenance |
| AGENTS.md §A.49 rule 4 on `main` | attribution of owner form comments | support on `main` |
| `AMENDMENT.md` (staging r2) at `e3fb631ec9c29535f73ee6c180169d794846df67` | the clauses amended | support off `main`; it lands with #1577 |
| r13 R6.RECON.26, R6.RECON.29, R6.REC.2, R6.REC.3, R6.REC.6, R6.REC.12, R6.REC.13, R6.REC.16, tables `review.record` and `migration.approval`, at `5ad8837521de0a26734266a64f91548fd3dcff1e` | the clauses amended | support on `main` (landed by #1604) |
| r9 `DESIGN.md` (NR-3, NR-5) and `AMENDMENT-1.md` at `e79e7ca90f863115bc75b7ae5195dbba016125da` | the clauses amended | support on `main` (landed by #1601, merge 13c05b4f) |
| custody design R6.CUST.8 (`design/obl29-custody-20261126`, PR #1616) | the clause amended | support off `main` until #1616 lands |
| `engine/records.py` (`_person`, `reviewers_of`) at `e3fb631ec9c29535f73ee6c180169d794846df67` | the current identity checks | provenance (PR #1577) |
