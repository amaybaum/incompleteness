*Independent proof review (PLAN.md step 9), recorded by the coordinator verbatim from the reviewer's report. `S` in paths is the session scratch directory, not retained. The scripts and outputs beside this file are the reviewer's; the coordinator re-ran them under `python3 -I -B`, and the re-run outputs are the `.out` files.*

# Independent review: unavoidable hidden predictive memory (Main.md:582–596) and the memory Corollary (Main.md:99)

Corpus at `eae01647`; Introduction at `4a260ca9`. This was a read-only review. I wrote the verdict
before I opened the audit directory `intro-corpus-audit-20261026/`. The comparison with the audit
comes last (§8).

## 0. Verdicts

| Object | Verdict |
|---|---|
| 1. Theorem (unavoidable hidden predictive memory), Main.md:582–590, parts (a)–(c), with the time-t identification | **ACCEPT WITH CHANGES** |
| 2. Corollary (Main.md:99; Intro "Corollary", L82), the (C1) derivation at Main.md:592, and Remark Main.md:596 | **ACCEPT WITH CHANGES** |
| **Overall** | **ACCEPT WITH CHANGES** |

All the mathematics I checked is correct. There is no counterexample to any stated claim. The time-t
identification holds, and §2 below proves it in a few lines. The changes are of four kinds:
- definitional consistency: "hidden prior" versus a correlated initial law, and a positive-probability qualifier;
- one imprecise derivation: "(C3) as (c) itself";
- broken cross-references in :596–:598;
- status and interpretive precision. In the bijective class, clauses (b) and the middle term of (c) are degenerate (§5.3). This does not affect correctness. It does affect what the Remarks at :592 and :594 claim.

Neither the Theorem nor the Corollary is wrong. The adjacent Remark at :594 *is* wrong in its
diagnosis (§6.1). It is not one of the review objects, but it sits inside the reviewed material.

## 1. Precise statements as proved

Notation. A *realization* is a tuple R = (C_H, φ, ν):
- C_H is a finite set;
- φ is a bijection of C_V × C_H;
- ν is a law on C_V × C_H, which may correlate the two coordinates.

Run it as follows: Z_0 ~ ν, Z_k = φ^k(Z_0), X_k = π_V Z_k and H_k = π_H Z_k. R is *faithful* to a law
P on C_V^{K+1} if the law of (X_0..X_K) equals P. Fix 1 ≤ t ≤ K−1. "Positive-probability (p, x)"
means P(X_<t = p, X_t = x) > 0. Set f_x(h) = π_V φ(x, h) and μ_{p,x} = Law(H_t | X_<t = p, X_t = x).

**Theorem (as proved; paper and kernel together).** For every faithful realization R of P and every
1 ≤ t ≤ K−1:
- (a) for positive-probability (p, x), P(X_{t+1} = · | p, x) = (f_x)_# μ_{p,x};
- (b) for positive-probability (p, x) and (p', x), ‖P(·|p,x) − P(·|p',x)‖_TV ≤ ‖μ_{p,x} − μ_{p',x}‖_TV;
- (c) M_t := I(X_<t; X_{t+1} | X_t) ≤ I(X_<t; H_t | X_t) ≤ log₂|C_H|, in bits.

The proof uses only that X_{t+1} is a function of (X_t, H_t). It does not use that φ is injective,
and it does not use how ν is structured.

**Corollary (as proved on paper).** Write W_t(P) for the visible statement "there exist
positive-probability (p, x) and (p', x) with P(·|p,x) ≠ P(·|p',x)". Write RR_t(R) for "there exist
positive-probability (p, x) and (p', x) with (f_x)_#μ_{p,x} ≠ (f_x)_#μ_{p',x}". Then, for t ≥ 1 and
K ≥ t+1:

  M_t > 0  ⇔  W_t(P)  ⇔  [for every faithful R: RR_t(R)].

- The first equivalence is the vanishing criterion for conditional mutual information.
- The second has two directions:
  - (⇒) Clause (a) gives RR_t(R) ⇔ W_t(P) in each faithful R.
  - (⇐) Take one faithful R, which exists by `S_imp_D`, and apply (a).

**(C1) as derived at :592.** If RR_t(R), then f_x is non-constant on supp μ_{p,x} ∪ supp μ_{p',x}.
So the hidden state influences X_{t+1} on positive-probability hidden states at time t. If f_x were
constant (= y) on that union, both pushforwards would be δ_y.

## 2. Check 1: the time-t identification (proof)

The kernel structure `HiddenMemory.Realization` is a bijection `step` together with an arbitrary
law `w` on Hist × V × H. Nothing in the kernel ties `w` to `step`, and no module links
`Equivalence.RevReal` to `HiddenMemory.Realization`. I checked this by grepping the imports and uses
of `HiddenMemory`: only `C3Necessity` and `CausalReadback` import it, and `CausalReadback` defines a
separate `RootedRealization`. The kernel theorem therefore holds for **every** joint law. The
missing step is only the instantiation.

**Lemma (identification).** Let R = (C_H, φ, ν) be faithful to P, with 1 ≤ t ≤ K−1. Put
Hist = C_V^t and define Ψ_t(z) = ((π_V φ^k z)_{k<t}, π_V φ^t z, π_H φ^t z). Take `step := φ` and
`w := (Ψ_t)_# ν`. Then:
1. w(p, x, h) = Pr(X_<t = p, X_t = x, H_t = h). This holds by definition.
2. On every sample, X_{t+1} = π_V φ(Z_t) = π_V φ(X_t, H_t) = `nextVis`(X_t, H_t) = `varNext`(Ψ_t(Z_0)). This uses only Z_{t+1} = φ(Z_t), that is, φ^{t+1} = φ ∘ φ^t.
3. By 2, the law of (`varHist`, `varNow`, `varNext`) under w is the pushforward of ν along (X_<t, X_t, X_{t+1}). By faithfulness this is the (<t, t, t+1)-marginal of P. `cmi` depends only on that triple marginal, so `memory R = M_t(P)`.
4. `histProb R p x` = P(X_<t = p, X_t = x). For positive-probability (p, x), `nextLaw R p x` = P(X_{t+1} = · | p, x) and `post R p x` = μ_{p,x}.

∎

The three issues the brief flagged:
- **Correlated initial laws.** The lemma uses no structure of ν. A product "visible prior × hidden prior" is a special case.
- **Hidden prior.** As for correlated initial laws: no assumption on ν enters.
- **Is H_t a deterministic function of (h_0, history)?** It is: H_t = π_H φ^t(x_0, h_0), and x_0 is part of the history. Clause (a) does not need this. It needs only X_{t+1} = f_{X_t}(H_t). For bijective φ the converse also holds: Z_0 = φ^{−t}(X_t, H_t), so X_<t is a function of (X_t, H_t). This has consequences (§5.3).

A time-dependent φ_k is covered too, with `step := φ_t`.

**Zero-probability histories.** Lean defines x/0 = 0, so for histProb = 0 both `post` and `nextLaw`
are the zero function. The paper leaves them undefined. The kernel clauses remain true there, since
both sides of (a) are 0. However, any "pair of posteriors with different pushforwards" must be
restricted to positive-probability histories. See CE-zero in §4.

**Probe.** `probe_identification.py` checks steps 2–4 exactly, in rational arithmetic:
- all 1,464 bijections at (n_V, |C_H|) ∈ {(2,2), (2,3), (3,2)};
- 7 initial laws each: uniform, a non-uniform product, a hidden point mass, a deterministic correlation h = x mod n_H, and 3 random correlated rational laws;
- horizon K = 3 and t ∈ {1, 2}, giving 20,496 cases.

It found 0 failures in ID1 (triple marginals) and ID2 (`nextLaw` against the path-law conditional).
Countercontrol CC1 in `probe_counter.py` reads X_{t+1} through φ² instead of φ, and the ID1 check
then fails in 40 of 48 cases. The check is live.

**Verdict on Check 1.** The identification holds. It is routine and is *not* formalized. Formalizing
it is cheap; §3 gives a fix.

## 3. Check 2: parts (a)–(c), line by line

**(a)** The proof reads "Determinism makes X_{t+1} a function of (X_t, H_t), so conditioning on p and
pushing μ_p through f_x IS the conditional law." This is correct. Explicitly, for positive (p, x):
P(X_{t+1} = y | p, x) = Σ_h Pr(H_t = h | p, x) · 1[f_x(h) = y] = ((f_x)_# μ_{p,x})(y). In the kernel,
`pushforward_identity` (HiddenMemory.lean:83) is this identity, proved by `Finset.sum_mul`, with
`nextLaw` computed from `w` and not posited.

**(b)** The proof reads "A deterministic map is a channel and total variation is monotone under
channels." This is correct and in the right direction:
‖(f_x)_#μ − (f_x)_#μ'‖_TV ≤ ‖μ − μ'‖_TV. The kernel proves it as `tv_marg_le` with the fibrewise
triangle inequality, and `distinguishability_floor` (:114) applies it.

**(c)** Two inequalities:
- The first inequality is correct. Given X_t, X_{t+1} = f_{X_t}(H_t), so the Markov chain X_<t → H_t → X_{t+1} holds conditionally on X_t, degenerately. Data processing gives I(X_<t; X_{t+1} | X_t) ≤ I(X_<t; H_t | X_t), and the direction is right. The kernel proves this as `cmi_le_of_deterministic` (FiniteEntropy.lean:383), exactly: I(A; C | B) − I(A; d(B,C) | B) = I(A; C | B, d) ≥ 0. I verified that `cmi w a b c` is I(a; c | b) (FiniteEntropy:352 with cmi3 at :189). So `memory R` = `cmiBits w varHist varNow varNext` is I(X_<t; X_{t+1} | X_t), as stated.
- The second inequality is also correct. I(A; C | B) ≤ H(C | B) ≤ H(C) ≤ log|C|. The paper writes I ≤ H(H_t) ≤ log₂|C_H|, which is correct, if slightly loose. The kernel proves it as `cmi_le_log_card` (:457), from H(A,B) ≤ H(A,B,C), subadditivity, and `entropy_le_log_card`. Bits come from dividing by log 2 (`cmiBits`), and the inequality survives because log 2 > 0.

The probe (`probe_identification.py`) checks A, B and C on all 20,496 cases with 0 failures. As an
independent control, M_t is computed two ways: by the kernel's entropy formula and by the
KL-divergence form. They agree within 1e-9 in every case.

**Defects in the statement at :582.** None affects correctness.
- (i) "with a hidden prior reproducing S" conflicts with :99, the Introduction (L30, L46) and `RevReal`, which all allow a correlated initial law on C_V × C_H. Read literally, "hidden prior" suggests a product law. The theorem holds for the general class, but the Corollary's converse needs the realization that `S_imp_D` supplies to lie in the class, and that realization's initial law is correlated. `probe_counter.py` confirms this: the replica's initial law is not a product in any trial. **Fix:** at :582, replace "with a hidden prior reproducing S" by "with an initial law on C_V × C_H, which may correlate the coordinates, under which the visible trajectory has the law of S".
- (ii) μ_p is defined as a conditional, so it needs P(p, x) > 0, and (b) needs that for both histories. **Fix:** add "positive-probability" in (a) and (b).
- (iii) The range of t is unstated. **Fix:** "1 ≤ t ≤ K−1" (or K ≥ t+1, as :592 says).

**The kernel citation inside :588 and :590.** It is accurate: "for a joint law of history, present and hidden state; reading a realization's time-t law as that joint law is a step not formalized". **Fix for that step:** add a Lean lemma `toRealization (R : RevReal V K) (t) (ht : t+1 ≤ K) : HiddenMemory.Realization (Fin t → V) V R.Hid` with `w := marg R.init Ψ_t`, together with `memory (toRealization R t) = cmiBits R.law (τ ↦ τ|<t) (τ ↦ τ t) (τ ↦ τ (t+1))`. The proof is `Function.iterate_succ_apply'` plus `marg_marg`.

## 4. Check 3: the Corollary's two directions (§A.34)

**Vanishing criterion.** I(A; C | B) = Σ_{(a,b): P(a,b)>0} P(a,b) · D(P_{C|a,b} ‖ P_{C|b}). This is
zero if and only if P_{C|a,b} = P_{C|b} for every positive (a, b), by the equality case of Gibbs'
inequality (D = 0 iff the two laws are equal; Cover–Thomas, information inequality and its corollary
for conditional mutual information).

Then ¬CI ⇔ W_t:
- If all next-step laws at a given x agree, they equal their mixture P(·|x).
- Conversely, if one of them differs from P(·|x), then, because P(·|x) is a convex combination of them, another one differs as well.

Status of the criterion:
- It is correct.
- In the Introduction it is **cited** ([CT06], which carries an unresolved `VERIFY` tag at Intro L295), and Main :99 and :580 call it "standard".
- It is **not proved** anywhere in the corpus.
- It is **not formalized**: FiniteEntropy has `cmi_nonneg` (non-strict Gibbs, `sum_mul_log_le`) and no equality case.

The two halves of the criterion are used asymmetrically:
- (⇒) needs only the easy half, CI ⇒ I = 0, which is algebra because every KL term is D(q‖q) = 0.
- (⇐) needs the strict half, I = 0 ⇒ CI, which is the equality case of log u ≤ u − 1.

**Direction (⇒): M_t > 0 ⇒ every faithful R has RR_t.** M_t > 0 gives ¬CI (easy half), which gives
W_t (mixture argument). In any faithful R, clause (a) turns the two differing conditionals into two
differing pushforwards. The two histories have positive probability, so the qualifier holds. The
direction is valid.

**Direction (⇐): [every faithful R has RR_t] ⇒ M_t > 0.** The hypothesis is universal, so it needs a
nonempty class. `S_imp_D` (Equivalence.lean:422) supplies R with `Hid` = clock × trajectory,
`init = marg P ι`, ι(τ) = (τ_0, (0, τ)), and a permutation extending the advance map. This is
faithful in the sense of :99 and the Introduction: a bijection of V × Hid, an initial law on
V × Hid, and `R.law = P`. It is *not* a product "hidden prior" (see the defect at :582 (i)). In that
R, RR_t together with (a) gives W_t, then ¬CI, then M_t > 0 (strict half). The direction is valid.
Under a literal product-prior reading of :582, existence would instead rest on the response-table
Extension at :498, which is proved on paper with a probe and is not in the kernel.

Both directions are also checked on every case of `probe_identification.py`. W_t ⇔ RR_t holds in
every realization, and W_t ⇔ (M_t > 1e-12) holds throughout, with 0 failures. The
`S_imp_D`-replica section of `probe_counter.py` rebuilds the clock-and-trajectory construction for
random rational laws and confirms that the law is reproduced exactly and that W_t = RR_t in the
replica.

**Defects.**
- **Intro L82 omits the qualifier.** It reads "a pair of posteriors with different pushforwards", without saying the posteriors belong to positive-probability histories ending at the same x. Under the kernel's 0/0 = 0 convention the unqualified form is **false**. In CE-zero (`probe_counter.py`) the law X_1 = X_0 with X_0 uniform is Markov (M_1 = 0), yet `nextLaw` at the zero-probability history (0) ending at x = 1 is the zero vector, while at (1) ending at x = 1 it is δ_1. **Fix:** "a pair of posteriors of positive-probability histories ending at the same x_t, with different pushforwards through f_{x_t}". Main :99 has "such posteriors", which inherits the qualifier, but only implicitly.
- **:592 states the converse from "some faithful realization".** It does not say that "every" yields "some" only because a faithful realization exists (`S_imp_D`), and it does not mention the vanishing criterion. **Fix:** add both, as :99 and :580 already do.
- **Abstract L12 counts unchecked steps.** It says "(each with one step not machine-checked)". That is accurate for Theorem 2. If "carries the visible memory in its hidden state" is meant as the Corollary, there are two unformalized steps: the identification and the strict vanishing criterion. Intro L82 and L209 state both correctly. **Fix:** make sure the abstract's clause refers to Theorem 2 only, or say "two steps".

**(C1) one-liner at :592.** It reads "(C1) because a hidden distinction invisible to f_x produces
identical pushforwards." The statement is true but elliptical. The operative contrapositive is: if
f_x is constant on supp μ_{p,x} ∪ supp μ_{p',x}, then the pushforwards coincide. So RR_t forces
f_x to be non-constant on positive-probability hidden states at (t, x). That is (C1) at step t, in
the stronger on-support form. The probe check C1 passes with 0 failures. **Fix:** state the
contrapositive explicitly.

**"(C3) as (c) itself" at :592 is imprecise.**
- (c) gives log₂|C_H| ≥ M_t. (C3) (§1.3 :78) is log₂|C_H| ≥ I* = sup_t I(X_<t; X_>t | X_t) ≥ M_t, which is stronger.
- CE-C3: take X_0, X_1, X_2 i.i.d. fair bits and X_3 = X_0. Then M_1 = 0, while I(X_0; X_2 X_3 | X_1) = 1 bit.
- (C3) follows from (c)'s *argument* applied to the whole future, which is `C3.c3_necessity` via `capacity_floor_of_fun`. It does not follow from (c) itself.
- Also, (C3) holds in **every** faithful realization, Markov ones included. It does not "follow from (C4)" in any sense beyond being unconditionally true.

**Fix:** "(C3) by the same data-processing argument applied to the whole visible future (C3 necessity; kernel `c3_necessity`)".

**Remark :596.**
- **Correct:** in a faithful realization, the (C4) gap ⇔ some M_k > 0, by (a) and the criterion. The "mediation" clause is automatic: by (a), differing next-step laws force differing posteriors.
- **Correct:** the bare form "non-Markovianity ⇔ a realization exists" is false, because Markov laws are realizable.
- **Defects:**
  - "(C4) coincides with clause (ii) itself" sits directly after a theorem whose clauses are (a)–(c). "(ii)" means the characterization theorem's (ii) at :520. **Fix:** "with condition (ii) of the characterization theorem".
  - "the theorem below" at :598 refers to the memory theorem, which is *above*, at :582. **Fix:** "the theorem above".
  - The enumeration "24, 720 and 720 realizations" (and the 1,464 at :590) covers bijections under the **uniform** joint prior only. I checked this in `primitive_probes.py` and `memory_probes.py`. They are not "every realization", which would include priors. My probe extends the check to 7 priors per bijection, including correlated ones. **Fix:** say "every bijection, under the uniform prior".

## 5. Check 4: counterexample attempts

### 5.1 Markov law (M_t = 0) whose every faithful realization has readout-relevant memory

**Impossible.** This is not just unfound; it is excluded. If RR_t held in even one faithful R, clause
(a) would give W_t, and the easy half of the criterion would then give M_t > 0. The probe has 5,304
cases with M_t = 0 and 0 with RR_t.

The only "counterexample" is CE-zero, which works only by dropping the positive-probability
qualifier (§4).

**What does occur.** In 656 cases M_t = 0 but I(X_<t; H_t | X_t) > 0. That is hidden memory which is
*not* readout-relevant. So the "readout-relevant" qualifier is essential, and §5.3 shows the
situation is generic.

### 5.2 Law with M_t > 0 and a faithful realization without readout-relevant memory

**Impossible**, by (a) in that realization together with the strict half of the criterion. The probe
has 15,192 cases with M_t > 0, and RR_t holds in all of them.

### 5.3 What the search did find: degeneracy in the bijective class (correctness unaffected)

For a bijective φ run from time 0, Z_0 = φ^{−t}(X_t, H_t). So X_<t is a deterministic function of
(X_t, H_t). This gives three consequences:
- **Disjoint supports.** For distinct positive-probability histories p ≠ p' ending at x, supp μ_{p,x} ∩ supp μ_{p',x} = ∅. So ‖μ_{p,x} − μ_{p',x}‖_TV = 1 always, and clause (b) is vacuous in the bijective class, since its right side is always 1.
- **The middle term of (c) is fixed.** I(X_<t; H_t | X_t) = H(X_<t | X_t) − H(X_<t | X_t, H_t) = H(X_<t | X_t), in every bijective realization, whatever its dimension or prior.
- **(c) becomes trivial.** It reads M_t ≤ H(X_<t | X_t) ≤ log₂|C_H|. The first inequality holds for any law.

Probe evidence:
- `probe_identification.py`, checks DIS and I(X<t;H|X)=H(X<t|X): 0 failures in 20,496 cases.
- Countercontrol CC2: a deterministic non-injective map g(x, h) = (h, 0) gives I(X_<2; H_2 | X_2) = 0, while H(X_<2 | X_2) = 2. So disjointness is a fact about bijectivity, and (a)–(c) survive without it.

## 6. Bearing on the broader framework

### 6.1 Remark :594 (the variational identity) is wrong in its diagnosis

It conjectures M_det := inf_R I(X_<t; H_t | X_t) = M_t over reversible deterministic completions. It
then says the fixed-dimension reading is false and that "any proof must therefore let the hidden
dimension vary".

By §5.3, every bijective completion has I(X_<t; H_t | X_t) = H(X_<t | X_t), whatever its dimension
or prior. So inf_R = H(X_<t | X_t). This exceeds M_t whenever H(X_<t | X_t, X_{t+1}) > 0.

Concrete case: i.i.d. fair coin, t = 1. M_1 = 0 but M_det = 1 bit. `probe_counter.py` shows this
for two different bijective realizations: the `S_imp_D` replica with |C_H| = 64, and a shift
register whose prior is independent of x_0.

So the conjecture is false over reversible completions at **every** hidden dimension. Letting the
dimension vary cannot help. The "1 of 15" count in `memory_probes.py` is exactly the set of
processes with H(X_<t | X_t, X_{t+1}) = 0. The only setting where the question is non-trivial is
non-injective objects such as the tail quotient T(P), and those are not reversible completions.

**Fix:** restate the remark as the identity I(X_<t; H_t | X_t) = H(X_<t | X_t) for reversible
completions, with the variational question posed only over non-injective predictive quotients.

### 6.2 (C2-structural) "as the retention required by (b)" (:592, :76)

In the bijective class, the distinction is total (TV = 1) at every time, for every law, Markov
included. The retention comes from reversibility. It is not evidence of memory.

The readback-relevant content is only (a), and it lives in the visible law. A pre-sampled response
table satisfies everything, as §1.3 itself acknowledges for (C4). So (b) does not by itself give a
write-then-persist reading.

### 6.3 (C3)

(C3) holds in every faithful realization. Reversibility yields the stronger bound
log₂|C_H| ≥ max_t H(X_<t | X_t) ≥ I*. So as a "diagnostic", (C3) has content only when |C_H| is
known independently, as in the horizon-capacity realization clause. The "saturated" statement at
:78 is a uniform-prior enumeration fact.

### 6.4 The Corollary is nearly definitional

By (a), RR_t(R) and W_t(P) are the same proposition, rewritten. The universal quantifier over
realizations adds nothing beyond (a) and the existence of one realization. This is correct, and
honest as stated, but it should not be presented as independent evidence that a substratum "stores"
memory (§7).

## 7. Kernel versus paper

| Step | Status |
|---|---|
| (a), (b), (c) for an arbitrary joint law `w` on Hist × V × H with X_{t+1} := π_V step(X_t, H_t) | **Kernel** (`pushforward_identity` :83, `tv_marg_le` :97, `distinguishability_floor` :114, `capacity_floor_of_fun` :150, `capacity_floor` :170, `unavoidable_hidden_predictive_memory` :185; FiniteEntropy `cmi_le_of_deterministic` :383, `cmi_le_log_card` :457, `cmi_nonneg` :372). I did not rebuild it: no `lean` or `lake` in this container. I inspected the source: no `sorry` or `admit`, and `#print axioms` is present. |
| Whole-future capacity (C3), m ≥ 2^{I*} | **Kernel** (`c3_necessity`, `card_hidden_ge_two_pow_Istar`), in the same joint-law form |
| Existence of a faithful realization of every law (correlated initial law) | **Kernel** (`S_imp_D`, Equivalence.lean:422) |
| Time-t identification: a `RevReal` run from time 0 induces the `Realization` whose `memory`, `nextLaw` and `post` are the path-law quantities | **Paper**, and only implicitly in Main. §2 gives the proof. Probe-checked here exactly. |
| Vanishing criterion: easy half (CI ⇒ I = 0) and strict half (I = 0 ⇒ CI) | **Cited / "standard"**: neither proved in the corpus nor formalized. `cmi_nonneg` has no equality case. |
| Corollary assembly (both directions) | **Paper** |
| Independent-prior realization for arbitrary real laws (needed only under a product-prior reading of :582) | **Paper and probe** (:498 Extension) |
| (C1) derivation, (C3) attribution, Remark :596 | **Paper** |

## 8. Correctness versus physical interpretation

**Correct mathematics.**
- (a)–(c) hold for every deterministic readout of an arbitrary joint law.
- The identification with a realization run from 0 is valid for every initial law.
- The Corollary is valid in both directions.
- (C1) follows on-support from RR_t.
- (C3) holds unconditionally, by the future-readout argument.

**Interpretation, not established by these proofs:**
- That "memory" is a *physical* property of a substratum's hidden sector. In the bijective class the hidden state encodes the entire visible past for **every** law, i.i.d. included (§5.3). The only part tied to non-Markovianity is the readout-relevant part, and by (a) that is a re-description of the visible witness.
- That a record is "written" and "persists". The response table pre-samples; (b) is vacuous in the bijective class.
- That (C1)–(C3) are diagnostics *caused* by memory. (C3) is unconditional.
- The posteriors μ_p are observer-conditional laws relative to the realization datum ν. A different faithful (φ, ν) gives different posteriors and the same readout-relevant pushforwards.

These do not undermine the theorems. They limit the physical reading of the Remarks at :592, :594
and :596, and of Intro L12 ("carries the visible memory in its hidden state").

## 9. Scripts

All are in `S/proofrev/memory/` and are run with `python3 -I -B`.
- `probe_identification.py`: 20,496 cases; checks ID1, ID2, A, B, C, DIS, I = H(X_<t|X_t), C1, the Corollary's two directions, and M_t computed by the entropy formula against the KL form. Prints `ALL CHECKS PASS`.
- `probe_counter.py`: countercontrols CC1 (live, 40/48) and CC2; constructions CE-zero, CE-C3, the `S_imp_D` replica (3 trials, law exact, initial law not a product, W = RR) and CE-594. Prints `ALL CONTROLS LIVE / CONSTRUCTIONS AS STATED`.

These are finite exhaustive checks at small size. The universal statements rest on the proofs in
§§2–4, not on the probes.

**A note on exactness.** All decisive equalities in the probes are exact `Fraction` comparisons:
- ID1, ID2, A, B, DIS, and the witness and RR tests.

Floating point appears in three places only. These are diagnostics, consistent with the Code Review
Rules. None of them carries a verdict:
- the CMI and entropy values;
- check C;
- the test "M_t > 1e-12". The exact counterpart of that test is the witness.

## 10. Comparison with the audit (read after the verdict above was written)

Source: branch `origin/audit/intro-corpus-20261026` at `a44003a0`, files `MATRIX.md` and
`FINDINGS.md`. I read them with `git show`; the working tree was not touched.

| Row | Audit | This review | Agreement |
|---|---|---|---|
| I-007 (memory is the discriminating content) | FAITHFUL, proved-paper | Correct, provided "memory" means *readout-relevant* memory. In the bijective class, hidden memory in the posterior sense is present for every law, Markov included (§5.3), so it does not discriminate. | Agree, with a qualification the audit does not record |
| I-008 (abstract: every deterministic completion carries the visible memory) | IMPRECISE; R-24 replaces "deterministic completion" with "reversible realization" | Agree that it is imprecise. Further point: under "reversible", the hidden state carries the *entire* past for every law, so the clause is true but non-discriminating. The discriminating form is readout-relevant memory, or M_t ≤ I(X_<t;H_t\|X_t). The theorem also does not need reversibility, so "faithful realization" (R-24's L189 wording) is more accurate than "reversible realization". | Agree; refine R-24's L12 text |
| I-093 to I-096 (Theorem 2 (a), (b), (c)-first, (c)-second) | FAITHFUL, proved-paper; the scope column records a correlated initial law and positive-probability posteriors | Correct; directions checked. The audit takes its definition from Main:97 and does not flag Main:582's "hidden prior" wording or its missing positive-probability qualifier and t range. I do (§3 fixes i–iii). Also: (b) is vacuous in the bijective class (TV = 1), and the middle term of (c) equals H(X_<t\|X_t). | Agree on the ratings; the audit misses the :582 wording defects and the degeneracy |
| I-097 (kernel form) | FAITHFUL, proved-kernel, certificate-checked | Matches my reading of the source. I did not rebuild it. | Agree |
| I-098 (identification not machine-checked) | FAITHFUL; its chain step 1 rates the written argument "proved" | Agree. Main gives the step only implicitly (proof of (a)). §2 gives the explicit proof and a cheap formalization path. The audit verified the identification itself only to traced-only level. | Agree; this review supplies the proof |
| I-099 (written proof exists) | FAITHFUL | Agree | Agree |
| I-100, I-100.a, I-100.b (Corollary and its two directions) | FAITHFUL | Both directions are valid (§4). I additionally flag Intro L82's missing "positive-probability histories ending at the same x_t" (CE-zero: false under the kernel's 0/0 convention). The audit's scope column has the qualifier, but its rating does not require it in the text. | Agree on validity; I would rate the L82 *wording* IMPRECISE, by the same reasoning as R-23 |
| I-101 (both directions use the vanishing criterion) | FAITHFUL | True. Refinement: the forward direction uses only the easy half (CI ⇒ I = 0); the converse needs the strict half (the equality case of Gibbs). | Agree |
| I-102 (\|C_H\| ≥ 2^{I*}) | IMPRECISE (R-22: I* undefined, no locator) | Agree. Also, reversibility gives the stronger log₂\|C_H\| ≥ max_t H(X_<t\|X_t) ≥ I* (§6.3). | Agree |
| I-103 (Pinsker bound) | IMPRECISE (R-03: "exact probes" tag on a floating-point probe) | Outside my objects, but I re-derived it. For two histories with weight ≥ p0 at TV ≥ δ, the triangle inequality against P(·\|x) and Pinsker (D ≥ 2TV² nats) give ≥ p0·δ² nats = p0δ²/ln2 bits. The bound is correct, and the issue is only the tag. | Agree |
| I-104 (four conditions named) | FAITHFUL | Agree | Agree |
| I-105, I-105.a ((C4) ⇔ M_t > 0) | IMPRECISE (R-23: time index, positive probability) | Agree. CE-zero shows that the positive-probability qualifier is load-bearing. | Agree |
| I-105.b | FAITHFUL | Agree | Agree |
| I-106 ((C4) carried in the hidden state of every faithful realization) | FAITHFUL | Mathematically correct. By (a) it is a re-description of the visible witness, not independent evidence of physical storage (§6.4, §8). | Agree on content; interpretive caveat not recorded by the audit |
| I-107 ((C1) follows from (C4)) | FAITHFUL | Correct, in the stronger on-support form. Main:592's one-liner is elliptical (§4). | Agree |
| I-108 ((C3) follows from (C4)) | FAITHFUL (cites `card_hidden_ge_two_pow_Istar` + Main:78) | **Disagree on the rating.** (C3) holds in every faithful realization *unconditionally*, so "follows from (C4)" is vacuously true and misdescribes the dependency. Main:592's "(C3) as (c) itself" is an insufficient derivation (CE-C3: M_1 = 0 while I* ≥ 1 bit). The audit's kernel citation is the correct source; Main:592's attribution is not. | Would rate IMPRECISE, and fix Main:592 |
| I-299 (L189: every deterministic completion carries the memory) | IMPRECISE (R-24) | Agree; same refinement as I-008. | Agree |

**Findings in this review that the audit does not have:**
1. **Identity in the bijective class.** I(X_<t; H_t | X_t) = H(X_<t | X_t) in every bijective realization run from time 0. Posterior supports are disjoint, so (b) is vacuous.
   - This **closes** Main:594's variational question over reversible completions, negatively, at every hidden dimension, and it shows that "any proof must let the hidden dimension vary" is wrong.
   - The audit's R-33 / CON-26 treat the fixed-dimension falsity as probe-only and record a "1 of 15" against "2 of 16" count discrepancy. I re-ran a copy of the audit's own `E2_memory_exact.py` in my directory. It reports 1 of 15 signature groups and 2 of 16 full laws attained, under uniform and under arbitrary priors alike. That is exactly what the identity predicts: attainment iff H(X_<t | X_t, X_{t+1}) = 0. So the discrepancy is a grouping difference (signature groups against full laws), not a disagreement between the two probes.
   - The fixed-dimension falsity is therefore a theorem, not only a probe result. R-33's softening to "fails in numerical probes" is unnecessary once the identity is stated.
2. **Main:582's "hidden prior"** conflicts with Main:99, Intro L30/L46 and `RevReal`. The converse of the Corollary needs the correlated-initial-law class, which is what `S_imp_D` supplies.
3. **Main:592's "(C3) as (c) itself"** is insufficient (CE-C3). It should cite the C3-necessity argument on the whole future.
4. **Main:596 and :598 cross-references.** "clause (ii)" is ambiguous next to (a)–(c), and "the theorem below" points to a theorem above. The enumerations at :590 and :596 cover the uniform prior only.
5. **Asymmetric use of the vanishing criterion** (easy half forward, strict half converse). Formalizing the strict half needs only the equality case of log u ≤ u − 1.

**Where the audit is ahead of this review:** R-22 (the undefined I* locator), R-24 (the second, Bell sense of "deterministic completion" at L136), R-03 (the probe-exactness tag), and R-25 (the abstract's "one step" count), which I flagged only conditionally.
