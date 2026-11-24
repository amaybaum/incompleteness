# Correction note to EXACT-DELTA.md (S1), section "P6 / Q8 / Q10"

EXACT-DELTA.md is kept unchanged. This note records where its Q10 table is superseded by the accepted Q10
disposition (DISPOSITION.md, sha256 7ae4448024bd04256cf585b722f4b97a2a9ba3dc9b449ad40fc4865bd9345f89; accepted as
final by owner amaybaum, 2026-11-24, in session). The classifications below follow that disposition, which rests on
static code reading, not on a tool run.

| Record | EXACT-DELTA says | Accepted disposition |
|---|---|---|
| rules/w1-w2-allow-v1.json | load-bearing: fingerprints reproduced at recorded_at | unchanged in substance: per-rule recorded_at (T1′) is read; evidence gap (ESC-1). The file-level recorded_at is not read (provenance) |
| rules/dr-deny-v1.json | load-bearing (same mechanism) | incorrect: the T1′ citation is not read; provenance only (ESC-5, administrative) |
| rules/resid-v1.json | load-bearing (same mechanism) | incorrect: the T1′ citation is not read; provenance only (ESC-5, administrative) |
| rules/register-infinity-params-v1.json | linted against P's edits_check.py | imprecise: the record's own P fields are not read; the lint uses the checker that the A1 configuration pins to P's edits_check.py; evidence gap (ESC-2) |
| records/repo-scope-v1.json | scope names extracted from P's edits_check.py | incorrect: `source` is never read or extracted; the engine applies only the lists; the record's claim of agreement with P's checker needs P; evidence gap in support (ESC-3) |
| records/gr58-hit-classification-v1.json | load-bearing: classification of a line at T1′ | unchanged in substance: `tree` is not read, but the classified line exists only at T1′; evidence gap (ESC-4) |

Also superseded:
- The README's single "provenance only" label for the group (S1 review nit N3) is incorrect for w1-w2,
  register-infinity, repo-scope and gr58. The README is to be corrected during the v5.5.10 implementation, once
  authorized, classifying every off-main reference individually per the disposition, under explicit independent
  review (owner decision, 2026-11-24).
- 86d79863821f3f8cdad86771008b2df89fd1961a is a computed blob id (AGENTS.md at 8e9b8334 with splice D296 of P's
  ledger applied), not an existing Git object.

ESC-6 stays open until the README correction and this note are both completed and reviewed.
