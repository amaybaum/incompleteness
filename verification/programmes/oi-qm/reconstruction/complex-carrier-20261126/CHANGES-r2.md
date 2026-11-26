# COMPLEX-CARRIER-1, lane 2: changes from r1 to r2

**WIP / UNVERIFIED. Model-written change record.** Base: REPORT.md at `77881879` (r1, committed
verbatim). r2 is REPORT-r2.md. PLAN.md and REPORT.md are unchanged. Authorization: owner decision
quoted in #1169 comment 7186638587 (amaybaum, 2026-11-26T08:28:18Z, item 7): "Approve findings
1–10, including the corrected counterexample, definite-B restriction, dimensional limitations and
range condition. Do not generalize the conclusions beyond their proved domain." Findings: the
independent review of r1, PR #1585 comment 7184957447. Evidence layer unchanged: mathematical
derivation on paper; nothing computed.

Each edited passage is mapped to its finding. No other passage was changed except the header
status line, which records the revision.

1. Finding 1 (Counterexample 9 and the §0 row (iii)).
   - §4.3: the background κ G⁻¹ ⊗ I_6 is replaced by Σ_b κ_b G⁻¹ ⊗ P_b with distinct κ_b > ε. The
     stabilizer is now shown to be strictly smaller than U(3)×U(2)×U(1), while Σ_n = 2γ Σ_b κ_b P_b
     has stabilizer exactly U(3)×U(2)×U(1).
   - The genericity condition becomes: absolute values of the coordinates in (−π, π] pairwise
     distinct, nonzero and not π. The reviewer's counterexample to the old condition is recorded.
   - Range stated: on T, abs(αμ) < 1/d or V_rest; on Z, abs(αμ) < 1/d, with αμ = 1/d on Z not
     claimed. The Z restriction is a writer narrowing: G⁻¹ is unbounded near k = 0 at αμ = 1/d.
   - The corpus anchor becomes SM:136 (the condensate clause as on-site O-equivariance) and SM:342.
   - Consequential edits: the §0 row (iii) for T and Z; the §4.7 status; the §5 H-cust
     (condensate) row, which now cites SM:136 and SM:374; §6 item 2; control X5, rewritten for the
     corrected state.
2. Finding 2 (§2.3, robustness).
   - "The structure" becomes "A structure".
   - Uniqueness is stated for B definite on each frequency eigenspace, with the reviewer's family
     S_t for B indefinite within a degenerate eigenspace.
   - The matched energy is written E_B = g(Bs·,·). It equals Q_B only for B = f(A) ⊗ C with C
     symmetric.
   - The headline is kept, with its proof: E_B positive definite iff B is g-positive, and then S = 1.
   - Consequential edit: the uniqueness item of §7's skepticism list.
3. Finding 3 (Proposition 6(c), Proposition 11 on Z).
   - The H_E quotient statement is restricted to d = 1, 2.
   - For d ≥ 3 the constant is neither an element of H_E nor 0 in it (Dirichlet space in p,
     discrete Sobolev embedding). In every d, l²-normalized near-uniform vectors tend to 0 in the
     E-norm.
   - Proposition 11 (Z) is corrected accordingly. The r1 claim that the background "is not in K" is
     replaced by "not examined here", since no proof for it is in hand.
4. Finding 4 (Theorem 1Z).
   - (a): the norm is stated as (1 + abs(cos θ))/sin θ, between s⁻¹ and 2s⁻¹.
   - The exclusion of spectrum beyond ±2 is done by the Riesz projection
     P_> = (F − λ_−(A))/(λ_+(A) − λ_−(A)), which has an isotropic, J-invariant range; the same
     argument applies in (b).
   - (c): "strong limits of polynomials" is replaced by the monotone-class argument via closedness,
     and the closed-involution step (1 − S)x/2 is made explicit.
5. Finding 5 (Proposition 2).
   - The range condition for (b)+(c) is added.
   - Q = 0 is extended to site-dependent site-local J.
6. Finding 6 (§4 introduction; Proposition 7 b-remark).
   - "S_n = 0 equals C_− = 0" is replaced by the correct directions: C_− = 0 iff all S_nm vanish,
     since (Φ_n)_n is a complex-linear isomorphism on T. C_− = 0 implies S_n = 0, but not
     conversely, and only that direction is used.
   - The vacuous reason in the b-remark is replaced by: x*x*ᵀ − (Jx*)(Jx*)ᵀ ≠ 0 for x* ≠ 0.
7. Finding 7 (Proposition 11 on T; §6 item 1).
   - "Acts trivially" is attributed to the extension chosen after Proposition 3, with O(6) as the
     null-sector compact symmetry.
   - "On all of phase space after H-ZM" becomes "on the reduced space obtained by the constraint
     w = 0 together with H-ZM (Proposition 5)".
8. Finding 8 (§2.6 and the b-remark).
   - Both are marked as carrier T only.
   - Consequential edits: the §0 "Needs b = 0?" cells for (i) and (iii); the §5 b = 0 row.
9. Finding 9 (Proposition 6(b); Proposition 4(a)).
   - 6(b): the graph norm is written with the matrix weight W = 1 + J_F(k)ᵀJ_F(k), and density
     follows from truncation and integrability of tr W for d ≥ 3.
   - 4(a): the cross-term step now uses positivity of C (C_xw antisymmetric, then 0).
10. Finding 10 (§2.5 Consequence; §6 item 2; §0 conclusion paragraph).
    - Reworded as a statement about the real-lift J: it is not a site-local structure, and a
      site-level reading of H-link's ⊗C^m is not supplied by it.
    - SM:505 is identified as the bijection-level carrier, out of scope, about which nothing is
      claimed.

Not changed: the conclusion's three-part classification (J sourced conditional on the lift;
separate bridge premise H-PF; named open hypothesis H-PF-int), the productivity verdict, the
open nodes and the node log. Each still holds after the corrections. No result is extended beyond
its proved domain.
