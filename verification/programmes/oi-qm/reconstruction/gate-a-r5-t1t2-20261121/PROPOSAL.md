# GATE-A r5, §2.4 corrections T1 and T2 (proposal)

**WIP / UNVERIFIED. Proposal only; not adopted.** This paper-only record drafts corrections T1 and
T2 to §2.4 of the GATE-A r5 proposal (`verification/programmes/oi-qm/reconstruction/gate-a-r5-20261121/PROPOSAL.md`
at `fd3cb064a2c03e93bfa12bcceb708c8c897a494c`, PR #1503, cited `GA`). The owner approved their
preparation and independent review (#1169 c.7066166097, item 1) and clarified the form
(c.7066187558): the implication I★ ⇒ I★_st-coh is to be proved under explicitly stated
compatibility assumptions, with free evolution as an admissible protocol stated as an assumption,
not hidden inside a definition. GA r5 is not adopted. #1503's branch and record are not changed:
this record sits on a separate branch stacked on `fd3cb064`. No manuscript, Issue body or contract
on `main` is edited. Physical source remains NOT PASSED.

The defects are those recorded in #1508's NOTE at `df520f3b`
(`verification/programmes/oi-qm/reconstruction/i3-source-20261121/NOTE.md`, §9), as reviewed in
#1508 c.7065957850 §3 and c.7066083871 §3. `GA:n` is line n of GA at `fd3cb064`.

**Revision r2** answers the review at `63f06224` (#1510 c.7066238695): s_Λ is retyped against
EP:79 (R1); ENC is folded into FE-ADM and the §2 definitions (R2); FE-ADM's non-exclusion of D-W is
recorded; Lemma TC is relabelled. r2 is not yet re-reviewed.

## 1. The two defects

- **T1 (mistyped relation).** GA:280 states "Both variants are strictly weaker than I★". For
  I★_st-coh as typed at GA:259–264, the comparison quantity is the Born-form visible family of
  `Sub:249` and `familyAt`, Φ_t(ρ_V) = Tr_H[φ̂^t (ρ_V ⊗ ω_H) φ̂^{−t}], with the model's autonomous
  dynamics. I★ fixes record laws p(h | π, p) of requested protocols (GA §2). The two definitions
  differ in three respects (c.7065957850 §3): (i) realization requirement, Born-form lift against
  record laws; (ii) dynamics, autonomous φ^t against a requested instrument; (iii) encoding,
  visible configurations against a declared X_A with a label rule. So "strictly weaker" does not
  follow as typed.
- **T2 (indexing).** GA:260–261 gives "the one model M* ... a visible sector V_A encoded by enc_A,
  with its hidden prior" for every target family Λ_A. With φ and the prior fixed, a sector indexed
  by A alone carries exactly one autonomous family {Φ_t}. For |A| ≥ 2 there are distinct target
  families on A (for example Λ_t = id and Λ_t = Ad_Z^t with Z = diag(1, −1, 1, …), which differ at
  t = 1 on the coherent input |+⟩⟨+| of the first two levels), so both GA variants are unsatisfiable
  by every model, the target's own dilation included. (For |A| = 1 every channel is trivial.)

## 2. Corrected definitions

**T2 correction (indexing by a setting).** The single-time family is indexed by (A, Λ) through a
setting. For every nonempty finite A and every target family Λ_A in GA's class, the encoding rule
assigns, from the typed data of Λ_A and before any comparison (I-2★), a **setting** s_Λ. Two typings
are consistent with EP (c.7066238695 R1); this record writes (b) and records (a) for T-D1:

- **(b) controller-field setting (written here).** s_Λ is a configuration c_{s_Λ} of M*'s
  controller fields C, loaded by ι; EP:79 permits a setting to load "only the specified controller
  fields" and keeps the law of the uncontrolled variables U, and so the one hidden prior ω_H,
  unchanged. The family is
  Φ^{(A,Λ)}_t(ρ) = Tr_{C×H}[φ̂^t (enc_A(ρ) ⊗ |c_{s_Λ}⟩⟨c_{s_Λ}| ⊗ ω_H) φ̂^{−t}], read back through
  enc_A, t ∈ ℕ. Assumption (c) of #1508's S1/S2 (one hidden state for every input) holds as before.
- **(a) preparation setting.** (ρ, s_Λ) is the preparation; EP:75 lets μ_p depend on p, so the hidden
  state ω_{s_Λ} may depend on s_Λ, but not on ρ. The family is
  Tr_H[φ̂^t (enc_A(ρ) ⊗ ω_{s_Λ}) φ̂^{−t}]; it stays linear in ρ.

A setting cannot change the hidden prior (EP:79); r1 of this record wrote it that way, and that
typing is withdrawn. The interface of `Sub:249` is kept as it stands (fixed visible/hidden
interface, one time at a time, no interventions): under (b) the prior of the uncontrolled hidden
variables is fixed and only controller fields vary with the family; under (a) the hidden state is
fixed per preparation. An alternative, one sector per (A, Λ), is recorded and not proposed: with
one prior and countably many encodings a single model realizes at most countably many population
families (#1508 NOTE Lemma R1, layer P), so a continuum of targets would need a continuum of
sectors.

**Encodings.** Every family above, and the operational family below, is read through enc_A and the
label rule 𝓛_A of the I★ witness; this is part of the definitions, and FE-ADM (§3) names 𝓛_A
explicitly. r1's separate assumption ENC is not an independent assumption and is folded in here.

**The operational single-time family.** For M*, A, Λ and t, write
p_{M*}(E | s_Λ, ρ, t) for the probability of the first outcome when ρ is prepared on X_A with s_Λ
loaded, the model evolves freely for t steps, and the two-outcome readout {E, 1 − E} is applied
and recorded. When a linear map L_t on matrices over A satisfies p_{M*}(E | s_Λ, ρ, t) =
Tr(E L_t(ρ)) for every density ρ and effect E, it is unique (Lemma TC below), and it is called the
**operational single-time channel** Λ̂^{M*,(A,Λ)}_t.

**Variants after the correction.**
- **I★_st-coh** (Born form, as in GA, with the T2 indexing): Φ^{(A,Λ)}_t = Λ_t for every t.
- **I★_st-coh^op** (operational): Λ̂^{M*,(A,Λ)}_t exists and equals Λ_t for every t.
- **I★_st-pop** (as in GA, with the T2 indexing): ⟨j|Φ^{(A,Λ)}_t(|i⟩⟨i|)|j⟩ = ⟨j|Λ_t(|i⟩⟨i|)|j⟩
  for all i, j ∈ A and every t; its operational counterpart I★_st-pop^op uses p_{M*}(|j⟩⟨j| |
  s_Λ, |i⟩⟨i|, t) instead.

## 3. Assumptions, stated separately

- **PROT (protocol restriction).** For each A, Λ, t, density ρ and effect E, the protocol
  π(ρ, Λ_t, E): prepare ρ; apply the one-outcome instrument {Λ_t}; apply the two-outcome instrument
  with Kraus operators √E and √(1 − E); record the outcome, is a protocol of `J_exact(A)`. This holds
  by EP:37–40, since Λ_t(ρ) = Tr_K[W^t (ρ ⊗ σ_K) W^{−t}] is a CPTP endomorphic map of A and the
  readout is a finite-outcome CP instrument; it is a check, not an import.
- **FE-ADM (free evolution as an admissible protocol), an assumption.** For every A, Λ and t, the
  procedure "load s_Λ, prepare ρ, evolve freely under Φ for t steps" is M*'s label interpretation
  𝓛_A of "prepare ρ, apply Λ_t", and the readout {E, 1 − E} is 𝓛_A's interpretation of the readout
  instrument (this names 𝓛_A, and so the encoding enc_A, for both). I★ does not entail FE-ADM: I★ lets 𝓛_A realize Λ_t by any admissible procedure,
  interventions included. FE-ADM is a constraint on the witness's label rule, and it is what makes
  the native single-time observation a protocol of `J_exact(A)`. It is the identification named
  ID-FE in #1508's NOTE. **FE-ADM does not exclude D-W** (c.7066238695): with s_Λ in the controller
  fields, the stepwise D-W satisfies FE-ADM by loading the program "apply Λ₁ at each step", so its
  "free evolution" is the autonomous Φ running a loaded program. That is consistent with the
  owner's "genuine restriction" (the protocol is in `J_exact(A)`), but FE-ADM is then a
  compatibility assumption, not a sourcing test; "free evolution" means "autonomous Φ with a loaded
  setting".
- **BF (Born-form agreement), an assumption, needed only for the Born-form variant.** For every A,
  Λ, t, density ρ and effect E, Tr(E Φ^{(A,Λ)}_t(ρ)) = p_{M*}(E | s_Λ, ρ, t): the corpus's
  Born-form representation of the visible sector gives the model's operational law on coherent
  inputs and arbitrary readouts. This is the complex-kinematics representation (KIN, decision 4 of
  #914 c.6875046763) applied to M*, and the representational condition R-EX of #1508's NOTE.
- **J-coh.** The protocols π(ρ, Λ_t, E) with coherent ρ and readouts E outside the configuration
  basis lie beyond the native single-time interface (c.7064942473); the coherent variants use
  them, the population variants do not.

## 4. Proposition P-ST and its witness

**Lemma TC (tomographic completeness; mathematical/definitional, no OI assumption; layer X).** If L, L′ are linear maps on M_n(ℂ) with Tr(E L(ρ)) =
Tr(E L′(ρ)) for every density ρ and every effect E (0 ≤ E ≤ 1), then L = L′.
*Proof.* Put X = (L − L′)(ρ). Tr(E X) = 0 for every effect E; effects span the Hermitian matrices
over ℝ (every Hermitian H is a real multiple of an effect plus a multiple of 1, and 1 is an
effect), and Hermitian matrices span M_n(ℂ) over ℂ, so Tr(Y X) = 0 for every Y ∈ M_n(ℂ), whence
X = 0. Densities span M_n(ℂ) over ℂ by the same argument, so L − L′ vanishes on a spanning set and
is zero by linearity. ∎

**Proposition P-ST.** Let M* be an I★ witness (GA §2), with the T2 indexing of §2. Then:
1. under FE-ADM, M* satisfies **I★_st-coh^op** and **I★_st-pop^op**;
2. under FE-ADM and BF, M* satisfies **I★_st-coh** and **I★_st-pop** as typed in §2 (the
   Born-form variants, on the interface of `Sub:249` unchanged).

**Witness for ⇒ (§A.34).**
- *Step 1 (I-4 on a restricted protocol).* By PROT, π(ρ, Λ_t, E) ∈ `J_exact(A)`. I★'s clause I-4
  gives p_{M*}(1 | π(ρ, Λ_t, E), ρ) = Tr(√E Λ_t(ρ) √E) = Tr(E Λ_t(ρ)), under the label
  interpretation 𝓛_A of I★.
- *Step 2 (FE-ADM).* FE-ADM identifies π(ρ, Λ_t, E) under 𝓛_A with "load s_Λ, prepare ρ, evolve
  freely t steps, read {E, 1 − E}", so p_{M*}(E | s_Λ, ρ, t) = Tr(E Λ_t(ρ)) for every ρ, E, t.
- *Step 3 (TC).* Λ_t satisfies the defining identity of the operational channel, and by Lemma TC
  it is the only linear map that does, so Λ̂^{M*,(A,Λ)}_t = Λ_t: I★_st-coh^op. Restricting to
  ρ = |i⟩⟨i| and E = |j⟩⟨j| gives I★_st-pop^op.
- *Step 4 (BF).* BF gives Tr(E Φ^{(A,Λ)}_t(ρ)) = p_{M*}(E | s_Λ, ρ, t) = Tr(E Λ_t(ρ)) for every ρ, E;
  by Lemma TC, Φ^{(A,Λ)}_t = Λ_t: I★_st-coh, and on diagonal inputs and fixed-basis readouts
  I★_st-pop. ∎

Step 1 uses one clause of I★ (I-4) on one family of protocols; I-1 (one label interpretation)
makes 𝓛_A the same in every step; I-2★ makes s_Λ a setting fixed from typed data, not fitted.
**Re-check under the retyped setting.** Steps 1–3 use only the operational law
p_{M*}(E | s_Λ, ρ, t) and so hold under either typing (a) or (b). Step 4 uses BF with the family of
§2: under (b) the Born-form family carries the controller configuration |c_{s_Λ}⟩⟨c_{s_Λ}| and the
one prior ω_H, under (a) the state ω_{s_Λ}; in both it is linear in ρ, so Lemma TC applies as
before. P-ST holds under either typing.

**P-ST in the three questions.** Label **(I)**.
- Established: P-ST, items 1 and 2, with Lemma TC, at layer X on paper; not yet independently
  reviewed.
- Assumed: FE-ADM (which carries the encoding through 𝓛_A) (an operational assumption on the
  witness's label rule); for item 2, BF (KIN applied to M*); for the coherent variants, J-coh
  through the protocols with coherent ρ and arbitrary E; for the population variants, no J-coh.
  PROT is checked from EP:37–40, not assumed.
- Missing: a physical source for FE-ADM (that the native free evolution, with a loaded setting,
  realizes the requested Λ_t), and, for item 2, for BF. Both need a physical mechanism, not
  mathematics; FE-ADM is a form of the O1 question.

## 5. What fails when an assumption fails

| Dropped | What fails | Witness of the failure |
|---|---|---|
| T2 indexing (one prior per sector) | both GA variants unsatisfiable by every model for \|A\| ≥ 2 | §1 T2: one autonomous family per sector, two distinct targets |
| FE-ADM | I★ ⇏ any I★_st variant: I★ constrains only the label interpretation of Λ_t, not the free evolution | the stepwise D-W (GA §2.2, sketch, layer P): its label for Λ_t is an interpreter step driven by program fields; with no instruction loaded, free evolution leaves the stored state unchanged, so its free family is the identity, not Λ_t, while it meets I★ at trivial E |
| encoding mismatch (a failure of BF, not a separate assumption) | if the Born-form family is computed in the configuration basis while 𝓛_A uses a logical basis U, BF's equation compares two different bases and fails; item 1 is unaffected, and item 2 holds for the transported target Ad_U ∘ Λ_t ∘ Ad_{U†} only | #1508 review c.7065957850 CM-2: under a logical-basis change, Ad_Z becomes the Hadamard target |
| BF (item 2 only) | I★ ⇒ I★_st-coh^op still holds under FE-ADM, but not I★ ⇒ I★_st-coh in Born form | #1508 NOTE Lemma S1 ((I) on its (b)–(d); layer X): under its assumptions (a)–(e), the one-step Born-form channel of any bijection with a fixed countable hidden state is Ad of a monomial unitary, so a bijective M* whose operational channel is Ad_H has Born-form family ≠ Ad_H; BF then fails, and S1 shows BF and I-4 are jointly unsatisfiable for such models on non-monomial targets |
| J-coh | the coherent variants lose their content: on configuration inputs and fixed-basis readouts only the population variants are tested | — (scope statement) |

**Consequence for the satisfiability of item 2.** For bijective models with a fixed countable hidden
state, the hypotheses of item 2 are jointly unsatisfiable on non-monomial targets (S1); item 2 is
then vacuous for them, not false. It is non-vacuous for models whose ontic dynamics on the visible
span is a non-monomial unitary (for example, a target's own dilation (A ⊗ K, W, σ_K) with W in
place of φ̂, which is not a bijection model).

## 6. Proposed replacement text for GA §2.4

For the owner and the reviewer; GA is not edited here.

- Replace GA:260–261 ("the one model M* has a visible sector V_A encoded by enc_A, with its hidden
  prior, such that:") by: "the one model M* has a visible sector V_A encoded by enc_A and, from the
  typed data of Λ_A and fixed before comparison, a setting s_Λ of its controller fields loaded
  under EP:79, with its one hidden prior, such that, with s_Λ loaded:" (typing (b); under typing
  (a), "a preparation (ρ, s_Λ) whose hidden state may depend on s_Λ but not on ρ (EP:75)").
- Add the operational variants I★_st-coh^op and I★_st-pop^op of §2 beside the two Born-form
  variants.
- Replace GA:280–282 ("Both variants are strictly weaker than I★ ...") by: "I★ implies I★_st-coh^op
  and I★_st-pop^op under the assumption FE-ADM that free evolution with a loaded setting is
  the label interpretation of the requested channel; it implies the Born-form variants I★_st-coh and
  I★_st-pop under FE-ADM and BF (Proposition P-ST of the T1/T2 record). Without FE-ADM, I★
  implies no single-time variant; without BF, it implies the operational but not the Born-form
  coherent variant. c.7064942473: 'Equivalence based on single-time observations is weaker than
  equivalence under arbitrary quantum experiments.'"
- In GA §2.4's paragraph "Neither variant contains instruments ...", add: "the operational
  variants use the protocols π(ρ, Λ_t, E), which lie in `J_exact(A)` (PROT)".

## 7. Owner decisions

- **T-D1.** Adopt, amend or reject the T2 indexing by settings (§2), with typing (b), controller
  fields with one hidden prior, as written, or typing (a), a preparation setting under EP:75; or the
  per-(A, Λ) sector alternative.
- **T-D2.** Whether Stage 1 (c.7065620072, D6) uses the Born-form variants with BF stated, the
  operational variants, or both. The interface of `Sub:249` is unchanged in either case; the
  operational variants change the comparison quantity, not the interface.
- **T-D3.** Whether FE-ADM is recorded as an assumption of the staging (#1508 NOTE §9 asks the same
  of ID-FE).

## 8. What this record does not do

It edits no manuscript, no `endpoints.md`, no Issue body, nothing of #1503's branch and nothing of
#1477 or #1483. It runs no computation and dispatches no workflow. It adopts no premise, criterion or
interface, and it posts nothing on #1169.
