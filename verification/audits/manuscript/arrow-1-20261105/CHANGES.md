# ARROW-1 Phase 2 change record

**Status: WIP / UNVERIFIED.** This record awaits independent scientific and minimum-change
review. Nothing here is merged.

- **Base:** `f5c281ae10a913ec68fa41b3b839ad0b164979cd`.
- **Authorization:**
  - #1112 c.6649271094: Option 3, the plan in c.6643840329, the side corrections.
  - #1112 c.6649643759 (amaybaum, 2026-11-05): the Main:744 label phrase, the
    `LEDGER.json` `id`/`label`/`fingerprint`, ch18:190, the ch02:192 and ch04:32
    reclassification, and Main:760(iii) NO CHANGE.
- **Basis:** `RECOVERY.md`, as reviewed in #1113 c.6649600806 and c.6649698455.
- **Commits:**
  - `e133ffbc`: record;
  - `d3e13c99`: Main and LEDGER;
  - `eb74b3e7`: papers;
  - `4081cba0`: book and FULL;
  - `e4ab279a`: regenerated `.tex`/`.pdf`;
  - then this record.

**How to read the table.**
- Each row is one fragment replacement. Its old text is unique in the file at the base, and
  each replacement stays within one paragraph line. Line numbers are therefore the same
  before and after.
- Each book row is applied identically to the FULL mirror. After the edits, the chapter
  paragraph and the FULL paragraph are byte-identical.
- Class labels:
  - *retain*: the derived claim stays, with its hypotheses.
  - *conditional*: the conditions are named.
  - *unresolved*: the assertion is removed and the open status stated.
  - *side-correction*: owner-listed, c.6649271094.
  - *owner-ruled*: c.6649643759.
- RECOVERY references are to sections of `RECOVERY.md`.

## Site-by-site changes

| # | Site (before → after) | Mirror | Class | RECOVERY | Old text | New text |
|---|---|---|---|---|---|---|
| 1 | `papers/Substratum.md`:14 → :14 | — | unresolved | B.8, C.3, E.2 | joined by a third projection that produces the arrow of time. | joined by a third projection that supplies a time-symmetric observer-selection rule and, on the expanding cosmological branch, a non-decreasing horizon-area parameter. |
| 2 | `papers/Substratum.md`:26 → :26 | — | unresolved | B.7, B.8 | The same construction produces a third projection (§5.4) that resolves the arrow-of-time question by descending the observer's emergent arrows — cosmological, thermodynamic, memory, measurement — from the horizon-growth clock and the C1–C4 observer-selection theorem of [Main, §4.6], answering the Ellis objection to bijective substrates without adding a structural commitment. | The same construction gives a third projection (§5.4): the C1–C4 observer-selection theorem of [Main, §4.6], which is time-symmetric and selects where observers can exist, together with a horizon-area parameter that is non-decreasing on the expanding cosmological branch; a common mechanism aligning the cosmological, thermodynamic, memory and measurement arrows is not established. |
| 3 | `papers/Substratum.md`:56 → :56 | — | conditional | B.3, B.9, C.3 | Entropy increase is then emergent as a coarse-grained description of the non-equilibrium dynamics observers necessarily see. | The rule is time-symmetric: the direction in which coarse-grained entropy increases is fixed by a low-entropy or product boundary condition, not by the rule (§5.4). |
| 4 | `papers/Substratum.md`:367 → :367 | — | conditional | B.8 | This section makes the synthesis claim explicit: quantum mechanics, general relativity, and the arrow of time are not three independent theories but three projections of the same finite deterministic construction. | This section makes the synthesis claim explicit: quantum mechanics and general relativity are not two independent theories but projections of the same finite deterministic construction, and a third projection bears on the arrow of time (§5.4). |
| 5 | `papers/Substratum.md`:371 → :371 | — | conditional | B.1, B.8, B.9 | and an arrow-of-time projection (§5.4) that produces the emergent cosmological, thermodynamic, memory, and measurement arrows from a single structural clock and the C1–C4 observer-selection theorem of [Main, §4.6]. | and an arrow-of-time projection (§5.4) that supplies the time-symmetric C1–C4 observer-selection theorem of [Main, §4.6] and, on the expanding cosmological branch, a non-decreasing horizon-area parameter. |
| 6 | `papers/Substratum.md`:377 → :377 | — | conditional | B.7, B.8 | the arrow-of-time projection (§5.4) works on the horizon-clock parameter along observer worldlines and produces the cascade of emergent arrows. | the arrow-of-time projection (§5.4) works on the horizon-area parameter along observer worldlines together with the observer-selection rule. |
| 7 | `papers/Substratum.md`:379 → :379 | — | conditional | B.1, B.2, E.2, E.4 | and time translation is broken intrinsically by the growth of the horizon, which is the boundary-thermodynamic and arrow projections (§5.4, [GR]). | and time translation is broken by the growth of the apparent horizon on an expanding background with $\rho + p/c^2 > 0$, an input to the boundary-thermodynamic and arrow projections; in exact de Sitter the horizon area is constant (§5.4, [GR]). |
| 8 | `papers/Substratum.md`:401 → :401 | — | conditional | B.8, B.9; §A.33 history voice | After Main §4.6 (structural observer-selection theorem), the arrow of time joins quantum mechanics and general relativity as a third emergent structure that the framework derives from the same underlying $(S, \varphi)$ and the same trace-out machinery. Before §4.6, the arrow of time was treated as external to the derivation chain — a past hypothesis or an anthropic selection, imposed on the framework rather than produced by it. With §4.6 in place, the observer's confinement | Main §4.6 (structural observer-selection theorem) supplies the selection content of the third projection, applied to the same underlying $(S, \varphi)$ with the same trace-out machinery. The observer's confinement |
| 9 | `papers/Substratum.md`:401 → :401 | — | unresolved | B.7, C.3 | in the coarse-grained description generated by iterating the one-step effective channel, and every arrow the observer sees descends from this confinement together with the horizon growth that the accelerating phase produces. The third projection | in the coarse-grained description generated by iterating the one-step effective channel. The confinement is time-symmetric and fixes where observers can exist, not a direction of time; that the arrows the observer sees descend from it together with horizon growth is not established. The third projection |
| 10 | `papers/Substratum.md`:403 → :403 | — | unresolved | B.8 | What is a projection, and what this section derives, is the *arrow* — the directedness of time within that domain. The framework derives the arrow; it posits the existence of the domain. Conflating the two would overstate what the projection delivers: §5.4 produces directedness, not the bare existence of succession. | What this section addresses is the *arrow* — the directedness of time within that domain. The framework posits the existence of the domain; for the arrow it establishes the conditional and time-symmetric results stated below, and the direction rests on boundary conditions. Conflating the two would overstate what the projection delivers. |
| 11 | `papers/Substratum.md`:405 → :405 | — | conditional | B.1, B.2, B.7, E.1–E.4 | **Horizon growth as the structural clock.** The framework's primary arrow is the cosmological horizon entropy $S_{\rm dS}(t) = A(t)/(4 l_p^2)$, monotonically increasing along any observer worldline in the $\Lambda$-dominated phase. The monotonicity is a feature of the causal partition rather than of any local frame: every observer in the accelerating phase agrees that $S_{\rm dS}$ increases, just as every observer in a Schwarzschild geometry agrees on the exterior direction. The horizon clock is observer-independent, continuous, and monotonic for as long as $\ddot a > 0$, which the framework identifies as the regime of interest for the derivations of [GR]. At the substrate level, $(S, \varphi)$ has no preferred direction: $\varphi$ and $\varphi^{-1}$ are equally valid as forward-time maps. At the observer level, the horizon clock picks out a direction, and all other arrows align with it. | **Horizon growth as the structural clock.** The framework's primary clock is the area $A(t) = 4\pi c^2/H^2$ of the apparent (Hubble) horizon, with the horizon entropy $S_{\rm dS}(t) = A(t)/(4 l_p^2)$ assigned to it at the de Sitter calibration ([GR, §2.3]). On an expanding flat Friedmann-Robertson-Walker background ($H > 0$) satisfying the null energy condition, $dA/dt = -8\pi c^2\dot H/H^3 \geq 0$: the area is non-decreasing along any comoving observer worldline, strictly increasing while $\rho + p/c^2 > 0$, and constant in exact de Sitter. The criterion is expansion with the null energy condition, not $\ddot a > 0$: the area also grows in the decelerating era, and is constant in exact de Sitter, where $\ddot a > 0$. Both conditions are inputs: the expanding branch is observed, not derived, and reading $A/(4 l_p^2)$ as the entropy of a dynamical horizon goes beyond the de Sitter calibration ([GR, §2.3]). The monotonicity is a feature of the causal partition rather than of any local frame, just as every observer in a Schwarzschild geometry agrees on the exterior direction. At the substrate level, $(S, \varphi)$ has no preferred direction: $\varphi$ and $\varphi^{-1}$ are equally valid as forward-time maps. At the observer level, the horizon parameter orders the expanding branch; that the other arrows align with it is not established. |
| 12 | `papers/Substratum.md`:407 → :407 | — | conditional | B.2–B.7, C.4; side correction (citation) | **The layered cascade.** Four derived arrows align with the horizon clock through a structural cascade. *Cosmological:* $S_{\rm dS}(t)$ monotonic in the $\Lambda$-dominated phase, as above. *Thermodynamic:* via Jacobson's coupling $\rho_s = \rho_{\rm crit}$ ([GR, §3]), the entropy of any horizon-bounded system increases with the observer's clock — the thermodynamic arrow descends from the structural arrow without an independent postulate. *Memory:* C2 (memory persistence) implies the observer's hidden sector preserves correlations forward along the clock rather than backward, because the coarse-grained mixing time of the hidden-sector dynamics is uniform in the two directions but the observer's measurement protocol commits to one. *Measurement:* the observer records "past" outcomes and prepares "future" states — an asymmetry inherited from the memory layer, not added on top of it. The chain grounds in one structural fact (horizon growth) and one structural constraint (C1–C4 observer selection via Main §4.6, conditional on its effective-mixing hypothesis and stated for the coarse-grained description generated by iterating the one-step effective channel). | **The layered cascade.** Four arrows are stated against the horizon parameter, with different status. *Cosmological:* $A(t)$ non-decreasing on the expanding branch, as above; the branch is an input, and no result here selects it. *Thermodynamic:* Jacobson's coupling $\rho_s = \rho_{\rm crit}$ ([GR, §7.2]) is an instantaneous identity, even in $H$, between the boundary energy density and $H^2$; it does not relate matter entropy to horizon area. The direction of coarse-grained entropy increase rests on a low-entropy or product boundary condition: from a product state at $t = 0$, the sum of the sector entropies is bounded below by its value at $t = 0$ at every earlier and later time ([GR, §A.6]), a two-sided bound rather than a monotonicity statement, and the generalized second law is open. *Memory:* C2 (memory persistence) is a retention condition; the coarse-grained mixing time of the hidden-sector dynamics is the same in the two directions, and the direction in which records are written and read is fixed by a non-stationary preparation together with the observer's orientation convention. *Measurement:* the observer records "past" outcomes and prepares "future" states — an asymmetry inherited from the memory layer, not added on top of it. That the thermodynamic, memory and measurement arrows align with the horizon parameter through a common mechanism is not established. The chain uses one input (horizon growth on the expanding branch) and one structural constraint (C1–C4 observer selection via Main §4.6, conditional on its effective-mixing hypothesis and stated for the coarse-grained description generated by iterating the one-step effective channel), which fixes where observers exist, not a direction. |
| 13 | `papers/Substratum.md`:409 → :409 | — | conditional / unresolved | B.1, B.8, C.1 | The framework therefore derives the existence of a monotonic parameter along observer worldlines, not a substrate-level arrow of time. This distinction answers Ellis's objection (a bijective substratum cannot carry an arrow of time) by agreeing with the objection's premise while deriving what the observer actually sees from the structure the substratum does have. | What the framework establishes is therefore a horizon parameter that is non-decreasing along observer worldlines on the expanding branch, given the inputs above, not a substrate-level arrow of time. This agrees with the premise of Ellis's objection (a bijective substratum cannot carry an arrow of time); the observed direction does not follow from the results above without the boundary conditions they name. |
| 14 | `papers/Substratum.md`:411 → :411 | — | side-correction | README side corrections; B.10 | This is not a new axiom — [Main, §1.3] already assumes a causal topology on the partition — but it is load-bearing | This is not a new axiom — it reduces to the ordering of moments together with $\varphi$ (scope note below) — but it is load-bearing |
| 15 | `papers/Substratum.md`:413 → :413 | — | conditional | B.10 | **Scope note: the arrow derivation is conditional on the ordering of moments.** The cascade derives a *direction* along the observer's worldline. It presupposes that the worldline's moments are *ordered* — that they form a sequence — since a monotonic parameter is monotonic with respect to an ordering. | **Scope note: the results of this section are conditional on the ordering of moments and on further inputs.** The cascade concerns a *direction* along the observer's worldline. It presupposes that the worldline's moments are *ordered* — that they form a sequence — since a monotonic parameter is monotonic with respect to an ordering. |
| 16 | `papers/Substratum.md`:413 → :413 | — | conditional | B.10 | The arrow derivation of this section is therefore conditional: it derives the direction *given* an ordering, and inherits the open status of the ordering question. What this section establishes is the conditional — ordered moments yield a derived monotonic parameter and an observer-imposed direction-convention — not an unconditional derivation of temporal directedness from the substratum alone. The causal topology of the worldline reduces to this ordering together with the dynamics $\varphi$ (it introduces no commitment beyond the ordering), so the arrow's single open dependency is the ordering question and nothing further. | The results of this section therefore inherit the open status of the ordering question. What this section establishes is conditional — given ordered moments and the expanding branch, a non-decreasing horizon parameter and an observer-imposed direction-convention — not a derivation of temporal directedness from the substratum alone. The causal topology of the worldline reduces to this ordering together with the dynamics $\varphi$ (it introduces no commitment beyond the ordering). The ordering is not the only dependency: the horizon parameter rests on the expanding branch and the null energy condition; the observer selection on the effective-mixing hypothesis and the iterated-channel description; the thermodynamic, memory and measurement directions on a non-stationary or low-entropy preparation and the orientation convention; and the alignment of the arrows is open. |
| 17 | `papers/Substratum.md`:415 → :415 | — | unresolved | B.8 | **CP violation as the residual Ellis-class objection.** The layered cascade closes the Ellis-axis objection for the arrow of time but does not automatically close the related question of CP violation. | **CP violation and the Ellis-class objection.** The related question of CP violation is separate from the cascade. |
| 18 | `papers/GR.md`:32 → :32 | — | conditional | B.8 | The reconstruction theorem and the synthesis claim that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same $(S, \varphi)$ are developed in [Substratum]. | The reconstruction theorem and the synthesis claim that quantum mechanics and general relativity descend as projections of the same $(S, \varphi)$, with a third projection bearing on the arrow of time, are developed in [Substratum]. |
| 19 | `papers/GR.md`:214 → :214 | — | side-correction | README side corrections | and whether its derived classical thermodynamic arrow — $\beta_E = \partial S_H/\partial E > 0$, settled classically by exact counting (kernel: `counting_passive`) — enters that completion | and whether its classical thermodynamic orientation — the energy ordering under which exact finite-bath counting with $\beta_E = \partial S_H/\partial E > 0$ makes the classical profile passive (kernel: `counting_passive`, from a monotone bath count), an orientation of energy rather than a direction of time — enters that completion |
| 20 | `papers/GR.md`:561 → :561 | — | conditional | B.8 | and the synthesis claim that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same $(S, \varphi)$ are developed in [Substratum]. | and the synthesis claim that quantum mechanics and general relativity descend as projections of the same $(S, \varphi)$, with a third projection bearing on the arrow of time, are developed in [Substratum]. |
| 21 | `papers/GR.md`:607 → :607 | — | side-correction | B.4, C.4 | Unitarity of $\varphi$ and subadditivity make the sum of the von Neumann entropies of $V$, $B$ and $D$ non-decreasing from a product initial state (Theorem A.6). | Unitarity of $\varphi$ and subadditivity bound the sum of the von Neumann entropies of $V$, $B$ and $D$ below by its value at a product initial state, at every earlier and later time (Theorem A.6); the bound is two-sided and does not make the sum monotone. |
| 22 | `papers/GR.md`:709 → :709 | — | conditional | B.8 | The reconstruction theorem and the synthesis claim — that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same deterministic $(S, \varphi)$ — are developed in [Substratum]. Together, this four-paper synthesis ([Main], [SM], [GR], [Substratum]) proposes that the Standard Model, general relativity, and the arrow of time descend from one finite deterministic construction, | The reconstruction theorem and the synthesis claim — that quantum mechanics and general relativity descend as projections of the same deterministic $(S, \varphi)$, with a third projection bearing on the arrow of time — are developed in [Substratum]. Together, this four-paper synthesis ([Main], [SM], [GR], [Substratum]) proposes that the Standard Model and general relativity descend from one finite deterministic construction, |
| 23 | `papers/SM.md`:1366 → :1366 | — | conditional | B.8 | The substratum-level reconstruction theorem and the synthesis claim that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same $(S, \varphi)$ are developed in [Substratum]. | The substratum-level reconstruction theorem and the synthesis claim that quantum mechanics and general relativity descend as projections of the same $(S, \varphi)$, with a third projection bearing on the arrow of time, are developed in [Substratum]. |
| 24 | `papers/SM.md`:1592 → :1592 | — | conditional | B.7, B.8 | and the synthesis claim that quantum mechanics, general relativity, and the arrow of time descend as three projections of the same $(S, \varphi)$ are developed in [Substratum]. Together, this four-paper synthesis ([Main], [SM], [GR], [Substratum]) makes a single claim: the Standard Model, general relativity, and the arrow of time are three projections of one finite deterministic construction — the visible-sector projection developed here, the boundary-level thermodynamic limit developed in [GR], and the horizon-clock-plus-observer-selection projection developed in [Substratum §5.4]. | and the synthesis claim that quantum mechanics and general relativity descend as projections of the same $(S, \varphi)$, with a third projection bearing on the arrow of time, are developed in [Substratum]. Together, this four-paper synthesis ([Main], [SM], [GR], [Substratum]) makes a single claim: the Standard Model and general relativity are projections of one finite deterministic construction — the visible-sector projection developed here and the boundary-level thermodynamic limit developed in [GR] — with the horizon-clock-plus-observer-selection projection developed in [Substratum §5.4], whose alignment of the arrows of time is open. |
| 25 | `papers/Methodology.md`:184 → :184 | — | conditional | B.1, B.2, B.8 | *The arrow* — that the ordering has an experienced direction — is derived in the framework's substratum treatment from horizon growth. | *The arrow* — that the ordering has an experienced direction — is addressed in the framework's substratum treatment: on the expanding cosmological branch, horizon growth supplies a non-decreasing parameter, and the direction rests on boundary conditions and the orientation convention. |
| 26 | `papers/Methodology.md`:184 → :184 | — | unresolved | B.8, B.10 | The arrow is derived, not posited, and rests on the causal topology, hence ultimately on the ordering. | The arrow rests on the causal topology, hence on the ordering, and on those boundary conditions. |
| 27 | `papers/Methodology.md`:184 → :184 | — | unresolved | B.8, B.10 | Causal topology and the arrow are downstream of these two and of structure (the dynamics, horizon growth) the framework has independently. No third temporal axiom is required, and none is concealed: the two-question framing of this section is the complete account of where the framework's temporal commitments lie. | Causal topology and the arrow are downstream of these two and of inputs the framework takes as given (the dynamics, the expanding branch, the boundary conditions that fix the arrow's direction). No third temporal axiom is required: the two-question framing of this section accounts for the framework's temporal axioms, and the arrow's boundary conditions are inputs rather than axioms. |
| 28 | `papers/Methodology.md`:227 → :227 | — | conditional | B.2, B.8 | these are either left open (ordering, §5.1) or derived downstream from structure the framework independently has (causal topology and arrow, §5.2 inventory). | these are either left open (ordering, §5.1), derived downstream from structure the framework independently has (causal topology, §5.2 inventory), or addressed downstream with boundary conditions taken as inputs (arrow, §5.2 inventory). |
| 29 | `papers/Explainer.md`:930 → :930 | — | unresolved | B.9 | Second, the "past hypothesis" of cosmology gets replaced by a conditional theorem. | Second, one role of the "past hypothesis" of cosmology — selecting where observers can exist — gets taken over by a conditional theorem. |
| 30 | `papers/Explainer.md`:930 → :930 | — | unresolved | B.9, C.3 | You don't need to posit low initial entropy to explain why we see it; you need the definition of observation together with the mixing hypothesis for equilibrium regions, which select for the non-equilibrium phase. | For that job you don't need to posit low initial entropy; you need the definition of observation together with the mixing hypothesis for equilibrium regions, which select for the non-equilibrium phase. The selection is time-symmetric: it does not explain why entropy is low at one end of the observed history, which remains a boundary condition. |
| 31 | `papers/Explainer.md`:930 → :930 | — | unresolved | B.9 | The mixing hypothesis is the premise that takes the place of the postulate. | The mixing hypothesis is the premise that takes the place of the postulate in that role. |
| 32 | `papers/Explainer.md`:932 → :932 | — | conditional | B.2 | In our universe, the non-equilibrium phase is provided by the expanding cosmological horizon. | In our universe, the non-equilibrium phase is associated with the expanding cosmological horizon — an expansion that is observed, not derived. |
| 33 | `papers/Explainer.md`:932 → :932 | — | conditional / unresolved | B.3, B.7, C.1 | Entropy increase, the Second Law, and the felt direction of time emerge as coarse-grained descriptions of the dynamics accessible to observers in this non-equilibrium phase. Like quantum mechanics itself, the direction of time is emergent — a consequence of observing a lossless cycle from within, during the phase when such observation is structurally possible. | Entropy increase, the Second Law, and the felt direction of time emerge as coarse-grained descriptions of the dynamics accessible to observers in this non-equilibrium phase, given a low-entropy boundary condition that the selection rule does not supply; whether those arrows and the expansion share a common mechanism is open. Like quantum mechanics itself, the direction of time is emergent — a feature of observing a lossless cycle from within — but which way it points is fixed by boundary conditions, not derived. |
| 34 | `papers/Main.md`:744 → :744 | — | owner-ruled consequence | F.4 (c.6649643759 item 1) | the rate condition $\tau_{\rm mix}\ll\tau_S$ stated in the past-hypothesis corollary | the rate condition $\tau_{\rm mix}\ll\tau_S$ stated in the observer-selection corollary |
| 35 | `papers/Main.md`:758 → :758 | — | unresolved (title) | B.9, F.4 | **Corollary (past-hypothesis replacement, with its rate condition).** | **Corollary (observer-selection rule, with its rate condition).** |
| 36 | `book/ch02-substratum.md`:176 → :176 | FULL:819 → :819 | conditional | B.8 | The next section turns to the synthesis: how quantum mechanics, general relativity, and the arrow of time relate to the substratum as three projections of the same construction. | The next section turns to the synthesis: how quantum mechanics and general relativity relate to the substratum as projections of the same construction, and what a third projection establishes about the arrow of time. |
| 37 | `book/ch02-substratum.md`:184 → :184 | FULL:827 → :827 | conditional | B.8 | The framework's claim is that quantum mechanics, general relativity, and the arrow of time are not three independent theories. Conditional on H-Bell at the Bell/local-lattice interface, they are three projections of the same finite deterministic construction. | The framework's claim is that quantum mechanics and general relativity are not two independent theories. Conditional on H-Bell at the Bell/local-lattice interface, they are projections of the same finite deterministic construction, and a third projection bears on the arrow of time. |
| 38 | `book/ch02-substratum.md`:192 → :192 | FULL:835 → :835 | conditional | B.5, C.3 (ruling item 3: C2 retention) | Observers, however, are not symmetric under this exchange. Condition C2 — persistence, in its slow-bath realization — picks out one direction along the observer's worldline as the direction in which the hidden sector's correlations with the visible sector's past are preserved. | Condition C2 — persistence, in its slow-bath realization — is a retention condition: it requires the hidden sector's correlations with the visible sector's past to persist to readback, and the coarse-grained mixing time it constrains is the same in the two directions; the direction in which records are written and read is fixed by a preparation and the observer's orientation convention. |
| 39 | `book/ch02-substratum.md`:192 → :192 | FULL:835 → :835 | conditional / unresolved | B.1, B.7, B.9, E.2 (ruling item 3) | to the non-equilibrium phase of $(S, \varphi)$; in the $\Lambda$-dominated cosmological phase, this phase is the one in which the horizon entropy $S_{\text{dS}}(t) = A(t)/(4\ell_P^2)$ is monotonically increasing. | to the non-equilibrium phase of $(S, \varphi)$; the restriction is time-symmetric and selects where observers can exist, not a direction. On an expanding cosmological background satisfying the null energy condition — inputs, not derived — the area $A(t)$ of the apparent horizon, and the horizon entropy $S_{\text{dS}}(t) = A(t)/(4\ell_P^2)$ assigned to it, is non-decreasing, strictly increasing while $\rho + p/c^2 > 0$ and constant in exact de Sitter. That the selected non-equilibrium phase is ordered by this growth is not established. |
| 40 | `book/ch02-substratum.md`:194 → :194 | FULL:837 → :837 | conditional / unresolved | B.1–B.7, E.4 | The cosmological horizon entropy provides a structural clock. Every observer in the accelerating phase agrees that $S_{\text{dS}}$ increases — the monotonicity is a feature of the causal partition rather than of any local frame — and other arrows of time align with this structural clock through a cascade. The thermodynamic arrow descends from Jacobson's coupling between boundary entropy and matter entropy. The memory arrow descends from C2 — persistence, realized by the slow bath — which preserves correlations forward along the clock rather than backward. The measurement arrow — the observer records past outcomes and prepares future states — descends from the memory arrow. The chain grounds in one structural fact (horizon growth in the accelerating phase) and one structural constraint (C1–C4 observer selection, conditional on the effective-mixing hypothesis of [Main §4.6] and stated for the coarse-grained description generated by iterating the one-step effective channel). | The horizon area provides a structural clock on that background. Every comoving observer on an expanding background satisfying the null energy condition agrees that it does not decrease — the monotonicity is a feature of the causal partition rather than of any local frame — and the criterion is expansion with the null energy condition, not acceleration: in exact de Sitter the area is constant. Whether the other arrows of time align with this clock is not established. Jacobson's coupling relates the boundary energy density to the expansion rate, not matter entropy to horizon area, so the direction of the thermodynamic arrow rests on a low-entropy or product boundary condition, and the generalized second law is open. C2 — persistence, realized by the slow bath — holds the same way in both directions; the direction of the memory arrow comes from a preparation and the observer's orientation convention. The measurement arrow — the observer records past outcomes and prepares future states — inherits the memory arrow's direction. The chain uses one input (horizon growth on the expanding branch) and one structural constraint (C1–C4 observer selection, conditional on the effective-mixing hypothesis of [Main §4.6] and stated for the coarse-grained description generated by iterating the one-step effective channel), which fixes where observers can exist, not a direction. |
| 41 | `book/ch02-substratum.md`:196 → :196 | FULL:839 → :839 | unresolved | B.7, B.8 | The framework's content here is precise: it derives a monotonic parameter along observer worldlines and four aligned arrows of time. What it does not derive is the convention | The framework's content here is precise: on the expanding branch it establishes a non-decreasing horizon parameter along observer worldlines, and it does not establish that the four arrows of time align. Nor does it derive the convention |
| 42 | `book/ch02-substratum.md`:196 → :196 | FULL:839 → :839 | conditional | B.1, B.2 | The framework derives the existence of a monotonic parameter; the labeling is an observer-imposed convention. | The parameter is conditional on the expanding branch; the labeling is an observer-imposed convention. |
| 43 | `book/ch02-substratum.md`:196 → :196 | FULL:839 → :839 | conditional | B.10 | The derivation here is therefore conditional on that ordering — it establishes that ordered moments yield a directed parameter, not that directedness arises from the substratum with no assumption about ordering at all. | The result here is therefore conditional on that ordering as well — it establishes that ordered moments on the expanding branch yield a non-decreasing parameter, not that directedness arises from the substratum with no assumption about ordering at all. |
| 44 | `book/ch02-substratum.md`:198 → :198 | FULL:841 → :841 | conditional / unresolved | B.7 | The horizon-clock projection works on the horizon-growth parameter along observer worldlines and produces the cascade of emergent arrows. | The horizon-clock projection works on the horizon-growth parameter along observer worldlines together with the observer-selection rule; the alignment of the arrows with that parameter is open. |
| 45 | `book/ch03-structural-realism.md`:58 → :58 | FULL:932 → :932 | unresolved | B.7, B.9 | The framework's account of the arrow of time, developed in Chapter 2 §2.6, follows from this exclusion: observers are restricted to the non-equilibrium phase of the substratum's dynamics, and the structural arrow of horizon growth provides the clock the observer's other arrows align with. | The framework's treatment of the arrow of time, developed in Chapter 2 §2.6, starts from this exclusion: observers are restricted to the non-equilibrium phase of the substratum's dynamics. The exclusion is time-symmetric; on the expanding branch, horizon growth supplies a non-decreasing clock, and whether the observer's other arrows align with it is not established. |
| 46 | `book/ch03-structural-realism.md`:202 → :202 | FULL:1076 → :1076 | conditional | B.8 | quantum mechanics, general relativity, and the arrow of time are projections expressing the substratum's content under different aspects; | quantum mechanics and general relativity are projections expressing the substratum's content under different aspects, with a third bearing on the arrow of time; |
| 47 | `book/ch04-methodology.md`:32 → :32 | FULL:1149 → :1149 | conditional | B.1, B.2 (ruling item 3) | The framework does not commit to a specific cosmological history beyond the structural arrow of horizon growth in the $\Lambda$-dominated phase. | The framework does not commit to a specific cosmological history beyond the expanding branch, taken as given, on which the horizon area does not decrease. |
| 48 | `book/ch18-beyond.md`:190 → :190 | FULL:5003 → :5003 | owner-ruled site | C.1 (c.6649643759 item 2) | Within a single cycle, the observer's experience is unidirectional (the arrow of time discussed in the next section), but at the substratum level the dynamics has no preferred direction. | Within a single cycle no state function increases throughout; a direction of the observer's experience is fixed by boundary conditions on a stretch of the cycle (the arrow of time discussed in the next section), and at the substratum level the dynamics has no preferred direction. |
| 49 | `book/ch18-beyond.md`:202 → :202 | FULL:5015 → :5015 | conditional | C.3, C.5 (A11) | The asymmetry is introduced by the trace-out — the marginalization over the hidden sector that produces the embedded observer's reduced description. The arrow of time is therefore a structural consequence of embedded observation, | The asymmetry enters through the trace-out of a non-equilibrium initial condition — the marginalization over the hidden sector that produces the embedded observer's reduced description; under the invariant measure the trace-out alone produces none. The arrow of time is therefore a feature of embedded observation of such a condition, |
| 50 | `book/ch18-beyond.md`:208 → :208 | FULL:5021 → :5021 | side-correction | README side corrections | Detailed balance asserts that the transition probabilities $T_{ij}$ between any two states satisfy $T_{ij} = T_{ji}$ at all timescales — the rate of transition from $i$ to $j$ equals the rate of transition from $j$ to $i$. This is a *substratum-level* T-symmetry: the dynamics has no preferred direction. | For a time reversal that preserves the partition, and the counting prior on hidden states, the visible transition probabilities satisfy reciprocity, $T_{ij} = T_{\theta j, \theta i}$ at all timescales, with $\theta$ the action of time reversal on visible states; when the visible states carry no T-odd data this is detailed balance, $T_{ij} = T_{ji}$ — the rate of transition from $i$ to $j$ equals the rate of transition from $j$ to $i$. This follows from *substratum-level* T-symmetry: the dynamics has no preferred direction. |
| 51 | `book/ch18-beyond.md`:216 → :216 | FULL:5029 → :5029 | unresolved / side-correction | B.7, C.6(β); README side corrections | The alignment of the thermodynamic and cosmological arrows is structural rather than coincidental. Both arrows trace to the same initial conditions of the cosmological partition. The universe started with low entropy at the cosmological level; the framework's structural conditions C1–C4 hold at the cosmological boundary (Chapter 7 §7.2); the thermodynamic arrow within the visible sector tracks the cosmological arrow because the cosmological boundary is the primary partition for any embedded observer. | Both arrows are traced to the same initial conditions of the cosmological partition. That is a common boundary condition, not a derived mechanism: that the thermodynamic arrow within the visible sector tracks the cosmological arrow is not established. The universe started with low entropy at the cosmological level, as an initial condition; at the cosmological boundary, coupling C1, persistence C2 and capacity C3 are verified, while history readback C4 is a named realization condition not presently discharged (Chapter 7 §7.2); the cosmological boundary is the primary partition for any embedded observer. |

The LEDGER row is not in the table above. In `verification/coverage/LEDGER.json`, the
entry `MAIN:C-past-hypothesis-replacement-rate-condition` is renamed to
`MAIN:C-observer-selection-rule-rate-condition`:
- `label`: `(past-hypothesis replacement, with its rate condition)` becomes
  `(observer-selection rule, with its rate condition)`;
- `fingerprint`: `a2f5c0c423aa9ca2` becomes `df04fba6b2d81e20`, as computed by
  `tools/proof_census.py --json` on the edited Main.
- Unchanged: `kernel: GAP`, `assumptions`, `area`, `line` and every other field.

Authorized by owner ruling c.6649643759, item 1; justified in `RECOVERY.md` §F.4.

## Follow-up edits (owner rulings #1112 c.6650301410)

These answer the Phase 2 reviews at `bd926c76`: the scientific review (#1113 c.6650236439) and
the minimum-change review (#1113 c.6650241392). The owner ruled on both in
[#1112 c.6650301410](https://github.com/amaybaum/incompleteness/issues/1112#issuecomment-6650301410)
(amaybaum, 2026-11-05).

Each row is a fragment replacement on the text at `bd926c76`. The old text is unique in its
file, and line numbers are unchanged. Book rows are applied identically to FULL.

**Ruling items.**
- **A1** adds ch18:214.
- **A2** adds Explainer:924–926.
- **A5:**
  - the Substratum:409 heading changes. The section still separates the symmetric §4.6
    content from the parameter that is conditional on its inputs.
  - ch02:220 changes. "Establish its relationship to the framework's three large emergent
    structures" overstated the arrow item, so it is narrowed to match ch02:184.
- **B1:** the apparent horizon replaces the "causal partition" clause, at Substratum:405 and
  ch02:194.
- **B2:** the conditions are added at the summary sites:
  - expanding homogeneous general-relativistic background;
  - apparent horizon;
  - null energy condition;
  - conclusion stated as non-decreasing.
- **B3:** Methodology:184.
- **B5:** Substratum:405 now says the result is background kinematics, and :14, :26 and :371
  say "read against", not that the projection supplies the parameter.
- **N1–N8** as reviewed:
  - N1, N2, N7 at Substratum:405;
  - N3 at ch02:192;
  - N4 at ch18:202;
  - N5 at Substratum:411;
  - N6 at Substratum:56;
  - N8 at SM:1592.

**Left as it stands.** ch18:214's second sentence, "Time evolution corresponds to the
horizon entropy increasing toward equilibrium", is unchanged. Ruling A1 covers only the
alignment sentence. The scientific review's B4 suggestion to make this clause conditional is
recorded here for the next review.

| # | Site (before → after) | Mirror | Class | Ruling | RECOVERY | Old text | New text |
|---|---|---|---|---|---|---|---|
| 52 | `papers/Substratum.md`:14 → :14 | — | conditional | B2, B5 | B.1, E.2 | joined by a third projection that supplies a time-symmetric observer-selection rule and, on the expanding cosmological branch, a non-decreasing horizon-area parameter. | joined by a third projection that supplies a time-symmetric observer-selection rule, read against the area of the apparent horizon, which on an expanding homogeneous general-relativistic background satisfying the null energy condition is non-decreasing as a matter of background kinematics. |
| 53 | `papers/Substratum.md`:26 → :26 | — | conditional | B2, B5 | B.1, E.2 | together with a horizon-area parameter that is non-decreasing on the expanding cosmological branch; | read against the apparent-horizon area, which is non-decreasing on an expanding homogeneous general-relativistic background satisfying the null energy condition (background kinematics, not a substratum prediction); |
| 54 | `papers/Substratum.md`:371 → :371 | — | conditional | B2, B5 | B.1, E.2 | that supplies the time-symmetric C1–C4 observer-selection theorem of [Main, §4.6] and, on the expanding cosmological branch, a non-decreasing horizon-area parameter. | that supplies the time-symmetric C1–C4 observer-selection theorem of [Main, §4.6], read against the apparent-horizon area, which is non-decreasing, as background kinematics, on an expanding homogeneous general-relativistic background satisfying the null energy condition. |
| 55 | `papers/Substratum.md`:56 → :56 | — | conditional | N6 | B.3 | the direction in which coarse-grained entropy increases is fixed by a low-entropy or product boundary condition, not by the rule (§5.4). | the direction in which coarse-grained entropy increases rests on a low-entropy or product boundary condition, not on the rule (§5.4). |
| 56 | `papers/Substratum.md`:405 → :405 | — | conditional | B5, N2 | B.1, E.2 | satisfying the null energy condition, $dA/dt = -8\pi c^2\dot H/H^3 \geq 0$: the area is non-decreasing along any comoving observer worldline, strictly increasing while $\rho + p/c^2 > 0$, and constant in exact de Sitter. | satisfying the null energy condition, $\dot H = -4\pi G(\rho + p/c^2) \leq 0$ and $dA/dt = -8\pi c^2\dot H/H^3 \geq 0$: the area is non-decreasing along any comoving observer worldline, strictly increasing while $\rho + p/c^2 > 0$, and constant in exact de Sitter. This is standard general-relativistic background kinematics, computed from the Friedmann equations of the background taken as given ([GR, §8.7]), not a prediction derived from the substratum. |
| 57 | `papers/Substratum.md`:405 → :405 | — | conditional | N1 | B.1, E.2 | Both conditions are inputs: the expanding branch is observed, not derived, and reading $A/(4 l_p^2)$ | Both are inputs: the expanding branch is observed, not derived, and the null energy condition is assumed of the matter content; reading $A/(4 l_p^2)$ |
| 58 | `papers/Substratum.md`:405 → :405 | — | conditional | B1 | B.1, E.1 | The monotonicity is a feature of the causal partition rather than of any local frame, just as every observer in a Schwarzschild geometry agrees on the exterior direction. | The monotonicity holds for every comoving observer of the homogeneous background. |
| 59 | `papers/Substratum.md`:405 → :405 | — | conditional | N7 | E.4 | At the observer level, the horizon parameter orders the expanding branch; that the other arrows | At the observer level, the horizon parameter orders the expanding branch non-strictly; that the other arrows |
| 60 | `papers/Substratum.md`:409 → :409 | — | unresolved (heading) | A5 | B.8 | **What the framework derives, and the directional-language subtlety.** | **What the framework establishes, and the directional-language subtlety.** |
| 61 | `papers/Substratum.md`:411 → :411 | — | conditional | N5 | B.5 | The memory-arrow step uses "the observer's worldline has a causal topology" as the carrier of the asymmetry. | The memory-arrow step uses "the observer's worldline has a causal topology" as the carrier of its orientation convention. |
| 62 | `papers/Substratum.md`:411 → :411 | — | conditional | N5 | B.5, B.7 | A framework in which the observer's worldline had no causal topology could not run the memory-arrow step, and the cascade would halt at the thermodynamic layer. | A framework in which the observer's worldline had no causal topology could not state the memory-arrow step. |
| 63 | `papers/SM.md`:1592 → :1592 | — | conditional | N8 | B.7 | — with the horizon-clock-plus-observer-selection projection developed in [Substratum §5.4], whose alignment of the arrows of time is open. | ; the horizon-clock-plus-observer-selection projection is developed in [Substratum §5.4], where the alignment of the arrows of time is open. |
| 64 | `papers/Methodology.md`:184 → :184 | — | unresolved | B3 | B.8 | a *causal topology*, and a derived *arrow* of time | a *causal topology*, and an *arrow* of time |
| 65 | `papers/Methodology.md`:184 → :184 | — | conditional | B2 | B.1, E.2 | on the expanding cosmological branch, horizon growth supplies a non-decreasing parameter, | on an expanding homogeneous general-relativistic background satisfying the null energy condition, the apparent-horizon area is a non-decreasing parameter (background kinematics), |
| 66 | `papers/Explainer.md`:924 → :924 | — | unresolved | A2 | B.9, C.3 | So the arrow, if there is one, has to come from somewhere else — specifically, from the observer. | So the arrow, if there is one, has to come from somewhere else — from the observer's description of the dynamics, given boundary conditions. |
| 67 | `papers/Explainer.md`:926 → :926 | — | unresolved | A2 | B.9, C.3 | A structural theorem (Main §4.6) establishes exactly that, under a stated mixing hypothesis | A structural theorem (Main §4.6) constrains the observer side of this — where observers can exist, not which way time runs — under a stated mixing hypothesis |
| 68 | `book/ch02-substratum.md`:192 → :192 | FULL:835 → :835 | conditional | N3 | B.1 | and the horizon entropy $S_{\text{dS}}(t) = A(t)/(4\ell_P^2)$ assigned to it, is non-decreasing, | and the horizon entropy $S_{\text{dS}}(t) = A(t)/(4\ell_P^2)$ assigned to it at the de Sitter calibration, is non-decreasing, |
| 69 | `book/ch02-substratum.md`:194 → :194 | FULL:837 → :837 | conditional | B1 | B.1, E.1, E.2 | The horizon area provides a structural clock on that background. Every comoving observer on an expanding background satisfying the null energy condition agrees that it does not decrease — the monotonicity is a feature of the causal partition rather than of any local frame — and the criterion | The apparent-horizon area provides a structural clock on that background. Every comoving observer of an expanding homogeneous general-relativistic background satisfying the null energy condition agrees that it does not decrease — standard background kinematics, not a prediction derived from the substratum — and the criterion |
| 70 | `book/ch02-substratum.md`:220 → :220 | FULL:863 → :863 | conditional | A5 | B.8 | The three projections establish its relationship to the framework's three large emergent structures. | The three projections establish its relationship to quantum mechanics and general relativity, and what it establishes about the arrow of time. |
| 71 | `book/ch03-structural-realism.md`:58 → :58 | FULL:932 → :932 | conditional | B2 | B.1, E.2 | on the expanding branch, horizon growth supplies a non-decreasing clock, | on an expanding homogeneous general-relativistic background satisfying the null energy condition, the apparent-horizon area supplies a non-decreasing clock, |
| 72 | `book/ch04-methodology.md`:32 → :32 | FULL:1149 → :1149 | conditional | B2 | B.1, B.2, E.2 | beyond the expanding branch, taken as given, on which the horizon area does not decrease. | beyond an expanding homogeneous general-relativistic background, taken as given, on which, with the null energy condition, the apparent-horizon area does not decrease. |
| 73 | `book/ch18-beyond.md`:202 → :202 | FULL:5015 → :5015 | conditional | N4 | C.3, C.5 | The substratum dynamics is T-symmetric; the observer's reduced description is not. | The substratum dynamics is T-symmetric; the observer's reduced description of a non-equilibrium initial condition is not. |
| 74 | `book/ch18-beyond.md`:214 → :214 | FULL:5027 → :5027 | unresolved | A1 | B.7, C.6 | The thermodynamic arrow and the cosmological arrow — the direction in which the universe expands — are aligned in the framework. | Whether the thermodynamic arrow and the cosmological arrow — the direction in which the universe expands — are aligned is open in the framework: it is neither established nor refuted. |

## Gate-manifest consequence: `verification/audit-census.json`

The ordinary PR `verify` run 41969128746 on `24452b01` failed its job "Numerical probes /
core B". The cause was `audit_census_probe.py`, AUDIT-B, vocabulary `B1-required`
(pattern "not presently discharged").

**The drift.** Row 51, the authorized ch18:216 side correction, adds a correct instance of
the required C4 status phrase at ch18:216 and FULL:5029. The counts move as follows:
- `book/ch18-beyond.md`: 0 → 1;
- FULL: 3 → 4.

**Disposition.** "repaired" still holds at that location. The phrase is the C4 status
sentence that the vocabulary requires, now in one more paragraph.

**Change.** Following the manifest's own drift rule, only `expect` and `why` of
`B1-required` change. The pattern is not widened. `python3 verification/lean/audit_census_probe.py`
passes locally after the change.

**Scope.** The manifest is a mutable gate file, not a frozen record; it is not listed in
`verification/infrastructure/legacy-records.json`. It was not in the authorized file list,
so this consequence is recorded here for the owner and reviewers to confirm, as the
LEDGER rename was.

**Owner ruling.** Accepted by owner ruling c.6650301410, item A4: ch18 0 → 1 and FULL 3 → 4.
The rule also requires the update to share a commit with the text change; this update came
in `6010cf44`, after the text change in `4081cba0`. The follow-up edits change no
audit-census count, and `audit_census_probe.py` passes.

## CI finding: the SC-42 integration step (not resolved here; reported to the coordinator)

The ordinary PR `verify` run 41970039595 on `6010cf44` failed one job, "Numerical probes /
core B", at the step "SC-42 integration source scope and must-fail controls". That step
runs `verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py`,
diffing against its pinned base `ca3a5bb2`.

1. **Wording hit: fixed.** The checker's added-text scan found one hit,
   `('papers/Substratum.md', 'caps', 'FLRW')`. The acronym in row 11 broke the
   caps-emphasis rule (§A.33). Row 11 now reads "flat Friedmann-Robertson-Walker
   background", the form Substratum:379 already uses, and Substratum `.tex`/`.pdf` are
   rebuilt (still 55 pages). Run locally after the fix, the checker gives:
   - `verdict: PASS`, with no failed predicates;
   - a `--self-test` byte-identical to the committed `sc42-integration-controls.json`.
2. **Byte comparison with the committed result: open, outside this round.** The step
   also runs `cmp` of the checker's output against the committed
   `sc42-integration-result.json` of that earlier round.
   - The checker adds one "chapter line mirrored in FULL" predicate per book-chapter line
     changed since `ca3a5bb2`.
   - This round's chapter edits add 10 such predicates and replace 1. All of them hold
     (ok = true), and the verdict is PASS either way.
   - The output therefore no longer matches the committed file byte for byte.
   - That file is another round's expected-result record. Per the coordinator's
     instruction, neither the checker nor its expected files are changed here. A
     precedent (`d83f8723`, #1013) regenerated the file for a chapter edit; whether to do
     so for this round is for the coordinator and owner to decide.

## Planned sites left unchanged

Each was reviewed against `RECOVERY.md`. No change was needed, under minimum change
(§A.25).

- **Main:744 body.** The replacement is scoped "in its role of selecting
  observer-compatible configurations". Only the label phrase changed (row 34).
- **Main:758 body** (B.9, F.4): unchanged; the title is row 35.
- **Main:760 (iii):** NO CHANGE by ruling c.6649643759, item 4.
- **Selection content kept as written:**
  - Substratum:56's selection sentence (row 3 changes only the last sentence);
  - Substratum:409's symmetry and convention content (row 13 changes only the last two
    sentences).
- **GR:797–805:** Theorem A.6 and "the generalized second law is open" are correct as
  written. GR:797 defines the generalized second law (delta review c.6649698455, item D).
- **Other retained sites:** Explainer:928 (Explainer:924–926 were later changed by ruling A2); Complexity:206; Structure:717;
  ch04:30; ch07:155–157.
- **Asking or listing, not asserting:**
  - ch02:182 (FULL:825) asks what relationship (S, φ) bears to the three structures;
  - ch03:62 (FULL:936) lists the arrow among consequences of the observer-admission
    boundary, which does bear on it through selection;
  - ch03:204 (FULL:1078) counts three projections without stating what the third derives.
- **Already stated as unresolved:** ch18:20, 204–212, 218–222, 328, 334; ch00:101;
  `book/README.md`:90; GR:805.

## Unlisted sites found by the corpus-wide grep, not edited

Grep run per §A.25 step 1, for `\barrows?\b`, "horizon clock", "structural clock",
"accelerating phase", "direction of time", "past hypothesis", "Ellis", "second law",
"horizon growth", "monotonically increasing", "unidirectional", "three projections" and
"third projection" over `papers/*.md` and `book/*.md`. These sites carry related wording but
are not on the authorized list. They are listed for an owner ruling.

1. **ch18:214 (FULL:5027).** The paragraph says "The thermodynamic arrow and the
   cosmological arrow — the direction in which the universe expands — are aligned in the
   framework" and "Time evolution corresponds to the horizon entropy increasing toward
   equilibrium".
   - It asserts alignment (`RECOVERY.md` B.7). It sits beside the edited ch18:216.
   - The plan listed ch18:204–214 as "already correct as unresolved". This record finds
     :214 an exception.
   - Recommended: the same treatment as ch18:216. **Resolved:** added by ruling A1, row 74.
2. **Substratum:399**, the heading "5.4 The arrow of time as a third projection", and
   **Substratum:393**, "(the arrow-of-time projection is developed in §5.4 …)".
   - These are labels for the narrowed framing.
   - Recommended: no change.
3. **Substratum:409's heading** "What the framework derives, and the directional-language
   subtlety". Its paragraph now states what the framework *establishes*. **Resolved:**
   changed to "establishes" by ruling A5, row 60.
4. **ch02:200 (FULL:843).** It reads "produce the persistence-based observer selection for
   the horizon-clock projection … the three projections are co-derived from a single
   construction". This is framing. Recommended: no change.
5. **ch02:220 (FULL:863).** It reads "The three projections establish its relationship to
   the framework's three large emergent structures." **Resolved:** narrowed to match
   ch02:184 by ruling A5, row 70, because it overstated the arrow item.
6. **GR:190.** It reads "Its classical layer is settled: exact finite-bath counting with
   $\beta_E>0$ makes the counting-selected profile passive (kernel: `counting_passive`)".
   It states $\beta_E>0$ as the condition, consistent with the GR:214 correction.
   Recommended: no change.
7. **Methodology:212, 214.** These describe other authors' derivations of ordering and
   arrow. Not OI claims; no change.
8. **Explainer:924–926.** Found by the Phase 2 scientific review, c.6650236439. "A
   structural theorem (Main §4.6) establishes exactly that" attributed the arrow's origin to
   §4.6. **Resolved:** added by ruling A2, rows 65–66.

## Build

- **Toolchain:** pandoc 3.1.3; XeTeX 3.141592653-2.6-0.999995 (TeX Live 2023/Debian).
- **Commands:** `sh ./build.sh Substratum GR SM Methodology Explainer Main`, then
  `sh ./build.sh --book`. Both reported `build: OK`.
- **Missing-character warnings:** 0. `build.sh` lists dropped glyphs per file and listed
  none.
- **Each `.tex`/`.pdf`** is built from the committed `.md`. `tools/staleness_check.py`
  reports 13 matched, 0 unstamped.

| Artifact | Pages at base | Pages after | Mean characters per page after |
|---|---|---|---|
| Substratum | 55 | 55 | 3185 |
| GR | 91 | 91 | 3166 |
| SM | 150 | 150 | 3156 |
| Methodology | 53 | 53 | 3021 |
| Explainer | 71 | 72 | 2786 |
| Main | 100 | 100 | 3277 |
| Book (FULL) | 560 | 561 | 2978 |

## Local checks

These were run in the worktree after the edits. They are offline and cheap, and none is
a scientific computation. All exited 0.

| Command | Result |
|---|---|
| `python3 tools/coverage_check.py` | `coverage_check: OK (134 canonical statements, 19 unattached checkers)` |
| `python3 tools/voice_check.py` | `voice_check: OK (no manuscript-voice history narration; 40 manuscript file(s) scanned)` |
| `python3 tools/claims_check.py` | `claims_check: OK (no withdrawn result asserted unconditionally)` |
| `python3 tools/duplicate_check.py` | `duplicate_check: OK (no paragraph repeated within a file)` |
| `python3 tools/staleness_check.py` | `staleness_check: OK (13 matched, 0 unstamped)` |
| `python3 tools/lean_manuscript_census.py` | `lean_manuscript_census: OK (… 25 current families; complete relative to the maintained registry)` |
| `python3 tools/artifact_placement_check.py` | `artifact_placement_check: OK (… self-test passed)` |
| `python3 verification/lean/audit_census_probe.py` | `audit_census_probe: ALL CHECKS PASS`, after the `B1-required` update |
| `python3 -I -B verification/audits/manuscript/bell-operational-reconciliation-20261029/check_sc42_integration.py` | verdict PASS, no failed predicates. Output differs from the committed result file; see the CI finding above |

The same checks passed at the base before the edits. No workflow was dispatched, and no
Lean module was built.
