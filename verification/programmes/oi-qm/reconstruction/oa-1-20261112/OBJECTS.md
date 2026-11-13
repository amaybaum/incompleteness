# Working-copy objects

Each file in this directory was written and reviewed as a session working copy before it was
committed. The table records, for each working copy, its last-modification time (UTC), its git
blob id and its SHA-256, read on 2026-11-12 from the working copies. Reviews in this directory
identify the text they read by file name, line numbers and time; a blob id here that equals the
committed blob shows the reviewed working copy and the committed file are the same bytes.

| Modified (UTC) | File | Blob | SHA-256 |
|---|---|---|---|
| 2026-11-12T17:00:43Z | `OA-1-REPORT.md` | `f2cc46e89b3ac5a8b405cec5eb22f86c8d4a6ed1` | `caf77a2a84af152d4b78f1c1bb8543b3576e62d3abf0081831fde4a39537ea72` |
| 2026-11-12T17:13:51Z | `REVIEW-OA-1.md` | `c6608a806f697556a222077a800f505f5ab4f55b` | `d4250c448a5a2dd5e8da070856f09a9e844c1969ce7d10306bfdb748be23db6d` |
| 2026-11-12T17:17:45Z | `OA-1-REPORT-r2.md` | `44f43b3e52af1a0540688d78702f59c1039d7398` | `b17318cdcacf3f5602b7b81af1583825e1d2f0d75863c95ac59f0bb3ffbe99fa` |
| 2026-11-12T17:23:14Z | `REVIEW-OA-1-r2.md` | `938fa6bc5532f05c9a6690ecdd8151cf8947a664` | `ab92f60ce3ef94c94708196d0012b67a53510351b10c6a6128b6b44be3ff3270` |
| 2026-11-12T17:27:51Z | `OA-1-REPORT-r3.md` | `dd7ed08d780c20dbdc6f68ec175b1c6067f6d671` | `ee53ea3837276dfd0a04846f448aa220ce95bf578bc582c8af7bba8972a79cb3` |
| 2026-11-12T17:30:08Z | `REVIEW-OA-1-r3.md` | `adfa30cd3460c8acd34d960a284101c002168c38` | `2fbab9c4d2cbd29e29538b82dd1fd475ea8c0356bd45b14a2af83d9e41a0fe9b` |
| 2026-11-12T17:31:19Z | `OA-1-REPORT-r4.md` | `41a1fb79cc640f3b5347ce5071d43d089e967e24` | `87e60622480fa3c35a01e38714bb0b6d965134308d059b036817926ce196d291` |
| 2026-11-13T02:30:06Z | `DELTA-REVIEW-OA-1-r4.md` | `ecb6711391605c4a92f463fe7d754ab60dbbb7d7` | `40359602ff5e9a5ddd5e8dd5e78592f1b7ea9c9870d9fc806e2c5342039e41c1` |
| 2026-11-13T02:30:23Z | `OA-1-REPORT-r5.md` | `5a16b213ebe96846e53072bf1cac226e455f9f72` | `75a0e997446a9c0167a95ce3ed81da22155ecd0966359d494791ee6353d33fd1` |

## Committed bytes differ from the reviewed working copies

The files below were committed in this directory with the reviewed bytes, then changed on the
listed lines only, by one or both of two substitutions:

- **(a)** the name of the session's temporary working directory is replaced by the word `working`,
  because the SC-42 added-text scan rejects that name as a local-path term;
- **(b)** a full 40-character working-copy blob id is replaced by its first 8 characters, because
  those working copies were not kept in the repository (§A.42 item 3).

No other byte differs; every file keeps its line count and line numbers, so line citations are
unaffected. Restoring the original text on the listed lines reproduces the reviewed bytes exactly:
under (a), every occurrence of `working` on a listed line is the substituted word; under (b),
the full id is the one at the same place in the reviewed blob. Each reviewed blob is in this pull
request's commit history, so it stays in the repository when the pull request lands by merge
commit. The reviewed blob and SHA-256 are the row in the table above. The restoration was checked
for every file below: it reproduces the reviewed blob and SHA-256.

| File | Reviewed blob | Reviewed SHA-256 | Committed blob | Committed SHA-256 | Lines changed (rule) |
|---|---|---|---|---|---|
| `REVIEW-OA-1.md` | `c6608a806f697556a222077a800f505f5ab4f55b` | `d4250c448a5a2dd5e8da070856f09a9e844c1969ce7d10306bfdb748be23db6d` | `e7dcaeea09e74b6338a37771226aa3cf693f2e81` | `5d79e1064524a6b360718b54e3b73da91db66f1c1b586f53448ba34fbd7f3a79` | 19 (a), 21 (a) |
| `DELTA-REVIEW-OA-1-r4.md` | `ecb6711391605c4a92f463fe7d754ab60dbbb7d7` | `40359602ff5e9a5ddd5e8dd5e78592f1b7ea9c9870d9fc806e2c5342039e41c1` | `bdced6024579bf428a4d9fb91964fc1f4da2c620` | `38ad9d88a11729f763da1311aed88e1dae773e7e4604d54cd75445c42934320c` | 279 (a, b), 281 (a), 388 (a, b), 389 (a, b), 390 (a) |
