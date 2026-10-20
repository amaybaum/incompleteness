# Corrections to PILOT.md after independent review

**Review:** an independent review of the head-`0004afc9` pilot returned changes needed, all of them text. It
reproduced every number, and the 10 required / 0 redundant classification stands.

**Before and after:**
- `PILOT.md` before: sha256 `eabdacb6581472f2ede529245c2022efd2efcd2f390ea30efa5dfbb15e950f6f`. This file is
  kept byte-identical as `PILOT.original.md`.
- `PILOT.md` after: sha256 `b03d2204158f8a3a7817651f07a1322638b31c7e787b7d8db7fdd4d5b402bb61`.

**Unchanged:** `PREREG.md` (`37a47210…825cca`), `closure.json` (`e6b0b51d…f7ed1`), `controls-out/` and every
script. No checker was re-run.

**One new measurement:** the 25-file count under B1, read with `git ls-tree` (output
`out/ec36_blobfiles.txt`, sha256 `0b42eb24…3e9092`).

| finding | change in PILOT.md |
| --- | --- |
| **B1** (blocking): §6 item 4 was false for byte-copy blobs | §6 items 4–5 rewritten. H3 accepts a name that *some tranche base* reaches (`check_objects.py:1529`, `:1614–1619`, H3 at `:1631–1633`, H4's held set at `:1621`). Tranche 5's base `ec36234c` contains the archive's own plain-file copies of byte-copy blobs, so H3 and K1 diverge. In-pilot example: the head's required blob `016e5428`. The claim that H3 rejects an omission is narrowed to objects that are neither plain-file copies nor reachable from a tranche base through the archive's own paths. The count of 25 affected entries (tranche 2, `byte-copy`, cited, all of the manifest's raw-form blobs) was re-derived from the manifest and `git ls-tree -r ec36234c -- …/objects/blob/`, and it matches the reviewer's. Added: the open consequence by code reading, an assumption-watch item, and N4 (coordinated omission of a byte-copy blob) recorded as **not run** and open |
| **N2**: N3 was not preregistered | The table labels N3 "added; not preregistered". "Every variant meets the preregistered pass criterion" is replaced by: LIVE, N1 and N2 meet their preregistered criteria; N3 has none and is reported as observed |
| **N3**: release-gate scope; tree-mode finding | §6 item 6: by code reading, `check_retention.py --gate` → `objects_gate` → `check_objects.py --reconstitute` (`check_retention.py:1137–1142`) would fail N3 through the same H3 line. The gate was not run to completion. §6 item 2: tree mode passing a coordinated tranche-2 omission is the documented `EXACT_FROM` design (docstring; line 744), not a new finding |
| **N4**: G-claim attribution of the history entries | §5: the G-claim column for `17de29c2`, `e8e9a726` and `a2a2a776` now reads "not in G-claim(h); required by `17de29c2`'s own claims" (`:489`, `:501`, and H4 under G-full). Counts are now G-claim(h) 7, G-full(h) 10. §4 is reconciled to 7 under G-claim(h) and 10 under G-full(h). Added a note that per-head counts must not be summed, because entries are shared across heads |
| **N6**: local gate run | §6 item 6: the single local gate run, stopped at 600 s, is not to be repeated locally (`retention-tests`, with owner approval) |
| **N7**: text precision | "Fixed inputs" notes that PREREG's "legacy/receipt class" means the classes `native-record` and `legacy-record`; the manifest has no receipt class, and the selection is unaffected. PREREG.md itself is unchanged. "main reaches it" is replaced by "some tranche base reaches it" (§6.4), and H7's wording by "the entry's own tranche base reaches" (§4) |
| **N8**: representativeness | §4 adds that this head is a weak test of over-retention, and why |
| status | The header and §7 record the review and that the corrected text has not been re-reviewed. §7's first bullet is restated as 7 head entries plus 3 history entries |

Findings **N1** (preregistration precedence rests on local mtimes and is self-attested) and **N5** (the G-full
argument for the history entries is correct) required no text change.

## Third pass (re-review R1)

- R1: "byte-copy blobs" narrowed to "the 25 raw-form (plain-file) byte-copy blobs" at lines 236, 252, 267, 269, 292. The other 227 byte-copy blobs are stored compressed, have different file ids, and H3 rejects their omission as it did for `dda14af0`.
- §6.4: "That is what N2 and N3 show" narrowed to `dda14af0`; the general statement rests on code reading.
- Status line updated.
- PILOT.md sha256 before: b03d2204158f8a3a7817651f07a1322638b31c7e787b7d8db7fdd4d5b402bb61; after: 7c3eed7337daa560b7f7399fb91e6b9126473caddfefb9052bf70d8150b8b4d5
- Line 255: "the 25 byte-copy blobs" → "the 25 raw-form byte-copy blobs" (third-pass cosmetic note). PILOT.md sha256 now: 894083293dd06bc477d0a86549cb78babebca04f455248f715806c1733985ea0
- Publication copy: PREREG.sha256 path field changed from the local scratch path to `PREREG.md`; the digest is unchanged.
