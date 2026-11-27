# A1 staging amendment r2, supplement S-1: recorded session identities (paper draft)

**Status.** Draft for independent review and the owner's adoption of the exact reviewed text. It
amends staging amendment r2 (`AMENDMENT.md` in this directory) and the Amendment 6 r13 identity rules,
replacing GitHub-identity requirements with explicitly recorded session identities. Adoption,
implementation, staging, freeze and execution keep their separate gates.

**Authority.** Owner decision (amaybaum, received 2026-11-27, coordinating session; recorded at
#1169 comment 7208869709, 2026-11-27T03:17:51Z), item S-1, quoted:

> S-1: authorize drafting and independently reviewing the staging r2 amendment replacing GitHub-identity requirements with explicitly recorded session identities. Preserve reviewer independence, exact-revision binding and review-scope requirements. Missing or ambiguous identity evidence must disqualify the review. Return for adoption of the exact reviewed amendment.

**Goal link (AGENTS.md §A.47).** Serves A1 retirement (#1169): it would decide how the writer, ordinary
reviewer and widening reviewer of the staging records can be shown distinct when every agent session
commits and writes to GitHub through one account.

## 1. The defect

Staging r2 §2 requires "the independently verified GitHub identity" of each root's actual author and
"distinct eligible identities" for the writer, ordinary reviewer and widening reviewer. r13 R6.RECON.29
defines an identity string as "a GitHub login", and R6.REC.6, R6.REC.13 and the `review.record` key
table compare such strings. All agent sessions use one GitHub account, so a login names no session,
and distinct logins cannot be produced for distinct sessions. A rule that compares logins either
admits nothing or treats self-declared strings as verified.

## 2. Session identities

**S1.1 The session registry.** A session identity is an entry of the session registry: the regular
file `a1-staging-sessions.json` in the admitted A1 plan record directory `D_rec`, pinned by the
R6.REC.16 `PREREG.md` Record pins table of the admitted `F`, beside the transition descriptor of
staging r2 §2. Its bytes are canonical JSON (R6.RECON.29) with closed keys `schema`
(`"oi-a1-staging-sessions/1"`) and `parties`, an array of entries with closed keys:

| Key | Type | Meaning |
|---|---|---|
| `id` | string matching `(session\|person)\.[a-z0-9][a-z0-9-]{1,62}`, its prefix equal to `kind` | the party's identity string, used as `author` and `reviewer`. A GitHub login holds no `.`, so no `id` can equal one |
| `kind` | `"session"` or `"person"` | an agent session, or a person such as the owner |
| `designation` | non-empty string | where the owner designated the party (for example a comment URL); provenance, not read by the tool |
| `same_party` | array of `id` | parties that count as the same party for independence: an interrupted session and its replacement writer (AGENTS.md §A.52), or sessions sharing one context |
| `scope` | array of paths, each a directory prefix | the record paths the party may author or review |

The owner records each designation in an owner record (AGENTS.md §A.42 item 7); the registry lists it
for the tool. Approving `F` approves the pinned registry as part of the plan (R6.REC.3, procedural).
The tool reads the registry only from `F`'s pin table, never from an argument, a commit author, a
GitHub login or a host record.

**S1.2 Well-formed and unambiguous.** The registry fails, and with it every record whose admission
needs an identity, when: it is missing, unpinned or malformed; two entries have equal `id`, or `id`
values equal after Unicode case folding; an `id` does not match its grammar or its prefix differs from
`kind`; or a `same_party` member names no entry. The grammar excludes GitHub logins, URLs, run or
check ids and Issue numbers (R6.REC.6's existing exclusions). `same_party` is read symmetrically and transitively: the party of `x` is the
closure of `x` under it.

**S1.3 What a record binds.** An `author` or `reviewer` value is an identity string only if it equals,
byte for byte, the `id` of exactly one registry entry. A review additionally binds:
- its exact artifact: `reviewed` `{path, blob_sha256}`, as now (R6.RECON.29 reference);
- its revision: a new required key `revision`, a commit id whose tree holds `reviewed.path` at a
  regular mode with bytes hashing to `reviewed.blob_sha256`, and which is `F` or an ancestor of `F`
  (for a review admitted by the post-freeze route, `REV` or an ancestor of it);
- its reviewer session: `reviewer`, resolved in the registry;
- its authorized scope: `reviewed.path` lies under a prefix of the reviewer's `scope`, and the
  reviewed record's path lies under a prefix of its author's `scope`.

**S1.4 Independence.** For a record with author `a`, ordinary review by `r` and, where required,
widening review by `w`: `r` is not in the party of `a`; `w` is in neither the party of `a` nor the
party of `r`; and for the configuration and staging roots, the three are pairwise in distinct parties.
Each comparison is mechanical over the registry. Whether the registry's designations and `same_party`
sets are true is review of the owner's records (§5).

**S1.5 Missing or ambiguous evidence disqualifies.** A review is disqualified (not a review of the
record) when its `reviewer` is not an identity string under S1.3, its `revision` is missing, unreadable
or does not hold the reviewed blob, the reviewed path is outside the reviewer's scope, or S1.2 fails.
A record whose `author` is not an identity string fails record lint. A disqualified review counts as
no review: the reviewed record then lacks its required review and fails with FAIL `record-invalid`
(R6.REC.6). Where a disqualified review carries an invalidation verdict, detection treats it as a
review whose independence cannot be established (R6.RECON.26 Form (i), r9 Amendment 1), so it blocks
rather than lapses. An unreadable required object stays ERROR (R6.REC.17).

## 3. Clauses that change

| Clause | Replacement text |
|---|---|
| staging r2 §2, "One-time transition" | "… and the registered session identity (S-1 §2) of its actual author." in place of "and the independently verified GitHub identity of its actual author." |
| staging r2 §2, "Initial widening review" | "The writer, ordinary reviewer and widening reviewer are registered parties in pairwise distinct parties (S-1 S1.4)." in place of "The writer, ordinary reviewer and widening reviewer are distinct eligible identities." |
| staging r2 §2, "In a later, separately approved activation" | add: "The plan also pins `a1-staging-sessions.json` (S-1 S1.1) in `D_rec` by the same Record pins table." |
| r13 R6.RECON.29, row "identity string" | "`author` and `reviewer`: the `id` of exactly one entry of the session registry admitted at `F` (staging S-1 S1.1), compared byte for byte; not a GitHub login, run, check, Issue or URL (R6.REC.6)." |
| r13 R6.REC.6 | "`reviewer` equal to `author`" reads "`reviewer` in the party of `author` (S-1 S1.4)"; "a `reviewer` value that points to a tool run, a CI run, a check run or an Issue" reads "a `reviewer` or `author` value that is not an identity string (R6.RECON.29), or a review disqualified under S-1 S1.5". |
| r13 R6.REC.13 | "by a non-author reviewer other than the record's own reviewer" reads "by a reviewer in neither the party of the record's author nor the party of its own reviewer (S-1 S1.4)". |
| r13 table `review.record` | add the row: `revision` — commit id — yes — the commit the reviewer read — holds `reviewed.path` with `reviewed.blob_sha256` at a regular mode, and is `F`, `REV` or an ancestor of it (S-1 S1.3). The `reviewer` acceptance reads "not in the party of the reviewed record's `author`; for a widening review, also not in the party of the reviewer of the superseding record's own review". |
| r13 table `migration.approval`, `author` | unchanged in meaning: the owner's registered `id` (kind `"person"`). |

R6.REC.2's statement that a writer may not review its own record, and every item-coverage,
exact-blob and verdict rule of R6.REC.6 and R6.REC.13, are unchanged.

## 4. Tool and review-lint changes (not implemented)

- `engine/records.py`: replace `_person` with a registry lookup (S1.2, S1.3); party closure and the
  S1.4 checks in record lint and in widening-review lint; the `revision` and scope checks of S1.3.
- `engine/config.py` or admission: read and validate `a1-staging-sessions.json` from `F`'s pin table
  (R6.REC.16), once per run; a failure fails every record needing an identity (S1.2).
- Key tables and generator: the `review.record` row `revision`, the identity-string encoding, and
  regenerated conformance mutants (R6.RECON.29) and the generated schema.
- `record_authority.py`: the registry file name as a fixed selector beside the staging selectors.
- Detection (R6.RECON.35, `category3.py`): a review disqualified by S1.5 is classified as one whose
  independence cannot be established, never dropped.
- Custody (R6.CUST.8) and the r9 NR-3 and NR-5 identity comparisons use the same identity strings and
  party relation.

## 5. Controls

Each is a specification until implemented.

| Id | Setup | Expected |
|---|---|---|
| S1-POS | Writer `w1`, ordinary reviewer `r1`, widening reviewer `x1`, distinct parties, each in scope; reviews carry valid `revision` | the root passes record lint |
| S1-UNREGISTERED | The reviewer `id` is in no registry entry | review disqualified; FAIL `record-invalid` for the record |
| S1-LOGIN | `author` and `reviewer` are both the shared GitHub login | FAIL `record-invalid` (not identity strings) |
| S1-SAME-PARTY | `r1` lists `w1` in `same_party` (or a chain `r1 → s → w1`) | review disqualified |
| S1-WIDENING-SAME-PARTY | The widening reviewer is in the ordinary reviewer's party | widening review disqualified; FAIL `record-invalid` |
| S1-AMBIGUOUS-ID | Two registry entries with equal `id` (variant: an entry whose `id` prefix differs from its `kind`) | registry fails; FAIL `record-invalid` for every record needing an identity |
| S1-NO-REGISTRY | The registry is absent from `F`'s pin table, or its bytes differ from the pinned SHA-256 | as S1-AMBIGUOUS-ID |
| S1-REVISION-MISMATCH | `revision` holds `reviewed.path` with other bytes, or is not an ancestor of `F`, or is missing | review disqualified |
| S1-OUT-OF-SCOPE | The reviewed path lies outside the reviewer's `scope` | review disqualified |
| S1-INVALIDATING-DISQUALIFIED | A disqualified review carries `invalidates` on a reconciliation record entry | detected as a provisional block; FAIL `record-invalid` and `retirement-blocked`, not lapsed |
| S1-REPLACEMENT-WRITER | The reviewer is the replacement writer of the author's interrupted session, recorded in `same_party` | review disqualified |

## 6. Open questions for the owner

| Id | Question | Recommended default | Alternative |
|---|---|---|---|
| OQ-S1-1 | Scope of the identity change | every record the tool reads (R6.RECON.29 is global), since one account serves all sessions everywhere | only the staging roots and their reviews, leaving other records on logins that cannot establish independence |
| OQ-S1-2 | Can a session registered after `F` review a post-freeze reconciliation record (R6.RECON.2)? | no: the registry is read from `F` only, so a new reviewer needs a new freeze | admit a registry pinned at `REV`, which would let a post-freeze commit add identities |
| OQ-S1-3 | Is `same_party` enough to capture shared context between sessions? | yes, with the owner recording it in each designation | derive parties from session lineage records outside the registry |
| OQ-S1-4 | Are identity strings authenticated? | no: as r9 R-8 records, the strings are self-declared, and the owner's designations and review of the registry are the guard | a signed attestation per session, a new mechanism needing its own design |

## 7. References (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7208869709, item S-1 | authority, quoted above | provenance |
| `AMENDMENT.md` (staging r2) at `e3fb631ec9c29535f73ee6c180169d794846df67` | the clauses amended | support off `main`; it lands with #1577 |
| r13 R6.RECON.29, R6.REC.2, R6.REC.3, R6.REC.6, R6.REC.13, R6.REC.16 and table `review.record` at `5ad8837521de0a26734266a64f91548fd3dcff1e` | the clauses amended | support on `main` (landed by #1604) |
| r9 Amendment 1 at `e79e7ca90f863115bc75b7ae5195dbba016125da` | the provisional-block treatment of S1.5 | support off `main` until #1601 lands |
| `tools/ledger_coverage/engine/records.py` at `e3fb631ec9c29535f73ee6c180169d794846df67` (`_person`) | the current identity check | provenance (PR #1577) |
