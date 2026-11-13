# Q-868-H unit 1: preserved objects

**WIP / UNVERIFIED research record, not for merge.** This directory preserves, byte for byte, the
Q-868-H unit 1 files (Issue #868; parent programme #1169) from the 2026-11-09 session handoff
snapshot. Nothing here is adopted, promoted or proposed for the manuscripts, and preservation
changes no status (§A.42 item 6; §A.46 item 3). Every review named below is a model-written
review, not human verification (§A.46 item 7).

## Authorization of the unit

Owner record: #868 comment 6742050189, posted by `amaybaum` at 2026-11-09T14:07:16Z, recording the
owner's answer **"Approve both (Recommended)"** to a question whose first item reads, verbatim:

> (1) Q-868-H, paper analysis plus independent review only. Can one native OI construction prepare
> two-wing joint states whose heralded branches stay inside both the native test set and OI's
> admissible state set? It covers failures, herald probabilities, conditional states, repetition
> and composition, with no quantum states supplied as inputs. Three outcomes are reported
> separately: validity, closure, and quantum compatibility. No outcome implies another without
> proof. No computation, construction changes, new assumptions or execution.

The same record states: "Next step: Q-868-H starts as a paper-only unit, followed by a fresh
independent review." Preservation of these files is authorized separately, by #1169 comment
6852816462, item 1.

## Source

Every file was copied from branch `ccr-9c2ecca4-vkb666`, commit
`820519cf011c09b37690213a758106ed3aa15cc2` ("Handoff snapshot (WIP, not for merge): #1169 unit
working files at session end, 2026-11-09"), path prefix `handoff-20261109/868-q868h/`, with the
relative path below kept. Each committed blob equals the source blob; no byte was changed. That
commit is not reachable from `main`.

## Status

- **r2** (`Q868H-UNIT1.md`) is **not yet independently reviewed.** Its header reads "revision r2.
  Pending fresh independent review." The snapshot's handoff index records the fresh r2 review as
  interrupted at handoff, with next step "Re-run fresh independent review of r2"; no output of that
  review is in the snapshot or here.
- **r1** (`r1/Q868H-UNIT1.md`) was independently reviewed (model review) with verdict
  **REVISE (narrow)**: blockers B1–B2, nits N1–N8; the review keeps the headline outcomes "(V) PASS,
  (C) PASS conditional, QC FAIL". r2 is the revision answering that review.
- **`DISPOSITIONS-r2.md`** is the r1 → r2 change note; it is part of the r2 submission and is
  unreviewed.

| File | Blob | SHA-256 | Status as recorded |
|---|---|---|---|
| `Q868H-UNIT1.md` | `4d96a563d5a6f9c097ebb812b9f465c2f7d3a711` | `1e128f286b14be3294cb8411e21f0b4b4516cbc9985fc2589fb6362a752179e6` | r2; not yet independently reviewed |
| `DISPOSITIONS-r2.md` | `a87d9351eb59bfd30cf8a643d3a285b16885d7f4` | `2916fa33c008205af1458695c6287b38ba87c805506649e8da95b0cce14bcaf4` | r1 → r2 change note; unreviewed |
| `r1/Q868H-UNIT1.md` | `6d2eb2454a0369302e6a155d67dcd34736f1ba28` | `428cc283087657377fe0329a1e07b6f1b01b98e7a733df82e56e163bd3651d49` | r1; review REVISE (narrow); superseded by r2 |
| `review/REVIEW-Q868H-UNIT1.md` | `a07c0f1e6575b72922cb677232b56a0920abfa16` | `bd82f3fc469348945a838183f052c28c527ee6f43e7fc91c4157abd1a8cfb520` | model-written independent review of r1; verdict REVISE (narrow) |
| `review/rv_qc1.py` | `95ea5f7d3a488c5ad0f20be4e4f39ebd6d958989` | `063bba2fcc1e587dd11979a453a33c8b6f0c7e8a30cf7a4d59725d096a8f09a2` | r1 reviewer probe (generic objects only) |
| `review/rv_qc1.out` | `37e8d1b28c1558bd6f63674834b034997c02ab0e` | `c0925d59fe95ff02a47761c35a9fa18aecbc95000dbcad5d673ade202dde4ae0` | its output: 6 checks, 0 failures |
| `review/rv_qc2.py` | `50df8f2a60efe7d1898047173002c8dd873a64ee` | `64790f3088042a2b91f6376b083bdd7666171549598a960c7afeb5c4ba34abcb` | r1 reviewer probe (generic objects only) |
| `review/rv_qc2.out` | `96bcd84c9ddc17d8f8f468629c555fa240be1596` | `57039acd99ac7f22d59d9f1e1986dfc00d356908e16ecbf33a24f850b645478f` | its output: 10 checks, 0 failures |
| `review/rv_qc3.py` | `4f32cc040da079aa148ddbb8a745d888c2c802d5` | `919f0337b1c760a2cf5b91ed4bc74d17ac42c7e2dcc606efdb27665e31209a37` | r1 reviewer probe (generic objects only) |
| `review/rv_qc3.out` | `fde8e7a12b6c3cb356f35ad0148dd05bd41d2d32` | `5ac2ccee53a7512917850b4f8df27d29810c1cbf920b3f2db53b087694480d86` | its output: 6 checks, 0 failures |
| `review/rv_qc4.py` | `0a06c6f19f80344b17282554d1f2c393ab7ad316` | `aeab798e6263abe286b5aeaac1f185dda812b51648371daae16cca0970dfc447` | r1 reviewer probe (generic objects only) |
| `review/rv_qc4.out` | `97d38cb8321902b11875e1eb2d0399f3f326bed5` | `a903d7900ebba7c2b0ab95b267613acbe03a53a648807126e2c97c77a82f506a` | its output: 9 checks, 0 failures |
| `review/rv_hh2.py` | `0429ed0bc54f34610b95366b9564b3d656dcfaa1` | `8b2fd6f66f0493cb2e7350e83d842120db5a163e328d4f9189717a307588f93a` | r1 reviewer probe (generic objects only) |
| `review/rv_hh2.out` | `d54a5b8eae3bf7f5c092063980e451f6fac23382` | `f8b4657761662c63ac33eb954479ce0a639e6c4c5bc194933b304a054197859c` | its output: 3 checks, 0 failures |
| `review/rv_scope.py` | `73015a1b6b4f1b519d6dc70f7d16e176562bd96e` | `47722b3a9f69473f355a053ff2d901bd1f5036376c0c6be9ab382259e731c9b3` | r1 reviewer probe (generic objects only) |
| `review/rv_scope.out` | `22a43c5d0727e4a825f6f0c4758ff37cd69a04e7` | `64f6717905a96b1597477fc67758687802a49bb16ef3f72f99be3b58659bbc8a` | its output: 6 checks, 0 failures |
| `probes/q868h_generic_checks.py` | `568201fa4a5586de5f40a2ed224074779849e2ea` | `1977dfb8c6f1974dc0d4ff6f445485547c49dfece4dae6c6232c7927ccd70eb9` | r1 writer probe, cited by r1 and r2 §10 (generic objects only) |
| `probes/q868h_generic_checks.out` | `80dcad6babbf4ae3952b7585d1b299f46de63873` | `cd38be73aa74b26d62b4562e907773163a8b42a5399ef457f1869233327ff704` | its output, run 3: 27 checks, 0 failures |
| `probes/q868h_generic_checks.run1.out` | `2fa047a79480aea5e42e7b1c338666d14408d939` | `4a43977b4ef880f6811ccc8e09586ed6374112a8a05ed5536f5f1f41756dfcb1` | earlier run 1: 26 checks, 0 failures |
| `probes/q868h_generic_checks.run2.out` | `562fd49bcc8b861bd32d3d569480685feb063864` | `6296f936792c719b0a3a7268a029a23c0736447e767cce2a03040d527ab1e6f6` | earlier run 2: 26 checks, 0 failures |
| `probes/r2_generic_checks.py` | `99f857ffd83d1979d2738caf33343b607bad7258` | `ad8285ecb355dd8b6e1091eecb2b79209754da7fd68dd03fa8ad85c02d45b29a` | r2 writer probe, cited by r2 §10 (generic objects only); unreviewed |
| `probes/r2_generic_checks.out` | `78b6f13c93889a1475fe4e959e2c40ebd809994d` | `b0f9950af596b4d160f4909a252af274df6480645f6a647a8c319f6136dbcda8` | its output, run 3: 20 checks, 0 failures |
| `probes/r2_generic_checks.run1.out` | `ad1e2880c102758f4015fdc00eb847c9aed2b367` | `3a380ff698e66cc6f7d313468243283b4b38ec18ad1b2edee0afe0fdbd0428ec` | earlier run 1: 19 checks, 2 failures (R1b, R2a; helper defect recorded in r2 §10) |
| `probes/r2_generic_checks.run2.out` | `231becfe94baf97629a9c675dc8deb981aa69359` | `f1146443cf7086bf87d90f9e2180a67ee88085720953374ed600d39972b8f908` | earlier run 2: 19 checks, 0 failures |

The check counts are the closing lines of the outputs as committed; no probe was re-run for this
preservation.

## References these files make to content not on `main` (§A.42 item 8)

- **ASSESS-868 r3a and its review (support off `main`; open gap).** r1, r2 and the r1 review take
  the definition of Q-868-H (ASSESS §7), Lemma H (§4.1), witness w3 and the J-labels from
  ASSESS-868 r3a, cited as `reassess/868/ASSESS-868.md` (sha256
  `d97c4b6b17bea9675d02a697e5164862471dad840dfbe9b54532baacd6788e1b`), and cite its review
  REVIEW-868-r3 (sha256 `2a5014a526399437754ecba4a8d8496ead456c33f10483c1b723acd170f0fd1d`). The
  same bytes are in the source commit at `handoff-20261109/868-assess/ASSESS-868.md` (blob
  `7196beebd6d4c5811132a2bf0fba33386566780b`) and
  `handoff-20261109/868-assess/review/REVIEW-868-r3.md` (blob
  `18681975a022f2bde51c2365da4c4bb11b2529dd`). They are not copied here; the gap closes when they
  land on `main`.
- **Corpus sources (support on `main`).** The units read their sources at
  `fd539e150759a6ea51ab279aeeac80fc06050ade`, which is reachable from `main`.
- **`src/` copies** named in `DISPOSITIONS-r2.md` are extracts of files at that commit; they are
  not in the snapshot and are not needed beyond it.
- **Issue and comment references** (#867, #868, #914, #1147, #1169, and comments on #868, #1210
  and #1211) name accountable homes, open obligations and authorization or scope records; the files
  use no proof content from them.
