# Independent review, round 2: A1 amendment proposal r2

**Scope.** I reviewed `PROPOSAL-r2.md`, `CHANGE-INVENTORY-r2.md`, `CHANGES-r1-to-r2.md`, `diffs-r2/` and `work-r2/`.
I am a non-author reviewer, working 2026-11-24. The review was paper-only:

- Nothing was written in the repository.
- GitHub was read by REST GET only: main, #1477 and the H..main compare.
- P's checkers and the S1 lint ran only on copies under `review-r2/`. The repository was read through `git show` and
  `git archive` into scratch.

**Inputs verified.**

- `MANIFEST.sha256` passes.
- PROPOSAL-r2 is `06d1091a…dd7e` and CHANGE-INVENTORY-r2 is `421f8a45…5472`.
- review-r1 is `268d8f33…2eac`, READING is `1d3c54c6…fd8d` and DESIGN-v6.0e is `4024a31c…5205131`.
- `main` is still `9deb6956`. #1477's head is still P.
- H..main changes exactly `.claude/settings.json`, `.github/workflows/a1exit-trial-verify.yml` and `AGENTS.md`.

## Verdict: REJECT (revise D402 and the SM:1394 entries only)

Everything else in r2 is acceptable, with the nits below:

- the ledger mechanics;
- item 7 kept exactly as frozen;
- D403 to D409;
- ESC-1 to ESC-4;
- the corrections for B2 and the r1 nits;
- the configuration;
- the side-change records.

One blocking finding remains, in the scientific wording of D402. It is fixable with a few words and at most three
further splices inside SM:1394.

## Blocking finding

### R2-B1. D402 asserts one common sufficient condition, and its open dependencies are absent from the manuscript

The owner set requirements 5 and 6 and the non-strengthening rule. D402 does not meet them.

**D402's new text.** It reads: "they hold under the assumptions of the local spatial/gauge construction of §2.3
together with cubic-group representation theory, and under the conditions marked at each entry."

**Evidence.**

1. **It is a single sufficiency statement, and the entries' marked conditions are incomplete for their own
   derivations** (SM at T1′/H):
   - **Three generations.** The entry marks only H-χ′. Theorem 10 (:456) gives "spin-1/2 sectors, one per SM
     generation, under H-spin′", and its proof (:460) also names light-spectrum selection. This is O-12. I confirmed
     the omission is real at H.
   - **Unique hypercharges.** The entry marks only the exception Y_Q = 0. Theorem 15 (:589) takes as inputs the gauge
     group, the five representations per family and family-universal charges. Its proof (:460) and :555 add "given
     the chiral structure named by H-χ′ with the observed family pattern".
   - **The SU(3)×SU(2)×U(1) group.** Theorem 5 gives U(3)×U(2)×U(1). The reduction to the Standard-Model group
     carries "the separate amplitude-scale-gauge/background-independence premises … and a specified charged matter
     action" (:344, :374), and the quotient needs "additional physical input" (:585).

   "These are theorems on the branch stated in §1 (Tier 2)" covers H-spin′ and H-χ′ through Tier 2. It does not cover
   the family-pattern input or the physical input for the Standard-Model quotient. D402 then states the conditions as
   sufficient. Requirement 5 says: "distinguish them rather than asserting one common sufficient condition".

2. **The open dependencies are not in the manuscript.** r2's own trace records unresolved dependencies:
   - the measure conditions of Lemma 1c and Proposition 4b;
   - the finite-quotient analogue of the Brillouin-zone integral;
   - the d = 3 continuum conditions;
   - the role of A6.

   These appear only in PREREG §32.9 and PROPOSAL §3.3, not in SM:1394. Requirement 6 says: "If any dependency
   remains unresolved, preserve that uncertainty explicitly".

3. **The A1 question.** At X, §2.3 no longer says "S finite under A1": P's D034 removed it under the X-02 rule. D402
   ties the predictions to §2.3's assumptions.
   - Under reading (i) of H's sentence (A1–A6; READING.md finds the text ambiguous), D402 drops finiteness from the
     stated sufficient conditions. For the entries with open dependencies, independence from A1 has not been
     established. That is the strengthening the owner prohibited.
   - D402 does carry the finite-representative forms of Lemma 1c and Proposition 4b, but only by reference, through
     §2.3's "with further hypotheses stated at each step". A reader of SM:1394 cannot see them.

4. **§32.9 says something false.** It states that D402 "does not replace the earlier count by any list of
   assumptions". D402 replaces the count by a reference to §2.3's list (A3–A4, A5–A6, site factorization,
   nearest-neighbour, H-link). The sentence should be corrected.

**Smallest fix**, a proposal; the writer must verify it.

- **D402 new text:** "they rest on the local spatial/gauge construction of §2.3 and on cubic-group representation
  theory, each entry under the further conditions of the theorem cited for it; whether an entry requires finiteness of
  the substratum is not established where that theorem uses the measure conditions of Lemma 1c or Proposition 4b, the
  continuum conditions of the d = 3 selection (§3.2) or, for $1/\alpha_0$, the infinite-lattice Brillouin-zone
  integral of §6.1."
- **Entry splices inside SM:1394.** Each old string occurs exactly once in SM.md at H; I checked.
  - "three generations (chirality conditional on H-χ', §4.8)" → "three generations (spin-1/2 sectors under H-spin',
    Theorems 9–10; chirality conditional on H-χ', §4.8)". This is O-12/D410.
  - "unique hypercharges from anomaly cancellation (apart from the exceptional branch $Y_Q=0$)" → "unique hypercharges
    from anomaly cancellation, given the observed family pattern and family-universal charges (Theorem 15; apart from
    the exceptional branch $Y_Q=0$)".
  - Optionally, mark the Standard-Model quotient's physical input (:585) at the gauge entry.
- **§32.9:** correct the false sentence, and list the open dependencies identically in §32.9 and in the proposal.

Each of these narrows the statement, so none can strengthen a claim. They lie inside the sentence that the owner's
option (c) authorizes rewriting. I recommend including D410: requirements 2, 5 and 7 cover it, and the owner confirms
it when approving the next revision.

## Per-prediction A1 conclusions (my independent trace, read from proof text at H and T1′)

| Prediction | Derivation read | Uses finiteness of the substratum? | Open or omitted conditions |
|---|---|---|---|
| Gauge group, (3,2,1) | Theorem 7 (:374–376): characters of O on six links, Schur (kernel `theorem_7`); Theorem 5 (:340): Schur under H-link + H-cust | **No use found** (verified at the proof steps). Theorem 7 is lattice-free representation theory. Theorem 5 assumes H-cust. | H-cust's kinetic clause is "a theorem at the symmetric point (Proposition 4b)" (:374). Proposition 4b takes the counting measure on a finite representative, or its H-blind extension (:334), so a discharged H-cust carries that condition. The entry assumes H-cust, so it is explicit. The Standard-Model quotient's physical input (:344, :585) is not marked. d = 3 enters through the Corollary (:210): A4, E5–E7 and the continuum step (census D20 W). The filters as written (the Weyl tensor, stable matter) use no finiteness. |
| Three generations | Theorem 8 (:434–436): 8 BZ corners into 1 ⊕ 3 (kernel `theorem_8`); Theorem 2 (:286); Theorems 9–10 | **No use found.** The corner combinatorics and the staggered identity hold on ℤ³ (the SM:222 scope; Q1 record). | H-spin′ is not marked (real, O-12). Theorem 8b (:440) concerns taste couplings and is not used for the count, so r2's listing of Lemma 1c here is over-cautious, not wrong. |
| One Higgs doublet | Theorem 11 (:464–468) | **No**: it is an input | none |
| Unique hypercharges | Theorems 14–15 (:575, :589): anomaly algebra | **No** (algebraic) | family pattern, five representations, family-universal charges and H-χ′ are not marked at the entry |
| 1/α₀ = 23.25 | §6.1 (:681–687): N_f = 6, T(R) = 1/2, a one-loop Brillouin-zone integral | **No use found.** The integral is over the infinite lattice. | finite-quotient analogue; the normalization of μ (whether Lemma 1c is involved) |
| ħ = c³ε²/(4Gσ) and Bekenstein–Hawking 1/4 | GR:58, GR:88, §5 (:312–322) | **Yes**: H-count, "including finiteness of the total system and the conserved energy shell" (GR:88 at T1′; "including A1" at H) | D403 carries it correctly. Nit: GR:88 also names H-Hawking explicitly and "selection of the physical slope remains an additional condition". |

**Is r2's "no use of A1 found" correct?** Yes, for the gauge, generation, Higgs, hypercharge and 1/α₀ entries,
traced to proof steps. **Are the four open dependencies real?** Yes, all four.

- **H-cust via Proposition 4b** (:334, verified).
- **Lemma 1c's measure.** Its alternatives at T1′ (:252) are the counting measure on a finite representative, a
  structured prior, or H-μ(φ,Θ) on ℤ^d. r2's §32.9 table omits the ℤ^d alternative; that is a nit.
- **The Brillouin-zone integral** (:683–689).
- **The d = 3 continuum conditions** (:208–210; census D20 W).

**D403** is a correct narrowing relative to H, which named only H-slope. I verified that it matches GR:88 at T1′,
apart from the two nits above. D403's new text does not match P's `PTR` pattern: "finiteness of the total system" is
not "finite total system".

**D404–D409** preserve meaning exactly.

- The named list equals ch09:36's "six properties developed in Chapter 5", namely isotropy, sublattice structure, link
  content, anomaly cancellation, taste content and generation count. I verified it verbatim at T1′.
- The set has six members and no finiteness.
- At H, ch19:212 listed A1 apart from these properties.
- Each FULL record mirrors its chapter record byte for byte. `--static` mirror parity gives 0.

## Review focus 1: r1 findings

- **B1:** resolved. The r1 claims are withdrawn, and the owner's option A supersedes the open-item handling.
- **B2:** resolved. §32.7 now says that a post-F class is inadmissible and that a class frozen at F has a hash cycle.
  O-9 is opened. Both A and C′ are conditional on it. v6.0e leaves sec. 13.1 and 13.3 unchanged on this point (lines
  2455–2470, 2538–2541), and the owner has deferred O-9.
- **N2:** kept as O-4.
- **N3:** corrected.
- **N4:** resolved: the DR, resid and reviews are removed, and `checks.item7` is the frozen-item placeholder.
- **N5:** resolved.
- **N6:** resolved. §32.4 states that the T1′ real-tree controls are not acceptance inputs, and §32.5 adds the
  provenance.
- **N7:** stated as a reading, with O-11.
- **N8:** resolved.
- **Q7:** the foreseeable records are now added.

## Review focus 2: item 7 is literally unchanged

- §32.4 row 7 reads "as frozen (§11 item 7)".
- The PREREG is a pure append (P's PREREG is a byte prefix).
- `checks.item7` is a placeholder that names the frozen wording. No restatement, exception, DR or resid remains.

**Re-run** (`item7.py`, output `item7.out`). This is my own implementation of the frozen wording, over `papers/*.md`
and `book/*.md` of H with the proposed 407-splice ledger.

- The pointer grep finds 4 lines. All 4 are the "(A1)" anomaly labels: appB:235 and :246, and FULL:5914 and :5925.
- The count grep finds 0 lines.
- Result: **PASS**.

Negative controls, each **FAIL** as required:

| Control | Result |
|---|---|
| NC1: SM:1394 phrase reinstated | count 1 |
| NC2: ch09:137 "six structural" reinstated | count 1 |
| NC3: "Fourteen items" added | count 1 |
| NC4: bare "(under A1)" added to SM:1394 | pointer finds 1 line that is not a false positive |
| NC5: "sixth of" added | count 1 |

**Nit.** LEDGER.md:304 names only appB:235 and :246. The FULL mirrors count as false positives by the ledger's mirror
convention. Row 7 should say so in one clause, so that the tool form chosen later does not widen the clause.

## Review focus 5: ledger mechanics

I rebuilt everything independently in my own sandbox `review-r2/sb`:

- P's checkers, PREREG r2 and the sitemap at H, which matches `586c526b…`.
- `edits.json` as P's edits plus the 8 records. P's file round-trips byte-exactly, and the result is sha256
  `8b46a8f4…`, equal to the writer's.

| Check | Result |
|---|---|
| `preserve_check --build-ledger` | 407 splices in 44 files, sha256 `a52ab365…`, equal to the writer's |
| P's 399 splices | all identical in the new ledger |
| `edits_check --static`, `--commit H --simulate`, `--pins` (uniqueness: 409 edits, 0 fail), `--repo-scan --simulate --final` (0 unexplained), `--self-test`; `preserve_check --verify-ledger` (re-derived identically; pin findings 0 with §32.10), `--self-test` | all exit 0 / PASS |
| New splices | the 8 splices equal the writer's `LEDGER-new-splices`; each old string occurs exactly once at H |
| `files` entries | change only for SM, ch09, ch19 and FULL |
| TeX diffs against T1′ | confined to the edited paragraphs plus the source stamp. The stamps equal my rebuilt SM.md `c4d01e0e…` and FULL `9f419aae…` |
| Pin parsers | both read 6 equal rows; the last heading is §32.10 of 13 |
| duplicate_check | OK |

Gaps I closed beyond r2:

- **`coverage_check.py`** on an H export with only D402–D409 applied: OK, 132 statements, identical to H. No coverage
  fingerprint is affected.
- **`claims_check`, `voice_check`, `dependency_label_check`, `baseline_label_check` and `citation_roles_check`:** the
  same output as at H.
- **`staleness_check`:** STALE for SM and book. This is expected, because the TeX is regenerated at execution.

**Authorization.** c.7093128173 says: "No change to … the 399 ledgered splices or any scientific conclusion is
authorized". The 399 splices are unchanged. D402 and D403 do change a scientific statement, by narrowing it.
OWN-A authorizes preparation only. The §32.9 placeholder must therefore quote an owner decision adopting D402 to
D409/D410 that expressly supersedes that clause. The §32 preamble's "which adds eight edit records" should be
attributed to that adoption decision.

## Review focus 6: ESC-1

v2 carries W2-a and W2-b, each identical to v1 apart from `recorded_at`, which is H. At top level only `author`,
`recorded_at`, `status` and `supersedes` differ.

- `file_widening(v1, v2)` returns `[]`.
- Removing an allow rule is not on v6.0e's widening list.
- The S1 lint gives 0 problems for v2 as proposed.
- The four W2 fingerprints reproduce sentence and context at T1′, H and main (`esc1.out`).
- The change is valid and not a widening. The question whether the predecessor v1 must pass its own fingerprint lint
  at T1′ remains O-4.

## Review focus 7: O-9, A/C′ and the side-change records

- **A and C′ against v6.0e.** Both correctly depend on O-9. B is invalid. Nothing in v6.0e changes this.
- **The side-change records frozen with F** are correct and minimal. They are classes for `.claude/settings.json` and
  the trial workflow, and a reconciliation for `AGENTS.md`, which is ledgered (sec. 13.3, design sec. 15 item 0).
  They match the H..main path set exactly, by REST compare; the tool's landing paths stay under
  `roles.side_change_classes`.
- **Caveat to state.** These records pin blobs at today's `main`. If `main` changes those paths again before `L`, a
  post-F record, admissible as unforeseen, or a re-freeze is needed.

## Review focus 8: scope

- **No scope creep.** D402 to D409 are within OWN-A.
- **Missing:**
  - the R2-B1 entry conditions, including O-12/D410;
  - the open dependencies stated in SM:1394;
  - consistent open-dependency lists between §32.9 and the proposal;
  - Lemma 1c's ℤ^d alternative and Proposition 4b's H-blind route in §32.9;
  - dropping Theorem 8b from the generation row, or marking it "not used by the entry".
- The writer's "coverage not measured" is now measured: no effect.

## What I re-ran, and how I verified it

**Verified by computation:**

- the manifest and input hashes;
- the PREREG pure append and the §32 extract;
- the edits.json reconstruction and its hash;
- the ledger build and hash;
- the 399-splice identity, the uniqueness of the new splices and the `files` entries;
- P's static, simulate, pins, repo-scan, both self-tests and verify-ledger;
- item 7 and its 5 negative controls;
- the TeX stamp hashes;
- the pin parsers and duplicate_check;
- coverage, claims, voice, dependency and baseline label, citation roles and staleness;
- ESC-1's lint and widening;
- the REST state;
- the uniqueness of the suggested fix strings.

**Verified by reading proof text:** SM at H and T1′, :222, :232, :252, :334–344, :374–376, :432–468, :543–591 and
:679–689; GR:58, GR:88 and §5; ch09:36 and :137.

**Inferred:** that the d = 3 filters use no finiteness, and the μ normalization of 1/α₀. Both are stated as open.

**Not run:** `guards_check` and SC-42, which are gate items.

## Files (`review-r2/`)

- `review.md` (this review)
- `item7.py` and `item7.out`
- `ledger_cmp.out`
- `esc1.out` and `lint_v2r1.py`
- `build-ledger.out`, `static.out`, `simulate.out`, `pins.out`, `reposcan.out`, `verify-ledger.out`,
  `selftest-*.out` and `rc.out`
- `pins_check.out`
- `cov_H.out` and `cov_newonly.out`
- `gate_tools.out` and the `*_tree*.out` files
- `sb/`, the sandbox plan directory
- `work/`, copies of P's files

`tree/` and `treeH/` are scratch exports and are not in the manifest.
