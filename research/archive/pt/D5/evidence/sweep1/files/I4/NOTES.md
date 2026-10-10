# pt/I4/NOTES.md — running record (thread I4, stage 6, Q-EX-FULL; inventory: generalization and completion)

Clock times are UTC from `date -u`. Read-only on the corpus; writes only inside `pt/I4/`.

## N0 — start (16:52:52Z)
- Directory `pt/I4/` absent at launch; created; `.start_marker` written first (16:52:52Z), then the four start
  checks appended (manifests 6/6 + ns OK; base HEAD 9f9f8257…, porcelain empty, no bytecode; ten protocol files at the
  expected prefixes, sidecars OK; `pt/` top-level listing with mtimes, 64 names). All passed.

## N1 — governing texts read (by 16:54:33Z)
- `PROTOCOL-STAGE6.md` (b277b7c1…) in full: record schema; censuses (a)/(b)/(c); I4 scope; deliverables.
- `PROTOCOL-STAGE5.md` (9e01f098…), `PROTOCOL-STAGE5-AMENDMENT-1.md` (1f639115…), `PROTOCOL-STAGE4.md`
  (d3da2811…), `PROTOCOL-STAGE3.md` (1a649168…), `PROTOCOL.md` (239dc123…), `INTEGRATION-NOTE-STAGE4.md`,
  `INTEGRATION-NOTE-STAGE3.md`; `pt/base/AGENTS.md` (959c4333…, byte-identical to the working copy's AGENTS.md).
- Not read (protocol exclusions): pt/I1, pt/I2, pt/I3, pt/D5, pt/C5, pt/audit/stage{3,4}-inputs/OWNER-*,
  pt/audit/stage5-inputs, pt/audit/stage6-inputs, pt/audit/reviews, pt/audit/aborted-launches.
- Scope check at L: all listed modules present except `OIHierarchy`, which is a namespace, not a file:
  `namespace OIHierarchy` is CompletedOI.lean:77; `namespace OIHierarchyGeneral` is CarrierGeneralOIPlus.lean:50.
  ImplementationLocality.lean's namespace is `InterventionLocality` (:95); EmbeddedObservation.lean's is
  `PrimitiveSource` (:74); MicroscopicReversibility.lean's is `MicroReversibility` (:67).
  "Related passive modules": PassiveIndependence.lean (361 lines), PassiveQuotient.lean (675) beside
  PassiveObservation.lean (365).
- Plan (depth-first, per the launch order): kernel census script first (coverage control (a)); then
  ReferenceExtension, SpectatorBridge, ImplementationLocality, StructuralClosure, LiftAudit; then the OI⁺
  characterizations (GeneralCarrier, CompletedOI, CarrierGeneralOIPlus) and independence theorems; then the
  substratum-source chain; then typed and quasilocal completions; Kₙ census; roadmap census; manuscript cross-refs.
