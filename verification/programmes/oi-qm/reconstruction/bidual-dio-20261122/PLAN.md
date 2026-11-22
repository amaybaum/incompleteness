# BIDUAL-DIO: restrictions of the state-space typing (F-S) and DIO-type (preregistration)

**WIP / UNVERIFIED. Paper-only research.** This plan is committed before the research record
(`NOTE.md`). It adopts no premise, edits no manuscript, Lean module or reviewed record, runs no
computation and changes no status. No merge is authorized.

- **Authorization.** Owner decision, `amaybaum`, #1169 c.7079945577 (2026-11-22T13:37:40Z), the
  "Quantum emergence (#1509)" item: "does a physically motivated restriction of (F-S), such as
  covariance or a single global slice order, restore DIO, so that the BIDUAL-REL counterexample
  does not survive restrictions motivated by OI's dynamics?" Required there: prove whether each
  restriction is sufficient to restore DIO; determine whether the restriction follows from OI or
  is an additional assumption; distinguish normal-state restrictions from constraints on
  slice-order selection; keep mathematical non-DIO existence distinct from physically realizable
  non-DIO behaviour. Stop condition there: a proof, a counterexample, or a precisely identified
  missing premise; no extension into new quantum-mechanical constructions. Safeguards there:
  paper-only; no new numerical searches or expensive computation; independent separate-session
  review; no manuscript or ledgered-file changes, no pull requests, no merges.
- **Write path.** This record is published by `git push` to its branch only. No pull request,
  Issue edit or comment is made by its writer. The branch-only state is provisional (§A.43).
- **Goal link (§A.47).** Serves #1509 (quantum emergence; the NONDIO line). It would decide, for
  each named restriction of (F-S), whether it restores DIO-type on the class where BIDUAL-REL's
  Theorem NDIO fails it, and whether OI's stated premises supply that restriction. It does not
  decide NN M4 (the nativeness criterion), M1-b, the A1 retirement, OPRES U1′, or anything about
  encoded carriers.
- **Tracking.** Accountable Issue #1509. Source record BIDUAL-REL, branch
  `research/bidual-rel-20261122`, head `dda8d67c`, from which this branch is cut; that branch is
  not changed.
- **A1 ledger check.** Before the first commit, `origin/research/a1exit-deletion-20261121` was
  fetched read-only at `8d7d67d094e4d118268f432ce50bf53d9230e7dd`, and
  `verification/audits/foundations/a1exit-deletion-20261121/ledger.json` was read there. Its
  `files` map lists 44 paths. The only one under `verification/programmes/oi-qm/reconstruction/`
  is `native-y-continuation-20261024/README.md`. None lies under
  `verification/programmes/oi-qm/reconstruction/bidual-dio-20261122/`, which is the only
  directory this record writes.

## 1. Pins

| Source | Pin | Use |
|---|---|---|
| BIDUAL-REL | `dda8d67c` | `NOTE.md`: Lemma PUR, Lemma DSJ, Theorem REL, Proposition BID′, Proposition HN, Construction GLU, Theorem NDIO, §5 |
| NONDIO-M2 | `7102e6af` (ancestor of `dda8d67c`) | `NOTE.md`: Lemmas VS, SL, CMP, JU; RED-M2; MIO-M2; CX-F; both slice orders; Proposition BID; §6 (LAW-σ, LAW-fa) |
| NONDIO-M1 | `dac9ca3f` (ancestor) | Lemma NRM (a), DET-at, through NONDIO-M2 |
| NATIVE-NONDIO | `ab830621` (ancestor) | NAT, DEC, M3, M4 |
| `papers/Main.md` | at `dda8d67c` | the Definition (line 42), Lemma 1 (line 46), Lemma 2 (line 48), the measure Remark (line 58), the status Remark (line 60), the posit ledger (line 736) |

## 2. The question

Notation as in BIDUAL-REL: A = B(ℓ²(C_V)), D = ℓ^∞(C_V), B = B(ℓ²(C_V) ⊗ ℓ²(Z)), A\*\* the
bidual, D\*\* the σ-weak closure of D in A\*\*. An assignment ρ ↦ Ω_ρ gives each state ρ of A a
state of B with PROD (Ω_ρ(a ⊗ c) = ρ(a)ω(c)). It is **DIO-type in (F-S)** when, for every
instrument of NONDIO-M2's RED-M2 class, the output configuration law depends on ρ only through
ρ|_D. BIDUAL-REL Theorem NDIO gives, for C_V = Z = ℕ, an affine assignment with PROD that is not
DIO-type.

**Q.** For each restriction R named in §5, is R sufficient for DIO-type in (F-S)? If not, which
counterexample satisfies R? Does R follow from OI's stated premises (with a citation), or is it an
additional assumption?

Each restriction is placed in one of two families, kept apart throughout:
- **normal-state restrictions**, which restrict the states (visible inputs, hidden state, or the
  carrier on which they live);
- **assignment restrictions**, which restrict how the joint state is chosen from (ρ, ω): symmetry
  (covariance) conditions and constraints on slice-order selection.

Mathematical existence of a non-DIO assignment is reported separately from whether OI's native
premises deliver non-DIO behaviour.

## 3. Assumptions

Those of BIDUAL-REL `PLAN.md` §3: KIN-B, LIN, TB, DEC, KIN-𝒟, σ-D, PROD, NAT (named, not
adopted), LAW-σ and LAW-fa (readings, neither adopted). The affine typing is assumed only where a
node says so; a result proved for every assignment with PROD, affine or not, says so. CNT-V
(C_V countably infinite) is the scope of Theorem NDIO; FIN-V (C_V finite, `Main:46`) is examined
as a restriction in D1, not assumed elsewhere.

## 4. Productivity test (§A.31), fixed before the walk

The investigation is a **gem** iff it yields a fact strictly stronger than the restatement
"BIDUAL-REL Theorem NDIO gives a non-DIO affine assignment with PROD on CNT-V; DIO-type holds for
normal ω with affine assignments, for normal visible inputs, and for each slice order", **and**
either (i) decides, for at least one restriction named in §5 that the restatement does not cover,
whether it is sufficient (with proof) or insufficient (with a counterexample satisfying it), or
(ii) exposes a hidden assumption in how (F-S), covariance or slice order is posed. Otherwise it is
a **non-gem** (coherence relabelling). "Missing premise" is an allowed outcome and is compatible
with either verdict.

## 5. Nodes and decision rules (depth-first; decisive branch first)

- **D0. Corpus and literature.** Search `papers/`, `book/`, `verification/` and the Lean trees
  for statements on: the cardinality of C_V; normality or σ-additivity of hidden priors and
  preparations; joint preparation of visible and hidden sectors; slice order or iterated limits;
  covariance of a preparation or append. *Rule:* record each hit with its location and what it
  states; a restriction is classed "follows from OI" only with such a citation.
- **D1 (decisive). FIN-V.** Is C_V finite by OI's premises, and does FIN-V restore DIO-type for
  every assignment with PROD? *Rule:* a citation and a proof give "sufficient, follows from OI";
  a missing citation gives "additional assumption". Skepticism on the favourable branch: test
  whether any OI object plays the visible role with an infinite carrier.
- **D2. Normal-state restrictions on CNT-V.** (a) normal visible inputs; (b) normal ω, including
  non-affine assignments. *Rule:* proof or counterexample; source in OI or additional assumption.
- **D3. Covariance.** (a) covariance of the assignment under a group of visible unitaries
  (diagonal unitaries, configuration permutations, all of U(A)); (b) hidden covariance: under the
  stabilizer of ω, as a covariant family in ω, and invariance of ω under all permutations of Z;
  (c) covariance under visible dephasing. *Rule:* for each, a proof of sufficiency, or an
  assignment satisfying it that is not DIO-type; for a restriction whose class is empty, a proof
  of emptiness.
- **D4. Slice-order selection.** (a) a single global slice order; (b) sector-wise selection,
  defined as a central element z of A\*\* weighting the two slice orders. *Rule:* proof of
  sufficiency, or a counterexample; for (b), the exact condition on z if one is proved.
- **D5. The exact condition.** Is there a condition on the assignment equivalent to DIO-type in
  (F-S)? If so, does OI supply it? *Rule:* an equivalence with proof in both directions (§A.34),
  stated with its circularity status; a citation, or the missing premise named precisely.
- **D6. Existence and realizability.** For each premise the non-DIO construction needs, where it
  stands under OI's stated premises and under LAW-σ and LAW-fa. *Rule:* proof and citation only.

Every node is closed by an explicit check with its verdict and support layer recorded at the node.
Every result is labelled **ESTABLISHED** (proved on paper here, layer X, or cited at its source's
standing; established within this record, not in the §A.46 sense), **ASSUMED** (a named premise)
or **MISSING** (a gap, with the node where the branch stopped).

## 6. Negatives and scope

A negative (insufficiency) is stated only for the restriction and class named at the node, with
the counterexample's premises listed. It is not a statement about (F-H), NAT preparations, encoded
carriers or OPRES's protocol class. A restriction is not called physically motivated unless D0
finds it in the corpus; a restriction equivalent to DIO-type by inspection is recorded as
definitional.

## 7. Stop conditions

Each is sufficient, and the record names the one under which it stops:
- every restriction of §5 has a proof, a counterexample, or a precisely identified missing
  premise;
- a node that needs computation, a change to the physical model or a new premise: name it and
  stop that branch;
- a node that needs a literature theorem that cannot be checked here: cite it at its source's
  standing, record it as missing, and stop that branch.

There is no successor round.
