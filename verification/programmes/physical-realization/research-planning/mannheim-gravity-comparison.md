# Mannheim gravity comparison and the OI G3 coupling gap

**Status: planning placeholder for review.** This note defines an investigation;
it reports no new theorem, computation or empirical result. It is not a native
control plane or an F candidate.

Planning snapshot: main `3519213a47c2c63f7ece3f55a81acffc2a96a3af` (2026-10-15).

## Question and scope

Which covariant gravitational equations and matter-coupling law follow from
OI's stated premises, which additional assumptions select them, and which
observables distinguish that completion from Mannheim's conformal gravity
and Einstein gravity with a dark-matter component?

The comparison is motivated by Philip Mannheim's lecture with Curt Jaimungal,
[Dark Matter and General Relativity Explained FROM SCRATCH](https://www.youtube.com/watch?v=HJcQLHqOziM).
Relevant passages are approximately 01:12 (higher-order Poisson equations),
01:20 (local and global gravitational contributions), and 02:07 (metric
solutions versus the equations selecting them). The
[creator's published transcript](https://curtjaimungal.substack.com/p/dark-matter-and-general-relativity)
is a source to check against the papers, not evidence for an OI derivation.

The maintained OI anchor is [GR.md at the planning snapshot](https://github.com/amaybaum/incompleteness/blob/3519213a47c2c63f7ece3f55a81acffc2a96a3af/papers/GR.md),
especially its abstract's G1-G4 dependency ladder, section 6.2's gravitational
coupling question, and sections 7.2-7.3's dark-sector construction and inherited
conditions. G3 is the open covariant field-equation, matter-coupling,
conservation/Bianchi and continuum-limit obligation. Horizon identities at G1
and weak-field consistency at G2 do not alone discharge it; G4 phenomenology
inherits G3 and its other named assumptions.

## Proposed work, in dependency order

- [ ] Build a source-to-claim ledger for both constructions. Distinguish
  assumptions, mathematical results, fitted quantities, conditional claims and
  raw observations. Check the hypotheses of any equation-selection theorem,
  including derivative order, dimension, field content and matter coupling.
- [ ] State the candidate OI covariant response law, its source variables,
  conservation equations and boundary conditions. If these are not fixed by
  the available premises, identify the exact missing map or selection principle
  before attempting a rotation-curve fit.
- [ ] Derive the weak-field scalar potentials from that same law. Identify
  which potential governs orbital motion and which combination governs light
  deflection, so that dynamics and lensing are tested jointly.
- [ ] Compare the resulting radial response with Mannheim's local and global
  terms, and with the conditional MOND-like response in GR section 7.3.
  Trace the coefficient of the acceleration scale: that section imports the
  factor 1/6 from Verlinde rather than deriving it from the substratum.
- [ ] Audit the vacuum-energy step. Determine whether a constant offset in
  the emergent Hamiltonian changes the gravitational source in the candidate
  completion. Quantum-statistical invisibility of the offset is a separate
  question from gravitational decoupling.
- [ ] Specify an observational comparison with shared data, explicit
  uncertainties and parameter accounting. Separate universal constants,
  fitted stellar mass-to-light ratios, distance/inclination uncertainties and
  independently predicted quantities. Include lensing and cluster or
  cosmological tests before making a general claim about dark matter.

## Controls and evidence obligations

- Recover the stated Newtonian and relativistic limits under their explicit
  assumptions; check conservation, boundary dependence and causal propagation.
- Test uncoupled or isolated limits where the proposed law claims they apply.
  Global boundary dependence is not by itself instantaneous signalling.
- Use a completion with the same horizon identities but a different source
  coupling as a control for any claim that those identities select the dynamics.
- Compare direct measurements as measured. For inferred quantities, expose the
  model-dependent inference rather than accepting or rejecting its summary
  without reproducing the underlying observables (AGENTS section A.24).
- Treat hidden-sector inaccessibility, dark-matter phenomenology and conformal
  symmetry as distinct statements requiring their own bridges.
- A fitted match is recorded as a fit; consistency checks and empirical
  confrontations retain separate evidence labels. A controlled failure limits
  the specific construction tested.

## First review milestone and possible outcomes

The first deliverable is a premise/source ledger and one explicit
weak-field-and-lensing implication, or a precise account of the missing
coupling map that prevents it. A useful negative outcome is a pair of
completions satisfying the same stated premises but giving different
gravitational predictions. A useful conditional outcome names every added
selection principle and the observables it constrains.

Before computational execution, fix the scope, controls, decision rules and
replay requirements. Any native round follows AGENTS section A.39, with its
own control plane and exact owner-designated F. This placeholder designates
no round and adopts no replacement gravitational law.

## Initial sources and related work

- Mannheim and O'Brien, [Galactic rotation curves in conformal gravity](https://arxiv.org/abs/1211.0188).
- Horne, [Conformal Gravity Rotation Curves with a Conformal Higgs Halo](https://arxiv.org/abs/1601.07537):
  a matter-coupling/conformal-frame challenge to examine alongside the responses.
- Dull, Schuller, Stritzelberger and Wolz,
  [Gravitational closure of matter field equations](https://arxiv.org/abs/1611.08878):
  check the exact matter and canonical-evolution premises before importing its conclusion.
- Planck Collaboration, [2018 cosmological parameters](https://arxiv.org/abs/1807.06209).
- LIGO/Virgo/KAGRA, [Tests of General Relativity with GWTC-3](https://arxiv.org/abs/2112.06861).
- The [OI-QM programme](../../oi-qm/PROGRAMME.md): the F2 operational reconstruction
  is a separate obligation. This comparison does not supply its physical
  observer, measurement or control principles.

This PR adds this planning note only. Manuscript or status corrections
supported by the investigation require their own reviewed change and
whole-corpus propagation under AGENTS section A.25.
