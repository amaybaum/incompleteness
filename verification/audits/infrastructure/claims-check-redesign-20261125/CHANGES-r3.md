# Changes in revision r3 (Issue #1565, PR #1567)

This note maps the r2 delta review's findings F1–F7 and the owner's r3 items to `DESIGN-r3.md`, and
justifies each removed or kept mechanism by the owner's three questions:
(1) what concrete failure it prevents;
(2) why an existing mechanism cannot prevent that failure;
(3) whether a simpler solution provides equivalent protection.

The r2 files (`DESIGN.md`, `DESIGN-r2.md`, `CHANGES-r2.md`, `results/`, and the r2 work files) are
unchanged. `work/licences.json` is r2's deployed file, kept so that r2 still reproduces. r3's
deployed file is `work/licences-r3.json`.

## Plain statement

The simpler architecture gives stronger protection against silent misses, and r3 adopts it.

- **Silent misses on every preserved control and probe:** r3 0; r2 9 on batch Y and 3 on the Y
  probes (deployed licences).
- **Corpus injection:** r3 has no silent pass in 1,115,046 results; r2 has 82,572.
- **The cost is review load.** At tree M, r3 gives 248 active REVIEW findings (211 distinct
  sentences, 155 distinct texts) against r2's 3, and 248 records are needed before the gate can be
  green. On the controls, 74 of 76 negatives need a record.
- **Residual.** Paraphrases outside the frozen lexicons still pass. Seven of the author's twelve
  post-hoc diagnostics pass under both r2 and r3.
- **Held-out status.** Batch Y is not held out for r3. A further independent batch is required
  (criterion 6).

## Review findings

| Finding | Disposition | Where |
|---|---|---|
| F1 G3 is adjacency, not qualification | Resolved by removal. No qualifier yields PASS, and G3 does not exist. A `negated` record on a polarity-flipped or concessive sentence is refused mechanically. Z-01..Z-07, Y-P-03 and Y-P-06 are REVIEW. | §3.3–3.6 R5; §6.2 |
| F2 records accept `governed` on an unlicensed hypothesis | Resolved mechanically. `governed` needs a cited, validated, owner-adopted licence entry, and the list is empty. `unrelated` evidence may not contain a qualifier token. Exit-code controls: H-slope `governed` (3), absent licence id (3), qualifier as evidence (3). | §3.6 R4–R5; §6.3 |
| F3 one-directional near-miss scan, suppressed by negators | Resolved by removal. Co-occurrence is order-free and negation-blind. Y-P-01, -07, -09, -10, -18, -19 and -20 and Z-08..Z-10 are REVIEW. | §3.3; §6.1–6.2 |
| F4 false-positive FAILs (Y-N-14, Y-N-16) | Resolved. FAIL needs a bare template in an otherwise clean unit, and both are REVIEW. No FPFAIL on any control or at tree M. | §3.4 |
| F5 copular code mismatch | Resolved. `code` is its own field and is matched exactly. Control "record with a wrong code" gives 3. | §3.6, §3.8 |
| F6 checks skipped without `--repo`; proposer and record path unchecked | Resolved. Records or licence entries without `--repo` give exit 3. Proposer is required. The review record path must exist on the main ref. | §3.6 R1, §3.7; §6.3 |
| F7 M2 did not mutate fronted or restrictor markers | Resolved. M2 adds the colon lead-in and `Under X,` positions: 14,080 insertions, 0 PASS. | §6.4 |
| Earlier R1–R12 | As in r2, except that the governance-related items (R1 G3, R2 frames, R4, R10 near-miss) no longer apply: the mechanisms they tested are removed. | — |

## Owner items

| Item | Disposition |
|---|---|
| Ambiguous claims require review rather than silently pass | Every sentence that touches a rule's vocabulary is REVIEW unless it is a bare FAIL. All 39 ambiguous controls are REVIEW. |
| Licensing enforced mechanically, including in review records | §3.6 R4, R5 and §3.7. The checker never decides licensing, and records cannot assert it without an adopted entry. |
| Negated hypotheses and misleading qualifying phrases must not license | No phrase licenses anything automatically. Records resting on a qualifier, a double negation or a concessive flip are refused. |
| Preserve all previous independent controls | X and Y are byte-identical (hashes below). The r1 and Y probes are preserved. |
| Reassess the architecture rather than accumulate patterns | The architecture is replaced. One mechanism was added after measurement (code P, below), and it reuses existing checker patterns. |
| Simplification: detection → review, with no automated hypothesis licensing | Adopted (§1, §3.5). |
| "Converge; do not add mechanisms where existing ones suffice" (2026-11-25T16:29:44Z) | Safe-PASS forms rejected (§3.4). No further mechanism added after code P. |

## Mechanisms: removed, kept, added

| Mechanism | Decision | (1) Failure prevented | (2) Why existing ones cannot | (3) Simpler equivalent? |
|---|---|---|---|---|
| G1–G3 governance positions, frame lexicons, R3/R5/R6/R7 codes, near-miss N1 | **Removed** | They prevented false FAILs on governed prose, a load cost rather than a miss, and they caused silent misses (F1, F3). | — | Yes: REVIEW plus a record gives the same outcome for correct prose, with no silent-pass route. |
| Licence-driven automated PASS and the fixture licence configuration | **Removed** | The same as above. | — | Yes: a `governed` record citing an adopted licence. |
| Clause segmentation | **Removed** | Only governance used it. | — | Not needed. |
| Exit codes 0–4, precedence, active-material scope | **Kept** | A confirmed violation, an unresolved review and a bad configuration are reported distinctly, and frozen records do not block. | — | No. |
| Review-record binding (sentence hash, full revision, ancestry, window hash) | **Kept**, extended to code A | A stale or retroactive acceptance. | — | No. |
| FAIL floor (bare template, clean unit) | **Kept, narrowed** | A record cannot wave through the plain canonical assertion (R2). | Records' basis checks bound claims, but they cannot prove a reviewer right. | All-REVIEW would lose the floor. |
| Risk lexicon | **Kept** (FAIL→REVIEW only) | False-positive FAIL (F4). | The bare template alone FAILs "It is well known that X" variants and negated frames. | It only lowers FAIL to REVIEW, so it cannot cause a miss. |
| Co-occurrence detection (code C) | **New core** | Silent misses through governance misreadings (F1, F3). | r2's governance passed them. | This *is* the simpler mechanism. |
| Anaphora (code A), previous unit only | **Kept** from r2's R1, narrowed | A pronoun subject with its antecedent in the prior sentence (A-TQ-1, H-A-3, Y-A-02). | C needs the subject in the unit. | A whole-paragraph window costs about 4× the load. |
| Strong cue (code P) | **Added after measurement** | D-03 and D-07 regressions against r2. | C and A need the subject in reach. | A wider A window costs much more load. Code P reuses existing checker patterns and adds 0 active REVIEWs at tree M. |
| Record bases with mechanical checks (R5) | **New** | `unrelated` used as a back door for a qualified or negated-qualifier assertion (F2 variant). | Binding alone does not constrain the decision. | Forbidding `unrelated` would make negations and questions unresolvable. |
| Licence `id`, `proposer`, `adoption`, review-record existence | **Extended** | An unadopted or self-reviewed licence used by a record (F2, F6). | r2 validated licences but records never cited them. | No. |
| Safe-PASS forms (negation in the slot) | **Rejected** | It would save at most 6 reviews at tree M. | — | REVIEW plus a record. The form would reintroduce the governance class (the ellipsis "X does not Y; X does."). |

## First-run record

- **The first complete r3 run** (wide lexicon): one MISS, P-KDEG-3, a subject omitted from the
  inventory; repaired. No other MISS or FPFAIL in any file, including batch Y (not held out).
- **Lexicon narrowed for load** (1,427 → 248 active findings), with every control and probe re-run
  at each step and no MISS introduced. The author diagnostics then exposed D-03 and D-07, and code P
  was added.
- **No control was edited.**

## Files (SHA-256)

Paths are relative to the audit directory (this note excluded).

```
cac365f00bda62a2f55535ce651a7cd7f818e199307e2fcfef944290214eaddf  ./CHANGES-r2.md
25af5534c0d3ff04526b8f73e92c0b65003c26f02ea939a4151cf0780860f240  ./DESIGN-r2.md
cfaf0bb0837c99e83086f3805eef3324b19af3680362eadc31cbee5db53b7dac  ./DESIGN-r3.md
f1ea30f0cc16bf6a30ed26502760f7451d18e3de90ab549f82b0155967581226  ./DESIGN.md
686920cac2ccaf17892a67abfcf40b1d7a8df1baeaad99bbec97c8a4c6ffee73  ./results-r3/author-diagnostics.txt
c7d908db9e67c058df9aad7005efe02f8477b6e3e499c122a6ced65aa36a3611  ./results-r3/compare.txt
a5237d0109b526414af7436b3b5e773e52299f6b0c8492f33790bb2825be5a12  ./results-r3/exitcodes.txt
d35cfe583491be288a2379223682f021a96f956e932d6615e50be772518def51  ./results-r3/injection-r2.txt
02ff8608a7d6e08b3447774f13eb0e36911f19508cd7aa55e264fb0f1cd5cf0c  ./results-r3/injection-r3.txt
28f678c7010b7d1ad301d13c0cc2846b73e541d1ead2cf217609d0432c1ef703  ./results-r3/m1.txt
a5a025cf6d22e76988a08ce9160cc90adc635149a293d672d3aeeff2018d755d  ./results-r3/m2.txt
51081ba634c5453398c6ac9f6f518f1e8a88eeb5c768b6efcfc186872372db8f  ./results-r3/r3-firstrun-controls.txt
5d7c463028d7e7d69d2e181f69e2c2b1afd374e4051fbbf95db84f5404763633  ./results-r3/r3-firstrun-controls_c.txt
7d999be2f5de2752705ad7bddae7b6105b9873ee1167dfc76ff12912ac6b3e37  ./results-r3/r3-firstrun-controls_d.txt
e64e006a4c380741a76981371cb79c1b2e841c545416519437fb79bc4bbddf58  ./results-r3/r3-firstrun-controls_r2.txt
00cc5a316c2fd7850f6921ca7c83549d1af1889519b02c9961346dbe7f1b061d  ./results-r3/r3-firstrun-heldout.txt
ddbb0885e5768faa3c7922799812605b554be825fcf918e58beba2b968b1c60f  ./results-r3/r3-firstrun-reviewer-heldout-Y.txt
991ad46a1c9e2c0fc81c043e2f6c21634129c0034c08d57a88c8f3b4c07543c4  ./results-r3/r3-firstrun-reviewer-heldout.txt
d526bcbcbe7b0acf02b7defcd19bfc95df97fc9981e04e0fba627f53ce8a81f6  ./results-r3/self-test.txt
3ff32ca3509e08043ef05d177ca8d2047b0d483c508e36075148cabcfd527dd2  ./results-r3/treeM-scan-summary-r3.json
727531e08adfda9684de1a2ac1248584ff66dc18fbc4623237beb043e9ceb0a5  ./results-r3/treeM-scan.txt
f37f83ccc4d74e070f22f333cfcd426650eb8821db9138a878b6400e14ef70d9  ./results/controls-controls.txt
a09f794149695c2e58dfd0d42f4972db6770191447a657660c74de7def7d0b2e  ./results/controls-controls_c.txt
bd9b2a9207e42c6edc40f0e6c0ada61039bc255a6feb46713d16db3c153db68c  ./results/controls-controls_d.txt
739cb246c61276a52fcce1f1b09716bb50279d7733e47e4171fd6c3d7e5339b9  ./results/controls-controls_r2.txt
d089cd0b55f843ec64583e657ed1aa3d70e94cfc388f0722a78fabf3f83661c1  ./results/controls-heldout.txt
d1ad8e40a7732e4afd812a032db62ab1f6352b73a5f38a1f747fccdbef24ea61  ./results/controls-reviewer-heldout.txt
f39a888cf7d53076cccf01db21204a8775b8c127df5053d20d6828aaa60efbb2  ./results/exitcodes.txt
2ccdb1eaa7e3fb5e82352cdd16b41a0ca23133ce1ecde8e36a21a4015fcbc4ac  ./results/injection.txt
b19612bb547e0c199b534c1efa725117526d5bfa5161f38af7013a993ac8114a  ./results/m2-m3.txt
53d67f380e71eaf9b06dc1e9c42695e5f80fbc15a83a3d215cdd02bddec345fd  ./results/probes-probe.txt
99ffce2ed4a5f3372027e282adaaaa748c57db42554ce0f0f63f26b6606b6cfc  ./results/probes-probe2.txt
444c0f137fcb182cf657309c2e4213e5bb25bb5a99ce11a8b508ddbd1f38224c  ./results/probes-probe3.txt
e9cbcc20c78f83c5415e8f74648fa16dec20a387b92597a4e8007b3f21056873  ./results/probes-probe4.txt
fdcb5cd4c6aeeb88784ae7e7a9ddfb9522388db48ec752ecc723be3927935ce2  ./results/self-test.txt
6131f4c709014c3be19c269940b8d767f3219af897a3ae76a9f41fdb210296a3  ./results/treeM-scan-summary.json
d185865270c1bb0957e70147050bd717b51031de6846808004cce9219078e34b  ./work/controls.json
17eccf2901c7b48c2cedf9ee43b7958b74a007df5970e6b39bd16771532d3aab  ./work/controls_c.json
e11d72f5ed94155b9b84e704c6bc9ce9fe477f5a56eb341ab9b56a9a0213a8aa  ./work/controls_d.json
18ba1af447ad1260b4439711e101173697ae7d787ee3e9ce901bd011d171883f  ./work/controls_r2.json
d17e0d0b190758c6292f7dc96266fea0442cca0c4c3442642e7dda5f3c1b7f16  ./work/heldout.json
1632e93b219ff91a4b638a4b2eb5905084fb82a0e2b4da472e8176ad0dce85ca  ./work/licences-fixture.json
679bdd1451148465144cc08efaa471b1d934c6cdbbde58b7e700e2dd107b7f21  ./work/licences-r3.json
157b15f3796b0089b481a5236e870436a216c88fc20c6896e324a9aca340bc88  ./work/licences.json
537233ac78a86be16d1b5a165643b631cd2deb2a3f3b93b5f00b1e5ebd0ef718  ./work/m2_r2.py
04a8b30e589648b50d1a426066a4b7f6860a6a11d7edf17e601db2ecfff3e9ab  ./work/proto.amended.py
43ae9c715cd8e0e270d3a880eb83688224e8058f5c65675a6357929eb24df3f5  ./work/proto.r2.py
bf5cad1a75b3e2c8301be5c64af80d564b3b248dd8faa24090bbbf1aacb1f2ef  ./work/proto.r3.py
3056c6d76b4a91462ab358bf08b235ccf69d36f70631a88e7eb64141a8ec17df  ./work/r3-author-diagnostics.json
ce31e49c69b188c6ccfa4eaac6a8ed431f234f51261114af5878972d79dd5c3d  ./work/reviewer-heldout-Y.json
c4591b6d8ec77f205f2eade8b563d7ed5fc3cf9434ba23b536fc570be98424e3  ./work/reviewer-heldout.json
815e7ff1713a754edc0f7d976c03316adac4b18ee6b007663d55b25db2cb866d  ./work/reviewer-probes-Y/m1-diag.json
06e32bbad6f70dae3c21eb34f1680fd55fa298060960735f626fc762a26d541c  ./work/reviewer-probes-Y/posthoc-probes.json
cee1545e90a7d90f8490045c74448a16b3815c317bfb37287673512d3881b012  ./work/reviewer-probes/probe.json
241554b1e61a004933155cd7c7b1b879bbaeef8493cef15c5c737994ceb7f61c  ./work/reviewer-probes/probe2.json
047a4e0e98c66a02e836f4ac9ee6c52bed593431d8899599c66b10b6a6487cc2  ./work/reviewer-probes/probe3.json
1e442fb6ff93257fcb911db3321539e4615da8482b45daebbad17d01a4406c97  ./work/reviewer-probes/probe4.json
425a53025efc01020eed85694a785f624f6821a608df80777c21fbd68467703d  ./work/run_r2.py
46cae4f6862605bc58d87d53a5156eb4ebd9ccb0bcb41d2c22167cc0953b8faa  ./work/run_r3.py
```
