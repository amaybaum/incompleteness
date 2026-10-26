# ħ framing and the θ₀ match: audit before correction

The owner directed this follow-up to #937 on 2026-10-26: "Correct the remaining 'ħ is derived' claims to distinguish
genuine derivations from calibration or consistency relations. Reconcile θ₀ against one authoritative definition."

`AUDIT.md` verifies each site at `main` `c967d6a9` before any edit. For every hit it gives the exact text, the corpus
line supporting or contradicting it, the class (OVERSTATED, INCORRECT, CORRECT or CONTEXT-OK), a minimal replacement
and the FULL mirror line, with the decisions it leaves to the owner.

`scripts/` holds the auditor's checks: `koide_theta0.py` and `koide_closure.py` recompute θ₀ and the lepton mass chain
from the PDG 2024 masses in high-precision arithmetic, with controls; their outputs are beside them. `kwic.py`,
`sentence.py` and `mirror.py` are the search helpers, run over a `git archive` of `c967d6a9`.

No manuscript text is changed yet. The audit is reviewed independently before the owner decides and any edit is made.
