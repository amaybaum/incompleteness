# OI-BH-1 — Hawking radiation, Page curve, and observer-access audit

Status: exploratory research / unreviewed. No manuscript amendment, theorem designation, or merge authorization.

## Source and scope

Primary manuscript: `book/ch07-gravity.md` §7.6 (as inspected 2026-10-25), including the nested partition `S = C_V × C_B × C_D`, H-scramble, the Page curve, proposed `0.646 t_evap` timing, island/cycle analogy, and generalized-second-law claim. Also inspect the gravity companion's Appendix A and existing hydrodynamics programme before claiming new results.

Do not conflate finite observation-horizon results in the foundations with physical event horizons. This research track does not modify A1/A2 exact-QM targets or adopt a new C5.

## Preliminary audit findings (not yet independently reproduced)

**BH-01, microscopic versus radiative information:** Bijectivity of the substratum map implies injective microscopic evolution, not injectivity of the restricted radiation channel. A finite example is `F(b,r)=(b,r)` with all input information in `b` and unchanged radiation `r`: perfectly reversible dynamics but radiation cannot reveal `b`. Require a theorem on transfer of distinguishing information to *accessible joint radiation records*, not just persistence in the global state. Extend to a fully evaporated endpoint with explicit late remnant/hidden-sector assumptions.

**BH-02, classical typicality versus quantum typicality:** Uniform sampling from cycles or classical configurations does not imply a Haar-like pure-state ensemble. A reversible permutation restricted to a computational product basis generates no entanglement from those basis states. H-scramble is acknowledged as open by the manuscript. Specify its exact ensemble, measure and dynamical hypotheses; test whether H-scramble already assumes the desired Page entropy, and whether it is derivable from C1–C4, a separately adopted information postulate, or the finite operational bridge.

**BH-03, entropy and the generalized second law:** General CPTP channels obey data-processing for relative entropy, but von Neumann entropy need not increase: a reset channel sends maximally mixed qubit to pure `|0><0|`, dropping entropy from one bit to zero. Strong subadditivity alone does not prove nondecrease of `S_matter+S_BH+S_dS` without geometric entropy definitions and physical evolution conditions. Identify missing hypotheses or downgrade claim.

**BH-04, Page-time fraction:** Under a Schwarzschild idealization with `dM/dt=-a/M²`, `t/t_evap=1-(M/M0)^3`; if `S_BH∝M²` and turnover is postulated at half initial black-hole entropy, `M/M0=1/√2` and `t/t_evap=1-2^{-3/2}≈0.6464`. The fraction is therefore conditional on the half-entropy turnover and the cubic mass-loss relation. Test greybody/species dependence, changes in effective degrees of freedom, entropy carried by radiation versus decreasing area, and the physical distinction between 'half the initial area lost' and a Page equality. No claim of universal agreement with island computations without comparing matching setups.

**BH-05, nested trace consistency versus information reconstruction:** Associativity of classical marginalization or partial traces is not a proof of a common emergent Hamiltonian, a common physical channel for dynamical horizons, or late-time radiation decoding. Retrieve actual bridge lemmas and list precisely what they establish.

**BH-06, islands and cycles:** `replica wormholes ↔ substratum cycles` is conjectural. Provide a mathematical map of the observables/replicas and matching correlators before calling this a microscopic realization of islands.

**BH-07, thermality:** A thermal-looking one-body spectrum need not be an exactly thermal joint state. Separate marginal Gibbs-like statistics, pair correlations, and total-radiation recoverability; specify the Hawking spectrum's greybody factors and approximation regime.

## Independent research lanes

1. **Formal finite access model.** Finite reversible substratum `F`, nested records `V/B/D`, emitted registers `R_1...R_n`. Define two initial states to be equivalent under a family of physical measurement protocols iff their joint-record distributions coincide. Construct one positive recovery example and one counterexample showing reversible global dynamics without accessible recovery. Record explicit protocol access restrictions and whether access can grow with time.
2. **Entropy lane.** Distinguish Shannon entropy of observer records, von Neumann entanglement entropy after a justified quantum representation, and generalized entropy including area terms. Produce a valid theorem or counterexample for each claimed monotonicity and identify exact dependencies.
3. **Page lane.** Compute toy curves for permutation-only, random unitary, and restricted-interface models using exact small systems where possible. Distinguish ensemble-average Page typicality from an actual fixed dynamical law; test scrambling as an independent property.
4. **Gravity lane.** Map Hawking temperature, greybody corrections, shrinking horizon geometry, energy conservation, and island/QES conditions to named OI assumptions; distinguish a conditional reproduction from a gravitational derivation.
5. **Manuscript integrity.** Trace each claim to an exact source, theorem, proof obligation and independent test; propose wording adjustments in a separate follow-up only after review.

## Acceptance / falsification criteria

- Each proposed claim marked PROVED / CONDITIONAL / COUNTEREXAMPLE / OPEN and backed by reproducible files and exact commit SHA.
- Explicit control: bijective, non-scrambling permutation should *fail* a claimed automatic Page curve.
- Explicit control: CPTP reset should *fail* unconditional entropy increase.
- Demonstrate at least one multi-emission correlation recovery model with a fixed physical access class; otherwise record the obstruction.
- No paper-level claim of a resolved paradox, quantum-gravity derivation, or universal 0.646 timing until the dependencies are discharged.
- Respect repository governance: separate F/E/review/receipt stages where applicable, exact-SHA CI, no automatic merging.

## First experiment

Use two initial classical messages `b∈{0,1}` and a reversible process which swaps the message into an outgoing register for a positive case; compare to one which leaves it in a retained hidden register for the negative case. Verify bijectivity and calculate the observer's full-record distinguishing advantage. Then construct a quantum Bell-pair transport model to evaluate the full radiation's von Neumann entropy by stage; compare with a product-basis permutation that cannot generate entanglement. These are discrimination tests, not a proof of black-hole physics.

## References to verify

- Hawking (1975), particle creation by black holes.
- Page (1993), average entropy of a subsystem.
- Popescu–Short–Winter (2006), canonical typicality under assumptions.
- Penington (2019/2020); Almheiri et al. (2019/2020), islands and replica wormholes.
- Existing OI gravity companion Appendix A, H-scramble/H-Hawking/H-slope conditions.

No changes to the existing manuscript until the audit has an independently reviewed result.
