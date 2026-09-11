# OI → hydrodynamics and continuum-breakdown research programme

Status base: `main` at `375e8cd50e2fc916ff96dd45ce072a1a2fdf63e4` (post-PR #571, Track B act 6 closed).

This is a **strategic parallel-track roadmap**. It is not a theorem, audit, preregistration, execution result, or manuscript edit. Detailed mathematical status remains controlled by the formal sources, frozen audits/results, verification ledger, and manuscript scope guards.

This programme sits under §8 of `verification/programmes/oi-qm/PROGRAMME.md`: it neither advances nor blocks the OI → QM equivalence/classification chain unless an explicit theorem later connects the two. Conversely, OI → QM results may not be imported here as evidence without a proved bridge.

---

## 1. Ultimate objective

The strongest hydrodynamic endpoint would be a theorem of the form

`concrete OI substratum + explicitly named hydrodynamic conditions -> Navier–Stokes`,

followed, if the named conditions can themselves be derived from the concrete OI physics, by the stronger result

`concrete OI substratum -> Navier–Stokes in a stated hydrodynamic/continuum limit`.

If Navier–Stokes is not uniquely forced, the acceptable endpoint is a universality/classification theorem identifying exactly which OI-compatible local reversible substrata have Euler/Navier–Stokes hydrodynamics and which do not.

A second, downstream objective is to test a **continuum-breakdown hypothesis**:

> a continuum singularity may be a singularity of the emergent observable/continuum description while the underlying finite reversible substratum remains completely regular.

This is initially a hypothesis to test, not a claim of the corpus.

---

## 2. Why this programme is plausible but not yet proved

The concrete OI representative already carries structural ingredients naturally associated with hydrodynamic universality: finiteness, deterministic reversible dynamics, bounded/local coupling degree, center/translation independence up to gauge, linearity, and background independence (A1–A6 of the substratum programme).

Those ingredients are not by themselves Navier–Stokes. In particular, the present roadmap does **not** assume that A1–A6 already imply:

- a locally conserved mass or number density;
- a locally conserved momentum density;
- the exact isotropy order needed by the stress tensor;
- local equilibrium or sufficient mixing;
- a hydrodynamic scaling limit;
- a constitutive relation producing a positive viscosity;
- incompressibility.

The first task is to determine which of those are already derived by the concrete substratum and which are genuinely additional conditions.

There is strong external precedent for the general mechanism, but it is only precedent. Frisch, Hasslacher and Pomeau (Phys. Rev. Lett. 56, 1505 (1986), DOI 10.1103/PhysRevLett.56.1505) showed that a class of deterministic lattice gases with discrete Boolean variables reproduces Navier–Stokes hydrodynamics. That result demonstrates logical/mathematical plausibility of discrete deterministic microdynamics yielding NS; it is **not** evidence that the OI representative satisfies their hypotheses.

The OpenAI Navier–Stokes work announced on 2026-09-08 supplies a sharp downstream test case for continuum breakdown: its stated result is a finite-time singular solution of the continuum equations with finite energy. Until independently settled in the normal mathematical process, this roadmap treats that work as an **external target/motivation only**, never as a premise in an OI theorem.

---

## 3. The hydrodynamic theorem ladder

The programme should not jump directly from A1–A6 to Navier–Stokes. It should close the following obligations in order.

### H1 — local conserved observables

Identify candidate microscopic observables corresponding to mass/number and momentum and prove exact local conservation laws under the concrete reversible update, or prove that the current substratum does not supply them.

A conservation law must be a theorem about the microscopic dynamics, not merely a conserved quantity of a chosen continuum fit.

### H2 — isotropic tensor structure

Determine whether the existing center-independence/cubic or octahedral covariance results are strong enough to force the isotropic tensor identities required by the hydrodynamic stress expansion at the needed order.

If not, state the missing isotropy condition explicitly. Do not replace cubic symmetry by full rotational symmetry silently.

### H3 — local equilibrium / mixing

State and test the weakest mixing or local-equilibrium condition needed to close the macroscopic equations. Existing hidden-sector mixing assumptions may be relevant only if a theorem identifies the same object; analogy is not a bridge.

### H4 — scaling map

Define the microscopic-to-continuum map and the scaling regime explicitly: lattice spacing, time scaling, field normalization, carrier growth, and the topology/norm in which convergence is claimed.

No statement of a continuum PDE is meaningful until this map is fixed.

### H5 — Euler-level limit

Derive the conservative hydrodynamic equations first. Identify pressure and the equation of state from the microscopic model or name them as additional constitutive input.

### H6 — viscous correction

Derive the first dissipative correction and identify the viscosity coefficient. The key question is whether irreversible viscous transport emerges from reversible microscopic dynamics by coarse-graining/mixing and scaling, rather than being inserted by hand.

A positive viscosity is an outcome to prove, not a default sign convention.

### H7 — incompressible Navier–Stokes

Only after H1–H6 are closed should the programme take an incompressible/low-Mach limit and prove a theorem of the form

`∂_t u + (u·∇)u = -∇p + ν Δu`,  `∇·u = 0`,

at an explicitly stated scope, dimension, boundary condition, and regularity class.

---

## 4. Outcome taxonomy for the hydrodynamic branch

Every hydrodynamic round reports one of four statuses.

### HD — Derived

The required hydrodynamic structure follows from already accepted concrete OI physics at the stated scale and scope.

### HC — Conditional

The structure follows only after adding a named physical/statistical/scaling condition. The result must say whether that condition is independently motivated and whether it is known to be necessary, sufficient, or merely sufficient.

### HI — Independent

A lawful OI countermodel shows that the structure is not implied by the current assumptions. This is a classification result, not a failure.

### HO — Open

The derivation is incomplete and no impossibility/countermodel has been proved. Construction or formalization failure is not independence.

The target should progressively reduce the conditional set rather than hiding it in the phrase “hydrodynamic limit.”

---

## 5. Continuum singularities: a downstream branch only

The singularity programme opens **only after** a controlled continuum bridge such as H4–H7 exists. Before that point, statements about OI resolving fluid or spacetime singularities are speculation and may not enter the manuscript as results.

### S1 — finite regular approximants versus singular continuum limit

Test whether a sequence of finite reversible OI systems can remain completely regular at every finite resolution while their emergent continuum fields develop unbounded local quantities in the limit, for example

`∀b < ∞ : ||u_b(t)||_∞ < ∞`,

while

`lim_{b→∞} ||u_b(t_*)||_∞ = ∞`,

with a uniform extensive bound such as

`sup_b ||u_b(t)||_2 < ∞`.

If proved, this would establish a precise mathematical sense in which a **continuum singularity need not be a substratum singularity**.

### S2 — singularity as failure of the emergent map

Identify exactly what fails at the singular limit: uniform convergence, differentiability, invertibility of the coarse-graining map, boundedness of a local observable, effective metric completeness, or something else.

“Breakdown of the continuum description” is not a theorem until the failed map/property is named.

### S3 — distinguish horizons from singularities

The programme must not equate a black-hole event horizon with a spacetime singularity.

- an **event horizon** is a causal/observational boundary: a region from which signals cannot reach the relevant asymptotic exterior;
- a **spacetime singularity** in classical GR is ordinarily characterized through geodesic/path incompleteness or related breakdown of the spacetime geometry.

Both may eventually admit an OI interpretation in terms of observer-accessible incompleteness, but they are distinct mathematical phenomena and require separate bridges.

### S4 — black-hole observational-incompleteness hypothesis

A precise OI version of the idea would be:

1. the underlying substratum evolution remains a globally defined finite bijection;
2. the observer-accessible/emergent geometry develops a causal region inaccessible to a specified exterior observer (horizon branch);
3. the effective continuum geometry may become geodesically incomplete or otherwise singular (singularity branch);
4. neither 2 nor 3 is interpreted as failure of the microscopic bijection unless a theorem proves such a failure.

If this chain can be constructed, black-hole physics would provide an example where **observational or emergent incompleteness coexists with complete underlying dynamics**. This is the hypothesis to test — not a restatement of GR and not yet an explanation of black holes.

### S5 — recovery obligations

Any serious black-hole claim must recover, at minimum, the relevant effective causal structure and distinguish which of the following are derived versus assumed:

- an effective Lorentzian metric or causal order;
- trapped regions / event horizons where claimed;
- geodesic or path incompleteness where a singularity is claimed;
- area/entropy relations where invoked;
- Hawking/thermal behavior where invoked;
- information flow and observer-dependent accessibility.

A finite substratum by itself does not settle any of these.

---

## 6. First research rounds

### Round H-A — hydrodynamic source audit

Inventory the concrete OI substratum against the exact ingredients of deterministic lattice-gas hydrodynamics and modern hydrodynamic-limit theorems. The round asks, one item at a time, whether mass conservation, momentum conservation, required isotropy, mixing/local equilibrium, and a scaling map are **derived, conditional, independent, or open**.

This is the first round because it can sharply bound the programme before any large derivation is attempted.

### Round H-B — minimal reversible fluid witness

If H-A does not stop the programme, construct the smallest explicit OI-compatible reversible local model carrying the required conserved fields, and prove its discrete conservation and symmetry properties.

This is a witness/construction round, not yet a continuum theorem.

### Round H-C — hydrodynamic limit

Freeze the scaling and convergence topology before execution. Derive the conservative limit and then the viscous correction, with Euler and Navier–Stokes reported separately.

### Round S-A — continuum-breakdown test

Only after H-C: use the derived continuum map to test whether regular finite substratum approximants can converge to a continuum singularity with bounded extensive quantities.

### Round S-B — spacetime/horizon branch

Only after an effective-geometry bridge exists: test whether horizons and geodesic incompleteness can arise in the emergent geometry while the finite reversible substratum remains complete. This round must keep horizon inaccessibility and singularity/geodesic incompleteness separate.

---

## 7. Programme-level controls

1. **Parallel-track separation.** No result here counts as progress on OI → QM, and no OI → QM result counts here without an explicit bridge.
2. **Bare OI is not NS.** The programme concerns the concrete local OI substratum plus whatever hydrodynamic conditions survive the source audit, not arbitrary finite reversible systems.
3. **External precedents are not premises.** FHP motivates plausibility; the 2026 OpenAI NS work supplies a test case. Neither may be used as evidence that OI satisfies a missing hypothesis.
4. **Reversibility versus dissipation must be proved, not hand-waved.** Viscosity must arise through an explicit coarse-graining/mixing/scaling theorem if claimed.
5. **Fix the continuum map before testing singularities.** No continuum blow-up claim is admissible without an explicit finite-to-continuum map and convergence notion.
6. **Do not equate horizon and singularity.** Observational inaccessibility and geodesic incompleteness are separate obligations.
7. **Do not read finite substratum regularity as a black-hole solution.** A regular bijection only says the microscopic update is defined; it does not by itself reproduce GR causal structure or resolve a singularity theorem.
8. **Outcome asymmetry.** One explicit counterexample can establish independence at a stated scope; failure to derive NS or a singularity bridge establishes only Open unless a no-go theorem is proved.
9. **Evidence type is always stated.** Kernel theorem, exact probe, prose/source audit, and theorem-from-external-premise remain distinct.
10. **No manuscript strengthening from this roadmap.** Publication-facing claims wait for the relevant theorem chain or an explicit classified endpoint.

---

## 8. Current one-line state

**A new parallel programme is opened: determine whether the concrete finite, deterministic, reversible, local OI substratum lies in a Navier–Stokes hydrodynamic universality class, first by auditing the exact conservation, isotropy, mixing and scaling obligations and then, only if that bridge closes, test whether continuum fluid and spacetime singularities can arise as failures/incompleteness of the emergent observable description while the underlying substratum dynamics remains regular. Black-hole horizons are treated as causal/observational boundaries and spacetime singularities as geodesic/path incompleteness; a future OI explanation may connect both to observer-level incompleteness, but the two are not conflated and no such result is presently claimed.**
