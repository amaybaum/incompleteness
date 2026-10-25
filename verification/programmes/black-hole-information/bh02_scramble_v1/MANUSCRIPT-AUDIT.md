# Manuscript audit for BH-02 / BH-04 (wording proposals only)

The proposals below concern the text at `809fac52`. `book/ch07-gravity.md` §7.6 and
`papers/GR.md` Appendix A were since corrected on `main` (merge `c37700ad`), so line numbers and
wording must be re-checked against `main` before any proposal is used.

Not a manuscript edit. Line numbers are at `809fac52`. Every book chapter line cited has an
identical mirror line in `book/The-Incompleteness-of-Observation-FULL.md`, given as `FULL:n`;
§A.14 and §A.25 require any adopted change to land in both and in every restatement listed under
"Propagation" below. Evidence labels C1–C7 refer to `REPORT.md` / `result.json` in this
directory. Assessments: **supports**, **conditions** (true only under a hypothesis the sentence
does not state), **contradicts** (a computed or proved result here is inconsistent with the
sentence as written). Where a contradiction holds only in a stated setting, the setting is named:
"definite configuration, aligned split" means a definite initial configuration with the B/R
factorization along configuration coordinates (the setting of GR Theorems A.7–A.8). Outside it,
a permutation acting on a superposition can produce Page-like states (C3), so the same sentence
is conditional on a superposed initial state with configuration-basis entropy `H(p_0)` at least the
target entropy (C2), which A.7's "definite initial state" excludes, and on H-scramble. Proposals
for `papers/` are written in the neutral register of §A.32–§A.33. Revised after independent
review (post-review changes listed in `PROVENANCE.json`).

**Literature values.** Page 2013 (JCAP 09 (2013) 028, arXiv:1301.4995v3) was read in full. For a
large Schwarzschild hole emitting photons and gravitons into empty space at constant mass-loss
coefficient α ≈ 0.000037474, β ≈ 1.4847 is computed there (Eq. (2), p.6) from Page's 1976 photon
and graviton emission rates (reproduced in Page 2005, Eqs. (19)–(21)); Page 1976 itself was not
read. The turnover t∗ ≈ 0.53810 t_decay is Eq. (8) (p.11), the 40.25% of the entropy lost is on
p.12, and 1/(1+β) is Page's τ₁₂ at f = 0 (Eq. (14), p.19). Each site cites the equation or page.
Proposals 1, 5, 17 and 20 may be adopted as far as these sources support them: the figures hold
for that species content, constant α and emission into empty space.

## book/ch07-gravity.md

**1. Chapter overview, line 12 (FULL:1887).**
> "the Page curve is derived from cycle typicality with structural Page time $t_P \approx 0.646\, t_{\text{evap}}$ independent of mass and greybody factors, matching the quantum-extremal-surface and entanglement-island programs through a substantially different mechanism."

- "derived from cycle typicality": **contradicts (definite configuration, aligned split)**; otherwise
  **conditions**. Acting on a definite configuration, every bijection visits only product basis
  states (C1); on a superposition it cannot exceed the superposition's configuration-basis entropy
  (C2). The Page value follows from the Haar ensemble posited by H-scramble, not from the cycle
  structure (C6(b)), and §7.6 itself states that H-scramble is not established.
- "independent of mass and greybody factors": **conditions** (C7). Exact for a constant
  mass-loss coefficient, turnover at half the initial black-hole entropy (radiation entropy equal
  to black-hole entropy lost) and `S ∝ M²`; a constant greybody factor cancels; an M-dependent
  effective coefficient or coarse-grained radiation-entropy accounting changes the fraction
  (0.5381 at constant α with Page's photon-and-graviton β ≈ 1.4847 [Page 2013, Eqs. (2), (8)]).
- "matching the quantum-extremal-surface and entanglement-island programs": **not supported** by
  any result here; the Page time a QES computation yields depends on its radiation-entropy
  accounting (C7(e)), and no matched comparison exists.
- Proposal: "Section 7.6 shows that information is never lost from the substratum bijection
  $\varphi$ (bijectivity), and that the Page curve follows if the substratum orbit satisfies the
  scrambling condition H-scramble, which is not established and which permutation dynamics acting
  on configuration states cannot satisfy; with the radiation's entropy taken equal to the
  black-hole entropy lost and a constant mass-loss coefficient, the turnover falls at
  $t_P = (1 - 2^{-3/2})\,t_{\text{evap}} \approx 0.646\,t_{\text{evap}}$."

**2. Line 116 (FULL:1991).**
> "The framework provides an alternative derivation through a substantially different mechanism, conditional on the scrambling condition H-scramble of [GR Appendix A] — and, under that condition, the two derivations converge on the same quantitative predictions."

- **Conditions.** The H-scramble dependence is stated. "Converge on the same quantitative
  predictions" additionally needs the same radiation-entropy accounting on both sides (C7(e)).
- Proposal: "… conditional on the scrambling condition H-scramble of [GR Appendix A]; under that
  condition, and with the radiation's entropy taken equal to the black-hole entropy lost, it
  reproduces Page's curve and turnover."

**3. Line 126 (FULL:2001).**
> "The framework's derivation of the Page curve runs through the *combinatorial* structure of the bijection $\varphi$ rather than through the gravitational path integral."
> "for a bipartite quantum system in a generic pure state, the marginal entropy of the smaller subsystem is approximately maximal, with corrections that vanish exponentially in the dimension of the larger subsystem."
> "a finite bijection can count its energy-shell cycles uniformly while visiting only product states ([GR Appendix A]); the condition is named, not established."

- First sentence: **contradicts (definite configuration, aligned split)**; otherwise **conditions**
  (C1, C2, C3, C6(b)): in Theorem A.8 the combinatorial structure supplies averaging bookkeeping,
  and the entropy value comes from H-scramble; a permutation produces Page-like entanglement only
  from a supplied superposition.
- Second sentence: **contradicts** (C5). Page's exact Haar mean deficit from `ln m` is about
  `m/(2k)`, which at equal dimensions tends to 1/2 nat, not to zero (exact: −0.4994 at m = k = 32);
  what is exponentially small is the probability of a large deviation (concentration), not the
  mean correction.
- Third sentence: **supports, understated.** "can … visit only product states" holds for every
  bijection acting on a configuration, not only for some (C1).
- Proposal: "The Popescu-Short-Winter result concerns Haar-random pure states: the marginal
  entropy of the smaller subsystem concentrates near Page's value, about $\ln d_{\min} - d_{\min}/(2 d_{\max})$,
  with deviations exponentially unlikely. Applying it to the substratum requires H-scramble: a
  finite bijection acting on a definite configuration visits only product configuration states,
  whatever its cycle structure, and acting on a superposition it cannot create more entanglement
  than the superposition's configuration-basis entropy; the condition therefore needs an input
  beyond the bijection, and it is named, not established."

**4. Lines 130–132 (FULL:2005–2007).**
> "For the typical state on the energy shell — typical in the sense of Popescu-Short-Winter measure concentration applied to the bijection's cycle structure, which is what H-scramble supplies — the radiation's entanglement entropy is approximately $S_{\text{rad}}(t) = \min(n_R(t), n_B(t)) \cdot \ln q,$ … and the corrections are exponentially small."

- **Conditions** (C6(c)): Haar typicality on a proper energy-shell subspace gives the shell's own
  typical value, which differs from `min(n_R, n_B) ln q`. For the Hamming-weight shells tested it
  lies below (certified in three cases off half filling, with a leading-order gap there); for the
  diagonal shell `span{|i⟩|i⟩}` it is exactly `H_m − 1`, above `S_Page(m,m)`. The formula needs the
  shell to be the full product space, or the dimensions replaced by the shell's own typical value.
- "corrections are exponentially small": **contradicts** at and near the turnover (C5; GR A.9
  itself gives −1/2 at `n_R = n_B`).
- Proposal: "… is approximately $\min(n_R(t), n_B(t)) \cdot \ln q$ when the shell is the full
  product of the two mode spaces, with a correction of order $q^{-|n_B - n_R|}$ that reaches about
  half a nat at the turnover."

**5. Lines 137–139 (FULL:2012–2014).**
> "The turnover — the Page time $t_P$ — occurs at $n_R(t_P) = n_B(t_P) = n_B(0)/2$, when half the initial boundary modes have been radiated."
> "independent of the black hole's mass and the species-dependent greybody factor. The Page time's structural status — its independence from solution-specific parameters — is the framework's distinctive content: the timescale at which information transfer becomes evident in the radiation is fixed by the framework's structural commitments to bijectivity and to the boundary-mode counting from §7.5."

- Turnover at `n_B(0)/2`: **conditions** — it is the identification `n_R(t) = n_B(0) − n_B(t)`,
  i.e. radiation entropy equal to black-hole entropy lost (β = 1, C7(e)).
- Independence: **conditions** (C7(c)–(e)), as in item 1.
- "distinctive content … fixed by … bijectivity and … boundary-mode counting": partly
  **supports**, partly **contradicts** (C7). The boundary-mode counting does supply `S ∝ M²` and,
  through `n_R(t) = n_B(0) − n_B(t)`, the β = 1 turnover. Bijectivity does not enter the fraction,
  and no OI coefficient (σ, q, ε, the 1/4) does; the fraction is the same number in any model with
  these inputs, so "distinctive content" is not supported.
- Proposal: "… $t_P = (1 - 2^{-3/2})\,t_{\text{evap}} \approx 0.646\,t_{\text{evap}}$, for a
  constant mass-loss coefficient and with the radiation's entropy equal to the black-hole entropy
  lost; a constant greybody factor cancels from the fraction, and mass-dependent emission (new
  species becoming light) would move it; for emission into empty space the radiation's
  coarse-grained entropy also exceeds the black-hole entropy lost [Page 2005, Eqs. (5)–(10)], and
  Page's accounting for photon and graviton emission from a large Schwarzschild hole, at constant
  mass-loss coefficient, gives $0.538\,t_{\text{evap}}$ [Page 2013, Eq. (8)]." Delete the
  "distinctive content" sentence.

**6. Line 141 (FULL:2016).**
> "The framework's Page curve derivation quantitatively matches the prediction from the quantum extremal surface formula and the entanglement-island construction developed by Penington, Almheiri-Engelhardt, and others."

- **Not supported** here (C7(e); no matched setup). Proposal: "Under H-scramble the framework's
  curve has the same shape as the curve obtained from the quantum-extremal-surface formula and the
  entanglement-island construction …; whether the turnover times agree depends on the
  radiation-entropy accounting each uses, and no matched comparison has been made."

**7. Line 143 (FULL:2018).**
> "The framework arrives at the same Page time, and approximately at the same Page entropy … through a structurally cleaner mechanism. The cycle-typicality argument invokes the Popescu-Short-Winter theorem applied to the deterministic substratum dynamics on the energy shell, under the scrambling condition H-scramble …"

- "same Page time": **not supported** (as item 6). "structurally cleaner mechanism": **not
  supported** — the typicality is imported through H-scramble (C6(b)).
- Proposal: drop "the same Page time" and "structurally cleaner"; keep the H-scramble clause and
  the no-replica statement.

**8. Line 145 (FULL:2020).**
> "What the framework's derivation establishes is that, under H-scramble, the Page curve's quantitative content is reproducible from a finite deterministic substratum without invoking the replica machinery; the scrambling condition itself is the open step."

- **Conditions.** Under H-scramble the quantitative content comes from the Haar ensemble
  H-scramble posits (C6(b)); with a definite configuration and the configuration factorization,
  H-scramble cannot hold for any bijection (C6(a)).
- Proposal: "… is that, if the substratum orbit satisfies H-scramble, Page's curve follows without
  the replica machinery. H-scramble cannot hold for a bijection acting on a definite configuration
  in the configuration factorization, so it requires a superposed initial state or a factorization
  of the emergent description not aligned with configurations; that step is open."

**9. Line 147 (FULL:2022).**
> "The framework's content here is that the typicality-providing ingredient need not be gravitational at all; it can be combinatorial, on the substratum side of the trace-out. This constitutes a microscopic realization of the entanglement-island construction."

- "can be combinatorial": **contradicts (definite configuration, aligned split)**; otherwise **not
  supported** (C1, C2, C3, C6(b)). In Theorem A.8 the typicality-providing ingredient is a
  quantum-ensemble hypothesis (H-scramble); a permutation reaches Page-like values only from a
  supplied superposition. "Microscopic realization" is **not supported**: it requires the explicit
  map of observables and replicas that BH-06 asks for, and none exists.
- Proposal: replace both sentences with "In the framework's argument the ingredient is H-scramble,
  a quantum-typicality condition on the substratum orbit that permutation dynamics on
  configuration states does not satisfy; the correspondence with island saddles is conjectural."

**10. Line 155 (FULL:2030).**
> "the convergence with the QES + islands programs provides additional theoretical support for the unitarity resolution … with the structural Page time prediction $t_P \approx 0.646\, t_{\text{evap}}$ providing a sharp quantitative target"

- **Conditions / not supported**, as items 5–6: the number is conditional on the accounting and
  not OI-specific. Proposal: drop "convergence … provides additional theoretical support" and
  "sharp quantitative target", or restate the 0.646 with its two hypotheses.

**11. Line 282 (FULL:2157).** "and the Page curve requires H-scramble" — **supports.**

**20. Line 114 (FULL:1989), added after review.**
> "The Page time occurs at approximately half the black hole's entropy has been radiated; the curve's turnover is the empirical signature of unitarity."

- **Conditions** (C7(e)). Half the entropy holds when the radiation's entropy equals the black-hole
  entropy lost (β = 1). With the definition given in the same sentence (radiation entropy equal to
  the remaining black hole's entropy) and Page's coarse-grained accounting for photon and graviton
  emission, the turnover comes when about 40.25% has been lost [Page 2013, p.12; 1/(1+β) is
  τ₁₂ at f = 0, Eq. (14), p.19].
- Proposal: "The Page time occurs when the black hole has lost a fraction $1/(1+\beta)$ of its
  initial entropy, where $\beta$ is the entropy carried off by the radiation per unit of
  black-hole entropy lost: one half for $\beta = 1$, about 40% for photon and graviton emission
  from a large Schwarzschild hole." [Page 2013, Eq. (14) p.19 and p.12]

## papers/GR.md (Appendix A and its summary)

**12. Line 611 (summary (iii)).**
> "$S_{\text{rad}}(t) = \min(n_R(t), n_B(t)) \cdot \ln q$ plus exponentially small corrections … the turnover occurs at the Page time $t_P \approx 0.646 \, t_{\text{evap}}$ (structural, independent of mass and greybody factors), and the Page value is recovered for all but an exponentially negligible fraction … conditional on the scrambling condition H-scramble of Appendix A, which is not established there"

- "exponentially small corrections": **contradicts** (C5; A.9's own −1/2). "independent of mass
  and greybody factors": **conditions** (C7). The H-scramble conditionality is stated; C6(a) adds
  that in the configuration factorization H-scramble fails for every bijection.
- Proposal: "… $\min(n_R(t), n_B(t)) \cdot \ln q$ up to a correction of order
  $q^{-|n_B(t)-n_R(t)|}$ (one half nat at $n_R = n_B$) … the turnover occurs at
  $t_P = (1-2^{-3/2})\,t_{\text{evap}}$ for a constant mass-loss coefficient and radiation entropy
  equal to the black-hole entropy lost (a constant greybody factor cancels) …"

**13. Lines 823–827 (Theorem A.8 statement; the dimensions are defined at line 827).**
> "For the dynamics $\varphi$ on the energy shell $\Sigma_E \subset \mathcal{H}_B \otimes \mathcal{H}_R$, the time-averaged entanglement entropy of the radiation equals the Page value … where $d_B = |\mathcal{C}_B(t)|$, $d_R = |\mathcal{C}_R(t)|$"

- **Conditions** (C6(c)). Haar on a proper shell gives a mean that differs from `S_Page(d_B, d_R)`
  with these full dimensions, in a shell-dependent direction: below for the Hamming-weight shells
  tested (certified in three cases), above for the diagonal shell `span{|i⟩|i⟩}` (exactly
  `H_m − 1`; 1/2 against 1/3 at m = 2, 13/12 against 0.9224 at m = 4). The statement needs `Σ_E`
  equal to the full product `C_B × C_R`, or the shell's own Haar mean in place of `S_Page`.
- Proposal: add the hypothesis "(the shell is the full product $\mathcal{C}_B \times \mathcal{C}_R$;
  for a proper shell the Page value is replaced by the Haar-on-shell mean)".

**14. Line 837.**
> "let $\varphi$ be one long cycle permuting it … every visited state is a product state with $S(\rho_R)=0$, while the Page value is $\ln d_{\min}-d_{\min}/(2d_{\max})>0$ for $d_B,d_R>1$ — a gap of $0.886$ nats already at $d_B=d_R=4$."

- **Supports, understated.** It holds for every bijection, not only one long cycle (C1). The figure
  0.886 is the large-dimension form displayed in Theorem A.8 (line 829); the exact Haar mean at 4×4
  is 664789/720720 ≈ 0.922 nats (C5).
- Proposal: "… for every bijection $\varphi$ of the shell, and in particular for one long cycle, …
  a gap of $0.886$ nats in the large-dimension form of the Page value ($0.922$ nats for Page's
  exact mean) at $d_B = d_R = 4$." Alternatively, display Page's exact mean
  $\sum_{k=d_{\max}+1}^{d_{\min} d_{\max}} 1/k - (d_{\min}-1)/(2 d_{\max})$ at line 829 and quote 0.922.

**15. Line 839 (definition of H-scramble).**
> "What the argument needs is a separate condition, **H-scramble**: the orbit ensemble equidistributes over quantum pure states on the shell, in the sense of an approximate unitary design or comparable scrambling property."

- **Supports** as the needed condition. Proposal: append "For a definite initial configuration
  and the configuration factorization of $\mathcal{H}_B \otimes \mathcal{H}_R$, no bijection
  satisfies it; it requires a superposed initial state, whose configuration-basis entropy then
  bounds the entanglement any bijection can produce, or a factorization not aligned with
  configurations."

**16. Lines 847–853 (Theorem A.9).** **Conditions** (C6(d)): A.8 bounds a cycle time-average at a
fixed bipartition; A.9 uses it pointwise in `t` along one trajectory with a moving bipartition
from a definite initial state. Proposal: state the needed pointwise (trajectory) typicality as
part of the hypothesis, or restate A.9 for time averages.

**17. Lines 855–861 (evaporation trajectory).**
> "$dM/dt = -\alpha/M^2$ where $\alpha = \hbar c^4 \Gamma / (15360 \pi G^2)$ and $\Gamma$ is the species-dependent greybody factor (solution-specific)" … "The Page time $t_P$ satisfies $n_B(t_P) = n_B(0)/2$"

- **Supports** the algebra (C7(a)–(c)); **conditions**: a constant `Γ` cancels, an M-dependent
  `Γ` does not (C7(d)); `n_B(t_P) = n_B(0)/2` is the β = 1 accounting (C7(e)).
- Proposal: add "for constant $\Gamma$, and with the radiation's entropy equal to the black-hole
  entropy lost; Page's coarse-grained accounting for photon and graviton emission gives
  $0.538\,t_{\text{evap}}$ [Page 2013, Eq. (8)]."

**18. Line 863.**
> "this is $S_{\text{rad}}(t_P) \approx S_{\text{BH}}(0) \ln q/(2\sigma)$: approximately half the initial black-hole entropy when $\sigma = \ln q$"

- **Conditions.** For `σ < ln q` this exceeds `S_BH(t_P) = S_BH(0)/2`, so the radiation would be
  more entangled than the remaining hole has Bekenstein-Hawking entropy; this is consistent only if
  the black-hole Hilbert space has more than `e^{S_BH}` states. It is the same shell question as
  item 13 (reviewer probe, not a result here).

**19. Lines 865–869 (Remark, comparison with QES + islands).**
> "The Page-curve derivation above quantitatively matches the prediction obtained via the quantum extremal surface formula …"
> "through a structurally cleaner mechanism: the cycle-typicality argument of Theorem A.8 invokes only Popescu-Short-Winter [29] applied to the deterministic substratum dynamics on the energy shell, with no replica trick, no ergodicity assumption, and no gravitational path integral."
> "which constitutes a microscopic realization of the entanglement-island construction."

- "quantitatively matches", "same Page time": **not supported** (item 6).
- "invokes only Popescu-Short-Winter … no ergodicity assumption": **contradicts** Theorem A.8 as
  stated two paragraphs earlier, which requires H-scramble, an equidistribution hypothesis on the
  orbit over pure states. Ergodicity over configurations does not supply it: one long cycle is
  ergodic on the shell and has S = 0 throughout (C1). No ordering between the two properties is
  claimed here.
- "microscopic realization": **contradicts / not supported** (item 9).
- Proposal: "Under H-scramble, the argument of Theorem A.8 uses Popescu-Short-Winter
  concentration with no replica trick and no gravitational path integral; H-scramble is itself an
  equidistribution hypothesis on the orbit over pure states, which ergodicity over configurations
  does not supply. The correspondence between island saddles
  and the post-turnover regime, and between replica wormholes and substratum cycles, is
  conjectural."

## Propagation (restatements found by corpus grep at `809fac52`)

- `book/ch18-beyond.md:146` (FULL:4958): "reproducing the Page curve at the emergent level" —
  **conditions**: H-scramble is not stated there.
- `book/ch18-beyond.md:148` (FULL:4960): "independent of mass and greybody factors, matches the
  quantum-extremal-surface and entanglement-island predictions" — as items 1, 5, 6.
- `book/ch19-open-problems.md:72` (FULL:5240): "The Page curve follows from cycle typicality …
  independent of mass and greybody factors. The framework's derivation matches the
  quantum-extremal-surface and entanglement-island predictions" — as items 1, 5, 6; its
  H-scramble clause supports.
- `book/ch19-open-problems.md:334` (FULL:5502): "Resolved (Page curve from typicality)" —
  **conditions**.
- `book/glossary.md:113` (FULL:6705): "The framework derives the Page curve from cycle typicality
  with structural Page time … independent of mass and greybody factors" — as items 1, 5.
- `book/ch09-universality.md:127` (FULL:2599), `book/appendix-a-prediction-status.md:116`
  (FULL:5661, G11 "Scrambling condition open", class C): **support**; G11's status cell could
  record that the condition is not satisfiable by permutation dynamics on configuration states.
- `papers/GR.md:12` (abstract) lists the Page curve among G4 implications "conditional on G3 and
  their listed assumptions": **supports**.
