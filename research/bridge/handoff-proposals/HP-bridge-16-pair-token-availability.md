# HP-bridge-16 — pair availability is token availability, in design

From `research/bridge`, node B19 (round 5). Proposed for the origin thread (O14 states its candidates through
`TokenAvailAt`) and the equivalence thread (E22). The coordinator routes.

## Statements and labels

Every statement is an availability statement.

1. **The equivalence** (B19-1). For an implementation class with an architecture (I4.32), context stability (I4.29) and
   label invariance (I4.30), `PairAvailAt 𝓘 arch U n ↔ TokenAvailAt 𝓘 arch U n` for every token operator `U` and every
   level `n`, level 0 included (`pairAvail_iff_tokenAvail`). token ⇒ pair (`pairAvail_of_tokenAvail`, I4.29 and I4.30):
   the spectator rule, then the transport rule along the associator. pair ⇒ token (`tokenAvail_of_pairAvail`, I4.30
   alone): the transport rule moving token A to the last factor, then the discard rule; the kernel's
   `discardWith_uniform_conjChannel` (through `discard_tensorOf_one`) returns the conjugation. Label: CONJECTURE ([D]:
   run 38124442150, `lean/BridgeToken.lean` §A; not certified, no census disposition).
2. **Domains.** token ⇒ pair attaches and discards nothing; pair ⇒ token uses the discard rule, a non-invertible
   protocol; the equivalence lives in the InstAvail closure with ancillas and discard, and contains no group-generation
   step.
3. **Consequence.** For a context-stable, label-invariant architecture every refutation of a token operation on the
   token is a refutation on the pair at the same level, and conversely: "the decision falls at the token" (B14-2,
   B14-4) is a design statement.

## Evidence

| item | pointer |
|---|---|
| module | `lean/BridgeToken.lean` §A (sha256 `23e3dcde…`); run 38124442150, job 114425761656 |
| script | `experiments/b19_preflight.py` P1–P4 (the uniform normalization's countercontrol P4), replay byte-identical |
| notes, results | `NOTES-B19.md`; `RESULTS.md` row B19-1 |

## What the recipient may assume

Items 1–3 at their labels.

## What the recipient may not assume

- certification;
- anything about a pair cone on `W 3` (item 1 concerns the Kronecker carrier of the kernel's theories);
- the equivalence without context stability for token ⇒ pair.
