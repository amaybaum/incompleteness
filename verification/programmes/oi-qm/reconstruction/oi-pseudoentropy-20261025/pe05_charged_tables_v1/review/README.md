# Review records: working name and paths

The review files in this directory were written while this stage carried its working name, **PE-02**, in the
directory `pe02_charged_tables_v1/`:
- `REVIEW.md`, with `toy_checks.*` and `tightness.*`;
- `RECHECK-r2.md`, with `r2_checks.*`;
- `RECHECK-r3.md`.

The owner (amaybaum, 2026-10-26) renamed the stage **PE-05**, after PE-04 was found taken by the thread's
quantum-reconstruction stage. The files are kept byte for byte as written. Read "PE-02" in them as this stage, not as
the thread README's PE-02 (computational versus physical observers), and map their paths as follows.

| Cited in the reviews | Now |
|---|---|
| `verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe02_charged_tables_v1/` | `verification/programmes/oi-qm/reconstruction/oi-pseudoentropy-20261025/pe05_charged_tables_v1/` |
| `pe02_charged_tables_v1/PLAN.md`, `NOTES.md`, `CHANGES-r2.md`, `CHANGES-r3.md` | `pe05_charged_tables_v1/` (same file names) |
| `pe02_charged_tables_v1/design/*` | `pe05_charged_tables_v1/design/*` |
| `pe02_charged_tables_v1/review/*` | `pe05_charged_tables_v1/review/*` |

The reviews also cite `PE-04` as the recommended new name. The owner's ruling replaced that with PE-05.

The schema identifiers `pe02-shard/1`, `pe02-measurements/1`, `pe02-verdict/1` and `pe02-rp01/1`, and the parameters
block tag `pe02-parameters`, are fixed identifiers. They are unchanged by the rename (PLAN §5).

## Confirmations before the specification freeze

The independent confirmations that preceded the freeze are kept here as written. The first one has one redaction: a
local scratch path is replaced by a description. All four were written after the rename, so they use the PE-05 paths.

| File | Commit confirmed | Verdict |
|---|---|---|
| `CONFIRM-1-7b469183.md` | `7b469183` (rename, P1–P3) | ACCEPT WITH NITS (C1–C6) |
| `CONFIRM-2-7736a1ce.md` | `7736a1ce` (C1–C5) | findings E1–E3 |
| `CONFIRM-3-d6fc056a.md` | `d6fc056a` (E1–E3) | findings IMP-1 and a typo |
| `CONFIRM-4-7d90b323.md` | `7d90b323` (IMP-1) | CONFIRM FOR FREEZE |

