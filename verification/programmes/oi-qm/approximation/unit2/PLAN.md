# OI-QM-APPROX-1, unit 2 (G3-D14): stability of the operational-completion characterization

Plan, fixed before any bound is written. Status of both directions at this commit: **open**.

- **Accountable home:** #1216 (OI-QM-APPROX-1). Parent programme #1169. Row D14 of unit 1's
  dependency matrix ("Approximate analogue of the five conditions", status "open (not stated
  anywhere read)", carrier C, independent of #945).
- **Authorization.** Owner decision at #1169 c.7184425769 (amaybaum, posted
  2026-11-26T06:26:07Z, decision time stated as 2026-11-26T06:25:53Z), item 2, lane 3: "Investigate
  both directions of approximate OI–QM equivalence through stability gate D14." The decision
  approves the lane 3 scope as written, supersedes the earlier parking of #1216, and keeps the
  restrictions "paper-only research, no computational experiments, no manuscript changes, no
  adoption of new premises and no automatic merges". It also states: "A rigorous negative result
  or counterexample is as valuable as a positive derivation. Do not favor conclusions merely
  because they support OI."
- **Writer:** Claude Code, designated writer for lane 3. Independent non-author review follows the
  report; no acceptance is claimed here.
- **Pinned source.** `origin/main` = `b6c6b80bbd4a878452e54759cc85f16c9ffb72da`
  (2026-11-26 08:23:24 +0200). "Main" = `papers/Main.md` at that commit (SHA-256 prefix
  `8b12696cd02b1e5c`); "OB/" = `verification/lean-mathlib/OIBridge/`. All `path:line`
  citations are at the pinned commit.
- **Goal link (§A.47).** Serves #1216 (Foundational): decides whether the exact characterization of
  finite operational QM by the five completion conditions (row D13) survives finite precision in
  each direction separately, at fixed (d, m, K), under a metric fixed here. It does not decide
  whether OI supplies any condition, exact or approximate.

## 1. Setting

The setting is that of `exactAll_iff_physical_general` (OB/GeneralCarrier.lean:100):

- a nonempty finite carrier A with |A| = d, and a `FiniteOperationalTheory` T on A
  (OB/OperationalAssembly.lean:594): availability predicates on finite outcome families of
  ℂ-linear maps on the complex matrices indexed by A (the system) and by A × Fin n (level n), an
  availability predicate on preparations, and the six structure rules of Main:572 (a)–(f), all
  kept **exact**;
- the complex matrix kinematics is taken as given, as in Main:572 and in the kernel. The trace
  norm, the positive semidefinite cone, the unitary group, the spectator tensoring
  `withSpectator`, transport along reindexings and the partial trace are kinematic data;
- "quantum instrument" means `IsFiniteEndomorphicKrausInstrument`: a finite Kraus family summing to
  the identity, with outcome assignment.

**Finite dimension is finite accessible resolution, not A1.** The carrier A and the ancilla levels
are the finite operational resolution of an observer's accessible description. A is not identified
with a finite substratum configuration space, the argument does not use total finiteness of the
substratum (posit A1), and unit 1's route C (direct identification of configurations with a
quantum carrier) is not used.

## 2. Metrics on complete accessible-history laws (declared in advance)

**Histories.** At a fixed level n ≥ 1 (carrier dimension N = d·n), or at the system (N = d), a
protocol π of horizon K with outcome bound m applies K available families, each with at most m
outcomes, the choice of each family a function of the earlier outcomes. For an input density
matrix ρ on the level's carrier the history law is
P^T_π(ρ)(o_1, …, o_K) = tr(F^K_{o_K} ∘ ⋯ ∘ F^1_{o_1})(ρ). The same definition with quantum
instruments gives P^Q. Preparations other than the inputs ρ are not part of the history class:
the exact characterization says nothing about `prepAvail` beyond the uniform attachment, and the
history class is kept to the exact theorem's scope. TV(p, q) = ½ Σ |p − q|, defined for any
complex vectors (a non-quantum theory may produce non-real or negative "probabilities").

Two metrics are declared, both before any bound. The reasons are fixed independently of outcome:
M_H is the finite-test metric Main uses for its density statements (Main:606, :610); M_C is the
law-level reading closest to the kernel statement, which concerns availability of specific maps,
and it implements unit 1 §7.1's requirement of a fixed correspondence with separate coverage and
soundness.

- **M_H (behaviour-set Hausdorff).** At fixed (level, m, K):
  M_H(T, Q) = max( sup_{π_T} inf_{π_Q} sup_ρ TV(P^T_{π_T}(ρ), P^Q_{π_Q}(ρ)),
  sup_{π_Q} inf_{π_T} sup_ρ TV(…) ). Protocols are compared as wholes; no correspondence between
  families is required.
- **M_C (correspondence metric).** At fixed (level, m, K): the soundness term is the infimum,
  over maps c sending each available family (≤ m outcomes) to a quantum instrument with the same
  outcome set at the same level, of sup_π sup_ρ TV(P^T_π(ρ), P^Q_{c(π)}(ρ)), where c(π) replaces
  each family by its image; the coverage term is the same with a map c′ from quantum instruments
  to available families; M_C is the maximum of the two terms. M_H ≤ M_C.

For a set Λ of levels (the system included where stated), M(·) on Λ is the supremum over Λ.

## 3. δ-forms of the five conditions (declared in advance)

Norms: for a family F = (F_a), ‖F‖ = sup_{X ≠ 0} Σ_a ‖F_a(X)‖₁ / ‖X‖₁ over all complex matrices
(the trace-norm induced norm of the map into the classical–quantum direct sum); for a single map,
the induced trace norm ‖·‖_{1→1}. Each δ-form replaces an equality or membership of the exact
condition by a distance at most δ in these norms, uniformly over the families it quantifies over;
none refers to the set of quantum instruments.

- **V_δ (validity).** For every available family at a level in Λ, every branch a and every
  positive semidefinite X with tr X = 1: dist₁(F_a(X), PSD) ≤ δ; and for every X,
  |Σ_a tr F_a(X) − tr X| ≤ δ‖X‖₁.
- **L_δ (trivial-ancilla consistency).** For every family F available on the system there is a
  family G available at level 1 with ‖G − transport(F)‖ ≤ δ.
- **I_δ (inert spectators).** For every family F available at level n, every finite spectator R
  and every relabelling e : R × (A × Fin n) ≃ A × Fin m′ with n, m′ in Λ, there is G available at
  level m′ with ‖G − withSpectator_e(F)‖ ≤ δ.
- **U_δ (reversible control).** For every level n in Λ and every unitary U on its carrier there
  is a single-outcome available Φ with ‖Φ − conj U‖_{1→1} ≤ δ.
- **C_δ (iterated composition).** Whenever the transport of F is available at level n(r+1) in Λ,
  there is G available at level n with ‖G − discard_{uniform}(F)‖ ≤ δ.

C_δ[M, Λ] denotes the conjunction restricted to families with at most M outcomes and to levels in
Λ. δ = 0 with Λ all levels and M unbounded is the exact `PhysicalCompletionConditions`.

## 4. Preregistered questions

| ID | Question | Status field |
| --- | --- | --- |
| Q0 | Does each of the five conditions admit a δ-form that does not import quantum structure beyond the given kinematics? If not, record the finding and stop. | open |
| Q1 (Direction 1) | At fixed (d, m, K): does C_δ[M, Λ] for suitable M, Λ imply M_C ≤ ε(δ, d, m, K) (hence M_H ≤ ε), with ε → 0 as δ → 0? | open |
| Q2 (Direction 2, converse) | At fixed (d, m, K): does M ≤ ε on a level set imply C_{δ(ε)} with δ(ε) → 0, separately for M = M_H and M = M_C? | open |

Q1 and Q2 are separate questions with separate statuses (§A.34). Neither direction's result is
used as evidence for the other.

## 5. Order of work

1. Q0, condition by condition. A failure stops the unit.
2. Q1 at d = 2.
3. Q1 at general d.
4. Q2, first M_H, then M_C.

## 6. Productivity test and stopping rule (fixed now)

- **Gem** iff the unit yields an explicit ε(δ) bound, a counterexample to stability, or a proof
  that a condition admits no non-quantum δ-form. Anything less is record-only.
- **Stop** when each direction reaches proved, disproved or a named gap at fixed (d, m, K), or
  when 3–4 consecutive passes yield no NEW finding.
- Any branch favourable to the framework is pressure-tested before it is accepted (§A.31).

## 7. Inputs and their labels

- [K] kernel-checked on `main`: `exactAll_iff_physical_general`, `general_characterization`
  (OB/GeneralCarrier.lean:100, :107), and the definitions and lemmas they rest on, cited by name.
- [P] Main §3.4 on `main`, in particular Main:572 (the operational-extension boundary), :604
  (adaptive telescoping), :606 and :610 (uniform realization, finite-test density). The finite-b
  items (Main:574 clause (1), the Rounding Lemma's open complex-entry constant, the clipped and
  normalized law) are open and are not used.
- Partially verified: unit 1 r4b (`../unit1/APPROX-UNIT1.md`), its [A] and [W] items; used only
  for labels (D13, D14) and for §7.1's coverage/soundness split.
- [L] standard literature, recalled.
- [A] this unit's own arguments, unreviewed.
- Off-main work (#1222, #1227, #1229, the F945-R note) is provenance only and no claim uses it.
  #945's repair is not done and not used.

## 8. Boundaries

Paper-only; no computation. No manuscript change. No new premise; no premise is chosen because it
reproduces QM (§A.29). #1169's exact conditions are not altered. Unit 1's `STATUS.md` is not
edited.
