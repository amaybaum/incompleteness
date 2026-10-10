# Owner's note on the discrete extension (received 2026-10-10, about 14:50Z, while Y and Z run; audit input)

Placed under `pt/audit/` (excluded from the threads' sweeps). Not transmitted to the threads: the owner leaves the
frozen protocol, the pre-audit record and the thread scopes unchanged. To be preserved in the final audit: the
reachability needed for cone uniqueness uses the connected subgroup `Ad{U⊗P₊ + V⊗P₋ : U, V ∈ SU(2)}` alone; the
discrete element CNOT contributes is part of the exact group census, not a premise of the proof. Exact confirmation
of the identities: `qex_owner_note6.py` (this directory).

----- BEGIN VERBATIM -----
This is a sound point to hold Stage 4. The independently replayed 15/15 pre-audit, fixed before Y or Z reports, provides a useful reference against which to assess both threads without adjusting the criteria afterward.

There is one mathematical precision worth preserving in the final audit.

### The discrete extension is not needed for uniqueness

Writing , the CNOT decomposition admits the factorization

\\mathrm{CNOT}
=
\\underbrace{(I\\otimes P_+ + iZ\\otimes P_-)}_{\\in K}
\\underbrace{(I\\otimes P_+ - iI\\otimes P_-)}_{\\text{discrete factor}}.

The second factor acts, up to global phase, as a target . Its square belongs to , so the generated group's quotient by is .

Crucially, the connected subgroup alone already has the pure-state reachability needed for the cone-uniqueness argument. The discrete extension is part of the exact group census, but not an additional premise required for that proof.

That distinction may help Y establish a cleaner minimal-sufficiency result.

### What remains genuinely unresolved

The most consequential question is now whether the required conditional rotations on the composite can be derived from embedded-observer principles, rather than imported as an operational assumption.

Y's positive theorem and Z's weaker-premise countermodels should be evaluated independently. A uniqueness proof establishes sufficiency; a countermodel for each relevant weakening is needed to support minimality.

I would leave the frozen protocol, pre-audit, and thread scopes unchanged. The present evidence supports the leading exclusion mechanism, but the observer-native provenance and minimality claims remain open until the two audits are complete.
----- END VERBATIM -----
