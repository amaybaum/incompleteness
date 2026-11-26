# Formal adjudication of retained witnesses (paper design r1)

## 0. Status, authority, scope and goal link

**Status.** Paper design r1. Not adopted. It changes no schema, admission rule, requirement,
expectation, tool, configuration or record. The proposed requirements (ids `R6.ADJ.n`) have no
force. They would take effect only through a separate owner decision, and then only through the
amendments that §6 lists. Implementation, freeze, trial, dispatch and merge are not authorized
(AGENTS.md §A.50, §A.51 item 6). OBL-29 remains blocking, and A1 retirement remains unauthorized.

**Authority.** Owner decision, amaybaum, received 2026-11-26T16:17Z, recorded at #1169 comment
7197443528, item 1, quoted:

> 1\. Formal adjudication design: Authorize a separate, bounded paper-only investigation, comparing
> the three proposed alternatives, satisfying all seven requirements and including positive and
> negative controls. Require independent non-author review.

The same decision, quoted: "No schema modification, admission-rule modification, implementation,
freeze, trial, dispatch or merge is authorized by this decision. OBL-29 remains blocking, and A1
retirement remains unauthorized." and "Return for a separate decision after the adjudication design
receives independent review." Item 2 of the same decision governs the token convention used in §5.4:
"Tokens establish evidence identity, never adjudication authority."

The seven requirements, as the recording comment lists them:

| Id | Requirement |
|---|---|
| RQ1 | explicit, verifiable authorization of an independent adjudicator |
| RQ2 | independence and conflict-of-interest rules |
| RQ3 | exact binding to the original finding, the disputed evidence and the proposed resolution |
| RQ4 | substantive resolution, not administrative override |
| RQ5 | preservation of the original finding and its full history |
| RQ6 | fail-closed handling of missing, ambiguous or contradictory evidence |
| RQ7 | a clearance path usable when the original reviewer is unavailable or disputes the resolution |

The three alternatives: (A) a dedicated adjudication record kind; (B) a schema extension of existing
records; (C) an amendment to the existing admission rules. The owner prefers an explicit, typed
mechanism over free-text fields that carry authorization meaning; the smallest sound solution decides.

**Base.** Adopted Amendment 6 r13 at `5ad8837521de0a26734266a64f91548fd3dcff1e`
(`verification/audits/foundations/a1exit-design-r6-20261125/`, PR #1593, adopted at #1593 comment
7193277489), cited here as r13. OBL-29 remedy r9 at `77a73c022091f598cf807fcf89d66c3cf43208de`
(`verification/audits/foundations/a1exit-obl29-remedy-20261126/`, PR #1601), conditionally adopted by
item 3 of the authority above, cited here as r9. The gap: the r8 review, #1601 comment 7197262397,
finding 4. Repository state: `main` at `942bd5ea1fd09f4223012b0755bce2d6da07c44a`.

**Goal link (AGENTS.md §A.47).** Serves A1 retirement (#1169) and its blocker OBL-29 (#1598). The
design decides which mechanism, if any, can give r9's route 2 (`Adjudicated(W)`) an admitted,
fail-closed form, and which of the seven requirements no mechanism can meet under r13's R6.REC.3.

**Scope.** Retained witnesses of r9 §2.2 (review witnesses and lineage witnesses) and the predicate
`Adjudicated(W)` of r9's decision. Out of scope: adjudication that withdraws or narrows a category-3
finding itself (the "mistaken independent finding" row of r9 §5.6), which is OD-5 below.

***

## 1. The problem

r9 §2.2 retains a witness `W` against a disputed repair basis. A discharge that relies on that basis
is blocked until `W` is cleared. For a review witness (an adverse or failed review `V` of the
disputed record `Q`), r9 offers two clearances that existing records can carry:

- `Inapplicable(W)`: the original qualification does not reproduce from custody (mechanical);
- NR-5: `V`'s own reviewer resolves `V` explicitly in a review `Z` of the replacement `R`.

Route 2 (`Adjudicated(W)`) requires "properly authorized and independently reviewed adjudication".
r9 shows that no key of r13's closed tables records an adjudicator's authorization, and that
R6.RECON.33 admits no authorization record. So an accepting review of `R` by anyone other than `V`'s
reviewer cannot be told apart from reviewer substitution, and route 2 is unavailable. When `V`'s
reviewer is unavailable, refuses or has an unusable identity, the witness can never clear. Every
discharge of the finding with a non-null repair is then blocked through (r3), and retirement can only
drop the bound edit (R6.RECON.26). This fails closed, but it does not meet RQ7.

**The structural constraint.** r13 R6.REC.3: the owner's approval of a record, a configuration, `F`
or a landing is given under AGENTS.md and quoted in the record that relies on it; "The tool neither
reads nor checks it, and no record kind, field, comment or host read represents it." R6.CFG.4 names
`oi-owner-authorization/1` as an example of an undefined record kind (ERROR `CONFIG_INVALID`). The
edit-id migration record carries an `approval` quotation checked "for form only (R6.REC.3)"
(R6.RECON.28, R6.RECON.32). That quotation is the one existing case of a typed field that quotes the
owner. Its reading, which this design follows, is that a quotation may be carried for the reviewer
and checked for form, but does not establish approval to the tool.

**The design question.** A freeze that pins a substituted reviewer must not be indistinguishable
from one that pins an authorized adjudicator. §2 asks what the tool can distinguish at all.

***

## 2. What can be made mechanically verifiable

### 2.1 The impossibility

**Claim I.** Under R6.REC.3, none of (A), (B) or (C) makes the owner's authorization of an
adjudicator mechanically verifiable.

*Argument.* The tool decides from git objects alone: the trees of `M`, `F`, any `REV`, the
cumulative set `R*` of r9 R6.OBL29.1, and the records the freeze pins (R6.REC.17). Every such object
can be written by any party with push access to a branch whose content later reaches `main`.
Reaching `main` is gated by the owner's merge approval (AGENTS.md §A.50 item 1), which the tool does
not read (R6.REC.3, R6.OUT.14). Records carry identity strings that are self-declared and not
authenticated (r9 R-8). So for any set of bytes that an authorized adjudication would produce, a
substitute can produce the same bytes, changing only who actually wrote them, which no byte records.
Two freezes with equal bytes get equal verdicts. The tool can tell an authorized freeze from a
substituted one only if some byte the tool reads can be produced only by an authorized party. That
requires authenticated identity: a signature checked against a pinned key, or a host read of the
owner's own record. R6.REC.3 excludes both, and AGENTS.md §A.42 item 2 excludes a host comment as
the sole support of an enduring claim. The argument depends on R6.REC.3 and on unauthenticated
identity strings, not on the choice among (A), (B) and (C).

### 2.2 What can be made mechanical

Claim I bounds what any alternative achieves. Within it, a mechanism can make these properties
mechanical, so that substitution needs a forgery that is recorded permanently and visible to the owner:

| Id | Property | Mechanical check |
|---|---|---|
| M1 | Explicitness | A typed authorization object exists, bound to this dispute. A freeze without one is distinguished from one with one. |
| M2 | Owner attribution | The authorization's `author` is a member of a tool constant `OWNER_IDENTITIES`, pinned with the tool files (as R6.RDIR.2 pins the admitted record directories). An authorization attributed to anyone else fails. |
| M3 | Scope equality | The authorization names the adjudicator, the finding and the witness, and these equal the adjudication's own. An authorization for another person or dispute fails. |
| M4 | Independent review of the authorization | The authorization is an item of the adjudication, so a non-author technical reviewer must accept it under R6.REC.6. That reviewer checks the quotation against the owner's record. |
| M5 | Landing before reliance | The adjudication and its review are on `main` (on `M`'s first-parent chain) before the freeze that cites them. They therefore passed an owner-approved merge, at which the owner sees a quotation of the owner's own words. |
| M6 | Conflict rules | Mechanical identity-string exclusions (§5.3). |
| M7 | Permanence | The adjudication, its authorization and every review stay in `R*` (r9 R6.OBL29.1), so a forgery cannot be withdrawn without trace. |

**Distinguishability of substitution.** The table states which attempts the tool distinguishes.

| Attempt | Distinguished mechanically? |
|---|---|
| S1. A substitute's accepting review of `R`, with no adjudication record | yes: NR-5 fails (reviewer is not `V`'s), and `Adjudicated(W)` is false |
| S2. An adjudication record without an authorization object | yes (M1) |
| S3. An authorization attributed to a non-owner identity | yes (M2) |
| S4. An authorization naming another adjudicator, finding or witness | yes (M3) |
| S5. A forged authorization that the technical reviewer rejects | yes (M4) |
| S6. A forged authorization accepted by a colluding technical reviewer and landed through an owner-approved merge | **no**: residual R-ADJ-1 |
| S7. A party writing under the adjudicator's identity string | **no**: residual R-ADJ-2 (r9 R-8) |

So the substitution case that remains needs a fabricated quotation of the owner, a second party's
false acceptance of it, and an owner-approved merge that shows it. All three stay on `main`.

### 2.3 Strengthenings assessed

The brief asked about three strengthenings: an authorization record that itself needs independent
review, a pinned registry of adjudicators reviewed at the freeze, and a quorum. A fourth, an
authenticated channel, is the only one that changes Claim I.

| Strengthening | Effect on substitution | Cost and reachability | Assessment |
|---|---|---|---|
| Separate authorization record kind, by an author other than the adjudicator, with its own non-author review, landed before the adjudication | S6 needs two colluding reviewers plus a false author instead of one reviewer | a second record kind, key tables and item-id row; one more landing | Marginal gain over M4. Not recommended as the default. OD-3 (c). |
| Pinned adjudicator registry as a tool constant `ADJUDICATORS` | S6 additionally needs a tool revision that adds the substitute, reviewed and landed under owner approval | every appointment is a tool revision. A "pre-dispute" variant (registry of the tool pinned at the original freeze) also stops post-hoc choice, but leaves no adjudicator for any dispute that arose before the registry, including every current A1 dispute | Raises the bar. The pre-dispute variant fails RQ7 for existing disputes. OD-3 (b). |
| Registry pinned in the configuration | none: the configuration is written by the plan side and admitted by the same freeze that would pin a substitute (r8 review, finding 4) | a closed-key change to `oi-retirement-config/1` | Unsound. Rejected. |
| Quorum of k ≥ 2 independent technical reviewers | S6 needs k colluding reviewers. Gives no authorization | k reviews per adjudication | Not a substitute for RQ1. May be added. OD-3 (d). |
| Authenticated channel: an owner signature on the adjudication's commit or a signed tag, checked against a pinned owner key; or a host read of the owner's comment | the only option that makes S6 and the owner-attribution part of S7 mechanically distinguishable | changes R6.REC.3; key custody and rotation; a host read also conflicts with §A.42 item 2 and with offline replay (R6.OUT.15) | Outside the three alternatives. OD-3 (e). Not recommended without an owner decision on R6.REC.3. |

Merge commits made through the host on `main` carry the host's own signature (for example
`942bd5ea`). That signature authenticates the host's merge, not the owner's identity, so it does not
change Claim I.

***

## 3. The alternatives against the seven requirements

The alternatives as investigated:

- **(A) Dedicated record kind.** A new reviewed, immutable kind `oi-adjudication/1`, written by the
  adjudicator, carrying typed bindings, a typed authorization quotation, per-item grounds and a
  disposition. It is reviewed under the ownership chain of r13 sec. 11, landed on `main`, and pinned
  by the citing freeze with kind `adjudication`.
- **(B) Schema extension of existing records.** (B1) An `adjudication` object added to
  `oi-review-record/1` (in the record or in a verdict entry), so that an adjudicator's review of `R`
  carries the adjudication. (B2) Adjudication keys added to `oi-reassessment/1`, extending the
  `repair: null` route.
- **(C) Amendment to the admission rules, no new keys.** (C1) The freeze's owner approval is taken as
  the authorization of whatever reviews it pins. (C2) A quorum of independent reviews of `R` carrying
  the NR-5 tokens replaces `V`'s reviewer. (C3) A tool-constant registry: a review of `R` with the
  NR-5 tokens by a registry member clears. (C4) Authorization stated in free text (a token or phrase
  in `method` or `reason`).

| Req | (A) | (B1) | (B2) | (C1) | (C2) | (C3) | (C4) |
|---|---|---|---|---|---|---|---|
| RQ1 | M1 to M7. Authenticity procedural (Claim I) | same keys as (A), inside a review | the reassessment's author is the plan side: authorization written by a conflicted party | none distinguishable (S1 passes) | no authorization at all | standing, typed in tool code. Not per-dispute | excluded by owner decision item 2 (tokens never carry authority) |
| RQ2 | typed parties; mechanical exclusions (§5.3) | as (A) | fails: author is a party | reviewer exclusions only | exclusions only | exclusions only | as (C3) |
| RQ3 | typed references to finding, witness, disputed record, replacement, reassessment | as (A) | partial: no witness binding without new keys | tokens (identity only) | tokens | tokens | tokens |
| RQ4 | typed per-item grounds, coverage checked; substance by review | as (A) | single `rederivation` string | general `accept` on `R`'s items | general `accept` | `accept`/`reject` on `R`'s items stands in for the disposition, conflating "is `R` correct" with "is `V`'s objection resolved" | as (C3) |
| RQ5 | no supersession; all in `R*` | as (A) | as (A) | `R*` | `R*` | `R*` | `R*` |
| RQ6 | typed failure conditions; contradiction rule (§5.7) | as (A), plus a hazard: older pinned tools see unknown keys in a review record and fail the reviewed record (R6.REC.6, R6.RECON.31's closed key set) | as (A) | no contradiction rule expressible | none | intent ambiguous: a member's ordinary review of `R` with tokens becomes an adjudication | as (C3) |
| RQ7 | unavailability: yes. Dispute: per round (§4) | as (A) | as (A) | yes, unsoundly | yes, unsoundly | only if a registry member is free of conflict; pre-dispute variant: no for existing disputes | — |

**Who reviews the adjudication.** r9 route 2 requires an independently reviewed adjudication. Under
(A) the adjudication is an ordinary reviewed record (one new row in R6.RECON.31's item-id table).
Under (B1) the adjudication sits inside a review record, and review records are not themselves
reviewed (no `oi-review-record/1` row in that table), so (B1) needs the same new row plus reviews of
reviews. Under (C2) and (C3) the technical review is a second review of `R` with no typed role.

**Detection interaction (r13 R6.RECON.35).** Detection reads any JSON file under
`verification/audits/` whose `schema` begins `oi-review-record/`. Under (B1), a revised review schema
would be read by every older pinned tool as class (b), a malformed record, and, where its text holds
`invalidates`, as a malformed finding binding at run level. Keeping the schema id and adding keys
instead fails the reviewed record in every older tool. (A) uses a schema outside both prefixes and
key names outside the class (b) review shape (R6.ADJ.14), so detection does not select it as a record.

**Size.** (A) adds one kind with five key tables, one row in R6.RECON.33's kind table, one row in
R6.RECON.31's item-id table, the `Adjudicated(W)` definition in r9 and three narrow exceptions (§6).
(B1) needs the same keys, the same item-id row, reviews of reviews and a compatibility change to the
most-read record kind. (B2) is unsound (RQ2). (C1) and (C2) are unsound (RQ1). (C4) is excluded.
(C3) is the only smaller candidate. It changes no schema, but it cannot express the disposition, the
dissents addressed or the role of the technical reviewer without putting decision meaning into
`accept`/`reject` or into free-text tokens (RQ4, RQ6). Its pre-dispute variant fails RQ7.

***

## 4. Recommendation

**Adopt (A), in its minimal form:** one record kind `oi-adjudication/1` as §5 states, with
authorization quoted inside it (no separate authorization kind) and attributed to `OWNER_IDENTITIES`.
It is the smallest alternative that meets RQ2 to RQ6 with typed fields, and it meets RQ1 to the
limit Claim I allows. (C3) is smaller but not sound for RQ4 and RQ6. (B) carries the same content as
(A) inside a record whose meaning and compatibility it changes.

**Requirements no alternative can meet in full.**

1. **RQ1, "verifiable".** No alternative makes the owner's authorization mechanically verifiable
   under R6.REC.3 (Claim I). (A) makes it explicit, owner-attributed, scope-bound, independently
   reviewed, landed under owner merge approval and permanent. The authenticity of the quotation stays
   procedural (R-ADJ-1). Only an authenticated channel, which needs an R6.REC.3 decision, changes
   this (OD-3 (e)).
2. **RQ7 against a persistent disputant, together with RQ6.** An original reviewer who dissents
   again after each adjudication obliges a fresh adjudication each time under fail-closed handling of
   contradictory evidence (§5.10 default). Mechanical finality would need a rule under which a
   party's later dissent does not defeat an adjudication, which narrows RQ6. The records cannot tell a
   repeated objection from a new one. The tension does not depend on the alternative. OD-2 states the
   choice. RQ7 for an unavailable reviewer, an unusable identity and a dispute that the adjudication
   answers is met in full.

***

## 5. Requirement text of the recommended option (proposed, not adopted)

Terms follow r13 R6.RECON.29 (reference, commit id, blob id, sha256, identity string, time) and r9
§2.2 (witness, disputed record `Q`, replacement `R`, candidate discharge `D` with reassessment `A`,
`R*`, custody). A *reference* is `{path, blob_sha256}`. An *item reference* is `{ref, item}`, with
`ref` a reference and `item` an item id of the referenced record or the pseudo-item `dissent`. A
*party* is an identity in the set `Parties(W, D)` of R6.ADJ.4.

### 5.1 Kind, location and keys

**R6.ADJ.1 Record kind and location.** An adjudication record (schema `oi-adjudication/1`) is
reviewed and immutable, under the ownership chain of r13 sec. 11. It decides one retained witness
`W` (r9 §2.2) against one replacement for one finding. It lies, with its review record, in the
reconciliation directory of its `replacement` (the directory of `replacement.path`, R6.RECON.1). A
configuration's freeze cites it by listing it in `records` with kind `adjudication`, and its review
with kind `review` (R6.CFG.4, R6.RECON.33). An adjudication referenced from another directory is
FAIL `record-invalid`.

**R6.ADJ.2 Key tables.** Each table is closed. A missing key, a key of another type or a key outside
the table is a form failure (condition `ADJ-FORM`).

*`oi-adjudication/1` record* (table `adj.record`)

| Key | Type | Required | Source and binding | Acceptance |
|---|---|---|---|---|
| `schema` | `"oi-adjudication/1"` | yes |  |  |
| `record_id` | non-empty string | yes | R6.REC.7 | unique among adjudication records in `R*` |
| `supersedes` | null | yes | R6.ADJ.10 | must be null |
| `author` | identity string | yes | the adjudicator | R6.ADJ.4 |
| `authorization` | object (`adj.authorization`) | yes | R6.ADJ.3 |  |
| `finding` | object (`reassess.finding` of R6.RECON.32) | yes | the finding whose discharge is in dispute | R6.ADJ.5 |
| `witness` | object (`adj.witness`) | yes | `W` as retained | R6.ADJ.5 |
| `replacement` | object (`reassess.repair.entry` of R6.RECON.32) | yes | `R` and its entry | R6.ADJ.5 |
| `reassessment` | reference | yes | `A` | R6.ADJ.5 |
| `dissents_addressed` | array of item references, no duplicate | yes (may be empty) | each non-accept item or non-empty `dissent` of a review of `R` that the adjudication answers | R6.ADJ.12 |
| `disposition` | `"cleared"` or `"upheld"` | yes | the decision on `W` for this replacement and finding | R6.ADJ.9 |
| `grounds` | non-empty array of grounds (`adj.ground`), `id` unique | yes | R6.ADJ.6 | coverage of R6.ADJ.6 |
| `method` | non-empty string | yes | how the adjudicator re-derived the dispute | contains the blob ids R6.ADJ.6 requires |
| `conflicts` | non-empty string | yes | the adjudicator's declaration of relationships to the parties, or `none` | its truth rests on the review |

*`authorization`* (table `adj.authorization`)

| Key | Type | Required | Source and binding | Acceptance |
|---|---|---|---|---|
| `quote` | non-empty string | yes | the owner's words authorizing this adjudicator for this dispute | form only; its correspondence to the owner's record rests on the review (R6.REC.3) |
| `author` | identity string | yes | the owner's login | a member of `OWNER_IDENTITIES` |
| `time` | time | yes | the time of the owner's record | form only |
| `source` | non-empty string | yes | where the owner's record is held | provenance only (AGENTS.md §A.42 item 2) |
| `adjudicator` | identity string | yes | the person authorized | equals the record's `author` |
| `finding` | object (`reassess.finding`) | yes | the dispute authorized | equals the record's `finding` |
| `witness_sources` | non-empty array of references | yes | the dispute authorized | set-equal to `witness.sources` |

*`witness`* (table `adj.witness`)

| Key | Type | Required | Source and binding | Acceptance |
|---|---|---|---|---|
| `class` | `"review"` or `"lineage"` | yes | r9 §2.2 |  |
| `disputed` | reference | yes | the disputed record `Q` |  |
| `edge` | `{successor, predecessor}` of references, or null | yes | the exact disputed edge | non-null exactly when `class` is `"lineage"` |
| `sources` | non-empty array of references, no duplicate | yes | the records forming `W`: each adverse or failed review for a review witness; the competing successor `S` for a lineage witness |  |
| `adverse` | array of item references, no duplicate | yes | for a review witness, each item that makes a source adverse or defective (a verdict other than `accept`, an omitted or duplicated item id, or `dissent` for a non-empty `dissent` field); for a lineage witness, `[{ref: S, item: "edge"}]` |  |
| `original_configuration` | reference | yes | the configuration under which `W` qualified (r9 §2.2) | resolves under R6.RECON.33 |

*ground (element of `grounds`)* (table `adj.ground`)

| Key | Type | Required | Source and binding | Acceptance |
|---|---|---|---|---|
| `id` | non-empty string, no whitespace | yes | item id `ground:<id>` for the review |  |
| `target` | item reference | yes | one element of `witness.adverse` or `dissents_addressed` |  |
| `reasoning` | non-empty string | yes | why the objection does or does not apply to this replacement for this finding | substance rests on the review |
| `evidence` | non-empty array of blob ids | yes | the objects the adjudicator read for this ground | R6.ADJ.6 |

Review item ids (one row added to R6.RECON.31's item-id table): `authorization`, `binding`,
`dissents`, `disposition`, `conflicts`, and `ground:<id>` for each ground.

### 5.2 Authorization

**R6.ADJ.3 Authorization.** The `authorization` object quotes the owner's authorization of this
adjudicator for this dispute, with author and time (AGENTS.md §A.42 item 7). The tool checks that:
its keys meet `adj.authorization`; `author` is a member of the tool constant `OWNER_IDENTITIES`
(for this repository `["amaybaum"]`), which is fixed by the tool's review and landing, pinned by
every configuration's `tool.files`, and changed only by a tool revision (as R6.RDIR.2 fixes the
admitted record directories); `adjudicator` equals the record's `author`; `finding` equals the
record's `finding`; and `witness_sources` is set-equal to `witness.sources`. A failure of the first
two checks is condition `ADJ-AUTH-FORM` or `ADJ-AUTH-OWNER`, and a failure of the last three is
`ADJ-AUTH-SCOPE`. The tool neither reads nor checks the owner's approval (R6.REC.3). The quotation
is evidence for the technical reviewer, who checks it against the owner's record (R6.ADJ.7). It does
not represent the approval to the tool. A statement of authorization anywhere else (a token, `method`,
`reason`, `grounds`, a commit message, pull-request or Issue text, a run log) is not an authorization.

### 5.3 Independence and conflicts

**R6.ADJ.4 Independence.** `Parties(W, D)` is the set of identity strings consisting of:
- the `author` of: the record carrying the finding; `Q`; `R`; `A`; the citing configuration; each
  record in `witness.sources` that has an `author`; and, for a lineage witness, the predecessor;
- the `reviewer` of: each review in `witness.sources`; each review in `R*` of `Q`, of `R` and of `A`
  that names their exact references; and, for a lineage witness, each review of the predecessor.

The author of an earlier adjudication of the same witness is not a party by that fact alone. A
further adjudication by the same adjudicator is evaluated with the earlier one under R6.ADJ.9.

The adjudicator (`author`) must not be a party and must not equal `authorization.author` (OD-4). The
technical reviewer (the `reviewer` of the adjudication's review, R6.ADJ.7) must not be a party and
must not equal the adjudicator. Every comparison is of identity strings (R6.RECON.29). An identity
that is a tool, CI or check run, an Issue, a URL or a run id fails (R6.REC.6). Any failure is
condition `ADJ-INDEP`. The `conflicts` declaration is reviewed, not checked. A relationship that the
identity strings do not show (a shared employer, the same agent session under two strings) is
residual R-ADJ-2.

### 5.4 Binding

**R6.ADJ.5 Binding.** For a candidate discharge `D` with reassessment `A` and witness `W`, an
adjudication binds `D` and `W` only if all of the following hold, each checked from git objects:
- `finding` equals `A`'s `finding` (path, blob sha256 and item);
- `reassessment` equals the reference of `A`, and `replacement` equals `A`'s `repair.entry`;
- `witness` equals `W` as reproduced from custody under r9 R6.OBL29.3: the same `class`, `disputed`
  and `edge`; `sources` set-equal to the records forming `W`; `adverse` set-equal to the adverse items
  computed from those records; and `original_configuration` equal to the configuration under which
  `W` qualified.

Any difference, and any reference that does not resolve, is condition `ADJ-BIND`. An adjudication
binds no other discharge, witness, replacement or finding. Typed references establish evidence
identity. They confer no authority, as the token convention of owner decision item 2 states for
tokens. r9's tokens are not used in this record kind.

### 5.5 Substance

**R6.ADJ.6 Substance.** The multiset of `grounds[].target` equals the set
`witness.adverse ∪ dissents_addressed`: one ground per target, none missing, none extra. Each
ground's `evidence` contains the git blob id of its target's record, of `Q` and of `R`. `method`
contains the git blob ids of the record carrying the finding, of each element of `witness.sources`,
of `Q`, of `R` and of `A`. Any failure is condition `ADJ-SUBST`. The tool checks coverage and
presence only. Whether the reasoning resolves the objection rests on the technical review (R6.REC.2,
R6.ADJ.7) and is residual R-ADJ-3. An adjudication whose only basis is an approval, a withdrawal, a
rehearing decision or a deletion meets no substance requirement that a reviewer can accept. A
disposition without grounds fails mechanically.

### 5.6 Technical review and admission

**R6.ADJ.7 Technical review.** Exactly one review record of the adjudication is cited by the freeze.
It meets R6.REC.6 and R6.RECON.31, covers every item id of R6.ADJ.2 with `accept`, and its `method`
names the git blob ids of the adjudication and of each element of `witness.sources`. On the item
`authorization`, the reviewer confirms that the quotation, author and time correspond to the owner's
record at `source`. On each `ground:<id>`, the reviewer re-derives the ground from the git objects,
not from the adjudicator's text. Every review in `R*` that names the adjudication's reference is a
review of it (R6.REC.6): one whose verdict on any item is not `accept`, or whose `dissent` is
non-empty, fails the adjudication. A failure is condition `ADJ-REVIEW`.

**R6.ADJ.8 Admission.** An adjudication is admitted for a run only if: the configuration at the
candidate freeze `F'` references it with kind `adjudication`, and its review with kind `review`
(R6.REC.4); both resolve from `F'` under R6.RECON.33 at a commit that lies on the first-parent chain
of the run's `M` and is an ancestor of `F'` (they were on `main` before the freeze); both lie at
their stated paths in the reconciliation directory of R6.ADJ.1; and both pass record lint
(R6.REC.6, R6.REC.7). An adjudication found in `R*` but not cited is not applied. It is still read
for R6.ADJ.9's contradiction rule and reported. Failures are `ADJ-ADMIT` (not cited, wrong location,
or not resolvable) and `ADJ-LANDED` (not on `M`'s first-parent chain before `F'`).

### 5.7 Decision

**R6.ADJ.9 `Adjudicated(W, D)`.** In r9's decision, `Adjudicated(W)` reads `Adjudicated(W, D)` and
holds exactly when some adjudication `J` meets all of the following:
1. it is admitted (R6.ADJ.8) and passes R6.ADJ.2 to R6.ADJ.7;
2. it binds `D` and `W` (R6.ADJ.5);
3. its `disposition` is `"cleared"`;
4. its `dissents_addressed` covers every dissenting review of `R` (R6.ADJ.12);
5. no contradicting adjudication exists. A contradicting adjudication is any record in `R*` of
   schema `oi-adjudication/1`, other than `J`, that names the same `finding`, `replacement` and
   `witness.disputed`, has an overlapping `witness.sources`, and has `disposition` `"upheld"`,
   unless that record is established invalid by a definite failure of R6.ADJ.2 to R6.ADJ.7.
   One whose validity cannot be established (a reference that does not resolve, or incomplete
   custody) contradicts. The condition is `ADJ-CONTRA`.

A valid adjudication with `disposition` `"upheld"`, admitted or not, also makes NR-5 false for the
same finding, replacement and witness (`ADJ-UPHELD`; OD-6). A new replacement is a new question.
`Adjudicated(W, D)` is false unless verified records establish it (r9 §2.2). When it is false and
`W` is not otherwise cleared, r9's result stands: FAIL `record-invalid` naming `D`'s reassessment,
`W` and each failed condition, with `retirement-blocked` for the finding. A required unreadable or
unverifiable git object gives ERROR.

### 5.8 Preservation

**R6.ADJ.10 Preservation.** An adjudication changes no finding, witness, record or review. It is
never superseded (`supersedes` is null). A correction is a new adjudication, which is evaluated with
every earlier one under R6.ADJ.9. No later record narrows, withdraws or replaces an earlier
adjudication. An adjudication, its review and every review of it stay in `R*` after a removal from
the current tree (r9 R6.OBL29.1), and a removed adjudication is evaluated as one that is present. The
finding stays in `category3.findings` whether or not it is discharged, and each witness stays
reported with its sources, its adverse items, and the route and records that cleared it. Clearing a
witness discharges nothing by itself: an applying reassessment is still required wherever
R6.RECON.26 and R6.RECON.27 require one.

### 5.9 Fail-closed handling

**R6.ADJ.11 Fail closed.** `Adjudicated(W, D)` is false when any of the following holds: a required
record, reference or custody object is missing or does not resolve; the retained description of `W`
cannot be reproduced (r9 R6.OBL29.3); a key is missing, ambiguous or malformed; two reviews of the
adjudication are cited; the dissenting reviews of `R` cannot be enumerated because custody is
incomplete; or a contradiction under R6.ADJ.9 (5) exists. No default, inference or later statement
supplies a missing element. The same inputs give the same result on every run.

### 5.10 Dissent on the replacement

**R6.ADJ.12 Dissents addressed.** A *dissenting review of `R`* is a review in `R*` that names
`R`'s exact reference and has a verdict other than `accept` on any item or a non-empty `dissent`.
Each such item, and `dissent` for a non-empty field, must appear in `dissents_addressed`, and so
receives a ground (R6.ADJ.6). Otherwise condition `ADJ-DISSENT` fails. For a discharge `D` for which
`Adjudicated(W, D)` holds for every witness that relies through `R`, a dissent item that an applying
adjudication addresses does not fail `R` under R6.REC.6, and does not count as dissent under r9 NR-3
and NR-5. It is preserved and reported. A dissent item that no applying adjudication addresses keeps
both effects. A dissenting review that lands after the adjudication is therefore unaddressed and
needs a further adjudication (default; OD-2).

### 5.11 Result and detection

**R6.ADJ.13 Result fields.** Each element of `category3.findings` gains `adjudications`: one entry
for every `oi-adjudication/1` record in `R*` that names the finding,
`{path, blob_sha256, witness_sources, disposition, admitted, applies, failures}`, with `failures` the
list of condition ids of R6.ADJ.3 to R6.ADJ.12. A witness cleared by adjudication is reported with
route `adjudication` and the references of `J` and its review. The name avoids r9 R6.OBL29.8's
`witness`, which is a commit id. No new outcome class is introduced.

**R6.ADJ.14 Detection compatibility.** An adjudication record and its elements contain no key
`reviewed` or `verdicts` and no `schema` value beginning `oi-review-record/` or `oi-reconciliation/`
at any depth. So R6.RECON.35 does not select it as a record of class (a) or (b). A file of schema
`oi-adjudication/1` that violates this is classed by R6.RECON.35 as it stands (a malformed record,
and a malformed finding where its text holds `invalidates`), which fails closed.

***

## 6. Interaction with OBL-29 r9 and Amendment 6 r13

On adoption, these would be separate amendments. None is made here.

| Location | Proposed change |
|---|---|
| r9 §2.2 route 2 and §5.6 "Route 2 adjudication" | route 2 is `Adjudicated(W, D)` of R6.ADJ.9. The sentence "Route 2 is therefore unavailable through existing records ... until an owner-authorized admission route exists" is replaced by a citation of R6.ADJ.1 to R6.ADJ.14. NR-5 and route 1 are unchanged. The original reviewer's resolution stays available and needs no adjudication. |
| r9 NR-3 and NR-5, "no eligible review of `R` in `R*` dissents" | gains R6.ADJ.12's exception for addressed dissent items |
| r9 decision | `Adjudicated(W)` reads `Adjudicated(W, D)`. Otherwise unchanged. |
| r9 R6.OBL29.8 | `adjudications` added beside `present_at_M` and `witness` (R6.ADJ.13) |
| r13 R6.REC.3 | add: "The `authorization` of an adjudication record (R6.ADJ.3), like the `approval` of an edit-id migration record (R6.RECON.32), quotes that approval for the reviewer and is checked for form and binding only; it does not represent the approval to the tool." |
| r13 R6.REC.6 | add R6.ADJ.12's exception for `R`, limited to the discharge the adjudication binds |
| r13 R6.RECON.31 | one item-id row for `oi-adjudication/1` (R6.ADJ.2) |
| r13 R6.RECON.33 and R6.CFG.4 | one kind row: `adjudication` → `oi-adjudication/1`. `oi-owner-authorization/1` stays undefined. |
| r13 R6.RECON.29 | the new tables enter the single-definition rule, and their conformance mutants are generated as for the other kinds |
| r13 tool constants | `OWNER_IDENTITIES`, beside the admitted record directories (R6.RDIR.2) |

Unchanged: R6.RECON.26's blocking rule and finding forms; R6.RECON.27's reassessment and its Keys
(an adjudication clears a witness, never a finding); R6.RECON.28; R6.RECON.35's selection; the token
convention (r9 §2.2, owner decision item 2), which keeps its role in NR-4 and NR-5 and is not used for
authority. Adjudication adds no route that lifts a block without an applying reassessment and a new
freeze (R6.CFG.3, AGENTS.md §A.50 item 5).

**Safety (no bypass).** Each conjunct of r9's `blocked(D, W)` is unchanged except `Cleared`, which
gains one disjunct, `Adjudicated(W, D)`, false unless R6.ADJ.9 holds. The exception of R6.ADJ.12
applies only where that disjunct holds for every witness relying through `R`. So every discharge
that r9 blocks stays blocked unless an admitted, bound, authorized, independent, substantive,
uncontradicted adjudication exists, subject to residuals R-ADJ-1 to R-ADJ-3.

**Reachability.** An adjudication can meet R6.ADJ.9 without any act of `V`'s reviewer. So route 2
is reachable when that reviewer is unavailable, has an unusable identity, or disputes `R` with
reviews that the adjudication addresses. It needs one authorized adjudicator and one technical
reviewer outside `Parties(W, D)`, and one owner authorization (CONTROLS.json: ADJ-P-UNAVAILABLE,
ADJ-P-DISPUTED, ADJ-P-UNUSABLE-IDENTITY).

***

## 7. Residual risks

- **R-ADJ-1. Forged authorization.** The tool cannot tell a genuine quotation of the owner from a
  fabricated one that a colluding technical reviewer accepts and that reaches `main` (Claim I, S6).
  Guards: procedural only. The owner's merge approval of the adjudication's landing (M5), at which the
  owner sees a quotation of the owner's own words with its `source`, and permanence in `R*` (M7).
  OD-3 lists the strengthenings.
- **R-ADJ-2. Identity.** Identity strings are self-declared (r9 R-8). Impersonation of the
  adjudicator, the reviewer or a party, and relationships the strings do not show, are guarded only
  procedurally.
- **R-ADJ-3. Substance.** Coverage of every adverse item and dissent is mechanical. Whether each
  ground's reasoning resolves its objection rests on the technical review, as every judgment in r13
  does (R6.REC.2).
- **R-ADJ-4. Termination.** Under the default of R6.ADJ.12 and R6.ADJ.7, a party who files a new
  dissent on `R` or on the adjudication after each adjudication keeps the witness unresolved until a
  further adjudication answers it (§4, OD-2).
- **R-ADJ-5. Availability of adjudicators.** Reachability needs one authorized adjudicator and one
  technical reviewer outside `Parties(W, D)`. Where no such person exists, the witness stands, which
  fails closed. The r13 identity strings cannot show whether such people exist.
- **R-ADJ-6. Custody.** `Adjudicated` depends on r9's custody of the witness and the dissent
  enumeration. Where custody is incomplete, it fails closed (R6.ADJ.11). r9's squash and rebase gap
  (r9 §6) applies to adjudication records as to every other record.

***

## 8. Owner decisions this design leaves

| Id | Decision | Alternatives and consequences | Design default |
|---|---|---|---|
| OD-1 | Mechanism | (A) as §5; (B1); (C3); none (route 2 stays unavailable, and RQ7 stays unmet) | (A) |
| OD-2 | Termination against a persistent disputant | (i) per round: every unaddressed dissent on `R` and every non-accepting review of the adjudication defeats it until a further adjudication answers it (RQ6 in full, RQ7 not guaranteed to terminate); (ii) finality: reviews by parties of `R` or of the adjudication that land on `main` after the adjudication are preserved and reported but do not defeat it, and a new substantive objection enters only as a well-formed category-3 finding (R6.RECON.26), which blocks under its own rules (RQ7 terminates; RQ6 narrowed for later party dissent) | (i) |
| OD-3 | Strengthening the authorization | (a) `OWNER_IDENTITIES` only; (b) an `ADJUDICATORS` tool-constant registry, with or without the pre-dispute variant; (c) a separate authorization record kind; (d) a quorum of k technical reviewers; (e) an authenticated channel (owner signature with a pinned key, or a host read), which needs an R6.REC.3 change | (a) |
| OD-4 | May the owner be the adjudicator? | Allowed: removes the separation between authorizer and adjudicator. Barred: an authorized third party is always needed. | barred |
| OD-5 | Scope | witness clearance only, or also adjudication of a mistaken independent finding (r9 §5.6), which would extend R6.RECON.27's `repair: null` route and needs its own design | witness only |
| OD-6 | Effect of an upheld adjudication on NR-5 | blocks NR-5 for the same finding, replacement and witness, or does not | blocks |
| OD-7 | Dissent exception | adopt R6.ADJ.12's exceptions to R6.REC.6 and to r9 NR-3 and NR-5 (needed for the dispute case of RQ7), or not (adjudication then reaches only the unavailable and unusable-identity cases) | adopt |

Adoption of this design, any amendment of r9 or r13, any tool revision, freeze, trial, dispatch and
merge each need their own owner decision (AGENTS.md §A.50 items 1 and 5, §A.51 item 6).

***

## 9. Reference trace (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7197443528 | authority, the seven requirements, token condition | provenance; author and time quoted in §0 |
| `5ad8837521de0a26734266a64f91548fd3dcff1e` (r13), PR #1593, #1593 comment 7193277489 | R6.REC.2, .3, .6, .7, R6.CFG.4, R6.RDIR.2, R6.RECON.26 to .35 | support off `main` (PR #1593 open); the cited requirements are quoted or paraphrased here |
| `77a73c022091f598cf807fcf89d66c3cf43208de` (r9), PR #1601 | §2.2 route 2, NR-3 to NR-5, token rule, decision, R6.OBL29.1, .3, .8, R-8, §5.6 | support off `main` (PR #1601 open) |
| #1601 comment 7197262397, finding 4 | the gap | provenance |
| `942bd5ea1fd09f4223012b0755bce2d6da07c44a` | `main` at drafting; AGENTS.md §A.42, §A.46, §A.47, §A.50, §A.51; signed merge example | support on `main` |

The design asserts no established result. Its claims (Claim I, the comparison, safety and
reachability) are for independent review (REVIEW-BRIEF.md).
