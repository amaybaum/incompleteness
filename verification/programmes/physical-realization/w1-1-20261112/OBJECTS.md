# Working-copy objects

Each file in this directory was written and reviewed as a session working copy before it was
committed. The table records, for each working copy, its last-modification time (UTC), its git
blob id and its SHA-256, read on 2026-11-12 from the working copies. Reviews in this directory
identify the text they read by file name, line numbers and time; a blob id here that equals the
committed blob shows the reviewed working copy and the committed file are the same bytes.

| Modified (UTC) | File | Blob | SHA-256 |
|---|---|---|---|
| 2026-11-12T16:57:46Z | `W1-1-REPORT.md` | `b9eddf4b9cf4943d26ef7a118a6f2eee65df4c9c` | `764bddb2d8e72092381f7491345bdf2cb827b75da7d2af9968a55a6b0689efbb` |
| 2026-11-12T17:05:54Z | `REVIEW-W1-1.md` | `aa6cc6b6b3ff19fd70309b33018c16c087adc8a9` | `3455ad14f97d1d894e8953a80eafd0b9f50724661e514317ff9169f9e4228fce` |
| 2026-11-12T17:09:23Z | `W1-1-REPORT-r2.md` | `63a5d1233b28f5b0e19ca99c171ef01750ec104b` | `18a26718892f747d6f4341bb7bb60ee5fcd12e415fb090c11524aa586578faa8` |
| 2026-11-12T17:12:01Z | `REVIEW-W1-1-r2.md` | `f466f9505c58a627263f3a098ba54c8c6d8da61e` | `9f22a4ba712def282b0e66f6bdd14df23416cd05f615acef3cd36e26f38d0952` |
| 2026-11-12T17:13:37Z | `W1-1-REPORT-r3.md` | `890429362bc27f580675b8c7d2c6ef04ed01d784` | `fcfe12a16bf1c3d2bb26e64beb2868f1b405f5fe91c2623183d67d8a07420973` |
| 2026-11-13T02:25:43Z | `DELTA-REVIEW-W1-1-r3.md` | `8f9dcfcc4d075f1de52201f8834fcb8647a00832` | `31820704bd9b06e74e58374161aab58108090b0cd0cce3b748fa07ad836c7fbd` |
| 2026-11-13T02:25:16Z | `W1-1-REPORT-r4.md` | `34b1a16fc84ed38b19aec482b555fe8876815959` | `ee9fe1d7759dbb7c27d1814f61493b0ebac07b2dd87db0c91e4338587a6a186c` |

## Committed bytes differ from the reviewed working copies

The files below were committed in this directory with the reviewed bytes, then changed on the
listed lines only, by one or both of two substitutions:

- **(a)** the name of the session's temporary working directory is replaced by the word `working`,
  because the SC-42 added-text scan rejects that name as a local-path term;
- **(b)** a full 40-character working-copy blob id is replaced by its first 8 characters, because
  those working copies were not kept in the repository (§A.42 item 3).

No other byte differs; every file keeps its line count and line numbers, so line citations are
unaffected. Restoring the original text on the listed lines reproduces the reviewed bytes exactly:
under (a), every occurrence of `working` on a listed line is the substituted word, except on
line 226 of `W1-1-REPORT.md`, where only the first is (the second, in "The working copies", is
original); under (b), the full id is the one at the same place in the reviewed blob. Each reviewed
blob is in this pull request's commit history, so it stays in the repository when the pull request
lands by merge commit. The reviewed blob and SHA-256 are the row in the table above. The restoration was checked
for every file below: it reproduces the reviewed blob and SHA-256.

| File | Reviewed blob | Reviewed SHA-256 | Committed blob | Committed SHA-256 | Lines changed (rule) |
|---|---|---|---|---|---|
| `W1-1-REPORT.md` | `b9eddf4b9cf4943d26ef7a118a6f2eee65df4c9c` | `764bddb2d8e72092381f7491345bdf2cb827b75da7d2af9968a55a6b0689efbb` | `a29cbcd4769ff6cdae82f932129e52985beb42f1` | `8635cd35a37f3f0802334f2ead637ed023b7a3592aabcb5f36ecdfae2735e689` | 226 (a) |
| `REVIEW-W1-1.md` | `aa6cc6b6b3ff19fd70309b33018c16c087adc8a9` | `3455ad14f97d1d894e8953a80eafd0b9f50724661e514317ff9169f9e4228fce` | `15a975d2d2b540b7994d9cbada53e1fbdf2efcf6` | `a1a7766c818b24beb3b26398c6210d6360b760bc2cd5ed8702f5f24fb5d4adbb` | 211 (a) |
| `W1-1-REPORT-r2.md` | `63a5d1233b28f5b0e19ca99c171ef01750ec104b` | `18a26718892f747d6f4341bb7bb60ee5fcd12e415fb090c11524aa586578faa8` | `e67231b1d22399b5ca192b2a14ae1f57504c4d16` | `22157778fc06b45ef7ccdcb7787568e42dcab277d0def7f69baf8a06d1f0389b` | 360 (a) |
| `W1-1-REPORT-r3.md` | `890429362bc27f580675b8c7d2c6ef04ed01d784` | `fcfe12a16bf1c3d2bb26e64beb2868f1b405f5fe91c2623183d67d8a07420973` | `7920d80d4a4bd2e1259b5181f5a08744537e5738` | `083e68f1f1646a83e8be47f93580a051e44508ace5b23ee69d19c02d31d922c3` | 383 (a) |
| `DELTA-REVIEW-W1-1-r3.md` | `8f9dcfcc4d075f1de52201f8834fcb8647a00832` | `31820704bd9b06e74e58374161aab58108090b0cd0cce3b748fa07ad836c7fbd` | `5a3f09fbb835083fe5885c31531132acd985e5d6` | `3feccdcae5e51f903368bdbd356687ba64edbfe31b10088be275afb0a6de1499` | 228 (b), 270 (b) |
| `W1-1-REPORT-r4.md` | `34b1a16fc84ed38b19aec482b555fe8876815959` | `ee9fe1d7759dbb7c27d1814f61493b0ebac07b2dd87db0c91e4338587a6a186c` | `8bf646292f54c649a2927a579675d04ad8d21462` | `2436f5d127484dee1d5c9bf6d95f6417b6d60eef27598f1e48e214f2491313b2` | 383 (a) |
