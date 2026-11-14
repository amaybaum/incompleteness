# NOTES-r3: working log for G3 unit 1, revision 3

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch** `research/g3-offset-873-20261113`, fetched by name with no `--depth`:
  - `e64b9a3c`: r1.
  - `5fe230cd`: REVIEW-r1.
  - `1aaf87a2`: r2 (G3-UNIT1-r2.md, NOTES-r2.md, RESPONSE-r1.md).
  - `25257ae5`: REVIEW-r2 (REVISE; R2-1 blocking).
- **Authority.**
  - #873 c.6859060590 (`amaybaum`, 2026-11-13T16:40:09Z).
  - c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z): unit 1, paper-only.
  - The coordinator's instructions for r2 and r3 are session messages, not owner records.
- **Files.** The r1 and r2 files in the working area are unchanged. r3 is new.

## 2. Searches (§A.19)

There are no new Lean searches beyond NOTES-r1 §2 and NOTES-r2 §2. For R2-1, the corpus passages on the
emergent zero-point normalization and on emergent feedback into the cosmological metric were re-read:
GR:332, GR:336, GR:358, GR:374 and GR:400.

## 3. Re-check of new or changed citations at `c3b5f37a`

| Line | Content checked |
|---|---|
| GR:58 | s_H up to an energy-independent constant |
| GR:332 | zero-point `½ħω` per mode to the cutoff |
| GR:346 | non-circularity, "no entry point" |
| GR:358 | "ground-state eigenvalue of Ĥ_eff"; feedback "through state-level quantities" |
| GR:374 | "the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume" |
| GR:400 | Reading 1, Reading 2, "the substratum budget fixes the constant part" |
| GR:422 | `S_dS = σA/ε²` |
| PairIdentification.lean | :296 and :446, with K9's hypotheses as listed in r3 §1.1 |

All other citations are carried unchanged from r2, which NOTES-r2 §3 re-checked.

## 4. Decisions and corrections in r3

1. **Two coupled completions** (R2-1).
   - K_cpl^free uses `e_free = min E` as a free coordinate on the σ-orbit.
   - K_cpl^conv uses `e_Z`, a convention-fixed function of the class.
   - The r2 "on shell, metric → origin" step held only for K_cpl^free, which is world-equivalent to
     K_dec. This replaces the B5 reasoning in r2 (N2:76–78; RESP:49–55). Those passages overclaimed:
     for K_cpl^conv the origin is an output of the emergent description by its own convention, and
     GR:346's loop closes.
2. **The new target (DZ).**
   - K_cpl^conv satisfies (SI), because `e_Z` depends only on the class [A].
   - The contentful contrast at GR:352 is therefore stated as (DZ), the source being constant in
     `e_Z`.
   - The review's "(SI) for the convention-fixed offset" is rendered as "(DZ) for the convention-fixed
     offset" (RESPONSE-r2, precision 1).
3. **N2:71 corrected.** `e_free` does not depend on the state. As a free coordinate on the σ-orbit it
   carries no gap dependence. `e_Z` does depend on the gaps.
4. **N2:73 corrected** (R2-2). "No shift-equivariant functional is reflection-invariant" holds only
   for reflections `E ↦ −E + c` with `c` independent of `E`. Under `E ↦ −E + 2·mean(E)`, the mean is
   invariant. How K_cpl responds to the branch is a convention, so "differ only" stays on the oriented
   branch.
5. **Three readings of (ii).**
   - (ii-S): no post-partition argument.
   - (ii-L): no self-consistent loop through post-partition data. This is GR:346 as argued, and it is
     R0.
   - (ii-W): an entry point exists.
   - (ii-L) is weaker than (ii-S) and suffices against K_cpl^conv.
6. **The verdict** keeps the category "counterexample" in the two-part scoped form that REVIEW-r2
   asks for.
7. **Checks.**
   - No computation or build was run.
   - The repository checks were not re-run by this writer. They pass at `1aaf87a2` per REVIEW-r2, and
     they do not scan drafts.
   - The new files were scanned by hand for barred strings.

## 5. Open questions for the owner (updated)

- **Q1. GR:352 notation.** Does `𝒢` include a free constant? Only a free constant, or a classical-origin
  relabelling of `T^cl`, keeps the content of GR:352. The relabelling is conditional on a covariant
  continuum limit in which a uniform classical energy has vacuum stress. Under ρ_C = 0 the claim is
  empty. Should a separately authorized manuscript unit state the qualifier?
- **Q2. Targets.** Should the unit adopt three targets?
  - (SI): relabelling at fixed classical data.
  - (SI′): solution level.
  - (DZ): zero-point decoupling, which carries the contentful contrast at GR:352.

  Offsets induced by classical changes would be tracked as AW-prov.
- **Q3. GR:426.** Should GR:426's attribution of `ρ_s = ρ_crit` to "Jacobson's Clausius relation" be
  reviewed in a separately authorized manuscript unit? The integrated Clausius energy gives `2ρ_crit`.
- **Q4. Unit 2.** Options:
  - (a) O1 as restated;
  - (b) the selecting datum in R2a;
  - (c) transport of `E_0` under W1-0 and the intertwiner (GR:70, GR:86);
  - (d) the AW-loop tension between GR:346 and GR:400 Reading 1;
  - (e) close the unit after review.
- **Q5. Docstring mismatches.** BohrFrequency.lean :8 and :9 need a disposition: an Issue, or a later
  Lean-maintenance unit.
- **Q6. Review routing.** Should the reviewer run a delta check of r2 → r3 against RESPONSE-r2's
  passage list before the ChatGPT exact-head review?
- **Q7. Route R0** (revised). Should GR:346 as argued (ii-L: no self-consistent loop through
  post-partition data) be held as a premise? It would exclude K_cpl^conv and give (DZ) conditionally.
  It is a decision under §A.29. Its cost is the removal of GR:400 Reading 1 and of the feedback stated
  at GR:358 and GR:374.
- **Q8. AW-loop** (revised; this replaces the r2 question about the B5 argument).
  - GR:346 argues that a QM → metric → partition loop has "no entry point".
  - GR:400 Reading 1, GR:358 and GR:374 admit a loop of that form.
  - Should this tension go to a separately authorized manuscript unit?
  - The F8 class (NEW candidate) is for the reviewer to confirm.

## 6. Limits

- The derivations were done by hand and are not machine-checked.
- Literature is recalled, and no verdict rests on it.
- B5 holds at the [P] level. It is a reading of paper arguments.
- The §A.31 fixed point is not reached.
- The countermodel is stated in the continuum.
