# Formal adjudication of retained witnesses (paper design r3)

## 0. Status, authority, scope and goal link

**Status.** Paper design r3. Not adopted. It changes no schema, admission rule, requirement,
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
receives independent review." Item 2 of the same decision governs the token convention: "Tokens
establish evidence identity, never adjudication authority."

**Revision.** r1 at `2de8462946c65dcf0f004a559fd12b9c18c22ceb` (PR #1605) received REVISE in the
independent review posted verbatim at #1605 comment 7197900888 (findings F1 to F12). r2 at
`6a0afe052b30c6a14d32e03960df3c1df72c4101` answered them and received a narrow REVISE in the
re-review at #1605 comment 7198103680 (findings N1 to N5). r3 makes only the textual fixes N1 to N5,
under the same authority. The finding maps are in REVIEW-BRIEF.md.

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
owner: it may be carried for the reviewer and checked for form, but it does not establish approval
to the tool. This design goes one step beyond that precedent (owner attribution, §5.2), and states
that step as a deliberate change of R6.REC.3 (§6).

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
substitute can produce the same record bytes, changing only who actually wrote them, which no record
byte authenticates. The tool can tell an authorized freeze from a substituted one only if some byte
it reads can be produced only by an authorized party. That requires authenticated identity: a
signature checked against a pinned key, or a host read of the owner's own record. R6.REC.3 excludes
both, and AGENTS.md §A.42 item 2 excludes a host comment as the sole support of an enduring claim.
The argument depends on R6.REC.3 and on unauthenticated identity strings, not on the choice among
(A), (B) and (C).

*Qualification (what lies just outside R6.REC.3).* Merge commits made through the host on `main`
carry the host's web-flow signature, and that signature covers the whole commit object, its `author`
field included: `942bd5ea` has author `amaybaum`, committer `GitHub` and a web-flow signature. With a
pinned web-flow key, the tool could therefore check that the commit introducing an adjudication is a
host-signed merge whose author is an owner identity. That would authenticate more than Claim I
allows, without owner key custody. Caveat: commits created through the host's API are also
web-flow-signed and can carry an arbitrary author, so the check authenticates the host's record of
the commit, not the owner's act, unless the landing path is constrained. Using it needs an R6.REC.3
decision. It is the web-flow variant of OD-3 (e).

### 2.2 What can be made mechanical

Claim I bounds what any alternative achieves. Within it, a mechanism can make these properties
mechanical, so that substitution needs a forgery that is recorded permanently and visible to the owner:

| Id | Property | Mechanical check |
|---|---|---|
| M1 | Explicitness | A typed authorization object exists, bound to this dispute. A freeze without one is distinguished from one with one. |
| M2 | Owner attribution | The authorization's `author` is a member of a tool constant `OWNER_IDENTITIES`, pinned with the tool files (as R6.RDIR.2 pins the admitted record directories). An authorization attributed to anyone else fails. |
| M3 | Scope equality | The authorization names the adjudicator, the finding, the witness and the replacement, and these equal the adjudication's own. Its time precedes the adjudication's landing. |
| M4 | Independent review of the authorization | The authorization is an item of the adjudication, so a non-party technical reviewer must accept it. That reviewer checks the quotation against the owner's record. |
| M5 | Landing before reliance | The adjudication and its review are on `main` before the freeze that cites them. They therefore passed an owner-approved merge, at which the owner sees a quotation of the owner's own words. |
| M5' | Dedicated landing (recommended, OD-3) | The first-parent commit on `main` that introduces the adjudication changes only the adjudication and its review. The owner's merge approval is then an approval of this record specifically. |
| M6 | Conflict rules | Mechanical identity-string exclusions (§5.3). |
| M7 | Permanence | The adjudication, its authorization and every review stay in `R*` (r9 R6.OBL29.1), so a forgery cannot be withdrawn without trace. |

**Distinguishability of substitution.**

| Attempt | Distinguished mechanically? |
|---|---|
| S1. A substitute's accepting review of `R`, with no adjudication record | yes: NR-5 fails (reviewer is not `V`'s), and `Adjudicated(W)` is false |
| S2. An adjudication record without an authorization object | yes (M1) |
| S3. An authorization attributed to a non-owner identity | yes (M2) |
| S4. An authorization naming another adjudicator, finding, witness or replacement, or dated after the landing | yes (M3) |
| S5. A forged authorization that the technical reviewer rejects | yes (M4) |
| S6. A forged authorization accepted by a colluding technical reviewer and landed through an owner-approved merge (with M5', a merge that carries only that record) | **no**: residual R-ADJ-1 |
| S7. A party writing under the adjudicator's identity string | **no**: residual R-ADJ-2 (r9 R-8) |

So the substitution case that remains needs a fabricated quotation of the owner, a second party's
false acceptance of it, and an owner-approved merge that shows it. All three stay on `main`.

### 2.3 Strengthenings assessed

| Strengthening | Effect on substitution | Cost and reachability | Assessment |
|---|---|---|---|
| Dedicated landing (M5') | S6 needs an owner-approved merge whose whole content is the forged record | one tree comparison; no schema | Recommended (OD-3). |
| Separate authorization record kind, by an author other than the adjudicator, with its own non-author review, landed before the adjudication | S6 needs two colluding reviewers plus a false author instead of one reviewer | a second record kind, key tables and item-id row; one more landing | Marginal gain over M4. OD-3 (c). |
| Standing adjudicator registry as a tool constant `ADJUDICATORS` | S6 additionally needs a tool revision that adds the substitute, reviewed and landed under owner approval | every appointment is a tool revision. A "pre-dispute" variant (registry of the tool pinned at the original freeze) also stops post-hoc choice, but leaves no adjudicator for any dispute that arose before the registry, including every current A1 dispute | Raises the bar. The pre-dispute variant fails RQ7 for existing disputes. OD-3 (b). |
| Per-dispute registry entry as a tool constant: `{adjudicator, finding, item, witness sources, replacement}` | S6 needs a reviewed tool revision, landed under owner merge approval, for this dispute; stronger than a quotation | a tool revision per adjudication; tool code becomes a ledger of disputes | Stronger authorization than (A)'s quotation, at the cost of a tool revision per grant. It can be combined with (A), whose record keeps the substance and review. OD-3 (b'). |
| Registry pinned in the configuration | none: the configuration is written by the plan side and admitted by the same freeze that would pin a substitute (r8 review, finding 4) | a closed-key change to `oi-retirement-config/1` | Unsound. Rejected. |
| Quorum of k ≥ 2 independent technical reviewers | S6 needs k colluding reviewers. Gives no authorization | k reviews per adjudication | Not a substitute for RQ1. May be added. OD-3 (d). |
| Authenticated channel: an owner signature on the adjudication's commit or a signed tag, checked against a pinned owner key; the web-flow variant of §2.1; or a host read of the owner's comment | the only options that make S6 and the owner-attribution part of S7 mechanically distinguishable | changes R6.REC.3; key custody for an owner key; the web-flow caveat of §2.1; a host read also conflicts with §A.42 item 2 and with offline replay (R6.OUT.15) | Outside the three alternatives. OD-3 (e). Needs its own R6.REC.3 decision. |

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
  the NR-5 tokens replaces `V`'s reviewer. (C3) A tool-constant registry (standing, or with
  per-dispute entries): a review of `R` with the NR-5 tokens by the registered adjudicator clears.
  (C4) Authorization stated in free text (a token or phrase in `method` or `reason`).

| Req | (A) | (B1) | (B2) | (C1) | (C2) | (C3) | (C4) |
|---|---|---|---|---|---|---|---|
| RQ1 | M1 to M7. Authenticity procedural (Claim I) | same keys as (A), inside a review | the reassessment's author is the plan side: authorization written by a party | none distinguishable (S1 passes) | no authorization at all | typed in reviewed tool code; with per-dispute entries stronger than (A)'s quotation | excluded by owner decision item 2 (tokens never carry authority) |
| RQ2 | typed parties; mechanical exclusions (§5.3) | as (A) | fails: author is a party | reviewer exclusions only | exclusions only | exclusions only | as (C3) |
| RQ3 | typed references to finding, witness, disputed record, replacement, reassessment | as (A) | partial: no witness binding without new keys | tokens (identity only) | tokens | tokens (identity only), plus the registry entry's typed scope | tokens |
| RQ4 | typed per-item grounds, coverage checked; substance by an independent review of the adjudication | as (A), but no review of the adjudication without reviews of reviews | single `rederivation` string | general `accept` on `R`'s items | general `accept` | the adjudicator's review of `R` is not itself reviewed (r9 route 2 requires an independently reviewed adjudication; reviews of reviews are undefined) | as (C3) |
| RQ5 | no supersession; all in `R*` | as (A) | as (A) | `R*` | `R*` | `R*` | `R*` |
| RQ6 | typed failure conditions; validity separated from admission; contradiction rule (§5.7) | as (A), plus a hazard: older pinned tools see unknown keys in a review record and fail the reviewed record (R6.REC.6, R6.RECON.31's closed key set) | as (A) | no contradiction rule expressible | none | "upheld" is expressible only as a dissent on `R`, so an upheld decision is indistinguishable from an ordinary dissent and has no typed contradiction rule | as (C3) |
| RQ7 | yes for an unavailable reviewer, an unusable identity and a dispute the adjudication answers; termination under OD-2 | as (A) | as (A) | yes, unsoundly | yes, unsoundly | yes with per-dispute entries; the pre-dispute variant fails existing disputes | — |

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
key names outside the class (b) review shape (R6.ADJ.14), so detection does not select a parseable
adjudication as a record.

**Why not (C3).** (C3) changes no schema, and with per-dispute entries its authorization is stronger
than (A)'s quotation. Its defects are elsewhere:
1. it has no independent review of the adjudication, which r9 route 2 requires, and adding one needs
   reviews of reviews, which r13 does not define;
2. an upheld decision can be expressed only as a dissent on `R`, which has no typed contradiction or
   upheld rule;
3. the adjudication's binding to the witness and the dissents it answers would be carried in
   free-text tokens, against the owner's preference for a typed mechanism (tokens may carry identity,
   but the decision would then live in untyped text);
4. tool code becomes a ledger of disputes, with a tool revision for every adjudication.

The per-dispute registry entry, without the rest of (C3), is kept as an optional strengthening of
(A) (OD-3 (b')).

**Size.** (A) adds one kind with five key tables, one row in R6.RECON.33's kind table, one row in
R6.RECON.31's item-id table, the `Adjudicated` definition in r9, a tool constant and the narrow
exceptions of §6. (B1) needs the same keys, the same item-id row, reviews of reviews and a
compatibility change to the most-read record kind. (B2) is unsound (RQ2). (C1) and (C2) are unsound
(RQ1). (C4) is excluded. (C3) is not sound for RQ4 and RQ6, for the reasons above.

***

## 4. Recommendation

**Adopt (A), in its minimal form:** one record kind `oi-adjudication/1` as §5 states, with
authorization quoted inside it (no separate authorization kind), attributed to `OWNER_IDENTITIES`,
and landed by a dedicated landing (M5'). It is the smallest alternative that meets RQ2 to RQ6 with
typed fields, meets RQ1 to the limit Claim I allows, and meets RQ7 under the recommended OD-2 default.

**Requirements no alternative can meet in full.**

1. **RQ1, "verifiable".** No alternative makes the owner's authorization mechanically verifiable
   under R6.REC.3 (Claim I). (A) makes it explicit, owner-attributed, scope-bound, dated before the
   landing, independently reviewed, landed by a dedicated owner-approved merge and permanent. The
   authenticity of the quotation stays procedural (R-ADJ-1). Only an authenticated channel, which
   needs an R6.REC.3 decision, changes this (OD-3 (e), including its web-flow variant).
2. **RQ7 and RQ6 together, in full.** With the recommended OD-2 default (refined (ii), R6.ADJ.12),
   RQ7 terminates: a reviewer whose objection an adjudication has answered cannot defeat it again by
   repeating the objection, and new substance from that reviewer enters as a category-3 finding,
   which binds under its own rules. RQ6 is narrowed only for those repeated objections. Under
   option (i), RQ6 holds in full but resolution can depend indefinitely on one reviewer's
   willingness, which conflicts with the owner's principle that adjudication remain available
   (§5.10). No alternative removes this trade-off, because the records cannot tell a repeated
   objection from a new one. Residual sock identities remain (R-ADJ-2).

***

## 5. Requirement text of the recommended option (proposed, not adopted)

Terms follow r13 R6.RECON.29 (reference, commit id, blob id, sha256, identity string, time) and r9
§2.2 (witness, disputed record `Q`, replacement `R`, candidate discharge `D` with reassessment `A`,
`R*`, custody). A *reference* is `{path, blob_sha256}`. An *item reference* is `{ref, item}`, with
`ref` a reference and `item` an item id of the referenced record or the pseudo-item `dissent`. A
*usable identity* is an identity string that is not a tool, CI or check run, an Issue, a URL or a
run id (R6.REC.6). `R*(C)`, for a commit `C`, is `R*` computed with `C` in place of `M` and
without `F` or `REV` (r9 R6.OBL29.1). For an adjudication `J`, `L(J)` is its *landing commit*: the
earliest commit `C` on `M`'s first-parent chain whose tree holds `J` and a review of `J` that
qualifies under R6.ADJ.7 when evaluated over `R*(C)`, with `Parties` at `C`; null when there is none.

### 5.1 Kind, location and keys

**R6.ADJ.1 Record kind and location.** An adjudication record (schema `oi-adjudication/1`) is
reviewed and immutable, under the ownership chain of r13 sec. 11. It decides one retained witness
`W` (r9 §2.2) against one replacement for one finding. It lies, with its review record, in the
reconciliation directory of its `replacement` (the directory of `replacement.path`, R6.RECON.1). A
configuration's freeze cites it by listing it in `records` with kind `adjudication`, and its review
with kind `review` (R6.CFG.4, R6.RECON.33). An adjudication cited from another directory fails
admission (`ADJ-ADMIT`).

**R6.ADJ.2 Key tables.** Each table is closed. A missing key, a key of another type or a key outside
the table is a form failure (condition `ADJ-FORM`).

*`oi-adjudication/1` record* (table `adj.record`)

| Key | Type | Required | Source and binding | Acceptance |
|---|---|---|---|---|
| `schema` | `"oi-adjudication/1"` | yes |  |  |
| `record_id` | non-empty string | yes | R6.REC.7 | unique among adjudication records in `R*` |
| `supersedes` | null | yes | R6.ADJ.10 | must be null |
| `author` | identity string | yes | the adjudicator | usable identity; R6.ADJ.4 |
| `authorization` | object (`adj.authorization`) | yes | R6.ADJ.3 |  |
| `finding` | object (`reassess.finding` of R6.RECON.32) | yes | the finding whose discharge is in dispute | R6.ADJ.5 |
| `witness` | object (`adj.witness`) | yes | `W` as retained | R6.ADJ.5 |
| `replacement` | object (`reassess.repair.entry` of R6.RECON.32) | yes | `R` and its entry | R6.ADJ.5 |
| `reassessment` | reference | yes | `A` | R6.ADJ.5 |
| `dissents_addressed` | array of item references, no duplicate | yes (may be empty) | each non-accept item, or `dissent` for a non-empty `dissent` field, of a review of `R` that the adjudication answers | each names a review of `R` in `R*(L(J))` and an item that is adverse in it |
| `disposition` | `"cleared"` or `"upheld"` | yes | the decision on `W` for this replacement and finding | R6.ADJ.9 |
| `grounds` | non-empty array of grounds (`adj.ground`), `id` unique | yes | R6.ADJ.6 | coverage of R6.ADJ.6 |
| `method` | non-empty string | yes | how the adjudicator re-derived the dispute | contains the blob ids R6.ADJ.6 requires |
| `conflicts` | non-empty string | yes | the adjudicator's declaration of relationships to the parties, or `none` | its truth rests on the review |

*`authorization`* (table `adj.authorization`)

| Key | Type | Required | Source and binding | Acceptance |
|---|---|---|---|---|
| `quote` | non-empty string | yes | the owner's words authorizing this adjudicator for this dispute | form only; its correspondence to the owner's record rests on the review |
| `author` | identity string | yes | the owner's login | a member of `OWNER_IDENTITIES` |
| `time` | time | yes | the time of the owner's record | earlier than the committer time of `L(J)` (form check only) |
| `source` | non-empty string | yes | where the owner's record is held | provenance only (AGENTS.md §A.42 item 2) |
| `adjudicator` | identity string | yes | the person authorized | equals the record's `author` |
| `finding` | object (`reassess.finding`) | yes | the dispute authorized | equals the record's `finding` |
| `witness_sources` | non-empty array of references | yes | the dispute authorized | set-equal to `witness.sources` |
| `replacement` | object (`reassess.repair.entry`) | yes | the replacement authorized | equals the record's `replacement` |

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
adjudicator for this dispute and this replacement, with author and time (AGENTS.md §A.42 item 7). The
tool checks:
- its keys meet `adj.authorization` (`ADJ-AUTH-FORM`);
- `author` is a member of the tool constant `OWNER_IDENTITIES` (for this repository `["amaybaum"]`),
  which is fixed by the tool's review and landing, pinned by every configuration's `tool.files`, and
  changed only by a tool revision, as R6.RDIR.2 fixes the admitted record directories
  (`ADJ-AUTH-OWNER`);
- `adjudicator`, `finding`, `witness_sources` and `replacement` equal the record's own (set equality
  for `witness_sources`) (`ADJ-AUTH-SCOPE`);
- `time` is earlier than the committer time of `L(J)` (`ADJ-AUTH-TIME`). Committer times are
  self-declared, so this is a form check of the record's chronology only. It establishes neither
  when the owner acted nor when the commit was made.

An authorization covers only the replacement it names; a later replacement needs a new
authorization. The owner attribution check goes beyond the migration `approval` precedent, whose
`author` is checked for form only; it is a deliberate change of R6.REC.3 (§6). Beyond it, the tool
neither reads nor checks the owner's approval. The quotation is evidence for the technical reviewer,
who checks it against the owner's record (R6.ADJ.7). A statement of authorization anywhere else (a
token, `method`, `reason`, `grounds`, a commit message, pull-request or Issue text, a run log) is not
an authorization.

### 5.3 Independence and conflicts

**R6.ADJ.4 Independence.** `Parties(W, D, C)`, for a commit `C`, is the set of usable identities
among:
- the `author` or `reviewer` of the record carrying the finding;
- the `author` of: `Q`; `R`; `A`; the citing configuration; each record in `witness.sources` that has
  an `author`; and, for a lineage witness, the predecessor;
- the `reviewer` of: each review in `witness.sources`; each review in `R*(C)` of `Q`, of `R` and of
  `A` that names their exact references; and, for a lineage witness, each review of the predecessor.

*Parties for adverse use.* When `J` is judged as adverse evidence (R6.ADJ.8), `Parties` is
`Parties_J(L(J))`: the same list computed from `J`'s own bindings instead of a candidate discharge,
that is, the record carrying `J.finding`, `Q` = `J.witness.disputed`, `R` = `J.replacement`, `A` =
`J.reassessment`, `J.witness.sources` and, for a lineage witness, `J.witness.edge.predecessor`, with
reviews taken from `R*(L(J))`. No citing configuration enters it. A candidate discharge, a
reassessment or a configuration that `J` does not bind, and any record landing after `L(J)`, cannot
change it.

A party identity that is missing, malformed or not usable is left out of `Parties`; it neither
excludes anyone nor fails the adjudication. The usable-identity rule applies to the adjudicator
(`author`) and to the technical reviewer only.

The adjudicator must be a usable identity, must not be in `Parties`, and must not be a member of
`OWNER_IDENTITIES` (OD-4). The technical reviewer (the `reviewer` of the review of R6.ADJ.7) must be
a usable identity, must not be in `Parties`, must not equal the adjudicator, and must not be a member
of `OWNER_IDENTITIES` (OD-4). Comparisons are of identity strings (R6.RECON.29). For clearing,
`Parties` is `Parties(W, D, M)`; for adverse use, `Parties_J(L(J))`. Any failure is condition
`ADJ-INDEP`.

The `conflicts` declaration is reviewed, not checked. A relationship that the identity strings do not
show (a shared employer, one agent session under two strings) is residual R-ADJ-2. The author of an
earlier adjudication of the same witness is not a party by that fact alone.

### 5.4 Binding

**R6.ADJ.5 Binding.** *Self-consistency* (part of validity): every reference in `J` resolves, and
`witness` reproduces from custody under r9 R6.OBL29.3 as a retained witness: the same `class`,
`disputed` and `edge`; `sources` set-equal to the records forming it; `adverse` set-equal to the
adverse items computed from those records; `original_configuration` equal to the configuration under
which it qualified. *Binding to a discharge* (part of clearing): for a candidate discharge `D` with
reassessment `A` and witness `W`, `J` binds `D` and `W` only if, in addition, `finding` equals `A`'s
`finding` (path, blob sha256 and item), `reassessment` equals the reference of `A`, `replacement`
equals `A`'s `repair.entry`, and `witness` describes `W`. Any failure is condition `ADJ-BIND`. Typed
references establish evidence identity and confer no authority, as owner decision item 2 states for
tokens. r9's tokens are not used in this record kind.

### 5.5 Substance

**R6.ADJ.6 Substance.** The multiset of `grounds[].target` equals the set
`witness.adverse ∪ dissents_addressed`: one ground per target, none missing, none extra. Each
ground's `evidence` contains the git blob id of its target's record, of `Q` and of `R`. `method`
contains the git blob ids of the record carrying the finding, of each element of `witness.sources`,
of `Q`, of `R` and of `A`. Any failure is condition `ADJ-SUBST`. The tool checks coverage and
presence only. Whether the reasoning resolves the objection rests on the technical review (R6.REC.2,
R6.ADJ.7) and is residual R-ADJ-3. A disposition without grounds fails mechanically. An adjudication
whose only basis is an approval, a withdrawal, a rehearing decision or a deletion meets no substance
requirement that a reviewer can accept.

### 5.6 Technical review, validity and admission

**R6.ADJ.7 Technical review.** A review of `J` *qualifies* when it meets R6.REC.6 and R6.RECON.31,
covers every item id of R6.ADJ.2 with `accept`, has an empty or absent `dissent`, is written by a
reviewer allowed by R6.ADJ.4, and its `method` names the git blob ids of `J` and of each element of
`witness.sources`. On the item `authorization`, the reviewer confirms that the quotation, author and
time correspond to the owner's record at `source`. On each `ground:<id>`, the reviewer re-derives the
ground from the git objects, not from the adjudicator's text. A review of `J` that does not accept
every item, or has a non-empty `dissent`, is *adverse to `J`*. Condition `ADJ-REVIEW` fails when no
qualifying review exists, or, for admission, when an adverse review of `J` is not exempt under
R6.ADJ.12 item 2.

**R6.ADJ.8 Validity and admission.**
- *Valid (adverse use).* `J` is valid as adverse evidence when `L(J)` exists and, evaluated over
  `R*(L(J))` with `Parties` at `L(J)`, `J` meets R6.ADJ.2 to R6.ADJ.6 (with R6.ADJ.5 self-consistency
  only) and some review of `J` in `R*(L(J))` qualifies under R6.ADJ.7, with `Parties` =
  `Parties_J(L(J))` (R6.ADJ.4). Validity for adverse use needs no citation by any freeze and is not
  changed by any record that lands after `L(J)` or that `J` does not bind: a later review of `J`,
  adverse or not, a later reviewer of `Q`, `R` or `A`, and the authors of a later reassessment or
  configuration are preserved and reported, and do not cancel it.
- *Pre-admitted.* `J` is pre-admitted for a run when: it meets R6.ADJ.2 to R6.ADJ.6 evaluated at
  the run's `M` and `R*`, with `Parties(W, D, M)`; some review of `J` in `R*` qualifies under
  R6.ADJ.7; the configuration at the candidate freeze `F'` references `J` with kind `adjudication`
  and exactly one qualifying review of `J` with kind `review` (R6.REC.4) (`ADJ-ADMIT`); both lie at
  their stated paths in the reconciliation directory of R6.ADJ.1 (`ADJ-ADMIT`); for each of the two,
  its blob is present at its path in some commit `C` on `M`'s first-parent chain with `C` an ancestor
  of `F'` (`ADJ-LANDED`); and, under the recommended dedicated landing (M5', OD-3), the commit `L1` on
  `M`'s first-parent chain that first holds `J`'s blob at its path differs from its first parent only
  by adding `J` and that review (`ADJ-DEDICATED`). Pre-admission does not depend on any adverse
  review of `J`, on any dissent on `R`, or on R6.ADJ.12.
- *Admitted.* `J` is admitted when it is pre-admitted and no adverse review of `J` in `R*` is
  non-exempt under R6.ADJ.12 item 2, which is evaluated with pre-admitted adjudications only
  (`ADJ-REVIEW`).

An adjudication that is valid but not cited is not applied for clearing. It is read for the
contradiction and upheld rules of R6.ADJ.9 and reported.

### 5.7 Decision

**R6.ADJ.9 `Adjudicated(W, D)`.** In r9's decision, `Adjudicated(W)` reads `Adjudicated(W, D)` and
holds exactly when some adjudication `J` meets all of the following:
1. it is admitted (R6.ADJ.8);
2. it binds `D` and `W` (R6.ADJ.5);
3. its `disposition` is `"cleared"`;
4. no contradicting adjudication exists. A contradicting adjudication is any record in `R*` of schema
   `oi-adjudication/1`, other than `J`, that *matches* `J` and has `disposition` `"upheld"`, and is
   valid for adverse use, or whose validity for adverse use cannot be established (a reference that
   does not resolve, incomplete custody, or no `L(J')` although a review of it that would qualify
   exists in `R*`). An upheld record established invalid for adverse use by a definite failure does
   not contradict. The condition is `ADJ-CONTRA`.

Two adjudications *match* when they name the same `finding` (reference and item), replacements with
the same `blob_sha256` and the same `entry_path` (whatever their paths), `witness.disputed` with the
same `blob_sha256`, and `witness.sources` that share at least one `blob_sha256`. Matching is by blob
identity, as r9 (r1) is, so a byte-identical copy of `R` at another path does not escape an upheld
adjudication.

An upheld adjudication valid for adverse use, cited or not, also makes NR-5 false for a replacement
and witness that it matches in the same sense, with `R` in place of `J.replacement` (`ADJ-UPHELD`;
OD-6). A wrongly upheld adjudication is reversed only through a new replacement whose blob differs: a
later cleared adjudication that matches it is always contradicted, while a replacement with another
blob is a new question with its own authorization. `Adjudicated(W,
D)` is false unless verified records establish it (r9 §2.2). When it is false and `W` is not
otherwise cleared, r9's result stands: FAIL `record-invalid` naming `D`'s reassessment, `W` and each
failed condition, with `retirement-blocked` for the finding. A required unreadable or unverifiable
git object gives ERROR.

### 5.8 Preservation

**R6.ADJ.10 Preservation.** An adjudication changes no finding, witness, record or review. It is
never superseded (`supersedes` is null). A correction is a new adjudication, evaluated with every
earlier one under R6.ADJ.9. No later record narrows, withdraws or replaces an earlier adjudication.
An adjudication, its review and every review of it stay in `R*` after a removal from the current tree
(r9 R6.OBL29.1), and a removed adjudication is evaluated as one that is present. The finding stays in
`category3.findings` whether or not it is discharged, and each witness stays reported with its
sources, its adverse items, and the route and records that cleared it. Clearing a witness discharges
nothing by itself: an applying reassessment is still required wherever R6.RECON.26 and R6.RECON.27
require one.

### 5.9 Fail-closed handling

**R6.ADJ.11 Fail closed.** `Adjudicated(W, D)` is false when any of the following holds: a required
key, record, reference or custody object of `J`, of its review, of `A` or of `R` is missing or does
not resolve; the retained description of `W` cannot be reproduced (r9 R6.OBL29.3); a key of `J` or of
its review is ambiguous or malformed; two reviews of `J` are cited; the reviews of `R` cannot be
enumerated because custody is incomplete; or a contradiction under R6.ADJ.9 (4) exists. Missing or
malformed identity fields of parties are not covered by this rule (R6.ADJ.4). No default, inference
or later statement supplies a missing element. The same inputs give the same result on every run.

### 5.10 Dissent on the replacement and on the adjudication

The recommended default for OD-2 is the refined option (ii) below. It answers the owner's principle,
as the r8 direction quoted in r9 §0 states it, that adjudication "remain available if the original
reviewer is unavailable", and its consequence that resolution must not depend indefinitely on one
reviewer's willingness. Option (i) is kept as an alternative in §8.

**R6.ADJ.12 Dissents.** A *dissent item on `R`* is an item with a verdict other than `accept`, or
`dissent` for a non-empty field, in a review in `R*` that names `R`'s exact reference. For a
pre-admitted adjudication `J` (R6.ADJ.8), `Answered(J)` is the set of usable identities consisting of the reviewer of each
review in `J.witness.sources` and the reviewer of each review referenced in `J.dissents_addressed`.
A review is *later* than `J` when its blob first appears on `M`'s first-parent chain after `L(J)`.

The rule is evaluated in four strata, each using only the results of earlier ones.

1. *Stratum 1: pre-admission.* Pre-admitted adjudications are computed (R6.ADJ.8). This depends on
   no review adverse to an adjudication, no dissent on `R` and nothing below.
2. *Stratum 2: exemption (refined (ii)).* For each pre-admitted adjudication `J` that binds `D` and
   is cleared, `Answered(J)` is computed. An adverse review of `J` is exempt when it is later than `J`,
   its reviewer is in `Answered(J)`, and each of its non-accept verdicts lies on an item `ground:<id>`,
   `disposition` or `dissents` (a non-empty `dissent` field alone does not prevent exemption). A
   non-accept verdict on `authorization`, `binding` or `conflicts` is never exempt, so the reviewer
   best placed to detect a forged quotation keeps a mechanical veto on it. A dissent item on `R` is
   exempt for `D` when its review is later than `J` and its reviewer is in `Answered(J)`. An exempt
   review is preserved and reported. New substance from that reviewer enters only as a category-3
   finding (R6.RECON.26), which binds under its own rules.
3. *Stratum 3: admission.* `J` is admitted when it is pre-admitted and every adverse review of it is
   exempt under stratum 2 (R6.ADJ.8, `ADJ-REVIEW`). A later adverse review of `J` by a reviewer
   outside `Answered(J)`, or on a non-exempt item, therefore defeats `J` until a further adjudication
   answers it.
4. *Stratum 4: effect on `R` and precondition.* A dissent item on `R` is *addressed* for `D` when it
   appears in `dissents_addressed` of an admitted cleared adjudication that binds `D`, and *disregarded*
   when it is addressed, or exempt under stratum 2 through an adjudication that stratum 3 admits. For
   evaluating R6.REC.6 on `R` and the no-dissent conditions of r9 NR-3 and NR-5 for `D`, disregarded
   items are left out. `D`'s discharge applies only if every witness relying through `R` is then
   cleared by some route (NR-5, `Inapplicable`, route 1 or `Adjudicated`), and every dissent item on
   `R` is disregarded (`ADJ-DISSENT`). A later dissent item on `R` that is neither addressed nor
   exempt therefore blocks the discharge. Where no adjudication is admitted for `D`, no item is
   disregarded, and r9 and R6.REC.6 apply unchanged.

*Non-circularity.* Stratum 1 reads no adverse review of an adjudication and no dissent on `R`.
Stratum 2 reads stratum 1 and the reviews. Stratum 3 reads strata 1 and 2. Stratum 4 reads stratum 3,
R6.REC.6 and NR-5, and none of these feeds back into strata 1 to 3. So each input set has exactly one
result. In particular, whether a later review of `J` by an answered reviewer is exempt is fixed in
stratum 2 before admission is decided.

### 5.11 Result and detection

**R6.ADJ.13 Result fields.** Each element of `category3.findings` gains `adjudications`: one entry
for every `oi-adjudication/1` record in `R*` that names the finding,
`{path, blob_sha256, witness_sources, disposition, landing, valid_adverse, pre_admitted, admitted,
applies, failures, exempt_reviews}`. `landing` is `L(J)` or null. `failures` lists the condition ids
of R6.ADJ.3 to R6.ADJ.12. `exempt_reviews` lists the references of the reviews R6.ADJ.12 exempts. A
witness cleared by adjudication is reported with route `adjudication` and the references of `J` and
its review. The name avoids r9 R6.OBL29.8's `witness`, which is a commit id. No new outcome class is
introduced.

**R6.ADJ.14 Detection compatibility.** An adjudication record and its elements contain no key
`reviewed` or `verdicts` and no `schema` value beginning `oi-review-record/` or `oi-reconciliation/`
at any depth. So R6.RECON.35 does not select a parseable adjudication as a record of class (a) or
(b). A file of schema `oi-adjudication/1` that violates this, or that does not parse and whose text
contains those prefixes, is classed by R6.RECON.35 as it stands: a malformed record, and a malformed
finding binding at run level where its text holds `invalidates`. Under r9 R6.OBL29.2 such a finding
binds from history. This fails closed but cannot be undone, so writers follow two practices: cite
records by blob id and path, never by schema string, in `reasoning` and `method`; and parse-check the
file strictly against `adj.record` before it is landed.

***

## 6. Interaction with OBL-29 r9 and Amendment 6 r13

On adoption, these would be separate amendments. None is made here.

| Location | Proposed change |
|---|---|
| r9 §2.2 route 2 and §5.6 "Route 2 adjudication" | route 2 is `Adjudicated(W, D)` of R6.ADJ.9. The sentence "Route 2 is therefore unavailable through existing records ... until an owner-authorized admission route exists" is replaced by a citation of R6.ADJ.1 to R6.ADJ.14. NR-5 and route 1 are unchanged. The original reviewer's resolution stays available and needs no adjudication. |
| r9 NR-3 and NR-5, "no eligible review of `R` in `R*` dissents" | gains R6.ADJ.12's disregard of addressed and exempt items, under its precondition |
| r9 decision | `Adjudicated(W)` reads `Adjudicated(W, D)`. Otherwise unchanged. |
| r9 R6.OBL29.8 | `adjudications` added beside `present_at_M` and `witness` (R6.ADJ.13) |
| r13 R6.REC.1 and R6.RECON.1 | the reconciliation directory also holds adjudication records and their reviews (R6.ADJ.1) |
| r13 R6.REC.3 | deliberate change: "The `authorization` of an adjudication record (R6.ADJ.3) quotes that approval for the reviewer. The tool checks its form, its scope, its time against the landing, and that its `author` is a member of `OWNER_IDENTITIES`. The last check is attribution, not verification of the approval, which the tool still neither reads nor checks." |
| r13 R6.REC.4 and R6.REC.5 | exception: an adjudication record and its reviews found in `R*` are read for R6.ADJ.9's contradiction and upheld rules and reported, without being referenced by the configuration. They are never used to clear unless cited. |
| r13 R6.REC.6 | add R6.ADJ.12's disregard of addressed and exempt items on `R`, limited to the discharge the adjudication binds and to its precondition |
| r13 R6.RECON.31 | one item-id row for `oi-adjudication/1` (R6.ADJ.2) |
| r13 R6.RECON.33 and R6.CFG.4 | one kind row: `adjudication` → `oi-adjudication/1`. `oi-owner-authorization/1` stays undefined. |
| r13 R6.RECON.29 | the new tables enter the single-definition rule, and their conformance mutants are generated as for the other kinds |
| r13 R6.RECON.36, R6.OUT.18 and the result JSON Schema | the `adjudications` field of R6.ADJ.13 and its element schema |
| r13 generators | the REQUIREMENTS, EXPECTATIONS and CONFORMANCE-MUTANTS generators gain the new requirements, expectation rows (runner null) and the mutants of the new tables |
| r13 tool constants | `OWNER_IDENTITIES`, beside the admitted record directories (R6.RDIR.2) |

Unchanged: R6.RECON.26's blocking rule and finding forms; R6.RECON.27's reassessment and its Keys
(an adjudication clears a witness, never a finding); R6.RECON.28; R6.RECON.35's selection; the token
convention (r9 §2.2, owner decision item 2), which keeps its role in NR-4 and NR-5 and is not used for
authority. Adjudication adds no route that lifts a block without an applying reassessment and a new
freeze (R6.CFG.3, AGENTS.md §A.50 item 5).

**Safety (no bypass).** Each conjunct of r9's `blocked(D, W)` is unchanged except `Cleared`, which
gains one disjunct, `Adjudicated(W, D)`, false unless R6.ADJ.9 holds. Adverse evidence (an upheld
adjudication) takes effect by validity alone: leaving it out of a freeze, landing a later adverse
review of it, adding a party after its landing, giving a later reassessment or configuration its
adjudicator's identity string, or copying `R` to another path does not cancel it. The disregard of R6.ADJ.12
applies only to items an admitted cleared adjudication addresses, or to repeated objections of
reviewers it has answered on its grounds, disposition and dissents (never on its authorization,
binding or conflicts), and only when every relying witness is cleared and every other dissent item
is addressed. So every discharge that r9 blocks stays blocked unless an admitted, bound,
authorized, independent, substantive, uncontradicted adjudication exists, subject to residuals
R-ADJ-1 to R-ADJ-3.

**Reachability.** An adjudication can meet R6.ADJ.9 without any act of `V`'s reviewer. So route 2
is reachable when that reviewer is unavailable, has a missing or unusable identity, or disputes `R`,
before or after the adjudication. It needs one authorized adjudicator and one technical reviewer
outside `Parties` and `OWNER_IDENTITIES`, one owner authorization and a dedicated landing on `main`
before `F'`. A mixed case, one witness adjudicated and another resolved by NR-5, is reachable
(CONTROLS.json: ADJ-P-UNAVAILABLE, ADJ-P-DISPUTED, ADJ-P-UNUSABLE-IDENTITY, ADJ-P-MISSING-REVIEWER,
ADJ-P-ADDRESSED-REDISSENT, ADJ-P-MIXED-NR5, ADJ-P-LANDING-SEARCH-AT-F).

***

## 7. Residual risks

- **R-ADJ-1. Forged authorization.** The tool cannot tell a genuine quotation of the owner from a
  fabricated one that a colluding technical reviewer accepts and that reaches `main` (Claim I, S6).
  Guards: procedural only. The owner's merge approval of a dedicated landing (M5, M5'), at which the
  owner sees a quotation of the owner's own words with its `source` and nothing else, and permanence
  in `R*` (M7). An answered reviewer's non-accepting verdict on `authorization` is never exempt
  under refined (ii) (R6.ADJ.12 stratum 2), so the original reviewer keeps a mechanical veto on the
  quotation. OD-3 lists the strengthenings.
- **R-ADJ-2. Identity.** Identity strings are self-declared (r9 R-8). Impersonation of the
  adjudicator, the reviewer or a party, relationships the strings do not show, and sock identities
  that file new dissents after an adjudication (which R6.ADJ.12 does not exempt) are guarded only
  procedurally. Evaluating adverse validity at `L(J)` from `J`'s own bindings stops records that land
  after `L(J)`, or that `J` does not bind, from cancelling an upheld adjudication, forged identity
  strings in them included. A forged identity in a record that `J` binds and that is present at
  `L(J)` can still make `J` invalid from the start, and remains guarded only procedurally.
- **R-ADJ-3. Substance.** Coverage of every adverse item and dissent is mechanical. Whether each
  ground's reasoning resolves its objection rests on the technical review, as every judgment in r13
  does (R6.REC.2).
- **R-ADJ-4. Termination.** Under refined (ii), a reviewer an adjudication has answered cannot
  defeat it by repeating the objection, but a new reviewer can, and a new category-3 finding binds as
  in r13. Under option (i), the answered reviewer can also defeat it each round.
- **R-ADJ-5. Availability of adjudicators.** Reachability needs one authorized adjudicator and one
  technical reviewer outside `Parties` and `OWNER_IDENTITIES`. Where no such person exists, the
  witness stands, which fails closed.
- **R-ADJ-6. Custody.** `Adjudicated` and adverse validity depend on r9's custody of the witness and
  the review enumeration. Where custody is incomplete, clearing fails and adverse evidence that cannot
  be evaluated contradicts (R6.ADJ.9, R6.ADJ.11). r9's squash and rebase gap (r9 §6) applies to
  adjudication records as to every other record, and to `L(J)` in particular.
- **R-ADJ-7. A wrongly upheld adjudication.** It binds its replacement, by blob, permanently. The
  only reversal is a replacement with another blob (R6.ADJ.9).

***

## 8. Owner decisions this design leaves

| Id | Decision | Alternatives and consequences | Design default | Reviewer recommendation (#1605 comment 7197900888) |
|---|---|---|---|---|
| OD-1 | Mechanism | (A) as §5; (B1); (C3); none (route 2 stays unavailable, and RQ7 stays unmet) | (A) | (A), after the F1 to F5 revisions |
| OD-2 | Termination against a persistent disputant | (ii) refined, R6.ADJ.12: a later dissent on `R`, or adverse verdict on `J`'s grounds, disposition or dissents, by a reviewer `J` has answered is preserved and does not defeat `J` (verdicts on its authorization, binding or conflicts still do); any other later dissent defeats it; new substance enters only as a category-3 finding (RQ7 terminates; RQ6 narrowed for repeated objections only). (i) per round: every later dissent defeats `J` until a further adjudication answers it (RQ6 in full; resolution can depend indefinitely on one reviewer's willingness, which conflicts with the owner's principle that adjudication remain available) | (ii) refined; not decided | (ii) refined; not (i) |
| OD-3 | Strengthening the authorization | (a) `OWNER_IDENTITIES` and the dedicated landing M5'; (b) a standing `ADJUDICATORS` tool-constant registry, with or without the pre-dispute variant; (b') a per-dispute registry entry in tool code; (c) a separate authorization record kind; (d) a quorum of k technical reviewers; (e) an authenticated channel: an owner signature with a pinned key, the web-flow variant (pinned host key and an owner-authored landing merge, with the API-commit caveat of §2.1), or a host read; each needs an R6.REC.3 decision | (a) | (a) plus the dedicated landing; (b') and the web-flow variant of (e) kept as later options |
| OD-4 | May the owner be the adjudicator or the technical reviewer? | Allowed: removes the separation between authorizer and judge. Barred: the authorizer holds neither judging role; the owner's merge approval still covers the R-ADJ-1 self-check. | barred in both roles (R6.ADJ.4) | barred in both roles |
| OD-5 | Scope | witness clearance only, or also adjudication of a mistaken independent finding (r9 §5.6), which would extend R6.RECON.27's `repair: null` route and needs its own design | witness only | witness only |
| OD-6 | Effect of an upheld adjudication on NR-5 | blocks NR-5 for the same finding, replacement and witness, by validity alone, or does not | blocks | blocks, once F1 and F2 are fixed (done in r2) |
| OD-7 | Dissent disregard | adopt R6.ADJ.12's disregard in R6.REC.6 and r9 NR-3 and NR-5 with its precondition (needed for the dispute case of RQ7), or not (adjudication then reaches only the unavailable and unusable-identity cases) | adopt | adopt, with the corrected precondition (done in r2) |

Adoption of this design, any amendment of r9 or r13, any tool revision, freeze, trial, dispatch and
merge each need their own owner decision (AGENTS.md §A.50 items 1 and 5, §A.51 item 6).

***

## 9. Reference trace (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7197443528 | authority, the seven requirements, token condition | provenance; author and time quoted in §0 |
| `5ad8837521de0a26734266a64f91548fd3dcff1e` (r13), PR #1593, #1593 comment 7193277489 | R6.REC.1 to .7, R6.CFG.4, R6.RDIR.2, R6.RECON.1, .26 to .36, R6.OUT.18 | support off `main` (PR #1593 open); the cited requirements are quoted or paraphrased here |
| `77a73c022091f598cf807fcf89d66c3cf43208de` (r9), PR #1601 | §0 (the owner's r8 direction), §2.2 route 2, NR-3 to NR-5, token rule, decision, R6.OBL29.1, .2, .3, .8, R-8, §5.6 | support off `main` (PR #1601 open) |
| #1601 comment 7197262397, finding 4 | the gap | provenance |
| `2de8462946c65dcf0f004a559fd12b9c18c22ceb` (r1), PR #1605, #1605 comment 7197900888 | the revised text and the review findings answered | provenance |
| `6a0afe052b30c6a14d32e03960df3c1df72c4101` (r2), #1605 comment 7198103680 | the revised text and the re-review findings answered | provenance |
| `942bd5ea1fd09f4223012b0755bce2d6da07c44a` | `main` at drafting; AGENTS.md §A.42, §A.46, §A.47, §A.50, §A.51; the signed merge commit of §2.1 | support on `main` |

The design asserts no established result. Its claims (Claim I, the comparison, safety and
reachability) are for independent review (REVIEW-BRIEF.md).
