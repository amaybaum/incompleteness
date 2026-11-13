# NOTES-r1: working log for G3 unit 1

## 1. Pins

- Source snapshot: `main` = `c3b5f37a354bb26437e2e0165c576a347a63c153` (committer date 2026-11-13 10:53:49 +0200).
  The branch `research/g3-offset-873-20261113` was checked at the same commit. It was read only, with
  no fetch, edit or gc.
- `verification/ROADMAP.md` was last changed on `main` at `5d4a565b6ba8924bc22d4a599d472833e62a7941`.
  The G3 row is at :85 on `c3b5f37a`. Issue #873's body cites L75 and L1184–L1190 at `9613b21c`. The
  text is the same and the line offset differs.
- Planning and authority, read through the GitHub REST API:
  - Issue #873, body (created 2026-10-18).
  - c.6600178826 (`amaybaum`, 2026-11-03T09:37:45Z): the obligation carried in the Issue.
  - c.6859060590 (`amaybaum`, 2026-11-13T16:40:09Z): owner selection, the question, and items 1–5.
  - c.6859687612 (`amaybaum`, 2026-11-13T17:07:37Z): item 1, "Authorize, start now (Recommended)",
    paper-only; Claude is the writer.
- Accepted W1-1 record: `verification/programmes/physical-realization/w1-1-20261112/W1-1-REPORT-r4.md`.
  Its standing is set out in `STATUS.md` in the same directory.

## 2. Searches before any absence claim (§A.19)

**Lean trees.** `verification/lean/` holds 6 `.lean` files and `verification/lean-mathlib/` holds 240.
The searches were case-insensitive, over `*.lean`:

- `stress.?energy`, `einstein`, `bianchi`, `cosmolog`, `vacuum`, `zero.point`, `energy origin`,
  `energy.shift`, `common shift`, `additive (energy|shift)`;
- `clausius`, `unruh`, `raychaudhuri`, `jacobson`, `bekenstein`, `hawking`, `area law`, `gravit`,
  `metric tensor`, `E₀`;
- `ricci`, `curvature`, `newton`, `poisson`, `first law`, `temperature`, `heat `, `boltzmann`,
  `equipartition`, `conserved energy`, `energy function`, `real energy`;
- `hbar`, `ℏ`, `action scale`, `tauK`, `τK`.

Results:

- The energy-origin hits are in BohrFrequency, AntiunitaryInvariance, CongruentReconstruction,
  PairIdentification, ThermalOrientation and OrientationSelection, and are inventoried.
- `HexLatticeGas.lean:102` states that it bears on nothing gravitational.
- `GradientLinkFlatness` matched on "curvature" only in the gauge-holonomy sense.
- `OI_Regulator_Symmetry.lean` matched `Λ` only as the exterior power `Λ²ℝ⁴`.
- There are no gravity, stress-energy, horizon-thermodynamics or real-energy declarations.

**Census registry.** `verification/lean-manuscript-census.json`, family "Hamiltonian reconstruction",
lists BohrFrequency, AntiunitaryInvariance, ThermalOrientation, ShellAssignment, PairIdentification
and CongruentReconstruction. No family concerns gravity.

**Papers, book, ROADMAP and verification records.** Patterns searched:

- `G3`, `W1-0`, `vacuum energy`, `cosmological constant`, `zero-point`, `stress-energy`, `T_{\mu\nu}`,
  `Bianchi`;
- `energy origin`, `common shift`, `energy shift`, `energy zero`, `choice of energy`, `vacuum offset`,
  `uniform offset`;
- `unimodular`, `trace-free`, `sequester`, `Lovelock`, `integration constant`, `rho_C`, `global phase`.

"G3" is overloaded in the corpus:

- the gravitational ladder rung (GR:12) is the sense used in this unit;
- Structure:154 uses it for a gauge-hierarchy level;
- Main:228 uses (G3) for the nonvanishing-overlap genericity condition.

**Records found and read.**

- `verification/audits/manuscript/corpus-consistency-20261026/AUDIT.md` §2, lines 258–380. Item 2.1
  records that GR:352 refutes inferring decoupling from quantum invisibility. Item 2.9 records that
  the phase-transition vacuum energy is not decided by the relative/absolute rule.
- W1-1 r4 §§8–10.
- No record on `main` constructs the GR:352 countermodel or states the target proposition separately.
  That is a negative finding, made after the searches above.

**Book.**

- The two-completion sentence appears only at GR:352 and in its paraphrase at Introduction:161.
- book/ch07-gravity.md:177 states the geometry-first proposal as conditional and does not carry the
  pair.
- The same search found no contradiction with GR:352 in `FULL.md`.
- No propagation is requested; this unit changes no manuscript.

## 3. Reading log (file:line at `c3b5f37a`)

- `papers/GR.md`: 1–35, 36–93 (§2, including :58 H-count, :70 intertwiner, :74 H-slope, :78 gap
  equation, :84–86), 160–200 (§3.2 end, §3.3), :292, 320–366 (§6), 368–414 (§7.1), 414–470 (§7.2,
  §7.3 start), 555–610 (§8.1–8.4), :633, :655, :689–697, :701, :743–752.
- `papers/Main.md`: :50, :62, :228, :242, :258, :340, :654.
- `papers/Introduction.md`: :155–161, :185, :244, :258, :286, :288.
- `papers/SM.md`: :140–148, :160–166, :292, :811, :1540–1550.
- `papers/Substratum.md`: :296, :375. `papers/Structure.md`: :150, :407–431, :471.
- `book/ch07-gravity.md`: :167–207. `book/ch02-substratum.md`: :158.
- Lean, statements read in full:
  - `BohrFrequency.lean`: 1–80, 180–315.
  - `AntiunitaryInvariance.lean`: 1–60, 140–307.
  - `ThermalOrientation.lean`: 1–110, 190–360, 372–480.
  - `CongruentReconstruction.lean`: 248–265.
  - `PairIdentification.lean`: 292–318.
  - `ShellAssignment.lean`: header and declaration list.
  - `CompletionAction.lean`, `DimensionalObstruction.lean` and `DimensionalCountermodel.lean`: headers,
    which are not about gravity or action scale.
- `verification/ROADMAP.md`: :70–90, :1190–1225.

## 4. Decisions in drafting

1. **Countermodel form.** The constant `Λ₁` is adjusted, rather than the pair being kept with an
   identical constant, so that the partition is shared exactly (§3.1, §3.3). The alternative,
   relabelling `T^cl`, is equivalent and is recorded in §3.3.
2. **The emergent offset functional** is `e(r) = tr(ρΩ_r)`. It is shift-equivariant for every
   normalized `ρ`, and invariant under the D-gauge and under unitary conjugation of the
   representative's frame. The alternatives, the ground eigenvalue or `tr Ω/m`, behave the same way.
3. **(SI) is stated at fixed classical data** because of the offset-provenance observation, F4.
4. **The verdict is "counterexample" rather than "conditional".** The question asks whether the existing
   results imply decoupling. The countermodel answers no. The conditional routes go under "routes", per
   the brief.
5. **Scope guards.**
   - No Λ magnitude claim.
   - The `10^122` relation is treated only as GR:362's dimensional identity.
   - F5's factor 2 records two absolute assignments. It is not offered as a contradiction or as a
     magnitude claim.
6. **No computation and no Lean build.** The repository checks `claims_check.py`, `staleness_check.py`
   and `voice_check.py` were not run. They scan the manuscripts, which this unit does not change. The
   deliverable was scanned by hand for path strings and history-voice phrases.

## 5. Open questions for the owner

- **Q1 (GR:352 notation).** Is `𝒢` in GR:352 meant to include a free constant term? Read with the same
  `T^cl` and the same constant, the pair does not share the partition for `ρ_C ≠ 0`, because the de
  Sitter radius changes. Three readings make the sharing claim exact: a free constant in `𝒢`, a
  relabelled `T^cl`, or `ρ_C = 0` (§3.3). Should a later, separately authorized manuscript unit state
  the qualifier?
- **Q2 (target form).** Adopt (SI) at fixed classical data as the unit's target proposition, with
  offsets induced by classical changes (F4) tracked separately as assumption-watch AW-prov?
- **Q3 (F5, absolute horizon energies).** GR:58 uses `E = c⁴R/G`. GR:422–426 uses
  `E_s = S_dS k_B T_cl = c⁴R/(2G)`. Which is W1-0's "energy of the horizon first law"? Should F5 go to an
  independent review before any manuscript consideration?
- **Q4 (unit 2 choice).** Options:
  - (a) O1, the shift-equivariance of the G3 trace sector `ℱ`;
  - (b) whether the substratum fixes a spacetime volume element (motivation for R2);
  - (c) the transport of the origin `E_0` under W1-0 and the intertwiner GR:70, GR:86;
  - (d) close the unit after review.
- **Q5 (F7).** Record the BohrFrequency.lean:7 docstring name mismatch in an Issue, or leave it to a
  future authorized Lean-maintenance unit?
- **Q6 (review).** The authorization calls for an independent non-author review and then the
  ChatGPT exact-head review. Who is the reviewer, and which draft PR carries this record? The
  authorization names "A draft PR linked here"; none has been opened by this writer.

## 6. Limits of this record

- The derivations are by hand and are not machine-checked.
- Literature is recalled and no verdict rests on it.
- The §A.31 fixed point (three to four passes with no NEW finding) is not reached: there was one pass
  per branch, with one NEW candidate (F4).
- The countermodel is stated in the continuum. The discrete transfer is argued only at the level of a
  linear source map (§4).
