# BH-01 manuscript audit: sentences depending on accessible recovery

Status: audit notes with wording proposals for later review. This file is not a
manuscript edit and authorizes none. Line numbers are at base commit `809fac52`
(`book/ch07-gravity.md` blob `2876061f`, `papers/GR.md` blob `90268f3b`). Each `ch07`
paragraph below is mirrored verbatim in `book/The-Incompleteness-of-Observation-FULL.md`
(blob `cb1cee2d`) at the line given in brackets; any adopted change lands in both (§A.14).

Key to the assessment column, relative to `REPORT.md` in this directory:

- **supports**: the sentence states what the toy result establishes (global conservation);
- **conditions**: the sentence holds only under endpoint conditions R1-R4 of `REPORT.md`
  (no remnant or bounded remnant, `D` decoupled or read, joint radiation records, `V`
  fully in the access class), which the sentence does not state;
- **contradicts**: the inference drawn in the sentence is refuted in the tested finite
  class.

The result is a finite toy access model; none of the assessments is a claim about black-hole
physics. Each assessment is about the inference the sentence draws from bijectivity.

## Chapter overview

**ch07 L12 [FULL L1887].** "Section 7.6 resolves the black hole information paradox:
information is never lost from the substratum bijection $\varphi$ (bijectivity); the Page
curve is derived from cycle typicality ..."

- Conservation clause: **supports** (C1 premise; a bijection loses no global information).
- "resolves the black hole information paradox": **contradicts** as an inference from
  bijectivity. Claim A: bijective dynamics with zero accessible advantage exist whenever
  some register is inaccessible at the endpoint. The paradox as §7.6 states it (L112) is
  about what the radiation carries.
- Proposal: "Section 7.6 shows that the substratum bijection $\varphi$ conserves
  information, and states the conditions under which the radiation records carry it: no
  remnant, the trans-cosmological sector decoupled, and joint access to the full radiation
  record."
- The Page-curve clause is outside BH-01 (BH-02 and the Page lane).

## Section 7.6, opening paragraph

**ch07 L110 [FULL L1985], sentence 2.** "The framework resolves the paradox at the
structural level: information is never lost from the substratum bijection $\varphi$ because
$\varphi$ is bijective."

- **contradicts** (resolution inferred from bijectivity alone; claim A); the
  conservation clause **supports**.
- Proposal: "Information is never lost from the substratum bijection $\varphi$, because
  $\varphi$ is bijective; whether it is recoverable from the radiation depends on the
  observer's access at the end of evaporation."

**ch07 L110 [FULL L1985], sentence 3.** "The apparent information loss is an artifact of
the trace-out ..."

- **conditions**. Relative to the global state the loss is only apparent. Relative to the
  observer's access class it is operational indistinguishability (equal record
  distributions) unless R1-R4 hold.
- Proposal: "The information loss is a property of the observer's access to the
  radiation, not of the substratum dynamics."

**ch07 L112 [FULL L1987].** "... the information appears to be lost when the black hole
completes its evaporation. This is in tension with the unitarity of quantum mechanics ..."

- **conditions**, and consistent with the conventional statement: the tension presupposes
  complete evaporation with no other sector (R1, R2). With a remnant or an inaccessible
  sector, the radiation carrying no information is compatible with bijective dynamics
  (claim A; C2 bounds what a remnant of capacity `|K|` can hide). No change proposed; the
  sentence describes the conventional paradox.

## Section 7.6, "The framework's resolution: nested trace-out"

**ch07 L118 [FULL L1993].** "Information is never lost from $\varphi$ — bijectivity is the
framework's structural commitment to unitarity at the substratum level. The apparent
information loss in Hawking radiation is an artifact of the *observer's* description, not of
the underlying dynamics."

- First sentence: **supports**.
- Second sentence: **conditions**, as for L110 sentence 3.
- The paragraph heading presents the nested trace-out as the resolution; see L124.

**ch07 L124 [FULL L1999].** "The nested trace-out is well-defined; the external observer's
emergent quantum mechanics is self-consistent when multiple causal boundaries coexist."

- **supports** as a consistency statement: [GR Theorem A.1] associativity holds for every
  bijection enumerated (claim E).
- It carries no recovery content: the 2688 bijections with zero accessible advantage satisfy
  it equally. As the mechanism of a resolution (the heading at L118) it **contradicts**.
- Proposal: keep the sentence; retitle the paragraph to describe consistency (e.g. "The
  observer's description: nested trace-out"), and state that nested consistency is
  independent of whether the radiation carries the information.

## Section 7.6, Page time paragraph

**ch07 L139 [FULL L2014].** "... the timescale at which information transfer becomes
evident in the radiation is fixed by the framework's structural commitments to bijectivity
and to the boundary-mode counting from §7.5."

- **contradicts** for the bijectivity part. In the tested families the step at which the
  message becomes accessible ranges over every emission step for bijective dynamics: swap
  cascades message-first or message-last, the `GL(4,2)` profiles, and the CNOT cascade at
  the final step only.
- In the linear class the emergence threshold is set by the entropy of the observer's prior
  over the interior (Lemma L, `r_t >= t - (n - k)`), not by bijectivity.
- The Page time concerns the entanglement-entropy turnover, which is BH-02 and Page-lane
  material.
- Proposal: "the Page time follows from the boundary-mode counting of §7.5 under H-scramble
  and the mass-loss law of [GR Appendix A.7]; bijectivity by itself does not fix when
  information becomes accessible in the radiation."

## Section 7.6, generalized second law paragraph

**ch07 L151 [FULL L2026].** "Any process that shrinks the black hole ... must transfer
information to the visible sector matter ... or to the cosmological boundary ... The total
information across the partition is conserved at the substratum level (bijectivity) ..."

- Conservation: **supports**.
- The sentence itself names the cosmological boundary (`D`) as a destination of the
  information. That is the case R2 excludes: information transferred to `D` is outside every
  access class of the external observer (claim C3 countercontrol: one `B`-`D` step gives
  zero advantage with all of `W` read). No change proposed for BH-01; the GSL claim is
  BH-03.

## Section 7.6, empirical status and falsification

**ch07 L153 [FULL L2028].** "... the framework's structural commitment to bijectivity
entails that information is never lost from the substratum, with the apparent information
loss being an artifact of the observer's trace-out."

- **conditions**, as for L118.

**ch07 L155 [FULL L2030], sentence 1.** "Falsification of the framework's resolution would
require evidence that black hole evaporation is genuinely non-unitary at the level of the
underlying dynamics — for instance, an empirical demonstration that the radiation from an
evaporating black hole carries less information than the matter that formed it, in a way
that cannot be reproduced by the framework's nested trace-out."

- **contradicts**. Radiation carrying less information than the infalling matter is
  reproduced by bijective dynamics in the tested class (claim A). So the example does not
  separate unitary from non-unitary dynamics.
- No outcome of that kind is excluded by "the framework's nested trace-out" without R1-R4.
  As stated, the falsifier can absorb any outcome (§A.29).
- Proposal, derived from C1: "Given complete evaporation with no remnant and the
  trans-cosmological sector decoupled, bijectivity requires the joint radiation record to
  determine the initial state; a radiation record carrying less information than the
  infalling matter under those conditions would contradict it."

**ch07 L155, sentence 2.** "No such evidence currently exists, and the convergence with the
QES + islands programs provides additional theoretical support ..."

- Outside BH-01 (Page lane, BH-06).

## Dependencies in the gravity companion (listed for review; outside the requested scope)

- **GR L817** (Appendix A.7 setup): "The trans-cosmological sector $D$ is frozen on
  evaporation timescales ($\tau_{\text{evap}} \ll \tau_B^D$) ..."
  - **contradicts** (item F of `REPORT.md`): with A.5's `tau_B^D ~ 1/H ~ 10^17` s, the
    ratio `t_evap / tau_B^D` is at least `1.70 x 10^57` at the A.5 example mass
    `30 M_sun`. The inequality reverses above `5 x 10^12` kg for every parameter choice in
    the stated intervals.
  - Theorem A.7 (L819) is stated for `t << tau_B^D`, while A.9 and the recovery question
    run to `t_evap`.
  - This is the premise R2 needs. A wording proposal belongs to the Page lane, which owns
    A.7.
- **GR L761** (Theorem A.5 hypothesis): coupling chain `V <-> B <-> D`, no direct `V`-`D`
  coupling. A.1 places `V` between the black-hole horizon and the cosmological horizon, so
  spatial locality would suggest `B <-> V <-> D` instead.
  - Question for the reviewer, not a finding of this audit: which chain is intended?
  - It decides whether information reaches `D` through the interior or through the
    radiation region. Either way R2 is needed.
- **GR L811** (A.6(iii)): "transfers information from $B$ to $V \cup D$". This is
  consistent with R2 being a substantive condition.

## Mirrors outside §7.6 that repeat the same inference (for §A.25 propagation if a proposal is adopted)

- `book/ch18-beyond.md` L146 [FULL L4958]: "Information is never lost from the substratum
  bijection $\varphi$ because $\varphi$ is bijective. The apparent information loss in
  Hawking radiation is an artifact of the trace-out ..."
- `book/ch19-open-problems.md` L72 [FULL L5240]: "Resolved at the level of information
  preservation; ... The substratum bijection $\varphi$ is bijective; information is never
  lost."
  - This is the most accurate of the sites. "Resolved at the level of information
    preservation" is supported, provided preservation is not read as recoverability from the
    radiation.
- `book/ch09-universality.md` L127: table row "BH information preserved"; **supports** as
  worded.
