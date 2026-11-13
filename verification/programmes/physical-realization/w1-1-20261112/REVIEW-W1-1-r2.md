# Focused re-check of W1-1 r2

Reviewer: the same independent agent as for `REVIEW-W1-1.md`. Read-only and paper-only. Sources are `fb733b4a`, read
with `git show` (the `w1-1-review/` copies). Object: `w1-1/W1-1-REPORT-r2.md` (363 lines; cited as `r2:<line>`). The
r1 report is unchanged.

## Verdict: ACCEPT WITH NITS

All of F1–F12 are applied, and correctly. The pressure-tests below find no error that changes a verdict, a derivation
result or a status row's substance. The nits are about precision: what "contradicts" means in F4, two validity
conditions missing from N2's first-order form, the order at which the F5 witness violates H-count, and the wording of
the gap route. They can be applied without another review round.

## F1–F12: applied?

| Finding | Applied | Where in r2 |
|---|---|---|
| F1 (N0 to ELABORATING; SM:292, SM:811, GR:695; narrowed gap) | Yes | r2:114–129, :298–300 |
| F2 (lattice identity; endpoint p(0)e^{δβ_D}/δ; variance term; ⇔ hypotheses) | Yes, with nit N2 | r2:139–158 |
| F3 (mean-energy form not realized by local cells) | Yes | r2:160–164, :309 |
| F4 (absorption only for 1+r > 0) | Yes, with nit N1 | r2:255–261 |
| F5 (one-way implication; witness; κ\* per reading; W1-add) | Yes, with nit N3 | r2:277–292 |
| F6 (C3 engages GR:50, :661, Sub:268(i); constant bound gives slope 0; s_D ≈ 0 stronger than H-inert) | Yes, with nit N5 | r2:191–204 |
| F7 (real lift, CE-RL) | Yes, with nit N6 | r2:228–237 |
| F8 (gap route a distinct open premise; GR:84 scope) | Yes, with nit N4 | r2:38, :218–226, :267–273 |
| F9 ("Recorded") | Yes | r2:92–93 |
| F10 (cross-propagation; C1 scoping) | Yes | r2:180, :323–330 |
| F11 (provenance) | Yes | r2:359–363 |
| F12 (citation [31], τ_Kω, Gauss-sum aside, CE-M "order of magnitude") | Yes | r2:185, :222, :100, :42 |

## Pressure-tests

**1. N2 first-order form (r2:149–151).** I re-derived it. Write A = E_p[e^{δβ_B}] and B = p(0)e^{δβ_D(E)}. Then:
- δβ_E = ln(A + B) = ln A + ln(1 + B/A).
- ln A = δE_p[β_B] + (δ²/2)Var_p(β_B) + O(δ³κ₃).
- So β_E ≈ E_p[β_B] + (δ/2)Var_p(β_B) + B/δ. The displayed form is correct.

Its validity needs two conditions that r2 does not list:
- δβ_B and δβ_D ≪ 1 on the support of p, so that the third cumulant is negligible.
- B/A ≪ 1, that is p(0) ≪ 1, so that ln(1 + B/A) ≈ B. Otherwise the endpoint enters as ln(1 + p(0)e^{δβ_D})/δ.

r2's condition p(0) ≪ βδ, for the endpoint to be *negligible*, implies p(0) ≪ 1, so the conclusions of r2:156–158
stand. The displayed form is offered more generally, though (nit N2).

Two further checks:
- The kδ/2 offset (r2:154) is a relative O(δ/E) correction, negligible on any reading.
- In reading L, ⟨E_D⟩ = 0 forces Var(E_B) = 0 and p(0) = 0 (for E > 0). So the ⇐ direction holds exactly on the
  lattice, and only ⇒ needs the smallness conditions.

**2. F4 split (r2:258–261).** The logic is right, but "contradicts" is too strong for one target.
- GR:186 and :210 do not assert β_E > 0. They state that the classical layer is "settled" *with* β_E > 0, which H-count
  supplies. At r ≤ −1 that premise is missing, so the classical orientation is not settled. This is a lost premise, not
  a contradiction of a stated fact. r = −1 belongs here as well as r < −1, but summary item 7 (r2:43) and the r2:317
  row say only "r < −1".
- `counting_passive` takes `Monotone Ω` (weak) as a hypothesis. For r < −1, Ω decreases near E\*, so the hypothesis
  fails and the theorem does not apply. The reflected count is passive for −ε, which is the flip of orientation r2
  describes. "Contradicts the hypothesis" should read "violates the hypothesis".
- At r = −1, the slope is zero at a point. That is compatible with `Monotone`, and even with `StrictMono` at an
  isolated point, so "does not contradict `counting_passive`" is correct. "The profile it yields is then uniform"
  holds only to first order in e_i.

(Nit N1.)

**3. F5 implication and witness (r2:285–286).**
- **⇒: correct.** GR:58's setting supplies conservation and V/H additivity, GR:695 states the real-energy shell is
  assumed, and H-count supplies the first-law identification. Then s_H = σA(E)/ε² + const gives
  β_E = (σ/ε²)dA/dE = β_geo(κ(E)).
- **⇐: the witness is valid.**
  - N_B independent cells with D empty: concave s\* lets one choose E\* with s_B′(E\*) = β_geo for any β_geo > 0, so
    W1-0 and W1-min(L) hold there.
  - s_H″ < 0 ≠ +β/E. GR:58 itself derives s_H″ = β/E from H-count, so the contrapositive applies. H-count fails as GR
    uses it.

  The violation is at second order. Over the shell scale e_i ~ k_BT, the mismatch is
  |s_H″ − k|·e_i²/2 ~ (βe_i)(e_i/E) ~ 10⁻¹²². That is exactly the δ_bath order. So the witness separates W1-min from
  H-count's second-order content, the δ_bath and de Sitter statements, and not from its slope content. r2:287 already
  says this extra content is consumed only by GR:58's de Sitter statements, δ_bath and §7.3. The witness paragraph
  should say the violation is second-order (nit N3).

**4. W1-add (r2:290–292).** This is fair and correctly sourced. GR:60 defines H-shell through the same formula,
P(i) ∝ Ω_H(E−e_i) under weak boundary coupling. GR:70 uses N_i = Ω_H(E−e_i), and GR:74 takes β_E as the slope of the
resulting R_E. "Recorded, not resolved" is the right status. One clarification is optional: GR:86's stated scope is
the product Gibbs marginal, and GR:60 and :86 point to a mean-force count at non-negligible coupling as the
alternative. This is a tension in GR's wording, not yet a demonstrated inconsistency.

**5. CE-RL as adopted (r2:228–237).** I re-checked it.
- A positive-definite quadratic form in 2N real variables gives Ω ∝ E^{N−1}, β = (N−1)/E and C = N−1.
- Reading L: β_geo·E = 8πσR²/ε² = 2σN_B, so β_E/β_geo = N_H/(2σN_B) ≈ R/(6σε) ≈ 7×10⁵⁹.
- A positive-definite form stays positive definite when restricted to H's coordinates, so counting H alone is
  legitimate.
- r2 correctly conditions the result on W1-0 (the lift's E identified with the first-law energy, with V/H additivity
  assumed despite the u·Av cross terms) and on D ≈ one Hubble volume.
- The GR:695 consistency note is accurate.

Unstated O(1) assumptions: one lattice site per ε³ (a = ε), and the number of real components per site (K = 6 under
GR:104, which multiplies N_H by 6). Neither changes the order of magnitude (nit N6).

**6. The gap route's status (r2:218–226, :272–273).** "Distinct open sufficient premise; undetermined for the finite
substratum; negative in the real lift" is correct.
- The NEW label is defensible: c.6818970549 named "a gap ≫ k_BT_cl" qualitatively, and r2 adds the threshold
  βΔ − ln βΔ ≳ ln(N_eff/2s_B) ≈ 1.4×10² and the decisive input.
- "Negative in the real lift" is immediate, since the lift's energies are continuous. It is correct, but say that it
  holds trivially.
- **Wording (nit N4).** r2:221 says "gapped or collective". By r2's own pressure-test (r2:222), translation invariance
  gives D the visible sector's fine per-cell granularity, so per-cell gaps are excluded. The live option is that D's
  low-lying configurations are *collective*: of order one per Hubble volume, not per cell.

## Nits (to apply; no further review needed)

- **N1 (F4 wording).**
  - Write "r ≤ −1 removes the β_E > 0 premise under which GR:186/:210 call the classical layer settled". Use this at
    r2:15, :43, :260–261 and in the r2:317 row.
  - Write "r < −1 violates `counting_passive`'s Monotone-Ω hypothesis (the theorem does not apply; the reflected
    profile is passive for −ε)".
  - Change "uniform" to "uniform to first order".
- **N2 (N2 validity).** Add δβ_B, δβ_D ≪ 1 on supp p and p(0) ≪ 1 as the conditions for the displayed first-order form,
  with ln(1 + p(0)e^{δβ_D})/δ otherwise. Note that ⇐ in reading L is exact on the lattice.
- **N3 (F5 witness).** State that the witness violates H-count at second order (s_H″), the order GR:58 derives from
  H-count, which is ~10⁻¹²² over shell-scale e_i.
- **N4 (gap route).** Replace "gapped or collective" with "collective (per-cell gaps are excluded by translation
  invariance given the visible sector's fine steps)", and mark the real-lift negative as immediate.
- **N5 (C3(c), r2:200).** Change "conflicts with the corpus's scoping … (GR:585)" to "goes beyond". GR:585 allows a deep
  sector of any size and does not bound D's shell count.
- **N6 (CE-RL).** State the assumptions a = ε and the per-site component count (K = 6 multiplies N_H). The order of
  magnitude is unchanged.
- **N7 (r2:305).** Change "Kernel-checked" to "kernel theorem on `main` (statement read; not rebuilt in this unit)".

## What the unit establishes (unchanged in substance)

At the layer of paper derivation, W1 is not derived from OI's present premises plus standard physics. It remains an
additional, conditional assumption.
- Every tested mechanism either fixes a state, uses ħ, restates W1 or H-inert (or something stronger), or needs a
  collective-deep-sector premise. That premise is open for the finite substratum and fails in the corpus's one
  real-energy model (CE-RL).
- A W1 excess with 1+r > 0 is absorbed into σ. With r ≤ −1 it is not inert: it removes the classical-orientation
  premise of GR:186/:210.
- H-count implies W1-0 ∧ W1-min(L), and the converse fails at second order.

This is a consistency-axis result. It moves no correctness band and promotes nothing, and nothing here is on `main` or
established in the §A.46 sense.
