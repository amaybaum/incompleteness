# Focused confirmation: TUNE-1 sourcing r2

**Object.** Branch `research/tune1-sourcing-1236-20261113`, fetched by name.
- Remote head: `890fe3dd18287f72f48e7884ef5cc272fb60e661`.
- The commit has a single parent, `c3b5f37a`. Its diff against `main` adds exactly seven files
  under `verification/programmes/oi-qm/reconstruction/drafts/tune-1-sourcing-20261113/`.

**Method.** Read-only. Each file was extracted with `git show`. The r1 → r2 changes were read as a
word diff. No computation on any OI rule.

**Verdict: CONFIRMED.**
- Every required change (R1–R6) and every minor item (m1–m10) is applied as I specified.
- The extra edits are accurate and add no claim.
- There is one cosmetic nit, listed below. It does not block.

***

## (1) R1–R6 and m1–m10

Each item was checked against the old → new text in my review, §8.

| Item | Where in r2 | Applied |
|---|---|---|
| R1 | §0 (c.6854774010 quoted; the quotation matches the comment I fetched); N1 verdict; §5 NL-C bullet; §7 row; NOTES-r2 item 1 | yes, verbatim |
| R2 | header; (b) row; status paragraph; N3.2; N3 verdict; §5; F-S4 | yes, verbatim |
| R3 | N1.3 (proviso `m + 1 ≤ L`, `(1−4ε)/(8ε)` form, `m ≥ L` open, "space to time" removed); F-S1; AW-SRC-1 | yes, verbatim |
| R4 | F-S2 (necessity only; "linked by necessity"; converse not shown); AW-SRC-2 scoped to the schema; productivity verdict scoped | yes, verbatim |
| R5 | (c) row: form of the action derived; fails OA-1's N2 under every measure (OA1:523, :530); Q3′ adequacy is L5.4 | yes |
| R6 | N3.5: OBS's H-μ glossed as μ-G (OBS:69–73), not P:145 | yes |
| m1 | (a): (ix), (xi), reference instance | yes |
| m2 | N3.1 | yes |
| m3 | (e) | yes |
| m4 | (b) row | yes |
| m5 | §1 | yes |
| m6 | §7: 3A:501 and 3A:794–805 rows | yes |
| m7 | N3.5: Main:742, OA1:561, mixing hypothesis and (EM) | yes |
| m8 | N0.4a | yes, not selected |
| m9 | NOTES-r2 item 6 | yes |
| m10 | (f) | yes |

## (2) The writer's three extra edits

- **m4 propagated to N3.1 and F-S2.** Both say "before use" and cite P:206–208. This matches the
  (b) row and the source: by layout, no record before round `j` depends on `c_j`. It is a
  qualifier, not a claim.
- **§6 reading inventory.** Adds c.6854774010, which is accurate because R1 required reading it.
  It also lists c.6848268369 explicitly, which was already read in r1.
- **NOTES-r2 items 11 and 12.** Both record open points that R3 and R2 create:
  - item 11: gates of `m ≥ L` rounds; my recovery sketch is "not attempted, and not asserted";
  - item 12: the conditional route under μ-O and μ-R, with D-OB7 cited.

  Both are accurate, and neither adds a claim.

## (3) Stop at (b) and scoping by measure

- Every place that states the ingredient now reads "not shown to supply" or "not shown to follow".
  This holds at:
  - the header (line 14);
  - the (b) row;
  - the status paragraph;
  - the N3 verdict;
  - §5.
- Each of those places carries, or points to, the split by measure:
  - excluded under μ-G;
  - not supplied unconditionally under μ-O, with the conditional route open;
  - undecided under μ-R.
- I grepped for "do not supply", "not supplied", "impossib", "no-go", "every embedded" and
  "cannot". The surviving hits are all scoped:
  - μ-G (N3.1);
  - R-lin (D5 at line 216 and F-S1);
  - the quotation of OA-1's reason for MP-0a (line 259);
  - "every embedded-tunability candidate within TUNE-1's schema (finite alphabet; continuous cells
    out of scope, not refuted)" (line 356).
- No statement is OI-wide.
- The stop is (b) everywhere. Parts (c), (e) and (f) are recorded as resting on the same ingredient.
  Part (c)'s adequacy remains L5.4, which is not a physical ingredient.

## (4) REVIEW byte identity and OBJECTS hashes

- `REVIEW-r1.md` is byte-identical to my `REVIEW.md` (`cmp`). Its sha256 is
  `d9c9f7d2…702bd2`.
- `TUNE-1-SOURCING-r1.md` and `NOTES-r1.md` are byte-identical to the files I reviewed.
- For all six files OBJECTS.md lists, the recomputed sha256 equals both its "reviewed" and its
  "committed" column. The listed blob prefixes match `git ls-tree` at the head:
  - `e21299f9`, `5ac597e9`, `72347688`, `20ee9b04`, `a1af11fe`, `3f25dd28`;
  - "Substituted lines: none" is correct.
- OBJECTS.md itself (blob `ea68cf71`) is not self-listed, as is unavoidable.

## (5) New overclaims

None found. Every added sentence narrows a claim, cites a source on `main` that I verified in r1's
review, or records an open point. The register is clean: all-caps tokens are identifiers or verdict
words, and there is no self-narration in the record body.

## Non-blocking nit (cosmetic; fix at the next touch)

- **Stale file names.** r2 lines 4 and 6 name `REVIEW.md` and `TUNE-1-SOURCING.md`, and
  RESPONSE-r1.md lines 3–4 name `REVIEW.md`, `TUNE-1-SOURCING.md` and `NOTES.md`. The committed
  names are `REVIEW-r1.md`, `TUNE-1-SOURCING-r1.md` and `NOTES-r1.md`.
- **"Nothing else differs".** r2 line 5 says "Nothing else differs from r1", but the three extra
  edits in (2) also differ. RESPONSE-r1.md discloses them, but the r2 sentence is literally
  inaccurate.

Suggested wording for the revision line: "…of the independent review of r1 (`REVIEW-r1.md`…)…
Beyond these, r2 differs from r1 (`TUNE-1-SOURCING-r1.md`) only in the edits listed under 'Other
edits' in `RESPONSE-r1.md`."
