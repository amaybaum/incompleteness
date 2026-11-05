# BORN-SEL (b): QB-3 wording and QB-4 review locations (#1059)

**Status.** WIP / UNVERIFIED. Paper only. Written by `writer-born` under the owner's rulings of #1059 c.6650820790
(amaybaum, 2026-11-05; posted 2026-11-05T05:49:40Z).
- **Review.** The r7 text of this file (`5ea9e4ca`) was independently reviewed in #1082 c.6651169194 (model-authored):
  QB-3 ACCEPT WITH CHANGES (Q1–Q8), and all six QB-4 results proved, B4 with a hypothesis correction and G2, N2.1 and
  U with precision edits. r8 (`500b3177`) applied those changes. The recheck of r8 (#1082 c.6651778560,
  model-authored: ACCEPT WITH CHANGES, minor) required R1–R10, which this revision (r9) applies. r9 is not reviewed.
- **Part 1** is the corrected QB-3 wording. It is not applied to the O-OBSMU record (#866, #914), and it changes no
  status.
- **Part 2** lists the QB-4 results, the review's verdicts, and where the corrections stand in `BORNSEL-B-MEASURE.md`
  r4. It is not a Lean plan.

Neither part edits Main, the book, a Lean module or a frozen record.

***

## 1. QB-3: μ-form / μ-number wording for O-OBSMU (corrected after review; not applied)

**The owner's scope limits, quoted** (#1059 c.6650820790):
- "μ-form: the representation form and its stated equivalences are invariant within their proved scope."
- "μ-number: the numerical probabilities are not invariant across the tested class of finite bijections, and their
  physical selection remains open."
- "The measure dependence of the indivisibility conclusion goes on the μ-number side, keeping any branch-by-branch
  implication."
- "No extrapolation from the generic-bijection counterexample to the native wave substratum."
- "This is an obligation classification, not a sourcing of the physical measure."

**The obligation it classifies.** The O-OBSMU μ leg, as #866 c.6600176951 quotes it from `verification/ROADMAP.md`
at `9613b21c`: "supply independently motivated structure selecting the physical observation map and ensemble, or
prove that the claims consuming an induced stochastic law are invariant under that residual choice".

**Route.** The review gives two routes to recording (c.6651169194 §1). Route A is taken.
#1059 c.6651648653 (amaybaum, Claude Code session chat, 2026-11-05; posted 2026-11-05T06:45:16Z) records: "The owner
selected **route A** for QB-3: preserve valid mathematical proofs through a reviewed evidence landing on `main`, rather
than narrowing conclusions purely because their evidence currently exists off-main." and "No proof promotion before
review and evidence retention." Accordingly:
- a minimal reviewed record lands on `main` first. It contains CE-8 (the map; `T^β`, `T^{α,O_A}`, `T^{α,O_B}`; the
  permutation status of `Γ_0, …, Γ_4`; divisibility under α on `O_A`; indivisibility under β), B4's root-dependent
  proof with its hypothesis that the hidden law at every root is a probability law, and the review;
- that landing is a merge and needs separate owner authorization, which no ruling gives;
- only after it may the wording below be recorded on O-OBSMU, with the bracketed items citing the landed record.

The review's route B, a wording narrowed to the support already on `main`, is not taken.

**Corrected wording** (exact text, as the review's full form; bracketed items cite the landed record):

> **O-OBSMU, μ leg: μ-form / μ-number.** This is an obligation classification. It does not source the physical
> measure, and it discharges nothing for a consumer that uses numerical probabilities.
> - **μ-form (invariant within its proved scope).** For every probability law μ on a finite `S = C_V × C_H` and every
>   horizon, the induced finite-horizon law lies in `Q_fb` (`D_imp_Qfb`, `Equivalence.lean:294`). `S ⇔ D ⇔ Q_fb`
>   holds for every finite-horizon law, with each direction kernel-checked (`finite_horizon_equivalence`,
>   `Equivalence.lean:462`). For every μ, the construction in that proof uses the permutation unitary of φ, the
>   product basis and the visible readout, and only the initial weights change. This is a reading of the proof, not a
>   stated theorem. The unitary's entries are 0 or 1, so the recovered table is the same for `|U|^p` at every `p > 0`
>   (Main:556).
> - **μ-number (invariance fails on the tested class; selection open).** On finite bijections, the numerical
>   probabilities change with μ: the finite-horizon law, the rooted family, the one-step rooted matrix (which equals
>   the Born-form theorem's `T_ij` when the hidden law given each root is uniform), and the conditional predictions
>   given a record. Main:60 records this for the two-state swap `φ(x,h) = (h,x)` under uniform versus point-mass hidden
>   priors. On the eight-state bijection CE-8 [landed record], the uniform law on `O_A`, the uniform law on `O_B` and
>   the counting law give one-step matrices `[[0,1],[1,0]]`, `J/2` and `[[1/4,3/4],[3/4,1/4]]`. Main selects the
>   counting measure by a posited maximal-entropy principle (Lemma 3, Main:56; posit (iv), Main:726, "not derived").
>   No derivation of a selection is established, and the physical selection is open.
> - **Indivisibility (Main:137) is on the μ-number side.** The implication holds for every law μ, with the hidden law
>   given each root taken as any probability law on `C_H` (fixed arbitrarily at roots of visible probability zero).
>   The implication: two distinct positive-probability visible histories with a common endpoint at order `k` make some
>   `Γ_s`, `1 ≤ s ≤ min(k, L−1)`, a non-permutation, and then the rooted family is not P-divisible on `{0,…,n}` for
>   every `n > s` with `Γ_n = I`. Support: Main:137 for a hidden prior shared by every root; [landed B4] for
>   root-dependent hidden laws. Whether its hypothesis and its conclusion hold depends on μ. On CE-8, the product law
>   uniform on `O_A` gives a P-divisible rooted family and no such pair of histories, and the counting law gives an
>   indivisible one.
> - **Scope.** The non-invariance is shown on non-native finite bijections: the two-state swap, and CE-8. These are not
>   claimed to satisfy (C2)–(C3) or to be instances of the native wave substratum. Nothing is inferred for the wave
>   substratum, where the question is unchecked.

**Where each review item is applied.**

| Item | Change in the wording |
|---|---|
| Q1 | membership in `Q_fb` is the kernel statement; "the same unitary, basis and readout" is stated as a reading of the proof term (`Equivalence.lean:297–299`), not a theorem |
| Q2 | the header states that the classification discharges nothing for a consumer of the numbers |
| Q3 | "no current premise selects" is replaced by Main:56's posited selection and Main:726's "not derived", with the selection open |
| Q4 | the one-step rooted matrix `Γ^κ_1` varies; the Born-form `T_ij` is its value at the uniform hidden law |
| Q5 | the implication carries its hypothesis: the hidden law at every root is a probability law |
| Q6 | the CE-8 laws are product laws, so the μ-dependence lies inside Main:137's shared-prior scope; B4 is needed only for root-dependent laws |
| Q7 | the scope names the two non-native bijections shown, claims nothing about (C2)–(C3), and drops the reference to C-1 |
| Q8 | the exponent clause cites Main:556 |

**Support for each clause** (the review's §A.42 item 8 trace):

| Clause | Support | Classification |
|---|---|---|
| μ-form, membership in `Q_fb`; `S ⇔ D ⇔ Q_fb` | `D_imp_Qfb` (`Equivalence.lean:294`); `finite_horizon_equivalence` (`Equivalence.lean:462`) | support on `main` [K] |
| μ-form, the same unitary, basis and readout | the proof term, `Equivalence.lean:297–299` | support on `main`; a paper reading of a kernel proof, not a theorem statement |
| μ-form, exponent | Main:556 | support on `main` |
| μ-number, numbers vary with μ | Main:60 (the two-state swap under uniform versus point-mass hidden priors); the map `φ(v,h) = (h,v)` is Main:78's. Under the uniform prior `Γ_1(a, j) = μ_H{h : h = j} = 1/2`, so `Γ_1 = J/2`; under `δ_0`, `Γ_1 = [[1,0],[1,0]]` [D, from those lines] | support on `main` |
| μ-number, CE-8 | BSB Lemma B3 (lines 129–138 at `7b46d36c`, unchanged in r4) | support off `main`: a gap until the route-A landing, which needs separate owner authorization |
| μ-number, selection open | Main:56; Main:726 | support on `main` |
| indivisibility, shared hidden prior | Main:137 | support on `main` |
| indivisibility, root-dependent laws; CE-8 dependence | BSB Lemma B4 (r4, lines 147–167) | support off `main`: a gap until the route-A landing, which needs separate owner authorization |
| BSB B1 (lines 117–122) | redundant with Main:556 | provenance |
| BSB N2 / §4 | not used: the selection clause rests on Main:56 and Main:726 (Q3) | provenance |
| BSB lines 142, 342 at `7b46d36c` (142 and 354 in r4); `PREREG-C1.md` §9 | the scope clause does not cite them (Q7) | provenance |
| #1082 c.6622453125 and c.6622587957 | a PR comment and an author-posted acceptance | provenance only |

**Consistency with the O-OBSMU note** (provenance only: branch `research/o-obsmu-20261104` at `f67b9f0c`, #1110,
off `main`, itself WIP / UNVERIFIED).
- That note's Theorem SI states that the recurrence-cycle P-divisibility of the rooted family depends on the hidden
  laws only through their supports, and not invariantly across supports (CC-1).
- CE-8's branches differ in support: one orbit against all of `S`. So the B4 dependence above is a dependence through
  the support, and the two are consistent [D].
- The note's consumer table puts the representation equivalence (U1–U3) outside the residual choice, as non-consumers
  that do not discharge O-OBSMU for any consumer that does; this agrees with μ-form and with the header's clause.
- Neither statement here relies on that note.

**What this part does not do.**
- It does not apply the wording to #866, #914 or any O-OBSMU record.
- It does not source μ.
- It does not claim non-invariance for the wave substratum.
- It changes no status, label or classification until the route-A record has landed, the wording has been reviewed,
  and the owner records it.

***

## 2. QB-4: the results reviewed, and where the corrections stand

The owner's ruling: "approved for paper review only. Independent mathematical review of B4 and Lemmas G, G2, U, E and
N2.1. Afterwards, present which results merit Lean formalization. No Lean implementation and no manuscript promotion."

**File and commits.** All six are in
`verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/BORNSEL-B-MEASURE.md`.
- The review read the file at `7b46d36c38734504c0ec3df27331835de5293d6a` (r3). r4, in this revision, applies the
  review's corrections to B4, N2.1, G2 and U; G and E are unchanged.
- **It is not on `main`.** The commits are on branch `research/born-sel-b-measure-20261104` (#1082).
- The `Main:N` lines the lemmas cite are at `main` `1609dc440f5a12d05b750f6d894bb91d09a099a3`; the review found the
  cited lines unchanged at `main` `f5c281ae`.

| Result | Lines at `7b46d36c` | Lines in r4 | Review verdict (c.6651169194) | Applied in r4 (not re-reviewed) |
|---|---|---|---|---|
| Lemma B4 | 147–159 | 147–167 | proved with correction | the hidden law at **every** root is a probability law (fixed arbitrarily at roots of visible probability zero), which step (iii) uses; positivity is relative to `ν⊗κ`; the range `1 ≤ s ≤ min(k, L−1)` and the conclusion for every `n > s` with `Γ_n = I`; the proof in steps (i)–(iii); the remark that the implication does not depend on the choice at zero-probability roots, while the conclusion's content there does; the CE-8 laws are product laws |
| Lemma N2.1 | 183–187 | 191–197 | proved | the characterization stated as an equivalence, with each direction proved; `w_O = μ(O)`; `0 log 0 = 0`; `U ≠ ∅`; the Gibbs proof of uniqueness of the maximizer, with Lemma G as an alternative, so the [L] citation is not needed |
| Lemma G | 193–195 | 203–205 | proved | unchanged |
| Lemma G2 | 197–203 | 207–214 | proved | the first two bullets hold for any `A ⊆ S`; the `ℤ`-indexed intersection and the finite-space support step stated; the "Consequently" bullet restricted to time-varying records, with the conserved-record case (`unif(I(A_r))` invariant, `s*` in its support); γ-c's coverage stated for veridical records (`s* ∈ A_r`) |
| Lemma E | 286–299 | 297–310 | proved | unchanged |
| Lemma U | 303–307 | 314–319 | proved | `n_s ∈ ℕ`, `Σ n_s = D ≥ 1`; the register sits in the hidden factor, `S′ = C_V × (C_H × [D])`; `|A| = D` and the fibre count; trajectories project at every horizon; `A` is not `φ′`-invariant in general, consistent with G2; the converse for a nonempty event |

B4's corrected hypothesis is also carried at BSB r4 lines 353 and 382, where the implication is cited.

**Lean.** The review's §3 ranks the results for formalization (B4 with CE-8 as a decidable witness; G2; N2.1 with E;
G only as a dependency; U not merited now). Presenting which results merit Lean formalization is the next step of the
ruling. No Lean work is authorized.
