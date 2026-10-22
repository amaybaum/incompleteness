# Review: Kₙ form of M0 (commit 1dcbde1d, mc-node9 PREREG)

Exact checks: `kn_review_checks.py` / `.out` here (Fractions; independent enumeration; simplex with certificates and a
separate verifier). All ok.

## Depth-first verdicts

1. **Definition: holds.** The constraint space of an affine set is unique, so Kₙ is well defined. Isotropic
   subspaces: 4/31/514 at n = 1/2/3, matching Σ[n,k]₂∏(2ⁱ+1). Uniform states: 7/91/2467, and 150451 at n = 4 by
   formula. The polytope {p ≥ 0, Σp = 1, p_x ≤ ½} has exactly the six line states as vertices, so K₁ is as stated.
   Every isotropic state is an equal mixture of Lagrangian cosets, so 6/60/1080/36720 vertices suffice.
2. **Membership test: holds.** The test is affine Farkas over a finite generator list. Because every point lies on
   Σ = 1, a homogeneous y with y·v ≤ 0 on all generators and y·x > 0 is enough; no normalization is needed.
   Non-extreme generators are harmless; a functional certifies only against a *complete* list (B2).
3. **Convexity: holds for records, for P, and for whole pairs.** P(h|r) = Σ_P P(P|r) P(h|r,P) is a mixture, and so is
   heralding. Kₙ is closed under marginals onto any subset of whole pairs (exhaustive check at n = 2, 3). Keeping one
   coordinate of a pair leaves the domain of every Kₘ.
4. **Controls: fail with witness.** Two weaker checkers pass both new controls (B1).
5. **Scope: holds in substance.** No M1/M2 rule or decision rule uses Kₙ to define preparations. The text still
   carries stale support-form wording (N1, N2).
6. **§A.41: fails in part** (B2).

## Findings

**B1 (blocking): the controls do not separate Kₙ from weaker checkers.** Witness from the exact run:
- *Vertex-only checker* (accepts only a uniform isotropic state). It passes all three K-BIAS-MASK arms and K-COMP2.
  It wrongly rejects every nonuniform member, including the owner's heralded target (2/5, 2/5, 1/10, 1/10) in
  report9, so it would print a false "lost" after heralding.
- *"Support contains an isotropic support, and every single-toy marginal is in K₁."* It passes both controls but
  accepts a non-member.

Fix: add two rows to §5, to the "Required for retained" list (§4.1) and to I-19.
- **K-MIX2** (positive): ½U[q₁=q₂=0] + ½U[p₁=p₂=0]. Support 7, which is not affine, and it is in K₂ with weights ½, ½.
  The report9 target can serve as a second positive at n = 1.
- **K-CORR2** (countercontrol): support the Lagrangian coset q₁=q₂=0, with weights 3/8, 1/8, 1/8, 3/8 on
  p₁p₂ = 00, 01, 10, 11. Both marginals are in K₁ and the maximum point probability is 3/8, yet it is not in K₂. A
  separating functional is printed in the `.out` file.

**B2 (blocking, §A.41): the generator census and certificate checking have no checkpoints.** A separating functional is
valid only against the complete generator list, and Q5 allows n ≤ 4. Fix: add to I-19:
- the census printed and checked against the formula (7, 91, 2467, 150451; or the Lagrangian set 6, 60, 1080, 36720,
  with the reduction checked);
- each certificate re-verified by code that does not depend on the solver: λ ≥ 0, Σλ = 1, Σλv = x; or y·v ≤ 0 on every
  generator and y·x > 0;
- mutants, each named with the control that catches it: the Kₙ test replaced by support ≥ 2ⁿ (K-BIAS-MASK), by
  vertex-only (K-MIX2), or by support plus marginals (K-CORR2); and one generator dropped (the census).

**B3 (blocking, claim/evidence): `design/kn` does not deliver what the §5 rows cite it for.**
- The docstring of `in_Kn_by_support` claims the test is necessary and sufficient for uniform targets. That is false:
  uniform on three points at n = 1 is in K₁, and uniform on U[q₁=q₂=0] ∪ U[q₁=1, p₂=0] (not affine) is in K₂.
  K-COMP2's verdict survives only through the separate count of zero isotropic supports inside the set.
- K-BIAS-MASK is decided by the closed-form K₁ bound, and the script produces no certificates. The rows' "with a
  separating functional / mixture weights" is therefore not yet evidenced.

Fix: correct the docstring to say the test is sufficient for non-membership when no isotropic support lies inside the
set, and either emit verified certificates or mark them as owed by the engine.

**N1.** Lines 531–532 should be deleted: "Marginalizing one binary coordinate at most halves support, so discarding
never creates a support violation either". The restriction is no longer a support bound. The halving fact belongs to
the withdrawn joint form, and marginalizing P can only enlarge the support of h.

**N2. Support-form wording in §5.**
- K-CLN-A: "within the bound" should read "in K₁".
- K-POS: "hidden support ≥ 2" should read "P(h|r) ∈ K₁ with mixture weights". I verified this exactly, with weights,
  over both periods. K-POS-RET is outside K₁ in every fiber, as stated.
- K-REUSE arm 2: "toy support 2" should become K₁ membership (weights not checked; scripts are off the repository).
- The "lost" rows (K-SYMP, K-SYMP2, K-MEM4, K-MEM5, K-POS-RET, K-PIND, K-PEX) should print a separating functional,
  with support as a diagnostic. Add to §4: "every generator has support ≥ 2ⁿ, so support < 2ⁿ implies
  non-membership". This makes them consistent with the Kₙ form.
- K-CLN and K-CLN0 test the detector on a single bit with a stand-in restriction. Say that they do not exercise the
  Kₙ test.

**N3.** §4 should state that h consists of whole retained pairs, with n set to their number, and that discarding a
whole pair is covered by closure under marginals.

**N4.** "Physically available record" (§4) is undefined. Use "accessible record (§1.1)".

**N5.** The "Coarser records" bullet should name the mixture weights: P(r′|r), and P(P|r) rather than P(P) (cf.
KM-23).

**N6. Q14's qualifications.**
- (i) is enforced in substance by I-6 but not cross-referenced. Cite it in §4 and I-6.
- (ii): add to §4.1 *Scope* that "retained" does not show Kₙ ⊆ Prep, citing I-20.
- (iii) is already enforced by I-12.

**N7. Wording and diagnostics.** In Q14, write "arbitrarily close to 1 (99/100 tested)" instead of "up to 99/100".
In the rows, write "the Kₙ test classifies" instead of "Kₙ-M0 prints", since these are given distributions. Give
"Diagnostics, deciding nothing" a checkpoint in I-19: a static check that the verdict path reads no diagnostic.

## Verdict

**REVISE.**
The mathematics holds (definition, K₁, 7/91, Farkas, convexity). The new controls do not separate Kₙ from a
vertex-only or support-plus-marginals checker, the certificate path has no census or verification checkpoint, and the
cited script makes a false iff claim and emits no certificates. B1–B3 are small and mechanical; with them and N1–N8
applied, the change is acceptable.
