# BORN-SEL (b): QB-3 proposed wording and QB-4 review locations (#1059)

**Status.** WIP / UNVERIFIED. Paper only. Written by `writer-born` under the owner's rulings of #1059 c.6650820790
(amaybaum, 2026-11-05; posted 2026-11-05T05:49:40Z).
- **Part 1** is a **proposal for independent review**. It is not applied to the O-OBSMU record (#866, #914), and it
  changes no status.
- **Part 2** lists locations for the owner-approved paper review. It is not a Lean plan.

Neither part edits Main, the book, a Lean module or a frozen record.

***

## 1. QB-3: proposed μ-form / μ-number wording for O-OBSMU (proposal; not applied)

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

**Proposed wording** (exact text, for review):

> **O-OBSMU, μ leg: μ-form / μ-number.** This is an obligation classification. It does not source the physical
> measure.
> - **μ-form (the invariance option holds within its proved scope).** The fixed-basis representation form and its
>   stated equivalences do not depend on the residual choice of μ.
>   - For every law μ on a finite `S`, the induced finite-horizon law lies in `Q_fb` through the same `U_φ`, basis and
>     readout. The kernel construction `D_imp_Qfb` (`Equivalence.lean:294`) is quantified over every `RevReal`, and
>     `S ⇔ D ⇔ Q_fb` holds for every finite-horizon law (`finite_horizon_equivalence`, `Equivalence.lean:462`).
>   - The native Born weights `|U_φ|²` lie in `{0, 1}` for every μ, so the representation's table is unchanged under
>     `|U|^p` for every `p > 0`.
> - **μ-number (the invariance option fails for the tested class; the selection option is open).** The numerical
>   probabilities the representation carries are not invariant across the tested class of finite bijections. These
>   are the finite-horizon law, the rooted family, the one-step matrix of the Born-form theorem, and the conditional
>   predictions given a record.
>   - On the eight-state bijection CE-8, the uniform law on one orbit and the counting law give different one-step
>     matrices: `[[0, 1], [1, 0]]` or `J/2` against `[[1/4, 3/4], [3/4, 1/4]]`.
>   - No current premise physically selects a branch of the measure. Their physical selection remains open.
> - **Indivisibility (Main:137) is on the μ-number side.**
>   - The implication "a readback gap with finite recurrence gives rooted indivisibility" holds under every measure
>     branch, including hidden laws that depend on the root.
>   - Whether its hypothesis and its conclusion hold depends on μ. On CE-8, the uniform law on the orbit `O_A` gives a
>     P-divisible rooted family, and the counting law gives an indivisible one.
> - **Scope.** The non-invariance is shown on generic finite bijections (CE-8). It is not extrapolated to the
>   manuscripts' native wave substratum, where it is unchecked. Computation C-1 addresses that case and has not been
>   run.

**Support for each clause** (to be checked by the reviewer):

| Clause | Support | Layer |
|---|---|---|
| μ-form, membership in `Q_fb` for every μ | `D_imp_Qfb` (`Equivalence.lean:294`), quantified over every `RevReal`; `finite_horizon_equivalence` (`Equivalence.lean:462`); BSB Lemma B1, lines 117–122 | kernel-checked (on `main`), with the exponent-insensitivity step a paper derivation (BSB B1: `0^p = 0`, `1^p = 1`) and Main:556's "check 6" |
| μ-number, CE-8 | BSB Lemma B3, lines 129–138; reviewed in #1082 c.6622453125 (rechecked by hand) and accepted at `7b46d36c` (c.6622587957) | paper derivation, off `main` |
| no branch selected | BSB §4, Q-sel summary, lines 345–347; N2, lines 161–181 | paper derivation, off `main` |
| indivisibility on the μ-number side | BSB Lemma B4, lines 147–159 | paper derivation, off `main` (QB-4) |
| scope | BSB lines 142, 342; `PREREG-C1.md` §9 | paper statement |

**Consistency with the O-OBSMU note** (provenance only: branch `research/o-obsmu-20261104` at `f67b9f0c`, #1110,
off `main`).
- That note's Theorem SI states that the recurrence-cycle P-divisibility of the rooted family depends on the hidden
  laws only through their supports, and not invariantly across supports (CC-1).
- CE-8's two branches differ in support: one orbit against all of `S`. So the B4 dependence above is a dependence
  through the support, and the two are consistent [D].
- The note's consumer table puts the representation equivalence (U1–U3) outside the residual choice, which agrees with
  μ-form.
- Neither statement here relies on that note.

**What the proposal does not do.**
- It does not apply the wording to #866, #914 or any O-OBSMU record.
- It does not source μ.
- It does not claim non-invariance for the wave substratum.
- It changes no status, label or classification until it has been independently reviewed and the owner records it.

**Off-`main` support (§A.42 item 8).** BSB is on this branch only (`7b46d36c`, unchanged at this head). The μ-number
and indivisibility clauses therefore rest on support off `main`, which is a gap. It must be closed before the wording
is recorded as established, either by landing BSB on `main` or by narrowing the wording.

***

## 2. QB-4: locations for the independent mathematical review

The owner's ruling: "approved for paper review only. Independent mathematical review of B4 and Lemmas G, G2, U, E and
N2.1. Afterwards, present which results merit Lean formalization. No Lean implementation and no manuscript promotion."

**File and commit.** All six are in
`verification/programmes/oi-qm/reconstruction/born-sel-b-measure-20261104/BORNSEL-B-MEASURE.md`.
- The file was last changed at `7b46d36c38734504c0ec3df27331835de5293d6a` and is unchanged at this branch's head.
- **It is not on `main`.** The commit is on branch `research/born-sel-b-measure-20261104` (#1082). There is no
  commit on `main` to cite, and the reviewer reads the file at `7b46d36c`.
- The `Main:N` lines the lemmas cite are at `main` `1609dc440f5a12d05b750f6d894bb91d09a099a3`.

| Result | Lines at `7b46d36c` | Statement in brief | Inputs it uses |
|---|---|---|---|
| Lemma B4 | 147–159 | Main:137's implication (gap + finite recurrence ⇒ rooted indivisibility) holds for root-dependent hidden laws; its hypothesis and conclusion depend on μ (CE-8) | Main:137; `isPermMatrix_of_stochastic_inverse` (via Main:133); CE-8, lines 129–138 |
| Lemma N2.1 | 183–187 | Every invariant law is `Σ_O w_O·unif(O)`; `H(μ_w) = H(w) + Σ_O w_O log|O|`; the maximal-entropy invariant law on an invariant `U` is `unif(U)` | `invariant_pow` (`CanonicalMeasure.lean:96`); `counting_maximal_entropy` |
| Lemma G | 193–195 | Among laws supported in `A`, `unif(A)` is the unique entropy maximizer; `unif(B)(· \| A) = unif(A)` for `B ⊇ A` | `entropy_le_log_card` (`FiniteEntropy.lean:98`); equality case from the literature |
| Lemma G2 | 197–203 | No invariant law gives a time-varying record probability 1 while keeping the actual microstate in its support | the invariance of μ; the definition of a time-varying record (line 52) |
| Lemma E | 286–299 | No fine-grained relaxation: entropy and `ℓ¹` distance to every invariant law are conserved, and `φ^L_* μ = μ`; the Cesàro mean is `Π(μ) = Σ_O μ(O)·unif(O)` | `entropy_marg_of_injective` (`FiniteEntropy.lean:158`); Main:640 |
| Lemma U | 303–307 | Every rational prior `μ(s) = n_s/D` is counting conditioned on an event in an inert enlargement `S × [D]`; irrational priors are outside its scope | the definitions only |

**Review questions per result** (proposed):
- Is each proof complete for the statement as made, one direction at a time where it is an equivalence (§A.34)?
- Are its hypotheses stated?
- Does it use only the cited inputs?

After the review, the writer presents which results merit Lean formalization. No Lean work is authorized.
