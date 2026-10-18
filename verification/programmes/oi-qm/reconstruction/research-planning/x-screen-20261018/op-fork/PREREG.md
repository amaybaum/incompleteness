# OP-weak vs OP-strong purification fork: preregistration

Research only. No native round, no F, no merge, no promotion of any X, no status change. This is consistency-axis work
(§A.23). Parent: the X screen `../REPORT.md` at `fb55f654`, "Recommended next investigation" (:128–136).

This file was written before any probe in `probes/` was run. The candidate cones in §4 were chosen by written analysis
before computation. The rule below decides on measured certificates, not on expected values.

## 1. Domain and retained premises

- Pair tables on two tokens, identified with 4×4 Hermitian matrices by the Pauli dictionary (`dict` [AT]). The token
  state space is the Euclidean ball (`TransitiveBody.eball 3` [AT]), that is, the qubit Bloch ball.
- K is a closed convex cone with SEP ⊆ K ⊆ maxCone (`hH1`, `hadd`, `hsmul`, `hmax` of
  `pairCone_eq_Q3_of_drive_maxCone` [AT]). maxCone is the dual of SEP.
- A *pure state* of K is a trace-one element on an extreme ray of K. m1 and m2 are the token-1 and token-2 marginals.
- No operation is assumed available or state-preserving. The native CNOT, the native local permutations and PC are
  used only as recorded side properties of a cone. They are never premises of the fork.

## 2. Clauses

- **E (existence).** Every token state ρ in the ball is m1 of some pure state of K.
- **R (relating set).** R = O(3), the affine automorphisms of the token-2 ball that fix its centre. Source: the
  retained premise that the token state space is the ball; nothing is said about availability. On tables, g ∈ SO(3)
  acts as Ad_{I⊗u}, and g ∈ O(3)∖SO(3) acts as Γ∘Ad_{I⊗u}, where Γ is the token-2 partial transpose. A probe
  checks this identification. It is a continuous set, but it is a set of symmetries of the given ball, not an
  operational resource. OP-weak asserts no procedure is available, so no continuous phase resource is imported.
- **U-weak (relation-only uniqueness).** For any two pure states ω, ω′ of K with m1(ω) = m1(ω′), there is g ∈ R with
  ω′ = (id⊗g)ω.
- **U-strong.** U-weak, with g required to satisfy (id⊗g)K = K.
- **TS (trivial-system clause).** `../REPORT.md` names this clause but defines it nowhere. A search of this branch
  and of the research branches turned up no definition. Two readings are tested:
  - TS-a: a pure state whose m1 is pure is a product of pure states;
  - TS-b: every product of pure token states is a pure state of K.

  Any other reading is out of scope and is recorded as [UP].
- **OP-weak** = E ∧ U-weak. **OP-strong** = E ∧ U-strong. The TS readings are recorded alongside each.

Variant, record-only: **U-weak-SO** restricts R to SO(3). That restriction imports a choice (connectedness, or
quantum compatibility), so the variant is tested but never used to decide the fork.

## 3. Decision rule (frozen)

This is the rule from `../REPORT.md` (:132–134), restated without change.

- **KEEP.** A written argument, with green exact certificates, shows OP-weak ⇒ OP-strong on the domain, or OP-weak
  ⇒ K ∈ {Q3, Γ(Q3)}. Next step: source OP from the lifted substratum purification (Main.md:602), with
  `fiber_freedom` as the kill test.
- **RETIRE.** An exact domain cone K ∉ {Q3, Γ(Q3)} satisfies E and U-weak at every marginal. This needs green exact
  certificates for:
  - (i) the domain inclusions;
  - (ii) the classification of K's pure states;
  - (iii) existence at every marginal, as a symbolic statement over the whole ball;
  - (iv) U-weak at every marginal;
  - (v) K ≠ Q3 and K ≠ Γ(Q3).
- **UNDECIDED.** Neither of the above.

Universal claims are written arguments, tagged [WA]; their exact certificates are tagged [EC]. A finite set of
instances is never reported as a theorem for a class.

**Verdict text.** `probes/replay.py` generates it from the `RESULT` lines the probes print. It is void if any control
in §5 fails.

**Wording (owner scope clarification, PR #864, comment 6247198574).** This arrived before this file was written and
is recorded here at owner direction. It changes no test and no rule.

- A RETIRE outcome is worded as **"OP-weak insufficient alone as a standalone cone-selection condition under the
  tested premises"**. It is not a global rejection of purification as a component of a later, independently sourced
  X, unless a separate result establishes that.
- A screen that finds no countermodel is not a uniqueness theorem.
- A KEEP outcome leaves sourcing from OI, G2, G3 and G6 open.

## 4. Nodes (depth-first; each closed by an explicit check)

- **N1. Extreme rays of maxCone.** Are they exactly the rank-one PSD tables and their Γ-images?
  - Method: the zero-set first-order nullspace, exact over ℚ(i), at B, Γ(B) and P₀₀. Each nullspace must be
    one-dimensional. Transport to all rank-one PSD tables by local congruence [WA].
  - Consequence used later: any rank-one PSD or Γ(rank-one) element of a domain cone is extreme in it.
- **N2. Lemma: sufficient condition for U-weak.** If every extreme ray of K is rank-one PSD or a Γ-image of one,
  then U-weak holds. [WA]: Uhlmann [L], plus the identification of R from §2.
- **N3. K(Z_F) = (Q3 ∩ Z_F\*) + cone(Z_F).** Three parts:
  - full classification of its pure states;
  - existence at every marginal, symbolic over the whole ball;
  - U-weak at every marginal; U-strong is expected to fail.
- **N4. L = Q3 ∩ Z_F\*.** The same checks as N3, plus U-weak-SO.
- **N5. K_Γ = Q3 + ℝ₊Γ(B).** The simplest cone with one added ray. Same checks.
- **N6. maxCone.** OP-strong without TS, and the TS readings. Record-only: this bears on whether OP-strong itself
  reduces to {Q3, Γ(Q3)}.
- **N7. Side properties, record-only.** For each cone in N3–N5: PC, MI, invariance under the 24 native
  permutations, and token symmetry.

## 5. Controls (all must be green, or the verdict is void)

- **C1 positive.** Q3 and Γ(Q3) pass E, U-weak and U-strong under the same classification and existence code.
- **C2 negative, existence can fail.**
  - K_B = SEP + ℝ₊B fails E at diag(1/4, 3/4);
  - SEP fails E at I/2;
  - the existence routine reports failure on a mutated cut set whose premise is violated.
- **C3 negative, U-weak can fail.** K_mut = Q3 + ℝ₊D, with D = Γ(B) + ½P₀₀, has an extreme ray outside the O(3)-orbit
  of the purifications at its marginal. U-weak must be reported FAIL.
- **C4 method countercontrol.** The zero-set nullspace for a non-extreme element, such as (B + P_{Ψ+})/2, must have
  dimension ≥ 2.
- **C5 identification.** Γ acts on token-2 Pauli coefficients as the y-reflection; Ad_{I⊗u} acts by a rotation.
- **C6 U-strong can fail and can pass.**
  - It must FAIL for at least one cone, with an exact witness;
  - it must PASS for Q3 and Γ(Q3).
- **C7 upstream replay.** The parent `p3_fixtures_op.py` output is byte-identical to its recorded digest
  `7d1d1db9…`.

Determinism: every probe runs twice, under `python3 -I -B`. Its stdout must be byte-identical across the two runs,
and `runs/SHA256SUMS` records the digests. Harness-error runs are kept, never deleted.
