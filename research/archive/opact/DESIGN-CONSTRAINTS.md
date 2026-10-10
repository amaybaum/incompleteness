# Design constraints carried into the DRIVE and P2 (effect-generation) freezes

Off-repo working note. Source: OPACT investigation from `254ad0a7` (scratchpad/opact/RESULT.md §2; exact E6, E9).

1. **Continuous DRIVE is not a stage operation.** If the stage index is countable, a probability-continuous
   one-parameter family that maps stage preparations to stage preparations, or stage effects to stage effects
   (read on the body), is constant. A reversible stage-wise operation on finite stages generates no
   nontrivial one-parameter group at all (divisibility). DRIVE must be typed on the completed body (OPACT-C /
   `CompletionAction`), with the flow acting on completed states.

2. **The P2 effect family is completed, not `stageEffects`.** `EffClose` / V4′ with
   `avail = stageEffects` is inconsistent with a nontrivial drive whose seed lies in `stageEffects`: the seed
   would be flow-invariant on the body. Stage effects ⊂ completed effects; the continuous symmetry acts on the
   latter. No freeze may preregister closure of `stageEffects` under a continuous group.

3. **StateRespect ≠ AffineRespect.** Only AffineRespect yields the unique affine extension; StateRespect is
   strictly weaker (countermodel `midOp`). A later round that sources operations must deliver AffineRespect
   (or a mixture-closure premise from which it follows), not StateRespect alone.

4. **Parameter continuity lives on the chart.** For a body of finite rank, continuity of a flow reduces to
   continuity of finitely many coordinate probabilities; norm continuity on all of ℓ^∞ is not the target.

5. **Finite-representative gauge principle (from RANK/OI-STAGE, 2026-10-02).** A1's finite representative is
   gauge for observables determined by finite visible/boundary data over the regime of the transfer theorem
   (Substratum.md:262). It is **not** established as gauge for the completion body, which depends on arbitrarily
   long conditioning histories: on a finite representative the body is a polytope with finite automorphism group
   (NG1), while on the infinite lattice the horizon dimensions grow (nonlinear rule: 0, 3, 5, 10, 20, 49, 88, 153).
   Any DRIVE built on the completion body must be built on an infinite member of the orbit, and "choose the finite
   representative without loss of generality" must be scoped to the observable class. Three distinct notions:
   finite observation ≠ finite predictive state ≠ quantum operational quotient.

6. **Selective-branch lemma and the record sector (from QUOTIENT, 2026-10-02).** Any effect space containing the
   unit and closed under the selective observation branches o_v* contains every protocol effect (each singleton
   effect is a branch word applied to the unit). A proper finite operational sector can therefore be invariant only
   under non-selective operations; selective outcomes must be written into a separate record sector. On the
   nonlinear and majority leap rules no 4-dimensional effect space containing the unit is invariant under the time
   step for effects of length ≤ 5 (≤ 7 nonlinear); the natural seed's orbit grows 2,3,4,…,9 under W and 2,4,5,8,13
   under W,F,S. These rules are controls, not candidates. Parked next direction (owner): the weakest field-neutral
   record-writing extension of the OI tower with a fixed 4-dimensional system-effect space preserved by
   non-selective operations, outcomes stored in a record sector (NG2: invasive observation is required).

7. **Dispositions after QUOTIENT (owner, 2026-10-02).** Nonlinear leap rule: closed as a forward candidate,
   retained as a negative control. Majority leap rule: closed as a forward candidate, retained as a negative
   control; its classical 4-simplex sector (three frozen period-3 phases cycled by W, plus absorbing states) is
   kept separate from the failed observer-interface target. QUOTIENT: negative at the stated finite horizons (no
   4-dimensional W-invariant effect space containing the unit at the tested depths; under W, F, S the maximal
   invariant space is {unit}). RANK: the finite-representative result is certified but does not promote to
   completion or all-horizon geometry (scope note). No act, freeze or repository mutation follows; design and
   control evidence only. No further depth on nonlinear/majority unless a later theorem makes a specific deeper
   horizon evidentially necessary. The live fork is the parked record-writing observer-interface investigation.

8. **Three-layer premise split (owner, 2026-10-03); scope of items 6–7.** Premises are classified as
   **G** (general operational interface: selective branches, record sector, disturbance allowed, forgetful
   non-selective operation, unit, consistent composition, explicit system/record split — not quantum),
   **R4** (elementary-system finite rank 4: R4-global = whole effect space of rank 4; R4-sector = a 4-dimensional
   unit-containing effect space invariant under the non-selective generators — system-specific, not a QM axiom),
   **Q** (QM-selecting: geometry, reversible transformations, sharpness, transport/dilation, composition, local
   tomography or replacement), and **theorem** (to be proved from earlier ones). Principle: the general framework
   must be broad enough to contain the negative controls; QM-specific premises eliminate them. Accordingly the
   dispositions in items 6–7 are scoped to R4: nonlinear and majority are closed as candidates for a
   passive-interface 4-dimensional elementary-system representation, not as operational theories; they are
   controls for R4 and Q, not for G. NG2 is a Q-layer (geometry) result. Operational invasiveness is a G clause
   whose truth is interface-dependent (RECORD Level 1: the linear rule is operationally non-invasive for every
   interface, proved), so it excludes no rule until the interface is broad enough.

9. **Two-track research plan; descriptive-level field; held GR/SUBSTRATE BRIDGE (owner, 2026-10-03).**
   Track I (observer/QM reconstruction: substrate → G → R4 → Q → QM; DRIVE, OI-STAGE, OPACT, RANK, QUOTIENT,
   RECORD, the premise ledger) and Track II (gravity/substrate: dynamical causal/metric structure, locality,
   equivalence-principle behaviour, backreaction, GR in a macroscopic limit) are kept distinct; GR is never assumed
   in Track I. The premise ledger carries a **descriptive-level** field — SUBSTRATE / INTERFACE (G) / R4 / Q — to
   catch observer-level quantum linearity being imposed on the substrate. Held item, after the ledger, with no claim
   that GR is derived: **GR/SUBSTRATE BRIDGE**, first questions (owner): (a) does the OI formulation require the
   substrate to be linear anywhere; (b) which premises assume a fixed background or causal structure; (c) which
   definitions survive dynamical causal/metric structure; (d) can the QM reconstruction be stated without the
   spacetime structure a gravity reconstruction must explain; (e) which extra substrate assumptions GR needs, and
   which are independent of Q. Target architecture (conjectural): common substrate principles ⇒ QM as the
   observer-accessible operational theory and GR as the effective dynamical geometry; the compatibility question is
   whether the substrate's effective geometry acts on, and is sourced by, the quantum sector as QM on curved
   spacetime requires.
   Corpus anchors found at 0f2687b7 (§A.19 — these are existing answers, to be read before the bridge starts):
   (a) yes, explicitly — (A5) linearity of the substratum update is a named posit (Substratum.md:100; Main.md:706
   posit-ledger item vii), equivalent to amplitude-scale gauge, held as a Tier-3 sharpened stipulation
   (Substratum.md:266–268), which also records that deriving it from the observer architecture would be circular
   (a nonlinear F gives observable amplitude-dependent dispersion). A5 is consumed by the wave-equation selection and
   the SU(N) reduction (Substratum.md:144–162; SM §4.1). GR.md:669 states the gravity-side partition results
   (U1–U3, ħ, area law, 1/4) do **not** need A2–A5 and survive a nonlinear or stochastic substratum under H-slope,
   H-frame, H-Hawking. So the corpus already splits the two tracks' linearity dependence: Track II's G1 results are
   claimed A5-free; the SM/gauge side is A5-conditional. (b)/(c) A6 background independence (covariant link data)
   is distinct from the state-dependent coupling graph (Substratum.md:102), whose metric/Ollivier–Ricci stability is
   the explicit hypothesis H-Bell (Substratum.md:132). GR.md's ladder: G1 horizon identities, G2 weak-field
   (done at consistency level), G3 covariant field equations open, G4 conditional on G3. In the corpus both QM
   (trace-out) and gravity (horizon thermodynamics / continuum limit) are emergent from the substratum; neither is
   substrate-level. RECORD relevance: the linear leap rule is the A5-type representative and the nonlinear and
   majority rules are A5-violating, so "substrate nonlinear, observer sector linear" is in direct tension with A5 as
   posited; the bridge must engage A5 (and amplitude-scale gauge) explicitly rather than around it.
   Ledger fields added for A5 (owner, 2026-10-03): consumers split into **direct** (consume A5 itself: the
   wave-equation selection, the amplitude-scale U(1)-phase stripping in the gauge-group reduction) and
   **transitive** (depend on A5 only through a direct consumer); a **replacement obligation** per direct consumer —
   the observer-level or intermediate theorem that would have to recover the exact linear structure that consumer
   needs if A5 is removed. Gravity scope: only the G1 horizon results are stated A5-free (GR.md:669); G2–G4 carry
   their own dependency status, G3 open; "GR is A5-free" is not claimed.
