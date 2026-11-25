# Changes in revision r2 of the claims-checker redesign (Issue #1565, PR #1567)

Base: PR #1567 head `1d768f7d8639fc45ec94fbe6d9fd2d27d825ddf5` (`DESIGN.md`, `work/*`). Review: PR
#1567 comment 7166791821 (verdict REVISE). Owner decision (`amaybaum`, 2026-11-25), verbatim: "#1567
| Correct the claims-checker design against the independent findings." with: "The prototype's
improvement over the existing checker is encouraging, but three silent misses remain unacceptable
without correction. Require actual logical qualification of the scientific claim, not merely
proximity to a qualifying phrase. Do not treat H-slope or any other hypothesis as licensing a
withdrawn claim without independently established scientific justification. Preserve the
reviewer's held-out controls and require additional independent controls for the revised design."
Owner directions: Issue #1565 comment 7165663427.

All work is local and paper-only: no repository file, no git ref and no GitHub text was changed.

**Goal link.** Verification integrity (Issue #1565): this revision decides whether the corrected
specification meets the review's findings and the owner's requirements well enough to go to a new
independent review with new held-out controls. It decides no manuscript claim and licenses no
hypothesis.

## Findings

| Finding | Change | Where |
|---|---|---|
| R1 G3 is co-occurrence | G3 applies only when a licensed qualifier heads a fronted antecedent (`If/When/Under/Given/Assuming/Provided/In/On/For …`) or a post-posed restrictor (`only under/if/when …`). New REVIEW trigger R6 for negating or contrasting operators scoping a qualifier (`without, even, regardless of, irrespective of, independently of, whether or not, or not, with or without, stronger than, beyond, except, apart from, unless, not`; post-posed `fails, is violated, does not hold, …`); R6 precedes G3. Polarity-flipped injections added to criterion 3. Result: all five R1 sentences and the 500-paragraph injection class are REVIEW, never PASS (6,883 / 6,883 at corpus scale for three flipped forms). | DESIGN-r2 §3.4, §5 criterion 3, §6.2, §6.4 |
| R2 G2 not mechanical | G2 applies only when A is the immediate complement of `that`/`whether`/`not claimed …:` (≤ 6 tokens, no clause boundary, no auxiliary between) and the local matrix ends with a known frame; coordinated complements and the claim-noun post-frame stated. `whether or not` and `whether X or Y,` excluded; `the necessity reading` removed as a frame (now R3). Comma + `since`/`because` added to the clause boundaries. All seven R2 sentences: 6 FAIL, 1 REVIEW (R3), 0 PASS. | §3.2, §3.4, §6.2 |
| R3 criterion 6 failed (24 / 34) | Specification repaired (R1, R2, R4, R5, R10); reviewer controls not edited. r2 on batch X: first complete run 32 / 34 (X-P-08 REVIEW; X-P-12 PASS, a silent miss introduced by r2 itself), final 34 / 34. Stated plainly that batch X is not held out for r2. Criterion 6 now requires a new independent batch. | §5 criterion 6, §6.1 |
| R4 no remedy for false-positive FAIL; §3.10/§3.5 mismatch | Added R7: an unknown negative, non-factive or reporting frame with A as immediate complement goes to REVIEW; known-frame lexicon extended (`it is false that`, `has not been shown`, `nobody has shown`, `no statement that`, …). Stated the rule-data amendment path for false-positive FAILs (new negative control, rule-data change, full self-test, independent review, owner approval; never a record). | §3.4 R7, §3.13 |
| R5(a) adjectival post-frame missing | Post-frame "the claim that A is withdrawn/false/unproved/…" implemented for every template; claim noun without a negative predicate → R7. Reviewer probes v1–v4 PASS; X-N-04 PASS. | §3.4 G2 item 4 |
| R5(b) H-slope licensed without review | Licensed lists removed from rule data; the deployed licence file is empty; H-slope is ineligible (`papers/GR.md:72`, `:76`). Mechanism controls run under a fixture marked `fixture: true` (H-slope absent, refused for scans) and under the empty file with mechanically derived expectations. "Under H-slope, …" is REVIEW in both. | §2, §3.6, §6.1 |
| R6 one exit code | Exit 1 FAIL, 2 unresolved REVIEW, 3 invalid/stale licence or review record, 4 self-test, usage or internal error (exceptions map to 4); precedence 4 > 3 > 1 > 2. 23 exit-code controls pass. | §3.8, §6.3 |
| R7 no source revision in records | Records carry `revision` (full commit reachable from `main`), `window_sha256` for R1/R5/N1, `code`; rule for later commits stated (ancestry, same sentence and window hash, same finding); stale or FAIL-matching records are exit 3. | §3.7, §6.3 |
| R8 adopt (b), define active material | Adopted. Active: `papers/**`, `book/**`, `README.md` outside `verification/`, `verification/README.md`, AGENTS.md outside `## … (record)` sections. Records reported in JSON with `active: false`, exit unaffected. pr982 records no longer needed. | §3.9 |
| R9 no licensing procedure | Four-step procedure: anchor quotation establishing the claim under exactly that qualifier, independent scientific review record bound to a commit, owner admission with three controls, re-review on anchor change. Unreviewed entries fail validation and the self-test (exit 3). | §3.6 |
| R10 paraphrase coverage | Per-rule frozen equivalence sets with stated derivation operations; lexical near-miss scan (subject term before a rule cue, no template match) → REVIEW N1. X-P-07, X-P-10, X-P-13 now FAIL. Disclosed that the three matching equivalence entries were written after reading those controls; the near-miss scan is the generalizing mechanism (R2-A-07 … R2-A-10 REVIEW). | §3.11, §3.12, §6.1 |
| R11 R7-FWD | Decided: amend the guard in the same change, pinning `OI_RULES` and the OI rule ids, absence of marker-list acceptance, and the licence file; `OI_MARKERS` not kept as a vestigial token. Rule data stay in `tools/claims_check.py`; licences and records in JSON under `verification/infrastructure/claims-check/`. | §3.1, §8 |
| R12 injection lacks polarity and frame scope | Three polarity-flipped, three cross-clause and one near-miss sentence added to the injection; none passes in 6,883 paragraphs. | §4, §5 criterion 3, §6.4 |

## Nits

| Nit | Change |
|---|---|
| `which` inconsistent between copular and verbal rules | Copular `which` in a comma-relative clause binds to the preceding noun phrase (X-P-05 FAIL). §3.3 |
| Double negation and "not surprising" go to REVIEW | `do not doubt that`, `no doubt that`, `not surprising that`, `cannot be doubted`, `undeniabl…` are treated as assertion (X-P-08, probe v7 FAIL). §3.4 R7 |
| §6.3 N-OI-3 written out in full | Stated in §4 and §6.4 tables. |
| §1 F2 definitions | Paragraph and "no named hypothesis" defined; figures recomputed: 6,883 / 2,539 / 1,972 / 1,023 / 19, identical to the reviewer's. §1 |
| §3.1 rule-data location open | Decided (see R11). §3.1 |

## Owner directions (Issue #1565 comment 7165663427)

| Direction | Status in r2 |
|---|---|
| 1 Scan every Markdown file, fail CI only for active material | Met: §3.9, exit-code controls. |
| 2 Licensing hypotheses established from the corpus with independent scientific review | Met as procedure; no licence exists yet (§3.6). |
| 3 Version-controlled review records with reviewer identity and exact source revision | Met: §3.7. |
| 4 Distinct exit codes for confirmed violations and unresolved review, both blocking | Met: §3.8. |
| 5 Simplest reliable approach passing held-out controls | Not yet demonstrated: the approach stays regex-only (no parser), but a new independent held-out batch is required (§5 criterion 6). |
| 6 Scientifically equivalent assertions without unrestricted NLU | Met within stated limits: equivalence sets and near-miss scan (§3.11–§3.12); residual class stated (§3.10). |

## Owner decision items

| Item | Status |
|---|---|
| Three silent misses | Closed: X-P-07, X-P-10, X-P-13 FAIL; near-miss scan sends further paraphrases to REVIEW. |
| Logical qualification, not proximity | G1/G2/G3 positional; R6 for negated qualifiers; licensed qualifier elsewhere in the clause never governs (R2-P-01). |
| No hypothesis licenses a withdrawn claim without independent justification | Licence file empty; validation and self-test refuse unreviewed entries; H-slope ineligible. |
| Preserve the reviewer's held-out controls | `work/reviewer-heldout.json` byte-identical (SHA-256 `c4591b6d…24e3`, as published in the review); probes byte-identical under `work/reviewer-probes/`. |
| Additional independent controls | Required by §5 criterion 6 from the next independent reviewer. Batch R2 (26 controls) was written by this revision's author for the new mechanisms and is not held-out evidence. |

## Not changed, with reason

- M1 deletion mutants not re-run: the r1 mutant set is not among the work files; it must be
  regenerated before acceptance (stated in §6.4).
- Trees A and H not re-scanned; their distinguishing paragraphs are controls that pass (§7).
- R6 kept at REVIEW rather than FAIL (stated minimum of the review; blocking; FAIL is a one-line
  change, §9 Q3).
- §A.42 provenance paragraphs of AGENTS.md not delimited (needs an AGENTS.md edit; §9 Q4).
- `papers/GR.md:144` near-miss left as a REVIEW rather than narrowing the cue after seeing it
  (§9 Q5).

## Results summary

| Run | Result |
|---|---|
| Original 92 controls (batches 1, H, C, D) | 92 / 92 under fixture; 92 / 92 under empty licences (derived expectations). First complete r2 run: 89 / 92. |
| Reviewer's 34 controls (not held out for r2) | first complete r2 run 32 / 34 (X-P-08 REVIEW, X-P-12 PASS); final 34 / 34, both configurations |
| Batch R2 (26, author) | first run 25 / 26 (R2-A-09 PASS); final 26 / 26 |
| Review's adversarial probes (30) | 22 exact; 8 REVIEW where the reviewer wrote FAIL (v13, g1–g6, f1); 0 PASS where FAIL was expected |
| Exit-code, licence and record controls | 23 / 23 |
| M2 / M3 | 0 of 4,400 insertions change a FAIL; current checker accepts 924 / 1,100 |
| Corpus injection (6,883 paragraphs, 11 sentences) | 0 PASS for every positive, flipped, cross-clause and near-miss sentence; governed G3 sentence 6,757 PASS / 126 REVIEW (merged sentences) under fixture, all REVIEW under empty licences; governed G2 sentence 6,883 PASS |
| Tree-M scan (1,133 files, empty licences) | exit 2; active 0 FAIL, 3 REVIEW (two mirrored H-Hawking KMS sentences, one near-miss in `papers/GR.md:144`); records 0 FAIL, 27 REVIEW |
| Self-test (`--self-test`) | exit 0: 152 controls, 0 mismatches, deployed licence file valid (empty) |

## Files

| File | SHA-256 |
|---|---|
| `DESIGN-r2.md` | `25af5534c0d3ff04526b8f73e92c0b65003c26f02ea939a4151cf0780860f240` |
| `DESIGN.md` | `f1ea30f0cc16bf6a30ed26502760f7451d18e3de90ab549f82b0155967581226` |
| `results/controls-controls.txt` | `f37f83ccc4d74e070f22f333cfcd426650eb8821db9138a878b6400e14ef70d9` |
| `results/controls-controls_c.txt` | `a09f794149695c2e58dfd0d42f4972db6770191447a657660c74de7def7d0b2e` |
| `results/controls-controls_d.txt` | `bd9b2a9207e42c6edc40f0e6c0ada61039bc255a6feb46713d16db3c153db68c` |
| `results/controls-controls_r2.txt` | `739cb246c61276a52fcce1f1b09716bb50279d7733e47e4171fd6c3d7e5339b9` |
| `results/controls-heldout.txt` | `d089cd0b55f843ec64583e657ed1aa3d70e94cfc388f0722a78fabf3f83661c1` |
| `results/controls-reviewer-heldout.txt` | `d1ad8e40a7732e4afd812a032db62ab1f6352b73a5f38a1f747fccdbef24ea61` |
| `results/exitcodes.txt` | `f39a888cf7d53076cccf01db21204a8775b8c127df5053d20d6828aaa60efbb2` |
| `results/injection.txt` | `2ccdb1eaa7e3fb5e82352cdd16b41a0ca23133ce1ecde8e36a21a4015fcbc4ac` |
| `results/m2-m3.txt` | `b19612bb547e0c199b534c1efa725117526d5bfa5161f38af7013a993ac8114a` |
| `results/probes-probe.txt` | `53d67f380e71eaf9b06dc1e9c42695e5f80fbc15a83a3d215cdd02bddec345fd` |
| `results/probes-probe2.txt` | `99ffce2ed4a5f3372027e282adaaaa748c57db42554ce0f0f63f26b6606b6cfc` |
| `results/probes-probe3.txt` | `444c0f137fcb182cf657309c2e4213e5bb25bb5a99ce11a8b508ddbd1f38224c` |
| `results/probes-probe4.txt` | `e9cbcc20c78f83c5415e8f74648fa16dec20a387b92597a4e8007b3f21056873` |
| `results/self-test.txt` | `fdcb5cd4c6aeeb88784ae7e7a9ddfb9522388db48ec752ecc723be3927935ce2` |
| `results/treeM-scan-summary.json` | `6131f4c709014c3be19c269940b8d767f3219af897a3ae76a9f41fdb210296a3` |
| `work/controls.json` | `d185865270c1bb0957e70147050bd717b51031de6846808004cce9219078e34b` |
| `work/controls_c.json` | `17eccf2901c7b48c2cedf9ee43b7958b74a007df5970e6b39bd16771532d3aab` |
| `work/controls_d.json` | `e11d72f5ed94155b9b84e704c6bc9ce9fe477f5a56eb341ab9b56a9a0213a8aa` |
| `work/controls_r2.json` | `18ba1af447ad1260b4439711e101173697ae7d787ee3e9ce901bd011d171883f` |
| `work/heldout.json` | `d17e0d0b190758c6292f7dc96266fea0442cca0c4c3442642e7dda5f3c1b7f16` |
| `work/licences-fixture.json` | `1632e93b219ff91a4b638a4b2eb5905084fb82a0e2b4da472e8176ad0dce85ca` |
| `work/licences.json` | `157b15f3796b0089b481a5236e870436a216c88fc20c6896e324a9aca340bc88` |
| `work/m2_r2.py` | `537233ac78a86be16d1b5a165643b631cd2deb2a3f3b93b5f00b1e5ebd0ef718` |
| `work/proto.amended.py` | `04a8b30e589648b50d1a426066a4b7f6860a6a11d7edf17e601db2ecfff3e9ab` |
| `work/proto.r2.py` | `43ae9c715cd8e0e270d3a880eb83688224e8058f5c65675a6357929eb24df3f5` |
| `work/reviewer-heldout.json` | `c4591b6d8ec77f205f2eade8b563d7ed5fc3cf9434ba23b536fc570be98424e3` |
| `work/run_r2.py` | `425a53025efc01020eed85694a785f624f6821a608df80777c21fbd68467703d` |
| `work/reviewer-probes/probe.json` | `cee1545e90a7d90f8490045c74448a16b3815c317bfb37287673512d3881b012` |
| `work/reviewer-probes/probe2.json` | `241554b1e61a004933155cd7c7b1b879bbaeef8493cef15c5c737994ceb7f61c` |
| `work/reviewer-probes/probe3.json` | `047a4e0e98c66a02e836f4ac9ee6c52bed593431d8899599c66b10b6a6487cc2` |
| `work/reviewer-probes/probe4.json` | `1e442fb6ff93257fcb911db3321539e4615da8482b45daebbad17d01a4406c97` |

`DESIGN.md`, `work/proto.amended.py`, `work/controls.json`, `work/heldout.json`, `work/controls_c.json` and `work/controls_d.json` are the PR #1567 head files, unchanged. `work/reviewer-heldout.json` and `work/reviewer-probes/*` are the reviewer's files, byte-identical. `work/licences-fixture.json` is a mechanism-test input that licenses nothing.
