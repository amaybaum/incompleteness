# ħ framing and θ₀: change note

This change applies the owner's decisions on `decisions/DECISIONS.md` (O1–O7) and the full set of corrections that need
no decision.

- **Branch:** `fix/hbar-theta0-20261026` (PR #939).
- **Base:** the branch was cut from `main` at `c967d6a9`. `main` at `b64919cd` (after #938) was merged in with an
  ordinary merge commit, `4ed4c6e6`, before any edit. The merge was clean: #938 touched only Main, Explainer,
  appendix-b, FULL, their artifacts, the coverage ledger's `MAIN:L-accessible-backflow-from-readback` entry and its own record.
- **Method:** `decisions/apply.py` (run as `python3 -I decisions/apply.py <worktree> <out.json>` on the merge commit
  `4ed4c6e6`) applied `decisions/entries.py` to the merged tree in the manner of `decisions/sim.py`, with
  the recommended set {O1A, O2a, O3b, O3-76, O4a, O5a, O6A, O7a} plus every no-decision entry. Each OLD string was
  asserted to occur exactly once in its line before replacement, and the FULL line was located by byte-identity with
  the chapter line before any edit and asserted identical to it afterwards. Every DECISIONS entry applied cleanly. Three
  texts were adjusted for the owner's qualifications and two residue sites were added; both are listed below.

## Owner decisions (amaybaum, 2026-10-26), verbatim

> "I approve all seven recommended options, with two scientific qualifications":
> - **O1-A:** "Apply H-slope consistently to Substratum Stage 3, Theorem 23, and its restatements. Reaffirm the coverage ledger."
> - **O2-a:** "Count Koide Q and θ₀ as two independent relations: eight Category A relations."
> - **O3-b:** "Remove consistency relations from the G4 predictions cell; describe them separately."
> - **O4-a:** "Adopt the sign-resolved, conditional 95% dressing interval."
>   - **Qualification:** "The interval is conditional on the stated linear-response model, including the assumed sensitivity coefficient and range of r. It should not be described as a model-independent experimental exclusion. The loop comparison is compatible with the 95% interval, but is not a confirmed prediction."
> - **O5-a:** "Retain the superlative only with its explicitly stated relative-precision metric."
> - **O6-A:** "Keep the different lepton-mass calculations distinct and correctly labeled."
>   - **Qualification:** "Retain the renormalization-group interpretation as a possible explanation, not as a demonstrated mechanism. The agreement of the mass ratios does not independently establish the proposed running."
> - **O7-a:** "Harmonize Koide values to the PDG 2024 basis used by SM:903."
> - "Proceed with the approved corrections, mirrored text, rebuilt outputs, independent review, and exact-head CI. Merge approval remains separate."

## What was applied

| Group | Edits | Of which mirrored in FULL |
|---|---|---|
| ħ, no decision (H1–H45, H14 in two parts) | 46 | 31 |
| θ₀ figure and labels, no decision (T1–T18, T2 in two parts) | 19 | 9 |
| Stale mass rows, no decision (M1–M7, M4 in two parts) | 8 | 6 |
| O1-A | 5 | 0 |
| O2-a | 3 | 3 |
| O3-b and O3-76 | 2 | 2 |
| O4-a, adjusted | 2 | 1 |
| O5-a | 7 | 5 |
| O6-A | 5 | 5 |
| O7-a | 6 | 5 |
| O6 qualification adjustment | 1 | 1 |
| Residue from the re-grep | 2 | 2 |
| **Total** | **106** | **70** |

The 106 edits touch 25 manuscript files: 8 papers (GR, SM, Main, Substratum, Structure, Methodology, Explainer, Juno),
16 book sources (14 chapters and appendices, the glossary and the readers' guide) and `book/README.md`, which is not
mirrored. FULL carries the 70 mirrored edits.

## Qualification adjustments

### O4-a: the dressing interval is conditional on the response model

DECISIONS' O4a texts gave the interval and said the loop comparison "is not decisive". They did not say that the
interval depends on the linear-response model, κ and the range of r, or that the loop value is not a confirmed
prediction, both of which the owner's qualification requires. The interval itself, its rule and its numbers are unchanged.

`papers/SM.md:940`, DECISIONS O4a-1 NEW:

> The agreement of $\theta_0 = 2/9$ with the observed $\theta_0 = 0.222225 \pm 0.000006$ ($0.001\%$, $0.4\sigma$) bounds the taste-structured part of an emergent mass-level dressing to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence (two-sided); a second-order lepton-Yukawa loop, of order $10^{-6}$, lies inside that interval for either sign, by a factor of about two, so the comparison is not decisive.

Applied:

> In this linear-response model, with $\kappa \approx -35$ and $\lambda_E/\lambda_{A_1} = 0.22$–$0.24$, the agreement of $\theta_0 = 2/9$ with the observed $\theta_0 = 0.222225 \pm 0.000006$ ($0.001\%$, $0.4\sigma$) bounds the taste-structured part of an emergent mass-level dressing to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence (two-sided); the interval is conditional on that response model, its sensitivity coefficient and the range of $\lambda_E/\lambda_{A_1}$, and is not a model-independent exclusion. A second-order lepton-Yukawa loop, of order $10^{-6}$, is compatible with the interval for either sign, by a factor of about two; the comparison is not decisive, and the loop estimate is not a confirmed prediction.

"This linear-response model" refers to the sentence just before it on the same line, which states
$d\theta_0/\theta_0 = \kappa\,(1 - \lambda_E/\lambda_{A_1})\,(\delta m/m)$ with $\kappa \approx -35$; $r$ is written out as
$\lambda_E/\lambda_{A_1}$, as SM writes it.

`book/ch06-matter-content.md:179` [FULL:1705], DECISIONS O4a-2 NEW:

> constrains it to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence, an interval that a lepton-Yukawa loop of order $10^{-6}$ lies inside for either sign, by a factor of about two (SM §7.2).

Applied:

> constrains it to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence, conditional on the linear response of $\theta_0$ to the dressing (sensitivity coefficient $\kappa \approx -35$, with $\lambda_E/\lambda_{A_1}$ in the range above) rather than as a model-independent exclusion; a lepton-Yukawa loop of order $10^{-6}$ is compatible with that interval for either sign, by a factor of about two, but is not a confirmed prediction (SM §7.2).

"The range above" is the $\lambda_E/\lambda_{A_1} \approx 0.22$–$0.24$ stated earlier in the same paragraph.

### O6-A: the renormalization-group reading is a possible explanation

O6-A changes only the figure in ch06:192 (0.07 % → 0.08 %). The rest of that sentence read "the pattern is consistent
with electroweak-scale renormalization-group running … where the larger $m_\tau$ Yukawa receives proportionally smaller
logarithmic corrections", which asserts the mechanism in its clause. The adjustment states the running as one possible
explanation and adds that the mass ratios do not establish it; the figures and the rest of the sentence are unchanged.
The adjustment does not overlap O6-i-2's span on the same line. A grep for the reading ("running of the lepton",
"logarithmic corrections than", "0.0595", "0.84 %") finds no other site in the corpus, so ch06:192 and its FULL mirror
are the only places it appears. The relabelled O6-A table rows (ch06:190, :305, :217–218) state what each closure
computes and make no mechanism claim.

`book/ch06-matter-content.md:192` [FULL:1718]:

> OLD: — the pattern is consistent with electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, where the larger $m_\tau$ Yukawa receives proportionally smaller logarithmic corrections than the small $m_e$ Yukawa.
>
> NEW: — one possible explanation of the pattern is electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, in which the larger $m_\tau$ Yukawa would receive proportionally smaller logarithmic corrections than the small $m_e$ Yukawa; the agreement of the mass ratios does not by itself establish that running.

## Residue found by the re-grep (two sites not in DECISIONS)

The re-grep for "0.02 %" attached to θ₀ found two sites that the audit, the review and DECISIONS did not list. Both
carry the stale θ₀ figure that the T entries correct, and both are corrected the same way:

- **R1** `book/ch06-matter-content.md:179` [FULL:1705]: "the empirical match at $0.02\%$ confirms a derived
  normalization" → "$0.001\%$". This is the book's statement of SM:928's sentence, "The empirical match at $0.02\%$
  does not *select* the normalization", which T2b corrects to $0.001\%$. The match is the θ₀ = $C_2/d^2$ match.
- **R2** `book/ch07-gravity.md:8` [FULL:1887]: "twenty-two classified SM observables … with the measured comparisons
  spanning $0.02\%$ to $1.2\%$" → "$0.0003\%$ to $1.2\%$". The range is over the twenty-two observables of SM §7.6.
  Its lower end was θ₀'s stale figure, although Koide $Q$ already stood at "< 0.01 %" there. After T4 and O7a-4 the
  tightest percent-quoted entry of that table is Koide $Q$ at $0.0003\%$ (SM:1267). The upper end, $1.2\%$, is
  unchanged.

R2 is a count-derived figure that follows mechanically from O7-a and the T entries. It is listed separately so that
the independent review can confirm the choice of $Q$'s figure for the lower end.

## Coverage ledger: SUBSTRATUM:T-23 re-affirmed

O1-3 changes Theorem 23's statement (Substratum:192). `tools/coverage_check.py` then reported the expected single
failure, `STALE entry SUBSTRATUM:T-23 (b69a16c2e08bd93f -> e6bf53b0d2ae0955)`. The new fingerprint equals the value
DECISIONS precomputed for the O1-3 text, because the applied wording is DECISIONS' verbatim.

Before re-affirming, the entry was re-read against the new statement:
- **Mapping.** The entry still points at `papers/Substratum.md` line 192, kind Theorem, label 23, area
  `reconstruction`; the line holds Theorem 23. Unchanged.
- **Level.** `kernel: "GAP"`. No kernel anchor names Theorem 23 or Stage 3: a grep of
  `verification/lean-manuscript-census.json`, `lean/`, `lean-mathlib/` and `tools/` finds none. The added hypothesis
  narrows the ħ clause and claims nothing more of a kernel, so GAP still holds.
- **Delta.** `"not formalized"`: still true.
- **Assumptions.** `"see the statement"`: the statement now names H-slope with the horizon and frame conditions, so
  the pointer covers the new hypothesis.

Only the fingerprint changed: `"b69a16c2e08bd93f"` → `"e6bf53b0d2ae0955"`. `coverage_check` is then OK (128 canonical
statements). §A.35 needs no registry change: no Lean anchor is involved.

### Open: two Stage-3 ħ statements beside Theorem 23

These are not edited here and are left for the review and the owner:
- Substratum:188, **Lemma 23.0**, ledger entry `SUBSTRATUM:L-23.0`, states "the same Stage-3 value of $\hbar$"; its
  proof says "Stage 3 fixes the same gap-equation value".
- Substratum:194, **Theorem 23's proof**, says "Stage 3 uniquely fixes $\hbar$".

Stage 3 is now conditional on H-slope (O1-2), but neither sentence names that condition. Theorem 23's proof runs under
the theorem's hypotheses, which now include H-slope for the ħ clause. Lemma 23.0's statement does not include it.
Adding it would change `SUBSTRATUM:L-23.0`'s fingerprint and need its own re-affirmation. Neither site was in the audit,
the review or DECISIONS, so it is reported rather than applied.

## Every site, old → new

Each entry gives the source line and, for a book source, the FULL line that carries the same edit. The O4a texts are the applied (adjusted) ones; DECISIONS' versions are quoted in the adjustments section above.

### Sites: ħ corrections (no decision) (46)

**H1** `book/ch07-gravity.md:10` [FULL:1889]
```text
OLD: The horizon's geometric and thermodynamic properties — surface gravity $\kappa$, area $A$, Hawking temperature $T$ — fix the values of the emergent physics: the action scale $\hbar$, the Bekenstein-Hawking entropy with its $1/4$ coefficient, the form of the dark-energy equation of state.
NEW: The horizon's thermodynamics relates the emergent action scale $\hbar$ to the discreteness scale $\epsilon$, with $\kappa$ and $A$ dropping out of $\hbar$ (Sections 7.3–7.4); it recovers the Bekenstein-Hawking entropy with its $1/4$ coefficient as a consistency relation of that calibration and supplies the dark-energy bookkeeping read in the running-vacuum channel (Section 7.8).
```

**H2** `book/ch07-gravity.md:14` [FULL:1893]
```text
OLD: the value of $\hbar$, the discreteness scale
NEW: the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the discreteness scale
```

**H3** `book/ch07-gravity.md:36` [FULL:1915]
```text
OLD: The most distinctive content of the framework's gravitational sector is the derivation of Planck's constant $\hbar$ as an emergent quantity determined by the cosmological horizon's thermodynamic properties. The standard view treats $\hbar$ as a fundamental constant of nature whose value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ is measured rather than derived.
NEW: The most distinctive content of the framework's gravitational sector is the treatment of Planck's constant $\hbar$ as an emergent action scale whose relation to the boundary geometry is fixed by the cosmological horizon's thermodynamics. The standard view treats $\hbar$ as a fundamental constant of nature, its value $1.055 \times 10^{-34}\,\mathrm{J\cdot s}$ measured.
```

**H4** `book/ch07-gravity.md:50` [FULL:1929]
```text
OLD: a QFT on a bifurcate Killing horizon, under the H-Hawking conditions, background must be periodic in imaginary time with period $\beta = 2\pi c / \kappa$, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$. This is a theorem *within* the derived QFT, not an external import — the regularity requirement follows from the Wick rotation's analytic structure.
NEW: a QFT on this bifurcate Killing horizon background is periodic in imaginary time with period $\beta = 2\pi c / \kappa$ under the H-Hawking conditions, giving a KMS state at temperature $T_Q = \hbar \kappa / (2\pi c k_B)$ when the emergent state belongs to that KMS class (H-spectrum). The step is therefore a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2]).
```

**H5** `book/ch07-gravity.md:82` [FULL:1961]
```text
OLD: This is not an additional empirical input but an algebraic consequence of the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ together with the definition of $l_p$.
NEW: It adds no relation beyond the structural commitment $\hbar = c^3 \epsilon^2 / (4G\sigma)$ and the definition of $l_p$, and its numerical value takes the measured $\hbar$ as input.
```

**H6** `book/ch01-observation.md:87` [FULL:431]
```text
OLD: Chapter 7 shows that the cosmological partition produces $\hbar$ as a thermodynamic identity at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following under the horizon conditions named there
NEW: Chapter 7 shows that, under the horizon conditions named there, the cosmological partition relates $\hbar$ to the discreteness scale through a thermal self-consistency condition at the horizon surface, with $1/4$ Bekenstein-Hawking entropy following
```

**H7** `book/ch02-substratum.md:22` [FULL:665]
```text
OLD: Chapter 7 develops each of these as theorems;
NEW: Chapter 7 develops each of these under the conditions it names;
```

**H8** `book/ch02-substratum.md:110` [FULL:753]
```text
OLD: Stage 3 takes Stage 2's output and derives the emergent value of $\hbar$. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics — forces the relation
NEW: Stage 3 takes Stage 2's output and derives the emergent action-scale relation. The argument is that thermal self-consistency at the partition boundary — established in Chapter 7 from the boundary layer's emergent thermodynamics, conditional on H-slope with the horizon and frame conditions named there — forces the relation
```

**H9** `book/ch02-substratum.md:112` [FULL:755]
```text
OLD: as the unique simultaneous solution.
NEW: as the unique simultaneous solution, which fixes only the ratio $\epsilon/\sqrt{\sigma} = 2\,\ell_P$.
```

**H10** `book/ch02-substratum.md:228` [FULL:871]
```text
OLD: the boundary thermodynamics, the value of $\hbar$, the Bekenstein-Hawking
NEW: the boundary thermodynamics, the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking
```

**H11** `book/ch00-introduction.md:97` [FULL:333]
```text
OLD: the Bekenstein-Hawking $1/4$ factor and the value of $\hbar$ from horizon thermodynamics under named horizon conditions
NEW: the Bekenstein-Hawking $1/4$ factor and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ as consistency relations of horizon thermodynamics under named horizon conditions
```

**H12** `book/ch04-methodology.md:204` [FULL:1323]
```text
OLD: the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from horizon thermodynamics are conditional on
NEW: the Bekenstein-Hawking $1/4$ coefficient and the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ from horizon thermodynamics are consistency relations conditional on
```

**H13** `book/ch06-matter-content.md:348` [FULL:1874]
```text
OLD: the value of $\hbar$ from horizon thermodynamics,
NEW: the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ relating the action scale to the discreteness scale (a self-consistency condition, §7.4),
```

**H14a** `book/ch09-universality.md:14` [FULL:2494]
```text
OLD: Some predictions are *universality-class* results
NEW: Some results are *universality-class* results
```

**H14b** `book/ch09-universality.md:14` [FULL:2494]
```text
OLD: the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry conditional on the horizon conditions named in Chapter 7
NEW: the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$ from partition geometry, consistency relations conditional on the horizon conditions named in Chapter 7
```

**H15** `book/ch09-universality.md:48` [FULL:2528]
```text
OLD: the Bekenstein-Hawking $1/4$ coefficient and the value of $\hbar$ from partition geometry sit at the same level
NEW: the Bekenstein-Hawking $1/4$ coefficient and the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, consistency relations, sit at the same level
```

**H16** `book/ch09-universality.md:92` [FULL:2572]
```text
OLD: *The value of $\hbar$ from partition geometry.*
NEW: *The action-scale relation from partition geometry.*
```

**H17** `book/ch09-universality.md:118` [FULL:2598]
```text
OLD: Bekenstein-Hawking $1/4$ and $\hbar$ from partition geometry under the horizon conditions of Chapter 7
NEW: the Bekenstein-Hawking $1/4$ and the action-scale relation for $\hbar$ as consistency relations under the horizon conditions of Chapter 7
```

**H18** `book/ch12-evolution-intelligence.md:197` [FULL:3449]
```text
OLD: — the value of $\hbar$, the Standard Model,
NEW: — the action-scale relation $\hbar = c^3\epsilon^2/(4G\sigma)$, the Standard Model,
```

**H19** `book/glossary.md:73` [FULL:6673]
```text
OLD: The framework's derivation of Planck's constant from horizon thermodynamics.
NEW: It relates Planck's constant to the discreteness scale, conditional on H-slope, and fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$: a self-consistency condition, not an independent determination of the value of $\hbar$.
```

**H20** `book/readers-guide.md:77` [FULL:177]
```text
OLD: the gap equation deriving $\hbar$
NEW: the gap equation relating $\hbar$ to the discreteness scale
```

**H21** `book/appendix-b-derivations.md:16` [FULL:5783]
```text
OLD: The framework derives Planck's constant $\hbar$ from a thermal self-consistency argument
NEW: The framework relates Planck's constant $\hbar$ to the discreteness scale through a thermal self-consistency argument
```

**H22** `book/appendix-b-derivations.md:173` [FULL:5940]
```text
OLD: The framework derives Planck's constant $\hbar$ as the unique self-consistent value matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory.
NEW: The framework derives the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ between Planck's constant and the discreteness scale by matching the classical horizon temperature to the KMS temperature of the emergent quantum field theory, conditional on H-slope with the horizon and frame conditions of Chapter 7 §7.3; with $\epsilon$ not independently known, it fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ (Chapter 7 §7.4), not the value of $\hbar$.
```

**H23** `book/appendix-b-derivations.md:211` [FULL:5978]
```text
OLD: with $\hbar$ unknown. This is a theorem *within* the derived QFT, not an external import.
NEW: with $\hbar$ unknown. The periodicity holds under the H-Hawking conditions and the KMS identification requires the emergent state to belong to that class (H-spectrum), so the matching below is a conditional infrared calibration, not a theorem within the derived QFT ([GR §3.2]).
```

**H24** `book/appendix-b-derivations.md:471` [FULL:6238]
```text
OLD: B.4 establishes the gap equation determining $\hbar$ from horizon thermodynamics
NEW: B.4 establishes the gap equation relating $\hbar$ to the discreteness scale through horizon thermodynamics
```

**H25** `book/appendix-c-objections.md:20` [FULL:6266]
```text
OLD: the gap equation deriving $\hbar$)
NEW: the gap equation for $\hbar$)
```

**H26** `book/appendix-c-objections.md:236` [FULL:6482]
```text
OLD: ## C.10 Circularity concerns: the gap equation deriving $\hbar$
NEW: ## C.10 Circularity concerns: the gap equation for $\hbar$
```

**H27** `book/appendix-c-objections.md:238` [FULL:6484]
```text
OLD: the framework's gap equation in Chapter 7 §7.4, which derives the Planck constant $\hbar$ from the cosmological horizon's geometric properties.
NEW: the framework's gap equation in Chapter 7 §7.3, which relates the Planck constant $\hbar$ to the discreteness scale through the cosmological horizon's thermodynamics.
```

**H28** `book/appendix-c-objections.md:242` [FULL:6488]
```text
OLD: The logical chain in Chapter 7 §7.4
NEW: The logical chain in Chapter 7 §7.3
```

**H29** `book/appendix-c-objections.md:257` [FULL:6503]
```text
OLD: - Classical-temperature matching → $\hbar$ fixed.
NEW: - Classical-temperature matching → $\hbar$ fixed in terms of $\epsilon$ (conditional on H-slope, Chapter 7 §7.3).
```

**H30** `book/appendix-c-objections.md:263` [FULL:6509]
```text
OLD: The framework's derivation of $\hbar$ is therefore consistent
NEW: The gap equation is therefore consistent
```

**H31** `book/README.md:64` (not mirrored in FULL)
```text
OLD: the framework's $\hbar$ derivation from thermal self-consistency at the cosmological horizon
NEW: the framework's action-scale relation for $\hbar$ from thermal self-consistency at the cosmological horizon
```

**H32** `papers/GR.md:18`
```text
OLD: — the value of $\hbar$, the Bekenstein-Hawking area law,
NEW: — the origin of the action scale $\hbar$, the Bekenstein-Hawking area law,
```

**H33** `papers/GR.md:170`
```text
OLD: Step 4 will fix its value via thermal matching.
NEW: Step 4 will fix it in terms of $\epsilon$ via thermal matching.
```

**H34** `papers/GR.md:336`
```text
OLD: The framework's predictions in Part II ($\hbar$, $S_{\text{dS}}$, the Type II RVM form of the dark energy) depend on
NEW: The framework's Part II results (the calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, $S_{\text{dS}}$, the Type II RVM reading of the dark energy) depend on
```

**H35** `papers/Main.md:684`
```text
OLD: the framework derives $\hbar$ and the Bekenstein–Hawking coefficient downstream, and the derived bound
NEW: the framework relates $\hbar$ to the discreteness scale and recovers the Bekenstein–Hawking coefficient downstream, as consistency relations of its horizon calibration [GR §3–§5], and the derived bound
```

**H36** `papers/SM.md:1350`
```text
OLD: including the derivation of $\hbar$, the Bekenstein-Hawking area law, the dissolution of the cosmological constant problem,
NEW: including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$, the Bekenstein-Hawking area law, the conditional dissolution of the cosmological constant problem ([GR §6.2]),
```

**H37** `papers/SM.md:1576`
```text
OLD: including the derivation of $\hbar$ from the cosmological horizon and the Bekenstein-Hawking area law including the $1/4$ coefficient (both conditional on the horizon conditions recorded there)
NEW: including the horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking area law with its $1/4$ coefficient (consistency relations, both conditional on the horizon conditions recorded there)
```

**H38** `papers/SM.md:1378`
```text
OLD: , ℏ = c³ε²/(4G), the Bekenstein-Hawking formula, and the universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). These are theorems.
NEW: , and the universal induced coupling $1/\alpha_0 = 23.25$ (§6.1). These are theorems on the branch stated in §1 (Tier 2), with the conditions marked at each entry. The horizon calibration $\hbar = c^3\epsilon^2/(4G\sigma)$ and the Bekenstein-Hawking coefficient it matches hold for the same class as consistency relations conditional on H-slope ([GR §3.2, §4–§5]).
```

**H39** `papers/Substratum.md:22`
```text
OLD: the framework determines $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, for an entropy $\sigma$ per boundary mode, the Bekenstein-Hawking entropy with the $1/4$ coefficient, and the dissolution of the cosmological constant problem.
NEW: the framework relates the action scale to the discreteness scale through the calibration $\hbar = c^3 \epsilon^2 / (4G\sigma)$, which fixes only $\epsilon/\sqrt{\sigma} = 2\,l_p$ for an entropy $\sigma$ per boundary mode, and recovers the Bekenstein-Hawking entropy with the $1/4$ coefficient as a consistency relation of that calibration, both conditional on H-slope [GR §3.2], and proposes a dissolution of the cosmological constant problem conditional on the covariant coupling step [GR §6.2].
```

**H40** `papers/Substratum.md:178`
```text
OLD: **Output:** The emergent value of $\hbar$ is $\hbar = c^3 \epsilon^2 / (4G\sigma)$ with $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length and $\sigma$ the entropy per boundary mode ([GR §3.1]).
NEW: **Output:** The emergent action-scale relation $\hbar = c^3 \epsilon^2 / (4G\sigma)$, equivalently $\epsilon = 2\sqrt{\sigma}\,l_p$, where $l_p$ is the Planck length and $\sigma$ the entropy per boundary mode ([GR §3.1]); it fixes only $\epsilon/\sqrt{\sigma}$, not the value of $\hbar$ ([GR §4]).
```

**H41** `papers/Substratum.md:180`
```text
OLD: detailed balance (consequence of $\varphi$ being a bijection). No new structural assumptions beyond Stages 1–2.
NEW: and the infrared detailed-balance condition H-slope with the horizon and frame conditions ([GR §2, §3.2, §8.5]), which does not follow from $\varphi$ being a bijection ([GR §3.2]) and is an assumption beyond Stages 1–2.
```

**H42** `papers/Explainer.md:411`
```text
OLD: The value of ℏ is determined by the partition geometry — which is what Section 5 derives.
NEW: The action scale ℏ is fixed by the partition geometry in terms of the discreteness scale — which is what Section 5 derives.
```

**H43** `papers/Explainer.md:477`
```text
OLD: The gap equation relates one free geometric parameter (ε), at given σ, to one output (ℏ).
NEW: The gap equation, conditional on the infrared detailed-balance condition H-slope with the horizon and frame conditions [GR §3.2], relates one free geometric parameter (ε), at given σ, to one output (ℏ).
```

**H44** `papers/Explainer.md:662`
```text
OLD: It makes quantitative predictions — the value of ℏ and dark energy evolution — that interpretations do not, and it accounts for
NEW: It relates ℏ to the discreteness scale and carries a running-vacuum reading of dark energy whose falsifiable content is the Type II channel ([GR §7.1]) — content that interpretations do not have — and it accounts for
```

**H45** `papers/Explainer.md:992`
```text
OLD: which derives ℏ, the Bekenstein-Hawking area law, and dark-sector phenomenology
NEW: which relates ℏ to the discreteness scale, recovers the Bekenstein-Hawking area law, and develops dark-sector phenomenology
```

### Sites: θ₀ figure and labels (no decision) (19)

**T1** `papers/SM.md:14`
```text
OLD: the Koide angle $\theta_0 = 2/9$ to $0.02\%$
NEW: the Koide angle $\theta_0 = 2/9$ to $0.001\%$
```

**T2a** `papers/SM.md:928`
```text
OLD: misses the observed $0.2227$ by a factor of four
NEW: misses the observed $0.2222$ by a factor of four
```

**T2b** `papers/SM.md:928`
```text
OLD: The empirical match at $0.02\%$ does not
NEW: The empirical match at $0.001\%$ does not
```

**T3** `papers/SM.md:934`
```text
OLD: (observed $0.2227$)
NEW: (observed $0.222225$)
```

**T4** `papers/SM.md:1318`
```text
OLD: | Koide $\theta_0$ | $C_2/d^2 = 2/9$ | 0.2222 | 0.2222 | 0.02% |
NEW: | Koide $\theta_0$ | $C_2/d^2 = 2/9$ | 0.22222 | 0.222225 | 0.001% |
```

**T5** `papers/SM.md:1329`
```text
OLD: $\theta_0$ at $0.02\%$)
NEW: $\theta_0$ at $0.001\%$)
```

**T6** `papers/SM.md:1572`
```text
OLD: the Koide angle from the cubic-group quadratic Casimir to $0.02\%$
NEW: the Koide angle from the cubic-group quadratic Casimir to $0.001\%$
```

**T7** `papers/Juno.md:401`
```text
OLD: Koide θ₀ (0.02%)
NEW: Koide θ₀ (0.001%)
```

**T8** `papers/Substratum.md:446`
```text
OLD: (0.02%)
NEW: (0.001%)
```

**T9** `book/README.md:62` (not mirrored in FULL)
```text
OLD: Koide $\theta_0 = 2/9$ at $0.02\%$
NEW: Koide $\theta_0 = 2/9$ at $0.001\%$
```

**T10** `book/ch05-gauge-structure.md:196` [FULL:1525]
```text
OLD: the Koide relation $2/9$ matched to $0.02\%$
NEW: the Koide angle $\theta_0 = 2/9$ matched to $0.001\%$
```

**T11** `book/ch06-matter-content.md:171` [FULL:1697]
```text
OLD: which is the angular form of the $Q = 2/3$ relation under the standard $\mathbb{Z}_3$-symmetric parametrization of three masses by an angle. The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222220$ at $0.02\%$
NEW: which is the phase of the standard $\mathbb{Z}_3$-symmetric parametrization of three masses, independent of the amplitude that $Q = 2/3$ fixes (SM §7.2). The framework's prediction matches the observed value $\theta_0^{\text{obs}} = 0.222225 \pm 0.000006$ at $0.001\%$ ($0.4\sigma$)
```

**T12** `book/ch06-matter-content.md:303` [FULL:1829]
```text
OLD: | $2/9$ | $0.22222$ | $0.02\%$ |
NEW: | $2/9$ | $0.222225$ | $0.001\%$ |
```

**T13** `book/ch08-juno.md:68` [FULL:2271]
```text
OLD: the Koide angle at $0.02\%$
NEW: the Koide angle at $0.001\%$
```

**T14** `book/ch08-juno.md:177` [FULL:2380]
```text
OLD: the Koide angle at $0.02\%$
NEW: the Koide angle at $0.001\%$
```

**T15** `book/ch08-juno.md:210` [FULL:2413]
```text
OLD: the Koide angle at $0.02\%$
NEW: the Koide angle at $0.001\%$
```

**T16** `book/ch03-structural-realism.md:42` [FULL:918]
```text
OLD: the Koide relation $2/9$
NEW: the Koide angle $2/9$
```

**T17** `book/ch03-structural-realism.md:118` [FULL:994]
```text
OLD: the Koide relation as $2/9$
NEW: the Koide angle as $2/9$
```

**T18** `book/appendix-a-prediction-status.md:80` [FULL:5617]
```text
OLD: | C | 1 | Within 1% | Ch 6 §6.5 |
NEW: | C | 1 | 0.001% | Ch 6 §6.5 |
```

### Sites: Stale $m_\tau$ = 1776.86 mass rows (no decision) (8)

**M1** `papers/SM.md:1269`
```text
OLD: | 0.51096 MeV | 0.51100 MeV | 0.007% |
NEW: | 0.51098 MeV | 0.51100 MeV | 0.003% |
```

**M2** `papers/SM.md:1270`
```text
OLD: | 105.652 MeV | 105.658 MeV | 0.006% |
NEW: | 105.656 MeV | 105.658 MeV | 0.002% |
```

**M3** `book/ch06-matter-content.md:12` [FULL:1538]
```text
OLD: $\theta_0 = 2/9$ — at $0.007\%$.
NEW: $\theta_0 = 2/9$ — at $0.003\%$.
```

**M4a** `book/ch06-matter-content.md:181` [FULL:1707]
```text
OLD: (the tau mass $m_\tau = 1776.86$ MeV)
NEW: (the tau mass $m_\tau = 1776.93$ MeV)
```

**M4b** `book/ch06-matter-content.md:181` [FULL:1707]
```text
OLD: $m_e = 0.51096$ MeV and $m_\mu = 105.652$ MeV against $0.51100$ and $105.658$ observed ($0.007\%$ and $0.006\%$; SM §7.2)
NEW: $m_e = 0.51098$ MeV and $m_\mu = 105.656$ MeV against $0.51100$ and $105.658$ observed ($0.003\%$ and $0.002\%$; SM §7.2)
```

**M5** `book/ch06-matter-content.md:189` [FULL:1715]
```text
OLD: | $0.51096$ MeV | $0.5110$ | $0.007\%$ |
NEW: | $0.51098$ MeV | $0.51100$ | $0.003\%$ |
```

**M6** `book/ch06-matter-content.md:304` [FULL:1830]
```text
OLD: | $0.51096$ MeV | $0.51100$ MeV | $0.007\%$ |
NEW: | $0.51098$ MeV | $0.51100$ MeV | $0.003\%$ |
```

**M7** `book/ch06-matter-content.md:344` [FULL:1870]
```text
OLD: ($m_e$ at $0.007\%$ and $m_\mu$ at $0.006\%$
NEW: ($m_e$ at $0.003\%$ and $m_\mu$ at $0.002\%$
```

### Sites: O1-A (5)

**O1-1** `papers/Substratum.md:182`
```text
OLD: ([GR §3, Theorem])
NEW: ([GR §3.2])
```

**O1-2** `papers/Substratum.md:184`
```text
OLD: **Status:** Theorem.
NEW: **Status:** Conditional on H-slope with the horizon and frame conditions ([GR §3.2]).
```

**O1-3** `papers/Substratum.md:192`
```text
OLD: and $\hbar=c^3\epsilon^2/(4G\sigma)$, with the same qualifications stated in [SM] for H-spin', H-χ', and the CKM-CP fork.
NEW: and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope with the horizon and frame conditions of [GR §3.2], with the same qualifications stated in [SM] for H-spin', H-χ', and the CKM-CP fork.
```

**O1-4** `papers/Structure.md:47`
```text
OLD: and $\hbar=c^3\epsilon^2/(4G\sigma)$, $\sigma$ the entropy per boundary mode [GR §3.1].
NEW: and $\hbar=c^3\epsilon^2/(4G\sigma)$ conditional on H-slope [GR §3.2], $\sigma$ the entropy per boundary mode [GR §3.1].
```

**O1-5** `papers/Methodology.md:339`
```text
OLD: and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$ tying Planck's constant
NEW: and the relation $\hbar = c^3\epsilon^2/(4G\sigma)$, conditional on H-slope ([GR §3.2]), tying Planck's constant
```

### Sites: O2-a (3)

**O2a-1** `book/ch06-matter-content.md:320` [FULL:1846]
```text
OLD: Koide $Q = 2/3$ (and equivalently Koide $\theta_0 = 2/9$ — the same prediction in dual form), and $\lambda(M_{\text{Pl}}) = 0$ from composite-Higgs structure. These seven relations are tested through five empirical channels
NEW: Koide $Q = 2/3$, Koide $\theta_0 = 2/9$ (independent of $Q$: the amplitude and the phase of the same parametrization, SM §7.2), and $\lambda(M_{\text{Pl}}) = 0$ from composite-Higgs structure. These eight relations are tested through five empirical channels
```

**O2a-2** `book/ch06-matter-content.md:320` [FULL:1846]
```text
OLD: lepton-mass dynamics (Koide $Q$)
NEW: lepton-mass dynamics (Koide $Q$ and $\theta_0$)
```

**O2a-3** `book/ch06-matter-content.md:332` [FULL:1858]
```text
OLD: eight Category A rows representing seven independent relations (the Koide relation and its angle have separate rows)
NEW: eight Category A rows, one for each relation
```

### Sites: O3-b (1)

**O3b-1** `book/ch09-universality.md:71` [FULL:2551]
```text
OLD: | Level G4 (universality class) | $S = A/(4 l_p^2)$, CC dissolution, $\hbar$ from partition geometry, RVM form | structural ($1/4$ untested directly) |
NEW: | Level G4 (universality class) | RVM reading (form shared by every smooth model) | non-discriminating; the consistency relations $S = A/(4l_p^2)$ and $\hbar = c^3\epsilon^2/(4G\sigma)$ and the descriptive CC distinction are stated in Chapter 7 §7.10 |
```

### Sites: O3-76 (applies under O3-b) (1)

**O3-76** `book/ch09-universality.md:76` [FULL:2556]
```text
OLD: with the strongest confirmations at the universality-class level and the open research program
NEW: with the universality-class level consistent with observation rather than sharply tested and the open research program
```

### Sites: O4-a (as adjusted for the owner's qualification) (2)

**O4a-1** `papers/SM.md:940`
```text
OLD: The $0.2\%$ agreement of $\theta_0 = 2/9$ bounds the taste-structured part of an emergent mass-level dressing by $\delta m/m \lesssim 8 \times 10^{-5}$; a second-order lepton-Yukawa loop supplies $\sim 10^{-6}$.
NEW: In this linear-response model, with $\kappa \approx -35$ and $\lambda_E/\lambda_{A_1} = 0.22$–$0.24$, the agreement of $\theta_0 = 2/9$ with the observed $\theta_0 = 0.222225 \pm 0.000006$ ($0.001\%$, $0.4\sigma$) bounds the taste-structured part of an emergent mass-level dressing to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence (two-sided); the interval is conditional on that response model, its sensitivity coefficient and the range of $\lambda_E/\lambda_{A_1}$, and is not a model-independent exclusion. A second-order lepton-Yukawa loop, of order $10^{-6}$, is compatible with the interval for either sign, by a factor of about two; the comparison is not decisive, and the loop estimate is not a confirmed prediction.
```

**O4a-2** `book/ch06-matter-content.md:179` [FULL:1705]
```text
OLD: constrains it to $\delta m/m \lesssim 8 \times 10^{-5}$, which a lepton-Yukawa loop satisfies (SM §7.2).
NEW: constrains it to $-2.5 \times 10^{-6} \lesssim \delta m/m \lesssim 1.7 \times 10^{-6}$ at 95% confidence, conditional on the linear response of $\theta_0$ to the dressing (sensitivity coefficient $\kappa \approx -35$, with $\lambda_E/\lambda_{A_1}$ in the range above) rather than as a model-independent exclusion; a lepton-Yukawa loop of order $10^{-6}$ is compatible with that interval for either sign, by a factor of about two, but is not a confirmed prediction (SM §7.2).
```

### Sites: O5-a (7)

**O5a-1** `book/ch04-methodology.md:134` [FULL:1253]
```text
OLD: (matched to $0.001\%$, the sharpest empirical agreement in the framework)
NEW: (matched to $0.001\%$)
```

**O5a-2** `book/ch06-matter-content.md:171` [FULL:1697]
```text
OLD:  — the sharpest empirical agreement in the framework.
NEW: .
```

**O5a-3** `papers/Substratum.md:446`
```text
OLD: — the sharpest empirical match in the framework
NEW: — matched to observation
```

**O5a-4** `papers/SM.md:1329`
```text
OLD: the two tightest (
NEW: two of the tightest (
```

**O5a-5** `book/appendix-a-prediction-status.md:215` [FULL:5752]
```text
OLD: — the framework's sharpest individual empirical match.
NEW: — the framework's sharpest individual empirical match in relative precision.
```

**O5a-6** `book/ch06-matter-content.md:12` [FULL:1538]
```text
OLD: , the sharpest empirical agreement in the framework,
NEW: , the sharpest empirical agreement in the framework in relative precision,
```

**O5a-7** `book/appendix-a-prediction-status.md:98` [FULL:5635]
```text
OLD: — the sharpest framework prediction across all 23,
NEW: — the sharpest framework prediction across all 23 in relative precision,
```

### Sites: O6-A (5)

**O6-i-1** `book/ch06-matter-content.md:190` [FULL:1716]
```text
OLD: | $m_\mu$ | Koide closure with $m_e$, $m_\tau$ | $105.74$ MeV | $105.66$ | $0.07\%$ |
NEW: | $m_\mu$ | Koide closure with the structural $m_e/m_\tau = 1/(36\pi^4)$ and $m_\tau$ | $105.74$ MeV | $105.66$ | $0.08\%$ |
```

**O6-i-2** `book/ch06-matter-content.md:192` [FULL:1718]
```text
OLD: agrees with observation more tightly ($0.07\%$)
NEW: agrees with observation more tightly ($0.08\%$)
```

**O6-ii** `book/ch06-matter-content.md:305` [FULL:1831]
```text
OLD: | $m_\mu$ | Koide closure | $105.74$ MeV | $105.66$ MeV | $0.07\%$ |
NEW: | $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | $105.656$ MeV | $105.658$ MeV | $0.002\%$ |
```

**O6-iii-1** `book/ch06-matter-content.md:217` [FULL:1743]
```text
OLD: | Layer 1 | $0.51096$ MeV | $0.511$ | $0.007\%$ |
NEW: | Layer 1 | $0.505$ MeV | $0.511$ | $1.2\%$ |
```

**O6-iii-2** `book/ch06-matter-content.md:218` [FULL:1744]
```text
OLD: | $m_\mu$ | Koide closure | Layer 1 | $105.74$ MeV | $105.66$ | $0.07\%$ |
NEW: | $m_\mu$ | Koide$(Q, \theta_0;\, m_\tau)$ | Layer 1 | $104.4$ MeV | $105.66$ | $1.2\%$ |
```

### Sites: O7-a (6)

**O7a-1** `book/ch00-introduction.md:77` [FULL:313]
```text
OLD: the observed value is $0.666661 \pm 0.000007$, a match to better than $0.001\%$ ($0.8\sigma$)
NEW: the observed value is $0.666664 \pm 0.000005$, a match to better than $0.001\%$ ($0.4\sigma$)
```

**O7a-2** `book/glossary.md:97` [FULL:6697]
```text
OLD: Observed value $Q = 0.666661 \pm 0.000007$.
NEW: Observed value $Q = 0.666664 \pm 0.000005$.
```

**O7a-3** `book/glossary.md:97` [FULL:6697]
```text
OLD: the match is better than $0.001\%$ ($0.8\sigma$)
NEW: the match is better than $0.001\%$ ($0.4\sigma$)
```

**O7a-4** `papers/SM.md:1267`
```text
OLD: | 0.66667 | 0.66666 | $< 0.01\%$ |
NEW: | 0.66667 | 0.666664 | $0.0003\%$ |
```

**O7a-5** `book/ch06-matter-content.md:302` [FULL:1828]
```text
OLD: | $2/3$ | $0.66667$ | $0.001\%$ |
NEW: | $2/3$ | $0.666664$ | $0.0003\%$ |
```

**O7a-6** `book/ch06-matter-content.md:12` [FULL:1538]
```text
OLD: matched to $0.001\%$
NEW: matched to $0.0003\%$
```

### Sites: O6 qualification adjustment (ch06:192) (1)

**Q6-rg** `book/ch06-matter-content.md:192` [FULL:1718]
```text
OLD: — the pattern is consistent with electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, where the larger $m_\tau$ Yukawa receives proportionally smaller logarithmic corrections than the small $m_e$ Yukawa.
NEW: — one possible explanation of the pattern is electroweak-scale renormalization-group running of the lepton Yukawa couplings from the substrate (compositeness) scale to the electroweak scale, in which the larger $m_\tau$ Yukawa would receive proportionally smaller logarithmic corrections than the small $m_e$ Yukawa; the agreement of the mass ratios does not by itself establish that running.
```

### Sites: Residue found by the re-grep (not in DECISIONS) (2)

**R1** `book/ch06-matter-content.md:179` [FULL:1705]
```text
OLD: the empirical match at $0.02\%$ confirms
NEW: the empirical match at $0.001\%$ confirms
```

**R2** `book/ch07-gravity.md:8` [FULL:1887]
```text
OLD: with the measured comparisons spanning $0.02\%$ to $1.2\%$
NEW: with the measured comparisons spanning $0.0003\%$ to $1.2\%$
```

## Rebuilt artifacts

`sh ./build.sh GR SM Main Substratum Structure Methodology Explainer Juno` and `sh ./build.sh --book`: `build: OK`
both times, with no dropped glyphs reported. `book/README.md` is not built.

| Artifact | Pages before | Pages after | Characters per page |
|---|---|---|---|
| GR | 87 | 87 | 3150 |
| SM | 146 | 146 | 3119 |
| Main | 90 | 90 | 3246 |
| Substratum | 52 | 52 | 3200 |
| Structure | 98 | 98 | 2847 |
| Methodology | 54 | 54 | 3016 |
| Explainer | 69 | 69 | 2780 |
| Juno | 22 | 22 | 2477 |
| Book (FULL) | 555 | 556 | 2961 |

## Checks (local, on the edited tree)

| Check | Result |
|---|---|
| `tools/toolchain_check.py` | OK |
| `tools/staleness_check.py` | OK (10 matched, 3 unstamped) |
| `tools/voice_check.py` | OK (40 manuscript files) |
| `tools/voice_scope_test.py` | OK |
| `tools/artifact_placement_check.py` | OK (self-test passed) |
| `tools/build_migration_manifest.py --check` | OK |
| `tools/claims_check.py` | OK |
| `tools/duplicate_check.py` | OK |
| `tools/dependency_label_check.py --strict` | OK (41 files) |
| `tools/coverage_check.py` | OK (128 canonical statements), after the T-23 re-affirmation; before it, the one expected STALE |
| `tools/lean_manuscript_census.py` | OK |
| `tools/legacy_records_check.py` | self-test OK; 303 records in 75 closed namespaces, all intact |
| `tools/citation_roles_check.py` | self-test OK; 0 manifests, all hold |
| `papers/oi_lattice_code/mirror_check.py` | 0 chapter lines absent from FULL |
| `papers/oi_lattice_code/citation_check.py` | 112 citations, 0 broken, 0 duplicate bib numbers |
| `papers/oi_lattice_code/architecture_check.py` | 259 invariants, 0 violations, 0 self-test failures |

`lean_axiom_check`, the `v3` steps and the full release gate run in CI (§A.40).

**Replay.** `decisions/apply.py` was re-run on a fresh `git archive` of the merge commit `4ed4c6e6`. It applied the same
106 edits, and every `papers/*.md` and `book/*.md` file it produced is byte-identical to the committed tree.

**§A.32/§A.33 added-lines scan.** The diff's added lines in `papers/*.md` and `book/*.md` were scanned for
meta-commentary, reader instructions, rhetorical parallelism, self-assessment, label-restating, revision-history phrases
and mid-sentence capitals outside the acronym whitelist (math stripped). There were 11 hits on added lines and 13 on
removed lines. Every added-line hit is text the edit left in place on a changed line, with the same hit on the removed
side: "striking" (ch08:177 and its mirror, SM:1572), "now" (SM, Methodology, Structure), and capitals "MOND", "FAILS"
and "DESI". The scan found no new hit.

## Re-grep for residue (`papers/*.md`, `book/*.md`)

| Pattern | Survivors |
|---|---|
| "0.02 %" | GR:534 only (CMB peak amplitudes vs ΛCDM; not θ₀) |
| "0.2227", "0.222220", "1776.86", "0.666661", "105.652", "0.51096", "0.66666 " | none |
| "$8 \times 10^{-5}$" (old dressing bound) | none; the only match, ch06:157 [F1683], is the Jarlskog value $3.18 \times 10^{-5}$ |
| "105.74" | ch06:190 [F1716] only: the O6-A (i) row, kept on purpose with its new label |
| "ten gravitational" | none |
| "seven (independent) relations", "dual form" | none |
| "derives Planck", "deriving $\hbar$", "derivation of $\hbar$/Planck" | book/README:98 only (not mirrored): appendix-b's contents list, "gap equation deriving $\hbar = c^3 \epsilon^2/(4G\sigma)$". It names the relation, not a value, and was not in the audit's site list, so it is left as it is |
| "value of $\hbar$" | Substratum:178 and appendix-b:173 [F5940] and glossary:73 [F6673] ("not the value", new text); invariance uses "the same value of $\hbar$" at ch02:134, ch03:80, ch07:22, ch07:124 (CONTEXT-OK per the audit); Substratum:188 (Lemma 23.0, see the open item) |
| "value of ℏ" | Explainer:298 and :507 (CONTEXT-OK per the audit) |
| "These are theorems" | SM:1378 now reads "These are theorems on the branch stated in §1 (Tier 2) …" (H38); appendix-c:222 is unrelated |
| "Status:** Theorem" | Substratum:140 and :172 (Stages 1–2, scoped); Stage 3 (:184) now reads "Conditional on H-slope …" |
| "sharpest" | θ₀ carries none. Koide $Q$ keeps it with the metric named at ch06:12, appendix-a:98 and :215; other hits concern JUNO, Cabibbo λ or are unrelated |

**Counts.** Category A: "These eight relations" (ch06:320) and "eight Category A rows, one for each relation"
(ch06:332), with FULL mirrors; no other site quotes the count. Twenty-four table entries and five empirical channels
are unchanged.

