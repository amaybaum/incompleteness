# Q-868-H unit 1: preserved objects

**WIP / UNVERIFIED research record, not for merge.** This directory preserves, byte for byte, the
Q-868-H unit 1 files (Issue #868; parent programme #1169) from the 2026-11-09 session handoff
snapshot. Nothing here is adopted, promoted or proposed for the manuscripts, and preservation
changes no status (§A.42 item 6; §A.46 item 3). Every review named below is a model-written
review, not human verification (§A.46 item 7).

The subdirectory `assess-868-r3a/` preserves, byte for byte, the assessment these files build on:
ASSESS-868 r3a, its review REVIEW-868-r3, DISPOSITIONS-r3a and the probes they rely on (section
"`assess-868-r3a/`" below).

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

- **r2** (now `r2/Q868H-UNIT1.md`; at `Q868H-UNIT1.md` until r3) was **independently reviewed** after preservation: verdict ACCEPT WITH CHANGES (`review/REVIEW-Q868H-UNIT1-r2.md`). At preservation time it was **not yet independently reviewed.** Its header reads "revision r2.
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
| `r2/Q868H-UNIT1.md` | `4d96a563d5a6f9c097ebb812b9f465c2f7d3a711` | `1e128f286b14be3294cb8411e21f0b4b4516cbc9985fc2589fb6362a752179e6` | r2 (moved from `Q868H-UNIT1.md`, bytes unchanged); review ACCEPT WITH CHANGES; superseded by r3 |
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

## `assess-868-r3a/`: ASSESS-868 r3a, its review and probes

**Source.** The same commit `820519cf011c09b37690213a758106ed3aa15cc2`, path prefix
`handoff-20261109/868-assess/`, with the relative path below kept. Each committed blob equals the
source blob, and the bytes equal the session working copy and the recovery staging copy (compared
byte for byte on 2026-11-13). Preservation is authorized by #1169 comment 6852816462, items 1–2.

**Selection.** The three named files; every probe file REVIEW-868-r3 wrote, re-ran or hash-confirmed,
with the recorded outputs its re-runs compare against; and the probe files ASSESS-868 r3a §11 and
DISPOSITIONS-r3a cite (`r3a_check` and the recorded run-1 outputs). Not copied, and still only at
the source commit: the earlier revisions `r1/`, `r2/ASSESS-868.md`, `r3/ASSESS-868.md`,
`DISPOSITIONS-r2.md` and `DISPOSITIONS-r3.md`; the earlier reviews `review/REVIEW-868.md` and
`review/REVIEW-868-r2.md`; the r2 reviewer's re-run outputs `review/probes/rv2/`; and
`review/probes/writer_rerun.out`.

**Status as recorded.** #868 comment 6742050189 (`amaybaum`, 2026-11-09T14:07:16Z): "Independent
review of r3: ACCEPT WITH NITS (REVIEW-868-r3.md, `2a5014a5…`)"; "Nits: applied in r3a
(`d97c4b6b…`)"; findings "model-written, model-reviewed; not human verification". #914 comment
6742050590 (`amaybaum`, 2026-11-09T14:07:18Z), a planning entry, cites "The reviewed ASSESS-868
(r3a, `d97c4b6b…`; review `2a5014a5…`, ACCEPT WITH NITS)". REVIEW-868-r3 reviewed r3
(`4cd2fb04…`); the r3 → r3a changes in DISPOSITIONS-r3a and the probe `r3a_check` have no separate
review. The probes check generic objects only. The check counts are the closing lines of the
outputs as committed; no probe was re-run for this preservation.

| File (under `assess-868-r3a/`) | Blob | SHA-256 | Role and status as recorded |
|---|---|---|---|
| `ASSESS-868.md` | `7196beebd6d4c5811132a2bf0fba33386566780b` | `d97c4b6b17bea9675d02a697e5164862471dad840dfbe9b54532baacd6788e1b` | r3a; the nits of REVIEW-868-r3 applied |
| `DISPOSITIONS-r3a.md` | `7f280769b9c30fccccd562cf5f44764d5fca9224` | `d4f71deb5c4cfde36ee0c15d3e7adff56f3004aac395f67e2cf8beb7258db1b2` | r3 → r3a change note; not separately reviewed |
| `review/REVIEW-868-r3.md` | `18681975a022f2bde51c2365da4c4bb11b2529dd` | `2a5014a526399437754ecba4a8d8496ead456c33f10483c1b723acd170f0fd1d` | model-written independent review of r3 (`4cd2fb04…`); verdict ACCEPT WITH NITS |
| `probes/g868_generic_checks.out` | `0b9db307754817704e1e7d0c8e9386791d5e33eb` | `e93f65418777522da2ed2d271493defe3aa6b6d2f2b93e64c9c1a15005e283e3` | its recorded output: 18 checks, 0 failures |
| `probes/g868_generic_checks.py` | `417dc522f0732f9b8d2168e8169bb0ff892f515d` | `292d16b04a1f5eda2298289962eede5fcaa347da24efba7f35b9571d1c8ef335` | writer probe (r1), cited in r3a §11; re-run by REVIEW-868-r3 |
| `probes/g868_generic_checks.run1-misspecified.out` | `22df95302dbccc10dce17c5305e071596edb6c3b` | `d4521708ff37f045c6b69b499f7ef3747a2d581925fc8da99769af328a016a9f` | run 1 recorded in r3a §11: 16 checks, 1 failure (G3b) |
| `probes/r2_validity_scope.out` | `1b556e9c2719170c28ec671d60edd811e2d3f6d8` | `d86e03c1979355d7bee206e9e68e3712576ec035fe0683df2f8e0a48558ef020` | its recorded output: ALL PASS |
| `probes/r2_validity_scope.py` | `4ca29efc51fefa280bef0a80a45b345f7bd644cc` | `cedf61129150dcac287675a1107f8cefbb68e94e3256a472faeb2060023a7101` | r2 probe as edited in r3 (V5 docstring only), cited in r3a §11; re-run by REVIEW-868-r3 |
| `probes/r2_validity_scope.run1-float.out` | `23a1a33fbd2de456c384b439ddc75453f6493454` | `a101caf5b74c140db9175fd7a7711ebe53a821208618d9bd0977d1d7a36708f2` | run 1 recorded in r3a §11: SOME FAIL (V4) |
| `probes/r3_scope_checks.out` | `67a9440306c09acc91a188c8b471d1911d3512f1` | `394b6fd8e033f49ca784457c1bbee09a2c1757e1b93b47d826471dbb3be58ed9` | its recorded output: 27 checks, 0 failures |
| `probes/r3_scope_checks.py` | `455a618096728ff0c9b40951e4cc2de2aa922ae9` | `e6afb063d08802f45c59e258b2f6f4933c9adc7041e71ac8d2ab7568ba299575` | r3 writer probe, cited in r3a §11; re-run by REVIEW-868-r3 |
| `probes/r3_scope_checks.run1.out` | `8356be28187f5dfaf5a8fabd28cb6a89ac09150b` | `ec76650ab8c46b7e6c13adf364e945247cbafcf3a353cdcb4c0dad06aec07223` | run 1 recorded in r3a §11 and hash-confirmed by REVIEW-868-r3: 24 checks, 1 failure (W8 control) |
| `probes/r3a_check.out` | `be8eece1e0c863c1ac65370ff48b3d6cad88549b` | `6e16d0eaa9be781c9b0042272744bf84d6a38ee20d3a761803955338fe84a01d` | its recorded output: 16 checks, 0 failures |
| `probes/r3a_check.py` | `d6de50156ae825fcf43ebee1ae03acfee0b6dcd1` | `5121c0f48e7500ecb8b630ce74f081f539e93c8908fed4879d9bf5eeefc3f4b5` | r3a writer probe, cited in r3a §4.4, §11 and DISPOSITIONS-r3a; not reviewed |
| `r2/probes/r2_validity_scope.py` | `0eb70f9456a8e20c9c40894c474d7fd57f363482` | `60095dc01a21c62735f81f29ac85f11986a58ff535cc72f6112a3350fa5e0ea2` | r2 probe as originally recorded (`60095dc0…`); re-run by REVIEW-868-r3 |
| `r2/probes/r2_validity_scope.out` | `1b556e9c2719170c28ec671d60edd811e2d3f6d8` | `d86e03c1979355d7bee206e9e68e3712576ec035fe0683df2f8e0a48558ef020` | its recorded output: ALL PASS |
| `review/probes/rv3_868_checks.py` | `356b3ef019f90574ca2b5678541b85c4f70998e6` | `cbc896dd8a03a830673e76e2ab8583c1d9a551b23b26c74b54d4ddfaa2fc999f` | REVIEW-868-r3's own probe |
| `review/probes/rv3_868_checks.out` | `6054cd15489327291a38c5458f3f67b32166b1be` | `9a078144ecb0351abcedab5c2095df60a96ea30ce4910f4eddec32ba9fb63a22` | its output: 24 checks, 0 failures |
| `review/probes/rv3/g868.out` | `0b9db307754817704e1e7d0c8e9386791d5e33eb` | `e93f65418777522da2ed2d271493defe3aa6b6d2f2b93e64c9c1a15005e283e3` | REVIEW-868-r3 re-run of `g868_generic_checks.py`: 18 checks, 0 failures |
| `review/probes/rv3/r2_edited.out` | `1b556e9c2719170c28ec671d60edd811e2d3f6d8` | `d86e03c1979355d7bee206e9e68e3712576ec035fe0683df2f8e0a48558ef020` | REVIEW-868-r3 re-run of `probes/r2_validity_scope.py`: ALL PASS |
| `review/probes/rv3/r2_orig.out` | `1b556e9c2719170c28ec671d60edd811e2d3f6d8` | `d86e03c1979355d7bee206e9e68e3712576ec035fe0683df2f8e0a48558ef020` | REVIEW-868-r3 re-run of `r2/probes/r2_validity_scope.py`: ALL PASS |
| `review/probes/rv3/r3.out` | `67a9440306c09acc91a188c8b471d1911d3512f1` | `394b6fd8e033f49ca784457c1bbee09a2c1757e1b93b47d826471dbb3be58ed9` | REVIEW-868-r3 re-run of `r3_scope_checks.py`: 27 checks, 0 failures |
| `review/probes/rv3/rv.out` | `ee17a903f4e938f7d8e9bef89de3e1afcc23ff64` | `c83449e42fd61a52d48c1ce263fca3bc2b6dc7140709ec432ebeb321ee28b2cb` | REVIEW-868-r3 re-run of `rv_868_checks.py`: 27 checks, 0 failures |
| `review/probes/rv3/rv2.out` | `86c2cd3ed479f10803720c4f640c7a422e511963` | `b7eaf2a782a36414ca5c09de646eed596b9f82533b157b2e51d1fac10e332d14` | REVIEW-868-r3 re-run of `rv2_868_checks.py`: 26 checks, 0 failures |
| `review/probes/rv_868_checks.py` | `51868668e71e624fd733a4e0f45f63e21e093506` | `b460abd4f19d30e3cacd05cd664cef356b3a5c2f85b87db994268aba0af70bc4` | first-round reviewer probe, cited in r3a §11; re-run by REVIEW-868-r3 |
| `review/probes/rv_868_checks.out` | `ee17a903f4e938f7d8e9bef89de3e1afcc23ff64` | `c83449e42fd61a52d48c1ce263fca3bc2b6dc7140709ec432ebeb321ee28b2cb` | its recorded output: 27 checks, 0 failures |
| `review/probes/rv2_868_checks.py` | `eaae4eeb9087b41a00304d3e574faa51e09e1876` | `791556c5a3f108c281da46c89dae7a9b11d3b955d8f2fcf2b6cfdd3f7ddc7a6c` | r2 reviewer probe, cited in r3a §11; re-run by REVIEW-868-r3 |
| `review/probes/rv2_868_checks.out` | `86c2cd3ed479f10803720c4f640c7a422e511963` | `b7eaf2a782a36414ca5c09de646eed596b9f82533b157b2e51d1fac10e332d14` | its recorded output: 26 checks, 0 failures |

## References these files make to content not on `main` (§A.42 item 8)

- **ASSESS-868 r3a and its review (support now on this branch; on `main` only when landed).** r1, r2
  and the r1 review take the definition of Q-868-H (ASSESS §7), Lemma H (§4.1), witness w3 and the
  J-labels from ASSESS-868 r3a, cited as `reassess/868/ASSESS-868.md` (sha256
  `d97c4b6b17bea9675d02a697e5164862471dad840dfbe9b54532baacd6788e1b`), and cite its review
  REVIEW-868-r3 (sha256 `2a5014a526399437754ecba4a8d8496ead456c33f10483c1b723acd170f0fd1d`). Both
  are now in this directory, at `assess-868-r3a/ASSESS-868.md` (blob
  `7196beebd6d4c5811132a2bf0fba33386566780b`) and `assess-868-r3a/review/REVIEW-868-r3.md` (blob
  `18681975a022f2bde51c2365da4c4bb11b2529dd`), byte-identical to the cited hashes. The gap is closed
  on this branch; on `main` it closes only when this directory lands.
- **References made by the `assess-868-r3a/` files.**
  - Earlier ASSESS-868 revisions, DISPOSITIONS-r2/-r3 and the reviews REVIEW-868 and REVIEW-868-r2:
    provenance for the revision history; at the source commit only.
  - `rerun-r3/` outputs (r3a §11): provenance; their bytes equal `probes/g868_generic_checks.out`
    and `review/probes/rv2_868_checks.out`, which are in this directory.
  - BRIDGE-UNIT1 r2–r5 and REVIEW-UNIT1 r1–r4 (#1211), cited by hash as draft inputs labelled as
    hypotheses (r3a §2) and by REVIEW-868-r3: support off `main`. Every cited hash matches a file at
    the source commit under `handoff-20261109/1211-bridge/` (r5 `78f1098e…`, r4 `4e97610d…`, r3
    `ee1c83c0…`, r2 `3905569b…`; reviews `e489fc19…`, `7a6a7f1c…`, `3cdf7dc2…`, `e242a794…`). Open gap.
  - QPHEN Phase 1 r5 texts SHARED-MECHANISM (`a7206701…`), QX6-BELL-CHSH (`9e9c0d02…`) and
    QX4-INCOMPATIBILITY-LG (`7f4cd21d…`), and REVIEW-PHASE1-r4 (`755c3af0…`), cited by hash as draft
    inputs labelled as hypotheses (r3a §2): support off `main`. Branch
    `research/qphen-phase1-frozen-20261109` holds the r7c texts and a copy of REVIEW-PHASE1-r4 with
    one phrase changed, whose hash differs; the cited bytes are committed for preservation on branch
    `research/recovered-1169-20261113`. Open gap.
- **Corpus sources (support on `main`).** The units read their sources at
  `fd539e150759a6ea51ab279aeeac80fc06050ade`, which is reachable from `main`.
- **`src/` copies** named in `DISPOSITIONS-r2.md` are extracts of files at that commit; they are
  not in the snapshot and are not needed beyond it.
- **Issue and comment references** (#867, #868, #914, #1147, #1169, and comments on #868, #1210
  and #1211) name accountable homes, open obligations and authorization or scope records; the files
  use no proof content from them.

## Known SC-42 hits (bytes preserved unchanged)

The SC-42 added-text scan flags these lines of preserved files. Each names the session-storage
directory of the session that wrote the file; the bytes are kept unchanged.

| File | Line | Pattern |
|---|---|---|
| `assess-868-r3a/ASSESS-868.md` | 142 | local path (session-storage directory name in a draft-input citation) |
| `assess-868-r3a/ASSESS-868.md` | 151 | local path (session-storage directory name in a draft-input citation) |
| `assess-868-r3a/review/REVIEW-868-r3.md` | 67 | local path (session-storage directory name) |

## r3 and the review of r2 (added 2026-11-13)

| File | Blob | SHA-256 | Status |
|---|---|---|---|
| `Q868H-UNIT1.md` | `ebf5215b13e3a7efb2274f0069b175925bcdff79` | `bf04ea952c2837c392e1af042207d490f45ebe9ba9fd93b8fe87461d1a862c38` | r3; applies RC1–RC5 and O1, O2, O3, O7 of the r2 review; focused confirmation ACCEPT; ChatGPT ACCEPT WITH DOCUMENTATION NITS (review 5891666660), nits applied |
| `DISPOSITIONS-r3.md` | `406ddfb96c0ac73bca1432ca27fc61fc8341a636` | `fd75e7c68fd738128120dcd302248fa2b047a40521d9015b59cf60d5e0fecbd5` | r2→r3 change note |
| `review/REVIEW-Q868H-UNIT1-r2.md` | `144cc7db4586fc108a06a6e94b09b666322950ea` | `651612e89c964c05bbc31d7b47c67cbb855456622b8eaee98bf3c79d9865268e` | fresh non-author model review of r2 at `82f592db`; verdict ACCEPT WITH CHANGES (RC1–RC5) |

Owner decision for r3 (amaybaum, 2026-11-13; #868 c.6853568040): "r3; ratify the probes". The owner retroactively ratifies the unit's generic linear-algebra probe scripts as covered.
