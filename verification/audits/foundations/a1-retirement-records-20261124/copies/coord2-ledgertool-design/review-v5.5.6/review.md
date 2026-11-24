# Independent review of DESIGN-v5.5.6 (complete amendment v5.5.3 -> v5.5.6)

Reviewer: independent; wrote neither v5.5.4-v5.5.6 nor any earlier review of them. Read-only
paper review; no code run, no git or GitHub activity. Scope: the complete amendment against the
owner's decisions DI-1 (option B) and DI-2 (option A, narrow) and acceptance criteria 1-8, under
the owner's stopping rule (a finding blocks only with a demonstrated or concrete counterexample).

## Verdict: REVISE

The design text enforces DI-1 and DI-2 on every authorization path I could enumerate; no authority
bypass by a former, future or away-and-back owner was found, and F1-F3 are closed. Two BLOCKING
findings remain, both under criterion 8 (controls) and both fixable by control-table text only
(sec. 5): two controls state an outcome the design text forbids in a full chain, and two amended
rules (the `A`-change approvals and the C5 "has designated" test) have no rejection control.

## 0. Inputs verified

| File | sha256 | |
|---|---|---|
| DESIGN-v5.5.3.md | 99e9ce3af5476e2ea4be1cab911e1aa2cf1c2d3b3a9bf7cf06fcb2f8cbfe3379 | OK |
| DESIGN-v5.5.6.md | e19e9406044b4be321074ff935f5978b5ebeb258a637a76545023d3cbeafca77 | OK |
| CHANGES-v5.5.6.md | 8c09fcd7857dc159a8fe7eb760fd49193399d9228ac4fc76e53c8bda08392229 | OK |
| CHANGES-v5.5.6.diff | aaa9ffa17919895991a8922b5ca415ec1c6e896dbe8a9b71be9f7aaa042127a4 | OK |
| CHANGES-v5.5.6-from-v5.5.5.diff | 5d7ac4f8a6fd82fbe2d2d9fa8561c2d2e664b597aa3803b8bedfd05f80453f19 | OK |
| review-v5.5.4/review.md | 34927de86bdbed0d8e8cc8e4e2438f18bf001082153bfddb283781767c5f0842 | OK |
| review-v5.5.5/review.md | c12db216df19940399f8d3a691a2c80be0cff6816c2dafbfd79539871853b7cc | OK |
| review-stage1-r4/review.md | e21cf9d34210ca4f41d6397a9f4b91d26674c9601f1399bacb8a57f9d2a5eae0 | read (sec. 6-7) |
| DESIGN-v5.5.5.md / CHANGES-v5.5.5.md | f6f966eb...aff9 / bf721f33...dc8b | as cited in CHANGES |

Fresh `diff -u` v5.5.3 -> v5.5.6 and v5.5.5 -> v5.5.6 are byte-identical to the two `.diff` files
apart from the header lines (14 and 8 hunks; 3027 -> 3143 lines). All 28 old/new blocks in
CHANGES-v5.5.6.md occur verbatim as whole contiguous lines in their files (script). TR66, TR67 and
LN11 rows are string-equal to review-v5.5.5 C7/C6(c); C5, C6(a), C6(b) equal after whitespace
collapse. TR54-TR67 and LN1-LN11 (word-bounded grep of every `*.md` under the design directory)
occur only in the v5.5.4-v5.5.6 drafts, their change files, work notes and the two reviews; no id
reused. TR68 and TR69 are unused anywhere.

## 1. Decisions, probes and earlier findings (criterion 1): MET

| Item | Closed by (v5.5.6 text) | Control |
|---|---|---|
| D1 former owner's designation | Designations: author = governing owner, no owner change since creation | TR54 |
| D2 former owner's unledgered withdrawal | Withdrawals: owner comment at creation, stays effective | TR55 |
| D3 pre-ownership designation | owner-comment definition (version in force at creation) | TR56 |
| L5 away-and-back ledger approval | Approvals: no owner change between creation and merge | TR57 |
| L6 pre-ownership ledger approval | Approvals: owner comment | TR58 |
| E6 cross-lineage `supersedes` | lineage bullet (same kind, schema, `record_id`) | LN1, LN8 |
| v5.5.4 B1 authorization records | "Owner authorizations"; point 7 last sentence | TR65 |
| v5.5.4 B2 predecessor vs today's owner | lineage predecessor clause; completed-action sentence | LN9 |
| v5.5.5 F1 point-5 contradiction | C5 parenthetical in point 5 | TR55, TR61 (traced: now consistent) |
| v5.5.5 F2 predecessor widening authorization | C6(a)/(b) "each authorization its lint requires, a widening review's included" | LN11 |
| v5.5.5 F3 missing controls | TR66 (withdrawal not owner comment), TR67 (point 3 former owner) | - |

## 2. Lineage (criterion 2): MET

Lineage = `record_id` (`config_id` for the configuration; `A` by fixed path and first-parent
predecessor, TR63). A predecessor must have the same kind, schema and id at every step, exist at or
before `F`, and itself pass the lint; cycles, forks (in the audit and plan directories at `F` and
in what the run reads) and two heads in one run fail. Each condition is decidable from git objects
and the records alone.

## 3. Authorization paths re-enumerated (criterion 3)

Each attacked with a former owner (posted while owner, evaluated after a change), a future owner
(posted before becoming owner) and away-and-back (4242 -> 5555 -> 4242 between posting and use).
Owner ids 4242/5555/6666; versions V1 (4242), V2 (5555), V3 ...

| # | Path | Former | Future | Away-and-back | Text holds | Rejection control |
|---|---|---|---|---|---|---|
| 1 | `designate` | author != governing: no | not owner comment | change between | yes | TR54, TR56, TR59 |
| 2 | `supersede`, designating half | as 1 | as 1 | as 1 | yes | TR61 |
| 3 | `withdraw` / revoking half | counts (decision) | not processed | counts (decision) | yes | TR66 |
| 4 | ledger / snapshot bound events | revoke only (K1), judged by recorded author/time | same | same | yes | TR31, TR32 (unchanged) |
| 5 | `oi-authority/1 approve`, `A` change (previous id) | governing = replaced version | not owner comment | change between | yes | **none (B-2)** |
| 6 | `oi-authority/1 approve`, ledger change | governing = in force at merge | not owner comment | change between | yes | TR57, TR58 |
| 7 | `oi-freeze-ledger/1 append` (N3) | as 6 | as 6 | as 6 | yes | TR57, TR58 |
| 8 | first `A`; new id of owner-id change | n/a; authenticated as pinned id | before merge | no owner change between creation and merge | yes | TR62 (timing only; **no change-between case, B-2**) |
| 9 | `oi-owner-authorization/1` for used records (incl. reconciliation records after `F`, PIN_OK, widening reviews) | owner != governing | owner not in force at `time` | change between `time` and admission | yes | TR65 |
| 10 | configuration's own authorization, `retirement.owner` | point 7 + 9 | same | same | yes | TR4, TR65 |
| 11 | predecessor authorizations, widening included (DI-2) | completed: owner at `time` | not owner at `time`: fails | counts (completed) | yes | LN9, LN11 |
| 12 | `A` changing between run and acceptance landing | acceptance predicate: same `A` blob as `main` now | same | same | yes (unchanged sec. 5) | - |
| 13 | review records; merged-by id | no owner authority; provenance | - | - | n/a | - |
| 14 | edit/hide of owner comments (point 3) | former owners' comments included (refuse-only) | current id's pre-ownership comments included | - | fail-closed | TR67 |

Hash binding was attacked directly: a comment pre-signed against a pending `A` blob (for example
5555 approving `from=<sha256 of V2>` while V1 is in force, or 4242 pre-signing `from=<sha256 of
V3>` before 4242 -> 5555 -> 4242 merges) is accepted by v5.5.3's letter and refused by v5.5.6
(not an owner comment; owner change between creation and merge). The text holds on every path;
criterion 3 is met for enforcement. The missing controls on paths 5 and 8 are B-2 (criterion 8).

## 4. Other criteria

- **Criterion 4: MET.** `record_id` is required only of a record that supersedes or is superseded;
  no per-kind schema is changed; LN10 keeps `supersedes: null` records without an id usable.
- **Criterion 5: MET.** Authority and ledger changes are judged at their merge against the version
  then governing; acceptance landings stand; predecessor authorizations, widening reviews included,
  need only owner at their `time`. Authorizations of records the run uses are approvals evaluated
  at admission ("current owner when evaluated"), as v5.5.3 already compared them with today's owner;
  the only newly refused case is away-and-back, which DI-1 requires.
- **Criterion 6: MET.** Traced under the C5 text: designate -> withdraw -> change, then a new `F'`:
  admitted at point 5. designate `F` -> supersede by `F2` -> supersede by `F3` -> change: both
  revoking halves pass the test (each named commit "has designated" by an owner comment at creation,
  the designating half being "the designation of `F2`" in the Designations bullet), designating
  halves not processed; a new designation of `F3` or `F4` is admitted at point 5. Designations by
  two former owners (4242's `F`, 5555's `F2`, then 6666): neither processed; 6666's own designation,
  or 6666's withdrawal of either, admits. In every case only a re-freeze is needed.
- **Criterion 7: MET.** All 14 hunks are DI-1, DI-2, C1-C7, the N3 cross-reference or direct
  consequences (title, status, snapshot field, merge-time trust item, S13). Quotes exact (sec. 0).
- **Consistency with unchanged v5.5.3 text: MET.** TR32 (bound supersession only revokes, earlier
  `F` stays superseded); N3 (append verified like a designation, author by "Owner at creation");
  authority-change procedure ("author numeric id is the previous `A`'s `owner.id`" = governing
  replaced version); admission points 1-7; reconciliation ("a ledger entry alone never designates");
  forms; K1 (recorded supersessions never designate).
- **Criterion 8: NOT MET** (B-1, B-2).

## 5. Findings

### B-1 (BLOCKING, criterion 8): TR54 and TR61 expect "admitted" where the design text, and the owner's accepted re-freeze, require a refusal

Text. "Owner authorizations": an authorization counts for a record the run uses only if "no owner
change merged between its `time` and the admission"; point 7 applies this to the configuration's
own authorization (ERROR `CONFIG_UNREVIEWED`). DI-1 as decided: pending designations are
invalidated by an ownership change and "pending freezes must then be re-frozen".

Counterexample. TR54, second case: 4242 designates `F`; 4242 -> 5555; 5555 designates the same `F`;
expected "`F` admitted as designated". `F` was named by 4242's comment before the change, so `F`'s
tree, and the configuration authorization in its pin table, existed before the change; that
authorization's `time` predates the owner change, so point 7 refuses with ERROR
`CONFIG_UNREVIEWED`. TR61, second case (4242 supersedes `F` by `F2`; change; 5555 designates `F2`;
"admitted"): identical, `F2` being named before the change. In a full chain (TR5's sense of
"admitted", `config.admission: "chain"`) both expectations are unattainable, and sec. 10.4 requires
a predicate to test its whole stated expectation. They are correct only at point 5 or in the
control harness, which TR66 states explicitly and TR54/TR61 do not. (review-v5.5.5 N1 raised this
as non-blocking; criterion 8 now requires outcomes that are precise and consistent with the text.)

Correction: C8 (sec. 6).

### B-2 (BLOCKING, criterion 8): two amended rules have no rejection control

(a) **`A`-change approvals** (hunk 6: "It must also count as an approval under 'Owner at creation'";
the first-`A`/new-id bullet: "with no owner change merged between its creation and that merge").
TR57/TR58/TR64 exercise only freeze-ledger changes; TR62 only the new id's timing against the merge;
TR40-TR44 are v5.5.3 rules. Concrete gap: an implementation that applies "Owner at creation" to
ledger changes but checks `A` changes as v5.5.3 did (author = previous `A`'s `owner.id`, created
before the merge) passes every control TR1-TR67 while accepting: 5555's approval of V2 -> V3
pre-signed (`from=<sha256 of V2>`) while V1 (4242) was in force; 4242's approval of V3 -> V4
pre-signed while owner, used after 4242 -> 5555 -> 4242; and 6666's new-id approval of V2 -> V3
(5555 -> 6666) created before V1 -> V2 merged. Each is a DI-1 violation (future owner;
away-and-back; ownership changed between approval and merge).

(b) **The C5 test** ("a designation that was an owner comment at its creation has designated its
commit"). TR55/TR61 cover only its acceptance side. An implementation that treats any designation
form, by any author, as "has designated" passes every control while admitting state from a comment
that was never an owner comment: 5555 designates `F` while 4242 is owner; 4242 -> 5555; 5555
withdraws `F`. The text refuses (withdrawal naming a commit never designated); no control asserts it.

Correction: C9 (sec. 6).

### NON-BLOCKING

- **N7.** TR60 "5555 designates `F`; `F` admitted" holds only for an `F` frozen after the change;
  recommend saying so (included as optional text in C8).
- **N8.** Criterion 6's double-supersession case rests on reading the designating half of a
  supersession as "a designation" in the C5 parenthetical; the Designations bullet supports it
  ("the designation of `F2`"). A control (designate -> supersede -> supersede -> change -> new
  designation admitted at point 5) would pin it.
- **N9.** The C5 test is not ordered in time: a designation created after the withdrawal that names
  it also satisfies "has designated". It only removes refusals and grants no authority.
- **N10.** After an owner change (including away-and-back), a round already accepted with `F2` can
  be admitted again with a new `F3` without withdrawing `F2`, because `F2`'s designation is no longer
  processed ("A designation is not completed for a later admission"). v5.5.3 behaved the same after
  a real owner change; under one owner it needed an explicit withdrawal. Consistent with DI-1; noted
  for the owner.
- **N11.** If an owner change merges after an acceptance landing's check run and before the landing
  merges, the merged append's approval does not count and the ledger is unverifiable for every later
  admission. Pre-existing (v5.5.3 is stricter); it rests on sec. 5's "re-checked ... before the
  landing merges" being enforced at merge time.
- **N12.** For a configuration predecessor at the fixed path `retirement-config.json`, the lint
  bullet "exists at `F` at its path" must be read with the lineage clause's "read from the object
  store at or before `F`"; worth stating, fail-closed either way.
- review-v5.5.5 N2-N6 still apply as stated there (not acted on, non-blocking).

## 6. Corrections (exact text)

**C8 (B-1).** In TR54, replace
`the second: `F` admitted as designated`
by
`the second: `F` is the one designated commit at point 5 (control harness); in a full chain, ERROR `CONFIG_UNREVIEWED` at point 7, since `F`'s configuration authorization predates the owner change and `F` must be re-frozen`.

In TR61, replace
`admission of `F2`: ERROR (missing designation) in the first, admitted in the second`
by
`admission of `F2`: ERROR (missing designation) in the first; in the second, `F2` is the one designated commit at point 5 (control harness), and in a full chain ERROR `CONFIG_UNREVIEWED` at point 7 as in TR54`.

Optional (N7): in TR60, `5555 designates `F`` -> `5555 designates an `F` frozen after the change`.

**C9 (B-2).** Controls (new ids), after TR67:

```text
| TR68 | V1 (owner 4242) -> V2 (owner 5555) is an owner change. Each case separately: an `A` change V2 -> V3 keeping 5555, whose previous-id approval (`from=<sha256 of V2>`) 5555 created while V1 was in force; an `A` change V3 -> V4 after V2 -> V3 (5555 -> 4242), whose previous-id approval 4242 created while V1 was in force; an owner-id change V2 -> V3 (5555 -> 6666), whose new-id approval 6666 created before V1 -> V2 merged | ERROR in each case: the change does not take effect, and every later admission refuses | DI-1; authority changes |
| TR69 | 5555 designates `F` while 4242 is the owner; 4242 -> 5555; 5555 withdraws `F` | ERROR (a withdrawal naming a commit never designated: the designation was not an owner comment at its creation) | DI-1, point 5 |
```

Consequential: status bullet "TR54-TR62 and TR64-TR67" -> "TR54-TR62 and TR64-TR69"; S13
"TR1-TR67" -> "TR1-TR69"; CHANGES updated. No design rule text changes.

## 7. Criteria

| # | Criterion | Met | Evidence |
|---|---|---|---|
| 1 | D1-D3, L5/L6, E6; B1, B2; F1-F3 closed | yes | sec. 1 |
| 2 | lineage unambiguous, independently verifiable | yes | sec. 2; LN1-LN8, TR63 |
| 3 | all paths enforce the same protections | yes (text) | sec. 3, 14 paths, no bypass; control gaps under 8 |
| 4 | `record_id` limited; null/no-id records usable | yes | lineage bullet; LN10 |
| 5 | completed actions judged at completion | yes | Completed actions bullet; C6; LN9, LN11, TR60 |
| 6 | no permanent unadmittability beyond re-freeze | yes | sec. 4 traces under C5 |
| 7 | diff scope, exact quotes, no id reuse | yes | sec. 0, 4 |
| 8 | controls precise, consistent, both sides | **no** | B-1 (TR54, TR61), B-2 (paths 5/8, C5 test) |
| - | consistency with unchanged v5.5.3 text | yes | sec. 4 |
