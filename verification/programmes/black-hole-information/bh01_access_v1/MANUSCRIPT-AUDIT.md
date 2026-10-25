# BH-01 manuscript audit: sentences depending on accessible recovery

Status: audit notes with wording proposals for later review. This file is not a
manuscript edit and authorizes none. Line numbers are at base commit `809fac52`
(`book/ch07-gravity.md` blob `2876061f`, `papers/GR.md` blob `90268f3b`). Each book
paragraph below is mirrored verbatim in `book/The-Incompleteness-of-Observation-FULL.md`
(blob `cb1cee2d`) at the line given in brackets; any adopted change lands in both (§A.14).

Key to the assessment column, relative to `REPORT.md` in this directory:

- **supports**: the sentence states what the toy result establishes (global conservation, or
  nested-trace consistency as an identity);
- **holds under unstated conditions**: the sentence holds under sufficient conditions it
  does not state (R1-R4 of `REPORT.md`: inaccessible endpoint set empty or smaller than the
  message set, `W`-dynamics independent of `D` or `D` read, cumulative joint records, all of
  `V` in the endpoint access). R1-R4 are sufficient guarantees, not necessary conditions:
  recovery also occurs when they fail;
- **not supported by bijectivity alone**: the sentence rests on bijectivity jointly with
  other ingredients (the Page curve, H-scramble, mode counting) that are outside BH-01, and
  the bijectivity part does not carry it;
- **contradicts**: the inference the sentence draws from bijectivity, or from nested-trace
  consistency, is refuted in the tested finite class;
- **unfalsifiable as stated**: no outcome of the kind the sentence names is excluded.

The result is a finite toy access model; none of the assessments is a claim about black-hole
physics. Each assessment concerns the inference the sentence draws.

## Chapter overview

**ch07 L12 [FULL L1887].** "Section 7.6 resolves the black hole information paradox:
information is never lost from the substratum bijection $\varphi$ (bijectivity); the Page
curve is derived from cycle typicality ..."

- Conservation clause: **supports** (C1 premise; a bijection loses no global information).
- "resolves the black hole information paradox": **not supported by bijectivity alone**.
  - Claim A: bijective dynamics with zero accessible advantage exist whenever the
    inaccessible endpoint set has at least `|M|` joint values (for a binary message,
    whenever any register is inaccessible). By C2 they cannot exist when it has fewer.
  - The paradox as §7.6 states it (L112) is about what the radiation carries.
  - The rest of the resolution rests on the Page curve and H-scramble, outside BH-01.
- Proposal: "Section 7.6 shows that the substratum bijection $\varphi$ conserves
  information, and states sufficient conditions under which the radiation records carry
  it: no remnant, the trans-cosmological sector decoupled, and joint access to the full
  visible record."

## Section 7.6, opening paragraph

**ch07 L110 [FULL L1985], sentence 2.** "The framework resolves the paradox at the
structural level: information is never lost from the substratum bijection $\varphi$ because
$\varphi$ is bijective."

- The conservation clause **supports**. The resolution inferred from bijectivity alone
  **contradicts** claim A.
- Proposal: "Information is never lost from the substratum bijection $\varphi$, because
  $\varphi$ is bijective; whether it is recoverable from the radiation depends on the
  observer's access at the end of evaporation."

**ch07 L110 [FULL L1985], sentence 3.** "The apparent information loss is an artifact of
the trace-out ..."

- **holds under unstated conditions**. Relative to the global state the loss is only
  apparent. Relative to the observer's access class, it is operational indistinguishability
  (equal record distributions) in instances outside R1-R4.
- Proposal: "The information loss is a property of the observer's access to the
  radiation, not of the substratum dynamics."

**ch07 L112 [FULL L1987].** "... the information appears to be lost when the black hole
completes its evaporation. This is in tension with the unitarity of quantum mechanics ..."

- Consistent with the conventional statement, which presupposes complete evaporation with
  no other sector. With a remnant or an inaccessible sector, the radiation carrying no
  information is compatible with bijective dynamics (claim A); C2 bounds what a remnant of
  `|K|` values can hide.
- No change proposed; the sentence describes the conventional paradox.

## Section 7.6, "The framework's resolution: nested trace-out"

**ch07 L118 [FULL L1993].** "Information is never lost from $\varphi$ — bijectivity is the
framework's structural commitment to unitarity at the substratum level. The apparent
information loss in Hawking radiation is an artifact of the *observer's* description, not of
the underlying dynamics."

- First sentence: **supports**.
- Second sentence: **holds under unstated conditions**, as for L110 sentence 3.
- The paragraph heading presents the nested trace-out as the resolution; see L124.

**ch07 L124 [FULL L1999].** "The nested trace-out is well-defined; the external observer's
emergent quantum mechanics is self-consistent when multiple causal boundaries coexist."

- **supports** as a consistency statement. [GR Theorem A.1] associativity is a Fubini
  identity for every map (claim E).
- It carries no recovery content: the 2688 bijections with zero accessible advantage satisfy
  it equally. As the mechanism of a resolution (the heading at L118) it **contradicts**.
- Proposal: keep the sentence; retitle the paragraph to describe consistency (e.g. "The
  observer's description: nested trace-out"), and state that nested consistency is
  independent of whether the radiation carries the information.

## Section 7.6, Page time paragraph

**ch07 L139 [FULL L2014].** "... the timescale at which information transfer becomes
evident in the radiation is fixed by the framework's structural commitments to bijectivity
and to the boundary-mode counting from §7.5."

- **not supported by bijectivity alone**. In the tested families, the step at which the
  message becomes accessible ranges over every emission step for bijective dynamics: swap
  cascades message-first or message-last, the `GL(4,2)` profiles, and the CNOT cascade at
  the final step only.
- In the linear class the emergence threshold is set by the entropy of the observer's prior
  over the interior (Lemma L, `r_t >= t - (n - k)`), not by bijectivity.
- The mode-counting and Page-time content is BH-02 and Page-lane material.
- Proposal: "the Page time follows from the boundary-mode counting of §7.5 under H-scramble
  and the mass-loss law of [GR Appendix A.7]; bijectivity by itself does not fix when
  information becomes accessible in the radiation."

## Section 7.6, generalized second law paragraph

**ch07 L151 [FULL L2026].** "Any process that shrinks the black hole ... must transfer
information to the visible sector matter ... or to the cosmological boundary ... The total
information across the partition is conserved at the substratum level (bijectivity) ..."

- Conservation: **supports**.
- The sentence itself names the cosmological boundary (`D`) as a destination of the
  information. That is the case R2 rules out. In the C3 leak countercontrol, one `B`-`D`
  step gives zero advantage with all of `W` read.
- No change proposed for BH-01; the GSL claim is BH-03.

## Section 7.6, empirical status and falsification

**ch07 L153 [FULL L2028].** "... the framework's structural commitment to bijectivity
entails that information is never lost from the substratum, with the apparent information
loss being an artifact of the observer's trace-out."

- **holds under unstated conditions**, as for L118.

**ch07 L155 [FULL L2030], sentence 1.** "Falsification of the framework's resolution would
require evidence that black hole evaporation is genuinely non-unitary at the level of the
underlying dynamics — for instance, an empirical demonstration that the radiation from an
evaporating black hole carries less information than the matter that formed it, in a way
that cannot be reproduced by the framework's nested trace-out."

- **unfalsifiable as stated**. Radiation carrying less information than the infalling
  matter is reproduced by bijective dynamics in the tested class (claim A). So the example
  does not separate unitary from non-unitary dynamics.
- Nested-trace consistency holds for every map (claim E), so "cannot be reproduced by the
  framework's nested trace-out" excludes no outcome (§A.29).
- No replacement falsifier is proposed here. A toy classical sufficiency result (C1) does
  not supply a physical falsifier. Its premises include the decoupling of `D` over the
  evaporation, whose stated support item F removes for every black hole above about
  `5 x 10^12` kg.
- The accurate diagnosis: as written, the section states no empirical falsifier for
  recoverability. Wording for that is left to the Page lane.

**ch07 L155, sentence 2.** "No such evidence currently exists, and the convergence with the
QES + islands programs provides additional theoretical support ..."

- Outside BH-01 (Page lane, BH-06).

## Other book sites drawing the same inference (for §A.25 propagation if a proposal is adopted)

**ch09 L108 [FULL L2580].** "Bijectivity is load-bearing because it preserves information
at the substratum level (resolving the BH information paradox in Chapter 7 §7.6)"

- "preserves information at the substratum level": **supports**.
- The parenthetical **contradicts** claim A, as for ch07 L110 sentence 2. It is the most
  direct bijectivity-to-resolution inference in the corpus.
- Proposal: "(the information-preservation half of Chapter 7 §7.6)", or remove the
  parenthetical.

**ch09 L127 [FULL L2599].** Table row "BH information preserved | Page curve at
$t_P \approx 0.646\, t_{\text{evap}}$, conditional on H-scramble | Ch 7 §7.6".

- **supports** as worded: preservation, not recoverability.

**ch18 L130 [FULL L4942].** "... the black hole information paradox ... receive the *same*
structural resolution in the framework ..."

- **holds under unstated conditions**. It inherits the status of ch18 L146 and ch07 L110.
- Minor.

**ch18 L146 [FULL L4958].** "Information is never lost from the substratum bijection
$\varphi$ because $\varphi$ is bijective. The apparent information loss in Hawking radiation
is an artifact of the trace-out ..."

- As ch07 L110 and L118.

**ch18 L158 [FULL L4970].** "The information paradox treats an emergent process (Hawking
radiation) as if it should preserve substratum information (which it does, through the
nested partition)."

- The parenthetical **contradicts**. It attributes radiation-level preservation to the
  nested partition, whose consistency carries no recovery content (claim E). Radiation-level
  recovery is not implied by bijectivity (claim A).
- Proposal: "(the substratum preserves it; whether the radiation carries it depends on the
  observer's endpoint access)".

**ch19 L72 [FULL L5240].** "Resolved at the level of information preservation; ... The
substratum bijection $\varphi$ is bijective; information is never lost."

- The most accurate of the sites. "Resolved at the level of information preservation"
  **supports**, provided preservation is not read as recoverability from the radiation.

**ch19 L334 [FULL L5502].** Status table row "| BH information paradox | Hawking vs unitarity
| Resolved (Page curve from typicality) | Ch 7 §7.6 |".

- **not supported by bijectivity alone**, and inconsistent with ch19 L72, which states the
  Page curve as conditional on H-scramble.
- Proposal, in the table's own two-word register (§A.30): "Conditional (H-scramble)".

## Dependencies in the gravity companion (listed for review; outside the requested scope)

- **GR L817** (Appendix A.7 setup): "The trans-cosmological sector $D$ is frozen on
  evaporation timescales ($\tau_{\text{evap}} \ll \tau_B^D$) ..."
  - **contradicts** (item F of `REPORT.md`): with A.5's `tau_B^D ~ 1/H ~ 10^17` s, the
    ratio `t_evap / tau_B^D` is at least `1.785 x 10^57` at the A.5 example mass `30 M_sun`.
    The inequality reverses above `4.918 x 10^12` kg for every parameter choice in the stated
    intervals.
  - Item F removes the stated support for applying Theorem A.7, and through it A.9, out to
    `t_P` and `t_evap`.
  - It does not show that information reaches `D`, that Theorem A.7 is false within
    `t << tau_B^D`, or that no other decoupling argument exists.
  - Wording belongs to the Page lane, which owns A.7.
- **GR L819, L821** (Theorem A.7 and its proof): both state an error `O(tau_S/tau_B^D)`
  independent of `t`. A.5(i) (L771) gives an `O(t/tau_B^D)` correction. Assumption-watch note
  in `REPORT.md`.
- **GR L761** (Theorem A.5 hypothesis): coupling chain `V <-> B <-> D`, no direct `V`-`D`
  coupling. A.1 places `V` between the black-hole horizon and the cosmological horizon, so
  spatial locality would suggest `B <-> V <-> D`.
  - Question for review, not a finding of this audit: are two meanings of `B` (boundary
    layer and black-hole interior) conflated?
  - Either chain leaves R2 a substantive condition.
- **GR L811** (A.6(iii)): "transfers information from $B$ to $V \cup D$". This is
  consistent with R2 being a substantive condition.
