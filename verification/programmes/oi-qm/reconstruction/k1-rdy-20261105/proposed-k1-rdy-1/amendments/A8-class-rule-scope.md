# A8. Scope of the P1 class rule's union clause

**Governs:** base lines 159–162, the clause from "If every member row is positive" to "if this is not decided".

**Addition.** "Every weighting supported on `C`" reads as every weighting whose positive entries are exactly the cycles
of `C`. Proved in `verification/programmes/oi-qm/reconstruction/k1-rdy-pref-proofs-20261105/PROOFS.md` §6:

- at this instance the clause is not reached in any branch, because the member row of `δ_0` is not a positive in B-pl,
  B-eq or B-ct (CR-6); the class token is decided in every branch by line 158's first sentence, as line 236 states;
- where the clause is reached, its positive outcome implies that every member of `𝓘` has a sharp `w` at which `NB` holds
  (CR-3), and its ABSENT outcome holds exactly when some member of `𝓘` has no sharp `w` (CR-4);
- its BLIND outcome does not by itself establish that some member of `𝓘` fails `NB` at every sharp `w` (CR-5).

No token, gate or order changes.
