# Recovered #1169 evidence (2026-11-13)

**WIP / UNVERIFIED preservation record, not for merge.** This directory preserves, byte for byte,
research files that existed only in the session storage of one coordinating Claude Code session or
only on a disposable session branch, so that they are not lost when that storage is discarded.
Everything here is **recovered, not accepted**: preservation adopts no premise, promotes no claim
and changes no status (§A.42 item 6; §A.46 item 3). Where a file records an owner acceptance or a
review verdict, that status is quoted below as recorded, and every review named here is a
model-written review, not human verification (§A.46 item 7). No file here is support for an
established claim until it lands on `main` and meets §A.46 item 1.

No recovered script was executed, and no computation on any OI rule was run, to assemble this
directory.

## Authority

Owner record #1169 comment 6852816462 (`amaybaum`, 2026-11-13T12:25:01Z), recording the owner's
decision "Authorize all (Recommended)", item 2, verbatim:

> 2. **Recovery of at-risk evidence:**
>    - the EOI PACKAGE r3 (`33075f9f`);
>    - the Q-C2-2 r14b review;
>    - ASSESS-1059 r6a and ASSESS-868 r3a;
>    - the qc21/qc22 session drafts.
>
>    Each keeps its provenance, and recovered material is labelled as recovered, not as accepted.

The same record lists as not authorized "new experiments, priority changes or merges".

Reporting gate (owner, 2026-11-13, as relayed to this session by the coordinating session; no
GitHub record of it was read here): each item is reported as **FOUND**, **VERIFIED** (hash
matches) and **PRESERVED** (committed and on a remote branch), separately. In the tables below,
PRESERVED reads "pending push" until this branch is on the remote.

The QPHEN review-chain texts (item 6) are not named in item 2. They were added at the coordinating
session's direction after an independent review of #1219 (item 4 of the same record) found that
texts cited by hash in #1219's frozen record exist only in session storage; whether item 2 covers
them is for the owner to confirm.

## Conventions

- **Recorded hash** is a sha256 of the file bytes unless marked otherwise. A recorded prefix (or
  prefix…suffix) matches when the file's sha256 starts (and ends) with it.
- **Original location** is a path relative to the session-storage root of session `57e93868…`,
  unless a commit is named.
- `FILES.tsv` lists every file in this directory with sha256, git blob id, size and original
  location. Every file except the two redacted copies (section "Exclusions and redactions") is
  byte-identical to its original location; this was checked with `cmp` against the source on
  2026-11-13, and every hash was recomputed before committing.
- Full 40-hex ids name objects in this repository; other ids are abbreviated to 8 characters.

## Summary

| Item | Directory | Files | FOUND | VERIFIED | PRESERVED |
|---|---|---|---|---|---|
| 1. EOI PACKAGE r3, inputs and review trail | `eoi-package/` | 16 | yes | yes (full 64-hex) | pending push |
| 2. Q-C2-2 r14b review and its probes | `qc22-r14b-review/` | 11 | yes | yes (`88a4ec2d…1d45`) | pending push |
| 3. ASSESS-1059 r6a, DISPOSITIONS-r6, REVIEW-1059-r6 | `assess-1059/` | 3 | yes | yes (`d08faa81`, `e01e3097`) | pending push |
| 4. ASSESS-868 r3a, REVIEW-868-r3, DISPOSITIONS-r3a, probes | not here: branch `research/q868h-868-20261113`, `drafts/q868h-20261109/assess-868-r3a/` | 28 | yes | yes (`d97c4b6b…`, `2a5014a5…`) | pending push of that branch |
| 5. qc21/qc22 session drafts | `qc-session/` | 573 | yes | no hash recorded; byte-identical to source | pending push |
| 6. QPHEN review chain cited by #1219 | `qphen-review-chain/` | 46 | yes | yes, 46 of 46 against #1219's cited hashes | pending push |
| 7. Local commits `a59a965a` … `d87547a4` | not files: git ref | 4 commits | yes | yes (commit ids) | remote ref present (see item 7) |

Total in this directory: 649 files (23,236,550 bytes) plus this README and `FILES.tsv`.

***

## 1. EOI PACKAGE r3

| Field | Value |
|---|---|
| Recorded hash, where | `33075f9f` (PACKAGE r3): #1169 c.6726546702 and #1208 c.6726546566 (`amaybaum`, 2026-11-08T20:14Z), the owner's designation of `F` for ARP-1-MARC; also #1169 c.6852816462. The full 64-hex value is in ARP-1-MARC's preregistration on `main` (below) |
| Original location | `eoi-audit/PACKAGE.md` (mtime 2026-11-08 15:52 UTC); inputs at `eoi-audit/` and `gate/`. On no branch before this one |
| sha256 / blob | `33075f9f2e4df52cf87536ebcb8c8c931f89960e3a067af30c182587f3109b74` / `8e5808e559cf03fd22b1beb5293902741ba148e4` |
| Status as recorded | The owner's words in c.6726546702: "accept the consolidated audit package (PACKAGE r3, 33075f9f) as the reconciled findings without adopting any correction". Model-written and model-reviewed: r2 reviewed ACCEPT (`REVIEW-PACKAGE-r2.md`); r3 applies that review's non-blocking items |
| Cited on `main` (`c3b5f37a`) | `verification/programmes/oi-qm/reconstruction/round-arp1-marc-20261108/preregistration.md` lines 124 and 885; `.../round-arp1-marc-20261108/evidence/order.json`; `verification/receipts/ARP-1-MARC.json` line 46 |
| FOUND / VERIFIED / PRESERVED | yes / yes / pending push |

Inputs and review trail. PACKAGE r3 records the sha256 of its inputs and earlier revisions; each
matches. The reviews are not hashed in the package.

| File | sha256 | Blob | Size | Matched against |
|---|---|---|---|---|
| `eoi-audit/AUDIT-C1.md` | `8aaa7518b625ae9f7a2cb4c119bdad889eff9f0963cd4f70e95ae1a8dfacec43` | `0f1ada1a` | 50813 | PACKAGE.md:55 |
| `eoi-audit/AUDIT-C2.md` | `54699d91876f203d900fdbdc40f5f4504914f293722d6232b3993f2e38f80d7f` | `4e8b8187` | 52999 | PACKAGE.md:56 |
| `eoi-audit/AUDIT-C3.md` | `d143754b469a5f9eaa90b9b0db5f06d2ec85ffbf946c9f9de855d3a55e40e68b` | `65279e5c` | 45338 | PACKAGE.md:57 (also `main`, preregistration.md:124) |
| `eoi-audit/AUDIT-C5.md` | `65f844f0f6d6403dd57fe1f902519fbdbce40abe68eda87c75e0eb67cf50627c` | `38d77885` | 40019 | PACKAGE.md:58 |
| `eoi-audit/PACKAGE-r1.md` | `c8960f5ca8f060859d7873bea61af37cc98cc525fdc4bacdfa3b04e4a1ec91bd` | `1651bd90` | 35659 | PACKAGE.md:14 |
| `eoi-audit/PACKAGE-r2-DISPOSITIONS.md` | `d91498541660fb26bc197e94dd56258f72c5c6973b505181ca200ec9c8f94834` | `8b42cc02` | 3492 | not hashed in the package |
| `eoi-audit/PACKAGE-r2.md` | `ef0612025c8ef044a4a6550538c956b4f4eed329627e34f194fecb2fabdeeec0` | `7537c5ea` | 48111 | PACKAGE.md:15 |
| `eoi-audit/PACKAGE.md` | `33075f9f2e4df52cf87536ebcb8c8c931f89960e3a067af30c182587f3109b74` | `8e5808e5` | 49831 | the recorded `33075f9f` (full value on `main`) |
| `eoi-audit/REVIEW-C1-r2.md` | `e5f3d630e9b24ed9d887721862666466e3aa96cad820cc1ea0f9fbba5a5b3532` | `42dda6b2` | 7506 | not hashed in the package |
| `eoi-audit/REVIEW-C2-r4.md` | `6dd0599419752a338e9111c969b43e75c4767fc517e7d3db193fd22b3f6ef719` | `72b94c0c` | 4763 | not hashed in the package |
| `eoi-audit/REVIEW-C3-r3.md` | `078c59effe9a5697da69155967ce75d0c0e496946245349087a3ccfba98d018b` | `2ae38264` | 3916 | not hashed in the package |
| `eoi-audit/REVIEW-C5-r2.md` | `8ac466006316968cc30165676a12b326b3021c3c3223984c84afaca636347673` | `5c513f2a` | 5296 | not hashed in the package |
| `eoi-audit/REVIEW-PACKAGE-r2.md` | `688954c56b27ef0c9784b48f38b8ee7563bda131127338c193bf71ae783de4df` | `81dc7c83` | 10610 | not hashed in the package |
| `eoi-audit/REVIEW-PACKAGE.md` | `e6ff56119e3f14614258b4485a3ca7c73c0a1865761f86d606a4a7a3d170761f` | `a796cd47` | 21216 | not hashed in the package |
| `gate/GATE-DRAFT.md` | `a5d42f9216404f587de85759fdb0ee9a84881f681f0f828d34854ecaa7acf936` | `139ec795` | 27095 | PACKAGE.md:59 (cited as `../gate/GATE-DRAFT.md`; layout kept) |
| `gate/REVIEW-GATE-r3.md` | `0c04a119448119106afd19464f62e77d38db660d842c3f4578610ce59ff3fdd7` | `6cfa9ac9` | 9626 | not hashed in the package |

## 2. Q-C2-2 (ARP-3) r14b independent review

| Field | Value |
|---|---|
| Recorded hash, where | `88a4ec2d…1d45`: #1169 c.6793400283 (`amaybaum`, 2026-11-11T10:28:31Z), "it is a session file, not yet published" |
| Original location | `arp/qc22/review/REVIEW-QC22-r14b.md` (mtime 2026-11-11 09:15 UTC), with the review's probes `arp/qc22/review/probes-r14b-rv/` (10 files). On no branch before this one |
| sha256 / blob | `88a4ec2db88b48795f0d7a1740fc383c3fc24031a6adf22578a16f0f3bfd1d45` / `a74c0c1cecb0bf0bd89b087a763263b3df2fe300` |
| Status as recorded | c.6793400283: "a fresh non-author Claude review of preregistration draft r14b (sha256 `e8f5fcfb…`) returned **REVISE** with three blockers"; "Q-C2-2 stays parked. Nothing here authorizes a revision pass, run, freeze, F/E designation or dispatch." Q-C2-2 r14c is listed as parked in c.6852816462 |
| Cited on `main` | nothing |
| FOUND / VERIFIED / PRESERVED | yes / yes / pending push |

The reviewed draft r14b itself is on branch `ccr-9c2ecca4-vkb666` at
`handoff-20261109/qc22/preregistration.draft.md`, and its rebuilt copy is here as
`probes-r14b-rv/r14b.rebuilt.md`.

| File | sha256 | Blob | Size | Matched against |
|---|---|---|---|---|
| `review/REVIEW-QC22-r14b.md` | `88a4ec2db88b48795f0d7a1740fc383c3fc24031a6adf22578a16f0f3bfd1d45` | `a74c0c1c` | 16166 | the recorded `88a4ec2d…1d45` |
| `review/probes-r14b-rv/added.txt` | `0262c4406efecfde30be1d7bf4dd1cc9c84e010f4dfbdc79e7ece95f34558448` | `4c715c18` | 12747 | not hashed in the review |
| `review/probes-r14b-rv/q1.out` | `dbd67e0ae76a049d914fdf520d755ab4bb32718a364891d125e88f1bae4a2154` | `05f674fe` | 83 | not hashed in the review |
| `review/probes-r14b-rv/q1_nof1.py` | `37df9bf22f457c1fc2fd9dff758bb40a831b6851c089a08fdf2323ca233340a2` | `f54c31b7` | 1549 | not hashed in the review |
| `review/probes-r14b-rv/q2_host.out` | `e7b66c3f63fb5673424f01693ba64171fbc32fb88b38e44b21d8b551dc5e0426` | `72ad2c46` | 507 | not hashed in the review |
| `review/probes-r14b-rv/q2_paged_obj.raw` | `3326133f89c08a2ba0c1c193ab936a15ff14a9bd2b39680b2dc40b0085707aaf` | `3b6f710f` | 13181 | redacted copy; original sha256 `d676db8f…`, not hashed in the review |
| `review/probes-r14b-rv/q3_verify_main_ifs.out` | `3b7891f0448ec07aff5099dfeaedb4a0055f8c800fad7fe39a31b5e9b6e534bd` | `c7bdea1d` | 821 | not hashed in the review |
| `review/probes-r14b-rv/q4.out` | `4439e4476ce67e714bc27f04774519a774e3be990e5f842f4556b73c659cc170` | `3153da98` | 30 | not hashed in the review |
| `review/probes-r14b-rv/q4_quotes.py` | `f861b9c2ba77e491d39e8216c8daa18daa9d42c00b776fd6996c39dc117bccce` | `b57f98ef` | 989 | not hashed in the review |
| `review/probes-r14b-rv/r14b.rebuilt.md` | `e8f5fcfb48ed861b3e2a14f37a6d333e37baafaf722130a7931bb756aca9bed9` | `3202d75f` | 204178 | REVIEW-QC22-r14b.md:10, :20 (`e8f5fcfb…`, the reviewed draft r14b) |
| `review/probes-r14b-rv/sheet.rebuilt.md` | `555bf62911dd5e2d71f129d7e289b0590cc0aa376d1cbee7b0900478aca6ced3` | `587caea3` | 22777 | REVIEW-QC22-r14b.md:22 (`555bf629…`) |

## 3. ASSESS-1059 r6a (#1059 Born re-assessment)

| Field | Value |
|---|---|
| Recorded hash, where | `d08faa81` (r6a): #1169 c.6743475622 (`amaybaum`, 2026-11-09T15:09:48Z), session handoff table; and `handoff-20261109/HANDOFF.md` line 21 at `820519cf011c09b37690213a758106ed3aa15cc2`, which also records the review as `e01e3097` |
| Original location | branch `ccr-9c2ecca4-vkb666` at `820519cf011c09b37690213a758106ed3aa15cc2`, `handoff-20261109/1059-assess/` (the three blobs are identical there); session copies at `reassess/1059/` |
| sha256 / blob | `d08faa8174e526f05c085051727ffd53096f688e933977b198b1d66f500da2b8` / `31d0de4698142373aa4b30a9eb6b8d29f459a33a` |
| Status as recorded | c.6743475622: "**Accepted**: r6 review ACCEPT WITH NITS; nits applied (r6a `d08faa81`)", role "Input to the dependency matrix". REVIEW-1059-r6 is a model-written review of r6 (sha256 `ccedea2f…`), not of r6a; the r6 → r6a nit edits have no separate review |
| Cited on `main` | nothing |
| FOUND / VERIFIED / PRESERVED | yes / yes / pending push |

The source branch is a session snapshot whose commit message says "WIP, not for merge"; its
risk is that the branch is disposable.

| File | sha256 | Blob | Size | Matched against |
|---|---|---|---|---|
| `ASSESS-1059.md` | `d08faa8174e526f05c085051727ffd53096f688e933977b198b1d66f500da2b8` | `31d0de46` | 74736 | the recorded `d08faa81` |
| `DISPOSITIONS-r6.md` | `528cd5c39b50f3e8ee79c7f6a41c046439dfa5acce87c0c53a0d4b773f4348fd` | `945ca25d` | 9969 | REVIEW-1059-r6.md:9 (`528cd5c3…48fd`) |
| `review/REVIEW-1059-r6.md` | `e01e309758c0b8f884b11cc92c00891e58bc640a4a2e0605155a04e009c6b017` | `9e44094c` | 12007 | the recorded `e01e3097` (HANDOFF.md; also ASSESS-1059.md:9 in full) |

## 4. ASSESS-868 r3a (#868 joint-systems re-assessment)

Preserved on a separate branch, beside the unit that depends on it: branch
`research/q868h-868-20261113` (draft PR #1269), commit `44f7c328ae38f0ecf8d90f73e5e8b3a4a2d5b2c5`,
directory `verification/programmes/oi-qm/reconstruction/drafts/q868h-20261109/assess-868-r3a/`
(28 files: ASSESS-868 r3a, DISPOSITIONS-r3a, REVIEW-868-r3 and 25 probe files). Its `OBJECTS.md`
carries the hash table, the recorded status and the off-`main` references.

| Field | Value |
|---|---|
| Recorded hash, where | `d97c4b6b…` (r3a) and review `2a5014a5…`: #914 c.6742050590 and #868 c.6742050189 (`amaybaum`, 2026-11-09T14:07Z); #1169 c.6743475622 |
| Original location | branch `ccr-9c2ecca4-vkb666` at `820519cf011c09b37690213a758106ed3aa15cc2`, `handoff-20261109/868-assess/`; session copies at `reassess/868/` |
| sha256 / blob | `d97c4b6b17bea9675d02a697e5164862471dad840dfbe9b54532baacd6788e1b` / `7196beebd6d4c5811132a2bf0fba33386566780b`; review `2a5014a526399437754ecba4a8d8496ead456c33f10483c1b723acd170f0fd1d` / `18681975a022f2bde51c2365da4c4bb11b2529dd` |
| Status as recorded | #868 c.6742050189: "Independent review of r3: ACCEPT WITH NITS (REVIEW-868-r3.md, `2a5014a5…`)", "Nits: applied in r3a (`d97c4b6b…`)", findings "model-written, model-reviewed; not human verification" |
| Cited on `main` | nothing |
| FOUND / VERIFIED / PRESERVED | yes / yes / pending push of `research/q868h-868-20261113` |

## 5. qc21 / qc22 session drafts (Q-C2-1 = ARP-2, Q-C2-2 = ARP-3)

No hash is recorded for this item; "session drafts" is read as the qc21/qc22 working directories
in session storage. VERIFIED here means byte-identical to the source (`cmp`), with the hashes in
`FILES.tsv`.

| Subdirectory | Files | Original location |
|---|---|---|
| `qc-session/arp/qc21/` | 342 | `arp/qc21/`, without `wt-impl/` (a git worktree of this repository; see item 7), `__pycache__/` and `pycc/*.pyc` |
| `qc-session/arp/qc22/` | 210 | `arp/qc22/`, without `__pycache__/`; one file redacted (below) |
| `qc-session/qc21w/` | 8 | `qc21w/` |
| `qc-session/qc21b2/` | 7 | `qc21b2/` (the 2026-11-11 qc21 B2 diagnosis `DIAG-QMP.md` with its self-test outputs) |
| `qc-session/qc21b2r2/` | 4 | `qc21b2r2/` |
| `qc-session/unpushed-d87547a4/` | 2 | git objects: `controls.py` and `qc21_check.py` of `round-arp2-qc21-20261108/` at commit `d87547a4a1ba000b512076a1f3036bcea7fb816b` (blobs `b1d4bea484fbe40d7f84fe4ad8d4fe55d3d6d9d5`, `aa9cd82ed98c6c8239a0e984bbfd172c78320812`) |

Contents: the qc21 preregistration revisions r1–r14b and PLAN/DESIGN-DS r1–r13; qc22 r1–r14a with
ACCESS r1–r13; the review trail (REVIEW-QC21-r14/-r14a/-REACHABLE, REVIEW-ACCESS r1–r13,
REVIEW-QC22-r13-full, REVIEW-QC22-r14b); dispositions; IMPL-DELTA r14/r14a; probes and controls.

| Field | Value |
|---|---|
| Recorded hash, where | none recorded for the item; #1169 c.6852816462 names "the qc21/qc22 session drafts" |
| Status as recorded | WIP / UNVERIFIED drafts. qc21 r14c was reviewed REVISE (minor); the qc21 r14d checkpoint `f634f8e3f2115ef28d11616e0d195221d3ce9cb3` carries an owner decision (#1169 c.6778994857); qc22 r14b was reviewed REVISE (item 2). Q-C2-1 execution and Q-C2-2 r14c are parked (c.6852816462) |
| Already on a branch | qc21 r14c and REVIEW-QC21-r14c, and qc22 r14b, DECISIONS-QC22-preF and REVIEW-QC22-r14a, on `ccr-9c2ecca4-vkb666` under `handoff-20261109/`; qc21 r14d on `research/arp2-qc21-prep-20261109` under `drafts/arp2-qc21/` |
| Cited on `main` | nothing (`main` names ARP-2 only in the ARP-1-MARC preregistration, line 841) |
| FOUND / VERIFIED / PRESERVED | yes / byte-identical to source / pending push |

## 6. QPHEN Phase 1 review chain cited by #1219

PR #1219's frozen record is `verification/programmes/oi-qm/reconstruction/qphen-phase1-20261109/`
on branch `research/qphen-phase1-frozen-20261109`, commit
`4c7f3f86191847592de18de55b364cc8cf591bb3`. It carries the r7c texts, its reviews and probes. Its
reviews cite by hash the earlier revisions r1–r7b, their dispositions and two further files, which
were in session storage only (`qphen/`). Every file below was matched against a hash cited in that
record (the citing file and line on that commit are given); all 46 match.

| File (under `qphen-review-chain/`) | sha256 | Blob | Cited as | Cited at (4c7f3f86) | Match |
|---|---|---|---|---|---|
| `r1/QX3-ANTIBUNCHING-r1.md` | `23775ceb774494cbbe06a6362945d0086d6b674d67ac6963a45572904279602c` | `4492e56b` | full 64-hex | REVIEW-PHASE1-r2.md:38, REVIEW-PHASE1.md:24 | yes |
| `r1/QX4-INCOMPATIBILITY-LG-r1.md` | `6edcf8fa5b0e7a85e075f92c1115823cf8cf1252f86a96fff22e924ae0579899` | `6c0823de` | full 64-hex | REVIEW-PHASE1-r2.md:38, REVIEW-PHASE1.md:25 | yes |
| `r1/QX6-BELL-CHSH-r1.md` | `1534b2c230991e7fcb5c1fedfffbfa38e9a9a05cb934a3155e8f289840fa7178` | `885518b0` | full 64-hex | REVIEW-PHASE1-r2.md:39, REVIEW-PHASE1.md:26 | yes |
| `r1/SHARED-MECHANISM-r1.md` | `5b07a5b9a97152d2e7aa7029c3b9bfb9135dd39657e24453b12e3e1cb4821898` | `7b76a467` | full 64-hex | REVIEW-PHASE1-r2.md:39, REVIEW-PHASE1.md:27 | yes |
| `r2/DISPOSITIONS-r2.md` | `064df364a51fda7f2256705cd9f1978b1eec44152f1c09587d7104bfddf3cb53` | `9cf1591e` | full 64-hex | REVIEW-PHASE1-r2.md:36 | yes |
| `r2/QX3-ANTIBUNCHING.md` | `26ba2167813887e9d6cca63e90667659a88a56365ce21f3ac319b638c8bfe615` | `6aae6e60` | full 64-hex | REVIEW-PHASE1-r2.md:32 | yes |
| `r2/QX4-INCOMPATIBILITY-LG.md` | `47fb4202049efb49a8cd9c471632d06aba74866e4b80f895ab0512c1cd45f975` | `f6f61307` | full 64-hex | REVIEW-PHASE1-r2.md:33 | yes |
| `r2/QX6-BELL-CHSH.md` | `9d68526ce41cd8fedf249fd3d4e377ef54f6de4679a6b884fcd6a9fe1805a875` | `6768b924` | full 64-hex | REVIEW-PHASE1-r2.md:34 | yes |
| `r2/SHARED-MECHANISM.md` | `7d10092a5c860123ab6902feeed1857ec07e8613b3b5e714478e0d959f408553` | `cfa62945` | full 64-hex | REVIEW-PHASE1-r2.md:35 | yes |
| `r3/DISPOSITIONS-r3.md` | `711bfda011a1bd9c78f9ffa0ea9980eca5869a7ea7f7bc5bd5033a56d3c63ebc` | `b4dc5a0b` | `711bfda011a1bd9c` | REVIEW-PHASE1-r3.md:15, REVIEW-PHASE1-r4.md:205 | yes |
| `r3/QX3-ANTIBUNCHING.md` | `4ea39322ec363331653ae79d9623ac5be5548d8a11147e0be0545535109718de` | `02ec3ec1` | `4ea39322ec363331` | REVIEW-PHASE1-r3.md:11 | yes |
| `r3/QX4-INCOMPATIBILITY-LG.md` | `866a6f2aeae4e3946b61a2ded9bf043689c0843c709b86e6099e8cc6e70badd6` | `51f3be29` | `866a6f2aeae4e394` | REVIEW-PHASE1-r3.md:12 | yes |
| `r3/QX6-BELL-CHSH.md` | `04882cc25af134768257aa4fa6c83412ecd79868010d3be938f50f1c9cb07c69` | `0ad65ee9` | `04882cc25af13476` | REVIEW-PHASE1-r3.md:13 | yes |
| `r3/SHARED-MECHANISM.md` | `6537031aa829965218bbd1424d5342917674d64683defafa97c74b64845280fd` | `fa71799a` | `6537031aa8299652` | REVIEW-PHASE1-r3.md:14 | yes |
| `r4/DISPOSITIONS-r4.md` | `a886e40d0311849b19480ef954e17cc1b50b2b0e804486af8c44ee95f1c67c5d` | `2e3d0343` | `a886e40d0311849b` | REVIEW-PHASE1-r4.md:15 | yes |
| `r4/QX3-ANTIBUNCHING.md` | `f372cef7d3baad57cb4cddd72a710bb1077a1235299fd34283fb5ca29b6c5282` | `27b23f19` | `f372cef7d3baad57` | REVIEW-PHASE1-r4.md:11 | yes |
| `r4/QX4-INCOMPATIBILITY-LG.md` | `2765e6f7cb06e4d6bbd60645616abd70588ca8b739235181845fed3cde6f97c4` | `67d8b847` | `2765e6f7cb06e4d6` | REVIEW-PHASE1-r4.md:12 | yes |
| `r4/QX6-BELL-CHSH.md` | `5c7ab0cb6efce8e33b23daad29fd20076e6cceeb1fe83d54e11b68c6d6ef774a` | `5cad079c` | `5c7ab0cb6efce8e3` | REVIEW-PHASE1-r4.md:13 | yes |
| `r4/SHARED-MECHANISM.md` | `23ec1ef19be8b2dd4aa77d59926853fd00a125ee552746db14d83203b366fd11` | `68366f2a` | `23ec1ef19be8b2dd` | REVIEW-PHASE1-r4.md:14 | yes |
| `r5/DISPOSITIONS-r5.md` | `01ef37655352c0d8dc0cdaf4512fee1df74ec5183267dd1982177addacbaa28c` | `3de5bb12` | `01ef37655352c0d8` | REVIEW-PHASE1-r5.md:15 | yes |
| `r5/QX3-ANTIBUNCHING.md` | `e231a795508769cec7645f05931b1ce04e418bbd69acd8802f794a0bec8add71` | `24200e66` | `e231a795508769ce` | REVIEW-PHASE1-r5.md:11 | yes |
| `r5/QX4-INCOMPATIBILITY-LG.md` | `7f4cd21d02a0dbf7946c4d481c6140f7e3c6df053a5096b8fd589de123a7b5a5` | `fdbc06d4` | `7f4cd21d02a0dbf7` | REVIEW-PHASE1-r5.md:12 | yes |
| `r5/QX6-BELL-CHSH.md` | `9e9c0d02c48dfc748baa7fade7a271c938e8ae817457ec635a3076cec774e4ea` | `b198471d` | `9e9c0d02c48dfc74` | REVIEW-PHASE1-r5.md:13 | yes |
| `r5/SHARED-MECHANISM.md` | `a72067015789371a087517d92f71a5fcc654770d1d3f105e217eda6fcba2cc4d` | `fcd02b6c` | `a72067015789371a` | REVIEW-PHASE1-r5.md:14 | yes |
| `r6/DISPOSITIONS-r6.md` | `468d188d56f7506627d637801d731c8c29f890ecf87580e60363d75b56e536a7` | `7f09bfac` | `468d188d56f75066` | REVIEW-PHASE1-r6.md:16 | yes |
| `r6/QX3-ANTIBUNCHING.md` | `01f8a44d64334d01923ee6c499dd4f59df9be341c0035148573e35bcd6e421da` | `b4ba5785` | `01f8a44d64334d01` | REVIEW-PHASE1-r6.md:12 | yes |
| `r6/QX4-INCOMPATIBILITY-LG.md` | `df4def7192b7d8226eb339330fc764a91a2ec062d42aa58748e24afae6647e0e` | `03807b47` | `df4def7192b7d822` | REVIEW-PHASE1-r6.md:13 | yes |
| `r6/QX6-BELL-CHSH.md` | `1243cea4e052a48730969f9a6f2f161ea67754a502088af396fa2ac78a9d2874` | `096bd145` | `1243cea4e052a487` | REVIEW-PHASE1-r6.md:14 | yes |
| `r6/SHARED-MECHANISM.md` | `67b3f5b54f25fdba3f65dedb9346c892d8833223711b8edb03f8352c2ea66327` | `a9e57588` | `67b3f5b54f25fdba` | REVIEW-PHASE1-r6.md:15 | yes |
| `r7/DISPOSITIONS-r7.md` | `98e17956d0dc7bfe0f98d0bccc59225d29c380de2773d91a51a9882dff854458` | `25b6ec3e` | `98e17956d0dc7bfe` | REVIEW-PHASE1-r7.md:16 | yes |
| `r7/QX3-ANTIBUNCHING.md` | `b6effd8a8a7364648c70250cc7258e2531a1317913eb109870837af1ee059b90` | `d73b4a92` | `b6effd8a8a736464` | REVIEW-PHASE1-r7.md:12 | yes |
| `r7/QX4-INCOMPATIBILITY-LG.md` | `6497d64efae0cedacd2ebc7e316c22c6797d0f798dd326dc34a5d47b295a0627` | `a8311223` | `6497d64efae0ceda` | REVIEW-PHASE1-r7.md:13 | yes |
| `r7/QX6-BELL-CHSH.md` | `33b01deb08aec45f6f3da18a6005ff86f9c244fe87fcd8bc265b562bdaeaaa3c` | `020e3468` | `33b01deb08aec45f` | REVIEW-PHASE1-r7.md:14 | yes |
| `r7/SHARED-MECHANISM.md` | `1aad26d1c5db83962c918ba76106d8548cc815c3fa66dfa982b589615131331a` | `d31c4703` | `1aad26d1c5db8396` | REVIEW-PHASE1-r7.md:15 | yes |
| `r7a/DISPOSITIONS-r7a.md` | `417932eed82889e554d3a3c1c889b6d36d4d59b8333b51574a860edeb25c1644` | `8d5d0ea3` | `417932eed82889e5` | REVIEW-PHASE1-r7a.md:16 | yes |
| `r7a/QX3-ANTIBUNCHING.md` | `baf3de3cc5807a36a3ee265ddf178c3aa23b0028050de5ecaabbb75929e2f024` | `45e38e8c` | full 64-hex | CHECK-r7b-independent.md:13, REVIEW-PHASE1-r7a.md:12 | yes |
| `r7a/QX4-INCOMPATIBILITY-LG.md` | `6b45c062bb5a6b1cbf7dabcaf15a8531d21e089f40b3bee9132a4b40ff7c1248` | `ec57a832` | full 64-hex | CHECK-r7b-independent.md:14, REVIEW-PHASE1-r7a.md:13 | yes |
| `r7a/QX6-BELL-CHSH.md` | `b77f0984a282603bb6ee2af3941d6bbe3f4fa696b220272329a241affbaa83fc` | `182f8ea2` | full 64-hex | CHECK-r7b-independent.md:15, REVIEW-PHASE1-r7a.md:14 | yes |
| `r7a/SHARED-MECHANISM.md` | `ab69695e33e7e805d4cf49cb3704807ba77637f5feba9c257a0c57ce30dce3e5` | `910d1bb2` | full 64-hex | CHECK-r7b-independent.md:16, REVIEW-PHASE1-r7a.md:15 | yes |
| `r7b/DISPOSITIONS-r7b.md` | `0080ac328cb38085e99fa8f38ccbe1aec18f732298c8acaaea9b6a153abaddcf` | `818b470f` | full 64-hex | CHECK-r7b-independent.md:21, CHECK-r7c.md:25 | yes |
| `r7b/QX3-ANTIBUNCHING.md` | `4a686c6deb9e051a5e04f01bc3f28484c663dcfee0b19794b807e291bcdcd8f9` | `ee055a28` | full 64-hex | CHECK-r7b-independent.md:17, CHECK-r7c.md:14 | yes |
| `r7b/QX4-INCOMPATIBILITY-LG.md` | `cafdd3210f3d295bc88aef252d503cc80b1e2492a5eaa40d86162534e375587e` | `0dc01999` | full 64-hex | CHECK-r7b-independent.md:18, CHECK-r7c.md:15 | yes |
| `r7b/QX6-BELL-CHSH.md` | `f915ab8892de5e2fd2e4016f3133af00d5aaa156958e4848fc7023fac653000c` | `a0bf458d` | full 64-hex | CHECK-r7b-independent.md:19, CHECK-r7c.md:16 | yes |
| `r7b/SHARED-MECHANISM.md` | `4c26576a269ef38c73dd3ae3a8ec5a95f03ee5ca0bf531dbb4644dcfea21fc72` | `2f8c9f25` | full 64-hex | CHECK-r7b-independent.md:20, CHECK-r7c.md:17 | yes |
| `R4-REVIEW-ADDENDA.txt` | `7aa1b1addfb21024b92654f24371ad7359bd955582d4a3cc614750f32935efec` | `7882f8a0` | `7aa1b1ad` | REVIEW-PHASE1-r4.md:18 | yes |
| `review/REVIEW-PHASE1-r4.md` | `755c3af0ae603b0ebeb06d5853c80357aba50a3634d152c66456e62e2f86a987` | `d41cac2c` | `755c3af0` | QX4-INCOMPATIBILITY-LG.md:424, REVIEW-PHASE1-r5.md:17, SHARED-MECHANISM.md:292 | yes |

`review/REVIEW-PHASE1-r4.md` here is the session original. The copy on the #1219 branch has one
phrase changed (a session-local path replaced), so its hash differs from the `755c3af0…` that
QX4-INCOMPATIBILITY-LG.md:424, SHARED-MECHANISM.md:292 and REVIEW-PHASE1-r5.md:17 on that branch,
and ASSESS-868 r3a §2, cite. `R4-REVIEW-ADDENDA.txt` is the reviewer brief addendum that
REVIEW-PHASE1-r4.md:18 hashes.

Status as recorded: the QPHEN Phase 1 design was frozen by the owner at r7c (#1210 c.6743200254,
as quoted in the #1219 commit message); r1–r7b are the superseded revisions its reviews examined.
Each review in the chain is model-written. Cited on `main`: nothing. FOUND yes; VERIFIED yes
(46 of 46); PRESERVED pending push.

Not found, or not included:

- **`DISPOSITIONS-r7c.md` at `856fa01d7010855a…`**, the version CHECK-r7c.md:22 verified, is
  **not found**. The `DISPOSITIONS-r7c.md` on the #1219 branch and in session storage is
  `d3adc823…`; it cites CHECK-r7c's own hash (`ab7ae723…`) in its last paragraph, so it was
  edited after that check. No file with sha256 `856fa01d…` was found in session storage
  (sha256 of all 454,718 files under 3 MB in the 267 session-storage directories, excluding `.git`, `.lake` and `__pycache__`), and no prefix of the current file has that hash.
- Not included, with reason: the top-level session copies `DISPOSITIONS-r2.md` … `-r7b.md`
  (byte-identical to the copies under `r2/` … `r7b/`); `main_fd.md` and `review/corpus/Main.md`
  (byte-identical to `papers/Main.md` at `fd539e150759a6ea51ab279aeeac80fc06050ade`, which is on
  `main`); the other `review/corpus/` extracts, `review/CHECK-r7b-diff.md`, `review/rerun/` and the
  session original of `review/REVIEW-PHASE1.md` (`8d704712…`; one phrase differs from the #1219
  copy), none of which #1219's record cites by hash.

## 7. Local commits `a59a965a` … `d87547a4` (Task C)

The qc21 implementation worktree (session `arp/qc21/wt-impl`, git directory
`.git/worktrees/wt-impl1`) is clean and detached at `d87547a4`. That commit and three ancestors
exist in the local object store and were on no remote ref when the recovery manifest was written:

| Commit | Parent | Date | Subject |
|---|---|---|---|
| `a59a965a9d13e780837b3de34b68d5d02aa3d85b` | `fd539e150759a6ea51ab279aeeac80fc06050ade` (on `main`) | 2026-11-09 09:14:30Z | WIP / UNVERIFIED: ARP-2-QC21 scripts (local bookkeeping, unpushed) |
| `3983d4cb12bd6c6c57a4b77837e6ba8b07998f90` | `a59a965a` | 2026-11-09 09:16:21Z | WIP / UNVERIFIED: ARP-2-QC21 scripts with the r12 STAB hook (local, unpushed) |
| `96217697ac85fbe623b141ec9fdb74de25ca311d` | `3983d4cb` | 2026-11-09 09:19:16Z | WIP / UNVERIFIED: r12a STAB-TRUE, STAB-FALSE, C-IFACE STAB rule (local, unpushed) |
| `d87547a4a1ba000b512076a1f3036bcea7fb816b` | `96217697` | 2026-11-09 09:19:59Z | WIP / UNVERIFIED: C-IFACE STAB rule matches the whole word (local, unpushed) |

They are preserved by the ref `research/recovered-qc21-local-d87547a4` pointing at `d87547a4`,
pushed by the coordinating session; the commits themselves are not modified. `git ls-remote` on
2026-11-13 showed that ref on the remote at `d87547a4a1ba000b512076a1f3036bcea7fb816b`. Their two
script files at `d87547a4` are also under `qc-session/unpushed-d87547a4/`. FOUND yes; VERIFIED yes
(commit ids); PRESERVED yes (remote ref present). The worktree must not be pruned (§A.40).

***

## Exclusions and redactions

- **Compiled Python.** All `.pyc` files and `__pycache__/` directories: `arp/qc21/pycc/0.pyc` …
  `11.pyc` (12 files) and the `__pycache__/` directories of `arp/qc21/` and `arp/qc22/`.
- **Worktree.** `arp/qc21/wt-impl/`, a git worktree of this repository; its unpushed commits are
  item 7.
- **Redaction (§A.42 item 4).** `probes-r14b-rv/q2_paged_obj.raw`, a raw GitHub Actions API
  response saved by the r14b reviewer, carries a GitHub noreply e-mail address twice on line 1.
  Both copies (`qc22-r14b-review/review/probes-r14b-rv/` and
  `qc-session/arp/qc22/review/probes-r14b-rv/`) are stored redacted: each occurrence of the address
  is replaced by `[redacted-email]`, and no other byte changes.

  | | sha256 | Size |
  |---|---|---|
  | original (not committed) | `d676db8f5419d2116d77fa6de08e3126fc943c3ee035e6e924f61dcdc097951c` | 13215 |
  | redacted (committed, both paths; blob `3b6f710feedee44758f2d834df015c01910cc2d3`) | `3326133f89c08a2ba0c1c193ab936a15ff14a9bd2b39680b2dc40b0085707aaf` | 13181 |

  The file also carries run ids, node ids and branch names, which were kept.
- **Archive.** `qc-session/arp/qc22/review/probes-full/artifact-dl/a.zip` (933 bytes, sha256
  `1ecf12cb918bb886b260ad1b7c22f85733f751bf5821986163f95da2b360b3ec`, blob
  `66dfecec344c77e001b16f53599c13693d2b4646`) is included. Its listing (`unzip -l`; not extracted)
  holds one member, `measurements.json` (2983 bytes, 2026-11-09 05:06, sha256 `77e2254d…`), a JSON
  object with schema `arp1-marc-measurements` version 1: counts and flags only, no code.
- **Scan.** All files were scanned for tokens, keys, signed URLs, IPv4 and e-mail addresses after
  redaction; the only remaining matches are the two code false positives listed below.

## Known SC-42 hits (bytes preserved unchanged)

The SC-42 integration check's added-text scan (`check_sc42_integration.py`, `*.md` and `*.py`)
flags the lines below. The local-path hits name session-storage paths or the session-storage
directory word; the two secret-pattern hits are code (a matrix product with the `@` operator and `np.linalg.inv`, and the
regular-expression source of a copy of the SC-42 check), not secrets. The bytes are preserved
unchanged; 82 hits in 49 files.

| File | Lines |
|---|---|
| `assess-1059/ASSESS-1059.md` | local path at lines 57, 58, 61, 62, 64, 65, 66, 68, 69, 638 |
| `eoi-package/eoi-audit/PACKAGE-r2.md` | local path at lines 394, 399 |
| `eoi-package/eoi-audit/PACKAGE.md` | local path at lines 409, 414 |
| `eoi-package/eoi-audit/REVIEW-PACKAGE.md` | local path at line 106 |
| `eoi-package/gate/GATE-DRAFT.md` | local path at line 234 |
| `eoi-package/gate/REVIEW-GATE-r3.md` | local path at line 6 |
| `qc-session/arp/qc21/DISPOSITIONS-r14a.md` | local path at line 53 |
| `qc-session/arp/qc21/preregistration.draft.md` | local path at lines 665, 1814 |
| `qc-session/arp/qc21/r10/preregistration-r10.draft.md` | local path at lines 362, 1088 |
| `qc-session/arp/qc21/r10parts/appendixC.md` | local path at line 3 |
| `qc-session/arp/qc21/r10parts/c_head.md` | local path at line 3 |
| `qc-session/arp/qc21/r11/preregistration-r11.draft.md` | local path at lines 381, 1259 |
| `qc-session/arp/qc21/r11a/preregistration-r11a.draft.md` | local path at lines 383, 1281 |
| `qc-session/arp/qc21/r11b/preregistration-r11b.draft.md` | local path at lines 385, 1283 |
| `qc-session/arp/qc21/r11parts/appendixC.md` | local path at line 3 |
| `qc-session/arp/qc21/r11parts/c_head.md` | local path at line 3 |
| `qc-session/arp/qc21/r12/preregistration-r12.draft.md` | local path at lines 389, 1310 |
| `qc-session/arp/qc21/r12a/preregistration-r12a.draft.md` | local path at lines 390, 1311 |
| `qc-session/arp/qc21/r13/preregistration-r13.draft.md` | local path at lines 579, 1554 |
| `qc-session/arp/qc21/r13a/preregistration.draft.md` | local path at lines 610, 1585 |
| `qc-session/arp/qc21/r14/preregistration.draft.md` | local path at lines 642, 1655 |
| `qc-session/arp/qc21/r14a/DISPOSITIONS-r14a.md` | local path at line 53 |
| `qc-session/arp/qc21/r14a/preregistration.draft.md` | local path at lines 652, 1715 |
| `qc-session/arp/qc21/r14awork/make_r14a.py` | local path at line 6 |
| `qc-session/arp/qc21/r14b/preregistration.draft.md` | local path at lines 659, 1767 |
| `qc-session/arp/qc21/r14bwork/make_impl_r14b.py` | local path at line 4 |
| `qc-session/arp/qc21/r14bwork/make_r14b.py` | local path at lines 8, 59, 60 |
| `qc-session/arp/qc21/r14c/preregistration.draft.md` | local path at lines 665, 1814 |
| `qc-session/arp/qc21/r14cwork/make_r14c.py` | local path at line 10 |
| `qc-session/arp/qc21/r14cwork/preregistration.r14c.md` | local path at lines 665, 1814 |
| `qc-session/arp/qc21/r14work/make_r14.py` | local path at line 5 |
| `qc-session/arp/qc21/review/REVIEW-QC21-r14.md` | local path at line 132 |
| `qc-session/arp/qc21/review/REVIEW-QC21-r14a.md` | local path at line 103 |
| `qc-session/arp/qc21/review/REVIEW-REACHABLE.md` | local path at line 3 |
| `qc-session/arp/qc21/review/probes-r11/prereg_appC.md` | local path at line 3 |
| `qc-session/arp/qc21/review/probes-r11/run/build_c_local.py` | local path at line 2 |
| `qc-session/arp/qc21/review/probes-r14/make_r14_redirected.py` | local path at line 5 |
| `qc-session/arp/qc21/review/probes-r14/rebuild-r14.md` | local path at lines 642, 1655 |
| `qc-session/arp/qc21/review/probes-r14a/make_r14a_redirected.py` | local path at lines 6, 596 |
| `qc-session/arp/qc21/review/probes-r14a/rebuild-r14a.md` | local path at lines 652, 1715 |
| `qc-session/arp/qc21/review/probes-r14b/rebuild-r14b.md` | local path at lines 659, 1767 |
| `qc-session/arp/qc21/review/probes-r14c/base/preregistration.draft.md` | local path at lines 659, 1767 |
| `qc-session/arp/qc21/review/probes-r14c/make_r14c.rebased.py` | local path at line 10 |
| `qc-session/arp/qc21/review/probes-r14c/rebuild-r14c.md` | local path at lines 665, 1814 |
| `qc-session/arp/qc21/review/proofs/search_k1_candidates.py` | secret pattern at line 40 |
| `qc-session/arp/qc21/sc42.main.py` | secret pattern at line 310 |
| `qc-session/arp/qc22/IMPL-DELTA-r14.md` | local path at line 10 |
| `qc-session/arp/qc22/r14/IMPL-DELTA-r14.md` | local path at line 10 |
| `qphen-review-chain/review/REVIEW-PHASE1-r4.md` | local path at line 20 |

## Known claims_check hit (bytes preserved unchanged)

`tools/claims_check.py` flags one paragraph of a preserved file:
`eoi-package/eoi-audit/AUDIT-C5.md` line 149, rule "GR: thermality asserted purely kinematic
(H-balance)". The paragraph is an audit's classification of manuscript sites; the matched words
are its description of a reading it rejects, not an assertion. The bytes are preserved unchanged.
The check's exemption list (`EXEMPTIONS` in `tools/claims_check.py`) is not changed here; an
exemption for this paragraph would need its own owner decision.

## References these files make to content not on `main` (§A.42 item 8)

These are recovered records, not claims; nothing here is offered as support for a claim on
`main`. The references the files make were not each traced. Known classes:

- Session-storage companions cited by path or hash: the ASSESS files cite `bridge/` and `qphen/`
  files (the cited QPHEN r5 texts are now in `qphen-review-chain/r5/`; the BRIDGE-UNIT1 files are
  on `ccr-9c2ecca4-vkb666` under `handoff-20261109/1211-bridge/`); REVIEW-QC22-r14b cites its
  probes (here); the EOI package cites its inputs (here) and is classified on `main`
  (preregistration.md:124) as provenance with its inputs "none of them on `main`".
- Commits off `main`: `820519cf` (session snapshot), `4c7f3f86` (#1219), `f634f8e3` (qc21 r14d),
  and `d87547a4` with its ancestors (item 7).
- Issues, comments and pull requests (#868, #914, #1059, #1169, #1208, #1210, #1219 and others),
  cited as authorization, status or planning records.

Each must be traced and classified before any of these files is used as support for a claim
(§A.42 item 8; §A.46 item 7).
