# Working-copy objects

Each file in this directory was written and reviewed as a session working copy before it was
committed. The table records, for each working copy, its last-modification time (UTC), its git
blob id and its SHA-256, read on 2026-11-12 and 2026-11-13 from the working copies. Reviews in this directory
identify the text they read by file name, line numbers and time; a blob id here that equals the
committed blob shows the reviewed working copy and the committed file are the same bytes.

| Modified (UTC) | File | Blob | SHA-256 |
|---|---|---|---|
| 2026-11-12T18:17:50Z | `OA-2-REPORT.md` | `ae3a78b553b4cdfca032085d2c3cf6d8772f350a` | `4aba70c5689b55dafb84875b300f695eabb04a94f40d8f04eb41e35aed336f34` |
| 2026-11-12T18:38:03Z | `REVIEW-OA-2.md` | `1d6a4674016723eb74f075337ff0f4a2aecac755` | `84df3089ba1b1036226533a9e2282379798c242458e472e05cb864d67960a227` |
| 2026-11-12T18:44:52Z | `OA-2-REPORT-r2.md` | `70a435ba4c1ebceaa87fada32812e43203dc4e22` | `ef3978a3a478a9456542b63e945a0247ca5757991f80d778f010bc7b0e9138f2` |
| 2026-11-12T18:49:16Z | `REVIEW-OA-2-r2.md` | `e55c66e579cee00cd1981c26d089974d3f88cd27` | `c8ef250c06b08cbea668e8c6f215a836d79e8b61f173ae686ca12cedac837234` |
| 2026-11-12T18:53:00Z | `OA-2-REPORT-r3.md` | `f7ca0968fee0acc5e7b038702490b467d2026baa` | `dd637ef698ea549659d8e411ab6692187bc8d92b86e3ca2a50e731c2532433bf` |
| 2026-11-13T02:37:36Z | `DELTA-REVIEW-OA-2-r3.md` | `73cf35eeec264cfda8e60cc5e4b290ef853d8faa` | `9115b2430fea20a1cb04192460bb5d6118eb72362eec7352d2cdc13104cca829` |
| 2026-11-13T02:38:00Z | `OA-2-REPORT-r4.md` | `9a6e368235d573e99fc24711850aa3930b4a313f` | `0fd7c0874c6908a1278750379f3124e0012e9abba48436c97e50de410a22e5a7` |

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
| `OA-2-REPORT.md` | `ae3a78b553b4cdfca032085d2c3cf6d8772f350a` | `4aba70c5689b55dafb84875b300f695eabb04a94f40d8f04eb41e35aed336f34` | `d57fb139db79b5dad68b2a89e10b078b352576b0` | `4b1f7ced09b769f281bd5c8f1cd618225b9df29cefbbc1e4045a8c21159f3e49` | 30 (a) |
| `REVIEW-OA-2.md` | `1d6a4674016723eb74f075337ff0f4a2aecac755` | `84df3089ba1b1036226533a9e2282379798c242458e472e05cb864d67960a227` | `c31efb366b45b35c44fe3d400f8eb72df6323364` | `9df1b0b8ce8791b4e8b43f78d35d0694238d4fcc5d0f26bbe0b714aa4030d1f2` | 11 (a) |
| `OA-2-REPORT-r2.md` | `70a435ba4c1ebceaa87fada32812e43203dc4e22` | `ef3978a3a478a9456542b63e945a0247ca5757991f80d778f010bc7b0e9138f2` | `aab0178811435e408b869863739eabc4c05d51dc` | `ac8e73ebe12d81d7148aed90b07023fc53dbb800a48b251e368d8c0483adde88` | 49 (a), 806 (a) |
| `OA-2-REPORT-r3.md` | `f7ca0968fee0acc5e7b038702490b467d2026baa` | `dd637ef698ea549659d8e411ab6692187bc8d92b86e3ca2a50e731c2532433bf` | `b097950f11eb2af40d29772bde317e77b6c01b82` | `145928fc5fcd78fb63f68cc261bc525e0428d9c1ffc4b3be56dd9f21769c49f2` | 58 (a), 940 (a) |
| `DELTA-REVIEW-OA-2-r3.md` | `73cf35eeec264cfda8e60cc5e4b290ef853d8faa` | `9115b2430fea20a1cb04192460bb5d6118eb72362eec7352d2cdc13104cca829` | `afbe3ca8213c974dc41913fc51e65f8b2cd16baf` | `12792e7614a57901be05f4039c3a20c2225709c0f73701391a30c6e7d3f43d07` | 331 (a), 461 (a), 462 (a), 470 (a), 473 (a, b), 475 (a), 671 (a, b) |
| `OA-2-REPORT-r4.md` | `9a6e368235d573e99fc24711850aa3930b4a313f` | `0fd7c0874c6908a1278750379f3124e0012e9abba48436c97e50de410a22e5a7` | `8f8ddf73366deb1a2caa13d8c826744d1ba87607` | `970935762ed94386726147f874b87fcab7666d392f117b0f00b2d3e0b90de0d3` | 65 (a), 958 (a) |
