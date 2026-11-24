# A1 plan amendment proposal, revision 2

This revision covers ESC-1 to ESC-4, the dependency on P, items P1 to P5 and P8, and item 7 kept as frozen with edits
D402 to D409.

## 0. Status

**Provisional.** This proposal depends on the reduced tool design. Its current draft is v6.0e, sha256
`4024a31cd2cde06763cb529eafeb023078c52dfa7a5d5fb377995373ab205131`, still under review. The design's implementation
does not exist yet. The proposal stays provisional until the final design is adopted and its implementation verified.
Every statement here about engine behaviour was read from the S1 implementation (`443e871f`) and must be re-checked
against the final implementation.

**Paper-only.** No repository file was changed, and nothing was committed, pushed, opened, dispatched, commented or
merged. This proposal amends, freezes and re-freezes nothing. It runs no trial and changes no premise. Every check
below was run in a local sandbox copy of the plan directory, reading git objects only.

**Answers.**

- Review r1 (`review-r1/review.md`, sha256 `268d8f330e4a8ff210f8ad4b0d998914ab270ddf5e45581e45776a8467212eac`,
  REJECT on B1 and B2).
- The owner's decisions of 2026-11-24 on item 7 and SM:1394, quoted in §3.
- `CHANGES-r1-to-r2.md` maps every change to its source.
- The r1 files are unchanged.

**Owner instructions** (owner `amaybaum`, 2026-11-24, in session; not yet recorded on GitHub), quoted:

> "Select option A: preserve item 7 exactly as frozen and resolve the ambiguous manuscript wording.
> For the three book sentences, name the Chapter-5 structural properties explicitly, preserving their existing
> scientific meaning.
> For SM.md:1394, select option (c): rewrite the sentence to state the actual mathematical dependencies of the
> predictions.
> Requirements:
> 1. Trace the predictions referred to in SM:1394 to their supporting derivations.
> 2. Identify which assumptions and additional hypotheses those derivations actually require.
> 3. Determine whether A1 is genuinely required.
> 4. Do not automatically substitute A2–A6 for A1–A6.
> 5. If different predictions have different dependencies, distinguish them rather than asserting one common
>    sufficient condition.
> 6. If any dependency remains unresolved, preserve that uncertainty explicitly.
> 7. Include the proposed edits and all affected mirrors in amendment proposal r2, with independent review.
> Keep item 7 unchanged. Preserve the frozen plan and original trial evidence.
> This authorizes paper-only amendment preparation, not amendment execution or re-freezing."

> "The important question is not what the original author intended by 'six structural properties,' but what the
> derivation actually requires. [...] we must not automatically replace A1–A6 with A2–A6. That could strengthen the
> scientific claim by asserting that the predictions hold without A1, when that independence has not been
> established." "ensuring that removing A1 does not silently strengthen claims elsewhere in the framework."

**Goal link (§A.47).** A1-EXIT (#1169). This proposal prepares, for the owner's decision:

- the amendment by which every §11 check, item 7 as frozen included, can pass at a new freeze;
- the manuscript edits that make item 7 pass without changing it.

**Independent review.** Pending. A non-author reviewer must review all of r2, and in particular the scientific content
of D402–D409 (§3.3, §3.4).

## 1. Summary

| Item | r2 | Recorded scientific values changed |
|---|---|---|
| Item 7 | **Kept exactly as frozen** (owner, option A). It passes at a tree built from the extended ledger: the count grep finds 0 lines; the pointer grep finds only the four "(A1)" anomaly labels that the ledger names as false positives. Negative controls fail as required. | none |
| D402–D409 (new) | 8 edit records, giving 409 records and 407 splices in 44 files. The 399 existing splices are byte-identical. | Manuscript text at 4 sites, mirrors included. SM:1394 gains H-count, H-frame, local boost structure and the detailed-balance ratio for the ħ and Bekenstein-Hawking relations. This is a narrowing: GR's own conditions are carried. |
| SM:1394 A1-dependence | Traced per prediction (§3.3). The gauge, generation, Higgs, hypercharge and 1/α₀ entries use no finiteness of the substratum in the derivations cited, with four open dependencies named. The ħ and Bekenstein-Hawking relations **do** use it, through H-count (GR:58, GR:88). | — |
| ESC-1 | v2 carries **W2-a and W2-b only**, at H. W1-a to W1-d are no longer needed: no count-literal line remains. Removing them is not a widening. | none |
| ESC-2 to ESC-4 | As r1; no record change | none |
| Dependency on P / B2 | `F` must be reachable before `L`. Arrangements A and C′ both depend on O-9. | none |
| P1–P5, P8 | §32-r2 (`diffs-r2/PREREG-append-s32-r2.diff`); configuration r2 (`diffs-r2/CONFIG-staged-draft-to-r2.diff`; r1→r2 in `CONFIG-r1-to-r2.diff`) | none |

**Withdrawn from r1 and r2-draft.** r1's recommendation O-1(a), the design-note-1 check, the narrower exception
option, the DR-1/3/4/5 and `resid` profiles with their rule files and reviews, and every restatement of item 7.

## 2. Facts from r1, confirmed by the review

V1–V12 of r1 were reproduced by the review r1 (Q1–Q5).

**Correction to V6 (N3).** The S1 ambiguity scan covers the configuration's directory, plus the common parent directory
of every referenced record, here `verification/audits/foundations/`.

## 3. Item 7 kept as frozen; edits D402–D409

### 3.1 The frozen wording

`PREREG.md` at P, lines 4631–4632:

> 7. Corpus grep for `\bA1\b`, "total-finiteness", "posit (ii)", "item (ii)", "finiteness posit": only the ledger's
> false positives remain; grep of posit counts ("Fourteen", "six structural", "sixth of"): zero.

Measured at T1′ (RT-I7 agrees):

- "six structural": 7 lines. "Fourteen": 0. "sixth of": 0.
- `\bA1\b`: 4 lines, the anomaly labels of appB:235/246 and their FULL mirrors, which are the ledger's false positives.

### 3.2 The edits

The edit records are in `diffs-r2/new-edit-records-D402-D409.json`, the splices in
`diffs-r2/LEDGER-new-splices-D402-D409.json`, and the full `edits.json` diff in `diffs-r2/EDITS-P-to-r2.diff`
(additions only).

| Id | File | Site at H | Old → new |
|---|---|---|---|
| D402 | `papers/SM.md` | :1394, part 1 | "they hold for every bijection satisfying the six structural properties." → "they hold under the assumptions of the local spatial/gauge construction of §2.3 together with cubic-group representation theory, and under the conditions marked at each entry." |
| D403 | `papers/SM.md` | :1394, part 2 | "hold for the same class as consistency relations conditional on H-slope ([GR §3.2, §4–§5])" → "hold for the same class as consistency relations conditional on H-count, which includes finiteness of the total system and a conserved energy shell, and on H-slope, H-frame, the horizon and frame conditions, local boost structure and the symmetric detailed-balance rate ratio ([GR §2.3, §3.2, §4–§5, §8.5])" |
| D404/D405 | ch09, FULL | ch09:137 (FULL:2552 at H) | "the six structural properties developed in Chapter 5 (" → "the structural properties developed in Chapter 5 (". The list follows unchanged. |
| D406/D407 | ch19, FULL | ch19:198 (FULL:5268 at H) | "(one of the framework's six structural properties of the bijection)" → "(one of the framework's structural properties of the bijection: isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count)" |
| D408/D409 | ch19, FULL | ch19:212, part 2 (FULL:5282 at H) | "The framework's six structural properties of the bijection (developed across Chapters 5-7) further narrow it." → "… structural properties of the bijection (isotropy, sublattice structure, link content, anomaly cancellation, taste content, generation count; developed across Chapters 5-7) further narrow it." |

**Book sentences.**

- They name the set that ch09:36 and ch09:137 enumerate as "the six properties developed in Chapter 5". That set does
  not contain finiteness (the independent reading of SM:1394, sec. 2, and review r1, Q6).
- At ch19:212 (H), the open hypothesis A1 is listed with the axioms, apart from these properties.
- Each set is unchanged; only the bare count is replaced by its members.

**Unique and non-overlapping.** Each old string occurs exactly once in its file at H (the ledger build checks
uniqueness). D408 starts after the end of D184 in the same line, with no overlap (ledger validation: 0 findings).

### 3.3 SM:1394: the dependency trace (requirements 1–6)

Citations are `papers/SM.md` at H unless named otherwise. The evidence layers are:

- **K**: kernel-checked;
- **D**: paper derivation;
- **N**: numerical;
- **R**: a reviewed record on `main` (`verification/audits/foundations/a1exit-q1-20261120/RESULT.md`, Q1, which tests
  whether each lattice theorem holds on ℤ³; `a1-09-dependency-census/CENSUS.md`, D15/D16/D32 and §§13–14).

| Prediction (SM:1394) | Derivation | Layer | Assumptions and hypotheses it uses | Uses finiteness of the substratum (A1)? |
|---|---|---|---|---|
| SU(3)×SU(2)×U(1), multiplicities (3,2,1) | Theorem 7 (:374–376); Theorem 5 (:340); Proposition 14a and its scope note (:579–585) | K (`theorem_7`, `LinkDecomposition.lean`; `QuarterTurn.lean`; `Averaging.lean`) for the decomposition; D for Theorem 5 and 14a; R (census D15: "Six links are finite-dimensional, not a finite universe", A) | d = 3 simple-cubic lattice with nearest-neighbour signed links (:348; posit ledger items (viii), (x)); d = 3 from the Corollary at :210 (A4, E5–E7, continuum conditions); H-link (one copy); H-cust; the additional physical input for the quotient (:585) | **No use found.** Theorem 7 is lattice-free representation theory, and Theorem 5 is Schur's lemma. Open: H-cust's kinetic clause, where Proposition 4b (:334) supplies it, takes the counting measure on a finite representative (ledger X-18, F). The entry assumes H-cust as a premise. |
| Three generations, identical gauge quantum numbers; chirality under H-χ′ | Theorem 2 (:286); Theorem 8 (:434); Theorem 9 (:448); Theorem 10 (:456); Theorem 13 (:543) | K (`theorem_8`, `TasteBranching.lean`); D; R (Q1: C2, C8, C10 step (ii), C12, C13 hold on ℤ³, and A4's finite clause is used by none) | the wave-equation form (A4, A5, nearest-neighbour range; §4.1, :60); d = 3; staggered reduction; H-spin′ (spin labels, Theorem 9); H-link (matter on links, Theorem 10); H-χ′ (Theorem 13); the family pattern as input (:458, :460) | **No use found** (Q1). Open: Theorem 8b (:440) uses the normalized observer-level branch, whose Lemma 1c (:252) takes the counting measure on a finite representative or a stated structured prior. On ℤ³ the ledger names the law condition H-μ(φ,Θ) (X-41), assumed and not adopted. Finding: SM:1394's entry names H-χ′ but not H-spin′, which Theorems 9–10 use (O-12). |
| One Higgs doublet | Theorem 11 (:464–468) | D | taken as input (:468); its accommodation uses Theorems 7 and 9 (H-spin′) | not used (it is an input) |
| Unique hypercharges (Y_Q ≠ 0) | Theorem 14 (:575); Theorem 15 (:589); :555 | D (group algebra) | the gauge group and the five representations per family as inputs; family-universal charges; the six anomaly conditions; Theorem 5 (H-link, H-cust); H-χ′ | **No use found** (algebraic) |
| 1/α₀ = 23.25 | §6.1 (:681–687) | N (a Brillouin-zone integral) and D (one-loop induced action); R (census D32: couplings inherit carrier gaps, W) | N_f = 6 and T(R) = 1/2 (§4.5–§4.6); scalar coupling matrix (Theorems 6–7; Theorem 6 under H-link); one-loop staggered vacuum polarization | **No use found.** Open: the integral is over the Brillouin zone of the infinite lattice, and the finite-quotient sum is not computed. Also open: whether the vertex coupling μ uses the normalized branch, and with it Lemma 1c's measure condition. |
| ħ = c³ε²/(4Gσ) and the Bekenstein-Hawking coefficient | GR:58 (H-count); GR:88; GR:314–316 | D | H-count (a finite total system on a conserved energy shell), H-slope, H-frame, the horizon and frame conditions (GR §8.5), local boost structure, the symmetric detailed-balance rate ratio | **Used.** GR:88 at H reads "requires H-count, including A1 and the conserved energy shell". At T1′ it reads "including finiteness of the total system". The ledger classes it X-70 (F, finite-scoped). An A1-free form exists only in records (P7B), not in any manuscript. SM:1394 at H named only H-slope. |

**The class quantifier.**

- "properties of the equivalence class [(S, φ)]/G_sub" and "They do not depend on which specific φ …" are kept
  unchanged.
- The class itself is that of Theorem 23, which at `X` is stated for finite substrata (ledger X-45, F).
- The rewrite neither widens the class nor states that the predictions hold outside it.

**Requirement 3 (is A1 genuinely required?).**

- For the gauge, generation, Higgs, hypercharge and 1/α₀ entries, no use of A1 was found in any cited derivation. The
  lattice theorems are kernel-checked or hold on ℤ³ by Q1's reviewed record.
- Four dependencies are recorded, not resolved, and stated in §32.9:
  - H-cust via Proposition 4b, if H-cust is discharged rather than assumed;
  - Lemma 1c's measure, for Theorem 8b and possibly for §6.1's μ;
  - the Brillouin-zone integral's finite-quotient analogue;
  - the d = 3 continuum conditions (census D20, W).
- For ħ and the 1/4, A1 is required: finiteness of the total system is part of H-count.

**Requirement 4 (no automatic A2–A6 substitution).**

- D402 replaces the count by a reference to SM's own dependency statement (§2.3, :60). That statement lists the site
  factorization, A3–A4, A5–A6, the nearest-neighbour restriction, H-link, E5–E7 for d, A4, A5 and nearest-neighbour
  range for the wave equation, and "further hypotheses stated at each step".
- It does not name A2–A6 as a sufficient set.
- Its "further hypotheses stated at each step" carry the finite-representative and structured-prior forms of
  Lemma 1c and Proposition 4b wherever an entry rests on them.

**Requirement 5 (distinguish).** The entries keep their own conditions. D403 separates the two horizon relations,
which need H-count with finiteness of the total system, from the rest.

**Requirement 6 (uncertainty).** The four open dependencies above are written into §32.9. O-12 records the H-spin′
omission.

**Non-strengthening, checked by edit.**

- D402 removes no condition from any entry and adds no class.
- D403 adds conditions taken from GR:88, so it narrows the claim.
- D404–D409 keep each set and its six members.

### 3.4 Checks of the extended plan

Run in a sandbox copy of the plan directory (`work-r2/run_all.sh`), with P's own checkers, at H:

| Check | Result |
|---|---|
| Control: P's `--build-ledger` on P's `edits.json` | reproduces `2055e68f…` |
| `preserve_check.py --build-ledger` | 407 splices in 44 files; `ledger.json` sha256 `a52ab365f98150e6f612770245ff29c59cc6edc923cd8c352896940b49750ed8`. `edits.json` sha256 `8b46a8f4c95e606325fcca666b1ed584b3de18acabe4d6bfd7f898587875689c`. All 399 P splices are byte-equal. The `files` entries change for SM, ch09, ch19 and FULL only. |
| `edits_check.py --static` | PASS: infinity, register, capitals and identifier 0; mirror parity 0; sitemap 194/194 |
| `edits_check.py --commit H --simulate` | PASS: 409 unique; residual 5, all allowed; criterion-5 0; identifier and count 0 |
| `--pins --commit H` | PASS |
| `--repo-scan --simulate --final` | PASS, 0 unexplained |
| `edits_check.py --self-test`; `preserve_check.py --self-test` | PASS; PASS |
| `preserve_check.py --verify-ledger`, then `--verify-pins` with the r2 PREREG | re-derived identically; pin findings 0 once §32.10 carries the new digests |
| Item 7 as frozen on H plus the new ledger (`item7_sim.py`) | count grep 0; pointer grep only the 4 false positives; **PASS** |
| Negative controls | reinstated "six structural assumptions", "Fourteen items, …" and the SM:1394 phrase: each **FAIL** |
| `duplicate_check.py` (from `main`) on the 4 edited sources and on the r2 PREREG | OK; OK |
| TeX, built by P's `rebuild_tex` (pandoc 3.1.3; the base control reproduces H's SM.tex and FULL.tex) | SM.tex `aba571c3…` and FULL.tex `5d37cafc…`. They differ from T1′'s TeX only in the edited paragraphs and the source stamp (`diffs-r2/*.tex.t1p-to-proposed.diff`). |

**Not run.**

- `guards_check.py --predict` and `--mutants`: about 20 minutes. They are gate items.
- The coverage check: whether any census fingerprint covers the SM:1394 paragraph is not measured. If one does, the
  coverage-ledger STALE list grows.
- The SC-42 regeneration: the book edits change stored FULL mirror prefixes, so the result regenerates on T0″.
- PDFs.

## 4. ESC-1 to ESC-4

**ESC-1.**

- v2 (`diffs-r2/w1-w2-allow-v2.json.proposed`) carries W2-a and W2-b at H. Their four fingerprints reproduce sentence
  and context at H (V1).
- S1 `file_widening(v1, v2)` returns `[]`.
- O-4's W1-d question no longer arises. Its part N2 remains: whether the predecessor v1 must pass its fingerprint lint
  at T1′.
- If the adopted design requires that, the alternative is a fresh W2 file without `supersedes`. That needs new rule ids
  and a widening review.

**ESC-2, ESC-3, ESC-4.** As r1. ESC-3 is worded per N8.

**§A.42 item 8 trace (N6).**

- `controls.json`'s `agents-md-at-T1p` and `a1_controls.py`'s real-tree controls are evidence about the
  implementation, not acceptance inputs (§32.4, §32.5).
- `dr-deny-v1` and `resid-v1` are no longer referenced by the configuration.

## 5. Reachability and landing (B2)

As in the B1/B2 draft, unchanged by the item-7 decision.

**Requirements.**

- `T` on `main`.
- `F` reachable before `L`.
- `F`'s tree holds the tool's audit directory.

**Correction of r1.** A post-`F` side-change class for the plan directory is not admissible: the plan's merge is
foreseen (design sec. 13.3). A class frozen at `F` would need a hash cycle.

**O-9.** A cycle-free rule is needed, for example: paths under the configuration's directory whose blob at `M` equals
their blob at `F`.

**Arrangements.**

- **A:** merge #1477 after `F` and before `L`.
- **C′:** merge #1477 at the reviewed head `G`, then designate `F = G`.
- Both depend on O-9.
- **B** is invalid.
- §32.7 states the §25.2 landing-diff reading (N7; O-11).
- Item 14's landing part goes through the tool, because `preserve_check --base main` is refused while `AGENTS.md`
  differs.
- The foreseeable `H..main` side changes are frozen with `F`: classes for `.claude/settings.json` and the trial
  workflow; a reconciliation for `AGENTS.md`, written as a first record.

## 6. P1 to P5 and P8

As r1 sec. 5, with these changes:

- v6.0e's workflow wording for P8.
- The configuration's `author` is a placeholder for the writer of this version (N5).
- `checks.item7` names item 7 as frozen.
- The DR/`resid` profiles, rule files and reviews are removed.
- The foreseeable side-change and reconciliation records are referenced.

**§32-r2.** The structure is §32.1–§32.10. §32.9 is the item-7 section and §32.10 is the last `Record pins`
subsection: 13 such headings, 6 rows for both parsers before the placeholders are filled. The PREREG is a pure append.

## 7. Consequences

**The frozen plan.**

- `P` and its seven files are unchanged.
- §31.31 stays `P`'s pins. §32.10 pins the new `edits.json` and `ledger.json`.
- c.7093128173's "No change to … the 399 ledgered splices … is authorized" is superseded only as far as the owner's
  decision of 2026-11-24 directs. That decision is to be quoted with its comment id in §32.9.

**Trials.**

- T0″ and T1″ are rebuilt from the amended plan.
- Their predicted trees contain the D402–D409 text, SM.tex and FULL.tex regenerated, the SC-42 result regenerated, and
  the coverage entries re-affirmed if any is stale.
- The §31.8 expectations for `preserve`, `guards` and `verify.yml` keep their form. The PDF set is unchanged: SM and
  FULL are already ledgered.
- The pre-freeze gate items 1–10 are re-run.

**Acceptance.**

- Item 7 as frozen is expected to pass.
- The scientific review of D402–D409 (§3.3) is a new requirement.

**Existing evidence.** T0′/T1′ of `P` remain evidence of what they tested.

## 8. Open questions for the owner

| # | Question | Recommendation |
|---|---|---|
| O-1 | Item 7 | **Settled by the owner**: kept as frozen, with D402–D409 |
| O-2 | A or C′ (each needs O-9) | none until O-9 is settled |
| O-3 | v2 and the review records in the plan directory | yes |
| O-4 | (N2) whether the predecessor v1 must pass its fingerprint lint at T1′ | for the design reviewer |
| O-5 | Records quoting `F`'s designation | the execution note and the landing record |
| O-6 | `retirement.owner` | remove it |
| O-7 | The delegation contract's location | with the final design |
| O-8 | Independent review of r2, including the science of D402–D409 | required before any authorization |
| O-9 | A cycle-free classification of the plan directory at `M` | for the design reviewer and the owner |
| O-10 | DR/`resid` machinery | **settled**: removed with item 7 kept as frozen |
| O-11 | The §25.2 landing-diff reading | approve it, if A or C′ is chosen |
| O-12 | SM:1394 names H-χ′ but not H-spin′, which Theorems 9–10 use for the spin-1/2 generation sectors | add "spin identification under H-spin′ (Theorem 9)" to the generation entry as a further edit (D410). It narrows the claim, but it is outside the owner's instruction, so it needs the owner's decision. It is not included in the counts above. |

## 9. Verification limits

- The trace in §3.3 reads derivations and the reviewed records Q1 and the census. It is not a new proof. The open
  dependencies are named, not resolved.
- Engine statements come from S1.
- No CI or trial was run.
- `guards_check`, the coverage check, SC-42 and the PDFs were not run.
- The sandbox runs used P's checkers against git objects at H, through read-only `git show` and `ls-tree`.
