# Notes for GATE-A-AMEND-r1.md

Paper-only: reading, grep and hand reasoning. No computation was run, no Lean was built, and
nothing in the repository or on GitHub was edited or posted.

## What was read

**On `main` at `c3b5f37a354bb26437e2e0165c576a347a63c153`.**

- `verification/programmes/oi-qm/reconstruction/oi-qm-ext-1/endpoints.md`, all 179 lines (blob
  `d9d92e038a8022e854586101067ce4de9789fdf6`). The same blob was confirmed at
  `fdc3dd7f7356dc8f83693f1a2bd8b3a12d24b051` and at `9d24914c5006d775315189dadf56769e1e9cc847`; both
  commits and the merge `dc0b333a1aaee5780d4f3dc514d92337c2c53307` are ancestors of `c3b5f37a`.
- Same folder: `README.md` lines 1–30; `whole-model-bridge.md` lines 1–10, 40–48, 178, 230–262.
  The other twelve files of the folder were not read.
- `verification/programmes/oi-qm/PROGRAMME.md` lines 3, 19–42, 513–545.
- `papers/Main.md` lines 556–600 (in particular 558, 562, 580, 582, 586–588, 596, 598, 600), with
  grep hits at 358 and 427.
- `papers/GR.md` line 162 in full; grep hits at 98, 160, 352, 633, 689.
- Lean statements read, not built: `OIBridge/GeneralCarrier.lean` 13, 36, 93, 100–102, 155–175;
  `OIBridge/PhysicalCharacterization.lean` 301 (location only); `OIBridge/CarrierGeneralOIPlus.lean`
  191, 198, 213 (locations only).

**Off `main`.** Branch `records/target-theorem-914-20261114` at
`755f9bffb904635f2c512a42a4dfa88f8591a6b1`: `README.md` in full; `TARGET-THEOREM-r3.md` by grep for
its EP citations, T3/T5 rows and selection rows (lines 5, 34, 38, 46–52, 121–132, 152–155, 165–175,
191–227). Not edited.

**GitHub, public API, read 2026-11-14.**

- #914 comments 6875046763 and 6875548603; #1169 comment 6875724719 (all in full).
- #1169 body in full (as of `updated_at` 2026-11-14T10:12:36Z), and all of its comments listed; in
  full: 6686258585, 6691915819, 6703342848, 6875057963, 6875553907; other comments by grep for
  "Gate A", "endpoints.md", "both directions", "J_exact" and "every operation".
- #873 body (title "Mannheim gravity comparison and the OI G3 coupling gap").

## Decisions made in drafting

- The superseded obligation is identified as EP:56–59 and the forward half of EP:157 and EP:170.
  No other line of EP quantifies over every admitted model with a law-equality conclusion. EP:104
  and EP:112 ("Both directions", "In both directions") are kept: they constrain each direction
  that is required, and the amendment applies them to I, S⇒ and S⇐.
- The reverse sector direction is stated in the coverage form S⇐, required under both readings of
  #914 c.6875548603, with the model-level necessity form S⇐′ left undetermined pending owner
  decision (R1). This is a drafting choice; the review should check it.
- I-2 reads "one common … architecture" as one architecture for every carrier A (R2). EP:54 is
  per carrier.
- C-1 to C-5 are drawn from EP:43, EP:102, EP:104, EP:164, §A.29 and #914 c.6875548603; C-3 is
  §A.29's hard-to-vary rule applied to C. They are planning constraints on a future C, not adopted
  premises.

## What could not be checked

- The owner's reply "I approve" (#1169 c.6875724719) and the statements quoted in #914
  c.6875548603 and c.6875046763 were given in coordinating conversations not visible here; they
  are known only as quoted in comments posted from the owner's account.
- Whether a more recent revision of the #1169 body or comments exists after the read time.
- The independent ACCEPT of Gate A (#1173 comments 6686122542 and 6686000116) was not read; the
  acceptance is known from #1169 c.6686258585 and the README link.
- What distinguishes members of `Q_exact(A)` (R2): EP does not state it, and no other record was
  searched for a definition.
- The remaining twelve files of `oi-qm-ext-1/` were not read; one of them could restate the
  class-wide forward obligation and so belong in §4.2 of the amendment.
- `papers/GR.md` §8.7 (line 689 onward) and §6.2 were not read beyond the grep hits; the gravity
  obligations cite only line 162 and the two grep hits quoted.
- Lean theorems were not rebuilt; their statements were read at the cited lines only, and
  `physical_of_exactAll` and the OI⁺ directions by location and name.
- No corpus-wide search was made for other records relying on the class-wide reading (for example
  in `verification/programmes/oi-qm/` outside `oi-qm-ext-1/`, or in other Issues).
