# SUBSTATE-1 ↔ Yang–Mills: continuous links, observations and action selection

**Status:** research-only cross-bridge with PR #1003 (constructive QCD) and issue #1007. No OI-to-Yang–Mills derivation, native intervention, new premise, manuscript correction or Lean theorem is asserted. Independent review pending.

## The common mathematical possibility

The present OI SM/GR branch uses a finite microscopic site alphabet, H-link/H-cust as conditional carrier identifications, and A6 covariance. The normalized \(\alpha=1/3\) real wave operator in SM §4.1 is an **observer-level lift** rather than a microscopic coefficient already derived from \(\varphi\).

SUBSTATE-1 proposes an internal carrier \(K\) with potentially continuous values, a measure-preserving bijection \(T\), prior \(\mu\), and finite measurable records \(\pi\). This creates mathematical room for continuous gauge variables and controlled readouts, but by itself does not source either.

Lattice Yang–Mills uses **link** values \(U_{xy}\in G\), not merely continuous state values *at sites*. Under a local gauge re-description \(U_{xy}\mapsto g_x U_{xy} g_y^{-1}\), a based loop transforms by conjugation and its trace is invariant. A physical OI completion needs an explicit map from the **same native microscopic state** into link holonomies, plus a sourced gauge-field dynamics/measure and measurement interactions.

Three different objects must not be conflated:

- **Gauge redundancy** relates physically equivalent descriptions of the links. It is not automatically an observer-controlled measurement.
- **Observation context** describes a real apparatus interaction with records, back-action, setting selection and failures. Merely selecting a measurable partition of passive data does not source a new coherent gate.
- **Yang–Mills action** weights field configurations dynamically. Haar is the natural invariant reference measure, **not** a derivation of the Wilson Boltzmann weight. Covariance alone does not fix a unique action.

## #1003's exact countercontrol still applies

On one SU(2) plaquette define \(w(U_p)=1-\frac12\operatorname{Re}\operatorname{Tr}(U_p)\). Both \(S_1=\sum_p w(U_p)\) and \(S_2=\sum_p w(U_p)^2\) are gauge-invariant. At holonomies with \(\theta=\pi/3\) and \(\theta=\pi\), the corresponding pairs \((w,w^2)\) are \((1/2,1/4)\) and \((2,4)\): these actions are not proportional. This is the **ambient** lattice example in PR #1003; it does not establish that both satisfy all other OI premises.

Replacing the site's finite alphabet with a continuum does not resolve the ambiguity. It may support continuous gauge-group kinematics, but does not select the Wilson action, continuum QFT, reflection positivity, confinement or a mass gap.

## New exact observation-selection countercontrol: continuous U(1)

Take four independently Haar-distributed U(1) links around one oriented closed square. Their holonomy \(U_p=e^{i\theta}\) is also Haar. Let \(c=\cos\theta\), \(w=1-c\); both \(w\) and \(w^2\) are gauge-invariant.

Keep **the same initial link distribution**, but suppose two *hypothetical* observation/herald contexts use different gauge-invariant conditional acceptance probabilities:

\[
a_W=\frac{13}{14}\left(1-\frac{w}{8}\right),
\qquad
a_{W^2}=1-\frac{w^2}{8}.
\]

They both lie in \([0,1]\) for every holonomy and **both** accept exactly \(13/16\) of all incident attempts. Despite equal success rates, accepted-loop statistics differ:

| Statistic | Unconditioned Haar | Context W | Context W² |
| --- | ---: | ---: | ---: |
| Accepted fraction | — | 13/16 | 13/16 |
| Mean cos(θ) | 0 | 1/14 | 2/13 |
| Mean cos²(θ) | 1/2 | 1/2 | 25/52 |

The two **rejected** populations are not interchangeable, either:
conditional means of cos(θ) are −13/42 and −2/3, respectively,
and conditional means of cos²(θ) are 1/2 and 7/12. Both
rejection rates are 3/16. Combining the accepted and rejected
moments with their actual probabilities recovers the **same** original
Haar values in both contexts. Thus the *whole attempted record*
correctly detects the conditioning effect even when an accepted-only
comparison and herald-rate match would not.

**Proof:** Fourier monomials in four independent Haar phases integrate to zero unless every exponent vanishes. Thus \(E[c]=E[c^3]=0\), \(E[c^2]=1/2\), \(E[c^4]=3/8\). Substituting these into the two acceptance polynomials yields the table. Gauge phases cancel around the closed loop, so both rules are gauge-invariant.

The deterministic script **yangmills_context_probe.py** checks the exact rational Laurent-polynomial arithmetic, gauge-loop vertex balance, positivity range, equal acceptance and rejection rates, selected and rejected moments, and recovery of the original Haar moments from the full attempted record. Its symbolic controls are not a continuum dynamical simulation, a nonabelian SU(3) test, a Wilson Gibbs measure, or a physical OI prediction.

**Negative result:** Even matching herald rates cannot distinguish a genuine gauge action from observation-based reweighting of an unchanged Haar ensemble. Full *attempted and rejected* records, a physically sourced observation mechanism and an unconditioned gauge-invariant observable map are essential. This is an independent U(1) ambient countercontrol alongside #1003's SU(2) action non-uniqueness; it is not a no-go against a properly sourced OI construction.

## Concrete link to the active quantum-reconstruction programme

The maintained OI→QM programme marks **F2** active. The current native observer interface does not source general coherent control. The retained native-Y research contains real nonlinear old-sign/new-pool interactions, but masked data, inaccessible q10 and the negative one-tick whole-V read prevent treating the described terminal decoders as an available selectable pair of complementary measurements. PR #912 is likewise a research record, not an adopted native gate or observer-access rule.

**Native observation sourcing verdict: BLOCKED for this retained interface.** The double-slit protocol's two same-preparation selectable path/eraser measurements have not both been implemented. This is an interface-specific result, not a universal no-go for continuous OI sub-states or other native layouts.

A valid unified candidate must pass these gates **in order**:

1. **Source:** pin a microscopic \(d=3\) bijection, an invariant measure, an actual covariant link carrier and finite permitted observer/setting interface. Keep the normalized observer-level wave operator separate.
2. **Action:** derive an induced gauge-invariant measure or action from that source, with #1003's \(S_1\) versus \(S_2\) countercontrol, not just covariance.
3. **Context:** implement two physical selectable settings from the same source, with all public/raw/failed/heralded records and the same incident preparation; disallow post-hoc private-field decoding.
4. **Operational structure:** demonstrate native composable noncommuting operations and an independent spectator/composition witness; retain classical coherent-wave and Bell/no-signaling controls.
5. **Matching:** only after sourcing passes, preregister a finite Wilson-loop and connected-correlator comparison with a decoupled baseline, normalizations, coupling calibration, errors and scale. No inference of Yang–Mills existence or mass gap from a finite match.

**Disposition:** exact ambient U(1) selection countercontrol PASS, pending independent review. Native Yang–Mills action selection and paired quantum observation settings BLOCKED/PARKED (missing sourcing). Full operational OI–QM and OI–Yang–Mills equivalences OPEN. No manuscript change, merge, freeze or physics claim promotion.
