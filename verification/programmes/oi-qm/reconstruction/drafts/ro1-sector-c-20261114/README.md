# RO-1: sector C specification (#1169), UNREVIEWED drafts

**UNREVIEWED — NOT AUTHORITATIVE.** RO-1 is the paper-only specification of sector C chosen by the
owner (#914 comment 6880010243; #1169 comment 6880022363). Writer: Claude Code; reviewer: ChatGPT
(#914 comment 6881174757). Its first step compares RO-1's scope with #1143 and proposes a split; the
owner decides the split before the specification starts. Nothing here establishes a result, adopts a
premise, or changes any Issue's planning or scope.

| File | What it is | SHA-256 |
| --- | --- | --- |
| `S3-PLAN-r2.md` | S3 plan r2: applies the independent review of r1 (route M kept open with a decisive test; negative controls beyond those on record need separate authorization; U2 and U3 narrowed to avoid overlap with #866, #913 and #914); plan for owner decision; unreviewed | `5be454bf2555b8c3269716ebd78685be024e85334021ddc0b12a61610e09e474` |
| `RESPONSE-S3-PLAN-r1.md` | Dispositions of that review | |
| `S3-PLAN-r1.md` | Paper-only plan for S3, physical executability of embedded-observer operations (accountable to #866 and #913), including the owner-suggested which-path recording route; plan for owner decision; reviewed (REVISE) | `582cb1413f683bfbabda523eaaa49707020f0629b6b3f55ce31037e9d6c19ac4` |
| `RO1-DEPS-r4.md` | Dependency assessment r4: applies the focused review of r3 (C1: interface ceilings and the preparation limit exclude quantum operations only; C2: separated-wing soundness on the finite carrier under global P-vii, at the cost of Bell coverage; X5 flagged); verdict UNDETERMINED; independently reviewed (ACCEPT); accepted by the owner at `549b1056` (#1169 c.6884568026) | `02340bf2fb3d07ef68ad355f8b559723d219890c16feae57d9163b349d71c87e` |
| `RESPONSE-DEPS-r3.md` | Dispositions of that review | |
| `RO1-DEPS-r3.md` | Dependency assessment r3: applies the independent review of r2 (first steps reordered on all four tracks; cross-track conflicts X1–X4 flagged; reuse with retention as the one partial discriminator); verdict UNDETERMINED; reviewed (ACCEPT WITH CHANGES) | `aee284f2d9f51df8a698aff0f08c64f5db922f9495f39fdb31c4bcc76d65451d` |
| `RESPONSE-DEPS-r2.md` | Dispositions of that review | |
| `RO1-DEPS-r2.md` | Dependency assessment r2: applies the independent review of r1 and the reviewer's additions; four tracks; verdict UNDETERMINED; reviewed (REVISE) | `01809afbba839b3fcc6aada8d54ddf17f6c2d463a16568659346d871f1d6545e` |
| `RESPONSE-DEPS-r1.md` | Dispositions of that review | |
| `RO1-DEPS-r1.md` | RO-1 step 2 dependency assessment r1, authorized on #914 (comment 6883931412): premises bearing on sector C; verdict UNDETERMINED; downstream premises listed as remaining; reviewed (REVISE) | `2d3ce3676d50c829d4684e6d0218d8ad6d307f07aa4b3b99d624bb45de593390` |
| `RO1-SPEC-r3.md` | Minimal r3: applies the review of r2 (no prejudging of S5 or S9; O11 answers narrowed to "not excluded"); reviewed (ACCEPT) | `90a4e47ed84eabdeee715525ad81f2e63151078534d390458af77278c7cf8146` |
| `RESPONSE-SPEC-r2.md` | Dispositions of that review | |
| `RO1-SPEC-r2.md` | Sector-C specification r2: applies the independent review of r1 and three reviewer checks (PR countermodel clause by clause, missing restriction, identity-relation analysis); stops S1–S3, S5–S9; reviewed (ACCEPT WITH CHANGES) | `5ea19f790120499b4d6325459f8153d1c5fc831fee07877f4603cc5132fb3528` |
| `RESPONSE-SPEC-r1.md` | Dispositions of that review | |
| `RO1-SPEC-r1.md` | Sector-C specification r1, authorized on #914 (comment 6883249235) after the owner adopted the r3 split; stops at six owner decisions; reviewed (REVISE) | `d7f4380d2c2786a30f68b2d1776f5212ca11750192778e2fed3e2bde7e6a4341` |
| `RO1-OVERLAP-r3.md` | Applies ChatGPT's review of r2 (PR review 5906070407, at `49d90f59`): coverage and soundness kept apart from necessity; necessity recorded as a settled scope decision; unreviewed | `51db9909321586d875c16c7f50c097b493c4ee2fd4cf63ea93324eeadbc34960` |
| `RESPONSE-REVIEW-r2.md` | Dispositions of that review | |
| `RO1-OVERLAP-r2.md` | The comparison in the owner's requested format: one allocation table, the six assessment items, statements labelled as result, proposed obligation or unproved assumption; recommendation not adopted; unreviewed | `d4617d155ee4d8f593ec1bbbf350d72c4016c2fa4008e0803cfd13506848f615` |
| `RO1-OVERLAP-r1.md` | Scope comparison of RO-1 and #1143, with a proposed split and owner questions; proposal for owner decision; unreviewed | `6aa7b08ea6f0f4f9f7d94e43c232e9fa938d50dc97679c8db2e807a10609a501` |
| `REVIEW-SPEC-r1.md` | Independent review of RO1-SPEC-r1 at `7156d761`: REVISE (three blocking, seven major, twelve minor) | `f3e19cf8e78e5832a0ac944e32587146af2462de4de7fc4f8932591feac758cd` |
| `REVIEW-SPEC-r2.md` | Independent review of RO1-SPEC-r2 at `551b2f18`: ACCEPT WITH CHANGES (three new major findings) | `a920b934bce674e32b8a916cc2af815036fb1882838a0b091cd09a4d544ca99f` |
| `REVIEW-SPEC-r3.md` | Focused confirmation of RO1-SPEC-r3 at `a407ff90`: ACCEPT (one nonblocking nit) | `ab6e12ef29d876b0c7f4a85d11fd4429937db839ef03dfd53a8619283fac7db3` |
| `REVIEW-DEPS-r1.md` | Independent review of RO1-DEPS-r1 at `9504385a`: REVISE (verdict label right; four blocking findings on its support) | `8536e21297b527b3294f61cf4f2d300c339c6b513be57b6739c4f7a6bf7f14a1` |
| `REVIEW-DEPS-r2.md` | Independent review of RO1-DEPS-r2 at `3b7d5aac`: REVISE (criteria 1, 3, 4 met; 2 not met: first steps not first on tracks (c), (d) and partly (a); four cross-track conflicts unflagged) | `e3dcd01306596b5892367fd8bf1b9354f348ecc3a23c043bcdf5243fdbbf7cda` |
| `REVIEW-DEPS-r3.md` | Focused review of RO1-DEPS-r3 at `4fc3f4aa`: ACCEPT WITH CHANGES (C1: the interface ceilings and D-A8 exclude quantum behaviour only, not both; C2: D-ceil gives separated-wing soundness on F under global P-vii) | `17a40f1857065bf89f48ecada65040dc18744037d057c873fec595ac5639989f` |
| `REVIEW-DEPS-r4.md` | Focused confirmation of RO1-DEPS-r4 at `dab18525`: ACCEPT (C1 and C2 resolved; two optional nits) | `8622bd2962a2b4663caba48b9f7c76ab206c11b7993acdcc8a50757711b8dd07` |
| `REVIEW-S3-PLAN-r1.md` | Independent review of S3-PLAN-r1 at `38b5a460`: REVISE (route M closed prematurely; negative controls need unauthorized construction; U2 and U3 overlap existing work) | `6e33a05e3fabd3e9ff2daeff35d4b7e9db1dedd6e79467ac04d797363805ba2c` |
