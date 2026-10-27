# Evidence verification (step 7): the evidence layer of the matrix

This file aggregates the three evidence parts into one evidence level per matrix row. It is rendered from `evidence.json` by `evidence/scripts/E4_aggregate.py`; the parts are `evidence/part-E1.md` (Lean certificates and formal coverage), `evidence/part-E2.md` (exhaustive computations and numerics) and `evidence/part-E3.md` (CI receipts and open obligations).

## The rule

- **Levels,** strongest first: *reproduced* (the audit regenerated the result and compared it), *certificate-checked* (checked against a retained certificate, expected result or kernel output) and *traced-only* (traced to a report whose evidence the audit did not check). *Failed* is separate: a row that an item with outcome *fail* lists is failed, whatever its other links.
- **Evidence-bearing links** are those of layer kernel, exhaustive-computation, numerical or exact-algebra. Paper derivations, literature, conjectures and links with no support have no artifact of a step-7 type; steps 2–3 verified their status, and step 7 adds nothing to them.
- **A kernel link** is matched by its declaration to the E1 items that name it: a *lean-certificate* item (name, axioms, kernel acceptance) and a *formal-coverage* item (the manuscript claim against the Lean statement). It takes the weaker of the two; a missing item counts as traced-only. A kernel-layer link whose source is a file rather than a declaration (a retained result, the coverage ledger) is matched to the E1 or E3 items naming that file, and takes the weakest of them.
- **An exhaustive-computation, numerical or exact-algebra link** is matched to the E2 computation items that list the row. It takes the weakest; no match counts as traced-only.
- **A row** takes its weakest evidence-bearing link. A row with no evidence-bearing link takes the weakest of the CI-receipt items that list it, if there are any (claims about the build, the toolchain or CI); otherwise it is traced-only, on the basis *no step-7 artifact*.
- Otherwise, CI-receipt and open-obligation items that list a row are recorded with it as context. They state limits; they do not set its level.

## Counts

| Evidence level | All rows | Rows with evidence-bearing links |
|---|--:|--:|
| reproduced | 67 | 58 |
| certificate-checked | 153 | 149 |
| traced-only | 187 | 28 |
| failed | 2 | 2 |
| **Total** | **409** | **237** |

Items: 178 (E1–E3). By part, level and outcome:

| Part | Level | Outcome | Items |
|---|---|---|--:|
| E1 | certificate-checked | partial | 9 |
| E1 | certificate-checked | pass | 111 |
| E1 | traced-only | partial | 2 |
| E2 | failed | fail | 1 |
| E2 | reproduced | partial | 4 |
| E2 | reproduced | pass | 14 |
| E2 | traced-only | partial | 1 |
| E3 | certificate-checked | partial | 3 |
| E3 | certificate-checked | pass | 12 |
| E3 | reproduced | pass | 4 |
| E3 | traced-only | partial | 7 |
| E3 | traced-only | pass | 10 |

## Failed rows

- **I-054** (IMPRECISE, numerical): an item listing the row failed: E2-10. E2-10: fail, "Evidence form of L30/L56/L84: L30 defines an 'exact probe' as 'an exhaustive computation in exact rational arithmetic at small size'; L84 tags the Pinsker bound…"
- **I-103** (IMPRECISE, proved-paper): an item listing the row failed: E2-10. E2-10: fail, "Evidence form of L30/L56/L84: L30 defines an 'exact probe' as 'an exhaustive computation in exact rational arithmetic at small size'; L84 tags the Pinsker bound…"

## Evidence-bearing rows left at traced-only

Each row below has a kernel or computation link that no evidence item reached, or reached only at traced-only.

| Row | Verdict | Proof status | Link | Gap |
|---|---|---|---|---|
| I-006 | FAITHFUL | proved-paper | `papers/Main.md:534@eae01647` (exact-algebra) | no computation item |
| I-025 | IMPRECISE | proved-paper | `papers/Main.md:119@eae01647` (exact-algebra) | no computation item |
| I-034 | FAITHFUL | proved-kernel | `papers/Main.md:453; 178-198@eae01647` (exact-algebra) | no computation item |
| I-036 | FAITHFUL | proved-paper | `papers/Main.md:121@eae01647` (exact-algebra) | no computation item |
| I-042 | IMPRECISE | proved-paper | `papers/GR.md:218-228@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-042 | IMPRECISE | proved-paper | `verification/programmes/black-hole-information/@eae01647` (exhaustive-computation) | no computation item |
| I-052 | MISCITED | proved-kernel | `papers/GR.md:218-228@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-052 | MISCITED | proved-kernel | `papers/Main.md:624@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-063 | FAITHFUL | proved-kernel | `verification/coverage/LEDGER.json@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-088 | FAITHFUL | proved-kernel | `papers/Main.md:618@eae01647` (exact-algebra) | no computation item |
| I-126 | FAITHFUL | proved-paper | `papers/Main.md:453@eae01647` (exact-algebra) | no computation item |
| I-176 | FAITHFUL | proved-paper | `papers/GR.md:140@eae01647` (exact-algebra) | no computation item |
| I-176 | FAITHFUL | proved-paper | `papers/GR.md:356@eae01647` (exact-algebra) | no computation item |
| I-177 | FAITHFUL | proved-paper | `papers/GR.md:581@eae01647; papers/GR.md:356@eae01647` (exact-algebra) | no computation item |
| I-191 | FAITHFUL | proved-paper | `papers/GR.md:338@eae01647` (exact-algebra) | no computation item |
| I-210 | FAITHFUL | conditional | `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:35-40@eae01647` (exact-algebra) | no computation item |
| I-258 | UNDERCLAIM | proved-kernel | `papers/GR.md:266@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-262 | FAITHFUL | proved-paper | `papers/Introduction.md:232@4a260ca9` (exact-algebra) | no computation item |
| I-266 | FAITHFUL | open | `verification/programmes/black-hole-information/bh01_access_v1/REPORT.md:22@eae01647` (exhaustive-computation) | no computation item |
| I-271 | FAITHFUL | proved-paper | `papers/Introduction.md:251@4a260ca9` (exhaustive-computation) | no computation item |
| I-272 | FAITHFUL | proved-paper | `papers/Main.md:286@eae01647` (exact-algebra) | no computation item |
| I-272 | FAITHFUL | proved-paper | `papers/Introduction.md:251@4a260ca9` (exact-algebra) | no computation item |
| I-273 | FAITHFUL | proved-paper | `papers/Introduction.md:253@4a260ca9` (exact-algebra) | no computation item |
| I-281 | UNDERCLAIM | open | `papers/GR.md:266@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-282 | FAITHFUL | open | `verification/ROADMAP.md:66@eae01647` (kernel) | kernel-layer link without a declaration source; no item names its file |
| I-319 | FAITHFUL | proved-paper | `verification/coverage/LEDGER.json@eae01647` (exhaustive-computation) | no computation item |
| I-324 | FAITHFUL | proved-paper | `lean:FiniteEntropy.lean:372:cmi_nonneg` (kernel) | matched only at traced-only: E1-55, E1-93 |
| I-330 | FAITHFUL | proved-paper | `verification/coverage/LEDGER.json@eae01647` (exhaustive-computation) | no computation item |
| I-368 | FAITHFUL | proved-paper | `S/b5_check.py (exact rationals and sympy; scratch, not a repository artifact)` (exact-algebra) | no computation item |
| I-370 | FAITHFUL | proved-paper | `S/b5_check.py (exact rationals and sympy; scratch, not a repository artifact)` (exact-algebra) | no computation item |
| I-375 | FAITHFUL | proved-paper | `S/b5_check.py (exact rationals and sympy; scratch, not a repository artifact)` (exact-algebra) | no computation item |
| I-375 | FAITHFUL | proved-paper | `verification/coverage/LEDGER.json@eae01647` (exhaustive-computation) | no computation item |
| I-379 | FAITHFUL | proved-paper | `S/b5_check.py (exact rationals and sympy; scratch, not a repository artifact)` (exact-algebra) | no computation item |

## Matrix labels that disagree with the chains

The evidence rule reads the chain's layers. These rows' labels disagree with their own chains; each is a correction for the matrix, recorded here and not applied.

- **Proof status implies an artifact, but the chain has no evidence-bearing link:** I-172 (numerical; evidence traced-only, no step-7 artifact (paper, literature, conjecture or none)), I-308 (proved-kernel; evidence certificate-checked, CI-receipt items, for a row with no evidence-bearing link), I-310 (proved-kernel; evidence certificate-checked, CI-receipt items, for a row with no evidence-bearing link), I-312 (proved-kernel; evidence certificate-checked, CI-receipt items, for a row with no evidence-bearing link).
- **Kernel-layer links whose source is a paper, ledger or roadmap line, not a declaration or a certified file:** I-042 `papers/GR.md:218-228@eae01647`; I-052 `papers/GR.md:218-228@eae01647`; I-052 `papers/Main.md:624@eae01647`; I-063 `verification/coverage/LEDGER.json@eae01647`; I-258 `papers/GR.md:266@eae01647`; I-281 `papers/GR.md:266@eae01647`; I-282 `verification/ROADMAP.md:66@eae01647`. Each holds its row at traced-only under the weakest-link rule.

## Rows resting on partial items

The level stands; the partial item's limits apply to the row (see the part files).

| Row | Level | Partial items |
|---|---|---|
| I-009 | certificate-checked | E1-70, E1-98 |
| I-054 | failed | E2-11 |
| I-071 | certificate-checked | E1-99, E2-11 |
| I-088 | traced-only | E1-98 |
| I-102 | certificate-checked | E1-66, E1-67 |
| I-108 | certificate-checked | E1-67 |
| I-111 | certificate-checked | E1-85 |
| I-114 | certificate-checked | E1-85 |
| I-120 | certificate-checked | E1-98 |
| I-121 | certificate-checked | E1-70 |
| I-128 | certificate-checked | E1-92 |
| I-129 | certificate-checked | E1-92 |
| I-147 | certificate-checked | E1-71 |
| I-148 | certificate-checked | E1-71 |
| I-149 | certificate-checked | E1-71 |
| I-157 | certificate-checked | E1-71 |
| I-193 | reproduced | E2-18 |
| I-194 | reproduced | E2-18 |
| I-225 | reproduced | E2-07 |
| I-227 | reproduced | E2-07 |
| I-259 | certificate-checked | E1-71 |
| I-265 | reproduced | E2-07 |
| I-286 | reproduced | E2-07 |
| I-289 | certificate-checked | E1-70 |
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
- The CI jobs examined replayed the OIBridge build from the Actions cache (E1-122, E3-11). Their axiom reports are the retained certificate; a fresh elaboration is proposed for owner authorization.
- Kernel declarations outside the 14 retained modules have axiom reports only in CI logs that expire (E3-14).

## Proposed for owner authorization (not dispatched)

- A fresh-build CI reproduction of `introduction_repro` at `17b830bc`.
- An extended expected result covering the additional modules (OD-15), made before their CI logs expire.
- BHa and BHb `mutants.py` replays in CI (E2).
