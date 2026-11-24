# A1 retirement working records: preservation copies (2026-11-24)

**These files are preservation copies, not byte-identical original evidence.** They are cleaned copies
of the coordinating session's local working records for the A1 retirement: the ledger coverage tool's
designs, implementation records and independent reviews, the A1 plan amendment proposal and its
reviews, the Q10 disposition, the SM.md:1394 reading, and the texts prepared for GitHub records.

- Status: preserved by owner decision (amaybaum, 2026-11-24, coordinating session): "preserve cleaned
  copies on a separate records branch, with a complete hash-mapping manifest. Do not introduce an
  exception to the repository's rules. ... A cleaned copy must never be presented as byte-identical
  original evidence."
- This branch is for preservation only. It is not a pull request, it establishes no claim, it accepts
  no implementation, and it is not to be merged without a separate owner decision.
- The tool implementation itself is preserved on branch `tools/ledger-coverage-20261123` at
  `3184c7f9075948d8474197eee03ba5b94ba85db5`, pending final independent acceptance.

## What the copies are

`copies/<path>` holds the copy of the local record `<path>`. `MANIFEST.json` lists, for every file,
its relative path, the SHA-256 and size of the local original, the SHA-256 and size of the copy,
whether the two are byte-identical, and the transformations applied with their counts.

The transformations are mechanical text substitutions only (`MANIFEST.json`, key `transformations`):
local absolute paths are replaced by placeholders (`<records>`, `<repo>`, `<write-state>`, `<tmp>`),
the local name of the session working directory is replaced by `workspace`, and the commit-identity
e-mail address is replaced by a placeholder. No scientific content, review verdict, test result or
owner decision was changed. Scripts among the copies may not run as copied, because their paths were
replaced.

**Hash references.** Every SHA-256 quoted inside a record refers to the local original of the file it
names, never to its copy here. The `original_sha256` column maps each original to its copy; a record
that is byte-identical to its original (`byte_identical: true`) has the same hash in both columns.

## Selection

The records copied are the text records (`.md`, `.json`, `.sha256`, `.diff`, `.patch`, `.py`, `.txt`,
`.yml`, `.sh`, each at most 512 KiB) at the top two levels of the record directories
`coord2-ledgertool-design`, `coord2-a1-amend`, `coord2-q10`, `coord2-sm1394` and `coord2-records`,
excluding working directories (`work*`); the staged configuration `staging-3184c7f9` and the edit diffs
`diffs-r5` in full; and the session handoff. Not copied: raw run outputs, logs, mutation outputs,
probe trees and copies of repository trees, which are regenerable or not needed by a surviving
record; the final review of `3184c7f9`, still in progress; and the paused OI-COMP-BENCH records.
