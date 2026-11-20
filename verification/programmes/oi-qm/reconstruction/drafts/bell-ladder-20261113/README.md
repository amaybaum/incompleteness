# Bell debugging ladder r3: preservation note

This note covers the seven files listed below and no other file. `OWNER-EXCEPTION.md` in this
directory records the owner exception under which the package lands with the gaps named below. Each is a byte-identical copy from
draft PR #1273 (branch `research/bell-ladder-868-20261113`, head
`d8e4f80e71b64972ee3e87a874544c8bd358d5c2`), at the path it has there. They are preserved because a
record on `main` uses r3 and its notes as support (§A.42 items 2 and 8). Preservation establishes no
claim of r3 (§A.46 item 1) and changes no scientific status.

Authority: owner decision of 2026-11-20 (`amaybaum`, #1169 comment 7030839727): "Narrow preservation
PR(s), not merges of the original drafts, for #1273, #1231 and #1232, plus #1274 where it is
needed." Accountable Issue: #868.

## Files

| File | Content | Blob at `d8e4f80e` | SHA-256 | Bytes |
| --- | --- | --- | --- | --- |
| `BELL-LADDER-r3.md` | the ladder, r3 | `0298088d66547e0aa28b634bacae196991507a8c` | `6e7708ceda86b8121dad6904cbc6c8373e819c08985a481808168a9778ebb5a6` | 29231 |
| `NOTES-r3.md` | writer's notes, r3 | `963d73523b2449d1674dbd0e6b9f000a7de5e351` | `831554fb18221422e947d6e08735c709d51cdc4a36558634d1a2c5c82a9e7792` | 9461 |
| `CONFIRM-r3.md` | confirmation of r3: ACCEPT | `c968776a8c082cc9f685dfa736d79f85f454ce6e` | `5f5e9e4562c2de4313c3114fba23cc7dc90563ff1c2e297577dadaffe51bfaaa` | 2156 |
| `REVIEW-r1.md` | review of r1: ACCEPT WITH CHANGES | `c84142dca0b7f554ddb5a449a1698399557a1fef` | `746171e9f5864e1e1ce29426d692d11ff870331c500278914ac0cafe1e6460ef` | 22548 |
| `RESPONSE-r1.md` | dispositions of the r1 review | `fe6301a93f25154681f5079b6d971f1e2cd45327` | `496a2f7b8e9ffd02a1e09b2f950d5580fbbee31b5bcbf27985e93fc4d0077294` | 5511 |
| `CONFIRM-r2.md` | confirmation of r2: ACCEPT WITH CHANGES | `0a629d501c2ee6c752e685b2b881b007acb0430e` | `c68dd910cc47958af481f3798aaac60f9978d332c564abe8223bfb1f9e8ea2f2` | 5829 |
| `RESPONSE-r2.md` | dispositions of the r2 confirmation | `23dc97b1979fca2ce523d073c2a5a6802909a42c` | `e02e0928448db560decc67cf2a0a0b60a70ae8407f897899f9f8b58d76c610c2` | 2732 |

`git hash-object` on each file reproduces its blob. Each SHA-256 equals the reviewed and committed
value that `OBJECTS.md` on #1273's branch records; it lists no substituted line.

## Citations on `main` that use these files

`selection-discriminator-20261113/support/synthesis/SYNTHESIS-r3.md` (SR3), line 39 and §8 lines
726–728, cites `drafts/bell-ladder-20261113/` at `d8e4f80e`: `BELL-LADDER-r3.md` (blob `0298088d`) as
support off `main` for MM-2, MM-4c, MM-5, MM-6, MM-7, MM-8, A4, T1 and T6; `NOTES-r3.md` (blob
`963d7352`) as support off `main` for MM-2 (:55–58), MM-5 (:67–69), MM-6 (:69), T7 (:76–78) and its
§4; `CONFIRM-r3.md` (blob `c968776a`) as provenance. Those paths and blobs are this directory's
files; the uses are support on `main` at these paths. `selection-discriminator-20261113/RETENTION.md`
(S4) compares that directory's assessment with SR3's MM-2, MM-3, MM-7 and MM-8. SR3 is not edited:
`selection-discriminator-20261113/ARTIFACTS.sha256` and `RETENTION.json` pin its bytes.

## Off-`main` support of r3 itself

r3's own reference table (`BELL-LADDER-r3.md` §6, lines 286–304) classifies these as support off
`main`; their standing at this landing:

- Bell-scope r2 (Theorem N, N′, Lemma G, the §4 bound, NBA; stages 5–6 and §0) lands in this change at
  `drafts/bell-scope-868-20261111/`, whose `README.md` gives its review findings.
- SUBSTATE-BRIDGE-1 r2 routes A/B/C, N3 and N4 (SB:177–190; §4 route C and stage 7): carried in
  `intervene-substate-results-20261113/NEW-RESULTS.md` §5, whose preservation is a separate change.
- SUBSTATE-BRIDGE-1 r2 L3 (SB:167–171; stage 3's directed form of (Sep)): **support off `main`**, under
  the owner exception (`OWNER-EXCEPTION.md`, E1). The planned
  carrier, the extract `SB-L3.md` on #1285's branch (blob `82b5a6a2`), was reviewed at `8177c917`
  (ChatGPT review 5903029353, ACCEPT WITH CHANGES), but it rests on a status note beside it whose
  blob at #1285's head (`7327726d`) has no review covering it. The whole SUBSTATE-BRIDGE-1 file is
  not landed: the owner chose a narrow extract (#868 comment 6874036684, OQ-3), and that file's
  G1 passage is the one #1274 restricts.
- Q-868-H r3 (QH:68–97; the stage-7 illustration at `BELL-LADDER-r3.md`:104): **support off `main`**,
  kept as non-load-bearing context under the owner exception (`OWNER-EXCEPTION.md`, E2). No verdict
  rests on it.
- REC-1 r7 (classification vocabulary): provenance, as r3's table classes it.

## Review and status

- `REVIEW-r1.md` (independent non-author review of r1, ACCEPT WITH CHANGES, C1–C14), `RESPONSE-r1.md`,
  `CONFIRM-r2.md` (of r2 at `b8096c79`, ACCEPT WITH CHANGES, R1–R3 and N1–N4), `RESPONSE-r2.md` and
  `CONFIRM-r3.md` (of r3 at `c4781c93`: ACCEPT, "nothing left to change"). Their line references to
  r1 and r2 are provenance.
- ChatGPT review 5892919040 on #1273 (posted under `amaybaum`, 2026-11-13T14:39:54Z) at `d8e4f80e`:
  "ACCEPT AS A CONDITIONAL PAPER RESULT, with two integration safeguards. Not a native Bell escape,
  OI-wide no-go or merge approval." Owner decisions on NOTES-r3's Q1–Q4: #1273 comment 6860580909
  (`amaybaum`, 2026-11-13): ledger (vii) is a conditional ledger posit; MI\* stays a distinct
  hypothesis; AL's answer is not written into the mixed-path test; the full-history convention
  applies to AL only.
- `BELL-LADDER-r3.md`:3–6 describes the ChatGPT review as pending, and `NOTES-r3.md`:1 labels the notes
  "not for landing"; both are the writer's draft-stage wording, kept byte-identical.
- All reviews are model reviews: evidence of review, not independent mathematical verification.
  r3 is a conditional paper result and is not established (§A.46 items 1 and 7). Stages 0–4 rest on
  designed toy maps that are not OI rules; stage 7 is undetermined.
- Remediation: `OWNER-EXCEPTION.md` states the remaining obligation for L3, QH, the Bell-scope probe
  and the Bell-scope findings, with their accountable Issues. This note authorizes no work.

## Not landed

`BELL-LADDER-r1.md`, `BELL-LADDER-r2.md`, `NOTES-r1.md`, `NOTES-r2.md` and `OBJECTS.md` remain on
#1273's branch. No record on `main` uses them; the review files cite r1 and r2 as review history.
