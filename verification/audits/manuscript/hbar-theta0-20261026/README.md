# ħ framing and the θ₀ match: audit before correction

The owner directed this follow-up to #937 on 2026-10-26: "Correct the remaining 'ħ is derived' claims to distinguish
genuine derivations from calibration or consistency relations. Reconcile θ₀ against one authoritative definition."

`AUDIT.md` verifies each site at `main` `c967d6a9` before any edit. For every hit it gives the exact text, the corpus
line supporting or contradicting it, the class (OVERSTATED, INCORRECT, CORRECT or CONTEXT-OK), a minimal replacement
and the FULL mirror line, with the decisions it leaves to the owner.

`scripts/` holds the auditor's checks: `koide_theta0.py` and `koide_closure.py` recompute θ₀ and the lepton mass chain
from the PDG 2024 masses in high-precision arithmetic, with controls; their outputs are beside them. `kwic.py`,
`sentence.py` and `mirror.py` are the search helpers, run over a `git archive` of `c967d6a9`.

The audit was reviewed independently before the owner decided and any edit was made.

`review/REVIEW.md` is the independent review of the audit (ACCEPT WITH CHANGES): the ħ account and the θ₀ figures are confirmed, six missed sites are added, one audit claim (the 105.74 MeV figure) is corrected, and each owner decision O1–O7 carries a recommendation. `review/mine/` holds the reviewer's own θ₀ computation.

`decisions/DECISIONS.md` gives the owner decisions O1–O7 in exact form: for each option, every site with its old and new text (FULL mirrors included), what it changes in any count, bound or classification, and a recommendation; and the complete set of corrections that need no decision. All text is checked against `main` `b64919cd`. `decisions/entries.py` holds the exact edits, `gen.py` the checks and `sim.py` the simulation that applied the recommended set to a copy of `main`.

`CHANGE-NOTE.md` records the applied change: the owner's decisions of 2026-10-26 verbatim, every site old → new, the adjustments made for the owner's two qualifications, two residue sites found by the re-grep, the `SUBSTRATUM:T-23` ledger re-affirmation, the rebuilt artifacts and the check results.
