# A1-EXIT R6 — preregistration: lemmas L6, L7, L9 on infinite hidden carriers

**Status.** Writer's paper-only preregistration, committed and pushed before any lemma is
classified. The classification is `RESULT.md` in this directory, in a later commit. No manuscript,
Lean or registry edit; no premise adoption; no merge. A1 (Main posit ledger item (ii)) remains open
and unadopted. Independent non-author review is required before any use of the result.

**Authorization.** Owner `amaybaum`,
[#1169 comment 7047514209](https://github.com/amaybaum/incompleteness/issues/1169#issuecomment-7047514209),
2026-11-20T18:31:48Z, "Owner decision record: A1 removal is the highest-priority objective". Step 1
table, row R6: "lemma recovery | L6 (Koopman dilation channel family, M9), L7 (physical-memory
theorem on a measurable hidden space, M16), L9 (coherent-channel invariance under an infinite
decoupled factor, M21, C8) | Valid proofs, or an explicit finite-only restriction of the unsupported
conclusions | Paper-only research record". Safeguards quoted from the same record: "1. **No
disguised A1.** A weaker hypothesis must not imply total finiteness indirectly, or reproduce A1
under another name." "2. **No forced proof.** Q1 and R6 may end with negative results or
finite-only restrictions. Success is an accurate classification, not necessarily a generalization
to infinite systems." "3. **No silent promotion.** Statements that are finite-only or conditional
stay clearly qualified in Main, the companion papers, the book and all mirrors." Step 2 (manuscript
propagation) is "queued, not authorized"; this record lists Step-2 corrections and applies none.

**Goal link (§A.47), from the authorization.** "Make OI's foundational formulation independent of
the assumption that the whole universe is finite, while keeping honest limitations on the results
that still require finiteness." This unit decides, for the consumers M9, M16, M21 and C8 of
A1-REMAINDER, whether each conclusion holds on an infinite hidden carrier, holds under a named
weaker condition, is finite-only, or is open. It does not decide whether any hidden law is
physically justified (R1).

**Source pin.** `main` at `9db518844df62151979acf6aac1d487b59c44907`. `M:n`, `Sub:n`, `GR:n` are line
`n` of `papers/Main.md`, `papers/Substratum.md`, `papers/GR.md` at the pin. Line numbers quoted from
REMAINDER refer to its own pin `21e16c61`.

| Short name | Path on `main` | Used for |
|---|---|---|
| REMAINDER | `verification/audits/foundations/a1-remainder-20261119/REMAINDER.md` | rows M9, M16, M21, C8; §2 R6; lemma index L6, L7, L9 |
| RIGID | `verification/audits/foundations/a1-rigid-visible-recurrence-20261119/A1-RIGID-1.md`; `verification/lean-mathlib/OIBridge/ObservableRigidity.lean` | measured rooted family `rootedFamily_productLaw`; P witness `exists_pIndivisibleWithin_of_nonPermutation` |
| MREC | `verification/lean-mathlib/OIBridge/MeasuredReciprocity.lean` | `rootMass`, `transition` under one law |
| CR | `verification/lean-mathlib/OIBridge/CausalReadback.lean` | `PDivisible`, `PIndivisibleWithin` |

## 1. Targets

Throughout: `V` is a finite set with `|V| ≥ 2` (Lemma 1; not at issue); `(H, 𝓗)` is a measurable
space; `ρ` is a probability on `H`; `F : V × H → V × H` is a measurable map; the rooted family is
`Γ_t(a, b) = ρ{h : π_V F^t(a, h) = b}` (M:131; RIGID `rootedFamily_productLaw`); P-divisibility on
`{0, …, n}` is CR `PDivisible`.

**T6 (L6; consumer M9 = M:328–334, M:742).** Define, for finite `V` and an infinite measurable
hidden carrier, a channel family `{Φ_t}` on `B(ℂ^V)` that (i) reduces to Main's
`Φ_t(σ) = Tr_H[U^t(σ ⊗ μ_H)U^{−t}]` when `H` is finite, `F` is a bijection and `μ_H` is the
diagonal density of `ρ`; (ii) is CPTP; (iii) preserves computational-diagonal states with
populations `Γ_t`; (iv) satisfies the CP-indivisibility theorem: if `(Γ_t)` is not P-divisible on
`{0, …, n}`, there are `0 < t_1 < t_2 ≤ n` with no CPTP `Λ` such that `Φ_{t_2} = Λ ∘ Φ_{t_1}`.
Separately preregistered sub-question **T6-K**: does the literal Koopman form named in REMAINDER —
the Koopman unitary of `F` on `ℂ^V ⊗ L²(H, ρ)` with a normal (density-operator) hidden reference
state — satisfy (iii) and (iv)?

**T7 (L7; consumer M16 = M:459–479).** State and prove, for an arbitrary measurable hidden space
and an arbitrary reference probability `π_H`, the C2 quantitative theorem (M:459) and the
physical-memory theorem (M:473) — the total-variation bounds, the conditional-memory bound
`I(X_{<k}; X_{k+1} | X_k) ≤ 2[ε log(n_V − 1) + h(ε)]`, and the persistence-form contrapositive —
or identify the step that fails.

**T9 (L9; consumers M21 = M:60 deep-sector sentences and M:732 item (ii); C8 = Sub:251–268
Theorem 24 (i), (iii) and Corollary (iii)).** (a) Coherent form: for a decoupled factor on a Hilbert
space `K_A` of any dimension, prepared in a normalized state and evolved by its own dynamics with
product dynamics, the reduced visible channel family is unchanged at every time. (b) Classical
form: for a decoupled factor `(A, 𝒜, α)` with `α` a probability and its own measurable dynamics,
the T6 family and the rooted family are unchanged. (c) Theorem 24(i) on a measurable hidden
carrier: under which condition on a hidden relabelling `σ` the family is unchanged. (d) Whether
Corollary (iii) exact transfer extends to these factors.

## 2. Classification rule (fixed before classification)

Each target, and each separately worded part of one, receives exactly one class:

- **INF** — holds on infinite carriers: a proof ([W] paper derivation, or a cited on-`main` proof)
  under hypotheses that pass the disguised-A1 test of §3, and the finite statement is recovered as a
  special case (control K1 for T6; stated specialization for T7, T9).
- **WEAK** — holds under a named weaker condition: a proof that uses an additional named hypothesis
  which passes §3, together with a model in which that hypothesis fails and the conclusion fails
  (or the proof's step fails), so that the hypothesis is shown to do work.
- **FIN** — finite-only: the step that fails on infinite carriers is identified, and a countermodel
  on an infinite carrier, satisfying every non-finiteness hypothesis of the statement, refutes the
  conclusion; the conclusion is restricted to finite representatives.
- **OPEN** — neither a proof nor a countermodel.

A part whose proof is a [W] derivation not checked by an independent reviewer is reported as
"proved [W], unreviewed"; no class is a scientific status until review. Counterexamples and
countermodels are reported as exact computations where they are computed (K2–K4). No displayed
equivalence is planned; if one arises, each direction is a separate question (§A.34).

## 3. Disguised-A1 test (safeguard 1)

A hypothesis set `𝒽` of a target fails the test if any of the following holds: (a) every model of
`𝒽` has a finite total carrier, a finite hidden carrier, a finitely supported hidden law, or a
finite-dimensional hidden algebra; (b) `𝒽` contains finite order, exact return `φ^L = id` or a
uniform probability on the whole hidden carrier; (c) `𝒽` names a property that only finite
carriers have under another name. The test is passed only by exhibiting one model of `𝒽` whose
hidden carrier is uncountable with a non-atomic law (diffuse model). "Normalized" (total mass one)
is checked against (a) by the same exhibit.

## 4. Controls

| Id | Control | Decision rule |
|---|---|---|
| K1 | Finite recovery for T6: on finite `H`, the defined family equals Main's partial-trace family with diagonal prior | Exact rational comparison, exhaustive over every bijection at `(|V|,|H|) ∈ {(2,2),(2,3),(3,2)}`, `t ≤ 6`, with rational non-uniform priors as well as the uniform one. Any mismatch voids T6's INF class |
| K2 | Koopman form (T6-K) with normal hidden state `|ψ⟩⟨ψ|`, `ψ` the normalized constant function | Exact rational computation. (i) diagonal preservation: report whether some `F` maps a diagonal input to a non-diagonal output. (ii) CP theorem: exhaustive over bijections at `(|V|,|H|) ∈ {(2,2),(2,3),(2,4)}`, `1 ≤ t_1 < t_2 ≤ 12`: a countermodel is a pair at which `Γ` admits no stochastic divisor, `Φ_{t_1}` is invertible as a superoperator, and `Φ_{t_2} ∘ Φ_{t_1}^{−1}` has positive semidefinite Choi matrix (exact principal-minor test). Countermodel found ⇒ T6-K is FIN-or-fails for the Koopman form; none found ⇒ reported as "no countermodel at these sizes", not as a proof |
| K3 | Diffuse-carrier exhibit for T6 and for the P-witness premise: the Bernoulli skew product `F(x, h) = (x ⊕ h_0, σh)` on `{0,1} × {0,1}^ℤ`, `ρ` the fair Bernoulli law | Exact computation on cylinders for `t ≤ 8`: the family is CPTP, diagonal-preserving with populations `Γ_t`; report whether `Γ` is P-divisible on `{0,…,8}`. If it is, this records that a non-permutation `Γ_1` on an infinite carrier does not by itself supply the P witness, so M9's full chain needs (NR) or (RIG) |
| K4 | T9(c) relabelling on a diffuse carrier | Exact: a non-ρ-preserving relabelling of `[0,1)` that changes `Γ_1`; and the ρ-preserving case leaving it unchanged |
| P1 | Non-normal state pathology | The T6 and T9 statements must say whether a non-normal (singular) hidden or factor state is admitted, and the proof must not use a density operator for one |
| P2 | Non-separable pathology | Any Hilbert space used must be shown separable under the stated hypotheses, or its non-separability flagged |
| P3 | Non-measurable map or set pathology | Every set whose measure is taken must be shown measurable from the hypotheses (in particular the coincidence sets `{h : F^t_H(x,h) = F^t_H(y,h)}`), or the hypothesis that makes it so stated |
| P4 | Unnormalizable factor (counting measure on an infinite set, `I` on `ℓ²` of an infinite set) | Must be excluded by the T9 hypotheses, with the step that fails shown |

Computations K1–K4 are in one deterministic script beside this file, standard-library Python
(`fractions.Fraction`), with every control's outcome written to a JSON file in a stated schema
(§A.44) and a nonzero exit status on any failed control. Floating point is not used.

## 5. Output

`RESULT.md` gives, per target and per part: the precise statement with hypotheses; the proof or
the failing step with countermodel; the disguised-A1 test with the diffuse exhibit; the class; the
consumers' current text (file:line) and where finiteness enters; the Step-2 manuscript corrections
(listed, not applied); Lean-candidacy (not built); §A.42 item 8 trace of every off-`main` reference;
and a reviewer checklist.

**Not done.** No manuscript, Lean, registry, book or mirror edit. No law selection (R1), no claim
about M4/M7's recurrence content beyond its use as the P witness, no attempt on L8 or L10.
