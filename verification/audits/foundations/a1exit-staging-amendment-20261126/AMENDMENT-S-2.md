# A1 staging amendment r2, supplement S-2: procedural reviewer independence (paper draft r1)

**Status.** Draft r1, for independent review and the owner's adoption of the exact reviewed text. It
supersedes supplement S-1 (`AMENDMENT-S-1.md` in this directory, adopted at
`3bc3693c66c65d768bc072b65d07f045fe8a23f5`, with the defaults OQ-S1-1 to OQ-S1-5). S-1 stays in force
until the owner adopts S-2. Adoption, implementation, staging, freeze and execution keep their
separate gates.

**Authority.** Owner decision (amaybaum, 2026-11-27, coordinating session; recorded at #1169 comment
7213109404, 2026-11-27T08:04:27Z). The approved text includes, quoted:

> - Draft S-2 to supersede S-1 as outlined, subject to independent review and owner adoption.
> - Agents with repository write permissions are presumed to exercise delegated owner authority within their assigned responsibilities.
> - Personal owner approval remains necessary only for explicitly reserved decisions.
> - Retain recorded session identifiers, non-authorship and independence declarations, exact evidence binding, adverse-evidence preservation and fail-closed verification.
> - Remove the identity registry, designation and withdrawal procedures, registry freeze bindings and owner identity registration.
> - Restate all affected adopted clauses consistently. Avoid replacing the registry with another unnecessarily complex identity mechanism.
> - Keep registry-dependent S-1 implementation paused. Reuse applicable completed work.

and the qualification: "Independence is procedural: reviewers declare non-authorship and any relevant
dependency on the writer, and the tool enforces only what it can verify mechanically, without
claiming to authenticate identities." The same decision: "Prefer the simplest governance mechanism
sufficient to protect scientific integrity." A later steer relayed by the coordinating session
supplies the test for each clause: keep it if it protects evidence validity or fail-closed
verification; drop it if it exists only for the registry.

**Goal link (AGENTS.md §A.47).** Serves A1 retirement (#1477). It would decide how a review of an A1
record shows that its reviewer is independent of the record's writer when all sessions write through
one account, with no registry.

## 1. Preserved results (the controls of this amendment)

Stated before the replacement rule. S-2 is acceptable only if every result below holds after it,
each checked by the controls named in §7.

| Id | Result preserved | Where it is stated now | Controls |
|---|---|---|---|
| P1 | Every fail-closed outcome that does not rest on authenticating an identity: a missing or malformed `author` or `reviewer` fails record lint; a review that cannot show independence counts as no review; an unreadable required object is ERROR | R6.REC.6, R6.REC.17, R6.OBL29.7, S-1 S1.8 | O1, O5, S2-MALFORMED, S2-DECL-MISSING |
| P2 | Exact evidence binding: `reviewed` names the exact `{path, blob_sha256}`; `revision` names a commit reachable from the review's root that holds those bytes | R6.RECON.31 `reviewed`, S-1 §3 | S1-REVISION-MISMATCH, S1-REVISION-POST-F, O2 |
| P3 | Adverse-evidence preservation: a finding is detected before lint; an invalidating review lapses only when its reviewer is the same identity as the exact named record's author; every other defect is a form failure that still blocks; a genuine finding stays in `Obl` | R6.RECON.26 Form (i), r9 R6.OBL29.1/.6, r9 Amendment 1 A1.1–A1.5 | S1-INVALIDATING-SAME-ID, S2-INVALIDATING-DECLARED, S2-INVALIDATING-MALFORMED, S2-NO-RETRO-LAPSE, the r9 Amendment 1 rows |
| P4 | S1.9's permanent block, where it does not depend on the registry: an invalidating review whose `reviewer` is not an identity string can never be resolved under r9 NR-5 | S-1 S1.9 "For the owner", r9 NR-5 | N-REFREEZE-REVIEW-WITNESS-NO-IDENTITY, S2-INVALIDATING-MALFORMED |
| P5 | The S11-2a binding to the configuration admitted at `F` | `AMENDMENT-S11-2a.md` (adopted at `6de7efa4`) | its own controls, unchanged |
| P6 | The r9 rules (NR-1 to NR-5, the token rule, R6.OBL29.*) and the custody rules (R6.CUST.*), apart from the words that compare identities | r9 `DESIGN.md`, custody `DESIGN.md` on `main` | the r9 and custody controls, unchanged |
| P7 | A writer never reviews its own record; item coverage and verdict rules of R6.REC.6 and R6.REC.13; the widening reviewer differs from the author and from every ordinary reviewer; OD-4 (the owner is neither adjudicator nor technical reviewer) | R6.REC.2, R6.REC.6, R6.REC.13, R6.ADJ.4 | O3, A4r, A12r, Z5, S2-ROOT-ROLES, ADJ-* |
| P8 | No identity is taken from an argument, a commit author or a host record | S-1 §5 "Registry source for controls" (its last sentence) | S2-FIELD-ONLY |

## 2. The replacement rule

**S2.1 Identity string.** `author` and `reviewer`, and every other key whose type is identity
string, hold the identifier the writing party records for itself: an agent session records the
session or subagent identifier its platform gives it; a person records their GitHub login. The
owner's identity string is the login `amaybaum`. An identity string matches, as a whole string,

    [A-Za-z0-9][A-Za-z0-9._:-]{0,127}

and is not made only of digits (a run or check id). So it holds no whitespace, no `/` (no URL or
path) and no non-ASCII character (no look-alike letters). A string that fails this is not an identity
string. A session whose platform identifier does not match records it with every other character
replaced by `-`; the tool cannot tell, and does not check, which form was used.

**S2.2 Comparison.** The *key* of an identity string is the string with ASCII letters made lowercase
and the characters `.`, `_`, `:` and `-` removed. Two identity strings are the **same identity** when
their keys are equal. So `Session_Fixture-Writer`, `session.fixture-writer` and `SESSIONFIXTUREWRITER`
are one identity; a respelling by case or separator does not make two. Two distinct platform
identifiers whose keys collide are treated as one, which can only refuse a review in lint (P1); its
effect in detection is stated in S2.5.

**S2.3 What a review records.** Each `oi-review-record/1` carries:
- `reviewer`: an identity string (S2.1);
- `reviewed`: the exact `{path, blob_sha256}`, as now;
- `revision`: the commit the reviewer read, with S-1 §3's acceptance and roots unchanged (`F` in chain
  record lint; `REV` on the post-freeze route; effective `M`, or `F` and `REV` where the walk reaches
  them, for detection and finding lookups; effective `M` for a custody review);
- `independence`: an object with exactly two keys, both required:
  - `not_author`: the literal `true`. The reviewer declares that it did not write the reviewed record
    or its evidence and did not direct their writing;
  - `depends_on`: an array, possibly empty, of identity strings, no two the same identity: every party
    on which the reviewer has a relevant dependency for this review (the session that started or
    instructs it, a session whose work it relied on beyond the reviewed record, a session sharing its
    context). Where the reviewer depends on the writer, it names the writer.

**S2.4 What the tool checks.** For a review and a set `X` of identity strings that the role must be
independent of (§3), the review is *independent of `X`* when:
1. `reviewer` is an identity string;
2. `independence` is present, has exactly its two keys, `not_author` is `true`, and `depends_on` is
   an array of identity strings with no two the same identity;
3. `reviewer` is the same identity as no member of `X`;
4. no element of `depends_on` is the same identity as a member of `X`.

Members of `X` that are not identity strings are skipped here; the record that carries one fails its
own lint (R6.REC.6), and R6.ADJ.4 already leaves them out of `Parties`. A declaration that names a
member of `X` contradicts the independence it would otherwise claim, so condition 4 is mechanical.

**S2.5 Outcomes.**
- *Record lint* (R6.REC.6, R6.REC.13, R6.CUST.8). A review that is not independent of its `X`, or
  whose `revision` fails §3 of S-1, counts as no review; the reviewed record then lacks its required
  review and is FAIL `record-invalid`. A record whose `author` is not an identity string fails lint.
- *Detection* (R6.RECON.26 Form (i), r9 Amendment 1). A review carrying `invalidates` or
  `invalidated` is disqualified, with no finding, only when its `reviewer` is an identity string that
  is the same identity as the `author` of the exact record its `reviewed` names, that record being in
  `R*`. When that record is absent from `R*`, the review is a provisional block (Amendment 1). In every
  other case it is a genuine finding; a malformed `reviewer`, a missing or malformed `independence`,
  a `depends_on` naming the author, or a failed `revision` is a form failure that still blocks. A key
  collision (S2.2) in this position needs the record's author field to carry the reviewer's key, which
  is fixed in the exact bytes the reviewer read; it is the same residual as a self-review.
- *Permanent block* (P4). An invalidating review whose `reviewer` is not an identity string cannot be
  resolved under NR-5, since no `Z` can be the same identity. It is lifted only by dropping the bound
  edit (R6.RECON.26), or by a repair-bearing reassessment whose review witness is cleared through
  route 2 as the adopted #1605 §6 rows provide (R6.ADJ.9), with a new freeze. S-1 S1.9 stated that
  route 2 does not exist; the #1605 §6 rows, adopted at #1169 comment 7208869709 before S-1, provide
  it. S-2 changes neither.

**S2.6 What the tool does not check.** It does not authenticate any identity string: it cannot tell
whether a session recorded its true identifier, whether two strings name one session, whether a
declared `depends_on` is complete, or whether `not_author` is true. A session that records an invented
identifier, or omits a dependency, passes every mechanical check. These rest on the reviewer's own
declaration and on review, as R6.REC.12's residual limit states: "The tool can check that the role
fields differ, not who actually wrote the records; identity rests on the writer's and the reviewer's
own recorded statements." S-2 neither narrows nor widens that limit. Identities are read only from
record fields, never from an argument, a commit author or a host record (P8).

## 3. Roles and the set `X`

| Role | `X` (S2.4) |
|---|---|
| Ordinary review (R6.REC.6), custody review (R6.CUST.8) | the reviewed record's or version's `author` |
| Widening review (R6.REC.13) | the superseding record's `author` and every ordinary reviewer of it |
| Allow root, class root and configuration (staging r2 §2, §3) | writer, ordinary reviewer and widening reviewer: each reviewer is independent of the other two roles, so the three are pairwise different identities and neither reviewer declares a dependency on another of the three |
| r9 NR-3 review of `R` | the parties NR-3 lists |
| r9 NR-5 resolver `Z` | the authors of `R`, of the disputed record and of the cited reassessment; and `Z`'s `reviewer` is the same identity as `V`'s |
| Adjudication technical reviewer (R6.ADJ.4, R6.ADJ.7) | `Parties`, the adjudicator, and each member of `OWNER_IDENTITIES` |

**"Distinct" for the allow root.** Staging r2's "distinct eligible identities" means: three
identity strings, pairwise not the same identity (S2.2), each reviewer independent of the other two
roles (S2.4). That is all the tool checks. Whether three strings name three sessions rests on their
declarations (S2.6).

## 4. Owner authority

**S2.7 Delegated by default.** Approval of a record, a review or a staging step within an agent's
assigned responsibility is given by that agent's delegated authority (#1169 comment 7213109404); it
is not a field and the tool does not read it. A decision reserved to the owner (AGENTS.md §A.50,
including the freeze of `F`, merges into `main`, and amendments of a frozen plan) is a recorded owner
decision, quoted with author and time in the record that relies on it (AGENTS.md §A.42 item 7).
S-2 changes no AGENTS.md text (OQ-S2-5).

**S2.8 Owner identities.** `OWNER_IDENTITIES` stays the tool constant of R6.ADJ.3 (`["amaybaum"]`),
pinned with the tool files and changed only by a tool revision. It is not a registry: it is read by
two attribution checks and one separation check, all by S2.2:
- R6.ADJ.3: the adjudication `authorization.author` is the same identity as a member
  (`ADJ-AUTH-OWNER`). The authorization remains an owner decision (OQ-S2-3);
- `migration.approval`: `author` is the same identity as a member (an edit-id migration needs the
  owner's approval in advance, AGENTS.md §A.48 item 3; OQ-S2-4);
- OD-4 (R6.ADJ.4): neither the adjudicator nor the technical reviewer is the same identity as a member.

Each is attribution or separation by string, not verification of the owner's act; R-ADJ-1 and R-ADJ-2
are unchanged.

## 5. Clause replacement

**S-1's own clauses.**

| S-1 clause | Under S-2 |
|---|---|
| S1.1 registry location and form | withdrawn |
| S1.2 owner designations, withdrawals, admitted threads, registry review, freeze approval quoting the registry SHA-256 | withdrawn |
| S1.3 party closure | withdrawn; replaced by same identity (S2.2) and declared dependency (S2.4) |
| S1.4 registry well-formedness | withdrawn; the identity-string grammar (S2.1) remains |
| S1.5 append-only across freezes | withdrawn |
| S1.6 scope | withdrawn (S-1 itself kept the owner's "review-scope requirements" in the item coverage of R6.REC.6 and R6.REC.13, which stay) |
| S1.7 independence | replaced by S2.4 and §3 |
| §3 what a review binds | `reviewed` and `revision` kept as written; `platform_ref` and the posted digest withdrawn; `independence` added (S2.3) |
| S1.8 lint | replaced by S2.5 (lint) |
| S1.9 detection and permanent block | replaced by S2.5 (detection, permanent block); lapse on same identity only, as before |
| §5 "Registry source for controls" | withdrawn, except its last sentence, kept as P8 and S2.6 |
| §6 inventory effect | superseded by §8 |
| §7 tool changes | superseded by §8 |
| §8 controls | §7 |
| OQ-S1-1 every record the tool reads | kept: S-2 applies to every record the tool reads |
| OQ-S1-2 registry read from `F` only | void |
| OQ-S1-3 spawning lineage as one party | void; a spawning dependency is declared in `depends_on` |
| OQ-S1-4 identities not authenticated | kept (S2.6) |
| OQ-S1-5 form comments as designations | void (OQ-S2-6) |

**The adopted clauses S-1 replaced or added, restated.**

| Clause | Text under S-2 |
|---|---|
| staging r2 §2, "One-time transition" | "… and the identity string (S-2 S2.1) of its actual author." |
| staging r2 §2, "Initial widening review" | "The writer, ordinary reviewer and widening reviewer are pairwise not the same identity, and each reviewer is independent of the other two roles (S-2 S2.4, §3)." |
| staging r2 §2, "In a later, separately approved activation" | S-1's added sentence (registry pin and its SHA-256 in the `F` approval) withdrawn; r2's text stands |
| staging r2 §2, "Prior-freeze continuity" | S-1's added S1.5 check withdrawn; r2's text stands |
| r13 R6.RECON.29, row "identity string" | "`author` and `reviewer`: an identity string as S-2 S2.1 defines it; not a run, check, Issue or URL. Two identity strings are the same identity when their keys are equal (S-2 S2.2)." |
| r13 R6.RECON.29, conformance mutants | near-miss mutants for an identity string: a URL (existing), surrounding space, an inner space, a non-ASCII look-alike letter, digits only, the empty string, 129 characters. S-1's registry mutants (unregistered id, prefix differing from kind) withdrawn |
| r13 R6.REC.6 | "`reviewer` equal to `author`" reads "a review that is not independent of the record's `author` (S-2 S2.4)"; "a `reviewer` value that points to a tool run, a CI run, a check run or an Issue" reads "an `author` or `reviewer` value that is not an identity string (S-2 S2.1)" |
| r13 R6.REC.13 | "by a non-author reviewer other than the record's own reviewer" reads "by a reviewer independent of the record's author and of every ordinary reviewer of the record (S-2 S2.4)" |
| r13 R6.REC.3 (with the adopted #1605 row) | its sentence on owner approval reads as S-2 S2.7; the #1605 attribution sentence stands, with `OWNER_IDENTITIES` compared by S2.2 |
| r13 R6.RECON.26 Form (i) | "… unless its `reviewer` is an identity string that is the same identity as the `author` of the record its `reviewed` names (S-2 S2.2). Only that disqualifies it. A malformed `reviewer`, a missing or malformed `independence`, a `depends_on` naming that author, or a failed `revision` is a form failure that still blocks (S-2 S2.5)." The provisional-block clause of r9 A1.5 follows |
| r13 table `review.record` | `reviewer`: acceptance "independent (S-2 S2.4) of the reviewed record's `author`; for a widening review, also of every ordinary reviewer of the superseding record". Row `revision` kept (S-1 §3). Row `platform_ref` withdrawn. New row `independence`: object `{not_author: true, depends_on: array of identity strings}`, required, acceptance S-2 S2.4 |
| r13 R6.RECON.33 kind table | S-1's row `sessions` withdrawn |
| r13 R6.RECON.31 item-id table | S-1's row for the registry withdrawn |
| r13 table `migration.approval`, `author` | "the owner's identity string; the same identity as a member of `OWNER_IDENTITIES` (S-2 S2.8)" |
| r9 Amendment 1, genuine finding (§1) and A1.1 | "whose `reviewer` is not the same identity as that record's `author` (S-2 S2.2); any other defect of the review is a form failure (S-2 S2.5)" |
| r9 Amendment 1, A1.2 | "shows `author` the same identity as `reviewer`" |
| r9 Amendment 1, A1.5 | "is disqualified if its `reviewer` is an identity string that is the same identity as that record's `author`" |
| r9 NR-3 | "Its `reviewer` is independent (S-2 S2.4) of the `author` of …, and of the `reviewer` of …" (the same lists) |
| r9 NR-5, Resolver | "`Z`'s `reviewer` is the same identity as `V`'s `reviewer`, and `Z` is independent (S-2 S2.4) of the `author` of `R`, of the disputed record and of the cited reassessment" |
| custody R6.CUST.8 | "whose review is independent (S-2 S2.4) of the version's `author`, and which meets S-1 §3 with root effective `M`" |
| #1605 R6.ADJ.3 | `ADJ-AUTH-OWNER` compares by S2.2 (S2.8); otherwise unchanged |
| #1605 R6.ADJ.4 | "usable identity" is an identity string (S-2 S2.1); comparisons are by S2.2; the technical reviewer's review is independent of `Parties`, the adjudicator and `OWNER_IDENTITIES` (S2.4); OD-4 as S2.8; `conflicts` stays reviewed, not checked |

R6.REC.2, R6.REC.12, and every item-coverage, exact-blob and verdict rule are unchanged.

## 6. Effect on existing records

At `origin/main` `4e2f034a7ea5a403e31571a89cf43011f02ea8ce` and `origin/tools/a1-ledger-coverage-r6`
`eeeaee74ea5f64f8f51f3cbebe26b35a22f44968`, no record under `verification/audits/` has schema
`oi-review-record/1` (the only matches are the design text and its generator), so no review, finding
or witness changes outcome. The tool-branch records whose `author` is `implementation-writer-20261123`
now carry an identity string; they still lack reviews and fail lint as before. Free-text authors with
spaces are not identity strings and fail as under S-1.

## 7. Controls

Each is a specification until implemented.

**Retained from S-1, restated where marked.**

| Id | Setup | Expected |
|---|---|---|
| S1-POS (restated) | Writer `w1`, ordinary reviewer `r1`, widening reviewer `x1`, pairwise different identities, each review with valid `revision` and `independence` naming none of the other roles | the root passes record lint |
| S1-LOGIN (restated) | `author` and `reviewer` are both the shared GitHub login | same identity: review counts as no review; FAIL `record-invalid` |
| S1-REVISION-MISMATCH | as in S-1 | review counts as no review |
| S1-REVISION-POST-F | as in S-1 | both bind normally |
| S1-INVALIDATING-SAME-ID | as in S-1 | disqualified; no finding |

**Void** (they test only the registry): S1-UNREGISTERED, S1-SAME-PARTY, S1-SAME-PARTY-REVERSED,
S1-SAME-PARTY-CHAIN, S1-SPAWNED, S1-MISSING-LINK, S1-DANGLING-LINK, S1-DUP-ID, S1-NO-REGISTRY,
S1-REGISTRY-BY-ARGUMENT (its property moves to S2-FIELD-ONLY), S1-DESIGNATION, S1-WITHDRAWN,
S1-WITHDRAWAL-KEEPS-LINKS, S1-WITHDRAWAL-REMOVED, S1-REGISTRY-REVIEW-PARTIAL, S1-PLATFORM-REF,
S1-REGISTRY-CHANGED, S1-SCOPE-BOUNDARY, S1-OUT-OF-SCOPE, S1-RETRO-MERGE (its property moves to
S2-NO-RETRO-LAPSE). Replaced: S1-WIDENING-SAME-PARTY and S1-WIDENING-AUTHOR-PARTY by S2-ROOT-ROLES;
S1-INVALIDATING-SAME-PARTY by S2-INVALIDATING-DECLARED; S1-INVALIDATING-UNREGISTERED by
S2-INVALIDATING-MALFORMED.

**Added.**

| Id | Setup | Expected |
|---|---|---|
| S2-RESPELL | reviewer `Session_Fixture-Writer` on a record by `session.fixture-writer`; variant `SESSIONFIXTUREWRITER` | same identity: review counts as no review; FAIL `record-invalid` |
| S2-MALFORMED | reviewer (or author) with surrounding space, inner space, a Cyrillic look-alike letter, digits only, empty, 129 characters, a URL | not an identity string: FAIL `record-invalid` |
| S2-DECL-MISSING | `independence` absent; variants: `not_author` false or `"true"`, an extra key, `depends_on` not an array, holding a malformed string, or two same-identity elements | review counts as no review |
| S2-DECL-AUTHOR | `depends_on` names the author; variant: names it respelled | review counts as no review |
| S2-ROOT-ROLES | allow root: widening reviewer the same identity as the writer; as the ordinary reviewer; ordinary reviewer declaring a dependency on the widening reviewer; widening reviewer declaring one on the writer | each: FAIL `record-invalid` |
| S2-INVALIDATING-DECLARED | invalidating review, record in `R*`, `depends_on` naming the author, reviewer a different identity | genuine finding with a form failure; FAIL `record-invalid` and `retirement-blocked` |
| S2-INVALIDATING-MALFORMED | as above, reviewer not an identity string; variant: `independence` missing | genuine finding with a form failure; blocks; no `Z` meets NR-5 |
| S2-NO-RETRO-LAPSE | a genuine finding; later, a record or review declaring that its reviewer depends on the author, or a record at another path naming the reviewer as author | the finding keeps binding |
| S2-OWNER-ROLES | adjudicator, or technical reviewer, `AMaybaum`; migration `approval.author` not an owner identity; adjudication `authorization.author` not an owner identity | `ADJ-INDEP`; FAIL `record-invalid`; `ADJ-AUTH-OWNER` |
| S2-FIELD-ONLY | identities offered by argument or derivable from commit authors, with record fields that fail | ignored; the record-field outcome stands |

**Changed expectations of existing controls.** NR5-SAME-NORMALIZED-REVIEWER (`Z` reviewer
`' SESSION.FIXTURE-REVIEWER-V '`): under S-2 a padded string is not an identity string, so the witness
stands instead of clearing; the control is restated with `Session_Fixture-Reviewer-V` to keep its
positive meaning, and the padded form becomes a negative case. NR5-REVIEWER-AUTHOR-ALIAS and
NR3-EXCLUDED-AUTHOR-ALIAS keep their outcome (blocked) and are respelled without whitespace so that
they still test aliasing. Each change is toward failing closed.

## 8. Effect on the completed implementation in #1577

| Work | Under S-2 |
|---|---|
| `engine/sessions.py` (`c9458354`, `dd6d563a`) | the registry, its admission and review, party closure, append-only, scope, designations and `platform_ref` are removed. Reused: the `revision` check of `review_binding_problems` and the three outcomes of `detection_outcome`, with same identity in place of the registry; `independence_problems` reduces to S2.4 |
| `record_authority.py` | the registry file name, schema and designation threads removed; `OWNER_IDENTITIES` kept |
| R6.RECON.33 `sessions` kind row and R6.RECON.31 item ids (`config.load`, `records.item_ids`) | removed |
| `adapters/sessions_controls.py` | the registry controls removed; the revision, same-identity and invalidating controls kept and renamed to §7 |
| M1 `015ba150` (`identity_fixture.py`, synthetic layering) | the fixture ids (`session.fixture-*`) are valid identity strings and are kept; `registry`, `registry_review`, `designation`, `entry` and `platform_ref` removed; `bind` keeps `revision` and adds `independence`; the layered build stays (it serves `revision`), without the registry file and its review; `OWNER` becomes `OWNER_IDENTITIES[0]` |
| M2 `a5d46cad`, M3 `e8694385` | kept as they are: they put identity strings in author and reviewer positions; only the three padded variants of §7 change |
| `eeeaee74` | the custody ordering is kept; the S1.5 sort goes with `sessions.py`'s registry code |
| `findings.same_identity`, `records._person` | replaced by S2.2 and S2.1 |

No implementation is made by this paper; it stays paused until adoption.

## 9. Open questions for the owner

| Id | Question | Recommended default | Alternative |
|---|---|---|---|
| OQ-S2-1 | Comparison of identity strings | ASCII grammar and key equality (S2.1, S2.2) | byte equality under a lowercase-only grammar (separator respelling passes); or r13's trim and case fold (look-alike and separator respelling pass) |
| OQ-S2-2 | Does a declared dependency on a party the role must be independent of disqualify? | yes in lint; a form failure that still blocks in detection | record only, for review (weaker; the declaration would bind nothing) |
| OQ-S2-3 | Who authorizes an adjudicator (R6.ADJ.3)? | the owner, as an explicitly reserved decision kept from the adopted #1605 rows, since route 2 overrides an independent adverse reviewer | delegated authority of the responsible agent; `ADJ-AUTH-OWNER` then compares with that agent, and OD-4 bars the authorizer from both judging roles |
| OQ-S2-4 | `migration.approval.author` | the same identity as a member of `OWNER_IDENTITIES` | form only, as r13 had before S-1 |
| OQ-S2-5 | Delegated authority in AGENTS.md | S-2 governs the A1 designs only; any AGENTS.md change is a separate owner-approved edit | none |
| OQ-S2-6 | S-1's admission of owner designation and withdrawal form comments in #1577 and #1169 | ends with S-2's adoption; other governed-thread status of those threads is untouched | kept, unused |

## 10. References (AGENTS.md §A.42 item 8)

| Reference | Used for | Classification |
|---|---|---|
| #1169 comment 7213109404 | authority, quoted above | provenance |
| #1169 comment 7209167255 | S-1's adoption and admitted threads | provenance |
| #1169 comment 7208869709 | adoption of r9 Amendment 1, S11-2a and the #1605 §6 rows | provenance |
| `AMENDMENT-S-1.md` at `3bc3693c66c65d768bc072b65d07f045fe8a23f5` | the clauses superseded | support off `main`; it lands with #1577 |
| `AMENDMENT.md` (staging r2) and `AMENDMENT-S11-2a.md` on `tools/a1-ledger-coverage-r6` at `eeeaee74ea5f64f8f51f3cbebe26b35a22f44968` | the clauses restated; P5 | support off `main`; they land with #1577 |
| r13 `DESIGN-r6.md` (R6.REC.2, .3, .6, .12, .13, R6.RECON.26, .29, .31, .33, tables `review.record`, `migration.approval`) at `4e2f034a7ea5a403e31571a89cf43011f02ea8ce` | the clauses restated | support on `main` |
| r9 `DESIGN.md` (NR-3, NR-5) and `AMENDMENT-1.md` at `4e2f034a7ea5a403e31571a89cf43011f02ea8ce` | the clauses restated; P3, P4, P6 | support on `main` |
| custody `DESIGN.md` (R6.CUST.8) at `4e2f034a7ea5a403e31571a89cf43011f02ea8ce` | the clause restated | support on `main` |
| #1605 adjudication design r4 at `6d79e98363f7542414a00598ddd0197737f09c84` (R6.ADJ.3, R6.ADJ.4, §6, OD-4) | the clauses restated; route 2 in S2.5 | support off `main` (branch `design/a1-adjudication-20261126`); its §6 rows are adopted |
| `engine/sessions.py`, `identity_fixture.py`, `findings.py`, `records.py`, `obl29_controls.py` at `eeeaee74ea5f64f8f51f3cbebe26b35a22f44968` | §7 changed expectations, §8 | provenance (PR #1577) |
