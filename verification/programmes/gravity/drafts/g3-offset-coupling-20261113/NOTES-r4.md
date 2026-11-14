# NOTES-r4: working log for G3 unit 1, revision 4

## 1. Pins

- **Source snapshot.** `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153`.
- **Branch.** `research/g3-offset-873-20261113`, fetched by name, with no `--depth`.

  | Commit | Content |
  |---|---|
  | `e64b9a3c` | r1 |
  | `5fe230cd` | REVIEW-r1 |
  | `1aaf87a2` | r2 |
  | `25257ae5` | REVIEW-r2 |
  | `b207fbaa` | r3 |
  | `95681321` | CONFIRM-r3: NOT CONFIRMED (C-1 and C-2 blocking) |

- **Authority.**
  - #873 c.6859060590 (`amaybaum`, 2026-11-13T16:40:09Z).
  - #873 c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z): unit 1, paper-only.
  - The coordinator's instructions are session messages, not owner records.
- **Files.** All r1–r3 files and RESPONSE-r1 and RESPONSE-r2 are unchanged. The r4 files are new.

## 2. Reading for r4

I re-read the following at `c3b5f37a`. The content of each matches its use in r4.

| Source | What was checked |
|---|---|
| GR:358 | feedback "through state-level quantities"; "the zero-point sum" excluded |
| GR:374 | "the emergent vacuum energy is a state-level quantity depending on the hidden sector's volume" |
| GR:400 | Reading 1: the "∼m²H² piece … epoch-differential (relative) effect in the sense of §8.3"; "the substratum budget fixes the constant part"; Reading 2 |
| GR:573 | "there is a classical microstate difference corresponding to this energy difference … Relative differences appear in the classical stress-energy tensor" |
| GR:575 | absolute levels "not a property of the microstates themselves" |
| GR:579 | electroweak and QCD transitions are not fixed by the relative/absolute distinction |
| AUDIT.md:55 | item 2.9 |
| GR:162, :334, :356 | Λ undetermined; its value an input |

## 3. Decisions in r4

1. **C-2 is accepted.** The corpus's use reconciles GR:400 Reading 1 with GR:346 through §8.3, and it
   does not admit K_cpl^conv. Part 2 is therefore "conditional on (ii-L)", not "counterexample".
2. **Added caveat [P].** The piece that Reading 1 feeds back is relative between epochs. GR:579 and
   AUDIT item 2.9 record that the relative/absolute rule does not decide how energy changes between
   epochs couple. The §8.3 classification of that piece therefore rests on GR:400's statement. This
   strengthens the conditionality of the reconciliation and does not change C-2's conclusion.
3. **Two items are separated in O0.**
   - Whether (ii-L) holds against self-consistent fixed points is an open proof question.
   - Whether to hold (ii-L) as a premise is an owner decision.
4. **(DZ)** is a property of the source map (C-3). Statements about pairs `κ, κ′` with equal `T^cl` and
   different `e_Z` are conditional on such pairs existing. Their existence is not shown, and GR:573
   suggests that changes of the gaps appear in `T^cl`.
5. **Checks.** No computation or build was run. The repository checks pass at `b207fbaa` per
   CONFIRM-r3, and they do not scan the drafts.

## 4. Verdict, r4

| Part | Category | Statement |
|---|---|---|
| 1 | Counterexample, for source maps | (SI) is not implied on (ii-W) or (ii-L). It follows conditionally on (ii-S). The witness K_cpl^free is world-equivalent to K_dec with Λ₀ left undetermined. |
| 2 | Conditional on (ii-L), for the coupling with physical content | (DZ) for the convention-fixed offset follows conditional on GR:346's argument (ii-L). The force of (ii-L) against self-consistent fixed points is not established. K_cpl^conv survives only under (ii-W) applied to absolute emergent quantities, which no corpus text adopts. |

## 5. Open questions for the owner (updated)

- **Q1. GR:352 notation.** Does `𝒢` include a free constant? Only a free constant, or a classical-origin
  relabelling of `T^cl`, keeps the content of GR:352. The relabelling is conditional on a covariant
  continuum limit. Should a separately authorized manuscript unit state the qualifier?
- **Q2. Targets.** Should the unit adopt (SI), (SI′) and (DZ)? Under (DZ), the source minus `T^cl`
  has no dependence on `e_Z`. (DZ) carries the contentful contrast at GR:352.
- **Q3. GR:426.** Should the attribution of `ρ_s = ρ_crit` to "Jacobson's Clausius relation" be
  reviewed? The integrated Clausius energy gives `2ρ_crit`.
- **Q4. Unit 2.** The candidates are:
  - (a) whether GR:346's argument (ii-L) holds against self-consistent fixed points. This is the
    smallest proof question that remains for Part 2.
  - (b) O1, as restated.
  - (c) the selecting datum in R2a.
  - (d) transport of `E_0` under W1-0 and the intertwiner.
  - (e) closing the unit after review.
- **Q5. Docstring mismatches.** BohrFrequency.lean lines 8 and 9 need a disposition.
- **Q6. Review routing.** Should the reviewer run a delta check of r3 → r4 against RESPONSE-r3's table
  before the ChatGPT exact-head review?
- **Q7. Route R0** (revised). Should GR:346 as argued (ii-L) be held as a premise under §A.29? Doing so
  excludes K_cpl^conv and gives (DZ) conditionally. It removes GR:400's Reading 1, and the feedback
  stated at GR:358 and GR:374, only if §8.3's identification fails. Otherwise those passages stand.
- **Q8. AW-loop** (revised). The reconciliation of GR:346 with the wording "emergent vacuum energy" at
  GR:358, GR:374 and GR:400 is supplied by GR:400's qualifier "relative … in the sense of §8.3". It is
  conditional on §8.3's identification (GR:573). It is not stated at GR:346. It carries the
  epoch-differential caveat of GR:579 and AUDIT item 2.9. Should it go to a separately authorized
  manuscript unit?

## 6. Limits

- The derivations are by hand and are not machine-checked.
- Literature is recalled, and no verdict rests on it.
- B5 is a reading of paper arguments [P].
- The §A.31 fixed point is not reached.
- The countermodel is stated in the continuum.
