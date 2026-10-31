*Independent proof review (PLAN.md step 9), recorded by the coordinator verbatim from the reviewer's report. `S` in paths is the session scratch directory, not retained. The scripts and outputs beside this file are the reviewer's; the coordinator re-ran them under `python3 -I -B`, and the re-run outputs are the `.out` files.*

# Independent review: Theorem (CP-indivisibility, framework scope), `papers/Main.md:326` @ eae01647

Reviewer scope: Main.md:322 (Lemma, diagonal preservation), :326 (Theorem), :328 (proof),
:330 (scope remark, Hadamard pair), :334 (three-notions remark), :718 (ledger row); the
Introduction @ 4a260ca9 L102–106 (§3.1) and L251 (Appendix B card game); Intro §2.5 (the
definition of P-divisibility); Main §2.3; Lean `OIBridge/EquivalenceChain.lean` (`isDiag_Phi`);
the probe `papers/oi_lattice_code/foundations/c1_cp_scope_probes.py`; the book mirror
(`book/appendix-b-derivations.md:92–96`, `FULL.md:5859–5863`).
The audit directory `verification/audits/manuscript/intro-corpus-audit-20261026/` was not opened
before this verdict was written.

## Verdict: **ACCEPT WITH CHANGES**

The theorem is true and its four-line proof is correct as written, under the definitions the
paper states (a CPTP map Λ on the whole matrix algebra, and a row-stochastic divisor on the whole
simplex). The proof proves more than the theorem states. Nothing found is fatal. The changes
needed are in the precision of the statement: the hypothesis is cited to a section that does not
define it, and the prior is not said to be diagonal. They are also needed on three surrounding
status surfaces: the Main.md:330/:334 remarks, the Main.md:718 ledger row and the book mirror,
together with one sentence of the Introduction (L106). Each of those states something stronger
than the evidence supports, or something false by implication.

## 1. Precise statement as proved

Let `C_V`, `C_H` be finite, φ a bijection of `C_V × C_H`, and `U|v,h⟩ = |φ(v,h)⟩`. Let μ be a
probability vector on `C_H`, entering as the **diagonal** state `diag μ = Σ_h μ(h)|h⟩⟨h|`. Put
`Φ_t(ρ) = Tr_H[U^t (ρ ⊗ diag μ) U^{-t}]` and
`T(t)_{ij} = ⟨j|Φ_t(|i⟩⟨i|)|j⟩ = Σ_h μ(h)·[π_V φ^t(i,h) = j]`, the rooted population matrix
Γ_t of Intro §2.5, computed with the **same** μ.

**Proved.** Fix times `s < t` with `s ≥ 1`. Suppose no row-stochastic `M` satisfies
`T(t) = T(s) M`. Then no linear map Λ on `B(C^{C_V})` satisfies both of the following:

* (a) for every `k`, the diagonal of `Λ(|k⟩⟨k|)` is non-negative and sums to 1;
* (b) for every `i`, `Λ(Φ_s(|i⟩⟨i|))` and `Φ_t(|i⟩⟨i|)` have the same diagonal.

In particular, no CPTP map, and indeed no positive trace-preserving map, satisfies
`Φ_t = Λ ∘ Φ_s`. The family is therefore CP-indivisible, and also P-indivisible in the
quantum sense.

The only property of the family that the proof uses is that `Φ_s(|i⟩⟨i|)` is diagonal for each
basis projector, at the single time `s`. Diagonal preservation of `Φ_t` is not used. Neither are
the permutation structure beyond diagonal preservation, a uniform prior, invertibility, (C1)–(C4),
or complete positivity of Λ.

**Corollary (combining it with Main §2.3's stochastic-inverse lemma; checked exhaustively in my
scripts).** For a permutation dilation with diagonal prior, the populations are P-indivisible
exactly when some Γ_k with `1 ≤ k < L = ord φ` fails to be a permutation matrix. In that case
the pair `(k, L)` is an indivisible pair, since `Γ_L = I` would need a stochastic right inverse
of Γ_k. So the family is CP-indivisible at `(k, L)`. The converse of the Corollary is false (see
§3).

## 2. Definitions, and the line-by-line check

* **The class.** Permutation unitaries `U`, with a hidden state that is diagonal in the
  computational basis. Main:322 writes `μ_H` without saying it is diagonal. Main:280 uses the
  uniform `ρ_H`, the Intro (L106) says "diagonal hidden state", and the Lean `priorState μ` is
  `Matrix.diagonal μ` by definition. Read as "the channels that preserve diagonal states", the
  Intro's word "them" also makes the statement true, because the proof needs nothing beyond that
  property.
* **P-divisibility.** Intro §2.5 gives the definition: for all `s < t ≤ n`, some stochastic Λ
  satisfies `Γ_t = Γ_s Λ`. This is a global row-stochastic matrix, with rows indexed by `x_0`.
  Main §2.3, which the theorem cites, contains no explicit definition. It uses P-divisibility
  through total-variation contraction and the "stochastic divisor" phrasing, and its `T` is
  defined with the **uniform** prior.
* **CP-divisibility** (Main:326). A CPTP map Λ on the whole state space with
  `Φ_{t2} = Λ ∘ Φ_{t1}` holding on **all** inputs. This is the standard RHP definition. The
  proof uses the equality only on diagonal inputs, and positivity of Λ only on the projectors
  `|k⟩⟨k|`. The theorem as stated is therefore weaker than what is proved.
* **Proof, step 1.** `M_{kj} := ⟨j|Λ(|k⟩⟨k|)|j⟩` is stochastic. Correct: positivity gives
  `M ≥ 0` and trace preservation gives row sums equal to 1. Λ is defined on every `|k⟩⟨k|`,
  including those outside the range of `Φ_{t1}`, so rank deficiency or non-invertibility of
  `Φ_{t1}` or `T(t1)` does no harm. The rows of `M` for unreachable `k` are irrelevant but still
  stochastic.
* **Proof, step 2.** `Φ_{t1}(|i⟩⟨i|) = Σ_k T_{ik}(t1)|k⟩⟨k|`. This follows from the Lemma,
  together with the identification of the diagonal of `Φ_t(|i⟩⟨i|)` with `T(t)` (Born-form
  theorem, Main:284, applied to `φ^t`). Correct.
* **Proof, step 3.** `T_{ij}(t2) = ⟨j|Λ(Φ_{t1}(|i⟩⟨i|))|j⟩ = Σ_k T_{ik}(t1) M_{kj}`, by
  linearity. Correct. A Λ that works on the range of `Φ_{t1}` only ever enters through
  `Λ(Σ_k T_{ik}|k⟩⟨k|)`, so what it does outside the range is immaterial.
* **Contrapositive.** Correct. It holds pair by pair: the same `(t1, t2)` witnesses both
  failures. The theorem's `t1 > 0` is automatic, because `Γ_0 = I` is always divisible.
* **The Lemma (Main:322–324).** Correct. It is kernel-checked in general by `isDiag_Phi`, which
  is quantified over every φ and every `μ : H → ℂ`. Two notes:
  * Mathlib's `permMatrix ψ` sends `|j⟩` to `|ψ^{-1} j⟩` (this is what `permConj_apply` shows).
    Lean's `Phi φ` is therefore the manuscript's channel for `φ^{-1}`. This does not matter for
    `isDiag_Phi`, which is universal in φ. It would matter for any future Lean statement that
    identifies the populations of `Phi φ` with `T(t)` of φ.
  * I verified exhaustively and exactly the stronger property `D∘Φ_t = Φ_t∘D` (dephasing
    covariance): off-diagonal inputs go to off-diagonal outputs. In my runs there were 0 failures
    out of 4392 (bijection, prior) instances, across all `t` in the recurrence cycle.

## 3. Implications, and the remark at Main:330

* **Direction proved.** (2), at a pair `(s, t)`, implies no CPTP (indeed no PTP) Λ at `(s, t)`.
  The proof needs only that `Φ_s` preserves diagonals.
* **The converse fails, even inside the class.** Take the CNOT dilation `φ(v,h) = (v, h ⊕ v)`
  with any diagonal prior: `(1/2,1/2)`, `(1/3,2/3)` or `(1,0)`. Then `Φ_1` is complete dephasing
  and `Φ_2 = id`, so `T(1) = T(2) = I`, which is P-divisible. But no linear Λ satisfies
  `Λ∘Φ_1 = Φ_2`, because `Φ_1(|0⟩⟨1|) = 0 ≠ Φ_2(|0⟩⟨1|)`. The family is CP-indivisible
  (`exact_examples.py` X2, exact). The exhaustive search finds 10,504 such
  (P-divisible, linearly incompatible) time pairs.
* **What the :330 remark shows.** It does not show the converse. It shows that the forward
  direction can fail outside the class.
  * **Verified exactly.** `Ad_H` is rational as a superoperator, since its entries are ±1/2.
    Then `Ad_H∘Ad_H = id`, and the Choi matrix of `Ad_H` is PSD (exact LDLᵀ) and trace
    preserving.
  * **Divisibility.** The family `{id, Ad_H, id}` at `t = 0, 1, 2` is CP-divisible for every
    pair: `(0, t)` trivially, and `(1, 2)` with `Λ = Ad_H`.
  * **Populations.** They are `J/2 → I`, and the exact Farkas certificate shows there is no
    stochastic divisor.
  * **Class.** `Ad_H` maps `|0⟩⟨0|` to a non-diagonal state, so it lies outside the class.
  * The remark is correct (`exact_examples.py` X1).
* **Diagonal preservation is sufficient, not necessary, for the forward implication.** Take
  `Φ_{t1}(ρ) = tr(ρ)|+⟩⟨+|` and `Φ_{t2} = id`. `Φ_{t1}` is not diagonal-preserving, the
  populations `J/2 → I` are P-indivisible, and the pair is CP-indivisible, since `Φ_{t1}` is not
  injective. So Main:334's "the exact conditions under which (2) constrains a quantum
  intermediate map" overstates. The sufficient condition is presented as exact.

## 4. Gaps and errors

None is in the proof itself. All are in the statement or in its surroundings.

| # | Location | Issue | Why it matters | Fix |
|---|---|---|---|---|
| G1 | Main:326, "the P-indivisibility of §2.3" | §2.3 states no definition of P-divisibility, and its `T` uses the uniform prior, whereas the Lemma's family has a general `μ_H`. | The theorem's hypothesis is not pinned down in the paper that states it. Its precise form lives in Intro §2.5. | State it inline: "if for some `t2 > t1` no row-stochastic `M` satisfies `T(t2) = T(t1)M`, with `T(t)_{ij} = ⟨j|Φ_t(|i⟩⟨i|)|j⟩` for the same μ, …". Optionally record the stronger conclusion (no positive TP Λ) and the Corollary (witness pair `(k, ord φ)`). |
| G2 | Main:322, `μ_H` | Diagonality of the hidden state is not stated, and it is load-bearing. With `U = SWAP` and hidden `|+⟩`, `Φ(ρ) = |+⟩⟨+|`, which is not diagonal. | Without it the Lemma is false. | Write `μ_H = Σ_h μ(h)|h⟩⟨h|`, as Lean and Main §3.4 do. |
| G3 | Main:324, "(Certified exactly for t = 1, …, 6 in `c1_cp_scope_probes.py`)" | The probe (P3) checks one random bijection at `(n_V, n_H) = (3, 4)`, with uniform prior and a dense check on one basis input. That is an instance, not a certification of the Lemma. The general proof is the kernel's `isDiag_Phi`, which is not cited here. The coverage ledger lists the Theorem as `kernel: P`, with this probe as its evidence, but the probe does not test the Theorem's implication. | Verification layers are conflated (AGENTS: Lean, exhaustive and instance checks are distinct). The Theorem in fact rests on its paper proof, which is correct. | Cite `isDiag_Phi` (`OIBridge/EquivalenceChain.lean`) at the Lemma, and describe the probe as an instance check. |
| G4 | Main:330, "must therefore not be equated with open-system non-Markovianity outside the diagonal-preserving class" | The wording implies that inside the class the two may be equated. They may not: the converse fails inside the class (CNOT dilation, §3). | The status surface reads stronger than what is proved. | "…must not be equated with open-system non-Markovianity: inside the diagonal-preserving class it implies CP-indivisibility, and the converse fails even there (dephasing followed by identity)." |
| G5 | Main:334, "the exact conditions under which (2) constrains a quantum intermediate map" | Diagonal preservation of `Φ_{t1}` is sufficient, not necessary (the counterexample in §3). | A necessary/sufficient slip. | "a sufficient condition". |
| G6 | Main:718, ledger row "CP-indivisibility of {Φ_t} — Proved for the framework's diagonal-preserving (permutation-dilation) channels" | The antecedent is dropped, so a conditional is stated as unconditional. A decoupled dilation `φ = σ × τ` gives `Φ_t = Ad_{P_σ^t}`, a unitary group, which is CP-divisible. | The row states a status stronger than its site, which the table's own preamble forbids. | "P-indivisible populations ⇒ CP-indivisibility: proved for permutation-dilation (diagonal-preserving) channels; fails for general CPTP families (Hadamard)". Or: "CP-indivisible whenever some rooted Γ_k is non-permutation, witness `(k, ord φ)`". |
| G7 | Book `appendix-b-derivations.md:92` = `FULL.md:5859` (Theorem B.2.5) | The hypothesis is "the P-indivisibility of the **substratum dynamics** (under C1–C4)". P-indivisibility is a property of the visible population family, not of the bijection. "Under C1–C4" suggests that C1–C4 supply the hypothesis, when they give only global, recurrence-cycle indivisibility (via C4, or a non-permutation Γ_k, plus recurrence). The proof also says "uniform ancilla", which is narrower than Main. The two book copies agree (checked by `diff`); the book disagrees with Main's statement. | §A.25 mirror drift: the book's statement differs from the paper's. | Mirror Main's (corrected) statement in both book files. |
| G8 | Book `appendix-b-derivations.md:96` = `FULL.md:5863` | "Information backflow at observable timescales" sits directly after the sentence on the BLP trace-distance criterion. The corpus's observable-timescale result is conditional-mutual-information backflow (notion (1), Main §2.3 readback lemma), not BLP backflow. Indivisibility is only global (Intro §3.1, L102). | It invites reading a notion (1) result as notion (3). | Say "conditional-memory (accessible) backflow". |
| G9 | Intro L106, "no unconditional implication holds among them" | Main:334 says only that none "is asserted". (2) ⇒ "`M_t > 0` for some `t`" does hold unconditionally for a full-support initial law: Markov ⇒ P-divisible, as Main:606 itself states. I checked this exhaustively on all 3,924 P-indivisible instances (`memory_check.py`). | A negative claim stronger than the corpus supports, which contradicts Main:606 when (1) is read existentially in `t`. | "no unconditional implication is asserted among them beyond (2) ⇒ memory at some time" (or Main's wording). Also "Outside that class the implication fails" → "need not hold". |

## 5. Counterexample search: attempts and outcomes

Scripts are in `S/proofrev/cp/`.
All were run with `python3 -I -B`.

* **`exact_lp.py`.** Exact rational LP feasibility. Every verdict is re-checked against an exact
  certificate: the primal point, or a Farkas vector. The self-test has controls with known
  answers, including an invertible pair whose unique divisor has a negative entry. The self-test
  passes.
* **`cp_search.py`** (exact, exhaustive).
  * **Domain.** Every bijection at `(|V|, |H|) = (2,2), (2,3), (3,2)`, giving 24, 720 and 720
    bijections. Priors were `(1/2,1/2)`, `(1/3,2/3)` and `(1,0)` for `|H| = 2`, and
    `(1/3,1/3,1/3)`, `(1/2,1/3,1/6)` and `(1/2,1/2,0)` for `|H| = 3`. Every ordered time pair was
    taken modulo the order of φ, with `s ≢ 0`, giving 62,199 pairs.
  * **Results.**
    * Diagonal preservation, dephasing covariance, and agreement of the populations with the
      classical count: 0 failures.
    * P-indivisible pairs: 34,444 (106 / 13,886 / 20,452). For every one, the Farkas vector
      lifts to a non-negative diagonal Choi functional that separates every CPTP Λ (34,444 of
      34,444 verified). This is the theorem's proof turned into exact certificates. It is not
      independent of the proof.
    * Converse failures (P-divisible, but no linear Λ, hence exactly CP-indivisible): 10,504.
    * P-indivisible pairs that are nonetheless divisible in the image-only classical sense (L
      defined only on rowspan `T(s)`, non-negative on `S ∩ ℝⁿ₊`): 0.
* **`cp_numeric.py`** (floating point; independent of the proof). Distance between the PSD Choi
  cone and the affine set of TP Λ with `Λ∘Φ_s = Φ_t`, by alternating projections over 1,500
  iterations, on all 8,575 distinct `(Φ_s, Φ_t)` pairs.
  * **Controls behave as expected.**
    * Hadamard pair: gap 7.6e-16.
    * Identity followed by dephasing: gap 0.
    * Identity to transpose (positive, not CP): gap 1.00.
    * Dephasing followed by identity: no linear Λ exists.
  * **The 5,938 distinct P-indivisible pairs.**
    * 4,484 are **exactly** CP-indivisible by linear incompatibility (`ker Φ_s ⊄ ker Φ_t`). This
      certificate is independent of the paper's proof.
    * The other 1,454 have numerical gaps of at least 5.6e-2. Of these, 452 were first reported
      as `inf` by a pseudo-inverse tolerance artifact and were recomputed with
      `cp_numeric_recheck.py`; their minimum gap is 0.54.
    * **No P-indivisible pair has a gap below 1e-3.**
  * **The 2,637 P-divisible pairs.**
    * 1,261 are exactly CP-indivisible: these are converse failures.
    * 1,159 (1,010 + 149 re-checked) are numerically CP-divisible (gap below 1e-4).
    * 215 (177 + 38) are numerically CP-indivisible (gap above 1e-3).
    * 2 are ambiguous.
  * Logs: `numeric.log`, and the re-check output.
* **`exact_examples.py`** (exact). X1: the Hadamard remark. X2: converse failure inside the class
  (CNOT). X3: the Intro Appendix B card game. There `Φ_1 = tr(·)I/2` and `Φ_2 = id`; the
  populations are P-indivisible and the pair is CP-indivisible, both through the lift and through
  linear incompatibility. This confirms the Intro's L251 use.
* **`recurrence_witness.py`** (exact). On all 4,392 instances, the populations are P-indivisible
  exactly when some Γ_k is non-permutation, and `(k, ord φ)` is then an indivisible pair.
* **`memory_check.py`** (exact). (2) ⇒ ∃t `M_t > 0` on all 3,924 P-indivisible instances, with
  `X_0` uniform. This bears on G9.

**Outcome.** No counterexample exists, and none can, given the proof. The search is a consistency
control and confirms that every premise holds on the whole small-size domain.

**What is numerical.** Only the SDP distance column, used for 1,454 of the 5,938 distinct
P-indivisible pairs and for the P-divisible classification. A rigorous SDP certificate was not
needed. The exact lift certificate settles every P-indivisible pair, and the exact
linear-incompatibility certificate settles 4,484 of them independently of the proof.

## 6. Assumptions (all used, all stated or implied in the corpus)

* `C_V` and `C_H` are finite, and φ is a bijection.
* The hidden state is diagonal (a probability vector μ), the same μ in `Φ_t` and in `T(t)`.
  Full support is not needed.
* Time is discrete. Γ_t is rooted at 0, with an uncorrelated product initial state `ρ ⊗ diag μ`.
* CP-divisibility in the global sense: Λ is CPTP on all of `B(C^{C_V})`. P-divisibility in the
  global sense: `M` is row-stochastic on the whole simplex.
* If either notion were weakened to intermediate maps defined only on the range of `Φ_{t1}`, as is
  sometimes done for non-invertible maps, the implication would have to be re-proved with the
  matching image-restricted classical notion. The classical image-restricted notion is strictly
  weaker in general. An abstract example: rows `(½,½,0)` and `(0,½,½)` mapped to `e_1` and
  `e_2`. My search found no instance of that gap in the permutation class at these sizes. The
  corpus uses the global notions throughout (Intro §2.5, Main:326), so this is a scope note, not
  a defect.

## 7. Proof correctness versus physical interpretation

**Mathematics (proved).** Inside the diagonal-preserving class, failure of a stochastic divisor
for the rooted populations at `(s, t)` excludes every positive trace-preserving intermediate map at
`(s, t)`, CPTP maps included.

**Interpretation.** The corpus attaches to this "(2) implies CP-indivisibility", that is, RHP
non-Markovianity of the dilated family. Main:330 explicitly warns that P-indivisibility is not
quantum non-Markovianity in general. As a statement about RHP CP-indivisibility the claim is
supported. Three limits should be kept in view:

1. **The witness is entirely classical.** Λ already fails on the diagonal subalgebra, and
   positivity on `|k⟩⟨k|` is all that is used. The CP/P distinction, which is the genuinely
   quantum content of the RHP criterion, is never exercised. Coherences play no role, and any
   classical stochastic process embedded diagonally (for example a classical channel after
   complete dephasing) behaves the same way. The theorem says the classical indivisibility is
   not removed by the quantum representation. It is not evidence of quantum memory, and should
   not be read as such.
2. **Inputs other than diagonal states.** What `Φ_t` means physically on non-diagonal inputs
   depends on coherent preparation, which Main's comparison of routes lists as level three, open.
   The theorem does not depend on it.
3. **The timescale is not observable.** For the framework's finite reversible representatives
   the guaranteed witness pair is `(k, L)`, with `L` the recurrence time. The theorem does not
   deliver CP-indivisibility on accessible windows, consistent with Intro §3.1's statement that
   the indivisibility is global. For the recurrence witness, BLP trace-distance backflow also
   occurs, because the trace distance of diagonal outputs equals the total-variation distance of
   the rows (Main §2.3, Step 3). For a general P-indivisible pair it need not.

## 8. Bearing on the broader framework

* **The Corollary.** "C1 (hidden influence within the recurrence cycle) ⇔ some Γ_k is
  non-permutation ⇔ populations P-indivisible ⇒ CP-indivisible at `(k, ord φ)`". If all Γ_k are
  permutations, then `x_k` is a fixed function of `x_0` for every `h`, so the hidden sector has no
  influence. This is a clean framework-level form that Main could state. Its converse fails
  (CNOT).
* **No route from this theorem to quantum structure.** CP-indivisibility proved this way adds no
  quantum structure beyond the classical population law. This agrees with Main:334's
  three-notions discipline, and it means no "quantum non-Markovianity" claim downstream should
  cite this theorem as evidence of anything beyond notion (2).
* **Propagation.** G4–G9 are status surfaces: Main:330, :334 and :718, the two book copies, and
  Intro L106. Under §A.25 they should be corrected together.

## 9. Comparison with the audit (I-128, I-129, FINDINGS)

This section was written after the verdict above. Source: `MATRIX.md`, `FINDINGS.md` and
`CONSISTENCY.md` at the audit commit `a44003a02`, read with `git show`.

* **I-128** (L106: "Tracing out a permutation unitary from a diagonal hidden state gives
  diagonal-preserving channels"; `isDiag_Phi`; proved-kernel; FAITHFUL; certificate-checked).
  **Agree.** One addition: `isDiag_Phi` covers every φ and every `μ : H → ℂ`, so it is stronger
  than the claim, but the Lean `Phi φ` is the manuscript's channel for `φ^{-1}` (§2). The
  Introduction's wording ("diagonal hidden state") is more precise than Main:322 (G2), so the
  row is correctly FAITHFUL to its Lean anchor.
* **I-129** (L106: "For diagonal-preserving channel families, P-indivisibility of populations
  implies CP-indivisibility"; Main:326; proved-paper; FAITHFUL; mirror appendix-b:92;
  traced-only). **Agree on the verdict.** I verified the proof line by line and in exact
  exhaustive instances, so this review upgrades the row's "traced-only" basis to an independent
  proof check. The row's broader class ("diagonal-preserving channel families") is correct, and
  in fact only `Φ_{t1}` needs to preserve diagonals. The row also understates the conclusion:
  no positive trace-preserving Λ exists either.
* **FINDINGS on I-128/I-129.** There are none, which is consistent with FAITHFUL.
* **Related findings that this review reproduces independently.**
  * R-02 / CON-42 (Intro L106 "no unconditional implication holds" is false, since (2) ⇒ ∃t
    `M_t > 0`) is my G9. It covers row I-127 (OVERCLAIM). I agree, and I checked it exhaustively
    (`memory_check.py`).
  * CON-30 (appendix B.2.5 scope: "P-indivisibility of the substratum dynamics (under C1–C4)")
    is my G7. I agree. The audit rates it low, and I would keep it low, because the proof is
    unaffected.
* **Not found in the audit.**
  * G4: the Main:330 implicature that the two notions may be equated inside the class, refuted
    by the converse failure inside the class (CNOT dilation).
  * G5: Main:334 "exact conditions", where diagonal preservation is only sufficient.
  * G6: the Main:718 ledger row, which drops the P-indivisibility antecedent.
  * G3: the Lemma's "certified exactly" names an instance probe rather than `isDiag_Phi`, and the
    coverage ledger's evidence for the Theorem is a probe that does not test the implication.
  * G8: the book's "information backflow at observable timescales" sits beside BLP.
  * G2: Main:322 does not say `μ_H` is diagonal.

  None is in the Introduction itself. G4, G5 and G6 bear on the L106 claim's anchor site and its
  status surfaces.
* **I-130** (Hadamard; FAITHFUL; reproduced). Agree. The remark shows failure of the forward
  implication outside the class, not the converse.
* **I-375** (card game CP-indivisible, Main:326). Agree. It is confirmed exactly, both through
  the theorem and independently, since `Φ_1` is constant and `Φ_2 = id`.
