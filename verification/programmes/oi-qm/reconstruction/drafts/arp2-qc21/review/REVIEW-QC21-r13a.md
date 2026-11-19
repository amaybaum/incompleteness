# Confirming check: Q-C2-1 r13a (ARP-2-QC21)

**Verdict: ACCEPT, with one nit.**

**Inputs.** Read-only: preregistration `fefd3b6e…`, PLAN `d2c624b2…`, both verified and diffed against `r13/`.

**The diff contains only R13-B1 and R13-B2:**
- the status line;
- the feasibility statement;
- D19's new options and the `d ≤ 16` caveat;
- D21(b)'s S1 binding and D21(a)'s note;
- the `E`-binding sentence in *The objects* and in the note's list;
- PLAN §21.

**Both are fixed, correctly and neutrally.**

- **D19 (0)(c), extreme rays.** It is correct. The facets of `cone{a_p}` depend only on its extreme rays, and each
  removed row is certified as a nonnegative combination of retained rows, so the cone and every steps-2–4 decision are
  unchanged. A linear model reproduces a removed row as a combination of retained ones. It is presented as unknown
  before `F`, with the `d ≤ 16` caveat.
- **D19 (i)(d), covering by sub-fragments.** It is correct and labelled one-sided. A noncontextual model of the whole
  restricts to each sub-fragment with the same `Acc`, so an infeasible sub-fragment implies B-P is contextual, and an
  all-feasible covering gives "not decided".
- **D19 (i)(e), a different facet enumeration.** It is correctly marked as a D10 method change needing its own review.
- **D21(b)'s S1 binding.** It is correct and mirrors ARP-1's verdict: a frozen `actions/artifacts/{DEC}/zip` template,
  in-memory `zipfile.ZipFile` and `io.BytesIO` only, and a canonical-JSON comparison without `dispatch_sha`, or an
  equivalent exact comparison with its own control. Under D21(a), the text states that S1's step conclusions suffice.

None of the options is recommended, and each states its Level and VOID consequences.

**Nit.** Under D19 (i)(d), name the token that "not decided" maps to: for example B-VOID, or a new B-NOT-DECIDED
recorded beside B-VOID's rules. That way `decide-b` and `decide-levels` stay mechanical, and no Level 2 is awarded on it.

**Remaining before `F`** (unchanged from the r13 review, items 3–5):
- the owner's D19–D23 decisions, recorded with author and time;
- the scripts brought to r13/r13a, then the self-tests and the design run;
- the `PENDING` fields;
- D9(a)'s landings;
- the confirmation run and the gate tests;
- the owner's freeze commitments;
- the round PR, and precondition 5's review of the filled plane and the scripts' blobs;
- the `F` dispatch and the designation request.
