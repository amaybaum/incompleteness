# C5-P as a property of an operational completion: design specification

**Design draft, not a preregistration.** Nothing here is frozen and no computation runs against it. It fixes what a
later preregistration must declare before C5-P is tested as a limit along a family of finite constructions rather than
as exact purification on one fixed finite carrier.

## Why the target changes

- papers/Main.md:352 [corpus]: "The purification, continuous-transitivity, and tomographic-locality axioms of the cited
  reconstructions are hypotheses of their continuum endpoint, which the classical-dimension obstruction places beyond
  any fixed finite carrier; they are not what the finite characterization uses." The full continuum-QM target lies in a
  compatible completion. Finite-carrier probes (nodes 8 and 9) are diagnostics and do not exclude such a completion.
- Lemma F (node 9 PREREG §2.4): finite protocols with rational preparations and transition probabilities never attain
  irrational quantum values exactly, though they can approach them.

## A fixed gap, stronger than the exactness obstruction

- **Lemma G (stabilizer gap) [rec, owner 2026-10-21].** For a pure stabilizer state on any finite number of qubits, a
  fixed local Pauli measurement has outcome probabilities in {0, ½, 1}. By the stabilizer density-matrix expansion, a
  Pauli expectation is 0 unless ±(the operator) lies in the stabilizer group, and is then ±1. For the biased witness
  with P(0) = 3/4, every pure stabilizer extension therefore errs by at least min_{q ∈ {0,½,1}} |3/4 − q| = **1/4**.
  This holds regardless of the number of systems, memory or circuit depth.
- **Coordinator check (numerical).** Over the 24 pure states reachable under H_A, H_B, CNOT_AB, X_A, X_B and
  Z-measurement updates from |00⟩, every single-qubit Bloch component lies in {−1, 0, 1} (`../owner-checks/fb2.py`).
- **Scope.** The bound holds while candidate pure extensions remain stabilizer states and the designated local
  measurement is preserved. Any other encoding or operation family is evaluated separately.
- The same three-value structure is the uniform-affine obstruction of node 8 and model A (node 9 NOTES, "the
  biased-state obstruction").

## Four declarations required before any convergence study

1. **The family and its embeddings.** Declare a sequence of finite constructions 𝒯₁, 𝒯₂, …, with maps carrying each
   stage's preparations, measurements, records and composites into the next. Each map must preserve the meaning of
   those objects: a stage-k experiment is still the same experiment at stage k+1. The family must state what supplies
   pure extensions outside the stabilizer/uniform-affine class (G2) before any convergence study is launched.
2. **Operational error.** Fix in advance a finite family 𝓔 of experiments, with the P(0) = 3/4 witness and the six- and
   seven-operation composition witnesses included at every stage. The stage-k error is the supremum over 𝓔 of the
   absolute probability differences against the declared target. Every experiment in 𝓔 is computed exactly at each
   stage.
3. **Purity: two proposals, never merged.**
   - (P-fin) Witnesses are pure at every finite stage, by the preparable-decomposition rule of that stage.
   - (P-lim) Purity is required only in the completion.
   
   A sequence of finite-stage pure states need not converge to a pure state of the completion. So approximate marginal
   matching alone never establishes endpoint purification. Under either proposal, endpoint purity is a separate proof
   obligation.
4. **Essential uniqueness.** Alternative purifications of the same target must become related, to within the stage-k
   error, by allowed reversible operations on the purifying system. Report this as its own line; it is never inferred
   from existence.

## Required controls

- **K-STAB-GAP (negative).** Every stabilizer-type family has stage error ≥ 1/4 on the biased witness at every stage. A
  convergence engine that reports the error going to 0 on it is broken.
- **K-RAT (calibration).** A family of rational finite approximants to a known qubit state. The error must go to 0,
  while exact attainment fails (Lemma F).
- **K-G1.** The six- and seven-operation witnesses. They are fixed and are never tuned.

## Two witnesses kept separate

- **G1, composition.** The six-operation experiment tests whether joint interactions compose correctly. The signed
  (stabilizer) repair passes it.
- **G2, pure-state richness.** The biased-marginal experiment tests whether the pure-state family is rich enough. The
  signed repair fails it, by Lemma G.

These are separate witnesses. That does not make them logically independent: purification and essential uniqueness may
also constrain composition. Fresh independent reservoirs are an assumption of the implementations tested so far, not a
universal requirement on an OI completion.

## Order

1. This specification, with K-STAB-GAP.
2. Model A stays a calibration. Its size is not increased in pursuit of purification while its pure-state family
   retains the 1/4 gap.
3. G1: an independently motivated composition rule for joint records, with K-G1 fixed.
4. G2: a proposed enlarged family must name what supplies non-stabilizer pure extensions before a convergence study.
