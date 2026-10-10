# Thread G — Effect-family reconstruction (P2/O1) (read-only research; charter as directed by the owner, 2026-10-01)

## Mission
Answer: what effect family does the OI completion itself canonically supply? Derive or rule out candidate definitions
of P2 (the completion's available effect family) from already-landed OI machinery. Do not try to prove KInf1 as a whole.
Do not assume K∞-R (drivability, D2–D9); that is a separate target. Background: threads/F/LEDGER.md — KInf1 is a
conditional shell (compact → convex → drivable → SEC); with full effects in finite dimension SEC is automatic (B7/B8),
with the unit alone it fails; so its content lives in P2.

## Research sequence
1. Inventory every existing source of effects in the repository: response functions, finite-stage readouts,
   exposed-face functionals, attach/read-out constructions, copy operations, conditioned laws, anything that maps states
   to [0,1]. For each record: canonical? representation-independent? functorial? survives passage to the completion?
   With exact identifier and file:line at 6d0abf6b, or corpus location.
2. Generate candidate P2 definitions, not candidate axioms. A candidate must be constructed from OI data. "All affine
   effects" is allowed only if OI actually proves all of them operationally available. "Response effects" already fails
   on the SIC ball (Thread F) and cannot simply be reused.
3. Test each candidate against the controls before proving anything:
   - Bloch / 3-ball: must supply enough support effects;
   - SIC realization of the Bloch ball: must not depend incorrectly on one finite realization;
   - bidisk: exposes whether the construction silently assumes strict convexity;
   - finite stages: how their effect sets approximate or generate completion effects;
   - unit-only family: negative control;
   - copy / attach-read-out constructions: whether they enlarge the family in a principled way.
4. Demand representation independence: if two finite OI realizations give the same completion state body, the
   candidate family must not depend on which realization was chosen. Copy naturality / composition may matter here —
   but only if the derivation actually needs them.
5. Identify the minimal closure operation. The likely outcome may be a closure of operationally generated effects under
   operations already justified by OI (limits, convex combinations, pullback under certified automorphisms,
   conditioning, copy/read-out). Each closure operation needs provenance; none may be inserted because it gives the
   desired theorem.
6. Finish with a trichotomy for each candidate: DERIVED from OI; INSUFFICIENT with an explicit countermodel; or BLOCKED
   on one precisely named missing theorem.

Most valuable possible result: E_OI := closure of {operationally generated response/readout effects}, with arguments
that it is canonical and that every relative-boundary point has a proper supporting effect in E_OI (discharging P2/O1;
O2–O5 then follow by B7/B8). If every natural candidate fails on the SIC ball or depends on a chosen finite realization,
that is also a major result: the missing principle is an effect-generation/completion theorem, not geometry.

## Research limits (frozen; as for Thread F)
1. Read-only against certified main = 6d0abf6ba5467e0b0c1f5437a03ae6bd22f9c28a.
2. Inspect, compute and draft only.
3. No branches, PRs, freezes, round records, receipts, ROADMAP edits or manuscript edits.
4. No new axiom or premise may be introduced to make a proof go through.
5. If a purported implication fails, produce the smallest explicit countermodel and identify the missing premise.
6. Separate logical necessity from later reconstruction convenience.
7. Do not promote written arguments to kernel results: "proved" requires an exact kernel identifier; a written
   argument is labelled as such.
8. Do not assume K∞-R.

## Evidence levels
kernel (landed Lean identifier) / exact computation (script in threads/G/, exact arithmetic) / written argument /
citation. They do not substitute for one another.

## Disposition (owner, 2026-10-01)
Conclusion recorded from F+G, not frozen as a premise: P2 factors as OI completion + effect generation/transport +
boundary covering + limit closure where required ⇒ sharp-enough effects for NB-1. Ordinary SEC is too weak:
`lorentz_of_effects` (NGB:105) consumes the sharp directional effects (1 + b·r)/2, so P2 must deliver the right
sharpness/normalization. D3 (`ClosureAvail`) is NOT adopted; it stays separately named until the generation mechanism
is understood. Next: Thread H, the minimal field-neutral vocabulary for Naimark-style transport.
