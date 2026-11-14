# NOTES-r2: working log for G3 unit 1, revision 2

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153` (committer date
  2026-11-13 10:53:49 +0200).
- **Branch.** `research/g3-offset-873-20261113` was fetched by name, with no `--depth`.
  - `e64b9a3c` holds r1. It adds `G3-UNIT1-r1.md` and `NOTES-r1.md` under
    `verification/programmes/gravity/drafts/g3-offset-coupling-20261113/`.
  - `5fe230cd` adds `REVIEW-r1.md` (REVISE).
  - The working copy of r1 is byte-identical to `e64b9a3c:…/G3-UNIT1-r1.md` (checked with `diff`).
- **Authority.**
  - #873 c.6859060590 (`amaybaum`, 2026-11-13T16:40:09Z).
  - c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z), unit 1, paper-only.
  - The coordinator's instruction to write r2 is a session message. It is not an owner record.
- **Other records.**
  - W1-1 r4: `verification/programmes/physical-realization/w1-1-20261112/W1-1-REPORT-r4.md`.
  - Corpus-consistency audit: `verification/audits/manuscript/corpus-consistency-20261026/AUDIT.md`.

## 2. Searches (§A.19)

r2 carries r1's search set, recorded at NOTES-r1 §2, with these additions.

- **The `Λ` sentence (N-1).** `Λ` occurs in 22 `.lean` files. Each instance re-checked denotes a region
  `Finset` (`SecondOrderDrive.lean`:59, :361), a matrix (`MinimalRepertoire.lean`:21) or the exterior
  power (`OI_Regulator_Symmetry.lean`:21 and :174 onward). None denotes a cosmological constant.
- **OrientationClosure.lean** carries `E₀` at :135–141 and :256–265, in reflection form only. It was
  missing from the r1 hit list.
- **New corpus anchors read for B5:**
  - GR:342, which states that the ordering "is forced by the logical structure of the derivation
    through three independent requirements";
  - GR:344, :346, :348;
  - GR:358 and GR:400 (Readings 1 and 2);
  - book/ch07-gravity.md:183 and :187;
  - GR:585 (recurrence).

## 3. Re-check of changed citations at `c3b5f37a`

Each line below was read at `c3b5f37a`. Its content matches the use in r2.

| Source | Lines |
|---|---|
| GR | 12, 40, 52, 58, 62–66, 70, 74, 78, 84, 86, 88, 162, 172, 292, 332, 334, 336, 340, 342, 344, 346, 348, 350, 352, 356, 358, 362, 374, 400, 422–426, 466, 573–579, 585, 633, 655, 693–697, 745–751 |
| Main | 62, 228, 242, 340 |
| Introduction | 157, 159, 161, 244, 258, 288 |
| SM | 144–148, 160, 162, 292, 811 |
| book/ch07-gravity.md | 183, 187 |
| AUDIT.md | 55, 371–378 |
| W1-1-REPORT-r4.md | 140, 298, 301, 346–351 |
| ROADMAP.md | 85, 1194–1198, 1214–1219 |

Lean declarations and lines:

| File | Lines |
|---|---|
| BohrFrequency.lean | 8, 9, 146, 201, 215, 235, 265, 279, 291 |
| AntiunitaryInvariance.lean | 152–157, 201, 244, 285 |
| CongruentReconstruction.lean | 251 |
| PairIdentification.lean | 296, 446; `hW` at 448 |
| ThermalOrientation.lean | 66, 76, 192, 195, 239, 256, 318, 336, 356, 403, 472 |
| ShellAssignment.lean | 69, 104 |
| OrientationClosure.lean | 135–141, 256–265 |
| SecondOrderDrive.lean | 59, 361 |
| MinimalRepertoire.lean | 21 |
| OIBridge.lean (imports) | 86, 93, 95, 96, 97, 284 |

## 4. Decisions in drafting r2

1. **The offset functional.** `e(r) = min_a E_a` replaces `tr(ρΩ_r)`. This corrects NOTES-r1:104–105,
   whose remark that the alternatives "behave the same way" holds for the shift only.
   - `min_a E_a` does not depend on the state or the gaps.
   - It does respond to the antiunitary branch.
   - No shift-equivariant functional is reflection-invariant [A].
   - "Differ only" is therefore scoped to the oriented branch.
2. **B5.**
   - GR:346's argument is read as a statement about the order of derivation.
   - For the uniform term, the origin is not a QM output (K1, K5–K7). On shell, K_cpl determines the
     origin from the metric. So the loop GR:346 excludes does not close through that term.
   - This step is new reasoning and is flagged for review.
3. **Classes.** 𝒞_div and 𝒞_tf are kept apart, so that the countermodel class and the R2a class are
   never conflated (B-2).
4. **Verdict category.** It stays "counterexample", conditional on B5's finding. The alternative
   verdict under (ii-S) is stated explicitly in §0.
5. **Checks.**
   - No builds or computations were run.
   - The repository checks were not re-run by this writer. The review records them passing at `e64b9a3c`,
     and they do not scan drafts.
   - Both new files and RESPONSE-r1.md were scanned by hand for path strings and history-voice phrases.

## 5. Open questions for the owner (updated)

- **Q1. GR:352 notation.** Does `𝒢` include a free constant? Only a free constant, or a classical-origin
  relabelling of `T^cl`, keeps the content of GR:352. With ρ_C = 0 the claim is empty. Should a
  separately authorized manuscript unit state the qualifier?
- **Q2. Target form.** Should the unit adopt both (SI) at fixed classical data and the solution-level
  (SI′) as its target propositions, with offsets induced by classical changes tracked as AW-prov?
- **Q3. GR:426.** This question is restated after S-7. Should GR:426's attribution of `ρ_s = ρ_crit` to
  "Jacobson's Clausius relation" be reviewed in a separately authorized manuscript unit? The integrated
  Clausius energy gives `2ρ_crit`. The value `ρ_crit` follows from the product definition
  `E_s = S_dS k_B T_cl`.
- **Q4. Unit 2.** Options:
  - (a) O1 as restated: invariance of the G3 equation's T- and Λ-sector on solutions, with
    conservation carried;
  - (b) the selecting datum in R2a: whether the substratum metric, as classical data, fixes the
    integration constant independently of `r`;
  - (c) transport of `E_0` under W1-0 and the intertwiner at GR:70 and GR:86;
  - (d) close the unit after review.
- **Q5. Docstring mismatches.** The two mismatches in BohrFrequency.lean (:8 and :9) need a
  disposition: an Issue, or a later authorized Lean-maintenance unit.
- **Q6. Review routing.** Review r2, or the delta from r1 to r2, before the ChatGPT exact-head review?
- **Q7. New: route R0.** Adopting the strong reading (ii-S) of requirement (ii), which corresponds to
  GR:400's Reading 2 for the source, would give (SI) for the uniform term conditionally.
  - It is a premise decision under §A.29.
  - Its stated cost is the removal of GR:400's Reading 1 and of the feedback at GR:358.
  - Does the owner want it posed? Or should GR:400's non-adjudication stand?
- **Q8. New: B5 argument.** The argument that GR:346's non-circularity does not reach the uniform
  term (origin not a QM output; on shell, metric → origin) is new reasoning. It should be checked
  specifically by the reviewer.

## 6. Limits

- The derivations were done by hand and are not machine-checked.
- Literature is recalled, and no verdict rests on it.
- The fixed point of §A.31 is not reached.
- The countermodel is stated in the continuum. A discrete transfer is argued only for linear source
  maps.
- B5 is a reading of a paper argument and holds at the [P] level.
