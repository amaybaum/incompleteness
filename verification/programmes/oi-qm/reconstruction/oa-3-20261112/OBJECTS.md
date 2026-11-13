# Working-copy objects

Each file in this directory was written and reviewed as a session working copy before it was
committed. The table records, for each working copy, its last-modification time (UTC), its git
blob id and its SHA-256, read on 2026-11-12 from the working copies. Reviews in this directory
identify the text they read by file name, line numbers and time; a blob id here that equals the
committed blob shows the reviewed working copy and the committed file are the same bytes.

| Modified (UTC) | File | Blob | SHA-256 |
|---|---|---|---|
| 2026-11-12T19:18:57Z | `OA-3-REPORT.md` | `1eb872a2954e553e1fb83d415826fe14b6bb02f0` | `547a4d54984427b3b7509c8ac5816394924471ba602b322915eb6c51ccc2227e` |
| 2026-11-12T19:30:47Z | `REVIEW-OA-3.md` | `261abfe59af27c63b8af5d59bea27804a4426b44` | `7b1aeaeede56defc1b021b181381f58632699d9c4e1436b2fbd80b45840e53e5` |
| 2026-11-12T19:41:10Z | `OA-3-REPORT-r2.md` | `de4286025d378466449c100ddf14ebe3b1b496c3` | `1c28a6347cd641d9096c99fee0662c7adf2fd39cc8c83ba06e977bfc0e72baa0` |
| 2026-11-12T19:44:15Z | `RECHECK-OA-3-r2.md` | `0ed4d04a12e65e6b4732de8757b7839cff6c630e` | `68e679be002df9b2ad52a064c65d6cd5190c42732e36bf6513be679d00df4cb3` |
| 2026-11-12T20:10:17Z | `OA-3-REPORT-r3.md` | `ad0756caf01f48bd4f16ca522d75f0d66a6e0c12` | `3aafffc0e0c750152edce7c984d9f57fb907d9cd4548eeea2da044ce1b3078c1` |
| 2026-11-12T20:10:34Z | `DELTA-REVIEW-OA-3-r3.md` | `d6d0f481fb462ef3abf931fd13850aab73a67be1` | `2b6613ebe308a1ef8918f16c3e38ddc66ecdd3d532acd235cde9bc042620fef6` |
| 2026-11-13T02:42:15Z | `DELTA-REVIEW-OA-3-r4.md` | `4de308546e3283b9c3f5ce285fc38cd4b34f34ca` | `80d0cc777313ad5b0bfb2085e25a4ee55d3e986f7d965acbb580ebb1158cf9fb` |
| 2026-11-13T02:42:32Z | `OA-3-REPORT-r4.md` | `0a36fd05ba6931705ecdbb1de9962d58a307c1cb` | `4b847d72bceae6e6eacdffae14e00d801d086826e04f176fde2d20ea26e5c973` |

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
| `OA-3-REPORT-r2.md` | `de4286025d378466449c100ddf14ebe3b1b496c3` | `1c28a6347cd641d9096c99fee0662c7adf2fd39cc8c83ba06e977bfc0e72baa0` | `6693de0b24644d9557e16146e5145ee3f1449459` | `f9a7354d48dcea780785965931313f5124c1fe90fc01dfbecd8ca451630aacad` | 38 (a) |
| `DELTA-REVIEW-OA-3-r3.md` | `d6d0f481fb462ef3abf931fd13850aab73a67be1` | `2b6613ebe308a1ef8918f16c3e38ddc66ecdd3d532acd235cde9bc042620fef6` | `47ea25fae4d073d73ce952fd1b807d074081d487` | `f7654539428d3f0256c771ca03612bb2e33a809a27efcbc8660d2cb91b09c4d0` | 12 (a), 106 (a), 218 (a) |
| `DELTA-REVIEW-OA-3-r4.md` | `4de308546e3283b9c3f5ce285fc38cd4b34f34ca` | `80d0cc777313ad5b0bfb2085e25a4ee55d3e986f7d965acbb580ebb1158cf9fb` | `cfa2055d8c1500b24ce02f2214bc58e64204d364` | `b16d3c22a999c194caecc431470984cb7cb7b0674a3c507587d6c738a3a064c8` | 11 (a) |
