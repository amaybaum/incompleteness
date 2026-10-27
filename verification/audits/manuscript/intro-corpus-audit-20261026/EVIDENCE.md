# Evidence verification (step 7): the evidence layer of the matrix

This file aggregates the three evidence parts into one evidence level per matrix row. It is rendered from `evidence.json` by `evidence/scripts/E4_aggregate.py`; the parts are `evidence/part-E1.md` (Lean certificates and formal coverage), `evidence/part-E2.md` (exhaustive computations and numerics) and `evidence/part-E3.md` (CI receipts and open obligations).

## The rule

The level grades the evidence for the row's chain, not the claim. For a row whose chain refutes the claim, the checked artifact is counter-evidence, and its level is recorded as the row's artifact level.

- **Levels,** strongest first: *reproduced* (the audit regenerated the result and compared it), *certificate-checked* (checked against a retained certificate, expected result or kernel output) and *traced-only* (traced to a report whose evidence the audit did not check, or a step with no artifact of a step-7 type). *Failed* is separate and overrides.
- **Each link gets a level.**
  - *A kernel link* with a declaration source is matched by declaration to the E1 items naming it: a *lean-certificate* item (name, axioms, kernel acceptance) and a *formal-coverage* item (the manuscript claim against the Lean statement). It takes the weaker; a missing item counts as traced-only. A formal-coverage item that records it does not cover the row is left out for that row. A kernel link whose source is a file (a retained result) is matched to the lean-certificate, formal-coverage or CI-receipt items naming that file.
  - *An exhaustive-computation, numerical or exact-algebra link* is matched to the items listing the row that are computations, or replays of a whole research record (CI-receipt items whose source is the record's directory). An item is not matched to a link that names other research records or probe files than the item does (a BH-01 item does not reach a BH-02 link), nor to a link that names only manuscript lines in files the item does not name (a check of a record is not a check of a paper's derivation; the match is by file, not by line range). It takes the weakest matched item.
  - *A link with no support (layer none)*, in a chain of such links only, is a claim about the build, the toolchain, CI or the records. It takes the weakest of the CI-receipt items listing the row.
  - *Every other link* (paper derivation, literature, conjecture) is traced-only: step 7 has no artifact type for it, and steps 2–3 verified its status.
  - A matched item with outcome *fail* fails the link. A link whose status is not *proved* counts as traced-only for the row, whatever its artifact.
- **The load-bearing links.** For a proved-kernel row, its kernel links. Its other links restate the result in the corpus, check it in parallel or record related obligations; they are recorded and do not grade it. For a proved-paper, exhaustive-exact, numerical or calibration row, all its links, so a paper step in the chain holds the row at traced-only whatever its computations reach. A row whose proof status is open, conditional, conjecture or unsupported is traced-only, since its chain does not establish the claim.
- **A row** is *failed* when an item listing it fails, with the item's failure scope as the basis, or when a load-bearing link fails. Otherwise it takes its weakest load-bearing link.
- **The artifact level** of a row is the weakest level over its kernel, computation and build links. For a row held at traced-only by its status or by a paper step, it records what the checked artifacts reach. For an UNSUPPORTED or OVERCLAIM row whose chain has no such link, it grades the computation items listing the row, as counter-evidence.
- CI-receipt and open-obligation items that list a row are recorded with it as context; apart from the two uses above, they do not set its level.

## Counts

| Evidence level | Rows |
|---|--:|
| reproduced | 44 |
| certificate-checked | 127 |
| traced-only | 235 |
| failed | 3 |
| **Total** | **409** |

By proof status:

| Proof status | reproduced | certificate-checked | traced-only | failed |
|---|--:|--:|--:|--:|
| proved-kernel | 0 | 126 | 4 | 0 |
| exhaustive-exact | 7 | 0 | 1 | 0 |
| numerical | 0 | 0 | 2 | 1 |
| calibration | 2 | 0 | 2 | 0 |
| proved-paper | 35 | 1 | 148 | 2 |
| conditional | 0 | 0 | 17 | 0 |
| open | 0 | 0 | 47 | 0 |
| conjecture | 0 | 0 | 9 | 0 |
| unsupported | 0 | 0 | 5 | 0 |

Traced-only rows whose checked artifacts reach a higher level: 20 reproduced, 26 certificate-checked (listed below).

Items: 178 (E1–E3). By part, level and outcome:

| Part | Level | Outcome | Items |
|---|---|---|--:|
| E1 | certificate-checked | partial | 9 |
| E1 | certificate-checked | pass | 111 |
| E1 | traced-only | partial | 2 |
| E2 | failed | fail | 2 |
| E2 | reproduced | partial | 2 |
| E2 | reproduced | pass | 15 |
| E2 | traced-only | partial | 1 |
| E3 | certificate-checked | partial | 3 |
| E3 | certificate-checked | pass | 12 |
| E3 | reproduced | pass | 4 |
| E3 | traced-only | partial | 7 |
| E3 | traced-only | pass | 10 |

## Failed rows

Each failure is of the evidence statement the row carries, as the basis states; it is not a failure of the claim unless the basis says so.

- **I-054** (IMPRECISE, numerical): E2-10 failed: The evidence tag fails: L84's 'with exact probes' and Main.md:170's 'Certified exactly' describe a floating-point probe on named instances, which is not an exact probe in L30's sense. The bound itself (paper proof with Pinsker) and its instance values (E2-09, reproduced exactly) stand.; E2-11 failed: The evidence tag fails on one reading of L30: 'exhaustive' as exhaustive over a class of laws, which the named instances are not. The probe values hold exactly on their instances (P1-P5, P-G reproduced), and the realization theorem rests on its paper proof (Main.md:496-500).; load-bearing link 0 matched a failed item; load-bearing link 1 matched a failed item; load-bearing link 2 matched a failed item
- **I-071** (UNDERCLAIM, proved-paper): E2-11 failed: The evidence tag fails on one reading of L30: 'exhaustive' as exhaustive over a class of laws, which the named instances are not. The probe values hold exactly on their instances (P1-P5, P-G reproduced), and the realization theorem rests on its paper proof (Main.md:496-500).; load-bearing link 2 matched a failed item
- **I-103** (IMPRECISE, proved-paper): E2-10 failed: The evidence tag fails: L84's 'with exact probes' and Main.md:170's 'Certified exactly' describe a floating-point probe on named instances, which is not an exact probe in L30's sense. The bound itself (paper proof with Pinsker) and its instance values (E2-09, reproduced exactly) stand.; load-bearing link 2 matched a failed item

## Rows held at traced-only by an unmatched or failed load-bearing artifact link

Each row below has a load-bearing kernel, computation or build link that no evidence item reached at certificate-checked or better.

| Row | Verdict | Proof status | Link | Gap |
|---|---|---|---|---|
| I-006 | FAITHFUL | proved-paper | `papers/Main.md:534@eae01647` (exact-algebra) | no computation item for this link |
| I-025 | IMPRECISE | proved-paper | `papers/Main.md:119@eae01647` (exact-algebra) | no computation item for this link |
| I-036 | FAITHFUL | proved-paper | `papers/Main.md:121@eae01647` (exact-algebra) | no computation item for this link |
| I-042 | IMPRECISE | proved-paper | `papers/GR.md:218-228@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-042 | IMPRECISE | proved-paper | `verification/programmes/black-hole-information/@eae01647` (exhaustive-computation) | no computation item for this link |
| I-052 | MISCITED | proved-kernel | `papers/GR.md:218-228@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-052 | MISCITED | proved-kernel | `papers/Main.md:624@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-088 | FAITHFUL | proved-kernel | `lean:OIBridge/RootedClassification.lean:135:rootedMap_periodic` (kernel) | no formal-coverage item; E1-98 does not cover this row: the kernel states periodicity of the rooted one-time maps, not the finite order of the bijection |
| I-126 | FAITHFUL | proved-paper | `papers/Main.md:453@eae01647` (exact-algebra) | no computation item for this link |
| I-129 | FAITHFUL | proved-paper | `lean:EquivalenceChain.lean:253:isDiag_Phi` (kernel) | no formal-coverage item; E1-92 does not cover this row: the kernel covers only the diagonal-preservation premise of the written theorem |
| I-149 | FAITHFUL | proved-kernel | `lean:CoherentLiftGauge.lean:537:gl2_strong_gauge_moves_relative_candidate` (kernel) | no formal-coverage item; E1-71 does not cover this row: CoherentLift is pointwise admissibility at every time; it does not encode 'compose exactly across times' (the cocycle condition is vacuous) |
| I-176 | FAITHFUL | proved-paper | `papers/GR.md:140@eae01647` (exact-algebra) | no computation item for this link |
| I-176 | FAITHFUL | proved-paper | `papers/GR.md:356@eae01647` (exact-algebra) | no computation item for this link |
| I-177 | FAITHFUL | proved-paper | `papers/GR.md:581@eae01647; papers/GR.md:356@eae01647` (exact-algebra) | no computation item for this link |
| I-191 | FAITHFUL | proved-paper | `papers/GR.md:338@eae01647` (exact-algebra) | no computation item for this link |
| I-258 | UNDERCLAIM | proved-kernel | `papers/GR.md:266@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-262 | FAITHFUL | proved-paper | `papers/Introduction.md:232@4a260ca9` (exact-algebra) | no computation item for this link |
| I-271 | FAITHFUL | proved-paper | `papers/Introduction.md:251@4a260ca9` (exhaustive-computation) | no computation item for this link |
| I-272 | FAITHFUL | proved-paper | `papers/Main.md:286@eae01647` (exact-algebra) | no computation item for this link |
| I-272 | FAITHFUL | proved-paper | `papers/Introduction.md:251@4a260ca9` (exact-algebra) | no computation item for this link |
| I-273 | FAITHFUL | proved-paper | `papers/Introduction.md:253@4a260ca9` (exact-algebra) | no computation item for this link |
| I-319 | FAITHFUL | proved-paper | `verification/coverage/LEDGER.json@eae01647` (exhaustive-computation) | no computation item for this link |
| I-324 | FAITHFUL | proved-paper | `lean:FiniteEntropy.lean:372:cmi_nonneg` (kernel) | matched only at traced-only: E1-55, E1-93 |
| I-330 | FAITHFUL | proved-paper | `verification/coverage/LEDGER.json@eae01647` (exhaustive-computation) | no computation item for this link |
| I-375 | FAITHFUL | proved-paper | `S/b5_check.py (exact rationals and sympy; scratch, not a repository artifact)` (exact-algebra) | no computation item for this link |
| I-375 | FAITHFUL | proved-paper | `verification/coverage/LEDGER.json@eae01647` (exhaustive-computation) | no computation item for this link |

## Traced-only rows whose checked artifacts reach a higher level

The row's level is traced-only because of its proof status or a paper step; the artifact level records what its kernel, computation or build links reach. For a refuted claim the artifact is counter-evidence.

| Row | Verdict | Proof status | Held by | Artifact level | Role |
|---|---|---|---|---|---|
| I-008 | IMPRECISE | proved-paper | paper-derivation | certificate-checked | support |
| I-009 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-032 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-055 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-074 | FAITHFUL | proved-paper | literature | certificate-checked | support |
| I-093 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-094 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-095 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-096 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-100 | FAITHFUL | proved-paper | literature, paper-derivation | certificate-checked | support |
| I-100.a | FAITHFUL | proved-paper | literature, paper-derivation | certificate-checked | support |
| I-100.b | FAITHFUL | proved-paper | literature, paper-derivation | certificate-checked | support |
| I-102 | IMPRECISE | proved-paper | paper-derivation | certificate-checked | support |
| I-106 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-107 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-108 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-118 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-120 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-122 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-123 | UNSUPPORTED | unsupported | proof status unsupported | reproduced | counter-evidence |
| I-125 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-146 | UNDERCLAIM | open | proof status open | certificate-checked | support |
| I-210 | FAITHFUL | conditional | proof status conditional | reproduced | support |
| I-211 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-216 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-218 | IMPRECISE | proved-paper | paper-derivation | reproduced | support |
| I-225 | OVERCLAIM | unsupported | proof status unsupported | reproduced | counter-evidence |
| I-227 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-230 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-246 | IMPRECISE | conditional | proof status conditional | certificate-checked | support |
| I-247 | FAITHFUL | conditional | proof status conditional | certificate-checked | support |
| I-254 | FAITHFUL | proved-paper | literature | reproduced | support |
| I-261 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-265 | IMPRECISE | proved-paper | paper-derivation | reproduced | support |
| I-267 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-286 | IMPRECISE | open | proof status open | reproduced | support |
| I-289 | IMPRECISE | open | proof status open | certificate-checked | support |
| I-290 | FAITHFUL | open | proof status open | reproduced | support |
| I-291 | IMPRECISE | numerical | link not proved | reproduced | support |
| I-292 | UNDERCLAIM | open | proof status open | certificate-checked | support |
| I-298 | FAITHFUL | proved-paper | paper-derivation | certificate-checked | support |
| I-299 | IMPRECISE | proved-paper | paper-derivation | certificate-checked | support |
| I-305 | FAITHFUL | exhaustive-exact | paper-derivation | reproduced | support |
| I-358 | FAITHFUL | proved-paper | literature | reproduced | support |
| I-372 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |
| I-377 | FAITHFUL | proved-paper | paper-derivation | reproduced | support |

## Chain-link corrections applied

`matrix/chain-relabels.json`, applied by `matrix/scripts/merge_matrix.py` with the mapper's layer kept as `mapper_layer`:

- **I-063** link 2 (`verification/coverage/LEDGER.json@eae01647`): kernel → none; a coverage-ledger entry records the kernel status; the kernel link is link 0, finite_horizon_equivalence.
- **I-282** link 1 (`verification/ROADMAP.md:66@eae01647`): kernel → none; a ROADMAP entry recording an open obligation, not a declaration.
- **I-309** link 0 (`git@17b830bc..b64919cd`): exhaustive-computation → none; a git identity check on sources (E2-19, ci-receipt), not a computation.
- **I-044** link 0 (`verification/programmes/black-hole-information/bh02_scramble_v1/REPORT.md:3@eae0`): paper-derivation → none; a research record's own status line: the claim is about the records, with no derivation.
- **I-227** link 0 (`papers/GR.md:833@eae01647`): exact-algebra → paper-derivation; a manuscript statement of the one-line proof (P_pi maps configuration basis states to basis states); the finite sweeps are link 1.
- **I-227** link 2 (`book/ch07-gravity.md:126@eae01647`): exact-algebra → paper-derivation; a manuscript statement of the one-line proof (P_pi maps configuration basis states to basis states); the finite sweeps are link 1.

## Rows resting on partial items

The item's limits apply to the row (see the part files). A formal-coverage item that does not cover a row is left out of that row's grading and appears above as a gap.

| Row | Level | Partial items |
|---|---|---|
| I-009 | traced-only | E1-70, E1-98 |
| I-102 | traced-only | E1-66, E1-67 |
| I-108 | traced-only | E1-67 |
| I-111 | certificate-checked | E1-85 |
| I-114 | certificate-checked | E1-85 |
| I-120 | traced-only | E1-98 |
| I-121 | certificate-checked | E1-70 |
| I-128 | certificate-checked | E1-92 |
| I-147 | certificate-checked | E1-71 |
| I-148 | certificate-checked | E1-71 |
| I-157 | certificate-checked | E1-71 |
| I-193 | reproduced | E2-18 |
| I-194 | reproduced | E2-18 |
| I-259 | certificate-checked | E1-71 |
| I-289 | traced-only | E1-70 |
| I-302 | certificate-checked | E1-71 |
| I-308 | certificate-checked | E3-11 |
| I-312 | certificate-checked | E3-12 |
| I-324 | traced-only | E1-55 |
| I-325 | certificate-checked | E1-66 |
| I-326 | certificate-checked | E1-67 |
| I-329 | certificate-checked | E1-101, E1-70 |
| I-331 | certificate-checked | E1-71 |

## Limits that apply across rows

- No Lean toolchain is available here, so no kernel item is *reproduced*: *certificate-checked* is the highest level a kernel link can reach (E1).
- The CI jobs examined replayed the OIBridge build from the Actions cache (E1-122, E3-11), and for 9 of the 14 Appendix A modules no fresh elaboration was observed at these sources (E3-11). The axiom reports are lake replays of an elaboration of byte-identical sources; a fresh elaboration is proposed for owner authorization.
- For the 21 printed declarations outside the retained result, "exactly the three axioms" is read from CI job-log text, which is diagnostic. The structured certificate there is the Release gate step's conclusion, which under `tools/lean_axiom_check.py`'s contract establishes that every printed report lies within the allow-list and that every declared `#print axioms` has a report. No row's level rests on the log text alone. The logs expire (E3-14).
- The concept DOI and the release archive that the Introduction cites (L197–200) were not checked (E3-16).

## Proposed for owner authorization (not dispatched)

- A fresh-build CI reproduction of `introduction_repro` at `17b830bc`.
- An extended expected result covering the additional modules (OD-15). It can be re-derived from the digest-checked log of job 121598983127 without a rebuild while that log is available; landing it in `papers/introduction_repro/` is a change on #918.
- BHa and BHb `mutants.py` replays, and the BHb `-O` replay, in CI (E2). The BHb `checks.py` replay is done (E3-18).
