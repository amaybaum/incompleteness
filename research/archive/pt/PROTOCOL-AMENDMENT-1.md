# PT protocol — amendment 1 (owner's direction after launch; append-only)

`PROTOCOL.md` (sha256 `239dc123b07cb83f354a0f9def3cc39f5fd025fb2f6b4f3c4ba3d3e0ddfa9b23`) is unchanged. This amendment
adds to it; where the two differ, this amendment governs.

**Owner's direction (verbatim).**
> 1. Thread A must separate two achievements. Constructing a closed completion of a pair system is one achievement.
> Proving that this completion corresponds to the required state space in `W 3` is another. The first does not
> automatically establish `hcl` for the cone used by the four-copy theorem. Any use of local tomography must remain
> explicit.
>
> 2. Threads B and C must establish sufficiency, not just eliminate counterexamples. Finding a weaker gate condition
> that distinguishes `M_max` from `M_D` is useful, but it must also support the required proof steps. Likewise,
> excluding `M_tok` is necessary for a proposed four-copy composition principle, but does not by itself derive FCC.
>
> 3. Opening draft PRs is a separate operational step. Since creating a PR can trigger CI automatically, please hold
> PR creation until that consequence is explicitly authorized. The four isolated scratchpad research threads can
> continue without PRs or CI.

> "I particularly agree with the three-outcome rule: a counterexample or a precisely identified gap is just as valuable
> as a successful derivation. We should not force a positive result."

## What this changes for the threads

- **Thread A.** `RESULT.md` reports two separate verdicts:
  - **(A-i) completion:** whether a pair system has a completion with a closed body — which construction, closed in
    which space, under which premises;
  - **(A-ii) correspondence:** whether that completion corresponds to the state space the theorem uses, the cone
    `K_p ⊆ W 3` — every use of local tomography (K2) named explicitly as an assumption.

  `hcl` for the theorem's `K_p` is claimed only if (A-ii) is established. (A-i) alone is reported as (A-i), not as
  `hcl`.
- **Thread B.** A clause that holds in `M_max` and fails in `M_D` is reported as a separation, not as sufficiency.
  Sufficiency means the clause supports every proof step that consumed `hgate`/`hinv` (`bell_mem`, `link_mem`,
  Lemma R, `bell_mem_dual`, `parity_witnesses`, and any other use on the path), step by step, with written arguments
  and exact checks (UNBUILT Lean where useful) — or else an exact countermodel to the theorem with the weaker clause in
  place of `hgate`.
- **Thread C.** Excluding `M_tok` (and the other countermodels) is reported as necessary-condition evidence only. A
  principle derives FCC only with a derivation of FCC and the token clauses from it, with exact ingredients.
- **Thread D** (the coordinator applies the same standard): a proposed smallest assumption is reported as sufficient
  only with a derivation of the target (N-CLASS; each `hadm` clause) from it; agreement with the countermodels alone is
  reported as such.
- **Every thread:** the "0. Answer" section distinguishes, for every implication it states, **sufficiency proved**
  from **survives the countermodels**.
- **PRs and CI:** threads never open PRs or run CI (unchanged). The coordinator holds PR creation until it is
  explicitly authorized.

## The integration review (coordinator)

For each thread: the strongest result achieved; the certified assumptions it uses; the additional assumptions that
remain; whether those additions genuinely explain the desired property or merely restate it. Then the central
question, decisive for K2:

> "Can the observer-native framework actually construct a two-system composite with the properties quantum mechanics
> requires, or must some of those properties remain independent principles?"
