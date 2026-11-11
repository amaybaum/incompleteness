# Bell-scope unit 1 (#868): dispositions of review 5857227567, r1 → r2

**WIP / UNVERIFIED writer record; authorizes nothing.** Review: PR #1231 review 5857227567 (ChatGPT, independent
reviewer, 2026-11-11T10:22:16Z), verdict REVISE, on head `7abf59d76ba363cbad72c7e0764ce3be2a275d06`. Each finding
was checked against `BELL-SCOPE-UNIT1.md` r1 and its proofs before it was applied. Section numbers are those of the
unit.

| # | Finding | Check | Disposition | Where changed |
|---|---|---|---|---|
| 1 | §3.5 item 3 states MI "equivalent" to CF under (M), (GI); Lemma G proves sufficiency only | Correct. Lemma G's proof is one implication. The reviewer's example (generator bits `a, b, r`, response bit `w`, uniform measure conditioned on `r = w`) was re-derived by hand and checked exactly: the event is not a product across generator and response coordinates, `(a, b)` is independent of `w` (probe G6c) | **Applied.** "Equivalent" replaced by "implied by"; a direction paragraph with the counterexample added to §3.3. The weaker "reduces to" wordings, which suggested the same equivalence, were also changed | §3.5 item 3; §3.3; §0 (class description, O3); §1 C3, C4; §2 MI row; §3.1 (MI); §3.4 O3; §6 P-d; probe G6c |
| 2 | §3.4 O2: "physically spacelike wings lie inside the graph cone except along the body diagonals" overstates; only some do | Correct. With *c* the wave speed, a configuration at Euclidean separation `d` along `n̂`, `Δt` updates apart, is spacelike and inside the graph cone only for `Δt/√3 < d ≤ Δt/‖n̂‖₁`; for `d > Δt/‖n̂‖₁` it is outside both cones | **Applied.** §3.4 O2 states the window and that farther-separated configurations meet (Sep) on the nearest-neighbour graph. §0 O2, which the review found accurate, now states the same window explicitly | §3.4 O2; §0 O2 |
| 3 | NBA names Sep and MI, while Theorem N also needs GI and the every-run and menu hypotheses | Correct. As written in r1, NBA ⇒ Theorem N inherited (GI) silently; the r1 remark on generator residues covered the case without (GI) only informally | **Applied.** The remark is now Theorem N′ (no GI; λ* = (Ω, ρ_A, ρ_B); hypothesis (MI\*)) with proof. NBA states its domain (finite jointly admissible menu, every-run outputs with a fixed local failure rule, no postselection, physical separation) and three assertions: (Gen)+(Rec); (Sep) in the actual `G_φ`; and either (GI)+(MI) for Ω or (MI\*) for λ*. The implication to (A) cites N or N′ by case. Lemma G gains the corresponding sufficient condition for (MI\*) | §3.2 (Theorem N′); §3.3 (Lemma G statement and proof); §3.4 NBA; §0 missing-lemma paragraph; §1 C3′, C12; §5 |
| 4 | Tightness: the witness shows optimality over Bell-local tables; tightness inside 𝒞_sep needs a member realizing it | Correct as a statement about r1: no member was exhibited | **Applied, both ways the review offered.** The optimality claim is scoped to MI Bell-local tables. Separately, a member of 𝒞_sep as an abstract class (six-site toy map, uniform measure with a product conditioning event) realizing the witness is given and checked (probe G7). §3.1 constrains the protocol and not the rule, so this shows attainment in the class as defined; it is stated that no member whose map is the native substratum rule is exhibited, and attainment there is open | §4.1; §0 verdict paragraph; §1 C6, C6′; §3.6; probe G7 |
| 5 | §4.4: "exact 2√2 unreachable by rational laws" depends on the preparation law | Correct. Rationality of every probability follows from (M) (ratios of counts); with general real preparation weights it fails | **Applied.** The aside is stated under (M), with the note that it does not apply to general weights and that the bound of §4.1 does not use it | §4.4 |

Also retained as the review asked: findings F1 and F2 reported and uncorrected; O1, O2, O3 kept as separate open
items; the probe described as generic controls, not OI-rule execution.

## Coordinator items

| Item | Disposition | Where changed |
|---|---|---|
| Label "Main posit (iv)" | The unit cites measurement independence as hypothesis (iv) of Main's theorem (O3 wording kept) and says it does not use the survey's label; the C2 row names the hypothesis numbering explicitly | §1 C2; §3.4 O3; §7 cross-check |
| Q-868-H unit 1 status | Row updated: independently accepted at r2a, sha256 `b56ccd9b4c8307e86b187b4dd05fb0de6252b781652690862e91b41f849031e8`, still off `main`. It stays provenance only; no statement of this unit relies on it | §7 table |

## Other changes

- Header: draft r2, review id, pointer to this file; the "no git write" phrase replaced, since the unit is committed.
- §3.6: probe path given relative to this directory; sha256 and check count updated (seventeen checks, G6c and
  G7a–d added). `probes/generic_bell_checks.out` regenerated with `python3 -I -B`, exit 0.
- §7: a row for the review itself (provenance). §8: review state updated.

## Verdict

Unchanged: (C) indeterminate for OI itself; (A) obstruction restricted to 𝒞_sep; (B) not established. No finding
refused. The r2 changes narrow three statements (items 1, 2, 5), complete one antecedent (item 3) and add one
scoped attainment result (item 4).
