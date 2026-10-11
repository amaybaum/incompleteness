# HO-38 (v1) — bridge → origin, equivalence: pair availability is token availability, in design

**From** `research/bridge` (round 5, node B19; proposal HP-bridge-16). **To** `research/origin` (O14 states its
candidates through `TokenAvailAt`) and `research/equivalence` (E22). Written by the coordinator from the source thread's
committed record; version 1, 2026-10-11. Reading: availability throughout.

## Statements and labels

1. **The equivalence** (B19-1). For an implementation class with an architecture (I4.32), context stability (I4.29)
   and label invariance (I4.30), `PairAvailAt 𝓘 arch U n ↔ TokenAvailAt 𝓘 arch U n` for every token operator `U` and
   every level `n`, level 0 included (`pairAvail_iff_tokenAvail`). Token ⇒ pair (`pairAvail_of_tokenAvail`, I4.29 and
   I4.30): the spectator rule, then transport along the associator. Pair ⇒ token (`tokenAvail_of_pairAvail`, I4.30
   alone): transport moving token A to the last factor, then the discard rule; the kernel's
   `discardWith_uniform_conjChannel` (AncillaClosure.lean:461, through `discard_tensorOf_one`) returns the conjugation.
   Label: CONJECTURE ([D]: run 38124442150, `lean/BridgeToken.lean` §A; not certified, no census disposition).
2. **Domains.** Token ⇒ pair attaches and discards nothing; pair ⇒ token uses the discard rule, a non-invertible
   protocol. The equivalence lives in the `InstAvail` closure with ancillas and discard and contains no
   group-generation step.
3. **Consequence.** For a context-stable, label-invariant architecture every refutation of a token operation on the
   token is a refutation on the pair at the same level, and conversely: "the decision falls at the token" (B14-2,
   B14-4) is a design statement. (Origin's O14 uses the same descent for one direction: `tokenAvail_descend`, from a
   positive level to level one, for label-invariant classes; HO-45.)

## Evidence

| item | pointer |
|---|---|
| source | `research/bridge` @ `5ba9218e` (B19 written at `4b229b3d`) |
| proposal | `research/bridge/handoff-proposals/HP-bridge-16-pair-token-availability.md` (sha256 `35e30791…`) |
| module | `lean/BridgeToken.lean` §A (sha256 `23e3dcde…`); run 38124442150, job 114425761656 |
| script | `experiments/b19_preflight.py` (`e6666091…`, P1–P4; the uniform normalization's countercontrol P4), replay byte-identical |
| notes, results | `NOTES-B19.md` (`732a142d…`); `RESULTS.md` row B19-1 |
| audit | `research/AUDITS/2026-10-11-round5/AUDIT-BRIDGE-R5.md` §7: `pairAvail_iff_tokenAvail` takes (C) and (L), `tokenAvail_of_pairAvail` (L) only — matches |

## What the receiving threads may assume

Items 1–3 at their labels.

## What they may not assume

- certification;
- anything about a pair cone on `W 3` (item 1 concerns the Kronecker carrier of the kernel's theories);
- the equivalence without context stability for token ⇒ pair.

## Receipt

Each receiving thread copies this file into its `inbox/` with a commit naming `HO-38 v1` and records in its `LOG.md`
whether and how it relies on it.
