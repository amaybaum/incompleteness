# Focused delta review of W1-1 r3 (r2 → r3 only)

Reviewer: independent agent, read-only and paper-only. No computation on OI rules, no Lean build, no commits or GitHub
writes. Owner gate (amaybaum, 2026-11-13, "Run all three (Recommended)"): a historical ACCEPT does not cover later
edits, so the waiver in `REVIEW-W1-1-r2.md` ("no further review needed") is not relied on here.

**Object reviewed.** `verification/programmes/physical-realization/w1-1-20261112/W1-1-REPORT-r3.md` at branch
`research/oa1-w1-1-20261112` commit `5fec096645b5a201af3ce37c0a60538e8407a365`: blob
`890429362bc27f580675b8c7d2c6ef04ed01d784`, SHA-256 `fcfe12a1…07420973`, 386 lines (cited `r3:<line>`). This equals the
blob and SHA-256 that `OBJECTS.md` records for r3, and the session working copy is byte-identical.
Compared against r2 blob `63a5d1233b28f5b0e19ca99c171ef01750ec104b` (accepted text) and `REVIEW-W1-1-r2.md` blob
`f466f9505c58a627263f3a098ba54c8c6d8da61e`. Sources: `fb733b4a` (the report's stated base) and current `origin/main`
`911a5cb6b61e6531bc8fad37ee3de4e5b1c2b019`, read with `git show`.

## Verdict: ACCEPT WITH CHANGES

All of N1–N7 are applied. Four added statements overreach or are wrong: E1–E4 below. E1 is a formula wrong at O(β).
E2 is an "exact" claim missing an endpoint condition. E3 turns "compatible with the hypothesis" into "the theorem
applies". E4 states a sufficient example as a necessary condition. Three further edits fix stated precision (E5–E7),
and three fix stale status text and a stale citation (E8–E10). None moves a verdict label or the headline result: W1
remains an additional physical assumption. The edits are given as exact replacement text. If r4 applies them verbatim,
a diff check against this file is enough; any other wording needs review.

## 1. Every delta hunk

| # | r3 lines | Change | Source nit | Finding |
|---|---|---|---|---|
| H1 | 1 | Title r2 → r3 | — | OK |
| H2 | 7 | Revision line: r2 re-checked, "nits … call for no further review" | — | Stale under the owner gate → E8 |
| H3 | 15–18 | F4 split: r ≤ −1 removes premise; r < −1 violates Monotone-Ω; CE-M regime | N1 | OK (CE-M threshold 1/(2×10⁶⁰) = 5×10⁻⁶¹ re-checked) |
| H4 | 38–45 | "r3 nits" block | N1–N7 | :40 inherits E2; :41 drops the shell-scale qualifier → E5 |
| H5 | 50 | Summary 2: "collective" deep sector | N4 | OK once E4 defines "collective" |
| H6 | 55 | Summary 7: r ≤ −1 premise lost; r < −1 negative T | N1 | OK |
| H7 | 160–166 | First-order form: validity conditions; "Otherwise …" | N2 | "Otherwise" formula wrong → E1 |
| H8 | 173–175 | Hypothesis list; reading-L ⇐ "exact"; kδ/2 offset | N2, pressure-test 1 | :173 OK; :174 overreach → E2; :175 OK |
| H9 | 217 | C3(c) "goes beyond" GR:585 | N5 | OK (GR:585 scopes the bounds to C_V, C_B "for a finite deep sector of any size") |
| H10 | 238 | Gap route narrowed to collective configurations | N4 | Quantifier overreach; categorical exclusion of per-cell gaps → E4 |
| H11 | 241 | Real-lift negative "immediately so" | N4 | OK (continuous spectrum, no gap) |
| H12 | 251–255 | CE-RL assumptions a = ε, K; PD restriction; V/H additivity | N6, pressure-test 5 | Correct; K-factor and undefined symbols → E6 |
| H13 | 282–284 | §7 r ≤ −1, r = −1, r < −1 | N1 | :282 OK; :283 overreach → E3; :284 needs scope → E3 |
| H14 | 309 | Witness violates H-count at second order, "~10⁻¹²²" | N3 | Number and scope → E5 |
| H15 | 328 | `counting_passive` row relabelled | N7 | OK (statement at :256 on current `main`; file unchanged since `fb733b4a`; no `sorry`/`axiom` in it) |
| H16 | 340 | Status row r ≤ −1 / r < −1 | N1 | OK |
| H17 | 377 | Limits: "r3 applies those nits without a further review round" | — | Stale → E8 |

Not changed in r3, but stale as a result of the delta or of `main`: r3:331 (status row omits N2's new conditions →
E7), r3:363 and :373 (inventory and review list → E8), r3:356 (Structure line numbers → E9).

## 2. Faithfulness to REVIEW-W1-1-r2

- **N1:** applied at every site named (r2:15, :43, :260–261, :317 → r3:15–18, :55, :282–284, :340). r3 also added
  "so the theorem applies" at :283. The reviewer's text did not say that: it said only that "does not contradict" was
  correct. That addition is E3.
- **N2:** applied as written. The reviewer's own replacement formula and "exact" note carry the two defects E1 and E2.
- **N3:** applied. It carries the reviewer's 10⁻¹²², and the r3:41 summary drops the reviewer's "over the shell scale"
  qualifier (E5).
- **N4:** applied. r3 lifts "of order one per Hubble volume" from the reviewer's pressure-test text and makes it a
  requirement ("must"), which E4 corrects.
- **N5, N6, N7:** applied faithfully.

## 3. Findings and derivations

**E1 (H7, r3:164): the "Otherwise" endpoint formula is wrong at O(β).**
- Write A = E_p[e^{δβ_B}] and B = p(0)e^{δβ_D(E)}. The identity at r3:158 gives δβ_E = ln(A + B) exactly, that is
  δβ_E = ln A + ln(1 + B/A).
- If p(0) is not ≪ 1, the endpoint enters as ln(1 + B/A)/δ, not ln(1 + B)/δ.
- With δβ_B ≪ 1, A = 1 + δ⟨β_B⟩ + …. So
  [ln(1 + B) − ln(1 + B/A)]/δ ≈ B⟨β_B⟩/(1 + B).
- That difference is of order β, the order of the quantity W1 tests. In this regime the endpoint term
  (~ln(1+B)/δ ≫ β) dominates anyway, so no verdict moves. The displayed replacement is still wrong as an additive
  decomposition.
- Minor: in r3:163, δβ_D ≪ 1 does not control cumulants (β_D enters only through e^{δβ_D(E)}), and the relevant point
  is E, not "the support of p".

**E2 (H8, r3:174; summary r3:40): the "exact" reading-L ⇐ needs an endpoint condition.**
- The derivation is correct up to Var = 0: E_D ≥ 0 with ⟨E_D⟩ = 0 forces E_B = E on the shell, so Var = 0 and p(0) = 0
  for E > 0.
- What it misses is the endpoint term. That term is Ω_B(0)Ω_D(E+δ)/Ω_H(E), the y = 0 term of
  Ω_H(E+δ) = Σ_y Ω_B(y)Ω_D(E+δ−y).
- With p concentrated at E_B = E and Ω_B > 0 on [0, E], Ω_D(y) = 0 for 0 < y ≤ E. So Ω_D(E) = 0 and β_D(E) is undefined
  (+∞), and "p(0) = 0" does not make p(0)e^{δβ_D(E)} vanish. All other y terms vanish.
- Counterexample: Ω_D(0) = 1, Ω_D(y) = 0 for 0 < y ≤ E, and Ω_D(E+δ) = M > 0. Then ⟨E_D⟩_shell(E) = 0, but
  Ω_H(E+δ)/Ω_H(E) = Ω_B(E+δ)/Ω_B(E) + Ω_B(0)M/Ω_B(E), so β_E ≠ β_B(E).
- Exactness also needs W1′(dS) at E + δ (the forward difference uses s_B(E+δ)). It further needs β_geo read as the
  forward difference of σA(E)/ε². r3:76 defines β_geo in continuum form, so without that reading it is exact only up to
  r3:175's own kδ/2 offset.

**E3 (H13, r3:283–284): `counting_passive` scope.**
- The kernel hypothesis is `Monotone Ω` for Ω : ℝ → ℝ, global and weak (ThermalOrientation.lean:256; `Passive` at :195
  is ∀ a b, E a < E b → p b ≤ p a).
- At r = −1, β_E(E\*) = 0 is compatible with that hypothesis but does not establish it, so "so the theorem applies" is
  unsupported.
- At r = −1 the profile's order is decided at second order. Take P(i) ∝ exp(½ s_H″(E\*) e_i²) with e_i ≥ 0 and
  s_H″(E\*) > 0. Then p rises with e, and the profile is not passive for ε.
- At r < −1, "the reflected profile is passive for −ε" is true only where the count is decreasing. For shell-scale ε_a
  near E\*, the kernel's argument applied to the reflected count gives it (equivalently, the theorem applied to a
  monotone extension of the reflected count off that window). That is a derivation here, not the kernel statement, and
  it is not global.

**E4 (H10, r3:238): "collective" is overstated as "of order one per Hubble volume", and the per-cell exclusion is
stated categorically.**
- With no gap (βΔ ≲ 1), each accessible deep mode carries ~k_BT. Under reading L, r = −⟨E_D⟩/E ~ −N_eff·k_BT/E, and
  E = 2s_B k_BT on de Sitter (β = kE, s_B = kE²/2), so r ~ −N_eff/(2s_B).
- In the dilute regime, the threshold βΔ − ln βΔ ≳ ln(N_eff/2s_B) holds automatically once N_eff ≲ 2s_B.
- So the collective route needs only N_eff ≪ 2s_B ≈ 4.5×10¹²² (far fewer than one per cell, against
  N_eff ≈ 3.2×10¹⁸² per-cell). "Of order one per Hubble volume" is one example of this, not the requirement.
- The exclusion of per-cell gaps rests on r3:239's "My inference is …": GR:66 states only a positive probe gap over a
  finite window. So the exclusion is conditional on that inference.

**E5 (H14, r3:309; H4, r3:41): the second-order mismatch figure and its scope.**
- Redone: in the witness, s_H″ ~ −β/E (CE-F, r3:118), and H-count gives s_H″ = k = β/E (GR:58, on the exact de Sitter
  calibration). So |s_H″ − k|·e_i²/2 ~ βe_i²/E = (βe_i)²/(βE).
- With βe_i ~ 1 and βE = 2s_H ≈ 4.5×10¹²² (r3:237), this is ≈ 2×10⁻¹²³. GR:58 quotes δ_bath ~ 10⁻¹²³. So "~10⁻¹²²,
  the δ_bath order" is off by a decade from the δ_bath figure it invokes.
- r3:41 drops the "over shell-scale e_i" qualifier. Globally, for |E − E\*| ~ E\*, the witness's s_H differs from
  σA(E)/ε² + const by O(s_H), so the violation is small only on the shell scale.
- "The order GR:58 derives from H-count" needs "on the exact de Sitter calibration": that is where GR:58 states
  s_H″ = β/E.

**E6 (H12, r3:251–255).**
- Re-checked:
  - R/(6σε) = 1.37×10²⁶/(6 × 3.23×10⁻³⁵) ≈ 7.1×10⁵⁹.
  - The restriction of a PD form to H's coordinates is PD.
  - K multiplies N_H only. GR:104 has κ_m = 1, so N_B is unchanged.
- At K = 6 the ratio is ≈ 4×10⁶⁰, so "neither changes the order of magnitude" should state the factor. The conclusion
  r ≫ 1 is unaffected.
- "(u, v)" and "u·Av" are not defined in r3. They are SM:296's F(u,v) = (v, Av − u) and E(u,v) = u·u + v·v − u·Av, and
  should be cited there.

**E7 (r3:331).** The status row "N2 first-order form; reading-L/C equivalences" was not updated with N2's added
conditions or the reading-L ⇐ exception. That is an in-document propagation miss.

**E8 (H2, H17; r3:7, :363, :373, :377): stale review status.**
- "which call for no further review" (r3:7) and "without a further review round" (r3:377) are superseded by the owner
  gate.
- The inventory says "for r2" (r3:363).
- The review list (r3:373) omits `REVIEW-W1-1-r2.md`.

**E9 (r3:356): stale citation against current `main`.**
- Structure:205 and :305 are correct at the stated base `fb733b4a`. On `origin/main` `911a5cb6` they are :206 and
  :306, after a line was inserted at Structure:180.
- No other line the report cites has moved:
  - GR's hunks since the base are in place at :88, :316, :466 and :623.
  - Main's hunks are in place.
  - SM's only line-shifting hunk is at :1626.
  - ThermalOrientation.lean is unchanged.
- Content changes at cited lines: GR:88 and :623 now add H-Hawking (i) and the symmetric detailed-balance rate ratio,
  and Main:724's ledger was reworded. Neither adds a shell or real-energy condition, so F1's finding (r3:12, :137,
  :323) still holds on current `main`.

**E10 (OBJECTS.md).** r4 and this review must be recorded with blob ids and SHA-256, as for earlier files.

## 4. Required edits (exact text)

**E1.** Replace r3:163–164 with:
> - δβ_B ≪ 1 on the support of p, so that third and higher cumulants of δβ_B are negligible, and δβ_D(E) ≪ 1, so that e^{δβ_D(E)} ≈ 1;
> - p(0) ≪ 1, so that ln(1 + p(0)e^{δβ_D}/E_p[e^{δβ_B}]) ≈ p(0)e^{δβ_D}. Exactly, δβ_E = ln E_p[e^{δβ_B}] + ln(1 + p(0)e^{δβ_D(E)}/E_p[e^{δβ_B}]); when p(0) is not small the endpoint enters as ln(1 + p(0)e^{δβ_D(E)}/E_p[e^{δβ_B}])/δ.

**E2.** Replace r3:174 with:
> - Exception: in reading L, ⟨E_D⟩ = 0 forces E_B = E on the shell, so Var(E_B) = 0 and p(0) = 0 for E > 0. The endpoint term of the identity is Ω_B(0)Ω_D(E+δ)/Ω_H(E), which p(0) = 0 does not remove. If also Ω_B(0)Ω_D(E+δ) = 0 and W1′(dS) holds at E and E+δ, then β_E = β_B(E) exactly, and the ⇐ direction holds exactly on the lattice with β_geo read as the forward difference of σA(E)/ε² (otherwise up to the kδ/2 offset). Only ⇒ needs the smallness conditions.

and in r3:40 replace "The ⇐ direction under reading L is exact on the lattice." with "The ⇐ direction under reading L
is exact on the lattice under an added endpoint condition."

**E3.** Replace r3:283 with:
> - **r = −1.** Here β_E = 0 at E\*, an infinite temperature. A zero slope at one point is compatible with `counting_passive`'s Monotone-Ω hypothesis (ThermalOrientation.lean:256) but does not establish it. The profile is uniform to first order in e_i; its passivity is decided at second order, and for s_H″(E\*) > 0 it is not passive for ε.

In r3:284 replace "That violates `counting_passive`'s Monotone-Ω hypothesis: the theorem does not apply, and the
reflected profile is passive for −ε." with "That violates `counting_passive`'s Monotone-Ω hypothesis, so the theorem
does not apply. For shell-scale ε_a, where the count is decreasing, the same argument applied to the reflected count
gives a profile passive for −ε (derived here; not a kernel statement)."

**E4.** In r3:238 replace "The deep sector's low-lying configurations must be *collective*: of order one per Hubble
volume, not one per cell. Per-cell gaps are excluded by translation invariance, given the fine steps of the visible
sector (pressure-test below)." with:
> The deep sector's thermally accessible low-lying configurations must be *collective*: N_eff ≪ 2s_B ≈ 4.5×10¹²² (with no gap, r ~ −N_eff/(2s_B)), far fewer than one per cell; of order one per Hubble volume is an example. Per-cell gaps are excluded by translation invariance if the visible sector's classical energy steps reach k_BT_cl, which is this unit's inference (pressure-test below).

**E5.** In r3:309 replace "which is the order GR:58 derives from H-count. Over shell-scale e_i ~ k_BT the mismatch is
|s_H″ − k|·e_i²/2 ~ (βe_i)(e_i/E) ~ 10⁻¹²², the δ_bath order." with "the order at which GR:58 derives s_H″ = β/E from
H-count on the exact de Sitter calibration. Over shell-scale e_i ~ k_BT the mismatch is |s_H″ − k|·e_i²/2 ~
(βe_i)(e_i/E) ~ 1/(2s_H) ≈ 2×10⁻¹²³, the δ_bath order; for |E − E\*| ~ E\* the two entropy functions differ at
O(s_H)." In r3:41 replace "(~10⁻¹²², the δ_bath order)" with "(over shell-scale e_i, ~10⁻¹²³, the δ_bath order)".

**E6.** In r3:254 replace "Neither changes the order of magnitude." with "With K components the ratio is K·R/(6σε),
≈ 4×10⁶⁰ at K = 6; r ≫ 1 is unchanged." In r3:255 replace "despite the u·Av cross terms" with "despite the u·Av cross
terms of E(u,v) = u·u + v·v − u·Av (SM:296)".

**E7.** In the r3:331 row replace "conditional on H-add, W1′(dS) on supp p, common lattice, p(0) ≪ βδ, δVar small"
with "conditional on H-add, W1′(dS) on supp p, common lattice, δβ_B, δβ_D ≪ 1, p(0) ≪ βδ, δVar small (reading-L ⇐
exact under the endpoint condition of §5)".

**E8.**
- r3:7: replace "r3 applies its nits N1–N7, which call for no further review. No verdict moved from r2 to r3." with
  "r3 applied its nits N1–N7. Under the owner's gate (2026-11-13) r3 was delta-reviewed
  (`w1-1/DELTA-REVIEW-W1-1-r3.md`, ACCEPT WITH CHANGES), and r4 applies its required edits E1–E10. No verdict label
  moved from r2."
- r3:377: replace "r3 applies those nits without a further review round." with "r3 was delta-reviewed (ACCEPT WITH
  CHANGES) and r4 applies its required edits."
- r3:363: replace "for r2" with "for r2–r4".
- r3:373: replace "**Review.** `w1-1/REVIEW-W1-1.md`." with "**Reviews.** `w1-1/REVIEW-W1-1.md`,
  `w1-1/REVIEW-W1-1-r2.md`, `w1-1/DELTA-REVIEW-W1-1-r3.md`."
- Also change the title to r4.

**E9.** In r3:356 replace "Structure:205/:305" with "Structure:205/:305 (at `fb733b4a`; :206/:306 on `origin/main`
`911a5cb6`)". Alternatively, rebase every citation to a current `main` commit and restate the header at r3:5. Either way
the base line must name the commit the numbers refer to.

**E10.** Add rows for r4 and this review to `OBJECTS.md`.

## 5. What stands

These items stand after the edits:
- W1 is an additional physical assumption, not derived (consistency axis; no correctness band moves; nothing here is
  established in the §A.46 sense).
- σ-absorption is restricted to 1 + r > 0.
- For r ≤ −1, GR:186/:210's β_E > 0 premise is lost.
- The gap route is an open, distinct sufficient premise. With E4 it is stated as N_eff ≪ 2s_B or a per-cell gap; it is
  undetermined for the finite substratum and fails, trivially, in the real lift.
- CE-RL r ≈ 7×10⁵⁹·K.
- H-count ⇒ W1-0 ∧ W1-min(L), and the converse fails at second order.
- W1-add (GR:86 versus GR:60/:70/:74) is recorded, not resolved.

Owner checkpoint still required before any use.

## Diff check of r4

**Object.**
- r4: `w1-1/W1-1-REPORT-r4.md`, blob `72800573868837a93ede067ea4e99504e9ed9bc0`, SHA-256 `34c0097d…dd1313a`, 403 lines.
- Compared with `diff` against r3, blob `890429362bc2…`.
- Read-only. The application record `W1-1-r4-APPLY.md` was read, but nothing in this check relies on it.

**Verdict: ACCEPT WITH CHANGES.** Two edits, D1 and D2, are needed. Both fix wording my own E6 and E8 text produced.
Once they are applied verbatim, no further review is needed beyond a diff check.

**(1) E1–E9 verbatim and in place.**
- `diff` changes exactly r3/r4 lines 1, 7, 40, 41, 163, 164, 174, 238, 254, 255, 283, 284, 309, 331, 356, 363, 373 and
  377, and appends r4:387–403. Each replacement is one line for one line.
- Every `> ` blockquote replacement in §4 occurs verbatim, as a substring, on its specified line: E1 at :163–164, E2 at
  :174, E3 at :283 and E4 at :238. I checked these mechanically.
- I checked the inline replacements by eye against §4: E2 at :40, E3 at :284, E5 at :309 and :41, E6 at :254–255, E7 at
  :331, E8 at :1, :7, :363, :373 and :377, and E9 at :356. All are verbatim and at the specified places.
- Text outside the edited spans is unchanged. In particular, "It is not a restatement of H-inert." is kept at :238, and
  the rest of :284 is kept.
- E10 is not applied in r4, as assigned.

**(2) Nothing else changed, and §13 (r4:387–403) is accurate.**
- No line outside the list above differs.
- §13's statements are correct:
  - every r4 line number equals its r3 line number, for :1–386;
  - each edit row names the right r4 lines;
  - E9 is applied by annotation, and :5 is unchanged;
  - E10 is outside the file.

**(3) The writer's three points.**
- **r4:7, "applies … E1–E10".** No edit is needed if the coordinator adds the `OBJECTS.md` rows for r4 and this review
  in the same commit as r4: the revision as committed then applies E1–E10. If the rows land separately, replace
  "and r4 applies its required edits E1–E10." with "and r4 applies its required edits E1–E9; E10's `OBJECTS.md` rows
  are added with r4."
- **r4:363, "for r2–r4".** An edit is needed (D1). `origin/main` has moved, so "via `git show origin/main:`" no longer
  names the commit the line numbers refer to. Replace "(all via `git show origin/main:` for r2–r4):" with "(all via
  `git show fb733b4a:` for r2–r4, the base named at :5; :356 also cites `origin/main` `911a5cb6`):".
- **r4:255, two adjacent parentheticals.** An edit is needed (D2). Replace "V/H additivity is assumed despite the u·Av
  cross terms of E(u,v) = u·u + v·v − u·Av (SM:296) (part of W1-0)." with "V/H additivity, part of W1-0, is assumed
  despite the u·Av cross terms of E(u,v) = u·u + v·v − u·Av (SM:296)."

**§13 follow-on.** After D1 and D2, add one row to the §13 table:
`| Diff check D1–D2 | :363 (inventory base); :255 (W1-0 parenthetical) |`. Then change the r4:390 sentence to "Each edit
is applied with the review's exact replacement text, including the diff check's D1–D2." Nothing else changes.

Confirmation of r4 blob 34b1a16fc84ed38b19aec482b555fe8876815959: ACCEPT. Reverting exactly four hunks reproduces the previous r4 blob 72800573868837a93ede067ea4e99504e9ed9bc0 byte for byte. The four hunks are r4:255 (D2), :363 (D1), :390 (the §13 sentence) and the new §13 row at :404. Each is verbatim the text given in "Diff check of r4", and nothing else changed.
