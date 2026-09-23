# Act 19 — the rigidity of the cross-time laws act 18 opened: CLOSURE WITHOUT A HEADLINE

**Act 19 terminates without a rigidity headline.** Its control plane was frozen and merged and
remains valid; an execution was run against it and is not certified. This note exists so the
repository carries a durable account of why there is a control plane in this directory and no
result note beside it.

**Nothing here says any mathematics is false.** The distinction the note keeps throughout is between
a statement being refuted and a statement being **uncertified by this round**. The conclusions named
below are the second. They may well be true; act 19 is not what establishes them.

---

## 1. What was valid

The control plane `preregistration.md` in this directory, blob
`8c828cab63ec2a09daf5c9b09dd4ab9924b0a057`, merged as
`84b469a8f78d538b204353e66c6066ab197d1a82`. That merge commit is act 19's mandated execution base
under `AGENTS.md` `§A.37`, and it placed the condition ladder `L0`–`L5` and the frozen quotient list
in certified history before any discriminating result existed. **The freeze is intact and is not
withdrawn by this closure.** It was consumed, never edited; its blob is unchanged on `main`.

The round was declared SEALING under the reserved tag `R7-OLR`, with the stem `_OLR_` and the module
`OIBridge/OrbitLawRigidity.lean`. **None of that formal state reached `main`.** No guard clause, no
Lean module, no census entry and no roadmap row was landed by act 19, and `R7-OLR` and `_OLR_` remain
free names outside this directory.

## 2. The execution, and where it stands

The execution branch `claude/act-19-execution` is preserved and is **not merged**. Four commits on it
matter to this closure:

| label | commit | what it is |
| --- | --- | --- |
| base | `84b469a8f78d538b204353e66c6066ab197d1a82` | the mandated base, on `main` |
| ladder commit | `ae983580a38dd416e8fb6a95795f1976eecabe62` | the ladder `L0`–`L5` stated, zero theorems, no candidate defined |
| the change | `52b64009419cc32c89dc1d37de183764b33476a1` | the `L4n` conjunct of `LadderConds` rewritten |
| discrimination commit | `5103154aeb754d4b83ea116f56a3d31fb8ab33b1` | the first theorem on the branch, the shared structural theorem in both forms |
| execution head | `1dd963ba4b64e791bddf6afc6c37fda29226e72b` | the head the execution offered for certification |

The ordering obligation the freeze imposes was honoured in every mechanical respect that an audit of
the branch can check. The chain is linear from the mandated base; no commit was amended, reset,
rebased or cherry-picked over; the ladder commit and its successor carry no theorem at all and no
candidate law is defined in any file before the discrimination commit; no commit message before that
point names a survivor; and every rung statement is byte-identical from the discrimination commit
through the execution head.

**One declaration changed between the ladder commit and the discrimination commit**, and that is
what closes the round.

## 3. The change at `52b64009`, and the adjudication

At the ladder commit, the naturality conjunct `L4n` was stated as ordinary equivariance: a lift `Ψ`
of the transition to dilations satisfying `Ψ (L * U) = L * Ψ U` for an in-fibre left move `L`, and
`Ψ (U * K) = Ψ U * K` for a weak gauge `K` at the anchor.

At `52b64009` it was restated as the existence, for each input, of **some** `L'` and **some** `K'` in
the same groups with `Ψ (L * U) = L' * Ψ U` and `Ψ (U * K) = Ψ U * K'`.

**That is not a restatement.** The first is the special case `L' = L`, `K' = K` of the second. What
the second says is that the output stays somewhere in the gauge orbit; what the freeze's `L4n` asks
is that the lift **commute with** two named transformation laws, and it says in terms that `L4n` is a
genuine strengthening of mere descent. The gap is sharpest on the right. Act 12's
`fibreGram_mul_weak_apply` says that a weak gauge with anchored phases `c` sends the fibre-Gram data
to `conj (c j) * G j k * c k` — a specific transformation with specific phases. An unrestricted `K'`
permits output phases other than `c`, and nothing in the rewritten conjunct requires them to be `c`,
or a fixed reindexing of `c`, or anything determined by the input at all. So the rewritten conjunct
does not encode the named transformation law commuting with the transition. It encodes orbit
preservation.

**The second ground is chronological and is independent of the first.** The execution disclosed,
unprompted, that between the ladder commit and the discrimination commit it had worked out by hand
that a carrier relabelling's natural representative-level lift is a reindexing rather than a left
multiplication, and that this reasoning is what motivated the change. That is **candidate-specific
information bearing on which laws survive**, arriving before the rung was rewritten and pointing in
exactly the direction the rewrite went. The ordering obligation fixes the ladder before knowledge of
which laws survive, not merely before a theorem appears in version control. A rung rewritten after
such knowledge does not acquire clean preregistered status from the fact that no theorem had yet been
committed. **The disclosure establishes the contamination rather than curing it**, and the round is
better for the disclosure having been made.

Either ground alone closes the round. Together they settle it: **`ae983580` is act 19's
uncontaminated ladder boundary, and `52b64009` is a post-ladder, candidate-informed weakening.**

## 4. What is uncertified, and what is not

**Uncertified by act 19:**

- **`L4n`.** Neither the strict form at the ladder commit nor the rewritten form at `52b64009` is
  established as the freeze's condition.
- **The carrier relabelling's survival through `L4n`**, and with it its survival through `L0`–`L4`.
- **The same-initial-orbit discriminating test at the full frozen ladder.** The construction the
  execution built is untouched as mathematics and stands as a conditional result at the lower rungs;
  what falls is its force at a ladder whose `L4n` is unsettled.
- **The wide-plurality headline over `L0`–`L4`.** It needs two inequivalent survivors, and one of the
  two is the candidate whose `L4n` qualification is uncertified.

**Not a defect, recorded so it is not relitigated:** the execution replaced the countercontrol's
predicted initial class with another member of the frozen witness supply, having certified in the
kernel that the predicted one provably cannot diverge under the freeze's own simultaneous
relabelling. The frozen target is existential over the initial orbit and the trajectories, and the
predicted witness is a prediction rather than a conjunct of the target. **Reporting that the
predicted witness failed and the existential target was witnessed differently is a legitimate
outcome**, and it is not an independent ordering failure. It cannot carry the discriminating test at
the full ladder while `L4n` is unsettled, but that is the consequence of §3 and not a fault of the
substitution.

**The lower-level proofs on the execution branch remain available as research material.** They are
not evidence for any later round, and no later round may cite them as settled. Anything a successor
wants from them it proves again under its own freeze.

## 5. What act 19 discovered, which is worth more than its headline would have been

The round exposed a **genuine ambiguity inside its own control plane**, and the ambiguity is
conceptual rather than clerical. The freeze predicts that the carrier relabelling has an obvious
representative-level lift and survives `L4n`, while its written `L4n` language says the lift commutes
with the two transformation laws. Those two sentences pull apart, and the execution ran into the gap
between them.

The phrase **"gauge-natural" was underspecified**, between at least three notions that a formalization
must choose among and that prose does not separate:

| notion | statement | what it asserts |
| --- | --- | --- |
| strict equivariance | `Ψ (g * U) = g * Ψ U` | the lift commutes with each gauge element itself |
| twisted equivariance | `Ψ (g * U) = α g * Ψ U`, for one fixed preregistered `α` | the lift commutes up to a fixed induced map on the group |
| orbit preservation | `Ψ (g * U) = g' * Ψ U`, for some `g'` | the output stays in the orbit, with nothing fixing which element |

The third is what `52b64009` states, and it should not be called commutation. The scientifically
interesting question — which act 19 could not settle, because settling it during execution is exactly
what the ordering obligation forbids — is whether the freeze intended the first or the second.

**That question belongs to a later round with its own freeze**, and this closure neither answers it
nor prejudges it. The observation to carry forward is that a condition asking one object to respect
another's symmetry is not fully stated until the respecting is pinned to a particular map, and that
the difference between the three rows above is the difference between a rigidity verdict that means
something and one that does not.

## 6. Status

Act 19 is closed. It has a valid control plane, an uncertified execution preserved and unmerged, and
no rigidity headline. The `P0` row is unchanged: act 19 moved nothing on it, and the closure moves
nothing on it either. No condition of the ladder is withdrawn, no candidate is adjudicated, and no
equivalence is added or widened by this note.
