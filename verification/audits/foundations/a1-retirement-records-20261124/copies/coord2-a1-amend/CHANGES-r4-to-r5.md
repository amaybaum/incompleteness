# Changes from r4 to r5, with the source of each

## Sources

- **N1, N3:** review r4 (`review-r4/review.md`, sha256
  `be8879aa6f86d97581c39f5e025fa152b42f9a09b36c02c51ce912ab9b2183f4`).
- **Item 4:** the owner's decision on the r4 review, quoted below.
- **Coordinator text:** the coordinator's final O-13 text `O13-DECISION-FINAL-r4.md`, sha256 `2633770b…5914`, which
  includes C1–C4.

The r1–r4 files and `O13-DECISION-FINAL-r4.md` are unchanged.

**Owner decision on the r4 review** (owner `amaybaum`, 2026-11-24), quoted:

> The O-13 decision text is acceptable in substance. Before final adoption:
> 1. Apply N1 to eliminate any possible implication that an unresolved dependency establishes independence from A1.
> 2. Apply N3 to the inventory.
> 3. Accept N2 as currently handled.
> 4. Preserve all three historical workflow runs, explicitly distinguishing the failed run from the successful runs.
>    Failed evidence must not be discarded or presented as acceptance evidence.
> 5. Recompute the affected hashes and update the O-13 decision text accordingly.
> 6. Obtain a focused independent delta review of these corrections only.
> Do not reopen the scientific assessment or any settled amendment question.

## Changes

| # | Change | Where | Source |
|---|---|---|---|
| 1 | D402 adopts N1's wording. Only the clause after "cited for it;" changes (texts below). Its reason text is updated to match. | `diffs-r5/new-edit-records-D402-D412.json`; `EDITS-P-to-r5.diff`; §32.9 edit table | N1 |
| 2 | One §32.9 bullet describing D402 is updated to match: "D402 states in the sentence that it is not established whether the entries require finiteness of the substratum, and names the conditions on which this turns." | §32.9 (`diffs-r5/PREREG-append-s32-r5.diff`) | N1 (consequential accuracy) |
| 3 | Higgs row categories: "E" becomes "none (unchanged)" | O13-INVENTORY-r5 §1 | N3 |
| 4 | Inventory rows that describe D402 are updated to the N1 wording: the frame row, its strengthened? cell, the 1/α₀ row, and the §2 sentence quoting D402. The heading and §32.9 version label are updated. Appendix A is regenerated from the r5 ledger. | O13-INVENTORY-r5 | N1 (consequential accuracy) |
| 5 | The three runs are listed separately in O-13 item 2. 45077568347 (T0′ trial) concluded failure; 45080985924 (T1′ trial) and 45083256017 (`verify` on T1′) concluded success. All three are kept as historical evidence of what they tested. The failed run is not discarded and is not presented as acceptance evidence. None is acceptance evidence for the amended plan. Re-verified by REST GET on 2026-11-24 (name, event, branch, head_sha, conclusion, created_at all as stated). | O13-DECISION-FINAL-r5 item 2 | item 4 |
| 6 | Hashes recomputed: D402 new_sha256, `edits.json`, `ledger.json`, the configuration pins, the §32.10 pins, the inventory hash, "proposal r5". Review lines carry the placeholder "<focused delta review: file, sha256, verdict>" for the r5 corrections; the r4 review is kept as cited. | O13-DECISION-FINAL-r5; `diffs-r5/CONFIG-r4-to-r5.diff`; §32.10 | item 5 |

**D402, r4:**

> …cited for it; whether an entry requires finiteness of the substratum is not established where those theorems use
> the measure conditions of Lemma 1c or Proposition 4b or the continuum conditions of the $d = 3$ selection (§3.2),
> and $1/\alpha_0$ is computed from the lattice momentum integral of §6.1 over the whole Brillouin zone, whose
> counterpart for a finite substratum and whose normalization of the vertex coupling are not established.

**D402, r5 (full):**

> they rest on the local spatial/gauge construction of §2.3 and on cubic-group representation theory, each entry
> under the further conditions of the theorems cited for it; it is not established whether the entries require
> finiteness of the substratum; this turns in particular on the measure conditions of Lemma 1c or Proposition 4b, the
> continuum conditions of the $d = 3$ selection (§3.2) and, for $1/\alpha_0$, which is computed from the lattice
> momentum integral of §6.1 over the whole Brillouin zone, on that integral's counterpart for a finite substratum and
> on the normalization of the vertex coupling.

**Accuracy adjustment to N1's wording.** The review's text ended "and, for $1/\alpha_0$, …". It is completed with r4's
reviewed 1/α₀ content: computed from the lattice momentum integral over the whole Brillouin zone, its finite-substratum
counterpart, and the vertex normalization.

## Results

| Item | Value |
|---|---|
| D402 new_sha256 | `ac5a1b8504586ec1432cba5ec278947a6ecc025f2df101e1d794bd7c78592c32` |
| Other splices | all other 409 splices are unchanged from r4 (old_sha256 `227117bc…` unchanged) |
| `edits.json` | `f99d705ae896c891806ee99c2217e24237cada5ac49e607b0b013bd43c6dd38d` |
| `ledger.json` | `65c8c866fa1ebebb338c869113ed3e1275a9aca1ededab58f6bdf286aab1a2e8` |
| Counts | 412 records; 410 splices in 44 files; P's 399 splices byte-equal |

## Checks (`work-r5/`)

| Check | Result |
|---|---|
| `--build-ledger` | as above |
| `edits_check --static` | PASS (the infinity scan finds 0 hits on the new text; register, capitals and identifier 0; mirror 0; sitemap 194/194) |
| `--commit H --simulate` | PASS (412 unique; residual 5, all allowed; criterion-5 0; identifier and count 0) |
| `--pins` | PASS |
| `--repo-scan --simulate --final` | PASS (0 unexplained) |
| both self-tests | PASS |
| `--verify-ledger` | re-derived identically |
| `--verify-pins` with the r5 PREREG | PASS |
| Item 7 as frozen | count 0 lines; pointer only the 4 false positives; PASS |
| NC1–NC5 | each FAIL |
| `duplicate_check` on the edited sources and the r5 PREREG | OK; OK |
| Gate tools (coverage, claims, voice, citation_roles, dependency_label, baseline_label) | identical output and exit status, H against H with D402–D412 |
| `staleness_check` | STALE for SM and the book, as expected |
| SM.tex | sha256 `778c10c0e98af6125f9fd8445cc176ee9f55b6d0d250628cb2af2c708ea414a2`; differs from T1′ only in the edited paragraphs and the stamp |
| FULL.tex | unchanged |
| PREREG r5 | pure append; §32.10 is the 13th and last `Record pins`; both parsers read 6 rows. The §32 text differs from r4 in 3 places: the D402 table cell, the one bullet, and the two pins. |

**Not run:** `guards_check`, SC-42, PDFs, CI.
