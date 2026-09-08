# Recurrence-horizon scaling and accessibility audit — preregistration

Base: `main` at `7f4e95a490124fb5f147db85ea3d192ba32a898b` (post-PR #545).

Backlog item #63. This round asks whether the controlling readback-return horizon of PR #543 can grow
without bound while the tightness property is preserved, or whether tight realizations have a
bounded horizon. It is the last unresolved physical question in Arc A of `OI-QM-RESEARCH-PROGRAMME.md`.

No candidate family, realization, permutation, prior, or bound has been searched for, inspected,
simulated, or constructed before this preregistration. The prior-expectation disclosure below records an
expectation held before execution, and is not evidence.

## Fixed inherited layer

Use the merged layers of PR #542 and PR #543 without modification.

- finite visible carrier `V`, finite hidden carrier `H`, deterministic reversible `phi : V x H ≃ V x H`;
- one fixed hidden prior `mu_H`, common to every visible root;
- rooted visible maps `Gamma_t(a,j) = P(X_t = j | X_0 = a)`, row-stochastic by `rootedMap_isRowStochastic`;
- the frozen realization-level `CausalReadback` parent with clauses W, S, R(1), R(2);
- `PDivisible`, `PIndivisibleWithin`, `C4e`, `C4r` as defined in `OIBridge/CausalReadback.lean`;
- the merged bridge `c4r_implies_pIndivisible`;
- the merged horizon route `c4r_of_identity_return_of_overlap` and
  `pIndivisible_of_identity_return_of_overlap` in `OIBridge/RecurrenceHorizon.lean`.

The controlling horizon is the one frozen by `RECURRENCE-TIGHTNESS-AUDIT-AMENDMENT-1.md`:

`N_CR := min { n > 0 : Gamma_n = I and there exists a storage witness time s with s < n }`.

`N_CR` is not `ord(phi)` and not the first visible return from time zero. A candidate that reports a
snapback time must prove that time is its `N_CR`, exactly as PR #543 required.

Call a realization **tight at `N_CR`** when it is parent-positive, `PDivisibleWithin(K)` holds for
every `K < N_CR`, and `PDivisibleWithin(N_CR)` fails. PR #543 exhibits one tight realization, with
`N_CR = 3`, and makes no claim about any other value.

## The question

Can `N_CR` be made arbitrarily large while tightness is preserved, or is the horizon of tight
realizations bounded?

## Target independence, frozen before execution

The two targets below are attempted **independently**. Neither is conditional on the other failing,
and they are not assumed to be exhaustive or mutually exclusive. Execution may not defer one because
the other looks likely, and may not treat progress on one as evidence about the other.

### S1 — unbounded tight construction

Determine whether there exists a family of parent-positive finite reversible realizations
`{R_k}` with

`N_CR(R_k) -> infinity`,

each `R_k` tight at its own `N_CR(R_k)`.

A family must be exhibited uniformly enough that the tightness properties are verified for every
member, not checked at finitely many values and extrapolated. A finite table of tight realizations
at increasing horizons is **not** an unbounded family; it is a partial result and must be reported
as one, with the exact horizons reached.

### S2 — horizon bound on tight realizations

The negative target is **not** that an obstruction is forced strictly before `N_CR` in every
realization. That statement is already false: PR #543's witness is parent-positive with `N_CR = 3`
and is `PDivisibleWithin(K)` for every `K < 3`, so no such universal earlier obstruction exists. It
is exactly what #543 proved cannot hold, and it may not be preregistered as a target.

The correct negation of S1 is a **bound on the horizon of tight realizations**:

`exists B, for all R: tight(R) -> N_CR(R) <= B`.

Equivalently: once `N_CR(R) > B`, some `K < N_CR(R)` must already fail `PDivisibleWithin(K)`, so `R`
is not tight. This negates unbounded tight scaling while remaining consistent with the known
`N_CR = 3` witness, which simply satisfies `3 <= B`.

Three strengths are distinguished, and must not be conflated.

**S2-a — absolute bound.** `B` is a constant, independent of every parameter of the realization.
This refutes S1 outright.

**S2-b — class-restricted bound.** `exists B, for all R in C: tight(R) -> N_CR(R) <= B`, for a named
structural class `C`. A legitimate positive result on this side, reported at exactly the scope
proved: neither promoted to an absolute bound nor demoted to unresolved because it is not universal.
State `C` explicitly, and whether the frozen physical realization is known to lie in it, known not
to, or not determined.

It refutes S1 only together with a **coverage theorem**, quantified over families rather than over
realizations:

`for all (R_k): [ (for all k, tight(R_k)) and N_CR(R_k) -> infinity ]`
`  -> exists k_0, for all k >= k_0, R_k in C`.

The stronger form, `for all k, R_k in C`, is also admissible. Either version, together with the
uniform bound on `C`, refutes S1.

There is no predicate "a realization admitting an unbounded family": admitting is a property of a
family, not of any single realization, and the coverage statement must be written over families to
mean anything.

S1 is existential — it asserts that some unbounded tight family exists — so its negation is
universal over all such families. Showing that one attempted family lies in `C` kills that candidate
and nothing more; it says nothing about families outside `C`. Coverage is a separate theorem, to be
stated and proved, never inferred from the failure of the families actually tried.

**S2-c — parameter-dependent bound.** `N_CR(R) <= f(|V|, |H|)` or similar, for tight `R`. This
does **not** by itself refute S1. S1 places no bound on the carriers along the family, so a bound
depending on `|V|` or `|H|` is consistent with `N_CR -> infinity`.

A parameter-dependent bound refutes S1 only together with a **uniform carrier bound**, quantified
over families in the same shape as the S2-b coverage theorem:

`for all (R_k): [ (for all k, tight(R_k)) and N_CR(R_k) -> infinity ]`
`  -> exists k_0, exists M, for all k >= k_0, |V_k| <= M and |H_k| <= M`.

The eventual form suffices; the stronger `for all k` version is also admissible. Note that this is
strictly stronger than saying the carriers cannot *grow*: an unbounded but non-monotone carrier
sequence has no growth in the naive sense and would slip through that phrasing, while it is excluded
here. As with coverage, the statement is about every putative S1 family, not about the families
actually attempted, and is itself a result to be stated and proved.

Execution must state which of S2-a, S2-b, S2-c any proved bound is, and must state explicitly
whether it refutes S1.

### Refutation standard for S1

S1 is **refuted** only by an actual theorem excluding unbounded tight families: S2-a, or S2-b with
a proved coverage theorem, or S2-c with a proved uniform carrier bound. Because S1 is existential,
each of these must quantify over every potential witness; ruling out the families actually
attempted refutes nothing.

Failure to construct such a family does not refute S1. Neither does exhaustive search over any
finite range of horizons, carriers, or priors: finite exhaustion bounds nothing beyond the range
exhausted, and must be reported as the finite statement it is. A failed construction is O-5.

## The mixed outcome is admissible and is not a contradiction

It may turn out that unbounded tight families exist in general **while** a strong horizon
bound holds under an additional physically motivated structural condition.

That is a scientifically important mixed outcome, not an inconsistency: the two statements quantify
over different classes. Execution must be able to report both, and must not suppress or weaken
either to force a single headline. Where both hold, the report states the general construction, the
restricted bound, the condition separating them, and whether that condition has independent physical
motivation.

## Two-sided interpretation guard, frozen before execution

Both directions are over-readable, and the negative direction is the easier one to over-read because
it sounds like the stronger outcome for the programme. Neither reading is admissible.

**A positive scaling result** shows that arbitrarily delayed guaranteed obstruction is
**mathematically possible**. It does **not** establish that physical recurrence or readback-return
times are inaccessible. Exhibiting realizations with large `N_CR` says nothing about the `N_CR` of
any physical realization.

**A horizon-bound result** caps `N_CR` **only over the class the theorem quantifies over**, and only
at the strength proved (S2-a, S2-b or S2-c). It does **not** establish physical accessibility
unless both of the following are separately established: the bound is quantitative, and the
physical realization is independently shown to satisfy the class condition. A qualitative bound, or
a quantitative bound over a class the physical realization is not known to inhabit, supports no
accessibility claim.

Neither outcome, alone or together, licenses any statement about accessible quantum-like
nonclassicality. Reporting rule 2 of the programme map remains binding.

## Prior expectation disclosure

Before execution, and without running any search, probe, or candidate construction, the drafting
expectation is that **S1 may be feasible**: the hidden-state count and the prior weights appear to
supply substantial freedom relative to the `N_CR - 1` monotonicity constraints a tight family
imposes, so the system looks underdetermined as the horizon grows.

This is recorded because this programme records expectations in the freeze rather than after it. It
carries the following restrictions:

- no search, probe, candidate realization, or construction has been run, inspected or simulated;
- an expectation is **not** evidence, and no execution step may cite it as support;
- it may **not** weaken, defer, or narrow the independent S2 attempt, which is to be pursued as
  though the expectation had not been formed;
- if S1 succeeds, the report must not present the expectation as a prediction confirmed; if S1
  fails, the report must state that plainly.

## Outcome taxonomy

The round must report exactly one headline class, and must not silently collapse any into another.

**O-1 — unbounded tight construction proved.** A family with `N_CR -> infinity`, each member tight,
is exhibited and verified uniformly.

**O-2 — absolute horizon bound proved (S2-a).** A constant `B`, independent of every parameter of
the realization, with `tight(R) -> N_CR(R) <= B` for all `R`. This refutes S1.

**O-3 — class-restricted or parameter-dependent bound proved (S2-b or S2-c).** A horizon bound is
proved for a named structural class, or as a function of the carriers, without an absolute bound.
Reported at exactly the scope proved, stating which of S2-b or S2-c it is and whether it refutes S1
— which for S2-b requires a proved coverage theorem, and for S2-c a proved uniform carrier bound.
Applies when no unbounded construction is also proved; if one is, the outcome is O-4.

**O-4 — mixed.** An unbounded tight construction (S1) is proved **together with** any non-refuting
bound: a class-restricted bound (S2-b) without coverage, a parameter-dependent bound (S2-c) without
a uniform carrier bound, or both.

This is the resolving class whenever O-1 and O-3 would each otherwise apply, and it takes precedence
over both, so exactly one headline class is reported. It is not a contradiction: S1 and a
non-refuting bound quantify over different classes, and the report states the general construction,
each restricted bound, the condition separating them, and whether that condition has independent
physical motivation.

**O-5 — unresolved.** Neither direction is settled. The construction or formalization fails and no
impossibility theorem is proved. This is **Open** in the sense of §6 of the programme map: it is
recorded as unresolved, never as independence, never as impossibility, and never as evidence that
the other direction holds. Tooling and construction failure must be reported separately from
mathematical failure, with the exact blocker named.

A finite set of tight realizations at increasing horizons, without a uniform family, is O-5 with the
horizons reached recorded — not O-1.

## Mandatory controls

1. **#543 recovery.** Any general construction must reproduce a tight realization at `N_CR = 3`, or
   state explicitly why its family starts above that horizon.
2. **Horizon verification per member.** For every candidate, verify `Gamma_(N_CR) = I`, a storage
   witness at some `s < N_CR`, and that no earlier `n < N_CR` both has `Gamma_n = I` and lies after a
   storage witness — so the reported horizon really is `N_CR`.
3. **Tightness verification per member.** Verify `PDivisibleWithin(K)` for every `K < N_CR`, over all
   pairs `s < t <= K`, not only the pairs from time zero.
4. **Parent verification per member.** Verify W, S, R(1) and R(2) on the declared realization; a
   family that loses parent-positivity as the horizon grows is not a tight family.
5. **Negative control.** A realization that is P-indivisible below its horizon must be rejected by
   the same checker, so the verification cannot pass vacuously.

## Evidence hierarchy

Per reporting rule 9 of the programme map, every reported result carries its evidence type.

1. Mathlib/Lean theorem at the existing `RootedRealization`, `C4r` and `PDivisibleWithin` interfaces;
2. exact finite arithmetic probes for explicit constructions and controls;
3. prose only for interpretation and theorem-boundary statements.

A uniform family claim (O-1) is a universal statement and is preferred as a kernel theorem; if it is
carried by prose plus finitely many exact instances, that must be stated in the same place the
result is reported. A formalization failure is reported separately from a mathematical failure and
is never classified as a mathematical negative.

## Non-doings

This preregistration does not:

- assert that S1 succeeds or that S2 succeeds;
- treat the two targets as exhaustive or mutually exclusive;
- define any new predicate, horizon, or readback condition;
- modify `RecurrenceHorizon.lean`, `CausalReadback.lean`, or any frozen audit or result note;
- edit the manuscript, book, README, census, bibliography or release record;
- claim anything about physical accessibility or inaccessibility of any horizon;
- claim that recurrence-scale behaviour is or is not accessible quantum-like nonclassicality;
- apply Barandes, or touch the `C_OI` classification of Arc B;
- reopen #542's accessible-window result or #543's tightness result.

## Execution discipline

- Freeze this preregistration by commit SHA and blob hash before any proof search, candidate
  construction, brute-force search, or new simulation.
- Once frozen, do not rewrite this file. Corrections are append-only preregistration amendments,
  each committed and frozen before the execution it affects.
- One PR for this research round.
- If rebasing becomes unavoidable, verify by blob hash; blob identity is authoritative.
- Final approval must name the exact completed PR head SHA after all required CI checks are green.

## Allowed final classifications

The final report must state separately:

1. S1: proved / refuted / partial / not settled, with the horizons actually reached, and — if
   refuted — the theorem that refutes it, never a failed search or a finite exhaustion;
2. S2: S2-a absolute bound / S2-b class-restricted / S2-c parameter-dependent / not settled, with
   `B` and any class or parameter dependence named, and an explicit statement of whether the bound
   refutes S1;
3. headline outcome: O-1 / O-2 / O-3 / O-4 / O-5;
4. the two-sided interpretation, stating explicitly what the result does not establish about
   physical accessibility in either direction;
5. evidence type for each reported result;
6. whether Arc A can now close, and whether any manuscript wording is demonstrably too strong —
   without editing it unless separately authorized.

Status: **preregistered; no proof, construction, search or probe execution has begun.**
